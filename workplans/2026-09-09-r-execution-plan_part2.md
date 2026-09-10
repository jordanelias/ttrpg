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

⚠ **THE HASH AND TEST-COUNT ROWS ARE ARC 1's RESULT AND ARE NO LONGER THE TREE'S (2026-09-10).**
`ED-FI-0009` landed the six investigation acts after this table was written and moved both;
`register --requirements` still reads 6 `not_met` · 3 `partial`. The table stays as Arc 1's record —
*unchanged* was Arc 1's declared success condition and it held — but **a unit must not control against
it. The live baseline has one owner: part 1's §3 · ENTRY STATE**, and this note deliberately does not
copy the values across the split. It is here because §15 is the section a session opens first, and
part 1's correction does not reach a reader who opens part 2 directly.

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

### §15.0d · ⚖️ **THE FABLE ADJUDICATION — §15.0 IS MORE OVERTURNED THAN UPHELD (ED-IN-0211)**

A read-only Fable node adjudicated §15.0–§15.0c against Layer 1 on Jordan's instruction. **Read this
before §15.0 below: five of its load-bearing claims do not survive, and two of the overturns say the
tree had already decided what §15.0 re-opened.** Three were re-verified by hand here before writing.

#### OVERTURNED — and the first two matter most

| §15.0 claimed | Layer 1 says | verified |
|---|---|---|
| **the six antonym closers are NEW ROWS** | **ONE GENERIC `release` VERB**, `eligibility: own`, generic over kind — `04:183` row 14, `04:945` row 15 (*"the loader asserts its domain equals `tenure_kinds \ {contain}`"*), `04:119`, `:345`, `:363`. `01:1121-1136` refuses the per-verb framing **by name**: *"Asking which verb ends an `oblige` is the wrong question… one sentence rather than four verbs."* `HANDOFF_NEXT.md:54` already files it as a **DATA defect**: *"Fix the table, and do not re-open the design."* | ✅ re-read `04:183`, `04:945` |
| **`requires_typed` is not a counterparty test** | **It is the counterparty test the design has.** Form 1 `existence(of: to, kind: Person)` is exactly *"the object of an `oblige` must be an entity"* — checked **by path** at load (`data/requires.py:538-582`) and evaluated **in the fold** (`loop/resolve.py:185-187`), which is where §15.0a says the check belongs. **F8 was a missing CELL, not a missing COLUMN**: `oblige` has `requires: —` and no typed cell | ✅ |
| **the missing `counterparty:` field is the schema gap** | **NON-FINDING.** Layer 1 has three homes, all per-operand: `Act.refs`/`payload` (`04:395`), `requires_typed` forms 1 and 5, and PART D row 13 + typed ids (`04:193-195`, unbuilt — an Arc-2/step-0 gap ED-IN-0206 already records). What actually let the fiat through: `oblige`'s empty cell, the operand aliasing, and untyped ids | ✅ |
| **"only the prose prevents `comply` answering a `dispatch`"** | **`comply` has `requires_typed: none` and no predicate, so the fold RAISES** (`resolve.py:189-200`). The prose is not the blocker | |
| **the Dispensation four are "a complete cycle, the strongest place to build"** | Written as **prose only**: all three responses carry `requires_typed: none`, there is no dispensation operand (`rosters.yaml:873-876`), `writes:` is *"per the term's own row"* with the nine terms **unspecified** (`04:1077` F.15 — *"`issue` produces a document nobody can comply with"*), and `refract`'s side is `absent`. **Blocked on F.15 and H-94, both unruled.** Not the strongest place | |

#### SOFTENED

- **"writes state" ⟂ "is an interaction"** — true of the **table's `writes:` column**, false of the architecture: `tell` *does* write, INTERIOR state at barrier 4 under a different token (`04:117` AX-3, `04:160`). ⚠ And **"interaction" is a coinage that collides with Layer 1's**: `04:396` types `Scene := (…, interactions : Act[])`, so in `04`'s vocabulary **every Act is an interaction**, `oblige` included. That fails `CLAUDE.md` §4's idempotent-meaning test — do not reuse the word this way.
- **Axis 3's "who resists" column CONFLICTS with `04` for all six groups.** `04:669` and `01:353-369` T-g: *"obstruction and scarcity need no verb."* The other party's resistance is **their own later act** — `tell` → the hearer's `refract`; `issue`/`establish` → their `evade / defy`; `petition`/`carry` → the body's `determine`; `levy` → scarcity; `succeed` → rivals contest the **seat at conferral**, a different verb. That is AX-1 + ED-SC-0035 applied.
- **"No corpus act can name two distinct parties"** — too strong. Actor + subject *are* two parties. What cannot form is a **THREE-PLACE** act (actor, office, heir) — which is precisely what broke `succeed`.
- **`hold` "paired, built"** — only the T-o path is built; T-m is why *"a person cannot resign an office"* (`HANDOFF_NEXT.md:54`).
- **U1 upstream of U7** — true for `contests:` rows, false for uncontested verbs whose counterparty is an operand and whose obstacle is scarcity.

