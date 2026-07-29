"""ED-PC-0042 (rider I3) — SHAPE HYGIENE guards for the mode-selection (`sel_*`) records.

Two defects, both from the 2026-07-23 wiring audit §4.4 ("shape divergence"), both mechanical and byte-identical:

(a) The `sel_*` bundle was a BARE POSITIONAL TUPLE that widened three times as the model grew — `element_afforded`
    emitted 5 fields, or 7 for `cut_thrust`; `afforded_heads` normalised to 8; `select_mode` returned 6 in a
    DIFFERENT order. Every consumer therefore carried its own index arithmetic *plus width guards*
    (`heads[hd][6] if len(heads[hd])>6 else None`), and ED-PC-0037.1 had to APPEND the per-arm magnitudes AFTER
    `element_ref` rather than beside the other magnitudes, because inserting a field would have silently transposed
    every reader. That is the positional fragility `core.strike` was made a KEYWORD chokepoint to eliminate ("the
    9-arg positional surface — the transposition-bug class — exists in exactly one place"), re-grown one field at a
    time. Fixed by naming the two records (`combat_systems.HeadOption` / `combat_systems.ModeSelection`).

(b) `point_concentration` was read through TWO parallel paths — the raw authored `w['geometry'][...]` and the baked
    `geo[...]`. They cannot disagree today (`geometry.bake` passes the raw primitives through verbatim, at import,
    and nothing constructs or mutates a weapon record at runtime), which is exactly why the split was survivable
    long enough to spread to six sites. Fixed by routing every whole-weapon read through the baked surface, which
    `bake`'s own docstring already nominates as "the single complete surface".

WHAT THESE TESTS ARE FOR. The refactor itself is proven byte-identical by the goldens and the rest of the suite.
These are the RECURRENCE guards (CLAUDE.md §0.1 #5: "if you cannot write the guard you have not understood the
pattern") — they fail when a NEW positional read, a NEW width guard, or a SECOND `point_concentration` path is
introduced, which is the only way this defect class comes back. Mutation-verified: see the docstring of each guard
for the exact mutation that turns it red. ONE MORE BLIND SPOT beyond the list above (adversarial review,
2026-07-29): the binding tracker handles `ast.Assign` only — a record bound through a FOR-LOOP TARGET with a
non-seeded name (`for tok, rec in afforded_heads(w).items(): rec[0]`) escapes the scan entirely; the current
code's loop names happen to be seeded. The semantic pins (uniform width, field order) still hold regardless —
this file's AST layer covers the spellings that exist, not all futures.

BLIND SPOTS, stated plainly:
  · The AST guards read the ENGINE SOURCE ONLY. Tests are deliberately exempt — a test that unpacks
    `select_mode`'s six-tuple positionally is PINNING the wire contract, which is its job.
  · They match syntax, not semantics: `getattr(rec, '_' + str(i))`, `operator.itemgetter(3)`, or a positional read
    laundered through a container/comprehension the checker cannot resolve would all pass. That is the standing
    grep-blind-spot tax (§0.1 #5); the field-order and tuple-compatibility pins below are the semantic half that
    does not depend on reading the source at all. The alias-resolution itself is only as good as `_bound_names`:
    mutation testing found it initially blind to a record bound through `<map>.get(key)` (mutant M3 survived), so
    that arm is now covered AND exercised by `test_the_guard_can_see_the_defect_it_excludes` — but an alias reached
    some third way (a helper's return value, a dict/list of records) would still slip through.
  · `test_baked_geometry_is_a_verbatim_passthrough` proves the two paths AGREE across the live roster; it cannot
    prove they must. If `bake` ever derives (rather than copies) a raw primitive, that test goes red — which is the
    intended signal, not a false alarm.
"""
import ast
import json
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                      'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
from config import CFG  # noqa: E402

