# spec.md — executable spec · Tier-1 deflection agent · skeleton (Assignment 3)

> Filled from `03_product_brief.md` v1. It is updated to v2 in Assignment 4, from the misses of the first eval run: every miss becomes a line here.

## problem
Tier-1 agents spend about 7 of the 11 minutes of a "how do I…" ticket searching the help center and rewriting an answer; those tickets are 55 % of 40,000 a month and pile up at payroll close. The agent drafts a grounded, cited answer for the questions it may answer and hands everything else to a person — it never states, computes or confirms an amount.

## user_workflow
```
- read      : ticket text (+ language)                 -> category, confidence             (L4 above threshold)
- guard     : category, confidence, text               -> draft | escalate                 (L4, rules)
- retrieve  : text                                     -> top-3 help-center passages       (L3)
- draft     : passages + text                          -> answer with citations            (L3 in production; L2 in the prototype)
- check     : answer                                   -> policy pass | block              (L4 — can only block)
- send      : answer                                   -> customer                         (L3 production · person only in the prototype)
- escalate  : ticket + passages + reason               -> human queue                      (person only)
```

## io_contracts
```
ticket : {id, text, language}
output : {category, confidence, decision: draft|escalate, reason, draft_text|NO_DRAFT,
          citations[{article, section, score}], policy: pass|block}
```

## components and thresholds
| Component | Rung | Threshold / setting (to be calibrated in Assignment 4) |
|---|---|---|
| Router | TF-IDF + logistic regression | confidence threshold, set on a calibration set separate from the eval-set |
| Guard topics | rules | amount, rate, contribution, deadline, refund, price, legal — a list with an owner and a review cycle |
| Retrieval | TF-IDF by section, top-3 | minimum score below which the answer is `NO_DRAFT` |
| Draft | pretrained model with retrieved passages ("cite or abstain") | answers in the customer's language, English or French only |
| Policy check | rules | blocks any draft with an amount, a deadline or a refund promise |

## edge_cases
- no passage above the retrieval floor → no draft, escalate
- language other than English or French → escalate
- two questions in one ticket, one of them about pay or a deadline → escalate the whole ticket with the how-to passage attached
- a how-to question that asks for a computed amount or a rate → escalate (guard) or block (policy)
- article older than 6 months or flagged "law changed" → escalate

## fallbacks
- confidence below the threshold → escalate, with the category and the passages shown to the person
- policy block → show the reason to the person, no draft, not approvable
- model/API error → escalate

## done_criteria
- the success criterion of `03_product_brief.md` §7: ≥ 45 % of automatable "how do I…" tickets resolved without human touch and not reopened within 7 days, measured on 200 fresh tickets
- zero answers that state, compute or confirm an amount
- zero policy breaches on adversarial tickets

## out_of_scope
The WON'T column of the MoSCoW board in `03_product_brief.md` §3.

## eval_set
`evals/eval_set_v0.csv` — 20 cases now, 50 with Assignment 4, 200 for Assignment 5.
