# Handoff — IN (Infrastructure / Cross-Cutting)

Lane-scoped continuity for the `IN` (infrastructure/cross-cutting) lane, per the
`ED-<LANE>-NNNN` namespace (`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention.
Root `HANDOFF.md` is the index; see it for the global "Next actions" pointer and cross-lane
items. `IN` is also the catch-all for genuinely cross-cutting repo-governance work (ID systems,
CI gates, canon-currency reconciliation) that doesn't belong to any one subsystem lane.

## Pending

- **Resolution Plan v1 — Stratum-A truth-reconciliation FIRST PASS EXECUTED 2026-07-07 (this branch,
  `claude/fable5-audit-resolution-plan-r6kzsa`).** Executes the doc/registry/ledger core of Stratum A;
  `designs/audit/2026-07-07-unaddressed-areas-audit/resolution_plan_v1.md` §7 has the full
  finding→fix execution log. EDs flipped `resolved`: ED-FI-0003 (OPT-6 knots ED-912 propagation),
  ED-IN-0022 (OPT-7 registry hygiene), ED-IN-0023 (OPT-8 consumer closure), ED-IN-0024 (OPT-14
  addenda), ED-IN-0025 (OPT-17 C-VERIFY notes), ED-SE-0004 (OPT-16 anti-orphaning), ED-PC-0004
  (OPT-15 ED-1042 flips + the **ED-PC-0005** residual re-file). Kept `open` with a progress note:
  ED-FA-0004 (OPT-1 — `[PRE-LPS-1/PORT-BLOCKING]` banners placed, LPS-1 sim impl = Stratum B),
  ED-WR-0005 (OPT-5 — ED-871 doc side done, sim + C-TW-3.. = Stratum B). Also executed the U-6
  CI-75→CI-100 supersession + fork-2 ARC-T04 strike (doc side), and DISAMBIGUATED the half-done
  ED-IN-0012/0013→0019/0020 renumber (U-11 — the ratification appended the new rows but never re-id'd
  the old edge-playability rows; now `status: superseded` + `renumbered_to`, physical row-dedup left
  to Jordan). **Deferred (loud):** all behavior-changing sim edits (`operations.py`, `ci_track.py`,
  `knots.py`, dead `pool_penalty`) = Stratum B; genuine needs-Jordan calls (anchoring cadence cap,
  CI75-1 seizure trigger, CI75-11 GD-1 checklist, knots §6.2 Coherence-loss) flagged in place, not
  decided. New id: **ED-PC-0005** (id_reservations PC next_free 5→6).
- **Unaddressed-areas comprehensive audit — DELIVERED 2026-07-07 (ED-IN-0017, this PR;
  deliverable 1 of 2).** 14 evidence clusters (incl. Jordan-directed pessimist NERS + pessimist
  resolver reviews) + 4 gap-closure agents + 5 independent refuters; every cluster's Honest-gaps
  section dispositioned per Jordan's directive. Deliverables at
  `designs/audit/2026-07-07-unaddressed-areas-audit/` — verdict-first report, finding_status,
  `ed_options.md` (17 candidates, **deliberately UNFILED — Jordan picks**; OPT-1/2/4/10/14 and
  the armature §5 docket are needs_jordan), and **`resolution_plan_v1.md`** — the comprehensive
  bottom-up + top-down resolution program (armature-FIRST sequencing override per Jordan;
  contract deployment + enforcement ladder; v40 re-authoring license operationalized; ecosystem
  tooling bindings; full finding→fix→lane→stratum→gate table). Headlines: the faction oracle implements the
  pre-LPS-1 superseded model; threadwork is a total island; live contests resolve through the
  deprecated raw-dice stub; the ~87% win-share is a small-n artifact riding an elimination
  lockout (n=100: 56/36/7/1); the Turmoil victory gate is permanently vacuous; ED-871/fork-2/
  ED-912/fork-11 rulings only partially executed; conviction_track_v30 still runs the superseded
  CI-75 model (unpropagated supersession, refuter-upgraded).
- **Key & Echo Armature v1 — DELIVERED 2026-07-07 (ED-IN-0018, this PR; deliverable 2 of 2,
  needs_jordan = its §5 fork docket).** `designs/architecture/key_echo_armature_v1.md` (seam
  contracts + Echo Matrix all-directions/all-scales + §3 registry deltas + A13-A16 conformance
  specs + the consolidated §5 docket — **merge does NOT ratify §5**) + the first executable Key
  substrate (`sim/substrate/keys.py`, 24 tests) + `tests/contracts` wired into CI. Staging:
  PR-2 = flag-gated echo wiring + the F7 smoke oracle; PR-3+ = per-lane shaping waves (armature
  §6.3). The §5 docket consolidates: OF-D6/OF-3/OF-7/OF-B1/RNG-COLLISION/ORD-3/ORD-4/OF-CAP,
  ED-SC-0002, ED-SE-0002, the ED-IN-0012/0013 double-allocation renumber (ledger lines 597-600),
  CI 75-vs-80, ER-2 band-discipline scope, contest live-dispatch.

- **Unaddressed-areas audit + Key & Echo Armature — RATIFIED 2026-07-07 (Jordan: "Perform
  consolidated ruling pass? I want to ratify all and get to work on this" — ED-IN-0026, same
  branch/PR, before merge).** Rules the armature's full §5 fork docket (16 rows — see
  `key_echo_armature_v1.md` §5 Ruling Log) and files all 17 `ed_options.md` candidates as EDs
  (`ED-FA-0004/0005`, `ED-IN-0019/0020/0021/0022/0023/0024/0025`, `ED-WR-0004/0005/0006`,
  `ED-FI-0003`, `ED-SE-0003/0004`, `ED-PC-0003/0004`, `ED-SC-0011`, `ED-MB-0004`; see
  `ed_options.md`'s Disposition table for the design-call ruling baked into each). Headlines:
  OF-7/OF-B1 ADOPTED — `sim/substrate/keys.py`'s `TickScheduler` now defaults both flags ON
  (propagation_spec_v1.md and key_substrate_v30.md amended to record the ratification; 25/25
  substrate tests + full 120-pass `tests/valoria` suite re-verified, no regressions); the
  ED-IN-0012/0013 double-allocation (§5.10) EXECUTED via the `ED-IN-0019`/`ED-IN-0020` renumber;
  the ER-2/Overwhelming band-discipline fork (§5.12, the one genuine no-default fork besides the
  renumber) ruled toward the symmetric-unification direction, execution deferred to `ED-PC-0003`;
  the A15 process extension (§5.16) landed in `key_type_registry_v30.md` §10, which also picked
  up a header CANONICAL/PROVISIONAL split correction found while editing the same file.
  `ED-SC-0002`/`ED-SE-0002` (§5.8/5.9) deliberately left unruled — pre-existing SC/SE-lane forks,
  out of this IN-lane pass's scope per CLAUDE.md §4's session-lane-scoping convention. Citation
  integrity + currency checks re-verified clean (`validate_ed_citations.py` 0 violations,
  `currency_consistency_check.py` clean, adjudicator baseline unchanged at 21/65).
- **Edge-playability audit — RATIFIED IN FULL 2026-07-05 (Jordan: "Ratify all", post-merge
  instruction on PR #81; merged as #81, ratification batch on the restarted branch).** Seam-level
  complement to PR #77: ~60 edges, 8 sonnet clusters, Fable-verified V1–V22. Deliverables at
  `designs/audit/2026-07-05-edge-playability-audit/` (all statuses now RATIFIED): report
  (verdict "the seams are the old GM's chair, still empty"; EP-1..EP-11 P1s, ep-12..ep-31 P2/P3
  register, SIG-1..4), grounding, dossiers + verification log. **All 10 §7 remediation items
  FILED 2026-07-05:** `ED-IN-0012` registry×rendering sweep · `ED-IN-0013` GM-token sweep of the
  handoffs (**renumbered 2026-07-07 to `ED-IN-0019`/`ED-IN-0020` respectively — armature §5.10,
  see the ratification entry below; `ED-IN-0012`/`ED-IN-0013` now mean the SC-audit batch content
  only**) · `ED-IN-0014` key the silent emitters (settlement/ci_political/era) · `ED-IN-0015`
  seam-feedback authoring convention · `ED-IN-0016` index the joints (CURRENT.md rows +
  faction_politics doc:null flip) · `ED-SE-0002` Accord/Order stacking ruling (**needs_jordan**:
  the ruling itself) · `ED-FA-0002` strategic-turn surface / domain_actions home doc ·
  `ED-FA-0003` BG victory-params re-export · `ED-FI-0002` counter-espionage loop · `ED-WR-0003`
  ambient-fabric window + Appraise Revelation (ED map also in the report §7 addendum;
  id_reservations bumped; SE/FA/FI/WR handoffs cross-referenced). P2/P3 register items without a
  §7 ED are ratified-as-findings, drawable for future allocations against the report. The five
  IN items execute in this lane; workplan-v6 sequencing applies.

- **Qualitative NERS audit (North-Star) — DELIVERED 2026-07-04, awaiting Jordan review (PR #77,
  branch `claude/ners-audit-fable5-9cpfdz`).** Corpus-wide qualitative audit (playability /
  cohesiveness / interdependencies / emergent narrative / threadwork-at-every-juncture), 55-agent
  adversarial workflow (12 dossiers + 5 degenerate-play hunters + 7 lenses; every carried finding
  refuted-or-confirmed with an intent gate). Deliverables at
  `designs/audit/2026-07-04-ners-qualitative-audit/`: `ners_qualitative_audit_v1.md`
  (verdict-first, throughlines-tree organized; 5 confirmed findings F-1..F-5 + 2 corpus signals
  S-1 register back-propagation blindness / S-2 steering-surface fragmentation),
  `strategic_judgments.md` (J-1..J-15: playable-season milestone, Gate-0-before-more-combat-depth,
  transport-seam closure, collision-engine detector, anti-drift + roadmap governance),
  `ed_options.md` (E-1..E-12 drafted candidates, **deliberately NOT filed** — Jordan picks and
  allocates per id_reservations protocol; merging PR #77 ratifies nothing). Follow-ups if adopted:
  E-2/E-3/E-7 are the recommended first three; GAP-1 = investigation lane never audited (E-12);
  32 deferred-unverified P2 candidates in `01_workings/deferred_unverified.json`.
- **Qualitative NERS audit (North-Star) — RATIFIED-AS-ACCEPTED 2026-07-05 (Jordan post-merge
  instruction on PR #77).** Corpus-wide qualitative audit (playability / cohesiveness /
  interdependencies / emergent narrative / threadwork-at-every-juncture), 55-agent adversarial
  workflow. Deliverables at `designs/audit/2026-07-04-ners-qualitative-audit/` (all statuses now
  RATIFIED): audit v1 (5 confirmed findings F-1..F-5 + corpus signals S-1/S-2),
  `strategic_judgments.md` (J-1..J-15), `ed_options.md`. **All 12 ED options FILED 2026-07-05**
  (forks resolved to audit defaults — E-1 adopt governance redesign; E-4 per-subsystem
  walkthrough policy; E-8 MS wins MS/RS): `ED-SE-0001`, `ED-IN-0003..0008`, `ED-WR-0001/0002`,
  `ED-PC-0001`, `ED-SC-0001`, `ED-FI-0001` (map in ed_options.md addendum; id_reservations
  bumped). ED-IN-0003 (convergence detector) + ED-IN-0004 (articulation triggers) are acceptance
  criteria of the **2026-07-05 emergent-narrative-engine design effort (IN FLIGHT, this branch)**
  — see `designs/audit/2026-07-05-emergent-narrative-engine/` once landed. Remaining filed items
  execute in their own lanes.

- **Emergent Narrative Engine design v1 — DELIVERED 2026-07-05, awaiting Jordan review (PR #78).**
  25-agent design workflow (4 dossiers → 3 architects → 3 judges + synthesis → 5 refuters → 5
  spec sections → 3 capstone verifiers → critic) + full remediation. Result: **the Arc-Vector
  Engine with a Subordinate Director** (B won all judge lenses; six layers,
  detect-then-schedule-then-render), closing ED-IN-0003 (L2 convergence detector) + ED-IN-0004
  (L5 render completion incl. the four ED-681 thread beats, worked) by construction. Deliverables
  at `designs/audit/2026-07-05-emergent-narrative-engine/`: `narrative_engine_design_v1.md`
  (head doc: architecture, staging, determinism, 9 open forks), `integration_with_ners_audit.md`
  (crosswalk), `00_grounding/` (charter with Jordan's four key considerations + C1–C7),
  `01_workings/spec_sections/s1..s5` (normative chapters incl. the ARC-S07 capstone trace,
  factionless mini-trace, effect-bearing COLLISION-B trace). **9 [OPEN — Jordan] forks — esp.
  fork 8 HELD BACK (director tension-curve subtract-only reverses charter language; not
  self-ratified by merge)**; forks 1–2 (Coup-Counter remap; ARC-T04 strike-or-author) block
  Stage 1. Corpus defects surfaced for follow-up: Coup Counter STRUCK but live in 6 register
  entries; ARC-T04 dangling; Torben Loyalty range register-vs-clock_registry conflict.

- **Narrative engine v2 "THE CHURN ENGINE" + Master Workplan v6 + steering reconciliation —
  RATIFIED IN FULL 2026-07-05 (Jordan: "Ratify commit merge all"; ED-IN-0009/ED-IN-0011;
  PR #78 merged). All stated fork defaults adopted incl. F-F/fork-8; fork 10's faction
  count = ED-FA-0001 (open, needs_jordan). Originally delivered as:** v2
  (`narrative_engine_design_v2_churn.md` + `spec/churn_amendments.md`, supersedes-in-part v1)
  reorganizes the engine around Jordan's churn critique: generator-not-corpus (templates ×
  binding, 138 register arcs = validation set), two-layer forecast (Layer A analytic — the M1
  ship, hard gate; Layer B seeded ensemble behind named preconditions incl. F7/F8), **the
  Light Function** (pruning-as-authorship; invariants i–iv; forecast severed from casting and
  actor-invisible per the adversarial pass), claim-grammar interface (a requirements input
  ADDING four SC sub-systems — shapes the SC lane's), load factorization (no runtime LLM;
  bake headline ~1,200–2,700 units under fork-6 default), kernel/data/wrapper modularity
  (nothing hard-baked; R-F1/R-F2/R-HB/R-CL/R-AI/R-RL). Five-refuter pass
  (`01_workings/refute_v2_*.md`) fully applied; survivors = forks 10–11 + fixture F8. **⚠️
  F-F/fork-8 (the Light-Function weight set + subtract-only discipline) is HELD BACK from
  merge-ratification — needs explicit Jordan sign-off.** Grounded by two dossiers
  (`01_workings/dossier_forecast_tractability.md`, `dossier_combinatorial_census.md`).
  **Workplan v6** (`designs/workplans/valoria_master_workplan_v6.md`, ED-IN-0009): M1/M2/M3
  milestones, IN spine, per-lane sequencing, tiered T0/T1/T2 decision register (no status
  fields), governance incl. the ED-PC plan-text-label rule. **ED-IN-0006 EXECUTED**:
  roadmap_state → `deprecated/references/` (banner), v5 → `archives/workplans/` (banner
  fixing its J-38 contradiction), decision-queue items 1–3 refreshed + queue demoted to
  dated snapshot, CURRENT.md rows updated (workplan v6 + new Narrative-engine row),
  `lane_assignments.yaml` repointed. Next IN actions live in v6 §2. **⚠️ F-F/fork-8 note
  below is superseded by the ratification above.**

- **Ecosystem-review Top-5 residuals not covered by their own lane.** Filed 2026-06-30 as
  ED-1050..1054 (full report: `designs/audit/2026-06-30-ecosystem-adversarial-review.md`).
  ED-1050 (combat parity oracle) lives in `handoffs/HANDOFF_PC.md` (RESOLVED, one residual
  left). This lane owns the rest:
  - **ED-1051 — module-contract gaps, `needs_jordan`.** `references/module_contracts.yaml`
    has 11/27 modules `doc:null` (grew from the originally-filed 10/27) and 13/27 resolvers at
    `[ASSUMPTION]` grade (grew from 11/27) — re-measured 2026-07-02, docket adjudication
    ED-IN-0002. `engine_clock` (the temporal spine, highest-priority module) now has a
    CANDIDATE home doc — `designs/architecture/propagation_spec_v1.md` (ED-1093, CANONICAL) —
    its `gap_notes` explicitly keep `doc:null` unflipped until this entry is ruled. Authoring
    is effectively done for `engine_clock`; only ratification/ordering remains for it, plus the
    other ~10 modules and 13 resolvers untouched. Also tracked at `decision_queue.md` item 12.
  - **ED-1052 — typed engine-params layer for Godot ingestion, still open.** No scope/fence
    decision made. A narrower path was found and executed (2026-07-01): `tools/export_engine_params.py`
    serializes the LIVE `combat_engine_v1/config.py` Class-C oracle directly to
    `references/engine_params/combat_engine_v1.json` (blocking CI round-trip check),
    sidestepping the settled-vs-in-flux dilemma without deciding the broader
    `params/*.md`-prose-parsing question (its own docstring is explicit it does NOT parse
    prose). A prior attempt (PR #37) asserting a Combat Pool formula as authoritative was
    REVERTED — that's the trap to avoid: type only what's genuinely settled, or mirror the
    live oracle mechanically. Also tracked at `decision_queue.md` items 17 and 24.
  - **ED-1054 — navigation surface, partially done, narrowed 2026-07-02 (ED-IN-0002).**
    Retired-session-file relocation to `deprecated/` is DONE (via ED-1084). Still open: (a)
    relocate the ~850KB of narrative markdown mislabeled as tests
    (`tests/emergent_arc_skeleton_test_2026-04-17_batch*.md`,
    `tests/sim_framework/session_audit_2026-04-19.md`) to `designs/audit/` or `archives/`;
    (b) regenerate `sim/README.md` (self-flags stale rather than being rewritten accurate),
    `sim/CONVENTIONS.md` (still `[PROVISIONAL — Pass 2l armature scaffold 2026-05-17]`), and
    `tools/README.md` (missing `currency_consistency_check.py`, `ci_module_shape_check.py`,
    `export_engine_params.py`, `validate_ed_citations.py`). Also tracked at `decision_queue.md`
    item 25.
  - **ED-1053 RESOLVED 2026-06-30** (see Decisions below).

## Decisions

- 2026-07-07 — **Consolidated ruling pass on the Key & Echo armature §5 docket + ed_options.md
  (ED-IN-0026).** Jordan: "Perform consolidated ruling pass? I want to ratify all and get to work
  on this" — exercising, before merge, the ratification authority PR #85's body had deliberately
  held back. Per-row disposition lives in `key_echo_armature_v1.md` §5's Ruling Log (16 rows) and
  `ed_options.md`'s Disposition table (17 filed EDs). Two rows were genuine no-default forks
  needing an actual pick: the ED-IN-0012/0013 renumber (executed) and the ER-2/Overwhelming
  band-discipline direction (ruled, execution deferred). Two rows (ED-SC-0002, ED-SE-0002) were
  explicitly left to their owning lanes rather than ruled from this IN-lane pass. See the Pending
  entry above for the full headline list.
- 2026-07-02 — **HANDOFF.md split into per-lane files, matching the `ED-<LANE>-NNNN`
  nomenclature.** Jordan: "Handoffs need to have the same tagging nomenclature. There are
  different handoffs for different lanes." Root `HANDOFF.md` is now a thin index + genuinely
  cross-cutting "Next actions" pointer; each lane (`MB, PC, FI, SC, FA, WR, IN, GO, SE`) gets
  its own `handoffs/HANDOFF_<LANE>.md` carrying that lane's Pending/Decisions/Next-actions.
  Motivation is the same one behind the `ED-<LANE>-NNNN` split itself: reduce concurrent-session
  merge-collision surface on shared continuity files. Note this partially reverses an EARLIER,
  deliberate consolidation (`deprecated/session_machinery/` retired per-topic session-log files
  in favor of one `HANDOFF.md`, because fragmented files rotted/went stale) — the difference
  this time is the fragmentation is keyed to the SAME lane taxonomy the ID system already
  enforces, not an ad-hoc per-topic split, and `tools/session_status.py`'s SessionStart banner
  still reads one root file so there's still a single "start here" surface, just a thinner one.
  `tools/session_status.py` unchanged (still greps root `HANDOFF.md`'s one `## Next` heading).
- 2026-07-02 — **`ED-<LANE>-NNNN` lane-tagged editorial namespace created (`ED-IN-0001`, PR #67,
  merged); D1-D5 adjudication docket reconciled (`ED-IN-0002`, PR #69, merged).** PR #58 hit two
  same-session concurrent-allocation collisions on the flat `ED-NNNN` sequence within one PR
  (`ED-1088`→`1090`; then `1089`/`1090`→`1093`/`1094` — see `ED-1094`'s own entry). Jordan: new
  EDs use `ED-<LANE>-NNNN` (9 lanes: `MB` mass battle, `PC` personal combat, `FI` field
  investigation, `SC` social contest, `FA` faction actions, `WR` world, `IN` infrastructure,
  `GO` godot, `SE` settlements — `SC`/`PC` deliberately disambiguated after a first draft
  proposed `SC` for both; a proposed `PY` python lane was dropped as not a real subsystem). Flat
  `ED-NNNN` is FROZEN at `ED-1094`, permanently valid, never retrofitted.
  `references/id_reservations.yaml` gained per-lane `next_free` counters;
  `tools/validate_ed_citations.py` and `tools/currency_consistency_check.py` extended to
  recognize both formats; `CLAUDE.md` §3 documents the format plus a new, not-yet-CI-enforced
  session-lane-scoping convention. Separately, Jordan pasted an uncommitted local adjudication
  docket (D1-D5, drawn from the 2026-06-30 ecosystem review's `needs_jordan` subset) for
  relevance-checking against the current tree; verdicts folded into the ED-1050/1051/1052/1054
  entries above (this file) and `handoffs/HANDOFF_PC.md`.
- 2026-07-02 — **Merge-ratifies-by-default convention adopted (ED-1094); ED-1083 doctrine
  ratified; J-38 propagation spec ratified (ED-1093).** Jordan: merging a PR ratifies its
  PROPOSED/provisional contents by default unless the PR body explicitly holds an item back
  for separate review — closes a real recurring gap where PR #55 was reviewed and merged but
  `holonic_container_doctrine_v1.md` (ED-1083) sat PROPOSED in `main` afterward because the
  prior convention required a distinct explicit ratification step nothing forced to happen.
  Applied same-day: ED-1083 flipped provisional → ratified; doctrine `## Status:` line
  PROPOSED → **CANONICAL**; `CURRENT.md` gained an Architecture/Holonic-doctrine row;
  `decision_queue.md` item 20 struck resolved; `CLAUDE.md` §2 documents the standing rule.
  **Applied a second time to J-38 itself, same PR (#58):** rather than land the propagation
  spec as PROPOSED and rely on "ratifies on merge" text (which would repeat the exact ED-1083
  failure mode this convention exists to close), the flip to CANONICAL was pre-staged in the
  PR — `designs/architecture/propagation_spec_v1.md` `## Status:` line PROPOSED → **CANONICAL**,
  ED-1093 ledger entry `status` → `ratified`, `decision_queue.md` item 18 struck resolved. A
  whole-session Fable review (triggered after the ED-1088 ID-collision reconciliation) caught
  this risk plus stale cross-references before merge. Scope: governs future PRs; does not
  retroactively reopen closed decisions or ratify anything a PR explicitly holds back and flags
  loudly as such.
- 2026-07-01 — **Month-overview + architecture-consolidation session executed** (12+ commits,
  ED-1081..1087; overview + execution/reconciliation logs + the frozen 23-item Jordan decision
  queue at `designs/audit/2026-07-01-month-overview-architecture-consolidation/`). Landed:
  LB-21 round-3 ID re-block · two silently-dead enforcement pieces revived
  (`broken_dependency_checker` ledger check; non-executable tracked pre-commit hook) · CLAUDE.md
  §6 falsified claims corrected (ED-1050/ED-1054 states) · holonic container doctrine v1
  **PROPOSED** (`designs/architecture/holonic_container_doctrine_v1.md`, ED-1083 — Jordan-vetoable)
  from the ingested 2026-07-01 workflow spec · Combat Pool collapsed to `max(5, History+6)` across
  every live stale site (ED-1084) · `values_master.yaml` QUARANTINED · names_index v2 (proper-noun
  fold; mirror 23→83) · session-log machinery → `deprecated/session_machinery/` · combat engine
  runtime **numpy-free** (σ-kernel via `sim.autoload.sigma_leverage`; state kernel engine-owned;
  ED-1085) with new container-hygiene guard · **first typed Godot params artifact**
  (`references/engine_params/combat_engine_v1.json`, blocking round-trip CI; ED-1052 seed) ·
  contract-conformance CI (report-only; ED-1051 backlog surfaced per-PR) · CLAUDE.md §10 fable
  tier + relay patterns; workplan **J-38** (propagation-spec authorship) docketed ·
  `currency_consistency_check` self-updating recency gate (CI + SessionStart banner; ED-1087) ·
  freshness pins refreshed + gate flipped **blocking** (LB-23 residual closed). Three scope
  defaults adopted Jordan-vetoable (values_master quarantine-not-regenerate; Godot seed included;
  freshness flip). Rulings made: **none** — everything gated sits in the decision queue.
- 2026-06-30 — **ED-1053 resolved: working-tree integrity port + sim oracle.** Ported the three
  "integrity" gates off the GitHub API to the working tree (no PAT/network): `broken_dependency_checker`
  and `patch_propagation_checker` now `os.walk`/read locally (both green against the checkout);
  `freshness_gate` computes git blob SHAs locally (verified identical to `git hash-object`) and checks
  119/131 `canonical_sha__` pins (12 stale → report-only). Dropped `GITHUB_PAT` from the CI integrity job.
  Hardened `ci_sim_fabrication_check`: full float-literal capture + `(variable,value)` matching close the
  value-collision / float-split holes (corpus blast kept to +~200 latent, changeset-scoped; `tools/`
  excluded from sim-classification). Added the first `sim/` test — `sim/tests/test_mc_v18_regression.py`
  (deterministic seeded `run_batch(n=2,seed=0)`: determinism + golden + bounded smoke) — and a new
  'Sim Reference Regression' CI job wired into All-Gates-Green. Updated CLAUDE.md §8.
- 2026-06-30 — **Adversarial ecosystem review + safe fixes.** Ran a 72-agent verification workflow
  (6 audit dimensions × 2 skeptical lenses); 24 findings survived, headline items hand-spot-checked.
  Rewrote `CLAUDE.md` into a Claude-Code-optimized operating manual (numbered sections, currency
  priority, data→Godot pipeline, port state, known-defect callouts). Filed the report under
  `designs/audit/` and the Top-5 as ED-1050..1054. **Re-blocked IDs** (`references/id_reservations.yaml`
  v2: round-1 A/B/C exhausted+overrun to ED-1042; round-2 block D = ED 1050-1099 / PP 800-829, next_free
  ED-1081, after contest_rebuild reserved 1055-1079 + combat at 1080). **Safe code/doc fixes applied:** single-sourced the patch-register size cap
  (`ci_register_size_check.py` 20k→policy 15k; register is ~5k); RETIRED banners on
  `references/subsystems/{handoff,checkpoint,session_log}_subsystem.md`; flipped
  `canon/session_checkpoint.md` `status: active`→`retired`; STALE banners on the four `designs/godot/*.md`
  specs; rewrote `README.md` to defer to CLAUDE/CURRENT/HANDOFF. **Not done (needs Jordan / re-sweep):**
  the parity-oracle balance values (ED-1050) and the Gate-0/contracts authoring (ED-1051).
- 2026-06-29 — **ED-citation integrity: full reconciliation (292 → 0; gate now BLOCKING).** Diagnosed the
  292 report-only violations: 286 `NONEXISTENT` from **dual ledger-of-record drift** (design docs minted ED
  numbers in inline `[EDITORIAL:]` tables never migrated to the JSONL), 6 `OPEN_AS_BASIS` (2 of them validator
  false positives). Fixed 3 validator defects (`tools/validate_ed_citations.py`): active-ledger precedence
  over stale archives, loud-parse + regex-salvage of 7 malformed archive YAMLs, and same-line basis scoping
  (table-row bleed). **Registered 91 grounded entries** (36 resolved / 12 provisional / 30 open / 13
  needs_jordan) — each verified against its citing doc by per-batch subagents (anti-fabrication). Repointed
  the ED-814→ED-907 phantom and reworded open/provisional over-claims to `pending`. Dropped `continue-on-error`
  on the `ed-citations` CI job + added to `ci-summary` needs. Report:
  `designs/audit/2026-06-28-ed-citation-triage/02_reconciliation.md`. **Residual for Jordan:** 13 needs_jordan
  items (NPC naming ED-634/595–602/610, ED-885 ratification ID); ID collisions ED-408–411/413/417/647.
- 2026-06-28 — **Editorial-ledger relevance triage.** Deep per-item verification of all **93 unresolved**
  entries (82 open + 10 provisional + 1 deferred) against the live working tree, in 6 read-only cluster
  passes. Result: **37 still relevant** (25 real open work + 12 NEEDS_JORDAN), **56 stale**. Applied via
  Workflow D: **31 struck** (21 superseded by later canon — esp. the mass-battle per-cell/Lanchester
  re-architecture + the 2026-06-22 `net-(Ob-0.5)` continuity fix; 10 `[PROPOSED:…]` migration residue),
  **25 resolved** (open-but-done — decision had landed, row never closed). Unresolved queue 93→37.
  ED-citation violations dropped 315→292 as a side effect. Report:
  `designs/audit/2026-06-28-editorial-relevance-triage/relevance_triage.md`. **Residual for Jordan:** 12
  NEEDS_JORDAN items (NPC naming ED-649/650/651, deferrals ED-644/788, design-intent gates
  ED-879/893/911/920/924/1033/1036); three of these (644/649/893) are the OPEN_AS_BASIS citations still
  holding the ED-citation validator report-only.
- 2026-06-28 — **Open-session unification + LB-22 closed.** Reviewed every `origin` session branch;
  six were already squash-merged into main (#14–#21), one (`claude/github-ci-environment-review` = PR #18)
  carried genuinely-unmerged work, and `claude/refresh-state-3m7nL` (abandoned 04-20 pre-migration line
  carrying the retired `session_checkpoint`/`session_log` harness) was excluded from the merge. Unified
  PR #18's **net-new** half (the LB-22 backlog) onto main — its already-landed half (12 skills +
  coverage_matrix, via #16) was kept at main's version, no re-litigation. **LB-22 done:** `valoria-orchestrator`
  retired to `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier.py`
  Check 4 flipped to **blocking for `skills/`** (`tools/` stays WARN pending the API→disk port). PR #18
  closed as superseded. `ci_register_size_check.py` taken from #18 (importable, no-PyYAML, ships the
  drift-guard test) with #22's `names_index.yaml` threshold line re-added; `lane_assignments.yaml`
  owns-globs repointed to `deprecated/`.
- 2026-06-28 — **Master Workplan v5** authored (`designs/audit/2026-06-28-recent-work-orchestration/`),
  reconciling the post-v4 work (06-12→06-28) into one register and superseding v4. Roadmap +
  lane_assignments repointed to v5. Ledger verified live: **713** entries / 0 duplicate IDs / ED 1042.
  (v5 de-staled this pass to live HEAD; PRs #16–#22 reconciled — see its §0/§10.)
- 2026-06-24 — Migrated the Claude↔GitHub automation to a Claude Code-native model:
  retired the `/home/claude` GraphQL/cache/session harness; gates now live once in `tools/`
  and run in CI (authoritative) + local hooks/`.githooks` (advisory). See the migration PR.
- 2026-07-01 — **Workplan sprawl cleanup.** `designs/workplans/` was dead (both files pre-dated v3/v4)
  while the live master workplan kept spawning in a fresh one-off `designs/audit/<date>-*/` folder each
  revision, so `CURRENT.md` had to manually chase it. Relocated v5 into `designs/workplans/` (now the
  one live home — see its `README.md`); archived the two dead files to `archives/workplans/`. Repointed
  `CURRENT.md`, `references/lane_assignments.yaml`, `references/roadmap_state.yaml`, and v5's own §0
  commit-path note. Frozen historical versions (v4 in `designs/audit/2026-06-11-orchestration/`, v3 in
  `2026-06-10-master-workplan-v3/`) were left in place intentionally — they're bundled with sibling
  audit artifacts and CURRENT.md already documents them as frozen records, not lost ones. Separately,
  flagged (not moved) the `sim/` vs `tests/sim/` vs `tests/sim_framework/` naming collision — three
  distinct-purpose directories, not duplicates; disambiguated via README notes in each rather than a
  path rename, since `tests/sim/` is path-matched by `ci_sim_fabrication_check.py`/`atomization_rules.yaml`/
  `lane_assignments.yaml` and a rename would need to update all three.

## Next actions

_(Reserved-ID state healthy as of 2026-07-02: LB-21 executed, then the `ED-<LANE>-NNNN` cutover
(ED-IN-0001) froze the flat sequence at `ED-1094`. `references/id_reservations.yaml`'s `lane_ids`
section is now the live allocation source for all NEW EDs — read `next_free` for your lane,
allocate, bump, co-commit; never max+1.)_

- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec now
  RATIFIED (2026-07-02).** The month's comprehensive review, the consolidation
  execution/reconciliation logs, and the **single consolidated 23+2-item Jordan decision queue**
  live at `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see
  `decision_queue.md` first — every gated item below is indexed there). **Doctrine ratification**
  (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`) and **J-38 propagation-spec
  authorship** (ED-1093, `designs/architecture/propagation_spec_v1.md` — supplies `engine_clock`'s
  candidate home doc; the `doc:null`/[ASSUMPTION] grade stays unflipped until ED-1051 is
  separately resolved) are both **CANONICAL** as of PR #58 (ED-1094 merge-ratifies-by-default).
  The propagation spec's own §5 carries its ranked open items (OF-7/OF-B1 amendments, D.6/OF-D6
  double-count, `decay()` spec, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) — ratification
  did not resolve these, only fixed the spec's home-doc status. Remaining highest-leverage queued
  decisions: the values_master regenerate-vs-retire call, the duplicate compilation homes, and
  item 19 (Agent-Teams/subagent-roster adoption).
- **Done this pass:** unified PR #18's net-new into main → **LB-22 complete** (orchestrator retired to
  `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier` Check 4 blocking
  for `skills/`). Earlier passes already landed the coverage_matrix single-source + 12-skill boilerplate
  strip (#16) — kept at main's version during the unify.
- **LB-22 residual (small):** `tools/` analysis utilities still carry `/home/claude` refs (WARN tier in
  `ci_hooks_verifier`); flip the `tools/` scope to blocking only after the GitHub-API→working-tree port
  (`freshness_gate`, `broken_dependency_checker`, `compliance_check`, `extract_*`, `valoria_collator`,
  `valoria_bulk_fix`). `valoria-orchestrator`'s old `tests/registry/test_descriptor_registry.py` import
  is dead (reads `/home/claude/…`, not CI-collected) — left as-is.
- **CI debt blocking-flips (LB-23) — reconciled 2026-07-01 (ED-1082):** `validate_ed_citations`
  is **already blocking** (since 2026-06-29, 0 genuine violations — the old "flip once triaged"
  action here was stale). `freshness_gate`'s remaining report-only step is being closed by the
  month-overview consolidation itself (pin refresh + blocking flip as its final commit); the
  optional K-2 SHA-split (115 `canonical_sha` fields → `references/canonical_freshness.yaml`)
  is a refactor that can follow independently, no longer a precondition.
- **`ci_political_v30` read-routing (LB-24):** raw file ~26k but tracked read returns 0
  (index-routes). Tooling/routing bug, not a faction-content decision — cross-referenced in
  `handoffs/HANDOFF_FA.md` since the file itself is faction/political content.
- **Ledger-status reconciliation (LA-23, Lane A — mostly done):** flipped ED-841/842/912 `open`→`resolved`
  and filed the never-written ED-938/ED-939 (backfilled from #13; artifacts verified). Dropped the
  report-only `validate_ed_citations` count 748→731. **Residual:** ED-914 left `open` — its mechanical
  parts remain (PP-719 record-or-strike; dead `fieldwork_design_v1` parent-path refs in `params/bg/core.md`,
  `designs/scene/fieldwork_v30.md`, `designs/scene/fieldwork_godot.md` — cross-referenced in
  `handoffs/HANDOFF_FI.md`).
- **The new `ED-<LANE>-NNNN` namespace's own residual (from ED-IN-0001's PR body):** the
  session-lane-scoping convention (`CLAUDE.md` §3) is documented but not yet CI-enforced —
  detecting which lane a PR's file changes belong to and flagging mismatches is real follow-up
  work, not built yet.