# The functions whose result IS a sel_* record, vs those that return a token->record MAP. The distinction matters:
# `len(heads)` (how many modes are afforded) is legitimate; `len(heads[h])` (how wide is the record) is the defect.
_RECORD_PRODUCERS = ('select_mode',)
_MAP_PRODUCERS = ('afforded_heads', 'element_afforded')
# Locals inside combat_systems that hold a record, and those that hold a map of records.
_RECORD_LOCALS = ('vals', 'opt', 'sel', '_sel')
_MAP_LOCALS = ('heads',)
# The engine modules that CONSUME the records (weapons.py/geometry.py are the build side and hold no consumers).
_CONSUMER_MODULES = ('combat_systems.py', 'wrapper.py', 'core.py', 'capabilities.py', 'weapon_physics.py')

# The raw geometric primitives `geometry.bake` passes through untouched. Reading any of these off `['geometry']`
# rather than off the baked `['geo']` surface re-opens defect (b).
_PASSTHROUGH_KEYS = ('curvature', 'point_concentration', 'cross_section', 'edge_keenness', 'strike_concentration')


def _tree(fname):
    path = os.path.join(ENGINE, fname)
    with open(path, encoding='utf-8') as fh:
        src = fh.read()
    return ast.parse(src, filename=path), src


def _called_name(node):
    if not isinstance(node, ast.Call):
        return None
    f = node.func
    return f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else None)


def _is_map_expr(node, maps):
    """Does `node` evaluate to a token -> record MAP? (`len()` of one is legitimate: it counts afforded modes.)"""
    if _called_name(node) in _MAP_PRODUCERS:
        return True
    return isinstance(node, ast.Name) and node.id in maps


def _is_record_expr(node, recs, maps):
    """Does `node` evaluate to a single sel_* record?"""
    if _called_name(node) in _RECORD_PRODUCERS:
        return True
    if isinstance(node, ast.Name) and node.id in recs:
        return True
    # `heads[tok]` / `afforded_heads(w)[tok]` — a subscript of a record MAP is itself a record.
    if isinstance(node, ast.Subscript):
        return _is_map_expr(node.value, maps)
    # `heads.get(tok)` / `afforded_heads(w).get(head)` — the same lookup spelled as a method. This arm exists
    # because leaving it out let a real mutant live: `selected_arm_magnitudes` binds its record through `.get`,
    # so the M3 mutant (`(h[6], h[7]) if ... len(h) > 7`) survived the first version of this checker.
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'get'
            and _is_map_expr(node.func.value, maps)):
        return True
    return False


def _bound_names(tree):
    """(record-valued names, map-valued names) — the declared locals, plus anything assigned from a producer call
    or from a record lookup. Iterated to a fixed point so a chain (`heads = afforded_heads(w)`; `h = heads.get(k)`)
    resolves regardless of statement order."""
    recs, maps = set(_RECORD_LOCALS), set(_MAP_LOCALS)
    for _ in range(8):
        before = (len(recs), len(maps))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign):
                continue
            targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if not targets:
                continue
            called = _called_name(node.value)
            if called in _MAP_PRODUCERS or _is_map_expr(node.value, maps):
                maps.update(targets)
            elif _is_record_expr(node.value, recs, maps):
                recs.update(targets)
        if (len(recs), len(maps)) == before:
            break
    return recs, maps


def _positional_reads(fname):
    """Every `<record>[<int>]` / `<record>[<slice>]` / `len(<record>)` in one engine module."""
    tree, src = _tree(fname)
    recs, maps = _bound_names(tree)
    hits = []
    lines = src.splitlines()
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript) and _is_record_expr(node.value, recs, maps):
            idx = node.slice
            if isinstance(idx, ast.Constant) and isinstance(idx.value, int):
                hits.append((node.lineno, 'int-index', lines[node.lineno - 1].strip()))
            elif isinstance(idx, ast.Slice):
                hits.append((node.lineno, 'slice', lines[node.lineno - 1].strip()))
        elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'len'
              and node.args and _is_record_expr(node.args[0], recs, maps)):
            hits.append((node.lineno, 'len-width-guard', lines[node.lineno - 1].strip()))
    return hits


