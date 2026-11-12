# SC — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Short names: `es/` = `engine/season/`; `K/` = `systems/social_contest/sim/contest/` (the kernel);
`PS/` = `proposals/2026-09-05-proceedings-subsystem/`; `PD/` = `proposals/2026-10-29-parliament-and-debate/`;
`SC-Pn` = a proposal file under `proposals/2026-11-12-subsystem-audit-suite/proposals/05_SC_*.md`
(listed in §8). Every run below is `PYTHONHASHSEED=0`; outputs are in the scratchpad named in §12.

## 0. Verdict

**The social contest as coded is a sound resolution primitive and not yet a sound basis for a
dynamic emergent narrative game: it grades one person's attempt on the one ladder, reproducibly, and
NPCs use it without a player, but a hearing almost never ends, cannot be lost by the bench, is not
moved by what is said in it, and offers nobody a choice inside it.** The live subsystem is a
166-line roll (`modules/social_contest/roll.py`) under a correct seam; around it stand the docket,
nine arrangement rows and seven contested verbs of the Proceedings design, of which computed play
reaches the roll and almost nothing else (three `matter.determined` in twelve seed-seasons across
seeds 0 and 1, against sixteen matters lapsed; every pool the same two dice; no docket item naming
its arrangement row). Beside it stands a 6,700-line kernel that models the same
subject a second way, is imported by four tests and nothing else, and holds the only social contest
a human can play. The single largest obstacle is that the proceeding has no closing economy: its
verdict is the judge's default roll against a default obstacle, repeated each season until it binds
or the docket lapses, with no input from the speeches, the proofs or the accused.

## 1. What it is, as coded

Two bodies of code carry the name. Only (a) is reached by the season loop.

**(a) The roll the loop runs.**

| piece | file | what it does |
|---|---|---|
| module entry | `modules/social_contest/roll.py` (166 lines) | `obstacle(inp)`: opposition score / 2, else `obstacle_default`; minus the room (`reception_gain·reception + proof_step·proofs`), floored at `OB_MIN`; plus `forgery_quality`; capped by `obstacle_ceiling` (solved per pool when `ceiling_per_pool`). `roll(inp, rng) -> Margin(net, ob)` with `net = roll_net(pool) + net_boost(leverage, pool)`. No `World`, no state, no token. |
| composition row | `references/module_contracts.yaml:52` `social_contest.roll` (`entry: verb_call`) | the registrar fills `manifest.MODULE_ENTRIES` at driver construction |
| host input builder and adapter | `es/seam/wrappers/sigma.py` (`contest_input`, `_frame`, `resolve`, `odds_of`, `believed_input`, `believed_chance`) | reads the actor's pool, a person subject's score, the room's terms for a prize `heard_by: bench`, an examined Record's forgery quality, the act's `effort`; freezes `queries/inputs.py::SocialContestInput`; holds the return to a `Margin`; applies S27.4 on the returned pair; settles the margin's fraction |
| pool reader | `es/seam/wrappers/pool.py::faculty` | `max(vocation attribute, capability key)`, else `pool_default`; plus `POOL_ADDENDS` (`world_q.practice`) |
| dispatcher | `es/seam/contest.py` (`contest`, `grade`, `_returned`) | prize → provider by manifest row; depth cap; typed `ContestRefused` / `ContestError` |
| ladder | `es/seam/ladder.py::degree_of` | `degree_from_net(settled_margin, 0)`, a call into `engine/dice_engine/dice_engine.py`, never a copy |
| fold | `es/loop/resolve.py` (`_contest`, `_grade`, `_fold`); `es/loop/sides.py::sides_of` | one generator per act, `H(seed, tick, actor, "roll:<prize>:<act id>")`; band-keyed `writes_at` / `emits_at` |
| prize rows | `es/rosters.yaml` `contest_subsystems.prizes`: `a standing`, `a proposition`, `a matter` (`heard_by: bench`) → `provider: social_contest` | |

Verbs that reach it (printed from `VERB_TABLE`, §12 run 3): `tell`, `lie`, `arrest` (a standing);
`argue`, `determine`, `interrogate` (a proposition); `speak` (a matter); and by routing row, with no
prize, the graded inquiries `research`, `examine`, `surveil`. Band consequences: `argue` writes
`Person.pursuits` at Success and Overwhelming; `determine` opens a disposal Tenure with
`Tenure.degree` at Partial and better and moves the judge's pursuits at Success and better; `arrest`
opens a `detain`; `tell`, `lie`, `speak` and `interrogate` write `[]` in every band (their band
decides the emitted kind, and for `tell` what WITNESS deposits).

**The proceeding around the roll** (`es/loop/effects_information.py`, `es/queries/world_q.py`,
`es/state/gate.py`, `es/data/arrangements.py`, `es/arrangements.yaml`): `petition` mints a Record;
`carry` or `open_case` puts a matter on `World.docket` (a sequence of dicts: `date`, `matter`,
`arrangement`, `petition`); `convene` forms a sitting whose slot `open_case` fills; `speak` is heard
by the bench at the speaker's place; `determine` (gate basis `determination`, `may_determine`) opens
the Tenure kind the docketed arrangement row `disposes:` — `oblige` when the item names no row,
which is every computed case — and writes the matter back to `None`; MATTER lapses an item held
beyond `docket_lapse` (4) seasons (`matter.lapsed`). State the subsystem owns: none in the module;
in `World`, the docket and the disposal Tenures.

**(b) The kernel the loop does not run.** `K/` (16 files): a bout of up to `budget` exchanges
(`resolver.py::Bout.resolve`) between two `Contestant`s before an `Adjudicator` or `Panel` at a
`Venue`; per-side `Standing`, `Reserve`, a `Room`, a stasis ladder, evidence `Dossier`s, fault
clinches (`DefeatCatalogue`), six win conditions (`ThresholdRace`, `TallyAtClose`, `ProofBar`,
`GraceThreshold`, `PersuasionTrack`, `VoteAtClose`), eight "canonical proceedings" and 13 further
venue presets (`modes.py`), typed surface tables (`dictionaries.py`), an adjudicator armature and
CR4/CR5 (`armature.py`, `rhetoric.py`, `appraise.py`), a pure-consumer chronicle (`narrative.py`),
a faction-vote adapter (`faction.py`), an interactive stdin harness (`agon_harness.py`) and a
389-check script (`_kernel_tests.py`). Three of its four "games" and three modes are stubs
(`wrapper.py::GAMES`, `modes.py::DyadicMode` and siblings).

**Execution evidence.**

- `python -m engine.season.harness.aperture 2 0` (the populated realm, 2 seasons, seed 0): `argue`
  attempted 41, executed 10 (5 `argument.won`, 5 `argument.lost`), refused 31 (`with=False`); `tell`
  attempted 48, refused 41 (`clause:hearer`); `lie` attempted 22, refused 16; `speak` attempted 25,
  refused 23 (`speech.unheard`, no docket item), executed 2 (`matter.turned`, both Failure);
  `determine` attempted 2, executed 0 (`clause:docket`); `open_case` 7 opened; `petition` 20 filed;
  `arrest` formed 1, attempted 0; `interrogate` formed 0. Pools: *"`argue`: pools rolled [2] over 9
  actors · two actors at different pools: no"*.
- A per-season probe on `build_realm(seed)` (§12 run 6). Seed 0, six seasons: `matter.determined`
  1 (Partial, season 5), `matter.undetermined` 2 (seasons 4 and 6), `determine.refused` 3,
  `matter.lapsed` 8 (all in season 6, the first season `docket_lapse` 4 can fire), `speak` executed
  11 (10 Failure, 1 Partial), `argue` executed 41 (10 won, 31 lost; `pursuit.moved` 3), `news.told`
  16 against `tell.refused` 199, `case.opened` 11, docket length 8 → 14 → 18 → 23 → 31 → 29. Seed 1,
  six seasons: `matter.determined` 2, `matter.undetermined` 2, `determine.refused` 6,
  `matter.lapsed` 8, `speak` executed 25 (18 Failure, 2 Partial, 5 Success), `argue` executed 52 (9
  won, 43 lost), `news.told` 21 against `tell.refused` 261, `case.opened` 16, docket 10 → 16 → 21 →
  25 → 29 → 29. Both seeds together: 27 cases opened and 110 petitions filed in twelve
  seed-seasons, 3 determined, 4 heard and failed, 16 lapsed.
- Docket composition at seed 0 after two seasons (§12 run 11): 11 matters, all persons; every
  item's `arrangement` is `None` (14 of 14); two items hold both a date and a matter; benches over
  the docketed persons seat 2, 4 or 5; 2 of 83 persons hold any capability and none an attribute;
  no disposal Tenure exists.
- `python -m engine.season.harness.corpus_run` (143 cases, seed 0; §12 run 13): `DEGREES RESOLVED BY
  VERB` — `argue` 947 (Failure 660, Partial 156, Success 129, Overwhelming 2), `tell` 158, `lie`
  138, `speak` 19 (Failure 16, Partial 3); `determine` is in `VERBS ONLY REFUSED`; `arrest` and
  `interrogate` are never attempted; `BANDS THAT DIFFER`: `interrogate`, `lie`, `speak`, `tell`
  False; the ARC bar reads *"ENDS = NOT-COMPUTABLE — closed by W23 (contest results) + W26 (binding
  decisions)"*.
- The module: `roll(inp, random.Random(7))` twice returns the same `Margin` (seeded, parameter
  generator). The default pair (pool 2, no opposing score) deals exactly Failure 0.74, Partial 0.19,
  Success 0.07, Overwhelming 0.00 (`band_odds`).
- The kernel: `python -m systems.social_contest.sim.contest._kernel_tests` → `RESULT: 389 passed, 0
  failed`. One `resolve_contest` call moves the process-global `random` stream and returns
  `('committee', 'win')`.

