# Re-evaluation — Habsburg Spain & Italy

**Scope:** all STEP-3-KEPT proposals originating from Habsburg Spain (`HAB-*`) and Renaissance Italy
(`IT-*`), re-judged against the BUILT `sim/territory/` substrate (registry.py, ledger.py,
goldenfurt_slice/, settlement_mgmt_stress_01, march_layer, infrastructure.py) rather than against the
design-doc corpus alone. Source proposals: `designs/audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md`
(§1 STEP-3 rationale, §2 the 44-kept table). Prior NERS verdicts:
`designs/audit/2026-07-11-comparative-governance-pessimist-ners-audit/pessimist_ners_audit_v1.md`.

**Set covered (11 items):** HAB-1, HAB-2, HAB-4, HAB-5, HAB-6, HAB-7, IT-1, IT-2, IT-5, IT-6, IT-8, and
IT-7. (IT-3 The Sforza Gambit and IT-4 Cipher-Chief were CUT at STEP-3 and never entered the 44-kept
table — noted below for completeness but not re-adjudicated as live proposals. HAB-3 Reichskolleg was
likewise CUT at STEP-3, redundant-in-kind with CHN-2.)

---

## Habsburg Spain

### HAB-1 — Corregidor (outside-appointee judicial override, layered over the sitting governor)
- **Original mechanic:** A specialist appointee seated *over* the sitting governor, overriding only
  Hold Court/Investigate while the governor keeps the rest of the portfolio; term-scoped, self-expiring
  tags (rotation-driven amnesia). Extends SE-7's oversight toolkit as a distinct *layer-over* mode
  (vs. IT-1's *replacement* mode).
- **Prior NERS verdict:** KEEP *(overturned: dossier's stub MERGE → critic's KEEP; steelman survived)*.
  Dossier was a placeholder (`"test"` reasoning) — the critic supplied the real adjudication: §1.4's
  suspicion-threshold "audit" is an unmechanized stub, and HAB-1 is the first proposal to actually
  mechanize it, distinct from SE-7's Visita/Residencia/Rotation and from IT-1's Podestà.
- **Re-eval vs built work:** STILL-VALID. The Goldenfurt slice (S-006, 9 named actors) has *already
  built* a working oversight/recall loop — G606 Submit-to-audit escape, suspicion capped at +1/season,
  Reputation:Just lowering recall Ob — but that loop covers the *recall* pathway, not a concurrent
  judicial-override layer seated above a sitting governor. Registry.py's Settlement schema carries
  `suspicion` as a live, read/written field (unlike inert `legitimacy`/`popular_support`), which is
  exactly the gate HAB-1 needs to trigger on. No collision with TAG_KINDS, no collision with the AP
  formula (`facility_tier -> AP = 2+facility_tier`) — HAB-1 doesn't touch AP at all, it overrides a
  *procedure*, not a resource.
- **Changes verdict? No.** The built substrate confirms rather than undercuts the KEEP: `suspicion` is
  a real, wired field HAB-1 can gate on, which strengthens the "genuinely mechanizes an existing stub"
  argument the critic made from prose alone.
- **Consolidated recommendation:** Ratify. Author into SE-7's oversight-toolkit section citing
  `suspicion` (registry.py) as the concrete trigger field; term-scoped tag expiry can piggyback on
  whatever seasonal-tick mechanism already ages `pressure` (Pi).

### HAB-2 — Valido (informal Favorite power-track)
- **Original mechanic:** An informal power-track (Royal Intimacy + Patronage Web) built purely through
  uncapped private Audience scenes, gated at Std-4 + Royal Intimacy 3, granting routing control over
  *all* Ministry consultas — broader than Std-6's single-Ministry right and rivaling Std-7's decree
  power — that collapses binarily on Disposition ≤ −2, deliberately breaking §1.0a's graduated-magnitude
  rule.
- **Prior NERS verdict:** CUT (confirmed). Omega-d dominance failure: HAB-2 is a strictly cheaper path
  to power than the Std-6/7 gates it sits beside (no Duty, no Deed, no confirmation, no withholding
  mechanism), and the lenient STEP-3 pass had already CUT a structurally identical offender
  (VEN-FA-2's AP-buffer) elsewhere in the same batch.
- **Re-eval vs built work:** SUPERSEDED (i.e., the cut is further reinforced, not reopened). HAB-2's
  entire premise leans on a Favorite outperforming *formal Standing* by manipulating Legitimacy-adjacent
  levers — but the built registry.py schema marks `legitimacy`/`popular_support` as INERT: never read or
  written anywhere in `sim/`. A power-track pitched as an alternate route to Legitimacy-grade authority
  has *no live state to attach to* in the built code, on top of the already-fatal Omega-d dominance
  problem identified from prose alone.
- **Changes verdict? No**, but the built-work fact adds an independent, code-level reason the cut is
  correct: even a narrowed HAB-2 (the pessimist audit's suggested "single new §1.0a collapse trigger +
  Disposition-threshold flavor note, no chair-gate bypass") would currently bind to nothing, since the
  Legitimacy axis it would modulate is dead weight in the executable substrate.
- **Consolidated recommendation:** Drop (confirmed). If Legitimacy/`popular_support` is ever wired live
  (a prerequisite noted independently in §1 of the BUILT-WORK FACTS as port-blocking), HAB-2 could be
  revisited as an entirely different, narrower proposal at that time — not before.

### HAB-4 — Overlapping Consulta Arbitration
- **Original mechanic:** Inter-ministry conflict arbitration with two procedure types (Agenda-Set
  blind-framing vs. Ratify accept/veto) and a Latency-to-paralysis cost, denominated in the existing
  Competence stat.
- **Prior NERS verdict:** REFINE (confirmed). N verified strong (the six Crown Ministries are currently
  purely decorative — Competence/Corruption tracks, flavor only — and nothing arbitrates intra-faction
  sub-organ conflict). Two Q/Omega gaps: "Ministry priority action" is used as a defined term with no
  underlying action-taking capability built anywhere in Part 7, and Omega-d is consequently
  unverifiable (unclear whether a Ministry action draws the Crown's seasonal AP budget or is free).
- **Re-eval vs built work:** STILL-VALID, with a concrete resolution path the built code supplies. The
  registry.py AP formula (`AP = 2+facility_tier`, +1 for Seat/Cathedral) is the *only* live seasonal-
  budget primitive in the built substrate; the pessimist audit's open question — does a Ministry action
  draw the Crown's seasonal budget or run free — should resolve to "draws the same AP pool," reusing
  the built formula rather than inventing a parallel Ministry-AP currency. No collision: Ministries and
  their Competence tracks don't exist in registry.py's Settlement schema at all, so there is nothing to
  duplicate.
- **Changes verdict? No** on the REFINE call itself, but the built AP formula gives the "generalize into
  a domain-agnostic arbitration primitive" follow-up (needed for Suez/ABCD per the audit's §5.5) a
  concrete resource to bind Omega-d against, closing the previously-unverifiable gap.
- **Consolidated recommendation:** Refine. Author §7.1a defining "Ministry priority action" as an AP
  draw against the built `facility_tier`-derived pool (or an explicit new Crown-only pool if Ministries
  are meant to sit outside settlement AP — needs_jordan on that scoping question specifically); drop the
  dossier's `auto_manual_resolution_duality` reuse citation (confirmed wrong, no such vocabulary exists
  in that doc).

### HAB-5 — Encabezamiento (Negotiated Quota)
- **Original mechanic:** A negotiated fixed-term tax **Compact** (pitched explicitly as "the 5th Ledger
  tag") locking an extraction figure below live capacity, with a reciprocal one-Petition-per-term
  obligation for the crown.
- **Prior NERS verdict:** KEEP (no steelman needed) — one of only two clean items (with HAB-7) in the
  entire 12-item authored-into-canon set. N unusually strong: independently triangulated across five
  catalogue episodes in four civilizations; the doc's own §5 synthesis declined to spin up sibling verbs
  precisely because HAB-5 already covers the pattern. Two open questions flagged as polish-grade only.
- **Re-eval vs built work: COLLIDES — Compact-vs-Leverage.** This is the single most consequential
  built-work finding in this set. `ledger.py`'s actual `TAG_KINDS = {Precedent, Grudge, Debt,
  Reputation, Leverage}` — there is **no "Compact" tag in code**, and the built 5th tag kind is
  **Leverage**, not Compact. HAB-5 was authored (and NERS-adjudicated) assuming a "Compact" tag family
  that simply does not exist in the executable substrate; whatever landed as PR#119 §1.3a's Compact
  text diverges from what `ledger.py` actually implements. The clean KEEP verdict was evaluated purely
  against prose-doc consistency, not against the built ledger schema.
- **Changes verdict? Yes.** The mechanical content of HAB-5 (a negotiated, fixed-term, below-capacity
  extraction lock with a reciprocal petition right) is still sound and still non-duplicate — but it
  cannot be authored as "the 5th Ledger tag" when the 5th built tag kind is already spoken for by
  Leverage, and Leverage's actual built semantics haven't been checked for fit. This demotes HAB-5 from
  "ratify as-is" to "reconcile the tag-family naming/schema before ratifying," even though nothing about
  its game-mechanical soundness changed.
- **Consolidated recommendation:** Reconcile-first, then ratify. Before landing HAB-5's text: (1)
  determine whether Encabezamiento's negotiated-lock semantics fit inside the built **Leverage** tag
  (reusing it, per the repo's own reuse-discipline norm) or genuinely need a 6th `TAG_KINDS` entry; (2)
  strike or rewrite every "5th Ledger tag" citation in the HAB-5 text to match whichever resolution is
  chosen; (3) only then treat this as the two-clean-items KEEP the prior audit certified. Flag loudly per
  CLAUDE.md §2 — this is exactly the kind of held-back item that must not get silently ratified by a
  routine PR merge, since the audit's clean-KEEP language could otherwise be read as "ship as written."

### HAB-6 — Crush the Estates (permanent Consent-Rule downgrade)
- **Original mechanic:** An irreversible SE-layer action rewriting a ratified faction's rank-ladder gate
  (e.g., Hafenmark's Alderman 2/3-supermajority vote → direct crown appointment, forever) — a
  constitutional-rupture lever.
- **Prior NERS verdict:** KEEP *(overturned: dossier's PRUNE → critic's KEEP; steelman survived)*. The
  dossier's re-home target (§1.0b / FA-JP2) was shown to operate strictly post-threshold (reward-
  magnitude discretion for a candidate who already cleared the vote) with no lever to eliminate the vote
  itself — mechanically incapable of absorbing HAB-6's consequence. Omega-d holds: gated behind an
  already-damaged Grudge-threshold state, costs convertible Military+Legitimacy, imposes a permanent
  hostile-trajectory tax.
- **Re-eval vs built work:** STILL-VALID. Governance in the built sim is per-settlement (no
  multi-settlement AP economy per the march_layer note), and the `subnational` dict field in registry.py
  is the plausible built home for faction-ladder/estate-gate state at settlement scale — nothing in the
  built code implements or contradicts an irreversible rank-ladder rewrite. No collision with
  TAG_KINDS, aggregation, or AP formula.
- **Changes verdict? No.** The built substrate neither confirms nor complicates HAB-6's mechanics; it
  simply hasn't been touched yet. The one legibility gap the audit flagged (no cross-reference
  distinguishing HAB-6 from §1.0b/FA-JP2) remains the only outstanding item.
- **Consolidated recommendation:** Ratify, with the audit's one-line fix (cross-reference §1.0b to
  clarify the two operate on different axes — reward-magnitude discretion vs. vote-elimination). No
  rework, re-home, or removal needed.

### HAB-7 — Ordenanza Ratification (guild self-regulation vs. civic check)
- **Original mechanic:** Guild-authored ordenanzas generate a Petition card the governor must
  Ratify/Reject/Amend; ratifying an entry-standard clause can lock caste exclusion in as settlement
  policy — a three-branch fork using existing Hold Court/Ledger/Influence machinery.
- **Prior NERS verdict:** KEEP (no steelman needed) — the other of the two clean authored items.
- **Re-eval vs built work:** STILL-VALID. HAB-7 explicitly reuses *existing* machinery (Hold
  Court/Ledger/Influence) rather than proposing a new tag kind or resource, so it does not collide with
  the built `TAG_KINDS` set the way HAB-5 does. Registry.py's `open_needs` field is a plausible built
  hook for tracking an outstanding, un-adjudicated Petition card, though this is a convenience note, not
  a load-bearing dependency.
- **Changes verdict? No.** Unlike HAB-5, HAB-7 never claimed a "5th tag" slot, so the Compact-vs-Leverage
  collision does not touch it. It remains the cleanest item in the entire set.
- **Consolidated recommendation:** Ratify as-is. No changes required from the built-work review; treat
  `open_needs` as an optional implementation anchor for the Petition-card queue, not a gating dependency.

---

## Renaissance Italy

### IT-1 — Podestà (contracted outsider governor)
- **Original mechanic:** An outsider-contracted governor, immune to internal faction rolls, with
  appointer-liability: an end-of-term Sindacato malfeasance finding bills the *appointing faction's*
  Legitimacy, not just the podestà's own standing. Extends SE-7's oversight toolkit.
- **Prior NERS verdict:** REFINE *(overturned: dossier's MERGE → critic's REFINE; steelman survived)*.
  The dossier misread its own cited source — the comparative-governance doc calls appointer-liability
  "genuinely new" and files IT-1/HAB-1 as *sibling* SE-7 extensions, not machinery SE-7 replaces. Only
  one clause is a real duplicate: the "Fair Magistrate" transferable Reputation credit vs. the existing
  §1.6 Reputation tag.
- **Re-eval vs built work:** RECONCILE — the "Fair Magistrate" clause. The Goldenfurt slice's already-
  built recall loop uses **Reputation:Just to lower recall Ob** as a live mechanism (part of the G606
  escape-hatch design). This is the *exact* built analog of IT-1's proposed "Fair Magistrate" credit —
  the built code has already implemented essentially the same idea under the Reputation tag that
  TAG_KINDS defines, confirming (with executable evidence, not just prose cross-reference) that the
  pessimist audit's duplicate-coverage call is correct.
- **Changes verdict? No** on REFINE, but the built code turns the prior audit's abstract "fold into §1.6
  Reputation" instruction into a concrete implementation move — it isn't a hypothetical merge target,
  it's an already-wired field with already-wired recall-Ob semantics.
- **Consolidated recommendation:** Refine. Strip the "Fair Magistrate" clause entirely and let a podestà
  who resolves cases justly simply accrue the built Reputation:Just tag through the same recall-Ob
  discount Goldenfurt already implements — no new field, no new text needed for that piece. Keep the
  appointer-liability channel (billing the appointing faction's Legitimacy) as IT-1's genuine
  contribution, but flag that Legitimacy is currently INERT in `sim/` (§1 BUILT-WORK FACTS) — the
  liability bill has nowhere live to land until Legitimacy is wired, which should be surfaced as a
  build-order dependency, not silently assumed to work.

### IT-2 — Condotta (three-phase mercenary contract: Ferma → Aspetto → Lapsed)
- **Original mechanic:** A Ferma→Aspetto→Lapsed mercenary state-machine on top of FA-2's cost fix —
  poaching during Aspetto, a post-lapse non-aggression cooldown.
- **Prior NERS verdict:** REFINE (confirmed). Two grounds survive independently: (i) the "recalled Mil
  pool ×0.5" figure is unreconciled against every flat-scalar `faction.Mil` read site, including
  `massbattle.py::_faction_to_unit` (mass-battle unit power) — a site the dossier had missed; (ii) IT-2
  is named head of a shared `Debt(garrison_pay)` family (with VEN-SE-1/Settle-Arrears/Index-Wages) and
  builds no Debt hook, meaning it would land first as unshared parallel infrastructure.
- **Re-eval vs built work:** STILL-VALID with a direct RECONCILE target confirmed. Two built-work facts
  land squarely on IT-2's two open grounds: first, `march_layer` is confirmed to be ARMY logistics, not
  governor economy — this is consistent with (not contradicting) the pessimist audit's finding that the
  fluctuating Mil pool must reconcile against mass-battle code (`massbattle.py::_faction_to_unit`) rather
  than governance code, since Mil-pool state genuinely lives on the army/logistics side. Second,
  `ledger.py`'s built `TAG_KINDS` already includes **Debt** as a live, non-hypothetical tag kind — the
  "shared `Debt(garrison_pay)` clock" the audit calls for is not new infrastructure to invent; it is a
  usage of an already-built tag.
- **Changes verdict? No** on REFINE, but the built Debt tag removes any ambiguity about whether the
  shared wage-liability clock requires new ledger machinery — it doesn't.
- **Consolidated recommendation:** Refine. (1) Reconcile the recalled-Mil-pool multiplier against all
  four read sites confirmed to exist, explicitly including `massbattle.py::_faction_to_unit`; (2) defer
  all wage/pension bookkeeping to the built `Debt` tag rather than authoring a bespoke tag, consuming the
  shared clock instead of building parallel infrastructure (this also directly resolves VEN-SE-1's CUT
  rationale — see cross-reference below).

### IT-5 — Legation Split (delegated multi-settlement authority cap)
- **Original mechanic:** A Weight-threshold-forces-split cap on delegated multi-settlement authority —
  the anti-over-mighty-subject brake paired with BYZ-6's pooled-AP consolidation accelerator (S-1
  synthesis: author both as one governance §1.9).
- **Prior NERS verdict:** REFINE *(overturned: dossier's MERGE → critic's REFINE; steelman survived)*.
  The dossier's three claimed "collisions" all evaporated on source read (wrong row, pattern reuse, a
  contradicted single-authoring-source demand). One real gap: IT-5 imports BYZ-6's pooled-AP benefit
  without restating BYZ-6's companion revolt-risk cost.
- **Re-eval vs built work:** RECONCILE-first — the primitive IT-5 brakes doesn't exist yet in code. The
  built-work facts are explicit: governance in `sim/` is **per-settlement**, with **no multi-settlement
  AP economy** (the AP formula `2+facility_tier` is scoped to one Settlement record; `march_layer` is
  army logistics, not a governor pooling mechanism; `npc_ids` is an unbounded per-settlement list with no
  cross-settlement actor cap). BYZ-6's pooled-AP "accelerator" — the mechanic IT-5 is supposed to brake —
  has no built substrate at all. IT-5 does not collide with anything built, but it also currently
  regulates a resource that does not exist outside design prose.
- **Changes verdict? Yes, partially** — not on the REFINE verdict itself (still correct on its own
  terms), but on sequencing. The built-work review makes concrete what was abstract in the S-1 synthesis
  note ("co-author with BYZ-6"): IT-5 cannot be authored as a standalone, buildable spec before BYZ-6's
  pooled multi-settlement AP primitive exists in `sim/territory/`, because IT-5's entire trigger
  (a Weight threshold on a *pooled* authority) has no field to read.
  Treat this as a firm build-order gate.
- **Consolidated recommendation:** Reconcile-first (build-order gate, not a design gate). Keep IT-5 and
  BYZ-6 as one governance §1.9 per the original synthesis, but explicitly sequence BYZ-6's pooled-AP
  registry extension (a new multi-settlement aggregate field, since none exists in the built Settlement
  schema) *before* authoring IT-5's split trigger against it. Also land the audit's outstanding fix: an
  explicit cross-reference restating BYZ-6's revolt-risk cost wherever IT-5 is invoked.

### IT-6 — Fiscal Tribunal (self-binding institution)
- **Original mechanic:** A settlement institution that self-binds: Levy-via-Tribunal writes a Precedent
  raising the governor's own future Levy Ob, and Local Actors gain an AI-triggered "Petition the
  Tribunal" action that can reverse a prior player action.
- **Prior NERS verdict:** NOT ADJUDICATED. `IT-6`/`ED-SE-0034` is one of three queued items (with
  CHN-7/ED-SE-0035, VEN-SE-3/ED-SE-0043) that hit transient structured-output failures across three
  workflow passes; per the design lead's explicit call, the pessimist audit was filed on the 41-item
  result and IT-6 carries forward to a follow-up rather than being force-adjudicated. Its STEP-3 status
  remains `needs_jordan`.
- **Re-eval vs built work:** STILL-VALID as a design proposal, but cannot be given a re-eval verdict
  category (STILL-VALID/REDUNDANT/COLLIDES/RECONCILE/SUPERSEDED) in the strict sense, since it has no
  prior NERS ruling to re-evaluate against. What the built substrate *does* offer: registry.py's
  `open_needs` field and `ledger.py`'s built **Precedent** tag kind are both plausible, already-live
  hooks for IT-6's mechanics — a self-binding Precedent write is directly expressible against the built
  Precedent tag, and an outstanding, un-actioned Petition maps naturally onto `open_needs`. Neither
  collides with anything built.
- **Changes verdict? N/A — no prior verdict exists to change.** This finding instead surfaces a gap: IT-6
  must complete its NERS adjudication before any consolidated recommendation can be finalized.
- **Consolidated recommendation:** Reconcile-first, in the narrow sense of "get it adjudicated." Route
  IT-6 through a follow-up NERS pass (per the pessimist audit's own coverage caveat) before treating it
  as promote-ready; when that pass runs, hand it this section's finding that `Precedent` (built tag) and
  `open_needs` (built field) are viable implementation anchors, so the adjudication isn't starting from
  a blank prose reading.

### IT-7 — Seggio Council (hereditary noble corporate faction)
- **Original mechanic:** A new subnational-faction archetype: hereditary bodies each holding a bespoke,
  non-transferable privilege sitting *outside* the Charter/Quo-Warranto system (only inherited, married,
  or seized), sharing a collective Eletti bloc-Treat.
- **Prior NERS verdict:** REFINE (confirmed). N and Omega-d survive robustly — administratively-
  irrevocable corporate-noble privilege is a real point on the revocability spectrum that neither
  Charter (§3.3a) nor Za (§3.3b) covers. Three Q gaps: the water/market-dispute adjudication clause
  strips a case class from Hold Court with no replacement resolver; the Guild-row interaction is
  ambiguous (is Seggio the standing claimant, a rival, or unrelated to Develop's Guild-charter option);
  recognition cost is asserted by omission.
- **Re-eval vs built work:** RECONCILE — with a genuine built hook. Registry.py's Settlement schema
  carries a **`subnational` dict** field — this is precisely the kind of structure a hereditary,
  non-transferable, outside-the-Charter-system body needs to live in, and its existence is independent
  confirmation that "subnational corporate politics" is a category the built substrate already
  anticipates, not a novel data shape IT-7 would have to invent from scratch. This doesn't resolve any
  of the three Q gaps (Hold Court replacement resolver, Guild-row ambiguity, recognition cost), but it
  does mean IT-7's eventual implementation has a concrete field to target rather than requiring new
  schema.
- **Changes verdict? No.** REFINE stands; the built `subnational` field is a positive implementation
  signal, not a defect finding, so it doesn't change the verdict category — it de-risks the authoring
  follow-up.
- **Consolidated recommendation:** Refine. Author settlement_layer_v30.md §3.3c per the audit's
  follow-up (recognition cost/trigger, transfer resolver citation, Local-Actor-budget exception vs.
  §4.5's 2-cap, explicit Hold-Court/Guild-row interaction), and additionally cite `subnational` (registry.py)
  as the concrete storage target for Seggio bodies in that same follow-up pass.

### IT-8 — Capital-Gated Mastership (Upstart Path)
- **Original mechanic:** An alternate §2.5 Free-Master gate: buy the rank (skip the caste-biased
  Masterpiece Examination) in exchange for a durable Upstart tag (Disposition −2, no Apprentices for 4
  seasons, easier to expel) — a skill-vs-capital fork that doubles as a capital-for-caste-mobility
  bypass.
- **Prior NERS verdict:** REFINE (confirmed). N clean, non-duplicative of sibling BYZ-3. The defect is a
  verified dead-text cost clause: of three costs meant to make the bought rank a real trade-off, only
  two attach to real machinery (Disposition −2, 4-season Apprentice lock); the third
  ("Guild Schism/expulsion check resolves at −1 Ob for the accuser") cites a settlement-Stability event
  card and a Demotion Trigger table that have no accuser/defendant role anywhere outside the Church-only
  Excommunication Tribunal.
- **Re-eval vs built work:** STILL-VALID, no collision. Caste/guild-rank mechanics of this kind sit
  entirely outside the registry.py Settlement schema (prosperity/defense/order, legitimacy/
  popular_support, facility_tier/AP, suspicion, pressure, subnational, npc_ids, ledger, open_needs,
  deck_state) — none of those fields model guild-internal rank or caste bias, so the built substrate
  neither confirms nor contradicts IT-8's mechanics; it simply hasn't reached that layer yet.
- **Changes verdict? No.** This is a pure design-text defect (a dead-text clause citing nonexistent
  machinery), independent of anything the sim/territory build does or doesn't implement.
- **Consolidated recommendation:** Refine, exactly per the audit's follow-up: strike the accuser-Ob
  sub-clause and replace it with a hook into the real Demotion-Magnitude/appeal machinery (e.g., "the
  Upstart's institutional-violation Demotion Magnitude is one severity tier worse"), mirroring how
  sibling BYZ-3 correctly reuses existing Demotion-Trigger language. Specify the flat Wealth buy-in
  magnitude. No built-work dependency blocks this refinement.

---

## Cross-cutting notes for this set

- **The Compact-vs-Leverage collision (HAB-5) is the single loudest finding in this batch** and should
  be surfaced prominently per CLAUDE.md §2's ED-1094 rule — HAB-5 was independently certified as one of
  only two "clean, no-steelman-needed" KEEP items in the entire 12-item authored set, which makes it the
  highest-risk candidate for a silent ratification that ships a schema mismatch. It must not merge as
  "5th Ledger tag" text without reconciling against the built `Leverage` kind first.
- **IT-2's and IT-5's REFINE follow-ups both now have concrete, code-verified targets** (the built `Debt`
  tag for IT-2's wage clock; the confirmed absence of any multi-settlement AP primitive for IT-5), which
  should replace the more abstract "reconcile against X" language in the original audit text with direct
  citations to `ledger.py`/registry.py once those follow-ups are authored.
- **IT-1's "Fair Magistrate" merge target is no longer hypothetical** — Goldenfurt's live
  Reputation:Just → lower-recall-Ob mechanism is the same idea already executing in built code, which
  should make that refinement close quickly.
- **IT-6 remains a genuine gap in NERS coverage**, not a re-eval finding — it needs a real adjudication
  pass before this section's STILL-VALID label can be upgraded to a definitive verdict category.
