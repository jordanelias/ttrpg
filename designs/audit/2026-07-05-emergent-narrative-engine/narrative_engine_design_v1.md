# Valoria — The Emergent Narrative Engine · Design v1

## Status: PROPOSED (Jordan-vetoable throughout; open forks §5; held-back items flagged in the PR body)
## Date: 2026-07-05 · Lane: IN (claims homes in the articulation/arcs/scene cluster) · Branch: `claude/ners-audit-fable5-9cpfdz`

**What this is.** The design spec + module contract for the engine that does what Valoria's
absent GM would do: notice that independent mechanical vectors have converged into a story,
decide it matters, call the player into it, and tell it in prose whose register tracks Coherence
and Certainty. Executes **ED-IN-0003** (convergence detector/applier) and **ED-IN-0004**
(articulation trigger completion) by construction; organized around Jordan's four key
considerations. Charter: `00_grounding/00_engine_charter.md` (Q1–Q4, constraints C1–C7, the
substrate total-accounting contract, 12 capstone requirements).

**Method.** 25-agent adversarial workflow: 4 source dossiers → 3 independent architectures →
3-judge panel → synthesis → 5 adversarial refuters (2 BLOCKER + 21 MAJOR findings applied or
rebutted) → 5 spec-section drafters → 3 capstone verifiers (all PASS-WITH-FIXES; fixes applied)
→ completeness critic (all gaps remediated or flagged). Full provenance: `01_workings/`.

---

## 0 · The architecture in one paragraph

**The Arc-Vector Engine with a Subordinate Director** (judge tally: B won all three lenses —
player-experience 82, architecture-integrity 84, buildability 85 — with mandatory grafts from
A and C). Six layers, **detect-THEN-schedule-THEN-render**: the arc register compiles OFFLINE
into a frozen typed arc-vector corpus (L0, `scenario_authoring` — PP-690 realized, and the
typed engine-params asset CLAUDE.md §5 wants); `game_director` owns the live vector store and
steps lifecycle FSMs on the Key stream each season (L1 — the world proceeds with zero player
Keys); a two-tier detector evaluates convergence over SETTLED state at the Accounting boundary
(L2 — the 8 authored COLLISION conjunctions as edge-triggered-once typed predicates, plus the
sim-validated cosine-similarity backbone generalized from articulation trigger-9, closing
ED-IN-0003); a **subordinate** director rations detector output into player_agency §4.3's 3-5
scene envelope with a salience economy and texture demotion (L3 — a ceiling, never a floor:
C7); one tie-graph casting rule injects arc-tagged candidates into the existing 7-priority
slate (L4 — why-you is always a citable edge); and the graduated NLG realizer + completed
articulation trigger table render the result deterministically (L5 — closing ED-IN-0004 and
C6). Scenes always resolve through the ordinary subsystem engines — the engine books venues,
never owns resolution (C3).

## 1 · The four questions, answered (normative spec chapters)

The full normative text lives in five chapters under `spec/` — each grounded, adversarially
refuted, and capstone-verified:

