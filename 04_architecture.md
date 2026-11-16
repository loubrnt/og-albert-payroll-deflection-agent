# 04 · Architecture — OG Albert · Tier-1 deflection agent

> Describes the prototype that was actually built (`/prototype`, run on 9 November 2026), not the one we plan. It replaces the design-only v0 of this file (written from `03_product_brief.md` and `spec.md` before the prototype existed); the v0 points the prototype does not cover yet are kept below.

## 1. One-line description
A copilot that, for the company's tier-1 support agents, routes each ticket, drafts a cited reply for "how do I…" questions from the help centre, and hands pay, legal, billing and product tickets to a person; nothing is sent without the agent in the prototype.

## 2. The diagram
```
ticket ──▶ [1 router] ──▶ [2 guard] ──▶ [3 retrieve + draft] ──▶ [4 policy check] ──▶ ⊘ agent approves / samples ──▶ sent
            TF-IDF+LR      rules          TF-IDF by section        rules (block only)
                              │ guard word · low confidence · human-only class       │ block
                              │ · language not covered · no passage                  │
                              └──────────────────────▶ escalate to a person (reason + passages) ◀┘
⏻ switch: the Head of Support can switch the agent off for everyone, for a category or for one customer
🙋 "Talk to a person" is always visible to the customer
```

## 3. Component table
| # | Component | Rung (1 rules · 2 classical ML · 3 pretrained model · 4 custom) | Pattern | Trust level (L1–L4) | Checkpoint ⊘ | Metric observed |
|---|---|---|---|---|---|---|
| 1 | Router (`router.py`) | 2 | routing (classify, then dispatch) | L4 above threshold, else person | abstention (below 0.70) | routing accuracy 70 % |
| 2 | Guard (`route_rule.py`) | 1 | routing gate | L4 (can only escalate) | abstention | drafts on human-only: 2 (must be 0) |
| 3 | Retrieve + draft (`retrieve.py`, `draft.py`) | 2 (retrieval) + 3 (draft; template in v0, model optional) | prompt chaining: retrieve → draft | L3 production · L2 prototype | approval (prototype) · sampling 10 % (production) | hit@3 31 %; cited expected section 27 % |
| 4 | Policy check (`policy.py`) | 1 | gate between draft and send | L4 (can only block) | abstention | policy blocks: 0 |

## 4. Workflow or agent?
A **workflow**: the path is fixed in advance — route, guard, retrieve, draft, check — with a gate between each step, and the model never chooses its own tools or steps. That is the right choice for a support agent whose worst error (a pay figure or a legal deadline) is costly and must be impossible, not improbable: the rules can only stop things, never invent. To move one step up (to an agent that decides to look at the customer's account, call a ticket tool, or ask a clarifying question), we would need (a) a router and guard that hold at zero drafts on human-only tickets on a fresh 200-case set, (b) account isolation tested, (c) a rollback trigger tested live.

## 5. Fallbacks
- retrieval finds nothing: `NO_DRAFT`, escalate with the reason *(v0 weakness: the floor 0.05 is too low — E27 got a draft; fixed in `spec.md` v2)*
- the model's confidence is below the threshold: escalate, the category and passages shown to the person
- the policy checker blocks the draft: the reason is shown to the person; no draft, not approvable
- the API is down: the template drafter answers with the same contract (it is the one used in v0)
- language other than English or French, two questions in one ticket with one on pay or a deadline, or an article older than 6 months: escalate *(from the v0 design; only the language check exists in the prototype)*

## 6. The override switch ⏻
- Who can switch it off: the Head of Customer Support (and their delegate). A named person and a night-time backup are still to be set.
- Scope: one ticket · one category · one customer · everyone.
- Tested on: **not yet tested** — in the prototype the switch is a button that does nothing. To test with the team before the oral: switch off, check that the next 5 tickets all go to the human queue with the reason "agent off", note the date and who did it here.

## 7. Data
- Training / demo data (`data/`): `tickets_synthetic.csv` (263 rows, generated from templates, labelled by category) and `demo_tickets.csv` (8 demo tickets for the inbox). Synthetic. The help centre (`kb/`, 12 articles) is synthetic too, written for the course.
- Evaluation data (`evals/eval_set_v0.csv`): 50 cases, inputs drafted by an AI assistant, labels drafted before the run and hashed; **review by the team pending**; never used for tuning; all 50 are demo data after the first run.
- Personal data present? No (synthetic). In production: tickets contain employees' personal data; employee payroll data is not sent to the model and retrieval is limited to the shared help centre — see `governance.md`.
- Live-traffic metric, not measurable on the eval-set: the 7-day reopen rate of sent answers (read in the Q1 pilot, see `02_investment_memo.md`).

## 8. Eval result v0
"**27 %** of the answerable 'how do I…' tickets got a draft citing the expected article and section (7 of 26) — the criterion is 45 %; **2** human-only tickets received a draft (must be 0). The two-grader number is pending." Full report: `evals/report_v0.md`.

## 9. What you would build next (3 lines max)
1. A router with more and more varied phrasings plus an embedding rung; thresholds set on a separate calibration set.
2. A maintained guard-topics list owned by the payroll specialists, and a retrieval floor calibrated on "no article" tickets.
3. A fresh 200-case eval-set (Assignment 5) and the model-based drafter, graded by two people.
