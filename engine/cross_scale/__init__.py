"""
engine.cross_scale — Inter-scale handoff, echo, zoom, articulation

Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Modules:
  - zoom_in_out: Zoom In-Out Protocol
  - handoff_rules: 8 handoff rules between scales
  - combat_bridge: faction aggregates → Combatant pair → the canonical combat resolver
  - scene_dispatch: consumer-side scale-seam glue

⚠ FOUR MODULES LEFT THIS PACKAGE. 2026-09-16 (ED-IN-0232, RULED by Jordan: *"anything key-based
gets retired"*) — `echo_transport` (the Key & Echo transport itself), `articulation` (the Key-bus
subscriber, Tier 1/2/3, entirely stub-wire callbacks observing an emitted Key) and
`parliamentary_bridge` (the §10 vote, whose single entry point returned early unless a scheduler was
attached), all three at `FORK:c6e82105`. 2026-09-29 (plan position `28-0`, ORPHAN-DELETE) —
`domain_echo` (the §5 Domain Echo COMPUTATION itself): `compute_domain_echo` had zero callers
anywhere in the tree, so the computation this package's name still nods to no longer exists here
either, only its history. The package keeps the name "echo" for that history, not for live content.
"""
