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
(`attr.spirit.will` replaces `attr.mind.will`, Spirit's one attribute; ten attributes in all; not yet in
`references/descriptor_registry.yaml`). Jordan 2026-11-14 dropped the proposed `attr.spirit.threadsensitivity`:
*"drop threadsensitivity, keep existing prac.thread_sensitivity"* (F, J-12).
**Lands in batch:** none (an interrogation; stage 2 decides the fold).

## Status: PROPOSED

Design input, reference under CLAUDE.md §0.05: it describes code, it is not a mechanism. Design documents under
`.designs/` and `proposals/` are cited for INTENT only and are labelled *reference* where cited. Lanes owning the files
it reads: SC (`modules/social_contest/`, `systems/social_contest/`), IN (`engine/season/`), DICE (`engine/dice_engine/`).

Markers: `[ASSUMPTION: ... — basis]`; `[UNVERIFIED]` for a claim not opened or not run.

**Findings in brief.** (1) The live subsystem is one draw per act: no exchange, no state between draws, no topic, no
composure (A.3). (2) Each social verb reads exactly one attribute, the same on both sides; Grace, Spirit and Attunement
are read by no social roll, and `lie` reads none (B.2). (3) Of the six roles: PRESENT 0, PARTIAL 3 (Reason, Attunement,
Presence), ABSENT 3 (Focus, Grace, Will) (C). Four of the six need exchanges to act as stated (F, J-11). (4) Proceeding
types exist as nine data rows (`arrangements.yaml`), but no computed case names one and most of their fields are read by
nothing (G). (5) The roll is discrete with whole-number pools, the opposition is halved rather than A-71/A-79's rule, and
the per-pool ceiling cuts the obstacle on about a fifth of contest pairs (E-1, E-4, E-5).

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
| `engine/season/rosters.yaml` | `graded_inquiries` (:1415, values :1440-1443), `verb_capability` (:1506, values :1550-1571), `task_difficulty` (:1576, values :1597-1606), `vocation_attribute` (:1608, values :1664-1667), `opposed_by: {}` (:1675), `contest_subsystems` prizes `a standing` (:1763), `a proposition` (:1779), `a matter` (:1785, `heard_by: bench` :1789), `advantage_sources` (:3581) |
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
| 4 | task difficulty: per verb, 1.0 for a contest against a person, 2.0 for an inquiry | `rosters.yaml:1597-1606`; `roll.py:162-164` | single roll input |
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
| Thread Sensitivity (`prac.thread_sensitivity`, `Person.thread_sensitivity`; not an attribute, and stays so: F, J-12) | none on the social chain | `state/carriers.py:843` | — |

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

**The ceiling's share, measured** (`social_pairs`, seed 0, n 20,000, `obstacle_terms` read per record): the per-pool
ceiling cuts the obstacle on **22.6 %** of `argue` pairs, 22.5 % of `tell` pairs and **47.6 %** of `examine` pairs;
S27.4 refuses none; pools are spread evenly over 1 to 6 (the drawn attribute, as `faculty` reads it).

## C. The six roles against the subsystem

Read against the live path (A.2). For each role: Jordan's words, the verdict, what exists, what the role needs, the
nearest mechanic, and the smallest addition that would make the role act as stated. Counts: PRESENT 0, PARTIAL 3
(Reason, Attunement, Presence), ABSENT 3 (Focus, Grace, Will).

A precondition that cuts across four of the six: Focus (*not being pulled away*), Attunement (*what is most likely to
rattle your opponent*), Grace (*remaining composed in face of difficulties*) and Will (*keep arguing*, *not get rattled
in first place*) each describe something that happens BETWEEN one move and the next. The live path is one draw per act
with no state carried between draws (A.3; H-336, `hole_register.yaml:6228`). In a single draw each of these can only be
approximated as a fixed term on the record; acting *in the manner stated* needs at least two exchanges and a carried
per-side state (F, J-11).

### C.1 Focus — *"staying on topic, not being pulled away from argument into something irrelevant"*

