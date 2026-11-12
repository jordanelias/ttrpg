# CORE — adversarial steelman audit · addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 785bc62 (working tree)

Addendum to `01_CORE_audit.md` (read at `601e715`). It covers what that audit declared skipped —
`loop/predicates.py`, `seam/wrappers/mass_battle.py` and the rest of `seam/wrappers/`, the `data/` loaders,
the `harness/` instruments it did not open, `registers/handoffs/HANDOFF_IN.md` and
`architecture/meta/04_CODE_ARCHITECTURE.md` — and adds the sections the brief's later amendments ask for
that the audit does not carry: a Layer-1 conformance reading (§4), the capability authoring surface (§5,
the brief's §14), the NPC and chooser intent for the core (§6), and what the archived design descriptions
and the earlier audit corpus change (§7). The first audit is not edited; where this reading contradicts
it, the correction is in §3. Finding numbers continue from the audit's last (F-CORE-11).

## 0. Verdict of the addendum

The first audit's verdict stands and is sharpened in one direction: **the kernel conforms to Layer 1 where
Layer 1 is about who may write, and departs from it where Layer 1 is about what a person may read and what
an act leaves behind.** Three things follow that the first audit could not see from the files it read.
(1) The capability a person brings to a roll has a real single reader (`seam/wrappers/pool.py::faculty`)
and no single author: its facts are spread over six files, five of eleven contested verbs name no
capability at all, and a skill cannot be acquired in play because rank one is worse than having none
(§5). (2) What made a person act — the question, and which term of his score decided — is held on a
driver object or nowhere, so the narrative cannot read a reason once the process ends (F-CORE-12). (3)
The one-code-path route from season call to playable scene exists and works for exactly one module
(personal combat, by a `decide` callable handed to the same entry); the seam already carries the argument
to the other three providers, which ignore it (§4.4). None of this is a defect in the gate, the fold or
the log.

## 1. What was read

Read in full, with comments and docstrings (line counts from `wc -l`):

| file | lines | note |
|---|---|---|
| `architecture/meta/04_CODE_ARCHITECTURE.md` | 1,657 | all of Parts A–G |
| `registers/handoffs/HANDOFF_IN.md` | 32 | Open and Standing orders |
| `loop/predicates.py` | 711 | nine registered predicates |
| `seam/wrappers/mass_battle.py`, `__init__.py`, `pool.py` | 515, 47, 100 | |
| `data/cast.py`, `goals.py`, `pursuits.py`, `affiliations.py`, `arrangements.py`, `geography.py`, `__init__.py` | 545, 580, 171, 213, 287, 63, 62 | the lazy and import-time loaders |
| `data/rosters.py`, `fixtures.py`, `requires.py`, `verbs.py` | 1,590, 1,169, 1,119, 2,186 | every roster binding, `DEFAULT_FIXTURES`, the `requires` grammar, the verb loader and its derived sets |
| `decision/budget.py`, `decision/sheet.py`, `harness/play_surface.py` | 83, 209, 95 | for §6 and the corrections |
| `loop/deliberate.py:56-330` | — | the map, the budget query, the release |
| `audits/01_CORE_audit.md`, `audits/02_CHAR_audit.md` (part one), the brief, `dossiers/01_CORE.md` | — | |

| `harness/run_cases.py`, `arms.py`, `loops.py`, `interactions.py`, `report.py`, `scarce.py` | 531, 315, 544, 470, 306, 266 | in full |
| `queries/world_q.py:3857-3990` | — | `attention_key`, for F-CORE-20 |

<!-- APPEND-READ -->

## 2. New adversarial findings (worst first)

### F-CORE-12 · degrades narrative · the reason for an act is not in the world

- **Claim.** Three facts a narrative reader needs about an act — what occasioned it, on whose behalf, and
  why this act and not another — have three different fates, and none is in `World`. (a) The `Question`
  an act answered is held by `Scene.occasion`, and Scenes are kept in `SeasonDriver.scenes`, a dict on
  the driver set once in `__init__` (`loop/driver.py:322`) and written at release
  (`loop/deliberate.py:303`). It is cumulative on purpose (the comment at `driver.py:317-321` says the
  fold's record must cross seasons), as are `resolved` and `act_of` beside it; but it is the driver's,
  not the world's: no `World` collection holds it and it is not hashed. (b) An act that answers a standing
  occasion (a creed, a vacancy, a held writ) is given no antecedent at all: `_occasion_of` returns `[]`
  for it (`loop/resolve.py:181-184`), so its Event cites the act and nothing else. (c) Which term of the
  score decided (pursuit, stance, the draw) is computed in `decision/choose.py` and kept by nothing;
  `Candidate.why` was removed (`state/carriers.py:591-593`).
- **Evidence / falsifier run.** `probe_reason.py`, headless world, seed 0, three seasons: the driver held
  8, 18 and 28 Scenes after seasons 0, 1 and 2 (it grows for the life of the driver); all 58 stored acts
  resolve their `scene` id only through that dict; 54 act-caused Events cite an occasion beyond the act
  and 4 cite the act alone (`record.created`, `finding.none`, `exchange.refused`, `commitment.made`).
  The falsifier was a `World` attribute or log field from which a second driver could recover a past
  act's question; there is none (`Act` fields: `actor, changes, contests, id, obstacle, payload, pool,
  reads, scene, stratum, verb, via`).
- **Touches.** R-01 and R-02 as *read* (a chain can be walked, its motive cannot), R-06, R-07; every arc
  whose beat is "he did it because".
- **Narrative consequence.** A chronicle built from a saved world can say that Carin made a record and
  cannot say it was for the creed she is committed to. A second `SeasonDriver` on the same world (every
  harness constructs one per run) starts with no memory of why anything was done.
- **Minimal fix at the owner.** The Scene is Layer 1's own type (`04` §B.9) and the act store is its
  resolver-side home: keep released Scenes in `state/acts.py` beside the acts they carry, append-only;
  give a standing-occasion act its occasion as a stored fact (the Scene's `occasion.source` and `about`)
  rather than as `causes[]`. Proposal `01_CORE_reason_trail_in_the_act_store.md`. The deciding term is
  the CHAR lane's (`02_CHAR_reason_trail_and_small_edits.md` Part A, an observer hook on the chooser);
  that proposal says *"what survives is the OCCASION … on the `Scene`"*, which is true for the length of
  the driver's life and is the gap this one closes.

### F-CORE-13 · blocks "playable" for four of eleven contested verbs' kin · one module is a scene, three are calls

- **Claim.** The route by which a registered module is both a season-loop call and a playable scene is
  built once and is sound: `seam/wrappers/combat.py:394-395` hands the host's decider to the *same* module
  entry (`entry.fn(inp, random.Random(seed), decide=host.decide)`), chosen by a party test on
  `PlayHost.persons`, with the same input and the same seed in both modes. `contest()` threads `host` to
  every provider. `sigma.resolve`, `mass_battle.resolve` and `fieldwork` accept it and do not read it
  (`seam/wrappers/mass_battle.py:361-363`: *"`host` … is accepted and NOT USED HERE either: mass battle's
  PLAYABLE mode would read this same keyword"*).
- **Evidence.** `grep -n "host" seam/wrappers/*.py`; `queries/inputs.py:178-191` (`PlayHost`: `persons`,
  `decide`, typed for combat's per-turn set only). No instrument enters a module standalone except
  through a season: `harness/` has no runner that builds one typed input and plays one scene.
- **Touches.** R-03 (the scene), R-05; the standing requirement's three points at once.
- **Minimal fix.** One scene contract for every module: the entry takes `decide=None`; the provider's
  party test is one shared function; a standalone runner builds the typed input from a fixture and calls
  the registered entry. Proposal `01_CORE_one_scene_contract.md` (the per-module choice points are the
  module lanes').

### F-CORE-14 · degrades legibility · a governance refusal cannot say which clause refused, and four predicates crash on a malformed act

- **Claim.** Nine predicates are registered (`confer, convene, dispatch, establish, interrogate, oblige,
  release, revoke, succeed`). (a) REM-14's clause trace (`_refuse`, `loop/predicates.py:62-75`) is written
  by five of them; `confer` (6 bare `return False`), `establish` (9), `oblige` (4) and `succeed` (2) say
  nothing. The clause reaches only `TRACE`, a process-global list, never the refusal Event, because a
  keyed `emits_on_refusal:` requires a typed cell (`data/verbs.py:972-976`). (b) `dispatch`, `convene`,
  `revoke` and `oblige` raise `TypeError` on a list-valued operand where the other five refuse, and the
  fold calls the predicate with no catch (`loop/resolve.py:285`).
- **Evidence / falsifier run.** `probe_predicates.py`: counts as above; `dispatch`, `convene`, `revoke`,
  `oblige` → `TypeError: unhashable type: 'list'`; `release`, `confer`, `succeed`, `interrogate`,
  `establish` → `False`. The guard exists at three sites as a comment (*"a list `subject` is unhashable:
  refuse, never raise"*, `predicates.py:142,153,192,553`) and not at the other four. A computed act does
  not carry a list today; a hand-built one and a client's callback can
  (`tests/test_u7_remit.py:515-523` records the same crash on a typed cell, fixed there).
- **Touches.** R-04 (the seat verbs are the governance surface), R-05; outcome legibility.
- **Narrative consequence.** The persons whose acts are strategic get the least explanation: a refused
  conferral emits `confer.refused` for seven different reasons and the actor's ledger cannot tell them
  apart, so he cannot learn which belief to revise (the mechanism §F1 clause 4 depends on).
- **Minimal fix.** One read of an act's referent that returns only an id or nothing; every refusing
  branch names its clause; the predicate's answer carries the clause so a row may key it. Proposal
  `01_CORE_predicates_name_their_clause.md`.

### F-CORE-15 · code matter · the capability a roll reads has one reader and six authors

Stated in full in §5. In short: `faculty` is the one pool reader; the facts it reads are in
`rosters.yaml` (three rosters and a table), `references/descriptor_registry.yaml`,
`references/npc_registry.yaml`, `data/fixtures.py`, `modules/combat/attributes.py` and case overlays.
Five of eleven contested verbs (`arrest`, `determine`, `lie`, `march`, `interrogate`) have no
`verb_capability` row, so every person rolls `pool_default` on them (`lie` beside `tell`, which has one).
`raised_capability` never mints a key (`loop/effects_combat.py:262-268`: a minted rank of 1 *"would
replace `pool_default` … and LOWER the pool"*), so no person learns a skill he was not built holding.
Endurance's default is written three times with two values (registry `default: 1`;
`modules/combat/attributes.py` `end` 4; the literal `4` at `seam/wrappers/combat.py:151`). Touches R-06,
R-09. Proposal `01_CORE_capability_authoring_surface.md`.

### F-CORE-16 · Layer-1 conformance · the verb table's `scale:` column is refused by Layer 1 in terms, and the code says it is not

- **Claim.** `04` §A.3 row 4: *"`scale:` on modules and **on seven verb rows** — deleted; the loader
  rejects the key"*; §B.13 invariant 10: *"unknown keys rejected — a `scale:` key fails the load"*.
  `data/verbs.py:129-137` and `:619-621` declare the invariant *"NOT ENFORCED, BECAUSE IT IS ABOUT A
  DIFFERENT FIELD: the chain's retired per-module `scale:`"*. Row 4 names the verb rows.
- **Evidence.** 15 rows of `verb_table.yaml` carry the key (values `person`, `settlement`, `territory`,
  `province`); the column has no reader (H-89, verified by the first audit).
- **Resolution.** This is not an ambiguity between two rows of the spec (the only case in which the code
  may pick, `CLAUDE.md` §0.05); the spec is single-valued and the code departs from it. Change the code:
  release CR-07 (delete the column, `VerbRow.scale`, its `RUNG_KINDS` check) and let the loader's
  unknown-key rule refuse it. The first audit's resolution 21 reaches the same edit from H-89; this is its
  Layer-1 ground. No proposal file: CR-07's text is the edit.

### F-CORE-17 · Layer-1 conformance · a refusal is priced, and the price leaves no receipt

`04` PART D row 51 grades *an unpriced refusal* STRUCTURAL with a named falsifier: *"a refusal Event's
`changes[]` is non-empty, carrying the debit's receipt"*. The debit is made (`loop/deliberate.py:294`,
`self._spent`, at release, so a refused act costs its scene) and is a driver dict, not a gate write.
**Falsifier run** (`probe_refusal_receipts.py`, headless, seed 0, three seasons): 27 refusal Events, 0
with a non-empty `changes[]`. The behaviour row 51 wants holds; its representation does not. Resolution in
§8 (row 9): the spec row's *construction* is unbuilt and stays unbuilt until a budget is a carrier field
(there is no `(Person, budget)` matrix row, and `budget` is ruled a Query, H-28); the row is refiled in
the register as "behaviour holds, falsifier fails", not edited in `04`.

### F-CORE-18 · design matter · a verb's facts live in its row and in fourteen rosters keyed by verb

`data/verbs.py` and `data/rosters.py` load fourteen mappings whose key is a verb and whose content is a
fact about that verb: `verb_capability` (9 verbs), `graded_inquiries` (3), `warrant_sourced` (2),
`choice_sourced` (2), `own_hold_declines` (2), `duel_terms` (2), and eight with one member
(`terms_sourced`, `vocation_sourced`, `held_document_declines`, `own_stance_declines`, `lie_verbs`,
`own_title_declines`, `held_edge_declines`, `violence_contexts`). Each has its own loader function and
refusal (about 250 lines of `data/verbs.py:1191-1895`), and `VerbRow` separately carries four boolean
columns each true on one row. The CHAR audit's F-CHAR-11 reads the person-side half (nine declines in
`opening_set`); this is the data half. It fails NERS-E as a ratio (fourteen loaders for twenty-seven
facts) and S (*one* verb, *one* row is the table's own premise, `04` §A.1). The capability case is
resolved in §5 (a `capability:` column on the row). The rest follows F-CHAR-11's proposal
(`02_CHAR_offer_what_can_be_done.md`) and is not re-proposed here.

### F-CORE-19 · hygiene · stale counts and claims at the owners

- `loop/predicates.py:1-4` says seven cells (five until…); the tail comment (`:685-710`) enumerates
  eight, includes the retired `give`, omits `succeed` and `interrogate`. Nine are registered.
- `data/fixtures.py:434-437`: *"`Person.capability` … with exactly one writer in the tree, which ZEROES
  it"*; writers today are a cast overlay, `cast.capability_of`, `_eff_train` and `_grown`.
- `data/requires.py:16-23,765-771` and `data/__init__.py:4` place `WorldReader`/`LedgerReader` and the
  loaders' importer in `shape.py`, a module that no longer holds them.
- `decision/sheet.py:2-3`: the design is *"PROPOSED and HELD BACK"*; it is RATIFIED (the CHAR audit's
  F-CHAR-15 records the same).
- `data/verbs.py:29-38`: a docstring explaining a forward declaration that *"is otherwise harmless"*
  (`VERB_TABLE: dict = {}` at `:1187`, rebound two lines later). Delete the declaration and the paragraph.

Fix: correct each when the file is next opened; no sweep (`CLAUDE.md` §0.1 pt 5).

### F-CORE-20 · degrades narrative, and narrows R-01 and R-04 · a need propagates to the one who could meet it and is not met

(Ranked second of this addendum's findings by consequence; numbered in the order found.)

- **Claim.** In the world built to show demand and delivery (`harness/scarce.py`: a town that runs dry, a
  steward who holds it and stands in a full granary), the shipped loop delivers nothing to the town in
  four seasons. The shortfall is recorded, deposited to the steward and raises a question; he does not
  answer it. With the harness naming his question for him (the instrument's one intervention) he sends
  8 salt once and never the 15 grain.
- **Evidence / falsifier runs.** `python -m engine.season.harness.scarce` (seed 0, four seasons,
  `scarce.txt`): unassisted, deliveries at the hungry town after the first season are 0 grain and 0 salt
  every season while the granary goes from 100 to 216 grain; the steward's six transfers are 1 grain
  from the granary to the granary, each refused. Cause located at `queries/world_q.py::attention_key`:
  the held town and his own granary are both tier 1, *"magnitudes inside tier 1 are not ranked
  (LIMIT)"*, and the tiebreak is the question id. Two in-process experiments, each against its
  same-seed control: answering the first *unanswered* question changes nothing (hash equal; a null,
  because a new claim heads the list every round); ordering a shortfall claim first inside tier 1 moves
  the hash at seeds 0, 1 and 2 and produces relief at seed 2 only (15 grain, claim-sourced), because at
  seeds 0 and 1 the steward attends and then does not choose `transfer`.
- **Touches.** R-01 (the edge exists; the consequence that matters does not follow), R-04 (a seat's
  management response), R-06.
- **Narrative consequence.** Famine is never relieved by the person whose office it is; a realm's
  stewards hoard beside starving towns for a reason no character holds. The story the settlement arcs
  need (want, appeal, relief or refusal, blame) has its first two beats and not its third.
- **Minimal fix at the owner.** Inside tier 1, order by recorded unmet need (one term, tier 2's
  precedent). Necessary and, measured, not sufficient: the second link is the ranking (the CHAR audit's
  F-CHAR-01). Proposal `01_CORE_unmet_need_is_attended_first.md`.

### F-CORE-21 · blocks an honest reading of loop bounds (H-25, CR-98) · the loop check passes on six cycles of 39,482, and cannot see the loops that run away

- **Claim.** `harness/loops.py` derives the cycle set from what is written against every *typed* reader
  and compares amplifiers with the register's LOOP rows. A verb's write carries no polarity (`?`), so
  every cycle through a verb is unsigned.
- **Evidence / falsifier run.** `python -m engine.season.harness.loops` (`loops.txt`): 73 processes,
  39,482 cycles: 4 amplifying, 2 damping, **39,476 unsigned**; verdict *"AMPLIFIERS … derived ==
  declared"*, exit 0. The six signed cycles are produced by the four `STEP_READS` processes and compared
  with `DECLARED_CYCLES`; both are literals in `loops.py` (`:154-181`), so the equality compares one
  file's two constants. The instrument lists its own blind spots and they are the character's interior:
  the nine predicate verbs, and *"DELIBERATE (all but its question sources)"*. Not on the graph at all:
  `Person.scar` (the CHAR audit measures it at a median maximum of 41 against a ladder of 3,
  F-CHAR-04), `Person.capability` raised by success (`_grown`, `practice`: `data/fixtures.py:469-473`
  calls practice *"a capped positive loop (success -> dice -> success)"*), `Person.stance` moved by a
  lost field and read by the next choice. The falsifier was an unsigned count small enough to read; it
  is 99.98 % of the set.
- **Touches.** R-02, R-09; the termination question the archived propagation spec leaves open across
  seasons (§7.1).
- **Minimal fix at the owner (input to CR-98, which is scheduled).** Declare the chooser as a reader
  (`Person.pursuits`, `stance`, `scar`, `capability` → `Act[].returned`, each signed where the score's
  term is monotone) and the fold's three interior writers as processes with their signs; add LOOP rows
  for the scar (amplifying; its bound is the CHAR proposal's season cap) and practice (amplifying; bound
  `practice_cap`). Until a verb's write has a polarity the verdict line should print the signed share
  beside "equal". Edits in `harness/loops.py` and the register; no new file (§8 row 24).

### F-CORE-22 · hygiene with a measurement risk · the one controlled-comparison instrument cannot tell a null from a fake control

`harness/arms.py` is the tree's n-seed two-arm instrument (`CLAUDE.md` §7 names it). Its shipped pair is
`field_casualty_model` `total` against `scaled_by_degree`, which differ only on a *lost, fought* field.
Its own docstring: one seed, two seasons, *"9 DECLARED marches and 0 resolved ones"*, and *"the tool
prints … how many resolved field battles it saw"*. `main` prints total acts and the tally by act subject
(`arms.py:288-310`); it prints no count of fought fields. With none fought the two arms are identical by
construction, and the printed line reads *"no category shifted significantly … This is a CONTROL, not
proof of no effect"*. The first audit found `march` among the never-attempted verbs of the corpus.
`[Not run here: the default invocation is twenty realm builds of two seasons each.]` Fix: `run_arm`
returns the count of field Events at a fought band (`FIELD_BANDS`), `main` prints it and prints
`NOT-COMPUTABLE` in place of a z when it is zero in both arms. The mapping form of an arm
(`{'fixtures': …, 'build': …}`) is general and has no command line (`:192-193`); giving it one makes
`arms` the control every proposal's gate in this suite can cite. `_pool_arm` and `_ARMS_POOL`
(`:255-272`), kept *"as historical records"*, are dead code; the record is the commit.

### F-CORE-23 · bears on the arcs charge · the provided corpus is loaded through a repair routine, and one case is gone

`harness/run_cases.py::_tolerant_yaml` exists because *"six of [the chain's] seven case files do not
load with `yaml.safe_load`"*. Re-run (`load_cases`, §10): eight defects recorded; `ARC1`, `ARC2`,
`ARC3`, `NPC1`, `NPC2`, `NPC3` are each *"committed inside a markdown fence with transcript preamble"*;
`ARC3.yaml` is *"TRUNCATED AT HEAD — 37 lines of a record above the first `- id:`"* and the recovery
*"recovered 0 row(s)"*, so one emergent case's needs are in no instrument's corpus although the
function's docstring says its rows *"are NOT DROPPED"*. 46 NPC and 97 ARC cases load. The files are the
specification the arcs charge adjudicates against, and code reads them (`CLAUDE.md` §0.05: a fact code
reads lives where code reads it, in a form a loader validates). Resolution (§8 row 26): normalise the
six files to plain YAML in one commit (the fence and preamble carry no case content; git keeps the
evidence), state the lost head in `ARC3.yaml` as one comment, and delete the repair path so the loader
is `load_yaml`. The lost case is closed as unrecoverable.

Also in this file's neighbour: `harness/report.py::emit` reads `TRACE` (`:171`), which is imported only
under `if __name__ == "__main__"` (`:301`), so `emit` works only when the file is run as a script
`[by reading; not executed, since it writes tracked files under engine/season/runs]`; its step-sequence
text lists six steps and omits ENCOUNTER (`:76-81`); its header counts *"46 unique NPCs"* by hand.

### Corroboration from the instruments read (no new finding)

- `harness/interactions.py` is the reason trail built outside the engine, at Jordan's request
  (`ED-IN-0335`: *"log character interactions so that we can audit then diagnose why"*). It wraps the
  chooser, re-reads each deliberation through the chooser's own functions, and keys its rows on Python
  object identity (`by_act[id(a)]`, with a `held` list *"so `id()` stays unique"*, `:250-251`). Its own
  list of what it cannot show includes *"why the fold refused … (a `REQUIRES_PREDICATES` verb reads
  through a hand-written predicate that records nothing)"*. That is F-CORE-12 and F-CORE-14 stated by
  the instrument that had to work around them.
- `harness/run_cases.py::grade` resolves each declared token to a verb, a hole id, a probe or an Event
  kind and reports `PLAYABLE` when every token names something present. It executes no case. The first
  audit's F-CORE-02 covers the executing instrument; this is the grading one, and its word for "every
  declared thing exists" is the standing requirement's word for something else.

<!-- APPEND-FINDINGS -->

## 3. Corrections to the first audit

| # | first audit | what this reading shows |
|---|---|---|
| C1 | §1.1 step 1: *"season-local driver state cleared (`driver.py:468-473`)"* | True of `round`, `_queued`, `_spent`, `_deliberated_at`, `_inputs`, `_realised`. Four more driver attributes are cumulative by design and never reset: `resolved`, `_resolved_ids`, `scenes`, `act_of` (`driver.py:307-324`: *"NOT season-local … R3 depends on that, and do not 'fix' it into one"*). The lifetime is deliberate; what F-CORE-12 questions is the home. `harness/soak.py:260-263` keeps one driver alive across batches for exactly this reason, and every other harness builds a fresh one |
| C2 | §9 choice surface: `DevelopmentSheet` *"per its docstring; body `[UNVERIFIED]`"* | Verified (`decision/sheet.py:115-163`). It shows the ranked candidate set, the budget remainder and copies of `capability`, `pursuits`, `stance`, `conviction`, `scar`, `body`; it does not show `attributes`, a pool or a believed chance per candidate; an index out of range or repeated raises `Forbidden`. Nothing but three tests calls it |
| C3 | §4 seam fidelity: personal combat returns a dict *"`[04 row not opened]`"* | Opened. `04` §C.5 says a provider returns a `Margin` and *"a subsystem returning a winner has not met the contract"* (D-24); §C.4 (ruled 2026-09-03) says a contested verb's degree is *"READ OFF THE SUBSYSTEM"*. Combat's `wound_state` is the ruled case. Mass battle returns `attacker_wins` and `winner=` (`mass_battle.py:457-459`), graded by a third ladder branch (`ED-IN-0279` (a)). Two rows of `04` decide the provider's return differently; the code follows the later ruling. Named in §4.3 |
| C4 | F-CORE-04: the pool default is everywhere because `build_at` seats no capability | Three further causes. Five contested verbs name no capability key (F-CORE-15). The realm's attribute switch ships off (`populated.py:1016`, `cast_attributes=False`) and one of 46 cast rows authors `stats:`. Lifepath templates grant only `argue` and `inquiry`, on 13 of 34 lifepaths, to 5 of 46 cast rows |
| C5 | resolution 19: `sigma.resolve` builds an unseeded generator when handed none | Upheld, and wider: `modules/combat/wrapper.py:565` has the same fallback (`rng=rng or random.Random()`). The archived propagation spec states the intent as a rule (RNG-1: no resolver reachable from the action phase may default to an unseeded generator). The combat line is the PC lane's |
| C6 | resolution 21 (retire `scale:`) rests on H-89 | It also rests on `04` §A.3 row 4 in terms (F-CORE-16), which makes it a conformance edit and not a judgment call |
| C7 | F-CORE-05: nothing shows an ending | Unchanged in code. The archived design holds an end condition the code could execute and does not: "Portrait Retirement" (a player concludes after two of three starting convictions resolve) and three lineage acts, of which succession is built as `play_surface.carry_on` (§7) |
| C8 | §2 item 1: DELIBERATE *"receives none [no token], so a chooser — a player's callback included — cannot write"* | It cannot write through the gate. It receives the live `Person` (`deliberate.py:202`), so a callback can assign to it directly; Layer 1 specifies a frozen `PersonInterior` (the CHAR audit's F-CHAR-12, cross-listed to this lane; resolved in §8 row 6) |

## 4. Layer-1 conformance reading (`architecture/meta/04_CODE_ARCHITECTURE.md`)

The spec is read at the row; no table or count is copied from it. Grades are the spec's own words.

### 4.1 Ownership (§A.2 and PART D)

| spec row | code | reading |
|---|---|---|
| one write path; tokens minted by the driver only (§B.1, D-3, D-4) | `World.write`; `mint_token` in `loop/driver.py` | conforms (first audit §2 item 1) |
| `decision/` owns nothing, no `World` in scope (§A.2, D-2) | no `World` name under `decision/`; `View.odds` is a host-made callable closed over the world (`deliberate.py:149-168`), declared there as a CONVENTION departure with its B4 reasoning | conforms by path scan; the declared departure is one the spec's own §C.11 licenses on the second of its two rows |
| `choose` receives a frozen `PersonInterior` (§B.2 row 2, §C.3) | the live `Person` | **departs**; change the code (§8 row 6) |
| `loop/deliberate` owns nothing (§A.2) | writes `self.scenes`, `self._queued`, `self._spent` on the driver, and `a.scene` on each released act | conforms in letter (driver state, not a store). The Scene record it creates has no owner in `state/` (F-CORE-12) |
| `seam/contest` returns Events + degree or a typed refusal, never a raise (§A.2, §B.10) | `ContestError`/`ContestRefused` returned; the depth cap decides nothing (first audit F-CORE-07) | conforms |
| providers own nothing, return a `Margin` (§A.2, §C.5, D-24) | `sigma` and `fieldwork` return typed outcomes; combat returns wound state, mass battle a winner marker | **two spec rows disagree** (§4.3) |
| one ladder (D-30) | three (dice margin, wounds, field bands), ruled | spec row graded CONVENTION and superseded by ruling; accepted |
| budget carries no office bonus (§A.3 row 15) | `budget_office_bonus=1` ships (`fixtures.py:592`; `decision/budget.py:60`) | **departs, known and tracked**: `HANDOFF_IN` "Build-order item 4 REVERTED" (deleting it starved news transport), IN-14 (ruled shape: more rounds). No new resolution |
| a refusal Event carries the debit's receipt (D-51) | no receipt (F-CORE-17) | behaviour conforms, construction does not |
| the log accepts no kind outside the derived roster (§B.13 #7, D-25) | the fold checks at build (`resolve.py::_act_events`); `EventLog.append` checks none (H-220) | departs; first audit F-CORE-11 |
| unknown keys rejected, `scale:` among them (§B.13 #10, §A.3 row 4) | `scale:` admitted on 15 rows | **departs** (F-CORE-16) |
| eligibility kinds exclude `capability` (§B.7, §B.13 #3, D-33) | refused by name at load (`data/verbs.py:894-906`) | conforms |
| every fixture named has a register row, or the run refuses at the site (§B.13 #11, D-38) | `Fixtures.get` raises `Ungraded` on an unregistered name (`fixtures.py:43-52`) | conforms for registration; the register-row half is `corpus_run`'s R5 |
| a refusal is a returned value, not a raise (§C.12 rejection 5, PROPOSED) | 586 `raise` statements in non-test `engine/season` (`Unspecified` 220, `Forbidden` 123, `SystemExit` 121); the spec measured 167 on 2026-09-05 | the port debt the spec names has grown about 3.5-fold; the spec's row is PROPOSED, so this is a reading, not a departure |
| `game/` holds the scene tree (§A.2) | no `game/` directory in this repository | out of this repository's scope (the implementation repo) |

### 4.2 Seams

`contest(proj, place, prize, claimants, depth, max_depth)` in the spec; the code's call adds `verb`,
`subject`, `rng`, `rung`, `effort`, `host` as keywords each provider accepts and most ignore
(`mass_battle.py:355-358`). The uniform keyword set is what keeps a fourth provider from growing a
dialect (shape divergence), and it is the reason `host` reaches every provider already. The spec's
"sides resolved once, at the seam boundary" (§C.5.1) holds: `loop/sides.py::sides_of` builds claimants
before the provider runs, and `field_estimate` calls the same function.

### 4.3 The one place two spec rows decide the same thing differently

§C.5's table (*the subsystem returns a `Margin`; a subsystem returning a winner has not met the
contract*) and D-24, against §C.4's ruled paragraph (*the degree is READ OFF THE SUBSYSTEM, never mapped
onto it by the table*). The code follows §C.4 for combat and extends it to the field by `ED-IN-0279`.
Under `layer-conformance` B4 this is the case where the site names the ambiguity and picks: it is named
at `seam/ladder.py:151` and `mass_battle.py:66-73`. Reading: correctly handled; the residual is that
`04` §C.5 and D-24 still read as if unamended, which is IN-44's listed backlog (Layer-1 edits owed) and
not a code defect.

### 4.4 Registered-module conformance, and one code path from scene to season

A registered module, by `04` §A.2 (amended) and `holonic_ARCHITECTURE.md` §43: reached by a composition
row, typed input, typed outcome, no token, no state between calls. Sixteen composition rows are
registered (`references/module_contracts.yaml: composition_roles`): three `verb_call` (`social_contest.roll`,
`combat.fight`, `mass_battle.resolve_field`), three `step_call` (`settlements.subsist`,
`settlements.produce`, `fieldwork.find`), ten `query`.

| property | holds? | evidence |
|---|---|---|
| reached by row, not import | yes | `seam/wrappers/_entry.py`; `mass_battle.py:423-428` looks the entry up by the role the prize row names |
| typed input | yes | `queries/inputs.py` (`MassBattleInput`, `PersonalCombatInput`, `SocialContestInput`, `FieldworkInput`, `ProvisionInput`) |
| typed outcome | two of four contest/inquiry providers | `Margin`, `Findings` typed; combat and mass battle return dicts read by key presence (first audit F-CORE-10) |
| no state between calls | yes for the module; the host reads geography once per process (`data/geography.py`) because the module may not | conforms; the cache is the host's and is declared |
| module reads no host file | yes | `MassBattleInput.geography` is handed in |

**How one module is both a playable scene and a season call, as built (combat).** The season path:
`_fold` → `contest()` → `combat.resolve` → `combat_input(w, …)` → `entry.fn(inp, rng)`. The playable
path differs in one argument: when a claimant is in `host.persons`, `entry.fn(inp, rng, decide=host.decide)`.
Same input builder, same seed, same entry, same return, nothing recorded about the mode
(`queries/inputs.py:189`). The estimate path (`fight_estimate`, `field_estimate`) is a third caller of
the same input builder and entry on a private generator. That is the pattern. What it lacks to be the
standing requirement's "playable alone":

1. **A standalone entry.** Nothing builds a typed input except from a `World` inside a season. A scene
   fixture (the persons, the place, the stakes) plus the existing input builder is enough; the builder
   already takes `w` and ids.
2. **The same pattern on the other three providers** (F-CORE-13).
3. **A typed view for the decider.** Combat's is `CombatTurnView` with a closed choice set
   (`modules/combat/wrapper.py::TURN_CHOICES`). Each module needs the equivalent: a frozen view and a
   closed set, owned by the module.
4. **Write-back that is already there.** The outcome returns to the fold, which writes by
   `writes_at(degree)` and emits; a standalone run that wants consequences applies the same fold to a
   one-act season. No second write path is needed, and none should be built.

The archived doctrine this implements is quoted in §7 (one engine at two fidelities; auto is the kernel
run headless, played is the same kernel run interactively). The code's combat seam is that doctrine
executed; the doctrine's third fidelity (witnessed) and its slate have no code.

## 5. Capability authoring surface for the core (the brief's §14)

### (a) Where the core reads a character capability, what it reads, and from where

| # | site | outcome it changes | reads | authored where |
|---|---|---|---|---|
| 1 | `seam/wrappers/pool.py:78-100` `faculty` | the **pool** of every social roll, graded inquiry and fight | `Person.capability[key]`, `Person.attributes[attr]`, the larger of the two; else `pool_default`; plus `POOL_ADDENDS` | `rosters.yaml: verb_capability` (verb → key), `vocation_attribute` (key → attribute); `Fixtures pool_default` |
| 2 | `seam/wrappers/sigma.py:117` `_opposition_of`; `pool.py:68-75` | the **obstacle** against a person subject (the module halves the score) | the subject's attribute by `vocation_attribute.opposed_by`, else the row's own attribute, else the capability key | same rosters; `opposed_by` is `{}` as shipped; `Fixtures obstacle_default`, `obstacle_ceiling`, `ceiling_per_pool` |
| 3 | `queries/world_q.py:4703` `practice` (a pool addend) | **growth by doing**: dice for recent successes | the log of the person's own acts in the key | `Fixtures practice_window`, `practice_step`, `practice_cap` |
| 4 | `loop/effects_combat.py:262-292, 797-817` `raised_capability`, `_grown`, `_eff_train` | **advancement**: a held key rises by one | `Person.capability`; the vocation on `train`'s `kind` operand | `rosters.yaml: vocation_sourced`; `write_matrix.yaml (Person, capability)` |
| 5 | `seam/wrappers/sigma.py:140-166` `_effort_levels`, `ADVANTAGE_SOURCES` | **advantage**: a shift to the roll per slot of effort | `Act` effort operand | `rosters.yaml: advantage_sources` (`[effort]`) with the function in code; `Fixtures effort_level` |
| 6 | `seam/wrappers/sigma.py:260-300` `believed_input` | a **candidate's score** (`odds_weighting`) and the player's shown odds | the believer's own pool; a `capability:<key>` claim in his ledger about the subject | `CAPABILITY_CLAIM` literal (`sigma.py:238`) |
| 7 | `seam/wrappers/combat.py:143-152, 203-232` `party_end`, `combat_input` | the fight's **attributes** and Endurance less one per body band | `Person.attributes` whole; `attr.body.endurance` with a literal default `4` | `modules/combat/attributes.py` SPEC (key, default, neutral, `registry_key`) |
| 8 | `queries/person_q.py:1123-1147` `OwnStateReader` | an **aperture**: whether `thread_read` forms and folds | `Person.thread_sensitivity` against `Fixtures thread_sensitivity_gate` | two stems named in the grammar (`data/requires.py:809`, `OWN_STATE_STEMS`); `npc_registry.yaml: ts` |
| 9 | `loop/resolve.py:1046` | a **refusal**: Ob greater than a multiple of the pool is not attempted | pool, obstacle | `Fixtures obstacle_refusal_multiple` |
| 10 | `decision/budget.py:57-62` | the **scene budget** (a cost ceiling) | live `hold` count, body bands, travel legs | `Fixtures scene_budget`, `budget_office_bonus`, `budget_leg_penalty`; `rosters.yaml: band_floors.body` |
| 11 | `decision/options.py:1627-1668` `competence` | the **confidence** a told claim lands at | `Person.attributes[Attunement]` | the attribute is named in code (`attribute_key("Attunement")`); `Fixtures competence_gain` (0) |
| 12 | `epistemic.py:919-931`; `person_q.heritage_regard` | a **tag** shown to witnesses, and regard from believed descent | `Person.heritage` | `descriptor_registry.yaml: heritage_roster`; `npc_registry.yaml: heritage` |
| 13 | `decision/sheet.py:73-94, 115-132` | what the player is **shown** | `capability`, `attributes` (creation sheet only) | — |
| 14 | `data/cast.py:314-398`; `harness/corpus_run.py:336-356`; `harness/populated.py:1355` | **who holds what at build** | `stats:`, `lifepath:`, `ts:`, `heritage:` rows; a case's `cast: capability:` | `references/npc_registry.yaml`; `cases/exercises/*.yaml`; `rosters.yaml: lifepaths`, `tables.lifepath_templates` |
| — | `loop/predicates.py`, the eligibility column, the write gate | nothing | no capability is read; Layer 1 refuses it (`data/verbs.py:894-901`) | — |

### (b) Data-driven, hard-coded, doubled

| fact | state |
|---|---|
| verb → capability key | data, in a roster keyed by verb outside the verb's row; **5 of 11 contested rows absent** |
| key → root attribute | data, closed both ways at load (`rosters.py:623-641`) |
| key → opposing attribute | data, column present, empty |
| the attribute roster, scale 1–7, names and aliases | data, single-owned (`descriptor_registry.yaml` → exporter `--check` → `engine/substrate/descriptors.py`) |
| the pool rule itself (larger of attribute and key; default; addends) | code (`faculty`); one owner |
| untrained default, obstacle default and ceiling, practice window/step/cap, effort level, TS gate, competence gain | Python (`DEFAULT_FIXTURES`), each with a register row; not a file a designer edits without opening engine code |
| which attribute judges a told claim | **hard-coded** (`options.py:1627`) |
| the one aptitude gate (Thread Sensitivity) | **hard-coded by name** in the grammar's stem set and in `Person` (a dedicated field) |
| Endurance's default | **tripled** (1, 4, 4) |
| combat's attribute keys and defaults | a second spec (`modules/combat/attributes.py`) pointing at the registry by `registry_key`; `faculty` and `disp` have no registry key |
| who holds a capability at build | four authored sources (cast row `stats:`, cast row `lifepath:`, case `cast: capability:`, hand-built worlds) and one switch that ships off |
| advantage sources | a roster of names cross-checked against a dict of functions in code (`sigma.py:151-156`) |
| what a capability is (kind, what it does, how it grows) | **nowhere**: no definition row exists; the meaning is the union of the sites above |

### (c) Target shape

**The single authoring file is `references/descriptor_registry.yaml`, a new block `capabilities:`**,
exported by the existing `tools/export_descriptors.py` behind its blocking `--check` and read through the
existing leaf `engine/substrate/descriptors.py`. Reasons, in the ladder's order: it already single-owns
the attributes, the practitioner stats, the heritage roster and the pursuit roster (precedent, step 4);
`modules/` may read the substrate leaf and may not read `engine/season/data` (architecture, step 5), so
it is the only existing owner both the season and a module can read; and `rosters.yaml` already has the
pointer mechanism (`from_descriptor:`) for a roster whose members belong to the registry. No second
capability system: the vocation *is* the capability, renamed in nothing.

What one definition must say for the core to use it (the interface):

```yaml
capabilities:
  argue:                       # the id every reader uses (today's vocation key)
    kind: skill                # closed set: attribute | skill | aptitude | trait
    scale: {floor: 0, ceiling: 7}
    base: attr.social.charisma # the attribute the pool starts from (today: vocation_attribute.values)
    opposed_by: attr.mind.will # optional (today: vocation_attribute.opposed_by)
    untrained: default         # default | attribute  (what a non-holder rolls: pool_default, or the base attribute)
    grows_by: [train, practice]  # closed set of growth rules the engine implements
    source: "<ruling or design reference>"
```

and what stays where it is: the **verb's** side is declared on the verb row (`capability: <id>` in
`verb_table.yaml`, required on every contested or graded row, `none` with a note where a roll reads no
capability), because one verb is one row; the **character's** side is the cast row
(`npc_registry.yaml: capabilities: {argue: 3}` beside `stats:`), validated by `data/cast.py` against the
block; the **magnitudes** that are no capability's own (the untrained default, the practice numbers, the
obstacle ceiling) stay in `Fixtures` with their register rows. The loaders in `data/rosters.py` derive
`VERB_CAPABILITY`, `VOCATION_ATTRIBUTE`, `VOCATION_OPPOSED_BY` and `VOCATIONS` from the block and the
verb rows, so every existing reader keeps its import and `faculty` is unchanged. `rosters.yaml:
verb_capability` and `vocation_attribute` are deleted in the same commit (edit the owner, never keep a
second copy).

Division with the CHAR lane, so that one fact has one proposal: this surface owns the **definition** of
a capability, the **verb's** declaration and the **acquisition** rule. Where a capability enters a
person's own *choice* (which attribute grades a told claim, the Thread-Sensitivity gate's two stems,
the planned temper and forecast uses) is `02_CHAR_capability_uses_table.md`'s one table of uses
(`use`, `key`, `form`, `gain`). The two compose without a second scheme: that table's `key` is a
registry key, and a capability id in this block is one.

The mapping capability → axiom → resolver input then reads, for any roll: the verb row names the
capability; the capability row names its kind, base and opponent; `faculty` and `_opposition_of` are the
two rules; `SocialContestInput`/`PersonalCombatInput` carry the pool and the opposition. A trace line per
roll (`pool = max(attr, key) + practice`) is the legibility artifact, written by `faculty`'s caller.

### (d) The RPG axioms the core implements, and those it contradicts or lacks

Implemented, in the tradition's ordinary names:

| axiom | where |
|---|---|
| **dice pool from a rating** (the rating is the number of dice) | `faculty` |
| **skill defaults to its governing attribute** (take the higher of the two) | `faculty`, CR-20 |
| **unskilled default** (a flat pool for one who has neither) | `pool_default` |
| **static opposition** (the obstacle is half the opponent's score) | `_opposition_of`; `modules/social_contest/roll.py::obstacle` |
| **degrees of success** on one ladder | `engine/dice_engine`, `seam/ladder.py` |
| **advancement by training** (a downtime action raises a rating by one) | `train`, `_eff_train` |
| **advancement by use**, windowed and capped | `practice`; `_grown` (a fight that drew blood) |
| **spend effort for advantage** (more of the scene for a better roll) | `effort`, `advantage_sources` |
| **the impossible task is not attempted** (obstacle past a multiple of the pool) | `resolve.py:1046` |
| **wound penalties** (injury lowers Endurance in a fight and scenes in a season) | `party_end`; `budget.body_band_penalty` |
| **action economy** (a fixed budget of scenes, modified by office, injury, travel) | `budget` |
| **prerequisite / aptitude gate** (one: Thread Sensitivity) | `OwnStateReader` |
| **equipment as a rated item** | `rosters.yaml: arms_kinds` → `engine/substrate/combat_kit.py` |
| **background package** (a lifepath grants starting skills) | `lifepath_templates` |

Contradicted or lacking, where a designer would expect otherwise:

| expectation | state | consequence |
|---|---|---|
| a first rank in a skill is better than none | **contradicted**: untrained default 2 exceeds rank 1, so the code refuses to mint a key | nobody acquires a skill in play; `train` is refused for every non-holder (the CHAR audit counts it among the leading refusals) |
| every contested roll names what it tests | 5 of 11 do not | a judge, a liar, an arresting officer and an interrogator are equally able by construction |
| attribute **plus** skill, or attribute **caps** skill | neither; it is the larger of the two | a high attribute makes the skill irrelevant until the skill passes it. This is a ruling (CR-20) and is accepted; it is stated so the block's `untrained:` and `base:` are read correctly. The archived design's pool was additive (`attribute × 2 + History + 3`, `derived_stats_v30` §14.4); a reader moving between the two should not expect the design's pool sizes |
| a **derived resource** from an attribute (hit points from Endurance, composure from a social attribute) | none on the season side; the combat module has its own (`modules/combat/`) | a wound is a band on one 0–1000 scale for every person; an enduring man is no harder to wear down in a season. PC and CHAR lanes |
| traits, talents, flaws as named tags with declared effects | no carrier but `heritage` and Thread Sensitivity, each a dedicated field | the block's `kind: trait` has no reader until one is designed; the proposal does not invent one |
| skill atrophy | only practice's window | none worth building now |
| opposed roll (both sides roll) | static opposition only, by ruling (2026-08-14) | accepted |
| help, teamwork, tools as bonuses | `advantage_sources` has one member | the roster is the place a second lands |
| **a capability gates an action** (trained-only) | **refused by Layer 1** (*"capability supplies dice and GATES NOTHING"*, D-33) with Thread Sensitivity as the one class-shaped gate (F.27) | the brief's "aperture" clause meets a ruled item. Named in §9; not resolved |
| derived statistics (a design set exists: `derived_stats_v30.md`, archived) | not built on the season side | out of the core; CHAR's |

### (e) Proposals, ordered

1. `proposals/01_CORE_capability_authoring_surface.md` — the block, the verb-row column, the cast-row
   key, the derived loaders, the deletion of the two rosters; hash EQUAL at shipped data.
2. The same file, part two: the five undeclared contested rows declared (a hash mover per row, each with
   its control), and the acquisition rule (`untrained: attribute | default` read by `faculty` so that a
   first rank is never a loss), which is what lets `train` mint.
3. The same file, part three (design-first, held on §9's survivor): a capability as a gate on an act,
   carried by the CHAR uses table's `at_least` form.
4. Beside it, not in it: `02_CHAR_capability_uses_table.md` (the decision layer's uses),
   `05_SC_capability_surface.md`, `06_FA_office_capabilities.md`, `07_SE_capability_and_chooser_surface.md`,
   `03_PC_person_inputs_content.md` and `10_DICE_one_score_two_roles.md` are the other lanes' §14
   proposals `[titles read; bodies not opened except CHAR's head]`.

Dependency edges: CHAR authors the cast rows; PC owns `modules/combat/attributes.py`'s pointer to the
block (its `faculty` and `disp` gain a `registry_key` or are declared combat-local); SC owns the
obstacle's composition; DICE owns the face rule the pool feeds.

## 6. The NPC and chooser intent, for the core (the brief's points (a)–(e))

The reconciliation of the intent's sources is the CHAR lane's; this section cites
`audits/02_CHAR_audit.md` (its §1 for the chooser as coded, §2 items 2 and 8 and §5 for the rulings and
where intent and code part; its statement of the intent was not yet written past part one when this was
read, so the citation is by owner and section, not by a later heading). What the core contributes is the
barrier the chooser stands behind, the budget, and the trail an act leaves.

**(a) What the core needs from NPCs and the chooser.** Who decides: one person, once per round, behind
DELIBERATE (`deliberate.py:131-202`). On what information: a `View` of at most `view_k` of his own claim
ids, one aggregated `Question` (`question_aggregation_rule: first` ships, so one question per
deliberation), a `Sensation` no score term reads, and the budget as a query. At what budget:
`scene_budget` 5 plus one per live `hold`, less body bands and travel legs, floor 1
(`decision/budget.py`), released one scene per round. With what visible reasons: none that persist
(F-CORE-12).

**(b) One chooser for player and NPC.** Yes, structurally: `choose(p, v, s, ask_budget)` is the single
call, `dispatching_chooser` hands named persons to a callback with the same four arguments plus the
automated chooser, and `development_space` ranks with `make_ranker` and packs with `release`, the
automated path's own functions; `take_ranked` is the control that reproduces the automated run. The
player and the NPC are the same kind of agent here. Two qualifications. The callback receives the live
`Person` and not Layer 1's frozen copy (C8). And a client's defect ends the season where an NPC's cannot
occur: a return over budget raises `Forbidden` (`deliberate.py:233-238`, by design: *the engine does not
truncate*), and a malformed operand raises inside four predicates (F-CORE-14). The first is a caller
contract a play loop must meet before it calls (the sheet already refuses a bad pick); the second is a
fold defect.

**(c) Where the core hard-codes an NPC rule instead of reading the chooser.** Four places, none a named
person or outcome (no scripting drift in the strict sense), each a decision about what an NPC may do
made outside the chooser:

- `Fixtures withheld_verbs` (`fixtures.py:1157`): `destroy_record`, the four army verbs, `marshal` and
  `surrender` form for nobody. The commander is thereby not an agent the chooser serves: an army is
  ordered only by a hand-built act or `harness/military_menu.py`.
- The once-per-season opportunity filter (`deliberate.py:260`, `data/verbs.py::opportunity_key`): a
  person never repeats a realised (verb, subject, counterparty) in a season, whatever he would choose.
- `question_aggregation_rule: first`: the order of `question_sources` decides what every person attends
  to first, ahead of his own ranking.
- `scenes_per_round: 1`: the driver spreads a person's five scenes one per round.

Each is a declared, swept fixture. The reading is that the *field* the chooser ranks is narrowed by the
loop four times before the chooser is asked, and three of the four narrowings are identical for every
person.

**(d) What an NPC needs to be characterful at the core, and what would make the choice legible.**
Distinguishable choices need distinguishable inputs at the barrier, and the barrier passes little that
differs: one question, a shared budget (seat-holders differ by one per hold, and cannot spend it,
first audit F-CORE-06), a pool that is the default for nearly everyone (§5). Legibility afterwards needs
three records the core does not keep: the occasion (the question's source and what it was about), the
seat or creed the act was for, and the deciding term. The first two are data the loop already holds at
release; the third is the chooser's and is one tuple per released scene. The archived design's
expression of the same need is the witnessed and reported layers and the retrospective scene (§7).

**(e) What is missing, as proposals.** `01_CORE_reason_trail_in_the_act_store.md` (the occasion, stored
with the Scene; the deciding term is the CHAR proposal's observer hook);
`01_CORE_predicates_name_their_clause.md` (a refusal an actor can
learn from); the frozen `PersonInterior` (§8 row 6, an edit at `loop/deliberate.py` and
`state/carriers.py`, no proposal file needed beyond the row); the commander as a chooser-served agent is
the MB and CHAR lanes' (`withheld_verbs` is released by B10-18b's CR-52/CR-53, already scheduled).

## 7. The archived design descriptions and the earlier audits: what they change

Neither tree is authority; each is read for intent and referents, and each old finding is re-verified
before it is used.

### 7.1 Design descriptions read (`.designs/systems/_architecture/reference/`)

`auto_manual_resolution_duality_v1.md`, `videogame_mode_spec.md`, `scale_transitions_v30.md` and
`campaign_architecture_v30.md` in full; `propagation_spec_v1.md` (its clock, aggregate-up and
termination sections, and every heading); `engine_atlas_v1.md` (reading guide and campaign spine; the
per-subsystem consolidation describes the retired `mc_v18` driver and was read as trimmed text);
`integration_proposal_v30.md` (executive summary, Parts 2–4, 7, 11–13, and every heading).

| intent (document) | as coded | what the difference costs |
|---|---|---|
| **The slate is the spine**: each season the engine offers specific, priority-ranked events; the player has 3–5 scene actions; *choosing what to attend is the gameplay*; what is not attended resolves by NPC AI (`auto_manual…` §1; `scale_transitions` §4.3) | no slate. Each person, the player's included, is asked one question per deliberation and shown a ranked candidate list (`DevelopmentSheet`); the budget is 5 scenes | the player is offered *acts*, not *events*. Triage between situations — the design's stated gameplay — is not a choice he is given; `question_aggregation_rule: first` makes it for him |
| **One engine at two fidelities** (fork A, ruled 2026-07-08): auto is the kernel run headless, played is the same kernel run interactively; a third, witnessed, between them | built for personal combat (`PlayHost`); absent for the other three providers; no witnessed mode | F-CORE-13; the doctrine and the code agree on the shape and differ in coverage |
| **Calibration**: the auto and played outcome distributions agree on matched inputs, checked by a parity harness (§6) | same entry, same seed in both modes for combat, so parity holds by construction where the decider echoes the automated policy; no parity instrument for a decider that plays differently | none while the played path is one module; the gate for each further module is the echo control (`play_surface.py:29-32`) |
| **Zoom in/out**, a stack of at most three; the zoom inserts a scene and does not pause the strategic clock | ENCOUNTER calls out to one provider and resumes; nothing nests (first audit F-CORE-07) | a duel inside a battle, the design's worked case (§3.7), has no code path; MB and PC lanes |
| **Domain Echo**: a personal scene with sufficient scope moves a faction stat at accounting, capped | no faction stat exists to move (Layer 1 §B.6.1: a faction is a Query return). Consequence travels as Events, claims and tenure changes | superseded by Layer 1, and deliberately. The propagation spec's own rule (*no aggregate is ever written*) is what Layer 1 made structural. The echo tables are not a to-do |
| **Mandatory and world-state triggers**; **"Where were you?"** retrospective scenes for events the player missed | a person learns of an event only by a witness channel; the chronicle space shows his ledger | the design's answer to legibility for an absent player is unbuilt. Its mechanism (a free scene next season built from the player's ties) is reachable from what exists: a `claim_landed` question already carries a told claim; nothing marks it as news of a major event |
| **Progressive revelation**; dark / perceived / named values; witnessed and reported layers (`integration_proposal` Parts 4, 7) | `04` §C.11's explanation contract (`explain(p, v) -> Derivation`, person-side) is specified and has no code | the player's sheet shows raw dicts (C2). GO and CHAR lanes; the core's part is that the contract needs the occasion F-CORE-12 does not keep |
| **End of a life**: portrait retirement after two of three convictions resolve; lineage by mentorship, succession or thread legacy (`campaign_architecture` Part 7) | `carry_on` rebinds the player to a continuation on death (succession); `endings_reached` is computed and shown to no one | an end condition a player can read exists in design and half in code; the first audit's play loop (its §8 step 4) should stop on it |
| **The slate's presentation and size** (`player_agency_v30` §4.2b, §4.3, §6): each entry shows who, where, a sentence, *the tag saying which conviction, duty or condition generated it*, and its priority; more entries than actions (Normal: 5–7 against 4); budget +1/+2 by standing, +1 for a knot nearby, −1 exhausted, −1 wounded | the `View` carries each question's `source` and `about`, which is the tag; the sheet does not show it. Budget 5, +1 per live hold, −1 per body band, −1 per travel leg | the generating tag is the cheapest legibility the design asks for and the data is already on the View (resolution 20). The budget's shape agrees with the design; its office term is the one Layer 1 refuses (§4.1) |
| **What is not attended resolves without the player, by its own rule** (§4.5: a table of what each unpursued entry does) | everything unattended is simply other persons' acts in the same fold | agrees in substance, and more generally than the table |
| **The pool** (`derived_stats_v30` §14.4): argue and fieldwork pools are `(primary attribute × 2) + History + 3`, 5–17 dice; one attribute per derived resource (`attribute × multiplier`) | `faculty`: the larger of the attribute and the held key, else 2, plus practice; 2–7 dice. No derived resources on the season side (`body` is a condition scale, not a function of Endurance) | a different axiom by ruling (CR-20), stated in §5 (d) so the two are not confused. "History" in the design is the capability key in code |
| **RNG-1**: no resolver may default to an unseeded generator (`propagation_spec` O.5) | two do (C5) | first audit resolution 19 |
| **Termination**: per-tick bounded; cross-season convergence not proven (`propagation_spec` §4.3) | the season loop has the same property by construction (one fold per round, no re-entry) and the same open question across seasons (H-25, CR-98: loops undeclared) | unchanged; the design's honest scope marker matches the register's |

Vocabulary the code still carries from these documents, for a reader who meets it: *scene action*
(the budgeted unit), *zoom* (ENCOUNTER's call-out), *sufficient scope* (no code), *Domain Echo* (no
code), *accounting* (MATTER and CENSUS between them), *slate* (no code).

Also read in this tree: `holonic_container_doctrine_v1.md` (§0–§2). Its two guardrails are the ones
`CLAUDE.md` §10 binds on every lane, and its statement of the target — *one uniform canonical shape at
every scale … compliant and convertible* — is the standard §4.4 and the one-scene proposal are written
to. Its cross-map names the Key substrate as the wrapper; that substrate is retired (`ED-IN-0232`), and
the seam's typed input/outcome is what replaced it.

### 7.2 The earlier audit corpus (`.audit/`; lesser weight; each old finding re-verified)

Read: `2026-08-11-code-leanness/00_code_leanness.md` (every heading; §1.13, §8, §9 in full),
`2026-08-11-world-schema-gap-audit/02_verdict_and_residuals.md` (§1–§2) and the headings of its second
adversarial pass, `2026-08-06-vector-audit/structure_audit/data/structure_metrics.json` (its keys and
counts), `2026-07-04-ners-qualitative-audit/strategic_judgments.md` (J-1 to J-7 and the list of J-8 to
J-15).

| old finding (audit, date) | re-verified against the tree at `785bc62` | status |
|---|---|---|
| a forked copy of the resolution core lives in the audit archive, *"values match live today; nothing would report it if they stopped"* (code leanness §1.13) | copied to `engine/reference/contest-groundup/engine.py` by ruling (`ED-IN-0231`), read by `tools/gen_sigma_parity_goldens.py`, and a parity golden (`engine/tests/goldens/sigma_leverage_parity.json`) is asserted by the `sim-regression` job | **now false**: a drift would be reported |
| sixteen copies of the "no rng supplied" fallback, disagreeing (code leanness §8.1) | two remain outside tests and the workbench: `seam/wrappers/sigma.py:533`, `modules/combat/wrapper.py:565` | mostly fixed; the residue is C5 |
| the degree ladder has sixteen producers and four meanings of `net` (§7.3, §8.1) | one owner of the four-band ladder (`engine/dice_engine/dice_engine.py::DEGREE_LABEL`, bound once in `data/rosters.py:1100-1103`); three seam ladders by ruling | fixed in the season engine; the three ladders are ruled, not drift |
| *"The masters already exist. The code does not read them"*; the test of a centralisation is *delete the master and see whether anything fails* (§9.2, §9.4) | in the season engine the rosters, the verb table, the write matrix, the offices, goals, cast and geography files are each read by a loader that refuses on absence (`data/*.py`); `params_tables.yaml` is retired. The capability facts fail the test in one place: `DEFAULT_FIXTURES` is a Python literal, so its "master" is the code | the finding does not return for rosters. Its falsifier is adopted as the gate of the capability proposal (delete `capabilities:` and the load must refuse) |
| Jordan's centralisation directive, 2026-08-11 (*"define once … centralize through injectable code, dictionaries, glossaries, masters"*, §8) | a ruling recorded in an archived audit; the same rule is `CLAUDE.md` §0.05 and §8 | referent for §5's single authoring surface; not cited as authority |
| *"a world of near-identical instances plus a handful of hardcoded singletons … a second campaign would differ from the first essentially by RNG seed"*; faction-unique behaviour dispatched by `faction.name` equality (world schema gap §1) | the engine that finding describes (`mc_v18`, four static factions) is retired; factions are a roster and a Query. **The finding returns in two new places**: the corpus builder builds one template world 143 times (first audit F-CORE-02), and persons differ in wants and not in what they can do (§5, the CHAR audit's F-CHAR-03) | **returning finding**, relocated from the faction to the case and the person |
| that audit's own instrument reported a `rediscovery` of 1 for every finding because its grouping key never matched (§2) | a method referent: a column that is always the same value is an absent measurement. The same shape is the CHAR audit's F-CHAR-06 (83 of 83 under every arm) and the first audit's depth-cap arms | lesson applied; nothing to fix here |
| J-1 (ratified 2026-07-05): *the milestone is one playable season, played from the screen, passing the dramatic-legibility questions at each juncture* (NERS strategic judgments) | no client plays a season (first audit F-CORE-05); no module but combat has a played mode (F-CORE-13) | **unanswered** after four months; the milestone's instrument (`tools/m1_acceptance.py`) measures execution and determinism, not play |
| J-5: *player decision surfaces are the biggest North-Star debt; resolvers were built before choice surfaces* | still the shape of the tree: four providers, one decider | unanswered; F-CORE-13's proposal is the core's share |
| J-7: *emergence is real but must be made visible to be believed* | the log is causal and the chronicle prints chains; the reason is not kept (F-CORE-12) and fade records crowd the log (first audit F-CORE-01) | partly answered |
| the vector audit's import-graph metrics (271 nodes, 408 edges, cycles, cut vertices, orphans) | a snapshot of the pre-season tree; its instrument survives as `tests/valoria/test_import_cycle_game_state_npe.py`, which `seam/wrappers/__init__.py:12-25` cites for the cycle it removed | history; no claim rests on it |

<!-- APPEND-CONTEXT -->

Read in part: `player_agency_v30.md` (§4.1, §4.2b–§4.5, §6, and every heading) and
`derived_stats_v30.md` (§1–§3, §14.4–§14.5, and every heading).

**Not read in these two trees** (declared, not sampled as if read): the rest of
`.designs/systems/_architecture/reference/` — the remainder of those two, `throughlines_complete.md`, `complete_systems_reference.md`, `conflict_architecture_proposal.md`,
`campaign_modes_v30.md`, `cogload_moderate_target.md`, `early_game_ignition_analysis.md`,
`hybrid_gaps_v30.md`, `ners_vsg_reconciliation_v1.md`, the governance and Key-substrate documents, the
flow skeletons and the index/infill siblings; `.designs/systems/overview/`; and in `.audit/` the
world-schema-gap register (four parts), its discussion and propagation map, the code-leanness plan, and
the NERS audit's main document and workings. Reason: context budget, after the files this addendum was
commissioned to read.

## 8. Resolutions decided in this addendum

Ladder steps: 1 superseded · 2 irrelevant · 3 answered by a design document · 4 precedent · 5 architecture.

| # | inconsistency / gap / unclear passage | resolution | step | carried by |
|---|---|---|---|---|
| 1 | the question an act answered is on the driver, not the world | Scenes are stored append-only in the act store; the driver keeps none past the season | 5 (`04` §B.9: `Scene` is a type; `state/acts` is its resolver-side home) | proposal `reason_trail` |
| 2 | a standing-occasion act cites nothing | its Scene's `occasion` (source, about) is the record; `causes[]` stays `[act]` (an occasion that is no Event is not a cause) | 4 (`_occasion_of`'s own rule) | proposal `reason_trail` |
| 3 | the deciding term is kept nowhere | the CHAR lane's observer hook on the chooser (`watch`) is its owner; the core adds no field. The stored Scene is what a watcher's record is keyed on | 4 (one owner per fact; CHAR's proposal already decides it) | `02_CHAR_reason_trail_and_small_edits.md` Part A |
| 4 | four predicates raise on a list operand | one referent read (`subject_of` answers an id or `""`); `dispatch`, `convene`, `revoke`, `oblige` read through it | 4 (`subject_of` is already "THE ONE READ") | proposal `predicates` |
| 5 | four predicates refuse without naming a clause; the clause never reaches the Event | every refusing branch calls `_refuse`; a predicate may return its clause, and a predicate row may key `emits_on_refusal:` on declared clause names | 4 (the typed cells' `Verdict.failed`) | proposal `predicates` |
| 6 | `choose` receives the live `Person` | build a frozen `PersonInterior` at DELIBERATE and pass it; `development_space` already copies. Change the code, not `04` | 3 (`04` §B.2) | edit: `state/carriers.py`, `loop/deliberate.py:202`; CHAR's F-CHAR-12 |
| 7 | `scale:` admitted against §A.3 row 4 | release CR-07; correct `data/verbs.py:129-137, 619-621` | 3 | CR-07 |
| 8 | provider return: `Margin` (§C.5, D-24) against degree-read-off-the-subsystem (§C.4) | the code's reading stands; `04` §C.5/D-24 gain the amendment marker at IN-44's batch | 1 (the 2026-09-03 ruling and `ED-IN-0279`) | IN-44 |
| 9 | D-51's falsifier fails though its behaviour holds | refile in the register as "priced by the driver's `_spent`; no receipt"; build nothing until a budget is a carrier field | 2 (the construction's subject, a budget write, was never built; `budget` is ruled a Query) | a register row edit |
| 10 | three providers ignore `host` | one scene contract; module lanes own the choice points | 4 (combat's `decide`) | proposal `one_scene_contract` |
| 11 | no standalone entry to a module | a scene runner that builds the typed input from a fixture and calls the registered entry | 5 | proposal `one_scene_contract` |
| 12 | capability facts in six files, no definition | `descriptor_registry.yaml: capabilities` | 4 (`attributes`' chain) | proposal `capability` |
| 13 | verb → capability is a roster outside the verb's row | a `capability:` column, required on contested and graded rows | 4 (`beneficiary:`'s required-column rule) | proposal `capability` |
| 14 | five contested rows declare no capability | each declares one, or `none` with a note; values proposed in the file | 5 | proposal `capability` |
| 15 | a first rank is worse than none, so no skill is acquired | `untrained:` on the definition; `faculty` reads a non-holder at the declared untrained value and a holder at `max(untrained, rank)` | 5 | proposal `capability` |
| 16 | Endurance default written three times | the combat spec's default is the one a fight uses; `party_end` reads `attributes.DEFAULT` through the module's typed export, not a literal; the registry's `default: 1` is the scale's and is renamed nothing | 4 (`modules/combat/attributes.py`: "a copied name or bound would be a second owner") | proposal `capability` (edit 7) |
| 17 | the attribute that judges a told claim is named in code; the Thread-Sensitivity gate is two stems named for it | both are uses of a capability in a person's own choice, and the CHAR lane's uses table owns them; a capability id from the registry block is a valid `key` there | 4 | `02_CHAR_capability_uses_table.md` |
| 18 | the predicates' stale counts; `fixtures.py`'s stale writer claim; `shape.py` references; the dead forward declaration | corrected at the site when next opened | 5 | edits |
| 19 | the play loop's caller contract (over-budget return raises) | the loop validates before it returns (the sheet's own rule); the engine keeps refusing | 4 (`development_space`) | first audit §8 step 4 |
| 20 | the design's slate against the code's per-person question | no slate is built in the core. The player's triage is offered by showing him *all* his questions for the round: `View.questions` already carries them (CP-T02-07); `DevelopmentSheet` shows only the aggregated one and gains `questions` | 5 | proposal `one_scene_contract` (edit 5) |
| 21 | the design's Domain Echo tables | closed as superseded by Layer 1 (no stored aggregate) | 1 | none |
| 22 | an end a player can read | the play loop stops on `endings_reached`, on the player's own conclusion (the design's portrait rule), or on an extinct line (`carry_on`) | 3 | first audit §8 step 4 |

| 23 | a need at a place a person holds is ordered behind routine news by a hash | inside attention tier 1, order by recorded unmet need; the ranking's half is CHAR's | 4 (tier 2's `-|valence|`) | proposal `unmet_need` |
| 24 | the loop check cannot sign a verb's write or see the chooser's reads | declare the chooser and the fold's interior writers as processes; LOOP rows for scar and practice; print the signed share | 5 | CR-98 (edits to `harness/loops.py` and the register) |
| 25 | `arms` prints no count of fought fields, so a null and a fake control read alike; its general form has no command line | print the count, refuse a z at zero, add `--fixture NAME=A,B` | 5 | edit: `harness/arms.py` |
| 26 | six corpus files need a repair routine to load; one case's head is lost | normalise the files to plain YAML; note the loss in `ARC3.yaml`; delete `_tolerant_yaml`'s recovery; the lost case is closed | 2 (the case's subject is unrecoverable) and 5 | edit: `cases/chain/*.yaml`, `harness/run_cases.py` |
| 27 | `report.emit` depends on a name bound only under `__main__`; its step text omits ENCOUNTER | import `TRACE` at module scope; derive the step list from `data/matrix.py::Step` | 5 | edit: `harness/report.py` |
| 28 | `run_cases` calls a case `PLAYABLE` when its declared tokens resolve | rename the verdict `DECLARED-PRESENT`; "playable" is reserved for a played run | 5 (`CLAUDE.md` §4: a word used as it is used outside the repository) | edit: `harness/run_cases.py`, `harness/report.py` |

<!-- APPEND-RESOLUTIONS -->

## 9. Survivors for Jordan

One, added to the first audit's one.

**May a capability gate an act?** The capability charge asks that an *aperture* respond to a capability
by declaration. Ratified Layer 1 says *capability supplies dice and gates nothing* (D-33, §B.7, §B.13
#3), with Thread Sensitivity as the single class-shaped gate. The code obeys: the eligibility column
refuses `capability`, and the one gate is a `requires` cell over two stems named for it.

- *Option A (the ruling as it stands).* No act is trained-only. Anyone may attempt anything his
  eligibility admits; a capability changes his odds. Thread Sensitivity stays the one exception. The
  game this makes: a world where an unlettered man may try to forge a writ and will usually fail, and
  where expertise is visible as outcome, never as access.
- *Option B (gates by declaration).* A capability definition may be named in a verb's `requires` cell
  (`own:<capability> >= threshold`). The game this makes: professions and schools matter as access —
  only a trained advocate pleads, only a surgeon tends a grave wound — and the option set differs
  between persons, which is the strongest lever on R-06 that the tree does not yet pull.

They are materially different games and the choice overwrites a ratified row, so it is not taken here.
The proposal builds A in full and specifies B's one grammar edit as held.

## 10. Evidence log

All at tree `785bc62`, `PYTHONHASHSEED=0`, no `pytest`. Outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/CORE_B/`.

| command | seed · seasons | outcome |
|---|---|---|
| `probe_predicates.py` (the nine predicates on a list-valued operand; bare/traced refusal counts by source) | 0 · 0 | nine registered; four raise `TypeError`; counts in F-CORE-14 (`probe_predicates.txt`) |
| `probe_reason.py` (what of an act's reason survives) | 0 · 3 | driver holds 8/18/28 Scenes; 58 acts; 54 Events with an occasion, 4 without; 3,085 TRACE rows in process (`probe_reason.txt`) |
| `probe_refusal_receipts.py` (`04` D-51's falsifier) | 0 · 3 | 27 refusal Events, 0 with `changes[]`; hash `383206baa7e7807e28cd609d2bb5f080` (`probe_refusal_receipts.txt`) |
| inline YAML census of `rosters.yaml`, `verb_table.yaml`, `write_matrix.yaml`, `npc_registry.yaml`, `descriptor_registry.yaml`, `module_contracts.yaml` | — | 67 verbs, 11 contested, 9 with a capability row; four vocations; 34 lifepaths, 13 holding a key; 46 cast rows (`stats` 1, `ts` 10, `lifepath` 5, `heritage` 4); 16 composition rows; 15 `scale:` rows |
| `grep -c` of `raise` in non-test `engine/season` | — | 586 (`Unspecified` 220, `Forbidden` 123, `SystemExit` 121, `ValueError` 54) |

| `python -m engine.season.harness.loops` (parts (a), (b); no seeds) | — | exit 0; 5 LOOP rows; 73 processes; 39,482 cycles (+4, −2, ?39,476); "derived == declared" (`loops.txt`) |
| `python -m engine.season.harness.scarce` | 0 · 4, both arms | named: one transfer of 8 salt, hash `d2730068e19527208b8b32b06bb36ba3`; unassisted: no delivery, hash `631b80ad65728c9787d41e85f8037392` (`scarce.txt`) |
| `probe_unanswered_first.py` (experiment against the shipped rule) | 0 · 4 | hash equal to control; positions answered 0 ×37, 1 ×2: a null (`probe_unanswered_first.txt`) |
| `probe_shortfall_salience.py` (experiment against the shipped key) | 0, 1, 2 · 4 | hash moves at all three; relief at seed 2 only (1 and 15 grain) (`probe_shortfall_salience.txt`) |
| `run_cases.load_cases` and `CORPUS_DEFECTS` (inline) | — | 46 NPC, 97 ARC cases; 8 load defects (six fenced files; `ARC3.yaml` truncated, 0 rows recovered) |

<!-- APPEND-EVIDENCE -->
