# Weapons from physics — how the engine rates a weapon, and where armour enters

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: PC · IDs: none allocated · `references/id_reservations.yaml` untouched
## Measured at HEAD `c8cc408`. Every number below was produced by calling the named function; §5 gives the commands. None was computed by hand.
## Suite: [README](README.md) · [04 the bout](04_the_bout.md) · [05 two modes](05_two_modes_of_one_bout.md) · **06 weapons** · [07 saying a weapon is good](07_saying_a_weapon_is_good.md) · [08 mass battle](08_mass_battle_units.md)

**What this answers.** How a weapon's characteristics become combat performance; where armour enters;
which of a bout's nine moments read which weapon property; and which tradition techniques a weapon's
geometry admits. [07](07_saying_a_weapon_is_good.md) turns these quantities into things a player can
be told.

---

## 1. Analysis

### 1.1 The record is parts, not stats

`systems/combat/combat_engine_v1/weapons.py` holds **52** records (its header still says 53). A record
is a list of located, massed parts — `elements`, `guards`, `haft`, `pommel` — each with `x_m` (distance
from the working hand), `mass_kg` and `extent_m`; a `geometry` block (`curvature`,
`point_concentration`, `cross_section`, `edge_keenness`, `strike_concentration`); `hands`; a native
`head` (point, cut_thrust, straight_cut, curved_cut, blunt); and, for eleven composites, `mode_elements`
naming the striking parts that afford different fighting modes (poleaxe, bec de corbin, lucerne
hammer, goedendag, guisarme, ji, kama yari, voulge, guandao, fauchard, hook sword).

⚠ `hand_guard` and `blade_guard` appear in each record as literals and are **overwritten at import**
by `weapon_physics.hand_guard()` / `blade_guard()`, which sum the located guards. The rapier's literal
`hand_guard=0.9` is live **0.68**; its `blade_guard=0.45` is live **0.54**. Read the baked value.

### 1.2 Three stages in `weapon_physics.py`

| stage | functions | what is computed | grounding |
|---|---|---|---|
| 1 · statics | `derive(w)` | m_total = Σm · moment = Σm·x · MoI = Σm·(x² + extent²/12) · PoB = moment / m_total | rigid-body statics: parallel-axis theorem plus each part's own rod inertia |
| 2 · force | `percussion_authority`, `puncture_pressure`, `energy_credit` | impact authority from mass and forward balance; a second hand ×1.25; a saturating gain for haft length | the 1.25 two-hand ratio is cited to Oh et al. 2022; the haft gain to Nathan 2003 |
| 3 · dynamics | `agility`, `defense_affinities`, `heft`, `handling`, `at_grip` | handiness; parry / dodge / wind affinities; striking mass; control demand | agility ∝ MoI^−0.25, exponent cited to Cross & Nathan 2009 and Fleisig 2002 |

The module keeps its two kinds of constant visibly apart: exponents and ratios carry the study they
come from, and fitted gains carry `[SIM-CALIBRATE]` and claim no source (`AGILITY_REF`, `PERC_SCALE`,
`PERC_EXP`, the guard-catch multipliers, the affinity band windows). That separation is the model's
best property and should survive every change proposed below.

Check on stage 1: `derive()` gives the rapier a balance point of **9.0 cm** and the arming sword
**11.0 cm**, which are the calibration targets their own records' comments state.

### 1.3 Armour enters three ways

**1 · What gets through — `core.coupling(head, armor, …)`.** Delivery by mode, times transmission by
tier. Blunt force transmits `{none 1.0, light 0.85, medium 0.70, heavy 0.55}` (`PERC_BLUNT_TRANSMIT`).
A cut-and-thrust sword takes the better of its cut arm and its half-sword thrust arm at each tier; the
function's own comment records the cut winning unarmoured (1.500 against 1.450) and the thrust winning
against anything armoured.

**2 · Whether the weapon can threaten this armour — `adef_cap` against `ADEF_THRESHOLD`.** The
thresholds rise with the tier (`light 0.30 · medium 0.45 · heavy 0.72`) and `ADEF_W` weights how much
the comparison matters (`0 · 0.4 · 1.0 · 1.7`). A blunt head takes the better of concussion and
puncture; a point scores on gap-seeking times lever authority; a pure cutter returns `ADEF_CUT = −0.9`
at every tier. The deficit feeds three consumers: `armor_defeat_sigma` (who controls the exchange),
`reach_threat` and `represent_measure_p` (whether a long weapon's reach survives an armoured man who is
not afraid of its point), and `core.damage`'s penetration knee (a blow that does not clear the deficit
leaves little lasting wound; the knee acts only at medium and heavy, where `PEN_THR` is non-zero).

**3 · Which part of the weapon is used — `select_mode`.** Armour chooses the striking element. Measured
damage mode by tier (`select_mode(c, tier, closed=False, cfg)`):