#### UPHELD

The false denominator (31 + a placeholder for 6 = **37**, and the placeholder can never execute); `PLAN.md:101`'s *"unnamed"* being stale; F7's self-loop and `04:177`'s holder-owned orientation; the operand aliasing itself; `succeed`'s non-empty refusal column; the `act.refused` zero; **the counterparty check belongs in the fold** (`04:579`); `commit`+`repudiate` landing together.
⚠ **Two of my own citations were wrong**: `_eff_transfer` is at `effects.py:406`, not `:504`; `_eff_move` at `:163`, not `:253`. Only `_eff_confer:112` resolved.

#### TWO NEW HIGH FINDINGS

1. **⚠ THE `Petition`/`Dispensation` CARRIER CONFLICT IS REAL AND UNRECORDED.** `04:180` row 11 rules them **kinds of `Record`**; `write_matrix.yaml:224` and `:112` carry them as their **own kinds**, and `carry`'s typed cell is `kind: Petition`. **ED-IN-0206 does not list this among its non-conformances and no plan carries an item for it.** It is the precondition for the `rescind` and `withdraw` closers, and it changes five rows. ✅ verified by hand.
2. **⚠ `HANDOFF_NEXT.md:55` POINTS THE INVESTIGATION REPAIR AT A MODEL LAYER 1 REFUSES.** It names *"#359's discovery model — a contest of capability against **secrecy**, emitting a Degree"*. `#359` declares `secrecy : Clamped<0,5>` (`proposals/2026-09-03-governance-corpus-rebuild/03-design-v2.md:740`), a stored scalar — and **`01_AXIOMS.md:1001-1002` refuses exactly that**: *"`secrecy` needs no representation at all, because under `AX-2` a claim nobody witnessed is simply unknown and secrecy is the **empty observer set**."* ✅ verified (Fable cited `04`; it is `01`). **The canon doc supplies what #359 does not, in a form `04` accepts:** `fieldwork_v30.md:353-355`'s **Concealment Ob is another person's act, present or absent** — the empty-observer-set model with a live counterparty and no stored scalar.

#### THE FORK: A THIRD OPTION NEITHER I NOR THE ROW POSED

**UNDECIDABLE-AS-POSED.** Both (a) and (b) presuppose a buildable `comply`, and F.15 + the operand famine mean it is buildable for **neither** channel today — **the fork is downstream of F.15.**

> **(c) `dispatch` needs no response verb at all.** The response to an order is **the ordinary act it asks for**, performed by the dispatched member — `holonic:433` §11.1: *"pool(act by remit) = capability of the dispatched establishment member(s) actually performing it."* `effects.py:87-89` and ED-SC-0035 lean this way.

**What it actually turns on: DOES AN ORDER CARRY TERMS?** If yes, `dispatch` is `issue` at person scale and (a) follows. If no, (c) follows and there is no response verb to be one or two. **That is the question for Jordan — not "is `comply` one verb or two".**

#### THE SIX: BUILDABLE FROM CANON, AND WHAT MUST BE INVENTED

Per Jordan's ruling, sourced from `investigation_systems_v30.md` / `fieldwork_v30.md`. **Supplied per act** — pool attribute, precondition/depth gate, the shared degree→outcome table (`fieldwork_v30.md:302-309`), reliability tag: Examine (Cognition, Verified) · Interview (Attunement via the Lattice, Testimonial) · Research (Recall, Documentary) · Surveil (Cognition, Observational, +2 Exposure) · Thread-Read (Spirit, TS≥30, Thread-verified, Coherence −1) · Reconstruct (Recall, own degree table `:276-281`, Derived).

**Must be invented or adjudicated — the real deliverable:**
1. **Every `writes:` cell.** No matrix row exists for Evidence Track, Exposure, Disposition or Case Board, so the loader refuses the rows. Under `04` three are **not fields at all**: Evidence Track is a count over held Claims; Exposure as a per-territory meter is a Rung social aggregate **forbidden at `04:237`**; Case Board is a View. Disposition maps to `tie`.
2. **The degree → claim-confidence path.** WITNESS mints every claim at `confidence_default=100`; nothing turns a Partial finding into a low-confidence claim, and Reconstruct's *"conclusion is wrong at Failure"* needs a claim whose **value is false**.
3. **New `requires` stems** (TS, Disposition, institutional access) — `REQUIRES_STEMS` is closed and refuses an unknown stem at load. A grammar change.
4. **Interview's collapse** of a seven-gate utterance lattice to one resolution — licensed by `rosters.yaml:458-463`.

**Interview is a VERB ROW, not proceedings — DECIDED-BY-TREE.** `investigation_systems_v30.md:229/:233` partitions the Lattice (exploratory) from the Social Contest (adversarial); escalation is a *transition to* a contest, i.e. a downstream second act. ED-SC-0033's twelve games include **interrogation**, not interview; ED-FI-0004 merged Interview into the **Lattice**, not into contests.

