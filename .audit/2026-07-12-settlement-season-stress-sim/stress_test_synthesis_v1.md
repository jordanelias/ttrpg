# Settlement-Season Stress Test — Max-Effort Synthesis

## Status: FILED — 2026-07-12 · Lane: IN (cross-cutting; SE, FA, PC) · Read-only review artifact — NOT canon.

**What this is.** An adversarial stress test of the PR#119 provisional governance mechanics, run as an
agent-driven mechanical play-out (there is no executable settlement-season engine in `sim/` — that package
is combat/faction/thread/mass-battle scale; the governance season loop is paper-only, so it was simulated by
the resolution engine acting as the ruleset). **7 diverse seeds × 5 seasons**, all PR#119 provisional items
live (the 12 authored comparative-governance items, the governance-ripple substrate, the 58-card deck). At
**every major probability roll the FAILURE branch was traced to depth 3** (deliberate failure-mode sweep, not
a fair campaign); each **gap was tested against the 14 earlier-rejected proposals**.

**What it exercised.** S1 Brixholm (Port·Hafenmark guild politics), S2 Dunmark (frontier Fortress·Crown
Directives), S3 Sanct Vaduz (Cathedral Seat·Church·Seggio), S4 Kronmark (famine Town·Compact — the substrate
§5.5 example), S5 Eisgrund (Mine·Varfell·patron-lapse), S6 Valholt March (3-settlement Territory·Mandate
aggregation), S7 Hohenfels (absentee Court Seat·Performance-Audit). Full per-season narratives in
`seed_traces/`; all 57 depth-3 roll-failure traces in `appendix_B_roll_failures.md`.

**Method.** A 13-agent Workflow — 5 kernel-extraction agents (Sonnet/Haiku) distilled the ruleset → 7 Opus
high-effort seed agents each simulated one seed across 5 seasons carrying state forward → one Opus max-effort
synthesis pass. **Then a main-session verification pass** (this document) that (a) recomputed every parseable
roll's odds against the repo's own engine code, (b) re-checked the two headline "dead-end by construction"
findings against the full canonical docs, and (c) re-tiered the findings accordingly. §0 below is that
verification layer — it is the reason this synthesis supersedes the raw workflow output.

**Existing-code provenance (per the "use all existing resources" directive).** Odds are not agent estimates.
They are computed from repo code: `dice_pool` from `skills/valoria-dice-model/valoria_dice.py` (exact
convolution on its own die model, cross-checked against its `outcome_probs` Monte-Carlo, Δ≤0.003), and
`d_sigma` from `sim/autoload/sigma_leverage.py`'s canonical closed-form `p_success()` with the real
`LEVEL_SIGMA` advantage table. `sim/provincial/faction_action.py` was confirmed runnable (the resolver enum
maps to actual code, not just paper). Ground-truth tables in `ground_truth_odds.md` (Appendix A).

---

## §0 · Verification & correction layer (READ FIRST)

The single most important output of this run is not a finding — it is a **correction of two findings**, caught
by verifying the sim's headline claims against the full canonical docs and the engine code. Compressed kernel
digests (the Sonnet extractors) dropped detail that made the seed agents perceive **holes that do not exist in
canon**. Both are downgraded here; failing to catch them would have mis-directed authoring effort.

### 0.1 · CORRECTED — "The event deck's Crisis family has ZERO resolvable cards" is **overstated (digest artifact).**
The workflow synth's #1 finding. Verified against `grounded_event_card_deck_v1.md` directly: the deck **does**
carry Crisis cards with branch structure — ECON-01 (Bank-Run Crisis, Capital-Posture:Debased), XSCALE-06 (ABCD
embargo), a three-card severance-Crisis suite (XSCALE-06/08, GEO-04), the Voss/Marchetti/Aldemar delayed-fuse
Crisis follow-ons — and the deck's own §C.2 states plainly that **"the bulk of Crisis/Friction/Petition
branches" resolve via `d_sigma` governor-verb choices**. So Crisis cards *are* resolvable; they route to the
`d_sigma` resolver. The seed agents improvised crises because their compressed kernel digest surfaced only the
~9 fully-delta'd low-Π Opportunity/Ambition cards and dropped the Crisis-branch detail. **Real residual (much
smaller):** per-branch explicit stat-delta tables are uneven across the deck and worth a direct completeness
audit — but that is a polish item, not "the single most load-bearing content failure." **Downgraded CRITICAL → LOW/verify.**

