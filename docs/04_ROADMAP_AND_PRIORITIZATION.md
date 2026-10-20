# Product roadmap and prioritization
**Assumption-based RICE scores**, not observations. Scale: reach = targeted users per quarter; impact = 0.25/0.5/1/2/3; confidence = 0–1; effort = person-months. Use scores to force trade-off conversations, not to manufacture certainty.

| Feature | Reach | Impact | Confidence | Effort | RICE | Phase |
|---|---:|---:|---:|---:|---:|---|
| Exact matching + exception triage | 20 | 3 | 0.80 | 1.5 | 32.0 | Shipped MVP |
| Evidence comparison + audit actions | 20 | 2 | 0.75 | 1.0 | 30.0 | Shipped MVP |
| Feed completeness / stale-feed monitors | 20 | 2 | 0.55 | 1.5 | 14.7 | Next |
| Persisted users / roles / approvals | 20 | 2 | 0.70 | 2.5 | 11.2 | Next |
| One-to-many trade matching / tolerance rules | 15 | 3 | 0.60 | 2.5 | 10.8 | Next |
| Evidence-grounded LLM assistant | 15 | 2 | 0.40 | 3.0 | 4.0 | Later gated pilot |
| Live broker integrations | 15 | 2 | 0.50 | 4.0 | 3.8 | Later |

## Now: working MVP
Prove mechanics: matching, exceptions, evidence display, dashboard, local CSV data ingestion, analyst workflow.

## Next: pilot readiness (proposed 6–10 weeks)
- Move data from memory to a database; append-only audit, SSO, RBAC, encryption and access control.
- Implement validated per-security normalization, fee treatment, currencies and holidays.
- Add one-to-many matching and configurable tolerances; expand correctness tests.
- Run 5–8 discovery interviews; collect issue severity rubric and measure task completion.

## Later: enterprise integrations and AI (conditional)
- Broker/custodian adapters; feed monitoring and exception SLA notifications.
- LLM-assisted investigation only when grounding, confidentiality and audit controls pass.
- Evaluation suite: factuality vs source evidence, unsafe suggestions, false confidence, operator correction rate.

## Go/no-go metrics for a pilot
- 100% deterministic unit test pass; anomaly recall/precision on a labeled test set.
- Explicit human confirmation prior to posting corrections.
- No exposure of cross-customer or confidential source data.
- Analyst task completion measurement compared to a manual baseline, with consent.
