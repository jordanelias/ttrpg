# Personal Combat — Balance State + Player Customization Surface

**Author:** PC-lane state report (CLAUDE.md §0) · **Date:** 2026-07-26
**Subject:** `systems/combat/combat_engine_v1/` at `248f344` (post ED-PC-0040, PR #237 merged).
**Status: REPORT — measured state, no engine change.** Nothing here tunes, ratifies or supersedes anything.

**MEASURED-BY:**
`systems/combat/combat_engine_v1/workbench/balance.py` (weapon / attribute / tradition / context / armour matrix),
`systems/combat/combat_engine_v1/workbench/armour_participation.py` (plate participation),
`systems/combat/combat_engine_v1/workbench/build_levers.py` (skills / abilities / disposition / asymmetric
armour / familiarity / archetypes — **added by this report**, because `balance._mk` cannot express those inputs).
Every number below is a re-run of one of those three at the sha above. Suite at time of measurement:
`pytest tests/valoria` → **877 passed, 21 skipped, 3 xfailed, 3 xpassed** (green).

**Noise floor.** Single cell ≈ **±4pp at n=600**, **±5–6pp at n=300**, **±7pp at n=200**. The mirror control
(`build_levers.py mirror`, n=2000) sits at 50 across three loadouts — arming/light 50.5 / 50.8 / 50.8,
longsword/heavy 49.0 / 51.4 / 47.3, rapier/none 48.5 / 51.8 / 49.7 over seeds 0/1/7 — so 50 is the correct
reference, but a single n=600 cell wanders several points off it on seed alone. Read the CI, not the point.

---

## 1. Balance state — the six headline facts

| # | Fact | Measurement |
|---|---|---|
| B1 | **Reach dominates the duel, and 26 weapons are behaviourally identical.** 26 of 53 sit in a 91–97% band vs the arming sword. | weapon matchup, N=300 |
| B2 | **The 1H sword/sabre class is the floor, not the middle.** sabre 22.5 · shamshir 29.9 · pulwar 30.7 · mace 36.6 · falchion 38.2, against arming's own 49.7. | weapon matchup, N=300 |
| B3 | **Plate is a wall, not a tier.** 38 of 53 weapons settle **zero** of their plate fights; 13 clear the 0.72 threshold and settle 0.59–0.99 of theirs. | participation, n=200 |
| B4 | **Attribute value is concentrated in two stats.** cog +20.4pp / history +19.4pp per point; focus **−0.7pp** (no measurable value). | attribute parity, N=300 |
| B5 | **Traditions are flat because they are nearly inert**, not because they are balanced: spread 3.8pp, `none` **highest** at 52.2. | tradition field, N=200/cell |
| B6 | **Armour is a free win off-plate.** heavy vs none = 95.7%, and the engine charges the wearer nothing for it. | build_levers armour, n=600 |

### 1a. Weapon matchup vs arming — N=300, light armour, uniform-4 build

| band | weapons |
|---|---|
| **91–97 (26 weapons)** | estoc 97.3 · dangpa 96.0 · yari 95.7 · bear_spear/naginata/ji 95.3 · podao/changdao/flamberge 95.0 · odachi 94.7 · spear/voulge 94.3 · partisan/guandao/fauchard 94.0 · bardiche/guisarme/bec_de_corbin 93.7 · kama_yari 93.3 · greatsword 93.0 · spetum 92.7 · ranseur/lucerne_hammer 92.3 · poleaxe/sparr_axe 92.0 · glaive 91.0 |
| 70–85 | longsword 84.3 · rapier 81.7 · goedendag 79.3 · staff 70.5 |
| 49–65 | tachi 64.0 · nandao 59.2 · katana 57.6 · szabla 56.1 · tsurugi 54.2 · jian 53.6 · **arming 49.7** |
| 22–40 | scimitar 39.4 · falchion 38.2 · mace 36.6 · pulwar 30.7 · shamshir 29.9 · sabre 22.5 |
| ≤18 | misericorde 17.4 · stiletto 17.3 · hook_sword 15.0 · rondel 12.0 · dagger 11.7 · paired_short 9.7 · main_gauche 8.3 · cinquedea 5.7 |

### 1b. Weapon × armour arcs — N=200/cell, both fighters at the same tier

⚠️ **A `0.0` in the heavy column means ZERO DECIDED FIGHTS, not a 0% win-rate.** `arming` vs `arming` at
heavy reads `0.0` for exactly that reason. Cross-check every heavy cell against §1c before quoting it.

| shape | weapons | none → heavy |
|---|---|---|
| **rises** (battlefield) | stiletto +87.8 · dagger +85.5 · paired_short +84.9 · misericorde +81.9 · main_gauche +80.5 · rondel +76.0 · mace +67.5 · jian +41.5 · longsword +14.5 · goedendag +13.1 · ranseur +6.5 | 8–24 → 91–100 |
| **flat** (context-independent) | estoc 96.5→95.0 · lucerne_hammer 96.0→97.3 · bec_de_corbin 96.0→94.7 · poleaxe 93.5→95.7 · guandao 94.5→100.0 | — |
| **falls to stalemate** | every pure cutter and every pure reach weapon: spear · yari · spetum · greatsword · flamberge · ji · partisan · fauchard · bear_spear · dangpa · guisarme · voulge · glaive · odachi · changdao · naginata · podao · bardiche · sparr_axe · rapier · katana · tachi · sabre · scimitar · shamshir · pulwar · falchion · nandao · staff · hook_sword · tsurugi · cinquedea · **arming** | → 0 decided |
| **mid-tier cliffs** (light → medium) | sparr_axe 92.0→**22.4** · odachi 91.5→**26.4** · nandao 50.0→**1.6** · scimitar 33.7→**3.3** · shamshir 29.6→**2.6** · staff 73.4→**8.7** · falchion 33.9→**6.9** · sabre 26.8→**6.1** | — |

### 1c. Plate participation — n=200, `ADEF_THRESHOLD[heavy] = 0.72`

| band | count | weapons (capability) | decided |
|---|---|---|---|
| clears (cap ≥ 0.9) | 13 | goedendag 1.300 · mace 1.300 · poleaxe 1.216 · estoc 1.104 · estoc_halfsword 1.104 · stiletto 1.092 · lucerne_hammer 1.063 · bec_de_corbin 1.034 · rondel 1.032 · longsword 1.020 · longsword_halfsword 1.020 · dagger 1.008 · misericorde 1.008 | 0.59–0.99 |
| marginal | 1 | main_gauche 0.744 | 0.23 |
| under | 7 | paired_short 0.696 · cinquedea 0.672 · hook_sword 0.576 · jian 0.543 · tsurugi 0.535 · **arming 0.504** · katana 0.502 | 0.00–0.07 |
| far under (< 0.45) | 32 | rapier 0.419 … fauchard 0.103 | 0.00–0.12 |

**Covert plate-killers (F19 residual, still live):** `ranseur` cap 0.284 settles 0.12 of its plate fights and
wins **100%** of what it settles; `guandao` cap 0.127 settles 0.02, wins 100%. Capability does not gate
penetration — raw magnitude still buys through.

### 1d. Attribute parity — marginal +1 from baseline (str/agi/end 4, rest 3, disp 4), N=300

| attribute | win% | marginal |
|---|---|---|
| cog | 70.4 | **+20.4pp** |
| history | 69.4 | **+19.4pp** |
| att | 61.6 | +11.6pp |
| strength | 61.4 | +11.4pp |
| end | 58.2 | +8.2pp |
| spirit | 56.5 | +6.5pp |
| disp | 55.4 | +5.4pp |
| agi | 55.2 | +5.2pp |
| focus | 49.3 | **−0.7pp — inside noise, no measurable value** |

### 1e. Tradition — unconditional field (N=200/cell) and the C1 context test (N=120/cell)

| tradition | uncond. win% |
|---|---|
| **none** | **52.2** |
| chinese | 50.7 |
| italian | 50.3 |
| english | 50.2 |
| filipino | 50.1 |
| spanish | 49.5 |
| german | 49.3 |
| japanese | 48.4 |

| context | leader | win% | runner-up | spread |
|---|---|---|---|---|
| arming | filipino | 53.4 | english 51.9 | 6.2pp |
| longsword | chinese | 51.9 | italian 51.3 | 4.8pp |
| rapier | english | 52.3 | italian 51.4 | 3.8pp |
| sabre | chinese | 52.1 | italian 50.9 | 5.7pp |
| spear | italian | 52.7 | filipino 52.6 | 4.7pp |

Spread **3.8pp** (was 6.8pp on 2026-06-28). Distinct leaders **4 of 5** (was 2 of 5). Both improved — §3 D5
explains why this is not the C1 win it looks like.

---

## 2. Customization surface — every lever a player has

Nine build inputs. Six are live and load-bearing; two are near-inert; one does not exist. **All are
build-time: `wrapper.engagement()` takes no player-decision parameter** (ED-PC-0001, open) — a fighter is
configured, then the engine resolves the bout autonomously.

| # | Lever | Where | Range | Measured worth | Verdict |
|---|---|---|---|---|---|
| C1 | **Weapon** | `c.weapon` → `weapons.WEAPONS` | 51 startable (+2 auto-switch half-sword forms) | 5.7 → 97.3% vs arming | **dominant** |
| C2 | **Armour** | `c.armor` | none / light / medium / heavy | heavy vs none **95.7%** | **dominant, and free** |
| C3 | **Attributes** | 9 constructor params | integers, ~1–7 | cog/history ≈ +20pp per point; focus ~0 | **live, badly skewed** |
| C4 | **Skills** | `c.skills` dict | 6 axes, **uncapped** | dodge +1 → 66.0; all six +1 → 80.5 | **live, strongest per-point** |
| C5 | **Disposition** | `c.disp` 1–7 | aggression axis | disp 1 → 39.1, disp 7 → 59.8 | **live, but monotone (D3)** |
| C6 | **Tradition** | `c.tradition` | 8 including `none` | ≤3.8pp spread with no kit equipped | **access gate only** |
| C7 | **Techniques + investment level** | `c.equipped` | 8 abilities × level 0–8 | every row inside ±4pp | **texture only, ~0 aggregate** |
| C8 | **Cross-training** | `c.known_traditions` | any set of traditions | widens C7's access; no aggregate effect | **live plumbing, inert payload** |
| C9 | **In-fight tactical choice** | — | — | — | **DOES NOT EXIST** |

### 2a. Skills — `c.skills`, the six axes `c.skill()` is actually called on (n=600)

| axis | engine consumer | +1 → win% |
|---|---|---|
| dodge | `mode_sigma` dodge branch | **66.0** |
| parry | `mode_sigma` parry branch | 60.2 |
| bind | `mode_sigma` wind branch + `bind_sigma` (5 sites) | 58.7 |
| balance | `footwork` | 58.3 |
| technique | `mode_sigma` parry/wind technique term | 52.4 |
| grab | `contact.grab_sigma` (also mitigates the live-edge hazard) | 49.2 — inside noise |
| bind +2 / bind +3 | | 70.5 / 77.0 |
| all six at +1 | | 80.5 |

### 2b. Techniques — the authored roster is 8 abilities across 5 of 8 traditions

| tradition | abilities | lever | op / value |
|---|---|---|---|
| german | `indes` · `staerke_schwaeche` · `zwerchhau` · `ringen_am_schwert` | counter_success · leverage · counter_select · edge_grab | +0.15 · ×1.20 · ×1.4 · ×0.4 |
| italian | `mezzo_tempo` · `misura` | counter_select · measure | ×1.40 · ×1.15 |
| english | `true_times` | anti_overcommit | +0.25 |
| spanish | `atajo` | leverage | ×1.18 |
| japanese | `shinogi` | spine_press | ×1.6 |
| chinese · filipino · none | **(no kit authored)** | — | — |

Investment maths: `ability_bonus = Σ value·level` (additive levers), `ability_factor = Π value^level`
(multiplicative), level ∈ [0, 8] (`MAX_INVESTMENT_LEVEL`), composed factor clamped to [1e-4, 1e3].
Level 0 is exactly inert. The tradition gates **access**, the invested level drives **efficacy**.

Measured (n=600): shinogi L1 49.7 · L2 52.8 · L4 50.0 · L8 56.4 · indes L1 45.9 · L4 48.3 ·
staerke_schwaeche L1 48.3 · L4 49.6 · full german kit L2 47.5 · **untaught shinogi L4 on a german 47.7
(the access gate works)** · cross-trained shinogi L4 on katana 51.4. **Every row inside the ±4pp floor.**

### 2c. Disposition (n=600) — monotone, not a trade-off

| disp | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| win% vs disp 4 | 39.1 | 41.2 | 48.0 | (50) | 54.1 | 54.4 | **59.8** |

### 2d. Asymmetric armour (n=600) — the case `balance.py` cannot show

| cell | win% |
|---|---|
| light vs none | 54.7 |
| medium vs none | 77.5 |
| heavy vs none | **95.7** |
| medium vs light | 80.9 |
| heavy vs light | **94.8** |
| rapier heavy vs rapier none | 95.4 |
| poleaxe heavy vs poleaxe none | 89.4 |

`c.armor` is read **only** as the target's protection — `select_mode`, `armor_defeat_sigma`, `reach_threat`,
`represent_measure_p`, `REACH_W`, `PERC_BLUNT_TRANSMIT`. No site charges the wearer mass, tempo, stamina or
mobility, and `WoundTracker`'s `equipment_health` parameter is never passed a value by `Combatant`.

### 2e. Composite archetypes vs the neutral baseline (n=600)

| archetype | win% |
|---|---|
| armour-breaker (poleaxe, str5 end5, technique1, heavy) | 95.2 |
| reach specialist (spear, agi5, balance1) | 95.0 |
| binder (longsword, str5 cog4, bind2 technique1, german kit L2) | 94.5 |
| duellist (rapier, agi5 att4, dodge+parry 1, italian kit L2) | 93.0 |
| grappler (dagger, str5, grab2 balance1, ringen L3) | **24.3** |

Four different investment stories land within 2.2pp of each other; the fifth is unplayable. The spread is
carried by C1/C2, not by the identity the player bought.

---

## 3. Findings

| # | Finding | Evidence |
|---|---|---|
| D1 | **Weapon choice erases build identity.** Four archetypes converge at 93.0–95.2 because 26 weapons already sit at 91–97. F18's identity erasure is a *build*-level fact, not only a weapon-table one. | §2e, §1a |
| D2 | **Armour has no cost.** Heavy is strictly dominant off-plate and unpriced, so C2 presents a choice with no trade-off to weigh. | §2d |
| D3 | **Disposition is a stat, not a temperament.** Monotone 39.1 → 59.8; `config.py`'s stated "BOTH poles cost" is not what the engine does. | §2c |
| D4 | **Focus buys nothing** (−0.7pp/pt) while cog and history buy ~+20pp each. C3 is a two-stat choice wearing a nine-stat costume. | §1d |
| D5 | **Tradition flatness is inertness, not balance.** With the imposition gate retired (ED-PC-0023) and the channel-weight vector removed (2026-06-29), an ability-less tradition differs from another only through `familiarity()`. `none` scoring **highest** shows the residual is unmodelled rather than balanced, and "4 of 5 distinct leaders" across 4.7–6.2pp spreads at N=120 is noise re-rolling, not context balance. | §1e, §2b |
| D6 | **The technique layer is a surface with almost nothing on it.** 8 abilities, 5 of 8 `eff_cw` channels identity ×1.0 (F23), 3 traditions with no kit at all, every aggregate row inside noise. | §2b |
| D7 | **No tactical layer exists.** C9 is empty; ED-PC-0001 is open. Every "opportunity to fight in a specific manner" is exercised before the fight starts. | `wrapper.engagement()` signature |
| D8 | **`0.0` at heavy is a stalemate, not a loss** — and `balance.py`'s matrix does not say so. A reader quoting that column without §1c will misread 38 weapons. | §1b vs §1c |

**Carried open from ED-PC-0040, re-confirmed live here (not re-discovered):** off-plate reach ~0.94 against
Jordan's ~0.75 target · ranseur/guandao covert plate-killers · medium tier never round-tripped · F21 cutter
grading · F22 roster gaps · F23 hollow channels · F24 selection-vs-damage.

## 4. What this report does NOT do

No constant is changed, no default flipped, no golden re-recorded, no ledger entry filed, no `## Status:`
line moved, no ID allocated. D1–D8 are **observations awaiting Jordan's design calls**, not a work plan —
several of them (D2's armour cost, D3's disposition shape, D5's tradition substance) are design questions
rather than defects with an obvious correct answer. The one artifact added is `workbench/build_levers.py`,
so §2's numbers are a re-runnable query rather than a recollection (the ED-PC-0040 rule).

---

# Part 2 — Method, caveats, and per-finding detail

---

## 1. Why this report exists, and what it is not

The question is two questions: *where is personal combat's balance right now*, and *what can a player
actually change about how their character fights*. The repo answers the first well and the second nowhere —
there is no document that enumerates the build surface, and the instrument that measures balance
(`workbench/balance.py`) structurally cannot reach half of it. `balance._mk` forwards nine attributes plus
weapon, armour and tradition. It has no way to set `c.skills`, no way to set `c.equipped`, no way to set
`c.known_traditions`, and its armour matrix always puts both fighters at the same tier. Four of the engine's
build inputs — and the two that turn out to matter most for the answer — were simply outside what could be
measured with what was in the repo.

So `workbench/build_levers.py` was added. It reuses `balance.py`'s method verbatim (one factor varied against
an otherwise-identical opponent, position-swapped, decisive −1/0/+1, Wilson 95% CI, crc32 seeding) and only
changes the constructor path so those four inputs can be set. It is an instrument, not a gate; nothing in CI
depends on it.

This is a **report**. It changes no constant, flips no default, re-records no golden, files no ledger entry,
allocates no ID, and moves no `## Status:` line. That matters because several of its findings (armour having
no cost, disposition being monotone, traditions being nearly inert) look like defects but are at least partly
design questions, and CLAUDE.md §2's ratification rule means a routine report must not smuggle a hard design
call into a merge.

## 2. Method, and the discipline it is under

### 2.1 The measurement contract

Every number in the index came from re-running one of three instruments at `248f344`:

| instrument | what it produced |
|---|---|
| `workbench/balance.py all 300` | §1a weapon matchup, §1d attribute parity, §1e tradition field + context matrix |
| `workbench/balance.py armour 200` | §1b weapon × armour arcs |
| `workbench/armour_participation.py participation 200` | §1c plate capability partition vs measured decided-rate |
| `workbench/build_levers.py all 600` + `mirror 2000` | §2a–§2e, and the fairness control |

`pytest tests/valoria` was green at the same sha (877 passed, 21 skipped, 3 xfailed, 3 xpassed) — stated
because a balance reading taken on a red tree is worth nothing, not because a green suite validates the
reading. CLAUDE.md §0.1 is explicit that the suite is a shipping gate, not a belief gate; it caught nothing
here because nothing was changed.

### 2.2 The control, run before the readings and not after

CLAUDE.md §0.1's fourth check — *a number without a control is not a measurement* — is the one this report is
most exposed to, because a mirror cell that drifts off 50 would invalidate every relative reading below it.
It was run at n=2000 across three loadouts and three seeds each:

```
arming/light      50.5  50.8  50.8
longsword/heavy   49.0  51.4  47.3
rapier/none       48.5  51.8  49.7
```

Nine cells, all straddling 50, including the heavy-armour loadout where a defect in the armour path would show
up first. The reference is 50.

This control is also what stopped the report's own first draft from being wrong. The n=200 pilot of the
customization sweep returned a mirror cell of **58.1** (CI 51.1–64.7), which excludes 50 and reads exactly like
a fairness bug. It was seed noise: the same cell at n=2000 reads 50.5. Had the pilot's numbers been written up
without re-running the control at a serious n, this document would have reported a phantom first-mover bias
and every lever row would have been silently mis-baselined by 8pp.

### 2.3 The noise floor, and what it disqualifies

A single cell carries roughly ±7pp at n=200, ±5–6pp at n=300, ±4pp at n=600. Nearly every row in §2b (the
ability layer) sits inside that floor. **That is the finding, and it must not be reported as a small positive
effect.** `shinogi L8` at 56.4 (CI 52.4–60.3) is the single ability row that clears 50, at maximum investment
— the top of a bounded scale — and one cell clearing a CI by 2.4pp after eleven cells did not is what a
multiple-comparison artifact looks like. It is reported as "inside the floor, with one marginal cell at max
investment", not as evidence the lever works.

This is the discipline ED-PC-0023's adversarial review imposed on exactly this layer when it retracted the
"+2.8pp specialist edge" as a tradition-membership confound. The correct instrument for a situational lever is
per-fight texture with outcome preservation (`test_levers_add_texture_without_shifting_balance`), not
aggregate win-rate. This report measures aggregate win-rate because the question asked is "what is a lever
worth", and the honest answer for C7 is "not measurable in aggregate — see the texture test for what it *does*
do".

### 2.4 The one claim verified by reading rather than measuring

D2 ("armour has no cost") is a structural claim, so it was checked structurally: every `.armor` read in the
engine was enumerated. `select_mode`, `armor_defeat_sigma`, `reach_threat`, `represent_measure_p`, `REACH_W`,
`PERC_BLUNT_TRANSMIT` and `halfsword_target` all read the **target's** armour; `wrapper.py:240/246` pass
`aggressor.armor` as the defender's view of its opponent; `wrapper.py:471` is trace emission. No site reads a
fighter's own armour to charge them for it, and `Combatant.__init__` never passes `WoundTracker`'s
`equipment_health` parameter, so armour does not add durability either. The measurement (heavy vs none = 95.7)
is then the *consequence* of that structure, not the evidence for it — which is the right way round, because a
win-rate alone could not distinguish "armour is unpriced" from "armour is priced but underpriced".

## 3. The balance state, read in order

### 3.1 Reach still owns the duel (B1)

Twenty-six of fifty-three weapons sit between 91.0 and 97.3 against the arming sword at light armour. The band
is 6.3pp wide and the noise floor at N=300 is ±5–6pp, so most of those weapons are not distinguishable from
each other at all. This is ED-PC-0040's carried-open **F18** ("off-plate reach over-buff + identity erasure;
26 weapons at 94±1"), measured live and unchanged — batch 4 removed the structural obstacle to re-tuning it
and the re-tune was never performed.

The handoff records why it was not: the ~0.75 target Jordan set is **not reachable by lever**. Ablation proved
the dominance is structural, not approach-side — a spear beats an arming sword 0.92 even when forced fully
closed, so it out-fights the sword at every measure rather than winning only the approach. Four levers were
joint-swept (`STOPHIT_CHANCE`, `STOPHIT_COMMIT`, `REPRESENT_BASE`, and a purpose-built `close_crowd_sigma`) and
every configuration that moved off-plate reach toward 0.75 broke `guisarme@heavy` below its floor. The
experiment was reverted. The recorded recommendation is to accept ~0.94 as the honest un-bugged value or
schedule a dedicated closed-phase-model session; nothing in this report changes that assessment.

### 3.2 The bottom of the table is the one-handed sword (B2)

The sabre reads 22.5, the shamshir 29.9, the pulwar 30.7, the falchion 38.2 — all *below* the mace's 36.6 and
far below the arming sword's own 49.7. These are historically-dedicated cutting swords finishing beneath the
weapon class they are supposed to typify. Two known-open items compose to produce it: **F21** (the flat
`ADEF_CUT = −0.90` cutter cliff, now load-bearing because ED-PC-0039's clamp floors every pure cutter's
capability to the same 0) and **ED-PC-0012** (the one-handed sabre-class thrust gap, deliberately deferred).
The mid-tier cliffs in §1b are the same defect seen from the armour axis: the scimitar goes 68.3 → 33.7 → 3.3
across none/light/medium, which is a gambeson reducing a cavalry sabre to a 34% weapon and mail to 3%.

### 3.3 Plate is a wall (B3, D8)

Thirteen weapons clear `ADEF_THRESHOLD[heavy] = 0.72` and settle 59–99% of their plate fights. Thirty-eight
settle **zero**. The `0.0` cells in §1b's heavy column are that stalemate, not a 0% win-rate, and `balance.py`'s
matrix renderer does not distinguish the two — the arming-vs-arming mirror cell also prints `0.0`. Anyone
reading that column without §1c beside it will conclude that thirty-eight weapons *lose* at plate when what
they actually do is fail to resolve.

Whether 38/53 non-participating is correct is a design question, not a bug: ED-PC-0040 files it as
"defensible under PC-5 and historically recognisable, but a large behavioural fact worth a design decision
rather than an inheritance". What is unambiguously still broken is the residual it names: the **ranseur**
(capability 0.284 against a 0.72 threshold) settles 12% of its plate fights and wins 100% of what it settles,
and `guandao` (0.127) does the same at 2%. The penetration knee is a graded threshold multiplier rather than a
gate, so raw head mass still buys through a capability the weapon does not have. That is F19's residual and it
is live at this sha.

### 3.4 Two attributes carry the character sheet (B4, D4)

Cognition is worth +20.4pp per point and History +19.4pp; Focus is worth −0.7pp, which at N=300 means no
measurable value at all. The engine reads Focus through five sites — `conc_max` (`3·Focus + 2·Spirit`), which
then feeds `FOCUS_CONSISTENCY_K = 0.10` and `FOCUS_MENTAL_K = 0.5`, plus two direct reads in
`POISE_FOCUS_K = 0.10` (structure-recovery speed) and `DISRUPT_K = 0.7` (disruption resistance) — and every one
of them is a small coefficient on a channel other terms dominate. A player spending a point on Focus is spending it on
nothing, and a nine-attribute sheet where two attributes carry four times the weight of the other seven is not
a nine-way choice.

Note that this table is *marginal* value from a specific baseline (str/agi/end 4, others 3, disp 4), which is
the correct budgeting instrument per the balancing methodology §3 — cumulative endpoints would mislead. It is
not evidence about how attributes behave at the extremes of their range.

### 3.5 Traditions are flat because they are empty (B5, D5)

The unconditional tradition spread is 3.8pp, down from 6.8pp on 2026-06-28, and four of five weapon contexts
now have distinct leaders where two did before. Read naively, the C1 contextual-balance target has been
substantially met. It has not.

What changed between those two measurements is not that traditions were balanced — it is that they were
**emptied**. The scalar 7-channel weight vector was removed on 2026-06-29 as a degenerate
"who-bought-balance" contest. The imposition gate was retired on 2026-07-23 as top-down scripting
(ED-PC-0023), and `PREFERRED`/`preferred()` were deleted with it (ED-PC-0035). What remains of a tradition, for
a fighter with nothing equipped, is `traditions.familiarity()` feeding `WARINESS_K` — a commit-caution nudge
against an unread style. `balance.py`'s tradition table equips nothing, so it is measuring that single
residual and nothing else.

Two things follow. First, `none` finishing **highest** (52.2) is the tell: if traditions conferred a modelled
advantage, the tradition-less fighter would not lead the field. Second, "4 of 5 distinct leaders" across
spreads of 3.8–6.2pp at N=120 per cell is inside the noise floor by a wide margin — it is the same coin
landing differently five times, not five paradigms each owning a context. The §2b sweep confirms this from the
other direction: german vs chinese (unfamiliar, 0.85 both ways) reads 47.7 and german vs none (familiarity 1.0)
reads 50.6, both inside ±4pp of each other.

This is not a regression. Both removals were correct — a hand-tuned channel vector and a forced preferred-node
coin-flip were exactly the fiat the design principle forbids. But the replacement (tradition gates access to a
kit; investment and skill drive efficacy) has only 8 abilities authored across 5 of 8 traditions, and 5 of the
8 `eff_cw` channels are identity ×1.0 for every legal build (F23). The architecture is right and the content
is not there yet, and "flat" currently means "absent" rather than "balanced".

## 4. The customization surface, lever by lever

### 4.1 What a player is choosing between

Nine inputs. In descending order of what they are currently worth:

**C1 weapon** and **C2 armour** are the decisive choices, and neither is really a *character* choice — they are
equipment. Between them they span 5.7–97.3% (weapon) and 50–95.7% (armour asymmetry). Everything else in the
build is a rounding correction on top of them.

**C4 skills** is the strongest per-point *character* lever and the least designed. `c.skills` is a free-form
dict; `Combatant.skill(axis)` returns `skills.get(axis, 0.0)` with no cap, no budget, and no cost. Six axes are
actually consumed (`bind`, `parry`, `dodge`, `balance`, `technique`, `grab`); anything else a caller puts in the
dict is silently ignored. One point of dodge is worth +16pp — comparable to a point of Cognition and better
than a point of anything else except History. One point in all six axes is worth +30.5pp, and nothing in the
engine stops a build from doing that, or from setting `bind: 50`. The bounding layer is a character-gen/economy
system that does not exist (ED-PC-0024 explicitly defers it as out of engine scope).

The engine's only skill-related safety rail is narrow and instructive: `contact.grab_sigma` clamps the
edge-hazard mitigation at 0 because uncapped skill above 1.0 previously flipped the term's sign, so that a
highly-trained grappler was *rewarded* by how sharp the blade they seized was (ED-PC-0034). One site was fixed;
the uncapped-skill class it belongs to was not.

**C3 attributes** is live but skewed to two of nine (§3.4).

**C5 disposition** is live, and behaves nothing like its specification. `config.py` describes it as a
temperament axis where "BOTH poles cost" — aggression risking overcommit, caution bleeding the Vor — with three
hooks: commit-depth skew, counter-selection tilt, and an initiative drift. Measured, it is monotone: 39.1 at
disp 1, 48.0 at disp 3, 54.1 at 5, 59.8 at 7, a ~21pp swing with no cost anywhere on the aggressive side. The
attribute-parity table agrees independently (+5.4pp for one point of disp from neutral). Whether the intended
shape is a genuine trade-off or whether aggression should simply be good is a design call, but the code and its
own comment currently disagree about which it is.

**C6 tradition** is an access gate (§3.5). Choosing German rather than Italian changes which four techniques
you may invest in and nothing else measurable.

**C7 techniques** and **C8 cross-training** are the layer the design principle leans on hardest — *efficacy from
investment and expertise, not membership* — and the layer with the least content. Eight abilities exist. Three
traditions (`chinese`, `filipino`, `none`) have no kit at all, deliberately: the ability armature's
source-tier discipline forbids authoring an ability without an S1/S2 anchor, and Filipino FMA is explicitly
unanchored. Two of the three bare morphology levers (`edge_read`, `facing_regime`, `choke_control`) are bare for
the same reason — `guardia` and `winden` were both removed as category errors when the HEMA critic caught them,
rather than kept as invented privilege.

The mechanisms around those eight abilities are sound and verifiable. The access gate works: an untaught
`shinogi` at level 4 on a German fighter measures 47.7, i.e. inert, exactly as `_invested()`'s tradition filter
promises. Cross-training works: adding `japanese` to `known_traditions` un-gates it. Graded investment works:
level 0 is exactly inert, `value^level` compounds without crossing sign, and the composed factor is clamped
against the overflow that used to crash resolution at deep investment. What none of it does is move an
aggregate outcome — every row is inside ±4pp.

**C9 does not exist.** `wrapper.engagement(A, B, first, cfg, rng, prev_closed=False)` has no player-decision
parameter. This is deliberate sim-first staging, and ED-PC-0001 is the open item that schedules the input
surface — with a flagged caveat that its own "deliberate deferral" provenance is circular (the audit that
established the intent is the audit that ratified it). The practical consequence for this report's question is
sharp: **every opportunity to fight in a specific manner is exercised before the fight starts.** A player picks
a weapon, armour, attributes, skills, a tradition, techniques and a temperament, and then watches.

### 4.2 The composite test, and what it says about identity

§2e is the question a player actually asks: does my build fight like the thing I built? Four archetypes with
genuinely different investment stories — a rapier duellist buying agility and defensive skills, a longsword
binder buying strength and bind, a poleaxe armour-breaker buying endurance and plate, a spear reach specialist
buying almost nothing — land at 93.0, 94.5, 95.2 and 95.0 against the neutral baseline. The spread across four
distinct identities is 2.2pp, which is inside the noise floor. The fifth, a dagger grappler with the deepest
single-technique investment in the set, reads 24.3.

The read is not "the archetypes are balanced". It is that the archetypes are **not differentiated at all** at
this level: the weapon carried the result in every case, and the skills, techniques and attributes that
constitute the character's identity moved it by less than measurement error. The grappler is low for the same
structural reason — the dagger is an 11.7% weapon off-plate, and no amount of grab skill or Ringen investment
compensates, because the compensation channel is worth a few points and the deficit is forty.

This is D1, and it is the report's most consequential finding for the design question the user asked. The
customization surface is broad — nine levers, 51 weapons, uncapped skills, graded technique investment,
cross-training — and its two equipment levers currently drown the other seven.

## 5. Where the standing documentation is stale

Three surfaces contradict the code at this sha, and a reader coming to combat customization will hit all
three:

1. **`combat_balancing_methodology.md` §7** presents a 2026-06-28 baseline (tradition spread 6.8pp, `none`
   *lowest* at 45.1, "2 distinct leaders", weapons "spear 91 · rapier 88 · staff 84 … mace 28"). Every one of
   those numbers has moved: the spread is 3.8pp, `none` is *highest*, there are 4 leaders, and the weapon table
   is now 26-wide at 91–97 with the staff down at 70.5. The doc labels §7 "a measured point-in-time baseline,
   not balance targets", so it is not lying — but it is the only balance summary in the repo and it is a month
   out of date.
2. **`ability_armature.md` §2c/§7** lists `seize` as a **live** lever with `vorschlag` and `sen_no_sen` built on
   it. `seize` is dead (its pre-contact consumer was cut 2026-06-05) and both abilities have since been removed
   from `ABILITIES` entirely — the roster is the eight in §2b. The armature's own §2c already carries a
   "STATUS CORRECTION … read this, not the per-row markers below" banner, and that banner is itself now stale.
3. **`CURRENT.md`**'s Personal-combat row is accurate but is a single ~4,000-character paragraph covering
   ED-900 through ED-PC-0023. It is a changelog, not an orientation. Nothing in it tells a reader what a player
   can configure.

None of these were edited by this report. Fixing 1 and 2 is a small, safe, PC-lane cleanup; it is listed here
so it is not re-discovered rather than smuggled into a report PR.

## 6. Falsifiers — what would show this report wrong

Per CLAUDE.md §0.1's third check, each claim carries the test that would break it:

| claim | falsifier | outcome |
|---|---|---|
| The 50 reference is sound | `build_levers.py mirror 2000` across 3 loadouts × 3 seeds | 9/9 straddle 50 — **held** |
| Abilities are ~0 in aggregate | any ability row's CI excluding 50 at n=600 | 11 of 12 include 50; `shinogi L8` alone excludes it by 2.4pp — **held, with the exception stated** |
| The tradition access gate is real | untaught `shinogi` L4 on a German moving the result | 47.7, inside noise — **held** |
| Armour has no wearer-side cost | any `.armor` read that charges the wearer | full enumeration found none — **held** |
| Disposition is monotone | any non-monotone cell in disp 1–7 | 39.1 < 41.2 < 48.0 < 50 < 54.1 ≈ 54.4 < 59.8 — **held** |
| `0.0` at heavy is stalemate | participation's decided-rate for those weapons being non-zero | 38 weapons at decided 0.00 — **held** |
| Skills are uncapped | a cap or budget anywhere in the engine | `skill()` is a bare `dict.get`; only `grab_sigma`'s clamp exists — **held** |

The claims this report does **not** make, and which its instruments cannot support: that any of D1–D8 is a
*bug*; that abilities have no per-fight effect (aggregate win-rate cannot see texture — that is what
`test_levers_add_texture_without_shifting_balance` is for); that the roster's win-rates would survive a
character-generation budget (there is none, so every archetype in §2e is unbudgeted); and that any of these
numbers is publication-grade at the balancing methodology's own standard (N≈3000, ±2–3pp). At n=600 this is a
quick read, run at the sha and re-runnable, not a calibration pass.
