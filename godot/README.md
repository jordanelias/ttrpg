# `godot/` — the Godot port home

Consolidated (ED-IN-0071 P2, 2026-07-16) from three former homes — `designs/godot/`,
`designs/videogame/`, and `designs/audit/2026-06-10-godot-conversion-strategy/` — into this
single top-level primary. It **is** the eventual `res://` project root. See `CLAUDE.md §6` for the
state-of-the-bridge (the conversion is **PROPOSED and largely un-executed** — do not treat the
skeleton as a runnable head-start). Old paths alias via `references/restructure_ledger.md`.

**Contents:**
- `godot_conversion_strategy_v1.md` — **the governing spec** (status **PROPOSED**, Jordan-vetoable
  throughout; the Part-VIII `[OPEN — Jordan]` register is the veto surface). Details below.
- `godot_architecture_specification.md` — the Godot architecture specification (formerly under
  `designs/videogame/`).
- `skeleton/` — the illustrative, non-compilable `personal_combat` slice (1 of 27 modules).
- Four **stale** pre-`d+σ` docs (`scene_tree_architecture.md`, `gm_to_engine_conversion.md`,
  `data_serialization_spec.md`, `implementation_sequence.md`, all 2026-04-18) — each carries a
  `⚠️ STALE / PARTIALLY SUPERSEDED` banner. Do not implement from them; defer to the strategy doc.

---

## `godot_conversion_strategy_v1.md`

**What it is:** the execution spec for the approved Godot epics (master workplan W4.1–W4.3) and the Workplan-R2 Phase E per-system ritual. It consolidates the 2026-06-06→10 architecture work (Key substrate, kernel/3-regimes, 27 module contracts + adjudicator, Descriptor Registry, the per-system flatten wave) into: a three-leg inventory (design corpus / valoria-game / sim armature), an explicit per-module conversion disposition for all 27 contracts (waves S/1/2/3/4/R), the valoria-game drift census (D1–D8) against the 2026-05-04 sync point, the four directional laws the converted game must preserve, the Python→Godot construct dictionary with the determinism/parity protocol (named draws · recorded-draw replay · Key-log equality), gated sequencing (Gate-0 → spine → per-module ritual → cross-scale), the frictions register (R1–R10), and the consolidated open-decision set.

**Supersedes in part:** `godot/implementation_sequence.md` (G1–G7 phasing) and the framing of `godot/data_serialization_spec.md`. `scene_tree_architecture.md` and `gm_to_engine_conversion.md` remain valid as amended in Parts III–IV.

**Companion state:** valoria-game frozen since 2026-06-06 (design sync 2026-05-04 @ `9057663f`); first action items are Gate-0 G0.1 (Key schema v2) and G0.2 (Godot-doc consolidation) per Part IX.