**ABSENT.**
- What exists: Focus is today the pool and the opposition of `tell` and `speak` (vocation `copying`,
  `rosters.yaml:1550-1551`, `:1664`), on the ground *"a claim relayed as it was held"* (the `vocation_attribute` note,
  `rosters.yaml:1608-1667`): exactness of reproduction, not staying on a topic. The act's topic EXISTS as an operand
  and is read by NOTHING on the roll: `argue`'s `subject` is an uttered Proposition (`verb_table.yaml:141-147`),
  `speak`'s `subject` is the docketed matter (:1480-1483), `tell`'s is the topic claim; `contest_input` receives the
  OPPONENT as `subject` (`resolve.py:812-815`, `sigma.py:183-226`), and `_eff_argue` reads `to` and the actor, never
  `subject` (`effects_information.py:665-668`): what is argued does not change what moves (`argued_pursuits` moves
  every held pursuit toward the arguer's, `person_q.py:723-748`). A scene carries `occasion: Question`
  (`state/carriers.py:622-631`). No derailment, no relevance test, no irrelevant move exists.
- Retained kernel (reference): a live `Stasis` ground, `Stasis.relevant(move_ground, live_ground)`
  (`systems/social_contest/sim/contest/primitives.py:11-25`), and an evasion fault *"argued off the live issue"*
  (`resolver.py:380-381`) that a venue's `DefeatCatalogue` makes fatal at two strikes (`primitives.py:262-280`).
- What the role needs: (i) the topic on the record the module reads; (ii) a pull away from it (an opponent's move or
  the room's) and a resistance to that pull. (i) has a carrier (the Proposition id or the docket matter in the act's
  payload; `Proposition` at `state/carriers.py:1006-1015` has `subject`/`predicate`); (ii) has none.
- Nearest mechanic: the obstacle composition (`roll.py::obstacle_terms`, :147-194), which already names each term.
- Smallest addition: a `topic` field on `SocialContestInput` (`queries/inputs.py:45-101`), filled by `contest_input`
  from the act's `subject` operand where the opponent operand is not `subject` (`argue`, `tell`, `lie`) and from the
  docket matter for `speak`; then ONE named term in `obstacle_terms` (or one `advantage_sources` member) for the pull
  off-topic, set by the opponent's score against the speaker's Focus. A pull that can actually derail (the speaker
  ending on a different ground) needs J-11's exchange.

### C.2 Reason — *"constructing the argument/speech, making it logical and reasonable and evidentiary with ability to account for opponent's factual circumstances like resources office influence etc"*

**PARTIAL.**
- What exists: an evidence term, `proofs` (`world_q.py:852-879`): deed claims about the opponent the speaker holds and
  the opponent cannot mirror, weighed by remove (`remove_weight`, :776-786), subtracted from the obstacle as
  `proof_step x proofs` (`roll.py:175-179`; `proof_step` 0.25, `fixtures.py:496`). It is read ONLY for a prize with
  `heard_by: bench` (`a matter`, i.e. `speak`; `sigma.py:213-218`, `:565-566`) and is 0 without a bench
  (`world_q.py:875`). No attribute scales it: Reason does not touch it. Reason is the pool of `interrogate` and the
  three inquiries only (`rosters.yaml:1666`). The opponent's circumstances exist as carriers and none reaches the roll:
  his seats (`Person.tenures` `hold` edges, `state/carriers.py:875`; `Office`, :1056), his faction's holdings
  (`faction_q.holdings`, :159), a rung's rank (`world_q.py:4694-4703`, rung kind's ordinal), his opinion of a faction
  (`world_q.py:3029`); person-side, `rank` is always 0 because no `office` claim is ever deposited (`options.py:1773-1784`,
  H-181). The arrangement row's `proofs:` column (what kinds of proof a proceeding admits, `arrangements.yaml`) is not
  read (H-216, `hole_register.yaml:4681`).
- Retained kernel (reference): `Dossier`/`EvidenceItem` with a hidden value and a ground, relevant only on the live
  ground (`primitives.py:283-310`); `logos` appeal weighted by venue (`modes.py:1-12`).
- What the role needs: the speaker's case quality (Reason) as a term, and the opponent's circumstances as facts the
  case can cite. Carriers exist for the facts (above); the speaker's knowledge of them is his ledger (`Claim`,
  `state/carriers.py:325`).
- Nearest mechanic: `proofs` and its `proof_step` weight.
- Smallest addition: (a) scale the evidence term by the speaker's Reason (one factor in the `proof_step x proofs`
  product, read on the record as a new raw operand); (b) read `proofs` for every social prize with a person opponent,
  not only `heard_by: bench` (the `venue is None` and empty-bench zero at `world_q.py:872-876` is what confines it); (c)
  one more read in `contest_input` for the opponent's circumstances, as claims the speaker holds about the opponent's
  seats and holdings (the `attributed_deeds` pattern over different predicates), counted into the same term.

### C.3 Attunement — *"understanding what is most likely to rattle your opponent or reading their intent, being able to read the room, identifying what kind of argumentation/speech is most effective for audience adjudicator opponent"*

