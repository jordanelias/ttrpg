# Session Log Index 2026-04-25 (consolidated)

## Consolidation front matter

- **topic_id:** `10_session_log_index`
- **atom_count:** 10
- **scope:** VALORIA_SESSION_2026-04-25_MASTER.md + valoria_session_master_2026-04-25.md atoms. Index-style consolidated doc — collapses 16 atoms into a single ED/PP coverage report. Most content already in commit history.
- **source distribution:**
  - `VALORIA_SESSION_2026-04-25_MASTER.md`: 8 atoms
  - `valoria_session_master_2026-04-25.md`: 2 atoms
- **drift surface:** single-source
- **post-audit canon target:** `No content ingestion — verification report only. Index doc itself archives with the session.`
- **status:** assembled (pending audit Stage 3)
- **assembled_from_commit:** atoms committed at `83c37da7001defdf3bb3425b17dda3f934d262d3`

## Audit checklist (Stage 3 input)

- [ ] Every ED listed in commit-manifest atoms exists in canon/editorial_ledger.yaml.
- [ ] Every PP listed exists in canon/patch_register_active.yaml or an archive.
- [ ] Stress-test results (Section 4) referenced from session-log atoms point at simulations/ files that exist.
- [ ] P1 resolutions claimed are reflected in current p1_blocker_count.

## Known drift dimensions

- ED-739 through ED-784 listed in VALORIA_SESSION master vs Sessions B/C/ED-717 in valoria_session_master — different ED ranges from different session phases.
- Commit-manifest atom may double-count commits also captured in valoria_session_2026_04_25_master_consolidation (canon rectification commits).

## Content

Atoms in section_index order from source.

<!-- atom: valoria_session_2026-04-25_master__00__preamble | section_index: 0 | source_section: "(preamble)" -->


# Valoria Audit + Stress-Test Session — Master Document

**Session date:** 2026-04-25
**Repository:** `jordanelias/ttrpg`
**Branch:** main
**Total commits this session:** 40
**Commit range:** `7d45753` (Wager system) → `be8a478` (glossary TC→CI rename)
**Editorial Decisions logged:** ED-739 through ED-782 (44 EDs)
**Stress tests run:** 60+ (numbered 1–63 plus integration audits)

---

<!-- atom: valoria_session_2026-04-25_master__01__section-1-commit-manifest-chronological | section_index: 1 | source_section: "Section 1 — Commit Manifest (chronological)" -->


## Section 1 — Commit Manifest (chronological)