### 0.2 · CORRECTED — "§2.5a defines no Gu-Std2→3 rung, so §1.3c Ordenanza is unreachable by construction" **collapses (digest + seed-setup artifact).**
The workflow synth's #7 finding and S1's "central GAP." Verified against `faction_politics_v30.md` §2.5
(lines 552–560): the **full Guild ladder is authored through Gu-Std 6** — Gu-Std 2 Free Master → **Gu-Std 3
Guild Master** ("Elected by Free Masters, 4 year-arcs as Free Master") → Senior Guild Master → Comptroller →
Grand Guildmaster. The Gu-Std2→3 rung **exists**; §1.3c's Gu-Std3+ authorship gate is reachable by the normal
ladder. Two artifacts stacked to manufacture the "gap": (1) the kernel digest compressed §2.5 to only the two
PROPOSED forks (0→1, 1→2) and dropped base rungs 3–6; (2) the S1 seed setup mis-titled a Gu-Std2 actor as
"Guild Master" (that title is Gu-Std3). **Real residual (minor):** §1.3c does not define a fallback resolver
for a *sub-threshold* presentment (a Gu-Std<3 actor tabling an ordenanza) — a genuine but small edge, not a
central break. **Downgraded CRITICAL → LOW-edge.**

### 0.3 · Odds verification — the engine is slightly MORE forgiving than the agents assumed.
Every parseable `dice_pool` roll was recomputed exactly (Appendix A). **Most agent-stated odds are within ±4
points** of ground truth — good calibration. **One consistent bias:** the agents under-estimate `P(net≥3)` on
7D at TN7 by ~5–7 points (they say ~48–50%; truth is **55%**). Example: S1 Perrin's Masterpiece Examination
(7D/TN7/Ob3) stated 48%, ground truth 55%. This does not overturn any failure trace (these are ~coin-flip
rolls either way), but it means the **demotion-spiral balance claim in §5 is real but marginally softened** —
the mid-difficulty rolls governors face are ~55%, not ~48%.

### 0.4 · Odds verification — a genuine architecture finding: `d_sigma` legible-vs-engine divergence.
The seed agents scored `d_sigma` (Directive/governor-verb) rolls with the deck's **design-stated legible
model** ("base 50% + flat +10%/pt, FLOOR .05 / CAP .90"). But `sim/autoload/sigma_leverage.p_success()` — the
`[CANONICAL]` engine — is a **continuous normal-CDF**, not linear (e.g. base_Ob 3, pool 7, +major: engine 78%
vs a linear read ~90%). Both are "canon" and they **diverge materially at the tails**. This is a real,
previously-unflagged reconciliation item: the player-facing legible odds the deck promises are not the odds the
engine actually rolls. **New finding — see §6.**

**Net of §0:** the two "author-new, blocks everything" headline findings are artifacts; the structural findings
below (which do not depend on digest fidelity — they concern mechanic *interactions* and the sim's *emergent
dynamics*) survive verification and are the real yield.

---

## §1 · Mechanic-stress verdicts (PR#119 provisional items)

Verdicts adopted from the workflow synthesis, **annotated** with the §0 verification (⇩ = corrected here).

