# THE NINE R-ROWS — EXECUTION PLAN, UNIT BY UNIT (PART 2)

## Status: **PROPOSED. REFERENCE under `CLAUDE.md` §0.05 — delete this file and the game behaves identically.** Nothing here may be cited as the reason a behaviour is correct. The mechanisms it names live in `engine/season/`'s registries, in the code, and in `engine/season/tests`. Merging it ratifies no design call; the calls it *records* were closed by the tests named in §11, not by this document.
## Lane: IN. Written 2026-09-09.

> **Navigation — this is part 2 of a two-file split** (`CLAUDE.md` §4: sequential parts, not
> index+infill). **Part 1** (`workplans/2026-09-09-r-execution-plan.md`) carries the front matter,
> **§1–§6**, plus **§11.0** and **§14** (relocated — see part 1's navigation block for why).
> **This file (part 2)** carries **§7–§10**, **§11** (preamble + §11.1 — §11.0 is in part 1),
> **§12**, **§13**, and **§15**. The break falls at the **§6/§7 boundary**; a short pointer stands
> in wherever a relocated section would otherwise sit.

---

## §7 · WHERE R-09's ROLL GOES

**Owner: `engine/season/seam/wrappers/sigma.py`.** ⚠ **RENAMED 2026-09-10** — this read
`seam/dice_seam.py`; U1 corrects it to a `wrappers/` path, and two live contradictory owners in one
document is worse than either spelling. Layer-1 `seam/wrappers/*` — `04 §A.2:164`, whose row
reads: `| seam/wrappers/* | **nothing, ever** | the projection | a `Margin` | **none** |`. It has no
token and writes nothing; it returns the subsystem's own result, which `degree_of` (moving to `seam/` at
step 8) grades through **the one ladder** — `shape.py:4050-4061`, `label[degree_from_net(result["net"],
result["ob"])]`.

⚠ **ONE HALF OF THAT ROW IS FOLLOWED IN CONTRACT AND NOT IN TYPE, AND THIS PLAN SAYS SO RATHER THAN
CLAIMING CONFORMANCE IT DOES NOT HAVE.** `04 §C.5:683` types the return *"a **MARGIN**. Never a
winner"*, and the crossings table (`04:692`) makes that **a type assertion**. `dice_seam.resolve`
returns a **dict**, as `combat_seam.resolve` does today and as `degree_of` grades (`{"net", "ob"}`).
What is honoured is the contract — **no winner, no band, a margin pair the one ladder reads** — and
what is deviated from is the type. A typed `Margin` for one provider and a dict for the other would
give the seam two return shapes, which is worse than either; typing both is its own `seam/` item
(§10), not a thing to smuggle in here. **Named deviation, with its reason, so a later reader does not
find it and conclude Layer 1 was ignored.**

⚠ **AMENDED 2026-09-10 (ED-SC-0037).** What it wraps is `engine/autoload/sigma_leverage.py::roll_net`
**plus `::net_boost`** — the σ layer, composed as `systems/social_contest/sim/contest/resolver.py:302`
composes it. `roll_net` **alone** is a back-compat shim over `roll_pool` that drops `roll_pool`'s `ob`
argument, i.e. the bare pool roll ED-SC-0037 costed. The paragraph below describes the underlying die
rule and stays true of it; when this section was written the wrapped subsystem was
`engine/autoload/dice_engine.py::roll_pool`
(**`:196-206`** — §2.10), whose die rule is the tree's only one (`_die_result`, `:153-161`, *"1 = -1
success, 2-6 = 0, 7-9 = +1 success, 10 = +2 successes. No chain."*, cited to `params/core.md §Die Rule,
PP-246`) and which refuses any TN but 7 via `_require_tn7`. ⚠ **`roll_pool` is not the file's only
net-producer** — `continuous_engine_sample` (`:209-223`) samples a fractional net from
`Normal(μ·N, σ·√N)`, the Godot-canonical continuous mode, and is the second. **Calling the discrete
one is a CHOICE**: the corpus is integer-pooled and `degree_from_net` reads either, so the choice is
reversible behind an unchanged seam. Stated because *"the tree's only one"* is true of the **die
rule** and false of the **net**, and a reader running the grep would find the second. The shape
precedent is `combat_seam.py`: derive exactly what the actor genuinely has, return a typed gap rather
than fabricate.

### Why this is not the second resolver `T-k` refuses, and not the "generic roll" the roster refuses

`rosters.yaml:517` opens the `contest_subsystems` note with *"⚠ A CONTEST IS A DISPATCH, NOT A GENERIC
ROLL."* Two answers below — ⚠ **and they answer only ONE of the two things that note says.** The
note's own continuation is about **calling the owning subsystem**: *"the three subsystems it should be
calling ARE BUILT … So the seam was not missing a ladder; it was failing to dispatch"* (`:515-520`),
and `:532-533` carries Jordan verbatim on these very prizes — *"we don't NEED to worry about them at
this point in time."* **A bare pool-vs-fixture roll standing in for a social contest is the generic
roll that note refuses, whatever the dispatch mechanism around it.** The answers below dispose of the
`if`-routing half and of the second-ladder half; they do **not** dispose of that half, and §11.0 is
where it goes.

1. **The provider returns `net`/`ob`, NEVER a band.** The band is read by `degree_of` calling
   `degree_from_net`, and that identity is already pinned:
   `test_we_the_ladder_is_the_trees_own_and_not_a_copy_of_it` (`:7798`) asserts
   `lad[0] is degree_from_net and lad[1] is DEGREE_LABEL` and then **replaces `S._LADDER` and requires
   every band to move with it**. A wrapper producing no band string also cannot trip
   `tests/valoria/test_degree_ladder_single_owner.py::test_no_new_hand_rolled_ladder` (`:452-474`),
   which flags a file producing **≥2** band strings.
2. **The `if`-routing half: this is a provider resolved by ROW, through `manifest/`.**
   `04 §C.5:682`, verbatim: `provider = manifest.resolve("contest", prizes[prize])   -- by string, at
   boot`. Dispatch by row is the shape the note **asks for**, and ED-SC-0033's point (1) rules it:
   *"the seam dispatches by manifest ROW rather than the hardcoded personal_combat literal"*. ⚠ Note
   what the ruling names — **`manifest`**, which is why the registry in U1 is `engine/season/manifest/`
   (`04 §A.2:136`, `04:125`, `04:1031`) and not a file under `seam/`.

### Signature

```python
sigma.resolve(w, claimants, causes, prize, *, verb, subject, rng) -> dict
  # RESOLVED
  # ⚠ `module` MUST MATCH THE MANIFEST ROW U1 WRITES (`provider: "sigma_leverage"`).
  #   This read `module="dice", resolver="dice_pool"` and would not match it.
  dict(status="RESOLVED", module="sigma_leverage", resolver="d10_sigma",
       pool=<int>, ob=<int|float>, net=<int>, rolls=[...], seed=<int>)
  # REFUSED -- ob > obstacle_refusal_multiple x pool
  dict(status="REFUSED", why="S27.4", pool=..., ob=...)
```

`degree_of` grades `{"net", "ob"}` **unchanged** (`shape.py:4050-4061`). `SeasonDriver.resolve` maps
`REFUSED` to the **existing** `attempt.refused` Event at `shape.py:3470-3486` — **which no CHOSEN act
reaches today**, because `Act.obstacle` defaults to `None` (`state/carriers.py:332`) and the chooser
never sets one. ⚠ **"Nothing sets it" would be false and the first draft said it:** `harness/probes.py:2373-2374`
builds `speak` Acts with `obstacle=` by hand, and `test_season_shape.py:3125` assigns
`a.obstacle, a.pool` directly to exercise the gate. The gate is reached today **by hand and never by
the loop**, which is the narrower true claim and the one that makes the provider's input new.

⚠ **AND S27.4 THEN HAS TWO EVALUATION SITES UNLESS THEY ARE UNIFIED, WHICH IS §8'S "THE RULE LIVES
ONCE" IN ITS OWN PLAN.** The driver's fold already evaluates `a.obstacle > mult * max(a.pool or 0, 0)`
(`shape.py:3470-3471`) on the ACT's declared pair; the provider would evaluate the same rule on the
DERIVED pair. **One owner:** the provider returns `REFUSED` with its derived `pool`/`ob`, the driver's
branch keeps its existing job (an act arriving with a hand-declared obstacle) and does **not**
re-evaluate what the provider already refused. The commit that lands the provider says which site owns
which input, or the arc has minted the nth obstacle gate while arguing against nth obstacle sites.

⚠ `[GAP: veto — 04 §C.5:684 spells the ladder call `degree = ladder.degree(margin, veto = provider.veto)`,
and the live `degree_from_net(net, ob, extension=None, **context)` (`dice_engine.py:227-228`) has no
`veto` parameter. `04 PART D row 23` (`:953`) grades the widening refusal "STRUCTURAL by signature",
which the live signature does not carry. `seam/wrappers/sigma.py` returns no veto and needs none — nothing it wraps
can widen an outcome — so this arc does not close the gap. It is named here so a later provider that
DOES need one does not discover it at the seam.]`

### Operands, each with its grade

- **`pool = p.capability.get(VERB_CAPABILITY[verb], fx.get("pool_default"))`.**
  `VERB_CAPABILITY` is a new roster (U1), **assumption, swept**. Warrant: `03 §A.2:28`, *"Rank supplies
  dice and gates nothing"*, and `#353 §9.2` as quoted live in the tree at `shape.py:854-855` —
  *"`capability` supplies dice and GATES NOTHING"*. `pool_default` is a **fixture with a register row
  and a three-point sweep**, because `capability` is **empty on every corpus person**
  (`requirements.yaml:72-74`; one writer, `probes.py:432`, which zeroes it — §2.3; ⚠ that row spells
  the writer `probes.py::_zero_capability` and **no such function exists** — the site is inside `p11`,
  decorated at `probes.py:422`. The row's PROSE is exact; its `::symbol` is not, and §2.3's *"states
  this exactly"* is narrowed to the prose), and `08 §3` gives
  assumption ⇒ inject-declare-sweep, **never refuse the whole corpus**. **[CLOSED — READ 2026-09-09.**
  `architecture/meta/08_DATA_AND_KEYS.md` §3 is at `:50`; its grade table gives `assumption` →
  *"**inject the default · declare the site · sweep three points.** ⚠ A verdict that flips across the
  sweep is itself a finding, and a more important one than the verdict"* (`:56`), and `absent` →
  *"**REFUSE. No default.** An instrument that fills it has invented"* (`:57`). So the licence used
  here is the `assumption` row's, exactly, and the refusal belongs to a grade this fixture does not
  carry.**]**
- **`ob`** = `act.obstacle` if declared; else the 2026-08-14 ruling — *"their corresponding **score/2
  plus whatever specific modifiers exist for them in that instance**"* (`dice_engine.py:242-245`) —
  applied to the **subject's** capability on the same key when the subject is a person; else
  `fx.get("obstacle_default")` (fixture, assumption, swept). **No "Base Ob by scale"** (Jordan
  2026-09-05). ⚠ And per §2.10, register this as an **nth site in a family the tree records as
  disagreeing**, not as adopting a single owner.
- **S27.4's refusal** (`ob > mult * pool`, `mult = w.fixtures.get("obstacle_refusal_multiple")`,
  `shape.py:3471`) is evaluated on the derived pair **inside the provider**.

### Seeding — and why per-draw `H`, not a threaded stream

