# cluster_C-MBSE

_Evidence cluster dossier, read-only; archived verbatim from the agent's final message by the Fable orchestrator (2026-07-07). Verdicts pending refuter pass + Fable adjudication - see `unaddressed_areas_audit_v1.md`._

# Cluster C-MBSE dossier

Evidence cluster for the 2026-07-07 unaddressed-areas audit. Two THINNER sweeps per charter (`designs/audit/2026-07-07-unaddressed-areas-audit/00_grounding/00_charter.md`): mass-battle playability (first-ever pass) + settlement/strategic keying census. Read-only session; no repo files created/edited/deleted. Sonnet evidence agent, barred from verdicts — findings below are evidence + hypothesis + severity/status tags for Fable's adjudication, not rulings.

---

## A1 RC-5 per-row triage table

Source of truth for "currently failing": `tests/coverage_matrix.md`'s 2026-07-05 entry (ED-MB-0003/PR #84) and `designs/audit/2026-07-04-mass-battle-cannae-gauge-audit/README.md`. **`python tests/sim/gauge_mb.py` was attempted and timed out at 2 min (n=60 × 20 rows × 2 modes, ~1-4 min/mode per prior profiling) — per instructions, fell back to recorded state rather than a partial/truncated run.** Confirmed passing set (5/20, multi mode): **H1, C1, C2, C6, C7**. All 15 remaining rows are failing; grouped below by mechanism.

### Group 1 — Cannae composition rows (DG-1/DG-3-targeted), now WIN-OUT overshoot — individually recorded 2026-07-05, n=30 multi

| Row | Composition | Expected band | Actual (2026-07-05) | Failure-signature hypothesis |
|---|---|---|---|---|
| H3 | `_envelop_army` (pin_frac=1/3, symmetric) vs Line | 55-72, draw<30% | 100/0/0 | DG-3's "intensive" per-troop pool fix (D1 removal) uncapped the enveloping army's per-front pool without any matching reduction on the defender's side; the coverage_matrix's own disclosed-not-chased finding is the leading suspect — spatially-separated attacking fronts (center+2 wings) each roll near-full combat score simultaneously, tempered only by a small `ENCIRCLEMENT_PENALTY` that taxes the *defender*, not the attacker. |
| H4 | `_envelop_army` vs Arrowhead (Cannae proper) | 45-62 | 86.7/6.7/6.7 (val 92.9) | same hypothesis |
| H5 | `_refused_army` vs `_envelop_army` | 48-62 | 83.3/0/16.7 (val 100) | same hypothesis, compounded — **both** sides are now composed armies benefiting from the same uncapped-pool fix simultaneously, an interaction never isolated by any ablation |
| H6 | `_refused_army` vs Line | 48-60 | 96.7/3.3/0 | same hypothesis |
| C4 | `_envelop_army` (pin_frac=2/3 infantry pin + cavalry wings) vs Line | 75-95, draw<30% | 100/0/0 | same hypothesis; C4 was already the sharpest *unexplained* gap pre-fix (RC-3) — it moved from undershoot to overshoot rather than landing in-band, evidence RC-1's fix isn't gauge-scale-sufficient in either direction |

### Group 2 — composition-involving, UNTRIAGED (no individually recorded post-07-05 measurement found anywhere in the corpus)

| Row | Composition | Expected band | Actual | Failure-signature hypothesis |
|---|---|---|---|---|
| H10 | Line vs `_envelop_army` (rev H3) | 28-45 | **not individually recorded** — only folded into the 15/20-fail aggregate | Same DG-1/DG-3 pool mechanism plausibly applies (the composed army sits on side B here), but H10 tests the *inverse* asymmetry — an overshooting enveloper could push `decA` either further out-of-band or accidentally into it. Genuinely unknown without a dedicated re-run; flagged, not guessed. |
| H11 | Arrowhead vs `_envelop_army` (rev H4) | 38-55 | **not individually recorded** | same as H10 |

### Group 3 — RC-5 single-subunit rows, mechanism never diagnosed by any audit pass (8 rows; README's original 9 minus C1, which newly passed 2026-07-05)

