"""GO-07 (batch B10-03b, the port gate's first position): THE PORTABLE DIGEST.

`World.content_hash` and `_entity_digest` fold a canonical, language-neutral byte encoding (the
table above `_OBJECT_HEADS` in `state/world.py`) under the same `blake2b`-128, no longer Python's
`repr()` and f-string formatting. Two halves:

  * THE VECTORS. Fixture entities whose encodings are committed byte strings, generated once from
    the encoder and pasted in: the port is built against them, so a change here is a declared
    format move that re-builds every pin. MUTATION, run 2026-10-28 and reverted: `_object_head`
    made to drop a dataclass's last field turns the Tenure vector test RED and the one-field test
    RED on `term`.
  * THE CONTROL. For seeds 0, 1 and 2 after one season: the event count, the per-collection entity
    counts, the census and the OLD `repr` digest (copied below as a local function, the base
    commit's bodies verbatim) equal what the base commit `b9beec9d` read. Its equality says no hashed
    state, act count, census figure or entity count moved; only the digest did (the old digest was
    blind to the act store, `tick` and a `Receipt`'s spec and serial, which the counts and the census
    only partly cover). The new digest is pinned beside it, so running this file under two
    `PYTHONHASHSEED`s shows the new hash does not depend on the process. AFTER GO-07 THIS CONTROL IS A
    CHANGE DETECTOR: every later batch that moves the world re-records it beside `BASE_HASHES`
    (`test_season_weather.py`).
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import types
from dataclasses import fields, replace
from enum import Enum
from fractions import Fraction
from pathlib import Path
from typing import NamedTuple

import pytest

from ..data.requires import UNKNOWN, Observation
from ..harness import populated as POP
from ..state.carriers import Event, Rung, Site, StateChange, Tenure, Term
from ..state.gate import Subject
from ..state.world import World, _canonical, _entity_digest

ROOT = Path(__file__).resolve().parents[3]


# --- THE VECTORS -----------------------------------------------------------------------------------

def _tenure() -> Tenure:
    """Str (a non-ASCII one, so a length is a BYTE count), int (a negative one), None, True, float,
    list, tuple, mapping and a nested dataclass (`Term`). `F` and `U` are pinned directly below."""
    return Tenure("t_fix", "p_rené", "set_town", "hold", 3, None, "Partial",
                  {"remit_acts": ("issue", "dispatch"), "w": 0.1, "n": -2, "ok": True,
                   "none": None, "l": [1, "x"]},
                  Term(7, "act:x"))


TENURE_VECTOR = (
    b"os6:Tenure9:"
    b"s2:ids5:t_fix"
    b"s7:subjects7:p_ren\xc3\xa9"
    b"s6:objects8:set_town"
    b"s4:kinds4:hold"
    b"s5:sincei3;"
    b"s5:untilN"
    b"s6:degrees7:Partial"
    b"s7:payloadm6:s10:remit_actst2:s5:issues8:dispatchs1:ll2:i1;s1:xs1:ni-2;"
    b"s1:wf3fb999999999999as2:okTs4:noneN"
    b"s4:termos4:Term2:s10:matures_ati7;s11:declared_bys5:act:x")
TENURE_VECTOR_HASH = "2bbf9687ea938a411784490f75428672"

# `Rung` is not a dataclass: its `_DECLARED` fields, sorted by name.
RUNG_VECTOR = (b"os4:Rung8:s5:datesl0:s8:envelopel0:s2:ids5:r_fixs4:kinds10:settlement"
               b"s7:recordsl0:s5:sitesl0:s6:storesm1:s5:graini3;s5:yieldm0:")
OBSERVATION_VECTOR = b"os11:Observation3:s7:subjects3:p_xs9:predicates9:conditions5:valueU"

# A whole world, frame by frame, in `content_hash`'s order: collections, tenures, then the log.
#
# THE THREE ORDERS DISAGREE HERE, ON PURPOSE, so a port that sorts everything by encoded bytes fails
# this vector: collection keys sort by raw `str` (`r_aaaaaa` before `r_fix`, though `s5:r_fix` precedes
# `s8:r_aaaaaa` as bytes), Tenure ids by raw `str` (`t_aaaaa` before `t_in`), and a mapping's entries by
# encoded bytes (`s2:bb` before `s3:aaa`, though `aaa` precedes `bb` as a `str`).
WORLD_FRAMES = (
    b"t3:s5:rungss8:r_aaaaaaos4:Rung8:s5:datesl0:s8:envelopel0:s2:ids8:r_aaaaaas4:kinds10:settlement"
    b"s7:recordsl0:s5:sitesl0:s6:storesm2:s2:bbi1;s3:aaai2;s5:yieldm0:",
    b"t3:s5:rungss5:r_fixos4:Rung8:s5:datesl0:s8:envelopel0:s2:ids5:r_fixs4:kinds10:settlement"
    b"s7:recordsl0:s5:sitesl0:s6:storesm1:s5:graini3;s5:yieldm0:",
    b"t3:s5:sitess5:s_fixos4:Site4:s2:ids5:s_fixs4:rungs5:r_fixs4:kinds7:harbours9:conditioni4;",
    b"t3:s6:docketi0;m1:s4:openF",
    b"t3:s1:Ts7:t_aaaaaos6:Tenure9:s2:ids7:t_aaaaas7:subjects8:r_aaaaaas6:objects7:r_realm"
    b"s4:kinds7:contains5:sincei0;s5:untilNs6:degreeNs7:payloadNs4:termN",
    b"t3:s1:Ts4:t_inos6:Tenure9:s2:ids4:t_ins7:subjects5:r_fixs6:objects7:r_realms4:kinds7:contain"
    b"s5:sincei0;s5:untilNs6:degreeNs7:payloadNs4:termN",
    b"t6:s1:Es4:ev_1s11:site.workedi2;s7:Partialt2:s5:act:xs5:act:y",
    b"t6:s1:~s5:s_fixs5:writes5:act:xs9:conditioni-1;",
    b"t2:s1:^os11:Observation3:s7:subjects5:s_fixs9:predicates9:conditions5:valuei4;",
)
WORLD_VECTOR_HASH = "08536e53dab620fe03b2c49eeee0dfd4"


def _tiny_world() -> World:
    w = World(0)
    w.rungs["r_fix"] = Rung("r_fix", "settlement", stores={"grain": 3})
    w.rungs["r_aaaaaa"] = Rung("r_aaaaaa", "settlement", stores={"bb": 1, "aaa": 2})
    w.sites["s_fix"] = Site("s_fix", "r_fix", "harbour", condition=4)
    w.add_tenure(Tenure("t_in", "r_fix", "r_realm", "contain", 0))
    w.add_tenure(Tenure("t_aaaaa", "r_aaaaaa", "r_realm", "contain", 0))
    w.docket = [{"open": False}]
    # A hand-built log, as `test_wb_the_carrier_moves_the_seeded_hash` strips one: the format of the
    # Event, change and observed frames is what is pinned, not how an Event reaches the log.
    w.log = [Event("ev_1", "site.worked",
                   [StateChange("s_fix", "write", "act:x", "condition", -1)],
                   ["act:x", "act:y"], 2, "Partial", (Observation("s_fix", "condition", 4),))]
    return w


def test_go07_the_fixture_entities_encode_to_the_committed_vectors():
    enc = _entity_digest(_tenure())
    assert enc == TENURE_VECTOR, enc
    assert hashlib.blake2b(enc, digest_size=16).hexdigest() == TENURE_VECTOR_HASH
    assert _entity_digest(Rung("r_fix", "settlement", stores={"grain": 3})) == RUNG_VECTOR
    assert _entity_digest(Observation("p_x", "condition", UNKNOWN)) == OBSERVATION_VECTOR


def test_go07_a_copied_unknown_is_still_unknown():
    """`UNKNOWN` is the one instance of a plain class with no `__deepcopy__`, so `copy.deepcopy` makes a
    SECOND instance and an identity test misses it. A world copied after a run (`test_person_projection`,
    `storybar.fork`) must hash as the original, and its UNKNOWN-valued observations must not raise."""
    assert copy.deepcopy(UNKNOWN) is not UNKNOWN, "the premise: a deep copy is a second instance"
    assert _canonical(copy.deepcopy(UNKNOWN)) == b"U"
    assert _entity_digest(copy.deepcopy(Observation("p_x", "condition", UNKNOWN))) == OBSERVATION_VECTOR
    w = _tiny_world()
    w.log[0].observed = (Observation("s_fix", "condition", UNKNOWN),)
    assert copy.deepcopy(w).content_hash() == w.content_hash()
    assert w.content_hash() != _tiny_world().content_hash(), "the UNKNOWN observation was not hashed"


def test_go07_the_world_hash_is_blake2b_over_the_committed_frames():
    w = _tiny_world()
    assert w.content_hash() == hashlib.blake2b(b"".join(WORLD_FRAMES), digest_size=16).hexdigest()
    assert w.content_hash() == WORLD_VECTOR_HASH


def test_go07_a_float_encodes_as_its_ieee754_bit_pattern():
    assert _canonical(0.1) == b"f3fb999999999999a"
    assert _canonical(1.0) == b"f3ff0000000000000"
    # `repr` would write `0.0` and `-0.0`; the bit patterns differ in the sign bit, and neither is text.
    assert _canonical(-0.0) == b"f8000000000000000" and _canonical(0.0) == b"f" + b"0" * 16
    enc = _entity_digest(_tenure())
    assert b"s1:wf3fb999999999999a" in enc, "the fixture's float field is not its bit pattern"
    assert repr(0.1).encode() not in enc, "a float reached the encoding as its `repr`"
    assert _canonical(0.1 + 0.2) != _canonical(0.3)


def test_go07_length_prefixing_separates_adjacent_strings():
    assert _canonical(("ab", "c")) == b"t2:s2:abs1:c"
    assert _canonical(("a", "bc")) == b"t2:s1:as2:bc"
    # The old log fold wrote `causes` as `','.join(e.causes)`, so these two cause lists collided.
    assert ",".join(("a,b",)) == ",".join(("a", "b"))
    assert _canonical(("a,b",)) != _canonical(("a", "b"))
    assert len({_canonical(("",)), _canonical(()), _canonical([])}) == 3


def test_go07_mapping_and_set_order_cannot_reach_the_encoding():
    assert _canonical({"b": 1, "a": 2, 3: None}) == _canonical({3: None, "a": 2, "b": 1})
    assert _canonical({"b": 1, "a": 2}) == b"m2:s1:ai2;s1:bi1;"
    assert _canonical({"x", "y", "z"}) == b"u3:s1:xs1:ys1:z"
    assert _canonical(frozenset({"y", "x"})) == b"z2:s1:xs1:y" != _canonical({"x", "y"})
    # A set sorts by its ENCODED items (`s1:b` before `s2:aa`), not by the raw `str` (`aa` before `b`).
    assert _canonical({"b", "aa"}) == b"u2:s1:bs2:aa"
    assert len({_canonical(1), _canonical(True), _canonical(1.0)}) == 3
    assert _canonical((True, False)) == b"t2:TF"

    class _E(Enum):
        A = "a"
    assert _canonical(_E.A) == b"es1:a"
    # A set of strings iterates in a per-process order; its encoding must not.
    prog = ("import sys; sys.path.insert(0, sys.argv[1]); "
            "from engine.season.state.world import _canonical; "
            "s = {f'id_{i}' for i in range(40)}; print(list(s)[:3], _canonical(s).hex())")
    outs = [subprocess.run([sys.executable, "-c", prog, str(ROOT)], capture_output=True,
                           text=True, check=True,
                           env={**os.environ, "PYTHONHASHSEED": seed}).stdout.strip()
            for seed in ("0", "1")]
    (order0, enc0), (order1, enc1) = (o.rsplit(" ", 1) for o in outs)
    assert order0 != order1, "the two processes iterated the set alike: this leg observed nothing"
    assert enc0 == enc1, "a set's encoding moved with PYTHONHASHSEED"


def test_go07_a_named_tuple_encodes_as_an_object_in_field_order():
    class _P(NamedTuple):
        x: int
        y: str
    assert _canonical(_P(1, "a")) == b"os2:_P2:s1:xi1;s1:ys1:a"
    assert _canonical(_P(1, "a")) != _canonical((1, "a"))


def test_go07_a_subclass_of_a_scalar_or_sequence_encodes_as_its_base():
    """`_encode_into` takes the exact-type branch for the hot types and a subclass fallback for the
    rest; a subclass instance (a `SeatId`, a numpy-style float, an int or sequence subclass) encodes
    byte-for-byte as its base type, so there is one encoding per type and not two."""
    class _I(int): pass
    class _F(float): pass
    class _S(str): pass
    class _L(list): pass
    class _T(tuple): pass
    for sub, base in ((_I(-7), -7), (_F(0.1), 0.1), (_S("p_a"), "p_a"),
                      (_L([1, "x"]), [1, "x"]), (_T((1, "x")), (1, "x"))):
        assert _canonical(sub) == _canonical(base), (type(sub), _canonical(sub), _canonical(base))
    assert _canonical(_L([1])) != _canonical(_T((1,))), "list and tuple must stay distinct"


def test_go07_a_fields_reading_is_the_canonical_encoding_not_repr():
    """G4 has one notion of "moved". A `fields=` subject reads its attributes through the same
    encoding as an `entity` subject, so a write that only re-orders a named mapping reads as
    unmoved (`before == after` on a dict), while `1`, `1.0` and `True` stay apart and the reading is
    a snapshot, not a reference."""
    w = _tiny_world()
    rung = w.rungs["r_fix"]
    sub = Subject.entity("rungs", "r_fix", fields=("stores",))
    whole = Subject.entity("rungs", "r_fix")
    rung.stores = {"grain": 3, "salt": 1}
    fields_a, whole_a = w.state_of(sub), w.state_of(whole)
    rung.stores = {"salt": 1, "grain": 3}
    assert w.state_of(sub) == fields_a, "a pure re-order of a named mapping read as moved"
    assert w.state_of(whole) == whole_a, "the two readings disagree about the same re-order"
    for other in ({"salt": 1, "grain": 3.0}, {"salt": 1, "grain": True}, {"salt": 1, "grain": 4}):
        rung.stores = other
        assert w.state_of(sub) != fields_a, other
        assert w.state_of(whole) != whole_a, other
    rung.stores = {"grain": 3, "salt": 1}
    held = w.state_of(sub)
    rung.stores["grain"] = 4                       # an in-place mutation of the same dict object
    assert w.state_of(sub) != held, "the reading held a reference, not a snapshot"
    assert all(isinstance(x, bytes) for x in w.state_of(sub)[1:]), "a fields reading is not canonical"


def test_go07_one_field_of_one_entity_moves_the_digest():
    """H-118's falsifier, field by field: every declared field of the fixture, changed alone, moves
    the entity's encoding; and one Site field changed in one of two otherwise identical worlds moves
    the world's hash."""
    base = _tenure()
    other = {"id": "t_other", "subject": "p_other", "object": "set_other", "kind": "contain",
             "since": 4, "until": 9, "degree": None, "payload": None, "term": Term(7, "act:y")}
    checked = 0
    for f in fields(Tenure):
        assert _entity_digest(replace(base, **{f.name: other[f.name]})) != _entity_digest(base), (
            f"`Tenure.{f.name}` changed alone and the digest did not move")
        checked += 1
    assert checked == len(other) == 9
    rung = Rung("r_fix", "settlement", stores={"grain": 3})
    for name in sorted(vars(rung)):
        alt = Rung("r_fix", "settlement", stores={"grain": 3})
        object.__setattr__(alt, name, "changed")
        assert _entity_digest(alt) != _entity_digest(rung), f"`Rung.{name}` did not move the digest"
        checked += 1
    assert checked == 9 + 8
    w1, w2 = _tiny_world(), _tiny_world()
    assert w1.content_hash() == w2.content_hash()
    w2.sites["s_fix"].condition = 3
    assert w1.content_hash() != w2.content_hash()


