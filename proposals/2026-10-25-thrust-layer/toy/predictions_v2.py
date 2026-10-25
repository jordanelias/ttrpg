"""v2 predictions, registered AFTER seeing v1 results and the instrument defects they exposed, and BEFORE v2 was run.
They are therefore informed, not blind; v1's blind predictions and their outcomes are kept in out_v1.txt.
A[cond][regime][metric] = mean over seeds (NaN/None ignored)."""
import math

def g(A, c, r, m): return A[c][r][m]
def f(x): return "nan" if (x is None or (isinstance(x, float) and math.isnan(x))) else f"{x:.3f}"
P = []
def pred(id, claim):
    def deco(fn): P.append((id, claim, fn)); return fn
    return deco

@pred("L1", "Apparent legibility does not discriminate: spread across regimes < 0.05")
def _(A):
    v = [g(A,'base',r,'leg_apparent') for r in ('BU','TD','TDR','HY')]; return (max(v)-min(v) < 0.05, ", ".join(f(x) for x in v))

@pred("L2", "Grounding of the DIRECTOR'S OWN beats: blind script TD < 0.65; replanning TDR > 0.90")
def _(A):
    td, tdr = g(A,'base','TD','grounded_forced'), g(A,'base','TDR','grounded_forced'); return (td < 0.65 and tdr > 0.90, f"TD {f(td)} TDR {f(tdr)}")

@pred("L3", "Standing motives deepen the 'why': why_linked(HY) >= why_linked(BU) + 0.20")
def _(A):
    h, b = g(A,'base','HY','why_linked'), g(A,'base','BU','why_linked'); return (h >= b+0.20, f"HY {f(h)} BU {f(b)}")

@pred("C1", "Consistency, unperturbed: violation rate BU = HY = TDR = 0, TD >= 0.15")
def _(A):
    v = {r: g(A,'base',r,'viol_any') for r in ('BU','HY','TDR','TD')}
    return (v['BU']==0 and v['HY']==0 and v['TDR']==0 and v['TD']>=0.15, str({k:f(x) for k,x in v.items()}))

@pred("C2", "Injection: runs with a forced outcome: BU = HY = 0, TD = TDR = 1")
def _(A):
    v = {r: g(A,'base',r,'injected_any') for r in ('BU','HY','TDR','TD')}
    return (v['BU']==0 and v['HY']==0 and v['TD']==1 and v['TDR']==1, str({k:f(x) for k,x in v.items()}))

@pred("C3", "Perturbation: post-kill violation rate TD >= 0.50; BU, HY <= 0.02; TDR <= 0.05")
def _(A):
    v = {r: g(A,'pert',r,'viol_post_any') for r in ('BU','HY','TDR','TD')}
    return (v['TD']>=0.5 and v['BU']<=0.02 and v['HY']<=0.02 and v['TDR']<=0.05, str({k:f(x) for k,x in v.items()}))

@pred("A1", "Director-thread arc fidelity (best case for top-down): arc_dir TDR >= 0.60 and TD < TDR")
def _(A):
    td, tdr = g(A,'base','TD','arc_dir'), g(A,'base','TDR','arc_dir'); return (tdr >= 0.60 and td < tdr, f"TD {f(td)} TDR {f(tdr)}")

@pred("A2", "A five-beat script dominates the chronicle: share of runs where the director's thread is the observer's main thread: TD >= 0.60")
def _(A):
    x = g(A,'base','TD','dir_is_main'); return (x >= 0.60, f(x))

@pred("A3", "Observer-picked arc rate: TD >= BU + 0.10")
def _(A):
    td, bu = g(A,'base','TD','arc_all'), g(A,'base','BU','arc_all'); return (td >= bu+0.10, f"TD {f(td)} BU {f(bu)}")

@pred("A4", "Apophenia: BU arc rate exceeds its shuffled null by <= 0.10")
def _(A):
    a, n = g(A,'base','BU','arc_all'), g(A,'base','BU','arc_null'); return (a-n <= 0.10, f"BU {f(a)} null {f(n)}")

@pred("A5", "Hybrid signal over null: (HY-null) >= (BU-null) + 0.05")
def _(A):
    h = g(A,'base','HY','arc_all')-g(A,'base','HY','arc_null'); b = g(A,'base','BU','arc_all')-g(A,'base','BU','arc_null')
    return (h >= b+0.05, f"HY-null {f(h)} BU-null {f(b)}")

