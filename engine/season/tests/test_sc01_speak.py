"""v9 SC-01 step 12 -- `speak` (`workplans/valoria_master_workplan_v9_part6.md` §SC-01, the CARRIED
block's *Step 12*): a typed cell, `contests: "a matter"`, four bands. `_eff_speak` only if `writes:` is
non-empty -- and it is empty at every band (the row's `writes_note` and `H-63`'s step-12 clause say why),
so no effect exists and none is asserted.

WHAT IS BUILT, each asked of the real loader, the real fold and the real seam on a HAND-BUILT world
(`probes.tiny_world`: `p_high` holds `off_duke`; `p_low`, `p_mid` live in `Hh`):
  * THE CELL: `existence` of `subject`, kind `DocketItem` (`determine`'s `docket` conjunct, read through
    `world_q.docketed`). A `speak` on a matter no docket names is refused `speech.unheard` before any
    contest is drawn; the same act after an `open_case` dockets the matter reaches the seam.
  * THE PRIZE: `a matter`, an interim row routed to the `sigma_leverage` provider at step 12 and
    repointed to `social_contest` at steps 13 + 15 (`test_sc01_provider.py`), so a resolved `speak`
    carries a degree off `degree_from_net`.
  * THE FOUR BANDS: each band emits its own kind and only that kind (`emits_at`), the degree on the Event
    is the band, and all four occur over a sweep of act ids and speaker pools.

THE FALSIFIERS (each seen red before the row was built, 2026-10-16):
  * the row: the shape test reads the typed cell, the prize and four distinct band kinds.
  * the cell: a `speak` before the docket item is `speech.unheard` with no degree; after it, a degree.
    MUTATION (seen red): the cell's kind `DocketItem` -> `Person`, true of the party whether or not he
    is docketed -> the undocketed `speak` is drawn, not refused.
  * the bands: four kinds, one per band, the Event's degree equal to the band that selected it.
    MUTATION (seen red): `Overwhelming` emits `Success`'s kind -> `test_..._each_band_emits_its_own_kind`
    reds.
  * the loader: a speak row with a flat `writes:`, with a band in `writes:` missing from `emits:`, or
    contesting a prize no `contest_subsystems` row claims, each refuses at load naming the row.
No test here asserts execution in the seed-0 realm (v9 §0.5's relaxed exit).
"""

from __future__ import annotations

import pytest

from ..data import verbs as _verbs
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.requires import Existence
from ..data.rosters import roster_map
from ..data.verbs import VERB_TABLE
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.effects import EFFECTS
from ..manifest import resolve as manifest_resolve
from ..queries import world_q
from ..state.carriers import Act, Claim
from engine.dice_engine.dice_engine import DEGREE_LABEL

SEAT, DUKE = "off_duke", "p_high"
SPEAKER, PARTY = "p_low", "p_mid"
BANDS = frozenset(DEGREE_LABEL.values())


def _world(fx=DEFAULT_FIXTURES):
    w = P.tiny_world(fx)
    # `test_u7_remit.py::_world`'s: the Duke knows the party his bench would hear.
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


def _kinds(events):
    return [e.kind for e in events]


def _docket(w, d):
    """The matter goes before the room the one way an act puts it there: the Duke opens a case."""
    out = _fold(w, d, Act(id="oc", actor=DUKE, verb="open_case", via=SEAT,
                          payload={"subject": PARTY}))
    assert _kinds(out) == ["case.opened"], _kinds(out)
    assert len(world_q.docketed(w, PARTY)) == 1


def _speak(key, actor=SPEAKER, subject=PARTY):
    return Act(id=key, actor=actor, verb="speak", payload={"subject": subject})


# ================================================================================================
# THE ROW
# ================================================================================================

def test_sc01_s12_speak_is_a_typed_contested_cell_with_four_ladder_bands():
    row = VERB_TABLE["speak"]
    assert row.contests == "a matter", row.contests
    req = row.requires_typed.requirement
    assert isinstance(req, Existence) and req.of == "subject" and req.kind == world_q.DOCKET_KIND, req
    # The four bands are the ladder's own (`degree_from_net`'s labels), keyed alike on both columns.
    assert set(row.writes_by_degree) == set(row.emits_by_degree) == BANDS, (
        sorted(row.writes_by_degree), sorted(row.emits_by_degree))
    # Each band reports its own outcome: four bands, four distinct kinds, no kind shared.
    kinds = [tuple(row.emits_at(b)) for b in sorted(BANDS)]
    assert len(set(kinds)) == 4 and all(len(k) == 1 for k in kinds), kinds
    # `writes:` is empty at every band, so no effect is registered (the row's `writes_note`).
    assert row.writes == () and "speak" not in EFFECTS
    # A refusal is the cell's one kind; the party-gap refusal emits the same union.
    assert row.emits_on_refusal == ("speech.unheard",), row.emits_on_refusal
    # The prize routes to a registered provider, so the verb is resolvable. Interim at step 12; steps 13
    # + 15 repointed it to the container's provider (ED-SC-0033 clause (2); `test_sc01_provider.py`).
    prize = manifest_resolve("contest", "a matter")
    assert prize is not None and prize["provider"] == "social_contest", prize
    assert prize["module_entry"] == "social_contest.roll", prize
    assert "interim" not in roster_map("contest_subsystems", "prizes")["a matter"]
    assert "speak" in resolvable_verbs()


