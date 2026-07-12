# Re-evaluation — China & Byzantium

**Scope.** All STEP-3 KEPT proposals tagged `CHN-*` or `BYZ-*` in
`comparative_governance_research_v1.md` (44-item KEPT batch), re-judged against the newly-discovered
BUILT substrate (`sim/territory/`, `goldenfurt_slice/`, `settlement_mgmt_stress_01`) rather than only
against design-doc-internal duplication. Prior verdicts are pulled from
`pessimist_ners_audit_v1.md`. Fourteen proposals are in scope: **BYZ-1, BYZ-3, BYZ-6, BYZ-7, BYZ-8,
BYZ-9** and **CHN-2, CHN-3, CHN-4, CHN-5, CHN-6, CHN-7, CHN-8, CHN-9**.

**Out of scope (cut at STEP-3, never reached the 44-KEPT batch, not re-evaluated here for status):**
BYZ-2 (Purchased Dignity — cut, doubly contingent on BYZ-1/HAB-2), BYZ-4 (Eparch price/wage
regulation — cut, overlaps HAB-7), BYZ-5 (Narrow-mandate sekreta — cut, redundant with HAB-4),
CHN-1 (Rank-Rung × Portfolio-Lane — cut, redundant with BYZ-1). Noted for completeness only; none of
the BUILT-work facts below bear on a cut item's un-reconsidered status.

**Reading key for "Re-eval vs built work":**
- **STILL-VALID** — built substrate neither duplicates nor contradicts the proposal; NERS verdict's
  reasoning is undisturbed by the new facts.
- **REDUNDANT** — built code (or a design-doc surface the built facts confirm as live) already does
  the job.
- **COLLIDES** — proposal's naming/schema conflicts with something the built code actually shipped.
- **RECONCILE** — proposal and built substrate touch the same surface but neither strictly subsumes
  the other; a merge/rename/anchor step is needed before authoring.
- **SUPERSEDED** — built work makes the proposal's premise obsolete outright.

---

### BYZ-1 — Office/Dignity split

- **Original mechanic:** Forks the single Standing stat into revocable Office + sticky Dignity,
  producing new states (disgraced-but-titled Office 0/Dignity 5; jumped-up Office 4/Dignity 1) and
  re-scoping §1.0a so Severe strips only Office while Total strips both.
- **Prior NERS verdict:** **DISTILL** (confirmed). N survives — no existing mechanic (§1.0a lay-status
  floor, §1.0b Recognition Fork, Guild Upstart tag) jointly covers the decouple. But it fails
  independently: **M-6** (re-scoping §1.0a's Default/Severe demotion to no longer touch
  stipend/seating/marriage unprices ED-776's calibrated stakes system-wide), **Mu-alpha** (banked peak
  Dignity is inert against all but rare Total triggers), **T-fail** (silently alters ED-776's effect
  across every ladder + the Part 9 parity table). Follow-up: retire the standalone §1.0b section;
  extend the lay-status floor **only to Total-magnitude triggers**, keep Default/Severe at full ED-776
  weight, reuse the Upstart single-tag pattern for the jumped-up-administrator case.
- **Re-eval vs built:** **RECONCILE — naming/pattern echo with the inert `legitimacy`/`popular_support`
  fields.** The built `registry.py` Settlement schema already carries a two-number
  revocable/sticky-shaped pair — `legitimacy`/`popular_support`, 0–7 — but both are **INERT (never
  read/written in `sim/`)**, a known port-blocking gap. BYZ-1's Office/Dignity is a *different* axis at
  a *different* scale (individual FA-rank identity, not settlement state) and is not literally the same
  mechanic, so this is not REDUNDANT — but the two "decoupled sticky-vs-revocable prestige pair" shapes
  now coexist in the corpus (one on paper, one dormant in code), and whoever eventually wires
  `legitimacy`/`popular_support` will be tempted to reach for BYZ-1's vocabulary. The built-work fact
  doesn't touch NERS's M-6/Mu-alpha/T-fail findings, which are pure ED-776-scoping problems unrelated
  to the sim.
- **Changes verdict?** No — the DISTILL rationale is untouched by the built facts. Adds one
  authoring-time constraint: if/when BYZ-1's Total-only kernel is eventually authored, its terminology
  must stay visibly distinct from `legitimacy`/`popular_support` so a future port pass doesn't conflate
  an FA-rank prestige split with the still-unwired settlement fields.
- **Consolidated recommendation:** reconcile-first, then refine. Retire the standalone §1.0b section per
  NERS; when the Total-magnitude-only kernel is authored, explicitly disclaim any relationship to the
  inert settlement `legitimacy`/`popular_support` pair to head off a future naming collision.

