"""v9 FA-01, THE MECHANISM HALF (batch B-J): A FACTION'S HEAD IS SEATED, AND THE HEAD'S ACT EXECUTES `via` THAT SEAT.

`Faction` has no verbs (A-4): a faction's act is a person's act through a seat. So "seat each faction's
head" is two observable facts on the built realm, and this file asks each of the real build, the real
decision machinery and the real fold:

  1. THE SEATING. Every faction whose head is authored in the cast (`data/cast.py::faction_leader`, the
     one owner of "who heads this faction", read by `harness/populated.py` for the creed and for
     provincial holdings) has that person holding a live `hold` on an office OF THE SAME FACTION at
     `build_realm(0)`. The factions with no authored head are pinned by name: they are the content half
     (B-V, IN-36), not a gap this file fills.
  2. THE EXIT AND ITS FALSIFIER. Each seated head's COMPUTED act through its own-faction seat
     (`questions_for` -> `opening_set` -> `pack_scenes`, no act hand-built) is folded on the built realm
     and executes, attributed by `harness/corpus_run.py::attribute` (the one owner of "executed", which
     `harness/aperture.py` also reads). Then, on a second build of the same seed with the head's seat
     closed, THE SAME ACT refuses.

⚠ MEASURED BEFORE ANY EDIT, 2026-10-14, on `40926a95` (the IN-48 build, since reverted: its opening-set decline never fired in the realm and the build hash is unchanged after the revert, so the reading holds on `e00d5b3c`) (build hash `11989dcf5e1c25afab556bf3f234a200`): the
plan's measure of "seated" was `grep -E '^    faction:' engine/season/offices.yaml` (Crown 8, Church 1,
Hafenmark 1, Restoration 1, Varfell 1, null 17). That column is read ONLY for a MINTED row
(`offices.yaml`'s header, "only a MINTED seat carries this file's `id`, `post`, `body` and `faction`"); a
loop-built seat derives its faction from the cast (`populated.py`, `office_faction` over the body). At
build every one of the six authored heads already holds a seat of its own faction, and five of the six
execute an act `via` it at the first fold. So the mechanism needed no data edit; this file is its record
and its falsifier. The sixth, the Restoration Movement's head (minted `off_restoration_leader`, remit
`[issue]`, rung T15), is SEATED and its computed acts through the seat refuse on purview at tick 0
(`issue.unauthorized`: the seat's purview does not reach the executor) -- a fact about that seat's ground
and remit, not about seating, and not widened here (`offices.yaml`'s J-8 note: remit is a grant decision).

Cost: three `build_realm(0)` and a handful of folds; seconds, against `aperture 4 0`'s ~20 minutes for the
same observation (CLAUDE.md §0.4: the cheapest instrument that can see it).
"""

from __future__ import annotations

from ..data import cast
from ..data.matrix import Step, WriteClass
from ..data.rosters import FACTIONS
from ..decision import assemble
from ..decision.choose import pack_scenes
from ..decision.options import opening_set
from ..harness import populated as POP
from ..harness.corpus_run import attribute
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Act
from ..state.ids import H

# [ASSUMPTION; medium; Jordan to correct; revert: drop the `faction x` member if the spine's test faction
# leaves `rosters.yaml: factions`]: the factions with no authored head. `Guilds` and `Schoenland` are B-V's
# content (IN-36: who leads them is `#457` D4's cast, authored in `references/npc_registry.yaml`); B-V
# moves this pin when it seats them. `faction x` is the governance spine's test faction (Jordan
# 2026-09-18, `governance_spine.yaml`), never placed in the realm.
LEADERLESS = {"Guilds", "Schoenland", "faction x"}

# The heads whose computed act executed `via` their seat at the first fold, MEASURED 2026-10-14 (each a
# `dispatch`, `order.given`). A FLOOR, not the whole set: a head added to it (Restoration, or B-V's
# foreign head) is growth, and the test does not fail on it.
EXECUTES_AT_FIRST_FOLD = {"Crown", "Church of Solmund", "Hafenmark", "Varfell", "Löwenritter"}


