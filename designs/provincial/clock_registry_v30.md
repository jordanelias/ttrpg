<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: clock_registry_v30_infill.md -->

<!-- v30 baseline — renamed from designs/systems/clock_registry.md on 2026-04-13 -->
# Valoria Clock & Track Registry
## Created: 2026-04-08 | Updated: 2026-06-24 (contest-track sync — Persuasion Track + Obligation clocks registered; Composure/Concentration/Health/Stamina formulas synced to derived_stats §14.1; ED-939, docket J-31) | Status: CANONICAL
## Single source of truth for all clocks, tracks, and counters.
## Cross-references to authoritative source for each track's rules.

---

## Shared Clocks (All Modes)

| Clock | Range | Start | Direction | Source |
|-------|-------|-------|-----------|--------|
| Mending Stability (MS) | 0–100 | 60 | ↓ (decay) | params/threadwork.md §RS Track. Videogame start = 60 per OWN-1/2 (Jordan passC, net-decays); resolves 60-vs-72 → 60 (was BG-default 72; videogame uses the TTRPG-default 60). Lore substrate-integrity trajectory still derives 72 at 245 AG — ms_trajectory_v1 reconciliation pending Jordan (creative-layer). |
| Church Influence (CI) | 0–100 | 28 | ↑ | conviction_track_v30.md §3 (generation), ci_political_v30.md (political effects) |
| Institutional Pressure (IP) | 0–100 | 20 | ↑ | peninsular_strain_v30.md §4.4, params_board_game.md §IP [PROVISIONAL: ED-793 — start value 20 per staleness report item 3; verify against params_bg_core] |
| Turmoil | 0–10 | 0 | ↑ (bad) | peninsular_strain_v30.md §4. Replaces Parliament Integrity (PP-403 repealed). |

## Faction-Specific Tracks (BG/Hybrid)

Progress tracks (0-base; 0 = not yet developed):

| Track | Owner | Range | Start | Source |
|-------|-------|-------|-------|--------|
| Torben Loyalty | Crown → Löwenritter | 0–7 | 3 | params_board_game.md §Torben (PP-498) |
| Elske Loyalty | Crown | 0–7 | 4 | params_board_game.md §Elske |
| Löwenritter Autonomy | Crown-Löwenritter (public) | Loyal/Restless/Autonomous/Split | Loyal | conflict_architecture_proposal §Graduated Autonomy |
| Popular Will (PW) | Shared (Hybrid only) | 0–5 | 0 | params_board_game.md §RM Founding [PROVISIONAL: ED-795 — staleness report says STRUCK per canonical_definitive_r2; verify] |
| Warden Cooperation (WC) | Shared | 0–3 | 0 | victory_architecture_v1.md §6 |
| Warden Recognition (WR) | Varfell | 0–4 | 0 | victory_architecture_v1.md §6 |
| Intel Advancement Counter | Varfell | 0–3 (resets to 0 at 4 → Intel +1) | 0 | params_board_game.md §Varfell [PROVISIONAL: ED-794 — staleness report says STRUCK per canonical_definitive_r2; verify] |

## Faction Stats (All Factions)

Stats: 1–7 scale, floor 1. Exception: Stability floor 0 in BG (0 = faction eliminated).

| Stat | Range | Source |
|------|-------|--------|
| Mandate | 0–7 (0 = subjugated) | params_factions.md §Faction Stats |
| Influence | 1–7 (BG: floor 1) | params_factions.md §Faction Stats |
| Wealth | 1–7 (BG: floor 1) | params_factions.md §Faction Stats |
| Military | 1–7 (BG: floor 1) | params_factions.md §Faction Stats |
| Stability | 0–7 (BG: 0 = eliminated) | params_factions.md §Faction Stats |
| Intelligence | 1–7 (BG: floor 1) | params_board_game.md §Varfell Intel [PROVISIONAL: ED-796 — staleness report says STRUCK, replaced by fieldwork Investigation + VTM; verify] |

Reputation and Standing (oscillating, BG):

| Track | Range | Source |
|-------|-------|--------|
| Reputation | 0–5 | bg_v05 §Standing (P-14) |
| Standing | 0–5 | bg_v05 §Standing (P-15) |

## Per-Territory Tracks (BG/Hybrid)

| Track | Range | Start | Source |
|-------|-------|-------|--------|
| Accord | 0–3 | Varies (§2.1) | peninsular_strain_v30.md §2. 3=Aligned, 2=Compliant, 1=Restive, 0=Revolt-eligible. |
| Piety Track (PT) | 0–5 | Varies by territory | victory_architecture_v1.md §2. Oscillating: 0 = Restoration pole, 5 = Piety pole. |
| Fort Level | 0–4 | Per geography_v30.md | geography_v30.md |
| Prosperity | 1–7 | Varies (see Territory Table) | params_board_game.md §Territory Table |
| Guild Favour | 0–7 | Varies | params_factions.md §Guilds |
| Church Attention Pool (AP) | 0–10 per territory | 0 | params_board_game.md §Church Inquisitor. First Inquisitor at AP ≥ 3; second at AP ≥ 6. |

## Personal Tracks (TTRPG/Hybrid)

