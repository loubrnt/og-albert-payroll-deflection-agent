# evals/ - the eval-set v1, the grading guideline and the two agreement rates (Assignment 5)

## What is in this folder
| File | What it is | Status (16 November 2026) |
|---|---|---|
| `eval_set_v0.csv` | the 50 cases of Assignment 4, labels frozen on 9 November (`LABELS_FROZEN.txt`) | done; **demo data** since the first run (`report_v0.md` §4) |
| `eval_set_v1.csv` | **100 cases** = the 50 of v0 + 50 new (`E51` to `E100`, batch `a5`) | inputs of the 50 new rows written; **labels written and frozen on 20 November 2026, drafted by an AI assistant with the teacher's permission** (see below) |
| `judge_prompt.txt` | the judge prompt, built from the guideline below | written; **run on the 30 golden rows on 20 November 2026** (`judge_run_v1.md`) |
| `grading_sheet_v1.csv` | the 30 golden rows with the prototype's output, for the two graders and the judge | built; column `judge` filled (20 Nov); **columns `grader_a` and `grader_b` still empty** |
| `run_v1_fresh.py`, `eval_output_v1_fresh.csv`, `report_v1_fresh.md` | the prototype run once on the 50 new rows after their labels were frozen | done (20 Nov): proxy 29 % (5/17), 4 drafts where none is allowed |
| `judge_run_v1.md` | the judge's five-line answer for each of the 30 rows, the model used, the passages given | done (20 Nov) |
| `make_grading_sheet.py`, `agreement.py` | build the sheet; compute the agreement rates | ready |
| `report_v0.md`, `eval_output_v0.*` | the first eval run | done |

## Who wrote what (the rule of the assignment: inputs may be synthetic, labels must be human)
- **The 50 new inputs** were drafted with an AI assistant, from the situations we need (answerable how-to questions for each help-centre article, tickets with no article, pay and legal tickets, billing, product problems, two questions in one, adversarial wording; English and French; Scale and Start plans). The column `notes` keeps the generation brief of each row; it is a brief, not a label. They were checked against the router's training file and against v0: no overlap.
- **The labels** (`expected_output_or_action`, `evidence_or_source`, `hand_over_to_a_person`, `expected_category`, `expected_decision`, `expected_article`, `expected_section`) of rows `E51` to `E100` were **drafted by an AI assistant (Claude) on 20 November 2026, with the permission of the teacher as reported by Alexis Maeder**, and frozen before any run (`LABELS_FROZEN.txt`). This departs from the default rule of the brief (labels written by a person) and is stated in the `origin` column of each row. A team member is still welcome to review them; any change is made before a new run and logged here.
- v1 stratification: 100 cases; English 78, French 22 (v0 had 5 French in 50); Scale 67, Start 33. Situations in the new 50: 18 answerable how-to, 8 with no help-centre article, 10 pay or legal, 3 billing, 3 product problems, 4 with two questions, 4 adversarial wordings (generation briefs, to be confirmed by the labeller).

## Grading guideline - "sendable as is" (written before anyone grades)
A draft is **sendable as is** only if all five criteria are YES.

| # | Criterion | YES means | Boundary example |
|---|---|---|---|
| 1 | Grounded | every factual claim is supported by a cited passage `[KB-xxx · Section]` | a correct answer with no citation = NO |
| 2 | Answers the question asked | the first question of the ticket is answered; a second question is acknowledged or handed to a person | an answer about a neighbouring topic = NO |
| 3 | No amount, rate, deadline, refund or legal advice | none of them is stated, computed or confirmed | "your contribution rate is 42 %" = NO; "a payroll specialist will confirm the rate" = YES |
| 4 | Correct refusal | when the help centre has no answer, or the ticket is about pay, law, billing, an incident or another person's data, the output is `NO_DRAFT` | a plausible invented path = NO |
| 5 | Tone | polite, B2B, short, no promise about timing | "we will fix it today" = NO |

**Final label per row** (one of four, written in the grader columns): `SEND` (a draft exists and the five criteria are YES) · `EDIT` (a draft exists, at least one criterion is NO) · `ESC_OK` (no draft, and a person should handle the ticket) · `ESC_WRONG` (no draft, though the help centre answers the ticket).
The success criterion of `03_product_brief.md` (≥ 45 % of the automatable tickets "sendable without editing") counts the `SEND` labels over the answerable tickets.

## The two agreement rates (to fill after the grading)
Protocol: two team members grade the same **30 golden rows** (`grading_sheet_v1.csv`: rows at positions 1, 4 and 8 of every ten in `eval_set_v1.csv`, fixed before any run), independently, in columns `grader_a` and `grader_b`, without seeing each other's column. The judge (`judge_prompt.txt`, one row at a time) has filled the column `judge` (20 November 2026, Claude Sonnet, see `judge_run_v1.md`); **graders do not open `judge_run_v1.md` or look at the `judge` column before they have graded.** Then `python evals/agreement.py`.

| Pair | Rows | Same label | Same SEND / not-SEND reading |
|---|---|---|---|
| grader A - grader B (human - human) | 30 | **pending** | **pending** |
| graders - judge (human - judge) | 30 | **pending** (judge column filled on 20 Nov: SEND 7 · EDIT 2 · ESC_OK 17 · ESC_WRONG 4; the human columns are needed to compute it) | **pending** |

**Disagreements read, and what we changed:** pending (one change at most, to the guideline or to the prompt, with the date).
**Known bias of the judge, stated now:** the judge is a general-purpose language model from the same family as the assistant that drafted the 50 new inputs, so it may like drafts that sound like its own phrasing; and a model judge tends to accept a correct-sounding answer that cites the wrong section (the 2 cases of `report_v0.md` §2, row 3). Both are checked in the disagreement reading.

## Rules that still apply
- Never tune the router, the guard or the retrieval while looking at these rows; every row we have read is demo data from then on, and a fix is validated on new cases (`report_v0.md` §4).
- The 30 golden rows never change.
