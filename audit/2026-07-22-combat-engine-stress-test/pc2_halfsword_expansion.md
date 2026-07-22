# PC-2 — half-sword roster expansion (attested ricassos): CAPABILITY SHIPPED, ACTIVATION HELD

**Lane:** PC · **ID:** ED-PC-0016 (`needs_jordan`) · **Date:** 2026-07-22 · **Depends on:** PC-1 (ED-PC-0014), PC-5 (ED-PC-0015)

## Summary

The register's **PC-2** is the half-sword roster expansion — extend the emergent half-sword capability
(PC-1) to the other attested-ricasso weapons per Jordan's ruling *"the ricasso is a physical fact — any
weapon with a ricasso + the required geometry half-swords."* The two attested candidates are **greatsword**
(`weapons.py`: blade "with ricasso, often flanked by parrying lugs") and **flamberge** (a dedicated
`ricasso` element, "blunted forward gripping section", flanked by **Parierhaken** hooked side-lugs — a
historical half-sword grip stop).

**What shipped (this PR):** the CAPABILITY substrate — `grippable=True` on both weapons' ricasso elements
(the physical fact, S-graded like `edge_keenness`). Both pass the geometry gate (`geo['halfsword']=True`,
`can_halfsword_thrust`; the flamberge's undulations are edge-local, its overall axis is straight and you
grip the plain ricasso, so it correctly qualifies), so `affords_halfsword` now = **{longsword, estoc,
greatsword, flamberge}**.

**What is HELD (deliberately not wired):** the auto-**switch** activation (the `*_halfsword` form records +
their `HALFSWORD_FORM` entries). An adversarial pass proved the naive activation ships a **net liability**,
and that the obvious cheap fix is **unsound**. Activation needs a duel-aware decision — a design call held
for Jordan.

---

## Adversarial finding 1 — the naive unconditional switch is a LIABILITY for these weapons

With the forms wired into `HALFSWORD_FORM` (the PC-1 unconditional `closed ∧ opp_armor∈{medium,heavy}` gate),
seeded winrate vs a uniform arming baseline (n=300, before = base weapon, after = with the switch):

| weapon | none | light | **medium** | **heavy** |
|---|---|---|---|---|
| greatsword | 94→94 | 90→90 | **93→50** | **71→55** |
| flamberge  | 93→93 | 95→95 | **93→49** | 72→69 |

