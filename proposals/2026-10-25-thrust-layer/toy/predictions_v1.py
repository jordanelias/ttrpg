"""PRE-REGISTERED predictions, written BEFORE any aggregate was computed (sha256 saved to predictions.sha first).

A[cond][regime][metric] = mean over seeds.  Conditions:
  base   entrench=1 refuse=0   |  noent  entrench=0   |  engine refuse=0.8 (the real engine refuses ~70-80% of acts)
  small  A=12 P=10 PR=4        |  null   A=8 P=8 PR=3 |  pert   player kills thread leader / protagonist at t=10
A['dose'][w], A['abl'][name], A['ctl'] as named below.
Each entry: (id, claim, check(A) -> (bool, evidence-string)).  A FAILED prediction is reported as failed.
"""


def g(A, cond, reg, m):
    return A[cond][reg][m]


def f(x):
    return f"{x:.3f}"


P = []


def pred(id, claim):
    def deco(fn):
        P.append((id, claim, fn)); return fn
    return deco


@pred("L1", "Apparent legibility (fields present) does not discriminate: spread across the four regimes < 0.05")
def _(A):
    v = [g(A, 'base', r, 'leg_apparent') for r in ('BU', 'TD', 'TDR', 'HY')]
    return (max(v) - min(v) < 0.05, "values " + ", ".join(f(x) for x in v))


@pred("L2", "Grounded legibility: BU ~ HY (both state-derived, within 0.05); the blind script TD is >= 0.30 below BU")
def _(A):
    bu, hy, td = (g(A, 'base', r, 'leg_grounded') for r in ('BU', 'HY', 'TD'))
    return (abs(bu - hy) < 0.05 and bu - td >= 0.30, f"BU {f(bu)} HY {f(hy)} TD {f(td)}")


@pred("L3", "Standing motives deepen the 'why': why_linked(HY) >= why_linked(BU) + 0.20")
def _(A):
    hy, bu = g(A, 'base', 'HY', 'why_linked'), g(A, 'base', 'BU', 'why_linked')
    return (hy >= bu + 0.20, f"HY {f(hy)} BU {f(bu)}")


@pred("C1", "Consistency, unperturbed: violation rate BU = HY = TDR = 0 and TD >= 0.15")
def _(A):
    v = {r: g(A, 'base', r, 'viol_any') for r in ('BU', 'HY', 'TDR', 'TD')}
    return (v['BU'] == 0 and v['HY'] == 0 and v['TDR'] == 0 and v['TD'] >= 0.15, str({k: f(x) for k, x in v.items()}))


@pred("C2", "Injection: runs containing a forced outcome: BU = HY = 0; TD = TDR = 1")
def _(A):
    v = {r: g(A, 'base', r, 'injected_any') for r in ('BU', 'HY', 'TDR', 'TD')}
    return (v['BU'] == 0 and v['HY'] == 0 and v['TD'] == 1 and v['TDR'] == 1, str({k: f(x) for k, x in v.items()}))


@pred("C3", "Perturbation (kill leader/protagonist at t=10): post-kill violation rate TD >= 0.50; BU, HY <= 0.02; TDR <= 0.05")
def _(A):
    v = {r: g(A, 'pert', r, 'viol_post_any') for r in ('BU', 'HY', 'TDR', 'TD')}
    return (v['TD'] >= 0.5 and v['BU'] <= 0.02 and v['HY'] <= 0.02 and v['TDR'] <= 0.05, str({k: f(x) for k, x in v.items()}))


@pred("C4", "Perturbation: among TD runs whose post-kill window still shows a 3-act arc, >= 40% contain violations (arc survives, incoherently)")
def _(A):
    x = g(A, 'pert', 'TD', 'arc_post_viol_share')
    return (x >= 0.40, "share " + f(x))


@pred("A1", "Arc: TD arc rate exceeds BU by >= 0.20 (a schedule produces the shape)")
def _(A):
    td, bu = g(A, 'base', 'TD', 'arc_all'), g(A, 'base', 'BU', 'arc_all')
    return (td - bu >= 0.20, f"TD {f(td)} BU {f(bu)}")


@pred("A2", "Apophenia: BU arc rate exceeds its shuffled-null rate by <= 0.10 (most apparent arcs are chance)")
def _(A):
    a, n = g(A, 'base', 'BU', 'arc_all'), g(A, 'base', 'BU', 'arc_null')
    return (a - n <= 0.10, f"BU {f(a)} null {f(n)}")


@pred("A3", "Hybrid carries real arc signal: (HY - null) >= (BU - null) + 0.10")
def _(A):
    h = g(A, 'base', 'HY', 'arc_all') - g(A, 'base', 'HY', 'arc_null')
    b = g(A, 'base', 'BU', 'arc_all') - g(A, 'base', 'BU', 'arc_null')
    return (h >= b + 0.10, f"HY-null {f(h)} BU-null {f(b)}")


