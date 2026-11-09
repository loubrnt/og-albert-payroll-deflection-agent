# 04 · Architecture — OG Albert · Tier-1 payroll documentation deflection agent

> **Status: v0, design only. The prototype is not built yet.** This file describes the design in `03_product_brief.md` and `spec.md`. Once `/prototype` exists, every line must be checked against it, and §6 and §8 completed.

## 1. One-line description
An agent that answers HR managers' "how do I…" payroll questions from the help center with a cited article, and hands anything touching an amount, a named employee or a legal deadline to a person.

In the prototype, a person approves every draft (L2). In production, answers go out on documentation questions with 5 % sampling (L3).

## 2. The diagram

```
ticket ─▶ [1 router] ─▶ [2 guard rule] ─▶ [3 retrieve] ─▶ [4 draft] ─▶ [5 policy check] ─▶ ⊘ approval ─▶ sent + logged
              │              │                 │                            │          (prototype: every draft
              │ low          │ human-only      │ no passage                 │ block     production: 5 % sampled)
              │ confidence   │ topic           │ above the floor            │
              ▼              ▼                 ▼                            ▼
          ⊘ abstention ─────────────▶ human queue, with passages and reason ◀┘

⏻ switch: the Head of Support can turn the agent off for everyone, for one category or for one customer
```

## 3. Component table

| # | Component | Rung (1 rules · 2 classical ML · 3 pretrained model · 4 custom) | Pattern | Trust level | Checkpoint ⊘ | Metric |
|---|---|---|---|---|---|---|
| 1 | Router: TF-IDF + logistic regression → category and confidence | 2 | routing | L4 above the threshold | abstention below the threshold | routing accuracy; recall on human-only tickets |
| 2 | Guard rule: amount, rate, contribution, deadline, refund, price, legal, named employee | 1 | routing | L4, can only escalate | abstention on every human-only topic | drafts on human-only tickets (must be 0) |
| 3 | Retrieval: TF-IDF by section, top 3 | 2 | prompt chaining (augmented LLM) | L3 | none; a retrieval floor triggers `NO_DRAFT` | hit@3 |
| 4 | Draft: pretrained model, passages only, "cite or abstain" | 3 | prompt chaining | L2 in the prototype · L3 in production | approval in the prototype · 5 % sampling in production | answers two graders would send without editing |
| 5 | Policy check: blocks any amount, deadline or refund promise | 1 | prompt chaining (gate) | L4, can only block | abstention: the reason is shown, the draft cannot be approved | policy misses (must be 0) |
| 6 | Send and log | — | — | person only in the prototype · L3 in production | approval in the prototype | 7-day reopen rate (live traffic only) |

## 4. Workflow or agent?
**A workflow.** The path can be drawn in advance: classify, guard, retrieve, draft, check. Each step can fail in a known place with a known fallback, the cost per ticket is predictable, and the rules that protect pay figures do not depend on the model's judgement. An agent choosing its own tools would put a pay-figure answer one jailbreak away, for no benefit on a bounded task. To move a step up, the eval-set would have to show that tickets really need a path we cannot draw in advance; multi-question tickets would be the first candidate.

## 5. Fallbacks
- **Retrieval finds nothing:** no passage above the floor → `NO_DRAFT`, escalate. The model never answers from general knowledge.
- **Confidence below the threshold:** escalate, with the category and the passages shown to the person. The threshold is still to be calibrated, on a set separate from the eval-set.
- **Policy check blocks the draft:** the reason is shown to the person; no draft can be approved.
- **API down:** escalate; the ticket goes to the human queue.
- **Language other than English or French, two questions with one on pay or a deadline, or an article older than 6 months:** escalate.

## 6. The override switch ⏻
- **Who can switch it off:** the Head of Support (owner of the agent in `governance.md`). A named person and a night-time backup are still to be set.
- **Scope:** everyone · one category · one customer.
- **Tested on:** not tested yet. A date and the people who ran the test must be added here once it has been done.

## 7. Data
- **Training and demo data:** synthetic help center of 12 articles in `kb/` (branch `a3-mvp-brief`). Synthetic router training tickets are still to be created.
- **Evaluation data:** `evals/eval_set_v0.csv`, 20 synthetic cases today, 50 for Assignment 4, 200 for Assignment 5. Inputs and labels were drafted by an AI assistant: the team must review the labels by hand before any run. Never used for tuning; any ticket looked at while building is named in `evals/report_v0.md`.
- **Personal data:** none in this repository. In production, employee payroll data is not sent to the model and retrieval is limited to the shared help center (see `governance.md`).

## 8. Eval result v0
Not run yet: the prototype does not exist. Criterion to report against: at least 45 % of automatable "how do I…" tickets get an answer two graders would send without editing, with zero answers stating an amount.

## 9. What we would build next
To be written from the three most frequent misses of `evals/report_v0.md`.
