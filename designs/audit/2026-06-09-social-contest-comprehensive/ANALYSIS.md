# Social Contest — Comprehensive Analysis (all workings, all dimensions)

**Date:** 2026-06-09 · **Scope:** audit (`task_gate('audit')` passed) · **Series:** companion to `2026-06-09-massbattle-comprehensive` and `2026-06-09-personal-combat-comprehensive`
**Method:** full read of the canonical set + the complete redesign record (fetch log at end); `valoria-resolution-diagnostic` pipeline on the live canon; prior-audit reconciliation per the document-consolidation discipline.
`[SELF-AUTHORED — bias risk]` The groundup engine and most of the prior audit record are Claude-authored across sessions. Treated as external; this analysis re-derives the canonical-layer findings from the sources, not from the prior record's conclusions.

---

## 0. VERDICT

**Social contest exists in three concurrently standing layers of distinct authority, and the canonical layer is NERS non-compliant as written — fails Robust and Smooth.** Not because the resolution architecture is unsound: the pools are healthy (5D+ with stacking to 12–18D), the Persuasion Track is a deep clock, and the loop audit comes back clean. It fails because **the canonical record contradicts itself on load-bearing values** — three P1 contradictions (strain math ambiguous by a factor of 3; the per-exchange Appraise step stated in the design doc is the rule params explicitly struck; patch PP-351 has different content in two canonical files plus a third rule claiming to replace it).

The deeper finding is that **the repair is already designed and ratified, but unexecuted**: the CR1–CR7 redesign (Jordan-ratified provisional, 2026-06-01) names most of these exact contradictions as its propagation targets, and the groundup engine (Jordan-ratified for commit, 2026-06-03; 151/151 tests after the 2026-06-05 balancing pass) is the validated mechanical substrate. **The blocking work is reconciliation and propagation, not new design.** The open decisions are consolidated for Jordan in §5 — ten blocks, sub-items lettered.

This falsifies the resolution-diagnostic skill's untested initial hypothesis ("social contest — likely compliant") at the record level, while confirming what the hypothesis was actually about: the contested-resolution architecture itself is the healthy case.

---

## 1. STATE OF RECORD — the three layers

| Layer | Files | Authority | Status |
|---|---|---|---|
| **L1 — Canonical** | `designs/scene/social_contest_v30.md` (+`_index`, `_infill`), `params/contest.md`, `params/contest_extensions.md` | CANONICAL — approved 2026-04-17, patched through ED-864 (2026-05-17) | Live canon; internally contradicted (§4) |
| **L2 — CR1–CR7** | `designs/audit/2026-06-01-contest-redesign/RATIFIED_2026-06-01.md` | **Provisional canon-of-record** (Jordan: "ratify all provisionally", 2026-06-01) | Ratified; **propagation not yet applied** — verified this session: `params/contest.md` still carries the flat-dice bonus stack CR6 replaces; the v30 doc still carries Composure CR3 splits; `canonical_sources.yaml` unchanged |
| **L3 — Groundup engine** | `designs/audit/2026-06-03-contest-groundup/` (7 code modules + 18 record docs) | **Ratified for commit** as a mechanical proposal — "diverges from the canonical social_contest_v30 … not a canon change" (`RATIFICATION.md`) | Built, audited, reconciled, validated, balanced; 151/151 tests (2026-06-05) |

**Reconciliation status.** This is the `<document_consolidation>` trigger shape ("which of these is current?"), but the instances carry explicit, distinct statuses rather than competing claims to the same status — so it is a **propagation queue, not a versions pile**. L2 supersedes L1's resolution internals on its own ratified terms; L3 implements L2's architecture (CR1 wrapper-over-modules, CR2 σ-substrate, CR6 δσ-leverage) while diverging on the tracker model (no Composure/Face/Concentration trio — `TERMINOLOGY.md` flags this as "the principal reconciliation item"). The consolidation target is the CR-mandated rewrite of v30 + params with the groundup engine as implementation substrate — **decision D-1, §5**.

---

## 2. THE WORKINGS — complete mechanical description

### 2.1 Canonical layer (the live rules)

**Setup (§2).** Adjudicator type fixes the Argue primary attribute — Expert Judge → Cognition, Crowd → Charisma, No-adjudicator → Attunement, Panel → Cognition `[PROVISIONAL, ED-137]` — and is fixed for the contest's duration. Primary genre (Memory/Projection) is assigned from the question's shape. Style bonus dice: +1D primary genre, +1D audience-faction boost match, max +2D, fixed at setup. Persuasion Track 0–10 (A wins ≥7, B wins ≤3, compromise 4–6), GM-set start (typical 5). Audience resistance = avg faction Stability (round up) −1, min 0, **eroding per exchange** at `−⌊exchange_count/2⌋` (ED-295 Option D, ratified ED-864 2026-05-17, all interaction types). Eight proceeding types (Formal 3 exchanges / Grand 5 / Royal Audience 3 / Church Tribunal 1–5 / Guild Arbitration 3 / Casual 1 / Private Negotiation 1–3 / Personal Appeal 1) with role structure and resistance modifiers. Stakes defined at Step 6 *(skeleton defect: Step 6 lives only in the infill — §4, P3-13)*.

