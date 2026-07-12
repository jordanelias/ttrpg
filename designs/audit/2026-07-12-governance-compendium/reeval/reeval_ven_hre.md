# Re-evaluation — Venice & HRE

**Scope:** all KEPT proposals originating from Venice (`VEN-*`) and the Holy Roman Empire (`HRE-*`) in
`comparative_governance_research_v1.md` STEP-3 (44 KEPT), re-judged against the now-BUILT
`sim/territory/` substrate (registry.py, ledger.py, goldenfurt_slice, settlement_mgmt_stress_01,
march_layer) as inventoried in this task's BUILT-WORK FACTS. Prior NERS verdicts are drawn from
`pessimist_ners_audit_v1.md`.

**Set composition.** Of the STEP-3 VEN/HRE items, `HRE-1`, `VEN-FA-1`, `VEN-FA-2`, `VEN-SE-4`,
`VEN-SE-6`, `VEN-SE-7` were **CUT** at STEP-3 (Administrative-void slot competition / redundancy with
prior SE items) and are not "kept" — they are out of this re-evaluation's scope per the task's
instruction ("all kept proposals"), but are named here so the roster is legible: nothing is silently
dropped, they were dropped upstream. **Ten** proposals were KEPT and are re-evaluated below: `HRE-2`
through `HRE-7`, and `VEN-SE-1`, `VEN-SE-2`, `VEN-SE-3`, `VEN-SE-5`.

---

## HRE proposals

### HRE-2 — Chapter Capture
- **Original mechanic:** Pre-vacancy patronage banking — a governor spends Duty-slots across seasons
  to bank "College seats owed" against a specific prince-bishopric Arm, which convert to vote-weight
  only if/when a vacancy fires in that Arm (a timing the player does not control). Proactive investment
  under uncertainty, contrasted against the existing College mechanism which is purely reactive
  (please currently-seated Prelates at the moment a vacancy exists).
- **Prior NERS verdict:** **KEEP** *(overturned: DISTILL[stub] → KEEP; steelman survived)*. The
  original dossier was a placeholder ("test" reasoning/artifact), capped at REFINE by the charter's
  own rule for un-adjudicated subtractive verdicts; the critic did the real source-work and confirmed
  N (proactive vs. reactive, genuinely distinct) and Omega-d (costs Duty-slots every season, branch-
  scoped so a wrong-Arm vacancy burns the investment) hold. Residual Q gaps (seats-owed→vote-weight
  conversion rate, decay conditions) are REFINE-grade notes, not verdict-changing.
- **Re-eval vs built work:** **STILL-VALID.** HRE-2's "College seats owed" counter is a new, narrowly-
  scoped accrual that does not touch any of the five built `ledger.py` `TAG_KINDS`
  (`Precedent, Grudge, Debt, Reputation, Leverage`) and does not read/write the inert
  `legitimacy`/`popular_support` fields on the `Settlement` schema — it is a standalone patronage
  counter, not a Ledger tag or a Mandate input. No collision surface exists in the built code for it
  to hit.
- **Changes verdict?** No. Nothing in the built substrate contradicts, duplicates, or blocks this
  mechanic; it sits outside the AP economy, the tag-kind enum, and the (inert) legitimacy fields
  entirely.
- **Consolidated recommendation:** **Ratify** as authored (with the existing REFINE-grade
  implementation notes — conversion rate, decay, §1.0b interaction — folded in at authoring time, not
  held as a blocker).

### HRE-3 — Convene the Circle
- **Original mechanic:** A new AP verb pooling Directive obligations across peer settlements, writing
  a "Circle Quota" tag callable by *any* member settlement — pitched as the corpus's first **lateral**
  (governor-to-governor) obligation/trust axis, contrasted against every existing tag being vertical
  (crown-down or settlement-up).
- **Prior NERS verdict:** **REFINE (confirmed).** N verified genuinely new (zero horizontal
  governor-to-governor cooperative mechanics exist pre-HRE-3). Two source-confirmed Q defects: (i) the
  triggering condition ("a Directive no single settlement could cheaply satisfy alone") has no
  mechanical referent — no settlement-capacity ceiling exists to test against; (ii) "Circle Quota"
  claims a sixth Ledger tag family but is mechanically thinner than a Debt variant.
