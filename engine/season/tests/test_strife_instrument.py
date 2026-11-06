"""`harness.strife` -- the side-aware classifier and the static route check.

What each block proves, and the control that stops it passing vacuously:

  1. THE REGISTRY LOADS 40 CODES AND REFUSES A BAD SIGNATURE. A signature naming an unknown verb, an
     undeclared kind, a code with no row, an unknown key or a bad attacker side is refused: each is
     planted in a temporary copy of the file and the load must raise (the loader is the only guard).
  2. DEATH IS TOLD BY ITS CAUSE. The same `person.died` kind classifies DN with no causing act and KL
     with a `fight` or a `march`. CONTROL: an unrelated verb classifies as neither.
  3. A FIELD IS TOLD BY WHO MARCHED. `field.won` is WA when the attacker is the authority and WR when
     it is a challenger, and the two codes SWAP for `field.lost`. FALSIFIER: swapping the side swaps
     the code, so a classifier that ignored side could not pass; and a side that cannot be told
     (`None`) yields no code, so nothing is guessed.
  4. `side_against`: the nearest governor and a governor above it are the authority; a faction in
     the chain nowhere is a challenger; no governor, or no attacker, is `None`.
  5. THE ROUTE CHECK IS REAL. `petition` reaches PT by a resolvable verb that emits a kind PT names;
     CH has no route (planted gap) and XE routes through `fight`; a verb that is not resolvable gives no
     route even when its row emits the kind. CONTROL: removing a verb from `resolvable` removes its route.
  6. OW AND XA ARE NOT DARK ON THE SHIPPED DEFAULT (`foreign` defaults True), DN still is; the residue
     counts an unmatched Event of a signature-named kind once and a matched one never; the loader's kind
     roster is `EVENT_KINDS`; the 24 terminal codes are found and those with no route are listed.

NOT COVERED, AND SAYING SO: the wiring from a real `World` (`readers_for`, `governors`) is exercised
only by the observed arm of the instrument (`python -m engine.season.harness.strife 4 0 1`), not here.
"""
from collections import Counter
from types import SimpleNamespace

import pytest

from engine.season.harness import strife as H
from engine.season.harness import strife_data as data
from engine.season.harness.strife_data import STRIFE_MOVES_YAML
from engine.season.queries import world_q as W


def ev(kind):
    return SimpleNamespace(kind=kind)


def readers(verb=None, side=None, held=False):
    return H.Readers(lambda e: verb, lambda e: side, lambda e: held)


def codes(e, rd):
    return sorted(c for c, _ in H.classify(e, rd))


def test_registry_loads_forty_codes_and_signatures():
    rows, sigs = data.load_moves()
    assert len(rows) == 40 and len({r["code"] for r in rows}) == 40
    assert len(sigs) >= 1


@pytest.mark.parametrize("bad", [
    "  - {kind: person.died, cause_verb: nonesuch, code: KL}",
    "  - {kind: nonesuch.kind, cause_verb: fight, code: KL}",
    "  - {kind: person.died, cause_verb: fight, code: ZZ}",
    "  - {kind: person.died, cause_verb: fight, code: KL, colour: red}",
    "  - {kind: field.won, attacker: Q, code: WA}",
])
def test_loader_refuses_a_bad_signature(tmp_path, bad):
    text = STRIFE_MOVES_YAML.read_text(encoding="utf-8").replace("signatures:\n", "signatures:\n" + bad + "\n", 1)
    p = tmp_path / "strife_moves.yaml"
    p.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        data.load_moves(p)


def test_a_death_is_told_by_its_cause():
    assert codes(ev("person.died"), readers(verb=None)) == ["DN"]
    assert codes(ev("person.died"), readers(verb="fight")) == ["KL"]
    assert codes(ev("person.died"), readers(verb="fight", held=True)) == ["XE"]   # a held person killed by a fight is executed
    assert codes(ev("person.died"), readers(verb=None, held=True)) == ["DN"]       # held, but no act of anyone: died, not executed
    assert codes(ev("person.died"), readers(verb="march")) == ["KL"]
    assert codes(ev("person.died"), readers(verb="tell")) == []      # control: another verb is neither


