#!/usr/bin/env python3
"""
build_engine_atlas.py — the generated half of the engine atlas (ED-IN-0152).

WHAT THIS IS FOR. Answering "what is this engine, subsystem by subsystem, and what actually
runs?" took a full session of hand-tracing, a blind re-derivation, and a diff. Most of that
labour was mechanical: finding code homes, callers, stubs, orphans, reachability, and — the
expensive part — finding what a hand-written description LEFT OUT. This renders the mechanical
part from sources that already exist, so the next person spends their effort on the half that
needs judgment.

WHAT IT DELIBERATELY DOES NOT DO. It does not write flow. An import graph yields "A calls B";
it does not yield "the read contest feeds the sigma assembly", which is the claim a reader
actually needs. Nor can it rule whether an absence is a defect or a deliberate deferral. Those
live in the authored flow skeletons (`systems/<x>/<x>_flow_skeleton_v1.md`) and the authored
companion (`systems/_architecture/engine_atlas_v1.md`). This tool's job is to render what is
countable and to CHECK what was authored — not to replace it.

COMPOSES, DOES NOT REINVENT (CLAUDE.md section 8). Every input has an existing owner:
  * `references/module_contracts.yaml`   — authored contracts
  * `references/key_graph.json`          — the registry<->contracts join (build_key_graph.py)
  * `references/wiring_manifest.yaml`    — build + port status
  * `references/execution_map.json`      — per-module build/executes status
  * `references/execution_trace.json`    — what a SEEDED CAMPAIGN actually called
  * the flow skeletons                   — the authored as-built view
Nothing here re-derives a fact one of those owns; where they disagree, the atlas shows both.

THE COVERAGE CHECK is the part that earns the tool. For each subsystem it AST-parses the code
home and lists public top-level callables that the authored skeleton never names. Those are
CANDIDATE omissions, not defects: a skeleton's section 1 lists what an outside caller can enter
through, which is legitimately narrower than every public def. But the list is exactly where
hand-tracing loses things, and it is cheap to regenerate.

CLI:
    python tools/build_engine_atlas.py            # render
    python tools/build_engine_atlas.py --check    # exit 1 if the committed file is stale
"""
import argparse
import ast
import json
import os
import re
import sys

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

ROOT = ci_common.REPO
SYSTEMS = os.path.join(ROOT, 'systems')
OUT_MD = os.path.join(ROOT, 'references', 'ENGINE_ATLAS.md')
OUT_JSON = os.path.join(ROOT, 'references', 'engine_atlas.json')

CONTRACTS = os.path.join(ROOT, 'references', 'module_contracts.yaml')
KEY_GRAPH = os.path.join(ROOT, 'references', 'key_graph.json')
EXEC_MAP = os.path.join(ROOT, 'references', 'execution_map.json')
EXEC_TRACE = os.path.join(ROOT, 'references', 'execution_trace.json')
SPEC = os.path.join(SYSTEMS, '_architecture', 'subsystem_flow_skeletons_v1.md')

BANNER = ('> **GENERATED** by `tools/build_engine_atlas.py`. Do not hand-edit — a hand-edit is '
          'silently discarded on the next build.\n>\n'
          '> This is the **countable** half of the atlas. The reading guide, the campaign spine '
          'and the open-decision set are authored in '
          '[`systems/_architecture/engine_atlas_v1.md`](../systems/_architecture/engine_atlas_v1.md); '
          'the per-subsystem flow is authored in each `systems/<x>/<x>_flow_skeleton_v1.md`. '
          'Nothing here ratifies anything.')


# ── inputs ───────────────────────────────────────────────────────────────────

def _read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def _json(path):
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def discovered_subsystems():
    """Every subsystem folder that EXISTS on disk, right now.

    The filesystem is the authority on what exists; the roster is the authority on what has been
    declared. Reading only the roster would make this tool blind to a subsystem someone adds
    tomorrow — the exact failure a generated atlas must not have. Reading only the filesystem
    would lose the lane/skeleton metadata. So both are read and reconciled, and any disagreement
    is RENDERED (see `drift`) rather than silently resolved.
    """
    if not os.path.isdir(SYSTEMS):
        return []
    out = []
    for name in sorted(os.listdir(SYSTEMS)):
        path = os.path.join(SYSTEMS, name)
        if os.path.isdir(path) and name != '__pycache__':
            out.append(name)
    return out


