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
```
The template drafter is used (this is the mode of `evals/report_v0.md`). Never tune the router, the guard or the retrieval while looking at `evals/eval_set_v0.csv`.
