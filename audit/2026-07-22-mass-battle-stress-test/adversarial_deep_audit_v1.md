# Deep Adversarial Audit — mass-battle engine (2026-07-24)

**Method.** Five structurally-independent read-only critics, each blind to the others' reasoning
(agonist→antagonist relay, CLAUDE.md §10), across five axes: fiat/arbitrary values, historical &
theory compliance, primitive emergence, sequencing/interdependency, reachability. Every headline
claim below was then **re-verified by hand** before being recorded here; agent-reported items not yet
independently checked are marked `[UNVERIFIED]`.

**Verdict in one line.** The engine's dominant failure mode is not wrong arithmetic — it is
**machinery that documents itself as working and does not**, sitting on a **provenance layer that is
largely self-referential**.

---

## 1. VERIFIED BY HAND (each checked directly against the source)

### 1.1 The anti-fabrication gate is defeated by a file in the repo
`tests/sim_verification_ledger.json` holds 26 entries of the form
`{"value": "3", "source": "orchestration.py", "note": "pre-existing constant"}` — **no variable
names**, bare integers, sourced to *the engine file that contains them*. It launders `K_LINEAR=12`,
`CASUALTY_SCALE=4`, `MAX_SUB_PHASES=5` and others through the gate. A closed provenance loop by
construction, and precisely the leak CLAUDE.md §7 warns about, instantiated as a checked-in artifact.
**Action: delete it and re-run the gate to see what actually fails.**

### 1.2 A fabricated citation on the envelopment-refusal gate
`orchestration.py` cites `[canonical: mass_battle_v30.md §A.3b — 45deg octagon GREEN/YELLOW boundary]`.
**"octagon" appears 0 times in that document.** The 45° threshold decides whether a cell may refuse an
envelopment — one of the highest-leverage branches in the flank model.

### 1.3 `K_LINEAR = 12` — the multiplier on ALL melee casualties — is a fit to superseded engine output
Its cited source (`mb_lanchester_design.md` §6) explicitly declines to supply magnitudes: *"Coefficient
values are sim-tuned at implementation — not pre-decided here."* Real origin: a work-log line recording a
fit to a trajectory where the loser routed at **~58% casualties** — roughly double the 15-30% band the
repo elsewhere calls historical.

### 1.4 Discipline degradation misreads canon by ~5×, as a ratchet
Canon (`mass_battle_v30.md:197`): *"Total Size lost **this turn** > current Discipline rating."*
Code (`core/state.py:182-185`): `my_loss = (cumulative loss since start)`, `disc_hits = int(my_loss / 1.0)`.
So it fires every 1 Size **ever** lost, against a canonical trigger of >5 lost *this turn*. Discipline
feeds the pool, movement, shock resistance and the yield gate.

### 1.5 `MORALE_EROSION_DAMP` silently breaks the canonical −3 cap — **my defect, landed today**
`core/state.py:111`: `erode_morale(min(loss, 3.0) * 0.7)` = **2.1**, while the comment on that line still
asserts *"cap −3 per Cascade Phase (§A.4)"*. Introduced by ED-MB-0036 (this session). Every canonical
morale trigger is 30% weaker than canon, with a comment claiming otherwise.

### 1.6 Converging bodies are divided by 1/N — verified algebraically AND measured
`orchestration.py:541-550`. For N identical converging atoms (base `B`, troops `T`, weight `W`):
`merged_base` is a troop-weighted **mean** (`B`) but `merged_troops` is a **sum** (`N·T`), giving
`corrected = B·W/T` against `naive = N·B·W/T` → **`factor = 1/N` exactly**. N subunits converging on one
target deal the damage of one — and that is exactly envelopment geometry.

Measured (H3 envelop vs 3-command line, n=20/side):

| | as A | as B | avg |
|---|---|---|---|
| `PC_CONVERGENCE_NORM=1` (default) | 52.6% | 25.0% | **38.8%** |
| `PC_CONVERGENCE_NORM=0` | 25.0% | 35.0% | **30.0%** |

A major live lever. **Note the naive prediction fails**: disabling it made results *worse* overall,
because both sides converge. The defect is real; the remedy is not a flag flip (see §4).

### 1.7 Feigned Retreat is entirely dead
`unit.feigned` is assigned in exactly one place — `orchestration.py:2005`, `= False`. It is **never set
True** anywhere in the package. So `PC_FEIGNED_RETREAT`, `FEIGNED_RECOGNIZE_OB`, `FEIGNED_RETREAT_OB`,
`OVEREXTEND_PENALTY` and three functions are unreachable. `engine.py:69` advertises it as `"WIRED"`.
*(This supersedes an earlier claim of mine that its live call site was post-rout pursuit — the deeper
truth is the flag can never be True at all.)*

