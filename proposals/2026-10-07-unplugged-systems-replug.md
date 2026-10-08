# The unplugged systems: what each needs before a composition row can reach it (IN-06, `33`)

## Status: PROPOSED — the design half of IN-06 (`workplans/valoria_master_workplan_v9_part4.md` §4.5), written in B-C, built in B-S, re-reviewed after IN-08 (B-G, B-H) before B-S opens

> **SCOPE.** This document is reference and a proposal (`CLAUDE.md` §0.05). It resolves nothing at
> runtime: delete it and the game behaves exactly the same. It builds nothing, allocates no ID, writes
> no ledger row and answers no Jordan item. Where it says what a module "needs", the evidence is the
> file and line cited, all of which were opened when this was written (2026-10-07, tree `4558f85`).
> Line numbers drift, so re-derive each one by its symbol before editing. Where it proposes a shape, the
> proposal is graded `[ASSUMPTION]` and B-S decides it at the owner.

- **Lane:** IN (WR, FI). **Position:** IN-06 (`33`): design in B-C, build in B-S.
- **Subjects:** `systems/threadwork/sim/`, `systems/fieldwork/sim/knots.py`,
  `systems/characters/sim/conviction.py`, `systems/overview/sim/ms_track.py` and the struck stubs in
  `systems/threadwork/sim/rendering.py`.
