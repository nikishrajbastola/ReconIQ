"""ReconIQ local demo server. Run: python app/server.py"""
import json, sys, csv, io, os
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs
sys.path.insert(0,str(Path(__file__).parent))
from engine import build_data,reconcile,parse_csv
from ai_investigator import investigate,InvestigationError
ROOT=Path(__file__).parent; DATA=ROOT.parent/'data'; internal,external=build_data(); result=reconcile(internal,external);audit=[]
class Handler(BaseHTTPRequestHandler):
    def send(self,body,status=200,ctype='application/json'):
        data=body.encode() if isinstance(body,str) else body
        self.send_response(status); self.send_header('Content-Type',ctype+'; charset=utf-8');self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
    def reply(self,obj,status=200): self.send(json.dumps(obj,default=str),status)
    def do_GET(self):
        global result
        path=urlparse(self.path).path
        if path=='/': path='/index.html'
        if path=='/api/ai/status': self.reply({'enabled':bool(os.getenv('OPENAI_API_KEY')),'model':os.getenv('OPENAI_MODEL','gpt-4o-mini') if os.getenv('OPENAI_API_KEY') else None});return
        if path=='/api/summary':
            ex=result['exceptions'];active=[e for e in ex if e['status']!='Resolved']; self.reply({**{k:v for k,v in result.items() if k!='exceptions'},'exception_count':len(active),'unresolved_value':round(sum(abs(e['difference']) for e in active),2),'resolved':len(ex)-len(active),'audit_count':len(audit),'recent':ex[:7]});return
        if path=='/api/exceptions': self.reply(result['exceptions']);return
        if path=='/api/audit': self.reply(audit[::-1]);return
        if path=='/api/records': self.reply({'internal':internal[:1000],'external':external[:1000]});return
        if path=='/api/download/internal' or path=='/api/download/external':
            records=internal if path.endswith('internal') else external
            out=io.StringIO();writer=csv.DictWriter(out,fieldnames=list(records[0].keys()));writer.writeheader();writer.writerows(records);self.send(out.getvalue(),ctype='text/csv');return
        name=path.lstrip('/');file=(ROOT/name).resolve()
        if file.parent==ROOT and file.is_file() and file.suffix in ('.html','.css','.js','.svg'):
            ct={'.html':'text/html','.css':'text/css','.js':'application/javascript','.svg':'image/svg+xml'}[file.suffix];self.send(file.read_bytes(),ctype=ct);return
        self.reply({'error':'Not found'},404)
    def do_POST(self):
        global internal,external,result,audit
        path=urlparse(self.path).path
        length=int(self.headers.get('Content-Length','0'))
        if length>7_000_000: self.reply({'error':'Request too large'},413);return
        try: obj=json.loads(self.rfile.read(length) or b'{}')
        except Exception: self.reply({'error':'Invalid JSON'},400);return
        if path=='/api/ai/investigate':
            exc=next((x for x in result['exceptions'] if x['id']==obj.get('id')),None)
            if exc is None: self.reply({'error':'Exception not found'},404);return
            try: self.reply(investigate(exc))
            except InvestigationError as e: self.reply({'error':str(e)},503)
            except Exception: self.reply({'error':'Unexpected AI provider error. Check server configuration.'},502)
            return
        if path=='/api/update':
            e=next((x for x in result['exceptions'] if x['id']==obj.get('id')),None)
            if e is None: self.reply({'error':'Exception not found'},404);return
            status=obj.get('status',e['status']);assignee=obj.get('assignee',e['assignee']);note=str(obj.get('note','')).strip()[:500]
            if status not in ('Open','Investigating','Resolved') or assignee not in ('Unassigned','Avery Chen','Jordan Lee','Morgan Patel'):
                self.reply({'error':'Invalid status or assignee'},400);return
            e['status']=status;e['assignee']=assignee
            audit.append({'event_id':len(audit)+1,'exception_id':e['id'],'trade_id':e['trade_id'],'status':status,'assignee':assignee,'note':note or 'Workflow state updated','actor':'Demo Analyst','timestamp':'2026-10-19 (demo simulated)'})
            self.reply({'ok':True,'item':e});return
        if path=='/api/reset': internal,external=build_data();result=reconcile(internal,external);audit=[];self.reply({'ok':True});return
        if path=='/api/upload':
            try:
                a=parse_csv(obj.get('internal_csv',''));b=parse_csv(obj.get('external_csv',''))
                if not a or not b: raise ValueError('Both CSVs must contain at least one record')
                r=reconcile(a,b)
                internal,external,result,audit=a,b,r,[];self.reply({'ok':True,'total':len(a),'exceptions':len(r['exceptions'])})
            except (ValueError,TypeError) as e: self.reply({'error':str(e)},400)
            return
        self.reply({'error':'Not found'},404)
if __name__=='__main__':
    host='127.0.0.1';port=int(sys.argv[1]) if len(sys.argv)>1 else 8080
    print(f'\n ReconIQ running at http://{host}:{port}\n Press Ctrl+C to stop.\n')
    ThreadingHTTPServer((host,port),Handler).serve_forever()
