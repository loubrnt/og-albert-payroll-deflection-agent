# 03 — Product brief · Tier-1 deflection agent · v1

**Team:** OG Albert · **Starting point:** P1 · Tier-1 deflection, HR & payroll SaaS · **Version:** v1 — 9 November 2026 (v2 waits for the user conversations, see §9–10)

> Same base case as `02_sizing.xlsx` and `02_investment_memo.md`. Source type in brackets: **measured** · **analogy** · **guess**.

## 1. Problem, user, do-nothing  *(from 01 and 02)*
- **Problem in one sentence (with a number):** 55 % of our 40,000 monthly tickets are "how do I…" questions already answered in the help center [measured, P1 proposal]; handled by hand they cost about €2.6M a year [55 % × 480k tickets × €10, derived] and pile up at payroll close.
- **User (persona):** *Camille*, HR manager in a 200-employee customer company — closes payroll on the last two days of the month, asks "how do I…" in the in-app widget, wants the answer in the middle of the payroll run. Behind her, *Inès*, tier-1 support agent — samples the agent's answers and receives every escalation; her pain is re-sending the same articles at month end.
- **Do-nothing baseline:** the process improves by itself, about 3 % a year [guess] ≈ €144k; the real alternative is the *help-center search revamp + month-end in-app checklists* project, ≈ €150k a year [guess] — the hurdle in `02_sizing.xlsx`.
- **Where the numbers stand:** base case €206k net, expected value €301k, flips at ≈ 43 % deflection. The decision is CONDITIONAL GO on **≥ 45 %**.

## 2. The process — as-is and to-be
Minutes and error rates are **guesses** until a time-and-motion sample of 30 tickets replaces them. Error costs come from `02_sizing.xlsx` (Inputs rows 30–32). The as-is total of 11 minutes of human time is consistent with the €5.6 of agent time per ticket computed from headcount (Inputs row 10).

| # | Step | Who today | Minutes | Error rate | Cost of an error | Automate / augment / keep human (test it fails) | Trust level | Minutes after | Metric for this step |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Read the ticket | agent | 1.0 (guess) | 2 % (guess) | misread → wrong answer, ~€8 | automate (fails none: read-only) | L4 | 0 | share of tickets parsed without error |
| 2 | Decide whether it is a "how do I…" and may be answered | agent | 0.5 (guess) | 5 % (guess) | a legal-deadline ticket treated as how-to ≈ €300; a pay-figure ticket ≈ €500 | automate **with a hard guard** (fails "low tolerance for error" on legal and pay topics → rule + escalate) | L4 above a threshold, otherwise person | 0 | routing accuracy; recall on human-only tickets |
| 3 | Search the help center | agent | 4.0 (guess) | 10 % wrong article (guess) | ~€8 (customer asks again) | automate | L3 | 0 | retrieval hit@3 |
| 4 | Draft the reply | agent | 3.0 (guess) | 4 % (analogy, class sheet) | ~€8 | automate on "how do I…", keep human elsewhere | L3 (5 % sampled) | 0.2 (sampling) | answers two graders would send without editing |
| 5 | Check the reply holds no amount, deadline or refund | agent | 1.0 (guess) | 3 % (guess) | ~€300–500 + contract risk | automate as a rule that can only block | L4 | 0 | drafts on human-only tickets (must be 0) |
| 6 | Send and log | agent | 1.5 (guess) | 1 % (guess) | ~€2 | automate | L3 | 0 | 7-day reopen rate |
| 7 | *(new)* Escalate with context | — | — | — | a customer waiting | keep human; pre-written context saves ~2 min | person only | 9 (instead of 11) | time to first human answer |

**Total:** 11 minutes of human time per "how do I…" ticket today → about **0.2 minutes** (sampling) when the agent answers; 9 minutes when it escalates.

**Where the pain sits (the two steps):** step 3 (search, 4 min) and step 4 (draft, 3 min) — 64 % of the handling time.
**The way back to a person (designed first):** a "talk to a person" button always visible to the customer; every uncertain, blocked or out-of-scope ticket goes to the human queue with the retrieved passages and the reason attached; the Head of Support can switch the agent off for everyone, for a category or for one customer.
**Where the governance line sits:** between steps 2 and 5 — anything that states, computes or confirms an amount (salary, bonus, contribution, net pay), or concerns a named employee, never gets an answer from the agent; legal deadlines are escalated in year 1 (`Include = 0` in the base case).

*Trust levels — same scale as Session 1: L1 suggests · L2 drafts, a person approves · L3 acts on a scope, a person samples · L4 acts alone under a threshold.*

## 3. Features — RICE and MoSCoW
Reach = tickets a month, from `02_sizing.xlsx`: 40,000 all tickets · 22,000 "how do I…" tickets (40,000 × 55 %) · 14,960 automatable ones (22,000 × 68 %). RICE = reach × impact × confidence ÷ effort (person-weeks). Impact 0.25–3.

