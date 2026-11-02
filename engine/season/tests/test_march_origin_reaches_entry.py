"""MB-05r THROUGH THE DRIVER PATH: a real `march` act, folded RESOLVE -> ENCOUNTER by the real
`SeasonDriver`, hands the mass-battle module entry a record whose `origin` is the attacker's own
territory. `test_mass_battle_provider.py`'s MB-05r block calls the provider directly with a hand-picked
`claimants` list and `subject`; here `loop/sides.py::sides_of` builds both from the act (`a.actor`'s home
settlement, `a.via`'s faction, the target's HOLDER faction) and the provider derives the origin.

That block's own pair (Crown at `set_s_004` on Varfell at `set_s_008`) is not reachable this way:
`set_s_008`'s holder is the Crown, so a Crown march there musters no defender and folds `Unopposed`.
The reverse march is: `p_npc_082` (Varfell, `set_s_008`, T3, east of the Valoris) on the bare
`set_s_004` (T2, Crown-held, one Crown man). The record is captured at `field_input`, the value
`resolve` passes to `entry.fn` unchanged, so what is asserted is what the module received. The entry
itself is not patched: `register_module_entries` refuses a table entry its composition row disagrees
with, and folding constructs a driver.

THE FALSIFIER: `field_input`'s `origin` forced to `None` (the pre-MB-05r host) reds the `origin`
assertion."""

from engine.season.data.matrix import Step, WriteClass
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q
from engine.season.seam.wrappers import mass_battle as wrapper
from engine.season.state.carriers import Act


def test_a_folded_march_across_the_river_hands_the_entry_its_origin(monkeypatch):
    target = "set_s_004"
    w = build_realm(0)
    for sid in [sid for sid, s in w.sites.items() if s.kind == "garrison" and s.rung == target]:
        del w.sites[sid]
    assert world_q.fortification_of(w, target) == 0.0, "deleting the garrison left a fortification"
    assert world_q.holder_faction_of(w, target) == "fac_crown", "set_s_004 is no longer Crown-held"
    assert world_q.mustered(w, target, "fac_crown"), "set_s_004 no longer musters a Crown defender"
    assert world_q.mustered(w, "set_s_008", "fac_varfell") == ["p_npc_082"], "the T3 Varfell muster moved"

    records = []
    real = wrapper.field_input
    monkeypatch.setattr(wrapper, "field_input",
                        lambda *a, **k: records.append(real(*a, **k)) or records[-1])

    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    act = Act(id="m1", actor="p_npc_082", verb="march", payload={"subject": target}, via="off_military_jarl")
    events = d.resolve(mint_token(w, WriteClass.ACTS), [act], 2)
    events = events + d.encounter(mint_token(w, WriteClass.ACTS), events, 2)

    kinds = [e.kind for e in events]
    assert "march.declared" in kinds and any(k.startswith("field.") for k in kinds), kinds
    assert "field.unopposed" not in kinds, f"the march was not fought: {kinds}"
    assert len(records) == 1, f"the entry was called {len(records)} times, not once"
    rec = records[0]
    assert rec.territory == "T2" and rec.fort_level == 0.0, f"not the bare T2 field: {rec}"
    assert rec.origin == "T3", f"the folded march did not hand the entry its origin: {rec.origin!r}"