def _pid(case_id: str) -> str:
    return f"p_{POP._slug(case_id)}"


def _heads() -> dict:
    """`{faction: person id}` for every faction with an authored head (`cast.faction_leader`)."""
    return {f: _pid(cid) for f in FACTIONS if (cid := cast.faction_leader(f))}


def _own_seats(w, f: str, pid: str) -> list:
    """The head's live `hold` Tenures on offices of the head's own faction."""
    return [t for t in w.tenures
            if t.kind == "hold" and t.live and t.subject == pid
            and t.object in w.offices and w.offices[t.object].faction == f]


def _built():
    w = POP.build_realm(0)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, a: Act) -> tuple:
    """Fold one act; `(made, refused)` for THAT act, by `corpus_run.attribute`, the one owner."""
    w.step = Step.RESOLVE
    w.log.extend(d.resolve(mint_token(w, WriteClass.ACTS), [a],
                           contest_max_depth=w.fixtures.get("contest_max_depth")))
    rows = [(made, no) for b, made, no in attribute(w, d, w.tick + 1) if b.id == a.id]
    assert len(rows) == 1, (a.id, rows)
    return rows[0]


def _again(a: Act) -> Act:
    """The same act, as a new object, to fold on another world."""
    return Act(id=a.id, actor=a.actor, verb=a.verb, via=a.via, payload=a.payload)


def _computed_acts_via(w, pid: str, seats: set) -> list:
    """Every act `pid`'s own decision machinery forms THROUGH one of `seats` this tick -- no act hand-built
    (the shape of the IN-48 build's `_computed_acts_via`, reverted at the B-J close, `40926a95`; no file
    carries it now)."""
    p = w.persons[pid]
    acts = []
    for q in world_q.questions_for(w, p):
        cands = opening_set(p, assemble(p, q, 12), q, w.fixtures)
        mint = lambda who, verb, subj, q=q: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}:{q.id}")
        for s in pack_scenes(p, cands, 99, w.fixtures, mint):
            acts.extend(a for a in s.acts if a.via in seats)
    return acts


def test_fa01_every_authored_head_holds_a_seat_of_its_own_faction():
    w = POP.build_realm(0)
    heads = _heads()
    assert set(FACTIONS) - set(heads) == LEADERLESS
    checked = 0
    for f, pid in heads.items():
        assert pid in w.persons, (f, pid)
        assert _own_seats(w, f, pid), f"{f}'s head {pid} holds no seat of {f}"
        checked += 1
    assert checked >= 6, checked


def test_fa01_exit_a_heads_computed_act_executes_via_its_seat_and_refuses_with_the_seat_removed():
    heads = _heads()
    w, d = _built()
    executed = {}
    for f, pid in heads.items():
        seats = {t.object for t in _own_seats(w, f, pid)}
        for a in _computed_acts_via(w, pid, seats):
            made, no = _fold(w, d, a)
            if made and not no:
                executed[f] = a
                break
    assert EXECUTES_AT_FIRST_FOLD <= set(executed), sorted(executed)
    for a in executed.values():
        assert a.via is not None

    # THE CONTROL: the same acts folded on a FRESH build with every seat standing. They execute there too,
    # so the refusal below comes from the closed seat and not from the acts having left the shared world
    # the first loop folded them in.
    wc, dc = _built()
    for f, a in executed.items():
        made, no = _fold(wc, dc, _again(a))
        assert made and not no, (f, a.verb, a.via, made, no)

    # THE FALSIFIER: a second build of the same seed, each head's own-faction seat closed (the seat
    # removed from under him; the office and every other edge stand), and THE SAME ACT folded again.
    w2, d2 = _built()
    for f, pid in heads.items():
        for t in _own_seats(w2, f, pid):
            t.until = w2.tick
        assert not _own_seats(w2, f, pid)
    refused = 0
    for f, a in executed.items():
        made, no = _fold(w2, d2, _again(a))
        assert no and not made, (f, a.verb, a.via, made, no)
        refused += 1
    assert refused == len(executed) >= len(EXECUTES_AT_FIRST_FOLD), refused