**PARTIAL** (the carriers for a reading exist; nothing chooses on it, and nothing for "rattle" exists).
- What exists: (1) the person's believed odds (`sigma.py::believed_input` :296-344, `odds_of` :394-457,
  `believed_chance` :464-482), handed to the chooser as `View.odds` and weighted in (`choose.py:165-191`, arm `believed`,
  `fixtures.py:980`): a read of his own chance, from his own ledger; but the believed opposition needs a
  `capability:` claim nobody deposits (`sigma.py:263-266`), so for a person opponent on a keyed verb the chance is
  `None` and the chooser's weight is unchanged; the room's terms are unknown unless passed (:338-343). No Attunement
  in any of it. (2) `competence` (`options.py:1690-1728`): the RECEIVER's Attunement scales a told claim's credit, at
  `competence_gain` 0 shipped (`fixtures.py:1069`), so inert; its docstring records why a live gain would invert
  Jordan's ruling (ED-IN-0327). (3) The `vocation_attribute` note records ED-IN-0350 (Jordan, 2026-11-05): *"attunement
  informs how character thinks the other character is receiving it and the best style of argument to deliver"*, *"a
  choice-side input that no code reads yet"* (`rosters.yaml:1608-1667`). (4) Reading the room resolver-side exists
  (`reception`, `world_q.py:792-849`) and is forbidden to decision code by design (`world_q.py:766-774`: *"he GUESSES
  them, and that guess is the game"*). (5) No kind of argument exists on the live path: `arrangements.yaml`'s six
  `speech_kinds` (forensic issue-ladder rungs) and `rosters.yaml: genres` (:3265) have no runtime reader (G).
- Retained kernel (reference): `appraise.py` (a partial reveal of the judge's disposition by roll band), the
  adjudicator armature (what moves THIS judge, `armature.py`), appeals ethos/pathos/logos (`primitives.py:27-29`),
  four styles (`dictionaries.py:76-136`). v30 intent: Appraise = Attunement + Recall against the opponent's Charisma/2
  (`.designs/.../social_contest_v30.md:155`).
- What the role needs: (i) a choice of approach on the act; (ii) the target's disposition the approach is matched
  against (the bench's pursuits, as `reception` reads them; the opponent's pursuits and convictions, `Person.pursuits`,
  `Person.conviction`); (iii) Attunement as how well the speaker reads (ii) before he chooses (i).
- Nearest mechanic: the advantage channel (`rosters.yaml: advantage_sources` :3581; `sigma.py:160-180`), the closed
  door for a mu-shift; and `believed_input`'s `room` parameter.
- Smallest addition: one closed roster of approaches and an `approach` operand on the act (as `effort` is carried,
  `state/carriers.py::effort_of`); one `advantage_sources` member whose level is the match between the approach and
  the target's disposition; the chooser picks the approach from a believed disposition whose error falls with his
  Attunement (the believed-room read person-side, filled with noise by Attunement). "Rattle" needs a rattle state
  (C.5, C.6, J-11).

### C.4 Presence/Charisma — *"the ability to be listened to and be compelling with your delivery"*

**PARTIAL.**
- What exists: Presence is the pool of `argue` and `determine` (`rosters.yaml:1552`, `:1571`, `:1665`; the 2026-11-05
  ruling, ED-IN-0350) and the opposition the hearer brings to an argument (same key, `opposed_by` empty). It is not read
  by `tell`, `speak` (Focus) or `lie` (none). "Being listened to" has two carriers, neither reading Presence: the bench's
  `reception` of the speaker (`world_q.py:792-849`, regard built from his deeds, not his delivery) and a hearer's
  `teller_weight` (`options.py:1830`, the credit a hearer gives a teller from the relation, the record and the hops).
- Retained kernel (reference): the Crowd adjudicator is Charisma-primary (`dictionaries.py:351-386`); v30 has Charisma
  as the strain modifier and Face's ceiling (`social_contest_v30.md:197-198`, `:247`).
- What the role needs: Presence on every act that delivers words to someone (`tell`, `speak`, `lie`, `argue`), and a
  term for being heard at all.
- Nearest mechanic: the governing score (`pool.py::score`, :97-109) and the verb's attribute list (the 2026-11-13
  proposal, `2026-11-13-verb-governing-attributes.md`, B05.24/B05.25).
- Smallest addition: name Presence among the attributes of `tell`, `speak` and `lie` (the row-level attribute list that
  proposal adds; today one attribute per vocation, `rosters.yaml:1664-1667`), and one factor of the speaker's Presence
  in what a hearer credits (`teller_weight`) or in `reception`.

### C.5 Grace — *"acting in the correct manner for the venue and occasion, as being seen as respectable, for remaining composed in face of difficulties and challenges"*

**ABSENT.**
- What exists: the venue is the actor's place (`sides.py:171-172`); building kinds and their `serves:` institutions
  (`venues.yaml:59-109`) are read at build only (`harness/populated.py:1291`, `:1305`); the arrangement's
  `venue_min_rank`, `floor`, `interposed` (incl. `ceremony`) are loaded and not read at runtime (G). Respectability:
  `reception` (regard from deeds) and `regard` (`person_q.py:424`); nothing from manner. Composure: no `Person` field
  (`state/carriers.py:774-875`); "Composure", "Concentration", "Face" and "Resolve" are names in the registry's
  `not_descriptors.derived_values` list (`descriptor_registry.yaml:274`) and nothing in `engine/season` or `modules`
  computes them (grep: no hit); `write()` guards a `(Person, coherence)` write (`state/world.py:1301-1311`;
  `write_matrix.yaml:200`) for a field `Person` does not have. The registry describes Grace as *"composure, calm,
  etiquette, manners"* (`descriptor_registry.yaml:53`).
- Retained kernel (reference): `Standing`/Face per side, built by ethos moves and never stripped
  (`primitives.py:31-47`, :64-131 *"Face has NO strip/strain channel wired"*); a venue-configured `DefeatCatalogue`;
  `GraceThreshold` win for an appeal (`modes.py:9-10`). v30's Face ceiling is Charisma x 3 (`social_contest_v30.md:247`),
  not Grace.
- What the role needs: (i) the venue's and occasion's expected manner (a fact of the proceeding: G); (ii) a composure
  state that difficulty strains and Grace holds.
- Nearest mechanic: the room term (`roll.py:175-179`), the one place the venue already enters the obstacle.
- Smallest addition: (a) carry the proceeding's kind (the docket item's arrangement row, `docketed_under`,
  `world_q.py:487`; or the venue building's `serves:`) onto the record, and one named term for Grace against the
  occasion's formality; (b) for composure in a single draw, Grace scaling the hostile half of the room term (today a
  bench against the speaker raises the obstacle unscaled, `roll.py:178`). Composure that holds or breaks across a
  proceeding needs a carried per-side mark (J-11).

### C.6 Will (Spirit) — *"the ability to keep arguing your case, to believe in yourself and remain confident, to not get rattled in first place, that 'x factor' that supports you"*

**ABSENT.**
- What exists: Spirit is named in a comment as *"the attribute that resists influence"* for `opposed_by`
  (`rosters.yaml:1668-1675`), whose rows ship EMPTY, so nothing reads it; the carrier and its reader exist
  (`data/rosters.py:670`, `pool.py:68-75`). `effort` (`sigma.py:153-157`; H-244) is the closest thing to "keep
  arguing" (more of the scene behind one roll), and the shipped chooser forms none. Repeated `argue` acts cost nothing
  and change nothing that makes the next harder (H-335). `confidence.broken` (`resolve.py:581-600`) is about a confided
  claim, not a person's self-confidence; the conviction crisis (`resolve.py:694-705`) changes faith, not resolve.
- Retained kernel (reference): `Reserve`/Concentration, spent per move and refilled by `regroup`
  (`primitives.py:49-56`), and a `silence` (yield) fault (:262-280); v30 sets Concentration = 3 x Focus + 2 x Spirit
  (`social_contest_v30.md:246`, `:267`).
