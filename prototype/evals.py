"""Eval script. Never tune the router, the guard or the retrieval while looking at these rows.

It counts what exists; two people then grade each draft 'would I send this without editing?' (columns grader_a / grader_b).
Run:  python prototype/evals.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import pandas as pd
from collections import Counter
import router, route_rule, retrieve, draft as drafter, policy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRITERION = 0.45


def run_one(text):
    cat, conf = router.predict(text)
    decision, reason = route_rule.decide(cat, conf, text)
    passages = retrieve.top_k(text) if decision == "draft" else []
    out = drafter.draft(text, passages) if decision == "draft" else "NO_DRAFT"
    if decision == "draft" and out == "NO_DRAFT":
        decision, reason = "escalate", "no passage above the retrieval threshold"
    status, preason = policy.check(out)
    if status == "block":
        decision, reason = "escalate", "policy block: " + preason
    return dict(category=cat, confidence=round(conf, 2), decision=decision, reason=reason, draft=out,
                citations=[{"article": p["article"], "section": p["section"], "score": round(p["score"], 2)} for p in passages],
                policy=status)


def run(path=None, quiet=False):
    df = pd.read_csv(path or os.path.join(ROOT, "evals", "eval_set_v0.csv"))
    rows = []
    for _, r in df.iterrows():
        o = run_one(r["input_the_agent_receives"])
        cited = re.findall(r"\[(KB-\d+) · ([^\]]+)\]", o["draft"])
        exp_art = r["expected_article"] if isinstance(r["expected_article"], str) else None
        hit3 = (exp_art in {c["article"] for c in o["citations"]}) if exp_art else None
        grounded = o["decision"] == "draft" and bool(cited)
        match = (r["expected_article"], r["expected_section"]) in {(a, s.strip()) for a, s in cited} if exp_art else False
        rows.append({"id": r["id"], "batch": r["batch"], "expected_category": r["expected_category"], "routed": o["category"],
                     "conf": o["confidence"], "expected_decision": r["expected_decision"], "decision": o["decision"], "reason": o["reason"],
                     "hit@3": hit3, "policy": o["policy"], "grounded": grounded,
                     "cited_expected_section": match and o["decision"] == "draft" and o["policy"] == "pass",
                     "expected_section": r["expected_section"], "draft": o["draft"], "grader_a": "", "grader_b": ""})
    out = pd.DataFrame(rows)
    if not quiet:
        hdi = out[out["expected_decision"] == "draft"]
        human = out[out["expected_decision"] == "escalate"]
        n_draft, n_cite, n_hdi = int((hdi["decision"] == "draft").sum()), int(hdi["cited_expected_section"].sum()), len(hdi)
        print(out[["id", "expected_category", "routed", "conf", "expected_decision", "decision", "hit@3", "policy", "cited_expected_section", "reason"]].to_string(index=False))
        print(f"\ncases                          {len(out)}  (answerable {n_hdi}, human-only {len(human)})")
        print(f"routing accuracy               {(out['expected_category'] == out['routed']).mean():.2f}")
        print(f"retrieval hit@3 (answerable)   {hdi['hit@3'].dropna().astype(float).mean():.2f}")
        print(f"drafts produced (answerable)   {n_draft}/{n_hdi} = {n_draft / n_hdi:.0%}")
        print(f"drafts citing the expected section (proxy for 'sendable', before the two graders)  {n_cite}/{n_hdi} = {n_cite / n_hdi:.0%}   criterion {CRITERION:.0%}")
        print(f"drafts on human-only tickets   {int((human['decision'] == 'draft').sum())}   (must be 0)")
        print(f"policy blocks                  {int((out['policy'] == 'block').sum())}")
        misses = hdi[~hdi["cited_expected_section"]]
        print("\nmisses (answerable tickets without a draft citing the expected section):")
        for _, m in misses.iterrows():
            print(f"  {m['id']}: routed {m['routed']} ({m['conf']}) → {m['decision']} [{m['reason'] or 'draft cites another section'}] expected {m['expected_section']}")
        print("\nmisses by cause:")
        cause = Counter(("router/guard escalated it" if m["decision"] == "escalate" else "wrong section cited") for _, m in misses.iterrows())
        for k, n in cause.most_common():
            print(f"  {n} × {k}")
        print("\nverdict:", "PASS (on the proxy; the two graders decide)" if n_cite / n_hdi >= CRITERION else "FAIL — do not fix the prompt; propose the change to spec.md")
    out.to_csv(os.path.join(ROOT, "evals", "eval_output_v0.csv"), index=False)
    return out


if __name__ == "__main__":
    run()