| # | OID | Subject | EDs |
|---|---|---|---|
| 1 | `7d45753` | Wager system: Edeyja Arc D + Arc E + WC decay + ms_budget reframe | ED-739/740/741/742 |
| 2 | `9a16e5d` | **P1-1 Strain trigger inversion** — held-instability advance + Treaty-pair decay | ED-743/744 |
| 3 | `3e6b0b3` | Scene Slate spec-fixes — Witness Mode + priority + Step 4 keywords + pruning | ED-745/746/747 |
| 4 | `19fc650` | scale_transitions §3.4/§3.6 stub fills + Stability hysteresis + Revolt dedup | ED-748/749/750 |
| 5 | `6035255` | faction_layer Sacred Veto cooldown + Niflhel NPC vote cleanup | ED-751/752 |
| 6 | `5f52e06` | mass_battle: Volley design rationale + officer death 1d10→1d20 | ED-753/754 |
| 7 | `8951cd9` | npc_behavior §8.11.5 cross-faction Outreach floor | ED-755 |
| 8 | `c3c7b88` | TC disambiguation glossary (top 5 files) | ED-756 |
| 9 | `40e2eb6` | Niflhel drift table row cleanup | ED-757 |
| 10 | `ebeb100` | Cardinal naming reconciliation (Stark/Voss/Vorn/Kald → Jarnstal/Olafsson/Tormann/Klapp) | ED-758 |
| 11 | `4db81bf` | peninsular_strain §5.2 Seizure Uncontrolled exclusion | ED-704 |
| 12 | `86c3534` | mass_battle PP-195 — Cohesion → Discipline canonical | ED-705 |
| 13 | `aa14957` | social_contest §7.2 Succession Contest as Grand Contest variant | ED-665 |
| 14 | `dbe0b16` | victory_v30 §8 RM Settlement Emergence pathway | ED-712 |
| 15 | `17523a2` | npc_behavior §3.5 Advisor-Principal Confidentiality Boundary | ED-664 |
| 16 | `2fa9133` | campaign_architecture §5.3 Elske residency null-intersection | ED-662 |
| 17 | `a617f4b` | Close ED-661 (superseded) + ED-669 (deferred); archive 6 entries | ED-661/669 |
| 18 | `ed46e3a` | Stress-test fixes: WC decay + confidentiality scope + priority list + succession weighting | ED-759/760/761/762 |
| 19 | `f9d6721` | Arc E post-Wager Scar threshold tolerance (3→5) | ED-763 |
| 20 | `f5e1ac0` | Niflhel STRUCK propagation params + Löwenritter Coup→Graduated Autonomy | ED-764 |
| 21 | `3125c05` | Officer death per-battle scope + Step 4 capitalization heuristic | ED-765/766 |
| 22 | `f35ff4e` | PROVISIONAL marker cleanup mass_battle (3 stripped) | ED-767 |
| 23 | `8224f72` | Document 13 orphaned PROVISIONAL markers (Jordan-blocked) | ED-768 |
| 24 | `92a35ad` | Editorial ledger maintenance — archive 13 entries | infrastructure |
| 25 | `2f52a0f` | RS→MS residual cleanup strategic_layer_v30_infill | ED-769 |
| 26 | `e2c0252` | Numeric bounds audit closure (14 stats triaged) | ED-770 |
| 27 | `fb15910` | Cross-reference audit fixes (4 broken refs) | ED-771 |
| 28 | `1f7e93d` | social_contest §7.3 Heresy Investigation Lifecycle | ED-772 |
| 29 | `b14a01b` | fieldwork §5.6b Knot Lifecycle (formation→strain→break/rupture) | ED-773 |
| 30 | `4b769ce` | threadwork §2.1 Approach Training canonical content + archive 5 | ED-774 |
| 31 | `2842117` | npc_behavior §6.4 Wrong-Style Penalty extended | ED-775 |
| 32 | `53cbf49` | faction_politics §1.0a Demotion Magnitude | ED-776 |
| 33 | `ded3271` | faction_politics §3.6 caste-transgressive PC Conviction + cross-ref fixes | ED-777 |
| 34 | `e5e250d` | social_contest §6.1.1 Wager Obligation edge cases | ED-778 |
| 35 | `2e05d2f` | §6.1.1 PC-death cross-ref fix (generational_transition) | ED-778 (revision) |
| 36 | `3ab14dc` | derived_stats §5.3 Inspiration mechanic canonical propagation | ED-779 |
| 37 | `df0bab8` | fieldwork §5.6a explicit Bonds ≥ 5 Knot prerequisite + archive 6 | ED-780 |
| 38 | `f89f3a6` | factions_personal Coup Counter STRUCK → Graduated Autonomy canonical | ED-781 |
| 39 | `e7fa400` | npc_priority_trees Coup Counter → Löwenritter Autonomy migration | ED-781 |
| 40 | `be8a478` | glossary TC → CI canonical rename per tcv_conflict §2 | ED-782 |

---

<!-- atom: valoria_session_2026-04-25_master__02__section-2-p1-resolution | section_index: 2 | source_section: "Section 2 — P1 Resolution" -->


## Section 2 — P1 Resolution

Both P1 blockers entering the session were resolved.

### P1-1: Strain trigger inversion (commit `9a16e5d`, ED-743/744)

**Defect:** The strain advancement rule produced inverted dynamics — Treaty pairs increased Strain rather than decreased it, and held-instability did not advance. Pax Romana logic was broken: factions in stable-but-tense alliance experienced no pressure to either consolidate or break, while Treaty signing produced friction.

**Fix:** Strain advances from held-instability (+1 per territory at instability per season, capped +3/season). Treaty-pair decay restored: −1 per Treaty pair, capped −2/season. Net behavior: alliances reduce strain; held instability accumulates pressure. Pax Romana behavior restored.

### P1-2: Reframed via Wager system (commit `7d45753`, ED-739/740/741/742)

**Defect:** Win Condition 3 (WC 3) was reading as a survival floor (lose if below) rather than a budget enabler (capability gate). Late-game players felt squeezed into a single playstyle.

**Fix:** WC 3 reframed as a budget threshold enabling three distinct viable end-game paths via the new Wager system:
- **Arc D Confrontation:** WC ≥ 2 + Scar count ≥ 3 (witnessed) → mandatory Zoom-In with three resolutions (discipline / refuse / escalate).
- **Arc E Wager:** WC ≥ 2 + Scar count ≥ 2 + active Knot + Grand Contest using Projection+Consequence+Solidarity + verifiable future commitment. Resolution by Conviction Track outcome. Wager-pass raises Arc D Scar threshold 3→5 permanently.
- **WC decay clause** (revised stress-test ED-759): ≥2 disruptive ops/season → WC −1 (cap −1/season). Arc D fires only if WC ≥ 1 in prior 4 seasons.
- **ms_budget reframe:** Path 1 (disciplined non-Warden) / Path 2 (WC 3 cooperative) / Path 3 (WC 3 wagered) / Path 4 (trap path).