- **Re-eval vs built work:** **RECONCILE** (two independent built-fact hits, both harder than the
  audit could see without the code). First, **`march_layer` is ARMY logistics, not a governor
  economy — governance is per-settlement with no multi-settlement AP economy in the built code at
  all.** HRE-3's entire premise (pooling AP/Directive obligations *across* settlements) has no
  substrate to attach to; this is not a Q-defect on the trigger condition, it is the absence of the
  layer the mechanic assumes exists. Second, the "Circle Quota" sixth-tag-family claim: built
  `TAG_KINDS` is a **closed five-member enum** (`Precedent, Grudge, Debt, Reputation, Leverage`) — the
  audit's "thinner than Compact's genuine cadence delta" comparison is itself now stale, since
  **Compact does not exist in the built ledger** (see HRE-5/VEN-SE-2 below); there is no sixth slot
  to extend into, closed or open.
- **Changes verdict?** **Yes.** The prior REFINE assumed a settlement-capacity ceiling was merely
  unspecified and a sixth tag family merely thin; the built code shows the former has no home layer
  at all (no cross-settlement AP economy exists to gate) and the latter has no open slot to extend
  (`TAG_KINDS` is closed at five, and Compact — the audit's own comparison point — isn't in code).
  This raises the bar from "fix two Q gaps" to "there is no multi-settlement layer for this to plug
  into yet."
- **Consolidated recommendation:** **Reconcile-first.** Do not author Circle Quota as a Ledger tag
  variant; either (a) scope HRE-3 down to a purely per-settlement Directive-assist verb with no
  cross-settlement pooling until a multi-settlement governance layer exists (march_layer is
  explicitly not that layer), or (b) treat "build the lateral-pooling substrate" as its own prerequisite
  authoring task before HRE-3 lands. Either way, express any accepted-obligation state as `Debt`
  (built, existing) rather than inventing a name — no open tag-kind slot exists.

### HRE-4 — Borrow
- **Original mechanic:** A financier loan secured against a *named* extractive right, spawning an
  Investigate-discoverable financier-actor; the hard clawback reuses (not duplicates) SE-4's Quo
  Warranto. Modeled as disciplined reuse against BYZ-7's parallel "pledge future extraction" shape.
- **Prior NERS verdict:** **KEEP** *(overturned: MERGE[stub] → KEEP; steelman survived)*. Placeholder
  dossier again capped at REFINE by charter rule; critic found no real duplicate — the new
  **Concession** tag differs from Debt (fires once, no named right, no autonomous actor) and from
  Compact (state-side counterparty, no capital infusion). Named one of the catalogue's two surviving
  canonical shapes that the wider pledge-family (Levy:Farm/Underwrite/Capital-Partnership/
  Foreign-Loan/BYZ-7) should collapse *into*.
- **Re-eval vs built work:** **RECONCILE**, narrower than HRE-3/VEN-SE-2. Built `TAG_KINDS` is closed
  at five (`Precedent, Grudge, Debt, Reputation, Leverage`); HRE-4's differentiation from Debt is sound
  (fires once vs. every season, named right vs. none), but the proposed **Concession** tag is, like
  Circle Quota, a *sixth* family the closed enum has no slot for. Unlike Circle Quota, Concession's
  differentiation logic survives — it is closer to `Leverage` (a held claim against a counterparty)
  than to Debt, so the reconciliation is a rename/subsumption into the existing `Leverage` kind rather
  than a structural rebuild.
- **Changes verdict?** No change to the underlying KEEP — HRE-4 remains the strongest of the
  pledge-family anchors and its Quo-Warranto reuse discipline stands untouched. But the "new tag"
  framing needs a built-fact correction before authoring: **Concession should land as a typed subtype
  of the built `Leverage` kind**, not a bespoke sixth family, mirroring the same closed-enum
  constraint that hits HRE-3 and VEN-SE-2.