@pytest.mark.parametrize('module', _CONSUMER_MODULES)
def test_sel_records_are_read_by_name_not_by_index(module):
    """(a) RECURRENCE GUARD. No engine consumer may index a sel_* record positionally, slice it, or branch on its
    len() — those are the three shapes the width-drift took (`heads[hd][3]`, `heads[h][:5]`, `len(vals)>6`).

    MUTATION (verified red): restore any one of the pre-refactor forms, e.g. in `select_mode`
        -        eff=heads[hd].eff,
        +        eff=heads[hd][0],
    or in `afforded_heads`
        -        heads[tok]=opt._replace(element_ref=el.get('element_ref'))
        +        heads[tok]=(opt[0],opt[1],opt[2],opt[3],opt[4],el.get('element_ref'),opt[6],opt[7])
    or in `selected_arm_magnitudes`
        -        return (h.eff_cut, h.eff_thrust) if h is not None else (None, None)
        +        return (h[6], h[7]) if h is not None and len(h) > 7 else (None, None)
    Each is caught, with file/line/source in the failure message.
    """
    hits = _positional_reads(module)
    assert not hits, (
        f"{module}: {len(hits)} positional read(s) of a sel_* record — use the HeadOption/ModeSelection field "
        f"names (ED-PC-0042/I3):\n" + "\n".join(f"  line {ln} [{kind}]: {src}" for ln, kind, src in hits))


def test_the_guard_can_see_the_defect_it_excludes():
    """§0.1 #2 — an assertion must be able to observe the failure it excludes. The guard above is a "no hits" claim,
    which a broken checker satisfies vacuously. This feeds the checker the EXACT pre-refactor source and requires it
    to flag all three shapes, so a checker that silently stops parsing cannot pass as clean."""
    src = (
        "def select_mode(c, armor, cfg):\n"
        "    heads = afforded_heads(c.w)\n"
        "    h = max(heads, key=lambda hd: heads[hd][0])\n"
        "    ct = heads[h][6] if len(heads[h]) > 6 else None\n"
        "    eff, dm, gap, perc, pc = heads[h][:5]\n"
        "    return dm, h, gap, perc, pc, eff\n"
        "def selected_arm_magnitudes(c, head):\n"
        "    opts = afforded_heads(c.w)\n"
        "    h = opts.get(head)\n"                      # the `.get` binding that let mutant M3 survive v1
        "    return (h[6], h[7]) if h is not None and len(h) > 7 else (None, None)\n"
    )
    tree = ast.parse(src)
    recs, maps = _bound_names(tree)
    assert 'heads' in maps                          # seed-sanity only: 'heads' is pre-seeded in _MAP_LOCALS, so this
                                                    # pins the seeding, NOT producer-binding (adversarial review note)
    kinds = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript) and _is_record_expr(node.value, recs, maps):
            if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, int):
                kinds.append('int-index')
            elif isinstance(node.slice, ast.Slice):
                kinds.append('slice')
        elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'len'
              and node.args and _is_record_expr(node.args[0], recs, maps)):
            kinds.append('len-width-guard')
    assert kinds.count('int-index') >= 4, kinds       # heads[hd][0], heads[h][6], h[6], h[7]
    assert 'slice' in kinds, kinds                    # heads[h][:5]
    assert kinds.count('len-width-guard') >= 2, kinds  # len(heads[h]) > 6  and  len(h) > 7 via the `.get` binding
    # and the legitimate `len(<map>)` form must NOT be flagged — the guard's own false-positive control
    ok = ast.parse("heads = afforded_heads(w)\nif len(heads) == 1:\n    pass\n")
    r2, m2 = _bound_names(ok)
    assert not [n for n in ast.walk(ok)
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'len'
                and n.args and _is_record_expr(n.args[0], r2, m2)]


