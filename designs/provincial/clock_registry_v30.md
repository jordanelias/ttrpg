<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: clock_registry_v30_infill.md -->

<!-- v30 baseline — renamed from designs/systems/clock_registry.md on 2026-04-13 -->
# Valoria Clock & Track Registry
## Created: 2026-04-08 | Updated: 2026-04-26 (staleness report refresh — ED-793 through ED-796) | Status: CANONICAL
## Single source of truth for all clocks, tracks, and counters.
## Cross-references to authoritative source for each track's rules.

---

## Shared Clocks (All Modes)

| Clock | Range | Start | Direction | Source |
|-------|-------|-------|-----------|--------|
| Mending Stability (MS) | 0–100 | 72 | ↓ (decay) | params_threadwork.md §MS. Videogame-only start value. |
| Church Influence (CI) | 0–100 | 28 | ↑ | conviction_track_v30.md §3 (generation), ci_political_v30.md (political effects) |
| Institutional Pressure (IP) | 0–100 | 20 | ↑ | peninsular_strain_v30.md §4.4, params_board_game.md §IP [PROVISIONAL: ED-793 — start value 20 per staleness report item 3; verify against params_bg_core] |
| Peninsular Strain | 0–10 | 0 | ↑ (bad) | peninsular_strain_v30.md §4. Replaces Parliament Integrity (PP-403 repealed). |

## Faction-Specific Tracks (BG/Hybrid)

Progress tracks (0-base; 0 = not yet developed):

| Track | Owner | Range | Start | Source |
|-------|-------|-------|-------|--------|
| Altonian Ecclesiastical Accord (AER) | Church/Hafenmark | 0–5 | 0 | victory_architecture_v1.md §AEA |
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
| Composure | 7–13 | Presence + 6 | params_contest.md §Composure |
| Concentration | 2–14 | Focus + Recall | params_contest.md §Concentration |
| Health | 7–13 | Endurance + 6 | params_core.md |
| Wounds | 0–max | 0 (accumulates) | params_combat.md §Wounds. Max = floor(End/2)+1. |
| Stamina | min 2 | Endurance + 1 (History STRUCK per PP-611) | params_combat.md §Stamina |
| Momentum | 0–4 | 0 | params_core.md §Momentum |
| Knot Count | 0–floor(Bonds/2)+1 | 0 | fieldwork_v30.md §5.6a (PP-632). Requires Bonds ≥ 5 to form first Knot. |

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