`SeasonDriver.resolve` — the driver, at the RESOLVE step, holding the ACTS token — constructs

```python
rng = random.Random(int(H(w.world_seed, w.tick, a.actor, f"roll:{prize}:{a.id}"), 16))
```

and passes it to `contest(..., rng=rng)`, which passes it to the provider. This satisfies **`04 §C.12`
rejection 4** (`:857-863`), verbatim: *"When R-09's producer is built … **its generator must be
constructed by the driver from the run seed and passed down exactly as `World` is.** This is the one
rejection that is **not yet load-bearing**, because no roll exists yet."* **U1 is what makes it
load-bearing**, and the plan should say so in the commit that lands it.

⚠ **"Threaded like `World`" in that rejection means *passed by parameter rather than reachable by a
global name*, not *one continuous stream*.** The two readings diverge, and `04 PART D row 35` (`:968`)
settles it: **"a new draw moving unrelated goldens" | `H(seed, tick, subject, purpose)`; no counter, no
service | MECHANICAL (a pinned golden); CONVENTION on `purpose` uniqueness — the chain's own measured
hazard.** A single stream threaded through the season makes every roll depend on the count of prior
draws, so **adding one contested verb would move every other verb's outcome.** Per-draw `H` is the
construction row 35 names.

It is the same **construction** `combat_seam.resolve` already uses — `combat_seam.py:153`,
`seed = int(S.H(w.world_seed, w.tick, a_id, f"contest:{prize}:{causes[0] if causes else ''}"), 16)`,
consumed at `:160`. That function is refactored to **take** `rng` rather than build its own.

⚠ **BUT IT IS NOT THE SAME SEED STRING, AND THE FIRST DRAFT'S CLAIM THAT IT WAS IS FALSE.** The driver
line above spells `purpose` as `f"roll:{prize}:{a.id}"`, against combat's `f"contest:{prize}:{causes[0]
…}"`, and the third argument differs too (`a.actor` versus `claimants[0]`). **Two different strings ⇒
two different seeds ⇒ every existing combat result moves**, which would silently re-record the
`kill / wound` goldens under cover of a refactor. **So `purpose` is PROVIDER-SPECIFIC, and the driver
asks the provider for it:** the manifest row carries the provider's `purpose(prize, act, causes)`, and
`personal_combat`'s is `f"contest:{prize}:{causes[0] if causes else ''}"` with `subject = claimants[0]`
— **byte-identical to `:153` by construction, which is then the refactor's own test.** `dice`'s is
`f"roll:{prize}:{a.id}"`, new and colliding with nothing. Per-draw `H` needs `purpose` uniqueness
(`04 PART D row 35`, `:968`, *"CONVENTION on `purpose` uniqueness"*); it does **not** need one spelling
across providers, and forcing one costs a golden re-record for nothing.

**After U1 there are exactly two `random.Random` construction sites in the package** —
`loop/driver.py::resolve` and **`seam/combat_seam.py`** (the path after step 8) — and the falsifier
counts call sites, not text (§2.5).

**Determinism controls that must hold.** `test_w9_check1_the_run_is_reproducible` (`:2652`);
`test_r4_event_ids_are_unique_per_draw_and_reproducible` (`:1143`);
`test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte` (`:1266`, one of **three**
`test_w15_*` — §2.15); and the campaign goldens under `engine/tests` **untouched** — the season
package imports `engine.autoload.dice_engine` (lazily, at `shape.py:3986`) and nothing imports the
season package into `mc_v18`.

⚠ **THAT LAST SENTENCE IS VERIFIED BY INSPECTION, NOT BY THE TEST THIS DOCUMENT FIRST NAMED.** There
is no `test_engine_does_not_import_systems.py::test_importing_engine_pulls_in_no_subsystem` — the name
lives only in that file's docstring (`:24`), is reproduced wrongly by `CLAUDE.md` §3, and
`grep -c "def test_importing_engine_pulls_in_no_subsystem"` returns **0**. The real function is
`test_importing_every_engine_module_pulls_in_no_subsystem` (`:358`), and what it asserts is that no
module under `engine/` loads a file under `systems/` (`:376-392`) — **a different claim**, silent on
`engine.season` versus `mc_v18`. The separation is real and measured by grep (U0's Control has the
command); **it is guarded by nothing, and under `CLAUDE.md` §0.1 pt 5 it should not be — the arc is
not load-bearing on it.** Because the goldens are therefore identical by construction, they are a
smoke check here and not a control.

### Why R-09 reads `partial` after U1, not `met`

**The roll varies by SEED and by FIXTURE, not by PERSON**, because `capability` has no writer (§2.3).
`met` follows when capability is written — character development, scale row 1, **out of this arc**
(§10) — or when W27's cast (U8) seeds it per case. **Record that sentence in R-09's `measured:`.**

### Which verbs gain `contests:` first, and the test that decides it

**`tell` and `speak`.** Both execute in the corpus today (`requirements.yaml:203`), and both are
social-stratum person-to-person acts that
`test_we_only_a_verb_that_declares_contests_can_be_graded_today`'s own docstring names as the verbs a
degree would matter for: *"`speak`, `tell`, `utter`, `petition` and `the six investigation acts` — the
person-to-person verbs a degree would matter most for — are all in that 31."* Prize: **`a standing`**,
already rostered (`rosters.yaml:542`).

**`tell`'s degree-keyed `emits`:** `Overwhelming`/`Success`/`Partial` → `news.told`; `Failure` →
`news.untold`. **Both kinds are already declared on the row** — `verb_table.yaml:484-485`,
`emits: ["news.told"]` and `emits_on_refusal: ["news.untold"]` — **so this introduces no new Event
kind**, which is the load-bearing property and it is checkable by reading the row.

