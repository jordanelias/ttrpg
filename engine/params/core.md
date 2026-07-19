<!-- version: v0.14-AUD1-R2 | sources: stage1_core_engine.md | last_updated: 2026-04-04 -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->
<!-- PATCHES APPLIED (canonical): PP-164, PP-232, PP-234, PP-243, PP-246–248, PP-255, PP-261, PP-289–290, PP-381, PP-383–386, PP-389, PP-551, PP-553, PP-610–611, PP-615, PP-617, PP-623, PP-627, PP-628, PP-629, PP-632, PP-633 -->
<!-- PP-247 (historical, superseded by ED-901/ED-900/ED-904 — see the Combat Pool row below for the live formula and citation; do not read this line as current) -->
<!-- PP-248 (Stamina formula corrected to End+1 per stage1 §3.9; Health row clarified) -->
<!-- PP-232 (Ob cap raised to 20; Overwhelming floor 3; Health formula revised; Stamina floor 2; armour wield constraint) -->

# params_core.md — Core Dice Engine

## Die Rule (d10)
<!-- PP-246: Corrected to match stage1_core_engine.md §1.1 canonical source. Prior "+2 no extra die" was a fidelity error. -->
| Face | Effect |
|------|--------|
| 1 | −1 success |
| 2–6 | 0 |
| 7–9 | +1 success |
| 10 | +2 successes |

Net successes = total successes minus total 1s (including bonus dice results). May be negative.

**Canonical:** no chain rule. Face 10 = +2 successes flat (PP-246 confirmed; valoria_master_document §1.1 explicit). Prior note about geometric chain (≈ +1.43 EV under chain) is **NON-CANONICAL** and struck.

## TN Values
| Mode | TN | When |
|------|----|------|
| Controlled | 6 | Prepared, unhurried, favourable |
| Standard | 7 | Default |
| Desperate | 8 | Duress, exhaustion, existential threat |

Thread operations: TN 7 standard; TN 8 for Locking, Dissolution, and Past-Oriented Pulling.

## Obstacle Scale
| Ob | Difficulty |
|----|-----------|
| 1 | Routine |
| 2 | Moderate |
| 3 | Difficult |
| 5 | Entrenched |
| 8 | Structural |
| 20 | Foundational (cap; no stacking above 20) |

Ob minimum: 1. No modifier may reduce Ob below 1. (PP-232)

**Continuous axis (videogame mode).** The obstacle is a continuous axis; the rows above are reference points, not a quantization. In continuous (Godot) mode fractional Ob is valid (see §Continuous Engine — weapon condition, cover, terrain) and a fractional Ob between two rows is a real intermediate difficulty: the continuous-mode success probability is strictly monotonic in Ob, so e.g. Ob 1.4 and Ob 1.6 give different odds. Integer Ob applies only in discrete/TTRPG mode, where `net` is an integer sum and a fractional Ob collapses to the next integer up (`Ob 1.4 ≡ 1.6 ≡ 2`).

## Degrees of Success
| Degree | Condition |
|--------|-----------|
| Overwhelming | Net ≥ 2× Ob AND net ≥ 3 (+1 Momentum) |
| Success | Net ≥ Ob |
| Partial | Net > 0 but < Ob |
| Failure | Net ≤ 0 |

Overwhelming requires a minimum of 3 net successes regardless of Ob. (PP-232)
Ob 20 exception: Overwhelming unavailable. Partial requires net ≥ 10.


## Continuous Engine (Decision E, 2026-05-15)

The engine MAY be implemented two ways with statistically equivalent outputs:

**Discrete (legacy / TTRPG-mode):** Roll N d10s. Count faces per canonical rule. Net = sum.

**Continuous (videogame-mode / canonical for Godot implementation):** Sample `net ~ Normal(μ·N, σ·√N)` where μ and σ are per-die statistics for the active TN (see EV table above).

**Equivalence validated:** Phase 5 sim 2026-05-15 (tests/sim/phase5_continuous_engine_2026-05-15.py) — max deviation 0.029 in mean, 0.022 in std at pool sizes 5-17. Both engines produce statistically identical outputs.

**Continuous-engine enables:**
- Fractional Ob (e.g., weapon condition +0.25 Ob)
- Fractional TN (PP-717 Fiore half-step TN already canonical for combat)
- Continuous degree resolution (outcome magnitude = net − Ob, as gauge)
- Linear extension to fractional modifiers (cover quality, terrain, environment)

