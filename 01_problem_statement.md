# 01 — Problem statement

**Team:** OG Albert (M2-INTER-2) · **Agent:** P1 — Tier-1 deflection agent for an HR & payroll SaaS · **Last updated:** 9 Nov 2026

> Every number says where it comes from: **measured** (company log, from the P1 proposal), **analogy** (a comparable, with its source) or **guess** (and how we will test it).

## 1. The problem in one sentence
**HR managers and payroll officers at our 2,500 customer companies** wait for a human answer to "how do I…" questions that the help center already answers, **especially at payroll close**, which ties up more than half of a 60-agent support team on repeat questions (≈ €2.6M of support time a year). Today they open a ticket and wait while agents copy-paste help-center articles. **Success** means at least 45 % of in-scope "how do I…" tickets resolved without human touch and not reopened within 7 days, with **zero** answers containing an employee's pay figure.

| Number in the sentence | Value | Measured / analogy / guess | Source or test |
|---|---|---|---|
| Customer companies | 2,500 | measured | P1 proposal (company numbers) |
| Tickets per month | 40,000 | measured | P1 proposal — ticketing log |
| Support agents | 60 | measured | P1 proposal |
| Share "how do I…", already in the docs | 55 % | measured | P1 proposal — ticket tags |
| Cost of one ticket handled by a human | €10 all-in | analogy | 60 × €45k ÷ 480k tickets = €5.6 of agent time + team leads, QA and tooling (class guide) |
| Support time spent on "how do I…" | 55 % × 480k × €10 ≈ €2.6M / yr | derived | from the rows above |
| Target deflection on the automatable share | ≥ 45 % | guess → S4 test | flip point of `02_sizing.xlsx` (≈ 43 %); measured on 200 real tickets with the S4 prototype |

## 2. Problem tree — from symptom to cause
- **Symptom** (what people complain about): "Support takes two days to answer at month end"; agents say they burn out at payroll close.
- **Problem** (what is actually going wrong): more than half of the tickets are questions already answered in the documentation; humans spend their time re-sending articles instead of handling pay-figure issues that really need them.
- **Root cause** (5 Whys):
  1. Why do customers open a ticket? — They cannot find the answer in the help center at the moment they need it (in the middle of a payroll run).
  2. Why can't they find it? — Search is keyword-based, articles are written in product vocabulary ("variable element"), customers ask in payroll vocabulary ("bonus for March").
  3. Why does nobody fix the articles? — The content team does not see which questions repeat: ticket tags are too coarse and nobody links tickets to articles.
  4. Why is there no feedback loop? — Support is measured on tickets closed, not on tickets prevented.
  5. Why? — Self-service has never had an owner or a metric.
- **What would fix the cause:** a mix — (a) a **documentation and process fix** (an owner and a "tickets prevented" metric for the help center) and (b) **GenAI** to bridge the vocabulary gap at the moment of need: understand a payroll question in natural language, find the right article, answer with a citation, and report the questions the docs do not cover (documentation-gap tickets).

## 3. Is AI the right tool?
| Question | Our answer |
|---|---|
| Is there a rule that solves 80 % of it? | No. A decision tree or an FAQ covers the top 20–30 questions; the long tail (≈ 1,500 articles, free-text questions, two vocabularies) is not rule-shaped. We still keep rules where they win: hard routing of anything with an amount or an employee name to a human. |
| Is it a prediction / generation problem, or an organisational decision? | Retrieval + generation (find the article, rephrase it for this question, cite it) plus a routing decision (answer / escalate). Pay figures and legal interpretation remain human decisions. |
| Do we have the data — which, how much, who owns it? | Yes: the help center (owned by us, ~1,500 articles), 12 months of tickets with tags and resolutions (~480k tickets; customer data processed under our B2B contract — DPA). We do **not** need employees' payroll data for "how do I…" questions, and the agent will not see it. |
| What does one error cost — and who pays it? | A wrong "how do I" answer: ≈ €8 (the customer asks again, a human handles a reopened ticket). A wrong legal deadline: ≈ €300 (late-filing penalty, goodwill credit) — paid by the customer first, then by us in trust. A wrong pay figure: ≈ €500 + labour-law exposure — this is why it stays human-only. |

**Level chosen:** **agent with retrieval (GenAI)** at L3 on documentation questions, with a rule-based router in front. **Why not the level below:** classical ML (intent classifier + canned answers) handles the top intents but not the long tail and cannot rephrase an article to a specific question; we still use a classifier-like rule to route money questions to humans.

## 4. Why this agent — the four selection questions
| Criterion | Our answer, one line |
|---|---|
| High frequency — is the work done every day or every hour? | Yes: ~22,000 "how do I…" tickets a month, ~1,000 per working day, with month-end peaks. |
| Bounded decision space — can we list its tools and outcomes on one slide? | Yes: tools = help-center search, ticket hand-off, doc-gap ticket; outcomes = answer with citation / ask a clarifying question / escalate. |
| Measurable success — can we say in one sentence whether it succeeded on one ticket? | Yes: resolved without human touch **and** not reopened within 7 days. |
| Recoverable failure — if it is wrong, is the damage limited and reversible? | Yes on documentation questions (the customer asks again); **no** on pay figures and legal deadlines — which is why those are out of scope (L1, human only). |

## 5. Press release (Working Backwards)
*Paris, 1 June 2027.* From today, HR managers in our 2,500 customer companies get an instant, cited answer to their "how do I…" questions directly in the payroll screen, even at 11 pm on closing day. In the pilot, half of these questions were resolved in under a minute without waiting for support, and support agents now spend their payroll-close week on the cases that need a human: pay errors and legal questions. Every answer links to the help-center article it comes from, and anything involving an employee's pay is passed to a payroll specialist. "In March I closed payroll for 140 employees without opening a single ticket — and when I asked about a bonus amount, I was put straight through to a person," says an HR manager at a 200-employee customer.

## 6. What would have to be true?
| # | Hypothesis | Measured / analogy / guess | How we will test it | Session |
|---|---|---|---|---|
| 1 | ≥ 45 % of automatable "how do I…" tickets are resolved without a human and not reopened within 7 days | guess | Replay 200 real tickets through the S4 prototype; graders check resolution + citation | S4 prototype |
| 2 | 68 % of "how do I…" tickets are answerable from the current help center | analogy (class worked example) | Manual audit of 200 tagged tickets against the help center | S3 / S4 |
| 3 | The router sends 100 % of pay-figure questions to a human (no L1 leakage) | guess | Eval-set with an oversampled slice of money questions; target 0 leaks | S5 metrics |
| 4 | Deflection does not drop during month-end / year-end (seasonal drift) | guess | Segment the A/B results by period (month-end vs mid-month) | S6 A/B |
| 5 | Deflected customers are not less satisfied (CSAT not lower than human answers) | guess | Counter-metric in the A/B test | S5 / S6 |

## 7. Do-nothing baseline
In 12 months without the agent, the problem does not stay still: volume grows with the customer base (+10 %/year guess), the content team keeps improving articles and agents get faster with macros — we price this at **≈ 3 % efficiency gain a year (≈ €144k)**, not zero. The month-end peak and agent burnout remain, and the next-best use of the same team would be a **help-center search revamp + in-app month-end checklists** (no GenAI), worth ≈ €150k a year: that is the hurdle our agent has to beat in `02_sizing.xlsx`.
