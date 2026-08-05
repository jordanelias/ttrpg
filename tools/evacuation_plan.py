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
import ast
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

# Audit units kept AGAINST the lane rule, by explicit ruling. One entry, one reason, no pattern --
# an override list is how a ruled exception stays visible; a cleverer classifier is how it hides.
AUDIT_KEEP_OVERRIDE = {
    # Jordan, 2026-08-04: "emergent narrative to be kept but joined appropriately". 46 .md, 175 IN
    # citations, design by subject -- the exact over-capture flagged before the lane rule was ruled.
    'audit/2026-07-05-emergent-narrative-engine',
}

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
    # THE PARITY ORACLE -- the LAST executable dependency the kept tree has on audit/.
    # tools/gen_sigma_parity_goldens.py:95 loads it to regenerate the committed golden that
    # engine/tests/test_sigma_leverage_parity.py asserts on. Its docstring said it "cannot move"
    # because sibling files in that directory `from engine import ...` -- but those siblings are
    # one-off session code that EVACUATES, so the constraint dissolves: there is nothing left to
    # break. engine/reference/ is the pre-designed home (build_fork.py:70 already maps the OTHER
    # parity oracle, tests/sim/v32-combat-balance, to exactly that destination), so this puts both
    # frozen reference implementations in one place beside the code they validate.
    # EXECUTION NOTE: the move requires updating gen_sigma_parity_goldens.py's load path in the
    # same commit, then regenerating the golden and confirming it is byte-identical.
    (lambda p: p == 'audit/2026-06-03-contest-groundup/engine.py',
     'engine/reference/contest-groundup/', 'R-REL-ORACLE',
     'frozen parity oracle -- the last executable dependency of kept code on audit/'),
    # THE ED UNIVERSE. tools/validate_ed_citations.py -- a BLOCKING CI gate -- builds its set of
    # valid ED ids from registers/ PLUS three directories under deprecated/ (its ARCHIVE_GLOBS at
    # :145): deprecated/archives/editorial/, .../editorials/, and deprecated/canon/. 26 files,
    # roughly ED-001..ED-1200.
    # R-DEPRECATED would evacuate all of them, and the gate's OWN docstring (:347-350) records what
    # that costs: losing ONE of those dirs shrank the universe 1167 -> 1107 and turned 110 VALID
    # citations into NONEXISTENT. NONEXISTENT is never deferred (:377-381), so the evacuation commit
    # would turn a blocking gate red -- and the tempting field fix (suppress NONEXISTENT) would
    # destroy the repo's only anti-fabrication citation check. The semantic being protected is
    # ED-IN-0075's: an archived ED is LEGITIMATE, not missing. A partial universe cannot tell a
    # typo from a fabrication from a correctly-archived id.
    # So they relocate rather than evacuate -- and this IS Jordan's "start fresh for registers":
    # frozen archive beside the active register, new work on a clean surface, provenance intact.
    # EXECUTION NOTE: add 'registers/archive/' to ARCHIVE_GLOBS in the same commit, and re-run the
    # gate to confirm the universe size is unchanged.
    (lambda p: (p.startswith(('deprecated/archives/editorial/', 'deprecated/archives/editorials/',
                              'deprecated/canon/'))
                and ('ledger' in os.path.basename(p) or 'editorial' in os.path.basename(p))),
     'registers/archive/', 'R-REL-EDUNIVERSE',
     'ED archive read by the BLOCKING citation gate -- evacuating it turns CI red on day one'),
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
    # THE SECOND PARITY ORACLE, and the reason it is a keep rather than a relocate. It is loaded by
    # ABSOLUTE PATH from kept tools/gen_sigma_parity_goldens.py:96 to regenerate the COMMITTED golden
    # engine/tests/goldens/sigma_leverage_parity.json, which kept CI test
    # engine/tests/test_sigma_leverage_parity.py:115 asserts on (`by_oracle["groundup"] >= 259`).
    # Evacuating it leaves a committed generated table with no source -- a frozen artifact that can
    # never be re-derived, which is the exact stale-artifact hazard this programme keeps closing.
    # It does NOT relocate: gen_sigma's own docstring (:11-12) says both oracles are frozen
    # provenance that must stay put, and the whole point of that generator is to INVERT the coupling
    # (oracle stays, test reads a table) rather than move the oracle around.
    # CAUGHT BY: the join-split reader scan below, after a literal-substring scan missed it entirely.
    # FOUND BY THE W3 REHEARSAL (ED-IN-0144), not by any static prediction. Each of these is a
    # Python module imported BY BARE NAME from kept code; deleting one does not fail a test, it
    # stops `pytest tests/valoria` COLLECTING, which is strictly worse and was invisible to both
    # the substring and the constructed-path scans.
    (lambda p: p == 'tests/sim/gauge_mb.py', 'keep', 'R-IMPORTED-MODULE',
     'imported as `import gauge_mb` by two KEPT shipping-gate tests (test_gauge_invariants, '
     'test_morale_write_sweep) -- evacuating it makes the whole suite uncollectable'),
    (lambda p: p == 'deprecated/skills/valoria-orchestrator/scripts/descriptor_registry.py',
     'keep', 'R-IMPORTED-MODULE',
     'imported as `import descriptor_registry` by two kept tests and a kept skill script -- '
     'filed under deprecated/ but still load-bearing on the shipping gate'),
    (lambda p: p == 'deprecated/skills/valoria-orchestrator/scripts/github_ops.py',
     'keep', 'R-IMPORTED-MODULE',
     'imported by tools/compliance_check.py, a BLOCKING CI gate. CLAUDE.md §8 records this '
     'import as the reason several tools were retired; the importer itself was never cleaned up'),

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
    # ---- the SECOND clause of Jordan's audit ruling, which was missing until 2026-08-04.
    # He said "probably keep audits from july overall" AND "Audit history for all of July, but
    # NONE FOR INFRASTRUCTURE". Only the first clause was implemented; the string "none for
    # infrastructure" appeared NOWHERE in the repository. R-AUDIT-RECENT became the single largest
    # keep rule in the partition -- 675 files, ~40% of the whole retained tree -- on half a ruling.
    # Found by the ED-IN-0132 adversarial audit of the programme, not by me.
    # ---- the ONE ruled exception to the lane rule. Jordan, 2026-08-04: "emergent narrative to be
    # kept but joined appropriately". This is the unit the lane rule's known over-capture was
    # always going to take -- a design effort filed under IN because cross-cutting work gets IN
    # ids -- and it was flagged as such BEFORE the rule was ruled on, so this is an override the
    # ruling anticipated, not a hole in it. "Joined appropriately" is a separate operation
    # (tools/join_audit_workings.py), not a verdict: the unit stays, as fewer files.
    (lambda p: audit_unit(p) in AUDIT_KEEP_OVERRIDE, 'keep', 'R-AUDIT-OVERRIDE',
     'design-subject unit that the lane rule would over-capture -- Jordan-ruled kept, and joined'),

    # RULED 2026-08-04, Jordan, on the units that cite no ED so the lane classifier abstains:
    # "contest gate packets like social contest or whatever get joined if multiple mds and
    # RETAINED". So the abstention outcome is ratified as a verdict rather than left as a default,
    # and the reduction comes from JOINING (tools/join_audit_workings.py --include-top), not cutting.
    # And on their non-markdown contents: "keep them if their accompanying audit directories are
    # being kept in main" -- a kept unit keeps its JSON. The joiner is .md-only by construction,
    # so that ruling is already satisfied; encoded here so it is a rule and not an accident.
    (lambda p: _audit_lane_verdict(p) == 'uncited', 'keep', 'R-AUDIT-UNCITED',
     'RULED KEPT (Jordan, 2026-08-04): design-subject packets that cite no ED -- retained, and '
     'joined where they carry multiple .md. Non-markdown contents stay with the kept unit'),

    (lambda p: _audit_lane_verdict(p) == 'infra', 'evacuate', 'R-AUDIT-INFRA',
     'infrastructure-lane audit -- Jordan: "none for infrastructure" / "we would only keep design '
     'lane dominant stuff". The record of HOW we worked, not what the game is'),

    (lambda p: _audit_is_recent(p), 'keep', 'R-AUDIT-RECENT',
     f'audit dated on/after {AUDIT_CUTOFF}, DESIGN-subject, unit head -- includes generators '
     f'in-window'),
    (lambda p: p.startswith('audit/'), 'evacuate', 'R-AUDIT-STALE',
     f'audit older than {AUDIT_CUTOFF}, or undated -- process record, not canon'),

    # ---- prose WITH a code pair, WHERE THE CODE HAS SUPERSEDED IT: the prose goes.
    # Jordan, 2026-08-04: "params .md are largely useless at this point and I want them gone. code
    # should have superseded them all by now" / "just dump the constants to a yaml".
    # This rule previously said KEEP ("information only"), on the strength of ~50 provenance
    # referents from kept code that deleting it would orphan. That objection is dissolved, not
    # ignored: "provenance can cite to a fork" (Jordan, same day), so the citations stay valid
    # against the evacuation tag. What is NOT dissolved is losing what the tables assert, so the
    # deletion is gated on tools/export_params_constants.py having captured them --
    # engine/engine_params/params_tables.yaml holds all 43 files BYTE-IDENTICALLY (the structured
    # table view is the useful part; the verbatim `raw` capture is what makes the claim provable
    # rather than dependent on my parser being total). tests/valoria/test_params_dump.py is the
    # falsifier, and it carries a positive control.
    # EXECUTION NOTE for the deletion slice: `export_params_constants.py --check` re-derives from
    # this tree, so it CANNOT survive its own source. Retire the gate -- from valoria-ci.yml,
    # valoria_local.py, ci_checks_registry.yaml and test_gate_coverage.EXPECTED_COMMANDS -- in the
    # SAME commit that removes engine/params/. It is a migration-window gate, deliberately strict
    # (no vacuous pass on an absent source) so it goes loudly red if anyone forgets.
    (lambda p: p.startswith('engine/params/'), 'evacuate', 'R-PARAMS-DUMPED',
     'parameter tables captured verbatim into engine/engine_params/params_tables.yaml -- data '
     'wearing prose, superseded by the typed layer; provenance cites the fork'),

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
    # RULED 2026-08-04, Jordan: "prose writer must stay." The ED-IN-0132 review recommended
    # evacuating prose-writer + its 19-file reference corpus on the grounds that its subject (the
    # index+infill pipeline) is retired -- and stated the counter itself: canon narrative STAYS on
    # main, and prose-writer is CLAUDE.md §9's routed skill for authoring it. Jordan took the
    # counter. The corpus is a live capability's calibration set, not detritus.
    # The rest of skills/ is still awaiting per-skill triage; this rule no longer pretends
    # otherwise for prose-writer specifically.
    (lambda p: p.startswith('skills/prose-writer/'), 'keep', 'R-SKILL-PROSE',
     'RULED KEPT (Jordan, 2026-08-04): canon narrative stays on main and this is the skill that '
     'authors it -- its reference corpus is a live capability, not a retired subject'),
    (lambda p: p.startswith('skills/'), 'keep', 'R-SKILLS',
     'kept pending per-skill triage -- the editorial/workplan skills lose their subject'),

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

