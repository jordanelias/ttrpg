# Valoria Simulation Workplan v1
## Long-Term Iterative Plan with NRSE All-Directions Analysis

**Date:** 2026-05-10
**Status:** Working artifact, committed to `references/simulation_workplan_v1.md`
**Supersedes:** Ad-hoc simulation approach used in this session
**Companion docs:** `coverage_matrix.md`, `handoff_running_simulations.md`, `handoff_review.md`

---

## §0 — GOAL AND APPROACH

### §0.1 The goal

Achieve full canonical coverage validated through granular simulation across 9 archetypes. The simulation pipeline is a **gap-discovery and correctness-validation instrument**, not just a deliverable. Each simulation must catch:

1. **Conflicts** — canon contradicting itself across files
2. **Errors** — wrong values, broken formulas, superseded rules still in active docs
3. **Incongruencies** — rules that don't fit Valoria's design principles
4. **Bad gameplay** — mechanics that produce unfun, unintuitive, or grindy play
5. **Excessive crunch** — complex mechanics without proportional design value
6. **Unnecessary systems** — mechanics that could be folded into existing ones
7. **Missing mechanics** — gaps where canon is silent on a needed rule

### §0.2 The approach

**Iterative.** Each simulation pushes canon updates immediately after running. Sessions interleave between:
- **Sim sessions** — run an archetype campaign, catch issues
- **Propagation sessions** — resolve accumulated EDs, propagate to design docs

**NRSE all-directions at every step.** Every mechanic exercised in simulation gets evaluated against:
- Necessary, Robust, Smooth, Elegant
- Top-down, bottom-up, vertical, diagonal, lateral, horizontal

Failure on any axis = a logged finding.

**License to innovate** when canon is silent after granular search. Mark proposals as `[INNOVATION-PROPOSAL — needs ratification]`. Jordan ratifies before innovation enters canon.

**Coverage matrix as live tracking instrument.** After every sim, update `coverage_matrix.md` to reflect mechanics moved from `—` to `✓` to `✓✓`.

---

## §1 — ITERATION CYCLE

### §1.1 The standard sim session flow

```
┌─────────────────────────────────────────────────────────────────┐
│ Session N: Archetype A_x simulation                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  0. Pre-bootstrap reads (session log, ED ledger)                │
│         ↓                                                       │
│  1. Bootstrap → status block                                    │
│         ↓                                                       │
│  2. Canon pull (28 base files + archetype-specific)             │
│         ↓                                                       │
│  3. NRSE-checkpoint #0: prep review of archetype mechanics      │
│         ↓                                                       │
│  4. Setup: PC, NPCs, scenario, starting state                   │
│         ↓                                                       │
│  5. NRSE-checkpoint #1: setup integrity                         │
│         ↓                                                       │
│  6. Sim Year 1 granular (Phase 4 → Phase 5 → personal scenes)   │
│         ↓                                                       │
│  7. NRSE-checkpoint #2: Y1 audit                                │
│         ↓                                                       │
│  8. Sim Year 2 granular                                         │
│         ↓                                                       │
│  9. NRSE-checkpoint #3: Y2 cumulative audit                     │
│         ↓                                                       │
│  10. Sim Years 3-7 (compressed if context budget tight)         │
│         ↓                                                       │
│  11. NRSE-checkpoint #4: final audit                            │
│         ↓                                                       │
│  12. Findings classification & innovation proposals             │
│         ↓                                                       │
│  13. ED entries opened (Commit 1: editorial scope)              │
│         ↓                                                       │
│  14. Resolutions (in-session) → Commit 2                        │
│         ↓                                                       │
│  15. Propagation to design docs (Commit 3 + canonical SHAs)     │
│         ↓                                                       │
│  16. Coverage matrix update                                     │
│         ↓                                                       │
│  17. Session log close (g.safe_session_close)                   │
└─────────────────────────────────────────────────────────────────┘
```

### §1.2 Propagation session flow (every 2-3 sim sessions)

```
┌─────────────────────────────────────────────────────────────────┐
│ Propagation session: clear accumulated EDs                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Bootstrap + pull all EDs marked "resolved" but not "closed" │
│  2. For each ED:                                                │
│     a. Read affected design docs                                │
│     b. NRSE-check the proposed text edit                        │
│     c. Apply edit                                               │
│     d. Update canonical_sources.yaml SHA                        │
│  3. Batch commit (editorial scope)                              │
│  4. Mark all ED entries as "closed"                             │
│  5. Update session log                                          │
└─────────────────────────────────────────────────────────────────┘
```

### §1.3 Interleaving

Recommended sequence:
- Session 1: Sim A2 TOTAL WAR
- Session 2: Sim A3 SCHISM
- Session 3: Propagation pass (clear A2+A3 EDs)
- Session 4: Sim A6 DEEP THREADWORK
- Session 5: Sim A4 WARDEN AWAKENING
- Session 6: Propagation pass
- Session 7: Sim A5 DIPLOMATIC CASCADE
- Session 8: Sim A7 ANARCHY DESCENT
- Session 9: Propagation pass
- Session 10: Sim A8 GENERATIONAL
- Session 11: Sim A9 STEADY SEASON
- Session 12: Sim A1 FUSE extension
- Session 13: Final propagation
- Session 14: Coverage matrix close-out, summary

~14 sessions total. ~300k chars of sim deliverables + ~80-120 ED entries + ~30-50 canon propagation commits.

---

## §2 — NRSE ALL-DIRECTIONS FRAMEWORK

### §2.1 NRSE criteria (per canon §canon_terms §definitions)

| Letter | Criterion | Applied to mechanic M |
|--------|-----------|----------------------|
| **N** | Necessary | Would removing M worsen gameplay? Does M support a cohesive experience from all directions? |
| **R** | Robust | Does M allow strategy, customization, creativity? Does it generate emergent narrative hooks? Is M fully formed and error-free? |
| **S** | Smooth | Does M integrate cleanly with interdependent mechanics? Does it zoom in/out across scales? Transitions cleanly between systems? Calculations consistent with adjacent mechanics? |
| **E** | Elegant | Logically simple? Clear approach? No unnecessary overhead? Player intuits complex outcomes from simple choices? |

