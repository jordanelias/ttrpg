#!/usr/bin/env python3
"""
registry.py — the unifying reader for Valoria's name/descriptor/quantity vocabulary.

FACADE, NOT A NEW SOURCE OF DATA. This module resolves a `term` by DELEGATING to the three
existing resolvers that already own their respective YAML files:

    tools/names.py               -- reads references/names_index.yaml (canonical display names)
    tools/descriptor_registry.py -- reads references/descriptor_registry.yaml (attribute descriptors)
    tools/quantity_registry.py   -- merges descriptor_registry.yaml + names_index.yaml

It imports those three modules BY MODULE (never re-parses their YAML, never reimplements
their resolution logic — CLAUDE.md §8: "every rule lives once, ... never re-implement a
rule") and exposes ONE reader interface on top: resolve() / resolves() / all_known().

THIS IS STEP ONE OF WS1 ("one registry, one reader"), NOT THE END STATE. As of this
writing:
  - NOTHING MOVES. references/names_index.yaml, references/descriptor_registry.yaml, and
    the merge logic inside tools/quantity_registry.py stay exactly where they are, byte-
    for-byte unmodified. No existing file's behavior changes.
  - This module only adds a READ-side facade in front of them.
The eventual WS1 end-state (see references/registry/README.md — PROPOSED, not built, no
data in it yet) flips this: vocabulary data moves into references/registry/*.yaml, and
names.py / descriptor_registry.py / quantity_registry.py become thin backward-compatible
SHIMS over THIS reader instead of the other way around. That flip is a later, separate,
higher-blast-radius checkpoint — not this one.

CONTRACT:
  - Working-tree only: no network, no GitHub API (CLAUDE.md §2) — everything this module
    touches is a local import + local file read.
  - stdlib + PyYAML only (PyYAML is used transitively, inside the delegated modules) — no
    new dependency introduced here.
  - Deterministic: control flow never depends on dict/set iteration order. Where a result
    enumerates over an unordered collection internally, order does not affect WHICH members
    end up in the result (see all_known(), a plain set union). all_known() itself returns a
    set (order not meaningful by construction) — sort at the call site if stable output is
    needed.
  - MEASURES / RESOLVES only. Like the three modules it wraps, this module never blocks a
    commit, never exits nonzero, never gates CI — it only answers "what does this term
    resolve to." Gating stays in tools/ci_*.py; this is a pure read-side facade.

PRECEDENCE — resolve() tries the three resolvers in this fixed order, and keeps every
resolver's hit (not just the winning one) so a disagreement can be surfaced rather than
silently swallowed:

  1. descriptor_registry  -> kind='descriptor'
     The narrowest, single-purpose owning parser of descriptor_registry.yaml's ATTRIBUTE
     section (the 9-attribute body/mind/social roster). Checked first because it is the
     ONLY one of the three that can resolve a bare STRUCTURAL KEY (e.g.
     "attr.body.strength"), not just a display name/alias — the most unambiguous form a
     caller can pass — and because descriptor_registry.yaml is the direct, unmirrored
     owner of that data: nothing is more authoritative for an attribute specifically.

  2. names                -> kind='name'
     references/names_index.yaml is documented (names.py's own docstring) as "the one
     place a definition's display name lives," resolved via an EXACT (case-sensitive)
     canonical/alias string match against a deliberately curated index. It MIRRORS
     descriptor_registry.yaml's attr/agg/fac/set sections (kept in sync by
     tools/ci_names_consistency.py) and ALSO carries entries that live only there: proper
     nouns (world.*, e.g. "Solmund"), clocks, tracks, mechanics, mass-combat stats. Checked
     second: a precise, deliberately-registered hit, but not as narrowly authoritative as
     descriptor_registry for the attribute domain specifically.

  3. quantity_registry     -> kind='quantity'
     The broadest, most permissive resolver: a best-effort, case-insensitive,
     punctuation/suffix-normalizing merge of ALL of descriptor_registry.yaml (attributes,
     aggregates, faction_stats, practitioner_stats, territory_stats, settlement_stats,
     by_reference, not_descriptors) PLUS names_index.yaml. Checked LAST, as the catch-all:
     empirically (verified by hand, not assumed — see test_registry.py), it is the ONLY one
     of the three that reaches practitioner_stats/territory_stats terms such as "Thread
     Sensitivity" or "Fort Level" — sections descriptor_registry.resolve() itself never
     searches (it only scans body/mind/social attributes) and names_index.yaml does not
     mirror (its own header comment lists only attr./agg./fac./set. as mirrored) — and the
     only one that tolerates messy input forms (parenthetical annotations, "Track"/"Pool"
     suffixes, underscores).

  Net effect ("quantity/descriptor keys before free names"): the two registries that carry
  a genuine, narrow, structural KEY namespace — descriptor_registry directly, and
  quantity_registry as its broadened merge — bracket names.py's free-form display-name
  match, with descriptor_registry (the most specific) winning first. Where more than one
  resolver answers a term they usually AGREE (they mirror the same YAML), and where they
  genuinely differ this facade DISCLOSES it via the 'disagreement' field rather than
  silently picking a winner — a real, LIVE instance exists today ("Thread Fatigue":
  names -> thread.thread_fatigue vs quantity_registry -> matched-but-keyless; pinned in
  test_registry.py, so the mechanism is exercised against real corpus data, not only a
  synthetic monkeypatch).

  STRUCTURAL-KEY COVERAGE + COLLISION SURFACING (WS1 antagonist findings ED-IN-0057, closed
  ED-IN-0058):
  * BARE STRUCTURAL KEYS — RESOLVED. resolve() now covers the WHOLE descriptor_registry.yaml
    structural namespace: attributes via descriptor_registry.resolve() (reused, §8), and the
    fac./set./prac./terr./agg. sections' keys + names + aliases via the non-attribute structural
    index (_nonattr_structural_index). So 'fac.influence', 'set.legitimacy',
    'prac.thread_sensitivity', 'terr.fort_level' all resolve now (kind='descriptor', with a
    'section' tag), where before they returned None indistinguishably from "unknown". A
    structural term like "Fort"/"Wealth" therefore routes through the AUTHORITATIVE descriptor
    registry rather than quantity_registry's fuzzy merge.
  * ALIAS/CANONICAL STRING COLLISION — RESIDUAL, but the entity is reachable and the collision is
    SURFACED. "Influence" is both an alias of attr.social.charisma AND the canonical name of
    fac.influence; the attribute wins the string (checked first), so the STRING "Influence" still
    resolves to attr.social.charisma and no 'disagreement' fires (the loser is discarded upstream).
    BUT fac.influence is now reachable by its bare KEY (above), so the entity is no longer lost —
    and collisions() reports the residual string-ambiguity as the precise work-list the WS1 data
    fold-in must disambiguate (give fac.influence a non-colliding display pointer). Resolving the
    string itself is a data change (the fold-in), not a precedence fix in this read-only reader.

RETURN SHAPE — resolve(term) is either None (no resolver recognizes `term` at all) or:
    {
      'term': <the input term, unchanged>,
      'kind': 'descriptor' | 'name' | 'quantity',
      'key':  <canonical dotted registry key for a descriptor/quantity hit (e.g.
               'attr.body.strength'), or the canonical DISPLAY STRING for a name hit (e.g.
               'Solmund') — matching what each source resolver treats as its own "the
               answer": names.py's primary currency is display strings, not dotted keys>,
      'registry_key': <the dotted STRUCTURAL key — a uniform pointer across kinds: == 'key'
               for a descriptor/quantity hit; the names_index dotted key (e.g. 'world.solmund')
               for a NAME hit, which 'key' does not carry; None only for a keyless quantity hit>,
      'via':  'descriptor_registry' | 'names' | 'quantity_registry',
      'disagreement': [ {'kind':, 'key':, 'via':}, ... ],   # every OTHER resolver that also
                       # matched `term` but with a DIFFERENT key; [] when none — always
                       # present, so callers never need a defensive .get().
      'matched_as': <str>,   # ONLY present when via == 'quantity_registry': the exact known
                       # display form quantity_registry matched against, which can differ
                       # from `term` after its own candidate-normalization.
    }
"""
import os
import sys

_TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)

# The descriptor file, anchored to THIS file's location (repo root = parent of tools/), so
# resolve() is CWD-independent without depending on any one sibling module having imported.
_DESCRIPTOR_PATH = os.path.join(os.path.dirname(_TOOLS_DIR), 'references', 'descriptor_registry.yaml')

# Guard the delegate imports. names.py already wraps its own `import yaml` (it is reached by the
# edit-time hook, which must never crash on absent PyYAML); descriptor_registry.py /
# quantity_registry.py do a BARE `import yaml`, so without this guard `import registry` would
# hard-crash in a PyYAML-less context — strictly LESS robust than names.py, the very module this
# facade claims fault-tolerance parity with (WS1 antagonist finding, ED-IN-0057). A delegate that
# fails to import degrades to None and its _hit()/all_known() contribution is skipped, never raised.
import names                    # noqa: E402 -- references/names_index.yaml reader (reused by identity)
try:
    import descriptor_registry  # noqa: E402 -- references/descriptor_registry.yaml reader (by identity)
except Exception:               # pragma: no cover
    descriptor_registry = None
try:
    import quantity_registry    # noqa: E402 -- merged descriptor+names vocabulary reader (by identity)
except Exception:               # pragma: no cover
    quantity_registry = None

_UNSET = object()
_DESCRIPTOR_REG_CACHE = _UNSET   # descriptor_registry.load() output, parsed at most once per process
_NONATTR_INDEX_CACHE = _UNSET    # non-attribute structural index, rebuilt whenever the reg reloads


