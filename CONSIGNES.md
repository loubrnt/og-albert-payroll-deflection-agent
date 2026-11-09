# Consignes et rendus — Data & AI Product (MSA-DAT07-04, C. Oprean)

Équipe **OG Albert** (INTER-2) · projet **P1 — Tier-1 deflection agent, HR & payroll SaaS** (choisi dans la feuille d'inscription, même agent qu'en Agentic Workflows).

## Le cadre
On est l'équipe produit IA d'un éditeur SaaS B2B fictif (P1 : 2 500 entreprises clientes, 40 000 tickets/mois, 60 agents support, pics en fin de mois, 55 % de questions « comment je fais… » déjà dans la doc). Agentic Workflows construit l'agent ; ici on décide s'il faut le lancer et comment.

**Notation :** livrable Git = 40 % du projet, lu dans **un seul dépôt d'équipe** (fichiers 01_, 02_, 03_…) dont le lien doit être dans la ligne de l'équipe de la feuille d'inscription. Inside affiche « individual » mais la prof note par équipe. Chacun doit signer des commits dans au moins 4 fichiers numérotés (question individuelle à l'oral sur un commit signé).

## Assignment 1 — Problem statement (dû le 8 nov.)
- `01_problem_statement.md` : problème en une phrase chiffrée (chaque chiffre : mesuré / analogie / guess), arbre symptôme → cause (5 pourquoi), l'IA est-elle le bon outil, les 4 critères de sélection, communiqué de presse (Working Backwards), hypothèses à tester, baseline « ne rien faire ».
- `governance.md` : les 6 questions de la session 1 (AI Act, données/RGPD, responsabilité, ce que l'agent ne doit jamais faire, explicabilité, ceux qu'il ne peut pas servir).

## Assignment 2 — Sizing & investment memo (dû le 8 nov.)
- `02_sizing.xlsx` (modèle de la prof) : dimensionnement bottom-up Low/Base/High avec une source pour chaque entrée, les 7 lignes de coût, 3 scénarios + probabilités → valeur attendue, comparaison avec « ne rien faire » et le projet alternatif (le seuil), point de bascule, onglet Build or buy.
- `02_investment_memo.md` : une page, ligne 1 = décision, puis Combien ? Quelle certitude ? Et si on se trompe ? Comparé à quoi ? + build / buy / orchestrate.
- `governance.md` : lignes de la session 2 (quel coût d'erreur est un risque légal ou réputationnel, qui en est propriétaire).

**Résultat :** CONDITIONAL GO — valeur attendue ≈ 301 k€/an (base 206 k€, pessimiste −202 k€, optimiste 994 k€) contre un seuil de 150 k€ ; la décision bascule à ≈ 43 % de déflection → condition : ≥ 45 % sur 200 vrais tickets avec le prototype S4. Montants de paie et délais légaux hors périmètre. Recommandation : orchestrate.
Les chiffres marqués *guess* / *judgement* sont des hypothèses : à relire et corriger si besoin.

## Ce qu'il faut rendre sur Inside (chacun — en retard mais accepté)
Inside → My courses → Data & AI Product → Assignments :
- **Assignment 1** : `README.md`, `01_problem_statement.md`, `governance.md`
- **Assignment 2** : `02_sizing.xlsx`, `02_investment_memo.md`, `governance.md`

## À venir
- **Assignment 3** (MVP brief & design loop) : énoncé daté du 8 nov., pas encore fait, pas d'espace de rendu sur Inside.
- **Assignment 4** (prototype & architecture) : **15 nov. 23:59, sur ce dépôt** — prototype (4 commits, un auteur chacun), `evals/report_v0.md`, `04_architecture.md`, `spec.md` v2, eval-set à 50 cas, section S4 de `governance.md`.
- À faire : mettre le lien de ce dépôt dans la ligne OG Albert de la feuille d'inscription, et que chacun remplisse sa ligne (onglet Students) avec son handle GitHub.
