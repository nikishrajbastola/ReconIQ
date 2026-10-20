import sys,json,time,statistics
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'app'))
from engine import build_data,reconcile
runs=[]
for size in (420,1000,5000):
 a,b=build_data(size);samples=[]
 for _ in range(9):
  t=time.perf_counter();r=reconcile(a,b);samples.append((time.perf_counter()-t)*1000)
 runs.append({'internal_rows':size,'external_rows':len(b),'median_reconciliation_ms':round(statistics.median(samples),3),'min_ms':round(min(samples),3),'max_ms':round(max(samples),3),'matched':r['matched'],'exceptions':r['exception_count'],'trials':len(samples)})
out={'hardware_note':'Local container environment; wall-clock timing includes Python processing only; not browser/network; not enterprise production benchmark','dataset':'Reproducible synthetic generator, seed=42','runs':runs}
p=Path(__file__).resolve().parents[1]/'benchmark_results.json';p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