def roster():
    """Subsystem roster — parsed from the flow-skeleton spec, its single owner.

    Deliberately NOT a second list: the spec's section 3 table is what makes the skeleton guard
    demand a file, so reading it here keeps the two apparatus halves on one roster.
    """
    text = _read(SPEC)
    start = text.index('## 3. Roster')
    end = text.index('## 4. ', start)
    rows = []
    for line in text[start:end].splitlines():
        m = re.match(r'\|\s*`([a-z_]+)`\s*\|\s*([A-Z]{2})\s*\|\s*`([^`]+)`\s*\|', line.strip())
        if m:
            rows.append({'subsystem': m.group(1), 'lane': m.group(2), 'skeleton': m.group(3)})
    return rows


def load_inputs():
    """Load every input, and RECORD any that is absent.

    A missing input must not degrade quietly: without the trace every subsystem would render as
    "not in trace", which reads as a finding rather than as a missing file. `absent` is carried
    into the render and the JSON so the document states its own blind spots.
    """
    import yaml
    absent = []
    contracts = ci_common.load_yaml(CONTRACTS)

    def opt(path, fallback):
        if os.path.exists(path):
            return _json(path)
        absent.append(os.path.relpath(path, ROOT))
        return fallback

    graph = opt(KEY_GRAPH, {'keys': {}, 'modules': {}})
    emap = opt(EXEC_MAP, {'modules': {}})
    trace = opt(EXEC_TRACE, {'by_subsystem_path': {}})
    return contracts, graph, emap, trace, absent


# ── derivation ───────────────────────────────────────────────────────────────

def code_files(subsystem):
    """Every .py under the subsystem folder. Sorted, so the render is deterministic."""
    base = os.path.join(SYSTEMS, subsystem)
    out = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d != '__pycache__')
        for fn in sorted(filenames):
            if fn.endswith('.py') and fn != '__init__.py':
                out.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    return sorted(out)


def public_callables(relpath):
    """Top-level public defs/classes in one file, via AST.

    AST, not a regex: a regex over `def ` also matches nested defs, strings and comments, and
    this list feeds an omission report where a false positive costs a reader's time.
    """
    try:
        tree = ast.parse(_read(os.path.join(ROOT, relpath)))
    except (SyntaxError, UnicodeDecodeError):
        return []
    names = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if not node.name.startswith('_'):
                names.append((node.name, node.lineno))
    return names


METAKEY = 'VALORIA_CONTRACTS'


def declared_contracts(subsystem):
    """Read an OPTIONAL package-level metakey instead of inferring from paths.

    A package may declare which module contracts it implements::

        VALORIA_CONTRACTS = ["faction_state", "faction_politics"]

    in `systems/<subsystem>/sim/__init__.py` (or the folder's own `__init__.py`). This is the
    preferred attribution because it is the only one that survives a file move and needs no
    heuristic: every other source infers from a path prefix, a name, or an authored header.

    It follows the precedent already in the tree — `stubwire.stub_resolve(module, symbol, reason)`
    is the same idea, a machine-findable declaration carrying structured payload, and it is why
    stub sites are the one gap class that never needs re-discovering.

    Adoption is VOLUNTARY and reported (see the adoption line in the render), so the tool works
    today on packages that have not declared, and gets more reliable as they do. Read by AST, so
    importing the package is never required.
    """
    out = []
    for rel in (os.path.join(SYSTEMS, subsystem, 'sim', '__init__.py'),
                os.path.join(SYSTEMS, subsystem, '__init__.py')):
        if not os.path.isfile(rel):
            continue
        try:
            tree = ast.parse(_read(rel))
        except (SyntaxError, UnicodeDecodeError):
            continue
        for node in tree.body:
            if not isinstance(node, ast.Assign):
                continue
            if not any(isinstance(t, ast.Name) and t.id == METAKEY for t in node.targets):
                continue
            try:
                value = ast.literal_eval(node.value)
            except ValueError:
                continue
            if isinstance(value, (list, tuple)):
                out.extend(str(v) for v in value)
    return out