- **Consolidated recommendation:** **Refine.** Ratify the mechanic; retype "Concession" onto built
  `Leverage` before authoring so the engine doesn't inherit a sixth undeclared tag kind. Keep as the
  pledge-family anchor per the audit's §5.2 topology call (BYZ-7 dissolves into it + §3.3a, not the
  reverse).

### HRE-5 — Guild Uprising (Compact/Suppress)
- **Original mechanic:** One crisis trigger, two opposite durable outcomes. Concord installs a
  permanent guild *veto* on the governor's own Develop authority, claimed to write under a "Compact"
  tag distinct from a claimed "Charter" tag; Suppression zeroes Guild Influence with a Grudge floor
  that never decays.
- **Prior NERS verdict:** **REFINE (confirmed).** N and Omega-d hold (genuine crisis-register rupture,
  seat+veto is new, not a restatement of Ratify). Two Q-smooth defects flagged: (i) tag-name
  collision — the doc's own §1.6 has no "Charter" tag, and **Compact already exists** (ED-SE-0019,
  a fixed-term extraction lock firing every season) — giving Concord's permanent seat-veto the same
  key produces two irreconcilable schemas under one name; (ii) the undecaying-floor vocabulary appears
  nowhere in §1.6's idiom.
- **Re-eval vs built work:** **COLLIDES — Concord-tag-vs-Leverage** (worse than the prior pass could
  know). The audit's fix presumed a real, landed ED-SE-0019 Compact tag that HRE-5's Concord could be
  cleanly distinguished from. **Built fact: there is no "Compact" in `ledger.py`'s `TAG_KINDS` at
  all** — the built fifth kind is `Leverage`, and PR#119 §1.3a's own Compact design diverges from/
  collides with the code. So the audit's proposed fix ("rename Concord's tag, distinguish it from the
  existing Compact") is itself now unresolvable as stated: the comparison target doesn't exist in the
  built engine. The actual collision is Concord-vs-`Leverage` (the real fifth built kind), and it must
  be reconciled against **whatever PR#119's Compact/Leverage cutover lands as**, not against a
  Compact tag that was never built.
- **Changes verdict?** **Yes.** The prior REFINE's fix path assumed a real target to rename away from;
  the built code shows that target is itself unresolved corpus-wide (Compact-vs-Leverage divergence,
  flagged as a standing collision in the BUILT-WORK FACTS). HRE-5 cannot be safely authored until the
  Compact/Leverage question is settled — its own fix is now contingent on a different, larger
  reconciliation.
- **Consolidated recommendation:** **Reconcile-first**, gated on the corpus-wide Compact-vs-Leverage
  resolution (this is the same blocking dependency VEN-SE-2 hits below — resolve once, apply to both).
  Once resolved, rename Concord's tag onto whichever kind wins, differentiate explicitly from Ratify's
  Influence-tick, and either specify or drop the undecaying-floor mechanic. `needs_jordan` carries
  forward unchanged (permanent self-constraint on player power is still a taste call), but it is now
  gated behind the tag reconciliation, not parallel to it.

### HRE-6 — Reichsacht
- **Original mechanic:** An "Outlawed" status flag with a contagion clause (harboring exposes the
  harborer) but enforcement-dependent teeth — a settlement with standing can Defy and shelter the
  outlaw, i.e. a Crown decree that can visibly, legibly fail. Cross-lane (SE status + FA Demotion
  Trigger).
- **Prior NERS verdict:** **KEEP (no steelman needed).** N clean — no existing mechanic (Defy,
  Excommunication, Collective Liability) does this job; Omega-d holds (declaring side inherits the
  cost-free existing Directive model unmodified, responding side fully costed, shelter branch costs
  *more* than baseline Defy). Two Q-smooth authoring notes, not demotions: give "Outlawed" an
  actor-scoped home distinct from the per-settlement §1.6 Ledger; generalize the §1.3b
  Collective-Liability contagion primitive.
