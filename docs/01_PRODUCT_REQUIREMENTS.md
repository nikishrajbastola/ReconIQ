# ReconIQ — Product Requirements Document (PRD)
**Version:** 1.0 | **Status:** Demo MVP implemented | **Date:** October 19, 2026

## Executive summary
ReconIQ is a portfolio prototype for investment operations teams that need to reconcile internal trade books against external broker confirmations. It identifies common breaks, shows transaction-level evidence, prioritizes investigations, and records analyst workflow decisions.

## The problem
Trade-processing teams may receive fragmented records from multiple systems. Mismatched quantities, prices, gross amounts, dates, duplicates, and missing entries require investigation. The resulting handoffs create operational work and can obscure the source of discrepancies. **These are industry-informed hypotheses, not validated interview findings.**

## Personas / jobs to be done
1. **Operations analyst (primary):** When my reconciliation run completes, I need a ranked exception queue and source evidence so I can decide what to check next.
2. **Team lead (secondary):** When unresolved differences accumulate, I need aggregate exposure and ownership information to manage risk and workload.
3. **Product manager (stakeholder):** When choosing improvements, I need break-type trends and workflow evidence so I can prioritize roadmap investments.

## MVP scope (implemented)
- Upload internal and broker CSVs; validate required headers and numeric/date fields.
- Match by unique `trade_id`, compare quantity > price > amount > settle_date with clear precedence.
- Flag missing broker records, missing internal records, duplicate broker IDs, and field-level discrepancies.
- Rank exceptions by severity and estimated absolute difference.
- Review paired evidence; provide transparent rule-based potential causes and recommended checks.
- Assign one of three demo analysts; move through Open / Investigating / Resolved; record audit activity in demo memory.
- Operations dashboard with match rate, counts, absolute unresolved value and category breakdown.
- Filter and search exception queue, download sample CSVs, reset sample environment.

## Intentionally out of scope
Production authentication, multi-tenant permissions, real broker API integrations, persisted datastore, intraday settlement calendars, FX conversions, many-to-many matching, fuzzy matching, netting, instrument lifecycle events, AI/LLM integration, risk model, financial advice. **The prototype uses deterministic rule-based investigation guidance, not live AI.**

## User stories and acceptance criteria
**US01** As analyst, I can import two valid CSVs. **Given** each contains the required 10 columns and valid dates/numbers, **when** I upload, **then** the dashboard shows new counts; **given** a missing field, the system rejects it with a readable error.

**US02** As analyst, I can see mismatch categories. **Given** two trades share an ID and have different quantity, **when** reconciliation runs, **then** the trade is flagged as a quantity break with the quantity-adjusted difference.

**US03** As analyst, I can inspect evidence. **When** I open an exception, **then** I see internal vs broker quantity, price, amount, settlement date; mismatched fields are highlighted.

**US04** As analyst, I can record a disposition. **When** I update status/assignee/note, **then** it appears in Audit activity, and open-exception metrics update.

**US05** As team lead, I can prioritize. **Given** high absolute discrepancies, **when** I open the exception queue, **then** the initial ordering favors Critical, High, then Medium, followed by magnitude.

## Nonfunctional / limitations
- Python standard-library HTTP server designed for localhost demo only.
- CSV 3 MB each, up to 5,000 rows each. Fields validated, not encrypted at rest because nothing is stored long-term.
- Demo workflow state is server-process memory only, resets on restart.
- No production accounting guarantees; no automatic correction of source records.
- Dollar formatting assumes USD; source CSV currently does not include a currency field.
- Difference is a screening proxy and **not** P&L loss or confirmed economic exposure; potential duplicates and missing records can overstate economic impact.

## Success measurement plan (proposed, not proven)
- **Detection recall:** verified known anomalies found / all seeded known anomalies.
- **False positive rate:** clean transactions incorrectly flagged / all clean transactions.
- **Investigation task completion time:** median elapsed time in a controlled test vs manual spreadsheet workflow.
- **Review confidence:** analyst-rated trust in explanation and evidence (1–5).
- **Workflow completion:** percentage of exceptions with documented review decisions.

## Release acceptance gate
Engine and API unit tests pass; imported sample CSV reconciles identically; dashboard and queue populated; resolving one issue decreases the open count; audit entry records the change; empty/invalid files display appropriate errors. See tests and benchmark script.
