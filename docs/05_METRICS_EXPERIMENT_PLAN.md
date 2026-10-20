# Metrics specification and experiment plan
## North-star candidate
**Verified exceptions resolved per analyst-hour** — requires time tracking and independent validation; not currently measured.

## Leading indicators
- Auto-match rate = matched internal trades / total internal trades. Not equivalent to model accuracy.
- Break detection recall and precision (requires labeled truth set).
- Median time-to-first-review and time-to-resolution (requires timestamps, currently unavailable).
- Investigation coverage = exceptions with reviewed evidence / total exceptions.
- Assignment backlog and SLA breach rate (future production metrics).

## Demonstration-only metrics
Default seed 42 and 420 internal records produces 306 auto-matches and 118 exception records. Some duplicate break IDs count as one exception per affected internal trade; unmatched external records produce independent exceptions. Open counts change when analyst disposition is saved. The “unreconciled value” sums absolute difference estimates and MUST NOT be interpreted as actual financial losses.

## Proposed experiment: evidence-first workflow
- **Research question:** Does source comparison + guided next step reduce analyst investigation time vs a plain CSV comparison?
- **Hypothesis:** analysts complete identical predefined exception investigations faster and with similar or better correctness.
- **Participants:** 8–12 experienced analysts, recruited and consented; within-subject crossover randomized by task/order.
- **Materials:** identical synthetic scenarios; both views use same underlying records.
- **Outcome:** median successful completion time; secondary = correctness, confidence, error types and subjective effort.
- **Analysis:** report per-participant paired differences, confidence intervals and limitations; do not claim statistical significance from tiny samples.
- **Guardrails:** no real trades, no execution actions, no confidential records.
- **Decision:** invest further if time improves and error rate doesn't deteriorate; otherwise revisit explanation quality and prioritization UX.

## Instrumentation to build next
Events: `reconciliation_started`, `reconciliation_completed`, `exception_opened`, `evidence_expanded`, `assignee_changed`, `resolution_saved`, `resolution_reopened`, `upload_error`. Include timestamp and anonymized session ID; privacy review before actual collection.