| Chapter | Contents | Answers |
|---|---|---|
| `spec/s1_q1_q2.md` | Participation-as-Key-emission; position/reach; non-participation as input; the durable ledger + ethics-as-pattern; anti-railroad. Casting tie-graph; positional story (leader/member/factionless ladder); the social-scale ladder (per-rung carrier/surfaces/ties, family rung disposition); impulsion; the four option-conditioning modes with cite-your-ledger-cause. | **Q1 + Q2** |
| `spec/s2_q3_arcs.md` | Story-vs-context = membership in the live vector store; meaningfulness test (durability × tie-proximity × identity-touch); emergence-vs-noise correlation tests + explicit discard; arc taxonomy + lifecycle FSM; braiding/concurrency; salience economy; slow/fast NPC variables; one-ledger rule; PLOT (forwards-pressure / backwards-story) with the CAN/CANNOT list; **the typed arc-vector schema + the full ARC-S07 compilation**. | **Q3** + register binding |
| `spec/s3_q4_render.md` | Five-surface map with Coherence/Certainty routing; venue matrix + no-popup rule; watching-vs-participating (offered-not-taken, honestly stated); trails; the **NLG realizer graduation** (fragment schema, bake protocol, runtime-executable coherence-tier + Certainty-register tables, per-NPC overlays); beat budgets; legibility acceptance criterion; the three anti-oatmeal defenses; **worked renders of all four ED-681 thread beats** (C6/P-14 discharge). | **Q4** |
| `spec/s4_substrate.md` | OWNS/READS per scale; Keys-in (subscription, Accounting cadence vs ORD-1..4, filtering ladder, V4 replay); Keys-out **total accounting** (rendered/accumulated/consumed/discarded-with-reason — zero silent drops); verbatim-ready `module_contracts.yaml` + `key_type_registry` entries; the declared-vs-implemented edge table; six directions with ordering notes; **conformance rules R1–R10** (canonical numbering), each with a named `tools/` home. | Substrate contract |
| `spec/s5_season_trace.md` | The worked 4-season ARC-S07 (Torben) trace hitting all 12 capstone requirements, incl. the total-accounting table, the two-seed divergence sketch, **Appendix A: the factionless mini-trace** (Jordan's named acceptance test) and **Appendix B: an effect-bearing register-authored COLLISION firing**. | Capstone proof |

## 2 · What it closes, what it claims

- **ED-IN-0003 (F-2)** — closed by L2: COLLISION A–J become typed, edge-triggered-once
  predicates over settled state; the cosine backbone supplies the temporal window the authored
  rows lacked; non-firing markers are DISCARDED-with-reason (total accounting), never silent.
- **ED-IN-0004 (F-4)** — closed by L5 + Stage 0: articulation §3.1 gains
  `scene.combat_resolved`, `scene.investigation_resolved`, the four ED-681 thread beats
  (worked renders in s3), and the two new meta Keys; the §6.4/ED-936 false assertion is
  corrected at its root.
- **Module homes claimed** (flipping doc:nulls): `game_director` (runtime spine),
  `scenario_authoring` (offline compile home + PP-690 campaign-skeleton seeds), `scene_slate`
  (demoted to candidate generator — the `mechanical.scene_entered` ownership conflict resolved
  to game_director single-source, with the required `key_substrate §8.5` co-edit flagged).
- **New Key types: exactly two** — `meta.convergence_detected`, `meta.arc_state_changed`
  (Class B, consumer-closed, C2-internal labels; a flagged fork against B's zero-new-types
  purity).
- **The corpus defects the compile surfaced** (dossier findings, now tracked in §5 forks):
  Coup Counter STRUCK but still triggering 6 register entries; ARC-T04 dangling (COLLISION-C
  blocked); Torben Loyalty range conflict (register 8→0 vs clock_registry 0–7); TC→CI / RS→MS
  aliasing throughout the register.

## 3 · Staging (each stage independently mergeable)

- **Stage 0 — Render-gap close** (independent, rides existing homes; NOT behind the compiler):
  articulation §3.1 completion + NLG graduation + C2 bake lint. Closes ED-IN-0004 + C6.
  *Honest cost note: the code/doc edit is near-zero; the fragment authoring for the new
  triggers is not (see s3's bake accounting).*
- **Stage 1 — Compile gate**: register → typed corpus (~45% compiles now; ~40% needs the
  lifecycle field; ~15% declared non-firing in the honesty ledger). Blocked on forks 1–2
  (Coup-Counter remap; ARC-T04 strike-or-author).
- **Stage 2 — Store + tick** (L1): autonomous progression. **Stage 3 — Detect** (L2): fully
  closes ED-IN-0003; blocked on fork 3 (temporal window). **Stage 4 — Schedule/cast/inject**
  (L3+L4) + the ORD-4 scene-queue fix + scene_entered resolution. **Stage 5 — Texture +
  conformance suite (R1–R10) + the capstone trace as a regression fixture.**
- Gate-0 honesty (refuter-forced): Stages 2–3 presume the engine-clock/Accounting-boundary
  substrate — their contracts are written against `propagation_spec_v1` and land behind
  ED-1051's resolution, consistent with strategic_judgments J-2 (no deepening past R3 before
  Gate-0; Stages 0–1 are the pre-Gate-0 work).

## 4 · Determinism & replay (V4)

Same Key log → same narrative state → same rendered text, conditional on the already-flagged
ORD-3/ORD-4 substrate flags plus the refuter-forced additions now in s4: the
`convergence_fired_set` ordered-iteration rule (the second ORD-2-class hazard the refuters
caught), integer-basis-points salience with total-order tiebreak (no float boundary
nondeterminism), and content-addressed fragment selection (no hash-seed/dict-order leakage).
The conformance suite (R1–R10) checks each mechanically.

## 5 · Open forks — Jordan's, never silently resolved

Stated as fork → recommended default; full wording in the chapters' `[OPEN — Jordan]` flags:

1. **Coup-Counter migration** → default: 1:1 threshold remap onto the Löwenritter Autonomy
   track (unblocks 6 register entries + COLLISION-F). Blocks Stage 1.
2. **ARC-T04 / Southernmost Ritual** → default: strike the two dangling cross-refs
   (COLLISION-C → 7-of-8), defer fresh authoring to a WR-lane ED.
3. **Convergence temporal window** → default: same-Accounting for the 8 authored conjunctions;
   4-season ±0.40 cosine window for the backbone. Blocks Stage 3.
4. **Two new Key types vs zero-new-types purity** → default: add both (total accounting, not
   type-count, is the invariant).
5. **Lifecycle-field ownership** → default: game_director-owned store; the npc_behavior
   arc-state bucket stays the specialization it reads.
6. **Bake key includes Certainty** → default: include (charter authority) — swings bake ~5-6×;
   fallback: Certainty as runtime lexicon-swap. Tuning-adjacent.
7. **GM-judgment-irreducible ~15%** → default: declare non-firing in the honesty ledger;
   author decision functions case-by-case later (C5 protection).
8. **⚠️ HELD BACK — the director's tension-curve ownership.** The charter said the director
   "owns the tension curve" (D11); every drafted section converged on **subtract-only
   rationing** (a ceiling, never a floor) because curve-*shaping* collides with the standing
   "no designed dramatic timing" NOT-list and C7. This REVERSES charter language and is
   therefore **not self-ratified by merging** — explicit sign-off requested (recommended
   default: subtract-only).
9. **Torben Loyalty range** — register 8→0 vs `clock_registry` 0–7 start-3; the capstone trace
   depends on start-8. Pre-existing corpus conflict routed here because the trace exposes it.

## 6 · The NOT-list (honest scope)

Inherited from doc-10 §8.5 and carried in full (s2 §Q3.7): no single-character heroic-arc
guarantees, no authored mystery/reveal arcs, no designed dramatic timing, no
failure-of-the-world model — plus: no three-act shape guarantees, and no arc labels ever
surfacing (C2). What the engine CAN produce: pressure-driven political/personal arcs with
setup (skeleton seeds), escalation and turn (lifecycle + convergence), diegetic resolution,
and retrospective coherence (chronicle + causes[] walk) — *experienced forwards as pressure
and choices, recognized backwards as story.*

## 7 · Adversarial & verification record

- **Refutation** (5 lenses, all SOUND-WITH-FIXES): determinism (4 MAJOR — all fixed into s4),
  veto/drift (the tension-curve fork §5.8 + convergence-effect whitelist honesty + C2 lint
  scope), content feasibility (2 BLOCKER — bake-volume vs Certainty-fork contradiction now
  carried in fork 6's ~5-6× swing; slot-divergence ≠ prose-distinctiveness now split into the
  three-defense treatment with ERA as the content gate), railroad (window-realness rule,
  no-silent-foreclosure via arc-edge routing, engaged-arc demotion protection), integration
  (Gate-0 phantom-dependency honesty; §8.5 co-edit; phantom 'chronicle' consumer fixed).
- **Capstone verification** (3 lenses, PASS-WITH-FIXES, fixes applied): contract coherence
  (Keys/modules/ownership consistent; R1–R10 canonical), trace accounting (12/12 capstones,
  §5/§12 type-check, zero unaccounted Keys), register round-trip (every ARC-S07 number
  faithful; COLLISION-C deltas corrected to register-verbatim; two-seed sketch consistent).
- **Completeness critic**: all gaps remediated in place (Q2 surfaces column, factionless
  mini-trace, thread-beat renders, effect-bearing COLLISION trace, ED-609/ED-1009/ui-§9.7/
  850KB-asset citations, NOT-list completion, offered-vs-taken honesty) — except where
  converted to §5 forks.

## 8 · Crosswalk

See `integration_with_ners_audit.md` for the finding-by-finding mapping to the ratified
2026-07-04 NERS audit (F-2, F-4, §4 wire-it ranking, J-3/J-4/J-7, S-1/S-2) and the inherited
prior-art questions (docs 10–13, the 2026-05-08 immersion audit), each answered or explicitly
deferred.