### 1.8 There is no pursuit in the mode the historical bands are measured in
The gauge runs `kind='multi'` → `run_multi_turn_battle`, which `break`s the moment either side routs.
`pursuit_damage` is called only at `orchestration.py:2360` and `discipline_check_cascade` only at 2473 —
both inside `run_multi_unit_battle`, which **the gauge never calls**. C5's band is explicitly grounded on
*"exploitation + pursuit"* (Boddy 2015). **The band cites a mechanism the measurement cannot contain.**
Historically the pursuit is where most of the loser's casualties occur and where the winner/loser
asymmetry is generated.

### 1.9 C2 and C6 are bit-identical experiments counted as two passes
`gauge_mb.py:347-348` and `370-371` carry **identical** shapes, kwargs
(`{'stance':'hold','discipline':8,'instructions':('brace',)}`), band (0-30) and metric (`rawA`), and
`matchup()` uses a fixed `seed_base`. C6 is presented in the doc as independent confirmation of C2. It is
the same run. Neither passes `width`/`depth`, so both build a 3-wide × 2-deep block — the "square /
schiltron / pike block" and the "shallower wall" are the same two-rank formation.

### 1.10 Better armour makes you take MORE arrow casualties
`units.py:1921`: `h_per_size = max(1, min(discipline, command) + dr)`.
`orchestration.py:1804`: `volley_hp_scale = (h_per_size + 1) // 2`, which **multiplies volley casualties
inflicted on that unit**. Higher `dr` (armour), discipline or Command ⇒ strictly more missile losses.
A fossil of a retired Size→HP conversion. Historically backwards without qualification.

---

## 2. AGENT-REPORTED, HIGH-CONFIDENCE, NOT YET RE-VERIFIED  `[UNVERIFIED]`

- **The cascade's advertised mechanism does not exist.** `dynamic_facings` is built, passed and rotated
  into, but never read inside `resolve_engagements`; its only consumer `_atom_avg_facing` has zero call
  sites. So *"later sub-phases see FLANK/REAR angles"* is false, and calibration attributed to cascading
  resolution was actually attributable to RNG reordering + pair truncation.
- **The Cannae fixing-force never fires.** `_front_fixers` is still computed per cascade sub-phase (the B6
  fix threaded `conv_scale`/`eng_counts`/`atom_sides` but not this), so a pinned centre + wrapping wings
  evaluates `False` in *both* groups. The exact mechanism ED-MB-0018 exists to deliver is dead by default.
- **Charge momentum never decays.** Halted cells `continue` before the `cell_last_speed` write, so a
  charger's closing speed is frozen and puncture + charge-shock fire at full magnitude every tick for the
  whole melee — falsifying the code's own comment that the differential "vanishes emergently."
- **`col_grid` dies on lateral movement.** Columns are keyed to spawn positions; after any wheel/envelop
  the live column keys no longer intersect, so every density reads 0 — silently disabling depth
  absorption, fatigue, stamina drain and volley density **for the manoeuvring side specifically**.
- **Rout lags up to 5 ticks** behind the damage that caused it (triggers fire only at 6-tick phase
  boundaries), so a subunit past every break criterion keeps rolling its full pool.
- **`unit.hp` vs `sum(cell_troops)` provably diverge** — pursuit and freed-attacker paths mutate `hp` with
  no cell write; `distribute_casualties` discards overkill residual (only the `_cellwise` variant has the
  spill loop). The two ledgers feed *different* mechanics, and which one a unit uses depends on its
  subunit count.
- **Depth adds unbounded killing power.** `SUPPORT_WEIGHT_FLOOR = 0.3` with no rank cutoff: every rank at
  depth ≥4 contributes 0.3 of its troops to the killing pool forever. Sabin/Zhmodikov — the doc's own
  citations — say depth was **relief and morale**, not additive killing power. "Too deep to fight"
  (Cannae) is therefore not merely unrepresented but **inverted**.
- **Melee measures as a square law.** The repo's own `config.py:336-346` records melee exponent
  **p≈1.65-1.7** against its own ≤1.4 bar, and `lanchester_signature.check_linear` *requires* the big
  force to win 65%+ at 2:1 — codifying numerical dominance as a pass criterion, in a repo whose four
  flagship precedents are all smaller-force victories.
- **Command has been removed from the combat pool** (`POOL_QUALITY_MODEL` default ON), while the grounding
  doc still cites Biddle and asserts *"engine command-decisiveness (cmd6-vs-2 → 40-0) is correct."*
- **Envelopment is a ~3× damage multiplier with zero direct morale penalty**, inverting du Picq/Cannae
  causality (collapse causes the killing, not the reverse).
- **No charge refusal.** Burkholder's *"a horse will not run headlong into a solid object"* is gated on the
  defender carrying the literal string `'brace'`.