| Item | Verdict | Evidence |
|---|---|---|
| **§5 resolution_quality → Standing bridge** | **HOLD** | Clean in all 7. The §5.5 famine/Aldric template ported exactly: a w_d-high (patronage-seated) governor is shielded from Need-jaw failure until the shield is pulled (S2, S4, S7). Load-bearing spine; never invented a mechanic. |
| **§1.0a Recognition/Demotion magnitude** | **HOLD** | Fired faithfully every seed: default −1 (Rosa S4, Aldric-Kronmark S4, Bjorn S3); Severe −2 on public-scandal framing (Dunmark S4, Sanct Vaduz, Sigrid S4, Gerta S5). The 3-consecutive-failure trigger and −2-vs-−1 fork both discriminated correctly. |
| **§1.4 Directive Comply/Bargain/Defy** | **HOLD + substrate bug** | Verb machinery clean everywhere. **But** §5 mis-scores a *sanctioned* Defy-Divert as maximal-negative Directive-jaw resolution_quality → feeds Duty-failure toward Demotion (S2 Gap 6). A rules-blessed verb is double-punished. Scoring bug in the bridge, not the fork. **(Sim-surfaced; verify against §5 scoring text.)** |
| **§1.0b Recognition Fork** | **STRAIN** | Confirm-vs-New-Grant resolves (S1 fired it, New-Grant chosen), but two edges undefined: no NPC/institutional granter decision-rule (S1 — engine chose by fiat), and no defined fate for a New-Grant when the conferring patron vacates mid-arc (S7). |
| **§1.0c Court Attendance + Hostage-Kin** | **HOLD (lightly loaded)** | Fired once (S7 S2, Obligation met, Suspicion held, hostage safe). Correctly inert where the Std-4+ threshold wasn't met (S3, S4). No stress surface reached — this item is under-tested, not proven. |
| **§1.0d Performance Audit (CHN-9, NERS MERGE)** | **MERGE CONFIRMED in direction, under-executed** | S7 headline. The audit never demoted Gerta — it armed (S1), advanced to Waiting Order (S3), then **auto-lapsed when the patron fell (S4)**; Gerta fell anyway via the *separate* Recall/collapse route (S5→4). "Audit protection" is illusory and its "Missed Obligation" trigger is undefined. The two accountability paths (audit-cascade vs Recall/Suspicion) must unify on one signal — which is what merging should have produced. **The MERGE call is right; execution left the paths divorced.** |
| **§1.1a Clerk Capacity / Corruption** | **STRAIN** | Full lifecycle worked once (S1: retain→corrupt→investigate→expel). Under load, underspecified on: net-zero-AP trap at CC0/CC1 (S3, S4, S5 — "buying AP" nets nothing while arming the hidden counter), undefined CC 1→2→3 scaling, undefined Corruption→Intrigue increment (S2, S6 — detonation adjudicated not computed), no severance rule when a defected clerkship keeps paying +1 AP (S7). |
| **§1.3a Locked Extraction / Survey / Encabezamiento** | **BREAK on the failure-mode** | Writes/locks correctly, but it is a *fuse*: no subsistence floor, ~8-season cooldown, no verb reverses it (S4 defining, S5, S6). A lock justified by one good season legally strips the town for years. The **protective** (extraction-LOW) Compact is Π-gated OUT of the exact crisis that needs it (S4, S5). Compact-vs-Directive precedence undefined (S2). Structural — survives verification. |
| **§1.3b Bind the Cells (SE-JP1, NERS MERGE)** | **MERGE CONFIRMED, hard** | The §1.3b (5-household cells) vs §4.5 (settlement tracks only 1–2 named Local Actors, no population-cell layer) collision is real: a frontier Fortress or small seat cannot populate 5-household cells, so neither the cells nor the 3-stack Cell-Revolt Crisis are constructible (S2, S3, S6; force-run in S4). **Secondary, working-as-designed but sharp:** where it *does* run, Collective-Liability reliably inverts the Order tool into a **revolt accelerant** — 3 stacks → Cell Revolt Crisis in S4, S5, S7 (and S1, S6). Structural — survives verification; reconciliation mandatory. |
| **§1.3c Ordenanza Ratification** | ⇩ **HOLD (was BREAK)** | **§0.2 correction:** the Amend/Ratify/Reject branch resolves cleanly whenever the actor is qualified (S3, S6, S7). The "unreachable by construction" claim was a digest+setup artifact — the Gu-Std2→3 rung exists (§2.5). Real residual: a sub-threshold presentment has no fallback resolver (minor edge). |
| **§2.5a Guild entry/mastership forks** | **STRAIN → HOLD** | Guarantor (S1, shared-liability + Precedent fired correctly) and Capital buy-in (S1 Upstart tag) both work. The "missing rung" that was flagged here is the §0.2 artifact — no authoring gap. |
| **§3.3b Za Patron-Lapse** | **HOLD (cleanest marquee item)** | End-to-end in S5: Rivals-Move Intrigue → S1 Bargain window → S2 auto-lapse → every downstream ripple through registered Keys. Faithful in S3, S4, S7. The w_d-shield-then-unshield dynamic is a genuine emergent feature. Its *interaction* with §3.3c is where trouble lives, not the item. |
| **§3.3c Seggio Council** | **BREAK** | S3: terminal lock. The only override is "seized by force" and the **governance layer has no force/seizure resolver**, so the central heresy investigation is unadjudicable for a full arc — the player can Investigate forever and never Hold Court. Recurs S5 (hardened rival foothold, Quo-Warranto-immune), S6 (Seggio blocks a needed verb-method). **(Note: a force resolver may exist at combat/mass-battle scale; the gap is the absence of a *governance-scale* seizure/emergence path, or a bounded non-force override.)** |
| **Π homeostat + R-4 band cliff + draw engine** | **HOLD as physics / DANGEROUS as tuned** | Draw-count `1+floor(Π/3)`, band→family mapping, and the Π 7→8 Intrigue→Crisis cliff all fired as specified (confirmed live in 4 seeds; S1 sat on Π7 and a single failed vote tipped it). But **no Grudge decay and no circuit-breaker** past the cliff → self-sustaining death spiral. See §5. |
| **Mandate derivation / feedback (§1.8)** | **BREAK at scale** | S6 refutes the cross-scale premise (§2 Pattern H). Also degenerate for single-settlement holdings (S4, S5: K=6 pins Mandate ~1 and perversely drains PS from a collapsing town nominally "above" its own Mandate). |
| **Event deck** | ⇩ **STRAIN (was BREAK)** | **§0.1 correction:** Crisis cards route to `d_sigma` and are resolvable; the "zero resolvable" claim was a digest artifact. Residual: uneven per-branch delta tables — a completeness-audit polish item. |

