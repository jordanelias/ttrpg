# MECHANICAL LOG SPECIFICATION — Granular Audit Trace
## Valoria Balance Audit · 2026-05-14 · Companion to `workplan_directions_NERS.md`
## Purpose: define logging format so every state change is auditable and reconstructable

---

# §0 PRINCIPLE

> **No state change occurs without a log entry. No log entry exists without a canonical-rule citation.**

Auditing means an external reviewer should be able to:
1. Pick any campaign from a sim run
2. Replay it event-by-event from the log
3. Verify every dice roll, formula evaluation, and state mutation against canonical rules
4. Identify exactly where any anomaly occurred

This document specifies the log format that enables this.

---

# §1 LOG FILE STRUCTURE

## §1.1 One JSONL file per campaign

Each campaign produces a single `.jsonl` file. One JSON object per line. Newline-delimited.

Filename: `{test_id}-{seed:06d}.jsonl`
Example: `T1-P1-BU-N-001-000042.jsonl`

## §1.2 Log directory structure

```
logs/
├── T1-P1-BU-N-001/
│   ├── 000000.jsonl
│   ├── 000001.jsonl
│   ├── ...
│   └── 000499.jsonl   # 500 campaigns
├── T1-P2-BU-N-001/
│   └── ...
└── T4-INT-001/
    └── ...
```

500 campaigns × 1 file each = small fixed overhead per test.

## §1.3 Log entry types (top-level `event_type` field)

| Type | Description | Frequency |
|------|-------------|-----------|
| `campaign_start` | Campaign initialization, seed, config | 1 per file (line 1) |
| `season_start` | Season N begins | 1 per season |
| `phase_start` | Phase begins (action / resolution / propagation / accounting) | 4 per season |
| `action_attempt` | Faction selects action; prereqs evaluated | 0+ per phase |
| `action_resolved` | Action's dice roll + degree determined | 0+ per phase |
| `state_change` | Single atomic state mutation | many per resolution |
| `propagation` | Cascading effect from state change | 0+ per state change |
| `hook_fire` | Mechanical hook (Revolt, Inquisitor Decay, etc.) | 0+ per season |
| `accounting` | End-of-season clock advancement + winner check | 1 per season |
| `victory_check` | Universal Sovereignty check fires | 1 per accounting |
| `victory` | Winner declared | 0 or 1 per campaign (final line if 1) |
| `timeout` | Campaign reached max seasons without winner | 0 or 1 per campaign |
| `campaign_end` | Final state snapshot | 1 per file (last line) |

---

# §2 UNIVERSAL FIELDS (every event)

Every log entry contains:

```json
{
  "ts": "2026-05-14T13:42:18.123456Z",
  "campaign_id": "T1-P1-BU-N-001-000042",
  "season": 12,
  "arc": 3,
  "event_type": "...",
  "event_id": 1547,            // monotonic per-campaign sequence
  "parent_event_id": 1543,     // if this is a propagation of a prior event
  ...event-specific fields
}
```

**`event_id` is mandatory and monotonic per campaign.** It enables reconstruction of causal chains.
**`parent_event_id` links propagations to their cause** — critical for auditing cascading effects.

---

# §3 PER-EVENT-TYPE SCHEMA

## §3.1 `campaign_start`

```json
{
  "event_type": "campaign_start",
  "config": {
    "seed": 42,
    "campaign_seasons": 36,
    "consent_rate": 0.6,
    "turmoil_cap": 12,
    "victory_threshold": 11,
    "proposals_enabled": ["P1", "P2", "P3", "P4", "P5", "P6"],
    "sim_version": "v11"
  },
  "initial_state": {
    "factions": {
      "Crown": {"L": 5, "Mil": 4, "I": 4, "W": 4, "Sta": 4, "territories": ["T01","T02","T03","T04","T05","T06"]},
      "Church": {"L": 5, ...},
      ...
    },
    "territories": {
      "T01": {"owner": "Crown", "accord": 2, "order": 3, "prosperity": 2, "garrison": false},
      ...
    },
    "clocks": {"CI": 0, "MS": 0, "Turmoil": 0, "PI": 3}
  },
  "canonical_ref": "peninsular_strain_v30 §2.1 starting state"
}
```

