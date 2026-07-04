# Dossier: Victory / Peninsular Strain / Insurgency Pipeline (Strategic Layer)

Lane: victory_strategic. Sources read: designs/provincial/victory_v30.md (+ index/infill),
designs/provincial/peninsular_strain_v30.md (+ index), designs/world/insurgency_pipeline_v30.md,
designs/architecture/player_agency_v30.md, canon/02_canon_constraints.md §B (GD-1/2/3),
canon/mechanics_index.yaml, references/module_contracts.yaml, references/canonical_sources.yaml,
sim/autoload/victory.py.

## Core loop (strategic layer)
Every faction shares one endpoint: hold all 15 playable territories, Accord ≥2 in each, Turmoil ≤6,
sustained 2 consecutive Accountings (victory_v30.md §0; peninsular_strain_v30.md §6.1; GD-1). Four
faction-differentiated non-military toolkits (Crown Treaty, Church Seizure, Hafenmark Proclamation,
Löwenritter Martial Governance; Varfell is military-only post CR-STRIKE) each produce Accord ≥2 at
lower Turmoil/MS cost than conquest (Accord 1). Battle costs MS -1 (peninsular_strain §3.1) and,
via held-instability (not battle-occurrence, ED-743), feeds both Turmoil (§4.1) and Altonian IP
(§3.2) when conquered ground stays at Accord ≤1. Accounting Step 4c-4e (§7) auto-resolves neglected
territory (Accord 1→0→Revolt→Uncontrolled) without player input, which is the GD-3 insurgency
formation trigger (2+ contiguous Uncontrolled territories, 2 seasons) — insurgencies can invade
anyone including their parent faction and are independently eligible for GD-1 sovereignty victory.

## Decision points
1. Territory-acquisition-method choice per target (military vs faction toolkit) — rich: real
   Accord/Turmoil/MS/Casus-Belli tradeoffs, faction-differentiated tools.
2. Accord/Turmoil budget management (garrison vs Govern vs let Accord decay) — moderate: legible
   thresholds, but largely reactive bookkeeping once triggered.
3. Endgame shape choice (which 15/15 + treaty-hegemony mix to pursue) — thin: only one victory
   *shape* exists post-GD-1 (total conquest/hegemony); no negotiated/partition/co-victory endpoint
   remains live.
4. Personal layer (player_agency_v30): Conviction vs Duty triage under Scene Slate budget — rich:
   3-9 opportunities vs 3-5 actions, explicit unpursued-consequence table (§4.5).
5. Whether/when to tolerate an emergent Insurgency vs suppress it (GD-2 mandatory response) — 
   moderate: mechanically real (invasion threat, GD-1 victory-eligible rival) but system-driven,
   little authored texture on how a player *chooses* to engage an insurgency politically.

## North Star assessment
Choice density: moderate overall — rich tactical/personal layer, but the strategic *endpoint* is
single-shape (GD-1 struck 8 alternates + Partition), which is a real narrowing at the highest level
even though day-to-day paths to it are varied. Feeds the collision engine mainly via Accord/Turmoil
world-state (territory mood, revolt, insurgency emergence) intersecting faction toolkits and player
Convictions/Duties — a solid autonomous-world generator, weaker on "different endings are possible."

## N / Omega / Q observations
- Ω non-dominance: the four-pressure design (Accord/Turmoil/MS/IP) is a genuine anti-rush device —
  cite peninsular_strain_v30.md "Design Principle" (military conquest structurally expensive).
- Q-smooth naming drift: GD-1 canon text (canon/02_canon_constraints.md §B) names the track
  "Political Stability ≤ 6"; every design doc and the sim call it "Turmoil" (0-10). sim/autoload/
  victory.py line ~68 aliases it via comment ("PS mapped to Turmoil clock") — works, but a designer
  reading canon text alone cannot find "Political Stability" defined anywhere.
- Q-robust: sim/autoload/victory.py VICTORY_THRESHOLD=15 correctly implements the "all 15" rule and
  matches victory_v30/peninsular_strain — the core sole-victory-function is sound.