# ---------------------------------------------------------------------------------------------
# THE SECOND CLAUSE OF THE AUDIT RULING (added 2026-08-04, ED-IN-0140)
#
# Jordan said TWO things and only the first was implemented: "probably keep audits from july
# overall" (done, AUDIT_CUTOFF) and "Audit history for all of July, but NONE FOR INFRASTRUCTURE"
# (absent -- the string appeared nowhere in the repository). R-AUDIT-RECENT therefore became the
# largest keep rule in the partition, ~40% of the whole retained tree, on half a ruling. The
# ED-IN-0132 adversarial audit of the programme found this; I did not.
#
# HOW "INFRASTRUCTURE" IS DECIDED, and why not by me reading 59 directory names. The repo already
# has a lane vocabulary -- the `ED-<LANE>-NNNN` namespace -- and an audit unit's own citations say
# which lanes its findings belong to. So the unit's DOMINANT cited lane is the classifier: IN
# means infrastructure/cross-cutting, anything else (MB/PC/FI/SC/FA/WR/SE/GO) means design.
# Jordan ruled this form directly: "we would only keep design lane dominant stuff."
#
# THE KNOWN OVER-CAPTURE, stated because it is real and was ruled on with eyes open: a lane tag
# records who FILED an item, not what it is ABOUT, and cross-cutting design work is filed under IN
# by convention. The largest casualty is audit/2026-07-05-emergent-narrative-engine (46 .md, 175
# IN citations), which is a design effort by subject. Jordan was shown this before ruling.
#
# UNITS THAT CITE NO ED AT ALL have no dominant lane and are NOT infrastructure by default --
# they are the 2026-07-01/02 contest-gate packets and scene-combat redesign work, design by
# subject. Evacuating them would be inferring a ruling that was not given; they are kept and
# flagged rather than silently cut.
_ED_LANE = re.compile(r'ED-([A-Z]{2})-\d{4}')
_LANE_CACHE: dict = {}