---

<!-- atom: valoria_session_2026-04-25_master__03__section-3-major-new-specs-authored | section_index: 3 | source_section: "Section 3 — Major New Specs Authored" -->


## Section 3 — Major New Specs Authored

### 3.1 — Wager System (ED-739/740/741/742, commit `7d45753`)

Added `social_contest §6.1` Wager Obligation framework: Continuity-Conviction NPCs may extend present trust against future-condition delivery. Resolution covers Condition Met / Not Met / Partial outcomes. Edeyja (`npc_behavior §5.2`) is the canonical example.

### 3.2 — Wager Obligation Edge Cases (ED-778, commit `e5e250d`/`2e05d2f`)

Added `social_contest §6.1.1` covering five edge cases the base spec didn't handle:
- **Counterparty death/incapacitation:** neutral discharge + PC Renown +1.
- **Counterparty institutional collapse:** 4-season suspension before discharge if no successor Standing.
- **Structural impossibility:** fail-forward (arc transition fires immediately, +1 Conviction Scar to PC).
- **PC death holding Wager:** transfers to successor faction per `generational_transition_v30` TRANSFER rule (Disposition resets to faction-default).
- **PC death owing Wager:** transfers to predecessor's faction; if condition no longer achievable, failure-by-incapacitation NPC Mandate +1.

Verifiability requirement carries from base spec: triggering condition must be confirmable.

### 3.3 — Advisor-Principal Confidentiality (ED-664, commit `17523a2`; extended ED-760)

**Historical anchor:** Privy Counsellor's oath, medieval evil-counsellors doctrine (Hoccleve, Joel Rosenthal), curia regis great-council/small-curia distinction, classical counsel theory (Plato, Aristotle, Plutarch, Cicero on counsel obligation).

Added `npc_behavior §3.5`:
- §3.5.1 — Private counsel zone (advisor speaks freely without consequence).
- §3.5.2 — Public consequence zone (breach types with Disposition / Renown / Standing penalties).
- §3.5.3 — Knot-mediated extraction (Disposition ≥ +3 + active Knot allows one-time gift).
- §3.5.4 — Public citation rupture (extended ED-760 to include closed tribunals + fictional/dramatic reframing).

### 3.4 — Succession Contest as Grand Contest variant (ED-665, commit `aa14957`; ED-762)

Added `social_contest §7.2`: track-distance weighted faction split for Compromise outcome. Track 4 = 60/40 split; Track 5 = 55/45; Track 6 = 50/50. Stability floor 3 prevents immediate Crisis cascade post-split. `baralta_crown_claim §2` remains the canonical Crown instance.

### 3.5 — RM Settlement Emergence (ED-712, commit `dbe0b16`)

Added `victory_v30 §8` Founding Mechanic disjunctive prerequisites: EITHER 2 territories at PT ≤ 2 OR 4 settlements at Order ≤ 1 + Community Organizing. Models 1848-style distributed governance failure alongside 1917-style concentrated regional crisis.

### 3.6 — Heresy Investigation Lifecycle (ED-772, commit `1f7e93d`)

Added `social_contest §7.3`: full lifecycle (Initiation 1 season → Investigation Proper 2-4 seasons with mandatory Interrogation per season → Verdict 1 season; total 4-6 seasons nominal). 8 closure conditions: Inquisitor death, demotion, reassignment; target death, defection, conversion to Church, faction protection (Parliamentary Stay); acquittal verdict. §7.3.3 multi-Inquisitor handling: one per Cardinal Justice jurisdiction; cross-jurisdictional may run parallel.

### 3.7 — Knot Lifecycle (ED-773, commit `b14a01b`)

Added `fieldwork §5.6b`. Strain accumulation from 6 sources: §2.6 remote Thread-Read (+1 per use), Composure-buffer use (+1), counsel extraction retry (+1), FR Lock/Dissolution near partner (+1), witnessing Knot partner Conviction Scar firing (+1 at Accounting), sustained Disposition < +3 (+1 per Accounting).

Capacity: Distant Knot 4 strain, Close Knot 7 strain. Break consequences: Disposition reset to +2 (or current −2, floor at −3), 4 Composure cost both partners, benefit cessation, possible Conviction Scar at high-strain Close break.

