# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## Lane-tagged handoffs (2026-07-02)

- **Social-contest staged rebuild (`claude/happy-shaw-da0f1d`, IN PROGRESS).** Agonist/antagonist gated rebuild
  of the contest engine: promote the stranded 62-test groundup engine (`designs/audit/2026-06-03-contest-groundup/`,
  actually **9 modules / 151 tests green**) onto the v30 surface + fold in CR1–CR7, build all four deliberative
  games (Agôn/Negotiation/Inquiry/Consensus), close J-36 seams, drive to settled canon (T-25 + sim-validation).
  Plan: `C:\Users\Jordan\.claude\plans\this-is-a-broader-nested-mountain.md`. Runs stage-by-stage via the Workflow
  tool (Opus agonist/antagonist/judge + Haiku scribe), Jordan ratifies each gate; cadence = auto-advance, interrupt
  only for design-authority forks.
  - **Stage 0 (Foundation) DONE + Gate 0 RATIFIED (2026-06-30).** Reconciliation contract + decisions:
    `designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md` (+ raw map + gate packet). Three ratified
    forks: **D0-1** appeal ethos/pathos/logos = build both multiplicative+additive behind a flag, decide by seeded
    A/B (player-win-rate vs venue-identity-spread); **D0-2** σ-leverage → new numpy-free `sim/autoload/sigma_leverage.py`
    sibling (retires the test-dir/numpy/sys.path-hack + the two-σ-kernels debt); **D0-3** TN6/7/8 divergence + Jordan's
    fractional-Ob idea → contest stays δσ TN7 (unaffected), open a substrate probe (reopens CR6 uniformity), non-blocking.
    Good news: `faction.py` already has BG-Vote/Succession/committee-band → Consensus mostly promote-existing.
    IDs reserved: `contest_rebuild` = ED 1055-1079 / PP 800-809.
  - **Stage 1a DONE + committed (d64e2ffe).** `sim/autoload/sigma_leverage.py` — numpy-free σ sibling, byte-identical
    to the oracle, 623 tests green; two-σ-kernels debt retired.
  - **Stage 1b DONE + committed.** 9-module kernel promoted to `sim/personal/contest/`, rewired onto the σ sibling
    (no third kernel); `degree` = clean carry-across (pool-aware integer degree added to sigma_leverage, distinct from
    `dice_engine.Degree` combat enum); old stub → `contest_legacy_stub.py`; 815 sim tests + both importers green.
  - **D0-3 RESOLVED → HYBRID** (present-as-Ob display over the δσ substrate; CR6 upheld, not reopened). Memo:
    `designs/audit/2026-06-30-contest-fractional-ob-probe/MEMO.md`; decision → ED-1055. Probe also surfaced a LIVE
    combat bug (`dice_engine.roll_pool` ignores `tn`; TN5/6/8 weapons rolled at TN7 rate) → spun out as a
    combat-lane task (`task_210994b7`, out of contest scope).
  - **Stage 1c DONE + merged into main (PR #44, all CI green).** v30 re-skin (8 proceedings, Persuasion Track
    banding, 4 adjudicator types) + `build_contest`/`resolve_contest` wrapper + MECHANICS registry, mirroring
    `tests/sim/mass_battle/engine.py`. 888 tests green.
  - **Stage 1d / Gate A DONE — 3 forks ratified by Jordan (2026-07-01).** Propagated CR1 (wrapper, confirmed
    already-realized)/CR2 (σ-substrate, confirmed already-realized)/CR3 (three trackers: Concentration+Face+
    Persuasion, Composure retired — contest-scope only) into prose (`social_contest_v30.md` §4/§8 + co-files,
    `params/contest.md`) + code (`sim/personal/contest/` Face primitive) + ledger (ED-1055, ED-1056). Packet:
    `designs/audit/2026-07-01-contest-gate-a-packet/GATE_A_packet.md`. **Ratified:** (1) Face scale-binding =
    combo formula, not a straight rescale — `Face_max = Charisma×3` (ceiling, player-build-controlled) +
    `Face_current = round(Standing/10 × Face_max)` (position within ceiling, earned through play, Standing's
    kernel math/Readiness/leak feed untouched); (2) Composure retirement scoped to the contest tracker only
    (knots/combat/conviction untouched, confirmed); (3) provisional EDs use non-basis citation phrasing until
    ratified (standing policy). A small Sonnet-tier finalize pass is applying the resolved formula + 4 agreed
    nits (dead imports, ED-1056 recitation, prose wording, TRACKERS sourcing); that pass also caught the ratified
    Face formula shipped with zero test coverage and added 10 targeted kernel checks (boundary cases, midpoint
    round-half-to-even, non-mutation, live-tracking). **Committed (884cf89a).** 1041 sim+valoria + 244 kernel
    checks green. Push to `claude/happy-shaw-da0f1d` updates the open tracking PR ([ttrpg#44]) — Jordan merges,
    not this session.
  - **NEW standing requirement (decision 5, 2026-07-01): the player-interaction model is a concrete deliverable,
    not a late audit.** First-draft walkthrough seeded ahead of Stage 6 so every later stage designs toward it:
    `designs/audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md` — setup screen,
    the exchange loop (Appraise / style-choice cards / roll-and-resolve / Face+Concentration bars), the
    resolution screen, and how Negotiation/Inquiry/Consensus should each look different from Agôn's track meter
    so Stage 4 doesn't converge them onto one UI. Stage 2 now owns authoring the Style/Venue flavor text; Stage 3
    now owns the Appraise-reveal boundary for `armature_position`; Stage 4 now owns each game's interaction
    shape; Stage 6 finalizes+ratifies the model this seeds. Plan file amended accordingly.
  - **Gate A committed (`884cf89a` mechanics + `98ecdf41` player-model), PR #44 all-green.**
  - **Stage 2 / Gate B (dictionaries) DONE + committed.** Built Venue×8 / Adjudicator×4 / Style×4 /
    InteractionType×4 typed dicts (`sim/personal/contest/dictionaries.py`, new module) + Style/Venue
    flavor text; closed ED-137 (Panel adjudicator). Packet:
    `designs/audit/2026-07-01-contest-gate-b-packet/` (pre-ratification snapshot + the authoritative
    `GATE_B_closeout_audit.md`). **Ratified and independently re-verified in actual code (not just ledger
    text):** Panel votes weighted-by-standing (ED-1057; reuses the existing `Adjudicator.discipline` field,
    NOT the contestant `Standing` name — no new state invented); Panel reachability = rebind Guild
    Arbitration's adjudicator → Panel (ED-1059; NO appeals — "let the decision ride"; roster stays 8);
    Terminal Doubt = terminal-value-everywhere, banded (PersuasionTrack) + tally (TallyAtClose) branches
    both specified (ED-1060); Guilds "GM picks" boost = context-derived from the venue's dominant
    ethos/pathos/logos via the existing `Appeal` machinery (ED-1061; literal "GM picks" text removed from
    both prose heads). ED-1055/1056/1058 flipped to `status: ratified` (a bookkeeping fix — they were left
    `provisional` only because two earlier finalize-workflow attempts were killed by infrastructure
    issues — API 401/529 errors and a background-task stop, unrelated to the work itself — before
    flipping their own metadata; the ratifications themselves happened earlier via Jordan's answers).
    1041 sim+valoria + 319 kernel tests green; freshness gate clean (5/5 fresh); no scope drift (grep
    confirmed knots/combat/conviction untouched, Composure retirement still contest-scoped).
  - **SOURCE-RESEARCH GROUNDING (found 2026-07-01 via files13.zip → already in repo, NOT orphaned).** The
    deliberation-critique source research
    `designs/audit/2026-06-28-social-contest-deliberation-critique/source-research/` (a 3-part
    Renaissance-deliberation / machination-games-lens / model-testing trilogy) is READ-AND-CITED-BUT-NOT-APPLIED:
    it shaped the plan's four-games / alea / consensus / commitment-store / armature *shape* via `critique.md`,
    but its rich detail (Dowlen small-pool weighted lottery; `liberum veto` as self-undermining equilibrium;
    Padgett robust action; Putnam two-level bargaining) is not yet in the code. Plan amended: Stage 3 (armature)
    and Stage 4 (four games) agonists must now READ the source-research trilogy directly, not just the critique
    distillation, so this commissioned scholarship actually reaches the implementation.
  - **Stage 3 / Gate C DONE + committed (54d04250).** CR4 (Ciceronian 6-rung stasis ladder now drives the
    genre +1D; the reachability gap — every proceeding opened Quality-default, so the conjectural/Memory
    stasis was unreachable in all 8 — fixed by opening Church Tribunal at Fact) and CR5 (a failed Obscuring
    move now strips the mover's own Face, standing-bounded, kept together with the Gate-B Doubt Marker as
    the full realization) are now mechanical, not nominal. New adjudicator **armature**: a continuous
    4-axis (Evidence/Consequence/Authority/Insinuation) Style×Conviction dot-product entering resolution
    as a δσ leverage shift (not a rounded pool die), gated off in asymmetric proceedings, revealed only
    PARTIALLY via Appraise (grounded in Greif/Padgett from the source-research trilogy — the style choice
    stays a bet, not a solved lookup). New modules: `sim/personal/contest/{armature,rhetoric,appraise}.py`.
    Four Jordan-ratified decisions filed directly as ED-1062 (armature keeps Insinuation as a deliberate
    new 4th axis, not canon's Solidarity; 2-genre epideictic compression accepted as-is; CR5 keeps both
    halves together; reachability fixed via Church Tribunal only). The finalize pass crashed on a session
    limit mid-flight but its tool-call side effects (the reachability fix, full canon propagation, ED-1062)
    persisted; a follow-up Sonnet-tier verification pass (the first antagonist check that actually ran)
    caught and fixed one real minor defect (stale provisional language in one field of `CR5_SELF_GATING`).
    1041 sim+valoria + 385 kernel tests green; freshness gate clean.
  - **Reconciled with `main` post-Gate-C (`715c5c3e`).** `main` had advanced substantially (mass-battle LC-8,
    a month-overview architecture consolidation, ~10 new EDs) while Gate C was in flight. Two real conflicts:
    `canon/editorial_ledger.jsonl` (both sides appended new entries — kept both, ascending ED order) and
    `references/canonical_sources.yaml` (both sides had independently run a full `freshness_gate.py --update`
    regeneration, so the whole file conflicted at the line level even though the content barely differed —
    resolved by regenerating fresh from the merged working tree rather than hand-patching). The merge also
    tripped `ci_register_size_check.py`: the combined ledger hit 150,949 tokens (cap 150,000). Fixed properly,
    not bypassed — split the ledger for the first time: archived the 216 oldest resolved/struck/superseded/
    applied entries (ED-001..ED-330) to new `canon/editorial_ledger_archive.jsonl` (live ledger now ~130k
    tokens, ~20k headroom), registered its own cap in `ci_register_size_check.py`, and extended
    `tools/validate_ed_citations.py` (`ARCHIVE_JSONL_PATHS`) to scan `.jsonl` archives — its existing
    `ARCHIVE_GLOBS` scanner only recognized the older pre-2026-05-28 YAML archive convention, so without this
    fix any doc citing one of the 216 archived EDs would have started reading as a broken citation. Verified:
    `validate_ed_citations.py` → 818 ids loaded, 0 citation-integrity violations; 1054 sim+valoria tests + 1
    skipped, unaffected. PR #63 open, CI running.
  - **NEXT: Stage 4** (the four deliberative games — Agôn/Negotiation/Inquiry/Consensus — parallel fan-out,
    reading the source-research trilogy directly per the Stage-3 grounding pattern: the `liberum veto` as a
    self-undermining equilibrium for Consensus's frivolous-block antibody, Dowlen's weighted lottery for
    `WeightedLot`/alea, Putnam two-level bargaining for Negotiation's ZOPA).
Per-lane continuity now lives in `handoffs/HANDOFF_<LANE>.md`, using the same 9 lane codes as
the `ED-<LANE>-NNNN` editorial namespace (`ED-IN-0001`, `CLAUDE.md` §3). This file is the
**index** plus genuinely cross-cutting items — read the lane file(s) relevant to your session
before starting work, and keep your own updates scoped to your lane's file (or this one, only
for cross-cutting items).

| Lane | Subsystem | File |
|---|---|---|
| `MB` | Mass battle | `handoffs/HANDOFF_MB.md` |
| `PC` | Personal / scene combat | `handoffs/HANDOFF_PC.md` |
| `FI` | Field investigation | `handoffs/HANDOFF_FI.md` |
| `SC` | Social contest | `handoffs/HANDOFF_SC.md` |
| `FA` | Faction actions | `handoffs/HANDOFF_FA.md` |
| `WR` | World | `handoffs/HANDOFF_WR.md` |
| `IN` | Infrastructure / cross-cutting | `handoffs/HANDOFF_IN.md` |
| `GO` | Godot conversion | `handoffs/HANDOFF_GO.md` |
| `SE` | Settlements | `handoffs/HANDOFF_SE.md` |

**Why the split:** the ID-collision incidents that motivated `ED-<LANE>-NNNN` (two same-session
concurrent-allocation collisions on the flat sequence within one PR — see `ED-1094`'s ledger
entry) are the same failure class that makes one shared `HANDOFF.md` a merge-collision magnet
once multiple lane-sessions run concurrently. This is a **partial, deliberate exception** to the
repo's earlier "one continuity surface" consolidation (`deprecated/session_machinery/` retired
per-topic session-log files because they rotted independently) — the difference is this split is
keyed to the SAME lane taxonomy the ID system already enforces, not an ad-hoc per-topic split,
and this root file remains the one stable SessionStart entry point.

**Note on `designs/audit/2026-06-30-open-items-adjudication-docket.md`:** that file (PR #68,
filed concurrently by a different session while this session was independently adjudicating the
same five items from a pasted copy) is now **ADJUDICATED, not still pending** — see its own
updated status header. Verdicts: D1/D5 resolved and struck, D2/D3 still open with materially
changed context, D4 partially done and narrowed. Detail lives in `handoffs/HANDOFF_PC.md` (D1),
`handoffs/HANDOFF_IN.md` (D2/D3/D4/D5), and `decision_queue.md` items 5/12/24/25 — not repeated
here.

**Full detail on the split itself, and every historical decision predating it, is filed at
`handoffs/HANDOFF_IN.md`'s Decisions log** — this root file does not duplicate that history.

## Next actions

_(Reserved-ID state healthy as of 2026-07-01: **LB-21 executed** — `id_reservations.yaml` v3
verified live max, allocated ED 1081–1087 to the month-overview consolidation from
block D, and pre-provisioned disjoint Round-3 block E (ED 1100–1149 / PP 830–849). Allocate
per the file's protocol; never max+1.)_

- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec now
  RATIFIED (2026-07-02).** The month's comprehensive review, the consolidation
  execution/reconciliation logs, and the **single consolidated 23-item Jordan decision queue**
  live at `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see
  `decision_queue.md` first — every gated item below is indexed there). **Doctrine ratification**
  (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`) and **J-38 propagation-spec
  authorship** (ED-1093, `designs/architecture/propagation_spec_v1.md` — supplies `engine_clock`'s
  candidate home doc; the `doc:null`/[ASSUMPTION] grade stays unflipped until ED-1051 is
  separately resolved) are both **CANONICAL** as of PR #58 (ED-1094 merge-ratifies-by-default).
  The propagation spec's own §5 carries its ranked open items (OF-7/OF-B1 amendments, D.6/OF-D6
  double-count, `decay()` spec, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) — ratification
  did not resolve these, only fixed the spec's home-doc status. Remaining highest-leverage queued
  decisions: Track-2 residuals (below), field-ON, the values_master regenerate-vs-retire call,
  the duplicate compilation homes, and item 19 (Agent-Teams/subagent-roster adoption).
- **Mass battle — Stages A–D + LC-8 landed on `main` (2026-06-30 → 2026-07-02, PRs #45/#52/#56/#57/#59);
  this file previously had zero record of any of it — closing that continuity gap now.** Coordinate-field
  true-adjacency contact (Stage A), facing/attention/reaction physics (Stage B), the command layer
  (`build_army`/timed `Order`s/escort — Stage C), and role/doctrine wiring + `build_envelopment`/
  `build_refused_flank` Unit-level presets (Stage D, ED-907/908/909) are all merged. **LC-8 executed
  2026-07-02 (ED-1088):** `Horseshoe`/`RefusedFlank` retired as `Subunit.shape` values per Jordan's
  go-ahead ("those are emergent outcomes") — only Line/Arrowhead/GappedLine/Column remain valid
  subunit shapes; envelopment/refused-flank exist only as the Unit-level presets above.
  `bat.py`'s grid-mode golden digests were deliberately re-baselined (approved behavior change).
  The workbench (`tests/sim/mass_battle/workbench/`) was extended to visualize the new multi-subunit
  presets — see `tests/coverage_matrix.md`'s 2026-07-02 entries for what shipped and two real bugs
  found/fixed along the way (a `reset_positions` multi-subunit collapse bug; a frontend preset-dispatch
  bug). **Governing plan:** `designs/audit/2026-06-30-massbattle-bottomup/05_redesign_workplan.md` +
  the session's own staged plan (Stages A–F, not yet promoted into the repo — ask the session for
  `using-opus-4-8-ultracode-floating-tiger.md` if resuming this thread). **Three Jordan rulings landed
  2026-07-02 (all executed same day):** (1) **ED-1089** — `FIELD_MOVEMENT=1`/`PC_NODE_COHESION=1` are
  now the DEFAULTS (Stage A step 7 executed; "yes, field movement is default."); the grid stays the
  byte-exact oracle via explicit `FIELD_MOVEMENT=0 PC_NODE_COHESION=0` pins (the CI gate was updated
  from env.pop to explicit '0' pins — load-bearing, see test_mass_battle_byte_exact.py), and bat.py's
  field digests were re-recorded (they had gone stale vs the LC-8 battery). (2) **ED-1090** — videogame
  sub-unit cap is **11** ("subunits can be as high as 11."), lifting the TTRPG hard cap of 3; enforced
  in `engine.build_army`; open reconciliation flagged: Command clamps 1–7, so >7 commanded subunits
  needs a future Command-exceeding mechanism (subordinate officers?) — future ED. (3) **ED-1091** —
  the charge-recoil now zone-gates to the frontal (GREEN) arc (`PC_RECOIL_FRONTAL`, default ON;
  historical-validity condition verified against `mass_battle_gauge_grounding.md` §4.3/Burkholder
  before executing, per Jordan's "c7 if it is historically valid"); gauge row C7 can now legitimately
  add a braced+enveloped variant (grounding doc §4.3/§5.7 still says "flagged, not fixed" — update on
  the next gauge pass). **An orphaned-proposal audit (2026-07-02) also flagged:** `references/
  mass_battle_redesign_workplan_v1.md` is fully superseded (no banner exists — worth a supersession
  marker); `designs/proposals/multiunit_envelopment_plan.md`'s cross-**Unit** spatial envelopment
  ("Path B") is a materially different, still-unbuilt mechanism from the Unit-level `build_envelopment`
  that landed — don't conflate "Envelopment shipped" with "Path B shipped."
  **Stage E (Army Configuration Mode) shipped 2026-07-02** (MVP: click-to-place deployment tab in the
  workbench, `GET /api/roster-options`, `engine.SUBUNIT_CAP` client-enforced). **Stage F investigated
  2026-07-02 (ED-1092):** speed-differential puncture and depth-absorption were already done; fidelity
  D2 (cavalry lethality gated by regime) verified already-correct by direct probe; fidelity D1's zone
  half shipped as ED-1091, its actor half was Jordan-gated (no canonical actor-gate predicate existed).
  **T1–T4 charge-recoil ruling EXECUTED 2026-07-02 (ED-1095)**, closing D1's actor half plus three
  further parts from Jordan's own multi-clause ruling: T1 actor-gate (`PC_RECOIL_CHARGER_GATE` —
  charger must literally be `troop_type=='cavalry'`), T2 brace-setup delay (`PC_BRACE_SETUP_DELAY` +
  `Subunit._brace_since_tick` — brace needs ≥1 full tick of setup, stamped by `check_orders`), T3
  reach-gate (structural only — wires `troop_types.registry.reach_for` into the recoil condition, does
  **not** populate `TROOP_TYPE_REACH`, which stays deliberately empty pending a separate ruling), T4
  mounted-archer default kiting (`build_army` implicitly defaults `role='Kite'` for `mounted_archers`
  with no explicit role/shape/instructions). All four additive/toggle-gated, byte-exact-off preserved
  (verified all 4 `bat.py` digest modes + `tests/valoria` 81 passed/10 skipped).
  **RESOLVED 2026-07-02 (ED-MB-0001) — the movement/pathing fix-plan (ED-1096's root-cause finding)
  is EXECUTED, adversarially reviewed, and verified.** `envelop`/`sweep`/wheel/kite are now real on
  the live default node path, not just the legacy grid path. All 8 fix-plan steps + decision gates 2
  and 4 landed on `claude/mass-battle-audit-5c6nih`: `Subunit._rekey_node_state` fixes check_drift's
  node-state corruption; `reset_positions` is a deliberate no-op for node-path atoms; weapon-derived
  `unit_type` (`troop_types.registry.unit_type_for`) wired into `build_unit`/`build_army`, kite
  decoupled from `unit_type=='ranged'`; lateral file-holding restored (siblings hold their own
  deployment file); the node WHEEL's 180° facing-lerp stall replaced with a rotation-based update;
  the maneuver acceptance validators (`validators.py`'s `v_envelop`/`v_sweep`) re-pointed at the node
  path via a new `path` parameter, landed as `tests/valoria/test_mass_battle_maneuvers.py`; the
  waypoint primitive (`Subunit._resolve_maneuver_goal`/`_envelop_goal`/`_sweep_goal`) gives
  `_node_advance` real per-tick steering for `envelop`/`sweep`, modeled on the legacy per-cell
  two-state machine at anchor granularity; `PER_CELL`'s default flipped `0`→`1` (gate 4, "yes, all
  options/modules must be turned on") unlocking fatigue/charge-shock/brace-recoil/cavalry-speed by
  default. **Decision gates 1 (Command/Discipline-gated conditional tactics) and 3 (facing/attention
  split) remain explicitly DEFERRED** per Jordan's own sequencing ruling ("gates 1 and 3 are to occur
  AFTER we confirm that envelopment/pincer/wheeling/etc with pathing/routing is confirmed to work") —
  not built, by design, not a gap. A 5-dimension adversarial-review Workflow (sonnet finders + opus
  verify) found and fixed 6 more real bugs the same session, the most significant being that kite
  steering had NOT actually been ported to the node path in the first pass either (step 7 built
  `_envelop_goal`/`_sweep_goal` but no `_kite_goal` — mounted_archers still closed to melee) — closed
  via a new `_kite_goal`, verified holding standoff distance 6.5-8.3 against a Line. **Verified:** all
  4 `bat.py` digest modes byte-exact (2 unchanged grid, 2 deliberately re-recorded field, isolated via
  bisection to steps 1/4/5/7); full `tests/valoria` suite green (88 passed/10 skipped/1 xfailed); a
  `build_envelopment` wing tracked tick-by-tick under default toggles genuinely wheels from row 36 to
  row 19 — past the defender's own settled row — not a straight walk-in; delivered to Jordan as an
  interactive Artifact re-tracing the exact H4 (Envelopment vs Arrowhead) scenario shown broken
  earlier in the engagement. **One combat-balance finding disclosed, NOT chased (out of this fix's
  scope, per this repo's standing discipline against retuning magnitudes to fit a band):** enabling
  `PER_CELL`'s previously-inert fatigue/attrition/envelopment-sigma mechanics makes a frontal
  engagement resolve faster than a wide envelopment detour can complete in some compositions —
  confirmed via direct isolation to be a combat-*pacing* interaction, not a movement regression (a
  single-subunit control fight at the same troop ratio favors the attacker 14-0-6/20 seeds; forcing
  `orchestration.PER_CELL=False` alone restores the affected test's pass). Visible at battle scale in
  `gauge_mb.py`'s re-run (H3/H4(Cannae)/H5/H6 lose 0-13% instead of the 45-72% expected band) — landed
  as a loud, documented `xfail(strict=False)` on `test_envelop_reaches_rear_node`, not silently
  patched. **Next action for whoever picks this up:** the underlying combat-balance/pacing question
  (numerically-dominant vs. thin-and-yielding pinning force; a maneuver time-budget separate from the
  frontal fight's own clock) is open and needs either Jordan's design call or a dedicated combat-
  balance pass — then decision gates 1/3 (Command/Discipline-gated conditional tactics; facing/
  attention split) can proceed per the sequencing ruling above. Full detail: `tests/coverage_matrix.md`'s
  2026-07-02 movement/pathing-audit entries; `designs/audit/2026-07-02-mass-battle-movement-pathing-audit/
  README.md`; ledger entry `ED-MB-0001` (canon/editorial_ledger.jsonl) — the first allocation under the
  new `ED-<LANE>-NNNN` namespace (ED-IN-0001, origin/main cutover) that superseded in-progress
  in-code citations of the now-frozen flat `ED-1097`.
- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec
  RATIFIED (2026-07-02); HANDOFF split into per-lane files (2026-07-02).** The month's
  comprehensive review, the consolidation execution/reconciliation logs, and the single
  consolidated Jordan decision queue live at
  `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see `decision_queue.md`
  first — every gated item below is indexed there). Highest-leverage queued decisions:
  **doctrine ratification** (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`),
  **J-38 propagation-spec authorship** (workplan v5 §3 — unblocks conversion register #1 +
  `engine_clock`/ED-1051), Track-2 residuals (below), field-ON, the values_master
  regenerate-vs-retire call, and the duplicate compilation homes.
- **Scene-combat — merged (`d4bf2af3` PR #40, `8fbc4b66` PR #47); next up, all Jordan-gated:**
  1. **Two Track-2 residuals awaiting Jordan's single-source-target decision** (forward_roadmap Track 2;
     "Still open on `main`" above): (a) `wt`/`spd` cost-path de-leak (`core.py:55`, `systems.py:46`) — an
     autonomous before/after measurement harness can be prepped (roster-wide damage/tempo delta report) without
     flipping the live code; (b) `WP.reach()`/`authority()` vs `systems.reach_base`/`wield_heft` canonical-home
     fork (`weapon_physics.py:193,205`) — a short comparison doc of what each side currently computes and where
     they diverge can be prepped without touching code. Neither decision itself is agent-actionable.
  2. **Close the channel-leverage residual (the §C remainder, Phase 4c).** The affinity budget fixed
     total-competence but not per-channel leverage → spanish broad-strong, chinese broad-weak, only 2 niches. The
     fix is the **effectiveness-functions calibration**: measure each channel's marginal win-leverage, then
     normalise so each paradigm is decisive in *its* context (chinese-burst should win a fast/light-weapon
     context; german-bind the longsword context — currently it doesn't). **Design-laden** (how strong each
     paradigm should be = Jordan). Full detail: `designs/scene/combat_engine_v1/phase4_5_plan_v1.md` §4c.
     Re-measure with `python designs/scene/combat_engine_v1/workbench/balance.py context`.
  3. **The abilities-as-access depth** (Phase 4b / REARCHITECTURE P4 / WS-4's other half): the 7 phase-slots +
     techniques-as-permission + the learning-gate ("can't bind-and-wind / Spanish footwork without having
     trained it"); resolves the dormant `eff_cw`. Carries open decisions flagged Jordan's: affinity
     full-point-buy vs thin, the cyclic node relation, naming. **Also gated: Phase 4a**, the full
     game-theoretic psychological layer (Bayesian-signaling reads, mixed-strategy feints, Stackelberg-timing
     initiative, two within-fight dynamics) — never built, and previously undocumented in the repo. Full detail:
     `designs/scene/combat_engine_v1/phase4_5_plan_v1.md` §Phase 4.
  4. **Tunable magnitudes** (Class-C, workbench-adjustable): `RECOVERY_TEMPO_K` (0.15), `LUNGE_*`,
     `CLOSE_REACH_REF`.
  5. **Phase 5 contact axis** (clinch/disengage/choke; consumes the dead `clinch` primitive) — full detail
     `phase4_5_plan_v1.md` §Phase 5 — and **WS-7 multi-combatant envelope** (gated on ED-911 ratification)
     remain design-gated, no immediate action.
  6. **Stale-branch cleanup (needs Jordan's confirmation before deletion):** `design/scene-combat-v1`
     (local+remote) and `origin/scene-combat-track2-cleanup` are fully merged and redundant. Do not delete
     unilaterally — switch the working branch to `main`, confirm no uncommitted work, then offer deletion as
     a separate explicitly-confirmed step.
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
- **`ci_political_v30` read-routing (LB-24):** raw file ~26k but tracked read returns 0 (index-routes).
- **Ledger-status reconciliation (LA-23, Lane A — mostly done):** flipped ED-841/842/912 `open`→`resolved`
  and filed the never-written ED-938/ED-939 (backfilled from #13; artifacts verified). Dropped the
  report-only `validate_ed_citations` count 748→731. **Residual:** ED-914 left `open` — its mechanical
  parts remain (PP-719 record-or-strike; dead `fieldwork_design_v1` parent-path refs in `params/bg/core.md`,
  `designs/scene/fieldwork_v30.md`, `designs/scene/fieldwork_godot.md`).
- **Design-tier docket awaiting Jordan:** J-31 extended (social-contest deliberative-game findings,
  row #39 → LA-19) and the new **J-36** (Key-bus closure for the 6 off-bus writers, row #40 — gated on
  the distillation report's deferred adversarial pass).
- **Mass-battle coordinate-field engine — Stages A–D merged (2026-07-02, PRs #52/#56); next up, all
  Jordan-gated.** Detailed continuity/history lives in the staged plan file (session-local, not in the
  repo tree): `using-opus-4-8-ultracode-floating-tiger.md`. All four stages are `FIELD_MOVEMENT=1`
  opt-in only — the grid path (`FIELD_MOVEMENT=0`, every existing scenario's default) stayed byte-exact
  throughout (`bat.py`'s frozen `unit`/`cell` digests unchanged across every commit in both PRs).
  - **A** — true-adjacency stand-off halt + an exact time-of-impact (continuous-collision) resolver
    (replacing an earlier halved-clamp heuristic), plus a reach-and-facing-asymmetric closing-budget
    throttle (a longer-reach, correctly-facing body "sets into formation" before a shorter-reach one).
  - **B** — facing/attention/reaction physics (anti-hyper-reactivity) on the field path.
  - **C** — command layer: `engine.build_army` (multi-subunit armies), a timed/conditional `Order`
    queue, and `escort_of`/formation-relative positioning.
  - **D** — wires the previously-inert `Subunit.role` (gated by `role_allowed`); new
    `engine.build_envelopment`/`build_refused_flank` realize ED-909's Unit-level "Envelopment"/"Refused
    Flank" postures as compositions of existing primitives (no new movement/combat mechanic).
  - **Open, Jordan-gated:** (1) **LC-8** — literally retiring `Horseshoe`/`RefusedFlank` as
    `Subunit.shape` values (`geometry.CELL_PATTERN_FN`/`config.MIN_DISCIPLINE`) would break the frozen
    `bat.py` grid digests (its own battery uses `Horseshoe` directly), so it needs an explicit
    sign-off + a deliberate re-baseline — deferred, not done in Stage D. (2) Stage E (Army
    Configuration Mode UI) needs a ruling on whether the videogame keeps the TTRPG's Command-rating
    subunit-cap hard limit of 3 or lifts it (`mass_battle_v30.md` §A.5) before it can be built; Stage E
    is also a genuinely different kind of work (frontend/UI over the now-complete engine primitives),
    not a natural default-continue from A–D. (3) Stage F (charge/depth/equipment physics) is only
    scoped at a high level in the plan — needs real design work before implementation.
  first — every gated cross-lane item is indexed there). For subsystem-specific continuity,
  go to your lane's file in the table above; `handoffs/HANDOFF_IN.md` carries the full
  cross-cutting/governance narrative (doctrine ratification, ED-<LANE>-NNNN namespace creation,
  merge-ratifies-by-default convention, ecosystem-review residuals not owned by another lane).
- **Reserved-ID state:** the flat `ED-NNNN` sequence is FROZEN at `ED-1094` (2026-07-02
  cutover, `ED-IN-0001`). All NEW EDs use `ED-<LANE>-NNNN` — `references/id_reservations.yaml`'s
  `lane_ids` section is the live allocation source; read `next_free` for your lane, allocate,
  bump, co-commit. Never max+1.