def audit_unit(rel: str) -> str:
    """The session unit a path belongs to: `audit/<session>` (or the bare file for loose ones)."""
    parts = rel.split('/')
    return '/'.join(parts[:2]) if len(parts) > 2 else rel


def _audit_unit_lane(unit: str) -> str | None:
    """Dominant `ED-<LANE>` cited across the unit's prose. None if it cites no ED at all.

    Cached per unit: `classify()` runs once per tracked file, and rescanning a 46-file unit that
    many times would make the planner unusable. The scan reads the working tree, consistent with
    every other rule here.
    """
    if unit in _LANE_CACHE:
        return _LANE_CACHE[unit]
    counts: collections.Counter = collections.Counter()
    base = os.path.join(REPO, unit)
    paths = []
    if os.path.isdir(base):
        for dirpath, _dirnames, filenames in os.walk(base):
            paths += [os.path.join(dirpath, n) for n in filenames if n.endswith('.md')]
    elif os.path.isfile(base):
        paths = [base]
    for full in paths:
        try:
            with open(full, encoding='utf-8', errors='ignore') as fh:
                counts.update(_ED_LANE.findall(fh.read()))
        except OSError:
            continue
    lane = counts.most_common(1)[0][0] if counts else None
    _LANE_CACHE[unit] = lane
    return lane


