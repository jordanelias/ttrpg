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

## P-4 — Sightline and the arc partition · **RULED by Jordan, 2026-07-30**

> *"135 degree viewing angle. Split yellow arc into two equal segments: yellow is 1.25x penalty and
> orange is 1.5x penalty. The 135 viewing angle is an arc that should be snapping from vertex of
> orange/yellow to vertex of orange/yellow"*

**This resolves the three-way conflict AND collapses two constants into one boundary.** The proposal
above recommended S6's 180° rear and implementing v30's range limit; the ruling supersedes the arc
half of that — **v30's 135° wins outright** — and adds a split the proposal did not anticipate.

### The ruled partition (per side, measured from the forward vertex)

| arc | span | width | damage-received |
|---|---|---|---|
| **GREEN** front | 0° … 45° | 45° | **1.0×** |
| **YELLOW** | 45° … 67.5° | 22.5° | **1.25×** |
| **ORANGE** | 67.5° … 90° | 22.5° | **1.5×** |
| **RED** rear | 90° … 180° | 90° | **2.0×** |

The old single YELLOW (45–90°, flat 1.5×) splits into two equal 22.5° segments, so flank damage now
*grades* from 1.25× to 1.5× as an attacker works round toward the rear, instead of stepping.
Ten sectors total (2 + 2 + 2 + 4), a 22.5°-resolution partition rather than eight uniform 45° faces.

### Why the ruling closes P-4 rather than just answering it

**The 135° viewing arc is ±67.5°, and 67.5° is exactly the yellow/orange vertex.** So the sightline
boundary *is* an arc boundary — it does not need its own constant, and it cannot drift out of sync
with the partition. That is the ruling's own phrasing ("snapping from vertex of orange/yellow to
vertex of orange/yellow") and it is a structural property, not a coincidence: FOV and damage arc are
one partition read two ways.

### What this supersedes in the tree

| constant | now | ruled |
|---|---|---|
| `FOV_HALF_DEG` | 105 (⇒ 210° visible) | **67.5** (⇒ 135° visible) |
| `REAR_BLIND_DEG` | 150 | **225** |
| `ANGLE_DEF_MOD` / `OCTAGON_DMG_MULT` | GREEN 1.0 / YELLOW 1.5 / RED 2.0 | **GREEN 1.0 / YELLOW 1.25 / ORANGE 1.5 / RED 2.0** |
| `octagon_angle` thresholds | 45, 90 | **45, 67.5, 90** |

⚠ **This is a behaviour change, not hygiene.** It narrows perception by 75° and re-prices the inner
flank band downward (1.5 → 1.25). It moves goldens and must ride with the re-base. The v30 **15-cell
perception range** remains unimplemented and is still recommended (proposal above) — the ruling
settles the *angle*, not the *distance*.

**Falsifier:** a cell with an attacker at 60° must report YELLOW at 1.25×, at 75° ORANGE at 1.5×, and
at 70° must still SEE it (inside 67.5°? no — 70 > 67.5, so it must NOT see it). That last case is the
sharp one: the perception boundary and the yellow/orange boundary must be the *same* number, so a
test that moves one without the other fails.

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

---

## §A — ADVERSARIAL REVIEW of these proposals (2026-07-30, read-only `fable`)

**Five recommendations took real damage; two survive clean; P-4's ruled content stands but my gloss on
it was geometrically wrong.** Corrections folded in below rather than argued with. The summary table
above is superseded by the one at the end of this section.

### A1 — P-3 OVERTURNED, and not for the reason I asked about

I asked whether a frontage split nets to parity. **It does not** — resolution is opposed
(`a_deg = compute_degree(a_net, max(1, b_net))`, `orchestration.py:1304-1305`), so a halved per-pair
pool both lowers damage dealt and raises damage taken. Parity was the wrong worry. P-3 breaks three
other ways:

1. **The owner I cited does not exist at the ruled granularity.** Exchanges are **atom-vs-atom** pairs
   (`orchestration.py:776-831`); `_pair_engaged_troops` splits one ATOM's score across pairs. D3-R2's
   geometry — a corner CELL engaged by two enemy CELLS **of one enemy subunit** — is a *single pair*,
   carrying no multiplicity signal at all.
2. **Where two enemy ATOMS do engage one cell, the existing mechanism does the OPPOSITE.** The
   documented residual: *"a single cell simultaneously adjacent to TWO enemy atoms contributes its full
   troop share to BOTH pairs"* (`core/exchange.py:159-163`). In exactly the corner geometry the
   doubly-engaged cell fights at **full weight twice** — a bonus. "Each gets ~half" is false against
   the source I cited for it.
