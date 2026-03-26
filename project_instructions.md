# VALORIA PROJECT INSTRUCTIONS

## For All Sessions — Read First

### What This Project Is
Valoria is a tabletop roleplaying game / board game / hybrid playable in all three modes. This project develops the complete ruleset, audits it against philosophical canon, stress-tests all mechanics, and compiles clean checkpoint editions.

**Architecture:** Skills live in Project Files (`/mnt/project/`). Persistent state lives on GitHub.

---

## MANDATORY MODEL ROUTING — ENFORCED ON EVERY TASK

**Before executing any task, assess minimum-viable model. This is non-negotiable.**

| Task Type | Model | Rationale |
|-----------|-------|-----------|
| Document chunking, indexing, section extraction | Haiku 4.5 | Structural; no reasoning |
| Format fixes, cross-reference insertion, table formatting | Haiku 4.5 | Mechanical transcription |
| Formula transcription from design docs to ruleset | Haiku 4.5 | Copy + format |
| Consistency repair (wrong numbers, broken refs) | Haiku 4.5 | Pattern matching |
| Mechanical gap-fill (known constraints, no ambiguity) | Sonnet 4.6 | Structured reasoning within bounds |
| Canon compliance checking | Sonnet 4.6 | Philosophical judgment |
| Stress testing / simulation | Sonnet 4.6 | Scenario reasoning |
| Mechanical audit (interaction analysis, gap detection) | Sonnet 4.6 | System-level reasoning |
| Compilation assembly (merging sources into clean doc) | Sonnet 4.6 | Judgment on integration conflicts |
| Editorial-adjacent design (faction cards, NPCs, setting) | Opus 4.6 | Creative + philosophical judgment |
| Ambiguous design intent resolution | Opus 4.6 | Deep contextual reasoning |
| Philosophy-heavy new mechanic design | Opus 4.6 | Foundations interpretation |

### Routing Protocol
1. Assess task complexity BEFORE starting.
2. If task can be done by a cheaper model: say so. Suggest user switch model or flag for batch processing at lower tier.
3. **NEVER run Haiku-tier or Sonnet-tier work on Opus.** Flag it and refuse to execute inline. Provide the task specification so the user can run it on the appropriate model.
4. When multiple sub-tasks exist, produce a routing table showing each sub-task's assigned model BEFORE executing any of them.
5. If the current model is wrong for the task, state: `[MODEL MISMATCH: this task is [Haiku/Sonnet]-tier. Switch model or confirm override.]`

### Skill Delegation — Mandatory
Skills exist to be used. Every multi-step task MUST be decomposed into skill calls. **Anti-pattern: doing skill work inline on Opus.** If the orchestrator catches itself about to do chunking, formula checking, or structural assembly inline, STOP and route to the appropriate skill + model.

| Skill | Model | When to Use |
|-------|-------|-------------|
| valoria-orchestrator | Sonnet 4.6 | Session start, workflow routing, editorial gate |
| valoria-chunker | Haiku 4.5 | Any input >500 lines |
| valoria-canon-guard | Sonnet 4.6 | Any new mechanic, any audit finding, any compilation stage |
| valoria-mechanic-audit | Sonnet 4.6 | Consistency, gap detection, formula checks |
| valoria-simulator | Sonnet 4.6 | Stress tests, edge cases, scenario simulations |
| valoria-compiler | Haiku 4.5 / Sonnet 4.6 | Assembly, patching, checkpoint export |

---

## GitHub API

**Repo:** `jordanelias/ttrpg` · branch `main`
**PAT:** {PAT from project instructions}

### Read
```
GET https://api.github.com/repos/jordanelias/ttrpg/contents/{path}
Authorization: token {PAT}
```
`content` field is base64-encoded. Decode before parsing. Capture `sha` for any write.

### Write
```
PUT https://api.github.com/repos/jordanelias/ttrpg/contents/{path}
Authorization: token {PAT}
Body: {"message": "{commit message}", "content": "{base64-encoded}", "sha": "{current sha}"}
```
Always GET before PUT. SHA not required for new files. On 409: re-GET and retry once. On failure after retry: output as fenced code block with manual paste instructions. Never silently drop state.

**Commit discipline:** Finalize files locally before pushing. One push per file per session. No revision commits.

