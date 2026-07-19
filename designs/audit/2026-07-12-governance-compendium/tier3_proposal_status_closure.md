# Tier 3 — Proposal-Status Closure Register

> **Status: PROVISIONAL / consolidation artifact.** This register triages every one of the 58
> comparative-governance proposals produced by the 2026-07-09 research pass, folding in (1) the
> pessimist–subtractive NERS audit verdicts (2026-07-11, 41 of 44 adjudicated), (2) the settlement-season
> stress-test synthesis (2026-07-12, the re-evaluation of the 12 built PR#119 items against play), and
> (3) the two open needs-a-Jordan-ruling dockets (rise-to-power §5, proactive-scale-menus §6). Nothing
> here is ratified canon; the individual proposals carry their own `promote-ready` / `needs_jordan` /
> `authored-PROPOSED` / `cut` status. This is the map, not the territory.
>
> **Naming note.** This register uses canonical Valoria terms throughout — "Discipline" (never the
> deprecated *Cohesion*) and the canonical faith-figure "Solmund" (no deprecated alias). Where a source
> mechanic touches faction morale it is rendered as Discipline.

---

## 3.0 Provenance and the empty `reeval/` directory

Four source artifacts feed this register:

| Source | Path | What it supplies here |
|---|---|---|
| **Research docket** | `designs/audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md` | The 44-kept / 14-cut cut-and-keep pass, the curated 44-item table, the S-1..S-6 synthesis groupings, the 5-item sequencing plan, and the 23-item `needs_jordan` consolidated queue. |
| **NERS audit** | `designs/audit/2026-07-11-comparative-governance-pessimist-ners-audit/pessimist_ners_audit_v1.md` | The KEEP→REFINE→DISTILL→MERGE→PRUNE→CUT verdict for **41 of the 44** kept proposals (3 hit structured-output failures and are un-adjudicated — see §3.10). |
| **Stress-test synthesis** | `designs/audit/2026-07-12-settlement-season-stress-sim/stress_test_synthesis_v1.md` | The re-evaluation of the **12 built PR#119 items** against 7-seed × 5-season adversarial play (the "re-eval-vs-built-work" column), plus the vindicated-rejected list (§3.7). |
| **Open Jordan dockets** | `rise_to_power_roster_system_research_v1.md` §5 and `41_proactive_scale_menus.md` §6 | The collected design-taste rulings owed (§3.9). |

**On the `reeval/` directory (`designs/architecture/governance_compendium_v1/reeval/`): it is empty.** No
standalone per-proposal re-evaluation files were authored. The task brief named those files as the source
of the "re-eval-vs-built-work verdict"; that re-evaluation was in fact delivered as the single 2026-07-12
stress-test synthesis document, whose §1 mechanic-stress verdict table and §4 vindicated-rejected table are
the operative re-eval surface. This register therefore reads the re-eval column **out of the stress-test
synthesis**, and flags any proposal outside PR#119 scope as "not stress-tested (not in PR#119)" rather than
inventing a verdict.

---

## 3.1 The four status cohorts

The 58 proposals resolve into a clean partition:

| Cohort | Count | Definition |
|---|---|---|
| **Authored into canon (PR#119)** | 12 | Written as PROPOSED text this session; live in the open PR; NERS verdicts directly actionable before merge. |
| **Promote-ready, unlanded** | 9 | Judged buildable without a Jordan ruling, but not yet authored (queued behind the P1 tier). |
| **Needs-Jordan** | 23 | A design-taste / scope / cross-lane / irreversibility fork that only Jordan can resolve; shipped as `needs_jordan`. |
| **Cut** | 14 | Rejected by the 2026-07-09 judgment pass (duplicate-in-kind, slot-competitor for the single Administrative void, or off-brief). |
| **Total** | **58** | 44 kept + 14 cut. |

The 44 kept were all allocated fresh lane-tagged EDs at filing time: **`ED-FA-0018..0034`** and
**`ED-SE-0018..0044`**. The 14 cut carry no ED.

---

## 3.2 Master status table — all 58 proposals

Columns: **NERS** = the 2026-07-11 subtractive verdict (KEEP / REFINE / DISTILL / MERGE / PRUNE / CUT, or
`—` for the 3 un-adjudicated and the 14 cut which the NERS pass did not re-judge). **Re-eval** = the
2026-07-12 stress-test verdict where the item is in PR#119 scope, else its stress relevance. **Disposition**
= the consolidated call this register lands on.

### 3.2a Authored into canon — PR#119 (12)

| Code | ED | Civ | Title | Original mechanic (one line) | NERS | Re-eval (stress) | Consolidated disposition |
|---|---|---|---|---|---|---|---|
| **HAB-5** | ED-SE-0019 | Habsburg | Encabezamiento (Negotiated Quota) | Fixed-term Compact (5th Ledger tag) locking an extraction figure below live capacity + reciprocal one-Petition-per-term right. | **KEEP** | §1.3a **BREAK on failure-mode** (the *lock substrate* it shares with SE-JP2 is a fuse: no subsistence floor, ~8-season cooldown, no reversal verb). | **Ratify the verb; fix the substrate.** The Compact bargain itself is clean (KEEP); the shared locked-figure read-path needs a subsistence-floor clamp + reversal verb (stress HIGH gap). Land the clamp in-PR. |
| **HAB-7** | ED-SE-0023 | Habsburg | Ordenanza Ratification | Ratify/Reject/Amend guild-authored rules via Hold Court; ratifying an entry clause can lock caste exclusion into policy. | **KEEP** | §1.3c ⇩ **HOLD (was BREAK)** — the "unreachable Gu-Std3 gate" alarm was a digest artifact; the ladder rung exists (§2.5). | **Ratify.** Clean in play and in audit. One-line drafting gap only: cite the Precedent tag on Ratify's persistence (as Reject cites Grudge). Author the sub-threshold-presentment fallback resolver as a minor edge (stress MEDIUM). |
| **SE-JP2** | ED-SE-0018 | Japan | Kokudaka Survey | Periodic assessment locks `assessed_base`; assessed/actual gap = bankable surplus or neglect-detonates-revolt hazard. | **REFINE** | §1.3a **BREAK on failure-mode** (shared with HAB-5); Survey is the *unilateral* stale-high strip vector. | **Refine-then-ratify.** Pull Survey out of the blanket "both promote-ready" at line 83; author Emergency Resurvey / out-of-cooldown clause; wire `assessed_base` into §4.3a Dearth; state Assessment-vs-Compact precedence; add Assessment to §1.6 Ledger families. |
| **SE-JP3** | ED-SE-0021 | Japan | Za patron lapse | Charter privileges lapse *automatically* when the patron's standing falls — new attack vector (target the patron, not the guild). | **REFINE** *(overturned MERGE→REFINE)* | §3.3b **HOLD (cleanest marquee item)** — end-to-end faithful in S5; w_d-shield-then-unshield is a genuine emergent feature. | **Refine-then-ratify.** Keep the subsection. Two one-paragraph fixes: inherit Quo-Warranto `floor(charter_age_seasons/8)` friction for prescription-hardened charters; cite ED-FA-0021 as prior art for the patron-bound-lapse shape. |
| **CHN-3** | ED-SE-0022 | China | Clerk Capacity | Second, opaque AP source ("Retain Clerks") with an Investigate-only hidden Clerk-Corruption counter. | **REFINE** | §1.1a **STRAIN** — net-zero-AP trap at CC0/CC1; CC 1→2→3 scaling, Corruption→Intrigue increment, defection-severance all undefined. | **Refine-then-ratify.** Define CC acquisition/decay (e.g. +1 per Retain-Clerks, cap 3, escalating Wealth cost), a FacilityTier ceiling coupling, Dismiss/Retain transition, an always-visible partial tell. Harvest VEN-FA-2's accounting semantics *without* its AP source. Fold the VEN-FA-2 CUT in as corpus-internal AP-pillar evidence. |
| **FA-JP2** | ED-FA-0019 | Japan | Recognition Fork (Confirm/New-Grant) | Every Recognition Event becomes a legible Confirm-vs-New-Grant stonewall-or-reward choice, all four ladders. | **REFINE** | §1.0b **STRAIN** — resolves, but no NPC/institutional granter decision-rule (engine chose by fiat); orphaned New-Grant fate when the patron vacates mid-arc undefined. | **Refine-then-ratify.** Define "ease by one step" against §1.0a's magnitude table; add a stacking/precedence clause across §1.0a/b/c/d (docket-level, §3.9); fix or drop the §1.4 Defiance citation; supply an NPC-granter decision-rule + orphaned-New-Grant fate. |
| **FA-JP4** | ED-FA-0020 | Japan | Court Attendance + hostage-kin | Recurring court-presence cost + hostage-kin lever easing Demotion thresholds while making the hostage a legible target. | **REFINE** *(steelman survived)* | §1.0c **HOLD (lightly loaded)** — fired once (S7), correctly inert below the Std-4 threshold; under-tested, not proven. | **Refine-then-ratify.** Rewrite the "eases by one step" trigger in §1.0a's vocabulary; give the Treasury cost a bare Wealth figure; cross-reference `faction_layer_v30.md` §3.2 treaty "Hostages" to defuse the name collision; fold the Mughal heir-scope extension as a first-class use. |
| **IT-8** | ED-FA-0022 | Italy | Capital-Gated Mastership | Buy the Gu-Std1→2 Free-Master rank vs the caste-biased Masterpiece Examination; durable Upstart tag (Disp −2, no Apprentices 4 seasons, easier to expel). | **REFINE** | §2.5a **STRAIN → HOLD** — Upstart tag fired correctly in S1. | **Refine-then-ratify.** Strike the dead accuser-Ob sub-clause (references a settlement-Stability card with no accuser role); replace with a hook into §1.0a's real Demotion-Magnitude machinery ("institutional-violation Demotion Magnitude one tier worse"). Specify the flat Wealth buy-in. |
| **IT-7** | ED-SE-0024 | Italy | The Seggio Council | Hereditary corporate bodies holding bespoke *non-transferable* privileges outside the Charter/Quo-Warranto system; shared Eletti bloc-Treat. | **REFINE** | §3.3c **BREAK** — S3 terminal lock: the only override is "seized by force" and the governance layer has **no governance-scale force/seizure resolver**; the central heresy investigation is unadjudicable for a full arc. | **Refine-then-ratify + author-new.** Author a recognition cost/trigger; supply a transfer resolver for marriage/inheritance/force paths; state the §4.5 Local-Actor-budget exception; name Hold-Court and Guild-row interactions. **CRITICAL:** author a bounded non-force override or a governance-scale seizure/emergence resolver (this is the stress test's #1 finding — pair with reinstating IT-3, §3.7). |
| **BYZ-3** | ED-FA-0023 | Byzantine | Guarantor-gated Guild entry | Joint-liability sponsorship at Gu-Std 0: 3–5 guarantors stake Disposition; "Vouched-For" tag; burned-twice lockout. | **REFINE** | §2.5a **STRAIN → HOLD** — shared-liability + Precedent fired correctly in S1. | **Refine-then-ratify.** Replace three unquantified magnitudes (Disposition hit, "double weight", raised future-sponsorship Ob) with concrete values; reconcile which guarantor (if any) is the +1D training mentor; narrow the shared §2.5a intro caste-note to IT-8 only. |
| **SE-JP1** | ED-SE-0020 | Japan | Goningumi cells (Bind the Cells) | New Keep-Order method binding Local Actors into fixed 5-household collective-liability cells; compounding Cell-Revolt failure. | **MERGE** | §1.3b **MERGE CONFIRMED, hard** — §1.3b's 5-household cells vs §4.5's 1–2 Local-Actor cap is a real substrate collision; non-constructible on frontier/small settlements. Where it *does* run, Collective-Liability reliably inverts Order into a revolt accelerant (Pattern D, ~6/7 seeds). | **Refine-then-ratify (MERGE the standalone).** Retire §1.3b as a standalone institution — the "Bind the Cells" verb row, the Collective-Liability Grudge-variant tag, the Cell-Revolt Crisis trigger, the Unbind verb. Fold at most into Force's "rebound risk" clause. **Do not** smuggle the tag-stacking/Crisis machinery into Force's flavor text under a new name (critic's scoping caveat). Reconcile the §4.5 actor-cap in-PR. |
| **CHN-9** | ED-FA-0021 | China | Kaochengfa Performance Audit | Optional patron-imposed triplicate-ledger toggle speeding demotion *and* promotion; auto-lapses when the patron falls. | **MERGE** | §1.0d **MERGE CONFIRMED in direction, under-executed** — S7: the audit never demoted Gerta; it armed, advanced to Waiting Order, then auto-lapsed when the patron fell (S4); Gerta fell anyway via the *separate* Recall route. "Audit protection" is illusory; "Missed Obligation" trigger undefined; the two accountability paths must unify. | **Refine-then-ratify (MERGE the standalone).** Retire §1.0d as a standalone toggle. Fold its one load-bearing delta — the season-count escalation (Waiting Order@1, patron review@2, auto Demotion-Magnitude-1@3) — into §1.0a's default-magnitude bullet. **Drop the promotion-acceleration clause entirely** (asserted, never a rule). Reconcile the audit-vs-Recall double-path onto one signal; define "Missed Obligation" (stress finding #7; consider VEN-SE-7's independent-archive fragment, §3.7). |

**PR#119 headline (NERS §1b + stress bottom line):** of the 12 built items, only **2 are clean unconditional
KEEP** (HAB-5, HAB-7); the other **10 need revision before the PR ratifies them** — 8 REFINE + **2 MERGE
(SE-JP1, CHN-9) that require deleting landed subsections**. Per CLAUDE.md §2 (ED-1094), merge *is*
ratification, so every one of these fixes must land **inside PR#119**, not as an unforced follow-up. The
stress test's independent bottom line: the **resolution substrate earned ratification** (the 5 primitives
produced a coherent unauthored downfall arc across 7 seeds), and both NERS MERGE flags (§1.0d, §1.3b) were
**confirmed by play** — but do **not** ratify §1.3a's failure-mode, §3.3c (Seggio), or Mandate-at-scale as-is.

### 3.2b Promote-ready, unlanded (9)

Judged buildable without a Jordan ruling but queued behind the P1 tier. **None are in PR#119**, so none were
stress-tested directly; their re-eval column reads "not stress-tested (not in PR#119)" except where the
stress test's structural findings implicate the surface they would touch.

| Code | ED | Civ | Title | Original mechanic (one line) | NERS | Re-eval (stress) | Consolidated disposition |
|---|---|---|---|---|---|---|---|
| **HRE-4** | ED-FA-0029 | HRE | Borrow (financier loan) | Loan secured against a *named* extractive right; spawns an Investigate-discoverable financier-actor; reuses Quo Warranto for the hard clawback (Concession tag). | **KEEP** *(overturned MERGE[stub]→KEEP)* | Not stress-tested. Named by the catalogue as one of **two surviving canonical pledge shapes** that Levy:Farm / Underwrite / Capital-Partnership / Foreign-Loan should collapse *into*. | **Promote (author next).** Clean KEEP. Optional REFINE: fold "Hated among merchants" into the single-axis Reputation track rather than a scoped variant. Reference shape for BYZ-7's re-home (§3.2c). |
| **HRE-2** | ED-FA-0024 | HRE | Chapter Capture | Pre-vacancy patronage banking "College seats owed" that convert to vote-weight only if/when a vacancy fires (timing the player doesn't control). | **KEEP** *(overturned DISTILL[stub]→KEEP)* | Not stress-tested. | **Promote.** Distinct from BYZ-9's external override (proactive seeding vs reactive please-the-seated). REFINE-grade authoring notes: seats-owed→vote-weight conversion, decay conditions, §1.0b interaction. |
| **HAB-1** | ED-SE-0030 | Habsburg | Corregidor (overlay) | Outside appointee *layered over* the sitting governor (override on Hold Court/Investigate, governor keeps the rest); self-expiring term-scoped tags. | **KEEP** *(overturned MERGE[stub]→KEEP)* | Not stress-tested. The first mechanic to actually mechanize §1.4's suspicion-threshold "audit" stub. | **Promote.** Distinct from IT-1 (concurrent layer-over vs replacement) and SE-7's Visita/Residencia/Rotation. Author as part of the S-2 five-instrument oversight toolkit. |
| **CHN-6** | ED-SE-0025 | China | Gongsuo Registration | Symmetric visibility/exposure toggle: unregistered = invisible/untaxable/unadjudicable; registered = adjudicable/Levy-eligible but opens a "Squeeze" Friction card. | **MERGE** | Not stress-tested. | **Re-home before promoting.** MERGE confirmed: fold the registration status into §1.3c Ordenanza as a *gating precondition* for whether a Petition can surface; resolve "guild wealth" through the §1.3a `assessed_base` substrate; retire the duplicate "Squeeze" card in favor of the §1.1a Clerk-Corruption trigger. Silently contradicts already-PROPOSED same-day §1.3c as written. |
| **HRE-3** | ED-SE-0026 | HRE | Convene the Circle | New AP verb pooling obligations across peer settlements; "Circle Quota" tag callable by any member — the first *lateral* governor-to-governor trust axis. | **REFINE** | Not stress-tested (but the corpus has zero horizontal governor-to-governor mechanics — genuinely new). | **Refine-then-promote.** Shrink "Circle Quota" to a Debt-family variant ("multilateral Debt, callable by any co-signer") per the §1.3b Collective-Liability precedent; add a Directive-size-vs-capacity gate; give the call-in an explicit "fires on X" trigger. Author the pooling primitive carefully — Malta/Great-Hurricane/ABCD catalogue chains all reuse it. |
| **VEN-SE-2** | ED-SE-0028 | Venice | Boschi Pubblici Requisition | New Directive type tying a province to a *named production dependency* (supply chain, e.g. timber→Arsenal); Defy starves the dependent building. | **REFINE** | Not stress-tested. | **Refine-then-promote.** Ground or drop the auto-success-bonus reference (VEN-SE-1 has no such bonus — inert cost M-6); specify the Bargain-failure state; reconcile with an active Compact tag; **state explicitly whether Requisition is a species of Extract (inheriting §1.3a Compact auto-resolution) or immune to it** (live Omega-d loophole around a landed P1 mechanic). |
| **IT-1** | ED-SE-0029 | Italy | Podestà (contracted outsider) | Outsider governor immune to internal faction rolls, with **appointer-liability**: end-of-term Sindacato malfeasance bills the *appointing faction's* Legitimacy. | **REFINE** *(overturned MERGE→REFINE)* | Not stress-tested. | **Refine-then-promote.** Keep the appointer-liability mechanic (the MERGE would have discarded it — a misread of its own cited source). Strip only the "Fair Magistrate" transferable-Reputation clause and fold into §1.6 Reputation; optionally reword the Disposition band as an explicit prerequisite exclusion. Author as part of S-2 with HAB-1. |
| **HAB-4** | ED-FA-0025 | Habsburg | Overlapping Consulta Arbitration | Inter-ministry conflict arbitration with two procedure types (Agenda-Set blind-framing vs Ratify accept/veto) + Latency-to-paralysis; denominated in the existing Competence stat. | **REFINE** | Not stress-tested. | **Refine-then-promote.** Define "Ministry priority action" and its action-economy source (Part 7 builds no per-Ministry action capability today — the arbitration presupposes an unbuilt foundation); specify Latency-1/2 effects; generalize into a domain-agnostic arbitration primitive that §7.1a instantiates. Drop the wrong `auto_manual_resolution_duality` reuse instruction (grep-verified: no such vocabulary there). |
| **IT-2** | ED-FA-0026 | Italy | Condotta three-phase contract | Ferma→Aspetto→Lapsed mercenary state-machine (poaching, reserve, post-lapse non-aggression) on top of FA-2's cost fix. | **REFINE** | Not stress-tested (off both focus areas — P3). | **Refine-then-promote.** Reconcile the fluctuating "recalled Mil pool ×0.5" against **all four** flat-scalar `faction.Mil` read sites (`_mil_advantage_signal`, CONQUEST_MIN_MIL gate, muster formula, **and `massbattle.py::_faction_to_unit`** — the mass-battle unit-power site the dossier missed); defer wage bookkeeping to the shared `Debt(garrison_pay)` clock. Drop the unsupported Non-Aggression consolidation claim. |

### 3.2c Needs-Jordan (23)

Each carries a specific fork only Jordan can resolve. The **NERS** column judges the mechanic-as-specified;
the **Re-eval** column notes stress relevance (none are in PR#119); the **Disposition** notes the ruling
required. The full question set is collected in §3.9. Three items (IT-6, CHN-7, VEN-SE-3) are un-adjudicated
by NERS — see §3.10.

| Code | ED | Civ | Title | Original mechanic (one line) | NERS | Re-eval / stress relevance | Consolidated disposition (ruling owed) |
|---|---|---|---|---|---|---|---|
| **CHN-2** | ED-FA-0018 | China | Imperial Examination Ladder | Non-Skyrim-Eight credentialing pipeline; capped pass rates; direct Std-3 appointment skipping the sponsorship grind; a "Waiting Laureate Pool" resource. | **REFINE** | The **winner of the Administrative-void contest** (§3.8); the single highest-value open rank decision. | **Ruling first (§3.8).** *Does the flat Crown Administrative branch get a differentiated sub-structure at all?* If yes: author §2.8 with an autonomous unmanaged-pool consequence (defection/discontent/rival-or-Niflhel recruitment) + the capped-passer resolution primitive. Drop the IT-8-style stigma-parity fix (imports the wrong pattern — examined legitimacy carried *more* prestige, not less). |
| **BYZ-1** | ED-FA-0027 | Byzantine | Office/Dignity two-track split | Forks single Standing into a revocable Office track + a sticky Dignity track (disgraced-but-titled; jumped-up-administrator states); re-scopes §1.0a. | **DISTILL** | Partial-vindicated for the *labeling* problem only (S1 title-vs-number mismatch); **supplies no missing rung** (the §0.2 correction shows there was none). | **Ruling + DISTILL.** *Should Standing decouple into authority + prestige?* Decide alongside HAB-2 (how many parallel status/power tracks?). If yes: retire the standalone §1.0b two-track section; preserve only the decoupled-prestige kernel by extending §1.0a's lay-status floor to **Total-magnitude triggers only** (keep Default/Severe at full ED-776 weight), reusing the Upstart single-tag pattern. |
| **HAB-2** | ED-FA-0034 | Habsburg | The Valido (Favorite track) | Informal Favorite power-track (Royal Intimacy + Patronage Web) that outperforms formal Standing; collapses *binarily* against §1.0a's graduated rule. | **CUT** | Not stress-tested. Keep-cut in the vindicated pass (fix lives elsewhere). | **CUT as pitched; a narrower version could earn a place.** Omega-d dominance stands: gated at Std-4 + Royal Intimacy 3 via uncapped Audience scenes — a "cheaper path to greater power" free win rivaling Std-7 decree power, its only cost a tail-risk binary collapse. A far narrower version (one new §1.0a Total-magnitude collapse trigger + a Disposition-threshold flavor note, **no chair-gate bypass, no new resource**) is a different proposal. |
| **BYZ-6** | ED-SE-0031 | Byzantine | Consolidated Command (Doux) | Pooled-AP multi-settlement governor with concentrated revolt risk (Π = max of members, crises hit the whole bloc). | **REFINE** *(overturned DISTILL→REFINE)* | Territory-scale governor AP economy is a stress HIGH gap (S6 — the "AP triage" premise rests on an unspecified rule). The KEPT vehicle the stress test wants *wired*. | **Ruling + refine.** *Are multi-settlement governors in scope?* Keep the vehicle (§6.1 is a player-eligibility gate, not an institutional risk/resource merger — the DISTILL rested on a false duplicate). Before promotion supply: a pooled-AP cap value/formula, explicit §1.1a Clerk-Capacity interaction under a merged pool, Directive/Event-Deck cadence for a consolidated bloc. Author with IT-5 as one governance §1.9 (S-1). |
| **IT-5** | ED-SE-0032 | Italy | Legation Split | Weight-threshold forces a split of delegated multi-settlement authority — the anti-over-mighty-subject *brake* to BYZ-6's *accelerator*. | **REFINE** *(overturned MERGE→REFINE)* | Same territory-scale surface as BYZ-6. | **Ruling + refine.** Keep IT-5 standalone (the three "collisions" evaporate on source read). Add a cross-reference to BYZ-6's revolt-risk cost when co-authored; add a composition note reconciling IT-5's and SE-9(b)'s independent `governor_emergence` triggers. Author with BYZ-6 (S-1). |
| **HRE-5** | ED-SE-0033 | HRE | Guild Uprising (Compact/Suppress) | One crisis trigger, two opposite durable outcomes: Concord installs a permanent guild *veto* on the governor's own Develop authority; Suppression zeroes Guild Influence with a never-decaying Grudge floor. | **REFINE** | Not stress-tested (Concord is the wired downstream consequence of HAB-7's "Guild Influence" — cross-scale link confirmed). | **Ruling + refine.** *May a governance outcome install a permanent guild veto on the player's own authority?* Rename Concord's tag (collides with the existing Compact = ED-SE-0019, incompatible schema); differentiate Concord from §1.3c Ratify (lean into seat+veto); specify or drop the undecaying Grudge floor; add a third Amend-style path or justify the binary. |
| **BYZ-9** | ED-FA-0028 | Byzantine | Cardinal Ratification Override | Cross-faction lever letting Crown/Parliament override the Church College's Cardinal election at a legitimacy cost. | **REFINE** | Not stress-tested. | **Ruling + refine.** *May an external faction breach Church electoral sovereignty?* (Class of the corpus's other blocked Church-roster items.) Strike the sees/Cathedral eligibility clause (imports Catholic diocesan structure that doesn't exist at Cardinal rank — the Four Cardinals are arm-heads at Himmelenger); replace with a **Crown-alone** Override hung on the Father Gustav Linder Crown-liaison channel (mirrors Justinianic symphonia, resolves both the parsing failure and the sovereignty asymmetry). |
| **IT-6** | ED-SE-0034 | Italy | Fiscal Tribunal | Self-binding institution: Levy-via-Tribunal writes a Precedent raising the governor's own future Levy Ob; Local Actors gain an AI-triggered "Petition the Tribunal" that can reverse a prior player action. | **— (un-adjudicated §3.10)** | Not stress-tested. | **Ruling + NERS follow-up owed.** *May an NPC-initiated ruling reverse a prior player governance action without consent?* NERS could not adjudicate (structured-output failure); carry forward to the follow-up audit before promoting. |
| **BYZ-7** | ED-FA-0029* | Byzantine | Pronoia Grant | Revenue-claim-*without*-governance state (collect a settlement's tax without governing it, sitting governor untouched) tied to a service quota. | **MERGE** | Not stress-tested. | **Ruling + MERGE.** *Is a revenue-without-governance state in scope, bridging FA rank and SE settlement?* Retire the standalone Precedent-tag machinery (mechanism-identical to §3.3a's live `floor(charter_age_seasons/8)` + Quo Warranto — Reskinned attractor). Author **one new grantee-type row** ("FA rank-holder, individual") in the existing §3.3 split-authority table, reusing §3.3a's prescription formula verbatim and citing HRE-4's canonical pledge shape. Net: one table row, zero new tags, zero new resolvers. *(*ED collision with HRE-4 in source — verify allocation.)* |
| **BYZ-8** | ED-FA-0030 | Byzantine | Oath-Bound Administrator | Renounce dynastic claim → delegated high office at reduced Coup Counter sensitivity; breakable at Total-magnitude cost. | **MERGE** | Not stress-tested. | **Ruling + MERGE (corrected target).** *How literally vs abstractly to model the renunciation archetype?* Author the oath-of-renunciation as a second collateral-type within the catalogue's own succession-oath unification (Extract Succession Oath, Fratricide Law → one parameterized `succession_rule`), **not** new Part 3 + Part 7 + Coup-Counter scaffolding. The "barred office" half cannot be built until Part 7 authors the exclusion axis it presupposes (that half is closer to CUT). Coup Counter is itself in unresolved numeric incoherence (ED-931, open). |
| **CHN-7** | ED-SE-0035 | China | Chancellery Gatekeeper | A named NPC between the Provincial Authority and the governor who can silently substitute a *harsher* Directive than issued. | **— (un-adjudicated §3.10)** | Not stress-tested. | **Ruling + NERS follow-up owed.** *May the no-GM engine silently, undetectably substitute a harsher Directive (deception of the player)?* NERS structured-output failure; carry forward. Dependency for CHN-8. |
| **CHN-8** | ED-FA-0031 | China | Institutional Purge (Bloc) | A bloc-scale §1.0a trigger demoting a whole credentialed ideological cohort at once (guilt-by-association), off a chokepoint NPC's hostility. | **PRUNE** *(overturned harsher DISTILL→PRUNE)* | Not stress-tested. | **Ruling + PRUNE (the single hardened verdict).** *Should a whole cohort be demotable at once?* As specified it is a **costless, contest-free, wielder-unaccountable, undetectable mass-purge switch** — fires unilaterally off a third party's Disposition, no defense roll, no backlash, inherits total invisibility from CHN-7. Pull it and its four verbatim-reuse dependents (A4 Household Roster, A9 kul-escheat, D3 Reign-Bound Cohort Purge, Cohort Capture) from promote-ready until it specifies a non-dominance cost/backlash to the wielding chokepoint, a telegraph, and a leader-tier appeal threshold. |
| **FA-JP3** | ED-FA-0032 | Japan | Varfell three-axis vassal tiering | Kinship / Grant-size / Council-eligibility as independent axes producing NPC threat-archetypes (rich-peripheral-barred vs poor-central-empowered). | **DISTILL** | Not stress-tested. | **Ruling + DISTILL.** *Should Varfell get a distinct vassal-classification differentiating its identity?* Fixed-at-investiture wealth-independent hard exclusion is precisely the gate-type deliberately *withheld* from Varfell (marked "Favored" to contrast Crown/Church's ascriptive gating) — reintroduced without supersession (T-fail). Grant-size duplicates Standing-tied scope; zero downstream wiring. Retire standalone §1.3d; fold any surviving council-exclusion kernel into §1.3c's Inner-Circle-Notes / a §3.2 Varfell-row boolean; drop Grant-size. |
| **FA-JP5** | ED-FA-0033 | Japan | Metsuke/Ometsuke surveillance split | Two target-segregated, non-poolable surveillance tracks (own-officers vs vassal-lords); a faction funding one is structurally blind to the other. | **DISTILL** | Not stress-tested. | **Ruling + DISTILL.** *Split faction surveillance into two blind tracks?* Fold the own-officer half into the §1.4 Suspicion track and the aggregate half into the §7.1 Schattendienst Competence/Corruption funding tradeoff; residual target-segregation as an Ob-modifier note, not a new resource axis — and only with an explicit logged supersession of **ED-SE-0005** if it touches Investigate (FA-JP5 adds bonus-dice plumbing to the exact verb ED-SE-0005 deliberately narrowed). Depends on FA-JP3 (open). |
| **SE-JP4** | ED-SE-0036 | Japan | Status Freeze | Caste-mobility lock trading Order for hard-blocked advancement. | **CUT** | Not stress-tested. | **Ruling + CUT (tone).** *A caste-mobility lock inside a caste system the corpus authors as critique?* CUT stands on two independent load-bearing axes: (i) Omega-d dominant — the freeze's benefit is static, monotonic, zero-upkeep while active (invoke once, leave on forever); (ii) T-fail — its text blocks "any Caste × Rank Advancement crossing" with no carve-out, silently nullifying the Warden-of-the-Thread / Riskbreaker / Niflhel escape valves Part 3 *explicitly* authored as resistance infrastructure for the Southern Einhir. Do not author the §1.3a Freeze subsection or the 13th caste-matrix exception column. |
| **CHN-4** | ED-SE-0037 | China | Salt Certificate | Tradeable, geography-siloed monopoly tokens as a Develop funding option + a "Convert to Hereditary Franchise" one-way door. | **REFINE** *(overturned MERGE[stub]→REFINE)* | Not stress-tested. Catalogue rates it "bolstered" — *the general form* Toll/Mining-Charter might fold into. | **Ruling + refine (bundle w/ CHN-5).** Not a duplicate of Guild-charter or Toll/Mining-Charter. One real gap: unlike its ED-SE-00xx siblings it enumerates **no autonomous Friction/Crisis churn hook** (Omega-c). Specify the churn/follow-on hook (e.g. a merchant-family Ambition/Petition once Certificate-Wealth or Disposition crosses a threshold). Do not merge away. |
| **CHN-5** | ED-SE-0038 | China | Kaizhongfa Colonize Directive | The batch's **only calendar-driven decay clock** (every existing Debt/Precedent tag fires on a trigger, not a schedule) — real new timing pressure. | **REFINE** *(overturned MERGE→REFINE)* | Not stress-tested. | **Ruling + refine (bundle w/ CHN-4).** Keep the mechanism — §1.3a locks a *static* figure; CHN-5's rate *itself* moves autonomously on a campaign calendar, pays the *governor*, value-flow inverted; folding it in would destroy the P3/Omega-c "world moves whether or not you act" property. Before promotion: specify Bargain/Defy interaction with the decay clock, pause/tick timing during a scene, rule out Certificate-hoarding dominance. Flag possible Class-A reclassification (campaign-wide decaying variable + terminal speculative state). |
| **HRE-6** | ED-SE-0039 | HRE | Reichsacht (outlawry) | An "Outlawed" status flag with a contagion clause (harboring exposes the harborer) but *enforcement-dependent* teeth (a settlement with standing can Defy and shelter). | **KEEP** | Not stress-tested. | **Ruling + promote.** *Should a Crown decree be visibly, legibly defiable and fail?* Clean KEEP. Two authoring notes: give "Outlawed" an actor-scoped home distinct from the per-settlement §1.6 Ledger; generalize the §1.3b Collective-Liability contagion primitive rather than parallel-inventing one (the single authoring point for a 4-item family: Magdeburg / Spanish-Fury / Drogheda all need the same contagion clause). |
| **HRE-7** | ED-SE-0040 | HRE | Mediatize | New Immediate/Mediatized settlement-status axis (separate from ownership), issuable only in a negotiated settlement — political status as treaty compensation currency. | **REFINE** *(overturned MERGE→REFINE)* | Not stress-tested. | **Ruling + refine.** *May a settlement's direct-answer status be administratively demoted without conquest and traded as treaty currency?* The duplicate-coverage claim fails against all three named targets. Real gaps: the sole delivery mechanism (a negotiated peace-treaty/succession payload) **does not exist in canon** (Succession Contest is deterministic-strength-based, no negotiation step); §3.3a-Charter composition on the same settlement unspecified. Define/attach to an actual negotiation-payload mechanism before authoring. |
| **HAB-6** | ED-SE-0041 | Habsburg | Crush the Estates | Irreversible SE-layer rewrite of a ratified faction's rank-ladder gate (Hafenmark's Alderman 2/3-supermajority → direct crown appointment, forever). | **KEEP** *(overturned PRUNE→KEEP)* | Not stress-tested. | **Ruling + promote.** *May an SE-layer action irreversibly rewrite a ratified faction's rank-ladder gate?* Clean KEEP: FA-JP2 (§1.0b) operates strictly *post-threshold* (modulates reward for a candidate who already cleared the vote) and cannot absorb the vote-elimination consequence. Grudge-threshold-gated behind an already-damaged state, costs convertible Military+Legitimacy, imposes a permanent Broken-Estates hostile-trajectory tax (permanence-of-cost matching permanence-of-benefit). One gap: add a one-line cross-reference distinguishing it from §1.0b. |
| **VEN-SE-1** | ED-SE-0042 | Venice | State Arsenal | A fourth Develop funding method with a persistent per-settlement Wage/Pension Debt liability (fires every season regardless of use) + a single-NPC-zeroes-output failure. | **CUT** | Not stress-tested. Referenced by VEN-SE-2's inert auto-success-bonus (which VEN-SE-1 does not actually grant). | **Ruling + CUT.** NERS CUT (see §1a disposition). The persistent-Debt + single-NPC-zeroes-output shape is worth harvesting into the shared `Debt(garrison_pay)` family rather than shipping standalone. Correct VEN-SE-2's phantom reference to a bonus VEN-SE-1 never provided. |
| **VEN-SE-3** | ED-SE-0043 | Venice | Bonifiche Capital Posture | A fifth Ledger tag family where a military *loss* triggers an economic choice, and the tag changes what *type* of extraction (liquid vs land) a Directive may ask for. | **— (un-adjudicated §3.10)** | Not stress-tested. | **Ruling + NERS follow-up owed.** *Are Ledger tag families extensible beyond the four?* — **already answered affirmatively in practice** (Compact/ED-SE-0019 is now a live fifth family; §3.353 of the research). VEN-SE-3's own proposed sixth family remains a separate `needs_jordan` call. NERS structured-output failure; carry forward. |
| **VEN-SE-5** | ED-SE-0044 | Venice | Scuole Grandi | A caste-excluded Civic Prestige resource that subtracts from Π *only* while excluded-caste Grudges drive it — a targeted, ceilinged pressure valve (palliative, never curative). | **DISTILL** | The stress test's **highest-value single tuning lever**: "Wire the already-KEPT VEN-SE-5 Scuole Grandi ceilinged Π-valve" to de-fang the R-4 death spiral (Pattern B, ~6/7 seeds). | **Ruling + DISTILL, but wire the kernel.** *May a caste-excluded resource modify the Π homeostat (a balance-sensitive surface)?* Retire the bespoke "Civic Prestige" resource + `−⌊CivicPrestige/3⌋` Π term + implied caste-provenance field (Class-A misclassification; self-declared scale-isolated dial). Re-home the capped, non-convertible, caste-targeted relief kernel as a Sponsor sub-option writing a Debt/Reputation Ledger tag and draining Π through the formula's **existing** generic "−Σ(player releases)" term. The stress test independently wants this valve wired — the DISTILL delivers it more cheaply. |

### 3.2d Cut (14)

The 2026-07-09 judgment pass cut these. The NERS pass did not re-judge cuts (its brief was the 44 kept), so
NERS reads `—`. The stress test **re-examined the cuts against play**; four were flagged for reinstatement
(§3.7), the rest keep-cut. Salvageable fragments per the research's own §5 closing note are recorded.

| Code | Civ | Title | Original mechanic (one line) | Cut rationale (2026-07-09) | Re-eval (stress) | Consolidated disposition |
|---|---|---|---|---|---|---|
| **IT-3** | Italy | The Sforza Gambit | Mercenary-captain converts an existing condotta into sovereignty when his employer state destabilizes. | Off both focus areas (faction-*emergence*, not intra-faction advancement/settlement mgmt); triply contingent (IT-2 + FA-7 + emergence pipeline). | **YES (S5) + partial ×2** — the strongest reinstatement candidate; play reproduced its exact end-state with no resolver to cover it. | **RECONSIDER — reinstate down-scoped (§3.7).** A *bounded* force-seizure/emergence resolver is the missing piece behind both the §3.3c Seggio terminal lock and the rival-capture dead-end. Down-scope from the "unbuilt emergence pipeline" it was cut against. |
| **VEN-SE-4** | Venice | Dedizione | Negotiated submission treaty: preserve local privilege for legitimacy at an extraction cap. | Redundant with prior SE-5 (Entry Terms Confirm-vs-Impose); same trigger, same tradeoff. | **partial ×4** — the most *recurring* partial across seeds. | **RECONSIDER (§3.7).** A mid-tenure negotiated cap binding on a *superior* authority is a shape the corpus lacks (its stated duplicate SE-5 fires only at annexation). Pair with the §1.3a subsistence-floor work. Its distinctive Two-Tier Law fragment folds into SE-5. |
| **VEN-SE-7** | Venice | Sindici Inquisitori | Roving-NPC audit with a frequency-floor catching artificially-suppressed Π, independent of Suspicion. | Redundant with prior SE-7 Visita (surprise inspection revealing true vs reported state). | **partial ×2** — its roving-frequency floor is exactly what Bind-the-Cells' deliberate Π suppression evades. | **RECONSIDER for the absentee/suppressed-Π case (§3.7).** Its independent archive is what the §1.0d audit-vs-Recall double-path reconciliation needs (CHN-9 follow-up). Not a general add — fold the frequency-floor into SE-7. |
| **BYZ-4** | Byzantine | Eparch price/wage regulation | Price/wage-ceiling regulation + foreign-merchant channeling → smuggling-Intrigue weight. | Stat-toggle grab-bag; price/wage half overlaps HAB-7's guild price-regulation. | **partial (S4), no (S6)** — famine seeds have no lever to curb hoarder profiteering. | **RECONSIDER the price-control half only (§3.7).** The rest was a correctly-cut grab-bag. The foreign-merchant channeling dial (smuggling → Intrigue weight) remains a minor Develop/trade addition per the research's §5 closing note. |
| **BYZ-2** | Byzantine | Purchased Dignity | Buy an honorific dignity for a lump sum → permanent yearly income + prestige rank; title-inflation homeostat. | Doubly contingent on BYZ-1; a *third* parallel "shortcut past earned Standing" lever before the corpus has decided how many it wants. | Keep-cut. | **Keep-cut.** Its return is gated on the BYZ-1 + HAB-2 "how many parallel status/power tracks?" ruling (§3.9). Elegant homeostat, not worth a new fiscal subsystem this pass. |
| **BYZ-5** | Byzantine | Narrow-mandate sekreta + coordinator | Multiple narrow-mandate ministries with no shared staff; a coordinator unlock at a −1D + Coup Counter cost. | Redundant-in-kind with HAB-4 (thinner treatment of the same inter-ministry-coordination space). | Keep-cut. | **Keep-cut.** HAB-4 does it richer, promote-ready, on the existing Competence stat. |
| **CHN-1** | China | Rank-Rung × Portfolio-Lane | Second "decouple Standing into two axes" fork (rank-rung authority + portfolio-lane category). | Redundant-in-kind with BYZ-1; adding both gives every rank three numbers. | Keep-cut. | **Keep-cut.** BYZ-1's authority/prestige split does it better and binds to §1.0a. |
| **FA-JP1** | Japan | Shugo-Jito dual office | Provincial-command tier + settlement-steward tier in one office, with intra-officer conflict. | Overlaps BYZ-6/IT-5 (command layer) *and* SE-4/SE-JP3 (charter/patron); a fourth Administrative-void competitor. | Keep-cut. | **Keep-cut.** Both its tiers are covered; the intra-officer conflict doesn't carry it. |
| **HRE-1** | HRE | Chancery Tri-Office | A Skyrim-Eight ladder branched three ways for Administrative advancement. | The least-distinctive Administrative-void competitor; CHN-2 is the differentiated shape. | Keep-cut. | **Keep-cut (slot-competitor).** Resolved by the §3.8 Administrative-branch ruling. |
| **VEN-FA-1** | Venice | Rectorship Pipeline | Rotation + mandatory end-of-term Relazione career spine for Administrative advancement. | Administrative-void competitor whose spine duplicates prior SE-7 (rotation + Residencia). | Keep-cut. | **Keep-cut (slot-competitor).** Covered by SE-7 + the S-2 oversight toolkit. |
| **VEN-FA-2** | Venice | Ducal Chancellery | An Administrative Capacity (AP-buffer) + ladder-fill role for the cittadini secretarial order. | Duplicates CHN-3's clerk-AP source, *undercuts the AP-scarcity pillar P1*, ladder-fill covered by CHN-2. | **Keep-cut on pillar grounds, harvest the spec** — its accounting semantics are exactly the CC-scaling/cost definition §1.1a (CHN-3) needs. | **Keep-cut; harvest, do not reinstate the buffer.** Correctly cut to preserve the AP-scarcity pillar. Fold its AP-accounting semantics into CHN-3's refine (§3.2a) *without* re-adding the AP source. The NERS pass explicitly cites this CUT as corpus-internal evidence the AP-pillar risk is real. |
| **VEN-SE-6** | Venice | Colonist Grant | Permanent Defense from founder-loyal colonists (militia without garrison); non-transferable Colonist Loyalty across succession. | Redundant with prior SE-9(a) Plant Colony. | Keep-cut. | **Keep-cut.** Its refinement (explicit non-transferability across governor succession) folds into SE-9. |
| **IT-4** | Italy | Cipher-Chief | A persistent Cipher Advantage resource *seized* rather than reset by a rival's coup; a chief-secretary intelligence edge across successions. | Administrative-void competitor; its one novel element doesn't require a whole competing ladder; CHN-2 wins the slot. | Keep-cut. | **Keep-cut (slot-competitor).** The seized-not-reset Cipher Advantage fragment could fold into an intelligence-continuity note; resolved by the §3.8 ruling. |
| **HAB-3** | Habsburg | Reichskolleg | Exam-based credential gate for Administrative advancement (colegios-mayores pipeline). | Redundant-in-kind with CHN-2; CHN-2 is the richer self-contained version. | Keep-cut. | **Keep-cut (slot-competitor).** Resolved by the §3.8 Administrative-branch ruling. |

---

## 3.7 (a) Vindicated rejected proposals — the stress-test reinstatement flags

The settlement-season stress test (2026-07-12 §4) traced each depth-3 gap against the 14 cuts. Of the 14, **one
produced a clean `resolves=yes`** and a cluster produced recurring `partial`s. Four are flagged for
reinstatement. The **honesty caveat that recurred**: in several places the real fix is a **KEPT** item, not a
cut — do not reinstate a cut where a kept item already owns the fix.

### IT-3 — The Sforza Gambit · **strongest reinstatement candidate**
- **Gap it fills:** a rival converts an economic foothold into sovereignty (S5), and the force-seizure path for a
  hardened Seggio privilege (S3, S6). Play **reproduced IT-3's exact end-state with no resolver to cover it.**
- **Why it was cut:** off both focus areas (faction-*emergence*, not intra-faction advancement or settlement
  management) and triply contingent (IT-2 + FA-7 + the unbuilt emergence pipeline).
- **Reinstatement shape:** a **bounded** governance-scale force-seizure / emergence resolver — the missing piece
  behind *both* the §3.3c Seggio (IT-7) terminal lock and the rival-capture dead-end. Down-scope it from the
  "unbuilt emergence pipeline" it was cut against to a bounded, single-purpose resolver. **This is the stress
  test's #1 prioritized finding for Jordan** ("author-new + reinstate IT-3 down-scoped"), directly coupled to
  the IT-7 CRITICAL disposition in §3.2a.

### VEN-SE-4 — Dedizione · most recurring partial (×4)
- **Gap it fills:** a mid-tenure negotiated extraction-cap-for-loyalty binding — recurs across S2 (Compact-vs-
  Directive precedence), S4 (crisis floor), S5 (re-patroning), S6 (subsistence).
- **Why it was cut:** judged redundant with prior SE-5 (Entry Terms Confirm-vs-Impose).
- **Reinstatement shape:** a mid-tenure negotiated cap binding on a *superior* authority is a shape the corpus
  genuinely lacks — its stated duplicate **SE-5 fires only at annexation**, not mid-tenure. Pair with the §1.3a
  subsistence-floor / reversal-verb work (stress HIGH gap #3). The distinctive Two-Tier Law fragment still folds
  into SE-5.

### VEN-SE-7 — Sindici Inquisitori · partial (×2), scoped reinstatement
- **Gap it fills:** a roving Π-suppression audit floor for the Suspicion→Recall case (S2); and the independent
  archive that unifies the §1.0d audit-vs-Recall double-path (S7).
- **Why it was cut:** redundant with prior SE-7 Visita.
- **Reinstatement shape:** **for the absentee / suppressed-Π case specifically, not a general add.** Its
  roving-frequency floor is exactly what Bind-the-Cells' (SE-JP1) *deliberate* Π suppression evades; its
  independent archive is what the CHN-9 (§1.0d) reconciliation needs. Fold the frequency-floor into SE-7 rather
  than shipping standalone.

### BYZ-4 — Eparch price/wage regulation · price-control half only
- **Gap it fills:** anti-gouging price control during famine (S4) — famine seeds have **no lever** to curb hoarder
  profiteering.
- **Why it was cut:** a stat-toggle grab-bag whose price/wage half overlaps HAB-7.
- **Reinstatement shape:** **the price-control half only.** The rest was a correctly-cut grab-bag. Couple with the
  §1.3a famine/coercive-extraction work (stress finding #13: "reconsider VEN-SE-4 / BYZ-4 price-control for the
  famine case"). The foreign-merchant channeling dial (smuggling → Intrigue weight) remains a minor Develop/trade
  addition.

**Two further cuts partially vindicated but NOT reinstated:**
- **VEN-FA-2 (Ducal Chancellery)** — keep-cut on pillar grounds; *harvest its AP-accounting spec* into CHN-3's
  refine without re-adding the AP buffer (it undercuts pillar P1). See §3.2d.
- **BYZ-1 (Office/Dignity split)** — reconsider *narrowly* for the S1 title-vs-standing-number labeling problem
  (its cut rationale looked weaker under play), **but it supplies no missing rung** — the §0.2 stress correction
  proved there was none to supply. BYZ-1 remains a `needs_jordan` DISTILL (§3.2c), not a reinstatement.

**All other cuts keep-cut** (BYZ-2, CHN-1, VEN-FA-1, FA-JP1, BYZ-5, HAB-2, IT-4, VEN-SE-6, VEN-SE-1, HRE-1):
each names an adjacent shape but the fix lives elsewhere (a kept item, a Church escalate verb, the §5 scoring
or severance rules, or off-target).

---

## 3.8 (b) The Crown Administrative branch flat-rank problem — the docket's #1 needs-Jordan

**The single truly empty rank surface in the corpus is the Crown's Administrative specialty branch (§1.1b).**
The 2026-07-09 judgment pass corrected a stale premise (the "missing Guild ladder" — §2.5 is in fact authored
through Gu-Std 6) and isolated the genuinely flat surface: among the three Crown Standing-3 specialty branches,
the Administrative branch **alone** states it opens no sub-office ladder.

The §1.1b table as it stands (`faction_politics_v30.md`):

| Branch | Ministry link | Sub-office opens | Primary mentor line | Secondary |
|---|---|---|---|---|
| **Martial** (Schwertzweig) | Kriegsamt (Ministry of War) | Löwenritter Knight ladder (Part 2 §2.1) | Royal Marshal → Löwenritter Grand Master | Knight-Commander of the player's garrison |
| **Administrative** (Stangzweig) | Haushalt (Finance) *or* Gerichtsamt (Justice) *or* Markamt (Lands) | **None; advancement within Crown ranks only** | Lord Treasurer → Lord Chief Justice | Chancellor of the Markamt |
| **Intelligence** (Schattenzweig) | Schattendienst (Intelligence) | Riskbreaker ladder (Part 2 §2.2); Niflhel transactional relationships (Part 2 §2.6) | Spymaster → Riskbreaker Commander | Senior Tribune of the Schattendienst |

**The problem in one line:** the Martial and Intelligence branches each open a rich named sub-office ladder
(Löwenritter Knights; Riskbreakers + Niflhel), while the Administrative branch's "Sub-office opens" cell reads
**"None; advancement within Crown ranks only."** An Administrative-branch player has no differentiated
progression minigame — only the generic Crown ladder every branch shares. (Note also: per §1.1b's caste-gating
line, the Administrative branch carries **the strongest caste bias** of the three — see Part 3 — so any
sub-structure authored here interacts with the caste system by construction.)

**Why it is the docket's #1:** *seven* proposals compete to fill this one empty slot — **CHN-2, HRE-1,
VEN-FA-1, VEN-FA-2, IT-4, HAB-3, FA-JP1.** One slot cannot be filled seven ways. The judgment pass kept the
single most differentiated shape (**CHN-2, the Imperial Examination Ladder** — a non-Skyrim-Eight credentialing
pipeline with capped pass rates, direct Standing-3 appointment skipping the sponsorship grind, and a "Waiting
Laureate Pool" resource) and **cut the other six as slot-competitors** (HRE-1, VEN-FA-1, VEN-FA-2, IT-4, HAB-3,
and FA-JP1's Administrative-void half). CHN-2 ships as `needs_jordan` because **filling the slot at all is a
Jordan taste call:** §1.1b's flat branch reads as a *stated contrast* against Martial/Intelligence — the
flatness may be deliberate design, not an oversight.

**The ruling owed (needs_jordan queue item 1):** *Does the deliberately-flat Crown Administrative branch get a
differentiated, non-Skyrim-Eight sub-structure at all?* The research's own recommendation is **yes**, with CHN-2
the winning shape. If yes, the NERS refine (§3.2c) applies: author §2.8 with (i) an autonomous consequence for
an unmanaged "Waiting Laureate Pool" (frustrated examinees → defection / discontent / rival-or-Niflhel
recruitment — the single most load-bearing piece of the historical dynamic), and (ii) the capped-passer
resolution primitive bound to a real sim/params resolution. **Drop** the IT-8-style stigma-parity fix: examined
legitimacy carried *more* prestige historically, so forcing parity with the capital-bought Upstart stigma
imports the wrong pattern.

This is item 5 of the sequencing plan's decision memo: **resolve CHN-2 first**, then BYZ-1 (the Standing
decouple), then the S-1 multi-settlement layer, then the rest.

---

## 3.9 (c) Collected "needs a Jordan ruling" handoff items

Three dockets carry open design-taste rulings. Consolidated here so nothing is left un-triaged. **None is a
research question — all are taste / scope / architecture calls.**

### 3.9a The comparative-governance needs_jordan queue (23 items — research §5)

The full ordered queue, verbatim in intent (the disposition detail per item is in §3.2c):

1. **CHN-2 Examination Ladder** — does the flat Crown Administrative branch (§1.1b) get differentiated
   sub-structure at all? *(Highest-value rank fork; recommended yes. See §3.8.)*
2. **BYZ-1 Office/Dignity split** — should Standing decouple into revocable authority + sticky prestige?
3. **HAB-2 Valido track** — an informal Favorite track that outperforms formal Standing, collapsing binarily?
   *(Decide with BYZ-1: how many parallel status/power tracks does the game want? Also governs whether the cut
   BYZ-2 pay-for-prestige economy ever returns.)*
4. **BYZ-6 + IT-5 Consolidated Command** — are multi-settlement governors (pooled AP, concentrated revolt risk,
   Weight-capped forced split) in scope for the governance layer?
5. **CHN-7 Chancellery Gatekeeper** — may the no-GM engine silently, undetectably substitute a harsher Directive
   than the PA issued (deception of the player)?
6. **CHN-8 Institutional Purge (Bloc)** — should a whole credentialed ideological cohort be demotable at once by
   a chokepoint NPC (guilt-by-association)? *(Depends on CHN-2 + CHN-7. NERS hardened this to PRUNE — §3.2c.)*
7. **HRE-5 Guild Uprising (Concord)** — may a governance outcome install a *permanent* guild veto on the
   governor's own Develop authority?
8. **IT-6 Fiscal Tribunal** — may an NPC-initiated ruling reverse a prior player governance action without
   consent? *(Also NERS-un-adjudicated — §3.10.)*
9. **HAB-6 Crush the Estates** — may an SE-layer action *irreversibly* rewrite a ratified faction's rank-ladder
   gate?
10. **HRE-6 Reichsacht** — should a Crown decree be visibly, legibly defiable and fail (contagion clause +
    enforcement-dependent teeth)?
11. **HRE-7 Mediatize** — may a settlement's direct-answer status be administratively demoted without conquest
    and traded as treaty compensation currency?
12. **BYZ-7 Pronoia** — is a revenue-claim-without-governance state in scope, bridging FA rank and SE settlement?
13. **BYZ-8 Oath-Bound Administrator** — the renunciation-of-dynastic-claim archetype; how literally vs
    abstractly to model the eunuch-derived grounding?
14. **BYZ-9 Cardinal Ratification Override** — may an external faction override the Church College's Cardinal
    election, breaching Church electoral sovereignty? *(Class of the corpus's other blocked Church-roster items.)*
15. **FA-JP3 Varfell three-axis vassal tiering** — should Varfell get a distinct vassal-classification
    differentiating its identity from the single-Standing-scalar model?
16. **FA-JP5 Metsuke/Ometsuke** — split faction surveillance into two target-segregated, non-poolable tracks?
17. **SE-JP4 Status Freeze** — a caste-mobility lock buying Order by hard-blocking advancement; tone call inside
    a caste system the corpus authors as critique. *(NERS CUT on Omega-d + T-fail — §3.2c.)*
18. **CHN-4 + CHN-5 Frontier Certificate Economy** — a tradeable geography-siloed monopoly-token economy with a
    hereditary-franchise one-way door (CHN-4) and the batch's first calendar-driven decay clock (CHN-5).
19. **VEN-SE-1 State Arsenal** — a persistent per-settlement Wage/Pension Debt liability + a single-NPC-zeroes-
    output failure mode. *(NERS CUT — §3.2c.)*
20. **VEN-SE-3 Bonifiche Capital Posture** — a fifth Ledger tag family where a military *loss* triggers an
    economic choice changing what *type* of extraction a Directive may ask for. *(Gate-question "are Ledger tag
    families extensible beyond four?" already answered YES in practice by Compact/ED-SE-0019; VEN-SE-3's own
    sixth family remains a separate call. NERS-un-adjudicated — §3.10.)*
21. **VEN-SE-5 Scuole Grandi** — a caste-excluded Civic Prestige resource modifying the Π homeostat (a
    balance-sensitive surface) as a targeted, ceilinged valve. *(NERS DISTILL, but the stress test's
    highest-value tuning lever — wire the kernel. §3.2c.)*

**Two cut items with salvageable fragments** worth a line in the same memo: **BYZ-4**'s foreign-merchant
channeling dial (smuggling → Intrigue weight) as a minor Develop/trade addition; and **VEN-SE-4 / VEN-SE-6 /
VEN-SE-7**, whose distinctive fragments (permanent violate-and-punish Two-Tier Law; non-transferability across
succession; audit frequency-floor catching Π-suppression) fold into prior SE-5 / SE-9 / SE-7 respectively.

### 3.9b Rise-to-power roster §5 — the individual-scale rulings owed

From `rise_to_power_roster_system_research_v1.md` §5 — the *individual*-side design (patronage, merit, marriage,
court favor, bureaucratic capture, retinues, purges, venality, ideological authority) layered on the settlement
ambition engine + the player Standing ladder.

**The one pure design-taste ruling:**
- **Can an NPC actually DEPOSE or SUPERSEDE the player at a rank the player holds?** §3.2 recommends shared rank
  space, which architecturally permits this — the sharpest "every action pays what it buys" stakes question in
  the design. If no, NPC advancement is partly a sandbox the player watches; if yes, the player's own
  consolidation writes the same legible vulnerability every NPC's does (purest Ω-d non-dominance). Architecture
  supports both via a single **`player_seats_are_contestable`** toggle. Research inclination: **yes, but gated
  behind the *coalition* threshold (E8/G6)** so the player is only deposable when over-consolidated past the
  point ordinary challenges bind — making the fall earned and legible, never a coin-flip.

**Genuine architectural gaps (new mechanics, flag before building):**
1. **Lineage/clan-scope objects above the NPC lifespan** (C5 Wang Mang `dynastic_leverage` across five reigns;
   I10 family `Entrenchment`) — need an entity the Accounting-cascade ticks *above* a single NPC. "The single
   biggest structural ask of this batch." Recommend the `scale_binding=lineage` profile (not registry-gated).
   Whether Valoria wants clan-scale actors at all is a scope call.
2. **The joint / Coalition ambition structure** (G6/G9 multi-NPC joint ambition; E8 `purge_cascade`
   supermajority coalition) — "the clearest new-mechanic requirement"; ambitions are strictly per-NPC today.
   Load-bearing for the entire downfall side.
3. **Peninsula-scale aggregation** (`renown`, J6) — `state.doctrinal_ruling` must sum `scene.witness` /
   `scene.gossip` across settlements an NPC never administers. The exact gap named in the system context.
4. **Mandate separable-from-possession** (F7, `custodian_id` ≠ `holder_id`) — "the sharpest genuine
   architectural gap of the ten."
5. **In-transit Key interception** (H2, `access.correspondence_filtered`) — no mechanism today for one NPC
   intercepting *other* NPCs' Keys before they resolve; every chokepoint entry needs it. *(Note: CHN-7
   Chancellery Gatekeeper, §3.9a item 5, is the governance-scale instance of this same primitive.)*
6. **Dormant/conditional tags** (G4, `trigger_condition: succession`) and **hidden-visibility tags** (H7) —
   new tag-family capabilities.
7. **A co_leadership / partial-Leadership state** (C8) and **mutable office `succession_rule`** (F2) — Part 2's
   succession model treats Leadership as binary and offices as static slots today. *(The `succession_rule`
   unification is the same one BYZ-8's MERGE target names — §3.2c.)*

**Thin spots / fact-check caveats** (advisory, do not over-trust): B6 Napoleon/Légion d'Honneur
"carrière ouverte aux talents" quote not re-verified verbatim; B7 Northcote–Trevelyan quote/timeline via
general search not primary; B8 Prussian Referendar exam dates secondary; A1 Cicero *patronus* leans on tertiary
framing; F9 Mongol keshig has **no clean historical reversal within the paradigm period** (its downfall
dynamic is inferred, the least empirically anchored); C10/I6 Venice + J-series closed-oligarchy gates
**speculative pending a Venice-style faction actually being authored** — do not build the `marriage_registered`
registry object until that faction exists.

**Infrastructure dependency, not a research gap:** no entry supplies a settlement-registry substitute — the
registry gating the *settlement-scale* ambition engine remains unbuilt. Court and lineage bindings can ship
without it; the settlement binding is blocked.

### 3.9c Proactive scale-menus §6 — the four-scale rulings owed

From `41_proactive_scale_menus.md` §6 (the task's "proactive §5 docket" — the design-taste rulings live in §6
of that file). Four scales: Organization / Settlement / Territory / Faction.

**Design-taste rulings only Jordan can make (each PROPOSED / unresolved):**
1. **Does the Organization scale get a full parallel AP/Standing/Treasury economy, or a lightweight
   scoped-reuse layer** with full-holding capability gated behind an "independent charter" flag (the O14
   distinction)? Research leans toward the lightweight layer as the cheaper honest default.
2. **Is the Territory a first-class persistent entity or a view/grouping over settlements?** X10/X13 argue
   first-class (administrator identity, command-split flag, Chamber network); X6/X9 (redistrict, reach-cap)
   argue it should be *cheaply re-drawable*. Likely reconciliation: a lightweight entity (roster + a few flags)
   whose *membership set is mutable*.
3. **BYZ-6 / IT-5 ratification.** The research now gives both a concrete shape (command-split flag; per-verb
   permissions table; shared Chamber-network prerequisite). Jordan's ruling is a *choice among specified
   options*, not an open design problem — but still a ruling, and per CLAUDE.md §2 (ED-1094) it should flip the
   relevant docs' Status lines + CURRENT.md as part of whatever PR lands it. *(Same item as §3.9a queue #4.)*
4. **The `power_base`↔scale-action gating rule** (§5B) is a proposal, not canon — reads cleanly off the
   `initiator_level` fields but has not been checked against the Ascendancy doc's `power_base` semantics; needs
   canon-guard review before adoption.
5. **Zero numbers, by design.** Per CLAUDE.md §5, none crosses into Godot until authored as prose params with
   PP/ED citations; the reach-cap constant (X9) is the one unavoidable number, left unspecified.

**Thin spots needing authoring before implementation:**
- **The Organization economy is unspecified** — what is "Org AP" / "Guild Capacity" numerically; how does an Org
  Treasury relate to member dues, responsions tithes (O8), assay fees (O4)? **The single biggest authoring gap.**
- **Inter-settlement latency (Relay/Beacon) presumes a game concept that may not exist** — contingent on the
  temporal spine (`engine_clock`, flagged `doc: null` / unwritten in CLAUDE.md §6). The strongest "new state"
  cases on paper, blocked on an unauthored temporal model.
- **The Territory Reserve Pool's internal logic is abstracted** (T2/T10) — fine as intent, underspecified as spec.
- **Tag-family proliferation.** The corpus now proposes Compact, Concession, Outlawed, Capital-Posture, *and* a
  new Muster family — five additions to Precedent/Grudge/Debt/Reputation. Muster and Compact may be collapsible;
  Concession and Capital-Posture overlap in the frontier entries. **A consolidation pass on the tag taxonomy is
  warranted before all five ship.** *(This directly touches the CHN-6, HRE-3, HRE-4, HRE-6, VEN-SE-3 tag
  dispositions above — every new-tag proposal must clear this consolidation.)*

**One structural caution the research surfaces (X4, X5):** several proactive levers are *historically
load-bearing for collapse* (Richelieu's intendants → the Fronde; Meiji's reneged compensation → Satsuma; Qin's
identity-erasure → the dynasty's fall). Stacked Grudges must auto-seed Crisis-family cards rather than sitting
inert. **The proactive menu and the reactive Crisis-card system must ship as one loop, not sequentially** — else
the game gets the centralizing upside with none of the historical downside.

---

## 3.10 The three NERS-un-adjudicated items (open triage residual)

The pessimist-NERS audit fully adjudicated **41 of 44**. Three queued items hit transient structured-output
failures across three workflow passes and were filed on the 41-item result per the design lead's explicit call.
They carry a **NERS verdict of `—`** above and are the only proposals in this register without a subtractive
verdict:

| Code | ED | Title | Status | Follow-up owed |
|---|---|---|---|---|
| **IT-6** | ED-SE-0034 | Fiscal Tribunal | needs_jordan | Re-run the pessimist-NERS dossier → critic → synthesis on this item before promoting. Also carries needs_jordan queue #8 (NPC-reversal-without-consent ruling). |
| **CHN-7** | ED-SE-0035 | Chancellery Gatekeeper | needs_jordan | Re-run NERS. Also carries needs_jordan queue #5 (silent harsher-Directive substitution ruling) and is a dependency for CHN-8's PRUNE remediation. |
| **VEN-SE-3** | ED-SE-0043 | Bonifiche Capital Posture | needs_jordan | Re-run NERS. Also carries needs_jordan queue #20 (sixth-Ledger-family ruling; the "are families extensible?" half is already answered YES by Compact/ED-SE-0019). |

**These three are the only un-triaged remainder in the entire 58-proposal set** — and even they are triaged to
"NERS re-run owed + Jordan ruling owed," not left blank. Nothing else is outstanding.

---

## 3.11 Closure statement

Every one of the 58 comparative-governance proposals now has a home:

- **12 authored (PR#119)** — 2 clean (HAB-5, HAB-7), 8 REFINE-in-PR, 2 MERGE-in-PR (SE-JP1, CHN-9); all fixes
  land inside PR#119 per ED-1094, and the stress test independently ratified the resolution substrate while
  confirming both MERGE flags.
- **9 promote-ready** — 3 clean KEEP (HRE-4, HRE-2, HAB-1), 6 refine-then-promote; queued behind the P1 tier.
- **23 needs-Jordan** — each mapped to a specific ruling in the consolidated queue (§3.9a), led by the Crown
  Administrative branch decision (§3.8); 3 carry an additional NERS-re-run residual (§3.10).
- **14 cut** — 4 flagged for scoped reinstatement by play (IT-3, VEN-SE-4, VEN-SE-7, BYZ-4 — §3.7), 2 harvested
  not reinstated (VEN-FA-2 spec, BYZ-1 labeling), 8 keep-cut with fragments noted.

The three open dockets' design-taste rulings (§3.9) are collected and cross-linked to the proposals they gate.
**Nothing is left un-triaged.**