def _load_descriptor_reg():
    """Load descriptor_registry.yaml's dict via the REAL descriptor_registry.load(), cached.

    Reads `_DESCRIPTOR_PATH` (anchored to this file's __file__, CWD-independent) with
    `errors='replace'` — so a stray non-UTF-8 byte degrades to a replacement char instead of
    raising UnicodeDecodeError (a ValueError, NOT an OSError — the earlier `except OSError`
    let it escape and break the module's own "never raises" contract for EVERY term, since
    resolve() calls _descriptor_hit first regardless of input; WS1 antagonist finding,
    ED-IN-0057) — and hands the raw TEXT to descriptor_registry.load(), so the PARSING rule
    is reused, not retyped. Result cached at module scope (mirrors names.py /
    quantity_registry.py, which both cache; the un-cached version re-parsed the YAML on every
    single resolve()/all_known() call — a real, measured cost for a bulk-facing reader).

    Never raises: returns None on a missing file, an absent/failed descriptor_registry module,
    or any parse error (same fault-tolerance discipline as the three wrapped modules).
    """
    global _DESCRIPTOR_REG_CACHE, _NONATTR_INDEX_CACHE
    if _DESCRIPTOR_REG_CACHE is not _UNSET:
        return _DESCRIPTOR_REG_CACHE
    reg = None
    if descriptor_registry is not None:
        try:
            with open(_DESCRIPTOR_PATH, encoding='utf-8', errors='replace') as f:
                text = f.read()
            loaded = descriptor_registry.load(text=text)
            reg = loaded if isinstance(loaded, dict) else None
        except Exception:
            reg = None
    _DESCRIPTOR_REG_CACHE = reg
    _NONATTR_INDEX_CACHE = _UNSET   # force the structural index to rebuild against the fresh reg
    return reg


# descriptor_registry.yaml sections OTHER than `attributes` that carry keyed entries.
# descriptor_registry.resolve() scans ONLY `attributes`, so the fac./set./prac./terr./agg.
# structural namespace otherwise resolves through NOTHING (WS1 antagonist finding, ED-IN-0058).
# `by_reference` is excluded: its keys are wildcards (conv.*, axis.*), not concrete resolvable keys.
_NONATTR_KEYED_SECTIONS = ('aggregates', 'faction_stats', 'practitioner_stats',
                           'territory_stats', 'settlement_stats')


