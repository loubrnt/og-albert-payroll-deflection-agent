"""Step 3 - the drafter. Template drafter: it quotes the best retrieved passage with its citation.

The eval in evals/report_v0.md was run with this drafter. A generative drafter would plug in here with the same
contract (ticket, passages -> text or NO_DRAFT); it has not been built or run for this assignment.
"""


def template_draft(ticket, passages):
    if not passages:
        return "NO_DRAFT"
    p = passages[0]
    return f"Hello, here is how to do it: {p['text']} [{p['article']} · {p['section']}] Tell us if that works for you."


def draft(ticket, passages):
    return template_draft(ticket, passages)
