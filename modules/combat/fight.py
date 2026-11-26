"""THE FIGHT -- the `combat` module's entry (A-25; plan position `31b`).

`modules/combat/` is the personal-combat engine: the import closure of `wrapper` and `combatant`, moved
from `systems/combat/combat_engine_v1/` at `31b`; it is a package (CI-09), its files import each other by
dotted name, and the host reaches it by the composition rows `combat.fight`, `combat.round` and `combat.duel_terms`, never by a
path. This file is the module entry: the composition row whose target is `fight` below (`entry: verb_call`, `verb: fight`),
registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction, and called by the host
adapter `seam/wrappers/combat.py::resolve` -- the `@provider("contest", "personal_combat")` the prize row
`the body` names, for every verb contesting that prize.

It takes the host's typed input record and a seeded `rng`, and imports the record type,
nothing else of the host. It never reads or writes `World`, holds no token and keeps no state between
calls (A-25): the engine's `wrapper._TRACE` hook is bound for the call and restored after it by `wrapper.traced` (one round, `fight_round`);
this file never assigns it.

It reads the scene, it does not grade it. It returns a `CombatOutcome` (`queries/inputs.py`): what the engine computed
as the rounds of `fight_round` leave it -- each party's lifted `WoundTracker` (`PartyWounds`), the yield, the
felling wound, the rounds fought, the scene's shape (`scene_shape`, B14.15) and the trace. No integer result is lifted and no winner crosses
the boundary: the host interprets the record, the wound-state refusal is `seam/wrappers/combat.py`'s, and the degree is
`seam/ladder.py::combat_degree`'s.
"""
from __future__ import annotations

import dataclasses
from typing import Callable, Mapping, Optional

from engine.dice_engine.draw import H2, Draw, seeded
from engine.dice_engine.sigma_leverage import levels_to_net_sigma
from engine.season.queries.inputs import (
    CombatOutcome, CombatRoundView, DecisiveBeat, DuelRoundInput, DuelRoundOutcome, DuelState, MortalResult, PartyWounds,
    PersonalCombatInput, SceneShape, Surrender)
from . import attributes as spec, combatant, core, wrapper
from .config import CFG

_MISSING = object()   # `getattr`'s default for a tracker field the engine does not carry (None is a value)


def _kit_kw(kit) -> dict:
    """`Combatant`'s keyword arguments for one party's `(weapon, armor)` kit; `None` (no kit given) is none, so the
    Combatant keeps its own defaults."""
    return {} if kit is None else dict(weapon=kit[0], armor=kit[1])


def _score_kw(score) -> dict:
    """`Combatant`'s keyword for one party's skill score (CR-85; the record's `scores` entry); `None` (none given) is none, so the
    Combatant keeps its own default."""
    return {} if score is None else dict(score=score)


