# Working notes — S3 / Q4 render lane

## Status: working notes (render-lane drafter, 2026-07-05). Deliverable = `spec_sections/s3_q4_render.md`.

## Sources read in full / targeted (working tree)
- `00_engine_charter.md` (full) — Q4 = L107–135; constraints C1–C7 L24–41; substrate contract
  L137–151; capstones L153–164; PLOT/NOT-list L100–105.
- `02_prose_render_stack.md` (full) — 4 modulation axes; articulation socket §5; NLG proposal (c);
  named gaps (e) 1–6 (schema, bake, runtime tables, pacing, ERA, texture).
- `03_articulation_nlg_architecture.md` (full) — §2 four orthogonal factors; §4 output-mode dial;
  §5 dual-register; §8 offline bake; §9 oatmeal register; §10 slots-in / open decisions.
- `01_arc_corpus.md` (full) — ARC-S07 anatomy (b); seed method + fixed SEEDS [42,77,99,137,201] (a).
- `articulation_layer_v30.md` (full) — §3.1 trigger table (10 triggers, #9 cosine, #10 belief);
  §3.2 significance (0–13); §3.3 starvation accumulator; §3.4 two render styles (flash/scene);
  §4 chronicle (§4.3 Top-N universal); §5 socket; §6.4 combat_resolved [ASSUMPTION] L294-298;
  §7 D11 pacing DEFERRED L302-304.
- `coherence-tiers.md` (full) — 6 tiers; Author×TS weight tables; Spirit modifier C≤4; 216 cells.
- `solmund_voice_v30.md §18` — Certainty register 5 rows (1-2/3/4/5/6+); gap at Cert-0; out-of-range 6+.
- `prose-writer/SKILL.md:151` — four chroniclers fixed Cert/TS (Church5/Hafenmark4/Restoration2/Warden0-TS70+).
- `threadwork_v30 §3.7` L719-725 — the four ED-681 beats: Withdrawal / Knot Anchoring / Place
  Anchoring / The Choice (C6).
- `player_agency_v30 §4` — 3-5 scene actions; §4.3 slate sizes L300-302; §4.2 priorities.
- `propagation_spec_v1` — O.3 ORD-2 (no set() gates order); O.5 RNG-MODEL-COLLISION + RNG-1/2/3;
  O.6 ORD-3; O.8 V4 "same rendered text" precondition set.
- `synthesis.md` (full) — L5 render; §6 render gap; §8 new Key types; §10 conformance; §11 forks.

## Key structural decisions (grounded)
1. Surface map = articulation's 3 tiers + texture (new) + slate. Cut scenes = ONLY interruption
   (charter L109). Routing keyed to Coherence (protagonist frame) + Certainty (ecclesiastical/
   chronicle). Both are realizer band inputs, never surfaced as numbers.
2. Venue matrix: every beat AT a location / THROUGH a venue / IN chronicle (L116). Realizer supplies
   prose skin only; the resolving subsystem owns the scene (C3). `beat-has-venue` rule = capstone #7.
3. Watching/participating: OFFER-not-outcome (M12) — FSM advances regardless of participation, an
   all-ignored major arc still converges; guarantee counts OFFERED windows. `watching-participating`
   rule + `engagement-window-divergence` rule (M9, closes illusory choice = capstone #3).
4. Trails = `causes[]` walk as in-world media (PP-687 §5.4; articulation §2.2 "Why?" walk).
   Investigation = trail consumer (fieldwork case board). Deterministic (render-is-pure).
5. Showing (present-tense cut/slate/texture) vs telling (chronicle retrospect) = output-mode dial
   (NLG §4). Foreclosure: `foreclosure-via-arc-event` (M10a, no passive-clock foreclose) +
   `foreclosure-must-render` (M10b, mandatory Tier-3 beat — positive-surfacing, distinct from
   discard-with-reason).
6. Realizer schema: fragment {key_type, significance_band(2 styles), band{coherence,ts,spirit},
   certainty_register, focalizer, slots, text, degradation_rule_ref, guards, connectives,
   provenance}. Slots from existing Key metadata only. ARC-S07 worked example.
7. Coherence table = bake-time budget (216 cells), runtime = deterministic exact-match. Certainty
   table = runtime lexicon-swap over the same pool (orthogonal to Coherence). Cert-0 gap flagged.
8. Per-NPC overlay = DISTINCT bake line item (M8): budget 35 × triggers × variants (~1,050 top-end),
   NOT 3-5×35 floor. Craft cost not certified by combinatorics.
9. Bake volume (M8/B1): honest dual figure — ~350-450 ONLY if Certainty=lexicon-swap (fork-6
   fallback); low-THOUSANDS under charter-default (Certainty in pool, 5-6×). Withdrew "feasible"
   headline against the default; carried CONDITIONAL-feasible verdict.
10. Render determinism (M4): `render-is-pure` — zero-randomness pure function (default) OR dedicated
    render sub-stream (campaign_seed,key.id) after RNG-3; forbid string-hash/dict-iter/wall-clock/
    shared World.rng. `total-order-selection` tie-break (M2) on fragments AND rationing Top-N.
    RNG-MODEL-COLLISION disposal = Stage-0 render precondition.
11. Convergence render (M5): cosine-detected convergences outside the 8 register-authored set =
    RENDER/CHRONICLE-ONLY, zero pressure_effects; `convergence-effect-provenance` rule traces every
    delta to a register line. Keeps cosine generality without fabrication or a hardcoded-8 whitelist.
12. Director (M7/M13): DROP tension-curve authorship. Subtract-only ceiling — cap/demote/select,
    never insert/advance/re-time (doc-10 §8.5 NOT-list stands, C7). `director-subtract-only` rule.
    Tension curve = read-only observation at most. `player-pursued-demotion-exempt` (M14) floors
    PC-participated arcs (K=3 default) against demotion railroad.
13. Legibility triad per surface (`legibility-triad` rule); UI ceilings 3-4 trackers, no mech vocab
    (C4 slot-type + C2 lint).
14. Anti-oatmeal (B2): Defense 1 vector-as-data = slot-filler divergence ONLY, NOT prose
    distinctiveness (withdrew "by construction"); Defense 2 ERA = UNBUILT, Stage-5 blocker;
    Defense 3 = 5-seed narrative regression, red until ERA exists. Arc-specific authored color =
    distinct bake line item.

## Adversarial findings disposition
- BLOCKERS B1 (bake volume dual-figure) + B2 (anti-oatmeal not structural) — APPLIED in Q4.6.5 / Q4.9.
- MAJORS applied in-section: M2 (total-order tiebreak Q4.6.6.1), M4 (render-is-pure Q4.6.6), M5
  (convergence provenance Q4.6.7), M6+M15 (scene_entered fork restored + §8.5 edit deliverable
  Q4.10/Q4.11), M7+M13 (director subtract-only Q4.7), M8 (per-NPC line item Q4.6.4), M9
  (engagement-window-divergence Q4.3), M10 (foreclosure rules Q4.5), M12 (offer-not-outcome Q4.3),
  M14 (demotion-exempt Q4.7).
- MAJORS carried as cross-lane open flags (Q4.11): M1 (convergence_fired_set ORD-2 → detector lane),
  M3 (cosine/meaningfulness float determinism → detector lane), M11 (pricing-preferred → compile
  lane), M16 (Gate-0/engine_clock gating tick/detect stages; render Stage-0 is clock-independent).

## Open items / uncertainties
- Fork 6 (Certainty in pool) is the single biggest swing; flagged as charter-authority default but
  volume headline honestly low-thousands. Jordan decides bake budget.
- scene_entered: charter says [OPEN — Jordan]; synthesis over-resolved. Restored as held-back fork
  requiring the key_substrate §8.5 edit in the same PR (ED-1094 loud-exception discipline).
- ERA is the gating unknown for the anti-oatmeal capstone — Stage-5 blocker, not satisfiable now.
