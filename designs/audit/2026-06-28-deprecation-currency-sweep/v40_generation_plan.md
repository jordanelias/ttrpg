# Valoria — v40 Generation Plan (clarity, not a rename)

> **Status: WORKING PLAN — for Jordan.** Companion to `deprecation_currency_plan.md`. Decision taken
> (2026-06-28): carry **v40 as a declared generation + enforced currency markers**, NOT a filename
> rename (Layers 1 + 2 below). Every step is Jordan-vetoable.

## 1. What "v40" means

v40 is a **generation milestone**, not a version suffix on files. It names the leap the corpus already
made past the v30 per-system flatten:

- universal **Key substrate** (PP-687) — every system emits/consumes Keys on one bus
- **contracts spine v3** (schema-2, ED-1008) + **descriptor registry**
- **combat-engine ratification** (`combat_engine_v1`, ED-900–904) + D1–D9 (ED-1029)
- **master-workplan v4** orchestration (the single three-lane register)

So: **v40 = the consolidated, contracts-bound, Godot-ready generation.** That is worth a generation
number. The `_v30` filenames stay.

## 2. Why not rename the files (the measured blast radius)

A literal `v30 → v40` rename touches: **138 files**, **~16,000 `_v30` string occurrences** (8,721 in
live `designs/`, 3,950 in `tests/`+`sim/`, 2,063 in `references/`, 524 in `canon/`), **64 SHA-pinned
docs** (each rename changes a path-derived `canonical_sha__*_v30_md` key and forces a `freshness_gate`
re-pin), and **45 `_v30.md` filenames cited in the append-only `canon/editorial_ledger.jsonl`** — whose
references *cannot* be rewritten without falsifying the history of record.

And it would not even deliver clarity: a filename never tells you whether a doc is current (`combat_v30.md`
is partially-live; `combat_v32_proposal.md` is dead — same suffix family). Renaming just moves that
ambiguity to a new number and stops nothing from adding a stray `combat_v42_proposal.md` next month.
**The currency signal belongs in an enforced marker, not a filename.**

## 3. What the corpus actually looks like (dry run, 2026-06-28)

`tools/ci_generation_consistency.py` over `references/canonical_sources.yaml`:

- **91 canonical design docs** form the v40 surface.
- A `## Status:` convention **already exists** but is **inconsistent**: `CANONICAL`, `WORKING DESIGN`,
  `DESIGN`, `REFERENCE`, `PROVISIONAL`, and **34 docs with no Status line at all** (mostly `_index`/
  `_infill` co-files, plus real docs: `npc_roster_v30`, `military_layer_v30`, `solmund_v30`,
  `thread_horizontal_integration_spec`, …).
- **1 currency drift:** `designs/scene/combat_v30.md` is canonical **and** a `superseded_id` (the
  partial-supersession — RESOLUTION layer dead → `combat_engine_v1`, lore retained). Expected, but it
  must be explicit (banner the dead section; keep the file).

The disease behind v30/v32 proliferation is exactly this: **currency is implied, not enforced.** v40
fixes the disease, not the symptom.

## 4. The plan — Layers 1 + 2

### Layer 1 — Declare & tag  *(done on this branch)*
- `CURRENT.md` promoted to the **Generation v40** index (header declares what v40 is).
- Cut `git tag v40.0` at the consolidation commit once Layer 2 lands (so the tag points at a clean state).

### Layer 2 — Enforce currency  *(gate done; normalization staged)*
- **`tools/ci_generation_consistency.py`** (this branch, **warn-only**, wired into `valoria_local.py`):
  asserts every canonical doc (a) exists, (b) carries a recognized `## Status:` line, (c) is not a
  `superseded_id`. Same "land report-only → flip blocking" pattern the other gates used.
- **Status vocabulary** (normalize to these): `CURRENT` (canonical head, generation v40) · `PROVISIONAL`
  (pending ratification) · `WORKING DESIGN` (live, pre-compile) · `REFERENCE` (live support) ·
  `SUPERSEDED` (→ pointer; lives in `archives/`/`deprecated/`).
- **Normalization pass (staged):** stamp the **34 no-status docs** with the right Status line and
  normalize the rest to the vocabulary. This is a ~34–91-file edit; **defer until the active combat +
  distillation sessions settle** (those touch combat/threadwork/faction heads — stamping now guarantees
  merge conflicts). The stamper is idempotent, so it re-runs cleanly post-merge.
- **Flip the gate to blocking** (`blocking=True` in `valoria_local.py` + add to CI) once §3's WARN count
  is zero.

## 5. Drift to resolve during normalization
- `designs/scene/combat_v30.md` — confirm the partial-supersession banner is in place (RESOLUTION → engine);
  it stays canonical for lore.
- `designs/provincial/ci_political_v30.md` — canonical with no Status line **and** a `files_to_recheck`
  target of the 250715f seizure-threshold supersession; stamp + verify it carries the probabilistic-
  declaration correction.
- `designs/provincial/faction_politics_v30.md` — canonical but the open **J-5** merge-vs-`faction_state`
  decision; stamp `PROVISIONAL` until J-5 rules.

## 6. Execution order
1. *(done)* gate tool + `valoria_local.py` wiring + `CURRENT.md` v40 header + this plan → commit on
   `chore/deprecation-archive-2026-06-28`.
2. *(after active sessions merge)* run the normalization stamper over the 91-doc set; resolve §5 drift.
3. flip `ci_generation_consistency.py` to blocking; add it to `.github/workflows/valoria-ci.yml`.
4. `git tag v40.0`.

**Net:** a real, named v40 generation and an *enforced* currency guarantee — the clarity a rename can't
give — for ~a day of work, zero filename churn, and no damage to the historical ledger.