- **Re-eval vs built work:** **STILL-VALID**, and now more implementable than the audit knew. The
  built `goldenfurt_slice` already wires **Directive Comply/Bargain/Defy** end-to-end, with a
  32-finding verification — this is exactly the "shelter branch = costed Defy" mechanism HRE-6's
  responding-side needs, no longer a design abstraction but a live, validated verb the mechanic can
  bind to directly. Additionally, goldenfurt_slice's already-solved **recall death-spiral fix**
  (suspicion capped +1/season, Reputation:Just lowers recall Ob) is directly adjacent machinery
  Reichsacht's enforcement-dependent teeth should reuse rather than reinvent, since both are
  "a punitive status that a settlement can legibly resist."
- **Changes verdict?** No change to KEEP, but the authoring notes sharpen: the "actor-scoped home for
  Outlawed" and the shelter-branch cost should be built as extensions of the existing
  Directive:Defy verb and the built `Reputation` tag kind (both real, both landed) rather than as new
  primitives.
- **Consolidated recommendation:** **Ratify**, with authoring bound explicitly to built
  Directive:Comply/Bargain/Defy and `Reputation` (existing `TAG_KINDS` member) — this is a case where
  the built substrate makes the KEEP *cheaper* to execute, not harder.

### HRE-7 — Mediatize
- **Original mechanic:** A new Immediate/Mediatized settlement-status axis (separate from ownership),
  issuable only as negotiated-settlement treaty compensation — administrative demotion without a
  battle.
- **Prior NERS verdict:** **REFINE** *(overturned: MERGE → REFINE; steelman survived)*. The dossier's
  duplicate-coverage claims against Charter, Cede, and Parliamentary Transfer all fail on source (each
  does a different job). Conceded real Q gaps: the sole delivery mechanism (a negotiated
  peace-treaty/succession payload) doesn't exist in canon (Succession Contest is
  deterministic-strength, no negotiation step), and composition with an existing Charter on the same
  settlement (both write §1.8 Legitimacy) is unspecified.
- **Re-eval vs built work:** **RECONCILE**, and the audit's second conceded gap is structurally worse
  than "unspecified" — it is **inert**. Built fact: `legitimacy`/`popular_support` exist on the
  `Settlement` schema (0-7) but are **never read or written anywhere in `sim/`** (explicitly
  port-blocking), and the §1.8 Mandate formula (`round(7T/(T+6))`) that would consume them **is not
  implemented** — L/PS inputs are inert. HRE-7's status axis is pitched as something that changes what
  §1.8 Legitimacy *means* for a settlement; but §1.8 Legitimacy has no live consumer in the built code
  at all. Authoring Mediatize now means writing a status flag that composes with a formula that
  doesn't run.
- **Changes verdict?** **Yes.** The audit treated the Charter-composition gap as a specification TODO
  alongside a missing negotiation mechanism. The built substrate reveals the composition target itself
  (§1.8 Legitimacy/Mandate) is dead code, not merely under-specified — a strictly harder blocker than
  "define the interaction," because there is currently no interaction to define against a running
  system.
- **Consolidated recommendation:** **Reconcile-first**, and sequence behind the Mandate/Legitimacy
  port-blocking fix noted in the BUILT-WORK FACTS (wiring L/PS into a live formula) — not behind
  Mediatize's own negotiation-payload gap alone. Once Legitimacy is live, re-run this REFINE; until
  then this is effectively a design-only proposal sitting on design-only substrate, and should not be
  scheduled ahead of the Legitimacy-wiring work it depends on.

---

## VEN proposals

### VEN-SE-1 — State Arsenal
- **Original mechanic:** A fourth Develop-funding method with a persistent per-settlement Wage/Pension
  Debt liability that fires every season regardless of use (distinct from event-triggered Debt), plus
  a single-NPC-zeroes-output failure mode.
