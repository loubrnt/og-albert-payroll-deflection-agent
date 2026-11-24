# Eval report v0 — OG Albert · Tier-1 deflection agent

**Date:** first run 9 November 2026; re-run on this repository 15 November 2026 (same decisions and drafts, see `evals/LABELS_FROZEN.txt`)   **Eval-set:** `evals/eval_set_v0.csv`, 50 cases (26 answerable "how do I…", 24 human-only)   **Prototype commit:** `eval-v0` (to tag when the four commits are pushed)
**Labels frozen before the run:** SHA-256 `16ded8fd…b47ecd` in `evals/LABELS_FROZEN.txt`. Raw output: `evals/eval_output_v0.txt` and `evals/eval_output_v0.csv`.
**Drafter used:** the **template drafter** (no model call): it quotes the best retrieved passage with its citation. There is no generative path in this repository.

## 1. The number against the criterion
| | Value |
|---|---|
| Success criterion (brief §7) | *"At least 45 % of the automatable 'how do I…' tickets are resolved without human touch, and zero answers state or confirm an amount"* on 200 fresh tickets by 22 November. The 50 cases of this assignment are a first reading, not the test; here the proxy is compared with the same 45 %, and the graded number uses the A4 rule ("two graders would send without editing"). |
| Drafts produced on answerable tickets | 9 / 26 = 35 % |
| **Drafts citing the expected article and section (automatic proxy, policy pass)** | **7 / 26 = 27 %** |
| **Drafts two graders would send without editing** (graded by hand) | **27 % — the proxy is confirmed by two graders** (23 Nov): on the 15 v0 rows of the golden set (`evals/grading_sheet_v1.csv`), both graders gave `SEND` exactly to the drafts the proxy counts as hits (4 of 8 answerable rows) and `EDIT` to E25 (right article, wrong section). See §3. |
| Drafts on human-only tickets (should be 0) | **2** (E27, E50) |
| Policy blocks | 0 |
| Routing accuracy | 70 % (35 / 50) |
| Retrieval hit@3 on answerable tickets | 31 % (8 of 26 — escalated tickets never reach retrieval and count as misses; of the 9 tickets that did reach it, 8 had the right article in the top 3) |

**Verdict:** criterion **not met** (27 % vs 45 %), and the safety condition **not met** (2 drafts on human-only tickets).

## 2. The three most frequent misses — and the two critical ones
19 of the 26 answerable tickets missed. Causes, by component:

| # | What went wrong (one line) | Tickets | Which component | What it becomes in `spec.md` v2 |
|---|---|---|---|---|
| 1 | The router classifies short or atypical how-to phrasings with low confidence (7) or as the wrong class (6): 13 of 19 misses. | E02 E07 E08 E10 E11 E13 E14 E17 E18 E19 E21 E22 E24 | 1 · router (TF-IDF + logistic regression, 263 synthetic examples) | Router training set ≥ 40 distinct phrasings per class, including short, messy and French tickets; add an embedding-based router as the next rung; **calibrate the 0.70 threshold on a separate calibration set**, never on the eval-set. |
| 2 | The language check wrongly rejects English tickets (3). | E06 E16 E26 | 2 · guard (`language_ok`) | Replace the word-count heuristic with a real language identifier; English and French are covered. |
| 3 | The right article is found but the wrong section is cited (2), or a French ticket finds no passage in the English KB (1). | E20 E25 · E04 | 3 · retrieval + draft | Retrieve per section with a title boost; French tickets are translated for retrieval or the KB gets French versions; multi-question tickets: answer the first topic and say so. |
| **A** | **Critical — a ticket with no article gets a draft.** The retrieval floor (0.05) is so low that "connect the company to SAP" matches the time-tracking article. | E27 | 3 · retrieval | Minimum retrieval score calibrated on ≥ 30 "no article exists" tickets; below it → `NO_DRAFT` and escalate. |
| **B** | **Critical — a how-to ticket that also asks for a pay amount gets a draft.** "minimum wage" is not in the guard list. | E50 | 2 · guard | Guard topics become a **maintained list owned by the payroll specialists / Legal** (minimum wage, severance, overtime, dismissal, GDPR requests…), reviewed each quarter. Fixes are validated on new cases, not on E50. |

## 3. Who graded, and how
**Done on 20 and 23 November, on the 30 golden rows of `evals/grading_sheet_v1.csv`** (15 of them are v0 cases), with the guideline of `evals/README.md` (labels `SEND` · `EDIT` · `ESC_OK` · `ESC_WRONG`). Two team members graded independently (`grader_a`, `grader_b`), without seeing each other's column or the judge's. Agreement: 30/30 between the two graders, 29/30 with the judge (E95). On every graded row, `SEND` matches the automatic proxy, so the 27 % headline of §1 stands as the graded reading. The first protocol (graders on the 7 + 2 + 2 drafts of this run, in `eval_output_v0.csv`) was replaced by the golden rows, which cover v0 and the fresh cases with one sheet.

## 4. What is demo data and what is eval data
- All 50 cases, the 12 help-centre articles and the guard/policy rules were **drafted in a single pass by one author, not by the graders**. That is a weakness: the eval-set partly agrees with the system's author. Two mitigations: the labels were written and hashed before the first run; and the guard list was deliberately stripped back to the words of the spec and the governance guardrail (amount, rate, deadline, refund, price, legal) before the run, after noticing it had started to copy the traps of the eval-set.
- **No ticket was used to tune** the router, the guard, the retrieval or the drafter after seeing the output. The run was done **once**. All 50 outputs have now been read, so **every case is demo data from now on**: fixes proposed in `spec.md` v2 must be validated on the 200-case set of Assignment 5 (new cases, labelled before the run).
- The router is trained on `data/tickets_synthetic.csv` (263 rows, synthetic); there is no overlap with eval inputs (checked automatically).

## 5. Next step (one line)
Have two graders fill `grader_a` / `grader_b`, then rebuild the router, the guard topics list and the retrieval floor as in `spec.md` v2 and re-measure on the new 200-case set.
