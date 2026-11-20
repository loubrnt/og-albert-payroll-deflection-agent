# Eval report v1 (fresh cases) — OG Albert · Tier-1 deflection agent

**Date:** 20 November 2026 · **Cases:** the 50 new rows of `evals/eval_set_v1.csv` (E51–E100, batch `a5`), never seen by the prototype before this run · **Labels:** frozen before the run (hash in `evals/LABELS_FROZEN.txt`, commit `evals: labels of E51-E100 written and frozen before any run`) · **Prototype:** unchanged since `eval-v0` (template drafter, no model call) · **Script:** `evals/run_v1_fresh.py`, run **once** · **Raw output:** `evals/eval_output_v1_fresh.csv`

> **Who wrote the labels.** OG Albert. The labels of E51–E100 were drafted with an AI assistant, with the teacher's permission (20 November 2026), and frozen before the run; see `evals/README.md`. Two-question tickets with a pay or legal part are labelled *person only*, as in `04_architecture.md` §5.

## 1. The number against the criterion
| | Value |
|---|---|
| Cases | 50: 17 answerable "how do I…", 8 with no help-centre article, 25 person only (pay / legal 18, billing 3, product 4) |
| Drafts citing the expected article and section (automatic proxy, policy pass) | **5 / 17 = 29 %** (v0, on cases already seen: 27 %) |
| Drafts two graders would send without editing | **pending** — columns `grader_a` / `grader_b` of `evals/eval_output_v1_fresh.csv` |
| Drafts on tickets that must not get one (must be 0) | **4**: E69, E73, E74 (no article), E96 (two questions, one legal) |
| By language (answerable) | English 5 / 11 · **French 0 / 6** |
| Routing accuracy | 66 % |
| Retrieval hit@3 on answerable | 29 % (escalated tickets never reach retrieval and count as misses) |
| Policy blocks | 0 |

**Verdict:** criterion **not met** (29 % vs 45 %) and the floor **not met** (4 drafts where none is allowed). The fresh cases confirm the reading of `report_v0.md`; they do not change the decision of `02_investment_memo.md` (stay in the pilot, fix, re-measure).

## 2. Misses, by component (the same three causes as v0, now on unseen cases)
| Cause | Tickets | Component | Already a line of `spec.md` v2? |
|---|---|---|---|
| Router confidence below 0.70 or wrong class on a how-to ticket | E51 E52 E57 E58 E60 E61 E63 E66 E67 | 1 · router | yes — more phrasings per class, calibrated threshold |
| French ticket, English help centre: no passage found | E53 E56 E68 (and E60 E63 E66 via the router) | 3 · retrieval | yes — translate for retrieval or French articles |
| **No article, but a draft is produced** (the retrieval floor 0.05) | E69 E73 E74 | 3 · retrieval | yes — case A of `report_v0.md` (calibrated floor, `NO_DRAFT` below) |
| **Two questions, one legal, but a draft is produced** | E96 | 2 · guard | yes — the two-question rule of `04_architecture.md` §5 is design only; the guard must look for a pay/legal part in any sentence |

## 3. What this run is and is not
- One run, no change to the prototype, no label touched after the run. From now on E51–E100 are **demo data** too: a fix is validated on new cases.
- The number is an automatic proxy; the graded number needs two people (`evals/README.md`).
- The 45 % criterion of `03_product_brief.md` §7 is a test on 200 fresh tickets; this is a first reading on 17 answerable cases, so one case moves the rate by about 6 points.
