"""U0 — units honesty (ED-PC-0002; consolidation_v1.md §4, R3 unified sequence, first increment).

head_len/grip_len (and every derived grip/lever/reach threshold) converted from the 0.30 m
"length-unit" to HONEST METRES: weapons.py stored lengths ×0.30, weapon_physics.UNIT_M deleted,
per-length gains rescaled /0.30 (PERC_2H_ARC, LEVER_K, REACH_GEOM_SCALE), stored-length constants
×0.30 (PERC_GRIP_1H, GRIP_SHORT/GRIP_LONG, LEVER_REF, REC_GRIP_REF, GRAB_SHORT_REACH_M — renamed
from GRAB_SHORT_REACH_LU), wind's edge-length saturation 3.0 lu -> 0.90 m.

CONTRACT: byte-identical at 1e-9 against tests/valoria/r3_identity_golden.json — the OLD-vs-NEW
identity-sweep fixture built ONCE pre-edit on the post-#72 tree (the §4 process wrapper's
mechanism; later byte-identical increments reuse the same fixture). The fixture stores all
lengths in METRES (unit-invariant), so it compares directly on both sides of the conversion.
NEVER hand-edit the fixture; a deliberate re-baseline increment (U1/U2/U9) regenerates it with
recorded reasons. PC-11 removed the `can_choke` key (54 rows, no value changed): a key REMOVAL for a deleted
primitive was the first hand-edit this fixture had. B10-11b's PC-20 (2) is the second: `tests/valoria/r3_identity_golden.json`'s
`systems[*].str_demand` cells were recomputed with the live `S.str_demand` (no generator exists), after a control run at
D_MASS 0 matched the old file exactly.
"""
import json
import math
import os


GOLDEN_PATH = os.path.join(os.path.dirname(__file__), 'r3_identity_golden.json')
TOL = 1e-9
GRIPS = (0.0, 0.25, 0.5, 0.75, 1.0)


def _mods():
    from modules.combat import combatant as C
    from modules.combat import combat_systems as S
    from modules.combat import weapon_physics as WP
    from modules.combat.config import CFG
    return C, S, WP, CFG


def _cmp(errs, name, path, old, new):
    if isinstance(old, bool) or isinstance(old, str):
        if old != new:
            errs.append((name, path, old, new))
        return
    if abs(old - new) > TOL:
        errs.append((name, path, old, new))


