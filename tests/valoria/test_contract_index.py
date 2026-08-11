"""The review surface must describe the tree, and its links must land.

`references/KEY_INDEX.md` + `references/CONTRACT_INDEX.md` exist so the Key graph and the module
contracts can be READ by a human — the reviewable form of `key_graph.json`, `module_contracts.yaml`
and `wiring_manifest.yaml`. That makes them exactly the kind of artifact this repo keeps getting
burned by: a rendering that was true when generated and quietly stopped being true, while still
reading as authoritative.

So two properties are pinned here, and they are different failures:

  1. FRESHNESS — the committed files equal a fresh build. A stale index is worse than no index:
     a reviewer makes decisions against numbers that no longer describe the tree.
  2. LINK INTEGRITY — every `#anchor` resolves to a heading that exists. This one is pinned
     because it already caught four real defects at introduction, all of the same shape: a name
     that LOOKS like a module or a key but is not one (`player_input` and `echo_transport` are
     registry prose resolving to no module; `*` is a wildcard that leaked into the contracts).
     Each rendered as a confident link to nothing. A dead link is worse than no link — the reader
     concludes the destination exists and the page is merely broken.

Both are guards on a generator, per CLAUDE.md §0.1 point 5: the defect class is "renderer assumed
a shape the authored file does not always have", and the guard is what makes that tolerable.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BUILDER = os.path.join(ROOT, 'tools', 'build_contract_index.py')
GRAPH = os.path.join(ROOT, 'references', 'key_graph.json')
DOCS = {
    'KEY_INDEX.md': os.path.join(ROOT, 'references', 'KEY_INDEX.md'),
    'CONTRACT_INDEX.md': os.path.join(ROOT, 'references', 'CONTRACT_INDEX.md'),
}

pytest.importorskip('yaml')

HEADING_RE = re.compile(r'^#{1,6}\s+(.*?)\s*$', re.M)
LINK_RE = re.compile(r'\]\(([^)#]*)#([^)]*)\)')


def _slug(text: str) -> str:
    """GitHub's heading-anchor slug. Kept independent of the builder's own `anchor()` ON PURPOSE:
    a shared helper would make both sides wrong together and the test would still pass."""
    return ''.join(c for c in text.lower() if c.isalnum() or c in '-_ ').replace(' ', '-')


@pytest.fixture(scope='module')
def docs():
    missing = [n for n, p in DOCS.items() if not os.path.exists(p)]
    if missing:
        pytest.fail(f'{missing} missing — run `python3 tools/build_contract_index.py`')
    return {n: open(p, encoding='utf-8').read() for n, p in DOCS.items()}


def test_indexes_are_current():
    """The committed files must equal a fresh build — they are generated, so any drift means a
    hand-edit or a stale commit, and either makes every number in them describe the wrong tree."""
    r = subprocess.run([sys.executable, BUILDER, '--check'],
                       capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, (
        f'contract index is stale:\n{r.stdout}\n{r.stderr}\n'
        'Regenerate with `python3 tools/build_contract_index.py` and commit.')


def test_every_anchor_link_resolves(docs):
    """THE LOAD-BEARING CHECK. Four dead links shipped in the first draft; none was visible by
    reading the generator."""
    slugs = {name: {_slug(h) for h in HEADING_RE.findall(text)} for name, text in docs.items()}
    broken = []
    for name, text in docs.items():
        for target, frag in LINK_RE.findall(text):
            dest = name if not target else os.path.basename(target)
            if dest not in slugs:
                broken.append(f'{name}: -> {target}#{frag} (no such generated file)')
            elif not frag:
                broken.append(f'{name}: -> {target}# (EMPTY anchor — links nowhere)')
            elif frag not in slugs[dest]:
                broken.append(f'{name}: -> {target}#{frag} (no such heading in {dest})')
    assert not broken, ('dead link(s) in the generated review surface:\n  '
                        + '\n  '.join(broken[:20]))


def test_no_row_was_rendered_by_iterating_a_string(docs):
    """`module_contracts.yaml` writes `from: 'engine'` (scalar) on two rows and `from: [a, b]`
    everywhere else. A renderer that iterates the scalar emits `` `e`, `n`, `g`, `i`, `n`, `e` `` —
    a row that looks like data and is pure artefact. The signature is a run of single-character
    code spans, which nothing legitimate produces."""
    bad = []
    for name, text in docs.items():
        for m in re.finditer(r'(?:`.` *, *){2,}`.`', text):
            line = text[:m.start()].count('\n') + 1
            bad.append(f'{name}:{line}: {m.group(0)[:40]}')
    assert not bad, ('a string was iterated into characters:\n  ' + '\n  '.join(bad[:10]))


def test_every_contract_module_and_key_type_is_rendered(docs):
    """Coverage: the point of an index is that nothing is missing from it. A silently truncated
    index is the failure mode that would make the review surface actively misleading."""
    import json
    with open(os.path.join(ROOT, 'references', 'key_graph.json'), encoding='utf-8') as fh:
        graph = json.load(fh)

    key_heads = {h for h in HEADING_RE.findall(docs['KEY_INDEX.md'])}
    missing_keys = {k for k, v in graph['keys'].items() if v['well_formed']} - key_heads
    assert not missing_keys, f'key type(s) absent from KEY_INDEX.md: {sorted(missing_keys)}'

    mod_heads = {h for h in HEADING_RE.findall(docs['CONTRACT_INDEX.md'])}
    missing_mods = set(graph['modules']) - mod_heads
    assert not missing_mods, f'module(s) absent from CONTRACT_INDEX.md: {sorted(missing_mods)}'


def test_adjudicator_verdicts_are_imported_not_reimplemented():
    """CLAUDE.md §8: every rule lives once. The index must show the SAME violation count the
    adjudicator produces — if it ever diverges, someone has grown a second copy of the checks."""
    spec = importlib.util.spec_from_file_location('bci', BUILDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    violations, _ = mod.adjudicate()
    if violations is None:
        pytest.skip('contract_adjudicator.py not present')
    text = open(DOCS['CONTRACT_INDEX.md'], encoding='utf-8').read()
    m = re.search(r'## Review queue — modules.*?### 1\. Contract violations \((\d+)\)', text, re.S)
    assert m, 'CONTRACT_INDEX.md has no violation count section'
    assert int(m.group(1)) == len(violations), (
        f'index reports {m.group(1)} violations, adjudicator produces {len(violations)} — '
        'the index has drifted from the checker it claims to render.')


def _load_builder():
    spec = importlib.util.spec_from_file_location('bci', BUILDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_render_is_deterministic():
    """The same inputs must render the same bytes, or `--check` is a coin flip.

    Found 2026-08-10 (ED-IN-0152): the under-declaration grouping ranked modules by count alone,
    leaving ties broken by `missing`'s insertion order — which comes from iterating
    `set(registry) - set(contract)` and therefore varies with PYTHONHASHSEED between processes.
    KEY_INDEX.md rendered two different byte sequences across runs, so `test_indexes_are_current`
    passed or failed depending on which process wrote last. Latent while only two modules appeared
    in that table; live the moment there were ties.

    This builds twice IN-PROCESS, which cannot catch a cross-process hash-seed difference, so it
    also re-renders under an explicitly different PYTHONHASHSEED in a subprocess — that is the
    variable that actually moved. The subprocess digests with sha256, NOT `hash()`: Python's
    builtin string hash is itself seed-randomised, so comparing `hash()` across seeds can never
    agree and would fail on a perfectly deterministic renderer. (This test's first draft did
    exactly that.)
    """
    mod = _load_builder()
    first = mod.build()
    second = mod.build()
    for path in first:
        assert first[path] == second[path], \
            f'{os.path.relpath(path, ROOT)} differs between two builds in the same process'

    outs = set()
    for seed in ('0', '1', '12345'):
        env = dict(os.environ, PYTHONHASHSEED=seed)
        r = subprocess.run([sys.executable, '-c',
                            'import importlib.util,sys;'
                            f'spec=importlib.util.spec_from_file_location("bci",{BUILDER!r});'
                            'm=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);'
                            'import hashlib;d=m.build();'
                            'h=hashlib.sha256();'
                            '[h.update(v.encode()) for v in [d[k] for k in sorted(d)]];'
                            'sys.stdout.write(h.hexdigest())'],
                           capture_output=True, text=True, env=env, cwd=ROOT)
        assert r.returncode == 0, f'render failed under PYTHONHASHSEED={seed}: {r.stderr}'
        outs.add(r.stdout.strip())
    assert len(outs) == 1, (
        f'render differs across PYTHONHASHSEED values ({len(outs)} distinct outputs) — '
        'something in the render iterates a set or dict whose order is not pinned')


def test_registry_only_reaches_a_review_queue():
    """Every under-declared key must appear in SOME review queue.

    Found 2026-08-10 (ED-IN-0152): the §3 filter matched only `registry_superset`, so a key whose
    producer AND consumer were both `registry_only` (contracts declare neither side) fell through
    every queue — not §3 (filtered out), not §1 (it has producers and consumers, so its chain does
    not terminate), not §2 (no contradiction). `scene.accord_echo` — one of the few key types with
    a live construction site — and `meta.cascade_cluster_event` were invisible in a document whose
    entire purpose is to be reviewed.
    """
    graph = json.load(open(GRAPH, encoding='utf-8'))
    text = open(DOCS['KEY_INDEX.md'], encoding='utf-8').read()
    start = text.index('## Review queue — keys')
    end = text.index('\n## ', start + 10)
    queue = text[start:end]

    orphaned = []
    for kt, v in graph['keys'].items():
        if not v['well_formed']:
            continue
        r = v['reconciliation']
        if 'registry_only' not in (r['producer_status'], r['consumer_status']):
            continue
        if kt not in queue:
            orphaned.append(kt)
    assert not orphaned, (
        'under-declared key(s) appear in NO review queue, so nobody reviewing this document can '
        f'see them: {sorted(orphaned)}')


def test_wildcard_consumers_are_not_reported_as_unauthored():
    """A wildcard consume is authored on purpose; calling it unauthored misdirects the reviewer.

    `articulation_layer` declares `{type: "*"}` — a deliberate universal read of the Key stream.
    The registry↔contract join does not expand wildcards, so every explicit type shows as
    undeclared. Reporting that as "the contract side is simply unauthored" turns one design
    question (should the wildcard be expanded?) into ~41 imaginary filing errors.
    """
    text = open(DOCS['KEY_INDEX.md'], encoding='utf-8').read()
    i = text.index('### 3. Under-declaration')
    section = text[i:i + 2500]
    assert 'the contract side is simply unauthored' not in section, \
        'the under-declaration header still claims the contract side is unauthored'
    assert 'wildcard' in section.lower(), \
        'the under-declaration section does not mention the wildcard cause at all'
