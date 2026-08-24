#!/usr/bin/env python3
"""Which module contracts are REAL? Measured by running the engine, not by reading declarations.

WHY THIS EXISTS
---------------
`references/module_contracts.yaml` declares 27 modules with `emits:`/`consumes:` blocks. CI already
has a conformance job — `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py`, wired
as "Module-Contract Conformance (report-only)" — but it compares DECLARATIONS AGAINST DECLARATIONS:
contracts vs the Key Type Registry vs canonical_sources.

⚠ THIS FILE ONCE CLAIMED "nothing in the tree has ever asked the engine what it actually emits."
THAT WAS FALSE and is retracted. `engine/tests/test_parliamentary_bridge.py:136` pins
`_ON_KEYS_BY_TYPE = {'scene.battle_concluded': 80, 'scene.contest_resolved': 105,
'da.public_governance': 2}` on a seeded campaign — per-type observed emission counts, golden-pinned —
and `tests/valoria/test_public_governance_transfer_key.py:157-172` wraps an emitter and asserts it
fires in a real campaign. What is actually new here is narrower and worth stating accurately:
nothing had compared observed emissions AGAINST THE CONTRACT REGISTRY WITH PER-MODULE ATTRIBUTION.

That distinction is the whole hub-and-bus question. A module that declares `emits: [scene.dialogue]`
and emits nothing is indistinguishable, to every existing instrument, from one that emits it every
season. This runs a seeded campaign and asks.

CLAUDE.md §0.2 — DONE MEANS IT RUNS. This is an execution artifact: its verdict cannot be satisfied
by editing a document, because the numbers come from a campaign. §0.1 pt 5's load-bearing predicate
admits it: its subject is the Key bus, which is game mechanism.

HOW IT ATTRIBUTES AN EMISSION TO A MODULE, and why it is done this way
---------------------------------------------------------------------
A `Key` carries no `source_module` field (keys.py:138 — deliberately; cascade_depth is likewise
scheduler-internal). So the emitter is recovered from the CALL STACK at emit time: the first frame
whose file lives under `systems/` or `engine/` names the module. Matching on the frame's FILE PATH
rather than on a module name is the same discipline the §3 path-seam probe had to adopt — a name can
be spelled around, a file path cannot.

Consumers need no instrumentation at all: `TickScheduler.subscriptions` is a public dict of
type_id -> [callback], and a callback's `__code__.co_filename` names the module that registered it.

THE INSTRUMENT DOES NOT CHANGE BEHAVIOUR. `_emit_at_depth` is WRAPPED, not replaced: the wrapper
records and delegates, and the patch is reverted in a finally block. The control for that claim is
`--check`'s golden assertion: a campaign run under instrumentation produces the same
`KeyLog.content_hash()` as one without. If that ever diverges, the instrument is lying about the
system it measures and its numbers are void.

USAGE
    python3 tools/contract_runtime_conformance.py                  # report
    python3 tools/contract_runtime_conformance.py --json
    python3 tools/contract_runtime_conformance.py --check          # exit 1 on undeclared types

⚠ `--check` IS WIRED NOWHERE. Not in `.github/workflows/valoria-ci.yml`, not in
`tools/valoria_local.py`, not in `references/ci_checks_registry.yaml` — only this tool's EXPORTER
(`tools/export_module_contracts.py --check`) is gated. This is a manual instrument today, and saying
"(CI)" here would assert an enforcement that does not exist, which is the CLAUDE.md §11 defect class.
Wiring it is a decision that waits on the two undeclared types below being declared or accepted.
"""
import argparse
import collections
import json
import os
import sys
import traceback

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_HERE)
sys.path.insert(0, ROOT)

COOKED = os.path.join(ROOT, 'engine', 'engine_params', 'module_contracts.json')

