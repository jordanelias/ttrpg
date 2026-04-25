<!-- version: v1.0 | source: designs/ttrpg/factions_ttrpg_v30.md | last_updated: 2026-04-13 -->
<!-- PATCHES APPLIED: SIM-FAC verification pass 2026-04-13. No mechanical changes. -->
<!-- SIM STATUS: VERIFIED — domain actions, unique actions, ethical framework modifiers -->

# params_factions_ttrpg.md — TTRPG Faction Mechanics

## Faction Stats — 1-7 Scale
| Stat | Represents |
|------|-----------|
| Mandate | Public legitimacy and popular support |
| Influence | Political reach and diplomatic weight |
| Wealth | Economic capacity |
| Military | Armed force and unit capacity |
| Intel | Intelligence network and covert operations |
| Stability | Internal cohesion and crisis resistance |

## Starting Values (game start, 45 AG)
| Faction | Mandate | Influence | Wealth | Military | Intel | Stability |
|---------|---------|----------|--------|----------|-------|-----------|
| Crown | 5 | 5 | 4 | 4 | — | 4 |
| Church | 5 | 6 | 5 | 4 | — | 5 |
| Hafenmark | 4 | 4 | 5 | 3 | — | 4 |
| Varfell | 4 | 4 | 4 | 4 | — | 4 |
| Guilds | 3 | 4 | 6 | 2 | — | 5 |
| ~~Niflhel~~ STRUCK | — | — | — | — | — | — |
| Revolution | — | 3 | — | — | — | 3 |
| Löwenritter | — | 3 | — | 5 | 3 | 5 |

> **Niflhel STRUCK** (per CR-STRIKE-2026-04-19 / conflict_architecture_proposal §Niflhel Dissolution / ED-764). Functions distributed to settlement-level phenomena: black markets (Wealth-bearing); intelligence brokers (Intel-bearing single NPCs); Thread exploitation sites (settlement-Order-bearing). No faction-level Niflhel stat sheet. Settlement-level brokers each have local Intel ≤ 4.

Partial sheets: Revolution (Influence, Stability, Intel only). [Niflhel removed per ED-764.]
Löwenritter (no Mandate, no Wealth). Guilds NPC-only: no deviation mechanic.

## Domain Action Resolution
Pool = character's relevant attribute + faction's relevant stat (if PC holds leadership).
NPC factions: Pool = faction's relevant stat.
Ob = target faction's relevant stat (1–7 scale, no division).
Seasonal cap: ±2 per stat per season at accounting. Minimum Ob: 1 (PP-285).

### Ethical Framework Modifiers
| Alignment | Ob Modifier |
|-----------|------------|
| Aligned with faction framework | −1 Ob |
| Neutral / unrelated | ±0 |
| Opposed to framework | +1 Ob |
| Church revealing Thread truth | +2 Ob |
Min Ob floor: 1 after all modifiers.

## Unique Actions
| Faction | Action | Pool | Ob | Notes |
|---------|--------|------|-----|-------|
| Crown | Royal Decree | Mandate | 2 | 1/season. Consecutive: +1 Ob per season. Cannot target absent stats. |
| Church | Excommunication | Mandate | vs target Mandate (or Ob 2 if non-leader) | Requires Mandate ≥ 3. |
| Hafenmark | Sovereign Authority Doctrine | Mandate | 4 | 1/campaign arc. Heresy Investigation risk. |
| Varfell | Private Collection | Intel | 2 | 1/season. +1 TS on use. TS 14+: triggers Spirit check. |
| Guilds | Economic Leverage | Wealth | vs target Wealth | Requires Guild Favour ≥ 5 in territory. |
| ~~Niflhel Quiet~~ STRUCK | — | — | — | Per ED-764. Settlement-level intelligence-broker NPCs use individual Intel; no faction-level Quiet action exists. |
| Revolution | Community Weaving | Influence | TT ÷ 20 (round up) | Requires practitioner TS 30+. Co-movement fires. |
| Löwenritter | Graduated Autonomy | — | track-state | Replaces Coup Counter (ED-589). Track stages: Loyal → Restless → Autonomous → Split. Per worldbuilding §3 / clock_registry §3. |

## Probability Reference (verified by SIM-FAC-01/02)
| Pool | Ob | P(Success+) | P(Overwhelming) |
|------|----|------------|----------------|
| 5D (Mandate) | 2 | 60% | 23% |
| 6D | 3 | 48% | 8% |
| 4D | 4 | 14% | 0% |
| 5D | 4 | 23% | 0% |
| 5D | 6 | 4% | 0% |

NPC-only equal-stat contest: ~14% success, ~59% partial, ~27% fail (design intent: PC agency matters).

## Stability Check — Seasonal Accounting
| Situation | Ob |
|-----------|-----|
| Quiet season | 1 |
| One active threat | 2 |
| Two concurrent threats | 3 |
| Active attack on Mandate/Wealth | 4 |
| Campaign-level crisis | 5 |
Anti-death-spiral floor: Stability ≤ 2 → treat as Ob 4 regardless of actual pressure.
P(survive, Stab 2 vs Ob 4) ≈ 59%. ~2 seasons at Stab 2 before probable collapse.

## Parliamentary Vote
Pool: relevant faction stat (typically Mandate or Influence).
Ob: opponent's relevant stat.
Format: best of 3 exchanges. First to 2 wins. Ties (neither wins 2): motion fails, TT+1, TC+1.

## Theocracy Counter Generation
Church Mandate ≥ 5: TC +1/season at accounting.
Piety Domain Action (1/season): Mandate pool, Ob 2. Success: TC +1 (stacks with above).
TC seasonal cap: ±5 combined from all sources.
Stability ≤ 4: TC generation pauses.

## ~~Coup Counter (Löwenritter)~~ STRUCK (ED-781 — supersedes per ED-589)

Per `designs/architecture/conflict_architecture_proposal.md §Graduated Löwenritter Autonomy` and `designs/provincial/clock_registry_v30.md L30 Löwenritter Autonomy`, the Coup Counter binary mechanism is replaced by a four-stage progression: **Loyal → Restless → Autonomous → Split** (track-state, not numeric counter). Triggers, Crown effects, and reversibility rules are in `conflict_architecture_proposal.md` L67-L82. Above §59 of this file (Löwenritter Graduated Autonomy entry) is the canonical reference for params lookup. The legacy Coup Counter spec is preserved in `deprecated/` per editorial policy.

Migration note: prior canonical text was "Counter never decrements. At 3: coup fires at next accounting." This is replaced by stage-based progression where stages 1-3 are reversible and only stage 4 (Split) is permanent. References to "Coup Counter" in NPC priority trees (`params/bg/npc_priority_trees.md` L42, L86, L149, L197) refer to the legacy track and should be migrated to "Löwenritter Autonomy stage" in a future cleanup pass.

## Southernmost Awareness (Faction Stat, 0–7 or 0–10 for research factions)
| Faction | Starting Awareness |
|---------|--------------------|
| Crown | 0 |
| Church | 0 |
| Hafenmark | 1 |
| Varfell | 2 |
| Revolution | 3 |
[NAME-PENDING: ED-048] Text holder: floor = 1.

<!-- patch_history: references/params_factions_history.md (to be created) -->
<!-- canonical_sources: references/canonical_sources.yaml -->
