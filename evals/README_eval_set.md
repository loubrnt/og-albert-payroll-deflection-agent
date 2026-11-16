# The eval-set — origin and rules for our project

`eval_set_v0.csv` holds our cases; one row is one ticket the agent receives, with the answer or action a good system would give.

## Origin — read this before trusting a number
- The **inputs are synthetic**: five tickets were written by hand, an AI generated variants (typos, two questions in one, French, an angry tone), and 20 were kept. Never real customer data.
- The **expected outputs and hand-over labels were drafted by an AI assistant, not yet by a team member**. They must be reviewed and corrected by the team: whoever did not write a case reviews its labels. Until that review is done, the `origin` column says "team review pending".
- The help center behind `expected_article` is the 12 synthetic articles in `kb/`.

## Columns
| Column | Meaning |
|---|---|
| `id` | E01… |
| `input_the_agent_receives` | the ticket text as the agent sees it |
| `expected_output_or_action` | what a good answer or action looks like, specific enough for two graders to say yes / no |
| `evidence_or_source` | the article and section the answer comes from |
| `hand_over_to_a_person` | yes / no, and the trust level |
| `segment` | language · plan |
| `origin` | where the case and its label come from |
| `notes` | why the case is in the set |
| `expected_category` | `how_do_i`, `pay_legal`, `billing` or `product` |
| `expected_decision` | `draft` or `escalate` |
| `expected_article` / `expected_section` | the help-center article and section, for `draft` cases |

## Rules
- 20 cases for Assignment 3, 50 with Assignment 4, 200 by Assignment 5.
- Label before running the prototype and never change a label because of its output.
- Never tune the prompt, the rules or the thresholds while looking at these rows. A row that was looked at while building is demo data: say so in `evals/report_v0.md`.
- "Sendable" is judged by two people on each output, independently. The script counts outputs; the people decide.
- Mix kept on purpose: easy and hard cases, ten that must be handed over to a person, a French ticket, and tickets with an amount or a deadline hidden in a how-to question.
