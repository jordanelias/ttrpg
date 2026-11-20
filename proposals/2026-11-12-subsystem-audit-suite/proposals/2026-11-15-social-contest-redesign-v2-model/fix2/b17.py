"""B17: skill expression from the view alone: random / take-the-top-worth / a reader who also weighs risk by the odds."""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
cast = F.cast(); T = F.TOLLS
def risky(lam):
    def f(v, me):
        behind = 0.5 - v.odds                  # >0 behind: he wants spread; <0 ahead: he wants none
        def val(o):
            spread = 0.0 if o.p is None else 2.0 * math.sqrt(max(0.0, o.p * (1 - o.p)))
            return o.ev + lam * behind * spread * (2.0 / max(1, v.turns_left))
        o = max(v.options, key=val); return Choice(o.move, o.ground, o.item, o.relation)
    return f
def rnd(v, me):
    o = random.Random(f"{v.n}|{v.mover}|{v.acc:.6f}").choice(v.options); return Choice(o.move, o.ground, o.item, o.relation)
SC = [("rally (cast, orator)", cast, "rally", dict(T, parties={"for": "orator"}), dict(floor=("guildsmen", "toll_men", "townsfolk"), effort=3), "orator"),
      ("audience (cast, scholar before the judge)", cast, "audience", dict(T, parties={"for": "scholar", "against": "bully"}), dict(bench=CB, effort=3), "scholar"),
      ("trial (cast, scholar accuses the bully)", cast, "trial", dict(T, parties={"for": "scholar", "against": "bully"}), dict(bench=CB, floor=FL, effort=3), "scholar"),
      ("debate (cast, orator moves)", cast, "debate", dict(T, id="remit", parties={"for": "orator", "against": "diplomat"}), dict(bench=CB, floor=("guildsmen",), effort=3), "orator"),
      ("trial (all-mid, a accuses)", mp, "trial", M, dict(bench=BENCH, effort=3), "a")]
H(f"B17 the played side's chooser, all else automatic: `for` carried (n={N})")
for lab, pp, rite, m, kw, who in SC:
    r = {k: carried(pp, rite, m, N, "b17", deciders={who: pol}, **kw) for k, pol in
         (("random", rnd), ("top worth", smart), ("risk-reader 1", risky(1.0)), ("risk-reader 3", risky(3.0)))}
    print(f"  {lab:44s} " + "  ".join(f"{k} {v:.3f}" for k, v in r.items()) + f"  | reader 3 - top {r['risk-reader 3'] - r['top worth']:+.3f} (z {z(r['risk-reader 3'], r['top worth'], N):+.1f})")
