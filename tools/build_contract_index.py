#!/usr/bin/env python3
"""build_contract_index.py — render the module contracts + Key graph as REVIEWABLE markdown.

WHY THIS EXISTS. Everything needed to review the engine's spine already exists, and none of it is
readable by a human in one sitting. `references/module_contracts.yaml` is 1,108 lines of authored
YAML; `systems/_architecture/key_type_registry_v30.md` is 1,295 lines of prose-flavoured registry;
`references/key_graph.json` is 62 KB of machine-readable join. A reviewer who wants to ask "what
actually produces `state.succession`, who listens, and where does the chain break" has to hold
three formats in their head at once. So the review does not happen, and the gaps the join already
MEASURED (2 keys nobody produces, 8 nobody consumes, 22 cross-scale edges with no transition) sit
recorded and unread.

This renders them. It is a VIEW — it decides nothing and derives nothing:

  * key rows come from `references/key_graph.json` (generated; the sole owner of the
    registry↔contracts join, including the disagreement classification and the family grouping),
  * module contract bodies come from `references/module_contracts.yaml` (the authored source),
  * build/port status comes from `references/wiring_manifest.yaml`,
  * and the check verdicts come from `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py`
    by IMPORT, not re-implementation (CLAUDE.md §8: never re-implement a rule).

Re-deriving any of those here would create a second answer to a question that already has one owner
— the exact defect the key graph was built to expose.

WHAT IT EMITS.
  * `references/KEY_INDEX.md`      — all key types by family: producers, consumers, payload,
                                     scale/permanence/horizon, and who-said-what when the two
                                     authored views differ.
  * `references/CONTRACT_INDEX.md` — all contract modules: IN → resolver → OUT, owned state,
                                     gates, derivations, transitions, loops, home doc, build status.

Both open with a REVIEW QUEUE: the open decisions, grouped by the kind of answer they need. That
ordering is the point — a reviewer building a spine needs the decisions first and the reference
material second, not 56 alphabetical rows to scan for surprises.

HONESTY LIMITS, stated here rather than discovered later:
  * A blank cell means NOT DECLARED, never "none". The two are different claims and this renderer
    cannot tell them apart — only the authors can.
  * Producer/consumer sets are the UNION of both views (key_graph's choice, preserved). The
    `agreement` column is what tells you whether the union was unanimous.
  * Family grouping is the registry's PHYSICAL `## §N Family:` filing, which differs from its own
    §9 logical count table (§9 says so itself: some Class-B types are physically filed under §8
    system_meta). Neither is wrong; they count different things.

Run:  python3 tools/build_contract_index.py           # write both files
      python3 tools/build_contract_index.py --check   # verify they are current (CI-able)
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys

try:
    import yaml
except ImportError:
    print('[contract-index] pyyaml required', file=sys.stderr)
    raise SystemExit(2)

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

ROOT = ci_common.REPO
GRAPH = os.path.join(ROOT, 'references', 'key_graph.json')
CONTRACTS = os.path.join(ROOT, 'references', 'module_contracts.yaml')
WIRING = os.path.join(ROOT, 'references', 'wiring_manifest.yaml')
REGISTRY = os.path.join(ROOT, 'systems', '_architecture', 'key_type_registry_v30.md')
SOURCES = os.path.join(ROOT, 'references', 'canonical_sources.yaml')
ADJUDICATOR = os.path.join(ROOT, 'skills', 'valoria-module-adjudicator', 'scripts',
                           'contract_adjudicator.py')

OUT_KEYS = os.path.join(ROOT, 'references', 'KEY_INDEX.md')
OUT_MODULES = os.path.join(ROOT, 'references', 'CONTRACT_INDEX.md')

BANNER = ('> **GENERATED** by `tools/build_contract_index.py`. Do not hand-edit — every fact below '
          'is rendered from a source file and a hand-edit is silently discarded on the next build.\n'
          '> Fix a fact at its source: keys in `systems/_architecture/key_type_registry_v30.md`, '
          'edges and owned state in `references/module_contracts.yaml`, build status in '
          '`references/wiring_manifest.yaml`.')

# How each reconciliation status reads to a reviewer, and — the part that matters — what KIND of
# answer it needs. A subset is a filing task; a conflict is a design decision. The key graph draws
# that distinction and this is where it becomes actionable rather than a status string.
STATUS_GLOSS = {
    'agreed': ('agreed', 'Both views declare the same set.'),
    'registry_superset': ('registry ⊃ contracts',
                          'The registry names systems the contracts have not declared back. '
                          'Filing task — no decision needed unless the registry is wrong.'),
    'contracts_superset': ('contracts ⊃ registry',
                           'The contracts declare systems the registry does not list. '
                           'Filing task, in the other direction.'),
    'registry_only': ('registry only', 'Only the registry speaks. The contract side is unauthored.'),
    'contracts_only': ('contracts only', 'Only the contracts speak. The registry entry is missing.'),
    'absent_both': ('ABSENT', 'Neither view names anyone. Nothing fills or reads this.'),
    'conflict': ('CONFLICT', 'Each view asserts what the other denies — needs a human ruling.'),
}


# ── loading ──────────────────────────────────────────────────────────────────

def load_all():
    with open(GRAPH, encoding='utf-8') as fh:
        graph = json.load(fh)
    contracts = ci_common.load_yaml(CONTRACTS)
    wiring = ci_common.load_yaml(WIRING)
    return graph, contracts, wiring


def adjudicate():
    """Import the adjudicator and run it. Its checks (A1-A12) live there and only there.

    Returns (violations, warnings) or (None, None) when the skill script is absent — a missing
    optional input degrades the review queue to 'not run', which is honest, rather than silently
    rendering a page that looks like it passed.
    """
    if not os.path.exists(ADJUDICATOR):
        return None, None
    spec = importlib.util.spec_from_file_location('contract_adjudicator', ADJUDICATOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    contracts = ci_common.load_yaml(CONTRACTS)
    with open(REGISTRY, encoding='utf-8') as fh:
        registry_md = fh.read()
    with open(SOURCES, encoding='utf-8') as fh:
        sources_text = fh.read()
    return mod.adjudicate(contracts, registry_md, sources_text)


# ── formatting helpers ───────────────────────────────────────────────────────

def esc(text) -> str:
    """Escape a value for a markdown TABLE cell (pipes break the row; newlines break the table)."""
    if text is None:
        return ''
    s = str(text).replace('|', '\\|')
    return ' '.join(s.split())


def code_list(items, empty='—') -> str:
    """Render a list of values as inline code.

    A bare STRING is wrapped, never iterated. `module_contracts.yaml` writes `from: 'engine'`
    (scalar) on two rows and `from: [a, b]` (list) everywhere else, and iterating the scalar
    silently renders `e`, `n`, `g`, `i`, `n`, `e` — a plausible-looking row that is pure
    artefact. Shape variance in an authored file is normal; a renderer that assumes one shape
    is the bug.
    """
    if items is None:
        return empty
    if isinstance(items, str):
        items = [items]
    items = [i for i in items if str(i).strip()]
    return ', '.join(f'`{esc(i)}`' for i in items) if items else empty


def anchor(name: str) -> str:
    """GitHub's heading-anchor slug: lowercase, drop punctuation, spaces→hyphens.

    Underscores are PRESERVED — GitHub keeps them. `meta.legacy_event` anchors as
    `metalegacy_event`, not `metalegacy-event`; getting this wrong yields links that look
    right and land nowhere.
    """
    keep = [c for c in name.lower() if c.isalnum() or c in '-_ ']
    return ''.join(keep).replace(' ', '-')


# `*` is not a malformed key — it is a WILDCARD SUBSCRIPTION, declared by `articulation_layer`
# and `fieldwork_knots` to mean "every key" (ED-IN-0149, which established this after a retraction
# that was itself wrong: counting `*` as a key type flips the pure-source topology figures).
# Rendering it as a broken key type would propagate the exact error that ledger entry corrects.
WILDCARD = '*'


def key_ref(kt, keys, *, here=False) -> str:
    """Link a key ONLY if it has a detail entry — anything else lands nowhere."""
    kt = str(kt)
    if kt in keys and keys[kt].get('well_formed'):
        return keylink(kt, here=here)
    if kt == WILDCARD:
        return '`*` _(wildcard subscription — every key, not a key type)_'
    return f'`{esc(kt)}` _(not a key type)_'


def keylink(kt: str, *, here=False) -> str:
    """Link to a key's detail entry. `here=True` inside KEY_INDEX.md itself — a same-file link
    must be a bare fragment, or every anchor breaks when the file is viewed standalone."""
    prefix = '' if here else 'KEY_INDEX.md'
    return f'[`{esc(kt)}`]({prefix}#{anchor(kt)})'


def modlink(m: str, *, here=False) -> str:
    prefix = '' if here else 'CONTRACT_INDEX.md'
    return f'[`{esc(m)}`]({prefix}#{anchor(m)})'


def link_list(items, linker, *, here=False, empty='—') -> str:
    items = [i for i in (items or []) if str(i).strip()]
    return ', '.join(linker(i, here=here) for i in items) if items else empty


def mod_refs(names, modules, *, empty='—') -> str:
    """Render module names, linking ONLY the ones that are contract modules.

    The producer/consumer unions carry registry prose that resolves to no module
    (`player_input`, `echo_transport`). Linking those would point at a heading that does not
    exist — a dead link that reads as a real destination, which is worse than no link, because
    the reader concludes the module exists and the page is just broken.
    """
    names = [n for n in (names or []) if str(n).strip()]
    if not names:
        return empty
    return ', '.join(modlink(n) if n in modules else f'`{esc(n)}` _(unresolved)_' for n in names)


def table(headers, rows) -> list:
    """Render a markdown table, or a placeholder when there are no rows."""
    if not rows:
        return ['_none_', '']
    out = ['| ' + ' | '.join(headers) + ' |',
           '|' + '|'.join('---' for _ in headers) + '|']
    out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    out.append('')
    return out


# ── KEY_INDEX.md ─────────────────────────────────────────────────────────────

# What counts as "the registry names a system the contracts have not declared back".
#
# `registry_superset` = contracts declared SOME of that side and the registry names more.
# `registry_only`     = contracts declared NONE of that side at all — the STRONGER case.
#
# Both are under-declarations and both belong in the §3 filing queue. `registry_only` was
# omitted at introduction, which silently hid every key whose producer AND consumer were both
# registry-only from EVERY review queue: not §3 (filtered out), not §1 (they have producers and
# consumers, so the chain does not terminate), not §2 (no contradiction). Two keys fell through
# that hole — `scene.accord_echo`, one of the few key types with a live construction site, and
# `meta.cascade_cluster_event`. Pinned by test_registry_only_reaches_a_review_queue.
#
# One owner: the three sites below (the filter, the missing-module grouping, and the per-key
# detail table) all read this tuple. They previously each hardcoded the single status.
UNDECLARED_STATUSES = ('registry_superset', 'registry_only')


def render_keys(graph, contracts) -> str:
    keys = graph['keys']
    real = {k: v for k, v in keys.items() if v['well_formed']}
    malformed = {k: v for k, v in keys.items() if not v['well_formed']}

    no_prod = sorted(k for k, v in real.items() if not v['producers'])
    no_cons = sorted(k for k, v in real.items() if not v['consumers'])
    conflicts = sorted(k for k, v in real.items()
                       if 'conflict' in (v['reconciliation']['producer_status'],
                                         v['reconciliation']['consumer_status']))
    # A contract may declare a WILDCARD consume (`{type: "*"}`). The registry↔contract join does
    # not expand it, so every explicit type the registry names that module against reads as
    # undeclared. That is a join artefact, not an authoring gap, and the difference decides what a
    # reviewer is being asked: expand the wildcard into N rows, or leave it as one deliberate edge.
    wildcard_consumers = sorted(
        m.get('module') for m in (contracts.get('modules') or [])
        if any((e or {}).get('type') == '*' for e in (m.get('consumes') or [])))

    under = sorted(k for k, v in real.items()
                   if v['reconciliation']['consumer_status'] in UNDECLARED_STATUSES
                   or v['reconciliation']['producer_status'] in UNDECLARED_STATUSES)

    L = [f'# Valoria — Key Index ({len(real)} key types)', '', BANNER, '']
    L += ['**Sources joined:** `references/key_graph.json` (generated) ← '
          '`systems/_architecture/key_type_registry_v30.md` + `references/module_contracts.yaml`. '
          'Module-level companion: [CONTRACT_INDEX.md](CONTRACT_INDEX.md).', '']
    L += ['A blank cell means **not declared**, which is not the same claim as "none". '
          'Producer/consumer sets are the **union** of both authored views; the `agreement` column '
          'says whether that union was unanimous.', '']

    # ── review queue ──
    L += ['---', '', '## Review queue — keys', '',
          'Ordered by the kind of answer needed, not by severity: a chain that terminates is a '
          '**design** question, an under-declaration is a **filing** question.', '']

    L += ['### 1. Chains that terminate (design questions)', '',
          f'**{len(no_prod)} key type(s) nobody produces** — a payload schema no system fills. '
          'Either something should emit it, or the type should be retired.', '']
    L += table(['key', 'family', 'declared consumers'],
               [[keylink(k, here=True), esc(real[k]['family']), code_list(real[k]['consumers'])]
                for k in no_prod])
    L += [f'**{len(no_cons)} key type(s) nobody consumes** — a message no system reads. Several '
          'are terminal world-events where a consumer may genuinely never exist; that is a '
          'legitimate answer, but it should be a recorded one.', '']
    L += table(['key', 'family', 'declared producers'],
               [[keylink(k, here=True), esc(real[k]['family']), code_list(real[k]['producers'])]
                for k in no_cons])

    L += ['### 2. Contradictions (need a ruling)', '']
    if conflicts:
        L += [f'**{len(conflicts)}** key type(s) where each view asserts what the other denies.', '']
        L += table(['key', 'registry says', 'contracts say'],
                   [[keylink(k, here=True),
                     code_list(real[k]['reconciliation']['registry_producers']
                               + real[k]['reconciliation']['registry_consumers']),
                     code_list(real[k]['reconciliation']['contract_producers']
                               + real[k]['reconciliation']['contract_consumers'])]
                    for k in conflicts])
    else:
        L += ['**None.** The two authored views agree everywhere they both speak — they differ '
              'only in how much they have authored. That distinction is load-bearing: it makes '
              'the backlog below a filing task rather than a pile of design decisions.', '']

    L += ['### 3. Under-declaration (filing questions)', '',
          f'**{len(under)}** key type(s) where the registry names systems the contracts have not '
          'declared back. No contradiction — but "not declared back" has two different causes and '
          'they need different answers.', '']
    if wildcard_consumers:
        L += ['⚠ **Not all of this is unauthored.** '
              + code_list(wildcard_consumers)
              + ' declare a **wildcard** consume (`{type: "*"}`) — authored deliberately, as a '
              'universal reader of the Key stream. This join does not expand wildcards, so every '
              'explicit type the registry names them against appears here. For those rows the '
              'question is *should the wildcard be expanded into explicit declarations*, which is '
              'a different decision from *someone forgot to file this*.', '']
    L += ['Rows whose contract side declares **nothing** on that side (`registry_only`) may also '
          'appear in queue 1 above: a key can both terminate and be under-declared. That is two '
          'problems on one key, not double-counting.', '']

    # Group by the module that is MISSING, not by key. The row count is what a reviewer sees first
    # and it badly overstates the work: if one module accounts for most of the gap, this is one
    # filing decision applied N times, not N decisions. Counting it is the difference between a
    # backlog you can close in an afternoon and one that looks like a redesign.
    missing = {}
    for k in under:
        r = real[k]['reconciliation']
        for side in ('producer', 'consumer'):
            if r[f'{side}_status'] not in UNDECLARED_STATUSES:
                continue
            w = side + 's'
            for m in set(r[f'registry_{w}']) - set(r[f'contract_{w}']):
                missing.setdefault(m, {'producer': [], 'consumer': []})[side].append(k)
    # Sort must be TOTAL. Ranking by count alone leaves ties broken by `missing`'s insertion
    # order, which comes from iterating `set(registry) - set(contract)` — PYTHONHASHSEED-dependent,
    # so the rendered file differed between runs and `--check` was flaky. Latent while only two
    # modules appeared here; live as soon as there were ties. Name is the tiebreak.
    # Pinned by test_render_is_deterministic.
    ranked = sorted(missing.items(),
                    key=lambda kv: (-(len(kv[1]['producer']) + len(kv[1]['consumer'])), kv[0]))
    for v in missing.values():
        v['producer'].sort()
        v['consumer'].sort()
    total_gaps = sum(len(v['producer']) + len(v['consumer']) for v in missing.values())
    if ranked:
        top, tv = ranked[0]
        top_n = len(tv['producer']) + len(tv['consumer'])
        L += [f'**Grouped by the module that is missing** — {total_gaps} undeclared edge(s) across '
              f'{len(missing)} module(s). `{esc(top)}` alone accounts for **{top_n} of '
              f'{total_gaps}**, so most of this column is one decision applied repeatedly, not '
              f'{len(under)} separate ones.', '']
        # Not every name here is a module: `player_input` is registry prose that resolves to
        # nothing. Linking it would manufacture a destination, so it renders as bare code with
        # the reason attached.
        L += table(['module missing the declaration', 'as producer of', 'as consumer of', 'total'],
                   [[modlink(m) if m in graph['modules']
                     else f'`{esc(m)}` _(not a contract module — unresolved reference)_',
                     len(v['producer']), len(v['consumer']),
                     len(v['producer']) + len(v['consumer'])] for m, v in ranked])

    L += ['<details><summary>per-key detail</summary>', '']
    L += table(['key', 'side', 'named by registry', 'declared in contracts'],
               [[keylink(k, here=True), side, code_list(r[f'registry_{w}']),
                 code_list(r[f'contract_{w}'])]
                for k in under
                for r in [real[k]['reconciliation']]
                for side, w in (('producers', 'producers'), ('consumers', 'consumers'))
                if r[f'{side[:-1]}_status'] in UNDECLARED_STATUSES])
    L += ['</details>', '']

    L += ['### 4. Names that resolve to no module', '',
          'Registry prose naming something that is not a contract module. Left unresolved on '
          'purpose — mapping `player_input` or `all subscribing systems` to a module is a design '
          'decision, and guessing one would fabricate it.', '']
    L += table(['unresolved reference'],
               [[f'`{esc(u)}`'] for u in graph['unresolved_references']])

    if malformed:
        L += ['### 5. Names that are not key types', '',
              'Entries in the contracts\' `emits`/`consumes` that are not `namespace.name` key '
              'types. `*` is the known and deliberate one — a **wildcard subscription** meaning '
              '"every key", not a malformed name (ED-IN-0149). Anything else here is a defect.', '']
        L += table(['name', 'reading', 'declared by'],
                   [[f'`{esc(k)}`',
                     'wildcard subscription — every key' if k == WILDCARD else '**unrecognised**',
                     code_list(v['producers'] + v['consumers'])]
                    for k, v in sorted(malformed.items())])

    # ── the index proper ──
    L += ['---', '', '## Key types by family', '']
    L += ['Family is the registry\'s **physical** `## §N Family:` filing. It differs from the '
          'registry\'s own §9 logical count table, which the registry notes itself: some Class-B '
          'types are physically filed under §8 `system_meta`. Neither count is wrong — they count '
          'different things.', '']

    fams = {}
    for k, v in sorted(real.items()):
        fams.setdefault(v['family'] or '(no family — not in the registry)', []).append(k)

    L += table(['family', 'types', 'no producer', 'no consumer'],
               [[f'[{esc(f)}](#family-{anchor(f)})', len(ks),
                 sum(1 for k in ks if not real[k]['producers']),
                 sum(1 for k in ks if not real[k]['consumers'])]
                for f, ks in sorted(fams.items())])

    for fam, kts in sorted(fams.items()):
        L += [f'### Family: {fam}', '']
        L += table(['key', 'producers', 'consumers', 'scale', 'permanence', 'horizon', 'agreement'],
                   [[keylink(k, here=True), code_list(v['producers']), code_list(v['consumers']),
                     code_list(v['scale']), esc(v['permanence']), esc(v['time_horizon']),
                     esc(STATUS_GLOSS.get(v['reconciliation']['consumer_status'],
                                          (v['reconciliation']['consumer_status'], ''))[0])]
                    for k in kts for v in [real[k]]])

    # ── per-key detail ──
    L += ['---', '', '## Key detail', '']
    for k in sorted(real):
        v = real[k]
        rec = v['reconciliation']
        L += [f'### {k}', '']
        if v['description']:
            L += [esc(v['description']), '']
        rows = [
            ['family', esc(v['family'])],
            ['scale', code_list(v['scale'])],
            ['permanence', esc(v['permanence'])],
            ['time horizon', esc(v['time_horizon'])],
            ['payload — required', code_list(v['payload']['required'])],
            ['payload — optional', code_list(v['payload']['optional'])],
            ['producers (union)', mod_refs(v['producers'], graph['modules'])
             if v['producers'] else '**none — nothing fills this**'],
            ['consumers (union)', mod_refs(v['consumers'], graph['modules'])
             if v['consumers'] else '**none — nothing reads this**'],
        ]
        L += table(['field', 'value'], rows)
        for side, word in (('producer', 'producers'), ('consumer', 'consumers')):
            st = rec[f'{side}_status']
            if st in ('agreed', 'absent_both'):
                continue
            label, gloss = STATUS_GLOSS.get(st, (st, ''))
            L += [f'- **{side}s — {label}.** {gloss} '
                  f'Registry: {code_list(rec[f"registry_{word}"])} · '
                  f'contracts: {code_list(rec[f"contract_{word}"])}']
        if rec['non_referent_prose']:
            L += [f'- **Prose naming no module:** {code_list(rec["non_referent_prose"])}']
        L += ['']

    return '\n'.join(L).rstrip() + '\n'


# ── CONTRACT_INDEX.md ────────────────────────────────────────────────────────

def render_modules(graph, contracts, wiring, violations, warnings) -> str:
    mods = contracts['modules']
    mods = mods if isinstance(mods, list) else list(mods.values())
    mods = sorted(mods, key=lambda m: m.get('module') or '')
    gmods = graph['modules']
    wmods = wiring.get('modules') or {}

    L = [f'# Valoria — Module Contract Index ({len(mods)} modules)', '', BANNER, '']
    L += ['**Sources joined:** `references/module_contracts.yaml` (authored contracts) + '
          '`references/key_graph.json` (generated homes/authority) + '
          '`references/wiring_manifest.yaml` (build + port status). '
          'Key-level companion: [KEY_INDEX.md](KEY_INDEX.md).', '']
    L += ['`authority` is derived, not stored (Jordan\'s 2026-08-02 precedence rule): **code** if a '
          'declared `sim_module` resolves on disk **or the module is on `build_key_graph.py`\'s '
          'CODE_EXISTS_UNDECLARED list** (code demonstrably present while its row deliberately '
          'declares no `sim_module` — `mass_battle`\'s row is MB-lane-owned and IN must not fill '
          'it), **prose** if only a design doc exists, **none** '
          'if neither. It expires on someone else\'s commit, which is why nothing hand-annotates '
          'it.', '']

    # ── review queue ──
    L += ['---', '', '## Review queue — modules', '']

    if violations is None:
        L += ['⚠️ `contract_adjudicator.py` not found — check verdicts below are **not run**, not '
              'passed.', '']
    else:
        by_check = {}
        for v in violations:
            by_check.setdefault(v.split(' ', 1)[0].split('[')[0].strip() or 'other', []).append(v)
        L += [f'### 1. Contract violations ({len(violations)})', '',
              'From `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py` (checks '
              'A1–A12), imported rather than re-implemented.', '']
        # Count DISTINCT module pairs alongside raw violations. Same reason as the key grouping
        # above: 20 A6 lines across 5 module pairs is 5 missing transition declarations, not 20
        # problems, and the raw count is what makes a tractable queue look like a redesign.
        pair_counts = {}
        for c, vs in by_check.items():
            pairs = set()
            for v in vs:
                if '[' in v and ']' in v:
                    pairs.add(v[v.index('[') + 1:v.index(']')])
            pair_counts[c] = pairs
        L += table(['check', 'violations', 'distinct module pairs', 'first instance'],
                   [[f'`{esc(c)}`', len(vs), len(pair_counts[c]),
                     esc(vs[0].split(':', 1)[1] if ':' in vs[0] else '')]
                    for c, vs in sorted(by_check.items())])
        for c, vs in sorted(by_check.items()):
            if pair_counts[c]:
                L += [f'`{esc(c)}` spans: ' + code_list(sorted(pair_counts[c])), '']
            L += [f'<details><summary><b>{esc(c)}</b> — {len(vs)} violation(s)</summary>', '']
            L += [f'- {esc(v)}' for v in vs]
            L += ['', '</details>', '']

    homeless = sorted(m for m, v in gmods.items() if not v.get('subsystem'))
    nodoc = sorted(m for m, v in gmods.items() if not v.get('doc'))
    noauth = sorted(m for m, v in gmods.items() if v.get('authority') == 'none')
    stubs = sorted(m.get('module') for m in mods if m.get('status') == 'stub')

    L += ['### 2. Modules with no home', '',
          f'**{len(homeless)}** of {len(gmods)} modules declare no subsystem home, '
          f'**{len(nodoc)}** have no design doc, and **{len(noauth)}** have neither doc nor code — '
          'a declared module that is currently nothing citable.', '']
    L += table(['module', 'subsystem', 'design doc', 'sim module', 'authority', 'status'],
               [[modlink(m), esc(v.get('subsystem')) or '**—**',
                 f'`{esc(v["doc"])}`' if v.get('doc') else '**—**',
                 f'`{esc(v["sim_module"])}`' if v.get('sim_module') else '**—**',
                 f'**{esc(v.get("authority"))}**' if v.get('authority') == 'none'
                 else esc(v.get('authority')),
                 esc(v.get('status'))]
                for m, v in sorted(gmods.items())
                if m in homeless or m in nodoc or m in noauth])

    if stubs:
        L += ['### 3. Stubs', '',
              'Pointer-only rows carrying zero edges.', '']
        L += table(['module', 'note'],
                   [[modlink(s), esc((next((m for m in mods if m.get('module') == s), {})
                                     .get('gap_notes') or [''])[0])] for s in stubs])

    if warnings:
        L += [f'### 4. Warnings ({len(warnings)})', '',
              'Not blocking. `W-GAP` entries are the contract authors\' own recorded gap notes — '
              'read them before treating a blank field as an oversight.', '',
              '<details><summary>show all</summary>', '']
        L += [f'- {esc(w)}' for w in warnings]
        L += ['', '</details>', '']

    # ── summary table ──
    L += ['---', '', '## Modules at a glance', '']
    rows = []
    for m in mods:
        name = m.get('module')
        g = gmods.get(name, {})
        w = wmods.get(name, {})
        rows.append([
            modlink(name), code_list(m.get('scales')), esc(m.get('resolver')),
            esc(g.get('authority')), esc(w.get('build')), esc(w.get('godot')),
            len(m.get('consumes') or []), len(m.get('emits') or []),
            len(m.get('state') or []), len(m.get('gates') or []),
            len(m.get('derivations') or []),
        ])
    L += table(['module', 'scales', 'resolver', 'authority', 'build', 'godot',
                'IN', 'OUT', 'state', 'gates', 'derivations'], rows)
    L += ['`build` / `godot` columns are from `wiring_manifest.yaml` '
          f'(as_of {wiring.get("as_of")}); a blank means the module has no row there.', '']

    # ── per-module detail ──
    L += ['---', '', '## Module detail', '']
    for m in mods:
        name = m.get('module')
        g = gmods.get(name, {})
        w = wmods.get(name, {})
        L += [f'### {name}', '']
        if m.get('aliases'):
            L += [f'_Also written as {code_list(m["aliases"])} in prose._', '']

        L += table(['field', 'value'], [
            ['registry system', f'`{esc(m.get("registry_system"))}`' if m.get('registry_system') else ''],
            ['scales', code_list(m.get('scales'))],
            ['resolver', f'`{esc(m.get("resolver"))}`' if m.get('resolver') else ''],
            ['design doc', f'`{esc(g.get("doc"))}`' if g.get('doc') else '**— none**'],
            ['sim module', f'`{esc(g.get("sim_module"))}`' if g.get('sim_module') else '**— none**'],
            ['authority', esc(g.get('authority'))],
            ['build / godot', f'{esc(w.get("build")) or "—"} / {esc(w.get("godot")) or "—"}'],
            ['status', esc(m.get('status'))],
            ['accounting phase', esc(m.get('accounting_phase'))],
        ])

        L += ['**IN** — keys consumed', '']
        L += table(['key', 'declared producers'],
                   [[key_ref(c.get('type'), graph['keys']), code_list(c.get('from'))]
                    for c in (m.get('consumes') or [])])
        L += ['**OUT** — keys emitted', '']
        L += table(['key', 'terminal', 'note'],
                   [[key_ref(e.get('type'), graph['keys']),
                     'yes' if e.get('terminal') else 'no', esc(e.get('note'))]
                    for e in (m.get('emits') or [])])

        if m.get('state'):
            L += ['**Owned state**', '']
            L += table(['quantity', 'bucket', 'writable', 'note'],
                       [[esc(s.get('name')), f'`{esc(s.get("bucket"))}`',
                         'yes' if s.get('writable') else '**no (derived)**', esc(s.get('note'))]
                        for s in m['state']])
        if m.get('gates'):
            L += ['**Gates**', '']
            L += table(['id', 'when', 'then', 'on', 'source'],
                       [[f'`{esc(gt.get("id"))}`', esc(gt.get('when')), esc(gt.get('then')),
                         esc(gt.get('on')), esc(gt.get('source'))] for gt in m['gates']])
        if m.get('derivations'):
            L += ['**Derivations**', '']
            L += table(['output', 'inputs', 'formula', 'source'],
                       [[esc(d.get('output')), code_list(d.get('inputs')), esc(d.get('formula')),
                         esc(d.get('source'))] for d in m['derivations']])
        if m.get('transitions'):
            L += ['**Scale transitions**', '']
            L += table(['field', 'value'],
                       [[esc(k), esc(v)] for t in m['transitions'] for k, v in t.items()])
        if m.get('loops'):
            L += ['**Feedback loops**', '']
            L += table(['with', 'damper'],
                       [[f'`{esc(lp.get("with"))}`', esc(lp.get('damper'))] for lp in m['loops']])
        if m.get('gap_notes'):
            L += ['**Gap notes** (the authors\' own recorded uncertainty — read before assuming '
                  'a blank field is an oversight)', '']
            L += [f'- {esc(n)}' for n in m['gap_notes']] + ['']
        if m.get('sources'):
            L += ['**Sources**', '', code_list(m['sources']), '']

    return '\n'.join(L).rstrip() + '\n'


# ── driver ───────────────────────────────────────────────────────────────────

def build():
    graph, contracts, wiring = load_all()
    violations, warnings = adjudicate()
    return {OUT_KEYS: render_keys(graph, contracts),
            OUT_MODULES: render_modules(graph, contracts, wiring, violations, warnings)}


def main(argv):
    docs = build()
    check = '--check' in argv
    stale = []
    for path, text in docs.items():
        rel = os.path.relpath(path, ROOT)
        if check:
            current = open(path, encoding='utf-8').read() if os.path.exists(path) else None
            if current != text:
                stale.append(rel)
            continue
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
        print(f'[contract-index] {len(text.splitlines()):>5} lines  ->  {rel}')
    if check:
        if stale:
            print('[contract-index] STALE: ' + ', '.join(stale)
                  + '\n  regenerate with `python3 tools/build_contract_index.py` and commit',
                  file=sys.stderr)
            return 1
        print('[contract-index] both indexes are current')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