def test_go07_a_type_with_no_rule_raises_rather_than_guessing():
    class _Plain:
        def __init__(self):
            self.a = 1

    # The last three HAVE a `__dict__` (a function, a namespace, a plain instance): a generic
    # `vars()` rule would encode them silently, and `lambda: 0` and `lambda: 1` would collide.
    probes = (object(), Fraction(1, 3), 1j, lambda: 0, types.SimpleNamespace(a=1), _Plain())
    for v in probes:
        with pytest.raises(TypeError, match="GO-07: no canonical encoding"):
            _canonical(v)
    assert len(probes) == 6


# --- THE CONTROL -----------------------------------------------------------------------------------

def _old_entity_digest(obj):
    """The base commit's `_entity_digest`, verbatim: the `repr` digest GO-07 replaced."""
    if hasattr(obj, "__dataclass_fields__"):
        return repr(obj)
    if isinstance(obj, dict):
        return repr(sorted((str(k), repr(v)) for k, v in obj.items()))
    if hasattr(obj, "__dict__"):
        return repr(sorted(vars(obj).items()))
    return repr(obj)


def _old_content_hash(w) -> str:
    """The base commit's `World.content_hash` body, verbatim, over `_old_entity_digest`."""
    h = hashlib.blake2b(digest_size=16)
    for name in World._STATE_COLLECTIONS:
        for k in sorted(getattr(w, name, {}) or {}):
            h.update(f"{name}|{k}|{_old_entity_digest(getattr(w, name)[k])}".encode())
    for name in World._STATE_SEQUENCES:
        for n, item in enumerate(getattr(w, name, ()) or ()):
            h.update(f"{name}|{n}|{_old_entity_digest(item)}".encode())
    for t in sorted(w.tenures, key=lambda t: t.id):
        h.update(f"T|{t.id}|{_old_entity_digest(t)}".encode())
    for e in w.log:
        h.update(f"{e.id}|{e.kind}|{e.emitted_at}|{e.degree}|"
                 f"{','.join(e.causes)}".encode())
        for c in e.changes:
            h.update(f"~{c.subject}|{c.mode}|{c.driver}|{c.field}|{c.delta}".encode())
        for o in (getattr(e, "observed", None) or []):
            h.update(f"^{o}".encode())
    return h.hexdigest()


