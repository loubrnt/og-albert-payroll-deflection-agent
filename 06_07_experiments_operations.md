# 06_07 - Experiments & operation - OG Albert - Tier-1 deflection agent (P1, HR & payroll SaaS)

> Sessions 6 + 7 deliverable. Every number traces to `02_sizing.xlsx` (`Sheet!Cell`), `05_metrics.md` (§) or `evals/report_v0.md` (§); a number that is derived shows its calculation. Every owner is a role named in `governance.md` or in the sizing (a person is still to be put on each role). Every threshold has a clock.

## §1 Prove the effect - hypothesis, unit, design (in words)

**Hypotheses** (one per business metric of `05_metrics.md` §4):

1. **Tickets resolved without a human.** If we let the agent answer the automatable "how do I…" tickets of a random half of our customer companies (English and French, Scale and Start plans), the share of those tickets closed without a human touch and not reopened within 7 days is at least **45 %** (the criterion of `report_v0.md` §1) in the treated half, against the rate of the untreated half measured at the same time, by the end of the run - without the 7-day reopen rate going above that of the untreated half, and without a single answer that states an amount. The baseline is not in the repository: the untreated half measures it during the run, which is why this is an experiment and not a before/after.
2. **Net annual value.** If the treated half reaches the measured deflection of hypothesis 1, then the net annual value computed with the **measured** deflection, error and supervision lines (instead of the guesses `Inputs!D22`, `D26`, `D52`) is above the hurdle of 150,000 € (`Inputs!D60`). From the sensitivity of `Decision!A32:C36`, the flip point is about 43 % and each point is worth about 8.2 k€ a year (`05_metrics.md` §2). This is a calculation made after the test, not a second experiment.
3. **No loss of quality (non-effect).** If we do the same, the 7-day reopen rate and the CSAT of the treated half stay inside the band of the untreated half (`05_metrics.md` §4, row 3); the band width is read from the untreated half during the run and written in §2 before the decision.

**Unit of randomisation: the customer company** (2,500 companies, `README.md`; 40,000 tickets a month, `Inputs!D6`) - not the ticket, because one company sends several tickets on the same topic, and a customer who got an agent answer and then a human one to a follow-up would sit in two arms; a reopen would be counted in the wrong arm. The remaining leak is the **support agents**: the 60 agents (`Inputs!D7`) work on both arms and may reuse the wording of the drafts in control tickets. That leak makes the control better, so it **under-estimates** the effect; we also read the control tickets' wording for copied phrasing.
**Design:** A/B on companies, 50 / 50, preceded by one week in shadow mode (the agent drafts on all tickets, nobody sees the drafts, a human sample grades them) to check the guardrails before any customer is exposed. What it cannot see: (a) the learning effect of the agents over several months; (b) a change in how customers phrase their questions once they know they talk to an agent; (c) the effect of the next product release (`governance.md` S3: the help centre lags behind releases); (d) a full year: the run covers one month end, not the year-end close.

## §2 Decide before - duration and decision rule

**Smallest improvement that still justifies the agent, and why:** the treated half must reach **45 %** of the automatable tickets resolved without a human and not reopened (criterion of `report_v0.md` §1), because from about 43 % the base case clears the hurdle and do-nothing (`Decision!C33`: 164,682 € at 45 % against 150,000 €); below 43 % the net value is under do-nothing (144,000 €, `Decision!D22`).
**Slowest guardrail to read → how long we run:** CSAT (weeks), then the 7-day reopen rate (a ticket sent on the last day is read 7 days later). We run **one calendar month, so that the run contains the month-end peak** (`README.md`: peaks at month end), and read the result 7 days after the last ticket.

| Input | Value | Source |
|---|---|---|
| Baseline p0 - an outcome that exists with and without the agent | the share of automatable tickets closed without a human and not reopened in the **untreated half**, read during the run | not in the repo yet; this is what the control arm is for |
| Smallest rise worth acting on | up to the 45 % of the treated half (flip point about 43 %) | `Decision!A32:C36`, `report_v0.md` §1 |
| Two risks accepted (false win · missed win) | 1 in 20 · 1 in 5 | preset in the calculator |
| Units per group | **not computed**: `evals/sample_size.xlsx` needs p0, which we only know after the control arm runs. For scale: the course's worked example for P1 needs about 330 per group for a 10-point rise from 25 % | course template S6_7 (README) |
| Volume per week | *derived*: 14,960 automatable tickets a month (`Upside!D9`) × 12 / 52 = **about 3,450 a week**, split between the two halves | `02_sizing.xlsx` |
| **Duration actually run** | one calendar month (+ 7 days of reading) | the slowest guardrail |

