"""scaled_orders_of_battle.py — the gauge scenarios rebuilt from HISTORICAL orders of battle.

WHY. The honest gauge scores all 20 rows with **tier-3 single-subunit** bodies: 25 cells, 400
troops, 5 wide x 5 deep. Rendering those (first pass, `png/H3.png`, `png/H4.png`) shows the problem
instantly — an "envelopment wing" is about **two visible cells**, so there is no geometric room for
a wrap and every envelopment row degenerates into two small blobs walking into each other. You
cannot compare that against a Cannae phase-map; there is nothing to compare.

METHOD, per Jordan's directive: take the REAL combatant numbers from the precedent battle, preserve
**the ratio**, **the formation**, and **the number of subunits**, and scale the absolute size down
only as far as the engine's own ceilings force.

Engine ceilings, measured (`config.py`, `engine.SUBUNIT_CAP`):

    MAX_TROOPS_PER_UNIT  10,000       SUBUNIT_CAP  11       BATTLEFIELD_SIZE  50 columns
    spawn rows           A=34, B=15   (19 rows apart, so total depth per side is bounded)
    explicit width x depth per subunit: up to 300 cells (cell cap 200 troops/cell)

So the larger side is pinned at the 10,000 cap and the smaller side is derived FROM THE HISTORICAL
RATIO, not chosen. Depth is **15** per Jordan's directive (was 8–10, which read as a line rather
than a mass).

HISTORICAL BASIS — numbers as cited in `research/diagrams/mass_battle_formations/SOURCES.md` and the
standard accounts:

| row | battle | historical strengths | ratio | formation | subunits |
|---|---|---|---|---|---|
| H3/H4 | **Cannae, 216 BC** (Polybius 3.107–118; Livy 22.44–49; Goldsworthy 2001) | Rome ~80,000 foot + ~6,000 horse = **86,000**; Carthage ~40,000 foot + ~10,000 horse = **50,000** | **1.72 : 1** Roman | Rome: compressed triplex acies, unusually deep. Carthage: convex crescent centre (Gauls/Iberians) that gives ground, African veterans on both wings, cavalry both flanks | Rome 8 · Carthage 7 (3 centre + 2 African + 2 cavalry) |
| H5/H6 | **Leuctra, 371 BC** (Xenophon *Hell.* 6.4; Plutarch *Pelopidas*) | Thebes **~7,000**; Sparta **~10,500** | **0.67 : 1** Theban (outnumbered) | Theban massed left wing 50 shields deep, remainder echeloned BACK (oblique/refused); Spartan line 8–12 deep | Thebes 5 (3 massed + 2 refused) · Sparta 6 |
| H7/H8 | **Zama, 202 BC** / manipular quincunx (Polybius 15.9–14) | Rome **~34,000**; Carthage **~40,000** | **0.85 : 1** | Roman maniples in a quincunx with LANES aligned front-to-back (to swallow elephants) | 6 per side |
| R1/R3 | **Agincourt, 1415** (Curry 2005; Barker 2005) | English **~6,000** (≈5,000 archers); French **~12,000–24,000** | **0.40 : 1** English | Archers massed on the wings behind stakes; French dismounted men-at-arms in deep battles | English 5 · French 6 |
| C1–C7 | **Cannae cavalry / Courtrai 1302 / Waterloo squares** | cavalry ≈ **20%** of the army at Cannae (10,000 of 50,000) | cavalry arm sized at that share | cavalry wider and shallower than foot (`TROOP_TYPE_DENSITY_CAP` caps cavalry at 100/cell) | 4 cavalry bodies vs 6 foot |

**Shapes and builders are the engine's own** (`build_army` / `build_envelopment` /
`build_refused_flank`) with explicit `troops`/`width`/`depth`. This scales the SCENARIO, not the
model: no new mechanism, no new constant, nothing about resolution changes.

⚠ SCOPE. This is a VISUALISATION scale, not a proposal to re-band the gauge. The historical bands in
`mass_battle_gauge_grounding.md` were fitted against the tier-3 battery; re-scoring at this scale
needs its own re-derivation and is deliberately not attempted here.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, '..', '..'))
sys.path.insert(0, os.path.join(_REPO, 'tests', 'sim'))

from mass_battle.engine import (build_army, build_envelopment,  # noqa: E402
                                build_refused_flank, SIDE_A_START_ROW, SIDE_B_START_ROW)

FIELD_W = 51
FIELD_D = 51                 # BATTLEFIELD_SIZE — square, 51 x 51 (odd: a true centre column)
CAP = 10_000                 # MAX_TROOPS_PER_UNIT — the larger side is pinned here

DEEP = 13                    # Jordan directive 2026-07-29 (10 -> 15 -> 13, to fit the 51-row budget)
THIN = 5                     # the Cannae crescent centre / a screen: a third of the mass
CAV_DEEP = 4                 # cavalry fights shallow and wide

STATS = dict(power=4, command=4, discipline=5, morale=6)

# ── DEPLOYMENT GEOMETRY (Jordan directive 2026-07-29) ───────────────────────────────────────────
# Target layout on the 50-deep field, with depth-15 masses:
#
#   rows  0.. 4   free ground behind B      (5 — room to pull back)
#   rows  5..17   side B, depth 13, front face at 17
#   rows 18..32   no-man's land             (15 — the approach)
#   rows 33..45   side A, depth 13, front face at 33
#   rows 46..50   free ground behind A      (5)
#                                           5 + 13 + 15 + 13 + 5 = 51 exactly
#
# MEASURED, because the engine's own spawn constants are misleading here: a formation extends
# DOWNWARD IN ROW INDEX from `starting_position` for BOTH sides. Side A advances toward lower rows,
# so A's FRONT is its start row and its REAR is start+depth-1; side B advances toward higher rows,
# so B's front is start+depth-1. The engine's shipped spawn rows (A=34, B=15) look 19 apart but
# B's own 15-row depth eats 14 of that — the true front-face gap is **5**, which is why bodies were
# in contact within a couple of ticks and no approach phase was ever visible.
#
# FRONT FACES ARE ALIGNED, not start rows. Bodies of different depth (a thin crescent centre, a
# 4-deep cavalry wing) must form ONE battle line, not a ragged one — so the start row is derived
# from the depth rather than shared.
A_FRONT = 33
B_FRONT = 17


def front_row(faction, depth):
    """Start row that puts a body of `depth` on its side's battle line."""
    return A_FRONT if faction == 'A' else (B_FRONT - depth + 1)