def _nonattr_structural_index(reg):
    """{lowercased term -> (key, section)} over every key / name / alias in the NON-attribute
    keyed sections of descriptor_registry.yaml. Cached (rebuilt when _load_descriptor_reg reloads).

    This is NEW coverage of a namespace no existing resolver reaches — NOT a reimplementation of
    the attribute rule, which stays delegated to descriptor_registry.resolve() (§8). Deterministic:
    sections are walked in a fixed order and the FIRST binding of a term wins, so the result never
    depends on dict iteration order."""
    global _NONATTR_INDEX_CACHE
    if _NONATTR_INDEX_CACHE is not _UNSET:
        return _NONATTR_INDEX_CACHE
    index = {}
    if isinstance(reg, dict):
        for section in _NONATTR_KEYED_SECTIONS:
            block = reg.get(section) or {}
            entries = block.get('entries') if isinstance(block, dict) else None
            for e in (entries or []):
                if not isinstance(e, dict) or not e.get('key'):
                    continue
                for form in [e['key'], e.get('name')] + list(e.get('aliases') or []):
                    if form:
                        index.setdefault(str(form).strip().lower(), (e['key'], section))
    _NONATTR_INDEX_CACHE = index
    return index


def _descriptor_hit(term):
    """Resolve `term` against descriptor_registry.yaml. First the ATTRIBUTE domain via the real
    descriptor_registry.resolve() (reused, §8); then — for the fac./set./prac./terr./agg.
    structural namespace descriptor_registry.resolve() does NOT scan — via the non-attribute
    structural index. None if unrecognized (including when the registry can't be loaded)."""
    reg = _load_descriptor_reg()
    if reg is None:
        return None
    try:
        entry = descriptor_registry.resolve(reg, term)
    except Exception:
        entry = None
    if entry:
        return {'kind': 'descriptor', 'key': entry.get('key'), 'via': 'descriptor_registry',
                'section': 'attributes'}
    hit = _nonattr_structural_index(reg).get(str(term).strip().lower())
    if hit is not None:
        key, section = hit
        return {'kind': 'descriptor', 'key': key, 'via': 'descriptor_registry', 'section': section}
    return None


def _names_hit(term):
    """Resolve `term` via the real names.key_for(); None if unregistered.

    The public 'key' carried on this hit is the CANONICAL DISPLAY STRING (names.py's own
    primary currency — e.g. 'Solmund'), but the dotted entries()-key returned by key_for()
    itself is kept under '_registry_key' so resolve() can compare it against a
    descriptor/quantity hit's dotted key on equal terms for disagreement detection.
    """
    registry_key = names.key_for(term)
    if registry_key is None:
        return None
    return {'kind': 'name', 'key': names.canonical(registry_key), 'via': 'names',
            '_registry_key': registry_key}


def _quantity_hit(term):
    """Resolve `term` via the real quantity_registry.resolve(); None if unmatched.

    `key` can legitimately be None even when this DID match the term — a not_descriptors
    entry (e.g. "Health", a recognized derived-value name with no registry-bound key).
    That still counts as a resolved hit: `matched_as` (not `key`) is quantity_registry's own
    "did we recognize this at all" signal.
    """
    if quantity_registry is None:
        return None
    matched, key = quantity_registry.resolve(term)
    if matched is None:
        return None
    return {'kind': 'quantity', 'key': key, 'via': 'quantity_registry', 'matched_as': matched}


def resolve(term):
    """Resolve `term` against the unified name/descriptor/quantity vocabulary.

    Tries descriptor_registry -> names -> quantity_registry, in that fixed order (see the
    module docstring's PRECEDENCE section for the full rationale) — but queries all three
    before returning, so that any OTHER resolver's differing answer can be disclosed via
    'disagreement' rather than silently discarded. Returns None if none of the three
    recognizes `term` at all.
    """
    if not isinstance(term, str) or not term.strip():
        return None

    hits = []  # [(hit_dict, comparison_key), ...] in FIXED precedence order
    d = _descriptor_hit(term)
    if d is not None:
        hits.append((d, d['key']))
    n = _names_hit(term)
    if n is not None:
        hits.append((n, n['_registry_key']))
    q = _quantity_hit(term)
    if q is not None:
        hits.append((q, q['key']))

    if not hits:
        return None

    winner, winner_cmp_key = hits[0]
    disagreement = []
    for hit, cmp_key in hits[1:]:
        if cmp_key != winner_cmp_key:
            disagreement.append({'kind': hit['kind'], 'key': hit['key'], 'via': hit['via']})

    result = {
        'term': term,
        'kind': winner['kind'],
        'key': winner['key'],
        # The dotted structural key — a UNIFORM NS2 pointer regardless of `kind`. Equal to
        # `key` for a descriptor/quantity hit; for a NAME hit it is the names_index dotted key
        # (e.g. 'world.solmund'), which `key` does NOT carry (that holds the display string).
        # None only when the winner is a quantity hit whose entry has no registry-bound key.
        'registry_key': winner_cmp_key,
        'via': winner['via'],
        'disagreement': disagreement,
    }
    if 'matched_as' in winner:
        result['matched_as'] = winner['matched_as']
    if 'section' in winner:
        result['section'] = winner['section']   # which descriptor_registry.yaml section owns the key
    return result


