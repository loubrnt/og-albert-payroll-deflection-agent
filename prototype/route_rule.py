"""Step 2 — the routing rule (rung 1), spec §user_workflow 'guard'.

A ticket is drafted only if: the router says how_do_i, confidence >= THRESHOLD, the language is English or French,
and the text contains none of the guard words (amounts, rates, deadlines, refunds, legal, prompt-injection phrases).
Anything else is escalated to a person.
"""
import re

THRESHOLD = 0.70
HUMAN_ONLY = {"pay_legal", "billing", "product"}

# Guard words come from the spec and the governance guardrail only (amount, rate, deadline, refund, price, legal) — not from the eval rows.
GUARD = re.compile(
    r"\b(refund\w*|price\w*|pricing|invoice\w*|subscription|discount\w*|rates?|deadlines?|"
    r"contribution\w*|cotisation\w*|legal\w*|law|lawyer|court|amount\w*|montant\w*)\b",
    re.I,
)
EN = {"the", "how", "do", "i", "to", "my", "we", "our", "can", "is", "and", "a", "for", "of", "in", "it", "what", "where", "why", "this", "that"}
FR = {"le", "la", "les", "je", "comment", "mon", "mes", "où", "est", "un", "une", "des", "pour", "de", "du", "et", "que", "qui", "veux", "peux", "nous"}


def language_ok(text):
    """Cheap check: at least 2 common English or French words, otherwise escalate (spec: other languages are out of scope)."""
    words = re.findall(r"[\wéèêàùç']+", (text or "").lower())
    return sum(w in EN for w in words) >= 2 or sum(w in FR for w in words) >= 2 or len(words) <= 3


def decide(category, confidence, text=""):
    """Return (decision, reason)."""
    if GUARD.search(text or ""):
        return "escalate", "guard word (amount, rate, deadline, refund or legal topic)"
    if not language_ok(text):
        return "escalate", "language not covered"
    if category in HUMAN_ONLY:
        return "escalate", f"human-only category: {category}"
    if confidence < THRESHOLD:
        return "escalate", f"confidence {confidence:.2f} below {THRESHOLD}"
    return "draft", ""
