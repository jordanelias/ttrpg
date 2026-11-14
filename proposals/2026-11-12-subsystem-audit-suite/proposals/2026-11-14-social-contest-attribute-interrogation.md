# SC · DICE — the social contest as it exists, read against Jordan's six attribute roles: an interrogation

Written: 2026-11-14, stage 1 of three (1: this interrogation, read-only; 2: a redesign proposal with build instructions
and a fold map into workplan v12; 3: the plan edits). Read at the working tree of branch `exec/v12-b00-b03` on
2026-11-14 (B01 landed; B01a .01 to .04 landed: drawn attributes and the `pairs` instrument). Every claim carries a
file:line read in this session; short probes ran with `PYTHONHASHSEED=0`. Nothing here was edited outside this file.

**Jordan's rulings this reads against (verbatim, relayed 2026-11-14):** *"proceedings/social contests should be calling
in: focus as staying on topic, not being pulled away from argument into something irrelevant; reason as constructing the
argument/speech, making it logical and reasonable and evidentiary with ability to account for opponent's factual
circumstances like resources office influence etc; attunement as understanding what is most likely to rattle your
opponent or reading their intent, being able to read the room, identifying what kind of argumentation/speech is most
effective for audience adjudicator opponent; charisma as the ability to be listened to and be compelling with your
delivery; grace as acting in the correct manner for the venue and occasion, as being seen as respectable, for remaining
composed in face of difficulties and challenges; will as the ability to keep arguing your case, to believe in yourself
and remain confident, to not get rattled in first place, that 'x factor' that supports you"*; *"the subsystem needs to be
using all of these attributes in the manner that I specified"*; *"argue/speech/etc verbs should all be calling the social
contest/proceedings subsystem as they all concern influencing people"*.

**Depends on:** B01 (drawn attributes), B01a .01 to .04 (`engine/season/harness/pairs.py`), the Spirit-group ruling
(`attr.spirit.will` replaces `attr.mind.will`; new `attr.spirit.threadsensitivity`; not yet in
`references/descriptor_registry.yaml`).
**Lands in batch:** none (an interrogation; stage 2 decides the fold).

## Status: PROPOSED

Design input, reference under CLAUDE.md §0.05: it describes code, it is not a mechanism. Design documents under
`.designs/` and `proposals/` are cited for INTENT only and are labelled *reference* where cited. Lanes owning the files
it reads: SC (`modules/social_contest/`, `systems/social_contest/`), IN (`engine/season/`), DICE (`engine/dice_engine/`).

Markers: `[ASSUMPTION: ... — basis]`; `[UNVERIFIED]` for a claim not opened or not run.

## A. The subsystem as it exists

### A.1 The files

**Live (the season loop reaches them):**