def test_units_refactor_byte_identical():
    """Every consumer-visible derived quantity — mass family, dynamics, circumstance bundle,
    percussion/heft, defence affinities, and the systems-level reach/tempo/leverage/recovery
    consumers — reproduces the pre-U0 golden at 1e-9, for the full 53-weapon roster."""
    C, S, WP, CFG = _mods()
    golden = json.load(open(GOLDEN_PATH, encoding='utf-8'))['weapons']
    assert set(golden) == set(C.WEAPONS), "fixture must cover the full roster exactly"
    errs = []
    for n, g in golden.items():
        w = C.WEAPONS[n]
        d = WP.derive(w)
        for k, v in g['derive'].items():
            _cmp(errs, n, f'derive.{k}', v, d[k])
        _cmp(errs, n, 'agility', g['agility'], WP.agility(w))
        _cmp(errs, n, 'energy_credit', g['energy_credit'], WP.energy_credit(w))
        _cmp(errs, n, 'handling', g['handling'], WP.handling(w))
        da = WP.defense_affinities(w)
        for k, v in g['defense_affinities'].items():
            _cmp(errs, n, f'defense_affinities.{k}', v, da[k])
        _cmp(errs, n, 'hand_guard_fn', g['hand_guard_fn'], WP.hand_guard(w))
        _cmp(errs, n, 'blade_guard_fn', g['blade_guard_fn'], WP.blade_guard(w))
        _cmp(errs, n, 'distraction', g['distraction'], WP.distraction(w))
        _cmp(errs, n, 'edge_vibration', g['edge_vibration'], WP.edge_vibration(w))
        _cmp(errs, n, 'grip_choke_max', g['grip_choke_max'], WP.grip_choke_max(w))
        _cmp(errs, n, 'grip_travel_max', g['grip_travel_max'], WP.grip_travel_max(w))
        _cmp(errs, n, 'armour_defeat_mode', g['armour_defeat_mode'], WP.armour_defeat_mode(w))
        _cmp(errs, n, 'baked_hand_guard', g['baked_hand_guard'], w['hand_guard'])
        _cmp(errs, n, 'baked_blade_guard', g['baked_blade_guard'], w['blade_guard'])
        _cmp(errs, n, 'gap', g['gap'], w['gap'])
        for rec in g['at_circumstance']:
            a = WP.at_circumstance(w, rec['grip'])
            for k in ('I_g', 'S_g', 'd_g', 'u', 'rear_clearance'):
                _cmp(errs, n, f'at_circumstance[{rec["grip"]}].{k}', rec[k], a[k])
            # geom_slide is stored in METRES in the fixture; post-U0 the live value IS metres
            _cmp(errs, n, f'at_circumstance[{rec["grip"]}].geom_slide_m',
                 rec['geom_slide_m'], a['geom_slide'])
        for i, gg in enumerate(GRIPS):
            _cmp(errs, n, f'grip_swing_ratio[{gg}]', g['grip_swing_ratio'][i], WP.grip_swing_ratio(w, gg))
            _cmp(errs, n, f'phi_grip_native[{gg}]', g['phi_grip_native'][i], WP.phi_grip(w, gg, w['head']))
            _cmp(errs, n, f'phi_grip_point[{gg}]', g['phi_grip_point'][i], WP.phi_grip(w, gg, 'point'))
            _cmp(errs, n, f'puncture_pressure[{gg}]', g['puncture_pressure'][i], WP.puncture_pressure(w, grip=gg))
            _cmp(errs, n, f'heft[{gg}]', g['heft'][i], WP.heft(w, grip=gg))
        for rec in g['percussion_authority']:
            _cmp(errs, n, f'percussion[{rec["grip"]},{rec["room"]}]', rec['v'],
                 WP.percussion_authority(w, grip=rec['grip'], room=rec['room']))
        _cmp(errs, n, 'heft_point_override', g['heft_point_override'],
             WP.heft(w, grip=0.5, sel_head='point', sel_pc=0.5))
        for gg in ('0.0', '0.5', '1.0'):
            c = C.Combatant('x', weapon=n)
            c.grip_position = float(gg)
            sg = g['systems'][gg]
            _cmp(errs, n, f'systems[{gg}].reach_base', sg['reach_base'], S.reach_base(c, CFG))
            _cmp(errs, n, f'systems[{gg}].wield_heft', sg['wield_heft'], S.wield_heft(c, CFG))
            _cmp(errs, n, f'systems[{gg}].weapon_tempo', sg['weapon_tempo'], S.weapon_tempo(c, CFG))
            _cmp(errs, n, f'systems[{gg}].close_tempo', sg['close_tempo'], S.close_tempo(c, CFG))
            _cmp(errs, n, f'systems[{gg}].str_demand', sg['str_demand'], S.str_demand(c, CFG))
            _cmp(errs, n, f'systems[{gg}].rear_clearance', sg['rear_clearance'], S.rear_clearance(c, CFG))
            _cmp(errs, n, f'systems[{gg}].close_unwieldiness', sg['close_unwieldiness'], S.close_unwieldiness(c, CFG))
            _cmp(errs, n, f'systems[{gg}].recoverability_factor', sg['recoverability_factor'], S.recoverability_factor(c, CFG))
        c = C.Combatant('x', weapon=n)
        c.lunge_depth = 0.4
        _cmp(errs, n, 'systems.lunged.recoverability_factor',
             g['systems']['lunged']['recoverability_factor'], S.recoverability_factor(c, CFG))
        _cmp(errs, n, 'systems.lunged.weapon_tempo',
             g['systems']['lunged']['weapon_tempo'], S.weapon_tempo(c, CFG))
        c2 = C.Combatant('x', weapon=n)
        _cmp(errs, n, 'systems.leverage', g['systems']['leverage'], S.leverage(c2, CFG))
        _cmp(errs, n, 'systems.lunge_quality', g['systems']['lunge_quality'], S.lunge_quality(c2, CFG))
        _cmp(errs, n, 'systems.grip_target_closed', g['systems']['grip_target_closed'], S.grip_target(c2, True, CFG))
        # PC-11: `systems.can_choke` (a bool over this primitive) is deleted with its golden row; the golden's
        # `grip_choke_max` is the pinned fact and "can gather in" is its sign, so the sign is what is compared (implied by the exact `grip_choke_max` compare above; kept because the plan retargets it).
        _cmp(errs, n, 'grip_choke_max>0', bool(g['grip_choke_max'] > 0.0), WP.grip_choke_max(c2.w) > 0.0)
        _cmp(errs, n, 'systems.grab_short_reach', g['systems']['grab_short_reach'],
             bool(w['head_len'] <= CFG['GRAB_SHORT_REACH_M']))
    assert not errs, f"{len(errs)} identity violations (first 10): {errs[:10]}"


