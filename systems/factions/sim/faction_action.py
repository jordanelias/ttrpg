"""
systems/factions/sim/faction_action.py — Faction action selection + resolution

Canon source: mc_v17.py faction_take_action; GD-2 (mandatory before stochastic)
Game Design constraints applicable: GD-1, GD-2
Status: [CANONICAL — Phase 2 implementation 2026-05-17; Phase 5/9 faction-unique
         dispatch wired 2026-05-17]
[PRE-LPS-1 / PORT-BLOCKING — ED-FA-0004, 2026-07-07: this module's scalar-L reads and
 string-label da_outcome emission are the pre-LPS-1 SUPERSEDED oracle (no per-settlement L/PS,
 no da.* Key plumbing — C-FA-1). Do NOT port as canon-conformant until ED-FA-0004 (Stratum B).]

v17 port: probabilistic action mix (M7_ASSUMPTION_SIX).
Historically the 30/35/20/15 (unique/Conquest/Muster/Govern) vector was a FIXED, uncited prior.
ED-FA-0012 (FA-5, 2026-07-08) retires the fixed vector: the 30/35/20/15 numbers survive only as the
PRIOR base weights, re-weighted by faction state BEFORE the draw and renormalized, so the mix
degenerates to the old vector in a neutral state. Grounding: Levy 1983 (a high-war baseline is
period-correct — the fix is *conditioning* the mix on state, not pacifying it); Blainey 1973 (war
onset tracks perceived relative power → Conquest keys off a mil-advantage signal); Olson 1993
(stationary-bandit incentive to govern held land → Govern keys off undergoverned share).

Dependencies:
  - sim/autoload/game_state
  - systems/settlements/sim/adjacency
  - systems/factions/sim/crown_initiative (Phase 5/9)
  - systems/factions/sim/excommunication (Phase 5/9)
  - systems/factions/sim/absolution (Phase 5/9)
  - systems/factions/sim/council_solmund (Phase 5/9)
  - systems/factions/sim/parliamentary_action (ED-SC-0007 mechanism; wired here per ED-FA-0012 fallback)
"""
from __future__ import annotations

import math
from engine.autoload.game_state import MULTS, ALL_PLAYABLE_15
from systems.settlements.sim.adjacency import ADJACENCY
from systems.factions.sim import crown_initiative
from systems.factions.sim import excommunication
from systems.factions.sim import absolution
from systems.factions.sim import council_solmund
from systems.factions.sim import parliamentary_action

# ── ED-FA-0012 (FA-5): state-conditioned action mix — PRIOR (base) weights ─────────────────────
# The retired M7_ASSUMPTION_SIX fixed vector, kept ONLY as the neutral-state prior. In a neutral
# state (no valid conquest target, no mil advantage, no undergoverned share, no threat) all three
# state multipliers below equal 1.0, so these renormalize back to exactly 0.30/0.35/0.20/0.15.
# [canonical: faction_action.py M7_ASSUMPTION_SIX prior; re-grounded ED-FA-0012 (FA-5)]
BASE_W_UNIQUE = 0.30      # [canonical: M7_ASSUMPTION_SIX faction-unique share, ED-FA-0012 prior]
BASE_W_CONQUEST = 0.35    # [canonical: M7_ASSUMPTION_SIX Conquest share, ED-FA-0012 prior]
BASE_W_MUSTER = 0.20      # [canonical: M7_ASSUMPTION_SIX Muster share, ED-FA-0012 prior]
BASE_W_GOVERN = 0.15      # [canonical: M7_ASSUMPTION_SIX Govern share, ED-FA-0012 prior]

# [SEED — ED-FA-0012 (FA-5): Blainey-1973 "war tracks relative power" coefficient split. Conquest is
#  nudged up by (a) whether a takeable target even exists and (b) a graded mil-advantage signal, each
#  worth at most +0.5× the base weight. The exact 0.5/0.5 split is a defensible round default, not a
#  fitted value — revisable, flagged SEED. canonical: designs/audit/2026-07-08-.../fa_se_...v1.md FA-5]
CONQUEST_TARGET_COEF = 0.5   # [canonical: ED-FA-0012 (FA-5) Conquest weight — target-exists term, SEED]
CONQUEST_MILADV_COEF = 0.5   # [canonical: ED-FA-0012 (FA-5) Conquest weight — mil-advantage term, SEED]

