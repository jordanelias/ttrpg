---
atom_id: valoria_session_2026-04-25_master__03__section-3-major-new-specs-authored
source_file: VALORIA_SESSION_2026-04-25_MASTER.md
source_section: "Section 3 — Major New Specs Authored"
section_index: 3
total_sections: 11
line_count: 101
char_count: 8656
source_sha256: dedb9b7e51dc8e7b
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

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