So: an NPC-versus-NPC social contest does happen with no player (every figure above is the shipped
chooser on a seeded realm). What rarely happens is a proceeding that closes.

## 2. Steelman

Ranked by the weight each bears.

1. **The seam is right, and it is the hard part.** One roll owner, one obstacle owner
   (`ED-SC-0033` cl. 3), one ladder (a call, with a test that monkeypatches the owner), a `Margin`
   and never a winner across the module boundary, a per-act generator so adding a contested verb
   moves no other act's draw (`04` PART D row 35), a typed refusal the fold turns into the row's own
   refusal kind. *Attack:* swap the entry for one returning a winner — `sigma.resolve` raises naming
   the entry (`:535-542`); read `degree_of` for a second band table — none. *Survived.*
2. **Contests are graded and the grade is used as data.** Band-keyed `writes:` and `emits:` on every
   contested row; `Event.degree` set on the one path; `tell`'s band decides whether and how
   faithfully the hearer holds the claim. *Attack:* the realm probe — `argument.won@Partial` (no
   write), `argument.won@Success` with `pursuit.moved`, `news.told@Partial` and `@Success` all occur.
   *Survived* for the success side; the failure side has no consequence (F-SC-10).
3. **The Proceedings design was built loop-native, not as a nested engine.** A hearing is acts by
   persons across scenes (`petition`, `carry`, `open_case`, `convene`, `speak`, `determine`), so it
   inherits propagation, witness, memory and the scene clock for free, and a proceeding "is just
   defined parameters" (`arrangements.yaml`). *Attack:* is any of it reached by computed play? The
   docketing half is (7 cases, 20 petitions in two seasons); the closing half rarely (F-SC-01); the
   parameters not at all (F-SC-06). *Survives as architecture, fails as play.*
4. **Keeping the 166-line roll over the kernel was measured, not assumed** (`roll.py:16-37`, SC-01
   step 15). *Attack:* re-ran three of its four claims — no generator parameter, global stream moved,
   winner returned. All reproduce. *Survived.*
5. **What a person cannot know stays hidden.** `believed_input` returns `None` where a factor is
   unknown; `decision/` cannot name `world_q`. *Attack:* nothing deposits a `capability:` claim, so
   a believed opposition is `None` for everyone and the chooser's odds term is silent for any
   contested act against a person who holds a score — today nobody does, so the term speaks
   everywhere and says the same thing. *Holds vacuously.*
6. **The honest default.** Every magnitude is an injected, swept fixture with a register row
   (`pool_default`, `obstacle_default`, `obstacle_ceiling`, `reception_gain`, `proof_step`,
   `docket_lapse`, `bench_quorum`); none is typed into a body. *Survived;* the cost is that the
   realm plays entirely on the defaults (F-SC-03).

## 3. Adversarial findings

Ranked worst first. "Falsifier" is the run that would have shown the claim wrong, and its outcome.

**F-SC-01 · blocks a requirement (R-04, R-05) · A proceeding rarely closes, and when it does nothing
said in it decided it.**
Claim: in computed play the chain docket → hearing → verdict completes three times in twelve
seed-seasons (27 cases opened), about five matters lapse for each one determined, and the verdict is
the judge's `pool_default` against `obstacle_default`.
Evidence: §1's runs; `workplans/valoria_master_workplan_v11_part3.md:281` (the 2026-11-01 probe:
*"`determine` never executed … no docket item named its row"*); `es/tests/test_sc01_the_bar.py:63-69,
:144-146` — THE BAR passes only at `pool_default` 30, *"OFF THE SWEEP"*, on two runs found *"in 1815
runs"*; `verb_table.yaml` `determine.contests_note` (*"the roll is the same for every party"*).
Causes, each read at its site: (i) `determine` forms about once a season and is refused at the
`docket` or `party` clause (aperture: 2 of 2; spine: 4 of 4); (ii) at the default pair it fails 0.74
of the time and Failure writes nothing; (iii) no computed case names an arrangement
(`effects_information.py:412-418`), so every disposal is `oblige`; (iv) `speak` is refused 23 of 25
times because the matter it addresses is not docketed.
Falsifier: a realm run showing `matter.determined` — **present: seed 0 once (season 5, Partial),
seed 1 twice in six seasons**. The claim is therefore "rarely", not "never"; the first draft of this
finding said never, on a two-season reading at one seed, and the control corrected it.
Consequence: the game's most distinctive scene produces filings and failed speeches. No trial ends,
so no sentence, no ban, no pardon, no appeal, no precedent.
Fix: B10-18c as scheduled (CR-57 to CR-64) for intake and rows; SC-P6 (acquittal) and SC-P3 (the
hearing fixture and choice) for the closing economy; cross-lane, formation (F-SC-10).

**F-SC-02 · blocks the standing requirement · Two owners of one subsystem, and the played one is the
one the game does not run.**
Claim: `K/` and the loop each own a proceedings roster, an obstacle, a bench ballot, evidence and
standing; the loop's are the ones the game follows; `K/agon_harness.py` is the only social contest a
human can play.
Evidence: `K/modes.py:485-519` against `es/arrangements.yaml`; `K/resolver.py:158` (`base_ob`)
against `roll.py:89`; `K/resolver.py:98-147` against `world_q.py:737`; importers of `K/` (§12 run 9:
four test files). `ED-SC-0033` cl. 2 rules the retirement.
Falsifier: any non-test import of `systems.social_contest` under `engine modules tools` — none.
Consequence: a designer or a port reads 6,700 lines, 389 green checks and 31 exported parameters and
takes them for the game. The standing requirement's "one code path, not two" fails in both
directions (a standalone the loop cannot reach; a loop path the standalone does not exercise).
Fix: SC-P2 (retire whole, after SC-P3 moves the played mode).

