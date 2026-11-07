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
#: (The per-seed ED-IN-0306 re-record notes this block carried before SE-06 are at `git show 4de5f994d:engine/season/tests/test_go07_canonical_digest.py`.)
#: RE-RECORDED AGAIN at v10 SE-06 (B10-07b), A DATA MOVE DECLARED: the 37 population cohorts hold their territory's temperament as
#: pursuits (`cohorts.yaml: temperaments:`), so the build moves (the cohorts' `pursuits` only: the counts of persons, rungs, offices and
#: sites are unchanged) and every seeded season takes another path (`acts` 599 / 638 / 633 -> 598 / 640 / 653, `log` 9378 / 11960 /
#: 9726 -> 8913 / 11937 / 9718). EVERY value below is this tree's, read with this file's own helpers and `populated.run`; CONTROL,
#: run in process on this tree: `temperaments:` deleted from a copy of `cohorts.yaml` reads the values this block held exactly, at
#: all three seeds, and the build world's old digest and content hash. Was, for seeds 0 / 1 / 2: `old` faa7f2b1... / 0be6716a... /
#: ab260df2..., `new` 873525df... / 3c6c0de3... / 07a0c784..., `census` 89a3fbcd... / b2c3ef40... / 10f3da31....
#: RE-RECORDED AGAIN at v10 CR-21 (M14, B10-07b), A DATA MOVE DECLARED: `happiness`'s `deontological_instrumental` cell +0.4 -> 0.0 (which
#: SE-06's cohort vectors read, so the build moves), `restore` celled (P/S -0.2) and the `deed:commitment.ended` cells re-rank candidates,
#: so every seeded season takes another path (`acts` 598 / 640 / 653 -> 606 / 651 / 655, `log` 8913 / 11937 / 9718 -> 9180 / 10898 / 9946).
#: A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM. EVERY value below is this tree's, read with this file's own helpers and `populated.run`;
#: CONTROL: the SE-06 tree (`bcaf1d519`) held the values listed as `Was` (its own pins; the build and two-season hashes of seed 0 were
#: re-read on an extracted copy of it, see `test_season_weather.BASE_HASHES`). Was, for seeds 0 / 1 / 2: `old` 7d1989f6... / ac68817f... / ed7ce0c1..., `new` 31e39c05... / 301950ee... / 83b98aac...,
#: `census` fce1b6a7... / 4029aeb0... / 4a8f2001....
#: RE-RECORDED AGAIN at v10 CR-16 (B10-07b), A BEHAVIOUR MOVE DECLARED: `Fixtures stance_polarity` `legacy` -> `declared`, so a grudge pulls
#: the contested acts against its object (every contested row whose opponent is its subject; `arrest` never forms in the realm, G-07) UP instead of down and every seeded season takes another path
#: (`acts` 606 / 651 / 655 -> 597 / 608 / 650, `log` 9180 / 10898 / 9946 -> 9347 / 10636 / 10728). The BUILD is unmoved (`Fixtures` is not
#: hashed: the build world's old digest and content hash below are the previous pins). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM. EVERY
#: value below is this tree's, read with this file's own helpers and `populated.run`; CONTROL, run in process on this tree:
#: `stance_polarity` swept back to `legacy` reads the values this block held exactly, at all three seeds. Was, for seeds 0 / 1 / 2: `old`
#: a70f7a83... / f51795a7... / 60507c37..., `new` e9f81463... / 4516fc49... / d2138e3a..., `census` 711e456d... / 6d9bd351... / a5adac42....
#: RE-RECORDED AGAIN at v10 CP-T02-01 (B10-09), A BEHAVIOUR MOVE DECLARED: a death names the seats it empties (one
#: `tenure.closed` per death write, receipted under the Offices), so every witness holds a claim on each vacated seat and the
#: seeded first seasons of seeds 0 and 1 take another path (seed 2's first season reads its old values unmoved). CONTROL, run in process on this tree: `World.seat_holds` stubbed to `[]` (the emission
#: off) reads the values this block held exactly. Was, for seeds 0 / 1: `old` 95068857... / 303810a3..., `new` 056584ed... /
#: 48e59dc4..., `census` f8f221e0... / f864b5ae..., `acts` 597 / 608, `log` 9347 / 10636. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
#: RE-RECORDED AGAIN at v10 CP-T02-02 (B10-09), AN ID MOVE DECLARED: a loop-built seat keeps its `offices.yaml` row's id
#: (`populated._seat_id`: the throne is `off_king`, no longer `off_npc_020`), so every hash that folds an Office id moves, and the ids
#: seed the draws, so the seeded first seasons of seeds 0 and 1 take another path (`acts` 608 / 616 -> 596 / 621, `log` 9138 / 11007 ->
#: 9760 / 11149; seed 2 keeps its acts, census, counts and log and re-hashes only). CONTROL, run in process on this tree: `_seat_id` replaced
#: by the slug rule (`off_<case slug>`) reads the values this block held exactly, at all three seeds, and the build world's old digest and
#: content hash. Was, for seeds 0 / 1 / 2: `old` e6f28fc9... / 85e94055... / 8a2d9108..., `new` b4aa3024... / 4687d35a... / 31f199ea...,
#: `census` 3c5fb2de... / 298a3ea5... (seed 2 unmoved). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
#: RE-RECORDED AGAIN at v10 CP-T03-00 (B10-09), A BEHAVIOUR MOVE DECLARED: both parties of a fight take their band (a felled
#: attacker dies; each kind's Event carries only its earners' changes), so the first season's deaths and deposits move at all
#: three seeds (`acts` 596 / 621 / 650 -> 590 / 620 / 651, `log` 9760 / 11149 / 10728 -> 9338 / 11060 / 10125, `persons`
#: 80 / 81 / 82 -> 77 / 81 / 81). Was, for seeds 0 / 1 / 2: `old` bc4d8440... / d5b68b41... / 3168fab6..., `new` ebe18510... /
#: 507a9bed... / c38c332d..., `census` bd2b200c... / 54df699b... / b34f3210.... CONTROL: the pre-item tree (`68767e731`) is the
#: tree this block was green on. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
#: RE-RECORDED AGAIN at v10 CP-T02-03 (B10-09), A BEHAVIOUR MOVE DECLARED: a `rung` goal whose rung its org's member governs is met
#: (`world_q.aim_state`) and forms no `need` (`goal_varfell_oastad_gate`, met at build, is the one shipped case), so the first season
#: moves at all three seeds (`acts` 590 / 620 / 651 -> 589 / 628 / 637, `log` 9338 / 11060 / 10125 -> 9154 / 11338 / 9817, `persons`
#: 77 / 81 / 81 -> 76 / 81 / 81). Was, for seeds 0 / 1 / 2: `old` 3c66f569... / 2fed7c77... / dd9b3a2a..., `new` 921de777... /
#: 2453fa53... / 9c7fdb69..., `census` 04e36dfe... / 3e1bbbef... / 8ba7fe46.... CONTROL, run in process on this tree: `aim_state` reading
#: `open` always (`AIM_RULES` cleared) reads the values this block held exactly, at all three seeds. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
#: CP-T02-05 (B10-09) added a stamp, `world_q.oughts_named`, and B10-09 close one REVERTED it (falsified on HR-9 control (4),
#: `Falsified: CP-T02-05`): the pins below are the reading with the stamp reverted; the build is equal throughout.
#: RE-RECORDED AGAIN at v10 IN-61 (B10-09), A DATA MOVE DECLARED: `off_king` `conferral` `null` -> `inheritance`, `off_heir` `null` ->
#: `appointed` (RS-27); `Office.conferral` folds into both digests, so `old` and `new` move at all three seeds and NOTHING ELSE DOES
#: (`acts`, `census` and every count equal). Was, for seeds 0 / 1 / 2: `old` 76409cd0... / f5081f07... / 25fe49f5..., `new`
#: f699c1d4... / 5c577efd... / 5f914de5.... CONTROL, run in process on this tree: the two seats' `conferral` set back to `None` on the
#: built world reads the old two-season realm hashes exactly at seeds 0-2. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
#: RE-RECORDED AGAIN at B10-09 close one (D2 + D3, then the CP-T02-05 revert), A BEHAVIOUR MOVE DECLARED: a felled attacker's own
#: `person.died` is placed where he fell (`world_q.event_place`), and a second `commit` on a held cause is declined person-side
#: (`rosters.yaml: held_edge_declines`); the `oughts_named` stamp is reverted, so this is the reading with the stamp reverted (`acts`
#: 589 / 628 / 637, equal to CP-T02-03's, `log` 9154 / 11338 / 9817 -> 9172 / 11338 / 9831). Was, for seeds 0 / 1 / 2:
#: `acts` 582 / 617 / 645, `old` 5675a99d... / 31188d9f... / ed1009cd..., `new` 76340255... / c7c14a9f... / e149edb1..., `census` 93eb8633... /
#: 67cda841... / 149c94a4.... CONTROL, run in process on the pre-revert tree (`f28c3f33c`): `oughts_named` stubbed to `()` reads the
#: two-season realm hash this block's tree reads, at seeds 0-2. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-RECORDED at ED-IN-0310 (`build_realm`'s `foreign` default True; Jordan, 2026-11-04): the Altonian cast adds persons, rungs and two offices, so
# every seed's hashes, act count, census and counts move. CONTROL, run in process on this tree: `build_realm(seed, foreign=False)` reads the
# previous literal below exactly at seeds 0-2 (old/new digests, acts, census, counts). Was seed 0 (one season): old 8504cdb7... / new 53469c5c..., 589 acts.
# RE-RECORDED at CR-10 (B10-09 close two, arm D2), A BEHAVIOUR MOVE DECLARED: `attention_key` spares a tier-1 own-act echo (A1-05), so the
# first season moves at all three seeds (`acts` 601 / 637 / 647 -> 623 / 672 / 655, `log` 9929 / 11758 / 10703 -> 9739 / 13356 / 10585, `persons`
# 76 / 81 / 81 -> 78 / 81 / 81). Was, for seeds 0 / 1 / 2: `old` d04a69b6... / 8d64280c... / 1c7ab31a..., `new` 5e4d77d3... / 0cfcf7ec... /
# 9fef90dd..., `census` 1268c806... / af7e633b... / 2f6133ea.... CONTROL, run in process on this tree: the tier-1 branch returning tier 4
# for an own-act claim (the every-tier screen) reads the seed-0 values this block held (via `test_season_weather`'s pins); the build is
# equal. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-RECORDED at v11 CR-28 (B10-09 close two; CP-T02-05's re-take), A BEHAVIOUR MOVE DECLARED: `questions_for` stamps the Propositions a
# person heard of from another (`world_q.propositions_heard`), so the first season moves at all three seeds (`acts` 623 / 672 / 655 ->
# 623 / 672 / 661, `log` 9739 / 13356 / 10585 -> 9741 / 12874 / 10699). Was, for seeds 0 / 1 / 2: `old` 3a3c84a9... / 910d2cf9... /
# f8077b2c..., `new` a2ff6dfe... / f5b9467f... / 762d314d..., `census` cc0a91a7... / af62fcd4... / 5c15e2da.... CONTROL, run in process
# on this tree: `propositions_heard` stubbed to `()` reads the seed-0 values this block held (via `test_season_weather`'s pins) and
# CR-10's two-season hashes at seeds 0-2; the build is equal. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v11 CR-81 (ED-IN-0318), A DATA MOVE AND A TRAJECTORY MOVE DECLARED: `build_realm` writes the starting
# acquaintances, so every seed's one-season world moves (`acts` 623 / 672 / 661 -> 630 / 662 / 663, `log` 9741 / 12874 / 10699
# -> 10847 / 13169 / 12201). Was, for seeds 0 / 1 / 2: `old` 8d5c403e... / e699f507... / 1dadbb92..., `new` 1f573c4c... /
# ea12c800... / 96763a69..., `census` f9114b10... / be1e3ddb... / 9c425d11.... CONTROL, run in process on this tree: every
# `build_realm` forced to `acquaintances=False` reads the old block exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-RECORDED at v11 CR-25 (B10-09 close two), A BEHAVIOUR MOVE DECLARED: a computed `establish` founds an office over a
# holding (`establish` gains `referent_class: Rung`, `questions_for` stamps `holdings_to_found`), so every seed's first
# season moves (`acts` 630 / 662 / 663 -> 619 / 659 / 658, `log` 10847 / 13169 / 12201 -> 10316 / 13121 / 12898; seed 0
# founds one office in the first season, `offices` 34 -> 35). Was, for seeds 0 / 1 / 2: `old` b72b5582... /
# f0572c69... / d5d3073b..., `new` 5fece5d9... / 19f10a6d... / 5a1f42dc..., `census` 97494bcc... / 299fe1f4... / 7234ba8a....
# CONTROL, run in process on this tree: `holdings_to_found` stubbed to `()` AND `establish`'s `referent_class` dropped reads the
# old block exactly at seeds 0-2 (the term alone stubbed does NOT: the column moves formation by itself). A GOLDEN
# RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v11 CR-82 (B10-09 close two, ED-IN-0319), A FIXTURE MOVE DECLARED: `ledger_cap` 200 -> 3200, so a realm
# ledger that reached the cap in season 1 now keeps what it evicted. Was, seeds 0/1/2: old 3ea197ac... / 1c06b375... /
# b8925f0e..., new f47dfa8c... / 472f71c9... / 06324657..., census f27fea77... / 38076abd... / e4fd0348...; acts 619/659/658
# -> 619/657/658; log 10316/13121/12898 -> 10316/13085/12898 (seed 1 alone moves its acts and log in season 1). CONTROL,
# run in process on this tree: the cap swept back to 200 after `build_realm` reads the old three entries exactly, every
# field. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v11 CR-17 (B10-09 close two), TWO BEHAVIOUR MOVES DECLARED: commit 1 ships `Fixtures odds_weighting` `believed` (H-248)
# and commit 2 re-derives `choice_temperature` 0.1 -> 0.05 (H-96). AT COMMIT 1 ALONE (measured on a scratch harness) seed 0 reads
# the block below it held exactly, seed 1 moves (`new` 1081dd4f... -> f9ac3028..., `acts` 657 -> 658, `log` 13085 -> 13083) and seed 2
# reads the old block. AT COMMIT 2 all three seeds move: for seeds 0 / 1 / 2 `acts` 619 / 657 / 658 -> 685 / 673 / 715, `log`
# 10316 / 13085 / 12898 -> 11775 / 10540 / 10566, `persons` 79 / 80 / 80 -> 77 / 80 / 80, and seed 0's `offices` 35 -> 34: CR-25's season-1 founding no longer
# occurs on seed 0 at tau 0.05, so no realm run shows a computed `establish` executing at HEAD (CR-25's falsifier is the
# hand-built world). Was, for seeds 0 / 1 / 2: `old` e700e9ef... /
# 4f06a8fe... / 8f4851b1..., `new` bdff0832... / 1081dd4f... / 37db6d14..., `census` bdce26ba... / 264d73dd... / b60a0405....
# CONTROL, run in process on this tree: `odds_weighting` swept to `none` and `choice_temperature` to 0.1 reads the old three
# entries' `new`, `acts` and `log` at seeds 0 / 1 / 2 (bdff0832... / 1081dd4f... / 37db6d14...; 619 / 657 / 658; 10316 / 13085 /
# 12898). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-RECORDED at v11 CR-86 (ED-IN-0342, a declared MOVER of every world hash: Valorsmark a faction and `fac_crown` ->
# `fac_valorsmark`, the Duchess's and the Duke's sworn `oblige` to `off_king`, the head seats). Was, for seeds 0 / 1 / 2: `old`
# 5250cd3f... / 0458835b... / 0a3e374e..., `new` 4761e5ca... / 033474f7... / 3217d743..., `census` e3e7b893... / 26d2bc88... /
# 395fe953..., `tenures` 989 / 1002 / 1003, `log` 11775 / 10540 / 10566; `acts` do not move (685 / 673 / 715).
# CONTROL, run in process on this tree at seed 0: the two vassals' obligees dropped read the old `log` (11775) and event digest.
# RE-RECORDED at v10 REM-31 (IN-46), A DECLARED MOVER: `the body` carries `march`'s `step: ENCOUNTER` / `declares: Declared`,
# so every fight is declared at RESOLVE and fought at ENCOUNTER. Was, for seeds 0 / 1 / 2: `old` da44a46a... / 4e5791b2... /
# 0f9fd8c4..., `new` 87b9d1f1... / 86ebc984... / 888a08cb..., `census` 64681b46... / 54968fb4... / 041e9f1d...; `acts` 685 / 673 /
# 715 -> 700 / 688 / 724, `log` 11793 / 10566 / 10584 -> 11846 / 10680 / 10614. CONTROL, run in process on this tree: `the body`'s
# `step:`/`declares:` popped reads the old three entries exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-RECORDED at v10 REM-30's `verb_capability` rows (`argue`, `inquiry`), A DECLARED MOVER: `train` forms one Candidate per
# vocation (`copying`, `argue`, `inquiry`) and `train`'s act id carries the vocation (`data/verbs.py::act_key`). Was, for seeds
# 0 / 1 / 2: `old` 781957cb... / 1e262e0e... / 8f438d3c..., `new` 36378f25... / 8899cdd5... / 048a326b..., `census` dc481e4e... /
# fced32bd... / a489798b..., `acts` 700 / 688 / 724 -> 705 / 697 / 730, `persons` 77 / 80 / 80 -> 79 / 80 / 81, `log` 11846 /
# 10680 / 10614 -> 11581 / 10739 / 10985. CONTROL: the rows commit's four files reverted reads the old three entries exactly
# (the file's tests, run on the parent tree). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v10 CR-30's commit for CR-20 + CR-30 TOGETHER (`Person.attributes`, `Person.heritage`: two new fields in every
# Person's repr, and four authored `heritage:` cast rows, which change the `marks` term of the `seen` claims their co-located
# witnesses hold). Was, for seeds 0 / 1 / 2: `old` 4ace8831... / 65f3ee2b... / fcbfc95b..., `new` 027c7516... / 5b000930... /
# 891860d4...; `acts`, `census` and `counts` do NOT move (705 / 697 / 730, the same census digests and log lengths). CONTROL: the
# ordered (kind, id) event list over two seasons equals the parent tree's at seeds 0 / 1 / 2 both with the four `heritage:` rows
# removed (the ledgers' claim values equal too) and with them present (only the `marks` of `seen` claims differ, 158 / 143 / 124
# of them) -- so only the repr-derived hashes move. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v10 CR-33 (the 34 lifepaths as creation templates), A DECLARED MOVER by ONE person: the registry authors four
# `lifepath:` keys, three that map to no capability key (NPC-002, NPC-005, NPC-080) and NPC-088's `3-CF4`, which holds `inquiry` at
# `pool_default`, so Carin Vedel's `Person.capability` repr is no longer empty. Was, for seeds 0 / 1 / 2: `old` bf061eff... /
# cad429d9... / 10959592..., `new` f2e5e265... / 0d25717b... / 05f065f4...; `acts`, `census` and `counts` do NOT move. CONTROL, run
# in process on this tree: `data/cast.py::capability_of` stubbed to `{}` reads the old `new` three exactly, and the ordered
# (kind, id) event list over one season equals the parent tree's (`d5358a9a`) at seeds 0 / 1 / 2 (11581 / 10739 / 10985 events).
# A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v10 CP-T03-01 (the `individual` conjunct on `fight`/`accept`): the only `old`/`new` movers. `Event.observed` is hashed and every
# `fight`/`accept` that clears `exists`/`with` now records `individual:<actor>` reads (28 / 24 / 18 at one season). Was, for seeds 0 / 1 / 2: `old`
# 65f9e76f... / cbbb8e0d... / b7960661..., `new` 69783660... / d81d7a73... / 9ab1a749.... `acts`, `census` and `counts` do NOT move. CONTROL: with those
# reads left off `observed` (a scratch switch) the old three `new` values read exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v10 CP-T03-09 (`capture`), A DECLARED MOVER of every realm: the row forms for the seats granting `dispatch` (26 of 34 live
# holds on `build_realm(0)`), so persons choose it and the act mix, the log and the hash move. Was, for seeds 0 / 1 / 2: `old` 31619119... /
# 63a729de... / 1a8a1088..., `new` 71ff6e92... / 73af0d1e... / 011a4605...; `acts` 705 / 697 / 730; `tenures` 997 / 1004 / 1014 (seeds 0, 1);
# `log` 11581 / 10739 / 10985. `build_realm(seed)` itself does not move (the row is chosen in play: 837d0f83... below stands). CONTROL, run in
# process on this tree: `capture` withheld from `populated.resolvable_verbs` reads the old `new` three exactly (71ff6e92... / 73af0d1e... /
# 011a4605...). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v10 PC-10b (a challenge is a Record; `accept` binds to one), A DECLARED MOVER wherever a challenge forms: every
# `challenge` mints a `challenge` Record and its maker's `hold`, and `accept` forms only on a `Record`-classed referent. `build_realm(seed)`
# does not move (837d0f83... below stands). Was, for seeds 0 / 1 / 2: `old` 020f6611... / a7ed3e98... / 53eb44c0..., `new` 009f9f31... /
# daca4682... / db5bd6f0...; `acts` 703 / 695 / 731; `records` 183 / 194 / 186; `log` 11585 / 10764 / 10582. CONTROL: the base tree
# (`95f58adb`'s `engine/season`) reads the old three exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CR-87 (violence made exceptional), A DECLARED MOVER of every season that fought and of the build: the
# build-time loyalty row names the creed, never its head, at no lower than -1 (`build_realm(seed)` moves: 837d0f83... ->
# 7266f56b...), and `fight` forms only in a held context, so the 1-season realm keeps the persons the fights felled (80 -> 83).
# Was, for seeds 0 / 1 / 2: `old` a0944c1b... / d52e342d... / e6f01019..., `new` 0fb73bc8... / 3b407a74... / 47151656...;
# `acts` 719 / 721 / 740; `persons` 80 at each. CONTROL: `tests/test_cr87_violence_contexts.py::revert_cr87` reads the old
# build and one-season hashes exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CR-85 (`faculty` replaces `history` in combat's pool and Ob, ED-IN-0330; every season fight
# rolls pool 8 against Ob 1.0, was 9 against 1.5): seed 1 was `old` 18de0fa6... / `new` f89ea45d... (`acts`,
# `census`, `counts` unmoved); seeds 0 and 2 do not move (seed 0 fights nothing, seed 2's fights land where they
# did). CONTROL: `test_cr85_faculty_replaces_history.py::revert_cr85` (the seam's faculty at 3 for every party) reads
# the old value exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CP-T03-04 (`arms` in `verb_capability`'s range: a FORMATION mover even at control, one more `train`
# Candidate per `train` formation with nobody holding the key; no roll moves). Was, for seeds 0 / 1 / 2: `old` 7e81a2cf... /
# ec800435... / ecc848ea..., `new` 20accb03... / 6e25b047... / fe9032ed...; `acts` 744 / 746 / 746; the census and counts in
# each row's trailing comment. `build_realm(seed)` does not move (7266f56b... stands). CONTROL:
# `test_cp_t03_04_arms.py::revert_cp_t03_04` (the three roster rows and the vocation off) reads the old three `new` values
# exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CP-T03-07 (`Person.body_ceiling`: a SCHEMA mover of every Person, so both the `repr` digest and the
# canonical one move at build and at every season; and the lasting mark, an outcome mover where a survivor reached the deepest
# gate -- one person at seed 2, whose body and ceiling moved and nothing else: `acts`, `census` and `counts` do NOT move at any
# seed). Was, for seeds 0 / 1 / 2: `old` 42847586... / 7e8ccabe... / 6c3fdfa0..., `new` b2dde1fc... / 07634b99... / 1cc4370d...;
# and the build pins in the test below, each with its `was`. CONTROL: `test_cp_t03_07_body_ceiling.py::revert_cp_t03_07`
# (`body_mark_model: none` and the field out of the canonical encoding) reads the old three `new` values and the old build
# `7266f56b...` exactly; the `repr` digest has no in-process revert (a dataclass `repr` carries every field). A GOLDEN
# RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CP-T03-08 (`tend` declares `referent_class: Person` and `wounded_with` stamps the wounded: a
# FORMATION mover of every season and an outcome mover -- a man below his ceiling tends himself whole; `acts`, `census`
# and `counts` move at every seed). Was, for seeds 0 / 1 / 2: `old` 92e19ffc... / 6cffb790... / aa306a67..., `new`
# eb2919ae... / fc3201f3... / 6da144ff..., `acts` 744 / 747 / 747, census f970d2ed... / 3b1d0142... / 015989bc..., `log`
# 13401 / 11767 / 11344. The build pins do not move (the item writes no field). CONTROL:
# `test_cp_t03_08_tend_on_the_wounded.py::revert_cp_t03_08` reads the old three `new` values exactly. A GOLDEN RE-RECORDED,
# NOT A BALANCE CLAIM.
BASE = {
    0: {"old": "942102ac04efcbc0ee8fb7f612ea7afb", "new": "d4c83c8ca9d5082f5237a3889e1a995b", "acts": 755,   # CP-T03-08: was 92e19ffc... / eb2919ae... / 744 / census f970d2ed... / records 202 / propositions 144 / tenures 1029 / log 13401. CP-T03-07: was 42847586... / b2dde1fc.... CP-T03-04: was 7e81a2cf... / 20accb03... / census 6032506e... / records 203 / propositions 143 / tenures 1028 / log 13400
        "census": "4cfb3efe1ad9455df9822760145226d1272e9da33efcf5a4f5925fe1598bcc3a",
        "counts": {"persons": 83, "rungs": 414, "offices": 34, "sites": 322, "records": 198, "propositions": 143, "dates": 5, "docket": 8, "tenures": 1024, "log": 13454}},
    1: {"old": "9538a881076b42112dbf5e05e43b4086", "new": "7cacc76327c222c2595c57f24d147d36", "acts": 754,   # B10-11b pin commit (PC-20 (1), the head-weighted strike impact, `K_STR_HEAD`; reading @4b334f2a): was 3caed4cc... / d9f3be70... / census 09f11a01... / log 11937; `acts` and the other counts do not move. CP-T03-08: was 6cffb790... / fc3201f3... / 747 / census 3b1d0142... / records 210 / propositions 146 / docket 9 / tenures 1022 / log 11767. CP-T03-07: was 7e8ccabe... / 07634b99.... CP-T03-04: was ec800435... / 6e25b047... / 746 / census 6282d017... / records 212 / propositions 145 / log 12273. CR-85 (faculty replaces history): was 18de0fa6... / f89ea45d...; `acts`, `census` and `counts` do not move. CP-T03-02 (a fight's `ending` + body Observation): was 327bac57... / f4330aac... / census 321d2548... / log 12271
        "census": "8256042d0c03e1c81da486a995219d636e155b9b2435eb23b92d5f01b97a5277",
        "counts": {"persons": 83, "rungs": 414, "offices": 34, "sites": 322, "records": 205, "propositions": 141, "dates": 5, "docket": 10, "tenures": 1011, "log": 11955}},
    2: {"old": "a1bc123599d8e2407aac94dcbc9037bb", "new": "447ed0d819b895fd828e4b1c26a34e69", "acts": 757,   # B10-11b pin commit (PC-20 (1), the head-weighted strike impact, `K_STR_HEAD`; reading @4b334f2a): was bb2336b4... / 285fb92a...; `acts`, `census` and `counts` do not move. CP-T03-08: was aa306a67... / 6da144ff... / 747 / census 015989bc... / records 183 / propositions 139 / tenures 984 / log 11344. CP-T03-07: was 6c3fdfa0... / 1cc4370d.... CP-T03-04: was ecc848ea... / fe9032ed... / 746 / census 49f45000... / propositions 141 / docket 8 / tenures 988 / log 11340. CP-T03-02: was 4fb68bcf... / a030141a... / census 414d3ac0... / log 11338; CR-87: was e6f01019... / 47151656... / 740
        "census": "ab2d3aa73d60479bb651435ea3bbe7b03298b9d17f8a94776ce5d6521d4bf902",
        "counts": {"persons": 83, "rungs": 414, "offices": 34, "sites": 322, "records": 179, "propositions": 138, "dates": 5, "docket": 7, "tenures": 981, "log": 11398}},
}


