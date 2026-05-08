# Unified Character Generation via Choice-Based Questionnaire
## Design Direction — accepted 2026-05-08
## Status: DESIGN DIRECTION (not yet authored — direction confirmed, question set pending)

---

## §1 — Referents

Three games inform this direction:

- **Ogre Battle: March of the Black Queen** (Quest, 1993) — Warren's tarot questions. Player answers ethical/situational scenarios; engine derives alignment and stats invisibly. Character creation IS self-expression, not optimization. Player never sees the derivation.
- **Disco Elysium** (ZA/UM, 2019) — 24 skills as voiced inner life. Thought Cabinet as equipped ideology. Personality is surfaced through inner voices, not stat labels. The system is invisible to the player because the presentation layer translates mechanics into experience.
- **Darklands** (MicroProse, 1992) — Career-time as character development. Skills gate content access (Latin makes texts legible; Religion makes relics readable). Lived experience determines what you can do. Time spent doing X IS history of X.

**Synthesis:** Convictions gate REACTIONS (DE-derived interior gate). Histories gate ACTIONS (Darklands-derived exterior gate). Both are derived from narrative choices rather than stat assignment (Ogre Battle-derived presentation layer). Together: a personality-and-competence simulation where the player never touches a stat sheet.

---

## §2 — Core concept

**Derive character state from narrative choices, not stat assignment.**

The existing mechanical substrate (Convictions, Self-Other, Beliefs, histories, skills, TS/Coherence/Spirit/Certainty) is retained unchanged. What changes is the authoring interface:

- **PC creation:** player answers 12–16 scenario-based questions across 4 Lifepath stages. Engine derives the full character-state object from the answer pattern. Player never sees Conviction weights, Self-Other values, or cultural template assignments.
- **NPC authoring:** designer answers the same questions FOR each NPC. Same output: character-state object + textural hooks. NPC backstory expressed as specific authored answers to the same framework.

**Same questionnaire. Same output object. Same textural hooks. Different answerer.**

### §2.1 What a textural hook is

Each question produces not just a stat change but a **specific narrative artifact** — a memory, a place, a person, a moment — that becomes queryable content the engine can surface during play.

"What happened when you were young?" → the spring the river flooded and the Church sent no aid. Engine stores: the river, the flood, the Church's absence, the character's reaction. Later references: "you remember when the Church sent no aid."

Hooks are the prose-writer's personalized feedstock. Not "this NPC has Faith 0.4" — but "this NPC remembers the spring the Church failed them, and that memory is why Faith 0.4."

---

## §3 — Structure

12–16 questions across 4 Lifepath stages with respite at junctures.

**Origin** (3–4 questions) → *respite* → **Formation** (3–4 questions) → *respite* → **Vocation** (3–4 questions) → *respite* → **Catalyst** (3–4 questions) → *your story begins.*

Each respite is a visual/narrative breath — a sense-impression of the world at the stage of life just described. Not a summary screen showing derived stats. Something like: the landscape of childhood. The first tools of a trade. The weight of a calling. The moment everything changed.

Total creation time: 10–15 minutes. Each question: short, evocative, Valoria-specific. Never more than ~2 minutes per question.

### §3.1 What each stage derives

| Stage | Derives | Textural hooks |
|---|---|---|
| **Origin** | Cultural template, caste, early Conviction seeding, starting Certainty, TS baseline, first Knot seed | Place of childhood, family situation, formative memory, first relationship |
| **Formation** | Conviction weight calibration (big moment), skill direction, Self-Other initial setting, second Knot seed | Training context, guiding principle, duty-vs-conscience moment, mentor/teacher |
| **Vocation** | History tag, skills, Belief #1 generation, content-access assignment | What you do, what you're best at, what you believe, what you can't forget |
| **Catalyst** | Arc-initiating event, Goal, final Conviction calibration, possible starting Scar | What changed everything, what you want now, what you'd protect, who you want to become |

