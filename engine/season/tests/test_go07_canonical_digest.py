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
BASE = {
    0: {"old": "b2464a6c87dd9d2da9e3b3cbc8143fdf", "new": "947c190baae2dda4b512d42271f36dd4", "acts": 539,
        "census": "5198ad48b4077e7bcdca144ccf692a296897cb22e2f3a240d655c72aa1302a14",
        "counts": {"persons": 82, "rungs": 411, "offices": 32, "sites": 322, "records": 88,
                   "propositions": 87, "dates": 1, "docket": 5, "tenures": 785, "log": 7018}},
    # SEED 1 RE-RECORDED, ED-IN-0304 phase 4 (`march_target_kinds` gained `territory`): one computed `march` on a
    # territory referent (a Varfell goal's) used to fold to `march.refused` and now resolves `field.unopposed` with
    # `army.arrived`, the realm's first computed arrival. Event kinds of the one season, before -> after: army.arrived
    # 0->1, field.unopposed 0->1, march.declared 9->7, march.refused 9->6, claim.deposited 7005->7001,
    # finding.none 115->116 (the later options shift with the army's new place). Seeds 0 and 2 did not move.
    # Was: old 97d2d92f..., new 36ef9545..., acts 560, tenures 810, log 8128, census 997a5648...
    1: {"old": "38e1c49edf8e6fd2b1a1127d32da07ca", "new": "80df23952bb3364cc1e55e4535c397b4", "acts": 558,
        "census": "1fe9761f2a4d4d981d81d4fe1c25fa7d5ce4e72625ba0761124cdf94572a8b6b",
        "counts": {"persons": 83, "rungs": 412, "offices": 32, "sites": 322, "records": 98,
                   "propositions": 87, "dates": 0, "docket": 2, "tenures": 811, "log": 8122}},
    # SEED 2 RE-RECORDED, same cause: one computed territory march, `march.refused` -> `field.unopposed` +
    # `army.arrived` (army.arrived 0->1, march.declared 3->1, march.refused 3->0), and the season's later choices
    # follow (record.created 43->44, proposition.uttered 24->22, finding.none 102->105, ...).
    # Was: old 455cfe8d..., new 7e8df32a..., acts 588, records 90, propositions 91, tenures 787, log 6879,
    # census b2adbbfe...
    2: {"old": "f6d436a4cca0a7ecc24ea45628cc55ec", "new": "e463df75d5006d310bf216f991d09cee", "acts": 583,
        "census": "4a98cbc721d20e50b70e59ac6064f1644ebc598d92b44e88f111874b2269e8a3",
        "counts": {"persons": 81, "rungs": 410, "offices": 32, "sites": 322, "records": 92,
                   "propositions": 89, "dates": 1, "docket": 2, "tenures": 788, "log": 6877}},
}


def test_go07_control_the_build_world_old_digest_is_unmoved():
    """The base commit's `repr` digest of `build_realm(0)`, before a single act, read this literal
    (`test_season_weather.BASE_HASHES[0]`'s retired value); the same world now reads the new pin."""
    w = POP.build_realm(0)
    assert _old_content_hash(w) == "8e4032a26cfeabdc55bba2178b82d564"
    assert w.content_hash() == "9ff5390939742b7bbb3af0fa2551e958"


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
