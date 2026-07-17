<!-- STATUS: PROPOSED — adversarial audit findings; read-only; docket UNRULED (Jordan picks per finding). -->
<!-- AUTHORITY: ED-IN-0073 (umbrella). Per-lane ED candidates listed in §4 are NOT yet allocated — file on ruling. -->

# Character-Decision Machinery — Adversarial Audit (Findings)

## Status: PROPOSED — read-only, docket unruled
## Date: 2026-07-17
## Umbrella ledger entry: ED-IN-0073 (`registers/editorial_ledger_in.jsonl`)
## Companion files: `01_remediation_L1_L2.md` (fix design), `02_emergence_oracle_spec.md` (n≥100 oracle)

---

## §0 Scope & method

Adversarial investigation of the character-decision substrate — Conviction vectors, Ethical
Framework, Beliefs, the derived scalars, the social-contest armature, faction action selection, the
Key substrate, and the articulation layer — along three axes: **logic/internal consistency**,
**narrative emergence**, and **qualitative rendering of quantitative state**.

Method: three independent read-only investigators (Sonnet finders) each attacking one axis against
the working tree, one Opus synthesis, plus independent arithmetic re-derivation of the two
quantitative findings (L1, and the remediation matrix in `01_`). Every finding below is cited to a
working-tree `file:line` and carries a **failure scenario** and a **genuine-hole vs not-yet-built**
classification, per the repo's finding-ledger discipline.

**Framing caveat (applies to the whole audit).** The design corpus is rich and largely honest about
its own gaps; the *executable substrate* implements a fraction of it. Several capability claims that
read as present-tense in the design docs are, in the working tree today, either **false in code** or
**degenerate in the math**. This audit separates the two conditions explicitly — an unbuilt spec is a
legitimate state; a shipped mechanism that contradicts its own stated purpose is not.

Severity key: **CRITICAL** (breaks a load-bearing claim), **MAJOR**, **MODERATE**, **MINOR**.

---

## §1 Axis A — Logic & internal consistency

