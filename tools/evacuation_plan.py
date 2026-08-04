#!/usr/bin/env python3
"""Compute the keep/evacuate partition of the working tree, and what each slice would break.

WHY THIS EXISTS, and why it is a tool rather than a table in a document.

`tools/build_fork.py` carries `CARRY` and `LEAVE`. They read like a partition and are not one:
`CARRY | LEAVE` leaves a large NEITHER set -- `.github/`, `.githooks/`, `.claude/`, `tools/`,
`tests/valoria/`, most of `references/`, `research/`, `skills/`, `CLAUDE.md`, `CURRENT.md`,
`HANDOFF.md`. Under EXTRACT (copy CARRY into an empty tree) the neither-set silently defaults to
left-behind, which is harmless. Under EVACUATE -- the ruled direction, ED-IN-0125 -- the mirror
operation "git rm everything not in CARRY" DELETES it, taking the enforcement tier, the shipping
gate and the session protocol with it. The defect is not in either list; it is in the assumption
that two lists cover the tree. So the first thing this tool does is REFUSE to emit a plan unless
the partition is total and disjoint over every tracked file (`--check` fails otherwise).

THE RULE (Jordan, 2026-08-04, ED-IN-0125). It cuts on OUTDATED, not on format:
  * prose with NO code pair   -> KEEP, and it IS the spec (canon/, the no-oracle module specs)
  * prose WITH a code pair    -> KEEP as information only; code wins (principle 7 / ED-1050)
  * neither                   -> EVACUATE (session audits, generated narrative, process boards)
Plus a second filter, because age alone fails: a 36 MB render directory six days old passes a
two-week rule. GENERATED ARTIFACTS EVACUATE; THEIR GENERATORS STAY.

WHAT "BREAKS" MEANS HERE. Deleting a tree is not the risky part; deleting it while something kept
still reads it is. So every evacuation candidate is reported with its READERS among kept files,
split into `blocking` (executable surfaces -- tools/, tests/valoria/, .github/, .githooks/,
.claude/) and `prose` (a mention in a kept document, which needs an alias row, not a code change).
A slice is ready when its blocking readers are zero or are retired in the same commit. That is the
auditable-deletion property that made evacuation preferable to extraction in the first place.

NOT A DELETER. This tool computes and reports. It never removes a file.

Usage:
    python3 tools/evacuation_plan.py                 # human report
    python3 tools/evacuation_plan.py --json          # write references/evacuation_manifest.json
    python3 tools/evacuation_plan.py --check         # partition totality + contract guard; exit 1 on fail
    python3 tools/evacuation_plan.py --slice audit   # one root in detail, with its readers
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:
    yaml = None

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The audit cutoff. Jordan first set a two-week rule ("we aren't keeping any older than two
# weeks", 2026-07-21) then widened it to the calendar month: "probably keep audits from july
# overall" (2026-08-04). July is the period the current architecture was built in, so the widening
# buys continuity of reasoning rather than volume for its own sake.
# Expressed as a date string so the rule is inspectable rather than a computed "now" that would
# make this tool's output depend on when it ran -- a silent nondeterminism in a deletion planner.
AUDIT_CUTOFF = "2026-07-01"

# Generated artefacts. The GENERATOR stays, the OUTPUT goes -- Jordan wants mass-battle and
# grid-scene visualisation, so `.py` under a render directory is kept by rule R-AUDIT-GEN below.
GENERATED_EXT = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf', '.html')

# proposals/ is per-file: some are load-bearing on kept code, most are not (ED-IN-0127 §6).
PROPOSALS_KEEP = {
    'valoria_fork_plan_of_record_v1.md',        # the plan governing this very operation
    'repo-reorganization-v1.md',                # RATIFIED, execution pending
    'pc_formation_system.md',                   # engine half BUILT; §8 residual
    'weapon_physics_and_concentration_model.md',  # §§1-6 BUILT; §7 the only spec of an unbuilt mechanic
    'mass_battle_fighting_withdrawal_v1.md',    # BUILT (gated); residuals attach to kept code
    'multiunit_envelopment_plan.md',            # held design decision on the kept MB engine
    '2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md',
    'grounded_event_card_deck_v1.md',
}

# RELOCATION. A third verdict, because keep/evacuate cannot express "this is ours, but it is filed
# in the wrong place". Jordan, 2026-08-04: "visualization tool for mb should be moved to mb and
# wiring should be to systems folder."
#
# The MB visualisation + measurement instruments are subsystem tooling that happens to sit in the
# audit corpus and in research/: `measure_colocation.py` is the STANDING measurement behind
# ED-MB-0056/0059, not a session record. Keeping them where they are would either strand real
# instruments in an evacuating tree, or force a keep-rule broad enough to drag ~78 stale one-off
# sims along with them. Moving them to the subsystem is the RULED §2a shape -- one subsystem = one
# folder -- and `systems/combat/combat_engine_v1/workbench/` (balance.py, build_levers.py,
# catalogue.py, armour_participation.py) is the established precedent for the instrument tier.
#
# Their RENDERED OUTPUT does not travel: R-AUDIT-GEN evacuates it, and it regenerates from the
# relocated source. (matcher(rel) -> bool, destination-dir, rule-id, reason)
RELOCATE = [
    (lambda p: p.startswith('audit/2026-07-29-scenario-visualization/') and p.endswith('.py'),
     'systems/mass_battle/workbench/', 'R-REL-MBVIZ',
     'MB scenario visualisation + co-location measurement -- subsystem instruments, not audit records'),
    (lambda p: p.startswith('research/diagrams/mass_battle_formations/') and p.endswith('.py'),
     'systems/mass_battle/workbench/', 'R-REL-MBDIAG',
     'MB formation-diagram generators -- the same instrument class, filed under research/'),
]


def relocation(rel: str):
    """Destination for a file that stays but belongs in a subsystem home. None if it stays put."""
    for matcher, dest, rule_id, reason in RELOCATE:
        if matcher(rel):
            return dest + os.path.basename(rel), rule_id, reason
    return None


# ORDERED rules. FIRST MATCH WINS, so the specific precedes the general. Every rule carries the
# reason it will print, because a deletion plan whose rows cannot be argued with is not reviewable.
# (matcher(rel) -> bool, verdict, rule-id, reason)
RULES = [
    # ---- relocation is checked FIRST: these files are kept, and their destination is the point.
    (lambda p: relocation(p) is not None, 'relocate', 'R-RELOCATE',
     'kept, but moved to its subsystem home -- see the RELOCATE table'),

    # ---- inside an evacuating parent, but KEEP (this is why the cut is per-file, not per-root)
    (lambda p: p.startswith('tests/sim/mass_battle/'), 'keep', 'R-MB-CANON',
     'the CANON mass-battle engine (J2/ED-MB-0064) -- 28 .py, zero .md, misfiled under tests/'),
    (lambda p: p.startswith('tests/sim/v32-combat-balance/'), 'keep', 'R-PARITY',
     'the numpy-free parity oracle the sigma kernel validates against'),
    (lambda p: p.startswith('tests/valoria/'), 'keep', 'R-SHIPGATE',
     'the shipping gate (CLAUDE.md 0.1) and the home of the fork plan\'s own falsifiers'),
    (lambda p: p == 'tests/coverage_matrix.md', 'keep', 'R-COVMATRIX',
     'read by ci_co_file_checker rule 3 -- retiring it is a gate change, not a prose deletion'),

    # ---- tests/ otherwise: stress corpora and narrative prose, neither code pair nor spec
    (lambda p: p.startswith('tests/'), 'evacuate', 'R-TESTS-PROSE',
     'stress/session prose under tests/ -- neither executable spec nor canon'),

    # ---- audit/: generated output goes, generators stay, then the two-week rule
    (lambda p: p.startswith('audit/') and p.lower().endswith(GENERATED_EXT), 'evacuate',
     'R-AUDIT-GEN',
     'generated artefact -- regenerable output, evacuates at ANY date; its generator is kept by '
     'R-AUDIT-RECENT if the session is inside the window'),
    # NOTE: there is deliberately NO "keep every .py under audit/" rule. The first draft had one,
    # justified by the FOUR visualisation generators in audit/2026-07-29-scenario-visualization/
    # that Jordan wants kept -- and it fired on 82 files, ~78 of which are one-off April/May session
    # sims (mc_v10.py, pp686_sim.py, stage10_articulation_sim.py). A keep-rule 20x broader than its
    # justification is how a "streamlined" repo quietly keeps its detritus. Ordering does the job
    # instead: R-AUDIT-GEN evacuates rendered output at any date, then the ordinary two-week rule
    # applies to source, so generators inside the window are kept BECAUSE their session is current
    # and stale one-off sims leave with their session.
    (lambda p: _audit_is_recent(p), 'keep', 'R-AUDIT-RECENT',
     f'audit dated on/after {AUDIT_CUTOFF} (two-week rule) -- includes generators in-window'),
    (lambda p: p.startswith('audit/'), 'evacuate', 'R-AUDIT-STALE',
     f'audit older than {AUDIT_CUTOFF}, or undated -- process record, not canon'),

    # ---- prose WITH a code pair: stays, demoted to information only
    (lambda p: p.startswith('engine/params/'), 'keep', 'R-PARAMS-INFO',
     'prose WITH a code pair -> information only (ED-1050). Zero runtime readers but ~50 '
     'provenance referents from kept code; deleting it orphans them'),

    # ---- prose with NO code pair: stays, and it IS the spec
    (lambda p: p.startswith('canon/'), 'keep', 'R-CANON',
     'philosophical canon P-01..P-14 -- prose with NO code pair, therefore authoritative'),

    # ---- code and the machinery that guards it
    (lambda p: p.startswith(('engine/', 'systems/')), 'keep', 'R-CODE', 'the executable model'),
    (lambda p: p.startswith(('tools/', '.github/', '.githooks/', '.claude/')), 'keep', 'R-INFRA',
     'infrastructure / compliance -- 99 of 102 tools are reachable; cut by SUBJECT, not orphan status'),
    (lambda p: p.startswith('references/'), 'keep', 'R-REGISTRIES',
     'the registries the tools read -- implied by "infrastructure/compliance tools"'),
    (lambda p: p.startswith('registers/'), 'keep', 'R-REGISTERS',
     'kept but RESTARTED (ED-IN-0127 §5): 103 kept files cite ED ids inline and 30 tools read this tree'),
    (lambda p: p.startswith('research/'), 'keep', 'R-RESEARCH', 'named in the keep-set by Jordan'),
    (lambda p: p.startswith('godot/'), 'keep', 'R-GODOT', 'the eventual res:// root (CLAUDE.md §6)'),
    (lambda p: p.startswith('skills/'), 'keep', 'R-SKILLS',
     'kept pending per-skill triage -- prose-writer and the editorial/workplan skills lose their subject'),

    # ---- proposals/: per file
    (lambda p: p.startswith('proposals/') and os.path.basename(p) in PROPOSALS_KEEP, 'keep',
     'R-PROP-LIVE', 'load-bearing on kept code or governs this operation'),
    (lambda p: p.startswith('proposals/'), 'evacuate', 'R-PROP-DEAD',
     'superseded, or speculative analysis that self-declares it ratifies nothing'),

    # ---- unambiguous detritus
    (lambda p: p.startswith('arcs/'), 'evacuate', 'R-ARCS', 'generated narrative content'),
    (lambda p: p.startswith('deprecated/'), 'evacuate', 'R-DEPRECATED',
     'history -- the evacuation tag preserves it'),
    (lambda p: p.startswith('dashboard/'), 'keep', 'R-DASHBOARD',
     'the published status site -- KEPT (Jordan, 2026-08-04). See the caveat below: its INPUTS shrink'),
    (lambda p: p.startswith('workplans/'), 'keep', 'R-WORKPLANS',
     'the steering surface -- KEPT (Jordan, 2026-08-04). 13 files: master workplan, the progress '
     'board the SessionStart banner reads, and 10 POINTER stubs. This is the continuity context, '
     'and it CARRIES ITS OWN STATUS -- which is the property that makes context safe to keep'),

    # ---- root files
    (lambda p: '/' not in p, 'keep', 'R-ROOT',
     'repo root: session protocol, currency index, CI config'),
]

_AUDIT_DATE = re.compile(r'^audit/(\d{4}-\d{2}-\d{2})')


def _audit_is_recent(rel: str) -> bool:
    """Date-prefixed audit entries on/after the cutoff. Undated entries are NOT recent.

    Deliberately string-compares ISO dates: lexical order is chronological, and it keeps the rule
    free of a `now` that would make a deletion plan depend on its run time.
    """
    if not rel.startswith('audit/'):
        return False
    m = _AUDIT_DATE.match(rel)
    return bool(m) and m.group(1) >= AUDIT_CUTOFF


def tracked() -> list[str]:
    out = subprocess.run(['git', 'ls-files'], cwd=REPO, capture_output=True, text=True, check=True)
    return [l for l in out.stdout.splitlines() if l.strip()]


def classify(rel: str) -> tuple[str, str, str]:
    for matcher, verdict, rule_id, reason in RULES:
        if matcher(rel):
            return verdict, rule_id, reason
    return 'UNPARTITIONED', 'R-NONE', 'no rule matched -- the partition is not total'


def partition() -> dict:
    buckets = {'keep': [], 'relocate': [], 'evacuate': [], 'UNPARTITIONED': []}
    by_rule = collections.Counter()
    reasons = {}
    moves = {}
    for rel in tracked():
        verdict, rule_id, reason = classify(rel)
        buckets[verdict].append(rel)
        if verdict == 'relocate':
            dest, rid, why = relocation(rel)
            moves[rel] = dest
            by_rule[rid] += 1
            reasons[rid] = why
        else:
            by_rule[rule_id] += 1
            reasons[rule_id] = reason
    return {'buckets': buckets, 'by_rule': by_rule, 'reasons': reasons, 'moves': moves}


# ---------------------------------------------------------------------------------------------
# What would break: readers of an evacuating tree among the files we are KEEPING
# ---------------------------------------------------------------------------------------------
BLOCKING_PREFIXES = ('tools/', 'tests/valoria/', '.github/', '.githooks/', '.claude/')
_CODE_EXT = ('.py', '.yml', '.yaml', '.json', '.sh', '.toml', '.ini')


def readers(evac_roots: list[str], keep: list[str]) -> dict:
    """For each evacuating top-level root, which KEPT files name it.

    Split blocking (executable) from prose (a mention in a kept document). A prose mention needs a
    restructure_ledger alias row; a blocking reader needs code retired or re-pointed in the SAME
    commit as the deletion.
    """
    result = {r: {'blocking': [], 'prose': []} for r in evac_roots}
    pats = {r: re.compile(r'(?<![\w/])' + re.escape(r.rstrip('/')) + r'/') for r in evac_roots}
    for rel in keep:
        full = os.path.join(REPO, rel)
        try:
            with open(full, encoding='utf-8', errors='ignore') as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError):
            continue
        for root, pat in pats.items():
            if pat.search(text):
                is_code = rel.startswith(BLOCKING_PREFIXES) and rel.endswith(_CODE_EXT)
                result[root]['blocking' if is_code else 'prose'].append(rel)
    return result


def contract_guard(evacuating: set[str]) -> list[str]:
    """Nothing that a module contract points at may be evacuated.

    build_fork.py's contract_coverage() states the trap: the tempting "minimal" cut drops the 14
    units that have a contract but no code YET, plus every `build: stub` unit -- which is the
    backlog, not dead weight. Same guard, opposite direction.
    """
    if yaml is None:
        return ['pyyaml missing -- cannot run the contract guard']
    path = os.path.join(REPO, 'references', 'module_contracts.yaml')
    if not os.path.exists(path):
        return ['references/module_contracts.yaml missing -- cannot run the contract guard']
    with open(path, encoding='utf-8') as fh:
        contracts = yaml.safe_load(fh) or {}
    bad = []
    for c in contracts.get('modules') or []:
        for field in ('doc', 'sim_module'):
            v = c.get(field)
            if not isinstance(v, str) or v.strip().lower() in ('none', 'null', 'n/a', ''):
                continue
            q = v.strip().rstrip('/')
            hits = [e for e in evacuating if e == q or e.startswith(q + '/')]
            if hits:
                bad.append(f"{c.get('module')}.{field} -> {q} ({len(hits)} file(s) would be evacuated)")
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', action='store_true', help='write references/evacuation_manifest.json')
    ap.add_argument('--check', action='store_true', help='partition totality + contract guard')
    ap.add_argument('--slice', metavar='ROOT', help='detail one evacuating root and its readers')
    args = ap.parse_args(argv)

    p = partition()
    keep, evac = p['buckets']['keep'], p['buckets']['evacuate']
    reloc, orphan = p['buckets']['relocate'], p['buckets']['UNPARTITIONED']
    retained = keep + reloc          # relocation is a KEEP-class verdict; only the path changes
    total = len(keep) + len(reloc) + len(evac) + len(orphan)

    # ---- THE CENTRAL GUARD: the partition must be total and disjoint.
    if orphan:
        print(f"[EVAC] PARTITION NOT TOTAL -- {len(orphan)} tracked file(s) match no rule.")
        print("       This is the CARRY-union-LEAVE defect. A file matching no rule has no verdict,")
        print("       and a mirror-image deletion would silently take it. First 20:")
        for o in orphan[:20]:
            print(f"        {o}")
        if args.check:
            return 1

    evac_roots = sorted({e.split('/')[0] for e in evac})
    bad = contract_guard(set(evac))

    if args.check:
        if bad:
            print(f"[EVAC] CONTRACT GUARD FAILED -- {len(bad)} contracted unit(s) inside the evacuate set:")
            for b in bad:
                print(f"        {b}")
            return 1
        print(f"[EVAC] partition is total over {total} tracked files "
              f"({len(keep)} keep / {len(reloc)} relocate / {len(evac)} evacuate)")
        print("[EVAC] contract guard: no contracted or stub unit is inside the evacuate set")
        return 0

    if args.slice:
        root = args.slice.rstrip('/')
        members = [e for e in evac if e.split('/')[0] == root]
        if not members:
            print(f"[EVAC] {root!r} is not an evacuating root. Evacuating: {', '.join(evac_roots)}")
            return 1
        r = readers([root], retained)[root]
        print(f"[EVAC] slice {root}/ -- {len(members)} file(s) would be evacuated")
        print(f"       blocking readers (must be retired/re-pointed in the SAME commit): {len(r['blocking'])}")
        for b in sorted(r['blocking']):
            print(f"         ! {b}")
        print(f"       prose readers (need a restructure_ledger alias row): {len(r['prose'])}")
        for s in sorted(r['prose'])[:15]:
            print(f"           {s}")
        if len(r['prose']) > 15:
            print(f"           ... and {len(r['prose']) - 15} more")
        return 0

    print(f"[EVAC] {total} tracked files: {len(keep)} KEEP / {len(reloc)} RELOCATE / {len(evac)} EVACUATE")
    if reloc:
        print("[EVAC] relocations (kept, moved to a subsystem home):")
        for src in sorted(reloc):
            print(f"        {src}\n          -> {p['moves'][src]}")
    print(f"[EVAC] rules fired:")
    for rule_id, n in p['by_rule'].most_common():
        print(f"        {rule_id:18s} {n:>5}   {p['reasons'][rule_id][:88]}")
    rd = readers(evac_roots, retained)
    print(f"\n[EVAC] per-slice readiness (blocking readers must go in the same commit):")
    for root in evac_roots:
        n = len([e for e in evac if e.split('/')[0] == root])
        b, s = len(rd[root]['blocking']), len(rd[root]['prose'])
        flag = 'READY' if b == 0 else f'{b} BLOCKING'
        print(f"        {root:14s} {n:>5} files   {flag:>14s}   {s:>4} prose refs")

    if args.json:
        out = os.path.join(REPO, 'references', 'evacuation_manifest.json')
        with open(out, 'w', encoding='utf-8') as fh:
            fh.write(json.dumps({
                '_generated': ('GENERATED by tools/evacuation_plan.py. The keep/evacuate partition '
                               'per ED-IN-0125/0127. NEVER hand-edit: rerun the tool. This is a PLAN, '
                               'not an authorisation -- no deletion is sanctioned by this file.'),
                'audit_cutoff': AUDIT_CUTOFF,
                'counts': {'total': total, 'keep': len(keep), 'relocate': len(reloc),
                           'evacuate': len(evac)},
                'moves': p['moves'],
                'by_rule': dict(p['by_rule']),
                'reasons': p['reasons'],
                'evacuate_roots': evac_roots,
                'readers': rd,
                'evacuate': sorted(evac),
            }, indent=1, sort_keys=True) + '\n')
        print(f"\n[EVAC] -> references/evacuation_manifest.json")
    return 0


if __name__ == '__main__':
    sys.exit(main())