def test_a_field_is_told_by_who_marched_and_the_codes_swap_on_a_loss():
    assert codes(ev("field.won"), readers(side="A")) == ["WA"]
    assert codes(ev("field.won"), readers(side="R")) == ["WR"]
    assert codes(ev("field.lost"), readers(side="A")) == ["WR"]
    assert codes(ev("field.lost"), readers(side="R")) == ["WA"]
    assert codes(ev("field.won"), readers(side=None)) == []           # a side that cannot be told is not guessed
    assert codes(ev("march.declared"), readers(side="A")) == ["FR"]
    assert codes(ev("march.declared"), readers(side="R")) == ["WN"]
    assert codes(ev("march.declared"), readers(side="O")) == ["OW"]             # an invasion by a foreign nation


def test_an_event_matching_no_signature_is_left_alone():
    assert H.classify(ev("petition.filed"), readers(verb="petition", side="A")) == []


def test_side_against_the_governors():
    assert W.side_against("f_crown", ["f_crown", "f_realm"]) == "A"   # the nearest governor
    assert W.side_against("f_realm", ["f_crown", "f_realm"]) == "A"   # a governor above it, sending force down
    assert W.side_against("f_rebel", ["f_crown", "f_realm"]) == "R"
    assert W.side_against("f_rebel", []) is None                       # nobody governs: no authority to compare
    assert W.side_against(None, ["f_crown"]) is None
    assert W.side_against("f_altonia", ["f_crown"], {"f_altonia"}) == "O"       # a foreign faction is an outside power
    assert W.side_against("f_altonia", [], {"f_altonia"}) == "O"                 # whether or not anything governs the rung
    assert W.side_against("f_rebel", ["f_crown"], {"f_altonia"}) == "R"          # control: a non-foreign challenger stays R


def test_the_route_check_finds_a_route_and_a_planted_gap():
    rows = {r["code"]: r for r in data.MOVES}
    assert [v for v, _ in H.route(rows["PT"])] and "petition" in [v for v, _ in H.route(rows["PT"])]
    assert H.route(rows["CH"]) == []                                    # no verb and no kind: a gap
    assert "fight" in [v for v, _ in H.route(rows["XE"])]               # XE composes on `fight`; formation on a held party is open
    only = {"carry"}                                                    # CONTROL: drop `petition` from the resolvable set
    assert "petition" not in [v for v, _ in H.route(rows["PT"], resolvable=only)]
    assert "carry" in [v for v, _ in H.route(rows["PT"], resolvable=only)]


def test_grade_cases():
    from collections import Counter
    rows = {r["code"]: r for r in data.MOVES}
    act = Counter({("KL", None): 3})
    assert H.grade(rows["KL"], Counter(), act, True) == ("OBSERVED", 3)
    sig_codes = {g["code"] for g in data.SIGNATURES}
    # DN carries a `dark` cell AND a signature. `measure()` passes `has_sig=True` for it, and `grade` returns before reading `dark`, so the
    # instrument grades it UNOBSERVED, never DARK: `dark` counts only on a row with no signature. Grade it the way `measure()` does.
    assert "DN" in sig_codes and rows["DN"].get("dark")
    assert H.grade(rows["DN"], Counter({"person.died": 99}), Counter(), "DN" in sig_codes) == ("UNOBSERVED", 0)
    # The DARK path itself, on a row with no signature: plant a `dark` cell on XA in a copy of the file.
    assert "XA" not in sig_codes
    xa = dict(rows["XA"], dark="a switch that ships off")
    assert H.grade(xa, Counter({"march.declared": 99}), Counter(), "XA" in sig_codes)[0] == "DARK"
    assert H.grade(rows["CH"], Counter(), Counter(), "CH" in sig_codes)[0] == "GAP"
    assert H.grade(rows["PT"], Counter({"petition.filed": 2}), Counter(), False) == ("OBSERVED", 2)


