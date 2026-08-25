# Throughlines and Precedent — a cross-scale analysis of Valoria
## Status: PROPOSED — analysis and recommendation only. Nothing here is ratified by merging it.
## Date: 2026-08-25 · Lane: IN (cross-cutting; touches PC, MB, SC, FA, SE, WR, GO) · No ED allocated

> **Read this first.** Under CLAUDE.md §0.05 this document is **reference, not mechanism.** It may be
> cited for intent, history and vocabulary. It may not be cited as the reason a behaviour is correct.
> Every recommendation in it names the module that would change, because a recommendation naming only
> a document is not a recommendation. If this file were deleted, the game would behave identically —
> which is the test §0.05 supplies, and this document passes it deliberately.

---

## What this is

A commissioned analysis. Jordan's instruction, in four parts across the session:

1. Read **all** proposals — including the June and July material that was archived out of `main` —
   and the historical research.
2. Orchestrate the **throughlines** and their application to Valoria's subsystems, **without pattern
   matching**.
3. Write the analysis alongside **extensive precedent research from acclaimed games**, ensuring every
   claim is **NERS-qualified**, adversarial, and shows subsystems **interacting across scales in all
   discussions**.
4. Draw extensively from the **Goldenfurt vectorized generation approach and other vectorized noisy
   slices**; and ensure coverage of the **officers system, advancement and demotion, and internal
   competition within factions**.

## The corpus actually read

| Source | Extent |
|---|---|
| Live proposals (`proposals/`) | 40 files · ~198,000 words |
| Live audit corpus (`audit/`) | 121 files · ~665,000 words |
| **Archived June/July 2026 design docs** — deleted from `main`, **recovered from git history for this run** | **579 files · ~1,547,000 words** |
| Live subsystem canon (`systems/`) | 224 files · ~655,000 words |
| Executable tree | ~39,000 lines of engine Python, read directly |

The archived corpus is the part nobody had read against the current tree. It was recovered by walking
`git log --diff-filter=D` and extracting each file at its last living commit. **June was the most
mechanically productive month in this repository's history and its output is not on `main`.**

## How it was made — and why the method is part of the finding

An agonist→antagonist relay per CLAUDE.md §10, tiered per §10's table:

| Phase | Tier | Count | Output |
|---|---|---|---|
| Read | **Fable 5**, read-only | 7 lanes | lane reports over the corpus above |
| Precedent | **Sonnet 5** + web | 5 dossiers | grand strategy · emergent narrative · TTRPG/GM-less · procgen · tactical/cross-scale |
| Throughline orchestration | **Opus 5** | 1 | the map: audit, register, matrix, decomposition, adversarial docket |
| Authorship | **Opus 5** | 5 chapters | this document |
| Adversarial pass | `valoria-critic` (structurally read-only) | — | edits to the chapters, per §0 — not a separate findings document |

⚠ **The orchestration node was commissioned on Fable 5 and hit the account's Fable usage limit.** The
seven Fable read lanes had already completed; the node was re-dispatched on Opus, which §10 assigns to
"the verify / judge / synthesis stage that *gates* a result". Recorded because a tier substitution
that goes unrecorded is how a method claim rots.

### The rule that did the most work

A **throughline** here is not a shared word. Two mechanisms are on one throughline only if there is
**(a)** state one writes and the other reads, **(b)** an invariant both instantiate such that changing
it changes both, or **(c)** a failure mode they share *by construction* — same math, same feedback
topology. Anything resting on shared vocabulary is a **collision**, and gets killed and recorded.

**25 candidate throughlines were killed under this rule** (~40 word-senses). That number is a quality
signal, not an absence of findings. Killing a false throughline is worth as much as finding a real
one, because a false one sends someone to build a bridge between two things that were never apart.

---

## The finding

**Valoria has four working engines and no populated world to run them on.**

The executable census, measured at `571ae14`:

| Subsystem | Executable Python | Scale |
|---|---:|---|
| `systems/mass_battle/sim` | 11,612 | unit / battle |
| `engine/` | 8,942 | spine |
| `systems/combat/combat_engine_v1` | 7,901 | personal |
| `systems/social_contest/sim` | 7,045 | personal |
| `systems/factions/sim` | 2,744 | faction |
| `systems/settlements/sim` | **1,012** | settlement |

The three scales that resolve **events** are heavily built. The two that hold **persons and their
offices** are the thinnest in the tree — settlements is one-eleventh the size of mass battle. Every
part of Jordan's officer mandate lives in those bottom two rows, and none of it executes.

The cross-scale matrix (Chapter 3 owns it in full) makes the same point without reference to size.
Of its **six EXECUTED cells, five are between non-personal scales** — faction↔faction, unit↔unit,
unit↔faction, settlement↔settlement — and the sixth, personal→faction, is **a faction contesting
itself** (`_emergency_council_parties` derives both sides from one faction's own aggregate stats;
the echo it returns is self-addressed, `actor_faction == target_faction`).

