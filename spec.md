# spec.md — executable spec · Tier-1 deflection agent · v2

> v2 after the first eval (`evals/report_v0.md`, 9 November 2026). Changes since the skeleton are marked **[v2]**. Every miss of the eval is a line below: a miss that is not in the spec will come back.

## problem
The company's tier-1 agents spend about 7 of the 11 minutes of a "how do I…" ticket searching the help centre and rewriting an answer; those tickets are 55 % of 40,000 a month and pile up at month end. The agent drafts a grounded, cited answer for the questions it may answer and hands everything else to a person — it never answers on a pay figure, a contribution rate or a legal deadline.

## user_workflow
```
- read      : ticket text (+ language)                 -> category, confidence             (L4 above threshold)
- guard     : category, confidence, text               -> draft | escalate                 (L4, rules)
- retrieve  : text                                     -> top-3 help-centre passages       (L3)
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
**[v2]** `reason` is always filled when `decision = escalate`, so that the person sees why.

## components, thresholds and what changed
| Component | v0 (what was built) | v2 — change, with the miss it comes from |
|---|---|---|
| Router | TF-IDF + logistic regression, 263 synthetic examples, 4 classes | **[v2] Misses 1 (13 of 19).** ≥ 40 distinct phrasings per class, including short, messy and French tickets; keep a held-out *calibration* set (separate from the eval-set) to set the confidence threshold; next rung = embedding-based router if routing accuracy stays below 85 % on the calibration set. |
| Confidence threshold | 0.70, fixed by hand | **[v2]** set on the calibration set so that the share of wrongly drafted human-only tickets is 0; never read off the eval-set. |
| Language check | count of 2 common English/French words | **[v2] Miss 2 (3).** Real language identification; English and French are covered, everything else escalates. |
| Guard topics | amount, rate, deadline, refund, price, legal | **[v2] Miss B (E50).** A **maintained list** owned by the payroll specialists / Legal: add minimum wage, severance, overtime, dismissal, GDPR requests; reviewed each quarter; each addition is validated on new cases. |
| Retrieval | TF-IDF by section, top-3, floor 0.05 | **[v2] Miss A (E27) and Miss 3 (E20, E25, E04).** Floor calibrated on ≥ 30 tickets with no matching article → `NO_DRAFT`; French tickets translated for retrieval (or French versions of the articles); title boost to pick the right section. |
| Draft | template (first section text + citation) | **[v2] Miss 3 (E25).** A ticket with two questions: answer the first retrieved topic and say that the second is handled by a person. |
| Policy check | regex: amount, refund, rate/deadline, legal | unchanged; it blocked nothing in v0 because the guard escalated first — add adversarial drafts to test it on its own. |

## edge_cases
- no passage above the retrieval floor → NO_DRAFT, escalate **[v2: floor calibrated]**
- language other than English or French → escalate **[v2: real language identifier]**
- two questions in one ticket, one of them about pay or a deadline → escalate the whole ticket with the how-to passage attached
- a how-to question that asks for a computed amount or a rate → escalate (guard) or block (policy)
- ticket contains personal data of an employee → draft allowed; the text is not copied into the log beyond the ticket id
- article older than 6 months or flagged "law changed" → escalate

## fallbacks
- confidence below the threshold → escalate, with the category and passages shown to the person
- policy block → show the reason to the person, no draft, not approvable
- model/API error → template drafter, same contract

## done_criteria
- the success criterion of `03_product_brief.md` §7: ≥ 45 % of automatable "how do I…" tickets sendable without editing, two graders **[v2: measured on the 200-case set of Assignment 5, not on the 50 cases already seen]**
- zero drafts on human-only tickets **[v0 result: 2 — not met]**
- zero policy breaches on the adversarial tickets

## out_of_scope
The WON'T column of the MoSCoW board: customer-facing widget · multilingual answers · pay-figure, contribution-rate and legal-deadline tickets · category-2 questions needing account data · billing and refund tickets.

## eval_set
`evals/eval_set_v0.csv` — 50 cases (labels frozen, hash in `evals/LABELS_FROZEN.txt`). All 50 are demo data from now on; 200 new cases by Assignment 5.