def test_no_length_unit_indirection_remains():
    """The 0.30 m length-unit is fully retired: no UNIT_M symbol survives in the engine, and the
    two honest-metre spot anchors hold (rapier blade 0.96 m, spear forward shaft 1.65 m — the
    values weapon_physics' old UNIT_M comment length-validated as 1.14 m / 2.01 m TOTAL lengths)."""
    C, S, WP, CFG = _mods()
    assert not hasattr(WP, 'UNIT_M'), "weapon_physics.UNIT_M must be deleted, not kept as an alias"
    assert 'GRAB_SHORT_REACH_LU' not in CFG and 'GRAB_SHORT_REACH_M' in CFG
    r, s = C.WEAPONS['rapier'], C.WEAPONS['spear']
    assert math.isclose(r['head_len'] + r['grip_len'], 1.14, abs_tol=1e-9)   # rapier 1.14 m overall
    assert math.isclose(s['head_len'] + s['grip_len'], 2.01, abs_tol=1e-9)   # spear 2.01 m overall


# ── B18.02: the slot interface (`03_PC_person_inputs_content` Part A) ───────────────────────────────────────────────

def test_the_slot_tuples_are_in_the_export():
    """The `axis` and `lever` slot tuples (`attributes.AXES`, `attributes.LEVERS`) are in the committed export's `attributes`
    section, and each member's declared default is the value the engine computes for a fighter holding none: an untrained
    axis reads 0.0 (`Combatant.skill`), a lever read as a factor reads 1.0 (`ability_factor`) and one read as a bonus 0.0
    (`ability_bonus`). Every lever a learned ability targets is a declared member, with the op the default implies."""
    from modules.combat import ability_primitives as ABIL, attributes
    C, _S, _WP, _CFG = _mods()
    path = os.path.join(os.path.dirname(__file__), '..', '..', 'engine', 'engine_params', 'combat_engine_v1.json')
    slots = json.load(open(path, encoding='utf-8'))['sections']['attributes']['slots']
    assert sorted(slots['axis']) == sorted(a.key for a in attributes.AXES)   # the file's keys are sorted
    assert sorted(slots['lever']) == sorted(l.key for l in attributes.LEVERS)
    fresh = C.Combatant('x')
    for a in attributes.AXES:
        assert slots['axis'][a.key]['default'] == a.default == fresh.skill(a.key)
    for lv in attributes.LEVERS:
        assert slots['lever'][lv.key]['default'] == lv.default
        assert lv.default in (0.0, 1.0)
        engine_reads = ABIL.ability_bonus(fresh, lv.key) if lv.default == 0.0 else ABIL.ability_factor(fresh, lv.key)
        assert engine_reads == lv.default, f"lever {lv.key}: the engine's untrained value is {engine_reads}"
    levers = {lv.key: lv for lv in attributes.LEVERS}
    checked = 0
    for name, ab in ABIL.ABILITIES.items():
        assert ab['lever'] in levers, f"ability {name!r} targets a lever the slot tuple does not declare"
        assert (ab['op'] == '+') == (levers[ab['lever']].default == 0.0), f"ability {name!r}: op {ab['op']} on lever {ab['lever']}"
        checked += 1
    assert checked >= 30


