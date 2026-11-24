# 08 — Launch memo (one page) — OG Albert · Tier-1 deflection agent

> **DRAFT for the team, 24 November 2026.** Every number traces to a file of this repository. The two lines marked **[team]** are decisions the team takes on 26 November, before the tag `v1.0`; nothing else should change without a new measurement.

**Decision [team — proposed]:** **NO customer-facing launch on 26 November.** The condition of our CONDITIONAL GO (`02_investment_memo.md`, line one) is **not met**: the agent reaches **29 %** sendable drafts on 50 fresh cases against a criterion of 45 % and a flip point of ≈ 43 %, and it drafted on **4** tickets that must go to a person (floor: 0). We ship `v1.0` as an **evaluated prototype in suggest-only**, fix the three causes below, and re-measure on new cases before any customer sees an answer.

## 1. What we measured (and how much to trust it)
| | Cases already seen (v0) | 50 fresh cases (v1, E51–E100) | Criterion |
|---|---|---|---|
| Sendable drafts, share of answerable tickets | 27 % (7/26) | **29 % (5/17)** — English 5/11, **French 0/6** | ≥ 45 % (flip ≈ 43 %) |
| Drafts on tickets that belong to a person | 2 (E27, E50) | **4** (E69, E73, E74, E96) | 0 |
| Answers that state an amount | 0 | 0 | 0 |
| Routing accuracy | 70 % | 66 % | — |

Sources: `evals/report_v0.md` §1, `evals/report_v1_fresh.md` §1. **Trust:** labels frozen before each run (`evals/LABELS_FROZEN.txt`); two graders on 30 golden rows agree with each other 30/30 and with the automatic proxy 30/30, and with the LLM judge 29/30 (`evals/README.md`). **Limits:** 17 answerable fresh cases (one case ≈ 6 points); synthetic tickets and help centre; labels of E51–E100 drafted with an AI assistant (teacher's permission); no user conversation held yet (`03_user_research.md`).

## 2. What it is worth at this level
At the measured 27 %, the net annual value is **≈ 17 k€** (`05_metrics.md` §4, *derived*), below the hurdle (150 k€, `Inputs!D60`) and below do-nothing (144 k€, `Decision!D22`). At 45 % it would be 164.7 k€ (`Decision!C33`). The decision rule of `06_07_experiments_operations.md` §2 — written before any unit — says **kill below 43 %**; we are not yet at the A/B, so we read it as "do not start the pilot".

## 3. Why it misses — three causes, each already a line of `spec.md` v2
1. **Router** (9 of 12 fresh misses): short or atypical how-to phrasings fall under the 0.70 confidence threshold or into the wrong class → more phrasings per class, threshold calibrated on a separate set.
2. **French tickets, English help centre** (0/6 in French): no passage found → translate for retrieval, or French articles.
3. **Safety floor** — a draft with no article (E69, E73, E74: retrieval floor 0.05) and a two-question ticket with a legal part (E96) → calibrated `NO_DRAFT` floor; the guard checks every sentence for pay or legal content.

## 4. What ships in `v1.0` on 26 November
- The prototype in **suggest-only** (drafts shown to an agent, only a human sends; `04_architecture.md` §6), the eval-sets v0 and v1, the grading guideline, the judge, the two reports, the switch and its test log.
- Switch test on 26 November, before the tag (third run; previous: 16 and 20 Nov, `06_07` §4): **[team — who runs it]** · result: _to fill_.
- Owners stay those of `governance.md` S7: Head of Customer Support decides on the switch; Legal owns the guard list.

## 5. What would change the decision
Re-open the launch when, on **new** cases labelled before the run (the 200 fresh tickets of `03_product_brief.md` §7, in shadow mode as in `06_07` §1): sendable drafts **≥ 45 %**, **0** drafts on person-only tickets, **0** amount leaks, and French no worse than English by more than the margin we fix beforehand. Then the Q1 pilot (20 % of customers, opt-in) and the A/B of `06_07` §2 apply unchanged.

## 6. Next steps **[team — names and dates]**
| Step | Owner | By |
|---|---|---|
| Hold the user conversations of `03_user_research.md` (they may change the scope, not only the number) | _to fill_ | _to fill_ |
| Router: phrasings + calibration set | _to fill_ | _to fill_ |
| French retrieval | _to fill_ | _to fill_ |
| `NO_DRAFT` floor + sentence-level guard | _to fill_ | _to fill_ |
| New labelled cases, one run, report | _to fill_ | _to fill_ |
