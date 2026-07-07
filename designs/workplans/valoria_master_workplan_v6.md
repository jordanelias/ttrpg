# Valoria — Master Workplan v6 (North-Star master: milestones, lanes, tiered decision register)

**2026-07-05 · status: CANON — RATIFIED (Jordan, 2026-07-05: "Ratify commit merge all", PR #78;
ED-IN-0011); the active master, supersedes v5. §5 is the live decision register (see its
ratification update — the T0 wall shrank to JD-1 + ED-1051).**

**as_of: HEAD `d31ac85a` (branch `claude/ners-audit-fable5-9cpfdz`, PR #78). Verified live:
`canon/editorial_ledger.jsonl` = 581 lines / 580 distinct IDs / flat-ED ceiling ED-1096 /
lane-tagged EDs through ED-IN-0008 · ED-MB-0002 · ED-PC-0001 · ED-SC-0001 · ED-SE-0001 ·
ED-WR-0002 · ED-FI-0001 (counts by direct JSONL scan at this SHA — the v5 header's "713
entries" no longer matches the live file's line count; report the method, not the memory).
Two count artifacts, surfaced not hidden: ED-306 appears twice (legacy duplicate in the
append-only ledger; rewriting it is a Jordan-reserved canon edit — register row T2-H3), and
ED-1095/ED-1096 are same-day-as-cutover 2026-07-02 flat allocations (valid; the flat freeze
holds from the cutover forward — no later flat allocation observed).**

**Supersedes (on merge):** `designs/workplans/valoria_master_workplan_v5.md` → moves to
`archives/workplans/` with a supersession banner (per `designs/workplans/README.md`). v5's
J-/LA-/LB-/LC- keys and v4's register rows 1–43 stay citable and are NOT renumbered; Appendix
A accounts for every open v5 item. v4 stays the frozen 06-11/06-22 record.

**Binds (does not fork):** `references/lane_assignments.yaml` (owns-globs; source pointer
repointed here) · `references/id_reservations.yaml` (lane counters live; allocation protocol
below) · `HANDOFF.md` + `handoffs/HANDOFF_<LANE>.md` (the ONLY per-lane status surface) ·
`CURRENT.md` (currency authority). Steering reconciliation executed with this document:
**ED-IN-0009** (this workplan) closing **ED-IN-0006** (roadmap_state retired, decision queue
refreshed, v5 archived, hierarchy adopted).

`[SELF-AUTHORED — bias risk: the inputs (the 07-04 NERS audit, the 07-05 narrative-engine
v1/v2 designs, the recent PC/MB session records) are Claude-authored; the 12 NERS EDs were
ratified-as-accepted by Jordan 2026-07-05 but their execution plans here are proposals. This
document sequences and dockets; it rules nothing — every fork in §5 is Jordan's, and the
held-back items are named loudly in the PR body.]`

---

## §0 · The North Star and how this document works

**North Star (ratified framing, 07-04 audit):** a Godot emergent grand-strategy ·
tactical-management · political-simulation · narrative RPG where **every subsystem points
toward an emergent-narrative player experience with rich meaningful choices**. The narrative
engine (v2, the Churn Engine) is the surface where all subsystems become visible; the
milestones below order everything by distance to that experience.

**Hierarchy (J-13, adopted per ED-IN-0006):** `CURRENT.md` (currency) → lane handoffs
(status) → this workplan (sequencing, milestones, decision register — DERIVED, it points at
the handoffs and never duplicates their status) → dated audit folders (evidence). Register
rows here carry **no status field** — only fork · default · what-it-blocks · home pointer.
Statuses live in exactly one place (the lane handoff or the ledger); the monthly reconcile
(§6) refreshes the pointers. This is the anti-drift design: v5 §3's J-38 line contradicted
CURRENT.md within four days precisely because two surfaces both claimed status.

**How to read:** §1 milestones · §2 the cross-cutting IN spine · §3 the narrative-engine
workstream · §4 per-lane workstreams (pointer + next increments + gates) · §5 the tiered
Jordan-decision register · §6 governance · Appendices A (v5 supersession) / B (session
inventory), both dated snapshots.

---

## §1 · Milestones

### M1 — ONE PLAYABLE SEASON (the ordering criterion, J-1)

A player takes a character through one full season loop in which every juncture is playable
and legible (the three questions answerable from the screen at each: what is at stake · who
is acting and why · what changed). Seven junctures, each mapped to the work that delivers it:

| # | Juncture | Delivering work (lane) |
|---|---|---|
| 1 | Strategic decision (the season's posture) | FA decision-surface work (J-5) + `domain_actions` module home (IN spine) |
| 2 | Domain action (resolve + Domain Echo render) | `domain_actions` authoring (IN); echo render via narrative Stage 0 |
| 3 | Social contest (a matter argued) | SC next stage (four deliberative games) + the claim-grammar requirements input (v2 §5) |
| 4 | Personal combat (one fight, legible) | PC lane R3 U-series; player-input surface (ED-PC-0001, post-R3) |
| 5 | Thread operation | Threadwork live; preconditions ED-1010/1011 (Coherence cap + C0 rule); MS naming sweep ED-WR-0002 |
| 6 | Season close (Accounting + propagation) | `engine_clock` ratification (ED-1051, home candidate = propagation_spec, ED-1093) + ordering flags ORD-3/ORD-4 |
| 7 | Articulation render (the season told back) | Narrative engine Stage 0 (ED-IN-0004) — ships first, J-7 visibility-before-rebalancing |

M1 requires **Layer A forecast only** (v2 §3 hard gate), the 8 authored COLLISION priors as
the convergence surface, and no Layer-B ensemble.

### M2 — THE ANY-SEED STORY BAR

v2 §9's fixture F1 as a shippable milestone: 5+ seeds each yield a chronicle that is
connected, continuous, rooted, live (invariants i–iv) and distinct in named actors, stakes,
outcomes — plus the F8 anti-self-fulfillment control passing. Requires narrative Stages 1–4
under the ratified Light-Function surface (F-F/fork-8, ED-IN-0011) and the Stage-1 compile
(fork-1 remap + fork-2 strike execution).

### M3 — GODOT VERTICAL SLICE

Gate-0 spine executed (G0.1–G0.5, §4-GO) + typed engine-params exports (ED-1052 scope
ruling) + the compiled generator corpus loading as a data pack (v2 §7 kernel/data/wrapper).
Explicitly after M1/M2's design closure: porting beyond the combat slice stays blocked on
authoring canon first (CLAUDE.md §6), and `valoria-game` has been frozen since 2026-05-04.

---

## §2 · Cross-cutting spine (IN lane)

Ordered; each item cites its ledger anchor. Status: `handoffs/HANDOFF_IN.md`.

1. **Steering reconcile (ED-IN-0006 → ED-IN-0009)** — EXECUTED WITH THIS PR: roadmap_state
   retired to `deprecated/references/` (banner), decision-queue items 1–3 refreshed, v5
   archived, hierarchy adopted (§0), CURRENT.md repointed.
2. **Gate-0 / ED-1051** — `engine_clock` ratification is juncture 6's gate and the GO lane's
   entry condition; the candidate home doc exists (propagation_spec_v1, CANONICAL ED-1093);
   what remains is the ruling that flips `module_contracts.yaml`'s `doc: null` (and then the
   other ~10 doc:null modules + 13 [ASSUMPTION] resolvers, prioritized by M1's junctures).
3. **`domain_actions` module home** — junctures 1–2 have no owning design doc; author the
   home (smallest of the doc:null closures, highest M1 leverage).
4. **Transport seams (J-3)** — consumer-declaration closure + targets[]/causes[] population
   rules are now v2 conformance rules (R1–R10 + R-F1/R-F2/R-HB/R-CL/R-AI/R-RL); the tools/
   home for each is narrative Stage-5 work but the RULES bind from Stage 0.
5. **Register back-propagation gate (ED-IN-0007)** — the CI register-touch discipline;
   pairs with the narrative Stage-1 compile (the register becomes a CI-round-tripped asset).
6. **Naming unification (ED-IN-0008)** — glossary fold-in, the 7-vs-9 attribute roster
   surface (queue item 13), resonance_style; feeds fork 10's faction-count ruling.
7. **Carried v5 LB tail** — LB-23 (freshness + ED-citation blocking-flips, gated on K-2 and
   triage-to-zero) · LB-24 (`ci_political_v30` read-routing) · supersession_register wiring
   (LB-19/22 tail) · names warn→block flips (v5 §10) · contest.py fabrication triage (queue
   16, prerequisite to the J-31 sim edit).

---

## §3 · Narrative-engine workstream (the Churn Engine, v2)

Head: `designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md`
(+ v1, spec chapters s1–s5 as amended by `spec/churn_amendments.md`). Executes ED-IN-0003
(detection) and ED-IN-0004 (render gaps). Stages, each independently mergeable:

| Stage | Contents | Gate |
|---|---|---|
| 0 | Render-gap close (ED-IN-0004: combat_resolved / investigation_resolved / 4 ED-681 thread beats / 2 meta Keys; §6.4 correction) | none — ships first (J-7) |
| 1 | Generator compile gate: template grammar + the 138+8 validation compile | execute the ratified fork-1 remap + fork-2 strike; fork 11 ratified at default |
| 2 | Store + tick (lifecycle FSMs) | Gate-0 honesty: Accounting substrate |
| 2.5 | Forecast — **Layer A alone for M1 (hard gate)**; Layer B only after: sim stubs (`npc_ai`, `ip_track`, `rs_track`, ~8 provincial), event-deck first code, scene-EV flag path, `canonical_key_log` serialization spec + ORD-3/ORD-4, fixtures F7+F8 | the listed preconditions |
| 3 | Detect (discovery + authored priors) | fork 3 window |
| 4 | Light + cast (+ ORD-4 scene-queue fix, scene_entered single-sourcing) | F-F/fork-8 RATIFIED (ED-IN-0011) — build gate only (after S2/S2.5) |
| 5 | Substance interface + scale-complete banks + conformance suite + fixtures F1–F8 | fork 6 (bake scoping); ERA instrument build |

Cross-lane handoff sequenced here: **v2 §5 (claim grammar) is a requirements input to the SC
lane's next stage** — four new contest sub-systems (evidence-weight δσ family · bluster move
class + pricing · precedent store + Recall rewire · commitment store + hypocrisy read),
shapes the SC lane's to accept or reshape. The FI lane (ED-FI-0001) is the evidence supply
chain for the same interface. ED-1054's residual (~>1MB tests/ narrative markdown) is now
ALSO a bake input asset — coordinate its relocation with Stage 5, don't lose it.

---

## §4 · Per-lane workstreams

_Format: **status pointer** (the handoff file — no status duplicated here) · next increments
· gates. Lane discipline: ED-<LANE>-NNNN allocation per `references/id_reservations.yaml`._

### PC — personal combat
Status: `handoffs/HANDOFF_PC.md`. Plan-of-record: R3 weapon-model consolidation
(`designs/audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md`, RATIFIED;
implementation not started). Sequence: **U0** units-honesty → **U1** PoB recalibration
(JD-1) → **U2** graded mode-affordance + Phase-C percussion enactment → **U3** edges
primitive (JD-2) → **U4** half-sword from attested grip (JD-3) → **U5** counterbalance →
**U6** retreat-as-default → **U7** weapon-class facing → **U8** guard-schema hygiene →
**U9** joint recalibration/capstone → **T-P2** profile-data campaign (JD-6, parallel) →
**T5** gated re-baselines incl. cross_section swap (JD-7). Forced order:
PoB → modes → capstone → P2-c. THEN: the player-input surface + ED-911 slots (**allocate
fresh ED-PC ids at filing — §6 collision rule**), Track-2 residuals (wt/spd damage-path
ready-except-spear; tempo-path NOT ready — double-counting; reach()/authority() =
retire-docstrings recommendation), phase4_5 (4a game-theoretic · 4b abilities-as-access ·
4c §C leverage · Phase 5 contact axis — gated on ED-911 + WS-7). M1 needs juncture 4 only:
one legible fight — the U-series' front half, not phase4_5.

### MB — mass battle
Status: `handoffs/HANDOFF_MB.md` (+ the 06-30 bottom-up workplan,
`designs/audit/2026-06-30-mass-battle-bottomup/05_redesign_workplan.md` — the governing
plan; do NOT resume `references/mass_battle_redesign_workplan_v1.md`, banner-superseded).
Next is NOT engine work: **Jordan rulings DG-1** (was pinning-force composition validly
ratified given it passed only under the RC-2 invincibility artifact?) + **DG-2**
(fighting-withdrawal/yield mechanic) + open **RC-5** (9/20 gauge rows failing for unrelated
reasons). Honest state: DG-3/DG-4 implemented (ED-MB-0002) but the Cannae gap is NOT closed
— H3/H5/H6 remain 100% draws. Then Stage-E UX depth (needs the Command-vs-cap-11 ruling,
ED-1090), Stage-F actor-gate, LC-8 re-baseline. Doc↔sim: §A.3b geometry + §A.8 splitting
numbers are banner-flagged; **sim leads canon** (ED-899/909/MB-0001/0002).

### SC — social contest
Status: `handoffs/HANDOFF_SC.md`. **First action: resolve the stage ambiguity** —
HANDOFF_SC says "Stage 3 next" while root HANDOFF says "Gate C done + merged PR #63, Stage 4
next"; read both + git and fix the stale one (this workplan does not adjudicate status).
Next stage contents: the four deliberative games (Agôn / Negotiation / Inquiry / Consensus —
agonists read the source-research trilogy directly: liberum veto → Consensus antibody,
Dowlen lottery → WeightedLot, Putnam two-level → ZOPA/win-sets) **+ the v2 §5 claim-grammar
requirements input (the four added sub-systems, shapes theirs)**; ED-SC-0001's sweeps fold
in (Recall/pool-cap, boost-vs-Appraise, coalition/solo floor per ED-297). Then seams (J-36
share) and settled canon (T-25).

### SE — settlements
Status: ED-SE-0001 (governance_play redesign staging; the event deck it specifies is also
the narrative generator's card substrate — no deck code exists yet, and Stage-2.5 Layer B
lists it as a precondition, so SE's deck work is on the M2 critical path even though SE
itself is not M1-gating beyond juncture 1's venue).

### WR — world
Status: ED-WR-0001 (GD-1 strain sweep, ~8 sites, grep-derived) + ED-WR-0002 (MS naming
sweep + enforce:block — precondition for the thread typed export and juncture 5). Cheap,
early, unblocking — schedule before the heavy lanes.

### FI — field investigation
Status: ED-FI-0001 (investigation audit) — now explicitly the **evidence supply chain** for
the claim-grammar interface (trails → evidence → argument → precedent → new stakes).

### FA — factions
Status: decision-surface work (J-5) delivers juncture 1; fork 10 (faction count 4–8
unreconciled across four docs, census finding) blocks any faction-scope bank/binding table
and needs its own ED + ruling. Sim win-share rebalancing stays post-M1 (J-7; queue 8) —
but F7's smoke oracle (narrative Stage 2.5 precondition) is where its regression gate lands.

### GO — Godot
Status: `handoffs/HANDOFF_GO.md` if present; governing spec =
`designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md`
(PROPOSED; 8-item register open). Gate-0 exact deliverables, none executed: **G0.1** Key.gd
v1→v2 (structured targets[], scale_signature[], symbolic_dimensions[4], time_horizon,
permanence, causes[]; drop scalar salience) · **G0.2** one ruled docs/architecture.md v2
(Meta-as-single-state-owner + thin services) + supersession banners on
implementation_sequence.md / data_serialization_spec.md · **G0.3** K8
Resource-vs-RefCounted verdict · **G0.4** register scene.combat_resolved +
scene.thread_operation, drop scene.draft_da · **G0.5** standing canonical-source gate.
Plus ED-1050's residual (re-export RESIST/GAP_EXPOSURE/gap-game to weapon_resource.gd /
strike_module.gd — Key-log parity known-red until done) and ED-1006 (downward Key
delivery). Consumes the IN spine; M3-gated.

---

## §5 · Tiered Jordan-decision register

_Rows: fork · default · blocks · home pointer. **No status column** — resolution lives in
the ledger/handoffs; the monthly reconcile refreshes this table's pointers. Tier = T0 blocks
M1 · T1 blocks a named stage · T2 taste/tuning/housekeeping._

**Ratification update (2026-07-05, ED-IN-0011 — Jordan: "Ratify commit merge all"):** every
fork in this register that carried a stated default is RATIFIED at that default — struck
below where T0, adopted-in-place for T1/T2 (F-F/fork-8 incl. the subtract-only discipline;
forks 1/2/3/6/7/9/11; v1 forks 4–5; F-A..F-G with F-G's numbers still Jordan's later).
ExecUTION of ruled directions (fork-1 remap, fork-2 strike) remains scheduled work.
Still genuinely open (no default existed): fork 10's faction COUNT (ED-FA-0001), JD-1..8,
DG-1/DG-2, RC-5, ED-1090, ED-1051, ED-1052, ED-911/WS-7, attribute roster, the
Godot register — cross-lane questions this PR never carried. (ED-1042 removed from this
list 2026-07-07 per ED-PC-0004: it was STRUCK 2026-06-28, superseded_by ED-1021, so it was
already stale when this line was written; the reverse-direction residual drift is re-filed
as ED-PC-0005.)

### T0 — block the M1 path

| Fork | Default | Blocks | Home |
|---|---|---|---|
| ~~F-F/fork-8 — the Light-Function decision~~ **RATIFIED at default 2026-07-05 (ED-IN-0011)** | subtract-only + the §4 weight enumeration (values stay tunable data) | — | v2 §4/§10 |
| ~~fork 1 — Coup-Counter remap~~ **RATIFIED at default (ED-IN-0011); execution = Stage-1 work item** | 1:1 remap onto Löwenritter Autonomy 4-stage | narrative Stage 1 compile (execution) | v2 §2 |
| ~~fork 2 — ARC-T04~~ **RATIFIED at default (ED-IN-0011); execution = Stage-1 work item** | strike; COLLISION-C → 7-of-8 | Stage-1 validation set (execution) | v2 §2 |
| JD-1 — PoB bands (PC U1) | per consolidation_v1 | the whole U-series chain → juncture 4 | R3 consolidation_v1 |
| ED-1051 — engine_clock ratification | flip doc:null to propagation_spec_v1 | juncture 6; GO entry | decision queue 12; CURRENT.md L32 |

### T1 — block a named stage

| Fork | Default | Blocks | Home |
|---|---|---|---|
| DG-1 — pinning-force ratification validity | re-adjudicate post-RC-2 | MB next stage | MB 06-30 workplan |
| DG-2 — fighting-withdrawal/yield | author the mechanic | MB next stage; H3/H5/H6 draws | MB 06-30 workplan |
| RC-5 — 9/20 gauge rows failing | triage per-row | MB gauge confidence | MB handoff |
| ED-1090 — Command-vs-cap-11 | keep TTRPG cap until ruled | MB Stage E | MB handoff |
| fork 3 — convergence temporal window | same-Accounting priors; 4-season cosine discovery | narrative Stage 3 | v2 §10 |
| fork 6 — Certainty-in-bake | include (headline ~1,200–2,700 units); fallback lexicon-swap (230–450) | Stage-5 build scoping | v2 §6/§10 |
| fork 10 — faction-count reconciliation (4–8 across four docs) | **ED-FA-0001 filed**; the count ruling itself is Jordan's (no default) | faction-scope banks/bindings | v2 §10; census §1.2 |
| fork 11 — scenario_authoring authoring-vs-runtime | compile = authoring-time | Stage 1 compile home | v2 §10; module_contracts [OPEN] |
| F-A — forecast fidelity per branch class | Layer A continuous / Layer B discrete; discrete per-lever deferred post-M1 | Stage 2.5 | v2 §3/§10 |
| JD-2…JD-8 (PC) | per consolidation_v1 rows | the named U-steps / T-P2 / T5 | R3 consolidation_v1 |
| J-31 extended sitting (SC deliberative findings) | per critique §6 tags | SC next stage; LA-19 | v5 row 39; SC handoff |
| J-36 — Key-bus closure (six off-bus writers) | on-bus, carve-outs explicit | Lane-C wiring; chronicle completeness | v5 row 40; [VERIFY] pass still deferred |
| ~~ED-1042 — wound-model spec-vs-code drift~~ **STRUCK in ledger 2026-06-28 (superseded_by ED-1021); reconciliation = ED-PC-0004; residual re-filed ED-PC-0005** | — | PC coverage confidence | queue 4 (superseded pointer) |
| ED-1052 — typed-params layer scope (+ queue 17/24) | extend the combat_engine_v1.json pattern to settled non-combat values | M3 exports | queue 24 |
| ED-911 (P1) + WS-7 | — | PC phase4_5 | PC handoff |
| fork 9 — Torben Loyalty range (register/sim 8→0 vs clock_registry 0–7) | reconcile at Stage-1 compile | ARC-S07 fidelity | v2 §2 |
| ED-609 — Torben Conviction emergence | stays open; compile cites with disposition | Conviction-emergence beats only | s2 compile note |
| attribute-roster ratification (queue 13) | — | ED-IN-0008 completion; descriptor keys for Godot | descriptor_registry; queue 13 |
| Godot strategy 8-item register + K8 + first-module target (queue 10–11) | — | Gate-0 execution | strategy doc |

### T2 — taste / tuning / housekeeping

| Fork | Default | Blocks | Home |
|---|---|---|---|
| F-B horizon k + ensemble N | k≈4, N≈64 | tuning only | v2 §3 |
| F-C forecast-render access rules | position-scoped (T-30); NPC reads barred by R-AI | counsel/omen surfaces | v2 §10 |
| F-D counterfactual-ghost budget | sparing | chronicle texture | v2 §10 |
| F-E anticipation reflexivity | one-pass | — | v2 §10 |
| F-G evidence-weight formula | form canonical, numbers Jordan's (ED-874 split) | SC addition (1) numbers | v2 §5/§10 |
| fork 7 — GM-judgment residue ~15% + bespoke-EFFECT NPC-ARCs | declare non-firing / hand-authored effect tables | honesty ledger only | v2 §2/§10 |
| forks 4–5 (v1: casting-breadth, venue-matrix edges) | v1 defaults | — | v1 §forks |
| J-8's six-part faction-inversion sitting (with J-7-key of v4 — naming collision with this plan's J-7 judgment noted; cite as "v4 J-7/J-8") | — | faction write-path port | v4 §3 |
| JD-6 P2 scope · JD-8 renderer recovery | per consolidation_v1 | T-P2/T5 detail | R3 plan |
| queue 8 — sim degenerate win-share | post-M1 (J-7); F7 oracle first | balance tuning | queue 8 |
| queue 9 — sim/ vs tests/sim naming | documented, high blast radius | — | sim/README.md |
| queue 14 — needs_jordan ledger set | — | per-entry | ledger |
| queue 19 — agent-roster promotion | on recurrence only | — | doctrine §7 |
| queue 21–23 — stale branches · duplicate compilation homes · pre-restructure ledger paths (+ ED-306 dup, header note) | — | — | queue; T2-H3 |
| ED-1054 residual — >1MB narrative-md relocation + sim README regeneration | coordinate with narrative Stage 5 (bake asset) | — | queue 25 |
| ED-879 (G8 C3×PoolFloor) · ED-538 (Accord/Stability compound) · ED-1043 (orchestration.py stages) · ED-1006 (downward Key delivery) · ED-1009 (multi-emitter attribution; v2 defers-with-pointer) · ED-1010/1011 (thread preconditions — T1 if juncture 5 slips) | — | as cited | ledger |
| ED-595–610 creative block · ED-913–932 hygiene batch | — | — | index-only |
| npc-comprehensive-audit orphan (Appendix B) | one triage ED, NPC-adjacent lane | — | Appendix B |

---

## §6 · Governance

- **Monthly reconcile (J-14, institutionalized):** checklist = re-verify ledger counts by
  scan → refresh §5 pointers (strike resolved rows, no status edits elsewhere) → confirm
  CURRENT.md rows against heads → confirm handoff freshness per lane → refresh the
  progress board (below) → dated-snapshot the session inventory delta → one commit
  `[editorial]` citing this section.
- **Progress board (ED-IN-0010):** `designs/workplans/workplan_v6_progress.yaml` is the
  ONE designated home for milestone/juncture-level rollup status (a rollup nothing else
  carries — lane detail stays in the handoffs; rows point at evidence). Rendered only by
  `tools/workplan_status.py` (one-liner in the SessionStart banner; `--full` ASCII
  diagram); owned and freshness-verified-on-every-read by the
  `valoria-workplan-navigator` skill ("where are we?" / "resume from the workplan" →
  position + options). A stale `as_of` is surfaced, never silently trusted — the
  anti-rot answer to the retired roadmap_state.yaml.
- **Register-touch rule (ED-IN-0007):** any edit to a compiled register surface must touch
  its runtime form in the same PR once narrative Stage 1 lands.
- **ID protocol:** `references/id_reservations.yaml` is the allocation source (read
  `next_free`, allocate, bump, co-commit — never max+1). Flat sequence frozen (ED-IN-0001);
  ledger ceiling verified ED-1096 (header note). **ED-PC collision rule, resolved loudly:**
  R3's ratified plan text labels its increments "ED-PC-0001..0012" — those are plan-text
  LABELS, never filed; the ledger's real ED-PC-0001 is the player-input item (filed
  2026-07-05). When R3 increments file, they allocate fresh IDs from `next_free` at filing
  time and cite the plan-text label in the description. Never trust an ID printed in a plan
  over the counter.