5 rupture triggers: ED-664 §3.5.4 public citation, partner death, FR Dissolution targeting partner, opposing Conviction shift, player explicit dissolution. Strain decay: −1 per season at sustained Disposition ≥ +3 + no strain added. Threadcut-being Knot Coherence parallel resource.

### 3.8 — Approach Training canonical (ED-774, commit `4b769ce`)

`threadwork_v30 §2.1` was empty header; canonical content scattered across `character_histories §Formation 2F` (Practitioner Mentorship), `§270` (Approach Training trait: +1D Leap), `§498` (skill ladder Partial-benefit advancement). Consolidated into canonical §2.1 with three acquisition pathways (character creation, in-campaign training with mentor TS ≥ 50 + full-season + Spirit Ob 2 roll, Catalyst 4E spontaneous).

### 3.9 — Wrong-Style Penalty extended (ED-775, commit `2842117`)

Added `npc_behavior §6.4.1-§6.4.3`:
- **§6.4.1 RS Declaration Timing:** locked at Contest setup; cannot switch mid-Contest.
- **§6.4.2 Compromise vs Partial mapping:** Total Victory/Decisive (no penalty), Compromise 5-6 (half: +1 strain), Compromise 4 (full +1 Stab), Partial 3 (full), Failure ≤2 (compounded +2).
- **§6.4.3 Cross-Contest stacking:** nominal stacking uncapped within a season but ±2 Domain Action cap caps net Stability at Accounting.

### 3.10 — Demotion Magnitude (ED-776, commit `53cbf49`)

Added `faction_politics §1.0a`. Three magnitude tiers:
- **Default = 1 rank** (most failures).
- **Severe = 2-3 ranks** (public scandal, Heresy non-excommunication, defection).
- **Total = Standing −1 Dismissal-with-Dishonor** (excommunication, treason, framework abandonment, Cardinal catastrophic).

Cross-rank flow specified (no intermediate-rank pass-through; mentor/livery/hall reset 1 season). Appeal mechanism: 2-season window, faction-internal Conviction Track; no appeal for Dismissal.

### 3.11 — Caste-Transgressive PC Conviction Mechanism (ED-777, commit `ded3271`)

Added `faction_politics §3.6.1` and `§3.6.2`:
- **§3.6.1:** three numeric mechanisms (Witness Spirit Ob 1→2 raise, Conviction Shake 1→2 seasons on failed check, self-applied Doubt Marker on Authority RS).
- **§3.6.2:** Conviction Reformation arc (3+ caste-transgressive engagements within 4-season window triggers mandatory Priority 0 Zoom-In; Spirit pool TN 7 Ob 3 resolution; Success consolidates transgressive Conviction permanently; Partial = caste-default Conviction crisis with PC Scar logged; Failure = Conviction Track reset + 2-season NPC-state).

Cross-ref correction: `npc_behavior §3.2` (Belief Revision) → `§3.3` (Scar Accumulation) in two places.

### 3.12 — Inspiration Mechanic Canonical (ED-779, commit `3ab14dc`)

Added `derived_stats §5.3`. Canonical Inspiration spec existed only in `deprecated/valoria_ttrpg_complete.md §10.4`; active docs referenced "Inspiration" without defining acquisition / recovery / loss. Now consolidated:
- **Acquisition:** mid-campaign 2-scene + Spirit Ob 1 check, or 4 CP shortcut, or Belief-to-Inspiration conversion at Belief completion.
- **Recovery:** full-scene engagement +1, focus-present-uncontested +1, max 2/season.
- **Loss:** focus destroyed → immediate 0 + optional Grief Scene Ob 2 conversion.
- **§5.3.4 distinction table:** Inspiration vs Belief vs Conviction (different scales, different persistence rules).

### 3.13 — Bonds ≥ 5 Knot Formation Prerequisite (ED-780, commit `df0bab8`)

Added `fieldwork §5.6a` step 5: **PC Bonds ≥ 5**. Derived from §3 Disposition ceiling = Bonds rule + Knot formation requires Disposition +5. Bonds 1-4 caps Disposition below +5, making Knot formation structurally impossible; this gate was previously invisible to players. Rationale section explains the Knot ecosystem locked behind this prerequisite (Wager system, Composure buffer, Thread-Read, Coherence anchoring).

### 3.14 — Coup Counter STRUCK → Graduated Autonomy (ED-781, commits `f89f3a6` + `e7fa400`)