### Document Hierarchy (Immutable)
1. **Valoria_Philosophical_Foundations.docx** — metaphysical canon; governs everything
2. **Mechanics.docx** — core mechanical principles and design intent; original edition
3. **Current ruleset checkpoint** — working document; subject to audit against 1–2

If conflict: higher-ranked document wins. Always. The ruleset header states this explicitly.

### Editorial Control
**User approves all:** setting, worldbuilding, character content, narrative, tone, faction behavior, design intent resolution, ambiguous calls.
**Claude executes without approval:** formula fixes, consistency repairs, format changes, audits, simulations.
**Flag format:** `[EDITORIAL: requires user approval — description]`

---

## Session Protocol
1. **Start:** Read `session_log_current.md` (NOT `session_log_archive.md`, NOT the deprecated `valoria_session_log.md`). Report status in ≤3 lines. Read `valoria_gap_register_consolidated.md` — P1 count only. Confirm task. **Produce model routing table before executing anything.**
2. **Work:** Execute via skill workflows. Checkpoint after each stage.
3. **End:** Replace content of `session_log_current.md` with session-close YAML. Append previous current block to `session_log_archive.md`. Update gap register if changed.
4. **Context limit:** Complete current stage → session-close → instruct new chat with handoff.

---

## Token Efficiency Rules — Non-Negotiable
- Chunk before analyzing (>500 lines → valoria-chunker first)
- Never re-read already-chunked documents within a session
- Never re-run completed stages
- Intermediate work: tables, not prose. Final outputs only as documents.
- Haiku for structural work; Sonnet for reasoning; Opus only for editorial/philosophical judgment.
- Session log: read ONLY `session_log_current.md` on resume. Never the archive.
- Finalize before committing to GitHub. No revision commits.

---

## Stress Testing & Simulation Coverage Matrix

The simulation coverage matrix tracks SEVEN dimensions. Every test scenario must be tagged across all applicable dimensions.

### Dimension 1: Mechanic (56 mechanics, M-001 through M-056)
The mechanic(s) being tested.

### Dimension 2: Game Mode
| Code | Mode |
|------|------|
| TTRPG | Tabletop RPG mode |
| BG | Board game mode |
| HYB | Hybrid mode |

Every mechanic must be tested in every mode where it applies.

### Dimension 3: Temporal Impact
| Code | Description |
|------|-------------|
| PAST | Mechanic engages with accumulated past (Histories, Memory Pull, flashbacks, institutional memory) |
| PRES | Mechanic resolves in present action (combat, skill checks, current-state operations) |
| FUT | Mechanic projects into future (clocks, countdown timers, strategic planning, trajectory) |
| CROSS | Mechanic bridges temporal modes (co-movement, TD accumulation, transformation arcs) |

### Dimension 4: Tracks & Timers Invoked
Tag every track or timer the test touches:
TT (Thread Tension), TC (Theocracy Clock), IP (Altonian Pressure), TS (Thread Sensitivity), TD (Temporal Disjunction / Coherence Degradation), INT (Intelligibility countdown), CERT (Certainty), COMP (Composure), TLK (Torben Loyalty Clock), PI (Parliament Integrity), DD (Deniability Debt), CE (Cumulative Exposure), FSTAT (any faction stat: Mandate/Influence/Wealth/Military/Intel/Stability)

### Dimension 5: Faction
Which faction(s) are involved. Every faction must appear in testing:
Crown, Church, Hafenmark, Varfell, Guilds, Niflhel, Revolution, Löwenritter, Schoenland (spoiler)

**Requirement:** Each faction must have a generic character representing it tested across all faction-relevant mechanics. This means at minimum one test per faction for: Domain Actions, faction stat changes, seasonal accounting, inter-faction interactions, and mode-specific faction operations.

### Dimension 6: Named NPCs
Every named NPC must be tested in scenarios appropriate to their unique mechanics and narrative position. Tag by name:

| NPC | Faction | Unique Mechanics to Test |
|-----|---------|--------------------------|
| Almud | Crown | Elevated TS (artefact contact), political paralysis, succession crisis trigger |
| Lenneth | Crown | Covert networks, scholarly TS acquisition, Revolution endowment |
| Torben | Crown/Altonia | Loyalty Clock, tutoring demand (IP 30), covert contact (Int Ob 3), retrieval options |
| Elske | Crown/Altonia | Conviction (Family vs Self-Determination), recruitment by multiple factions, independence paths |
| Himlensendt | Church | Devout Constraint (sincere, zero TS awareness), institutional expansion, TC driver |
| Olafsson | Church | Cardinal mechanics, Church internal politics |
| Klapp | Church | Cardinal mechanics, Church expansion, intelligence operations |
| Baralta | Hafenmark | Devout + constitutional legalist, divine authority claim vs Confessor jurisdiction |
| Vaynard | Varfell | Secret Thread knowledge pursuit, artifact collection, consequentialist pragmatism |
| Maret Uln | Varfell/Southernmost | Practitioner mechanics, Southernmost access, Revolution adjacency |
| Ehrenwall | Löwenritter | Coup trigger conditions, Martial Law, Crown loyalty assessment |

**Requirement:** Each NPC must appear in at least one scenario that tests their unique mechanics in relation to their faction. Additionally, test each NPC in at least one cross-faction interaction scenario (e.g., Ehrenwall assessing Almud's compromises → coup threshold; Baralta confronting Himlensendt on jurisdiction; Vaynard's secret knowledge discovery by Inquisitors).

### Dimension 7: Character Archetype
| Archetype | Description |
|-----------|-------------|
| Practitioner | TS-active, performs Thread operations |
| Faction Leader | Controls faction stats via Domain Actions |
| Inquisitor | CE accumulation, investigation procedure, TS risk |
| Riskbreaker | Deniability Debt, covert operations |
| Löwenritter Knight | Military specialist, institutional loyalty |
| Knight Templar | Church military, Devout Constraint |
| Devout Character | TS-blocked, Dissonance Marks |
| Non-TS Scholar | Research-based, no Thread perception |

### Coverage Matrix Format
```
| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
```

### Coverage Requirements (Phase 3 gate)
Before any compilation is considered complete, the matrix must show:
- Every mechanic (M-001–M-056) tested in at least Isolation + Interaction
- Every game mode (TTRPG/BG/HYB) covered for every applicable mechanic
- Every faction tested with a generic character in faction-relevant mechanics
- Every named NPC tested in their unique-mechanic scenarios
- Every archetype tested in archetype-defining mechanics
- Every track tested at: starting value, mid-range, threshold crossing, and terminal value
- Zero untested P1 interactions (cross-referenced from mechanic-audit Mode C dependency graph)

---

## Persistent Files (GitHub)

| File | Location | Purpose |
|------|----------|---------|
| `session_log_current.md` | root | Latest session state — READ THIS ON RESUME |
| `session_log_archive.md` | root | Historical record — DO NOT read on resume |
| `valoria_gap_register_consolidated.md` | root | Open issues (P1/P2/P3) |
| `valoria_comprehensive_workplan.md` | root | 5-phase workplan |
| `canon/canon_constraints.md` | canon/ | 14 philosophical constraints |
| `canon/valoria_canonical_timeline.md` | canon/ | Canonical setting chronology |
| `designs/` | designs/ | Phase 1 batch design files |
| `compilation/` | compilation/ | Phase 2 compilation stages |
| `skills/` | skills/ | Canonical skill definitions |
| `tests/` | tests/ | Simulation outputs and coverage matrix |

---

## 14 Canon Constraints (Quick Reference)
P-01 Inseparability (co-movement mandatory) · P-02 Ein Sof = fullness · P-03 Rendering = consciousness · P-04 Monstrosity ≠ moral · P-05 Three modes distinct · P-06 Threadcut = is without becoming · P-07 Calamity = rendered-side · P-08 Barrier = inaccessibility · P-09 Memory pull = messy · P-10 Epistemic seduction = perceptual shift · P-11 TD universal · P-12 Relational contagion · P-13 Forgetting = rendering failure · P-14 All modes express inseparability

---

## Current Status
**Phase:** 2 (Compilation) — Phase 1 Design complete (38/38 gaps resolved)
**Compilation progress:** 2/28 stages (core engine, characters)
**Gap Register:** 108 items (consolidated)
**Simulation Coverage:** 0/56 mechanics tested (Phase 3)
**Editorial Pending:** Territory names, Varfell victory tuning, 10 seasonal event cards, Restoration NPCs, Niflhel primus inter pares, Varfell Private Collection transfer, E-01 (assassination perpetrator), E-03 (AG calendar name)