**F-SC-03 · degrades narrative (R-06, R-09) · In the realm a contest does not depend on who
contests, and between persons it is not even.**
Claim: every realm roll is 2 dice against Ob 2 (or Ob 1 where a subject holds a key at the default);
where scores exist an equal opponent is a rising disadvantage.
Evidence: aperture (*"pools rolled [2] over 9 actors"*); `harness/populated.py:1016`
(`cast_attributes: bool = False`); exact odds (§12 run 8): equal pairs s = 1 / 4 / 12 → P(Failure)
0.350 / 0.488 / 0.606; 6 against 3 succeeds 0.570, 3 against 6 succeeds 0.052; pool 2 against a held
score of 2 fails 0.42, against no score 0.74 (H-127's inversion). Cause: a die nets
`MU_PER_DIE` 0.4 and an opposing point costs 0.5 (`roll.py:141`, RULED form).
Falsifier: two realm actors at different pools in aperture's `pools` line — none.
Consequence: characters built "robustly" differ in what they attempt and never in whether they
succeed; a master orator and a mute have one distribution.
Fix: the flag is CHAR's (CR-20's carrier is landed; the cast's `stats:` are not seated). The rate is
RULED: SC-P5, held back, §11.

**F-SC-04 · degrades narrative (R-01, R-02 legibility) · The roll that decided a contest is not in
the log.**
Evidence: `loop/resolve.py:406, :866`; `state/carriers.py::Event` (no margin, pool or obstacle);
H-284. Falsifier: fold one `argue` and read the Event — band only (H-284's author re-confirmation;
the fields were re-read here, the fold was not re-run `[UNVERIFIED re-run]`).
Consequence: no chronicle, player or later mechanism can say why a side prevailed or how narrowly.
Fix: SC-P1.

**F-SC-05 · degrades narrative (R-02) · A hearing has one terminal state, and speech does not reach
it.**
Claim: (a) `determine` at Failure writes `[]` and the standing sitting question re-asks the bench
each season, so the contest decides when a docketed person is bound, never whether (H-162 (c), the
register's own words); (b) `matter.carried / advanced / held / turned` have no reader, and `speak`
writes nothing in any band; (c) the band a verdict lands in is stored on `Tenure.degree`, whose one
reader filters to `commit` edges (`queries/faction_q.py:146`).
Falsifier: grep for a reader of the four `matter.*` kinds under `es/` non-test — harness comments
only; grep `.degree` readers — the hash, the gate's diff, `faction_q`.
Consequence: an accused cannot win, an advocate cannot help him, and a narrow conviction is the same
conviction as a crushing one.
Fix: SC-P6 (dismissal); CP-T05-01 and CP-T05-02 (i) (`hearing`, held on a design whose approval is a
merge, not a ruling); SC-P4 (band-keyed `disposes:`).

**F-SC-06 · degrades narrative · "A proceeding is just defined parameters" is true of the loader and
of nothing that plays.**
Evidence: `arrangements.yaml` nine rows × thirteen keys; readers under `es/` non-test: `disposes`,
`disposal`, `quorum` (§12 run 10); `speech_kinds` none; a computed docket item names no row.
Falsifier: `DOCKET_ARRANGEMENT` non-`None` on any item after a realm season — none: 14 of 14 items
read `None` at seed 0 after two seasons (§12 run 11); the plan's own probe read 0 of 10 and 0 of 5.
Consequence: trial, tribunal, inquisition and excommunication are one act with one consequence.
Fix: CR-60/CR-61 (plan); SC-P4 for the unread keys.

**F-SC-07 · blocks the standing requirement · No decision exists inside a social contest on the
live path.**
Evidence: `sigma.py:459-460` (`host` accepted, unused); the choice a `speak` carries is its subject
and its `effort`; `world_q.proofs` spends the whole inventory. Falsifier: any operand of a contested
social row read by the roll other than `effort` — none in `_frame`.
Consequence: nothing to play. Fix: SC-P3.

**F-SC-08 · degrades narrative (R-02, R-08) · Most social acts die before the roll, and a failed one
costs nothing but its scene.**
Evidence: aperture — `argue` 31 of 41 refused (`with=False`: the hearer is not with the arguer),
`tell` 41 of 48 and `lie` 16 of 22 (`clause:hearer`), `speak` 23 of 25 (`exists:DocketItem=0`); the
four-season probe's `tell.refused` 115 against `news.told` 12. Failure bands of `tell`, `lie`,
`speak`, `argue`, `determine`, `interrogate` write `[]` (H-219: *no row has a Failure consequence to
gate*). Falsifier: a contested social row whose Failure band writes — `arrest` alone emits a distinct
kind and it never executes.
Consequence: the social layer's visible output is refusal. Formation is CORE's (the chooser aims at
hearers who are elsewhere and at matters not before a room); the failure economy is SC's and is
design-first (H-219, H-221).

**F-SC-13 · degrades narrative (R-06, R-08) · The chooser does not weigh a speech, and the verdict
does not read the judge.**
Claim: `decision/choose.py::_writing_bands` returns `None` for a contested verb that writes in no
band, so `odds_weight` is 1.0 and `settle_efforts` offers no `effort` variant for `speak`, `tell`,
`lie` and `interrogate`; and `determine` draws on no vocation, so a judge's convictions, regard and
skill do not enter his verdict.
Evidence: `choose.py:154-162, :165-175, :234-266`; `corpus_run`'s *"BANDS THAT DIFFER … interrogate
False · lie False · speak False · tell False"*; `rosters.yaml: verb_capability` (no `determine` row);
`verb_table.yaml` `determine.contests_note`.
Falsifier: an `effort` operand on any executed `speak` act in a realm run — not searched for in the
log `[UNVERIFIED by run; established by reading the one function that forms the variant]`.
Consequence: persons differ in which social act they pick and not in how hard they press it; a
harsh judge and a lenient one are one distribution. Fix: SC-P3 edit 3 (speech writes a stage, so the
existing chooser code prices it); CP-T05-01 (`opposed`); CR-92 for the judge's faculty. §15.

**F-SC-14 · degrades narrative (R-02, R-07) · Evidence is typed where it is held and a scalar where
it is used; nothing said in a hearing can be answered.**
Evidence: `world_q.py:852-879` (one float; mirror by holding); `sigma.py::contest_input` (room terms
only for `heard_by: bench`); `rosters.yaml: proofs` and each row's `proofs:` unread. Falsifier: an
act payload naming a cited claim or Record on any contested social row other than `tell`/`lie`'s
`said` — none in `verb_table.yaml`. Consequence: a case cannot be built item by item, broken by a
contradiction, or spoiled by a forgery. Fix: SC-P8. §16.

**F-SC-09 · hygiene with a Layer-1 edge · `reception` and `proofs` read other persons' ledgers at
RESOLVE.**
Evidence: `world_q.py:833-848` (each judge's ledger), `:877-879` (the opponent's); `04` §B.2 F8;
`ED-SC-0040`'s superseding row (option B, closed). The breach ships; it is nearly inert (the mirror
zeroes proofs; the fixed ceiling clips a hostile room). Fix: the SC-02 re-source build, which is held
on a merge-default approval, not on Jordan.

**F-SC-10 · hygiene, a plan defect · SC-05's carried block describes a path the code does not have.**
It schedules forwarding `degree_extension.py` at `seam/ladder.py` with *"Hash: none"* and a falsifier
about a `tell` *"the old extension demoted"*. `degree_of` applies no extension (`ladder.py:262-264`).
Fix: SC-P2 edit 5.

**F-SC-11 · hygiene · Registry and export surfaces describe the kernel.**
`references/module_contracts.yaml:464-486` (`sim_module`, `resolver: dice_pool`, `persuasion_track`,
*"reached live only via emergency_council"*); `engine/engine_params/sim_params.json` (31
`social_contest` keys, among them `_kernel_tests.py` constants); `es/requirements.yaml`'s scale row
for social contests (`in_loop: 'seam unbuilt'`, *"4 of 45 verb rows declare `contests:`"*) against
11 rows that do and 7 routed to this provider. Fix: SC-P2 edits 3–4; §8 step 1.

**F-SC-12 · hygiene · Test strength.** THE BAR's fixture (`pool_default` 30) saturates every roll it
reaches, so it cannot observe a failed contest at the shipped arm, and says so. The kernel's 389
checks assert a model the game does not execute; many are tolerance bands fitted to their own seeded
stream. `test_sc01_provider.py` plants the kernel's winner shape and is the right kind of test.
`[SKIPPED partial: `K/_kernel_tests.py` lines 520–1727 read by outline; `es/tests/test_sc0*.py`
not opened except the bar's header]`.

## 4. Code matters

- **Ownership and duplication.** Live path: single owners hold (roll, obstacle, ladder, pool reader,
  docket query `docketed`, bench `judging_set`/`sits_over`, `BENCH_BASIS`). Duplicated across the two
  bodies: everything in F-SC-02. Within the live path one doubling: the S27.4 refusal is evaluated on
  a hand-declared obstacle in the fold and on the derived pair in the provider — stated as one rule
  with two operands (`sigma.py:498-507`); accepted.
- **Dead or unreached.** `K/` whole. `arrangements.yaml: speech_kinds`. Ten arrangement keys.
  `seam/contest.py:284-300`'s two trailing `Unspecified` raises (no prize row lacks a provider;
  kept live by its own note). `seam/ladder.py::ladder_error` (returns `""` always).
  `CAPABILITY_CLAIM` has a reader and no depositor.