- What the role needs: (i) resistance to being moved (the opposition side); (ii) persistence across exchanges;
  (iii) resistance to a rattle.
- Nearest mechanic: `opposed_by` (a data row per vocation, read by `_opposing_attribute`).
- Smallest addition: (a) `opposed_by` rows naming Spirit for the vocations Jordan's words cover (data only,
  `rosters.yaml:1675`; with the Spirit key renamed first, E-7); (b) Spirit as the cost or the cap of keeping on (the
  number of exchanges or the effort a side may spend), which needs J-11; (c) Spirit as the resistance to a rattle term
  (C.3, C.5), once one exists. Where Will's *"not get rattled in first place"* and Grace's *"remaining composed"* divide
  is open (F, item 4).

## D. The influence verbs

**How I decided.** I read each of the 67 rows (`verb_table.yaml`, `VERB_TABLE`) for its everyday meaning and kept a verb
when its success depends on changing another person's belief, choice or conduct by what is said, or by standing pressed
in words. I excluded acts on things (records, stores, works, armies as records), movement, violence, and acts that need
no one's assent. Three groups result. Routing read from `social_roll_verbs()` (`verbs.py:1928-1937`), `contests:`, and
`stratum`/`eligibility`.

**D.1 Influence verbs the social roll deals today (5):**

| verb | everyday act | route today | pool / obstacle | calls the subsystem without change? |
|---|---|---|---|---|
| `argue` | persuade a hearer of a proposition | `a proposition`, roll | Presence vs hearer's Presence/2 + 1.0 | yes (it is the subsystem); topic unread (C.1) |
| `tell` | inform a hearer to sway him | `a standing`, roll | Focus vs hearer's Focus/2 + 1.0 | yes |
| `lie` | deceive a hearer | `a standing`, roll | `pool_default` 2 vs 2/2 + 1.0, no attribute | yes; reads no attribute (B.1) |
| `speak` | address a sitting on a docketed matter | `a matter`, roll, bench room | Focus vs the matter-person's Focus/2 + 1.0 - room | yes |
| `interrogate` | compel a detainee to confess | `a proposition`, roll | Reason vs detainee's Reason/2 + 1.0 | yes; writes nothing (`verb_table.yaml:1783-1814`) |

**D.2 Verbs the social roll deals that are NOT influence by words (5):** `determine` (a bench rules a matter;
`binding_decision`, `remit:determine`; rolls the judge's Presence against the party's: E-9), `arrest` (laying hands;
`contested_physical`, `a standing`, Coordination; the row itself marks the prize an [ASSUMPTION],
`verb_table.yaml:187`), and the inquiries `examine`, `research`, `surveil` (Reason; a Site, a Record, a Rung).

**D.3 Influence verbs NOT routed to the subsystem (11):**