| file | role |
|---|---|
| `modules/social_contest/roll.py` (206 lines) | the module entry `roll` (:197-206) and the obstacle owner `obstacle` / `obstacle_terms` (:89-194); `__init__.py` is two lines of docstring |
| `engine/season/seam/wrappers/sigma.py` | the host input builder `contest_input` (:183-226), the adapter `resolve` (:495-601, `@provider("contest", "social_contest")`), the opposition read `_opposition_of` (:117-145), the advantage channel (:153-180), the believed odds (:296-482) |
| `engine/season/seam/wrappers/pool.py` | the one pool reader `faculty` (:78-94) and `score` (:97-109), the attribute reads (:54-75), the untrained score (:112-117) |
| `engine/season/seam/contest.py` | `contest()` (:182) dispatches a prize to its provider; `grade()` (:118) does the same for an inquiry with no prize |
| `engine/season/seam/ladder.py` | `degree_of` (:225) grades the returned net/ob pair through `degree_from_net` |
| `engine/season/loop/resolve.py` | `_contest` (:766-874) and `_grade` (:877-898), chosen at :1106-1107; `_fold` (:343) applies `writes_at`/`emits_at` |
| `engine/season/loop/sides.py` | `sides_of` (:55-172): for a social prize, `claimants = [actor, target]`, `subject = target`, `rung = place_of(actor)` (:171-172) |
| `engine/season/data/verbs.py` | `SOCIAL_ROLL_PROVIDER = "social_contest"` (:1925), `social_roll_verbs()` (:1928-1937), `TASK_DIFFICULTY` (:1940-1957) |
| `engine/season/rosters.yaml` | `graded_inquiries` (:1415, values :1440-1443), `verb_capability` (:1506, values :1550-1571), `task_difficulty` (:1576, values :1596-1606), `vocation_attribute` (:1608, values :1664-1667), `opposed_by: {}` (:1675), `contest_subsystems` prizes `a standing` (:1763), `a proposition` (:1779), `a matter` (:1785, `heard_by: bench` :1789), `advantage_sources` (:3581) |
| `engine/season/verb_table.yaml` | the ten rows the roll deals: `argue` (:133), `arrest` (:171), `determine` (:360), `lie` (:534), `speak` (:1475), `tell` (:1582), `examine` (:1738), `interrogate` (:1783), `research` (:1815), `surveil` (:1838) |
| `engine/season/queries/world_q.py` | the room: `judging_set` (:642-719), `declared_sitting` (:722-734), `declared_votes` (:737-762), `reception` (:792-849), `proofs` (:852-879), `docketed` (:208-226) |
| `engine/season/queries/inputs.py` | `SocialContestInput` (:45-101), `Margin` (:105) |
| `engine/season/loop/effects_information.py` | the outcome effects: `_eff_determine` (:512), `_eff_argue` (:648-675), `_eff_arrest` (:1142); `tell`/`lie` write nothing and deposit at WITNESS (`verb_table.yaml` `tell` notes) |
| `engine/season/queries/person_q.py` | `argued_pursuits` (:723-748), `regard` (:424) |
| `engine/season/decision/choose.py` | `odds_weight` (:165-191): the believed chance on a contested candidate's pursuit term |
| `engine/season/decision/options.py` | `competence` (:1690-1728, Attunement, receiver side, gain 0), `rank` (:1773-1784, always 0) |
| `engine/season/arrangements.yaml` + `data/arrangements.py` | nine arrangement rows and six `speech_kinds` (see G) |
| `engine/dice_engine/sigma_leverage.py`, `dice_engine.py` | `roll_net` (:404), `net_boost` (:196), `settle_margin` (:324), `band_odds` (:345), `settle_record` (:386); `roll_pool` (`dice_engine.py:205`), `degree_from_net` (:236) |
| `engine/season/harness/pairs.py` | the random-pairs instrument (B01a.04): `social_pairs` (:147-164) |
| `references/module_contracts.yaml` | the composition row `social_contest.roll` (:52-56, `entry: verb_call`, `verb: tell`) and the contract row (:464-480) |

**Retained, not reached by the season loop:** `systems/social_contest/sim/contest/` (16 files, 6,686 lines): the
exchange kernel (`resolver.py`, `modes.py`, `primitives.py`, `armature.py`, `appraise.py`, `rhetoric.py`,
`dictionaries.py`, `policy.py`, `faction.py`, `narrative.py`, `wrapper.py`, ...). `roll.py:16-37` records why it was not
adopted (no rng parameter, returns a winner, reads one abstract `faculty`). Its importers in code are tests, the
`arms` harness and a cycle census (`engine/tests/test_contest_kernel.py`, `engine/season/harness/arms.py`,
`tests/valoria/test_import_cycle_game_state_npe.py`); `sigma.py` and `roll.py` name it only in docstrings.

**Design documents (reference, intent only):** `.designs/systems/social_contest/reference/social_contest_v30.md`
(+ `_index`/`_infill`, `social_contest_system_v2*.md`, `social_contest_flow_skeleton_v1.md`,
`social_contest_currency_v1.md`); `proposals/2026-09-05-proceedings-subsystem/` (cited by the code as `19_PLAN.md`,
`21_RECONCILIATION.md`, `18_FINDINGS.md`, `04_VERBS.md`, `08_SEAM.md`); the `05_SC_*`, `13_SC_*`, `16_PESSIMIST_SC_*`,
`U5c_SC_*` files beside this one.

### A.2 The pipeline, from a verb being formed to its effects

