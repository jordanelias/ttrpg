# THE MODULAR HIERARCHY CODE ARCHITECTURE (adjudicated, binding on the suite)

## THE UNIFICATION
The prior formulation asked for contracts "defined in a centralized hierarchical manner", with a
surface descending game -> subsystem -> module -> key -> field, and a runtime half where each
subsystem's wrapper owns all I/O, "inputs trickle down with granularity, outputs aggregate up".
It was never executed, and the recorded reason is exact:

    "it needs a decision about what the levels ARE ... Nesting the three under a new top-level
     key would be a hierarchy in SHAPE and not in MEANING - worse than the honest flat state,
     because it would look done."

JORDAN'S CONTAINMENT AXIOM ANSWERS THE LEVELS QUESTION.

    THE MODULE HIERARCHY *IS* THE CONTAINMENT LADDER.

    Person -> Family -> Community -> Settlement -> Territory -> Duchy -> Realm

    Parent-child in the module tree MEANS containment in the world. That is a hierarchy in
    meaning, not in shape. Every level is a level of the GAME, so it cannot be a filing system.

## WHY THIS IS THE WHOLE DESIGN, NOT A FILING DECISION
1. T6 (down-stroke) IS "inputs trickle down with increasing granularity". A realm decision enters
   the realm module and is REFRACTED by each child module until it reaches a person as something
   sized to them. The down-stroke is not a feature; it is what the architecture does.
2. T5 (up-stroke) IS "outputs aggregate up". A person's demand enters their family module and is
   carried or dropped at each rung. Filtering is a rung REFUSING to aggregate - a real act by a
   real person at that rung (T1), not a threshold.
3. S ("propagates as required across scales") therefore becomes STRUCTURAL rather than a quality
   to be checked. A design where propagation is the architecture cannot fail S by omission; it can
   only fail it by a rung being missing. That is why Family and Community had to be added.
4. F-17 (scale-blind primitives) dissolves: one rung module, instantiated at every rung, means a
   mechanism written for elites is automatically available to populations.

## FACTION IS ORTHOGONAL TO THE HIERARCHY - THIS IS THE SECOND HALF
A faction is NOT a rung and NOT a module in the tree. It is a SET of persons, and it composes
ACROSS the tree. Its scale is DERIVED from where its members stand -- see 01_substrate.md 1.3,
which REJECTS "smallest node spanning all members" (one member taking ship promotes a village
conspiracy to realm scale) in favour of a presence/density/footprint PROFILE. THE SPINE WINS ON
ANY CONFLICT WITH THIS FILE.
- Making faction a TIER is exactly why it could not scale before (F-10).
- Keeping it a set-system is what makes "two brothers" and "a national church" the same object
  with the same mechanics (A-2), and makes growth/shrink one operation in two directions (A-4).
- A faction ACTS by acting through the persons it contains, at whatever rungs they sit. That is
  T1 made structural: a faction has no verbs of its own.

## THE FIVE-LEVEL CONTRACT SURFACE, RE-LEVELLED
    WORLD
      +-- RUNG (person/family/community/settlement/territory/duchy/realm)
      |     one module per rung; owns that rung's state; declares what it aggregates
      |     upward and what it refracts downward
      +-- SYSTEM (a concern that instantiates at one or more rungs: interior, holding,
      |     demand, opportunity, argument, investigation, alignment)
      +-- CAPABILITY (a named thing a person at a rung can do)
      +-- STATE + EVENTS (what is stored, what is emitted, who may read it)

RULES BINDING EVERY MODULE
R-1 A module may read its OWN state and any message addressed to it. It may NOT read a sibling's
    state. It MAY compute an aggregate over its descendants ON DEMAND -- a norm is the stances of
    the members, computed when asked, never a stored field and never a per-tick push. (An earlier
    draft of this file said a module "receives aggregates", which imported a push/wrapper flow the
    spine does not have and would have re-created stored aggregate state. Corrected.)
R-2 A module may write ONLY its own state, and a container's own state is only its stake, its
    judging set and its standing dates. Everything else lives on persons. No module reaches through
    another to write.
R-3 Every decision function takes (actor, actor's VIEW) - never (actor, world). This is the T4
    signature rule and it binds at every rung. Omniscience becomes unspellable.
R-4 A system instantiated at a rung must be instantiable at EVERY rung it claims, or it declares
    the rungs it excludes and why. No elite-only mechanisms by accident.
R-5 Faction/alignment code composes over rung modules; it never becomes one.
