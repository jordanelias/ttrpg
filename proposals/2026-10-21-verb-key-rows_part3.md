# Verb key rows — part 3: §3.1.10-§3.2 key rows, §4 why no per-row value fan, §5 host rows, §6 cost and ordering, §7 open items
## Status: PROPOSED (2026-10-21). Not ratified; merging ratifies nothing unless Jordan so rules. Static reading. No season, probe or test ran. One import of three loaders (running their import-time checks on the shipped tables) listed three rosters. No proposed row was loaded; every claim that a skeleton loads is unverified.
## Parts, in reading order: [head](2026-10-21-verb-key-rows.md) (§1 head, §2 disposition table) · [`_part2`](2026-10-21-verb-key-rows_part2.md) (§3.0-§3.1.9 key rows) · **this file** (§3.1.10-§3.2 key rows, §4 why no per-row value fan, §5 host rows, §6 cost and ordering, §7 open items).

Citation shorthands, K-1..K-10 and F-1..F-6 are the head's §1.

---

## 3 (continued). Key rows

Continued from [`_part2`](2026-10-21-verb-key-rows_part2.md) §3.1.9; the rules of §3.0 apply.

#### 3.1.10 `propose` and `allege` — KEYs on `utter` (composed bodies)

```yaml
  - verb:        "propose"
    stratum:     "social"
    eligibility: ["own"]
    beneficiary: "none"
    requires:    "—"
    writes:      ["Proposition.exists"]
    emits:       ["proposition.proposed"]
    emits_on_refusal: []
    grade:       "assumption"
    source:      "this proposal §3.1.10; U:96; `utter`'s row (VT:1315-1324)"
  - verb:        "allege"
    stratum:     "social"
    eligibility: ["own"]
    beneficiary: "none"
    requires:    "—"
    writes:      ["Proposition.exists"]
    emits:       ["proposition.alleged"]
    emits_on_refusal: []
    grade:       "assumption"
    source:      "this proposal §3.1.10; U:96; `utter`'s row (VT:1315-1324)"
```

- **Why keys and not one operand on `utter`**: a person chooses whether to propose a course or to allege
  a fact, and a per-row value cannot be chosen (F-5; `_part3` §4).
- **Effect**: composed. `_eff_propose` and `_eff_allege` call one helper extracted from `_eff_utter`
  (`loop/effects_information.py:876-910`), which mints the Proposition and the maker's `hold` with the
  mood read from a roster `utterance_moods` in `rosters.yaml` (`keys: [verb_table]`,
  `values: {propose: OUGHT, allege: HOLDS}`), by `UTTERANCE_MOODS.get(a.verb)`. A hand-built act's
  payload `mood` still wins, as at `:904`. The walker follows the helper (DV:457-465), so each key is a
  `hold` opener in its own name.
- **No roster of every mood**: none is proposed. `utterance_moods`
  maps two verbs to two moods and holds no `WAR`; `WAR_MOOD` stays where it is
  (`queries/faction_q.py:210-216`), `declare`*'s, and nothing reads it from a roster. One owner each.
- **Reader that makes them keys**: `world_q.ambitions` (`queries/world_q.py:1700`): a live `commit` to a
  Proposition is an ambition only if its mood is OUGHT (`:1733`). So a person who commits to a proposal
  gains an ambition and one who commits to an allegation does not. `threaten` is not here: it is
  §3.1.11's, a `tell`.
- **Alignment**: each carries `utter`'s cells (`deontological_instrumental: -0.7`, "the uttered word
  binds", RO:3107; the other six `null`). The claim lands on the Proposition, a subject no regard is read
  of, so no `deed:` cell is needed [ASSUMPTION: no reader judges a Proposition as a doer — basis:
  `regard` is asked of persons (PQ:336)].