⚠ **What the first draft wrote instead was that *"loader invariant 7 admits them"*, and that is a
PROSE INVARIANT CITED AS MECHANISM — the §0.05 defect this document's own `## Status:` line invokes.**
Invariant 7 (`04:466`, *"the Event-kind roster is **derived** from every emission column, and the log
accepts no other kind"*) is **SPECIFIED AND UNBUILT**: `04 §F.20b:1084` records that the fold mints
`act.ineligible`, `act.refused` and `contest.resolved` as **body literals**, that *"invariant 7 refuses
all three at `append`"*, and therefore that *"the loop as built cannot run under the loader as
specified … **or the derived roster is not derived**"*. No derived Event-kind roster and no kind check
at `append` exist in `engine/season/data/`. **So nothing admits these kinds; nothing has to, because
they are already on the row.** Do not cite invariant 7 as the reason. `writes:` stays `[]` at every
band, and a
`Failure: []` is **lawful** — `04 §C.4:630-634`: *"**`Failure: []` is the only place in this architecture
where writing nothing is correct**, and it is correct because the act still **emits** … **That is the
difference between a refusal (the precondition failed, no contest occurred) and a loss (the contest
occurred and went against you)**."*

**`speak`'s `Failure`** needs a refusal kind its row must declare (today `emits_on_refusal: []`): add
`speech.unheard` to the matrix's declared kinds, or reuse `news.untold`. **The loader's derived roster
decides, not the body.**

**Decided at §0 test 5** — the smallest corpus-executing set that makes R-09 measurable. The stated
alternative, `petition`/`repudiate`, moves the same number and additionally touches `Petition.exists`
writes, which is more.

---

## §8 · THE PROSE→CODE TRANSLATION PROCESS — a repeatable procedure

`CLAUDE.md` §0.05 governs. **The process runs PER STATEMENT, not per document, and terminates in a form
a LOADER or a FALSIFIER evaluates** — `04 G.3.1:1355`: *"A design statement survives only in a form
something other than a reader can evaluate."*

### STEP 1 — LOCATE AND CLASSIFY, by *"would changing this change the GAME, or how the CODE works?"*

| the prose says | it becomes | where | the reader that makes it DECLARED (ID-13) |
|---|---|---|---|
| a closed set (kinds, sources, forms) | a **ROSTER** | `rosters.yaml` `rosters:` with `source:`, `open:`, `note:` | bound at import by `data/rosters.py`; a body literal of ≥3 identifiers fails `test_jordan_no_definition_is_hardcoded_in_a_body` (`test_season_shape.py:1800`) |
| a mapping keyed on a roster | a **TABLE** | `rosters.yaml` `tables:` with `row: H-NN`, `default_cell`, `sweep`, `keys` | `table()` / `roster_map()`; the loader cross-checks keys against the roster **both ways** (`data/fixtures.py:94::_load_matter_tables` is the template) |
| a free scalar | a **FIXTURE** | `data/fixtures.py` `DEFAULT_FIXTURES` + a `hole_register.yaml` row (`grade`, `site`, **3 distinct sweep points**) | `Fixtures.get(name)` raises on an unregistered name; `test_w9_check3_every_fixture_read_resolves_to_a_register_site` (`:2805`) refuses a read with no `site:` |
| an act | a **VERB ROW** | `verb_table.yaml`: five columns + `requires_typed` (one of the **seven forms**, `04 §F.24a:1090`) + degree-keyed `writes`/`emits` **iff `contests:`** | the fold (`loop/driver::_fold`); `resolvable_verbs()`; **twelve loader invariants at import** (`04 §B.13:441-477`) |
| a precondition no form fits | a **PREDICATE** | `loop/predicates.py`, `@requires_predicate` | **but FIRST ask whether the grammar needs an eighth form.** `§F.24a` closes *"30 of 32 cells"* with seven, and *"two cells are not predicates at all"* |
| what a verb changes | an **EFFECT** | `loop/effects.py`, `@effect_for`, writing **only** through `w.write` | `writes:` ⊆ matrix rows (invariant 1); an effect touching nothing **emits the refusal** (`shape.py:3352-3357`) |
| a consequence per outcome | a **DEGREE BRANCH** | the sixth/seventh columns | `writes_at(degree)` / `emits_at` (`shape.py:3302`) |
| a mechanism | **CODE + A FALSIFIER** | the owning Layer-1 module | the test that is **RED BEFORE and GREEN AFTER** |

### STEP 2 — PROVENANCE, IN THE ROW AND ON THE LINE

Every roster / table / verb row carries `source:` naming a `PP-NNN` / `ED-NNN` / `file §`. A numeric
literal in `.py` carries `# [canonical: path §section]` on the same or previous line **or fails
`tools/ci_sim_fabrication_check.py`**. A number that is **not** a game value carries `[JUSTIFIED: …]`
(the live examples: `test_season_shape.py:555` — *"a VACUITY FLOOR over this package's own module
count, not a game value"* — and `:558`, and `state/carriers.py:327`) or `[GROUNDED: …]` for a measured
sweep point. An **`assumption`** row carries a `site:` and three distinct `sweep:` points —
**`register.py::rule_R2`**, not G6 (§2.7). An **`absent`** row carries a non-empty `cite:` recording
that §0's five tests were run — **that is G6** (`register.py:34, :240`). And `rule_G12` forbids a
`cite:` arguing for a grade the row does not carry.

### STEP 3 — THE GATES THAT PROVE FAITHFULNESS, IN THIS ORDER

```
python -c "import engine.season.shape"              # the loader's cross-checks fire at import
                                                    # (NOT all twelve of 04 §B.13 -- invariant 7 is
                                                    #  unbuilt, 04 §F.20b:1084)
python -m engine.season.harness.register --check    # R2: site + 3 distinct sweep points; G6; G12
python -m pytest engine/season/tests -q             # the no-hardcoding guard, check 3, the H-66 sweep
python tools/ci_sim_fabrication_check.py
python tools/export_sim_params.py --check
# AND THE EXECUTION:
python -m engine.season.harness.corpus_run          # the verb EXECUTES, or the fixture IS READ, in >=1 world
```

⚠ **On the fifth line, stated plainly (§2.8).** `export_sim_params.py --check` is **run by no CI job,
no `.githooks/` hook and no `tools/valoria_local.py` step**, and the tool has no row of its own in
`references/ci_checks_registry.yaml`. Seven of the eight `tools/export_*.py` are invoked in
`.github/workflows/valoria-ci.yml` (`:126, :127, :134, :137, :141, :146, :150`); this one is not.
**The round-trip is nonetheless enforced**, by `tests/valoria/test_export_sim_params.py:21`, which calls
`esp.check()` directly and is inside the blocking `pytest tests/valoria` job (`valoria-ci.yml:365`);
the same file's `test_every_value_is_a_real_literal_from_source` re-extracts independently and compares
each value to the AST literal at its **definition site**. So: **running the command by hand tells you
sooner, not more.** Do not describe it as an unguarded surface, and do not add a CI step for it in this
arc — that would be a second copy of a rule that already lives once (`CLAUDE.md` §8).

**A TRANSLATION THAT LOADS BUT NEVER EXECUTES IS A CARRIER BEFORE ITS READER.**

### STEP 4 — THE REVERSE TEST, APPLIED BOTH WAYS

`04 G.3.5:1414`, verbatim: *"**The single test, applied in both directions.** If this document were
deleted, would the game behave differently? **No** → it is reference. **Yes** → the mechanism is in the
wrong place; move it into data or code and leave a pointer."*

- **DELETE THE PROSE** — the game must behave identically. It is now reference.
- **DELETE THE ROW** — the loader must **REFUSE, naming the row**. It is mechanism.
- **If deleting the row changes nothing, the row has no reader** and is not yet declared.

**How a runtime registry differs from reference prose, checkably.** A registry is opened by **exactly
one loader** — `grep -rln "verb_table.yaml" engine/season` → `data/files.py` plus one loader — and bound
to names code reads. A design document is opened by nothing: the one read of #353, at
`SOURCE_353_TEXT` (`shape.py:2276`), is for gap **attribution**, not resolution. `CLAUDE.md` §3's
`engine/season/` row already draws this line for `hole_register.yaml` — grader mechanism, game
reference.

**The live backlog, sited.** `sim_params.json` is an AST extract of module-scope literals under
`systems/*/sim` and `engine/` (`export_sim_params.py` `SCAN_DIRS`). Its **252 uncited** constants
(§2.9) belong to the retained three subsystems and the retire set, and are reached by this arc **only
where a seam reads one** — **U1 reads none; U9 reads none.** The loop's own constants **never enter
it**: they take the fixture / table route above, which is **stricter** — a register row with three
distinct sweep points, not a citation comment. The *"321 → 415 still inside `systems/`"* sentence in
`CLAUDE.md` §0.05 is about a migration **this arc does not run** (§10).

### WORKED INSTANCE — U7 group 3, the Dispensation four

`issue`'s cell *"scope enumerates executors, not places"* and `open_case`'s *"the act DECLARES the
stages and their terms"* are, per `04 §F.24a:1105-1110`, *"**constraints on the well-formedness of the
Act**, not questions asked of the world. **They belong in the `Act` schema and are refused at
construction**, not evaluated at RESOLVE."* So they are **not** `requires` cells and no predicate is
written for them.

`comply` / `evade / defy` / `refract` need an operand name — `dispensation` — added to the **closed**
`requires_operands` roster (`rosters.yaml:865`) with a `source:`, **and** `F.15`'s nine terms as a
`Record` kind schema **in data** before any predicate can read them. `F.15` (`04:1077`) grades that
absence: *"**the nine dispensation terms** *(§B.5)* — *\"nine typed terms\"* and nothing lists them | a
schema for one Record kind, **unspecified** | **not an assumption so much as an absence: the entire
downward mechanism has no executable content**, and `issue` produces a document nobody can comply
with"*.

**That is the shape of every remaining prose-only mechanism: the roster row precedes the predicate, and
the predicate precedes the effect.**

---

## §9 · THE GUARD-BLINDING HAZARD, HANDLED STRUCTURALLY

**One cause: a gate whose corpus is a hardcoded path is invariant under a move out of that path.** PR
#383's step-5 adversarial pass overturned the claim that no gate narrowed — *"**false**, and my
measurement was invariant by construction. Three gates read `files.SHAPE_PY` alone and did narrow."*
**Six rules, binding on every gate this arc writes.**

1. **THE CORPUS IS DERIVED, NEVER NAMED.** Model gates read `_model_modules()`
   (`test_season_shape.py:491-511`); instrument gates read `files.package_modules()`
   (`data/files.py:148-159`), which is `PACKAGE_DIR.rglob("*.py")` and whose docstring says why:
   *"THE DISCOVERY IS THE POINT … Recursive, because the harness modules now live one directory down
   and a flat `glob` would silently drop eight of them."* **A new directory — `seam/`, `decision/`,
   `manifest/` — is scanned the day it exists, with no edit anywhere.** The margin-producer scan already reads
   `files.package_modules()`, which is why U1's falsifier needs no corpus change.
2. **EVERY DERIVED-CORPUS GATE CARRIES A VACUITY FLOOR** in the `test_h115` form
   (`test_h115_the_fourteen_load_time_raises_are_unchanged`, `test_season_shape.py:513`, floor at
   `:556` — **not** the `:452` `test_h115` sibling, which carries no floor): `assert len(mods) >= 8, f"model set collapsed to
   {len(mods)} — this guard would pass vacuously"`; and where the gate polices a family, assert the
   family is present.
3. **POSITIVE `in` ASSERTIONS NAME A SYMBOL, NOT A PATH** — `inspect.getsource(<module>.<symbol>)`, so
   a move makes the **import fail loudly** rather than the assertion pass vacuously.
   **`files.SHAPE_PY` (`data/files.py:133`) MAY NOT APPEAR IN ANY NEW TEST**; at step 10 the constant
   is deleted, so any survivor is a `NameError`, **which is the good case**.
4. **A MODULE-LEVEL NAME REBOUND BY A TEST OR PROBE IS READ BY ITS CONSUMER THROUGH THE OWNER MODULE'S
   GLOBALS.** The four live rebinds — `S.ALIGNMENT` (`:2302`), `S._LADDER` (`:7837`),
   `S.belief_contradicts` (`:7012`), `probes.py:2450`'s `_s.contest = spy` — are re-pointed at steps
   6/7/8, and **any new rebindable** (the `PROVIDERS` table, the `draw` factory) is exposed from its
   owner and rebound there. PR #383's step-6 commit demonstrated the failure rather than predicting it:
   with a copied binding, *"the game behaves identically and only the instrument goes blind."*
5. **PLANT BEFORE TRUSTING.** Each new gate lands with **the counterfactual in its docstring** — the
   plant that turns it red — on the precedent at `test_season_shape.py:1828-1831`.
6. **NO NEW CI STEP.** The job is `python -m pytest engine/season/tests -q -n auto`
   (`.github/workflows/valoria-ci.yml:370`, recursive) plus
   `python -m engine.season.harness.register --requirements` (`:376`). **No gate this arc writes needs
   one**, and adding one would be the apparatus reflex `CLAUDE.md` §0.1 pt 5 disarms.

---

## §10 · NON-GOALS AND DE-SCOPING

| item | scale / row | why not this arc | what would change that |
|---|---|---|---|
| grid-based map combat with units | scale 5 / R-05 | **unbuilt design.** `requirements.yaml:104` — *"**GRID-BASED MAP COMBAT WITH UNITS DOES NOT EXIST ANYWHERE IN THE TREE**"*; a seam cannot be wired to a subsystem that does not exist | a design pass, then one engine behind an unchanged seam (`T-l`) |
| settlement management / city building | scale 6 / R-04 | `domain_actions` and `settlement_economy` are `doc: null` in `module_contracts.yaml`; the inline economy in `matter()` is *"a mode that never got its seam"* (`rosters.yaml:490-495`) — **the engine behind the seam must be BUILT** | the MATTER seam item, after this arc |
| mass-battle seam | scale 4 / R-05 | `a field` refuses by name; sides need `faction_q.resolve` (`04 §C.5.1:699`) which is R-04 / U9 | after U9 |
| the six investigation acts | scale 7 / U7 group 4 | their seam is **UNRULED** (`rosters.yaml:479`); `rosters.yaml:502-505` — *"**INVESTIGATION MUST NOT BE MADE A CONTEST TO BECOME GRADEABLE** … Giving them a prize so the existing machinery can grade them is scripting drift"* | the fieldwork translation under §8 |
| character creation / development | scale 1 / R-06, R-09's person term | **no writer for `capability`** (§2.3) and no `F.31` world-gen roster; individuation is demand-driven at CENSUS and **nothing demands** (`04 §C.7:743`) | a practice verb and the roster |
| design-ruling **R8**'s `seen` struct | R-07 deepening | its **own** sequencing ruling — `references/design_rulings_2026-09-06.md:287-288`: *"the first thing to build is not the carrier but **the consumer** — a person who forms a candidate because of what they came to believe"*; and R8.3 (`:266`) gates on `Claim.value` having exactly two readers | after U6 shows the claim→decision channel open |
| `Receipt` before/after, `NoOpReceipt` (`04 PART D row 5`, `:934`); the act store as state; the snapshot | not one of the nine | correctness items the 2026-09-06 plan puts on its critical path. **None of the nine's measures moves on them** | its own unit, sequenced beside U7 |
| typing the seam's return as a `Margin` (`04 §C.5:683`, the crossings type assertion at `04:692`) | not one of the nine | ⚠ **A DECLARED DEVIATION, NOT AN OVERSIGHT** (§7). Both providers return a **dict** today, which is what `combat_seam` returns and what `degree_of` grades (`{"net","ob"}`). Typing one and not the other gives the seam two return shapes — worse than either. The **contract** (no winner, no band, a margin the one ladder reads) is honoured; the **type** is not | one `seam/` unit typing both providers together, sequenced beside U7 |
| step B retirement; the Godot port | — | gated on R-04 (`CLAUDE.md` §3). `04 §C.12` rejection 4 is the **only** port constraint this arc must honour, and U1 does — it is what makes it load-bearing | after U9 |
| the `systems/` constant migration (252 uncited) | §0.05 backlog | **outside the loop's data path**; touched only where a seam reads a constant, and U1 and U9 read none | per-seam, as seams land |

⚠ **Two numbering schemes collide and a session will trip on it.** `references/design_rulings_2026-09-06.md`
numbers **R1..R8**; `engine/season/requirements.yaml` numbers **R-01..R-09**. **Design-ruling R8
(partial observation, `:198-320`) is not `R-08` (non-rational choice).** Commits `c3dca09` and `01141b4`
are ruling-numbered. Design-ruling R8's work has not started, so there is no live collision today.

---

## §11 · WHAT NEEDS JORDAN — AFTER THE FIVE TESTS

**ZERO open escalations, as of 2026-09-09 — and the count reached zero by a RULING, not by an
argument.** That distinction is the whole history of this section and is kept rather than tidied away.

⚠ **The first draft said *"Every candidate closes. ZERO escalations"*, and it reached that count by
CLOSING THE ONE LIVE QUESTION ON A QUOTE THAT DOES NOT EXIST** — *"ED-SC-0033 … 'wiring it now wires a
retired tree'"*, a string found nowhere in `registers/editorial_ledger_sc.jsonl` and, repo-wide, in
exactly one file: this one. A paraphrase promoted to a quotation, then used to close the escalation it
was invented to answer. The adversarial pass caught it, the count went to **one**, the row was put to
Jordan as `ED-SC-0037`, and **Jordan answered it**. The count is zero again for the opposite reason.
**A session reading this section cold must not conclude the escalation was talked away.**

*(§11.0 — Jordan's `ED-SC-0037` ruling on the interim social-contest provider — is recorded in
part 1; see the navigation block above.)*

---

### §11.1 · The nine that close

Recorded so a later session does not re-open them — the ED-IN-0185 failure `CLAUDE.md` §0 names.

| candidate | closes at | by |
|---|---|---|
| where the pool comes from (`verb_capability`, `pool_default`) | test 5 | `08 §3`: assumption ⇒ inject-declare-sweep; post-adoption §6 trap 14 |
| how `ob` is derived | tests 1 + 3 | Jordan 2026-08-14, *"their corresponding score/2 plus whatever specific modifiers exist for them in that instance"* (`dice_engine.py:242-245`); *"Base Ob by scale"* struck by Jordan 2026-09-05. ⚠ Registered as an nth site, not a single owner (§2.10) |
| which verbs gain `contests:` first | test 5 | the smallest corpus-executing set that makes R-09 measurable; the alternative is stated in §7 |
| scene tick shape (rounds; player granularity) | tests 1 + 4 | R-03's statement is **newer** than #353 S26.2; `rosters.yaml:455-460` records Jordan's granularity constraint verbatim |
| whether the tick may skip a person with no news | test 5 | a CONSTRUCTION over AX-2 (U2 decision 4), with its own falsifier (U2 falsifier b). ⚠ **Narrowed by the adversarial pass:** the first draft called it *a theorem* on the condition *"a claim landed, or `sense` changed"*, and that condition is **incomplete** — `questions_for` and `person_side_eligible` also read tenures, dates, docket, crossings and propositions. The corrected three-clause condition is a design call with an obvious engineering answer (derive the dirty set from the write matrix), so it still closes at test 5; it does not close as a proof |
| softmax sampling for R-08 | tests 1 + 5 | R-08 **is** the ruling; `tau` is assumption, swept. ⚠ **Narrowed:** `tau = 0` is a byte-identity arm that validates **plumbing, not the sampler** — the zero-temperature limit over the tied majority of candidates is uniform, not the alphabetical `sorted()` at `shape.py:810`, so the arm needs a discontinuous special case that exercises the old path (U4). Both prior plans name the arm and neither notices this; it does not reopen the ruling |
| the 13 convictions replacing the 4-axis stand-in | tests 3 + 4 | `references/descriptor_registry.yaml:235-251` already declares them and exports them behind a **blocking** `--check` (`valoria-ci.yml:137`). ⚠ **Narrowed by §2.6:** what closes is *may we READ the tree's own single-owner roster* — yes, and `H-46`'s own cite calls that a data edit. **`H-46` stays OPEN and its `absent` grade does not move**, on Jordan's *"may be modified in future"*. Populating is not closing |
| the 10 world-scale cases | test 5 | `PLAN.md:1613-1617` decides ≥2 realm rungs and records it on `H-95`. *"Jordan may overturn it; that is a ruling, not an open question this plan waits on."* |
| investigation: a contest or its own kind | test 5, **and de-scoped** | `04 §C.4` gives a degree only through `contests:`; a single-claimant provider is lawful (only combat refuses <2 — `combat_seam.py:142-145`); `rosters.yaml:502-505`'s *"not a contest"* is a note on the mechanism's shape, and `03 §E.1:220`'s *"an examination"* is not clearly the detective sense. **Nothing in this arc needs the answer**; the row stays UNRULED with this disposition recorded so it is not escalated by default |

---

## §12 · CRITICAL FILES

> ⚠ **THIS SECTION OPENED ON A FILE THAT DOES NOT EXIST, AND IT IS THE FIRST THING A COLD SESSION READS
> TO ORIENT.** The struck entry read: *"`engine/season/shape.py` — the driver (`SeasonDriver`, `:2724`),
> the chooser (`:773-818`), the seam (`:3875-4153`) until steps 7–9 move them. **Every unit's entry
> state is a line here**, and every line number here is against `main` `f41f20a1` (4,153 lines)."*
> **`shape.py` was deleted at step 10; `main` is `8b79440`.** §3 was re-measured on 2026-09-10 and this
> section was not, which is a scope failure of that amendment and is recorded rather than tidied.
> **Every entry below is re-measured at that commit.**

- **`engine/season/loop/driver.py`** (1,402) — the driver (`SeasonDriver`), `resolvable_verbs()` and its
  three gates (`:85-140`), the RNG construction U1 and U4 both reach for. **Where `shape.py`'s driver
  went.** ⚠ L5 splits this into driver + six steps.
- **`engine/season/decision.py`** (890) — the chooser (`make_chooser`), `align`, `stance_toward`,
  `urgency`. **U4's target, and U3b's.** ⚠ **A FILE, where `04:1046` requires a directory from its first
  commit** — L1's unit, and the reason U4 waits.
- **`engine/season/seam.py`** (372) — `contest`, `contest_subsystem`, `degree_of`, the ladder, and the
  `if _sub["module"] == "personal_combat":` literal at **`:341`** that U1 deletes. ⚠ **A FILE, where
  `04 §A.2:135` names a directory** — L2's unit.
- **`engine/season/combat_seam.py`** (**193**, not 189 — measured 2026-09-10) — the precedent
  `seam/wrappers/sigma.py` copies: derive one field,
  return the gap, per-draw `H` seeding at `:130, :153, :160`. ⚠ Its `purpose` string
  (`f"contest:{prize}:{causes[0] …}"`) is **not** the σ provider's and must not be unified with it
  (§7, Seeding). ⚠ **CORRECTED: this read *"at `seam/combat_seam.py` after step 8"*. Step 8 ran and did
  NOT move it** — the file is at the package root (`data/files.py:138` `COMBAT_SEAM_PY`) and
  `PATH_SEAM_ALLOWED` still reads `'season/combat_seam.py'`. **L2 moves it to
  `seam/wrappers/combat.py`**, and that is where the rename inside the shrink-only set is owed.
- **`engine/season/manifest/`** — **NEW in U1, and one of Layer 1's nine** (`04 §A.2:136`,
  `04:125`, `04 §C.5:682`, `04:1031`). Owns `PROVIDERS` and `resolve(role, module)`; the thing
  `seam/contest.py` calls and the thing ED-SC-0033 clause (1) names.
- **`workplans/2026-09-06-shape-decomposition-plan.md`** — **the single owner of decomposition steps
  7-10.** U0 carries only the deltas; three of them were written back into this file on 2026-09-09
  (its `:85`, `:88`, `:155` and its §4 step-7 / step-8 rows).
- **`engine/season/verb_table.yaml`** (555, 32 rows) — `contests:` and the degree-keyed
  `writes` / `emits` columns (U1, U5, U7); the seven-form `requires_typed` cells.
- **`engine/season/rosters.yaml`** (**1,039**, not 1,036) — `contest_subsystems` (**`:513`**, prizes at **`:542-546`**),
  `conviction_axes` (`:145`) and `tables.alignment` (`:975`) for U3, the seam table at `:474-482`, the
  granularity ruling at `:455-460`, and the new `verb_capability` / `stance_delta` / `scale_of_rung`
  rows.
- **`engine/season/write_matrix.yaml`** (372) — the `Person.stance` row at `:203-209`, already declared,
  already emitting `stance.moved`, and listed at `:50` among the RES-stepped rows with no producer.
- **`engine/season/tests/test_season_shape.py`** (**8,349** lines; **187** test functions,
  **187 passed** — re-observed 2026-09-10) — the no-producer scan at **`:8158-8168`** (regex `:8163`,
  the basename record at `:8164` U1 must re-point), inside
  `test_we_only_a_verb_that_declares_contests_can_be_graded_today` at **`:8118`**, with its **FOUR**
  breaks at **`:8135`**, **`:8143`**, **`:8146-8154`** and the scan itself.
  ⚠ **All five figures on this line were wrong and every one is corrected:** the file was cited at
  8,078 lines with 186 tests and *"**three** breaks at `:7866`, `:7872`, `:7877-7883`"* — a count §3's
  own new baseline already contradicted by one test, inside this document.
  ⚠ **And the AST-guard entry is struck entirely:** it read *"(`:2224`, whose corpus at `:2231` is
  `files.SHAPE_PY` **alone** and is re-pointed at step 7)"*. **`files.SHAPE_PY` no longer exists** —
  `data/files.py:133-137` defines `LOOP_DIR` / `DRIVER_PY` as its replacement — and step 7 ran. The
  live AX-2 guard is `test_decision_module_never_names_world`, which **L1** re-points from one file to
  a path scan over `decision/`.
