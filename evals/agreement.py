"""Agreement rates for evals/grading_sheet_v1.csv. Standard library only.

Columns used: grader_a, grader_b (the two human graders), judge (the model judge). Labels: SEND, EDIT, ESC_OK, ESC_WRONG.
Run from the repo root:  python evals/agreement.py
Prints, for each pair, the share of rows with the same label and the share with the same SEND / not-SEND reading
(the "sendable as is" reading is the one the success criterion uses), then lists the disagreements.
"""
import csv, os, sys

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grading_sheet_v1.csv")
rows = list(csv.DictReader(open(PATH, encoding="utf-8")))


def pair(x, y):
    both = [r for r in rows if r[x].strip() and r[y].strip()]
    if not both:
        return None
    same = sum(r[x].strip().upper() == r[y].strip().upper() for r in both)
    same_send = sum((r[x].strip().upper() == "SEND") == (r[y].strip().upper() == "SEND") for r in both)
    return len(both), same, same_send, both


for a, b, name in [("grader_a", "grader_b", "human - human"), ("grader_a", "judge", "grader A - judge"), ("grader_b", "judge", "grader B - judge")]:
    res = pair(a, b)
    if res is None:
        print(f"{name}: no rows graded on both columns yet")
        continue
    n, same, same_send, both = res
    print(f"{name}: {n} rows, same label {same}/{n} = {same / n:.0%}, same SEND / not-SEND reading {same_send}/{n} = {same_send / n:.0%}")
    for r in both:
        if r[a].strip().upper() != r[b].strip().upper():
            print(f"   {r['id']}: {a}={r[a]} {b}={r[b]}")