# [SEED — ED-FA-0012 (FA-5): "undergoverned" = own held territory whose Accord sits below this
#  threshold. 4.0 is canon Accord bucket boundary "2" (ACCORD_MAP[2]=4.0, game_state) — a settlement
#  under bucket 2 is materially discontent. Threshold is a clean canon-aligned SEED default.]
LOW_ACCORD_SEED = 4.0        # [canonical: game_state ACCORD_MAP bucket-2 boundary; ED-FA-0012 (FA-5) SEED]

# ── ED-FA-0009 (FA-2): Muster as a fiscal-military purchase ─────────────────────────────────────
# The military enterpriser (Redlich 1964, the Wallenstein/Mansfeld contractor model; Tilly 1990,
# coercion-and-capital) is paid REGARDLESS of the levy's success — raising troops is a purchase, not
# a wager. So Muster costs Wealth up front, every attempt, and money buys pool (floor(W/2) extra dice)
# rather than the old "free unless you fail" inversion.
MUSTER_WEALTH_COST = 1       # [canonical: Redlich 1964 (military-enterpriser); Tilly 1990 — ED-FA-0009 (FA-2)]
MUSTER_WEALTH_TO_POOL_DIV = 2  # [canonical: ED-FA-0009 (FA-2) — pool = Mil + floor(W/2), money raises troops]

# ── ED-FA-0013 (FA-6 a/b): Terms-vs-Storm fork at conquest ──────────────────────────────────────
# Grotius, De iure belli ac pacis (1625) Book III + Parker 1994 (breach/chamade convention): a
# garrison that surrenders on terms keeps the honors of war and the town is spared; a garrison that
# forces the storm forfeits that protection. Terms is strictly lighter on Accord/Legitimacy.
ACCORD_TERMS = -10           # [canonical: settlement_layer_v30 §5.1 FA-6 branch (a) "lighter Accord"; Grotius III / Parker 1994 — ED-FA-0013]
ACCORD_STORM = -25           # [canonical: settlement_layer_v30 §5.1 FA-6 branch (b) storm = existing baseline — ED-FA-0013]
# §5.3 Entry Terms (ED-SE-0011): a "surrender on terms" transfer makes Confirm Privileges the natural
# fork, which seeds the new settlement's Legitimacy at 3 (vs Impose Administration's 1). Do NOT invent
# a different number — this is the doc's exact Confirm-Privileges seed.
ENTRY_TERMS_CONFIRM_L_SEED = 3  # [canonical: settlement_layer_v30 §5.3 Entry Terms — "Confirm Privileges … L seeds 3" (ED-SE-0011)]

# Minimum Military to open a conquest at all (existing v17 gate, preserved).
CONQUEST_MIN_MIL = 3.0       # [canonical: faction_action.py v17 conquest gate — Mil >= 3 to attack]

# Sentinel the _try_* dispatch convention returns when an action is unavailable (fall through).
_NOOP = 'invalid'


def _successes(pool: float, rng) -> int:
    """Strategic-scale roll: d6 >= 4 per die (v17 convention, M3 compatible)."""
    if pool <= 0:
        return 0
    return sum(1 for _ in range(int(pool)) if rng.randint(1, 6) >= 4)  # [canonical: v17 strategic-scale resolution — d6, success on >=4 per die (M3)]


def _degree(net: int) -> str:
    if net >= 3:
        return 'Overwhelming'
    elif net >= 1:
        return 'Success'
    elif net == 0:
        return 'Partial'
    return 'Failure'


def _conquest_targets(faction, world) -> list:
    """Adjacent, enemy-held territories this faction could attack.

    Shared by `_try_conquest` (target selection) and `faction_take_action`'s state-conditioned
    Conquest weight (ED-FA-0012, FA-5) so the two never drift on what "a valid target" means.
    Neutral (owner=None) territories are NOT conquest targets — matches the v17 predicate.

    [hash-seed fix 2026-05-20] sort before use — `adj` is built from ADJACENCY set-literals whose
    iteration order depends on PYTHONHASHSEED; sorting collapses that into a deterministic list.
    """
    adj = set()
    for tid in faction.territories:
        adj |= ADJACENCY.get(tid, set())
    return sorted(tid for tid in adj
                  if tid in world.territories
                  and world.territories[tid].owner not in (faction.name, None))