- **Skeptic convention (carried v4 §8 / v5 §8):** propagate-don't-caveat · ED citations
  ledger-verified, never memory-sourced · source-tier discipline · rules live once, in
  `tools/`.
- **Session lane-scoping (CLAUDE.md §4):** declare the lane, keep the PR scoped; IN only for
  genuinely cross-cutting work.

---

## Appendix A · v5 supersession table (dated snapshot, 2026-07-05 — every open v5 item accounted)

| v5 item | Disposition in v6 |
|---|---|
| §0a / LB-21 reserved-ID exhaustion | EXECUTED 2026-07-01 (id_reservations v3, blocks D/E) then made structurally moot by the ED-IN-0001 lane cutover (2026-07-02) — lane counters, no shared blocks. |
| Row 39 / J-31 extended / LA-19 | Carried → §4-SC (four games + ED-SC-0001 folds + v2 §5 requirements input); the commitment store the critique wanted is now SC addition (4). Register: J-31 in T1. |
| Row 40 / J-36 Key-bus closure | Carried → T1; the deferred [VERIFY] adversarial pass still gates it; the narrative engine RAISES its priority (six off-bus writers break the chronicle's one-ledger property). |
| Row 41 / J-33 combat-traditions critique | Superseded-in-part by R2 (MERGED PR #72) + R3 (RATIFIED plan-of-record): the morphology line landed as the granularity audit + consolidation_v1. Residue = JD-1..8 + Track-2 + phase4_5 → §4-PC + §5. |
| Row 42 deprecation sweep | Executed (v5 §10 #17). Residual supersession_register wiring → §2 item 7. |
| Row 43 / J-37 deterministic-NLG realizer | **SUPERSEDED by the narrative engine v1+v2** — the offline prose-writer bake + splice realizer IS the PP-688 §11 answer (v2 §6); J-37's ratification question becomes the narrative staging's fork gates. |
| J-38 propagation-spec authorship | RATIFIED (ED-1093/ED-1083/ED-1094, 2026-07-02) — the v5 §3 line saying "open/PROPOSED" was the ED-IN-0006 contradiction; corrected here, v5 archived with banner. |
| LA-23 residual (ED-914 mechanical: PP-719 record-or-strike + dead fieldwork_design_v1 refs in 3 files) | Carried → WR/IN small-sweep pool (schedule with ED-WR sweeps). |
| LB-22 | Done (v5 §10). `tools/`-scope hooks-verifier flip residual → §2 item 7 (names/tools tail). |
| LB-23 freshness + ED-citation flips | Carried → §2 item 7 (gates unchanged: K-2 SHA-split; triage-to-zero). |
| LB-24 ci_political read-routing | Carried → §2 item 7. |
| Lane-C contest.py fabrication triage | Carried → §2 item 7 (queue 16). |
| Names LB item (v5 §10 #22) | Carried → §2 item 6 (folds into ED-IN-0008) + §2 item 7. |
| v4 rows 1–38 + docket J-1…J-35 | Carry as before (v4 frozen record); still-open keys resolve through §5's pointers (headline carriers: J-31, J-33, J-36, v4 J-7/J-8, J-12/J-18 tails). |
| Decision-queue (2026-07-01) items | Refreshed in place this PR: 1–2 superseded by R2 → R3 JDs; 3 superseded (phase4_5 sequenced §4-PC); 6/18/20 strikethroughs confirmed; 4/5/7–17/19/21–25 carried with §5 pointers. |

## Appendix B · Session-inventory snapshot (dated 2026-07-05; ~40 dated sessions, 2026-06→07)

Dispositions per the 07-05 inventory sweep: PC 16 sessions · MB 5 · SC 8 · IN/GO 11 ·
SE/WR/FA/FI 1 + heads — all tracked into a lane workstream or an archived/superseded record,
EXCEPT:

- **ORPHAN: `designs/audit/2026-06-22-npc-comprehensive-audit.md`** — 449 verified findings,
  zero inbound references from any live surface (v5 §0 staged it as "ledger candidates at
  next lane entry"; no lane entered). Default (T2 row): file ONE triage ED in the
  NPC-adjacent lane to fold-or-retire it; its findings are also candidate inputs to the
  narrative engine's NPC voice/anti-oatmeal banks (v2 §6).
- Weak-tracked (note-only): `2026-06-19-pc-loose-ends` (superseded by R2/R3 line),
  `2026-06-09-consolidation-master` (historical; superseded by v5→v6 lineage).

The 2026-07-04/05 sessions themselves: the NERS qualitative audit (MERGED PR #77, 12 EDs
ratified) · the narrative engine v1 + v2 + this workplan (PR #78, this document).

---
*v6 is the single working master on merge, superseding v5 (archived). Every §5 row is
Jordan's; the held-back item is F-F/fork-8 (one surface: subtract-only + the weight set).
This document allocated **ED-IN-0009** (steering reconcile execution + v6 authorship record)
per the lane protocol; no other IDs assigned here.*
