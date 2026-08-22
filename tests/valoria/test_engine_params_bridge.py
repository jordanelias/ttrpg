"""THE INVARIANT S5 EXISTS TO REACH, made enforceable (plan S5e, 2026-08-22).

`proposals/2026-08-21-execution-order-v1.md` §2 states the target in a paragraph: an AUTHORED
surface under `references/` is cooked by ONE exporter behind a blocking `--check` into ONE artifact
under `engine/engine_params/`, read by ONE leaf under `engine/substrate/`. Nothing else parses the
authored surface; nothing else reads the artifact.

⚠ THAT SENTENCE IS NOT TRUE OF THE TREE TODAY, AND THIS FILE SAYS SO RATHER THAN ASSERTING IT.
Written as a hard invariant it would be RED ON ARRIVAL — `key_types.json`'s one reader is not a leaf,
`descriptor_registry.yaml` has five parsers, `module_contracts.yaml` has nine — and a gate that is
red on arrival gets deleted by the next session, which loses the check entirely (`CLAUDE.md` §0.2's
"a hard assertion would be red on arrival" is the same reasoning the seam ratchet is built on).

So it splits the claim by what is actually true:

  * ONE WRITER PER ARTIFACT is true today, so it is a HARD assertion. This is the half that matters
    most for the port: two tools writing one cooked file is how the bridge acquires a silent second
    owner and starts drifting.
  * READERS and PARSERS are RATCHETS. Each declared set can only shrink. A new ad-hoc reader of a
    cooked artifact, or a new tool parsing an authored surface directly instead of going through
    the exporter, fails immediately; removing one is banked by editing the map here.

SUBJECT, under `CLAUDE.md` §0.1 pt 5: `engine/engine_params/` is the bridge the Godot port is
generated against and the set of files `engine/` reads AT IMPORT — delete one and the engine does
not start. That is the game, not this repository's process. It scans `tools/` because that is where
the writers live, but its subject is the runtime input, which is the same carve-out
`test_descriptors_runtime.py` and `test_world_initial_state.py` ride (plan §3a: an exporter is a
build step of L0, because its output is a runtime input).

It replaces the retired `single_owner_check.py` for this one surface, and deliberately not for the
tree at large — that generality is what made the old checker apparatus about apparatus.
"""
from __future__ import annotations

import collections
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parents[2]
PARAMS = REPO / 'engine' / 'engine_params'

#: The artifact with NO writer, and why. `params_tables.yaml` is the byte-identical capture of the
#: 43 evacuated `engine/params/*.md` tables; `tools/export_params_constants.py` was a
#: migration-window gate retired WITH its source, so the capture can no longer be regenerated and
#: its "NEVER hand-edit" header is absolute (`CLAUDE.md` §5). It is a runtime input all the same —
#: `dice_engine.py` and `sigma_leverage.py` read it — so it is excluded from the writer rule by
#: name rather than by a predicate that would also excuse a genuinely orphaned artifact.
NO_WRITER = {'params_tables.yaml'}

#: {artifact -> modules under engine/ that BIND its path at runtime}. Measured, not assumed: an
#: earlier draft of this file listed `key_types.json` with three readers and `params_tables.yaml`
#: with two, on the strength of a grep that could not tell a path construction from a docstring
#: mentioning the filename. Four bindings exist in the whole of `engine/`, and three of them are
#: already the target shape.
#:
#: `params_tables.yaml` has NO runtime binding — `dice_engine.py` and `sigma_leverage.py` only cite
#: it in prose — so it is a tracked runtime input with no runtime reader, which is worth knowing
#: and is why it is absent here rather than listed with an empty set.
#:
#: SHRINK-ONLY toward one substrate leaf each.
ENGINE_READERS = {
    'composition.json': {'engine/substrate/composition.py'},
    'descriptors.json': {'engine/substrate/descriptors.py'},
    'world_initial_state.json': {'engine/substrate/world_initial_state.py'},
    # The one that is not a leaf. `echo_transport` builds the path itself and hands it to
    # `TypeRegistry.load`, so the Key vocabulary has one reader but no `engine/substrate/` owner —
    # the shape every other artifact has. Closing it means a `substrate/key_types.py` leaf; that is
    # a real change to the Key substrate's surface and is not folded into this step.
    'key_types.json': {'engine/cross_scale/echo_transport.py'},
}