def _fight_cfg(inp: PersonalCombatInput, cfg: Optional[dict] = None) -> Optional[dict]:
    """The engine's `cfg` carrying the record's operands: `BASE_POOL` and `POOL_FLOOR` (`wrapper._pool_dice` reads them) and
    `OPPOSITION_RATE` (`core.ob_from_defender` reads it), each where the record carries one (not `None`), laid over `cfg`
    (the workbench's config overlay; `config.CFG` where it passes none); or `cfg` itself (`None`: the engine's own `CFG`, so
    `core.OPPOSITION_RATE`, `MU_PER_DIE` since B15.03) where the record carries none. A copy: neither dict is ever written."""
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
    `ends` (the seam composes it with the body bands), and `disp` has no registry key. `None` is none."""
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
            return Surrender(by=e["by"], round=e["round"], accepted=e["accepted"])
    return None


def _beat(trace: list) -> Optional[DecisiveBeat]:
    """The trace's last `wound` event that felled its victim, or `None` when nobody was felled. The `wound` event
    names no weapon and no round: the weapon is the striker's as `fight_start` issued it, the round the count of
    `round_start` events up to the wound."""
    weapons: dict = {}
    rnd, found = 0, None
    for e in trace:
        kind = e.get("kind")
        if kind == "fight_start":
            weapons = {e["A"]: e["weapon_A"], e["B"]: e["weapon_B"]}
        elif kind == "round_start":
            rnd += 1
        elif kind == "wound" and e.get("felled"):
            found = DecisiveBeat(by=e["by"], victim=e["victim"], source=e["source"],
                                 weapon=weapons.get(e["by"], ""), round=rnd)
    return found


def scene_shape(trace, claimants: tuple, health_full: Mapping[str, int]) -> SceneShape:
    """The scene's `SceneShape` (B14.15), a PURE FOLD over the trace's `wound` and `round_start` events (and nothing else: a
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
        if kind == "round_start":
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


def mortal_wound(outcome: PartyWounds, rng: Draw, terms: tuple) -> MortalResult:
    """THE MORTAL-WOUND DRAW (B15.07, PHY_A A3; A-5 to A-8, A-81): whether a party the scene FELLED dies, is left for dead, or lives.

    `outcome` is his lifted tracker (`felled` true); `rng` his own `Draw` (`_mortal_draw`: keyed `fight.mortal`, A-30), never the scene's stream;
    `terms` is `(pool, obstacle, levels_for, levels_against)`, the record's `mortal` entry less its key: the pool the one pool rule on the untrained
    default and the obstacle `mortal_wound_ob[terms]` (both `world_q.mortal_terms`), the levels named `LEVEL_SIGMA` levels (his governing
    attribute and a tending ally's `healing` for or against him, his body band against him), summed by `levels_to_net_sigma`. ONE ROLL ON THE
    ONE SAMPLER: `core.resolve` (`roll_net_continuous` plus `net_boost`, the roll a fight's every exchange and the survivor's mark roll take),
    banded by `degree_from_net` (`core.degree`'s label of the owner ladder).

    Failure: he dies (`mortal`, the scene's wounds). Partial: he stands up at `max_wounds` (or the scene's, if more), left for dead. Success and Overwhelming: he stands
    up with the scene's wounds. Every band writes (A-81): none is the untouched band. Pure: one roll, nothing kept."""
    pool, ob, levels_for, levels_against = terms
    deg, _net = core.resolve(pool, levels_to_net_sigma(list(levels_for), list(levels_against)), rng, ob)
    if deg == "fail":
        return MortalResult(mortal=True, wounds=outcome.wounds, degree=deg)
    # Partial is AT LEAST `max_wounds`: a felling can leave more wounds than `max_wounds` (the tracker counts every wounding blow), and left for
    # dead is never lighter than standing up wounded as the scene left him [ASSUMPTION; low; PHY_A says "`wounds = max_wounds`"; revert: that]
    return MortalResult(mortal=False, wounds=max(outcome.wounds, outcome.max_wounds) if deg == "partial" else outcome.wounds, degree=deg)


def _mortal_draw(rng: Draw, pid: str, key) -> Draw:
    """The `Draw` one felled party's mortal roll takes. `key` (the record's): the host's keyed draw `(world_seed, tick, pid, "fight.mortal:<cause>")`
    (A-30), seeded through the one constructor -- the dealt fight's, never a position in the scene's stream, and carried as its key so the
    record stays a value (a `Draw` object in it would be consumed by the first call). `None` (a sampled estimate's record, whose draws must stay
    private): a sub-key of the scene's own `Draw` at its current ordinal (B15.05's form, `H2(rng.key, purpose)`), so each sample draws afresh
    and nothing of the dealt key is read."""
    return seeded(key) if key is not None else seeded(H2(rng.key, f"fight.mortal:{pid}:{rng.n}"))


def _combatants(inp: PersonalCombatInput, cfg: dict, states: tuple = (DuelState(), DuelState())):
    """The record's two Combatants, each carrying its `DuelState`: built from the typed input, re-derived on `cfg` (`Combatant.rederive`, the one
    derivation path), then the state laid on -- damage, Stamina and Concentration (`None` is the derived maximum, a fight's start), poise and the
    weapon in hand (`None` is the kit's own); initiative is the round's to take. A fresh pair each call: nothing of an earlier pair survives."""
    a_id, b_id = inp.claimants
    a_end, b_end = inp.ends
    # THE KITS (CP-T03-03): each party's `(weapon, armor)` in `claimants` order, read off the typed input. A record
    # built without them (`kits == ()`) is two Combatants at the engine's own default kit, as before.
    a_kit, b_kit = inp.kits or (None, None)
    # THE SKILL SCORES (CR-85, ED-IN-0330; B05.57): each party's skill score for the fight's verb, read off the typed input; it
    # is `Combatant.score`, the number the Ob his opponent rolls against is taken from. A record built without them
    # (`scores == ()`) fights at the Combatant's own default. His registered pool addends ride beside it as `pool_addends`
    # (read by the pool alone, never the Ob). [ASSUMPTION: carrier -- basis: the smallest edit that keeps the two numbers
    # apart; `Combatant.score` is the score's one home, IS-PC-05]
    a_score, b_score = inp.scores or (None, None)
    a_add, b_add = inp.addends or (0, 0)
    # THE AUTHORED ATTRIBUTES (PC-06 K-1): each party's `Person.attributes`, mapped by PC-14's `registry_key`.
    a_attr, b_attr = inp.attributes or (None, None)
    # THE WORKBENCH'S FOUR FIELDS (B14.11): each party's tradition, techniques, axes and disposition, passed as the kits are.
    a_ext = _extras_kw(*(p[0] if p else None for p in (inp.traditions, inp.techniques, inp.axes, inp.dispositions)))
    b_ext = _extras_kw(*(p[1] if p else None for p in (inp.traditions, inp.techniques, inp.axes, inp.dispositions)))
    A = combatant.Combatant(a_id, end=a_end, **_attr_kw(a_attr), **_kit_kw(a_kit), **_score_kw(a_score), **a_ext)
    B = combatant.Combatant(b_id, end=b_end, **_attr_kw(b_attr), **_kit_kw(b_kit), **_score_kw(b_score), **b_ext)
    A.pool_addends, B.pool_addends = a_add, b_add
    # THE CARRIED WOUND (B05.61, `UPR` §3 edit 4; A-8): each party's signed level from before the fight, read by `assemble_net_sigma` alone.
    # Carried the way `pool_addends` is, an instance attribute [ASSUMPTION: carrier; IS-PC-05 (B15) replaces it]; 0.0 where the record carries none.
    A.carried, B.carried = inp.carried or (0.0, 0.0)
    for c, st in zip((A, B), states):
        c.rederive(cfg)
        c.wt.cumulative_damage = st.cumulative_damage
        c.stamina = float(c.stamina_max) if st.stamina is None else st.stamina
        c.conc = c.conc_max if st.conc is None else st.conc
        c.poise = st.poise
        c.initiative = 0.0
        if st.form is not None:
            c.weapon = st.form
    return A, B


def _lift(inp: PersonalCombatInput, c) -> Optional[dict]:
    """One party's `{quantity: value}` over `inp.wound_quantities`, read off its tracker: a fresh dict each call; a quantity the tracker lacks is
    left out, and a Combatant with no tracker is `None`."""
    wt = getattr(c, "wt", None)
    if wt is None:
        return None
    out = {}
    for q in inp.wound_quantities:
        v = getattr(wt, q, _MISSING)
        if v is not _MISSING:
            out[q] = v
    return out


def _check_terms(terms) -> None:
    """The engine's own refusal of a term outside `wrapper.DUEL_TERMS`, raised before the first draw of a fight or a round."""
    if terms not in wrapper.DUEL_TERMS:
        raise ValueError(f"terms {terms!r} is not one of {wrapper.DUEL_TERMS}")


def _attempts(trace: tuple, claimants: tuple) -> dict:
    """`{claimant id: attack attempts}` over one round's trace: each `roll` (the exchange's aggressor), `stophit` (the longer weapon) and pursued
    `disengage` (the closer who pursues) is one attempt by the party named. A pure count."""
    n = {pid: 0 for pid in claimants}
    for e in trace:
        kind = e.get("kind")
        striker = (e.get("aggressor") if kind == "roll" else e.get("longer") if kind == "stophit"
                   else e.get("shorter") if kind == "disengage" and e.get("pursued") else None)
        if striker is not None:
            n[striker] = n.get(striker, 0) + 1
    return n


def fight_round(inp: DuelRoundInput, rng: Draw, deciders=None, *, cfg: Optional[dict] = None) -> DuelRoundOutcome:
    """ONE ROUND AS ITS OWN ENTRY (A-101; PB step 1, PCR-2): build the two Combatants, lay each `DuelState` on, draw `first` (the coin, inside the round),
    run `wrapper.engagement` once, and -- where the round felled nobody -- take the yield rolls (`wrapper.settle_round`) and, where the fight goes on,
    the between-round recovery (`wrapper.recover`); then lift the states. It keeps nothing: no `World`, no module attribute, no state between calls.

    The round says HOW it ended (`ended_by`, `exchanges`, `attempts`), never who won: there is no `winner` on it. `felled` is the party the round
    felled, `yielded` the party whose yield roll failed; a round neither felled nor yielded in which the two yield rolls tied ends the fight with
    nobody yielded -- the trace then carries the engine's `fight_result` event, the one marker a loop reads.

    `rng` is THE ROUND'S OWN `Draw` (`wrapper.round_draw(fight_key, inp.round)`, B16.03), and THE CALLER'S DUTY IS TO HAND EACH ROUND ITS OWN (a `Draw` reused across
    calls repeats `first` and the `gap:`, `upset:`, `yield:` keys, which name the round's key and not a position). Round `r` is a function of `(fight_key, r)` and of
    the states it is handed, and no draw depends on another round's count (A-30). WITHIN the round the draws are `first` (the coin, `H2(rng.key, "first")`), the keyed
    `gap:`, `upset:` and `yield:` draws, and the positional `rng.random()` and `core.resolve` draws of `engagement`, which advance the round's own `Draw` in a fixed
    order: the plan's finer `(r, beat, site)` keying of those is not built (`engine/season/hole_register.yaml` H-581). `cfg` is the workbench's overlay (`fight`'s). `deciders` is the
    per-party approach decider, consulted by no round yet; `inp.plans` is read by no round yet (a missing phase is `normal`)."""
    fi = inp.fighters
    cfg = _fight_cfg(fi, cfg) or CFG
    terms = fi.terms
    _check_terms(terms)
    a_id, b_id = fi.claimants
    A, B = _combatants(fi, cfg, inp.states)
    trace: list = []
    with wrapper.traced(trace.append):
        first = A if seeded(H2(rng.key, "first")).random() < 0.5 else B
        trace.append(dict(kind="round_start", round=inp.round, first=first.label))
        wounds0 = {A: A.wt.wounds, B: B.wt.wounds}   # the round's opening wounds: a wound gate crossed since is the yield roll's licence (B15.10)
        loser, closed, ended_by = wrapper.engagement(A, B, first, cfg, rng, inp.prev_closed,
                                                     terms=None if terms == wrapper.LETHAL_TERMS else terms, turn=inp.round)
        trace.append(dict(kind="round_end", round=inp.round, felled=(loser.label if loser is not None else None), ended_by=ended_by))
        yielder = None
        if loser is None:
            over, yielder = wrapper.settle_round(A, B, wounds0, terms, cfg, rng, 0, inp.round, fi.decisiveness or (0.0, 0.0))   # `0`: the workbench loop's `scene` ordinal, which a round's own key has no use for
            if not over:
                wrapper.recover(A, B, cfg)   # a felling, or a yield, is not a pause to recover in; a `terms` round whose yield rolls pass is (the old loop's law, hash EQUAL; PCR-2 (3)'s 'not after terms' is not followed)
            elif yielder is None:
                trace.append(dict(kind="fight_result", result=0, winner=None))   # both yield rolls failed at one Health: honour is even, nobody yields
    trace = tuple(trace)
    return DuelRoundOutcome(
        states=tuple(DuelState(cumulative_damage=c.wt.cumulative_damage, stamina=c.stamina, conc=c.conc, poise=c.poise, form=c.weapon) for c in (A, B)),
        wounds={a_id: _lift(fi, A), b_id: _lift(fi, B)},
        felled=loser.label if loser is not None else None, yielded=yielder.label if yielder is not None else None,
        closed=closed, trace=trace, ended_by=ended_by,
        exchanges=sum(1 for e in trace if e.get("kind") == "outcome"), attempts=_attempts(trace, (a_id, b_id)))


def fight(inp: PersonalCombatInput, rng: Draw,
          decide: Optional[Callable[[CombatRoundView], str]] = None, cfg: Optional[dict] = None,
          max_rounds: Optional[int] = None) -> CombatOutcome:
    """Fight one fight between the record's two parties and return a `CombatOutcome`: `wounds[id]` is that
    party's `PartyWounds` (absent when the Combatant carries no tracker, which the host refuses), `surrender` the
    scene's un-refused `yield`, `beat` the wound that felled a party, `rounds` the `round_start` count and `trace` the
    scene's events.

    THE FIGHT IS A LOOP OVER `fight_round` (PB step 1) with the `DuelState`s in this frame: up to `max_rounds` rounds (twelve, `wrapper.DEFAULT_ROUNDS`),
    stopping on a felling, a yield, a withdrawal or the last round. The workbench's own loop stays `wrapper.fight`; this one is the host's.

    EACH ROUND DRAWS FROM ITS OWN KEY (B16.03): `fight_round` is handed `wrapper.round_draw(fkey, r)`, `fkey` being `wrapper.fight_draw(rng)` (one uniform of
    `rng`, which keeps a caller that reuses one `Draw` for many fights from fighting one fight n times), so no round's draws depend on another's count (a
    fight that ends at round 3 and one that runs to 12 draw round 3 alike).

    The `rng` is a parameter, and the module builds no generator of its own (`04 §C.12` rejection 4 as amended, A-30: a draw is a function of its key):
    the host builds it from its own seed and passes it down; the module forms keyed SUB-draws of it, or of a hex key the record carries
    (`seeded(H2(rng.key, ...))`), which are values, never state kept between calls. A module whose directory is gone is refused earlier, at
    driver construction, by the registrar resolving this file.

    `decide` (v10 REM-31, IN-46) is the host's PLAYABLE per-round decider, called at the top of each round, before every draw of it. It crosses the
    module boundary OUTWARD, so it is handed a typed view, never a `Combatant`: `CombatRoundView` -- the round index, the
    claimants and a fresh copy of each party's `inp.wound_quantities` (`_lift`, above). `None` (AUTOMATED,
    the default) is the engine's own engage-every-round loop exactly.

    `cfg` (a config overlay) and `max_rounds` (a round cap) are the WORKBENCH's (B14.11); the host
    never passes them, and `None` is the engine's own `CFG` and round cap. """
    a_id, b_id = inp.claimants
    _check_terms(inp.terms)
    cfg_ = _fight_cfg(inp, cfg) or CFG
    A, B = _combatants(inp, cfg_)
    trace: list = [dict(kind="fight_start", A=A.label, B=B.label, weapon_A=A.weapon, weapon_B=B.weapon,
                        armor_A=A.armor, armor_B=B.armor, tradition_A=A.tradition, tradition_B=B.tradition)]
    states = (DuelState(), DuelState())
    wound_state = {a_id: _lift(inp, A), b_id: _lift(inp, B)}
    prev_closed, result, tie = False, 0, False
    fkey = wrapper.fight_draw(rng)
    for rnd in range(1, (wrapper.DEFAULT_ROUNDS if max_rounds is None else max_rounds) + 1):
        if decide is not None:   # THE PER-TURN CHOICE (REM-31): before every draw of the round; draws nothing
            choice = decide(CombatRoundView(round=rnd, claimants=inp.claimants,
                                           wound_state={pid: None if q is None else dict(q) for pid, q in wound_state.items()}))
            if choice not in wrapper.ROUND_CHOICES:
                raise ValueError(f"the decider returned {choice!r}, which is not one of {wrapper.ROUND_CHOICES}")
            if choice == wrapper.WITHDRAW:
                trace.append(dict(kind="withdraw", round=rnd))
                break            # UNRESOLVED, no further round, no riposte draw
        out = fight_round(DuelRoundInput(fighters=inp, states=states, plans=({}, {}), round=rnd, prev_closed=prev_closed),
                          wrapper.round_draw(fkey, rnd), cfg=cfg)
        trace.extend(out.trace)
        states, wound_state, prev_closed = out.states, out.wounds, out.closed
        loser = out.felled or out.yielded
        if loser is not None:   # +1 => A won; a yielder stands, and the other party holds the field
            result = -1 if loser == a_id else 1
            break
        if any(e.get("kind") == "fight_result" for e in out.trace):   # the yield rolls tied: unresolved
            tie = True
            break
    if not tie:
        trace.append(dict(kind="fight_result", result=result, winner=(a_id if result == 1 else b_id if result == -1 else None)))
    A, B = _combatants(inp, cfg_, states)   # the two parties as the last round left them: their trackers lift to `PartyWounds`

    wounds = {pid: pw for pid, pw in ((a_id, _party_wounds(A)), (b_id, _party_wounds(B))) if pw is not None}
    shape = scene_shape(trace, (a_id, b_id), {pid: pw.health_full for pid, pw in wounds.items()})
    # THE MORTAL-WOUND DRAW (B15.07, PHY_A A3): the last step of the scene, before the outcome is returned -- each party the scene felled rolls
    # once (`inp.mortal`, claimants order). A record without the operands (`()`) draws nothing: the felling stands.
    mortal = {pid: mortal_wound(wounds[pid], _mortal_draw(rng, pid, ops[4]), ops[:4]) for pid, ops in zip((a_id, b_id), inp.mortal)
              if pid in wounds and wounds[pid].felled}
    return CombatOutcome(claimants=(a_id, b_id), wounds=wounds, surrender=_surrender(trace), beat=_beat(trace),
                         rounds=shape.rounds, shape=shape, trace=tuple(trace), mortal=mortal)
