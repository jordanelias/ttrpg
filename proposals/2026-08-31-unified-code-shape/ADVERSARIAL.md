# ADVERSARIAL REVIEW — the ideal unified code shape

## Status: reference. Written 2026-08-31 against working-tree HEAD `d080535`
## (branch `claude/pr345-trace-reconciliation-kysn30`; the suite landed at `0ceddd6`, and `d080535`
## — the query-catalogue count fix — landed **during** this review and is accounted for below).
## Under `CLAUDE.md` §0.05 this document is **REFERENCE, never mechanism.** It rules nothing.

> **METHOD.** Everything gradeable by running was **run**, not read. Structured files were parsed
> (`yaml.safe_load` / `json.load`), never `grep -c`. Every `path:line` cited below was opened. Every
> finding carries the refutation I attempted against it; the ones where the refutation **succeeded**
> are in §6, not in §1–§5, because a finding I could not break is worth more than a long list.
>
> **Counts. FATAL: 0 · MAJOR: 16 · MINOR: 14.** (Seventeen MAJOR headers, sixteen distinct findings —
> Momentum appears twice, at §2.4 as a smuggled departure and at §5.1 as the seventh false N-line,
> because the two criteria ask different questions of the same object.) **Nothing here is fatal.** The suite's central
> architecture survived every attack I could execute against it. What did not survive falls into four
> recurring classes: **derived counts computed by subtraction or from memory instead of by re-counting**
> (six instances — the exact defect the suite corrects in its sources, occurring inside the suite that
> carries the lesson); **one flagship finding mislabelled in a way that makes its own prescribed fix
> unsafe**; **one conflation a source lane names and forbids by name**; and **four values that enter the
> shape with no owner, no write class, or no N-line**, including one object two independent critics had
> already cut.

### The three that matter most

1. **§2.1–2.2 — the `0.671` finding is mislabelled, and the fix it prescribes is unsafe.** It is not an
   arithmetic error: `proposals/2026-08-29-valoria-from-scratch/10_resolution_surface.md:17–19,160`
   **declares its own die** (no botch face) and derives σ ≈ 0.671 correctly from it. Both constants are
   exact for their own model — I computed them. So "wrong wherever it is quoted" is false, and editing
   σ to 0.800 while leaving μ = 0.5 and the Pool/σ table would break the source documents. **And the die
   swap the suite actually makes is a departure from the design line that is never declared or priced**
   — under the executing die a 1D pool can net **below zero**, which the design-line die cannot.
2. **§5.1 — the seventh false N-line is `Momentum`, and it was already cut, twice, by the suite's own
   source.** `16_ners_audit.md:44–46` heads it *"§2 The three false N-lines → 2.1 MOMENTUM — CUT. Found
   independently by two critics"*, and the cut was **applied**. The suite re-adds it with no owner, no
   write class, no params row, and a **per-scene** grant that breaks its own P-A/P-C fidelity
   invariance. The possibility survives the cut because Convictions already weight the option ranking.
3. **§2.3 — `06` §6 performs the exact conflation its source lane names and forbids.**
   `03_arcs_41_55_and_emergent.md:31–35` says *"The seven LOST arcs share one blocker, **and it is not
   thresholds** … §5 separates the two claims, **because the corpus has been conflating them**."* The
   suite's *"the ten LOST arcs are one loss, ten times"* is that conflation, and it contradicts the
   suite's own `05` §3, which **closes** the world-substrate hole five of those seven die on.

---

## Status / what was RUN

Every command below was executed in this checkout. Results are the ones quoted throughout.

| # | command | result |
|---|---|---|
| 1 | `python3 tools/m1_acceptance.py --summary` | `verdict: NOT MET`, 2 rows failing; row 1 FAIL (2 stub calls), row 2 PASS (`641aa8c55c3e…`), row 3 PARTIAL, **row 4 `0/7` and self-declared DOC-DERIVED**, row 5 BLOCKED |
| 2 | `python3 proposals/_session_provenance/2026-08-31-fable5-review/throughlines/sweep.py` (HEAD) | `swept: 163 · CITED: 24 · UNCITED: 139` |
| 3 | same sweep in a worktree at `origin/main` (`ca77f21`) | `swept: 153 · CITED: 24 · UNCITED: 129` |
| 4 | same sweep against local `main` (`f59fd0e`; the script does not exist at that ref, so it was copied in) | `swept: 150 · CITED: 24 · UNCITED: 126` |
| 5 | `run_campaign(seed=7, max_seasons=3)` vs `max_seasons=50` vs `params={'CAMPAIGN_SEASONS':3}` | final season **50 · 50 · 3** — `max_seasons` is dead, confirmed by execution |
| 6 | seeded campaign `seed=42` with the live `World` captured | `keys_emitted=169`; **2 distinct key types** (`scene.contest_resolved` 104, `scene.battle_concluded` 65) of **55** registered; `npcs_generated=0`; `world.npcs` empty |
| 7 | scheduler subscription census on the same run | **13 subscribed types, none of them one of the two emitted** |
| 8 | AST census of `.adjust(` over non-test `engine/` + `systems/` | **31 sites · 20 write `L` · 9 modules · exactly 1** (`engine/cross_scale/echo_transport.py:455`) inside a `sched.emit(key, apply=…)` callback |
| 9 | `json.load` over `engine/engine_params/key_types.json`, scale-field scan | **4 malformed fields across 2 types** (`mechanical.scene_entered`, `meta.cascade_cluster_event`) — flow-lists with trailing comments parsed as strings |
| 10 | emitted each affected type with no explicit scale signature | both **raise** `KeyValidationError: … non-canonical scale '['` — the two types are unemittable, proven by execution |
| 11 | `typing.get_type_hints` over every non-test module in `engine/` + `systems/` (139 modules, side effects suppressed, per-module) | **exactly 15** raise `NameError` on an unimported annotation (2 further raises are `staticmethod`/NamedTuple artifacts of the probe, not annotation defects) |
| 12 | module-reachability probe over the same campaign | **70 of 139** non-`__init__` modules never loaded (89 of 169 loaded counting `__init__`) |
| 13 | world-registry census on the live `World` | **11 of 13** post-migration registries empty by `len()`; **12 of 13** by content; only `settlements` (37) populated |
| 14 | `composition.require` spy through a default seed-42 campaign | **12 roles resolve**, not 5 |
| 15 | AST search for `class Person\|Rung\|Office\|Site\|Tenure\|Query\|Act\|Claim\|Proposition\|View\|Sensation\|StateChange` across all Python | **zero definitions** — the suite's fact 1 confirmed |
| 16 | `grep`-then-open on `generate_npc` | defined `systems/world/sim/npe.py:226`; **zero production call sites** — the only non-test mentions are comments saying it gets none |
| 17 | `json.load` consumer/emitter census over all 55 key types | **5** with an empty consumer list; **6** with no *named* consumer; **0** carrying a `terminal` field |
| 18 | exporter census + `.github/workflows/valoria-ci.yml` | 8 exporters exist, **7** run `--check` in the blocking `validators` job |
| 19 | `yaml.safe_load` over `references/module_contracts.yaml` | modules **27**, composition_roles **27**, `doc is None` **9** (naive `grep -c` gives 10), `[ASSUMPTION]` resolvers **11 by grep, 0 by parse** — both CLAUDE.md corrections confirmed |
| 20 | `grep -rl` per key type over non-test Python | **36 of 55** types appear in no non-test module (24 in no `.py` at all, 12 only in tests) |
| 21 | exact σ derivation for both die models | no-botch die: μ=0.5, var=0.45, **σ=0.670820**; engine die: μ=0.4, var=0.64, **σ=0.800000** — both exact for their own model |
| 22 | script over all 18 suite documents for sibling-file references | **5 broken**, all in `02_ONTOLOGY.md` |
| 23 | script over `TRACE_REGISTER.md`: 56 distinct `path:line` citations | **0** point at a missing file; **0** point past EOF; a 247-row symbol-at-line spot check found **1** genuine off-by-one |
| 24 | `python3 -m pytest tests/valoria -q` | **2 failed, 1776 passed, 23 skipped, 15 xfailed** in 6m10s. Both failures are `tests/valoria/test_forked_status.py` (`test_the_fork_rows_name_a_real_ref`, `test_the_evacuated_content_is_actually_at_the_ref`) and are **pre-existing and environmental**: `git cat-file -e c451bcb^{commit}` fails in this clone, so the fork ref the ledger names is not fetched here. I reproduced both failures in a clean worktree at `origin/main` (`ca77f21`), which predates this suite entirely. **Not attributable to the suite, and not a finding.** |
| 25 | `git diff --stat f59fd0e HEAD -- engine systems tools` | **empty** — no executable code has changed between the trace register's stated HEAD and mine, so every measurement above is directly comparable to the register's |

**Not run:** nothing in Godot (no engine binary, and the port repository is not in this checkout). Every
`[engine]` verdict in §3 is my own knowledge of published Godot behaviour, and §7 says so.

---

## 1 · CORRECTNESS — findings, most severe first

### 1.1 · MAJOR — `13_EXECUTION.md` §4.1: the "correction to step 1" is itself wrong, on all three of its claims

**What it says.** *"`mechanical.accounting` HAS a declared consumer… **`mechanical.season_change` HAS
NONE.** It is one of exactly **two** declared-emitted types with no declared consumer… The contract
row currently **declares it non-terminal**, so the honest close is a contract edit."*