## Threadwork junctures
- PRESENT: peninsular_strain_v30.md §3.1 ties Battle directly to MS (Thread substrate) -1/-2 per
  battle type — military strategy has an explicit Thread cost.
- PRESENT: victory_v30_infill.md line 17 — Community Weaving (PT-related) is explicitly a Thread
  operation with Co-Movement card draw + P-01 auto-effects.
- ABSENT-BUT-PLAUSIBLE: insurgency_pipeline_v30.md GD-3 formation (territorial neglect → Uncontrolled
  → Insurgency) has no stated interaction with Gap/Knot mechanics, despite Uncontrolled/neglected
  territory being exactly the kind of substrate-adjacent event calamity_radiation matrices elsewhere
  key off of. No citation ties insurgency birth to a Thread event.

## Dramatic legibility
Answerable: mostly yes. Whose position is at risk — legible via per-territory Accord/Turmoil
dashboards and GD-2 mandatory-response triggers. What does each actor want — well-differentiated
via §0.5/§5 toolkits (Crown=hegemony via Treaty, Church=Seizure, Hafenmark=dynastic claim, Varfell=
conquest only, RM=cultural presence). What happens if no one acts — mechanically explicit and
autonomous (Accord 1→0 auto-Revolt, Insurgency auto-formation, GD-2 auto-mandatory-actions).

## Candidate degenerate lines
- Total-hegemony-only endgame: since GD-1 struck all alternates/Partition, every faction's optimal
  play converges on the same terminal shape (15/15 + Accord2 + Turmoil≤6); the "myriad paths"
  promise is delivered at the tactical layer, not the strategic-shape layer.
- Insurgency-as-shortcut: GD-3/§7.1 states a Promoted Faction wins at "11+ territories" (see finding
  below) — if literally implemented this would be a materially *easier* win condition than every
  established faction's 15/15, a structural asymmetric degenerate path (not reflected in sim, which
  hardcodes 15 for all factions — so currently only a doc-level risk, not an implemented one).

## Edges in/out
- IN from mass_battle_v30 (Battle resolution → MS/Accord/Turmoil consequences) — implemented.
- IN from restoration_movement/conviction_track (PT decay → Latent RM → Insurgency Stage1/2) —
  implemented per insurgency_pipeline §2-3.
- OUT to GD-2 mandatory-action pass (Accord thresholds trigger Muster/Govern) — implemented.
- OUT to parliamentary_transfer/social_contest (non-parliamentary status gates) — implemented per
  insurgency_pipeline §4.3/§5.3.
- OUT to player_agency Scene Slate (territory Accord 0, mass battle in player's territory = Priority
  0 mandatory scenes) — implemented (§4.2 Step 1).
- LATERAL to peninsular_strain_v30 itself — DIVERGENT: victory_v30.md §0.1 Partition is marked
  [SUPERSEDED-BY: GD-1]; the identical content in peninsular_strain_v30.md §6.3 carries no such
  marker (see finding).

## Directions
- top-down: GD-1's philosophy (non-dominance, no solvable strategy) sits in tension with GD-1's own
  mechanic (single victory shape) — the pressure system mitigates but doesn't resolve this.
- bottom-up: sim/autoload/victory.py correctly implements "all 15," contradicting the doc-level
  "11+" citation in insurgency_pipeline_v30 — sim is the trustworthy layer here, not the newer doc.
- lateral: peninsular_strain_v30.md (sibling, same scale) missed the GD-1 propagation pass that
  victory_v30.md received.
- diagonal: Battle→MS coupling connects the strategic layer to the Thread-crisis scale directly.
- forwards: GD-3 pipeline is fully specified with sim modules named but several are marked
  "pending Pass 2l" in canon/02_canon_constraints.md §B cross-references — worth checking Pass 2l
  landed before treating insurgency as implementation-ready.
- backwards: victory_v30.md still carries a stale open item citing "pending Varfell Path B user
  decision (ED-311)" in its header even though GD-1 already struck all Path B variants — an
  uncleaned stale-decision citation.

