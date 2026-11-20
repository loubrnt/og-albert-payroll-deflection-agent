"""The override switch (the "off" button of 04_architecture.md §6), made real for the prototype.

Three states, stored in data/switch.json and logged (append-only) in data/switch_log.jsonl:
  on            - the pipeline runs as in evals/report_v0.md
  suggest_only  - drafts are shown to the agent but cannot be sent from the tool (humans send)
  off           - every ticket goes to the human queue with the reason "agent off"; no router, no draft

Used by prototype/app.py (the inbox) and tested by prototype/test_switch.py. The state file is read on every ticket,
so a change takes effect on the next ticket (no restart).
"""
import json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "data", "switch.json")
LOG = os.path.join(ROOT, "data", "switch_log.jsonl")
STATES = ("on", "suggest_only", "off")


def status():
    try:
        return json.load(open(STATE, encoding="utf-8"))["state"]
    except (FileNotFoundError, KeyError, ValueError):
        return "on"


def set_state(state, who, why=""):
    if state not in STATES:
        raise ValueError(f"state must be one of {STATES}")
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    json.dump({"state": state, "who": who, "at": now}, open(STATE, "w", encoding="utf-8"))
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps({"at": now, "state": state, "who": who, "why": why}) + "\n")
    return state


def off_result():
    """What a ticket becomes when the agent is off: same contract as evals.run_one."""
    return dict(category=None, confidence=None, decision="escalate", reason="agent off", draft="NO_DRAFT", citations=[], policy="pass")


def run_ticket(text):
    """The pipeline behind the switch: off -> human queue with the reason 'agent off'; otherwise evals.run_one (unchanged)."""
    if status() == "off":
        return off_result()
    import evals
    out = evals.run_one(text)
    out["suggest_only"] = status() == "suggest_only"
    return out
