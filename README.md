# ReconIQ

A polished, **runnable** financial reconciliation and exception triage app with an auditable demo workflow and full PM documentation. Made for an institutional-fintech product-management internship portfolio.

## Quick start (Windows / macOS / Linux)
1. Install **Python 3.10 or newer** from python.org (Windows: check "Add Python to PATH"). No `pip install` is required.
2. Extract ZIP. Open Terminal / PowerShell **inside the `ReconIQ` folder**.
3. Run:
   ```
   python app/server.py
   ```
   Windows alternative: `py app/server.py`.
4. Open **http://127.0.0.1:8080** in your web browser.
5. Run demo: Overview → Exception center → Review → change status/assignee and write note → Save → Audit activity → Data sources.
6. Stop the server with **Ctrl+C**. All workflow updates reset when the server stops.

> Use only nonconfidential synthetic data. This localhost prototype has no account permissions, encryption or production controls.

## Contents
- `app/`: Python reconciliation engine, standard-library API server and custom React-free HTML/CSS/JS interface.
- `data/`: repeatable example internal/broker CSV files.
- `docs/01_PRODUCT_REQUIREMENTS.md`: complete MVP PRD and acceptance criteria.
- `docs/02_MARKET_COMPETITIVE_RESEARCH.md`: vendor context, positioning, and interview questions.
- `docs/03_PM_CASE_STUDY.md`: product thesis, decisions, trade-offs and transparent results.
- `docs/04_ROADMAP_AND_PRIORITIZATION.md`: assumption-based RICE, now/next/later.
- `docs/05_METRICS_EXPERIMENT_PLAN.md`: North Star, evaluation and A/B-like usability study.
- `docs/06_LAUNCH_AND_GTM.md`: pitches, risks and launch plan.
- `docs/07_VIDEO_SCRIPT_AND_SHOT_LIST.md`: your exact 90-second video script and shot list.
- `docs/08_RESUME_AND_INTERVIEW.md`: application wording, resume bullets and Q&A.
- `tests/`: automated tests and measurable synthetic benchmark.
- `benchmark_results.json`: benchmark result from this package's local run.

## Implemented features
Local CSV upload/export, validation, trade-ID matching, field checks, duplicate detection, exception severity, KPI dashboard, a filterable exception list, side-by-side evidence, rule-based next-step guidance, assignment/status/note, audit log, demo reset and product-insight explanations.

## Key accuracy and scope limits
- **The default synthetic dataset intentionally injects lots of errors.** The match rate is not accuracy or a real-world customer result.
- **No LLM/AI is integrated.** Hypotheses are transparent rules; AI is in the *future roadmap*. Project name describes the target vision, not a shipped AI model.
- **Not financial advice, certified risk calculation or an enterprise-grade reconciliation system.** Differences are screening signals, not realized P&L.
- Single-user localhost app; no persisted database, authentication, real broker feeds or cloud deployment.
- Exact-ID, one-to-one matching and fixed evaluation order only. It doesn't account for partial trades/many-to-many reconciliation or complex instrument conventions.

## Developer & test commands
```
python -m unittest discover -s tests -v
python tests/benchmark.py
python app/server.py 8081
```

## Suggested video
Follow `docs/07_VIDEO_SCRIPT_AND_SHOT_LIST.md`. The user only needs to capture and narrate the demo.

## Source context
- https://www.arcesium.com/opterra
- https://www.arcesium.com/aquata-data-platform

**Attribution:** Independent portfolio learning project; not affiliated with or endorsed by Arcesium.

## NEW: Live AI investigation assistant

Open an exception and click **Generate evidence-backed AI investigation**. This now makes a genuine OpenAI Responses API call when `OPENAI_API_KEY` is configured. Results include validated `INT.*`, `BRK.*`, and `RECON.*` evidence-field citations; the previous rule-based guidance remains available. The feature is **not active until you provide your own API key**; no paid requests were run when this package was created. Read `docs/09_LIVE_AI_SETUP_AND_GUARDRAILS.md` for Windows/macOS/Linux instructions, safety and evaluation details.
