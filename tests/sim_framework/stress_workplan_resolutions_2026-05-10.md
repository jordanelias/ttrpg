---
title: Stress-Test Workplan Resolutions — Q1–Q25
date: 2026-05-10
session_token: 1096c009dd81e221
parent: tests/sim_framework/stress_test_workplan_2026-05-10.md
authoring_model: Claude Opus 4.7
directive: Jordan "resolve all, no naval" (2026-05-10)
---

# Stress-Test Workplan Resolutions

> **Scope.** Resolves Q1–Q25 from `stress_test_workplan_2026-05-10.md §7`. Naval (Q1) dropped per Jordan directive. The remaining 24 Qs are resolved via three routes: (1) **canon-grounded** — already specified in fetched canon, prior workplan §7 question reflected outdated knowledge; (2) **proposed** — canon silent or partial, this document proposes a specific resolution with rationale, ranked alternatives, fallback; (3) **superseded** — the original gap has been obsoleted by later canon (PP-460, PP-605, PP-510, Royal Crisis fuse, graduated autonomy, AER removal).
>
> **Workplan impact.** Several Qs collapse, merge, or drop entries in the workplan. §"Workplan deltas" at the end enumerates every change to V1.0 → V1.1.
>
> **Authority.** This document proposes. Jordan ratifies. Per project-owner contract, canonical adoption requires Jordan's explicit acceptance — typically by PP- commit against the affected params/canon/design path, or by terse confirm-and-proceed in a follow-on session.

---

## Resolution legend

| Tag | Meaning |
|---|---|
| **RESOLVED ✓** | Canon already specifies the answer; original Q reflects outdated knowledge. No design action required. |
| **SUPERSEDED ↻** | Original gap obsoleted by later PP/ED. Map old → new and update workplan references. |
| **PROPOSED →** | Canon silent or partial. Specific resolution recommended with rationale; alternatives considered; Jordan to ratify. |
| **DROPPED ✕** | Out of scope per Jordan directive. |

---

## Q1 — ED-055 naval scope ✕ DROPPED

**Directive:** "no naval."

**Workplan impact.**
- §4 W1.1 (ED-055 closure) deleted from W1 stress module list. W1 retains only land-based modules (W1.2 terrain NERS, W1.3 cross-scale terrain).
- §4 S1.5 (naval gap closure / carve-out) becomes permanent carve-out. Coastal scenarios deleted from S1 scope. Schoenland-pivot scenarios marked out-of-scope.
- §5 Phase 4 W1 entry adjusted to "land-only verification."
- §7 Q1 row removed; resolution timeline shortens.
- Schoenland-as-tributary remains in canon but with no naval-projection mechanic; this is consistent with the existing Schoenland T16 status ("not in play" per faction starting stats in `params/bg/core.md`).

**Cross-affected systems unblocked:** S1 (mass combat), W1 (geography) can now both proceed in Phase 4 without ED-055 dependency.

---

## Q2 — B4 #11 Coup Counter advancement source events ↻ SUPERSEDED

**Original Q:** What events advance the Löwenritter Coup Counter, and by how much?

**Investigation.** `params/bg/core.md:87–99` documents **Löwenritter Graduated Autonomy** with this introducer: *"Graduated autonomy (conflict_architecture_proposal). **Replaces binary Coup**."* The mechanic is a 4-stage state machine (Loyal → Restless → Autonomous → Split), not a counter accumulating from sources. Triggers per stage are spelled out:

- **Loyal → Restless:** Crown Stability ≤ 3, **OR** no military action 4+ seasons, **OR** Crown loses a province.
- **Restless → Autonomous:** Crown Stability ≤ 2, **OR** Ehrenwall Disposition toward Almud < 0, **OR** 4+ seasons Restless without resolution.
- **Autonomous → Split:** Crown attacks Löwenritter, **OR** Crown eliminated, **OR** 4+ seasons Autonomous without resolution.

Plus an explicit Reversal rule: stages 1–3 are reversible.

**Verdict.** **B4 #11 is obsolete.** The binary-coup-counter model no longer exists in canon. The graduated-autonomy state machine replaces it.

**Workplan impact.**
- §4 **S8 renamed** "Löwenritter Coup" → "Löwenritter Graduated Autonomy."
- §4 **S13 merges into S8.** S13 was tagged "proposed; needs engine_v4" but the canon is actually live in `params/bg/core.md` (not deferred). S13 entry dissolved; its content folded into a unified S8 stress plan.
- §4 S8 stress modules updated:
  - S8.1 (spec gap closure) → strike (no gap).
  - S8.2 (V1 mechanism validation) → validate the 4 stages + 9 triggers + reversal rule per canon.
  - S8.3 (V3 interaction chain) → graduated transitions interact with Crown Stability, Ehrenwall Disposition, military activity tempo, Crown territorial holdings, and PI track effects. Test the full coupling map.
  - S8.4 (V4 NERS) → boundary: Crown Stability oscillates 2/3/2/3 (boundary trigger thrash); cascade: simultaneous trigger from multiple conditions; ambiguity: 4+-season trigger when 3.5 seasons elapse before reversal then thread breaks; optimal play: can Crown intentionally stall Restless by maintaining marginal Stability?
  - S8.5 (V12 narrative emergence) → does each stage transition read as Löwenritter character development or as state-machine tick?
  - **New S8.6 (V8 convergence):** under hostile player input, does the autonomy state ever deadlock? E.g., Crown blocks Reversal paths while Restless trigger remains marginal.

**Confidence.** High.

---

## Q3 — B4 #12 Coup effect on Crown Mandate ↻ SUPERSEDED

**Original Q:** What is the canonical effect of a successful coup on Crown Mandate?

**Investigation.** Same canon section. Effects are per-stage on Crown:

- **Restless:** Crown +1 Ob offensive deployment; T14 status: S014 Barracks follows Löwenritter orders for defensive actions only.
- **Autonomous:** Crown Military reduced by T14 garrison; cannot access Fort 3; **PI −1**.
- **Split:** Crown loses T14, **PV drops by 3**, **PI −3**. Löwenritter becomes a separate playable faction with M3/I2/W3/Mil6/Stab5.

No direct Mandate (L or PS) penalty in the state machine. The PI and PV effects are the canonical strategic-impact channels.

**Verdict.** **B4 #12 superseded — the question itself assumed the wrong mechanic (binary coup) and the wrong output axis (Mandate).** Canonical effect channels are: PI, PV, T14 status, Military access. Mandate is downstream (PI changes affect long-term faction state but not directly).

**Workplan impact.** S8.2 module covers verification. No separate Q3-driven module needed.

**Confidence.** High.

---

## Q4 — B4 #13 Seizure Failure consequences ✓ RESOLVED

**Original Q:** What are the consequences of a failed Mass Seizure (Stability −1 + Casus Belli chain)?

**Investigation.** `params/bg/ci_seizure.md:57–58`:
- *"Failure: Stability −1."*
- *"Political cost: Casus Belli granted to controlling faction on every seizure attempt. (See §Casus Belli.) (PP-510)"*

And `params/bg/ci_seizure.md:60`: *"Battle requirement: If the target territory has a garrison... Church must first win a Battle before Seizure proceeds. If Church wins: Seizure roll proceeds immediately. If Church loses: no Seizure this season; Casus Belli still granted."*

