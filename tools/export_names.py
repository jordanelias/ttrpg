#!/usr/bin/env python3
"""Cook the canonical naming index so a TERM has one owner that reaches code.

WHY THIS EXISTS. `references/names_index.yaml` calls itself *"the one place a definition's name
lives"*, and until now it lived there for `tools/` only. MEASURED 2026-09-16: of the vocabulary
registers, exactly one arrow reached executable code -- `engine/season/data/cast.py`, which opened
the YAML itself and built a private alias map over `token_class: faction` rows. `alias_registry`'s
two apparent reads in `engine/substrate/descriptors.py` are a COMMENT and a DOCSTRING. Nothing under
`systems/` read any of them, so a naming ruling landed in `references/` and stopped there:
`systems/world/sim/npe.py` still generated NPCs affiliated to `'Church'` six days after Jordan
ruled the name is `Church of Solmund`, and `engine/tests/test_f7_smoke_oracle.py` pinned goldens on
the same stale string.

This is the sixth instance of the pattern `tools/export_world_initial_state.py` states in its own
docstring: ONE AUTHORED SURFACE, ONE EXPORTER, ONE ARTIFACT, ONE LEAF. The authored surface is
`references/names_index.yaml`; this cooks it into `engine/engine_params/names.json` behind a
blocking `--check`; `engine/substrate/names.py` is the single runtime reader, and being a substrate
leaf it is importable from `engine/` AND from `systems/` without either naming the other.

⚠ THE VALIDATION IS THE POINT, NOT THE TRANSPORT. Copying YAML into JSON buys nothing. What this
refuses is the shape that makes a term NON-IDEMPOTENT -- one string that a later session, reading
it cold, can resolve two ways:

FOUR ARE REFUSED -- a `SystemExit` here reds a blocking gate at authoring time rather than
surfacing as a wrong faction in a generated NPC:

  · an alias that maps to two different canonicals      -- resolution is a coin flip
  · an alias that is also somebody's canonical name     -- the name means itself and something else
  · a legacy tag that is also a live alias              -- deprecation that resolves anyway
  · a legacy tag that is another row's canonical name   -- a live name refused as deprecated

THE FOURTH IS RECORDED, NOT REFUSED, and the asymmetry is the honest part. Two entries claiming one
display string is real here and not a typo: `Order` is a Conviction AND a settlement stat,
`Stability` is a faction stat AND a mechanic. Refusing would force a merge that deletes a real
quantity, so they go into an `ambiguous` block and `engine/substrate/names.py` raises on resolving
one -- `descriptors.json`'s `unimplemented` precedent, which records a gap where an instrument
reads it instead of in a docstring nothing opens.

§4's rule (ED-IN-0179) is that a word read cold in a later session must yield the SAME meaning.
These five are that rule with a falsifier -- see `tests/valoria/test_names_chain.py`, which plants
each one and asserts the refusal.

Usage:
    python3 tools/export_names.py           # write the artifact
    python3 tools/export_names.py --check   # re-derive and diff (exit 1 on drift)
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
SRC = os.path.join(REPO, 'references', 'names_index.yaml')
OUT = os.path.join(REPO, 'engine', 'engine_params', 'names.json')


def _fail(msg):
    raise SystemExit(f'[names] {msg}')


def build():
    data = ci_common.load_yaml(SRC, default=None)
    if not data:
        _fail(f'cannot read {os.path.relpath(SRC, REPO)}')
    entries = data.get('entries') or {}
    if not entries:
        _fail('no `entries:` block. If it was emptied, restore it rather than deleting this '
              'exporter -- an empty naming index resolves every name to nothing, silently.')

    canonical: dict = {}      # key -> canonical
    aliases: dict = {}        # alias -> canonical
    legacy: dict = {}         # legacy tag -> canonical
    by_class: dict = {}       # token_class -> [canonical, ...]
    owner_of_canonical: dict = {}   # canonical -> key that declared it (first wins)
    ambiguous: dict = {}            # canonical -> [key, ...] when more than one claims it

    for key, row in sorted(entries.items()):
        if not isinstance(row, dict):
            continue
        canon = row.get('canonical')
        if not canon:
            _fail(f'entry {key!r} declares no `canonical:`. A row with no canonical name cannot '
                  f'be the owner of anything; delete it or name it.')
        canon = str(canon)
        # (3) two entries claiming the same canonical -- RECORDED, NOT FAILED, and the distinction
        # matters. `Stability` is `fac.stability` (a 0-7 faction stat) AND `mech.stability` (a
        # mechanic); they are two real quantities that share a display string, so "merge the rows"
        # would delete one. The file's own header offers `context:` for a colliding display, but
        # scopes it to PROSE matching (the §3.5 gate `vector_audit` reads) -- it does not tell a
        # caller which row owns the string. So the honest artifact is one that CANNOT resolve an
        # ambiguous name and says so, which is `descriptors.json`'s `unimplemented` precedent:
        # record the gap where an instrument reads it rather than guessing or deleting.
        if canon in owner_of_canonical:
            ambiguous.setdefault(canon, [owner_of_canonical[canon]]).append(key)
        else:
            owner_of_canonical[canon] = key
        canonical[key] = canon

        tc = row.get('token_class')
        if tc:
            by_class.setdefault(str(tc), []).append(canon)

        for a in (row.get('aliases') or []):
            a = str(a)
            # (1) an alias mapping to two canonicals
            if a in aliases and aliases[a] != canon:
                _fail(f'alias {a!r} resolves to BOTH {aliases[a]!r} and {canon!r}. A reader '
                      f'meeting {a!r} cold cannot tell which is meant, which is exactly the '
                      f'non-idempotence ED-IN-0179 forbids. Rename one, or drop the alias.')
            aliases[a] = canon

        for tag in (row.get('legacy') or []):
            legacy[str(tag)] = canon

    # (2) an alias that is also somebody's canonical
    for a, canon in sorted(aliases.items()):
        if a in owner_of_canonical and owner_of_canonical[a] != owner_of_canonical[canon]:
            _fail(f'{a!r} is an alias of {canon!r} AND the canonical name of '
                  f'{owner_of_canonical[a]!r}. The same string names two things; resolving it '
                  f'depends on which table you reach first.')

    # (4) a legacy tag that is also a live alias
    both = sorted(set(legacy) & set(aliases))
    if both:
        _fail(f'{both} are declared BOTH legacy and alias. A legacy tag is meant to stop '
              f'resolving; an alias resolves. Pick one per tag.')

    # (5) a legacy tag that is another row's CANONICAL name. Added 2026-09-16 -- an antagonist pass
    # found it as the unguarded fourth member of the family the three above enumerate, and the leaf
    # makes it bite: `names.py` tests LEGACY before CANONICAL, so a legacy tag colliding with a live
    # canonical would make `canonical_for()` RAISE on a name that is perfectly current. Nothing
    # triggers it today (the eight legacy tags collide with nothing), which is why it is cheap now.
    shadowed = sorted(t for t in legacy if t in owner_of_canonical)
    if shadowed:
        _fail(f'{shadowed} are declared LEGACY while also being another entry\'s canonical name. '
              f'engine/substrate/names.py checks legacy before canonical, so this would refuse a '
              f'live name as deprecated. Rename the legacy tag, or retire the row that claims it.')

    return {
        '_generated': 'tools/export_names.py — do not hand-edit; edit references/names_index.yaml',
        'schema_version': 1,
        'source': 'references/names_index.yaml',
        'registry_version': data.get('version'),
        'count': len(canonical),
        # Sorted because nothing iterates these for order -- unlike `world_initial_state`'s
        # faction table, whose order sets an RNG draw and must NOT be sorted. Checked, not assumed.
        'canonical': dict(sorted(canonical.items())),
        'aliases': dict(sorted(aliases.items())),
        'legacy': dict(sorted(legacy.items())),
        'by_class': {k: sorted(v) for k, v in sorted(by_class.items())},
        #: Display strings more than one entry claims. `engine/substrate/names.py` REFUSES to
        #: resolve these rather than returning whichever row it met first.
        'ambiguous': {k: sorted(v) for k, v in sorted(ambiguous.items())},
    }


def main(argv):
    text = json.dumps(build(), indent=2, sort_keys=False, ensure_ascii=False) + '\n'
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f'[names] MISSING {os.path.relpath(OUT, REPO)} — run without --check.')
            return 1
        if open(OUT, encoding='utf-8').read() != text:
            print(f'[names] DRIFT — {os.path.relpath(OUT, REPO)} is stale. '
                  f'Run: python3 tools/export_names.py')
            return 1
        d = json.loads(text)
        classes = ', '.join(f'{k}={len(v)}' for k, v in d['by_class'].items())
        amb = len(d['ambiguous'])
        print(f'[names] OK — {d["count"]} names, {len(d["aliases"])} aliases, '
              f'4 idempotence checks passed, {amb} display collision(s) recorded ({classes}).')
        return 0
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(text)
    print(f'[names] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
