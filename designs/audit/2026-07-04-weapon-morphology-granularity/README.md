# Weapon-morphology granularity audit — 2026-07-04

**Status: PROPOSED, Jordan-vetoable · lane PC · no ED-PC IDs allocated yet · no canonical file touched.**

Reasoned audit (`audit_v1.md`) of how to extend the bottom-up weapon-morphology model
(`designs/scene/combat_engine_v1/weapons.py` located parts + `geometry.py` scalars, derived through
`weapon_physics.py`) with more granular morphological characteristics — triggered by this session's
silhouette-reconstruction exercise, which showed a faithful renderer must *invent* the two facts the model
does not store: blade transverse width and edge symmetry (the latter hand-authored as a 21-weapon name set,
exactly the per-weapon-table shape the model forbids). The audit inventories the current primitive surface
and its consumers, ranks the missing degrees of freedom (edge topology; width/thickness/section-fill
profile; grippable-element half-sword affordance; guard axis semantics), proposes four schema-level
primitives (P1–P4) with "absent ⇒ identity" defaults, Phase-0-style S-graded grounding, per-primitive
double-count audits, and a mass-closure anti-fabrication loop, maps each to concrete engine wiring
(legibility, `defense_affinities.wind`, `thrust_factor`, the `cross_section`→`gap` armour-defeat chain — the
flagged HIGH balance risk, sequenced strictly behind the Phase-C percussion recalibration), and gives a
five-tranche implementation plan (T1 = edge topology first) with falsifiable heft-style acceptance orderings
and the loud Jordan-gated list.