**Pre-registered segments** (the S5 list, `05_metrics.md` §3): language (English, French) · plan (Scale, Start) · category (answerable, human-only) · month-end against the rest of the month.
**Decision rule, written on 16 November 2026, before the first unit** (frozen by the commit of this file):
- **Ship** (scale beyond the pilot) if the treated half reaches ≥ **45 %**, the 7-day reopen rate and CSAT are inside the band of the untreated half, the wrong-answer rate is ≤ **4 %** (`Inputs!D26`) in **every** segment, and there is **zero** amount leak and **zero** draft on a human-only ticket.
- **Iterate** (stay in the pilot, fix, re-run on a new sample) if the treated half is between 43 % and 45 %, or one segment is above 4 %.
- **Kill** if the treated half is below **43 %** (flip point), or the 7-day reopen rate is above the untreated half's for two weeks in a row (`02_investment_memo.md` §3).
- **Stop early only if** the harm threshold of `governance.md` (Session 5) is reached: one amount leak in the sample, or the reopen rate above the human baseline for two weeks, or a wrong-answer rate above 4 % in a segment - never on a good number, and never to look.

## §3 Watch the four layers - monitoring and drift

| Layer | Metric (from `05_metrics.md`) | Threshold that pages someone | Clock | Owner | Tool - startup | Tool - large company |
|---|---|---|---|---|---|---|
| Infrastructure | pipeline errors and fall-backs to the template drafter or to humans-only | any outage that sends tickets to humans-only (`spec.md` fallbacks) | real time | on-call engineer (monitoring and on-call line, `Inputs!D54`) | platform metrics · Sentry · Grafana Cloud | Cloud Monitoring / CloudWatch · Datadog |
| Model quality | sendable drafts (level 2) on the frozen eval-set; router accuracy and hit@3 (level 1) | sendable drafts below 45 %, or any drop against the last release | at every change, and weekly on the human sample | eval owner (`Build or buy` row 05: "2 devs + 1 eval owner") | Langfuse · Phoenix | LangSmith · Langfuse self-hosted · Datadog LLM |
| Product & guardrails | amount leaks; drafts on human-only tickets; wrong-answer rate per segment; 7-day reopen rate; CSAT | **one** amount leak; one draft on a human-only ticket; wrong-answer rate above 4 % in a segment; reopen above the human baseline for two weeks | daily | Head of Customer Support | SQL table + Metabase / Looker Studio | warehouse + Power BI / Tableau / Looker |
| Business | tickets resolved without a human; net value against the hurdle | deflection below the flip point (about 43 %) over a full month | monthly | Head of Customer Support with Finance | weekly query + a sheet | BI dashboard |
| Paging | - | - | - | on-call engineer | Slack webhook | PagerDuty / Opsgenie |

**Where the service runs:** today the prototype is a **Streamlit app on the team's laptops** (`prototype/app.py`): there is **no FastAPI service in the repository yet**. For a pilot we would wrap the four steps in a FastAPI service on Cloud Run or Render **in an EU region** (EU hosting is a condition in `02_investment_memo.md` §5 and `governance.md` Session 1); secrets in `.env`, never in Git.
**Release path and gates:** dev (every commit: the rules and `prototype/test_switch.py`) → staging (every change of prompt, model, sources or guard list: the 100-case eval-set and the judge, then shadow mode; the laptop is our staging) → production by the adoption steps of the sizing (20 → 40 → 60 → 70 %, `Inputs!D39:D42`), each step guarded by the harm threshold and by no amount leak in the sample (`Inputs!G40`: Q2 only if the 7-day reopen rate holds and there is no leak).
**First drift expected: knowledge drift** - the product ships a release and the help centre lags behind it (`governance.md` S3: "questions about the last release"; Q3 note of `Inputs!G41` on the year-end close). Signal: the share of tickets that end in `NO_DRAFT` because no passage is found goes up, and documentation-gap tickets repeat. What we re-run: the frozen eval-set (`evals/eval_set_v1.csv`, golden 30 included) at every release of the product, every change of the help centre and every model version; the human sample of the week reads the new topics first.

## §4 Contain the incident - trace, classes, rollback

