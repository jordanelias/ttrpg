# The unplugged systems: what each needs before a composition row can reach it (IN-06, `33`)

## Status: PROPOSED — the design half of IN-06 (`workplans/valoria_master_workplan_v9_part4.md` §4.5), written at B-C and RE-REVIEWED AT THE B-S OPENER (2026-10-23, tree `2decf4a0`), after IN-08's cells (B-G, PR #465) and chain (B-H, PR #466) · every §6 item is resolved on the `CLAUDE.md` §0 ladder, so this is ratified on merge (ED-1094); nothing is held back

> **SCOPE.** This document is reference and a proposal (`CLAUDE.md` §0.05). It resolves nothing at
> runtime: delete it and the game behaves exactly the same. It builds nothing, allocates no ID, writes
> no ledger row and answers no Jordan item. Each carrier below is cited by its SYMBOL, and was opened
> at `2decf4a0` for this re-review; a line number is given only as a reading aid, because line numbers
> drift. Where an answer rests on judgment it is marked `[ASSUMPTION; medium; Jordan to correct]` with
> its revert. The B-C text was written at `4558f85`; every claim the tree no longer supports has been
> corrected or dropped here, not annotated.

- **Lane:** IN (WR, FI). **Position:** IN-06 (`33`): design at B-C, build at B-S.
- **Subjects:** `systems/threadwork/sim/`, `systems/fieldwork/sim/knots.py`,
  `systems/characters/sim/conviction.py`, `systems/overview/sim/ms_track.py` and the struck stubs in
  `systems/threadwork/sim/rendering.py`.