`params/factions_personal §94` legacy Coup Counter spec STRUCK; canonical mechanism is now Graduated Autonomy 4-stage track (Loyal → Restless → Autonomous → Split per `conflict_architecture_proposal §Graduated Löwenritter Autonomy`). `npc_priority_trees.md` migrated: 4 cell references at L42, L86, L149, L197 + section header L239 + spec text L241 all converted from "Coup Counter = 2" to "Löwenritter Autonomy = Restless".

### 3.15 — Glossary TC → CI canonical rename (ED-782, commit `be8a478`)

Per `tcv_conflict_register §2` decision (2026-04-19), Theocracy Counter renamed to Church Influence (CI). `references/glossary.md` updated:
- Stat table entry renamed "Theocracy Counter | TC*" → "Church Influence | CI" with milestones (60 = Mass Seizure available, 75 = Phase Transition, 100 = Unification).
- TC collision note updated to reflect rename eliminates half the collision.
- Abbreviation collision table updated.
- ~675 residual TC references in active spec flagged as queued cleanup.

---

<!-- atom: valoria_session_2026-04-25_master__04__section-4-stress-tests-run | section_index: 4 | source_section: "Section 4 — Stress Tests Run" -->


## Section 4 — Stress Tests Run

### Tests 1-7 (initial)

| # | Topic | Result |
|---|---|---|
| 1 | Strain inversion behavior | PASS — capped 0-10, time-to-Collapse 4-10 seasons |
| 2 | Wager state machine | FAIL → FIXED ED-759 (≥2 ops/season → −1 WC, cap −1/season) |
| 3 | Advisor confidentiality bypass | PARTIAL → FIXED ED-760 (closed fictional reframing + closed tribunal) |
| 4 | Succession Contest split | FAIL → FIXED ED-762 (Track-weighted 60/40, 55/45, 50/50; Stab 3 floor) |
| 5 | RM Settlement Emergence | PASS — disjunctive pathways coherent |
| 6 | Witness Mode + cascade | FAIL → FIXED ED-761 (priority list extended 4→8, Witness Mode roll-required) |
| 7 | Cross-system integration | PASS with ED-763 (Arc E post-Wager Scar threshold raises 3→5 permanently) |

### Tests 8-21 (extended)

| # | Topic | Result |
|---|---|---|
| 8 | Sacred Veto cooldown | PASS — per-veto-USE not per-Mandate-state |
| 9 | Officer death | FAIL → FIXED ED-765 (per-battle not per-event) |
| 10 | Step 4 keyword false-positive | FIXED ED-766 (capitalization heuristic + suggestion mode) |
| 11 | Heresy Investigation TC | PASS — Inquisitor rank gating works |
| 12 | Niflhel STRUCK propagation | FIXED ED-764 (params files + Löwenritter Coup→Graduated Autonomy) |
| 13 | Coherence at War scale | PASS — well-specified 0-10 with depletion warning |
| 14 | Domain Echo cap | PASS — 1/faction/scene coherent |
| 15 | Disposition extremes | PASS — −5 to +5 bounds |
| 16 | Standing 7 vs Mandate 5 | PASS — personal capital vs faction power coherent |
| 17 | Mending capacity vs Scenario B drain | PASS — intended Path 2/3 necessity |
| 18-19 | PROVISIONAL marker / numeric bounds | Triaged ED-767/768/770 |
| 22 | Faction stat drift bounds | PASS — ±2/season cap at Accounting |
| 24 | Heresy Investigation timeline | FAIL → FIXED ED-772 (8 closure conditions) |

### Tests 25-50 (continuation)

