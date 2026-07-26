# Personal Combat — Complete Defect Register

**Status: REGISTER — measured/diagnosed, no fix applied.** Companion to
`combat_balance_customization_state_index.md` (the balance state) and
`combat_balance_customization_state_infill.md` (method). Subject: `systems/combat/combat_engine_v1/` at
`248f344`. Date: 2026-07-26.

**MEASURED-BY:** `workbench/balance.py` (matchup N=300, armour matrix N=200/cell) ·
`workbench/armour_participation.py` (plate capability/participation, n=200) · `workbench/build_levers.py`
(build levers, n=600; mirror control n=2000) · direct reads of `weapons.py` for the primitive diagnoses.

**Reading note that governs the whole register:** in the armour matrix a **`0.0` at the heavy tier means ZERO
DECIDED FIGHTS**, not a 0% win-rate. The arming-vs-arming mirror cell prints `0.0` for that reason. Every heavy
claim below is cross-checked against the participation table.

**Provenance discipline:** items marked **[tracked]** already exist in `registers/editorial_ledger_pc.jsonl`,
`HANDOFF_PC.md`, or the four-dimension audit index — they are re-confirmed live here, **not re-discovered**.
Items marked **[new]** were first identified in this pass.

---

## A. Weapon-level defects

### A1 — Weapons with NO context anywhere (dominated at every tier) · severity HIGH

Two weapons lose at every armour tier *and* fail to participate at plate. Every other low-scoring weapon has at
least one tier where it is decisive; these have none.

| weapon | none | light | medium | heavy | plate cap (thr 0.72) | decided @ plate |
|---|---|---|---|---|---|---|
| **cinquedea** | 4.5 | 5.0 | 6.5 | — | 0.672 (under) | **0.00** |
| **hook_sword** | 16.5 | 15.5 | 14.0 | — | 0.576 (under) | **0.00** |

**cinquedea — the worst weapon in the roster, by a wide margin. [new]**
Record: 1H, `cut_thrust`, mass 0.80 kg, `head_len` 0.360 m. It is *dagger-length* (it clears the 0.375 m
open-contact threshold) but carries sword handling and a **wide** blade — the name means "five fingers," which is
its blade width. Low point-concentration follows, so it cannot play the armour-gap thrust game that every other
dagger-class weapon wins with (rondel cap 1.032, stiletto 1.092, misericorde 1.008, dagger 1.008 — cinquedea
0.672). **It is a dagger that cannot dagger, at sword weight, with no reach.** Its 4.5–6.5% across the three
tiers where it can act is not a tuning error; it is a weapon with no purpose in the current model.
*Historically the cinquedea was a civilian status/dress weapon, not an armour tool — so the engine's physics are
arguably right and the missing thing is the context in which "civilian dress weapon" is the correct choice
(see §D2).*

**hook_sword — compounded by A2. [new]**
Record: 1H, `curved_cut`, 2 elements (`curved_cut` + `blunt`), 0.75 kg, `head_len` 0.450 m. Reads 14–16.5% flat
and cannot defeat plate. But hook swords are **a paired system** — they hook together, and the paired use *is*
the weapon. Measuring one solo is the A2 modelling gap, so its number is not trustworthy as a balance finding.

### A2 — Companion/paired weapons measured as primaries · severity HIGH (modelling gap, not balance) · [new]

| weapon | none | light | medium | heavy | what it actually is |
|---|---|---|---|---|---|
| **main_gauche** | 11.0 | 14.0 | 11.5 | **91.5** | a left-hand parrying dagger — used *with* a rapier, never alone |
| **paired_short** | 8.0 | 5.0 | 10.1 | **92.9** | the record's own name says paired |
| **hook_sword** | 16.5 | 15.5 | 14.0 | — | a paired system |

**The engine has no off-hand slot, no paired-weapon system, and no companion-weapon concept.** These three are
therefore being measured in a configuration in which they were never used. Note that `main_gauche` and
`paired_short` both read **~92% at plate** — the engine's own numbers say they are fine as close-quarters
armour tools and broken only as duel primaries, which is exactly the signature of a modelling gap rather than a
balance one.

**Do not "fix" these by buffing them.** The fix is the absent subsystem (§D1).