- **Consumers in B-S:** IN-35 (the Calamity coupling), IN-32 (`tie / knot`, H-182), PC-06 K-3
  (`thread_read`'s typed operand, H-85) and WR-01's reach into `engine/season/`.

**The re-review's finding in one paragraph.** IN-08 made the conviction quantities season-native, and
nothing in the tree yet reads what the other three modules would compute. So **no module plugs at B-S**:
each B-S consumer builds its half host-side or on a carrier this document names (§2), and every module
stays in `systems/`, unplugged, with its store. IN-06's own build therefore adds no composition row,
sheds no store and moves no closure. Its EXIT clause *"a plugged row's deletion refuses"* has no row to
observe at B-S; that is a named residue, not a defect (§5).

---

## 0. The B-S entry gate, reconciled

The four statements disagreed (IN-06's entry: B-R, B-F, B-D3; WR-01 and PC-06 in `_part7`: B-R and B-V;
`_part3` §B.1's row: all four). None says another's member is unneeded; each names a file it shares. The
reconciled gate is their **union**, read **by PR landing**, because the closing SHAs the plan quotes are
pre-squash and are not ancestors of `HEAD` (checked with `git merge-base --is-ancestor`: `541c8d12`,
`53807be4`, `0a690b30`, `0f998f64`, `c13144b9` and IN-03's `e02715f8` each fail).

**B-S opens when all of these have landed:**

| member | why B-S waits on it | landed as |
|---|---|---|
| B-R closed | the verb files (`verb_table.yaml`, `loop/effects_*.py`) | PR #496 `97513712` |
| B-V closed | `rosters.yaml` | PR #498 `b1eabf5d`; remainder PR #499 `2decf4a0` |
| B-F closed | `loop/matter.py` (IN-21, SE-01) and IN-03's registrar shape (`31a`) | PR #470 `3faafd29`; PR #471 `8047c6e0` |
| B-D3 merged | threadwork's in-module halves (R-14) | PR #464 `e337d948` (where `operations.RESILIENCE_GAIN_SWEEP` first appears, `git log -S`) |
| IN-08 merged | the carriers this design names | B-G PR #465 `f8fbc3ab`; B-H PR #466 `f2670889` |
| this design re-reviewed after IN-08 | IN-06's own EXIT | this revision |

**B-Y is not a member.** It runs beside B-S and merges after it, then before B-T (`_part3` §B.0, §C.2).
At `2decf4a0` every member has landed, so the gate is met.

---

## 1. What "plugged" means, and the rules a plugged module meets

A module is **plugged** when the season loop reaches it through exactly one composition row
(`references/module_contracts.yaml` `composition_roles:`, cooked by `tools/export_composition.py` into
`engine/engine_params/composition.json`, resolved by string through `engine/substrate/composition.py`).
Every row now carries `entry:`, and `engine/season/manifest/registrar.py::register_module_entries`
records it in `MODULE_ENTRIES` at driver construction (`loop/driver.py`, the construction block that
also calls `check_contest_prizes` and `check_inquiry_modules`). At `2decf4a0` there are four rows:
`combat.fight`, `fieldwork.find`, `mass_battle.resolve_field` and `social_contest.roll`, and `modules/`
holds exactly `combat`, `fieldwork`, `mass_battle` and `social_contest`.

The module contract is A-25 (`workplans/valoria_master_workplan_v9_part5.md`). A module that plugs meets
all of these; a module that stays unplugged is bound by none of them (rule 1 binds reachable code), so
it keeps its store.

1. **No state between calls.** A module never reads or writes `World`, holds no token, keeps no state
   between calls and imports no other module. The four ways the modules below break it: a module-level
   store; a `_store(world)` router writing a duck-typed attribute onto whatever `world` it is handed; an
   unseeded `random.Random()` fallback; a late import of another module.
2. **The clause** for a shed is **AX-4**, *one owner, one writer*
   (`architecture/meta/04_CODE_ARCHITECTURE.md`, AX-4 row), enforced at **D-3**, *a write outside the
   matrix* (`04` defect table row 3). The knot store also breaches **D-10**, *two homes for one
   relation* (row 10). **D-8**, *a stored aggregate* (row 8), is never the clause for a shed.
3. **Rng is a parameter**, seeded and handed in. Each fallback goes away; it is not seeded.
4. **A row lands with its caller.** `module_contracts.yaml` `composition_roles:` header: *"a role no
   caller requires is not declared"* (ID-13). And no field without a reader (ID-13, as
   `state/carriers.py::Person.born`'s comment states it).
5. **Plugged code moves.** `tests/valoria/test_modules_reachable_closure.py` (SM-7) holds `modules/**`
   equal to the reachable closure in both directions, so a closure moves into `modules/<name>/` only in
   the commit that plugs it, on `31b`/`31c`'s method (import walk, directory-prefix MOVE row, path
   readers re-derived).
6. **One identity per module, its directory name** (A-25; the `combat` row's precedent). Settled for
   every module here (§6 item 8).
7. **The `wiring.build` fact** in `module_contracts.yaml` moves from `unwired`/`deferred` to `gated` or
   `live` only in the commit that plugs the row. No B-S commit moves one (§2).

---

## 2. Per module: the carrier as it stands, and which B-S item plugs what

| module (`rosters.yaml` module roster `kind:`) | the carrier, as it stands at `2decf4a0` | the B-S item, and what it plugs | stays unplugged? |
|---|---|---|---|
| **knots**: `fieldwork` (minigame) | the `tie` and `knot` Tenure kinds, two directed edges owned by their subject (`04` §A.3 row 9); `Tenure.since`; no gauge, no tier, no strain | **IN-32** builds `_eff_tie` host-side (`loop/effects_information.py`): an executed act opens the actor's `tie` to the act's `subject`, read by `decision/options.py::teller_weight`'s `relation` term. No composition row | **yes** — `knots.py` stays in `systems/fieldwork/sim/`, store kept; the `knot` kind stays declined (§3.1) |
| **conviction**: `characters` (management space) | `Person.scar` `{element: count}` and `Person.conviction` `{affiliation: intensity}`, written at RESOLVE by `loop/resolve.py::_scar_witnesses` and `_conviction_crisis`, read by `queries/person_q.py::crisis_weights` and `conviction_after_crisis` | **none**: superseded by IN-08 | **yes** — stays in `systems/characters/sim/` (§3.2) |
| **threadwork**: `threadwork` (loop-resident) | `(Person, coherence)`: a write-matrix row, Seam-only, with no field and no producer; Thread Sensitivity: no carrier (H-85) | **K-3** lands the Thread Sensitivity carrier and types `thread_read` (no module row). **IN-35**'s Mending is `restore`'s arm, host-side. **WR-01**'s reach has nothing to reach at B-S | **yes** — every file stays in `systems/threadwork/sim/` (§3.3) |
| **ms_track**: `overview` (loop-resident) | none: the season `World` has no `clocks`, and a decaying world track would be a fourth clock | **IN-35** writes the coupling rule in `loop/matter.py`'s wear loop, host-side | **yes** — stays in `systems/overview/sim/` (§3.4) |
| **rendering stubs** (A-20) | none: both struck at position 27 | none | the file stays as a record (§3.5) |

**What IN-06's build itself leaves:** no composition row, no store-shed, no closure move, no
`wiring.build` change. The `_part3` §B.1 B-S row lists `module_contracts.yaml`, `composition.json`,
`manifest/registry.py`, `modules/` and the three `systems/` modules in EDITS; under this re-review none
of them is edited by IN-06, and the B-S card's handoff line *"threadwork/knots/conviction plugged"*
reads *none plugged*.

---

## 3. Each module

### 3.1 knots: `systems/fieldwork/sim/knots.py`

**What it holds** (unchanged since B-C; kept because the module stays unplugged and keeps them):
`_knots` and `_knot_id_counter` (module level, `:155-156`); the `_store(world)` router (`:159-164`;
the file's own `[ASSUMPTION]`, *"World has no .knots field"*, `:27-28`); `world.knot_id_counter`
inside `form_knot` (`:236-241`); the unseeded fallback in `form_knot` (`:218-221`); two late imports in
`apply_knot_loss`, of `systems.characters.sim.conviction.apply_conviction_scar` (break, `:349`, scarring
the pursuit `honour`) and `systems.threadwork.sim.coherence.apply_coherence_delta` (rupture, `:375`). The
`Knot` record is one symmetric record (`actor_a`, `actor_b`, `:111`), which `04` §A.3 row 9 overrides:
two directed edges, strain a Query.

**Why it does not plug at B-S.** Every output it computes has no reader in the season, and most of its
inputs have no carrier:
- **The tier** (Close / Distant, from the formation degree, `form_knot` `:226-234`) is read only through
  the strain range (`TIER_RANGE`) and the break and rupture consequences. Strain moves only through
  `sustain_knot` and `check_knot_rupture`, and **no verb in `verb_table.yaml` moves strain** — so a tier
  would be a carrier nobody reads (ID-13).
- **The formation roll's inputs** — `bonds`, `disposition_with_<id>`, `spirit`, `history_relationships`
  (`form_knot` `:185-216`) — match no field in `state/carriers.py` and no row in `write_matrix.yaml`.
  `ts` gets its carrier at K-3 (§3.3), after IN-32.
- **The ratified formula** is ED-FI-0005's Knot Pool, *(Spirit × 2) + History(Relevant) + 3*, with Bonds
  an eligibility gate only (`registers/editorial_ledger_fi_archive.jsonl`). The module's pool at
  `:216` omits the `+ 3` (H-182's record), so it is not that formula's oracle. A pool the season could
  supply today would follow `seam/wrappers/sigma.py::_pool_of`'s precedent (a person's `capability`,
  else the injected `pool_default`), but nothing would read the tier it graded.
- **The break and rupture consequences** (`composure_damage`, `disposition_set_to`, `apply_knot_loss`
  `:328-343`) have no season carrier; the coherence change has none either (§3.3).

**What IN-32 builds instead, host-side** `[ASSUMPTION; medium; Jordan to correct]`. The row
`tie / knot` (`verb_table.yaml`) names two kinds for one opener. H-182 (`hole_register.yaml`) is about
**ties** — *a telling does not knit teller and hearer* — and names the tie's reader:
`decision/options.py::teller_weight`'s `relation` term (today `1 + rank_gain * rank(p, teller)`). So
`_eff_tie` opens a **`tie`** from the actor to the act's `subject`, writing `Tenure.since` and emitting
`bond.formed`, exactly the row's declared writes. The **`knot`** kind stays declined: a knot forms by
ED-FI-0005's roll (ladder step 3, ratified), and opening one with no roll would also feed the live
`knot` reader (`epistemic.py::_ch_witness_key`, the firsthand-via-knot channel) with edges canon says
form only by that roll. *Revert:* `_eff_tie` opens a `knot` too, ungraded, and the epistemic channel
reads it.

**Facts IN-32 builds on:**
- **The partner operand is the act's `subject`** (§6 item 2). No operand is coined.
- **`tie / knot` is celled** on the seven axes and in `affiliation_engagement` (`rosters.yaml`), and
  is not in `alignment.uncelled:`. So every executed tie can scar its observers through
  `_scar_witnesses`: an expected hash mover, to be declared in IN-32's commit.
- **The falsifier, on IN-33's precedent.** IN-33 (H-58's `cite:`) coined two operands at ladder steps 3
  and 5, executed 0 times in `aperture 4 0`, and its 100 refused attempts moved the seed-0 trajectory
  so that `comply`, `oblige` and `confer` stopped executing; it was reverted. IN-32 states, before it
  lands: (1) `python -m engine.season.harness.aperture 1 0` shows `tie / knot` offered > 0 **and**
  executed > 0, and the `relation` term reads an executed tie; (2) the `corpus_run` "WHERE THE <n> GO"
  set is read before and after, and no previously executing verb falls to 0. Either failing, IN-32
  reverts and records the attempt on H-182's `cite:` with its checkpoints, as IN-33 did on H-58.

**The gauge** (§6 item 1) and the contract row `fieldwork` (already re-keyed, §6 item 8) need nothing
at B-S.

### 3.2 conviction: `systems/characters/sim/conviction.py`

**Superseded by IN-08** (ladder step 1). The B-C questions dissolve against the tree:
- **The key set agrees.** `Person.scar` is no longer per axis: it is `{element: count}`, an element
  being a pursuit name (the fifteen of `descriptor_registry.yaml`'s `pursuit_roster`) or, since IN-08
  H11, an affiliation name (`affiliation_roster`); the two rosters refuse a shared name
  (`data/affiliations.py::_load_engagement`). The module's `CONVICTIONS` **is** `descriptors.PURSUITS`
  (`:60`), and `tests/valoria/test_conviction_roster_single_owner.py` asserts the identity. So the
  module keys the pursuit half of the season's own key set, and knows nothing of the affiliation half.
- **The apply arithmetic** has its season owner: `_scar_witnesses` writes one count per observer per
  violated element, at RESOLVE, through the gate (`ED-IN-0261`'s scar model). The module's Truth
  scaling (`CERTAINTY_SCALING`) and its Thread-witnessing season cap (`apply_conviction_scar`) are not
  part of that model.
- **The threshold read** has its season owners: `person_q.crisis_weights` at `SCAR_WEIGHT_SHIFT_AT`
  (2) and `conviction_after_crisis` at `SCAR_CRISIS_AT` (3), the second called by `_conviction_crisis`,
  which is `(Person, conviction)`'s only writer in play.
- **`Person.conviction`** (named here, as IN-06's finding (5) requires) is `{affiliation: intensity}`,
  0-5, filled at world build from the cast's `affiliations:` (`data/cast.py::conviction_of`) and moved
  only by the crisis. The module has no counterpart for it.
- **`Person.pursuits`** is produced now (`determine` at SC-02 `22b`, `argue` at IN-12 step 9:
  `write_matrix.yaml`'s pursuits row). A scar acts on pursuits only through `crisis_weights`' weight
  shift (`scar_weight_shift`, shipped 0). `conviction.py` reads and writes no pursuit, so no edge
  between them is drawn.

**It stays where it is, unplugged.** Nothing in `engine/season/` imports it. Two tests do:
`test_conviction_roster_single_owner.py` (it is that guard's named non-engine witness file and its
identity check) and `engine/tests/test_knots_ed912.py`. `module_contracts.yaml`'s `piety_track` row
keeps `wiring.build: deferred`, and its note *"reached only via the unwired knot chain"* stays true.

### 3.3 threadwork: `systems/threadwork/sim/`

**Stores and breaches as they stand** (kept, because nothing plugs):

| file | store / router | rng fallback | cross-file reach |
|---|---|---|---|
| `coherence.py` | `_practitioner_state` (`:143`); `_store` (`:146-151`, `world.practitioners`) | — | — |
| `operations.py` | — | `_resolve_operation` (`:304-307`) | `charge_working` → `coherence.apply_coherence_delta` (`:277-287`) |
| `opposing.py` | — | `:158-160` | imports `operations` (`:37`) |
| `collective.py` | — | `:178-180` | imports `operations` (`:29`); the B-C late import of `coherence` is gone — its cost now goes through `charge_working` |
| `co_movement.py` | `_deck_state` (`:73`); `_store` (`:76-81`); global `random.shuffle` (`:90`) | `:111-112` | — |
| `threadcut.py` | `_threadcut_registry` (`:60`); `_store` (`:63-68`) | — | — |

**Why nothing plugs at B-S.** Each B-S consumer either builds its half without the module or has no
reader for what the module would return:
- **`(Person, coherence)` has no reader anywhere in `engine/season/`** (a grep for `coherence` across
  its Python finds only `state/world.py`'s Seam-only guard and a shape test), and no B-S act would move
  it: Mending costs 0 Coherence at every degree (ED-871; `operations.MENDING_COHERENCE_COST`), its
  restorative term can never pass the resting point, and no costly working (Weaving, Pulling, Locking,
  Dissolution, Leap) has a verb or a B-S position. `thread_read`'s own Coherence cost is *"not
  expressed here"* and carried on ED-FI-0009 (its `source:` in `verb_table.yaml`). A module that wrote
  the field and also read it back to compute its next value would be the only reader, and H-182 already
  records that a writer reading its own edge is not a reader (`tie`'s `release`). So the field does not
  land at B-S (§6 item 4).
- **The pool** (`_actor_pool`: Spirit × 2 + History + TPS) reads `spirit` and `history`, which have no
  season carrier (K-2 is unratified; Spirit is J-9's, held in `_part5` §J). `_pool_of`'s injected
  default would supply a pool, but only a graded working would need one, and none lands.
- **IN-35** builds Mending as `restore`'s arm, host-side (§6 item 3).
- **WR-01's reach** passes a resilience into a working's cost. At B-S no working with a cost runs in
  the season, and the slot has no carrier to fill it (§6 item 11).

**K-3's carrier: Thread Sensitivity (H-85).** `thread_read` (`verb_table.yaml`) requires *"Thread
Sensitivity >= 30"* and sits outside `resolvable_verbs()` for want of a carrier, a stem and a
per-person value. Named here `[ASSUMPTION; medium; Jordan to correct]`:
- **the carrier** is a per-person integer on `Person`, filled at world build from the cast registry's
  authored `ts:` key (`references/npc_registry.yaml`) by a `data/cast.py` reader, on
  `cast.conviction_of`'s precedent. It is never written in play, on `Person.born`'s precedent (one
  field, set at construction, its one reader named). It is **not** a `Person.capability` key, because
  `capability` *"supplies dice and GATES NOTHING"* (`rosters.yaml: verb_capability`, quoting #353
  §9.2) and this value is a gate;
- **the reader** is `thread_read`'s typed cell: a `scalar_threshold` (`data/requires.py`) `of: actor`
  over a new predicate stem in `REQUIRES_STEMS` — a stem, not an operand, so `requires_operands` stays
  the closed eight (precedent: plan position `19`'s four stems, and `with`). The threshold is a
  `Fixtures` value, not a literal (`work`'s `floor`, H-08). The 30 is `fieldwork_v30.md:297`'s figure,
  so K-3 carries it as that value's source, not as the reason it is correct;
- **the authored values**: 32 of the registry's persons carry `ts:`. Most are `null # [GAP]`, which
  leaves the key absent, so the person cannot attempt (canon: *"Characters below the gate cannot
  attempt the action"*). Four values are at least 30, two of them non-numeric (`75–80`, `~50`). How a
  range or an approximate value reads is K-3's parse rule to state; *proposed:* the lower bound of a
  range, the number in `~N`. Whether any such person is in `build_realm(0)`'s cast decides whether K-3's
  EXIT (`thread_read` executed in computed play) can be met at all, and is K-3's first measurement.

**Expected to stay unplugged after B-S as well** (no B-S consumer touches them): `co_movement.py` (its
only computed output, `ms_delta`, is reported and written nowhere, `:15-21`, and its deck is persistent
world state with no carrier); `threadcut.py` (its per-being flag and `rendering_strain` have no
carrier); `opposing.py` and `collective.py` (no verb).

**A-24's "threadwork re-plugging into `ms_track`/`knots`"** is never a module-to-module call: position
27 struck both writes and left the values reported (`opposing.py`'s `ms_delta` and `knot_ob_penalty`;
`co_movement.py:15-21`). Neither target plugs at B-S (§3.1, §3.4), so nothing carries them.

### 3.4 ms_track: `systems/overview/sim/ms_track.py`

**No store; no carrier.** It reads and writes `world.clocks['MS']` (`apply_ms_baseline_decay` and
`apply_ms_delta`, `:68-70`, `:89-91`) on whatever `world` it is handed; its header says no caller passes
a season `World`, *"which carries no `clocks`"* (`:27-29`), and `state/world.py` declares none. The
binding constraint is the three-clock bound: `loop/census.py`'s S29 comment, *"NO CLOCK GENERATES
ANYTHING"*, and the `(Person, coherence)` row's `by:` in `write_matrix.yaml`, *"the three licensed
clocks are exhaustive -- matter, bodies, and the confidence of a memory"*. A world track that decays
by −1 a year with nobody acting (PP-255) is a fourth clock.

**IN-35 does not use it** (§6 item 5). The coupling rule rides the existing MATTER wear loop over
lattice sites, with the effect per territory a Query over band floors, and `loop/matter.py::_crossings`
already emits the band crossings. Its quantity is `(Site, condition)` on `condition_scale`; its rate is
IN-35's per-season coupling weight (weight 0 reproduces today). Neither `ms_track`'s `[0, 100]` clamp
nor its yearly rate has a place in that rule. `ms_track.py` stays unplugged in `systems/overview/`,
and IN-35's commit says so.

### 3.5 rendering stubs: `systems/threadwork/sim/rendering.py` (A-20)

Nothing to plug. Both stubs were **struck** at position 27 (`apply_rs_strain`: no carrier at either
reading; `check_calamity_threshold`: no carrier), and the file holds no entry point. It is kept only
because `registers/mechanics_index.yaml`'s `rendering_stability` entry names it as `sim_module`. A
place-side reality-strain carrier, if the season ever gains one, is IN-35's coupling rule, not a
revived stub.

---

## 4. The deletion refusal: the three accounts, reconciled

IN-06's falsifier wants a plugged row's deletion to refuse at driver construction **in a fresh
subprocess**. `MODULE_ENTRIES` cannot give that: `register_module_entries` refuses a missing row only
for a role it already holds in a live process. The three design accounts, read against the tree:

1. **IN-03's, as built** (`31a`, landed in PR #471; generalized at FI-02/FI-03). A role's roster row
   names its `module_entry:` — the contest role's prize rows (`rosters.yaml: contest_subsystems`) and
   the inquiry role's rows (`inquiry_modules`). `manifest/registry.py::_check_module_entry`, called
   from `check_contest_prizes` (`verb_call` rows) and `check_inquiry_modules` (`step_call` rows), reads
   the composition rows through `engine.substrate.composition` (data loaded at import, not
   `MODULE_ENTRIES`), so a deleted row refuses at construction in a fresh process, naming it. Its
   docstring says so: *"THIS IS THE DECLARATION THAT A ROW MUST EXIST."* This covers **every
   role-backed row, of either entry kind** — `fieldwork.find` is a `step_call` and is covered.
2. **IN-06's B-C `[ASSUMPTION]`** (the host consumer declares the role it calls; the registrar refuses a
   declared role no row backs) and
3. **IN-07's `require_entries(needs)`** (`proposals/2026-10-07-settlements-computation-modules.md`
   §2.3: `loop/matter.py::STEP_CALLS` and `queries/world_q.py::QUERY_ENTRIES`, checked right after
   `register_module_entries`) are **the same mechanism**, for the rows no role roster names: a `query`
   row, a `step_call` a loop step calls directly, and a `verb_call` an effect calls with no prize row.

**Reconciled:** a row a role roster names is held by IN-03's built check, unchanged. A role-less row is
held by IN-07's `require_entries`, built once at B-T with its first row (E1). IN-06's candidate is
withdrawn in its favour, so there is one mechanism, not two. **B-S needs nothing from either**, because
it plugs no row; if a revert arm in §6 plugs one, it takes a role of its own (§6 item 3), and IN-03's
check covers it with no new mechanism.

---

## 5. Falsifiers at build (B-S), and the residues

- **IN-06's EXIT** (*a plugged row's deletion refuses in a fresh subprocess; one seed run twice in one
  process gives equal hashes*) has **no row to observe at B-S** — a named residue for B-S's handoff
  line. The second half's instrument already exists for any row that does plug:
  `engine/season/tests/test_build_realm_determinism.py::test_build_realm_seed_0_is_deterministic_across_n_seasons`
  compares a fresh `build_realm(0)` against its module-scoped fixture's, **in one pytest process** (the
  B-C question *"whether the two runs share a process"*: they do). A plugged row adds two things it
  lacks: an assertion that the plugged path executed at least once, and a control (re-plant one shed
  store or fallback; the hashes must then differ).
- **Each consumer keeps its own falsifier:** IN-32 as §3.1 states it; IN-35 its #457 control (unmanaged
  arm falls outward, managed arm stabilizes, weight 0 reproduces today); K-3 `thread_read` leaving the
  no-predicate set.
- **Residues the B-S close must name, because this re-review makes them unobservable at B-S:** K-3's
  second falsifier clause (*"threadwork's Coherence reads and writes the person, not a module store"*):
  no Coherence is read or written in the season at B-S, and no module store is reachable; WR-01's EXIT
  and its season-run falsifier: no working with a cost runs in the season.

---

## 6. Resolved at the B-S opener (was "Deliberately left to B-S")

Each item: the answer, then the ladder step (`CLAUDE.md` §0) that gives it.

1. **The knot gauge's home** → candidate (ii), a Query over the edge's strain events since `since`,
   clamped in order. **Step 3:** ratified Layer 1 says *"two directed edges; strain is a Query"*
   (`04` §A.3 row 9) and *"a Query is a function, never a stored aggregate"* (D-8); candidate (i), the
   gauge stored as `Tenure.degree`, contradicts both. **Not built at B-S** (step 2): no verb moves
   strain, so the Query would read nothing.
2. **The partner operand of `tie / knot`, and strain-moving verbs** → the partner is the act's
   `subject`, a person. **Step 4:** IN-09 typed `comply` with no new name because *"the act's `subject`
   IS the held writ"* (`rosters.yaml: requires_operands` note), and a computed act's payload already
   carries `subject`. Coining an operand is the route IN-33 took and reverted. **Strain-moving verbs:**
   none exists and no B-S position owns one (step 2), so `sustain_knot` and `check_knot_rupture` stay
   unrowed.
3. **The seam role a thread working rides, and the thread-operation verb rows** → **no thread-operation
   verb row lands at B-S.** IN-35's Mending is `restore`'s arm, host-side and ungraded (step 3: #457's
   *"Mending as persons' acts (the `restore` arm)"*, carried verbatim in IN-35's entry; step 5: Mending
   costs 0, so a graded Mending through the module would grade a roll whose outcome only IN-35's
   coupling weight reads, at the cost of a new role and a plugged closure)
   `[ASSUMPTION; medium; Jordan to correct]`. *Revert:* Mending graded through the threadwork module.
   **The role, whenever a working does plug:** a role of its own in `_ROLE_ROSTERS`, with its roster
   row naming `module_entry:` and its own construction check. **Step 4:** SM-3 (Jordan, 2026-09-05:
   *"investigation is not a contest seam. it is its own thing"*) and `rosters.yaml`'s rule that
   investigation *"must not be made a contest to become gradeable"*. A working is one practitioner
   against an Ob, not two parties over a prize.
4. **The shape of the `coherence` field** → when it lands, **one structured field** holding
   `resting_point` and `elastic_displacement` apart (they have separate remedies, `coherence.py`'s
   `recover` and `mend_resting_point`), under the existing `(Person, coherence)` row. **Steps 4 and 5:**
   `Person.scar` and `Person.conviction` are each one field under one row, and the Seam-only guard in
   `state/world.py::World.write` is keyed on that one pair; two rows would need it twice. The band and
   the failure latch are derived (a Query, and the crossing an Event), never stored. Recovery rides the
   act that next writes the field, with the elapsed seasons read off a tick stored in the same record:
   the scar and conviction writes emit nothing (their `_scar_witnesses` / `_conviction_crisis`
   precedent), so there is no `coherence.changed` Event to read it from
   `[ASSUMPTION; medium; Jordan to correct]`. **When:** not at B-S (§3.3) — **step 5, ID-13**: no reader
   exists and no B-S act moves it. *Revert:* K-3 expresses `thread_read`'s Coherence cost as a swept
   `Fixtures` magnitude shipping 0 (H-94's precedent), through item 3's role, landing this field and
   plugging `modules/threadwork/` (`operations.py` and `coherence.py`, the rest staying in `systems/`
   with their imports re-pointed). **The Thread Sensitivity carrier:** §3.3, at K-3 (step 5)
   `[ASSUMPTION; medium; Jordan to correct]`.
5. **Whether `ms_track`'s arithmetic survives inside IN-35's coupling rule** → no. **Step 3:** #457's
   rule keys on site band floors over `(Site, condition)`, at a per-season coupling weight; the
   three-clock bound forbids a world track that moves on its own (§3.4).
6. **The entry kind for conviction's arithmetic, and whether it plugs** → it does not plug, so it has no
   entry kind. **Step 1:** superseded by IN-08 H3, H11 and H13 (§3.2).
7. **The `query`/`step_call` deletion declaration** → IN-03's built check for role-backed rows, IN-07's
   `require_entries` for role-less ones. **Step 4** (§4).
8. **Re-keying the contract rows** → `fieldwork_knots`: **step 1**, already re-keyed to `fieldwork` at
   FI-02/FI-03 (the `inquiry_modules` row names it). `piety_track` and `peninsular_strain`: **step 2**,
   their modules do not plug, so no consumer keys them. `threadwork` already carries its directory
   name. The `[OPEN — Jordan]` name-collision note on `piety_track` is untouched.
9. **The import walk and the MOVE to `modules/<name>/`** → none at B-S. **Step 2:** nothing plugs, and
   SM-7 forbids a move without a plug.
10. **Every formula** → unchanged: this design ports no number. ED-FI-0005's Knot Pool, R-14's
    arithmetic and the season rates belong to their owners.
11. **WR-01's two unruled things** (`_part7` WR-01: *"must be settled with IN-06's design"*) → **the
    gain** is a `Fixtures` field read by the host and passed on the input record, the sweep `(0, 1, 3)`
    shipping 0 (**step 4**, H-94's precedent for an unruled magnitude; a module global patched by tests
    is a hidden input under A-25). **The slot** keeps the module's name, `resilience`, as an
    input-record field; **what fills it** waits on J-9 / K-2, held with Jordan, so until then the host
    passes 0 (**step 2** for B-S: no working with a cost runs, so the reach has nothing to carry)
    `[ASSUMPTION; medium; Jordan to correct]`.
12. **The B-C items left open** → `decision/options.py`'s `regard` as the season's Disposition: **step
    2**, moot while knot formation stays unbuilt. IN-08's *"is `tie / knot` celled or `uncelled:`"*:
    celled (§3.1). The entry gate: §0.
