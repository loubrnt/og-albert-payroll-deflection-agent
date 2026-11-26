# 08 — Launch memo (one page) — OG Albert · Tier-1 deflection agent

> 26 November 2026, the version tagged `v1.0`. Every number traces to a file of this repository. Nothing here was measured on real customers.

**Decision: NO-GO for a customer-facing launch. We ship `v1.0` as an evaluated prototype in suggest-only, and we re-open the decision only on new cases.** The condition of our CONDITIONAL GO (`02_investment_memo.md`, line one) is **not met**: **29 %** of the answerable fresh cases get a draft two graders would send without editing, against a criterion of **45 %** and a flip point of **≈ 43 %**; and the agent drafted on **4** tickets that belong to a person, against a floor of **0**. The decision rule written before any measurement (`06_07_experiments_operations.md` §2) says *kill below 43 %*; we are not at the A/B yet, so we read it as "do not start the pilot".

## 1. What we measured — and how much to trust it
| | Cases already seen (v0, E01–E50) | 50 fresh cases (v1, E51–E100) | Criterion |
|---|---|---|---|
| Sendable drafts, share of answerable tickets | 27 % (7 / 26) | **29 % (5 / 17)** — English 5 / 11, **French 0 / 6** | ≥ 45 % (flip ≈ 43 %) |
| Drafts on tickets that belong to a person | 2 (E27, E50) | **4** (E69, E73, E74, E96) | 0 |
| Answers that state an amount | 0 | 0 | 0 |
| Routing accuracy | 70 % | 66 % | — |

Sources: `evals/report_v0.md` §1, `evals/report_v1_fresh.md` §1. **Why we trust it:** labels frozen and hashed before each run (`evals/LABELS_FROZEN.txt`); the prototype was run once on the fresh cases, unchanged since `eval-v0`; two graders read the 30 golden rows on their own and agree with each other **30 / 30**, with the automatic proxy **30 / 30**, and with the LLM judge **29 / 30** (E95, now settled in the guideline, `evals/README.md`). **Why we do not trust it too much:** 17 answerable fresh cases (one case moves the rate by ≈ 6 points); synthetic tickets and help centre; labels of E51–E100 drafted with an AI assistant (teacher's permission); no user conversation held yet (`03_user_research.md`). None of these limits could turn 29 % into 45 %.

## 2. What it is worth at this level
At the measured 27 %, the net annual value is **≈ 17 k€** (*derived*, `05_metrics.md` §4) — below the hurdle (**150 k€**, `Inputs!D60`) and below do-nothing (**144 k€**, `Decision!D22`). At 45 % it would be **164.7 k€** (`Decision!C33`); each point between is worth ≈ 8.2 k€ a year (`05_metrics.md` §2). Launching now would spend the fixed costs (204 k€, `Decision!D14`) on a tool that does not pay for them.

## 3. Why it misses — three causes, each a line of `spec.md` v3
1. **Router** — 9 of the 12 fresh how-to misses: short or unusual phrasings fall under the 0.70 threshold or into the wrong class → more phrasings per class, a threshold set on a separate calibration set, an embedding rung if still below 85 %.
2. **French** — 0 / 6: French tickets, English help centre, no passage found → French retrieval; until then French how-to tickets escalate with a stated reason and French is reported as its own segment.
3. **Safety floor** — three drafts with no article (E69, E73, E74: retrieval floor 0.05 too low) and one two-question ticket with a legal part (E96) → a calibrated `NO_DRAFT` floor, and a guard that reads every sentence.

## 4. What ships in `v1.0` today
- The prototype in **suggest-only** (drafts shown to a support agent, only a human sends; `04_architecture.md` §6), never in front of a customer.
- The eval-sets v0 and v1, the grading guideline (E95 settled), the judge prompt and run, the two reports, `spec.md` v3.
- **The switch, tested a third time today** (26 Nov, Mathis Meimoun's laptop, `prototype/test_switch.py`): off → the next 5 tickets to the human queue with "agent off"; suggest-only → 5 outputs marked; on → pipeline runs. **Passed** (log in `data/switch_log.jsonl`; earlier runs 16 and 20 Nov).
- Owners unchanged (`governance.md` S7–S8): the Head of Customer Support signs any move towards customers and holds the switch by day; Legal owns the guard list.

## 5. What would change the decision
We re-open the launch when, on **new** cases labelled and frozen before the run — first a new batch of 50, then the 200 fresh tickets of `03_product_brief.md` §7 in shadow mode (`06_07` §1):
- sendable drafts **≥ 45 %** overall, with **French no more than 10 points below English**;
- **0** drafts on person-only tickets and **0** amount leaks;
- the switch test passed again on the release candidate.

Then the Q1 pilot (20 % of customers, opt-in) and the A/B of `06_07` §2 apply unchanged. If the new batch stays below 43 % after the three fixes, we stop and fund the next-best project (help-centre search revamp + month-end checklists, 150 k€ a year).

## 6. Next steps
| Step | Owner (role) | By |
|---|---|---|
| Hold the user conversations of `03_user_research.md` (they may change the scope, not only the number) | OG Albert, two members per conversation | 11 Dec 2026 |
| Router: ≥ 40 phrasings per class, calibration set, threshold set on it | eval owner + 2 devs | 18 Dec 2026 |
| `NO_DRAFT` floor calibrated on "no article" tickets; guard reads every sentence | eval owner; Legal validates the guard list | 18 Dec 2026 |
| French retrieval (translate for retrieval, or French articles) | 2 devs + content team | 15 Jan 2027 |
| New batch of 50 cases, labelled and frozen by people, one run, report v2 | eval owner + two graders | 22 Jan 2027 |
| 200 fresh tickets in shadow mode → go / no-go for the Q1 pilot | Head of Customer Support signs | 26 Feb 2027 |

## 7. Who did what (from the commit history)
| Member | Main contributions |
|---|---|
| Lou Brunet (loubrnt) | Assignments 1–2 (problem statement, sizing, investment memo, governance S1–S2), README, grader B |
| Cristian Larrain (cristianlrn) | product brief, lean canvas, research guide, spec skeleton, the prototype (router, guard, retrieval, policy, switch), eval-set v1 and judge prompt, 05 and 06_07 first versions |
| Alexis Maeder (AlexisMaeder) | Assignment 5 labels and fresh run, judge run, second rollback test, metrics and architecture updates |
| Colin Pietri (colinpietri20) | grader A and the agreement rates, one wording of the success criterion across 01–03, reviews |
| Mathis Meimoun (Mathmnms) | personas, journeys and stakeholder map (01), the eval-set condition in the memo (02), architecture v0 (04), graded results reported (05, evals), third rollback test (06_07), `spec.md` v3 and the E95 decision, this launch memo |
