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
> an initial population count — is answerable today from **46 authored `status: canonical` records**,
> by the same deterministic, golden-safe manoeuvre `populate_from_geography` already used to fix the
> identical defect for settlements.

Three discriminators separate this from the vacuous "an unfinished game is unfinished", and the
chapters carry all three wherever the claim appears: the emit/consume asymmetry is **one-directional**
(108 outputs against 7 key-typed inputs); the absence is **guarded**, not pending; and
**ratification outruns execution** as a measured standing class (see `02_ruled_but_unexecuted.md`).

---

## The chapters

| | Chapter | Thesis |
|---|---|---|
| 1 | **The World Has No People In It** | One absent object explains the largest connected group of Valoria's disconnected substrate; the absence is guarded rather than pending, and 46 authored officeholders are waiting on a loader with a proven in-tree template. |
| 2 | **The Ladder Runs Both Ways, On Paper** | Jordan's three asks need almost nothing designed and nearly everything wired: 88 up-gates and 74 demotion cells are authored, the relational substrate executes, and what is missing is one owned Standing, one writer per direction, and one decision that reads a divergent interest. |
| 3 | **One Resolver, Four Scales, One Scalar** | The margin ladder is exemplary and is being fed two constants — `net` ignores TN across 28 call sites, `ob` is hand-set against a ruling that says derive it — and one level up, everything that crosses a scale boundary crosses as a single scalar. |
| 4 | **Weights Bias, Noise Chooses** | VSG's architecture survived every audit and its calibration survived none; it should ship behind an executing expressive-range gate. |
| 5 | **What We Should Not Do** | Ten documented failures from acclaimed games, converted into guards on named Valoria modules — plus the four problems the field has not solved and this project should not pretend to have. |

Supporting registers, which are the shortest path from this session to running behaviour:

- `01_verified_defects.md` — defects verified at HEAD, each with a falsifier.
- `02_ruled_but_unexecuted.md` — decisions Jordan already made that the tree does not obey.
- `03_method_and_corrections.md` — how the run was conducted, and **its own two errors**.

---

## What this analysis got wrong

Recorded here rather than buried, because the analysis argues that Valoria's characteristic hazard is
mistaking a shared word for a shared mechanism, and its own orchestrator did exactly that.

1. **The `Standing` claim is RETRACTED.** The orchestrator asserted that `Standing` was ratified to
   0–10 on 2026-07-08 and left unexecuted, so the officer ladder was written against a nonexistent
   scale. False. **Three genuinely distinct mechanisms share the name** — a contest ethos float
   (`primitives.py:31-48`), an unclamped `Faction.standing: int` (`game_state.py:129`), and the
   prose-only officer rank ladder 0–7. The 2026-07-08 ruling identified the homonym and ordered the
   senses **scope-tagged apart**; it did not unify a range. Chapter 2 carries the correction, and the
   real defect it exposed — an unclamped integer read straight into a dice pool — is worth more than
   the claim it replaced.
2. **The first thesis over-generalised.** Ten absences were presented as one pattern; the audit
   narrowed them to seven, and showed that three belonged to three different classes.

Both were caught by the **structurally independent** adversarial stage — a reader that never saw the
producer's reasoning — and neither by the producer re-reading its own work. That is §10's relay doing
the job it was designed for, and it is the strongest evidence in this document that the adversarial
stage earns its cost.

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
- `engine/engine_params/params_tables.yaml` is a **byte-frozen capture of prose** whose degree bands
  are the **pre-ruling, retracted** ones. The live ladder is margin-based in
  `engine/autoload/dice_engine.py::degree_from_net`. Never lift a number from the capture without
  checking the code.
- **`PP-NNN` provenance is advisory** — most cited ids resolve to no register. `ED-` citations are
  validated by a blocking gate.
- `python tools/m1_acceptance.py --summary` at `571ae14`: verdict **NOT MET**, 2 rows failing; row 4
  is self-declared **DOC-DERIVED** and must never be cited as evidence a juncture runs.
