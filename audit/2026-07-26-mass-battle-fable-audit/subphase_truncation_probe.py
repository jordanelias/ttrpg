"""A3 measurement probe — does the MAX_SUB_PHASES bound ever bite, and with what weight?

ED-MB-0048 (plan v2 §3 A3). Read-only observation: wraps
`orchestration.resolve_engagements_cascading`, reads the counters that function now returns
(`truncated_groups` / `truncated_pairs` / `truncated_troops` / `n_groups`) and accumulates them.
It changes no engine state, draws no RNG, and does not alter what the wrapped function returns —
so a battery run under this probe is byte-identical to one run without it.

WHY A PROBE AND NOT A TEST. The audit's truncation row is the one that was never re-derived by
anyone but the agent that produced it (plan §0's provenance table marks it **UNVERIFIED — treat as
a lead**, G12). This is the re-derivation. It also supplies the CONTROL the original number lacked
(§0.1 #4): "0 truncations" alone cannot distinguish "the bound is generous" from "this workload
never cascades at all" — so the headroom (max observed group count vs the bound) is reported
alongside, and a run where the max group count is 1 is reported as NOT INFORMATIVE about the bound.

⚠ The pinned grid battery reads 0 and will mislead if quoted alone (plan A3's own warning), so the
default sweep covers all four bat.py modes AND the gauge's multi-unit / envelopment / Cannae rows,
which are where cascades actually occur.

  python3 audit/2026-07-26-mass-battle-fable-audit/subphase_truncation_probe.py [--quick]
"""
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, '..', '..'))
_SIM = os.path.join(_REPO, 'tests', 'sim')
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)


class Tally:
    def __init__(self):
        self.calls = 0
        self.trunc_calls = 0
        self.groups_dropped = 0
        self.pairs_dropped = 0
        self.troops_dropped = 0.0
        self.group_hist = Counter()

    def observe(self, res):
        self.calls += 1
        n = res.get('n_groups', 0)
        self.group_hist[n] += 1
        if res.get('truncated_groups', 0):
            self.trunc_calls += 1
        self.groups_dropped += res.get('truncated_groups', 0)
        self.pairs_dropped += res.get('truncated_pairs', 0)
        self.troops_dropped += res.get('truncated_troops', 0.0)

    def report(self, label, bound):
        maxg = max(self.group_hist) if self.group_hist else 0
        print(f"\n--- {label}")
        print(f"    resolver calls            : {self.calls:,}")
        print(f"    calls that truncated      : {self.trunc_calls:,}")
        print(f"    groups dropped            : {self.groups_dropped:,}")
        print(f"    pairs dropped             : {self.pairs_dropped:,}")
        print(f"    engaged-troop weight lost : {self.troops_dropped:,.3f}")
        print(f"    max depth-groups in a call: {maxg}   (bound MAX_SUB_PHASES={bound})")
        print(f"    group-count histogram     : {dict(sorted(self.group_hist.items()))}")
        if maxg <= 1:
            print("    [NOT INFORMATIVE] no call in this workload produced more than one depth "
                  "group — a zero here says nothing about the bound.")
        elif self.trunc_calls == 0:
            print(f"    [CLEAN, WITH HEADROOM] headroom = {bound - maxg} group(s) at the observed "
                  f"maximum.")
        else:
            print("    [TRUNCATION OBSERVED] the bound bit — see the weight above.")


def _install(tally):
    import mass_battle.orchestration as O
    real = O.resolve_engagements_cascading

    def wrapped(*a, **kw):
        res = real(*a, **kw)
        tally.observe(res)
        return res

    O.resolve_engagements_cascading = wrapped
    return real


def run_bat_battery(tally):
    import mass_battle.bat as bat
    import mass_battle.orchestration as O
    # bat.py resolves battles through engine.resolve_battle -> orchestration.run_multi_turn_battle,
    # which calls the module-global name we just rebound, so the wrapper is on the live path.
    assert O.resolve_engagements_cascading.__name__ == 'wrapped'
    mode, digest = bat.compute()
    return mode, digest


def run_gauge(tally, n):
    import gauge_mb as g
    import mass_battle.config as c
    tests = g.TESTS + (g.CAV_TESTS if c.PER_CELL else [])
    npass = g.run('multi', tests, n=n)
    return npass, len(tests)


def main():
    quick = '--quick' in sys.argv
    import mass_battle.config as c
    bound = c.MAX_SUB_PHASES
    mode_desc = (f"PER_CELL={os.environ.get('PER_CELL','?')} "
                 f"FIELD_MOVEMENT={os.environ.get('FIELD_MOVEMENT','?')} "
                 f"PC_NODE_COHESION={os.environ.get('PC_NODE_COHESION','?')} "
                 f"CASCADING_ENABLED={c.CASCADING_ENABLED}")
    print(f"=== A3 sub-phase truncation probe — {mode_desc} ===", flush=True)

    bat_t = Tally()
    _install(bat_t)
    mode, digest = run_bat_battery(bat_t)
    print(f"    bat.py battery digest: {mode} {digest[:16]}…", flush=True)
    bat_t.report(f"bat.py battery [{mode}] (10 matchups incl. envelop/cannae/oblique)", bound)

    gauge_t = Tally()
    _install(gauge_t)   # rebind onto the already-wrapped name; both tallies stay separate
    npass, ntot = run_gauge(gauge_t, n=4 if quick else 14)
    gauge_t.report(f"honest gauge multi (n={4 if quick else 14}) — {npass}/{ntot} rows in band", bound)


if __name__ == '__main__':
    main()
