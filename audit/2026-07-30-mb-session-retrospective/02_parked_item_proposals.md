# Proposals for every parked item

**Date:** 2026-07-30 · **Lane:** MB · **ED:** ED-MB-0061
**Sources:** `00_lessons.md` (S1–S7, Track F), `01_pc_facing_model_fix_plan.md` (§7 R0–R8, §8 D1–D9, §9–§10 rulings)

## Status: PROPOSED (merge ratifies per ED-1094 — each item below states what merging it decides)

---

Every item Jordan was asked to rule on now carries a **recommendation with a rationale and a
falsifier**, so a ruling is an accept/reject rather than an open design question. Where I recommend
something the evidence cannot yet settle, I say so and name the measurement that would.

---

## P-1 — The golden mode matrix · **blocks the re-base**

**Problem.** `PC_CELL_MORALE` is simultaneously a game flag and a golden **mode selector**. At
default-ON, `_mode_key` appends `_cm` to all four base modes, so they key as `unit_cm` / `cell_cm` /
`unit_field_cm` / `cell_field_cm` — and `MODES['cell_cm']` (PER_CELL=1, FIELD=0, CM=1) collides with
what `cell` now produces.

**Options.**
- **(a) Drop the flag from the mode key; pin it in `FIELD_PINS` at its shipped value.** Four modes,
  one configuration — the shipped one.
- **(b) Keep the key; re-name the four base modes to their `_cm` forms and retire the old `cell_cm`.**
  Four modes, all at CM=1, names change.
- **(c) Keep both axes: eight modes** (each base mode × CM on/off).

**Recommendation: (b).** ⚠ This reverses ED-MB-0053, which I executed eight hours earlier, so state
the reason plainly: §4a added `PC_CELL_MORALE` to the key because the four modes all ran at CM=0 and
therefore verified float-order over every per-cell map *except* the three that matter. **The flags-ON
ruling solves that problem a different way** — every mode now runs at CM=1, so the coverage gap §4a
existed to close is closed by the default, and the key no longer needs to carry the flag. (b) keeps
the *names* honest about what is measured; (a) is the same configuration with less honest labels.

**Reject (c):** it doubles a battery that already takes ~6 min/mode to verify a flag Jordan has ruled
must always be ON. Modes should span configurations we ship, not configurations we have retired.

**Falsifier:** after the re-base, `unit_cm` must differ from the retired `unit` golden. If they match,
the flag is inert in that mode and (b) bought nothing — which is exactly the check §4a's own control
applied and passed.

---

## P-2 — `CONTACT_REACH` · the one flag not turned on

**Problem.** It is a **magnitude**, not a switch (`0.0` currently), so "turn everything on" has no
mechanical meaning for it. Inventing a value is fabrication (§7).

**Recommendation: leave at `0.0` and RECLASSIFY it, rather than treat it as an un-flipped flag.**
Its own comment says `0.0 => ON contact predicate == OFF adjacency (exempt value)` — i.e. 0.0 is a
*deliberate identity*, not a disabled state. With `FIELD_CONTACT=1` the field path takes per-troop-type
`reach_for()`, so nothing is gated off by it.

**Under the circle substrate it should be retired entirely.** R4 makes reach a radius composing as
`r + reach`, with `reach_for` the single owner. A separate global scalar override is then a second
owner of one quantity (§8) and should be deleted, not valued.

**Falsifier:** grep for a live read of `CONTACT_REACH` on the field path after R4. If none, deleting
it is a no-op and the question dissolves. If one exists, it needs a ledger-backed value.

---

## P-3 — The multiplicity-penalty magnitude (D3-R1)

**Problem.** Jordan ruled *"there should be a disadvantage when having to attack/defend against
multiple cells."* The magnitude is a design number.

**Recommendation: do not pick a number — derive the penalty's SHAPE from an existing owner, then let
one parameter be fitted.** Concretely: the penalty is a **frontage split**, not a multiplier. A cell
engaged by N opponents divides its engaged frontage among them, so each exchange draws a proportionally
smaller pool — a mechanism that already exists in `_pair_engaged_troops`. Under that shape:

- 1 opponent → full frontage → parity (unchanged).
- 2 opponents → each gets ~half → the cell fights both at reduced strength, and **takes damage from
  both**. Net disadvantage emerges without a constant.

