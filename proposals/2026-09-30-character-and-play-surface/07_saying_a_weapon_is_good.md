# Saying a weapon is good — contribution, suitability, and the words players use

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: PC (presentation) · IDs: none allocated
## Measured at HEAD `c8cc408`; every number was produced by calling the named function (§6).
## Suite: [README](README.md) · [06 weapons](06_weapons_from_physics.md) · **07** · [09 character sheet](09_the_character_sheet.md) · [03 play surface](03_play_surface.md)

**The problem, in Jordan's framing from the session this suite digests:** *"the stat block IS the
physics/geometry/type and its derivations, so for character facing purposes we need to be able to say
if something is good for parrying"* — and *"people will go 'this is a well balanced sword' or 'this
spear handles well' … because they don't think in terms of the raw values but the experience using
it."* The engine resolves relationally, pairing one fighter's terms against another's. This document
says what can honestly be stated about a weapon on its own, how to phrase it, and which quantity each
everyday phrase should read.

---

## 1. Analysis — a contribution is the weapon's; an outcome is the match's

Every relational function in the combat engine is a comparison of per-side terms, and each per-side
term is a function of one fighter's equipment and build. `combat_systems.leverage(c, cfg)` shows it
cleanly: it reads only `c.w` — `grip_len`, `head_len`, `hands` — and nothing about the wielder or the
opponent:

```
lever = grip_len − 0.2·head_len ;  leverage = (0.22/0.30)·(lever − 0.096) [+0.20 if two-handed]
rapier −0.079 · arming sword 0.000 · longsword 0.193 · staff 0.622 · poleaxe 0.658
```

"A long-gripped two-handed weapon brings real leverage to a bind, and a rapier almost none" is true,
general, and statable with no opponent in the room. What is relational is `bind_sigma`, which takes the
*difference* of two fighters' `leverage()` plus guard catch, tactile read, a moment term and wound
state, and decides who wins a particular bind. So there are two kinds of number:

| kind | examples | can go on a weapon's card? |
|---|---|---|
| **contribution** — a function of one weapon | `defense_affinities`, `agility`, `lunge_quality`, `leverage`, `weapon_tempo`, `recoverability_factor`, `heft`, `adef_cap` against each fixed armour threshold, `spine`, `affords_halfsword`, `grab_hazard` | yes |
| **outcome** — a comparison of two sides | `bind_sigma`, `mode_sigma`, `reach_threat`, `armor_defeat_sigma`, `read_contest` | only in a matchup preview, computed live |

The one term that does not decompose is `traditions.familiarity(a, b)`: a lookup keyed on both
traditions at once (the `ADJACENT` pairs). There is no "how familiar is this tradition" on its own.

## 2. Measured — what a handful of weapons bring

Contribution terms, native grip. Higher is better except `recov`, which multiplies over-commit
exposure (lower recovers better). `heft` feeds damage only for cut and thrust heads; a blunt weapon's
damage runs on percussion authority (`core.damage`).

| weapon | PoB cm | MoI | agility | tempo | recov | heft | lunge | parry | dodge | wind | leverage | armour-defeat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dagger | 3.7 | 0.003 | 0.92 | 1.85 | 0.30 | 0.19 | 1.00 | 0.40 | 1.00 | 0.40 | −0.013 | 1.008 |
| arming sword | 11.0 | 0.135 | 0.36 | 1.25 | 0.71 | 0.77 | 0.77 | 0.56 | 0.68 | 0.57 | 0.000 | 0.504 |
| rapier | 9.0 | 0.158 | 0.34 | 1.25 | 0.67 | 0.76 | 1.00 | 0.70 | 0.66 | 0.71 | −0.079 | 0.419 |
| longsword | 13.9 | 0.208 | 0.32 | 1.20 | 0.98 | 1.00 | 0.48 | 0.58 | 0.50 | 0.72 | 0.193 | 0.613 |
| estoc | 19.7 | 0.576 | 0.25 | 1.09 | 1.84 | 1.91 | 0.32 | 0.77 | 0.40 | 1.00 | 0.291 | 0.522 |
| katana | 18.8 | 0.104 | 0.38 | 1.22 | 0.85 | 1.53 | 0.54 | 0.43 | 0.58 | 0.43 | 0.274 | −0.900 |
| greatsword | 18.0 | 0.897 | 0.22 | 0.95 | 3.15 | 1.60 | 0.14 | 0.54 | 0.40 | 0.90 | 0.231 | −0.900 |
| spear | 69.2 | 1.966 | 0.18 | 0.81 | 8.28 | 0.67 | 0.21 | 0.40 | 0.40 | 0.40 | 0.152 | 0.288 |
| staff | 0.0 | 0.348 | 0.28 | 1.28 | 0.46 | — | 0.03 | 0.40 | 0.45 | 0.40 | 0.622 | 0.915 |
| poleaxe | 37.1 | 1.461 | 0.20 | 0.83 | 5.44 | — | 0.17 | 0.40 | 0.40 | 1.00 | 0.658 | 1.300 |
| mace | 41.9 | 0.244 | 0.31 | 1.00 | 2.59 | — | 0.01 | 0.40 | 0.60 | 0.40 | 0.004 | 1.300 |

