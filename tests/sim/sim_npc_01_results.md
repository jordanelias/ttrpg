# SIM-NPC-01: BG NPC Priority Tree Simulation Results
## Date: 2026-04-13
## Source: designs/systems/npc_behavior_system_v1.md §8
## Method: Python Monte Carlo, 5 seeds × 12 seasons (3 BG years), d10 pool engine
## Seeds: 42, 137, 256, 999, 1701

---

## Executive Summary

The priority tree system produces functional cross-faction interaction with no degenerate cycles. However, three critical balance problems and four moderate issues were identified. The most severe: the Löwenritter coup fires deterministically in 5/5 runs, Crown enters a Mandate death spiral, and Church Framework Drift is unconditionally dominant.

---

## End-State Data (12 seasons, all 5 seeds)

### Clocks
| Seed | TC | RS | IP | PI | Coup | Torben |
|---|---|---|---|---|---|---|
| 42 | 43 | 64 | 32 | 0 | 3 | 4 |
| 137 | 47 | 66 | 32 | 0 | 3 | 4 |
| 256 | 43 | 61 | 32 | 0 | 3 | 4 |
| 999 | 43 | 62 | 32 | 0 | 3 | 4 |
| 1701 | 44 | 64 | 32 | 0 | 3 | 4 |

### Faction Stats (end of S12)
| Faction | M range | I range | W range | Mil range | S range | Eliminated? |
|---|---|---|---|---|---|---|
| Crown | 0 | 5 | 1–3 | 4 | 5–7 | Never |
| Church | 4 | 7 (all) | 5 | 4 | 2–7 | Never |
| Hafenmark | 4 | 7 (all) | 5 | 3 | 1–4 | Never |
| Varfell | 2–4 | 4 | 4 | 4 | 3–7 | Never |
| Guilds | 3 | 4 | 6 | 2 | 5–7 | Never |
| Löwenritter | 3 | 3 | 0 | 5 | 5–7 | Never |
| Ministry | 3 | 4 | 0 | 0 | 1–7 | Never |

---

## Findings

### F-01 (CRITICAL): Crown Mandate Death Spiral
**Observation:** Crown Mandate reaches 0 in 5/5 runs by S12. Royal Decree (P3) fails at Ob 2 roughly 50% of the time, costing Mandate −1 on failure. Each failure reduces the pool for future Decrees, accelerating collapse.

**Root cause:** Crown P3 fires Royal Decree almost every season. The failure cost (Mandate −1) is not gated — it applies to all Decree failures regardless of Mandate level. At Mandate 2, the 2D pool has ~50% chance of net 0 (Failure) at TN 7, triggering another Mandate −1. At Mandate 1, the pool is 1D — almost guaranteed failure.

**Impact:** Crown loses all political legitimacy. Cannot issue Decrees. Cannot defend against Church actions. Cannot maintain Torben Loyalty through political means.

**Proposed patch (PP-NPC-01):** Add to Crown Priority Tree P3: "Do not attempt Royal Decree if Crown Mandate ≤ 2 (insufficient institutional authority to sustain decree legitimacy). At Mandate ≤ 2, Crown defaults to P4 (maintain/govern)." Additionally, Royal Decree failure cost should only apply at Mandate ≥ 3 (the institution absorbs reputational damage; at M ≤ 2 the institution is too weak to lose further legitimacy from a failed attempt).

---

### F-02 (CRITICAL): Löwenritter Coup Is Deterministic
**Observation:** Coup Counter reaches 3 in 5/5 runs. TC≥40 fires reliably because Church passive +1/season pushes TC from 28 to 40 by S12. Crown's only TC-reduction tool (Royal Decree targeting Church Mandate) fails too often (see F-01). Once TC≥40, the Coup Counter increments every season Crown fails to reduce TC.

**Root cause:** The TC≥40 coup trigger fires on Crown inaction, but Crown has no reliable TC-reduction action. Hafenmark Suppress negates the passive +1 but Church Assert (+1) often replaces it. Crown Royal Decree can reduce Church Mandate to slow TC, but the Decree failure cascade (F-01) eliminates this tool.

**Impact:** The coup is a narrative certainty, not an emergent possibility. Players cannot prevent it without PC intervention. This violates the design intent (coup as emergent threat, not predetermined).

**Proposed patch (PP-NPC-02):** Two changes:
1. Crown Priority Tree P2: add "If TC ≥ 35: Crown takes TC-reducing action (Senator Outward to Hafenmark to coordinate Suppress, or direct DA targeting Church Mandate)." This gives Crown earlier awareness of the TC threat.
2. Coup Counter: increment only if TC ≥ 40 AND Crown took no TC-reducing action AND Church actively Asserted this season. Passive TC advance alone should not trigger the counter — it should require active Church aggression going unchallenged.

---