| Feature | Reach / month | Impact | Confidence | Effort | RICE | MoSCoW |
|---|---|---|---|---|---|---|
| Policy checker (no amount, deadline or refund) | 22,000 | 3 | 100 % | 0.5 | 132,000 | **MUST** |
| One-click escalate, with context | 40,000 | 2 | 100 % | 1 | 80,000 | **MUST** |
| Routing with a confidence score | 40,000 | 2 | 80 % | 1 | 64,000 | SHOULD |
| Eval-set of 200 tickets and the eval script | 14,960 | 2 | 100 % | 2 | 14,960 | **MUST** |
| Draft with help-center citations | 14,960 | 3 | 50 % | 3 | 7,480 | **MUST** |
| Customer-facing widget in the app | 40,000 | 2 | 50 % | 6 | 6,667 | WON'T |
| Auto-close resolved tickets | 14,960 | 0.5 | 80 % | 2 | 2,992 | COULD |
| Multilingual answers | 4,000 | 2 | 50 % | 4 | 1,000 | WON'T |

- **MUST (4):** policy checker · one-click escalate with context · eval-set of 200 · draft with citations.
- **SHOULD:** routing with a confidence score. **COULD:** auto-close resolved tickets.
- **WON'T this time (≥ 5) — the out-of-scope list, dated 9 Nov 2026:** the customer-facing widget in the MVP · multilingual answers · pay-figure and any amount-related tickets · legal-deadline tickets (year 1) · category-3 questions needing an employee's data · billing and refund tickets · any answer sent without sampling on payroll topics.
- **The feature that tests our flip assumption, and why it is a MUST:** *Draft with citations*. It is only 5th on RICE, but its confidence is 50 %: it is our riskiest assumption (can a grounded answer reach 45 % without human touch?). We build it first to learn; without it the flip point (≈ 43 %) cannot be measured.
- **The cut that hurt the most:** the customer-facing widget. Deflection is realised only when customers see the answer, and the adoption ramp in `02_sizing.xlsx` starts with a widget for 20 % of customers in Q1. The MVP tests answer quality on tickets replayed through the prototype, not customer behaviour; customer behaviour is measured in the A/B test (Session 6).

## 4. Data  *(from the six-question audit — details in `governance.md`)*
The prototype uses a **synthetic** help center of 12 articles and synthetic tickets (20 now, 50 for Assignment 4, 200 for Assignment 5), generated from a few hand-written examples and labelled by hand; no real customer data. In production: our own help center (~1,500 articles) and 12 months of tickets (~480k). Coverage: English and French only; legal-deadline and pay-figure topics excluded. Freshness: an article older than 6 months, or about a law that changed, triggers escalation. Retrieval never reads other customers' tickets.

## 5. Model — one rung per part
| Part | Rung (1 rules · 2 classical ML · 3 pretrained model · 4 hybrid) | Why the rung below fails |
|---|---|---|
| Routing | 2 — TF-IDF + logistic regression | Rules cannot cover the many phrasings of the same question. |
| Guard and policy check | 1 — rules | A model can be talked into it; a pattern on amounts, "refund", "deadline", "legal" cannot. Nothing is below rules. |
| Retrieval | 2 — TF-IDF over chunked articles | Keyword search on whole pages returns the wrong section. (Embeddings are the next rung if hit@3 < 85 %.) |
| Draft | 3 — pretrained model given the retrieved passages and a "cite or abstain" instruction | A template can only quote a sentence; it cannot answer in the customer's words. |
| Overall | 4 — hybrid | A single LLM agent "doing everything" would put a pay-figure answer one jailbreak away. |

## 6. Where it lives (integration surface)
Production: the in-app widget, next to the payroll screen (Q1 pilot for 20 % of customers, opt-in). MVP: a test screen that shows, for each replayed ticket, the route, the draft, the citations, the policy line and three buttons (send · edit · hand over). Speed: under 5 seconds. Format: short answer, numbered steps, link to the article. Fallback: "talk to a person". Log visible to Support ops, QA and the DPO.

## 7. Success criterion — one sentence
> By 22 November 2026, on **200 fresh tickets** that no one has used to tune the prototype, at least **45 %** of the automatable "how do I…" tickets are resolved without human touch and not reopened within 7 days — and **zero** answers state or confirm an amount.

*The threshold is our flip point (≈ 43 % in `02_sizing.xlsx`, rounded up to 45 %). The 50 cases of Assignment 4 are a first reading, not the test.*

## 8. Risks and rollback trigger
- Top risks: (1) a pay or legal ticket misrouted as how-to; (2) a stale article (law changed in January) quoted as current; (3) the novelty effect inflates the pilot; (4) agents see it as a replacement and stop sampling honestly.
- **Rollback trigger (one line):** go back to the previous adoption step if the 7-day reopen rate exceeds the human baseline for two weeks, or if one answer stating an amount is found in sampling.

---
*v2 only — after the users (to complete once the conversations in `03_user_research.md` have taken place)*

## 9. What the users changed
| Change | Evidence (who said / did what) |
|---|---|
| _Pending — fill only from real conversations or a session with classmates in role, said explicitly._ | |

## 10. What they could not decide
_Pending._ Likely candidates: the escalation threshold, the legal basis for processing tickets in production, who in the company may widen the scope — and who or what decides instead.