def test_go07_control_the_build_world_old_digest_is_unmoved():
    """The base commit's `repr` digest of `build_realm(0)`, before a single act, read this literal
    (`test_season_weather.BASE_HASHES[0]`'s retired value); the same world now reads the new pin."""
    w = POP.build_realm(0)
    c = POP.build_realm(0, foreign=False, acquaintances=False)   # ED-IN-0310 + CR-81: the realm before the empire and the acquaintances
    assert (_old_content_hash(c), c.content_hash()) == ("a2b12c0d640dd015504b2e622c2ae07b", "e9ec044a5bf7248449fef9e8a28c0896")   # CP-T03-07 (`body_ceiling`, a Person field): was d7b1bb37... / e9611b77...; CR-87 (loyalty toward the creed): was 1808a6f0... / 6717d2d1...; CR-33 verify pass (NPC-004's `lifepath: 3-CH5` holds `inquiry`, a Person repr): was 1dd20ec5... / dfdbd5df...; CR-33 (NPC-088 holds `inquiry`): was b016e338... / a4998422... (CR-20+CR-30: was 970d0b5b... / 060d8901... (CR-86: was 919faacb... / c7ca8d50...)
    a = POP.build_realm(0, acquaintances=False)                  # CR-81's control arm: the parent tree's build
    assert (_old_content_hash(a), a.content_hash()) == ("0bfaf18815fedddcfc55b754329a9255", "b9928b271a022bb49e4a743859bcb386")   # CP-T03-07: was 1f53bc11... / e6a40e18...; CR-87: was f37a51c3... / 7a9778bc...; CR-33 verify pass (NPC-004's `lifepath: 3-CH5` holds `inquiry`, a Person repr): was 024abccb... / bfee1369...; CR-33: was d4be83d2... / 070b68df... (CR-20+CR-30: was be420f67... / 87682033... (CR-86: was f78bcaf4... / 70ea49cb...)
    f = POP.build_realm(0, foreign=False)                        # CR-81: was 919faacb... / c7ca8d50... (acquaintances off reads it)
    assert (_old_content_hash(f), f.content_hash()) == ("eac2356d678fa882b0e919fc37e67f98", "69dbd3be3b7b0067baffbb2eff10b8fd")   # CP-T03-07: was e5e7812b... / 2c9b523d...; CR-87: was 622e0736... / ccabd3be...; CR-33 verify pass (NPC-004's `lifepath: 3-CH5` holds `inquiry`, a Person repr): was d1ecf597... / 0b43b49c...; CR-33: was f1c15230... / ebd5e067... (CR-20+CR-30: was a7628b4e... / 7b7992f7... (CR-86: was 42f55a5f... / e12a710b...)
    assert _old_content_hash(w) == "02997e750e3652605a9872e910d978b3"   # CP-T03-07: was 8018a699...; CR-87: was 3a7025a9...; CR-33 verify pass (NPC-004's `lifepath: 3-CH5` holds `inquiry`, a Person repr): was 42b898c4...; CR-33: was ff134c63... (CR-20+CR-30: was da08203b... CR-86: was 47c172b0... (ED-IN-0342). CR-81: was f78bcaf4... (acquaintances=False reads it); ED-IN-0310: was 919faacb...; v10 IN-61: was 26c255ac...
    assert w.content_hash() == "600d8b27147478e158553552cc1409a5"   # CP-T03-07 (`body_ceiling`; `revert_cp_t03_07` reads the old): was 7266f56b...; CR-87: was 837d0f83...; CR-33 verify pass (NPC-004's `lifepath: 3-CH5` holds `inquiry`, a Person repr): was 6ad7b832...; CR-33: was d61848d3... (CR-20+CR-30: was b4bc2df0... CR-86: was 3ae970a1... (ED-IN-0342). CR-81: was 70ea49cb... (acquaintances=False reads it); v10 IN-61: was 4ab812ba... (CP-T02-02); before that 3e31638e... (CR-21)


def test_go07_control_the_world_did_not_move_only_its_digest(monkeypatch):
    from .test_strife_credit import revert_cr79
    revert_cr79(monkeypatch)
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