## §3.2 `season_start`

```json
{
  "event_type": "season_start",
  "season": 12,
  "snapshot": {
    "factions_L": {"Crown": 5, "Church": 5, "Hafenmark": 3, "Varfell": 2},
    "factions_territories_count": {"Crown": 7, "Church": 3, "Hafenmark": 3, "Varfell": 2},
    "clocks": {"CI": 12, "MS": 0, "Turmoil": 8, "PI": 5, "Strain": 8}
  }
}
```

Snapshot at season start enables verification of inter-season state evolution.

## §3.3 `action_attempt`

```json
{
  "event_type": "action_attempt",
  "phase": "action",
  "actor": "Crown",
  "action_name": "Crown Initiative",
  "mode": "Mode_I_Royal_Progress",         // if applicable
  "target": null,                          // or territory ID / faction name
  "prereqs": [
    {"check": "actor.name == 'Crown'", "result": true, "canonical_ref": "Part_10 §3"},
    {"check": "actor.senator_inward_used == false", "result": true, "canonical_ref": "P5 spec"},
    {"check": "actor.stats['W'] >= 2", "result": true, "actual": 3, "canonical_ref": "P5 spec"}
  ],
  "prereqs_passed": true,
  "score": 8.5,
  "selection_weight": 4
}
```

If prereqs_passed is false, action does not proceed; log entry ends here.

## §3.4 `action_resolved`

```json
{
  "event_type": "action_resolved",
  "parent_event_id": 1547,
  "actor": "Crown",
  "action_name": "Crown Initiative",
  "mode": "Mode_I_Royal_Progress",
  "pool_calculation": {
    "components": [
      {"source": "actor.stats['I']", "value": 4, "canonical_ref": "P5 spec §pool"}
    ],
    "total_pool": 4
  },
  "obstacle_calculation": {
    "formula": "max(1, sum(territory.accord for territory in actor.territories) // 2)",
    "inputs": {
      "territory_accords": {"T01": 2, "T02": 1, "T03": 2, "T04": 2, "T05": 1, "T06": 0, "T07": 2},
      "sum": 10
    },
    "result": 5,
    "canonical_ref": "P5 spec §obstacle / М-2 geography holds pressure"
  },
  "dice_roll": {
    "rolls": [4, 6, 2, 5],
    "successes_count": 3,
    "explosions": [],
    "method": "roll_pool(pool=4)",
    "canonical_ref": "peninsular_strain_v30 §3.1 dice resolution"
  },
  "net": -2,                              // successes - ob = 3 - 5 = -2
  "degree": "Failure",
  "degree_table_ref": "peninsular_strain_v30 §3.2 degree table",
  "outcome_applied": [1548, 1549]         // event_ids of resulting state_change entries
}
```

**Every formula has its inputs logged. Every dice roll has its result. Every canonical reference is cited.** This is what makes the log auditable.

## §3.5 `state_change` (atomic mutation)

```json
{
  "event_type": "state_change",
  "parent_event_id": 1547,
  "target_type": "faction" | "territory" | "clock" | "treaty_register",
  "target_id": "Crown",
  "attribute": "stats.L",
  "before": 5,
  "after": 6,
  "delta": 1,
  "cap_applied": false,                    // true if min/max clamp triggered
  "canonical_ref": "P5 spec §effects / 'L+1 on Success'",
  "reason": "Crown Initiative Mode I Success outcome"
}
```

**Every mutation is atomic.** A single `action_resolved` may produce multiple `state_change` entries (e.g., L +1 AND accord +1 on Crown Initiative Mode I Success → 2 state_change entries).

