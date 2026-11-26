# 03 — AI Lean Canvas · Tier-1 deflection agent

> Same numbers as `02_sizing.xlsx` (base case) and `03_product_brief.md`.

## The nine classic blocks
| Block | Our answer | Comes from |
|---|---|---|
| 1. Problem — top 3 pains | (1) Agents search and retype the same articles — 7 of the 11 minutes of a "how do I…" ticket. (2) Customers wait at payroll close, the busiest days of the month. (3) Support is measured on tickets closed, not on tickets avoided. | 01 |
| 2. Users / customer segments | HR managers and payroll officers of our 2,500 customer companies (Camille); tier-1 support agents who sample and take the escalations (Inès). | 01, 03 brief §1 |
| 3. Unique value proposition — one sentence | "The right payroll answer in seconds, with the help-center article it comes from — and a person for anything that touches an employee's pay." | 01 (press release) |
| 4. Solution — the MUST features | Policy checker · one-click escalate with context · draft with citations · eval-set of 200. | 03 brief §3 |
| 5. Channels — where it lives | In-app widget next to the payroll screen (Q1 pilot, 20 % of customers, opt-in); MVP: a test screen replaying tickets. | 03 brief §6 |
| 6. Value — what it is worth per year (year 1, base case) | Base €206k net · expected value €301k (pessimistic −€202k, optimistic €994k) against a hurdle of €150k and do-nothing of €144k. | 02 |
| 7. Cost structure — the cost lines | Tokens €3k · integration €120k one-off (€40k a year over 3 years) · evaluation €40k · supervision €75k (1.5 FTE) · monitoring €25k · re-evaluation €24k · expected cost of wrong answers €14k. | 02 |
| 8. Key metric — the success criterion | ≥ 45 % of automatable "how do I…" tickets get a draft two graders would send without editing, read first on the 50 fresh cases of Assignment 5, then on 200 fresh tickets (7-day reopen rate read in the Q1 pilot); zero answers that state an amount. **Measured at `v1.0`: 29 % on the fresh cases, 4 drafts on person-only tickets, 0 amounts — not met.** | 03 brief §7, `evals/report_v1_fresh.md` |
| 9. Unfair advantage — data or know-how nobody else has | Our own help center (~1,500 articles), 12 months of tickets, and the payroll know-how to write the policy check; a vendor bot cannot know our jurisdiction rules. | 02 (build or buy) |

## The five AI blocks
| Block | Our answer | Comes from |
|---|---|---|
| 10. Data — sources, rights, gaps | Help center (ours) and the customer's question; tickets contain customers' employee data, we are the processor (DPA). Synthetic data in the course. Gaps: languages other than English and French, legal topics, pay figures. | `governance.md` S1–S3 |
| 11. Model — rung per part | Rules (guard, policy check) · TF-IDF + logistic regression (route) · TF-IDF (retrieve) · pretrained model with retrieved passages (draft). We orchestrate: hosted model via an EU API, our own retrieval and eval-set. | 03 brief §5, 02 memo §5 |
| 12. Evaluation — the eval-set and its size | `evals/eval_set_v0.csv`: 20 → 50 cases; `evals/eval_set_v1.csv`: 100 cases (Assignment 5) → 200 (production standard, next step); labelled before the run, two graders per output, never used to tune. Two graders agree 30 / 30 on the golden rows, the LLM judge 29 / 30; a ticket with a pay or legal question is person only as a whole (E95 rule). | `evals/` |
| 13. Human in the loop — trust level per step, way back to a person | L3 on "how do I…" (10 % sampled in the pilot, 5 % at steady state), person only on anything with an amount or a named employee; "talk to a person" always visible; override switch for the Head of Support. | 03 brief §2 |
| 14. Risks & governance — what it must never do, rollback trigger | Never state, compute or confirm an amount. Go back one adoption step if the 7-day reopen rate exceeds the human baseline for two weeks, or one amount leak is found in sampling. | `governance.md`, 02 memo §3 |