1. **Formation.** `decision/options.py::opening_set` (:63) forms Candidates for a person's question; `operand_bags`
   (:1350) fans `to` over the persons he knows where the row's typed cell binds `to` (`argue`, `tell`, `lie`).
   `argue` forms only on a `Proposition`-classed referent (`verb_table.yaml:139`, `referent_class_note`, which records
   that it formed on nobody at three seeds).
2. **Choice.** `decision/choose.py::odds_weight` (:165-191) weights a contested candidate by the person's believed
   chance, `sigma.believed_chance` (:464-482) over `believed_input` (:296-344): his own pool, the opposition from a
   `capability:` claim he holds (none is ever deposited, :263-266), the room unknown unless passed. Which arm ships is
   `Fixtures.odds_weighting`, shipped `believed` (`fixtures.py:980`; `choose.py:144-150`).
3. **Admission.** `loop/resolve.py::_admits` (:187): eligibility, then the row's `requires` against the world.
4. **Dispatch.** `resolve()` (:1074-1107): a row with `contests:` goes to `_contest`; a `graded_inquiries` verb goes
   to `_grade`.
5. **Sides.** `_contest` reads the opponent as `payload[row.opponent_operand()]` (:812-815): the `counterparty`
   operand when the row names one (`to` for `argue`/`tell`/`lie`; `subject` for `arrest`/`determine`/`interrogate`),
   else `subject` (`speak`: the docketed matter). `sides_of` (`sides.py:171-172`) returns `[actor, target]`, `target`,
   and the actor's place as the rung.
6. **The act's generator.** `draw_factory(world_seed, tick)(actor, "roll:<prize>:<act id>")` (`resolve.py:833`);
   inquiries use `"roll:<verb>:<act id>"` (:893).
7. **Provider.** `seam/contest.py::contest` (:182) looks up `@provider("contest", <prize row provider>)` = `sigma.resolve`.
8. **Record.** `sigma.contest_input` (:183-226) builds `SocialContestInput`: `pool = faculty(actor, verb)` (:225);
   `opposition = _opposition_of(subject, verb)` unless the subject is the actor (:224); the room's `reception` and
   `proofs` only when the prize row says `heard_by: bench` (:213-218; only `a matter`, i.e. `speak`); an examined
   Record's `forgery_quality` only for an inquiry (:219, :570); `leverage = advantage_sigma(effort)` (:256);
   `difficulty = TASK_DIFFICULTY[verb]` on the `task` arm (:229-241).
9. **Roll.** `roll.roll` (:197-206): `Margin(net = roll_net(pool) + net_boost(leverage, pool), ob = obstacle(inp))`.
   One draw of whole dice (`sigma_leverage.py:404-414`, `_dice_dealt` = `max(1, round(pool))`, :292-296).
10. **Refusal.** S27.4 on the returned pair: `ob > obstacle_refusal_multiple x pool` -> `REFUSED` (`sigma.py:589-591`).
11. **Fraction.** `settle_record` (`sigma.py:598`; `sigma_leverage.py:386-401`): the fractional part of `boost - ob` is
    settled by one more uniform draw from the act's generator.
12. **Grade.** `ladder.degree_of` (:225) -> `degree_from_net` -> one of four bands (Failure, Partial, Success,
    Overwhelming).
13. **Fold.** `_fold` applies the row's `writes_at(band)` and `emits_at(band)` (`resolve.py:432-533`); a refusal folds
    through `_refuse_party_gap` (:735, :860).
14. **Effects.** Per row: `argue` moves the hearer's `pursuits` toward the arguer's (`_eff_argue`
    `effects_information.py:648-675`, `argued_pursuits` `person_q.py:723-748`); `determine` disposes a tenure and moves
    the party's pursuits (`_eff_determine`, :512); `arrest` opens a `detain` edge (:1142); `tell`/`lie` write nothing
    and deposit claims at WITNESS (`verb_table.yaml` `tell` writes `[]` at every band); `speak` writes nothing at any
    band and emits `matter.carried/advanced/held/turned` (`verb_table.yaml:1495-1499`), which no code reads
    (`grep` of the four kinds in `engine/`, `modules/`: the verb row and two hole-register rows only);
    `interrogate` writes nothing and emits `confession.*` (:1783-1814).

