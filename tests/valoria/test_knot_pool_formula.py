"""
Regression guard for the Knot Pool formula (ED-FI-0005 / OPT-AV-9, C3-F2).

The attribute/value coherence audit (ED-IN-0029) found FOUR non-agreeing live Knot
Pool formulas. Jordan RATIFIED one: `(Spirit × 2) + History(Relevant) + 3`, with
Bonds demoted to an eligibility-gate (the `floor(Bonds/2)+1` COUNT cap), NOT an
additive pool term. There is no sim/ oracle that computes the Knot Pool, so this is
a doc-content guard: it pins the ratified formula on every carrying surface and
fails if any surface regresses to the superseded `(Bonds × 2) + 3` pool term.
"""
import os
import re

REPO = os.path.join(os.path.dirname(__file__), "..", "..")

# The surfaces that carry the Knot Pool *formation-pool* formula (not the count cap).
SURFACES = (
    "designs/scene/derived_stats_v30.md",
    "designs/personal/knots_v30.md",
    "designs/scene/fieldwork_editorial.md",
)


def _norm(text):
    # collapse whitespace and unify the multiplication glyph so `(Spirit × 2)` and
    # `(Spirit×2)` match the same canonical shape
    return re.sub(r"\s+", "", text).replace("×", "*").replace("×", "*")


def _knot_pool_lines(body):
    return [ln for ln in body.splitlines() if re.search(r"knot pool|knot pool\b", ln, re.I)
            or re.search(r"^\s*-\s*Knot pool", ln, re.I)]


def test_ratified_formula_present_on_every_surface():
    ratified = _norm("(Spirit*2)+History(Relevant)+3")
    for rel in SURFACES:
        body = open(os.path.join(REPO, rel), encoding="utf-8").read()
        assert ratified in _norm(body), f"{rel}: ratified Knot Pool formula missing (ED-FI-0005)"


def test_no_surface_carries_the_superseded_bonds_pool_term():
    # the exact superseded POOL term; the `floor(Bonds/2)+1` COUNT cap is legitimate
    # and must NOT trip this guard, so we match the additive `(Bonds*2)+3` shape only
    superseded = _norm("(Bonds*2)+3")
    for rel in SURFACES:
        body = open(os.path.join(REPO, rel), encoding="utf-8").read()
        assert superseded not in _norm(body), (
            f"{rel}: superseded Knot Pool pool term (Bonds×2)+3 regressed (ED-FI-0005)")


def test_bonds_count_cap_preserved():
    # Bonds stays the eligibility-gate: the count cap floor(Bonds/2)+1 must survive
    cap = _norm("floor(Bonds/2)+1")
    for rel in ("designs/personal/knots_v30.md", "designs/scene/fieldwork_editorial.md"):
        body = open(os.path.join(REPO, rel), encoding="utf-8").read()
        assert cap in _norm(body), f"{rel}: Bonds count cap floor(Bonds/2)+1 lost"