- **Prior NERS verdict:** **CUT (confirmed; N plank corrected).** Steelman won on N (state production
  vs. guild-privilege is a real distinct dynamic — the dossier's duplicate-coverage claim against
  Guild-charter was overstated). Fails decisively on two independent grounds: (i) Omega-d — for +1 AP
  over base Develop it removes roll variance and doubles output while its only cost is a
  voluntarily-avoidable Treasury toll (escalation never fires), violating the section's own design law
  that growth methods must hand power to a different faction; (ii) mechanism-level tag duplication —
  the bespoke Wage/Pension Debt tag duplicates the Compact family and the catalogue's shortlist call to
  unify a single `Debt(garrison_pay)` clock across VEN-SE-1/IT-2/etc.
- **Re-eval vs built work:** **REDUNDANT** (named: built `Debt`, `ledger.py TAG_KINDS`), reinforcing
  the existing CUT rather than reopening it. The built ledger already has a live `Debt` tag kind that
  a per-season wage liability would naturally express through — there is no missing schema for the
  "persistent liability" half of the pitch, only the CUT's Omega-d objection (the AP-buffer/auto-succeed
  half) stands, and that objection is untouched by the built-substrate check. Facility-tier AP economy
  (`AP = 2+facility_tier`, `+1` Seat/Cathedral) confirms Develop-adjacent AP costs are a live, tuned
  surface in the built code — exactly what VEN-SE-1's near-free +1 AP buy would distort, sharpening
  rather than softening the CUT.
- **Changes verdict?** No. Built facts confirm both of the audit's independent CUT grounds rather than
  disturbing either: the wage-liability half has an existing built home (`Debt`) that makes VEN-SE-1's
  bespoke schema doubly unnecessary, and the AP-economy half is now known to be a tuned, live system
  the mechanic would still dominate.