**⚠ AND THE SIX ARE NOT BLOCKED ON U1 — they need a DIFFERENT seam.** `rosters.yaml:482` types investigation *"ITS OWN KIND — not a contest"* and `:505-508` forbids giving them a prize: *"Giving them a prize so the existing machinery can grade them is **scripting drift**."* They need the **shared ladder** (`04:122` T-k) and a provider under a **NEW manifest role** — `manifest/registry.py:22` has exactly one role, `"contest"`. U1's σ-leverage wrapper and manifest plumbing are reusable upstream; U1's contest-specific half is not on their path.
⚠ **Which indicts U1 half (b):** it plans `contests:` on `tell`/`speak` — the same *"give it a prize so the machinery grades it"* move `rosters.yaml:505-508` refuses for investigation.

#### THE LOGIC CHECK — SEVEN STEPS THAT DO NOT FOLLOW

The derivation *"a real interaction has a counterparty, an obstacle and a degree, and the antonym is the fourth face"* smuggles in more than the ruling says:
1. **"Some / some / some" → "necessarily all three."** Jordan's second ruling is **partitive**. §15.0's own axis-3 table then lists eight verbs *"legitimately needing none"* — internally inconsistent.
2. **"mechanisms OR interactions" → interactions only.** The first disjunct was dropped. `work` → wear, `utter` → a Proposition: a mechanism with no second party, and not a fiat.
3. **"another entity" → "a counterparty that resists at RESOLVE."** The other entity is already the `subject`/`to` operand; the leap to *obstacle* imports a resolution model `04` reserves for `contests:` and refuses elsewhere.
4. **"undone by ANOTHER party's act" inverts T-m** — `01:1127`: the OWNER ends what they own; T-o is the seat exception.
5. **"a fiat cannot fail on the world's terms"** — the fold's refusals *are* that; `oblige`'s empty refusal column is a **row defect under invariant 4**, not a category.
6. **"a fiat is monotonic, which is why divergence fell"** — a causal claim with **no control** (§0.1 pt 4); the named falsifier (`commit`+`repudiate` moving it the other way) is unrun. A hypothesis.
7. **A fourth counterparty shape breaks "necessarily":** the six's counterparty is the **concealer — optional, found by presence at the scene**, named nowhere on the act.

**What survives:** F7 and F8 are real; the fold is the right site for the check; the counterparty half of the ruling is real **and spellable with existing forms**; the antonym half is real **and already spelled by `release`**.

---

### §15.0 · ⭐ **THE VERB TABLE, MEASURED ON THREE AXES — and the ruling that reorders U7 (ED-IN-0210)**

Measured from `verb_table.yaml` and the loaded `VERB_TABLE`, 2026-09-10. **The ledger row is
`ED-IN-0210`; this section is its working.**

⚠ **FIRST, THE DENOMINATOR IS FALSE. `len(VERB_TABLE) == 32` COUNTS A PLACEHOLDER AS A VERB.**
`verb_table.yaml:490` carries **`"the six investigation acts"`** as one row — `requires: "per act"`,
`writes: []`, loaded as a real key. Its own `requires_typed_note` admits it: *"the cell defers to six
acts the table does not carry as rows."* **31 real verbs + 1 placeholder for 6 unwritten rows = 37**,
and the placeholder **can never execute**, so it permanently inflates every ratio. Asserted at
`corpus_run.py:516`, `probes.py:988`, `test_season_shape.py:8374` and R-05's `measured:` line — **every
"of 32" in this plan and in `requirements.yaml` is wrong, including the ones this arc quoted.**
Layer 1 already named the repair (`HANDOFF_NEXT.md:55` item 2b: *"split into six rows with writes;
#359's discovery model — a contest of capability against secrecy, emitting a Degree — is the shape"*
— ⚠ **the split is DONE (§15.0e); the second clause is what ED-FI-0009 puts to Jordan, and
`rosters.yaml:505-508` refuses the "contest" half of it by name**),
and ⚠ `PLAN.md:101`'s premise for grading them `assumption` — *"they are **unnamed**… nothing to
inject"* — **is stale**: they are named in a CANONICAL doc, `investigation_systems_v30.md:217`/`:427`
— **Examine · Interview · Research · Surveil · Thread-Read · Reconstruct**.

#### AXIS 1 — pairing: what can be undone

| kind | opened by | closed by | |
|---|---|---|---|
| `hold` | `confer` | `revoke` | paired, built |
| `contain` | `move` | `move` | self-paired, built |
| `commit` | `commit` | `repudiate` | paired, **neither built** |
| `oblige` · `succeed` · `tie`/`knot` | each by its own verb | — | **unpaired** |
| `Record.exists` | `create_record` · `forge` · `open_case` | `destroy_record` | paired 3:1 |
| `Site.condition` | `work` degrades | `restore` repairs | paired |
| `Rung.stores` | `transfer` · `levy` · `exchange` | conserved | self-paired |
| `Office.exists` · `Petition.exists` · `Dispensation.exists` | `establish` · `petition` · `issue` | **nothing** | **unpaired** |
| `Proposition.exists` | `utter` | — | **deliberately** — §14 makes it immutable |