**Verdict.** **Canon explicit.** Both consequences enumerated: Stability −1 on Seizure failure, Casus Belli on every attempt (success or failure) per PP-510. ED-355 and related EDs explicitly marked RESOLVED in the file.

**Workplan impact.**
- §4 S5.2 Module remains as drafted; remove "open finding" framing since the spec is closed.
- §4 S5.1 (post-PP-716 propagation check) unchanged.
- §4 S5 priority **demoted from P2 to P3 except for V8 convergence** — primary mechanic is mature; only systemic-cycle and cross-system stress remain.
- §5 Phase 5 S5 entry effort halved (0.5 session, not 1).

**Confidence.** High.

---

## Q5 — B4 #14 Treaty × Strain recovery interaction → PROPOSED

**Original Q:** How does the Treaty mechanic interact with Strain recovery? Canon silent.

**Investigation.** Treaty is canonical (`Formal Crown Treaty (Senator Outward)` at `params/bg/core.md:215`; `Diplomatic Token (PP-517/521)` at `faction_actions.md:126,357`). Strain table is canonical (`params/bg/core.md:140`): Peace/Tension/Fracture/Crisis/Collapse bands at 0–10 with effects. Strain sources are canonical (`peninsular_strain_v1.md §3` referenced from `params/bg/clocks.md`):
- Battles on Valorian soil: MS −1 (MS −2 Campaign/War).
- Inter-faction battle each season: IP +2; Turmoil +1.
- Faction elimination: Strain +2.
- Territory Revolt (Accord 0): Strain +1.
- Covert / ungarrisoned Church Seizure: no MS/IP/Strain cost.

**No explicit Treaty→Strain interaction** appears in fetched canon. The B4 finding is correct: this is a gap.

**Proposal (PROPOSED →).** Add Treaty integration with Strain via two channels:

1. **Active Treaty between two factions suppresses Strain accumulation from inter-faction battle between those factions.** Active Treaty implies no battle by definition; this clause is principally housekeeping: if a Treaty is active and a battle occurs anyway, the battle automatically breaks the Treaty (Diplomatic Token removed) and the Strain advance fires normally. No double penalty.
2. **Treaty violation event = Strain +1 single tick.** Defection is a Strain source. When Diplomatic Token removed via "military conflict with Hafenmark — any season either party initiates" (existing canonical clause at `faction_actions.md:126,357`), the removing event also adds +1 to current Strain. This places Treaty violation at the same severity as territory revolt or arc-level event.

**Rationale.** The proposal works entirely within existing canon: it does not invent a new mechanic, just couples two existing systems. Treaty already has explicit termination conditions; Strain already has explicit advancement sources. The B4 gap was about the absence of a coupling — this proposal supplies it minimally.

**Alternatives considered.**
- **(A) No coupling (canon-silence as canonical).** Rejected: Treaty defection is a major political event with no Strain consequence; that gap is the actual concern B4 flagged.
- **(B) Strain decay accelerated by active Treaty (e.g., −0.5/season per Treaty active).** Rejected: introduces fractional Strain (existing system is integer-only); adds new mechanic surface where the symptom is just under-coupled-defection.
- **(C) Treaty grants Strain immunity to its parties.** Rejected: too strong; gives Treaty an exploit (faction A treaties with everyone, immune to Strain crisis effects).

**Fallback.** If Jordan rejects: minimal version is **just clause (2)** — Treaty violation = Strain +1. Clause (1) is housekeeping and can be implicit if explicit causes confusion.

**Workplan impact.**
- §4 S7 stress module S7.1 (block-on-canon) replaced with V1 spec validation against this proposal.
- §4 S7 priority P1 → P2 once accepted.
- §7 Q5 row removed; resolution timeline shortens.

**Confidence.** Medium — the proposal is canon-coherent, but Jordan may have a more specific narrative-design intent for Treaty (e.g., Treaty as binding contract with bespoke break-conditions per pair). Ratification needed.

---

## Q6 — B4 #8 AER generation mechanic ↻ SUPERSEDED

**Original Q:** AER (Altonian Ecclesiastical Relationship) generation mechanic — not in any read doc.

**Investigation.** `params/bg/tracks.md:13`:
> *`<!-- [REMOVED 2026-05-04] AER (Altonian Ecclesiastical Relationship) track removed. Church-Altonian diplomacy → Altonian hooks. -->`*

**Verdict.** **AER was removed from canon on 2026-05-04.** Church-Altonian diplomacy now flows through Altonian hooks (not a dedicated track). B4 #8 is obsolete.

**Workplan impact.**
- §4 S9 (Altonian Vanguard / IP) — drop AER from gap list. The S9.1 module's "AER generation" line removed.
- §7 Q6 row removed.

**Confidence.** High.

---

## Q7 — B4 #9 Warden emergence behavior post-RS40 ↻ SUPERSEDED

**Original Q:** Warden emergence post-Realm-Stability-40 behavior undefined.

**Investigation.** `params/bg/core.md:99–100` documents canonical Warden tracks (PP-605):
- **Warden Cooperation (WC):** 0–3, Peninsula-wide. **Requires WR ≥ 2 to advance.**
- **Warden Recognition (WR):** 0–3, **Varfell-only private track. Gates WC.**

WC effects table at `params/bg/core.md:148–152`:
- WC = 0: no effect.
- WC ≥ 1: +1D to all Thread operations peninsula-wide.
- WC ≥ 2: MS decay rate halved (−1/season becomes −0.5, rounded down).
- WC = 3: MS +2/season at Accounting.

**Verdict.** **PP-605 resolves the structure.** Warden involvement is gated by Varfell-private WR track (gates) → peninsula-wide WC track (effects). The B4 gap predated PP-605's introduction of this two-track gating; "post-RS40 emergence" reflected an earlier single-trigger model that PP-605 replaced.

**Note.** "RS40" in B4 likely referred to the **MS 59–40 band** (Mending Stability), per the MS effects table in `params/bg/clocks.md`. The MS-band-vs-WC-track relationship is canonical via WC effects: low MS triggers Wardens because WC effects on MS decay are conditional on the band, not the inverse. The B4 framing inverted causation.

**Workplan impact.**
- §4 S9 — drop "Warden emergence post-RS40" from gap list.
- §4 add stress modules to S9 covering WC/WR coupling:
  - **S9.6 — V3 WC × WR × MS interaction chain.** Verify WR (Varfell-private) gates WC (peninsula-public); MS decay modulated by WC.
  - **S9.7 — V4 NERS WC = 3 boundary.** MS +2/season at Accounting — does this stabilize MS or thrash it?
- §7 Q7 row removed.

**Confidence.** High on PP-605 supersession; Medium on RS40-as-MS-band interpretation (text is ambiguous; new modules covers either reading).

---

## Q8 — B4 #10 Campaign-scale vs standard battle distinction → PROPOSED (canonize proposal)

**Original Q:** Campaign-scale vs standard battle distinction — not formally specified.

**Investigation.** `params/mass_combat.md:223` documents `## Battle Scale [PROPOSAL]`:

| Scale | 1 Size ≈ | Thread Sensitivity min |
|---|---|---|
| Skirmish | ~10 soldiers | 30+ |
| Company | ~100 soldiers | 30+ |
| Battle | ~500 soldiers | 50+ |
| Campaign | ~1,000 soldiers | 50+ |
| War | ~5,000 soldiers | 70+ |