The switch *loses* ~40pp at medium and ~16pp at heavy for the greatsword. **Root cause (different from the
longsword's):** unlike the longsword — whose base cut_thrust genuinely cannot defeat a harness, so
half-swording is a net gain (PC-5: 38→73% at heavy) — the greatsword/flamberge base forms **already
out-fight** their half-sword forms when closed, on **reach + mass**. Forcing the half-sword throws those
away for a gap-thrust they don't need. This is precisely the liability class PR #210 flagged as the reason
*not* to expand the ricasso set before the mechanism was correct.

## Adversarial finding 2 — the cheap per-form conditional is UNSOUND

The natural fix — make `halfsword_target` conditional: switch only when the half-sword form *out-delivers*
the base form's own best closed mode vs that armour — was tested and **rejected**. Using the engine's own
damage function (faithful `core.strike` mirror: real `sel_perc`, `heft_resp`, `thrust_auth`), the single-strike
`'success'`-degree closed-damage comparison is **strength-fragile and contradicts the full-duel outcome**:

| strength | longsword @heavy | greatsword @heavy |
|---|---|---|
| 3 | BASE (6/5) | **HALF (3/4)** |
| **4 (roster default)** | **BASE (7/7)** | **HALF (4/5)** |
| 6 | HALF | BASE |

At the roster-default strength=4 the single-strike signal says the **opposite** of the duel: it would make
the longsword *not* half-sword at heavy (breaking PC-5's validated 73% win) and the greatsword *switch*
(the very liability we're avoiding). The signal flips with strength because a blunt/mass mode's damage
scales super-linearly with strength while a point's is near-linear. **The real signal is the full-duel
dynamics** — armour-defeat **sigma-control** (`armor_defeat_sigma`), **reach** (`reach_base`/`reach_threat`),
and multi-exchange tempo — none of which a single-strike, per-form predicate can see. Curve-fitting a
strength or heft threshold to force the right answer would be exactly the self-referential fit CLAUDE.md §7
warns against.

## Recommendation (the real design question — for Jordan)

The half-sword switch decision belongs where the **reach differential vs the actual opponent** is known —
the **wrapper** (it already holds both combatants at the call site, `wrapper.py:123`). Options:

1. **Duel-aware conditional** at the wrapper: half-sword only when the fighter's base reach/mass advantage
   over *this* opponent is not already decisive (needs one calibration anchor — a real design call).
2. **Half-sword as a competing MODE** (not a whole-weapon form swap): let `select_mode`/the exchange choose
   the shortened grip when it out-couples, so the choice emerges from the same comparator as every other
   mode. Larger refactor; most aligned with the primitive-law/emergence doctrine (§0/§8).
3. **Close-efficacy calibration**: a long weapon's full-grip point may be over-rated at grapple range (that
   unwieldiness is *why* one half-swords); fixing `close_efficacy` for long weapons could make the half-sword
   naturally win the closed comparison.

Until one lands, greatsword/flamberge record the capability (`affords_halfsword=True`) but do not switch —
behaviorally inert, no liability.

---

## Ready-to-activate artifact — the authored `*_halfsword` form records

Authored to the estoc/longsword half-sword convention (total length + mass conserved; the gripped forte
folds into the haft; the free blade tip projects forward; guard/pommel trail behind the working hand). Both
derive to sane forms (mass conserved; `heft=0`/negative `PoB_frac` — the established half-sword signature,
identical to `longsword_halfsword`) and saturate PC-5 thrust authority (`greatsword_halfsword` head_len 0.60
→ tauth 0.92; `flamberge_halfsword` head_len 0.455 → tauth 1.0). Drop these into `weapons.py` and add to
`HALFSWORD_FORM` once the activation decision (above) lands:

```python
 # half-sword: the SHORTENED greatsword (working hand up on the ricasso/forte; the ricasso + parrying lugs
 # are the attested grip). Total length + mass conserved from the base.
 'greatsword_halfsword': dict(
   mass=2.751, head_len=0.6, grip_len=1.05, hands=2, head='point', hand_guard=0.4, blade_guard=0.45, reach_adj=-0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.3, mass_kg=0.673, extent_m=0.6, orient_deg=0, material='steel'),  # free blade tip (forward of the new hand-on-blade grip point)
    ],
   guards=[
     dict(x_m=-0.66, mass_kg=0.19, extent_m=0.26, type='cross', orient_deg=90, material='steel'),  # cross guard (trailing behind the working hand)
    ],
   haft=dict(x_m=-0.525, mass_kg=1.004, extent_m=1.05),
   pommel=dict(x_m=-1.05, mass_kg=0.884),
   geometry=dict(curvature=0.0, point_concentration=0.72, cross_section=0.92, edge_keenness=0.5, strike_concentration=0.1),
   base='greatsword'),

 # half-sword: the SHORTENED flamberge — the forward hand grips at the Parierhaken (the hooked side-lugs are
 # the attested half-sword grip stop), so the plain distal tip projects forward while the flame-ground/waved
 # section stays BEHIND the hand (you grip the plain ricasso/forte, never the waves).
 'flamberge_halfsword': dict(
   mass=2.7001, head_len=0.455, grip_len=1.195, hands=2, head='point', hand_guard=0.4, blade_guard=0.5, reach_adj=-0.05,
   wclass='bladed', hilt='simple',
   elements=[
     dict(x_m=0.23, mass_kg=0.4641, extent_m=0.45, orient_deg=0, material='steel'),  # free blade tip (plain distal section, forward of the Parierhaken grip point)
    ],
   guards=[
     dict(x_m=0.0, mass_kg=0.1266, extent_m=0.1, type='lug', orient_deg=60, material='steel'),  # Parierhaken (now AT the working hand, the forward grip stop)
     dict(x_m=-0.75, mass_kg=0.2953, extent_m=0.3, type='cross', orient_deg=90, material='steel'),  # main cross-guard (trailing behind the working hand)
    ],
   haft=dict(x_m=-0.5975, mass_kg=1.3517, extent_m=1.195),
   pommel=dict(x_m=-1.195, mass_kg=0.4624),
   geometry=dict(curvature=0.0, point_concentration=0.72, cross_section=0.92, edge_keenness=0.5, strike_concentration=0.1),
   base='flamberge'),
```

And the `HALFSWORD_FORM` additions (held): `'greatsword': 'greatsword_halfsword', 'flamberge': 'flamberge_halfsword'`.