**Continuous degree thresholds (videogame implementation):** discrete `Success (net ≥ Ob)`, `Overwhelming (net ≥ 2·Ob)`, `Partial (net > 0 < Ob)` map onto continuous magnitude `net − Ob` directly. UI surfaces magnitude as gauge.

**Adoption note:** discrete engine remains canonical for TTRPG-mode play; continuous engine is canonical for Godot implementation. They are interchangeable specifications of the same underlying probability distribution.

**Validation scope (WS-D-1, ED-836).** Phase 5 sim demonstrated distribution equivalence at combat-system parameters (pool 5-17D, TN 7). The result is mathematically system-agnostic (CLT applies to any d10 dice pool sum), so it transfers to social contest, thread operations, fieldwork, mass-combat, and faction systems by construction. System-specific validation sims have not been run; faction-scale (bare 1-7D pools) sits at the small-pool boundary where Normal approximation grows shaky and would benefit from dedicated sanity-check.

**Continuity correction (sub-5D fidelity; ER-2, `engine_replacement_reconciled §2/§5`; landed 2026-06-22).** Below ~5D the raw Normal underestimates `P(success)` versus the discrete engine by 4–32% (it omits the half-integer continuity term the discrete lattice implies at the threshold). The continuous engine therefore resolves against **`net − (Ob − 0.5)`** rather than `net − Ob`: the `−0.5` continuity term restores agreement with the discrete engine to ~1–3% across the whole range (e.g. `0.067` vs `0.070` at 2D, Ob 3). The same half-step applies at each integer degree boundary. Above ~5D the term is negligible. This closes the small-pool boundary flagged in the Validation-scope note above, keeping discrete and continuous modes in agreement on the same action's odds.

## Coherence 0 — NPC Transition (PP-261)
At Coherence 0: character becomes NPC (100% functional, player agency ends). See params_threadwork.md for full rule.
## Momentum
- Range: 0–4
- Gain: Overwhelming success OR Belief achieved
- Spend: 1 Momentum = 1 automatic success (non-Thread rolls only)
- Reset: start of each session

## Momentum Carry Rule (PP-255)
Momentum range: 0–4. Resets to 0 at the **start of each session** (not scene).
**Between-scene carry within a session:** Momentum carries between scenes within the same session. A character who ends Scene 1 with Momentum 2 begins Scene 2 with Momentum 2.
**Hoarding cost:** Momentum cannot be banked across sessions. Any unspent Momentum at session end is lost.

## MS Baseline Decay (PP-255)
Mending Stability (MS) loses **−1 per in-game year** from baseline drift alone (confirmed bg_v05 Part Seven precedent analysis). This applies across all modes:
- TTRPG: −1 MS per 4-season year, applied at Year-End Accounting.
- Board Game: −1 MS per Year-End step.
- Hybrid: same as TTRPG.
Thread operations accelerate this. Restoration sources can offset but not reverse baseline decay.
MS floor: 0 (Rupture). MS ceiling: 100. Starting value by mode: TTRPG default = 60; Board Game default = 72.


## Pool Minimum
No penalty may reduce a pool below 1D. Ob penalties still apply at 1D.

## Expected Value (per die)

Canonical face rule (1 = −1, 2-6 = 0, 7-9 = +1, 10 = +2, no chain). Recalculated 2026-05-15 to fix prior error that treated face 10 as +1.

| TN | E[net] per die | σ² per die | σ per die |
|----|---------------|------------|-----------|
| 6 | 0.50 | 0.65 | 0.806 |
| 7 | 0.40 | 0.64 | 0.800 |
| 8 | 0.30 | 0.61 | 0.781 |

Used by continuous engine to parameterize Normal(μN, σ√N) sampling. See "Continuous Engine" section below.

## Quick Reference — P(≥N net), TN 7

Monte Carlo (N=100k each) under canonical face rule (no chain), 2026-05-15.

| Pool | E[Net] | P(≥1) | P(≥2) | P(≥3) |
|------|--------|-------|-------|-------|
| 4D | 1.60 | ~70% | ~45% | ~22% |
| 6D | 2.40 | ~83% | ~63% | ~40% |
| 8D | 3.20 | ~89% | ~75% | ~57% |
| 10D | 4.00 | ~92% | ~83% | ~68% |
| 12D | 4.80 | ~94% | ~87% | ~76% |