def test_an_empty_slot_reproduces_todays_fight():
    """One matchup, four seeds, the record equal: a fight whose slot fields are absent, given as `None` per party, or given
    as each slot's declared default is the same fight, event for event. The control: one axis two points above its default
    is a different fight on some seed (so the equality could have failed)."""
    from engine.dice_engine import draw
    from engine.season.queries.inputs import PersonalCombatInput
    from modules.combat import attributes, fight as entry
    base = dict(claimants=("A", "B"), ends=(4, 4), wound_quantities=("felled", "wounds", "max_wounds", "health_remaining", "health_full"),
                kits=(("arming", "heavy"), ("arming", "heavy")))   # a mirror in heavy armour: twelve rounds, so an axis has rounds to act in
    defaults = {a.key: a.default for a in attributes.AXES}
    absent = PersonalCombatInput(**base)
    nones = PersonalCombatInput(**base, techniques=(None, None), axes=(None, None), dispositions=(None, None))
    declared = PersonalCombatInput(**base, techniques=({}, {}), axes=(dict(defaults), dict(defaults)),
                                   dispositions=(attributes.DEFAULT['disp'], attributes.DEFAULT['disp']))
    raised = PersonalCombatInput(**base, axes=({k: 2.0 for k in defaults}, None))
    differs = 0
    for seed in range(4):
        fought = [entry.fight(r, draw.seeded(draw.H2("slot_default", seed))) for r in (absent, nones, declared, raised)]
        assert fought[0] == fought[1] == fought[2], f"seed {seed}: an empty slot moved the fight"
        differs += fought[3] != fought[0]
    assert differs >= 1, "a raised axis never changed a fight: the equality above could not have failed"


# ── B18.06: one carry rule at the kit's owner (`03_PC_loadout_and_carry` item 1) ────────────────────────────────────

def test_carry_demand_of_equals_the_keyed_spelling():
    """The two spellings of the carry rule are one rule, and its harness term is the one the engine charges today. (1) for
    each weapon pair and each armour tier, `carry_demand(keys, tier)` equals `carry_demand_of(the keys' masses, tier)`,
    and a carried kilogram adds `D_MASS`; (2) with nothing carried, the demand is `ARMOR_DEMAND[tier]`, and the stamina
    `combat_systems.act_cost` charges for that tier above the same fighter unarmoured is `ACT_WEIGHT / D_WT * COST_SCALE`
    times `max(0, carry_demand_of((), tier) - strength)`, at a Strength under the demand and one over it. B18.07 relocates
    the harness term onto this function; this is the number it must keep."""
    from engine.substrate import combat_kit as K
    C, S, _WP, CFG = _mods()
    keys = ('dagger', 'arming', 'greatsword', 'spear')
    checked = 0
    for tier in sorted(K.ARMOUR_TIERS):
        for carried in ((), keys[:1], keys[:2], keys[1:], keys):
            masses = tuple(C.WEAPONS[k]['mass'] for k in carried)
            assert K.carry_demand(carried, tier) == K.carry_demand_of(masses, tier)
            assert K.carry_demand_of(masses, tier) == CFG['D_MASS'] * sum(masses) + CFG['ARMOR_DEMAND'][tier]
            checked += 1
    assert checked == 5 * len(K.ARMOUR_TIERS) and len(K.ARMOUR_TIERS) == 4
    unit = CFG['ACT_WEIGHT'] / CFG['D_WT'] * CFG['COST_SCALE']
    paid = 0
    for tier in sorted(K.ARMOUR_TIERS):
        for strength in (1.0, 7.0):
            bare = C.Combatant('b', weapon='arming', armor='none', strength=strength)
            worn = C.Combatant('w', weapon='arming', armor=tier, strength=strength)
            extra = S.act_cost(worn, 0.0, CFG) - S.act_cost(bare, 0.0, CFG)
            owed = unit * max(0.0, K.carry_demand_of((), tier) - strength)
            assert abs(extra - owed) < 1e-12, f"{tier} at Strength {strength}: act_cost charges {extra}, carry_demand says {owed}"
            paid += extra > 0
    assert paid >= 3, "no armour tier was ever charged: the equality above could not have failed"


