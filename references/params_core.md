<!-- version: v0.14-AUD1-R2 | sources: stage1_core_engine.md | last_updated: 2026-04-04 -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->
<!-- PATCHES APPLIED: PP-164, PP-255 (Momentum between-scene carry; RS baseline decay −1/year) -->
<!-- PP-247 (Combat Pool formula corrected to match stage1 §2.3/§3.4: Agi + hist_pts + 3) -->
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
| 10 | +1 success + roll one bonus die (chains indefinitely) |

Net successes = total successes minus total 1s (including bonus dice results). May be negative.
Note: expected value of face-10 under chain rule ≈ +1.43 net at TN7 (geometric series). Higher than "+2" model for large pools.

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

## Degrees of Success
| Degree | Condition |
|--------|-----------|
| Overwhelming | Net ≥ 2× Ob AND net ≥ 3 (+1 Momentum) |
| Success | Net ≥ Ob |
| Partial | Net > 0 but < Ob |
| Failure | Net ≤ 0 |

Overwhelming requires a minimum of 3 net successes regardless of Ob. (PP-232)
Ob 20 exception: Overwhelming unavailable. Partial requires net ≥ 10.


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

## RS Baseline Decay (PP-255)
Rendering Stability (RS) loses **−1 per in-game year** from baseline drift alone (confirmed bg_v05 Part Seven precedent analysis). This applies across all modes:
- TTRPG: −1 RS per 4-season year, applied at Year-End Accounting.
- Board Game: −1 RS per Year-End step.
- Hybrid: same as TTRPG.
Thread operations accelerate this. Restoration sources can offset but not reverse baseline decay.
RS floor: 0 (Rupture). RS ceiling: 100.


## Pool Minimum
No penalty may reduce a pool below 1D. Ob penalties still apply at 1D.

## Expected Value (per die)
| TN | E[net] per die |
|----|---------------|
| 6 | 0.40 |
| 7 | 0.30 |
| 8 | 0.20 |

## Quick Reference — P(≥N net), TN 7
| Pool | E[Net] | P(≥1) | P(≥2) | P(≥3) |
|------|--------|-------|-------|-------|
| 4D | 1.3 | ~80% | ~50% | ~25% |
| 6D | 2.0 | ~92% | ~70% | ~45% |
| 8D | 2.6 | ~97% | ~82% | ~60% |
| 10D | 3.3 | ~99% | ~90% | ~73% |
| 12D | 4.0 | ~99% | ~95% | ~83% |

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

**Recall (Rec):** Knowledge, experience, retention. Sets the per-History point cap — a History can never hold more points than the character's Recall score.
**Focus (Foc):** Concentration, discipline, precision under pressure. Governs Thread contact duration: Contact Rounds = Focus score (range 1–7).

## Derived Scores

| Score | Formula | Range | Notes |
|-------|---------|-------|-------|
| Health | Endurance + 6 | 7–13 | Damage buffer before Wounds. Wound threshold fires every (End+6) damage received; Health resets to full on each Wound. (PP-248) |
| Stamina | Endurance + 1 | min 2 | Combat resource. Floor 2. Cannot wear armour that would reduce Stamina to 1 or below. (PP-248) |
| Composure | Charisma + 6 | 7–13 | Social damage buffer before Rattled. Parallels Health = Endurance + 6. (PP-234, ED-127 resolved) |
| Combat Pool | Agility + weapon proficiency History (points + 3) | Variable (min 5) | Split Offence/Defence each round. (PP-247) |
| Contact Rounds | Focus | 1–7 | Max rounds maintaining Thread contact (practitioners only) |
| Certainty | 10 (starting); countdown to 0 | 0–10 | Epistemological confidence in consensus reality. See PP-289 section below. |
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


## Certainty Track (PP-289)
Range 0–10. Starting value: 10. Counts down toward 0.
Loss triggers: Coherence 0 event (−1), sustained Southernmost exposure >3 scenes (−1/scene), catastrophic ontological revelation (−2).
At Certainty 0: character cannot distinguish Thread substrate from consensus reality. GM takes partial narrative control. Treated as incapacitated for social/Thread purposes.
Recovery: +1 Certainty per long rest outside Southernmost with no Thread operations.
Spirit is unrelated to Certainty. Certainty ≠ Coherence (Coherence = personal rendering integrity; Certainty = epistemological grounding).

## Reach Terminology (PP-290) — replaces Close zone / Far zone
- Short Reach: melee contact (≤ 1 metre). Applies to most melee weapons.
- Long Reach: extended melee (polearms, spears; ≤ 3 metres).
- Ranged: everything beyond Long Reach. Ranged weapons are Ranged until GM rules terrain or cover changes effective distance.
'Close zone' and 'Far zone' are struck from all design documents.

## Net Successes Floor — Correction (PP-246 note)
Net successes CAN be negative (per stage1 §1.1). Prior "Floor: 0" was an error.
Negative net successes contribute to Failure degree only; they do not compound penalties further.

