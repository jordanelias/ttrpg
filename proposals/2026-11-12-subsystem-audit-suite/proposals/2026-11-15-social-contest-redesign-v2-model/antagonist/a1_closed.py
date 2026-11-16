"""Antagonist: independent closed-form checks for F-A, F-B, F-D, F-F, F-G. Uses only the live sigma_leverage
(MU_PER_DIE, SD_PER_DIE, soft_cap via net_boost, LEVEL_SIGMA) and the plan's own pool_of/even_line/opposed_ob text."""
import sys, math, random
sys.path.insert(0, "/home/user/ttrpg")
from engine.dice_engine import sigma_leverage as SL
MU, SD = SL.MU_PER_DIE, SL.SD_PER_DIE
Phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
pool_of = lambda score, add, pa, pf: max(pf, score + add + pa)        # B04.24
even_line = lambda pa: MU * pa                                         # B04.24
opposed_ob = lambda score, rate: rate * max(0.0, score)                # B04.24
PA, PF, RATE, UNTR = 6, 5, MU, 2                                       # B05.23 shipped; pool_default 2
def p_margin_ge(pool, ob, sigma, k=1.0):
    p = max(1.0, pool); b = SL.net_boost(sigma, p)
    return 1 - Phi((ob + k - MU * p - b) / (SD * math.sqrt(p)))
def cap(p, ceiling=2.0):          # H-213 per-pool cap on the Normal (the model's G15 reading; shown both ways)
    return MU * p + math.sqrt(p) * (ceiling - MU)

print("== F-A one ballot, legal_trial, shipped (track_step .3, difficulty routine .5, stakes 0, d.score 2, Will mid)")
for label, pool in (("bench pool.judging = max(rank 0, untrained 2)+0", max(0, UNTR) + 0),
                    ("bench j1 rank 2 + addend 1", max(2, UNTR) + 1),
                    ("hearer pool_of(untrained,0,6,5)", pool_of(UNTR, 0, PA, PF))):
    hard = even_line(PA) + 0.5 + 0.0 + opposed_ob(2, RATE)
    for capped in (False, True):
        ob = min(hard, cap(pool)) if capped else hard
        row = [f"t={t:+d}:{p_margin_ge(pool, ob, 0.3 * t):.3f}" for t in (-3, -1, 0, 1, 3)]
        print(f"  {label:48s} pool={pool:4.1f} ob={ob:.2f} cap={'Y' if capped else 'N'}  P(S+): " + " ".join(row))

print("\n== F-B declared, quorum 2: P(>=2 of n seats S+), seats i.i.d. at the BEST track (+3), bench pool 2 vs 3")
for pool in (2, 3):
    hard = even_line(PA) + 0.5 + 0.0 + opposed_ob(2, RATE)
    p = p_margin_ge(pool, min(hard, cap(pool)), 0.9)
    for n in (1, 2, 3, 5):
        q = sum(math.comb(n, k) * p**k * (1 - p)**(n - k) for k in range(2, n + 1))
        print(f"  pool {pool} p_seat={p:.4f} n={n}: P(quorum met)={q:.2e}  expected in 2000 = {2000*q:.2f}")

print("\n== F-D abridged conversation, all-4 speaker and hearer, empty pursuits/convictions, no trait")
mv = [(4-1)/6, 0.0, 0.0, (4-1)/6]                      # B24p.06: evidence=Reason, consequence=0, authority=0, solidarity=Attunement
m = sum(mv)/4
fit = [(v-m)/(max(mv)-m) if v >= m else (v-m)/(m-min(mv)) for v in mv]
print("  moved_by =", [round(x, 3) for x in mv], " fit per ground =", [round(x, 3) for x in fit])
rnd = random.Random(0); N = 200000; best = 0
for _ in range(N):
    read = rnd.gauss(MU*10, SD*math.sqrt(10)) - (even_line(PA) + 1.4)
    blur = 1.0 * (1 - (1 + math.tanh(read)) / 2)
    bel = [min(1, max(0, v + blur * rnd.gauss(0, 1))) for v in mv]
    g = max(range(4), key=lambda i: (bel[i], -i))
    best += fit[g] > 0
q_best = best / N
print(f"  share of choices on a +1 ground (MC, n={N}): {q_best:.3f}")
p_off = Phi(((even_line(PA) + 0.5) - MU*10) / (SD*math.sqrt(10)))
print(f"  P(hold fails) at Focus 4 in room `none` (distraction .5): {p_off:.3f}")
shield = min(0.6, 0.1*(4-1))
for rank, proofs in ((0, 0.0), (1, 0.0), (1, 2.0)):
    pool = pool_of(4 + rank, 0, PA, PF)
    prf = SL.level("minor") * min(proofs, 0.5*4) * 2 * 0.5
    out = []
    for lvl, d in (("plain", 0), ("routine", .5), ("demanding", 1), ("hard", 1.5)):
        base_ob = even_line(PA) + d + opposed_ob(2, RATE)
        def carried(sig):
            return (1-p_off)*p_margin_ge(pool, base_ob, sig) + p_off*p_margin_ge(pool, base_ob + 1.5, sig)
        nofit = carried(prf)
        withfit = q_best*carried(prf + 0.75) + (1-q_best)*carried(prf - 0.5*(1-shield))
        out.append(f"{lvl}: {withfit:.3f} (nofit {nofit:.3f})")
    print(f"  rank {rank} proofs {proofs}: pool {pool}  " + "  ".join(out))

print("\n== F-F order walk (alternating, max 3; actor effort+1, addressed effort+1)")
for eff in (0, 1, 2):
    left = {"for": eff+1, "against": eff+1}; seq = []; turn = ["for", "against"]; i = 0
    while len(seq) < 3:
        able = [s for s in turn if left[s] > 0]
        if not able: break
        s = turn[i % 2]
        if left[s] <= 0: i += 1; continue
        seq.append(s); left[s] -= 1; i += 1
    print(f"  effort {eff}: {seq}")

print("\n== F-G strain_carried = max(0, marks - strain_rest*scenes_since)*press_base, one mark per sitting, one rest scene between")
marks = 0; ser = []
for k in range(1, 12):
    carried = max(0, marks - 1*1) if marks else 0      # scenes_since the last mark = 1 at each sitting after the first
    ser.append(carried); marks += 1
print("  plan formula, strain carried in at sittings 1..11:", ser)
marks_open = 0; ser2 = []
for k in range(1, 12):
    ser2.append(max(0, marks_open)); marks_open = max(0, marks_open + 1 - 1)  # v30: each rest scene clears one mark
print("  v30 reading (a mark clears per scene of rest):     ", ser2)
