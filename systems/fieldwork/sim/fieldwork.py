"""
systems/fieldwork/sim/fieldwork.py — Fieldwork resolution — Exploration / Investigation / Socializing

Canon source: systems/fieldwork/fieldwork_v30.md
Params source: params/fieldwork.md
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17; STUB-WIRED 2026-07-29, OI-02,
         ED-IN-0091 plan §2.2/§3 Wave 1 stage 3]

Dependencies:
  - sim/autoload/dice_engine
  - sim/personal/investigation
  - sim/personal/conviction

Entry points:
  - run_fieldwork_scene(scene: FieldworkScene) -> FieldworkResult
  - advance_disposition(target, delta: int) -> DispositionState
  - advance_evidence(case, delta: int) -> EvidenceState

"""
from __future__ import annotations

from engine.substrate import stubwire

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]
#
# OI-02 (ED-IN-0091 plan §2.2/§3 Wave 1 stage 3): converted from an unconditional
# `raise NotImplementedError` to the single-owner stub-wire primitive (engine/substrate/stubwire.py,
# plan §2.1) — a typed no-op instead of a crash, visible to structure_audit's `stub_wired`
# attribute and review_core's `stubs.count` ratchet by construction (greppable import, no second
# registry). `module_contracts.yaml` has no entry for this module by that exact name (only the
# sibling `fieldwork_knots` is contract-declared — verified 2026-07-29, G12: the register's "io_contract
# from their module contracts" lead does not resolve for `fieldwork`/`investigation` themselves);
# `io_contract` below cites this module's own docstring "Entry points" declaration instead. The FI
# design gate: ED-916 ("Zero continuous-engine validation at fieldwork parameters" — fieldwork.py
# and investigation.py flagged there as NotImplementedError stubs with zero coverage-matrix hits).


def run_fieldwork_scene(scene: FieldworkScene):
    return stubwire.stub_resolve(
        'systems.fieldwork.sim.fieldwork',
        'run_fieldwork_scene(scene: FieldworkScene) -> FieldworkResult',
        reason='Pass 2l armature stub, design-gated on ED-916 (zero continuous-engine validation '
               'at fieldwork parameters); OI-02, ED-IN-0091 plan §2.2')


def advance_disposition(target, delta: int):
    return stubwire.stub_resolve(
        'systems.fieldwork.sim.fieldwork',
        'advance_disposition(target, delta: int) -> DispositionState',
        reason='Pass 2l armature stub, design-gated on ED-916 (zero continuous-engine validation '
               'at fieldwork parameters); OI-02, ED-IN-0091 plan §2.2')


def advance_evidence(case, delta: int):
    return stubwire.stub_resolve(
        'systems.fieldwork.sim.fieldwork',
        'advance_evidence(case, delta: int) -> EvidenceState',
        reason='Pass 2l armature stub, design-gated on ED-916 (zero continuous-engine validation '
               'at fieldwork parameters); OI-02, ED-IN-0091 plan §2.2')
