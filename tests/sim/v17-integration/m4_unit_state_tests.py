"""m4_unit_state_tests — boundary tests for M4."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import m4_unit_state as m4


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
        _FAILURES.append((label, f"raised {type(e).__name__} instead of {exc_type.__name__}"))
        print(f"  ✗  {label}  — wrong exception: {type(e).__name__}")


def t1_schema():
    print("\n=== T1: schema — 9 classes, 3 active, 6 reserved ===")
    check(len(m4.UNIT_CLASSES) == 9, "9 unit classes")  # [canonical: see UNIT_CLASSES ledger]
    check(len(m4.ACTIVE_UNIT_CLASSES) == 3, "3 active classes")  # [canonical: see ACTIVE_UNIT_CLASSES ledger]
    check(len(m4.RESERVED_UNIT_CLASSES) == 6, "6 reserved classes")  # [canonical: see RESERVED_UNIT_CLASSES ledger]
    check(m4.ACTIVE_UNIT_CLASSES == {'Levy', 'LightInf', 'HeavyInf'},
          "Active = {Levy, LightInf, HeavyInf}")
    check(m4.RESERVED_UNIT_CLASSES == {'Cavalry', 'Archer', 'Crossbow', 'Sling', 'Artillery', 'KnightsTemplar'},
          "Reserved = {Cavalry, Archer, Crossbow, Sling, Artillery, KnightsTemplar}")
    check(set(m4.UNIT_CLASSES) == m4.ACTIVE_UNIT_CLASSES | m4.RESERVED_UNIT_CLASSES,
          "Active ∪ Reserved = all classes (no leaks)")
    check(m4.ACTIVE_UNIT_CLASSES.isdisjoint(m4.RESERVED_UNIT_CLASSES),
          "Active ∩ Reserved = ∅ (no overlaps)")
    # Stats dict completeness
    for cls in m4.UNIT_CLASSES:
        check(cls in m4.UNIT_STATS, f"  UNIT_STATS contains {cls}")
        required_fields = {'martial', 'endurance', 'discipline', 'health', 'bg_dmg_mod', 'ttrpg_dmg_mod', 'armour', 'anti_armour', 'volley'}
        check(set(m4.UNIT_STATS[cls].keys()) == required_fields,
              f"  {cls} has all 9 fields",
              detail=f"missing: {required_fields - set(m4.UNIT_STATS[cls].keys())}")


def t2_canonical_stat_values():
    print("\n=== T2: canonical stat values (mass_battle_v30 §B.2 table) ===")
    # Levy: 1/1/1/7, BG +1, TTRPG +1
    s = m4.UNIT_STATS['Levy']
    check(s['martial'] == 1 and s['endurance'] == 1 and s['discipline'] == 1 and s['health'] == 7,  # [canonical: see UNIT_STATS ledger]
          "Levy 1/1/1/7", detail=f"got {s['martial']}/{s['endurance']}/{s['discipline']}/{s['health']}")
    check(s['bg_dmg_mod'] == 1 and s['ttrpg_dmg_mod'] == 1, "Levy Dmg Mod BG+1 TTRPG+1")  # [canonical: see UNIT_STATS ledger]
    check(s['armour'] == 'None', "Levy armour None")

    # LightInf: 3/3/3/9, BG +2, TTRPG +1
    s = m4.UNIT_STATS['LightInf']
    check(s['martial'] == 3 and s['endurance'] == 3 and s['discipline'] == 3 and s['health'] == 9,  # [canonical: see UNIT_STATS ledger]
          "LightInf 3/3/3/9")
    check(s['armour'] == 'Light', "LightInf armour Light")
    check(s['bg_dmg_mod'] == 2 and s['ttrpg_dmg_mod'] == 1, "LightInf Dmg Mod BG+2 TTRPG+1")  # [canonical: see UNIT_STATS ledger]

    # HeavyInf: 4/4/4/10, BG +4, TTRPG +2
    s = m4.UNIT_STATS['HeavyInf']
    check(s['martial'] == 4 and s['endurance'] == 4 and s['discipline'] == 4 and s['health'] == 10,  # [canonical: see UNIT_STATS ledger]
          "HeavyInf 4/4/4/10")
    check(s['armour'] == 'Medium', "HeavyInf armour Medium")
    check(s['bg_dmg_mod'] == 4 and s['ttrpg_dmg_mod'] == 2, "HeavyInf Dmg Mod BG+4 TTRPG+2")  # [canonical: see UNIT_STATS ledger]

    # Cavalry: 4/3/5/9
    s = m4.UNIT_STATS['Cavalry']
    check(s['martial'] == 4 and s['endurance'] == 3 and s['discipline'] == 5 and s['health'] == 9,  # [canonical: see UNIT_STATS ledger]
          "Cavalry 4/3/5/9")
    check(s['armour'] == 'Heavy', "Cavalry armour Heavy")

    # Archer: 3/2/3/8
    s = m4.UNIT_STATS['Archer']
    check(s['martial'] == 3 and s['endurance'] == 2 and s['discipline'] == 3 and s['health'] == 8,  # [canonical: see UNIT_STATS ledger]
          "Archer 3/2/3/8")

    # KnightsTemplar: 5/5/6/11, BG +5, TTRPG +3
    s = m4.UNIT_STATS['KnightsTemplar']
    check(s['martial'] == 5 and s['endurance'] == 5 and s['discipline'] == 6 and s['health'] == 11,  # [canonical: see UNIT_STATS ledger]
          "KnightsTemplar 5/5/6/11")
    check(s['armour'] == 'Heavy', "KnightsTemplar armour Heavy")
    check(s['bg_dmg_mod'] == 5 and s['ttrpg_dmg_mod'] == 3, "KnightsTemplar Dmg Mod BG+5 TTRPG+3")  # [canonical: see UNIT_STATS ledger]

    # Artillery: 2/2/2/8
    s = m4.UNIT_STATS['Artillery']
    check(s['martial'] == 2 and s['endurance'] == 2 and s['discipline'] == 2 and s['health'] == 8,  # [canonical: see UNIT_STATS ledger]
          "Artillery 2/2/2/8")

    # Sling and Crossbow: 2/2/2/8 and 3/2/3/8 respectively
    s = m4.UNIT_STATS['Sling']
    check(s['martial'] == 2 and s['endurance'] == 2 and s['discipline'] == 2 and s['health'] == 8,  # [canonical: see UNIT_STATS ledger]
          "Sling 2/2/2/8")
    s = m4.UNIT_STATS['Crossbow']
    check(s['martial'] == 3 and s['endurance'] == 2 and s['discipline'] == 3 and s['health'] == 8,  # [canonical: see UNIT_STATS ledger]
          "Crossbow 3/2/3/8")


def t3_keyword_flags():
    print("\n=== T3: anti_armour and volley keyword flags ===")
    # Anti-Armour: HeavyBlunt units (Artillery + KnightsTemplar per §B.2 keyword)
    check(m4.UNIT_STATS['KnightsTemplar']['anti_armour'] is True, "KnightsTemplar anti_armour True")  # [canonical: see UNIT_STATS ledger]
    check(m4.UNIT_STATS['Artillery']['anti_armour'] is True, "Artillery anti_armour True")  # [canonical: see UNIT_STATS ledger]
    check(m4.UNIT_STATS['Levy']['anti_armour'] is False, "Levy anti_armour False")
    check(m4.UNIT_STATS['Cavalry']['anti_armour'] is False, "Cavalry anti_armour False (HeavyCut, not HeavyBlunt)")
    check(m4.UNIT_STATS['HeavyInf']['anti_armour'] is False, "HeavyInf anti_armour False")

    # Volley: Ranged + Artillery
    check(m4.UNIT_STATS['Archer']['volley'] is True, "Archer volley True")  # [canonical: see UNIT_STATS ledger]
    check(m4.UNIT_STATS['Crossbow']['volley'] is True, "Crossbow volley True")  # [canonical: see UNIT_STATS ledger]
    check(m4.UNIT_STATS['Sling']['volley'] is True, "Sling volley True")  # [canonical: see UNIT_STATS ledger]
    check(m4.UNIT_STATS['Artillery']['volley'] is True, "Artillery volley True")  # [canonical: see UNIT_STATS ledger]
    check(m4.UNIT_STATS['Levy']['volley'] is False, "Levy volley False")
    check(m4.UNIT_STATS['KnightsTemplar']['volley'] is False, "KnightsTemplar volley False (no melee→Volley)")


def t4_basic_ops():
    print("\n=== T4: UnitRoster basic operations ===")
    r = m4.UnitRoster()
    check(r.total_units() == 0, "Empty roster total = 0")
    check(r.unit_count('T1', 'Levy') == 0, "Empty roster unit_count = 0")
    check(r.units_in_territory('T1') == {}, "Empty territory dict = {}")
    check(r.territories_with_units() == set(), "No territories with units initially")

    r.muster('T1', 3, 'Levy')  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r.unit_count('T1', 'Levy') == 3, "After muster 3 Levy in T1 → 3")  # [canonical: see MUSTER_DEFAULT_CLASS ledger]
    check(r.total_units() == 3, "Total = 3")
    check(r.total_units('T1') == 3, "T1 total = 3")  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r.territories_with_units() == {'T1'}, "T1 in territories_with_units")

    # Muster more
    r.muster('T1', 2, 'LightInf')
    r.muster('T2', 4, 'HeavyInf')  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r.total_units() == 9, "Total after multi-muster = 9 (3+2+4)")  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r.total_units('T2') == 4, "T2 total = 4")  # [canonical: derived test boundary — see ledger entries + module constants]

    # Default class
    r2 = m4.UnitRoster()
    r2.muster('T1', 2)  # no class — should default to Levy
    check(r2.unit_count('T1', 'Levy') == 2, "Default muster class = Levy")  # [canonical: see MUSTER_DEFAULT_CLASS ledger]

    # Battle losses
    r.apply_battle_losses('T1', {'Levy': 1, 'LightInf': 2})
    check(r.unit_count('T1', 'Levy') == 2, "After losses: T1 Levy 3 - 1 = 2")
    check(r.unit_count('T1', 'LightInf') == 0, "After losses: T1 LightInf 2 - 2 = 0 (pruned)")
    check('LightInf' not in r.units_in_territory('T1'), "Zero count auto-pruned from territory dict")

    # Losses beyond count — clamps to 0, doesn't go negative
    r.apply_battle_losses('T1', {'Levy': 10})
    check(r.unit_count('T1', 'Levy') == 0, "Over-loss clamped to 0")


def t5_adjacency_commitment():
    print("\n=== T5: adjacency-gated commitment ===")
    r = m4.UnitRoster()
    r.muster('T1', 5, 'Levy')  # [canonical: derived test boundary — see ledger entries + module constants]
    r.muster('T1', 3, 'LightInf')  # [canonical: derived test boundary — see ledger entries + module constants]
    adjacency = {
        'T1': {'T2', 'T5'},  # [canonical: example adjacency for test]
        'T2': {'T1', 'T3'},
        'T3': {'T2'},
        'T5': {'T1'},
    }

    # Adjacent commit succeeds
    committed = r.commit_to_battle('T1', 'T2', {'Levy': 2}, adjacency)
    check(committed == {'Levy': 2}, "Adjacent commit T1→T2 of 2 Levy → returns committed dict",
          detail=f"got {committed}")
    check(r.unit_count('T1', 'Levy') == 3, "T1 Levy reduced 5→3")  # [canonical: derived test boundary — see ledger entries + module constants]
    check(r.unit_count('T2', 'Levy') == 0, "T2 Levy unchanged (caller forwards committed to battle)")

    # Non-adjacent raises
    check_raises(
        lambda: r.commit_to_battle('T1', 'T3', {'Levy': 1}, adjacency),
        ValueError,
        "Non-adjacent commit T1→T3 raises ValueError",
    )

    # Insufficient units raises
    check_raises(
        lambda: r.commit_to_battle('T1', 'T2', {'Levy': 100}, adjacency),
        ValueError,
        "Over-commit raises ValueError (insufficient Levy)",
    )

    # Reserved-class commit raises
    check_raises(
        lambda: r.commit_to_battle('T1', 'T2', {'Cavalry': 1}, adjacency),
        ValueError,
        "Reserved class commit raises ValueError",
    )

    # Reserved-class muster raises
    check_raises(
        lambda: r.muster('T1', 1, 'KnightsTemplar'),
        ValueError,
        "Reserved class muster raises ValueError",
    )

    # Unknown class raises
    check_raises(
        lambda: r.muster('T1', 1, 'Wizard'),
        ValueError,
        "Unknown class muster raises ValueError",
    )

    # Non-positive count raises
    check_raises(
        lambda: r.muster('T1', 0, 'Levy'),
        ValueError,
        "Zero count muster raises ValueError",
    )
    check_raises(
        lambda: r.muster('T1', -1, 'Levy'),
        ValueError,
        "Negative count muster raises ValueError",
    )


def t6_serialization():
    print("\n=== T6: JSONL serialization round-trip ===")
    # Empty roster
    r1 = m4.UnitRoster()
    d = r1.to_dict()
    check(d == {}, "Empty roster to_dict = {}")
    r1b = m4.UnitRoster.from_dict(d)
    check(r1 == r1b, "Empty roster round-trips")

    # Single-territory single-class
    r2 = m4.UnitRoster()
    r2.muster('T1', 3, 'Levy')  # [canonical: derived test boundary — see ledger entries + module constants]
    d = r2.to_dict()
    check(d == {'T1': {'Levy': 3}}, "Single muster serializes correctly",  # [canonical: derived test boundary — see ledger entries + module constants]
          detail=f"got {d}")
    r2b = m4.UnitRoster.from_dict(d)
    check(r2 == r2b, "Single-muster round-trip")

    # Multi-territory multi-class
    r3 = m4.UnitRoster()
    r3.muster('T1', 3, 'Levy')  # [canonical: derived test boundary — see ledger entries + module constants]
    r3.muster('T1', 2, 'LightInf')
    r3.muster('T2', 4, 'HeavyInf')  # [canonical: derived test boundary — see ledger entries + module constants]
    r3.muster('T5', 1, 'Levy')
    d = r3.to_dict()
    expected = {
        'T1': {'Levy': 3, 'LightInf': 2},  # [canonical: derived test boundary — see ledger entries + module constants]
        'T2': {'HeavyInf': 4},  # [canonical: derived test boundary — see ledger entries + module constants]
        'T5': {'Levy': 1},
    }
    check(d == expected, "Multi-state serializes correctly",
          detail=f"got {d}")
    r3b = m4.UnitRoster.from_dict(d)
    check(r3 == r3b, "Multi-state round-trip")

    # JSON form round-trip
    js = r3.to_json()
    r3c = m4.UnitRoster.from_json(js)
    check(r3 == r3c, "JSON round-trip")

    # from_dict validates schema
    check_raises(
        lambda: m4.UnitRoster.from_dict({'T1': {'Wizard': 3}}),  # [canonical: derived test boundary — see ledger entries + module constants]
        ValueError,
        "from_dict rejects unknown unit class",
    )
    check_raises(
        lambda: m4.UnitRoster.from_dict({'T1': {'Levy': -1}}),
        ValueError,
        "from_dict rejects negative count",
    )


def t7_pool_contribution():
    print("\n=== T7: pool_contribution for resolve_battle Step 3 ===")
    check(m4.pool_contribution({}) == 0, "Empty commitment → pool 0")  # [canonical: see pool_contribution ledger]
    check(m4.pool_contribution({'Levy': 3}) == 3, "{Levy: 3} → 3 (3×1)")  # [canonical: see pool_contribution ledger]
    check(m4.pool_contribution({'Levy': 2, 'LightInf': 1}) == 5, "{Levy:2, LightInf:1} → 5 (2×1 + 1×3)")  # [canonical: see pool_contribution ledger]
    check(m4.pool_contribution({'HeavyInf': 5}) == 20, "{HeavyInf:5} → 20 (5×4)")  # [canonical: see pool_contribution ledger]
    check(m4.pool_contribution({'KnightsTemplar': 2}) == 10, "{KnightsTemplar:2} → 10 (2×5)")  # [canonical: see pool_contribution ledger]
    # Heterogeneous including reserved classes (pool_contribution doesn't gate on active)
    check(m4.pool_contribution({'Levy': 1, 'Cavalry': 1, 'KnightsTemplar': 1}) == 1 + 4 + 5,  # [canonical: derived test boundary — see ledger entries + module constants]
          "Heterogeneous pool sums all Martial")  # [canonical: see pool_contribution ledger]
    # Unknown class raises
    check_raises(
        lambda: m4.pool_contribution({'Wizard': 1}),
        ValueError,
        "Unknown unit class in pool_contribution raises",
    )


def run_all():
    print("=" * 100)  # [canonical: N/A — display formatting]
    print("M4 Unit State Management — Test Suite")
    print("=" * 100)  # [canonical: N/A — display formatting]
    t1_schema()
    t2_canonical_stat_values()
    t3_keyword_flags()
    t4_basic_ops()
    t5_adjacency_commitment()
    t6_serialization()
    t7_pool_contribution()
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
