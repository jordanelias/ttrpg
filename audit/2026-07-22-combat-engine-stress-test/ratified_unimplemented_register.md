# Ratified-but-not-implemented register (2026-07-22)

**Purpose.** A single index of work that was **ratified / RULED / landed as a plan-of-record** but whose **code
or artifact implementation is missing or incomplete**, and which **remains relevant** (not later superseded).

**Why this exists (the prevention motive).** This session repeatedly "discovered" things the corpus had already
diagnosed and ratified — most sharply, I reported the half-sword name-table + dead `can_halfsword_thrust` as a
*novel* finding when it is exactly **audit G3 / plan P3 / consolidation JD-3** (ratified 2026-07-04), un-wired.
The repo has an observability surface for **unratified** work (`PROPOSALS.md`, via
`tools/observability/build_proposals.py`) and for **marker debt** (`DECISIONS.md`), but **no index of the dual
case — ratified yet unbuilt** — so these items are invisible unless you already know they exist. That blind spot
is the root cause; see **§Prevention**.

**Status legend:** `NOT STARTED` · `PARTIAL` (formula/data built, not wired live) · `BLOCKED` (needs a named
prerequisite) · `NEEDS-JORDAN` (a ratified default exists but the expansion is a held-back call).

---

## PC — Personal combat (verified against code this session)

Sources: `audit/2026-07-04-weapon-morphology-granularity/{audit_v1.md,consolidation_v1.md}` (RATIFIED
plan-of-record per `CURRENT.md`), `registers/handoffs/HANDOFF_PC.md`, `registers/editorial_ledger_pc.jsonl`,
the accepted-red tests in `tests/valoria/test_combat_*.py`.

| # | Item | Ratified where | Requires | State | Evidence |
|---|---|---|---|---|---|
| PC-1 | **Emergent half-sword via `grippable`/ricasso** | audit **G3** + plan **P3** + **JD-3** (2026-07-04) | `elements[].grippable=True` on ricasso zones; `affords_halfsword(w)=(∃ grippable fwd element)∧can_halfsword_thrust(cv,pc)`; retire `HALFSWORD_FORM`/`HALFSWORD_BASE` as behaviour gates; land **byte-identical at {longsword, estoc}** | **NOT STARTED** | `weapons.py:864 HALFSWORD_FORM={'longsword','estoc'}` still a live name-table; `geometry.can_halfsword_thrust` **dead** (bake computes `geo['halfsword']`, zero readers); no `grippable` field or `affords_halfsword` in code |
| PC-2 | **Half-sword roster expansion** (which attested ricassos grant a form) | **JD-3** (default: parity only) | after PC-1 lands, flip `grippable=True` for flamberge/greatsword (attested ricassos) → new anti-plate capability | **NEEDS-JORDAN** (blocked on PC-1) | ricasso attested in data: `weapons.py:111` greatsword "with ricasso, often flanked by parrying lugs"; `weapons.py:690` flamberge ricasso mass element |
| PC-3 | **Live-wire JD-4 (reversed-grip/Mordhau) + JD-9 into `element_afforded`** | **ED-PC-0009** (JD-4/JD-9 DETERMINED 2026-07-08) | add the weak reversed-grip percussion + graded cut/point as competing selection tokens | **PARTIAL / BLOCKED** | formula built + tested (`weapon_physics.reversed_grip_percussion`; `tests/valoria/test_combat_reversed_grip.py`) but **not wired live** — blocked on a `core.coupling` fix (DELIVERY doesn't scale with percussion magnitude except vs mail/plate) per consolidation §"U2 scope note" |
| PC-4 | **ED-PC-0012 — secondary-point `THRUST_AUTH_REF` fix** | ED-PC-0012 (open, "known, documented, load-bearing residual") | scale `DELIVERY['point']` by the candidate's own thrust magnitude (as `CUT_AUTH_REF` does for 'cut'); expected to remove the sabre/scimitar/falchion spurious plate-switch | **NOT STARTED** (deferred) | `test_combat_invariants.py::test_use_mode_selection_emerges_from_primitives` lists sabre/scimitar/falchion as FLAGGED changers pending this fix |
| PC-5 | **PHASE-C — reach-class / mass-model / poleaxe-spike recalibration** | tracked accepted-red; deferred pending Jordan target bands | armour-conditional approach stop-hit (spear/yari), poleaxe spike-vs-plate, PoB_frac normalization (heft-ordering) | **BLOCKED (design call)** | accepted-red `test_gap_game_poleaxe_spikes_plate`, `test_falsifiable_heft_ordering`; see this session's Phase-C investigation — needs target win-rate bands |
| PC-6 | **R3 slices U3–U9** (edges-data JD-2, grip-physics, renderer JD-8, T-P2/T5) | consolidation_v1.md (RATIFIED plan-of-record) | the remaining execution tranches after U0/U1/U2 | **NOT STARTED** | HANDOFF_PC: U0/U1 done, U2 live (formula only); U3–U9 unexecuted; JD-8(b) renderer rebuild pending (scratchpad script confirmed lost) |

**Note (not RBNI, but adjacent):** the **half-sword *liability*** finding (the switch is a net loss where enabled)
is a *new bug*, not ratified-unimplemented — but it means PC-1's byte-identical expansion would propagate a broken
mechanic, so PC-1 and PC-5 should land together, not PC-1 alone.

---

## SC / IN / GO — (populating from corpus sweep)

_pending subagent verification_

## MB / FA / WR / FI / SE — (populating from corpus sweep)

_pending subagent verification_

---

## Prevention — why key aspects were missed, and the systemic fix

**Root cause.** There is no observability surface for *ratified-but-unbuilt* work. The repo generates
`PROPOSALS.md` (unratified/open items, `tools/observability/build_proposals.py`) and `DECISIONS.md` (marker-level
debt), but the **dual** — *decided, not yet built* — has no index, so it is discoverable only by someone who
already read the specific audit. Every "I found X" this session where X was already ratified traces to this gap.

**Fix (proposed, systemic — the durable prevention):**
1. **This register becomes a generated surface.** Add `tools/observability/build_ratified_unimplemented.py`
   (sibling of `build_proposals.py`, reusing `obs_core.py`) that scans three machine-readable signals and emits
   this register automatically, so it can never silently drift:
   - **accepted-red tests** whose docstrings carry a deferral tag (`[PHASE-C FLAG]`, `DEFERRED`, `not silently
     patched`) — each is a ratified expectation the code doesn't yet meet;
   - **ledger entries** ratified (`status: ruled`/`ratified`) but carrying an `implemented: false` (or an
     `unwired`/`deferred` note) field — **requires adding a small `implemented` boolean to the ledger schema**;
   - **plan-of-record JD/U items** marked with a ratified *default* but no execution record.
2. **Search discipline (immediate, no tooling):** before labelling any finding "novel", grep `audit/` +
   `registers/editorial_ledger*.jsonl` for the mechanism keyword (here: `halfsword`, `ricasso`, `grippable`).
   This session's miss would have been caught by a single `grep -ri ricasso`.
3. **Anti-orphan gate for the geo surface.** The dead `geo['halfsword']` slipped through because — unlike the
   wrapper's circumstance fields (`test_every_circumstance_field_has_a_live_reader`) — the `geometry.bake` output
   coefficients have **no reader-existence test**. Add one; it would have flagged `can_halfsword_thrust` as dead
   the day it was written.

**Net:** the blind spot is structural (no RBNI index), so the fix is structural (generate one) — not "try harder
to remember". Items 2 and 3 are cheap and land now; item 1 is the real prevention and is a small tool.
