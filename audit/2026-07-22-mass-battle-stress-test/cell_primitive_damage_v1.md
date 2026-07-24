# Cell-Primitive Damage — the aggregate-smear bug, and what fixing it reveals (ED-MB-0040, 2026-07-24)

**Status: BUILT + GATED OFF (`PC_CELL_DAMAGE=1`), byte-exact when off. Measured, not yet default.**
Jordan directive (2026-07-24, verbatim): *"the cell is the primitive"*, *"each cell has its own octagon
facing"*, *"each cell has its own capacity to receive and issue damage"*, *"flank/rear damage is supposed
to be cellular"*, *"damage is supposed to be done to cells"*, *"we are supposed to have damage only being
emitted by cells in direct contact"*.

## The bug (confirmed by direct read of the resolution path)

The engine computed **one scalar per subunit-pair**: `_octagon_dmg_mod` evaluated each defender cell's own
octagon arc, then **averaged them into a single number**, which multiplied the pair's damage. That scalar
total was then handed to `distribute_casualties`, which **spread it across every engaged cell in
proportion to cell density only**. So:

- A rear-facing cell and a front-facing cell **in the same subunit lost the same troops**. The 2× rear
  multiplier only inflated a total that was then smeared uniformly.
- Envelopment could not **strip a formation shell-inward** — the exposed shell and the protected interior
  thinned at the same rate.
- A **monolithic** subunit was therefore near-unbreakable by envelopment (the flank/rear bonus dissolved
  into its whole pool) — which is precisely the artifact ED-MB-0038 had to work around with matched
  command-granularity, and the "engine gap" ED-MB-0039 characterised. **Both were downstream of this.**

## The fix

`_octagon_cell_mods` is now **the single owner** of the per-cell arc (each cell judged against its own
facing, its own local attacker centroid, its own pin/FOV state, its own reaction clock).
`_octagon_dmg_mod` is redefined as the **mean of that map** — byte-identical, so the aggregate path is
untouched. Under `PC_CELL_DAMAGE`, the same map additionally yields **per-cell allocation weights**
(`troops × that cell's own facing multiplier`), and the pair's casualties are applied to those specific
cells (`distribute_casualties_cellwise`, overflow-spilling so `cells == hp` holds even under annihilation).

**The pair TOTAL is unchanged** — only *where* the casualties land. That makes the A/B a clean isolation
of placement alone. Volley (area fire) keeps the aggregate spread: it has no contact-facing arc.

## Measured (n=30/60, multi mode)

**It fixes the pathology it was predicted to fix.** Infantry envelopment vs a 3-command line:

| | side-A | side-B | swing | side-symmetric avg |
|---|---|---|---|---|
| aggregate smear (OFF) | 64.3% | 23.3% | **41.0pp** | **43.8%** (below band, envelop *loses*) |
| cell-primitive (ON) | 65.5% | 50.0% | **15.5pp** | **57.8%** (inside the 55-72 band) |

