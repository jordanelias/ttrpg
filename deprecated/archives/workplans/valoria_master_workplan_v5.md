# Valoria — Master Workplan v5 (post-v4 reconciliation, three-lane, single register)

> ⚠️ **SUPERSEDED (2026-07-05, ED-IN-0009) — DO NOT RESUME FROM THIS FILE.** The live master
> is `designs/workplans/valoria_master_workplan_v6.md`; its Appendix A accounts for every
> open item below. Known defect this banner corrects (ED-IN-0006): §3's J-38 row below says
> open/PROPOSED — **J-38 was RATIFIED 2026-07-02 (ED-1093/ED-1083/ED-1094)**; trust
> CURRENT.md, never this file, for status. J-/LA-/LB-/LC- keys remain citable as history.

**2026-06-28 · status: SUPERSEDED by v6 (was CANON-PROPOSED; the active master 2026-06-28 → 2026-07-05).**
**as_of: live HEAD `d80d364` (#22; first written `as_of a3837d0`/#15 and de-staled this pass — see §10). Verified live: editorial ledger `canon/editorial_ledger.jsonl` = 713 entries / 0 duplicate IDs / ED ceiling 1042. v4's register and lanes are carried forward; this document folds the post-v4 work (06-12 → 06-28) that no prior workplan had reconciled, plus the six PRs (#16–#22) that landed at/after first write (§10).**

**Supersedes (on commit):** `designs/audit/2026-06-11-orchestration/valoria_master_workplan_v4.md` — its §0 reconciliation, §1 operating model, §2 unified register (rows 1–38), §3 docket (J-1…J-35), and §4–§6 lane queues are RETAINED. v4 stays the frozen 06-11/06-22 record; J-/LA-/LB-/LC- IDs stay citable and are NOT renumbered. v5 extends and de-stales them with the month of work that landed since.

**Binds (does not fork):** `references/lane_assignments.yaml` (owns-globs, reserved blocks) · `references/roadmap_state.yaml` (repointed here) · `references/id_reservations.yaml` (exhaustion flagged below) · the 2026-06-28 audit corpus this document dockets (`designs/audit/2026-06-28-*/`).

`[SELF-AUTHORED — bias risk: the reconciled inputs and the 06-28 critiques are Claude-authored across 06-12→06-28 sessions. Counterweights carried forward from v4 §8. This consolidation applies the recent work's ratified rulings and files its open findings as docket rows; it asserts no new game values and rules nothing — every recommendation is Jordan-vetoable, §3 is the veto surface.]`

---

## §0 — RECONCILIATION RECORD (post-v4 work streams; per-stream scan, citations to live commits)

v4 reconciled work through the **06-22 loose-ends sweep** (its §0 stops at ledger ED-1038). Between 06-12 and 06-28 the following landed and is folded here. Ledger moved 653 → **711** entries; ED ceiling 1012 → **1042**.

| Stream (commit) | What landed | Register effect |
|---|---|---|
| **Infra migration** (`1be02b6`, #11; `6d12980`; 06-24) | Claude↔GitHub ecosystem migrated to a **Claude-Code-native** architecture; CI gates **decoupled** (each gate runs independently; aggregator added) and a local advisory tier added (`.githooks/pre-commit` + `.claude/settings.json`), all validators sharing one implementation in `tools/`. Decoupling surfaced two pre-existing debts and applied **interim** treatments: `freshness_gate`'s stale-canonical step made **report-only** (broken-dependency + patch-propagation stay BLOCKING); `coverage_matrix` cap found bumped to 10000 in a **third** location (`atomization_rules.yaml`). | New **LB items** (below): the two blocking-flips + the coverage_matrix consolidation. The migration itself closes the v4 "Claude Code/ultracode migration (workflow)" out-of-register note. |
| **ED-912 — Disposition & Knot ±5** (`75a3eb9`/`a3837d0`, #14/#15; 06-28) | Jordan ruling: Disposition becomes a flat −5..+5 (no Bonds ceiling; **Bonds ≥ 5 is now an explicit Knot prerequisite**), resolved via a stepped Ob table; the Knot model = ED-773 strain reframed as a bidirectional −5..+5 bond-strain gauge. Break/rupture = Disposition −3, 4 Composure. **Resolves ED-841/842/912/914; supersedes PP-632/PP-684.** Source-of-truth + consumer-tail regenerated across fieldwork/derived_stats/threadwork/core/knots/registry/clock_registry; canonical_sources SHAs refreshed; "Disposition table" → "Stance table" in mass-combat (disposition struck from combat per ruling). **`[LEDGER-FLIP — DONE this PR (LA-23): ED-841/842/912 flipped open→resolved with resolution notes citing the ruling. ED-914 left open — its consolidation direction is resolved but mechanical residuals remain (PP-719 record-or-strike; dead fieldwork_design_v1 parent-path refs in 3 files); progress noted on the entry.]`** | **Advances register #22** (value-taxonomy: Composure 4-on-break now fixed, Disposition decoupled) and feeds **#20 / J-18** (fieldwork canonical-line). Disposition triple-divergence (row #20) substantially narrowed. |
| **J-31 social-contest repair** (`ba62f19`, #13; 06-26) | Recovered the J-31 docket from a pre-switch WIP stash: ED-938/939/1042 + rule resolutions ED-890/893/894/895/896/897/899/900/902 (PP-351/614). **`[LEDGER-GAP — FIXED this PR (LA-23): ED-938 (v2 supersession) and ED-939 (Rattled +1 Ob → −1D) were referenced in the #13 commit + live docs (clock_registry_v30, derived_stats_v30 §10.5) but never filed. Both now filed as resolved entries (artifacts verified live), so the dangling citations resolve.]`** Repointed every stale `social_contest_system_v2.md` reference to `social_contest_v30.md` across 22 docs (+ SUPERSEDED/DO-NOT-CITE banner on v2, ED-938); terminology rename (Past/Future→Memory/Projection, Direct/Indirect→Revealing/Obscuring, CLASH/REINFORCE/CROSS, Suspicion Token→Doubt Marker, Read→Appraise); rescaled Composure/Concentration/Health/Stamina; registered Persuasion Track + Obligation clocks; de-duped §5.2 (ED-1042). | **Advances register #15 (J-31 → LA-19) substantially.** Two carried residuals: (a) the **contest.py sim edit is deferred** behind pre-existing sim-fabrication debt (19 uncited constants on main block any edit until separately triaged) → new Lane-C/Lane-B triage item; (b) ED-1033/1036 (row #33) still open. |
| **Combat engine ER-2 fix** (`793f1a6`, #12; supersedes #10) | `degree()` now applies the ER-2 continuity correction (k−0.5 banding) that had landed in canon TEXT (`a3d3888`) but never in engine CODE — without it the continuous read ran 5–9pp low across the 5–13D band (NERS R+S fail, 2026-06-23). Dead `DAMAGE_SCALE`/`CAP_END` knobs removed. | **Touches register #17 / #35** (personal-combat residual): code-side propagation of ratified canon; the engine↔doc seam (F3/F4) narrows. Does not resolve J-33 (the ratify/coverage decisions remain). |
| **NPC v30 audit + audit-of-the-audits staging** (`8a2dbed`/`d446cc2`; merged `2508d36`, #9) | 449 verified findings across 24 NPCs + 6 system + ethics/resonance staged as **ledger candidates**; combat-traditions morphology critique checkpointed. | **Not new P1s** — staged candidates file via lane-block discipline at next lane entry (per v4 §0 staging counsel). Tracked, not docketed as register rows. |

**No new P1-class architecture defect surfaced by the post-v4 work.** The two 06-28 critiques (below) are *under-configuration / seam-closure* findings against systems already in the register, not new failure classes — their own headlines say so ("none of this requires redesigning a mechanic").

---

## §1 — OPERATING MODEL (carried unchanged from v4/v3)

Three write-disjoint lanes per `references/lane_assignments.yaml` (owns-globs; reserved ED/PP blocks — see §0a exhaustion note). One operator; sessions are the currency; **Lane B WIP = 1**; rituals ride with feature work; budget rule — no new structural proposal advances while the K-items are unbuilt; hooks detect · the model interprets · Jordan decides. The Decision Docket (§3) is not a lane; every lane parks against it. This consolidation session operates under the sole master handoff, outside lane declaration.

### §0a — RESERVED-ID EXHAUSTION (new launch-blocker)

The reserved ID blocks in `references/id_reservations.yaml` (A 890–939 · B 940–969 · C 970–999; verified live max ED 884 / PP 726 on 2026-05-31) are **exhausted**: the live ED ceiling is now **1042**, past every reserved range, and the ledger already carries IDs in the 1000s (filed ad hoc since the blocks ran out). Per the file's own `exhaustion_policy` ("at integration: assign the next disjoint blocks per lane; never overlap a prior block; bump version"), the next round of disjoint blocks must be assigned before any lane allocates again. → **LB-21** below.

---

## §2 — UNIFIED OPEN REGISTER — v5 DELTA

v4 §2 rows **1–38 carry forward** as the standing register (not re-printed). The post-v4 work re-statuses these rows; the 06-28 audit batch adds new rows **39–42**.

### Re-statused carried rows (per §0)

| Row | New status |
|---|---|
| **#15** Social-contest record (J-31 → LA-19) | **ADVANCED** — J-31 docket recovered + 22-doc repair landed (`ba62f19`); CR1–CR7 propagation (LA-19) remains; contest.py sim edit deferred behind sim-fabrication debt; ED-1033/1036 still open (row #33). New deliberative-game findings extend the docket → **#39**. |
| **#17 / #35** Personal-combat residual | **ADVANCED** — ER-2 continuity correction propagated to engine CODE (`793f1a6`); dead knobs removed. J-33 ratify/coverage decisions unchanged. Combat-traditions critique adds **#41**. |
| **#20** Fieldwork canonical-line split (LA-1 + J-18) | **ADVANCED** — ED-912 collapses the Disposition triple-divergence to the flat ±5 model; Thread-Read stat + §11 remainder still gate Lane-C module 20. |
| **#22** Value-taxonomy drift (J-12 + LA-18) | **PARTIALLY RESOLVED** — ED-912 fixes Composure-on-break (→4) and decouples Disposition from Bonds; Composure ×3-vs-+6 name/formula call (J-12) + Stamina/Concentration/Combat-pool/Intel consumer staleness (LA-18) remain. |

### New rows (06-28 design-audit batch — currently undocketed findings)

| # | Finding / decision | Sev | Source (corpus) | Owner |
|---|---|---|---|---|
| 39 | **Social-contest "deliberative game" under-configuration** — 8-lens critique (`2026-06-28-social-contest-deliberation-critique/critique.md` + `findings.json`; 38 findings, 0 refuted, 9 downgraded, 2 already-handled; 11 strengths). Headline: the contest is a mature **agôn** that collapses the other three deliberative functions (bargain / truth / unity) and three Caillois families (alea / mimicry / ilinx) onto the single zero-sum Persuasion Track. Highest-leverage, descending: **(1)** point the existing **armature dot-product** at the *adjudicator* (verdict legitimacy currently a flat `avg-Stability − 1` scalar, not emergent) — the central bottom-up violation; **(2)** make the **procedure contestable** (capture / forum-shopping / antechamber — *broglio*; Disposition+Subversion stop at the chamber door); **(3)** add a **Negotiation/ZOPA** mode + faction **win-sets** (Putnam two-level — the spec itself defers this); **(4)** add the missing resolution families (**alea**/sortition, **mimicry**/acclamation, **Type-3** consensus-with-holdout); **(5)** add a **commitment store** (a ledger of conceded propositions; "Concede a Point" today records nothing). Much of the fix is **propagating ratified-but-stranded design** (CR5, groundup win-conditions/Panel, `belief_revised` Key) → ties **#15 / J-31 / LA-19**. Recommendations tagged free-win / structural / needs-your-call in critique §6. | **design-tier** (mostly P2/P3 seam-closure; no new P1) | social-contest deliberation critique 2026-06-28 | **J-31** (extended) → LA-19; new builds Lane C |
| 40 | **Distillation & cross-scale coherence** (`2026-06-28-distillation-coherence/distillation_coherence_report.md`; method-flagged `[VERIFY]` — the adversarial pass was rate-limited, not run). Two-primitive meta-finding (sigma resolver + armature dot-product are the whole spine; everything else is accounting/clock/read/manifest). Debt is connective tissue: **(1) six systems write state silently OFF the Key bus** — `territorial_piety`, `ci_political`, `victory`, the **Mending Stability world-clock** (no module owns it), Coherence threshold-crossings, settlement events — breaking save=initial+log/replay; the report calls this "the single biggest thing between you and one coherent engine"; **(2)** the 7-value resolver enum is really **2 parameterizations + 4 non-rolling kinds** (social/mass never formally verified against the kernel); **(3)** state buckets mislabeled (climb-to-threshold "track" → really "clock"; Initiative/Poise need a mean-reverting signed-float bucket that doesn't exist); **(4)** phantom/duplicate modules (`settlement_economy`/`npc_memory`/`scene_timer`+`audit`/`campaign_architecture`). Ties **#4** (shadow/phantom modules), **#5** (duplicate pairs), **#22** (bucket taxonomy), **#37** (`ci_political` access). Needs the deferred adversarial verification before any structural action. | **architecture-tier** (P2; `[VERIFY]`-gated) | distillation-coherence 2026-06-28 | **J-36** (new) — Key-bus closure decision; gates Lane-C wiring |
| 41 | **Combat-traditions morphology / distillation critique** (`2026-06-28-combat-critique/` — distillation proposal + compact/reconcile inputs, recovered modules & resolution, recovered reconcile + adversarial pass, `2026-06-28-combat-critique-recovered.json`). Checkpointed prior-session WIP (committed `a3837d0`); a morphology critique → integration-spec line on the combat traditions (F2 tradition-imbalance / dead-abilities territory, register #17). Needs a read-through to extract its ratified-vs-open split into the docket. | **design-tier** (combat; ties #17) | combat-critique 2026-06-28 | **J-33** (extended) |
| 42 | **Deprecation / currency enforcement sweep** (`2026-06-28-deprecation-currency-sweep/deprecation_currency_plan.md`). A plan to enforce deprecation/currency discipline across the corpus (deprecation-map residual, supersession-register wiring — extends v4 LB-19). Lane-B enforcement work, not a design decision. | **infra (P3)** | deprecation-currency-sweep 2026-06-28 | **Lane B** → LB-22 |

`[NULL: no new P1 class. The 06-28 critiques are under-configuration/seam-closure against systems already in rows #4/#5/#15/#17/#22/#37; their own executive summaries state "none of this requires redesigning a mechanic."]`

---

## §3 — DECISION DOCKET — v5 ADDITIONS

v4's J-1…J-35 carry forward unchanged (status as of v4 §3 + the §0 advances above). New / extended keys:

| ID | Decision | Unblocks |
|---|---|---|
| **J-31** (extended) | Social-contest sitting now also carries the deliberative-game findings (row #39): adjudicator-armature retarget (free-win-tier), procedure-capture, ZOPA/win-sets, the three missing resolution families, the commitment store. Rule alongside the existing §5 D-1…D-10 + 06-18 residual. | LA-19; the new social builds (Lane C); module 13 confidence |
| **J-36** (new) | **Key-bus closure**: ratify bringing the six off-bus writers (territorial_piety, ci_political, victory, the MS world-clock, Coherence crossings, settlement events) onto the Key substrate — or accept specific carve-outs. Gated on the distillation report's deferred adversarial-verification pass (row #40 `[VERIFY]`). | Lane-C wiring of those systems; the "one coherent engine" goal; articulation/chronicle completeness |
| **J-33** (extended) | Combat residual now also carries the combat-traditions morphology critique (row #41) — fold its ratified-vs-open split in when J-33 is ruled. | module 16 completion |
| **J-38** (new, 2026-07-01, ED-1083/ED-1086) | **Propagation-spec authorship**: the cross-scale propagation contract — per-direction boundary transform (aggregate up / distribute down), ordering & determinism (seeded RNG, stable iteration, fixed step), and a termination/convergence guarantee (bounded depth or fixpoint). Named by the holonic doctrine (`designs/architecture/holonic_container_doctrine_v1.md` §4) as the highest-value unauthored canon: it interlocks the Godot conversion-strategy register #1 (downward Key delivery, ED-1006) and the `engine_clock` doc:null gap (ED-1051). Top-tier judgment (CLAUDE.md §10 `fable`/`opus`); lands as its own PROPOSED design doc. | register #1; ED-1051 `engine_clock`; Lane-C ports beyond the combat slice; doctrine ratification (ED-1083) |

**Docket cadence is Jordan's.** The recent work cleared no docket key outright but *advanced* J-31 (repair landed; sitting now larger but better-evidenced) and narrowed J-18/J-12 via ED-912.

---

## §4–§6 — LANE QUEUE ADDITIONS

v4's LA-/LB-/LC- queues carry forward. New items:

### Lane A (Canon / Editorial / Design-content)
- **LA-19** (carried) — now the home for the row-#39 propagation (CR1–CR7 + groundup win-conditions/Panel + `belief_revised` Key) once J-31's extended sitting rules.
- **LA-23** (new — **mostly DONE this PR**) — **ledger-status reconciliation for the recent rulings**: ✅ ED-841/842/912 flipped `open`→`resolved` (resolution notes cite the 2026-06-28 ruling); ✅ ED-938/ED-939 filed as resolved entries (artifacts verified). Dropped the report-only `validate_ed_citations` count 748→731 (LB-23). **Residual (still open):** ED-914's mechanical parts — **PP-719** record-or-strike + the dead `fieldwork_design_v1` parent-path refs in `params/bg/core.md`, `designs/scene/fieldwork_v30.md`, `designs/scene/fieldwork_godot.md`. Lane A ONLY (structural ledger ops). | gated: none (editorial-tier; Jordan-vetoable). |

### Lane B (Infrastructure · WIP = 1) — the deferred HANDOFF debt, now docketed
| ID | New item | Gate |
|---|---|---|
| **LB-21** | **Reserved-ID re-block** (§0a) — assign the next round of disjoint ED/PP blocks per lane in `references/id_reservations.yaml`, never overlapping a prior block; bump `version`; refresh `verified_live_max`. Launch-blocker for clean concurrent allocation. | integration seam (do at a lane pause) |
| **LB-22** | **DONE (§10, unified from PR #18).** `valoria-orchestrator` retired to `deprecated/skills/`; `valoria-vector-audit` read-path rewritten to read the working tree; `ci_hooks_verifier.py` Check 4 flipped **warning → blocking for `skills/`** (`tools/` stays WARN pending the API→disk port). **Residual carried to a new LB item:** flip the `tools/` scope to blocking after porting `freshness_gate`/`broken_dependency_checker`/`compliance_check`/`extract_*`/`valoria_collator`/`valoria_bulk_fix` off `/home/claude`; the deprecation/currency sweep itself **executed** in #17 (row #42) — only wiring `canon/supersession_register.yaml` into the fetch set (v4 LB-19) remains. | — (cleared) |
| **LB-23** | **CI debt blocking-flips** — after **K-2 (SHA-split)** moves the 115 `canonical_sha` fields out of `canonical_sources.yaml` → `references/canonical_freshness.yaml` (writer `tools/freshness_gate.py`), flip `freshness_gate`'s stale-canonical step back to BLOCKING. Separately, **reconcile the `validate_ed_citations` state**: the tool `sys.exit(1)`s but the CI job pins `continue-on-error: true` (`valoria-ci.yml` "ED Citation Integrity (report-only)") — so it is **non-blocking**, surfacing **315 corpus-wide violations / 190 open-ref info (verified live at HEAD `d80d364`; was 748/788 — #20's validator-precision pass dropped it by ~2×)**. Flip to blocking only after the count is triaged toward 0 (LA-23 chips at it; the bulk is `mechanical_terms_index`/`throughlines`/registries citing open/legacy EDs). Solo / non-parallel-window (K-2 / LB-6 class). | K-2 (solo) |
| **LB-24** | **`ci_political_v30` read-routing** (v4 row #37) — raw file ~26k bytes but tracked read returns 0 (index-routes to `_index.md`); CI is the central pacing valve. Rebuild/repoint the read path. | — |

### Lane C (Simulation / Godot)
- **Social-contest deliberative builds** (row #39) — the adjudicator-armature retarget, ZOPA/win-set modes, alea/mimicry/Type-3 resolution families, commitment store: each a Lane-C build **gated on J-31's extended sitting**.
- **Key-bus closure wiring** (row #40/J-36) — bring the six off-bus writers onto the substrate, **gated on J-36** + the deferred adversarial pass.
- **contest.py sim-fabrication triage** — the 19 uncited constants on main block the J-31 sim edit; triage (cite or cut) is a prerequisite to landing the deferred contest.py change. Lane-C (or Lane-B if treated as sim-anti-fabrication tooling).

---

## §7 — DONE THIS PASS (executed with this workplan; excluded from queues)

Two unambiguous Lane-B quick-wins landed alongside this document:
- **coverage_matrix threshold consolidated to one source** — `tools/ci_register_size_check.py` now reads the `tests/coverage_matrix.md` cap from `references/atomization_rules.yaml` via `_coverage_matrix_threshold()` (safe hardcoded fallback so the unbypassable CI gate never crashes on a parse error); the duplicated literal that had drifted 8000-vs-10000 is removed. (Closes the v4/HANDOFF consolidation item.)
- **Old-harness boilerplate stripped from 12 domain `skills/*/SKILL.md`** — `Model:` lines + `assert_bootstrap()`/`quick_bootstrap()` bootstrap-gating + `g.read_files_graphql()`/"fetched from GitHub this session" framing removed; required-file lists preserved and repointed to working-tree reads (the CLAUDE.md "working tree is the source of truth" migration). `valoria-vector-audit` (load-bearing read-path) and `valoria-orchestrator` (retired-harness skill) deliberately left for LB-22.

---

## §8 — CARRIED PRINCIPLES

v4 §8 carries unchanged (Deferred/Triggered/Dropped sets; the three process principles — *propagate-don't-caveat*; *ED citations ledger-verified, never memory-sourced*; *source-tier discipline*). One reinforcement from this pass:
- **Rules live once.** The coverage_matrix consolidation realizes the CLAUDE.md "every rule lives once, in `tools/`, called by both CI and hooks" invariant for a threshold that had silently triplicated. Audit the other `ci_register_size_check.py` literals against `atomization_rules.yaml` for the same drift class (a larger LB item, not done here).

---

## §9 — SEQUENCE & SIZING

- **Jordan (docket):** unchanged priority from v4 §9 (J-2 → J-1 → J-22 → J-6 → J-23, then the sittings). J-31's extended sitting and the new J-36 (Key-bus closure) slot into the system-gate tier; J-36 waits on the distillation report's deferred adversarial pass.
- **Lane B (WIP=1):** the two quick-wins are done; remaining new spine — **LB-21 (re-block, at the next integration pause)** → LB-24 (ci_political read-routing, ungated) → LB-22 (vector-audit rewrite → ci_hooks_verifier flip) → **K-2 (solo)** → LB-23 (freshness/ED-citation flips). LB-22's deprecation-enforcement + supersession-wiring ride the K-budget.
- **Lane A:** LA-19 fires after J-31's extended sitting; the ED-912 consumer tail is already propagated.
- **Lane C:** the social-contest builds + Key-bus wiring are gated (J-31 / J-36); the contest.py sim triage is the ungated prerequisite that unblocks the deferred J-31 sim edit.
- **Commit path for this orchestration:** quick-wins (`tools/`+`references/` + 12 `skills/`) → this workplan under `designs/audit/2026-06-28-recent-work-orchestration/` → repoint `roadmap_state.yaml` + `lane_assignments.yaml` source to v5 → update `HANDOFF.md`. Banner v4 superseded on commit. **[RELOCATED 2026-07-01: moved to `designs/workplans/`, now the one live home for the master workplan — see its `README.md`. This file's own path references above describe where it was originally committed, not where it lives now.]**

---

## §10 — POST-AUTHORSHIP RECONCILIATION (de-stale to HEAD `d80d364`)

v5 was first written `as_of a3837d0` (#15). Six PRs landed at/after that point; this section folds them so the register is live, not frozen. (Verified live: ledger **713** / 0 dup / ED 1042; `validate_ed_citations` **315 / 190**.)

| PR (commit) | What landed | Register effect |
|---|---|---|
| **#16** (`a08874f`) | v5 itself + the two Lane-B quick-wins (§7). | self. |
| **#17** (`fc2529d`) | **Deprecation sweep + v40 generation executed** — 34 audit folders archived, combat v31/v32 proposals deprecated, `CURRENT.md` declared, new gate `tools/ci_generation_consistency.py`. | **Re-statuses row #42**: the deprecation/currency plan is no longer a *plan* — it **executed**. Residual = wire `canon/supersession_register.yaml` into the fetch set (LB-19/LB-22 tail). |
| **#19** (`0631779`) | **Narrative-state propagation review + deterministic-NLG architecture** (`designs/audit/2026-06-28-narrative-state-articulation/`, ANALYSIS; proposes a future PP-688 §11 realizer — factored condition-gated NLG with an offline LLM bake; no canon edited). | **New row #43** (below) + a new docket key. Ties J-36 / articulation (PP-688). |
| **#20** (`9220954`) | **ED-citation system made trustworthy** — validator precision (scope/ranges/status-vocab/provenance) + grounded ledger flips + triage docs. | **Updates LB-23**: corpus violations **748→315**, open-refs **788→190**. The flip-to-blocking gate is unchanged in *kind* (still `continue-on-error`), now far closer to triage-to-zero. |
| **#21** (`509b167`) | Removed dead damage-scale audit harnesses; `__file__`-relative combat imports; wound-tracker reset preserves spirit/strength. | Housekeeping under personal-combat residual (#17/#35); no new docket. |
| **#22** (`d80d364`) | **Centralized definition naming** — `references/names_index.yaml` + `tools/names.py` + `ci_names_check.py`/`ci_names_consistency.py` + `valoria_rename.py` + `tests/valoria/test_names.py`; CI wires a report-only drift lint + a blocking mirror-consistency gate. | **New LB item (names):** per-entry `warn→block` flips + fold the rest of the proper-noun corpus into the index + retire the registry mirror `name` fields (deferred by the index header itself). |

### Unification of PR #18 (this pass) — LB-22 closed
Reviewed every `origin` session branch (the "open chats"): six were already squash-merged into main (#14–#21); **PR #18** (`claude/github-ci-environment-review`) held the only genuinely-unmerged work — its **net-new** half *was* the LB-22 backlog. Landed it onto main (orchestrator → `deprecated/skills/`; `valoria-vector-audit` read-path rewrite; `ci_hooks_verifier` Check 4 blocking for `skills/`), keeping main's already-merged half (12 skills + coverage_matrix via #16) unchanged. Took #18's importable `ci_register_size_check.py` (no-PyYAML, ships the drift-guard test) and re-added #22's `names_index.yaml` threshold; repointed `lane_assignments.yaml` owns-globs to `deprecated/`. PR #18 closed as superseded. The abandoned `claude/refresh-state-3m7nL` (04-20 pre-migration line carrying the retired session-log/checkpoint harness) was **excluded** from the merge. **`CURRENT.md` "Master workplan" row repointed v4 → v5** (stale-pointer fix).

### New row #43

| # | Finding / decision | Sev | Source | Owner |
|---|---|---|---|---|
| 43 | **Deterministic narration realizer (the PP-688 §11 gap)** — every consequential change is already a Key on a closed, replay-deterministic log (PP-687); PP-688 already specifies significance/triggers/chronicle but **defers the no-runtime-LLM realizer** that turns a Key into on-voice prose (Stage-10 test A3 = DEFERRED). #19 proposes a factored, condition-gated NLG pipeline with an **offline LLM bake** (reuse PP-688 stages as content-selection/planning; the X/Y/Z voice grammar as lexicon; Datalog story-sifting over the Key log for significance/arc detection; a RimWorld-style pacing director for the deferred D11). Architecture-only (no schemas/worked example); `03_…` is a *proposed* PP-688 §11 to lift into `articulation_layer_v30.md` only if ratified. | **design-tier** (P2/P3; no new P1 — extends an existing deferral) | narrative-state-articulation 2026-06-28 (#19) | **new docket key** (below) → ties J-36 + articulation (PP-688) |

### §3 addition — new docket key

| ID | Decision | Unblocks |
|---|---|---|
| **J-37** (new) | **PP-688 §11 deterministic-NLG realizer** — ratify (or amend/decline) the factored condition-gated NLG + offline-bake architecture as the canonical realizer slotting into PP-688; gates the chronicle/articulation completeness path. No structural gate — a Jordan design call (the load-bearing external quotes in `02_…` flagged for a verbatim re-check first). | articulation/chronicle prose (A3); the "one coherent engine" narration surface; complements J-36 (Key-bus closure). |

---
*v5 is the single working master on commit, superseding v4. Every recommendation is Jordan-vetoable; §3 is the veto surface. No ED IDs assigned by this document; staged candidates file via lane blocks (and only after LB-21 re-blocks the exhausted ranges). §10 de-stales the doc to HEAD `d80d364`.*
