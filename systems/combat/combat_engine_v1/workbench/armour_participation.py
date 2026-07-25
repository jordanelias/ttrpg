"""Armour-interaction instrument (ED-PC-0040) — the measurements that five batches of remediation kept asserting
without running.

WHY THIS FILE EXISTS. Batches 4, 5 and 5.1 of the four-dimension audit each returned HALF-STANDS from adversarial
review, and the meta-review of that arc found a single common cause: quantitative claims were written into ledger
entries and code comments faster than they were measured, and the scripts that would have falsified them were
ad-hoc and thrown away. Three concrete misses, all of which this file answers in one run:

  · ED-PC-0038's ledger recorded "spear/yari/estoc -> 0" damage at plate. The ESTOC is the single most decisive
    plate weapon in the roster (`strike_profile`, below, reports 0.93 nonzero rate at mean 12.84).
  · ED-PC-0039 "restored" a plate-participation guard that watched one weapon out of a capable class of fourteen
    (`participation`, below, prints the whole class and the derivation of its membership).
  · ED-PC-0038 called mail "a tier the fix was never meant to touch"; it moved the odachi 41 points
    (`tier_table`, below, run at two commits and diffed).

The rule this file is meant to enforce, from the ED-PC-0040 meta-review: NO QUANTITATIVE CLAIM IN A LEDGER ENTRY
OR A CODE COMMENT WITHOUT A RE-RUNNABLE SOURCE. A claim about armour interaction should be a query against this
instrument, not a recollection.

It is DEV TOOLING, not a gate — `tests/valoria/test_combat_invariants.py`'s
`test_plate_participation_tracks_armour_defeat_capability` is the CI-enforced form of the `participation` view, and
it derives its bands from this script's output rather than from hand-set numbers.

CLI:
    python workbench/armour_participation.py participation [n]   # capability partition vs measured decided-rate
    python workbench/armour_participation.py strikes [n]         # per-strike damage BY SELECTED HEAD (finds F24)
    python workbench/armour_participation.py tiers [n] [w,...]   # share/decided across all four armour tiers
    python workbench/armour_participation.py all [n]

To compare against another commit, run it in a worktree and diff:
    git worktree add /tmp/wt <sha> && (cd /tmp/wt && python systems/combat/combat_engine_v1/workbench/armour_participation.py tiers)
"""
import sys, os
import random
import zlib
import collections

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import core
import wrapper
import combat_systems as S
import weapons as W
from combatant import Combatant, WEAPONS
from config import CFG

REFERENCE = 'arming'   # the uniform opponent every cell is measured against, as in workbench/balance.py


def _seed(key):
    """crc32, not hash() — hash() is PYTHONHASHSEED-salted and would make a reference table irreproducible
    run-to-run. Same rationale (and same function) as workbench/balance.py's _seed."""
    return zlib.crc32(repr(key).encode()) % 9999


# ── capability ────────────────────────────────────────────────────────────────────────────────────
def capability(name, cfg=CFG):
    """The weapon's BEST armour-defeat capability over every mode AND every grip it can actually reach in a fight.

    The grip clause is the part that has to be here rather than inline at a call site: `wrapper` swaps a weapon
    into its `HALFSWORD_FORM` when closed against medium/heavy armour, so the capability that governs a real fight
    is the half-sworded one. Measured on the base form alone the estoc reads 0.522 and the longsword 0.613 —
    both apparently sub-threshold — while in a fight they half-sword to 1.104 and 1.020 and are the two most
    decisive plate weapons on the board. Every partition in this file, and the CI guard derived from it, would be
    wrong without it."""
    forms = [name] + ([W.HALFSWORD_FORM[name]] if name in W.HALFSWORD_FORM else [])
    return max(S.adef_cap(WEAPONS[f], cfg, m) for f in forms for m in ('blunt', 'point', 'edge'))


def _duel(w, armor, n, cfg=CFG):
    """Position-swapped duel vs the reference weapon. Returns (decided_rate, share_of_decided|None)."""
    rng = random.Random(_seed((w, armor)))
    wins = dec = 0
    for i in range(n):
        swap = i >= n // 2
        A = Combatant('A', weapon=(w if not swap else REFERENCE), armor=armor)
        B = Combatant('B', weapon=(REFERENCE if not swap else w), armor=armor)
        r = wrapper.fight(A, B, cfg, rng)
        if swap:
            r = -r
        if r:
            dec += 1
        if r == 1:
            wins += 1
    return dec / n, (wins / dec if dec else None)