def _mil_advantage_signal(faction, world, targets) -> float:
    """[SEED — ED-FA-0012 (FA-5), Blainey 1973] Graded 0–1 signal of this faction's Military edge
    over the factions that own its conquest targets.

    Heuristic (defensible, not fitted): relative advantage of faction.Mil over the MEAN Mil of the
    distinct target-owning factions, clamped to [0, 1]. A faction with no edge (or behind) reads 0;
    roughly double the mean enemy Mil saturates at 1. No RNG consumed — pure state read.
    [canonical: ED-FA-0012 (FA-5) mil-advantage term; Blainey 1973]
    """
    if not targets:
        return 0.0
    owners = {world.territories[t].owner for t in targets}
    enemy_mils = [world.factions[o].Mil for o in owners if o in world.factions]
    if not enemy_mils:
        return 0.0
    mean_enemy = sum(enemy_mils) / len(enemy_mils)
    if mean_enemy <= 0:
        return 1.0
    return max(0.0, min(1.0, (faction.Mil - mean_enemy) / mean_enemy))


def _undergoverned_share(faction, world) -> float:
    """[SEED — ED-FA-0012 (FA-5), Olson 1993] Share of this faction's OWN held territories whose
    Accord sits below LOW_ACCORD_SEED — the stationary bandit's incentive to invest in held land.
    Returns 0.0 when the faction holds nothing. No RNG consumed.
    [canonical: ED-FA-0012 (FA-5) Govern weight; Olson 1993 stationary-bandit]
    """
    own = [world.territories[t] for t in faction.territories
           if t in world.territories and world.territories[t].owner == faction.name]
    if not own:
        return 0.0
    low = sum(1 for t in own if t.accord < LOW_ACCORD_SEED)
    return low / len(own)


def _threat_signal(faction, world) -> float:
    """[SEED — ED-FA-0012 (FA-5)] 1.0 if any territory adjacent to this faction is held by a faction
    with strictly higher Military than this one (a proximate military threat worth mustering against),
    else 0.0. No RNG consumed — pure state read.
    [canonical: ED-FA-0012 (FA-5) Muster weight — proximate-threat term]
    """
    adj = set()
    for tid in faction.territories:
        adj |= ADJACENCY.get(tid, set())
    for tid in adj:
        t = world.territories.get(tid)
        if t and t.owner and t.owner != faction.name and t.owner in world.factions:
            if world.factions[t.owner].Mil > faction.Mil:
                return 1.0
    return 0.0


