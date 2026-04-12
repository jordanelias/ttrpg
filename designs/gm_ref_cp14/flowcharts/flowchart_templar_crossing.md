<!-- DEPRECATED -->
> **DEPRECATED — 2026-04-11**
> CP14 flowchart. Based on outdated CP14 mechanics.
> Do not use as a canonical source.

---

# FLOWCHART: The Templar Crossing
## Seed: Season 2. Church deploys Templars into T6 (Varfell Highlands). TC=34. Vaynard present.
## Mode: HYB (BG opening → Zoom In → TTRPG personal scene → Zoom Out)
## Tracks at seed: TC=34, RS=68, IP=22, PI=5. Church M=4(5-1 diplomatic), Varfell holds T6.

---

### NODE 0: Church declares Templar deployment into T6
State: TC=34, RS=68. Church Mil 4D vs Varfell Mil 5D (home terrain +1D [PROVISIONAL]).
Branch conditions: BG Battle outcome (expected values).

  ├── BRANCH A: Church wins BG Battle (net margin ≥1, ~35%)
  │   State delta: Varfell loses T6. Church Mil stays 4. TC +1 next season (territory control). Vaynard is now in Church-controlled territory.
  │   → NODE A1: Church occupies T6. Zoom In fires (Vaynard in territory).
  │       Branch conditions: Vaynard's Phase 4 Leap.
  │       ├── BRANCH A1a: Vaynard fails Leap (1% probability — see G3 analysis)
  │       │   State delta: No Gap stabilisation. RS −4 (Gap forms). −4 Composure.
  │       │   → NODE A1a1: Gap forms in Church-occupied T6. RS=64.
  │       │       → Monstrous Incursion check: RS≤60 next season triggers Incursion.
  │       │       Terminal: PRESSURE (RS declining, T6 a liability for Church)
  │       │
  │       └── BRANCH A1b: Vaynard succeeds Leap (99%)
  │           State delta: Gap averted. RS=68. TS 56→57.
  │           → NODE A1b1: Debate with Klapp (Church now in control).
  │               Branch conditions: Conviction Track outcome (Church-favourable audience, resistance 3).
  │               ├── BRANCH A1b1-Win (Vaynard wins, track ≥7 — requires leverage mechanic or major pool swing)
  │               │   State delta: Klapp releases Vaynard. Church reputation −1 (lost a public debate in their territory).
  │               │   [DEAD BRANCH — mechanically near-impossible at median pools without ED-054 leverage]
  │               │
  │               ├── BRANCH A1b1-Stalemate (track 4–6 — most likely at ~55%)
  │               │   State delta: Vaynard detained but not condemned. Escapes when Varfell forces retreat and Church regroups.
  │               │   → NODE A1b1S: Vaynard free, Church holds T6. Intelligence gained: pre-existing Gap noted.
  │               │   Terminal: PRESSURE (Church expanding; practitioner underground network threatened)
  │               │
  │               └── BRANCH A1b1-Lose (track ≤3 — Klapp wins, ~45%)
  │                   State delta: Vaynard formally detained. Church gains practitioner intelligence.
  │                   → NODE A1b1L: Inquisitorial proceeding opens (see §6.7 Asymmetric Proceedings).
  │                   [GAP: No rule for what "detained practitioner" means mechanically — NPC action?]
  │                   Terminal: CAMPAIGN EVENT (practitioner captured; Resistance/Vaynard arc activated)
  │
  ├── BRANCH B: Tie / Varfell narrow hold (net margin 0–1, ~65%)
  │   State delta: T6 holds. Church Mil 4→3 (battle losses). TC unchanged from battle.
  │   Vaynard is in Varfell-controlled territory post-battle.
  │   → NODE B1: Zoom In fires (battle ongoing; Vaynard in T6).
  │       Branch conditions: Vaynard's Phase 4 Threadwork success (99% Overwhelming).
  │       ├── BRANCH B1a: Gap stabilised (99%)
  │       │   State delta: RS=68. TS=57. Vaynard not in danger (Varfell controls the zone).
  │       │   → NODE B1a1: Klapp arrives at edge of engagement for parley.
  │       │       Branch conditions: Does Vaynard engage with Klapp?
  │       │       ├── BRANCH B1a1-Engage: Vaynard initiates debate. (This session's primary path — see NODE B1a1D)
  │       │       │   → NODE B1a1D: Debate (same resolution tree as A1b1 above)
  │       │       │   [PC choice determines — no mechanical forcing]
  │       │       │
  │       │       └── BRANCH B1a1-Withdraw: Vaynard departs with Varfell forces.
  │       │           State delta: No debate. Klapp notes practitioner presence. Church Intel activated.
  │       │           → NODE B1a1W: No immediate consequence. Church Investigation Action available next season.
  │       │           Terminal: STABLE (short term) / PRESSURE (if Church investigates)
  │       │
  │       └── BRANCH B1b: Gap not stabilised (1%)
  │           → See NODE A1a1 (same RS consequence regardless of territory control)
  │
  └── BRANCH C: PC intervenes in BG Battle (non-Vaynard PC changes outcome)
      State delta: PC uses a Domain Action to reinforce Varfell or block Church.
      Branch conditions: PC's Domain Action roll (faction-specific).
      ├── BRANCH C1: PC Domain Action succeeds
      │   → Varfell hold strengthened. Church forced to withdraw this season.
      │   → Church Mandate −1 (public failure). TC momentum stalled.
      │   → NODE C1a: Vaynard's Thread work proceeds unimpeded. No Zoom In combat risk.
      │   Terminal: STABLE (Varfell secured; Church set back 1–2 seasons)
      │
      └── BRANCH C2: PC Domain Action fails
          → Battle resolves per BG mechanics (Branches A or B above).
          → PC takes Faction Consequence: Influence −1 (failed public action).
          Terminal: PRESSURE (PC credibility damaged; same battle resolution)

---

## CROSS-MODE COMPARISON

| Property | TTRPG | Hybrid (this session) | Board Game |
|----------|-------|----------------------|------------|
| Battle resolution | Full TTRPG mass combat (multi-turn) | BG rolls first; Zoom In for personal scene | BG roll only; 3-step resolution |
| Practitioner role | Full Phase 4 Leap and ops | Phase 4 rear-only (PP-101); else Phase 5 front-line | Abstracted to Co-Movement card |
| Debate stakes | Personal belief/faction echo | Conviction Track → narrative (captured/free) + queued domain echo | N/A (no debate at BG scale) |
| Thread consequences | RS changes immediate | RS changes immediate; queue domain echo | RS changes at Accounting only |
| Player decisions/scene | High (combat allocation + Thread + debate) | High (same) | Low (BG roll + 1 tactic card) |
| Dominant tension | Personal survival + Thread risk | Mode collision (personal vs strategic) | Clock management (TC/IP/RS) |

**Cross-mode finding:** The Hybrid mode correctly bridges both layers but produces the highest cognitive load of any mode (tracking both BG suspended state and TTRPG active state simultaneously). This confirms Mode J finding: the Zoom In/Out procedure needs a GM reference card (ED-055).

---

## LINKS TO EXISTING SCENARIO DOCUMENTS

- **valoria_emergent_scenarios.md:** SCENARIO 1 (Practitioner Enters Combat) confirmed by this flowchart — Vaynard's Phase 4 Leap path is exactly SCENARIO 1's "No declared attacker → Eligible → Diagnosis → Leap" tree. No contradiction.
- **valoria_narrative_scenario_chains.md:** ARC 2 (Vaynard) — the practitioner detention branch (A1b1-Lose) directly feeds into Vaynard's "Inquisitor risk" arc. This flowchart extends that arc with the specific hybrid trigger condition.
- **DEAD BRANCH noted:** BRANCH A1b1-Win is mechanically near-impossible without ED-054 leverage mechanic. This means player agency is severely limited in the Klapp debate without editorial resolution of ED-054. This is a campaign-design concern: a GM who seeds this scenario must understand ED-054 is needed for Vaynard to have a viable win path.