The chaotic deployment knife-edge (ED-MB-0039's root cause) **damps by ~62%**, and the honest
side-symmetric average moves **into** the history-grounded band. This is the strongest evidence yet that
ED-MB-0039's "moderate envelopment is unreachable" was **not** a missing mechanic — it was this bug.

**But it re-bases the whole battery.** Full gauge: **8/20 (OFF) → 4/20 (ON)**. Because every contact in
every row now concentrates casualties on exposed cells, the calibration of rows that were tuned against
the smeared model shifts — notably `C4` 93.2→71.2 (out of 75-95), `H11` 45.6→15.4, `H10` 83.3→59.6,
`C5` →100 (ceiling 98). The mechanic is **more physically correct and less calibrated**: every band was
fitted (implicitly) to the smear.

## Why it ships gated OFF

Turning it on is a **re-baselining of the entire mass-battle balance**, not a local fix. That is a
Jordan-scale call and needs a calibration pass (the constants most implicated: `OCTAGON_DMG_MULT`,
`MULTI_SIDE_SHOCK`, `K_LINEAR`, and the reaction/FOV gates, all of which were set when flank damage was
diluted and now bite at full strength on the cells that are actually exposed). Landing it gated:
- preserves every golden digest and the current gauge (byte-exact OFF — verified against the pre-change
  engine, identical winners + hp to 6dp across the battery),
- makes the correct model **available and measurable**,
- and converts ED-MB-0039's "engine gap / design fork" into a **calibration** problem, which is tractable.

## Recommended next (the honest path)

1. **Re-calibrate against history with the cellular model ON** — the bands are the fixed point, the
   constants are free. Start with `OCTAGON_DMG_MULT`/`MULTI_SIDE_SHOCK` (now double-counting: per-cell
   concentration *plus* a subunit-level multi-side multiplier are two expressions of the same
   encirclement effect — a genuine double-count the smear was hiding).
2. **Per-cell morale** (Jordan: *"a cell should be able to have worse morale than another cell in the same
   subunit"*; *"cells aggregate into those subunit holistic scorings in the first place"*) — the same
   holonic move on the morale channel: cells carry own morale, aggregate up to the subunit score, which
   modulates back down. Cells that are being killed from the rear should break locally first.
3. Re-run the historical scenarios (Cannae OOB, `cannae_historical.py`) as the primary oracle rather than
   the abstract parity rows — per Jordan's directive to match real formations, spreads and force ratios.

## The historical test Jordan actually asked for — and it still FAILS

Per the directive to *"match what real army formations would look like… roughly match Cannae by having the
same spread and number of subunits as the actual battle"*, `cannae_historical.py` builds the real order of
battle at Jordan's scale (**5000 Carthage vs 8600 Rome, ~1.72:1**): a thin wide Carthaginian crescent
centre that baits, two deep African veteran columns that swing in, cavalry superiority (~2:1) that wheels
to the rear; Rome as a **deep, frontage-limited mass of maniples** (granular, so it *can* break
piecemeal) plus two weak cavalry wings. Subunit cap 11/side.

**Result: Carthage wins 0 / 20, both sides, with `PC_CELL_DAMAGE` OFF *and* ON.**

That is the headline finding of this pass, and it is more important than the gauge score: **the engine
cannot yet reproduce the defining envelopment of pre-modern warfare** even with the damage model
corrected. Cell-primitive damage was necessary but not sufficient. What the parity rows hid — and the
historical OOB exposes — is that the engine has no way for an **outnumbered** force to win by
manoeuvre: Lanchester density enters linearly and the 1.72:1 numerical edge simply grinds through,
because the mechanisms that historically *neutralise* numbers are missing or mute:

- **No local morale collapse.** Cells being killed from the rear cannot break *locally* — morale is a
  subunit (ED-1019) quantity, so a maniple whose rear rank is being butchered fights on at full value
  until the whole subunit's aggregate morale fails. Jordan's per-cell morale (next section) is the fix.
- **Rome's deep mass suffers no penalty for its own depth.** Historically the Roman mass was *too deep to
  fight* — its rear ranks were dead weight and its frontage was the binding constraint. In the engine
  depth is free: a 3-deep maniple contributes support without cost, so "more men" is strictly better.
- **The bait/elastic centre is not modelled.** A centre that gives ground *deliberately* while remaining
  unbroken (the whole Carthaginian plan) has no representation; the centre simply loses.

**This reframes the remaining work.** The gauge's abstract parity rows were measuring a ruler against
itself; the historical OOB is the real oracle, and it says the missing primitives are *local (cellular)
morale*, *a cost to useless depth*, and *deliberate elastic withdrawal* — not a "moderate-envelopment
band" (ED-MB-0039's fork). Recommend re-testing **all 20 precedents against their real orders of battle**
(force ratios, subunit counts, frontages) rather than force-parity abstractions, per the directive.

## Jordan's specification of the missing Cannae primitive (2026-07-24) — TIMING is the mechanic

Verbatim: *"cannae battle will still require the ability for cannae centre units to be defensive, to move
forward then bait enemy and withdraw so they get pulled in and ensure that the cavalry (which must be
fast) has the time to make contact from behind for encircle before the centre units get close to routing,
so pathing timing is huge."*

This names the primitive the engine lacks, and it is a **scheduling/pathing** primitive, not a damage one:

1. **Defensive posture on the centre** — the crescent fights to *survive*, not to win (intent/stance
   already exists as `PC_INTENT_RESOLUTION`; it must actually buy survivability, i.e. trade damage output
   for casualty resistance and morale-hold).
2. **Advance → bait → elastic withdrawal.** The centre moves *forward* to make contact, then **gives
   ground under pressure while remaining unbroken**, drawing the enemy mass *into* the pocket. The engine
   has `feigned retreat` (PC_FEIGNED_RETREAT) but it is a discrete tactic-check, not a *continuous*
   fighting-withdrawal that preserves formation integrity while yielding distance.
3. **A race with an explicit clock.** The battle is won iff `t_cavalry_reaches_rear < t_centre_routs`.
   That makes **movement rates, release timing and path length first-class balance parameters** — the
   cavalry's speed multiplier, the orbital-wheel radius (`ENVELOP_STANDOFF`), the wing release tick, and
   the centre's rout resilience must be tuned *against each other*, and the historical outcome is the
   assertion. This is the direct design consequence of the ED-MB-0039 finding that the outcome was
   "deployment-chaotic": once the centre can *survive on purpose*, the race stops being a knife-edge
   coin-flip and becomes a **designed, tunable tempo problem** — which is exactly what a player would
   experience as tactics.

**Implementation order this implies** (supersedes the ED-MB-0039 "band fork" as the priority): per-cell
morale (local breaking, so the pocket's shell degrades before the whole centre) → defensive-intent
survivability + continuous fighting-withdrawal on the centre → tempo calibration of the cavalry race
(speed / release tick / wheel radius) → then re-run the historical OOB as the acceptance test.

## CRITICAL CORRECTION — the Cannae test above ran with the Cannae mechanics TURNED OFF

Jordan (2026-07-24): *"do you have a bunch of things turned off right now too? … dude you gotta turn all
the boolean flags ON."* A flag audit says yes — **12 of 33 boolean flags default OFF**, and they are
precisely the primitives the Cannae plan needs:

| OFF by default | what it is | Cannae role |
|---|---|---|
| `PC_INTENT_RESOLUTION` | stance = offence/defence commitment | **"centre units to be defensive"** |
| `PC_FEIGNED_RETREAT` | feigned-retreat tactic | **"move forward then bait enemy and withdraw"** |
| `PC_YIELD_EMERGENT` / `_RALLY` / `_POCKET` | give ground / rally / pocket exits | give ground instead of dying |
| `PC_STOCHASTIC_ROUT` | break at the historical 15–30 % casualty band | centre breaks realistically, not at annihilation |
| `PC_CLOSE_RANKS` | cells refill the fighting line | the centre holds frontage while bleeding |
| `PC_RESERVE_COMMIT`, `PC_TROOP_DENSITY_CAP`, `PC_FRACTIONAL_POOL`, `PC_FRICTION_CEV` | reserves, mounted density cap, fractional pool, CEV friction | tempo, cavalry frontage, variance |

The wayfinding/geometry Jordan asked about is **live**: `PC_NODE_COHESION`=ON, `FIELD_MOVEMENT`=ON,
`PC_WHEEL`=ON, `PC_REFUSE`=ON, `PC_OCTAGON_DMG`=ON, and `perimeter.py` (face normals / approach
alignment) is wired into `_envelop_goal` (ED-MB-0035). The *movement* model was on; the **tactical**
model was off.

### Re-measured historical Cannae (5000 v 8600, real OOB, n=20/side)

| configuration | Carthage as A | Carthage as B | avg |
|---|---|---|---|
| defaults (as first reported above) | 0 % | 0 % | **0 %** |
| + cell damage, intent, feigned retreat, yield, stochastic rout, close-ranks, fractional pool | 0 % | — | **0 %** |
| all ON **except `PC_FRICTION_CEV`** | 0 % | 5 % | **2.5 %** |
| **ALL boolean flags ON** | 20 % | 55 % | **37.5 %** |

Three findings, all material:

1. **The earlier "the engine cannot reproduce Cannae" conclusion was an artifact of testing with the
   tactical mechanics disabled.** 0 % → **37.5 %** once they are on. The correct statement: *the engine
   CAN produce an outnumbered (1.72:1) envelopment win, in over a third of trials.* Historically Cannae
   was decisive, so the target is higher still — but this is a working mechanism to calibrate, not a gap.
2. **`PC_FRICTION_CEV` is load-bearing** — the only difference between the 37.5 % and 2.5 % rows.
   (Jordan's *"except for FRICTION_CEV maybe"* is worth revisiting: the data says Clausewitzian
   combat-effectiveness friction is exactly what lets a smaller, better-handled force beat a bigger one.
   With no friction the larger army's linear Lanchester edge is near-deterministic and Carthage never
   wins.) This is ED-MB-0016's gated DG-6 friction — it belongs in the calibration as a first-class term.
3. **A residual side-asymmetry remains** (20 % vs 55 %) even full-kit — the ED-MB-0039 deployment-tempo
   sensitivity, now much reduced but not gone, and exactly what Jordan's *"pathing timing is huge"* points
   at.

**Implication for the whole battery:** every gauge measurement in this repo — including ED-MB-0038's
8/20 and ED-MB-0039's regime analysis — was taken with 12 mechanics off. The honest next step is a
**full-kit re-baseline**: run the 20 precedents with all flags ON against their real orders of battle and
calibrate from there. Default-OFF gating exists for golden byte-exactness, a *regression-testing*
concern, not a *design-truth* one — the two need separating (a documented **"full-kit" profile** vs the
byte-exact legacy profile).