**Seven unpaired creators, six closers named by Jordan** (`ED-IN-0210` ruling 2): `waive`, `deposed`,
`fray / loosen`, `rescind`, `withdraw`/`deny`, `abolish` / `dissolve`. **All are NEW rows.**

#### AXIS 2 — mechanism/action vs relationship, and they are ORTHOGONAL

| class | verbs |
|---|---|
| establishes/ends a RELATION (`Tenure`) | `commit` `confer` `oblige` `succeed` `tie / knot` `repudiate` `revoke` `move` `determine` |
| acts on MATTER or a thing's state | `transfer` `levy` `exchange` `work` `restore` `create_record` `forge` `open_case` `destroy_record` `establish` `issue` `utter` `petition` `carry` `convene` `kill / wound` |
| writes NOTHING — pure emission | `speak` `tell` `dispatch` `comply` `evade / defy` `refract` `the six investigation acts` |

⚠ **"Writes state" and "is an interaction" are INDEPENDENT.** `tell` writes nothing yet is a genuine
interaction — it moves a claim into another's ledger. `oblige` writes state and is **not** one. That
orthogonality is why a fiat passes a green suite: the test was on the wrong axis.

#### AXIS 3 — obstacle + degrees, and the two complete cycles already in the table

**Declared today: ONE.** `kill / wound` → `contests: "the body"`, the only `contests:` row.

⭐ **`issue → comply / evade / defy / refract` IS A COMPLETE INTERACTION CYCLE, ALREADY WRITTEN.** All
three responses require *"a claim of the dispensation's terms is in the actor's own ledger"* and emit
`compliance.given` / `compliance.withheld` / `terms.distorted`. **All four are unbuilt, and U7 files
them last as "group 3".** The investigation six are the second such family (#359's capability against
secrecy), de-scoped entirely as "group 4".

**Where an obstacle and degrees are structurally required** — ⚠ **this column is a READING, not a
declaration: nothing in `verb_table.yaml` names a counterparty, and that missing field is arguably the
schema gap the whole ruling implies**: `tell`/`speak` (the hearer), `evade / defy`/`refract` (the
issuer's authority — `refract` is degrees *by definition*), `levy` (the levied), `succeed` (rival
claimants), `petition`/`carry` (the receiving body), `establish`/`issue` (those bound).
**Legitimately needing none** — one party, own resources: `create_record` `utter` `work` `restore`
`move` `commit` `repudiate` `destroy_record`.

#### WHAT THIS REORDERS

1. **The Dispensation four are the strongest place in the table to build, and U7 ranks them last.**
   They fail none of the three tests structurally.
2. **`commit` + `repudiate` land TOGETHER** — the one matched pair both unbuilt; reversible state
   should move divergence the *other* way, which is a falsifiable prediction and the unit's control.
3. **U1 is upstream of U7** (§15.0a).
4. ⚠ **The `dispatch`/`comply` fork is OPEN and is `ED-IN-0210`'s `needs_jordan`.** `comply` keys on a
   **claim in the ledger**, which `dispatch`'s `order.given` already deposits — so the response family
   is anchored to the *artifact* when its mechanism is the *claim*. Either `comply/evade/refract`
   answer both channels, or `dispatch` needs its own obey/disobey pair.

---

### §15.0a · ⭐ **THE RULING THAT SUBSUMES §15.0b AND §15.0c (Jordan, 2026-09-10)**

> **"Verbs invoke mechanisms or interactions between a character and another entity/character.
> They are not fiats."**

**THIS IS THE ROOT OF WHICH F7 AND F8 ARE SYMPTOMS**, and it is why a green 190-test suite could not
see either. The two effects U7 group 1 built were **fiats**: `_eff_oblige` declared *a duty now
exists* by writing an edge; `_eff_succeed` declared *this person is heir*. Neither invoked anything
**between two parties**. So:

- **a fiat needs no counterparty** → nothing checked that `einhir_texts` was an entity, and it is not
  one (F8);
- **a fiat needs no two distinct parties** → a `Tenure(X, X)` self-loop read as lawful (F7);
- **a fiat cannot fail on the world's terms** → the only refusal available was *"the edge is already
  open"*, which is bookkeeping, not resistance;
- **a fiat is monotonic** → hence the absorbing state and the fallen divergence counts of §15.0b.

**SO THE THREE COMPLETION CLASSES ARE ONE THING SEEN FROM THREE SIDES.** A verb that is a real
interaction has, necessarily: a **counterparty** (an entity that is not the actor), an **obstacle**
(what the counterparty or the world sets against it), and a **degree** (how it went). A verb missing
all three is not an unbuilt verb — **it is a fiat wearing a verb's clothes**, and wiring it produces
exactly what this unit produced: state that appears, cannot be resisted, cannot fail, and never ends.
The antonym is the fourth face: what a fiat cannot do is be **undone by another party's act**.

