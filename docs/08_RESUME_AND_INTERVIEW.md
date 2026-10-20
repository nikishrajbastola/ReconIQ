# Resume bullets, application paragraph and interviews
## Resume project entry (use after running app and confirming it works)
**ReconIQ — Financial Reconciliation & Exception Intelligence Platform** | Python, JavaScript, REST API, product strategy
- Built an interactive institutional-fintech prototype that compares internal ledger and broker trade records, detecting seven discrepancy categories with transparent rule-based logic and source-level evidence.
- Implemented CSV ingestion/validation, exception prioritization, operations KPIs, analyst assignment, resolution workflows and audit event tracking.
- Created a PRD, competitive desk-research brief, assumption-based RICE roadmap, discovery interview plan and experiment design to evaluate investigation efficiency.
- Benchmarked the deterministic reconciliation engine on labeled synthetic input; documented accuracy, system boundaries and production-readiness trade-offs. **Include this last bullet only after running the benchmark and checking its output.**

## Application short answer
“I built ReconIQ, a functional prototype that investigates reconciliation breaks between investment firms' internal trading records and broker confirmations. Beyond engineering the matching engine, I wrote its PRD, prioritized roadmap, customer discovery plan, experiment strategy and competitive positioning. The project sharpened my understanding of the product decisions behind data-heavy financial operations: explainability, data quality, exception workflows, auditability and practical trade-offs.”

## Interview questions and talking points
**Why this product?** Arcesium's public Opterra/Aquata offerings work in adjacent data and operations domains; I wanted hands-on product fluency rather than a generic trading app.

**How did you prioritize?** Trustworthy matching and source evidence first, then triage and audit. Deferred AI, real broker integrations and hosting until validation, correctness and security gates.

**What is innovative?** Not the recon category itself; the demo focuses on an accessible, complete evidence-to-resolution workflow with explicit human oversight.

**How would you measure success?** Paired controlled task studies: successful exceptions resolved per analyst-hour plus correctness and reviewer confidence.

**What would you improve?** Persistent database, one-to-many matching, currencies, calendar/fee handling, SSO/RBAC and independently evaluated AI summaries.

**What research have you done?** Public vendor desk research and persona hypotheses; user interviews are planned, not yet performed.

**Did you use AI in the product?** No. Offline MVP guidance is deterministic; LLM integration is a proposed feature, not shipped. Be transparent.

**Does this replicate Arcesium?** No. It is an educational prototype of a subset of reconciliation workflows, not a comparison of enterprise breadth or capability.