- **H3 passes on a free parameter.** `n_cmd=3` is the only value landing in band (0% @1, ~53-71% @3,
  ~95% @6, 100% @9), and its *triplex acies* citation is misapplied — the code deploys the three bodies
  **abreast**, whereas triplex acies is a **depth** arrangement.
- No terrain/elevation/weather; no ammunition, missile screen or combined-arms structure; no emergent
  exhaustion lull; sibling morale pull is **symmetric**, so a broken section exerts zero panic pressure.

---

## 3. THE PATTERN

Three independent critics converged on the same shape without seeing each other:

1. **Documented-but-inert machinery.** The cascade, the fixing force, feigned retreat, `col_grid` after a
   wheel, `PC_ROTATE_FLOOR`, pursuit-in-the-gauge-path. Each *reads* as implemented.
2. **Self-referential provenance.** Of ~92 mechanical magnitudes, **17 survive hand-verification**. The
   rest resolve to the engine's own changelog, its own config, a nonexistent ledger row, or a proposal
   that explicitly declines to supply values.
3. **Scale inversion against the cell-primitive ruling.** Density, facing, morale, stamina and rout are
   computed at unit/subunit level and pushed *down*, where the ruling asks them to aggregate *up*.

A fourth, cutting across all: **this session's own "+0.0pp, therefore inert" measurements were wrong
three times** — an unissued order, an unreachable centroid trigger, a set-but-unconsumed state. A null
result on a gated mechanic must be read as *"the harness probably never reached it"* until the mechanic
is instrumented directly.

---

## 4. REMEDIATION SEQUENCE (dependency-ordered)

**Tier 0 — measurement integrity (do first; everything else is measured through these).**
1. Delete `tests/sim_verification_ledger.json`; re-run the anti-fabrication gate; triage the fallout.
2. Fix the C2≡C6 duplicate and give C2 a genuinely deep braced block. Re-count the cavalry tally.
3. Report the **side-symmetric mean** in the gauge, never the A-side value.
4. Either move the C-battery onto `kind='multi_unit'` (so pursuit exists) or strike "pursuit" from the
   bands' grounding. Do not leave both standing.

**Tier 1 — defects that distort every reading.**
5. Convergence: make `merged_base` extensive (`sum`), matching `merged_troops`; add a partition-invariance
   regression (one body of 4T ≡ four bodies of T).
6. Make `Unit.hp` a derived property over cells; route pursuit/freed-attacker damage through the cell
   distributor; hoist one shared spill loop.
7. `volley_hp_scale` → a fixed lethality constant; route the target's own `eff_dr` into the volley.
8. Discipline trigger → per-turn loss vs `eff_discipline`, per canon.
9. Restore the −3 cap (apply the damp inside the cap, or raise the cap) and fix the false comment.

**Tier 2 — dead machinery: wire or delete, no third option.**
10. Cascade `dynamic_facings`; `_front_fixers` scoping; `cell_last_speed` decay; `col_grid` rebuild from
    live cells; per-tick rout triggers.

**Tier 3 — design calls for Jordan (NOT to be executed unilaterally).**
- Depth: cap the support stack at physically-reaching ranks and move depth's value to relief/morale.
- Envelopment: shift the effect from damage multiplier to morale collapse.
- Cavalry: graded, always-on charge refusal vs steadiness; `'brace'` becomes a multiplier.
- Command: restore a Biddle-shaped σ-ceiling term, or retract the Biddle grounding.
- Rout band: flip `PC_STOCHASTIC_ROUT` default ON and align the §A.4 ladder to 15-30%.
- Yield: split `YIELD_POOL_MULT` into offence-malus + survivability terms.
- **The disengage-and-recharge cycle the engine lacks (noted 2026-07-25, §7.1).** Contact, once made, is
  permanent: there is no way to express "the charge is spent; the horsemen draw off and come again". The
  impulse + charger-latch pair models it adequately for the braced-wall case, but a real cycle would also
  give cavalry a way to break off an unfavourable grind instead of grinding to destruction.

**Standing principle to restore:** *"the band is not lowered to make the engine pass."* It is currently
violated three distinguishable ways — raising ceilings, choosing a free construction parameter until the
row lands, and citing an engine measurement as a band's justification. The second is the most powerful
and the least visible.

---

## 5. REACHABILITY (fifth critic) — verified additions

Reachability is **prior to grounding**: a value cannot be justified *or* grounded if the mechanism it
parameterises never runs. These were confirmed by hand and by runtime probe.

### 5.1 H6 produces ZERO COMBAT — a live break in the measuring instrument
`RefusedFlank vs Line` reads `a_cas = 0.0, b_cas = 0.0, dec_n = 0, d = 100.0` across **60/60 seeds**. Not a
stalemate — **no casualties at all**. The two bodies close to ~2 units apart and then freeze permanently.

