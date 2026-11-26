# Prototype — Tier-1 deflection agent (v0)

Four steps, one file each, as in `04_architecture.md`:

| Step | File | Suggested author (one commit each, own Git account) |
|---|---|---|
| 1 Router (TF-IDF + logistic regression) | `router.py` | member 1 |
| 2 Guard (rules) + 4 Policy check (rules) | `route_rule.py`, `policy.py` | member 2 |
| 3 Retrieve + draft | `retrieve.py`, `draft.py` | member 3 |
| Eval script and Streamlit surface | `evals.py`, `app.py` | member 4 |

Run (from the repo root):
```
pip install -r requirements.txt
python prototype/evals.py        # prints the numbers; writes evals/eval_output_v0.csv for the two graders
streamlit run prototype/app.py   # the inbox (demo tickets only, never the eval rows)
python prototype/test_switch.py "<your name>"   # rollback test: off / suggest-only / on, logged in data/switch_log.jsonl; exit 0 = passed
python evals/run_v1_fresh.py     # the one run on E51-E100 (already done on 20 Nov: do not re-run to tune)
```
Checked on 26 November 2026 with Python 3.14 and the versions of `requirements.txt`: `evals.py` gives the numbers of `evals/report_v0.md` (27 %), `test_switch.py` passes, the inbox runs (`screenshot_inbox_v1.0.png`).

| File added after Assignment 4 | What it does |
|---|---|
| `switch.py` | the override switch: `on` · `suggest_only` · `off`, state in `data/switch.json` (not tracked), read on every ticket, every change logged |
| `test_switch.py` | the rollback test of `06_07_experiments_operations.md` §4 (run on 16, 20 and 26 November) |
The template drafter is used (this is the mode of `evals/report_v0.md`). Never tune the router, the guard or the retrieval while looking at `evals/eval_set_v0.csv`.