## §3.6 `propagation`

```json
{
  "event_type": "propagation",
  "parent_event_id": 1548,                // the state_change that caused this
  "kind": "morale_cascade" | "treaty_cascade" | "excommunication_cascade",
  "trigger": "Crown.Sta dropped below 2",
  "affected_targets": ["T01", "T02"],
  "subsequent_events": [1551, 1552, 1553],
  "canonical_ref": "T12 Morale and Legitimacy Cascade"
}
```

Propagations are explicit. They allow auditors to verify cascade chains.

## §3.7 `hook_fire`

```json
{
  "event_type": "hook_fire",
  "hook_name": "revolt_check",
  "fired_at": "end_of_season",
  "subject": {"territory": "T06", "accord": 0},
  "outcome": "revolt_succeeded",
  "consequences_applied": [1620, 1621, 1622],
  "canonical_ref": "peninsular_strain_v30 §7 step 4c (Revolt: Accord 0 → Uncontrolled)",
  "rule_check": {
    "edited_rule_id": "ED-632",
    "rule_text": "Popular Uprising at Accord 0 = Uncontrolled, NOT transfer to Inquisitor holder"
  }
}
```

Hook fires are logged with `rule_check` blocks tying them to specific canonical edits (ED-numbered editorial decisions).

## §3.8 `accounting`

```json
{
  "event_type": "accounting",
  "season_ending": 12,
  "clocks_before": {"CI": 12, "MS": 0, "Turmoil": 8, "PI": 5, "Strain": 8},
  "clocks_after": {"CI": 13, "MS": 0, "Turmoil": 7, "PI": 5, "Strain": 7},
  "clocks_changes": [
    {"clock": "CI", "delta": 1, "canonical_ref": "Campaign Index tick"},
    {"clock": "Turmoil", "delta": -1, "canonical_ref": "Turmoil decays by 1 if no revolts"}
  ],
  "arc_boundary_reached": true,             // if season % 4 == 0
  "arc_resets_applied": ["pa_session", "influence_surge", "ecclesiastical_appointment"]
}
```

## §3.9 `victory_check`

```json
{
  "event_type": "victory_check",
  "check_type": "Universal_Peninsular_Sovereignty",
  "threshold_used": 11,                     // P2 if enabled, else 15
  "per_faction_evaluation": [
    {
      "faction": "Crown",
      "territories_direct": 7,
      "territories_via_treaty": 4,
      "treaties_active": [{"partner": "Hafenmark", "type": "CrownTreaty"}],
      "total_controlled": 11,
      "threshold_met": true,
      "all_accord_ge_2": true,
      "turmoil_le_cap": true,                // 7 <= 12
      "criteria_all_met": true,
      "sovereignty_history_before": 1,
      "sovereignty_history_after": 2,
      "winner": true
    },
    {"faction": "Church", "territories_direct": 3, ...,"criteria_all_met": false, "sovereignty_history_after": 0},
    ...
  ],
  "winner_declared": "Crown",
  "canonical_ref": "peninsular_strain_v30 §6.1 Universal Peninsular Sovereignty"
}
```

The victory_check entry shows EVERY check evaluated for EVERY faction. Even if Crown wins, log shows why Church/Hafenmark/Varfell didn't.

## §3.10 `victory` / `timeout`

```json
{
  "event_type": "victory",
  "winner": "Crown",
  "winning_season": 12,
  "winning_arc": 3,
  "victory_path": "treaty_hegemony",         // or "direct_conquest" / "co_victory_partition"
  "final_state_snapshot": {
    "factions": {"Crown": {"L": 6, "Sta": 4, ...}, ...},
    "territories_summary": {"Crown_direct": 7, "Crown_treaty": 4, "Church": 3, "Hafenmark": 1, "Uncontrolled": 0},
    "clocks": {...}
  },
  "almud_state": "strong",                   // character-scale outcome
  "almud_state_evidence": {
    "min_sta_observed": 3,
    "min_L_observed": 4,
    "deposition_attempts": 1,
    "deposition_succeeded": false
  }
}
```