- **Contract and seam fidelity.** Against `04` §A.2: the module conforms (typed input, typed
  outcome, no token, no state, reached by composition row). Declared deviations: the adapter takes
  `World` (CONVENTION, `combat.resolve`'s precedent); the seam's return is a dict, not a `Margin`
  (typed only at the module boundary). Undeclared until `ED-SC-0040`: F-SC-09. Against
  `references/module_contracts.yaml`: the composition row is right; the module row is stale
  (F-SC-11).
- **Determinism.** Live: per-act generator, parameter-passed; a hand call with `rng=None` makes a
  fresh unseeded `Random()` and never touches the global stream (`sigma.py:533`). Kernel:
  `random.gauss` / `random.uniform` / `roll_net(rng=random)` on the global stream
  (`K/resolver.py:32, :139, :144, :334`).
- **Performance.** Not a constraint: one `roll` is microseconds (`roll.py:33`); the realm season's
  cost is elsewhere (17 s, 55 s, 190 s, 341 s for seasons 1–4 at seed 0 under a loaded machine — a
  CORE matter, noted because it bounds how far any SC instrument can sweep).
- **Test strength.** §3 F-SC-12.

## 5. Design matters

**One subsystem or two (the special charge).** As rulings: one — the Proceedings subsystem *"owns
all social contests"* and the orphaned code retires (`ED-SC-0033`). As code: two competing owners of
the same facts (F-SC-02), with no call between them. They are not layers of one design: the kernel
is a bout simulator with its own inputs (faculty, standing, dossier), its own roster and its own
outcome vocabulary (`a`/`b`/`draw`, track bands, `committee`); the Proceedings build is acts on the
world's own carriers. Nothing the kernel computes can be handed to the loop without a rewrite of its
entry (no generator, a winner where a margin belongs, a second obstacle). What the kernel has that
the loop lacks is design, not code: a per-exchange choice, defeat by a named fault, a verdict that
can cross the room, a chronicle of the bout's shape. Each has a loop-native home (SC-P3, SC-P1).

**Four models, one name (the design set and the earlier audits, as referents).** The archived head
`social_contest_v30.md` (read in full; intent only) describes a paired-exchange game: Appraise, a
style pick, both orators roll and the higher wins (CLASH / REINFORCE / CROSS / TIE), strain against
Face, Concentration, a Persuasion Track, then Obligations that bind for seasons, chain contests
that resume where a compromise left the track, a three-way heresy verdict (acquittal, insufficient
evidence, tribunal), a Domain Echo into faction state. The three-lens audit
(`.audit/2026-08-06-social-contest-three-lens-audit/00_synthesis.md` §0) found *"three resolution
models wearing one name"*: that prose (no engine), the kernel (a different, per-move loop absent
from the prose), and a legacy pool-compare stub. Re-verified at `601e715`: the stub is deleted; the
kernel still cannot be given a Style through `build_contest` and `_resolve_agon` still builds a
`Bout` with no armature (`K/wrapper.py:110-111, :215-216`), so everything ratified at Gate C remains
unreachable from the kernel's own public entry; that audit's F9 (`hard` costs 5 against `advance`'s
3 and runs identical code, `K/resolver.py:375-408`, while `K/agon_harness.py:328` calls it *"a
bigger swing"*) is still true; its *"live campaign path resolves every contest as `logos_spammer` vs
`logos_spammer`"* is now false — that path was deleted with the campaign driver. The season then
added a fourth model, the one-sided roll under the Proceedings acts, which is the only one the game
runs. Of the archived intent, the loop carries: Obligations (a `determine` opens an `oblige` with a
term that lapses at MATTER — the binding commitment, with no violation consequence); the three-way
verdict not at all (SC-P4, SC-P6 restore two of its three ends); the chain contest only as a
memoryless re-hearing (SC-P3's case-file stages give it memory); the Domain Echo not at all, by
Layer 1's ruling that a faction is a view. The paired compare of §4 Step 4 is the archived form of
§11 item 1's option; the ruling of 2026-08-14 is later and governs.

**The duality doctrine (`auto_manual_resolution_duality_v1.md`, `ED-SC-0013`, RULED 2026-07-08).**
*"Auto = the contest kernel run headless, played = the same kernel run interactively. Not two
mechanics — one engine at two fidelities … same engine ⇒ consistent by construction."* This is the
standing requirement's one-code-path clause, ruled four months earlier. It names the kernel as the
engine; `ED-SC-0033` and `ED-SC-0037` (both later) changed which engine. The principle survives the
change of engine and is what SC-P3 implements: the played hearing and the automated one are the
same season acts, chosen by a callback or by the chooser. Its calibration fork C (how close auto and
played must be) dissolves for the same reason the doctrine gives. Its "Witness" middle fidelity has
no loop form and none is proposed.

**What SC-05 should be (ladder first).** (1) Superseded/ruled: yes — retirement is ruled;
`A1-58` makes the timing the plan's. (2) Irrelevant: the adopt-or-keep question is, since SC-01 step
15 measured that the kernel cannot be the entry. (3)–(4) not needed. (5) Architecture: delete whole,
forward nothing, after the played mode has moved. Nothing survives to Jordan on SC-05 itself; one
consequence does (§11 item 2).

**Rulings accepted as binding and not re-raised:** `ED-SC-0033` (ownership; row dispatch; single
obstacle owner), `ED-SC-0034` (aggregates as Queries; pool-only latitude; no deprivation), `ED-SC-0035`
(pressure is the gap; no second-person lever), `ED-SC-0037` (the σ-leverage d10 resolver),
`ED-SC-0038` (per-matter outcomes; binding in scene), `ED-SC-0039` (the design is intent only),
`ED-SC-0040` (option B), Jordan 2026-08-14 (`score/2` plus instance modifiers; one ladder),
2026-09-05 (no base Ob by scale), the rosters ruling that investigation is not a contest, `ED-1094`.

**Where intent, ruling and code disagree.**

| subject | intent or ruling | code | cost |
|---|---|---|---|
| a failed determination | #453 §9.6 (intent): an acquittal | nothing happens; re-heard | no acquittal (F-SC-05) |
| per-matter outcome vector | `ED-SC-0038` (RULED): win one item, lose three | one margin per act; one matter per item | bundles and conditions unrepresentable; not built, not scheduled by name |
| binding in scene | `ED-SC-0038` (RULED) | a `determine` binds at its own RESOLVE: holds | — |
| the room reads the speaker | `PS/19_PLAN` 17–18 (intent) vs `04` F8 (ratified) | ledger reads ship | F-SC-09 |
| issue ladder (stasis) | `PS/03` `ladder: issue` | only Fig. 27's concession ladder, as `speech_kinds`, unread | the best-grounded historical primitive is absent |
| twelve parameter rows | intent | nine seeded, none bound by computed play | F-SC-06 |
| the nested run | `PS/21` step 15 | unbuilt; one `speak` is one draw | F-SC-07 |

**NERS cuts.**

- *The kernel* fails N from every direction the season can look (nothing reads it, nothing feeds
  it); it holds in one direction only — a human at a terminal — which is "narrowed, not passing". Cut
  it; what dies is a played bout, which SC-P3 re-homes.
- *`determine` as the judge's roll against the party* survives N (cut it and a verdict is a fiat
  write) and fails R as built: no strategy, no variety in resolution, and an extreme (Failure) that
  does nothing — *"a mechanism breaking at its extremes fails"*. SC-P6 and the `hearing` operand are
  what R asks.
- *`speech_kinds` and the ten unread keys* fail N today; they pass only with a reader (SC-P4).
- *`effort`* survives: one lever, priced in scene slots, on the μ-shift channel, used by NPCs
  (`settle_efforts`) and a player alike. Cutting it would leave the social roll with no choice at all.
- *The per-pool ceiling* survives N (M-7, no deprivation) with an S flag it states itself: at an
  `effort` boost the chance at each pool's own cap is not monotone in the pool (`roll.py:112-114`).
- *E, last:* the live path is 166 lines of module and about 700 of host for a legible four-band
  result — a good ratio. The Proceedings data is a poor one today: 300 lines of rows for one read key.

**Design that exists only as prose and is not yet game:** latitude (the pool multiplier),
interposition kinds, frank-speech licence, aptness priced not refused, the multilateral tally as a
general rule (one declared row exists), the legitimacy index (CR-65), membership contests (CR-66),
negotiation as a played game (the row is seeded; `mutual` disposal has no computed route), every
kernel "game" but the agôn.

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Hole-register rows (primary)

| id | listed | verified | evidence | action |
|---|---|---|---|---|
| H-126 | open | open | pools `[2]` for all realm actors | CHAR: seat cast attributes; SC adds rows for `lie`, `interrogate` (SC-P7) |
| H-127 | open | open; inversion reproduced | 0.42 vs 0.74 at pool 2 | G-14: no floor |
| H-87 | open | open (an injected default, 2) | `contest()` depth always 0 from `_contest`; the cap is unreachable by a social prize (no nested contest exists) | leave; it binds when a nested run exists |
| H-131 | open | **closed** | `World.write`'s `finally: self.gate.close()` (`state/world.py` ~:1000); `gate.py:1893-1898` | G-18: close the row |
| H-132 | open | wrongly filed (FA/CORE: grant reduction basis) | not an SC fact | to FA lane |
| H-137 | open | wrongly filed (CORE); closed for Tenures at CR-06 per its cite | — | to CORE |
| H-141 | open | wrongly filed (CORE) | — | to CORE |
| H-142 | open | wrongly filed (FA/CORE) | — | to FA |
| H-143 | open | wrongly filed (CORE) | bears on SC only in that `determine`'s shared predicate keeps `NotYours` unreachable (`effects_information.py:581-586`) | to CORE |
| H-100 | closed | closed (IN-31, ruled 2026-10-21) | `REVOCATION_DISPOSAL` | none |
| H-113 | open | **closed** | `resolve.py:533` `row.emits_at(_degree)`; the row's own closure note | close the row's index status |
| H-120 | open | **closed (stale)** | every prize is claimed (§12 run 3) | G-16 |
| H-174 | open | answered (J-17: jurisdiction follows presence) | `gate.py:939-945` | none |
| H-213 | open | open (an injected default, swept; per-pool arm shipped) | `roll.py:152-154` | none |
| H-226 | open | **superseded in part** | `interrogate` is a resolvable row; formed 0 in aperture | G-17 |
| H-228 | open | wrongly filed (SE/CORE: `raze`) | — | to SE |
| H-261 | open | wrongly filed (FA: decree reach) | — | to FA |
| H-276 | open | **closed** | `sigma.py:210` (`opposition = None if subject == claimants[0]`); probe: self-plea opposition `None` | G-15 |
| H-284 | open | open | F-SC-04 | SC-P1 |
| H-288 | open (RULING) | open; reproduced exactly | §12 run 8 | SC-P5, §11 |
| H-296 | open | open, not re-run; `arrest` never executes in the realm | aperture | follows H-288 |
| H-321 | open | open; reproduced | aperture pools line | CHAR (flag) |
| H-353 | open | wrongly filed (FA) | — | to FA |

Secondary rows that bear on a finding: H-162 (c) (no acquittal; SC-P6), H-215/H-216 (room terms;
F-SC-09), H-217 (`succession` row; CR-35's), H-219/H-221 (Failure consequences; design-first),
H-281 (unread keys; SC-P4), H-210 (forgery quality; read, inert at the fixed ceiling).

### 6.2 Workplan positions

| id | listed | verified | action |
|---|---|---|---|
| B10-13 / CR-83 | DESIGN-FIRST | open; a design file, no code | proceed |
| B10-18c CR-57…CR-64, CR-74 | BUILD | open; the batch's premise re-measured (F-SC-01, F-SC-06) | proceed; add SC-P1 before it (its exit probes need the record), SC-P6 after CR-61 |
| CR-65, CR-66, CR-67, CR-38, CR-92 | DESIGN-FIRST | open | CR-92 answers which faculty judges (G-21) |
| CR-39 | HELD on CR-38 | open | none |
| SC-02 | HELD on its design's approval | the design is written; approval is the merge default (`ED-1094`) | not Jordan's: merge and release |
| CP-T05-01, CP-T05-02 (i) | HELD on SC-02 | open; these are what make speech reach a verdict | release with SC-02; highest-value SC build after the record |
| SC-05 | HELD on B10-18c | decided here | SC-P2 |
| SC-07 | BLK: a carrier per item | open; P-4 (recorded defeat) gains a carrier with CR-36/37's `resolution` Record | none |
| NM-W1 | HELD, partly landed | not SC's | — |
| CR-27, CR-31, CR-55, CR-56, CP-T05-02 (ii)(iii), CP-T05-03, CP-T05-04 | LANDED | landed (`lie` executes in aperture; `matter.lapsed` is declared and not yet seen in 4 seasons at lapse 4, as expected) | none |
| CR-35, CR-36 | BUILD (B10-17) | open | SC-P4's Record disposal waits on them |
| CP-T05-05 | CUT (?) | not opened `[UNVERIFIED]` | — |

### 6.3 Inconsistencies, gaps and unclear passages — decided resolutions

| # | what | resolution | ladder step | carried by |
|---|---|---|---|---|
| G-01 | two owners of the social contest | retire `K/` whole | 1 (ruled) + 5 | SC-P2 |
| G-02 | SC-05 forwards an extension the live path never applied | forward nothing; keep `BandExtension` in its owner | 5 | SC-P2 |
| G-03 | `module_contracts.yaml` `social_contest` row describes the kernel | repoint `sim_module`, `resolver`; drop the state row and note | 5 | SC-P2 |
| G-04 | `sim_params.json` exports kernel constants | re-derive by the exporter after deletion | 4 (exporter is the owner) | SC-P2 |
| G-05 | `requirements.yaml` scale row says the seam is unbuilt | rewrite the row to the measured state: *roll in loop through seven rows; proceedings close about once in seven seed-seasons* | 3 (code decides) | §8 step 1 |
| G-06 | ten arrangement keys and `speech_kinds` read by nothing | cite a reader at B10-18c's close or delete the key | 4 | SC-P4 |
| G-07 | a computed case names no arrangement | answered by plan: CR-60, CR-61 | 3 | — |
| G-08 | a verdict's band changes nothing a reader sees | `disposes:` may be band-keyed | 5 | SC-P4 |
| G-09 | no acquittal | Failure dismisses; take H-162 (c)'s revert | 3 | SC-P6 |
| G-10 | the roll's operands are dropped | `Event.ending` | 4 (combat's precedent) | SC-P1 |
| G-11 | speech does not reach the verdict | answered by plan (CP-T05-01, CP-T05-02 (i)); the hold is a merge, not a ruling | 3 | SC-P3 names the edge |
| G-12 | F8 breach in `reception` / `proofs` | answered (`ED-SC-0040`, option B); build the re-source | 3 | — |
| G-13 | an equal opponent is a rising disadvantage | RULED form; proposal held back | survives | SC-P5, §11 |
| G-14 | H-127: a low held score is easier than none | no floor; the stand-in's size is its own swept value | 5 | SC-P5 item 2 |
| G-15 | H-276 open in the register, fixed in code | close the row, citing `c627426a` | 1 | register edit |
| G-16 | H-120 says three prizes are unclaimed | close: all five are claimed | 1 | register edit |
| G-17 | H-226 says `interrogate` is not built | rewrite to the residue: built, never formed in computed play | 1 | register edit |
| G-18 | H-131's open half (close at a barrier with no writes) | irrelevant: a window cannot outlive its write | 2 | register edit |
| G-19 | no person's skill varies | the flag is CHAR's; SC's reader is ready | 3 (CR-20) | cross-lane |
| G-20 | `PS/README.md` Status: *"Nothing exists in `engine/season/` until SC-01"* | strike the clause; point at `HANDOFF_SC.md` | 1 | owner edit |
| G-21 | which faculty a judge, an arrester, a liar and an interrogator roll | `lie` → `copying`, `interrogate` → `inquiry` (siblings); judge and arrester are CR-92's | 4; 3 | SC-P7 |
| G-22 | THE BAR passes only off the sweep | re-pin on SC-P3's fixture at shipped fixtures; delete `BAR_FIXTURES` | 5 (§0.1 pt 2) | SC-P3 gate |
| G-23 | a trait cannot reach the roll without code | one generic `trait` advantage source, rows in data | 5 | SC-P7 |
| G-24 | `K/` Gate-C ratifications (armature, CR4, CR5, epideictic compression) concern code that retires | they lapse with their subject unless Jordan keeps one as design input | survives | §11 |
| G-25 | `ED-SC-0038`'s per-matter vector is ruled and unbuilt, with no position by name | one docket item per matter already gives one margin per matter; a BUNDLE is several items opened by one act — design-first under B10-18c's CR-61 (the case file names its matters) | 5 | §8 step 9 |
| G-26 | the lane research file (`research/by_lane/SC_social_contest.md`) describes `speak` as uncontested and `argue`/`seize` as absent | stale at HEAD (D_T05 rows 71–73 already say so); the file is dated reference — no edit, cite D_T05 | 2 | — |

| G-27 | the chooser prices and puts effort behind only contested verbs that write; a speech writes nothing | a carried or advanced `speak` writes a stage on the case file; the existing rule then covers it | 5 | SC-P3 edit 3 |
| G-28 | the hearing's consequence: bench ledgers (F8) or bench commits (SC-02) or the proceeding's own record | the case file (a World Record) is the carrier; CP-T05-02 (i)'s arithmetic unchanged | 5 | SC-P3 edit 3 |
| G-29 | a choice inside a hearing must be the same for player and NPC | proofs subset and plea are Candidate variants, formed as `effort` is | 4 (`settle_efforts`) | SC-P3 edit 2 |
| G-30 | evidence reaches a contest as one float; the proofs roster and each row's `proofs:` are unread | cited, typed entries admitted by the row | 4 (`tell`'s held-claim rule) | SC-P8 |
| G-31 | the only answer to a proof is silently holding the same claim | rebuttal by a held contradiction strikes the entered proof | 5 | SC-P8 |
| G-32 | a forged Record in a hearing: *"counted as a proof until examined"* is listed unbuilt | it counts until an `examine` finding names it forged, which strikes it | 3 (`PS/19_PLAN` step 25, intent) | SC-P8 edit 5 |
| G-33 | archived intent adds dice per Finding cited; the code moves the obstacle | the code's placement is kept (ruled obstacle form); named in SC-P8 | 3 (ruling) | SC-P8 |
| G-34 | the walkthrough's *"every number the resolver uses … the player can see"* (`.audit/`) against the hidden room | the player sees what his character believes (`View.odds`) and, after the act, his own roll (SC-P1); the room stays hidden | 3 (code and `PS/15`) | SC-P1 |
| G-35 | `ED-SC-0013` names the kernel as the one engine at two fidelities | superseded as to the engine by `ED-SC-0033`/`0037`; the principle is kept | 1 | SC-P3 |

