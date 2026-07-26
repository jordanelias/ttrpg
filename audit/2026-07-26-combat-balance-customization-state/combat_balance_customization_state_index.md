# Personal Combat — Balance State + Player Customization Surface (SKELETON)

**Author:** PC-lane state report (CLAUDE.md §0) · **Date:** 2026-07-26
**Subject:** `systems/combat/combat_engine_v1/` at `248f344` (post ED-PC-0040, PR #237 merged).
**Status: REPORT — measured state, no engine change.** Nothing here tunes, ratifies or supersedes anything.
**Prose:** `combat_balance_customization_state_infill.md` (co-filed; method, caveats, per-finding detail).

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
