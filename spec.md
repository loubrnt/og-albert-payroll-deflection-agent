# spec.md — executable spec · Tier-1 deflection agent · v3 (final, tag `v1.0`)

> v2 after the first eval (`evals/report_v0.md`, 9 November 2026); **v3 on 26 November 2026, after the run on the 50 fresh cases (`evals/report_v1_fresh.md`) and the two graders.** Changes since the skeleton are marked **[v2]**, changes since v2 **[v3]**. Every miss of an eval is a line below: a miss that is not in the spec will come back.

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
| Router | TF-IDF + logistic regression, 263 synthetic examples, 4 classes | **[v2] Misses 1 (13 of 19).** ≥ 40 distinct phrasings per class, including short, messy and French tickets; keep a held-out *calibration* set (separate from the eval-set) to set the confidence threshold; next rung = embedding-based router if routing accuracy stays below 85 % on the calibration set. **[v3]** Confirmed on fresh cases: 9 of the 12 how-to misses (E51 E52 E57 E58 E60 E61 E63 E66 E67), routing accuracy 66 %. The v2 line is not built yet; it stays the first fix. |
| Confidence threshold | 0.70, fixed by hand | **[v2]** set on the calibration set so that the share of wrongly drafted human-only tickets is 0; never read off the eval-set. |
| Language check | count of 2 common English/French words | **[v2] Miss 2 (3).** Real language identification; English and French are covered, everything else escalates. **[v3]** French is *covered* on paper but scores **0 / 6** on the fresh cases (English 5 / 11): French is a segment we serve worse, not a segment we serve. Until French retrieval exists, a French how-to ticket escalates with the reason "French retrieval not available" instead of failing silently, and French is reported as its own segment (`05_metrics.md` §3). |
| Guard topics | amount, rate, deadline, refund, price, legal | **[v2] Miss B (E50).** A **maintained list** owned by the payroll specialists / Legal: add minimum wage, severance, overtime, dismissal, GDPR requests; reviewed each quarter; each addition is validated on new cases. **[v3] Miss E96** (two questions, the second legal): the guard reads the ticket as a whole and lets it through. The guard checks **every sentence** of the ticket; one pay or legal sentence sends the whole ticket to a person. |
| Retrieval | TF-IDF by section, top-3, floor 0.05 | **[v2] Miss A (E27) and Miss 3 (E20, E25, E04).** Floor calibrated on ≥ 30 tickets with no matching article → `NO_DRAFT`; French tickets translated for retrieval (or French versions of the articles); title boost to pick the right section. **[v3]** The floor is now the main safety gap: 3 of the 4 drafts on person-only fresh tickets (E69, E73, E74) are "no article, draft anyway". The calibration set for the floor gets its own "no article" tickets, never taken from the eval-set. |
| Draft | template (first section text + citation) | **[v2] Miss 3 (E25).** A ticket with two questions: answer the first retrieved topic and say that the second is handled by a person. |
| Policy check | regex: amount, refund, rate/deadline, legal | unchanged; it blocked nothing in v0 because the guard escalated first — add adversarial drafts to test it on its own. |

## edge_cases
- no passage above the retrieval floor → NO_DRAFT, escalate **[v2: floor calibrated]**
- language other than English or French → escalate **[v2: real language identifier]**
- two questions in one ticket, one of them about pay or a deadline → escalate the whole ticket with the how-to passage attached **[v3: this is also the grading rule now — E95, `evals/README.md`]**
- a how-to question that asks for a computed amount or a rate → escalate (guard) or block (policy)
- ticket contains personal data of an employee → draft allowed; the text is not copied into the log beyond the ticket id
- article older than 6 months or flagged "law changed" → escalate

## fallbacks
- confidence below the threshold → escalate, with the category and passages shown to the person
- policy block → show the reason to the person, no draft, not approvable
- model/API error → template drafter, same contract

## done_criteria
- the success criterion of `03_product_brief.md` §7: ≥ 45 % of automatable "how do I…" tickets sendable without editing, two graders **[v2: measured on cases not yet seen: first the 50 new cases of `evals/eval_set_v1.csv` (Assignment 5), then 200 fresh tickets, not on the 50 cases already seen]**
- zero drafts on human-only tickets **[v0 result: 2 — not met; v1 fresh result: 4 (E69, E73, E74, E96) — not met]**
- **[v3] status on 26 November 2026:** sendable drafts **27 %** (cases seen) and **29 %** (fresh cases, 5 / 17), both graded by two people who agree with the proxy on 30 / 30 golden rows → the success criterion is **not met**; this is the evidence behind line one of `08_launch_memo.md`
- zero policy breaches on the adversarial tickets

## out_of_scope
The WON'T column of the MoSCoW board: customer-facing widget · multilingual answers · pay-figure, contribution-rate and legal-deadline tickets · category-2 questions needing account data · billing and refund tickets.

## eval_set
`evals/eval_set_v0.csv` — 50 cases (labels frozen, hash in `evals/LABELS_FROZEN.txt`). All 50 are demo data from now on. Assignment 5: `evals/eval_set_v1.csv`, 100 cases (the 50 of v0 + 50 new, E51-E100); 200 cases is the production standard, still to reach. **[v3]** E51-E100 are demo data too since their run (20 Nov): every fix above is validated on a **new** batch, labelled and frozen before its run, never on these 100.