def _audit_lane_verdict(rel: str) -> str | None:
    """'infra' | 'design' | 'uncited' for an IN-WINDOW audit file; None if the rule does not apply.

    Restricted to the window on purpose: an out-of-window infrastructure audit already evacuates
    under R-AUDIT-STALE, and letting this rule claim it would move files between rule buckets
    without changing a single verdict -- making the rule-fired counts lie about what each rule
    decides.
    """
    if not _audit_is_recent(rel):
        return None
    lane = _audit_unit_lane(audit_unit(rel))
    if lane is None:
        return 'uncited'
    return 'infra' if lane == 'IN' else 'design'


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


def slice_prefixes(evac: list[str], retained: list[str]) -> dict:
    """Group the evacuate set by the SHORTEST PURELY-EVACUATING prefix of each file.

    THE DEFECT THIS FIXES, which arrived with the first sub-root evacuation. `readers()` used to
    scan kept files for the evacuating file's TOP-LEVEL directory. That was already loose for
    `tests/` (three kept sub-trees under it) and became actively misleading when
    `engine/params/` flipped to evacuate: the pattern `engine/` matches nearly every kept file in
    the tree, so a 43-file slice would report hundreds of "blocking readers" that have nothing to
    do with it. A slice report whose blocking count is noise is worse than none -- it trains the
    reader to discount the number that exists to stop a bad deletion.

    So a slice is the shortest prefix under which NOTHING is retained. `engine` is impure (all the
    code), `engine/params` is pure -> that is the slice. A file with no pure ancestor (a lone
    evacuating file in a kept directory) is its own slice. Returned as {top-level root: [prefixes]}
    so the readiness table stays short while the scan stays precise.
    """
    out = collections.defaultdict(set)
    for chosen in pure_prefixes(evac, retained):
        out[chosen.split('/')[0]].add(chosen)
    return {k: sorted(v) for k, v in sorted(out.items())}


