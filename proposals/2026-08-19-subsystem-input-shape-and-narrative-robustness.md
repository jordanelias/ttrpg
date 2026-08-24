# How Each Subsystem Is Shaped By Its Inputs — and whether we can generate a world that feels real

## Status: FINDINGS + CORRECTED PLAN. Content/design only — no tooling, no moves, no registry edits (another session owns the restructure). Nothing here proposes a vocabulary; see §2.

**Date:** 2026-08-19 · **Method:** agonist→antagonist relay. A plan was written, an independent read-only critic attacked it without seeing its reasoning, **the critic returned UNSOUND**, I verified its blocking claims against the tree, and the plan was rebuilt. §1 records what the critique killed, because that is the most useful part.

---

## §1 THE PLAN WAS WRONG AND THE RELAY CAUGHT IT

I proposed hand-building three inventories per subsystem (keys, acquisition-layer stats, inputs), an 11-value input-type axis, and a six-dimension robustness metric. **Three of the four instruments rebuild artifacts that already exist, anchored and guarded. The fourth measures wiring while claiming to measure design.** Verified:

| Claim | Verified |
|---|---|
| **15 per-subsystem flow skeletons already exist**, one per subsystem, with §2 IN (`input · kind · origin · anchor`), §4 OUT, §5 state (`field · R/W/RW · owner`), §6 seams (**with a `direction` column**), §7 traced gaps with *required evidence* | ✅ `systems/*/[a-z]*_flow_skeleton_v1.md` — 15 files; format contract at `systems/_architecture/subsystem_flow_skeletons_v1.md:88-99` |
| A guard test asserts every citation lands on its named symbol | ✅ `tests/valoria/test_flow_skeletons.py` — **95 passed** |
| **The input-kind enum already exists and is enforced**: `key · world-state · arg · param · flag · registry · file` | ✅ spec `:93`. My 11-type axis would have been a **fifth** competing vocabulary |
| **Vocabulary unification is under an explicit Jordan hold** — *"No vocabulary unification lands here or anywhere else until that fork resolves"* (ED-IN-0103) | ✅ `references/module_contracts.yaml:16-21` |
| `npcs` has code, traced to `engine/autoload/npc_ai.py` + `systems/world/sim/npe.py` | ✅ `npcs_flow_skeleton_v1.md:12-16`. **My "npcs has zero .py files" was a folder-vs-code error** the spec forbids by standing rule (`:102-104`) |
| The taxonomy axis is already CANONICAL and is **not** gameplay/worldly — it is strategic/personal scale + named containers, and **threadwork is explicitly not a gameplay container** | ✅ `systems/_architecture/videogame_mode_spec.md:3`, `:83` |
| `acquisition` already names a Varfell territorial mechanic | ✅ `systems/factions/sim/varfell_territorial_acquisition.py` — a §4 word-choice collision |

**Currency of the existing artifacts, since building on stale ones would be the same mistake:** skeletons stamp `Traced at: 6545067`, only **6** subsequent commits touch `systems/` or `engine/`, the guard is green, and `build_engine_atlas.py --check` reports current.

**The corrected plan:** don't inventory — **read the skeletons and the atlas, and produce the delta.** Adopt the existing 7-value `kind` enum. Replace the six-dimension composite with **open half-edges** (declared inputs with no producer, declared outputs with no consumer), which is a design property rather than a code-mass proxy. Everything below follows it.

---

## §2 WHAT ACTUALLY SHAPES EACH SUBSYSTEM — and the Key substrate is not it

The skeletons carry **165 traced inputs** across 15 subsystems. By the enforced `kind` enum:

| kind | count | share |
|---|---:|---:|
| `arg` | 49 | 30% |
| `world-state` | 42 | 25% |
| `param` | 17 | 10% |
| `flag` | 14 | 8% |
| `registry` | 12 | 7% |
| **`key`** | **7** | **4%** |
| `file` | 4 | 2% |
| *(qualified variants my parse split out)* | 21 | 13% |