Resolutions decided: **35** (33 closed by the ladder; G-13 and G-24 survive to §11).

## 7. Research transfer

Read: `research/00_INDEX.md` (structure and the SC rows), `research/by_lane/SC_social_contest.md`
(§0–§3.1 in full; the remainder not paged — `[SKIPPED partial: lines 143–799]`),
`research/game_precedent_suite/dispositions/D_T05.md` (in full),
`research/social_contest_procedures/01–03` (headings and the three "For the engine" tables),
`research/rhetoric_oratory_contest/` (through the lane file's assessment, not re-read),
`research/game_precedent_suite/dispositions/D_T06.md` (in full, rows truncated at 640 characters).
Not opened: `tables/R4`, `R5`, `tutorials/T05`, `T06` (their content reached this audit through the
two dispositions, which cite them row by row), `research/by_lane/FI_fieldwork_investigation.md`,
the companion parts `[SKIPPED: named in §17]`.

**Changes what to build.**

- *Burning Wheel, Duel of Wits — the compromise scaled to what the winner lost* (lane file §2.2;
  `[UNVERIFIED]` for its failure mode). The precedent the lane judged to transfer best needs a reader
  of the verdict's degree. Used: SC-P4 (band-keyed disposal) is that reader in its cheapest form.
- *Dogs in the Vineyard — conceding is a priced move; the only conversion that survived the
  proceedings relay (P9).* Used: CR-62's plea through the obstacle; SC-P3 makes it a choice.
- *Griftlands — spend-and-roll persuasion was less fun than fighting; cards supplied a
  non-stationary per-turn decision* (T2; the Klei quote is repo-side and unverified in v3). Used as a
  warning against SC-P3's own risk: a `speak` menu that is the same every exchange. The proofs subset
  (a hand that depletes) is the non-stationary element; D_T05 row 12 ran the kernel harness and won
  by answering "1" every time, which is the failure SC-P3's falsifier is written against.
- *Guild 2 — the verdict weighs evidence (≤ 3 items) then rhetoric; a verdict scale from not guilty
  to death; a charge and a later trial date* (D_T05 rows 17–22). Used: SC-P6 (not guilty exists),
  SC-P4 (a scale), and as confirmation that docket-then-sitting is a shipped shape.
- *Venice and the inquisitions* (`social_contest_procedures/01`, `02`): every sourced procedure fits
  the thirteen arrangement keys, and *"in every row `appeal_basis` is a different authority than the
  bench … it never rehears"*. Used: supports CR-59 as written and argues for keeping `appeal_basis`
  when SC-P4's deletion runs; the Quarantia's separate guilt and penalty ballots are the historical
  form of SC-P4's band-keyed disposal.
- *Emergent-narrative requirements (via D_T05 rows 66–68): a complication-modal middle band; a "why"
  on every event.* Used: F-SC-08 (the modal outcome is Failure, 0.74, and writes nothing) and SC-P1.

- *The detective and noir set* (`D_T06.md` in full; §16): L.A. Noire — an accusation needs a held
  notebook item and a missing clue removes the option (the loop HAS this for `tell`; SC-P8 extends
  it to `speak`). Ace Attorney / Danganronpa — testimony set against a presented item; argument and
  rebuttal as the trial's structure (the loop LACKS both; SC-P8 edit 3 is the form that needs no
  authored truth: two held items compared). Pentiment — a judgment bound without a truth test and
  remembered by a community (the loop's `determine` is this shape; the remembering is WITNESS).
  Obra Dinn, Golden Idol, Shadows of Doubt's exact-match form — a verifier oracle; refused by axiom,
  and D_T06 row 3 records the precedent's own leak. Guild 2 — evidence with strength, believability
  and expiry, and belief with provenance (the loop HAS provenance and decay; SC-P8 makes them count
  in a hearing).
- *The three-lens audit's persistent-argument board* (`.audit/…/03_persuasion_documents_
  adjudication.md:84-130`, re-read): what cards fixed for Griftlands is non-stationarity of the
  per-turn decision, which a persistent board of standing claims supplies without cards, on the
  condition that general verbs can reduce every board state. Used: the case file's stages are that
  board (SC-P3 edit 3, SC-P8 edits 2–3); `speak` with `answers:` is the general verb.

**Tried, did not transfer.**

- *Ace Attorney's one correct statement per round and its penalty gauge.* Needs an authored truth
  and a human; refused by the relay. Only the present-against-testimony shape is used (above).
- *Triangle Strategy's Scales vote (persuade each voter once against a hidden threshold).* The loop
  has a declared vote (`world_q.declared_votes`, quorum) on one row that computed play cannot reach;
  the precedent would transfer only after CR-61. Not used now.
- *Victoria 3's enactment clock.* The docket's lapse is the only clock; parameters do not transfer.
- *Disco Elysium's shown odds.* The design hides the room; the season shows a constant. Display is a
  port matter.
- *The kernel's own classical grounding (stasis × genre, Nyāya self-gating).* The lane file finds
  stasis sound as forensic terrain and over-claimed where crossed with genre; the crossing retires
  with the kernel (G-24).

**Decorative.** The kernel's thirteen cross-cultural venue presets cite journals by DOI for `[SEED]`
numbers; no number follows from a source. The latitude floor (~0.7) read off a variance ratio in
firms is a surface analogy (lane file §1.3 pt 4).

**Nulls (findings).** No shipped game models argument content (N-1): neither resolver claims to.
No precedent in the corpus shows a simulation in which NPCs conduct a multi-stage proceeding to a
verdict without a player; the nearest (Guild 2, CK3) script the stages. Durability of attitude change
is unsolved in eight surveyed systems; `argue`'s `pursuit_shift` is an unanchored 0.1.

## 8. Best path forward

Proposal files (all `## Status: PROPOSED`; SC-P5 held back):
`…/proposals/05_SC_contest_record_on_event.md` (SC-P1), `05_SC_sc05_kernel_retirement.md` (SC-P2),
`05_SC_playable_hearing.md` (SC-P3), `05_SC_arrangement_rows_that_bind.md` (SC-P4),
`05_SC_opposed_obstacle_parity.md` (SC-P5), `05_SC_acquittal.md` (SC-P6),
`05_SC_capability_surface.md` (SC-P7), `05_SC_evidence_and_rebuttal.md` (SC-P8).

**To run well alone.**

1. *Edit.* Correct the owners that mis-state the subsystem: `es/requirements.yaml`'s social-contest
   scale row (G-05), `hole_register.yaml` H-276 / H-120 / H-226 / H-131 (G-15 to G-18),
   `PS/README.md`'s clause (G-20). Gate: `python -m engine.season.harness.register --requirements`
   exits 0. Unblocks: honest reading of R-04/R-09.
2. *Edit.* SC-P1 — the contest record. Gate: its test; a declared golden re-pin. Unblocks: the
   explanation B10-18c's narrow options wait on; every instrument below.
3. *Merge, then build (plan).* SC-02's re-source, CP-T05-01, CP-T05-02 (i). Gate: the plan's
   falsifier worlds. Unblocks R-02 inside a hearing (speech changes the verdict); removes F-SC-09.
4. *Build (plan).* B10-18c in its order. Gate: its exit probes at seeds 0–2.
5. *Edit.* SC-P6 — acquittal, after CR-61. Gate: its test and the realm probe (docket length no
   longer monotone). Unblocks R-02, R-09 (a hearing with two ends).
6. *Edit.* SC-P4 — band-keyed `disposes:`; the unread keys go at B10-18c's close. Gate: its test;
   seeded hashes equal. Unblocks categorical outcomes (R-04 contributor).
7. *Small build.* SC-P3 — `build_hearing`, `--play`. Gate: its two-run artifact. This is the step
   that makes SC a playable game of its own on the season's code path.
8. *Small build.* SC-P8 — evidence cited and answered, after CR-61, SC-02 and SC-P3. Gate: its
   three-part artifact on `build_hearing`. Unblocks R-02 and R-07 inside a hearing (what a person
   holds decides the case; a contradiction held by another answers it).
8a. *Small build.* SC-P2 — retire the kernel. Gate: hashes equal; exporter `--check`.

**To compose.**

9. *Design-first.* The bundle: one act opening several matters with conditions between them
   (`ED-SC-0038`), on CR-61's case file. Gate: a hand-built world where one hearing binds on one
   matter and dismisses another.
10. *Cross-lane (CHAR).* Seat the cast's attributes so pools differ (G-19); then SC-P7's rows.
    Gate: aperture's pools line reads *"two actors at different pools: yes"*. Unblocks R-06, R-09.
11. *Cross-lane (CORE).* Formation: `argue`/`tell` aimed at a present hearer, `speak` at a docketed
    matter (F-SC-08). Gate: aperture refusal shares for the three verbs below one half.
12. *Design-first.* What losing costs (H-219, H-221): a Failure band with a consequence on at least
    `argue` and `speak`. Gate: a control arm reproducing today.
13. *Held.* SC-P5, after §11 item 1.

## 9. Playable standalone and integrated

| point | exists today | missing | closes it |
|---|---|---|---|
| entry point | season: `harness/headless.py`, `populated.run`, `play_surface.dispatching_chooser`. Kernel: `python -m systems.social_contest.sim.contest.agon_harness` | a season entry that starts in a hearing | SC-P3 edit 4 |
| scenario seed / fixture | `governance_spine.build`, `probes.tiny_world`; `test_sc01_the_bar.py`'s swept seeds at `pool_default` 30 | a world with a fired sitting, a named row, a bench and two parties holding proofs | SC-P3 edit 1 |
| choice surface | verb, subject, hearer, `effort` (0–2) before the roll; `tell`/`lie` content by `said_of` (chosen for him) | a choice per exchange: which proof, which plea, attend or evade, for the judge bind or wait | SC-P3 edit 2; CR-62, CR-63 |
| outcome legibility | `Event.degree` and the kind; refusals carry `observed` reads | the roll's operands; the room's contribution | SC-P1 |
| stakes | `argue`: the hearer's pursuits; `determine`: an `oblige` (computed) with an unread degree | a disposal that differs by row and by band; a verdict speech can move; something to lose | SC-P4, SC-P6, CP-T05-02 (i) |
| end condition | `matter.determined` (rare), `matter.lapsed` (after 4 seasons) | acquittal | SC-P6 |
| instrument | `aperture`, the §12 per-season probe (scratch), `sigma.odds_of` | a kept reading of proceedings opened / heard / closed per season | SC-P3's `--auto` run is that reading; no new instrument |
| golden | realm goldens under `es/tests/` | a hearing golden | SC-P3's gate |

**One code path?** No. The standalone that exists (`agon_harness`) runs `K/`; the season runs
`roll.py`. After SC-P3 and SC-P2: yes — the standalone is the season loop on a fixture, the module
entry is the same `roll`, the player is a callback on the existing seam.

**Layer 1 conformance as a registered module.** Conforms: `social_contest.roll` is a composition
row with `entry: verb_call`; typed frozen input; `Margin` out; no token, no state; reached by string
(`sigma.py` imports nothing from `modules/`). Open: the wrapper's `World` read (declared
CONVENTION); F-SC-09 (answered, unbuilt); the module's contract row (stale, SC-P2).
`holonic_ARCHITECTURE.md` §43, §45–§47 were not opened `[UNVERIFIED]`; the conformance claim rests on
`04` §A.2 as quoted in the code and on the registrar's refusals.