# ── THE RATCHET ────────────────────────────────────────────────────────────────────────────────
# Two-sided, the repo convention: it fails if the number RISES (drift) and if it FALLS without
# being re-pinned (so paying the debt is recorded rather than silently banked).
#
# UNDECLARED_TYPE_MAX is 0 and is a HARD FLOOR, not a ratchet: a Key type that flows at runtime and
# that NO module declares is drift with no legitimate reading — the contract is the interface.
#
# It is deliberately narrower than "observed but not declared": the wide measure also catches
# registry holes and ownership questions, and gating those blames code for a hole in a declaration.
#
# ⚠⚠ THIS FLOOR WAS VACUOUS ON THE CONSUME SIDE FOR ITS FIRST FEW HOURS, AND IT REPORTED "MET"
# BECAUSE OF IT (retracted 2026-08-24 by an adversarial pass). `_triage` fell back to the wildcard
# consumers when no module explicitly declared a type — `declared_by.get(t) or list(wildcards)` —
# so while ANY module declares `{type: "*"}`, the owners list could never be empty and
# `undeclared_type` was UNREACHABLE on that side. That is CLAUDE.md §0.1 pt 2 exactly: an assertion
# that cannot observe the failure it excludes. With the fallback gone the floor is NOT met, and the
# two types it was hiding are real: `scene.accord_echo` and `meta.cascade_cluster_event` are both in
# the Key vocabulary (`engine/engine_params/key_types.json`) and NO module contract names either, on
# either side. A wildcard grants a MODULE permission to consume; it does not DECLARE that a type
# exists. Those are different facts and conflating them is what made the gate unfailable.
UNDECLARED_TYPE_MAX = 0
# DECLARED_ONLY is the hub-and-bus gap itself: declared, never observed. Large today, and that is
# the honest state rather than something to fix here. Reported, never gated.


def _load_contracts():
    """The DECLARED interface, from the cooked artifact — never by parsing the YAML.

    Reading `references/module_contracts.yaml` here would make this the ELEVENTH parser of that
    registry, which `tests/valoria/test_engine_params_bridge.py::test_no_new_parser_of_an_authored
    _surface` exists to stop. `tools/export_module_contracts.py` is the exporter; this reads its
    output, which also gives us the `path_to_module` binding no tool owned before.
    """
    with open(COOKED, encoding='utf-8') as fh:
        d = json.load(fh)
    return d['modules'], [tuple(x) for x in d['path_to_module']], set(d['unattributable'])


def _module_of(path, path_to_module):
    """The CONTRACT module a source file belongs to, by longest path prefix.

    ⚠ THIS IS THE STEP THAT WAS WRONG ON THE FIRST RUN, and the wrongness looked exactly like a
    finding. Attributing by DIRECTORY NAME gave `factions`, `engine.cross_scale.echo_transport`;
    the registry's module names are LOGICAL (`domain_actions`, `social_contest`), so nothing could
    ever match and the tool reported "0 of 60 declared emissions happen". The true statement was
    "my attribution scheme and the registry disagree about what a module is called". The binding is
    now the registry's own `sim_module` field, cooked into `path_to_module` and sorted
    longest-prefix-first, so a subdirectory resolves to the most specific module that claims it.

    Returns (module_or_None, raw_rel_path). The raw path is carried so an unattributed emission is
    REPORTABLE rather than silently dropped into a bucket — an unattributable emitter is a finding
    about the registry, not noise to hide.
    """
    rel = os.path.relpath(os.path.abspath(path), ROOT).replace(os.sep, '/')
    for prefix, module in path_to_module:
        if rel == prefix or rel.startswith(prefix.rstrip('/') + '/'):
            return module, rel
    return None, rel