def pure_prefixes(evac: list[str], retained: list[str]) -> set:
    """The shortest wholly-evacuating ancestor of each evacuating file (or the file itself)."""
    impure = set()
    for r in retained:
        segs = r.split('/')
        for i in range(1, len(segs)):
            impure.add('/'.join(segs[:i]))
    out = set()
    for rel in evac:
        segs = rel.split('/')
        chosen = rel
        for i in range(1, len(segs)):
            pref = '/'.join(segs[:i])
            if pref not in impure:
                chosen = pref
                break
        out.add(chosen)
    return out


def _is_evacuating_path(built: str, pure: set, evac_set: set) -> bool:
    """Is this constructed path wholly inside the evacuate set?

    `built in evac_set` alone is too narrow (it is usually a directory) and "something under it
    evacuates" is too broad -- `tests/sim` contains both the evacuating stress prose and the KEPT
    canon mass-battle engine, and the broad test reported all 30 kept readers of the latter as
    split-path breakages. Wholly-evacuating is the property that actually predicts a break.
    """
    if built in evac_set:
        return True
    return any(built == p or built.startswith(p + '/') for p in pure)


def readers(prefixes_by_root: dict, keep: list[str], evac_set: set) -> dict:
    """For each evacuating root, which KEPT files name any of its evacuating prefixes.

    Split blocking (executable) from prose (a mention in a kept document). A prose mention needs a
    restructure_ledger alias row; a blocking reader needs code retired or re-pointed in the SAME
    commit as the deletion.
    """
    result = {r: {'blocking': [], 'prose': []} for r in prefixes_by_root}
    pats = {}
    for root, prefs in prefixes_by_root.items():
        alts = []
        for p in prefs:
            # a prefix that IS a tracked file needs no trailing slash -- but it does need a right
            # boundary, so `audit/foo.md` cannot match inside `audit/foo.mdx`. A directory prefix
            # carries its own boundary in the slash, and must NOT take the lookahead (the next
            # character there is a word character by construction).
            alts.append(re.escape(p) + (r'(?![\w-])' if p in evac_set else '/'))
        pats[root] = re.compile(r'(?<![\w/.-])(?:' + '|'.join(alts) + r')')
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