# ── view 1: the capability partition vs measured participation ────────────────────────────────────
def participation(n=200, armor='heavy', cfg=CFG):
    """Does the ability to SETTLE a fight inside armour track the capability to DEFEAT that armour?

    This is the view the ED-PC-0039 review used to prove the one-weapon guard was blind: it kills members of the
    capable class and reads the column. Membership is derived, never listed, so a new weapon lands on the correct
    side automatically."""
    thr = cfg['ADEF_THRESHOLD'][armor]
    rows = []
    for w in sorted(WEAPONS):
        dec, sh = _duel(w, armor, n, cfg)
        rows.append((w, capability(w, cfg), dec, sh))
    rows.sort(key=lambda r: -r[1])
    print(f"# participation vs {REFERENCE} at {armor} (n={n}); ADEF_THRESHOLD[{armor}] = {thr}")
    print(f"{'weapon':22s} {'capability':>10s} {'band':>9s} {'decided':>8s} {'share':>7s}")
    for w, cap, dec, sh in rows:
        band = 'clears' if cap >= 0.9 else ('marginal' if cap >= thr else ('under' if cap >= 0.45 else 'far under'))
        print(f"{w:22s} {cap:10.3f} {band:>9s} {dec:8.2f} {('  n/a' if sh is None else f'{sh:7.2f}')}")
    clears = [r for r in rows if r[1] >= 0.9]
    under = [r for r in rows if r[1] < 0.45]
    print(f"\n# clears (cap>=0.9): {len(clears)} weapons, decided {min(r[2] for r in clears):.2f}..{max(r[2] for r in clears):.2f}")
    print(f"# far under (cap<0.45): {len(under)} weapons, decided {min(r[2] for r in under):.2f}..{max(r[2] for r in under):.2f}")
    worst = max(under, key=lambda r: r[2])
    print(f"# most decisive weapon that CANNOT defeat this tier: {worst[0]} (cap {worst[1]:.3f}, decided {worst[2]:.2f}, "
          f"share {worst[3]}) — the covert-plate-killer residual (F19/ED-PC-0040)")
    return rows


# ── view 2: per-strike damage BY SELECTED HEAD ────────────────────────────────────────────────────
def strike_profile(n=20, armor='heavy', cfg=CFG):
    """What each weapon actually LANDS, keyed by the head `select_mode` chose to land it with.

    This view found F24: `select_mode` repeatedly picks a head that provably cannot wound what it faces. Read the
    rows where `nonzero` is 0.00 on a large `strikes` count — the weapon is choosing that mode over and over and
    getting nothing — and compare a weapon's rows against each other (the podao's `point` at 0.00 against its own
    `curved_cut` at 2.40 is the clean demonstration).

    Implemented by wrapping `core.strike` for the duration of the sweep; the wrapper is always removed."""
    tally = collections.defaultdict(lambda: [0, 0, 0])
    cur = {'w': None}
    orig = core.strike

    def probe(attacker, defender, deg, c, net=None, pool=None):
        v = orig(attacker, defender, deg, c, net, pool)
        if defender.armor == armor and attacker.weapon in (cur['w'], str(cur['w']) + '_halfsword'):
            t = tally[(cur['w'], getattr(attacker, 'sel_head', None))]
            t[0] += 1
            t[1] += (1 if v > 0 else 0)
            t[2] += v
        return v

    core.strike = probe
    try:
        for w in sorted(WEAPONS):
            cur['w'] = w
            rng = random.Random(_seed((w, armor)))
            for _ in range(n):
                wrapper.fight(Combatant('A', weapon=w, armor=armor),
                              Combatant('B', weapon=REFERENCE, armor=armor), cfg, rng)
    finally:
        core.strike = orig

    print(f"# per-strike damage by SELECTED head, vs {REFERENCE} at {armor} ({n} fights/weapon)")
    print(f"{'weapon':22s} {'sel_head':13s} {'strikes':>8s} {'nonzero':>8s} {'mean_dmg':>9s}")
    rows = sorted(tally.items(), key=lambda kv: kv[1][1] / max(1, kv[1][0]))
    for (w, head), (k, nz, tot) in rows:
        print(f"{w:22s} {str(head):13s} {k:8d} {nz/max(1,k):8.2f} {tot/max(1,k):9.2f}")
    mute = [(w, h, k) for (w, h), (k, nz, _) in rows if nz == 0 and k >= 20]
    if mute:
        print(f"\n# SELECTED-BUT-INERT (F24): {len(mute)} weapon/head pairs selected >=20 times for ZERO damage every time —")
        for w, h, k in mute:
            print(f"#   {w} selects {h} {k} times, lands nothing")
    return tally


# ── view 3: the full tier table (the round-trip check ED-PC-0038 skipped) ──────────────────────────
def tier_table(n=200, weapons=None, cfg=CFG):
    """share / decided across ALL FOUR armour tiers. Run at two commits and diff to answer "did this batch move a
    tier it was not aiming at?" — the question ED-PC-0038 did not ask about mail, at a cost of 41 points on the
    odachi."""
    weapons = weapons or sorted(WEAPONS)
    tiers = ('none', 'light', 'medium', 'heavy')
    print(f"# share (decided) vs {REFERENCE}, all tiers, n={n}")
    print(f"{'weapon':22s} " + " ".join(f"{t:>15s}" for t in tiers))
    out = {}
    for w in weapons:
        cells = []
        for t in tiers:
            dec, sh = _duel(w, t, n, cfg)
            out[(w, t)] = (dec, sh)
            cells.append("      n/a (0.00)" if sh is None else f"{sh:9.2f} ({dec:.2f})")
        print(f"{w:22s} " + " ".join(f"{c:>15s}" for c in cells))
    return out