**Why this rather than a flat multiplier:** it is the ED-1083 guardrail (never special-case an
entity/outcome) and it composes with D3-R2 automatically — a corner cell splitting frontage *and*
showing an exposed YELLOW face is worse than either alone, with no interaction term to tune.

⚠ **Keep it distinct from ED-MB-0018's arc-spread shock** (see `01_…§9`), or that fix re-breaks.

**Falsifier:** a 1-v-2 exchange must show the doubly-engaged cell losing more troops per tick than a
1-v-1 cell of identical stats, with both arms at the same arc. If the split alone does not produce it,
a magnitude is genuinely needed and *then* becomes a Jordan number.

---

## P-4 — The v30 sightline conflict

**Problem.** `mass_battle_v30.md:155` specifies a **135° forward sightline with a 15-cell perception
range**. The code implements **210°** visible (`REAR_BLIND_DEG=150`, `FOV_HALF_DEG=105`) and **no
perception-distance limit at all**.

**Recommendation: the CODE's arc wins; the DOC's range limit wins.** They are two separate quantities
and the honest answer differs for each.
- **Arc:** 210° visible is consistent with the octagon partition Jordan ruled (REAR = 180°, so visible
  = 180°… ⚠ *these disagree*: 210° visible implies a 150° rear blind arc, while S6's REAR arc is 180°).
  **This is a genuine third conflict and I flag it rather than paper over it** — S6, the code, and v30
  give three different rear boundaries (180° / 150° / 225°). **Recommend adopting S6's 180°**, since
  it is the most recent ruling and is the one the arc partition is built from; the other two then
  become supersession notes.
- **Range:** the doc's 15-cell perception limit is a real mechanic the code simply lacks. An unbounded
  sightline means a cell reacts to a threat 50 cells away, which is why `assign_targets`' 'nearest'
  fires unconditionally (A2). Recommend implementing the limit.

**Falsifier:** with a 15-cell limit, a reserve subunit at the far edge must not acquire a target. Today
it does — measurable directly (H6's A3/A4 had `target=Y` at face-gap 11.8).

---

## P-5 — D4: apex-on-leading-edge vs facing-the-bisector

**Problem.** S1 pins a cell's heading perpendicular to the perimeter's leading edge; S5/D3-R2 turn the
corner cell to face the gap bisector. Both cannot hold.

**Recommendation: S1 is a DEPLOYMENT/parade property, not a standing invariant.** It describes how a
formation is *laid out* (cells abreast, apexes on the leading edge, march perpendicular). Once engaged,
cells turn — that is the entire point of the facing model — and the apex leaves the line. The perimeter
remains the surface of battle; the apex does not remain welded to it.

The critic's **Minkowski-envelope** reading is the version that survives contact: the perimeter is the
body circles' outer envelope, whose corner is an arc of the corner cell's own circle. Every apex
orientation in a fan then lies *on* that arc, so "the apex touches the perimeter" stays true through
rotation — at corners, which is exactly where it matters.

**Recommend adopting the envelope reading** and demoting S1 to "true at deployment; the envelope form
is what holds under rotation."

**Falsifier:** build the perimeter as centres-hull + 0.5 inset (R5a's closure check). If a rotating
corner cell's apex leaves that surface, S1-as-invariant is dead and only the envelope form survives.

---

## P-6 — Reach arc span

**Recommendation: FRONT only (±45°).** It matches the current front-face-only box extension, matches
"weapons reach where you are looking", and keeps reach composable as a single forward radius. Giving
SIDE reach would let a cell fight in a 180° arc, which no source asks for.

**Falsifier:** a cell with an enemy at 60° bearing (SIDE) must not engage it at reach distance.

---

## P-7 — Grid-path scope for the circle

**Recommendation: FIELD-ONLY, confirmed by structure.** `resolve_toi_and_commit` has exactly one call
site, inside `if FIELD_MOVEMENT:`. The grid path never enters it, so the circle substrate cannot touch
the frozen grid oracle. This needs no ruling beyond a confirmation — it is a fact about the call graph,
not a choice.

---

## P-8 — S4 × S7: may a cell translate laterally without turning?

**Problem.** S7 makes heading = direction of travel. S4's perimeter conditioning implies correction
motion that is *not* forward.

**Recommendation: yes, with a rate cap, and treat the two as different motions.** Heading is the
**intent** vector (where the cell fights and advances); infill is a **correction** applied in the
formation frame. A soldier sidesteps to close a gap without turning to face the gap — the distinction
is real, not a fudge. Proposed: forward motion along the heading at full speed, lateral correction
capped at a fraction of it, so a formation cannot crab sideways faster than it advances.

**Falsifier:** a formation ordered to hold with a hole in it must close the hole without its cells'
headings rotating. If closing the hole requires a turn, S7 is stricter than the design intends.

---

## P-9 — `PC_FACING_SLEW_BASE = 60` ratification

**Problem.** Explicitly tagged *"NOT ratified — do not enable"*, and the flags-ON flip made it live —
with a provenance record (`provenance.py:159-164`) that now reads false. It is **doubly** load-bearing
under S7, since heading is also travel.

**Recommendation: ratify a DERIVED value, not the placeholder.** 60°/tick·disc is round-number
provenance. A defensible derivation: a body wheeling at its own march rate turns about its pivot at
`ω = v/r` — so the slew cap should fall out of speed and formation depth rather than be asserted.
Ship the placeholder as `[CALIBRATED-DEBT:]` until derived, and **fix the false provenance record
immediately** regardless of the ruling.

**Falsifier:** at 60°/tick a discipline-5 cell completes a 180° reversal in 3 ticks. Compare against
the reform/wheel timings canon already asserts; if they disagree by >2×, the placeholder is wrong.

---

## P-10 — Retire `FACING_REACTION_TICKS`?

**Recommendation: retire it, after R2.** Two owners currently model "cells cannot turn instantly" on
different clocks — a 2-tick penalty hold and a 60°/tick state rotation. With heading as real slewed
state, the penalty should *emerge* from where the cell is actually pointing. §8's one-rule-one-owner.

**Falsifier:** with the clock removed, a flanked cell must still take elevated damage for the ticks it
spends turning. If the damage disappears entirely, the clock was carrying behaviour the slew does not
reproduce and must stay.

---

## P-11 — R8: separation of pre-existing overlap

**Recommendation: BUILD, and it becomes nearly free on circles.** F10 is real — `s > 0` prevents new
interpenetration and by construction never undoes existing overlap, so any overlap that forms persists
forever. On circles the separator is one line: push each body along the centre line by `(2r − dist)/2`.
It is symmetric, deterministic, needs no RNG and no discipline roll.

⚠ It is a **new mechanism**, not a port of the dead grid-era `resolve_internal_collisions`, and must be
gated and measured as such.

**Falsifier:** inject an overlapping pair, run one tick, assert `dist ≥ 2r`. And an activity control
(G13): the separator must not freeze anything to achieve it.

---

## P-12 — R6's final shape

**Now largely settled by Jordan's §9/§10 rulings.** Remaining content: (a) D3-R1's frontage split
keyed on **body count**, (b) D3-R2's exposed-arc determination from the perimeter. No polygon (D2),
no new multiplier (D3-R2 uses the existing 1.5×). The only open sub-question is P-3's magnitude, and
the recommendation there is that the split needs none.

---

## Summary — what a ruling decides

| # | item | recommendation | needs a number? |
|---|---|---|---|
| P-1 | golden mode matrix | (b) rename base modes to `_cm`, retire old `cell_cm` | no |
| P-2 | `CONTACT_REACH` | leave 0.0, retire under R4 | no |
| P-3 | multiplicity penalty | frontage split, no constant | **only if the split alone fails** |
| P-4 | sightline | S6's 180° rear; implement the 15-cell range | no (both exist in sources) |
| P-5 | D4 | Minkowski envelope; S1 is a deployment property | no |
| P-6 | reach arc | FRONT only | no |
| P-7 | grid scope | field-only (structural fact) | no |
| P-8 | lateral infill | allowed, rate-capped | **yes — the cap** |
| P-9 | slew base | derive from `v/r`; fix the false provenance now | **yes — or derive** |
| P-10 | `FACING_REACTION_TICKS` | retire after R2 | no |
| P-11 | R8 separation | build; trivial on circles | no |
| P-12 | R6 shape | settled by §9/§10 | see P-3 |

**Two genuine numbers remain** (P-8's lateral cap, P-9's slew rate) and one conditional (P-3). Every
other parked item resolves to a structural argument or an existing source.