- **Consolidated recommendation:** **Drop**, per the CUT. If any fragment survives, it is the
  "wage clock" idea generally — but it should be authored once as the shared `Debt(garrison_pay)`
  clock (§5.3's cross-item call, IT-2 + VEN-SE-1 + Settle-Arrears + Index-Wages), typed onto built
  `Debt`, not as VEN-SE-1's standalone auto-succeed Develop method.

### VEN-SE-2 — Boschi Pubblici Requisition
- **Original mechanic:** A new Directive type tying a province to a named production dependency (a
  supply chain, e.g. timber → Arsenal), with a Defy consequence that starves the dependent building.
- **Prior NERS verdict:** **REFINE (confirmed).** N and the strategic-resource-node concept survive
  (corroborated by three catalogue entries needing "the tag"). Two source-confirmed defects: (i) a
  fabricated dependency — the flagship Defy consequence ("dependent building loses its auto-success
  bonus") presupposes a VEN-SE-1 Arsenal auto-success bonus that does not exist in VEN-SE-1's actual
  spec, so the stated Defy cost is inert; (ii) a live Omega-d loophole — `Requisition [Strategic
  Resource]`, if a distinct Directive type, silently bypasses the §1.3a Encabezamiento/Compact
  auto-resolution.
- **Re-eval vs built work:** **RECONCILE**, same blocking dependency as HRE-5. Ground (i) is now moot
  differently than expected: with VEN-SE-1 (its dependency target) **CUT**, the flagship Defy
  consequence has no counterparty to reference at all, not merely a fabricated one — the Defy branch
  needs a different dependent-building target entirely. Ground (ii) is the harder hit: the audit
  worried about bypassing §1.3a's Compact auto-resolution, but **built fact confirms there is no
  Compact tag in code** — PR#119's §1.3a Compact diverges from/collides with the built fifth
  `TAG_KINDS` member (`Leverage`). The bypass question ("does Requisition inherit Compact
  auto-resolution or evade it?") cannot be answered until Compact-vs-Leverage is itself resolved
  corpus-wide.
- **Changes verdict?** **Yes**, on both grounds. (i) VEN-SE-1's CUT removes VEN-SE-2's own cited
  dependent target — the Defy branch must be re-grounded against a real built structure (e.g. the
  facility-tier AP chain) rather than the now-cut Arsenal bonus. (ii) the Compact bypass question is
  now provably unanswerable pending the same corpus-wide Compact/Leverage reconciliation blocking
  HRE-5 — this is not an independent Q gap, it is the *same* open architectural question surfacing a
  second time.
- **Consolidated recommendation:** **Reconcile-first**, gated jointly on (a) VEN-SE-1's CUT (pick a
  real dependent-building target for the Defy branch — a facility-tier chain is the built candidate)
  and (b) the shared Compact-vs-Leverage resolution also blocking HRE-5. Once both resolve, this is a
  clean promote-ready REFINE.

### VEN-SE-3 — Bonifiche Capital Posture
- **Original mechanic:** A fifth Ledger tag family where a military *loss* triggers an economic
  choice, and where the tag changes what *type* of extraction a Directive may ask for (liquid vs.
  land) — framed as an open gate-question on whether Ledger tag families are extensible beyond the
  original four.
- **Prior NERS verdict:** **Not adjudicated.** `pessimist_ners_audit_v1.md` explicitly carries
  VEN-SE-3 (`ED-SE-0043`) forward unresolved — it hit transient structured-output failures across
  three workflow passes and was filed out of the 41-item result per the design lead's call, pending a
  follow-up pass. No KEEP/REFINE/CUT verdict exists yet to re-evaluate against.
- **Re-eval vs built work:** **COLLIDES — "fifth family" vs. built `Leverage`.** The STEP-3 authoring
  note (`comparative_governance_research_v1.md` line 353) already flagged that the extensibility
  gate-question was answered in the affirmative in practice once Compact (ED-SE-0019) was treated as a
  landed fifth family, leaving VEN-SE-3's *own* proposed sixth family as the separate open call. Built
  fact sharpens this further: the code's actual fifth `TAG_KINDS` member is **`Leverage`**, not
  Compact — so VEN-SE-3's premise ("a fifth family") is now simply **false against the built engine**;
  it would be a sixth (or, if Compact/Leverage collapse into one, a fifth contender competing directly
  with whatever wins that collapse). Either framing requires the same Compact-vs-Leverage
  reconciliation blocking HRE-5 and VEN-SE-2 to be resolved first.
- **Changes verdict?** N/A (no prior verdict to change) — but the built-fact check materially narrows
  what a future dossier pass can conclude: VEN-SE-3 cannot be adjudicated as "add the fifth family"
  because that slot is already occupied by `Leverage` in code, independent of the still-open
  Compact/Leverage design collision.
- **Consolidated recommendation:** **Reconcile-first**, and re-file into the still-pending audit pass
  with the corrected premise (VEN-SE-3 is competing for a sixth slot in a five-deep closed enum, not
  filling an open fifth), gated on the same Compact-vs-Leverage resolution as HRE-5/VEN-SE-2. Do not
  adjudicate standalone until that shared reconciliation lands — three separate proposals now converge
  on the identical open question.

### VEN-SE-5 — Scuole Grandi
- **Original mechanic:** A caste-excluded Civic Prestige resource (0-10, tracked) that subtracts from
  the Π (pressure) homeostat only while excluded-caste Grudges drive it — a targeted, ceilinged
  pressure valve, never curative.
- **Prior NERS verdict:** **DISTILL (confirmed, one dossier plank corrected).** Steelman corrected a
  schema-gap complaint (caste is a derivable predicate over existing `actor.caste`, not a phantom
  field), but the mechanic fails on: (i) misclassification — minting a tracked resource + a new
  conditional term on a central formula is Class A, mandatorily triggering Omega-a, which the
  proposal fails by its own text ("no conversion path to any Standing or rank, ever" — self-declared
  scale-isolated/flavor-only); (ii) the doc's own freshly-ratified precedent (§1.3a Compact) shows
  persistent capped multi-season effects are built as a **Ledger tag family**, not a bespoke
  resource+formula branch; (iii) the Π homeostat band is listed as still-open balance work — the wrong
  place to add an unforced conditional term; (iv) no named actor at risk. Follow-up: retire Civic
  Prestige and its Π term; re-home as a Sponsor sub-option writing a Debt/Reputation Ledger tag,
  draining Π through the formula's existing generic release term.
- **Re-eval vs built work:** **STILL-VALID direction, RECONCILE on landing details.** Built fact
  confirms `Settlement` carries a live `pressure` (Π) field, and `goldenfurt_slice` already resolved a
  **Π mis-sign/death-spiral bug (CG-1, bidirectional restore)** on that exact field — this is a
  documented fragile surface with a known, validated fix pattern, corroborating ground (iii)'s "still-
  open balance work" call even more concretely than the audit knew: Π isn't just unbalanced in the
  abstract, it has a recent real bug on record. Ground (ii)'s re-homing recommendation (Debt/Reputation
  Ledger tag) is directly supported by built `TAG_KINDS`, which does contain live `Debt` and
  `Reputation` kinds — no reconciliation blocker here, unlike HRE-5/VEN-SE-2/VEN-SE-3's Compact
  collision, because the DISTILL's target kinds are real and uncontested.
- **Changes verdict?** No change to DISTILL, but strengthened: the Π-field death-spiral history is a
  concrete built-code reason (not just a documentation flag) to keep any caste-relief mechanic off the
  central Π formula and onto a discrete, already-validated Ledger-tag surface instead.
- **Consolidated recommendation:** **Merge-into-X** — retire Civic Prestige as a standalone resource
  and author the relief kernel as a Sponsor sub-option writing built `Debt` or `Reputation` tags,
  per the DISTILL's own follow-up, now with the CG-1 Π-fragility precedent as additional supporting
  citation for why the central formula itself must stay untouched.

---

## Summary table

| ID | Prior NERS | Re-eval verdict | Consolidated recommendation | Key built-fact driver |
|---|---|---|---|---|
| HRE-2 Chapter Capture | KEEP | STILL-VALID | Ratify | No `TAG_KINDS`/legitimacy touch — no collision surface |
| HRE-3 Convene the Circle | REFINE | RECONCILE | Reconcile-first | `march_layer` = army logistics only, no cross-settlement AP economy; `TAG_KINDS` closed at 5 |
| HRE-4 Borrow | KEEP | RECONCILE (narrow) | Refine — retype onto `Leverage` | `TAG_KINDS` closed at 5, no open 6th slot for "Concession" |
| HRE-5 Guild Uprising | REFINE | COLLIDES (Concord vs `Leverage`) | Reconcile-first | No Compact in code; built 5th kind is `Leverage`, diverges from PR#119 §1.3a |
| HRE-6 Reichsacht | KEEP | STILL-VALID (cheaper now) | Ratify, bind to built Directive verbs | goldenfurt_slice Directive Comply/Bargain/Defy + suspicion-cap fix already live |
| HRE-7 Mediatize | REFINE | RECONCILE | Reconcile-first, sequence behind Legitimacy fix | §1.8 Mandate formula unimplemented; L/PS fields inert in `sim/` |
| VEN-SE-1 State Arsenal | CUT | REDUNDANT (confirms CUT) | Drop | `Debt` tag kind already covers wage-liability concept |
| VEN-SE-2 Boschi Pubblici | REFINE | RECONCILE | Reconcile-first (2 blockers) | Dependent-target CUT (VEN-SE-1); Compact/Leverage bypass unanswerable |
| VEN-SE-3 Bonifiche Capital Posture | not adjudicated | COLLIDES ("5th family" claim) | Reconcile-first, re-file | Built 5th kind is `Leverage`, not an open slot |
| VEN-SE-5 Scuole Grandi | DISTILL | STILL-VALID direction | Merge-into-X (Sponsor + `Debt`/`Reputation`) | Π field has documented CG-1 death-spiral history; `Debt`/`Reputation` are real built kinds |

**Cross-cutting finding:** three of the ten proposals (HRE-3, HRE-5, VEN-SE-3) and one adjacent
(VEN-SE-2) independently collide with the same unresolved architectural question — **whether/how
PR#119's proposed `Compact` tag reconciles with the built ledger's actual fifth `TAG_KINDS` member,
`Leverage`** — and a closed five-member tag enum means every "new Ledger family" pitch in this batch
needs that reconciliation before it can be adjudicated on its own merits. This should be resolved once,
as a single `IN`-lane or `SE`-lane ticket, rather than re-litigated per-proposal.