Plus PP-201 (PROVISIONAL) warning that Dissolution at mass-battle scale is "campaign-altering" and adds Strain rules at the Campaign/War scales: "Battles on Valorian soil: MS −1 (MS −2 for Campaign/War scale)."

**Verdict.** **PROPOSED scale table is internally coherent and load-bearing for the strain mechanics. Recommend canonization.**

**Proposal (PROPOSED →).** Promote the 5-scale table from [PROPOSAL] to canonical. Drop the `[PROPOSAL]` marker on commit. The scale determines:
1. Battle Size unit conversion (10 / 100 / 500 / 1,000 / 5,000 soldiers per "1 Size").
2. Thread Sensitivity floor for participation.
3. Strain cost (battles at Campaign/War tier produce MS −2 instead of MS −1; this is already explicit in `peninsular_strain_v1.md §3`).
4. Implicit player-stake calibration (engine UI: "Skirmish" framing vs "War" framing).

**Rationale.** The proposal has been in the file since at least 2026-04-02 (per PP-104 dated changelog). Strain calculations downstream already reference Campaign/War scale. The lack of canonization is a process gap, not a design gap.

**Alternatives considered.**
- **Reduce to 3 scales (Skirmish / Battle / War).** Rejected: collapses Company and Campaign into adjacent bands; loses the Campaign distinction which is exactly what B4 #10 wanted.
- **Add a 6th scale ("Engagement", <10 soldiers).** Rejected: <10 already collapses to personal combat per `params/combat.md` and existing mass→personal handoff rules (`scale_transitions.md`); 6th scale would duplicate.

**Workplan impact.**
- §4 S1 (Mass combat) — explicitly stress all 5 scales in S1.1 V1 module. Each scale validated for size arithmetic and Strain coupling.
- §4 add **S1.6 — V4 Campaign-tier-specific edge cases.** Stress the boundaries: 999 vs 1,001 soldier engagement at Battle/Campaign boundary. Campaign-scale Dissolution PP-201 application.
- §7 Q8 row removed.

**Confidence.** High.

---

## Q9 — ED-586 Arc state vs Priority 6 at Mandate < 3 → PROPOSED

**Original Q:** When a faction is at Mandate < 3 (Legitimacy or Popular_Support degraded), how does Priority 6 ("Attacked") behavior interact with the Arc state?

**Investigation.** `params/bg/npc_priority_trees.md:44` shows the Crown priority tree (full read needed for other-faction trees). Priority 6 = "Attacked → Military proportional. Crown covert (Influence +1 Ob)." Priority 4 (Default) contains the T2 Kronmark conditional but no Mandate-degradation handling. **No "Arc state" reference in `npc_priority_trees.md`.**

"Arc state" likely refers to the Royal Crisis arc (Q20-related) or a similar narrative-arc clock. ED-586 is from SIM3 batch (older), predating PP-686 v2 / PP-684 (PP-684 = Conviction Taxonomy + Axis Matrix per Conviction work).

**Proposal (PROPOSED →).** At Mandate < 3, Priority 6 ("Attacked") behavior degrades from "military proportional" to **"defensive only — no offensive deployment, no covert escalation."** Rationale: Mandate < 3 represents institutional fragility; an aggressive Priority 6 response from a Mandate-degraded faction would over-commit and accelerate collapse (Strain feedback). Defensive-only response models the faction's reduced political capacity.

**Engine logic.** When NPC priority tree fires Priority 6 AND faction L < 3 OR PS < 3: substitute "Military proportional" → "Defensive Military only (no expansion / no covert)." Covert Influence +1 Ob clause retained as written (since covert is already qualified).

**Rationale.** Maps the "Arc state vs Priority 6" tension by reading the question as: at low Mandate, the priority tree's aggression overshoots the faction's actual capacity to sustain conflict. The proposal converts the priority tree into a Mandate-aware response — low Mandate damps Priority 6 aggression rather than overriding it.

**Alternatives considered.**
- **At Mandate < 3, skip Priority 6 entirely (jump to Priority 7 Pass).** Rejected: too passive; a faction at Mandate 2 still defends its capital.
- **At Mandate < 3, Priority 6 fires but Crown loses the Domain Action automatically.** Rejected: deterministic loss is not engine logic for a probabilistic system; this would be a hack.

**Workplan impact.**
- §4 W6.4 module (Open finding SIM3-04 ED-586) — replace with this proposal as the V1 baseline. Stress modules test the proposal.
- §7 Q9 row removed.

**Confidence.** Medium — depends on what "Arc state" means specifically. If Jordan has a different intent, replace.

---

## Q10 — ED-587 Stability Crisis Zoom In trigger absent → PROPOSED

**Original Q:** Stability Crisis trigger for Zoom-In into personal scale is absent.

**Investigation.** `params/scale_transitions.md` documents Phase-Lock Protocol legal Zoom-In entry points: "After Phase 1, After Phase 3, After Phase 6 Step 1" (PP-103). No explicit Stability-Crisis-triggered Zoom-In.

**Proposal (PROPOSED →).** Add a **Stability-Crisis Zoom-In trigger** integrated with existing Phase-Lock Protocol:

When at any phase boundary an active faction has Stability ≤ 1, the engine **offers** a Zoom-In into a personal-scale Crisis Scene at the next legal Phase-Lock entry point (After Phase 1, 3, or 6 Step 1). The player may decline (continue at strategic scale) or accept (zoom in to a cabinet meeting, succession debate, public address, etc.).

If accepted, the Crisis Scene resolves at personal scale and produces a Domain Echo into faction stats at next Accounting per existing PP-108/PP-109 rules. The personal scene narrative is generated from the canonical Crisis catalog (TBD, low-content list of ~6-12 crisis scene templates; e.g., "cabinet meeting at the brink," "royal address to a hostile court," "succession debate with rival claimants").

