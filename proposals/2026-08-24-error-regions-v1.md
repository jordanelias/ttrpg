# Error regions from the 2026-08-24 hub-and-bus session — executable plan

## Status: PROPOSED (Jordan-requested, 2026-08-24). Ratifies on merge per CLAUDE.md §2.

> **Why this document exists despite §0.** CLAUDE.md §0 forbids the adversarial pass from creating
> documents — its output is edits plus at most one commit paragraph. Jordan asked for this one
> directly ("write down every region of error… in the form of a plan item to be executed in a new
> session"), which is a Jordan deliverable, not a pass artifact. It is written to be **executed and
> deleted**, not maintained. If a session finds it still here with every item closed, delete it.

**Source.** One session on branch `claude/hub-and-bus-contract` (commits `5cd99ee`, `f34d579`,
`d781459`, `8def4e7`, `cd11a23`, `783dab2`, `cd25ec0`), plus four read-only Fable-5 critics
dispatched against that session's own published claims. Every item below is a defect that **shipped
or was published**, not a hypothetical.

**The one-line finding.** Of the six defects the critics found, **four were the instrument's model of
the registry, not the engine** — and every one of them produced a *plausible finding* that would have
driven real work in the wrong direction. The generator is no longer "apparatus guards apparatus"
(§0.3's T3, disarmed); it is **measurement whose subject is a declaration rather than an execution**.

---

## R1 — DISCRIMINATORS THAT DO NOT DISCRIMINATE

**The master pattern, and the reason this document is ordered by it.** Six times this session a
classifier, filter, or predicate was built, trusted, and used to drive a bulk operation or publish a
number — and it separated something *other than* what its name claimed. Twice it drove a bulk
operation that had to be reverted in full.

| id | the discriminator | what it actually separated | cost |
|---|---|---|---|
| R1.1 | work-item classifier v1 | what a row **cites** (matched the `source:` field) | culled **149** rows incl. `ED-IN-0014` "Key the silent emitters" — *the hub-and-bus gap itself*. Reverted. |
| R1.2 | "terminal status ⇒ no live question" | whether the row's **work** finished, not whether its **question** was answered | cleared **17** rows; `ED-PC-0016` is `ratified` while `weapons.py:911-920` still says "a design call held for Jordan". Reverted. |
| R1.3 | emitter attribution by directory name | tree layout vs **logical** contract names | published "0 of 60 declared emissions happen" — true of the scheme, false of the engine |
| R1.4 | longest-prefix path match (unordered) | a parent directory swallowed a sibling | battle Keys attributed to `peninsular_strain`, which never emits |
| R1.5 | stack walk "first frame a contract claims" | the first **claimed ancestor**, i.e. a caller | laundered an unclaimed emitter onto a bystander |
| R1.6 | exporter type filter `'.' in t` | dotted strings, silently dropping `{type: "*"}` | **13 phantom drift findings**; one step from transcribing 13 type names into a contract that already declared a superset |

**LESSON (bind this).** *Name the predicate by what it actually separates, then find one case on each
side that it must get right, and check those two by hand before it drives anything.* R1.1 and R1.2
each had a single counterexample discoverable in under two minutes; neither was looked for, because
both discriminators were **plausible**. Plausibility is the failure mode, not carelessness.

**LESSON 2.** *A discriminator demonstrated wrong must not drive a bulk operation — and the revert is
total, not surgical.* R1.2 was reverted in full even though only 2 of 17 were proven wrong, because
the predicate that selected all 17 is the thing that failed.

### Plan items

- **R1-A. Re-do the ledger triage row by row, or not at all.** The 17-row clearing is reverted; the
  queue is back to **154**. Do NOT re-clear by status. For each candidate row: read the row's *full
  description* for the words "held", "needs Jordan", "escalated", "not taken", "pending", and grep the
  code it names for the same. Close only rows where the successor is **cited by id**.
  *Files:* `registers/editorial_ledger*.jsonl`, `tools/triage_work_items.py`,
  `systems/combat/combat_engine_v1/weapons.py:908-921`, `systems/combat/combat_engine_v1/config.py:81`.
- **R1-B. Give `tools/triage_work_items.py` a self-test with known-answer rows.** Pin `ED-IN-0014` and
  `ED-IN-0004` as CODE and `ED-PC-0016` as *still open*. A classifier with no known-answer fixture is
  not falsifiable.
- **R1-C. Reconcile the two proven-wrong dispositions.** `ED-PC-0016` (half-sword auto-switch,
  duel-aware decision) and `ED-PC-0049` (`ADEF_POINT` 1.2 vs escalated ~1.53) are **genuine Jordan
  calls**. They belong in the escalation set, not the cleared set.

---

## R2 — ASSERTIONS THAT CANNOT OBSERVE THE FAILURE THEY EXCLUDE (§0.1 pt 2)

Four instances, one of which had been green over a dead ratified mechanic.

- **R2.1** `engine/tests/test_knots_ed912.py::test_ed912_break_disposition_…` asserted
  `c["conviction_scar"] == 1` — the **announcement dict knots.py writes for itself** — while the scar
  store was never touched. Two halves agreeing with themselves. ED-912 §6.1 was a no-op and the test
  was green.
- **R2.2** `test_a_caller_is_not_credited_as_the_emitter` v1 asserted *"the attributed module binds a
  path"*. `peninsular_strain` binds a path — so the guard was **green over the exact bug it was
  written for**. Fixed only by recording the emitting file separately from the matched frame; fold
  them and a laundering walk is self-consistent.
- **R2.3** `_triage`'s `declared_by.get(t) or list(wildcards)` made `undeclared_type` **unreachable**
  on the consume side. The tool reported the hard floor MET. It is now RED, hiding two real gaps.
- **R2.4** (earlier this session) `test_the_exemption_does_not_shrink_the_ED_universe` called a
  nonexistent function behind `hasattr`, so its `>= 1190` floor had **never executed**.

**LESSON.** *Write the mutation before the assertion.* For every new guard, state the one-line change
that must turn it red, apply it, and confirm. Four of these four were caught only by doing that
afterwards — R2.1 and R2.4 by accident, months late.

**LESSON 2 (the sharper one).** *Assert on the STATE the mechanic changed, never on the reporting
value the mechanic's own caller wrote.* R2.1's dict and R2.3's fallback are the same error: the
system was allowed to grade its own homework.

### Plan items

- **R2-A. Sweep `tests/valoria` and `engine/tests` for the R2.1 shape** — assertions on a
  `consequences`/`result`/`report` dict written by the code under test, where no corresponding state
  read exists in the same test. Fix by adding the state read; do not delete the dict assertion.
  *Files:* start from `engine/tests/test_knots_ed912.py:105-166` as the worked before/after.
- **R2-B. Sweep for `hasattr(...)`-guarded assertions** (the R2.4 shape) — a guard that silently
  skips is a guard that never ran. *Files:* `tests/valoria/test_ed_citation_scope.py` as precedent.

---

## R3 — NUMBERS THAT ARE CIRCULAR OR SYNTHETIC

- **R3.1** Published "**108 declared / 13 matched**". Folding wildcard expansion into `declared` makes
  `matched == observed` **for that module by construction** — the number cannot fail. All 13 were
  `articulation_layer`, which declares `consumes: []` and matched only itself. Honest figures:
  **82 declared / 13 observed / 0 matched**.
- **R3.2** `fieldwork_knots` was credited with 13 declared consume edges. It has **zero
  `.subscribe(` calls anywhere in the tree** — the only production subscriber is
  `engine/cross_scale/articulation.py:169`. 26 of the 108 were synthetic.

**LESSON.** *Before publishing a conformance/coverage number, ask: what would make this number go
DOWN? If nothing can, it is not measuring conformance — it is measuring that the plumbing ran.*

### Plan items

- **R3-A. Audit every ratchet and coverage constant in the tree for the R3.1 shape.** A count whose
  denominator is derived from its own numerator is unfailable. *Files:*
  `tests/valoria/test_engine_params_bridge.py` (`AUTHORED_PARSERS`, `ENGINE_READERS`),
  `tools/contract_runtime_conformance.py` (`UNDECLARED_TYPE_MAX`),
  `tools/validate_ed_citations.py` (`BURN_DOWN_MAX`, `UNRESOLVABLE_CEILING`),
  `tests/valoria/test_engine_does_not_import_systems.py` (`BASELINE_TOTAL`, `NESTED_BASELINE`).

---

## R4 — CLAIMS OF NOVELTY OR ENFORCEMENT THAT DO NOT EXIST

- **R4.1** Published *"nothing in the tree has ever asked the engine what it actually emits."* **False.**
  `engine/tests/test_parliamentary_bridge.py:136` golden-pins
  `_ON_KEYS_BY_TYPE = {'scene.battle_concluded': 80, 'scene.contest_resolved': 105,
  'da.public_governance': 2}` on a seeded campaign. The real novelty is narrower: nothing compared
  observed emissions **against the contract registry with per-module attribution**.
- **R4.2** `tools/contract_runtime_conformance.py`'s docstring said `--check   # ratchet (CI)`. It is
  wired **nowhere** — not `valoria-ci.yml`, not `valoria_local.py`, not `ci_checks_registry.yaml`.
  This is the §11 defect class: doctrine asserting an enforcement that does not exist is worse than
  none, because it stops the next reader from checking.
- **R4.3** `DECLARED_ONLY_MAX = None  # set by --pin on first run` referenced a `--pin` flag `main()`
  never implemented.
- **R4.4** (earlier) Declared CI **green** from a `curl` to `api.github.com` that returned **HTTP 403**;
  the grep found no failures *in the error body*. Three jobs were still running.

**LESSON.** *Before writing "nothing does X" or "this is enforced", grep for X and read the wiring.
A negative existential and an enforcement claim are the two claim types this repo is worst at, and
both are cheap to check.*

**LESSON 2.** *Absence of a failure string is not evidence of success.* R4.4 is the general case:
verify the **transport succeeded** before interpreting its payload.

### Plan items

- **R4-A. Decide whether `contract_runtime_conformance.py --check` gets wired.** It exits 1 today
  (two undeclared types, R8.2). Options: declare the two types in `module_contracts.yaml` and wire it
  blocking; wire it report-only; or leave it manual and delete the ratchet language. **Do not leave
  the docstring claiming CI.** *Files:* `tools/contract_runtime_conformance.py`,
  `.github/workflows/valoria-ci.yml:270-281`, `tools/valoria_local.py:60-66`,
  `references/ci_checks_registry.yaml`.
- **R4-B. Sweep the tree for "nothing/no tool/never" claims about the tree itself** and check each.
  CLAUDE.md §0.3 records 13 countable figures, none guarded (`ED-IN-0156`, still open).

---

## R5 — INVENTING CANON WHILE APPEARING TO IMPLEMENT IT

The most dangerous region, because the output looks like centralization.

- **R5.1** Shipped `CONVICTION_ALIASES = {'Reason': 'Scholastic', 'Autonomy': 'Liberty'}`, justified
  in a comment as *"a rename rather than a design call"*. **Two authored surfaces refuse that
  mapping**: `systems/characters/conviction_taxonomy_v30.md:282` ("Reason (legacy tag) | composite —
  see PP-685 per character") and `references/alias_registry.yaml:658-663` (legacy list, **no**
  canonical target, "Per-character migration in PP-685"). `Autonomy` appears in neither. The alias
  decided a ruling by accident — the exact act the adjacent comment claimed to refuse for
  Survival/Power. **Deleted.**
- **R5.2** `systems/world/sim/npe.py` carried `opposites = {"Faith": "Reason", "Order": "Survival",
  "Justice": "Power", "Loyalty": "Truth"}` + inverses — **six of eight names non-canonical**. Once
  `CONVICTIONS` became canonical this could **mint** names `resolve_conviction` raises on. The pairs
  are not salvageable by renaming: `Justice↔Power` is an opposition **no taxonomy in the corpus
  states**. Replaced with a uniform draw over the other twelve.
- **R5.3** `knots.py` now scars `conviction='Honor'`. Defensible (Honor's gloss is "pledged oath…
  binding"; taxonomy §8 D1 ratifies Honor for pledged-bond material) but **canon names no Conviction
  for ED-912 §6.1** — this is a session call, not a transcription, and it is not marked as one.

**LESSON.** *When two surfaces decline to state a mapping, that silence IS the ruling — it means "not
decided", not "obvious". Implementing the obvious-looking value converts an open question into
shipped canon with no ledger row and no reviewer.*

**LESSON 2.** *A centralization that must invent a value to complete itself is not finished; it has
found a Jordan question. Stop and record it.*

### Plan items

- **R5-A. Mark `Honor` as a session design call or get it ruled.** Either add a ledger row
  (`ED-FI-*` or `ED-PC-*`) recording that ED-912 §6.1's Conviction was chosen, not transcribed, or
  route it to Jordan. *Files:* `systems/fieldwork/sim/knots.py:349-363`,
  `systems/fieldwork/knots_v30.md` (Scar rows), `systems/characters/conviction_taxonomy_v30.md` §8.
- **R5-B. Cook the 13×4 conviction-axis matrix into an artifact.** It is the grounded answer to "what
  is the opposite of Conviction X" that R5.2 had to stub. Registered as `map.conviction_axis`
  (`references/descriptor_registry.yaml:258`), authored in
  `systems/characters/conviction_axis_matrix_v30.md`, cooked **nowhere**. Same pattern as
  `conviction_roster`: registry → `tools/export_descriptors.py` → `descriptors.json` →
  `engine/substrate/descriptors.py`.
- **R5-C. Grep `systems/` and `engine/` for other ungrounded pair/opposite/antonym maps** built on
  retired vocabularies. R5.2 survived a roster centralization *in the same commit*.

---

## R6 — ARITHMETIC AND CITATION ERRORS INSIDE MY OWN CORRECTIONS

Small, but they were in the documentation of the fix, which is where a later reader trusts most.

- **R6.1** `references/descriptor_registry.yaml` said the nine-name roster had *"4 of them appear in
  no canonical set"* — it is **3** (Reason, Autonomy, Continuity) — and *"5"* for npe's eight — it is
  **6** (only Faith and Order are canonical). Both corrected.
- **R6.2** Cited `engine/tests/test_pipeline_reach.py:152` for **world-npcs**; :152 is **world-knots**,
  world-npcs is **:135**. Both are honest-deferrals so the conclusion held, but the citation was wrong.
- **R6.3** A caller-attribution comment block was pasted **twice verbatim** in
  `tools/contract_runtime_conformance.py`.

**LESSON.** *Recount every number you put in a comment or commit message, from the data, at write
time. A count inside an explanation is trusted more than one in a report and checked less.*

---

## R7 — THE PROSE-COUPLING TAX (measured, three times in one session)

`tests/valoria/test_flow_skeletons.py::test_anchors_resolve` requires every `` `path:line symbol` ``
anchor in 10 `.md` flow skeletons to land on its symbol. Editing **five `.py` files** drifted **236**
anchors and turned 9 subsystems red; a later one-file fix drifted **38** more; the `npe.py` fix drifted
**38** again. Each time the tree was green only after a mechanical remap.

**The tension, stated fairly.** The gate enforces a real property (a skeleton was *traced*, not
recalled), and its own docstring argues that losing it makes the skeletons unfalsifiable decoration.
Against that: its downstream artifact `references/engine_atlas.json` has **zero readers under
`engine/` or `systems/`**, so by §0.1 pt 5's load-bearing predicate it guards a process-only artifact;
and it makes prose freshness a **blocking precondition of every code edit**, which is §0.3's T-terms
pointed directly at the game.

### Plan items — **this is a Jordan call, not a session call**

- **R7-A. Choose one:** (a) retire `tests/valoria/test_flow_skeletons.py` and banner the skeletons as
  an unmaintained snapshot; (b) keep it and ship `tools/restamp_flow_anchors.py` so the tax is one
  command (accepting that a restamper weakens "was it traced" to "does the symbol exist"); (c) keep
  it and generate the anchors from code instead of hand-authoring them.
  *Files:* `tests/valoria/test_flow_skeletons.py` (379 lines, read the docstring first),
  `systems/_architecture/subsystem_flow_skeletons_v1.md`, `tools/build_engine_atlas.py`,
  `references/engine_atlas.json`.
  *A working remapper exists from this session and is the seed for (b) — it builds an OLD→NEW line
  map with `difflib` against the pre-edit blob rather than re-guessing lines.*

---

## R8 — REAL DEFECTS FOUND IN PASSING (not mine; must not be lost)

These surfaced during the audit and belong to the game, not to this session's errors.

- **R8.1** `systems/fieldwork/knots_v30.md:189` says the Close-Knot-break Scar goes **"+1 to both
  partners"**; `apply_knot_loss` scars only the single `actor` passed
  (`systems/fieldwork/sim/knots.py:317,361`). Canon-vs-code; §0.05 says decide and change the code.
- **R8.2** `scene.accord_echo` and `meta.cascade_cluster_event` are **in the Key vocabulary**
  (`engine/engine_params/key_types.json`) and **no module contract names either**, on either side,
  while `engine/cross_scale/articulation.py:125,129` subscribes to both. This is what R2.3 was hiding.
  `scene.accord_echo` is one dormant branch from being emitted (`echo_transport.py:354`).
- **R8.3** `references/module_contracts.yaml:814-817` says `da.*` has **"ZERO emitter code"**;
  `systems/factions/sim/parliamentary_transfer.py:230` emits `da.public_governance`. Stale registry note.
- **R8.4** `ED-SC-0004` is **code-vs-code**, not doc-vs-doc: two Argue-pool formulas are both live
  (`systems/social_contest/sim/contest/primitives.py:211` and `contest_legacy_stub.py`). **§0.05
  cannot arbitrate between two code surfaces** — this is a genuine Jordan fork, and my triage
  mis-filed it as "answered by §0.05".
- **R8.5** Mass-battle armour: the type-dependent cells the two tables disagree over are implemented
  by **neither** surface — the live engine uses a type-blind `dr=1`
  (`tests/sim/mass_battle/equipment/armour.py:17,37-40`). §0.05 does not answer a conflict when the
  code implements neither value; that is a design gap.

**LESSON (this is the correction to my own §0.05 application).** *"The code is the formula" resolves
doc-vs-code. It does NOT resolve doc-vs-doc when the code implements neither value, and it CANNOT
resolve code-vs-code. Before filing a row as "answered by §0.05", check that the code implements
exactly one of the disputed values.* My triage filed **20** rows this way; at least 3 of 3 tested
were misfiled.

---

## R9 — THE GRADED SURFACE (§0.3's T2) — still unaddressed by every plan

From a full read of the plan corpus: **no plan closes T2, and two say so explicitly.**

- `proposals/2026-08-20-return-to-game-plan-v1.md` §6: *"T2 is only half-addressed… Rewriting the
  reward is a Jordan decision… deliberately not attempted here."* The Stop hook has since been
  **emptied** (culling wave 3), which deletes the apparatus-facing grade **without installing a
  game-facing one**. T2 is now vacuum, not fixed.
- `proposals/2026-08-21-execution-order-v1.md` §3a finding 2: **"no game regression can currently red
  CI"** — `m1_acceptance.py` is one of 12 `level: 5` rows that cannot fail the build. The doc calls
  it "the most consequential item on this page." Nothing has executed it.
- `tools/m1_acceptance.py` still declares row 4 DOC-DERIVED and rows 3/5 partial/blocked, so the one
  game signal is **structurally incapable of a green verdict**.

**The two concrete closures both exist on paper and neither has an owner:** wire `m1_acceptance`
rows 1–2 (the execution-bound ones) into a **blocking** tier; and execute **S10** (zero-assertion
counters — `faction_action_errors` / `scene_resolver_errors` appear nowhere in `engine/`).

### Plan item

- **R9-A. Make one game regression able to red CI.** This is the smallest change that moves T2 and it
  is the throughline of every other item here. *Files:* `tools/m1_acceptance.py:297-319`,
  `.github/workflows/valoria-ci.yml`, `references/ci_checks_registry.yaml`,
  `proposals/2026-08-21-execution-order-v1.md` §3a.

---

## R10 — THE SESSION'S OWN OUTPUT RATIO

Measured on this branch vs `main`:

| area | net lines |
|---|---|
| `tools/` (apparatus) | **+904** |
| `tests/valoria/` (apparatus tests) | **+436** |
| generated artifact + registries + CI | +562 |
| prose `.md` | +79 |
| `engine/tests/` (game tests) | +42 |
| **game code (`engine`+`systems` .py)** | **+120** |

**11 lines of apparatus per line of game code**, in a session whose subject was centralizing the
game, under rulings recorded the same day. Tree-wide the ratio is now 1.53:1 (down from §0.3's 3.9:1),
but `tests/valoria` (**29,602 lines**) is the size of all game code (**30,159**) while `engine/tests`
— the suite that executes the game — is **4,060**.

**LESSON.** *An instrument that measures the game is still apparatus. "Load-bearing on the game" (§0.1
pt 5) licenses building it; it does not make building it game work.* The honest accounting is that
this session produced one game fix (the Conviction roster + a revived ratified mechanic) and a large
amount of measurement about why more is not wired.

### Plan item

- **R10-A. Next session's first commit touches `engine/` or `systems/` and moves an execution
  number.** The enumerated list exists: **31 declared emit edges belong to modules that have code and
  emit nothing**, and **five of them already have a live subscriber** (`mechanical.mission_shift`,
  `state.scar_acquired`, `meta.knot_formed`, `scene.combat_resolved`, `scene.combat_felled` — all
  subscribed at `engine/cross_scale/articulation.py:116-130`). Wiring one moves `observed` from 3 to
  4, which is falsifiable. *Files:* `tools/contract_runtime_conformance.py` (run it first),
  `engine/autoload/game_state.py`, `engine/cross_scale/echo_transport.py`.

---

## R11 — GAME CODE FILED WHERE THE GAME CANNOT REACH IT

Two Fable critics were sent at `tests/` and `audit/` with one question: *what in here should actually
be game code?* Both found the same shape — **not misplaced tests, but misplaced mechanisms.**

### R11.1 — An entire engine lives under `tests/`

`tests/sim/mass_battle/` is **11,342 Python lines across 28 files** — `orchestration.py` 2,864,
`hierarchy/units.py` 2,571, plus geometry, per-cell morale, perimeter, Lanchester signature,
equipment and troop-type models. `systems/mass_battle/sim/`, which the **campaign actually runs**, is
**2,420 lines**.

Evidence it is game, not archive: `tests/valoria/test_degree_ladder_single_owner.py:25-27` calls it
verbatim *"the canon mass-battle engine (`tests/sim/mass_battle/`)"*; **43 of 156 `tests/valoria`
files import `mass_battle.*`** (~5,900 lines of behavioural tests pointing at it); every recent ED-MB
batch landed there. `engine/sim_reference_README.md:27-29` records the split with a **stale**
"last advanced 2026-07-08" stamp and a "largely frozen archive" framing that is false of this subtree.

**This is why my 30,159-line "all game code" figure in R10 is wrong.** The game's best battle model was
outside the measurement, outside `engine/`+`systems/`, and disconnected from the campaign that ships.

- **R11-A.** Move `tests/sim/mass_battle/` into `systems/mass_battle/`. The move is mechanical; the
  **reconciliation is not** — *which* engine `resolve_mass_battle` runs is a real MB-lane design call,
  and it is the same question Critic D independently named as the largest unexecuted game work
  (the J2 canon-engine migration, adapter with `degree_map` never built).
  *Files:* `tests/sim/mass_battle/`, `systems/mass_battle/sim/`, `engine/sim_reference_README.md:27-29`,
  `engine/mc_v18_walkthrough.md:81`, `registers/handoffs/HANDOFF_MB.md`.
- **R11-B.** Correct `sim_reference_README.md`'s stale stamp and frozen-archive claim (R4 class).

### R11.2 — A ratified formula the code does not implement — **in a file I edited today**

`systems/fieldwork/knots_v30.md:37` gives the Knot Pool as `(Spirit × 2) + History(Relevant) + 3,
min 5` (PP-632, ED-FI-0005). `systems/fieldwork/sim/knots.py:216` computes
`pool = (spirit * 2) + history_rel` — **no `+3`, no `min 5`**. The doc contradicts itself (`:76` gives
the un-augmented form, which the sim cites at `knots.py:57`).

`tests/valoria/test_knot_pool_formula.py:7` states *"There is no sim/ oracle that computes the Knot
Pool, so this is a doc-content guard."* **That premise is false**, so the test pins three prose
surfaces and stays green while the game plays the un-ratified variant.

- **R11-C.** Apply the ruling in `knots.py:216` (or rule `:76` correct and fix the doc), then re-point
  `test_knot_pool_formula.py` at the code. Under §0.05 the code is the formula — so today the game
  *is* the `:76` variant, and that is a decision nobody made.
  **Note it sits ten lines from the ED-912 Scar path I fixed this session and I did not see it.**

### R11.3 — A re-formed guard chain, depth 4

`game ← tests ← tools/ci_vacuous_assertion_check.py` (scans assertions inside `tests/valoria` +
`engine/tests`; the **only** `layer: L2` row in `references/ci_checks_registry.yaml:34,413-419`)
`← tests/valoria/test_vacuous_assertion_check.py` (175 lines guarding the scanner). Same shape as the
deleted `test_wf_harness_check.py`, one rung shallower and report-only. Adjacent:
`test_known_red_register.py` (111 lines) guards a register of failing tests.

**Apparatus-subject tests measured at ~51 files / ≈10,800 lines — ~36% of `tests/valoria`** — *after*
crediting the bridge/exporter/milestone/§11 guards to the game side. Largest single block: **~2,700
lines guarding `skills/valoria-vector-audit/scripts/`**.

- **R11-D. Apply §0.1 pt 5's predicate to that ~10,800 lines** — but NOT to
  `ci_vacuous_assertion_check`.

  ⚠ **CORRECTED 2026-08-24 by an adversarial relay. The first version of this item named
  `test_vacuous_assertion_check.py` as a delete candidate. THAT CONTRADICTS A STANDING JORDAN
  RULING**, and the ruling is recorded at the call site, in the workflow, verbatim:

  > `.github/workflows/valoria-ci.yml:247-249` — *"`ci_vacuous_assertion_check` below is KEPT by
  > Jordan's ruling of 2026-08-21 (culling plan §5.6): it is a literal encoding of CLAUDE.md §0.1
  > point 2, and deleting it would have required striking §0.1 in the same commit."*

  So the depth-4 chain **persists BY RULING, not by oversight**, and R11.3's framing of it as a
  re-formed generator is wrong on this one instance. Deleting the pair needs a NEW Jordan ruling
  AND a same-commit strike of §0.1 pt 2 — it is not a session call and not a predicate application.
  `references/ci_checks_registry.yaml:34` independently records it as the file's ONLY `layer: L2`
  row, i.e. already classified as the deliberate exception rather than an unnoticed rung.

  **How the error happened, because it is the session's own pattern again:** one read-only critic
  applied the predicate correctly *in the abstract* and never checked whether the artifact was
  ruled; I relayed its recommendation into this document without checking either. A predicate is
  not a licence to act where a ruling already decided — CLAUDE.md §0's five-test ladder puts
  "superseded by a later ruling" FIRST for exactly this reason, and neither of us ran test 1.

  What remains genuinely in scope for the predicate: `test_known_red_register.py` (111 lines
  guarding a register of failing tests) and the ~2,700-line vector-audit cluster, whose subject is
  `skills/valoria-vector-audit/scripts/`. Run test 1 on each before touching it.

- **R11-E. PROTECT LIST — a cull must not take these.** All of `engine/tests/`;
  `test_combat_invariants.py`, `test_key_substrate.py`, `test_combat_draw_stream.py` + `_draw_stream.py`,
  `test_engine_does_not_import_systems.py`, `test_degree_ladder_single_owner.py`,
  `test_world_initial_state.py`, `test_morale_write_sweep.py`, `test_contract_runtime_conformance.py`,
  `test_descriptors_runtime.py`, `test_conviction_roster_single_owner.py`,
  `test_faction_obstacle_conventions.py`, `test_faction_l_reconstruction.py`,
  `test_no_polling_triggers.py`, `test_claim_provenance_fields.py`, `test_field_golden_pins.py`,
  the three golden JSONs, and the combat + mass-battle behavioural family (~13k lines).

### R11.4 — `audit/` holds a ratified mechanism with no implementation anywhere

`audit/` is **230 files / 79,126 lines**. The plan step to empty it (**S7**) already exists *twice* in
executable form — `tools/evacuation_plan.py` (keep/relocate/fork rules with ruled exceptions) and
`proposals/2026-08-18-culling-plan-v1.md:212-246`. **S7 is an execution job, not an analysis job.**

The dangerous finding: **the entire Churn-engine parameterization exists only in
`audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md`** — a `## Status:
RATIFIED` head referenced by `CURRENT.md:40`. Grep finds no implementation: `churn|narrative_engine|
light_function` yields one `params_tables.yaml` line across `engine/` and only unrelated comments
across `systems/**/*.py`. Under §0.05 the game's ratified narrative layer has **no mechanism at all**,
and forking the doc blindly leaves no spec on `main` either.

**Two shipping-gate tests read `audit/` — S7 breaks CI if run naively:**
- `tests/valoria/test_audit_plan_ids_are_allocated.py:245-246` opens
  `audit/2026-08-11-code-leanness/01_plan.md` (a unit the culling plan marks "delete outright") and
  walks all of `audit/` with a corpus floor `MIN_HEADER_DOCS = 40`.
- `tests/valoria/test_evacuation_plan.py:293-304` **requires**
  `classify('audit/2026-06-03-contest-groundup/engine.py') == 'relocate'` to `engine/reference/` —
  that file is the frozen parity oracle behind `engine/tests/test_sigma_leverage_parity.py`'s golden.

- **R11-F. Execute S7 from `evacuation_plan.py`, not from the ratified prose**, repointing both test
  fixtures in the same commit. Sizing: ~6 files move to code homes; ~35–40 extract as reference;
  ~185 files / ~72% fork.
- **R11-G. The narrative-engine head moves, it does not fork** — already ruled at culling-plan
  `:220-221`. Whether its Light-Function weights become code is a separate, unasked design question.
- **R11-H. Two ledger/tree disagreements to reconcile first.**
  `references/restructure_ledger.md:1277` declares `audit/2026-08-06-vector-audit/` forked while
  `structure_audit/data/structure_metrics.json` is still on disk and line-anchored from
  `systems/_architecture/engine_atlas_v1.md:308` and `systems/factions/factions_flow_skeleton_v1.md:186-187`
  — the `pathres.resolve()` dir-prefix hazard §8 documents, live. Inversely,
  `audit/2026-08-03-session-oddities.md` is cited by `tools/build_fork.py:20` and
  `systems/_architecture/repository_keep_set_v1.md:20`, is **absent from disk, and has no ledger row**.

---

## Files read this session (the audit trail)

**Game code:** `systems/characters/sim/conviction.py`, `systems/world/sim/npe.py`,
`systems/fieldwork/sim/knots.py`, `systems/factions/sim/faction_action.py`,
`systems/factions/sim/parliamentary_transfer.py`, `systems/mass_battle/sim/__init__.py`,
`systems/combat/combat_engine_v1/{weapons,config,combat_systems}.py`,
`systems/social_contest/sim/contest/primitives.py`, `engine/substrate/{descriptors,keys}.py`,
`engine/cross_scale/{articulation,echo_transport}.py`, `engine/autoload/game_state.py`,
`engine/mc_v18.py`.

**Registries / artifacts:** `references/{descriptor_registry,module_contracts,alias_registry,
ci_checks_registry,restructure_ledger,engine_atlas}.{yaml,md,json}`,
`engine/engine_params/{descriptors,key_types,composition,module_contracts,sim_params}.json`,
`registers/editorial_ledger*.jsonl`.

**Tests:** `engine/tests/{test_knots_ed912,test_pipeline_reach,test_parliamentary_bridge,
test_world_population,test_mc_v18_regression,test_f7_smoke_oracle}.py`,
`tests/valoria/{test_flow_skeletons,test_engine_params_bridge,test_ci_common_primitives,
test_ed_citation_scope,test_conviction_roster_single_owner,test_module_contracts_artifact,
test_contract_runtime_conformance}.py`.

**Tools:** `tools/{export_descriptors,export_module_contracts,export_sim_params,
contract_runtime_conformance,triage_work_items,valoria_local,pathres,ci_common,
m1_acceptance,build_engine_atlas}.py`, `.github/workflows/valoria-ci.yml`, `.claude/settings.json`.

**Prose (read deliberately, per Jordan's explicit request for plan documents):**
`CLAUDE.md` §0–§11, `CURRENT.md`, `HANDOFF.md`,
`systems/characters/conviction_taxonomy_v30.md`, `systems/fieldwork/knots_v30.md`,
`proposals/{2026-08-18-culling-plan-v1,2026-08-21-execution-order-v1,
2026-08-20-return-to-game-plan-v1,2026-08-18-breaking-the-recursion,repo-reorganization-v1,
valoria_fork_plan_of_record_v1,2026-08-16-system-scores-census}.md`,
`workplans/{workplan_v6_progress,return_to_game_queue}.yaml`, the 10 `*_flow_skeleton_v1.md`,
`systems/_architecture/engine_atlas_v1.md`.

---

## Execution order for a new session

1. **R10-A** — wire one emitter; move `observed` 3 → 4. *Do this first, before reading anything else.*
2. **R9-A** — make one game regression able to red CI.
3. **R4-A** — settle the conformance `--check` wiring (it exits 1 today).
4. **R1-A / R1-C** — the ledger triage, row by row, with `ED-PC-0016` and `ED-PC-0049` escalated.
5. **R5-A / R5-B** — mark or rule `Honor`; cook the conviction-axis matrix.
6. **R7-A** — Jordan's call on the flow-skeleton anchor gate.
7. **R2-A / R2-B / R3-A / R5-C / R4-B** — the sweeps, in whatever order the work touches them.
8. **R8.1–R8.5** — file as ledger rows if not fixed; R8.4 is a genuine Jordan fork.

9. **R11-A / R11-C** — the two mechanisms filed outside the game tree (the MB engine; the Knot Pool
   formula). R11-C is small and unblocked; R11-A carries a real MB-lane design call.
10. **R11-F / R11-G / R11-H** — S7, executed from `evacuation_plan.py`, with the two ledger/tree
    disagreements reconciled first and both test fixtures repointed in the same commit.

**Correction to R10 from R11.1.** The "all game code = 30,159 lines" figure excluded
`tests/sim/mass_battle/` (11,342 lines), which is game code by every test in this document. The
11:1 apparatus-to-game ratio for *this session's own output* stands — none of my +120 landed there —
but the tree-wide 1.53:1 is wrong in the game's favour once that engine is counted where it belongs.
