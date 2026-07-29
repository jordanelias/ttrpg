"""
systems/fieldwork/sim/investigation.py — Investigation systems — NPE, Interface, Dialogue Lattice, Response Matrix

Canon source: systems/fieldwork/investigation_systems_v30.md
Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17; STUB-WIRED 2026-07-29, OI-02,
         ED-IN-0091 plan §2.2/§3 Wave 1 stage 3]

Dependencies:
  - sim/personal/fieldwork
  - systems/world/sim/npe

Entry points:
  - resolve_npe_response(npc_id: str, prompt: dict, world: GameState) -> NPEResponse
  - evaluate_dialogue_lattice(scene, choice: str) -> LatticeOutcome
  - apply_response_matrix(actor, target, action) -> MatrixResult

"""
from __future__ import annotations

from engine.substrate import stubwire

# [PROVISIONAL — Pass 2l armature stub; implementation pending against canonical source]
#
# OI-02 (ED-IN-0091 plan §2.2/§3 Wave 1 stage 3): converted from an unconditional
# `raise NotImplementedError` to the single-owner stub-wire primitive (engine/substrate/stubwire.py,
# plan §2.1) — see systems/fieldwork/sim/fieldwork.py's matching note for the module_contracts.yaml
# / io_contract provenance detail and the ED-916 FI design-gate citation (both apply identically here).


def resolve_npe_response(npc_id: str, prompt: dict, world: GameState):
    return stubwire.stub_resolve(
        'systems.fieldwork.sim.investigation',
        'resolve_npe_response(npc_id: str, prompt: dict, world: GameState) -> NPEResponse',
        reason='Pass 2l armature stub, design-gated on ED-916 (zero continuous-engine validation '
               'at fieldwork parameters); OI-02, ED-IN-0091 plan §2.2')


def evaluate_dialogue_lattice(scene, choice: str):
    return stubwire.stub_resolve(
        'systems.fieldwork.sim.investigation',
        'evaluate_dialogue_lattice(scene, choice: str) -> LatticeOutcome',
        reason='Pass 2l armature stub, design-gated on ED-916 (zero continuous-engine validation '
               'at fieldwork parameters); OI-02, ED-IN-0091 plan §2.2')


def apply_response_matrix(actor, target, action):
    return stubwire.stub_resolve(
        'systems.fieldwork.sim.investigation',
        'apply_response_matrix(actor, target, action) -> MatrixResult',
        reason='Pass 2l armature stub, design-gated on ED-916 (zero continuous-engine validation '
               'at fieldwork parameters); OI-02, ED-IN-0091 plan §2.2')