**What is true**, from `json.load` over `engine/engine_params/key_types.json`:

- `mechanical.season_change` **has** a declared consumer: `consuming_systems: ['all subscribing systems']`.
  It is a **wildcard**, not an absence.
- The set of declared-emitted types with an **empty** consumer list is **five**, and `season_change`
  is not in it: `mechanical.settlement_captured`, `mechanical.era_transition`,
  `mechanical.second_calamity`, `mechanical.theocracy_unification_declared`, `state.settlement_revolt`.
  Excluding wildcards instead gives **six**, which does include `season_change`. Never two.
- **No type in the registry carries a `terminal` field at all** — 0 of 55. The row does not "declare it
  non-terminal"; it declares nothing.

**Ground.** `python3 -c "import json; …"` over the cooked registry, printed above; corroborated by
`tools/m1_acceptance.py --summary`, whose row 3 reports *"0 declared terminal"* and whose "2 unconsumed"
is a **runtime** figure over the 47 keys a 1-season probe emitted — a different measurement entirely,
which is where the "two" appears to have come from.

**Why it matters.** This paragraph is the suite's instruction for **step 1**, the one step it says is
the shortest path out of being prose. An implementer following it looks for a `terminal` field that no
type has, and closes one type when five others carry the same defect.

**Refutation attempted:** I re-read the paragraph for a scope qualifier ("at runtime", "by name") and
there is none; and I checked whether `env.crisis` — m1_acceptance's other unconsumed key — has an empty
consumer list. It does not (`['all']`). So the "two" cannot be recovered as a static registry fact.

**Smallest fix.** Replace the bullet with: *"`mechanical.season_change` has only a WILDCARD consumer
(`all subscribing systems`) and no named module. Five declared-emitted types have an empty consumer
list. No type in the registry declares `terminal` at all, so the contract close is an addition, not a
flip — and it is owed to six rows, not one."*

### 1.2 · MAJOR — `TRACE_REGISTER.md` §6.2: "only 5 roles are resolved during a default campaign" is 12

**What it says.** *"**Only 5 roles are resolved during a default campaign:** `season_driver`,
`accounting`, `faction_action`, `world_gen_settlements`, plus the contest builder/resolver pair."*
(The sentence says five and then names six.)

**What is true.** Instrumenting `engine.substrate.composition.require` through `run_campaign(seed=42)`
with default params, **12 roles resolve**:

```
accounting · contest_side.a · contest_side.b · faction_action · parliamentary_motion ·
parliamentary_vote · parliamentary_vote_declaration · scene_builder.contest ·
scene_resolver.contest · season_driver · territory_transfer_candidate · world_gen_settlements
```

**Ground.** Monkeypatched `composition.require` before importing `mc_v18`, ran a default campaign,
collected the role strings. This is a **lower bound**: a caller doing `from …composition import require`
would bypass the spy. I checked — `grep` over `engine/` and `systems/` shows **every** caller uses
`from engine.substrate import composition` then `composition.require(…)`, so the spy sees all of them
and 12 is exact.

**Why it matters.** The register's own method note says *"Reachability claims come from an executed
probe, not from reading imports."* This one was not probed; it was inferred, and it misses the entire
parliamentary cluster plus `territory_transfer_candidate`. The trace register is the suite's lookup
table, and this is the row a later reader would use to decide which roles are dead.

**Refutation attempted:** I checked whether the parliamentary roles resolve only under a flag. They do
not — the run used `run_campaign(seed=42)` with no params at all.

**Smallest fix.** Replace with the twelve, and note the fifteen that do not resolve (the ten
`snapshot_state.*`, `parliamentary_transfer`'s proposal half, `scene_resolver.combat`,
`scene_resolver.fieldwork`, `scene_resolver.investigation`, `rs_track_delta`).

### 1.3 · MAJOR — `TRACE_REGISTER.md` §4.1 / `13` §1 fact 6: "nine of the fourteen registries stay empty" is eleven of thirteen

**What it says.** *"**MEASURED after `run_campaign(seed=42)`:** `settlements` = 37; `beliefs` = 0;
`knots` = 0; `convictions` = 0; `practitioners` = 0; `treaties` = 0; `npcs` = 0; `insurgencies` = 0.
**Nine of the fourteen registries stay empty for the whole campaign.**"* `13_EXECUTION.md` §1 fact 6
repeats "9 of 14".

**What is true.** The register's own field table at `:274–301` lists **thirteen** dict registries (the
other two post-migration fields, `npc_counter` and `knot_id_counter`, are ints). Measured on the live
`World` after a seed-42 campaign:

- **empty (11):** `practitioners`, `insurgencies`, `uncontrolled_streaks`, `npcs`, `treaties`,
  `convictions`, `beliefs`, `knots`, `territory_infrastructure`, `npc_drift_state`, `threadcut_beings`
- **non-empty (2):** `comovement_deck` (2 keys, both holding **empty** lists), `settlements` (37)

So **11 of 13** by `len()`, and **12 of 13** if `comovement_deck`'s two empty lists are read for content.

**Three separate errors in one sentence:** the denominator does not match the register's own table, the
numerator does not match its own list (which names seven), and the direction of the error understates
the finding the suite is making.

**Ground.** Captured the live `World` by spying `game_state.serialize_world`, then measured each field.

**Refutation attempted:** I checked whether "fourteen" could include the two int counters — that gives
15, not 14 — or exclude `settlements` — that gives 12. No reading yields 14.

**Smallest fix.** *"Eleven of the thirteen post-migration registries are empty; twelve if
`comovement_deck`'s two empty lists are read for content. Only `settlements` (37) is populated."*

### 1.4 · MINOR–MAJOR — `11_PARAMS.md` §3 and `00_INDEX.md`: "twelve of twenty-five are assumption-grade" is eleven

**What it says.** *"Of twenty-five rows: nine are already owned, four are ruled and owed a row, and
**TWELVE** are assumption-grade."* `00_INDEX.md` repeats *"Twelve of twenty-five parameter rows are
assumption-grade, and the ledger says so."*

**What is true.** Parsing the §3 table rows: ASSUMPTION appears on rows **11, 12, 13, 14, 15, 17, 18,
20, 22, 24, 25 — eleven**. Row 23 (the contest depth cap) is graded **`NO DEFAULT, EVER`** with owner
`caller-supplied`, which is a fourth grade, not an assumption. 9 + 4 + 11 + 1 = 25.

**Why it matters, beyond one digit.** Twelve is `25 − 9 − 4` — the number was derived by subtraction
rather than by counting the column, which is the exact failure mode `11` §5 diagnoses two sections
later (*"nobody re-derives a constant that is sitting in a table"*), and the row it silently absorbs is
the one the suite most insists must never acquire a value.

**Refutation attempted:** I re-read row 23 for an ASSUMPTION tag. There is none, and `§2` row 9 gives
the same posture the same non-assumption grade (`REQUIRED, NO DEFAULT`).

**Smallest fix.** *"nine are already owned, four are ruled and owed a row, **eleven** are
assumption-grade, and one — the contest depth cap — is required-with-no-default."*

### 1.5 · MINOR — `03_OWNERSHIP.md` §2: "a **territory's** turmoil" is a peninsula clock, and the true fact is stronger

**What it says.** *"a territory's turmoil — written at exactly one site, read at exactly one site,
connecting nothing"*, offered as one of three *"live instances, each found by measurement rather than
by reading."*

**What is true.** `Territory` (`engine/autoload/game_state.py:234–252`) has no `turmoil` field, and an
AST scan finds **zero** reads or writes of any `.turmoil` attribute anywhere in Python. The real object
is `World.clocks['Turmoil']` — a **peninsula-scale clock**, initialised to `0.0` at
`engine/autoload/game_state.py:338` and read at exactly one site,
`engine/autoload/victory.py:73` (`ps = world.clocks.get('Turmoil', 0.0)`).

**The mis-scoping is inherited, not invented.** `references/descriptor_registry.yaml:192` declares
`{key: prov.turmoil, … scope: territory}` — the registry labels a `World.clocks` entry
territory-scoped, and the suite followed the registry.

**And the corrected fact is a better example than the one given.** `Turmoil` is *never written after
initialisation*, so `ps_ok = (0.0 <= PS_MAX)` at `victory.py:74` is permanently true and the
Political-Stability term of the victory condition is inert — dead state inside a win check, which is a
sharper instance of §2's own argument than "written once, read once".

**Refutation attempted:** I searched `.py`, `.yaml` and `.json` for every occurrence of `turmoil`
before concluding, and read `victory.py:55–95` in full rather than ruling from the grep line.

**Smallest fix.** *"the peninsula's `Turmoil` clock — initialised once at `game_state.py:338`, never
written again, and read at exactly one site (`victory.py:73`), where it makes a victory condition's
stability term unconditionally true."*

### 1.6 · MINOR — `13_EXECUTION.md` §3: two stale-oracle assertions are three, and "twelve lines below" is 287

- *"**Two** test files assert that no large-N balance oracle exists."* — **three** do:
  `engine/tests/test_f7_smoke_oracle.py:266`, `engine/tests/test_mc_v18_regression.py:97`,
  `engine/tests/test_parliamentary_bridge.py:96`, all carrying the same sentence
  (*"an n>=100 oracle that still does not exist"*). The register's C12 also says two.
