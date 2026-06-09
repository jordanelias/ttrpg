#!/usr/bin/env python3
"""tests/hooks/test_r7_value_formula.py — confirms W1.5/R7: a non-derived_stats design doc
that DEFINES a derived-value formula (the F4-F7 drift class) triggers a non-blocking advisory;
the authoritative derived_stats doc and formula-free docs do not."""
import sys, io, contextlib
sys.path.insert(0, '/home/claude')
from github_ops import quick_bootstrap
def run(h, adds):
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):
        try: h.pre_commit_gate(adds, [])
        except Exception: pass
    return buf.getvalue()
def main():
    g, h, _, _ = quick_bootstrap(); h.task_gate('infrastructure')
    F='<!-- version: vT -->\n# t\nComposure = Charisma + 6\n'      # drift formula
    NF='<!-- version: vT -->\n# t\nComposure draws on Charisma; see derived_stats.\n'  # no formula
    a = run(h, [('designs/scene/social_contest_v30.md', F)])    # non-authority + formula -> advisory
    b = run(h, [('designs/scene/derived_stats_v30.md', F)])     # authority doc -> no advisory
    c = run(h, [('designs/scene/social_contest_v30.md', NF)])   # no formula -> no advisory
    assert 'R7 advisory' in a and 'Composure' in a, f"A should warn: {a!r}"
    assert 'R7 advisory' not in b, f"B (authority) must not warn: {b!r}"
    assert 'R7 advisory' not in c, f"C (no formula) must not warn: {c!r}"
    print("PASS: R7 flags non-authority derived-value formulas, exempts derived_stats + formula-free docs")
if __name__=='__main__': main()
