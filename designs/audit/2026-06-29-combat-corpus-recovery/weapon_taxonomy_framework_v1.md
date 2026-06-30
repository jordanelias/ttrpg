# Weapon Taxonomy & Weapon-Tradition Framework — v1
**Class-C proposal · OPEN · Jordan-vetoable · 2026-06-12 · personal-combat (F2 ruling)**

`[SELF-AUTHORED — bias risk: I built this on my own prior weapon work; the structural/naming calls (§5) are yours.]`

Built **bottom-up** from the live engine weapon vectors (`combat_engine_v1/combatant.py`) + the ratified axis substrate (`weapon_axes_v2.md`), and **top-down** from the project's own historical research (`martial_traditions_mapping.md`, the seven-axes/bridge corpus). No canon retconned; every per-weapon number below is an *existing* engine value or is flagged as a tunable.

This responds to F2's three asks: (1) a bottom-up weapon taxonomy keyed on **head type · balance · length · grip**; (2) historical infill of what weapons sit where; (3) **≥2 weapon-traditions that directly inform how a weapon of a given type is used**, plus the "more classes / class specialization" answer.

---

## §1 — What already exists, and the one axis F2 adds

`weapon_axes_v2` ratified a six-axis substrate (`reach · weight · hands · head · speed · handling`) and reclassified ~15 weapons as points in it. The engine's `combatant.py` carries each weapon as a vector with those fields **plus** `mass`, `pob_frac` (point-of-balance), `head_len`/`grip_len` (lever-arm), `gap`, `clinch`, `percussion`, guard primitives.

The gap against Jordan's four named axes:

| Jordan's axis | Already in the model? | Source |
|---|---|---|
| **head type** | ✅ `head` = point / cut-and-thrust / straight-cut / curved-cut / blunt | `weapon_axes_v2 §2` |
| **balance** | ⚠️ **data present, unconsumed** — `pob_frac` exists on every weapon but **nothing reads it** (this is exactly the F5 "dead `mass`/`pob_frac` data") | `combatant.py` |
| **overall length** | ◐ binary `reach` (short/long); a continuous length (`head_len`+`grip_len`) is present but only `reach` is resolved | `combatant.py` |
| **grip** | ✅ `hands` (1H/2H) + off-hand slot + dynamic `grip` state (normal/choke/lunge) + half-sword re-vector | `weapon_axes_v2 §3`, `combatant.py` |

**The one genuinely new axis is balance** — and adding it **resolves F5's dead-data finding by consumption rather than reversion**: `pob_frac` (and `mass`, via F7) stop being dead the moment balance and the Strength-gated damage cap read them. *This changes the F5 recommendation: do not revert the `mass`/`pob_frac` commit — F2 + F7 give those fields a job.*

---

## §2 — The taxonomy: four primary axes (Jordan-named) + three supporting

| Axis | Values / band | Engine field | Drives |
|---|---|---|---|
| **Head type** | point · cut-and-thrust · straight-cut · curved-cut · blunt | `head` | armour interaction (point finds gaps; cut degrades vs plate; blunt crushes), bind behaviour, cut↔thrust mode |
| **Balance** *(NEW consumption of `pob_frac`)* | **hilt-balanced** ≤0.15 · **neutral** 0.15–0.35 · **head-heavy** >0.35 | `pob_frac` | **recovery/tempo** (hilt = fast recover, head-heavy = committed/slow), **point & edge agility** (hilt = nimble), **percussive impact + bind leverage** (head-heavy = more crush, more leverage in the clinch) |
| **Length** | **short** <2 · **medium** 2–3.5 · **long** 3.5–5 · **polearm** >5 (units = `head_len`+`grip_len`); current binary `reach` is the resolved coarse form | `reach` (+ `head_len`/`grip_len`) | measure, phase-dependent reach-TN, **how many grid squares the weapon threatens (F1)** |
| **Grip** | 1H / 2H · + off-hand slot (1H) · + grip-state normal/choke/lunge · + half-sword form | `hands`, `grip` | bind leverage (2H → +Strength δσ), off-hand loadout (dagger/buckler/shield), reach (grip-length), the half-sword head→point re-vector for armoured thrusts |
| *weight* (supporting) | light / heavy | `wt` / `mass` | STR-multiplier, speed, STR-min; **`mass` feeds the F7 Strength-gated damage cap** |
| *speed* (supporting) | scalar −0.5 … 3 | `spd` | tempo channel |
| *handling* (supporting) | Forgiving / Standard / Demanding | `hand` | skill curve (mass-troop learnability vs technical ceiling) |

