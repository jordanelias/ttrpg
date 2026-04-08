---
name: valoria-arc-generator
description: >
  Generate emergent campaign arcs for Valoria — causal chains that emerge
  from mechanical systems running in parallel, not scripted plot. Use whenever
  the user asks for: emergent arcs, campaign arcs, narrative arcs, scenario
  chains, "what arcs come out of X mechanic", "arcs involving Non-Player Character Y", or
  "what happens when Z system runs". Also trigger when the user asks how
  mechanics combine, what factions generate naturally, or how the world evolves
  without player intervention. Always use this skill rather than generating
  arcs inline.
---

# VALORIA ARC GENERATOR

**Model:** Sonnet 4.6.

## Input Validation (MANDATORY BEFORE ANY ARC GENERATION)

Before generating arcs, fetch the following from GitHub:

```python
# Step 1: always fetch canonical_sources.yaml first
files = g.read_files_graphql(['references/canonical_sources.yaml'])
canonical = files['references/canonical_sources.yaml']
if canonical is None:
    raise RuntimeError("canonical_sources.yaml missing — cannot resolve which docs are current")

# Step 2: fetch required docs based on arc scope (see Read Protocol below)
# Step 3: check gm_ref/ directory to avoid arc duplication
```

**Memory contamination warning:** userMemories may contain mechanical values (track values, territory data, faction stats, etc.) that feel current but are not fetched from GitHub. Do not use any value from memory as a source for mechanical analysis. Fetch only.

**Do not read compilation stage files from memory.** Even if you have seen them this session, verify via `canonical_sources.yaml` which version is current before using any values.

**If `compilation_current: false` in `canonical_sources.yaml`:** Use the canonical design doc for that system, not the compilation snapshot.

## What This Produces

Each arc has three components:
1. **Narrative block** — 3–4 paragraphs in plain prose. Describes what the arc feels like at the table, which Non-Player Characters are present, what players observe before they understand what is happening. No mechanical jargon in this block.
2. **Mermaid flowchart** — Full causal chain from mechanical seed through branches to resolution. Every node cites the mechanic driving it. Branches represent player choice points.
3. **Footer** — Emergent logic statement (1–2 sentences: why no player designed this), arc shape (season count and structure).

Deliver 3–5 arcs per batch unless the user specifies otherwise. End each batch with a cross-arc interaction table.

---

## Read Protocol (GitHub fetches — do not skip)

Fetch in this order. Check `canonical_sources.yaml` to confirm current paths before fetching.

**Always required:**
- `references/canonical_sources.yaml` (done in input validation)
- `references/glossary.md` — term definitions; fetch before using any game-specific term
- `references/params_factions.md` — faction stats, Domain Actions, seasonal accounting
- `references/params_core.md` — dice engine baseline

**Fetch if arcs involve Thread mechanics:**
- `references/params_threadwork.md`
- `canon/00_philosophical_foundations.md` §1–2 only (inseparability, scale principle) — fetch the file, read only those sections

**Fetch if arcs involve social/debate:**
- `references/params_debate.md`

**Fetch if arcs involve mass battle:**
- `references/params_mass_combat.md`

**Fetch if arcs involve specific Non-Player Characters:**
- The canonical NPC doc (check `canonical_sources.yaml` for current path)

**Fetch if arcs involve territories or clocks:**
- The canonical territories doc (check `canonical_sources.yaml` for current path)

**Check for prior arcs (fetch directory listing, avoid duplication):**
- `gm_ref/` — list contents via GitHub API before generating; do not reproduce an arc already documented there

**Fetch log (emit before any analysis):**
```
## FETCH LOG
canonical_sources.yaml: ✓ fetched ([N] lines)
[canonical design doc path]: ✓ fetched ([N] lines)
references/params_[system].md: ✓ fetched ([N] lines) / ✗ missing
```
If any required file is missing from this log, stop — the analysis is invalid.

**Version check:** confirm `<!-- version: -->` tag in each fetched params file matches current ruleset version in `compilation/README.md`. If mismatch: flag `[STALE PARAMS: <file> is vX.XX, current is vY.YY]` and stop.

**Do not read stage files or design files directly to get mechanical values.** Use params files. If a value is missing from params, flag it as a gap rather than reading the source document mid-generation.

---

## Arc Generation Rules

**Mechanical grounding:** Every node in the flowchart must cite a specific mechanic — stat, Ob value, threshold, trigger condition, or faction rule from the fetched params files. No nodes that say "situation escalates" without naming the mechanic doing the escalating.

**Emergence standard:** Each arc must satisfy: *no single player decision caused this; it required multiple independent systems running simultaneously.* If a single player choice is sufficient to explain the arc, it is a plot hook, not an emergent arc.

**Canon constraints (non-negotiable):**
- Niflhel does not harvest threads. Never attribute Rendering Stability drain to Niflhel operations.
- All three clock dimensions (Rendering Stability, Theocracy Counter (TC), Institutional Pressure (IP)) are independent. Do not treat them as the same system.
- Ethical framework penalties apply to factions, not players directly.
- Seasonal cap: ±2 per faction stat per season regardless of Domain Action count.

**Scope:** Keep arcs to systems with current params files. Do not invent mechanics. If a mechanic needed for an arc has a known gap, note the gap inline rather than assuming a value.

**Non-Player Character fidelity:** Use documented Beliefs, Resonant Styles, and trigger conditions exactly from the fetched NPC doc. Do not invent Non-Player Character motivations. If Non-Player Character data is needed and not found, flag it with [EDITORIAL].

**Editorial gate:** Any arc requiring a worldbuilding or narrative decision not resolvable from fetched documents must be flagged: `[EDITORIAL: requires user approval — description]`.

---

## Format Template

```
## Arc N: [Title]

**Primary mechanics:** [list — each cited to its params file]
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
- `.md` file if 4+ arcs or if the user requests a document.
**Pre-commit (run before every `atomic_commit()` call):**
```bash
python3 tools/freshness_gate.py --update
python3 tools/broken_dependency_checker.py
python3 tools/patch_propagation_checker.py
```
Exit 0 required on all three. On non-zero exit: fix the reported issue before committing.

**Post-commit verification:** after `atomic_commit()` returns a SHA, re-fetch all files modified in that commit and confirm content matches what was committed. If content differs: flag immediately, do not proceed.

- Commit to `gm_ref/` on GitHub after every batch via `g.atomic_commit()`. File naming: `arcs_NN_MM_[topic].md`.
- Log any canon corrections found during generation as `[GAP-ARC-NN]` in the output document.