### A.3 The mechanics, and the shape of each

Every mechanic the live path has is inside ONE draw: there is no exchange, no state carried between rolls of one
proceeding, and no state machine. `hole_register.yaml` H-336 (:6228) records the measured absence (*"no conversation has
state: no dodge, no trust gate, no turn, no stall"*) and H-335 (:6216) the consequence (*"a speech or an argument
changes nothing that makes the next one harder or easier, so it can be repeated free"*).

| # | mechanic | where | shape |
|---|---|---|---|
| 1 | entry: a verb whose `contests:` prize the `social_contest` provider runs, or a `graded_inquiries` route | `verbs.py:1928-1937`; `rosters.yaml:1763-1789`, `:1440-1443` | gate, no roll |
| 2 | pool: the larger of the held capability key and the vocation's attribute, else `pool_default` (2), plus practice (cap 2) | `pool.py:78-109`, `:51`; `fixtures.py:449`, `:488` | single roll input, whole dice |
| 3 | opposition: the opponent's `score` on the OPPOSING attribute (`opposed_by` else the row's own), halved | `sigma.py:117-145`; `pool.py:68-75`; `roll.py:165-168` | single roll input |
| 4 | task difficulty: per verb, 1.0 for a contest against a person, 2.0 for an inquiry | `rosters.yaml:1596-1606`; `roll.py:162-164` | single roll input |
| 5 | stand-in obstacle (`obstacle_default` 2) on the `stand_in` control arm only | `roll.py:172-174` | control arm |
| 6 | the ceiling: fixed 2, solved per pool (`chance_floor`) on the shipped arm | `roll.py:64-86`, `:183-194`; `fixtures.py:463`, `:469` | single roll bound |
| 7 | the room: `reception_gain x reception + proof_step x proofs`, subtracted, floored at `OB_MIN` | `roll.py:175-179`; `world_q.py:792-879` | single roll input, `speak` only |
| 8 | forgery: an examined Record's `forgery_quality`, added | `roll.py:180-182`; `sigma.py:219` | single roll input, inquiries only |
| 9 | leverage: `advantage_sources` (only `effort`) -> named sigma levels -> `net_boost` (a mu-shift) | `sigma.py:153-180`; `sigma_leverage.py:196-210` | single roll; the shipped chooser forms no effort (`H-244`) |
| 10 | S27.4 refusal: `ob > 2 x pool` | `sigma.py:589-591` | gate on the pair |
| 11 | the margin and its fraction (settle draw) | `sigma.py:598`; `sigma_leverage.py:324-342` | one extra uniform in the same roll |
| 12 | bands: `degree_from_net`, four bands | `ladder.py:225`; `dice_engine.py:236` | single roll output |
| 13 | outcome classes: per-row `writes`/`emits` by band | `verb_table.yaml` rows above | fold of one band |
| 14 | effects: pursuits moved (`argue`, `determine`), a tenure disposed (`determine`), custody (`arrest`), claims deposited (`tell`, `lie`), nothing (`speak`, `interrogate`) | A.2 step 14 | one write per act |
| 15 | the bench (who sits over the act's rung) | `world_q.py:642-719` | a read; it feeds `reception`/`proofs` and `determine`'s `bench.size` quorum |
| 16 | a declared vote (`excommunication_deliberation`): bench members holding a live `commit` to an OUGHT against the party | `world_q.py:722-762`, `:4745` | a `requires` conjunct, not a roll input |
| 17 | believed odds (what the person thinks his chance is) | `sigma.py:296-482` | read-only, chooser side |
| 18 | repeated exchange | none in the live path (H-336) | ABSENT |
| 19 | proceedings / hearing structure: a calendar slot, a docket item naming a matter and an arrangement row, a bench, `determine` | `world_q.py:208-226`, `:642-762`; `arrangements.yaml` | a gate and a lookup; the order, proofs and speech kinds of a row are not read (G) |
| 20 | audience / adjudicator: the bench at the speaker's place (`speak`), the party's place (`determine`'s quorum); otherwise the opponent alone | `sides.py:162-172`; H-215 (`hole_register.yaml:4668`) | a read |
| 21 | topic, composure, rattle, venue fit, respectability, delivery | none in the live path | ABSENT (C) |
| 22 | evidence: `proofs` (deed claims about the opponent the speaker holds and the opponent cannot mirror) | `world_q.py:852-879` | a single roll input, `speak` only; the arrangement's `proofs:` column is not read (H-216, `hole_register.yaml:4681`) |

**The retained kernel, for contrast (reference, not live):** a multi-exchange state machine. A `Bout` runs up to a
proceeding's exchange budget (`modes.py:485-515`: Formal Contest 3, Grand Contest 5, Royal Audience 3, Church Tribunal
1-5, Guild Arbitration 3, Casual Dispute 1, Private Negotiation 1-3); per side it carries `Standing`/Face
(`primitives.py:31-47`), `Reserve`/Concentration with per-move costs and `regroup` (:49-56), `Room` (:232-236), a live
`Stasis` ground with a relevance test (:11-25) and an evasion fault for arguing off it (`resolver.py:380-381`), a
venue-configured `DefeatCatalogue` (`primitives.py:262-280`: barred device, self-contradiction, evasion strikes,
silence), evidence with hidden value (`Dossier`, :283-310), an adjudicator armature of what moves this judge
(`armature.py`), a partial-reveal `Appraise` (`appraise.py`), and four win conditions (`modes.py:1-12`).

## B. Attribute use today

### B.1 Every read of an attribute on this chain

The registry has ten attribute keys (`references/descriptor_registry.yaml:41-53`). Jordan's Spirit-group change is not in
it: `attr.mind.will` still stands at :47 (name Spirit, aliases Will, Willpower) and no `attr.spirit.*` key exists
anywhere outside `.designs/`/`.audit/` (grep of `attr.spirit` and `threadsensitivity` over `*.py`/`*.yaml`: no hit).

| attribute (key) | read on the social chain | file:line | what it does |
|---|---|---|---|
| Focus (`attr.mind.focus`) | the pool AND the opposition for `tell` and `speak` (vocation `copying`) | `rosters.yaml:1550-1551`, `:1664`; `pool.py:60-75`, `:97-109` | pool base; opponent's score halved into Ob |
| Reason (`attr.mind.acuity`) | the pool AND opposition for `interrogate`, `examine`, `research`, `surveil` (vocation `inquiry`) | `rosters.yaml:1553-1555`, `:1569`, `:1666` | as above (an inquiry's subject is rarely a person: A.2 step 8) |
| Attunement (`attr.social.attunement`) | NOT read by the roll. One reader on the receiving side of a telling: `competence` scales a deposited claim's confidence by the receiver's Attunement, at `competence_gain` 0 (shipped), so it is 1 for everyone | `options.py:1683`, `:1690-1728`; `fixtures.py:1069` | inert at the shipped gain; `rosters.yaml:1608-1667`'s note records Jordan's 2026-11-05 ruling (ED-IN-0350) that Attunement *"informs how character thinks the other character is receiving it"*, a choice-side input *"that no code reads yet"* |
| Presence/Charisma (`attr.social.charisma`) | the pool AND opposition for `argue` and `determine` (vocation `argue`) | `rosters.yaml:1552`, `:1571`, `:1665` | as above |
| Grace (`attr.social.grace`) | none | — | — |
| Spirit/Will (`attr.mind.will`) | none on the social chain. `rosters.yaml:1668-1675` names Spirit as *"the attribute that resists influence"* for `opposed_by`, which ships empty (`{}`), so nothing reads it. Read by the combat module only (`modules/combat/attributes.py:49`) | — | — |
| Perception (`attr.mind.perception`) | none on the social chain (combat only, `modules/combat/attributes.py:48`) | — | — |
| Coordination (`attr.body.agility`) | the pool AND opposition for `arrest` (vocation `arms`, a social-roll verb contesting `a standing`) | `rosters.yaml:1570`, `:1667` | as above |
| Strength, Endurance | none on the social chain | — | — |
| Thread Sensitivity (`Person.thread_sensitivity`, not an attribute today) | none on the social chain | `state/carriers.py:843` | see F, J-12 |

`lie` names no vocation (`rosters.yaml:1557-1568`, the comment above the three B11 rows): its pool and its opposition are both `pool_default` (2) for
every person (`pool.py:112-117`; `sigma.py:330-335`), so `lie` reads no attribute at all.

Other readers checked and found not to touch the social chain: `seam/wrappers/combat.py:144-235` (combat's input),
`decision/sheet.py:93` (the creation sheet, read only), `harness/populated.py:1360`, `:2005` and
`state/carriers.py:737-772` (the writers: drawn whole numbers on `(1, 6)`, `fixtures.py:452`).
`governing_attribute` (named in B05.09) does not exist on this tree (grep: no hit in `engine/`, `modules/`).

### B.2 The pairs instrument, per verb

Run: `PYTHONHASHSEED=0 python -m engine.season.harness.pairs social --verb <v> --diff all --n 40000 --seed 0`, for every
verb `social_roll_verbs()` returns (`argue, arrest, determine, examine, interrogate, lie, research, speak, surveil,
tell`); about 11 s each. `y` is the share of Success-or-better (`pairs.py:18-22`); SLOPE is per point of `a[k] - b[k]`,
11 bins read in every cell. Values rounded to three places; every cell not shown in bold lies in `[-0.002, +0.002]`.

| verb | Str | End | Coord | Focus | Reason | Spirit | Perc | Attun | Presence | Grace |
|---|---|---|---|---|---|---|---|---|---|---|
| argue | 0 | 0 | -0.001 | 0 | 0 | 0 | -0.001 | 0 | **0.061** | -0.001 |
| determine | -0.001 | 0 | 0 | 0 | -0.001 | 0 | 0.001 | 0 | **0.061** | -0.002 |
| tell | -0.001 | 0.001 | 0 | **0.062** | 0.001 | -0.001 | 0.001 | 0 | 0 | 0 |
| speak | -0.001 | -0.001 | -0.001 | **0.060** | 0 | -0.001 | 0 | -0.001 | -0.001 | 0.002 |
| lie | -0.001 | 0 | 0 | -0.001 | 0 | 0.001 | 0 | 0.001 | 0.001 | 0 |
| interrogate | 0 | 0 | 0 | 0.001 | **0.060** | 0.001 | 0 | 0.001 | 0 | 0.001 |
| arrest | 0.001 | 0 | **0.061** | 0 | -0.001 | 0 | 0 | 0.001 | 0.003 | -0.001 |
| examine | 0 | 0.001 | 0 | 0.001 | **0.034** | 0 | 0.001 | 0 | -0.001 | 0 |
| research | -0.001 | 0 | -0.001 | 0.001 | **0.032** | 0.001 | 0 | 0 | 0 | 0 |
| surveil | 0 | 0 | 0 | 0.001 | **0.033** | 0.001 | 0 | 0 | 0 | 0 |

**Reading.** Each verb reads exactly one key, its vocation's, on both sides (the actor's pool and the opponent's
halved opposition, since `opposed_by` is empty); `lie` reads none. Grace, Spirit, Attunement and Perception have no
slope on any social verb. The three inquiries' slope is about half the contests' because their obstacle (difficulty
2.0 + the opponent's half-score) sits above the per-pool ceiling for most pairs, so the opponent's score is cut away
(`roll.py:190-194`) and only the actor's side moves the curve [ASSUMPTION: the halving is the ceiling's cut — basis:
difficulty 2.0 vs 1.0 is the only difference between `examine` and `interrogate` in the record, both read Reason].

**What the instrument does not model (so these slopes are of the record, not of the shipped act):**
`social_pairs` calls `contest_input(w, [a, b], verb, subject=b)` with no `room` (`pairs.py:155`), so `speak`'s
`reception`/`proofs` never enter; it always opposes a person, where `speak`'s opponent is the docketed matter (a person
only when the matter is one), `argue`'s is the hearer `to`, and the inquiries' subjects are a Site, a Record or a Rung
(`verb_table.yaml:1738`, `:1815`, `:1838`), which have no score; and it reads no capability key and no practice.