Mechanism: `_node_advance`'s lateral-file-holding rule (`hierarchy/units.py:1239-1246`) pins any subunit
with ≥1 sibling to its **own spawn column**, and nothing closes a lateral gap unless the subunit carries an
active `envelop`/`sweep`/`kite`/yield instruction. The refused army's strong wing carries none. The
time-of-impact halt independently stops the row-wise approach. H5 resolves only because *its* opponent has
manoeuvring wings that close the gap from the other side.

**This was visible in the session's own gauge output as `UNRESOLVED` and was recorded as "an all-draw
stalemate" without investigation.** A row reporting 0.0/0.0 casualties is not a balance result; it is a
broken instrument, and it should have been chased on first sight.

### 5.2 The refused-flank preset is broken in shipped code
`engine.py:453` `refuse_range=3`, and **no caller anywhere overrides it** (gauge, bat.py, workbench all
take the default). Measured minimum centroid-to-enemy distance the refused wing ever reaches: **~9.5** — so
`Order('enemy_range:3', ...)` at `engine.py:502` never fires and the wing holds all battle. It needs ≈10.
Same centroid-trigger class as the session's yield-probe bug, but in **production** code; and its
provenance tag cites a `sim_verification_ledger.json` row that does not exist.

### 5.3 `PC_WHEEL` defaults ON and is a no-op
Its only consumer is `hierarchy/units.py:1513`, inside legacy `advance_cells()`, which returns early on the
default node path. Kite/envelop/sweep were ported to `_node_advance`; the overhang wheel was missed. A flag
that ships ON and does nothing is worse than one that ships OFF.

### 5.4 The cascade never produces more than one group
Instrumented across the rows most likely to produce multi-rank contact: the simultaneous-group count is
**always 1**. So `MAX_SUB_PHASES = 5` never binds and "cascading resolution" degenerates to a single pass.
This independently corroborates §2's finding that `dynamic_facings` is write-only — the mechanism is both
**unread and never triggered**, from two different directions.

### 5.5 Further dead surface
- `equipment/armour.py` (`ARMOURY`, `dr_vs_piercing`, `tiers`) — its only consumer discards the armour half
  (`weapon, _armour = loadout_for(...)`); live ranged DR comes from the flat `RANGED_DR_DEFAULT = 2`.
- Order triggers `immediate`, `ally_at:D`, `own_strength:FRAC` — implemented and validated, **zero
  producers**. Only `tick:N` has a working producer/consumer path.
- The escort mechanism (`escort_of` and friends) — consumption fully wired, `escort_of` never assigned.
- `PC_RESERVE_COMMIT` — doubly unreachable: its only reader lives in `run_multi_unit_battle` (never called
  in scope), and nothing ever tags a subunit `'reserve'`.
- `yielding` is **never cleared** by `reset_morale_between_battles` (every sibling transient is), so with
  rally off it persists across battles for the rest of a campaign.

**Consequence for the census:** any constant whose mechanism is unreachable should be classified as such
*before* its provenance is argued about. Fixing reachability changes what the other findings even mean.

---

## 6. JORDAN RULING (2026-07-24): canon values MAY be broken for balance/tuning

> *"we are allowed to break canon values in the pursuit of balancing/tuning"*

This **reclassifies several findings** and must be applied before remediation:

- A deliberate, documented divergence from a canonical magnitude is **legitimate**, not a defect.
- What remains a defect is a divergence that is **silent or actively misdescribed** — where a comment,
  tag or doc asserts canon is being followed while the code does something else. That misleads the next
  reader and corrupts the provenance layer, which is the actual problem this audit found.

Applied to the specific items:

| finding | old framing | corrected action under the ruling |
|---|---|---|
| `MORALE_EROSION_DAMP` makes the §A.4 cap −2.1 | "restore the −3 cap" | **Keep the value.** Fix the comment, which still claims *"cap −3 per Cascade Phase (§A.4)"*. Label it a deliberate tuning divergence. |
| `DISCIPLINE_LOSS_THRESHOLD = 1.0` vs canon's "> Discipline this turn" | "implement the canonical trigger" | **Jordan's call.** It is a *shape* change (a variable replaced by a constant), not just a magnitude — a Discipline-5 veteran now cracks on the same loss as a Discipline-1 levy, inverting what the stat is for. Flagged for decision; either is defensible, but it must be **declared**. |
| `OVEREXTEND_PENALTY` applied per-turn vs canon's per-season | "context mismatch" | Legitimate tuning; **document the transfer**. |

**The rule this establishes:** the engine is free to diverge from canon, and free to use fitted
magnitudes — provided the divergence is *visible*. Every constant should say which it is:
GROUNDED (magnitude from an external source), JUSTIFIED (mechanism sourced, magnitude fitted — the
honest default), or DECLARED-DIVERGENCE (deliberately unlike canon, with the reason). A false
`[canonical: ...]` tag is the only genuinely unacceptable state.

