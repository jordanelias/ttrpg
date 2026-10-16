"""v9 SC-01 steps 13 + 15, ONE change (`workplans/valoria_master_workplan_v9_part6.md` §SC-01, the
CARRIED block's *Step 13* and *Step 15*): the social contest container's contest provider, and the
three social prize rows repointed to it.

WHAT IS BUILT, each asked of the real manifest, the real registrar, the real fold and the real seam:
  * THE REPOINT (step 13, ED-SC-0033 clause (2)): `a standing`, `a proposition` and `a matter` drop
    `interim: true` and name `provider: social_contest` -- a ROW change. Three rows, not the plan's two:
    step 12 added `a matter` (`speak`'s prize) as an interim row.
  * THE PROVIDER (step 15): `@provider("contest", "social_contest")`, the host adapter in
    `seam/wrappers/sigma.py`, reached by the prize rows' STRING; it calls the module entry the rows name
    (`module_entry: social_contest.roll`, registered by `30`'s registrar at driver construction, never
    imported by the host) and holds the entry to a `Margin` at the boundary -- a margin, never a winner
    (`08_SEAM.md`'s provider rule, intent only). The automated mode stays the σ-leverage roll: SC-05's
    measurement, recorded in `modules/social_contest/roll.py`'s docstring, keeps it over the kernel.
  * THE RUNG (C-8): a contested act on a non-`mass_battle` prize dispatches at the actor's place
    (`world_q.place_of`), where it dispatched at the placeholder `"R"`.

THE FALSIFIERS (each run red before the build, 2026-10-16, base `29af7354`):
  * the rows name the container's provider and none is interim -- RED at base (`sigma_leverage`, interim).
  * the provider is registered by importing the seam and the driver constructs -- RED at base.
  * THE HALF-STATE: the rows repointed with no provider registered refuse at driver construction naming
    the first such prize (`30`'s refusal (c)); a misspelled `provider:` and a deleted composition row
    each refuse naming the row. This is why 13 and 15 are one change.
  * the entry returns a `Margin`; an entry returning the kernel's winner shape, or a dict carrying a
    winner, is refused at the host boundary naming the entry -- RED at base (no `Margin` type).
  * a hand-built `speak` and `tell` resolve end to end through the new provider, the Event's degree the
    one ladder's reading of the provider's own pair -- RED at base (no `social_contest` provider).
  * C-8: a contested `speak` by the Duke dispatches at his settlement `S`, the copyist's at the hearth
    `Hh` -- RED at base (both `"R"`).
  * SCRIPTING DRIFT: the arrangement-id scan first written here MOVED at step 16, which owns the
    closure test (`tests/test_sc01_the_bar.py`, its one home).
No test here asserts execution in the seed-0 realm (v9 §0.5's relaxed exit).
"""

from __future__ import annotations

import random

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.rosters import roster_map
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..manifest import MODULE_ENTRIES, PROVIDERS
from ..manifest.registrar import ModuleEntry
from ..queries import world_q
from ..queries.inputs import Margin, SocialContestInput
from ..queries.person_q import said_of
from ..seam import ladder
from ..seam.wrappers import sigma
from ..state.carriers import Act, Claim
from engine.substrate import composition

PROVIDER = "social_contest"
ENTRY = "social_contest.roll"
SOCIAL_PRIZES = ("a matter", "a proposition", "a standing")
SEAT, DUKE = "off_duke", "p_high"
SPEAKER, PARTY = "p_low", "p_mid"


def _social_rows() -> dict:
    return {k: r for k, r in roster_map("contest_subsystems", "prizes").items()
            if isinstance(r, dict) and r.get("module") == "social_contest"}


def _world(fx=DEFAULT_FIXTURES):
    w = P.tiny_world(fx)
    w.persons[DUKE].ledger.append(Claim("c_knows_party", DUKE, PARTY, "exists:Person", 1, 0,
                                        "firsthand", 100, "own"))
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _docket(w, d):
    out = _fold(w, d, Act(id="oc", actor=DUKE, verb="open_case", via=SEAT, payload={"subject": PARTY}))
    assert [e.kind for e in out] == ["case.opened"], [e.kind for e in out]


