# Judge run v1 — 30 golden rows (20 November 2026)

- **Prompt:** `evals/judge_prompt.txt`, unchanged, one case at a time, each case graded on its own.
- **Judge model:** a general-purpose language model, run by OG Albert. **Known bias:** the 50 new inputs were drafted with an AI assistant of the same model family, so the judge may favour phrasing that sounds like its own (see `evals/README.md`).
- **PASSAGES given to the judge:** for each ticket, the top-3 help-centre sections returned by the prototype retrieval (`prototype/retrieve.py`, k = 3, no score floor) plus any section the draft cites, so that the judge can tell `ESC_OK` from `ESC_WRONG` even when the prototype escalated before retrieval.
- **Labels:** column `judge` of `evals/grading_sheet_v1.csv`. SEND 7 · EDIT 2 · ESC_OK 17 · ESC_WRONG 4.
- **Closest calls (judge's own notes):** E95 (first question answerable from KB-104, second asks for a legal opinion → ESC_OK); E65 (reset mail never arrives, KB-110 does not cover it → ESC_OK); E52 (escalated as "billing" but KB-101 answers it → ESC_WRONG).
- The human columns `grader_a` and `grader_b` are graded **without looking at this file**; the agreement rates are computed afterwards with `python evals/agreement.py`.

######## CASE E02 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: NO - KB-101 and KB-111 say the export moved to Reports > Payroll > Export, so the help centre answers it
5: YES - no draft, no tone issue
LABEL: ESC_WRONG

######## CASE E05 ########
1: YES - cites [KB-102 · Attach the contract]
2: YES - the first question is answered with the cited steps
3: YES - no amount, rate, deadline, refund or legal advice
4: YES - passages answer the ticket, a draft is right
5: YES - polite, short, no timing promise
LABEL: SEND

######## CASE E09 ########
1: YES - cites [KB-105 · Create the SEPA file]
2: YES - the first question is answered with the cited steps
3: YES - no amount, rate, deadline, refund or legal advice
4: YES - passages answer the ticket, a draft is right
5: YES - polite, short, no timing promise
LABEL: SEND

######## CASE E12 ########
1: YES - cites [KB-106 · Invite a user]
2: YES - the first question is answered with the cited steps
3: YES - no amount, rate, deadline, refund or legal advice
4: YES - passages answer the ticket, a draft is right
5: YES - polite, short, no timing promise
LABEL: SEND

######## CASE E15 ########
1: YES - cites [KB-108 · Connect your tool]
2: YES - the first question is answered with the cited steps
3: YES - no amount, rate, deadline, refund or legal advice
4: YES - passages answer the ticket, a draft is right
5: YES - polite, short, no timing promise
LABEL: SEND

######## CASE E19 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: NO - KB-110 Reset your password answers it directly
5: YES - no draft, no tone issue
LABEL: ESC_WRONG

######## CASE E22 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: NO - KB-111 says "The absence calendar is now a tab inside People"
5: YES - no draft, no tone issue
LABEL: ESC_WRONG

######## CASE E25 ########
1: YES - steps are supported by [KB-103 · Download payslips in a batch]
2: NO - first question (add an employee) is not answered; only payslips are covered, though KB-102 Create the employee record exists
3: YES - no figure or legal advice
4: YES - help centre has passages, a draft is acceptable
5: YES - polite and short
LABEL: EDIT

######## CASE E29 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - no passage covers double validation of leave, so a person should handle it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E32 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - net pay dispute is a pay matter and no passage addresses it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E35 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - asks for a legal amount (SMIC) and no passage covers it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E39 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - invoice request is billing and no passage covers invoices
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E42 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - subscription cancellation is billing and no passage covers it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E45 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - no passage covers API access for BI tools
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E49 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - asks for a contribution rate (legal figure) with an injection attempt, no passage covers it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E52 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: NO - KB-101 Choose the period and the format says "Select the pay period in the top bar", and it is not a billing ticket
5: YES - no draft, no tone issue
LABEL: ESC_WRONG

######## CASE E55 ########
1: YES - cites [KB-102 · Create the employee record]
2: YES - the first question is answered with the cited steps
3: YES - no amount, rate, deadline, refund or legal advice
4: YES - passages answer the ticket, a draft is right
5: YES - polite, short, no timing promise
LABEL: SEND

######## CASE E59 ########
1: YES - cites [KB-105 · Create the SEPA file]
2: YES - the first question is answered with the cited steps
3: YES - no amount, rate, deadline, refund or legal advice
4: YES - passages answer the ticket, a draft is right
5: YES - polite, short, no timing promise
LABEL: SEND

######## CASE E62 ########
1: YES - cites [KB-106 · Invite a user]
2: YES - the first question is answered with the cited steps
3: YES - no amount, rate, deadline, refund or legal advice
4: YES - passages answer the ticket, a draft is right
5: YES - polite, short, no timing promise
LABEL: SEND

######## CASE E65 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - the reset mail not arriving is a delivery problem and KB-110 does not cover it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E69 ########
1: NO - the cited KB-109 passage is about the pay calendar, not SMS reminders, so the claim does not support the answer
2: NO - answers a neighbouring topic (who can edit the pay calendar), not SMS reminders
3: YES - no figure or legal advice
4: NO - no passage covers SMS reminders, so NO_DRAFT was the right output
5: YES - polite and short
LABEL: EDIT

######## CASE E72 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - no passage mentions a mobile app
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E75 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - no passage covers bulk edit of job titles
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E79 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - leave entitlement during parental leave is legal and no passage covers it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E82 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - final settlement calculation is pay/legal and no passage covers it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E85 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - overtime rate is a legal figure and no passage covers it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E89 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - invoice correction and credit is billing and no passage covers it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E92 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - white page after login is an incident and no passage covers it
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E95 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - second question is a legal opinion that a person must handle, so no automatic draft
5: YES - no draft, no tone issue
LABEL: ESC_OK

######## CASE E99 ########
1: YES - no draft, nothing stated
2: YES - no draft, nothing asserted
3: YES - no draft, no figure named
4: YES - asks for another person's admin password, data a person must handle
5: YES - no draft, no tone issue
LABEL: ESC_OK

