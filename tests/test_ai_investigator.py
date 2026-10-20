import unittest, sys, json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'app'))
from engine import build_data,reconcile
from ai_investigator import evidence_bundle,investigate,InvestigationError

class AITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        a,b=build_data();cls.exc=reconcile(a,b)['exceptions'][0]
    def sample(self,source='INT.quantity'):
        return {'output':[{'content':[{'type':'output_text','text':json.dumps({
            'summary':'Observed quantity discrepancy.',
            'hypotheses':[{'cause':'Possible allocation discrepancy','why':'Quantity differs.','citations':[source],'confidence':'low'}],
            'recommended_actions':[{'action':'Confirm allocations','reason':'Records disagree','citations':['RECON.kind']}],
            'missing_evidence':['Execution report'],
            'limitations':'Unconfirmed hypothesis'})}]}]}
    def test_evidence_ids(self):
        ids=[e['id'] for e in evidence_bundle(self.exc)]
        self.assertIn('RECON.kind',ids)
        self.assertIn('INT.quantity',ids)
        self.assertEqual(len(ids),len(set(ids)))
    def test_valid_model_output(self):
        response=investigate(self.exc,transport=lambda body:self.sample())
        self.assertEqual(response['mode'],'live_ai')
        self.assertEqual(response['analysis']['hypotheses'][0]['citations'],['INT.quantity'])
    def test_invalid_citation_rejected(self):
        with self.assertRaisesRegex(InvestigationError,'evidence validation'):
            investigate(self.exc,transport=lambda body:self.sample('INVENTED.confirmation'))
    def test_missing_api_key(self):
        with self.assertRaisesRegex(InvestigationError,'not configured'):
            investigate(self.exc,key='')
    def test_missing_citations(self):
        data=self.sample(); body=json.loads(data['output'][0]['content'][0]['text'])
        body['hypotheses'][0]['citations']=[]
        data['output'][0]['content'][0]['text']=json.dumps(body)
        with self.assertRaises(InvestigationError):
            investigate(self.exc,transport=lambda request:data)
    def test_absent_record(self):
        a,b=build_data(); r=reconcile(a,b)
        missing=next(x for x in r['exceptions'] if x['kind']=='missing_broker')
        ids=[e['id'] for e in evidence_bundle(missing)]
        self.assertIn('BRK.record_absent',ids)

if __name__=='__main__': unittest.main()
