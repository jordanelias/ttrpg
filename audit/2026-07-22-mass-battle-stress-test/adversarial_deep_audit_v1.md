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
