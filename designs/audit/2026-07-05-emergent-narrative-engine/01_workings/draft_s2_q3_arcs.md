# Working notes — Q3 (arcs) spec-section draft

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0068]
_Deliverable = `spec_sections/s2_q3_arcs.md`. These are the reasoning/grounding/finding-application notes behind it._

## Grounding read (working tree only)
- `00_engine_charter.md` FULL — Q3 L81–105, C1–C7 L24–41, substrate contract L137–151, capstones L153–164.
- `01_arc_corpus.md` FULL — entry anatomy §a, ARC-S07 §b, T-23/T-24 §d, hooks §e.
- `02_prose_render_stack.md` FULL — modulation axes, articulation socket §b, NLG proposal §c, gaps §e.
- `synthesis.md` FULL — six-layer architecture, arc_vector schema §2, detector §3, forks §11.
- `dossier_register_formalizability.md` FULL — schema §2, %s §3, gaps §4, ARC-S07 §5, COLLISION-C §6.
- Canon cited directly: `arc_register_events.md` §V–VI (COLLISION A–J, L25 "not predictable"), `arc_register_factions.md:10-11,32,38,41,43-44` (ARC-S07/S20/S35/T02/T13), `articulation_layer_v30.md` §3.1 (trigger-9 cosine, L94–112), §3.2 (sig 0–13), §3.3 (accumulator), §7 (pacing DEFERRED), §10 (D11=Deferred), §6.4 (ED-936 ASSUMPTION), `propagation_spec_v1.md` O.3 ORD-1/2, O.4 SSI, O.5 RNG + RNG-MODEL-COLLISION, O.6 ORD-3, O.7 ORD-4, O.8 V4.
- Dossiers from task prompt: content_economics (350-450 vs low-thousands, per-NPC floor), nlg_graduation (ERA unbuilt, 5 seeds).

## Required deliverables — coverage map
- Story-vs-context threshold + meaningfulness test → §Q3.0, §Q3.1 (binary membership + 3-factor integer product).
- Emergence-vs-noise correlation tests + discard path → §Q3.2 (Tier A register conjunctions effect-bearing; Tier B cosine RENDER-ONLY; FIRED/DETECTED-RENDER-ONLY/DISCARDED).
- Arc taxonomy + lifecycle FSM → §Q3.3 (5 measurable axes; seeded→…→terminal FSM; ED-IN-0003 ownership).
- Concurrency/braiding/causes[]-raising → §Q3.4 (per-tier budget, participating_actors braiding, ~15%→75-85% causes[] rate, CR-5).
- Salience economy → §Q3.5 (foreground budget CEILING, §3.3 accumulator generalized, total-order tiebreak, player-exempt demotion, C2 lint).
- Slow/fast NPC variables → §Q3.6 (variable-cadence contract table + per-NPC bake caveat).
- One-ledger rule → §Q3.7 (progression IS narrative state, no new currency, co-protagonists).
- PLOT + CAN/CANNOT → §Q3.7 (4 moments; director-subtract-only; CAN 7 / CANNOT 6).
- Typed arc_vector schema → §Q3.8 (full pseudo-YAML + compile reality + gating:pricing).
- Full worked ARC-S07 → §Q3.10 (typed vector + 6-step end-to-end trace + verdict).
- Conformance CR-1..CR-12 → §Q3.9.
- Forks + held-back calls → §Q3.11; cross-lane seams → §Q3.12.

## Adversarial findings — application ledger (BLOCKERS mandatory; MAJORS apply-or-rebut)

### BLOCKERS (both applied)
- **B1 bake-volume** → APPLIED in §Q3.8 "Render binding" + fork 6. Headline is now LOW-THOUSANDS under fork-6 default (Certainty in pool, ~5-6×); 350-450 is the conditional (lexicon-swap fallback) figure. Removed the unconditional "feasible".
- **B2 anti-oatmeal not structural** → APPLIED in §Q3.8. Withdrew "by construction"; vector-as-data = slot-filler divergence only; prose distinctiveness needs ERA bake gate over 5 fixed seeds; ERA UNBUILT = Stage-5 blocker; arc-specific color = distinct line item.