Continuous engine: net ~ Normal(0.4·pool, 0.8·√pool) for TN 7. Sampled distribution matches discrete Monte Carlo to within 0.03 in mean and std at pool sizes 5-17 (Phase 5 validation 2026-05-15).

Full multi-TN tables: references/tn_full_tables.md (generate via dice-model Task 8 if absent).

## Attributes

Range: **1–7** (all attributes). Average human: 3. Creation max: 5 (one attribute only; all others ≤ 4). Advancement max: 7.
Point pool at creation: 31 points across 10 attributes. Minimum 1 per attribute.

| Group | Attributes |
|-------|-----------|
| Physical | Agility (Agi), Endurance (End), Strength (Str) |
| Mental | Cognition (Cog), Recall (Rec), Focus (Foc) |
| Social | Attunement (Att), Bonds (Bon), Charisma (Cha) |
| Metaphysical | Spirit (Spi) |

**Bonds (Bon):** Governs relational *capacity* (ED-912 — Disposition is now a flat **−5..+5**, NOT Bonds-capped): (1) Knot prerequisite = **Bonds ≥ 5** (an explicit gate, no longer a Disposition ceiling); (2) max Knot count = floor(Bonds/2)+1. Bonds 5 = first Knot eligible (at Disposition +5, the Bonded level); Bonds 7 = 3 Close Knots at full capacity. (supersedes PP-632 / PP-684 "ceiling = Bonds")

**Knot Formation (AUD-NPC-01):** Disposition +5 + TS ≥ 30 (either party) + Knot capacity available → Spirit pool (Spirit×2) vs TN 7, Ob 2. Overwhelming: Close Knot + co-movement draw. Success: Distant Knot. Partial: no Knot, 2-season cooldown. Failure: Disposition −1, 4-season cooldown. Non-sensitive (TS < 30 both): Knot impossible. See fieldwork_v30 §5.6a.

**Recall (Rec):** Knowledge, experience, retention. Sets the per-History point cap — a History can never hold more points than the character's Recall score.
**Focus (Foc):** Concentration, discipline, precision under pressure. Governs Thread contact duration: Contact Rounds = Focus score (range 1–7).

## Derived Scores