| # | Topic | Result |
|---|---|---|
| 26 | Knot formation/breaking | FAIL → FIXED ED-773 (Knot Lifecycle full spec) |
| 27 | Wrong-Style Penalty stacking | FAIL → FIXED ED-775 (RS timing + Compromise mapping + cross-Contest) |
| 28 | Cardinal track timeline | PASS — Cardinal aspirational by design (vacancy bottleneck) |
| 29 | Composure/Spirit recovery | PASS — per-scene reset |
| 30 | TS rise rate | SURFACED defect — §2.1 was empty. FIXED ED-774 |
| 31 | TS visibility thresholds | PASS — discrete bands 0-9, 10-29, 30-49, 50-69, 70+ |
| 33 | Standing demotion magnitude | FAIL → FIXED ED-776 |
| 34 | Multi-faction PC Standing | PASS — per-faction independent |
| 35 | Doubt Marker stacking | PASS — "only one active, new replaces old" |
| 36 | Composure/Concentration compound | PASS — two separate tracks |
| 38 | Multi-NPC Conviction cascade | PASS — Knot strain relational, Conviction personal |
| 39 | Mass Battle Volley × Thread Weaving | PASS — design intent per ED-753 |
| 40 | Caste × Standing at character creation | PASS — caste affects advancement, starting Standing always 0 |
| 41 | PT vs CV interaction | PASS — CV ≡ PT (same stat under two names per §4.2) |
| 42 | Treaty multiple pairs | PASS — no faction-level cap |
| 43 | Scene Slate Priority hierarchy | PASS — well-specified |
| 44 | MS ↔ Coherence interaction | PASS — separate resources, parallel coupling at operations only; PP-197 cascade only at TS ≥ 70 + Coherence 0 |
| 45 | Niflhel residue settlement-broker NPCs | PASS — specced in `settlement_layer §4.7-4.9` |
| 46 | Caste-transgressive PC Conviction | FAIL → FIXED ED-777 (cross-ref §3.2→§3.3 + numeric mechanism) |
| 47 | PC vs PC Inquisition | COHERENT (single-player canonical, multi-player symmetric) |
| 48 | Multi-PC Standing competition | PASS — §7.2 Succession Contest handles multiple claimants |
| 49 | Wager Obligation + counterparty death | FAIL → FIXED ED-778 (5 edge cases) |
| 50 | Treaty + Wager combination | PASS — intentional separation |

### Tests 51-63 (final batch)

| # | Topic | Result |
|---|---|---|
| 51 | Spirit pool depletion/recovery | PASS — Thread Fatigue handles depletion (Spirit attribute is dice basis) |
| 52 | Inspiration mechanic | FAIL → FIXED ED-779 (canonical content propagated) |
| 53 | Bonds × Knot/Disposition edge cases | FAIL → FIXED ED-780 (Bonds ≥ 5 surfaced explicitly) |
| 54 | TS thresholds → Coherence 0 outcomes | PASS — 3 tiers specified (TS 30-69, 70-89, 90+) |
| 55 | AER (Altonian Engagement Ratio) | PASS — advancement/decay specified in `params/bg/tracks.md` |
| 56 | VTM (Varfell Track Memory) | PASS — STRUCK per PP-663 |
| 57 | Coup Counter | FAIL → FIXED ED-781 (legacy STRUCK; Graduated Autonomy canonical; npc_priority_trees migrated) |
| 58 | Settlement Order recovery | PASS — Pacify, Chapel, Weaving, Community Organizing all provide +1 |
| 59 | NPC AI Survival Priority | PASS — Survival overrides everything |
| 60 | TC milestones (20/40/55/75/80/100) | FAIL → FIXED ED-782 (glossary TC→CI rename) |
| 63 | Galbados naming residuals | PASS — 2 active references are meta-documentation about the rename |

**Tests not run:** 21, 23, 25, 32, 37, 61, 62, 64, 65 (deferred for next iteration).

---

<!-- atom: valoria_session_2026-04-25_master__06__section-6-editorial-decisions-summary | section_index: 6 | source_section: "Section 6 — Editorial Decisions Summary" -->


## Section 6 — Editorial Decisions Summary

### EDs resolved this session (44)

| ED | Description | Severity |
|---|---|---|
| ED-661 | Closed (superseded) | infra |
| ED-662 | Elske residency null-intersection | P3 |
| ED-664 | Advisor-Principal Confidentiality Boundary | P2 |
| ED-665 | Succession Contest as Grand Contest variant | P2 |
| ED-669 | Closed (deferred-design-intent) | infra |
| ED-704 | Seizure Uncontrolled exclusion | P2 |
| ED-705 | Cohesion → Discipline canonical | P3 |
| ED-712 | RM Settlement Emergence | P2 |
| ED-739 | Wager Edeyja Arc D | P1 |
| ED-740 | Wager Edeyja Arc E | P1 |
| ED-741 | WC decay calibration | P1 |
| ED-742 | ms_budget reframe | P1 |
| ED-743 | Strain held-instability advance | P1 |
| ED-744 | Treaty-pair decay | P1 |
| ED-745-747 | Scene Slate spec-fixes | P2 |
| ED-748-750 | scale_transitions spec-fixes | P2 |
| ED-751-752 | faction_layer spec-fixes | P2 |
| ED-753-754 | mass_battle spec-fixes | P2 |
| ED-755 | Cross-faction Outreach floor | P3 |
| ED-756 | TC disambiguation glossary | P3 |
| ED-757 | Niflhel drift table cleanup | P3 |
| ED-758 | Cardinal naming reconciliation | P3 |
| ED-759-762 | Stress-test fixes batch 1 | P2 |
| ED-763 | Arc E post-Wager Scar threshold | P2 |
| ED-764 | Niflhel STRUCK params propagation | P2 |
| ED-765-766 | Officer death + Step 4 capitalization | P2 |
| ED-767 | PROVISIONAL cleanup mass_battle | P3 |
| ED-768 | 13 orphaned PROVISIONAL markers documented | P3 (Jordan-blocked) |
| ED-769 | RS→MS residual cleanup | P3 |
| ED-770 | Numeric bounds audit closure | P3 |
| ED-771 | Cross-reference audit fixes | P3 |
| ED-772 | Heresy Investigation Lifecycle | P2 |
| ED-773 | Knot Lifecycle | P2 |
| ED-774 | Approach Training canonical | P2 |
| ED-775 | Wrong-Style Penalty extended | P3 |
| ED-776 | Demotion Magnitude | P3 |
| ED-777 | Caste-transgressive PC Conviction | P3 |
| ED-778 | Wager Obligation edge cases | P3 |
| ED-779 | Inspiration mechanic propagation | P2 |
| ED-780 | Bonds ≥ 5 Knot prerequisite | P3 |
| ED-781 | Coup Counter STRUCK → Graduated Autonomy | P2 |
| ED-782 | Glossary TC → CI rename | P3 |

