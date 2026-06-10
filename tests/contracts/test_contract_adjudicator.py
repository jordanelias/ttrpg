#!/usr/bin/env python3
"""Tests for contract_adjudicator: one pass + one failure case per check
A1-A9, plus wildcard semantics (the seed uses 'da.*', 'scene.*', '*').

Plain asserts; runs under pytest or as a script (python3 test_contract_adjudicator.py).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "skills", "valoria-module-adjudicator",
                                "scripts"))
from contract_adjudicator import adjudicate, _pat_overlap, _wild_registered

REGISTRY = """# Key Type Registry (fixture)

### da.initiated
### da.resolved
### scene.dialogue
### scene.witness
### scene.battle_concluded
### state.scar_acquired
### env.peninsular_strain_shock
### meta.knot_formed
### mechanical.scene_entered

## 9. Summary
| Family | Count |
|---|---|
| **Total** | **9** |
"""

REGISTRY_BAD_TOTAL = REGISTRY.replace("**9**", "**12**")
SOURCES = "  - design_doc: designs/fixture/home_doc_v30.md\n"


def mod(name, **kw):
    base = {"module": name, "doc": None, "scales": ["scene"], "resolver": None,
            "consumes": [], "emits": [], "state": [], "transitions": [],
            "loops": [], "status": "extracted",
            "sources": ["fixture [READ: test]"]}
    base.update(kw)
    return base


def run(*modules, registry=REGISTRY, sources=SOURCES):
    return adjudicate({"modules": list(modules)}, registry, sources)


def hits(prefix, items):
    return [i for i in items if i.startswith(prefix)]


# ── wildcard primitives ─────────────────────────────────────────────────────

def test_pat_overlap():
    assert _pat_overlap("da.initiated", "da.initiated")
    assert not _pat_overlap("da.initiated", "da.resolved")
    assert _pat_overlap("da.*", "da.initiated")
    assert _pat_overlap("da.initiated", "da.*")
    assert _pat_overlap("da.*", "da.*")
    assert not _pat_overlap("da.*", "scene.*")
    assert not _pat_overlap("da.*", "scene.dialogue")
    assert _pat_overlap("*", "da.initiated")
    assert _pat_overlap("scene.*", "*")
    assert not _pat_overlap("", "da.*")


def test_wild_registered():
    reg = {"da.initiated", "scene.dialogue"}
    assert _wild_registered("da.initiated", reg)
    assert _wild_registered("da.*", reg)
    assert not _wild_registered("env.*", reg)
    assert _wild_registered("*", reg)
    assert not _wild_registered("*", set())


# ── A1 schema ───────────────────────────────────────────────────────────────

def test_a1_pass():
    v, _ = run(mod("ok"))
    assert not hits("A1", v)


def test_a1_stub_with_edges_violates():
    v, _ = run({"module": "s", "status": "stub",
                "emits": [{"type": "da.initiated", "terminal": True}]})
    assert hits("A1", v)


def test_a1_bad_bucket_violates_unknown_scale_warns():
    v, w = run(mod("m", scales=["orbital"],
                   state=[{"name": "x", "bucket": "heap", "writable": False}]))
    assert any("bucket" in x for x in hits("A1", v))
    assert any("orbital" in x for x in hits("A1", w))   # warning, not violation
    assert not any("orbital" in x for x in v)


# ── A2 emit-closure ────────────────────────────────────────────────────────

def test_a2_registered_and_inhabited_family_pass():
    v, _ = run(mod("m", emits=[{"type": "da.initiated", "terminal": True},
                               {"type": "da.*", "terminal": True}]))
    assert not hits("A2", v)


def test_a2_unregistered_exact_violates():
    v, _ = run(mod("m", emits=[{"type": "scene.thread_operation",
                                "terminal": True}]))
    assert any("scene.thread_operation" in x for x in hits("A2", v))


def test_a2_empty_family_wildcard_violates():
    v, _ = run(mod("m", emits=[{"type": "ghost.*", "terminal": True}]))
    assert any("ghost.*" in x for x in hits("A2", v))


# ── A3 consume-closure ─────────────────────────────────────────────────────

def test_a3_pass_exact_and_wildcard_wiring():
    prod = mod("prod", emits=[{"type": "da.*", "terminal": False}])
    cons = mod("cons", consumes=[{"type": "da.initiated", "from": ["prod"]},
                                 {"type": "da.*", "from": ["prod"]}])
    v, _ = run(prod, cons)
    assert not hits("A3", v)


def test_a3_producer_not_emitting_violates():
    prod = mod("prod", emits=[{"type": "scene.dialogue", "terminal": False}])
    cons = mod("cons", consumes=[{"type": "da.initiated", "from": ["prod"]}])
    v, _ = run(prod, cons)
    assert any("does not emit" in x for x in hits("A3", v))


def test_a3_unregistered_consume_violates_engine_skips_wiring():
    cons = mod("cons", consumes=[{"type": "ghost.signal", "from": "engine"}])
    v, _ = run(cons)
    a3 = hits("A3", v)
    assert any("ghost.signal" in x for x in a3)          # registry check fires
    assert not any("producer" in x for x in a3)          # engine skips wiring


# ── A4 orphans ─────────────────────────────────────────────────────────────

def test_a4_family_wildcard_consumer_counts():
    prod = mod("prod", emits=[{"type": "scene.dialogue", "terminal": False}])
    cons = mod("cons", consumes=[{"type": "scene.*", "from": ["prod"]}])
    _, w = run(prod, cons)
    assert not hits("A4", w)


def test_a4_global_star_does_not_silence():
    prod = mod("prod", emits=[{"type": "scene.dialogue", "terminal": False}])
    reader = mod("reader", consumes=[{"type": "*", "from": "engine"}])
    _, w = run(prod, reader)
    assert any("scene.dialogue" in x for x in hits("A4", w))


def test_a4_terminal_emission_no_warning():
    prod = mod("prod", emits=[{"type": "scene.dialogue", "terminal": True}])
    _, w = run(prod)
    assert not hits("A4", w)


# ── A5 derived-value write guard ───────────────────────────────────────────

def test_a5():
    ro = mod("ro", state=[{"name": "Mandate", "bucket": "derived_value",
                           "writable": False}])
    rw = mod("rw", state=[{"name": "Mandate", "bucket": "derived_value",
                           "writable": True}])
    v0, _ = run(ro)
    v1, _ = run(rw)
    assert not hits("A5", v0)
    assert any("Mandate" in x for x in hits("A5", v1))


# ── A6 cross-scale transitions ─────────────────────────────────────────────

def test_a6():
    prod = mod("prod", scales=["peninsula"],
               emits=[{"type": "env.peninsular_strain_shock",
                       "terminal": False}])
    cons = mod("cons", scales=["provincial"],
               consumes=[{"type": "env.peninsular_strain_shock",
                          "from": ["prod"]}])
    v, _ = run(prod, cons)
    assert hits("A6", v)
    prod2 = dict(prod, transitions=[{"via": "scale_transitions §3.x"}])
    v2, _ = run(prod2, cons)
    assert not hits("A6", v2)


# ── A7 cycles ──────────────────────────────────────────────────────────────

def test_a7():
    a = mod("a", emits=[{"type": "da.initiated", "terminal": False}],
            consumes=[{"type": "scene.dialogue", "from": ["b"]}])
    b = mod("b", emits=[{"type": "scene.dialogue", "terminal": False}],
            consumes=[{"type": "da.initiated", "from": ["a"]}])
    v, _ = run(a, b)
    assert hits("A7", v)
    a2 = dict(a, loops=[{"with": "b", "damper": "seasonal cap"}])
    v2, _ = run(a2, b)
    assert not hits("A7", v2)


# ── A8 doc anchoring ───────────────────────────────────────────────────────

def test_a8():
    anchored = mod("a", doc="designs/fixture/home_doc_v30.md")
    unanchored = mod("b", doc="designs/fixture/missing_v30.md")
    docless = mod("c", doc=None)                       # has sources -> W-DOC
    ungrounded = mod("d", doc=None, sources=[])        # nothing -> violation
    v, w = run(anchored, unanchored, docless, ungrounded)
    assert not any("[a]" in x for x in hits("A8", v))
    assert any("[b]" in x for x in hits("A8", v))
    assert any("[c]" in x for x in hits("W-DOC", w))
    assert not any("[c]" in x for x in hits("A8", v))
    assert any("[d]" in x for x in hits("A8", v))


# ── A9 registry self-check ─────────────────────────────────────────────────

def test_a9():
    _, w_ok = run(mod("m"))
    assert not [x for x in hits("A9", w_ok) if "drift" in x]
    _, w_bad = run(mod("m"), registry=REGISTRY_BAD_TOTAL)
    assert any("declares 12" in x for x in hits("A9", w_bad))


# ── exit semantics ─────────────────────────────────────────────────────────

def test_clean_contracts_yield_zero_violations():
    prod = mod("prod", doc="designs/fixture/home_doc_v30.md",
               emits=[{"type": "scene.dialogue", "terminal": False}])
    cons = mod("cons", doc="designs/fixture/home_doc_v30.md",
               consumes=[{"type": "scene.dialogue", "from": ["prod"]}])
    v, _ = run(prod, cons)
    assert v == []


if __name__ == "__main__":
    fns = [f for n, f in sorted(globals().items())
           if n.startswith("test_") and callable(f)]
    for f in fns:
        f()
        print(f"PASS {f.__name__}")
    print(f"== {len(fns)} tests passed ==")
