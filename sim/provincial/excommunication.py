"""
sim/provincial/excommunication.py — Church Excommunication faction-unique action

Canon source:
  - designs/provincial/faction_canon_v30.md §9 (Tactic / Unique Action Overview)
  - designs/provincial/faction_canon_v30.md (Church faction sheet — Tactic / Unique Actions)
  - systems/social_contest/social_contest_v30.md §7.1 (Excommunication Tribunal, ED-625)
Game Design constraints applicable: GD-2 (mandatory-before-stochastic action selection)
Status: [PROVISIONAL — Phase 5/9 integration 2026-05-17. §9 strategic-scale
         action wrapping a single-roll abstraction of the §7.1 Tribunal procedure.
         Outcomes blend §9 base effects with §7.1 escalated effects when formal
         grounds (CI >= 40 + Church.L >= 4) are met.]

Dependencies:
  - sim/personal/tribunal — §7.1 procedural resolution
  - sim/autoload/dice_engine — Degree enum
"""
from __future__ import annotations

from dataclasses import dataclass, field

from sim.personal import tribunal
from engine.autoload.dice_engine import Degree


# ── Ledger-cited constants ────────────────────────────────────────────────────

# Canon: faction_canon_v30.md §9 — "Requires Church L >= 3"
EXCOMM_PREREQ_L_LIGHT = 3  # [canonical: faction_canon_v30.md §9]

# Canon: §9 outcomes (base strategic effects, applied universally).
# GRANULAR CONVENTION (v17 mc_v17.py:530, 531): canonical "L -1" -> adjust('L', delta * MULTS[L]) = adjust('L', -20).
# All *_L_DELTA constants below are in granular units (canonical_stat_units * MULTS[L]).
# MULTS[L] = 20 per params/factions.md.
_MULTS_L = 20  # [canonical: params/factions.md §Stat multipliers]
EXCOMM_OUTCOME_OW_TARGET_L_DELTA = -1 * _MULTS_L  # canonical "-1 L" [faction_canon §9]
EXCOMM_OUTCOME_SUCCESS_TARGET_L_DELTA = -1 * _MULTS_L  # canonical "-1 L" [faction_canon §9]
EXCOMM_OUTCOME_FAIL_CHURCH_L_DELTA = -1 * _MULTS_L  # canonical "Church L -1" [faction_canon §9]
EXCOMM_OUTCOME_FAIL_TARGET_L_DELTA = 1 * _MULTS_L  # canonical "+1 L sympathy" [faction_canon §9]

# Canon: social_contest §7.1 — Faction-target consequences on success
# "Mandate -2; all Church Domain Actions vs faction Ob -1; CI +3."
# §7.1 escalation = additional -1 L on top of §9 base (total -2 stat-tier).
EXCOMM_FORMAL_ADDITIONAL_L_DELTA = -1 * _MULTS_L  # additional; total -2 stat-tier
EXCOMM_FORMAL_CI_DELTA = 3  # CI is 0-100 direct (not stat-tier) [social_contest §7.1]

# CI cap — peninsular_strain track is conventionally 0-100
CI_CEILING = 100.0  # [canonical: faction_layer_v30 + peninsular accounting cap]

# Granular conversion: L stat multiplier (see params/factions.md)
# Faction.adjust applies granular_delta / MULTS[stat] to stat. A "L -1" effect
# in canon means 1 granular point at the stat level, i.e. adjust('L', -1).
# This is the v18 convention used throughout faction_action.py.

# Senator Inward slot — Crown Initiative documentation states this slot is
# "1x per season; shares no slot with Senator Outward". Excommunication is
# the Church equivalent unique action. Cooldown handled via faction.senator_inward_used.


# ── Result type ───────────────────────────────────────────────────────────────

@dataclass
class ExcommResult:
    """Outcome of one Excommunication attempt."""
    status: str  # 'invalid_prereq' | 'invalid_no_target' | 'resolved'
    degree: Degree | None = None
    target_name: str | None = None
    formal_grounds: bool = False
    tribunal_pool: int = 0
    tribunal_ob: float = 0.0
    tribunal_net: int = 0
    effects_applied: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


# ── Action entry point ────────────────────────────────────────────────────────

