#!/usr/bin/env python3
"""Cook references/descriptor_registry.yaml into data the ENGINE reads at runtime.

WHY THIS EXISTS.

`systems/` stems from `engine/` and `references/` (Jordan, 2026-08-20). Measured the same day,
`references/` was load-bearing on **tools and prose only**: no module under `engine/` or `systems/`
loaded `descriptor_registry.yaml` or `module_contracts.yaml` — every runtime hit was a comment or a
docstring — while the rosters the code actually runs on were HARDCODED TWINS in
`engine/autoload/game_state.py` (`MULTS`, `ALL_PLAYABLE_15`, the `fac.*` field set). A registry that
only tools read is a document, not a root.

This is the writer half of making it a root. `engine/substrate/descriptors.py` is the reader, and it
is the single owner of "how the engine reads the registry" — nothing else parses the YAML.

WHAT IT EMITS, AND WHY DATA RATHER THAN A GENERATED MODULE. `engine/engine_params/descriptors.json`,
same shape as its four sibling exports: the markdown/YAML stays the AUTHORED, reviewable surface and
code reads the cooked artifact. Emitting a generated `.py` would put executable code in a directory
whose whole contract is "typed data the Godot port ingests", and would give the port nothing.

WHAT IT USED TO RECORD, AND WHY THAT SECTION IS NOW EMPTY. This tool does not resolve roster
disagreements; it RECORDS them in its `unimplemented` block, because each needs a ruling and not a
value edit. It carried two, and BOTH ARE NOW CLOSED:

  * THE 5-vs-6 GAP — `faction_stats` declared FIVE keys while the Faction dataclass implemented SIX
    fields, with `L` written by 20 of `.adjust()`'s 31 non-test call sites and declared NOWHERE.
    RULED 2026-08-23: Jordan ruled "Legitimacy is a base", so `fac.legitimacy` is declared, bound to
    `L` by `FACTION_KEY_TO_FIELD`, and the roster is SIX on both sides.
  * THE UNIMPLEMENTED FLOORS — ED-IN-0029 (2026-07-08) ratified per-stat floors that
    `Faction.adjust` ignored in favour of a blanket 0.5/7.0 for six weeks. WIRED 2026-08-22 (plan
    S5d), then partly superseded 2026-08-23 by "Influence can be 0", which replaced that docket's
    Influence floor of 1. All six stats floor at 0.

An EMPTY `unimplemented` block is the correct state when nothing is outstanding, and it is not a
licence to keep it empty: `tests/valoria/test_descriptors_runtime.py` pins the exact expected set,
so a silent addition fails as loudly as an unauthorised deletion.

Usage:
    python3 tools/export_descriptors.py           # write engine/engine_params/descriptors.json
    python3 tools/export_descriptors.py --check   # re-derive and diff vs committed (exit 1 on drift)
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
SRC = os.path.join(REPO, 'references', 'descriptor_registry.yaml')
OUT = os.path.join(REPO, 'engine', 'engine_params', 'descriptors.json')

# The registry writes bounds as a "lo-hi" string. One parser, here, so no reader re-invents it.
# `lo-hi`, and `lo-hi+` for an open ceiling (the registry uses e.g. "0-100+" for TS). One parser,
# here, so no reader re-invents it. Bracketed axis forms ("[-1,+1]") are NOT descriptors with
# numeric bounds in the sense the engine clamps on; they live under by_reference/not_descriptors and
# are not emitted by _section().
SCALE_RE = re.compile(r'^\s*(-?\d+(?:\.\d+)?)\s*-\s*(-?\d+(?:\.\d+)?)(\+?)\s*$')

# Registry key -> the field name the Faction dataclass actually uses. Hand-confirmed against
# engine/autoload/game_state.py:99-111 and MULTS at :45. `L` is deliberately absent: it has no
# registry entry at all, which is the finding, not an oversight here.
FACTION_KEY_TO_FIELD = {
    'fac.influence':  'I',
    'fac.legitimacy': 'L',   # Jordan 2026-08-23: "Legitimacy is a base." Six stats, not five.
    'fac.wealth':     'W',
    'fac.military':   'Mil',
    'fac.stability':  'Sta',
    'fac.intel':      'intel',
}


def _bounds(scale):
    # A missing scale is legitimate: some entries are registered for NAME and provenance only. Emit
    # nulls so a reader cannot clamp on a bound the registry never declared.
    if scale in (None, ''):
        return None, None, None
    m = SCALE_RE.match(str(scale))
    if not m:
        raise SystemExit(f'descriptor_registry.yaml: unparseable scale {scale!r}. '
                         f'Scales are written "lo-hi"; fix the registry or this parser, not both.')
    lo, hi, open_top = m.group(1), m.group(2), m.group(3)
    num = lambda s: float(s) if '.' in s else int(s)
    # An open ceiling ("0-100+") is a SOFT reference point, not a clamp. Returning the number would
    # let a reader clamp on it; returning None forces the reader to notice.
    return num(lo), (None if open_top else num(hi)), (num(hi) if open_top else None)


def _section(reg, name):
    out = {}
    for e in (reg.get(name) or {}).get('entries', []) or []:
        lo, hi, soft = _bounds(e.get('scale'))
        row = {'name': e.get('name'), 'floor': lo, 'ceiling': hi}
        if soft is not None:
            row['open_ceiling_reference'] = soft
        out[e['key']] = row
    return out


def build():
    reg = ci_common.load_yaml(SRC, default=None)
    if not reg:
        raise SystemExit(f'cannot read {os.path.relpath(SRC, REPO)}')

    attrs = reg.get('attributes') or {}
    a_lo, a_hi, _a_soft = _bounds(attrs.get('scale'))
    if a_lo is None:
        raise SystemExit('descriptor_registry.yaml: attributes.scale is missing. The attribute scale '
                         'is the one bound the engine clamps every character stat on; it may not be absent.')
    roster = []
    for domain in ('body', 'mind', 'social'):
        for key in (attrs.get(domain) or []):
            roster.append(key if isinstance(key, str) else key.get('key'))

    faction = _section(reg, 'faction_stats')

    return {
        '_generated': (
            'GENERATED by tools/export_descriptors.py from references/descriptor_registry.yaml. '
            'NEVER hand-edit: regenerate and commit together. Read at runtime by '
            'engine/substrate/descriptors.py, which is the SOLE reader — nothing else parses the YAML.'
        ),
        'schema_version': 1,
        'source': 'references/descriptor_registry.yaml',
        'registry_version': str(reg.get('version', '')),
        'registry_ratified': str(reg.get('ratified', '')),
        'attributes': {
            'scale': {'floor': a_lo, 'ceiling': a_hi},
            'default': attrs.get('default'),
            'roster': roster,
            'count': len(roster),
            'pending_tenth': (
                'Jordan ruled 2026-08-14 that the roster WILL BE 10 attributes. The registry ships '
                f'{len(roster)} and the tenth is UNNAMED. This sentinel exists so a reader cannot mistake '
                'the current roster for a closed one; delete it in the commit that names the tenth.'
            ) if len(roster) < 10 else None,
        },
        'faction_stats': faction,
        'faction_field_map': FACTION_KEY_TO_FIELD,
        'settlement_stats': _section(reg, 'settlement_stats'),
        'practitioner_stats': _section(reg, 'practitioner_stats'),
        'territory_stats': _section(reg, 'territory_stats'),
        # ⚠ EMPTY AS OF 2026-08-23, AND THAT IS A RESULT RATHER THAN A DELETION.
        # This block carried RATIFIED canon decisions the executable model had not implemented. Both
        # are now implemented and their rows are gone in the commits that implemented them:
        #   * `per_stat_floors` -- wired into Faction.adjust at plan S5d (2026-08-22).
        #   * `faction_L` -- Jordan ruled 2026-08-23 that Legitimacy IS a base descriptor, so it is
        #     declared in references/descriptor_registry.yaml and bound to the `L` field above.
        # An empty register is the correct state when nothing is outstanding. It is NOT a licence to
        # keep it empty: `tests/valoria/test_descriptors_runtime.py` pins the exact expected set, so
        # both an unauthorised deletion AND a silent addition fail there.
        'unimplemented': {
        },
    }


def main(argv):
    text = json.dumps(build(), indent=2, sort_keys=False) + '\n'
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f'[descriptors] MISSING {os.path.relpath(OUT, REPO)} — run without --check.')
            return 1
        if open(OUT).read() != text:
            print(f'[descriptors] DRIFT — {os.path.relpath(OUT, REPO)} is stale. '
                  f'Run: python3 tools/export_descriptors.py')
            return 1
        d = json.loads(text)
        print(f'[descriptors] OK — {d["attributes"]["count"]} attribute(s), '
              f'{len(d["faction_stats"])} faction stat(s), '
              f'{len(d["unimplemented"])} unimplemented ratified item(s).')
        return 0
    with open(OUT, 'w') as fh:
        fh.write(text)
    print(f'[descriptors] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
