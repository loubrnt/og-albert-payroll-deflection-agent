"""Streamlit demo surface: Tier-1 deflection agent — the agent's inbox. Run: streamlit run prototype/app.py

The inbox shows DEMO tickets (data/demo_tickets.csv), never the eval rows.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import streamlit as st, pandas as pd
import router, route_rule, retrieve, draft as drafter, policy, switch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
st.set_page_config(page_title="Tier-1 deflection agent — prototype v0", layout="wide")
page = st.sidebar.radio("Prototype v0", ["Inbox", "Eval — eval_set_v0.csv"])
st.sidebar.caption("Streamlit = demo surface. No auth, no logs, fake data only.")
_state = switch.status()
_choice = st.sidebar.radio("⏻ Override switch", list(switch.STATES), index=list(switch.STATES).index(_state))
if _choice != _state:
    switch.set_state(_choice, who="agent (prototype UI)", why="changed from the sidebar")
    st.rerun()
st.sidebar.caption(f"State: {switch.status()} - read on every ticket; every change is logged in data/switch_log.jsonl")

if page == "Inbox":
    st.title("Tier-1 deflection agent — prototype v0")
    tickets = pd.read_csv(os.path.join(ROOT, "data", "demo_tickets.csv"))
    c1, c2 = st.columns([1.1, 2])
    with c1:
        st.subheader("Open tickets")
        choice = st.radio("Pick a ticket", tickets["id"] + " · " + tickets["text"].str.slice(0, 60), label_visibility="collapsed")
    with c2:
        row = tickets[tickets["id"] == choice.split(" · ")[0]].iloc[0]
        st.subheader(row["id"] + " · " + row["text"])
        if switch.status() == "off":
            cat, conf, decision, reason = None, None, "escalate", "agent off"
            st.caption("agent off → escalate - the ticket is in the human queue with the reason \"agent off\"")
        else:
            cat, conf = router.predict(row["text"])
            decision, reason = route_rule.decide(cat, conf, row["text"])
            st.caption(f"routed as {cat} ({conf:.2f}) → {decision}" + (f" — {reason}" if reason else ""))
        if switch.status() == "off":
            st.warning("Agent off - no draft. Handed over to the human queue with the reason \"agent off\".")
        elif decision == "draft":
            passages = retrieve.top_k(row["text"])
            text = drafter.draft(row["text"], passages)
            status, preason = policy.check(text)
            if text == "NO_DRAFT" or status == "block":
                st.warning(f"No draft: {preason or 'no passage found'}. Hand over to a person.")
            else:
                st.markdown("**Suggested reply — review before sending**")
                st.write(text)
                st.caption("Sources: " + " · ".join(f"{p['article']} · {p['section']}" for p in passages))
                st.caption(f"Policy check: {status} · AI answer — you approve before sending (L2 in this prototype; L3 with sampling in production: 10 % in the pilot, 5 % at steady state)")
                b1, b2, b3 = st.columns(3)
                b1.button("✅ Send", type="primary", disabled=(switch.status() == "suggest_only")); b2.button("✏️ Edit"); b3.button("↗ Hand over to a person")
        else:
            # A low-confidence how-to ticket is not a "human only" topic: say which kind of hand-over it is.
            kind = "Human only" if reason.startswith(("guard word", "human-only")) else "Handed over"
            st.warning(f"{kind} — no draft ({reason}). Handed over to a person with the reason and the context.")
        st.button("🙋 Talk to a person (always visible)")
else:
    st.title("Eval — evals/eval_set_v0.csv")
    import evals
    out = evals.run(quiet=True)
    st.dataframe(out.drop(columns=["draft"]), use_container_width=True, hide_index=True)
