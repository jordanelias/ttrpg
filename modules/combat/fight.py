"""THE FIGHT -- the `combat` module's entry (A-25; plan position `31b`).

`modules/combat/` is the personal-combat engine: the import closure of `wrapper` and `combatant`, moved
from `systems/combat/combat_engine_v1/` at `31b`; it is a package (CI-09), its files import each other by
dotted name, and the host reaches it by the composition rows `combat.fight` and `combat.duel_terms`, never by a
path. This file is the one module entry: the composition row whose target is `fight` below (`entry: verb_call`, `verb: fight`),
registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction, and called by the host
adapter `seam/wrappers/combat.py::resolve` -- the `@provider("contest", "personal_combat")` the prize row
`the body` names, for every verb contesting that prize.

It takes the host's typed input record and a seeded `rng`, and imports the record type,
nothing else of the host. It never reads or writes `World`, holds no token and keeps no state between
calls (A-25): the engine's `wrapper._TRACE` hook is bound for the call and restored after it by `wrapper.fight`'s own `trace`
argument; this file never assigns it.

It reads the scene, it does not grade it. It returns a `CombatOutcome` (`queries/inputs.py`): what the engine computed
before `wrapper.fight` collapses it to an int -- each party's lifted `WoundTracker` (`PartyWounds`), the yield, the
felling wound, the rounds fought, the scene's shape (`scene_shape`, B14.15) and the trace. The integer `wrapper.fight` returns is not lifted, and no winner crosses
the boundary: the host interprets the record, the wound-state refusal is `seam/wrappers/combat.py`'s, and the degree is
`seam/ladder.py::combat_degree`'s.
"""
from __future__ import annotations

import dataclasses
from typing import Callable, Mapping, Optional

from engine.dice_engine.draw import Draw
from engine.season.queries.inputs import (
    CombatOutcome, CombatTurnView, DecisiveBeat, PartyWounds, PersonalCombatInput, SceneShape, Surrender)
from . import attributes as spec, combatant, wrapper
from .config import CFG

_MISSING = object()   # `getattr`'s default for a tracker field the engine does not carry (None is a value)


def _kit_kw(kit) -> dict:
    """`Combatant`'s keyword arguments for one party's `(weapon, armor)` kit; `None` (no kit given) is none, so the
    Combatant keeps its own defaults."""
    return {} if kit is None else dict(weapon=kit[0], armor=kit[1])


def _faculty_kw(fac) -> dict:
    """`Combatant`'s keyword for one party's skill score (CR-85; the record's `scores` entry); `None` (none given) is none, so the
    Combatant keeps its own default."""
    return {} if fac is None else dict(faculty=fac)


def _fight_cfg(inp: PersonalCombatInput, cfg: Optional[dict] = None) -> Optional[dict]:
    """The engine's `cfg` carrying the record's operands: `BASE_POOL` and `POOL_FLOOR` (`wrapper._pool_dice` reads them) and
    `OPPOSITION_RATE` (`core.ob_from_defender` reads it), each where the record carries one (not `None`), laid over `cfg`
    (the workbench's config overlay; `config.CFG` where it passes none); or `cfg` itself (`None`: the engine's own `CFG`, so
    `core.OPPOSITION_RATE`, the control 0.5) where the record carries none. A copy: neither dict is ever written."""
    carried = {k: v for k, v in (("BASE_POOL", inp.pool_add), ("POOL_FLOOR", inp.pool_floor),
                                 ("OPPOSITION_RATE", inp.opposition_rate)) if v is not None}
    return {**(CFG if cfg is None else cfg), **carried} if carried else cfg


def _extras_kw(trad, tech, axes, disp) -> dict:
    """`Combatant`'s keywords for one party's four workbench fields (B14.11): a tradition name, `{name: level}` techniques
    (`Combatant.equipped`), `{axis: bonus}` axes (`Combatant.skills`, whose own name stays) and a `disp`; each `None`
    (none given) is none, so the Combatant keeps its own default."""
    return {k: v for k, v in (("tradition", trad), ("equipped", tech), ("skills", axes), ("disp", disp)) if v is not None}


def _attr_kw(authored) -> dict:
    """`Combatant`'s keywords for one party's authored attributes (PC-06 K-1): each `attributes.SPEC` entry whose
    `registry_key` the party authored, by that key; every other field stays at the class default. `end` is the input's
    `ends` (the seam composes it with the body bands), and `faculty`/`disp` have no registry key. `None` is none."""
    if not authored:
        return {}
    return {s.key: authored[s.registry_key] for s in spec.SPEC
            if s.key != "end" and s.registry_key is not None and s.registry_key in authored}