**WHAT THIS CHANGES FOR U7, and it is not a small amendment:**

1. **THE TWENTY ARE NOT A WIRING BACKLOG.** U7 reads them as verbs that merely lack a predicate and
   an effect. Most lack a **mechanism**: who the other party is, what they set against it, and how
   the outcome is graded. That is design work, and it is why the corpus "reaching" a verb is a much
   weaker licence than this arc treated it as — reachability says a candidate forms, not that an
   interaction exists to run.
2. **`requires_typed` IS NOT A COUNTERPARTY TEST.** `oblige` passes the first gate with
   `requires: —` and no typed cell at all, so nothing in the fold ever asks whether the act has
   someone to act upon. **A counterparty check belongs in the fold, not in each effect body** — every
   sibling effect re-implements a partial one (`_eff_confer:112`, `_eff_transfer:504`,
   `_eff_move:253`), which is the "same situation, four verbs, three answers" defect `_operand`'s own
   docstring names.
3. ⚠ **`subject`, `to` AND `site` ARE ONE ALIASED OPERAND** (`decision/options.py:307-312`, all three
   `return subject`). **No corpus-formed act can name two distinct parties today.** So under this
   ruling, *no* two-party verb is currently buildable from the corpus — which is a far more useful
   statement of U7's real blocker than "18 have no predicate/effect", and it was not in the plan.
   `H-94`'s structural half closed the operand channel; it did not make the operands **distinct**.
4. **U1 IS UPSTREAM OF U7, NOT PARALLEL TO IT.** The obstacle (U1/§7) and the degree (U1 half (b) +
   U5) are two of the three faces above. Verbs built before them can only be fiats.

---

### §15.0c · ⚠⚠ **U7 GROUP 1 WAS BUILT, MEASURED, AND REVERTED. TWO HIGH FINDINGS; THE HEADLINE RESULT WAS AN EDGE TO NOTHING.**

`oblige` and `succeed` were carved, the corpus executed them (**6 → 8 of 32**, distinct executed
sets 2 → 4, `PROBE FLIPS 0`, 190 tests green after six adjudicated re-pins), and a read-only critic
then broke the carve on two findings that a green suite could not see, **because the unit added no
test asserting the SHAPE of the edge either effect opens.** Both verified against the tree before
acting:

> **F7 — `succeed` opens a SELF-LOOP, and the orientation is ruled the other way.**
> `decision/options.py:307-312` derives `subject`, `to` **and** `site` from the SAME value — the
> question's referent:
> ```
>     if name == "subject": return subject
>     if name == "to":      return subject
> ```
> So for **every corpus-formed `succeed`**, `_operand(a,"to") == _operand(a,"subject")` and the
> effect builds `Tenure(subject=X, object=X, kind="succeed")` — the heir and the office are the same
> id. ⚠ **And the docstring argued orientation from S15.1, which decides nothing between the two
> readings, while the tree rules the axis it did not check:** `04:177` §A.3 row 8 —
> *"`succeed : Person → Person`, **owned by the holder**"*, forced by `01_AXIOMS.md:1203-1212`
> (*"succession is a disposition of the holder, not a property of the place"*). Neither reading
> admits heir → office. The subject was also a **Record id**, which PART D row 13 (`04:943`) grades
> **STRUCTURAL**: a relation whose subject cannot act. `state/world.py:257` then routed it to
> `w._unowned` — an edge no person owns and nobody can ever close.

> **F8 — `_open_tenure` opened an edge to an id that names NO ENTITY, and that was the headline.**
> `einhir_texts` is the **`subject` field of `prop_einhir`**, not an entity: measured, it is in none
> of `w.persons`, `w.offices`, `w.rungs`, `w.records`, `w.sites` or `w.propositions`. So
> *"Carin Vedel takes a duty toward the suppressed texts she copies"* — reported as this arc's first
> emergent result — **was a Tenure pointing at a bare string.** Every sibling effect in the file
> does the existence check this one omitted: `_eff_confer:112`, `_eff_transfer:504`, `_eff_move:253`.
> `holonic_ARCHITECTURE.md:541` types the kind `oblige : Person → Person | Office`.

**Nine further findings, all applying to whatever rebuilds this**, in descending order of bite:
`succeed`'s `emits_on_refusal` is **`["succession.refused"]`, NOT empty** (`verb_table.yaml:471`), so
the idempotent no-op asserts a failed succession when the designation stands; `oblige`'s empty column
falls back to the **`act.refused` body literal** (`loop/resolve.py:268`), which
`hole_register.yaml:2691` records as **emitted 0 times across 89 baselines** — a load-bearing zero
this unit would silently falsify; the replacement partition assertion pins `min(hi) == 2` where its
own comment measures `hi == {2,3,4,5,6}` (§0.1 pt 2 — it cannot observe the failure it excludes);
two sentences inside the edited block still read *"still exactly two sets"* and *"the executed set is
STILL one"*; `actor_end` is pinned as an **ordered** list the code never sorts; the W-D movement was
filed in **R-05's** `measured:` when the row that owns that instrument is **R-02** (`:153-154`); and
`_REFERENT_OPERANDS` was cited as why `subject` reaches `_eff_oblige` when the real owner is
`decision/choose.py:131-132` (`_payload_of`), because an untyped verb returns `{}` before
`_REFERENT_OPERANDS` is consulted.