def _counts(w) -> dict:
    out = {n: len(getattr(w, n)) for n in World._STATE_COLLECTIONS + World._STATE_SEQUENCES}
    out["tenures"] = len(w.tenures)
    out["log"] = len(w.log)
    return out


#: Read on the base commit `b9beec9d` (the old digest; PYTHONHASHSEED 0 and 1 identical), except
#: `new`, read on the GO-07 tree. `census` is the sha256 of `populated.run`'s return value as sorted
#: JSON -- the census plus `acts`, `actors`, `act_subjects` and `claim_sources`.
#: RE-RECORDED at v10 REM-22 (B10-05), A GAME MOVE DECLARED, NO DIGEST MOVE: `restore`, `work` and `examine`
#: declare `referent_class: Site`, so the act mix of every seeded realm moves; EVERY value below is the REM-22
#: tree's, read with this file's own helpers (`_old_content_hash`, `_counts`) and `populated.run`, and the control
#: still means what it meant -- the digest format changed and the world, at a given tree, did not (the two
#: digests are read of the SAME run). Was, for seeds 0 / 1 / 2: `old` b2464a6c... / 97d2d92f... / 455cfe8d...,
#: `new` 947c190b... / 36ef9545... / 7e8df32a..., `acts` 539 / 560 / 588, `log` 7018 / 8128 / 6879.
#: RE-RECORDED AGAIN at v10 REM-23 (B10-05), A GAME MOVE DECLARED, NO DIGEST MOVE: `commit` declares
#: `referent_class: Proposition`, so it forms only on a Proposition the question it answers names -- 83 of 83
#: persons formed it before (attempted 38 / 33 / 34 at seeds 0 / 1 / 2, `aperture 1 s`), 6 / 2 / 1 do now
#: (attempted 1 / 1 / 1) -- and the act mix of every seeded realm moves with it. EVERY value below is the REM-23
#: tree's, read with this file's own helpers (`_old_content_hash`, `_counts`) and `populated.run`; CONTROL, run: the
#: same script on the REM-22 tree (`e66a22ec`) reads the values this block held, so the move is this unit's.
#: Was, for seeds 0 / 1 / 2: `old` ea5d101c... / 0982d7ba... / 978f8690..., `new` 3c627dea... / 9b9145f7... /
#: 7619c18e..., `acts` 543 / 588 / 607, `log` 7345 / 10146 / 8132.
#: RE-RECORDED AGAIN at v10 REM-24 (B10-05), A GAME MOVE DECLARED, NO DIGEST MOVE: `petition` declares
#: `referent_class: Person`, so it forms only on a person the question it answers names -- formed for 82 / 81 / 82
#: of 83 persons before (attempted 19 / 17 / 20, refused 9 / 13 / 12, every one on `exists:Person=0`), 40 / 39 / 43
#: do now (attempted 10 / 4 / 8, refused 0) -- and the act mix of every seeded realm moves with it. EVERY value below
#: is the REM-24 tree's, read with this file's own helpers (`_old_content_hash`, `_counts`) and `populated.run`;
#: CONTROL, run: the same script on the REM-23 tree (`409c467b`, a `git worktree`) reads the values this block held
#: exactly, so the move is this unit's. Was, for seeds 0 / 1 / 2: `old` 26fa3179... / e51b0d83... / c961a57a...,
#: `new` 290655d8... / 9537c69e... / 43b51550..., `acts` 532 / 582 / 583, `log` 6647 / 8656 / 7196.
#: RE-RECORDED AGAIN at v10 REM-25 (B10-05), A GAME MOVE DECLARED, NO DIGEST MOVE: `carry`, `found` and `build`
#: declare `referent_class: Record`, and the `Record` term widens from `writs_held` to `writs_held` plus
#: `records_held_for_holding_rows`, so they form only on a Record the person holds (a petition, for the realm) --
#: 83 of 83 persons formed each before (`carry` attempted 15 / 18 / 12, `found` 11 / 14 / 21, `build` 12 / 13 / 12,
#: all refused on `exists:petition=0` / `exists:works=0`, `aperture 1 s`), 9 / 4 / 9 do now (`carry` attempted
#: 2 / 0 / 1, executed 2 / 0 / 1; `found` 0 / 0 / 0; `build` 0 / 1 / 1), and `comply` forms on a held petition his
#: ledger names (attempted 2 / 2 / 1, refused on `exists:dispensation=0`) -- and the act mix of every seeded realm
#: moves with it. EVERY value below is the REM-25 tree's, read with this file's own helpers (`_old_content_hash`,
#: `_counts`) and `populated.run`; CONTROL, run: this file's own control test on a detached worktree at the REM-24
#: tree (`f2381695`) is green against the values this block held, so the move is this unit's. Was, for seeds
#: 0 / 1 / 2: `old` 9930edaa... / eaa35b59... / 7397b498..., `new` cd0ea7bc... / 3688012e... / 9dde0b7b...,
#: `acts` 529 / 579 / 578, `log` 6396 / 8662 / 7190.
#: RE-RECORDED AGAIN at v10 CP-T05-04 (B10-05), A GAME MOVE DECLARED, NO DIGEST MOVE: `argue` declares
#: `referent_class: Proposition` and `open_case` declares `Person`, and `world_q.docket_question` asks the witness
#: of a docketing about the matter docketed -- `argue` formed for 37 / 35 / 39 of 83 persons before (attempted 8 / 10 / 5,
#: every one refused on `exists:Proposition=0`, `aperture 1 s`), for none now; `open_case` formed for 8 / 8 / 8 persons
#: and 6 / 6 / 8 do (executed 4 / 2 / 1 -> 2 / 1 / 1 with the question, 3 / 1 / 1 with the columns alone: the lost case
#: is `terr_T13`'s, a rung) -- and the act mix of every seeded realm moves with it (the docket question moves seeds 0 and
#: 1 and not seed 2). EVERY value below is the CP-T05-04 tree's, read with this file's own helpers (`_old_content_hash`,
#: `_counts`) and `populated.run`; CONTROL, run: this file's own control test on a detached worktree at the REM-25 tree
#: (`92892b09`) is green against the values this block held, so the move is this unit's; and in-process on this tree the
#: columns alone (the docket term stubbed) read `new` 7f36d369... / 43c143d5... / b3e6f82c... and the docket question
#: alone (the columns blanked) 66a48d9a... / 209b02f9... / 7e87cc54..., so each unit moves the hash by itself (seed 2:
#: the question moves nothing). Was, for seeds 0 / 1 / 2: `old` 38c7de45... / 233f7e8e... / 09176dd8..., `new`
#: da1ce5eb... / f80b2949... / 7e87cc54..., `acts` 523 / 575 / 591, `log` 6348 / 8597 / 7724.
#: RE-RECORDED AGAIN at v10 REM-2C (B10-05), A GAME MOVE DECLARED, NO DIGEST MOVE: `research` declares
#: `referent_class: Record` and `Record` leaves `rosters.yaml: occasion_only_classes`, so the own-referent term stamps
#: the question's own Records and `research` forms only on a Record -- formed for 83 / 83 / 83 persons before (attempted
#: 69 / 66 / 53, refused at admission on `exists:Record=0` 67 / 62 / 53, `aperture 1 s`), 23 / 20 / 25 now (attempted
#: 5 / 8 / 1, none refused at admission) -- and the act mix of every seeded realm moves with it (the freed scene slots
#: go to other verbs). EVERY value below is the REM-2C tree's, read with this file's own helpers (`_old_content_hash`,
#: `_counts`) and `populated.run`; CONTROL, run: this file's own control test on a detached worktree at the CP-T05-04
#: tree (`ea6f1dba`) is green against the values this block held, so the move is this unit's (each half moves the
#: one-season hash alone: `test_season_weather.py`'s `BASE_HASHES` note). Was, for seeds 0 / 1 / 2: `old`
#: 956afe6b... / 508ac507... / 7d9c2981..., `new` 26bcb37d... / 3b43b9fc... / b3e6f82c..., `acts` 524 / 577 / 595,
#: `log` 6267 / 8493 / 7707.
#: RE-RECORDED AGAIN at v10 REM-52 (B10-05), A GAME MOVE DECLARED, NO DIGEST MOVE: `body_step` ships at `10`, `H-125`'s
#: live arm (it was the control `0`), so the first MATTER draw of the realm, which finds every larder empty, falls
#: the body of each cohort it leaves short by `10` x its unmet units (36 / 32 / 35 of the 37 cohorts from 1000 to 940
#: at seeds 0 / 1 / 2, 37 `body.changed` Events at seeds 0 / 1 and 38 at seed 2, where the base held 0 / 0 / 1), and
#: the act mix of every seeded realm moves with it (the mechanism between the Events and the acts is not split here):
#: `acts` 577 / 637 / 630 -> 576 / 637 / 629, `log` +107 / +110 / +107 Events, `aperture 1 s`: `tend` executed
#: (attempted less refused) 1 / 0 / 1 -> 2 / 5 / 3, `utter` attempted +1 at seed 0, `challenge` -1 and `release` +1
#: attempted at seed 1, no other verb row moves. No budget band is crossed at 940. NOBODY DIES OF IT: at
#: `10` the lowest body is 940, and `person.died` is the same Event set before and after (1 / 0 / 2 at seeds 0 / 1 / 2,
#: p_npc_050; none; p_npc_034 and p_npc_041, all RESOLVE-written). EVERY value below is the REM-52 tree's, read with
#: this file's own helpers (`_old_content_hash`, `_counts`) and `populated.run`; CONTROL, run: the same script on a
#: detached worktree at the REM-2C tree (`a397fa16`, whose game code is `07f46301`'s) reads the values this block
#: held exactly, and so does the REM-52 tree with `body_step` swept back to `0` in `data/fixtures.py` and
#: `written=True` left in `loop/matter.py` (a scratch worktree), so the move is `body_step`'s alone and
#: `written=True` moves nothing at these seeds. Was, for seeds 0 / 1 / 2: `old` 7a9ba50d... / 0418dc12... /
#: 35e6932d..., `new` 8bec380b... / 82223978... / e707d359..., `acts` 577 / 637 / 630, `log` 6377 / 9117 / 7933.
#: RE-RECORDED AGAIN at v10 REM-27 (B10-06), A GAME MOVE DECLARED, NO DIGEST MOVE: `march` declares
#: `referent_class: Rung`, so it forms only on a Rung the question carries as `Rung` (`places_named`,
#: `larders_in_purview`), and `RUNG_REMIT_ACTS` widens by derivation to `{issue, dispatch}` -- `march` attempted
#: 10 / 15 / 3 -> 8 / 24 / 10 (`aperture 1 s`, every one still refused), and the act mix of every seeded realm moves
#: with it. EVERY value below is the REM-27 tree's, read with this file's own helpers (`_old_content_hash`, `_counts`)
#: and `populated.run`; CONTROL, run in process on this tree: `march`'s column blanked in the shared `VERB_TABLE` and
#: `RUNG_REMIT_ACTS` narrowed back to `{issue}` reads the values this block held exactly, at all three seeds. Was, for
#: seeds 0 / 1 / 2: `old` 3d139b32... / 31fa260b... / 3f836210..., `new` 5d2e5f77... / 8a50ca82... / b8678a41...,
#: `acts` 576 / 637 / 629, `log` 6484 / 9227 / 8040.
#: RE-RECORDED AGAIN at v10 REM-28 (B10-06), A GAME MOVE DECLARED, NO DIGEST MOVE: `convene` declares `referent_class:
#: Rung`, so it forms only on a Rung the question carries as `Rung` (`places_named`, `larders_in_purview`) and never on
#: a person-rung or a Proposition, and `RUNG_REMIT_ACTS` widens by derivation to `{issue, dispatch, convene}` (no offer
#: moves). `convene` attempted 3 / 0 / 5 -> 4 / 5 / 6 and executed 1 / 0 / 1 -> 4 / 5 / 5 (`aperture 1 s`, realm), and
#: each convened date carries a holder, so CALENDAR forms docket slots (`dates` 1 / 0 / 1 -> 4 / 5 / 5, `log` +711 /
#: +1421 / +926). EVERY value below is the REM-28 tree's, read with this file's own helpers (`_old_content_hash`,
#: `_counts`) and `populated.run`; CONTROL, run in process on this tree: `convene`'s column blanked in the shared
#: `VERB_TABLE` and `RUNG_REMIT_ACTS` re-derived reads the values this block held exactly, at all three seeds. Was, for
#: seeds 0 / 1 / 2: `old` ab2da387... / fd4a0315... / 9c74e8d9..., `new` ecb47cd0... / 27e9d231... / 9726db8d...,
#: `acts` 581 / 641 / 632, `log` 6482 / 9221 / 8096.
#: RE-RECORDED AGAIN at v10 REM-28 `dispatch` (B10-06), A GAME MOVE DECLARED, SEED 1 UNMOVED: `dispatch` declares
#: `referent_class: Person`, so it forms only on a person the question names and never on a rung, a Record or a Site
#: (`names no person the world holds`, 16 of 33 pooled attempts at `aperture 1 s`, all refused), and no derived set
#: moves. Seeds 0 and 2 re-record (`dispatch` attempted 11 / 8 / 8 -> 2 / 8 / 6, refused 9 / 0 / 2 -> 0, the freed scenes
#: taken by other acts: `acts` 583 / 642 / 627 unmoved in count, `log` 7193 -> 7196 and 9022 -> 9030); seed 1, where no
#: `dispatch` was refused, reads the block above exactly. EVERY value below is the REM-28 `dispatch` tree's, read with this
#: file's own helpers and `populated.run`; CONTROL, run in process on this tree: `dispatch`'s column blanked in the shared
#: `VERB_TABLE` reads the values this block held exactly, at all three seeds. Was, seed 0: `old` cfc94deb..., `new`
#: 7d99c0f7..., `census` 0124fffe..., `records` 102, `tenures` 817, `log` 7193; seed 2: `old` c4d68221..., `new`
#: 7f9c285d..., `census` 9f007552..., `log` 9022.
#: RE-RECORDED AGAIN at v10 REM-28 `revoke` (B10-06), A GAME MOVE DECLARED, SEED 2 ALONE: `revoke` declares `referent_class:
#: Office`, so it forms only on a seat the question carries as an Office and never on a person, a rung, a Record or a Site
#: (`names no office the world holds`, 18 of 18 pooled attempts at `aperture 1 s`, all refused), and it EXECUTES NOTHING
#: either way (`_req_revoke` reads `office`, a computed act carries `subject`: IN-53 D1, H-207 (A)). No derived set moves.
#: Only seed 2 had a `revoke` attempted (7 attempts, all refused, 9 -> 7 after the dispatch commit), so seeds 0 and 1 read the
#: block above exactly; at seed 2 the freed scenes are taken by other acts (`acts` 627 -> 625, `log` 9030 -> 9029). EVERY value
#: below is the REM-28 `revoke` tree's, read with this file's own helpers and `populated.run`; CONTROL, run in process on
#: this tree: `revoke`'s column blanked in the shared `VERB_TABLE` reads the values this block held exactly, at all three
#: seeds. Was, seed 2: `old` 5e120ea4..., `new` e3e9e5a5..., `census` 8bdf5c05..., `acts` 627, `log` 9030.
#: RE-RECORDED AGAIN at v10 CR-23 (B10-06), A GAME MOVE DECLARED, NO DIGEST MOVE: MATTER's last `stores` write to a rung
#: carries the stock report (`stores:<kind>`) when `requisitionable` flips across the barrier (`Fixtures stock_report =
#: crossing`, `H-243`), WITNESS deposits it to the seats over the larder, and the larders they are told of are stamped for
#: `requisition`, so the act mix of every seeded realm moves (`log` 7196 / 10642 / 9029 -> 9270 / 11955 / 9381: the
#: deposits and what follows them). EVERY value below is the CR-23 tree's, read with this file's own helpers and
#: `populated.run`; CONTROL, run in process on this tree: `stock_report = off` reads the values this block held exactly,
#: at all three seeds. Was, for seeds 0 / 1 / 2: `old` 0e54dc8a... / 25a37ac1... / eff84f40..., `new` 30a95964... /
#: 79336806... / c39ac83e..., `acts` 583 / 642 / 625, `log` 7196 / 10642 / 9029.
#: RE-RECORDED AGAIN at v10 REM-29 (B10-06), A GAME MOVE DECLARED, NO DIGEST MOVE: `migrate`'s capacity throttle is a
#: `room` conjunct (`world_q.has_room`), so a full rung is refused at admission with the read on the Event, WITNESS
#: deposits it to the migrant and he does not re-form that `migrate` (`aperture 1 s`, realm: attempted 67 / 135 / 88 ->
#: 41 / 80 / 61); the freed scenes and the deposited claims move the act mix of every seeded realm (`acts` 602 / 644 / 617
#: -> 598 / 640 / 619, `log` 9270 / 11955 / 9381 -> 9316 / 12278 / 9949). EVERY value below is the REM-29 tree's, read
#: with this file's own helpers and `populated.run`; CONTROL, run on this tree: the `room` conjunct and its refusal key
#: deleted from `migrate`'s row reads the values this block held exactly, at all three seeds. Was, for seeds 0 / 1 / 2:
#: `old` f84cb2d2... / 185bd2be... / 42ac60f1..., `new` 1d402d15... / ce81d904... / 47b0b565..., `census` 3004e5b7... /
#: c1d5db92... / ba91b58d....
#: RE-RECORDED AGAIN at v10 REM-2B (B10-06), A GAME MOVE DECLARED, NO DIGEST MOVE: `evade / defy`, `construe` and `exchange`
#: are typed and resolvable again (v9 IN-09 / IN-33 restored), so the chooser offers them and their attempts (`exchange` 21 /
#: 36 / 34 at `aperture 1 s`, none executed) take scenes and emit refusals that WITNESS deposits: the act mix of every seeded
#: realm moves (`acts` 598 / 640 / 619 -> 597 / 643 / 632, `log` 9316 / 12278 / 9949 -> 9319 / 11995 / 9722). EVERY value
#: below is the REM-2B tree's, read with this file's own helpers and `populated.run`; CONTROL, run in process on this tree: the
#: three rows put back to their base shape (untyped, unclassed, their decline notes, `exchange` writing one pair with no effect)
#: read the values this block held exactly, at all three seeds. Was, for seeds 0 / 1 / 2: `old` 1842a06d... / e13520cf... /
#: e06e57c1..., `new` 4cc07cbe... / 6e72eb59... / 8e5af677..., `census` 7ab6c655... / 26755d2c... / 03428a48....
#: RE-RECORDED AGAIN at v10 IN-45 (B10-06), A DATA MOVE DECLARED: `venues.yaml: planned_works` authors two works, minted last in
#: `build_realm` through `create_record`'s own effect, so the build moves (two Records and their masters' `hold` edges: `records`
#: +2, `tenures` +2) and the seed-0 season takes one more act (597 -> 598, `log` 9319 -> 9334): the masters' `found` and `build`
#: form on their works and the seed-0 realm's sampled order shifts. Seeds 1 and 2 keep their acts, census and log (a works's terms
#: first ripen at tick 1, which one season does not reach). EVERY value below is the IN-45 tree's, read with this file's own helpers
#: and `populated.run`; CONTROL, run in process on this tree: `planned_works` emptied reads the values this block held exactly, at
#: all three seeds, and the build world's old digest and content hash. Was, for seeds 0 / 1 / 2: `old` 789bc9eb... / 64276910... /
#: b8031dc3..., `new` 41ffb48b... / 6c52b44c... / 9bb7306d..., `census` ed0c8bac... (seed 0; seeds 1 and 2 unmoved).
BASE = {
    # SEED 0 RE-RECORDED, ED-IN-0306 (`arrival_only_kinds`, on top of main at 59f2f97f): a computed `migrate` onto a territory
    # rung is declined (migrate.refused 35->40, residence.changed 3->1, claim.deposited 8190->8233; acts 598->599). CONTROL:
    # main at 59f2f97f, probed in its own checkout by the same run, reads the previous entry exactly.
    0: {"old": "faa7f2b173ad28cc63a18b514d6d835a", "new": "873525dfb363231695cefb17ad4b17a1", "acts": 599,
        "census": "89a3fbcdb936497449f34fb9402af7568537dd3ebc57e64dcfaed248e9a970a3",
        "counts": {"persons": 82, "rungs": 411, "offices": 32, "sites": 322, "records": 118,
                   "propositions": 98, "dates": 7, "docket": 6, "tenures": 843, "log": 9378}},
    # SEED 1 RE-RECORDED, ED-IN-0306 phases 4 and 5 (on top of main at 59f2f97f): `march_target_kinds` gained `territory`, so computed
    # marches on territory referents now resolve (army.arrived 5->6, field.unopposed 5->6, march.declared 21->18, march.refused
    # 16->12), and computed `move`s and `migrate`s onto a territory are declined (travel.moved 11->10, travel.blocked 22->23,
    # residence.changed 3->2; acts 643->638). CONTROL: main at 59f2f97f reads the previous entry exactly.
    1: {"old": "0be6716a18eb57d44cea06e05aaf643b", "new": "3c6c0de333bba66196eb5b76a07d75ed", "acts": 638,
        "census": "b2c3ef40dcb036301a6b96166a104c46fb04eb9b36316b52d4a02e779b90e804",
        "counts": {"persons": 83, "rungs": 412, "offices": 32, "sites": 322, "records": 135,
                   "propositions": 96, "dates": 7, "docket": 2, "tenures": 868, "log": 11960}},
    # SEED 2 RE-RECORDED, same cause (travel.moved 4->3, travel.blocked 27->29; acts 632->633). CONTROL: main at 59f2f97f reads
    # the previous entry exactly.
    2: {"old": "ab260df2819bdb10e12c8488fde208e2", "new": "07a0c78487abfd59764989aae839694a", "acts": 633,
        "census": "10f3da318d1ec1d17663728e67fd2d099c45c57f59b79a3948112049b75944ad",
        "counts": {"persons": 81, "rungs": 410, "offices": 32, "sites": 322, "records": 125,
                   "propositions": 100, "dates": 7, "docket": 2, "tenures": 842, "log": 9726}},
}


def test_go07_control_the_build_world_old_digest_is_unmoved():
    """The base commit's `repr` digest of `build_realm(0)`, before a single act, read this literal
    (`test_season_weather.BASE_HASHES[0]`'s retired value); the same world now reads the new pin."""
    w = POP.build_realm(0)
    assert _old_content_hash(w) == "bcc59ba42cdfe4fa740e8d50c3b4f7c0"        # v10 IN-45: was 8e4032a2... (control reads it)
    assert w.content_hash() == "fe427626f9e91ab83ffd556c0bec4ea7"            # v10 IN-45: was 9ff53909... (control reads it)


def test_go07_control_the_world_did_not_move_only_its_digest():
    checked = 0
    for seed, base in BASE.items():
        w = POP.build_realm(seed)
        out = POP.run(1, seed, w=w)
        got = {"old": _old_content_hash(w), "new": w.content_hash(), "acts": out["acts"],
               "census": hashlib.sha256(json.dumps(out, sort_keys=True, default=repr)
                                        .encode()).hexdigest(),
               "counts": _counts(w)}
        assert got == base, f"seed {seed}: {got}"
        assert got["old"] != got["new"], "the digest format did not change"
        checked += 1
    assert checked >= 3
