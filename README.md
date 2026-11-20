# OG Albert — Tier-1 payroll documentation deflection agent

**Course:** Data & AI Product: From Diagnosis to Delivery (MSA-DAT07-04) · Albert School · shared project with Agentic Workflows
**Cohort:** M2-INTER-2

## Team
| Name | Git handle | Also in the Agentic Workflows team? |
|---|---|---|
| Alexis Maeder | AlexisMaeder | yes |
| Colin Pietri | colinpietri20 | yes |
| Mathis Meimoun | Mathmnms | yes |
| Cristian Larrain | cristianlrn | yes |
| Lou Brunet | loubrnt | yes |

## Our agent
- **Starting point:** P1 — Tier-1 deflection agent for an HR & payroll SaaS
- **The company:** HR & payroll SaaS, 2,500 customer companies, 40,000 tickets per month, 60 support agents, peaks at month end.
- **The job, in one sentence:** When an HR manager asks a "how do I…" question in the in-app widget, the agent answers from the help center with a cited article, producing a resolved ticket without human touch — and escalates anything touching an employee's pay figures.
- **Trust level per step:** L3 on documentation questions (with sampling) · L1 (human only) on anything with an amount or a named employee · legal deadlines escalated in year 1.
- **One thing it must never do:** state, compute or confirm an amount (salary, bonus, contribution, net pay).

## Repository structure
| File | Session | Status |
|---|---|---|
| `01_problem_statement.md` | S1–S2 — Assignment 1 | done |
| `governance.md` | created for Assignment 1, one line added every session | S1 + S2 + S3 + S4 done |
| `02_sizing.xlsx` | S2 — Assignment 2 | done |
| `02_investment_memo.md` | S2 — Assignment 2 | done — CONDITIONAL GO |
| `03_product_brief.md` | S3 — Assignment 3 | v1 done, v2 waits for the user conversations |
| `03_ai_lean_canvas.md` | S3 — Assignment 3 | done |
| `03_user_research.md` | S3 — Assignment 3 | guide ready, **conversations to hold** |
| `03_prototype_link.md` | S3 — Assignment 3 | prompt and link, to share before the user tests |
| `04_architecture.md` | S4 - Assignment 4 | four steps, a gate between them, a person where the money or the customer is; figures from the first eval run |
| `05_metrics.md` | S5 - Assignment 5 | five sections written; numbers traced to `02_sizing.xlsx` and `evals/report_v0.md`; judge run on the 30 golden rows on 20 November (`evals/judge_run_v1.md`); labels of the 50 new cases (E51-E100) frozen and first run on them (`evals/report_v1_fresh.md`: 29 % proxy, 4 drafts where none is allowed); the two human grader columns are pending, then the agreement rates (`evals/README.md`) |
| `06_07_experiments_operations.md` | S6 + S7 - Assignment 6-7 | five sections written; rollback tested on the prototype on 16 and 20 November (`prototype/test_switch.py`, two team members); the final push (`08_launch_memo.md`, tag `v1.0`) follows on 26 November |
| `08_launch_memo.md` | S8 | |
| `spec.md` | S3 skeleton → S4 v2 | v2 done, after the first eval run |
| `/evals`, `/kb` | from S3, S4, S5 | v0: 50 cases (labels frozen before the run, to be reviewed by the team), the run output and `evals/report_v0.md` (27 % proxy against the 45 % criterion, tag `eval-v0`, two graders still to grade); v1: 100 cases, guideline, judge prompt and judge run, grading sheet; 12 synthetic help-center articles |
| `/prototype` | from S4 | four steps (router, guard + policy check, retrieve + draft, evals + surface); run once, template drafter |