# ================================================================================================
# THE CELL: NO DOCKET, NO CONTEST
# ================================================================================================

def test_sc01_s12_a_speak_on_an_undocketed_matter_is_unheard_and_draws_no_contest():
    w, d = _world()
    out = _fold(w, d, _speak("sp0"))
    assert _kinds(out) == ["speech.unheard"], _kinds(out)
    assert all(e.degree is None for e in out), [(e.kind, e.degree) for e in out]
    # THE CONTROL, one clause away: the same act once the matter is docketed reaches the seam.
    _docket(w, d)
    out = _fold(w, d, _speak("sp1"))
    assert len(out) == 1 and out[0].degree in BANDS, [(e.kind, e.degree) for e in out]
    assert out[0].kind != "speech.unheard"


def test_sc01_s12_a_speak_writes_nothing_and_leaves_the_docket_as_it_was():
    """`writes:` is `[]` at every band: the speech is a deposit at WITNESS, not a state change, so the
    docket the bench will determine is exactly the one `open_case` wrote, whatever band the speech drew."""
    w, d = _world()
    _docket(w, d)
    before = [dict(i) for i in w.docket]
    checked = 0
    for i in range(12):
        out = _fold(w, d, _speak(f"spw{i}"))
        assert out and out[0].degree in BANDS
        assert not any(e.changes for e in out), [(e.kind, e.changes) for e in out]
        checked += 1
    assert checked == 12
    assert [dict(i) for i in w.docket] == before


# ================================================================================================
# THE FOUR BANDS
# ================================================================================================

def _bands_seen():
    """Every band a docketed `speak` resolves at, over act ids and the speaker's `copying` (the
    capability `rosters.yaml: verb_capability` maps `speak` to): `{band: {kinds emitted}}`."""
    seen: dict = {}
    folded = 0
    for pool in (1, 2, 4, 8):
        w, d = _world()
        w.persons[SPEAKER].capability = {"copying": pool}
        _docket(w, d)
        for i in range(24):
            out = _fold(w, d, _speak(f"spb{pool}_{i}"))
            assert len(out) == 1, _kinds(out)
            e = out[0]
            seen.setdefault(e.degree, set()).add(e.kind)
            folded += 1
    assert folded == 96, folded
    return seen


def test_sc01_s12_each_band_emits_its_own_kind_and_all_four_occur():
    row = VERB_TABLE["speak"]
    seen = _bands_seen()
    assert set(seen) == BANDS, sorted(seen, key=str)
    for band, kinds in seen.items():
        assert kinds == set(row.emits_at(band)), (band, sorted(kinds), row.emits_at(band))
    # Distinct: no kind is reported for two bands.
    assert len({k for ks in seen.values() for k in ks}) == 4, seen
    # The four pairs, literal: the row read back against itself cannot see a swapped pair.
    assert seen == {"Overwhelming": {"matter.carried"}, "Success": {"matter.advanced"},
                    "Partial": {"matter.held"}, "Failure": {"matter.turned"}}, seen


# ================================================================================================
# THE LOADER
# ================================================================================================

def _planted(monkeypatch, key, value):
    real = _verbs.load_yaml

    def planted(text):
        doc = real(text)
        if isinstance(doc, dict) and "verbs" in doc:
            for r in doc["verbs"]:
                if r.get("verb") == "speak":
                    r[key] = value
        return doc
    monkeypatch.setattr(_verbs, "load_yaml", planted)


@pytest.mark.parametrize("key,value,match", [
    ("writes", [], "declares `contests: a matter` and a FLAT `writes:`"),
    ("emits", {"Overwhelming": ["matter.carried"], "Success": ["matter.advanced"],
               "Failure": ["matter.turned"]}, "keys `writes` on"),
    ("contests", "a matterr", "which is not a `contest_subsystems.prizes` key"),
])
def test_sc01_s12_the_loader_refuses_a_malformed_speak_cell(monkeypatch, key, value, match):
    _planted(monkeypatch, key, value)
    with pytest.raises(SystemExit, match=match):
        _verbs._load_verb_table()


def test_sc01_s12_the_loader_control_the_shipped_row_loads():
    """The control for the three plants above: the unplanted table loads, with `speak` contested."""
    assert _verbs._load_verb_table()["speak"].contests == "a matter"


def test_sc01_s12_a_speaker_under_one_die_is_refused_not_a_crash():
    """S27.4 (Ob > 2 x Pool) is a refusal, not an abort: a docketed `speak` by a speaker whose
    `copying` pool is under 1D comes back as the verb's refusal kind, where it used to raise an
    uncaught `Unspecified` out of the season (found at B-N's `/code-review`). Control: pool 1 resolves."""
    checked = 0
    for pool, refused in ((0, True), (0.5, True), (1, False)):
        w, d = _world()
        w.persons[SPEAKER].capability = {"copying": pool}
        _docket(w, d)
        out = _fold(w, d, _speak(f"zpool{pool}"))
        assert bool(out) and (_kinds(out) == ["speech.unheard"]) is refused, (pool, _kinds(out))
        checked += 1
    assert checked == 3