**Integration (zoom in and out).** In: a contested act at RESOLVE dispatches by prize row; the
social prizes carry no `step:`, so they resolve in the round they are chosen and never suspend the
driver. Out: Events into the one log; receipts through the gate. There is no pause because there is
no scene to enter: a hearing is spread over scenes of the season. That is sound for an agent
simulation and is what SC-P3 keeps; a client that wants the hearing as one sitting presents the
same acts consecutively.

**No GM.** Everything a hearing needs a GM for in the kernel's design (adjudicator type, exchange
count, resistance, track start) is a venue parameter there and an arrangement key here. What still
needs one today: choosing the row a case is heard under (CR-61), choosing which proof is spent
(SC-P3), deciding that a failed prosecution is over (SC-P6).

**Ordered work:** §8 steps 2, 3, 5, 6, 7, 8.

## 10. Interfaces

| with | SC consumes | SC emits | real (executed) or designed |
|---|---|---|---|
| DICE | `roll_net`, `net_boost`, `band_odds`, `settle_record`, `degree_from_net`, `LEVEL_SIGMA` | — | real |
| CHAR | `Person.capability`, `Person.attributes` (through `pool.faculty`), pursuits (for `argue`, reception valence), ledger (proofs, `said_of`) | `Person.pursuits` (argue; determine's consequence), claims at WITNESS, `practice` dice from the log | real path, empty inputs in the realm (attributes unseated) |
| CORE (loop, gate) | docket, Dates, the scene clock, `Act.effort`, `via` | Events with degree; disposal Tenures through `determination`; `matter.lapsed` at MATTER | real |
| FA (governance, seats) | `judging_set` over seat `hold`s with the `determine` grant; `seat_faction` | `oblige` (joins `establishment_of`), `detain` (excludes from muster, `sides_of`), `ban` (revocation's cost uses the same kind) | real for `oblige` (rare); `detain`/`ban` by hand-named row or `arrest` (never executes) |
| FI (fieldwork) | Records as proofs' sources; forgery quality | the graded inquiries roll through this module (`grade`) | real; forgery inert at the fixed ceiling |
| PC (combat) | — | a failed `argue` does not hand off to `fight`; a yielded duel has no social reader | designed only |
| MB | — | a prisoner is not in the army | real (one read) |
| SE | place (`place_of`) as the room | — | real |
| WR / chronicle | — | Events; no contest record | designed (SC-P1) |
| GO (port) | — | `sim_params.json` kernel keys | real and wrong (F-SC-11) |

## 11. Survivors for Jordan

1. **What an equal opponent costs (H-288; SC-P5).** RULED today: Ob = score / 2. Option A keeps
   it: a social act is an attempt against a defence that is worth more than the attack, increasingly
   with skill; the status quo holds and moving anyone is uphill. Option B prices the opponent at the
   dice's own mean (0.4 per point): equal parties are even, and asymmetry comes from the room, the
   proofs and effort. A is a world of entrenchment; B is a world where the better arguer usually
   wins. Ladder: not superseded; not irrelevant (it governs every contested social act once scores
   are seated); the design documents restate the ruling; precedent (combat, mass battle) is
   two-sided but a different mechanism; the architecture is indifferent. It survives.
2. **Whether anything ratified for the kernel is kept as design (G-24).** `ED-1056` to `ED-1062`
   ratified, for `K/`: the Face scale-binding, weighted-by-standing panel ballot, the Guild
   Arbitration rebind, the venue-derived Guilds boost, the armature's fourth axis, the two-genre
   compression, CR5's scope. SC-P2 deletes their only implementation. Option A: they lapse with
   their subject (the retirement ruling is later and general; "the record dies when its subject
   dies"). Option B: Jordan names those he wants re-expressed on the Proceedings carriers (the
   weighted ballot on `declared_votes`; the armature as SC-P7 trait rows). A gives a smaller, single
   design; B keeps authored intent at the cost of re-deriving it. The ladder's step 1 points to A;
   it is listed because A overwrites ratified items by deletion.

## 12. Evidence log

Scratchpad: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/SC/`.

| # | command or probe | seed / seasons | outcome |
|---|---|---|---|
| 1 | `python -m engine.season.harness.register --requirements` | — | exit 0; met 3, partial 5, not_met 1 (`requirements.txt`) |
| 2 | `python -m engine.season.harness.aperture 2 0` | 0 / 2 | exit 0; figures in §1 (`aperture_2_0.txt`) |
| 3 | `VERB_TABLE` print of contested rows, prizes, capability keys | — | 11 rows contest; 7 through `social_contest`; table 67 rows |
| 4 | `python -m systems.social_contest.sim.contest._kernel_tests` (a script, not pytest) | 20260603 (its own) | `RESULT: 389 passed, 0 failed` |
| 5 | `resolve_contest` global-stream probe; `inspect.signature` | 123 | stream moved; no `rng` parameter; `('committee','win')` |
| 6 | `probe_realm.py <seed> <seasons>`: social Event kinds per season on `build_realm` | 0 / 6; 1 / 6 (and 1 / 3) | §1; `realm_seed0_6.txt` (hash `e324ea2b…`), `realm_seed1_6.txt` (hash `af2f6e40…`), `realm_seed1_3.txt` (hash `26d2091b…`; its three seasons agree with the six-season run's first three). Single run per seed: counts, not rates |
| 7 | the same probe, first attempt | — | **failed** (`ModuleNotFoundError`, no `PYTHONPATH`); caught by reading the output, re-run |
| 8 | exact odds: `band_odds` over `obstacle(SocialContestInput(…))` | — | tables in F-SC-03 and SC-P5; `MU_PER_DIE` 0.4; per-pool caps 2.0 / 2.842 / 3.6 / 4.23 |
| 9 | `grep -rnE "^\s*(from|import) systems\.social_contest"` over `engine modules tools tests` | — | four test files |
| 10 | grep of arrangement-key and `SPEECH_KINDS` readers under `es/` | — | `disposes`, `disposal`, `quorum` read; `speech_kinds` none |
| 11 | docket composition after two seasons (`matter` kind, `arrangement`, bench sizes) | 0 / 2 | 11 person matters, 3 empty slots; `arrangement` `None` on 14 of 14; benches 2 / 4 / 5; capability held by 2 of 83, attributes by 0; no disposal Tenure |
| 12 | self-plea probe: `contest_input(w, [p], verb="speak", subject=p)` on `probes.tiny_world` | — | opposition `None`; a third party against him: 14.0 |
| 13 | `python -m engine.season.harness.corpus_run` | 0 | exit 0 (`corpus_run.txt`): 143 cases; degrees by verb in §1; 23 of 67 verbs executed; `determine` only refused; ARC ends NOT-COMPUTABLE |
| 15 | exact odds at the proposed rate (`band_odds(6, 1.2)`, `band_odds(3, 2.4)`) | — | 0.630 and 0.124 Success or better; SC-P5's falsifier re-worded on this reading |
| 14 | `git status --short` | — | see the receipt |

Not run: `pytest` (by instruction). Not re-run: H-284's fold, H-296's arrest sweep.

## 13. Provided arcs and characters — adjudication

Corpus read: `es/cases/chain/CASE_BRIEF.md`; the 143 cases through `harness/run_cases.py::load_cases`
(972 needs: 427 core, 463 important, 82 flavour). A keyword pass found 240 needs in 105 cases that
mention a contest, hearing, vote, plea or persuasion; the table adjudicates the cases whose CORE
needs turn on this subsystem's mechanism. "Represented" means reached by computed play in a run
above, not declared. `corpus_run` (§12 run 13) is the corpus reading: over the 143 cases `argue`
rolled 947 times, `tell` 158, `lie` 138, `speak` 19 (16 Failure, 3 Partial); `determine` was only
ever refused; `arrest` and `interrogate` were never attempted; and the instrument reports the ARC
lane's endings as *"NOT-COMPUTABLE — closed by W23 (contest results) + W26 (binding decisions)"*,
which is this subsystem's debt to the arcs in the instrument's own words.

| case | need (short) | hardness | represented today? | evidence | change required | owner | proposal | gate |
|---|---|---|---|---|---|---|---|---|
| ARC-04 | an accusatory process advances through fixed stages on its own timetable | core | partly: a docketed matter ages and lapses; stages exist on the case file and mature at MATTER | `loop/matter.py:338-395, :437-457`; `open_case` executes (7 in 2 seasons) | stages that mean something (the rite's stage list) | SC | plan CR-60/61 | CR-61's exit |
| ARC-04 | a contest can defeat an accusation for now, the case file intact and reopenable | important | no | H-162 (c) | dismissal that keeps the file | SC | SC-P6 | its test (second `open_case` admitted) |
| ARC-04 | the patron chooses support / abandonment / extraction | core | partly: `speak` for another on his matter exists; extraction is not SC's | `speak` rows | advocate as a decision | SC, FA | plan CR-63 | CR-63's exit |
| ARC-05 | force a stalled private calculation into a public formal contest | core | partly: `petition` → `carry` dockets by right | `petition.carried` 2 per season | the contest must then resolve | SC | SC-P6, CP-T05-02 (i) | hearing fixture closes |
| ARC-06 | a ruling is separate from, and needs a separate act to, enforce | core | yes in shape: `determine` opens an `oblige`; `comply` / `evade / defy` are separate rows | `_disposal`; rows `comply`, `evade / defy` (emission-only) | enforcement with its own roll and cost | FA (with SC) | plan CR-63 (appear / evade / defy) | `compliance.given` above 0 |
| ARC-06 | implementation fails on its own roll, independent of how decisively the contest was won | core | no: nothing reads the verdict's degree; no implementation act rolls | `faction_q.py:146` | a reader of the degree, or explicit independence | FA | SC-P4 gives the degree a consequence | — |
| ARC-10 | introduce explosive tangential evidence mid-contest for a benefit and a wider cost | core | no: a `speak` spends all proofs, chosen by nobody | `world_q.proofs` | proofs as a chosen subset; the wider cost is WITNESS's fan-out, which exists | SC | SC-P3 edit 2 | its `--play` falsifier |
| ARC-10, ARC-21, ARC-31 | one contest, more than two outcome tiers with categorically different consequences | core | no: four bands, one consequence | `_eff_determine` | band-keyed disposal | SC | SC-P4 | its test |
| ARC-21 | a failed formal challenge weakens the challenger and strengthens the target | core | no | Failure writes `[]` | a Failure consequence | SC | SC-P6 (dismissal only); the cost to the bench is §8 step 12 | — |
| ARC-R18 | a formal vote can end with neither side at a majority | core | by hand only: a `declared` row with `quorum`; votes are live `commit`s | `world_q.declared_votes`; `arrangements.yaml` `excommunication_deliberation` | computed cases name a row; a `Record` disposal for a debate | SC, FA | plan CR-61; CR-36/37 | `docket_named_arrangement` above 0 |
| ARC-R18 | pre-vote persuasion of a third party, undone if a rival persuades him back | important | yes: `argue` moves pursuits; `commit` / `release` | `argue` executed 24 in 4 seasons | none in SC | — | — | realm probe |
| ARC-31 | a multi-exchange debate interruptible by an unrelated violent event | core | yes by construction once a hearing spans scenes: any act can fall between two `speak`s | scene clock (R-03) | a strain cost on whoever was mid-hearing | SC | SC-P3 (the hearing is season acts); the strain is §8 step 12 | hearing fixture with a planted `fight` |
| ARC-42 | cite a previously established, verifiable fact as a distinct bonus move | important | partly: a held deed claim is a proof; `proof_step` 0.25, mirror-zeroed in play | H-216 | SC-02 re-source (the mirror stops being total); chosen proofs | SC | plan SC-02; SC-P3 | SC-02's falsifier |
| ARC-42 | an insider's testimony is higher-credibility evidence because of his pedigree | important | no | — | a trait or office as an advantage | SC, CHAR | SC-P7 | its test |
| ARC-42 | the debate cannot occur until other storylines reach states | core | not SC's: convergence is a property of who dockets what | — | none | CORE | — | — |
| EMG-C4 | a multi-round contest where a designated champion may be substituted mid-contest | core | partly: any person may `speak` on a matter (an advocate) | `speak` rows; `subject_may_be_self` | substitution is free once the hearing is acts | SC | SC-P3; CR-63 (self or advocate) | hearing fixture |
| EMG-X6 | an asymmetric proceeding: one side denied an option, the other given an advantage | core | by data shape only: `floor`, `order`, `interposed`, `proofs` keys — all unread | F-SC-06 | the keys need readers | SC | SC-P4 (keep or delete); CR-62/63 | a row whose `floor: closed` refuses a `speak` |
| EMG-X6 | the outcome forks on two axes: the internal vote and audience sentiment | important | no | — | design-first (bench vs floor) | SC | — | — |
| NPC-071 | persuasion scored differently by appeal to rule or to circumstance | core | no | — | a trait row keyed on plea | SC, CHAR | SC-P7 | its test |
| NPC-001 | unmoved by rhetoric; moved by evidence or a stated consequence | core | no | — | a trait row keyed on proofs present | SC, CHAR | SC-P7 | its test |
| NPC-085 | a procedural venue where a regulatory challenge is contested | core | partly: a docket, a bench, `determine` | realm runs | closure (F-SC-01) | SC | SC-P6, B10-18c | hearing fixture |
| NPC-085 | citing applicable precedent measurably improves the odds | core | no: no Record of a prior ruling exists to cite | — | the `resolution` Record as a proof kind `record` | SC, FA | plan CR-36/37; then SC-P3's proofs | — |
| SCN-12, NPC-081 | succession resolved by a formal contested vote | core | no: no `succession` row (`disposes: hold` has no site) | H-217 | CR-35 | FA, SC | plan CR-35 | H-217's test goes red |
| SCN-04 | persuasion difficulty derived from a stored disposition toward the target | core | partly: regard enters `speak`'s obstacle only | `world_q.reception` | regard in `argue` (H-267) | SC, CHAR | plan (H-267's position) | — |
| SCN-04 | a sub-action damages a separate persistent resource of the opponent; stress with stacking penalties | core | no: no social resource exists | D_T05 row 13 | design-first; ED-SC-0035 forbids a second-person lever, so the resource must be the target's own | SC | §8 step 12 | — |

**Wrongly stated needs.**

- ARC-03 *"a GM-judged optimal timing window"*, NPC-071's and NPC-085's `UNCLEAR:` rows, ARC-55's
  `UNCLEAR:` — these state a gap in the source, not a need; adjudicate as authoring debt.
- SCN-04 *"any personal-scale roll … automatically also apply a change to a faction-scale resource"*
  — contradicts the ruled absence of stored faction aggregates (Layer 1 PART D rows 1/8/14). The
  faithful reading: the faction view (`faction_q`) changes because a member's pursuits or commits
  did. No change.
- EMG-C4 *"designated combatant"* in a formal proceeding — two readers would take it as a duel
  champion (PC) or an advocate (SC). Resolution: advocate; a trial by combat is a `challenge` under
  PC.
- ARC-R18, ARC-31 carry `[STRUCK-MECHANIC]` in their own `one_line`; their vote and tribunal needs
  stand, the Coup Counter does not.

**Arcs this lane can bring up soonest, in order.**

1. **ARC-04** (the accusation with its own timetable) — after B10-18c's CR-60/61 and SC-P6. Artifact:
   a seeded `build_hearing` run in which the accused is dismissed in one arm and bound in another by
   the patron's `speak`, from persons' acts only.
2. **ARC-10 / ARC-21** (graded categorical verdicts) — after SC-P4 and one re-authored row.
   Artifact: three seeds whose verdict bands differ open three different Tenure kinds.
3. **ARC-05** (forcing a public contest) — after SC-P6. Artifact: `petition` → `carry` → a closed
   matter within `docket_lapse`.
4. **NPC-071 / NPC-001** — after SC-P7 and CHAR's trait carrier. Artifact: `sigma.odds_of` differs by
   plea for the one and by proofs for the other.
5. **ARC-R18, SCN-12, NPC-081, NPC-085's precedent** wait on FA: CR-35, CR-36/37 (the `resolution`
   Record, the `succession` row).

Dependency edges: SC ← CHAR (attributes seated; a trait carrier); SC ← CORE (formation: present
hearers, docketed matters; the scene clock); SC ← FA (CR-35/36/37; seats and benches); SC → FA
(`detain`, `ban`, `oblige` as governance inputs); SC → WR/chronicle (the contest record).

## 14. Capability authoring surface

**(a) Where the subsystem takes a character capability, and from where.**

| point | what is read | from | site |
|---|---|---|---|
| the actor's pool | the vocation key the verb draws on; the vocation's attribute; whichever is larger; else `pool_default` | `rosters.yaml: verb_capability`, `vocation_attribute`; `Person.capability`, `Person.attributes`; `Fixtures.pool_default` | `seam/wrappers/pool.py::faculty` |
| practice dice | his own acts in that key at Success or better in a window | the log; `Fixtures.practice_window / step / cap` | `queries/world_q.py::practice`, registered in `POOL_ADDENDS` |
| the opposition | a person subject's key or opposing attribute, the larger | `rosters.yaml: vocation_opposed_by` (every row ships absent), else `vocation_attribute` | `seam/wrappers/sigma.py::_opposition_of` |
| the obstacle | opposition / 2, else `obstacle_default`; ceiling | `Fixtures`; a literal `2.0` | `modules/social_contest/roll.py::obstacle` |
| advantage | `effort` × `effort_level` | `rosters.yaml: advantage_sources`; `Fixtures.effort_level`; `sigma_leverage.LEVEL_SIGMA` | `sigma.py::advantage_sigma` |
| the room | each judge's pursuits against the speaker's deeds; proofs held | ledgers; `Fixtures.reception_gain`, `proof_step` | `world_q.reception`, `proofs` |
| what he believes of another's skill | a claim `capability:<key>` in his own ledger | nothing deposits one | `sigma.py::believed_input` |
| growth | `train` raises a key a person already holds | the `train` row | `_eff_train` (not opened `[UNVERIFIED]`) |
| the kernel (retiring) | `faculty` → `Pool.size = max(5, 2·faculty + 3)`; adjudicator → primary attribute | literals | `K/primitives.py:208-211`; `K/modes.py:426-431` |

**(b) Data-driven or not.** Data-driven: which key a verb draws on, which attribute a key starts
from and is opposed by, the advantage roster's membership, every magnitude (fixtures with register
rows). Hard-coded: the composition rules (`max(attribute, key)` for the pool and for the
opposition); the halving; the absent-versus-held asymmetry (absent → `pool_default` 2, held 0 → no
dice); "Success or better" as the practice criterion; one Python function per advantage source.
Doubled: the kernel's whole capability mapping (F-SC-02). Missing rows: `lie`, `interrogate`,
`determine`, `arrest` draw on nothing.

**(c) Target shape — what a capability definition must say for this subsystem to use it, and where.**
The owner exists: `engine/season/rosters.yaml` (`verb_capability`, `vocation_attribute`,
`vocation_opposed_by`, `advantage_sources`) over `Person.capability` and `Person.attributes`. The
social roll needs, per capability, exactly:

1. `id` — the key on `Person.capability`;
2. `verbs` — the contested or graded verbs that draw on it (today the inverse map `verb_capability`);
3. `attribute` — the attribute it starts from (`vocation_attribute`);
4. `opposed_by` — the attribute a subject resists with (`vocation_opposed_by`);
5. `practised` — whether use raises it, and by which criterion (today global fixtures);
6. for a TRAIT (a tag, not a score): `side`, `when`, `level` — SC-P7's `trait_advantages` row.

Interface the holistic stage should preserve, whatever file finally carries the definitions:
`faculty(w, person, verb) -> int` (dice), `opposition(w, subject, verb) -> Optional[float]` (a score
or none), `advantage levels(operands) -> ([aggressor], [defender])` in `LEVEL_SIGMA` names, and a
person-side reading `believed(person, subject, key) -> Optional[value]`. The module itself reads none
of them: it reads `SocialContestInput`. A capability never gates a social act (ruled: *capability
supplies dice and gates nothing*).

**(d) RPG axioms.**

Implemented, in the tradition's words: a **dice pool** counted against a fixed **target number**
(d10, successes net); **difficulty as an obstacle** the net must meet; a **passive opposed test**
(the defender does not roll; half his rating is the difficulty); **degrees of success** in four
bands read off the margin (a mixed-success middle); **advantage as a shift** rather than bonus dice
(`net_boost`, soft-capped); **effort for advantage** (spend extra scene actions); **unskilled
default** (two dice); **advancement by use** (practice dice from recent successes) and **by
training**; **situational modifiers** from the room; **hidden difficulty** (the player sees what
his character believes); **no gating by skill**.

Contradicted or lacking, that a designer would expect:

- *Trained is at least as good as untrained* — contradicted: a held key of 0 or 1 rolls fewer dice
  than no key, and a low held score is easier to oppose than none (H-127).
- *Attribute plus skill* — the pool is the larger of the two, not the sum; a deliberate choice
  (CR-20) that makes a skill below its attribute worthless. State it on the authoring surface.
- *Contested rolls are symmetric* — contradicted by the passive test at half rating (§11 item 1).
- *Advancement persists* — practice dice are a window over the log and lapse; only `train` persists.
- *Criticals and fumbles* — absent (Overwhelming is a margin band; no botch).
- *Specialisations, tags, traits that modify particular uses* — absent (SC-P7).
- *Helping / teamwork dice* — absent; an advocate replaces, he does not add.
- *A social resource (composure, resolve, stress)* — absent in the loop; present only in the kernel.
- *Knowing your opponent* — the believed-odds term has no depositor for another's capability.

**(e) Proposals, ordered.** (1) SC-P7 edits 1–2 (rows for `lie`, `interrogate`); (2) CHAR seats the
cast's attributes (not an SC file); (3) SC-P7 edits 3–4 (the generic trait source), once the
character surface names its trait carrier; (4) SC-P5 if §11 item 1 is ruled for B; (5) the
trained-below-untrained asymmetry is the pool reader's owner's to decide — SC states it and asks that
the merged surface make "absent" and "0" the same or say why not.
