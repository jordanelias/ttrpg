# 05 — Independent verification, corrections to the critics, and the method rule

## Status: FILED (2026-08-29) — analysis. Reads: [`00_INDEX.md`](00_INDEX.md)
## Everything in this file was verified by the synthesising session by READING the cited code,
## not by pattern-matching. Where a claim began as a search result it says so and says what the
## search would have missed.

---

## 1. The method rule this critique was run under

**Jordan, this session:** *grep, regex and glob are used to LOCATE and FIND, but not to CONCLUDE.*

A match count, an empty result or a pattern hit is a **pointer to a place that must then be opened and
read**. This binds hardest on negatives — *"nothing writes this"*, *"no caller exists"*, *"zero
references"* — because a pattern's silence is evidence about the pattern, not about the tree. Before
concluding a negative one must ask what the pattern would MISS: an alias, a dict write, a generic
setter, a value passed positionally, a key built at runtime, a differently-spelled synonym, or a
string-resolved call through `composition.require`.

**The repository already knows this and records the failure** (`registers/handoffs/HANDOFF_IN.md`):
*"Reachability is not an import graph … dependencies are declared in `references/` and resolved by
string at first call. `treaty.py` and `beliefs.py` have zero textual importers and are both live via
`composition.require` in `restore_world`. Check `module_contracts.yaml` as well as grep before calling
anything dead."*

The rule was relayed to all nine critics mid-run. Its effects are visible in the results: T4 rebuilt
its central negative by opening every contract block rather than matching, and downgraded one claim
from *"impossible"* to *"expressible but unwired"* as a result.

**It also caught this session.** A first pass at the cooked descriptor registry used a printer that
filtered to dict-valued keys, which silently dropped `roster` (a list) and would have supported the
false conclusion that no attribute roster exists. Reading the block verbatim showed the nine attributes
and the `pending_tenth` sentinel exactly as the suite claims. **The suite's claim was right and the
instrument was wrong** — which is the failure mode the rule exists to prevent, arriving in the
direction that would have produced a fabricated finding rather than a missed one.

---

## 2. Verified by reading — findings that stand

### 2.1 P0-7 is real, and it is four dead clocks, not one

A name-grep for `Turmoil` would miss a variable-keyed write, so **every site touching `world.clocks`
was located and then read**:

| site | what it does |
|---|---|
| `game_state.py:338` | initialises `{'CI': 30.0, 'MS': 60.0, 'IP': 20.0, 'PI': 0.0, 'Strain': 0.0, 'Turmoil': 0.0}` |
| `game_state.py:368` | serialises `dict(world.clocks)` |
| `game_state.py:439` | restore — `w.clocks = dict(snapshot['clocks'])`, which can only **echo** what was serialised |
| `victory.py:73` | reads `Turmoil` as political stability; `ps_ok = ps <= PS_MAX` |
| `ms_track.py:69,90` | writes literal `'MS'` |
| `ci_track.py:177` | writes literal `'CI'` |
| `mass_seizure.py:214` | writes a **module constant** key, not a variable |
| `excommunication.py:163-171` | routes through `ci_track.apply_ci_delta` — literal CI |

**No site anywhere writes `world.clocks[<variable>]`.** So the negative holds under reading, not merely
under matching: **`IP`, `PI`, `Strain` and `Turmoil` are initialised and never written.** `IP` even
carries an in-code comment saying so.

**Consequence the suite states too narrowly.** P0-5/P0-7 name one dead clock. The finding is that the
engine has **no general clock-writing mechanism at all** — two hand-written trackers and one flag. And
`11 §7`'s `we.altonian_pressure` proposes a **new** `institutional_pressure` place gauge without reading
the dormant `IP` clock that already exists for exactly that quantity. *(T7 reached the same collision
independently, from the design side.)*

### 2.2 `Key.causes` — P0-11 states it backwards

A `causes=` pattern would miss post-construction mutation, so **attribute access was located and read
instead**. `.causes` appears in non-test code at exactly two places, **both inside `keys.py` itself**:
`:166` (serialisation) and `:385` (the invariant that causes may only cite already-logged Keys).
**Nothing anywhere appends to a Key's `causes` after construction**, so construction sites are the whole
population. Reading those:

