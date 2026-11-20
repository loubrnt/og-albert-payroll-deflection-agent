"""Runs the prototype ONCE on the 50 new rows of eval_set_v1.csv (E51-E100, batch a5), whose labels were frozen before
this run (evals/LABELS_FROZEN.txt). Same counting as prototype/evals.py; nothing is tuned.
Writes evals/eval_output_v1_fresh.csv. Run from the repo root:  python evals/run_v1_fresh.py
"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "prototype"))
import pandas as pd
import evals as E

df = pd.read_csv(os.path.join(ROOT, "evals", "eval_set_v1.csv"))
df = df[df["batch"] == "a5"]
rows = []
for _, r in df.iterrows():
    o = E.run_one(r["input_the_agent_receives"])
    cited = re.findall(r"\[(KB-\d+) · ([^\]]+)\]", o["draft"])
    exp_art = r["expected_article"] if isinstance(r["expected_article"], str) else None
    match = exp_art is not None and (r["expected_article"], r["expected_section"]) in {(a, s.strip()) for a, s in cited}
    rows.append({"id": r["id"], "segment": r["segment"], "expected_category": r["expected_category"], "routed": o["category"], "conf": o["confidence"],
                 "expected_decision": r["expected_decision"], "decision": o["decision"], "reason": o["reason"],
                 "hit@3": (exp_art in {c["article"] for c in o["citations"]}) if exp_art else None, "policy": o["policy"],
                 "cited_expected_section": bool(match and o["decision"] == "draft" and o["policy"] == "pass"),
                 "expected_article": exp_art or "", "expected_section": r["expected_section"] if exp_art else "", "draft": o["draft"],
                 "grader_a": "", "grader_b": ""})
out = pd.DataFrame(rows)
out.to_csv(os.path.join(ROOT, "evals", "eval_output_v1_fresh.csv"), index=False)
ans, hum = out[out.expected_decision == "draft"], out[out.expected_decision == "escalate"]
print(f"cases {len(out)} (answerable {len(ans)}, person only or no article {len(hum)})")
print(f"routing accuracy {(out.expected_category == out.routed).mean():.0%}")
print(f"drafts produced on answerable {int((ans.decision == 'draft').sum())}/{len(ans)}")
print(f"drafts citing the expected section (proxy) {int(ans.cited_expected_section.sum())}/{len(ans)} = {ans.cited_expected_section.mean():.0%}  criterion 45%")
print(f"retrieval hit@3 on answerable {ans['hit@3'].astype(float).mean():.0%}")
print(f"drafts on tickets that must not get one {int((hum.decision == 'draft').sum())}  (must be 0): {', '.join(hum[hum.decision == 'draft'].id)}")
print(f"policy blocks {int((out.policy == 'block').sum())}")
for seg in ["en", "fr"]:
    s = ans[ans.segment.str.startswith(seg)]
    print(f"  proxy {seg}: {int(s.cited_expected_section.sum())}/{len(s)}")
print("misses on answerable:")
for _, m in ans[~ans.cited_expected_section].iterrows():
    print(f"  {m.id} [{m.segment}] routed {m.routed} ({m.conf}) -> {m.decision} [{m.reason or 'cites another section'}] expected {m.expected_article} · {m.expected_section}")
print("drafts on must-not tickets:")
for _, m in hum[hum.decision == "draft"].iterrows():
    print(f"  {m.id} [{m.expected_category}] {m.draft[:160]}")
