# Working notes — S5 Worked Season Trace (ARC-S07 Torben Loyalty Clock)

_Drafter lane, 2026-07-05. Working tree only. These are my scratch reductions; the polished
deliverable is `spec_sections/s5_season_trace.md`._

## Sources locked before drafting
- Charter capstones 1–12: `00_engine_charter.md:153-164`. C1–C7: `:24-41`. Q1–Q4: `:43-135`.
  Substrate contract / total accounting: `:137-151`.
- ARC-S07 register entry: `references/arcs/arc_register_factions.md:10-11` (IP30→Tutoring Demand;
  Loyalty 8→0 at −1/season on Covert Contact fail Intel vs Ob3; ≤3→Coup Counter +1; ≤2→Crown
  Mandate −2 cumulative; 3 consecutive contacts → floor 6; Laskaris PROTECTIVE delay+flip;
  Direction sentence).
- Full walkthrough + decision tree: `tests/sim/sim_arc_01_irrational_player_arcs.md:24-84`
  (three endings: retrieved / Altonian / dead; the CI→Domain-Action→Sovereign-Constraint seed;
  Debate-vs-Himlensendt, Elske recruitment, IP-B/IP-D/IP-F irrational branches).
- Cross-refs: ARC-S20 Ehrenwall's Count `:19-20`; ARC-T02 Almud Belief crisis `:40-41`;
  ARC-T13 Torben-after-Crown `:43-44`; ARC-S35 Succession Vacuum `:31-32`; NPC-ARC-LAK Laskaris
  flip `:312-313`.
- COLLISION-C Tutoring+Southernmost: `arc_register_events.md:37-39` (ARC-T04 is the dangling
  constituent — synthesis fork 2).
- Render triggers: `articulation_layer_v30.md:81-92` (10-trigger table); trigger-9 cosine spec
  `:94-110` (`abs(sim)>0.40`, 4-season window, corr +0.937 one faction pair); significance form
  `:127-137`; §6.4 combat_resolved `:294-298`; pacing DEFERRED `:304`.
- Register axes: `02_prose_render_stack.md` (Coherence ladder, Spirit, Certainty §18, chronicler
  fixed Cert/TS pairs). Bake key: `dossier_nlg_graduation`.
- Transport type-check: `scale_transitions_v30.md:173` (§5 Domain Echo), `:302-335` (§12
  all-directions; §12.3 populate sub-scale targets; §12.4 scenario_authoring→settlement_layer
  down-seam; §12.5 NERS note).

## Illustrative PC
"Ser Halden" — a Crown household agent, former sword-tutor to the heir Torben, Bonded to Torben,
Duty to Crown. Illustrative only, NOT a canon NPC [UNGROUNDED — PC identity is a trace vehicle;
every mechanic it touches is cited]. The tie-graph edges Bond(Halden,Torben)+Duty(Halden,Crown)
are what the casting resolver matches — that is the grounded part.

## Spine chosen
Season-2 covert contact partially FAILS (drives Loyalty→3 by Autumn) → richest capstone coverage
(convergence, coup chain, foreclosure). The success spine is carried in the divergence table
(capstone #3) and the seed-42 sketch (capstone #11), so both branches are shown.

## Adversarial fixes applied in the trace (map)
- BLOCKER bake-volume → render-register note + open flag O-6 (350-450 only under fork-6 fallback;
  default = low-thousands).
- BLOCKER anti-oatmeal → two-seed sketch states slot-filler divergence is structural, PROSE
  distinctiveness is NOT; ERA over 5 fixed seeds is an UNBUILT Stage-5 blocker.
- convergence_fired_set ORD-2 → Beat 3.2 uses order-preserving dict key, not set().
- Top-N tiebreak → scheduling sidebar mandates (salience DESC, tier_rank, id ASC).
- cosine ±0.40 float nondeterminism → Beat 3.2 quantize-to-integer-grid + sorted summation + port pin.
- realizer fragment selection → render sidebar: zero-randomness pure fn OR (campaign_seed,key.id)
  sub-stream; forbid string-hash/dict/wall-clock; gate on RNG-MODEL-COLLISION.
- convergence-EFFECT fabrication → Beat 3.2 cosine-detected-outside-register = RENDER/CHRONICLE-
  ONLY, zero pressure_effects.
- scene_entered fork → open flag O-1 (restored as fork; key_substrate §8.5 L510 edit required).
- tension-curve vs no-designed-timing + graduates-deferred-spec → scheduling sidebar: director
  SUBTRACTS only (ration/demote), never inserts/reorders/delays/time-compresses; drop curve.
- engagement-window-divergence → Beat 2.1 divergence table proves ≥2 outcome classes → ≥2 states.
- foreclosure silent via passive clock → Beat 4.2: foreclosure only via edge_triggered event +
  mandatory Tier-3 chronicle render.
- pricing-preferred unenforced → accounting note: gating vectors must carry justification.
- watching/participating rubber-band → Beat 4.1 offer-not-outcome; CI counts offered windows.
- salience demotes player-pursued arc → scheduling sidebar: participated-in-last-K demotion-exempt.
- Stages 2-3 phantom engine_clock dep → open flag O-7 (gate Stage 2/3 behind Gate-0/ED-1051).

## Rung ladder traversed (capstone #1 needs ≥3)
individual (Torben the heir; Halden) → family (the dynasty: Almud father, Elske sibling-heir;
Bond/Knot cluster) → faction (Crown; Löwenritter via coup chain; Church as antagonist) → world
(Altonia / IP / peninsula). Four rungs.

(Full prose is in the deliverable.)