def joined_path_readers(evac_roots: list[str], retained: list[str], evac_set: set | None = None) -> dict:
    """Kept CODE that builds a path into an evacuating tree OUT OF SEGMENTS.

    THE FALSE NEGATIVE THIS EXISTS FOR, and it was a real one. `readers()` greps for the literal
    `audit/`. `tools/gen_sigma_parity_goldens.py:96` writes

        os.path.join(REPO_ROOT, 'audit', '2026-06-03-contest-groundup', 'engine.py')

    which contains no such substring, so the scan reported that file as having no readers while a
    kept tool loaded it to regenerate a committed golden that a kept CI test asserts on. A
    substring scan cannot see a split path -- not "did not", *cannot*. The same shape hides
    `tools/m1_acceptance.py`'s read of the workplans progress board.

    So: parse each kept `.py`, walk every `os.path.join(...)` / `Path(...)` call and every `/`
    chain, keep the CONSTANT string segments, and test the reconstructed relative path. Non-constant
    segments (variables) are skipped rather than guessed -- guessing is the fabrication this repo
    forbids, and a skipped segment yields a shorter path that still matches on its root, which is
    the level the slice cares about.

    `evac_set`, when given, tightens the hit test from "this path exists" to "this path is
    EVACUATING". Without it, a root that is only partly evacuating (`engine/`, now that
    `engine/params/` has flipped) reports every kept `os.path.join(REPO, 'engine', ...)` as a
    split-path breakage. Same reason as `slice_prefixes`: a false blocking hit costs the report
    its credibility.
    """
    hits = {r: [] for r in evac_roots}
    roots = set(evac_roots)
    pure = pure_prefixes(sorted(evac_set), retained) if evac_set is not None else set()

    def const_segments(node):
        """Constant string pieces of a join/Path/`/`-chain, in order."""
        out = []
        if isinstance(node, ast.Call):
            f = node.func
            name = getattr(f, 'attr', None) or getattr(f, 'id', None)
            if name in ('join', 'Path'):
                for a in node.args:
                    out.extend(const_segments(a))
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            out.extend(const_segments(node.left))
            out.extend(const_segments(node.right))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.append(node.value)
        return out

    for rel in retained:
        if not rel.endswith('.py'):
            continue
        try:
            tree = ast.parse(open(os.path.join(REPO, rel), encoding='utf-8', errors='ignore').read())
        except (OSError, SyntaxError, UnicodeDecodeError):
            continue
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Call, ast.BinOp)):
                continue
            segs = [s for s in const_segments(node) if s and '/' not in s and s not in ('.', '..')]
            if len(segs) < 2:
                continue
            for i, s in enumerate(segs):
                if s in roots and i + 1 < len(segs):
                    built = '/'.join(segs[i:])
                    if evac_set is not None:
                        leaves = _is_evacuating_path(built, pure, evac_set)
                    else:
                        leaves = os.path.exists(os.path.join(REPO, built))
                    if leaves:
                        hits[s].append(f'{rel} -> {built}')
                    break
    return {k: sorted(set(v)) for k, v in hits.items()}