### §3.2 NPC scope by tier

| Tier | Questions | Hooks | Replaces |
|---|---|---|---|
| PC | 12–16 (full) | 12–16 | Manual stat assignment + separate Belief/Goal/Inspiration authoring |
| Tier 1 NPC | 12–16 (full, designer-authored) | 12–16 | Migration roster + character_analyses + scattered prose |
| Tier 2 NPC | 8–10 (abbreviated) | 8–10 | npc_roster flaw + implicit goals |
| Tier 3 NPC | 5 (minimal) | 5 | Nothing (currently zero hooks) |

Total authoring: ~37 NPCs × ~10 average = ~370 authored answers. Replaces 4 separate authoring workflows while producing textural hooks that are entirely new.

---

## §4 — NPC → PC transition

When a player retires and takes control of an NPC (or starts as an NPC), they inherit the NPC's questionnaire answers — the full character-state object with all textural hooks.

**Revision questionnaire** at transition: ~5 adjustment questions that let the player modify the NPC's profile while retaining core textural hooks. "Baralta experienced [X]. Now that you're her, do you accept that, or would she have responded differently?"

Preserves hooks (the NPC's history happened). Allows agency (the player's interpretation may differ from the designer's). Same mechanism works for "starting as an NPC" — the player inherits the NPC's profile and can adjust at the first respite juncture.

---

## §5 — Critique findings (7 risks)

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| 1 | Question space constrains character concepts | Mid | Include "between" options; freeform Belief entry at Vocation stage |
| 2 | Designer constraint on NPC authoring | Low | Custom answers with manual mapping as exception path; if >30% override, questions are wrong |
| 3 | Mapping matrix fragility (degenerate vectors) | High | Stage 10 sim validation; degenerate-detection as validator |
| 4 | Replayability decay (same questions) | Low | Replay value from choosing differently (Ogre Battle model); variant phrasing optional |
| 5 | NPC→PC transition assumes player acceptance | Mid | Revision questionnaire (~5 adjustment questions) |
| 6 | Textural hook surfacing quality | Mid | Tag-based matching with conservative surfacing; better few-well-matched than many-poorly-matched |
| 7 | Mode transition (reflective questionnaire → active gameplay) | Mid | Questions short and evocative; respite junctures; 10–15 min max |

---

## §6 — Open items

1. **Opacity vs transparency.** Does the player see their derived Conviction vector after creation, or discover through play? Decision needed.
2. **Branching vs universal questions.** Different Origins get different questions (richer, more authoring) vs everyone answers same questions (simpler, more universal)? Trade-off documented.
3. **Mapping tool.** Designer needs a validation tool for answer→state derivations. Engineering task.
4. **Hook surfacing spec.** When/how does the engine surface hooks? Tag-matching thresholds. Spec needed.
5. **Prototype question set.** Draft one stage (e.g., Origin) with mechanical mappings to ground the authoring template.
6. **Personality-gated reaction integration.** Conviction voices + questionnaire-derived textural hooks must compose — the voice intrusion should reference the hook that produced the Conviction weight. Prose-writer spec.

---

## §7 — Relationship to existing canon

The questionnaire does NOT replace the mechanical substrate. Convictions, Self-Other, Beliefs, histories, skills, TS/Coherence/Spirit/Certainty — all identical to what exists. The questionnaire is a **derivation interface** that produces the same character-state object the substrate defines.

- `conviction_taxonomy_v30` (PP-684) remains canonical.
- `conviction_migration_roster_v30` (PP-685) remains canonical for existing NPC profiles; questionnaire answers supersede migration-roster entries when authored.
- `faction_behavior_v30` (PP-686) cascade math remains canonical.
- `character_histories_v30` Lifepath stages remain canonical; the questionnaire maps onto the same 4 stages.
- `character_canon_v30` and `faction_canon_v30` framework schemas remain valid.