# ── B18.07: the shortfall rides the input (`03_PC_loadout_and_carry` items 2, 3) ─────────────────────────────────────

def test_the_relocated_harness_term_charges_the_same_stamina(monkeypatch):
    """One mirror fight per armour tier, the fighter of Strength 1 paying the harness at every worn tier and the one of
    Strength 4 at heavy only. AFTER: the record carries each party's `short` (`combat_kit.shortfall`, the host's fill) and
    `act_cost` reads it. BEFORE: the record carries none and `act_cost` is the oracle's old line, recomputed here from
    `ACT_WEIGHT`, `D_WT`, `ARMOR_DEMAND` and the Combatant's Strength (not a stored golden). The fight's events and the
    round's stamina are equal. Control: a record whose `short` is raised a point spends more stamina, so the equality
    could have failed."""
    from engine.dice_engine import draw
    from engine.season.queries.inputs import DuelRoundInput, DuelState, PersonalCombatInput
    from engine.substrate import combat_kit as K
    from modules.combat import fight as entry
    _C, S, _WP, CFG = _mods()

    def old_act_cost(c, commit, cfg):
        return (cfg['ACT_BASE'] + cfg['ACT_WEIGHT'] * S.wield_heft(c, cfg) + cfg['ACT_COMMIT'] * commit
                + cfg['ACT_WEIGHT'] / cfg['D_WT'] * max(0.0, cfg['ARMOR_DEMAND'][c.armor] - c.strength)) * cfg['COST_SCALE']

    strengths = (1, 4)
    key = 'attr.body.strength'

    def record(tier, shorts=None):
        return PersonalCombatInput(claimants=("A", "B"), ends=(4, 4), wound_quantities=("felled", "wounds", "max_wounds", "health_remaining", "health_full"),
                                   kits=(("arming", tier), ("arming", tier)), attributes=({key: strengths[0]}, {key: strengths[1]}),
                                   **({} if shorts is None else dict(short=shorts)))

    def round_one(rec, seed):
        out = entry.fight_round(DuelRoundInput(fighters=rec, states=(DuelState(), DuelState()), plans=({}, {}), round=1, prev_closed=False),
                                draw.seeded(draw.H2("harness_term", seed)))
        return tuple(s.stamina for s in out.states), out.trace

    checked = paid = 0
    for tier in sorted(K.ARMOUR_TIERS):
        shorts = tuple((K.shortfall((), tier, s), None) for s in strengths)
        paid += any(p > 0 for p, _ in shorts)
        for seed in range(3):
            after = (entry.fight(record(tier, shorts), draw.seeded(draw.H2("harness_fight", seed))), round_one(record(tier, shorts), seed))
            with monkeypatch.context() as m:
                m.setattr(S, 'act_cost', old_act_cost)
                before = (entry.fight(record(tier), draw.seeded(draw.H2("harness_fight", seed))), round_one(record(tier), seed))
            assert after == before, f"{tier}, seed {seed}: relocating the harness term moved the fight"
            checked += 1
    assert checked == 3 * len(K.ARMOUR_TIERS) and paid == 3
    heavy = tuple((K.shortfall((), 'heavy', s), None) for s in strengths)
    raised = tuple((p + 1.0, None) for p, _ in heavy)
    assert round_one(record('heavy', raised), 0)[0][0] < round_one(record('heavy', heavy), 0)[0][0], "a raised `short` spent no more stamina"
    # the close is slowed by a shortfall once CARRY_CLOSE_K is above 0, and by nothing at the shipped 0 (the control, bit for bit)
    slow = {**CFG, 'CARRY_CLOSE_K': 0.5}
    short_of, fit = _C.Combatant("S", weapon="spear", armor="heavy", short=2.0), _C.Combatant("F", weapon="spear", armor="heavy", short=0.0)
    assert S.close_rate(short_of, 1.0, 0.0, 1.0, slow) < S.close_rate(fit, 1.0, 0.0, 1.0, slow), "a shortfall slowed no one's close"
    assert S.close_rate(short_of, 1.0, 0.0, 1.0, CFG) == S.close_rate(fit, 1.0, 0.0, 1.0, CFG), "the shipped CARRY_CLOSE_K 0 is not the control"


