---
name: valoria-arc-generator
description: >
  Generate emergent campaign arcs for Valoria — causal chains that emerge
  from mechanical systems running in parallel, not scripted plot. Use whenever
  the user asks for: emergent arcs, campaign arcs, narrative arcs, scenario
  chains, "what arcs come out of X mechanic", "arcs involving NPC Y", or
  "what happens when Z system runs". Also trigger when the user asks how
  mechanics combine, what factions generate naturally, or how the world evolves
  without player intervention. Always use this skill rather than generating
  arcs inline.
---

# VALORIA ARC GENERATOR

## What This Produces

Each arc has three components:
1. **Narrative block** — 3–4 paragraphs in plain prose. Describes what the arc feels like at the table, which NPCs are present, what players observe before they understand what is happening. No mechanical jargon in this block.
2. **Mermaid flowchart** — Full causal chain from mechanical seed through branches to resolution. Every node cites the mechanic driving it. Branches represent player choice points.
3. **Footer** — Emergent logic statement (1–2 sentences: why no player designed this), arc shape (season count and structure).

Deliver 3–5 arcs per batch unless the user specifies otherwise. End each batch with a cross-arc interaction table.

---

## Read Protocol

Before generating, read the following in this order. Stop reading a file once you have what you need — do not read documents in full if the relevant section is identifiable.

**Required reads:**
1. `compilation/stage1_core_engine.md` — dice, TN, Ob, degrees of success
2. `compilation/stage6_factions.md` — faction stats, ethical frameworks, Domain Actions, unique actions, seasonal accounting
3. `compilation/stage12_campaign_modes.md` — session structure, endgame indicators, clock synchronisation

**Read if arcs involve Thread mechanics:**
- `designs/threadwork_redesign_v25.md` — Coherence, RS, Leap, operations, co-movement
- `canon/Valoria_Philosophical_Foundations.md` §1–2 only (inseparability, scale principle)

**Read if arcs involve social/debate:**
- `designs/debate_system_redesign_v1.md` — quaestio structure, asymmetric proceedings, genre resonance

**Read if arcs involve mass battle:**
- `designs/mass_battle_v3.md` — CR, Cohesion, Thread in battle, co-movement at scale

**Read if arcs involve specific NPCs:**
- `compilation/stage13_npcs.md` — Beliefs, Resonant Styles, trigger conditions, mechanical profiles

**Read if arcs involve territories or clocks:**
- `compilation/stage7_territories.md`
- `compilation/stage5_clocks.md` (if present; check directory first)

**Check for prior arcs (avoid duplication):**
- `gm_ref/` directory — list contents before generating; do not reproduce an arc already documented there

---

## Arc Generation Rules

**Mechanical grounding:** Every node in the flowchart must cite a specific mechanic — stat, Ob value, threshold, trigger condition, or faction rule. No nodes that say "situation escalates" without naming the mechanic doing the escalating.

**Emergence standard:** Each arc must satisfy: *no single player decision caused this; it required multiple independent systems running simultaneously.* If a single player choice is sufficient to explain the arc, it is a plot hook, not an emergent arc.

**Canon constraints (non-negotiable):**
- Niflhel does not harvest threads. Never attribute RS drain to Niflhel operations.
- All three clock dimensions (RS, TC, IP) are independent. Do not treat them as the same system.
- Ethical framework penalties apply to factions, not players directly — players have no framework penalty unless they are operating as a faction leader.
- Seasonal cap: ±2 per faction stat per season regardless of Domain Action count.

**Scope:** Keep arcs to systems already compiled or in experimental designs. Do not invent mechanics. If a mechanic needed for an arc has a known gap (GAP-ARC-01 or similar), note the gap inline rather than assuming a value.

**NPC fidelity:** When named NPCs appear, use their documented Beliefs, Resonant Styles, and trigger conditions exactly. Do not invent NPC motivations. If NPC data is needed and not in stage13, flag it with [EDITORIAL].

**Editorial gate:** Any arc that requires a worldbuilding or narrative decision not resolvable from existing documents must be flagged: `[EDITORIAL: requires user approval — description]`.

---

## Format Template

```
## Arc N: [Title]

**Primary mechanics:** [list]
**Primary NPCs (if any):** [list]

---

### Narrative

[3–4 paragraphs prose. No mechanical jargon. What the table experiences.]

---

### Mechanical Causal Chain

[mermaid flowchart]

**Why this arc is emergent:** [1–2 sentences]

**Arc shape:** [season counts, structure]
```

---

## Output

- Inline in chat if 3 arcs or fewer and no prior arcs to check.
- `.md` file to `/mnt/user-data/outputs/` if 4+ arcs or if user requests a document.
- Commit to `gm_ref/` on GitHub after every batch. File naming: `arcs_NN_MM_[topic].md`.
- Log any canon corrections found during generation as `[GAP-ARC-NN]` in the output document.