def faction_take_action(faction, world, rng) -> str:
    """Select and execute one action for a faction this season.

    GD-2: mandatory threat-response before stochastic selection.
    ED-FA-0012 (FA-5): the four action buckets' PRIOR weights (30/35/20/15, M7_ASSUMPTION_SIX) are
    re-weighted by faction state BEFORE the single selection draw, then renormalized to sum 1.0, so
    the cumulative-threshold dispatch below is identical in structure to v17 — only the boundaries
    move. In a neutral state the mix is exactly the old 30/35/20/15. Grounding: Levy 1983 / Blainey
    1973 / Olson 1993 (see module header). Phase 5/9: the unique slot routes to faction-unique
    actions per faction.name (and, per ED-FA-0012, falls back to a Parliamentary Censure).

    Signals below consume NO RNG; the ONLY draw is `roll = rng.random()`, exactly as in v17 — so the
    only campaign-level RNG shift is downstream, from which bucket the moved boundary selects.
    """
    # ── State signals (RNG-free) ────────────────────────────────────────────────────────────────
    targets = _conquest_targets(faction, world)
    has_target = 1.0 if (targets and faction.Mil >= CONQUEST_MIN_MIL) else 0.0  # [canonical: ED-FA-0012 (FA-5) target-exists indicator]
    mil_adv = _mil_advantage_signal(faction, world, targets)
    deficit = _undergoverned_share(faction, world)
    threat = _threat_signal(faction, world)

    # ── State multipliers (all = 1.0 in a neutral state → degenerate to the prior vector) ────────
    conquest_mult = 1.0 + CONQUEST_TARGET_COEF * has_target + CONQUEST_MILADV_COEF * mil_adv  # [canonical: ED-FA-0012 (FA-5); Blainey 1973]
    govern_mult = 1.0 + deficit    # [canonical: ED-FA-0012 (FA-5); Olson 1993 stationary-bandit]
    muster_mult = 1.0 + threat     # [canonical: ED-FA-0012 (FA-5) proximate-threat term]

    # ── Re-weight the PRIOR base weights and renormalize to a probability vector ──────────────────
    w_unique = BASE_W_UNIQUE
    w_conquest = BASE_W_CONQUEST * conquest_mult
    w_muster = BASE_W_MUSTER * muster_mult
    w_govern = BASE_W_GOVERN * govern_mult
    total = w_unique + w_conquest + w_muster + w_govern
    w_unique /= total
    w_conquest /= total
    w_muster /= total
    w_govern /= total

    # Cumulative thresholds — same dispatch order/fall-through as v17 (unique → Conquest → Muster →
    # Govern). In a neutral state cum_unique=0.30, cum_conquest=0.65, cum_muster=0.85 (the old mix).
    cum_unique = w_unique
    cum_conquest = cum_unique + w_conquest
    cum_muster = cum_conquest + w_muster

    roll = rng.random()

    # Faction-unique slot (Phase 5/9 dispatch; ED-FA-0012 Parliamentary fallback inside).
    if roll < cum_unique:
        unique_result = _try_faction_unique(faction, world, rng)
        if unique_result != _NOOP:
            return unique_result
        # fall through to Conquest if faction-unique unavailable

    # Conquest.
    if roll < cum_conquest:
        result = _try_conquest(faction, world, rng)
        if result != _NOOP:
            return result

    # Muster.
    if roll < cum_muster:
        result = _try_muster(faction, world, rng)
        if result != _NOOP:
            return result

    # Govern (fallback).
    return _try_govern(faction, world, rng)


def _try_faction_unique(faction, world, rng) -> str:
    """Phase 5/9 dispatch — faction-unique action routing by faction.name, with a universal
    Parliamentary-Censure fallback (ED-FA-0012).

    Crown: Crown Initiative (3 modes via select_initiative_mode heuristic).
    Church: picked by situational priority (Excommunication → Council → Absolution).
    Varfell/Hafenmark: no faction-specific unique action yet (Pass 2d/2e BLOCKED).

    ED-FA-0012 fallback: whenever a faction's OWN unique logic falls through to 'invalid' — including
    Crown/Church when their priority chains find nothing, and always for Varfell/Hafenmark — the
    faction attempts a Parliamentary Censure (parliamentary_action.propose_censure) if it is
    parliamentary-eligible. This reuses the EXISTING 30%-prior unique slot rather than inventing a new
    bucket (minimal-invention integration point). propose_censure self-gates on GD-3 + the §5.4
    proposer-minimum and returns the same '{_NOOP}' sentinel when unavailable.
    """
    specific = _faction_specific_unique(faction, world, rng)
    if specific != _NOOP:
        return specific

    # Universal fallback: Parliamentary Censure (ED-FA-0012 — reuse the unique slot, don't add one).
    if faction.parliamentary:
        censure = parliamentary_action.propose_censure(faction, world, rng)
        if censure != _NOOP:
            return censure

    return _NOOP