# ── B18.09: the weapon in hand is round state; a switch costs tempo (`03_PC_loadout_and_carry` item 5) ──────────────

def test_a_switch_debits_one_act_threshold():
    """A `switch` spends one `ACT_THRESHOLD` of the switcher's readiness and puts the other weapon in hand. (1) THE DEBIT: a mirror
    in which A carries the very weapon he holds (so the swap changes nothing but the tempo), the same seeds with and without
    the switch: the `switch_paid` event's readiness is `ACT_THRESHOLD` below what it was, at the shipped threshold and at an overlaid one,
    and A takes fewer actions over the seeds. (2) THE HAND: a spear-and-dagger fighter who switches opens the round with the dagger,
    the round's `DuelState.form` records it, the next round (no switch) still holds it, and the carry follows: the figure
    `carry_short` reads is the secondary's entry of `short`, the spear now the carried weapon. (3) THE CLOSED SET: a fighter with no secondary
    never forms `switch` by the default rule (every weapon, both measures) and a decider that answers it raises as any answer outside
    the set does; with a secondary the same answer is taken."""
    import pytest
    from engine.dice_engine import draw
    from engine.season.queries.inputs import DuelRoundInput, DuelState, PersonalCombatInput
    from modules.combat import fight as entry
    C, S, _WP, CFG = _mods()
    quantities = ("felled", "wounds", "max_wounds", "health_remaining", "health_full")

    def record(kit_a, kit_b=("arming", None, "light"), short=()):
        return PersonalCombatInput(claimants=("A", "B"), ends=(4, 4), wound_quantities=quantities, kits=(kit_a, kit_b), short=short)

    def one_round(rec, seed, switch, cfg=None, states=(DuelState(), DuelState()), prev_closed=True, rnd=1):
        return entry.fight_round(DuelRoundInput(fighters=rec, states=states, plans=({}, {}), round=rnd, prev_closed=prev_closed, switch=switch),
                                 draw.seeded(draw.H2("switch_round", seed)), cfg=cfg)

    def opened_with(out):
        return [e for e in out.trace if e["kind"] == "engagement_start"][0]["weapon_A"]

    # (1) the debit
    mirror = record(("arming", "arming", "light"))
    for threshold in (CFG['ACT_THRESHOLD'], CFG['ACT_THRESHOLD'] + 1.0):
        cfg = {**CFG, 'ACT_THRESHOLD': threshold}
        debits, acts_with, acts_without = [], 0, 0
        for seed in range(24):
            with_ = one_round(mirror, seed, ("A",), cfg)
            without = one_round(mirror, seed, (), cfg)
            assert [e["by"] for e in with_.trace if e["kind"] == "switch"] == ["A"]
            assert not [e for e in without.trace if e["kind"] in ("switch", "switch_paid")]
            paid = [e for e in with_.trace if e["kind"] == "switch_paid"]   # none where the round ended before it reached the closed phase
            if paid:
                assert len(paid) == 1 and paid[0]["by"] == "A"
                debits.append(paid[0]["was"] - paid[0]["ready"])
            acts_with += sum(e["kind"] == "commit" and e["aggressor"] == "A" for e in with_.trace)
            acts_without += sum(e["kind"] == "commit" and e["aggressor"] == "A" for e in without.trace)
        assert len(debits) >= 12 and all(abs(d - threshold) < 1e-9 for d in debits), f"the debit is not one ACT_THRESHOLD ({threshold}): {debits}"
        assert acts_with < acts_without, "a switch that takes no tempo: A acted as often with it as without"

    # (2) the hand
    rec = record(("spear", "dagger", "heavy"), short=((0.0, 2.5), (0.0, None)))
    out = one_round(rec, 3, ("A",))
    assert opened_with(out) == "dagger" and [e for e in out.trace if e["kind"] == "engagement_start"][0]["weapon_B"] == "arming"
    assert C.HALFSWORD_BASE.get(out.states[0].form, out.states[0].form) == "dagger" and out.states[1].form == "arming"
    held, _ = entry._combatants(rec, CFG, out.states)
    assert (held.weapon, held.secondary, S.carry_short(held, CFG)) == ("dagger", "spear", 2.5)
    first, _ = entry._combatants(rec, CFG)
    assert (first.weapon, first.secondary, S.carry_short(first, CFG)) == ("spear", "dagger", 0.0)
    again = one_round(rec, 4, (), states=out.states, rnd=2)
    assert opened_with(again) == "dagger" and not [e for e in again.trace if e["kind"] == "switch"]
    assert opened_with(one_round(rec, 5, ("A",), states=again.states, rnd=3)) == "spear"

    # (3) the closed set
    alone = record(("spear", None, "light"))
    for key in C.WEAPONS:
        c = C.Combatant("X", weapon=key)
        assert not any(S.switch_wanted(c, closed, CFG) for closed in (True, False)), key
    with pytest.raises(ValueError):
        entry.fight(alone, draw.seeded(draw.H2("switch_set", 0)), decide=lambda view: "switch")
    taken = entry.fight(rec, draw.seeded(draw.H2("switch_set", 1)), decide=lambda view: "switch" if view.round == 1 else "withdraw")
    assert [e["by"] for e in taken.trace if e["kind"] == "switch"] == ["A"]

    # (4) THE DEFAULT RULE SEES ITSELF FIRE: a spear in hand with a dagger carried switches on a closed measure and on none else; the dagger in hand
    # with the spear carried never does; a fighter at the collapse line does not
    spear_dagger = C.Combatant("X", weapon="spear", secondary="dagger")
    assert S.switch_wanted(spear_dagger, True, CFG) and not S.switch_wanted(spear_dagger, False, CFG)
    assert not S.switch_wanted(C.Combatant("X", weapon="dagger", secondary="spear"), True, CFG)
    spent = C.Combatant("X", weapon="spear", secondary="dagger"); spent.stamina = CFG['STAMINA_COLLAPSE']
    assert not S.switch_wanted(spent, True, CFG)

    # (5) A SWITCH IS PAID IN THE CLOSED PHASE, SO A ROUND THAT NEVER CLOSES VOIDS IT: against a longer weapon at light armour the round may end in the
    # approach; there the swap goes back, no tempo was taken and the weapon in hand is the one he began with
    long_rec = record(("spear", "arming", "light"), kit_b=("yari", None, "light"))
    paid_n = void_n = 0
    for rec_5 in (long_rec, record(("spear", "arming", "light"))):   # against a yari the rounds end in the approach; against the arming sword they close
        for seed in range(24):
            out = one_round(rec_5, seed, ("A",))
            kinds = [e["kind"] for e in out.trace]
            in_hand = C.HALFSWORD_BASE.get(out.states[0].form, out.states[0].form)
            if "switch_void" in kinds:
                void_n += 1
                assert "switch_paid" not in kinds and in_hand == "spear", (seed, in_hand)
            elif "switch_paid" in kinds:
                paid_n += 1
                assert in_hand == "arming", (seed, in_hand)
    assert void_n >= 1 and paid_n >= 1, (void_n, paid_n)   # both outcomes were seen, so neither branch went unchecked

    # (6) `engage` IS THE ENGINE'S DEFAULT, NOT 'NO ONE SWITCHES': a decider that answers it every round plays the identical fight to no decider (REM-31's
    # AUTOMATED and PLAYABLE replay equal), a party with a secondary included
    for seed in range(4):
        auto = entry.fight(long_rec, draw.seeded(draw.H2("switch_engage", seed)))
        played = entry.fight(long_rec, draw.seeded(draw.H2("switch_engage", seed)), decide=lambda view: "engage")
        assert auto == played, seed
    assert any(e["kind"] == "switch" for e in auto.trace), "no switch under the default: the equality above could not have failed"

