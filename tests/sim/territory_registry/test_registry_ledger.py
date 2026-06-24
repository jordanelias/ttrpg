"""
Test: settlement registry + ledger (sim_build_spec §1-§2 / audit gap G1).

Run:  PYTHONPATH=<repo-root> python tests/sim/territory_registry/test_registry_ledger.py
"""
import math

from sim.autoload.game_state import create_world
from sim.territory import registry as reg
from sim.territory.settlement import compute_settlement_state, aggregate_to_province


def test_ap_economy():
    town = reg.Settlement(sid="S-006", name="Goldenfurt", stype="Town",
                          province_id="Kronmark", facility_tier=1)
    assert town.ap == 3, town.ap                     # 2 + FacilityTier(1)
    seat = reg.Settlement(sid="S-001", name="Valorsplatz", stype="Seat",
                          province_id="Valorsplatz", facility_tier=3)
    assert seat.ap == 6, seat.ap                     # 2 + 3 + 1 (Seat bonus)


def test_ledger_survives_succession():
    reg.reset_registry()
    s = reg.register_settlement(reg.Settlement(
        sid="S-006", name="Goldenfurt", stype="Town",
        province_id="Kronmark", governor_id="PC"))
    s.add_tag("Precedent", "only-sons-exempt")                  # durable (ttl=None)
    s.add_tag("Grudge", "Orsk", ttl=3, created_season=0)        # transient
    assert s.has_tag("Precedent", "only-sons-exempt")
    # succession at season 5: durable survives; the ttl-3 grudge (from s0) is swept
    reg.succeed_governor("S-006", "NPC-successor", season=5)
    assert s.governor_id == "NPC-successor"
    assert s.has_tag("Precedent", "only-sons-exempt"), "durable Precedent must survive succession"
    assert not s.has_tag("Grudge", "Orsk"), "expired transient Grudge should be swept"


def test_reputation_single_valued():
    s = reg.Settlement(sid="X", name="X", stype="Town", province_id="P")
    s.add_tag("Reputation", "Just")
    s.add_tag("Reputation", "Harsh")                 # latest read replaces prior
    reps = s.tags("Reputation")
    assert len(reps) == 1 and reps[0].key == "Harsh", reps


def test_multi_settlement_province_aggregation():
    world = create_world()                           # World now carries .settlements
    reg.reset_registry(world)
    for sid, order, prosp in [("S-004", 4, 3), ("S-005", 2, 2), ("S-006", 1, 1)]:
        reg.register_settlement(reg.Settlement(
            sid=sid, name=sid, stype="Town", province_id="Kronmark",
            order=order, prosperity=prosp, owner_faction="Crown"), world)
    prov = aggregate_to_province("Kronmark", world)
    assert prov.settlement_count == 3, prov.settlement_count
    assert prov.accord == 2, prov.accord             # floor((4+2+1)/3) = floor(2.33) = 2
    assert prov.effective_prosperity == 6, prov.effective_prosperity
    assert reg.province_accord("Kronmark", world) == 2


def test_registry_backed_derived_values():
    world = create_world()
    reg.reset_registry(world)
    reg.register_settlement(reg.Settlement(
        sid="S-006", name="Goldenfurt", stype="Town", province_id="Kronmark",
        prosperity=3, defense=1, order=2, fort_level=0, owner_faction="Crown"), world)
    st = compute_settlement_state("S-006", world)
    assert st.local_economy == 150, st.local_economy        # Prosperity 3 * 50
    assert st.garrison_strength == 20, st.garrison_strength  # Defense 1 * 20 + Fort 0 * 30
    assert st.public_order == 40, st.public_order            # Order 2 * 20
    assert st.settlement_type == "Town"


def test_backward_compat_fallback():
    world = create_world()
    reg.reset_registry(world)                        # empty registry → Territory fallback
    st = compute_settlement_state("T1", world)       # canonical territory must still resolve
    assert st.settlement_id == "T1"


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    for t in tests:
        t()
        print(f"PASS  {t.__name__}")
    print(f"\nALL {len(tests)} TESTS PASSED")
