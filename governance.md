# Governance — our living file

> Created for Assignment 1, one line added every session. One question at the oral is drawn from this file.
> Answers are provisional: write what you know today, and mark what you still have to check.

## Session 1 — the six questions
| # | Question | Our answer (provisional) | To check with |
|---|---|---|---|
| 1 | **EU AI Act:** which risk tier is our agent in, and why? | **Limited risk — transparency obligation (art. 50):** it is a chatbot talking to people, so the widget says "AI assistant" on every answer and offers "talk to a person". It is not high-risk: it does not decide on employment, pay, promotion or termination (Annex III §4) — answers about pay figures are excluded by design. If scope ever moved to individual pay decisions, it would become high-risk. | Legal counsel / DPO — confirm the Annex III reading |
| 2 | **Data:** whose data does it use, and on what legal basis? | The help center (ours) and the customer's question. Customers' tickets are processed as **processor** under the B2B contract and DPA (GDPR art. 28); our own use of past tickets to build the eval-set = legitimate interest (art. 6(1)(f)), pseudonymised. Employee payroll data is **not** sent to the model. EU hosting; the LLM provider must not train on our data. | DPO; check the DPA allows LLM sub-processors |
| 3 | **Accountability:** who is accountable when it is wrong — and where is the human? | The **Head of Support** owns the agent's answers (product owner). Humans: reviewers sample ~5 % of answers, read every escalation, and any customer can ask for a person in one click. | Head of Support (to name) |
| 4 | **Never:** what must it never do? | **Never state, compute or confirm an amount** (salary, bonus, contribution, net pay) or anything about a named employee — it escalates to a payroll specialist (L1, human only). | Eval-set: 0 leaks on the money slice |
| 5 | **Explainability:** explainable to whom? | To the **customer**: every answer cites the help-center article it comes from. To the **support agent**: the escalation note says why it escalated. To the **auditor**: logs of question, retrieved articles, answer, model version. | Monitoring owner |
| 6 | **The people it cannot serve:** what happens to them? | Questions outside the docs, other languages, pay-figure questions, users who prefer a human: immediate hand-off to the human queue with the conversation attached — never a dead end. Repeated unanswered questions open a documentation-gap ticket. | Support team lead |

## Session 2 — the cost of error
- Which cost-of-error line is a **legal or reputational** risk, not just money? **Legal & payroll-rule deadlines** (a wrong DSN/URSSAF or leave-rule deadline can make the customer file late and pay a penalty — and the error depends on jurisdiction/collective agreement), and **pay figures** (a wrong amount quoted to an HR manager can end in a labour-law dispute and a public loss of trust). That is why both are out of scope in the base case (`02_sizing.xlsx`, Include = 0); legal deadlines enter only with a jurisdiction check, in the optimistic scenario.
- Who in the company **owns** that risk? The **Head of Legal & Compliance** owns the legal-deadline content and its validation; the **Head of Support** owns the agent and the escalation rule; the DPO owns the data line.

## Session 3 — data (to come)
## Session 4 — human-in-the-loop points and the override switch (to come)
## Session 5 — counter-metrics and the segments we report (to come)
## Session 6 — protected segments and the harm threshold that stops an experiment (to come)
## Session 7 — accountable owner, rollback authority, incident path (to come)
