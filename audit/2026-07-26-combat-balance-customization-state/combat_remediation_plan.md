# Personal Combat — Consolidated Remediation Plan

**Status: PLAN — PROPOSED, nothing executed. HELD FOR JORDAN on the items marked ⚖.**
**Date:** 2026-07-26 · **Lane:** PC · **Subject:** `systems/combat/combat_engine_v1/` at `f447584`
**Addresses:** every combat concern raised in this arc — the balance-state report (D1–D8), the defect register
(A1–A7, B1–B13, C1–C8, D-gaps, E1–E5), the independent `fable` audit (F1–F10), and the plan's own two
adversarial passes (X1–X6, Y1–Y5).

**Nothing here changes an engine constant.** This is the ordering, the batching, and the acceptance criteria.

---

## §1 One index, deduplicated

Several IDs are the same defect seen from different angles. Collapsing them first, because remediating them
separately is how the same code path gets patched twice:

| merged item | absorbs | one-line statement |
|---|---|---|
| **M1 staff percussion** | F1, the staff half of A4 | `percussion_authority` uses CoM offset as the lever, so a centre-gripped haft derives **exactly 0** authority regardless of mass |
| **M2 thrust-arm heft** | F2, the ranseur half of A5, part of B5/F19 | `heft` keys the lever on the head *token*, so 19 `cut_thrust` weapons are paid the **swing** moment on their **thrust** arm |
| **M3 poleaxe spike adef** | F3 | PC-5's `thrust_authority` silently broke ED-1080's "spike ≈ hammer" calibration; **plate now shields against the poleaxe** |
| **M4 raw negative cap in deficits** | F4, two of B6's four channels | `reach_threat` / `represent_measure_p` feed unclamped `adef_cap` into a capability deficit — the class ED-PC-0039 fixed only in the damage knee |
| **M5 sign-blind ability ratios** | F5, part of D6/C6 | multiplicative channel levers ratio-multiply a **signed** difference, so investment backfires when behind |
| **M6 native cut ungraded** | A7a, A3, part of B2/F21 | `core.coupling` ignores `eff` for `straight_cut`/`curved_cut`: **16 weapons, 31% of the roster, couple identically regardless of edge** |
| **M7 mode selection pathologies** | A7b, B1/F24, part of M3 | `select_mode` picks heads that cannot wound, flips identity on a 2.2% margin, and never prices the adef consequence |
| **M8 saturation flat-tops** | F7, F8/B9, B10, B11 | derived orderings computed then discarded by clamps: parry 36/53 identical, tempo 38/53 clipped |
| **M9 unreachable authored content** | F6, part of A1 | `percussion_element_authority ∝ |x|/Lt` zeroes any guard-mounted element; hook_sword's authored blunt mode can never fire |
| **M10 off-hand absence** | A6, A2, part of A1 | no shield/buckler/targe and no off-hand slot; three weapons measured in a configuration they were never used in |
| **M11 weapon data integrity** | F9, sparr_axe in A4, jian/tsurugi in A5 | `extent_m` inconsistent within a class; 13 records protrude past `head_len`; sparr_axe cannot defeat any armour |
| **M12 dead surface + doc drift** | F10, E1–E3, B12 | dead keys leaking into the Godot contract (3rd recurrence), comments contradicting adjacent code, two stale docs |
| **M13 build-layer** | D1–D8/C1–C8 | weapon dominance, free armour, monotone disposition, inert focus/tradition/abilities, no tactical layer |
| **M14 absent subsystems** | carry context, multi-combatant, chargen economy, terrain | design-scale gaps, not defects |

---

## §2 The split that governs everything: defect vs design call

Mixing these is how a remediation pass turns into an unratified balance change.

**DEFECTS — the code contradicts its own stated contract. No design input needed.**
M1, M2, M3, M4, M5, M9, M11 (protrusions), M12.

**⚖ DESIGN CALLS — Jordan's, and the plan must not pre-empt them.**

| # | call | why it is not mine |
|---|---|---|
| ⚖1 | **M6 direction:** re-anchor `CUT_AUTH_REF` (coupled to the incidental-cut path) or a non-saturating form | either buffs keen curved swords and nerfs dull ones — a balance change |
| ⚖2 | **M13/D2:** should armour cost the wearer, and in what channel | mass/tempo/stamina/mobility all plausible, all absent |
| ⚖3 | **M13/D3:** is disposition a genuine trade or is aggression simply good | code and its own comment disagree |
| ⚖4 | **B7:** is 38/53 non-participation at plate correct | "defensible and historically recognisable" per ED-PC-0040 |
| ⚖5 | **M14 carry context:** scene taxonomy, and whether scene-tagging gets commissioned (X2) | cross-lane; the balance frame becomes conditional on a content mix |
| ⚖6 | **M10 scope:** is the off-hand in scope for personal combat, at what priority | subsystem-scale |
| ⚖7 | **M7:** is the roster-wide thrust-lean wanted at all | already open from ED-PC-0027/0028; A7b is that question answered as data |

---

## §3 Batches