### L1 — CRITICAL — the "continuous 4×4 dot-product" armature is, for style selection, a single-axis lookup
**Genuine hole.** `sim/personal/contest/armature.py:228-235` builds every `STYLE_AXIS` row via
`_row()` as `1.0` on the style's one primary axis and a uniform `0.15` on the other three. The
alignment then reduces exactly to
```
alignment(style, judge) = 0.85·judge[primary(style)] + 0.15·S            (S = Σ judge axes)
```
The `0.15·S` term is **identical for every style against a fixed judge**, so it cancels in any
style-vs-style comparison; the gap between any two styles is purely `0.85·(judge[p1] − judge[p2])`.
The three off-axis cells contribute a constant offset and **zero discriminative power**. The module's
~250-line docstring is dedicated to distinguishing its "genuinely continuous" projection from the
"degenerate categorical single-axis" Resonant-Style match it claims to supersede (its own "judge
finding 5"); that distinction collapses. Verified by re-derivation: a balanced judge `[.5,.5,.5,.5]`
scores an identical `0.725` for all four styles.
**Failure scenario:** a designer authors two adjudicators intended to reward different rhetorical
styles by giving them different off-axis emphasis; the off-axis cells are ignored, so both behave
identically except on the single axis each style names. **Fix designed in `01_`.**

### L2 — CRITICAL — two incompatible vector spaces are both named `armature_position`, never bridged
**Genuine hole (architectural).** The Key substrate defines `armature_position` over
`{hierarchical, sacred, instrumental, traditional}` (`engine/substrate/keys.py:56`, enforced as
invariant 6, `keys.py:340-346`), derived from the 13-Conviction vector via `CONVICTION_AXIS_MATRIX`
(`conviction_axis_matrix_v30.md §5`). The contest adjudicator defines a **different** `ArmaturePosition`
over `{evidence, consequence, authority, insinuation}` (`armature.py:261-283`), hand-authored per demo
(`agon_harness.py:132`: `DEMO_JUDGE_POSITION = ArmaturePosition(consequence=0.75, evidence=0.35)`) and
**never derived from any NPC's convictions**. No code converts one to the other; a Key carrying the
contest vector as `symbolic_dimensions` would be rejected by invariant 6. Consequence: **an NPC's
Convictions have zero mechanical effect on how that NPC judges a social contest** — the judge vector
is authored independently or defaults to zero (`position_of()` fallback).
**Failure scenario:** the entire "Convictions drive social-contest outcomes" story is unbacked in
code; Himlensendt's Faith:0.9 does not make him harder to move with Consequence appeals, because
nothing maps Faith → a contest-axis susceptibility. **Fix designed in `01_`.**

### L3 — CRITICAL — two "canonical" docs assign different core Convictions to the same NPCs
**Genuine content contradiction.** `npc_behavior_v30.md §2.3` gives Baralta primary **Precedent** (the
trait ED-400 exists to establish, on which her whole Arc Map hangs); `conviction_migration_roster_v30.md
§2.3` gives her **Faith/Virtue/Warden — no Precedent at all**. Vossen: Equity ("power must flow from
the people") vs **Honor/Warden/Community — Equity absent**. Maret Uln: Equity/Reason vs
Honor/Authority/Identity — zero overlap. The roster's cast is also a stale set (Cesare, Lorenzo, a
"Niflhel envoy" for a **struck** faction, several explicit placeholders).
**Failure scenario:** any engine or reader resolving Baralta's Conviction gets a different answer —
and therefore different Resonant-Style vulnerabilities, Framework-Drift rows, and Ob modifiers —
depending only on which "canonical" doc it read.

### L4 — MAJOR — the primary NPC doc runs on a superseded taxonomy with no matrix rows
**Genuine hole (asserted-finished canon).** `npc_behavior_v30.md` (stamped `CANONICAL`) cites legacy
labels **Reason / Autonomy / Continuity** as the operative Conviction for most of its cast (44
occurrences: Vaynard primary "Reason", Edeyja secondary "Reason", Haelgrund primary "Continuity",
etc.), but `conviction_taxonomy_v30.md §1.2` declares those labels superseded, and there is **no
`CONVICTION_AXIS_MATRIX` row for "Reason"** (the matrix has "Scholastic"). The projection
`convictions → 4-axis armature` therefore cannot be computed for the majority of named NPCs, and the
migration roster meant to fix it (L3) doesn't cover Edeyja.

### L5 — MAJOR — the 4-axis Community/Identity collapse is real, quantified, and was deferred unmeasured
**Acknowledged debt, but the magnitude was never computed before deferring.** Community
`[0,+.3,−.2,+.5]` vs Identity `[+.4,+.2,0,+.6]`: Euclidean distance **0.469**, versus **2.156** for a
maximally-separated pair (Faith/Utility) — 4.6× smaller. The "village-belonging vs bloodline-belonging"
distinction the taxonomy's §2.1 calls load-bearing is mechanically near-flattened, differing almost
entirely on one axis. `conviction_axis_matrix_v30.md §4.1` acknowledges the collapse and defers a 5th
axis "unless required" — but the deferral rationale never states the 0.469-vs-2.156 gap; "load-bearing"
was asserted, not measured against a baseline.

### L6 — MODERATE — no convergence/stability argument for the Scar→Cascade→Drift→Action loop
**Spec gap.** The per-season cascade (`faction_behavior_v30.md §3.2.3`, a weighted-average walk up an
acyclic org tree) provably terminates — not circular. But the campaign-level feedback loop (events
Scar convictions → cascade → aggregate framework → Framework Drift + Ob → actions → new events) has
**no bound, no oscillation analysis, no fixed-point argument** anywhere. A leader oscillating across
the 3-Scar crisis-damping threshold (`§3.2.5`) could whipsaw the aggregate framework season to season;
nothing rules it out, and the repo's own degenerate-sim admission (CLAUDE.md §7) is the nearest
evidence, pointing the wrong way. The `02_` oracle is the constructive test for this.

### L7 — MINOR-MODERATE — the Conviction magnitude layer is uncalibrated and invisible to the anti-fabrication gate
**Disclosed but unmitigated.** `STYLE_AXIS` 1.0/0.15, `κ=0.03` drift, `ARMATURE_MAX_DSIGMA=0.50σ`, and
every cell of the 13×4 axis matrix are `[SEED]` or hand-assigned by historical analogy.
`references/values_master.yaml` contains **zero** occurrences of "Conviction" — the whole vector
apparatus is un-indexed by the tooling meant to catch fabricated constants.

---

## §2 Axis B — Narrative emergence

### N1 — CRITICAL — GD-2's mandatory pre-pass (the refutation's chief safeguard) is not implemented
**Genuine hole (asserted-in-comment).** `faction_action.py` claims the GD-2 "mandatory-before-stochastic"
threat-response pass in its docstring/comments (lines 4, 179), but `faction_take_action()` goes
straight to the stochastic draw; `mandatory_actions()` exists only in **retired** `mc_v14/v15`. The
mechanism cited to prove "the engine layers stochastic selection on deterministic threat-response" is
narrated, not built.

### N2 — CRITICAL — the NPC Arc state machine has zero code
**Not-yet-built, but presented as the emergence mechanism.** Almud Arc A–F, Himlensendt A–C, etc.
(`npc_behavior_v30.md §5`) are hand-specified branch tables with prose branch conditions; no arc-state
class or selection logic exists in `sim/` or `engine/`. Under "there is no GM — the engine resolves
everything," arc "emergence" is presently a Choose-Your-Own-Adventure lookup with nothing computing
the branch.

### N3 — CRITICAL — GD-3's insurgency pipeline (cited as defeating predictability) fires zero times
**Built-but-unreachable.** `test_f7_smoke_oracle.py:126` and `test_mc_v18_regression.py` assert
`insurgencies_formed == 0` and `npcs_generated == 0` across every seeded batch; the test comment calls
it a "built-but-unreachable island." The mechanism cited as proof the faction roster is "non-static"
has produced no new factions in any run on file.

### N4 — MAJOR — the "87% degenerate win-share" citation is stale, and its replacement is not evidence of health
**Correction to prior claims (including earlier in this session).** `test_f7_smoke_oracle.py:6`
documents the 87% as a "SMALL-N ARTIFACT" from one unguarded `run_batch(8, seed=42)`, revised to
`{Crown 37.5, Church 12.5, Hafenmark 12.5, Varfell 37.5}` — but the file itself says "Still small-n
(NOT balance signal)... Do not tune to it." The primary regression golden is **n=2**:
`{Crown 50, Church 0, Hafenmark 0, Varfell 50}`. True balance at meaningful scale (n≥100, the bar the
audit doc itself set) has **never been run**. The degenerate-attractor question is open, not closed.
The `02_` oracle spec is the constructive close.

### N5 — MAJOR — Hafenmark has a structural absorbing-state trapdoor **(already tracked — not re-filed)**
`test_f7_hafenmark_elimination_lockout`: 0 territories → can never act again; the only recovery path
(`parliamentary_transfer`) is never called. **This is already ledgered as `ED-FA-0005` ("elimination
lockout, no-permanent-lockout ruled").** Recorded here for completeness; **no new ED** (anti-duplication
discipline).

### N6 — MAJOR — the "~75–85% story-fraction" is a hypothetical laundered into canon
**Genuine hole (evidence laundering).** Traced to
`designs/audit/2026-04-30-architecture-session/11_story_vs_happenings_analysis.md`, self-labeled
"Analysis — not a proposal, not a spec," reasoning *"here's an honest distribution estimate"* by
analogy to Dwarf Fortress/CK, **contingent on three additions** (protagonist frame, arc detector,
punctuation events) that grep to zero hits in code. `articulation_layer_v30.md §10` (a `CANONICAL`
doc) restates it as fact with the hedges removed.

### N7 — MAJOR — the Stage-10 "12/14 PASS" behind the canonical promotions is unreproducible
`designs/audit/2026-04-30-architecture-session/sims/pp687_sim.py` (708 lines) imports only stdlib —
**not `sim.*` or `engine.*`** — is in no suite, not run by CI, unrelated to `mc_v18`. The battery
stamped on the taxonomy, axis-matrix, and articulation docs as the promotion basis cannot be
re-verified against the live engine, and 2/14 failures are unnamed.

### N8 — MODERATE — `arcs/simulated/` is hand-authored fiction, not engine telemetry
`arcs/simulated/arcs_01_04.md` carries author-process tells (prose probabilities, mermaid branch
diagrams) and is dated a month **before** `faction_action.py` existed — it cannot be output of an
engine that did not yet exist. The older name `gm_ref/` was more honest.

### N9 — MODERATE — the determinism refutation is weaker than its "REFUTED" tone; collision variety is thin
Of the five safeguards `refute_deterministic-priority-trees.md` cites, three (GD-2 pass N1, GD-3
pipeline N3, arc mutation N2) don't fire in the live substrate. Its *structural* argument (Ω
non-dominance is a property of player strategy space, not NPC stochasticity) is sound; its
*evidentiary* base is not. Separately, half the roster (Varfell, Hafenmark) has no unique action —
`_faction_specific_unique()` returns `_NOOP` — shrinking collision variety below what §5/§8 promise.