def contracts_for(subsystem, contracts, emap, graph, skel):
    """Which module contracts belong to this subsystem — from THREE sources, with provenance.

    A single join is not enough and a name-guess is wrong. Measured on the current tree, a
    code-path join alone attributes only 9 of 27 contracts, because several declare code outside
    their own folder (`faction_state`'s `sim_module` is `engine/autoload/game_state.py`) or
    deliberately declare none at all (`mass_battle`'s row is MB-lane-owned).

    So three sources are unioned and each attribution records WHY it was made:
      `code`     — a declared code path under `systems/<subsystem>/`
      `graph`    — `key_graph.json`'s own `subsystem` attribution
      `authored` — the skeleton's `Contracts:` header, itself guarded to name only real
                   contracts (`test_contract_names_resolve_in_the_generated_index`)

    Union, not precedence: disagreement between sources is information, and the provenance tag is
    what lets a reader see a contract attributed on one weak basis rather than three.
    """
    src = {}

    def add(name, why):
        if name:
            src.setdefault(name, set()).add(why)

    for name in declared_contracts(subsystem):
        add(name, 'declared')
    for name, rec in (emap.get('modules') or {}).items():
        if (rec.get('code') or '').startswith(f'systems/{subsystem}/'):
            add(name, 'code')
    for m in (contracts.get('modules') or []):
        sim = m.get('sim_module')
        if isinstance(sim, str) and sim.startswith(f'systems/{subsystem}/'):
            add(m.get('module'), 'code')
    for name, rec in (graph.get('modules') or {}).items():
        if rec.get('subsystem') == subsystem:
            add(name, 'graph')
    if skel:
        m = re.search(r'\*\*Contracts:\*\*(.*)', skel['text'])
        if m:
            declared = {mm.get('module') for mm in (contracts.get('modules') or [])}
            for nm in re.findall(r'`([^`]+)`', m.group(1)):
                if nm in declared:
                    add(nm, 'authored')
    return {k: sorted(v) for k, v in sorted(src.items())}


def reachability(subsystem, trace):
    """Calls this subsystem made in a seeded campaign, per phase, from the execution trace."""
    phases = {}
    for phase, buckets in (trace.get('by_subsystem_path') or {}).items():
        n = buckets.get(subsystem)
        if n:
            phases[phase] = n
    return {'total': sum(phases.values()), 'phases': dict(sorted(phases.items()))}


def emits_keys(owned, graph):
    """Key types these contracts are recorded as producing, per the generated key graph."""
    out = set()
    for kt, v in (graph.get('keys') or {}).items():
        if not v.get('well_formed'):
            continue
        if set(v.get('producers') or []) & set(owned):
            out.add(kt)
    return sorted(out)


SECTION_RE = re.compile(r'^## (\d)\. ', re.M)


def skeleton_facts(relpath):
    """Parse the authored skeleton: its section-1 names and its section-7 gap count."""
    path = os.path.join(ROOT, relpath)
    if not os.path.isfile(path):
        return None
    text = _read(path)
    bounds = [(int(m.group(1)), m.start()) for m in SECTION_RE.finditer(text)]
    spans = {}
    for i, (num, pos) in enumerate(bounds):
        end = bounds[i + 1][1] if i + 1 < len(bounds) else len(text)
        spans[num] = text[pos:end]
    gaps = spans.get(7, '')
    gap_rows = [ln for ln in gaps.splitlines()
                if ln.startswith('|') and not re.match(r'^\|[\s|:-]+\|$', ln)]
    gap_rows = [ln for ln in gap_rows if 'Evidence' not in ln and '---' not in ln]
    return {'text': text, 'entry_section': spans.get(1, ''), 'gap_count': max(0, len(gap_rows) - 1)}


def coverage(subsystem, skel):
    """Public callables in the code home that the authored skeleton never names.

    CANDIDATES, not defects. Section 1 lists what an outside caller can enter through, which is
    narrower than every public def — a helper class or an internal factory legitimately never
    appears. But this is precisely where hand-tracing drops things, and unlike a human it costs
    nothing to recompute. Matched against the WHOLE skeleton, not just section 1, so a callable
    discussed anywhere (a flow step, a gap row) counts as covered.
    """
    missing = []
    files = code_files(subsystem)
    total = 0
    for rel in files:
        for name, lineno in public_callables(rel):
            total += 1
            # No skeleton at all => nothing is named. Reporting zeros here instead would make an
            # untraced subsystem look identical to a fully-covered one.
            if skel is None or not re.search(r'\b' + re.escape(name) + r'\b', skel['text']):
                missing.append({'name': name, 'at': f'{rel}:{lineno}'})
    missing.sort(key=lambda d: (d['at'], d['name']))
    return {'public': total, 'unnamed': missing, 'files': len(files)}


