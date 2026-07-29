# Adversarial coordination review — Fable read-only critic, 2026-07-29 (ED-IN-0091)

**All 17 findings were reconciled the same day.** The ownership holes are closed by
`02_disposition_map.md` (the authoritative OI→owner table) and the remaining resolutions are folded
into `01_orchestration_plan_v1.md`, `00_open_items_register.md`, the MB plan's §12 and the PC plan's
§15 — at source, not as an appendix. This file is the record of what was found and what was decided.

> **Provenance.** The findings below are **restated by the orchestrator from the critic's register;
> adjudications inline.** The critic's verdict paragraph is reproduced as delivered; each numbered
> finding is a faithful 2–4 line restatement carrying its P-level, its evidence pointer, and the
> adjudicated resolution. Per G12 (a subagent's measurement is a *lead* until the orchestrator
> re-derives it), the two claims that overturned existing register text — F7 and F8 — were re-checked
> against the working tree before being written back as corrections.

---

## Verdict, as delivered

> **Verdict up front:** the zero-collision claim is false on at least five shared files, the "nothing
> dropped" claim is false for ~10 register rows plus ~8 row-halves, and the two loudest cross-plan
> couplings (goldens, the wrapper characterization pin) have no owner on either side. Several
> register rows are also stale against the working tree, so one plan wave would re-implement an
> already-landed fix.

---

## Findings register

### F1 · Coverage holes — rows and row-halves owned by nobody · **[P1]**
**Finding.** OI-15, OI-16, OI-25, OI-34, OI-37, OI-38, OI-39 are owned by no wave; eleven row-halves
are dropped between register and plan — OI-10 (J: placeholder-name rulings absent from the §5
docket), OI-18 (B: contest self-flag not in OI-17's conversion list), OI-19, OI-20 (sim half), OI-31
(B: ED-WR-0003), OI-33 (absent from §5), OI-40 (IN half: the 4-vocabulary reconciliation), OI-41,
OI-43 (B: doc homes for the other 8 `doc:null` modules), OI-48 (B: the ED-SC-0011 bridge owner),
OI-59 (B: hub grounding). The plan's "no routed item exists only as a pointer" is therefore true of
the MB/PC routing and false of the register as a whole.
**Adjudicated.** (a) New `02_disposition_map.md`: every OI-01..OI-59 row, split halves as separate
lines, → exactly one owner, seeded at plan time. OI-15/16 → Wave 4 item 5; OI-25 → a new Wave 3
item 7; OI-18's B half + OI-19 → Wave 1's stub-conversion scope (self-flag only — SC game builds
stay gated on the SC P0 docket); OI-20 sim half, OI-34, OI-37, OI-38, OI-39, OI-41, OI-43's doc
homes, OI-48's ED-SC-0011 bridge and OI-59's hub grounding → a new **§3.5 Deferred-to-lane table**
with lane, rationale, and tracking pointer each. OI-37 explicitly: the SE lane's own highest-priority
item — this program does not pre-empt a lane workstream. (b) §5 gains the missing J rows (fork 12
placeholder names, fork 13 the `bucket:` tag, fork 14 the contest build) plus a completeness clause;
the register's J-count line is corrected. (c) Wave 5's exit becomes "every row **matches**
`02_disposition_map.md`" — a diff against a table seeded at plan time, not a synthesis invented at
capstone time.

### F2 · The wrapper seam pins behaviour while PC deliberately moves it · **[P1]**
**Finding.** The IN plan pins wrapper *behaviour* with a characterization test while PC batches
E1b/E2a/E2b/E3a/E3b change roster-wide damage on purpose. Once Wave 1's bridge routes combat through
the wrapper, PC's changes move IN-owned campaign goldens (`engine/tests/test_f7_smoke_oracle.py`
pins `scenes_resolved`) and no session is designated to re-record them.
**Adjudicated.** The characterization test is **shape/contract-level only** — result schema,
determinism under a fixed seed, presence of the fields the bridge consumes — never outcome or
balance values. The bridge ships **flag-OFF** behind `DISPATCH_COMBAT_BRIDGE` with byte-identical
goldens; the flip to ON happens only after PC's E0–E3 have merged, as one deliberate IN-owned golden
re-record citing both plans, and the reach-oracle combat rows assert under the flag and xfail while
it is off. PC §15's seam declaration now states that `engine/tests` campaign goldens join PC's
blast-radius disclosure only once the flag is ON.