- **`engine/autoload/dice_engine.py`** — `_die_result` (`:153-161`), `degree_from_net` (`:227`),
  `roll_pool` (`:196-206`). The single owner of the **ladder**, imported and called, never mirrored.
- **`engine/autoload/sigma_leverage.py`** — **the ruled contest provider (ED-SC-0037).**
  `roll_net` (`:286`) **plus `net_boost` (`:190`) — both, or it is not σ-leverage.** ⚠ It does **NOT**
  own the obstacle: `eff_ob` (`:169`) is *"DISPLAY ONLY (not the resolution value)"* by its own
  docstring and **consumes** `base_ob`; `effective_ob` (`:180`) is an arg-order alias of it.
  The worked composition is `systems/social_contest/sim/contest/resolver.py:302,307`.
- **`architecture/meta/04_CODE_ARCHITECTURE.md`** — §A.2 `:127`, §C.1 `:502`, §C.2 `:520`, §C.4 `:573`,
  §C.5 `:677`, §C.5.1 `:699`, §C.7 `:743`, §C.12 `:810` (rejection 4 at `:854`), PART D `:923` (header
  `:928`), §E.1 `:1038`, F.15 `:1077`, F.20a `:1083`, §F.24a `:1090`, §B.13 `:441`, G.2.9 `:1317`,
  G.3.1 `:1355`, G.3.5 `:1414`.

---

> ### ⚠ **A CITATION DRIFT IN `rosters.yaml`, MEASURED AND BOUNDED RATHER THAN SWEPT BLIND**
>
> Three lines were inserted into `engine/season/rosters.yaml` after this document's citations were
> taken. **The shift is NOT uniform and a blanket `+3` would be wrong**, so the boundary is measured:
>
> | verified UNCHANGED | verified **+3** |
> |---|---|
> | `:89` `rung_kinds` · `:145` `conviction_axes` · `:305` `observation_deposit_modes` · `:337` the three modes · `:339` `combat_degree_bands` · `:349` its *"NOT the ladder's four bands"* note · `:360` `wound_harm_models` · `:370` *"`total` IS THE CONTROL"* | `:455-460`→**`:458-462`** · `:502-505`→**`:505-508`** · `:514`→**`:517`** · `:539-543`→**`:542-546`** · `:865`→**`:868`** · `:975`→**`:978`** · `:999`→**`:1002`** |
>
> **So the three lines landed between `:376` and `:441`.** Everything cited at ≥ `:441` is `+3`;
> everything at ≤ `:376` is unchanged. **The citations this session re-typed into new text are
> corrected** (`:517`, `:532-533`, `:542-546`, `:513`, `:978`); the rest are left for the unit that
> next opens them, per the standing rule that a stale path is fixed **in the commit that surfaces it**
> and nowhere else — opening a sweep here would be apparatus work on a reference document.
> ⚠ **Re-derive by anchor, never by adding 3**: the boundary above is why.