### The finding

> **Keys flow OUT and essentially never IN.** The skeletons trace **108 outputs** against **7 key-typed inputs** — and 6 of those 7 are not subsystem consumption at all: four are `_architecture` (the substrate constructing its own objects, plus `echo[...]` dict fields), one is `articulation`'s subscriber callback receiving the emitted object, and one is a mis-kinded dice roll in fieldwork.

**No gameplay subsystem and no worldly subsystem takes a Key as an input.** The Key substrate — the thing the architecture is organised around — is a pure emission-and-transport layer. What actually shapes a subsystem is **its caller's arguments (30%) and direct world-state reads (25%)**.

### ⚠ This corrects my own earlier interim claim

I reported from `module_contracts.yaml` that "gameplay subsystems consume almost nothing" (combat 2, fieldwork 1, social_contest 1, threadwork 0, mass_battle 0) while `npc_behavior` consumed 31 and `faction_state` 25. **That was true of declared *Key* edges and misleading as a general statement.** The skeletons show social_contest with 17 traced inputs, mass_battle 12, combat 11, threadwork 11 — they are richly shaped, just not *by Keys*. The contracts declare only the Key layer, which is 4% of the real input flow.

The corrected statement is structural rather than per-subsystem: **the Key layer is asymmetric — rich as an output path, vestigial as an input path.** That is why nothing loops.

### Per-subsystem input profile

| subsystem | lane | IN | OUT | state | seams | gaps | dominant kind |
|---|---|---:|---:|---:|---:|---:|---|
| overview | IN | 18 | 10 | 21 | 23 | **18** | world-state / param |
| _architecture | IN | 15 | 9 | 14 | 12 | 17 | world-state / key |
| social_contest | SC | 17 | 9 | 14 | 10 | 16 | arg / flag |
| factions | FA | 11 | 8 | **23** | 10 | 15 | arg / world-state |
| world | WR | 14 | 9 | 15 | 12 | 10 | world-state / arg |
| characters | PC | 14 | 7 | 13 | 4 | 7 | **arg (7)** |
| mass_battle | MB | 12 | 9 | 14 | 6 | 10 | **arg (6)** |
| victory | IN | 12 | 7 | 9 | 4 | 7 | world-state |
| threadwork | WR | 11 | 10 | 9 | 9 | 11 | world-state |
| combat | PC | 11 | 6 | 8 | 7 | 6 | arg |
| fieldwork | FI | 9 | 7 | 7 | 9 | 10 | arg |
| settlements | SE | 8 | 7 | 11 | 9 | 12 | even |
| npcs | WR | 8 | 7 | 7 | 6 | 10 | arg / world-state |
| articulation | IN | 7 | 3 | 3 | 5 | 10 | arg |
| ui | IN | 0 | 0 | 0 | 0 | 9 | — |
| **TOTAL** | | **167** | **108** | **168** | **126** | **168** | |

**168 traced gaps — one per input.** That ratio is the headline number for "how complete is this."

### Open half-edges (the corrected metric), as the skeletons already record them

Only two outputs are traced as having no consumer at all, and both are load-bearing:
- **threadwork** — `scene.thread_operation`, `meta.thread_woven`: *"declared in contract, never constructed anywhere."* A subsystem with 10 outputs emits **zero** of them in code.
- **characters** — `CampaignResult.final_state['convictions'/'beliefs']`: *"nothing reads these two keys downstream."*

---

## §3 NARRATIVE ROBUSTNESS — can we generate a world that feels real?

The genuinely new axis, and the critique did not invalidate it. Measured directly.

### §3.1 What the runtime can express, per entity

