#!/usr/bin/env python3
"""Cook references/descriptor_registry.yaml into data the ENGINE reads at runtime.

WHY THIS EXISTS.

`systems/` stems from `engine/` and `references/` (Jordan, 2026-08-20). Measured the same day,
`references/` was load-bearing on **tools and prose only**: no module under `engine/` or `systems/`
loaded `descriptor_registry.yaml` or `module_contracts.yaml` — every runtime hit was a comment or a
docstring — while the rosters the code actually runs on were HARDCODED TWINS in
`engine/autoload/game_state.py` (deleted at plan position `29b`, with the `fac.*` block). A registry
that only tools read is a document, not a root.

This is the writer half of making it a root. `engine/substrate/descriptors.py` is the reader, and it
is the single owner of "how the engine reads the registry" — nothing else parses the YAML.

WHAT IT EMITS, AND WHY DATA RATHER THAN A GENERATED MODULE. `engine/engine_params/descriptors.json`,
same shape as its four sibling exports: the markdown/YAML stays the AUTHORED, reviewable surface and
code reads the cooked artifact. Emitting a generated `.py` would put executable code in a directory
whose whole contract is "typed data the Godot port ingests", and would give the port nothing.

WHAT THE `unimplemented` BLOCK RECORDS. This tool does not resolve roster disagreements; it
RECORDS them in its `unimplemented` block, because each needs a ruling and not a value edit.

ITS LAST ROW, `fac_intel_multiplier`, DIED AT PLAN POSITION `29b` (2026-10-01) with `game_state.py`, the
`Faction` dataclass and the `fac.*` descriptor block it described; the block is empty again. The two it
carried before that (the 5-vs-6 faction-stat gap, the unimplemented per-stat floors) closed earlier and
died with the same block.

An EMPTY `unimplemented` block is the correct state when nothing is outstanding, and it is not a
licence to keep it empty: `tests/valoria/test_descriptors_runtime.py` pins the exact expected set,
so a silent addition fails as loudly as an unauthorised deletion. ⚠ AND THE EMPTY STATE IS NOT
EVIDENCE THE REGISTER IS COMPLETE — it was empty for three weeks while `fac.intel` was
outstanding. The pin catches what enters this block; nothing catches what never reaches it.

THE FACTION BLOCK IS GONE (29b, `ID-13`): this tool no longer cooks `faction_stats` or a field map, and
`engine/substrate/descriptors.py` no longer exposes a faction roster check.

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


def _conviction_roster(reg):
    """The 13 Convictions, from the registry. The SOLE machine-readable statement of the roster.

    Validated here rather than trusted: the count is declared alongside the names and they must
    agree, because a roster that silently loses a name is exactly how the two subsystem copies
    drifted apart in the first place.
    """
    block = reg.get('conviction_roster') or {}
    names = [n for n in (block.get('names') or []) if isinstance(n, str)]
    if not names:
        raise SystemExit('descriptor_registry.yaml: conviction_roster.names is missing or empty. '
                         'It is the single owner of the Conviction roster; two subsystems read it.')
    declared = block.get('count')
    if declared is not None and int(declared) != len(names):
        raise SystemExit(f'descriptor_registry.yaml: conviction_roster declares count={declared} '
                         f'but lists {len(names)} names. A roster whose own count disagrees with '
                         f'itself is how the 9-vs-8-vs-13 split started.')
    if len(set(names)) != len(names):
        raise SystemExit('descriptor_registry.yaml: conviction_roster.names contains duplicates.')
    return {'source': block.get('source'), 'count': len(names), 'names': names}


def _axis_roster(reg):
    """The 4 ethical axes, from the registry. The SOLE machine-readable statement of the name set.

    Validated exactly as `_conviction_roster` is, and for the same reason one level up: this set
    is what `engine/substrate/keys.py` validates a Key's axis names against AND what
    `engine/season/decision/choose.py` sums a candidate's score over. Before 2026-09-14 each held
    its own literal and nothing compared them, so the two could disagree in silence.
    """
    block = reg.get('axis_roster') or {}
    names = [n for n in (block.get('names') or []) if isinstance(n, str)]
    if not names:
        raise SystemExit('descriptor_registry.yaml: axis_roster.names is missing or empty. '
                         'It is the single owner of the ethical-axis set; the Key substrate and '
                         'the season engine both read it.')
    declared = block.get('count')
    if declared is not None and int(declared) != len(names):
        raise SystemExit(f'descriptor_registry.yaml: axis_roster declares count={declared} '
                         f'but lists {len(names)} names.')
    if len(set(names)) != len(names):
        raise SystemExit('descriptor_registry.yaml: axis_roster.names contains duplicates.')
    return {'source': block.get('source'), 'count': len(names),
            'scale': block.get('scale'), 'names': names}


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
        # THE CONVICTION ROSTER, centralized 2026-08-24. Enumerated in the registry rather than
        # left `by_reference` to a design document, because two subsystems had each invented their
        # own roster in the absence of one code could read — and the disagreement was costing a
        # ratified mechanic (a Close-Knot-break Scar that silently never landed).
        'conviction_roster': _conviction_roster(reg),
        # THE ETHICAL-AXIS ROSTER, centralized 2026-09-14 (ED-IN-0230). Same move as the line
        # above and after the same class of defect: `keys.py::AXES` and `rosters.yaml:
        # conviction_axes` each held a literal and NOTHING compared them, while the roster's own
        # note claimed a refusal that did not exist.
        'axis_roster': _axis_roster(reg),
        'settlement_stats': _section(reg, 'settlement_stats'),
        'practitioner_stats': _section(reg, 'practitioner_stats'),
        'territory_stats': _section(reg, 'territory_stats'),
        # ⚠ EMPTY, AND THAT IS A RESULT RATHER THAN A DELETION. This block carries RATIFIED canon decisions
        # the executable model has not implemented, each naming what it needs. Its last row,
        # `fac_intel_multiplier` (a multiplier for `fac.intel` in `engine.autoload.game_state.MULTS`), died at plan
        # position `29b` with `game_state.py`, `Faction` and the `fac.*` descriptor block it described. An empty
        # register is the correct state when nothing is outstanding and it is NOT a licence to keep it empty:
        # `tests/valoria/test_descriptors_runtime.py` pins the exact expected set, so an unauthorised deletion AND
        # a silent addition both fail there. ⚠ The empty state is not evidence the register is complete.
        'unimplemented': {},
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
              f'{len(d["unimplemented"])} unimplemented ratified item(s).')
        return 0
    with open(OUT, 'w') as fh:
        fh.write(text)
    print(f'[descriptors] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