def attempt_excommunication(church, target_faction, world, rng) -> ExcommResult:
    """Church attempts to excommunicate `target_faction`.

    Resolves via tribunal.run_excommunication_tribunal. Outcomes per §9 base
    + §7.1 escalated effects when formal grounds met.

    Prereq (§9 minimum): Church.L >= 3.
    Formal grounds (§7.1): CI >= 40 AND Church.L >= 4 -> escalated effects.
    """
    # Prerequisite — light §9 gate
    # Canon: faction_canon §9 "Requires Church L >= 3"
    if church.L < EXCOMM_PREREQ_L_LIGHT:
        return ExcommResult(
            status='invalid_prereq',
            notes=[f"Church.L {church.L:.2f} < {EXCOMM_PREREQ_L_LIGHT} (§9 minimum)"],
        )

    if target_faction is None or target_faction.name == church.name:
        return ExcommResult(
            status='invalid_no_target',
            notes=["No valid target faction"],
        )

    if not getattr(target_faction, 'parliamentary', True):
        return ExcommResult(
            status='invalid_no_target',
            target_name=target_faction.name,
            notes=["Target is non-parliamentary (cannot be excommunicated)"],
        )

    # Already-excommunicated targets cannot be re-excommunicated this season
    # (Canon: §9 "Reversal: Grand Debate (5 exchanges) or new Confessor"
    # — excomm is a state; re-applying is no-op.)
    if getattr(target_faction, 'excommunicated', False):
        return ExcommResult(
            status='invalid_no_target',
            target_name=target_faction.name,
            notes=[f"{target_faction.name} already excommunicated"],
        )

    # Run tribunal procedure
    tres = tribunal.run_excommunication_tribunal(
        accused=target_faction,
        church=church,
        world=world,
        rng=rng,
    )

    result = ExcommResult(
        status='resolved',
        degree=tres.degree,
        target_name=target_faction.name,
        formal_grounds=tres.formal_grounds,
        tribunal_pool=tres.pool_size,
        tribunal_ob=tres.ob,
        tribunal_net=tres.net,
        notes=list(tres.notes),
    )

    # Apply §9 base outcomes
    deg = tres.degree
    if deg in (Degree.OVERWHELMING, Degree.SUCCESS):
        # §9: target faction L -1 (canonical "1 stat-tier", granular -20)
        target_faction.adjust('L', EXCOMM_OUTCOME_OW_TARGET_L_DELTA)
        target_faction.excommunicated = True
        result.effects_applied.append(
            f"{target_faction.name}.L {EXCOMM_OUTCOME_OW_TARGET_L_DELTA/_MULTS_L:+.1f} stat-tier "
            f"(granular {EXCOMM_OUTCOME_OW_TARGET_L_DELTA:+d}) [§9 base]"
        )
        result.effects_applied.append(f"{target_faction.name}.excommunicated = True")

        # §9 Overwhelming-only effects (Circles strip, Rep -1): not modeled in v18 schema
        if deg == Degree.OVERWHELMING:
            result.notes.append(
                "[PROVISIONAL] §9 Overwhelming additional effects (Circles stripped, "
                "Reputation -1) not modeled — v18 schema gap"
            )

        # §7.1 escalation when formal grounds met
        if tres.formal_grounds:
            target_faction.adjust('L', EXCOMM_FORMAL_ADDITIONAL_L_DELTA)
            result.effects_applied.append(
                f"{target_faction.name}.L {EXCOMM_FORMAL_ADDITIONAL_L_DELTA/_MULTS_L:+.1f} stat-tier "
                f"[§7.1 escalation, total -2.0]"
            )
            old_ci = world.clocks.get('CI', 0.0)
            # [2026-05-20 migration] route through ci_track.apply_ci_delta — single
            # canonical surface for CI arithmetic. Was: inline ceiling clamp.
            from sim.peninsular.ci_track import apply_ci_delta
            new_ci = apply_ci_delta(EXCOMM_FORMAL_CI_DELTA,
                                    source=f"excommunication §7.1 formal",
                                    world=world)
            result.effects_applied.append(
                f"world.clocks.CI {old_ci:.1f} -> {new_ci:.1f} (§7.1 +{EXCOMM_FORMAL_CI_DELTA})"
            )
            result.notes.append(
                "[PROVISIONAL] §7.1 'Church Domain Actions vs faction Ob -1' not modeled — "
                "v18 schema gap"
            )

    elif deg == Degree.FAILURE:
        # §9 Failure: Church L -1; target +1 (sympathy martyr)
        church.adjust('L', EXCOMM_OUTCOME_FAIL_CHURCH_L_DELTA)
        target_faction.adjust('L', EXCOMM_OUTCOME_FAIL_TARGET_L_DELTA)
        result.effects_applied.append(
            f"{church.name}.L {EXCOMM_OUTCOME_FAIL_CHURCH_L_DELTA/_MULTS_L:+.1f} stat-tier [§9 failure]"
        )
        result.effects_applied.append(
            f"{target_faction.name}.L {EXCOMM_OUTCOME_FAIL_TARGET_L_DELTA/_MULTS_L:+.1f} stat-tier "
            f"[§9 sympathy]"
        )

    else:
        result.notes.append("Partial degree: no L mutation per §9 (Partial absent from table)")

    return result


def select_excommunication_target(church, world, rng):
    """Pick an Excommunication target for the Church faction.

    Heuristic: highest-L non-Church parliamentary, not-already-excommunicated.
    GD-2 mandatory threat-response candidate (current strategic AI is stochastic;
    will tighten when Phase 8/9 strategic AI lands).
    """
    candidates = [
        f for fn, f in world.factions.items()
        if fn != church.name
        and getattr(f, 'parliamentary', True)
        and not getattr(f, 'excommunicated', False)
        and len(f.territories) > 0
    ]
    if not candidates:
        return None
    # Highest L first (the most institutionally weighty rival)
    candidates.sort(key=lambda f: f.L, reverse=True)
    return candidates[0]