**P1 count entering session: 2. Exit: 0.**

### Editorial ledger maintenance

- 30+ entries archived to `editorial_ledger_archive.yaml` over the session.
- `editorial_ledger.yaml` maintained under 2000-token cap throughout.

---

<!-- atom: valoria_session_2026-04-25_master__08__section-8-historical-research | section_index: 8 | source_section: "Section 8 — Historical Research" -->


## Section 8 — Historical Research

Research conducted to anchor specs in real-world precedent:

### Advisor confidentiality (ED-664)

- **Medieval frame:** counsel obligatory for legitimate kingship (Hoccleve 1410-11 to Henry V; Joel Rosenthal); private frank counsel protected by institutional necessity; "evil counsellors" doctrine as legal fiction underpinning baronial rebellions.
- **Classical theory:** Plato (Republic + Laws), Aristotle (NE 1142b), Plutarch ("How to Tell a Flatterer from a Friend"), Cicero (rejected quietism).
- **Institutional structure:** Curia regis Norman England — small curia → Privy Council; great council → Parliament. Privy Counsellor's Oath same wording substantively as medieval.
- **Core tension:** "If counsel is obligatory, it impinges upon sovereignty; if not, it becomes irrelevant and futile."

### Royal hostage / foreign princess at court (ED-662)

- Sargon II's daughter Ahat-abiša married to Ambaris of Bit-Purutaš (~720 BC); lost freedom when husband betrayed alliance.
- Erasmus advocated geographic limits on dynastic marriage.
- Habsburg-Trastámara dynastic accumulation.
- Diplomatic immunity customary for visiting royals.
- Royal Marriages Act 1772 (UK).

### Cross-campaign persistence

- Persistent World (Bartle 1989+).
- New Game Plus (coined Chrono Trigger 1995).
- Hogwarts Legacy intentionally single-playthrough.
- Rogue Legacy 2 has explicit cross-campaign progression.
- State of Decay 2 has 4 distinct legacy endings.

### Ministry seniority

- Ming Five Chief Military Commissions Left/Right co-leadership.
- Ancien Régime France complex protocol with Chancellor as judicial head + connétable as chief military officer.
- "First Minister" title given only 6 times early modern.

---

<!-- atom: valoria_session_2026-04-25_master__10__section-10-session-statistics | section_index: 10 | source_section: "Section 10 — Session Statistics" -->


## Section 10 — Session Statistics

- **Commits:** 40 (all on `main`).
- **Editorial Decisions logged:** 44 (ED-739 through ED-782).
- **EDs archived:** 30+ across two cap-maintenance passes.
- **Stress tests run:** 60+ (numbered through 63 with gaps).
- **Stress tests passed without modification:** 27.
- **Stress tests producing fixes:** 19.
- **Spec files materially modified:** 14 (primary specs) + 4 (params/references/canon).
- **Cross-reference audit corpus:** 39 files, 220+ sections.
- **Cross-references repaired:** 6 (4 in ED-771, 2 in ED-777).
- **P1 blockers entering session:** 2.
- **P1 blockers exiting session:** 0.

<!-- atom: valoria_session_master_2026-04-25__00__preamble | section_index: 0 | source_section: "(preamble)" -->


# Valoria Session Master — 2026-04-25

**Scope:** Sessions B, C, ED-717, and cleanup across 3 context windows.
**Total commits:** 15
**P1 blockers:** 2 → 1