- `faction_action.py:399` — `causes=[]`, with the comment *"No upstream Key exists to cite:
  resolve_mass_battle is a plain call, not an emission. `[]` is the honest value — a fabricated cause is
  worse than no cause."*
- `parliamentary_transfer.py:232` — `causes=[]`
- `echo_transport.py:328` — `causes=[caused_by_key_id] if caused_by_key_id else []`, with a comment
  citing an honesty test.

**So the ruled independence metric is not blocked by discipline someone forgot. It is blocked because
two of the three emitters have no upstream Key to cite by construction.** P0-11 frames this as an
authoring gap; it is a **wiring** gap, and the remedy is to give those emitters genuine upstream Keys,
not to instruct anyone to populate a field. T3 independently reached the same conclusion from the other
end and added the sharper half: **empty ancestries are pairwise disjoint**, so the metric computed today
would count one witnessing retold three times as three independent supports — it **fails open**, and a
naive implementation would launder correlated rumour into corroboration.

### 2.3 The credence ghost — three-way independent rediscovery, verified

Read, not matched:

- `02_character_generation.md:464` — *"**Cut:** the standalone `credence` Gauge"*, executed at `:465-481`.
- `02_character_generation_part2.md:172` — `cg.stage`'s state list carries **zero Gauges**; `:121` — *"no
  credence disclosure row — 02 declares no Gauge"*; `:214-218` — a falsifier demanding zero `cg.*` gauge
  rows.
- `08_settlement_management.md:341` — deposits into `credence.<proposition>`.
- `08:354-356` — justifies it by citing *"`02 part 2 §10.1`'s `credence` row"*, **which does not exist**.
- `08:351-352` — quotes `02:521`'s *"move **confidence**"* as *"move **credence**"*.

**The suite's only post-generation belief writer is wired to an object the suite deleted**, and `08`'s
own stated motivation — *"nothing could move a person's belief after they were generated"* — remains
true after its own fix.

### 2.4 `scene.investigation_resolved` is registered

`systems/_architecture/key_type_registry_v30.md:881-897`, read in full: description *"Investigation,
inquiry, or trial concluded"*; required `scene_id`, `subject_id`, `finding`; **optional `witnesses`**;
`emitting_systems: [scene_slate, faction_politics]`; `consuming_systems: [faction_layer, npc_behavior,
articulation]`. `08 §6.3` declares no such type exists and calls the witness set undefined. **Both halves
are wrong, and the registered type already carries the field `08` says is missing.**

### 2.5 The unbounded-gauge hole is two gauges

`engine/engine_params/descriptors.json`, `practitioner_stats` block read verbatim:

```
prac.thread_sensitivity   floor: 0     ceiling: null   open_ceiling_reference: 100
prac.tps                  floor: null  ceiling: null
```

The suite names `prac.thread_sensitivity` five times across `00`, `01`, `01 part2` and `13` P0-5 as *the*
case where three declaration-time guards are inert. **`prac.tps` sits two lines away with both bounds
null** — strictly worse — and appears nowhere in the suite under any spelling located (`prac.tps`,
`TPS`, `pool score`). Every author who found the TS defect had the TPS row on screen.

**And the remedy differs in the two directions:** the TS fix is cheaper than P0-5 implies, because the
`100` is already in the file and merely sits in a field the guards do not read; the TPS fix is more
expensive than anyone has costed, because there is no value to promote.

### 2.6 The spine: three stubs, one reason

Read in full (see [`00 §2`](00_INDEX.md)): `mc_v18.py:212-218` defers knot formation because *"Prerequisites
… are personal-scale actor fields (Disposition, Bonds, TS) that do not exist anywhere on the aggregate
strategic World — the same 'context-derivation gap' the `scene_dispatch.py` module docstring already
names for combat/contest actor derivation"*; `mc_v18.py:194-202` defers NPC generation for the same class
of reason; `combat_bridge.py:103-111` derives one field from `faction.Mil` and labels the Combatant with
the faction id. **One absence explains four stubs, and the suite closes it without naming it.**

### 2.7 The shipped NPC chooser reads world truth, and names factions

