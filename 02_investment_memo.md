# 02 — Investment memo (one page)

**Recommendation:** **CONDITIONAL GO** on **deflection ≥ 45 % on "how do I…" tickets, measured by 22 Nov 2026 on a 200-case eval-set, synthetic or anonymised (answers two graders would send without editing), with 0 pay-figure leaks; the 7-day reopen rate is then read in the Q1 pilot.**

> Line one is the decision. Everything below is evidence for that line. Same base case as `02_sizing.xlsx`.

| €/year, year 1 | Pessimistic | Base | Optimistic | Expected value |
|---|---|---|---|---|
| Net annual value | −€202k | €206k | €994k | **€301k** |
| Probability | 0.25 | 0.50 | 0.25 | — |
| Do-nothing (value of the current process improving on its own) | €173k | €144k | €127k | |
| Next-best project: help-center search revamp + month-end in-app checklists (the hurdle) | €150k | €150k | €150k | |

## 1. How much?
Base case, bottom-up: 40,000 tickets/month × 55 % "how do I…" × 68 % answerable from the docs × 50 % deflection = 7,480 tickets/month at steady state; with the adoption ramp (20 → 40 → 60 → 70 %, average 47.5 %) that is **42,600 tickets deflected in year 1 × €10 = €426k gross**, minus €14k expected cost of wrong answers and €3k of tokens, minus €204k of fixed costs (integration amortised, eval-set, 1.5 FTE of supervision, monitoring, re-evaluation) = **€206k net**. **Measured:** volume, headcount, the 55 % share (P1 company log). **Analogies:** €10 per ticket, 68 % automatable (class worked example), Octopus Energy adoption ramp. **The one guess that matters:** the 50 % deflection rate.

## 2. How sure?
Not very — which is why this is a conditional go. EV = €301k, but the base case is only €56k above the hurdle and the pessimistic case loses €202k (35 % deflection, slow adoption, higher error and supervision costs). **Flip point:** in the sensitivity table, the base case drops below the hurdle and below do-nothing at **≈ 43 % deflection** (30 % → €42k, 45 % → €165k). The prototype measures that number, first on 50 eval cases and then on a 200-case eval-set (no real customer data) by 22 Nov; below 45 % we do not scale beyond the Q1 pilot.

## 3. What if we're wrong?
The cost that dominates is not the model (tokens ≈ €3k/yr) but **the people around it**: supervision (€75k) and evaluation (€40k). The error tail sits in two categories, priced and excluded from the base case: legal deadlines (5 % × €300 per error would cost more than the tickets it saves) and pay figures (hard L1). **Governance line:** a wrong legal deadline or pay figure is a legal and reputational risk, owned by the Head of Legal & Compliance (content) and the Head of Support (agent, escalation rule). Kill switch: if the 7-day reopen rate exceeds the human baseline for two weeks, or one pay-figure leak is found in sampling, we go back to the previous adoption step.

## 4. Compared to what?
Do-nothing is not zero: docs and agents improve by ~3 % a year (≈ €144k of support time). The same team could instead ship a **help-center search revamp + month-end in-app checklists** (≈ €150k/yr, our hurdle). The base case and the EV clear both; **the pessimistic case does not clear the hurdle** — hence the condition, not a plain GO. Upside not priced: documentation-gap tickets reduce future volume.

## 5. Build, buy or orchestrate?
**We orchestrate** — a hosted LLM through an EU-hosted API, our own retrieval on the help center, our own router and eval-set — because payroll data, the jurisdiction guardrail and the doc-gap loop must stay ours. Weighted scores (`Build or buy` tab): Build 3.5 · Buy 2.95 · **Orchestrate 3.8**. At year-1 volume, buying at ~€0.92/resolution (Intercom Fin list price, to recheck) is cheaper by ≈ €68k/yr on the comparable lines: **we would switch to buy** if a vendor offered EU hosting, no training on our data, exportable logs and a hard "never quote an amount" rule.

*Sources: P1 project proposal (company numbers) · 02_sizing "How to fill it" (P1 worked example) · Octopus Energy ramp (S2 slides) · Klarna press release (27 Feb 2024) and Bloomberg (8 May 2025) · Zillow Group Form 8-K (2 Nov 2021) · Intercom Fin public pricing · provider token price list (rechecked on commit day).*