### BYZ-3 — Guarantor Guild entry

- **Original mechanic:** Joint-liability sponsorship at the Guild §2.5 Std-0 entry gate — a scarce,
  spendable social-collateral resource (guarantor Disposition stake), a "Vouched-For" tag, and a
  burned-twice lockout. Landed together with IT-8 per S-4 (guild ladder entry/mastership fork).
- **Prior NERS verdict:** **REFINE** (confirmed). N genuinely strong — suretyship that transfers a
  player's future-misconduct cost to a third party is absent from the corpus's only other sponsorship
  mechanic (Mentor Relationship, pure training bonus, no cost transfer). Omega-d holds. The defect is
  **non-executable magnitudes**: "a Disposition hit," "double weight" (of an unstated base), "raises Ob
  on future sponsorships" are three unquantified numbers where the corpus convention (and BYZ-3's own
  landed twin IT-8) uses exact figures. Plus the pre-existing Gu-Std 0 "Mentor" cell is unreconciled.
- **Re-eval vs built:** **COLLIDES (partial) — "Vouched-For" as a proposed new tag family vs. the
  closed built `TAG_KINDS` enum.** `ledger.py` ships exactly five tag kinds — `{Precedent, Grudge, Debt,
  Reputation, Leverage}` — no sixth slot exists in code. A standalone "Vouched-For" tag, as currently
  worded, would either require extending the shipped enum (a real schema change, not a documentation
  add) or — more consistent with existing practice — should be authored as a typed instance of an
  existing kind. Joint-liability suretyship (a claim against the guarantor redeemable on the
  sponsored party's misconduct) is a **Debt** or **Leverage** shape, not a new primitive; PR#119's
  §1.3a "Compact" attempt already shows the corpus's failure mode when a proposal invents tag
  terminology instead of typing onto the built five.
- **Changes verdict?** Yes — adds a concrete required fix beyond NERS's quantification ask: type
  "Vouched-For" onto the built **Debt** (or **Leverage**) tag kind rather than authoring it as a sixth
  kind, since the enum is closed in shipped code, not just in design-doc convention.
- **Consolidated recommendation:** refine. Quantify the Disposition hit / weight multiplier / Ob raise
  per NERS, reconcile the Gu-Std 0 Mentor cell, **and** re-type "Vouched-For" as a Debt/Leverage tag
  instance before promotion.

### BYZ-6 — Consolidated Command (Doux)

- **Original mechanic:** Pooled-AP multi-settlement governor (`AP = 2 + Σ FacilityTier`, capped),
  concentrated revolt risk (Π = max of member settlements on any bloc-wide crisis). Paired with IT-5
  (Legation Split, the Weight-threshold brake) as one governance §1.9 per S-1.
- **Prior NERS verdict:** **REFINE** (overturned DISTILL→REFINE — the dossier's premise that §6.1
  "Multi-Settlement" Stature already covers this was false; §6.1 is a player-eligibility scope gate,
  not an institutional risk/resource merger). Follow-up asked for: (a) a cap value/formula for pooled
  AP, (b) explicit §1.1a Clerk-Capacity interaction, (c) Directive/Event-Deck cadence for a
  consolidated bloc.
- **Re-eval vs built:** **STILL-VALID, and the built formula directly answers NERS's open gap (a).**
  `registry.py`'s shipped per-settlement AP formula is `AP = 2 + facility_tier` (`+1` for
  Seat/Cathedral). BYZ-6's proposed pooled formula, `AP = 2 + Σ FacilityTier`, is the *literal
  built formula summed across the member settlements* — not a coincidence, an exact structural match.
  This resolves the single biggest promotion blocker NERS flagged (no cap value/formula) with real
  numeric grounding instead of an invented cap. On the Π = max side: the built `pressure (Pi)` field
  exists per-settlement in the schema, so "bloc-wide crisis resolves at Π = max of members" is directly
  computable off shipped data — no new field needed, only a new aggregation rule (contrast with the
  built province-level `Accord = floor-average Order`, which is a *different* aggregation shape BYZ-6
  should not accidentally borrow). Per the BUILT-WORK FACTS, `march_layer` is army logistics, not a
  governor economy, and governance today is strictly per-settlement — so BYZ-6 is still genuinely new
  build work, not redundant with anything shipped; it's just no longer *uncalibrated* new build work.
- **Changes verdict?** Yes — moves this from "REFINE, blocked on an unspecified cap" toward
  promote-ready: the cap formula NERS asked for is now directly derivable from shipped code
  (`2 + Σ facility_tier` across the consolidated bloc), removing the single hardest open item.