---

## §2 · Recurring failure-cascade patterns (depth-3 traces)

These are **emergent dynamics of the sim**, independent of digest fidelity — the core yield. Each is the L1→L2→L3
shape that recurred across seeds.

- **Pattern A — Demotion spiral (7/7, universal).** Any negative-Need/positional resolution_quality Key → (L1)
  rank held, Key logged → (L2) two more failures over 1–3 seasons → (L3) §1.0a Demotion fires, Appeal opens,
  **Appeal fails**. Terminal: Rosa 3→1, Aldric-Dunmark Banneret→Retainer (−2), Miriam Canon→Deacon,
  Aldric-Kronmark 3→2, Bjorn 3→1, Sigrid 4→2, Gerta 6→4. **The tragic-downfall arc is currently the default, not
  an edge case.** (Softened slightly by §0.3: mid rolls are ~55%, not ~48%, but the universality holds.)
- **Pattern B — Π runaway / no circuit-breaker (~6/7).** Blocked ambition or accumulating Grudges → Grudge
  written → Π climbs, Intrigue weight rises → crosses the R-4 cliff and **pins** (no Grudge decay, no valve):
  S5 pinned at Π10 for 3 seasons (explicit death spiral), S1 pinned by 3 durable Grudges, S7 held 10.
- **Pattern C — Compact/Assessment lock-in during a *worsening* crisis (~4/7: S4, S5, S6, S7).** Survey locks
  assessed_base at pre-crisis Prosperity → Fiscal Stance reads the stale figure → Prosperity falls → town
  stripped below subsistence, no reversal ~8 seasons, **no defined below-subsistence state.** A *deterministic*
  strip, not a probabilistic risk.
- **Pattern D — Collective-Liability cell-revolt stacking (~6/7).** Bind the Cells → one infraction → Collective
  Liability (whole-cell Disp−1) → stacks to 3 → Cell Revolt Crisis (Order→0/1, PS collapse, secession-class in
  S6). The Order tool becomes the crisis engine.
- **Pattern E — Patron-lapse un-shielding the queued Demotion (~4/7: S4, S5, S7; the §5.5 template).** w_d-high
  governor accrues negative Keys under protection → §3.3b Za-lapse pulls the shield → shielded Keys convert *en
  masse* to Duty-failure → Demotion. The governor is undone by an event they did not author. Elegant; also means
  standing can rest entirely on a variable outside the player's control.
- **Pattern F — Clerk-Corruption loaded gun (~6/7).** Retain Clerks → hidden counter starts, +1 AP → Treasury
  leaks, Intrigue weight rises, failed Investigates raise concealment (positive feedback, no cap) → entrenched
  clerk becomes an independent power center / public-scandal −2 Demotion vector.
- **Pattern G — Absentee/Defy → Suspicion → Recall on an undefined threshold (~3/7: S1, S2, S7).** Repeated Defy
  or absentee status → Suspicion accrues (increment undefined) → Recall fires at a **threshold nobody defined**
  (S2 ran the whole Recall on fiat).