def build_rows():
    """One row per subsystem that EXISTS, plus a drift record for everything that does not line up.

    Robust to future edits in both directions, which is the whole point:
      * a NEW folder with no roster row still gets a row (marked undeclared) — additions are never
        silently skipped;
      * a DELETED folder that still has a roster row is reported, not crashed on;
      * a contract owned by no subsystem is reported;
      * a trace bucket matching no subsystem is reported.
    Nothing here is a hardcoded subsystem list.
    """
    contracts, graph, emap, trace, absent = load_inputs()
    nomen = nomenclature_audit(contracts, graph)
    declared = {r['subsystem']: r for r in roster()}
    on_disk = discovered_subsystems()

    rows = []
    for sub in on_disk:
        meta = declared.get(sub)
        skel_rel = meta['skeleton'] if meta else f'systems/{sub}/{sub}_flow_skeleton_v1.md'
        skel = skeleton_facts(skel_rel)
        owned_src = contracts_for(sub, contracts, emap, graph, skel)
        owned = sorted(owned_src)
        rows.append({
            'subsystem': sub,
            'lane': (meta or {}).get('lane', '—'),
            'declared_in_roster': meta is not None,
            'skeleton': skel_rel,
            'skeleton_present': skel is not None,
            'code_files': len(code_files(sub)),
            'contracts': owned,
            'contract_provenance': owned_src,
            'build': {m: (emap.get('modules', {}).get(m) or {}).get('build') for m in owned},
            'executes_flag': {m: (emap.get('modules', {}).get(m) or {}).get('executes')
                              for m in owned},
            'trace': reachability(sub, trace),
            'emits': emits_keys(owned, graph),
            'gap_count': (skel or {}).get('gap_count', 0),
            'coverage': coverage(sub, skel),
        })

    known = set(on_disk)
    mapped = {c for r in rows for c in r['contracts']}
    all_contracts = {m.get('module') for m in (contracts.get('modules') or []) if m.get('module')}
    trace_buckets = {b for buckets in (trace.get('by_subsystem_path') or {}).values()
                     for b in buckets}

    drift = {
        'absent_inputs': sorted(absent),
        'folders_without_roster_row': sorted(known - set(declared)),
        'roster_rows_without_folder': sorted(set(declared) - known),
        'roster_rows_without_skeleton': sorted(
            r['subsystem'] for r in rows if r['declared_in_roster'] and not r['skeleton_present']),
        'contracts_owned_by_no_subsystem': sorted(all_contracts - mapped),
        'trace_buckets_matching_no_subsystem': sorted(trace_buckets - known),
    }
    return rows, drift, nomen


SCAN_ROOTS = ('systems', 'engine', 'references', 'registers', 'tools')
SCAN_EXT = ('.py', '.md', '.yaml', '.yml')