### Tier-0.1 executed — `tests/sim_verification_ledger.json` deleted
The 26-entry bare-integer self-whitelist is gone. **Effect is latent, not immediate**: the
anti-fabrication gate scans only *changed* sim files (`ci_sim_fabrication_check.py:378`), so removing the
whitelist surfaces nothing until the next sim edit — at which point previously-laundered bare integers
in that file will be flagged. That is the intended behaviour: the laundering mechanism is removed, and
the debt becomes visible as the code is touched, rather than all at once.

---

## 7. TIER-2 EXECUTED (2026-07-24) — dead machinery: wired or deleted

The Tier-2 rule was *wire or delete, no third option*. Seven items, all resolved. Each carries a
regression test that was verified to FAIL against the pre-fix code, not merely to pass after it.

| item | verdict | what was actually wrong |
|---|---|---|
| cascade `dynamic_facings` | **deleted** | A write-only parallel facing store. `run_battle` built the dict, `resolve_engagements` received it and never read it, `_rotate_defender_facing` wrote rotations into it; its only reader `_atom_avg_facing` had **zero call sites**. The concept — engaged cells pivot toward their attacker — is live and better implemented by `Subunit.cell_facing_vec` (discipline-gated slew, rout flip, and what `_octagon_cell_mods` actually reads). Deletion is behaviour-preserving by construction; goldens unchanged. |
| `_front_fixers` scoping | **wired** | Computed inside `resolve_engagements` from whatever pair list that call received — which under `CASCADING_ENABLED` is one cascade sub-phase *group*, not the tick. A defender pinned frontally by a body in group 0 and flanked by a detachment in group 1 saw an **empty fixer set** and wheeled freely. That is the Cannae shape exactly: the mechanism was dead in the case it exists for. Hoisted to `_compute_front_fixers`, computed once per tick, threaded in like `eng_counts`/`atom_sides` already were. |
| `cell_last_speed` decay | **wired** | Both paths `continue`d past a halted cell without touching the speed map, so a cell kept the speed it charged in for the rest of the battle — and a cell is halted exactly when it is in contact, so every melee cell scored its charge impetus every tick of a grind. Momentum is now an impulse (halted → 0; `hold` → 0), with the braced-wall repel preserved by latching the *charger role* at impact rather than re-deriving it from the per-tick differential. See §7.1, including a correction to my own first diagnosis. |
| `col_grid` rebuild | **wired** | Built once, in `Unit.__post_init__`, from the spawn footprint; `sync_col_grid` refreshed only `density`, only for the columns already in the list. Column *membership* was therefore frozen at spawn. A body that wheeled or drifted occupied columns absent from its own grid, at which point `_fatigue_sigma` found no live blocks and returned 0.0 and `_defender_depth` returned 0.0 — **no fatigue and no depth-based charge absorption, for precisely the manoeuvring units**. Membership and per-column `depth` now track live cells; stamina carries over for surviving columns. |
| per-tick rout trigger | **wired** | Morale collapse was checked every tick; the annihilation trigger (`troop_total < SUBUNIT_ROUT_FLOOR`) only in `rout_resolution`, at a phase boundary — every `TICKS_PER_PHASE`(=6) ticks. A subunit ground below the floor kept fighting at full effectiveness for up to 5 further ticks. Both triggers are now on the tick clock; `rout_resolution` keeps its boundary check (idempotent), so §A.12 sequencing is untouched. |
| `PC_WHEEL` (§5.3) | **wired** | Shipped defaulting **ON** and was a no-op: its only consumer sat in legacy `advance_cells`, which returns early on the node path. Kite/envelop/sweep were ported to `_node_advance`; the overhang wheel was missed. Now a `_resolve_maneuver_goal` branch: a body whose whole footprint lies beyond the enemy's frontage turns in on the nearest enemy cell instead of marching its spawn file into empty air. Inert for any body with a file inside the enemy frontage, i.e. every head-on matchup. |
| `yielding` never cleared (§5.5) | **wired** | The one DG-2 transient `reset_morale_between_battles` missed — every sibling (`pocketed`, `feigned`, `overextended`, the rout break-point, the reaction clock) was cleared. With rally off nothing else clears it, so a subunit that yielded once stayed flagged for the rest of the campaign. Now cleared at the battle boundary with the others. |


### 7.1 Momentum-at-halt: an impulse, plus a latch — and a correction to my own first diagnosis

`cell_last_speed` at a contact halt was frozen at whatever the cell charged in with, and
`_momentum_speed` reads it with no moved-this-turn guard — so every melee cell scored its charge impetus
on every tick of a grind. Making it an **impulse** (a halted cell records 0) is the physically correct
primitive: `halted_cells` is rebuilt from *pre*-movement contacts, so the impact tick still records the
real closing speed and the charge lands once, where Sabin puts it.

