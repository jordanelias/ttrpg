---
atom_id: valoria_session_master_2026-04-25__01__context-window-1-session-b-core
source_file: valoria_session_master_2026-04-25.md
source_section: "Context Window 1 — Session B Core"
section_index: 1
total_sections: 5
line_count: 39
char_count: 2949
source_sha256: 8b5f5049f7c1710a
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## Context Window 1 — Session B Core

### Niflhel Dissolution

Niflhel was not a faction — it was the Church's inquisitorial arm. Dissolved per conflict_architecture_proposal (CANON). Functions distributed to settlement-level phenomena.

| Commit | SHA | Files Modified | What |
|--------|-----|----------------|------|
| 1 | `f8dafe0` | params/bg/core.md, params/factions/stats_1_7_scale.md, params/bg/npc_priority_trees.md | Faction stat blocks struck, priority trees struck, dissolution note added |
| 2 | `1fdc160` | references/throughlines_complete.md, throughline_registry.md, throughlines_meta.md, throughlines_meta_infill.md | T-10 "Niflhel as Accelerationist" struck. М-4 count 5→4 |
| 3 | `747adcd` | designs/npcs/npc_behavior_v30.md, references/canonical_sources.yaml | §2.12 (four-arm structure), §8.8 (priority tree), §8.8a (intelligence output) struck. Scattered refs updated |

**Replacement mechanics added** (commit 6, `d78d7b9`):

- **§4.7 Black Markets** — Automatic when settlement Order ≤ 1 or no governor. Wealth +0.5, Accord −0.5. Disappear at Order ≥ 3.
- **§4.8 Intelligence Brokers** — Individual named NPCs in settlements with Prosperity ≥ 3 and weak governance. Sell intel, fabricate intel, can be killed/bought/turned. One per qualifying settlement.
- **§4.9 Thread Exploitation Sites** — Settlements at Thread Proximity ≤ 2. Any actor can harvest (RS −0.5/harvest/season, Wealth +1). Tragedy-of-the-commons dynamic.

### Löwenritter Graduated Autonomy

Binary Coup Counter (0–4, threshold 4) replaced with 4-stage graduated autonomy.

| Stage | Trigger | Effect |
|-------|---------|--------|
| **Loyal** | Start | S014 Barracks answers to Crown via Ehrenwall. Normal. |
| **Restless** | Crown Stability ≤ 3, OR no military action 4+ seasons, OR Crown loses a province | S014 follows Löwenritter for defensive only. Crown +1 Ob offensive deployment. |
| **Autonomous** | Crown Stability ≤ 2, OR Ehrenwall Disposition < 0, OR 4+ seasons Restless | S014 does not respond to Crown. T14 garrison under Ehrenwall exclusively. PI −1. |
| **Split** | Crown attacks Löwenritter, OR Crown eliminated, OR 4+ seasons Autonomous | T14 becomes Löwenritter territory. Separate faction. PI −3. Irreversible. |

**Reversal:** Stages 1–3 reversible by raising Stability, conducting military action, or improving Ehrenwall Disposition.

| Commit | SHA | Files Modified | What |
|--------|-----|----------------|------|
| 4 | `c0be619` | params/bg/core.md, params/bg/institutions.md, designs/provincial/clock_registry_v30.md, references/canonical_sources.yaml | Coup Counter → graduated autonomy table. Pre/post-coup → pre/post-Split terminology |
| 5 | `f6b6ae6` | designs/npcs/npc_behavior_v30.md | §8.7, §7.5, arc refs: Coup Counter → Autonomy stages throughout NPC behavior trees |
| 6 | `d78d7b9` | designs/territory/settlement_layer_v30.md, references/canonical_sources.yaml | Settlement phenomena §4.7-4.9 added (see above) |

---