**Failure modes per criterion:**
- N-fail: M is redundant with another mechanic. Remove or fold.
- R-fail: M produces unfun play, no strategic depth, no customization. Redesign or strip.
- S-fail: M conflicts with adjacent mechanic, breaks at scale transition, inconsistent calculation. Fix integration.
- E-fail: M requires extensive memorization or sub-rules. Simplify.

### §2.2 Six directions

| Direction | Test |
|-----------|------|
| **Top-down** | Victory condition → faction layer → personal scene: does intent flow down correctly? E.g., if Peninsular Sovereignty requires Accord ≥ 2, do faction-level Govern actions actually produce Accord at expected rate? Does personal-scale governance work (Standing 5+ Governor) feed back appropriately? |
| **Bottom-up** | Personal scene → Domain Echo → faction layer → world-state: does emergence work? Does a Sufficient-Scope personal action produce sensible faction effects? Do faction-level patterns aggregate to world-state changes (MS, IP, Strain)? |
| **Vertical** | Scale transitions (Personal ↔ Settlement ↔ Territory ↔ Peninsula): consistent? E.g., Govern action operates at territory scale but affects settlement Order which affects Accord. Are scale boundaries clean? |
| **Diagonal** | Cross-silo interactions: fieldwork ↔ threadwork ↔ social contest ↔ combat ↔ Piety/CI ↔ faction layer. Do silos interact correctly when they intersect? E.g., does Thread-Read during fieldwork generate proper Domain Echoes? Does combat damage interact with Coherence (Wound → Coherence stress)? |
| **Lateral** | Same mechanic across factions/territories/NPCs: applied consistently? E.g., does Suppress work the same way for Crown vs Hafenmark vs Varfell? Does Govern Ob computation use same formula across all controllers? |
| **Horizontal** | Timing/sequence: Phase 4 → Phase 5 → Accounting → next season → Year-End. Do effects fire in correct order? Are cooldowns honored? Are seasonal caps enforced? |

### §2.3 NRSE evaluation per checkpoint

At each checkpoint, the simulator runs the active mechanics through a matrix:

```
                  N    R    S    E    TD   BU   V    D    L    H
Mechanic X1       ✓    ✓    ?    ✓    ✓    ✓    ✓    ?    ✓    ✓
Mechanic X2       ✓    ✓    ✓    ✓    ✓    ✓    ✓    ✓    ✓    ✓
Mechanic X3       ✓    ✗    ✓    ✓    ✓    ✗    ✓    ✓    ✓    ✓    ← R-fail + BU-fail
                                                                       → finding
```

Findings logged per §5.

### §2.4 The discipline: don't skip the checkpoints

