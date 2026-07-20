<!-- Remediation program for the ED-IN-0073 character-decision adversarial audit. -->
<!-- Companion to 00_findings.md, 01_remediation_L1_L2.md, 02_emergence_oracle_spec.md. -->

# Character-Decision Substrate — agonist-antagonist remediation program

## Status: PROPOSED — Jordan-gated. Phase-0 docket UNRULED except D1 (ruled per-NPC, 2026-07-18).
## Date: 2026-07-18
## Scope: remediation orchestration for the ED-IN-0073 audit findings (L1-L7, N1-N9, Q1-Q7).
## Ref: ED-IN-0073 (this audit), ED-IN-0071 (P4 reorg / RATIFIED destination), ED-IN-0075 (Truth axis).

> **Provenance:** synthesized from 4 independent adversarial critics (A opus scale/decomposition,
> B edge-integrity, C precedent, + a 5th opus **adversarial pass on this plan itself**) and the
> `ED-IN-0073` audit. The plan-critic's findings are folded in below (verdict was NEEDS_REVISION;
> its CRITICAL sequencing fix and three dropped findings are now incorporated).

## Phase-0 ruling state (live)

| Fork | Question | State (2026-07-18) |
|---|---|---|
| **D1** | authoritative Conviction per contested NPC (roster vs npc_behavior) | **RULED — per-NPC.** Jordan adjudicates the per-NPC diff at Phase 2. |
| **D2** | add a Class-B 5th axis, or accept the Community/Identity collapse? | **EXPLAINED, awaiting ruling.** Recommendation: record 0.469/2.156 now; defer axis ruling to post-Phase-4 oracle. |
| **D3** | execute the ED-644 territorial `conviction_track_v30`->`piety_track` rename now, or hold? | **EXPLAINED, awaiting ruling.** Recommendation: EXECUTE (file already corrupted by a half-applied sweep — deferral is no longer free). |
| **D4** | ratify the C-1..C-9 audit dispositions? | **EXPLAINED, awaiting ruling.** Recommendation: ratify all 9 as stated (only C-7/C-9 ship in Slice A; rest stay phase-gated). |
| ~~D-folder-name~~ | folder name | **CLOSED** — `conviction/` per reorg §5.4 + ED-IN-0075. |

---

## Context — why this exists

The final P4 relocation (the "character slice") was scoped; an adversarial review surfaced far more
than a folder boundary. The **character-decision substrate** (Conviction vectors, the contest
armature, Beliefs, NPC arc/action machinery, the Key->prose rendering layer) carries **content
contradictions, mechanism degeneracies, and unbuilt-but-asserted-done claims**, catalogued in the
`ED-IN-0073` audit (`designs/audit/2026-07-17-character-decision-adversarial-audit/`, docket
**UNRULED**). Relocating the docs *on top of* these would ratify live contradictions into a
subsystem by location.