### F3 · G11 "one golden-moving PR globally" vs three concurrent golden-movers · **[P1]**
**Finding.** The MB plan's G11 reserves a single global golden-moving slot, but three sessions each
own golden families that move independently — MB digests, PC reference tables, IN campaign goldens.
Read globally, G11 serializes the whole program on one lane.
**Adjudicated.** Define **golden families with one owner each** in all three documents: MB digests
and `bat.py` batteries → MB; `combat_armour_reference.json` and the PC reference tables → PC;
`engine/tests` campaign goldens (F7, pipeline-reach) → IN. G11 is restated **per family** — one
golden-moving PR in flight *per family* — and any change crossing families requires a coordination
note in root `HANDOFF.md` before the PR opens. The MB plan's own G11 text remains authoritative
**inside** the MB family; the restatement scopes it, it does not overrule it.

### F4 · `review_baseline.yaml` three-way collision on a Jordan-gated file · **[P2]**
**Finding.** Wave 1 seeds a `stubs.count` baseline, MB's I1 conversion later moves that count, and
Wave 4's vocab work can move `vocab.a17` — on a file CODEOWNERS-gated to Jordan, where a raise
requires an explicit ED.
**Adjudicated.** Wave 1 seeds `stubs.count` at the **full expected converted set including
`altonian_reinforcements`**, so MB's later conversion can only move the count in the improving
direction and trips nothing. Wave 4 pre-declares the `vocab.a17` protocol: if the un-blinded scan
surfaces new debt the wave **stops**, records the measured delta, and files the baseline raise as an
explicit ED — never a silent edit. Among the three sessions, **only IN edits
`registers/review_baseline.yaml`**.

### F5 · `id_reservations.yaml` corruption risk under concurrent sessions · **[P2]**
**Finding.** All three plans allocate `ED-<LANE>-NNNN` "at execution time" from one file that is a
single YAML mapping with hand-maintained comment provenance — three live sessions editing it mid-run
is exactly the collision class §3 already documents, on the one file that has no merge-friendly
structure.
**Adjudicated.** Wave 0 gains a pre-flight item: **pre-allocate each session's ED block in ONE
commit before the three sessions start** (the IN block from the IN lane; a small MB and a small PC
block recorded in the file's comment per its own allocation protocol), so no session touches
`id_reservations.yaml` mid-run. One-line mirrors in MB §12 and PC §15.

### F6 · `module_contracts.yaml` + regenerated observability artifacts, two writers · **[P2]**
**Finding.** MB's E1 instructs "regenerate the observability artifacts" while IN's Wave 5 re-runs the
whole observatory; both edit `module_contracts.yaml`. Two sessions regenerating the same generated
artifacts produce a merge that silently picks one.
**Adjudicated.** **IN is the sole regenerator** of `graph.json` / incompleteness / the PROPOSALS
family, at Wave 5. MB's E1 edits **sources only** (the `module_contracts` row + the `build_graph.py`
alias) and defers artifact regeneration to IN's Wave-5 observatory pass — this scopes E1's own
regeneration instruction, it does not cancel the ED-1094 ratification. Wave 3's exit is restated:
dangling-emit count 4 → ≤1, **or ≤2 while ED-MB-0010's row has not yet merged**, that row being
excluded from the wave's denominator. Contract-file convention: MB owns rows `:465-486` and its E1
deletion, IN owns the rest; the hunks are distant and git-mergeable; each PR touches only its own
rows.