⚠ **The critic could execute nothing** (Read/Grep/Glob only), so every stage-2 number stands
unverified by it — and it says so. Six of its own attacks **failed and are recorded as failures**,
including the one that mattered most to this unit: *"striking the season threshold is weakening a
guard to get green"* — **no**, the measurement genuinely falsifies it and re-pinning it looser would
have been worse. That adjudication survives and should be reused, not re-argued.

**WHAT SURVIVES THE REVERT:** the reachability measurement (five verbs reached; `oblige` 4 calls,
`succeed` 3), the six re-pin adjudications, the antonym taxonomy in §15.0b, and the discovery that
**`subject`/`to`/`site` are one aliased operand** — which is the fact that makes any two-operand verb
unbuildable today and was not in the plan.

### §15.0b · ⚠ **U7's GROUPING IS WRONG, AND JORDAN NAMED WHAT REPLACES IT (2026-09-10)**

U7 groups its twenty verbs by *"no hole, merely unbuilt"* against *"hole-gated"*. Executing group 1
showed that partition does not predict anything useful, and Jordan supplied the one that does:

> **"Adding a verb can reduce divergence if its antonym has yet to be built."**
> **"Some verbs will require antonyms. Some will require an obstacle. Some will require degrees of
> success."**

**THE FIRST HALF IS CONFIRMED BY MEASUREMENT, not adopted on authority.** Read the `writes:` column
across all 32 rows:

| Tenure kind | opened by | closed by | |
|---|---|---|---|
| `hold` | `confer` | `revoke` | **paired**, both built |
| `contain` | `move` | `move` | **self-paired**, built |
| `commit` | `commit` | `repudiate` | **paired**, NEITHER built |
| `oblige` | `oblige` | — | **UNPAIRED** |
| `succeed` | `succeed` | — | **UNPAIRED** |
| `tie` / `knot` | `tie / knot` | — | **UNPAIRED** |

**U7 group 1 built exactly the two unpaired openers**, and every W-D divergence count fell
(`none` 6→4, `actor` 8→5, `total` 12→9) with every `genuine` count unchanged. An unpaired opener
writes **monotonic, irreversible** state — an `oblige` edge can never close — so across forks it
converges to the same value. **An absorbing state, which is global to the verb set**, and that is
why `total` moved too. A chooser-side explanation (budget competition) cannot account for `total`;
it is a real second effect and it is not the mechanism.

**THE THREE COMPLETION CLASSES, and every verb belongs to at least one:**

| class | what the verb needs before it means anything | who owns it |
|---|---|---|
| **ANTONYM** | a closer for what it opens, or its state is monotonic and divergence-suppressing | **U7**, and it must build **pairs**. ⭐ **JORDAN NAMED THEM, 2026-09-10: `oblige` ↔ `waive`; `succeed` ↔ `deposed`; `tie / knot` ↔ `fray / loosen`.** None of the three closers exists in `verb_table.yaml` today — they are new rows, not unbuilt ones, which is why `grep release` finds nothing and `04:945`'s generic `release` is unbuilt. Each pair lands together |
| **OBSTACLE** | an `ob` for its resolution to be anything but automatic | **U1** — §7's Operands, and `sigma_leverage` does NOT supply one (§15.0) |
| **DEGREE** | a `contests:` prize and a band ladder, or its outcome is binary | **U1 half (b)** + **U5** |

**WHAT THIS CHANGES, concretely:**

1. **`commit` + `repudiate` are the next U7 unit, TOGETHER.** They are a matched pair, both unbuilt,
   and landing them together adds **reversible** state — which should move divergence the *other*
   way. That is a falsifiable prediction and the next unit's control.
   ⚠ `commit`'s own blocker is upstream (its Q4 source only fires for a person who already holds
   one), so the pair lands when that clears — but they land **together** regardless.
2. **`tie / knot` needs an antonym before it needs a kind ruling.** §15.1 defers it on *which*
   Tenure kind; it is also unpaired, so building either kind alone repeats what group 1 did.
3. **⚠ `U6` MUST NOT BE MEASURED OVER A VERB SET OF UNPAIRED OPENERS.** R-01/R-02 are propagation
   measurements; a verb set that suppresses divergence by construction will read as *less*
   propagation and the number will be attributed to the engine rather than to the roster. **U6's
   precondition gains a clause: every opener in the executing set has its closer built, or the
   measurement says which do not.**

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
| **U7 gp 4** · six investigation acts | — | ✅ **BUILT 2026-09-10, ED-FI-0009** — §15.0e. De-scoped no longer; the DEGREE half is the ruling request |

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

