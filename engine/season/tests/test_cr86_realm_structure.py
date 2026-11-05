"""CR-86 (ED-IN-0342) -- the realm's structure: Valorsmark a faction, the vassals sworn, the heads seated.

Each block names the falsifier that would have shown the claim wrong, and its control:

  1. `faction_q.head` of Valorsmark is the King -- and of Hafenmark / Varfell / the Church their seat-holders.
     Control: a faction with no `head_seat` (the Guilds) is still `None`; vacate the King's seat and the head goes.
  2. Valorsmark is ONE faction and "Crown" is its alias: every `faction: Crown` membership (a cast cell, an office
     overlay) resolves to it; `Crown` is not a roster member.
  3. The two vassals' `oblige` edges are in the built realm and are READ by `purview_reaches`. In the as-built realm
     the realm rung already contains every duchy, so the King's ground reaches a Varfell territory with or without the
     edge (asserted below as the control that says so); the planted detachment cuts `duchy_varfell` out of the
     realm, and only then does the Duke's edge decide: reached WITH it, not WITHOUT it.
  4. The Church's territory has its dwelling already (no row added).
"""
import pytest

from engine.season.data import cast
from engine.season.gaps import Forbidden
from engine.season.data.rosters import FACTION_BY_PROP, FACTIONS, HEAD_SEAT, office_faction
from engine.season.harness.populated import build_realm
from engine.season.queries import faction_q
from engine.season.state.gate import _ground_reaches, purview_reaches

VALORSMARK = "fac_valorsmark"


def _king(w):
    return next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == "off_king")


def test_head_of_valorsmark_is_the_king_and_the_other_seated_heads_are_their_seat_holders():
    w = build_realm(0)
    assert faction_q.head(w, VALORSMARK) == _king(w) == "p_npc_020"
    assert faction_q.resolve(w, VALORSMARK).head == "p_npc_020"
    assert faction_q.head(w, "fac_hafenmark") == "p_npc_050"
    assert faction_q.head(w, "fac_varfell") == "p_npc_052"
    assert faction_q.head(w, "fac_church_of_solmund") == "p_npc_021"
    assert len(HEAD_SEAT) == 4 and set(HEAD_SEAT) <= set(FACTIONS)


def test_head_controls_a_faction_without_a_head_seat_is_none_and_a_vacant_seat_has_no_head():
    w = build_realm(0)
    assert "Guilds" not in HEAD_SEAT and faction_q.head(w, "fac_guilds") is None
    for t in w.tenures:                      # planted: the King's seat is vacated
        if t.kind == "hold" and t.object == "off_king":
            t.until = 0
    assert faction_q.head(w, VALORSMARK) is None


def test_crown_is_valorsmarks_alias_and_every_crown_membership_resolves_to_it():
    assert "Valorsmark" in FACTIONS and "Crown" not in FACTIONS
    assert FACTION_BY_PROP[VALORSMARK] == "Valorsmark"
    assert cast.resolve_faction("Crown") == "Valorsmark"
    assert office_faction(None, "Crown") == "Valorsmark"            # a case overlay's `faction: Crown`
    # the Phase 1 close: an authored alias also agrees with a `body:`'s derived faction (legal before CR-86)
    assert office_faction("Imperial Court", "Crown") == "Valorsmark"
    with pytest.raises(Forbidden):
        office_faction("Imperial Court", "Church")                    # a real disagreement still refuses
    w = build_realm(0)
    crown_rows = [r for r in cast.load().values() if str(r.get("faction") or "").startswith("Crown")]
    assert len(crown_rows) >= 5, "the registry's Crown rows are what the alias must carry"
    for r in crown_rows:
        assert cast.faction_of(r)[0] == "Valorsmark"
    assert cast.faction_leader("Valorsmark") == "NPC-020"
    assert not any(o.faction == "Crown" for o in w.offices.values())
    assert sum(1 for o in w.offices.values() if o.faction == "Valorsmark") >= 8


def test_the_two_vassals_are_sworn_to_the_king_by_oblige_and_no_duke_lost_land():
    w = build_realm(0)
    sworn = {t.subject for t in w.tenures if t.kind == "oblige" and t.object == "off_king" and t.live}
    assert {"p_npc_050", "p_npc_052", "p_npc_070"} <= sworn          # the Duchess, the Duke, the Grand Master
    held = {d: [t.subject for t in w.tenures if t.kind == "contain" and t.object == d and t.live]
            for d in ("duchy_valorsmark", "duchy_hafenmark", "duchy_varfell")}
    assert "terr_T12" in held["duchy_varfell"] and "terr_T8" in held["duchy_hafenmark"]
    assert held["duchy_valorsmark"], "the King's own duchy holds its territories (the geography's `Crown` rows)"


def test_the_dukes_oblige_edge_is_what_reaches_a_varfell_territory_once_the_duchy_is_outside_the_realm():
    # CONTROL: in the as-built realm the King reaches the Varfell territory by containment alone.
    w = build_realm(0)
    king = w.offices["off_king"]
    assert _ground_reaches(w, king, "terr_T12") and purview_reaches(w, king, "terr_T12")

    def detached(drop_edge: bool):
        w = build_realm(0)
        for t in w.tenures:
            if t.kind == "contain" and t.subject == "duchy_varfell":
                t.until = 0                                       # the duchy leaves the realm
            if drop_edge and t.kind == "oblige" and t.object == "off_king" and t.subject == "p_npc_052":
                t.until = 0                                       # planted removal of the Duke's oath
        return w, w.offices["off_king"]

    w, king = detached(drop_edge=False)
    assert not _ground_reaches(w, king, "terr_T12"), "the planted detachment must remove the containment route"
    assert purview_reaches(w, king, "terr_T12")                   # the Duke's oblige edge brings his ground
    w, king = detached(drop_edge=True)
    assert not purview_reaches(w, king, "terr_T12")               # without the edge: not reached
    # per-vassal control: with the Duke's edge dropped, the Duchess's edge does not bring Varfell's ground
    assert any(t.kind == "oblige" and t.live and t.subject == "p_npc_050" and t.object == "off_king" for t in w.tenures)


def test_the_church_territory_already_has_its_dwelling():
    w = build_realm(0)
    assert any(t.kind == "contain" and t.subject == "set_s_036" and t.object == "terr_T9" for t in w.tenures)
    assert any(t.kind == "hold" and t.live and t.subject == "p_npc_021" and t.object == "terr_T9"
               for t in w.tenures)