That alone broke the braced-wall repel: `test_reach_weapon_class`'s pike-vs-cavalry retention margin
collapsed from >0.02 to **0.0035**. The cause is a modelling error one level up. `a_mom > b_mom` is how
the engine identifies **who the charger is** — it is not the cause of the recoil. The cause is a mounted
body pressed onto a hedge of set poles, and a wall does not stop repelling after one tick. With
impulse momentum the differential is true only at impact, so re-deriving the role every tick reduced the
repel to a single tick. The fix is to **latch the charger role at impact** (`atom._pressing`) and hold it
while the pair stays in contact; every other condition on the gate — brace, frontal zone, cavalry-only,
the reach test — is still re-evaluated every tick, so the wall stops repelling the moment it is broken,
flanked or out-reached. The latch expires when the bodies part and at the battle boundary.

**Correction to my first pass.** I initially recorded this as a Tier-3 punt, on the reading that the
impulse *cost* gauge row C1 (cavalry vs a steady unbraced line, the Burkholder/Sabin anchor), which I had
seen at 85-87%. Bisecting against a clean pre-Tier-2 tree showed the opposite: **C1 reads 86.7% at the
baseline** and the impulse is what brings it to **48.3%, inside its 35-55 band**. I had attributed a
pre-existing failure to my own change and drawn a trade-off that did not exist. With the latch, both
anchors hold at once — C1 in band *and* the pike repel intact — which is what a correct primitive plus a
correct role model should do, and is why the punt was wrong.

### Provenance: the 24 dangling `sim_verification_ledger.json` citations

