# The settlements module — what each loop-resident computation computes, and the levy-to-field feed

## Status: PROPOSED — the design IN-07 (`36`, = SE-02) owes before its build (B-T). Nothing here is built. What each extraction COMPUTES is Jordan's to review (the entry's gate, `workplans/valoria_master_workplan_v9_part4.md:398`); every judgment call is marked [ASSUMPTION]. HELD BACK from ratification-on-merge (ED-1094): §5's A13-A15 (the levy feed) are Jordan's, and the PR body lists them as held back.

> **Scope.** Reference, not mechanism (`CLAUDE.md` §0.05): if this file were deleted the game would behave
> identically. It allocates no ID, writes no ledger row and schedules nothing; the plan (`_part3` §B, row B-T)
> owns order. The module contract is `_part5` §A `### A-25` (`:383-422`) and is not restated here. Every
> `file:line` was opened at `4558f85`. Paths are relative to `engine/season/` unless they start with a top-level
> directory.

---

## 1. What IN-07 asks, read against the code

The entry (`_part4:398-412`): extract the rules living in the gate (`state/gate.py`), `world_q` and the MATTER
step into `step_call` and `query` entries with a typed input and output; the verb adapters and every MATTER
write stay host; design the feed from `levy` to a field's troops. The falsifier for each extraction has four
parts: both hashes unchanged; the old host body gone (`rg`); deleting the module's composition row refuses at
driver construction; one seed run twice in one process gives one hash.

**Three facts about the tree change how the build can meet that falsifier:**

1. **No production row carries `entry:`.** `composition_roles:` holds one row, `mass_battle.resolve_field`,
   with no entry (`references/module_contracts.yaml:52-54`; `engine/engine_params/composition.json` `"entry": null`).
   The registrar registers only rows that carry one (`manifest/registrar.py:86-90`). The settlements rows are the
   first `step_call` and `query` rows.
2. **Deleting a row does not refuse anything today, in a fresh process.** The registrar refuses a role that
   `MODULE_ENTRIES` already holds and no row declares (`registrar.py:114-120`). In a fresh subprocess the table
   starts empty (`:64`), so a deleted row simply registers nothing. A `verb_call` has a second owner that notices,
   the prize row (refusal (c), `_part6:76-79`). A `step_call` or `query` has no prize row. **§2.3 adds the need
   that makes deletion refuse.**
3. **`modules/` does not exist yet** (`git ls-files` finds only `godot/skeleton/.../modules/`). IN-03 (`31a`, B-L)
   creates it (`_part4:184`). The settlements roster entry still names `home: "systems/settlements/"`
   (`rosters.yaml:1888`).

---

## 2. The mechanism every extraction shares

### 2.1 Where the code goes

- **The rule** goes to `modules/settlements/<file>.py` as a pure function of one typed input record. It does
  not read or write `World`, holds no token, keeps no state between calls and imports no other module (A-25).
- **The input and output record types** live host-side, beside the projection builders, in
  `queries/world_q.py`. The module imports them, since it depends upward on `engine/`. IN-03's precedent says
  the same: *"The builder and the input and output types live host-side, where projections are built (A-25);
  the module imports the types"* (`_part4:190-191`). They do not go in a new `queries/` file:
  `world_q.py:851-854` refuses a fourth `queries/` module. **[ASSUMPTION A1]** The record kind is whatever IN-03
  lands (`Said` is a `NamedTuple`, `_part4:299`), with one shape for every settlements record.
- **The projection builder** (host) reads `World` and builds the input record. **The public query names stay
  host** as projection wrappers, keeping their signatures and their `TRACE.query` line: `subsistence_draw`,
  `demanded`, `delivered`, `population`, `capacity`, `ceiling`, `share`, `fortification_of`. This matters
  because callers outside the loop use them (effects, the harness, tests). The trace is also part of committed
  output: `demanded`'s `QUERY` row appears in the committed `runs/TRACE.txt:3287` and `:3947`, which
  `test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte` holds byte-for-byte.
  **[ASSUMPTION A3]** So the falsifier's "host body gone" is checked by `rg` on **the rule's own expression or
  helper**, named per extraction below, not on the public name.
