# DICE — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

Grounded: 2026-11-12 by `audits/24_GROUNDING_GAMES.md` (GM-07; GC-3) — §7's "Football Manager's three fidelities of one match engine" is not established in the tree or on the web; the clause now says so. The transfer it supports (one sampler for both fidelities) rests on ED-SC-0013 and is unchanged.

## Read at: 601e715 (working tree)

Subject: the resolution substrate — `engine/dice_engine/` (`dice_engine.py`, `sigma_leverage.py`),
`engine/substrate/` (leaf readers and the `pc_engine` path seam), `engine/engine_params/` and its exporters
(`tools/export_*`), `engine/tests/`, and the call sites in `engine/season/` and `modules/` through which a
draw reaches the fold. Instrument: the `resolution-diagnostic` skill's five properties, run on the real
functions; its output is evidence carried into a NERS reading (§5), not a verdict. Probe scripts and their
output are in the scratchpad (§12); nothing in the tree was edited but this file and the five proposal
files named in §6.

## 0. Verdict

The dice engine is a sound basis for a dynamic emergent narrative game, and it is the best-owned code in
the tree, but in computed play it is fed a constant, so it produces chance without character. The face
rule, the margin ladder, the sigma boost and the exact odds function each have one owner, advantage is a
mean shift on every path, no caller resolves on a reduced obstacle through `eff_ob`, and the odds the
engine states are the odds it deals (284 graded realm rolls at seed 0 over four seasons: Failure 70.4 %,
against 74.0 % exact at the pair that 265 of them were rolled at; 2,137 graded corpus rolls: 72.6 %). The
single largest obstacle is upstream of the dice and is this subsystem's to name: at world build all 83
realm persons roll two dice on every graded verb, no person holds an attribute, the advantage channel
summed to zero on every one of 568 observed rolls, and at that pair three quarters of contested acts fail
and write nothing while the top band cannot occur at all. The second obstacle is inside the subsystem:
there is not one roller but three (whole dice, a Normal sampler that reads half a success harder, and
mass battle's private copy), and the claim that they are equivalent is false at the level the game reads.

## 1. What it is, as coded

### 1.1 The modules

| file | what it owns | state held |
|---|---|---|
| `engine/dice_engine/dice_engine.py` (311 lines) | the face rule (`_die_result`, `:153-161`: 1 → −1, 2–6 → 0, 7–9 → +1, 10 → +2); `roll_pool` (`:205`, whole dice, floor 1D, any TN but 7 refused by `_require_tn7`); `continuous_engine_sample` (`:218`, Normal(0.4·N, 0.8·√N), fractional N, returns 0.0 with no draw at N ≤ 0); `degree_from_net` (`:236`, four bands on `margin = net − ob`: < 0 Failure, < 1 Partial, ≥ 3 Overwhelming, else Success); `BandExtension` (`:95`, a veto of the top band); `MU_PER_DIE`, `SIGMA_PER_DIE`; `DEGREE_LABEL`, `DEGREE_ORDINAL` | none; stdlib only |
| `engine/dice_engine/sigma_leverage.py` (468 lines) | `soft_cap` (1.5·tanh(x/1.5)); `net_boost` (capped sigma × 0.8 × √max(1, N), the mean shift); `levels_to_net_sigma` and `LEVEL_SIGMA` (minor 0.25 / moderate 0.50 / strong 0.75 / major 1.00); `p_success` (Normal closed form); `band_odds` (exact enumeration of the dealt roll, `:345`); `settle_margin` / `settle_record` (the fraction of a margin paid by one uniform draw, `:324`, `:386`); `record_odds`; `roll_net` (whole dice, `max(1, int(round(pool)))`); `roll_net_continuous` (fractional pool, floor 1.0); `eff_ob`, `effective_ob`, `sigma_space_ob_shift` (display only) | one `lru_cache` (`_net_counts`) |
| `engine/substrate/` (7 leaves, 581 lines) | `descriptors` (attribute, pursuit, axis, affiliation and heritage rosters), `names` (canonical naming; raises on an ambiguous or legacy name), `composition` (role → module attribute by string, cached), `combat_kit`, `battle_orders`, `stubwire` (the typed not-built result and its counter), `pc_engine` (the one `sys.path` seam into `modules/combat/`) | `composition._CACHE`, `pc_engine._LOADED`, `stubwire.invocations`; each JSON read once at import |
| `engine/engine_params/*.json` (8 artifacts) | cooked exports, each written by one `tools/export_*.py` behind a `--check` | none |

### 1.2 How the season loop reaches a draw

One path, by composition row, for every graded social act and every graded inquiry:

`loop/resolve.py:833` (a contest) or `:893` (an inquiry) builds the act's own generator,
`draw_factory(world_seed, tick)(actor, "roll:<prize or verb>:<act id>")` → `seam/contest.py::contest` or
`::grade` → the manifest's provider → `seam/wrappers/sigma.py::resolve` (`:451`) → `contest_input`
(pool from `seam/wrappers/pool.py::faculty`; obstacle operands carried raw; leverage from
`advantage_sigma`) → the module entry `modules/social_contest/roll.py::roll` (`:157`):
`roll_net(pool, rng) + net_boost(leverage, pool)` against `obstacle(inp)` → a `Margin(net, ob)` → the
S27.4 refusal on the pair (`ob > 2 × pool`) → `settle_record` (one `rng.random()`, only where
`boost − ob` has a fraction) → `seam/ladder.py::degree_of` (`:262-264`) → `degree_from_net(settled, 0)`.

Two other providers return something that is not a margin and are graded off their own result, by
ruling (Jordan, 2026-09-03): personal combat (`wound_state` → `combat_degree`, three bands) and mass
battle (`attacker_wins` → `field_degree`, four bands). Each draws inside its module: combat from the
Normal sampler (`modules/combat/core.py:62`, `SL.roll_net_continuous`) plus some thirty Bernoulli draws
per exchange in `wrapper.py`; mass battle from its own roller (`modules/mass_battle/resolution.py:37`).

Fourteen of the 67 verb rows roll (E-09): `tell`, `lie`, `speak`, `argue`, `determine`, `arrest`,
`interrogate` and the inquiries `research`, `examine`, `surveil` through the social roll; `fight`,
`accept`, `capture` through combat; `march` through mass battle. The other 53 are decided by typed
preconditions with no draw.

The season package makes five other kinds of draw, all through the same keyed mint and none through the
dice engine: the chooser's Gumbel noise (`decision/choose.py:463`, temperature 0.05, live), intent
disclosure (`:654`), a confided telling (`loop/witness.py:136`), the body hazard (`loop/matter.py:730`)
and the weather table (`queries/world_q.py:1205`). The last four ship at rate 0 or an empty table
(`data/fixtures.py:937`, `:1040`, `:690-691`, `:535`) and take no draw in a shipped realm.

### 1.3 What ran, and what it showed

- **The realm, seed 0, two seasons** (E-02): 1,529 folded acts; 118 graded margin rolls, every one at
  pool 2 and leverage 0.0; 114 at Ob 2.0, one at 1.536 and three at 2.842 (a room's terms); Failure 80,
  Partial 27, Success 11, Overwhelming 0; three fields graded, all unopposed, so no battle die was
  rolled; no fight.
- **Seed 0, four seasons**: 284 graded rolls; 280 at pool 2 and four at pool 3 (the practice addend,
  from season three); leverage 0.0 on all 284; Failure 200, Partial 61, Success 23, Overwhelming 0; five
  fields, one fought, in which mass battle's `roll_pool_fractional`, `compute_degree` and
  `_sigma_net_boost` each ran twice and `dice_engine.roll_pool` was called exactly 284 times (once per
  social roll, never by the battle).
- **Seed 1, two seasons**: 166 graded rolls, all pool 2, leverage 0.0; Failure 128, Partial 29, Success
  9; two fights, which drew seven times from `continuous_engine_sample`.
- **At build** (E-03): 83 persons; `capability` non-empty on two (both `inquiry: 2`, the default's
  value); `attributes` non-empty on none; `faculty` is 2 for all 83 on every one of the nine verbs that
  name a key.
- **`aperture 1 0`** (E-12): its `POOLS ROLLED` lines read `pools rolled [2]` for `argue`, `lie`,
  `research`, `speak`, `surveil` and `tell`, each with *"two actors at different pools: no"*.
- **The corpus** (E-13, the CORE lane's run, 143 cases, seed 0): `DEGREES RESOLVED` Failure 1,552,
  Partial 373, Success 209, Overwhelming 3 on the margin ladder (72.6 / 17.5 / 9.8 / 0.14 %), and
  Felled 8, Wounded 1 off the scene.
- **The module entry called alone** (E-14): `roll(inp, rng)` on a hand-built record, 200,000 seeded
  rolls at pool 2, Ob 2, one level of effort: 56.76 / 25.88 / 16.81 / 0.55 % against `record_odds`'
  56.54 / 26.09 / 16.82 / 0.55.

## 2. Steelman

Ranked by the weight each bears.

1. **The odds stated are the odds dealt, and one function says so.** `band_odds` enumerates the roll
   over the owner's own face table, settles each net by the same split `settle_margin` uses, and grades
   it on the owner's ladder; it copies none of the three (`sigma_leverage.py:350-356`).
   *Attack:* compare realised frequencies with it on three independent populations. Realm 421 rolls at
   (2, 2.0) across two seeds: Failure 72.0 % against 74.0 (standard error 2.1); corpus 2,137: 72.6 %
   over a mix of obstacles; standalone 200,000: within 0.22 points. *Survived.*
2. **Advantage is a mean shift everywhere, and the obstacle is never reduced by it.** Social:
   `roll_net + net_boost` (`roll.py:165`). Combat: `roll_net + soft_cap·sigma_n` against
   `ob_from_defender` (`core.py:135`). Mass battle: `_sigma_net_boost` (`resolution.py:221`).
   *Attack:* grep every caller of `eff_ob`, `effective_ob`, `sigma_space_ob_shift` and `capped=False`
   (E-17). The only callers are the parity test and the golden generator. *Survived*, with one
   qualification that is not a breach: the social obstacle carries a flat room term (F-DICE-10).
3. **Determinism without a shared stream.** Every roll's generator is `H(seed, tick, actor, purpose)`;
   adding a contested verb moves no other act's draw (`04` PART D row 35). The fraction draw is taken
   only when there is a fraction, so whole-Ob hashes did not move when it landed.
   *Attack:* look for a draw on the process-global stream on a loop path. Mass battle's `rngsource`
   falls back to the stdlib module outside a `using()` block, but the season's wrapper scopes one;
   the retiring contest kernel draws globally and the loop does not reach it. *Survived.*
4. **The ladder is one function for every scale that returns a margin**, guarded two ways (a behavioural
   sweep and a source scan), with the TN question closed by refusal instead of convention.
   *Attack:* evaluate every ladder on a domain the guard does not sweep. Mass battle's copy differs on
   6 of 10,000 tenth-step cells (F-DICE-07). *Narrowed:* one class on dyadic values, two at a band edge
   otherwise.
5. **The extremes are handled by rule, not by accident.** A pool floors at one die in every entry
   point; an impossible attempt is refused before dice are dealt (S27.4); a per-pool ceiling keeps a
   10 % chance of Partial-or-better at the hardest obstacle (`roll.py::_chance_floor_cap`; probe: 10.00 %
   at pools 1 to 6); the soft cap saturates (40 stacked `major` levels: boost 1.697 against 1.681 for
   four). Response is monotone in Ob and in pool on the whole-dice path (E-16).
   *Attack:* sweep pool 1 to 10 at Ob 2 and Ob 1.0 to 3.0 in quarters. *Survived.*
6. **The substrate leaves fail loudly.** A missing role, an unknown pursuit, an ambiguous name, a
   legacy tag and an undeclared context key each raise. *Attack:* find a silent default. Two remain,
   both at the dice engine's own seam (F-DICE-11).

## 3. Adversarial findings

Ranked worst first. "Fix" names the owner; the edits are in the proposal files of §6.

### F-DICE-01 · blocks a requirement · the engine is fed a constant

- **Claim.** In computed play every social roll is the same roll. Who acts does not change the dice,
  and nothing a person does before rolling changes them either.
- **Evidence.** `seam/wrappers/pool.py:94-100`: the pool is the held attribute, else the held key, else
  `pool_default` (2). `harness/populated.py:1016`: `cast_attributes=False` ships, and its docstring
  records that the registry authors `stats:` for one row. `sigma.py:160-167`: leverage is the sum of
  one source, `effort`.
- **Falsifier run.** E-03: 83 of 83 persons roll 2 on all nine keyed verbs. E-02: 568 graded rolls over
  three runs; 564 at pool 2, four at pool 3 (practice, seed 0, seasons three and four); leverage 0.0 on
  all 568. E-12: `aperture 1 0` prints *"two actors at different pools: no"* on six verbs.
- **Touches.** R-09 (its by-person conjunct, `workplans/valoria_master_workplan_v11.md:79`), R-06.
- **Consequence.** The world generates variance and no character: a skilled advocate and a ploughman
  argue at identical odds, so no story of the form *she was the better speaker* can arise.
- **Minimal fix.** Not in the dice. (a) Content and the switch: `stats:` on the cast rows in
  `references/npc_registry.yaml` and `cast_attributes` flipped (character lane; §13, §14).
  (b) `10_DICE_one_score_two_roles.md` so that a score, once held, is read in both roles.
  (c) `10_DICE_advantage_sources_for_the_arcs.md` so that the sigma channel carries something.

### F-DICE-02 · degrades narrative · the default outcome is nothing, and the top band cannot occur

- **Claim.** At the pair 535 of the 568 observed realm rolls were thrown at (pool 2, Ob 2), Failure is 74 %,
  Failure writes nothing on any social-path verb, and Overwhelming is impossible (two dice net at most
  4, a margin of 2).
- **Evidence.** `band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0)` (E-16). The corpus run's
  `BANDS THAT DIFFER` line reads False for `interrogate`, `lie`, `speak` and `tell` (E-13).
- **Falsifier run.** Overwhelming: 0 of 568 realm rolls; 3 of 2,137 in the corpus. A run of four
  failures has probability 0.300, of eight 0.090.
- **Touches.** R-01, R-02 (a failed act deposits only in witnesses' ledgers), R-09.
- **Consequence.** Three of four contested acts are non-events, and the band the verb table keys its
  strongest writes on is unreachable for the whole population.
- **The root, from the design set.** The engine's own design names this regime as its weakest. The
  armature (`sigma_leverage_engine_armature.md` §A, §G) scopes uniform leverage to the continuous
  engine, records that ED-836 flags bare pools of 1 to 7 dice as *"shaky"*, and lists the social
  contest as needing no help because its pools were *"already 5–18D"*; the designed pools were an
  attribute doubled plus history with a floor of five (`complete_systems_reference.md:138`, `:183`).
  The built social pool is the score itself (`pool.py:94-100`, CR-20), one to seven dice and two by
  default. The game follows the code; the cost is this finding: every lumpiness the design assigned to
  a regime it expected to avoid is the season's ordinary roll.
- **Minimal fix.** The magnitudes are Jordan's (`pool_default`, H-126). The form is fixable without a
  ruling: `10_DICE_one_score_two_roles.md` takes person-opposed rolls to Ob 1.0, where the bands read
  42 / 32 / 25 / 1 %.

### F-DICE-03 · degrades narrative · holding a score makes a person easier to oppose

- **Claim.** An unauthored person is opposed at `obstacle_default` (2.0, the stand-in for a subject with
  no score); a person holding the key at 2 is opposed at 1.0; a person holding an attribute at 1, at
  0.5. The stand-in is worth a score of 4 while the same person rolls as a score of 2.
- **Evidence.** `sigma.py:117-137`, `roll.py:141`; H-127's `cite:` records the inversion as live and
  unmeasured; `modules/combat/core.py:113-116` names the cross-module half (*"two ladders for one
  quantity"*).
- **Falsifier run.** E-07: Partial-or-better at pool 2 is 26.00 % against the unauthored subject,
  58.00 % against the key at 2, 73.50 % against an attribute at 1.
- **Touches.** R-06, R-09.
- **Consequence.** The moment content gives one character a modest score she becomes the softest
  target in the realm. Authoring characters makes them weaker.
- **Minimal fix.** `10_DICE_one_score_two_roles.md`.

### F-DICE-04 · degrades narrative · four rolled verbs name no capability

- **Claim.** `arrest`, `determine`, `interrogate` and `lie` roll through the social provider with no row
  in `rosters.yaml: verb_capability`, so neither party's skill can ever enter.
- **Evidence.** E-09 (`rolled with NO capability key`; `march` is the fifth and is mass battle's).
  H-312 measured `interrogate`: scores of 0 or 20 on either side leave `(0.74, 0.19, 0.07, 0.0)`.
- **Touches.** R-05, R-06.
- **Consequence.** A liar is exactly as convincing as an honest teller with the same default; a judge's
  learning does not bear on a determination.
- **Minimal fix.** Four roster rows, in the same proposal.

### F-DICE-05 · degrades narrative, and a port hazard · two samplers half a success apart

- **Claim.** The Normal sampler has the whole-dice roll's mean and variance and not its bands. Under a
  ladder that reads `margin >= 0` it is about half a success harder.
- **Evidence.** `dice_engine.py:222` and `sigma_leverage.py:420` both say *"statistically equivalent"*;
  the second adds *"Canonical for Godot"*. The source is ED-833 (2026-05-15, a Jordan decision), which
  adopted the continuous engine as the videogame's specification on a validation of mean and standard
  deviation at pools 5 to 17; the armature's own audit listed a *"discrete/continuous divergence"*
  (its T3) and scoped it as a small-pool caveat. `modules/combat/core.py:72-75` records that the local
  continuity shift was removed when combat moved to the owner's ladder.
- **Falsifier run.** E-06: Failure, whole dice against Normal: pool 6 / Ob 3, 53.04 against 62.03 %;
  pool 8 / Ob 3, 38.58 against 46.48 %; pool 11 / Ob 4, 37.31 against 44.01 %. Sampled, seed 7,
  n = 200,000, pool 8 / Ob 3: 38.59 against 46.42 %. A Normal shifted by +0.5 lands within a point of
  the whole dice in all seven cells.
- **A returning finding.** The degree census of 2026-08-12
  (`.audit/2026-08-12-degree-vocabulary-census/00_findings.md` §3) said combat's ladder *"should probably
  NOT be merged"*, because its −0.5 offsets were a continuity correction and merging *"would
  re-introduce the 5–9pp low read the correction was written to fix"*. The ruling of 2026-08-15 (no
  system keeps its own bands) merged it, with the order *"migrate, measure, report before tuning"*.
  Re-verified at HEAD: the low read is there, 6.7 to 9.0 points at pools 6 to 11 (E-06). The
  correction can be restored without a private ladder, in the sampler (a Normal centred half a
  success higher is the whole-dice distribution to within a point); whether to do so is a combat
  balance move and is cross-listed to the PC lane with this measurement as the report the ruling asked
  for.
- **Touches.** R-09; NERS-S (*calculations consistent in methodology*).
- **Consequence.** In the Python game, none visible: combat is tuned on its own sampler. In a port that
  reads *"canonical for Godot"* as covering the social roll, shown odds and dealt odds part by 7 to 12
  points.
- **Minimal fix.** `10_DICE_exported_face_rule_and_band_edges.md`: correct the two claims and name the
  sampler per provider where code reads it. The offset itself is left (§6, resolution 5). Narrowing
  *"canonical for Godot"* narrows ED-833, so it is also in §11.

### F-DICE-06 · degrades narrative · the advantage channel has one member, one sign, and sums to zero

- **Claim.** The one door for a modifier holds `effort` alone, cannot count against the actor, and
  carried nothing on any observed roll.
- **Evidence.** `rosters.yaml:3481`; `sigma.py:151`, `:167` (the `defender` list of
  `levels_to_net_sigma` is never passed). `fixtures.py:977`: `npc_effort="on"`.
- **Falsifier run.** E-02: leverage 0.0 on 568 of 568.
- **Touches.** R-02, R-09.
- **Consequence.** A wound, a favour, a precedent or a threat cannot change a later roll; ARC-53's two
  core needs have no carrier (§13).
- **Minimal fix.** `10_DICE_advantage_sources_for_the_arcs.md`.

### F-DICE-14 · degrades narrative · the chooser's odds answer for one verb, and "cannot say" reads as certain

(Numbered out of rank order because it was added with the NPC and chooser charge, §15; by severity it
sits here.)

- **Claim.** The believed-odds query the chooser weighs contested candidates by returns a figure for
  `determine` alone, the same figure for every person; for every other contested candidate it returns
  `None`, which the chooser treats as a chance of 1.
- **Evidence.** `decision/choose.py::odds_weight` (*"return 1.0 if chance is None"*);
  `sigma.py:286-289` (no claim about the subject → `None`); `sigma.py:383-388` (no believed mode for a
  fight or a field).
- **Falsifier run.** E-19, realm, seed 0, one season: 4,929 queries; 102 figures, all `determine`
  (0.26, 0.4346, 0.5765: the default pair at effort 0, 1, 2); `None` for `march` 3,813 times and for
  `accept` 1,014 times.
- **Touches.** R-08 (non-omniscient, non-optimal choice), R-06.
- **Consequence.** A lord weighs a march as if it could not be lost, and a duellist an acceptance as if
  he could not fall; knowing nothing of an opponent is the most favourable belief available.
- **Minimal fix.** `10_DICE_believed_odds_have_a_prior.md` for the social roll; the believed estimate
  of a fight or a field is the PC and MB lanes', to the interface stated there.

### F-DICE-07 · hygiene with a port cost · a second roller, and a ladder in two classes

- **Claim.** Mass battle rolls its own dice, grades on its own ladder copy and boosts with its own
  sigma functions; the copy is not behaviourally the owner; the guard that says it is cannot see the
  difference.
- **Evidence.** `modules/mass_battle/resolution.py:37-55`, `:57-77`, `:101-120`, `:209-230`; zero
  `engine.*` imports under `modules/mass_battle/`. `tests/valoria/test_degree_ladder_single_owner.py:302-309`
  sweeps integers, quarter-step nets and half-step obstacles, all exactly representable.
- **Falsifier run.** E-02 (seed 0, four seasons): the battle's roller ran from computed play with no
  call into `dice_engine.roll_pool`. E-04: 6 of 10,000 cells differ on tenths (for example net 4.3,
  Ob 3.3: Partial against Success), 72 of 160,000 on fortieths; `3 + net_boost(-1e-16, 9)` against 0 is
  Success on the owner and Overwhelming on the copy.
- **A returning finding.** The same census (§2) recorded that its quarter-step grid was *"structurally
  unable to observe"* the tolerance. The guard written from it eleven days later kept the grid. The
  roll-and-resolution inventory of 2026-08-19 named the forked roller; it is still forked, one
  directory over.
- **Touches.** R-04 (the field), NERS-S.
- **Consequence.** None in play today (the differing cells are float dust). The cost is that the port
  must transcribe two rollers and two ladders, and that the ruling *"ONE resolver for all d10
  probability … No system keeps its own bands"* (2026-08-15) is met by a test that cannot fail.
- **Minimal fix.** `10_DICE_one_roller_one_fraction_rule.md`.

### F-DICE-08 · hygiene, latent · three rules for a fraction of a die

- **Claim.** Whole-dice paths round a fractional pool (half to even: 2.5 deals 2, 3.5 deals 4), the
  Normal sampler takes it as it is, mass battle deals one more die with probability equal to the
  fraction.
- **Evidence.** `sigma_leverage.py:295`, `:449`; `resolution.py:72-76`.
- **Falsifier run.** E-05: Partial-or-better at Ob 2, pool 2.49 → 26.00 % rounded against 32.86 % by the
  stochastic die; pool 2.51 → 40.00 % against 33.14 %.
- **Touches.** NERS-S; the port (GDScript's `round` rounds half away from zero).
- **Consequence.** Unreached in the season today (`faculty` returns `int`). It becomes a 14-point step
  the day a pool is fractional.
- **Minimal fix.** Same proposal; one rule, the same shape as the fraction of a margin.

### F-DICE-09 · hygiene · the typed layer omits the facts every draw depends on

- **Claim.** The face rule, the band edges and the named-level table are not exported; three artifacts
  have no Python runtime reader; the resolver named in the contract is not the one a provider returns.
- **Evidence.** E-11: `sim_params.json` carries six scalars for the dice engine. The face rule is an
  `if` chain, the edges are comparisons, and `LEVEL_SIGMA` is an annotated assignment that
  `tools/export_sim_params.py:226` skips. E-10: `game_constants.json`, `sim_params.json` and
  `value_pointer_links.json` are read by tools and tests only. `references/module_contracts.yaml`:
  social contest `resolver: dice_pool` against `sigma.py:110` `d10_sigma`; the combat row's comment
  still says *"base Ob 3 FIXED"*. `04_CODE_ARCHITECTURE.md:181` types the ladder as reading *"the
  exported band edges"*.
- **Falsifier run.** All seven `--check`s exit 0 (E-10) while the three facts are absent: the
  round-trip observes that the artifact equals a fresh extract, never that the extract covers the fact.
- **Touches.** The port gate (B10-20).
- **Minimal fix.** `10_DICE_exported_face_rule_and_band_edges.md`.

### F-DICE-10 · evidence, accepted · the room is a flat obstacle shift

- **Claim.** A bench's regard and unmirrored proofs move the obstacle by a flat amount
  (`roll.py:142-143`), so their leverage falls with the pool where a sigma level's does not.
- **Falsifier run.** E-08: one point of reception against a base Ob of 3 is worth 1.25 z at pool 1, 0.88
  at 2, 0.63 at 4, 0.44 at 8; one level of effort is 0.48 z at every pool.
- **Disposition.** Deliberate, with safeguards (floored at `OB_MIN`, bounded by the ceiling), and
  licensed by the ruling's *"plus whatever specific modifiers exist … in that instance"*. Since the
  fraction rule it pays smoothly. Accepted; recorded (§6, resolution 9). No build.

### F-DICE-11 · hygiene · the extension seam is unreached by the loop and half open

- **Claim.** `BandExtension`'s only users are in `systems/social_contest/sim/contest/`, which the loop
  does not reach; `seam/contest.py:184` accepts an `extension` argument its body never reads, under a
  docstring that says *"EVERY ARGUMENT IS LOAD-BEARING"*; and the context check runs only in the top
  band.
- **Falsifier run.** E-04: `degree_from_net(2, 0, extension=E(), poool=8)` returns Success with no
  error; the same call at margin 3 raises; `degree_from_net(5, 0, pool=8)` with no extension returns
  Overwhelming and swallows the key, against the docstring's *"Unknown keys are REFUSED rather than
  swallowed"* (`dice_engine.py:75`).
- **Minimal fix.** In `degree_from_net`, validate context before the band is decided and refuse context
  with no extension; delete the dead parameter in `contest()` (§6, resolutions 11 and 12).

### F-DICE-12 · hygiene · half the advantage module's surface has no game caller

- **Claim.** `p_success`, `eff_ob`, `effective_ob`, `sigma_space_ob_shift`, `sigma_N` and `eff_sigma`
  are called by no module the loop reaches. `band_odds`' docstring says `p_success` *"stays the Gaussian
  closed form combat reads"*; combat does not call it.
- **Falsifier run.** E-17: the only callers are `engine/tests/test_sigma_leverage_parity.py`,
  `tools/gen_sigma_parity_goldens.py` and the retiring kernel. The parity golden's eight pinned
  functions include three of them.
- **A returning shape.** The combat wiring audit of 2026-07-23
  (`.audit/2026-07-23-combat-engine-wiring-audit/wiring_audit_v1.md:58`) found `core.effective_ob` dead
  and display-only; combat deleted it (`core.py:59-61`, re-verified). The twin it wrapped is still in
  the dice engine.
- **Minimal fix.** Delete with the kernel when it retires (SM-15, Jordan's timing); until then correct
  the one false sentence (§6, resolution 13).

### F-DICE-13 · hygiene · stale passages at the owner

`dice_engine.py:8` and `:6-7` (status and sources naming the retired `params/core.md`);
`engine/dice_engine/__init__.py:8` (*"PROVISIONAL — Pass 2l armature stub"* on the package that is the
ruled owner); `sigma_leverage.py:5-9`; `loop/resolve.py:887-888` (*"HOLDS ONLY WHILE `verb_capability`
names no inquiry"*: it now names three); `requirements.yaml`'s social-contest scale note
(`in_loop: "seam unbuilt"`, against a registered provider that rolled 568 times above);
`resolution.py:43-46` (the volley path *"hand-rolls its own d10 loop"*; D_T01 row 38 found it delegates).
Each is an edit at its line (§6, resolution 14).

## 4. Code matters

**Ownership and duplication.** One owner each for: the face rule (`_die_result`), the margin ladder,
the per-die pair, the soft cap, the boost, the exact odds, the margin's fraction, the pool reader
(`pool.py::faculty`), the social obstacle (`roll.py::obstacle`). Second owners that remain: mass
battle's four functions and two literals (F-DICE-07); combat's inline `soft_cap(net_sigma) *
sigma_n(pool)` (`core.py:135`), numerically identical to `net_boost` on the probe grid (E-04) and so a
second spelling of one operation, which the diagnostic skill already names; the pool floor, re-applied
at `sigma_n`, `net_boost`, `p_success`, `_dice_dealt`, `roll_net_continuous` and `roll_pool` with two
literals (`max(1, …)`, `max(1.0, float(…))`).

**Dead or unreached.** §3 F-DICE-11 and F-DICE-12. `ladder_error()` (`seam/ladder.py:116`) returns `""`
always and is kept for its importers. `continuous_engine_sample`'s `pool <= 0 → 0.0` branch is
unreachable through `roll_net_continuous` (which floors first); its one other caller is an experiment
arm (`harness/arms.py:261`).

**Contract and seam fidelity.** `04` §A.2 types `seam/wrappers/*` as reading the projection and returning
a `Margin`; `sigma.py` reads `World` (declared at its head as a convention-grade deviation, with
`combat.py` as precedent) and hands the seam a dict; the module boundary is held to `Margin` and a
wrong return raises (`sigma.py:535-542`). `04:181` (the ladder reads exported edges) and `04:778` (a
provider veto reaches the ladder) are not met: the edges are code and no veto path exists in the season
seam. `04:1057` row 30 (*"subsystems return a `Margin`"*) holds for one of three providers, the other
two by ruling. `engine/dice_engine/` is a project shape, not a registered module (`04:1011`), which is
right: it holds no token and no state.

**Determinism.** Sound on the loop path (steelman 3). One caution for the port: the fraction draw and
the dice share one generator in a fixed order (`sigma.py:533-552`), so a port must draw dice first.

**Test strength.** Strong where it matters most: `test_band_odds.py` swaps a band edge and requires the
tuple to move, and walks the face table by brute force; `test_odds_of.py` holds mode (a) to the dealt
distribution within three standard errors; `test_degree_boundary_epsilon.py` uses `nextafter` and
proves its predecessor vacuous. Weak in three places: the single-owner sweep's domain (F-DICE-07);
`test_per_die_one_owner.py` pins that the advantage module reads the owner's pair, not that the pair is
the faces' (probe: it is, 0.4 and 0.8); `test_band_extension_seam.py:130-137` tests the undeclared key
at margin 4 only, so it cannot see the lower-band hole. `engine/tests/` holds one golden
(`sigma_leverage_parity.json`), which pins eight pure functions against a frozen copy; CLAUDE.md §7's
sentence that the goldens under `engine/tests/` *"observe any output-moving change to
campaign-reachable code"* describes a campaign driver that is deleted. Not read in full:
`test_sigma_leverage_parity.py`, `test_knots_ed912.py`, `test_engine_params_bridge.py`,
`test_knot_pool_formula.py`, `test_fractional_pool.py` and `test_dice_engine_properties.py` (test names
and the passages cited above only).

**Performance.** `degree_from_net` ran 4,535 times in the four-season realm against 284 rolls: the rest
is `band_odds` answering the chooser's believed chance. `_net_counts` is cached per dice count and
`_chance_floor_cap` per (pool, ceiling); nothing here is a cost centre (the run took 640 s on a
contended machine for reasons outside this subsystem).

## 5. Design matters

**Ruled, accepted as binding, not re-raised.** TN 7 always (ED-IN-0196). One ladder on the margin, four
universal bands, Partial a whole success wide (2026-08-14, 2026-08-15). Advantage in sigma, as a mean
shift (ED-884, ED-934). An obstacle against a person is their score halved plus that instance's
modifiers. Combat's degree is read off the scene (2026-09-03). No base Ob by scale (2026-09-05).
Investigation is not made a contest to become gradeable. Capability supplies dice and gates nothing.
One engine at two fidelities, with `E[auto | event] ≈ E[played | event]` (the auto/manual duality,
ED-SC-0013, ruled 2026-07-08). The continuous engine as the videogame's specification (ED-833,
2026-05-15), which the built social roll departs from (§11).

**Where ruling and code agree.** All of the above are executed by the code read, with the exceptions in
§3.

**Where they disagree, and which the game follows.**
- *"No system keeps its own bands"* against mass battle's `massbattle.py:77-89`, which labels a finished
  battle Overwhelming / Success / Partial / Failure by survivor ratios under the ladder's four names.
  The game follows the code; the season does not read that label (`field_degree` reads
  `attacker_wins`), so the cost is a vocabulary collision for anyone reading a battle result (MB lane).
- *"ONE resolver for all d10 probability"* against three samplers (F-DICE-05, F-DICE-07).
- PP-232's *Ob minimum 1* (`OB_MIN`) against a composed obstacle of 0.5 for a subject with a score of 1
  (`roll.py:119-120` says so itself). The fractional-obstacle ruling is later and governs; `OB_MIN` is
  the floor a favourable modifier may not push below, which is how the code uses it.
- ED-833 (every system samples the Normal in the videogame) against the social roll and the field,
  which deal whole dice (F-DICE-05; §11).

**Where the design set (archived, intent only) and the code disagree.** Read in full: the four
documents under `.designs/engine/` and `auto_manual_resolution_duality_v1.md`; read at the passages a
search for the resolution terms returned: `videogame_mode_spec.md` (§3, §4), `complete_systems_reference.md`,
`engine_atlas_v1.md`, `cogload_moderate_target.md`, `throughlines_complete.md`; searched and found to
carry nothing on the draw: the remaining seven.
- *Pool regime.* The design's pools were an attribute doubled plus history, floor five; the built social
  pool is the score (F-DICE-02). The game follows the code.
- *Advantage contributors.* The armature's porting interface (§D) asks each system for a **signed**
  set of contributors, **gated** by the state they are relevant in. The built channel is unsigned and
  has one ungated member (F-DICE-06). The intent and resolution 17 agree.
- *The obstacle against a person.* `videogame_mode_spec.md:174` writes `floor(stat/2) + modifier`; the
  code halves without flooring, on the later fractional-obstacle ruling. The code governs.
- *Disposition lowers the obstacle.* `complete_systems_reference.md:197` (`Ob = max(1, base − Disp)`) is
  the retracted Ob-reduction form; the case corpus's SCN-04 inherits it. Superseded by the mean-shift
  ruling; the lawful form is an instance modifier on the opposing side or a named level (§13).
- *The dice as a Godot autoload.* `sim_reference_README.md` maps the dice to an autoload; the package's
  own head and `holonic_ARCHITECTURE.md` §47 say never. Layer 1 governs.
- *"All modules are stubs" and the PROVISIONAL status vocabulary* (`sim_reference_CONVENTIONS.md`) are
  where `engine/dice_engine/__init__.py:8`'s stale status line comes from (F-DICE-13).

**Five properties, as evidence for the NERS reading.**

| property | finding | lands on |
|---|---|---|
| P-i legible odds | The engine can state exact odds (`band_odds`, `odds_of`); a person at the play surface holds `View.odds`, his believed chance. Advantage is a named level end to end. The Normal closed form understates the whole-dice roll by 4 to 17 points (E-16) and has no game caller. No surface prints a chance to anyone. | E-legibility: the engine is ready, the surface is absent |
| P-ii uniform leverage | Exact for the sigma channel on the floored pool (0.4823 z at every pool from 0.25 to 16). Not uniform for the room (F-DICE-10). On whole dice one level buys 11.6 to 19.9 points of Partial-or-better across pools 1 to 8: the z is uniform, the points are not, as on any bell. | S |
| P-iii bounded, monotonic | Holds (steelman 5). One non-monotone cell, recorded at B10-08 and re-confirmed: with effort, the chance at each pool's own cap reads 21.57 / 20.37 / 18.76 / 20.56 % at pools 1 to 4. | R-complete |
| P-iv graded, recoverable | Four bands from every margin; a failed act can be re-formed next season; an impossible act is refused, not rolled. Against that: the top band is unreachable at the shipped pair, and combat and the field do not return the four bands (by ruling). | R-complete |
| P-v right engine | Three samplers for one quantity; a fractional pool has three meanings; the rate draws of §1.2 are a second kind of draw with one keyed owner and no graded output. | S |

**NERS cut on the design objects.**
- *The margin ladder.* Cut it and each scale re-bands (the August census found eight ladders in seven
  classes). N holds in every direction for providers that return a margin. Survives.
- *The sigma channel.* N as a mechanism (one unit for every modifier at every pool size). In the season
  it is a claimed possibility with no producer in play: narrowed until a source carries something
  (F-DICE-06). What the cut would lose today: nothing observable.
- *The exact odds function.* N: cut it and the chooser's believed chance and any display fall back on a
  closed form 12 points wrong at the shipped pair. Survives.
- *The fraction of a margin.* N: cut it and Ob 1.5 plays as Ob 2 (the sawtooth the IN research lane
  measured on 2026-10-16; at HEAD equal-skill odds fall smoothly, E-07). Survives.
- *`BandExtension`.* A ruled seam (ED-SC-0032) whose only client is outside the loop. What dies if it is
  cut: the kernel's de-saturation and nothing in the game. It stays because the ruling asked for the
  seam; it is not yet game.
- *The Normal sampler.* N for combat (a continuous net feeds a continuous damage tail); for everything
  else it is a second convention. Narrowed to combat.
- *E, scored last as a ratio.* Against what N and R found: the two files carry one ladder, one face
  rule, one odds function and one advantage unit for every scale, in under 800 lines. The overhead is
  the unreached half of `sigma_leverage.py` and mass battle's copy.

**Design that exists only as prose.** A per-roll display of odds to the player (the engine function
exists; no surface). A second advantage source. An uncertainty floor for the social roll: combat has a
5 % upset floor (`modules/combat/config.py:295`, a designer rule), the social roll has certain-zero
cells and refuses the impossible, so the floor differs by resolver (D_T01 row 3). Fifty-three of 67
verbs take no draw, so an *implementation* that can fail after a won contest (ARC-06) has no carrier.

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Items listed in the dossier

| item | listed | verified | evidence | action |
|---|---|---|---|---|
| H-31 the margin model | open, `assumption` | superseded | The rulings of 2026-08-14 and 2026-08-15 fix `margin = net − ob` and the four edges; the code is that form; the row's other sweep arms are not live options | regrade `ruled`, citing the archive's *Resolver architecture — RULED* |
| H-88 the seam does not dispatch | open, `assumption` | closed | `seam/contest.py:245-283` dispatches by manifest row; E-02 graded margins, fields and scenes from computed play; the row's own 2026-10-26 correction says so | close the row |
| H-98 the fourth combat band | open, `absent`; blocks R-09 | irrelevant | Combat's three bands are data (`rosters.yaml: combat_band_edges`) and ruled off the scene; no verb row keys a fourth; the row itself says it is *"NOT invented"* | close; remove from R-09's `blocks:` (resolution 15) |
| H-114 `_eff_kill` takes no degree | open? | closed | `loop/effects_combat.py:63` takes `res`; the row records closure by `W-E` | none; the row's head should say CLOSED |
| H-115 degree branches raise `SystemExit` | open? | closed | `data/verbs.py:382-424` raise `Unspecified` | none (the row says so in its body) |
| H-152 a `total`-arm march death emits no `person.died` | open, `assumption` | wrongly filed (MB / core effects; no dice mechanism). `march`'s row now emits `person.died` and `tenure.closed` (E-09) `[UNVERIFIED at _eff_march's total branch]` | E-09 | the MB lane verifies and closes |
| H-244 what one slot of effort is worth | closed? | open as a number; built | `fixtures.py:466`; no roll of 568 carried effort (the chooser priced effort variants of `determine` only, E-19) | keep; its value is unexercised in play until a believed opposition exists |
| H-310 a confession graded by the dice alone | open, RULING | wrongly filed (FI / SC) | The mechanism a ruling would need exists: an instance modifier on the obstacle, as `forgery_quality` is for `examine` | that lane's; cross-listed in §10 |
| H-312 `interrogate` has no contest key | open | open; resolved by proposal | E-09 | `10_DICE_one_score_two_roles.md` edit C |
| H-126, H-127, H-213 (bear on findings) | `assumption` | open as numbers | E-03, E-07; ceiling caps of 2.842 observed in play | H-127's scope narrowed by the same proposal |
| H-332, H-349, H-361 (secondary) | — | not adjudicated here | excerpts only; none bears on a finding | their primary lanes |
| CP-T01-01 `faculty` | CLOSED (B10-08) | closed | `pool.py:78` | none |
| CP-T01-02 practice | CLOSED | closed, and observed | four pool-3 rolls, seed 0, seasons 3–4 | none |
| CP-T01-03 `band_odds`, `odds_of` | CLOSED | closed; mode (b) built later under CR-17 | `sigma.py:260`, `:350` | none |
| CP-T01-05 effort | CLOSED | closed; unexercised in computed play | E-02 | see H-244 |
| CP-T01-06 the per-pool ceiling | CLOSED | closed, and observed | Ob 2.842 on 17 realm rolls | none |
| CR-17 believed odds | LANDED | closed | `sigma.py:420-448` | none |

### 6.2 Resolutions (every inconsistency, gap and unclear passage found)

| # | what | kind | decided resolution | ladder step | carried by |
|---|---|---|---|---|---|
| 1 | Mass battle's private roller, ladder copy and sigma functions | two owners | Mass battle calls the owner; the 1e-9 tolerance moves into `degree_from_net` | 3 (ruling 2026-08-15), 4 (the other two modules import the engine) | `proposals/10_DICE_one_roller_one_fraction_rule.md` |
| 2 | The single-owner sweep cannot observe a tolerance | gap in a test | Resolved by 1 (the copy is gone); no new test | 5 | same |
| 3 | A fraction of a die has three meanings | inconsistency | On whole dice, the fraction is one more die with that probability; `band_odds` enumerates the mixture | 4 (`settle_margin`'s rule for a fraction of a margin) | same |
| 4 | Half-to-even rounding of a pool | defect | Removed by 3 | 5 | same |
| 5 | The Normal sampler reads half a success harder than whole dice | inconsistency | Leave the offset (combat is tuned on it; nothing compares the two); correct the two claims; name the sampler per provider. The narrowing of ED-833 is in §11 | 1 (the later ratified build of the social roll), 5 | `proposals/10_DICE_exported_face_rule_and_band_edges.md` |
| 6 | Face rule, band edges and `LEVEL_SIGMA` not exported | gap | Module-scope literals at the owner; an assertion ties the per-die pair to the faces | 3 (`04:181`, CLAUDE.md §0.05) | same |
| 7 | Resolver names: `dice_pool` / `d10_sigma` / `d_sigma`, and a stale combat comment | inconsistency | One vocabulary of three in `module_contracts.yaml`, matched by the wrappers | 5 | same |
| 8 | A person with no score is opposed at the non-person stand-in; holding a score lowers the obstacle | inconsistency | One score, two roles: the opposing score is the pool's base; the stand-in is for non-persons, as H-127 says | 3 (the ruling; H-127's own text), 4 (combat) | `proposals/10_DICE_one_score_two_roles.md` |
| 9 | The room moves the obstacle by a flat amount | unclear (is it advantage?) | It is an instance modifier under the ruling; accepted as built; the measured non-uniformity goes into H-215's `cite:` | 3 | none (a register sentence) |
| 10 | Four rolled verbs name no key | gap | `lie: copying`, `interrogate: inquiry`, `arrest: arms`, `determine: argue`, each `assumption` under H-126 | 4 (`tell`, the inquiries, `fight`) | `proposals/10_DICE_one_score_two_roles.md` |
| 11 | Context keys swallowed below the top band and with no extension | defect against the docstring | `degree_from_net` validates context on entry; context with `extension=None` raises `TypeError` | 5 | none (a six-line edit at `dice_engine.py:291`; stated here) |
| 12 | `contest()`'s unread `extension` parameter | dead code | Delete the parameter and the word in the docstring | 5 | none (edit at `seam/contest.py:184`) |
| 13 | `band_odds` says combat reads `p_success` | false sentence | Reword: *"the Normal closed form, kept for the parity golden; no game path calls it"* | 5 | none (edit at `sigma_leverage.py:359`) |
| 14 | The stale passages of F-DICE-13 | unclear | Each corrected at its line; `requirements.yaml`'s social-contest note to *"provider built (`modules/social_contest/roll.py`); the kernel is not reached"* | 1 | none (edits listed in F-DICE-13) |
| 15 | H-98 blocks R-09 on a band nothing consumes | wrongly stated blocker | Close H-98; R-09 then rests on its own measure (two actors at different pools; a non-combat verb at two bands whose writes differ, which `argue` meets in the corpus, E-13) | 2 | none (two register edits) |
| 16 | H-31 graded `assumption` on a ruled form | stale grade | `ruled` | 1 | none |
| 17 | The advantage channel cannot count against the actor | gap | Sources return levels for and against; the owner's two-list signature is used | 4 (`levels_to_net_sigma`'s own signature) | `proposals/10_DICE_advantage_sources_for_the_arcs.md` |
| 18 | A wound changes no later roll | gap | `wounds` as the second advantage source | 4 (the roster's note names how a source lands) | same |
| 19 | SCN-05's *"automatic successes at one unit per success"* | need stated in a retired dialect | A spent resource buys named levels, as `effort` spends slots | 3 (advantage is a mean shift) | same |
| 20 | `OB_MIN` cited as *"Ob minimum"* while a composed obstacle reaches 0.5 | unclear | `OB_MIN` is the floor a favourable modifier may not push below; reword the tag at `sigma_leverage.py:114` | 1 (the fractional-obstacle ruling is later) | none (a comment) |
| 21 | CLAUDE.md §7 describes goldens under `engine/tests/` that observe campaign-reachable code | stale Layer 0 sentence | Reword to what the directory holds (one parity golden over pure functions) | 2 | none (Layer 0 is the orchestrator's to edit) |
| 22 | Mass battle labels a finished battle with the ladder's four names on other thresholds | vocabulary collision | Rename the survivor-ratio label's values in `massbattle.py` (MB lane) | 3 (*"No system keeps its own bands"*) | cross-listed to MB |

| 23 | A person who holds no claim about an opponent gets no believed chance, and the chooser reads that as 1 | gap; unclear polarity | He assumes an ordinary person (`pool_default`), from the fixtures, never the World | 4 (`faculty`'s own fallback) | `proposals/10_DICE_believed_odds_have_a_prior.md` |
| 24 | No believed estimate exists for a fight or a field | gap | The interface is stated (a `believed_estimate` provider role returning shares over the provider's own bands); the build is PC's and MB's | 5 | same, edit C |
| 25 | Nothing of a roll survives it but the band | gap | The record the provider already returns is the reason trail; one optional field on the graded act's first Event, proposed to CORE | 5 | same, edit D |

Resolutions decided: 25. One (resolution 5, in part) narrows a Jordan decision and is listed in §11;
none of the others overwrites ratified canon or a `(RULED)` item.

## 7. Research transfer

Read: `research/00_INDEX.md`; `research/by_lane/README.md`; `research/by_lane/IN_infrastructure.md` (its
kernel rows, §9.1 and §9.2); `research/game_precedent_suite/dispositions/D_T01.md` in full;
`research/valoria_game_precedent_companion_v1_part3.md` §7.9 and `_part4.md` I-5 to I-9;
`research/historical/mass_battle_gauge_grounding.md` §1 (head). `[SKIPPED: research/provenance/, the
historical corpora and the companion's other parts — the index places no resolution-kernel material in
them (`00_INDEX.md` §3, the "Resolution kernel" row), and none bore on a finding.]`

**Precedents that change what to build.**
- *Baldur's Gate 3, Disco Elysium (shown odds; D_T01 rows 6, 24).* Both show the player the chance.
  Transfer: the engine's odds function exists and is exact; what is missing is a surface. It also
  fixes which function a surface must call: never `p_success` (12 points low at the shipped pair).
- *Blades in the Dark, PbtA (the complication band is modal, 41 to 45 %; D_T01 rows 10, 12, 29).*
  Transfer by contrast: under the ruled ladder Partial is 19 % at the shipped pair and never modal at
  any pool from 1 to 8 against Ob 1 to 4. The ruling is not re-raised; the measured cost is that the
  band most able to generate material is the rare one. Proposal 2 raises it to 32 % for person-opposed
  rolls without touching the ladder.
- *The IN lane's own B-instrument (2026-10-16, §9.1), the odds sawtooth.* Superseded by code: re-run at
  HEAD, equal-skill odds fall smoothly (65.0 → 43.9 % over scores 1 to 8). The fraction rule landed
  after that reading. What remains of it is a different shape: at equal skill the higher the score the
  worse the actor's odds, because the obstacle grows at 0.5 per point and the mean at 0.4.
- *COMP-3 §7.9 and I-7 (the Partial band falls as pools grow).* Confirmed at HEAD under the
  opponent-scaled obstacle (40.0 → 16.1 % over equal scores 1 to 8). Its remedy, a band width that
  scales with the pool, contradicts a ruling and is not proposed. On an attribute scale of 1 to 7 the
  band stays between 17 and 40 %.

- *The campaign simulator's through-line, "rich engine, starved input"* (`mc_v18_walkthrough.md` §7,
  2026-07-16: a 1,905-line battle engine fed one rounded scalar per side). Historical, and it
  transfers exactly: the season loop repeats it one level down, an exact odds function and a sigma
  channel fed a constant pool and a zero leverage (F-DICE-01). What it changes: the next build in this
  subsystem is an input, not a mechanism.
- *The auto/manual duality (ED-SC-0013; Football Manager's three fidelities of one match engine).*
  `[CORRECTED 2026-11-12, audits/24_GROUNDING_GAMES.md GC-3: the Football Manager half is not established.
  The tree's own check marks it CONTRADICTS (research/game_precedent_suite/dispositions/D_T04.md row 58;
  tutorials/T16:79), and a second attempt found no Sports Interactive statement
  (grounding/football_manager_instant_result.md). The duality stands on the ruling ED-SC-0013 alone.]`
  Transfer: the calibration constraint is met by construction only if both fidelities of an event draw
  from one sampler. That is why F-DICE-05 is filed above hygiene: a played social scene built on the
  Normal sampler beside an automated one on whole dice would be mode-shopping by 7 to 12 points.

**Tried and did not transfer.**
- *Karmic dice, pseudo-random distribution, shuffle bags, pity timers, XCOM's hidden aim assist (D_T01
  rows 5, 17, 19, 20, 27).* Each is memory in the generator. Layer 1's AX-7 excludes state hidden from
  the player, and the keyed per-act draw is what keeps a new verb from moving old outcomes. Null.
- *Position and effect, the devil's bargain (rows 13, 14).* Both need someone reading the fiction; no
  GM. The one part that transfers is already built: `effort` is a stated cost for better odds.
- *`MBG` §1 (draws near parity are expected).* It grounds the mass-battle gauge, not the d10. Decorative
  for this subsystem.
- *Duel of Wits' scaled compromise (I-5).* A social-contest design object; nothing in the dice.

**From the surviving audit corpus** (`.audit/`, lesser weight; each re-verified before use). Read: the
degree census's findings in full and its instrument's head; the re-band cost instrument
(`.audit/2026-08-14-degree-reband-consumer-cost/reband_delta.py`, a script; its docstring); the two
combat-engine audits at the passages a search for the resolution terms returned. Three leads, all of
which still hold at HEAD and are folded into F-DICE-05, F-DICE-07 and F-DICE-12. One old finding is now
false: the census's 45 % divergence of the faction ladder describes code deleted at plan position
`29b`. Its method transfers and is used here: classes computed by evaluating imported functions, on
more than one domain, with a warning when the domains disagree. Its own limit also transfers, as a
caution: a grid of exactly representable values cannot see a tolerance.

**Nulls.** No surveyed game governs its own resolver by refusal (COMP-3 §7.9 says so and it stands).
No precedent in the corpus addresses one engine serving a duel, a debate and a battle with comparable
odds; the tree's answer (one ladder, per-provider samplers) is its own. No corpus is dedicated to the
kernel (`IN_infrastructure.md:105`): the d10's parameters have no calibration target, here or anywhere
in `research/`.

## 8. Best path forward

Ordered. *Alone* marks what the subsystem needs to run well by itself; *compose* what it needs from, or
gives to, another lane.

| # | change | file | gate (execution artifact) | unblocks | cost |
|---|---|---|---|---|---|
| 1 | *Alone.* Face rule, band edges and named levels as exported literals; correct the two equivalence claims; one resolver vocabulary | `engine/dice_engine/*.py`, `references/module_contracts.yaml`, three wrapper strings | `export_sim_params --check` shows three new keys; season hash equal | the port gate; a correct odds display | edit |
| 2 | *Alone.* Context validated on entry; dead `extension` parameter deleted; false sentences corrected (resolutions 11 to 14, 20) | `dice_engine.py`, `seam/contest.py`, comments | the lower-band probe of E-04 raises; season hash equal | — | edit |
| 3 | *Compose (MB).* One roller, one ladder class, one fraction rule | `dice_engine.py`, `sigma_leverage.py`, `modules/mass_battle/resolution.py` | mass-battle goldens and the season hash byte-equal; `grep "randint(1, 10)"` prints one line | R-04's field on the same dice; the port | small build |
| 4 | *Compose (IN).* One score, two roles; four verb rows | `seam/wrappers/pool.py`, `sigma.py`, `rosters.yaml` | control arm reproduces today's hash; `odds_of` falsifier of the proposal | R-09 (a score matters in both roles), R-05 | edit, a declared mover |
| 5 | *Compose (CHAR).* Authored `stats:` for the cast, or a generation rule, and `cast_attributes` on | `references/npc_registry.yaml`, `harness/populated.py` | `aperture 4 0`: *"two actors at different pools: yes"* on a non-combat verb | R-09's by-person conjunct, R-06 | design-first (content is Jordan's) |
| 6 | *Compose (PC).* A signed advantage channel and `wounds` | `sigma.py`, `rosters.yaml`, `fixtures.py` | nonzero leverage on a graded roll in `aperture`; control arm hash equal | R-02 (a fight's result reaches a later debate), ARC-53 | small build |
| 7 | *Compose (CORE / GO).* A surface that prints `odds_of` for an act the player is about to choose | the play surface's client, not the engine | a headless callback that reads `v.odds` and logs it beside the dealt band | NERS-E; the playable test of §9 | small build |
| 7b | *Compose (CHAR).* Believed odds have a prior | `sigma.py::believed_input`, one fixture | the spy of E-19 returns figures for `argue` and `arrest`; control arm hash equal | R-08 (a belief that can be wrong for a reason) | edit, a declared mover |
| 8 | *Alone, later.* Delete the unreached advantage surface with the kernel | `sigma_leverage.py`, the parity golden | the golden's function floor drops by three; nothing else moves | — | deletion, on Jordan's timing (SM-15) |

Steps 1 and 2 move no hash and can land first. Step 4 before step 5: otherwise authoring a character
makes her easier to oppose (F-DICE-03).

## 9. Playable standalone and integrated

The standing requirement asks whether each subsystem is a playable game of its own. A resolution
substrate holds no scenario, no state and no ending, and it should not acquire them: that conflict
between the requirement's wording and the subsystem's nature is named here and not resolved. What can
be judged is the unit of play the substrate owes every other subsystem, **one roll as a decision**:
a situation, a real choice, legible odds, stakes, a graded result.

| element | exists today | missing |
|---|---|---|
| entry point | `modules/social_contest/roll.py::roll(inp, rng)` and `sigma_leverage.record_odds`, callable with a hand-built `SocialContestInput` (E-14) | a harness line that deals one named act and prints its record; none exists and none is proposed (a client of `play_surface.py` is the place, step 7) |
| scenario seed | the act's own generator, `H(seed, tick, actor, "roll:…")` | — |
| choice surface | which verb, against whom, and `effort` 0 to 2 (one named level per scene slot spent) | any second lever; at Partial-writing verbs three stacked acts beat effort 2 (59.5 against 57.6 %, H-244), so effort is a real choice only where Success alone writes |
| outcome legibility | `odds_of` mode (a), exact; `View.odds`, the person's believed chance; the band is a word | no surface shows either; the believed chance is `None` against any person (nothing deposits a capability claim) |
| stakes | the verb row's `writes:` and `emits:` by band | Failure writes nothing on the social path; four rolled verbs have identical writes at every band |
| end condition | none, correctly: a roll ends when it is graded | — |
| instrument | `aperture`'s `POOLS ROLLED` and `DEGREES RESOLVED` lines; `corpus_run`'s `DEGREES RESOLVED BY VERB` | a reading of leverage (always 0 today) |

**One code path.** Yes for the social roll: the standalone call above and the loop run the same module
entry, typed input to typed outcome, no held state, reached by composition row; realised frequencies
match in both. For a fight and a field the question belongs to the PC and MB lanes; from this side,
neither returns a margin and each draws from its own sampler.

**Layer 1.** `engine/dice_engine/` is correctly not a module. The registered module that rolls,
`modules/social_contest/roll.py`, conforms: typed record in, `Margin` out, no token, no state, the
generator passed down. Deviations are the wrapper's `World` read (declared) and `04:181` / `04:778`
(unmet, §4).

**Integrated.** Executed edges: the fold constructs the generator, the provider returns the pair, the
ladder grades it, the verb row's band cells write and emit, witnesses deposit. All observed in E-02.

**No GM.** Nothing in the roll needs one. What a GM would supply at a table and the engine does not is
*position*: how bad a failure is here. The engine's answer is the verb row's fixed table.

**Ordered work to close the gaps:** steps 4, 5, 6 and 7 of §8, in that order.

## 10. Interfaces

| with | DICE consumes | DICE emits | real or designed |
|---|---|---|---|
| CORE (fold, seam) | the act's generator; verb, subject, effort; fixtures | `Margin`; `settled_margin`; a band label | real (568 rolls observed) |
| CHAR (persons) | `Person.capability`, `Person.attributes`, the act log (practice) | believed chance to the chooser (`View.odds`) | real as wiring; the attribute read returned nothing for 83 of 83 |
| SC (social contest module) | the composed obstacle (score/2, room, forgery, ceiling) | `roll_net`, `net_boost`, `band_odds`, `OB_MIN` | real |
| FI (inquiries) | `graded_inquiries` routes; a Record's `forgery_quality` | the same roll, no prize | real (`research`, `surveil`, `examine` graded) |
| PC (combat) | — | `roll_net_continuous`, `degree_from_net`, `soft_cap`, `sigma_n`, the band enum | real (seven Normal draws, seed 1); combat's scene bands are its own |
| MB (mass battle) | — | nothing by import | designed only: the ruling says one resolver; the code keeps a copy (F-DICE-07) |
| FA, SE, WR | — | — | none: no faction, settlement or world act rolls except through a person's act |
| GO (port) | — | `sim_params.json` (six scalars), `game_constants.json` (`TN_STANDARD`) | real as artifacts; no face rule, edges or levels (F-DICE-09) |

Cross-listed: H-310 (a confession's truth as an obstacle modifier) to FI / SC; resolution 22 to MB;
the `ob_from_defender` half of resolution 8 to PC.

## 11. Survivors for Jordan

One, listed because its resolution narrows a decision of his.

**Which sampler the videogame's non-combat rolls use (ED-833 against the built social roll).**
ED-833 (2026-05-15) adopted the Normal sampler as the specification for every system in the videogame.
The social roll was built on whole dice after ED-SC-0037 (2026-09-09), and B10-08's exact odds and
fraction rule, ratified on merge, are whole-dice mechanisms. The two are not interchangeable: at the
shipped pair the whole dice fail 74.0 % of the time and the Normal sampler 85.6 % (E-06).

- **Option A, as built (decided here, ladder step 1).** Whole dice for the social roll and the field;
  the Normal sampler for personal combat only. As a game: odds a player can count (*two dice, two
  successes needed*), exact and displayable; a fraction of an obstacle paid in probability; leverage
  uniform in z but lumpy in points at small pools. The port carries two samplers.
- **Option B, as ED-833 reads.** Every provider samples the Normal. As a game: fractional pools and
  obstacles are native, leverage is exactly uniform at every pool, the fraction rule and the exact
  enumeration are deleted in favour of a closed form; no dice exist to show; and unless the sampler is
  re-centred by half a success every non-combat act becomes about ten points harder than today. The
  port carries one sampler. Every season hash moves.

Proposal `10_DICE_exported_face_rule_and_band_edges.md` is written for A and says which of its edits
depend on it. Under either option the half-success offset between the two samplers can be closed in the
sampler (F-DICE-05); under A that is a combat balance move for the PC lane, under B it decides whether
every non-combat roll gets about ten points harder.

Three other items are declared movers taken at step 3 or 4 and marked `[ASSUMPTION; Jordan to correct]`
in their proposals, each with a control arm that reproduces today's bytes: the opposition fallback
(person-opposed rolls go from 26 % to 58 % Partial-or-better), the wound level and the believed prior.
None overwrites a ruling; each changes how often things happen, so they are named here for visibility
and not as questions.

## 12. Evidence log

All runs with `PYTHONHASHSEED=0`. Scratchpad:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/DICE/`.

| id | command or probe | seed · seasons | outcome |
|---|---|---|---|
| E-01 | `python -m engine.season.harness.register --requirements` | — | exit 0; R-09 `partial` (`requirements.txt`) |
| E-02 | `probe_rollers.py` (wraps the three rollers and `degree_of`, runs `populated.run`) | 0 · 2; 0 · 4; 1 · 2 | §1.3 (`rollers_4_0.txt`, `rollers_2_1.txt`; the 0 · 2 figures from the same script's console) |
| E-03 | inline: `build_realm(0)`, capability and attribute census, `faculty` per verb | 0 · build | 83 persons; capability on 2; attributes on 0; pool 2 for all |
| E-04 | `probe_props.py`: ladder owner against mass battle's copy; float edge; extension context | — | 6 / 10,000 and 72 / 160,000 cells differ; context swallowed below margin 3 (`props.txt`) |
| E-05 | `probe_props.py` and inline: fractional pool, rounding against the stochastic die | — | 26.00 / 32.86 %, 40.00 / 33.14 % (`engines.txt`) |
| E-06 | inline: whole dice against the Normal sampler, closed form and sampled | 7 · n 200,000 | Failure 38.59 against 46.42 % at pool 8, Ob 3 (`engines.txt`) |
| E-07 | inline: equal-skill table; the opposition inversion | — | 26.00 / 58.00 / 73.50 % |
| E-08 | `probe_props.py`: room against effort, by pool | — | 1.25 to 0.44 z against 0.48 z |
| E-09 | inline: rolled verbs, keys, `advantage_sources`, band-keyed writes | — | 14 of 67 roll; five name no key; `('effort',)` |
| E-10 | seven `tools/export_*.py --check`; grep for readers of each artifact | — | all exit 0; three artifacts have no engine or module reader |
| E-11 | inline: `sim_params.json` rows for the dice engine; annotated constants skipped | — | six scalars; two skipped tree-wide, one of them `LEVEL_SIGMA` |
| E-12 | `python -m engine.season.harness.aperture 1 0` | 0 · 1 | exit 0; `POOLS ROLLED [2]`, *"different pools: no"* (`aperture_1_0.txt`) |
| E-13 | `python -m engine.season.harness.corpus_run`, read from the CORE lane's run (`runs/CORE/corpus_run.txt`), not re-run | 0 · per case | `DEGREES RESOLVED` as in §1.3 |
| E-14 | inline: the module entry alone | 0 · n 200,000 | 56.76 / 25.88 / 16.81 / 0.55 % against 56.54 / 26.09 / 16.82 / 0.55 |
| E-15 | inline scan of `engine/season/cases/**/*.yaml` `need:` rows | — | 973 rows; 96 name a draw, a degree or a modifier |
| E-16 | `probe_props.py`: `band_odds` against `p_success`; named levels; monotonicity; ceiling | — | `props.txt` |
| E-17 | grep censuses: callers of the display functions, `capped=False`, `BandExtension`, draw sites | — | as cited in §3 |
| E-18 | `git status --short` | — | this file and five proposal files are the lane's only changes |
| E-19 | inline: `sigma.believed_chance` spied during `populated.run(1, 0)` | 0 · 1 | 4,929 queries; 102 figures (`determine`); `None` for `march` 3,813 and `accept` 1,014 |
| E-21 | `.audit/` entries read (§7): the degree census, the re-band instrument, two combat audits (searched) | — | three leads re-verified at HEAD; one old finding now false |
| E-20 | design set read (§5): four files under `.designs/engine/` and the duality doctrine in full; five cross-cutting files at their resolution passages; seven searched | — | intent only; the disagreements are listed in §5 |

Not run: `pytest` (by instruction); `aperture 4 0` (R-09's own measure; the CORE lane's run had not
finished when this was written, and the four-season probe of E-02 reads the same realm).

## 13. Provided arcs and characters — adjudication

`CASE_BRIEF.md` read; the corpus scanned (E-15). The exercises overlay is authored for 35 of 292 NPC
rows and 0 of 611 ARC rows (`runs/CORE/exercises.txt`), so no case row here is routed to a verdict by
the tree's own instrument; what follows is this lane's reading of the needs whose mechanism is the draw.
Needs whose mechanism is a clock, a seat, a ledger or a scene structure are other lanes' even where the
word *roll* appears in them.

| case | need (short) | hardness | represented today? | evidence | change required | owner | proposal | gate |
|---|---|---|---|---|---|---|---|---|
| ARC-22, NSC-04, NSC-07, SCN-01, ARC-10 | one roll resolves to four graded outcomes with different consequences | core / important | partly: four bands exist and three occur; the fourth is unreachable at the shipped pair; four rolled verbs write the same at every band | E-02 (O 0 of 568), E-13 (`BANDS THAT DIFFER`) | a score above 2 or an obstacle below 2 for someone; band-distinct writes on `lie`, `speak`, `tell`, `interrogate` | CHAR (scores), SC / FI (rows) | `10_DICE_one_score_two_roles.md` for the obstacle | `DEGREES RESOLVED` shows Overwhelming on a non-combat verb in a realm run |
| ARC-18 | a failed roll leaves the situation unchanged | important | yes | Failure writes nothing on the social path (E-13) | none | — | — | — |
| ARC-06 | an implementation can fail on its own roll, independent of the contest before it | core | no: 53 of 67 verbs take no draw; the implementing verbs are deterministic | E-09 | a `graded_inquiries`-style route for the implementing verb (a row, not code) | CORE / SC | none here | the verb appears in `DEGREES RESOLVED BY VERB` |
| ARC-17 | detection by repeated checks over seasons, persistence not certainty | important | yes | per-act keyed draws, memoryless; `surveil` graded 236 times in the corpus | none | — | — | — |
| SCN-04 | difficulty derived from a stored disposition between the two | core | partly: a bench's regard moves the obstacle (`reception`); a hearer's own stance toward the speaker does not | Ob 1.536 and 2.842 in E-02 | an instance modifier reading the subject's standing toward the actor, in `roll.py::obstacle` | SC | none here | an obstacle that differs for two speakers at one hearer |
| ARC-53 (two rows) | a wound from a personal contest persists as a penalty on later rolls at another scale; a faction's stat adds to its leader's roll | core | no | leverage 0.0 on 568 of 568 | `wounds` as an advantage source; the faction half restated as dice from the seat (a pool addend) | IN, then FA | `10_DICE_advantage_sources_for_the_arcs.md` | nonzero leverage for a wounded actor |
| NPC-085 | precedent correctly cited improves an advocate's odds | core | no | one advantage source | an advantage source reading a determined matter | SC (waits on `Tenure.degree`, H-162) | same, table E | — |
| SCN-12 | a third party's support eases a formal contest; a named character's conditional bonus | important | no | same | an advantage source reading a commitment of support | SC / FA | same, table E | — |
| SCN-04, SCN-07, SCN-LOOP-C | a stacking penalty from a spent personal resource, feeding back on the same rolls | core | no: no such carrier | — | a strain carrier, then a source; the soft cap bounds the loop | CHAR | same, table E | — |
| SCN-13 | helpers add `floor(stat/2)` dice to an anchor | core | no: threadwork is outside the loop | `systems/threadwork/sim/` calls `roll_pool` directly | a pool addend over a collective act | WR / FI | same, table E | — |
| SCN-05 | successes bought before the roll at one unit each | core | no, and **wrongly stated**: a flat bonus on the net is a retired form | `resolution-diagnostic` §2 | restate as named levels bought | IN | same, resolution 19 | — |
| SCN-02 | one aggregate roll per window with difficulty the sum of the sub-actions' | core | no, and it **conflicts with a ruling**: obstacles are per matter and nothing composes them across a bundle (ED-SC-0038, `roll.py:105-106`) | — | named, not resolved | SC | — | — |
| ARC-23 | an uninvested skill gates whether an attempt can be made | core | no, and it **conflicts with a ruling**: capability supplies dice and gates nothing | `rosters.yaml:1500-1502` | named, not resolved; the nearest lawful form is S27.4 (an attempt at Ob > 2 × pool is refused) | CHAR | — | — |
| EMG-C2, NSC-05, SCN-08, NPC-052 | a per-use or per-season chance of a separate event | important / core | the mechanism exists (a keyed rate draw: body hazard, confide, intent, weather); none of these four events is a row, and all four built rates ship at 0 | `fixtures.py:535`, `:690-691`, `:937`, `:1040` | a rate fixture and its event per need | WR / CORE | none here | the event kind appears in a realm log |
| EMG-X5, EMG-X7, SCN-07 | a randomised table of outcomes on a threshold crossing | important / flavour | partly: the weather draw is a keyed table draw (`world_q.py:1205`); no other table exists | — | a table fixture per need | WR | none here | — |
| NPC-001, NPC-004, NPC-075, ARC-22 (lead's loyalty) | a character's competence decides how she fares | core | no: every person rolls the default | E-03 | authored `stats:` and the switch | CHAR | `10_DICE_one_score_two_roles.md` is the precondition | *"two actors at different pools: yes"* |
| EMG-X6 | an especially decisive margin triggers a side effect regardless of who wins | core | partly: the settled margin is on the record (`settled_margin`); nothing reads its size beyond the band | `sigma.py:554-555` | an effect reading the margin, or Overwhelming as the trigger | SC | none here | — |

**Needs wrongly stated, and the resolution.** SCN-05 (above, resolution 19). ARC-02's UNCLEAR row
(a trajectory *"resolved by GM judgment"*): there is no GM; the lawful reading is the chooser's ranked
draw over the person's own pursuits, which is the character lane's. SCN-09's *"success probability
representable as an explicit range varying with pool size"* is met by `band_odds` and needs nothing.

**Arcs this lane can bring up soonest** (the draw's part only; no arc is simulated end to end by a
change in the dice alone, since each also needs its verbs, seats or clocks):

1. ARC-18, ARC-17: already represented; nothing to build.
2. ARC-53: after `10_DICE_advantage_sources_for_the_arcs.md` (the wound half). Dependency: a fight must
   occur in the arc's run (PC), and the faction half needs FA's seat addend.
3. ARC-22, ARC-10, NSC-04, NSC-07: after `10_DICE_one_score_two_roles.md` **and** CHAR's scores (so the
   fourth band is reachable), **and** the SC / FI rows that write differently by band.
4. NPC-085, SCN-12: after SC produces the state their sources read.

**Dependency edges.** CHAR → DICE (scores before the roll can differ by person). DICE proposal 2 →
CHAR (the inversion must be gone before scores are authored). PC → DICE proposal 4 (a wound must
exist). SC → DICE (precedent, support, band-distinct rows). MB ← DICE proposal 1 (the roller).
GO ← DICE proposal 3 (the exported facts).

## 14. Capability authoring surface

### (a) Where this subsystem takes a character capability, what it reads, from where

| point | reads | from | code |
|---|---|---|---|
| the pool (dice) | the vocation's attribute, else the held capability key, else `pool_default`; plus addends | `Person.attributes`, `Person.capability`, `Fixtures.pool_default`; `POOL_ADDENDS` (practice, from the act log) | `seam/wrappers/pool.py:78-100` |
| verb → vocation | which key a verb draws on | `rosters.yaml: verb_capability` | `pool.py:27`, `data/rosters.py` |
| vocation → attribute | which of the ten the pool starts from; which attribute opposes | `rosters.yaml: vocation_attribute` (`opposed_by`) over `references/descriptor_registry.yaml: attributes` | `pool.py:64`, `:73-74` |
| the obstacle | the subject's larger of key and opposing attribute, halved; else `obstacle_default` | the same carriers on the subject | `sigma.py:117-137`, `roll.py:141` |
| advantage | named levels per source | `rosters.yaml: advantage_sources`, `Fixtures.effort_level`, the act's `effort` operand | `sigma.py:140-167` |
| the ceiling | the pool again (the cap solved per pool) | `Fixtures.obstacle_ceiling`, `ceiling_per_pool` | `roll.py:64-86`, `:152-153` |
| growth | `train` (+1 on a held key); practice (dice from recent successes) | `loop/effects_combat.py:794`; `queries/world_q.py:4703` | — |
| combat's pool and Ob | `faculty` per party, then `max(5, faculty + 6)` and `faculty / 2` | `PersonalCombatInput.faculties` | `modules/combat/core.py:54-58`, `:124` |

### (b) Data-driven, hard-coded, doubled

- **Data-driven:** verb → vocation, vocation → attribute, the attribute roster and its scale (1 to 7),
  the advantage roster, every magnitude above (fixtures with register rows), lifepath → starting keys.
- **Hard-coded in a module:** the level table (`LEVEL_SIGMA`, in the engine and not exported); combat's
  `POOL_FLOOR = 5` and `BASE_POOL = 6` (`core.py:51-52`); the binding of a source name to its function
  (`sigma.py:151`, code by design: a source reads state); the divisor 2 in *score / 2* (`roll.py:141`,
  `core.py:124`), which is ruled and is written twice.
- **Doubled:** the opposing score has two readings (social: no fallback, no practice; combat: both;
  F-DICE-03). A person's capability lives in two carriers (`capability` keys and `attributes`), joined
  by `max` at read.

### (c) The interface this subsystem needs

The dice engine needs, per roll, exactly four things from a capability system, and nothing about what a
capability *is*:

```
score(person, verb)      -> whole number   # the dice he brings; also what an opponent halves
addends(person, verb)    -> whole dice     # each from a named, registered source
levels(person, act)      -> (for, against) # named levels only: minor / moderate / strong / major
modifiers(subject, act)  -> obstacle terms # instance modifiers on the opposing side, each named
```

For the subsystem to use a capability, its **definition must say**: its key; its kind (a *score* that
supplies dice, or a *tag* that supplies a named level under a stated condition); its scale (floor and
ceiling in dice, or the level name); which verbs draw on it; what opposes it; and how it grows (the
`train` and practice parameters, or *fixed*). It must **not** say: a flat bonus to a net, a change of
TN, a reduction of an obstacle by the actor, or a gate on attempting (each is excluded by a ruling).

**The single file.** The existing owner is `engine/season/rosters.yaml`: `verb_capability` and
`vocation_attribute` already define a vocation by its verbs, its attribute and its opposition, over the
attribute roster in `references/descriptor_registry.yaml`. What extends it is one block in that file in
which each vocation row carries the fields above (the two present tables are its `verbs:` and
`attribute:` / `opposed_by:` columns), and a `tags:` block whose rows name an `advantage_sources`
member, a level and a condition. No second system: `Person.capability` stays the carrier of scores,
`Person.attributes` of the ten, and a tag is a held key whose row says it yields a level.

### (d) The axioms implemented, in the tradition's vocabulary, and those missing or contradicted

Implemented: **dice pool with counted successes** (d10, success on 7+, a 10 counts twice, a 1 subtracts);
**fixed target number, variable obstacle** (difficulty is the number of successes needed, never the
face); **attribute-or-skill, whichever is higher, gives the pool**; **opposed tests against a static
difficulty derived from the opponent** (half the opponent's score, not an opposed roll); **degrees of
success by margin** (fail, partial, success, critical at +3); **advantage as a shift, with diminishing
returns** (named steps, a soft cap, no stacking to certainty); **minimum pool of one die**; **no test
where success is impossible** (the refusal at twice the pool); **advancement by use** (practice) and
**by training** (+1 on a held skill); **extended effort** (spend more of a scene for better odds).

Lacking, where a designer would expect them: **specialisations or tags** that help under a condition
(the door exists, no row); **wound penalties** (proposal 4); **helping** (no collective act in the
loop); **unskilled use** distinct from the default (an unauthored person and a novice are the same two
dice); **exploding or re-rolled dice and luck points** (excluded by design: no hidden generator state,
and a spend buys levels, not successes); **a critical failure** (a net below zero is not distinguished
from a miss).

Contradicted, by ruling and so not defects: *a skill is required to attempt* (capability gates
nothing); *difficulty by scale of the task* (no base Ob by scale); *a modifier lowers the difficulty*
(the actor's advantage never touches the obstacle).

### (e) Proposals, ordered

1. `proposals/10_DICE_one_score_two_roles.md` — the `score` reader, read in both roles; four verb rows.
2. `proposals/10_DICE_advantage_sources_for_the_arcs.md` — the signed `levels` channel and its second
   member; the table of sources that wait on other lanes' state.
3. `proposals/10_DICE_exported_face_rule_and_band_edges.md` — the level table, the faces and the edges
   where the authoring surface and the port can read them.
4. `proposals/10_DICE_one_roller_one_fraction_rule.md` — so a capability means the same dice in a
   field as in a debate.

The merged authoring file itself (the vocation and tag blocks in `rosters.yaml`) is the holistic
stage's to shape; this section states what the dice need from it and proposes no private scheme.

## 15. The NPC and chooser surface

The statement of the design intent for NPCs and the chooser is the CHAR lane's
(`audits/02_CHAR_audit.md`, its section answering this charge); it is cited here, not redone. What
follows is the dice engine's side of it, from code.

**(a) What the chooser needs from this subsystem, and what it gets.** A person deciding whether to
attempt a contested act needs his chance of the bands in which the act would write, as he believes it,
from his own ledger. The engine supplies exactly that query: `seam/wrappers/sigma.py::believed_chance`,
closed over the person as `View.odds` (`:441-448`), which `decision/choose.py::odds_weight` multiplies
into the pursuit term, and `settle_efforts` uses to decide whether a scene's worth of effort is worth
it. The query is typed correctly (it takes no person, so nobody can ask another's belief) and reads no
World but for his own past acts. What it returns in play is F-DICE-14: a figure for one verb, identical
for every person, and `None`, read as certainty, for the rest. Temperament and conviction do not enter
the roll and should not; they enter the choice. The budget enters as effort: one named level per scene
slot spent.

**(b) One interface for a seated player and an NPC.** Yes, as built. `harness/play_surface.py` hands a
player's callback the same `View`, so the same `odds` query, that the shipped chooser receives. The
sources disagree about what a player should be shown: `odds_of` mode (a), the true odds, is described
as *"the display … the player's"* (`sigma.py:385`), and the B10-08 amendment AM-B-03 planned displays
as mode (a); Layer 1's AX-7 says no state is hidden from the player; the IN research lane observed that
a shown chance can only be the actor's estimate. The ruled and built wins: nothing calls mode (a) from
the loop or the play surface, and what the player's View carries is his believed chance. If true odds
are ever printed to a player, the player and the NPC stop being the same kind of agent on this point;
that is named, not resolved.

**(c) Where a rule is hard-coded instead of read from the chooser.** None in the dice engine: it
decides nothing. Two adjacent observations for their lanes. The fixture and roster are named
`npc_effort` / `npc_efforts` although `settle_efforts` runs for whoever the shipped chooser serves,
a seated player's delegate included (a name, not a rule). Inside a fight, the commitment depth, the
defence mode and whether to counter are drawn from the generator (`modules/combat/combat_systems.py:1127-1162`):
decisions a person would make are made by dice inside the module, not by the chooser (PC lane).

**(d) What would make an NPC characterful here, and legible afterwards.** Distinguishable people need
distinguishable inputs to the same roll: a score that differs (F-DICE-01), a wound that tells
(F-DICE-06), and a belief about an opponent that can be wrong for a reason (F-DICE-14). The engine
needs no per-person rule for any of these. A person's attitude to risk is the chooser's (today the
believed chance multiplies the term linearly: every person is risk-neutral); the dice engine's part is
only that the chance it hands over is his own. Afterwards, the narrative can read the band and nothing
else: the roll's record (pool, obstacle, leverage, net, settled margin) is returned by the provider and
dropped at the fold; `Event` keeps `degree` alone. *She argued with two dice against a hostile bench
and missed by one* is computable at the moment of the roll and unrecoverable a tick later.

**(e) What is missing, as proposals.** `proposals/10_DICE_believed_odds_have_a_prior.md`: the prior
(built here), the `believed_estimate` role for a fight and a field (the interface; PC and MB build it),
and the roll's record on its Event (the interface; CORE builds it). `10_DICE_one_score_two_roles.md` and
`10_DICE_advantage_sources_for_the_arcs.md` supply the inputs that make two people's rolls differ.