**Exchange loop (§4, seven steps).**
1. **Appraise** — *the rule is contradicted between doc and params; P1-1, §4.* Both orators read the audience's current state; degrees: failure = misleading signal, 1 = axis type, 2 = full boost, 3+ = boost + one detail (Belief / threshold / emotional state).
2. **Choose style** — genre × orientation as one pick (params PP-235 names: Cite Precedent / Bury Precedent / Propose Vision / Imply Consequence; the doc's §2 parenthetical names them Precedent / Suppression / Vision / Insinuation — fork, P2-5).
2b. **Corroborate** — declared coalition member, Knot-sharing Ob 1 / non-Knot Ob 2 / asymmetric-disadvantaged Ob 2 (PP-257); success +1D, failure 1 strain to corroborator.
3. **Argue** — pool `(Primary Attribute × 2) + History bonus` (History = points + 3), TN 7; + setup bonus dice; + Recall +2D for a specific named verifiable citation (once per source per Grand Contest, ED-617; per-exchange in Formal); + Evidence-Track Findings +1D/+2D-cap at Exchange 1 (PP-636); + Resonant-Style targeting +1D with per-style riders (extensions); + Momentum spend (1 = 1 auto-success, cap 4). Stacking ceiling +5D positional; practical pools 12–18D (extensions).
4. **Resolve by interaction type** — CLASH (same genre, opposite orientation): compare successes, movement = margin − resistance if positive; strain to loser = margin + winner's Cha-mod − loser's Focus-defence, min 0. REINFORCE (same/same): as CLASH with (margin − 1, min 0) base. CROSS (different genres): each side independently `⌊successes/2⌋` vs resistance, net movement = difference, **no strain**; Obscuring-side larger movement → Doubt Marker instead of movement. TIE: both take 1 strain (CROSS-tie exempt, PP-236), track +1 to first-to-speak holder. **Indirect/Obscuring win:** no track movement; Doubt Marker / Suspicion Token on opponent (−2 to opponent's next winning margin before resistance, one active, consumed on use) — *the doc's heading for this block was lost to atomization; P3-13.*
5. **Forfeit** — Regroup (track +1 to opponent, Concentration restores to max) or Concede a Point (1 strain, track +1 to opponent, +1D next exchange).
6. **Strain & resources** — *load-bearing values contradicted; P1-2, §4.* Composure = Cha × 3 (3–21, ED-694; equipment adds flat). Strain ≥ Composure → Rattled mark (resets, excess carries); 2 marks = socially incapacitated; Knot buffer redirects damage (+1 strain/use). Rattled penalty channel: doc says +1 Ob/level; params says −1D/level (Decision-B 2026-05-15, PP-716 channel reservation) — *P2-4.* Concentration = Focus × 3; at 0 → Spent (−2D next exchange, opponent +1D, then resets). Recovery: Rattled 1 mark/non-social scene; Composure full at scene change; everything clears at scene end.
7. GM records on the hidden ledger.

**Initiative (§5).** Exchange 1 rolled — Attunement vs Attunement, TN 7 Ob 1, higher net acts last (ED-581); transfers to exchange winner; tie stays. *(params still carries the pre-ED-581 deterministic rule with the ED-138 open flag — P3-12.)*

**Post-contest (§6).** Thread co-movement by winning genre (Memory → MS +1 retention shift; Projection → +1D first matching Domain Action + conditional MS +1). Domain Echo on decisive wins (Memory → faction Mandate +1 in the cited domain; Projection → the +1D). Total Victory (≥9/≤1): Contest Fatigue on loser, +1 Momentum winner, Disposition/Reputation shift, BG-mode Mandate −1. **Obligations (§6.1):** binding cross-season commitments from decisive Formal/Grand wins — duration/violation table (Formal 2 seasons / Mandate −1 … Church Tribunal until-revoked / Heresy acceleration); settlement-targeted variants (C-08); **Wager Obligations** (Grand + Projection + Consequence style; verifiable, achievable, time-bound future conditions) with the ED-778 edge-case table (counterparty death → neutral discharge + Renown; institutional collapse → 4-season suspension; structural impossibility → fail-forward + Scar; PC-death transfer both directions per generational_transition). NPC Obligations block violating actions on the priority tree unless Survival priority — a won contest constrains NPC strategy, not just stats. **Conviction Scar visibility (§6.2)** — momentary portrait indicator, no stat reveal. **Chain Contests (§6.3):** Compromise defers — follow-up at the carried track position, Scars persist, Deadlock rule (ED-582: two consecutive zero-movement exchanges → both resistances −1; a third → ends as Compromise), max chain 3 → cold equilibrium (Disposition freeze, 4-season topic lockout).

**Asymmetric proceedings (§7).** Fixed roles; disadvantaged party halves resistance; advantaged side immune to CROSS strain. **§7.1 Excommunication Tribunal** (ED-625): prerequisites CI ≥ 40 + Church Mandate ≥ 4 + (Evidence ≥ 3 ∨ Obligation violation ∨ 2 convictions); track starts at 7; no accused corroboration; 1–3 exchanges; consequence tables for NPC/PC/faction; Act of Contrition revocation; the designed counter is preventing the filing (Stay, CI < 55). **§7.2 Succession Contest** (ED-665): Standing ≥ 5 claimants (cross-faction needs Mandate ≥ 3 + structural claim); per-faction adjudicator bodies; Decisive → single leader; Compromise → **faction split** per §7.2.1 track-weighted ratios (4→60/40, 5→55/45, 6→50/50), stat division by ratio, **Stability floor 3** (keeps the split out of mandatory-Zoom-In crisis), territory/treaty split, schismatic identity by Conviction; Total Victory → unified + free Wager extraction. **§7.3 Heresy Investigation lifecycle** (ED-772): Initiation → Investigation (2–4 seasons, one mandatory Zoom-In Interrogation per season) → Verdict; 4–6 seasons nominal; eight closure conditions (Inquisitor death/demotion/reassignment, target death/defection/protection/conversion, acquittal); one active Investigation per target per jurisdiction; player counter-strategies enumerated.

**BG layer (§10).** Sides declare; pool = sum of side Mandate; genre +1D, dominant-faction boost +1D (orientation excluded — public voting); resistance base 0, +1 per Stability ≥ 6 abstainer, max +2 *(scale-fragile by construction — P2-7)*; each side's movement = successes − resistance if positive, net = difference; bands pass / committee / fail; lobby offset clamped to the 4–6 zone (ED-621, PP-256); Total Victory → dominant losing faction Mandate −1. Thread consequences do not fire at BG scale (personal-scale argument required). **§10.1 Parliamentary Stay** (ED-631): 2+ factions vs Church, only while CI < 55; success suspends a Tribunal filing one season. **§11 Hybrid:** one BG round → clamped offset → TTRPG contest resolves.

**Thread interfaces.** §9.3 Practitioner Weaving (TS ≥ 30: +⌊TS/30⌋D, visible, Church may file HI, Coherence Ob 1 after). §9.4 Thread ops between exchanges — *the temporal-axis-conflict effect is stated three different ways across three canonical files; P1-3.* §9.4b Adjudicator Thread Response (ED-667): Certainty-indexed table C5 (proceedings corrupted, exchange voided, HI fires) → C2–0 (no response; TS 30+ adjudicators may bank Evidence), gated by the threadwork §2.3 visibility table. TS gate on Evidence targeting (P-08 compliance, extensions).

**Other TTRPG rules.** §9.1 preparation (+1D Exchange 1; Overwhelming adds TN 6 Appraise; rushed TN 8; stacks with Findings to +3D). §9.2 coalitions (Lead per exchange, individual Composure, **shared Concentration = Σ(Focus + Recall)** per PP-237 — *contradicts ED-694's Recall removal; P2-8*). §9.5 Beliefs → Momentum (max 1/contest). §9.6 Forced Unmask = violence in chamber → auto-loss (infill) — *name-collides with PP-255's stalemate Forced Unmask; P3-11.* §9.7 Niflhel toolkit stub (no Formal/Grand participation; private negotiation Ob = ⌊Stability/2⌋+1; ED-041 open).

**Stochastic surface inventory (Phase 0).** Dice: Appraise, initiative roll, corroboration, prep, Argue. Deterministic accounting: strain math, resources, Domain Echo, Obligations, Tribunal/HI/Succession consequence tables. Clocks: Persuasion Track (deep, 0–10), Evidence Track, Obligation clocks, chain counter. The system is the composite the diagnostic prefers: a small stochastic surface inside a deterministic institutional wrapper.

**Cross-system surface map.**

| System | Surface |
|---|---|
| core engine | TN 6/7/8, degrees, Momentum, Let It Ride, pool floor 1D |
| combat | parallel pool construction `(Attr×2)+H(+3)`; **CR7: Concentration shared** (reverses the armature handoff's "cut" — D-7) |
| npc_behavior | Resonant Style targeting, Conviction Scars (§3.3/§3.4), arc transitions, Certainty table |
| faction_layer | §5.5 rebuttal shape, Mandate-weighted votes, Succession, Obligation-blocked priority trees, Sacred Veto (boundary open) |
| investigation / fieldwork | Findings citation (PP-636, F-TRANS-11), Evidence Track prerequisites for Tribunal |
| threadwork | R-65, §9.4/§9.4b, MS co-movement, visibility table, P-08 gate |
| settlement / territory | settlement-targeted Obligations (C-08); Succession territory split |
| clocks / player_agency / scale_transitions | Obligation clocks (clock_registry); chain-contest Scene Slate (player_agency §4.2); HI mandatory Zoom-Ins (scale_transitions §4.3.2 + ED-749 hysteresis) |
| church / CI | Tribunal CI ≥ 40, Stay CI < 55, ⌊CI/20⌋ vote bonus, PP-349 self-investigation exception |
| generational_transition | Obligation transfer both directions (ED-778) |

**GD-1 compliance:** `[NULL: victory paths — examined; every contest outcome feeds stats / territory / political surface; none grants or gates victory directly. Compliant.]`

### 2.2 CR1–CR7 layer (provisional canon-of-record, 2026-06-01)

| CR | Decision | Replaces | Fixes |
|---|---|---|---|
| CR1 | Wrapper→modules ("container") on the shared σ-leverage engine; stochastic surface = {Appraise, ResolveExchange} only | v30 resolution internals | architecture |
| CR2 | Substrate migration: success-counting → σ-space net engine (per-die −1/0/+1/+2) shared with combat/core | success-count resolution | the deep Smoothness fix — one substrate |
| CR3 | Three trackers: **Concentration** (shared w/ combat, Focus×3) + **Face** (new, contest-local ethos) + **Persuasion** (preserved); Composure retired | Composure-as-buffer | Lesson-1 (stamina/standing split); Face ≠ Disposition/Reputation |
| CR4 | Ciceronian **stasis × genre**: stasis = terrain (conjectural/definitional/qualitative/translative), authored genres = stance; stasis sets primary genre; translative = the Stay | GM-fiat primary-genre assignment; siloed Stay | F5 (definitional gap) + F6 (jurisdiction silo) |
| CR5 | Orientations re-grounded: Direct → Persuasion (merits); Indirect → attacks opponent **Face**, self-Face backfire on failure | Doubt Marker / Suspicion Token | F7 self-gating (Quintilian/Nyāya) |
| CR6 | Leverage as **δσ**: setup advantages accumulate as δσ, tanh soft-capped, uniform probability impact (validated +0.191 uniform across 5D–26D) | flat-dice bonus stack | **F1** — uniform impact, not uniform form |
| CR7 | Concentration shared with combat | armature handoff's "Concentration cut from combat" | cross-system identity — **must propagate into the combat spec (D-7)** |

σ-engine constants (kept, `params/core.md` via the armature handoff §1): per-die map 1→−1 / 2–6→0 / 7–9→+1 / 10→+2; σ_N = 0.8·√Pool; level→δσ Minor 0.25 / Moderate 0.50 / Strong 0.75 / Major 1.00; `eff_σ = 1.5·tanh(net_σ/1.5)`; Effective Ob = base − eff_σ·σ_N. A δσ has the same probability impact at every pool size (the √N small-pool insight is why this engine exists).

**Propagation checklist (ratified, all verified pending this session):** rewrite v30 internals; `params/contest.md` flat-dice → δσ lever table + Composure → Concentration+Face + reconcile the named contradictions (Rattled channel, Cha-mod ×3, token naming); record CR7 in the combat spec; register the redesigned doc in `canonical_sources.yaml`; ED entries CR1–7 (collision-aware); T-25 pass + sim before non-provisional.

### 2.3 Groundup engine (ratified-for-commit implementation, 2026-06-03 → balanced 2026-06-05)

**Architecture.** Acyclic seven-module DAG: `contract` (Move/ContestView/FaultState/Adjudicator/Panel) · `engine` (σ-leverage + base d10) · `primitives` (Stasis, Appeal ethos/pathos/logos, Standing, Reserve, Pool, SelfGating, Leverage, Room, Resonance, Readiness, DefeatCatalogue, Evidence/Dossier) · `resolver` (Bout wrapper + **Venue** top-down spec + win-conditions) · `modes` (institution presets) · `policy` (decoupled archetypes) · `faction` (adapter). No privileged "merits": primitives accumulate per-side advancement; **the venue decides what winning is and which faults are fatal.**

**Win-conditions:** ThresholdRace (debate/disputation) · TallyAtClose (assembly — resolves the mismatched-appeal 100%-draw deadlock) · VoteAtClose (ballotta, secret council) · ProofBar (tribunal — burden of proof; defender prevails on doubt) · GraceThreshold (petition — sovereign's discretion) · **PersuasionTrack** (canon's two-pole banded track: committee/decisive/total). **DefeatCatalogue** = venue-configured nigrahāsthana (barred-device, self-contradiction, evasion, silence) — deterministic clinch, no roll. **Panels** aggregate member character/discipline/learned-hostile. **Evidence:** hidden-weight dossier, relevance-gated, corroboration with diminishing returns, readiness-free hard proof. **Pressure:** institutional tilt + public-raised susceptibility (leak unlock). **Jitter ±8%** removes high-faculty exact-tie artifacts. **Faction adapter:** per-voter §5.3/§5.4 motions with ⌊CI/20⌋ and committee bands; §7.2 succession bands + §7.2.1 ratios (implemented literally, counter-intuition flagged); §10 coalition pooling on the two-party spine. Ten venue presets; policy archetypes including `counterpuncher` (confirmatio-before-refutatio, Quintilian-grounded).

**Development arc (compressed; full record in the directory):** P1 turn-order bias 87/13 → boundary resolution, validated symmetric at every faculty → appeals found inert (CODE_REVIEW P1) → modulation design (resonance = role↔character blend with leak; readiness = the build-then-close payoff) → F1 (build strictly dominated, 0.000) fixed → generality audit (proof axis / win-condition / panels / fault-set hard-coded) → venue generalization → FULL_AUDIT → adversarial CRITIQUE → **AUDIT_RECONCILED master** (R1 `resist` scale-fragile MEDIUM — works at small pools 0.338→0.433, inert at large 0.205→0.205; R4 evidence readiness-free **and** uncapped MEDIUM; R2 Standing-hub and R3 Partial-credit re-scoped to Jordan questions; loop null and faculty curve empirically confirmed) → historical / venue / evidence-pressure validations (each institution's documented behavior reproduced; the one over-tuned case, automatic grace, corrected) → **balancing pass 2026-06-05** (pool-aware Overwhelming bar OVERWHELM_SIGMA 0.85; RES_FLOOR 0.15; bar swaps; ballotta; 151/151; chronicle targets pass except the drama floor on bar venues and the courtier monoculture in ethos-grace venues — both held for Jordan).

**Groundup NERS (reconciled + balancing):** **N pass · R partial (R1, R4, unseeded/exit-0 tests) · S pass · E partial (Standing hub, band duplication).**

---

## 3. DIMENSIONAL ANALYSIS — the diagnostic on the live canon

**Phase 0** — decomposed in §2.1: small dice surface + deterministic wrapper + deep clocks. Correct composite.

**Phase 1 — stress points.** Argue pools: design floor (Attr 1) = 2D + H bonus ≥ 5D typical; with stacking, practical 12–18D — healthy. The genuinely small designed rolls: Appraise (1–7D per the doc's Attunement-only version; ~2–14D per params' Att+Rec — even the floor is contradicted, P1-1) and the BG vote at small coalitions (Mandate-sum pools). Exposure: every contest, routine.

**Phase 2 — what the stress points decide.** Appraise decides information quality, recoverable per exchange — low stakes per roll. Argue feeds a 0–10 clock over 3–5+ exchanges — graded, deep, the Lesson-4 shape done right. Irreversible-class outcomes (Excommunication, Succession) ride multi-exchange tracks with designed counters (Stay; claimant gating) — intent-gated pass.

**Phase 3a — impact uniformity: FAIL (known).** Every bonus is flat dice (+1D/+2D) on pools of varying size: impact scales with 1/√N. A +1D at 5D ≫ +1D at 18D in probability terms. This is F1; **CR6 is the ratified answer** (δσ, validated uniform). Until propagation, the canonical bonus economy is non-uniform.
**Phase 3b — cliffs.** Win/loss/compromise bands, Tribunal start-7, fault counts: intended, spaced, legible — exempt. Tribunal stacks (start 7 + no corroboration + Inquisitor-set count) are explicit fait-accompli design with a documented counter (the Stay) — intent-gated pass. No accidental stacked cliff found in the canonical layer beyond the value contradictions themselves.
**Phase 3c — role conflation.** Composure carries social-stamina *and* standing-buffer (the CR3 finding; ratified split into Concentration + Face). "Forced Unmask" names two unrelated mechanics (P3-11).

**Phase 4 — loops.** `[NULL: feedback loops — examined; none undamped+unbounded.]` Strain is bounded by Composure with scene recovery; Rattled caps at incapacitation with per-scene recovery; Doubt/Suspicion is one-shot; Momentum caps at 4; chain contests cap at 3 → cold equilibrium; Obligation-violation consequences feed the faction layer where Mandate/Stability dampers live; Succession splits are bounded by the Stability-3 floor (explicitly designed to stay out of the mandatory-Zoom-In crisis band). Cross-system: contest → Mandate → vote pool (§10) is gain-positive but vote pools are episodic and committee-banded — damped.

**Phase 5 — intent gate.** Coalition dominance (ED-297): ratified intent. Tribunal asymmetry: explicit intent + safeguard. The three P1 contradictions: not intent — record corruption. Flat-dice non-uniformity: pre-CR inheritance, `[INTENT SUPERSEDED]` by CR6.

**Phase 6 / NERS verdict — canonical layer:**

```
SYSTEM: social contest (canonical L1)   COMPONENTS: dice + deterministic + clock
VERDICT: NON-COMPLIANT — load-bearing values contradicted across the canonical record

N: partial — duplicated anti-stall apparatus (ED-582 Deadlock vs ED-864 erosion, P3-15);
   PP-255's 10-exchange cap unreachable (no proceeding exceeds 7 exchanges, P3-10);
   Forced-Unmask name collision (P3-11); Composure dual role (CR3 pending)
R: FAIL — strain math ambiguous ×3 (P1-2); the doc's per-exchange Step 1 is a struck rule
   (P1-1); PP-351 exists in three incompatible forms (P1-3); flat-dice bonuses non-uniform
   (CR6 pending); SIM-DEBT-04 open — the Cha×2 / Att×2 adjudicator pools were never calibrated
S: FAIL — terminology fork runs through the canonical pair itself (skeleton CLASH/REINFORCE/
   CROSS + Revealing/Obscuring + Doubt Marker; infill Head-On/Echo + Indirect; params Head-On/
   Echo Match/Cross-Time + Direct/Indirect + Suspicion Token; two style-name sets);
   unpropagated patches (ED-581, PP-614, ED-694↔PP-237); doc and params disagree on the
   same mechanics
E: partial — the player-facing loop (read, pick a style, move a visible track) is intuitable;
   the maintenance surface is not (three temporal-axis rules, two token names, two style sets)

REMEDIATION (worst-first):
  P1 value adjudication (D-2/D-3) → Lesson 2/record-integrity: settle ×3, depletion, Appraise, PP-351
  CR propagation as ONE consolidation rewrite → Lessons 1/2/6 wholesale (CR3/CR5/CR6)
  Groundup R1/R4/test fixes (already specified in the reconciled master)
  SIM-DEBT-04 → close in the new substrate (venue/role weighting), not on the dying pools
```

**Videogame-implementability (P-03, no GM — engine resolves).** GM-fiat points needing engine rules at propagation: primary-genre assignment (**CR4 answers**: stasis-derived); GM-set starting track; compromise narration; Finding scope-relevance; Guild "GM picks" boost; §7.2 adjudicator tie-breaking; Wager partial-met judgment; Appraise-failure misleading-signal generation. Constraint spot-check: P-08 ✓ (TS gates on Evidence targeting), P-14 ✓ (extensions-PP-351 routes thread-op co-movement to the Track — whichever PP-351 survives D-3 must preserve this), GD-1 ✓ (null above).

---

## 4. FINDINGS — severity-ranked, this session's value-add

Prior-audit findings (F1–F7, R1–R4, the CR targets) are inventoried in §§2.2–2.3 and not re-listed. What follows is what this session found **in the canonical record itself** that no prior audit document states. Every value cited from source; severity per editorial-ledger convention.

### P1 — load-bearing contradictions (ledger entries appended this session)

**P1-1 — The doc's Appraise step is a struck rule.**
`social_contest_v30.md` §4 Step 1: "Roll Attunement alone (no History), TN 7, Ob 1" (PP-278); §8 Derived Values: "Appraise pool | Attunement only | 1–7." `params/contest.md` PP-614: Appraise = **Attunement + Recall**, Ob = opponent's Charisma ÷ 2 (round up, min 1) — and the params entry explicitly records the old "Read pool = Attunement only, Ob 1" as **STRUCK**. The design doc states, twice, the exact rule the rule-params layer struck. This fires on every exchange of every contest — the highest-frequency roll in the system. Even the pool floor in Phase 1 is contradicted (1–7D vs ~2–14D).

**P1-2 — Strain math ambiguous by a factor of 3; Concentration depletion breaks Spent under the params reading.**
The ×3 rescale (ED-694) was applied inconsistently:
- Doc §8: Cha-mod = max(0, ⌊(Cha−3)÷2⌋) **×3** (range 0–6); Focus defence = ⌊Foc÷2⌋ **×3** (range 0–9). Doc §4 Step 6 bracket: "[ED-127 resolved, ED-694 updated… Strain, Charisma modifier, and Focus defence all scaled ×3 to match.]"
- Doc §4 CLASH bullets: Cha-mod **unscaled** ("Cha 4–5: +1; Cha 6–7: +2"), Focus defence **unscaled** ("Foc 6–7: 3") — inside the same document.
- `params/contest.md` Derived Values: both **unscaled** (0–2 / 0–3).
- Concentration: doc §4 Step 6 "Depletes by **3** per exchange, **−3** additional on exchange loss"; params: **−1**/exchange, **−1** on loss. The params depletion against the ×3 pool (Focus×3, range 3–21) disables Spent at every stat level: Focus 7 → 21 Concentration → never Spent inside any proceeding (max 7 exchanges); even Focus 1 survives 3 exchanges. The doc's −3 preserves the original Spent geometry (the rescale multiplied pool and drain together); the params kept old drain against the new pool.
Strain is the contest's damage engine; until D-2 resolves, the loser's strain in any CLASH is undefined within a factor of 3.

**P1-3 — PP-351 exists in three incompatible forms across the canonical record.**
Same patch lineage, three live texts:
- Doc §9.4 (both the skeleton clause and the labeled "Temporal Axis Conflict (PP-351)" block): opposing-axis Thread op → **TN 8 on both orators' next Read roll**.
- `params/contest_extensions.md` PP-351: opposing-axis op → **±1 Persuasion Track per thread-op co-movement card** (the P-14 routing — co-movement expressed on the Track).
- `params/contest.md` PP-258 ("replaces PP-123"): opposing-axis op → **−1D to both parties' Argue** for that exchange.
Three different effects (TN shift on Read / Track movement / dice penalty on Argue) on three different rolls. Patch-record integrity failure, not a mere fork: the ID system exists precisely to prevent this. D-3 is genuinely Jordan's — no evidence arbiter distinguishes them.

### P2 — propagation failures and structural fragilities

**P2-4 — Rattled penalty channel contradicted.** Doc §4 Step 6: "**+1 Ob** per Rattled level (cumulative)." `params/contest.md`: "**−1D** per Rattled level" citing Decision-B (2026-05-15) and PP-716's channel reservation (Ob-channel reserved for circumstance, dice-channel for condition). The params entry is later and decision-cited; the doc was never updated. Evidence-resolvable in D-2's batch.

**P2-5 — The terminology fork runs through the canonical pair itself.** Interaction names: skeleton CLASH / REINFORCE / CROSS; infill **Head-On / Echo Match / Cross-Time** (infill §4 INDIRECT WIN block); params Head-On / Echo Match / Cross-Time. Orientations: skeleton Revealing / Obscuring; infill and params **Direct / Indirect**. Genres: infill §4 Step 2 still says "**Past or Future**" — the pre-PP-234 names the skeleton's own header renames to Memory/Projection. Tokens: skeleton **Doubt Marker**; params **Suspicion Token** (−2 next winning margin — same effect, different name). Styles: doc §2 Step 3 "(Precedent, Suppression, Vision, or Insinuation)"; params PP-235 "Cite Precedent / Bury Precedent / Propose Vision / Imply Consequence." One mechanic, two-to-three names at every layer — the Smoothness FAIL's core evidence. CR5/CR3 propagation must pick one set; the rewrite (D-1) is the venue.

**P2-6 — Faction-boost table divergence, including a struck row still live.** Doc §2 Step 3 table retains the **Niflhel** boost row; `params/contest.md` records that row struck (ED-764 — Niflhel cannot participate in Formal/Grand per §9.7, so a parliamentary boost row is incoherent). Ethical-mode labels differ: doc "Divine Command" / "Rawlsian Social Contract" vs params "Faith" / "Equity Social Contract." Label choice is creative-layer (D-4); the struck-row survival is mechanical drift.

**P2-7 — Canon §10's BG resistance arithmetic is scale-fragile by construction.** §10: resistance base 0, +1 per Stability ≥ 6 abstainer, max +2; each side moves max(0, successes − resistance), net = difference. At BG pools (Mandate sums, ~5–20D, E[succ] ≈ 0.4·pool), a flat 0–2 resistance subtracted from both sides before differencing is largely self-cancelling and proportionally inert at large pools — the same structure the groundup adapter measured as R1 (0.338→0.433 effect at small pools, 0.205→0.205 at large). R1 is not only an engine finding; it generalizes to the canonical rule the adapter implements. The groundup fix (resistance as σ-space floor, RES_FLOOR 0.15) is the template.

**P2-8 — Coalition Concentration contradicts ED-694.** §9.2 PP-237: shared pool = Σ(Focus + **Recall**) across members. ED-694 (cited in §8 and §4 Step 6) removed Recall from Concentration — "no conceptual link to sustained focus." The coalition rule was never updated; solo and coalition Concentration now derive from different attribute sets.

**P2-9 — SIM-DEBT-04 still open.** Doc §12 Simulation debt: "Adjudicator-type pool variation untested. Charisma×2 and Attunement×2 pools need calibration." Open since 2026-04-17. Recommended close in the new substrate (§7), not on the dying pools.

### P3 — hygiene, duplication, atomization damage

**P3-10 — PP-255's 10-exchange stalemate cap is unreachable.** No proceeding reaches 10 exchanges: Formal 3, Grand 5, Royal Audience 3, Tribunal 1–5, Guild 3, Succession 3–7, Private 1–3 (doc §2 Step 5, §7.2). Chain contests are separate contests, each re-counted. The cap is dead apparatus unless a longer proceeding is intended.

**P3-11 — "Forced Unmask" names two unrelated mechanics.** PP-255 (params/extensions): stalemate resolution — loser is whoever sits closer to their losing threshold, Composure as tiebreak. Infill §9.6: violence in the contest chamber → violent party auto-loses. A rules lookup on the term returns the wrong mechanic half the time; rename one (cheap, fold into D-1's rewrite).

**P3-12 — params first-to-speak is pre-ED-581.** Doc §5: Exchange-1 first-to-speak **rolled** (Attunement vs Attunement, TN 7 Ob 1, higher net acts last), ED-581, with §12 marking ED-138 resolved. `params/contest.md` still carries the deterministic rule with the ED-138 open flag.

**P3-13 — Atomization damage in the skeleton.** (a) Setup Step 6 ("Define stakes") exists only in the infill — the skeleton's §2 jumps Step 5 → Step 7. (b) The Doubt-Marker bullet block in §4 sits headingless after TIE; its heading ("**INDIRECT WIN** …") lives in the infill. A skeleton-only reader gets a procedure with a missing step and an orphaned rule block — and the skeleton is what the resolver serves.

**P3-14 — Composure's stale historical row.** Doc §12 "Resolved by this version" still says "Composure = Charisma + 6. Parallels Health = Endurance + 6" — the pre-ED-694 value; §8 says Charisma × 3. The params header carries the same Cha+6 fossil in a comment. Confusing, not load-bearing (§8 governs).

**P3-15 — Two anti-stall mechanisms layered, never reconciled.** ED-582 Deadlock (chain contests: two consecutive zero-movement exchanges → both resistances −1; a third → forced Compromise) predates ED-864/ED-295-D per-exchange erosion (resistance −⌊exchanges/2⌋, all interaction types, all contests). Erosion makes Deadlock's trigger rare-to-unreachable (resistance is already falling). Not contradictory — duplicative; the Necessity question is D-8.

**P3-16 — Convergence, not defect: ED-137 Panel.** Canon's Panel adjudicator is provisional ("use Expert Judge"); the groundup engine has a built, validated Panel model (member character / discipline / learned-hostile aggregation). Propagation closes ED-137 for free.

---

## 5. CONSOLIDATED DECISIONS FOR JORDAN

Ten blocks; sub-items lettered inline. D-2 is evidence-weighted (a recommendation is stated, vetoable); D-3/D-4/D-9 are genuinely open (no evidence arbiter).

| # | Decision | Options / recommendation | Source |
|---|---|---|---|
| **D-1** | Propagation strategy | **Recommended:** one consolidation rewrite of `social_contest_v30` + `params/contest*` per CR1–CR7, with the groundup engine as implementation substrate (closes P2-5, P3-11–P3-14, ED-137 in the same pass). Alternative: patch-by-patch propagation (more commits, same end-state, keeps the contradictions live longer). | RATIFIED_2026-06-01 propagation checklist; groundup RATIFICATION.md |
| **D-2a** | ×3 strain scaling (P1-2) | **Recommended:** ×3 consistently (doc §8 + §4 Step 6 bracket reading) — it is the ED-694-dated intent and preserves strain/Composure geometry. Veto = revert all to unscaled and rescale Composure. | doc §4/§8 vs params Derived Values |
| **D-2b** | Concentration depletion (P1-2) | **Recommended:** −3/exchange, −3 on loss (doc) — params' −1 disables Spent at every stat level against the ×3 pool. | doc §4 Step 6 vs params |
| **D-2c** | Appraise rule (P1-1) | **Recommended:** params PP-614 (Att + Rec, Ob = opp Cha ÷ 2 min 1) — it is the explicit strike of the doc's rule, and an opponent-indexed Ob is the better videogame shape. | params PP-614 vs doc §4 Step 1 / §8 |
| **D-3** | PP-351 content (P1-3) | Jordan's call among: TN 8 both Read (doc §9.4) / ±1 Track per co-movement card (extensions — the P-14-cleanest routing) / −1D both Argue (params PP-258). Whichever survives must preserve P-14 co-movement expression. | the three texts, §4 P1-3 |
| **D-4** | Ethical-mode labels + Niflhel row | Labels (Divine Command↔Faith; Rawlsian↔Equity Social Contract): creative layer, either set. Niflhel boost row: confirm strike (ED-764) — mechanically incoherent with §9.7. | doc §2 Step 3 vs params |
| **D-5** | Groundup balancing helds | (a) imperial-discipline pressure constants 0.05/0.20/0.25; (b) drama-floor exemption for bar venues; (c) courtier monoculture in ethos-grace venues — accept as institutional flavour or re-tune. | BALANCING_PASS_2026-06-05 |
| **D-6** | Groundup design helds | (a) counterpuncher ContestView extension; (b) §7.2.1 split ratios implemented literally — the 60/40-at-Track-4 counter-intuition (closer contest → more even split would be the intuitive direction) stands as written; confirm or invert. | AUDIT_RECONCILED; FACTION_NOTES |
| **D-7** | Reconciled-master re-scoped questions | Standing-as-hub (E-coupling); Partial credit on ProofBar; pressure-on-evidence interaction; §5.5 rebuttal ↔ Sacred-Veto boundary; small-coalition pooling coarseness — five carried questions, none blocking commit. | AUDIT_RECONCILED §R2/R3 + carried |
| **D-8** | CR7 ↔ combat armature | CR7 shares Concentration with combat; the armature handoff recorded Concentration **cut** from combat. One must yield; the combat spec must record the outcome. **Recommended:** CR7 (later, Jordan-ratified). | RATIFIED_2026-06-01 CR7; sigma_leverage_handoff |
| **D-9** | ED-582 vs ED-864 anti-stall | Keep both (Deadlock as chain-specific accelerator) or fold Deadlock into erosion. **Recommended:** fold — erosion subsumes the trigger (P3-15). | doc §6.3 vs ED-864 |
| **D-10** | Legacy opens | (a) ED-136 system rename — "Contest" proposed; candidates Contest / Contention / Proceeding (P1 in doc §12, pending since 2026-04). (b) ED-041 Niflhel social toolkit — stub in §9.7; groundup venue model is the natural home. | doc title block, §12, §9.7 |

---

## 6. INFRASTRUCTURE FINDINGS (tooling, not canon)

**INF-1 — `fetch_system('social_debate', …)` cannot return the design doc.** The resolver matches on key prefix; the concept key is `social_debate`, the files are `social_contest_*`. Every depth returns only `params/contest.md`. The canonical doc is unreachable through the documented depth-aware path; `g.read_file()` works.

**INF-2 — Silent index substitution.** `read_files_graphql` / `read_index` on `designs/scene/social_contest_v30.md` silently return `…_index.md` (`[INDEX ROUTE]`), and `read_sections` then operates on the index (42 "heading not found" warnings this session). A consumer can believe it audited the doc while holding the index. Substitution should be loud or absent.

**INF-3 — Bootstrap fetches a retired register.** `quick_bootstrap` still pulls `editorial_ledger_summary.yaml`; the architecture record retires it in favour of the JSONL as single store. `[DRIFT: register architecture — bootstrap fetch list not updated]`

---

## 7. RECOMMENDED ORDER OF WORK

1. **D-2 / D-3 adjudication** (Jordan, minutes) — unblocks the strain math and Appraise; everything downstream copies these values.
2. **CR propagation as one consolidation rewrite** (D-1) — v30 + params/extensions rewritten on the groundup substrate; closes P1-1..P1-3, P2-4..P2-6, P2-8, P3-11..P3-14, ED-137; registers in `canonical_sources.yaml`; collision-aware ED entries for CR1–7.
3. **Groundup R1 / R4 / test fixes** — already specified in the reconciled master (resistance as σ-floor; evidence soft-cap + readiness gate; seeded tests, real exit codes).
4. **SIM-DEBT-04** — close in the new substrate (venue/role weighting), not on the retiring Cha×2/Att×2 pools.
5. **T-25 pass + simulation** — the CR ratification's own condition for lifting provisional status.
6. **INF-1..INF-3** — resolver key alias, loud index routing, bootstrap fetch list.

---

## 8. AUDIT TRAIL

[READ: designs/scene/social_contest_v30.md — full, 56,083 chars] [READ: designs/scene/social_contest_v30_index.md — full] [READ: designs/scene/social_contest_v30_infill.md — full, 5,479 chars]
[READ: params/contest.md — full, 15,023 chars] [READ: params/contest_extensions.md — full]
[READ: canon/02_canon_constraints.md — full, P-01..P-15 + GD-1..GD-3] [READ: tests/audit/audit_sim_social_contest.md — full, 2026-04-08, predates current ruleset]
[READ: designs/audit/2026-06-01-contest-redesign/RATIFIED_2026-06-01.md — full] [READ: designs/audit/2026-05-29-combat-armature/sigma_leverage_handoff.md — full]
[READ: designs/audit/2026-06-03-contest-groundup/ — all 18 record docs full: README, RATIFICATION, framework, TERMINOLOGY, FULL_AUDIT (superseded), AUDIT_CRITIQUE (superseded), AUDIT_RECONCILED (master), AUDIT, AUDIT_MODULATION, MODULATION_DESIGN, STRESS, STRESS_MATRIX, STRESS_MODULATION, BALANCING_PASS_2026-06-05, HISTORICAL_VALIDATION, VENUE_VALIDATION, EVIDENCE_PRESSURE_VALIDATION, FACTION_NOTES, CODE_REVIEW]
[ASSUMPTION: groundup .py modules not re-read — the audited record (CODE_REVIEW + reconciled master) carries file:line citations; code-level re-verification belongs to step 3 of §7]
[NULL: feedback loops, canonical layer — examined; all bounded (§3 Phase 4)] [NULL: GD-1 victory paths — examined; compliant (§2.1)]
[CONFIDENCE: high on P1-1..P1-3, P2-4..P2-6, P2-8, P3-10..P3-15 (direct text); medium on P2-7 (structural argument + adapter measurement, no canon-side simulation run)]
[GAP: combat-spec text for CR7/D-8 — armature handoff read, combat spec itself not re-read this session; D-8 resolution requires it]