def _party_wounds(c) -> Optional[PartyWounds]:
    """One party's `PartyWounds`, every field read off its `WoundTracker`; `None` when the Combatant carries no tracker
    (the host refuses it by name). A field the tracker lacks raises `AttributeError` naming it."""
    wt = getattr(c, "wt", None)
    if wt is None:
        return None
    return PartyWounds(**{f.name: getattr(wt, f.name) for f in dataclasses.fields(PartyWounds)})


def _surrender(trace: list) -> Optional[Surrender]:
    """The scene's first `yield` event the engine did not refuse (a refused declaration is not a surrender), or `None`."""
    for e in trace:
        if e.get("kind") == "yield" and e.get("refused") is None:
            return Surrender(by=e["by"], round=e["turn"], accepted=e["accepted"])
    return None


def _beat(trace: list) -> Optional[DecisiveBeat]:
    """The trace's last `wound` event that felled its victim, or `None` when nobody was felled. The `wound` event
    names no weapon and no round: the weapon is the striker's as `fight_start` issued it, the round the count of
    `turn_start` events up to the wound."""
    weapons: dict = {}
    rnd, found = 0, None
    for e in trace:
        kind = e.get("kind")
        if kind == "fight_start":
            weapons = {e["A"]: e["weapon_A"], e["B"]: e["weapon_B"]}
        elif kind == "turn_start":
            rnd += 1
        elif kind == "wound" and e.get("felled"):
            found = DecisiveBeat(by=e["by"], victim=e["victim"], source=e["source"],
                                 weapon=weapons.get(e["by"], ""), round=rnd)
    return found


def scene_shape(trace, claimants: tuple, health_full: Mapping[str, int]) -> SceneShape:
    """The scene's `SceneShape` (B14.15), a PURE FOLD over the trace's `wound` and `turn_start` events (and nothing else: a
    `yield` declares an ending the shape does not count, and no new engine event is emitted for it). `claimants` is the
    record's `(A, B)`; `health_full` is `{id: full Health}` for each party whose Combatant carries a tracker (a `wound` event
    carries the victim's `cumulative` damage, and Health full is the one number the trace does not hold).

    `blows[p]` counts `wound` events `p` struck (the engine emits one only for damage above 0); `first_blood` is the first's
    striker; `nearest[p]` is `health_full[p]` less the most `cumulative` damage `p` reached; `lead_changes` counts the times the
    party AHEAD on Health fraction became the other one -- ahead is the strictly higher `remaining / full`, compared by cross
    multiplication (no float), a tie leaves the last leader standing, so a tie is no lead and no change, and the first lead
    taken from the opening tie is not a change. A party absent from `health_full` has no fraction to compare: `lead_changes`
    is then 0 and he is absent from `nearest`."""
    blows = {pid: 0 for pid in claimants}
    cumulative = {pid: 0 for pid in claimants}
    rounds, first_blood, changes, ahead = 0, None, 0, None
    for e in trace:
        kind = e.get("kind")
        if kind == "turn_start":
            rounds += 1
        elif kind == "wound":
            by, victim = e["by"], e["victim"]
            blows[by] = blows.get(by, 0) + 1
            if first_blood is None:
                first_blood = by
            cumulative[victim] = max(cumulative.get(victim, 0), e["cumulative"])
            if all(pid in health_full for pid in claimants) and len(claimants) == 2:
                (a, b) = claimants
                ra, rb = health_full[a] - cumulative[a], health_full[b] - cumulative[b]
                lead = a if ra * health_full[b] > rb * health_full[a] else b if rb * health_full[a] > ra * health_full[b] else None
                if lead is not None:
                    if ahead is not None and lead != ahead:
                        changes += 1
                    ahead = lead
    nearest = {pid: max(0, health_full[pid] - cumulative[pid]) for pid in claimants if pid in health_full}
    return SceneShape(rounds=rounds, blows=blows, first_blood=first_blood, lead_changes=changes, nearest=nearest)


