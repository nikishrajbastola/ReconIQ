# Lean launch, positioning and stakeholder plan
## Positioning statement
For investment operations teams dealing with cross-system trade mismatches, ReconIQ is an **evidence-first exception triage prototype** that unifies deterministic discrepancy detection, prioritization, review guidance and an audit workflow. Unlike a generic dashboard, it connects the source-level break to a next investigation action. Competitive advantage remains **unvalidated**.

## 30-second pitch
“Investment firms process trade records across internal systems and external brokers. When figures disagree, analysts need to determine what's wrong and what to investigate first. I built ReconIQ, a functioning portfolio prototype that reconciles two trade feeds, identifies seven break classes, prioritizes differences and provides auditable exception handling. I also created its PRD, prioritization strategy and a research plan for validating whether evidence-first workflows improve analyst productivity.”

## Packaging for a hiring manager
- README first, then 90-second walkthrough.
- Show two source feed CSVs, the dashboard, a flagged quantity mismatch, evidence comparison, disposition update, and audit record.
- Explain the technical guardrail: deterministic logic for finance; advisory guidance for next steps.
- Show what you would test before treating the product as enterprise-ready.

## Stakeholders and launch risks
- Operations lead: matching logic and severity rubric review.
- Engineer: CSV schema, error handling, performance tests, persistence plan.
- Risk/compliance: read-only principle, auditability, role access, retention.
- Sales/strategy: segment assumptions, buyer objections, positioning.

## Example launch checklist (pilot, NOT shipped)
- Interview actual users and document workflows.
- Validate instrument precision and currency-specific accounting requirements.
- Threat model, auth/RBAC, encrypted storage, incident runbook.
- Integration contracts and E2E test suite.
- Measure latency, reconciliation correctness and operator overrides.
- Legal/privacy approval before real financial data ingestion.