| Track | Range | Start | Source |
|-------|-------|-------|--------|
| Coherence | 0–10 | 10 | params_threadwork.md §Coherence |
| Certainty | 0–5 | Varies by background (see params_core.md) | params_core.md §Certainty. Oscillating: 5 = Solmund orthodoxy, 0 = Thread acceptance. |
| Thread Sensitivity (TS) | 0–100 (hard cap) | Varies (0 for non-practitioners) | params_threadwork.md §TS |
| Composure | 3–21 | Charisma × 3 | derived_stats_v30.md §5.1 / §14.1 |
| Concentration | 5–35 | (3×Focus)+(2×Spirit) | derived_stats_v30.md §5.2 / §14.1 (ED-902) |
| Health | 13–55 | (End+6) × (MW+1), MW cap 3 | derived_stats_v30.md §4.1 / §14.1 |
| Wounds | 0–max | 0 (accumulates) | params_combat.md §Wounds. Max = floor(End/2)+1. |
| Stamina | 5–47 | (3×End)+(2×Spirit) | derived_stats_v30.md §4.2 / §14.1 |
| Momentum | 0–4 | 0 | params_core.md §Momentum |
| Knot Count | 0–floor(Bonds/2)+1 | 0 | fieldwork_v30.md §5.6a (PP-632). Requires Bonds ≥ 5 to form first Knot. |

## Contest Clocks & Tracks (TTRPG/Hybrid)

Per-contest and contest-generated trackers (social_contest_v30.md). Per-character contest *resources* (Composure, Concentration) are in Personal Tracks above.

| Track | Range | Start | Scope | Source |
|-------|-------|-------|-------|--------|
| Persuasion Track | 0–10 | GM-set (typical 5) | Per-contest | social_contest_v30.md §2 (setup) / §6 (resolution). A wins ≥7, B wins ≤3, compromise 4–6; Total Victory ≥9 / ≤1. |

**Obligation clocks (contest-generated).** Binding cross-season commitments produced by a Decisive Formal/Grand Contest win (social_contest_v30.md §6.1). Each Obligation is tracked as a clock carrying: **source contest** (which proceeding + season produced it), **parties** (the bound losing side and the right-holding winning side), **commitment** (the specific, achievable, verifiable thing that must be done or not done), **duration in seasons** (Formal 2 / Grand 4-or-until-named-condition / Royal Audience 2 / Church Tribunal until-revoked), and **violation trigger** (what constitutes breach and fires the §6.1 consequences). GM advisory: cap ~3 active for tracking tractability (ED-619). Wager Obligations (future-conditional; Grand + Projection + Consequence) and their edge cases per §6.1.1 (ED-778); settlement-targeted Obligations per §6.1 / settlement_bridge_unification C-08. [ED-939, docket J-31]

## NPC-Specific Tracks

| Track | NPC | Range | Start | Source |
|-------|-----|-------|-------|--------|
| Cardinal Influence | 3 Cardinals | 0–5 each | Varies | params_factions.md §Cardinals |
| Ministry AP-Tokens | Ministry NPC | per-territory | 4 tokens | params_board_game.md §Ministry |

## Fieldwork Tracks (TTRPG/Hybrid/Godot)

| Track | Range | Start | Scope | Source |
|-------|-------|-------|-------|--------|
| Exposure | 0–10+ (vs Cover thresholds) | 0 | Per-character, per-territory, per-season | fieldwork_v30.md §6 |
| Cover (derived) | 2–14 | Cognition + History | Per-character | fieldwork_v30.md §6.1 |
| Evidence Track | 0–threshold (3/5/8) | 0 | Per-investigation | fieldwork_v30.md §4.1 |
| Disposition | −4 to floor(Bonds/2)+1 | Faction-indexed | Per-NPC per-PC | fieldwork_v30.md §5.1 (PP-632) |

## Cooldown/Duration Tracks

| Track | Range | Source |
|-------|-------|--------|
| Thread Debt | per-token | params_board_game.md §Thread Debt |
| Casus Belli | per-faction | params_board_game.md §Casus Belli |

---

*Registry maintained by valoria-orchestrator. Update in same commit as any clock/track creation or modification.*

## Player Tracks (Throughline T2, T7)

| Track | Range | Start | Source |
|-------|-------|-------|--------|
| Resources | 0–5 | Varies by background (1–3) | player_agency_v30 §9 |

## Settlement Tracks (Throughlines T1, T7)

| Track | Range | Start | Source |
|-------|-------|-------|--------|
| Settlement Prosperity | 0–5 | Per settlement registry | settlement_layer_v30 §1.3, §2.1 |
| Settlement Defense | 0–5 | Per settlement registry | settlement_layer_v30 §1.3, §2.1 |
| Settlement Order | 0–5 | Per settlement registry | settlement_layer_v30 §1.3, §2.1 |
| Local Actor Disposition | −3 to +5 | +1 toward governor, 0 others | settlement_layer_v30 §4.5 |
| Guild Favor (per settlement) | 1–7 | 3 (Guild-managed) / 1 (other) | player_agency_v30 §9 (T2) |


### Settlement Derived Values (derived_stats_v30 §4, AUD-CK-01 resolved)

| Track | Range | Derivation | Source | Direction |
|-------|-------|-----------|--------|-----------|
| Local Economy | 0–250 | Prosperity × 50 | settlement_layer_v30 §1.3 | Higher = more gold income |
| Garrison Strength | 0–250 | Defense × 20 + Fort Level × 30 | settlement_layer_v30 §1.3 | Higher = harder to attack |
| Public Order | 0–100 | Order × 20 | settlement_layer_v30 §1.3 | 0 = riot events fire |

