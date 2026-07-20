# Churn Amendments — v2 deltas to the v1 normative chapters (s1–s5)

## Status: RATIFIED (Jordan, 2026-07-05, PR #78; ED-IN-0011 — companion to ../narrative_engine_design_v2_churn.md; the chapters remain normative except where amended here)

Each v1 chapter stays in force; this file is the authoritative delta list. Where a delta and
the chapter text conflict, the delta wins pending the chapters' next full revision.

## s1_q1_q2.md (Q1 player→world · Q2 world→player)

- Casting SELECTION is unchanged (tie-graph + realized state only — v2 §4's forecast
  severance; forecast terms never pick who is summoned). What changes is the summons'
  RENDER: it carries a computed stakes-preview ("what happens if no one acts" = the §3
  horizon rendered diegetically under v2 §6's never-a-meter / never-a-promise rules),
  replacing s1's authored-clock-text impulsion.
- The four option-conditioning modes now cite **computed horizons**: gating/pricing/
  foreclosure previews come from `stake_horizon` objects (continuous-class per-lever only
  for M1, v2 §3), and foreclosure warnings from `foreclosure_countdown` — rendered as
  pressure, never as a countdown; every gate still cites its ledger cause.
- The anti-railroad window test upgrades: window realness is verified against
  **option-conditional distributions** (a real window = the per-lever horizon measurably
  differs), not only post-hoc seed comparison.
- Factionless mini-trace (Appendix A) unchanged — re-annotate its casting beats with the
  forecast columns when s5 is revised.

## s2_q3_arcs.md (Q3 legibility-as-narrative + register binding)

- **Story-vs-context threshold restated**: membership in the LIT SUBTREE (v2 §4), with the
  meaningfulness test as the candidacy gate — arc membership remains the mechanism, but arcs
  are now template INSTANCES (v2 §2), and the store is the generator's runtime, not a
  compiled corpus.
- The taxonomy gains the **template layer**: tier/shape (the ~13 structural shapes) above
  instance; census correction — the register is 138 entries, not ~110.
- The detector section is superseded by v2 §3: **actual + potential**, discovery over the
  ensemble with the 8 authored COLLISIONs demoted to priors (fixture F4). The
  edge-triggered-once conjunction machinery survives as the prior-evaluation path.
- The salience-economy section is **replaced** by a pointer to v2 §4 (the Light Function);
  s2's braiding/concurrency/causes[]-raising rules are absorbed as light-inertia and
  connectivity terms.
- ARC-S07 compile: stakes_tags `[pricing, foreclosure]`; Laskaris IP+3 as NPC-ARC-LAK
  cross_ref; the range conflict is fork 9; **ED-609 disposition carried** (compile does not
  depend on it; stays open).
- PLOT section: setup/escalation/turn unchanged; add the **projected-next-beat** object
  (v2 §6) as the forward-facing half; the CAN/CANNOT list stands.

## s3_q4_render.md (Q4 presence)

- The surface map gains the **forecast surfaces**: counsel/omen/rumor register
  (Certainty-keyed), NPC anticipatory behavior (diegetic heuristics over observable state —
  never engine forecast objects, R-AI; the F-C fork now scopes only which counsel/omen
  RENDER surfaces a position sees), Thread perception as the native forecast query,
  stakes-preview lines on slate entries, sparing chronicle counterfactual ghosts (F-D) —
  all under v2 §6's never-a-meter / never-a-promise render rules.
- The bake section gains: **bake directives as versioned data** (v2 §7); the author-weight
  tables as bake parameters (v2 §6); the census-grounded unit numbers (headline ~1,200–2,700
  under fork-6's include-default; 230–450 only under the lexicon-swap fallback); the
  **scale-complete bank matrix** (character/family/faction/settlement/
  territory/world with binding sources); aggregation templates as a bank class.
- Anti-oatmeal restated as the **five-property theorem** (binding/consequence/scarcity/
  memory/range); the two-seed test generalizes to the any-seed regression (F1).
- The four ED-681 thread-beat worked renders (Q4.6.8) stand unchanged.

## s4_substrate.md (the substrate contract)

- **New engine-owned state**: ensemble cache (per-Accounting), `stake_horizon` /
  `convergence_candidate` / `foreclosure_countdown` / `option_distribution` stores, the
  light ledger (per-thread inertia + budget), projected-next-beat register.
- **New conformance rules** (each one rule, one tools/ home; joining R1–R10): R-F1
  forecast/live shared resolver code (incl. the flag-gated scene-EV sub-clause) · R-F2
  ensemble determinism (sha256 over the canonical Key-log serialization, sorted iteration,
  integer basis-point marginals, integer light-inertia decay) · R-HB hard-bake AST hunt (no
  content literals in kernel) · R-CL grammar-closure (no Key family without a render path) ·
  R-AI forecast actor-invisibility (no actor resolver reads a forecast object) · R-RL
  re-light discipline (catch-up beats render-only + focalizer-cited).
- **READS addendum**: once the SC lane declares its precedent + commitment stores (v2 §5 —
  new stores, not existing substrate), the engine's render READS both — s4 §S4.1's READS
  column grows accordingly; the engine still OWNS only its one store.
- Module contracts annotated with the **kernel/data/wrapper tiers** (v2 §7); scenario_
  authoring's compile output declared a versioned data pack (starting conditions swappable).
- Total-accounting classes unchanged; forecast outputs are CONSUMED-INTO-STATE; discarded
  ensemble branches are not Keys (no accounting entry — they are computation, not events);
  DISCARDED-with-reason still applies to candidate beats the light declines.
- Determinism section: add the dossier's hazards + mitigations (frozenset ordering, erf/Φ
  portability, seed stability across save/load — never wall-clock).

## s5_season_trace.md (the worked season)

- Existing beats gain two annotation columns when next revised: **light** (score terms that
  lit the beat) and **forecast** (the horizon band the beat's summons carried).
- The three v2 authored mini-traces (ensemble-stats §9.1, zoom-coherence §9.2, claim-grammar
  §9.3) join the trace suite; Appendices A/B unchanged.
- Build-time fixtures F1–F8 (v2 §9, incl. F8's anti-self-fulfillment control) are the
  Stage-5 regression set this trace seeds.