| Row | Matchup | Expected band | Actual | Failure-signature hypothesis |
|---|---|---|---|---|
| H2 | Arrowhead vs Line | 48-62 | Only a **stale, pre-`PER_CELL`-flip** note survives (`mass_battle_gauge_grounding.md:101`: "DIVERGE-soft… subtle formation edges washed to ~even by the ED-1013 cohesion pool") | Per README §1 RC-5: "`PER_CELL` pacing/lethality issue in plain, uncomposed fights… this audit did not diagnose it." |
| H7 | GappedLine vs Line | 48-62 | stale-only | same (DIVERGE-soft) |
| H8 | GappedLine vs Arrowhead | 50-65 | stale-only | same (DIVERGE-soft) |
| H9 | Line vs Arrowhead (rev H2) | 38-52 | stale-only | same (DIVERGE-soft) |
| R1 | Ranged Line (hold) vs Line, open field | 0-30, draw<30% | stale note: "loses open-field (directionally correct) but too-drawish" | Ranged-resolution engine gap named directly in the stale note — likely a draw-rate (TOO-DRAWISH) failure, not a direction miss |
| R3 | Ranged vs Ranged mirror | 42-58 | stale note: "mirror unresolvable in 20 turns" | Ranged engagements may not reach decisive resolution within the 20-turn multi-mode cap — a pacing gap specific to `unit_type='ranged'` |
| C3 | Cav vs Cav mirror | 42-58 | **no record at all** — `CAV_TESTS` postdate the pre-flip validation note (cavalry is `PER_CELL=1`-gated), so no historical baseline exists to compare against | Wholly undiagnosed; needs its own dedicated instrumentation, no inherited hypothesis available |
| C5 | Cav vs SHAKEN Line (morale 2/start 6) | 65-98, draw<30% | **no record at all** | same as C3 — wholly undiagnosed |

**Honest read for Jordan's T1 ruling:** RC-1/DG-1/DG-3 explain (with a *new*, still-open* mechanism question) exactly the 5 Group-1 rows. Group 2 (H10/H11) is a real audit gap — nobody re-measured them after the composition-builder changed. Group 3 (8 rows) has never had a single ablation run against it since the `PER_CELL` default flip; the only "hypothesis" on file predates that flip entirely and may no longer apply.

---

## A2 DG-2 status

**"Captured" (Jordan, 2026-07-05, `AskUserQuestion`) means:** DG-2 = *"create as workplan"* — the mechanic is **designed, not implemented**. `designs/proposals/mass_battle_fighting_withdrawal_v1.md` (Status: **PROPOSAL — pending Jordan sign-off before implementation. Not canon yet.**) captures:
- A third state between "eroding" (full commitment) and "routed" (atomic, instant, all-subunit disintegration) — a per-subunit `yielding` state with facing preserved toward the enemy (unlike rout).
- Entry via a discipline-gated `'yield'` order (commanded), with emergent auto-entry flagged **default-off pending measurement**.
- Reuses `_kite_goal`'s reflect vector + the TOI/halt substrate + ED-MB-0001 §6's ratified path-budget formula — explicitly **not** the "recoil/knock-back idiom" the originating audit floated, which PR #84's session confirmed does not exist as a displacement primitive.

