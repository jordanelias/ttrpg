# MB session retrospective — lessons, adversarial pass, and plan corrections

**Date:** 2026-07-30 · **Lane:** MB · **Session:** 2026-07-29c, merged as `94bb902` (PR #271)
**Governs:** `audit/2026-07-26-mass-battle-fable-audit/{02_remediation_plan,03_execution_plan}.md`

## Status: PROPOSED (merge ratifies per ED-1094, EXCEPT §4's Jordan forks)

---

## §0 — Why this document exists

The session executed most of execution-plan v2's Track A, landed three EDs, took a ruling that every
mechanic defaults ON, and **left `main` CI-red with 16 failures**. Two independent read-only critic
passes overturned material claims *after* they were committed.

The plan already carries twelve guardrails (`03_execution_plan.md` §1), each written from a specific
prior failure. **This session broke new ground: it produced failure modes G1–G12 do not cover.** The
guardrails below are numbered to continue that series and are written to the same standard — each
names the specific mistake that produced it, and the task it now guards. A restated principle is
useless (CLAUDE.md §0.1's own opening); specificity about *what to attack* is the whole of the fix.

---

## §1 — New guardrails, G13–G21

| # | Guardrail | The failure that produced it |
|---|---|---|
| **G13** | **If doing nothing scores well on your metric, the metric cannot validate a change. Every improvement number ships with an ACTIVITY control.** | The exclusion pass was reported at "17.31% → 0.35% overlap". The 0.35% arm had **deadlocked the engine** — cells were not overlapping because they were not moving. Overlap is a metric a null system trivially wins. G6 says "attack the setup"; it does not name the degenerate-solution case, which is the one that bit. **Guards: every §6 Track D measurement, D1's arms, D5.** |
| **G14** | **Decompose a performance regression into (cost per iteration) × (iteration count) before optimising. A new gate that slows the engine has changed BEHAVIOUR until proven otherwise.** | An 8.2× slowdown (47s → 386s) was diagnosed as pair-solve cost. A swept-AABB broad phase was designed, implemented and verified exact — and bought nothing (386s → 370s), because the defect was an **8.05× rise in tick count** (1,482 → 11,934 resolve calls), not per-pair work. A correct optimisation for a problem that did not exist. **Guards: any task adding a per-tick gate — B1a, B3, D2.** |
| **G15** | **A retraction is a grep, not a sentence. Sweep the tree for the retracted value; mark every surviving site.** | ED-MB-0060 retracted the "17.31%" figure — and the *same commit* wrote it into two NEW source comments (`hierarchy/units.py`, `config.py`), with three further live assertions elsewhere. A retraction that does not sweep re-seeds the number it withdraws. **Guards: every retraction; E-track editorial.** |
| **G16** | **Mutation-verify against DELETION of the whole feature, not perturbation of one line. If deleting the gated block passes, the guard tests nothing.** | `test_cell_exclusion_no_deadlock.py` was shipped "mutation-verified". It killed the one planted mutant — by accident of the fixture's 8.1° bearing. A critic found **two survivors**: deleting the entire `if PC_CELL_EXCLUSION:` block, and weakening the filter to `s <= 0.5`. The guard could observe the skip branch and never the pass's positive behaviour. G2 requires a guard that *can* fail; it does not require that it fail *on absence*. **Guards: every new test (extends G2).** |
| **G17** | **A falsification is only as good as its operationalisation. Write down the quantity the hypothesis predicts BEFORE measuring, then check the measured quantity is that one.** | The hypothesis "same-subunit overlap is an artefact of per-cell rotation" was recorded as FALSIFIED because 100% of overlapping pairs had identical facing. The relevant rotation is box-vs-**separation direction**, not box-vs-box. The measured depth distribution is quantitatively *consistent* with the hypothesis it was used to reject. A hypothesis wrongly filed as dead is worse than one left open. **Guards: D1, D3, every falsifier §0.1 #3 demands.** |
| **G18** | **Measure with the engine's own predicate. Inventing a distance or threshold to decide "engaged"/"overlapping" creates a second owner of that rule, and it will disagree.** | Engagement was measured by **centroid-to-cell distance** while the engine decides contact on **oriented faces and normals** (`core/contact.find_contacts`, `obb_front_reach_overlap`). A 50-cell body's centroid sits ~5 units behind its own front face, so every reported gap was inflated. Separately `measure_colocation._depth` projects onto only the FIRST body's frame — wrong for differently-faced pairs, and can return negative for a pair `obb_overlap` just certified. Violates §8's "every rule lives once". **Guards: C-track observability, D5, D6.** |
| **G19** | **The critic runs before the claim leaves the session, not after someone asks. A result reported without an independent read is provisional by construction.** | Both critic passes this session were run only when Jordan asked, and **both overturned committed claims**. §10 already specifies the agonist→antagonist relay and `.claude/agents/valoria-critic.md` is wired read-only with CI enforcement — the apparatus existed and was bypassed. Of the four defects that escaped into a claim or a commit, **all four** were measurement-setup errors: the class a producer structurally cannot audit in itself. **Guards: every task that reports a number.** |
| **G20** | **A test asserting a flag defaults OFF protects the oracle, not the engine. Every gated-off mechanic needs a parallel ON-mode behavioural test, or the gate is a permanent blind spot.** | Flipping 15 flags ON surfaced **nine engine defects in one commit** — rear damage `0.0` instead of 2× front, opposing bodies interpenetrating, intent-resolution inverted, `PC_FRICTION_CEV` handing one side a systematic win, and more. None was reachable by any test or audit while the flags were off. Worse, the suite contained **seven tests asserting "this flag must default OFF"**, which *institutionalised* the blindness: they made the unmeasured state the protected state. **Guards: D2, B3, and the whole flag surface.** |
| **G21** | **A standing directive is a default, not a one-time instruction. On discovering a new instance of a class already ruled on, APPLY the ruling — do not re-report it as a finding.** | Jordan ruled "all options/modules must be turned on" on 2026-07-02 (ED-MB-0001) and restated it repeatedly across this session. The session kept *reporting* flags as OFF (`PC_CLOSE_RANKS`, `PC_FRONTAGE_BLEND`, the §5.1 census) instead of turning them on, until told in capitals. Re-surfacing a settled decision as a question is a form of not doing the work. **Guards: every task that inspects a gate.** |

---

## §2 — What survived, and what did not

Both critic passes were structurally independent (read-only tools, no access to the producer's
reasoning), per §10's relay.

**Survived attack:**
- The **attribution control** on the golden re-record: running at `PC_CELL_EXCLUSION=0` reproduced
  both prior field goldens byte-for-byte, which proves the entire remainder of the changeset inert on
  both field modes — a stronger control than the claim required.
- **Grid-mode no-op**, verified structurally (single call site inside `if FIELD_MOVEMENT:`) rather
  than by digest agreement, which is the G7 failure mode avoided.
- The **deadlock diagnosis itself** (46.9% of same-side solves returning `s=0`; halted cells
  20,356 → 3,300; ticks 1,482 → 11,934) and the `s > 0` repair.

**Overturned:** the guard's sufficiency (G16), the rotation falsification (G17), the "tangent by
construction" geometry, the retraction's completeness (G15), and the `_depth` metric underlying the
−48.6% / −74.4% headline (G18).

**Consequence for canon:** ED-MB-0059's *mechanism* stands; its *headline percentages* do not. They
must be re-measured with a true SAT depth over both bodies' axes before being cited again.

---

## §3 — Issues flagged this session with no home in either plan

The two plans (`02_remediation_plan.md`, `03_execution_plan.md`) predate all of these. Routed:

### 3.1 — Engine defects exposed by the flags-ON ruling (NEW Track F)

| id | defect | evidence |
|---|---|---|
| **F1** | `PC_FRICTION_CEV` confers a large systematic ONE-SIDED advantage | mean hp A 0.9910 / B 0.8634 over 20 historical rows, 13/20 at exactly 1.0000; with it alone off, A 0.8625 / B 0.9390. Its config note claims only "shifts the RNG stream" |
| **F2** | Rear damage is `0.0`, not 2× front, under `PC_FACING_MODEL=1` | `test_octagon_damage::test_rear_is_exactly_double_front`, `seed 5: rear 0.0 != 2x front 6.0` |
| **F3** | Opposing cell **bodies interpenetrate after a commit** | `test_obb_contact_toi::test_head_on_no_interpenetration_no_stall` — undercuts the cross-side invariant ED-MB-0059 was built on top of |
| **F4** | Charge drives bodies into interpenetration | `test_obb_contact_toi::test_cavalry_charge_reaches_contact` |
| **F5** | Intent-resolution inverts its own design claim | `test_holder_survives_better_with_intent`, off 24.6 / on 24.0 |
| **F6** | Per-cell break no longer subsumes the body-level break | `test_per_cell_break_subsumes_the_body_level_one`, off 55.5 / on 40.8 |
| **F7** | Conditional orders stop firing (withdraw; own-strength) | `test_conditional_orders` ×2 |
| **F8** | DG-2 rally fails on a pressured yielding subunit | `test_dg2_yield_residuals::test_rally_keeps_pressured_yielding_subunit` |

### 3.1a — F3/F4 BISECTED (2026-07-30). Cause isolated; the exclusion pass is exonerated.

The misattribution risk was real and was raised independently by a `fable` critic, which correctly
refused the "0 class (b)" classification as unproven and supplied a concrete class-(b) mechanism:
the same-side pass caps one cell of a cross-side pair against its own neighbour while the enemy cell
keeps its full `best_t`, making stop-fractions heterogeneous and voiding the swept-SAT certificate at
`hierarchy/units.py:2169-2173`.

**The control was then run, and it refutes that mechanism:**

| arm | `test_obb_contact_toi` |
|---|---|
| `PC_CELL_EXCLUSION=1` (as shipped) | 2 failed |
| `PC_CELL_EXCLUSION=0`, all else ON | **2 failed — identical** |
| all 15 flipped flags OFF | **6 passed** |
| `PC_FACING_MODEL=0`, all else ON | **6 passed** |

So F3/F4 are **class (a)**, caused by **`PC_FACING_MODEL` alone**, and `PC_CELL_EXCLUSION` neither
causes nor worsens them. ED-MB-0059's default-ON disposition stands on this axis.

**Two corrections this bisect forces on §3.1 as first written:**

1. `PC_FACING_MODEL` accounts for **exactly two** of the sixteen failures (16 → 14 with it off), not
   the larger share assumed.
2. **F2 (rear damage `0.0`) is NOT caused by `PC_FACING_MODEL`** — `test_rear_is_exactly_double_front`
   still fails with it off. Its cause is unidentified and needs its own bisect. The plausible-sounding
   story (a half-sector octagon rotation under the facing model) is exactly the kind of mechanism that
   should not be believed without the control — G17.

⚠ **Still unresolved for the whole 16:** each remaining failure needs its own single-flag bisect
before being called class (a). The classification is now proven for F3/F4 only.

### 3.2 — Spatial-integrity residuals (extend Track B)

- **F9** — the collision solve is **enemy-gated**: `toi_deferred = FIELD_MOVEMENT and
  enemy_cells_float`, so same-side exclusion inherits a cross-side precondition it has no reason to;
  formations with no enemy supplied interpenetrate freely.
- **F10** — **nothing separates already-overlapped bodies.** `s > 0` prevents new interpenetration
  and by construction never undoes existing overlap. `resolve_internal_collisions` (ED-MB-0057,
  still dead) is the only primitive ever built for it, and it is intra-subunit + grid-era.
- **F11** — **a formation whose facing is off its lattice axis is self-interpenetrating by
  construction**, at depth `1 − cos θ`, because offsets are laid out on the row/col frame while
  boxes orient along the facing. This is a substrate design question, not a bug to patch: either the
  body box shrinks, or the lattice pitch grows, or exclusion is defined on a different volume than
  the contact box.
- **F12** — **node cohesion fails on unengaged units.** Measured H6 t=24: B3 at face-gap 5.68 has
  packing 0.606 and facing rotated 33° off-axis; frozen A3/A4 hold exactly 1.000. Mean
  nearest-neighbour distance falls to ~0.68 (below pitch) *while* the bounding box grows — clumping
  with voids, not spreading. Jordan's design statement is the spec: *"subunits should be
  conditioning the cells to be aligned accordingly and consequently move accordingly"*, and cells
  *"should automatically be collapsing/shrinking for a closest fit/infill relative to points of
  engagement"*.
- **F13** — deployment gives **zero inter-subunit gap**: H6's B0–B5 sit 5 apart at ~5 wide, edge to
  edge. Jordan: *"each column of units would be spaced slightly so as to increase their ability to
  manoeuvre."*

### 3.3 — Instrument and hygiene debt (extend Track A/C)

- **F14** — `test_cell_exclusion_no_deadlock.py` is near-vacuous (G16). Rebuild so deletion of the
  gated block fails it.
- **F15** — `measure_colocation._depth` biased (G18). True SAT depth over both bodies' axes; then
  re-measure ED-MB-0059's headline.
- **F16** — `core/contact.py:161` asserts *"Co-location is now geometrically impossible on the field
  path"* — refuted by this session's own 875 cross-side measurements.
- **F17** — seven superseded "must default OFF" policy tests. Per G20 each becomes an ON-mode
  behavioural test; the inert-when-off content stays valid run with the flag explicitly off.
- **F18** — `CONTACT_REACH` is the one flag left at its OFF value because it is a **magnitude, not a
  switch**. It needs a canonical value from the ledger or an explicit ruling that 0.0 is correct.
  Inventing one is fabrication (§7).
- **F19** — **`main` is CI-red.** Until cleared, no other lane can distinguish a real regression from
  the known 16.

---

## §4 — Corrections to the two plans

### 4.1 — The structural problem: both plans are built around an oracle that no longer exists

`03_execution_plan.md` is organised around protecting byte-exact goldens — G11 ("one golden-moving
PR in flight, globally, ever"), the A1a gate, the single golden-moving slot. **The flags-ON ruling
invalidates that architecture for one transition:** every mechanic changed at once, so every digest
moved at once, and G11 cannot be satisfied by serialising.

G11 is not wrong; it is **suspended for exactly one event and then resumes**. The plan needs an
explicit re-base phase that G11 does not apply to, with the re-base itself as the single global
golden-moving PR.

### 4.2 — NEW Phase 0, which gates everything remaining

The existing critical path (`A1a → A1b → §4a → B1a → B1c → D1`) is **no longer executable as
written**: B1a and D1 both need a stable oracle, and there isn't one.

```
F3/F4 bisect vs PC_CELL_EXCLUSION ──► GATE (decides ED-MB-0059's disposition)
      │
      ├─ F1 friction asymmetry · F2 rear-damage-zero      [live engine bugs, fix before re-base]
      ├─ F5 · F6 · F7 · F8                                 [defect triage, may be pre-existing]
      ├─ F14 rebuild the guard (G16) · F15 fix _depth (G18) · F16 · F17 (G20)
      │
      ▼
Jordan fork: the GOLDEN MODE MATRIX. PC_CELL_MORALE is now both a game flag and a mode
selector, so at default-ON the four base modes key as *_cm and MODES['cell_cm'] collides
with 'cell'. Cannot be resolved by a session.
      │
      ▼
RE-BASE all digests at all-flags-ON, once, as the single global golden-moving PR (G11 resumes after)
      │
      ▼
then the existing plan resumes:  B1a → B1b → D1 → D2/D3/D5
```

**Rationale for the ordering, and it is the whole point:** re-basing the oracle *before* fixing F1–F4
would **bake nine defects into the definition of correct**. A golden is a record of behaviour; record
it while the engine is wrong and every later change is measured against wrongness. This is G13 at
the level of the oracle rather than a single metric.

### 4.3 — Amendments to specific plan items

| plan item | correction |
|---|---|
| **§9 ORDER / critical path** | Replaced by §4.2. `A1a` is satisfied but its *premise* (goldens are the stability anchor) is void until the re-base. |
| **G11** | Add: "suspended for the single all-ON re-base event, which is itself that PR; resumes immediately after." |
| **§2 HARD RULE 3** ("every fix ships a mutation-verified guard") | Strengthen with G16: mutation must include **deleting the feature**, not only perturbing it. Rule 3 as written is what `test_cell_exclusion_no_deadlock` satisfied while testing nothing. |
| **§2 HARD RULE 4** ("goldens moved ⇒ publish the delta") | Add the attribution control as mandatory: re-run with the changing flag OFF and show the prior golden reproduces. That control is the one thing this session did that survived both critics. |
| **§10 ORCHESTRATION** | Add G19: the critic is **scheduled**, not discretionary — dispatched before the result leaves the session. This session's apparatus existed and went unused. |
| **D5 casualty realism** | **Promote to blocking.** Already "understated badly" in v1; at all-ON it is worse — mean end-state hp 0.9272 combined, with rows at exactly 1.0000. An engine where a 24-tick battle between 6,500 and 9,900 men costs <2% is not a balance question, it is a broken resolver. |
| **B3 "wire or delete the dead machinery"** | Now partly ruled: the flags-ON directive *is* the disposition for every gated-off mechanic. `resolve_internal_collisions` (F10) and `_reach_throttle` remain, since they are unwired code rather than gated code. |
| **§6 fork "two mass-battle trees"** | Reinforced by measurement: `systems/mass_battle/sim/massbattle.py` (1,905 lines) has **zero** occurrences of `resolve_toi_and_commit` or `PC_CELL_EXCLUSION`. The restructure relocated an older, different engine and left the live one at `tests/sim/mass_battle/`. Every fix this session landed in one tree only. |

### 4.4 — What `02_remediation_plan.md` needs

Its §0 frame — *"three mechanisms are silently changing battles already, and the engine cannot
currently tell you why any battle ended the way it did"* — is **confirmed and understated**. The
flags-ON pass raises the count from three to at least twelve. Its surface inventory should absorb
Track F wholesale, and its "silently distorting outcomes today" list should lead with F1
(`PC_FRICTION_CEV`), which distorts *who wins* rather than by how much.

---

## §4.5 — AUTHORITATIVE GEOMETRY SPEC (Jordan, 2026-07-30, two hand diagrams)

Recorded verbatim as canon input because it **contradicts what the code does** and is the spec any
`PC_FACING_MODEL` fix must satisfy. Not yet reconciled with `mass_battle_v30`; that is E-track work.

**S1 — The facing octagon is POINT-FORWARD, not face-forward.** *"the facing octagon is rotated such
that a point is what touches the subunit facing line."* Diagram 1: a cell body (blue), the two
forward-oriented octagon faces (red) meeting at a vertex, and that **vertex** contacting the
subunit's face line (black). So the octagon carries a ~22.5° rotation relative to a face-forward
octagon, and the leading feature is a **vertex**, with two faces flanking it.

⚠ If the code builds arcs face-forward, every sector is displaced by half a sector and front / flank
/ rear are all mis-assigned. That was the leading hypothesis for F2 (`rear 0.0 != 2x front 6.0`) —
**and the bisect refutes it as the sole cause**, since F2 survives `PC_FACING_MODEL=0` (§3.1a). The
orientation defect may still be real and separately consequential; it is no longer an explanation
for F2. G17: state the predicted quantity, then check the measurement is of that quantity.

**S2 — The subunit has a PERIMETER, and it is the surface of battle.** Diagram 2: a 3-cell subunit
drawn as three cells abreast inside a single black perimeter, with the march direction (green arrow)
**perpendicular to the perimeter's long axis** — i.e. the subunit advances broadside, frontage
leading. Each cell's octagon vertex touches the perimeter's **leading edge** from inside.

Consequences the tree does not currently implement:
- The subunit perimeter is a derived first-class object (frontage × depth envelope of the cells),
  and it — not the individual cell boxes — is what a facing line means.
- *"The surface of battle between units is the boundary between their cells"* now has a precise
  reading: cells tile the perimeter; the perimeter's leading edge is the contact surface.
- This is the design answer to **F12 (porosity/clumping)** and **F13 (zero inter-subunit gap)**: if
  the subunit owns a perimeter and conditions its cells to fill it, a formation cannot go porous
  without the perimeter itself deforming, which is observable and controllable.

**S5 — THE POINT-FORWARD OCTAGON IS THE DISADVANTAGE MECHANIC. This is why S1 matters.**
Diagram 3: a friendly subunit (blue cells in a black perimeter) meeting an enemy line (purple), every
cell carrying its two forward faces. Jordan: *"you can see the corner is stuck facing between the two
purple so it's at the greatest disadvantage of the cells, and then you see the facing of supporting
cells."*

The mechanism, stated precisely:

- Engagement is **face-to-face** between octagon faces, not centre-to-centre.
- Because the octagon leads with a **vertex**, a cell at the perimeter's **corner** points its vertex
  into the *gap between two enemy cells* — so it is engaged on **both** of its forward faces at once,
  by a different enemy on each. It splits its frontage two ways and is at **maximum disadvantage**.
- A cell whose forward **face** meets an enemy face squarely is at parity — one face, one opponent.
- Cells behind the contact contribute as **supporting** cells, and their facing is what determines
  whether they support.

**This is the payoff of S1, and it is emergent rather than scripted:** point-forward geometry makes
*salients and corners* automatically take a 2:1 face disadvantage, so perimeter SHAPE (S2) drives
local outcome without any rule that says "corners are weak". Concavity, convexity, the cost of a
protruding flank and the value of a refused one all fall out of the same primitive. A face-forward
octagon cannot produce this: a flat leading face meets one opponent and the corner penalty vanishes.

⚠ **Audit consequence.** "Is the octagon point-forward or face-forward?" is therefore not cosmetic
and not merely an arc-indexing question — it decides whether the engine has this mechanic at all.
Any `PC_FACING_MODEL` fix must be checked against S5, not just against the arc multipliers.

**S6 — THE BODY IS A CIRCLE; THE OCTAGON IS AN ARC PARTITION. Conflating them is the root cause.**
Diagram 4 (Jordan): the octagon drawn inside the legacy grid square, with *"the cell should be a
circle not a square"*, and the arc semantics — **green = the two FRONT faces flanking the forward
vertex, yellow = the two SIDE faces, red = the four REAR faces, roughly based on field of vision."*
(Colour is not consistent across the four diagrams and is not semantic — the geometry is.)

Regular octagon, vertex-forward, each face 45°:

| arc | faces | angular span from the forward vertex |
|---|---|---|
| **FRONT** (green) | 2 | 0° … ±45° |
| **SIDE** (yellow) | 2 | ±45° … ±90° |
| **REAR** (red) | 4 | beyond ±90° — a full 180° |

**The defect this exposes, and it is architectural.** `geometry.py:365-372` records the
circle→box substitution in its own words: *"a body-only CellBox (w=d=1.0, reach_front=0) has the
same footprint **diameter** as the legacy circle model."* Same diameter **on the axes** — but a unit
square's diagonal is 1.414, so its circumscribed radius is 0.707, not 0.5, and a square is
**ROTATION-VARIANT where a circle is not.** One oriented box is currently serving three jobs at once:
exclusion volume, facing/arc carrier, and reach envelope. So **changing a cell's facing changes its
collision volume.**

That single conflation explains two of the session's hardest findings mechanistically:

1. **F3/F4 (bodies interpenetrate under `PC_FACING_MODEL`).** The flag slews facings; the oriented
   box rotates; two previously-disjoint bodies overlap *without either one moving*. Worse, the
   swept-SAT solve explicitly assumes axes are constant over a tick (*"over one tick the box axes and
   corner-offsets are CONSTANT — Euclidean motion translates only the centre"*), which a slewing
   facing violates outright, voiding the certificate. **With a circular body, facing has zero effect
   on collision and this failure cannot occur.** This is consistent with the bisect: `PC_FACING_MODEL`
   alone causes F3/F4.
2. **F11 (a lattice self-interpenetrates off-axis at depth `1 − cos θ`).** Precisely the square-vs-
   circle artefact. Circles of r=0.5 at pitch 1.0 are tangent at *every* rotation; squares at pitch
   1.0 interpenetrate whenever the facing is off the lattice axis.

**The separation of concerns S6 requires:**

| concern | shape | rotation behaviour |
|---|---|---|
| **body / exclusion** | circle, r = 0.5 | **invariant** — facing cannot move it |
| **facing / damage / FOV** | octagon arc partition, vertex-forward | **variant, and always has been — that is the point** |
| **engagement / reach** | forward envelope beyond the body | orientation matters, collision does not |

**Rotation-variance is not the defect; its LOCATION is (Jordan, 2026-07-30: "the octagon has always
been rotation-variant").** The octagon *must* be rotation-variant — an arc partition whose sectors
did not turn with the cell would carry no facing information at all, and S5's corner-disadvantage
mechanic is precisely a rotation-variant effect. The defect is that rotation-variance **leaked out of
the arc partition and into the exclusion volume**, because one `CellBox` carries both. Turning a cell
is supposed to change *who it fights and how well*; it is not supposed to change *what space it
occupies*. Separate the two shapes and each gets the behaviour it should have — the circle rigid
under rotation, the octagon turning freely on top of it.

This is §8's "every rule lives once" applied to geometry: three different questions, three owners.
The current code answers all three with one `CellBox`, which is why turning the facing model on
breaks the collision invariant.

**S6a — THE SQUARE FITS WITHIN THE CIRCLE, NOT THE CIRCLE WITHIN THE SQUARE (Jordan, 2026-07-30).**
The containment is currently inverted, and the inversion is measurable:

| | body radius on-axis | body radius on the diagonal | rotation-variant? |
|---|---|---|---|
| **now** — circle inscribed in a 1.0 square | 0.5 | **0.7071** | yes |
| **spec** — square inscribed in an r=0.5 circle | 0.5 | **0.5** | **no** |

The square's corners currently exceed the intended body radius by **0.2071** — over-claiming the
body's extent by **41% in the diagonal directions**, and only there. That directional overhang *is*
the off-axis interpenetration: it appears exactly when the facing is off the lattice axis and
vanishes at 0°/90°, which is the `1 − cos θ` signature F11 measured.

Under the spec the numbers close cleanly: pitch 1.0 with an r=0.5 circle makes adjacent cells
**exactly tangent at every orientation**, and any square retained for tiling or arc bookkeeping has
side `r√2 = 0.7071` and can never protrude past the exclusion circle. The binding constraint becomes
the circle at all orientations, which is precisely what makes the invariant hold under rotation.

⚠ The alternative repair — keep side 1.0 and grow the exclusion circle to the circumscribed
r=0.7071 — is **rejected by this spec** and would also space every formation 41% further apart,
changing frontage, density, contact and every band fitted on top of them.

**S3 — Cell relational positioning is CENTROID-BASED to the other cells in the subunit.**

**S4 — Movement is vector-based on a continuous field; the SUBUNIT conditions its cells' alignment
and they move accordingly.** Cells hold relative distance within their network; they collapse/infill
toward points of engagement rather than opening voids.

**Gap analysis against the tree.** `_node_rel` is centroid-anchored (S3 ✓). But S1, S2 and S4's
"conditioning" are not implemented: there is no subunit-perimeter object anywhere, cells relax
INDIVIDUALLY toward rotated slots rather than being conditioned as a body, and the octagon's
orientation convention needs verification against S1. F11's finding — that a 1.0-pitch lattice of
1.0×1.0 boxes self-interpenetrates at depth `1 − cos θ` whenever the facing is off the lattice axis —
is very likely an artefact of *not having* S2: with a perimeter that owns the frontage, cell
placement is a tiling problem inside a known boundary rather than an emergent consequence of
per-cell relaxation.

---

## §5 — For Jordan

1. **The golden mode matrix** (§4.2) — blocking, and not a session's call.
2. **`CONTACT_REACH`** (F18) — the one flag not turned on, because it is a magnitude.
3. **ED-MB-0059's disposition**, pending the F3/F4 bisect: if the exclusion pass causes cross-side
   interpenetration, default-ON is wrong and the ratified entry needs amending.
