"""sim.substrate — executable Key substrate (v1).

Status: [PROVISIONAL — Key & Echo armature v1, ED-IN-0018, 2026-07-07]

The first executable form of the Key substrate specified in
designs/architecture/key_substrate_v30.md (§2 universal schema, §2.3 invariants,
§4.1 single update rule) and designs/architecture/propagation_spec_v1.md
(§1 ordering/SSI discipline, §4 termination guard). Prior to this module the
Key/emit substrate existed only as design canon plus declared YAML edges in
references/module_contracts.yaml — no Key class, no emit() path, no key log
existed anywhere in sim/ (unaddressed-areas audit, cluster C-REACH/C-KEY
calibration; see designs/audit/2026-07-07-unaddressed-areas-audit/).

Deliberately NOT implemented here (each blocked on an open fork — see
designs/architecture/key_echo_armature_v1.md §5, the consolidated docket):
  - observer resolution / armature interpretation (§4.1 steps 3-4): ORD-3 is a
    PROPOSED, unratified ordering rule; implementing compute_observers() before
    it lands would bake in hash-order nondeterminism.
  - decay() over the key log (AU-4): OF-3, unspecified.
  - canonical cap constants: OF-CAP is open — caps are REQUIRED caller
    parameters, never defaulted, so no fabricated constant enters the repo.
  - campaign-loop wiring: PR-2 scope (flag-gated), not this module.
"""

from sim.substrate.keys import (  # noqa: F401
    AXES,
    ROLES,
    SCALES,
    PERMANENCE_VALUES,
    TIME_HORIZON_VALUES,
    EmittedAt,
    Key,
    KeyLog,
    KeyValidationError,
    Target,
    TerminationBreach,
    TickScheduler,
    TypeRegistry,
    Visibility,
)