---

> ⚠ **ED-IN-0207 AND ED-IN-0208 IN THIS DOCUMENT WERE RENUMBERED TWICE, ENDING AT ED-IN-0210 AND ED-IN-0211, ON
> MERGE (2026-09-10).** `main` had independently allocated both ids to different subjects — the
> σ-leverage skill split (PR #390) and the blocking-rulings measurement (PR #393) — while this
> branch allocated them to Jordan's verb-table rulings and the Fable adjudication. Both sessions
> read `next_free: 207` and neither saw the other's bump. `main`'s rows are published and cited in
> merged PR titles, so they keep the ids and these moved. A lane tag makes CROSS-lane collision
> impossible by construction; **within** a lane the allocation protocol is still discipline alone,
> and this is what that costs. ⚠ **IT HAPPENED TWICE.** The first renumber moved these rows to
> 0209/0210; `main` then merged PR #392, which had allocated **0209** to the layer-conformance
> skill, so they moved again to 0210/0211. The rule held both times and that is the point — the
> LATER-MERGING side moves, so a published id never shifts under a citation already aimed at it.

## §15.0e — THE SIX, BUILT. What landed, what it moved, and what it did not build.

**`ED-FI-0009`, 2026-09-10.** Jordan, in order: *"'the six investigation acts' is a massive issue:
that is not a verb"*, then *"you must ensure you build the six from investigation systems"*.

### What landed

`verb_table.yaml`'s one row is now six, named by canon at `investigation_systems_v30.md:217` —
**`examine` · `interview` · `research` · `surveil` · `thread_read` · `reconstruct`**. Each carries a
typed `requires` built from the **existing** closed grammar: no new `requires_form`, no new
`requires_operand`, no new predicate stem. ⚠ That contradicts my own `ED-IN-0211`, which said the
build needed *"new requires stems (a grammar change)"*. It did not: `existence` (`exists:<Kind>`),
`relation` (`present_at`) and `own_ledger` (`claim.held`) cover five of the six, and the sixth —
`thread_read` — carries `requires_typed: none` under the loader's own reason (c), an operand the
closed roster has no name for, which is `H-85` and is a citation rather than a new hole.

### What it moved, measured

| | before | after |
|---|---|---|
| verb-table rows | 32 (a placeholder counted as one verb) | **37** |
| resolvable by the fold | 12 | **17** |
| **executing in the corpus** | 6 | **10** |
| distinct corpus behaviours, 89 live cases | 2 | **16** — the six alone carry 2 → 10, the new `alignment` cells 10 → 16 |
| §F1 clause-4 drops, 89 worlds, shipped default | **25, every one `move`** | **1,104 decision-affecting, five verbs** (1,491 raw) |
| — predicates clause 4 can fire on | **1** (`contain.path`) | **5** (`+ exists:Site · Record · Person · Rung`) |
| `W-D` acceptance, NPC-088 2-slot slice | 0 of 16 forks diverged | **14 of 18** |
| corpus cases | NPC-086 `BLOCKED`, NPC-010 3 blockers | NPC-086 **`DEGRADED`**, NPC-010 2 |

⚠ **THE CLAUSE-4 `before` FIGURE IS 25 BECAUSE IT WAS MEASURED, AND THE FIRST WRITING OF THIS
TABLE SAID 13.** The 13 was quoted from `test_wb_clause_four_fires_…`'s docstring, which put a
QUOTED number and a MEASURED one on either side of one ratio — the asymmetry §0.1 pt 4 names, in
the headline of this section. Both sides are now one script (a wrapper on `belief_contradicts`
over all 89 corpus worlds at `DEFAULT_FIXTURES`), run at `d59c3e1` in a throwaway worktree and
again on the commit. Two consequences: the ratio is smaller than published, and `move` itself
**FELL, 25 -> 18**, where the quoted figure had it rising. The channel is not lost — 18 firings,
and `travel.blocked` still fires — but the fall is real and is UNDIAGNOSED. ⚠ The tree carries two
further figures for this same quantity, unreconciled: the docstring's 13 (86 worlds, an earlier
instrument) and `test_wd_a_fork_…`'s corpus table, which reads **0** at the shipped cell via
`wd_extra.corpus_drops`. Three instruments, three answers; only the 25/1,491 pair is like-for-like.

The clause-4 line is the one that matters, because the tree had already written down what it would
take: *"The defect this exposes is that §F1 clause 4 has exactly ONE reachable instance in the
corpus; that is a producer hole and is where the work goes."* The six gave the grammar four more
live cells — `exists:Site` · `exists:Person` · `exists:Record` · `exists:Rung`.