def _recording(monkeypatch) -> list:
    """Wrap the registered provider so each call's verb, rung and return is seen. The wrapper calls the
    real provider, so what is folded is what the provider returned."""
    real = PROVIDERS[("contest", PROVIDER)]
    calls: list = []

    def rec(w, claimants, causes, prize, **kw):
        out = real(w, claimants, causes, prize, **kw)
        calls.append(dict(verb=kw.get("verb"), rung=kw.get("rung"), prize=prize, out=out))
        return out
    monkeypatch.setitem(PROVIDERS, ("contest", PROVIDER), rec)
    return calls


def _grade(out: dict) -> str:
    degree_from_net, label = ladder.degree_ladder()
    return label[degree_from_net(out["net"], out["ob"])]


# ================================================================================================
# STEP 13: THE ROWS
# ================================================================================================

def test_sc01_s13_the_social_prize_rows_name_the_container_provider_and_none_is_interim():
    rows = _social_rows()
    assert tuple(sorted(rows)) == SOCIAL_PRIZES, sorted(rows)
    for prize, row in sorted(rows.items()):
        assert row["provider"] == PROVIDER, (prize, row["provider"])
        assert "interim" not in row, (prize, "still interim: ED-SC-0033 clause (2)'s repoint not made")
        assert row["module_entry"] == ENTRY, (prize, row.get("module_entry"))


# ================================================================================================
# STEP 15: THE PROVIDER, REGISTERED; AND THE HALF-STATE THAT SPLITTING 13 FROM 15 WOULD SHIP
# ================================================================================================

def test_sc01_s15_the_provider_is_registered_and_the_driver_constructs_on_the_shipped_rows():
    assert ("contest", PROVIDER) in PROVIDERS, sorted(PROVIDERS)
    # No provider stays registered that no row names: the interim one went with the repoint.
    assert ("contest", "sigma_leverage") not in PROVIDERS, sorted(PROVIDERS)
    SeasonDriver(P.tiny_world())
    assert ENTRY in MODULE_ENTRIES, sorted(MODULE_ENTRIES)


def test_sc01_s13_s15_the_rows_repointed_without_their_provider_refuse_at_driver_construction(monkeypatch):
    """THE HALF-STATE: step 13 landed and step 15 not. Every social row names `social_contest` and
    nothing registered it -> `30`'s refusal (c), naming the first such prize in roster order."""
    for row in _social_rows().values():
        monkeypatch.setitem(row, "provider", PROVIDER)
    monkeypatch.delitem(PROVIDERS, ("contest", PROVIDER), raising=False)
    with pytest.raises(Unspecified, match=r"prize 'a standing' names provider 'social_contest', "
                                          r"which nobody registered"):
        SeasonDriver(P.tiny_world())


def test_sc01_s15_a_misspelled_provider_row_refuses_at_driver_construction_naming_the_row(monkeypatch):
    monkeypatch.setitem(_social_rows()["a matter"], "provider", "social_contst")
    with pytest.raises(Unspecified, match=r"prize 'a matter' names provider 'social_contst'"):
        SeasonDriver(P.tiny_world())


def test_sc01_s15_a_deleted_composition_row_refuses_at_driver_construction_naming_the_row(monkeypatch):
    SeasonDriver(P.tiny_world())                       # the control: the shipped rows construct
    monkeypatch.delitem(composition.ROLES, ENTRY)
    with pytest.raises(Unspecified, match=ENTRY.replace(".", r"\.")):
        SeasonDriver(P.tiny_world())


# ================================================================================================
# LENS B: A MARGIN, NEVER A WINNER
# ================================================================================================

def _record(**kw) -> SocialContestInput:
    base = dict(pool=4, opposition=None, obstacle_default=2.0, obstacle_ceiling=2.0,
                obstacle_refusal_multiple=2.0, leverage=0.0)
    base.update(kw)
    return SocialContestInput(**base)