### F7 · OI-53 is partially STALE — a wave would re-implement a landed fix · **[P2]**
**Finding.** `ci_quantity_vocabulary_check` already routes through `ci_common.sim_reference_roots()`
(ED-IN-0087) **and** already has a recurrence guard; `build_apparatus_registry` is fixed; the
`mechanics_index` `sim_module:` paths verify live. Genuinely remaining: `audit_staleness.py:69`,
`build_decisions.py:57`, `workplan_status.py:71`.
**Adjudicated.** The register's OI-53 row is corrected in place and marked `[corrected 2026-07-29
critic pass]`, listing what is already fixed and the three remaining sites plus F14's addition.
Wave 4 item 3 is rewritten to **re-verify each site at execution**, route every fix through the
**existing** single owner `ci_common.sim_reference_roots()` and **extend the existing guard test** —
never ship a second owner or a second guard (§8's "every rule lives once").

### F8 · MB §12 I3's premise is false · **[P2]**
**Finding.** `tests/sim/mass_battle/test_persubunit_stress.py:17` resolves to `<repo>/tests/sim`,
which is **live**, not the retired `<repo>/sim`. Lines 17-19 insert the same live path twice; it is a
redundant duplicate `sys.path` insert, not an F4-class retired-root reference.
**Adjudicated.** MB §12 I3 is rewritten with the `[corrected 2026-07-29 critic pass]` marker and the
disposition downgraded to "optionally remove the redundant duplicate insert, zero behavioral stakes".
The corresponding clause in the register's OI-53 row is corrected the same way.

### F9 · IN's acceptance criterion is hostage to an unscheduled MB item · **[P2]**
**Finding.** §1's "zero unconditional `NotImplementedError` in live trees" cannot be satisfied by the
IN session: `systems/mass_battle/sim/altonian_reinforcements.py` is MB-owned and MB §12 I1 carries no
slot, so IN's own exit criterion depends on another session's unscheduled work.
**Adjudicated.** The criterion becomes "zero unconditional `NotImplementedError` in live trees,
**except files under an accepted cross-session handoff**, each cited in the reach oracle's xfail
manifest (currently exactly one: `altonian_reinforcements.py` → MB plan §12 I1)". MB §12 I1 gains a
suggested slot: with the first E-track editorial batch — it needs no golden slot and is independent
of A/B/D and of fork #1.

### F10 · The inbound sections exist only on this branch · **[P2]**
**Finding.** MB §12 and PC §15 land in this PR. A session that branches from `main` before it merges
reads a plan with no inbound section at all, and the start order of the three sessions is nowhere
declared.
**Adjudicated.** Both inbound sections open with a line stating they landed via **PR #252** — the IN
program's PR — and that a `main` checkout lacking the section means that PR has not merged, so the
inbound items must not start yet. The IN plan's lane-partition block gains an explicit **ORDERING**
line: PR #252 merges *before* the MB/PC sessions branch from `main`; the three-session concurrency
begins after that merge.

### F11 · PC I4 hangs off an optional audit · **[P2]**
**Finding.** The `_emit()`→Key mapping (OI-26) is routed as a rider on PC §12's wrapper audit, which
§12 itself frames as "if a session has budget for one more independent read-only audit". The IN side
consumes that mapping, so a conditional deliverable gates a scheduled one.
**Adjudicated.** PC §15 I4 is promoted to a **scheduled inbound batch, not conditional**: run the
§12 wrapper read-only audit and produce the `_emit()`→Key mapping table as its deliverable, in serial
position after E3 and before any E4+ ⚖ work. §12's "if budget" framing is superseded **for this item**
by the 2026-07-29 routing directive.

### F12 · IN writes into live lanes' handoffs · **[P2]**
**Finding.** Wave 0's exit files the docket into "lane handoffs" and Wave 5 item 5 updates them —
including `HANDOFF_MB.md` and `HANDOFF_PC.md` while those sessions are running and (per the MB plan's
own §10) their orchestrators own those files.
**Adjudicated.** IN writes **only** `HANDOFF_IN.md` and root `HANDOFF.md` (genuinely cross-cutting
items), never a carved-out lane's handoff while its session is live. Cross-lane items are filed as
lines in the §5 docket / the disposition map and flagged in the PR body for the lane session to
ingest.

### F13 · `CURRENT.md` contention · **[P2]**
**Finding.** MB's E4 flips subsystem `## Status:` lines while IN's Wave 5 runs a `CURRENT.md` stamp
reconcile, and `currency.stamps` has baseline 0 — so any drift regresses the ratchet regardless of
which session caused it.
**Adjudicated.** MB §12 gains a coordination bullet: E4 edits **only MB's own subsystem rows/status
lines** and says so in its PR body. IN's Wave-5 stamp reconcile runs **last** among the three
sessions' merges it can see, and touches only the stamp and IN-owned rows.