# ── historical strengths (men), for the ratio derivation ────────────────────────────────────────
HIST = {
    'cannae':    {'rome': 86_000, 'carthage': 50_000},
    'leuctra':   {'thebes': 7_000, 'sparta': 10_500},
    'zama':      {'rome': 34_000, 'carthage': 40_000},
    'agincourt': {'english': 6_000, 'french': 18_000},
}


def scale_pair(big, small):
    """Scale a historical pair to the engine cap, PRESERVING THE RATIO exactly."""
    hi = max(big, small)
    return round(CAP * big / hi), round(CAP * small / hi)


def _specs(faction, n, w, d, troops_total, shape='Line', troop_type='infantry',
           row_offset=0, col_span=None, **kw):
    """n side-by-side blocks on the side's battle line, centred, sharing `troops_total`.

    `row_offset` echelons a body BACKWARD (away from the enemy) in field terms for either side —
    positive means further from contact, so a refused wing reads the same way on both sides.
    """
    start_row = front_row(faction, d) + (row_offset if faction == 'A' else -row_offset)
    span = col_span or (n * w)
    left = max(1, (FIELD_W - span) // 2)
    per = troops_total / n
    out = []
    for i in range(n):
        s = {'shape': shape, 'tier': 3, 'troop_type': troop_type, 'troops': per,
             'concentration': 100.0, 'width': w, 'depth': d,
             'starting_position': (start_row, left + i * w)}
        s.update(kw)
        out.append(s)
    return out


# ── the armies ──────────────────────────────────────────────────────────────────────────────────

def roman_mass(faction, troops=None, n=8, **kw):
    """Cannae's Roman army: 8 bodies, compressed frontage, DEEP. Polybius' 'many times deeper than
    it was wide' compression is the whole reason the crescent could envelop it."""
    troops = troops if troops is not None else scale_pair(*HIST['cannae'].values())[0]
    return build_army(_specs(faction, n, 4, DEEP, troops, **kw), faction, faction, **STATS)


def carthaginian_crescent(faction, troops=None, **kw):
    """Cannae's Carthaginian army: THIN centre that gives ground + 2 African veteran wings +
    2 cavalry wings = 7 bodies, matching the historical articulation."""
    troops = troops if troops is not None else scale_pair(*HIST['cannae'].values())[1]
    foot = troops * 0.80                       # cavalry was ~20% of the Carthaginian army
    horse = troops * 0.20
    centre = _specs(faction, 3, 5, THIN, foot * 0.45)        # Gauls/Iberians, deliberately shallow
    wings = []
    for col in (6, FIELD_W - 17):                            # African veterans, full depth
        wings.append({'shape': 'Line', 'tier': 3, 'troop_type': 'heavy_infantry',
                      'troops': foot * 0.275, 'concentration': 100.0, 'width': 5, 'depth': DEEP,
                      'starting_position': (front_row(faction, DEEP), col)})
    for col in (1, FIELD_W - 10):                             # cavalry on both flanks
        wings.append({'shape': 'Line', 'tier': 3, 'troop_type': 'cavalry',
                      'troops': horse / 2, 'concentration': 100.0, 'width': 7, 'depth': CAV_DEEP,
                      'starting_position': (front_row(faction, CAV_DEEP), col)})
    return build_envelopment(centre, wings, faction, faction, **STATS)


def theban_oblique(faction, troops=None, **kw):
    """Leuctra: the massed left wing (historically 50 shields deep — here DEEP, the engine's usable
    maximum) with the remainder echeloned BACK. 5 bodies."""
    troops = troops if troops is not None else scale_pair(HIST['leuctra']['thebes'],
                                                          HIST['leuctra']['sparta'])[0]
    back = 6 if faction == 'A' else -6
    strong = [{'shape': 'Line', 'tier': 3, 'troop_type': 'heavy_infantry',
               'troops': troops * 0.7 / 3, 'concentration': 100.0, 'width': 4, 'depth': DEEP,
               'starting_position': (front_row(faction, DEEP), 8 + i * 4)} for i in range(3)]
    refused = [{'shape': 'Line', 'tier': 3, 'troop_type': 'infantry',
                'troops': troops * 0.3 / 2, 'concentration': 100.0, 'width': 5, 'depth': 8,
                'starting_position': (front_row(faction, 8) + back, 28 + i * 5)} for i in range(2)]
    return build_refused_flank(strong, refused, faction, faction, **STATS)


def spartan_line(faction, troops=None, n=6, **kw):
    troops = troops if troops is not None else scale_pair(HIST['leuctra']['thebes'],
                                                          HIST['leuctra']['sparta'])[1]
    return build_army(_specs(faction, n, 5, 10, troops, **kw), faction, faction, **STATS)


def quincunx(faction, troops=None, n=6, **kw):
    """Zama's manipular quincunx: lanes aligned front-to-back. The gaps ARE the formation."""
    troops = troops if troops is not None else scale_pair(*HIST['zama'].values())[0]
    specs = _specs(faction, n, 4, DEEP, troops, col_span=n * 7, **kw)
    for i, s in enumerate(specs):
        r, c = s['starting_position']
        s['starting_position'] = (r + (4 if faction == 'A' else -4) * (i % 2), c + i * 3)
    return build_army(specs, faction, faction, **STATS)


def wedge_army(faction, troops=None, n=5, **kw):
    troops = troops if troops is not None else CAP
    return build_army(_specs(faction, n, 5, DEEP, troops, shape='Arrowhead', **kw),
                      faction, faction, **STATS)


def line_army(faction, troops=None, n=6, depth=DEEP, **kw):
    troops = troops if troops is not None else CAP
    return build_army(_specs(faction, n, 5, depth, troops, **kw), faction, faction, **STATS)


def english_archers(faction, troops=None, n=5, **kw):
    """Agincourt: archers massed, shallow, wide — and heavily outnumbered."""
    troops = troops if troops is not None else scale_pair(HIST['agincourt']['english'],
                                                          HIST['agincourt']['french'])[0]
    return build_army(_specs(faction, n, 6, 5, troops, troop_type='archers',
                             unit_type='ranged', **kw), faction, faction, **STATS)


def french_battles(faction, troops=None, n=6, **kw):
    troops = troops if troops is not None else scale_pair(HIST['agincourt']['english'],
                                                          HIST['agincourt']['french'])[1]
    return build_army(_specs(faction, n, 5, DEEP, troops, troop_type='heavy_infantry', **kw),
                      faction, faction, **STATS)


def cav_wing(faction, troops=None, n=4, **kw):
    """Cavalry arm at the Cannae share (~20% of army strength), wide and shallow."""
    troops = troops if troops is not None else CAP * 0.20
    return build_army(_specs(faction, n, 8, CAV_DEEP, troops, troop_type='cavalry', **kw),
                      faction, faction, speed='Fast', **STATS)


def braced_block(faction, deep=True, n=6, **kw):
    return build_army(_specs(faction, n, 5, DEEP if deep else 5, CAP,
                             troop_type='heavy_infantry', instructions=('brace',),
                             stance='hold', **kw), faction, faction, **STATS)


def cav_envelop(faction, **kw):
    """Combined arms: infantry pins the centre, cavalry wheels the flanks — the ED-MB-0039 'stable'
    regime and the only envelopment shape the engine currently resolves cleanly."""
    centre = _specs(faction, 3, 5, DEEP, CAP * 0.7)
    wings = [{'shape': 'Line', 'tier': 3, 'troop_type': 'cavalry', 'troops': CAP * 0.15,
              'concentration': 100.0, 'width': 7, 'depth': CAV_DEEP,
              'starting_position': (front_row(faction, CAV_DEEP), col)} for col in (1, FIELD_W - 10)]
    return build_envelopment(centre, wings, faction, faction, **STATS)


SCALED = [
    ('H1',  'Line vs Line (mirror) — parity control',          line_army,             line_army),
    ('H2',  'Wedge vs Line',                                   wedge_army,            line_army),
    ('H3',  'Cannae: Carthaginian crescent vs Roman mass',     carthaginian_crescent, roman_mass),
    ('H4',  'Cannae: crescent vs Roman wedge',                 carthaginian_crescent, wedge_army),
    ('H5',  'Leuctra oblique vs Cannae crescent',              theban_oblique,        carthaginian_crescent),
    ('H6',  'Leuctra: Theban oblique vs Spartan line',         theban_oblique,        spartan_line),
    ('H7',  'Zama: Roman quincunx vs Carthaginian line',       quincunx,              line_army),
    ('H8',  'Quincunx vs wedge',                               quincunx,              wedge_army),
    ('H9',  'Line vs wedge (rev H2)',                          line_army,             wedge_army),
    ('H10', 'Roman mass vs Carthaginian crescent (rev H3)',    roman_mass,            carthaginian_crescent),
    ('H11', 'Wedge vs crescent (rev H4)',                      wedge_army,            carthaginian_crescent),
    ('R1',  'Agincourt: English archers vs French battles',    english_archers,       french_battles),
    ('R3',  'Archers vs archers (mirror)',                     english_archers,       english_archers),
    ('C1',  'Cavalry vs steady unbraced line',                 cav_wing,              line_army),
    ('C2',  'Courtrai: cavalry vs BRACED deep block',          cav_wing,              lambda f, **k: braced_block(f, deep=True)),
    ('C3',  'Cavalry vs cavalry (mirror control)',             cav_wing,              cav_wing),
    ('C4',  'Cannae cavalry: envelopment vs line',             cav_envelop,           line_army),
    ('C5',  'Cavalry vs SHAKEN line',                          cav_wing,              lambda f, **k: build_army(
        _specs(f, 6, 5, DEEP, CAP), f, f, power=4, command=4, discipline=5, morale=2, morale_start=6)),
    ('C6',  'Cavalry vs BRACED-shallow line',                  cav_wing,              lambda f, **k: braced_block(f, deep=False)),
    ('C7',  'Cavalry envelopment vs holding line',             cav_envelop,           lambda f, **k: build_army(
        _specs(f, 6, 5, DEEP, CAP, stance='hold'), f, f, **STATS)),
]