## §3.11 `campaign_end`

```json
{
  "event_type": "campaign_end",
  "total_events_logged": 8423,
  "log_integrity_check": {
    "all_parent_ids_resolve": true,
    "monotonic_event_ids": true,
    "monotonic_seasons": true,
    "every_state_change_has_canonical_ref": true,
    "every_dice_roll_has_inputs_recorded": true,
    "every_obstacle_calc_has_inputs_recorded": true
  }
}
```

A self-check block. If any integrity flag is false, the campaign log is corrupt and the run must be discarded.

---

# §4 LOGGING REQUIREMENTS PER PROPOSAL

Each proposal adds specific logging requirements beyond the universal schema:

## §4.1 P1 — Q-21 EA throttle

When Ecclesiastical Appointment is attempted:
- Log `prereqs[]` entry: `{"check": "ecclesiastical_appointment_arc_used == false", "result": ..., "canonical_ref": "P1 throttle"}`
- Log `prereqs[]` entry: `{"check": "world.arc - actor.ea_last_arc >= 2", "result": ..., "canonical_ref": "P1 every-other-arc"}`
- If blocked: log the block reason explicitly

## §4.2 P2 — Threshold 11/15

In `victory_check`:
- Log `threshold_used` field showing 11 vs 15
- Log per-faction `territories_via_treaty` calculation showing which treaties counted

## §4.3 P3 — Treaty Expiration

In `accounting` (arc-boundary only):
- Generate one `hook_fire` event per active Crown Treaty
- Log: `{"hook_name": "treaty_expiration_check", "subject": {"treaty": {"crown": "...", "partner": "..."}}, "dice_outcome": {"roll": 0.34, "threshold": 0.4, "lapsed": true}}`
- If lapsed: subsequent `state_change` removes from both factions' treaty registers, linked via `parent_event_id`

## §4.4 P4 — Vaynard's Settlement

When Vaynard's Settlement is attempted:
- Log `target` field with territory ID and `target_state` (accord, order, prosperity before action)
- Log `pool_calculation` with Mil + W/2 split
- Log `state_change` for territory accord and order separately (two atomic mutations)

## §4.5 P5 — Crown Initiative

When Crown Initiative is attempted:
- Log `mode` field (Mode_I_Royal_Progress / Mode_II_Great_Work / Mode_III_Coronation_Renewal)
- For Mode II: log Open Pledge state in a dedicated `pledge_open` event
- For Mode III: log Church-state dependencies in prereqs and Excommunication-clear in state_change
- For Mode I: log per-territory Accord state used in Ob calculation

For Mode II Open Pledge: emit `pledge_progress` events at seasons 1 and 2 of the 3-season pledge:
```json
{
  "event_type": "pledge_progress",
  "pledge_id": "Crown_Initiative_Mode_II_S12",
  "season_in_pledge": 1,
  "of_total": 3,
  "still_open": true,
  "excommunicated": false,                  // breach trigger
  "W_cost_paid_this_season": 1
}
```

## §4.6 P6 — Charter of Liberties

When Charter is attempted:
- Log `prereqs[]` entry confirming pure-W cost (no Token cost in revised version)
- Log `state_change` for L and PI as separate atomic entries

## §4.7 P7 — Vaynard's Hall (if enabled)

- Log Token sacrifice as separate `state_change` entry on `revelation_tokens` attribute
- Log public-insult target selection if Overwhelming degree

---

# §5 LOG SIZE AND PERFORMANCE

## §5.1 Estimated log size per campaign