def test_endings_total_the_study_and_yield_24_terminal_codes():
    rows = data.MOVES
    assert sum(r.get("ends", 0) for r in rows) == 102
    terminal = {r["code"] for r in rows if r.get("ends", 0) > 0 and r.get("terminal", True)}
    assert len(terminal) == 24 and "XP" not in terminal and {"PC", "CO", "WA", "XE"} <= terminal
    assert all(r.get("ends", 0) == 0 for r in rows if r["code"] in {"SH", "DR", "BR", "MO", "OP", "RU", "VI", "SZ"})


def test_loader_refuses_ends_that_do_not_total_102(tmp_path):
    text = STRIFE_MOVES_YAML.read_text(encoding="utf-8").replace("ends: 20", "ends: 21", 1)
    p = tmp_path / "strife_moves.yaml"
    p.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        data.load_moves(p)


def test_the_side_read_by_default_reads_altonia_and_schoenland_as_outside_powers():
    from engine.season.data.rosters import faction_prop_id
    for name in ("Altonia", "Schoenland"):
        assert W.side_against(faction_prop_id(name), ["f_crown"]) == "O", name
    assert W.side_against(faction_prop_id("Valorsmark"), ["f_crown"]) == "R"     # control: a realm faction is not


def _load_with(tmp_path, old, new):
    text = STRIFE_MOVES_YAML.read_text(encoding="utf-8")
    assert text.count(old) == 1, old
    p = tmp_path / "strife_moves.yaml"
    p.write_text(text.replace(old, new), encoding="utf-8")
    return data.load_moves(p)


def test_ow_and_xa_are_not_dark_on_the_shipped_default(tmp_path):
    rows = {r["code"]: r for r in data.MOVES}
    seen = Counter({"march.declared": 7, "news.told": 2})
    assert "dark" not in rows["OW"] and "dark" not in rows["XA"]
    assert H.grade(rows["XA"], seen, Counter(), False) == ("KIND-ONLY", 9)       # an upper bound, not DARK
    assert H.grade(rows["OW"], seen, Counter({("OW", "O"): 4}), True) == ("OBSERVED", 4)
    # FALSIFIER: put the cell back in a copy of the file and the same grade reads DARK.
    cell = 'needs: [side], ends: 1}\n  - {code: AM'
    rows2 = {r["code"]: r for r in _load_with(tmp_path, cell, 'needs: [side], dark: "x", ends: 1}\n  - {code: AM')[0]}
    assert H.grade(rows2["XA"], seen, Counter(), False) == ("DARK", 0)
    # CONTROL: DN still ships dark (ageing is 0.0) and CH is still a GAP.
    assert H.grade(rows["DN"], Counter(), Counter(), False)[0] == "DARK"
    assert H.grade(rows["CH"], seen, Counter(), False)[0] == "GAP"


def test_residue_counts_an_unmatched_event_and_not_a_matched_one():
    seen, act, res = Counter(), Counter(), Counter()
    tell_death, fight_death, petition = ev("person.died"), ev("person.died"), ev("petition.filed")
    H.count_event(tell_death, readers(verb="tell"), seen, act, res)
    H.count_event(fight_death, readers(verb="fight"), seen, act, res)    # matches KL
    H.count_event(petition, readers(verb="petition", side="A"), seen, act, res)
    assert res == Counter({("person.died", "tell", None): 1})
    assert act == Counter({("KL", None): 1})
    assert seen == Counter({"person.died": 2, "petition.filed": 1})
    # `petition.filed` is a kind no signature names: in neither tally.
    assert not any(k[0] == "petition.filed" for k in res) and not any(c == "PT" for c, _ in act)
    seen2, act2, res2 = Counter(), Counter(), Counter()
    H.count_event(tell_death, readers(verb="tell"), seen2, act2, res2)
    assert res2[("person.died", "tell", None)] == 1 and not act2
    # a march that cannot be sided is residue with its cause verb; a sided one is not
    H.count_event(ev("march.declared"), readers(verb="march", side=None), seen2, act2, res2)
    H.count_event(ev("march.declared"), readers(verb="march", side="O"), seen2, act2, res2)
    assert res2[("march.declared", "march", None)] == 1 and act2[("OW", "O")] == 1
    assert sum(res2.values()) == 2 and sum(act2.values()) == 1