def fight(inp: PersonalCombatInput, rng: Draw,
          decide: Optional[Callable[[CombatTurnView], str]] = None, cfg: Optional[dict] = None,
          max_bouts: Optional[int] = None) -> CombatOutcome:
    """Fight one bout scene between the record's two parties and return a `CombatOutcome`: `wounds[id]` is that
    party's `PartyWounds` (absent when the Combatant carries no tracker, which the host refuses), `surrender` the
    scene's un-refused `yield`, `beat` the wound that felled a party, `rounds` the `turn_start` count and `trace` the
    scene's events.

    The `rng` is a parameter and is never constructed here (`04 §C.12` rejection 4): the host builds it
    from its own seed and passes it down. A module whose directory is gone is refused earlier, at
    driver construction, by the registrar resolving this file.

    `decide` (v10 REM-31, IN-46) is the host's PLAYABLE per-turn decider, forwarded to the engine's own
    turn loop (`wrapper.fight`'s `decide`), never re-implemented here. It crosses the module boundary
    OUTWARD, so it is handed a typed view, never a `Combatant`: `CombatTurnView` -- the turn index, the
    claimants and a fresh copy of each party's `inp.wound_quantities` (`_lift`, below). `None` (AUTOMATED,
    the default) is the engine's own engage-every-turn loop exactly.

    `cfg` (a config overlay) and `max_bouts` (a bout cap) are the WORKBENCH's (B14.11), forwarded to `wrapper.fight`; the host
    never passes them, and `None` is the engine's own `CFG` and bout count. `max_bouts` is the tree's name until PCR-3."""
    a_id, b_id = inp.claimants
    a_end, b_end = inp.ends
    # THE KITS (CP-T03-03): each party's `(weapon, armor)` in `claimants` order, read off the typed input. A record
    # built without them (`kits == ()`) is two Combatants at the engine's own default kit, as before.
    a_kit, b_kit = inp.kits or (None, None)
    # THE SKILL SCORES (CR-85, ED-IN-0330; B05.57): each party's skill score for the fight's verb, read off the typed input; it
    # is `Combatant.faculty`, the number the Ob his opponent rolls against is taken from. A record built without them
    # (`scores == ()`) fights at the Combatant's own default. His registered pool addends ride beside it as `pool_addends`
    # (read by the pool alone, never the Ob). [ASSUMPTION: carrier -- basis: the smallest edit that keeps the two numbers
    # apart; IS-PC-05 (B15) replaces it with the `pool` slot]
    a_fac, b_fac = inp.scores or (None, None)
    a_add, b_add = inp.addends or (0, 0)
    # THE AUTHORED ATTRIBUTES (PC-06 K-1): each party's `Person.attributes`, mapped by PC-14's `registry_key`.
    a_attr, b_attr = inp.attributes or (None, None)
    # THE WORKBENCH'S FOUR FIELDS (B14.11): each party's tradition, techniques, axes and disposition, passed as the kits are.
    a_ext = _extras_kw(*(p[0] if p else None for p in (inp.traditions, inp.techniques, inp.axes, inp.dispositions)))
    b_ext = _extras_kw(*(p[1] if p else None for p in (inp.traditions, inp.techniques, inp.axes, inp.dispositions)))
    A = combatant.Combatant(a_id, end=a_end, **_attr_kw(a_attr), **_kit_kw(a_kit), **_faculty_kw(a_fac), **a_ext)
    B = combatant.Combatant(b_id, end=b_end, **_attr_kw(b_attr), **_kit_kw(b_kit), **_faculty_kw(b_fac), **b_ext)
    A.pool_addends, B.pool_addends = a_add, b_add
    # THE CARRIED WOUND (B05.61, `UPR` §3 edit 4; A-8): each party's signed level from before the fight, read by `assemble_net_sigma` alone.
    # Carried the way `pool_addends` is, an instance attribute [ASSUMPTION: carrier; IS-PC-05 (B15) replaces it]; 0.0 where the record carries none.
    A.carried, B.carried = inp.carried or (0.0, 0.0)
    trace: list = []
    # THE DUEL TERMS (RS-25, PC-10a): the record's own field, default `'death'` (`wrapper.LETHAL_TERMS`); the engine
    # refuses a term outside `wrapper.DUEL_TERMS` by name.
    terms = inp.terms

    def _lift(c) -> Optional[dict]:
        wt = getattr(c, "wt", None)
        if wt is None:
            return None
        out = {}
        for q in inp.wound_quantities:
            v = getattr(wt, q, _MISSING)
            if v is not _MISSING:
                out[q] = v
        return out

    # THE VIEW THE DECIDER READS (REM-31): built per turn from the trackers, a fresh dict each call.
    turn_choice = None if decide is None else (
        lambda turn: decide(CombatTurnView(turn=turn, claimants=inp.claimants,
                                           wound_state={a_id: _lift(A), b_id: _lift(B)})))
    # The engine's own note: `_TRACE` adds no rng draw and no state mutation, so capturing it CANNOT change the result. That is
    # why the scene may be recorded without perturbing it. `wrapper.fight` binds the hook from `trace` and restores it itself.
    bouts = {} if max_bouts is None else dict(max_bouts=max_bouts)
    wrapper.fight(A, B, cfg=_fight_cfg(inp, cfg), rng=rng, terms=terms, decide=turn_choice, trace=trace.append,
                  **bouts)   # the integer it returns is not lifted

    wounds = {pid: pw for pid, pw in ((a_id, _party_wounds(A)), (b_id, _party_wounds(B))) if pw is not None}
    shape = scene_shape(trace, (a_id, b_id), {pid: pw.health_full for pid, pw in wounds.items()})
    return CombatOutcome(claimants=(a_id, b_id), wounds=wounds, surrender=_surrender(trace), beat=_beat(trace),
                         rounds=shape.rounds, shape=shape, trace=tuple(trace))
