"""Runs the prototype ONCE on the 30 golden rows of eval_set_v1.csv and writes evals/grading_sheet_v1.csv for the graders.

The golden rows are fixed by position, before any run: in eval_set_v1.csv, the rows whose position (0-based) modulo 10 is 1, 4 or 8.
The prototype is not changed and not tuned here. Run from the repo root:  python evals/make_grading_sheet.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "prototype"))
import pandas as pd
import evals as E

ROOT = E.ROOT
df = pd.read_csv(os.path.join(ROOT, "evals", "eval_set_v1.csv"))
gold = df[[i % 10 in (1, 4, 8) for i in range(len(df))]]
rows = []
for _, r in gold.iterrows():
    o = E.run_one(r["input_the_agent_receives"])
    rows.append({"id": r["id"], "segment": r["segment"], "ticket": r["input_the_agent_receives"], "decision": o["decision"], "reason": o["reason"],
                 "citations": "; ".join(f"{c['article']} · {c['section']}" for c in o["citations"]), "output": o["draft"],
                 "grader_a": "", "grader_b": "", "judge": ""})
pd.DataFrame(rows).to_csv(os.path.join(ROOT, "evals", "grading_sheet_v1.csv"), index=False)
print(len(rows), "rows written to evals/grading_sheet_v1.csv")