| verb | everyday act | route today |
|---|---|---|
| `petition` | ask a superior for something | `social`, no roll: writes `Record.exists`, emits `petition.filed` |
| `covenant` | offer terms to a counterparty | `social`, `remit:issue`, no roll: writes a Record, `covenant.offered` (consent is the other's later act) |
| `interview` | question a person | `social`, no roll: emits `finding.made`; a prompt with no reply (K-36, `rosters.yaml:1433`) |
| `challenge` | call a man out | `social`, no roll: writes a challenge Record; `accept` then routes to combat |
| `open_case` | bring an accusation before a bench | `social`, `remit:determine`, no roll: dockets a matter |
| `construe` | read an order's terms to one's own ends | `social`, no roll: emits `terms.distorted` |
| `issue` | order / decree | `binding_decision`, brute office function, no roll |
| `dispatch` | send a man on an errand | `binding_decision`, brute, no roll |
| `order_unit` | command a unit | `uncontested_material`, no roll |
| `give` | give (a gift that buys favour, in one reading) | `social`, no roll; influence only by reading |
| `forge` | deceive by a false document | `uncontested_material`, no roll; the forgery's quality later opposes an inquiry (`roll.py:180-182`) |

Borderline and excluded with reason: `comply` / `evade / defy` (a receiver's answer to an order, not an attempt to move
anyone), `conceal` (hides, addresses no one), `utter` (makes a Proposition exist, addresses no one), `commit`,
`forgive`, `tie / knot`, `oblige` (binds oneself), `train` (moves a capability, not a mind), `recruit` (an army-record
act here, `verb_table.yaml:1932`), `exchange` (trade; no bargaining exists), `confer`, `convene`, `pardon`, `revoke`,
`release`, `succeed`, `establish`, `surrender`, `seize` (office or tenure acts whose efficacy is not in question).
The brute-function verbs that compel by standing (`issue`, `dispatch`, `order_unit`, `confer`, `convene`) fall under
the ruling that a brute office function rolls nothing; whether `issue` and `order_unit` are influence (the order's
obedience is in question) is stage 2's (F, item 6).

**Counts:** 16 influence verbs (5 routed to the subsystem, 11 not); 5 more verbs routed to the subsystem that are not
influence by words.

## E. Discrepancies and defects that bear on the redesign

| # | what | where | what it changes |
|---|---|---|---|
| E-1 | **The roll is discrete.** `roll_net` deals `max(1, round(pool))` whole d10s (`sigma_leverage.py:292-296`, :404-414); `band_odds` enumerates the same whole dice (:345-375). A fractional pool exists only as `roll_net_continuous` (:417), unused here. | `roll.py:205` | A-5 (bell curve, fractional dice and obstacles) is not met by the roll; only the margin's fraction is honoured (`settle_margin`, :324-342). |
| E-2 | **The pool is a whole number.** `faculty -> int` (`pool.py:78-94`); `score` takes `int(attr)` and `int(have)` (:108-109); `SocialContestInput.pool: int` (`inputs.py:85`). Attributes are drawn as whole numbers 1-6 today (`state/carriers.py:743-749`), so nothing is cut yet; an averaged governing score (2026-11-13 proposal) or a fractional base would be. | `pool.py:108-109` | Any fractional governing score is truncated, not carried. |
| E-3 | **The pool is the larger of key and attribute, not a sum; no base, no floor 5.** | `pool.py:105-109` | A-6 (skill score plus a base, floor five) is not met; A-7 (two inputs) is not met (one attribute per vocation, `rosters.yaml:1664-1667`). |
| E-4 | **The opposition is halved** (`score / 2`, the 2026-08-14 ruling quoted at `roll.py:95-100`). No code carries the A-71/A-79 single opposed-contest rule at 0.4 per point of the defender's trained score (grep of `engine/`, `modules/` for an opposed-rule owner or the 0.4 weight: no hit; the rule lives in `29_DICE_one_opposed_rule_form_and_tuning.md`, PROPOSED). | `roll.py:165-171` | The social roll and A-71/A-79 disagree on the opposition's weight. |
| E-5 | **The per-pool ceiling cuts the obstacle on 22.6 % of `argue` pairs and 47.6 % of `examine` pairs** (B.2 probe), where the opponent's score then stops mattering. | `roll.py:183-194`; `fixtures.py:463`, `:469` | Flattens the opposition's slope (half for the inquiries, B.2); any new obstacle term (C) is cut the same way above the cap. |
| E-6 | **Fallbacks.** `pool_default` (2) is the score of anyone holding neither key nor attribute (`pool.py:109`, :112-117); since B01a every built person holds all ten, so on the live path it is reached by `lie` alone (no vocation) and by a world built with `generated_attribute_range` None. `obstacle_default` (2) stands in only on the `stand_in` control arm (`roll.py:172-174`). | as cited | `lie` reads no attribute (B.2: every slope 0). |
| E-7 | **The Spirit key.** The registry carries `attr.mind.will` (`descriptor_registry.yaml:47`, `:64` in `agg.mind`); so do `references/names_index.yaml:84`, `references/definitions/definitions.yaml:103`, `modules/combat/attributes.py:49` and the `opposed_by` comment `rosters.yaml:1669`. Jordan's `attr.spirit.will` is in none of them. | as cited | A rename touches these before any `opposed_by` row (C.6) can name it. |
| E-8 | **`opposed_by` ships empty**, so every opposition is read on the verb's own attribute: the hearer of an argument resists with his Presence, a told man with his Focus. | `rosters.yaml:1675` | Will has no reader (C.6). |
| E-9 | **`determine` is a seat's binding decision and rolls**: the judge's Presence against the party's Presence/2 + 1.0. The party's case and the speeches made at the sitting do not enter (only `speak`'s own roll reads the room). | `verb_table.yaml:360-423`; `rosters.yaml:1571`, `:1602` | Bears on *"a brute office function rolls nothing"* and on who the adjudicator is (G). |
| E-10 | **What is argued is read by nothing**: the roll gets the opponent as `subject`; `_eff_argue` moves every held pursuit of the hearer toward the arguer's, whatever the Proposition. | `resolve.py:812-815`; `effects_information.py:665-668`; `person_q.py:723-748` | No topic (C.1); an argument about anything moves the same pursuits. |
| E-11 | **`speak` writes nothing at any band**; its four emitted kinds have no reader. | `verb_table.yaml:1489-1499`; H-63 (`hole_register.yaml:728`) | A speech changes nothing in the world; the proceeding's outcome is `determine`'s alone (E-9). |
| E-12 | **`interrogate` writes nothing**; a confession is graded by the dice, never by whether there is anything to confess (H-310, `hole_register.yaml:5916`). | `verb_table.yaml:1783-1814` | — |
| E-13 | **The believed odds are `None` for every person-opposed keyed verb**: `believed_input` needs a `capability:` claim and nothing deposits one, so the chooser cannot price `argue`, `tell`, `interrogate`, `determine` or a person-matter `speak`; it can price `lie` (opposition known at `untrained`). | `sigma.py:263-266`, :321-329 | Attunement's natural home (the read of one's chances) returns nothing today. |
| E-14 | **The room is `speak`'s only.** `reception`/`proofs` are read only for `heard_by: bench` (`a matter`); `proofs` is 0 without a bench. | `sigma.py:213-218`, :565-566; `world_q.py:872-876` | No other influence verb has an audience or evidence term (C.2, C.4). |
| E-15 | **The advantage channel carries only `effort`, and the shipped chooser forms no effort.** | `sigma.py:164`; H-244 | The one sigma door is idle in play; every new attribute term that is a mu-shift lands here. |
| E-16 | **The verb table's header forbids a modifier from an office** (*"no verb exists only for office-holders, and none carries a modifier"*), against A-12 (*a seat carries a modifier*). | `verb_table.yaml:33-35` | A-12 has no place on the record today (`SocialContestInput` has no seat field, `inputs.py:85-101`). |
| E-17 | **The contract row is stale**: `module_contracts.yaml` gives `social_contest` a `persuasion_track` state (:471) and a `doc:` into the quarantined v30 (:466); the live module keeps no state (`roll.py:10-14`). | `references/module_contracts.yaml:464-480` | A reader of the contract would expect a track. |
| E-18 | **The pairs instrument models a bare person-vs-person record** (no room, no capability, no practice; `speak`/inquiries opposed by a person). | `pairs.py:147-164` | Its social slopes are of the record, not of the shipped act (B.2); a redesign with exchanges needs `social_pairs` to call the module's new entry rather than `roll`. |
| E-19 | **`arrest` is a physical act on the social roll** (prize `a standing`, Coordination), marked [ASSUMPTION] by its own row. | `verb_table.yaml:187` | A body contest routed to the influence subsystem. |
| E-20 | **S27.4's refusal on `arrest` is labelled with the counterparty's kind** though the actor's pool failed. | `verb_table.yaml:171-208` `refusal_note` | Minor. |

## F. What I could not determine (for stage 2)

1. **J-11 — one roll, or exchanges in which a side can be rattled?** What exists: the live path is ONE draw per act
   (`roll.py:197-206`; H-336), and a proceeding is a sequence of separate acts (`open_case` dockets, `speak` acts at a
   sitting, `determine` rules) with no state carried between them. `sitting_exchanges` is named only in plan files
   (`master/instructions/IS_B2_SC_FI_CORE_CHAR.md:153-195`, B24, HEAR_B, PROPOSED: rosters `issue_rungs`,
   `hearing_moves`, `hearing_faults`); nothing in `engine/` or `modules/` reads it (grep). The retained kernel IS an
   exchange state machine (A.3, contrast paragraph), refused at SC-05 for its interface (`roll.py:16-37`), not for its
   structure. **The smallest exchange structure the six roles need**, read off what they name: (a) a per-side state
   carried across a bounded number of exchanges: a rattle or composure mark (Grace holds it, Will prevents it,
   Attunement aims at it) and a persistence budget (Will); (b) a live topic per exchange and a move that may leave it
   (Focus); (c) each exchange one draw of the existing roll (the ruled sigma-leverage roll stays the draw; the exchange
   is a loop around it), so the margin, ladder and S27.4 stay single-owned; (d) a stop: a bound on exchanges, a side
   yielding, or the state crossing a line. Whether the exchange belongs inside the module entry (one call returns one
   `Margin` after N internal draws) or in the season loop (N acts) is stage 2's; the module rule (*"keeps no state
   between calls"*, `roll.py:10-14`; A-25) admits state inside one call. 
2. **J-12 — ANSWERED (Jordan, 2026-11-14):** *"drop threadsensitivity, keep existing prac.thread_sensitivity"*. No
   `attr.spirit.threadsensitivity`; ten attributes. For the record: `Person.thread_sensitivity` (`state/carriers.py:843`)
   is a whole number authored at build from a cast row's `ts:` (`data/cast.py:279-283`), never written in play, read by
   one gate (`thread_read`'s `thread_sensitivity >= 30`, `data/requires.py:798-809`, `fixtures.py:1155`). It bears on
   the contest only through design intent (Thread use in a contest must be perceived by the adjudicator,
   `social_contest_v30.md:560`, `:580`, reference); nothing on the live social path reads it.
3. **What the new attributes do to the existing pools.** Jordan's roles assign Presence to delivery, Reason to the case,
   Focus to staying on topic. Today `tell`/`speak` pool on Focus as *exactness of relay*, and `argue` pools on Presence
   alone. Whether Focus stays a pool input for `tell`/`speak` or moves to a topic term, and whether `argue`'s pool
   becomes an average (the 2026-11-13 rule) of Presence and Reason, is stage 2's.
4. **Where Will ends and Grace begins.** Will: *"to not get rattled in first place"*; Grace: *"remaining composed in face
   of difficulties and challenges"*. Both touch one rattle state. One reading: Will decides whether a blow rattles,
   Grace how a rattled speaker carries himself (his manner and his standing afterwards). [ASSUMPTION: that split — basis:
   the words "in first place" vs "in face of"]; Jordan may read it otherwise.
5. **Who the adjudicator is in each case.** Today: for `speak`, the bench at the speaker's place; for `determine`, the
   party's place (H-215 records the difference); for `argue`/`tell`/`lie`, the hearer alone; nobody else. A proceeding
   type (G) would name it.
6. **Which commanding verbs are influence.** `issue`, `order_unit`, `dispatch` compel by standing and are brute
   functions; whether obedience is in question (and so drawn: `27_MB_A_command_and_the_obedience_draw.md`, PROPOSED)
   decides whether they call the subsystem.
7. **What a won or lost proceeding writes.** `speak` writes nothing (E-11); `argue` moves pursuits regardless of topic
   (E-10). The six roles act on how the contest goes; what it leaves in the world is a separate design.
8. **`determine`'s roll** (E-9): whether the verdict is a draw of the judge's, the result of the speeches, or a
   brute decision once the case is heard.
9. [UNVERIFIED] Whether any shipped seed actually executes an `argue` (its formation note records 0 formed at three
   seeds, `verb_table.yaml:139`); not re-run here.
10. Whether a computed `carry` (which writes `DocketItem.arrangement`, `verb_table.yaml` `carry` row) ever names an
    arrangement row in play [UNVERIFIED; `open_case` does not: G.1].

## G. Proceeding types

Jordan, 2026-11-14 (relayed): *"proceedings, as I understand them to be designed, have different types based upon what
is at stake, what factions are involved, what the venue is, who the adjudicators are, who the audience is, how and what
kind of arguments/speeches are presented and in what order, what system is used to render a verdict, etc; from heresy
trial to parliamentary debate to private negotiation to rallying a crowd etc"*.

### G.1 What the live engine defines

**A proceeding type exists as DATA: `engine/season/arrangements.yaml`, nine rows**, loaded by one loader with a closed key
set (`data/arrangements.py:73-77`): `id, disposal, bench_basis, floor, records_dissent, venue_min_rank, term_required,
appeal_basis, interposed, order, proofs, disposes, disposal_reach, quorum`.

| row | disposal | order | proofs | disposes / reach | venue_min_rank | floor | other |
|---|---|---|---|---|---|---|---|
| `arbitration` | bench | alternating | record, testimony, oath | oblige / room | hearth | closed | |
| `parliamentary_debate` | bench | rank | — | Record / realm | duchy | open | records dissent; interposed procedure |
| `council_of_state` | bench | rank | — | Record / realm | duchy | closed | interposed procedure |
| `legal_trial` | bench | rank | record, testimony, oath | detain / settlement | settlement | open | appeal by `determine`; interposed person, procedure |
| `tribunal` | bench | rank | record, testimony, oath | ban / body | settlement | admitted | interposed office, procedure |
| `interrogation` | bench | scripted | testimony, confession | detain / room | hearth | closed | |
| `inquisition_hearing` | bench | scripted | testimony, confession, record | ban / body | settlement | closed | appeal by `determine`; interposed office, procedure, document |
| `excommunication_deliberation` | **declared** (quorum 2) | rank | record, testimony | ban / realm | settlement | closed | interposed procedure, ceremony |
| `negotiation` | **mutual** (bench_basis none) | alternating | record, testimony | oblige / room | hearth | closed | |

The header names three more that are NOT seeded: `audience / embassy`, `appeal to a higher authority` and `public debate`
(`disposal: none`, `disposes: standing`, outside the enum), `arrangements.yaml:24-29`, `:43-47`. Beside the rows:
`speech_kinds` (six forensic issue-ladder kinds: `deny`, `cite_incompatible`, `impugn_motive` (Partial at best),
`concede_fact`, `concede_harm`, `hand_error_back`; `arrangements.yaml:57-96`), and the rosters `genres` (forensic,
deliberative, epideictic: *"NOTHING DERIVES `genre` YET"*, `rosters.yaml:3265-3275`), `proofs` (record, testimony, oath,
confession), `ladder_rungs` (:3289).

**What code reads at runtime, and what it does not:**

| field | read by | effect |
|---|---|---|
| `disposes` | `_eff_determine` (`effects_information.py:614`), `open_case`'s check (:429), the write gate's disposal kinds (`state/gate.py:274-275`) | what a determination opens (oblige, detain, ban) |
| `disposal == "declared"`, `quorum` | `declared_sitting` (`world_q.py:722-734`), the `vote` conjunct's stems (:4745) | a vote count gates `determine`'s admission for `excommunication_deliberation` |
| `bench_basis` | not read: `judging_set` uses the constant `BENCH_BASIS` (`world_q.py:676-681`) | — |
| `order`, `proofs`, `floor`, `interposed`, `venue_min_rank`, `term_required`, `appeal_basis`, `disposal_reach`, `disposal == "mutual"` | nothing at runtime (grep; `records_dissent` by a harness probe only, `harness/probes.py:2728-2739`; `term_required` *"has no reader yet"*, `effects_information.py` `_disposal` docstring; H-216 for `proofs`) | — |
| `speech_kinds`, `genres`, `ladder_rungs` | the loader only (`data/arrangements.py:136-140`; `data/rosters.py:874-876`) | — |

**And no computed case names a row.** A docket item carries its arrangement only when a hand-built `open_case` declares
it; *"`None` -- every computed case -- is the realm's path"* (`effects_information.py:417-426`; `world_q.py:675-677`,
:726-727). So in play every proceeding is heard under no type: the bench is whoever holds a `determine` grant over the
place, the verdict is one `determine` roll, and the arrangement rows are reached by tests and hand-built worlds only.

**The other parts of a proceeding, live:**
- **Venue.** The act's rung is the actor's place (`sides.py:171-172`); buildings are rungs of kind `hearth`
  (`venues.yaml:21-27`) with an institution tag `serves:` (Crown, court, Parliament, Church, Guild, Löwenritter, Einhir,
  Altonian; `venues.yaml:64-109`), read at build to seat inhabitants (`harness/populated.py:1291`, `:1305`) and not by any
  contest.
- **Adjudicators.** The bench, `judging_set` (`world_q.py:642-719`): live holders of a `hold` granted `determine` whose
  office's scope contains the venue. One kind only: a seat-holding bench. No single-judge / panel / crowd / no-adjudicator
  distinction.
- **Audience.** None beyond the bench (`reception` sums the bench, `world_q.py:833`). Witnesses who see an act deposit
  claims at WITNESS (`loop/witness.py`) but do not judge it.
- **Verdict systems.** (a) `determine`: one bench member's roll (E-9), admitted by `bench.size` quorum; (b) a declared
  vote for `excommunication_deliberation`, as an admission gate, not a tally that decides; (c) `negotiation`'s
  `disposal: mutual` is loaded and read by nothing; the plan's form is the counterparty's own sampled choice
  (`05_SC_negotiation_scene.md`, PROPOSED); (d) a ruler's decree is `issue`, a brute function; (e) a crowd's mood: none.
- **Order and kinds of speech.** `order` (alternating, rank, scripted) and `speech_kinds` exist as data and are unread;
  the live path has one kind of speech (`speak`) and one draw per act, in whatever order the season's acts fall.
- **Stakes.** `disposes` + `disposal_reach` on the row (read: `disposes` only); on the act, the prize (`a standing`, `a
  proposition`, `a matter`), which picks only the provider and whether a bench hears it (`rosters.yaml:1763-1789`).
- **Factions involved.** Nothing on the row. Derivable: the seats' factions (`seat_faction`, `state/gate.py`), the
  `serves:` tags of the building, the parties' affiliations (`Person.conviction`).

### G.2 What the retained kernel and the design documents name (reference)

- **Kernel, eight proceedings** (`systems/social_contest/sim/contest/modes.py:485-515`, `dictionaries.py:503-602`): Formal
  Contest (3 exchanges, alternating, Crowd), Grand Contest (5, alternating, Crowd), Royal Audience (3, Crown objects
  throughout, resistance halved for the petitioner, Expert Judge), Church Tribunal (1-5, Inquisitor proposes, halved for
  the accused, Expert Judge, track starts biased, opening ground FACT), Guild Arbitration (3, symmetric, Panel voting
  weighted by standing), Casual Dispute (1, no adjudicator, no tracker), Private Negotiation (1-3, symmetric, no
  adjudicator, tracker optional), Personal Appeal (1, no adjudicator). Each: exchanges, role structure, resistance
  modifier, adjudicator type, track start, tracker mode.
- **Kernel, four adjudicator types** (`dictionaries.py:337-386`): Expert Judge (Cognition-primary), Crowd (Charisma),
  No Adjudicator (Attunement), Panel (Cognition, weighted ballot).
- **Kernel, four venue win conditions** (`modes.py:1-12`): court (ProofBar, burden on the challenger), disputation
  (ThresholdRace), assembly (TallyAtClose, the body votes), appeal (GraceThreshold); three institutional modes
  (`fused_arbiter`, `deliberative_body`, `scholastic_disputation`, :150-155); six cross-cultural venues
  (`public_oration` (the Roman *contio*), `inquisition_hearing`, `excommunication_court`, `imperial_petition`,
  `secret_council`, `memorial_remonstrance`, :157-311); three scaffolds that raise when called (Dyadic counsel,
  Negotiation, Ceremonial, :333-365); a Parliamentary adapter with a Mandate-weighted vote (`faction.py:1-6`).
- **Design documents:** `social_contest_v30.md:42-45` (adjudicator types with their settings, Crowd: *"Parliamentary
  session, public forum, street crowd"*), §7.1 Excommunication Tribunal and §7.3 Heresy Investigation lifecycle
  (`:449-497`); the 2026-09-05 proceedings proposal's `03_PARAMETERS.md` §E.1/§E.2 (the source the nine rows were
  transcribed from, per `arrangements.yaml`'s header); `05_SC_negotiation_scene.md`, `05_SC_playable_hearing_B.md`,
  `U5c_SC_proceedings_residue.md` (all PROPOSED). `canon/` holds no list of proceeding kinds (grep of `canon/` for
  parliament, heresy, tribunal, inquisition: two history passages, `canon/philosophy/08_history.md:380`,
  `canon/02_foundations_amendment_leap_mechanism.md:92`, neither a proceeding roster).

### G.3 Jordan's four, against the engine today

| type | what could represent it | verdict |
|---|---|---|
| **heresy trial** | rows `inquisition_hearing` (scripted order; testimony, confession, record; disposes `ban`), `tribunal` (`ban`, reach `body`), `excommunication_deliberation` (declared vote, quorum 2, `ban`, reach realm); the `interrogate` verb (`remit:determine`, a detainee; its note: *"the Church Tribunal is accusatorial"*, `verb_table.yaml:1797`); a `cathedral`/`chapter_house` building (`serves: [Church]`) | **PARTIAL**: the rows and the `ban` disposal are live through `determine`; the Church is not the bench (any `determine` seat over the place), order, proofs and speech kinds are unread, and no computed case names the row |
| **parliamentary debate** | row `parliamentary_debate` (open floor, records dissent, duchy and up, rank order, disposes a Record, reach realm); buildings with `serves: Parliament` (`court`, `hall`, `moot_hall`) | **PARTIAL**: the row exists; nothing reads its order or floor; no members' vote decides (its disposal is `bench`, one roll); no audience |
| **private negotiation** | row `negotiation` (`disposal: mutual`, no bench, alternating, disposes `oblige`, reach room); verbs `covenant` (offers terms) and `oblige` (binds oneself) | **PARTIAL**: row and verbs exist; `mutual` has no reader; no exchange; consent is a separate later act |
| **rallying a crowd** | no row (the unseeded `public debate`, `disposal: none`); the `epideictic` genre (*"no bench at all ... the only prize is standing"*) in a roster nobody reads | **ABSENT**: no crowd or audience carrier, no verdict by mood |

### G.4 What a proceeding-type carrier would hold, and where the data already lives

| part (Jordan's list) | existing home | state |
|---|---|---|
| what is at stake | `arrangements.yaml` `disposes`, `disposal_reach`; the act's prize | `disposes` read; reach unread |
| factions involved | none on the row; derivable from seats (`seat_faction`), `venues.yaml` `serves:`, `Person.conviction` | absent as a field |
| venue | `venue_min_rank` on the row; the building kind and `serves:` in `venues.yaml` | loaded, unread at the contest |
| adjudicators | `bench_basis` (unread; constant used) + `judging_set` | one kind only; no single / panel / crowd / none field |
| audience | none | absent |
| kinds of speech and their order | `order`, `speech_kinds`, `genres`, `ladder_rungs` | loaded, unread; no exchange count |
| proofs admitted | `proofs` | loaded, unread (H-216) |
| verdict system | `disposal` (bench, declared, mutual; `none` named, unseeded), `quorum`, `records_dissent`, `appeal_basis` | `declared`/`quorum` read as an admission gate; `bench` = one `determine` roll; `mutual` unread |

The precedent for where such a carrier lives is already in the tree: a roster row per type that code reads at runtime,
as `contest_subsystems` (`rosters.yaml:1695-1789`, read by `manifest.resolve`) and `arrangements.yaml` (read by
`data/arrangements.py`) are. The missing links, as found: (1) the case-to-type link for a computed case
(`effects_information.py:417-426`); (2) any field of the row on `SocialContestInput` (`inputs.py:85-101`), so the module
cannot see the type it is resolving; (3) the readers for the loaded-but-unread fields above.

