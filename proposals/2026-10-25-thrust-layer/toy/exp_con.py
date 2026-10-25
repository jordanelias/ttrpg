"""CONSTRAINED WORLD: NPC death very rare; violence against anyone with standing gated (accusation is the usual weapon);
a killing carries significant consequences; closures that do not kill bind a peace.  Predictions registered BEFORE the first run."""
import random, regimes10 as R
N = 300
CON1 = dict(death_p=0.01, gate_p=0.9, accuse=True, truce=True, conseq=True, lethal=False, tdr_kill=False)
CON2 = dict(death_p=0.01, gate_p=0.9, accuse=True, truce=True, conseq=True, lethal=True,  tdr_kill=True)
def mean(ms, k):
    xs = [m[k] for m in ms if m.get(k) is not None]; return sum(xs) / len(xs)
rng = random.Random(21)
def aminn(ms):
    d = [m['arc_all'] - m['arc_null'] for m in ms]
    bs = sorted(sum(rng.choice(d) for _ in d) / len(d) for _ in range(2000)); return sum(d) / len(d), bs[50], bs[1950]
def run(reg, con, **kw):
    out = []
    for s in range(N):
        ev, _ = R.simulate(s, reg, con=con, **kw); W = R.LAST
        M = R.run_metrics(ev, shuf_rng=random.Random(s + 999))
        hv = [e for e in ev if e['verb'] == 'harm' and e['delta'] > 0 and isinstance(e['actor'], int)]
        M['deaths'] = W.A - sum(W.alive)
        M['harm'] = len(hv); M['harm_stand'] = sum(1 for e in hv if e.get('tstand', 0) > 0)
        M['accuse'] = sum(1 for e in ev if e['verb'] == 'accuse' and e['delta'] > 0)
        M['gate'] = W.gate_refused
        death_ids = {e['id'] for e in ev if e.get('death')}
        M['revenge'] = sum(1 for e in R.executed(ev) if e['motive'] and e['motive'][0] == 'reaction' and e['motive'][1] in death_ids)
        M['outcry'] = sum(1 for e in ev if e['verb'] == 'outcry')
        M['late'] = sum(1 for e in R.executed(ev) if e['t'] >= 22)
        out.append(M)
    return out
def ladder_rate(reg, con):
    met = tot = 0
    from collections import defaultdict
    for s in range(N):
        ev, _ = R.simulate(s, reg, con=con); seq = defaultdict(list)
        for e in ev:
            if e['verb'] in ('goal_met', 'goal_failed', 'ambition_fired') and e['motive']: seq[e['motive'][1]].append(e['verb'])
        for v in seq.values():
            tot += 1; met += 1 if 'goal_met' in v else 0
    return met / tot
if __name__ == '__main__':
    ARMS = [('BU', 'BU', CON1), ('HYg3', 'HYg3', CON1), ('HYg3d', 'HYg3d', CON1), ('TDR (forced yield)', 'TDR', CON1),
            ('TDSc nonlethal', 'TDSc', CON1), ('HYg3c nonlethal', 'HYg3c', CON1),
            ('TDSc lethal+conseq', 'TDSc', CON2), ('HYg3c lethal+conseq', 'HYg3c', CON2), ('TDR lethal+conseq', 'TDR', CON2)]
    res = {n: run(r, c) for n, r, c in ARMS}
    print("arm                    deaths harm_on_standing gate_refused accuse revenge outcry | arc_all arc-null[CI]            closed five_node why_linked late_events")
    for n, r, c in ARMS:
        ms = res[n]; a = aminn(ms)
        hs = sum(m['harm_stand'] for m in ms) / max(1, sum(m['harm'] for m in ms))
        print(f"{n:22} {mean(ms,'deaths'):6.2f} {hs:15.3f} {mean(ms,'gate'):12.1f} {mean(ms,'accuse'):6.1f} {mean(ms,'revenge'):7.2f} {mean(ms,'outcry'):6.2f} | {mean(ms,'arc_all'):7.3f} {a[0]:+.3f} [{a[1]:+.3f},{a[2]:+.3f}] {mean(ms,'arc_closed'):6.3f} {mean(ms,'five_node'):9.3f} {mean(ms,'why_linked'):10.3f} {mean(ms,'late'):11.1f}")
    lr = ladder_rate('HYg3', CON1)
    print("\nladder: share of ambitions with >=1 goal met (HYg3, constrained):", round(lr, 3))
    P = [
     ("K1", "Constrained arms: deaths/run <= 0.6 in every CON1 arm and harm aimed at standing <= 0.10 of harm",
      lambda: all(mean(res[n], 'deaths') <= 0.6 for n in res if n in ('BU','HYg3','HYg3d','TDR (forced yield)','TDSc nonlethal','HYg3c nonlethal')) and
              all(sum(m['harm_stand'] for m in res[n]) / max(1, sum(m['harm'] for m in res[n])) <= 0.10 for n in ('BU','HYg3','HYg3d','TDR (forced yield)','TDSc nonlethal','HYg3c nonlethal'))),
     ("K2", "Bottom-up still has no ordering signal: |arc-null(BU)| < 0.05", lambda: abs(aminn(res['BU'])[0]) < 0.05),
     ("K3", "A bound peace restores the silence death supplied: arc-null >= +0.08 for TDSc nonlethal and HYg3c nonlethal",
      lambda: aminn(res['TDSc nonlethal'])[0] >= 0.08 and aminn(res['HYg3c nonlethal'])[0] >= 0.08),
     ("K4", "The forcing director with a forced yield keeps its signal: arc-null(TDR forced yield) >= +0.08", lambda: aminn(res['TDR (forced yield)'])[0] >= 0.08),
     ("K5", "Significant consequences are real: revenge events/run >= 3.0 in the lethal+conseq arms and <= 0.5 in the nonlethal arms",
      lambda: all(mean(res[n], 'revenge') >= 3.0 for n in ('TDSc lethal+conseq','HYg3c lethal+conseq','TDR lethal+conseq')) and all(mean(res[n], 'revenge') <= 0.5 for n in ('TDSc nonlethal','HYg3c nonlethal'))),
     ("K6", "A lethal climax with consequences does not lose the arc signal: arc-null(TDSc lethal+conseq) >= arc-null(TDSc nonlethal)",
      lambda: aminn(res['TDSc lethal+conseq'])[0] >= aminn(res['TDSc nonlethal'])[0]),
     ("K7", "The ladder survives the authority gate: >= 0.90 of ambitions meet a goal", lambda: lr >= 0.90),
    ]
    print("\n== PREDICTIONS (registered before the first run)")
    ok = 0
    for id, claim, fn in P:
        v = bool(fn()); ok += v; print(f"[{'CONFIRMED' if v else 'FALSIFIED'}] {id}: {claim}")
    print(f"{ok}/{len(P)} confirmed")