def test_record_field_order_is_pinned():
    """(a) The two orders DIFFER (HeadOption leads with `eff`, ModeSelection with `dm`) and both are load-bearing:
    ModeSelection's order is stored in golden_element_parity.json and unpacked six-wide by ~15 tests; HeadOption's
    is what `_replace`/`.eff_cut` resolve against. Reordering either is a silent, roster-wide transposition, so the
    orders are pinned HERE rather than left to whatever the goldens happen to catch.

    MUTATION (verified red): swap any two field names in either namedtuple declaration."""
    assert S.ModeSelection._fields == ('dm', 'head', 'gap', 'perc', 'pc', 'eff')
    assert S.HeadOption._fields == ('eff', 'dm', 'gap', 'perc', 'pc', 'element_ref', 'eff_cut', 'eff_thrust')
    # the three trailing fields default to None — element_afforded constructs 5-wide for every non-cut_thrust head
    assert S.HeadOption(1.0, 'shear', 0.5, None, 0.6) == (1.0, 'shear', 0.5, None, 0.6, None, None, None)


def test_records_stay_tuple_compatible_on_every_path_the_corpus_uses():
    """(a) The refactor is only byte-identical because a namedtuple IS a tuple. Each assertion below stands for a
    REAL consumer that would break if these records ever became a dataclass/dict:
      · `list(...) == <json list>`      -> test_combat_element_parity.test_select_mode_parity_all_tiers
      · six-way unpack                  -> test_combat_invariants / test_combat_audit_pins (~15 sites)
      · `[1]`, `[:2]`, `[:6]`           -> test_combat_invariants:775, test_combat_thrust_magnitude, capabilities
      · `isinstance(r, tuple)`          -> workbench/catalogue.py:206
      · json array encoding             -> the golden fixture's own regeneration path
    Note `NamedTuple(...) == [list]` is False — but so is `tuple(...) == [list]`, and the parity test converts with
    `list(...)` before comparing, so the comparison SEMANTICS are unchanged. That is asserted, not assumed."""
    sel = S.select_mode(Combatant('x', weapon='poleaxe'), 'heavy', False, CFG)
    assert isinstance(sel, tuple)
    assert len(sel) == 6
    plain = (sel.dm, sel.head, sel.gap, sel.perc, sel.pc, sel.eff)
    assert sel == plain and tuple(sel) == plain
    assert list(sel) == list(plain) == json.loads(json.dumps(sel))
    dm, head, gap, perc, pc, eff = sel                       # the six-way unpack every test uses
    assert (dm, head, gap, perc, pc, eff) == plain
    assert sel[1] == sel.head and sel[:2] == plain[:2]
    # and the same for HeadOption, which the capability/parity tests index
    opt = S.afforded_heads(WEAPONS['poleaxe'])['point']
    assert isinstance(opt, tuple) and len(opt) == 8
    assert opt[0] == opt.eff and opt[:6] == tuple(opt)[:6]
    assert json.loads(json.dumps(opt)) == list(opt)
    # the comparison hazard, pinned explicitly in BOTH directions so the parity path can never drift silently
    assert sel != list(plain)
    assert tuple(plain) != list(plain)


def test_afforded_heads_emits_one_uniform_width():
    """(a) The width guards (`len(vals)>6`, `len(h)>7`) were removable only because every option is now the same
    shape. If a future branch re-introduces a short tuple, the guards are gone and the reads would go wrong
    silently — so the uniformity is asserted directly, across the whole roster and at several grips.

    MUTATION (verified red): emit a bare 5-tuple from any `element_afforded` branch."""
    checked = 0
    for name, w in WEAPONS.items():
        if 'base' in w:
            continue
        for grip, room in ((0.0, 1.0), (0.5, 0.6), (1.0, 0.3)):
            for el in S._mode_elements(w):
                for tok, opt in S.element_afforded(el, w, grip=grip, room=room).items():
                    assert isinstance(opt, S.HeadOption), (name, tok, type(opt))
                    assert len(opt) == 8, (name, tok, len(opt))
                    checked += 1
            for tok, opt in S.afforded_heads(w, grip=grip, room=room).items():
                assert isinstance(opt, S.HeadOption), (name, tok, type(opt))
                assert len(opt) == 8, (name, tok, len(opt))
                checked += 1
    assert checked > 400, f"only {checked} options inspected — the sweep collapsed"   # §0.1 #2: assert that it asserted