def _faction_specific_unique(faction, world, rng) -> str:
    """The faction's OWN unique-action priority chain (pre-ED-FA-0012 body, unchanged). Returns a
    dispatch string on success or '{_NOOP}' when the faction has no specific unique action available
    this season — at which point _try_faction_unique applies the Parliamentary-Censure fallback."""
    if faction.name == 'Crown':
        mode = crown_initiative.select_initiative_mode(faction, world, rng)
        if mode is None:
            return _NOOP
        if mode == 'royal_progress':
            r = crown_initiative.attempt_royal_progress(faction, world, rng)
        elif mode == 'great_work':
            r = crown_initiative.attempt_great_work(faction, world, rng)
        elif mode == 'coronation_renewal':
            r = crown_initiative.attempt_coronation_renewal(faction, world, rng)
        else:
            return _NOOP
        if r.status != 'resolved':
            return _NOOP
        return f'CrownInitiative_{mode}:{r.degree.value}'

    if faction.name == 'Church':
        # Priority 1: Excommunication (primary offensive, high strategic impact)
        if faction.L >= excommunication.EXCOMM_PREREQ_L_LIGHT:
            target = excommunication.select_excommunication_target(faction, world, rng)
            if target is not None:
                r = excommunication.attempt_excommunication(faction, target, world, rng)
                if r.status == 'resolved':
                    return f'Excommunication:{r.degree.value}'
        # Priority 2: Council (1/arc, rare but high-value Mandate boost)
        if not getattr(faction, 'council_used_this_arc', False):
            r = council_solmund.attempt_council(faction, world, rng)
            if r.status == 'resolved':
                return f'Council:{r.degree.value}'
        # Priority 3: Absolution — only when Church.L >= 4 (cost is L-1; protect Excomm prereq)
        if faction.L >= 4.0:
            target = absolution.select_absolution_target(faction, world, rng)
            if target is not None:
                r = absolution.attempt_absolution(faction, target, world, rng)
                if r.status == 'resolved':
                    return f'Absolution:{r.degree.value}'
        return _NOOP

    # Varfell + Hafenmark — no faction-specific unique action yet (Pass 2d/2e + contamination audit
    # BLOCKED). ED-FA-0012: the Parliamentary-Censure fallback in _try_faction_unique is the ONLY
    # live path for these two through the unique slot.
    return _NOOP


def _try_conquest(faction, world, rng) -> str:
    """Attempt military conquest of adjacent territory.

    Phase 7 (§4.10 sub-step 3): single-roll path replaced with
    `resolve_mass_battle` engine invocation per
    systems/mass_battle/mass_battle_integration_v30.md §4.10.
    GD-1 binding: produces faction stat / territorial-control deltas only —
    no victory triggers from the battle outcome itself.

    ED-FA-0013 (FA-6 a/b): on attacker victory the settlement-side effect forks Terms vs Storm.
    Terms (defender NOT routed — degree 'Success') is strictly cheaper for the attacker and preserves
    legitimacy; the AI accepts Terms whenever it is available. Storm (defender routed — degree
    'Overwhelming', or Terms otherwise not chosen) keeps the existing harsher baseline.

    Citations:
      - systems/mass_battle/mass_battle_integration_v30.md §4.10 step 3
      - systems/settlements/settlement_layer_v30.md §5.1 (FA-6) / §5.3 (Entry Terms)
      - canon/02_canon_constraints.md §B GD-1
    """
    targets = _conquest_targets(faction, world)

    if not targets or faction.Mil < CONQUEST_MIN_MIL:  # [canonical: v17 conquest gate — Mil >= 3]
        return _NOOP

    target = rng.choice(targets)
    t = world.territories[target]

    # Phase 7 §4.10.3 — mass-battle engine invocation (replaces v17 single-roll path).
    # Defender is the territory owner faction, or None (uncontrolled garrison stub).
    from systems.mass_battle.sim.massbattle import resolve_mass_battle
    defender_faction = world.factions.get(t.owner) if t.owner else None
    battle = resolve_mass_battle(
        faction_a=faction,
        faction_b=defender_faction,
        terrain=None,  # [GAP: terrain modifiers deferred to Phase 7 follow-on Steps 2-9]
        world=world,
    )
    deg = battle['degree']

    if battle['attacker_wins']:
        old = t.owner
        if old and old in world.factions:
            # [hash-seed fix 2026-05-20] .discard() → list guard-remove
            if target in world.factions[old].territories:
                world.factions[old].territories.remove(target)
            world.factions[old].adjust('L', -10)  # [canonical: faction_layer §2.3 loser-Legitimacy-on-transfer, v17]
        t.owner = faction.name
        # [hash-seed fix 2026-05-20] .add() → guarded append (preserves set-like idempotence)
        if target not in faction.territories:
            faction.territories.append(target)
        t.garrison = True

        # ── ED-FA-0013 (FA-6 a/b): Terms vs Storm settlement-side fork ────────────────────────────
        # [SEED — attacker-AI policy default, ED-FA-0013] The attacker accepts surrender on Terms
        # whenever it is available (defender NOT routed → degree 'Success'). Terms is strictly cheaper
        # for the attacker (lighter Accord penalty, no reputational Storm cost) and nothing in the
        # current AI prefers the costlier path — so Terms is the defensible default, open to a future
        # explicit AI-policy choice. [canonical: settlement_layer_v30 §5.1 FA-6 branch (a); Grotius III]
        if deg == 'Success':
            # Branch (a) Accept surrender on terms — Grotius III / Parker 1994 (honors of war).
            t.adjust_accord(ACCORD_TERMS)  # [canonical: settlement_layer_v30 §5.1 FA-6(a) lighter Accord — ED-FA-0013]
            # §5.3 Entry Terms: "surrender on terms" makes Confirm Privileges the natural fork, which
            # seeds the new settlement's Legitimacy at 3 (Joyeuse Entrée; ED-SE-0011). This module is
            # the PRE-LPS-1 scalar oracle (ED-FA-0004): there is no populated per-settlement L in the
            # live campaign, so the seed is carried at territory grain as a forward-compatible,
            # golden-inert proxy (read by nothing yet) that LPS-1 relocates onto Settlement.legitimacy.
            # [canonical: settlement_layer_v30 §5.3 "Confirm Privileges … L seeds 3" (ED-SE-0011)]
            t.entry_terms_l_seed = ENTRY_TERMS_CONFIRM_L_SEED
        else:
            # Branch (b) Storm (defender routed — degree 'Overwhelming') — existing harsher baseline,
            # UNCHANGED. [canonical: settlement_layer_v30 §5.1 FA-6(b) storm = existing baseline — ED-FA-0013]
            t.adjust_accord(ACCORD_STORM)  # [canonical: v17 Assault/capture Accord baseline; settlement_layer §5.1 FA-6(b)]

        world.battle_count += 1

    return f'Conquest:{deg}'


