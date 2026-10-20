"""Deterministic synthetic data and auditable reconciliation engine (stdlib only)."""
import csv, io, json, random, hashlib
from datetime import date, timedelta
from collections import Counter

SECURITIES=[('AAPL','Apple Inc.'),('MSFT','Microsoft'),('NVDA','NVIDIA'),('AMZN','Amazon'),('GOOGL','Alphabet'),('JPM','JPMorgan'),('TSLA','Tesla'),('META','Meta'),('BRK.B','Berkshire')]
CUSTODIANS=['Northern Trust','State Street','BNY Mellon','Citi Custody']
BROKERS=['Goldman Sachs','Morgan Stanley','J.P. Morgan','UBS']
CAUSES={'quantity':'Partial fill or allocation discrepancy','price':'Execution price or booking discrepancy','amount':'Fee, FX, or cash adjustment discrepancy','missing_broker':'Trade missing from broker feed','missing_internal':'Unbooked external trade','duplicate':'Possible duplicate posting','settlement':'Settlement-date difference'}

def build_data(n=420,seed=42):
    rng=random.Random(seed); internal=[]; external=[]; start=date(2026,10,1)
    for i in range(n):
        sym,_=rng.choice(SECURITIES); qty=rng.randint(10,800)*10; price=round(rng.uniform(40,700),2); day=(start+timedelta(days=rng.randrange(13))).isoformat(); settle=(date.fromisoformat(day)+timedelta(days=2)).isoformat()
        base={'trade_id':f'TRD-{10000+i}','security':sym,'side':rng.choice(['BUY','SELL']),'quantity':qty,'price':price,'amount':round(qty*price,2),'trade_date':day,'settle_date':settle,'counterparty':rng.choice(BROKERS),'custodian':rng.choice(CUSTODIANS)}
        internal.append(dict(base)); other=dict(base)
        mod=i%23
        if mod==0: other['quantity']=max(1,qty-50); other['amount']=round(other['quantity']*price,2)
        elif mod==1: other['price']=round(price+0.85,2); other['amount']=round(qty*other['price'],2)
        elif mod==2: other['amount']=round(base['amount']+125.0,2)
        elif mod==3: continue
        elif mod==4: other['settle_date']=(date.fromisoformat(settle)+timedelta(days=1)).isoformat()
        external.append(other)
        if mod==5: external.append(dict(other))
    for k in range(max(3,n//90)):
        sym,_=rng.choice(SECURITIES); qty=100+k*20; price=round(90.5+k*11,2)
        external.append({'trade_id':f'EXT-{9900+k}','security':sym,'side':'BUY','quantity':qty,'price':price,'amount':round(qty*price,2),'trade_date':'2026-10-11','settle_date':'2026-10-13','counterparty':'Goldman Sachs','custodian':'BNY Mellon'})
    return internal,external

def reconcile(internal,external):
    idx={}; duplicates=set()
    for row in external:
        key=row['trade_id']; idx.setdefault(key,[]).append(row)
        if len(idx[key])>1: duplicates.add(key)
    exceptions=[]; matched=0; seen=set(); issues=Counter()
    def add(key,kind,a,b,diff,priority):
        evidence={'internal':a,'external':b}
        exc={'id':f'EX-{len(exceptions)+1:04d}','trade_id':key,'security':(a or b or {}).get('security','UNKNOWN'),'kind':kind,'category':kind.replace('_',' ').title(),'severity':priority,'difference':round(float(diff),2),'internal':a,'external':b,'status':'Open','assignee':'Unassigned','evidence':evidence,'hypothesis':CAUSES[kind],'next_action':ACTION[kind]}
        exceptions.append(exc);issues[kind]+=1
    for a in internal:
        key=a['trade_id'];seen.add(key);items=idx.get(key,[])
        if not items:
            add(key,'missing_broker',a,None,a['amount'],'High');continue
        b=items[0]
        if key in duplicates:
            add(key,'duplicate',a,b,b['amount'],'High');continue
        kind=None; diff=0
        if int(a['quantity'])!=int(b['quantity']): kind='quantity';diff=(int(a['quantity'])-int(b['quantity']))*float(a['price'])
        elif abs(float(a['price'])-float(b['price']))>0.01: kind='price';diff=a['amount']-b['amount']
        elif abs(float(a['amount'])-float(b['amount']))>0.01: kind='amount';diff=a['amount']-b['amount']
        elif a['settle_date']!=b['settle_date']: kind='settlement';diff=0
        if kind:
            prio='Critical' if abs(diff)>25000 else 'High' if abs(diff)>2000 or kind=='duplicate' else 'Medium'
            add(key,kind,a,b,diff,prio)
        else: matched+=1
    for key,items in idx.items():
        if key not in seen:
            for b in items: add(key,'missing_internal',None,b,b['amount'],'High')
    exceptions.sort(key=lambda e:({'Critical':0,'High':1,'Medium':2,'Low':3}[e['severity']],-abs(e['difference'])))
    for i,e in enumerate(exceptions): e['id']=f'EX-{i+1:04d}'
    total=len(internal); return {'total':total,'matched':matched,'match_rate':round(100*matched/total,1) if total else 0,'exception_count':len(exceptions),'unresolved_value':round(sum(abs(x['difference']) for x in exceptions),2),'breakdown':dict(issues),'exceptions':exceptions}

ACTION={'quantity':'Verify partial executions and allocation statements; confirm correct quantity with counterparty.','price':'Compare broker execution confirmation and internal booking price; request correction approval.','amount':'Review transaction fees and FX adjustments; reconcile cash postings.','missing_broker':'Check broker feed completeness and execution confirmation before escalating.','missing_internal':'Verify external execution and locate missing internal booking.','duplicate':'Inspect duplicate broker feed records and request confirmation before excluding entries.','settlement':'Compare venue settlement calendar and booking instructions; confirm settlement date.'}
REQUIRED=['trade_id','security','side','quantity','price','amount','trade_date','settle_date','counterparty','custodian']
def parse_csv(content):
    if len(content)>3_000_000: raise ValueError('CSV exceeds 3 MB limit')
    reader=csv.DictReader(io.StringIO(content)); fields=reader.fieldnames or []
    missing=set(REQUIRED)-set(fields)
    if missing: raise ValueError('Missing columns: '+', '.join(sorted(missing)))
    rows=[]
    for i,row in enumerate(reader):
        if i>=5000: raise ValueError('Maximum 5,000 rows per file')
        try:
            obj={k:str(row[k]).strip() for k in REQUIRED}
            obj['quantity']=int(obj['quantity']);obj['price']=float(obj['price']);obj['amount']=float(obj['amount'])
            if not obj['trade_id'] or obj['quantity']<=0 or obj['price']<0: raise ValueError('Invalid trade field')
            date.fromisoformat(obj['trade_date']);date.fromisoformat(obj['settle_date'])
        except (ValueError,TypeError,KeyError) as e: raise ValueError(f'Row {i+2}: {e}')
        rows.append(obj)
    return rows

if __name__=='__main__':
    a,b=build_data();r=reconcile(a,b);print(json.dumps({k:v for k,v in r.items() if k!='exceptions'},indent=2))
