from common import *
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "c3.py")).read().split('H(f"C3.1')[0].split("N = int")[1].split("\n",1)[1])
n = int(sys.argv[1]) if len(sys.argv) > 1 else 800
H(f'C3.6 every rig level best somewhere: P(the arranger carries) by rig, gap and his case; the best rig on 2 x stake x P - rig_price x tilt^2 (n={n})')
tab={}
for rung in (1, 2, 4):
    for ra in (1, 4, 7):
        pp = cast_with(a_rung=rung); pp["a"]["attributes"]["reason"] = ra
        ps={}; ts={}
        for r in (0, 0.5, 1):
            ps[r]=carried(pp, "trial", M, n, "g", bench=BENCH, floor=("crowd",), effort=3, arranger="a", rig=r)
            ts[r]=host.build(pp, "trial", M, bench=BENCH, floor=("crowd",), effort=3, arranger="a", rig=r)[1].tilt
        tab[(rung,ra)]=(ps,ts)
        print(f'  a rung {rung}, Reason {ra}: ' + ', '.join(f'rig {r}: P {ps[r]:.3f} tilt {ts[r]:.2f}' for r in ps))
for rp in (1.0, 0.5, host.FOLD['rig_price']):
    cnt=Counter()
    for (rung,ra),(ps,ts) in tab.items():
        for st in (0.25,0.5,1.0):
            b=max(ps,key=lambda r: 2*st*ps[r]-rp*ts[r]**2); cnt[b]+=1
    print(f"  rig_price {rp}: the best rig over 9 cases x stakes 0.25/0.5/1: {dict(sorted(cnt.items()))}")
