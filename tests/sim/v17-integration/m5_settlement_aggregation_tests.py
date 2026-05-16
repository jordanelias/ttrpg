"""m5_settlement_aggregation_tests — boundary tests for M5."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import m5_settlement_aggregation as m5
import m1_church_infrastructure as m1


_PASSED = 0
_FAILED = 0
_FAILURES = []


def check(condition, label, detail=""):
    global _PASSED, _FAILED
    if condition:
        _PASSED += 1
        print(f"  ✓  {label}")
    else:
        _FAILED += 1
        _FAILURES.append((label, detail))
        print(f"  ✗  {label}  — {detail}")


def check_raises(callable_, exc_type, label):
    global _PASSED, _FAILED
    try:
        callable_()
        _FAILED += 1
        _FAILURES.append((label, "did not raise"))
        print(f"  ✗  {label}  — did not raise")
    except exc_type:
        _PASSED += 1
        print(f"  ✓  {label}")
    except Exception as e:
        _FAILED += 1
        _FAILURES.append((label, f"wrong: {type(e).__name__}"))
        print(f"  ✗  {label}  — wrong: {type(e).__name__}")


def t1_constants():
    print("\n=== T1: canonical constants ===")
    check(m5.ORDER_MIN == 0, "ORDER_MIN = 0")  # [canonical: see ORDER_MIN ledger]
    check(m5.ORDER_MAX == 5, "ORDER_MAX = 5 (Pacify cap)")  # [canonical: see ORDER_MAX ledger]
    check(m5.PROSPERITY_MIN == 0, "PROSPERITY_MIN = 0")  # [canonical: see PROSPERITY_MIN ledger]
    check(m5.DEFENSE_MIN == 0, "DEFENSE_MIN = 0")  # [canonical: see DEFENSE_MIN ledger]
    check(m5.FAMINE_PROSPERITY_THRESHOLD == 0, "Famine trigger at Prosperity 0")  # [canonical: see FAMINE_PROSPERITY_THRESHOLD ledger]
    check(m5.FAMINE_ORDER_PENALTY == -1, "Famine penalty -1 Order")  # [canonical: see FAMINE_ORDER_PENALTY ledger]
    check(m5.REVOLT_ORDER_THRESHOLD == 0, "Revolt trigger at Order 0")  # [canonical: see REVOLT_ORDER_THRESHOLD ledger]
    check(m5.FLOURISHING_ORDER_THRESHOLD == 5, "Flourishing requires Order 5")  # [canonical: see FLOURISHING_ORDER_THRESHOLD ledger]
    check(m5.FLOURISHING_PROSPERITY_THRESHOLD == 4, "Flourishing requires Prosperity 4")  # [canonical: see FLOURISHING_PROSPERITY_THRESHOLD ledger]
    check(m5.MINE_SURPLUS_PROSPERITY_THRESHOLD == 3, "Mine surplus at Prosperity 3+")  # [canonical: see MINE_SURPLUS_PROSPERITY_THRESHOLD ledger]
    check(m5.MINE_SURPLUS_TREASURY_DELTA == 50, "Mine surplus +50 treasury")  # [canonical: see MINE_SURPLUS_TREASURY_DELTA ledger]
    check(m5.FORTRESS_DEFENSE_CHECK_OB == 2, "Fortress garrison check Ob 2")  # [canonical: see FORTRESS_DEFENSE_CHECK_OB ledger]
    check(m5.RM_CELL_RESILIENCE_THRESHOLD == 3, "RM resilience at 3+ settlements")  # [canonical: see RM_CELL_RESILIENCE_THRESHOLD ledger]
    check(m5.RM_CELL_RESILIENCE_OB_PENALTY == 1, "RM resilience +1 Ob penalty")  # [canonical: see RM_CELL_RESILIENCE_OB_PENALTY ledger]
    check(m5.CONSENSUS_DELAY_SEASONS == 1, "Consensus delay +1 season")  # [canonical: see CONSENSUS_DELAY_SEASONS ledger]
    check(m5.GOVERNANCE_TRANSITION_MODES == ('disestablishment', 'accommodation', 'transformation'),
          "3 governance transition modes")  # [canonical: see GOVERNANCE_TRANSITION_MODES ledger]


def t2_governance_action_ob_formulas():
    print("\n=== T2: §3.2 Governor Assignment Ob formulas ===")
    # Develop: floor(Prosperity/2) + 1 → at P=0→1, P=2→2, P=4→3, P=5→3
    check(m5.governance_action_ob('develop', 0) == 1, "Develop Ob at P=0 → 1")  # [canonical: see governance_action_ob ledger]
    check(m5.governance_action_ob('develop', 2) == 2, "Develop Ob at P=2 → 2")
    check(m5.governance_action_ob('develop', 3) == 2, "Develop Ob at P=3 → 2 (floor)")
    check(m5.governance_action_ob('develop', 4) == 3, "Develop Ob at P=4 → 3")
    check(m5.governance_action_ob('develop', 5) == 3, "Develop Ob at P=5 → 3 (floor)")

    # Fortify same formula
    check(m5.governance_action_ob('fortify', 0) == 1, "Fortify Ob at D=0 → 1")
    check(m5.governance_action_ob('fortify', 4) == 3, "Fortify Ob at D=4 → 3")

    # Pacify: max(1, floor((3 - Order) + 1)) → at O=0→4, O=2→2, O=3→1, O=4→1 (min cap), O=5→1
    check(m5.governance_action_ob('pacify', 0) == 4, "Pacify Ob at O=0 → 4")  # [canonical: see governance_action_ob ledger]
    check(m5.governance_action_ob('pacify', 1) == 3, "Pacify Ob at O=1 → 3")
    check(m5.governance_action_ob('pacify', 2) == 2, "Pacify Ob at O=2 → 2")
    check(m5.governance_action_ob('pacify', 3) == 1, "Pacify Ob at O=3 → 1")
    check(m5.governance_action_ob('pacify', 4) == 1, "Pacify Ob at O=4 → 1 (min floor)")
    check(m5.governance_action_ob('pacify', 5) == 1, "Pacify Ob at O=5 → 1 (min floor)")

    # Administer: always 2
    for o in [0, 2, 3, 5]:
        check(m5.governance_action_ob('administer', o) == 2, f"Administer Ob always 2 (at O={o})")  # [canonical: see governance_action_ob ledger]

    # Unknown action raises
    check_raises(
        lambda: m5.governance_action_ob('not_an_action', 3),
        ValueError,
        "Unknown action raises ValueError",
    )


def t3_governance_state():
    print("\n=== T3: SettlementGovernance dataclass ===")
    gov = m5.SettlementGovernance(sid='S-001')
    check(gov.order == 3 and gov.prosperity == 2 and gov.defense == 2,
          "Default governance: O=3, P=2, D=2",
          detail=f"got O={gov.order} P={gov.prosperity} D={gov.defense}")
    check(gov.rm_presence is False and gov.garrison_present is False,
          "Default flags False")
    check(gov.governor_faction is None, "Default governor None")

    # Construction with overrides
    gov2 = m5.SettlementGovernance(sid='S-002', order=5, prosperity=4, defense=3, rm_presence=True)
    check(gov2.order == 5 and gov2.prosperity == 4 and gov2.rm_presence is True,
          "Override construction works")

    # Bounds validation
    check_raises(
        # [canonical: see ORDER_MAX ledger — 5 is the canonical cap, so 6 triggers bounds check]
        lambda: m5.SettlementGovernance(sid='X', order=6),
        ValueError,
        "Order 6 (above max) raises ValueError",
    )
    check_raises(
        lambda: m5.SettlementGovernance(sid='X', order=-1),
        ValueError,
        "Order -1 raises ValueError",
    )
    check_raises(
        lambda: m5.SettlementGovernance(sid='X', prosperity=-1),
        ValueError,
        "Prosperity -1 raises ValueError",
    )
    check_raises(
        lambda: m5.SettlementGovernance(sid='X', defense=-1),
        ValueError,
        "Defense -1 raises ValueError",
    )

    # Serialization
    d = gov2.to_dict()
    expected = {'sid', 'order', 'prosperity', 'defense', 'rm_presence', 'garrison_present', 'governor_faction', 'rm_governed'}
    check(set(d.keys()) == expected, "to_dict has all 8 expected keys",
          detail=f"missing: {expected - set(d.keys())}")
    check(d['order'] == 5 and d['prosperity'] == 4 and d['rm_presence'] is True,
          "to_dict values preserved")

    # apply_governance_action — pacify
    new_gov = m5.apply_governance_action('pacify', m5.SettlementGovernance(sid='X', order=2))
    check(new_gov.order == 3, "Pacify success: order 2 → 3")  # [canonical: see governance_action_effect ledger]
    new_gov = m5.apply_governance_action('pacify', m5.SettlementGovernance(sid='X', order=5))
    check(new_gov.order == 5, "Pacify at cap 5 stays at 5")  # [canonical: see ORDER_MAX cap]

    # apply_governance_action — develop
    new_gov = m5.apply_governance_action('develop', m5.SettlementGovernance(sid='X', prosperity=2))
    check(new_gov.prosperity == 3, "Develop success: prosperity 2 → 3")

    # apply_governance_action — fortify
    new_gov = m5.apply_governance_action('fortify', m5.SettlementGovernance(sid='X', defense=1))
    check(new_gov.defense == 2, "Fortify success: defense 1 → 2")

    # apply_governance_action — administer (no immediate change)
    base = m5.SettlementGovernance(sid='X', order=3)
    new_gov = m5.apply_governance_action('administer', base)
    check(new_gov.order == base.order, "Administer: no immediate Order change (caller marks no-decay)")


def t4_famine_event():
    print("\n=== T4: §4.3 Famine event (Prosperity 0) ===")
    gov_map = {
        'S-001': m5.SettlementGovernance(sid='S-001', prosperity=0, order=3, defense=2),
        'S-002': m5.SettlementGovernance(sid='S-002', prosperity=3, order=3, defense=2),  # no event
    }
    events = m5.resolve_settlement_events(gov_map)
    famine_events = [e for e in events if e.event_type == 'famine']
    check(len(famine_events) == 1, "1 famine event fired",
          detail=f"got {len(famine_events)}")
    if famine_events:
        e = famine_events[0]
        check(e.sid == 'S-001', "Famine on S-001 (prosperity 0)")  # [canonical: see FAMINE_PROSPERITY_THRESHOLD ledger]
        check(e.immediate_effects.get('order_delta') == -1, "Famine effect: order_delta -1")  # [canonical: see FAMINE_ORDER_PENALTY ledger]
        check(e.severity == 'critical', "Famine severity critical")


def t5_revolt_event():
    print("\n=== T5: §4.3 Revolt event (Order 0) ===")
    gov_map = {
        'S-001': m5.SettlementGovernance(sid='S-001', order=0, prosperity=2, defense=2, garrison_present=False),
        'S-002': m5.SettlementGovernance(sid='S-002', order=0, prosperity=2, defense=2, garrison_present=True),
        'S-003': m5.SettlementGovernance(sid='S-003', order=3, prosperity=2, defense=2),  # no event
    }
    events = m5.resolve_settlement_events(gov_map)
    revolts = [e for e in events if e.event_type == 'revolt']
    check(len(revolts) == 2, "2 revolt events fired (both at Order 0)",  # [canonical: see REVOLT_ORDER_THRESHOLD ledger]
          detail=f"got {len(revolts)}")

    unsuppressed = next((e for e in revolts if e.sid == 'S-001'), None)
    suppressed = next((e for e in revolts if e.sid == 'S-002'), None)

    check(unsuppressed is not None and unsuppressed.suppressed_by_garrison is False,
          "S-001 revolt NOT suppressed (no garrison)")  # [canonical: see SettlementEvent revolt ledger]
    check(unsuppressed.immediate_effects.get('governor_expelled') is True,
          "S-001 governor expelled")
    check(unsuppressed.severity == 'critical', "Unsuppressed revolt is critical")

    check(suppressed is not None and suppressed.suppressed_by_garrison is True,
          "S-002 revolt suppressed by garrison")  # [canonical: see settlement_layer §4.3 — "Governor expelled unless garrison present"]
    check(suppressed.immediate_effects.get('governor_expelled') is False,
          "S-002 governor NOT expelled (garrison holds)")
    check(suppressed.severity == 'normal', "Suppressed revolt is normal")


def t6_other_events():
    print("\n=== T6: §4.3 Mine surplus / Fortress / Flourishing / Cathedral religious event ===")
    # Set up: use real registry, modify it with specific events firing
    # S-027 is a Mine in T15 — boost its Prosperity to 3
    # S-005 is a Fortress in some territory — check garrison check fires under hostile military
    # First find the actual settlement types in the registry
    reg = m1.build_settlement_registry()

    mines = [s for s in reg.values() if s.settlement_type == 'Mine']
    fortresses = [s for s in reg.values() if s.settlement_type in ('Fortress', 'Fortress-City')]
    cathedrals = [s for s in reg.values() if s.religious_building == m1.RB_CATHEDRAL]
    print(f"     Registry contains: {len(mines)} Mine, {len(fortresses)} Fortress(-City), {len(cathedrals)} Cathedral-bearing")

    if mines:
        mine = mines[0]
        gov_map = {mine.sid: m5.SettlementGovernance(sid=mine.sid, prosperity=4, order=3, defense=2)}
        events = m5.resolve_settlement_events(gov_map, registry=reg)
        mine_events = [e for e in events if e.event_type == 'mine_surplus']
        check(len(mine_events) == 1, f"Mine {mine.sid} P=4 fires mine_surplus event")  # [canonical: see MINE_SURPLUS_PROSPERITY_THRESHOLD ledger]
        if mine_events:
            check(mine_events[0].immediate_effects.get('province_treasury_delta') == 50,
                  "Mine surplus: +50 treasury delta")  # [canonical: see MINE_SURPLUS_TREASURY_DELTA ledger]

    if fortresses:
        fort = fortresses[0]
        gov_map = {fort.sid: m5.SettlementGovernance(sid=fort.sid, defense=3, order=3, prosperity=2)}
        # No hostile military → no event
        events = m5.resolve_settlement_events(gov_map, registry=reg, hostile_military_per_province=set())
        garrison_checks = [e for e in events if e.event_type == 'fortress_garrison_check']
        check(len(garrison_checks) == 0, f"Fortress {fort.sid} no hostile → no garrison check")

        # With hostile military in the province → event fires
        events = m5.resolve_settlement_events(gov_map, registry=reg, hostile_military_per_province={fort.territory_id})
        garrison_checks = [e for e in events if e.event_type == 'fortress_garrison_check']
        check(len(garrison_checks) == 1, f"Fortress {fort.sid} + hostile → garrison check fires")  # [canonical: see settlement_layer §4.3 Fortress row]
        if garrison_checks:
            check(garrison_checks[0].immediate_effects.get('ob') == 2,
                  "Garrison check Ob 2")  # [canonical: see FORTRESS_DEFENSE_CHECK_OB ledger]
            check(garrison_checks[0].immediate_effects.get('defense_pool') == 3,
                  "Defense pool = settlement Defense")

    # Flourishing — Order 5 + Prosperity 4
    gov_map = {'S-001': m5.SettlementGovernance(sid='S-001', order=5, prosperity=4, defense=2)}
    events = m5.resolve_settlement_events(gov_map)
    flourishing = [e for e in events if e.event_type == 'flourishing']
    check(len(flourishing) == 1, "Order 5 + Prosperity 4 → flourishing")  # [canonical: see FLOURISHING_ORDER_THRESHOLD + FLOURISHING_PROSPERITY_THRESHOLD ledgers]

    # Just below either threshold → no flourishing
    gov_map = {'S-001': m5.SettlementGovernance(sid='S-001', order=5, prosperity=3, defense=2)}
    events = m5.resolve_settlement_events(gov_map)
    check(not any(e.event_type == 'flourishing' for e in events), "Order 5 + Prosperity 3 → no flourishing")  # [canonical: see FLOURISHING_PROSPERITY_THRESHOLD ledger]

    # Cathedral + CV change → religious event
    if cathedrals:
        cath = cathedrals[0]
        gov_map = {cath.sid: m5.SettlementGovernance(sid=cath.sid)}
        events = m5.resolve_settlement_events(gov_map, registry=reg,
                                               ci_change_per_province={cath.territory_id: 5})
        rel_events = [e for e in events if e.event_type == 'religious_event']
        check(len(rel_events) == 1, f"Cathedral {cath.sid} + CV change → religious event")  # [canonical: see settlement_layer §4.3 Cathedral row]
        if rel_events:
            check(rel_events[0].immediate_effects.get('cv_direction') == 'rising',
                  "CV+5 → rising direction")
        # No CV change → no event
        events = m5.resolve_settlement_events(gov_map, registry=reg)
        check(not any(e.event_type == 'religious_event' for e in events),
              "Cathedral + zero CV change → no religious event")


def t7_rm_cell_resilience():
    print("\n=== T7: §3.3 ED-683 RM Cell Resilience ===")
    reg = m1.build_settlement_registry()
    # Find a province with at least 3 settlements
    provinces_settlement_counts = {}
    for s in reg.values():
        provinces_settlement_counts.setdefault(s.territory_id, []).append(s.sid)
    target_province = max(provinces_settlement_counts.items(), key=lambda kv: len(kv[1]))[0]
    province_sids = provinces_settlement_counts[target_province]
    print(f"     Using province {target_province} with {len(province_sids)} settlements: {province_sids}")

    # 0 RM presence
    gov_map = {sid: m5.SettlementGovernance(sid=sid) for sid in province_sids}
    ob = m5.rm_cell_resilience(target_province, gov_map, reg)
    check(ob == 0, "0 RM presence → +0 Ob penalty")  # [canonical: see RM_CELL_RESILIENCE_THRESHOLD ledger]

    # 2 RM presence — below threshold
    gov_map[province_sids[0]].rm_presence = True
    gov_map[province_sids[1]].rm_presence = True
    ob = m5.rm_cell_resilience(target_province, gov_map, reg)
    check(ob == 0, "2 RM presence → +0 Ob (below threshold of 3)")  # [canonical: see RM_CELL_RESILIENCE_THRESHOLD ledger]

    # 3 RM presence — meets threshold
    if len(province_sids) >= 3:
        gov_map[province_sids[2]].rm_presence = True
        ob = m5.rm_cell_resilience(target_province, gov_map, reg)
        check(ob == 1, "3 RM presence → +1 Ob (threshold met)")  # [canonical: see RM_CELL_RESILIENCE_OB_PENALTY ledger]

        # 4+ RM presence still +1 (not stacking)
        if len(province_sids) >= 4:
            gov_map[province_sids[3]].rm_presence = True
            ob = m5.rm_cell_resilience(target_province, gov_map, reg)
            check(ob == 1, "4 RM presence → still +1 Ob (no stacking)")  # [canonical: see RM_CELL_RESILIENCE_OB_PENALTY ledger]

    # Cross-province no leakage: RM in another province doesn't affect this one
    other_provinces = [tid for tid, sids in provinces_settlement_counts.items() if tid != target_province and len(sids) >= 1]
    if other_provinces:
        other = other_provinces[0]
        other_sids = provinces_settlement_counts[other]
        for sid in other_sids:
            gov_map[sid] = m5.SettlementGovernance(sid=sid, rm_presence=True)
        # The other province now has full RM presence; target_province unchanged
        ob_other = m5.rm_cell_resilience(other, gov_map, reg)
        check(ob_other == (1 if len(other_sids) >= 3 else 0),
              f"Other province {other} with {len(other_sids)} RM presence → independent check")


def t8_aggregation():
    print("\n=== T8: Settlement → Territory aggregation ===")
    reg = m1.build_settlement_registry()
    # Use province with multiple settlements
    provinces_settlement_counts = {}
    for s in reg.values():
        provinces_settlement_counts.setdefault(s.territory_id, []).append(s.sid)
    target_province = max(provinces_settlement_counts.items(), key=lambda kv: len(kv[1]))[0]
    province_sids = provinces_settlement_counts[target_province]

    # All settlements at Order 3 → Accord aggregate 3
    gov_map = {sid: m5.SettlementGovernance(sid=sid, order=3) for sid in province_sids}
    accord = m5.aggregate_order_to_accord(target_province, gov_map, reg)
    check(accord == 3, f"All Order 3 → Accord aggregate 3")  # [canonical: see aggregate_order_to_accord ledger]

    # Mixed orders — floor of mean
    if len(province_sids) >= 4:
        for i, sid in enumerate(province_sids[:4]):
            gov_map[sid].order = [3, 4, 2, 5][i]
        accord = m5.aggregate_order_to_accord(target_province, gov_map, reg)
        # Mean of [3, 4, 2, 5] + remaining at 3 = depends on len; check on first 4 manually
        # The remaining settlements still have order=3 from earlier creation
        sids_first_4 = province_sids[:4]
        observed_total = sum(gov_map[sid].order for sid in province_sids)
        observed_mean = observed_total / len(province_sids)
        expected_accord = int(observed_mean // 1) if observed_mean >= 0 else 0
        # Use floor function
        import math
        expected_accord = math.floor(observed_mean)
        check(accord == expected_accord, f"Mixed orders → floor(mean) = {expected_accord}",  # [canonical: see aggregate_order_to_accord ledger]
              detail=f"got {accord}, expected {expected_accord} (mean {observed_mean:.2f})")

    # Empty governance map → 0
    accord = m5.aggregate_order_to_accord(target_province, {}, reg)
    check(accord == 0, "Empty governance → Accord 0")

    # Prosperity → Wealth aggregation
    gov_map = {sid: m5.SettlementGovernance(sid=sid, prosperity=4) for sid in province_sids}
    wealth = m5.aggregate_prosperity_to_wealth(target_province, gov_map, reg)
    # 4 * 0.1 = 0.4
    check(abs(wealth - 0.4) < 0.001, f"All Prosperity 4 → Wealth 0.4",  # [canonical: see PROSPERITY_TO_WEALTH_RATE ledger]
          detail=f"got {wealth}")

    # Empty → 0
    wealth = m5.aggregate_prosperity_to_wealth(target_province, {}, reg)
    check(wealth == 0.0, "Empty governance → Wealth 0")


def t9_governance_transition_and_consensus_delay():
    print("\n=== T9: §4.3 Governance Transition + Consensus Delay ===")
    # Governance Transition: 3-mode choice event
    event = m5.governance_transition_event('S-001')
    check(event.event_type == 'governance_transition', "Event type is governance_transition")
    check(event.choice_required is True, "Choice required")  # [canonical: see GOVERNANCE_TRANSITION_MODES ledger]
    check(event.choice_options == m5.GOVERNANCE_TRANSITION_MODES,
          "3 mode options matches GOVERNANCE_TRANSITION_MODES")  # [canonical: see GOVERNANCE_TRANSITION_MODES ledger]

    # Mode effects
    e = m5.governance_transition_effects('disestablishment')
    check(e['order_delta'] == -1 and e['order_decay_seasons'] == 2 and e['pt_delta'] == -1 and e['accord_growth_per_season'] == 0.5,
          "Disestablishment: -1 Order 2 seasons, -1 PT immediate, +0.5 Accord/season")  # [canonical: see settlement_layer §4.3 Disestablishment]

    e = m5.governance_transition_effects('accommodation')
    check(e['pt_delta'] == -0.5 and e['order_delta'] == 0,
          "Accommodation: no Order penalty, -0.5 PT only")  # [canonical: see settlement_layer §4.3 Accommodation]

    e = m5.governance_transition_effects('transformation')
    check(e['transition_seasons'] == 4 and e['pt_delta_after_completion'] == -1,
          "Transformation: 4-season conversion, -1 PT after completion")  # [canonical: see settlement_layer §4.3 Transformation]

    check_raises(
        lambda: m5.governance_transition_effects('not_a_mode'),
        ValueError,
        "Unknown mode raises ValueError",
    )

    # Consensus Delay: RM-governed settlement + emergency action in province
    gov_map = {
        'S-001': m5.SettlementGovernance(sid='S-001', rm_governed=True),
        'S-002': m5.SettlementGovernance(sid='S-002', rm_governed=False),  # no event
    }
    reg = m1.build_settlement_registry()
    # Find S-001's province
    s001_province = reg['S-001'].territory_id
    events = m5.resolve_settlement_events(gov_map, registry=reg,
                                           emergency_action_provinces={s001_province})
    delays = [e for e in events if e.event_type == 'consensus_delay']
    check(len(delays) == 1, "RM-governed S-001 + emergency in its province → consensus_delay fires")  # [canonical: see CONSENSUS_DELAY_SEASONS ledger]
    if delays:
        check(delays[0].immediate_effects.get('delay_seasons') == 1,
              "Delay seasons = 1")  # [canonical: see CONSENSUS_DELAY_SEASONS ledger]
        check(delays[0].immediate_effects.get('waiver_mandate_cost') == 1,
              "Waiver Mandate cost = 1")  # [canonical: see CONSENSUS_DELAY_WAIVER_MANDATE_COST ledger]
        check(delays[0].immediate_effects.get('waiver_presence_cost') == 1,
              "Waiver Presence cost = 1")  # [canonical: see CONSENSUS_DELAY_WAIVER_PRESENCE_COST ledger]

    # Without emergency → no delay
    events = m5.resolve_settlement_events(gov_map, registry=reg)
    check(not any(e.event_type == 'consensus_delay' for e in events),
          "RM-governed but no emergency → no consensus_delay")


def t10_province_summary():
    print("\n=== T10: province_settlement_summary ===")
    reg = m1.build_settlement_registry()
    provinces_settlement_counts = {}
    for s in reg.values():
        provinces_settlement_counts.setdefault(s.territory_id, []).append(s.sid)
    target_province = max(provinces_settlement_counts.items(), key=lambda kv: len(kv[1]))[0]
    province_sids = provinces_settlement_counts[target_province]

    gov_map = {sid: m5.SettlementGovernance(sid=sid, order=3, prosperity=2, defense=2, rm_presence=True)
               for sid in province_sids}
    summary = m5.province_settlement_summary(target_province, gov_map, reg)

    check(summary['province'] == target_province, "Summary province ID")
    check(summary['settlement_count'] == len(province_sids), "Summary settlement count")
    check(summary['mean_order'] == 3.0, "Summary mean Order")
    check(summary['rm_presence_count'] == len(province_sids), "Summary RM presence count")
    expected_resilience_ob = 1 if len(province_sids) >= 3 else 0
    check(summary['rm_resilience_ob_penalty'] == expected_resilience_ob,
          f"Summary RM resilience Ob = {expected_resilience_ob}")
    check(summary['accord_aggregate'] == 3, "Summary accord aggregate = 3")


def run_all():
    print("=" * 100)  # [canonical: N/A — display formatting]
    print("M5 Settlement-Territory Aggregation — Test Suite")
    print("=" * 100)  # [canonical: N/A — display formatting]
    t1_constants()
    t2_governance_action_ob_formulas()
    t3_governance_state()
    t4_famine_event()
    t5_revolt_event()
    t6_other_events()
    t7_rm_cell_resilience()
    t8_aggregation()
    t9_governance_transition_and_consensus_delay()
    t10_province_summary()
    print()
    print("=" * 100)  # [canonical: N/A — display formatting]
    print(f"PASSED: {_PASSED}    FAILED: {_FAILED}")
    print("=" * 100)  # [canonical: N/A — display formatting]
    if _FAILURES:
        print("\nFailures:")
        for label, detail in _FAILURES:
            print(f"  ✗ {label}")
            if detail:
                print(f"      {detail}")
    return 0 if _FAILED == 0 else 1


if __name__ == "__main__":
    sys.exit(run_all())