**Why balance is not redundant with weight + head.** A longsword and a greatsword are both `heavy cut-and-thrust`, but balance .14 vs .22 — the greatsword commits harder and recovers slower. A mace and a poleaxe are both `heavy blunt`, but .60 vs .45 — the mace is a forward-mass levy crusher, the poleaxe a hafted lever for grappling/armour-defeat. Head + weight cannot separate these; balance can. It is the "how the mass is distributed along the weapon" dimension that turns two same-head/same-weight weapons into different fights.

---

## §3 — The roster as axis-vectors (historical infill)

Live engine weapons (✓ = instantiated in `combatant.py`) plus the `weapon_axes_v2` expansions that are *expressible but not yet instantiated* (○ = content call, §5). `bal` = `pob_frac`; `len` = `head_len`+`grip_len`.

| Weapon | head | bal | band | len | grip | wt | Best-fit historical | Tradition depth (mapping) |
|---|---|---|---|---|---|---|---|---|
| ✓ Rapier | point | .10 | hilt | 3.8 long | 1H +offhand | light | Italian/Spanish rapier | 2–3 (regional) |
| ○ Estoc / tuck | point | — | — | long | 1H/2H | light | anti-armour needle | (new) |
| ✓ Arming sword | cut-thrust | .12 | hilt | 3.2 med | 1H +offhand | light | period workhorse | (home for the straddle) |
| ○ Sidesword | cut-thrust | — | — | long | 1H +offhand | light | civilian companion | (new) |
| ✓ Longsword | cut-thrust | .14 | hilt | 4.4 long | 2H | heavy | German/Italian longsword | 5–6 (universal) |
| ✓ Greatsword | straight-cut | .22 | neutral | 5.4 polearm | 2H | heavy | *Zweihänder* / ōdachi-cut | (new) |
| ○ Messer / falchion | straight-cut | — | — | long | 1H +offhand | light | *Messer* | (new) |
| ✓ Sabre | curved-cut | .18 | neutral | 3.3 med | 1H +offhand | light | szabla/talwar/dao/katana | 6 (universal) |
| ○ Curved 2-hander (ōdachi/wodao) | curved-cut | — | — | polearm | 2H | heavy | ōdachi / wodao | (home for the straddle) |
| ✓ Dagger / short sword | cut-thrust | .25 | neutral | 1.1 short | 1H +offhand | light | Fiore/German dagger | 5–6 |
| ✓ Paired short | cut-thrust | .22 | neutral | 1.9 short | 1H ×2 | light | FMA *doble baston* | 3 |
| ✓ Spear | point | .42 | head-heavy | 6.7 polearm | 2H (1H+shield var) | light | *qiang*/*yari*/lance | **7–8 (richest)** |
| ✓ Staff | blunt | .05 | hilt | 5.6 polearm | 2H | light | *gùn*/*bō*/short-staff | 6 |
| ✓ Mace | blunt | .60 | head-heavy | 2.5 med | 1H | heavy | levy mace | 3 (object common, art thin) |
| ✓ Poleaxe / war-hammer | blunt | .45 | head-heavy | 4.4 long | 2H | heavy | *azza* / poleaxe corpus | 3 (technical) |
| ✓ Longsword (half-sword form) | point | .12 | hilt | (short) | 2H, blade-grip | heavy | *kurzes Schwert* | (grip-state, not a weapon) |