### A3 — The one-handed cutting-sword collapse · severity HIGH · [tracked, re-confirmed]

Every dedicated cutting sword finishes **below the arming sword's own 49.7**, and three finish below the mace's
36.6:

| weapon | duel (light) | none → light → medium → heavy |
|---|---|---|
| **sabre** | **22.5** | 59.8 → 26.8 → 6.1 → — |
| **shamshir** | 29.9 | 64.1 → 29.6 → 2.6 → — |
| **pulwar** | 30.7 | 53.6 → 24.3 → 4.2 → — |
| **falchion** | 38.2 | 72.6 → 33.9 → 6.9 → — |
| **scimitar** | 39.4 | 68.3 → **33.7** → 3.3 → — |

**The smoking gun is the *light* column.** Light armour is a gambeson — a padded jacket. The scimitar goes
68.3 → 33.7 against one, and to 3.3 against mail. A padded jacket should not halve a cavalry sabre.

Causes, all already on the books: **F21** (flat `ADEF_CUT = −0.90`) · **ED-PC-0039's clamp**, which floored every
pure cutter's capability to the same 0 and so erased grading *within* the cutter class (a bardiche and a shamshir
now fail plate identically) · **ED-PC-0012** (the one-handed sabre-class thrust gap, deferred since 2026-07-08 and
still open).

### A4 — The light→medium cliff · severity HIGH · [tracked, re-confirmed]

| weapon | light | medium | drop |
|---|---|---|---|
| **sparr_axe** | 92.0 | **22.4** | **−70pp** |
| **odachi** | 91.5 | 26.4 | −65pp |
| **staff** | 73.4 | 8.7 | −65pp |
| **podao** | 96.0 | 44.4 | −52pp |
| **nandao** | 50.0 | 1.6 | −48pp |
| **bardiche** | 90.5 | 55.0 | −36pp |

`sparr_axe` is diagnosed in `HANDOFF_PC.md`: a single `straight_cut` element with `adef_cap = −0.90` — it cannot
defeat *any* armour. A sparth/war-axe realistically has a concentrated edge and, being poleaxe-family, a top
spike; compare `poleaxe`'s three elements. ED-PC-0040 separately records that the **medium tier never
round-tripped** after ED-PC-0038 and that the 0039 clamp made the **odachi worse**.

### A5 — Over-performers (the other half of "unbalanced") · severity HIGH · [tracked, re-confirmed]

- **estoc — the single best weapon in the game, with no weakness anywhere.** Duel 97.3; armour arc
  96.5 / 96.0 / 92.0 / 95.0; plate capability 1.104. There is no tier, no armour state, and no matchup context in
  which choosing the estoc is wrong. That is a balance failure in the C1 sense (*no option globally best*) even
  though nothing about it is a *bug*.
- **The 26-weapon 91–97% band** (D1) — a 6.3pp band against a ±5–6pp noise floor, i.e. one dominant option
  wearing 26 names.
- **Covert plate-killers (F19 residual):** `ranseur` capability 0.284 against a 0.72 threshold settles 12% of its
  plate fights and wins **100%** of what it settles; `guandao` (0.127) the same at 2%. Raw magnitude buys through
  a capability the weapon does not have.
- **jian / tsurugi plate paradox:** geometry yields `adef_cap` 0.543 / 0.535, *above* the arming sword's 0.504, so
  a light straight sword out-points the arming sword in the plate stalemate. Low decided-rate, so low impact.

### A6 — Absent from the roster entirely · severity HIGH · [new]

**There is no shield, no buckler, and no targe anywhere in the 51-weapon roster.** Verified programmatically
against `weapons.WEAPONS`.

Sword-and-buckler is the subject of **MS I.33, the oldest surviving fechtbuch**. Rapier-and-dagger is *the*
defining Renaissance civilian pairing. Sword-and-shield is the commonest armed configuration in the period the
setting draws on. Their absence is the largest single content gap in the roster, and it compounds A2: with no
off-hand slot there is nowhere to put a buckler even if one existed.

---

## B. Resolution-layer defects · all [tracked], all open