@pred("D1", "Oatmeal: structural/slot signature ratio R_oat: TD <= 0.10 and BU >= TD + 0.10")
def _(A):
    td, bu = g(A, 'base', 'TD', 'R_oat'), g(A, 'base', 'BU', 'R_oat')
    return (td <= 0.10 and bu >= td + 0.10, f"TD {f(td)} BU {f(bu)}")


@pred("D2", "Climax timing std (seasons): TD at least 1 season below BU (templated timing)")
def _(A):
    td, bu = g(A, 'base', 'TD', 'tp_std'), g(A, 'base', 'BU', 'tp_std')
    return (bu - td >= 1.0, f"TD {f(td)} BU {f(bu)}")


@pred("B1", "Five-node completeness (setup, turn, climax, resolution) : TD > BU and HY > BU")
def _(A):
    td, bu, hy = (g(A, 'base', r, 'five_node') for r in ('TD', 'BU', 'HY'))
    return (td > bu and hy > bu, f"TD {f(td)} BU {f(bu)} HY {f(hy)}")


@pred("B2", "Metronome: median gap CV of main-thread beats lower in TD than in BU")
def _(A):
    td, bu = g(A, 'base', 'TD', 'gap_cv_med'), g(A, 'base', 'BU', 'gap_cv_med')
    return (td < bu, f"TD {f(td)} BU {f(bu)}")


@pred("B3", "Dead-end share of executed events is lower in HY than in BU (ambitions give consequences)")
def _(A):
    hy, bu = g(A, 'base', 'HY', 'dead'), g(A, 'base', 'BU', 'dead')
    return (hy < bu, f"HY {f(hy)} BU {f(bu)}")


@pred("K1", "Control: HY(w=0, occasions off, lifecycle off) reproduces BU's log exactly on every seed")
def _(A):
    return (A['ctl']['equal'] == A['ctl']['n'], f"{A['ctl']['equal']}/{A['ctl']['n']} identical")


@pred("K2", "Dose: why_linked rises with ambition weight w (Spearman >= 0.9 over the five means) and arc_all never drops > 0.05 between adjacent w")
def _(A):
    ws = sorted(A['dose']); xs = [A['dose'][w]['why_linked'] for w in ws]; ar = [A['dose'][w]['arc_all'] for w in ws]
    from regimes import spearman
    ok = spearman(list(range(len(xs))), xs) >= 0.9 and all(ar[i + 1] - ar[i] >= -0.05 for i in range(len(ar) - 1))
    return (ok, "why_linked " + ",".join(f(x) for x in xs) + " | arc_all " + ",".join(f(x) for x in ar))


@pred("K3", "Ablation: removing occasions lowers HY thread continuity by >= 0.02; removing lifecycle lowers HY arc closure by >= 0.03")
def _(A):
    a = g(A, 'base', 'HY', 'thread_cont') - A['abl']['noocc']['thread_cont']
    b = g(A, 'base', 'HY', 'arc_closed') - A['abl']['nolife']['arc_closed']
    return (a >= 0.02 and b >= 0.03, f"occasion effect on thread_cont {f(a)}; lifecycle effect on arc_closed {f(b)}")


@pred("R1", "Robustness: HY - BU on why_linked and on (arc_all - arc_null) keep their sign in noent, engine, small")
def _(A):
    out = []; ok = True
    for c in ('noent', 'engine', 'small'):
        d1 = g(A, c, 'HY', 'why_linked') - g(A, c, 'BU', 'why_linked')
        d2 = (g(A, c, 'HY', 'arc_all') - g(A, c, 'HY', 'arc_null')) - (g(A, c, 'BU', 'arc_all') - g(A, c, 'BU', 'arc_null'))
        out.append(f"{c}: why {f(d1)} arc {f(d2)}")
        ok = ok and d1 > 0 and d2 > 0
    return (ok, "; ".join(out))


@pred("N1", "Quiet world: TD inflates stakes: peak magnitude of the main thread in 'null' is >= 2x BU's")
def _(A):
    td, bu = g(A, 'null', 'TD', 'peak_mag'), g(A, 'null', 'BU', 'peak_mag')
    return (td >= 2 * bu, f"TD {f(td)} BU {f(bu)}")


@pred("E1", "Engine-like refusal (80%): bottom-up grounded legibility and arc rate collapse, and the TD advantage on arc rate widens vs base")
def _(A):
    bu_a = g(A, 'engine', 'BU', 'arc_all'); bu_b = g(A, 'base', 'BU', 'arc_all')
    td_e = g(A, 'engine', 'TD', 'arc_all') - bu_a; td_b = g(A, 'base', 'TD', 'arc_all') - bu_b
    return (bu_a < bu_b and td_e > td_b, f"BU arc base {f(bu_b)} -> engine {f(bu_a)}; TD-BU gap base {f(td_b)} -> engine {f(td_e)}")