- **Creed**: each carries `utter`'s shared cell `sacred: 0.8` (RO:2469, "the word once spoken").
- **Capability**: none (uncontested).
- **Chooser**: as `utter` (untyped, `requires: "—"`, so no operand is bound). With both keys built, a
  computed `utter` is a second OUGHT mint beside `propose`; §5 records it.
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: moods stay a hand-built payload of `utter`]`.
- **Falsifier**: a person who commits to an `allege`d Proposition has no new ambition (`ambitions`), and
  one who commits to a `propose`d one has.
- **Would be observed by**: that unit test, unbuilt.

#### 3.1.11 `threaten` — KEY on `tell` (shared contest; replaces the intent draw for its row)

```yaml
  - verb:        "threaten"
    stratum:     "social"
    eligibility: ["own"]
    beneficiary: "actor"
    requires:    "the teller holds a claim on the subject, and the person told is with the teller"
    requires_typed:
      all:
        - form:      own_ledger
          of:        subject
          conjunct:  holds
        - form:      relation
          of:        to
          relation:  with
          conjunct:  hearer
    counterparty: to
    contests:    "a standing"
    writes:
      Overwhelming: []
      Success:      []
      Partial:      []
      Failure:      []
    emits:
      Overwhelming: ["news.told", "threat.made"]
      Success:      ["news.told", "threat.made"]
      Partial:      ["news.told", "threat.made"]
      Failure:      ["news.untold"]
    emits_on_refusal:
      holds:        ["threaten.refused"]
      hearer:       ["threaten.refused"]
      counterparty: ["threaten.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.11; U:96 (threaten, moved from `utter`); `tell`'s row; `declare_intents`"
```

- **What a threat is, in the code's terms**: a telling whose `said` is the teller's own declared intent
  (`person_q.intent_said`, PQ:884-891) naming the hearer. `declare_intents` already turns a telling into
  such a disclosure, by chance `intent_disclosure` per telling (`decision/choose.py:486-516`; shipped
  `0.0`, `data/fixtures.py:773`, at which no draw is taken). The key: for a row in a roster
  `disclosing_tellings` (`keys: [verb_table]`, `values: [threaten]`), `declare_intents` always discloses,
  and only an act in a later scene whose operands name `to`; a `threaten` with no such act is declined at
  CHOOSE, as `opening_set` declines a `tell` with nothing to say (VT:1073-1075). `tell` keeps the draw.
  This is `confide`'s move on `telling_privacy`, made on `intent_disclosure`.
- **Reader that makes it a key**: **intent**. The hearer's ledger receives `(teller, intent:<verb>, …)`
  naming him, and `world_q.named` (`queries/world_q.py:750`, via `intent_named`, PQ:894-900) raises his
  `claim_landed` question about the teller (RO:1913-1919). Today no such claim exists in shipped play.
- **Alignment**: all seven `null`, `confide`'s reasons (the claim lands on the topic; `tell`'s
  `uncelled:` reason).
- **Creed**: none. **Capability**: `copying`, `tell`'s, the same roll.
- **Chooser**: `tell`'s fan, narrowed at CHOOSE as above. `threaten` has a row only to make the
  disclosure a choice. The roll is `tell`'s (whether the hearer takes the telling in); what the threat
  then does is the hearer's own choice through `named`, not a roll that moves him, the research's
  cheap-talk reading (`_part11:192-197`).
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: threats stay `intent_disclosure`'s draw]`.
- **Falsifier**: at `intent_disclosure: 0.0`, an executed `threaten` leaves the hearer holding an
  `intent:` claim naming him and a `claim_landed` question about the teller; a `tell` in the same world
  leaves neither.
- **Would be observed by**: that unit test, unbuilt. R-08's `measure:` (`requirements.yaml:1312`) does not
  see it (all-null cells).

---

### 3.2 Keys that wait (PARKED names whose eventual form is a key)

None is buildable until its dependency lands; each would otherwise be a carrier nobody reads (`ID-13`).

| key | host and body | cell / counterparty | writes | own kinds | waits on | falsifier when built |
|---|---|---|---|---|---|---|
| `assassinate` | `fight`, composed on `_eff_kill`'s helper | `fight`'s + a held cover (`existence` of a `cover` Record, `relation held_by`) | `fight`'s bands | `person.assassinated`, a `covert_kinds` member (§3.0) | `conceal`'s cover Record and its mask on `seen.who`; the seam's aim input (yields refused) | witnesses hold the death and no `seen.who` naming a covered actor, at the cover's degree; `trail_of` later finds it |
| `capture` | `fight`'s contest, composed | `fight`'s cell | `Felled`: a `detain` opened, not `Person.exists`; `Wounded`: `Person.body` | `person.captured` | the seam's aim *alive* | a Felled subject of `capture` is alive and detained; of `fight`, dead |
| `champion` | `challenge`/`accept` | a third person operand (the principal); needs a second known-person fan name (the roster holds `to` only, RO:1905) | as host | `duel.championed` | the `challenge` Record (PC-10b), a stakes reader (M3) | the principal's stake moves on the champion's band |
| `besiege` | `march`, composed | `march`'s | no field; a siege term on the Rung | `siege.laid` | M-6 | a besieged Rung's stores fall per season while no field is fought |
| `testify` | `tell`, no body | `tell`'s + the hearer sits on the bench of a docketed matter about the subject | `[]` | `news.told`, `testimony.given` | a hearer-side bench form; a reader of `testimony` at `determine` | a determination weighs testimony and not gossip |
| `flatter` | `praise`'s | `praise`'s; the praise the teller does not hold | `praise`'s | `flattery.given`, a `covert_kinds` member; whether the hearer's own claim carries it is `lie`'s design | `lie` (J-C-6) | the teller's own cells separate flattery from praise; `trail_of` finds it |
| `track` | `examine`'s route | a Person quarry and presence at the Rung he left | `[]` | `quarry.tracked` | an inquiry entry that finds a person's leaving acts (RO:2232-2250) | the finder holds `contain.path:<dest>` for the quarry's last `travel.moved` |
| `coup` | `conspire`* | the plot Proposition live with enough commits | a seat `hold` closed and opened | `seat.usurped` | an executor of the plot | the plotter seated and the holder unseated in one write |
| `repay` | `transfer`, composed | a held `debt` Record naming the payer | `Rung.stores`; `Record.exists` on full payment | `debt.repaid` | `borrow`* | a full repayment ends the debt; a partial one leaves it |
| `bargain` | `exchange`, contested | `exchange`'s, typed | as `exchange`, price by degree | `bargain.struck` | `H-94`; a price prize | the price differs by degree |
| `navigate` | `move` | `move`'s | `move`'s | `move`'s | M-WT-1, M-WT-3, then `verb_capability: navigate` | two travellers on one route differ in time lost by navigation capability |

---

## 4. Why no name is carried as a value fanned on its host's row

A tempting fourth disposition carries a name as a value of one operand on the host's row, fanned in
`opening_set` as `said` is. This proposal does not use it, because such a value cannot be chosen. Two
Candidates of one row that differ only in a fanned value have the same act id: `act_key` builds the id
from the subject, the row's known-person operands and the seat and nothing else (DV:1112-1121), so the
second would be refused as a duplicate by the act store, the failure `act_key`'s own docstring records
for `tell` before T4 (DV:1098-1102). They have the same score: the pursuit term is
`align(c.verb, axis)` (`decision/choose.py:149`), keyed by verb. They draw the same noise: the Gumbel draw
is keyed `choice:{verb}:{subject}` (`decision/choose.py:381`). And no person-side reader reads the value.
`said` is not a counter-example: it is one value per subject, fixed by `said_of`, not a choice among
several. So a value that should vary what a person chooses is a KEY, with its values in a roster keyed
by `verb_table` (`graded_inquiries`' shape, RO:1104-1130), which gives each value its own act id, score,
noise and alignment cells; and a value the host's own operands or world state already fix is DERIVED,
recovered by a predicate (F-1). Thirteen names look like such values at first reading. They go:
`propose` and `allege` to KEY (a person chooses between them); `provision`, `equip` and `peace` to
DERIVED; `rally`, `pursue`, `retreat`, `withstand`, the reserve, `formation`, `alliance` and `tribute`
(U:323) to PARKED.

Three words are not used for new operands or categories, under CLAUDE.md §4: `term` (already
`TERM_KEY`, a positive whole number of seasons on a `confer`, `loop/effects_governance.py:34-53`), `order`
(an ordinary word for a command; the `marshal`* Record is called `battle_order` here), and `mode` (a
category word that would read as a fourth disposition). `stance` is used only for `Person.stance` and the
code's own `stance_term`.

---

## 5. What each host row keeps, and what its justification cell should now say

"Justification" is the upload's fourth column. A host loses nothing it executes today; each change below
is a kind earned by object class (one body, the kind picked by what was written: the `Subject.earns`
mechanism, `state/gate.py:1343-1355`, used by `seize`'s two halves, VT:939-940, and by `release`'s
`commitment.ended`, VT:864), one precondition, or one roster read.

| host | keeps | changes | justification cell, proposed |
|---|---|---|---|
| `fight` | row and `_eff_kill` | none | "Floor act: attack a person. Key on its body: `accept`. `assassinate` and `capture` wait on the seam's aim input and on `conceal`." |
| `accept` | row | adds `duel.fought` on each band and three zero `deed:` cells (§3.1.1) | "A key on `fight`'s body: the duel the challenged consents to, held by witnesses as a duel." |
| `challenge` | row | none | "… `champion` waits on the challenge Record and a stakes reader." |
| `march` | row | none | "The only act that contests ground. `storm` is every fought march; `besiege` waits on a siege state (M-6)." |
| `tell` | row, `uncelled:` line, `news.told` as the told-deposit trigger | none to the row. Its kinds `news.told` and `confidence.broken` become PAIRED once `confide` and `threaten` emit them (F-2); both value 0 before and after, since `tell` is uncelled and the table's only `deed:` keys are `matter.undetermined`, `person.died` and `body.changed` (RO:2812, :2908, :3061-3062, :3123-3124). `_circle_of` reads `confided_tellings`; `declare_intents` reads `disclosing_tellings` | "Moves an unwritten claim between persons. Keys: `confide` (a chosen circle), `threaten` (a chosen disclosure of intent), and on its prize `praise` and `insult` (a regard written). Confession and confrontation are recovered from what is told; counsel cannot be told from news of a motion. Waiting: `testify`, `warn`, `flatter`, `lie`." |
| `utter` | row; the payload `mood` for a hand-built act | its body's mint moves to a helper `propose` and `allege` share (§3.1.10). With `propose` built, a computed `utter` is a second OUGHT mint; it stays only for hand-built moods [ASSUMPTION: a `formation_decline_note:` on `utter` once `propose` executes; revert: both form] | "The one mint of a Proposition. Keys: `propose` (OUGHT) and `allege` (HOLDS)." |
| `commit` | row | one per actor: `_eff_commit` returns `NO_CHANGE` when the actor already holds a live `commit` to the Proposition, so the gate's `NoOpReceipt` emits `commitment.refused` (G4's decline, `loop/effects.py:44-46`). Not a typed conjunct: the grammar has no "no live edge" form, which is why `oblige`'s guard is a predicate (`_req_oblige`, `loop/predicates.py:339`), and a predicate would displace `commit`'s typed cell (the fold evaluates one or the other, VT:176) | "A person binds himself to a Proposition, once. A vote is a member's commit to the motion; an oath a commit to a HOLDS claim." |
| `speak` | row | none | "… its moves (refute, concede, object, define) wait on the issue-rung write; to plead is to speak." |
| `petition`, `convene`, `determine` | rows | none | names derived only (accuse; adjourn; arbitrate) |
| `examine` | row's columns | **rename to `search`, recommended.** Its own justification is "search a place" (U:139). Precedent: `FIGHT-RENAME`, where "only the `EFFECTS` key and its row moved" (`loop/effects_combat.py:32-33`). Price: every `examine` act id moves (K-9), every seeded hash where one executes, and the goldens re-record, said so (CLAUDE.md §7); the research batches renames for that reason (R-10, `_part3:239`), and this one joins that batch rather than waiting or escalating | "Reads what happened at the Site where the actor stands. `track` waits on a finding of a person's leaving acts." |
| `survey` | row and `_eff_survey` | none to the row; its rebuild's place sheet is what `audit` and `scout` wait on | "… Keys: `audit` (a seat's, under its purview, heard by its obligees) and `scout` (by presence). A census is a survey of a place." |
| `confer` | row | none; `conferral_bases` stays `[appointed, elected, annex]`, `open: false` (RO:2064-2082) | "The only act that fills a seat. To appoint is to confer on an `appointed` seat, to designate to confer the heir seat, to steward to confer for a term; to elect waits on a count of commits (M-COUNT)." The upload's "Appoint, designate and elect are bases of it" (U:255) is wrong against the roster and should go |
| `release` | row and `_eff_release` | earns `seat.resigned` when the closed edge is a `hold` on an Office (the research's M-RESIGN, `_part14:567`), beside `tenure.closed` | "The holder closes his own edge. Resigning, abdicating, abandoning a place, denying a gift and withdrawing a petition are releases of what each holds." |
| `transfer` | row and `_eff_transfer` | earns `relief.given` when the receiving rung is in shortfall (`_part14:586`) [UNVERIFIED: the world read that decides a shortfall] | "The one conserving mover of matter by consent: pay, haul, relieve. `repay` waits on the debt Record; `tribute` on `covenant`." |
| `seize` | row | none | "… conquest is its Rung half. `annex` is a conferral basis, not a taking, and waits on M-ANNEX." The upload's U:366 fold of `annex` should go |
| `build` | row | none | "… to fortify is to build a `garrison` Site; `improve` waits on M-WORKS (b)." |
| `work` | row | none | "… mining is work at a `seam`; fishing cannot be told from a harbour's other labour; `cultivate` waits on a `field` site kind and `hunt` on a carrier for wild food." |
| `exchange` | row | none (still blocked on `H-94`, VT:330-339) | "… trade, buy, sell and barter are exchanges, recovered by which side gives `coin`; `bargain` waits on `H-94` and a price prize." |
| `move` (U's `travel`) | row | none | "… navigate, ride and sail wait on a priced route (M-WT-1..3)." |
| `give`, `oblige` (U's `pledge`), `revoke`, `establish`, `issue` | rows | none | derived names only: cede; swear; dismiss; amend; warrant and commission |
| the 17 unbuilt hosts (`levy`, `muster`, `marshal`, `supply`, `pillage`, `proclaim`, `covenant`, `declare`, `recruit`, `conspire`, `assign`, `craft`, `conceal`, `mend`, `tend`, `train`, `marry`) | — | when each lands, its row names its keys and derived names from §2 | e.g. `levy`: "… paid troops are `hire_troops`, a key"; `pillage`: "… `sack` is a key, barred by `surrender`"; `covenant`: "… peace is not a covenant term: it is the release of a war commit (`queries/faction_q.py:229-232`)" |

Two of the critique's internal contradictions (B8) close under this table: `heal` is derived from NP's
`tend` (#110) and threadwork's `mend` on a body is narrated as a mend (#52); `swear` is derived from
`oblige` for fealty (#115) and from `commit` for an oath to a claim (#35), told apart by the object.

---

## 6. Cost and ordering

### 6.1 New rows

| subsystem | new, host built | new, once the host row exists | amended | waiting (§3.2) |
|---|---|---|---|---|
| PC | — | — | `accept` | `assassinate`, `capture`, `champion` |
| MB | — | `hire_troops` (`levy`), `sack` (`pillage`) | — | `besiege` |
| SC | `confide`, `praise`, `insult`, `threaten`, `propose`, `allege` | — | — | `testify`, `flatter` |
| FI | — | `audit`, `scout` (`survey`'s place sheet) | — | `track` |
| GV, FA, EC, WT | — | — | — | `coup` (FA); `repay`, `bargain` (EC); `navigate` (WT) |
| NP | — | `teach` (`train`) | — | — |
| **total** | **6** | **5** | **1** | **11** |

### 6.2 What each new row trips, and where

| at | check | owner | the new rows that meet it |
|---|---|---|---|
| import | K-1, K-2, K-3 | `data/verbs.py::_load_verb_table` | all eleven |
| import | K-5 density: seven cells or an `uncelled:` line; and every new `deed:<kind>` key must be a kind some row emits (DV:1424-1433) | `_load_alignment` | all eleven; the `deed:` cells of `accept`, `hire_troops`, `sack`, `insult`, `teach` |
| import | `keys: [verb_table]` on each new roster (`confided_tellings`, `disclosing_tellings`, `regard_acts`, `utterance_moods`) and on the new `verb_capability` entries (`confide`, `threaten`) | `data/rosters.py` [UNVERIFIED: that a generic table's `keys:` is enforced against the verb table at load; it is for `alignment` (DV:1425-1433) and `affiliation_engagement` (`data/affiliations.py:159-162`)] | confide, threaten, praise, insult, propose, allege |
| driver construction | K-4 `check_effects`, `check_preconditions` | `manifest/registry.py:599`, `:637` | all eleven |
| driver construction | invariant 11: a fixture named by code has a register row | §B.13 item 11 | `regard_act_weight` |
| test | the always-refused and never-attempted pins | `tests/test_season_shape.py:~7927` (the assertion over `refused_only`) | any new row that forms and is refused in the corpus; re-record, said so |
| test | seeded hashes | `tests/test_build_realm_determinism.py`, `tests/test_aperture.py` and the other `content_hash` readers (`grep -l content_hash tests/`) | any new row chosen in a seeded world; `accept`'s extra kind; `confide`'s and `threaten`'s emissions (§6.6) |

The opener walker (F-4) is NOT on this list: every key on a Tenure-opening host composes its own body
(§3.0), and the walker follows helpers.

### 6.3 Chooser growth

Not measured; the formula only. For a person `p` answering question `q`, let `T` be the topics `tell`
forms on with a non-empty `said`, `K` the persons `p` knows (`known_persons`, PQ:954), `P` the Person
referents of `q`, `R` the Rung referents in a seat's purview, and `s` the number of `p`'s seats granting
the remit (H-134's per-seat Candidates).

- `confide`: `+|T|·|K|`, `tell`'s count again.
- `threaten`: at most `+|T|·|K|`, narrowed at CHOOSE to hearers some later-scene act of `p` names.
- `praise`, `insult`, `teach`: `+|P \ {p}|` each.
- `audit`, `hire_troops`: `+|R|·s` each.
- `scout`, `sack`: at most `+1` each, and `0` unless a question raises the rung `p` stands at (§3.1.3).
- `propose`, `allege`: `+1` each wherever `utter` forms.

The score runs `align` per Candidate per axis (`decision/choose.py:149`), so cost grows linearly in the
added Candidates; `confide` and `threaten` dominate wherever `tell` already does.

### 6.4 Ordering

1. **Buildable now, on shipped hosts, before `lie`, `M-COUNT`, `H-85`, `M-6`, `H-94`:** `accept`'s kind;
   `confide` (with `_circle_of`'s roster read); `threaten` (with `declare_intents`'s); `propose` and
   `allege` (with the mint helper out of `_eff_utter`); `commit`'s one-per-actor decline; `release`'s
   and `transfer`'s earned kinds; the `examine` → `search` rename, in the research's rename batch.
2. **After `H-194` ships `stance_polarity: declared`:** `praise` and `insult` (with the stance-append
   helper moved out of `_eff_march`). Under the shipped `legacy` arm the stance term cannot separate them
   (§3.1.5).
3. **Once the host row exists:** `audit`, `scout` (`survey`'s place sheet); `hire_troops` (`levy`);
   `sack` (`pillage`; its bar with `surrender`; and a question source raising the occupied rung);
   `teach` (`train`, which adds the `(Person, capability)` matrix row).
4. **On their dependencies (§2, §3.2):** `flatter` after `lie`; `warn` after an intent claim can be
   held (`threaten`, step 1, supplies one); `elect` after `M-COUNT`; `trace`, `diagnose` after `H-85`;
   `besiege` after M-6; `bargain` after `H-94`; `assassinate`, `ambush`, `disguise` after `conceal`;
   `capture` and then `ransom` after the seam's aim input; the `marshal` choices after the field module
   takes a per-order input; `alliance` after an ally reader; `navigate`, `ride`, `sail` after
   M-WT-1..3.

### 6.5 What the list's columns and fold lines would change

- The Coded/Proposed column: `confide`, `threaten`, `praise`, `insult`, `propose`, `allege`, `audit`,
  `scout` become rows marked "Proposed (key on `tell` / `utter` / `survey`)"; `hire_troops`, `sack`,
  `teach` "Proposed (key on `levy` / `pillage` / `train`)"; `accept` stays "Coded, to rebuild" with the
  added kind; `threaten` leaves `utter`'s suite for `tell`'s.
- Each "Folded in (no row of their own)" line splits into up to three: **Keys** (own rows), **Derived**
  (with the predicate) and **Parked** (with the dependency). U:79 would read: *Keys: confide, praise,
  insult. Derived: confess (the teller's own deed), confront (told to its subject), counsel (low
  confidence). Parked: testify (a hearer-side bench form, a proof reader), warn (an intent claim to
  retell), flatter (lie), lie.* The research's §III.4 table (`_part3:194-222`) uses one column, "folded
  into it", for all three and would take the same split.
- Three fold lines are wrong against the code and drop: `designate`/`elect` as bases (U:255), `annex`
  under `seize` (U:366), and peace as a covenant term (U:323; peace is the release of a war commit).
  `hunt` (U:382) moves to Parked, as the research found (`_part17:210`).

### 6.6 Hash and emission moves

- A new key mints new act ids for its own acts and moves no existing id (K-9).
- A run's `content_hash` moves wherever a new row is chosen in place of something else; that is every
  seeded world in which one forms and wins the score. A behaviour change and a golden re-record, said so
  (CLAUDE.md §7).
- `accept`'s second kind adds one Event per executed `accept`.
- **`confide` changes what `tell` emits at shipped settings.** Today no circle exists at
  `telling_privacy: 0`, so `confidence.broken` is never emitted. Once a `confide` executes, its hearer
  holds the claim under a circle, and that hearer's later `tell` of it to an outsider emits
  `confidence.broken` (`loop/resolve.py:532`). `tell`'s row is unchanged and its Events change.
- **`threaten` changes what hearers hold at shipped settings.** At `intent_disclosure: 0.0` no intent
  claim exists; an executed `threaten` deposits one and `world_q.named` raises a `claim_landed`
  question that does not arise today.
- `release`'s and `transfer`'s earned kinds change emitted kinds where they execute.
- The `examine` → `search` rename moves every `examine` act id (K-9), in the rename batch.
- `KIND_VERB`: every new kind maps to its one row; `news.told` and `confidence.broken` become paired at
  no valuation cost (§5, `tell`). `flatter`, built on `praise`'s prize with its own covert kind, pairs
  nothing.

---

## 7. Open items

None survives CLAUDE.md §0's five answer-it-first tests; the two queued items this proposal touches
(J-C-6 `lie`, and `succeed`'s basis) are already on the queue and are not re-flagged.