Tier-0.1 deleted that file; 24 constants across `config.py`, `bat.py`, `engine.py` and
`workbench/server.py` still cited it. They were at least honest about being fitted ("CALIBRATED, not
independently historically cited") but they were tagged `[canonical: ...]` and pointed at a file that
no longer exists — the false-tag state §6 calls the only unacceptable one. All 24 are retagged
**`[CALIBRATED-DEBT: … — magnitude fitted to engine behaviour, no external source]`**, naming the
deleted whitelist as the former citation so the history is not laundered away either.

`CALIBRATED-DEBT` is a fourth honest label alongside GROUNDED / JUSTIFIED / DECLARED-DIVERGENCE, and is
accepted by the anti-fabrication gate's tag pattern. It says something the other three do not: *this
number has no source at all and is known debt*. Twenty-four of them is the honest count of that debt in
the engine's constant layer today.

### What Tier-2 does NOT claim
None of these were balance changes and none were tuned. Three of them (fixers, col_grid, rout clock)
had been silently *removing* effects the model intended to have, so the gauge moving after them is
expected and is not evidence either way about the bands — same caveat as Tier-1. The fourth (momentum at
halt) *does* move a band row, and deliberately: it takes C1 from 86.7% to 48.3%, into its 35-55 band, by
removing a permanent shock bonus for standing still. That is a defect removal whose direction happens to
be favourable, not a tuning pass — no constant was touched.

---

## 8. IS 20/20 REACHABLE BY CONSTANTS? (reachability sweep, 2026-07-25)

**Question.** Jordan: *"is there any combination of these constants where we magically somehow get to
20/20?"* The prior question to any tuning pass: for each failing row, does **any** setting reach its
band? A row invariant to every toggle is blocked by structure, and no constant-fitting will pass it.

**Tool.** `reachability_sweep.py` — one subprocess per (row, config) so `config.py` re-reads the
environment cleanly; 33 booleans in both directions + 6 magnitudes at their extremes (85 configs);
`--stack` greedily hill-climbs the strongest movers together, since 2^33 is not enumerable.

### 8.1 Two defects in the instrument, found before its results were trusted

**(a) Low-n positives are manufactured by noise, and the error is ASYMMETRIC.** The first run used
n=16 against the gauge's own n=60. Measured on R1, the *identical baseline config* reads **26.7 / OK at
n=16 and 44.1 / WIN-OUT at n=60**; the sweep accordingly reported 76 of 85 configs putting R1 in band
when the row is 14 points outside it and none of them do. Sampling noise can only **widen** an observed
span, so a NEGATIVE verdict ("the whole span missed") is conservative and survives low n, while a
POSITIVE verdict is exactly what noise fabricates. Negatives may be read at low n; **every positive was
re-verified at n=60 before being recorded below.** The tool now warns below n=40.

**(b) Ragged band parse.** Row tuples are not uniform — a normal row is 9 fields ending
`(..., lo, hi, dexp)`, a braced-repel row carries a 10th trailing `'rawA'`. Counting from the end read
C2's band as `(30, 'high')` instead of `(0, 30)`: wrong for exactly the two rows the cavalry-repel
question turns on. Now anchored on the `dexp` token with asserts on both row shapes.

### 8.2 Verified results (positives at n=60; negatives at n=16, valid per the asymmetry above)

| row | band | reachable? | how |
|---|---|---|---|
| H4 Cannae | 45-62 | yes — **but a FALSE PASS** | stack `PC_FRICTION_CEV=1, PC_ENVELOP_PATH=0, LANCHESTER_ENABLED=0, FACING_REACTION_TICKS=0` → 46.7 OK. It passes the envelopment row **by switching off envelopment pathing**. No single toggle reaches it (span 0.0-37.5). |
| H5 RefusedFlank | 48-62 | yes — legitimate | stack `PC_FRICTION_CEV=1, PC_FRACTIONAL_POOL=1` → 48.3 OK. Two real gated mechanisms; neither disables the thing under test. The one genuinely interesting hit. |
| H9 rev-H2 | 38-52 | yes — **band-fitting** | `K_LINEAR=24` → 45.0 OK. K_LINEAR is *already* the constant fitted to superseded engine output (§1.3); doubling it to land a row is the "choose a free construction parameter until it passes" failure named in §4. `PC_STOCHASTIC_ROUT=1` looked like a hit at n=16 (46.7) and is **not** one (52.8 WIN-OUT). |
| H6 RefusedFlank vs Line | 48-60 | **no** | span 50.0-100.0; greedy stack reaches 50.0 only via `PC_WHEEL=0`, which is the pre-port all-draw state (§5.1) — not a result. |
| H10 rev-H3 | 28-45 | **no** | span 25.0-100.0. Four apparent hits at n=16 (`PC_FACING_MODEL=1`, `MULTI_SIDE_SHOCK=0.0`, `FACING_REACTION_TICKS=0/1`) — **all four fail at n=60** (56.7, 57.6, 58.3). Zero reachable configs. |
| R1 Ranged vs Line | 0-30 | **no** | the 76 apparent hits were the n=16 artifact above. |
| C2 Cav vs braced deep block | 0-30 rawA | **no** | span 43.8-100.0; best stack 37.5. **Not a magnitude problem** — see §8.4. |
| C4 Cav flank/envelopment | 75-95 | yes — legitimate | `PC_STOCHASTIC_ROUT=1` → 91.5 OK at n=60 (baseline 98.3 WIN-OUT). A real gated mechanism, already proposed for default-ON in §4. `PC_FRICTION_CEV=1` looked like a hit at n=16 and is not one (61.7). |
| C6 Cav vs braced shallow Line | 0-30 rawA | **no** | span 43.8-100.0; best stack 43.8. |
| R3 Ranged mirror | 42-58 | **no** | pinned at exactly 50.0 / UNRESOLVED under every config; greedy stack does not move it. Note the win-split 50.0 is *inside* the band — the row fails the DECISIVE check. This is a missing resolution path, not a miscalibrated number, and reporting it as "out of band" would send the next reader to tune a number that is already right. |

### 8.3 Answer

**No.** Of the ten failing rows, at the gauge's own n=60:

- **legitimately reachable — 2:** H5 (`PC_FRICTION_CEV=1 + PC_FRACTIONAL_POOL=1`), C4 (`PC_STOCHASTIC_ROUT=1`).
- **reachable only illegitimately — 2:** H4 (passes Cannae with envelopment pathing OFF), H9 (`K_LINEAR=24`,
  doubling the constant already fitted to superseded output).
- **no reachable configuration at all — 6:** H6, H10, R1, R3, C2, C6.

So the honest constants-only ceiling is **12/20**, and even that assumes the two legitimate hits do not
conflict with each other or knock out a currently-passing row — untested, and `PC_STOCHASTIC_ROUT=1`
already demonstrates the risk: it passes C4 and *fails* H9 (52.8, WIN-OUT).

**The most useful thing the sweep found is not the count.** It is that the optimizer's cheapest route
to a green row is to **deactivate the mechanism the row exists to measure** — H4 passes Cannae with
envelopment pathing off. Any future tuning effort will rediscover that route, because on a win-share
gauge two lines colliding and a double envelopment can produce the same number.

**Consequence for the gauge, not for the constants.** `gauge_mb.py:417,421` already computes `a_cas`,
`b_cas` and mean turns-per-battle, and bands **none** of them. Casualty ratios and duration are the
quantities the literature actually constrains (loser ~15-30% at the break, winner ~5%, asymmetry
appearing *after* the rout rather than during the fight); win-share of a hypothetical repeated matchup
is close to unfalsifiable, and all 20 bands are judgement calls with no literature-derived interval.
A casualty-banded gauge rejects `PC_ENVELOP_PATH=0` immediately — two lines colliding do not produce
Cannae's casualty asymmetry whatever the win-share says. **That is the highest-value next step, ahead
of any further constant work.**

### 8.4 CORRECTION — C2/C6 is a mechanism gap, not a magnitude call

The Tier-2 handoff recorded C2/C6 as *"the latch removed the timing problem; what remains is magnitude —
`PC_CHARGE_RECOIL=6` and `SIGMA_PER_D=0.2` against `_wall_prep`"*, and queued it for Jordan as a
magnitude decision. **The sweep falsifies that.** Against C2's 0-30 band:

| lever | values swept | C2 result |
|---|---|---|
| `PC_CHARGE_RECOIL` | 0 / 3 / 12 / **24** (4x the default 6) | 100.0 / 93.8 / 87.5 / **87.5** |
| `SIGMA_PER_D` | 0.1 / 0.4 / 0.8 (4x range) | 93.8 / 93.8 / 93.8 — **completely insensitive** |
| `PC_BRACE_ENABLED` | off / on | 100.0 / 93.8 |

Quadrupling the recoil coefficient buys **6 points of the ~64 required**, and switching the entire brace
apparatus off costs **6**. The whole braced-wall mechanism is worth ~6 points on a row that needs ~64, and
`SIGMA_PER_D` — the conversion rate the recoil is denominated in — does not move it at all. The
coefficient is not the binding constraint; the mechanism is.

This **retires a Tier-3 magnitude call** and replaces it with a mechanism gap, and it independently
corroborates the older finding already in `HANDOFF_MB.md`: a frontal deep line cannot repel a charge in
this engine at any coefficient, because *a repelling formation is a square/box with all-around brace,
not a deep frontal line*. The all-around brace primitive is the work; the coefficient is not.

---

## 9. THE CASUALTY SCOREBOARD'S FIRST EXPERIMENT (2026-07-25)

Jordan approved the two instruments (§8's consequence) and granted permission to experiment on Tier-3
from historical precedent, iteratively. This is the first such experiment, and it overturned a default.

### 9.1 `PC_STOCHASTIC_ROUT` — the win-share gauge was penalising the correct change

The flag implements the du Picq 15-30% break band (ED-MB-0031) and shipped **OFF**; its own comment says
that without it "units grind to ~58% before breaking". Measured across all 20 rows:

| | OFF (shipped) | ON |
|---|---|---|
| loser casualties | **61-87%** | **29-41%** (band 15-30) |
| winner casualties | 7.8-37.8% | **3.3-17.4%** (cap 15) |
| casualty realism | 0/20 | **2/20** |
| win-share | 10/20 | **7/20** |

The win-share count drops three rows and the flip is still right. **The reachability sweep had already
tested this exact flag** (§8.2), found "passes C4, fails H9", and recorded it as a wash — a judgement
made on the wrong instrument, hours before the right one existed. **Default flipped ON.**

### 9.2 Rout contagion — mechanism ratified, magnitude NOT

`Unit.derive_rout` broke an army only when **every** subunit had routed, so sections broke at 15-30%
each and then absorbed casualties while their siblings fought on. `ROUT_CASCADE_FRAC` generalises that
to a fraction of starting strength, per du Picq's contagion. Measured (with the break band on):

| arm | casualty realism | win-share | note |
|---|---|---|---|
| no contagion (1.0) | 2/20 | 7/20 | H6 stuck at 79.2% loser |
| **⅔ of line** (0.5 / 0.34) | **5/20** | 7/20 | H6 fixed: 79.2% → 29.7% |
| **⅓ of line** (0.30) | **7/20** | 6/20 | every envelopment row in band; H6 now *undershoots* at 14.1% |

**Left at its inert default (1.0).** Two reasons, and neither is indecision: (a) ⅓ buys two casualty
rows and costs one win-share row and makes H6 break too early — that is a real trade, not a clear win;
(b) per-cell state (Jordan's 2026-07-25 directive) **redefines what a "section" is**, so any value
chosen now is fitted to a granularity that is about to change. The mechanism is grounded; the number
would be `CALIBRATED-DEBT`, and there is no reason to incur it yet.

### 9.3 Two methodological failures in my own experiment, recorded

**(a) `0.34` and `0.5` returned byte-identical results, and it is not robustness.** The gauge armies
have three subunits, so the broken share can only be 0, ⅓, ⅔ or 1 — both thresholds are first crossed
at ⅔. I ran the same experiment twice. Presented uninterrogated, "insensitive across a 47% range" would
have entered the record as evidence of a robust plateau. It is evidence of nothing. **A sweep over a
continuous parameter must be checked against the DISCRETENESS of what it acts on.**

**(b) The unchanged rows were the informative ones.** H1/H2/H7/H8/H9 are identical to the decimal across
every contagion arm, because `make_unit` builds them as a SINGLE subunit per side — the broken share is
0 or 1 and no threshold below 1.0 can fire. The mechanism is inert there by construction, not
ineffective. That is the sharpest argument yet for the per-cell directive: **an army with one subunit
has no line to come apart.** At cell granularity every body has sections that can break independently
and the same contagion applies *within* a subunit. The residual 30-33% on exactly those rows is the gap
per-cell morale exists to close.