- **The write** stays host: every `w.write(...)` in `loop/matter.py`, every `Observation` construction and
  every `_crossings` emission (an L5 emission rule, `matter.py:35-82`).

### 2.2 How a call site reaches the entry

**[ASSUMPTION A2]** Every settlements call site resolves its role by string, through
`engine.substrate.composition.require(role)`, inside the call. That is the shape
`seam/wrappers/mass_battle.py:117-122` already uses, and `require` caches (`engine/substrate/composition.py:58-59`).
Some callers run with **no driver**: `harness/populated.py:425` reads `capacity` while it seats cohorts at
world-gen, and `harness/scarce.py:158` reads `demanded`/`delivered`. Since `MODULE_ENTRIES` is filled only at
driver construction (`loop/driver.py:267-271`), a lookup through it would refuse in those callers.
`MODULE_ENTRIES` stays the construction-time record and the subject of §2.3's check. *Revert:* if IN-03's
build routes `verb_call` sites through `MODULE_ENTRIES` and Jordan wants one lookup path, the driverless
callers construct a driver first.

### 2.3 Making a deleted row refuse at driver construction

**[ASSUMPTION A2, continued]** The host declares what it calls, in the file that calls it:
`loop/matter.py::STEP_CALLS` and `queries/world_q.py::QUERY_ENTRIES`, each a tuple of
`(role, entry kind)`. One new registrar function, `require_entries(needs)`, runs right after
`register_module_entries(VERB_TABLE)` (`driver.py:271`). It refuses, with `_refuse`'s `Unspecified` naming
the role (`registrar.py:67-71`), in two cases:

- a needed role that `MODULE_ENTRIES` does not hold;
- a needed role registered under a different `entry:` kind.

This is the host stating WHAT it needs while the composition row states WHICH module provides it — the split
`module_contracts.yaml:30-36` already describes. It is not a second owner of the module's identity.

The same check covers the levy feed's query (§4), which is declared in `seam/wrappers/mass_battle.py`.

### 2.4 The four falsifiers, made executable once and reused

| part | instrument |
|---|---|
| both hashes unchanged | Read the realm hash and the corpus hash on B-T's base commit **before** each extraction, then again after it. The realm hash is `World.content_hash()` (`state/world.py:1274`) on `harness/populated.py::build_realm(0)` (`:446`) after one season. The corpus instrument is B-T's to name **[UNVERIFIED: `harness/corpus_run.py` prints no single corpus hash; its only hash site is the R4 same-seed comparison at `:836`]** |
| old host body gone | `rg -n '<pattern>' engine/` returns nothing. The pattern for each extraction is in §3 |
| a deleted row refuses | In a fresh subprocess, strip one settlements row's `entry:` (or delete the row) from `composition.ROLES` before `SeasonDriver(...)`. Construction must raise `Unspecified` naming the role. Precedent: `tests/valoria/test_module_registrar.py`'s per-case subprocess (`registrar.py:39-42`) |
| one seed twice, one hash | One process: `build_realm(0)` and one season, twice. The two `content_hash()` values must be equal. This catches module-level caches, which A-25 forbids |

**Order matters to the hash.** A `Rung` is digested as `repr(sorted(vars(obj).items()))` (SE-04's citation of
`state/world.py:181-182`), so the insertion order of keys **inside** `Rung.stores` reaches the hash. The
comment at `matter.py:325-326` says so of the draw. Every output record below therefore carries ordered
tuples in the order today's loops produce them, never an unordered mapping, and the host rebuilds dicts from
them in that order. Float expressions are copied operand for operand (yield, §3 E3; fortification, §3 E6).

---

## 3. The extractions