Armour-defeat thresholds for comparison: light 0.30, medium 0.45, heavy 0.72.

**The rapier, read correctly.** Parry 0.70 and wind 0.71 come from its baked swept hilt (hand_guard
0.68, blade_guard 0.54) and long blade; its leverage, −0.079, is the lowest on the roster. So the rapier
*meets* a bind well and cannot *dominate* one — which is the physically exact form of "the rapier does
not seek the bind", arrived at from the record rather than asserted as tradition flavour.

## 3. Measured — where "well balanced" actually lives

A test case built for this question: take the arming sword, move its 0.369 kg counterweight pommel
onto the blade (same total mass, bad balance), and make the head blunt. Then read every contribution:

| term | arming sword | badly balanced blunt copy | change |
|---|---|---|---|
| balance point | 11.0 cm | 29.5 cm | 2.7× further from the hand |
| MoI | 0.135 | 0.177 | +31 % |
| agility | 0.36 | 0.33 | −8 % |
| parry / dodge / wind | 0.56 / 0.68 / 0.57 | 0.53 / 0.64 / 0.58 | hundredths |
| **recoverability (over-commit exposure)** | **0.71** | **1.58** | **2.2× worse** |
| **tempo** | **1.25** | **1.12** | **10 % slower** |
| lunge quality | 0.77 | 0.60 (0.05 if the point is also blunted) | — |
| damage basis | cut/thrust heft 0.77 | percussion authority 7.18 of 8.0 | now a club |
| armour-defeat | 0.504 | **1.167** — clears plate | see below |

Three findings, each of which changes what a player-facing description should read:

1. **Balance barely moves the affinities.** Parry, dodge and wind are dominated by guard hardware and
   compressed by their bands ([06](06_weapons_from_physics.md) F3). A "well balanced" descriptor that
   read them would call a badly balanced sword nearly as good as a well balanced one.
2. **Balance lives in recovery and tempo.** Moving the pommel more than doubles the exposure to a riposte
   after over-committing and slows the cadence by a tenth. That is what "well balanced", "lively" and
   "quick to recover" mean in this engine, and it is where those words should read.
3. **The engine cannot tell a wooden waster from an iron club.** The blunt copy's armour-defeat of
   1.167 clears heavy plate because `material` has no reader ([06](06_weapons_from_physics.md) F1).
   Asked in the session whether a blunt wood sword with bad balance is worse than a good sharp one, the
   honest answer is: worse at everything a sword is for — cutting (gone), thrusting (lunge 0.60 or less),
   recovering (2.2× exposure) — and, today, *better* against plate than it has any right to be.

## 4. Suitability for an action — the phrasing

Jordan, in the same session: *"we can even discuss it as suitability for an action if we want to avoid
claiming a fixed value since relational."* That is the right grammar, and it is not new: the tradition
decomposition already describes techniques as **access**, **bias** and **tendency** — a tendency being
"a propensity", not a guarantee ([04](04_the_bout.md) §1). Weapons are the same kind of object — a fixed
contribution into a contest that also needs the other side — and should share the grammar. It also
supplies the unit: suitability for *which* of the nine moments.

- Staff — leverage 0.622: **well suited to winning the bind** (`exchange.bind_entry`).
- Rapier — parry 0.70, leverage −0.079: **suited to meeting a bind and to the parry, poorly suited to
  dominating the bind.**