| weapon | none | light | medium | heavy |
|---|---|---|---|---|
| arming sword, longsword | shear | puncture | puncture | puncture |
| poleaxe | puncture | puncture | puncture | puncture |
| bec de corbin | puncture | puncture | puncture | **percussion** |

The poleaxe commits to its spike at every tier; it is the bec de corbin that turns to its hammer
against plate.

Roster totals at each weapon's native head: **25 of 52** clear light armour, **20** clear medium,
**13** clear heavy (bec de corbin, dagger, estoc and longsword in their half-sword forms, goedendag,
lucerne hammer, mace, main gauche, misericorde, poleaxe, rondel, **staff**, stiletto). Sixteen pure
cutters sit at `ADEF_CUT`.

### 1.4 What each moment of a bout reads from the weapon

The nine moments are `state_graph.py::INJECTION_POINTS` ([04](04_the_bout.md) §2). ⚠ That dict's
`injects` column describes how traditions were *meant* to express themselves ("German prefers wind,
Italian refuses it"). The label-keyed imposition gate that did so was retired (ED-PC-0023; its data
deleted, ED-PC-0035). **The only live tradition mechanism is a learned ability on a lever.** The last
column reports that, not the intent.

| # | moment | weapon terms read | live tradition access, and its physical prerequisite |
|---|---|---|---|
| 1 | `approach.measure` | reach (`head_len`, `reach_adj`, `reach_base`); `adef_cap` against the opponent's tier via `reach_threat` | `misura` on the `measure` lever; any weapon |
| 2 | `reopen.measure` | the same reach and deficit logic: `reopen_prob`, `represent_measure_p` | `misura`, through the lever |
| 3 | `exchange.commit` | `lunge_quality` = point_concentration × lightness × hand-balance × one-hand bonus; `recoverability_factor` scales over-commit exposure | English `true_times` (`anti_overcommit`); any weapon |
| 4 | `exchange.read` | `legibility`: a thrust reads hard, a cut or blow easy; tassel `distraction` (ranseur, guandao, jian); double and false edges (`edge_lines`) | none — `edge_read` has no ability |
| 5 | `exchange.mode` | `defense_affinities(w)`: parry from hand_guard and agility, dodge from agility and one-handedness, wind from blade_guard, rigidity, leverage and edge length; `contact_moment_edge` | none tradition-keyed; a fighter favours the wind only through `skill('bind')`, the weapon's wind affinity and learned bind abilities |
| 6 | `exchange.bind_entry` | `leverage()` = grip_len − 0.2·head_len (+0.20 two-handed); blade_guard catch; `edge_vibration` (flamberge); `spine(w)` | German `Stärke-Schwäche` and Spanish `atajo` (`leverage`) on any weapon; **Japanese `shinogi` (`spine_press`) needs a spine — 25 single-edged weapons**, from katana and sabre to glaive and guandao |
| 7 | `exchange.counter` | recovery tempo (`weapon_tempo`, derived from balance and head mass) | Italian `mezzo_tempo`, German `zwerchhau` (`counter_select`), German `indes` (`counter_success`); any weapon |
| 8 | `burst.continuation` | tempo-determined (`ACT_THRESHOLD`, `BURST_MAX`); the weapon enters through its tempo | none — the Chinese and Filipino "flow" tendency is unanchored |
| 9 | `contact.axis` | `grip_choke_max`, `affords_halfsword` (longsword, greatsword, flamberge, estoc), and **the opponent's** `grab_hazard` | German `ringen_am_schwert` (`edge_grab`) lowers the self-injury of seizing **the opponent's** live edge; nothing about the wielder's own weapon limits it |

**The principle, stated exactly.** A tradition never grants what the geometry cannot support, but the
gate sits wherever the physics puts it: for `shinogi`, on the spine of your own blade; for
`ringen_am_schwert`, on the edge of the blade you seize.

---

## 2. Findings that only running the functions shows

**F1 · Material has no reader, so wood is steel.** The `weapons.py` schema note says `material` was
"restored per Phase-0 but DELIBERATELY INERT in R1 (no live reader)", and a search of the engine finds
none. The earlier `proposals/weapon_physics_and_concentration_model.md` used material to derive mass
from density; the live model authors mass per part, so material now informs nothing — including
hardness, which is what separates a wooden staff from an iron mace against a harness. Consequence,
measured: the staff's `percussion_authority` is 5.63 of 8.0, its `adef_cap` **0.915**, and it clears
**heavy** armour (0.72). `core.adef_cap`'s own docstring says *"A wooden staff (low authority) does
NEITHER."* The code contradicts the sentence that documents it.