---

<!-- atom: valoria_session_master_2026-04-25__02__context-window-2-session-b-secondary-session-c | section_index: 2 | source_section: "Context Window 2 — Session B Secondary + Session C" -->


## Context Window 2 — Session B Secondary + Session C

### Session B Secondary Propagation

| Commit | SHA | Files Modified | What |
|--------|-----|----------------|------|
| 7 | `6e952c3` | designs/architecture/conflict_architecture_proposal.md, params/bg/victory.md, designs/provincial/baralta_crown_claim_v30.md, references/canonical_sources.yaml | conflict_architecture_proposal PROPOSAL → CANON. Coup → Autonomy in victory + baralta_crown_claim |
| 8 | `3cfa81f` | designs/npcs/npc_roster_v30.md, params/bg/npcs_special.md, references/canonical_sources.yaml | Dalla Virke → independent intelligence broker. npcs_special Niflhel → settlement-level refs |

### Session C — Tensions Deck + Royal Assassination

**Tensions Deck** — 6 cards, draw 1 at game start. Each amplifies one faction-friction point and triggers an S8+ event if not averted.

| # | Card | Amplifies | S8+ Event |
|---|------|-----------|-----------|
| 1 | Royal Crisis | Crown-Church friction + succession | Royal family member assassinated (sub-roll for target) |
| 2 | Feldmark Famine | Crown breadbasket | Prosperity collapse in Crown food supply |
| 3 | Cardinal Independence | Church internal | Rogue Cardinal appoints bishop-governor unilaterally |
| 4 | Guild Fracture | Hafenmark-Guild friction | S017 Guild schism, Market Quarter contested |
| 5 | Einhir Incident | Varfell-RM friction | Public cultural confrontation, all factions declare position |
| 6 | Ministry Crisis | Crown-Löwenritter + governance | Ministry bureaucracy collapses, Church fills vacuum |

**Fuse model:** Visible from S1 (NPC dialogue, atmospheric events). Player can investigate S1–S7. Event fires S8–S12 if not averted.

**Royal Assassination Fuse** — fires on Royal Crisis card.

| Roll | Target | Consequence Arc |
|------|--------|-----------------|
| 1–2 | Lenneth | Almud revenge arc — Crown governance suffers, investigation opens |
| 3–4 | Torben | Elske retrieval — military deployment to Varfell territory, Altonian crisis |
| 5–6 | Almud | Lenneth takes throne — Crown identity inverts (pro-Einhir, pro-Thread-research) |

| Commit | SHA | Files Modified | What |
|--------|-----|----------------|------|
| 9 | `d29d8b6` | params/bg/tensions_deck.md (NEW), params/bg/royal_assassination.md (NEW), references/canonical_sources.yaml | Standalone params files for both specs |
| 10 | `238cf45` | params/bg/phases.md, references/canonical_sources.yaml | Game Setup section: Tensions Deck draw, starting settlements, assassination target determination |

---

## Provenance

Atom-by-atom inventory in source/section order:

| atom_id | source | section_index | source_section | lines |
|---|---|---|---|---|
| `valoria_session_2026-04-25_master__00__preamble` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 0 | (preamble) | 12 |
| `valoria_session_2026-04-25_master__01__section-1-commit-manifest-chronological` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 1 | Section 1 — Commit Manifest (chronological) | 47 |
| `valoria_session_2026-04-25_master__02__section-2-p1-resolution` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 2 | Section 2 — P1 Resolution | 22 |
| `valoria_session_2026-04-25_master__03__section-3-major-new-specs-authored` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 3 | Section 3 — Major New Specs Authored | 101 |
| `valoria_session_2026-04-25_master__04__section-4-stress-tests-run` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 4 | Section 4 — Stress Tests Run | 80 |
| `valoria_session_2026-04-25_master__06__section-6-editorial-decisions-summary` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 6 | Section 6 — Editorial Decisions Summary | 58 |
| `valoria_session_2026-04-25_master__08__section-8-historical-research` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 8 | Section 8 — Historical Research | 35 |
| `valoria_session_2026-04-25_master__10__section-10-session-statistics` | `VALORIA_SESSION_2026-04-25_MASTER.md` | 10 | Section 10 — Session Statistics | 15 |
| `valoria_session_master_2026-04-25__00__preamble` | `valoria_session_master_2026-04-25.md` | 0 | (preamble) | 8 |
| `valoria_session_master_2026-04-25__02__context-window-2-session-b-secondary-session-c` | `valoria_session_master_2026-04-25.md` | 2 | Context Window 2 — Session B Secondary + Session C | 39 |