def observe(n=2, base_seed=0, path_to_module=None):
    """Run a seeded campaign with the bus instrumented. Returns (emits, consumes, key_hash, orphans)."""
    if path_to_module is None:
        _, path_to_module, _ = _load_contracts()
    from engine.substrate import keys as _keys
    from engine import mc_v18

    emits = collections.Counter()          # (module, type_id) -> count
    orphans = collections.Counter()        # rel_path -> count, for emitters no contract claims
    # (module, type_id) -> {emitting file}. Carried so an attribution can be CHECKED against the
    # module's own path prefix — without it, "attributed to a module that binds a path" is the
    # strongest assertion available, and that is satisfied by the caller-laundering bug too.
    sites = collections.defaultdict(set)
    original = _keys.TickScheduler._emit_at_depth
    schedulers = []

    def wrapper(self, key, depth, apply):
        if self not in schedulers:
            schedulers.append(self)
        # THE FIRST ELIGIBLE FRAME IS THE EMITTER, AND THE WALK STOPS THERE. It used to keep
        # walking outward until SOME frame matched a contract, which is how a run attributed
        # `scene.battle_concluded` to `peninsular_strain`: the true emitter
        # (systems/factions/sim/faction_action.py) is claimed by nothing, so the loop kept climbing
        # into the campaign driver and scored the first ancestor that happened to be claimed. A
        # caller is not an emitter.
        #
        # `emitter_rel` IS RECORDED SEPARATELY AND SET EXACTLY ONCE, and that separation is what
        # makes the defect observable rather than merely fixed. Fold it into the same variable the
        # match writes and a caller-laundering walk records the MATCHED frame's path, which trivially
        # sits under the matched module's prefix — so the conformance report comes out
        # self-consistent and the guard in tests/valoria/test_contract_runtime_conformance.py cannot
        # fire. Measured: with the two folded, restoring the bug left that guard green.
        who, emitter_rel = None, None
        for fr in traceback.extract_stack()[:-1][::-1]:
            rel_probe = os.path.relpath(os.path.abspath(fr.filename), ROOT).replace(os.sep, '/')
            if not (rel_probe.startswith('systems/') or rel_probe.startswith('engine/')):
                continue
            if rel_probe.startswith('engine/substrate/'):
                continue          # the bus is never the emitter
            if emitter_rel is None:
                emitter_rel = rel_probe
            who = _module_of(fr.filename, path_to_module)[0]
            break
        if who is None:
            orphans[(emitter_rel or '<unknown>', getattr(key, 'type', '?'))] += 1
        _t = getattr(key, 'type', '?')
        emits[(who or '<unattributed>', _t)] += 1
        if who is not None and emitter_rel:
            sites[(who, _t)].add(emitter_rel)
        return original(self, key, depth, apply)

    _keys.TickScheduler._emit_at_depth = wrapper
    try:
        mc_v18.run_batch(n=n, base_seed=base_seed)
    finally:
        _keys.TickScheduler._emit_at_depth = original

    consumes = collections.Counter()
    for sch in schedulers:
        for type_id, callbacks in (getattr(sch, 'subscriptions', {}) or {}).items():
            for cb in callbacks:
                fn = getattr(getattr(cb, '__code__', None), 'co_filename', None)
                m = _module_of(fn, path_to_module)[0] if fn else None
                consumes[(m or '<unattributed>', type_id)] += 1
    key_hash = None
    for sch in schedulers:
        log = getattr(sch, 'log', None)
        if log is not None and hasattr(log, 'content_hash'):
            key_hash = log.content_hash()
            break
    return emits, consumes, key_hash, orphans, sites


