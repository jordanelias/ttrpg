# Cluster I dossier — mode bridge & temporal cadence (verbatim agent output)

_Sonnet evidence agent, 2026-07-05. Headline claims Fable-verified against the working tree —
see `verification_log.md` (fieldwork_hybrid §9.2 contains only the phase-order sentence and the
bonus-scene rule survives only in the two infill files, GM-phrased, confirmed; board_game.md
carries 16 `params_bg_*` reference lines, zero of which exist under `references/`; params/bg/
victory.md carries Varfell Path C (VTM=5) at two sites while victory_v30.md L388 reads "Path C —
STRUCK (PP-663, 2026-04-19)"). Fable reclassification: candidate finding 5 (D.6 double-count) is
KNOWN-TRACKED — propagation_spec_v1 §5's own ranked open-flag list carries it; the player-chair
consequence framing is this dossier's addition. Verbatim below._

---

# The Mode Bridge & Temporal Cadence — Playability Audit

**Cluster scope:** designs/architecture/scale_transitions_v30.md (+ _index/_infill), designs/architecture/player_agency_v30.md, designs/scene/fieldwork_hybrid_v30.md (+_infill), designs/territory/settlement_layer_v30.md §4, designs/architecture/propagation_spec_v1.md, references/module_contracts.yaml, params/board_game.md + params/bg/*, designs/provincial/victory_v30.md + strategic_layer_v30.md.

**Currency note up front:** `CURRENT.md` has **no row** for scale_transitions, player_agency, or fieldwork/fieldwork_hybrid — the entire Mode Bridge cluster is absent from the one human-readable currency index, though all three are tracked in `references/canonical_sources.yaml` (lines 185-189, 451-454, 478-482) and internally marked `## Status: CANONICAL`/`DESIGN — canonical`. Everything below resolves currency from the files' own Status lines since CURRENT.md is silent on this cluster.

---

### E1 · Mode boundaries themselves
1. **MOMENT:** the instant the game decides "you are now in Personal / Hybrid / BG resolution."
2. **DECISION:** per `scale_transitions_v30.md` §3.2 (line 49), "**GM** recognises faction scope" — the current canonical skeleton still names a Game Master as the decision-maker for the Personal→Faction handoff.
3. **FEEDBACK:** none specified for how the *engine* signals a mode boundary crossing to the player (no UI/state-transition described anywhere in §1/§6).
4. **LATENCY:** §6.1 (TTRPG→BG) and §6.3 (Hybrid→TTRPG) are literally empty headers in the skeleton (`scale_transitions_v30.md` lines 239, 244; confirmed 9/8 tokens in `scale_transitions_v30_index.md` lines 96,98) — no procedure exists to time-box these two of three named transitions.
5. **FRICTION:** low in principle (§1's three-mode table is clean), but the load-bearing "who decides" language for two of the eight handoffs (§3.2, and the fieldwork bonus-scene grant, see Candidate Finding 1) is GM-adjudicated prose never translated to an engine rule.
6. **RECIPROCITY:** §12 (All-Directions Key Delivery, ratified J-1) is a genuine, well-specified answer for *how* consequences propagate once a mode is set — but it doesn't touch *who/what sets the mode* in the first place.
7. **VERDICT:** PLAYS-ROUGH (as authored) / INERT for §6.1 & §6.3 specifically — P1 — **NOT-INTENDED** (contradicts CLAUDE.md's explicit "no GM — the engine resolves everything").

### E2 · Zoom In / Zoom Out round-trip
1. **MOMENT:** BG Domain Action outcome → personal scene → consequence back into BG state.
2. **DECISION:** legal entry points are well-bounded (PP-103: after Phase 1/3/6-Step-1; mid-Phase-5 defers, PP-250/ED-158) — `scale_transitions_v30.md` §4.1.
3. **FEEDBACK:** Scene Opportunity Ob shift (±1/±2 by BG degree, §4.1) is clear and legible — a real, felt consequence of strategic performance on personal difficulty.
4. **LATENCY:** §4.2 states plainly the BG clock does **not** pause — Zoom In "inserts a personal scene into the resolution sequence," Phase 6 Steps 2-6 continue after Zoom Out (PP-110). This is coherent and stated once, cleanly.
5. **FRICTION:** ED-159 (incapacitation) and ED-167 (CF wound → +1 Ob to commander) are concrete, well-cited consequence hooks — low friction, high legibility.
6. **RECIPROCITY:** strong — BG degree shapes the scene (down), scene outcome reshapes BG via Domain Echo (up); this is the cluster's best-specified loop.
7. **VERDICT:** PLAYS-WELL — P2 (the residual risk is entirely the empty §6.3 procedure feeding this loop, already flagged in E1) — **DELIBERATE**.

### E3 · Coherence across the bridge (§6.4/§6.5)
1. **MOMENT:** a PC's Thread-resource state carrying across Zoom cycles.
2. **DECISION:** §6.4 — first activation = Coherence 10, subsequent = carry-forward, no free reset. §6.5 — single declaring PC bears all Coherence cost; co-leadership explicitly disallowed.
3. **FEEDBACK:** the "no free reset" rule is exactly the kind of resource-continuity signal that makes cross-mode play feel like one game rather than three save states.
4. **LATENCY:** instantaneous, state-carried — no queuing ambiguity here (unlike Domain Echo).
5. **FRICTION:** §6.5's single-payer rule is a deliberate scarcity lever (one PC "bears the Thread bridge cost") — this reads as an intended strategic constraint, not friction.
6. **RECIPROCITY:** n/a — this is single-directional resource bookkeeping, correctly scoped.
7. **VERDICT:** PLAYS-WELL — P3 — **DELIBERATE**.

### E4 · Thread timing in Hybrid (§10)
1. **MOMENT:** a Thread op (Dissolution/POP/Lock/Weave/Mend) performed inside a Hybrid season.
2. **DECISION:** CI auto-effect table (Dissolution +1, POP −1, others none) is deterministic and clean.
3. **FEEDBACK:** paradox window (1 season on POP) is a good legible consequence.
4. **LATENCY:** **ambiguous** — the CI table doesn't state whether it fires immediately (scene-end, per §5.3's "Full TTRPG" timing) or queues to Accounting (per §5.3's Hybrid timing, PP-109's deliberate anti-manipulation asymmetry). If CI ticks instantly while that same action's Domain Echo consequence queues, the player experiences two different latencies from one action with no stated reconciliation.
5. **FRICTION:** "BG Co-Movement ceiling applies only to BG-initiated Thread abstraction (not TTRPG scene Thread ops)" (line 291) is a correct-looking asymmetry but is asserted, not derived — no worked example shows both halves resolving in the same season.
6. **RECIPROCITY:** "Full TTRPG RS values propagate directly to BG RS track" — one-directional and stated once, no ambiguity there.
7. **VERDICT:** PLAYS-ROUGH on the latency question — P2 — **UNDETERMINED**.

### E5 · BG Survey ↔ TTRPG Discovery
1. **MOMENT:** a strategic Survey action seeding a personal fieldwork scene's difficulty.
2. **DECISION:** the ±2-cap Fieldwork Offset table (Failure −1 / Partial 0 / Success +1 / Overwhelming +2 Ob) is identically stated in both `scale_transitions_v30.md` §3.9 row 7 and `fieldwork_hybrid_v30.md` §9.1 — consistent, well-cited, genuinely playable.
3. **FEEDBACK:** direct and proportional — better strategic play measurably eases the personal scene.
4. **LATENCY:** §9.2 confirms phase order is fixed (Strategic before Personal) so the offset is always available same-season — no lag.
5. **FRICTION:** low for the Offset half of the loop.
6. **RECIPROCITY:** **broken on the payoff half.** The "bonus Personal Phase scene... replaces, does not extend, standard 2–3 Personal Phase scenes" rule cited by `scale_transitions_v30.md` §3.9 row 9 as living in `fieldwork_hybrid.md §9.2` **does not exist in that section** (checked: `fieldwork_hybrid_v30.md` lines 23-26 contain only the phase-order sentence). The rule only survives in the infill co-files (`fieldwork_v30_infill.md:127`, `fieldwork_hybrid_v30_infill.md:12`), phrased as "**the GM may grant** a bonus Personal Phase scene" — an adjudicated grant, not an engine-decidable trigger — and referencing a "2-3 Personal Phase scenes" cap that `player_agency_v30` §6.1 has since superseded with a difficulty-scaled 3-5 scene-action budget, unreconciled.
7. **VERDICT:** the Ob-shift half PLAYS-WELL; the bonus-scene reward half is **MISSING** in engine terms — P1 — **NOT-INTENDED**.

### E6 · Scene slate + scene action budget
1. **MOMENT:** season-start Slate generation, player choosing among 4-9 opportunities with 3-5 actions.
2. **DECISION:** the 7-step generation algorithm + deterministic cross-step pruning (`player_agency_v30` §4.2-§4.3) is unusually rigorous — same state produces same Slate, same entry-set produces same final Slate.
3. **FEEDBACK:** §4.5's "Opportunities Not Pursued" table is the standout feature — every unpursued Priority tier has a stated, differentiated consequence (NPC resolves alone, Disposition penalty, Standing −1, "opportunity lost permanently"). This is genuine triage-as-gameplay (the Pathologic precedent, §1.5, is earned).
4. **LATENCY:** same-season resolution for attended and unattended entries alike — no batching opacity here.
5. **FRICTION / starvation risk:** mandatory (Priority 0) entries "cannot be declined" and consume 1 action each; a real risk exists if enough of the eight `scale_transitions` §4.3.2 mandatory triggers co-fire in one season to exceed the budget entirely. The design **does** cap this: overflow triggers Witness Mode (free Read/Appraise, one narrative input, no Domain Echo, no Momentum/Coherence cost) rather than a hard block — a genuine, working release valve (ED-745/ED-761). But there is **no stated ceiling on the count of simultaneous mandatories** — only a priority *order* among them (§4.2 internal ordering list, 8 entries) — so a pathological season (Settlement Revolt + Heresy target + Leader Removal + Mass Battle all firing at once) degrades every discretionary slot to Witness Mode with nothing to stop it recurring.
6. **RECIPROCITY:** strong — Conviction/Duty-aligned entries (§4.2 Steps 3-4) mean player-authored goals genuinely shape what the Slate offers, not just what the world imposes.
7. **VERDICT:** PLAYS-WELL as the strongest-specified system in this cluster — P2 on the uncapped-mandatory-count edge case — **DELIBERATE** (Witness Mode is a deliberate, cited mitigation; the residual gap is UNDETERMINED).

### E7 · Season/accounting cadence as the temporal seam
1. **MOMENT:** declare Duty/DA → play Personal-Phase scenes → watch Accounting resolve.
2. **DECISION:** `module_contracts.yaml` accounting_sequence (season_tick → B_concern → DA_proposal → C_project → D_opinion → E_offscreen → settlement_accounting) and `propagation_spec_v1.md` §O.1 ("season is the tick," `run_season` = SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY) together describe a real, ordered heartbeat — not a black box, on paper.
3. **FEEDBACK:** the rhythm *should* read to the player as declare → play → see consequences resolve in a legible order.
4. **LATENCY:** engine_clock's `doc: null` status (module_contracts.yaml line 686-698) is real but not fatal on its own — `propagation_spec_v1.md` §O.2 supplies a candidate home doc, formally unratified pending ED-1051 (known, per calibration).
5. **FRICTION / player-visible ordering artifacts:** **yes, concretely.** §D.6 (`propagation_spec_v1.md` lines 247-253) flags a HIGH-PRIORITY, Jordan-unresolved double-count risk: a strategic modifier's down-targeted settlement `stat_deltas` may overlap the very settlement stats `AGGREGATE_s` reads to re-derive the faction stat — "the same scene outcome is counted twice." §4.3 states the termination guarantee is explicitly CONDITIONAL on this being ruled disjoint, and that if not, the up/down loop "can sustain a bounded-magnitude oscillation that `decay()` may not damp" — and `decay()` itself is unspecified (OF-3). **Player-chair scenario:** one Governance action swings a faction stat by roughly double the printed rule's magnitude, and/or the number partially reverses next season with no visible cause — reading as buggy inconsistency rather than a legible strategic response to the player's choice.
6. **RECIPROCITY:** the aggregate-up (§2, AU-1 "no aggregate is ever written") / distribute-down (§3, D.1) split is a clean, well-specified rule *in the abstract* — the risk is specifically at their seam (D.6), not in either transform alone.
7. **VERDICT:** DEGENERATE-RISK if D.6 resolves non-disjoint — P1 — **UNDETERMINED** (explicitly an open Jordan ruling, not yet a bug, but its failure mode is player-visible drift/oscillation that nothing in canon currently describes to the player as intentional). [Fable: KNOWN-TRACKED — propagation_spec §5's own open-flag register.]

### E8 · BG-layer params currency
1. **MOMENT:** a player-facing strategic-layer screen built from `params/board_game.md` + `params/bg/*`.
2. **DECISION → SPOT CHECK 1 (navigation):** `params/board_game.md` is an auto-generated index whose **every one of its `params_bg_*` links** points to `references/params_bg_*.md` — none of which exist (verified: `references/params_bg_clocks.md` etc. are all MISSING). Actual content lives at `params/bg/*.md`; one filename doesn't even match (`params_bg_tc_seizure.md` linked vs actual `ci_seizure.md`). The cited "Board game" head in `CURRENT.md` is, as a navigable index, 100% dead.
3. **FEEDBACK → SPOT CHECK 2 (internal contradiction):** `params/bg/phases.md` Phase 5 step 11 reads "[DISSOLVED — Hollow Victory totals no longer tracked]" but the same file's Year-End Accounting step 6 still reads "Hollow Victory totals announced publicly" — a live dramatic beat referencing a dissolved mechanic, within one file.
4. **LATENCY → SPOT CHECK 3 (broken citation):** `params/bg/phases.md` step 12 cites victory conditions at "`designs/board_game/victory_v30.md` §3" — that path does not exist (`designs/board_game/` is missing entirely); the actual canonical head is `designs/provincial/victory_v30.md`.
5. **FRICTION → SPOT CHECK 4 (stale numbers, most severe):** `params/bg/victory.md` still lists **Varfell Path C ("Thread Supremacy," PV≥10 + VTM=5 + MS≥50)** — explicitly **STRUCK** in canonical `victory_v30.md` line 388 ("Path C — STRUCK, PP-663, 2026-04-19") — and its co-victory table uses pre-PP-663 **VTM** thresholds (VTM≥3/≥4) and **≥4-territory** gates where canonical `victory_v30.md` (lines 541-543) now requires **WR≥2** (PP-663: "VTM ≥3 replaced by WR ≥2") and **≥3 territories** (PP-545/546), and is missing the canonical "Varfell controls T13" gate for Varfell+RM co-victory entirely.
6. **RECIPROCITY:** the design intent (PP-663, ED-311, both formally CLOSED) clearly moved the Thread-mastery axis from VTM to WR — the params layer simply never absorbed that closure.
7. **VERDICT:** DEGENERATE-RISK / player-facing — a strategic layer built from these tables would let a player grind toward a dead victory path (VTM=5) and misjudge real co-victory eligibility — P1 — **NOT-INTENDED**.

---

## Candidate findings

1. **[NEW] GM-era decision language survives in GM-less canon at the mode boundary itself.** `scale_transitions_v30.md` §3.2 line 49 ("GM recognises faction scope") is in the current canonical skeleton, not just deprecated infill. Failure scenario: the engine has no stated rule for detecting a Personal→Faction handoff — the single most basic "who decides the mode" question in this cluster is unanswered for the videogame. Compounded by `params/scale_transitions.md` ("GM makes final scope determination," "GM narrative") and the fieldwork infill's "GM may grant a bonus scene." Severity P1. Intent gate: **NOT-INTENDED** (direct contradiction of CLAUDE.md's explicit framing).

2. **[NEW] §6.1/§6.3/§3.3/§8 are hollow in the mechanical skeleton, content-bearing only in the co-filed infill — a co-filing/atomization defect with real gameplay cost.** `scale_transitions_v30.md` §6.1 (line 239), §6.3 (line 244), §3.3 (line 51), §8 (line 271) are single-line headers; `scale_transitions_v30_infill.md` lines 17-18, 43, 46-47, 54-55 carry the actual prose (and it's GM-era prose). Failure scenario: an implementer reading only the "mechanical spec" file — the CLAUDE.md-endorsed way to resolve rules — finds no procedure for two of the three headline mode transitions. Severity P1. Intent gate: **UNDETERMINED** (could be read as "handoffs are authored sugar over the substrate," per the file's own §3 preamble, but the specific named §6 procedures read as accidentally emptied, not superseded).

3. **[NEW] The Mode Bridge cluster is invisible to `CURRENT.md`.** No row for scale_transitions, player_agency, or fieldwork/fieldwork_hybrid, despite CANONICAL status and tracked SHA pins in `canonical_sources.yaml`. Failure scenario: anyone (agent or designer) following CLAUDE.md's mandated currency-resolution order never lands on the docs that answer "who decides the mode." Severity P2. Intent gate: **NOT-INTENDED**.

4. **[NEW] BG Survey→TTRPG Discovery's reward half doesn't exist as an engine rule.** The specific "bonus Personal Phase scene" payoff cited by `scale_transitions_v30.md` §3.9 row 9 at `fieldwork_hybrid.md §9.2` is absent from that section; it survives only in infill, GM-phrased, and referencing a scene-budget number (2-3) superseded by `player_agency_v30` §6.1's 3-5. Failure scenario: the strategic→personal information pipeline's intended reward (a Survey paying off with a *free* extra personal scene) has no deterministic trigger for the engine to fire. Severity P1. Intent gate: **NOT-INTENDED**.

5. **[KNOWN-TRACKED reframe — Fable reclassification] Season/Accounting double-count risk is a real, described, player-visible failure mode, not just an abstract open flag.** `propagation_spec_v1.md` §D.6 + §4.3: if the down/up split isn't ruled disjoint, faction stats double-count and can oscillate, undamped (`decay()` unspecified, OF-3). Failure scenario as above (E7). Severity P1 (consequence); the ruling itself is a known-open item in the spec's §5 register. Intent gate: **UNDETERMINED**, explicitly awaiting Jordan.

6. **[NEW] BG victory params are measurably stale against ratified canon, including a struck victory path.** `params/bg/victory.md` retains Varfell Path C (VTM=5, struck PP-663) and pre-PP-663 VTM/territory thresholds for two co-victories, missing the T13 gate. Failure scenario: player pursues a dead win-condition; strategic layer misjudges co-victory eligibility if built from this table. Severity P1. Intent gate: **NOT-INTENDED**.

7. **[NEW] `params/board_game.md`'s navigational index is entirely broken** (all `params_bg_*` links dead to a nonexistent `references/params_bg_*.md` path; real files at `params/bg/*.md`), and `params/bg/phases.md` contains both an internal contradiction (Hollow Victory "DISSOLVED" vs. still "announced publicly" in the same file) and a dead citation to a nonexistent `designs/board_game/victory_v30.md`. Severity P2. Intent gate: **NOT-INTENDED**.

8. **[NEW] Thread-op CI timing during Hybrid Zoom-Ins is unreconciled with the stated Domain Echo timing asymmetry.** `scale_transitions_v30.md` §10 vs §5.3/PP-109: does CI+1/-1 fire instantly like the "Full TTRPG" case or queue to Accounting like Hybrid Domain Echo? Not stated either way. Severity P2. Intent gate: **UNDETERMINED**.

## Threadwork note (P-14 at these seams)

P-14 ("co-movement cannot be omitted in any play mode," `canon/02_canon_constraints.md` line 23) is **structurally honored, not violated**, at this cluster's Thread seams: `scale_transitions_v30.md` §10 gives Hybrid its own deterministic CI auto-effect table rather than silently dropping co-movement when Thread ops cross into the strategic layer, and explicitly scopes the "BG Co-Movement ceiling" to BG-*initiated* abstraction only — preserving full three-dimensional co-movement for TTRPG-scene ops rather than degrading it (the correct asymmetry: same constraint, mode-appropriate fidelity, not an omission). §5.6's Thread Domain Echo further generalizes "Epistemic CI Trigger (PP-182) to all factions," consistent with P-14's demand that co-movement not be special-cased per faction. The gap is not philosophical compliance but *operational timing*: Finding 8 above (does the CI effect fire same-instant or Accounting-queued relative to that scene's Domain Echo) is exactly the kind of seam where an unstated latency difference could make co-movement's presence feel arbitrary to the player — technically never omitted, but inconsistently *timed* across the two consequence channels of one action. That is the one P-14-adjacent risk worth closing before Godot implementation: not "is co-movement always present" (yes) but "does the player experience it as one coherent physics, or as two clocks that happen to agree in the abstract spec but were never shown resolving together."