- **Pattern H — Cross-scale Mandate drag REFUTED (S6 headline; degenerate S4, S5).** Peripheral settlement
  collapse *should* pull Mandate down to signal it. Actual: `Mandate = clamp(round(7T/(T+6)))` is saturating and
  Seat-dominated (W11 vs W2–3), so Kolstad's revolt→secession moved rounded Mandate **not at all** (held 5). Worse,
  §1.8 L-feedback **inflated** the dying settlement's Legitimacy (Kolstad L 3→4 *while in open revolt*). **The real
  cross-scale collapse carrier is the Standing/resolution_quality Key and the ledger tags — not Mandate.**

---

## §3 · Gap catalogue (re-tiered after §0 verification)

**CRITICAL**
- **§3.3c Seggio "seized by force" with no governance-scale force/seizure (or bounded non-force override) resolver.**
  Terminal lock; core investigation unadjudicable for a full arc. (S3; recurs S5, S6.)

**HIGH**
- **§1.3a — no subsistence floor / circuit-breaker; ~8-season cooldown outlives the crisis; below-subsistence terminal
  state undefined** (no depopulation/Prosperity-floor/settlement-death engine). (S4, S5, S6.)
- **Π homeostat — no Grudge decay and no circuit-breaker past the R-4 cliff.** Death spiral. (S1, S5, S7.)
- **§1.3b vs §4.5 actor-cap collision (SE-JP1).** Bind-the-Cells non-executable on small/frontier settlements; assumes
  a population-granularity layer the settlement schema lacks. (S2, S3, S6; forced S4.)
- **§5 resolution_quality mis-scores a sanctioned Defy as Duty-failure.** Corrupts every Demotion count involving a
  blessed verb. (S2.) *(Verify against §5 text.)*
- **Mandate saturation + L-feedback hides peripheral collapse; single-settlement Mandate degenerate.** (S6, S4, S5.)
- **Territory-scale governor AP economy undefined** (pool / serial / per-settlement cap). The "AP triage" premise rests
  on an unspecified rule. (S6.)
- **§1.0d audit vs Recall double-path unreconciled; "Missed Obligation" undefined.** Audit protection illusory. (S7.)
- **§3.3b × §3.3c asymmetry** — patron-lapse strips the reform-aligned player while hereditary Seggi are
  revocation-immune; no symmetric non-revocable footing for a patron-dependent actor. (S3.)
- **`d_sigma` legible-vs-engine odds divergence** (§0.4) — the deck's promised +10%/pt legible odds ≠ `sigma_leverage.p_success`
  continuous CDF. Reconcile which is canon at the tails. (All d_sigma rolls.)
- **No character attribute block supplied in any seed** (Cognition/Charisma/History/…). Every pool size was
  engine-assigned — **no dice validation is possible until this exists in the seed/roster spec.** (S1, S3, S5, S6, S7.)

**MEDIUM**
- Clerk Capacity: CC scaling, Corruption→Intrigue increment, defection-severance undefined. (S3–S7.)
- Suspicion→Recall threshold + per-Defy increment undefined. (S1, S2.)
- Recognition Fork: NPC-granter decision-rule; orphaned New-Grant fate. (S1, S7.)
- Appeal specified Piety-Track-only; non-Church factions have no track; Std-7 adjudicator may not exist in a
  one-faction frame. (S6, S4.)
- No re-patroning path for a lapsed Za charter. (S5.)
- No anti-gouging / price-control verb during famine. (S4, S6.)
- Absentee governor: no in-settlement resolution penalty or delegate-of-record. (S7.)
- Territory card volume > AP response budget; no rule for unhandled cards. (S6.)
- Compact-vs-Directive precedence undefined. (S2.)
- Predicate-unsatisfiable card dealt with no whiff/reshuffle rule. (S2.)
- **§1.3c sub-threshold presentment has no fallback resolver** (the surviving residual of §0.2). (S1, S3.)

**LOW / verify**
- **Event-deck per-branch delta completeness** (the corrected §0.1) — uneven stat-delta tables across Crisis/mid cards;
  audit for completeness, but Crisis cards *are* resolvable via `d_sigma`. (S2, S3, S4, S6.)
- Weight double-count in a card delta (EVT-OPP-03 Prosp+1 already yields Weight+1 via derivation). (S1.)

---

## §4 · Vindicated rejected proposals

Of the 14 cuts, the sim produced **one clean `resolves=yes`** and a cluster of recurring `partial`s. **Honesty
caveat that recurred:** in several places the real fix is a **KEPT** item, not a cut — do not reinstate a cut
where a kept item already owns the fix.