def test_a_signature_kind_is_matched_or_residue_never_both():
    kinds = {g["kind"] for g in data.SIGNATURES}
    assert kinds >= {"person.died", "field.won", "field.lost", "march.declared"}
    # The verbs and sides are READ FROM THE SIGNATURES (plus one verb no signature names, as a control), so a signature added later is swept.
    verbs = {None if g.get("cause_verb") in (None, "none") else g["cause_verb"] for g in data.SIGNATURES} | {None, "tell"}
    sides = (None, *sorted({g["attacker"] for g in data.SIGNATURES if "attacker" in g}))
    assert {"accept", "fight", "march"} <= verbs and {"A", "R", "O"} <= set(sides)
    checked = 0
    for kind in sorted(kinds):
        for verb in sorted(verbs, key=str):
            for side in sides:
                for held in (False, True):
                    rd = readers(verb=verb, side=side, held=held)
                    hits = H.classify(ev(kind), rd)
                    seen, act, res = Counter(), Counter(), Counter()
                    H.count_event(ev(kind), rd, seen, act, res)
                    assert len(hits) <= 1, (kind, verb, side, held, hits)      # mutually exclusive
                    assert sum(act.values()) + sum(res.values()) == 1          # exactly one tally
                    assert (sum(act.values()) == 1) == bool(hits)
                    checked += 1
    assert checked >= len(kinds) * len(verbs) * len(sides) * 2


def test_declared_kinds_is_the_one_roster(tmp_path):
    from engine.season.data.verbs import EVENT_KINDS
    assert data.declared_kinds() == EVENT_KINDS
    assert "nonesuch.kind" not in EVENT_KINDS
    # every kind the shipped registry names is in the one roster, so the shipped file loads
    rows, sigs = data.load_moves()
    named = {k for r in rows for k in r["kinds"]} | {g["kind"] for g in sigs}
    assert named and named <= EVENT_KINDS
    # the loader refuses a kind absent from it, in a row and in a signature
    with pytest.raises(ValueError):
        _load_with(tmp_path, "kinds: [petition.filed, petition.carried]", "kinds: [petition.filed, nonesuch.kind]")
    with pytest.raises(ValueError):
        _load_with(tmp_path, "signatures:\n", "signatures:\n  - {kind: nonesuch.kind, code: KL}\n")


def test_terminal_codes_and_routeless_terminals():
    rows = data.MOVES
    term = H.terminal_codes(rows)
    assert len(term) == 24 and "XP" not in term and {"PT", "KL", "XE"} <= term
    assert all(r.get("ends", 0) > 0 for r in rows if r["code"] in term)
    only_petition = H.routeless_terminals(rows, resolvable={"petition"})
    assert set(only_petition) == term - {"PT"}                                  # all but PT lose their route
    full = H.routeless_terminals(rows)
    assert len(full) < len(only_petition)                                       # CONTROL: the full set routes more
    assert set(full) <= term and "PT" not in full
    assert full == ["DN"]                                                       # DN has no verb by design; every other terminal code has a route


def test_a_death_in_an_accepted_duel_is_killed_and_a_foreign_field_is_outside_war():
    """The S1r residue named both: five deaths per seed were caused by `accept` (a duel accepted; its Felled band emits `person.died`),
    and a foreign marcher's `field.won` / `field.lost` matched nothing. FALSIFIERS: a held person felled by `accept` is NOT classified
    (it stays residue: execution is a fight on a held party, not a duel); a challenger's `field.lost` is still WA, not OW."""
    assert codes(ev("person.died"), readers(verb="accept")) == ["KL"]
    assert codes(ev("person.died"), readers(verb="accept", held=True)) == []
    assert codes(ev("field.won"), readers(side="O")) == ["OW"]
    assert codes(ev("field.lost"), readers(side="O")) == ["OW"]
    assert codes(ev("field.lost"), readers(side="R")) == ["WA"]