def module_import_readers(evac_set: set, retained: list[str]) -> dict:
    """Kept Python that IMPORTS a module living in an evacuating tree, BY BARE NAME.

    THE THIRD BLIND SPOT, and the one only a real rehearsal could find (W3, ED-IN-0144).
    `tests/valoria/test_gauge_invariants.py` and `test_morale_write_sweep.py` do

        import gauge_mb

    where `gauge_mb` is `tests/sim/gauge_mb.py`, classified EVACUATE by R-TESTS-PROSE. Neither
    existing scan can see it: `readers()` greps for the path string `tests/sim/gauge_mb.py`, which
    never appears; `joined_path_readers()` looks for constructed paths, and there is no join. The
    dependency is expressed as a MODULE NAME resolved through sys.path at runtime.

    Deleting it does not fail a test -- it stops `pytest tests/valoria` COLLECTING AT ALL. The
    entire shipping gate becomes unrunnable, which is a strictly worse outcome than a red test and
    is invisible to every static prediction the planner had made.

    So: for each evacuating `.py`, take its module name, and find kept `.py` that import it.
    Bare-name imports only -- a dotted package import is already visible to the path scans.
    """
    # A bare name that is ALSO a real top-level package resolves to the package, not to a
    # same-named file in an evacuating tree. Without this, `import engine` in engine/autoload/*.py
    # reports tests/sim_framework/engine.py as a breakage -- a false positive on the most
    # load-bearing package in the repo. Checked before reporting, not after.
    packages = {d for d in os.listdir(REPO)
                if os.path.isdir(os.path.join(REPO, d))
                and os.path.exists(os.path.join(REPO, d, '__init__.py'))}
    by_module = {}
    for rel in evac_set:
        if rel.endswith('.py') and not rel.endswith('__init__.py'):
            mod = os.path.basename(rel)[:-3]
            if mod in packages:
                continue
            by_module.setdefault(mod, []).append(rel)
    if not by_module:
        return {}
    def bare_imports(rel):
        try:
            tree = ast.parse(open(os.path.join(REPO, rel), encoding='utf-8',
                                  errors='ignore').read())
        except (OSError, SyntaxError, UnicodeDecodeError):
            return []
        names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names += [a.name.split('.')[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                names.append(node.module.split('.')[0])
        return names

    # TRANSITIVE CLOSURE, because one hop is the wrong answer and says so out loud: keeping
    # github_ops.py because a blocking gate imports it immediately makes ITS two imports
    # load-bearing as well. Reporting one hop per run turns a dependency closure into a
    # whack-a-mole loop where each fix reveals the next -- and a partially-kept import chain is
    # exactly as uncollectable as no chain at all.
    hits = collections.defaultdict(list)
    frontier = [r for r in retained if r.endswith('.py')]
    seen_sources = set()
    while frontier:
        rel = frontier.pop()
        if rel in seen_sources:
            continue
        seen_sources.add(rel)
        for n in bare_imports(rel):
            for target in by_module.get(n, []):
                hits[target].append(f'{rel} (import {n})')
                frontier.append(target)      # its own imports are now load-bearing too
    return {k: sorted(set(v)) for k, v in hits.items()}


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

    evac_set = set(evac)
    prefixes = slice_prefixes(evac, retained)
    evac_roots = sorted(prefixes)
    bad = contract_guard(evac_set)

    if args.check:
        imports = module_import_readers(evac_set, retained)
        if imports:
            print(f"[EVAC] MODULE-IMPORT READERS -- {len(imports)} evacuating module(s) are "
                  f"imported BY NAME from kept code. Deleting these does not fail a test, it "
                  f"stops pytest COLLECTING:")
            for target, readers_ in sorted(imports.items()):
                print(f"        ! {target}  <-  {', '.join(readers_[:3])}")
            return 1
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
        # accepts a top-level root ('audit') or any evacuating prefix ('engine/params')
        root = args.slice.rstrip('/')
        members = [e for e in evac if e == root or e.startswith(root + '/')]
        if not members:
            print(f"[EVAC] {root!r} is not an evacuating root. Evacuating: {', '.join(evac_roots)}")
            return 1
        prefs = [p for lst in prefixes.values() for p in lst
                 if p == root or p.startswith(root + '/')] or [root]
        r = readers({root: prefs}, retained, evac_set)[root]
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
    rd = readers(prefixes, retained, evac_set)
    jr = joined_path_readers(evac_roots, retained, evac_set)
    print(f"\n[EVAC] per-slice readiness (blocking readers must go in the same commit):")
    for root in evac_roots:
        n = len([e for e in evac if e.split('/')[0] == root])
        b, s = len(rd[root]['blocking']), len(rd[root]['prose'])
        j = len(jr.get(root, []))
        flag = 'READY' if (b == 0 and j == 0) else f'{b} BLOCKING'
        print(f"        {root:14s} {n:>5} files   {flag:>14s}   {s:>4} prose refs"
              f"{'   +' + str(j) + ' SPLIT-PATH' if j else ''}")
        # a partly-evacuating root: name the sub-trees, or the count above reads as the whole root
        if prefixes[root] != [root]:
            shown = prefixes[root][:4]
            more = f' ... +{len(prefixes[root]) - 4} more' if len(prefixes[root]) > 4 else ''
            print(f"          slices: {', '.join(shown)}{more}")
    if any(jr.values()):
        print("\n[EVAC] SPLIT-PATH readers -- kept code building a path into an evacuating tree out of")
        print("       segments. A literal-substring scan CANNOT see these; each is a silent breakage:")
        for root, lst in jr.items():
            for h in lst:
                print(f"        ! {h}")

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
                'split_path_readers': jr,
                'evacuate': sorted(evac),
            }, indent=1, sort_keys=True) + '\n')
        print(f"\n[EVAC] -> references/evacuation_manifest.json")
    return 0


if __name__ == '__main__':
    sys.exit(main())