| # | defect | severity |
|---|---|---|
| B1 | **F24 — selection contradicts damage.** `select_mode` picks heads that provably cannot wound: falchion selects `point` on 46/47 plate strikes for 0 damage; podao picks `point` (mean 0.00) over its own `curved_cut` (mean 2.40) 78% of the time; every 2H sword flips to `blunt` at mail. | high |
| B2 | **F21 — no grading inside the cutter class.** ED-PC-0039's clamp floors every pure cutter to capability 0, so nothing distinguishes a bardiche from a shamshir. | high |
| B3 | **F22 — roster gaps.** sparr_axe horn, falchion point, greatsword/odachi half-sword, staff wound-coupling. | med-high |
| B4 | **F23 — hollow ability channels.** 5 of 8 `eff_cw` channels are identity ×1.0 for every legal build. | med |
| B5 | **F19 — capability does not gate penetration.** At equal capability, head mass still orders penetration (partisan cap 0.176 out-damages spear cap 0.288 at every K). A magnitude knee cannot express the principle; it needs multiplicative gating. | high |
| B6 | **Four-channel armour-defeat double-count with no recorded budget.** The same deficit enters `armor_defeat_sigma`, `reach_threat`, `represent_measure_p` *and* the penetration knee — against a repo rule forbidding exactly that. | high |
| B7 | **38 of 53 weapons decide zero plate fights.** Defensible under PC-5, but a large behavioural fact inherited rather than decided. | design call |
| B8 | **Off-plate reach ~0.94 vs Jordan's ~0.75 target** — and **proven NOT reachable by lever**: ablation shows the spear beats the arming sword 0.92 even when forced fully closed. Needs a closed-phase leverage/damage rework. | high |
| B9 | **`MAX_TEMPO_PEN = 0.8` flat-tops 38 of 53 weapons** to 0.80 — the largest single emergence-suppressor. | high |
| B10 | **`PERC_EXP = 0.30` low-mass compression** over-credits native secondary blunt elements (lucerne fluke, bec beak). | med |
| B11 | **`PERC_TRANSMIT_FLOOR = 0.35` flat-tops 11 Mordhau transmission ratios.** | med |
| B12 | **`adef_cap` blunt branch does not thread `sel_head`** — `puncture_pressure` reads whole-weapon blade-tip concentration for a pommel strike. Latent (ADEF_BLUNT wins the max) but structurally wrong. | low/latent |
| B13 | **`PEN_DEFICIT_K` is exported to a Godot contract whose port has no penetration knee at all.** | parity red |

---

## C. Build-layer defects (the customization surface) · [new, this pass]

| # | defect | evidence |
|---|---|---|
| **C1** | **Weapon choice erases build identity (D1).** Four archetypes with genuinely different investment stories land at 93.0 / 94.5 / 95.2 / 95.0 — a 2.2pp spread, inside noise. | build_levers, n=600 |
| **C2** | **Armour has no wearer-side cost (D2).** heavy vs none = 95.7%. Verified structurally: every `.armor` read is target-side, and `WoundTracker`'s `equipment_health` is never passed a value. | build_levers + full enumeration |
| **C3** | **Disposition is a stat, not a temperament (D3).** Monotone 39.1 → 59.8 across disp 1–7, against `config.py`'s own stated "BOTH poles cost." | build_levers, n=600 |
| **C4** | **Focus buys nothing (D4)** — −0.7pp/pt, inside noise — while cog buys +20.4 and history +19.4. Two of nine attributes carry the sheet. | balance.py attr, N=300 |
| **C5** | **Tradition flatness is inertness, not balance (D5).** Spread 3.8pp with **`none` highest** at 52.2. With the imposition gate retired and channel weights removed, an ability-less tradition differs only via `familiarity()`. "4 of 5 distinct context leaders" across 3.8–6.2pp spreads at N=120 is noise re-rolling. | balance.py tradition + context |
| **C6** | **The technique layer is a correct mechanism with almost no content (D6).** 8 abilities across 5 of 8 traditions; every aggregate row inside the ±4pp floor. | build_levers, n=600 |
| **C7** | **No in-fight tactical layer exists (D7).** `wrapper.engagement()` has no player-decision parameter. | ED-PC-0001, open since 2026-07-05 |
| **C8** | **`balance.py`'s heavy column prints `0.0` for zero-decided (D8)**, not a 0% win-rate — 38 of 53 weapons hit it, and the arming mirror cell prints `0.0` too. | state report §1b vs §1c |