---

## §3 Axis C — Qualitative rendering of quantitative state

**Axis verdict: the "engine renders quantitative state as referenceable qualitative content" claim is
largely an unbuilt IOU today, and where code exists it contradicts the present-tense claim.** These
are mostly *not-yet-built* — a legitimate state — but they are flagged loudly because the claim was
narrated as operative.

### Q1 — CRITICAL (not-yet-built) — the Key→prose realizer does not exist
`engine/cross_scale/articulation.py`: all three entry points (`render_protagonist_lens`,
`evaluate_articulation_triggers`, `generate_chronicle_entry`) are one-line `raise NotImplementedError`.
The caption spec (`§3.4`) and chronicle templating (`§4.5`) say only "Phase 5a Godot"; no schema,
format, or worked example exists (`2026-07-05-emergent-narrative-engine/.../02_prose_render_stack.md`
confirms). Feed a live Key log today and it raises.

### Q2 — CRITICAL (genuine hole; claim currently FALSE) — Keys do not mutate character vectors
`engine/substrate/__init__.py` documents the observer/armature-apply steps (§4.1 steps 3-4) as
"Deliberately NOT implemented," blocked on fork ORD-3; `armature_position` has **zero occurrences in
`engine/`**. `impact_vector` is carried on the Key, validated, serialized — and **never applied to
anyone**. Any present-tense "Keys mutate the vector; the vector shapes which Keys fire" is false today.