### F14 · A fourth retired-tree scanner · **[P3]**
**Finding.** `tools/ci_audit_registry_check.py:23` still scans the retired `designs/audit/`
(`AUDIT_DIR = os.path.join('designs', 'audit')`) — the same pattern-defect class as OI-53, missed by
the register.
**Adjudicated.** Added to the register's OI-53 row as the critic's own addition, and to Wave 4 item
3's sweep list **and the guard's scan set** — the guard is the fix, the sweep is only the cleanup.

### F15 · Wave 2 item 7 silently drops four OI-12 members · **[P3]**
**Finding.** Item 7 reads "`npc_ai`, `companion`, `rs_track`/`ip_track`, threadwork/world orphan
sims", which omits `systems.settlements.sim.{settlement,temperaments}`,
`systems.social_contest.sim.parliamentary_stay` and `engine.autoload.registry` — four of OI-12's
twelve members.
**Adjudicated.** Item 7 now says **the full OI-12 list** and enumerates it: `npc_ai`, `companion`,
`rs_track`/`ip_track`, threadwork `co_movement`/`collective`/`opposing`/`rendering`, world
`miraculous_event`/`restoration_movement`, settlements `settlement`/`temperaments`, social_contest
`parliamentary_stay`, `engine.autoload.registry`.

### F16 · PC I4's mapping table has no home · **[P3]**
**Finding.** The `_emit()`→Key mapping is described as "the contract between the two sessions" but no
file path is given, so either session could reasonably write it into
`systems/_architecture/key_type_registry_v30.md` — an IN-owned file.
**Adjudicated.** The table lives in the PC audit folder
(`audit/2026-07-26-combat-balance-customization-state/`, e.g. `wrapper_emit_key_map.md`). Any edit to
`systems/_architecture/key_type_registry_v30.md` stays **IN-owned** (Wave 3) and *consumes* PC's
table.

### F17 · A fork-1 "promote" ruling would invalidate the reach oracle and orphan an FA seam · **[P3]**
**Finding.** If Jordan rules "promote" on MB fork 1, the campaign's battle resolution moves trees:
the IN reach oracle's MB rows are pinned against the currently-wired tree and would become false, and
the `faction_action.py:349` call site — an **FA**-lane file, owned by neither the MB nor the IN
session — is the seam that would have to move.
**Adjudicated.** A **re-entry protocol** is recorded in IN §5 row 1 and in MB §12's seam declaration:
a fork-1 "promote" ruling spawns an **FA-lane wiring item** (the seam is FA-owned); the IN
reach-oracle's MB rows flip to stub-flag the moment the ruling lands and stay there until the FA item
re-pins them.

---

## Checked and cleared

Reconstructed from the adjudication record rather than quoted — the critic examined these and did not
file against them, and each was re-derived by the orchestrator before being recorded as clear:

- **The MB/PC *code*-file partition holds.** No wave in `01_…` touches `systems/mass_battle/`,
  `tests/sim/mass_battle/`, `systems/combat/`, or `faction_action.py:349`. The zero-collision claim
  fails on *shared registry and generated* files (F4/F5/F6/F13), not on the code lanes.