Trigger condition: Stability ≤ 1 at phase boundary. Frequency: once per season per faction (deduplicate; don't fire every phase if Stability remains low across multiple phases in one season).

**Rationale.** ED-587 surfaces a real UX gap: the engine has explicit Zoom-In entry points but no explicit Stability-driven prompt to use them. Adding a Crisis-triggered prompt creates the player-facing surface that connects strategic-layer stress to personal-scale drama — directly serving the `<intent_of_game>` "emergent narrative" goal.

**Engine logic.**
- At every legal Phase-Lock entry point, scan all active factions.
- If any faction has Stability ≤ 1 AND no Crisis Scene fired this season: surface Zoom-In prompt.
- Player accepts → trigger Crisis Scene from catalog matched to faction state.
- Player declines → log "Crisis declined" (narrative beat for future reference).
- Decline does NOT advance Strain (no penalty for declining); the Stability situation continues at strategic scale.

**Alternatives considered.**
- **Mandatory Zoom-In at Stability ≤ 1.** Rejected: removes player agency; player should choose engagement depth.
- **Stability ≤ 2 trigger.** Rejected: too frequent; Stability of 2 is unstable but not crisis.
- **Stability ≤ 0 trigger (elimination-imminent).** Rejected: too late; the dramatic beats live in the descent, not the catastrophe.

**Workplan impact.**
- §4 C4.3 module (ED-587 fix) — replaced with this proposal as V1 baseline.
- **New §4 line item.** Crisis Scene catalog (~6–12 templates) must be authored as a Phase-0b prerequisite. Each template specifies narrative framing, NPC participants, available Appeal/Debate options, and Domain Echo mappings to Stability.
- §7 Q10 row removed.

**Confidence.** Medium — directionally correct; catalog content is design work.

---

## Q11 — ED-588 RM Phase 2 T9 holding condition unreachable ↻ SUPERSEDED

**Original Q:** Restoration Movement (RM) Phase 2 T9 holding condition is unreachable.

**Investigation.** RM canon at `params/bg/core.md:20, 38, 166, 221–222`:

- *"Restoration Movement | 5 players only (optional) — **statless faction; operates through PT and Presence only**"* (core.md:20, 38)
- *"Restoration Movement | — | — | — | — | — | — | **No faction stats. Operates via Presence markers and Community Weaving only. (PP-460)**"* (core.md:166)
- Domain Action table at core.md:221–222:
  - *"Community Organising (Restoration) | 2 | Pool: 1D base + 1D per adjacent territory with RM Presence marker. **Failure: no Stability cost (RM has no Stability).**"*
  - *"Community Weaving (Restoration) | (100−MS)÷20 round up min 1 | −1 per Presence marker in territory"*

**Verdict.** **PP-460 supersedes B1's RM model.** RM is now a statless faction operating exclusively via Presence markers and Community Weaving. Concepts like "Phase 2 T9 holding condition" (which presupposes RM holding a territory in the conventional faction-control sense) no longer apply — RM doesn't "hold" T9 (Himmelenger) or any other territory in the traditional model; it places Presence markers and exerts Community-action effects.

If the underlying B1 concern was "RM doesn't ever consolidate enough Presence at T9 to be politically significant," that's now a **Presence-marker accumulation rate** question, not a holding-condition question. The fetched canon shows Community Organising pool scales with adjacent Presence markers, which gives RM a growth mechanism.

**Workplan impact.**
- §4 S15 — drop ED-588 from open-finding list (note in editorial ledger: superseded by PP-460).
- §4 add new S15.5: **V5 full-scenario RM ignition + propagation.** Drive 5+ campaigns with RM enabled (5-player config). Verify Presence markers can accumulate to political significance via Community Organising / Community Weaving. If they cannot, that surfaces a balance issue (rate-tuning), not a structural gap.
- §7 Q11 row removed.

**Confidence.** High on PP-460 supersession; Medium on whether the underlying B1 concern persists post-PP-460. Stress S15.5 will surface if so.

---

## Q12 — ED-589 RM Presence marker mechanics undefined ↻ SUPERSEDED

**Original Q:** RM Presence marker mechanics not specified.

**Investigation.** Same canon as Q11. PP-460 defines Presence markers operationally through Domain Actions:

- **Community Organising:** Pool scales with adjacent Presence markers. Placement mechanism: success on Community Organising places markers.
- **Community Weaving:** Pool = `(100−MS)÷20 round up, min 1`. Modifier: −1 per Presence marker in territory.

These define what Presence markers DO (their effects on RM action pools). Canon does not explicitly enumerate **how they are removed** (only placed). The B1 finding may have surfaced this asymmetry.

**Verdict.** **Mostly superseded by PP-460; one residual minor gap on removal mechanics.**

**Residual proposal (PROPOSED →).** Define Presence marker removal:
- Each marker removed by: (a) opposing faction successful Community Suppression action (new — not currently canonical); OR (b) territory eliminated from RM's reach (RM Presence in territory T cannot persist if no adjacent territory has any RM presence — orphan-pruning); OR (c) MS = 100 (Restoration complete — RM dissolves).
- (a) is a new mechanic; recommend deferral until balance testing shows it's needed. Default: markers persist until territory orphans.

**Alternative.** Simpler model: Presence markers never voluntarily removable; they persist until RM dissolves (MS = 100 or campaign end). Player who wants RM-free territory must accept Presence as a permanent ambient effect.

**Workplan impact.**
- §4 S15 — replace ED-589 reference with PP-460-superseded + residual Presence-removal stress.
- §4 add **S15.6 — V4 NERS Presence removal.** Test removal scenarios; verify whichever model Jordan picks (orphan-prune-only or with-Community-Suppression).
- §7 Q12 row removed (or merged with Q11 row).

**Confidence.** Medium.

---

## Q13 — ED-616 Parliamentary block on Tribune actions → PROPOSED

**Original Q:** No canonical mechanism for Parliament to block Tribune actions.

**Investigation.** `params/bg/parliament.md` does not mention 'tribune' or 'block' anywhere in the file (greps returned no matches). `params/bg/faction_actions.md` references "Tribune Intel actions (Investigate, Spy, Counter-Narrative) [PP-664: VTM-building struck with VTM track]" — Tribune is an Intel-action category in the BG.

**Proposal (PROPOSED →).** Add a Parliamentary Procedural Block mechanic for Tribune actions:

When Parliament is in active Session (per existing parliament.md procedure — verify exact session-trigger semantics in full read) AND a Tribune Intel action is declared by any faction, the Parliamentary opposition may move for a Procedural Block.

- **Block roll:** Influence pool from non-acting factions (each contributing 1D if they vote to block) vs Ob = `(Acting faction PI value) + 1`.
- **Success:** Tribune action suspended this season. Acting faction may re-declare next season.
- **Overwhelming success:** Tribune action suspended + acting faction PI −1 (procedural defeat).
- **Failure:** Tribune action proceeds normally; no penalty to acting faction.
- **Limit:** One Procedural Block attempt per Parliamentary Session.

**Rationale.** Parliamentary authority over Tribune actions is a natural extension of Parliament's procedural role. The mechanic uses existing pools (Influence) and existing scales (PI). It introduces no new attribute, only a new resolution surface that couples PI track to Intel-action visibility.

**Alternatives considered.**
- **Block is automatic when Parliament is in session (no roll).** Rejected: too strong; effectively kills Intel-action use in many seasons.
- **Block requires Parliamentary supermajority (>50% factions vote block).** Rejected: harder to administer in engine; vote pools cleaner.
- **Block applies only to Spy and Counter-Narrative, not Investigate.** Could be reasonable refinement; defer to ratification.

**Workplan impact.**
- §4 G2.1 module replaced with this proposal as V1 baseline.
- §4 G2.4 V4 NERS module unchanged.
- §7 Q13 row removed.

**Confidence.** Medium — proposal is mechanically minimal but Jordan may have intent for Tribune-Parliament relationship that's narrower or broader.

---

## Q14 — ED-617 Grand Contest Recall once-per-source → PROPOSED

**Original Q:** Grand Contest Recall — should the Recall bonus be once-per-source?

**Investigation.** `params/contest.md` Pools table:
- "Recall bonus: +2D — Citing specific named verifiable claim. Binary. Either genre."

And Contest Types table at `contest.md:142`:
- Grand Contest: 5 rounds, alternating, standard pool, Crowd adjudicator.

**The "binary" descriptor means the bonus is +2D or 0 — no scaling. But the question is whether a single source can grant the bonus multiple times across the 5-round Grand Contest.**

**Proposal (PROPOSED →).** **Recall bonus is once per cited source per Contest, regardless of Contest Type.** Once a specific named claim is "in evidence" within a Contest, re-citing it grants no additional bonus (the claim is rhetorically present; restating is not novel evidence).

Across separate Contests, the same source may be cited again (fresh adjudication; new pool of crowd / judge memory).

**Engine logic.** Per Contest instance, maintain a citation-set tracking sources cited with Recall bonus. On Recall declaration, check set. If source already cited, no bonus; if new, +2D and add to set.

**Rationale.** Standardizes Recall behavior across all 6 Contest types. Closes the obvious exploit: in a 5-round Grand Contest, otherwise a single named claim could grant +2D per round = +10D across the Contest, which dominates strategy. Once-per-source caps this to +2D total per source.

**Alternatives considered.**
- **Once per source per round** (current implicit reading — Recall is +2D each invocation regardless): Rejected as creating the +10D exploit.
- **Recall pool granted at Contest start, decayed +2D / +1D / +0 / +0 / +0 across rounds:** Rejected: novel mechanic where simpler suffices.
- **Limit Recall to Memory-genre only:** Rejected: contest.md states Recall bonus applies to either genre (Memory or Projection).

**Workplan impact.**
- §4 P2 (Contest general) — module P2.1 V1 includes Recall-citation tracking spec.
- §7 Q14 row removed.

**Confidence.** High on the canonical fix direction; Medium on whether Jordan considers cross-Contest re-cite (allowed in this proposal) or never-cite-twice (stricter alternative).

---

## Q15 — ED-618 Torben Conviction window S1–S8 → PROPOSED

**Original Q:** Torben Conviction window S1–8 formal definition.

**Investigation.** `params/bg/npcs_special.md` documents **Torben Loyalty Track** (range 0–7, starts at 7, sources for gain/loss specified). Torben Conviction is separate from Loyalty — Conviction is at the personal-scale per PP-684 Conviction Taxonomy (13-Conviction set, 52-cell axis matrix). Canon does NOT define a temporal window during which Torben's Conviction values are formable vs locked.

The Altonian Tutoring Demand fires at IP ≥ 40 (per npcs_special.md:line 12-ish noted in B5 update); when triggered, Torben goes to Altonia and Torben Loyalty decays. This is the natural "Torben removal" event from peninsula.

**Proposal (PROPOSED →).** Define Torben Conviction window:

- **S1–S8 (formative window):** Torben's Conviction values respond to player-NPC interactions, threadwork knots formed with Torben, and faction-level events the player participates in. Each scene where the player directly engages Torben can shift one Conviction value per the Axis Matrix per the standard Conviction-shift rules.
- **S9+ (locked):** Torben's Conviction values lock to whatever state they reached at end-of-S8. Subsequent scenes still produce scene-level outcomes but do not modify the locked Conviction profile.
- **Early lock trigger:** If Altonian Tutoring Demand fires at IP ≥ 40 before S8, the window closes early (Torben physically removed from peninsula).

**Rationale.** S1–S8 maps to the canonical "early game" per `arc_test_batch3` reference timeline (S1–S8 = settlement governance friction + tension escalation). Locking Torben's Conviction at the formative-period end gives the player a meaningful early-game window to influence a load-bearing NPC, then commits the result for the rest of the campaign. Matches the narrative pattern of childhood-formative-then-adult-fixed character development.

**Alternatives considered.**
- **No lock — Torben Conviction mutable throughout.** Rejected: makes Torben's character noise; player can flip him repeatedly.
- **S1–S5 window (shorter).** Could be reasonable; matches the very-early game; Jordan may prefer this.
- **No formative window — Torben's Conviction is starting-state hard-fixed.** Rejected: removes a player engagement surface that the EDs suggest was intended.

**Workplan impact.**
- §4 W7.3 (Torben Conviction window) — replaced with this proposal as V1 baseline. Stress includes early-lock edge cases.
- §4 P6.2 (V5 full scenario covering Torben Conviction arc) — anchored on this window.
- §7 Q15 row removed.

**Confidence.** Medium — narrative-design call; Jordan may prefer different window length or different lock semantics.

---

## Q16 — ED-619 3-Obligation GM advisory cap → engine logic → PROPOSED

**Original Q:** The 3-Obligation GM advisory cap (TTRPG-era) must become engine logic since the videogame has no GM.

**Investigation.** In TTRPG framing, the GM advised players when a character had 3 outstanding Obligations to "consider retiring or resolving" before accepting a 4th. In videogame, no GM → engine must enforce or surface.

**Proposal (PROPOSED →).** Engine-enforced 3-Obligation soft cap:

- A character may have 0–3 active Obligations with no engine intervention.
- When an action would create a 4th Obligation, engine **surfaces a forced-choice UI prompt** to the player BEFORE the Obligation finalizes: *"This character is at Obligation capacity. Accept this Obligation requires choosing one existing Obligation to retire (cleared without resolution — modest narrative penalty) or dissolve (resolved in a Wager — possible Conviction shift). Or decline the new Obligation."*
- Player picks: (a) retire existing + accept new, (b) dissolve existing via Wager + accept new (per F1 Wager mechanic), or (c) decline new.
- Engine never auto-resolves. Player choice required to proceed.

**Rationale.** Preserves the GM-advisory intent (player aware of Obligation overload) and forces explicit player decision (no implicit auto-discard). The retire/dissolve mechanic plugs directly into existing F1 Wager and Knot Lifecycle mechanics (since Obligations are knot-related). No new mechanic invented — only a UI prompt that triggers existing resolution paths.

**Alternatives considered.**
- **Hard cap (cannot accept 4th, period).** Rejected: too rigid; some narrative moments warrant temporary overload.
- **Soft cap with stat penalty (accept 4th but take Stability −1).** Rejected: introduces a stat penalty where the existing system uses choice instead.
- **No engine intervention; player tracks manually.** Rejected: explicitly contradicts the "no GM in videogame" reality — the GM's advisory role HAS to migrate somewhere.

**Workplan impact.**
- §4 add new engine-layer stress module under E-layer: **E1.5 — V11 Obligation cap UI flow.** Verify engine surfaces prompt; verify all three player choices propagate to canonical Obligation resolution.
- §7 Q16 row removed.

**Confidence.** High on directionally correct (engine must enforce something); Medium on the specific UI flow.

---

## Q17 — B1 #4 Splinter Influence split (60/40 or unsplit) → PROPOSED

**Original Q:** When a faction succession-splits, does Influence split 60/40 same as Mandate, or remain unsplit?

**Investigation.** B2 sims confirmed Mandate split is 60/40 between majority-successor and splinter. Canon at `params/factions/stats_1_7_scale.md` defines Influence as the institutional-reach attribute. Other stats (Wealth, Military, Stability) split rules not fully visible in fetched canon but B2 work tested Mandate split specifically.

**Proposal (PROPOSED →).** **Influence splits 60/40 same as Mandate.**

Rationale: Influence represents institutional reach/relationship-network. When a faction politically splits, the institutional network divides along the same fracture as the Mandate split — the majority-successor retains 60% reach; the splinter retains 40%. Reach is more concentrated in personnel and relationships than Mandate (which is more abstract authority); but personnel and relationships split with the faction they go with. Therefore 60/40 mirrors Mandate.

Alternative considered:
- **Influence unsplit (full to majority-successor).** Rejected: this would model splinters as institutionally-impotent immediately, which contradicts B1/B2's findings that successful splinters do operate institutionally.
- **Influence splits more aggressively (50/50 or worse for majority).** Rejected: contradicts the population-percentage logic (the majority by definition retains the larger share).
- **Wealth and Military split per separate rules (not at 60/40).** Outside this Q's scope but flag for adjacent ratification: I would propose Wealth and Military split per the same 60/40 rule for consistency, but balance-test may require different splits.

**Workplan impact.**
- §4 S15 stress modules include this proposal as V1 baseline for stat-split testing.
- §7 Q17 row removed.

**Confidence.** High direction; Medium on whether other stats follow 60/40 or have bespoke rules.

---

## Q18 — B3 #5 CI seasonal cap vs Piety Yield at T9 ✓ RESOLVED

**Original Q:** Should the CI seasonal cap be reduced from ±5 (allowing Piety Yield to dominate at T9 PT=5), or should Piety Yield be retuned to fit within ±5?

**Investigation.** `params/bg/ci_seizure.md:13`: **"CI seasonal cap (PP-504): ±3 per season from player-initiated Domain Actions. ±5 per season from all sources combined (includes Conditio[nal effects]...)."**

The cap is already canonical as a two-tier structure: ±3 from Domain Actions specifically, ±5 from all sources (Domain Actions + Piety Yield + conditional effects). The B3 finding was that Piety Yield at T9 PT=5 produces large per-season CI advance — the cap accommodates this by tiering: Piety Yield contributes to the ±5 "all sources" bucket but does not occupy the ±3 "Domain Actions" bucket.

**Verdict.** **Canon explicit — the cap is already tiered to handle the Piety-Yield-dominance issue B3 surfaced.** The PP-504 design (two-tier cap with Piety Yield falling under the wider ±5 cap) IS the answer to B3 #5. No additional design action needed.

**Workplan impact.**
- §4 S5 — strike "B3 design decision #5" from open list.
- §7 Q18 row removed.

**Confidence.** High.

---

## Q19 — B3 #6 T2 Kronmark garrison priority entry ✓ RESOLVED

**Original Q:** Should T2 Kronmark have an explicit Crown priority tree entry, or accept T2 as exposed?

**Investigation.** `params/bg/npc_priority_trees.md:44` shows Crown Priority 4 (Default) with sub-clause: *"If T2 Kronmark is ungarrisoned AND any Varfell unit is active in T4: deploy minimum [garrison]."* The conditional IS in the priority tree, just at the Default (Priority 4) level rather than as an elevated priority.

**Verdict.** **Canon explicit — T2 Kronmark garrison defense is in the priority tree at Priority 4 Default with the Varfell-T4-trigger conditional.** B3 #6 is answered: T2 has explicit priority-tree coverage (just not at elevated priority).

The current priority is reactive (defensive deployment triggered by Varfell action), not proactive (preemptive permanent garrison). This is the design choice — Kronmark is held by ambient defensive posture, escalating only when Varfell adjacency activates.

**Workplan impact.**
- §4 W6 stress modules retain T2-stress as edge-case coverage but no canon change needed.
- §7 Q19 row removed.

**Confidence.** High.

---

## Q20 — B4 #7 Almud's father (backstory or live Royal Crisis card) ↻ SUPERSEDED

**Original Q:** Is Almud's father's assassination a fixed backstory event, or made live via a Royal Crisis card?

**Investigation.** `params/bg/royal_assassination.md`:
- Title: **"Royal Assassination Fuse"**
- Source: `designs/architecture/conflict_architecture_proposal.md` (CANON)
- Trigger: **Royal Crisis Tension Card (Card #1)**
- Model: Fuse (S0 seed → S8+ fire, succeed-on-fire)
- Target Determination: sub-roll at game start or when Royal Crisis card drawn — Lenneth (1-2), Torben (3-4), Almud (5-6).
- **Notes: "Replaces the prior fixed backstory (Almud's father assassination) per Session A Patch 7 backstory strike."**

**Verdict.** **Canon explicit. Almud's father is backstory (struck from live mechanics). The Royal Crisis Tension Card now triggers a live assassination fuse with three possible targets, three distinct mid-game consequence arcs.** B4 #7 is answered: live, via Royal Crisis card, not Almud's father (target is now Lenneth/Torben/Almud per sub-roll).

**Workplan impact.**
- §4 S11 (Royal Assassination) — replace S11.1 V1 module with verification of the canonical Fuse + 3-target sub-roll + 3 consequence arcs.
- §4 S11 priority remains P1 (load-bearing for narrative arc; mature canon but never stress-tested).
- §4 S11.2 V3 chain — verify each of three Target Consequences (Lenneth dies → Almud revenge arc; Torben dies → Elske retrieval; Almud dies → Lenneth takes throne) propagates coherently to mid-game state.
- §4 add **S11.5 — V12 narrative emergence per target.** Each of three arcs should produce distinctly different mid-game; verify under stress.
- §7 Q20 row removed.

**Confidence.** High.

---

## Q21 — E1 non-d10-pool resolution mechanics? → CLARIFIED

**Original Q:** Are there any non-d10-pool resolution mechanics anywhere in canon?

**Investigation.**

- Default: d10 pool at TN 7 (1=−1, 7–9=+1, 10=+2 — per `params/core.md` and used universally).
- **TN variance found:** `params/mass_combat.md` `Volley Phase Pool (PP-503) [PROVISIONAL]`: "Volley Phase pool = Power stat (1–7) rolled at TN 6." **TN 6, not TN 7.** Ranged unit output uses TN 6.
- **Ob computation** (`Battle Ob = floor(defender Military / 2) + 1`) is a derived Ob, not a different dice mechanic — still d10 pool resolution.
- **Faction stat scale** (1–7 per `stats_1_7_scale.md`) defines pool size, not a different dice mechanic.
- **Pre-contest prep** (`Attunement + History`, TN 7 Ob 1) is a standard d10 pool at TN 7.
- **Rushed pre-contest prep:** "TN 8" — yet another TN variant.

**Verdict.** **The d10 mechanic is universal across canon, but TN varies: TN 6 (Volley Phase), TN 7 (default everywhere else), TN 8 (rushed pre-contest prep).** No fundamentally different resolution system (no flat-checks, no fixed-degree, no card-draw, no point-buy).

**Workplan impact.**
- §4 **E1.1 V1 update** to include TN 6 and TN 8 validation, not just TN 7.
- §4 **E1.2 V2 update** distribution tables for TN 6, TN 7, TN 8 across pool sizes 1d–20d.
- §7 Q21 row removed (answer documented).

**Confidence.** High — but may have missed an edge mechanic in files not exhaustively read. Recommend full grep across all `params/` for `TN \d` patterns as part of E1 stress execution.

---

## Q22 — E2 unified clock state machine or per-system? → CLARIFIED

**Original Q:** Is there a unified clock state machine or are clocks one-off per-system implementations?

**Investigation.** `params/bg/clocks.md` documents three named clocks (MS, CI, IP) each with bespoke band tables and effect mappings. The bands and effects are clock-specific (MS bands by Proximity-Rating × range; CI by range only; IP by range only). No shared state-machine abstraction; each clock has its own canonical effects table.

The `clock_registry_v30_infill.md` is small (645 chars) — possibly a higher-level index but not a unified state-machine spec.

**Verdict.** **Clocks are per-system implementations sharing a common scale convention (0–100 typical, with named bands).** No unified canonical state machine. Each clock specifies its own ranges, triggers, and effects.

**Workplan impact.**
- §4 **E2.1 V1** updated to validate per-clock (MS, CI, IP, PI, RDT, TD, WC, WR, Torben Loyalty, Elske Loyalty, Patience Counter, Coup Counter [obsolete via Q2]). Each is its own state-machine instance.
- §4 add **E2.6 — coverage matrix of clocks.** Map every clock to: range, fill sources, drain sources, threshold effects. Verify no missing clock surfaces; verify no unused clocks (orphans).
- §7 Q22 row removed.

**Confidence.** High.

---

## Q23 — E3 tracks orthogonal or coupled? → CLARIFIED (mixed)

**Original Q:** Are tracks orthogonal (independent) or coupled?

**Investigation.** `params/bg/tracks.md` shows explicit couplings:

- **RDT → TD:** TD "Activates at RDT 2." (Direct gating.)
- **WR gates WC** (per `params/bg/core.md`).
- **Trade Network Investment** appears orthogonal (Hafenmark-only, persists until control transfer).
- **AP (Attention Pool)** per-territory; inquisitor deployment tied to AP thresholds.
- **VTM struck (PP-663):** track removed; faction-level Thread now character-scale only.
- **AER removed (Q6):** track no longer exists.

**Verdict.** **Mixed model. Some explicit couplings (RDT→TD, WR→WC), others orthogonal. Workplan E3 should map coupling explicitly per track.**

**Workplan impact.**
- §4 **E3.5 — V3 explicit coupling map.** Enumerate every active track. For each: list dependencies (other tracks that affect it) and dependents (other tracks it affects). Surface any unintended couplings or coupling gaps.
- §7 Q23 row removed.

**Confidence.** High.

---

## Q24 — E4 four scales fully canonical or only personal/strategic? → CORRECTED (5+ scales)

**Original Q:** Are all four scales canonical, or does game only distinguish personal vs strategic?

**Investigation.** `params/scale_transitions.md` Scale Table:

| Scale | Example | Base Ob |
|---|---|---|
| Object | One item, one wound | 1 |
| Personal | One person | 2 |
| Relational | Small group, social agreement | 3 |
| Territorial | A duchy, a district | 4 |
| Structural | A kingdom, an institution | 5+ |

Plus **Mass** (battle) as a distinct scale via Mass→Personal handoff and Mass→Thread rules. Plus **Thread** scale (Leap-triggered contact duration).

**Verdict.** **Canon distinguishes more than four scales. The taxonomy is: Object / Personal / Relational / Territorial / Structural / Mass / Thread.** Seven scales, with explicit handoff rules between each pair (`scale_transitions.md` "Eight Handoff Rules"). My V1.0 workplan said four (personal / settlement / territory / peninsula) — that was wrong relative to canon.

**Workplan impact.**
- §4 **E4 entry rewritten.** Replace "personal ↔ settlement ↔ territory ↔ peninsula" with the canonical 5-scale spatial taxonomy (Object/Personal/Relational/Territorial/Structural) plus Mass and Thread as orthogonal scales triggered by combat / Thread mechanics.
- §4 E4.1 V7 transition matrix expanded — 7 scales = 21 transition pairs (vs my V1.0's 6 pairs). Each direction tested.
- §4 E4.4 narrative emergence anchored on the richer taxonomy.
- §5 Phase 1 effort estimate for E4 may need to expand to 2.5–3 sessions given the wider scale set.
- §7 Q24 row removed.

**Confidence.** High.

---

## Q25 — S3 faction actions canonically open or hidden? → CLARIFIED (mixed)

**Original Q:** Are faction actions canonically open-info or hidden?

**Investigation.**

- Most actions are **publicly declared** at phase start (per the phase structure in `params/bg/phases.md` and action declarations in `faction_actions.md`).
- **Private tracks** explicitly named: Varfell Patience Counters (PC), Hafenmark RDT and TD (both "Hafenmark private track"), Varfell-only WR.
- **Public tracks:** Turmoil (explicit "Public"), MS/CI/IP all visible to all factions per their effect tables (effects apply universally).
- **Intel actions** (Tribune Investigate, Spy, Counter-Narrative) explicitly probe hidden state — they exist BECAUSE some state is hidden.
- **Early-Seizure visibility (PP-507) [PROVISIONAL]:** CI < 50 = all factions observe seizure attempt; CI ≥ 50 = only factions with Intel ≥ 3 in target territory observe. So visibility is conditional on game state.

**Verdict.** **Hybrid model.** Default: action declarations are public. Specific overrides:
- **Hidden private tracks** (RDT, TD, PC, WR, Elske Loyalty initial state) belong to one faction.
- **Conditionally visible actions** (Early Seizure, Intel actions targeting Intel-protected state).
- **Intel actions** are the mechanism for moving information from hidden to known.

**Workplan impact.**
- §4 **S3.5 — V11 + new module on visibility map.** Enumerate per-action and per-track visibility classification (public / private-to-faction / Intel-gated). Verify the engine surfaces the right information to the right players.
- §4 **C6.3 (new) — V10 dominant strategy probe on Intel-action exploitation.** Intel actions are the asymmetric-info exploit surface; stress probe whether dominant Intel-spam is exploitable.
- §7 Q25 row removed.

**Confidence.** High direction; Medium on completeness of the per-action visibility map (needs Phase 0b enumeration).

---

## Workplan deltas (V1.0 → V1.1)

### Section-by-section changes

**§0.4 Gating prerequisites.**
- Add: "Canonize the Battle Scale table (`params/mass_combat.md:223`) — strip the [PROPOSAL] marker on the next infrastructure commit. Per Q8."
- Add: "Author Crisis Scene catalog (~6–12 templates) for Stability-Crisis Zoom-In trigger. Per Q10."
- Add: "Confirm Influence-split 60/40 rule. Per Q17. Add to spec patch (B2 ready)."

**§2 Stress vector taxonomy.** No change.

**§3 Prior coverage.** No change.

**§4 System enumeration (per-system changes):**

- **E1 Dice/TN/Degree:** add TN 6 (Volley) and TN 8 (rushed) to E1.1, E1.2 distributions. Add new E1.5 "Obligation cap UI flow" module (per Q16).
- **E2 Clocks:** add E2.6 coverage matrix module (per Q22). E2.1 enumerated to per-clock list.
- **E3 Phases/Tracks:** add E3.5 explicit coupling map module (per Q23).
- **E4 Scale transitions:** rewrite the scale enumeration to 5+1+1 (Object/Personal/Relational/Territorial/Structural + Mass + Thread). E4.1 transition matrix becomes 21 pairs. Effort 2 → 2.5–3 sessions (per Q24).
- **P2 Contest:** P2.1 V1 includes Recall-once-per-source rule (per Q14).
- **S1 Mass combat:** S1.1 V1 explicitly validates 5-scale Battle Scale table (per Q8). Add S1.6 Campaign-tier edge cases. Remove S1.5 (naval carve-out unconditional per Q1).
- **S5 CI Seizure:** S5.2 module reframed (not "open finding" — canon is mature per Q4 + Q18). Priority demoted; effort halved.
- **S7 Treaty/Accord:** S7.1 replaced (Q5 proposal as baseline).
- **S8 Löwenritter Coup → Renamed "Löwenritter Graduated Autonomy" (per Q2 + Q3).** S13 dissolved into S8. S8.1 striked. S8.2–S8.6 rewritten against the canonical 4-stage state machine.
- **S9 Altonian Vanguard / IP:** drop AER (per Q6) and reframe Warden gaps (per Q7). Add S9.6 (WC × WR × MS interaction), S9.7 (WC=3 NERS).
- **S11 Royal Assassination:** S11.1 replaced with verification of canonical Royal Crisis Fuse + 3-target sub-roll (per Q20). Add S11.5 narrative emergence per target.
- **S13 Graduated Löwenritter autonomy → MERGED INTO S8 (per Q2/Q3).** S13 entry removed.
- **S15 Faction succession:** S15.5 (RM full scenario per Q11) and S15.6 (Presence removal per Q12) added. Replace ED-588/589 references with PP-460-superseded markers.
- **W1 Geography:** W1.1 (ED-055 naval) dropped (per Q1). W1.2 and W1.3 retained.
- **W6 NPC priority trees:** W6.4 replaced with Q9 proposal as baseline. W6.5 unchanged.
- **W7 Special NPCs:** W7.3 replaced with Q15 Torben window proposal as baseline.
- **G2 Parliament:** G2.1 replaced with Q13 Tribune-Block proposal.
- **C4 Scale-transition seams:** C4.3 replaced with Q10 Stability-Crisis-Zoom-In proposal.

**§5 Phase ordering.**
- Phase 0b spec-gap session count: 8 gaps were listed in V1.0. Post-resolution: 6 of 8 are RESOLVED or SUPERSEDED (Q2/Q3/Q4/Q6/Q7/Q18), reducing the Phase 0b workload. Remaining design work: Q5 Treaty/Strain, Q10 Crisis catalog, Q13 Tribune block, Q15 Torben window, Q16 Obligation engine flow, Q9 Priority 6 Mandate degradation, Q12 RM Presence removal model. Each is a single-session decision-and-canonize, not a full design pass.
- Estimated total: **Phase 0b reduces from ~16 sessions to ~7 ratification-and-commit sessions.**

**§6 Per-phase session sketches.**
- Session-two recommendation: was "ED-055 naval scope (single decision)" → DROP (per Q1). Replace with: **Session-two = Phase 0b first decision batch.** Bundle Q5 + Q10 + Q13 + Q15 + Q16 ratifications into one decision session (each is a small narrative-mechanical confirmation; bulk-ratify in one pass to avoid 5 separate sessions).
- Session-three recommendation: was E1 → still E1, but with TN 6 / TN 8 / Obligation UI included (Q21/Q16).

**§7 Open questions.**
- All 24 resolvable Qs removed.
- §7 reduced to a residual "open items still pending Jordan ratification" list (the 7 proposed items from Phase 0b).

**§8 Out of scope.**
- Add: "Naval mechanics. Out of scope per 2026-05-10 directive. Schoenland T16 remains in canon as tributary; no naval projection."

**§9 Risks / anti-patterns.** No change.

**§10 Changelog.**
- Add: "**V1.1 (2026-05-10).** Post-resolution of 24 open questions. Naval dropped. 6 questions RESOLVED via canon, 8 SUPERSEDED via PP-460/PP-605/PP-510/Royal Crisis fuse/Graduated Autonomy/AER removal, 10 PROPOSED with rationale and alternatives. See `stress_workplan_resolutions_2026-05-10.md`."

### Total session-count revision

V1.0 estimate: ~55–65 sessions (excluding engine_v4-deferred).
V1.1 estimate: **~45–55 sessions** (Phase 0b shrinks by ~9 sessions due to resolutions; new modules across §4 add back ~3 sessions; net −6 sessions).

---

## Residual ratifications pending Jordan

The proposed resolutions below are the only items still needing Jordan acceptance before downstream stress can run. Each is a single-decision item, bundle-able into one ratification session.

| Q | Proposal | Decision required |
|---|---|---|
| Q5 | Treaty defection → Strain +1; Treaty break automatic on inter-faction battle | Accept / refine / reject |
| Q8 | Promote Battle Scale 5-tier table from [PROPOSAL] to canon | Accept / refine |
| Q9 | Priority 6 at Mandate < 3 → defensive-only | Accept / refine |
| Q10 | Stability ≤ 1 → Zoom-In offer at next Phase-Lock entry; opt-in for player; Crisis catalog authored | Accept / refine; window length |
| Q12 | RM Presence markers: orphan-prune-only (simpler) or with Community-Suppression action (richer) | Pick one |
| Q13 | Parliamentary Procedural Block on Tribune: Influence-pool vote vs PI Ob, once per Parliamentary Session | Accept / refine |
| Q14 | Recall once-per-source-per-Contest, fresh across Contests | Accept / refine |
| Q15 | Torben Conviction window S1–S8 (formative), lock at S9 or on Altonian Tutoring Demand fire | Accept / refine; window length (S1–S5 alt) |
| Q16 | Obligation cap: engine surfaces forced-choice prompt on 4th-Obligation; player retire / dissolve / decline | Accept / refine |
| Q17 | Influence splits 60/40 same as Mandate; Wealth/Military follow same rule pending balance test | Accept / refine |

---

## Confidence summary

- **High-confidence resolutions** (canon-grounded or directly canon-derivative): Q1 (directive), Q2, Q3, Q4, Q6, Q7, Q11, Q14, Q18, Q19, Q20, Q21, Q22, Q23, Q24. Fifteen items.
- **Medium-confidence resolutions** (proposals with one plausible alternative): Q5, Q8, Q9, Q10, Q12, Q13, Q15, Q16, Q17, Q25. Ten items.
- **Low-confidence items:** none in this batch — every Q produced a defensible verdict from canon evidence, even when the verdict was "proposed, needs ratification."

`[SELF-AUTHORED — bias risk]` This document was authored in the same session as the canon fetches; an independent reviewer would likely flag: (a) proposal completeness — some PROPOSED items invent minimal mechanics where Jordan may have richer designs in mind; (b) my "alternatives considered" lists are not exhaustive — typically 2–3 alternatives per proposal vs the broader design space; (c) the "RESOLVED" verdicts assume the fetched canon is authoritative and current — if there are unmerged PP-s in flight that adjust these mechanics, the resolutions may be stale; (d) merging S13 into S8 (per Q2/Q3) is structurally clean but loses the historical record of the binary-coup era — recommend keeping a `[SUPERSEDED]` placeholder rather than full deletion.

`[ASSUMPTION: Jordan directive "resolve all, no naval" grants authority to propose canonical resolutions where canon is silent — basis: directive form is imperative; project-owner contract permits Claude to execute on Jordan's specification. CONFIDENCE: high]`

`[GAP: Q9 "Arc state" interpretation — I assumed Arc state refers to Royal Crisis / faction succession arcs. If Arc state means something different in Jordan's design (e.g., a clock I haven't surfaced), Q9 proposal may need rework.]`

`[GAP: Q5 Treaty mechanic — the fetched canon shows Formal Crown Treaty and Diplomatic Token mechanics but I did not exhaustively read all treaty variants. Hafenmark "Dynastic Proclamation" and other faction-bespoke treaty-like actions may have their own Strain interactions. Verify exhaustively before stress execution.]`

---

## Changelog

- **V1.0 (2026-05-10).** Initial authorship. Resolves Q1–Q25 from `stress_test_workplan_2026-05-10.md §7`. 1 dropped (naval), 6 resolved via canon, 8 superseded, 10 proposed. Workplan deltas enumerated for V1.1 update.
