# Working notes — Q1/Q2 spec-section drafter

## Status: working notes (2026-07-05, Lane IN). Deliverable = `spec_sections/s1_q1_q2.md`.

## Grounding reads (working tree)
- `00_grounding/00_engine_charter.md` (full) — Q1/Q2 required-content lists, C1–C7, substrate
  contract, capstones.
- `00_grounding/01_arc_corpus.md`, `03_prior_art_and_module_homes.md` (full).
- `01_workings/synthesis.md` (full) — the architecture I'm drafting sections of.
- `designs/architecture/player_agency_v30.md` (full) — §2 Convictions, §3 Duties, §4 Scene Slate +
  7-priority + Witness Mode + §4.5 not-pursued table, §5 Stature/Renown/independent, §6 budget,
  §7.6 emergent arcs (prose-not-mechanism).
- `designs/npcs/npc_behavior_v30.md` — §5 arc FSM + §5.0b Knot-strain + §5.1 generic triggers + §5.2
  Almud Arc A (ED-672 foreclosure exemplar) + §8.11 Outreach/Demand generation.
- `designs/architecture/scale_transitions_v30.md` — §4.1/§4.3.2/§4.3.3 Zoom In (impulsion), §4.4
  Where-Were-You, §5 Domain Echo.
- `canon/02_canon_constraints.md` P-04 (no alignment system — hard boundary for ethics-as-pattern).
- `designs/architecture/holonic_container_doctrine_v1.md §2` (scripting-drift / shape-divergence
  guardrails).
- `references/arcs/arc_register_factions.md` (ARC-S07 exact deltas; ledger_cause example).

## Section scope delivered
Q1: participation-as-Key-emission (C3 book-venues loop); reach-scales-with-position (Domain Echo,
leader delegation as owned consequence, member missions, factionless Renown); non-participation as
input (OFFER-not-outcome invariant); the seven-surface durable ledger; ethics-as-pattern (P-04);
anti-railroad (window-divergence + attention-demotion-exemption + slate total-order tiebreak).
Q2: one tie-graph casting rule across all four channels; scene_entered restored as explicit fork;
positional story (leader concern/project filtered target=leader anti-spreadsheet; member
duties-with-refusal-costs under asymmetry; factionless vector ladder); social-scale ladder with
family rung bind-or-declare-absent; impulsion (diegetic clocks / forced-choice / refusal costs) +
tension-curve reconciliation; four option-conditioning modes each citing ledger_cause + pricing-
preference enforcement + foreclosure edge-only + mandatory-chronicle.

## Adversarial findings applied (in-scope for Q1/Q2)
- MAJOR scene_entered silently resolved → **restored as [OPEN — Jordan] fork** (§Q2.2), with the
  §8.5 L510 edit made a precondition of the default. Rebutted the synthesis "RESOLVED — not a fork".
- MAJOR watching/participating rubber-banding → **OFFER-not-outcome** invariant (§Q1.3, rule 6).
- MAJOR illusory-choice → **engagement-window-divergence** conformance rule 7 (§Q1.6).
- MAJOR attention-railroad → **player-pursued-arc demotion-exemption** rule 8 (§Q1.6).
- MAJOR tiebreak nondeterminism → **arc_vector.id total-order** tiebreak on slate injection (§Q1.6).
- MAJOR unenforced pricing preference → **pricing-preferred** rule 10 (ratio report + gating
  justification, §Q2.6.a).
- MAJOR silent foreclosure → **foreclosure-via-edge-only + mandatory Tier-3 render** rule 11
  (§Q2.6.b).
- MAJOR tension-curve vs no-designed-timing → **reconciliation clause** (§Q2.5): director may only
  ration/demote (subtract), never insert/re-time; dropped any tension-curve *ownership* claim from
  my sections.
- MAJOR convergence_fired_set ORD-2 → noted as an **inherited precondition** owned by the Q3/detect
  lane; casting must not re-introduce set order (§Q2.1 determinism note). Not owned here.

Blockers in the adversarial set (bake-volume 350-450; anti-oatmeal "structural by construction")
are in the RENDER lane (synthesis §6), NOT this section — I did not restate either claim here, so
there was nothing to walk back in Q1/Q2. Flagged that the two blockers land on the render lane.

## Genuine forks surfaced (see spec §Forks)
1. scene_entered ownership [OPEN — Jordan] (+ §8.5 edit precondition).
2. Coup Counter migration — both the foreclosure exemplar and ARC-S07 trigger on the STRUCK Counter.
3. K (demotion-exemption lookback) = 2 seasons [OPEN — Jordan tuning].
4. T-30 asymmetry — charter-named, no live home-doc cite verified this pass [UNGROUNDED].

## Key design decisions / rationale
- Kept the whole section on ONE substrate + ONE casting rule to honor C5 shape-non-divergence:
  every world→player channel is the same `participating_actors ∩ tie_graph` test; every
  player→world effect is the ordinary Key stream read by the FSM stepper. No per-channel dialect.
- Ethics-as-pattern deliberately routes through *existing* readers (npc_memory / Standing / Cascade)
  and Convictions-as-ledger, never a scalar — P-04 is a FAIL-if-present check, so I extended the C2
  lint to forbid a moral-valence scalar even internally.
- Family rung: made "never silently skip" a checked property (`ladder-completeness` rule) via an
  explicit `absent_deliberate` gaps[] entry — the honesty-ledger pattern from the register dossier.