⚠⚠ **AND THE FIRST WRITING OF THIS PARAGRAPH PICKED THE ONE EXAMPLE THAT IS FALSE, WHICH IS WHY THE
TABLE ABOVE NOW CARRIES TWO NUMBERS.** It read: *"`restore`, a verb that cannot execute, now drops
on beliefs a failed `examine` deposited: one person's failed look teaches them not to try to mend
the thing."* The belief is real; the behaviour is not. `restore` is not in `resolvable_verbs()`, and
`choose.py` applies the `verbs=` filter **after** `opening_set` returns — so clause 4 drops a
Candidate that was never going to be offered, and nothing any person does changes. **387 of the
1,491 are inert; the decision-affecting figure is 1,104 across five verbs.** Measured further:
`examine` and `restore` fire on the **identical eight subjects**, because their cells are the same
shape — one belief counted under two verbs, not two findings. The sentence is withdrawn.

**What survives is the predicate row, and it is the better claim anyway**: clause 4 could fire on
ONE predicate before (`contain.path`, via `move`) and can fire on FIVE now. The monoculture is what
broke. Counting verbs overstated the breadth; counting predicates does not.

### What it did NOT build — and the escalation I filed for it, withdrawn the same day

Nothing resolves a **degree** for an investigation act, so their `emits:` is flat — while
`fieldwork_v30.md` §4.2 grades every one of them on four bands. `rosters.yaml:482` types
investigation's seam `UNRULED | UNRULED | UNRULED — ITS OWN KIND, not a contest`, and `:487-491`
rules what a session may do about that: *"the blanks are Jordan questions, not session guesses:
writing a plausible IN/OUT for a mode nobody has ruled would be inventing the architecture rather
than recording it, and the seam is precisely the thing that must not be invented."*

I filed ED-FI-0009 as four questions that are one question, `needs_jordan: true`. **All four are
answered inside the tree and the flag is withdrawn.** §0: *"`needs_jordan` means Jordan is the only
person who can answer this, not nobody got around to it."*

| I asked | the tree already answered |
|---|---|
| what is investigation's seam? | `workplans/2026-09-06-season-loop-execution-plan.md:647` ran this blank through the same five tests four days earlier and closed it at **test 3**: *"NOT A SEAM. The loop IS the mechanism"* — RESOLVE → WITNESS, out = *"Claims graded by degree; Failure emits `finding.none` and deposits nothing"*, **work item 4.5**. The six rows already ship that refusal half verbatim. I cited `rosters.yaml`'s seam table and never asked who else had cited it. |
| may `capability` gate, since canon contradicts canon? | **An equivocation, withdrawn.** `fieldwork_v30.md:76` is the *Perception gates* paragraph and governs **depth access** — its examples are the Depth-1/Depth-2 gates from the table at `:34-35`, and Depth 0's gate is *None*. Canon does not say a low-Cognition character cannot Examine; it says they cannot reach Hidden content by examining. `#353 §9.2` forbids gating a **verb**. Compatible. **Test 5.** |
| what supplies the obstacle? | Follows the first: the producer is item 4.5. The GM-set Evidence-Track threshold is answered by the engine's own premise — *"There is no GM — the engine resolves everything."* **Test 5.** |
| where does Exposure land, given `04:237`? | **Test 4, by precedent.** `01_AXIOMS.md:1001-1002`: *"secrecy needs no representation at all … secrecy is the **empty observer set**."* Conspicuousness is that quantity with the sign reversed — the **size** of the observer set, which WITNESS already computes per Event. `04:237` is not the obstruction; it is why a per-territory meter was the wrong shape. |

**What is left is work, not a ruling: item 4.5**, a degree producer at RESOLVE → WITNESS. Its own
blockers are `W27`'s cast (no attribute values on any person), the absent Depth carrier, and
`§27.4`'s refusal to route an uncontested attempt to an `Ob = 0` roll.

### How the scope was cut, which is the method working

The first carve was larger: an `obstacle:` column on the verb row, a `seam/attempt.py` producing a
margin from `roll_pool`, a branch in `loop/resolve.py`, `Person.capability` read for a pool and
gating a derived depth. A read-only critic (`.claude/agents/valoria-critic.md`, structurally
Read/Grep/Glob) **overturned four of those five** against surfaces I had not cited —
`rosters.yaml:481/:487-491/:505-508`, `#353 §9.2`'s explicit *"if you find yourself writing
`if capability < N` inside an option set, you are re-implementing a gate the design deleted on
purpose"*, and `§27.4`'s *"an uncontested attempt routes to a gate, never to an `Ob = 0` roll"*. It
also killed the depth derivation on its own terms: canon predicates depth on the **content dug for**,
not on the digger, so *"depth = the deepest gate the actor passes"* would have made raising an
attribute **raise** the obstacle. Every overturn was re-verified at source before the carve was cut
back. Two of its findings were kept as work rather than as notes: loader invariant 12 was **one-sided**
(it read `writes:` and never `emits:`, so the six's exact shape loaded clean and raised mid-corpus),
and the six landed **conviction-inert**, which was measured to displace `tell` by the alphabet before
weighted `alignment` cells replaced it.