def test_sc01_s15_the_entry_returns_a_margin_and_nothing_that_names_a_winner():
    SeasonDriver(P.tiny_world())                       # the registrar fills MODULE_ENTRIES
    got = MODULE_ENTRIES[ENTRY].fn(_record(), random.Random(7))
    assert isinstance(got, Margin), type(got)
    assert set(Margin.__dataclass_fields__) == {"net", "ob"}, sorted(Margin.__dataclass_fields__)


@pytest.mark.parametrize("winner", [
    (("a", "win"), None),                              # the kernel's own return, `((band, reason), bout)`
    dict(status="RESOLVED", winner="p_low", net=3.0, ob=2.0),
])
def test_sc01_s15_an_entry_returning_a_winner_is_refused_at_the_host_boundary(monkeypatch, winner):
    w, _d = _world()
    real = MODULE_ENTRIES[ENTRY]
    # THE CONTROL: the shipped entry passes the same boundary, on the same world and act.
    ok = sigma.resolve(w, [SPEAKER, PARTY], ["c"], "a standing", verb="tell", subject=PARTY,
                       rng=random.Random(3))
    assert ok["status"] == "RESOLVED" and ok["module"] == PROVIDER, ok
    monkeypatch.setitem(MODULE_ENTRIES, ENTRY,
                        ModuleEntry(real.role, real.entry, real.verb, real.target, lambda inp, rng: winner))
    with pytest.raises(Unspecified, match=r"social_contest\.roll.*not a `Margin`"):
        sigma.resolve(w, [SPEAKER, PARTY], ["c"], "a standing", verb="tell", subject=PARTY,
                      rng=random.Random(3))


# ================================================================================================
# END TO END: A HAND-BUILT `speak` AND `tell` THROUGH THE NEW PROVIDER, AND C-8's RUNG
# ================================================================================================

def test_sc01_s15_a_docketed_speak_resolves_through_the_provider_at_the_speakers_place(monkeypatch):
    w, d = _world()
    _docket(w, d)
    calls = _recording(monkeypatch)
    folded = 0
    for actor, place in ((SPEAKER, "Hh"), (DUKE, "S")):
        assert world_q.place_of(w, actor) == place, (actor, world_q.place_of(w, actor))
        out = _fold(w, d, Act(id=f"sp_{actor}", actor=actor, verb="speak", payload={"subject": PARTY}))
        assert len(out) == 1, [(e.kind, e.degree) for e in out]
        call = calls[-1]
        assert call["verb"] == "speak" and call["prize"] == "a matter", call
        # C-8: the seam dispatched at the actor's place, never the `"R"` placeholder.
        assert call["rung"] == place, (actor, call["rung"])
        assert call["out"]["status"] == "RESOLVED" and call["out"]["module"] == PROVIDER, call["out"]
        assert out[0].degree == _grade(call["out"]), (out[0].degree, call["out"])
        folded += 1
    assert folded == 2 and len(calls) == 2


def test_sc01_s15_a_tell_resolves_through_the_provider(monkeypatch):
    w, d = _world()
    calls = _recording(monkeypatch)
    w.persons[SPEAKER].ledger.append(
        Claim("c_s15", SPEAKER, "Hh", "stores:grain", 8, 0, "firsthand", 37, "own"))
    tell = Act(id="s15_tell", actor=SPEAKER, verb="tell",
               payload={"subject": "Hh", "to": PARTY,
                        "said": said_of(w.persons[SPEAKER].ledger, "Hh", w.fixtures)})
    out = _fold(w, d, tell)
    assert len(calls) == 1, calls
    call = calls[0]
    assert call["verb"] == "tell" and call["prize"] == "a standing" and call["rung"] == "Hh", call
    assert call["out"]["module"] == PROVIDER, call["out"]
    graded = [e for e in out if e.degree is not None]
    assert graded and all(e.degree == _grade(call["out"]) for e in graded), (
        [(e.kind, e.degree) for e in out], call["out"])
