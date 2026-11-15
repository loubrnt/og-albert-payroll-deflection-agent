"""Step 4 — the policy checker (rung 1: rules). It can only block. Returns (status, reason)."""
import re

RULES = [
    (r"(€|\$|£)\s?\d|\d+\s?(€|euros|dollars|%)|\bprice\b|\bpricing\b", "states an amount or a price"),
    (r"\brefund(ed|s)?\b|\bcredit note\b", "promises a refund"),
    (r"\b(contribution|cotisation)s?\b|\brates?\b|\bdeadlines?\b|\bby when\b", "states a rate or a deadline"),
    (r"\blegal(ly)?\b|\blawyer\b|\bcourt\b|\bby law\b", "gives legal advice"),
]


def check(draft_text):
    """Return ('pass', '') or ('block', reason). NO_DRAFT passes (nothing to send)."""
    if draft_text == "NO_DRAFT":
        return "pass", ""
    for pat, reason in RULES:
        if re.search(pat, draft_text, flags=re.I):
            return "block", reason
    return "pass", ""