@pred("A6", "Sensitivity: sign of (TD-BU) and of (HY-BU) in arc rate is the same in >= 3 of the 4 arc-criterion variants")
def _(A):
    vs = [k for k in A['base']['BU'] if k.startswith('arc_p')]
    s_td = sum(1 for k in vs if A['base']['TD'][k]-A['base']['BU'][k] > 0)
    s_hy = sum(1 for k in vs if A['base']['HY'][k]-A['base']['BU'][k] > 0)
    ok = (s_td >= 3 or s_td <= 1) and (s_hy >= 3 or s_hy <= 1)
    return (ok, f"TD>BU in {s_td}/4 variants; HY>BU in {s_hy}/4")

@pred("D2", "Timing: std of main-thread peak season TD <= BU - 1.0")
def _(A):
    td, bu = g(A,'base','TD','tp_std'), g(A,'base','BU','tp_std'); return (bu-td >= 1.0, f"TD {f(td)} BU {f(bu)}")

@pred("B1", "Five-node completeness: TD > BU and TDR > BU and HY >= BU")
def _(A):
    td, tdr, bu, hy = (g(A,'base',r,'five_node') for r in ('TD','TDR','BU','HY')); return (td>bu and tdr>bu and hy>=bu, f"TD {f(td)} TDR {f(tdr)} BU {f(bu)} HY {f(hy)}")

@pred("B2", "Metronome: median gap CV of main-thread beats TD < BU")
def _(A):
    td, bu = g(A,'base','TD','gap_cv_med'), g(A,'base','BU','gap_cv_med'); return (td < bu, f"TD {f(td)} BU {f(bu)}")

@pred("K1", "Control: HY(w=0, occasions off, lifecycle off) reproduces BU's log on every seed")
def _(A): return (A['ctl']['equal']==A['ctl']['n'], f"{A['ctl']['equal']}/{A['ctl']['n']}")

@pred("K2", "Dose: why_linked rises with w (Spearman >= 0.9) and arc_all never drops > 0.05 between adjacent w")
def _(A):
    from regimes2 import spearman
    ws = sorted(A['dose']); xs = [A['dose'][w]['why_linked'] for w in ws]; ar = [A['dose'][w]['arc_all'] for w in ws]
    return (spearman(list(range(len(xs))), xs) >= 0.9 and all(ar[i+1]-ar[i] >= -0.05 for i in range(len(ar)-1)),
            "why " + ",".join(f(x) for x in xs) + " | arc " + ",".join(f(x) for x in ar))

@pred("K3", "Ablation: removing occasions lowers HY thread_cont by >= 0.02; removing lifecycle lowers HY arc_closed by >= 0.03")
def _(A):
    a = g(A,'base','HY','thread_cont')-A['abl']['noocc']['thread_cont']; b = g(A,'base','HY','arc_closed')-A['abl']['nolife']['arc_closed']
    return (a >= 0.02 and b >= 0.03, f"occasion {f(a)}; lifecycle {f(b)}")

@pred("R1", "Robustness: HY-BU on why_linked and on (arc_all - null) keep their sign in noent, engine, small")
def _(A):
    out=[]; ok=True
    for c in ('noent','engine','small'):
        d1 = g(A,c,'HY','why_linked')-g(A,c,'BU','why_linked')
        d2 = (g(A,c,'HY','arc_all')-g(A,c,'HY','arc_null'))-(g(A,c,'BU','arc_all')-g(A,c,'BU','arc_null'))
        out.append(f"{c}: why {f(d1)} arc {f(d2)}"); ok = ok and d1>0 and d2>0
    return (ok, "; ".join(out))

@pred("N1", "Quiet world: TD inflates stakes: main-thread peak magnitude in 'null' >= 2x BU's")
def _(A):
    td, bu = g(A,'null','TD','peak_mag'), g(A,'null','BU','peak_mag'); return (td >= 2*bu, f"TD {f(td)} BU {f(bu)}")

@pred("E1", "Refusal-heavy substrate (80%): the TD-BU gap in arc rate widens relative to base (forced beats bypass refusal)")
def _(A):
    ge = g(A,'engine','TD','arc_all')-g(A,'engine','BU','arc_all'); gb = g(A,'base','TD','arc_all')-g(A,'base','BU','arc_all')
    return (ge > gb, f"gap base {f(gb)} -> engine {f(ge)}")