- Arming sword — leverage 0.000: **no particular suitability either way for the bind** — neither
  strength nor flaw, which a good/bad verdict cannot say and suitability can.
- Spear — reach, but armour-defeat 0.288: **suited to holding measure against the unarmoured; the
  suitability falls as the opponent's armour rises**, because `reach_threat` decays with the deficit.
  The phrase carries its condition instead of hiding or overstating it.

## 5. The words players use, and what each should read

| everyday phrase | reads | not |
|---|---|---|
| well balanced · lively · quick to recover | `recoverability_factor`, `weapon_tempo`, `agility` | the affinities (§3 finding 1) |
| blade-heavy · point-heavy · sluggish | `PoB_frac` high with `recoverability_factor` high | — |
| hits like a hammer · authoritative | `percussion_authority` (blunt), `heft` (cut, thrust) | — |
| a parrying weapon · keeps the hand safe | parry affinity (hand_guard × agility) | — |
| commands the bind · strong in the bind | `leverage`, wind affinity | — |
| holds them at the point | reach with `adef_cap` against the tier | reach alone |
| punches through mail · turns on plate | `adef_cap` against the medium / heavy thresholds | — |
| can be gripped by the blade | `affords_halfsword` | — |

The phrases already exist in the vocabulary of people who handle swords, and their physical referents
are the quantities in the left column; the mapping is closer to translation than authorship. Each phrase
is a **band**, which is the repository's own presentation rule: the precedent research's S6 —
*"Publish every input. Publish a band, not a number. Never publish the trigger point."*
(`research/valoria_game_precedent_companion_v1_part2.md` §5) — grounded in Jagged Alliance 2, whose
social layer was loved and whose tactical arithmetic was resented in the same game.

The cost, stated rather than discovered: a dozen phrases compress a continuous space, and two weapons
that differ underneath can share a phrase. That is the legibility-against-depth problem the same
research records as unsolved across the genre (its D2). Choose the number of bands deliberately.

## 6. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **C-1** | A pure `weapon_card(w)` returning the contribution terms of §1, and nothing computed anywhere else. No summariser exists today. | beside the physics, in `systems/combat/combat_engine_v1/` | a test asserts each card field equals its named function's output | small | buildable now |
| **C-2** | The descriptor vocabulary as data: phrase × term × band, with band breakpoints taken from the roster's own distribution (quantiles over the 52 weapons), not invented constants. | a YAML under `references/`, one loader (`CLAUDE.md` §0.05: a term code reads lives where code reads it) | every phrase names its term; re-banding after a roster change moves no phrase by hand | small | PC lane |
| **C-3** | Phrase every weapon judgment as suitability for a named moment; show outcomes only in a matchup preview computed live against the actual opponent, as signed contribution differences, never as the threshold. | presentation layer ([03](03_play_surface.md)) | no card field is a `*_sigma` | — | design rule |
| **C-4** | Before shipping "well balanced" or "handles well", settle [06](06_weapons_from_physics.md) W-3 (the recovery tail) and W-1 (material). Otherwise the card will call a guandao unrecoverable by a factor of 62 and a wooden staff a plate-breaker. | — | — | — | ordering |
| **C-5** | Resolve the parry floor ([06](06_weapons_from_physics.md) W-2) before "a parrying weapon" is offered as a descriptor: today it would read "poor" for 35 of 52 weapons. | — | — | — | ordering |

## 7. Reproduce

```sh
cd systems/combat/combat_engine_v1 && python3 - <<'EOF'
import sys, copy; sys.path.insert(0, '.')
import weapon_physics as WP, combat_systems as S, core
from weapons import WEAPONS; from config import CFG; from combatant import Combatant
b = copy.deepcopy(WEAPONS['arming']); b.pop('_derived', None)
b['elements'][0]['mass_kg'] += b.pop('pommel')['mass_kg']; b['head'] = 'blunt'
WEAPONS['bad'] = b
for n in ('arming', 'bad'):
    w, c = WEAPONS[n], Combatant('x', weapon=n)
    print(n, round(WP.derive(w)['PoB_cm'], 1), WP.defense_affinities(w),
          round(S.recoverability_factor(c, CFG), 3), round(S.weapon_tempo(c, CFG), 3),
          round(core.adef_cap(w, CFG), 3))
EOF
```
