"""tests/hooks/test_r4_derived_aggregate.py -- W1.4/R4. Faction Mandate is a DERIVED aggregate
(settlement_layer §1.8 / Jordan 2026-05-30); a direct write/delta to it is the F1 drift class.
Confirms R4 flags WRITES (Mandate -1, +=, ±Mandate, +1 Mandate) but not READS (Legitimacy =
Mandate x 20, += Mandate x 5)."""
import sys, io, contextlib
sys.path.insert(0, '/home/claude')
from github_ops import quick_bootstrap

def run(h, content):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try: h.pre_commit_gate([('designs/provincial/faction_layer_v30.md', content)], [])
        except Exception: pass
    return 'R4 advisory' in buf.getvalue()

def main():
    g, h, _, _ = quick_bootstrap(); h.task_gate('infrastructure')
    H = '<!-- version: vT -->\n# t\n'
    writes = {
        'pm_minus':   H + 'Campaign defeat: Mandate \u2212 1 (stat damage).',   # U+2212 minus
        'hyphen':     H + 'Turmoil failure: Mandate -1.',                       # ASCII hyphen
        'plusminus':  H + 'Domain Echo: \u00b1Mandate on resolution.',          # ±Mandate
        'delta_pre':  H + 'On success: +1 Mandate to the acting faction.',      # +1 Mandate
        'pluseq':     H + 'Mandate += recovery_step at Accounting.',            # +=
    }
    reads = {
        'formula': H + 'Legitimacy = Mandate \u00d7 20, starting = stat \u00d7 20.',  # = Mandate x 20
        'delta_read': H + 'Successful Govern action: Legitimacy += Mandate \u00d7 5.',# += Mandate x 5
        'prose': H + 'Mandate increases as settlements gain Legitimacy.',             # descriptive
    }
    wr = {k: run(h, v) for k, v in writes.items()}
    rd = {k: run(h, v) for k, v in reads.items()}
    print("WRITES (expect all True):", wr)
    print("READS  (expect all False):", rd)
    assert all(wr.values()), f"all writes must warn: {wr}"
    assert not any(rd.values()), f"no reads may warn: {rd}"
    print("PASS: R4 flags Mandate writes/deltas, ignores Mandate reads in formulas/prose")

if __name__ == '__main__': main()