- **The physical-routing claim holds for MB/PC.** Every register row marked "→ MB plan" / "→ PC plan"
  resolves to a real track or to an appended §12/§15 item; no MB- or PC-routed item exists only as a
  pointer. (The failure is elsewhere — F1's *unrouted* rows.)
- **Wave ordering is sound.** Spine-before-seams (W1 → W2), the oracle built first and driven green
  wave by wave, and W5 last are not disputed; the oracle-as-falsifier construction is the plan's
  strongest feature.
- **The stubwire primitive is a genuine single owner.** Derived flag (import-based), no standalone
  registry file, three independent observers (audit attribute, telemetry, ratchet) with a stated
  mutation check — consistent with §8 and §0.1 point 5.
- **The register's own `[verified]`/`[corrected]` spot-check tags reproduce.** The three 2026-07-29
  corrections (`mc_v18`'s silent except FIXED, `handoff_rules`'s import-orphan claim standing, the
  dispatch branch routing to the deprecated resolver) each re-derive against the working tree.
- **`engine/tests/test_f7_smoke_oracle.py` pins what F2 says it pins** — `scenes_resolved` against
  `GOLDEN_SCENES_RESOLVED`, with `npcs_generated == 0` self-documenting the OI-05 flip.
- **The §5 docket's existing 11 rows are correctly held** — none of them is a routine-work item
  bundled into a merge-ratifying PR, and each names its blocker. The defect was omission (F1b), not
  mis-classification.

*Companions: `00_open_items_register.md` · `01_orchestration_plan_v1.md` · `02_disposition_map.md`.*

---

## Appendix — the critic's register, verbatim

*(Preserved unedited by the orchestrator, which held the original text; the restatements above
carry the adjudications, this appendix carries the source. Two working-tree claims in it — F7's
"already fixed" set and F8's live-path reading — were independently re-derived by the orchestrator
before the corrections were written back, per G12.)*

**Verdict up front:** the zero-collision claim is false on at least five shared files, the "nothing dropped" claim is false for ~10 register rows plus ~8 row-halves, and the two loudest cross-plan couplings (goldens, the wrapper characterization pin) have no owner on either side. Several register rows are also stale against the working tree, so one plan wave would re-implement an already-landed fix.

**1. [P1]** ~10 register rows and ~8 row-halves are owned by no plan, no §5 fork, and no D ruling — "union accomplishes ALL work" is false. Never mentioned by any wave, §5 row, or MB/PC routing: OI-15, OI-16, OI-25, OI-34, OI-37 (which the register itself calls the SE lane's "single highest-priority open item"), OI-38, OI-39. Half-dropped: OI-10's J half, OI-18's B half, OI-19, OI-20's sim half, OI-31's B half, OI-33 (a J row entirely missing from the §5 docket, contradicting the register's own "12 J listed loudly" claim), OI-40's IN half, OI-41, OI-43's B half, OI-48's B half, OI-59's B half. Wave 5's exit gate would force the capstone to invent dispositions for rows no wave executed and no ruling deferred.

**2. [P1]** The wrapper seam declaration pins *behavior* on one side and promises only *API stability* on the other — every PC behavioral batch breaks IN's characterization test, and once the Wave-1 bridge is live every PC batch also moves IN-owned campaign goldens (`test_f7_smoke_oracle.py:125` pins `scenes_resolved` on seed-42); a CI surface the PC plan's blast-radius sections never mention. No designated re-recorder.

**3. [P1]** MB's G11 — "One golden-moving PR in flight, **globally**, ever" (`03_execution_plan.md:90,:479`) — is violated by the concurrency design itself: concurrent golden-movers MB A1a/A2/B1a, IN Wave-2's F7 re-record, PC E1b–E3b regens. Neither other plan cites G11; no arbitration mechanism exists.

**4. [P2]** `registers/review_baseline.yaml` is a three-way collision on a CODEOWNERS-Jordan-gated file: IN's stubs.count ratchet; MB's I1 conversion later changing the count; IN Wave-4's OI-53 fix possibly moving `vocab.a17` (baseline 29) upward — a baseline raise = Jordan sign-off mid-wave.

**5. [P2]** `references/id_reservations.yaml` is edited by all three sessions and has a documented history of silent corruption under exactly this pattern (the 2026-07-05 last-key-wins regression recorded in the file itself). "Reconcile on merge as documented precedent" understates the risk — the precedent includes cross-lane silent regression.

**6. [P2]** "Zero file overlap" is literally false: MB E1 edits `references/module_contracts.yaml:473` + `tools/observability/build_graph.py:73` and regenerates the same whole-file observability artifacts IN Wave-5 regenerates; IN Wave-3 edits the same YAML (distant hunks — git-mergeable, but the regenerated JSON/JS artifacts are whole-file rewrites). Wave 3's exit "dangling-emit count 4 → ≤1" silently requires MB E1 to have merged first.

**7. [P2]** OI-53 is partially STALE: `ci_quantity_vocabulary_check.py:170` now defaults through `ci_common.sim_reference_roots()` (single owner, ED-IN-0087, guard already existing at `tests/valoria/test_sim_reference_roots.py`); `build_apparatus_registry.py` fixed; all `mechanics_index.yaml` `sim_module:` values verified live. Still stale: `audit_staleness.py:69`, `build_decisions.py:57`, `workplan_status.py:71`. Wave 4 would re-implement an existing owner + guard (a §8 violation).

**8. [P2]** MB §12 I3's premise is FALSE — `test_persubunit_stress.py:17` computes `<repo>/tests` + `/sim` → `<repo>/tests/sim`, a live directory; line 19 adds the same path again. A redundant duplicate insert, not a retired-root reference. A session "fixing the retired root" per the description could delete the wrong insert.

**9. [P2]** IN's own P1 acceptance ("zero unconditional `NotImplementedError` in live trees") is hostage to MB's I1, which has no slot in MB §9's order — IN Wave-1/Wave-5 would report red on a criterion it is forbidden to fix.

**10. [P2]** The routing appendices exist only on the uncommitted IN branch; PC §1's bootstrap checks out `origin/main`. Three sessions launched simultaneously would have MB/PC never see I1–I4. "A dedicated session reading only its own plan misses nothing" is true only after this PR merges.

**11. [P2]** OI-26's "contract between the two sessions" hangs off an *optional, unscheduled* PC activity — PC I4 fires only "when the §12 wrapper pass runs," and §12 is itself conditional ("**if** a session has budget"). No PC batch owns it; it executes never.

**12. [P2]** IN Wave-0/Wave-5 write into `HANDOFF_MB.md`/`HANDOFF_PC.md` while the dedicated sessions are writing them — the merge-collision class the 2026-07-02 handoff split existed to kill (MB reserves handoff writes to *its* orchestrator; PC's handoff cap was blown four times already).

**13. [P2]** `CURRENT.md`: MB E4's CANONICAL flips and IN Wave-5's stamp reconcile both touch it, with `currency.stamps` at baseline 0 and no convention on who edits which rows or in what order.

**14. [P3]** A live-tool retired-root site the register's own sweep missed: `tools/ci_audit_registry_check.py:23` still scans `designs/audit/` (retired 2026-07-19) — the report-only freshness signal is permanently silent, including for the three audit folders these plans write into.

**15. [P3]** Wave 2 item 7's named list drops four of OI-12's members (`settlements.sim.{settlement,temperaments}`, `social_contest.sim.parliamentary_stay`, `engine.autoload.registry`) — an executing agent following the named list will skip them.

**16. [P3]** The `key_type_registry_v30.md` deliverable location for PC I4 is unspecified — if PC writes the mapping into the registry doc, a fourth shared file appears.

**17. [P3]** MB fork #1's "promote" outcome invalidates IN's reach-oracle MB rows and forces a change at the byte-untouched seam (`faction_action.py:349` — FA-lane, owned by *neither* session), with no re-entry protocol.

**Checked and cleared** (verified non-problems): lane-split editorial ledgers (collision-free by construction; `id_reservations.yaml` is the residual risk); `engine/engine_params/combat_engine_v1.json` (PC-only); `references/descriptor_registry.yaml` (IN Wave-3 only); `engine/substrate/keys.py` (IN-only — the MB dev tree imports nothing from `engine/`, PC never touches it); the `scene.combat_resolved` emitter already exists IN-side (`engine/cross_scale/echo_transport.py:67`), so Wave-3's "≥1 consumed" falsifier does not hidden-depend on PC's `_emit()` mapping; the `test_build_proposals.py` proposals-count pin (no plan adds `proposals/` docs); `workplans/workplan_v6_progress.yaml` (no plan edits it); OI-53's remaining members verified still stale; PC §13 guardrails vs IN (consistent — Fable on review only, `hCritic` usage); MB fork discipline vs IN §5 (correctly deferred); `module_contracts.yaml` hunk-level collision risk low (distant regions).