- *"A golden test's docstring states win-shares that contradict the constant **twelve lines below
  it**."* — the docstring is `test_f7_smoke_oracle.py:16` and the live
  `GOLDEN_WIN_SHARE = {'Crown': 12.5, 'Church': 0.0, 'Hafenmark': 12.5, 'Varfell': 75.0}` is at `:303`.
  **287 lines**, not twelve. The contradiction is real and `TRACE_REGISTER.md` C8 states it correctly
  with both line numbers; only `13`'s paraphrase invented the proximity.

**Smallest fix.** "three test files"; and delete "twelve lines below it" or replace with the two cited lines.

### 1.7 · MINOR — `06_EMERGENT_NARRATIVE.md` §8: "Eighteen rows" over a nineteen-row table

The table carries rows numbered `1 … 17, 19, 18` — nineteen rows, with the last two transposed. The
closing sentence reads *"Eighteen rows, and the count is not the point."* Count and renumber.

### 1.8 · MINOR — the query catalogue's residue survived its own fix

`d080535` corrected the headline to *"26 ROWS — 18 RESOLVER-SIDE (1–18) AND 8 PERSON-SIDE (19–26)"* in
`08_FUNCTION_SURFACE.md` §2.2 and to *"26 rows — 18 resolver-side and 8 person-side"* in
`02_ONTOLOGY.md` §5.2. **Both files still say, two lines later, "the 7 person-side rows are enforced by
the opposite omission"** (`08:84`, `02:611`). Verified by grep at HEAD.

### 1.9 · MINOR — an unregistered token collision: `yield`

