---
atom_id: master_document_2026-04-25__49__8-9-faction-balance-simulation-work-remains-valid-
source_file: master_document_2026-04-25.md
source_section: "§8.9 Faction-balance simulation work remains valid for Mode 3 calibration"
section_index: 49
total_sections: 50
line_count: 112
char_count: 6690
source_sha256: 312f97236be6f341
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## §8.9 Faction-balance simulation work remains valid for Mode 3 calibration

**Decision:** The 37 simulator iterations and ~50,000 runs produced calibration-relevant data for Mode 3 Strategy tuning, not the primary balance frame.
**Rationale:** Simulation cannot model emotional engagement. It can model arithmetic-completion rates of Strategy mode. Useful for one of three modes.
**Status:** Final. sim_balance.py preserved as Mode 3 calibration tool.

---

# PART IX — RELATIONSHIP TO EXISTING CANON

This section maps proposals to canonical document requirements.

| Canonical Document | Required Update | Priority |
|---|---|---|
| `player_agency_v30.md` | Add §0 mode declaration. Update §5.2 to specify 3-scene Ascension Arc. Add Wanderer mode mechanics to §5.3. Add Trajectory mode (entirely new section). | P0 |
| `victory_v30.md` | Convert §3.1–§3.6 from arithmetic milestones to Victory Scene specifications. Update §3.4 with Tribune Compact. Update §10 Win Probability table. | P0 |
| `peninsular_strain_v30.md` | Reconcile §6.2 with three-mode architecture (Universal Sovereignty as aspirational, milestones as Mode 3 targets). | P0 |
| `campaign_architecture_v30.md` | Update §7 (Portrait Retirement) to be primary Wanderer mechanism. Add Trajectory Endgame Sequence. Add Victory Scene templates. | P0 |
| `videogame_mode_spec.md` | Add §6 (or new section) for emotional engagement modes. Specify mode-specific UI surfaces. | P0 |
| `factions_personal_v30.md` | Update Hafenmark Proclamation with Wealth cost. Update Hafenmark PI condition to 7. Add Tribune Compact for Varfell. | P0 |
| `params/bg/victory.md` | Sync to PP-540/PP-541. Apply VTM → WR replacement. Update Co-Victory thresholds against current PV values. | P1 |
| `geography_v30.md` | Operationalize BALANCE-005 (Hafenmark food dependency) via Calamity Refugee penalty. Update T15 Askeheim with PV 2 post-WC ≥ 3. | P1 |
| `npc_character_analyses_v30.md` | Specify post-Vaynard Varfell succession (Maret Uln canonical). Disambiguate Baralta personal vs faction Mandate. | P0 |
| `conflict_architecture_proposal.md` | Already canonical — no changes needed; this proposal underpins three-mode design. | (no update) |
| `scale_transitions_v30.md` | Already supports two-scale architecture; preserved unchanged. | (no update) |
| (new) `three_modes_specification.md` | Author this document from `three_modes_of_fulfilment_2026-04-25.md` proposal. | P0 |
| (new) `trajectory_templates.md` | Author 12 Trajectory Goal templates. | P1 |

---

# PART X — META-OBSERVATIONS ON THE DESIGN PROCESS

Five reframes occurred in this session, each subsuming the prior:

1. **Strategic-layer audit** assumed faction-balance was the question. Output: 6-proposal §6 set targeting strategic equality.
2. **Monte Carlo simulation** assumed mechanical changes could equalize win rates. Output: 11-flag calibration achieving 6.9 pp spread.
3. **Player-experience reframe** revealed strategic-layer ranking inverts player-experience ranking. Output: §6.9–§6.15 proposals targeting Conviction/Duty/Slate richness.
4. **Leadership felt-win** revealed that faction-leadership attainment has no canonical fulfilment moment. Output: 3-scene Ascension Arc as Personal Victory.
5. **Three modes of fulfilment** revealed that "winning" itself is mode-dependent. Output: complete reframe of fulfilment architecture.

Each reframe was triggered by a single sentence from Jordan that exposed a hidden assumption in the prior frame:

- Reframe 3 trigger: "Perform audit from a radically fresh perspective based upon player experience"
- Reframe 4 trigger: "Players need to be able to feel a 'win' if they end up controlling a faction"
- Reframe 5 trigger: "A player needs to be able to find fulfilment in the game ranging from whether they simply want to be wandering within the world... all the way through to conquering the peninsula"

**Process implication:** the simulator-driven approach (Stages 1–2) was working on a substrate where the design problem had not yet been correctly framed. The sim work remains valid as Mode 3 sub-calibration but did not produce primary design conclusions. The primary conclusions came from text-based reasoning about player intent.

**For future similar work:** before extensive simulation, verify the design problem at the player-experience level. Simulators answer "what does the math do" but cannot answer "what does the player want to feel." The latter question must come first.

---

# PART XI — DOCUMENT MAP

For navigation across deliverables produced this session:

```
/mnt/user-data/outputs/
├── faction_balance_audit_2026-04-25.md (47KB)
│   └── Stage 1: Strategic-layer audit. Six §6 proposals.
│       Status: superseded as primary frame; valid as Mode 3 input.
│
├── balance_simulation_report_2026-04-25.md (21KB)
│   └── Stage 2: Monte Carlo simulation report. 14 iterations.
│       Status: sim work valid for Mode 3 calibration.
│
├── sim_balance.py (36KB)
│   └── Monte Carlo simulator. 750 lines. 4-faction d10 TN-7 model.
│       Status: tool preserved for Mode 3 calibration.
│
├── faction_balance_audit_player_experience_2026-04-25.md (51KB)
│   └── Stage 3: Player-experience reframe. Conviction/Duty/Slate analysis.
│       Status: superseded as primary frame; informs Modes 1–2.
│
├── leadership_win_proposal_2026-04-25.md (21KB)
│   └── Stage 4: 3-scene Ascension Arc. Personal Victory mechanic.
│       Status: subsumed into Mode 3 Stature 7 path.
│
├── three_modes_of_fulfilment_2026-04-25.md (39KB)
│   └── Stage 5: Three emotional engagement modes. PRIMARY FRAME.
│       Status: canonical recommendation.
│
└── master_document_2026-04-25.md (THIS DOCUMENT)
    └── Consolidation. Single reference for all session outcomes.
```

For implementation work, this master document is the single entry point. Companion deliverables are reference material only.

---

# PART XII — FINAL STATEMENT

The session began asking: **"Are factions balanced for win rate?"**

It ends answering: **"What does winning even mean?"**

Three answers, each legitimate:

- **Wanderer**: Winning means living a life worth recording in a Portrait.
- **Trajectory**: Winning means reaching the conclusion you authored at the start.
- **Strategy**: Winning means seeing your faction's victory performed as a scene.

The same engine. The same Valoria. Three games. Three fulfilments.

The faction-balance question — whether Crown wins 19% to Varfell's 18% — matters only for the third mode, where it has been mostly resolved. The first two modes don't measure faction win rate at all. They measure whether the player got what they came for.

This is the design.

---

**End of master document. 2026-04-25.**