- **Consumers that wait on this design** (all B-S): IN-32 (`tie / knot`, H-182), IN-35 (the Calamity
  coupling, which needs thread operations as a carrier), PC-06 K-3 (`thread_read`'s typed operand) and
  WR-01's reach into `engine/season/`.

---

## 1. What "plugged" means, and the rules every module below must meet

A module is **plugged** when the season loop reaches it through exactly one composition row
(`references/module_contracts.yaml` `composition_roles:`, cooked by `tools/export_composition.py` into
`engine/engine_params/composition.json`, resolved by string through `engine/substrate/composition.py`).
If the row carries `entry:`, `engine/season/manifest/registrar.py` records it in `MODULE_ENTRIES` when
the driver is constructed (`engine/season/loop/driver.py:267-275`). Today the only row is
`mass_battle.resolve_field` (`composition.json:6-12`), and it carries no `entry:`.

The module contract is A-25 (`workplans/valoria_master_workplan_v9_part5.md:383-422`). Every rule below
applies to each module in §3:

1. **No state between calls.** A module "never reads or writes `World`, holds no token, keeps no state
   between calls, imports no module" (`_part5:388-389`). Each module in §3 breaks this in one or more of
   four ways:
   - a module-level store;
   - a `_store(world)` router that writes a duck-typed attribute onto whatever `world` it is handed;
   - an unseeded `random.Random()` fallback;
   - a late import of another module.
2. **The clause.** The store-shed satisfies **AX-4**, *one owner, one writer*
   (`architecture/meta/04_CODE_ARCHITECTURE.md:115`), enforced at **D-3**, *a write outside the matrix:
   one path; an unmarked cell raises; no public setters* (`04:1017`). The knot store also breaches
   **D-10**, *two homes for one relation* (`04:1024`). **D-8**, *a stored aggregate* (`04:1022`), is never
   the clause for a shed. It grades an aggregate stored on a carrier, and none of these stores is that.
3. **Rng is a parameter.** It is seeded and handed in, never constructed inside the module. That is the
   shape IN-03's entry takes (`_part4:193-194`). Each fallback listed in §3 goes away. It does not get
   seeded.
4. **A row lands with its caller.** `module_contracts.yaml:40` says *"a role no caller requires is not
   declared"* (ID-13). No row in §3 lands before the verb, step or projection that calls it.
5. **Plugged code moves.** A-25 says `modules/<name>/` holds *"reachable running code only"* and
   `systems/<name>/` holds *"nothing reachable"* (`_part5:397-399`). IN-05 lands SM-7's test that
   `modules/**` equals the reachable closure in both directions (`_part4:267`, `:425`), and it lands
   before B-S. So a composition target left under `systems/` reds that test. B-S therefore moves each
   plugged closure to `modules/<name>/`, using the same method as `31b`/`31c` (`_part4:233-238`,
   `:279-283`): an import walk from the targets, a directory-prefix MOVE row, and the path readers
   re-derived. **IN-06's EDITS field names the composition rows and the store-shed but not this move**
   (`_part4:381`).
6. **One identity per module, its directory name** (`_part5:410`; precedent: the `combat` row,
   `module_contracts.yaml:816`). Three of the contract rows carry other names: `fieldwork_knots`
   (`:260`), `piety_track` (`:159`, whose `sim_module` is `conviction.py`) and `peninsular_strain`
   (`:479`, whose `sim_module` is `systems/overview/sim/`). Composition role names here use the
   directory: `fieldwork.*`, `characters.*`, `threadwork.*`, `overview.*`. B-S decides whether the
   contract rows are re-keyed when it plugs them. Consumers key the `modules:` list by name
   (`tools/export_composition.py:164-171`), so a re-key is a sweep, not a rename. The `[OPEN — Jordan]`
   name-collision note on `piety_track` (`module_contracts.yaml:182`) is untouched by this document.
7. **The `wiring.build` fact moves** from `unwired`/`deferred`/`stub` to `gated` or `live`
   (`module_contracts.yaml:940-947`) in the commit that plugs the row.

---

## 2. The modules at a glance

| module (roster `kind:`, `rosters.yaml:1883-1890`) | store to shed | clause | carrier it needs | composition row `[ASSUMPTION]` | plugs at B-S? |
|---|---|---|---|---|---|
| **knots**: `fieldwork` (minigame) | `knots.py:155` `_knots`, `:156` `_knot_id_counter`, plus `:159-164`, `:237-239`, `:218-221` | AX-4 at D-3, **and D-10** | the `knot` Tenure, two directed edges (`04:196`); the ED-912 gauge's home is UNLOCATED (H-182); a degree from the fieldwork container, which is SM-3's second role | `fieldwork.form_knot`, `entry: verb_call`, `verb: "tie / knot"` | yes, with IN-32 |
| **conviction**: `characters` (management space) | `conviction.py:82` `_conviction_state`, plus `:85-90` | AX-4 at D-3 | `Person.scar` (`carriers.py:602`) and `Person.pursuits` (`:567`), **as IN-08 leaves them: to be confirmed at the B-G/B-H re-review** | `characters.conviction_scar` (the apply arithmetic) and `characters.conviction_threshold` (`entry: query`) | only if a caller lands (§3.2) |
| **threadwork**: `threadwork` (loop-resident) | `coherence.py:140` `_practitioner_state`, plus `:143-148`; the rng fallbacks; `operations.py:250`'s direct write | AX-4 at D-3 | `(Person, coherence)`: a matrix row with no field and no producer (H-47, H-62); Thread Sensitivity (H-85) | `threadwork.<operation>` `verb_call`, one per thread-operation verb; `threadwork.coherence_band`, `entry: query` | yes, with IN-35 / PC-06 K-3 / WR-01 |
| **ms_track**: `overview` (loop-resident) | no store; it writes `world.clocks['MS']` (`ms_track.py:70`, `:91`) | AX-4 at D-3, and the three-clock bound | **none as written.** The season `World` has no `clocks`, and a clock that decays with time would be a fourth licensed clock | none, unless IN-35's coupling rule calls its arithmetic as a `step_call` | IN-35 decides |
| **rendering stubs** (A-20) | none: `rendering.py` has no entry point | n/a | none: both stubs STRUCK at position 27 | none | no |

---

## 3. Each module

### 3.1 knots: `systems/fieldwork/sim/knots.py`

(The IN-06 entry writes `knots.py:155-156`. The full path is `systems/fieldwork/sim/knots.py`.)

**Store to shed.**
- `_knots: dict[str, Knot]` at `:155` and `_knot_id_counter = [0]` at `:156`.
- The router `_store(world)` at `:159-164`, which returns `world.knots` if the attribute exists and the
  module dict otherwise. The file's own `[ASSUMPTION]` says why it is there: *"World has no .knots
  field"* (`:27-28`).
- `world.knot_id_counter` at `:237-239`.
- The unseeded fallback `random.Random()` at `:218-221`.
- Two late imports of other modules, each wrapped in `except (ImportError, AttributeError): pass`:
  - `systems.characters.sim.conviction.apply_conviction_scar` at `:349`, reached on a Close-knot break
    (`:345-363`);
  - `systems.threadwork.sim.coherence.apply_coherence_delta` at `:374`, reached on a rupture
    (`:371-378`).

  A-25 forbids both imports. After the shed, the entry returns the consequences it already builds as a
  dict (`:328-337`), and the **host adapter** writes the scar and the coherence change through the gate
  under its own token. Composing entries is the host's job, never a module's.

**Clause.** AX-4 at D-3. **D-10 as well:** the season already keeps the knot relation as a `knot`
Tenure, read by `engine/season/epistemic.py:441`, so `_knots` is a second home for one relation.
Also observed, and binding on the shape: the `Knot` record is **one symmetric record**
(`actor_a`, `actor_b`, `:111-121`). `04` requires `tie`/`knot` to be two directed edges, one owned by
each party, with *"strain is a Query"* (`04:196`, §A.3 row 9; `:393`; D-12 at `04:1027`). The shed
therefore splits the record into edges. It does not port the record.

**Carrier.**
- **The edge** is the `knot` Tenure. `verb_table.yaml:1124-1134`'s `tie / knot` row opens it, writes
  `Tenure.since` and emits `bond.formed`. It stays declined (`effect_decline_note`) until IN-32 builds
  `_eff_tie` and the partner operand.
- **The gauge** (ED-912's −5..+5 bond strain, `:61-80`) is UNLOCATED. H-182
  (`engine/season/hole_register.yaml:4079`) records:
  - the only source mapping it to `Tenure.degree` is one clause of a retired plan;
  - `Tenure.degree` is `Optional[str]` (`engine/season/state/carriers.py:88`);
  - `04` §A.3 row 9 *"makes strain a Query stored nowhere, which cuts against storing the gauge on
    either edge"*;
  - *"Whoever builds `tie / knot` decides the carrier."*

  That is IN-32, at B-S. Two candidates for it to weigh, neither decided here:
  - (i) the gauge stored as the edge's `degree`, a string field that would hold an integer;
  - (ii) the gauge as a Query over the edge's event history (the strain events since `since`, clamped
    in order), which is what `04:196` says.

  `(Tenure, degree)` is an ACTS row written at RES (`engine/season/write_matrix.yaml:337-344`), with no
  producer today (H-162).
- **The degree.** Formation grades a roll into a tier: Overwhelming gives Close, Success gives Distant,
  anything else gives no knot (`:223-234`). An uncontested act carries no degree in the season
  (`write_matrix.yaml:344`, citing `loop/resolve.py::_fold`). So the tier needs a graded call through a
  seam. SM-3 already places that: *fieldwork is a container that is not a `contest()` and needs a second
  role in `_ROLE_ROSTERS`* (`_part4:422`). `_ROLE_ROSTERS` is at
  `engine/season/manifest/registry.py:27` (SM-3's row cites `:25`), and today it holds `contest` only.
  FI-02 owns that role.
- **Input-record fields with no season source.** The prerequisites and the pool read `bonds`,
  `disposition_with_<id>`, `ts`, `spirit` and `history_relationships` (`:185-216`).
  - `ts` is Thread Sensitivity, H-85's absent carrier.
  - `bonds` and `disposition` match no field in `carriers.py` and no row in `write_matrix.yaml` (by grep).
  - The break consequences `composure_damage` and `disposition_set_to` (`:341-343`, `:370`) have no
    season carrier either.

  **Unverified:** whether `decision/options.py`'s `regard` is the season reading of Disposition. Not
  opened here.
- **The formula is not this file's to supply.** H-182 records that *"the retired code's formation pool
  omitted the `+ 3` of the ratified Knot Pool (ED-FI-0005), so it was not that formula's oracle"*.
  `:216` is the pool to correct at the build, not to port.

**Composition row `[ASSUMPTION]`:** `fieldwork.form_knot`, `kind: callable`, `entry: verb_call`,
`verb: "tie / knot"`. It lands with IN-32's adapter and the partner operand, and not before (rule 4).
Strain events (`sustain_knot`, `check_knot_rupture`) need acts that move them. None exists in the verb
table, so those entries stay unrowed at B-S unless IN-32 lands such a verb.

### 3.2 conviction: `systems/characters/sim/conviction.py`

**Store to shed.**
- `_conviction_state` at `:82`.
- The router `_store(world)` at `:85-90`, which writes `world.convictions` when present.
- The per-actor `ConvictionState` (`:118-133`). Of its fields:
  - `scars` is the one quantity the season has a row for.
  - `resonant_active` and `in_crisis` are re-derivable from `scars` by the thresholds at `:63-65`
    (set at `:229-233`), so the shed carries only the counts and reads the flags. That follows from
    AX-4's one store per carrier. It is not D-8.
  - `pending_belief_revisions` has no carrier and no writer left: `Person.beliefs` was deleted
    (`carriers.py:568-570`) and `beliefs.py` with it (`registers/mechanics_index.yaml:344`).
  - `last_scar_season`, the Thread-witnessing season cap (`:210-219`), is readable from the `scar.taken`
    events' seasons. It needs no field.
  - `log` is the event log's job.

**Clause.** AX-4 at D-3.

**Carrier. To be confirmed at the B-G/B-H re-review.**
- `Person.scar` exists (`carriers.py:602`) as a dict keyed **per axis**: *"ONE ROW PER AXIS"*
  (`write_matrix.yaml:204-210`, RES, ACTS, `social: true`, emits `scar.taken`; `carriers.py:582-596`).
  `conviction.py` keys scars **per Conviction name** from `descriptors.CONVICTIONS` (`:59`, folded at
  `:205`). These are two different key sets. Nothing in the tree maps a Conviction to an axis, and
  IN-08's atomic commit re-axes the alignment table from 4 to 7 (`_part5:42`). Until that lands, the
  key set this module must write is not knowable. **The open question for the re-review:** does
  `scar[axis]` carry a Conviction scar, does IN-08 leave a per-Conviction key, or is the mapping a
  roster that IN-08 or B-S authors.
- `Person.pursuits` (`carriers.py:567`; `write_matrix.yaml:186-193`, unproduced, H-62) is named as the
  second carrier by the IN-06 entry (`_part4:393`). The IN-06 entry and `_part3` (`:76`) say IN-08's
  cells create the reading B-S builds on (*"`Person.pursuits` and the scar counts exist as the cells
  commit and the chain leave them"*, `_part4:381`). **Also to be confirmed at the re-review:** what a
  scar does to `pursuits`. Nothing in `conviction.py` reads or writes a pursuit, so this design states
  no edge between them.
- `module_contracts.yaml:193` already says the module is *"reached only via the unwired knot chain."*

**Composition rows `[ASSUMPTION]`.**
- **The apply arithmetic.** `before + max(0, magnitude + scaling)` with the season cap (`:207-227`). It
  becomes a pure entry: counts in, counts out. The host adapter whose act causes the scar writes
  `(Person, scar)`.
- **The threshold read** (`check_conviction_threshold`, `:244-264`). Its natural kind is
  `entry: query`. Its consumer is the Conviction CRISIS that `carriers.py:599-601` names. That consumer
  is unbuilt, so this row has no caller.

A-25's closed entry set (`verb_call`, `step_call`, `query`) has no kind for "pure arithmetic that more
than one verb's adapter calls". The registrar refuses one target under two roles and two `verb_call`
rows for one verb (`registrar.py:97-108`). B-S decides between two options:
- a `verb_call` row bound to the first verb that scars;
- keeping the arithmetic host-side until a second caller exists.

**What plugs at B-S.** Only what a landed caller requires. The one scar source in the tree is a
Close-knot break from positive strain (`knots.py:345-363`), and it needs strain-moving acts that no
verb provides (§3.1). If IN-32 lands none, conviction stays unplugged at B-S and says so in the commit.

**Also open at B-S:** `conviction.py:41` imports `engine.substrate.descriptors` for the roster. IN-03's
module shape imports *"the dice engine and the record types, nothing else"* (`_part4:193-195`). Either
the roster arrives in the input record, or the leaf import is admitted at the owner.

### 3.3 threadwork: `systems/threadwork/sim/`

**Stores and breaches**, file by file:

| file | store / router | rng fallback | cross-file write |
|---|---|---|---|
| `coherence.py` | `_practitioner_state` `:140`; router `:143-148` (`world.practitioners`) | — | — |
| `operations.py` | — | `:228-231` | `apply_coherence_delta` at `:250` (imported `:44`) |
| `opposing.py` | — | `:137-140` | imports `operations`, `coherence` (`:37-41`) |
| `collective.py` | — | `:152-155` | `apply_coherence_delta`, late import at `:166` |
| `co_movement.py` | `_deck_state` `:73`; router `:76-81` (`world.comovement_deck`); global `random.shuffle` `:88-90` | `:110-112` | — |
| `threadcut.py` | `_threadcut_registry` `:60`; router `:63-68` (`world.threadcut_beings`) | — | — |

Imports between files inside one module's directory are not A-25's *"imports no module"*. The coherence
writes are the problem: `operations.py:250` writes the practitioner store directly. After the shed, each
operation returns its coherence cost (the module's callers already compute a non-positive delta,
`coherence.py:295-302`), and the host writes the carrier.

**Clause.** AX-4 at D-3.

**Carrier.**
- **`(Person, coherence)`.** The matrix row exists (`write_matrix.yaml:178-185`): RES, ACTS,
  `social: false`. The gate refuses any driver but the seam (`engine/season/state/world.py:957`).
  `Person` declares **no** `coherence` field (`carriers.py:556-614`), and the row's `unproduced:` cell
  cites H-47 and H-62. H-47's own text (`hole_register.yaml:534-545`) still reads *"a 54 fold-in with no
  Part D row"*, grade `absent`, owner unassigned, though the matrix row now cites it. What is actually
  absent is the field and a producer. The v9 plan assigns H-47 to IN-06
  (`workplans/valoria_master_workplan_v9.md:354`).

  The value has two quantities, `resting_point` and `elastic_displacement` (`coherence.py:21-30`). Each
  has its own remedy, and they are stored apart so that recovery *"never assigns"* the resting point
  (`:28-30`, `:359-360`). **So the field must keep both quantities apart.** B-S decides between one
  structured field and two matrix rows.

  `failure_observed` (`:411-416`) is a first-observation latch. In the season the crossing is an Event
  (`coherence.changed`), so the latch is not stored.
- **Where the write comes from.** Because the gate admits only the seam, a thread operation that costs
  Coherence is a **seam-dispatched verb**, a CALL verb in A-25's sense (*"each declared by `contests:`
  and a prize row"*, `_part5:404-405`). No thread-operation verb exists: the verb table's
  thread-adjacent rows are `restore` (`verb_table.yaml:779`, uncontested material) and `thread_read`
  (`:1095`, writes nothing). IN-35 lands *"Mending as persons' acts (the `restore` arm)"*
  (`_part5:265-267`). B-S decides which seam role a thread operation rides: `contest`, or a second
  `_ROLE_ROSTERS` row on SM-3's precedent.
- **Recovery is not a step.** `recover()` returns stretch per season of rest (`coherence.py:338-370`).
  If it ran as a loop step, the world would write coherence on its own. `write_matrix.yaml:183` already
  refused that as *"a FOURTH LICENSED CLOCK against §25.1 ... 'the three licensed clocks are exhaustive
  -- matter, bodies, and the confidence of a memory'"*. Recovery therefore rides an act at RES, through
  the seam, like the stress does. **`[ASSUMPTION]`:** elapsed seasons are an input of that act, read off
  the person's last `coherence.changed` event.
- **Thread Sensitivity (H-85).** PC-06 K-3's `thread_read` and the knot prerequisite (§3.1) both read
  it, and it has no carrier, stem or per-person value (`hole_register.yaml:1062`). R05-THREAD declined to
  type it there and *"waits on threadwork"*. This design names it as a carrier B-S must supply before K-3
  can type `thread_read`'s operand. It does not supply it.
- **R-14's resilience term** is WR-01's in-module swept fixture (`_part7:164`). Its reach into
  `engine/season/` is this carrier's input field, at the control `0`.

**Composition rows `[ASSUMPTION]`.**
- `threadwork.<operation>`: `entry: verb_call`, one per thread-operation verb that B-S lands, each
  `verb:` naming that row. Refusal (b) at `registrar.py:92-96` forbids the row before its verb.
- `threadwork.coherence_band`: `entry: query` over the projected coherence. It lands only with a
  consumer, such as IN-35's band read.

**The plugged closure.** Re-derived at B-S by the import walk from these targets. On today's imports it
is expected to be `operations.py`, `coherence.py`, and `opposing.py`/`collective.py` if their verbs land.

**Expected to stay in `systems/threadwork/sim/`, unplugged:**
- `co_movement.py`. Its cards' only computed output, `ms_delta`, is reported and written nowhere
  (`:15-21`). Its deck is persistent world state (`:73`, reshuffled when exhausted, `:115-119`) with no
  carrier. Plugging it is a design call about the deck, not a shed.
- `threadcut.py`. Its per-being flag and `rendering_strain` (`:71-76`) have no carrier.

A file that stays keeps its store. Rule 1 binds reachable code.

**A-24's "threadwork re-plugging into `ms_track`/`knots`"** (`_part5:380`). This is never a module-to-
module call. Position 27 struck both writes and left the values reported: `opposing.py:110-115` (each
side's `ms_delta` and `knot_ob_penalty`) and `co_movement.py:15-21`.
- **Into knots:** the host adapter carries a reported value from one entry's output record into another
  entry's input, once IN-32 has located the gauge (§3.1).
- **Into ms_track:** no target exists (§3.4). `ms_delta` stays reported unless IN-35's coupling rule
  takes it as an act's consequence.

### 3.4 ms_track: `systems/overview/sim/ms_track.py`

**Store to shed.** None at module level. It reads `world.clocks.get('MS', MS_START)` (`:68`, `:89`) and
writes `world.clocks['MS']` (`:70`, `:91`) on whatever `world` it is handed. Its own header says *"no
caller passes a season `World` (which carries no `clocks`). `33` decides the carrier"* (`:27-29`).
`engine/season/state/world.py` has no `clocks` field: grep finds only docstring prose at `:813` and
`:825`.

**Clause.** AX-4 at D-3 for the write path. The binding constraint is the three-clock bound:
- `engine/season/loop/census.py:37`: *"NO CLOCK GENERATES ANYTHING"*;
- `write_matrix.yaml:183`: the three licensed clocks are exhaustive.

A world-track that decays by −1 a year with nobody acting (`:60-71`, PP-255) is a fourth clock.

**Carrier.** **None as written.** MS does not return as a world clock in this design. IN-35 owns the one
route: the Calamity *"re-expressed as a coupling rule"* in the existing MATTER wear loop over lattice
sites, *"the effect per territory as a Query over band floors"*, with yearly rates converted to per-season
rates (SEAM-CLOCK) (`_part5:261-269`). The place-side carrier is `(Site, condition)`, worn by the MATTER
clock, as `rendering.py:19-25` reads it.

**Composition row.** None from this design. IN-35 decides whether any of `ms_track`'s arithmetic
survives: the clamp to `[0, 100]` (`:55-57`) and the rate (`:45`, `:49`).
- If it does, it is a `step_call` called by MATTER, named `overview.<rule>`, with its rate as an input
  (the season rate is IN-35's). It lands with the coupling rule.
- If IN-35 writes the rule in `loop/matter.py` itself, `ms_track.py` stays unplugged in
  `systems/overview/`, and the commit says so.

### 3.5 rendering stubs: `systems/threadwork/sim/rendering.py` (A-20)

Nothing to plug. A-20's answer allows *"a retained or season-native carrier, or struck"*
(`_part5:376`), and both stubs were **struck** at position 27:
- `apply_rs_strain`: no carrier at either reading (`rendering.py:10-31`);
- `check_calamity_threshold`: no carrier (`:33-37`).

The file holds no entry point (`:2`). It is kept only because `registers/mechanics_index.yaml`'s
`rendering_stability` entry names it as `sim_module` (`rendering.py:39-40`). The reality-strain it once
stood for needs a place-side carrier (`:19-25`). If the season gains one, it is IN-35's coupling rule,
not a revived stub. No composition row, no shed.

---

## 4. The deletion refusal: what makes "delete the row → refuse" true in a fresh process

IN-06's falsifier requires that deleting a plugged row **refuses at driver construction in a fresh
subprocess** (`_part4:382`, `:395`). Today it would not:
- The registrar's "no row declares" refusal fires only when `MODULE_ENTRIES` already holds the role in a
  live process (`registrar.py:114-120`).
- In a fresh process a deleted row leaves nothing to refuse on, because *"no data at `30` declares that
  a row must exist"* (`tests/valoria/test_module_registrar.py:20-24`; `_part4:214-218`).

IN-03 (`31a`, B-L, before B-S) places the declaration. Its candidate is *"the prize row ↔ composition row
agreement ... checked at construction"* (`_part4:216-217`). B-S reads what `31a` landed and applies it:

- **`verb_call` rows on a CALL verb with a prize row** (knot formation through SM-3's role, a seam-
  dispatched thread operation) are covered by `31a`'s agreement as it stands. Deleting the row leaves a
  prize row naming a module with no entry, and construction refuses naming it.
- **`query` and `step_call` rows** (`threadwork.coherence_band`, `characters.conviction_threshold`, an
  `overview` step) have no prize row, so `31a`'s agreement does not reach them. **`[ASSUMPTION]`
  candidate:** the host consumer declares the role it calls, and the registrar refuses a demanded role
  that no row backs. The engine already names a ROLE and the registry names the MODULE
  (`engine/substrate/composition.py:10-14`), so this records demand, not a second owner of "which
  module". A-25's two owners (`_part5:409-410`) stay two. B-S reconciles this candidate with `31a`'s
  actual shape before adding anything.

---

## 5. Falsifiers at build (B-S)

1. **Deletion refuses, fresh process.** For each plugged row, use `test_module_registrar.py`'s
   subprocess harness (`_HEAD`, `:46-60`): drop the row, construct `SeasonDriver(World(0))`, and assert
   the exception names the role.
2. **One seed, twice, one process, equal hashes.** Build the populated realm at one seed, run it, take
   `World.content_hash()` (`engine/season/state/world.py:1274`). Run it again in the **same** process
   and compare. Three things make the run worth doing:
   - **It must reach the entry.** Assert the plugged path executed at least once, for example
     `python -m engine.season.harness.aperture 1 0` showing `tie / knot` executed > 0 (H-182's trigger,
     `hole_register.yaml:4053-4056`). Equal hashes over a run that never called the module observe
     nothing (`CLAUDE.md` §0.1 pts 2-3).
   - **Its control.** Re-plant one shed store, for example a module-level id counter like
     `knots.py:156`, or an unseeded `random.Random()` fallback. The two hashes must then **differ**.
     That shows the assertion can see the failure it excludes.
   - **The surfaces it guards.** Each store and fallback listed in §3 for the plugged closure.
3. **The export round-trips.** `python tools/export_composition.py --check` passes with every target
   resolved, and the module's covering tests (`tests/valoria/test_coherence_elastic_plastic.py` and
   `engine/tests/test_knots_ed912.py`, as moved) stay green, or are re-pointed in the same commit.

---

## 6. Deliberately left to B-S

- The knot gauge's home: candidate (i) or (ii) in §3.1, or another. H-182 assigns it to whoever builds
  `tie / knot`, which is IN-32.
- The partner operand of `tie / knot`, and whether strain-moving verbs exist at all.
- The seam role a thread operation rides (`contest`, or a second `_ROLE_ROSTERS` row), and the
  thread-operation verb rows themselves (IN-35, PC-06 K-3).
- The shape of the `coherence` field (one structured field, or two matrix rows), and the
  Thread Sensitivity carrier (H-85).
- Whether `ms_track`'s arithmetic survives inside IN-35's coupling rule.
- The entry kind for conviction's apply arithmetic, and whether it plugs at all.
- The `query`/`step_call` deletion declaration (§4), once `31a` has landed its own.
- Re-keying `fieldwork_knots`, `piety_track` and `peninsular_strain` to directory identities.
- The import walk that fixes each plugged closure, and the MOVE to `modules/<name>/`.
- Every formula. This design ports no number. ED-FI-0005's Knot Pool, R-14's arithmetic and the season
  rates are their owners'.

## 7. Re-review after IN-08 (B-G, B-H): what to re-read

- `Person.scar`'s key set after the 4 → 7 re-axing, and whether a Conviction maps onto it (§3.2).
- What `Person.pursuits` holds after the cells commit and H7 → 6f, and whether any scar consequence
  touches it (§3.2).
- Whether `tie / knot` is celled on the seven axes or joins the `uncelled:` set (IN-08 → IN-32,
  `_part5:43`), since that decides the verb row `fieldwork.form_knot` binds to.