**Frame-fixing facts:**
- **The destination is RULED.** `proposals/repo-reorganization-v1.md` §2a/§5.4 (RATIFIED,
  ED-IN-0071, PR #150) puts `generation/ conviction/ beliefs/ companion/` under nested
  `systems/character/`; §5.4 explicitly names the folder **`conviction`** and assigns this slice
  **two renames** (personal->`conviction`, territorial->`piety_track`). So the destination *and*
  the folder name are settled, not open.
- **Critic disagreement, resolved.** Critic A said DEFER/route to `_architecture`; Critic C found
  the ratified plan-of-record A never checked. Synthesis: **C wins "should it happen"; A's
  substance (cross-scale substrate, the L3 contradiction) becomes the R-CONTENT/R-MECH work.** The
  lane-gap is real but non-fatal — `npcs/ articulation/ ui/ _architecture/` already run lane-less
  and file editorial work under **IN**; `character/` joins that cohort.
- **The plan-adversarial-pass caught a §2 trap** (below): relocating the L3-contradicting roster
  *before* reconciling it would **ratify-by-default** a CRITICAL contradiction into canon. Fixed by
  pulling the roster out of the relocation.

Intended outcome: a producer->independent-antagonist relay (CLAUDE.md §10) that lands the ratified
relocation cleanly **without ratifying any contested content**, executes the two RULED renames, and
closes / *loudly holds back* every audited failing — split into **what ships now** vs **a tracked,
Jordan-gated program**.

---

## ▶ START HERE — the two-tier split

**Slice A (ship now, PR-sized, mechanical):**
1. **Phase-0 docket to Jordan** (the design gate — see below). Nothing content-touching merges
   until D1 is ruled. *(D1 ruled per-NPC 2026-07-18; D2/D3/D4 recommendations pending confirm.)*
2. **Phase 1 — relocation** (`systems/character/`, roster EXCLUDED, PATH-ONLY, gated on D1).
3. **Phase 5a — doc-hygiene** (restore N6 hedges, single-source Q7 status) — runs *in a parallel
   worktree* to Phase 1 (different files -> genuine collision-avoidance, unlike the sequential rest).

**Program B (tracked, multi-session, Jordan-gated — NOT one PR):**
- **Phase 2** R-CONTENT (L3 reconcile-and-relocate the roster, L4 label migration).
- **Phase 3** R-MECH (L1/L2 armature *structure* repair; magnitudes stay `[SEED]`).
- **Phase 4** R-EMERGE (the n>=100 oracle — a **harness build + compute run**, not one bullet;
  CLAUDE.md §7: no CI runs full `mc_v18`). Its baseline runs **before** Phase 3.
- **Phase 5b** R-RENDER (first Key emitter; keep the unbuilt realizer honestly flagged).

---

## Phase 0 — Jordan decision gate (BLOCKS Slice-A merge + all of Program B)

Present as a compact ruling docket (AskUserQuestion + PR body). Each fork leads with the *cost*,
not the do-nothing default, so the framing does not pre-empt.

- **D1 (L3 — CRITICAL):** authoritative Conviction per contested NPC (Baralta, Vossen, Maret Uln...)
  — `conviction_migration_roster_v30` vs `npc_behavior_v30`. **Coupling to disclose:** choosing
  `npc_behavior` as authoritative *inherits its L4 problem* (it still runs on the superseded 9-label
  taxonomy with no matrix rows), whereas the roster already uses the 13-taxonomy. So D1 and L4 are
  one decision, not two. **RULED per-NPC (2026-07-18):** the per-NPC diff is brought to Jordan at
  Phase 2 for case-by-case adjudication.
- **D2 (L5 — MAJOR):** add a Class-B 5th axis to separate Community/Identity, or accept the
  collapse? **Lead with the measured cost:** Euclid 0.469 vs 2.156 max (4.6x smaller) — the two are
  mechanically near-indistinguishable today; the taxonomy's own §4.1 deferral never stated this
  number. **Recommendation:** record the measurement in canon now; defer the add/accept ruling until
  the Phase-4 oracle reports whether the collapse matters in play.
- **D3 (ED-644 — RULED-but-repeatedly-deferred):** execute the *territorial*
  `designs/scene/conviction_track_v30.md`->`piety_track` rename (cross-lane, -> `systems/settlements/`)
  **in this program**, or hold with a stated reason? Reorg §5.4 assigns it here and prior slices
  deferred it "to land with the character slice"; the plan must not use "loud not silent" to defer
  again silently. **Recommendation: EXECUTE** — a half-applied token-sweep has already corrupted the
  territorial doc (its stat noun reads "Conviction (PT)" and its ED-644 note now reads the
  self-referential "PT ≡ PT / PT -> PT"), so holding no longer means "leave unchanged," it means
  "leave broken."
- **D4 (docket):** ratify the C-1..C-9 audit dispositions (adopt `01_`/`02_` designs, restore
  hedges, downgrade unbacked promotion stamps). **Recommendation: ratify all 9 as stated** — only
  C-7/C-9 ship in Slice A; C-3/C-4 point back to D1, C-5 to D2, C-6 to the oracle; each stays
  phase-gated.
- **~~D-folder-name~~ — CLOSED, confirm only:** folder = `conviction/` per reorg §5.4 + ED-IN-0075
  (which retired the character "Piety Track" name today). One-line confirm; flag only if Jordan
  prefers `piousness`.

---

## Consolidated failing register (all findings; nothing dropped)

**R-STRUCT (relocation):** nested `systems/character/{generation,conviction,beliefs}/`; the traps
and exhaustive edges are in Phase 1 below.

**R-CONTENT:** **L3** roster<->npc_behavior conviction contradiction (needs D1). **L4** 44 legacy
Reason/Autonomy/Continuity labels in CANONICAL `npc_behavior_v30`, no `CONVICTION_AXIS_MATRIX`
"Reason" row -> projection uncomputable for most NPCs. **Q7** four-way `## Status:` contradiction
(articulation/taxonomy/axis-matrix).

**R-MECH:** **L1** armature `STYLE_AXIS` uniform-0.15 -> single-axis lookup (balanced judge ties all
styles at 0.725). **L2** two unbridged `armature_position` spaces -> **Convictions have zero contest
effect**. **L5** Community/Identity collapse (0.469 vs 2.156). **L6** no convergence/stability
argument for the Scar->Cascade->Drift->Action loop. **L7** whole magnitude layer is `[SEED]`,
invisible to the anti-fabrication gate (`values_master.yaml` has 0 "Conviction").

**R-EMERGE:** **N1** GD-2 mandatory pass asserted-in-comment, unbuilt. **N2** NPC arc state machine
= zero code. **N3** GD-3 insurgency fires zero times. **N4** balance untested at n>=100 (golden is
n=2). **N6** "75-85% story-fraction" hypothetical laundered into CANONICAL. **N7** Stage-10 "12/14
PASS" promotion basis (`pp687_sim.py`) unreproducible. **N8** `arcs/simulated/` is hand-authored
fiction dated before `faction_action.py` existed. **N9** determinism refutation weaker than its tone
+ `_faction_specific_unique()` returns `_NOOP` for half the roster. **N5 = already ED-FA-0005, do
NOT re-file.**

**R-RENDER (mostly not-yet-built — keep honestly flagged, do not present-tense):** **Q1** realizer
`NotImplementedError`. **Q2** Keys don't mutate vectors (blocked on ORD-3). **Q3** flagship Key
types never emitted. **Q4** `Belief.statement` read by nothing. **Q5** the "qualitative half" is a
labeling illusion (`symbolic_dimensions`/`impact_vector` both axis->float). **Q6** determinism +
templates = unsolved oatmeal problem.

---

## Slice A

### Phase 1 — R-STRUCT relocation (producer -> **round-trip** antagonist)
**PATH-ONLY. Ratifies NO content.** PR body carries a hard banner: *"Path relocation only; ratifies
no PROPOSED content; `conviction_track_v1.md` §1 remains SUPERSEDED (PP-717); L3 roster contradiction
NOT touched here — reconciled in Phase 2."* **Merge gated on D1 ruled.**

- **Producer** (sonnet, worktree): create `systems/character/{generation,conviction,beliefs}/`;
  `git mv` the move-set; rewrite the 6 lazy inbound edges to `systems.character.sim.*`; repoint
  machine-read referrers; add aliases; fix the H1 title; preserve the supersession banner + add a
  CURRENT.md pointer to `conviction_taxonomy_v30`; update CURRENT.md/CLAUDE.md §3/HANDOFF_IN;
  allocate `ED-IN-NNNN` (character/npcs are lane-less -> **IN**, not SC).
- **Move-set (corrected):** 5 docs move now — `conviction_taxonomy_v30`, `conviction_axis_matrix_v30`,
  `character_generation_questionnaire_v30`, `conviction_track_v1` (+`_pp718_vetting`). **EXCLUDE
  `conviction_migration_roster_v30`** (the L3-contradicting doc) — it moves in Phase 2 with its
  reconciliation, so `designs/personal/` does NOT empty 100% yet -> the roster gets a **per-file
  alias** (same machinery already used for `tribunal`). **Defer `companion.py`** (stale canon,
  stub, zero coupling). Sim: `conviction.py`+`beliefs.py` -> `systems/character/sim/`; `tribunal.py`
  stays -> **per-file aliases, never a `sim/personal/` directory alias.**
- **Edge/trap discipline [B]:** the 6 inbound edges are all lazy (`beliefs:176,227`;
  `game_state:344,348`; `knots:348`; `contest_legacy_stub:240`); **do NOT touch**
  `excommunication.py:22 from sim.personal import tribunal`. Repoint the
  `canonical_sha__designs__personal__X_md` KEY NAMES (not just `design_doc:` values) or the freshness
  gate breaks. Repoint `mechanics_index`(4), `descriptor_registry`(5), `module_contracts` piety_track
  `doc:`, `glossary.md:84`. **grep exact `conviction_track_v1`, never substring `conviction_track`**
  (hits the STAYING territorial `conviction_track_v30`). Retain `CERTAINTY_SCALING` (no keyword
  caller). Cosmetic docstring sweep (`sim/personal/__init__.py`, fieldwork/`__init__`, ci_track:6,
  companion).
- **Collision docket [B, HIGH]:** this PR **executes the RULED personal->`conviction` rename** and
  (per D3) either executes or loudly-holds ED-644's territorial->`piety_track`; it **defers only the
  genuinely-open SC arm** — `ED-SC-0003` (SC debate-tracker also homes at this doc via
  `glossary.md:84`) + `ED-IN-0048` (must be resolved coordinated with ED-SC-0003). Flag those two
  for a coordinated SC+IN follow-up ruling at the new location; do not attempt to resolve them.
- **Antagonist** (sonnet, read-only, cold diff): slice-9/10 template PLUS a **real
  `restore_world()` round-trip test** — deserialize a snapshot carrying `convictions`/`beliefs`/
  `knots` keys and assert it reconstructs, because `game_state.py:344/348` is uncalled + untested and
  **import-smoke alone cannot catch a wrong-but-importable rewrite of that path.** Verify: no
  dangling `sim.personal.{conviction,beliefs}` refs; the SHA key-names repointed; the exact-filename
  grep left `conviction_track_v30` untouched; the PATH-ONLY banner + collision flags present; all
  gates + full suite. Changeset-aware gates (co-file, register-size, sim-fabrication) re-run **after
  commit** (this session's repeated lesson — they read committed `origin/main..HEAD`).

### Phase 5a — doc-hygiene (parallel worktree to Phase 1)
Restore the removed hedges in `articulation_layer_v30 §10` (N6); single-source the four-way `##
Status:` lines (Q7) via the obs_core regex owner. Different files from Phase 1 -> genuine parallel
lane. Antagonist (sonnet): confirm no CANONICAL claim now over- or under-states.

---

## Program B (tracked; each is its own PR, most Jordan-gated)

### Phase 2 — R-CONTENT (producer -> **opus** antagonist)
On D1: rebuild `conviction_migration_roster_v30` from the authoritative source; migrate
`npc_behavior_v30`'s 44 legacy labels to the 13-taxonomy; add the missing `CONVICTION_AXIS_MATRIX`
rows (the "Reason"->"Scholastic" gap). **This PR also relocates the roster** into `systems/character/`
(reconcile-and-move together, so a contradicting roster never enters canon). Antagonist is **opus**
(§10 — the verify node that gates a CRITICAL result): re-grep both docs for ANY residual per-NPC
disagreement; confirm every named NPC has a computable 13-taxonomy->4-axis projection; refute "no
contradiction remains."

### Phase 4 — R-EMERGE oracle (run FIRST as instrument; producer -> skeptic panel)
Build the `02_emergence_oracle_spec.md` harness (`harness/metrics.py/runner`, per 02_:92) — a
deterministic seeded **n>=100** `mc_v18` run reporting win-share, insurgency counts, arc-branch
firing, framework-drift oscillation. **Run a baseline BEFORE Phase 3** (so the L1/L2 fix's effect is
measurable) and again after. It is a **measurement instrument**, not a fix for the unbuilt GD-2/arc/
GD-3 mechanisms (N1/N2/N3 remain honestly deferred). Antagonist = **perspective-diverse skeptic
panel** (opus): one verifier per failure mode (degenerate attractor? seed-dependence? oracle
measuring inert mechanisms?). Report **N4 OPEN until it runs at scale** — never "closed."

### Phase 3 — R-MECH armature (opus producer -> opus arithmetic antagonist)
Implement the genre-overlap `STYLE_AXIS` (L1) + `CONV_TO_RESONANCE` 13x4 derivation (L2) from `01_`;
wire the conviction->contest bridge; deprecate the hand-authored `DEMO_JUDGE_POSITION`. **Scope
caveat:** this repairs *structure* only — `01_:168` says magnitudes stay `[SEED]` until calibrated
under Phase 4's harness. **Phase 3 does NOT close L1/L2; magnitude-canonicalization + L7 indexing is
a Phase-4-gated follow-on.** Antagonist (opus): **independently re-derive** — confirm the new
`STYLE_AXIS` is rank>1 (styles don't tie on a balanced judge) and the conviction->contest map
measurably matters (Faith:0.9 now harder on Consequence appeals); refute any re-introduced hidden
single-axis collapse. (Matches the audit's own arithmetic-re-derivation method.)

### Phase 5b — R-RENDER + evidence hygiene (producer -> completeness critic)
Re-run the Stage-10 battery against the live engine OR downgrade the CANONICAL promotion stamps
(N7); build the first *emitter* of `state.scar_acquired` so Q3's consumer apparatus has a producer;
keep Q1/Q2/Q4/Q5/Q6 flagged as staged (ORD-3/Phase-5a), never present-tense. **Tracked, not
addressed here:** N8 (`arcs/simulated/` provenance — rename/relabel as authored, not telemetry), N9
(`_NOOP` unique actions + the refutation's evidentiary weakness). Antagonist = **completeness
critic** (opus): "what CANONICAL claim still lacks a producer? what promotion stamp is still
unbacked?" — its findings seed the next round.

---

## Model tiering (per §10)
Sonnet: Phase-1 producer+antagonist, Phase-5a, Phase-2 producer, Phase-5b producer. **Opus:** the
Phase-0 adjudication synthesis, **Phase-2 antagonist** (CRITICAL gate), Phase-3 producer+antagonist
(load-bearing math), Phase-4 skeptic panel, Phase-5b completeness critic. Worktree isolation ONLY
where lanes are genuinely concurrent (Phase-1 ∥ Phase-5a) — dropped from the sequential Program-B
path.

## Verification
- Per-phase: the named adversarial antagonist + full gate battery (naming, co-file, currency,
  broken-dep, ED-citation, register-size, freshness, patch-propagation) run **after commit**, +
  `tests/valoria + tests/contracts + sim/tests`. Phase 1 additionally: the `restore_world()`
  round-trip.
- Program success = the audit's own bar: `01_` makes conviction->contest real + the armature
  discriminate (Phase-3 antagonist confirms by re-derivation); the `02_` oracle runs at n>=100 with a
  non-degenerate win-share (Phase-4 panel confirms); no CANONICAL doc carries an unbacked promotion
  stamp (Phase-5b confirms); no per-NPC Conviction disagreement remains (Phase-2 opus antagonist
  confirms).

## What the adversarial pass on this plan changed (audit trail)
1. **Pulled the L3-contradicting roster out of Phase 1** -> Phase 2 (kills the §2 ratify-by-default
   trap on a CRITICAL finding; Phase 1 is now genuinely content-free). **[top fix]**
2. **Two-tier split** (Slice A now / Program B tracked) + explicit START; Phase 4 sized as a
   harness-build and **decoupled/baseline-first**; Phase 3 flagged as structure-only (magnitudes
   `[SEED]`-blocked on Phase 4).
3. **Phase-0 corrected:** D4 folder-name demoted to confirmation (already RULED); D1<->L4 coupling
   disclosed; D2 leads with the measured cost; **ED-644 hoisted into the gate** as explicit
   execute/hold (was a deferral escape-hatch).
4. **Added dropped findings N8, N9, Q5** (Q5 is a MAJOR) to the register with dispositions.
5. **Split the collision docket:** execute the two RULED renames; defer only the genuinely-open
   `ED-SC-0003`+`ED-IN-0048` SC arm.
6. **Un-toothed the Phase-1 antagonist** (real `restore_world()` round-trip, not import-smoke);
   **raised the Phase-2 antagonist to opus**; removed ceremonial worktree isolation from the
   sequential path.