### Q3 — CRITICAL (genuine hole) — the flagship qualitative Key types are never emitted
`state.scar_acquired`, `state.belief_revised`, `meta.knot_ruptured` — the types the entire
trigger/significance/K-B-I machinery is built around — return **zero matches** across `sim/` and
`engine/`. The consumer apparatus is complete on paper with no producer.

### Q4 — CRITICAL (genuine hole) — `Belief.statement` is read by nothing
Grepping `.statement` across `sim/` returns exactly one hit: inside `Belief.to_dict()`'s own
serializer. No dialogue or scene code reads it; `revise_belief()` only flips the enum and bumps a
counter. "A character references a belief directly" is unbuilt — a flag with authored decoration
nobody consumes.

### Q5 — MAJOR — the "qualitative" half is a labeling illusion at the substrate
`symbolic_dimensions` and `impact_vector` are *both* axis→float dicts; `interpretation(npc,key)` is a
scalar (`key_substrate_v30.md §4.1`). The only human-readable text in a Key is a few authored short
strings on specific payloads, supplied by whatever emits the Key (currently nothing). "Simultaneously
quantitative and qualitative" is true only in that a Key *could* carry a hand-typed string beside its
numbers; the qualitative content is not derived or generated.

### Q6 — MAJOR (not-yet-built, honestly flagged) — determinism + templates = the oatmeal problem, unsolved
`§8 A5` requires "same Key log → same output." The corpus names the risk ("Compton's 10,000 Bowls of
Oatmeal") and the RATIFIED follow-on says the anti-repetition property is "UNBUILT, a Stage-5 blocker."
Honest — but "will players see the same 44-type captions repeatedly" has no answer yet, because nothing
renders.

### Q7 — MINOR (doc hygiene) — `articulation_layer_v30.md` declares its status four contradictory ways
Header `CANONICAL`, body `PROVISIONAL` twice, footer "PROVISIONAL pending ratification." The same
self-contradiction appears in the taxonomy and axis-matrix docs.

---

## §4 Cross-cutting patterns

1. **"Small fixed set dressed as a continuous/general mechanism."** `STYLE_AXIS`'s uniform-0.15 rows
   (L1) and the 6-word belief-relevance vocabulary that misses most of the cast (Almud, Baralta,
   Ehrenwall, Vossen, the Guild Council all fail the keyword path, `npc_behavior_v30 §8.11.1`). Each
   presents a lookup as the richer thing it is named after.
2. **"Same name, two live definitions."** `armature_position` ×2 (L2), Conviction legacy-vs-new (L4),
   `CANONICAL`-vs-`PROVISIONAL` within single files (Q7). Exactly the drift CLAUDE.md §4 warns about,
   found concretely in the Conviction system.
3. **Evidence laundering under status promotion.** A hypothetical estimate (N6) and an unreproducible
   stdlib-only script (N7) sit behind `CANONICAL` stamps. The one place the pattern crosses from
   honest-gap into asserted-as-done.

---

## §5 ED docket (candidates — file per-lane ON RULING; not pre-allocated)

Following the `ED-IN-0029`/`ED-IN-0027` read-only-audit precedent, this audit is umbrella-filed as
**ED-IN-0073** and the per-lane items below are presented as a **ruling docket** rather than
pre-burning lane IDs (avoids cross-lane collision surface; keeps the PR IN-scoped). Allocate from
`references/id_reservations.yaml` `lane_ids` on Jordan's pick.

| Cand. | Lane | Finding | Proposed disposition |
|---|---|---|---|
| C-1 | SC | L1 armature degeneracy | Adopt the genre-overlap `STYLE_AXIS` in `01_ §2`; re-`[SEED]` magnitudes. |
| C-2 | SC (+IN cross-ref) | L2 dual `armature_position` | Adopt the `CONV_TO_RESONANCE` derivation in `01_ §3`; deprecate the hand-authored path. |
| C-3 | SC | L3 roster vs npc_behavior contradiction | Pick one canonical Conviction per NPC; reconcile roster ↔ `§2`. |
| C-4 | SC | L4 legacy 9-Conviction labels in CANONICAL doc | Migrate 44 legacy citations to the 13-taxonomy; add missing matrix coverage. |
| C-5 | SC | L5 4-axis collapse magnitude | Record the measured 0.469/2.156; rule on the Class-B 5th axis with data. |
| C-6 | FA (+IN) | L6 / N4 cascade + balance untested at scale | Adopt the `02_` oracle; treat N4 as OPEN until it runs. |
| C-7 | IN | N6 story-fraction laundering | Restore the hedges in `articulation_layer_v30 §10`; mark contingent. |
| C-8 | IN | N7 unreproducible Stage-10 promotion basis | Re-run the battery against the live engine or downgrade the promotion stamps. |
| C-9 | IN | Q7 four-way status contradiction | Single-source the `## Status:` line (obs_core regex owner). |
| — | FA | N5 Hafenmark lockout | **Already `ED-FA-0005`; do not re-file.** |
| — | IN/GO | Q1–Q3, Q6 rendering unbuilt | Already staged (Phase-5a / ORD-3 / narrative_engine_design_v2); tracked, not new. |

---

## §6 What survives (steelman)

- `faction_action.py` is real, executable, and performs a genuine state-conditioned stochastic draw.
- The Key **object model** (`keys.py`) is real, validated, causal-DAG-enforced, deterministic — the
  scaffolding for referenceable events exists, even though nothing populates or renders it.
- The **concept** — legible actors whose collisions generate drama; non-dominance held by hidden
  state rather than by randomizing choice; a no-runtime-LLM NLG plan of offline-baked factored
  templates — is coherent and defensible. It is the *evidence of achievement*, not the *architecture*,
  that collapses.
- The per-season cascade math provably terminates.
- The corpus is, in most places, honest about its own gaps.

The repairs in `01_` (L1/L2) and `02_` (the n≥100 oracle for L6/N1–N4) are the highest-leverage
closes: they make the conviction→contest path real, make the armature genuinely discriminate, and give
the emergence claim its first test at the scale that would reveal a degenerate attractor.