Skipped checkpoints lead to compounding error. The FUSE sim missed:
- T13 passive Accord recovery (S-fail: didn't apply phases.md Step 4c)
- Treaty-pair Strain decay (S-fail: didn't apply peninsular_strain §4.2)
- IP advancement formula (E-fail: used wrong/no formula)

Each unchecked checkpoint cascaded into 6-8 seasons of incorrect state. **The NRSE check is mandatory at every step**, not optional.

---

## §3 — FINDING TAXONOMY

### §3.1 The 7 finding types

| Type | Definition | Recognition signal | Resolution path |
|------|------------|-------------------|-----------------|
| **Conflict** | Two canon sources contradict on the same rule | Citing two different docs gives different answers | Identify authoritative source; mark other as superseded; propagate fix |
| **Error** | Wrong value, broken formula, or superseded rule still active in non-superseded docs | Sim outcome doesn't match canonical rule when applied; supersession register flags fire | Identify correct value; update doc; track via ED |
| **Incongruency** | Rule that contradicts Valoria's design principles (e.g., "asymmetry is in tools, not destination") | Rule favors one faction structurally without design justification | Surface to Jordan; may be intentional or design defect |
| **Bad gameplay** | Mechanic produces unfun, grindy, unintuitive, or counterproductive play | P(success) ≤ 10% on routine actions; player has no meaningful choice; outcomes feel random | Redesign mechanic; usually involves rebalancing Ob, pool, or cost |
| **Excessive crunch** | Complex mechanic without proportional design value | Multiple sub-rules, edge cases, tracking burden that doesn't add depth | Simplify or fold into existing system |
| **Unnecessary system** | Mechanic could be fully expressed via existing systems | Two systems doing 80%+ overlapping work | Fold one into the other; deprecate redundant |
| **Missing mechanic** | Canon silent on a rule the simulation needs | Cannot find canonical answer after granular search across silos | Open ED; if Jordan ratifies, draft canon text |

### §3.2 Severity classification

| Severity | Definition | Examples from this session |
|----------|------------|---------------------------|
| **P1** | Blocking: sim cannot proceed correctly | ED-743 superseded phases.md Step 4e not propagated; mass_battle path wrong |
| **P2** | Significant: sim accuracy degraded but proceeds | Passive Accord recovery missing; Treaty-pair Strain decay missing |
| **P3** | Minor: clarification or efficiency improvement | Pool formula wording ambiguous |

### §3.3 Boundary cases

- A "bad gameplay" finding may also be an "incongruency" if the bad gameplay violates a design principle.
- A "conflict" between two docs may be resolved by clarifying which is authoritative (often the more recent ED).
- A "missing mechanic" sometimes turns out to exist elsewhere — always do granular search first.

---

## §4 — INNOVATION LICENSE

### §4.1 When to innovate

Innovation is permitted when:
1. The simulation requires a mechanic that does not exist in canon
2. Granular search across **all relevant silos** (Silos 1-15) returned nothing
3. **Cross-references checked:** mechanical_terms_index, canonical_sources.yaml, glossary.md, alias_registry.md, deprecated_registry — all confirm gap

### §4.2 Granular search procedure

Before innovating, verify gap:
1. Search canonical_sources.yaml for keyword in design doc filenames
2. Search mechanical_terms_index.md for the term and adjacent concepts
3. Search across all params/ files (cd params; grep -ri "keyword")
4. Search across all designs/ files
5. Check supersession_register.yaml for archived versions of the concept
6. Check glossary.md and alias_registry.md for naming variants

If 5/5 returns nothing, gap is real. Innovate.

### §4.3 Innovation proposal format

```yaml
innovation_proposal:
  id: INNOV-NNN
  date: 2026-MM-DD
  archetype: A_x
  problem: |
    <one paragraph: what does the simulation need to resolve?>
  searched: |
    <list of 5+ files checked, confirming gap>
  proposal:
    mechanic_name: <canonical name>
    spec: |
      <full mechanical specification>
    parameters:
      - <names, ranges, computations>
    integration:
      - <how it connects to existing mechanics>
  nrse_analysis:
    N: <does removing this worsen game? evidence>
    R: <does this allow strategy/customization/emergence?>
    S: <does this integrate cleanly with adjacent mechanics?>
    E: <is this logically simple, intuitable?>
  all_directions_check:
    top_down: <how it fits victory condition flow>
    bottom_up: <how it scales up from personal scene>
    vertical: <scale transition behavior>
    diagonal: <cross-silo interactions>
    lateral: <consistency across factions>
    horizontal: <timing/sequence>
  affected_docs:
    - <path1>: <what changes>
    - <path2>: <what changes>
  ed_opened: ED-NNN
  ratification_status: pending|ratified|rejected
```

### §4.4 Innovation flagging in sim output

Every innovation in active simulation must be flagged:
- In-text: `[INNOVATION-PROPOSAL ED-NNN]` at first use
- In rolls: explicit notation that the resolution uses a proposed-not-ratified mechanic
- Findings log entry as `type: innovation`
- Coverage matrix: mark mechanic as `🔧` (proposed) not `✓` until ratified

### §4.5 Rejection handling

If Jordan rejects an innovation:
- Mark ED as `rejected` with reason
- Sim output that used the rejected proposal needs annotation: "this season's outcome conditional on INNOV-NNN; if rejected, revise"
- Coverage matrix: remove the `🔧` mark

---

## §5 — LOGGING FORMAT

### §5.1 Per-finding entry (YAML)

```yaml
finding:
  id: F-NNN
  severity: P1|P2|P3
  type: conflict|error|incongruency|bad_gameplay|excessive_crunch|unnecessary|missing|innovation
  archetype: A1-A9
  session_id: 2026-MM-DD-archetype
  step: Y_x-S_y | Phase_z | NRSE-checkpoint-N
  description: <one sentence>
  evidence:
    - canon_ref: <file_path>:<section>
      text: |
        <verbatim quote>
    - canon_ref: <file_path>:<section>  # for conflicts, multiple refs
      text: |
        <verbatim quote>
  affected_silos: [N, M]  # Silos 1-16 per mechanical_terms_index
  affected_directions: [td, bu, v, d, l, h]  # which of 6 directions
  nrse_failures: [N, R, S, E]  # which NRSE criteria failed
  proposed_resolution: |
    <text describing fix>
  affected_docs:
    - <file_path>: <what changes>
  ed_opened: ED-NNN
  status: open|resolved|propagated|closed
```

### §5.2 Per-session log entry

At session close, append to session_log_current.md:

```markdown
## Session 2026-MM-DD — Archetype A_x simulation

**Outcome:** <summary>
**Duration (sim seasons):** <N>
**Deliverable:** /mnt/user-data/outputs/<filename>.md (<N> lines)

### Findings count
- P1: <N>
- P2: <N>
- P3: <N>

### EDs opened
- ED-NNN: <one-line description>
- ED-NNN: <one-line description>

### EDs resolved this session
- ED-NNN: <resolution>

### EDs propagated (commits)
- ED-NNN → <files updated>
- Commit hash: <hash>

### Coverage matrix delta
- Silos newly at ✓✓: [N]
- Silos advanced from — to ✓: [M]
- Overall coverage: X% → Y%

### Carry-forward for next session
- <items to address>

### Innovations proposed
- INNOV-NNN: <description> [pending ratification]

### Risks surfaced
- <items>
```

### §5.3 Session log file management

- One `session_log_current.md` at canon root, replaced each session
- Previous logs archived to `deprecated/archives/session/session_log_archive_YYYY-MM.yaml`
- `g.safe_session_close(new_log, bootstrap_log)` handles this

---

## §6 — PER-ARCHETYPE WORKPLANS

### §6.1 A1 FUSE (Year 3-7 extension)

**Status:** Y1-Y2 done in this session. Y3-Y7 compressed; needs granular treatment.

**Pre-sim canon to pull (additional to base 28):**
- `designs/scene/social_contest_v30.md`
- `designs/scene/conviction_track_v30.md`

**NRSE-prep targets (mechanics to exercise in Y3-Y7):**
- Conviction Transformed state (C1 Transforms — verify Renown +1 grant per ED-793)
- Cardinal Renborg loyalist remnant (continued antagonism after primary fuse averted)
- Tributary treaty negotiation Crown ↔ Hafenmark (test ED-791 propagation; full Phase 1/2/3 procedure)
- Settlement adjacency: travel to T7 / T17 / T10 for governance work
- Standing 4 → 5 transition (Hafenmark Senior → Inner Circle, +2 scene actions)
- Renown 10 cap interactions (Grand Contest at any time)
- Long-form NPC arc completion (Yrsa Vossen → Cultural Uprising signal at T9)
- Warden Recognition for Varfell as background event (NOT primary subject)

**NRSE checkpoints:**
- #0 (prep): verify ED-793 Renown grant for Transformed state is logically applied; identify if Conviction state grants have edge cases (e.g., what if Conviction Transformed multiple times across same Conviction?)
- #1 (setup): Margarete's TS 10 + Coherence 10 starting state; verify Y3 carry-forward state matches Y2-end exactly
- #2 (Y3 audit): combat #2 vs Cardinal-aligned Templar — verify combat pool composition includes any TS-developed History
- #3 (Y4 audit): Almud abdication scene — verify Crown succession mechanics align with Torben Loyalty track
- #4 (Y5-Y7 audit): Hafenmark Tributary arrangement — verify ED-791 propagation works in practice
- #5 (final): victory check at S40+ for Peninsular Sovereignty conditions

**Likely findings:** ~3-5 EDs. Mostly minor (procedural details on Tributary, Conviction multiple-transformation handling, late-Renown effects).

### §6.2 A2 TOTAL WAR (priority #1 next)

**Status:** Not built. Highest mechanical gap (Silo 10 at ~5%).

**Pre-sim canon to pull:**
- `designs/provincial/mass_battle_v30.md` (60,996 bytes) — primary
- `designs/territory/march_layer_v30.md` — march/A* mechanics
- `params/mass_combat.md`
- `designs/provincial/military_layer_v30.md` (verify path)
- `params/bg/military.md`

**Setup:**
- PC: Hafenmark colonel (assigned to Baralta's command at T8 Gransol)
- Stats: Cog 4 / Cha 3 / Str 4 / End 4 / Agi 4 / Att 3 / Bon 3 (warrior leader build)
- Histories: Tactics 3, Sword 2
- Convictions: Hafenmark's military doctrine, comradeship, peninsula vs Altonia
- Scenario: Crown declares war on Hafenmark over T8 secession movement. 4-6 mass battles across T2-T8 frontier. Siege of T8 Gransol.
- 15+ named NPCs from Crown, Hafenmark, Löwenritter, Varfell observer

**NRSE checkpoints:**
- #0 (prep): verify Mass Battle scale classification (Skirmish/Campaign/War per §A.3). Verify Battle Pool construction formula.
- #1 (setup): PC stat sheet matches canonical character creation rules
- #2 (Y1 — opening campaign): first standard battle (T2 frontier) — exercise Cascade Phase 1-6, Casualty rolls, Wound resolution
- #3 (Y1 — Mass Battle): T8 siege initiation — Mass Battle scale, MS −2 cost, Fort level effects, Bypass rule
- #4 (Y2 — sustained war): March layer (march budget = Mil÷2 edges; A* pathfinding through hostile territory; vision/recon)
- #5 (Y2 — Officer Capture event): exercise ED-334/335 capture mechanics, ransom valuation
- #6 (Y3 — naval support): coastal edges via Port (S-002 Riverside), naval mechanics
- #7 (post-war): Post-Battle Consequence Scenes, BG→TTRPG handoff

**Predicted findings (likely 8-12 EDs):**
- Mass Battle retreat conditions specifics
- Captured general ransom valuation formula
- Siege duration formula (Fort levels vs Mil deltas vs supply)
- Naval combat specifics (Port-to-Port mechanics)
- March budget computation edge cases (e.g., does carrying baggage cost movement?)
- Vision/recon specifics in fog of war
- Bypass rule edge cases (can army bypass a Fort 3 settlement?)
- Levy Restriction interaction with sustained war
- Campaign Supply mechanics

**Innovation candidates if canon silent:**
- Cavalry vs infantry differential (mentioned in stats but advancement unclear)
- Battle Tempo / pacing rules across multi-battle campaigns
- Field hospital / Wound recovery rate during sustained war

**Coverage matrix delta (predicted):**
- Silo 10 (Mass Battle): ~5% → ~70% (deep coverage)
- Silo 3 (Territory): adjacency exercised extensively
- Silo 5 (Combat): personal scenes exercise high-stress combat
- Silo 12 (Clocks): MS drift acceleration tracked

### §6.3 A3 THE SCHISM

**Pre-sim canon:**
- `designs/provincial/ci_political_v30.md`
- `params/bg/ci_seizure.md` (already in base)
- `params/bg/institutions.md`
- `params/bg/ministry.md`
- Whatever Reformed Settlement spec exists (search needed)

**Setup:**
- PC: Senior Solmund cleric, likely a Bishop of one of the 4 Cardinal aspects (Justice or Prudence most contested)
- Stats: Cog 5 / Att 5 / Cha 4 / Spi 3 (theologically engaged)
- Histories: Theology 3, Rhetoric 2
- Convictions: doctrinal fidelity, institutional reform vs schism, the soul of the Church
- Scenario: Post-FUSE. Cardinal Renborg's hardliners go underground; Inquisitor Haelgrund destabilized; PC must navigate institutional fracture
- 15+ NPCs: all 4 Cardinals, Haelgrund, Bishops, junior clerics, heretical movement leaders

**NRSE checkpoints:**
- #0 (prep): verify CI generation formula per seasonal calc; verify Mass Seizure probability P(declare) = ((CI-60)/40)^3.3
- #1 (setup): PC stat sheet + Standing 3 (Bishop) in Church + Disposition tracking with 4 Cardinals
- #2 (Y1 — CI climbing): Piety Spread + Active Inquisition + Cardinal Focus actions; AP threshold tracking (3 / 6 for Inquisitor deployment)
- #3 (Y2 — Schism trigger): Cardinal Renborg's Schism (or successor's); schisming Cardinal ignores Focus; CI dynamics shift
- #4 (Y3 — Excommunication Tribunal): exercise chain contest mechanics
- #5 (Y4 — Mass Seizure attempt): formal Seizure declaration at CI 65+; probability roll; Battle component if garrisoned territory
- #6 (Y5 — Reformed Settlement): if CI ≥ 40, Reformed Settlement option opens
- #7 (final): victory path — Church territorial consolidation OR Hollow Victory (Church+Hafenmark)

**Predicted findings (10-15 EDs):**
- Cardinal defection mechanics (Cardinal joins another faction or splits Church)
- Bishop appointment post-Cardinal collapse
- Reformed Settlement procedural details (votes, conditions, effects)
- Schismed Cardinal stats and AI
- Heresy investigation Evidence Track procedures
- Templar deployment under Schism conditions
- Inquisitor career arc and replacement when killed/excommunicated
- Settlement infrastructure 4-axis Church model (Chapel/Church/Cathedral/Seminary)
- Mass Seizure Battle component edge cases
- Theocratic Bid phase if CI 100 reached

### §6.4 A4 WARDEN AWAKENING

**Pre-sim canon:**
- `params/southernmost.md` (already in base — verify)
- Whatever RM (Restoration Movement) spec exists
- `canon/01_foundations_amendment_self_rendering.md`
- `canon/02_foundations_amendment_leap_mechanism.md`
- Edeyja-specific docs (search needed)

**Setup:**
- PC: Vaynard (Varfell Duke, practitioner TS 35, Spi 4, Att 4, Cog 5)
- Path B commitment: Southernmost Dominion
- Convictions: substrate stewardship, Varfell duty, the Mending crisis
- 15+ NPCs: Edeyja (TS 75-80), Wardens, RM cell leaders (Vossen, Hann), Threadcut beings encountered, Calamity-affected settlement residents

**NRSE checkpoints:**
- #0 (prep): verify WR advancement rule (per ED-795 now propagated); verify Forgetting Check resistance (TS 29); verify RM Emergence triple condition
- #1 (setup): Vaynard's starting WR (probably 0); first Expedition rolls
- #2 (Y1 — Expeditions to T15): Expedition seasons advance WR; encounter cosmological events (Shifting Objects, Gaps, Folklore)
- #3 (Y2 — Calamity Radiation): MS bands trigger effects per Proximity; PC and settlement effects
- #4 (Y3 — RM Emergence): triple condition (WA ≤ −2 + 3 territories PT ≤ 1 + MS ≤ 50) checked; if met, RM emerges as latent faction
- #5 (Y4 — Edeyja contact): Overwhelming Forgetting Check at TS 50+; conversation scene
- #6 (Y5 — coordinated Mending): MS recovery via Warden cooperation (WC track advances)
- #7 (final): Path B victory check — PV ≥ 8, T4+T13 held, WR ≥ 3, Season ≥ 12

**Predicted findings (10-15 EDs):**
- Edeyja interaction protocol (what specifically does the scene look like?)
- Threadcut being stat blocks
- RM Active stats specifics post-Emergence
- Calamity event probability formula (currently no canonical rate)
- Shifting Objects / Gaps / Folklore event resolution mechanics
- Southernmost Surge mechanics
- Forgetting Check effects on TS < 29 practitioners (specific outcomes)
- WC ≥ 1 / 2 / 3 effects integration with normal seasonal Mending
- Warden NPC AI (post-Emergence)
- De-Actualisation procedure

### §6.5 A5 DIPLOMATIC CASCADE

**Pre-sim canon:**
- `designs/provincial/faction_layer_v30.md` (already in base — full read needed)
- Treaty Phase docs if separate
- `params/bg/ed_resolutions.md`

**Setup:**
- PC: Brigitte (Crown, post-FUSE Year 8) OR a Hafenmark/Varfell diplomat
- Stats: Cha 5 / Cog 4 / Att 4 / Bon 4 (diplomatic build)
- Histories: Law 3, Rhetoric 2
- Scenario: Cascade of treaty negotiations across 4 factions + Schoenland diplomatic exchange (Elske retrieval)
- 15+ NPCs: All faction heads, plus Elske, Doux Alexios Laskaris, Hjalmar Strand (loyal Crown emissary)

**NRSE checkpoints:**
- #0 (prep): verify all 6 treaty types' Stability deltas + Accord-on-cession rules per faction_layer §3 (post-ED-791/792 propagation)
- #1 (setup): existing treaty relationships at start
- #2 (Y1 — Tributary negotiation Hafenmark→Crown): Phase 1 Influence Ob 2 / Phase 3 Mandate Ob 2 / Wealth flow established
- #3 (Y2 — Alliance Crown↔Varfell): test Alliance qualification for §6.1 hegemony (per faction_layer §3)
- #4 (Y2 — Commercial Crown↔Guilds): trade rights, multi-faction effects
- #5 (Y3 — Schoenland Elske retrieval): Crown/Löwenritter Senator Outward in T4, Elske Loyalty advances to 6+, retrieval Military vs Ob 2
- #6 (Y4 — Open Pledge breach): test PP-515 mechanics; Pledge breached → Stability −1 + Casus Belli to all witnesses
- #7 (Y5 — Coalition collapse cascade): one treaty breaks, others test
- #8 (final): hegemony achieved via Treaty-bound + Submitted + Institutional Dominance

**Predicted findings (8-12 EDs):**
- Treaty Phase 2 Concession value formulas (territory ≤ what value of indemnity?)
- Guarantor option invocation mechanics
- Sovereign Authority Doctrine specifics (once per campaign — when exactly?)
- Treaty breach cascade across multiple co-signatories
- Diplomatic Token usage timing (PP-517 — sim earlier had wrong number)
- Schoenland naval mechanics if Elske retrieval requires sea route
- Crown Treaty interaction with non-Crown faction-layer treaties

### §6.6 A6 DEEP THREADWORK

**Pre-sim canon:**
- All `designs/threadwork/` files
- `params/threadwork.md` (already in base — full read)
- `canon/01_foundations_amendment_self_rendering.md`
- `canon/02_foundations_amendment_leap_mechanism.md`
- Threadcut being docs

**Setup:**
- PC: Aldric Hann (RM operations leader, Cog 4 / Cha 4 / Bon 4, TS 35+, Coherence 8)
- High-TS practitioner exercising full operation suite
- Scenario: Knot rupture cascade. RM cell coordinated operations against Church territory. Contested Intentionality scenes against Varfell practitioners. Co-Movement card draws.

**NRSE checkpoints:**
- #0 (prep): verify Operation Risk Taxonomy (Restorative/Manipulative/Destructive); verify FR (Forced Resolution) mechanics
- #1 (setup): Aldric's stat sheet, Coherence track, Thread Tension baseline
- #2 (Y1 — Pulling operations): test scale gates (Object/Personal at TS 30+; Relational at 50+)
- #3 (Y2 — Locking + Dissolution): contested ops with another practitioner (Maret Uln)
- #4 (Y3 — Knot rupture): cascade through PC's social network; Conviction Scars on NPCs
- #5 (Y4 — Threadcut being encounter): social fieldwork with Threadcut being; epistemological strain
- #6 (Y5 — Forced Resolution): high-stakes Op forces FR; Dissolution Residue tracked
- #7 (final): Coherence track stress test — does PC reach Crisis (Coherence ≤ 2)?

**Predicted findings (12-18 EDs):**
- High-TS scale gate enforcement edge cases (what happens at exactly TS 50?)
- Co-Movement card draws specifics (P-01 compliance)
- FR vs FR Both-Fail Scaling formula
- Knot rupture cascade depth cap
- Threadcut being stat blocks (likely missing from canon)
- Sustained Opposition mechanics across multiple seasons
- Thread Domain Echo (ED-673) integration specifics
- Coherence 0 outcome scenarios
- Thread Resonance markers in Phase 5 clearing
- Thread Debt token decay specifics

### §6.7 A7 ANARCHY DESCENT

**Pre-sim canon:**
- `params/bg/stress_patches.md`
- `params/bg/tracks.md`
- World-State Transition docs (search)

**Setup:**
- PC: post-FUSE alternate where assassination succeeded (Lenneth died)
- Scenario: Almud paranoia → Emergency Powers → PI drops → multiple Tension Cards fire → IP climbs → MS drops → RM emerges → cascade
- 15+ NPCs: most surviving roster, with multiple Conviction Scars and Belief Revisions

**NRSE checkpoints:**
- #0 (prep): verify each World-State Transition trigger (Occupation, Anarchy, Post-Calamity)
- #1 (Y1 — Lenneth death aftermath): Crown stability collapse cascade; Torben Loyalty plummet
- #2 (Y2 — Emergency Powers): Crown L damage; PI dropping below 2; Hafenmark Parliamentary Manoeuvre disabled
- #3 (Y3 — IP climbing): test ED-743 IP formula AND new ED for IP 80 skirmishes / IP 100 invasion (per Jordan note); Altonian Vanguard appearance
- #4 (Y4 — Occupation Era triggered): IP ≥ 100 + Altonian diplomacy ≤ 1 → Governorate; faction action Ob +2 in occupied territories
- #5 (Y5 — MS approaching 0): Post-Calamity Era trigger imminent
- #6 (Y6 — Anarchy Era): all factions Stability 0; direct personal governance; founded Organization option
- #7 (Y7-10 — recovery or terminal): Parliament quorum restored vs Second Calamity at MS ≤ 5 sustained

**Predicted findings (10-15 EDs):**
- World-State Transition exact triggers (verified ED-799 IP 80 skirmishes)
- Rupture Scene procedure
- Pastoral Assumption mechanics
- Faction-collapse Stability dynamics in detail
- Multiple-faction Submission cascade
- Emergency Powers full mechanics (CI +1, etc.)
- Anarchy Era founded Organization mechanics
- Altonian Vanguard stats and AI in active invasion
- Second Calamity threshold and terminal conditions

### §6.8 A8 GENERATIONAL deep

**Pre-sim canon:**
- `designs/architecture/generational_transition_v30.md` (already in base)
- `params/factions_personal.md`
- Companion mechanics docs (search)

**Setup:**
- 3-character lineage across 60+ seasons
- Char 1: dies in combat (Death pathway)
- Char 2: Portrait Retirement after 3 Convictions Fulfilled
- Char 3: inherits city-state from collapse, rebuilds

**NRSE checkpoints:**
- #0 (prep): verify Generational Transition categories (PRESERVE/TRANSFORM/RESET/BREAK/TRANSFER)
- #1 (Char 1 Y1-5 — building): Companion formation (Bonds ≥ 5)
- #2 (Char 1 death — sudden): test Death pathway vs Retirement; what transfers, what resets
- #3 (Char 2 setup): Renown inheritance (+1 if predecessor ≥ 7)
- #4 (Char 2 Y6-12 — building): Conviction arcs lead to 3 Fulfilled
- #5 (Char 2 Portrait Retirement S12): Lineage Acts (Mentorship/Succession/Thread Legacy)
- #6 (Char 3 setup): faction collapse scenario; inherits city-state with partial stats
- #7 (Char 3 Y13-25 — rebuilding): Stage 2→3→4→5 emergence pathway from city-state recovery

**Predicted findings (8-12 EDs):**
- Companion stat block specifics
- Age track effects (Long Campaign mechanics)
- Inspiration economy precise mechanics (ED-779 reference)
- Character creation full integration (Caste + Initiation)
- History point cap by Recall specifics
- Death pathway differential from Portrait (resources, transfers)
- Multiple Portrait Retirements stacking effects
- City-state collapse mechanics specifics

### §6.9 A9 STEADY SEASON

**Pre-sim canon:**
- Base 28 files sufficient

**Setup:**
- PC continuing during stable peninsula stretch (post-Y10 of any campaign where Peninsular Sovereignty achieved)
- Routine play: regular Govern cycles, Connect rolls, no crisis events
- Test card-hand economy, Cooldown Track, Take-a-Breath

**NRSE checkpoints:**
- #0 (prep): verify Phase 4 priority order; verify Cooldown Track mechanics; verify Card Renewal
- #1 (Y1 — steady operations): regular Govern rolls; Trade; routine Senator action
- #2 (Y2 — Cooldown Track exercise): cards advancing through slots; returning to hand at 0
- #3 (Y3 — Take-a-Breath in non-combat contexts): Stamina recovery formula (End+History)×2
- #4 (Y4 — Read action for new NPCs): Disposition initialization mechanics
- #5 (Y5 — Sincerity Gate test): Spirit roll for trust events
- #6 (final): does routine play produce engagement? Or is it grindy?

**Predicted findings (5-8 EDs, plus engagement assessment):**
- Card Renewal specifics
- Cooldown Track edge cases
- Pool Floor 1D minimum enforcement
- Sincerity Gate Ob and pool composition
- Steady-state Renown trickle (does Renown actually advance during quiet seasons?)
- Disposition decay rules without Knot
- **Engagement / bad-gameplay assessment:** is steady-state play actually engaging? If grindy, propose pacing fixes.

---

## §7 — COVERAGE MATRIX INTEGRATION

### §7.1 Live tracking

After each sim, update `coverage_matrix.md`:
- Each silo: mark mechanics moved from `—` to `✓` to `✓✓`
- Overall coverage %: recompute per silo
- Sequence of next archetypes: adjust based on remaining gaps

### §7.2 Archetype → silo mapping (per coverage_matrix.md §2)

Current depth after A1 FUSE (Y1-Y2 only):
- Silo 1 (character): ~35% deep
- Silo 5 (combat): ~40%
- Silo 6 (social contest): ~50%
- Silo 8 (fieldwork): ~50%
- Silo 12 (clocks): ~60%
- Silo 13 (tensions deck): ~10% (1 of 12 cards)
- Other silos: 5-30%

Target after all 9 archetypes:
- All silos: 70%+ deep
- Tensions deck: 80%+ (most cards exercised)
- Silo 10 (mass battle): 90% (A2 dominates this)
- Silo 9 (Piety/CI): 90% (A3 dominates)

### §7.3 Coverage matrix update protocol

After each session:
1. List mechanics exercised in session (with specific sub-rule depth)
2. Update silo cells in coverage_matrix.md
3. Recompute silo percentage
4. Commit updated matrix in same batch as session log

---

## §8 — PROPAGATION PIPELINE

### §8.1 Three-stage propagation (per session)

**Stage 1: Open EDs** (Commit 1, editorial scope)
- All findings of any severity get ED entries
- Status: `open`
- Severity per §3.2
- Commit message: `[editorial] sim A_x findings — ED-NNN..MMM`

**Stage 2: Resolve in-session if possible** (Commit 2, editorial scope)
- EDs that have clear canonical answer (cross-reference solves them) → resolved in same session
- EDs that need Jordan input → flagged `jordan_decision: pending` until response
- Commit message: `[editorial] sim A_x resolutions — ED-NNN..MMM`

**Stage 3: Propagate to design docs** (Commit 3, editorial scope)
- All `status: resolved` EDs get text edits to affected design docs
- Update canonical_sources.yaml SHA hashes
- Mark EDs `status: closed` with closure_commit reference
- Commit message: `[editorial] sim A_x propagation — close ED-NNN..MMM`

### §8.2 Conflict-prevention rule (lesson from this session)

**Before resolving any ED:**
1. Pull ALL design docs related to the ED's topic
2. Grep for keywords in those docs
3. If existing canon already specifies a rule — ALIGN with it, don't overwrite
4. Existing canon is authoritative; the new ED becomes cross-reference
5. If genuinely no existing canon (after granular search), proceed with innovation per §4

**Verified during this session:** ED-791 and ED-792 had to be revised at propagation time because the proposed resolutions contradicted pre-existing faction_layer §3 canon. The revised propagation aligned with existing canon — this was correct. Don't repeat the conflict pattern.

### §8.3 Co-file rules (hook-enforced)

Per session, design doc edits MUST include:
- `references/canonical_sources.yaml` with updated SHA hashes for edited docs
- `canon/editorial_ledger.yaml` with ED status updates
- `canon/editorial_ledger_summary.yaml` with counts

Hook will block commits that violate co-file rules. SHA computation:
```python
def git_blob_sha(content_str):
    content_bytes = content_str.encode('utf-8')
    header = f"blob {len(content_bytes)}\0".encode()
    return hashlib.sha1(header + content_bytes).hexdigest()
```
(After encode, `len(content_bytes)` is byte count — correct.)

### §8.4 Supersession register checks

Some commits trigger supersession register warnings (HOOK ⚠ SUPERSESSION). Three categories:
1. **Regression risk** — the commit might un-do a superseded rule. Verify carefully.
2. **Cross-reference update** — the commit appropriately updates the active canonical version. Fine.
3. **Noise** — the file is touched but the superseded rule isn't affected. Ignore.

Always log supersession warnings in session log for Jordan review.

---

## §9 — SESSION SEQUENCE & DEPENDENCIES

### §9.1 Suggested order

| Session | Archetype/Type | Key dependencies | Rationale |
|---------|----------------|------------------|-----------|
| 1 | A2 TOTAL WAR | None | Largest mechanical gap (Silo 10) |
| 2 | A3 SCHISM | A2 (Mass Seizure may include Battle) | High mechanical density, builds on A2 battle mechanics |
| 3 | **Propagation** | A2+A3 EDs | Clear accumulated findings |
| 4 | A6 DEEP THREADWORK | None | High-density practitioner mechanics |
| 5 | A4 WARDEN AWAKENING | A6 (high-TS work) | Cosmological layer; relies on Thread foundation |
| 6 | **Propagation** | A6+A4 EDs | Clear accumulated findings |
| 7 | A5 DIPLOMATIC CASCADE | A2 (Casus Belli, war aftermath) | Treaty mechanics in post-war context |
| 8 | A7 ANARCHY DESCENT | A2, A3 (cascade triggers) | Endgame mechanics; needs prior crisis context |
| 9 | **Propagation** | A5+A7 EDs | Clear accumulated findings |
| 10 | A8 GENERATIONAL deep | Most others (long campaign needs varied scenarios) | Lifecycle test |
| 11 | A9 STEADY SEASON | A8 (routine play within long campaign context) | Engagement assessment |
| 12 | A1 FUSE extension | Builds on existing FUSE Y1-2 | Wrap up A1 archetype |
| 13 | **Final propagation** | All accumulated EDs | Close out |
| 14 | Coverage matrix close-out | All sessions | Summary deliverable |

### §9.2 Cross-archetype dependencies

- **A2 outputs feed A3, A5, A7:** mass battle context, Casus Belli triggers, faction stat damage
- **A6 outputs feed A4:** practitioner mechanics, scale gates, Coherence dynamics
- **A2+A3 outputs feed A7:** crisis cascade conditions, faction Stability damage history

Where possible, carry state forward from prior sims (e.g., A2 ends with Crown-Hafenmark war damage; A5 picks up post-war treaty negotiations using those damaged factions).

### §9.3 Innovation ratification interspersion

After every 2-3 sim sessions, dedicate brief time to:
- Present accumulated innovations to Jordan
- Get ratification decisions
- Update EDs accordingly

Don't let innovations pile up unratified — they block downstream sims that depend on the proposed mechanic.

---

## §10 — RISK REGISTER

| Risk | Mitigation |
|------|------------|
| **Context budget exhaustion mid-sim** | Compress Y3+ if context >75%; produce handoff for next session; never sacrifice Y1-Y2 granularity |
| **Canon conflicts surfaced too late** | NRSE-checkpoint #0 (prep) explicitly checks for known canon conflicts before sim starts |
| **Innovation drift from canon** | All innovations flagged `[INNOVATION-PROPOSAL ED-NNN]` and tracked separately; Jordan ratifies before canon integration |
| **Coverage matrix drift** | Update matrix after EVERY session (Stage 3 of propagation pipeline) |
| **Hook failures blocking propagation** | Pre-flight check: verify `task_gate('editorial')`, `safe_commit` signature, co-file inclusion before issuing commit |
| **Forbidden token slip (Galbados)** | Grep all deliverables before claiming done; hook also enforces |
| **Session log corruption** | Use `g.safe_session_close()` not manual write; check for "stale" status block on next bootstrap |
| **Supersession regression** | All supersession ⚠ warnings reviewed in session log; Jordan can audit |
| **Excessive ED accumulation without propagation** | Propagation sessions interleaved every 2-3 sim sessions (per §9.1) |
| **Lost archetype context across sessions** | Each session log carries forward state explicitly; next session's pre-bootstrap reads prior log |

---

## §11 — TOOLING & PROCESS

### §11.1 Bootstrap

Per Valoria PI. Note ED-796 (open) — manual override of context_gate hard-stop acceptable until recalibration.

### §11.2 Commit hygiene

- `task_gate('simulation')` for sim-output commits (rare — sims usually deliverables, not commits)
- `task_gate('editorial')` for ED entries / canon edits
- `task_gate('infrastructure')` for hook code (ED-796 work)
- Message format: `[scope] description — PP-NNN / ED-NNN`
- Co-file: design doc changes always include canonical_sources.yaml

### §11.3 Working files

- `/home/claude/` for in-session edits (private scratch)
- `/mnt/user-data/outputs/` for deliverables to Jordan
- Repo (jordanelias/ttrpg) for canon updates only

### §11.4 Session log management

- One `session_log_current.md` at canon root
- Archive previous logs to `deprecated/archives/session/session_log_archive_YYYY-MM.yaml` at session close

---

## §12 — IMMEDIATE ACTIONS (this session close)

### §12.1 Open ED-798

**ED-798:** IP threshold clarification — Altonian invasion mechanics. Per Jordan 2026-05-10:
- IP 80+ → Altonia tests borders with skirmishes / small unit incursions (NEW; not formalized in canon)
- IP ≥ 100 → Altonia regularly invades through one or both mountain passes (peninsular_strain §6.4 says "Altonian Governorate activates" — clarify this means actual large-scale invasion, not just political occupation)
- canon currently has "IP 75 = Altonian Vanguard" (params/bg/core.md) and PROVISIONAL Altonian Vanguard Mechanics (PP-568 ED-340) — these mostly align with Jordan's note but require explicit IP 80-99 skirmish phase formalization

**Proposed text additions:**
- peninsular_strain §6.4 update: clarify Occupation Era = "regular Altonian invasion through one or both mountain passes (T10 Spartfell NE pass; second pass — verify location)"
- params/bg/core.md update: IP 75 Altonian Vanguard appears → IP 80 sustained Vanguard presence + skirmishes/small unit incursions → IP 100 large-scale invasion
- New section: Altonian Vanguard escalation ladder

**Open as ED:** P2, source "Jordan clarification 2026-05-10."

### §12.2 Commit this workplan

Commit `references/simulation_workplan_v1.md` to canon. Single file commit. Editorial scope. Doesn't trigger co-file rule (references/canonical_sources.yaml only triggered when *design docs* change).

### §12.3 Final state

After this session:
- 4-5 commits total (`639595a7`, `66b5f546`, `4272fd67`, `cf10980c`, this commit)
- 3 EDs open (ED-796, ED-797, ED-798)
- 1 ED deferred (ED-788)
- ED-799+ available for next session
- Coverage matrix: ~35-40% (A1 partial)
- Workplan committed to canon
- Handoff delivered

---

## §13 — STARTING POINT FOR NEXT SESSION

Next session: A2 TOTAL WAR.

**Pre-bootstrap reads (required):**
- `session_log_current.md` — latest session log
- `canon/editorial_ledger_summary.yaml` — open EDs (ED-796, 797, 798 at minimum)
- `references/simulation_workplan_v1.md` — this document
- `coverage_matrix.md` — current coverage state
- `handoff_running_simulations.md` — corrected version

**First steps:**
1. Bootstrap per Valoria PI
2. Confirm 3 EDs open: ED-796, ED-797, ED-798
3. Read §6.2 A2 workplan above
4. Pull canon batch (28 base + 5 archetype-specific)
5. NRSE-checkpoint #0 (prep review)
6. Begin setup

**Expected duration:** 1 full session for A2 sim Y1-Y2 granular + Y3-Y7 compressed; ~25-35k char deliverable; ~8-12 EDs surfaced; followed by Stage 1 ED commit.

---

## §14 — CHANGELOG

| Version | Date | Notes |
|---------|------|-------|
| v1 | 2026-05-10 | Initial workplan. Author: Claude this session. Status: committed `references/simulation_workplan_v1.md`. |

Future versions update as workplan evolves. Each version commits to canon with editorial scope.
