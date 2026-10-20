# 90-second demo — complete script and shot list
**Recording setup:** Start the app (README), browser zoom 85–90%, screen capture 1080p, use microphone, record full desktop/app. Don't claim any real customer usage or LLM intelligence.

**0:00–0:09 | Hero dashboard**
“Financial firms reconcile huge volumes of data across internal ledgers and broker records. But even a small discrepancy can send an analyst into a manual investigation. I built ReconIQ to organize that process.”

**0:09–0:23 | KPI cards and charts**
“This working prototype reconciles a synthetic investment portfolio. Here you can see how many trades were processed, how many matched automatically, and which exceptions require attention. All the numbers come from the matching engine—not a static mockup.”

**0:23–0:39 | Exception center, filter High and open a row**
“The queue surfaces quantity, price, amount, settlement, missing-trade and duplicate breaks. I can filter for urgent discrepancies, open an individual trade and inspect both source records side by side.”

**0:39–0:55 | Drawer, guidance section**
“ReconIQ also suggests what the analyst should check next, grounded in the detected break type. In this MVP those suggestions are explicitly rule-based. Core financial reconciliation stays deterministic and auditable.”

**0:55–1:08 | Assign status + note, save and go to Audit activity**
“I can assign the issue, record my investigation and update its status. The queue metrics change, and an audit event records the decision.”

**1:08–1:20 | Data sources, download**
“The product accepts two transaction CSV feeds and runs a new reconciliation locally. I intentionally used synthetic data and kept the engine independent of cloud APIs.”

**1:20–1:30 | Product insights, close**
“As a product manager, I also defined the PRD, user personas, competitive context, metrics and prioritized roadmap. Next, I'd validate the workflow with actual investment operations teams before expanding toward production integrations and grounded AI.”

## Fast shot sequence
1. Open `http://127.0.0.1:8080`; overview.
2. Click Exception center → filter `High` → click Review.
3. Scroll drawer to evidence and guidance; select `Investigating`, assignee `Avery Chen`, add note “Compared broker allocation against internal ledger; follow-up pending.” → Save.
4. Click Audit activity; show new entry.
5. Click Data sources; show both downloads and upload form.
6. Click Product insights; close on hero dashboard if desired.

## On-screen overlays (optional)
- “Deterministic matching | Human-in-the-loop review”
- “7 discrepancy types | Evidence-first investigation”
- “Synthetic data | Local MVP | No customer claims”

## Recording tips
Show cursor movement clearly and pause briefly on evidence comparison. Speak at ~125–140 words per minute. Rehearse once before final capture.