# ── view 4: the committed REFERENCE TABLE + drift detection ───────────────────────────────────────
# ED-PC-0038 aimed at plate and moved MAIL — odachi -23pp, naginata -25pp, staff -12pp — and shipped saying mail was
# "a tier the fix was never meant to touch". ED-PC-0039 then moved the odachi another -18pp, also undisclosed. Neither
# was caught by a test; both were caught, batches later, by a human reading numbers. The reference table below makes
# that mechanical: the full roster x all four tiers is recorded as committed data, and `drift()` reports every cell
# that has moved. `tests/valoria/test_combat_armour_reference.py` turns it into a gate.
#
# The point is NOT to freeze balance. It is to make a balance change VISIBLE AND DELIBERATE: when a change is
# intended, regenerate with `--update`, and the regenerated diff is reviewable evidence of exactly what moved. What
# is no longer possible is moving a tier nobody was looking at and not knowing.
REFERENCE_N = 40
REFERENCE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..',
                              'tests', 'valoria', 'data', 'combat_armour_reference.json')


def reference_table(n=REFERENCE_N, cfg=CFG):
    """{weapon: {tier: [decided, share|None]}} over the whole roster. Seeds are deterministic per (weapon, tier),
    so an UNCHANGED engine reproduces this byte-for-byte and every difference is attributable to a code change."""
    return {w: {t: list(_duel(w, t, n, cfg)) for t in ('none', 'light', 'medium', 'heavy')}
            for w in sorted(WEAPONS)}


def drift(tolerance=0.15, n=REFERENCE_N, cfg=CFG, path=REFERENCE_PATH):
    """Cells that moved more than `tolerance` from the committed reference, plus roster membership changes.

    Returns (moved, added, removed): `moved` is a list of (weapon, tier, field, was, now) sorted worst-first."""
    import json
    with open(path, encoding='utf-8') as f:
        ref = json.load(f)['table']
    now = reference_table(n, cfg)
    added = sorted(set(now) - set(ref))
    removed = sorted(set(ref) - set(now))
    moved = []
    for w in sorted(set(ref) & set(now)):
        for t in ('none', 'light', 'medium', 'heavy'):
            was_dec, was_sh = ref[w][t]
            now_dec, now_sh = now[w][t]
            if abs(now_dec - was_dec) > tolerance:
                moved.append((w, t, 'decided', was_dec, now_dec))
            if was_sh is None or now_sh is None:
                if (was_sh is None) != (now_sh is None):
                    moved.append((w, t, 'share', was_sh, now_sh))
            elif abs(now_sh - was_sh) > tolerance:
                moved.append((w, t, 'share', was_sh, now_sh))
    moved.sort(key=lambda r: -(abs((r[4] or 0) - (r[3] or 0))))
    return moved, added, removed


def write_reference(n=REFERENCE_N, cfg=CFG, path=REFERENCE_PATH):
    """Regenerate the committed reference. Deliberately manual — the resulting diff IS the disclosure."""
    import json
    import subprocess
    try:
        sha = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True,
                             cwd=os.path.dirname(__file__)).stdout.strip() or 'unknown'
    except Exception:
        sha = 'unknown'
    payload = {
        '_': ('Reference armour-interaction table (ED-PC-0040). Regenerate ONLY with '
              '`python workbench/armour_participation.py --update`, and treat the resulting diff as the required '
              'disclosure of what a change moved. Cells are [decided_rate, share_of_decided|null] vs the arming '
              'sword, position-swapped, deterministically seeded.'),
        'generated_at_sha': sha, 'n': n, 'reference_weapon': REFERENCE,
        'table': reference_table(n, cfg),
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=1, sort_keys=True)
        f.write("\n")
    print(f"wrote {os.path.relpath(path)} at n={n}, sha {sha[:8]}")


if __name__ == '__main__':
    if '--update' in sys.argv:
        write_reference()
        sys.exit(0)
    if '--drift' in sys.argv:
        moved, added, removed = drift()
        for w, t, field, was, now in moved:
            print(f"MOVED  {w:22s} {t:7s} {field:8s} {was} -> {now}")
        for w in added:
            print(f"ADDED  {w}")
        for w in removed:
            print(f"REMOVED {w}")
        print(f"# {len(moved)} cell(s) beyond tolerance, {len(added)} added, {len(removed)} removed")
        sys.exit(0)
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    n = int(sys.argv[2]) if len(sys.argv) > 2 else None
    ws = sys.argv[3].split(',') if len(sys.argv) > 3 else None
    if mode in ('participation', 'all'):
        participation(n or 200)
        print()
    if mode in ('strikes', 'all'):
        strike_profile(n or 20)
        print()
    if mode in ('tiers', 'all'):
        tier_table(n or 200, ws)