Six entries plus one shared query, in build order. Each subsection gives: the rule as it lives today; the
role and its entry kind; the typed input and output; what stays host; the `rg` pattern that must go to zero;
the covering tests.

### E1 · `settlements.larder_draw` (`query`) and `settlements.drawn_under` (`query`) — the larder ladder

**Today.**
- `world_q.py:498-544`, `nearest_store`: walk up from a rung (`parent_of`, `:543`) to the first rung holding
  `> 0` of a kind. It reads a running `available` view first (`:535-540`) and stops at the first id not in
  `w.rungs` (`:533`).
- `world_q.py:547-624`, `subsistence_draw`: for each housed person in sorted id order (`:602`), skip
  non-cohorts (`:604-605`). For each weighted kind in sorted order (`:609`): `want = wt * person.weight`
  (`:610`); the source is `nearest_store` over the running `left` (`:613`); `take = min(want, held)` (`:620`).
  The result is `{pid: (home, {kind: (want, take, src)})}`.
- `world_q.py:696-708`, `_drawn_under`: sum one column (want or take) over eaters homed in a subtree. Its two
  wrappers are `demanded` (`:627-664`) and `delivered` (`:667-693`).

**Input.**
- `LarderInput`:
  - `weights: tuple[(kind, int)]`, sorted by kind;
  - `eaters: tuple[Eater]`, sorted by pid, where `Eater(pid, home, weight: int, is_cohort: bool)`;
  - `ladders: tuple[(home, tuple[rung, …])]`;
  - `stores: tuple[(rung, tuple[(kind, int)])]`, in each rung's own dict order.
- How the host builds it:
  - `ladders` is `ancestry(w, home)` truncated at the first id not in `w.rungs`. `ancestry` includes the start
    and returns `[id]` for an unknown id (`state/containment.py:104-106`), while `nearest_store` stops there.
  - `is_cohort` is read off the carrier property (`state/carriers.py:621`), so the module does not
    re-derive `weight > 1`.
- `Under(record: DrawRecord, subtree: frozenset[str], column: "want" | "take")` is `drawn_under`'s input. The
  host builds `subtree` with `_subtree` (`world_q.py:951-956`).

**Output.**
- `DrawRecord(rows: tuple[DrawRow])`, where `DrawRow(pid, home, cells: tuple[(kind, want, take, src | None)])`.
  It is the record `subsistence_draw` returns today, as ordered tuples.
- `drawn_under` returns `tuple[(kind, units)]`, sorted (`:708`).

**What it computes.**
- The cohort exemption (`ED-IN-0255`): **[ASSUMPTION A5]** the module applies the rule and the host supplies
  the predicate's value.
- The ladder walk over a running view, which is how scarcity binds (`:519-524`).
- `take = min(want, held)` with no further walk.
- The subtree sum.