`faction_action.py:208-273` read in full. Four state signals — `_conquest_targets`,
`_mil_advantage_signal`, `_undergoverned_share`, `_threat_signal` — re-weight four prior buckets, then a
single `rng.random()` draw dispatches. **`_threat_signal` (`:196-206`) walks adjacency and compares
`world.factions[t.owner].Mil > faction.Mil`** — perfect knowledge of every neighbour's military
strength, in shipped code. No belief term anywhere.

**And a contrast worth recording in the suite's favour:** `_try_faction_unique` dispatches *"by
`faction.name`"* — Crown gets Crown Initiative, Church gets an Excommunication → Council → Absolution
priority chain. That is exactly the `if faction == X` scripting drift `00 §6` principle 2 forbids. **The
suite's principle is right and the engine currently violates it**, which is an argument for the suite
that no suite document makes.

---

## 3. Corrections to the critics

Per `CLAUDE.md` §0.1, agent results are not taken at face value.

| # | critic claim | correction |
|---|---|---|
| **C-1** | T8: the emission cap is a **BLOCKER** — Phase 6 can produce a world that crashes | **Downgraded to an unowned reconciliation item.** The cap does raise rather than clamp (`keys.py:561-565`) and is live by default (`ECHO_TRANSPORT` defaults ON, Jordan 2026-07-08) — but the tree emits **164–229 Keys per campaign** (`engine_clock.py:47`), ~3–5 per season against a per-tick cap of 64 (~13× headroom), and `echo_transport.py:96-103` labels the constant *"CALLER-SUPPLIED … NOT canonical mechanical constants"*, ruled that way under ED-IN-0026 and tunable via `ECHO_EMISSIONS_PER_TICK_MAX`. **The unowned-baton half stands; the architecture-blocker half does not.** |
| **C-2** | T4: *"the only consumer of `Holding` is the Slate"* (grep-derived) | **Upgraded by the critic on request**, by opening every contract block. Two self-corrections resulted: belief-reading advance terms are **expressible but unwired**, not impossible; and `02 §6` **is** a real NPC-side Holding consumer, governing what an NPC *believes* rather than what it *does*. Final wording carried: **no action-selection function takes a belief as input.** |
| **C-3** | T2: `RELATION_SHARE_MAX` might make beliefs decorative by construction (the brief's framing) | **The critic refused the brief and was right.** The cap binds only summed selection terms; form-transition gates, `allegiance` transitions, Knot rupture and `09` advance predicates all fire off affective state **uncapped**, and the creed-revision → Scar path exits the cap entirely. **The cap is sound design and should survive.** T3 reaches the opposite conclusion for *belief specifically* — and both are right, because belief alone has no gate consumer. |
| **C-4** | T3 and the ruled design cite `causes=` at `:317/:166/:389` | **Line numbers have drifted** to `:328/:232/:399`. Substance upholds. |
| **C-5** | T8: `13 §1` cites `wiring_map_check --summary` | **Confirmed as a wording defect**: that tool was retired in plan S5c; the live instrument is `tools/build_contract_index.py:653`. `13 §2` demands re-verification of engine claims and then cites a retired instrument for its own headline number. |

---

## 4. Method notes carried forward

1. **Independent rediscovery is the bankable signal.** X-1 was found by three critics who could not see
   each other; X-3, X-4, X-6 and X-7 by two each. `CLAUDE.md` §10 records why this matters more than any
   single critic's confidence.
2. **Steelman-first changed the results.** Every critic was required to build the strongest version of
   the suite's answer before attacking it, and several of the sharpest findings are *"this good mechanism
   is one named producer away from working"* rather than *"this is wrong"* — which is a materially
   different, and more useful, class of finding.
3. **Null results were required to be stated.** Each critic's coverage note records what it did **not**
   read, so silence elsewhere is legible rather than mistaken for coverage.
4. **The suite's evidentiary hygiene is genuinely good.** T1 checked thirteen tree citations by hand and
   reported: *"Every tree citation I checked was accurate — the findings above are design holes, not
   fabricated citations."* This critique found **no fabricated `path:line` anywhere in the suite.** The
   defects are cross-document staleness and unowned seams, not invented evidence.