def nomenclature_audit(contracts, graph):
    """Measure whether each canonical identifier can actually be FOUND by searching for it.

    A canonical name is only useful as a handle if searching for it returns its references and
    little else. Key types already satisfy this by construction — `scene.combat_resolved` is
    dotted and distinctive. Module contract names largely do NOT: `victory`, `audit`, `world` are
    ordinary words, so the token count is dominated by unrelated prose and identifiers, and a
    reader who greps one gets noise instead of a region.

    This does not assert a rule; it produces the evidence for one. `occurrences` is the raw count
    of the bare token across the corpus; `qualified` counts uses of a namespaced form
    (`contract:<name>`), the convention `_identifier_census.yaml` already uses with `key:`/`py:`.
    A name with a high raw count and no qualified form is un-findable today.
    """
    names = sorted({m.get('module') for m in (contracts.get('modules') or []) if m.get('module')})
    keys = sorted(k for k, v in (graph.get('keys') or {}).items() if v.get('well_formed'))

    counts = {n: 0 for n in names}
    qualified = {n: 0 for n in names}
    key_counts = {k: 0 for k in keys}
    word = {n: re.compile(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])') for n in names}
    qual = {n: re.compile(r'contract:' + re.escape(n)) for n in names}

    for root in SCAN_ROOTS:
        base = os.path.join(ROOT, root)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames if d != '__pycache__')
            for fn in sorted(filenames):
                if not fn.endswith(SCAN_EXT):
                    continue
                full = os.path.join(dirpath, fn)
                # Never scan our own output. Counting occurrences inside the generated file makes
                # the render self-referential: each build changes the counts, which changes the
                # file, which changes the counts — it never reaches a fixed point and `--check`
                # can never pass. Caught by test_atlas_is_current on the first run.
                if os.path.abspath(full) in (os.path.abspath(OUT_MD), os.path.abspath(OUT_JSON)):
                    continue
                try:
                    text = _read(full)
                except (UnicodeDecodeError, OSError):
                    continue
                for n in names:
                    if n in text:
                        counts[n] += len(word[n].findall(text))
                        qualified[n] += len(qual[n].findall(text))
                for k in keys:
                    if k in text:
                        key_counts[k] += text.count(k)

    return {
        'contracts': {n: {'occurrences': counts[n], 'qualified': qualified[n]} for n in names},
        'keys_median_occurrences': sorted(key_counts.values())[len(key_counts) // 2]
        if key_counts else 0,
        'contracts_median_occurrences': sorted(counts.values())[len(counts) // 2] if counts else 0,
    }


# ── render ───────────────────────────────────────────────────────────────────

def esc(t):
    return str(t).replace('|', '\\|')


def table(headers, rows):
    out = ['| ' + ' | '.join(headers) + ' |', '|' + '|'.join(['---'] * len(headers)) + '|']
    out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return out + ['']


def reached_label(row):
    """Three states, because 'no' hides the distinction that matters most.

    A subsystem the trace never touched is not the same as one that has no code to touch; and a
    subsystem reached only behind a default-off flag is a third thing again. The trace measures
    one seeded campaign, so `never` means "not in that run", never "unreachable in principle" —
    the authored skeleton is what rules on reachability in principle.
    """
    if row['code_files'] == 0:
        return 'no code'
    return f"**yes** ({row['trace']['total']:,} calls)" if row['trace']['total'] else 'not in trace'


def render(rows, drift, nomen):
    L = ['# Valoria — Engine Atlas (generated)', '', BANNER, '']
    L += [f'**{len(rows)} subsystems** · sources: `module_contracts.yaml`, `key_graph.json`, '
          '`execution_map.json`, `execution_trace.json`, and the authored flow skeletons.', '']
    problems = {k: v for k, v in drift.items() if v}
    L += ['---', '', '## 0. This document\'s own coverage', '']
    if not problems:
        L += ['Every subsystem folder on disk has a roster row and a flow skeleton; every module '
              'contract maps to a subsystem; every execution-trace bucket matches one; every '
              'input file was present. Nothing is being silently skipped.', '']
    else:
        L += ['⚠ The generator reconciles the **filesystem** (what exists) against the **roster** '
              '(what is declared) and its inputs. These did not line up, and are reported rather '
              'than silently resolved — a generated atlas that quietly drops a new subsystem is '
              'worse than no atlas.', '']
        labels = {
            'absent_inputs': 'Input file absent — figures that depend on it are NOT findings',
            'folders_without_roster_row': 'Subsystem folder on disk with no roster row (an '
                                          'ADDITION the roster has not caught up with)',
            'roster_rows_without_folder': 'Roster row whose folder is gone (a DELETION)',
            'roster_rows_without_skeleton': 'Declared subsystem with no authored flow skeleton',
            'contracts_owned_by_no_subsystem': 'Module contract mapping to no subsystem folder',
            'trace_buckets_matching_no_subsystem': 'Execution-trace bucket matching no subsystem '
                                                   '(engine-level paths are expected here)',
        }
        L += table(['reconciliation', 'items'],
                   [[labels.get(k, k), ', '.join(f'`{esc(x)}`' for x in v)]
                    for k, v in problems.items()])
    L += ['---', '', '## 1. Subsystem atlas', '']
    L += ['`reached` is measured from ONE seeded campaign (`references/execution_trace.json`). '
          '"not in trace" means that run did not call it — not that it is unreachable; the '
          'authored skeleton rules on reachability in principle.', '']
    L += table(
        ['subsystem', 'lane', '.py', 'contracts', 'reached', 'emits keys', 'gaps', 'flow skeleton'],
        [[f"`{r['subsystem']}`", r['lane'], r['code_files'],
          ', '.join(f'[`{c}`](CONTRACT_INDEX.md#{c})' for c in r['contracts']) or '—',
          reached_label(r), len(r['emits']) or '—', r['gap_count'],
          f"[skeleton](../{r['skeleton']})"] for r in rows])

    L += ['## 2. Declared vs executed', '']
    L += ['Each contract\'s declared `build`/`executes` status beside what the trace measured. A '
          'disagreement here is a finding, not noise: it means the status field and the run '
          'disagree about the same module.', '']
    dv = []
    for r in rows:
        for m in r['contracts']:
            dv.append([f'`{m}`', f"`{r['subsystem']}`", esc(r['build'].get(m) or '—'),
                       str(r['executes_flag'].get(m)), reached_label(r)])
    L += table(['contract', 'subsystem', 'declared build', 'declared executes', 'trace'], dv)

    L += ['## 3. Authored-coverage check', '']
    L += ['Public top-level callables in each subsystem folder that its authored skeleton never '
          'names, found by AST. **These are candidates, not defects** — a flow skeleton lists what '
          'an outside caller can enter through, which is narrower than every public def, so a '
          'helper legitimately never appears. The list matters because this is exactly where '
          'hand-tracing drops things, and recomputing it is free.', '']
    L += table(['subsystem', 'public callables', 'not named in skeleton'],
               [[f"`{r['subsystem']}`", r['coverage']['public'], len(r['coverage']['unnamed'])]
                for r in rows])
    for r in rows:
        un = r['coverage']['unnamed']
        if not un:
            continue
        L += [f"<details><summary><b>{r['subsystem']}</b> — {len(un)} unnamed</summary>", '']
        L += table(['callable', 'at'], [[f"`{u['name']}`", f"`{u['at']}`"] for u in un])
        L += ['</details>', '']

    total_un = sum(len(r['coverage']['unnamed']) for r in rows)
    total_pub = sum(r['coverage']['public'] for r in rows)
    named = total_pub - total_un
    pct = (100.0 * named / total_pub) if total_pub else 0.0
    L += [f'**Corpus coverage:** {named} of {total_pub} public callables '
          f'({pct:.1f}%) are named by an authored skeleton.', '']

    adopted = [r['subsystem'] for r in rows
               if 'declared' in {w for v in r['contract_provenance'].values() for w in v}]
    L += ['## 4. Attribution provenance', '']
    L += ['How each contract was attributed to its subsystem. `declared` is a package-level '
          f'`{METAKEY}` metakey — the only source that survives a file move; the rest are '
          'inferred. Adoption is voluntary, so this line is the adoption meter, not a failure: '
          f'**{len(adopted)} of {len(rows)}** subsystems declare.', '']
    prov = []
    for r in rows:
        for c, why in sorted(r['contract_provenance'].items()):
            prov.append([f'`{c}`', f"`{r['subsystem']}`", ', '.join(f'`{w}`' for w in why)])
    L += table(['contract', 'subsystem', 'attributed by'], prov)

    L += ['## 5. Nomenclature — can a canonical name be found by searching for it?', '']
    L += ['A canonical identifier is only a usable handle if searching for it returns its '
          'references and little else. **Key types satisfy this by construction** — dotted and '
          'distinctive, median '
          f"{nomen['keys_median_occurrences']} occurrence(s). **Contract names largely do not**: "
          'several are ordinary English words, so the count below is dominated by unrelated prose '
          f"and identifiers (median {nomen['contracts_median_occurrences']}). "
          'This is evidence for a naming rule, not the rule itself — nothing is enforced here.', '']
    L += ['`qualified` counts uses of a namespaced form (`contract:<name>`), the convention '
          '`_identifier_census.yaml` already uses with `key:`/`py:`. A name with a high raw count '
          'and zero qualified uses cannot be located by search today.', '']
    worst = sorted(nomen['contracts'].items(), key=lambda kv: -kv[1]['occurrences'])[:12]
    L += table(['contract', 'bare occurrences', 'qualified uses'],
               [[f'`{n}`', v['occurrences'], v['qualified']] for n, v in worst])
    return '\n'.join(L) + '\n'


def build():
    rows, drift, nomen = build_rows()
    payload = {
        '_generated': ('GENERATED by tools/build_engine_atlas.py — the countable half of the '
                       'engine atlas. Do not hand-edit.'),
        'schema_version': 1,
        'subsystems': rows,
        'drift': drift,
        'nomenclature': nomen,
    }
    return {OUT_MD: render(rows, drift, nomen), OUT_JSON: json.dumps(payload, indent=1, sort_keys=True) + '\n'}


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true',
                    help='exit 1 if a committed file differs from a fresh render')
    args = ap.parse_args(argv)

    docs = build()
    stale = []
    for path, text in docs.items():
        rel = os.path.relpath(path, ROOT)
        if args.check:
            current = _read(path) if os.path.exists(path) else None
            if current != text:
                stale.append(rel)
        else:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(text)
            print(f'[engine-atlas] {len(text.splitlines()):>6} lines  ->  {rel}')
    if args.check:
        if stale:
            print('\n[engine-atlas] STALE: ' + ', '.join(stale))
            print('  regenerate with `python tools/build_engine_atlas.py` and commit')
            return 1
        print('[engine-atlas] atlas is current')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
