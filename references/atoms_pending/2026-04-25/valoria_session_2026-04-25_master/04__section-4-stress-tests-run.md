---
atom_id: valoria_session_2026-04-25_master__04__section-4-stress-tests-run
source_file: VALORIA_SESSION_2026-04-25_MASTER.md
source_section: "Section 4 — Stress Tests Run"
section_index: 4
total_sections: 11
line_count: 80
char_count: 5097
source_sha256: dedb9b7e51dc8e7b
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

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