3. **Unsurfaced collision with a Jordan-ratified ruling.** Intensive/partition-invariant resolution is
   ratified (`orchestration.py:815-829`) and pinned by `test_partition_invariance.py:37-52`. A
   defender penalty keyed on engaged-body count makes 2-atoms-on-1 **strictly better for the
   attackers** than 1-merged-on-1 — partition variance through the defender's door — and **the pinned
   test will not catch it**, because it asserts only the attacker-side factor. This would have landed
   silently.
4. **My falsifier certifies the null.** 1-v-2 vs 1-v-1 confounds multiplicity with outnumbering: even
   an engine with no split gives the 1-v-2 cell two opposed damage streams. The capable control is
   **split-vs-merged at equal total troops** (2×T vs 1×2T) — the partition-invariance comparison this
   lane already owns.

**Revised P-3: the multiplicity penalty needs a mechanism that does not exist, and its first design
constraint is not to break partition invariance.** It is a genuine open design item, not a
"derive-the-shape" exercise. P-12 inherits this and also contradicts its own §9 source, which said the
magnitude *is* a Jordan number.

### A2 — P-9's derivation OVERTURNED; the provenance fix survives

`ω = v/r` is a **category error**: `_slew_facing` is rotation-in-place, and its live use is the
ATTENTION slew on **engaged, mostly halted** cells (v = 0). Under `v/r` a stationary cell can never
re-face — abolishing the mechanic exactly where D3-R2 needs it (*"the vertex will be oriented at
midpoint between opponents"* requires a halted cell to rotate). And **no per-cell pivot radius exists
in the engine**: `v` is available (`cell_last_speed`), `r` is not.

**My falsifier has no referent.** It compares against "the reform/wheel timings canon already asserts";
v30's Phase 7 "Reform" (`:504-506`) is a discipline/morale recovery step with no rotation timing, and
`PC_WHEEL` carries no deg/tick canon. So it was unfalsifiable as written. (Residual: two unread
"wheel" lines at v30:652/654 — if a timing hides there this softens to "uncited".)
**Surviving half: fix the false provenance record now, regardless of the ruling.**

### A3 — P-11 SOFTENED to "build, but none of it is free"

Every "nearly free" adjective was wrong:
- **Order-dependent.** The current solve is a commutative per-cell min-cap, a stated design property
  (`units.py:2259-2261`). A pairwise positional impulse is not, unless accumulated Jacobi-style — which
  my one-line spec did not say.
- **Does not converge in a dense lattice.** Interior neighbours sit at exact tangency, so any push δ
  creates new overlap ≈ δ with the next neighbour: a displacement **wave**, not a local fix.
- **The `s > 0` lesson recurs.** A separator triggered on `dist < 2r` sits on the same knife edge that
  produced the deadlock; avoiding per-tick micro-impulses needs a depth threshold — **a constant**,
  contradicting "no constant".
- **At `dist → 0` the centre line is undefined**, so "needs no RNG" fails precisely for the co-located
  pairs that motivated it.
- **Placement unspecified, and both options are bad**: post-commit writes positions no TOI certified;
  pre-solve becomes a proposal the cap can cancel.
- **My falsifier is blind to the real risk** — it tests the isolated pair, and the G13 control tests
  *freezing* while the failure mode here is oscillation. A jittering formation passes it.

### A4 — P-1: recommendation (b) survives, but my rationale was DANGEROUS

I wrote that "(a) is the same configuration with less honest labels". **That is false, and if it
persuaded anyone to pick (a) it would re-open ED-1089.** The mode key's job is run-vs-golden
discrimination, and this lane's own method *mandates flag-OFF control runs* — HARD RULE 4's attribution
control and every single-flag bisect in §3.1b. Under (a) a `CM=0` control run keys **identically** to
the `CM=1` golden and silently checks against the wrong configuration. Only (b) is safe.
Also: "(b) reverses ED-MB-0053" **overstates** — (b) keeps the key extension, which is the load-bearing
half, and retires only the fifth mode's separate-config role.
**And my falsifier cannot fail:** the re-base flips ~15 digest-relevant pins at once, so `unit_cm` will
differ from the retired `unit` golden regardless. The capable falsifier is `unit_cm` vs the **same
configuration with CM=0 alone**, at the new pin vector.

### A5 — P-4: the ruled numbers check out; my "structural, cannot drift" gloss is WRONG

Arithmetic verified (135/2 = 67.5; sectors sum to 360; REAR_BLIND 225 consistent with the existing
`FOV_HALF_DEG = 180 − REAR_BLIND_DEG/2` derivation). But:

**A vertex-forward octagon has vertices at multiples of 45°, so 67.5° is the side-face MIDPOINT, not a
vertex.** A vertex at ±67.5° exists only *because the split creates one*. So the boundary is **created
by the ruling, not pre-existing structure** — Jordan's phrase "vertex of orange/yellow" describes the
*new* partition correctly, but my claim that the coincidence proves the spec right is unfounded. It was
the same "consistency tell" error as D1, made a second time.

Worse, the anti-drift property holds **only if single-owned**, and **my own supersession table ships
67.5 in two constants** (`FOV_HALF_DEG` *and* the `octagon_angle` thresholds) — the exact two-owner
drift I claimed was structurally impossible. **Single-source it.**

Also outstanding: no supersession notes for S6's "8 sectors, 45°" or §10's "same 8 sectors" (a G15
sweep failure, again); `config.py:386`'s anatomical ~190–210° citation becomes **false** under 135°;
and the summary table above still answers P-4 with "S6's 180° rear", contradicting the ruled body in
the same file.

### A6 — P-10 under-scoped three ways

`FACING_REACTION_TICKS` is live on **both** paths and pinned digest-relevant in all four modes, while
`_slew_facing` runs only on the field commit path — so engine-wide retirement leaves the **grid oracle
with no turn latency at all**, and field-only retirement creates a path dialect. My proposal scoped
neither. Worse, **the clock currently carries the FOV gate** (`can_react`): blind attackers are never
faced, so the penalty persists — that *is* the surprise-rear mechanic. Retiring the clock before
FOV-gating the slew lets a cell turn toward an attacker the ruled 135° arc says it cannot see, and
**under P-4's ruling that hole widens from RED to the whole ORANGE band**. My falsifier passes while
that invariant is lost.

### A7 — P-2, P-5, P-8: recommendations survive, falsifiers do not

- **P-2:** my mechanism claim is wrong — `reach_for` enters via the **standoff** contact path, which
  takes *priority* over `FIELD_CONTACT` (`core/contact.py:248-253, 303`). And the only `CONTACT_REACH`
  read binds a local `_reach` that is **never consumed** (`core/contact.py:365`), so my grep falsifier
  would demand a ledger-backed value for a dead variable — G17's wrong-quantity shape. "Live read"
  must mean *consumed*.
- **P-5:** my falsifier is **wrong-signed**. The Minkowski envelope is the centres-hull **outward
  offset** by 0.5; I wrote "inset", which measures an inward surface and condemns both hypotheses
  indiscriminately.
- **P-8:** my falsifier is **vacuous by construction** — it can only falsify the rival strict-S7
  reading, never my recommendation. And the recommendation re-opens the two-owner heading problem R1
  exists to close, without saying which owner carries the correction vector.

### A8 — F20's bearing on P-4

P-4's surviving 15-cell range recommendation **has no named predicate**, and with four disagreeing
proximity owners an implementation can satisfy the falsifier on one while the limit binds another. And
my cited evidence is wrong: H6's A3/A4 at face-gap **11.8** is *inside* 15 cells, so those subunits
would acquire a target under the fix too — the example does not demonstrate the behaviour the fix
changes.

### Revised verdict

| # | standing after attack |
|---|---|
| **P-6, P-7** | **survive clean** (P-7 verified structurally) |
| **P-4** | ruled content stands; my gloss overturned; single-owner + G15 sweep required |
| **P-1** | (b) survives; my (a)≡(b) rationale is FALSE and must not be relied on; falsifier replaced |
| **P-2, P-5** | recommendation survives; falsifier replaced |
| **P-8** | open fork; falsifier vacuous; owner question unanswered |
| **P-10** | direction right, scope and FOV precondition missing |
| **P-11** | build, but order-dependence, convergence, threshold-constant and placement are all open |
| **P-3, P-12** | **OVERTURNED** — no mechanism exists at cell granularity, the existing residual is the opposite, and it collides with ratified partition invariance |
| **P-9** | derivation OVERTURNED; unfalsifiable as written; provenance fix survives and is urgent |

**Nine of twelve falsifiers could not fail as written.** That is the single most useful thing this
review produced, and it is a G19 result: I wrote twelve falsifiers in one pass without an independent
read, and most of them certified their own conclusions.