## Findings detail (for structured output)
F1 [NEW, P2]: insurgency_pipeline_v30.md §7 and §7.1 state Promoted Factions win "once they hold
11+ territories sustained 2 seasons" — contradicts GD-1's own "all 15" text (canon/
02_canon_constraints.md §B GD-1) and victory_v30.md §0 / peninsular_strain_v30.md §6.1, and
contradicts the actual sim implementation (sim/autoload/victory.py VICTORY_THRESHOLD=15, applied
uniformly to all faction_id including insurgencies). Same wrong "11/15" figure also appears in
references/canonical_sources.yaml (FACTION-SPECIFIC-VICTORY-PATHS replacement note) — recurs
across 2 files, not a one-off typo. Divergent status: doc claims a different threshold than the
implemented sim.

F2 [NEW, P2]: peninsular_strain_v30.md §6.3 "Co-Victory: Peninsular Partition" is live, unmarked
canonical text describing a co-victory that GD-1 (canon/02_canon_constraints.md §B, 2026-05-17)
explicitly STRUCK (confirmed by references/canonical_sources.yaml FACTION-SPECIFIC-VICTORY-PATHS
entry, which lists "Partition Co-Victory" among struck items). victory_v30.md §0.1, which carries
near-identical content, DID receive a [SUPERSEDED-BY: GD-1] banner (2026-05-17). The GD-1
propagation cross-reference list in canon/02_canon_constraints.md §B (lines ~54-59) never names
peninsular_strain_v30.md, explaining the gap. Co-filed/sibling doc missed a propagation pass.

F3 [KNOWN-TRACKED, module_contracts.yaml victory gap_notes]: MS is an "unowned clock" at the
victory gates (g_ms0/g_ms5/g_msrec) and world-state era transitions (Post-Calamity/Occupation/
Anarchy) are UNKEYED — no Key event exists for era changes. Added scope beyond bare tracking: this
directly undermines the Ω "autonomous world" clause's *legibility* — the game's three terminal/
era-shift states (the most consequential world-state changes in this subsystem) are invisible to
the articulation/Key stream, so no narrative surface can react to or foreshadow them.

F4 [NEW, P3]: canon/02_canon_constraints.md GD-1 text names the Turmoil track "Political Stability"
— no design doc (victory_v30, peninsular_strain_v30) or params file defines a "Political Stability"
track; it's Turmoil (0-10) throughout. sim/autoload/victory.py aliases it via an unlabeled inline
comment only. A designer resolving GD-1 literally would not find this track by name.

F5 [NEW, P3]: victory_v30.md retains a stale open-item citation ("Status: DESIGN — pending Varfell
Path B user decision (ED-311)") in its header even though GD-1 (2026-05-17) already struck all
Southernmost Dominion / Path B variants per canonical_sources.yaml — an uncleaned dangling
decision-pointer post-supersession.

F6 [NEW, P3, candidate/UNDETERMINED]: victory_v30.md's own cross-references (header "See also",
§0 "Full rules," §0.5 "Full specifications") all point to "designs/board_game/peninsular_strain_v1.md"
— a path/version that does not exist (actual file: designs/provincial/peninsular_strain_v30.md).
This exact stale path string recurs in ~15+ other corpus files (grep), suggesting a corpus-wide
rename that was never propagated to citations — flagging for this lane's territory but likely a
broader, possibly-already-known cross-cutting issue (not confirmed tracked).

F7 [top-down, P2, UNDETERMINED/DELIBERATE-per-Jordan]: GD-1's replacement of 8 faction-specific
victory conditions + Partition co-victory with one universal "conquer everything" endpoint is a
Jordan-directed hard rule (HR-1), so likely deliberate — but it measurably narrows the space of
*distinct victory shapes* from ~9 to 1, in tension with the charter's "myriad options and decisions"
North Star at the strategic-shape level (tactical-path variety via toolkits is preserved; ending
variety is not). Flagging as a design-tradeoff observation, not a bug.