---

## D. Absent subsystems

| # | gap | consequence | status |
|---|---|---|---|
| **D1** | **Off-hand / paired-weapon / shield slot** | A2 and A6 both descend from this. No buckler, no rapier-and-dagger, no case of rapiers, no sword-and-shield. | **[new]** — not designed anywhere |
| **D2** | **Carry context / social-legal weapon availability** | The balance frame assumes every weapon is available in every scene. Historically a rapier was carriable in a city and a spear was not. See the proposal's Appendix B. | **[new]** — Jordan's design direction, 2026-07-26 |
| **D3** | **Multi-combatant** | Engine is strictly 1v1. | designed, DESIGN-ONLY, ED-911 |
| **D4** | **Character-generation economy** | Skills are literally uncapped (`skill()` is a bare `dict.get`); nothing bounds investment. | ED-PC-0024 put it out of engine scope |
| **D5** | **Player tactical layer** | C7 above. | ED-PC-0001, open |
| **D6** | **Terrain / elevation / footing** | No representation at any layer. | never designed |
| **D7** | **Ranged weapons in this engine** | The roster is melee-only. | out of `combat_engine_v1` scope |

---

## E. Instrument and documentation defects

| # | defect | status |
|---|---|---|
| E1 | `balance.py`'s armour matrix renders zero-decided as `0.0`, indistinguishable from a loss (C8). | **[new]** |
| E2 | `combat_balancing_methodology.md` §7's baseline is 2026-06-28 and **every figure has moved** (tradition spread 6.8→3.8, `none` lowest→highest, 2→4 context leaders, the whole weapon table). It is the only balance summary in the repo. | **[new]**, flagged not edited |
| E3 | `ability_armature.md` §2c/§7 still lists `seize` as a **live** lever with `vorschlag`/`sen_no_sen` built on it. `seize` is dead and both abilities were removed from `ABILITIES`. Its own "STATUS CORRECTION" banner is itself now stale. | **[new]**, flagged not edited |
| E4 | `references/values_master.yaml` is quarantined-stale; indexes a nonexistent `engine/params/combat.md`. | tracked (CLAUDE.md §5) |
| E5 | The `UPSET_FLOOR = 0.05` clamp compresses **every** win-rate this engine reports toward [0.05, 0.95], so an observed 0.95 is a raw ~1.00 and the roster's apparent ceiling is partly the clamp. | tracked + tagged (ED-PC-0036) |

---

## F. What is NOT a defect (checked, cleared)

Recording these so they are not re-litigated:

- **Mirror fairness holds.** 9/9 cells straddle 50 at n=2000 across arming/light, longsword/heavy, rapier/none.
- **The ability access gate works.** An untaught technique at level 4 measures 47.7 — inert, exactly as specified.
- **Graded investment and cross-training work**, and level 0 is exactly inert.
- **The dagger class rising to ~95% at plate is correct**, not a bug — it is the canonical armoured-grapple
  finisher (rondel to the gaps), and the participation table confirms the capability that earns it.
- **The mace's arc (24.9 → 92.4) is correct** — the duel-vs-battlefield principle working as designed.
- **No name-keyed weapon or tradition branches exist in live resolution** (verified by the four-dimension audit).
- **The engine's test suite is green**: 877 passed, 21 skipped, 3 xfailed, 3 xpassed.

---

## G. Severity-ordered shortlist

If only five things are fixed, the register says these five:

1. **A6 + §D1 — shields and the off-hand slot.** The largest content gap; also dissolves A2's three false
   negatives.
2. **B1 (F24) — selection contradicts damage.** Weapons are choosing attacks that cannot hurt what is in front
   of them; every number in this register is measured through that defect.
3. **A3 + B2 (F21) — the cutting-sword collapse.** Five historically-central weapons below the baseline, with a
   gambeson as the smoking gun.
4. **C1 + C2 — weapon dominance and free armour.** Together they make every other build lever unmeasurable
   (see the proposal's §9 blocking claim).
5. **A1 — cinquedea and hook_sword.** The only two weapons with no context anywhere; the cheapest concrete fix
   in the register, and cinquedea is the test case for whether carry-context (§D2) is the right frame.