**Stays host.**
- `subsistence_draw(w)` (projection plus call, returning today's dict shape; four test files read it).
- `demanded`/`delivered` with their `TRACE.query` lines (`:663`, `:692`).
- `home_of` and its trace.

**[ASSUMPTION A4]** The per-eater `QUERY nearest_store` trace rows disappear. No committed artifact carries
one (`rg nearest_store engine/season/runs/` finds none); `test_w15` is the falsifier if that is wrong.

**`rg` to zero.** `def nearest_store`, `def _drawn_under`, `wt \* person.weight`.

**Tests.**
- `tests/test_demand_delivery.py`
- `tests/test_territorial_subsistence.py`
- `tests/test_governance_build.py` and `tests/test_season_shape.py`, both of which name `nearest_store`.
  Re-point them to the module and re-read each one, not assume it.

### E2 · `settlements.subsist` (`step_call`, MATTER) — draw, dearth, debit

**Today.**
- `matter.py:327`: MATTER calls `subsistence_draw`.
- `matter.py:328-338`: derives `draws`, `short_by_person` and `drained` from the record.
- `matter.py:381-386`: computes each drained rung's gap per kind, `demanded - delivered`.
- `matter.py:425-432`: `lost = body_step * Σ short`, skipped at `<= 0` (the control arm).
- `matter.py:437`: `max(0, body - lost)`.
- `matter.py:444`: death at `<= 0`.
- `matter.py:459-463`: the debit `after = have - amt`, written only if something changed.

**Input.** `SubsistInput(larder: LarderInput, body_step: int, bodies: tuple[(pid, int)])`. `bodies` is sorted
and holds eaters only.

**Output.**
- `SubsistOutcome`:
  - `draw: DrawRecord`;
  - `short_by_person: tuple[(pid, tuple[(kind, int)])]`, sorted pid, sorted kind (`:331-336`);
  - `shortfalls: tuple[(rung, tuple[(kind, int)])]`, sorted rung, sorted kind, positive only (`:382-386`);
  - `falls: tuple[BodyFall]`, sorted pid, with `lost > 0` only;
  - `larder_after: tuple[(rung, tuple[(kind, int)])]`.
- `BodyFall(pid, body_after, dies: bool)`.
- `larder_after` holds changed rungs only. Within each rung, kinds appear in the order the draw first debited
  them (`:334`), because that order reaches `r.stores.update(...)` (`:469`).

**What it computes.** The ledger of one season's subsistence: who ate what from where, who went short, whose
body falls by how much, whether that body reaches zero, and what each larder holds afterwards. This
**reconciles with `drawn_under` by construction**: one module computes both, as `world_q.py:552-557` requires
of their owner today.

**Stays host.**
- `w._subsistence_shortfall` (`:403`) and the `TRACE.note` sample (`:387-400`).
- Every body write (`:436-440`).
- `_crossings` (`:442-443`).
- Every death write (`:449-453`).
- Every debit write with `observed=` (`:468-473`).
- The `Observation(src, f"{SHORTFALL_PREDICATE}:{k}", n)` construction (`:385`). The predicate string is host
  vocabulary (`data/requires.py`).

MATTER calls the entry once, where `:327` stands.

**`rg` to zero.** `step \* sum(short_by_person`, `have.get(k, 0) - amt`, `need\[k\] - got.get`.

**Tests.**
- `tests/test_territorial_subsistence.py`: an office-holder keeps his body while the cohort's body falls
  (`matter.py:302-304`).
- `tests/test_season_shape.py`, `-k w8` and the `LB-3b` pins (`matter.py:423-424`).
- `tests/test_demand_delivery.py`.

⚠ **`inspect.getsource(SeasonDriver.matter)` is read by eight tests** (`matter.py:3-9`). Before editing MATTER,
`rg` for every pin that asserts on MATTER's source text, and re-record the ones that name the moved lines.

### E3 · `settlements.produce` (`step_call`, MATTER) — yield and credit

**Today.**
- `matter.py:485-491`: for each site in id order whose `site.rung == rid`, and each `(k, base)` in
  `SITE_YIELD[kind]` (`data/fixtures.py:175`), add
  `int(base * (max(0, condition) / condition_scale) * season_factor)`. Zero entries are dropped.
- `matter.py:501`: credit `stores + produced`. This reads the stores **after** the same rung's debit write
  (`:468`), because each rung's debit, yield and credit run in sequence inside the per-rung loop (`:455-506`).

**Input.** `ProduceInput`:
- `table: tuple[(site_kind, tuple[(kind, base)])]`;
- `scale: int`;
- `factor`;
- `sites: tuple[(site_id, kind, rung, condition: int)]`, sorted by id;
- `stores: tuple[(rung, tuple[(kind, int)])]`;
- `larder_after`, from E2's output, overlaid on `stores` by the module.

**Output.** `ProduceOutcome(rows: tuple[(rung, produced: tuple[(kind, int)], credited: tuple[(kind, int)])])`.
Rungs are sorted, and only those with nonzero `produced` appear. Kinds within a row follow site order, then
table order, as the loop builds them.

**What it computes.** What each rung's fabric yields this season, scaled by its condition, and the larder that
results. The order rule — draw before produce, `#353 §25`, `matter.py:268-272` — is kept by the host calling E2
before E3.

**Stays host.** The `yield` and `stores` writes (`:495-506`) and the `last_emission_of` causes.

**`rg` to zero.** `base \* (max(0, site.condition)`.

**Tests.** `tests/test_season_shape.py::test_w8_matter_draws_before_it_produces_which_is_353s_stated_order`
(named at `matter.py:310-311`); `tests/test_governance_build.py` (`SITE_YIELD`).

### E4 · `settlements.housing` (`query`) — population and capacity

**Today.**
- `world_q.py:800-802`, `population`: the summed `weight` of residents (`residence_of`, `:738-769`) whose
  residence lies in the subtree.
- `world_q.py:842-844`, `capacity`: `max(capacity_floor[dwelling], dwelling Sites in the subtree)`.

**Input.** `HousingInput`:
- `subtree: frozenset[str]`;
- `residents: tuple[(pid, rung, weight: int)]`;
- `dwelling_rungs: tuple[rung]`, one entry per dwelling Site;
- `floor: int`.

**Output.** `Housing(population: int, capacity: int)`.

**What it computes.** RR-2: residents and not persons present (`:777-781`), and `ED-SE-0051`'s floor.

**Stays host.**
- `residence_of`, with its two-edge `Forbidden` (`:762-767`).
- `population(w, r, residence=None)` and `capacity(w, r)` as wrappers.
- `_eff_migrate`'s refusal, `population + weight > capacity` (`loop/effects_migration.py:171`). That is an
  effect body (A-25).

**`rg` to zero.** `capacity_floor"\)\[DWELLING_KIND\]`, `w.persons\[pid\].weight for pid, home in residents`.

**Tests.** `tests/test_migrate_capacity.py`, `tests/test_works_founding.py`, `tests/test_aperture.py`.

### E5 · `settlements.fabric` (`query`) — a works' ceiling and the commons' share

**Today.**
- `world_q.py:274-287`, `ceiling`: `condition_scale` when no live works names the site or the works declares
  no terms. Otherwise `scale * min(matured, declared) // declared`.
- `world_q.py:304`, `share`: `(1, max(1, len(presence)))`.

**Input.** `FabricInput(scale: int, live_works: int, declared: int, matured: int, present: int)`.

**Output.** `Fabric(ceiling: int, share: (int, int))`.

**What it computes.** The bound on a fabric's rise (r2 §A.6.3: multiply first, divide last) and the commons
share (§A.6.4).

**Stays host.**
- `works_for` and `matured_terms` (`:209-247`; a Record/hold scan and a log scan).
- **[ASSUMPTION A6]** The two-live-works `Forbidden` (`:276-281`). It is a store-integrity backstop against
  hand-built worlds, not a settlement rule.
- `resolve.py:851`'s clamp and `_rise`'s `headroom * num // den` (`loop/effects_economy.py:126-130`). Both are
  fold and effect bodies, so A-25 keeps them host.

**`rg` to zero.** `scale \* min\(matured_terms`, `max\(1, len\(presence\(`.

**Tests.** `tests/test_works_founding.py`.

### E6 · `settlements.fortification` (`query`) — a settlement's walls

**Today.** `world_q.py:1015-1020`: the mean garrison condition over the subtree, divided by scale; `0.0` with
no garrison. Its one caller is the field adapter (`seam/wrappers/mass_battle.py:180`).

**Input.** `FortInput(conditions: tuple[int], scale: int)`.

**Output.** `float`, computed as `sum / (scale * n)`, operand for operand.

**What it computes.** `H-38`'s *"`Site.condition` is the model"* applied to defence.

**Stays host.** `fortification_of(w, r)` as the wrapper the adapter calls.

**`rg` to zero.** `sum\(s.condition for s in garrisons\)`.

**Tests.** `tests/test_mass_battle_provider.py`, `tests/test_march.py`.

**Why extract one-line rules at all (E4–E6).** The module is what the port carries. A-25 places the port's
`core/modules/<name>/` beside the module (`_part5:401`), so a settlement rule left inside `world_q` is a rule
the port must hand-transcribe. **[ASSUMPTION A12]** If Jordan reads E4–E6 as overhead (NERS-E, *"no
unnecessary overhead"*), they drop and E1–E3 stand alone.

---

## 4. Considered and NOT extracted — each with its reason

**`state/gate.py`: zero extractions [ASSUMPTION A7].**
- Every rule in it is F3 write authority:
  - `seat_hold` (`:230-250`);
  - `purview_reaches` (`:253-287`), which levy's `basis: purview` conjunct reads (`verb_table.yaml:567-570`);
  - `may_fill` (`:371-391`);
  - `may_renew` (`:394-422`);
  - `sits_over` (`:425-445`);
  - `may_determine` (`:448-501`);
  - `tenure_write_basis` (`:538-757`).
- The gate never observes stores (`:419-421`), so it computes no settlement quantity.
- Two further reasons it cannot call a module:
  - A-25 has the host write World *through the gate*, so the gate is host by definition.
  - `state/` imports only `data/`, `gaps` and `state/` (`:47-55`), so reaching `MODULE_ENTRIES` (in
    `manifest/`) from it would invert the layering.
- B-T's EDITS column lists `state/gate.py` (`_part3:272`). Under this design that is a plan line to drop
  (see the receipt).

**Other host rules that stay host:**

| rule | where | why it stays host |
|---|---|---|
| `upkeep_of` | `world_q.py:1260-1291` | An Office field with a fixture fallback. It is governance, a management space whose verbs are host (A-25) |
| `members`, `leaders`, `footprint`, `density`, `mustered`, `sovereign_fraction`, `provinces_of`, `faction_holding`, `holder_faction_of`, `uncontrolled` | `world_q.py:875-1229` | Polity queries over `commit`/`hold`, i.e. faction management (A-25 roster). `mustered` is the field adapter's projection |
| site wear | `matter.py:557-587` | **[ASSUMPTION A10]** A one-line clamp on every Site kind. The clock is AX-5's matter self-motion, not a settlement economy rule. It is the next candidate if Jordan wants every Site rule in the module |
| record stages | `matter.py:139-183` | A Record clock, and `Tenure` is host |
| tenure terms | `matter.py:214-221` | A Tenure clock, `T-n`, judged by the gate |
| claim decay | `matter.py:235-265` | Knowledge, which is HOST (A-25) |
| travel | `matter.py:542-551` | A Person leg |
| `_crossings` | `matter.py:35-82` | An L5 emission rule shared by Sites and persons |

**Effect bodies stay host** (A-25): `_eff_levy`, `_eff_migrate`, `_rise`, `_eff_march`.

---

## 5. The levy-to-field feed

**What happens today.**
- `levy` moves `amount` of `kind` from the levied rung's `stores` into the treasury, which is the rung of the
  seat the act exercises (`loop/effects_governance.py:340-347`, conserved through `_shift`,
  `loop/effects_shared.py:117`; the row is at `verb_table.yaml:557-580`).
- A field's force is people:
  - The attacker is the mustered members at the actor's nearest settlement under the `via` office's faction
    (`loop/sides.py:77-83`).
  - The defender is `mustered(target, holder faction)` (`seam/wrappers/mass_battle.py:154`).
  - Each side becomes **one** subunit sized `troops = Σ Person.weight` (`systems/mass_battle/sim/massbattle.py:326-329`,
    floored at `_MIN_TROOPS`, `:215`).
- So **nothing a levy does reaches a field.** `massbattle.py:187-196` records that a weight-to-troops conversion
  is open work and refuses to invent one.

**The feed, proposed [ASSUMPTION A13].** A levied treasury **provisions** a field; it does not create troops.
Troops stay people; stores bound how many of them can be fielded. A new query, `settlements.provision`
(`modules/settlements/provision.py`), is called by the field adapter for each side.

- **Input.** `ProvisionInput(weight: int, stores: tuple[(kind, int)], ration: tuple[(kind, int)], on: bool)`.
  - `weight` is the side's Σ `Person.weight`.
  - `stores` is the side's treasury.
  - `ration` is the larder's own `subsistence_weight` table. This is the same ladder in the same units, since
    a cohort's `want` is `wt * weight` (`world_q.py:610`): a field eats as the people it is made of eat.
  - `on` is a new fixture, `field_provisioning`, shipped off. Its precedent is `field_walls_dr`'s sweep
    (`hole_register.yaml:3204`).
- **Output.** `Provision(troops: int, consumed: tuple[(kind, int)])`.
  - When `on` is false: `troops = weight` and `consumed = ()`. This is the control arm, byte-identical to today.
  - When `on` is true: `troops = min(weight, min over kinds with ration > 0 of stores[k] // ration[k])` and
    `consumed = ration[k] × troops`, per kind.
- **The treasuries.**
  - Attacker: the rung of `a.via`'s office, the same treasury `levy` fills (`effects_governance.py:342`).
  - Defender **[ASSUMPTION A14]**: the stores of the nearest held rung at or above the target, the walk
    `holder_faction_of` already makes (`world_q.py:1185-1188`).
- **Consumption [ASSUMPTION A15].** `_eff_march` (RESOLVE, host) debits `consumed` from each side's treasury.
  A field that only *bounded* would be a ratchet: levy once and you are provisioned for every battle after,
  which fails NERS-R's completeness. The march row's `writes:` gains `Rung.stores` once per side.
  - **Rejected, with reasons:**
    - Converting stores into troops. That mints persons, and no step constructs a `Person`
      (`matter.py:95-97`).
    - Scaling troops by a function of stores. That invents the conversion `massbattle.py:187-196` refuses.
    - No feed at all. That is kept as the control arm.
- **An unprovisioned side** fields `troops = 0`, which massbattle's crash floor lifts to 1 (`:197`).
  **[ASSUMPTION A16]** It is a floor, not a refusal. Whether `march` should refuse at its precondition when the
  treasury is empty is the march row's question; this design does not answer it.
- **What the adapter passes.** `resolve_field` gains `troops_a`/`troops_b` keywords, where `None` means
  Σ weight, i.e. today. That is an edit to the mass battle module after it moves (IN-05, `31c`), in the MB lane.

**J-18.** A season field is one troops-sized subunit, so its depth varies with force size
(`_part5:505`, `massbattle._weighted_unit`, `massbattle.py:202-219`). The feed changes `troops` and therefore
depth.
- Under J-18 (A), the recommended answer that MB-07 builds, support past the weapon's reach is capped. A
  better-provisioned force then scales through its relief terms, not its pool.
- Under (B), depth keeps adding pool down to the 0.3 floor.

The feed's code does not depend on J-18's answer, but the size of its effect does. **The `on` arm is measured
only after MB-07 lands (B-D2)**, and a J-18 revert re-reads it.

**Sequence.**
1. IN-49 (B-K) makes `levy` execute in computed play (`_part5:333-338`). Until then treasuries fill only from
   hand-built acts, and the `on` arm would read empty treasuries and floor every field.
2. The feed is built with `on` false, so the hash does not move.
3. Flipping `on` is a **declared hash mover**, read against the `off` arm on the same seed.

**Feed falsifiers.**
- At `on = false`, both hashes are unchanged.
- At `on = true`, a seeded march whose attacker treasury holds less than one ration per weight fields fewer
  troops than its mustered weight, and its treasury falls by `consumed`.
- A planted second levy into the same treasury raises the next field's troops.

---

## 6. Where SE-04 meets this module

- **(a) H-170** (`hole_register.yaml:3700-3711`). The arms change `cohorts[].weight`, which reaches only
  `Eater.weight` (E1) and `residents[].weight` (E4). The module is unchanged by any arm, which is why IN-07's
  build precedes SE-04 (DEPS D). The arms then run through the module and the shipped `2` is their control.
- **(b) H-171 `Rung.envelope`** **[ASSUMPTION A17]**. No record here carries `envelope`, because modules write
  nothing. If SE-04 gives it a writer, the value is a field of `Housing` (E4) and the write is host. If SE-04
  deletes it, nothing here changes. `population` does not count it today (`world_q.py:789-794`).
- **IN-13's occupation-subsistence reader**, if its hole row calls for one (`_part3:272`), would be one more
  `SubsistInput` field. It is not designed here.

---

## 7. Build order inside B-T, one extraction per commit

1. **§2.3's `require_entries`**, landing with E1. Without a needed role it has nothing to check.
2. **E1 → E2 → E3.** These are MATTER and its draw. E2 and E3 share `larder_after`.
3. **E4 → E5 → E6.**

Each commit:
- reads both hashes on its base;
- adds one `composition_roles:` row with `entry:`, re-exported with `tools/export_composition.py` (blocking
  `--check`);
- adds one host-need tuple member;
- runs its covering test file and `tests/valoria/test_engine_does_not_import_systems.py`.

The first commit also moves the roster's `settlements` home to `"modules/settlements/"` (`rosters.yaml:1888`)
**[ASSUMPTION A18]**. Re-read what reads `home:` before moving it (`rosters.yaml:1870-1878` names
`R04_PENDING_SUBSYSTEMS` and `tools/evacuation_plan.py`).

The feed (§5) is a separate position. It edits `seam/wrappers/mass_battle.py`, `loop/effects_combat.py`,
`verb_table.yaml` (march) and the moved mass battle module, none of which is on B-T's file list.

---

## 8. Assumptions, gathered

| # | the call | revert |
|---|---|---|
| A1 | Record types live in `world_q.py`, in the record kind IN-03 lands | IN-03 lands them elsewhere → follow it |
| A2 | Call sites resolve by `composition.require` (because of driverless callers); driver construction checks host-declared needs with `require_entries` | One lookup path through `MODULE_ENTRIES`, with driverless callers constructing a driver |
| A3 | Public query names stay as host wrappers; `rg` targets the rule's expression | Rename the wrappers and re-point the tests |
| A4 | Per-eater `nearest_store` trace rows are dropped | `test_w15` reddens → the host emits them |
| A5 | The cohort exemption rule lives in the module and reads the host's `is_cohort` value | The host filters eaters |
| A6 | The two-live-works `Forbidden` stays host | It moves into the module |
| A7 | `state/gate.py`: zero extractions | Jordan names a gate rule as a settlement rule |
| A10 | Site wear stays host | Wear joins E3 |
| A12 | E4–E6 are extracted | Drop them as overhead |
| A13 | The feed bounds troops by the treasury, using the larder's ration, behind a `field_provisioning` fixture that ships off | No feed (the control arm) |
| A14 | The defender's treasury is the nearest held rung's stores | The target settlement's larder ladder |
| A15 | The field consumes its ration from the treasury, written by `_eff_march` | Bound only, accepting the ratchet |
| A16 | An unprovisioned side gets the crash floor, not a refusal | The march precondition refuses |
| A17 | No record carries `envelope` | SE-04 (b) gives it a writer → it becomes a `Housing` field |
| A18 | The roster's settlements home moves to `modules/settlements/` | Keep it and add a second root |

**Two of these lead to materially different games and are the ones Jordan's review should weigh first:**
- A13 + A15: whether levied stores bound and feed a field at all.
- A14: whose stores the defender eats.

Every other line is answered by precedent or by the architecture (`CLAUDE.md` §0, steps 4–5).
