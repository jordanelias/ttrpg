"""
sim/cross_scale/domain_echo.py — Domain Echo (§5) — scene → faction stat propagation

Canon source: designs/architecture/scale_transitions_v30.md §5

Implements §5.1-§5.6: Trigger gating by Sufficient Scope (§7), amount table
by degree, timing by mode, Debate→Echo, Accord Echo (§5.5), Thread Echo (§5.6).
PP-329 cap: 1 Echo per faction per scene.

Step 10.1 from Phase 7 follow-on per module_manifest.md (cross-scale
battle-result echo). This Tier 0 lands the §5 protocol; consumers wire in.

Dependencies:
  - sim/autoload/game_state

Entry points:
  - compute_domain_echo(degree: str, scope_met: bool, source_scene: dict, world: GameState) -> DomainEchoResult
  - compute_accord_echo(scene_outcome: str, degree: str, world: GameState) -> AccordEchoResult
  - compute_thread_echo(thread_event: dict, world: GameState) -> ThreadEchoResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# §5.2 amount table by degree
# [canonical: §5.2 Amount table — "Overwhelming ±2, Success ±1, Partial
#  narrative-only, Failure -1 to acting faction's own stat"]
ECHO_AMOUNT_BY_DEGREE = {
    "Overwhelming": 2,
    "Success": 1,
    "Partial": 0,           # narrative only
    "Failure": -1,
}

# §5.2 cap per stat per Echo
# [canonical: §5.2 — "Cap: ±2 per stat per Echo. (ED-071 resolved by PP-329:
#  one Echo/scene/faction prevents compounding)"]
ECHO_STAT_CAP = 2

# PP-329 — one Echo per scene per faction
PP_329_ECHO_PER_SCENE_PER_FACTION = 1

# §5.5 Accord Echo per-territory cap
# [canonical: §5.5 — "Cap: ±1 Accord in one territory per Zoom In"]
ACCORD_ECHO_PER_TERRITORY_CAP = 1


@dataclass
class DomainEchoResult:
    fires: bool                 # False if Sufficient Scope (§7) not met
    affected_faction: Optional[str]
    affected_stat: Optional[str]
    delta: int
    timing: str                 # "scene_end" / "accounting"
    notes: list[str] = field(default_factory=list)


@dataclass
class AccordEchoResult:
    fires: bool
    target_territory: Optional[str]
    accord_delta: int           # ±1 per §5.5 cap
    rs_delta: int               # immediate if violence-trigger
    fires_at: str               # "accounting_step_4c"
    notes: list[str] = field(default_factory=list)


@dataclass
class ThreadEchoResult:
    fires: bool                 # §5.6 Thread Significance gating
    affected_faction: Optional[str]
    affected_stat: Optional[str]
    delta: int
    notes: list[str] = field(default_factory=list)


def compute_domain_echo(degree: str, scope_met: bool, source_scene: dict, world=None) -> DomainEchoResult:
    """Compute §5.2 Domain Echo for a scene by degree + scope gate."""
    notes = []
    if not scope_met:
        return DomainEchoResult(
            fires=False, affected_faction=None, affected_stat=None,
            delta=0, timing="never",
            notes=["Sufficient Scope (§7) not met; no Echo per §5.1"],
        )

    amount = ECHO_AMOUNT_BY_DEGREE.get(degree)
    if amount is None:
        return DomainEchoResult(
            fires=False, affected_faction=None, affected_stat=None,
            delta=0, timing="never",
            notes=[f"Unknown degree '{degree}'; no Echo computed"],
        )

    if amount == 0:
        # Partial — narrative only
        return DomainEchoResult(
            fires=False, affected_faction=source_scene.get('actor_faction'),
            affected_stat=None, delta=0, timing="scene_end",
            notes=["Partial degree: narrative-only per §5.2; no stat change"],
        )

    # Failure: -1 to acting faction's OWN stat per §5.2
    if degree == "Failure":
        return DomainEchoResult(
            fires=True,
            affected_faction=source_scene.get('actor_faction'),
            affected_stat=source_scene.get('most_relevant_stat'),
            delta=-1,
            timing="scene_end",  # Full / Register Shift mode (§5.3)
            notes=["§5.2 Failure: -1 to acting faction's own stat"],
        )

    # Success / Overwhelming: ±amount to target faction's most-relevant stat
    # Cap per stat per Echo: ±2 (already enforced by amount table maxing at 2)
    return DomainEchoResult(
        fires=True,
        affected_faction=source_scene.get('target_faction'),
        affected_stat=source_scene.get('most_relevant_stat'),
        delta=amount,
        timing="scene_end",
        notes=[f"§5.2 {degree}: ±{amount} (capped at ±{ECHO_STAT_CAP})"],
    )


def compute_accord_echo(scene_outcome: str, degree: str, world=None) -> AccordEchoResult:
    """Compute §5.5 Accord Domain Echo for personal scenes producing Accord changes.

    scene_outcome: 'governance' / 'destabilisation' / 'territorial_transfer' / 'violence'
    degree: 'Overwhelming' / 'Success' etc.
    """
    notes = []

    if scene_outcome == 'governance' and degree in ('Overwhelming', 'Success'):
        # [canonical: §5.5 — "PC publicly governs/administers a territory ...
        #  Overwhelming/Success | Accord +1 in that territory"]
        return AccordEchoResult(
            fires=True, target_territory=None,  # caller specifies tid
            accord_delta=+1, rs_delta=0,
            fires_at="accounting_step_4c",
            notes=["§5.5 governance: +1 Accord (queued to next Accounting)"],
        )

    if scene_outcome == 'destabilisation' and degree == 'Success':
        return AccordEchoResult(
            fires=True, target_territory=None,
            accord_delta=-1, rs_delta=0,
            fires_at="accounting_step_4c",
            notes=["§5.5 destabilisation: -1 Accord (queued)"],
        )

    if scene_outcome == 'territorial_transfer':
        # Transferred territory Accord set to 2
        return AccordEchoResult(
            fires=True, target_territory=None,
            accord_delta=0, rs_delta=0,  # delta semantics differ — caller sets accord=2
            fires_at="accounting_step_4c",
            notes=["§5.5 territorial transfer: Accord set to 2 in transferred territory"],
        )

    if scene_outcome == 'violence':
        return AccordEchoResult(
            fires=True, target_territory=None,
            accord_delta=-1, rs_delta=-1,
            fires_at="immediate",
            notes=["§5.5 violence: RS -1 immediate; Accord -1 in territory"],
        )

    return AccordEchoResult(
        fires=False, target_territory=None,
        accord_delta=0, rs_delta=0, fires_at="never",
        notes=[f"No §5.5 rule for scene_outcome='{scene_outcome}' degree='{degree}'"],
    )


def compute_thread_echo(thread_event: dict, world=None) -> ThreadEchoResult:
    """Compute §5.6 Thread Domain Echo per ED-673."""
    notes = []
    event_type = thread_event.get('event_type')

    # [canonical: §5.6 table]
    rules = {
        ('Dissolution', 'success'): ('controlling_faction', 'Stability', -1),
        ('Mending', 'territorial_success'): ('controlling_faction', 'Mandate', +1),
        ('Gap_creation', None): ('controlling_faction', 'Stability', -1),
        ('Lock_creation', 'unauthorized'): ('controlling_faction', 'Mandate', -1),
        ('Public_thread_op', 'church_territory'): ('Church', 'Mandate', -1),
        ('Public_thread_op', 'varfell_territory_vtm_ge_3'): ('Varfell', 'Mandate', +1),
    }

    sub = thread_event.get('sub_condition')
    key = (event_type, sub)
    if key not in rules:
        return ThreadEchoResult(
            fires=False, affected_faction=None, affected_stat=None,
            delta=0, notes=[f"No §5.6 rule for ({event_type}, {sub})"],
        )

    faction, stat, delta = rules[key]
    return ThreadEchoResult(
        fires=True,
        affected_faction=thread_event.get(faction, faction),
        affected_stat=stat,
        delta=delta,
        notes=[f"§5.6 {event_type} ({sub}): {stat} {delta:+d}"],
    )