| Score | Formula | Range | Notes |
|-------|---------|-------|-------|
| Health | (End+6) × (MW+1), MW = min(floor(End/2)+1, 3) | 14–48 (cap MW=3) | Total damage capacity. Non-resetting; each wound subtracts WI=(End+6). **Each wound adds a fractional Ob to the roll — NEVER a −1D pool cut** (Jordan ruling 2026-07-08, ED-PC-0005; reverses PP-716's −1D unification). Combat = ED-1041's bilateral channel (+0.15 Ob attacking / +0.25 Ob defending per wound); non-combat per-pool values are a follow-on calibration, flagged pending (ED-PC-0006). Equipment adds flat Health. **See `designs/scene/derived_stats_v30.md` §4.1 as authoritative.** (PP-716's −1D unification superseded by ED-PC-0005; PP-717 D1 MW cap) |
| Stamina | (3 × Endurance) + (2 × Spirit) | 5–35 | Combat action economy. Variable action costs (standard 5, heavy 8, defensive 3). Armor adds to drain per action. Take a Breath restores (End + History) × 2. (ED-694) |
| Composure | Charisma × 3 | 3–21 | Social damage buffer before Rattled. Strain scaled ×3. Equipment (attire, regalia) adds flat Composure. (ED-694, replaces Cha+6) |
| Combat Pool | max(5, Relevant History + 6) | min 5 | **Agility-INDEPENDENT** resolution pool — ratified 2026-05-29 R1 (ED-901; re-ratified ED-900/904 with combat_engine_v1). Supersedes the struck (Agility × 2) + History + 3 form (PP-615/PP-247 era). Single source: `designs/scene/combat_engine_v1/` (see `references/module_contracts.yaml` personal_combat). ED-1084 propagation. |
| Thread Fatigue | Spirit × 5 (threshold) | 5–35 | Thread action economy. Counts up from 0. Contact breaks at threshold. Variable operation costs (Pulling 5, Locking 7, Dissolution 10). Focus sets max operations per session (Focus − 1). (ED-694, replaces Contact Rounds = Focus) |
| Concentration | (3 × Focus) + (2 × Spirit) | 5–35 | Social-contest and combat attention/composure resource, shared derivation (ED-902 coefficients; ED-901 struck the interim Focus×3 form; ED-933 params propagation). Row added 2026-07-08 (ED-IN-0029 docket, OPT-AV-7) — this table lacked a Concentration row entirely despite the quantity being load-bearing in both contest (`params/contest.md`) and combat (`designs/scene/combat_engine_v1/config.py` `CONC_FOCUS`/`CONC_SPIRIT`). **See `designs/scene/derived_stats_v30.md` §4 as authoritative.** |
| Truth | 5 (starting, varies by background) | 0–5 | Per-character metaphysical stance — **consolidates the former Certainty Track + the character-scale piety / "religious standing" notion** (ED-IN-0075). Solmund orthodoxy (5, *Himmelenger pole*) → Thread-truth acceptance (0, *Edeyja pole*). Numeric is engine-internal — **players see the qualitative band, never the number**. The 13 Convictions are a separate value-frame system (`conviction_taxonomy_v30.md`) and are unchanged. See Truth Track section below. |
| Coherence | 10 (starting); countdown to 0 | 0–10 | Personal rendering legibility |
| Resolve | Spirit | 1–7 | Maximum total Inspiration value |

<!-- patch_history: references/params_core_history.md -->

---
<!-- PP-243 applied 2026-04-04: Momentum auto-success interaction with roll -->

## Momentum Auto-Success Interaction (PP-243)
Momentum auto-successes **add to** (not replace) the dice roll. A 1-result on a die can cancel a Momentum auto-success.

Example: Spend 1 Momentum (1 auto-success) + roll 1D TN 7.
- Die shows 10: net = 1 (auto) + 2 (roll) = 3 → may reach Overwhelming if ≥ 2×Ob AND ≥ 3 net.
- Die shows 7–9: net = 1 (auto) + 1 (roll) = 2 → Success at Ob 1, not Overwhelming (net < 3).
- Die shows 1: net = 1 (auto) − 1 (roll) = 0 → Failure at Ob 1.

Spending 2 Momentum on Ob 1 (2 auto-successes): auto-successes alone reach Ob 1 but cannot satisfy Overwhelming floor (need ≥ 3 net). Must also roll to reach Overwhelming.


## Truth Track (PP-551 — redesigned from PP-289; renamed from the former "Certainty Track" and consolidated with the character-scale piety / "religious standing" notion per ED-IN-0075)
**Definition:** The character's operative metaphysical stance — where they sit on the axis between Solmund orthodoxy and acceptance of Thread cosmology as the true foundation of the rendered world. This subsumes both the former **Certainty** track (cosmological framework) and the vague character-scale **piety / "religious standing"** meter: a character's standing toward Church orthodoxy *is* their Truth band. Both poles are stable states; this is a transformation track, not a deterioration track. The **13 Convictions** (Faith, Order, Reason, … — `conviction_taxonomy_v30.md`) are a **separate, orthogonal value-frame system and are UNCHANGED** by this consolidation — Truth is *what one holds true about reality's foundation*; Convictions are *the values one judges by*.

**Pole exemplars:** the **Edeyja pole** (0 — knows Thread as the metaphysical foundation) ↔ the **Himmelenger pole** (5 — devout Solmund orthodoxy). Naming the poles after canonical exemplars, not after a "more/less true" reading of the number: high Truth = deep orthodoxy (which canon holds to be *sincerely wrong*), low Truth = Thread-truth acceptance.

**Range: 0–5 (oscillating), engine-internal.** 5 = Full Solmund orthodoxy. 0 = Full Thread-truth acceptance. **Players never see the number — only the band label below.**

| Value | Label | Operative belief |
|-------|-------|-----------------|
| 5 | Orthodox *(Himmelenger pole)* | Solmund created the rendered world. Thread phenomena are demonic or heretical. |
| 4 | Faithful | Doctrine is basically correct; Thread phenomena are unusual but explicable within faith. |
| 3 | Questioning | Doctrine shows cracks; Thread experiences are real but not fully explained. |
| 2 | Skeptic | Solmund framework has failed to explain too much; Thread substrate is real. |
| 1 | Transitional | Thread cosmology is the better account; Solmund is a rendering, not the source. |
| 0 | Accepted *(Edeyja pole)* | Thread substrate is the ground of being; Solmund is a human rendering that exceeds it. |

**Who has it:** All player characters. Named NPCs at GM discretion. Factions do not hold Truth.

**Starting value:** Assigned at creation by background. Devout orthodox: 5. Average Valorian: 4. Secular: 3. Post-First Leap practitioner: 2. Thread cosmology adherent: 1.

**Movement toward 0 (Thread acceptance):** Witnessing Thread operation first time in arc (−1); surviving threadcut being contact (−1); completing First Leap (−1, permanent); Coherence 0 event (−1); Southernmost exposure > 2 consecutive scenes (−1); catastrophic revelation (−1, GM-called).

**Movement toward 5 (Solmund reinforcement):** Cardinal absolution (once/arc, +1); sustained orthodox community at Year-End if character present (+1); Overwhelming Church Tribunal victory — defendant/witness who accepts verdict (+1).

**Mechanical effects:**
- Truth 5: +1D in Church/orthodox contexts; first Coherence loss per session nullified (doctrine scaffolds).
- Truth 2–1: −1D in Church/orthodox contexts; Coherence recovery +1 per long rest.
- Truth 0: −2D in Church/orthodox contexts; +1D among Thread-aware communities; Coherence recovery +2 per long rest; TS growth +1 per major Thread encounter (GM-called); arch-heretic classification.

**Church interaction by level:** Truth 5 → Heresy Investigation Ob +2. Truth 2–1 → standard Ob. Truth 0 → Investigation Ob −2; Excommunication automatic on capture.

**Relationships:** Independent of Coherence (operational resource) and Thread Sensitivity (perceptual depth). Can diverge from Beliefs (declared vs confronted). Not tracked in Board Game mode — abstracted into PT dynamics.

Spirit is unrelated to Truth.

## Reach Terminology (PP-290) — replaces Close zone / Far zone
- Short Reach: melee contact (≤ 1 metre). Applies to most melee weapons.
- Long Reach: extended melee (polearms, spears; ≤ 3 metres).
- Ranged: everything beyond Long Reach. Ranged weapons are Ranged until GM rules terrain or cover changes effective distance.
'Close zone' and 'Far zone' are struck from all design documents.

## Pool Floor (all systems)

**Pool floor: 1D.** All dice pools have a minimum of 1D regardless of cumulative penalties. Formula: max(1, base_pool − penalties). Applies to:
- Feint pool reduction in combat (PP-294: pool reduction floor minimum 1D)
- Spent + Rattled combined penalties in Contest (social_contest_v30.md §4 Step 7)
- Stamina-depleted or wound-penalised fieldwork pools
- Any other system that applies subtractive penalties to a pool

Pool floor of 1D does NOT prevent Failure — a 1D roll at TN 7 vs Ob 1 has P(success) ≈ 40%. The floor preserves player agency at the mechanical edge without guaranteeing outcome.

## Net Successes Floor — Correction (PP-246 note)
Net successes CAN be negative (per stage1 §1.1). Prior "Floor: 0" was an error.
Negative net successes contribute to Failure degree only; they do not compound penalties further.

## ED-301 Propagation: TS/Coherence Orthogonality
- TS and Coherence are orthogonal axes. See params_threadwork ED-301 section for full detail.
- Coherence track models layer 2 integrity (unconscious self-rendering). TS measures perceptual depth. Neither implies the other.

## Attribute Roles — Fieldwork (PP-628, from fieldwork_v30.md §2.1)

| Attribute | Fieldwork Role |
|-----------|----------------|
| Cognition (Cog) | Terrain/navigation exploration; physical evidence examination (Examine); Surveil; Concealment pool (Cognition × 2) |
| Recall (Rec) | Lore/research investigation (Research); Reconstruct action |
| Attunement (Att) | Thread-aware exploration (sensing); Witness/informant investigation (Interview); Socializing: Read, Negotiate |
| Spirit (Spi) | Thread-Read (perceptive Leap): (Spirit × 2) + History + TPS. All Thread contact pools. Sincerity Gate check. |
| Endurance (End) | Endurance-based exploration (forced marches, harsh terrain) |
| Bonds (Bon) | Socializing: Connect action |
| Charisma (Cha) | Socializing: Impress, Rumour, Converse |

Cover (derived): Cognition + most relevant History for concealment/tradecraft. Fieldwork Pool: (Primary Attribute × 2) + History bonus (matching Combat Pool and Contest Pool construction per PP-615/PP-234).