### MAJORS owned by Q3 → APPLIED in doc
- convergence_fired_set ORD-2 → CR-1 ordered dedup key (§Q3.2).
- L3 rationing tiebreak → CR-6 total order (salience DESC, tier_rank, id ASC) (§Q3.5).
- ±0.40 cosine + meaningfulness float product → CR-11 integer/fixed-point + port parity (§Q3.1, §Q3.2).
- convergence-EFFECT fabrication seam → CR-2 cosine-detected = RENDER-ONLY zero pressure_effects; register-trace required (§Q3.2).
- tension curve vs no-designed-timing NOT-list + director graduates DEFERRED D11 → merged ruling: DROP tension-curve; director = stateless SUBTRACT-only ceiling; CR-9 (§Q3.7). Grounded in articulation §7/§10 D11=Deferred.
- engagement-window-divergence → CR-3 (≥2 outcome classes → ≥2 next states; illusory-choice compile flag) (§Q3.3).
- foreclosure silent via passive clock → CR-4 (foreclosure only from edge/convergence; mandatory Tier-3 chronicle) (§Q3.3).
- pricing-preferred unenforced → CR-10 (gating:pricing ratio + why-not-pricing note) (§Q3.8).
- watching/participating rubber-band → folded into Q1/Q4 lane but the OFFER-not-outcome principle stated via ARC-S07 step 4 ("ignoring is remembered, never a pause; FSM ticks on schedule"); full invariant is Q4's — noted as seam.
- salience demotes player-pursued arcs → player-participated demotion exemption (K seasons) (§Q3.5).

### MAJORS owned by other lanes → recorded as seams/forks (rebutted-as-deferred with recommended fix carried)
- scene_entered silently resolved vs charter [OPEN] → RESTORED as explicit held-back fork, §Q3.11; recommended game_director single-source; flagged for PR body.
- scene_entered inconsistent with key_substrate §8.5 → §Q3.11 requires an explicit §8.5 edit in the same PR; until then it stays a fork.
- L5 realizer fragment-selection determinism / RNG-MODEL-COLLISION → §Q3.12 (Q4 lane); carried the recommended fix (pure-fn or dedicated render sub-stream seeded (campaign_seed,key.id); forbid hash/dict/wall-clock).
- Stages 2-3 phantom-depend on engine_clock/ED-1051 → §Q3.12 (staging); gated behind Gate-0 per J-2.
- per-NPC voice budgeted at name-swap floor → §Q3.6 ruling: distinct bake line item 35×triggers×variants (~1050 ceiling), not 3-5×35; feasibility conditional.

## Key design decisions / rationale
- **Story-vs-context is set-membership, not a classifier** — the charter's "arc membership decides, not event type" (L83) is the whole architecture; discriminators are questions asked of an already-instantiated vector, not independent sorters.
- **Two-tier detector with asymmetric effect authority** — register conjunctions bear authored deltas (they're the only place combined pressure is authored, `arc_register_events.md` L25); cosine tail is detect+render only. This threads the needle between hardcoded-8 scripting drift and fabricated deltas — the single most important structural ruling in the section.
- **All replay-critical thresholds ruled to integer arithmetic** — meaningfulness product, cosine compare, rationing sort, dedup key. This is the recurring V4/ED-1050 determinism class; numbers stay [OPEN — Jordan tuning], arithmetic is structure.
- **Director de-scoped to subtract-only** — the biggest correction vs synthesis §4, forced by articulation §7 (pacing DEFERRED, nothing to graduate) + doc-10 §8.5 NOT-list. Preserves emergent timing.

## Open items / residual risk
- COLLISION-C stays blocked by ARC-T04 (fork 2) regardless of schema quality — ARC-S07 still feeds B/F.
- Axis 9 (ARC-P04) has no clock home — open-number gap, not addressed structurally here (register-side fix).
- The exact tier_rank axis weights, meaningfulness cutoff, concurrency caps, K exemption window = all [OPEN — Jordan tuning].
- ERA must be built (Stage-5 blocker) before anti-oatmeal capstone #11 can be certified.
