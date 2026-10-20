# ReconIQ — Product Management Case Study
## Problem framing
Investment operations reconcile internal and broker transaction records. Even when most records align, differences in quantity, price, amount, settlement date or feed completeness generate investigative work. Which differences should receive attention first, and can analysts understand the underlying data without repeated manual lookups?

## Product thesis
An exception-focused workflow with visible evidence and auditable decisions could reduce investigative friction. The correct starting point is reliable deterministic matching; LLM narratives are optional and must never be treated as source-of-truth financial calculations.

## Target user / jobs
Primary: investment operations analyst. Secondary: operations lead. See `01_PRODUCT_REQUIREMENTS.md`.

## MVP trade-offs
1. **Trade-ID exact matches over fuzzy matches:** easiest to test and explain, lower false-positive risk, but won't match ID-transformed executions.
2. **Source evidence over ungrounded AI:** rule-based suggestions are less sophisticated than agentic AI, but reliable and demonstrable offline.
3. **Local server over hosted SaaS:** easy zero-cost reviewer setup, but no customer-ready identity, security, or persistent storage.
4. **Synthetic data over real investment data:** zero privacy risk and repeatable tests, but no verified production-like distribution or user outcomes.

## What shipped
Runnable Python engine + HTTP API + dark institutional dashboard. Features: import/export CSV, per-trade reconciliation, seven exception classes, portfolio metrics, search/filter queue, investigation comparison, assign/status/note and audit log. See root README.

## Results — clearly labeled
The default seeded **synthetic** demo contains 420 internal trades and, on clean launch, produces 306 auto-matched trades (72.9%) and 118 exceptions under the stated exception-count convention. These are deliberately injected anomalies, NOT performance claims for actual customers. Runtime benchmark results are in `benchmark_results.json` after executing the benchmark script.

## What surprised us? (engineering observation, not user research)
Naively equating sum(abs(amount differences)) with financial loss is misleading: missing records and duplicates are triage estimates, not realized loss. The dashboard therefore labels it **gross absolute unreconciled exposure (not P&L)**.

## Risks and mitigations
- Incorrect automatic matching → require deterministic source-level rules, add an exception review queue.
- Duplicate and absent trades overstate risk → label difference as a proxy, do not call it realized loss.
- Over-trusting explanations → display “potential cause” and manual verification action; no automatic ledger changes.
- Sensitive information → use synthetic data only; prohibit production data in prototype.
- Unverified product-market fit → interview target users before claiming ROI.

## Product decision framework
Prioritize first-run correctness and user trust. Later add persisted evidence, one-to-many matching, SLA policies, feed integrations and gated AI assistance based on structured, cited transaction facts.

## Why this maps to Arcesium PM responsibilities
- **Customer-needs analysis:** problem, personas, interview plan, jobs-to-be-done.
- **Engineering collaboration:** API/engine design, constraints and product trade-offs.
- **Competitive research:** real adjacent products and defensible positioning hypothesis.
- **Strategic prioritization:** RICE roadmap and metrics.
- **Communication:** product narrative, live demo, brief, artifact package.

## Honest interview framing
Say: “I built a functional local prototype with deterministic matching, synthetic data, rule-based investigation guidance and an audit workflow. I also drafted a discovery plan and a roadmap for production-grade integrations and AI. I haven't done customer validation or deployed it to production.”