**What remains:** everything except the design doc itself. Zero code landed (`grep -c yielding tests/sim/mass_battle/*.py` → no hits confirmed by the D1-D4/D2b fix inventory in PR #84, which touched `orchestration.py`/`hierarchy/units.py`/`percell.py` for unrelated bugs, not this mechanic). The doc's own §0 explicitly sequences DG-2 *after* RC-1's accounting question is stable, reasoning: authoring a yield/displacement mechanic on an unstable pool-accounting floor would be tuning new canon to compensate for still-live bugs — "exactly the band-fitting this repo's discipline forbids." Since PR #84 landed, that floor got *less* stable, not more: the Group-1 WIN-OUT overshoot and the new partition-invariance question (A1 above) mean DG-2 is now double-gated — behind both (a) the original RC-1 stability question the doc already names, and (b) the new, not-yet-ruled partition-invariance question PR #84 surfaced. `HANDOFF_MB.md`'s "Next action: Jordan's ruling on the new partition-invariance question and DG-2's build sequencing" states this correctly but doesn't flag the double-gating explicitly.

---

## A3 MB playability walk

**First-ever playability-lens pass at MB scale.** Prior coverage (`designs/audit/2026-07-05-edge-playability-audit/01_workings/cluster_D_mass_battle.md`, PR #81) audited **cross-scale seams** (E1-E10: Thread↔Mass, Mass↔Personal, Scene↔Mass, Mass↔Faction, Mass↔Settlement, Fieldwork↔Mass, mandatory zoom, Contested Figure, zoom in/out, aftermath) using the same MOMENT/DECISION/FEEDBACK/LATENCY/FRICTION/RECIPROCITY rubric — carried below as KNOWN-TRACKED, not re-litigated. What cluster D did **not** cover: the in-scale experience — deployment and the battle's own moment-to-moment resolution. This walk fills that gap, from Army Configuration Mode (Stage E MVP) through aftermath.

**Currency:** `designs/provincial/mass_battle_v30.md` (+ `_integration_v30.md`), confirmed via `CURRENT.md:27`.

### MB-P1 · Army Configuration Mode (deployment)
1. **MOMENT** — Click-to-place: choose shape/troop-type/role/tier/troop-count per subunit, click the canvas to place it, build a roster up to `SUBUNIT_CAP=11` per side (`tests/sim/mass_battle/workbench/static/index.html:88-140`, `server.py:19-38`).
2. **DECISION** — Real but implementation-facing, not player-facing: no resource/Treasury cost to muster, no fog-of-war (both sides' full composition visible while building), no Command-derived cap (flat 11 regardless of the general's Command stat, contrast §A.5), no tactic-card selection (Envelopment/Feigned Retreat/Ambush/Concentration/Refused Flank/Hammer & Anvil, §A.8, are not exposed choices — they're baked into which preset builder function you invoke).
3. **FEEDBACK** — Good at the tool level: a live roster list with cap counter, canvas schematic redraw on every placement.
4. **LATENCY** — Immediate, synchronous.
5. **FRICTION** — None modeled (no AP, no Muster action, no season cost) because this is not a game surface.
6. **RECIPROCITY** — N/A; this is a single-operator authoring tool, not a two-sided game state.
7. **VERDICT** — **This is not a player-facing surface at all.** `index.html:2`: `<title>Mass-Battle Workbench — tick-by-tick visualizer</title>`. It is the same class of artifact as `tests/sim/` generally: a Python/HTML developer tool for validating the engine, explicitly the surface "Jordan actually watches" per `HANDOFF_MB.md`, not a Godot player UI. The Godot port has not begun mass battle: per `CLAUDE.md §6`, the skeleton covers 1/27 modules (`personal_combat`), none of it mass battle. **The only text describing what a *player* sees/decides during army configuration is §A.7 Phase 1's prose** (below) — there is no implemented surface, dev or player-facing, that matches it.

### MB-P2 · During the battle (turn resolution)
1. **MOMENT** — Per design (`mass_battle_v30.md §A.7`): 7 phases/turn — Strategy Declaration (secret, simultaneous: sub-unit assignment, formation, tactical action, Thread intent, Offence/Defence split) → Volley → Manoeuvre → Offensive Thread → Engagement → Cascade → Reform.
2. **DECISION** — Per design, real and per-phase (Phase 1 tactic/split declaration, Phase 3 Reserve commitment, Phase 4 Thread targeting). **Per the only implemented surface (the workbench):** zero. "Run traced battle" is a single deterministic auto-resolve call; there is no Phase-1 declaration UI, no per-phase interrupt, no tactic selection, no Thread-intent declaration. Once launched, the player's only input is a playback scrubber.
3. **FEEDBACK** — The workbench's tick-by-tick replay (facing-color-coded canvas, HP bars, an event log) is a genuinely strong *trace* surface — better than most seams in this corpus. But it is retrospective only: you watch what already happened, you do not steer it.
4. **LATENCY** — N/A to the design's phase structure (the workbench does not implement phases as player-visible beats at all — see it wholesale as one opaque simulation tick sequence, then a replay).
5. **FRICTION** — None — because there is nothing to do.
6. **RECIPROCITY** — N/A.
7. **VERDICT** — **MISSING as a player-decision surface.** The rubric's MOMENT/DECISION axes have a real answer only in TTRPG prose; the only executable implementation collapses the entire 7-phase turn structure into a single deterministic auto-resolve with a replay-only trace. Tie-in to A1: even where a player's tactical choice *is* legible (e.g., choosing an envelopment composition), 5 of the 6 currently-measured Cannae-pattern rows now resolve as historically-implausible curbstomps (WIN-OUT, 0-3% draw) rather than the contested outcome the historical grounding intends — so even a hypothetical future UI exposing this decision would currently hand the player an outcome the corpus's own gauge says is miscalibrated.

### MB-P3 · Aftermath / named officers
1-6. **Per design** (`mass_battle_v30.md §D.1/§D.2`), this is genuinely excellent: a mandatory, free Aftermath scene with three real choice points (Tend the Wounded/Survey/Address the Population, each a different stat+skill with named consequences), named officer NPCs generated at Muster with Disposition tracking, a legible 1d20-vs-total-Size-loss incapacitation formula with a worked example, capture/ransom/governor-transition/companion-eligibility follow-through, and a graceful non-participation branch ("Where Were You?"). Cluster D's **E10 already rated this PLAYS-WELL — "the best-integrated seam in this cluster"** (KNOWN-TRACKED, not re-litigated).
7. **VERDICT (sharpened, NEW angle cluster D did not check):** Cluster D audited *spec quality* via the cross-scale-transition rubric. This pass checked *implementation presence* and found **none**. Direct grep across `sim/` and the workbench confirms zero hits for aftermath/officer/incapacitation logic except a single, narrower mid-battle stub: `orchestration.py:1428-1430`'s `Command=0 → instant rout` general-incapacitation check (§A.5's *in-battle* consequence, not §D.2's *post-battle* capture-roll apparatus). The workbench's UI stops at a "winner" banner (`index.html:401,412`) — no aftermath scene, no officer roster, no disposition tracking anywhere in the executable corpus. **The best-specified seam in the whole cluster is currently 0% implemented**, in either the Python sim or the (nonexistent) Godot port. This compounds with cluster D's own CF4 (`scene.battle_concluded` missing from the Tier-2 articulation trigger table, KNOWN-TRACKED P2): even a built aftermath scene would not register as a narrative-significant beat today.

---

## B4 keying census (transition site · doc § · candidate key type)

Ground truth cross-checked directly against `references/module_contracts.yaml` (not just the design docs), which turns out to matter: the three ED-IN-0014 targets are **not uniformly thin** — settlement_layer and victory already have `gates:` scaffolding (empty `emits:`), while ci_political has **no gate scaffolding at all**, only a `gap_notes` mention. This changes the shape of the keying work per-module, which matters directly for armature §3.

| Transition site | Doc § | Contract state (module_contracts.yaml) | Candidate key type (illustrative, unratified) |
|---|---|---|---|
| **Settlement Order → 0, local revolt** | `settlement_layer_v30.md §1.3, §4.3` — "Order 0 \| Local revolt… Governor expelled unless garrison present" | Gate `g_ord0` **exists** (`:556-560`), but shares an undifferentiated `emits: [{type: env.population_change, terminal: false}]` with the whole module — no gate-specific emit | `state.settlement_revolt` (mirrors the existing `state.coup_attempted`/`state.succession` naming already in the registry per cluster E's E4) |
| **Settlement Defense → 0, undefended auto-capture** | `settlement_layer_v30.md §5.2` — "Ungarrisoned settlements with Defense 0 are auto-captured on any hostile military entry — no roll needed" | Gate `g_def0` **exists** (`:561-565`), same undifferentiated-emit gap | `mechanical.settlement_captured` (auto-capture path) — distinct from an Assault/Siege capture, which has its own decision content worth a separate type |
| **Siege → Order 0 → surrender** | `settlement_layer_v30.md §5.1` — "Each season: defender Order −1… When Order = 0, settlement surrenders" | **No gate id at all** — this is a different trigger from `g_ord0` (siege-caused vs generic revolt) but the contract doesn't distinguish them | `mechanical.settlement_surrendered` (siege-specific, so causes[] can distinguish "starved out" from "revolted") |
| **L/PS mean-reverting drift → Mandate feedback** | `settlement_layer_v30.md §1.8` — "±1/settlement/season toward Mandate" | **No gate id at all** — modeled only in `loops:`/`derivations:` (`:554,593-596`), not as a discrete transition | `state.legitimacy_drift` — needs a *new* transition-site entry authored from scratch, not just an emit clause added to an existing gate |
| **Derived-value-held-at-0 (Local Economy/Garrison Strength/Public Order)** | `settlement_layer_v30.md §1.3` | Gate `g_dv0` **exists** (`:566-570`) | `state.settlement_stat_collapse` |
| **CI milestone crossings 40/55/65/80/100** | `ci_political_v30.md §2.1` (**verified table: 40/55/65/**80**/100 — see Finding C-MBSE-12 below, a real discrepancy with ED-IN-0014's own "40/55/65/**75**" citation**) | `ci_political` module has **`consumes: [], emits: [], transitions: [], loops: []`, and no `gates:` key at all** (`:628-644`) — the thinnest of the three targets; only a `gap_notes` line names the CI-100 event | `mechanical.ci_milestone_crossed` (payload: threshold value) — needs *gate scaffolding authored from nothing*, not just an emit clause |
| **CI 100, Theocracy Unification Attempt** | `ci_political_v30.md §2.2` | same — no gate, only `gap_notes:641` | `mechanical.theocracy_unification_declared` |
| **Card play → Cooldown Track → return to hand** | `ci_political_v30.md §5.1-§5.3` — cards placed on Cooldown at play, −1 slot/Accounting, return to hand at 0 | Tracked only as opaque `state: {name: "card hands / cooldown", bucket: track}` (`:637`) — no per-event transition modeled | `state.card_cooldown_expired` / `state.card_played` |
| **MS = 0 → Post-Calamity Era** | `victory_v30.md §5.1` | Gate `g_ms0` **exists** (`:658-662`) | `mechanical.era_transition` (payload: `post_calamity`) |
| **MS ≤ 5 sustained 10 seasons → Second Calamity (true terminal)** | `victory_v30.md §5.1` | Gate `g_ms5` **exists** (`:663-667`) | `mechanical.second_calamity` — the game's only true terminal deserves its own type, not a generic era tag |
| **MS restored to 20 within 10 seasons → recovery** | `victory_v30.md §5.1` | Gate `g_msrec` **exists** (`:668-672`) | `mechanical.era_transition` (payload: `post_calamity_recovered`) |
| **IP = 100 → Phased Occupation Era (3 sub-phases)** | `victory_v30.md §5.2` — First Mountain Pass / Schoenland corridor / Northwest Pass, each with its own sustain-threshold | **No gate id exists**, despite `gap_notes:679` naming this exact transition by name ("IP=100 Phased Occupation… UNKEYED") — an internal inconsistency in the contract itself: g_ms0/g_ms5/g_msrec/g_diss all got gate entries, this one didn't | `mechanical.era_transition` (payload: `occupation_phase_1/2/3`) |
| **IP visibility milestones 60/80/90** | `victory_v30.md §5.2` — named Scene Slate beats with in-fiction text | No gate; not even named in `gates:` | `mechanical.ip_milestone_crossed` |
| **All factions dissolved → Anarchy Era** | `victory_v30.md §5.3` | Gate `g_diss` **exists** (`:673-677`) | `mechanical.era_transition` (payload: `anarchy`) |

**KNOWN-TRACKED baseline:** EP-4 (settlement zero-Key blackout), EP-5 (best-authored beats stranded), ED-IN-0014 (files exactly this keying work, citing `registry §10 already flags two of the three` — **could not corroborate**: `key_type_registry_v30.md §10` is generic "Extension Process" boilerplate, not per-system candidate flags; either a different §10 was meant or this is stale — flagged, not chased further).

---

## B5 event-deck readiness

**What the deck must contain** (`designs/territory/governance_play_redesign_v1.md` Part 2, PROPOSAL 2026-06-22): a stateful, pressure-driven card engine, not a random table —
- A per-settlement **Pressure scalar Π (0-10)**, homeostat-governed: `Π_next = clamp(Π + Σunserved-Needs + Σactive-Grudges + ΣNPC-ambitions-in-motion + shock − Σplayer-releases, 0, 10)`, drawing `1 + ⌊Π/3⌋` cards/season.
- A **YAML card schema** (`id, family, triggers[], weight, cooldown, excludes[], the_ask, responses[], follow_on`) across **7 families**: Petition, Friction, Opportunity, Crisis, Intrigue, Ambition, Thread.
- A **Ledger tag system** (Precedent/Grudge/Debt/Reputation/Leverage) that persists across governor succession.
- An **NPC ambition engine** (autonomous per-Accounting progress, firing Ambition cards at threshold) and a **Directive generator** (mandatory faction-issued order each season, with Comply/Bargain/Defy responses).
- This is explicitly named as **"the canonical home for the §4.3 settlement events, generalized from 8 hard-coded rows into an open, stateful, GM-/sim-authorable card set"** (`governance_play_redesign_v1.md:147`) — i.e. it is meant to *subsume*, not sit beside, the transition sites cataloged in B4's settlement rows.

**What exists** (verified this session — `sim/territory/` + a live pytest run):
- **G1 (settlement registry) is built and tested**, exactly as ED-SE-0001/R-5 claim: `sim/territory/registry.py` (148 lines — `Settlement` dataclass, `register_settlement`/`get_settlement`/`province_members`/`province_accord`/`succeed_governor`) + `sim/territory/ledger.py` (75 lines — `LedgerTag` with all 5 kinds from §1.6: Precedent/Grudge/Debt/Reputation/Leverage, dedupe-by-`(kind,key)`, single-valued Reputation, TTL sweep). **`pytest tests/sim/territory_registry/test_registry_ledger.py -q` → 6 passed** (run directly this session, ~0.05s): `test_ap_economy`, `test_ledger_survives_succession`, `test_reputation_single_valued`, `test_multi_settlement_province_aggregation`, `test_registry_backed_derived_values`, `test_backward_compat_fallback`. This is the goldenfurt_slice README's "S0-S1" milestone.
- A **fully-authored, adversarially-verified content pack** already exists as design content (not yet wired to any engine): `designs/territory/goldenfurt_slice/` — `event_deck.md` (28 cards across all 7 families: Petition 3, Friction 5, Opportunity 3, Crisis 4, Intrigue 5, Ambition 6, Thread 2) + `npc_cast.md` (6 collision-wired NPC dossiers + 3 minor actors) + a documented 4-lens adversarial pass (32 findings, 15 high; some fixed in v1.1, some — predicate-grammar triggers, an empty Wessel/Greta collision card, decorative-Knot wiring, ethic mechanization, numeric tuning — still open pending a "§9 sim sweep" that itself needs the unbuilt engine below).

**What's missing for narrative Stage 2.5's precondition:** everything past the registry/ledger. Direct grep across all of `sim/` for `Pressure|Directive|ambition|EVT-S|card_store|event_deck|homeostat` → **zero hits outside the design docs.** Per the goldenfurt README's own S0-S6 sequence: S2 (governance verbs + full AP economy — partially scaffolded, `test_ap_economy` exists but the 8-verb menu isn't implemented), **S3 (Directive generator + Comply/Bargain/Defy) — not started**, **S4 (deck engine + Π homeostat) — not started**, **S5 (NPC ambition tick) — not started**, **S6 (port the 28-card Goldenfurt pack to runnable YAML) — not started**. `designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:162-167` names "the unbuilt event deck" as one of Stage 2.5 Layer B's explicit preconditions (alongside ~19 sim stubs, the `canonical_key_log` spec, and a deterministic seeded smoke oracle), and `designs/workplans/valoria_master_workplan_v6.md:195-198` confirms directly: **"no deck code exists yet, and Stage-2.5 Layer B lists it as a precondition, so SE's deck work is on the M2 critical path even though SE itself is not M1-gating beyond juncture 1's venue."** This is a hard cross-lane dependency, not SE-lane housekeeping.

---

## Findings (C-MBSE-1..15)

| # | Claim | Severity | Status | Evidence |
|---|---|---|---|---|
| C-MBSE-1 | RC-5's 8-row residual (H2,H7,H8,H9,R1,R3,C3,C5) remains completely undiagnosed post-ED-MB-0003; the only mechanism notes on file predate the `PER_CELL` default flip and may no longer apply. | P2 | KNOWN-TRACKED (README §1 RC-5; `HANDOFF_MB.md` "separate, not-yet-opened lane item") | README §1, `mass_battle_gauge_grounding.md:101` |
| C-MBSE-2 | H10/H11 use the same `_envelop_army` composition builder DG-1/DG-3 rewrote, but were silently omitted from every post-fix measurement table (both the 07-04 and 07-05 "honest gauge result" tables and the RC-5 list) — an audit gap by omission, not by mechanism. | P2 | NEW | `gauge_mb.py:227-228`; absent from `coverage_matrix.md:341-448` and README §1 |
| C-MBSE-3 | The 5 Cannae composition rows now systematically overshoot (WIN-OUT) rather than land in-band; root cause is explicitly flagged-not-decided (spatially-separated fronts each rolling near-full pool, encirclement tax falling on the defender not the attacker). | P1 | KNOWN-TRACKED (ED-MB-0003 ledger entry, `coverage_matrix.md:433-442`) | `canon/editorial_ledger.jsonl:587` |
| C-MBSE-4 | DG-2 is double-gated (behind both the original RC-1-stability question its own doc names, and the new partition-invariance question PR #84 surfaced) — `HANDOFF_MB.md`'s framing is accurate but doesn't state the double-gating explicitly. | P2 | NEW (nuance on a KNOWN-TRACKED status) | `mass_battle_fighting_withdrawal_v1.md §0`; `coverage_matrix.md:433-445` |
| C-MBSE-5 | Army Configuration Mode (Stage E MVP) is a developer visualizer, not a player-facing surface — no resource cost, no fog-of-war, flat (not Command-derived) subunit cap, no tactic-card selection; the Godot port has not begun mass battle (0/27 contract modules). | P1 | NEW (first playability pass at MB) | `index.html:2` title tag; `CLAUDE.md §6` (1/27 modules skeleton) |
| C-MBSE-6 | The battle's "during" experience has zero implemented player decision points — the 7-phase §A.7 turn structure (secret Phase-1 declaration, per-phase tactics, Thread intent) collapses to one deterministic "Run traced battle" button; only a post-hoc replay trace exists. | P1 | NEW | `mass_battle_v30.md §A.7`; `index.html` battle-launch code (no phase-gated input) |
| C-MBSE-7 | The Aftermath/Named-Officer apparatus (§D.1/§D.2 — cluster D's E10 "best-integrated seam") has zero implementation anywhere in the executable corpus; only a narrower mid-battle general-incapacitation stub exists. | P1 | NEW (sharpens KNOWN-TRACKED cluster-D E10, which audited spec quality not implementation presence) | `orchestration.py:1428-1430`; zero grep hits for aftermath/officer in `sim/` or workbench; `index.html:44,401,412` (winner-banner only) |
| C-MBSE-8 | Even a built aftermath scene wouldn't register as a narrative-significant beat (`scene.battle_concluded` missing from the Tier-2 articulation trigger table). | P2 | KNOWN-TRACKED | cluster D CF4, cites confirmed prior finding `articulation-battle-concluded-trigger-gap` |
| C-MBSE-9 | settlement_layer's three transition gates have differentiated conditions but share one undifferentiated `emits:` clause at the module level — a gate-specific emit is needed per site, not one module-wide patch. | P1 | NEW (armature-actionable detail on KNOWN-TRACKED EP-4) | `module_contracts.yaml:545-570` |
| C-MBSE-10 | The L/PS mean-reverting drift (§1.8) has **no gate id at all** in module_contracts.yaml — modeled only in `loops:`/`derivations:` — so the keying work must author a wholly new transition-site entry here, not just add an emit clause. | P2 | NEW | `module_contracts.yaml:552-554,593-596` |
| C-MBSE-11 | ci_political has **zero gate scaffolding** (`consumes:[], emits:[], transitions:[], loops:[]`, no `gates:` key) — unlike settlement_layer/victory, which at least have empty-but-present gate entries. ED-IN-0014's "emission wiring, not design" framing understates ci_political specifically: the gate structure itself doesn't exist yet either. | P1 | NEW (sharpens KNOWN-TRACKED EP-5) | `module_contracts.yaml:628-644` |
| C-MBSE-12 | A verified numeric discrepancy: ci_political_v30.md §2.1's mechanical CI milestone table reads **40/55/65/80/100**, but conviction_track_v30.md §11.3's presentation table reads **40/55/65/75** (a different threshold, for a similarly-named Seizure-related transition) — neither doc cites the other, and this "75" was carried unverified into both cluster E's dossier and ED-IN-0014's own filed description. Additionally, the presentation table stops at 75 — it never narrates the mechanically-more-consequential CI 80 ("Church Ascendant") or CI 100 (Theocracy Unification Attempt) milestones at all. | P2 | NEW | `ci_political_v30.md:78-85` vs `conviction_track_v30.md:511-520` (both read directly this session) |
| C-MBSE-13 | victory's `gates:` list has entries for MS-related transitions and all-dissolved, but **no gate id for IP=100 Phased Occupation** (or its 3 sub-phases, or the IP 60/80/90 milestones) — despite the module's own `gap_notes` naming this exact transition as unkeyed. Internal inconsistency in the contract file itself. | P2 | NEW | `module_contracts.yaml:657-679` |
| C-MBSE-14 | The event-deck build ladder (S0-S6) has S0-S1 done and independently verified (6/6 tests passing, run directly this session), S2 partially scaffolded, S3-S6 entirely unbuilt (zero engine-content grep hits) — and this is now confirmed a hard M2 critical-path blocker via Stage 2.5 Layer B, not SE-lane housekeeping. | P1 | KNOWN-TRACKED core (ED-SE-0001, R-5, workplan v6 SE row); NEW is the direct S2-S6 grep confirmation + live test run | `sim/territory/registry.py`, `ledger.py`; `goldenfurt_slice/README.md:79-87`; `valoria_master_workplan_v6.md:195-198` |
| C-MBSE-15 | A fully-authored, adversarially-verified 28-card deck + 6 NPC dossiers already exists as design content (goldenfurt_slice) — the B5 gap is build-execution, not authoring-from-scratch — but that content carries its own disclosed, still-open residue (predicate-grammar triggers, an empty collision card, decorative-Knot wiring, ethic mechanization, numeric tuning) gated on the same unbuilt engine. | P2 | NEW | `goldenfurt_slice/README.md:72-83` |

---

## Honest gaps

- **`gauge_mb.py` did not complete in the ~2-minute budget** (aborted at 115s / 2min per instructions); A1's "actual" values for 10 of 15 failing rows (H10, H11, H2, H7, H8, H9, R1, R3, C3, C5) are **not independently re-verified this session** — several (H10, H11, C3, C5) have no individually recorded value anywhere in the corpus at all, and this is stated explicitly in the table rather than inferred or estimated.
- `tests/valoria`'s full suite was not re-run this session (relied on PR #84's recorded "88 passed/16 skipped/1 xfailed"); only the narrow `territory_registry` test file was run directly (6/6 passed, confirmed live).
- ED-IN-0014's "registry §10 already flags two of the three" claim could not be corroborated — `key_type_registry_v30.md §10` is generic extension-process boilerplate, not per-system candidate flags. Possibly refers to a different location or is itself stale; flagged, not chased further (thinner-sweep scope).
- B4's picture leans on `module_contracts.yaml` (read directly, line-cited) plus targeted design-doc excerpts; it does not independently re-verify every cluster-D/E line citation against the working tree byte-for-byte — those citations are carried as KNOWN-TRACKED per the charter's non-duplication rule, with re-verification being the orchestrator/refuter's job, not this cluster's.
- The B4 "candidate key type" column is illustrative only (naming-convention-matched to existing registry families `mechanical_event`/`state_transition`/`env`/`da`/`scene`), not checked against the full `key_type_registry_v30.md §4/§5` membership for collision or PP-674 Class-B vetting — filing is explicitly out of scope for this read-only cluster.
- A3's playability walk is a single-pass document/source read, not a played or traced session — it inherits the charter's own standing caveat (gap class 2: "all playability verdicts are paper-walks; no human-plays evidence anywhere").
- `tests/sim/mass_battle/workbench/server.py` was grepped, not read in full — the "zero aftermath logic" claim rests on a clean string-match absence (`aftermath`/`officer`) rather than a complete manual read of the battle-resolution glue code.