**Rule binding every batch, from this lane's own history:** one concern per commit; each ships a **guard**
(ED-PC-0040: *if you cannot write the guard you have not understood the pattern*); each states its **Godot
export impact** (§17 of the proposal — all 226 params are exported); each discloses golden diffs rather than
regenerating to green. **The last two same-commit "while I'm here" fixes are why batches 4 and 5 both
half-stood.**

### Batch R1 — correctness, no balance intent *(no ⚖ needed; start here)*

| item | change | guard it must ship |
|---|---|---|
| **M5** | stop ratio-multiplying signed differences in `bind_sigma` / `reach_sigma` | a test that equips the lever on the **disadvantaged** side and asserts the term does not worsen — parameterised over every multiplicative lever, so new ones inherit it |
| **M4** | apply ED-PC-0039's `max(0, cap)` at both σ-path deficit sites | assert the three deficit consumers agree on a clamped input |
| **M12** | delete `CHOKE_GRIP_MIN` + the unread physics constants; fix `wrapper.py:134`'s comment | **a CI check that every exported CFG key has ≥1 live reader** — this class has now been cleaned three times, so the third fix must be the last |

R1 is the highest value per unit of risk in the whole plan: three real defects, no balance intent, and M5 is
currently making the investment system *punish* investment.

### Batch R2 — the zeroes *(things that should work and do nothing at all)*

| item | change | guard |
|---|---|---|
| **M1** | give the authority lever a tip-lever term for centre-balanced hafts (the per-element `|x|/Lt` form already exists) | assert **no roster weapon with mass > 0 derives 0 percussion authority**; pin the staff's stagger as non-zero, since its own docstring cites it as the worked example |
| **M9** | same lever-form defect one layer down: a guard-mounted element must not zero | assert every **authored** `mode_element` is reachable by `afforded_heads` for at least one legal configuration |

M1 and M9 are the same root cause (a lever form that returns 0 at x=0) at two scales. **They are still two
commits** — M1 moves damage roster-wide, M9 only un-hides a mode.

### Batch R3 — the calibration break

| item | change | guard |
|---|---|---|
| **M3** | re-anchor `ADEF_POINT` or exempt the blunt-composite spike from `tauth`; **re-verify the comment's claim rather than the comment** | assert `adef_cap(poleaxe, spike) ≥ ADEF_THRESHOLD['heavy']` — the ED-1080 intent, made mechanical instead of a prose claim |
| **M2** | split the heft lever on the **resolved arm** (`sel_dmg=='puncture'`), not the token | assert `heft(w, thrust-resolving) ≈ heft(w, 'point')` across all 19 `cut_thrust` weapons |

Both move damage. **R3 is where the reference tables start moving**, so every commit regenerates
`combat_armour_reference.json` with the diff as the disclosure.

### Batch R4 — grading ⚖1 *(blocked on Jordan)*

**M6** (native cut ungraded) and **M8** (saturation flat-tops). Both restore an ordering the engine already
computes and throws away. M6 needs ⚖1 first. M8's `MAX_TEMPO_PEN` fix has a known shape (surgical over-cap
tail) and a known cost (`r3_identity_golden.json` must be hand-reproduced — no generator exists).

### Batch R5 — mode selection

**M7.** Largest golden blast radius in the plan and it interacts with R3 and R4 (M3's finding that the
comparator never prices adef is an M7 sub-item). **Deliberately last among the resolution batches**, and it
carries ⚖7.

### Batch R6 — structure *(⚖6)*

**M10** off-hand slot. Cheap entry: `core.COVERAGE_GAP['partial']` is fully plumbed and **has no live caller**
— the shield's damage hook already exists and is merely unreachable. Proposal §13 is the spec.

### Batch R7 — data *(⚖ partly)*

**M11.** Protrusions and `extent_m` consistency are defects; sparr_axe's missing armour-defeating mode and
cinquedea's purpose are content/design.

### Batch R8 — build layer and beyond

**M13**, **M14**, and the proposal's own increment ladder (§15). **Gated by the proposal's §9 blocking claim:
a modulation layer built before weapon dominance is resolved will measure as inert, exactly as the ability
layer already did.**

---

## §4 What this plan deliberately does NOT do

- **It does not re-tune off-plate reach.** Proven not reachable by lever (four swept; breaks `guisarme@heavy`).
  It needs a closed-phase model rework, which is its own project.
- **It does not touch the resolver** (ED-900/904) or `UPSET_FLOOR` (a designer rule).
- **It does not bundle.** Every merged item above is at least one commit; several are more.
- **It does not pre-allocate IDs.** PC `next_free = 41`, recorded; allocate at point of use.

## §5 The honest state of the evidence

- **Everything in R1–R3 is independently verified** — either measured by me with a falsifier, or reported by the
  blind `fable` audit and then **re-run by me** (M1, M3, M5 were re-verified; M2, M4 were not re-run and are
  carried at the auditor's confidence).
- **`wrapper.py`'s mutation ordering, RNG sequencing and burst/latch machine remain unaudited** — the fable pass
  spot-checked only. **Defect classes like stale `sel_*` carryover and draw-order divergence would live there,
  and no batch above covers them.** That is the largest known blind spot in this plan.
- **290 combat tests are green with F1–F6 all present.** The suite is a shipping gate, not a belief gate; every
  guard named above exists because the current suite cannot see these.