---

## §13 · SIZE — measured, and over the convention's threshold

**SPLIT EXECUTED 2026-09-10, at the §6/§7 boundary this section itself specified.** The single file
this section used to measure no longer exists as one file: it is now
`workplans/2026-09-09-r-execution-plan.md` (**part 1**: front matter, §1–§6, §11.0, §14) and
`workplans/2026-09-09-r-execution-plan_part2.md` (**part 2**: §7–§10, §11 preamble + §11.1, §12,
§13, §15). Both, re-measured at `tools/ci_common.py::tokens` — the repo's single owner of that
estimate, characters ÷ 4 — after the split:

| | lines | `tokens()` | `len()` | `wc -c` |
|---|---|---|---|---|
| **part 1** | 1,848 | 33,435 | 133,741 | 135,435 |
| **part 2** (this file) | 1,049 | 21,958 | 87,835 | 89,217 |

⚠ **Say which character count, per this section's own long-standing rule**: the `len()`/`wc -c` gap
on each file is that file's own `§`, `⚠`, `→` and `≥`; `tokens()` divides `len()`, not `wc -c`. **Neither
part is under** `references/atomization_rules.yaml`'s `sequential_chunk_tokens: 15000` — part 1 at 33.4k
and part 2 at 22.0k are each still over the 15k convention threshold individually. The split was scoped
to this task as a two-way split at the §6/§7 boundary; it roughly halves the overage rather than
eliminating it, and a further split of part 1 (the larger half, and still the more crowded of the two —
§6 alone runs to U0-U10) is left as a later call rather than taken here.

**Measured immediately before the split, for the record — this is the "2,848 lines, 54,547 tokens"
figure the last four re-measurements below refer to:** **2,848 lines**, **54,547 tokens**, `len()`
**218,190**, `wc -c` **221,177 bytes** (RE-MEASURED 2026-09-10 after the Arc-3 amendments, the
adversarial reconcile, and the U3a revert). Both are true of their own basis, which is the failure
mode `CLAUDE.md` §0.1 names and which PR #383 paid for once already (*"One instrument, named, for
numbers that get compared."*).