def _try_muster(faction, world, rng) -> str:
    """Muster military strength in owned territory.

    ED-FA-0009 (FA-2): Muster is a fiscal-military PURCHASE, not a free-except-on-failure roll. The
    military enterpriser is paid regardless of outcome (Redlich 1964, the Wallenstein/Mansfeld
    contractor model; Tilly 1990, coercion-and-capital), so Wealth is charged UP FRONT on every
    attempt and money buys pool: pool = Mil + floor(W/2). The old "W-3 only on Failure" inversion is
    retired — the up-front cost now serves the failure-penalty role (no double-charge).
    """
    if not faction.territories:
        return _NOOP

    # Pay the enterpriser up front, ALWAYS — before rolling (Redlich 1964; Tilly 1990). Faction.adjust
    # clamps at its Wealth floor, so an already-broke faction still fires the attempt (the proposal
    # specifies a cost, not a hard Wealth gate) — it simply pays what it can.
    faction.adjust('W', -MUSTER_WEALTH_COST)  # [canonical: ED-FA-0009 (FA-2) up-front W cost; Redlich 1964 / Tilly 1990]

    # Money raises troops: pool = Mil + floor(W/2). [canonical: ED-FA-0009 (FA-2); Redlich 1964]
    pool = faction.Mil + math.floor(faction.W / MUSTER_WEALTH_TO_POOL_DIV)
    ob = 1  # [canonical: v17 Muster Ob 1]
    net = _successes(pool, rng) - ob
    deg = _degree(net)

    if deg in ('Overwhelming', 'Success'):
        faction.adjust('Mil', 5 if deg == 'Overwhelming' else 3)  # [canonical: v17 Muster Mil gain +5/+3]
    # ED-FA-0009 (FA-2): Failure carries NO additional Wealth penalty — the up-front cost above already
    # priced the failed levy. Do NOT re-charge the retired v17 W-3-on-Failure here (double-charge).

    return f'Muster:{deg}'


def _try_govern(faction, world, rng) -> str:
    """Govern an owned territory to improve Accord."""
    if not faction.territories:
        return _NOOP
    target = rng.choice(list(faction.territories))
    t = world.territories.get(target)
    if not t or t.owner != faction.name:
        return _NOOP

    pool = faction.I
    ob = 2  # [canonical: v17 Govern Ob 2]
    net = _successes(pool, rng) - ob
    deg = _degree(net)

    if deg in ('Overwhelming', 'Success'):
        t.adjust_accord(15 if deg == 'Overwhelming' else 10)  # [canonical: v17 Govern Accord gain +15/+10]
    elif deg == 'Failure':
        faction.adjust('Sta', -5)  # [canonical: v17 Govern Failure Stability -5]

    return f'Govern:{deg}'