> **The crossings that execute are exactly the ones that need no person.**

### The narrowed claim, after adversarial audit

The first draft of this analysis asserted something broader — that Valoria's substrate is built and
its writers are absent, generally. **The adversarial pass refuted the general form and it is
withdrawn.** What survives, and what the chapters argue:

> Valoria's authored state has no writers; and **one absent object — a persistent named person
> instantiated at world-gen — accounts for the largest connected group of those absences.** That
> absence is not schedule state. It is *ratified and guarded*: a `strict=True` xfail
> (`engine/tests/test_pipeline_reach.py:625`) and a seeded golden (`test_f7_smoke_oracle.py:335`,
> `assert npcs == 0`) both fail if the world ever populates. Its stated blocker — that no canon names
> an initial population count — is answerable today from **35 authored `status: canonical` records** (of 46 total; 11 are `status: proposed`, and loading *those* would be the very fabrication the deferral protects),
> by the same deterministic manoeuvre `populate_from_geography` used for
> identical defect for settlements.
>
> ⚠ **That manoeuvre is NOT golden-safe for persons** — Correction 4 refutes the
> extrapolation. The settlements docstring's claim is true *about settlements*, which have no
> per-season RNG-drawing consumer; `world.npcs` does (`npe.simulate_npc_actions`, called from
> `systems/overview/sim/accounting.py:139`). The honest sequence is **RNG substream → loader**.

Three discriminators separate this from the vacuous "an unfinished game is unfinished", and the
chapters carry all three wherever the claim appears: the emit/consume asymmetry is **one-directional**
(108 outputs against 7 key-typed inputs); the absence is **guarded**, not pending; and
**ratification outruns execution** as a measured standing class (see `02_ruled_but_unexecuted.md`).

---

## The chapters

| | Chapter | File | Thesis |
|---|---|---|---|
| 1 | **The World Has No People In It** | `04_ch1…` | One absent object explains the largest connected group of Valoria's disconnected substrate; the absence is guarded rather than pending, and 35 canonical officeholders are waiting on a loader — though the in-tree template is *not* as free as first claimed (see Correction 8). |
| 2 | **The Ladder Runs Both Ways, On Paper** | `05_ch2…` | Jordan's three asks need almost nothing designed and nearly everything wired: **74 rungs are authored across ten tables, each carrying an entry gate *and* a demotion cell**, plus ≥15 cross-cutting down mechanisms — against **0 up and 0 down paths executing**. The sharpest finding is not an absence: `_emergency_council_parties` is a **default-ON intra-faction two-sided contest firing ~975× per golden batch** — the contest, trigger, resolver and consequence all exist, and neither side is anybody. |
| 3 | **One Resolver, Four Scales, One Scalar** | `06_ch3…` | The margin ladder is exemplary and is being fed a constant: **`roll_pool` accepts `tn`, records it, and discards it** — pinned to TN 7, wrong by 21.2 percentage points on Failure at 6D/Ob 2/TN 8, across **19 production call sites**. (The obstacle half of this thesis was *refuted* during review — see Correction 7.) One level up, the same defect: **every executing cross-scale crossing carries one scalar and no person, three of them the same field, `Faction.Mil`.** |
| 4 | **Weights Bias, Noise Chooses** | `07_ch4…` | VSG's architecture survived every audit and its calibration survived none; it should ship behind an executing expressive-range gate. |
| 5 | **What We Should Not Do** | `08_ch5…` | Ten documented failures from acclaimed games, converted into guards on named Valoria modules — plus the four problems the field has not solved and this project should not pretend to have. |

Supporting registers, which are the shortest path from this session to running behaviour:

- `01_verified_defects.md` — defects verified at HEAD, each with a falsifier.
- `02_ruled_but_unexecuted.md` — decisions Jordan already made that the tree does not obey.
- `03_method_and_corrections.md` — how the run was conducted, and **its own two errors**.

---

## What this analysis got wrong — eleven corrections

Recorded in `03_method_and_corrections.md` rather than buried, because the analysis argues that
Valoria's characteristic hazards are mistaking a shared word for a shared mechanism and citing prose
as evidence of behaviour — and its orchestrator did both.