def _triage(observed_edges, declared, path_to_module, unattributable, side):
    """Split observed-but-not-declared edges into the THREE conditions they actually are.

    ⚠ A FLAT "observed_only" READS AS DRIFT AND IS MOSTLY NOT, which matters because it is the half
    a gate would block on. All three emissions this instrument found on 2026-08-24 were reported as
    undeclared; every one of the three Key TYPES is in fact declared, just not by the module the
    emission came from. The conditions have different owners and different fixes:

      undeclared_type    no module declares this Key type at all. REAL DRIFT — the contract is the
                         interface, and a type flowing outside it has no legitimate reading.
      ownership_mismatch the type IS declared, and the declared owner HAS an implementation path,
                         but the emission came from outside it. THREE readings, not two, and the
                         third is the one a reader is most likely to act on wrongly: the registry's
                         `sim_module` is wrong; OR the call lives in the wrong module; OR — the live
                         case — a DELIBERATE CENTRALIZED CARRIER emits on the subsystem's behalf.
                         `engine/cross_scale/echo_transport.py` is exactly that for
                         `scene.contest_resolved` (ED-IN-0028/ED-SC-0007), and it is the shape the
                         hub-and-bus directive ASKS FOR. Acting on this label as though it were
                         always a defect would decentralize the hub. The instrument does not pick.
      unobservable       the type IS declared, and its declared owner binds NO implementation path
                         (`sim_module: none`). Nothing can ever be attributed to it, so this is a
                         REGISTRY gap (the ED-1051 backlog), not a wiring gap. Counting it as drift
                         would blame the code for a hole in the declaration.
    """
    owner_path = dict((m, p) for p, m in path_to_module)
    declared_by = {}
    any_key = 'emits_any' if side == 'emits' else 'consumes_any'
    wildcards = sorted(m for m, d in declared.items() if d.get(any_key))
    for m, d in declared.items():
        for t in d[side]:
            declared_by.setdefault(t, []).append(m)
    out = {'undeclared_type': [], 'ownership_mismatch': [], 'unobservable': []}
    for edge in sorted(observed_edges):
        module, _, type_id = edge.rpartition(':')
        owners = declared_by.get(type_id)
        if not owners and wildcards:
            # A wildcard grants the MODULE permission; it does not DECLARE the type.
            # Folding it in here is what made this branch unreachable. The edge is
            # still undeclared — it is only reported with the wildcard named.
            out['undeclared_type'].append(
                f'{edge}  (only a wildcard covers it: {", ".join(wildcards)})')
            continue
        if not owners:
            out['undeclared_type'].append(edge)
        elif all(owner_path.get(o) is None for o in owners):
            out['unobservable'].append(f'{edge}  (declared by {", ".join(owners)}, no impl path)')
        else:
            out['ownership_mismatch'].append(f'{edge}  (declared by {", ".join(owners)})')
    return out