**Shape of the census (carried from the mapping, not waved away):** universals = spear, sabre, staff, longsword; regional/niche = rapier, paired-short, heavy-blunt. **Documented gap = short-blunt** (shillelagh/canne/tonfa) — the mace partly fills it; a dedicated short-blunt weapon is your call (§5). **Folklore the research red-flags** (do not encode as fact): a continuous bare-mace combat art, the field flail, "Kali" as one mother-art, Bodhidharma/Shaolin, the *gada* "2,000-year lineage."

---

## §4 — The weapon↔tradition link: a two-layer class system

F2 asks for "more classes **or** class specialization" and "≥2 weapon-traditions that directly inform how a weapon of a given type is used." The framework answers with **specialization**, because it is more expressive *and* more NERS-Elegant than flat class proliferation (the synthesis already showed 8+6 coexisting fails E):

**Layer 1 — Cognitive base classes** *(weapon-agnostic — how you read and select).* The six native traditions from `martial_traditions_synthesis`: **Constraint · Tempo-read · Intent-seize · Flow · Root · Reach.** These are σ-leverage biases over the substrate channels (read-channel, tempo, bind-leverage, facing) — *how a fighter thinks*, independent of what they hold.

**Layer 2 — Weapon-traditions** *(NEW — keyed on `head` — how a weapon-TYPE is fought).* These are the F2 "≥2 weapon-traditions." Each is a bundle of biases that activate for a head-class and inform that class's signature play. Minimum two; four proposed to cover the head-space:

| Weapon-tradition | Head-class it informs | What it does to those weapons | Historical grounding |
|---|---|---|---|
| **Point-line** *(min set)* | point (rapier/estoc/spear) | the lunge (drive off rear leg), line-control / opposition (every offence carries embedded defence), tempo-thrust, *cavazione* disengage; rewards measure + facing | Italian rapier (Capoferro/Fabris/Giganti) · Spanish *destreza* (*atajo*, the *círculo*) · Chinese *qiang* (*lan/na/zha*) |
| **Bind-leverage** *(min set)* | cut-and-thrust / straight-cut (longsword/arming/messer/greatsword) | the bind, *Winden*, *Stark/Schwach* leverage (2H Strength δσ), half-sword re-vector for armour, pommel-strike; rewards the in-bind state | German Liechtenauer (the tactile/bind tradition) |
| **Draw-flow** *(optional)* | curved-cut (sabre/curved-2H) | draw-cut on the pass, the moulinet, fast follow-cuts → tempo/flow, paired-weapon weaving; rewards recovery + sustained tempo | sabre schools (szabla/Mamluk/talwar) · Japanese kenjutsu · Filipino flow (*sinawali*) |
| **Haft-percussion** *(optional)* | blunt (mace/poleaxe/staff) | crush, half-haft grip, armour-defeat / *Mordstreich*, the grappling-heavy clinch; rewards Strength + the head-heavy balance band | European poleaxe corpus (*Le Jeu de la Hache*, Talhoffer, Mair) |