| # | The error | Caught by |
|---|---|---|
| 1 | `Standing` "ratified 0–10 and unexecuted" — **a vocabulary collision promoted to a mechanism claim.** Three distinct mechanisms share the name; the ruling ordered them *scope-tagged apart*. | the independent adversarial audit |
| 2 | Ten absences over-generalised into one pattern | the same audit, narrowing it to seven |
| 3 | **A stale golden propagated inside a warning against stale goldens** | Chapters 1, 2 and 5, independently |
| 4 | "Golden-safe by construction" — populating the world **does** move seeded goldens | Chapter 1, by controlled experiment |
| 5 | "46 records each with stats" — **exactly one has stats**; 7 have territory | Chapter 2, by counting |
| 6 | `temperaments.py` called **executed**; it has zero callers and zero tests — *executable*, not executed | Chapter 4 |
| 7 | **R2: a recommendation that would have overwritten a live Jordan hold** — sourced from a stale docstring | Chapter 3 |
| 8 | "46 `status: canonical` records" — **35 are canonical; loading the other 11 would be the fabrication the deferral forbids** | CH1 antagonist pass |
| 9 | **The `Standing` retraction was itself partly wrong** — the ledger entry (never opened until the third pass) ratifies a range *and* orders the scope-tag | CH2 antagonist pass |
| 10 | **"No n≥100 balance oracle exists"** — `tools/balance_oracle.py` exists and has been the control on three golden re-pins. Inherited from **CLAUDE.md §7, which is stale**, and propagated without a grep | cross-chapter antagonist pass |
| 11 | **Incomplete propagation** — three retractions each missed a document, leaving one directory holding both a retraction and its retracted claim | cross-chapter antagonist pass |

**Not one of the eleven was caught by the producer re-reading its own work.** Six came from
structurally independent readers, five from downstream authors refusing to take a supplied claim on
trust — and four of those by *measuring, counting or grepping* rather than reading.

Error 10 is the sharpest indictment of the method and the strongest argument for it at once: an
analysis whose central rule is *verify against code, never inherit from prose* inherited from prose —
from CLAUDE.md itself — the claim that **a particular file does not exist**, and eleven agents
repeated it without running `ls`. That is CLAUDE.md §10's relay and §0.1's measurement
discipline both earning their cost, on this document, in this session.

Error 7 is the one worth dwelling on: a register built to catch decisions that outran their evidence
sourced one of its two headline rows from **a comment** — written by someone rigorous, in the right
file, about their own function, and simply older than the measurement that superseded it. The lesson
at its narrowest: **prose ages silently and code does not.**

## Standing caveats carried into every chapter

- The **~87% degenerate win-share** figure is a **retracted small-N artefact** that five documents
  propagated. The live golden at HEAD is `engine/tests/test_f7_smoke_oracle.py:267` —
  `GOLDEN_WIN_SHARE = {'Crown': 62.5, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 12.5}`,
  regenerated 2026-08-24 at the mass-battle engine swap.
  ⚠ **This caveat originally carried a stale value** — `{Crown: 37.5, Church: 12.5, Hafenmark: 12.5,
  Varfell: 37.5}` — read out of a comment at `:75` that exists to preserve the PREVIOUS pin. That is
  this analysis's third self-inflicted error and it is recorded in `03_method_and_corrections.md`
  rather than silently fixed, because it happened *inside a warning against propagating a retracted
  number*. And ⚠ **none of these figures is a balance fact**: the file states (`:264-265`) that
  n=2/seed-0 and n=8/seed-42 "cannot distinguish a balance change from noise", and the n>=100 oracle
  its own line 8 demands still does not exist. They are reproducibility pins.
- ⚠ **`tools/balance_oracle.py` EXISTS, and this analysis said four times that it did not.** It is the
  n≥100 controlled comparison — 120 campaigns per arm, both arms in one process, two-proportion z —
  and it has been run **three times as the control before a golden re-pin**
  (`engine/tests/test_f7_smoke_oracle.py:106, :137, :218`). The claim was inherited from
  **CLAUDE.md §7 and `test_f7_smoke_oracle.py:8`, both stale**, and propagated without a grep — the
  run's own no-pattern-matching failure, one level up. What does not exist is a *CI-gated standing*
  oracle, and the tool's author argues against making it one (`balance_oracle.py:11-13`: *"a gate
  that slow gets skipped, which is worse than a tool that gets run"*). **Consequence: every
  recommendation here that hedged "this re-pin cannot honestly be called neutral, because no control
  exists" is wrong, and becomes concrete — add an arm to `tools/balance_oracle.py` and run it before
  touching the golden.**
- `engine/engine_params/params_tables.yaml` is a **byte-frozen capture of prose** whose degree bands
  are the **pre-ruling, retracted** ones. The live ladder is margin-based in
  `engine/autoload/dice_engine.py::degree_from_net`. Never lift a number from the capture without
  checking the code.
- **`PP-NNN` provenance is advisory** — most cited ids resolve to no register. `ED-` citations are
  validated by a blocking gate.
- `python tools/m1_acceptance.py --summary` at `571ae14`: verdict **NOT MET**, 2 rows failing; row 4
  is self-declared **DOC-DERIVED** and must never be cited as evidence a juncture runs.