def report(n=2, base_seed=0):
    declared, path_to_module, unattributable = _load_contracts()
    emits, consumes, key_hash, orphans, sites = observe(n, base_seed, path_to_module)
    obs_e = {(m, t) for (m, t) in emits}
    obs_c = {(m, t) for (m, t) in consumes}
    # A module declaring `{type: "*"}` declares EVERY type on that side (key_substrate §8.7's
    # universal readers). Expanding against the types actually seen is the only honest expansion:
    # enumerating the whole Key vocabulary would inflate `declared` with edges nothing exercises.
    # ⚠ WILDCARD EDGES ARE COUNTED SEPARATELY AND NEVER AS `matched` (corrected 2026-08-24 by an
    # adversarial pass). Expanding `{type: "*"}` over the observed types and folding the result into
    # `declared` makes `matched == observed` FOR THAT MODULE BY CONSTRUCTION — the number cannot
    # fail, so it measures path attribution and flag plumbing, not conformance. This shipped for a
    # few hours as "108 declared / 13 matched"; all 13 were `articulation_layer`, which declares
    # `consumes: []` and matched only itself. It also inflated `declared` by 26 synthetic edges,
    # 13 of them for `fieldwork_knots` — a wildcard consumer with ZERO subscriptions anywhere in
    # the tree, so it was credited with declaring edges nobody authored.
    obs_types_e = {t for _, t in obs_e}
    obs_types_c = {t for _, t in obs_c}
    dec_e = {(m, t) for m, d in declared.items() for t in d['emits']}
    dec_c = {(m, t) for m, d in declared.items() for t in d['consumes']}
    wild_e = {(m, t) for m, d in declared.items() if d.get('emits_any') for t in obs_types_e}
    wild_c = {(m, t) for m, d in declared.items() if d.get('consumes_any') for t in obs_types_c}
    return {
        'modules_declared': len(declared),
        'emits': {
            'declared': len(dec_e), 'observed': len(obs_e),
            'matched': sorted(f'{m}:{t}' for m, t in dec_e & obs_e),
            'wildcard_covered': sorted(f'{m}:{t}' for m, t in (wild_e & obs_e) - dec_e),
            'declared_only': sorted(f'{m}:{t}' for m, t in dec_e - obs_e),
            'observed_only': sorted(f'{m}:{t}' for m, t in obs_e - dec_e),
            'triage': _triage([f'{m}:{t}' for m, t in obs_e - dec_e],
                              declared, path_to_module, unattributable, 'emits'),
        },
        'consumes': {
            'declared': len(dec_c), 'observed': len(obs_c),
            'matched': sorted(f'{m}:{t}' for m, t in dec_c & obs_c),
            'wildcard_covered': sorted(f'{m}:{t}' for m, t in (wild_c & obs_c) - dec_c),
            'declared_only': sorted(f'{m}:{t}' for m, t in dec_c - obs_c),
            'observed_only': sorted(f'{m}:{t}' for m, t in obs_c - dec_c),
            'triage': _triage([f'{m}:{t}' for m, t in obs_c - dec_c],
                              declared, path_to_module, unattributable, 'consumes'),
        },
        'emission_volume': sum(emits.values()),
        # Modules the registry binds to no implementation path — they CANNOT be observed, so their
        # declared edges are not evidence of a wiring gap. Reported separately for that reason.
        'unattributable_modules': sorted(unattributable),
        # Files that emitted a Key and that no contract claims. Each is a registry gap.
        # (module:type) -> the files that actually emitted it. The falsifier for attribution.
        'attributed_sites': {f'{m}:{t}': sorted(v) for (m, t), v in sorted(sites.items())},
        'unclaimed_emitters': {f'{f}::{t}': c
                               for (f, t), c in sorted(orphans.items(), key=lambda kv: -kv[1])},
        'key_log_content_hash': key_hash,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--check', action='store_true', help='ratchet mode: nonzero on drift')
    ap.add_argument('-n', type=int, default=2)
    ap.add_argument('--seed', type=int, default=0)
    a = ap.parse_args(argv)
    r = report(a.n, a.seed)
    if a.json:
        print(json.dumps(r, indent=1))
        return 0
    for side in ('emits', 'consumes'):
        s = r[side]
        print(f'{side.upper():<9} declared {s["declared"]:>3}   observed {s["observed"]:>3}   '
              f'matched {len(s["matched"]):>3}   declared-only {len(s["declared_only"]):>3}   '
              f'observed-only {len(s["observed_only"]):>3}')
    print(f'\nemissions in {a.n} seeded campaign(s): {r["emission_volume"]}')
    print(f'contract modules with NO implementation path: {len(r["unattributable_modules"])}'
          f' of {r["modules_declared"]}  -> {", ".join(r["unattributable_modules"])}')
    if r['unclaimed_emitters']:
        print('\n  files that emitted a Key and that NO contract claims:')
        for f, c in r['unclaimed_emitters'].items():
            print(f'    {c:>5} x  {f}')
    print(f'key-log content hash: {r["key_log_content_hash"]}')
    for side in ('emits', 'consumes'):
        tri = r[side]['triage']
        for cond, label in (('undeclared_type', 'DRIFT — no module declares this Key type'),
                            ('ownership_mismatch', 'OWNERSHIP — declared elsewhere, emitted here'),
                            ('unobservable', 'REGISTRY — declared owner binds no impl path')):
            if tri[cond]:
                print(f'\n  {side}: {label} ({len(tri[cond])}):')
                for x in tri[cond]:
                    print(f'    {x}')
    if a.check:
        bad = (r['emits']['triage']['undeclared_type']
               + r['consumes']['triage']['undeclared_type'])
        if len(bad) > UNDECLARED_TYPE_MAX:
            print(f'\nFAIL: {len(bad)} Key type(s) flow at runtime that NO contract declares. '
                  f'The contract is the interface — declare it or stop emitting it:')
            for x in bad:
                print(f'  {x}')
            return 1
        print(f'\nOK: every Key type that flows is declared by some module '
              f'(ownership mismatches and registry gaps are reported above, not gated).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