def resolves(term):
    """True if `term` resolves against any of the three registries. Thin convenience over
    resolve() — no independent logic."""
    return resolve(term) is not None


def all_known():
    """Union of every known display name / alias / structural key across all three
    resolvers, as a set. (Sort at the call site for stable/printable output — CLAUDE.md
    determinism note: a set's own iteration order is never relied on here or by callers.)
    """
    known = set()

    for _key, e in names.entries().items():
        if not isinstance(e, dict):
            continue
        c = e.get('canonical')
        if c:
            known.add(c)
        for a in (e.get('aliases') or []):
            if a:
                known.add(a)

    if quantity_registry is not None:
        known |= quantity_registry.all_known()

    reg = _load_descriptor_reg()
    if reg is not None:
        try:
            attrs = descriptor_registry.all_attributes(reg)
        except Exception:
            attrs = []
        for e in attrs:
            if not isinstance(e, dict):
                continue
            if e.get('key'):
                known.add(e['key'])
            if e.get('name'):
                known.add(e['name'])
            for a in (e.get('aliases') or []):
                if a:
                    known.add(a)
        # non-attribute structural namespace (fac./set./prac./terr./agg. — bare keys included,
        # which quantity_registry.all_known() does not carry since resolve() can't match a raw key)
        for section in _NONATTR_KEYED_SECTIONS:
            block = reg.get(section) or {}
            entries = block.get('entries') if isinstance(block, dict) else None
            for e in (entries or []):
                if not isinstance(e, dict) or not e.get('key'):
                    continue
                known.add(e['key'])
                if e.get('name'):
                    known.add(e['name'])
                for a in (e.get('aliases') or []):
                    if a:
                        known.add(a)

    return known


def collisions():
    """DIAGNOSTIC (not resolution): display strings / aliases bound to MORE THAN ONE structural key
    across descriptor_registry.yaml — the un-pointered ambiguities the WS1 data fold-in must resolve.
    The canonical instance is "influence" -> {attr.social.charisma, fac.influence}: an attribute
    alias and a faction-stat name collide on one string, so fac.influence is reachable by no display
    string (only by its bare key). Returns {lowercased term: sorted[keys]} for every term bound to
    >1 key — making the collisions the reader CANNOT auto-resolve VISIBLE (the precise work-list for
    the fold-in) rather than silently swallowed. Keys themselves are unique and excluded."""
    reg = _load_descriptor_reg()
    if reg is None:
        return {}
    term_keys = {}   # lowercased display term -> set(keys)
    try:
        attrs = descriptor_registry.all_attributes(reg)   # attribute rule reused, §8
    except Exception:
        attrs = []

    def _add(forms, key):
        for form in forms:
            if form:
                term_keys.setdefault(str(form).strip().lower(), set()).add(key)

    for e in attrs:
        if isinstance(e, dict) and e.get('key'):
            _add([e.get('name')] + list(e.get('aliases') or []), e['key'])
    for section in _NONATTR_KEYED_SECTIONS:
        block = reg.get(section) or {}
        entries = block.get('entries') if isinstance(block, dict) else None
        for e in (entries or []):
            if isinstance(e, dict) and e.get('key'):
                _add([e.get('name')] + list(e.get('aliases') or []), e['key'])
    return {t: sorted(ks) for t, ks in sorted(term_keys.items()) if len(ks) > 1}
