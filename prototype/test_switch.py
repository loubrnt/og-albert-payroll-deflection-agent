"""Rollback test (06_07_experiments_operations.md §4): switch the agent off, check that the next 5 tickets go to the human queue
with the reason "agent off", try the suggest-only position, switch back on, check that the pipeline runs again.
Every change is logged in data/switch_log.jsonl (that file is the evidence of the test date).

Run from the repo root, on the laptop that is our staging:   python prototype/test_switch.py "<who runs it>"
Exit code 0 = test passed.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(__file__))
import pandas as pd
import switch

who = sys.argv[1] if len(sys.argv) > 1 else "unknown"
tickets = pd.read_csv(os.path.join(switch.ROOT, "data", "demo_tickets.csv"))["text"].tolist()[:5]
assert len(tickets) == 5, "need 5 demo tickets"
before = switch.status()

t0 = time.perf_counter()
switch.set_state("off", who, "rollback test: switch off")
res_off = [switch.run_ticket(t) for t in tickets]
elapsed = time.perf_counter() - t0
off_ok = all(r["decision"] == "escalate" and r["reason"] == "agent off" and r["draft"] == "NO_DRAFT" for r in res_off)

switch.set_state("suggest_only", who, "rollback test: suggest-only position")
sugg_ok = all(r.get("suggest_only") is True for r in (switch.run_ticket(t) for t in tickets))

switch.set_state("on", who, "rollback test: back on")
on_ok = all(r["reason"] != "agent off" for r in (switch.run_ticket(t) for t in tickets))

print(f"off: the next 5 tickets went to the human queue with the reason 'agent off': {off_ok} (switched off and 5 tickets handled in {elapsed:.2f} s)")
print(f"suggest-only: all 5 outputs marked suggest_only: {sugg_ok}")
print(f"on again: the pipeline runs on all 5 (reason is not 'agent off'): {on_ok}")
switch.set_state(before, who, "rollback test: state restored")
print("state restored to:", switch.status())
sys.exit(0 if (off_ok and sugg_ok and on_ok) else 1)