# ── (b) point_concentration: ONE read surface ───────────────────────────────────────────────────────────────────

def _raw_geometry_reads(fname):
    """Every `<expr>['geometry'][<passthrough key>]` in one engine module."""
    tree, src = _tree(fname)
    lines = src.splitlines()
    hits = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Constant)
                and node.slice.value in _PASSTHROUGH_KEYS):
            continue
        inner = node.value
        if (isinstance(inner, ast.Subscript) and isinstance(inner.slice, ast.Constant)
                and inner.slice.value == 'geometry'):
            hits.append((node.lineno, node.slice.value, lines[node.lineno - 1].strip()))
    return hits


@pytest.mark.parametrize('module', _CONSUMER_MODULES)
def test_baked_primitives_have_exactly_one_read_surface(module):
    """(b) RECURRENCE GUARD. `geometry.bake` passes the raw primitives through so that `geo` is the single complete
    surface; no engine consumer may reach around it into the authored `['geometry']` dict. (weapons.py and
    geometry.py are the BUILD side — they are not in _CONSUMER_MODULES and are free to read the raw params.)

    MUTATION (verified red): revert any one site, e.g. in `lunge_quality`
        -    pc = w['geo']['point_concentration']
        +    pc = w['geometry']['point_concentration']
    """
    hits = _raw_geometry_reads(module)
    assert not hits, (
        f"{module}: {len(hits)} raw-`['geometry']` read(s) of a baked passthrough primitive — read `w['geo'][...]`, "
        f"the single surface (ED-PC-0042/I3):\n" + "\n".join(f"  line {ln} ({key}): {src}" for ln, key, src in hits))


def test_the_geometry_guard_can_see_the_defect_it_excludes():
    """§0.1 #2 again — feed the checker the exact pre-refactor line and require a hit, so a vacuous pass is
    impossible."""
    tree = ast.parse("pc = sel_pc if sel_pc is not None else w['geometry']['point_concentration']\n")
    found = [n for n in ast.walk(tree)
             if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant)
             and n.slice.value in _PASSTHROUGH_KEYS
             and isinstance(n.value, ast.Subscript) and isinstance(n.value.slice, ast.Constant)
             and n.value.slice.value == 'geometry']
    assert len(found) == 1


def test_baked_geometry_is_a_verbatim_passthrough():
    """(b) The routing above is byte-identical only while `bake` COPIES the raw primitives rather than deriving
    them. Asserted across the whole live roster and every passthrough key, so a `bake` change that starts
    transforming one of them shows up here as a deliberate decision rather than as silent drift in whichever
    consumer happened to read the other path.

    This is also the evidence for the report's claim that the two paths CANNOT disagree today."""
    checked = 0
    for name, w in WEAPONS.items():
        assert 'geo' in w and 'geometry' in w, name
        for key in _PASSTHROUGH_KEYS:
            assert w['geo'][key] == w['geometry'][key], (name, key, w['geo'][key], w['geometry'][key])
            checked += 1
    assert checked == len(WEAPONS) * len(_PASSTHROUGH_KEYS) > 0
    # mode-elements carry ONLY the baked surface (weapons.py pops their raw `geometry` at bake time), so the
    # element path never had a second option in the first place — the split was whole-weapon-only.
    for name, w in WEAPONS.items():
        for i, me in enumerate(w.get('mode_elements', ())):
            assert 'geo' in me and 'geometry' not in me, (name, i, sorted(me))