#: {authored surface -> tools that PARSE it}. SHRINK-ONLY, toward the exporter alone.
#: `world_initial_state.yaml` already conforms and is the worked example of the target state.
#: `module_contracts.yaml` is the furthest away, and legitimately so for now — it is a
#: multi-purpose registry whose `modules:` block predates `composition_roles:` and feeds the
#: generated indexes. Folding those readers is plan step S5c.
AUTHORED_PARSERS = {
    'world_initial_state.yaml': {'tools/export_world_initial_state.py'},
    'descriptor_registry.yaml': {'tools/export_descriptors.py',
                                 'tools/ci_names_consistency.py',
                                 'tools/definitions_store.py',
                                 'tools/quantity_registry.py',
                                 'tools/registry.py'},
    'module_contracts.yaml': {'tools/export_composition.py',
                              'tools/build_contract_index.py',
                              'tools/build_engine_atlas.py',
                              'tools/build_fork.py',
                              'tools/build_key_graph.py',
                              'tools/ci_quantity_vocabulary_check.py',
                              'tools/evacuation_plan.py',
                              'tools/m1_acceptance.py',
                              'tools/trace_execution_phases.py'},
}

_PATHISH = re.compile(r"(os\.path\.join|Path\(|open\(|load_yaml|safe_load|read_text|/ ['\"])")
_OUT_BINDING = re.compile(r"^\s*(?:OUT|OUT_PATH|DEST|TARGET)\s*=.*$", re.M)


def _artifacts():
    return sorted(p.name for p in PARAMS.iterdir() if p.is_file())


def _py(*roots):
    for root in roots:
        for p in sorted((REPO / root).rglob('*.py')):
            rel = p.relative_to(REPO).as_posix()
            if '__pycache__' in rel or '/tests/' in rel or rel.startswith('engine/tests/'):
                continue
            yield rel, p.read_text(encoding='utf-8')


def _writers():
    """A tool WRITES an artifact when it binds it as its output path, or opens it for writing."""
    found = collections.defaultdict(set)
    for rel, txt in _py('tools'):
        for a in _artifacts():
            if a not in txt:
                continue
            if any(a in m.group(0) for m in _OUT_BINDING.finditer(txt)) or \
                    re.search(rf"open\([^)]*{re.escape(a)}[^)]*['\"]w['\"]", txt):
                found[a].add(rel)
    return found


def _readers_under(root, names):
    """Modules under `root` that BIND one of `names` as a path — not ones that mention it.

    The distinction is the whole reliability of this file. A filename appears in docstrings,
    provenance comments and error messages all over the tree; what matters is whether the module
    constructs a path to it. So a line counts only when it holds the name as a STRING LITERAL and
    it, or the line above it, is a path construction. That two-line window is what catches
    `_PATH = (Path(...)\n  / "engine" / "engine_params" / "key_types.json")`.
    """
    found = collections.defaultdict(set)
    for rel, txt in _py(root):
        lines = txt.splitlines()
        for i, ln in enumerate(lines):
            stripped = ln.strip()
            if stripped.startswith('#'):
                continue
            for n in names:
                if f'"{n}"' not in ln and f"'{n}'" not in ln:
                    continue
                context = ' '.join(lines[max(0, i - 1):i + 1])
                if _PATHISH.search(context):
                    found[n].add(rel)
    return found


def test_every_cooked_artifact_has_exactly_one_writer():
    """HARD. Two tools writing one artifact is how the bridge acquires a second owner: each
    regenerates from a different source, the last one to run wins, and `--check` passes for
    whichever ran last. There is no ratchet here because the property holds today."""
    writers = _writers()
    problems = []
    for a in _artifacts():
        w = writers.get(a, set())
        if a in NO_WRITER:
            if w:
                problems.append(f'{a}: declared writer-less but written by {sorted(w)} — if it is '
                                f'regenerable again, delete it from NO_WRITER')
            continue
        if len(w) != 1:
            problems.append(f'{a}: {len(w)} writer(s) {sorted(w) or "(none)"}, expected exactly 1')
    assert not problems, 'engine_params writer defects:\n  ' + '\n  '.join(problems)