| Event type | Avg per campaign | Bytes per event | Subtotal |
|------------|------------------|-----------------|----------|
| campaign_start | 1 | 2000 | 2000 |
| season_start | 36 | 300 | 10800 |
| phase_start | 144 | 100 | 14400 |
| action_attempt | ~108 | 600 | 64800 |
| action_resolved | ~72 | 1200 | 86400 |
| state_change | ~200 | 250 | 50000 |
| propagation | ~30 | 400 | 12000 |
| hook_fire | ~50 | 500 | 25000 |
| accounting | 36 | 600 | 21600 |
| victory_check | 36 | 1500 | 54000 |
| victory + end | 2 | 1500 | 3000 |
| **Total** | **~715 events** | | **~344 KB per campaign** |

For 500-campaign test: ~172 MB. For 72,000 campaigns total workplan: ~24 GB. Manageable on disk; compressible.

## §5.2 Logging overhead

In-process logging: ~5-10% sim runtime overhead. Acceptable.

Optimization: batch-write per-season; flush per-campaign-end. Avoid per-event flushing.

## §5.3 Tiered logging (optional)

For high-volume tests (e.g., 72,000-campaign workplan), tiered logging:

- **Tier 1 (always log)**: campaign_start, victory, campaign_end, prereq failures, integrity violations
- **Tier 2 (log if enabled)**: full event stream
- **Tier 3 (skip by default, log on rerun-with-debug)**: per-die-roll detail

Default for workplan: Tier 1 + Tier 2 enabled, Tier 3 disabled.

---

# §6 AUDIT WORKFLOW

How auditors use the logs:

## §6.1 Spot-check audit

1. Pick random campaign log
2. Read `campaign_start` to verify config
3. Read `victory` (or `timeout`) to see outcome
4. Scan `victory_check` to verify winner-calculation
5. Spot-check 3-5 random `action_resolved` events: verify pool, obstacle, and dice math
6. Verify `campaign_end` integrity flags are all true

Time: ~10 minutes per campaign.

## §6.2 Targeted audit

For specific hypothesis (e.g., "is Q-21 throttle actually firing?"):

```python
import json
# Load all logs from test T1-P1-BU-N-001
ea_attempts = 0; ea_blocked_by_throttle = 0
for log_path in glob.glob('logs/T1-P1-BU-N-001/*.jsonl'):
    for line in open(log_path):
        event = json.loads(line)
        if event['event_type'] == 'action_attempt' and event.get('action_name') == 'Ecclesiastical Appointment':
            ea_attempts += 1
            for prereq in event.get('prereqs', []):
                if 'every-other-arc' in prereq.get('canonical_ref', '') and not prereq['result']:
                    ea_blocked_by_throttle += 1
print(f"EA attempted {ea_attempts} times; blocked by throttle {ea_blocked_by_throttle} times")
```

Time: ~5 minutes for any specific question across 500 campaigns.

## §6.3 Replay audit

Reconstruct any single campaign event-by-event:

```python
def replay_campaign(log_path):
    state = None
    for line in open(log_path):
        event = json.loads(line)
        if event['event_type'] == 'campaign_start':
            state = event['initial_state']
        elif event['event_type'] == 'state_change':
            apply_state_change(state, event)
        elif event['event_type'] == 'victory':
            return state, event['winner']
```

Any discrepancy between replay-state and logged-state indicates a logging bug or sim non-determinism.

## §6.4 Canonical-rule cross-reference audit

For each `canonical_ref` field, verify the referenced rule actually exists and produces the logged effect:

```python
canonical_refs_used = set()
for event in all_events:
    if 'canonical_ref' in event:
        canonical_refs_used.add(event['canonical_ref'])
# Manual: verify each ref against canonical sources
```

This is the deepest audit. Catches sim-vs-canon drift.

---

# §7 IMPLEMENTATION CHECKLIST

For sim implementers building this logging:

