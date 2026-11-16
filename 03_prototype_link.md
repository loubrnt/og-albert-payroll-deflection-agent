# 03 — Prototype link

> One clickable prototype of where the agent lives (the surface), made in under an hour, before Session 4. It is a question for users, not the product: fake data only.

- **Link:** https://claude.ai/artifact/6h8m583cHmBEecJ5ijjiMg — private until it is shared from the page's Share menu (to do before the user tests). The source is kept in the `prototype/` folder with Assignment 4.
- **Tool:** AI-built single-page artifact (HTML)
- **Version:** v0.1 — built from the prompt below, 8 fake tickets (4 answerable, 1 with no article, 3 human-only). v0.2 and v0.3: one line each after the user conversations.
- **The prompt we used (the brief in three paragraphs):**

```
Paragraph 1 — who uses it and for what job:
Inès is a tier-1 support agent at an HR and payroll software company. At month end she handles hundreds of "how do I…" tickets. The screen is her inbox: she opens a ticket and decides in seconds whether to send an answer prepared for her, edit it, or hand the ticket to a payroll specialist.

Paragraph 2 — what is on the screen (panels, buttons, the one thing it must never do):
Left: a list of 8 fake tickets with a route tag (HOW-DO-I, PAY/LEGAL, BILLING, PRODUCT) and a "waiting since" time. Right: the selected ticket, a draft answer in numbered steps with citations like [KB-101 · Export], a policy line ("Checked: no amount, no deadline, no refund"), and three buttons: Send, Edit, Hand over to a person. A "Talk to a person" button is always visible. The agent must never show a draft containing a pay figure, a contribution rate or a legal deadline: those tickets show "Human only — no draft" and the reason.

Paragraph 3 — the rules (routing, what is "human only", the trust level):
Only HOW-DO-I tickets get a draft, and every draft carries the caption "AI answer — you approve before sending (L2 in this prototype; L3 with 5 % sampling in production)". PAY/LEGAL and BILLING tickets are human only. Low-confidence tickets go to "Hand over" with the retrieved passages attached. Fake data only.
```

- **Screenshot:** to add in the repo (`prototype/screenshot_v0.1.png`) and link here.
- **Note on the surface:** in production the agent answers the customer in the in-app widget (see `03_product_brief.md` §6). This prototype shows the agent-inbox view, which is where the answer quality is checked before anything reaches a customer.