**The build space = base × weapon-tradition.** A character picks a cognitive base (how they think) **and** a weapon-tradition (the weapon-family they've trained), and the two compose:
- *Tempo-read + Point-line* → a counter-thrust fencer who stop-hits into the lunge.
- *Root + Haft-percussion* → an armoured poleaxe-breaker who wins the clinch.
- *Intent-seize + Draw-flow* → a sabreur who reads the opening before the draw-cut.
- *Constraint + Bind-leverage* → walks the angle into the bind, then wins on *Stark/Schwach*.

This is "specialization": ~6 bases × 2–4 weapon-traditions ≫ the expressiveness of 6 flat classes, at a fraction of the Elegance cost of listing all combinations as separate classes.

**Critical constraint (armature §1.1 — modulate, never unlock):** a weapon-tradition **does not gate** what a character may wield. Any fighter can pick up any weapon. The weapon-tradition only tilts *how well they exploit that weapon-type's axes* — a Bind-leverage fighter with a rapier is competent but off-specialty; the rapier's point-line potential goes under-used. This keeps the system Robust (no hard class-locks) and the choice meaningful (specialization, not restriction).

---

## §5 — What remains yours (project-owner contract)

1. **D-δ — in-world naming & cultures** *(creative layer — yours alone).* Every label above is a historical/mechanical archetype. What the Valorian weapons are called, which cultures carry which weapon-tradition, and any essence/metaphysics coupling are your decisions. This doc provides grounded structure + lore *hooks* only.
2. **Which expandable weapons to instantiate** (○ rows — estoc, sidesword, greatsword, messer, curved-2H, the mace/poleaxe split): a content call.
3. **Ratify the balance axis** — consuming `pob_frac`, with the band thresholds (.15/.35) and the per-weapon `pob_frac` values (currently inherited engine data, tunable).
4. **D-β — base-class count / specialization depth**: six bases is the proposal; weapon-traditions can be 2 (minimum) to 4 (full head-coverage).
5. **D-γ — the `grade='V'` amendment** still governs any new ability lever a weapon-tradition introduces (bottom-up channel + top-down convergent-universal, NERS-gated).
6. **Short-blunt** weapon class — add beyond the mace, or leave to the mace? (documented thin gap).

---

## §6 — How this couples to the other J-33 rulings

- **F5 (wounds):** the balance axis consumes `pob_frac` → **don't revert** the F5 `mass`/`pob_frac` data; F2 gives `pob_frac` a job and F7 gives `mass` one. The dead-data finding closes by consumption.
- **F7 (damage cap):** `mass` (weight axis) is the natural input to a Strength-gated cap — head-heavy + high-mass + high-Strength is the legitimate hard-hit path; the cap reads `mass` × Strength.
- **F4 (σ-leverage):** every weapon-tradition bias is a σ-leverage tilt (the mapping already expresses traditions as biases across the σ channels), so the weapon-tradition layer rides the corrected σ-engine — no separate resolution path.
- **F1 (grid):** the **length** axis sets weapon reach-TN = how many grid squares a weapon threatens; the Spanish/geometric content in Point-line maps to the facing→FoV channel — the weapon-tradition layer is also what informs grid positioning and facing exploitation.

---

## Citations
- `designs/scene/combat_engine_v1/combatant.py` — live weapon vectors (`head`, `hands`, `reach`, `wt`, `mass`, `pob_frac`, `head_len`/`grip_len`, `clinch`, `percussion`, guard primitives), the modulate-not-unlock `grip` state.
- `designs/audit/2026-05-29-combat-armature/weapon_axes_v2.md` — the six-axis substrate, the head refinement, the 15-weapon reclassification, the point-vs-armour table extension.
- `designs/audit/2026-05-29-combat-armature/martial_traditions_mapping.md` — the weapon census, per-weapon tradition-at-depth counts, the seven-axes-per-tradition mapping, the folklore red-flags.
- `designs/audit/2026-05-29-combat-armature/martial_traditions_synthesis.md` — the six cognitive-mode base classes, the `grade='V'` amendment, the armature §1.1 modulate-not-unlock principle.
- `designs/audit/2026-06-09-personal-combat-comprehensive/comprehensive_analysis_personal_combat.md` — F2 (tradition imbalance / dead levers) and F5 (dead `mass`/`pob_frac`) findings.

`[CONFIDENCE: high on the taxonomy structure and the weapon-vector grounding (read from live `combatant.py`); high on historical infill (the mapping's full-read corpus); medium on the exact `pob_frac` band thresholds (.15/.35 are my proposal over inherited values — tunable).]`
`[ASSUMPTION: `pob_frac` semantics = head-heaviness/forward-mass concentration (low = hilt-balanced, high = head-heavy) — basis: the value ordering (staff .05, rapier .10 … spear .42, mace .60) matches that reading; flag if the field means something else in `geometry.py`'s consumption that I haven't traced.]`
`[Coordinate-don't-claim: this is a Class-C proposal; D-δ naming and the structural ratifications stay yours; the martial-traditions base-class layer is the parallel-owned synthesis's, extended here, not overwritten.]`