- **Consolidated recommendation:** refine (author §1.9 jointly with IT-5 per S-1, using the built
  `2 + Σ facility_tier` formula as the pooled-AP cap and `Pi = max(member Pi)` as the crisis
  aggregation; still owes the Clerk-Capacity interaction and Directive cadence per NERS).

### BYZ-7 — Pronoia Grant

- **Original mechanic:** A revenue-claim-without-governance state — collect a settlement's tax without
  governing it, tied to a service quota, sitting governor untouched. Heritability-creep half explicitly
  flagged by its own source entry to reuse SE-4's prescription formula.
- **Prior NERS verdict:** **MERGE** (confirmed). Two independent redundancy findings: (i) the
  proposal's own source instructs reusing SE-4's formula, yet the pitch builds a standalone Precedent
  tag with its own accrual/escalation math that is mechanism-identical to §3.3a's
  `floor(charter_age_seasons/8)` + >16-season Quo Warranto; (ii) the catalogue independently groups it
  with HRE-4/Levy:Farm/Underwrite/Capital-Partnership/Foreign-Loan as one "pledge future extraction"
  family. What survives: granting revenue-without-governance to an *individual* FA rank-holder (a real
  config gap in §3.3's table). Follow-up: retire the standalone Precedent-tag machinery; add one new
  grantee-type row to §3.3, reusing §3.3a's formula verbatim, citing HRE-4's canonical pledge shape.
- **Re-eval vs built:** **REDUNDANT (unaffected either way — the redundancy is entirely design-doc-
  internal, §3.3a vs. the proposal's own standalone accrual math).** None of the BUILT-WORK FACTS touch
  §3.3a's prescription formula, the split-authority table, or FA-rank grant mechanics — `sim/territory/`
  doesn't model a rank-holder/governor split at all, only per-settlement fields. Nothing in the built
  substrate strengthens or weakens the MERGE call; it stands purely on the design-doc self-collision
  NERS already found.
- **Changes verdict?** No.
- **Consolidated recommendation:** merge-into-§3.3a (per NERS: retire the standalone Precedent
  machinery, add the one new "FA rank-holder, individual" grantee-type row).

### BYZ-8 — Oath-Bound Administrator

- **Original mechanic:** Renounce dynastic claim for delegated high office at reduced Coup Counter
  sensitivity; breakable at Total-magnitude cost. New loyalty archetype.
- **Prior NERS verdict:** **MERGE** (confirmed, corrected target). The kernel is worth keeping but as
  pitched it fails on its own terms: (i) presupposes a "barred office" exclusion axis Part 7 doesn't
  actually have (every Std-6/7 is uniformly succession-eligible today, so the oath buys access the
  character already has); (ii) its numeric hook, Coup Counter, is confirmed in unresolved numeric
  incoherence (ED-931, open). Corrected redundancy target: not §1.0c Hostage-Kin (mechanically
  distinct) but the catalogue's own flagged succession-configuration family (Partible/Elective/
  Fratricide/Oath — line 306's "one parameterized `succession_rule`" call).
- **Re-eval vs built:** **REDUNDANT, unaffected by built work.** `sim/territory/` and the Goldenfurt
  slice model settlement-scale governance (prosperity/defense/order/AP/suspicion/pressure), not
  faction-scale succession rules or Coup Counter — nothing in the BUILT-WORK FACTS bears on Part 7's
  exclusion axis or the Coup Counter's numeric coherence. The MERGE call rests entirely on design-doc
  internals (Part 7 gap + Coup Counter incoherence) that the built substrate doesn't touch.
- **Changes verdict?** No.
- **Consolidated recommendation:** merge-into-succession_rule (unify with Partible/Elective/Fratricide/
  Oath per NERS/catalogue line 306); the "barred office" half stays held — closer to drop — until Part 7
  authors an exclusion axis for it to attach to.

### BYZ-9 — Cardinal Ratification Override

- **Original mechanic:** Cross-faction lever letting Crown/Parliament override the Church College's
  Cardinal election at a legitimacy cost.
- **Prior NERS verdict:** **REFINE** (confirmed). N + Omega-d clean (no existing costed secular check on
  senior-clerical appointment). The failure is the eligibility clause — "Crown for state-recognized
  sees, or Parliament for a Hafenmark-resident Cathedral" imports diocesan structure that doesn't exist
  at the Cardinal rank (the Four Cardinals are centrally-seated functional arm-heads; the trigger
  condition never obtains for the row it's attached to). Follow-up: strike the sees/Cathedral clause;
  replace with a unified Crown-alone override hung on the existing Father Gustav Linder liaison
  channel.
- **Re-eval vs built:** **STILL-VALID — no collision with the inert settlement `legitimacy` field.**
  Worth checking explicitly given the shared word "legitimacy": the NERS entry itself specifies the
  cost as "Disposition + Precedent + CI" on the costed path, not a draw against the settlement-scale
  `legitimacy`/`popular_support` fields (which are INERT and settlement-scoped, not FA/Church-scoped
  anyway). BYZ-9 operates one layer above anything `sim/territory/` currently models (Church College
  rank politics), so none of the BUILT-WORK FACTS bear on its eligibility-clause defect.
- **Changes verdict?** No.
- **Consolidated recommendation:** refine (strike the sees/Cathedral clause per NERS; ship the
  Crown-alone version via the Gustav Linder channel). Flag explicitly in the authored text that its cost
  currency is Disposition/Precedent/CI, not the settlement `legitimacy` stat, to preempt confusion once
  that field is eventually wired.

### CHN-2 — Imperial Examination Ladder

- **Original mechanic:** The Crown Administrative-branch (§1.1b) void-filler: a non-Skyrim-Eight
  credentialing pipeline — capped pass rates, direct Standing-3 appointment skipping the sponsorship
  grind, a "Waiting Laureate Pool" resource. `needs_jordan` (does the flat branch get sub-structure at
  all).
- **Prior NERS verdict:** **REFINE** (confirmed). N strong (fills the doc-confirmed flat §1.1b gap, no
  duplicate). Two surviving defects: (i) no autonomous consequence for an unmanaged Waiting Laureate
  Pool (Q-robust — the historically load-bearing "frustrated examinees as instability" dynamic has no
  answer); (ii) the capped-passer count binds to no sim/params resolution primitive. Also: drop the
  dossier's IT-8-style stigma-tag fix (the critic showed the jinshi case is the opposite historical
  polarity — examined legitimacy carried *more* prestige, not less).
- **Re-eval vs built:** **STILL-VALID, defect (ii) unresolved by built work.** Nothing in
  `sim/territory/`, `ledger.py`, or the Goldenfurt slice models an examination/credentialing pipeline,
  a pass-rate cap, or a population-scale resolution primitive of the kind CHN-2 needs — this is purely
  FA-rank design space the sim doesn't touch. The built AP/deck/Directive machinery (Goldenfurt) is the
  closest analog for "what a real resolution primitive looks like once built" but supplies no
  ready-made hook for a *population-capped tournament* specifically.
- **Changes verdict?** No.
- **Consolidated recommendation:** reconcile-first at the `needs_jordan` layer (does §1.1b get
  sub-structure at all — still the single highest-value open rank decision per the source doc), then
  refine: specify the unmanaged-pool autonomous consequence and an actual capped-passer resolution
  procedure before promotion.

### CHN-3 — Clerk Capacity

- **Original mechanic:** A second, orthogonal AP source ("Retain Clerks," converts Wealth into AP) with
  a hidden Clerk Corruption counter discoverable only via Investigate — the corpus's only opaque-
  liability AP source.
- **Prior NERS verdict:** **REFINE** (confirmed). N unusually strong — the only mechanic anywhere that
  converts Wealth into AP, the scarcest currency. But §1.1a as landed specifies **no
  acquisition/growth mechanism and no ceiling**, so Omega-d cannot be disproven (the charter puts the
  burden on the proposal); the same 2026-07-09 pass cut VEN-FA-2's AP-buffer for exactly this reason
  ("undercuts the governance doc's core AP-scarcity pillar P1"). The hidden Corruption counter is also
  a real M-6 legibility violation — every sibling mechanic posts its cost visibly.
- **Re-eval vs built:** **RECONCILE — the built AP formula supplies the missing numeric anchor NERS
  said was absent.** `registry.py`'s shipped formula is `AP = 2 + facility_tier` (`+1` Seat/Cathedral),
  the sole AP source confirmed live in the built substrate (wired end-to-end in the Goldenfurt slice).
  This is exactly the concrete baseline CHN-3's uncapped second source needs to be bounded against —
  e.g., "Clerk Capacity adds at most `facility_tier`" — turning NERS's "no ceiling specified" complaint
  from an open question into a specifiable one. It also raises the stakes on getting the cap right: the
  500-seed `settlement_mgmt_stress_01` sweep found a **runaway-negative regime** in a world with *no* AP
  economy modeled at all; an uncapped *second* AP source layered onto the one AP economy that does
  exist (Goldenfurt's) is a plausible aggravator of exactly that kind of divergence if left unbounded,
  or — if capped against `facility_tier` — a plausible stabilizer. Either way the cap is no longer
  optional once a concrete baseline exists to cap against.
- **Changes verdict?** Yes — the built formula converts NERS's abstract "no ceiling" finding into a
  concrete, specifiable fix (`≤ facility_tier`-scaled cap against the shipped `2 + facility_tier`
  baseline), and the stress-test runaway-negative finding makes shipping without that cap materially
  riskier than the design-doc-only reading suggested.
- **Consolidated recommendation:** refine. Cap Clerk Capacity against the built `facility_tier`-scaled
  AP baseline; keep the hidden-corruption/Investigate-only discovery mechanic but log its accrual to
  the ledger (per M-6) even while its *magnitude* stays hidden from the player.

### CHN-4 — Salt Certificate (bundled with CHN-5)

- **Original mechanic:** Tradeable, geography-siloed monopoly tokens as a Develop funding option, with
  a one-way "Convert to Hereditary Franchise" door.
- **Prior NERS verdict:** **REFINE** (overturned MERGE[stub]→REFINE — the original dossier was a
  placeholder, `"test"` throughout). Critic: not a duplicate of Guild-charter (political-claimant cost
  vs. tradeable liquidity-timing token) nor Toll/Mining-Charter (different verb/trigger); catalogue
  frames CHN-4 as the *general form* those might fold into. Omega-d holds. Gap: unlike its ED-SE-00xx
  siblings it specifies no autonomous Friction/Crisis churn hook (Omega-c).
- **Re-eval vs built:** **COLLISION-adjacent — tag typing must resolve to the built `Leverage` kind, not
  "Compact."** The BUILT-WORK FACTS are explicit: `ledger.py`'s `TAG_KINDS` has no "Compact" — the
  shipped 5th kind is **Leverage**, and PR#119's own §1.3a "Compact" attempt already collides/diverges
  with it. NERS's own §5.8 flags CHN-4's bundled twin CHN-5 (and CHN-6, HRE-5) as orbiting exactly this
  "Compact" naming hazard. CHN-4's "Convert to Hereditary Franchise" one-way door is structurally a
  durable claim-tag mint — the kind of thing a careless authoring pass reaches for "Compact" to name.
  It must be typed onto the built **Leverage** kind instead.
- **Changes verdict?** Yes — adds a concrete typing constraint beyond NERS's churn-hook ask: the
  franchise-conversion tag must resolve to built `Leverage`, never an invented "Compact" kind.
- **Consolidated recommendation:** refine. Specify the autonomous churn/follow-on hook per NERS (e.g., a
  merchant-family Ambition/Petition once Certificate-Wealth or Disposition crosses a threshold); type
  the hereditary-franchise conversion as a **Leverage** tag, not "Compact."

### CHN-5 — Kaizhongfa Colonize Directive (bundled with CHN-4)

- **Original mechanic:** The batch's only calendar-driven decay clock — every existing Debt/Precedent
  tag fires on a schedule, not a trigger — pays the governor, real new timing pressure on the otherwise-
  static Comply/Bargain/Defy cost menu.
- **Prior NERS verdict:** **REFINE** (overturned MERGE→REFINE — the dossier's MERGE claim that §1.3a's
  locked-figure substrate does the same job, and the catalogue's supposed corroboration, are **both
  false on source**: §1.3a is a static, player-triggered, extract-side lock; CHN-5's rate moves
  autonomously on a campaign calendar, pays the governor, and the value-flow is inverted. The catalogue
  actually lists CHN-5 among items it does *not* materially touch — the dossier's "corroboration" was
  fabricated). Follow-up: specify Bargain/Defy interaction with the decay clock, pause/tick timing
  during a scene, rule out Certificate-hoarding dominance; flag possible Class-A reclassification.
- **Re-eval vs built:** **RECONCILE — the built `pressure (Pi)` primitive is the natural home for an
  autonomous per-settlement clock, and Goldenfurt already solved its worst failure mode.** CHN-5 wants
  exactly what `Pi` already is in the built substrate: an autonomous, campaign-timed, per-settlement
  value that moves whether or not the player acts. Goldenfurt's worked verification specifically
  **already solved the Pi mis-sign/death-spiral via CG-1's bidirectional-restore fix.** Authoring CHN-5
  as a bespoke standalone resolver risks re-deriving (and re-breaking) a failure mode Goldenfurt has
  already fixed once; authoring it as a Pi-modifying trigger inherits the fix for free. Separately, per
  NERS §5.8/§5.9, CHN-5 orbits the same "Compact" naming hazard as CHN-4/CHN-6 — its Debt/Precedent tag
  family must resolve to built **Leverage** or **Debt**, not an invented "Compact."
- **Changes verdict?** Yes — two concrete built-work-driven fixes beyond NERS's own follow-up: (a)
  implement the decay clock as a modifier on the built `Pi`/pressure primitive, reusing the CG-1
  bidirectional-restore fix, rather than a from-scratch resolver; (b) type its tag family as
  Debt/Leverage, not "Compact."
- **Consolidated recommendation:** refine. Hook the autonomous decay clock into the built `Pi` pressure
  primitive (inheriting CG-1's death-spiral fix); resolve tag typing to Debt/Leverage; keep the Class-A
  reclassification flag open for the authoring pass.

### CHN-6 — Gongsuo Registration

- **Original mechanic:** A symmetric visibility/exposure toggle — unregistered = invisible, untaxable,
  unadjudicable; registered = adjudicable, Levy-eligible, but opens a "Squeeze" Friction card. Neither
  state dominates.
- **Prior NERS verdict:** **MERGE** (confirmed). Self-assessment that it "rides entirely on existing
  machinery" is wrong on inspection, but for redundancy reasons that argue for merging, not keeping
  standalone: (i) same-day §1.3c Hold Court/Precedent canon already resolves guild disputes with **no**
  registration precondition — CHN-6 silently contradicts it; (ii) "Squeeze" is verbatim the already-
  landed §1.1a Clerk-Corruption Intrigue trigger; (iii) "guild wealth" ignores the §1.3a `assessed_base`
  substrate built one section earlier; (iv) the 1-AP, no-roll, no-cooldown toggle is freely reversible
  (flip on for a Levy season, flip off before Squeeze fires) — a specification-baked Omega-d/M-6 gap;
  (v) targets a stale insertion point. Also orbits "Compact" naming (§5.8/§5.9). Follow-up: fold
  registration into §1.3c as a gating precondition; resolve "guild wealth" via §1.3a Assessment; retire
  "Squeeze" in favor of the §1.1a Clerk-Corruption trigger.
- **Re-eval vs built:** **RECONCILE, plus a new dependency the built substrate surfaces.** The built
  `suspicion` field on Settlement is the concrete analog for exactly the exposure axis CHN-6 wants
  ("invisible/untaxable" vs. "adjudicable/exploitable"), reinforcing NERS's own finding that "Squeeze"
  duplicates the Clerk-Corruption trigger rather than needing a bespoke card — `suspicion` is the field
  that trigger should already touch. Separately, the 500-seed stress sweep's root finding **F1**
  (Village/Fortress-City/Cathedral-City type taxonomy undefined in §1.2) is directly load-bearing here:
  a registration toggle's consequences plausibly differ by settlement type (a Cathedral-City's guild
  register behaves differently from a Village's), and that per-type behavior has no defined taxonomy to
  hang off yet.
- **Changes verdict?** Yes — adds a hard precondition NERS didn't have visibility into: CHN-6 cannot be
  meaningfully merged into §1.3c until F1's settlement-type taxonomy is resolved, since the merge target
  itself needs to know which settlement types the registration precondition applies to.
- **Consolidated recommendation:** reconcile-first (resolve F1 type taxonomy), then merge-into-§1.3c per
  NERS (registration as a gating precondition; "guild wealth" via §1.3a Assessment; "Squeeze" retired in
  favor of the built `suspicion`-driving Clerk-Corruption trigger).

### CHN-7 — Chancellery Gatekeeper

- **Original mechanic:** A named NPC sitting between the Provincial Authority and the governor who can
  silently substitute a harsher Directive than the one actually issued — a genuinely new information-
  asymmetry failure mode (comply in good faith with an order that was never real). `needs_jordan` (tone
  fork). CHN-8 is contingent on this proposal (plus CHN-2).
- **Prior NERS verdict:** **NOT ADJUDICATED.** Per the audit's own coverage caveat, CHN-7
  (`ED-SE-0035`) hit transient structured-output failures across all three workflow passes and was
  filed as carried-forward rather than re-run further; no verdict exists to confirm or overturn.
- **Re-eval vs built:** **RECONCILE — Goldenfurt is the first real Directive-pipeline substrate CHN-7
  has ever had to attach to.** The Goldenfurt slice is a worked, 32-finding-verified Town with 9 named
  actors and a 28-card deck that "wires Directive Comply/Bargain/Defy + AP economy" — this is the
  concrete built analog of the exact surface CHN-7 proposes to intercept (a Directive issued by a
  Provincial Authority, received by a governor). Before this, CHN-7 was pure design-doc speculation with
  no built pipeline to test against; now there is one, with a real named-actor roster to check the
  Gatekeeper role against. Two open questions the built work raises concretely: (a) does the Gatekeeper
  need to be a 10th named actor, or can it be modeled as a role one of Goldenfurt's existing 9 already
  plays; (b) `npc_ids` is an unbounded list at the schema level (no actor cap in general code), but
  Goldenfurt's *worked* slice deliberately caps at 9 — CHN-7 needs to state which convention it's
  targeting.
- **Changes verdict?** N/A (no prior verdict exists to change) — but the proposal's evaluability has
  materially improved: it now has a concrete built Directive/actor substrate to adjudicate against
  instead of none.
- **Consolidated recommendation:** reconcile-first. Before this proposal can even receive its first real
  NERS pass, adjudicate it against Goldenfurt's worked Directive pipeline and 9-actor roster (does the
  Gatekeeper add a 10th actor or reuse an existing role); it still owes both the deferred NERS
  adjudication and its original `needs_jordan` tone decision.

### CHN-8 — Institutional Purge (Bloc)

- **Original mechanic:** A bloc-scale §1.0a trigger demoting a whole credentialed ideological cohort at
  once, wielded by CHN-7's chokepoint NPC — new because every existing trigger keys to one individual's
  conduct. Contingent on CHN-2 + CHN-7.
- **Prior NERS verdict:** **PRUNE** (hardened from DISTILL — the one case where adversarial scrutiny
  found the *dossier too lenient*). CHN-8 as specified is a **costless, contest-free, wielder-
  unaccountable, undetectable mass-purge switch**: it fires unilaterally off a third party's Disposition
  with no defense roll and no backlash (unlike its cited sibling Denounce-as-Heretic's acquittal-
  backlash), and inherits total invisibility from CHN-7. That's exactly the Omega-d "free win" the
  charter routes to CUT/PRUNE. Aggravating factor: four later proposals (A4 Household Roster, A9
  kul-escheat, D3 Reign-Bound Cohort Purge, Cohort Capture) depend on CHN-8 as a generalized
  `coalition_purge` primitive reused *verbatim*, so the gap propagates wholesale into all four. Follow-
  up: block downstream reuse until CHN-8 specifies a real non-dominance cost/backlash, a telegraph (or
  justified zero-telegraph + compensating cost), and a leader-tier appeal threshold.
- **Re-eval vs built:** **REDUNDANT-of-a-fix — the built Goldenfurt slice already demonstrates the
  exact safety-valve pattern CHN-8 is missing.** Goldenfurt's worked, verified solution to the
  structurally adjacent "unaccountable hostile-actor escalation" problem — the recall death-spiral — is
  a three-part pattern: **(1)** a capped increment (suspicion capped at +1/season), **(2)** an escape
  hatch (G606 Submit-to-audit), **(3)** a counter-weight (Reputation:Just lowers recall Ob). CHN-8 as
  pitched has **none** of these three — no cap, no escape, no counter-tag — which is a concrete,
  built-precedent confirmation of exactly the missing-safety-valve diagnosis NERS's PRUNE rests on. This
  doesn't overturn PRUNE; it corroborates it with a working counter-example that shows the corpus
  already knows how to fix this class of problem and CHN-8 simply doesn't use the pattern.
- **Changes verdict?** No — reinforces PRUNE. Supplies a concrete repair template (capped increment +
  escape hatch + counter-Reputation, mirroring G606/suspicion) for CHN-8 and its four dependents if the
  mechanic is ever revived.
- **Consolidated recommendation:** drop (per NERS PRUNE, confirmed and strengthened by the built
  Goldenfurt safety-valve precedent). If revived: mandatory suspicion-style cap, a Submit-to-audit-style
  escape hatch, and a Reputation-style counter-weight before A4/A9/D3/Cohort-Capture may reuse it.

### CHN-9 — Kaochengfa Performance Audit

- **Original mechanic:** An optional patron-imposed triplicate-ledger toggle that speeds both demotion
  and promotion and auto-lapses when the imposing patron falls — a "patron-durability bet" riding
  existing Obligations/Demotion columns.
- **Prior NERS verdict:** **MERGE** (confirmed). The demotion clock reproduces §1.0a's existing "Default
  magnitude: one rank" endpoint (both terminate at Demotion-Magnitude-1 on a ~3-season horizon) — its
  "Waiting Order @1 season / patron review @2" are timestamps on the way to a pre-existing endpoint with
  no independently specified mechanical consequence (Reskinned attractor, M-4). Its headline "speeds up
  demotion **and** promotion" is **not a rule** — a full-document grep finds no promotion cadence/
  formula anywhere in the corpus; line 141 asserts it but supplies nothing executable. The claimed
  patron-durability bet is already live and universal via §1.0 point 7 (Mentor Relationship). Omega-d
  unrebutted: toggling it on costs the imposing patron nothing. This is one of the **two MERGE verdicts
  requiring deletion of already-landed subsections** (§1.0d), a live PR-blocking issue per CLAUDE.md's
  ED-1094 default-ratification rule.
- **Re-eval vs built:** **STILL-VALID, unaffected by built work.** `sim/territory/` and Goldenfurt model
  settlement-scale prosperity/defense/order/AP/suspicion/pressure — nothing in the built substrate
  models FA-rank promotion cadence, and the built facts supply no promotion-resolution primitive that
  could retroactively back CHN-9's unquantified "speeds promotion" claim. The MERGE rests entirely on
  design-doc-internal redundancy (§1.0a's existing endpoint, §1.0 point 7's existing patron-durability
  bet) that the built facts neither confirm nor disturb.
- **Changes verdict?** No.
- **Consolidated recommendation:** merge-into-§1.0a. Per NERS: delete the standalone §1.0d subsection as
  landed (this is one of the two MERGE deletions the open PR must complete before it can be treated as
  ratified, per CLAUDE.md §2's ED-1094 rule) — no promotion-speed clause survives since no promotion
  formula exists anywhere in the corpus for it to hook.

---

## Summary table

| ID | Original mechanic (one line) | Prior NERS | Re-eval verdict | Changes prior? | Recommendation |
|---|---|---|---|---|---|
| BYZ-1 | Standing → Office (revocable) + Dignity (sticky) | DISTILL | RECONCILE (inert `legitimacy`/`popular_support` naming echo) | No | reconcile-first, then refine (Total-only kernel) |
| BYZ-3 | Joint-liability Guild-entry guarantor | REFINE | COLLIDES (partial — "Vouched-For" vs closed `TAG_KINDS`) | Yes | refine (type as Debt/Leverage + quantify) |
| BYZ-6 | Pooled-AP consolidated multi-settlement command | REFINE | STILL-VALID (built `2+facility_tier` answers the cap gap) | Yes (de-risks) | refine (author §1.9 w/ BYZ-6+IT-5, built AP formula) |
| BYZ-7 | Revenue-claim-without-governance, individual rank-holder | MERGE | REDUNDANT (unaffected) | No | merge-into-§3.3a |
| BYZ-8 | Renounce dynastic claim for delegated office | MERGE | REDUNDANT (unaffected) | No | merge-into-succession_rule |
| BYZ-9 | Crown/Parliament override of Cardinal election | REFINE | STILL-VALID (no legitimacy-field collision) | No | refine (Crown-alone via Linder channel) |
| CHN-2 | Examination-pipeline credentialing (Std-3 skip) | REFINE | STILL-VALID (no built resolution primitive to borrow) | No | reconcile-first (needs_jordan), then refine |
| CHN-3 | Wealth→AP second source, hidden Corruption counter | REFINE | RECONCILE (built `2+facility_tier` anchors the missing cap) | Yes | refine (cap vs. built AP formula) |
| CHN-4 | Tradeable monopoly certificate + hereditary franchise | REFINE | RECONCILE (tag must type as built Leverage, not "Compact") | Yes | refine |
| CHN-5 | Calendar-driven autonomous decay clock, pays governor | REFINE | RECONCILE (hook into built `Pi`/CG-1 fix) | Yes | refine |
| CHN-6 | Registration visibility/exposure toggle | MERGE | RECONCILE (blocked on F1 type-taxonomy) | Yes | reconcile-first (F1), then merge-into-§1.3c |
| CHN-7 | Gatekeeper NPC silently substitutes harsher Directive | NOT ADJUDICATED | RECONCILE (Goldenfurt = first real target) | N/A | reconcile-first vs. Goldenfurt roster |
| CHN-8 | Bloc-scale credentialed-cohort mass purge | PRUNE (hardened) | REDUNDANT-of-a-fix (Goldenfurt shows the missing pattern) | No (reinforced) | drop |
| CHN-9 | Patron-bound triplicate-ledger promotion/demotion speeder | MERGE | STILL-VALID (unaffected) | No | merge-into-§1.0a (delete §1.0d) |