**F2 · The spine lever is not a katana feature.** `WP.spine(w) > 0` for 25 weapons: bardiche,
changdao, dangpa, falchion, fauchard, glaive, guandao, guisarme, hook sword, ji, kama yari, katana,
naginata, nandao, odachi, podao, pulwar, sabre, scimitar, shamshir, sparr axe, spetum, szabla, tachi,
voulge. `shinogi` is Japanese in provenance and general in physics — which is the design working as
intended, and worth saying so no one "fixes" it into a nationality lock.

**F3 · The parry affinity barely discriminates.** `defense_affinities` bands each affinity into
[0.40, 1.00]. Across the roster parry sits at its floor for **35 of 52** weapons (fifteen distinct
values in all); dodge for 26, wind for 17. Highest parry: main gauche and hook sword 0.95, estoc 0.77,
rapier 0.70. Either most weapons genuinely cannot parry with their hardware, or the band window is
narrower than the roster; the model does not currently say which.

**F4 · Recovery spans two orders of magnitude.** `recoverability_factor` — the multiplier on
over-commit exposure in `overcommit_exposure` — runs from **0.30** (dagger, rondel, cinquedea, paired
short blades) to **23.6** (bardiche), **25.8** (bear spear) and **62.1** (guandao). Whether a 62-fold
exposure is physics or an unexamined tail is not established here; it matters because
[07](07_saying_a_weapon_is_good.md) finds that balance registers mainly *through* this term.

**F5 · Two stale counts.** The `weapons.py` header's "53-weapon roster" is 52;
`affords_halfsword`'s docstring already flags its own stale set.

*Checked and not a finding:* `adef_cap` appears in both `core.py` and `combat_systems.py`, but the second
is a one-line delegate to the first (ED-PC-0038 moved the rule to `core` so the damage path and the
sigma path read one capability). The rule has one owner.

---

## 3. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **W-1** | Resolve F1 in one of two ways, and do not leave the docstring asserting what the code does not do. **(a)** Give armour-defeat a material term — a hardness factor on `percussion_authority` / `puncture_pressure` against rigid tiers, sourced like `energy_credit` or tagged `[SIM-CALIBRATE]`. **(b)** Declare material inert by design and rewrite the `adef_cap` docstring to say a staff defeats plate by mass and leverage. | `weapon_physics.py` stage 2; `core.adef_cap` docstring | (a) staff `adef_cap` < `ADEF_THRESHOLD['medium']` with the mace unchanged at 1.300, pinned by one test; (b) the docstring matches `adef_cap(staff)` | (a) new coefficients; (b) one line | PC lane. The architecture already reserves `material` for exactly this, so it is answerable without a ruling |
| **W-2** | Decide whether F3's floor is intended. If polearms and two-handers genuinely cannot parry with their hardware, say so in `defense_affinities`; if the band should discriminate across the roster, widen the window. | `weapon_physics.defense_affinities` `_band` windows | count of distinct parry values and of weapons at the floor, before and after | small | PC lane |
| **W-3** | Put the recovery tail (F4) on the balance harness before any player-facing word reads `recoverability_factor`. | `combat_systems.recoverability_factor` | guandao exposure and win-rate against a mirror, with a mid-roster control | small | buildable now |
| **W-4** | Correct the two stale counts (F5). | `weapons.py` header; `affords_halfsword` docstring | — | trivial | buildable now |
| **W-5** | State each ability's physical prerequisite as a derived predicate beside the ability — `shinogi` needs `spine(own) > 0`; `ringen_am_schwert` needs `grab_hazard(opponent) > 0` — so a character sheet can answer "which techniques can I use with this weapon" from code rather than prose. | `ability_primitives.py` | every ability names a predicate; a test asserts it | small | PC lane; serves [09](09_the_character_sheet.md) |

Nothing here needs Jordan. W-1 is a model choice the architecture already makes room for; the rest is
repair and measurement.

---

## 4. What this does not establish

- Whether any of these values is *balanced*. Balance is a campaign-level claim and the campaign
  instrument this repository names has no live successor (`CLAUDE.md` §7).
- Whether select_mode's choices are historically right. The table reports what the engine does.

## 5. Reproduce

```sh
cd systems/combat/combat_engine_v1 && python3 - <<'EOF'
import sys; sys.path.insert(0, '.')
import weapon_physics as WP, combat_systems as S, core
from weapons import WEAPONS; from config import CFG; from combatant import Combatant
for n in ('rapier', 'arming', 'staff', 'poleaxe', 'mace'):
    w = WEAPONS[n]; c = Combatant('x', weapon=n)
    print(n, WP.derive(w)['PoB_cm'], round(WP.agility(w), 2), WP.defense_affinities(w),
          round(S.leverage(c, CFG), 3), round(core.adef_cap(w, CFG), 3))
print('spine set:', sorted(n for n, w in WEAPONS.items() if WP.spine(w) > 0))
EOF
```