| Proposal | Gap it addresses | Result | Recommendation |
|---|---|---|---|
| **IT-3 The Sforza Gambit** | Rival converts economic foothold → sovereignty (S5); force-seizure path for a hardened Seggio privilege (S3, S6) | **YES (S5)** + partial ×2 | **Reconsider — strongest reinstatement candidate.** Play reproduced its exact end-state with no resolver to cover it. A *bounded* force-seizure/emergence resolver is the missing piece behind both the §3.3c terminal lock and the rival-capture dead-end. Down-scope it from the "unbuilt emergence pipeline" it was cut against. |
| **VEN-SE-4 Dedizione** | Mid-tenure negotiated extraction-cap-for-loyalty (S2 Compact-vs-Directive, S4 crisis floor, S5 re-patroning, S6 subsistence) | partial ×4 | **Reconsider.** The most *recurring* partial — a mid-tenure negotiated cap binding on a superior authority is a shape the corpus lacks (its stated duplicate SE-5 fires only at annexation). Pair with the §1.3a floor work. |
| **VEN-SE-7 Sindici Inquisitori** | Roving Π-suppression audit floor for Suspicion→Recall (S2); unifying audit vs Recall (S7) | partial ×2 | **Reconsider for the absentee/suppressed-Π case specifically.** Its roving-frequency floor is exactly what Bind-the-Cells' deliberate Π suppression evades; its independent archive is what the §1.0d double-path reconciliation needs. Not a general add. |
| **VEN-FA-2 Ducal Chancellery** | Explicit AP-buffer accounting that Clerk Capacity omits (S2–S5) | partial ×4 | **Keep-cut on pillar grounds, harvest the spec.** Correctly cut to preserve the AP-scarcity pillar; do NOT reinstate the buffer, but its accounting semantics are exactly the CC-scaling/cost definition §1.1a needs. |
| **BYZ-4 Eparch price/wage regulation** | Anti-gouging price control during famine (S4) | partial (S4), no (S6) | **Reconsider the price-control half only.** Famine seeds have no lever to curb hoarder profiteering; the rest of BYZ-4 was a correctly-cut grab-bag. |
| **BYZ-1 Office/Dignity split** | Title-vs-standing-number mismatch (S1) | partial | **Reconsider narrowly** for the labeling problem (its cut rationale looked weaker under play), **but it does not supply any missing rung** — the §0.2 correction shows there was none to supply. |
| Others (BYZ-2, CHN-1, VEN-FA-1, FA-JP1, BYZ-5, HAB-2, IT-4, VEN-SE-6/1, HRE-1) | various | partial/no | **Keep-cut.** Each names an adjacent shape but the fix lives elsewhere (kept BYZ-6 / a Church escalate verb / the §5 scoring or severance rules / off-target). Detail in the workflow synth log. |

---

## §5 · Balance observations (for tuning)

- **The demotion spiral is near-deterministic given roll cadence.** Governors face 3–4 major rolls/season, most at
  **~40–60%** (per the ground-truth engine, Appendix A — mid `dice_pool` rolls are ~55%, `d_sigma` FLOOR .05/CAP
  .90). Over 5 seasons, *never* logging the 3 failures that trip §1.0a is negligible. If some governors are meant to
  survive: raise the failure count, lower roll cadence, or let successes actively *retire* prior failure Keys.
- **Appeals essentially never succeed: 0/6 across seeds** (~20–31% vs a Std-7 adjudicator, often with Reputation
  penalties stacked). If the Appeal window is meant to be a real remedy, the adjudicator Ob is too high.
- **R-4 band cliff (Π 7→8) is a real dramatic feature but has no relief valve.** Live in 4 seeds. Discrete
  Intrigue→Crisis jump + no Grudge decay + draw-count scaling with Π = self-sustaining death spiral. **Wire the
  already-KEPT VEN-SE-5 Scuole Grandi ceilinged Π-valve**, and/or add a transition band or Grudge half-life. Highest-value single tuning lever.
- **§1.3a stale-high Assessment is a deterministic strip, not a risk.** A subsistence-floor *clamp* on extraction
  (not a balance number) is the fix.
- **Mandate saturation `round(7T/(T+6))` masks the exact collapse it should surface** and §1.8 L-feedback inflates a
  dying settlement's Legitimacy. Add a below-subsistence penalty/floor term, or formally designate Standing/tag Keys
  (not Mandate) as the cross-scale collapse carrier and stop asking Mandate to do that job.
