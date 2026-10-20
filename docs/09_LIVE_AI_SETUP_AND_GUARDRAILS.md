# Live AI investigation assistant — setup & safety

## Turn on live AI (Windows)

1. Create an OpenAI API key at https://platform.openai.com/api-keys. API usage is billed separately from ChatGPT subscriptions.
2. Open PowerShell **in the extracted reconiq folder** and run:

   ```powershell
   $env:OPENAI_API_KEY = "YOUR_KEY_HERE"
   $env:OPENAI_MODEL = "gpt-4o-mini"
   python app/server.py
   ```

3. Visit http://127.0.0.1:8080 in your browser. Open an exception and click **Generate evidence-backed AI investigation**.
4. The dashboard shows the model name, possible root causes, confidence labels, follow-up checks, and field-specific citations. Hover over the green evidence citations to inspect exact source values.

For macOS / Linux:

```bash
export OPENAI_API_KEY='YOUR_KEY_HERE'
export OPENAI_MODEL='gpt-4o-mini'
python3 app/server.py
```

**Never** paste an API key into the browser, a CSV file, GitHub, or a video. Do not hardcode a key into source. The key stays in the local backend environment. Do not expose this demonstration server publicly: it has no authentication, account controls, API quotas, or request rate limiting.

## Architecture

- The deterministic matching engine computes the actual mismatched fields and numbers. The model never performs financial reconciliation or writes to trade records.
- `app/ai_investigator.py` composes a minimal case evidence bundle (`INT.quantity`, `BRK.quantity`, `RECON.difference`, etc.) and sends it to OpenAI's Responses API.
- `text.format` uses a strict JSON schema for a consistent investigation report. The backend rejects any returned evidence IDs not present in the submitted bundle.
- The UI shows exactly which field and value supports each model-generated hypothesis/action. These are **field citations**, not citations to external confirmations.
- All causes are marked as hypotheses. Missing proof is explicitly requested. A human must verify any real-world action.
- The assistant never changes a trade or closes an exception. Analysts retain full control of existing workflow state.
- Model input is limited to the current case and minimal fields; API request uses `store:false`. **Never upload real client or proprietary financial data without permission and appropriate security/compliance review.**

## Caveats to mention in interview

- A citation proves the cited field appeared in the provided record; it **does not prove an inferred root cause**. Field-level grounding and citation validation reduce, but do not eliminate, hallucinations.
- Model confidence is qualitative and not calibrated. Do not claim that the confidence labels are statistical probabilities.
- This feature requires internet connectivity, a working API key, account API access and available API billing.
- Testing uses mocked AI responses; no paid live API request was made during packaging because the user's key was not available.
- The local server is a prototype; production would require authentication, private storage, logging controls, input validation, security testing, and separate permissions for sensitive customer data.

## Evaluation plan

Create a labeled synthetic test set of exception root causes. Measure citation validity, hypothesized cause top-1 accuracy, action utility (rated by a domain expert), hallucination rate, refusal behavior, latency, and cost per investigation. Compare LLM mode to the deterministic rule-based baseline and include realistic unknown-cause examples.

## Troubleshooting

- “Live AI is not configured”: define `OPENAI_API_KEY` **in the same terminal session** before starting the server.
- “Invalid API key”: regenerate/verify your key in your API account.
- “API rate limit or quota exceeded”: check API credits, quotas, and billing.
- “AI response failed evidence validation”: model output was rejected instead of displaying unverified citations; retry, or use rule-based guidance.
