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

WHAT IT DOES NOT DO. It does not resolve the roster disagreements it exposes; it RECORDS them, in
the same shape `export_game_constants.py` uses, because each needs a ruling and not a value edit:

  * `faction_stats` declares FIVE keys (influence, wealth, military, intel, stability). The Faction
    dataclass implements SIX fields (L, Sta, W, I, Mil, intel) — `L` (Legitimacy/Mandate) is written
    by 32 call sites and is declared NOWHERE in the registry. That is the 5-vs-6 half of the
    faction-stats packet awaiting Jordan (HANDOFF.md; plan Q1).
  * the registry's PER-STAT floors were ratified 2026-07-08 (ED-IN-0029, OPT-AV-14/D14 + OPT-AV-18):
    Influence floors at 1, the rest at 0. `Faction.adjust` (game_state.py:127-131) applies a BLANKET
    floor of 0.5 and ceiling of 7.0 to every stat, and no caller overrides it. **The ratified floors
    have never been implemented.** Wiring them moves the seeded goldens, so it is a separate,
    measured commit — not a side effect of adding this exporter.
  * `attributes` ships NINE and Jordan ruled 2026-08-14 that it will be TEN. The tenth is unnamed, so
    the export carries an explicit `pending_tenth` sentinel rather than silently shipping nine as if
    the roster were closed (plan Q2).

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
    'fac.influence': 'I',
    'fac.wealth':    'W',
    'fac.military':  'Mil',
    'fac.stability': 'Sta',
    'fac.intel':     'intel',
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
        'unimplemented': {
            'faction_L': {
                'what': "engine/autoload/game_state.py's Faction dataclass carries `L` "
                        "(Legitimacy/Mandate), written by 32 .adjust() call sites across engine/ and "
                        "systems/. references/descriptor_registry.yaml declares no entry for it.",
                'why_it_matters': 'The registry declares five faction stats; the code implements six. '
                                  'This is the 5-vs-6 half of the faction-stats packet.',
                'needs': 'ruling — is Legitimacy a base faction descriptor, or derived like Mandate?',
            },
            'per_stat_floors': {
                'what': 'The per-stat floors above were RATIFIED 2026-07-08 (ED-IN-0029, OPT-AV-14/D14 '
                        '+ OPT-AV-18): Influence floors at 1, the rest at 0. Faction.adjust '
                        '(game_state.py:127-131) applies a blanket floor of 0.5 and ceiling of 7.0 to '
                        'every stat, and none of its 32 callers overrides either.',
                'why_it_matters': 'A ratified canon decision that has never reached the executable '
                                  'model. Wiring it moves the seeded campaign goldens, so it is a '
                                  'separate measured commit, not a side effect of this export.',
                'needs': 'implementation with a measured golden delta',
            },
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