def test_the_writer_scan_is_not_vacuous():
    """§0.1 pt 2 — "every artifact has one writer" is also what a scan that finds nothing reports
    for an empty artifact list. Pin that the scan sees the real surface."""
    arts = _artifacts()
    assert len(arts) >= 8, f'only {len(arts)} artifacts found — the walk is broken'
    writers = _writers()
    assert writers.get('composition.json') == {'tools/export_composition.py'}, writers.get('composition.json')
    assert writers.get('world_initial_state.json') == {'tools/export_world_initial_state.py'}


def test_no_new_engine_reader_of_a_cooked_artifact():
    """RATCHET, shrink-only. The target is one leaf under `engine/substrate/` per artifact; what is
    pinned is that the set does not GROW. A module reading a cooked artifact directly instead of
    through its leaf is the ad-hoc-reader decay this whole pattern exists to prevent."""
    actual = _readers_under('engine', list(ENGINE_READERS))
    problems = []
    for a, declared in ENGINE_READERS.items():
        found = actual.get(a, set())
        for extra in sorted(found - declared):
            problems.append(f'{a}: NEW engine reader {extra} — read it through its substrate leaf, '
                            f'or declare it here deliberately with a reason')
        for gone in sorted(declared - found):
            problems.append(f'{a}: {gone} no longer reads it — GOOD, remove it from ENGINE_READERS '
                            f'in this same commit so the progress is banked')
    assert not problems, 'engine_params reader drift:\n  ' + '\n  '.join(problems)


def test_no_new_parser_of_an_authored_surface():
    """RATCHET, shrink-only. Every tool that parses an authored surface directly is a second reader
    of a file the exporter is supposed to own. `world_initial_state.yaml` has exactly one and is
    the worked example; `module_contracts.yaml` has nine and is what S5c is for."""
    actual = _readers_under('tools', list(AUTHORED_PARSERS))
    problems = []
    for src, declared in AUTHORED_PARSERS.items():
        found = actual.get(src, set())
        for extra in sorted(found - declared):
            problems.append(f'{src}: NEW parser {extra} — go through the exporter, or declare it '
                            f'here with a reason')
        for gone in sorted(declared - found):
            problems.append(f'{src}: {gone} no longer parses it — GOOD, remove it from '
                            f'AUTHORED_PARSERS in this same commit')
    assert not problems, 'authored-surface parser drift:\n  ' + '\n  '.join(problems)


def test_the_target_state_is_recorded_as_distance_not_as_a_claim():
    """How far the tree is from §2's paragraph, asserted so it can only close.

    Three of the four runtime bindings are already the target shape — one artifact, one leaf under
    `engine/substrate/`, nothing else. The fourth, `key_types.json`, has exactly ONE reader but that
    reader is `engine/cross_scale/echo_transport.py`, not a leaf: the Key vocabulary is the one
    cooked artifact with no substrate owner. Closing it means adding a `substrate/key_types.py`,
    which changes the Key substrate's public surface and is deliberately not folded into this step.
    """
    multi = {a: sorted(r) for a, r in ENGINE_READERS.items() if len(r) > 1}
    assert not multi, (
        f'an artifact gained a second engine reader: {multi}. One artifact, one reader — a second '
        f'is the ad-hoc-reader decay this whole pattern exists to prevent.'
    )
    non_leaf = {a: sorted(m for m in r if not m.startswith('engine/substrate/'))
                for a, r in ENGINE_READERS.items()}
    non_leaf = {a: m for a, m in non_leaf.items() if m}
    assert non_leaf == {'key_types.json': ['engine/cross_scale/echo_transport.py']}, (
        f'readers outside engine/substrate/ are now {non_leaf}. If key_types.json gained a leaf, '
        f'that is the last of the four closing — update this test and say so.'
    )
