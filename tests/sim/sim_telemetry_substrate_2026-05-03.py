"""
Telemetry Substrate Simulation — Stage 5 (Mandatory Zoom-In Frequency + SA-Budget Saturation)
================================================================================================
Date: 2026-05-03
Skill: simulation

PURPOSE
-------
Exercises the Phase 5a session 3.5 telemetry substrate (valoria-game commit b8b9a4a) by
porting SceneTimer + TimeAggregator data-flow into Python and driving them with synthetic
season-loops. Produces empirical distributions for:

  Q1  Mandatory zoom-in count per season         — frequency of §4.3.2 triggers
  Q2  Total opportunities per season             — slate size (mandatory + elective)
  Q3  SA-budget saturation rate                  — % of seasons where opps exceed budget
  Q4  Mandatory-overflow rate                    — % of seasons where mandatory > budget
  Q5  Per-system scene-count distribution        — which systems get how much attention
  Q6  Per-system minute estimate                 — using TABLETOP duration anchors (assumption)
  Q7  Time-per-SA distribution                   — minutes/SA per system

CANON ANCHORS
-------------
- designs/architecture/scale_transitions_v30.md §4.3.2 — 8 mandatory zoom-in triggers
- designs/architecture/scale_transitions_v30.md §4.3.3 — World-State (Priority 1) triggers
- designs/architecture/player_agency_v30.md §6 — Scene Action Budget (4 SA/season Normal,
  5–7 opps/slate, modifiers Standing 4-5 +1, 6-7 +2, Knot +1, Wounded -1, Out of Breath -1)
- designs/architecture/campaign_modes_v30.md §12.3 — TABLETOP timing table (Personal 60-90min,
  Strategic 20-30min, Cascade 10-15min, Accounting 5-10min). Used as ASSUMPTION durations
  pending real measurement (see CAVEATS).

CAVEATS
-------
[ASSUMPTION] Per-scene minute durations are TABLETOP anchors, not measured videogame values.
  Stage 5 of the time-review plan is precisely the work of replacing these with measurements
  from real Godot runtime. This harness verifies the substrate's data-flow and produces
  duration-INDEPENDENT outputs (Q1-Q5) plus duration-DEPENDENT outputs (Q6-Q7) flagged as
  estimates.

[ASSUMPTION] Mandatory-trigger probabilities per season are calibrated against engine_v3.py
  observations for revolt frequency and faction-elimination cascades, plus reasoned estimates
  for the remaining triggers. Probabilities are documented per-trigger below.

[ASSUMPTION] Playthrough length 40 seasons (10 game-years) — placeholder pending Stage 0
  Jordan-decision on target campaign hours.

OUTPUTS
-------
Writes:
  /home/claude/sim_telemetry_jsonl/<persona>_<run>.jsonl   — raw telemetry sidecar files
  /home/claude/sim_telemetry_results.json                  — aggregated stats
Stdout: human-readable report

USAGE
-----
  python3 sim_telemetry_substrate_2026-05-03.py [--seed=42] [--campaigns=100] [--seasons=40]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import statistics
import sys
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Tuple


# ════════════════════════════════════════════════════════════════════════════════
# §A. Python port of SceneTimer + TimeAggregator
# ════════════════════════════════════════════════════════════════════════════════
#
# Mirrors the GDScript substrate at autoload/SceneTimer.gd + systems/util/TimeAggregator.gd.
# Wall-clock kept OUT of "Key" payloads here too — the simulator emits Keys to a deterministic
# stream and writes wall-clock to a separate JSONL sidecar, joined by scene_id.

@dataclass
class Key:
    """Mirror of valoria-game/systems/keys/Key.gd"""
    type: str
    timestamp: int
    payload: dict
    scope: str
    source_system: str

    @property
    def id(self) -> str:
        # Mirror Key._content_hash — SHA256 of canonical serial, first 12 hex
        serial = "%s|%d|%s|%s|%s" % (
            self.type, self.timestamp,
            json.dumps(self.payload, sort_keys=True),
            self.scope, self.source_system,
        )
        return hashlib.sha256(serial.encode()).hexdigest()[:12]


class KeyStore:
    """Mirror of autoload/KeyStore.gd subset — emit, log_hash, subscriptions."""
    def __init__(self):
        self.timeline: List[Key] = []
        self.subs: Dict[str, list] = {}   # type -> [callback]

    def emit(self, type_: str, payload: dict, scope: str, source: str = "sim") -> Key:
        ts = len(self.timeline)
        k = Key(type=type_, timestamp=ts, payload=payload, scope=scope, source_system=source)
        self.timeline.append(k)
        # Dispatch
        for pat, cbs in self.subs.items():
            if pat == "*" or pat == type_ or (pat.endswith(".*") and type_.startswith(pat[:-2] + ".")):
                for cb in cbs:
                    cb(k)
        return k

    def subscribe(self, pattern: str, cb):
        self.subs.setdefault(pattern, []).append(cb)

    def log_hash(self) -> str:
        serial = "".join(
            f"{k.id}|{k.type}|{k.timestamp}|{json.dumps(k.payload, sort_keys=True)}\n"
            for k in self.timeline
        )
        return hashlib.sha256(serial.encode()).hexdigest()[:16]


class SceneTimer:
    """Mirror of autoload/SceneTimer.gd — wall-clock sidecar."""
    SCHEMA_VERSION = 1

    def __init__(self, keystore: KeyStore, jsonl_path: str, campaign_id: str, session_id: str):
        self.ks = keystore
        self.path = jsonl_path
        self.campaign_id = campaign_id
        self.session_id = session_id
        self._open: Dict[str, dict] = {}       # scene_id -> open record
        self._records: List[dict] = []
        # Subscribe
        keystore.subscribe("mechanical.scene_entered", self._on_entered)
        keystore.subscribe("mechanical.scene_exited",  self._on_exited)
        keystore.subscribe("mechanical.scene_skipped", self._on_skipped)
        # Wall-clock generator: synthetic monotonic ms counter (sim has no real clock).
        # Real Godot runtime would use Time.get_ticks_msec().
        self._wall_ms = 0

    def advance_wall(self, ms: int):
        """Advance the synthetic wall clock — caller invokes between scene_entered/exited."""
        self._wall_ms += ms

    def _on_entered(self, k: Key):
        sid = k.payload["scene_id"]
        self._open[sid] = {
            "scene_id": sid,
            "system_id": k.payload["system_id"],
            "scope": k.payload["scope"],
            "slate_priority": k.payload["slate_priority"],
            "season_n": k.payload["season_n"],
            "parent_scene_id": k.payload.get("parent_scene_id", ""),
            "stack_depth": k.payload.get("stack_depth_after", 1),
            "wall_in_ms": self._wall_ms,
        }

    def _on_exited(self, k: Key):
        sid = k.payload["scene_id"]
        if sid not in self._open:
            return
        op = self._open.pop(sid)
        wall_out = self._wall_ms
        elapsed = max(0, wall_out - op["wall_in_ms"])
        rec = {
            "schema_version":     self.SCHEMA_VERSION,
            "scene_id":           sid,
            "session_id":         self.session_id,
            "campaign_id":        self.campaign_id,
            "system_id":          op["system_id"],
            "scope":              op["scope"],
            "slate_priority":     op["slate_priority"],
            "season_n":           op["season_n"],
            "parent_scene_id":    op["parent_scene_id"],
            "stack_depth":        op["stack_depth"],
            "sa_cost_actual":     k.payload.get("sa_cost_actual", -1),
            "outcome_class":      k.payload.get("outcome_class", ""),
            "ended_by":           k.payload.get("ended_by", ""),
            "wall_in_ms":         op["wall_in_ms"],
            "wall_out_ms":        wall_out,
            "raw_elapsed_ms":     elapsed,
            "paused_ms_excluded": 0,
            "idle_ms_excluded":   0,
            "elapsed_ms":         elapsed,
            "orphan":             False,
        }
        self._records.append(rec)

    def _on_skipped(self, k: Key):
        rec = {
            "schema_version":     self.SCHEMA_VERSION,
            "scene_id":           k.payload["scene_id"],
            "session_id":         self.session_id,
            "campaign_id":        self.campaign_id,
            "system_id":          k.payload.get("system_id", ""),
            "scope":              k.payload.get("scope", ""),
            "slate_priority":     k.payload.get("slate_priority", -1),
            "season_n":           k.payload.get("season_n", -1),
            "parent_scene_id":    "",
            "stack_depth":        0,
            "sa_cost_actual":     0,
            "outcome_class":      "skipped",
            "ended_by":           "auto_resolve",
            "wall_in_ms":         self._wall_ms,
            "wall_out_ms":        self._wall_ms,
            "raw_elapsed_ms":     0,
            "paused_ms_excluded": 0,
            "idle_ms_excluded":   0,
            "elapsed_ms":         0,
            "orphan":             False,
        }
        self._records.append(rec)

    def flush(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as f:
            for r in self._records:
                f.write(json.dumps(r) + "\n")


class TimeAggregator:
    """Mirror of systems/util/TimeAggregator.gd."""
    @staticmethod
    def per_system_minutes(records: List[dict]) -> Dict[str, float]:
        out: Dict[str, float] = {}
        for r in records:
            if r.get("orphan"): continue
            sid = r.get("system_id", "")
            ms = r.get("elapsed_ms", 0)
            out[sid] = out.get(sid, 0.0) + ms / 60_000.0
        return out

    @staticmethod
    def sa_consumption_by_system(records: List[dict]) -> Dict[str, int]:
        out: Dict[str, int] = {}
        for r in records:
            if r.get("orphan"): continue
            sa = r.get("sa_cost_actual", 0)
            if sa < 0: continue
            sid = r.get("system_id", "")
            out[sid] = out.get(sid, 0) + sa
        return out

    @staticmethod
    def time_per_sa_by_system(records: List[dict]) -> Dict[str, float]:
        mins = TimeAggregator.per_system_minutes(records)
        sa = TimeAggregator.sa_consumption_by_system(records)
        out: Dict[str, float] = {}
        for sid, m in mins.items():
            n = sa.get(sid, 0)
            out[sid] = m / n if n > 0 else -1.0
        return out

    @staticmethod
    def mandatory_zoom_rate(records: List[dict]) -> dict:
        by_season: Dict[int, int] = {}
        for r in records:
            if r.get("orphan"): continue
            if r.get("slate_priority", -1) != 0: continue
            s = r.get("season_n", -1)
            by_season[s] = by_season.get(s, 0) + 1
        counts = sorted(by_season.values())
        if not counts:
            return {"seasons_observed": 0, "mean": 0.0, "p50": 0, "p90": 0, "max": 0}
        return {
            "seasons_observed": len(counts),
            "mean": sum(counts) / len(counts),
            "p50": counts[len(counts) // 2],
            "p90": counts[min(len(counts) - 1, int(len(counts) * 0.9))],
            "max": counts[-1],
        }


# ════════════════════════════════════════════════════════════════════════════════
# §B. World-state model + Mandatory-trigger probabilities
# ════════════════════════════════════════════════════════════════════════════════
#
# Per scale_transitions §4.3.2: 8 Mandatory triggers. Per-season probabilities are
# calibrated below. These are MODELING ASSUMPTIONS pending real telemetry from
# campaign playtests.
#
# Calibration anchors:
#   - engine_v3.py revolts: ~5-15% of territories per season under stress (Strain ≥ 3).
#     Player is in 1 of 17 territories at any time → revolt-at-player-location p ≈ 0.05.
#   - Heresy investigations: rare event, faction-political — model as 0.03/season.
#   - Faction leader removal: NPC succession — engine_v3 averages ~1 succession/8-12 seasons
#     across 4 factions, but only player's faction triggers Mandatory → 0.02/season.
#   - Mass Battle at settlement: scales with ongoing campaigns. engine_v3 logs ~1 battle
#     per 2-4 seasons during conflict periods, ~30% of which involve a settlement in the
#     player's province → 0.07/season weighted average.
#   - Companion arc trigger: depends on companion count. Assume 2-3 companions, each with
#     ~10% per-season arc-progression chance → 0.04/season aggregate.
#   - Knot Partner crisis: depends on Knot count + NPC scar accumulation rate. Assume
#     1-2 active Knots, ~5% per-season crisis rate → 0.03/season.
#   - Stability Crisis: §4.3.2 hysteresis — fires once per Stab≤2 entry, re-arms after
#     Stab≥3 sustained 2 Accountings. Across a 40-season campaign, expect 1-3 events
#     → 0.05/season average, but heavily clustered.
#   - Rank Advancement Recognition: tied to Standing-rank crossings. Player progresses
#     through 7 standings over campaign — ~0.15/season early, ~0.05 late. Average 0.08.

@dataclass
class WorldState:
    season: int = 0
    player_standing: int = 1               # 0-7 ladder
    player_wounds: int = 0
    player_stamina: int = 5                # 0-5; 0 = Out of Breath
    player_knots: int = 1                  # active knots in player's territory count
    faction_stability: int = 4             # 1-7
    faction_stability_low_streak: int = 0  # consecutive Accountings at ≤2 (hysteresis)
    strain: int = 0                        # 0-10
    ci: int = 30                           # 0-100
    rs: int = 60                           # 0-100
    active_battles: int = 0
    rng: random.Random = field(default_factory=random.Random)

    def advance_world(self):
        """Tick the macro state. Drives mandatory-trigger probabilities."""
        # Strain creeps up on conflict, drops on peace.
        if self.active_battles > 0:
            self.strain = min(10, self.strain + 1)
        elif self.strain > 0:
            self.strain -= 1
        # CI advances slowly under Church pressure.
        self.ci = min(100, self.ci + self.rng.randint(0, 2))
        # RS decays per canonical -1/season baseline.
        self.rs = max(0, self.rs - 1)
        # Stability drifts with strain.
        if self.strain >= 5 and self.rng.random() < 0.3:
            self.faction_stability = max(1, self.faction_stability - 1)
        elif self.strain <= 2 and self.rng.random() < 0.15 and self.faction_stability < 7:
            self.faction_stability += 1
        # Hysteresis bookkeeping (ED-749).
        if self.faction_stability <= 2:
            self.faction_stability_low_streak = 0
        else:
            self.faction_stability_low_streak += 1
        # Battles resolve.
        self.active_battles = max(0, self.active_battles - 1)
        if self.rng.random() < 0.15:
            self.active_battles += 1

    def standing_modifier(self) -> int:
        """§6.2: +1 at Standing 4-5, +2 at Standing 6-7."""
        if self.player_standing >= 6: return 2
        if self.player_standing >= 4: return 1
        return 0

    def fatigue_modifier(self) -> int:
        """§6.2: -1 if Wounded (2+ wounds) or Out of Breath (Stamina 0)."""
        m = 0
        if self.player_wounds >= 2: m -= 1
        if self.player_stamina == 0: m -= 1
        return m


# 8 mandatory triggers per §4.3.2, plus knot bonus.
MANDATORY_TRIGGERS = [
    "settlement_revolt",
    "heresy_investigation_target",
    "faction_leader_removal",
    "mass_battle_at_settlement",
    "companion_arc_trigger",
    "knot_partner_crisis",
    "stability_crisis",
    "rank_advancement_recognition",
]

# §4.3.3: 5 World-State (Priority 1) triggers — always presented but can decline.
WORLDSTATE_TRIGGERS = [
    "clock_band_transition",
    "npc_conviction_crisis",
    "treaty_proposed_or_broken",
    "territory_control_change",
    "warden_emergency",
]


def fire_mandatory_triggers(ws: WorldState, persona: str) -> List[str]:
    """Returns list of mandatory triggers firing this season. ASSUMPTION-DRIVEN probabilities."""
    fired = []
    rng = ws.rng

    # Settlement Revolt — Order 0 in player's territory. Scales with strain.
    p_revolt = 0.05 + 0.03 * max(0, ws.strain - 3)
    if rng.random() < p_revolt: fired.append("settlement_revolt")

    # Heresy Investigation — depends on CI and player's faction (Church-aligned less likely target).
    p_heresy = 0.03 + 0.01 * (ws.ci // 30)
    if persona == "church_aligned": p_heresy *= 0.3
    if rng.random() < p_heresy: fired.append("heresy_investigation_target")

    # Faction Leader Removal — succession events
    p_succession = 0.02 + (0.02 if ws.faction_stability <= 2 else 0)
    if rng.random() < p_succession: fired.append("faction_leader_removal")

    # Mass Battle at Settlement — only if active_battles and player's province targeted
    if ws.active_battles > 0 and rng.random() < 0.30:
        fired.append("mass_battle_at_settlement")

    # Companion Arc Trigger — assume 2-3 companions, each ~10%/season
    p_companion = 0.04 + 0.02 * (1 if persona == "social" else 0)
    if rng.random() < p_companion: fired.append("companion_arc_trigger")

    # Knot Partner Crisis — depends on knot count
    p_knot = 0.03 * ws.player_knots
    if rng.random() < p_knot: fired.append("knot_partner_crisis")

    # Stability Crisis — hysteresis: requires Stab ≤ 2 AND streak == 0 (just entered)
    if ws.faction_stability <= 2 and ws.faction_stability_low_streak == 0:
        if rng.random() < 0.85:    # near-certain on first entry into low-stab
            fired.append("stability_crisis")

    # Rank Advancement — Standing crossings (rare; about ~7 over a campaign)
    p_rank = 0.08 if ws.player_standing < 5 else 0.04
    if ws.player_standing < 7 and rng.random() < p_rank:
        fired.append("rank_advancement_recognition")
        ws.player_standing += 1

    return fired


def fire_worldstate_triggers(ws: WorldState) -> List[str]:
    """Priority 1 triggers — presented but optional."""
    fired = []
    rng = ws.rng
    if ws.ci % 25 < 3 and rng.random() < 0.4: fired.append("clock_band_transition")
    if rng.random() < 0.10:                   fired.append("npc_conviction_crisis")
    if rng.random() < 0.06:                   fired.append("treaty_proposed_or_broken")
    if rng.random() < 0.12:                   fired.append("territory_control_change")
    if ws.rs <= 40 and rng.random() < 0.20:   fired.append("warden_emergency")
    return fired


# ════════════════════════════════════════════════════════════════════════════════
# §C. Trigger → System mapping + ASSUMPTION durations
# ════════════════════════════════════════════════════════════════════════════════
#
# Maps each trigger to a system_id + scope + estimated duration.
# Durations sourced from campaign_modes_v30 §12.3 TABLETOP timing and re-scaled for
# videogame mode — Personal halved (computer-paced not GM-paced), Strategic halved.
# THESE ARE PLACEHOLDERS until real measurement.

TRIGGER_PROFILE = {
    # (system_id, scope, base_minutes, sa_cost)
    "settlement_revolt":            ("combat",         "personal",    8,  1),
    "heresy_investigation_target":  ("social_contest", "relational",  10, 1),
    "faction_leader_removal":       ("strategic",      "peninsular",  6,  1),
    "mass_battle_at_settlement":    ("mass_battle",    "territorial", 14, 2),
    "companion_arc_trigger":        ("fieldwork",      "personal",    7,  1),
    "knot_partner_crisis":          ("social_contest", "relational",  6,  1),
    "stability_crisis":             ("social_contest", "relational",  9,  1),
    "rank_advancement_recognition": ("fieldwork",      "personal",    5,  1),
    # World-state Priority 1
    "clock_band_transition":        ("fieldwork",      "personal",    4,  1),
    "npc_conviction_crisis":        ("social_contest", "relational",  6,  1),
    "treaty_proposed_or_broken":    ("strategic",      "peninsular",  5,  1),
    "territory_control_change":     ("fieldwork",      "personal",    4,  1),
    "warden_emergency":             ("threadwork",     "personal",    7,  1),
    # Elective fillers — ambient opportunities
    "elective_fieldwork":           ("fieldwork",      "personal",    5,  1),
    "elective_social":              ("social_contest", "relational",  6,  1),
    "elective_strategic":           ("strategic",      "peninsular",  4,  1),
    "elective_combat":              ("combat",         "personal",    7,  1),
}


# ════════════════════════════════════════════════════════════════════════════════
# §D. Persona models — different player styles
# ════════════════════════════════════════════════════════════════════════════════

PERSONA_PROFILES = {
    # difficulty (Narrative/Normal/Hard), sa_base, slate_size, elective_taste
    "narrative_completionist":  ("narrative", 5, (4, 5), {"fieldwork": 0.4, "social_contest": 0.4, "strategic": 0.1, "combat": 0.1}),
    "normal_balanced":          ("normal",    4, (5, 7), {"fieldwork": 0.3, "social_contest": 0.3, "strategic": 0.2, "combat": 0.2}),
    "normal_combat_focused":    ("normal",    4, (5, 7), {"fieldwork": 0.1, "social_contest": 0.1, "strategic": 0.2, "combat": 0.6}),
    "hard_strategist":          ("hard",      3, (7, 9), {"fieldwork": 0.2, "social_contest": 0.2, "strategic": 0.5, "combat": 0.1}),
}


def gen_elective_slate(ws: WorldState, persona: str, slate_size_range: Tuple[int, int],
                       taste: Dict[str, float]) -> List[str]:
    """Generate the elective opportunity slate per player_agency §6.1."""
    n = ws.rng.randint(*slate_size_range)
    out = []
    for _ in range(n):
        # Weighted choice from taste
        choices = list(taste.keys())
        weights = [taste[c] for c in choices]
        pick = ws.rng.choices(choices, weights=weights, k=1)[0]
        if pick == "fieldwork":           out.append("elective_fieldwork")
        elif pick == "social_contest":    out.append("elective_social")
        elif pick == "strategic":         out.append("elective_strategic")
        elif pick == "combat":            out.append("elective_combat")
    return out


# ════════════════════════════════════════════════════════════════════════════════
# §E. Season runner — integrates substrate
# ════════════════════════════════════════════════════════════════════════════════

def run_season(ws: WorldState, persona: str, ks: KeyStore, st: SceneTimer):
    """One season: world ticks → triggers fire → slate built → player picks → telemetry emitted."""
    profile = PERSONA_PROFILES[persona]
    difficulty, sa_base, slate_size_range, taste = profile

    ws.advance_world()
    ws.season += 1

    # 1. Mandatory triggers (Priority 0) — cannot be declined except by overflow
    mandatory = fire_mandatory_triggers(ws, persona)

    # 2. World-state Priority 1 triggers
    p1 = fire_worldstate_triggers(ws)

    # 3. Elective slate (Priority 2-4)
    elective = gen_elective_slate(ws, persona, slate_size_range, taste)

    # 4. Compute SA budget per §6
    sa_budget = sa_base + ws.standing_modifier() + ws.fatigue_modifier()
    sa_budget = max(1, sa_budget)  # floor

    # 5. Player's pick order: Mandatory > P1 > elective. Overflow mandatory auto-resolves.
    sa_used = 0
    scenes_played: List[Tuple[str, str]] = []     # (trigger, "played"|"skipped")

    # Pay mandatory first
    for trig in mandatory:
        cost = TRIGGER_PROFILE[trig][3]
        if sa_used + cost <= sa_budget:
            scenes_played.append((trig, "played"))
            sa_used += cost
        else:
            scenes_played.append((trig, "skipped_mandatory_overflow"))   # auto-resolved

    # Then P1 — pick by random taste, skip rest
    for trig in p1:
        cost = TRIGGER_PROFILE[trig][3]
        if sa_used + cost <= sa_budget and ws.rng.random() < 0.6:
            scenes_played.append((trig, "played"))
            sa_used += cost
        else:
            scenes_played.append((trig, "skipped"))

    # Then elective — pick until budget exhausted
    for trig in elective:
        cost = TRIGGER_PROFILE[trig][3]
        if sa_used + cost <= sa_budget:
            scenes_played.append((trig, "played"))
            sa_used += cost
        else:
            scenes_played.append((trig, "skipped"))

    # 6. Emit Keys + advance synthetic wall clock
    seq = 0
    for trig, status in scenes_played:
        sys_id, scope, base_min, sa_cost = TRIGGER_PROFILE[trig]
        # Slate priority — mandatory=0, p1=1, elective=3
        if trig in MANDATORY_TRIGGERS:                 prio = 0
        elif trig in WORLDSTATE_TRIGGERS:              prio = 1
        else:                                          prio = 3

        scene_id = hashlib.sha256(f"{ws.season}|{seq}|{trig}|{ws.rng.random()}".encode()).hexdigest()[:12]
        seq += 1

        if status == "played":
            ks.emit("mechanical.scene_entered", {
                "scene_id": scene_id, "system_id": sys_id, "scope": scope,
                "sa_cost_estimated": sa_cost, "slate_priority": prio,
                "season_n": ws.season, "parent_scene_id": "", "stack_depth_after": 1,
            }, scope, "sim_director")
            # Advance wall by sampled minutes (lognormal-ish — ±25% jitter)
            elapsed_ms = int(base_min * 60_000 * (0.75 + ws.rng.random() * 0.5))
            st.advance_wall(elapsed_ms)
            ks.emit("mechanical.scene_exited", {
                "scene_id": scene_id, "sa_cost_actual": sa_cost,
                "outcome_class": ws.rng.choice(["success", "partial", "failure", "overwhelming"]),
                "ended_by": "player", "sufficient_scope": True,
            }, scope, "sim_director")
        else:  # skipped or skipped_mandatory_overflow
            ks.emit("mechanical.scene_skipped", {
                "scene_id": scene_id, "system_id": sys_id, "scope": scope,
                "slate_priority": prio, "season_n": ws.season,
                "reason": "mandatory_overflow" if "mandatory" in status else "abstract_resolve",
            }, scope, "sim_director")

    # 7. Stamina / wound recovery (simple)
    if ws.player_stamina < 5: ws.player_stamina += 1
    if ws.player_wounds > 0 and ws.rng.random() < 0.3: ws.player_wounds -= 1


# ════════════════════════════════════════════════════════════════════════════════
# §F. Run-many + Aggregate
# ════════════════════════════════════════════════════════════════════════════════

def run_one_campaign(persona: str, n_seasons: int, seed: int, out_dir: str) -> dict:
    """Run one campaign, write JSONL, return per-campaign summary."""
    rng = random.Random(seed)
    ws = WorldState(rng=rng)
    ks = KeyStore()
    campaign_id = f"{persona}_seed{seed}"
    session_id = f"sess_{seed}"
    jsonl_path = os.path.join(out_dir, f"{campaign_id}.jsonl")
    st = SceneTimer(ks, jsonl_path, campaign_id=campaign_id, session_id=session_id)

    for _ in range(n_seasons):
        run_season(ws, persona, ks, st)

    st.flush()
    records = st._records

    # Compute saturation: seasons where >=1 elective skipped or mandatory overflowed.
    sa_budget_base = PERSONA_PROFILES[persona][1]   # ignore standing mods for headline number
    seasons_saturated = 0
    seasons_mandatory_overflow = 0
    by_season: Dict[int, dict] = {}
    for r in records:
        s = r["season_n"]
        bs = by_season.setdefault(s, {"played": 0, "skipped": 0, "mandatory_overflow": 0,
                                      "mandatory_total": 0})
        if r["slate_priority"] == 0:
            bs["mandatory_total"] += 1
        if r["outcome_class"] == "skipped":
            bs["skipped"] += 1
            if r["slate_priority"] == 0:
                bs["mandatory_overflow"] += 1
        else:
            bs["played"] += 1
    for s, bs in by_season.items():
        if bs["skipped"] > 0: seasons_saturated += 1
        if bs["mandatory_overflow"] > 0: seasons_mandatory_overflow += 1

    return {
        "persona": persona,
        "seed": seed,
        "n_seasons": n_seasons,
        "log_hash": ks.log_hash(),
        "records": len(records),
        "per_system_minutes": TimeAggregator.per_system_minutes(records),
        "sa_consumption_by_system": TimeAggregator.sa_consumption_by_system(records),
        "time_per_sa_by_system": TimeAggregator.time_per_sa_by_system(records),
        "mandatory_zoom_rate": TimeAggregator.mandatory_zoom_rate(records),
        "seasons_saturated": seasons_saturated,
        "seasons_mandatory_overflow": seasons_mandatory_overflow,
        "sa_budget_base": sa_budget_base,
    }


def aggregate(results: List[dict]) -> dict:
    """Aggregate across runs, by persona."""
    by_persona: Dict[str, List[dict]] = {}
    for r in results:
        by_persona.setdefault(r["persona"], []).append(r)

    out: Dict[str, dict] = {}
    for persona, runs in by_persona.items():
        n = len(runs)
        # Per-system minutes — collect distribution per system
        sys_minutes: Dict[str, List[float]] = {}
        sys_sa: Dict[str, List[int]] = {}
        for run in runs:
            for sid, m in run["per_system_minutes"].items():
                sys_minutes.setdefault(sid, []).append(m)
            for sid, s in run["sa_consumption_by_system"].items():
                sys_sa.setdefault(sid, []).append(s)

        def stats(xs):
            if not xs: return {"n": 0, "mean": 0, "p50": 0, "p90": 0, "max": 0}
            xs_sorted = sorted(xs)
            return {
                "n": len(xs),
                "mean": round(statistics.mean(xs), 2),
                "p50": round(xs_sorted[len(xs_sorted) // 2], 2),
                "p90": round(xs_sorted[min(len(xs_sorted) - 1, int(len(xs_sorted) * 0.9))], 2),
                "max": round(xs_sorted[-1], 2),
            }

        # Mandatory zoom rate aggregated across all seasons of all runs
        all_mzr = [run["mandatory_zoom_rate"]["mean"] for run in runs]
        all_mzr_p90 = [run["mandatory_zoom_rate"]["p90"] for run in runs]
        all_mzr_max = [run["mandatory_zoom_rate"]["max"] for run in runs]

        seasons_total = sum(run["n_seasons"] for run in runs)
        sat_total = sum(run["seasons_saturated"] for run in runs)
        ovf_total = sum(run["seasons_mandatory_overflow"] for run in runs)

        out[persona] = {
            "n_runs": n,
            "seasons_total": seasons_total,
            "saturation_rate":         round(sat_total / seasons_total, 4),
            "mandatory_overflow_rate": round(ovf_total / seasons_total, 4),
            "mandatory_per_season_mean":  round(statistics.mean(all_mzr), 2),
            "mandatory_per_season_p90":   round(statistics.mean(all_mzr_p90), 2),
            "mandatory_per_season_max":   round(statistics.mean(all_mzr_max), 2),
            "minutes_by_system_per_run": {sid: stats(xs) for sid, xs in sys_minutes.items()},
            "sa_by_system_per_run":      {sid: stats(xs) for sid, xs in sys_sa.items()},
            "sa_budget_base":            runs[0]["sa_budget_base"],
        }
    return out


def report_human(agg: dict, n_seasons: int):
    print()
    print("=" * 78)
    print(f"TELEMETRY SUBSTRATE SIM — {n_seasons} seasons/campaign")
    print("=" * 78)
    for persona, p in agg.items():
        print(f"\n── {persona} (n={p['n_runs']}, base SA={p['sa_budget_base']}) ──")
        print(f"  saturation_rate (any skip):       {p['saturation_rate']*100:.1f}% of seasons")
        print(f"  mandatory_overflow (cannot fit):  {p['mandatory_overflow_rate']*100:.1f}% of seasons")
        print(f"  mandatory_zoom_ins / season:      mean={p['mandatory_per_season_mean']}  p90={p['mandatory_per_season_p90']}  max-observed={p['mandatory_per_season_max']}")
        print(f"  per-system minutes / campaign (mean[p90]):")
        for sid, s in sorted(p["minutes_by_system_per_run"].items(), key=lambda kv: -kv[1]["mean"]):
            print(f"    {sid:18s}  {s['mean']:6.1f} min  [p90 {s['p90']:6.1f}]   {s['n']} runs with system")
        print(f"  per-system SA / campaign (mean[p90]):")
        for sid, s in sorted(p["sa_by_system_per_run"].items(), key=lambda kv: -kv[1]["mean"]):
            print(f"    {sid:18s}  {s['mean']:6.1f} SA   [p90 {s['p90']:6.1f}]")


# ════════════════════════════════════════════════════════════════════════════════
# §G. Main
# ════════════════════════════════════════════════════════════════════════════════

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--campaigns", type=int, default=100)
    ap.add_argument("--seasons", type=int, default=40)
    ap.add_argument("--out_dir", default="/home/claude/sim_telemetry_jsonl")
    ap.add_argument("--summary_path", default="/home/claude/sim_telemetry_results.json")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    print(f"[sim] {len(PERSONA_PROFILES)} personas × {args.campaigns} campaigns × {args.seasons} seasons")
    print(f"[sim] = {len(PERSONA_PROFILES) * args.campaigns} total campaigns / "
          f"{len(PERSONA_PROFILES) * args.campaigns * args.seasons} season-runs")

    all_results: List[dict] = []
    for persona in PERSONA_PROFILES.keys():
        for run in range(args.campaigns):
            seed = args.seed + run * 1000 + hash(persona) % 997
            r = run_one_campaign(persona, args.seasons, seed, args.out_dir)
            all_results.append(r)
        print(f"[sim] {persona}: {args.campaigns} campaigns done")

    agg = aggregate(all_results)
    with open(args.summary_path, "w") as f:
        json.dump({
            "config": {"campaigns": args.campaigns, "seasons": args.seasons, "seed": args.seed},
            "by_persona": agg,
        }, f, indent=2)

    report_human(agg, args.seasons)
    print(f"\n[sim] summary: {args.summary_path}")
    print(f"[sim] jsonl:   {args.out_dir}/")


if __name__ == "__main__":
    main()