*(Post-first-adversarial-pass, pre-amendment: 2,057 lines, 37,869 tokens. The Arc-3 amendments added
**275 lines net**, and the second adversarial pass — thirteen HIGH findings, five of them refuting
this document's own new claims — added **279 more**. That pass cost more lines than the amendments it
audited, which is the honest shape of a reconcile that found a false central argument* — §3, §5, U0, U1's head, §11.0 and U10 were largely REPLACED rather than extended, and U0
collapsed from 60 lines to 22, which offsets most of §15's 200.)*

*(The pre-pass figures, kept so the delta is checkable: 1,520 lines, 24,868 tokens, `len()` 99,474,
`wc -c` 100,697. The pass added **537 lines net** — corrections, the §11.0 escalation and §14 — while
U0 itself SHRANK from **125 lines to 60** by citing its owner instead of restating it.)*

That pre-split total was **over** `references/atomization_rules.yaml`'s `sequential_chunk_tokens:
15000`, and the first drafting of this section claimed it was under. It was not; the claim was
retracted rather than left standing, which was the only move available to a document whose whole
subject is citation fidelity.

**What that meant in practice, kept so the reasoning is checkable rather than just the conclusion.**
The threshold is a `WARNING`-level convention (`CLAUDE.md` §4), not a blocking gate: the sibling
`workplans/2026-09-06-season-loop-execution-plan.md` is **23,206 tokens** and sits on `main` with CI
green. So the single file was, at each measurement, at or near the size of its closest peer and
subject to the same convention — shipping it as one part was a deliberate choice for a while, not an
oversight. The successive re-measurements read 60%, 85%, 112%, 120%, 124%, 126%, 131% longer than that
peer, each one restated rather than re-asserted from the last, until the split below stopped being
deferrable.

**Where it split.** At the §6/§7 boundary: §1–§6 are verification and sequence; §7–§15 are the deep
placement argument, the repeatable procedure and the Arc-3 method (§15, added 2026-09-10, after this
guidance was first written, is the third of those and is placed with part 2 on that basis — see part
1's navigation block for the one-line reasoning). The break is a reading-order break, not a filing
one: it was **not** taken at §2, because the corrections there license every citation reproduced
downstream of them, and separating them from the units would recreate the index+infill shape
`CLAUDE.md` §4 retired. **§11.0 went with part 1** — an escalation a reader must see cannot live in a
second file — and **§14 went with part 1** too, since it audits both parts; part 2 carries a pointer
at each section's original position rather than a second copy of either.

*(§14 — the adversarial-pass changelog, which audits both parts — is recorded in part 1; see the
navigation block above.)*

---

## §15 · ARC 3 — THE ORDER, THE METHOD, AND THE ANTAGONIST'S CHARTER

**Added 2026-09-10.** §1-§14 were written as a standalone plan; `workplans/2026-09-09-layer1-conformance-plan.md`
(PROPOSED, PR #386) then made U1-U10 **Arc 3** of a three-arc sequence. This section carries what that
framing adds and **nothing that already lives elsewhere** (`CLAUDE.md` §8). It does not restate the
dependency graph (§4), the placement argument (§7), the translation procedure (§8), the guard-blinding
handling (§9) or the non-goals (§10). Those stand.

### §15.0 · ⚠ **ARC 1 HAS LANDED. RE-READ §15.1 THROUGH THIS SECTION — MOST OF ITS BLOCKERS ARE GONE AND ONE OF ITS DESIGNS IS STALE.**

**PR #386 merged 2026-09-10 (`main` `c2de9ee`, 11 commits, 50 files) and it did not stop at a plan —
it EXECUTED Arc 1.** Merged into this lane at `61f687e`; measured here after the merge:

| | |
|---|---|
| `engine/season/` now holds | **`decision/`** (`budget` · `choose` · `options` · `questions`) · **`seam/`** (`contest` · `ladder` · **`wrappers/combat.py`**) · **`manifest/`** (`__init__` · `registry`) · **`queries/`** (+ `person_q` · `cache`; **`readers.py` DELETED**) · **`loop/`** (+ `calendar` · `census` · `deliberate` · `matter` · `resolve` · `witness`) |
| content hash | `ee0383bf3f4606e56b80cd07c0284f0a` — **unchanged**, as a pure structural arc must be |
| `pytest engine/season/tests` | **190 passed** (was 187; Arc 1 added three) |
| `register --requirements` | **6 `not_met` · 3 `partial`** — unchanged, which is Arc 1's own declared success condition |
| `ED-SC-0037` | **`status: ruled`, `needs_jordan: false`** — the flip is on `main` |

**WHAT THIS UNBLOCKS, and it is most of the arc.** L1–L5 are merged, so the Arc-1 rows of §15.1's
table are satisfied: **U1** (needs `seam/` + `manifest/`), **U2** (needs `loop/`'s six steps),
**U3** (needs `decision/` as a directory) and **U4** (same) are all **UNBLOCKED**. ⚠ **Arc 2 is NOT
built** — `state/` holds only `carriers.py`, `ids.py`, `world.py`: no `gate.py`, no `Receipt`, no
token type. **So `U9` remains blocked on `G3`/`Act.via`, and that is now the arc's only structural
blocker.**

⚠ **AND U1's `manifest/` DESIGN IS STALE — READ THIS BEFORE BUILDING IT.** U1 below specifies
`manifest/` as owning *"`PROVIDERS: dict[tuple[str, str], Callable]`, keyed `(role, module)`, filled
at import by a `@provider(role, module)` decorator"*. **That is not what shipped.** The real
`manifest/registry.py` is a **descriptor lookup, not a callable registry**:

- `resolve(role, key) -> Optional[dict]` returns `dict(module=…, resolver=…, doc=…)` read out of
  `references/module_contracts.yaml` — **not a function to call.** `_ROLE_ROSTERS = {"contest":
  ("contest_subsystems", "prizes")}` is the whole role map.
- **`None` is a real answer**, deliberately: an unclaimed prize leaves the seam's generic refusal
  intact. So U1's third-gate amendment cannot ask `manifest.has(...)`; it asks whether
  `resolve("contest", row.contests)` is `None`.
- **`rosters.yaml`'s `prizes` is STILL the string schema** (`"a standing": "social_contest"`), so
  U1's prize→row schema change is still owed — and it must now fit `resolve`'s lookup, which reads
  the mapped value as a **module name validated against the contracts file** and raises if the
  contracts declare no such module. A bare `provider: "sigma_leverage"` will not resolve unless
  `module_contracts.yaml` declares it.
- **The `if _sub["module"] == "personal_combat":` literal SURVIVES**, now at
  **`engine/season/seam/contest.py:124`** — so U1's *"the literal is deleted"* is still real work,
  and its line citation moves from `shape.py:4122` to that.
- ✅ **`seam/wrappers/combat.py` exists**, which settles U1's placement adjudication empirically:
  `seam/wrappers/sigma.py` now has a real sibling rather than an argued one.
- Arc 1 also shipped `manifest.unclaimed_contest_prizes()` — invariant 9's **key** side, which
  `check_rows()` does not cover — found by #386's own Fable gate. U1 should assert on it rather
  than re-deriving the check.

⚠ **Any citation in this document to `queries/readers.py` is dangling — the file is deleted.**

**DO NOT re-plan Arc 3 from scratch on this.** §2's corrections, §4's graph, §7's placement argument
and §8's procedure are unaffected: they are about the game, not about where a module sits. What is
stale is precisely the precondition column and U1's manifest shape, both corrected above.

---

### §15.1 · The order, and what each unit is waiting on

`H` = hard (cannot start, or cannot be measured). Read with §4, which owns the *reasons*.

```
   ARC 1 (L0→L1→L2→(L3∥L4)→L5)          ARC 2 (G1→G2→G3→G4)
        │                                      │
        │ manifest/ (L4) · seam/wrappers/ (L2)  │ Act.via (G3)
        │ decision/ (L1) · loop/ six steps (L5) │
        ▼                                      ▼
  U1 ──H──▶ U5 ──┐                       U7 gp 1-2 ──S──▶ U9
  U2 ────────────┤                        U8 ────────H───▶ │
  U4 ────────────┴──H──▶ U6 ──▶ U7/U8/U9 ──────────────────┴──▶ U10
  ▲                     (FIRST                                  (SECOND
  └──S── U3           MEASUREMENT)                            MEASUREMENT)
```

⚠ **THREE EDGES IN THE FIRST DRAFT OF THIS GRAPH CONTRADICTED §4, AND ONE CONTRADICTED THIS
SUBSECTION'S OWN TABLE TWO ROWS LATER. Corrected, with §4's grade named at each:**

- **`U3 ──H──▶ U6` was wrong.** §4 `:453` names R-01/R-02's hard inputs as **R-09, R-03, R-07, R-08**
  = U1, U2, U5, U4. **U3 is not among them**, and §4 `:412` grades its edge
  `H-46 ──S──▶ R-08` — **soft, and to U4, not U6.** The table below always said *"U1, U2, U4, U5"*,
  so the graph disagreed with the table inside one subsection.
- **`U9 ◀──H── U7 gp 1-2` was wrong.** §4 `:475` grades it **`R-05a → R-04 — SOFT`**, in those words.
  Drawn `──S──` here. What is **hard** into U9 is `Act.via` (G3) and U8's cast.
- **U8's edge was missing.** §4 `:479` grades `W28 → R-06b` **hard**, and U9's own preconditions
  require U8's NPC-lane cast, so it is drawn.

**This subsection does not re-grade anything.** Where it and §4 disagree, **§4 wins and this graph is
the defect** — that is what *"read with §4, which owns the reasons"* means, and the first draft failed
its own instruction.

| unit | starts when | why not sooner |
|---|---|---|
| ~~**U3a** · the 13×4 as a carrier nothing reads~~ | ~~now, on `main`~~ | **STRUCK 2026-09-10 — BUILT, LANDED, REVERTED.** A declared-but-unread table is what `04:124` binds `data/` to raise on, and its byte-identity control was **fake by this document's own `F13` criterion** (identical *by construction*). See the box below |
| **U3** · the table + the swap + the projection, ONE unit | ✅ **UNBLOCKED 2026-09-10 — L1 IS MERGED** | the table may not be separated from its reader (`04:124`), and the swap resolves the `Precedent` two-sense collision. **The score now lives in `decision/choose.py`** |
| **U7 gp 1-2** · 15 of the 20 verbs | **now, on `main`**, with one qualifier measured | `verb_table.yaml`, plus **appends** to `loop/{predicates,effects}.py` |
| **U1** · R-09 producer + R-05b | ✅ **UNBLOCKED 2026-09-10** — L2, L4 merged and ED-SC-0037 is `ruled` | ⚠ but read **§15.0**: the shipped `manifest/` is a descriptor lookup, not the `@provider` registry U1 specifies |
| **U2** · R-03 scene tick | ✅ **UNBLOCKED** — L5 merged; `loop/` now holds the six steps | reshape `season()` into rounds against `loop/driver.py` + the six, not the old single body |
| **U4** · R-08 sampling | ✅ **L1 merged** (`decision/` is a directory: `budget`·`choose`·`options`·`questions`); still needs U3 | the sampler lands in `decision/choose.py`, which now satisfies `04:1046` by construction |
| **U5** · R-07 stance | **U1 half (b) merged** | its precondition is a non-empty `DEGREES RESOLVED:` line |
| **U6** · R-01/R-02 first measurement | **U1, U2, U4, U5 merged** | measuring before a producer exists measures the theorem (§4) |
| **U7 gp 3** · the Dispensation four | the `dispensation` operand row + F.15's nine terms exist as data | §8's worked instance — a prose→code translation, not wiring |
| **U8** · R-06b ambitions + cast | **W28's `cast:` blocks authored, NPC lane first** | `PLAN.md:1587-1589` |
| **U9** · R-04 strategic scale | ⛔ **STILL BLOCKED — the arc's ONLY structural blocker.** `G3` (`Act.via`) + U7 gp 1-2 + U8's NPC lane. **Arc 2 is unbuilt**: `state/` has no `gate.py`, no `Receipt`, no token | `H-108`; §4 grades it hard |
| **U10** · second measurement | U7/U8/U9 merged | — |
| **U7 gp 4** · six investigation acts | — | **de-scoped** (§10) |

> ### ⚠ **U3 CANNOT BE EXECUTED AS SPECIFIED, AND THIS WAS FOUND BY PRE-FLIGHT — STAGE 1 DOING ITS JOB.**
>
> U3 bills itself *"Preconditions. None. **Data only.** Can start on `main` today"* (`:1057`). Measured
> against the tree 2026-09-10, it is neither, and the two failures point opposite ways:
>
> **(1) The 13 convictions and the 13×4 projection are INERT unless `decision.py` changes.**
> `decision.py::make_chooser`'s score is
> `sum(float(p.convictions.get(ax, 0.0)) * align(c.verb, ax) for ax in CONVICTION_AXES)` —
> `Person.convictions` is keyed **by AXIS**, over the four-member roster. For 13 convictions to reach
> the score they must be **projected** through the matrix, which changes `make_chooser` — **in
> `decision.py`, the module L1 turns into a directory.** So data-only ships two **dead carriers that
> pass every test**, which is the exact defect `rosters.yaml`'s own alignment note forbids
> (*"a zero matrix makes convictions inert … it would pass every test while meaning nothing"*).
>
> **(2) The axis membership swap silently ZEROES every seeded person.** `conviction_axes` holds
> `[Precedent, self_preservation, suspicion, harm_borne]`; the registry's four ethical axes are
> `(hierarchical, sacred, instrumental, traditional)` (`engine/substrate/keys.py:59`). **Zero overlap.**
> `harness/headless.py:92-94` seeds Carin, the Bailiff and the Warden **by the old axis names**, and
> `harness/corpus_run.py:228` picks `axes[pick]` from the same roster. After a swap every
> `convictions.get(ax, 0.0)` returns `0.0`, every candidate scores alike, **the ranking collapses to the
> alphabetical tiebreak and the content hash moves** — with no test naming why. Separately,
> `data/verbs.py::_load_alignment:320-327` raises `Forbidden` on any alignment row key outside the
> roster, so all **27 declared cells** (not 128 — that figure is the SPARSE key space of a 32×4 table
> with `default_cell: 0.0`) go invalid at import.
>
> **⚠ U3's own falsifier cannot observe either failure.** `test_w5_the_alignment_table_is_swept…` flips
> on **alignment**, not on the projection, and stays green throughout. A projection-specific falsifier is
> owed: two persons whose 13-vectors project to different axis vectors must rank differently.
>
> **✅ And one finding cuts the other way, making U3 smaller:** the 13×4 matrix is **already authored**,
> with per-row calibration rationale, at `systems/characters/reference/conviction_axis_matrix_v30.md` §2
> (`:24-40`). The 52 projection cells are **transcription with provenance**, not invention — U3's
> *"GAME CONTENT … the assumption grade where [no source] exists"* understates what exists. ⚠ Cite
> **PP-684**, the matrix's own authority; `PP-687` is the axis-space substrate it projects **onto**
> (that doc's §1 says so), and the descriptor registry's `PP-687` attribution is what propagated the slip.
>
> ### ⚠⚠ **U3a WAS BUILT, LANDED, AND THEN REVERTED — 2026-09-10. THERE IS NO "CARRIER WITH NO READER" HALF OF U3, AND THE SPLIT BELOW IS AMENDED TO SAY SO.**
>
> The split as first written landed the 52 projection cells as **a table nothing reads**, with
> **byte-identity as the control**. It was executed (`a8184b9`), every instrument came back green —
> hash stationary, `runs/` byte-identical, `PROBE FLIPS 0`, 187 passed — and **it was reverted on two
> findings, one from a read-only critic and one worse one found while checking that critic's work.**
>
> **(1) A DECLARED-BUT-UNREAD TABLE IS THE ONE THING RATIFIED LAYER 1 BINDS `data/` TO RAISE ON.**
> `04:124` — the ID-12 · ID-5 · ID-13 row, whose module is `data/` — reads *"every roster, **table**,
> fixture, matrix and verb row read at load by one loader that cross-validates and raises on any
> absence or **any declared-but-unread row**"*. `01_AXIOMS.md` ID-13 states it: ***"A DECLARED FIELD
> MUST REACH A READER, OR IT IS NOT DECLARED … not a weak mechanism — it is a mechanism that does not
> exist, wearing a schema's clothes."*** `04:1157`: *"the fix `ID-13` licenses is a reader **or
> removal**, not a hole row."* **And `rosters.yaml` has already done this to itself:** its header
> (`:69-73`) records `governance_modes` and `power_bases` **DELETED** — *"They were not wrong; they
> were UNREAD"* — and `:907` calls an unused combinator *"the dead carrier `ID-13` refuses"*. The unit
> proposed to add, to that exact file, the thing that file deletes.
>
> ⚠ **And the licensing analogy this plan used was false.** It read *"a carrier with no reader, the
> same shape as U1 half (a)'s producer with no caller."* **Not the same shape.** `04:125` licenses the
> manifest provider explicitly — *"the seam names a role; a manifest row names the provider, **resolved
> at boot**"* — so that provider **is read, at boot**; it is merely **unexercised** by a corpus verb.
> An unread table is **unreachable**. The analogy substituted *unexercised* for *unreachable*.
>
> **(2) THE BYTE-IDENTITY CONTROL WAS A FAKE CONTROL BY THIS DOCUMENT'S OWN CRITERION — and this
> finding is worse than the first, because the first would have left the unit merely non-conformant
> while this one leaves it UNCONTROLLED.** §14's `F13` row, written into this file two commits before
> U3a was built, rejects `pytest engine/tests` as a control on the ground that both arms are
> ***"identical by construction — `CLAUDE.md` §7 (ED-MB-0066) names this a fake control."***
> **A table nothing reads is byte-invariant BY CONSTRUCTION.** The hash could not have moved, so the
> arm could not have failed, so it measured nothing. U3a's commit message asserted the opposite in
> terms — *"a carrier with no reader is byte-invariant, and that is what makes this control a
> measurement rather than a tautology"* — which is the criterion **exactly inverted**. Recorded in
> full rather than quietly corrected, because the inversion was written by the same session that had
> just written the rule.
>
> **THE CONSEQUENCE: THE 52 CELLS LAND IN U3b, IN THE SAME COMMIT AS THEIR READER.** That is how all
> three tables that already exist live — `alignment`→`data/verbs.py:318`,
> `band_floors`/`site_yield`→`data/fixtures.py:108,124` — so it composes on the existing primitive
> instead of special-casing this one. U3b's own control (`report && delta`, hash MOVES, flips named)
> is a real one. **Nothing is lost by waiting: U3b was already blocked on L1.**
>
> **SEVEN FINDINGS THE REVERTED CARVE PRODUCED. U3b INHERITS THEM; DO NOT RE-DERIVE THEM.**
>
> | # | finding, verified |
> |---|---|
> | **a** | **The 52 cells are exact.** Parsed programmatically from `conviction_axis_matrix_v30.md` §2 `:26-38` and re-verified by an independent re-parse: **52/52, every sign.** Row order matches both the document and `descriptor_registry.yaml:239-251`, so a derived row set aligns by name **and** by position. Column order matches `keys.py:59`. The table is **DENSE — 52 of 52 declared** |
> | **b** | **Do not mint a `convictions:` roster.** `engine/substrate/descriptors.py:155` reads *"THIS IS THE ONLY CONVICTION ROSTER IN THE ENGINE"*, and `:175` is `CONVICTIONS = tuple(_DATA['conviction_roster']['names'])` — the same registry a local copy would transcribe. **Derive from that owner** (U5's `ladder_bands` shape) |
> | **c** | ⚠ **But derive ON FIRST USE, NOT AT IMPORT.** `data/files.py:110-114` states the package rule — every reach out of the package loads *"BY PATH AND ON FIRST USE … deferred so the tracer still runs where the tree is absent, degrading to a NAMED gap rather than an ImportError at import"* — and both live reaches (`seam.py:205`, `test_season_shape.py:8087`) are inside function bodies. `engine/substrate/descriptors.py:41-49` does a bare `open()` **at module scope**, so an at-import derive turns a missing cooked artifact into an `ImportError` for the whole season package. **U5's precedent targets `engine.autoload` and does not cover this** |
> | **d** | **`Precedent` will carry two senses in one file until the swap.** It is a CONVICTION (a projection row key) and an AXIS (`rosters.yaml:171`, and an `alignment` row key). That is the `exposure` collision `conviction_axes`' own note forbids at `:161-163` **with a loader refusal**. U3b's swap resolves it — `Precedent` leaves the axis sense — so **the swap and the table must land together**, which is a second reason not to split them |
> | **e** | **`default_cell` is unreachable on a dense table**, and `H-46` is graded `absent` with `default: "none"` (`hole_register.yaml:527-528`). `register.py::rule_R3` refuses a default on an `absent` row but quantifies over **register rows**, so it cannot see a table injecting one. Annotate it or omit it; do not let it read as an injected default |
> | **f** | **Cite PP-684, and get the locator right.** The matrix's authority is `PP-684` (its own `:3`, `:5`, `:16`). ⚠ The reverted carve said the `PP-687` slip came from `descriptor_registry.yaml`'s `map.conviction_axis` row — **it does not: that row (`:259`) carries no PP at all.** `PP-687` is on the **adjacent** `axis.*` row (`:258`), where it is arguably correct, since `:16` makes PP-687 the axis space the matrix projects **onto** |
> | **g** | **The source contradicts itself about its own status** — `## Status: CANONICAL` (`:6`) against `**Status:** PROVISIONAL` (`:9`), plus PROVISIONAL at `:2`, `:230`, `:250`, and a live revision protocol at `:236`. **`CURRENT.md` indexes no row for it at all.** Under §0.05 it is reference either way, but say *transcribed from a provisional source* rather than *canonical* |
>
> **What the reverted carve does NOT establish, stated so it is not claimed:** the critic had no Bash
> and re-derived **none** of the five instrument results; it verified the cells and attacked the
> inertness claim by grep. Four of its attacks **failed and are recorded as failures** — no generic
> `tables:` iteration exists (`_TABLES` has four sites, all in `data/rosters.py`), `keys:` is
> validated by nothing, no test asserts a table count, and `rule_R2` correctly does not fire on an
> `absent` row. **The inertness was real. It was the licence that was wrong, not the fact.**

> **THE SPLIT, and §6's U3 body is amended to it before either half is built:**
> ~~**U3a** — land the table as a carrier nothing reads, control byte-identity~~ — **STRUCK, see the box
> above. There is no U3a.** **U3 IS ONE UNIT AND IT IS BLOCKED ON L1:** the 52 projection cells, the
> axis swap, alignment's 27 cells re-authored onto the ethical four,
> `headless.py`/`corpus_run.py` re-seeded **by conviction**, and the projection wired into
> `make_chooser` — **all in one commit, because the table and its reader may not be separated
> (`04:124`) and the swap is what resolves finding (d).** **Hash MOVES**, recorded via
> `report && delta`, every flip named.
>
> ⚠ **A read-only critic attacked this and reported U3 startable** — its `H3-H`, reasoning that
> `rosters.yaml` sits in a conforming module and no Arc-1 unit moves it. **That is true and it is not
> the question**; the critic did not open `make_chooser`'s score or the harness seeding. Recorded rather
> than dropped, because a later session will find that verdict and needs to know its scope.

> ### ⚠ **U7's `commit` WAS BUILT AND REVERTED, 2026-09-10 — AND IT IS IN THE WRONG GROUP.**
>
> `PLAN.md` `W31(a)` files `commit` under *"no hole, merely unbuilt"*, and this plan does **`commit`
> first** on its own reasoning: *"`Q4` (a live `commit` to an OUGHT) is the only question source that
> fires in a quiet season, and no verb can create one — every world seeds it by hand."* An effect was
> written (`@effect_for("commit")`, opening a `commit` Tenure actor→Proposition on `_eff_confer`'s
> pattern) and **reverted**. What it bought and what it cost, both measured:
>
> | | |
> |---|---|
> | `resolvable_verbs()` | **12 → 13** — the verb leaves *"19 have no predicate/effect"* |
> | `corpus_run` | `commit` moves to **"attempted and always refused"**, joining `work` |
> | executed set | **unchanged, 6 of 32.** U7's acceptance — *"the executed set gains the verb in ≥1 world"* — **NOT MET** |
> | content hash | **MOVES**, `ee0383bf…` → `2fa92709…` |
> | `delta HEAD` | **PROBE FLIPS 0**; probes 122→122; gap events 66→66; **+1 CLAIM, +1 EVENT, +1 WRITE** — one refusal, corpus-wide |
> | `pytest engine/season/tests` | **6 FAILED**, 181 passed |
>
> **Reverted on the trade, not on a defect in the effect.** Six pinned-golden tests
> (`test_wc_transfer_executes_in_the_corpus_and_the_executed_set_is_exactly_this`, the two W-B
> clause tests, the two W-D fork tests, and the ranking-discrimination test) go red because adding a
> verb to the resolvable set changes candidate sets corpus-wide and shifts the fork measurements.
> **Re-pinning six goldens to purchase one refusal event, for a unit whose own acceptance is unmet,
> is the trade `CLAUDE.md` §0.1 refuses** — a golden re-record must be intended and stated, and
> "the verb is now visibly refused" does not earn it. §0.2: done means it runs, and it does not run.
>
> **⚠ AND THE DIAGNOSIS IS THE REAL FINDING: `commit` IS A `W31(b)` ROW, NOT A `W31(a)` ROW.**
> Measured, not inferred — a spy on `EFFECTS["commit"]` over two seasons of `build_world(0)` records
> **ZERO calls**, while the log carries one `commitment.refused`. **The refusal happens in the fold,
> upstream of the effect**, at the typed `requires`. The cause is visible in the world: NPC-088 holds
> **exactly one Proposition** (`prop_einhir`) and **exactly one live `commit`** — Carin's, to that
> same Proposition. Q4 reads a person's *own* live commit-to-OUGHT, so the only person it fires for
> is the one person for whom a new commitment changes nothing; the other two never receive a question
> whose subject is a Proposition, and `operands_for` binds `subject` from the question.
>
> **So `commit`'s blocker is not a missing effect. It is that no question source hands a Proposition
> subject to a person who does not already hold one** — a hole of the `W31(b)` *"lands only when its
> row moves"* kind. Writing the effect cannot move it, which is why the effect is not on `main`.
> ⚠ **AND THAT RE-CHECK WAS THEN RUN, WHICH OVERTURNS THE SENTENCE ABOVE. `commit` IS THE EXCEPTION,
> NOT THE PATTERN — AND `PLAN.md` SENT THIS PLAN AT PRECISELY THE ONE VERB IN ITS GROUP THAT DOES NOT
> WORK.**
>
> A throwaway diagnostic — stub effects registered in-process for all 14, `build_world(0)` driven four
> seasons, **nothing written to disk** — measures which verbs the fold actually **reaches**:
>
> | outcome | verbs |
> |---|---|
> | **REACHED — the corpus forms the act and calls the effect** | **`forge` (4 calls) · `oblige` (4) · `succeed` (3) · `tie / knot` (3) · `petition` (2)** |
> | resolvable with an effect, but never reached | `carry` · `commit` · `repudiate` · `restore` |
> | **not resolvable even WITH an effect** — no `requires_typed`, no predicate | `determine` · `establish` · `exchange` · `levy` · `open_case` |
>
> Operands arriving: `subject` for `forge`/`oblige`/`petition`/`tie / knot`; `subject` **and** `to`
> for `succeed`.
>
> **So five of group 1 need ONLY AN EFFECT BODY, and they are startable on `main` today.** Four of the
> five carry `requires: —` (no precondition), so they pass the first gate outright; `succeed` is typed
> on a `held_by` relation the world satisfies. `PLAN.md` `W31(a)`'s *"no hole, merely unbuilt"* is
> **correct for these five and wrong for `commit`** — and this plan's *"`commit` first"* instruction,
> inherited from `PLAN.md:1649-1651`, aimed the first unit at the single group-1 row whose blocker is
> upstream. **Do `forge`, `oblige`, `petition`, `tie / knot`, `succeed` first; they execute.**
>
> ⚠ **The six golden re-records will still happen, and THIS time they are the intended trade.** A
> group that makes five verbs **execute** is exactly what U7's acceptance asks for and what §0.2 calls
> done; re-recording for that is a stated, intended re-pin. Re-recording for one refusal event was
> not. **State the re-pin in the commit, per §0.1, and record the flips with `report && delta`.**
>
> ### ✅ **AND THEN TWO OF THE FIVE WERE BUILT AND MEASURED — THEY EXECUTE. THE EFFECTS ARE REVERTED; THE MEASUREMENT IS NOT.**
>
> `_eff_oblige` and `_eff_succeed` were written (composing on one `_open_tenure` primitive rather
> than two copies) and run against the full 143-case corpus:
>
> | observable | before | after |
> |---|---|---|
> | `VERBS THAT EXECUTED` | **6** of 32 | **8** of 32 — gains `oblige`, `succeed` |
> | `DISTINCT EXECUTED SETS` | **2** | **4** |
> | `VERBS ONLY REFUSED` | 2 | **1** (`work`) |
> | `resolvable_verbs()` | 12 | **14** |
> | headless CONTENT HASH | `ee0383bf…` | `c44b1d96c7d504e9970bfe75ec6e18e5` |
> | NPC-088 season 1 | acts 6 · events 29 · deposits 19 | **acts 7 · events 31 · deposits 21** |
>
> **And the world produced something legible that nobody authored: `duty.taken` — Carin Vedel
> opens an `oblige` Tenure toward `einhir_texts`**, the suppressed cultural texts NPC-088 exists to
> copy. The chooser picked it. A new grammar claim `('einhir_texts', 'held_by:p_carin', False)`
> follows it into the ledger. `succeed` correctly emits `succession.refused` in her world (she
> holds no office) and executes elsewhere in the corpus.
>
> **R-05's `measured:` line moves from *"6 of 32 verbs execute"* to *"8 of 32"* when this lands.**
>
> ⚠ **WHY IT IS REVERTED RATHER THAN SHIPPED: SIX TESTS GO RED, AND ONE OF THEM NEEDS A CLAIM
> REWRITTEN, NOT A NUMBER BUMPED.** Five are honest re-pins of sets that grew by exactly these two
> verbs. The sixth is not:
>
> | # | test | what it needs |
> |---|---|---|
> | 1 | `…the_executed_set_is_exactly_this` **`:6154`** | pin 6 → 8. Its own message already says *"4 → 6 was `W-C`'s measurement and ANY MOVEMENT IS A FRESH ONE"* — so the re-pin must be attributed to THIS unit, not re-read as W-C's |
> | 2 | `…ranking_cannot_discriminate` **`:5230`** | pin 6 → 8 |
> | 3 | `…ranking_cannot_discriminate` **`:5300`** | ⚠ **NOT A NUMBER.** It asserts `set(by_sig)` is **exactly two** signatures *"differing by `tell` alone"*, split on a season threshold. **There are now four.** The structural claim is FALSIFIED — and falsified in the good direction, since executed-set diversity is what R-01/R-06/R-08 want. The test's own name is a finding (*"the ranking CANNOT discriminate"*), so landing this means **deciding what property it should now protect** and rewriting the claim with the new measurement. That is a judgment call and it is the reason this unit stopped |
> | 4 | `…control_arm_deposits_no_claim…` **`:7046`** | the `actor` arm now carries `('einhir_texts', 'held_by:p_carin', False)` beside `stores:grain`. The test warns that EMPTY would mean the cap is evicting — a non-empty gain is the good case and must be re-measured, not assumed |
> | 5 | `…clause_four_fires…` **`:7329`** | headless drops are `{succeed, transfer}`, not `transfer` alone |
> | 6 | `…report_py_reproduces_every_committed_artifact…` | `report` re-records the eight `runs/` artifacts; `delta HEAD` names every flip and the commit QUOTES it |
>
> **The six re-records are the INTENDED trade here** — §0.2 grades a juncture on behaviour that
> executes, and two verbs executing is that. What must not happen is bumping six numbers at the end
> of a long session and calling the suite green: `CLAUDE.md` §7 names re-pinning as *"the
> uncontrolled path"*, and row 3 is a design call wearing an assertion's clothes. **Land all six in
> one pass, with row 3 argued rather than edited.**
>
> **The effect bodies are ~60 lines and regenerate from this box.** `_open_tenure(w, subject, obj,
> kind)` is the primitive — idempotent, returns touched ids, `[]` on an already-live edge so the
> fold's write-nothing guard emits the row's refusal. `oblige`: `_open_tenure(w, a.actor,
> _operand(a, "subject"), "oblige")`. `succeed`: `_open_tenure(w, _operand(a, "to"), _operand(a,
> "subject"), "succeed")` — **the HEIR is the subject of the edge** (S15.1, an edge is owned by its
> subject) and the office is the object. ⚠ **Do NOT route `_eff_confer` through it**: conferral is
> open-and-close on a single-holder row, while duties and designations are additive — same `writes:`
> column, different operation.
>
> ⚠ **`carry`'s blocker is named and is a DEPENDENCY, not a hole:** it needs `Existence(subject,
> Petition)` and only `petition` writes `Petition.exists` — so `carry` becomes reachable **after
> `petition` executes**, within the same group. Sequence `petition` before `carry`.

⚠ **U7 gp 1-2's *"touches no module Arc 1 moves"* WAS TOO STRONG, and the qualifier is measured.**
`ED-IN-0206` item (6) — the row this plan cites throughout — reads *"`loop/` IS driver + effects +
predicates, **NOT '{driver} + six steps'**"*, naming those two files **as the non-conformity L5 exists
to repair**. So the first draft's justification cited a claim its own source contradicts. **What is
actually true, measured:** effects register through a **decorator into a module-level dict** —
`loop/effects.py:48` `EFFECTS: dict = {}`, `:51` `def effect_for(verb)` — and the fold reads it at a
**single site**, `loop/driver.py:856` `eff = EFFECTS.get(a.verb)`. U7 gp 1-2 **appends decorated
functions**; it edits no dispatch table and no `driver.py` line. L5 **relocates that one read**. **The
lanes touch at exactly one line neither unit rewrites**, which is why they are parallel — a measurement,
not the blanket claim that stood here. ⚠ **If L5's scope turns out to absorb `predicates.py` and
`effects.py` into the six steps, U7 gp 1-2 is no longer startable and this row is void** — that scope
lives in the conformance plan's L5 and is **`[UNVERIFIED` from this lane: the file is on PR #386 and
not on `main`]**.

⚠ **`Act.via` is the one place Arc 2 touches this graph.** If G3 slips, **U9 slips with it** — do not
land `via` from the Arc-3 lane to unblock U9. G3 lands it *with* AX-4 clause 2 at the gate, and a
`via` field with no gate check behind it is a dead carrier, which is the defect `04 §F.20a` names.

### §15.2 · The method — cited, not restated

**`workplans/2026-09-09-layer1-conformance-plan.md` §9 is the single owner of the agonist→antagonist
method and it binds every Arc-3 unit unchanged**: four stages per unit (**PRE-FLIGHT → CARVE → ATTACK →
RECONCILE**), none skipped or merged; a relay and not a dialogue, because subagents are stateless and
the critic's value *is* that it never saw the producer's reasoning; and its five rules — a finding is
applied or refuted **by measurement**, a pass that finds nothing has not run *and equally must not
manufacture one*, a falsifier is reproduced **both arms** or it is not a falsifier, a selector is only
as good as the paths you point it at, and **measure at the merge, not at the commit you are standing
on.** Read it there. It is not reproduced here.

**Independence is structural, never declared** (`CLAUDE.md` §10). `.claude/agents/valoria-critic.md`
grants `Read, Grep, Glob` — no `Write`, `Edit` or `Bash` — so a critic dispatched with
`subagent_type: "valoria-critic"` **cannot write**, whatever its prompt says. A sentence inside a
prompt saying *"you are read-only"* restricts nothing.

### §15.3 · **THE ANTAGONIST'S CHARTER — five heads, ruled by Jordan 2026-09-10**

Jordan, this session: *"use an agonist-antagonist methodology where the antagonist ensures adherence to
plan, fidelity to plan instructions, logical correctness, factuality and Layer 1 compliance."*

**This is a widening of the stage-3 brief, and the widening is the point.** The #383 arc's critics were
briefed to attack the *carve* — and a critic asked only whether the code is right will not ask whether
the code is the code the plan asked for. #383 shipped a flat `decision.py` and **no stage-3 pass
objected**, because none of them was pointed at the plan. Every Arc-3 stage-3 dispatch asks all five,
in this order, and **answers each with a measurement or a citation, never an opinion**:

| # | head | what the critic must produce | the failure it exists to catch |
|---|---|---|---|
| **1** | **ADHERENCE TO PLAN** | *Which unit is this, and did it do that unit?* Name every change in the diff **not** in the unit's file list, and every item in the file list **not** in the diff | a unit that quietly widened, or that shipped 2 of a test's 3 breaks and called the suite green (U1's own hazard) |
| **2** | **FIDELITY TO PLAN INSTRUCTIONS** | Each of the unit's stated falsifiers and controls, **reproduced from its recorded recipe**, both arms, with the outcome | *"adversarially reviewed"* with no artifact. §0.1 pt 3: name the falsifier or you have not attacked the result. Step 6's recipe **did not reproduce** and a session following it would have concluded the hazard was overstated |
| **3** | **LOGICAL CORRECTNESS** | Does the acceptance **observe** what it claims? Can the assertion see the failure it excludes? Is the control a control, or identical to the arm by construction? | `pytest engine/tests` cited as a control when it never imports `engine.season` — a **fake control** (§0.1 pt 4, ED-MB-0066). And U4's `tau = 0` arm, which validates plumbing and **not the sampler** |
| **4** | **FACTUALITY** | Open every `file:line`, `::symbol` and quoted string in the commit message against the **working tree at the merge base**. Report each as verified / corrected / unverifiable | this document's own §1 found **19 corrections and 7 material errors** in its planner, then §14 found **a FABRICATED QUOTE used to close its only escalation**. A quotation that is a paraphrase is the recurring defect in this lane |
| **5** | **LAYER 1 COMPLIANCE** | For every file added or moved: **which of `04 §A.2:127-139`'s nine modules is it in, and which `04` line puts it there?** A file with no citation has not been placed. Check by **path**, not by name | `ED-IN-0206` — ten steps of green instruments read as architectural progress they were not, because no stage asked this question. Head 5 is the direct repair |

**Three rules that keep the charter from becoming theatre:**

- **Heads 1 and 5 are answered against `architecture/` and this file, not against the producer's
  summary.** A critic handed only the diff cannot answer *"is this the unit?"* — so stage 3's prompt
  carries the **unit's own section of this document**, verbatim, and nothing about how the diff was
  produced.
- **A null head is a finding and must carry its trail.** *"Head 5: examined all four added files
  against `04 §A.2`; each cites its row; no divergence"* is complete. *"Head 5: fine"* is incompletion
  wearing a finding's clothes. Symmetrically: **do not mint a Layer-1 objection to fill head 5** —
  `04` decides these by citation, so a head-5 finding without an `04` line is not a finding.
- **The output is EDITS, not a document** (`CLAUDE.md` §0). No `audit/` entry, no findings file, no
  per-unit report. At most **one paragraph in the commit message**, and at most **one ledger row, only
  if it needs a human decision** — and before flagging one, run §0's five tests and expect it to close
  at test 3, because `04_CODE_ARCHITECTURE.md` has already decided every structural question Arc 3
  raises.

### §15.4 · Tiering — per call, and the arithmetic rather than a vibe

Subagents inherit the session model, so an un-annotated fan-out on an Opus session runs Opus
everywhere (`CLAUDE.md` §10). Set it per call.

| unit | producer | stage-3 critic | why |
|---|---|---|---|
| **U3** convictions/axes, **U7 gp 1-2** verb rows | `sonnet` | `sonnet` | bounded table authoring against a declared schema; the loader is the judge |
| **U1** provider + manifest row + third gate | `opus` | `opus` | the third-gate amendment is a judgment, and being wrong is silent — it moves R-05's count for the wrong reason |
| **U2** scene tick | `opus` | `opus` | decision 4's skip condition is a **construction**, not a theorem, and its completeness is a claim about the whole read surface |
| **U4** sampler | `opus` | `opus` | the `tau = 0` discontinuity is exactly the kind of error a cheaper tier reports as a control |
| **U5** stance, **U8** ambitions/cast | `sonnet` producer · `opus` critic | `opus` | mechanical to build; U5 has **no byte-identity control**, so the critic carries the weight |
| **U6 / U10** measurements | `sonnet` | `opus` | running the instrument is mechanical; **reading the number is the judgment**, and the falsifier is *"report which channel is still closed and leave both rows `not_met`, honestly"* |
| **U7 gp 3** Dispensation four | `opus` | `opus` | §8's prose→code translation |
| **U9** strategic scale | `opus` | `opus` | the scale-vocabulary problem U9 must *state before it writes* |
| **arc gate** | — | **`fable`**, read-only | `CLAUDE.md` §10 puts `fable` on the audit/guardrail node, never synthesis |

**Do the arithmetic, do not assert the tier**: delegating to a cheaper tier pays only if the delegation
overhead costs less than the drop saves. And three caching facts bite this pattern — parallel agents
sharing a prefix **cannot read each other's cache** (fire one, await its first token, then fan out);
`haiku`'s cache minimum is **4,096 tokens**, the largest on the roster, so a short shared preamble
**silently never caches** there; and switching model mid-conversation **invalidates the whole cache**,
so escalate at unit boundaries.

**Parallel write lanes need `isolation: "worktree"`** — one repo, colliding trees otherwise — and
return **fixed-format summaries**, not raw context. In Arc 3 that is **U3 ∥ U7 gp 1-2** only.

### §15.5 · The end-of-arc gate

One dispatch after U10, `subagent_type: "valoria-critic"`, `model: "fable"`, read-only, carrying the
arc's commit messages and instrument outputs **and nothing about how they were produced**. It is asked
the five heads of §15.3 **over the arc rather than over a unit**, plus the one question a per-unit pass
structurally cannot ask:

> **Did any source-scanning guard silently narrow when a symbol left the file it names?** This has
> recurred at decomposition steps 2, 4 and 5. **Assume it recurred again and look for it.**

**And the honest exit condition, which is not "the rows are green":** Arc 3 is done when the
`measured:` line of every row states what an instrument printed, and the `status:` line agrees with it.
**If reconvergence is still ≥96% at U6, U6's own falsifier governs — report which channel is closed and
leave R-01/R-02 `not_met`.** Both prior plans carry that clause and it is not optional.