**Trace - one OpenTelemetry trace per ticket, one span per step of `04_architecture.md`:** `request` (ticket id · timestamp · language · plan · versions of rules, model and help centre · latency) → `route` (category · confidence) → `guard` (draft or escalate · reason) → `retrieve` (passages and scores · no-hit) → `draft` (text · citations · latency · cost) → `policy_check` (pass or block · reason) → `human_decision` (approved · edited · escalated · sent · human grade if sampled · judge label). Stored in **Langfuse (EU cloud) for the pilot**, kept **12 months** like the tickets and logs (`governance.md` S3: purpose limitation).
**Our one-page dashboard - five panels:** stat tiles with thresholds, "am I paged?" (amount leaks, drafts on human-only tickets, 7-day reopen, wrong-answer rate) · line over time, "trend or spike?" (tickets resolved without a human per day) · histogram this week against last, "has the router's confidence drifted?" · bars by segment (language × plan), "is one group served worse?" (fairness, `05_metrics.md` §3) · worst-cases table, "what do we fix on Monday?" (policy blocks, low-confidence drafts, reopened tickets). Built as a Streamlit tab next to the inbox for the pilot.

| Class | Example on our agent | Action |
|---|---|---|
| Caught | the policy check blocks a draft that contains a contribution rate, or the guard escalates a how-to ticket that also asks for the minimum wage (`report_v0.md` §2, case B) | counted; weekly review; a spec line if it repeats |
| Sent wrong | a draft cites the right article but the wrong section and the customer reopens within 7 days (`report_v0.md` §2, row 3) | counted in the wrong-answer rate; fixed in the next release, validated on new cases |
| **Harmful** (above the harm threshold) | a ticket without an article gets a draft that sends a how-to path for a pay or legal question, or an answer states an amount (`report_v0.md` §2, case A) | **rollback now** (below), incident report, DPO informed if personal data is involved |
| Outage | the model or API is down, or retrieval returns nothing for everyone | fall-back to the template drafter; if the pipeline is down, humans-only automatically; page the on-call engineer |

**Rollback plan**

| Field | Ours |
|---|---|
| 1 · Trigger | any event of the harm threshold of `governance.md` S5 (one amount leak in the sample · reopen rate above the human baseline for two weeks · wrong-answer rate above 4 % in a segment), or an outage not solved when the pager fires |
| 2 · Who decides (day / night) | day: the **Head of Customer Support** (or a delegate); night: the **on-call engineer**, who may move the system to off or suggest-only on a leak or an outage and tells the Head of Customer Support the next morning |
| 3 · The action | first **suggest-only** (drafts are shown to the agent, only a human sends); **off** when the trigger is an amount leak or an outage; **redeploy the previous version** of rules, model or help centre when the trigger follows a release |
| 4 · Time to execute | prototype: the state file is read on every ticket, so the change applies to the **next ticket** (the test below: 5 tickets handled in 0.00 s after the switch). Production: a target is set with the Head of Customer Support at the first live test; no number is claimed before |
| 5 · What people see | agents: the inbox shows the state and the ticket arrives in the human queue with the reason **"agent off"**; customers: "talk to a person" is always visible, so there is no dead end (`governance.md` Q6) |
| 6 · Last tested | **16 November 2026**, on the prototype (the laptop is our staging), with `prototype/test_switch.py`, run from `cristianlrn`'s laptop: off → the next 5 demo tickets went to the human queue with the reason "agent off"; suggest-only → the 5 outputs marked suggest-only; back on → the pipeline ran again. Evidence: `data/switch_log.jsonl`. **Passed.** Next test: 26 November, before the launch memo, by a second team member |

## §5 Own the system - the five owners

| Decision | Owner (role) | Written where |
|---|---|---|
| Run an experiment on real users | **Head of Customer Support** signs (owner of the agent); the **DPO** reads it before the start | this file §1-§2 · `governance.md` S6 |
| Read the weekly numbers and act | **Head of Customer Support** (guardrails, product, business rows); the **eval owner** (model-quality row) | §3 |
| Press the switch (day / night) | **Head of Customer Support** (day); **on-call engineer** (night) | §4 · `governance.md` S7 |
| Approve a release (prompt, model, sources, guard list) | **Head of Customer Support** and the **eval owner** together; the **Head of Legal & Compliance** for the guard list | `evals/README.md` |
| Keep the trace; answer a customer or a regulator | the **DPO** for a regulator and for data requests; the **Head of Customer Support** for a customer; trace in Langfuse (EU), 12 months | `governance.md` S7 |

*Copied into `governance.md` (Sessions 6 and 7):* who signs an experiment on real users, who can press the switch and when it was tested, where the trace lives and for how long - plus the line that the company answers for what the system says (Moffatt v. Air Canada, 2024 BCCRT 149).