### F-03 (CRITICAL): Church Framework Drift Unconditionally Dominant
**Observation:** Church Influence hits ceiling (7) in 5/5 runs by S4. Framework Drift fires every 2 seasons with no condition except "no external challenge" — and the simulation never challenges Church Influence directly because no faction's priority tree targets Church Influence.

**Root cause:** The drift condition ("no external challenge for 2 consecutive seasons") is too loose. In practice, a "challenge" should mean a DA specifically targeting Church Influence. But Church Influence is never targeted because other factions prioritise TC/Mandate/Military.

**Impact:** Church becomes the dominant social actor in all games without any player action. This is partially intentional (Church institutional momentum) but reaching Influence 7 by S4 is too fast.

**Proposed patch (PP-NPC-03):** Revise Church Framework Drift: "Church Influence +1 only if: (a) no faction targeted Church with any hostile DA this season, AND (b) Church Stability ≥ 4 (institutional confidence requires internal cohesion), AND (c) TC advanced this season (the institutional momentum that drives Influence IS the TC advance — they are the same process). Frequency: per year (not per 2 seasons)." This ties Influence drift to TC progress and internal stability, slowing it from S4-ceiling to approximately S8-S10 ceiling.

---

### F-04 (MODERATE): Varfell P2 Fires Every Season
**Observation:** Varfell always fires Priority 2 (Private Collection) because the Collection is always "available." Per canonical rules (stage6 §8.5), the Collection is once/season — but the priority tree treats "available" as "exists," not "unused this season."

**Proposed patch (PP-NPC-04):** Add state tracking to Varfell Priority Tree: "P2 fires only if Private Collection not used this season. After P2 fires, mark Collection as used. Resets at Accounting. If Collection already used, skip to P3." This aligns the priority tree with the canonical 1/season limit.

---

### F-05 (MODERATE): No Faction Elimination in 12 Seasons
**Observation:** Priority 1 (Survival: Stability ≤ 2) fires reliably and prevents any faction from reaching Stability 0. The system is stable — possibly too stable for a 12-season game.

**Analysis:** This is partially by design. The priority tree template places survival as the highest priority because factions should not self-destruct through AI stupidity. However, the simulation does not model player-faction military aggression, which is the primary elimination vector.

**Proposed resolution:** No patch needed. The priority trees correctly prevent NPC self-destruction. Faction elimination requires player-driven military campaigns, which are outside the scope of NPC AI. Log as EXPECTED.

---

### F-06 (MODERATE): RS Decline Too Slow
**Observation:** RS ends at 61–66 across all runs. Starting value 72, annual decay −1. Only 3 years of decay (−3) plus minor Collection failure effects (−1 per failed Collection).

**Analysis:** RS decline is primarily driven by Thread operations at faction scale, which are not modeled in this simulation. The NPC priority trees do not include RS-damaging actions (Thread operations are PC-driven or event-driven). The slow decline is expected at the NPC-only level.

**Proposed resolution:** No patch to priority trees. RS decline from Thread operations should be modeled in a separate simulation (SIM-NPC-05 or a new SIM-RS entry). The priority trees correctly avoid RS-damaging actions (no NPC faction intentionally damages RS except Niflhel's Thread Tension accumulation, which is not directly modeled here).

---

### F-07 (LOW): Interaction Loop Functional
**Observation:** Church→Varfell (Heresy Investigation), Crown→Church (Royal Decree), Guilds→weakest Wealth, Hafenmark→TC (Suppress), Löwenritter→Crown (monitor). The interaction loop creates meaningful faction relationships without degenerate cycles.

**Status:** PASS. No patch needed.

---

## Patches Required

| ID | Severity | Target | Description |
|---|---|---|---|
| PP-NPC-01 | CRITICAL | Crown Priority Tree P3 | Gate Royal Decree on Mandate ≥ 3. Remove failure cost at Mandate ≤ 2. |
| PP-NPC-02 | CRITICAL | Crown Priority Tree P2 + Coup Counter | Crown TC awareness at TC ≥ 35. Coup trigger requires active Church Assert, not just passive TC. |
| PP-NPC-03 | CRITICAL | Church Framework Drift | Condition on Stability ≥ 4 + TC advance + per year not per 2 seasons. |
| PP-NPC-04 | MODERATE | Varfell Priority Tree P2 | Once-per-season state tracking for Collection use. |

---

## Simulation Limitations

1. Territory control not modeled (simplified to count). Territorial seizure, fortification, and adjacency effects omitted.
2. Player faction actions not modeled (NPC-only). The simulation tests AI-vs-AI, not AI-vs-player.
3. Events/cards not modeled. BG event cards introduce variance not captured here.
4. RM founding and Warden emergence not modeled (conditional on game state triggers not reached in 12 seasons).
5. Niflhel Thread Tension accumulation not modeled at faction interaction level.
6. Coalition mechanics (PP-504) not modeled.

## SIM-NPC-01 Status: COMPLETE. 7 findings. 4 patches proposed. 3 critical.