| Entity | Fields | Named? | What can vary |
|---|---:|---|---|
| **Settlement** (`settlements/sim/registry.py`) | **~20** | **yes** | prosperity · defense · order · fort_level · garrison · legitimacy · popular_support · facility_tier · suspicion · pressure · active_directive · religious_building · church_attention · governor_emergence |
| **Faction** (`engine/autoload/game_state.py`) | ~11 | yes | **7 of 11 are booleans**, 4 of those `*_used_this_arc` turn-tracking. The stats live elsewhere (L/Sta/W/I/Mil) |
| **NPC** (`systems/world/sim/npe.py`) | **5 axes** | **NO** | stance (issue→1–5) · worldview (1–2 of 8 convictions) · affiliation + loyalty 0–3 · compromise_category · volatility 1–5 |

**A generated NPC has no name, no relationships, no history, no memory and no goal.** Two of them differ in five dimensions, none of which reads as personality. `references/names_index.yaml` holds **528 entries** and has **no runtime loader** — the engine can generate a person and cannot name them.

### §3.2 The inverse correlation

The authored corpus is richest exactly where the runtime is poorest.

`systems/npcs/` holds **20 documents**: a roster of 13 named characters with roles, motivations, arc trajectories and mode-interface matrices; foils; character analyses; and a **relational graph with six authored edge types** — sworn-bond, liege-vassal, kinship, patronage, rivalry, feud — each with strain capacity, accrual mechanisms and break/transition rules. `systems/characters/` adds a conviction taxonomy with an axis matrix and composition rules.

**Zero code references any of it.**

> **Authored narrative richness and runtime expressiveness run opposite to one another.** The most heavily designed entity — the NPC, six relation types and a conviction matrix — is the least implemented: five integers and no name. The least designed — the settlement — is the most implemented, and it is the only entity a player could presently perceive as particular.

### §3.3 Why this compounds with §2

A character cannot be *shaped* by what happens to them when (a) the entity has no field to record it in, and (b) the subsystems resolving their scenes take no Keys as input. The narrative gap and the input-asymmetry gap are the same gap seen from two sides: **events are emitted and never read back into the things they happened to.**

---

## §4 WHAT I AM NOT DOING, AND WHY

- **Not proposing an input vocabulary.** ED-IN-0103 holds it, and the 7-value `kind` enum already exists and is enforced.
- **Not proposing "equal robustness" as a goal.** The critique's strongest argument: `videogame_mode_spec.md` assigns *different* resolution modes per container by design, and CLAUDE.md §10 names growing a scale-local dialect as **shape divergence** — which "make them equal" invites. The defensible narrow version is equalising only **specification completeness** and **closed half-edges**, both already enumerable.
- **Not scoring subsystems on a composite.** Four of my six dimensions produce four different winners, and code-mass dimensions rank the two most design-complete, least-wired subsystems (threadwork, fieldwork) as weakest — backwards for a design investigation.

---

## §5 WHAT WOULD FALSIFY THIS

| Claim | Check | Ran |
|---|---|---|
| 15 skeletons exist with the stated sections; guard green | `ls`; read the spec; run the test | ✅ 95 passed |
| The `kind` enum exists and is enforced | read spec `:93` | ✅ |
| ED-IN-0103 holds vocabulary work | read `module_contracts.yaml:16-21` | ✅ |
| Keys are ~4% of traced inputs | parse §2 of all 15 skeletons | ✅ — **21 rows carry qualified kinds** (`arg (default)`, `key (gate)`) and were split out; totals stated include them |
| NPC has 5 axes and no name field | read the dataclass | ✅ |
| `names_index.yaml` has no runtime loader | grep `engine/`+`systems/` | ✅ |
| Skeletons are current | 6 commits since the trace ref; atlas `--check` current | ✅ partial — **I did not re-trace; if any of those 6 commits changed a traced path the counts drift** |

**The claim most likely to be wrong:** that the §2 counts are complete. My parser reads markdown tables and drops malformed rows; it found 165 of the 167 §2 rows the section-counter saw. The skeletons themselves are the authority, not my parse of them.