- [ ] Every `action_attempt` logs ALL prereqs with canonical_ref
- [ ] Every `action_resolved` logs pool_calculation, obstacle_calculation, dice_roll with inputs
- [ ] Every state mutation goes through a logging wrapper (no direct attribute assignment)
- [ ] Every state_change has canonical_ref and reason
- [ ] Every propagation has explicit parent_event_id linkage
- [ ] Every hook_fire logs the rule check
- [ ] Every victory_check logs ALL factions' evaluations, not just winner
- [ ] campaign_end self-check runs and reports integrity flags
- [ ] Log file per campaign is JSONL (one event per line)
- [ ] No state changes occur OUTSIDE the logged event stream
- [ ] No dice rolls occur OUTSIDE logged dice_roll fields

---

# §8 EXAMPLE — Full event sequence for one action

To illustrate, here's an annotated sequence for a single Crown Initiative Mode I action:

```jsonl
// Action selection
{"event_id": 1547, "event_type": "action_attempt", "actor": "Crown", "action_name": "Crown Initiative", "mode": "Mode_I_Royal_Progress", "prereqs": [...], "prereqs_passed": true, "score": 8.5, ...}

// Resolution (pool, obstacle, dice, degree)
{"event_id": 1548, "event_type": "action_resolved", "parent_event_id": 1547, "pool_calculation": {"components": [{"source": "I", "value": 4}], "total_pool": 4}, "obstacle_calculation": {"formula": "max(1, sum(territory.accord)//2)", "inputs": {"sum_accord": 10}, "result": 5, "canonical_ref": "P5 spec"}, "dice_roll": {"rolls": [4,6,2,5], "successes_count": 3}, "net": -2, "degree": "Failure", ...}

// Even Failure has consequences: W cost was paid
{"event_id": 1549, "event_type": "state_change", "parent_event_id": 1548, "target_type": "faction", "target_id": "Crown", "attribute": "stats.W", "before": 3, "after": 1, "delta": -2, "canonical_ref": "P5 spec §cost: W-2 regardless of outcome", "reason": "Crown Initiative cost paid"}

// And the senator_inward slot is consumed
{"event_id": 1550, "event_type": "state_change", "parent_event_id": 1548, "target_type": "faction", "target_id": "Crown", "attribute": "senator_inward_used", "before": false, "after": true, "delta": null, "canonical_ref": "P5 spec §slot: Senator Inward 1×/season", "reason": "Slot consumed"}
```

Four log lines for one failed action. **Auditable end-to-end.**

For a successful action with cascading effects, expect 8-15 log lines per action.

---

# §9 RELATIONSHIP TO WORKPLAN

This specification works alongside `workplan_directions_NERS.md`:

- **Workplan** defines: WHAT to test
- **Mechanical log** defines: HOW to record what the tests observe

For every test in the workplan, the mechanical log provides the audit trail. A test passes only if:
1. The summary statistic matches the pass criterion AND
2. The mechanical log integrity check passes for all 500 campaigns AND
3. Spot-check audit of 5+ random campaigns confirms canonical rules were followed

**No test passes on summary statistics alone.** The mechanical log is the verification surface.

---

# §10 NEXT STEPS

To execute the workplan with this logging:

1. **Iteration 0 (preparation)**: implement the logging wrapper in `mc_v12.py`. Estimated effort: ~200 lines of code over the v11 simulator.
2. **Iteration 0.1**: verify integrity checks fire correctly on synthetic broken logs.
3. **Iteration A**: run Phase 1 tests for P1/P2/P3. Spot-check 5 logs per test.
4. **Iteration B**: run Phase 2 pairwise tests for top-priority pairs.
5. **Iteration C**: run Phase 4 integration tests (RC-v1 package).
6. **Iteration D**: run Phase 5 throughline tests + manual canonical_ref verification.

At completion: pass/fail report per test + full log archive + audit summary.

---

*Mechanical Log Specification · 2026-05-14*
*Companion to workplan_directions_NERS.md*
*Authority: peninsular_strain_v30 mechanical rules + canon constraints P-01..P-15*
*Status: ready for implementation; awaiting v12 simulator build*