`yield` names two different things in the suite: the **MATTER harvest function**
(`04` §3 *"`yield`, once per season, here and nowhere else"*; `05` §6 row 2; `11` §3 row 13) and an
**argument act** in the open verb vocabulary (`08` §3.2, argument family: *"`plead`, `press`, `descend`,
`produce`, `object_to_venue`, `yield`, `propose`, `counter`, `probe`"*). `02` §4.8 maintains a
five-meaning disambiguation register for `hold` precisely against this hazard and does not carry
`yield`. It is also a Python keyword, which makes the collision expensive on the oracle side.

### 1.10 · MINOR — five broken sibling-document references, three of which resolve to the wrong real document

A script over all 18 files found five, **all in `02_ONTOLOGY.md`**, and no others anywhere in the suite:

| line | reference | resolves to |
|---|---|---|
| 7 | `01_LAWS.md` | nothing — the file is `01_THROUGHLINE.md` |
| 11 | `15_PROVENANCE.md` | **`15_ADJUDICATIONS.md`** — a real, wrong document |
| 406 | `09_PYTHON_ORACLE.md` §4 | nothing — the migration sequencing is in `13_EXECUTION.md` |
| 723 | `05_FUNCTION_SURFACE.md` §4 | **`05_WORLD_CHURN.md` §4** — the actorless event channel, not the commitment/exposure formulas, which are in `07` §3.1 |
| 1152 | `08_GODOT_4_6.md` §2 | **`08_FUNCTION_SURFACE.md` §2** — the Query catalogue, not the port's project layout |

The three that resolve are the dangerous ones: a reader chasing `05_FUNCTION_SURFACE.md §4` for the
`need()` formulas lands on an event-row schema and concludes the formulas are unwritten.

---

## 2 · FIDELITY — misquotes, smuggled departures, inherited errors

### 2.1 · MAJOR — the `0.671` correction is **mislabelled**, and applying it as prescribed would corrupt its sources

This is the suite's most-repeated finding — carried in `01` §4, `02` §2.3, `08` §5, `11` §2 row 4 and
§5, `15` §2 row 7 and `16` §2 row 1 — and described as *"the same **arithmetic error** in a binding
table"* found by two independent lanes, *"wrong wherever it is quoted"*, and to be *"corrected at
adoption rather than propagated again."*

**It is not an arithmetic error.** `proposals/2026-08-29-valoria-from-scratch/10_resolution_surface.md`
declares its **own die** and derives σ from it:

- `:17` — *"A die showing 1–6 scores nothing. A die showing 7, 8 or 9 scores one success. A die showing
  10 scores two successes."*
- `:19` — *"Per-die: P(0) = 0.6, P(1) = 0.3, P(2) = 0.1. Mean = 0.5 successes/die, variance = 0.45,
  σ ≈ 0.671."*
- `:160` — *"**The arithmetic, derived fresh for this die, and this document owns the constant.** …
  **0.671 is the constant for this die**; docs 09 and 12 price flat shifts against it and cite here
  rather than deriving their own."*

I computed both models exactly: the no-botch die gives var 0.45, **σ = 0.670820**; the executing die
(face 1 = −1) gives var 0.64, **σ = 0.800000**. **Both are correct for their own model.** Every corpus
citation I opened — `07_alignment.md:580`, `09_churning_world.md:430`,
`12_coercion_and_force.md:240`, `11_code_shape.md:218`, `CODESHAPE_FORBIDDEN.md:16` — says *"doc 10 §6's
constant **for this die**"* and cites the owner rather than asserting an engine measurement.

**So the finding is a MODEL DIVERGENCE, not an arithmetic error**, and three consequences follow that
the suite does not draw:

1. **"Wrong wherever it is quoted" is false.** In every document that uses the no-botch die, 0.671 is
   right, and replacing it with 0.800 would make that document internally inconsistent.
2. **The prescribed fix is unsafe.** `16` §2 row 1 records *"corrected to `0.800` in three documents"*.
   If those documents keep μ = 0.5 and the Pool/σ table at `10_resolution_surface.md:37`, changing only
   σ breaks the pair. σ and μ come from one die; you change the die or you change nothing.
3. **The "two independent lanes" convergence is weaker than advertised.** Both lanes found the same
   *difference between two models*, which one comparison establishes. It is not two derivations of an
   error.

**Refutation attempted, and it failed.** I looked for any place the corpus claims 0.671 describes the
*executing engine's* die. There is none — the whole suite is "Valoria from scratch" and doc 10 says it
is deriving fresh for its own die. So the mislabelling stands.

**Smallest fix.** In all seven places: replace *"an arithmetic error"* / *"wrong wherever it is quoted"*
with *"the design line specifies a **different die** — no botch face, μ = 0.5, σ ≈ 0.671 — and the
executing owner's die has a botch face, μ = 0.40, σ = 0.800. Both constants are correct for their own
die. This shape adopts the executing die, so **every derived statistic changes together**, and a
document that keeps the design-line die keeps 0.671."*

### 2.2 · MAJOR — and the die swap itself is a **smuggled departure**

Following from §2.1: `02` §8.2, `08` §5 and `11` §2 rows 1–3 adopt the executing die
(`1 = −1 · 2–6 = 0 · 7–9 = +1 · 10 = +2`, μ = 0.40) as settled fact. **The design line this suite
reconciles specifies a different die**, and the suite never declares that as a departure or prices it —
it presents the whole divergence as a wrong constant.

**What the departure costs, unpriced:**

| | design-line die | executing die |
|---|---|---|
| μ per die | 0.50 | 0.40 (−20%) |
| σ per die | 0.671 | 0.800 (+19%) |
| can a pool roll **negative**? | **no** | **yes** — a 1D pool nets −1 with p = 0.1 |

That last row is a mechanical change, not a calibration one. The Failure band (`margin < 0`) is
reachable at small pools under one die and much less so under the other; `OB_MIN = 1` means very
differently-shaped things in each; and `proposals/2026-08-31-ideal/11_challenges_round1.md:123`
computes underdog and disaster probabilities *from* σ ≈ 0.671 — numbers that are simply void under the
adopted die and that nothing in the suite retracts.

`01` §0 sets the standard the suite fails here: *"Where the ideal shape departs from what the tree does,
**the departure is stated as a departure with its cost priced**."* The rule cuts both ways and this is a
departure from the **design line**, arriving disguised as a correction to it.

**Smallest fix.** One row in `15` §2 and a paragraph in `11` §2: *"RULED — this shape adopts the
executing die, including the botch face. That is a departure from the design line's die, and it
changes μ, σ, and whether a small pool can net below zero. Every statistic the design line derived from
its own die is void under this ruling and must be re-derived, not edited."*

### 2.3 · MAJOR — `06_EMERGENT_NARRATIVE.md` §6 makes the exact conflation its own source forbids by name

**What the suite says.** §6 is headed *"**The ten LOST arcs are one loss, ten times.**"* It then gives
the threshold framing (*"the design cannot resolve an arc whose premise is that nobody wants it
resolved"*) and the numbers *"thirteen"* survive at a scheduled sitting and *"three"* lose their ending
at a counter. `05` §5.2 repeats the 13/3 pair.

**What the sources say.**

- The 13 and the 3 are **lane 1's closure axis over arcs 1–18 only**
  (`proposals/2026-08-30-arc-reachability/01_arcs_01_18.md:32–33`;
  `04_SYNTHESIS.md:85–88`), and lane 1 recorded exactly **one** LOST arc in that band. The closure axis
  and the story axis are **orthogonal** in the source — `04_SYNTHESIS.md:83` introduces it as *"a
  closure axis the story axis was hiding"*.
- Lane 3's seven LOST arcs — the majority of the ten — are explicitly **not** a threshold loss.
  `03_arcs_41_55_and_emergent.md:31–35`: *"**The seven LOST arcs share one blocker, and it is not
  thresholds.** All seven … die on either a world-substrate quantity the new design does not have
  (five) or an actor the new design cannot instantiate (two). Neither is a threshold problem. **§5
  separates the two claims, because the corpus has been conflating them.**"*
- And §5 closes: *"**Does the refusal of thresholds cost stories? In this band, no.** … The corpus has
  been conflating these. They should be reported as **two independent findings**: *the threshold
  refusal costs nothing here*, and *the missing world quantity costs seven arcs*."*

**So the suite performs, verbatim, the conflation a source lane names and forbids** — and it does so
while, three documents away, **closing** the world-substrate hole that five of those seven arcs die on
(`05` §3, `15` R-15). The two claims cannot both stand: if the `Site`-kind closure works, at most five
of the ten LOST remain, and they are not "one loss".

**Refutation attempted:** I checked whether the suite scopes the 13/3 anywhere ("in one band", "lane 1").
It does not, in either `05` §5.2 or `06` §6. And I checked whether the suite anywhere reconciles the
world-substrate closure against the LOST count. It does not.

**Why it matters.** §6 is where the suite prices what Law 1 costs. Priced at "ten arcs" it looks like
the single largest concession in the design; priced honestly it is **three closure-losses in an
eighteen-arc band, with the other seven belonging to two blockers the suite closes or gates
separately.** Overstating a cost is not a safe error — it is the argument someone will later use to
re-admit thresholds.

**Smallest fix.** Split §6 into the two findings the source demands: *"Thresholds: in lane 1's band,
three of eighteen arcs end at a counter and lose their ending; thirteen end at a scheduled sitting and
survive. Lane 3 reports the threshold refusal costs **nothing** in its band. Separately, the ten LOST
arcs are **not** one loss: five die on the world-substrate hole this suite closes (`05` §3), two on the
off-board-actor gate (`05` §4.4), one on lane 1's closure axis, and the remainder are lane 2's."*

### 2.4 · MAJOR — Momentum is re-introduced, and it was **cut as a false N-line by two independent critics** in the suite's own source

`02` §5.5.2 and `07` §6 give `Belief` a mechanical consequence: *"It grants **Momentum** for aligned
action — spendable, capped, **per-scene**"*. `15` R-11 repeats it as part of a Jordan-ruled definition.

**The source cut it, twice, and applied the cut.**

- `proposals/2026-08-29-valoria-from-scratch/16_ners_audit.md:44–46` — **"§2 The three false N-lines →
  2.1 MOMENTUM — CUT. Found independently by two critics."**
- `10_resolution_surface.md:223` — *"**Momentum — CUT, and this entry is a retraction, not a tidy-up.**
  … (i) Its N-line was false … a Conviction **is** a stance row … Convictions keep full resolver
  consequence with Momentum deleted. (ii) Its residue was `+1 die` — **a flat pool bonus, which is the
  one shape §6 of this very document refuses**. (iii) It was produced by 'scene-level detection' and
  reset 'per session' — and neither a scene nor a session exists at AUTO fidelity. That makes it a pool
  term available to a played person and unavailable to the identical person resolved headless, **a
  direct breach of §7's fidelity-invariance guarantee**."*
- `02_the_person.md:696` — *"**Momentum, in any form — CUT**"*, same three grounds.

**The suite reproduces reason (iii) as its own law and then breaks it.** `07` §2 P-A: *"the same world,
the same seed and the same choices produce the same outcome **at every fidelity**"*; P-C: *"switching
fidelity mid-campaign changes nothing about the world"*. A **per-scene** grant cannot satisfy either,
because `06` and `07` define `auto` as the fidelity in which no scene is rendered.

This is a departure from a source with a recorded, applied, twice-independent cut, made **without
mentioning that the cut exists** — the definition of smuggled. See also §5.1, where it is the seventh
false N-line.

**Smallest fix.** Either delete the Momentum clause from `02` §5.5.2, `07` §6 and `15` R-11 (Convictions
already weight the option ranking and stance already gates salience — the possibility survives), or add
a `15` ruling that re-admits it **against** the recorded cut, defines its scope in a frame that exists
at `auto` fidelity, gives it an owner row in `03`, a class in `04` §4, and a params row in `11`.

### 2.5 · MINOR — the coverage sweep was **not** run against `main`, and the suite's own documents are in its denominator

`00_INDEX.md` and `16` §4 item 1: *"The sweep instrument, **run against current `main` this pass**,
reports **162** documents swept, 24 cited, **138** uncited."*

Executed, three ways:

| tree | swept | cited | uncited |
|---|---|---|---|
| `origin/main` = `ca77f21` | **153** | 24 | **129** |
| local `main` = `f59fd0e` (sweep.py copied in — it does not exist at that ref) | **150** | 24 | **126** |
| HEAD `d080535`, suite present | **163** | 24 | **139** |

162/138 is reachable only with the suite's own in-progress documents in the tree — ten of its eighteen
files are over the 200-line threshold, and 153 + 9 = 162. So the figure counts **nine of this suite's
own documents among the 138 uncited**, and the phrase "against current `main`" is false.

`16` §4 item 2 already concedes that the coverage figure is *"a measurement that changed what it
measured"* — but attributes the change to documents being revised to cite what the sweep found. **The
actual mechanism is that the measuring document inflated its own denominator**, which is a different
and less flattering story, and the one worth recording.

**Smallest fix.** *"The sweep, run on this branch **with this suite present**, reports 163 swept, 24
cited, 139 uncited. Against `origin/main` without this suite it is 153 / 24 / 129. Nine of this suite's
own documents are in the uncited count, which is what §4 item 2 means concretely."*

### 2.6 · MINOR — an inherited half-fix: the firsthand salience floor

`16_ners_audit.md`'s 2026-08-30 extension records that the **accepted** half of ruling A-6 — a salience
floor for firsthand claims — *"is written nowhere in the design"*, and that the owning document *"still
computes the flat product `recency × confidence_live × relevance × stanceweight` with the 0.05 clamp
and no `max`."*

The suite carries the defect forward: `02` §5.4 ships exactly that flat product with exactly that clamp
and **no floor term**, while `02` §10 item 7 lists only *"the **testimony** half of the salience
floor"* as open and asserts *"A firsthand claim gets a floor"* as settled. A reader implementing §5.4
gets no floor for either.

**Smallest fix.** Add the `max(floor, …)` term to §5.4's formula, or change §10 item 7 to *"the salience
floor, both halves — the firsthand half is ruled and **is not in §5.4's formula**; the testimony half is
undecided."*

### 2.7 · MINOR — "eight merged pull requests"

`00_INDEX.md`: *"reconciled from **eight** merged pull requests, fourteen trace logs, five prior
adjudications and the executing tree."* Eight is #337–#344, inherited from
`proposals/2026-08-31-authoritative-architecture/00_INDEX.md`. But `16` §2 rows 10–12 take three
substantive overturns from **#349**, and the branch this suite sits on descends from `ca77f21` (#349).
Say "#337–#344 plus #349", or nine.

---

## 3 · GODOT — every `[engine]` claim, its verdict, and the 4.6 test

I could not open Godot. Every verdict below is my own knowledge of published engine behaviour, which is
the same epistemic class the document itself claims (`10`'s header: *"`[engine]` marks a claim about
**published engine behaviour**"*).

| # | claim | where | verdict |
|---|---|---|---|
| 1 | typed `Dictionary[K,V]` since **4.4** | `10` §1.1 r1 | **correct** |
| 2 | `@abstract` since **4.5** | `10` §1.1 r2 | **correct** |
| 3 | `WorkerThreadPool.add_group_task` since **4.0** | `10` §1.1 r3 | **correct** |
| 4 | GDScript has no module system, no visibility modifiers, no way to scope an identifier out of a function body | `01` Law 2, `10` §3, `15` R-9 | **correct**. `_`-prefixing is convention only; `load()`/`preload()` by string and `class_name` statics are reachable from any script |
| 5 | IEEE float addition is not associative; a band gate on a summed value makes the difference observable | `04` §5, `10` §4, `15` R-8 | **correct**, and the reasoning is sound |
| 6 | Python floors toward −∞; **GDScript integer division truncates toward zero**, so a naive port diverges on negative deltas | `10` §4 | **correct**, and it is the sharpest engine observation in the document. `%` differs too (GDScript keeps the dividend's sign; Python keeps the divisor's) — worth adding, since `wear` is the negative-delta case |
| 7 | `Vector2` components are **32-bit floats in a standard build**; a Python double round-tripping breaks parity at the last bits; integers below 2²⁴ are exact | `10` §5.1 | **correct**, and correctly hedged — `real_t` is 64-bit only in a `precision=double` build |
| 8 | a built-in value type has no reference-bearing fields, so `Vector2` cannot be widened | `10` §5.1 | **correct** |
| 9 | `load()` returns the **cached** instance; never use `Resource` for a carrier | `10` §5, §11 | **correct** — `ResourceLoader` default `CACHE_MODE_REUSE` |
| 10 | `.tres` carries a script path and is an **execution surface**; wrong for a save file | `10` §8 | **correct**, and it is the right caution |
| 11 | the `class_name` namespace is **flat and global**; no `Settlement.Person` | `10` §5.2 | **correct** |
| 12 | GDScript ints are **signed 64-bit**; `<<` on a high bit yields a negative; the RNG seed is unsigned-backed; never `abs()` a negative seed | `02` §6, `10` §7 | **correct**. `abs()` halves the reachable seed space and overflows at `INT64_MIN` |
| 13 | JSON loses integer precision above **2⁵³**; ids cross as strings | `02` §6, `10` §7, §9 | **correct** — Godot's JSON parser yields doubles for numbers |
| 14 | **no cycle collector**; `RefCounted` cycles leak permanently; ids break the cycles | `02` §6, `10` §11 | **correct**, and the design argument (`succeed ∘ contain` is cyclic in the *normal* case) is the strongest single justification in the port document |
| 15 | union types have no GDScript representation; `(kind_tag, id)` | `10` §5.2 | **correct** |
| 16 | **`Container` is a Godot built-in, the `Control`-derived base of `VBoxContainer`**, so `class_name Container` *"collides **and shadows a UI type silently**, where `Node` would have failed loudly at once"* | `02` §2.2.1 | ⚠ **WRONG ON THE MECHANISM — see G-1** |
| 17 | `address.gd` **not** `path.gd` — *"Path2D/Path3D exist"* | `10` §5 | ⚠ **overstated — see G-2** |
| 18 | exceeding recursion depth is **a CRASH, not a catchable error** | `09` §4, `08` §6, `11` §6 | ⚠ **half right — see G-3** |

### G-1 · MAJOR (mechanism) — `02` §2.2.1: there is no silent-shadowing path

GDScript's analyzer rejects a `class_name` that shadows a native class, **and it does so identically for
every native class**. `class_name Container` and `class_name Node` both produce a parse-time error of
the *"hides a built-in/native class"* form; neither compiles, and neither shadows anything. The claim
that `Container` would collide *silently* while `Node` would fail *loudly at once* describes a
distinction the engine does not make.

The **conclusion survives** — `Container` is a real native class and is a bad name — but the *reason
given* is the whole content of the amendment (*"the second refusal corrects an earlier choice that
landed on a worse collision"*), and it is not a real hazard. Second, minor: `Container` is
`VBoxContainer`'s **transitive** base (`VBoxContainer → BoxContainer → Container → Control`), not "the
base".

**Smallest fix.** *"[engine] `Container` is a native Godot class (`Control → Container → BoxContainer →
VBoxContainer`), so `class_name Container` is a parse-time error — exactly as `class_name Node` would
be. Both names are simply unavailable, which is the reason to use `Rung`."*

### G-2 · MINOR — `10` §5: a file name never enters the `class_name` namespace, and `Path` is free in Godot 4

Two things: (a) `path.gd` as a *file name* collides with nothing — only `class_name` identifiers occupy
the global namespace; (b) the bare identifier **`Path` does not exist in Godot 4** — Godot 3's `Path`
was renamed `Path3D`, so `class_name Path` is actually legal. The advice to call it `address.gd` is
still good (it matches `address(person)` in `08` row 23), but the stated engine reason is not one.

### G-3 · MINOR (overstated) — `09` §4: "a CRASH, not a catchable error"

**Not catchable is right** — GDScript has no exceptions at all, so nothing about a depth breach can be
caught, and the design conclusion (a required cap plus a typed error result) is correct and should not
be softened. But **"crash" overstates the debug case**: exceeding `debug/settings/gdscript/max_call_stack`
produces a reported *"Stack overflow"* error and aborts the script, not necessarily the process. Say
*"an unrecoverable script-level error you cannot catch"* and the argument is unchanged and exactly true.

### The 4.6 test — **the suite's claim survives, and I tried hard to break it**

I went through every construct the suite names and asked whether any needs 4.6:

- typed `Dictionary` → **4.4**; `@abstract` → **4.5**; `WorkerThreadPool.add_group_task` → **4.0**;
  `PackedInt64Array` / `PackedInt32Array` → 4.0; `clampi` → 4.0; `Vector2` / `RefCounted` /
  `class_name` / `.tres` / `FileAccess.store_64` / `JSON` semantics → all 4.0-era;
  `ResourceLoader` cache modes → 4.0.
- I looked for a 4.6-only construct anywhere in the suite (`10` §§2–11, `02` §6, `09` §4). **There is
  none.** `10` §1.1 row 5 asserts this and it holds.

So **"nothing here needs 4.6" is correct**, and re-labelling the fork as **4.3 versus ≥4.5** is the right
move. Two refinements I would make:

1. The honest floor is arguably **≥4.4, not ≥4.5**. `@abstract` is graded *"yes, weakly"* by the suite
   itself, and its own fallback (`push_error` + a typed error result) is *"needed anyway, since
   GDScript has no exceptions"*. So the only genuinely load-bearing gate is typed `Dictionary` at 4.4.
   The fork is best stated **4.3 versus ≥4.4, with ≥4.5 as a nice-to-have.**
2. `10` §1.2's void-baseline argument is **correct and independently confirmed**: I read
   `workplans/return_to_game_queue.yaml:70–86`, and the setting-only arm moved parse errors
   **169 → 161 with `broken_scripts` unchanged at 61**, exactly as `10` §1.2 says, refuting the
   "121 → 16 from one setting" story. And `references/ecosystem_versions.yaml` — the file
   `godot/godot_conversion_strategy_v1.md:41` cites as pinning 4.6 — **does not exist in the working
   tree and appears in no commit** (`git log --all -- "*ecosystem_versions*"` returns nothing).
   Both verified.

---

## 4 · SINGLE OWNERSHIP — the attack, and the gaps

`03_OWNERSHIP.md` §1 claims *"Four owners, one log, and Nobody. **Every value in the game is in exactly
one row.**"* and §6 offers the test *"Name any value. This table says who owns it."* I took twenty
values — from the suite, from the setting, and from running code — and tried each against the table.

| # | value | source | verdict |
|---|---|---|---|
| 1 | `wear(site_kind)` | `05` §2, `11` §3 r11 | ✗ **owner is "params"**, which is not a row |
| 2 | `COND_SCALE` | `10` §4, `11` §3 r10 | ✗ same |
| 3 | `OB_MIN`, `L`, `K`, `B`, the depth cap | `11` §2–3 | ✗ owners are "params", "the dice owner", "the descriptor registry", "caller-supplied" — **four owners the table does not have** |
| 4 | `Momentum` | `02` §5.5.2, `07` §6 | ✗ **no owner anywhere** |
| 5 | `Belief.revision_pressure` | `02` §5.5.2 | ✗ Person owns `beliefs`, but the writer is **another person's social success** — a write of "anything about another person", which the Person row forbids outright |
| 6 | `ConveningCondition` | `04` §3 | ✗ **the seventh gap — see below** |
| 7 | `tick` / the season counter | `02` §6, `04` §6 | ✗ no row. It is in **every id in the game** (`H(world_seed, tick, subject_id, purpose)`) |
| 8 | `world_seed` | `04` §6 | ✗ no row |
| 9 | "holds office" | `02` §2.1 vs §4.1 | ✗ **two homes** — a `marks[]` row of kind `office` *and* a `hold` Tenure |
| 10 | "where a person lives" | `02` §2.1 | ✗ **two homes** — a `marks[]` row of kind `residence` *and* the `contain` Tenure that §2.1's own "deliberately absent" table says replaces `address` |
| 11 | `knot.strain` | `02` §4.2–4.3 vs §4.7 | ⚠ **owner cannot write it.** §4.7 says a Tenure is owned by its **subject**; §4.3 says a `tie`/`knot` is stored on the **lower id**. When those differ, the subject owns a record it does not hold |
| 12 | a "suppression scar" | `06` §8 r15 | ✗ named as a mechanism, no object, no owner, no N-line. (`state.scar_acquired` is a live registered key type) |
| 13 | `Person.weight` | `02` §2.1.2 | ⚠ Person owns it; only **CENSUS** writes it, and CENSUS is not a person acting |
| 14 | `Person.capability[a].rank` | `02` §2.1.3 | ⚠ Person owns it; no row in the `04` §4 write matrix, so every advancement is an unmarked cell |
| 15 | `convictions`, `beliefs`, `Duty` | `02` §5.5 | ⚠ Person owns them; **no rows in the write matrix at all**, and §4 says *"any unmarked cell is a write-class violation"* |
| 16 | `Site.drawers[]` | `02` §2.4 | ⚠ Site owns it; no write-matrix row |
| 17 | `Proposition` after its utterer dies | — | ✓ **named gap 1**, and ruled here |
| 18 | `Record`, `Venue`, `Dispensation` | — | ✓ **named gap 2**, and ruled here |
| 19 | `World.clocks['Turmoil']` | running code | ✗ a live world-scale value with no row (see §1.5) |
| 20 | `Faction.intel` | running code | ✓ correctly homed as a Nobody/Query casualty, and its unreachability is confirmed (`MULTS` has no `intel` key, so `adjust('intel', …)` raises before any bound is consulted — `engine/substrate/descriptors.py:30–31` says so) |

**Five of these are the six the document already names. The rest are new.**

### 4.1 · MAJOR — the table has a **sixth owner it does not list: `params`**

`11_PARAMS.md` is a twenty-five-row ledger whose owner column reads `params` (16 rows), `the dice owner`
(5), `the descriptor registry` (2), `the event substrate` (1) and `caller-supplied` (1). **Not one of
those is a row in `03` §1**, and `wear` is not a marginal case — `05` §2 calls it *"the world's entropy…
the quantity the whole political layer exists to argue about."*

Under the §6 test as written, `03` is incomplete for at least twenty-five values that the suite's own
ledger enumerates.

**Refutation attempted:** I checked whether §1's *"every value in the game"* could be read to exclude
constants. It cannot — §1's Nobody row includes `needs` and `openings`, which are equally not primary
state, and `05` §2.5 explicitly insists `wear` *"belongs in the exported parameter table where code
reads it"*, i.e. it is a value with a home.

**Smallest fix.** Add a sixth row: *"**params** — every exported constant, owned by the typed artifact
and read by code; never in prose and never in two files (`11_PARAMS.md`)."*

### 4.2 · MAJOR — the seventh gap: **`ConveningCondition` has no owner, no write class, and no N-line**

```
ConveningCondition := (id, holder, predicate, date_form, set_by, set_at)     -- 04 §3, CALENDAR
   holder in Rung | Office
```

Checked against every surface:

- **`03` §1** — the Rung row owns `matter, dates[], envelope, stake[], judging_set_rule`; the Office row
  owns `post, remit, conferral, revocation, establishment[], dates[], upkeep`. **Neither owns
  conditions.**
- **`03` §1.3** — not among the six named gaps.
- **`04` §4** — no row in the write matrix, so attaching or clearing one is an unmarked cell.
- **`14` §2** — not in the N-line table, though `14` §2 opens *"**No object enters this shape without an
  N-line.**"*
- It is not a Query (it is stored and read at CALENDAR), not matter, not a Tenure, not a Claim.

**It is load-bearing.** `04` §3 hangs the entire threat-and-pressure layer on it (*"A threat is a
published band predicate that schedules an occasion"*), and `06` §8 row 3 — **hostage politics** — is
produced by *"vacancy-by-absence as a convening condition over presence"*. A first-class object with a
six-field schema, two mechanisms depending on it, and no owner.

**Smallest fix.** One row in `03` §1 (*"a `ConveningCondition` is owned by its `holder` — the Rung or
Office whose date it schedules"*), one row in the `04` §4 matrix (CALENDAR-written at CALENDAR,
RESOLVE-written by `convene`), and one N-line in `14` §2.

### 4.3 · MAJOR — the write matrix's inconsistent row: `bodies, ageing, death`

The prompt's specific question. The row is:

```
| bodies, ageing, death | no | **yes** | no | **no (killing is an act)** | no | no |
```

The cell is self-contradicting: it marks RESOLVE **no** while its own parenthesis says killing **is an
act**, and acts resolve at RESOLVE. §4's closing rule is *"**Any unmarked cell is a write-class
violation**"* — so **every murder in the game is a write-class violation by the matrix's own rule.**

Two rows below, `carrier existence` **is** marked `yes (create/destroy)` at RESOLVE. So one row permits
what the other forbids, for the same event. And `04` §3's MATTER prose — *"Death. A named person's death
is **the one place** a Person leaves existence **without an act**"* — presupposes that other places do
it *with* one.

**Smallest fix.** `| bodies, ageing, death | no | yes (ageing, illness, natural death) | no | **yes**
(killing, wounding — an act) | no | no |`, and delete the parenthetical from the RESOLVE cell.

### 4.4 · MAJOR — a Law-4 contradiction: `(Tenure, until)` and what an Event may end

`01` Law 4 is asymmetric and explicit: `social: true ⇒ an Event may never write this row`. Now read the
matrix: `Tenure` is written at **MATTER** (*"`until` on death"* — an Event) **and** at RESOLVE. Under
Law 4 that forces `(Tenure, until)` to be **`social: false`** — "either driver".

But `05` §7 refuses, in its own table: *"an event that grants or revokes an office | offices are
social; **the Partition forbids it outright**"*.

Both cannot hold. A `hold` Tenure **is** the office relation, and `until = tick` on it **is** the
office ending. If `(Tenure, until)` is `social: false`, the Partition permits an Event to end any
tenure — a storm could vacate a praefecture, and only convention stops it. If it is `social: true`,
death cannot end a tenure and the succession mechanism (`04` §3 death rule 1; `06` §8 rows 2 and 13)
has no producer.

**Refutation attempted:** I looked for a carve-out keyed on the *event kind* (death vs. storm). The
Partition is explicitly keyed on `(record-kind, field)` and `02` §5.1's falsifier says so: *"Wrong if
any state change's driver depends on the **instance** rather than on the `(record-kind, field)` pair."*
A death-only exemption is exactly such an instance dependence, so the escape hatch is closed by the
suite's own falsifier.

**Smallest fix.** Declare the pair explicitly and narrow `05` §7: *"`(Tenure, until)` is `social:
false`, and it is the one row where that is uncomfortable. What keeps a storm from revoking a
praefecture is not the column but the event-row grammar: an actorless row's `deposits` may write
`until` **only on a `(Person, exists)` change it also caused**. That is a rule, not a column, and it is
the Partition's one declared seam."*

---

## 5 · NERS — the seventh false N-line, over-distillation, R, S-UP/S-DOWN

### 5.1 · MAJOR — **the seventh false N-line is `Momentum`**, and it has already been adjudicated as one, twice

`14` §3 lists six and `14` §7 predicts a seventh *"most likely in `Sensation`, the newest object"*. It is
not in `Sensation`. It is in `Belief`.

| | |
|---|---|
| **the object the suite KEEPS** | `Momentum` — *"granted for aligned action — spendable, capped, per-scene"* (`02` §5.5.2, `07` §6, `15` R-11) |
| **its claimed N-line** | acting on principle must have a mechanical consequence: *"Acting on principle gives you something to spend, not a better chance at things."* |
| **why the possibility survives the cut** | **the suite's own ontology already provides it, in two places.** `02` §5.5.4's DELIBERATE row: *"**Convictions weight the option ranking**; a Belief is what makes a costly option **choosable at all**."* And `02` §5.4's `stanceweight(c) = clamp(1 + λ·agreement(c), 0.05, 2.0)` already gives aligned material retrieval priority in the View. Acting on principle keeps full resolver consequence with Momentum deleted — which is **verbatim** what the source found |
| **who found it first** | `proposals/2026-08-29-valoria-from-scratch/16_ners_audit.md:44–46` — *"§2 **The three false N-lines** → 2.1 **MOMENTUM — CUT. Found independently by two critics.**"* The cut was **applied** in `10_resolution_surface.md:223` and `02_the_person.md:696` |
| **and the residue is worse than surplus** | it has **no owner** (`03`), **no write class** (`04` §4), **no params row** (`11`), and it is **per-scene** — a frame `07` §2 defines out of existence at `auto` fidelity, breaking P-A and P-C |

**This is the highest-value finding in this review**, because it is over-determined: the source cut it
as a false N-line, the cut was applied, and the suite re-adds it without argument, in violation of three
of its own structures.

**Refutation attempted, twice.** (1) Could Momentum be a *different* object from the one cut? No — the
cut object was *"the only mechanical account of how the Restoration produces outcomes… playing to your
values"*, which is the same claim `02` §5.5.2 makes. (2) Could "spendable, a choice, not a bonus" evade
reason (ii)? Partly — a spend is a choice where `+1 die` is arithmetic, and that is a real distinction.
But it does not touch reason (i), which is the N-line itself, or reason (iii), which is fidelity
invariance. Two of three grounds survive intact.

**Smallest fix.** Delete the Momentum clause from `02` §5.5.2, `07` §6 and `15` R-11 and let Convictions
carry it — the vocabulary gets shorter, which is the meta-rule. If it is kept, `15` owes a ruling that
names the recorded cut, answers grounds (i) and (iii), and supplies the three missing rows.

### 5.2 · MAJOR — the over-distillation: cutting `Gauge` left `revision_pressure` a monotone ratchet

`02` §9 cuts the `Gauge` type — *"bounded, decaying, no setter"* — on the ground that *"the decay law
survives narrowly, in claim confidence and recency."* And `05` §5 closes the door behind it:
**"EXACTLY THREE QUANTITIES ARE CLOCK-DRIVEN: matter, bodies, and the confidence of a memory. No fourth
may be added."**

But `02` §5.5.2 ships `Belief := (…, **revision_pressure**, history[])`, and §5.5.4 gives it exactly one
motion: *"a challenging outcome **adds** revision pressure; revision is an act."* Nothing removes it
except the holder's own revision act. Under §5's rule, nothing may.

**So `revision_pressure` is a monotone accumulator with no relaxation** — a quantity that ratchets on
every social defeat for the whole campaign and discharges an arbitrarily large accumulation the first
time its holder revises. That is precisely the shape `Gauge` existed to bound, and the possibility
`Gauge` carried — *a quantity that accumulates and relaxes without an act* — **does not survive its
cut**; it is required by an object the suite ships.

**And the running code agrees.** `systems/characters/sim/beliefs.py:57` declares
`revision_pressure: int = 0` and `:225` is `belief.revision_pressure += 1`. There is no decrement
anywhere in the module. The ratchet is live today, and the suite adopts it without noticing.

**Refutation attempted:** I searched the whole suite for any decay, cap, or reset on `revision_pressure`
(`grep -n "revision_pressure\|revision pressure" *.md` — four hits, none of them a relaxation), and
checked `05` §5.1's two "not events" for a fourth interior decay. There is none, and §5 forbids adding
one.

**Smallest fix.** Either (a) declare `revision_pressure` the **fourth** clock-driven quantity and amend
`05` §5 to say four, pricing the exception, or (b) make it non-monotone by construction — pressure is
*recomputed at read* from the holder's recent challenging outcomes, which needs no store, no fourth
clock, and no exception, and is what Law 3 would say if anyone asked it.

### 5.3 · MINOR — two objects enter the shape without an N-line

`14` §2 opens *"**No object enters this shape without an N-line.**"* and `01` §6 makes it test 1.
Checked against the twenty-three-row table:

- **`Dispensation`** — a six-field record with *"NINE typed terms"* (`02` §7.3), the whole of the
  down-stroke, an owner ruled in `03` §1.3 gap 2 — **and no N-line.**
- **`ConveningCondition`** — see §4.2. No N-line and no owner.

(`Duty` correctly has none — `02` §5.5.3 says it adds no record.)

### 5.4 · MINOR — a producerless dependency the suite cut a sibling for: `imminence(c.horizon.band)`

`06` §4.3 cuts `forecast_mass` because *"it has no producer anywhere in the corpus. An object with no
producer cannot have an N-line."* The reduced formula it leaves is

```
depth_score(c) = cast_score(c) × imminence(c.horizon.band)
```

**`c.horizon` has no producer either** — and worse, the candidate contract **forbids** one:
`06` §5 C-3 requires *"an emitter supplies **realized-state terms only** … **never publish the
trigger**"*, and `horizon.band` is a forecast term by construction. So the same reasoning that cut
`forecast_mass` applies to `imminence`, in the same paragraph.

**This is not a seventh false N-line** — I tried to make it one and could not. Cutting `imminence`
collapses `depth_score` into `cast_score`, and `06` §4.3 says explicitly that collapsing them *"starts
pushing futures at the player, which is the failure that turns a churning world into a story with a
plot."* So the possibility does **not** survive; the term is load-bearing. It is a different and
arguably worse defect: **a load-bearing input whose only legal producer is forbidden by the contract in
the next section.**

**Smallest fix.** Narrow C-3 to *"realized-state terms only, **plus a horizon band on a date that
already exists in the calendar**"* — a scheduled sitting's distance is a realized fact about a `Date`,
not a forecast, so the exemption costs nothing and gives `imminence` a legal producer.

### 5.5 · MAJOR — R: **a real blocker, over-scoped into an evasion**

`14` §5's verdict is *"**R IS NOT SCORABLE** … until it is answered per seat, an R verdict on this shape
would be manufactured"*, and `15` §3 escalates *"WHICH SEATS ARE PLAYABLE"* as *"the highest-value
escalation in the suite."*

**The real half.** `14` Rule 3 is sound: a dominant act at an NPC seat is characterisation, and grading
it as a defect would be the amputation error the E-ratio exists to prevent. `06` §6.2's worked case is
genuine — *"the two acts that reproduce the corpus's flagship arc are the two acts a play-space audit
filed as DOMINANCE DEFECTS"* — and that specific question ("is the crown a playable seat?") really does
need a person.

**The evasion half, and it is two things.**

1. **The suite banks three R verdicts anyway, all favourable.** `14` §5's own table records the act
   economy's petition-spray dominance defect **"closed"** by one act per person, and the floor's two
   defects **"closed"** by two subtractions — three R judgments about seats whose playability was never
   established, in the document that says an R verdict would be manufactured. Under `CLAUDE.md` §0.1
   point 4 that is the asymmetric-skepticism failure by name: an unfavourable result is withheld for
   want of a precondition that a favourable one is not held to.
2. **For the architecture, the question is already answered by the suite's own laws.** `01` §3 and `07`
   §1: the player is a Person, `played` is a fidelity flag, and `07` §7 refuses *"a player-only
   mechanism of any kind"*. Under `R-4`/every-rung, **every seat is occupiable** — that is the whole
   content of `07` §5. So under `15` §3's own five-test ordering, test 5 ("answered by what makes sense
   for the architecture") answers it: *the playable seats are the persons.* What genuinely remains is
   narrower and content-shaped: **which seats a campaign OFFERS as starting characters.**

**Verdict.** The blocker is real for `06` §6.2's single question and is over-scoped into a whole-axis
refusal. **Smallest fix:** in `14` §5 and `15` §3, replace *"which seats are playable"* with *"which
seats a campaign offers at start"*, state that architecturally every person is occupiable, and mark the
three banked closures as **provisional under the same rule they are exempted from.**

### 5.6 · MAJOR — S-UP: it breaks at the date whose convener spent his act elsewhere

**The trace.** A fisher holds a grievance (a `stance` row). He performs `petition` — `08` §3.2 lists it
political-up, available to *anyone* — creating `Petition(petitioner, proposition, respondent_venue,
backing[])`. A person with standing performs `carry(person, petition, date)`, creating a `DocketItem` on
that Date's `docket[]` (`02` §7.1). The Date fires at CALENDAR. Its convener performs `compose_agenda`,
**an act**, ranking the items *he holds a claim of* and admitting the top `capacity(date)`. An omitted
petition is a **drop** and deposits as one when its backers learn. Filtered by a named person at a rung:
**yes.** S-UP's structure holds.

**Where it breaks.** `compose_agenda` costs the convener **his one act for the season** (`02` §7.1,
`07` §4). So a convener with any other priority — and `02` §7.1 says he *"holds the cheapest real power
in the game"*, which means he always has one — simply does not compose. And **the suite has no rule for
that date.** `04` §3 covers only the *vacant* date (*"A VACANT DATE FIRES, ALLOCATES NOTHING, AND
LAPSES"*), and this date is not vacant: its convener exists and chose otherwise. Does it fire with an
unranked docket? Admit in arrival order? Lapse? Nothing says, and it is **the common case, not the edge
case.**

A second, quantitative break rides on the same economy: `carry` costs the carrier a whole act, so the
up-stroke's global throughput is **one petition per standing person per season**, against `06` §4.5's
190–200 candidates a season across 37 settlements. The suite never prices this.

**Smallest fix.** One line in `04` §3: *"a date whose convener did not `compose_agenda` fires and
admits its docket in **arrival order** up to `capacity(date)` — burial requires an act, and so does
prioritisation."* That preserves "burial is safe but never free" (`06` §8 row 8) and closes the branch.

### 5.7 · MAJOR — S-DOWN: it reaches the postless person, and breaks on the function's own return type

**The trace.** A Duke `issue`s a Dispensation (one act). It is published as a `tell`, so it **distorts
in transit** (`02` §7.3). A postless fisher eventually holds a `told_by(person, handle)` claim about the
terms. `opening_set(person, view)` is recomputed over the changed **claimed** terms and yields an
opening. Nobody authored it, and `eligible()` never consults office (`02` §2.1.3). **The mechanism
works** — S-DOWN's structure holds, and `12` T3 is a real falsifier for it.

**Where it breaks — a live contradiction in the suite.** The function at the centre of this path has
**two return types in four documents**:

| document | signature |
|---|---|
| `07` §3.2 | `opening_set : (Person, View) -> Act[]` |
| `12` T3 | asserts the result *"contains `petition`"* and *"at least one **act** from three different families"* |
| `08` row 20 | `opening_set(person, view) -> **Candidate[]**` — *"**NOT `Act[]`**: typing it as acts makes the option set an authored list rather than a computed one"* |
| `15` §2 row 13 | *"overturned: **`opening_set` returns Acts** — it returns candidates"* |

The overturn landed in `08` and `15` and **not** in `07` or `12`, so two documents ship the signature
the suite says it overturned, and the test that is S-DOWN's falsifier asserts against the wrong type.

**A second break, unpriced.** `02` §7.3 says the Dispensation *"travels by being noticed, not down a
chain of posts"* — but the only transport the suite defines **is** a chain of `tell` acts, each costing
a person their one act, with WITNESS fan-out gated on presence. For a Duke's dispensation to reach 37
settlements takes on the order of 37 person-seasons of `tell`. The five witness channels
(`06` §4.2) govern **what the slate may cast**, not how a claim propagates; there is no non-act news
transport anywhere in the shape.

**Smallest fix.** Correct `07` §3.2 and `12` T3 to `Candidate[]` and re-word T3's assertions in terms of
candidates whose `resolver_ref` spans three families; and add one row to `05` §6's churn ledger for
**news propagation** — either as an act-cost the design accepts and states, or as a channel with a
latency (`02` §10 item 9 already carries "channel latency values" as a homeless number, which is the
same gap seen from the other side).

---

## 6 · WHAT SURVIVED — what I tried to break and could not

**Everything below I attacked by running it. Each held.**

- **The whole execution-path measurement block** (`13` §1). Every one of the eight facts and three
  defects reproduced:
  - `max_seasons` is dead — `run_campaign(seed=7, max_seasons=3)` ran **50** seasons; only
    `params={'CAMPAIGN_SEASONS':3}` ran 3. `DEFAULT_PARAMS` always supplies the key, so the fallback at
    `engine/mc_v18.py:239` is never taken.
  - Four malformed cooked registry fields across two types, and **both types raise** when emitted with
    no explicit scale signature — proven by emitting them and catching
    `KeyValidationError: … non-canonical scale '['`.
  - **Exactly fifteen** modules annotate a type they never import — I got 15 `NameError` modules from a
    per-module `get_type_hints` sweep (two further raises were `staticmethod`/NamedTuple artifacts of my
    own probe, not annotation defects). `engine/autoload/npc_ai.py:33`'s
    `select_action(actor_id: str, world: GameState)` is among them and `GameState` is never imported —
    which makes `12` T1's step-zero obligation exactly right.
  - **2 of 55** key types emitted in a seeded campaign; **13** subscriptions on the scheduler and
    **none of them for an emitted type**; `world.npcs` empty; `npcs_generated = 0`; `generate_npc` has
    zero production callers.
  - **31** `.adjust(` sites, **20** on `L`, across **9** modules, with **exactly one**
    (`echo_transport.py:455`) inside a `sched.emit(key, apply=…)` callback. I counted by AST, not grep,
    and got the suite's numbers exactly.
  - Every core object of the shape is **absent** — an AST search for all twelve class names across every
    `.py` in the tree returns **zero** definitions.
  - `tools/m1_acceptance.py --summary` reports **0/7, NOT MET**, and row 4 declares itself DOC-DERIVED
    in its own output.
- **The trace register's citation integrity.** All 56 distinct `path:line` citations resolve to a file
  that exists, and **none** points past EOF. A 247-row automated spot check of "does the named symbol
  appear at the cited line" produced one genuine off-by-one
  (`game_state.py` `senator_inward_used` is at `:126`, cited in a `127–129` range) and nothing else.
  Given `16` §4 item 5's admission that prior sessions drifted 2–20 lines and fabricated one citation,
  this is a materially better artifact than its predecessors and deserves to be said.
- **The contradiction table (§10).** I re-derived C1, C3, C8, C12, C14, C15, C19, C20, C24, C25, C33,
  C34, C35 and C36 independently. All correct, including the two hardest:
  - **C25**: I ran `grep -rl` per type over `engine/`, `systems/`, `tools/`, `tests/`. **24** types
    appear in no `.py` at all and **12** only in test files — **36 in no non-test module**, exactly as
    claimed.
  - **C34**: `grep -cE '^\s+resolver:.*\[ASSUMPTION\]'` returns **11**; `yaml.safe_load` returns **0**,
    because the tag lives in a comment. Both halves of the method warning confirmed.
  - **C33**: parsed `doc is None` gives **9** (`audit, domain_actions, engine_clock, game_director,
    npc_memory, scenario_authoring, scene_slate, scene_timer, settlement_economy`) against `grep -c`'s
    10. CLAUDE.md's correction holds.
  - **C35**: `len(final_state['settlements'])` after a seed-42 campaign is **37**, so both figures in
    CLAUDE.md §6's sentence are stale, as the register says.
- **Every claim about `dice_engine.py`.** Four bands on the margin (`:279–294`); `_require_tn7` raises
  on any TN but 7 (`:182–193`); `_SIGMA_PER_DIE = 0.800` at **`:175`** — the exact line the suite cites;
  `BandExtension` can only express 3→2, because `may_overwhelm`'s return is consulted in exactly one
  branch under `not` (`:284–293`); `validate_context` refuses undeclared keys. σ = 0.800 is **exactly**
  right for the implemented face rule — I computed var = 0.8 − 0.16 = 0.64.
- **Every claim about `engine_clock.py`.** Three phases in that order (`:115–125`); `run_tick`'s
  `action_callback` is caller-supplied with the module's own stated reason (`:93–96`); the accounting
  call is raw at `:123`; `next_tick()` runs last so the emission counter spans both phases.
- **Every claim about `keys.py`.** Invariants 1–3, 5–8 **raise**; invariant 4 holds by construction;
  invariant 9 warns. Both termination caps are **required constructor arguments with no default**
  (`:476–490`) and both breaches **raise `TerminationBreach`** rather than clamping (`:531`, `:556`,
  `:561`). `next_tick()` raises on an undrained queue (`:598`), which is the mechanism `05` §4.2 cites
  for "there is no transport that lands an emission in a later season" — verified, that claim is true.
- **`engine/substrate/__init__.py:17–19`** says, in the module's own words, that observer resolution is
  *"NOT implemented … ORD-3 is a **PROPOSED, unratified** ordering rule; implementing `compute_observers()`
  before it lands would bake in hash-order nondeterminism."* The suite's precondition on WITNESS
  (`04` §3, `12` T2, `13` step 0c) is exactly this, and it is the strongest single claim in the suite.
- **"Seven exporters with blocking round-trip checks."** Eight `tools/export_*.py` exist and all eight
  accept `--check`; exactly **seven** run in the blocking `validators` job
  (`.github/workflows/valoria-ci.yml:126,127,134,137,141,146,150`); `export_sim_params.py` is not
  wired. The count is right.
- **The fractional-pool overturn** (`15` §2 row 8). `engine/autoload/sigma_leverage.py:314` is now
  `max(1.0, float(pool))` with a docstring dating the fix to 2026-08-21, while the **discrete** path at
  `:277` correctly keeps `int(round(pool))`. Fixed, and two trace logs are stale on it — as claimed.
- **The Godot version evidence.** `references/ecosystem_versions.yaml` does not exist and appears in
  **no commit** (`git log --all` returns nothing). `workplans/return_to_game_queue.yaml:76–77` records
  `setting_only: {failed_to_load: 54, parse_errors: 161, broken_scripts: 61}` against
  `stock: {54, 169, 61}` — the setting moved 169→161 and cleared zero broken scripts, refuting the
  "121→16 from a project setting" story exactly as `10` §1.2 says.
- **The play-space numbers.** `19 of 55` with a blocked core and `eleven` of them RICH reproduce
  verbatim at `proposals/2026-08-30-play-space-coverage/08_coverage_matrix.md:174` and `09_GAP_REPORT.md:22–24`.
- **The arc verdict table** (40/2/22/10/9) reproduces exactly at
  `proposals/2026-08-30-arc-reachability/04_SYNTHESIS.md:15`, as does "42 of 74".
- **The seven-phase retirement.** `proposals/2026-08-29-valoria-from-scratch/09_churning_world.md:45`
  is headed *"### 1.2 The seven phases"* and enumerates **P0 … P7 — eight**. `04` §2's *"its 'SEVEN
  PHASES' header sat over an eight-row table"* is right.
- **`02` §5.2's executable precedents.** `engine/substrate/canon_buckets.py:38` `canonical_accord` and
  `engine/substrate/descriptors.py:78` `faction_bounds` are both pure, computed-on-demand functions with
  no store. Query-shaped, as claimed.
- **The suite's honesty posture.** Every document carries HELD BACK, §0.05 and §0.2 in its header; `12`
  §6 lists six quantities as measurements owed; `16` §4 lists eight limits including *"the
  reconciliation had no independent check before the adversarial stage"*. I found **no case** where the
  suite claimed a measurement it had not made — the failures in §1 are all **derived counts**, not
  invented measurements, which is a different and much less serious defect.
- **`pytest tests/valoria`** — see the status line below.

---

## 7 · WHAT I COULD NOT CHECK

Stated plainly, because an honest gap beats a confident guess.

1. **Anything in Godot.** No engine binary, and `jordanelias/valoria-game` is not in this checkout.
   Every `[engine]` verdict in §3 — including G-1, my most confident engine finding — is my own
   knowledge of published behaviour, not an executed test. **G-1 in particular should be settled by
   someone typing `class_name Container` into a 4.x project**, which takes a minute and is worth more
   than my recollection.
2. **The compile ratchet's 84.** It is a property of the port repo and the 4.3 binary. I confirmed the
   `169 / 161 / 5-14-8` baselines in `workplans/return_to_game_queue.yaml`, but **84** appears in
   `CLAUDE.md` and the execution-order plan, not in a baseline I could reproduce here.
3. **`04` §2's "its `P7` writes were unlicensed under its own three-write-class rule"** and **"its
   WITNESS was not global"**. I verified the eight-vs-seven phase count and stopped; the other two
   claims about the retired design I did not adjudicate.
4. **Whether the four structural tests would pass.** They cannot be run — nothing they test exists. The
   suite says so and I am confirming, not contradicting.
5. **The n≥100 balance question.** `tools/balance_oracle.py` exists and works, but ~13 minutes per arm
   and nothing in this review is campaign-reachable, so both arms would be identical by construction —
   a fake control, and I did not run one. (`07` §3 of `03_OWNERSHIP.md`'s own discipline.)
6. **The "71 of 140 non-test modules" figure.** I measured **70 of 139** excluding `__init__.py`
   (80 of 169 including them) at the identical tree — `git diff f59fd0e HEAD -- engine systems` is
   empty, so the code has not moved. The suite is off by one on both numerator and denominator under
   the filter I could reconstruct; I could not determine which filter yields exactly 140, so I am
   reporting the discrepancy rather than the finding.
7. **`15` R-2's claim that "two competent sweeps reached opposite headlines".** I read both headlines in
   the reconciliation logs and they are as described, but I did not re-audit either sweep's underlying
   work to judge which was more nearly right. The ruling's *disposition* — neither survives whole — is
   consistent with everything I did check.
8. **Most of the corpus.** The sweep says 139 documents over 200 lines are uncited. I read the eighteen
   suite documents, the five arc/play-space/from-scratch sources the suite leans on hardest, the
   fourteen trace logs' manifest, and the code. **This review inherits the same scope limit `16` §4
   item 1 declares**, and any "there is no X" I have stated carries it.

---

> **CLOSING.** The architecture is not what broke. Four laws, four carriers, one edge, one state change,
> the by-omission signatures, the Partition-as-schema-column, fixed point, and ids-not-pointers all
> survived everything I could run at them, and the trace register is the most trustworthy artifact this
> line has produced. What broke is narrower and very consistent: **six derived counts computed by
> subtraction or from memory instead of by re-counting** (§1.1–1.4, 1.6, 1.7), **one flagship finding
> mislabelled in a way that makes its own prescribed fix unsafe** (§2.1–2.2), **one conflation the
> source lane names and forbids** (§2.3), and **one object re-admitted that two independent critics had
> already cut** (§2.4 / §5.1). None is fatal. All are cheap to fix, and every one of them is an instance
> of the discipline the suite itself teaches, applied everywhere except to the document doing the
> teaching.