- **Clerk Capacity is a strict trap at low CC** (net-zero AP while arming a hidden liability) — a negative-EV button
  only an uninformed player presses.
- **`d_sigma` odds calibration (§0.4).** Decide whether the deck's legible +10%/pt is the contract (and make the engine
  match it) or `sigma_leverage.p_success` is (and make the deck stop promising linear odds). They diverge at the tails.

---

## §6 · Prioritized findings for Jordan

Re-ranked after §0 verification (the deck-Crisis and §1.3c items dropped from the top; the structural items rose).
Ranking = severity × recurrence × blocking-ness.

1. **Reconcile §3.3c Seggio irrevocability** with a bounded non-force override (or a refer-up verb), and scope a
   **bounded governance-scale force-seizure/emergence resolver.** CRITICAL terminal lock (S3 unadjudicable for a full
   arc). **→ author-new + reinstate IT-3 (down-scoped).**
2. **Fix the §1.3b vs §4.5 actor-cap collision (SE-JP1) in-PR.** NERS MERGE flag confirmed hard; blocks the marquee
   escalation across 3 seeds and assumes a population layer the schema lacks. **→ refine-then-ratify.**
3. **Add a subsistence-floor clamp to §1.3a; define the below-subsistence terminal state; allow a reversal verb /
   shorten the cooldown.** Deterministic strip in 4 seeds. **→ refine-then-ratify + author-new.**
4. **Fix the §5 resolution_quality mis-scoring of a sanctioned Defy** (verify against §5 text first). Small,
   high-leverage — corrupts every Demotion count involving a blessed verb. **→ verify-then-refine.**
5. **Wire a Π relief valve (KEPT VEN-SE-5) and/or an R-4 transition band + Grudge decay.** De-fangs the death spiral
   and the near-deterministic demotion cascade behind 3 seeds. **→ refine (wire an existing kept item).**
6. **Define the territory-scale governor AP economy (wire KEPT BYZ-6) and add a Mandate below-subsistence term / fix
   the L-feedback inversion.** The S6 cross-scale premise is refuted until both exist. **→ refine.**
7. **Reconcile the §1.0d audit vs Recall double-path and define "Missed Obligation."** NERS CHN-9 merge confirmed
   correct-in-direction but under-executed. **→ refine-then-ratify** (consider VEN-SE-7's independent-archive fragment).
8. **Reconcile the `d_sigma` legible-vs-engine odds divergence** (§0.4). New finding; decide the canonical odds contract.
   **→ decide + refine.**
9. **Supply a character attribute schema in the seed/roster spec.** Input-completeness gap — no dice validation is
   possible while every pool is engine-assigned. **→ author-new.**
10. **Specify Clerk Capacity CC-scaling, Corruption→Intrigue increment, and defection-severance** (harvest VEN-FA-2's
    accounting *without* adding its AP source). **→ refine.**
11. **Define the Suspicion→Recall threshold and per-Defy increment.** A missing constant that decided real outcomes by
    fiat in 2 seeds. **→ author-new (constant).**
12. **Audit event-deck per-branch delta completeness** (the corrected §0.1 — NOT "author 49 cards from scratch"; Crisis
    cards resolve via `d_sigma`, but per-branch stat-delta tables are uneven). **→ verify + polish.**
13. **Author a §1.3c sub-threshold-presentment fallback resolver** (the §0.2 residual) and **reconsider VEN-SE-4 /
    BYZ-4 price-control** for the famine/coercive-extraction case. **→ author-new (edge) + reconsider-cut.**

**Bottom line.** The **resolution substrate earned ratification** — across 7 adversarial seeds it produced a
coherent, unauthored downfall arc entirely through the 5 primitives, and the two NERS-flagged items (§1.0d, §1.3b)
had their MERGE verdicts **confirmed**. Do **not** ratify §1.3a's failure-mode, §3.3c, or Mandate-at-scale as-is —
they are dead-ends by construction. But **discount the two loudest "author-everything" alarms**: the deck's Crisis
band and §1.3c are *not* holes in canon — they were holes in the compressed kernel the sim ran on. The verification
layer (§0) is the reason this run is trustworthy: an unverified stress test would have sent authoring effort at two
phantom gaps while under-weighting the real structural ones.
