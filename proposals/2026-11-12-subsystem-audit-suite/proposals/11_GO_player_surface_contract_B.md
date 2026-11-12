# GO — the player-surface contract, B: four readings and one scene pair, for every subsystem

Reconciled: 2026-11-12, U5d closure — folded **A-48** (the slate is a list of questions for the player; NPCs take the first), **A-9** (a turn is a short sequence), **A-47**, **A-43** and **A-1**. §1 (R77: "the Scene Slate is `View.questions` in attention order with the scene budget; no second generator") stands for the generator and gains the choice: the player is offered the ordered list and picks which questions to attend within the budget; an NPC takes the first (`question_aggregation_rule = "first"` stays the NPC's rule). A question opened by a threshold is marked mandatory and cannot be passed over (A-47). The scene pair carries a scene's steps in the chooser's order, a step able to hang on the band of the one before (A-9). Auto-resolve is the same call without a decider (A-1), as §6 has it. A shown person carries a legibility band and, at low legibility, no reasons (`U5d_WR_zero_coherence_unknowable.md`). The player/NPC difference A-48 introduces is confined to which question is attended; the resolver is one.

## Status: PROPOSED

Supersedes `11_GO_player_surface_contract.md` (SURF). Carries `audits/11_GO_audit_addendum_B.md`
F-GO-15 to F-GO-19 and resolutions R50–R59, R72–R74, R76–R78. Lane: GO states the interface; the files
are IN's and CHAR's (`engine/season/decision/`, `queries/person_q.py`, `harness/play_surface.py`) and
each module lane's (the scene pair). It cites and does not restate: CHAR's `watch` hook
(`02_CHAR_reason_trail_and_small_edits.md` Part A) and own-state decline (`02_CHAR_offer_what_can_be_done.md`),
PC's round and approach (`03_PC_duel_round_and_approach.md`), MB's phase decider and report
(`04_MB_playable_field_scenario.md` B, D; `04_MB_typed_outcome_and_one_path.md`), SC's ending tuple
(`05_SC_contest_record_on_event.md`) and hearing (`05_SC_playable_hearing.md`), FI's evidence items
(`08_FI_05_evidence-interface.md`) and conclusion (`08_FI_03_playable-inquiry.md`).

**What stands from SURF, and what changes.** §1 (the offer carries its terms) stands and is extended.
§2 (`explain`, as `04` §C.11 states it) stands unchanged and is not repeated here. §3 (`aftermath`) is
**corrected**: its `own_act` field cannot be computed from a `Claim`, and it is replaced by two
readings. §4 (scars and crises emit an Event) and §5 (`OFFER-CONTAINS`) stand. §6 (every scene through
one typed decider) is **corrected**: there are two kinds of play, and only one needs a decider.

## What it changes in `engine/season/` at runtime

Nothing in the automated run: every addition is a reader that writes nothing, draws nothing and holds
no token. The ranker hands out terms it already computes. A played run gains what it lacks today: the
outcome of the player's own act, what he learned since he last decided, which candidates answer which
question, and which candidates his own state withholds.

## The problem, with evidence

All readings: `populated.build_realm(0)`, one season, `PYTHONHASHSEED=0`, hash `5ab73af2…` equal to
the plain run (addendum §B7, E-B3 to E-B5). One person at one seed is a reading, not a rate.

1. **Six lanes, six shapes for "what the player sees".** SE: `sheet(w) -> dict`. FA: "a digest". MB:
   `FieldOutcome.report` of `PhaseSummary` and a `FieldPhaseView`. PC: `DuelRoundOutcome.trace` and
   `CombatTurnView`. SC: a tuple on `Event.ending`. FI: "one scenario summary line". Two surfaces that
   already exist differ on what they may read: `decision/sheet.py` takes no `World`;
   `harness/military_menu.py::menu(w, actor)` takes it. That is a scale-local interface dialect per
   lane (`CLAUDE.md` §10, shape divergence), and a port would re-implement six.
2. **A person cannot read the outcome of his own act.** `p_npc_001` took 15 acts. Two `research` acts
   ended `finding.none` at `degree=Failure`; his ledger holds **no** claim of that kind. Ten of the 15
   Events carry `observed` (what the fold read); `Event.ending` says of itself "NO PRODUCTION READER
   EXISTS AT THIS COMMIT" (`state/carriers.py:303`). Of his 119 claims, **none** carries an Event id
   or an act id as id, subject or value, so no person-side reading can pair a deed with its result.
3. **SURF §3's pairing field does not exist.** It specified `own_act: the act id of his that the
   claim's chain names`. `Claim.chain` is "WHO PASSED THIS CLAIM ON, ORIGIN FIRST", a tuple of person
   ids (`carriers.py:358-371`); `Claim.doer` is "the holder's own id when the claim records HIS OWN
   act" (`:372-381`). Neither holds an act id.
4. **The offer is flat.** Five deliberations showed 22, 32, 33, 32 and 38 candidates (157 rows in a
   season) over 33 distinct verbs. Twenty-one verbs were offered five times across the five sheets,
   whatever the question (`forge`, `sabotage`, `conceal`, `challenge`, …), and `train` twenty times;
   five appeared once (`petition`, `tend`, `lie`, `commit`, `argue`). `Candidate` carries `verb`, `subject`, `operands`; its `why` was removed because
   nothing read it (`carriers.py:591-595`). Nothing tells a client which rows answer the question in
   front of the person and which are the standing menu.
5. **Play is of two kinds and the first contract named one.** A duel's turns are not season acts, so
   the driver suspends and calls a decider (REM-31). A hearing's turns are (`speak`, `tell`, `give`,
   `determine` are rows), and SC decided the hearing is the season loop on a fixture with a callback
   on the chooser slot, with no decider. The seated person's offer at seed 0 already held `speak`,
   `argue`, `petition`, `interview`, `research`, `surveil`, `reconstruct`, `challenge`, `accept`,
   `commit`, `comply`, `build`, `found` and `tend`.

## The resolution, decided

Ladder step 4 (the precedents are `decision/sheet.py`'s rule "ranks and selects; never forms",
`PlayHost`/`CombatTurnView` for a suspended scene, and `harness/military_menu.py` for a host-side
reader of the actor's own affairs) and step 5 (one owner per reading). **The port renders five typed
readings and one scene pair; it computes none of them.**

```
SEASON SCALE, for one seated person
  person-side, under decision/ (no World; the AX-2 path scan covers them):
    situation(p, v, ask_budget)  -> Situation      what is in front of him
    offer(p, v)                  -> Offer          what he may do, why it ranks, what his own state withholds
    account(p, since)            -> tuple[AccountRow]   what he has learned since (tick, round)
    dossier(p, subject)          -> tuple[DossierRow]   what he holds about one subject (the case board)
  host-side, beside the dispatch seam (reads World; HIS OWN acts only):
    receipt(w, act_of, pid, since) -> tuple[ReceiptRow]  what each act of his came to
SCENE SCALE, for a scene the driver suspends
    <Module>TurnView · a closed choice set · decide(view) -> choice | None · an outcome carrying `trace` and `ending`
```

### 1. `Situation` (`decision/sheet.py`; `DevelopmentSheet` split in two)

```
@dataclass(frozen=True)
class AskedRow:
    question: Question            # source, referents, classes, about: as carried on View.questions
    claim: Optional[Claim]        # the claim of HIS that `about` names, where it is one; else None
@dataclass(frozen=True)
class Situation:
    person_id: str
    budget: int                   # ask_budget()
    body: int; capability: Mapping; pursuits: Mapping; stance: tuple; conviction: Mapping; scar: Mapping
    holdings: tuple               # ((tenure kind, object id), ...): his own live Tenures, through OwnStateReader
    asked: tuple                  # AskedRow per Question in v.questions, in attention_key order
```

`asked` is the season loop's own answer to "what demands this person's attention": the questions
`world_q.questions_for` produced, in the order `attention_key` gave them. It is what the quarantined
design called the Scene Slate, built from the person's ledger and standing occasions, not from a
second generator. `holdings` is empty until `OwnStateReader` answers his own Tenures (CHAR's item 2);
the field ships with the reader.

### 2. `Offer` (`decision/sheet.py`; terms from `decision/choose.py::make_ranker`)

```
@dataclass(frozen=True)
class OfferRow:
    candidate: Candidate          # a deep copy, as today
    occasion: Optional[str]       # the id of the AskedRow question whose referents hold candidate.subject;
                                  # None for a standing candidate (one formed on no referent)
    terms: tuple                  # score_terms' tuple, exactly as the chooser summed it
    odds: Optional[tuple]         # View.odds for this candidate: what he BELIEVES, which may be wrong
    cost: int                     # Scene.cost's unit
@dataclass(frozen=True)
class WithheldRow:
    verb: str; subject: Optional[str]
    unmet: str                    # the own-state conjunct of the row's requires_typed that answered False
@dataclass(frozen=True)
class Offer:
    rows: tuple                   # make_ranker's order
    withheld: tuple               # own-state declines only
```

- `terms` has one source: CHAR's `watch` hook on `make_chooser`. SURF's two floats (`pursuit`,
  `stance`) and CHAR's `DevelopmentSheet.terms` are the same datum; this is its one name.
- `occasion` is derived in the sheet from `candidate.subject` and `v.questions`; it forms nothing and
  ranks nothing `[ASSUMPTION; low; revert: drop the field, the client groups by subject]`.
- `withheld` is the display of CHAR's decline (`opening_set` declining on a conjunct the actor's own
  state answers `False`): the decline returns the conjunct instead of dropping it. **Only own-state
  stems appear.** A requirement the world answers is never predicted to him; it is met as a refusal,
  in the receipt. This is the lawful form of the design set's "locked option, hover shows what is
  needed", and it cannot show a control for a capability the world would have to confirm.
- A candidate that runs against a conviction is **not locked**. It is an ordinary row whose stance
  term is negative; picking it is the act, and the cost is the fold's (`_conviction_crisis`).
- The army verbs are not `OfferRow`s: their command rides the act's payload, which no `Candidate`
  carries (`Fixtures withheld_verbs`). `harness/military_menu.py` is their surface and stays as ruled
  (an engine-side Python API). A later payload-carrying verb family follows the menu's shape: a frozen
  record of legal commands with bounds, the module's vocabulary, and advisories, built host-side for
  the actor's own holdings.

### 3. `receipt` (`harness/play_surface.py`, beside `dispatching_chooser` and `carry_on`)

```
@dataclass(frozen=True)
class ReceiptRow:
    act: str; verb: str; subject: Optional[str]
    kinds: tuple                  # kinds of the Events whose causes[] name the act DIRECTLY, in log order
    degree: Optional[str]
    ending: tuple                 # Event.ending as stamped: per-party for a fight; the margin tuple once SC-P1 lands
    read: tuple                   # ((subject, predicate, value or None), ...) from Event.observed;
                                  # the value is shown only where his own ledger holds a claim on that cell
def receipt(w, act_of, pid, since) -> tuple[ReceiptRow, ...]
```

The law is the one `Claim.doer` already states: "a person always knows his own act, so it leaks
nothing a channel withholds". It is host-side because an `Event` has no actor and the pairing of an
Event to an act is the driver's (`SeasonDriver.act_of`); it is not `explain`, and it walks forward
from his own act, never back from an Event to another's. Three limits keep it from widening: it
returns rows for `pid`'s acts only; it reads `causes[]` at depth one (the fold's verdict on the act,
not its later consequences, which reach him through WITNESS or not at all); and a term the fold read
is shown as the requirement (the arithmetic of his own refused act) with its value withheld unless he
holds it (§C.11: hidden in existence, never in arithmetic). No verb row today needs its actor kept
ignorant of his own band; if one does, it declares `receipt: none` on its row and the reader obeys.

### 4. `account` (`decision/sheet.py`, beside `chronicle`; replaces SURF's `aftermath`)

```
@dataclass(frozen=True)
class AccountRow:
    claim: Claim                  # as held: subject, predicate, value, source, confidence, when, round, chain, doer
    own: bool                     # claim.doer == holder: the echo of his own deed
    prior: Optional[Claim]        # the claim he held on the same (subject, predicate) just before, if he still holds it
    unattributed: bool            # a change he can see (prior differs, or an event-kind deposit) for which
                                  # no claim of his names a doer (no doer, no Seen.who, no deed_doer answer)
def account(p, since: tuple) -> tuple[AccountRow, ...]      # since = (tick, round), questions_for's own key
```

Read from the person's own ledger and nothing else. `claim.teller`, `claim.hops` and `chain[0]` (the
origin) are already derived on `Claim`, so "who told me, at how many removes" needs no new field.
`prior` is how a quantity becomes trackable across periods for a person who holds claims about it,
and only for him. **Another person's reasons are shown exactly here**: as the claims the player's
person holds about that person's deeds, tellings and commitments, with their sources.

### 5. `dossier` (`queries/person_q.py`; the case board)

```
@dataclass(frozen=True)
class DossierRow:
    claim: Optional[Claim]        # FI-05's E1: a belief he holds
    record: Optional[str]         # FI-05's E2: the id of a Record on his live hold
    proof_kind: str               # derived, rosters.yaml: proofs
    support: float                # LedgerReader's support over distinct origins
    against: tuple                # ids of claims of his that the pairing rule marks as disagreeing
def dossier(p, subject) -> tuple[DossierRow, ...]
```

The content rules are FI's and SC's (what an item is, how it is weighed, what contradicts it). GO's
part is that the board is a reading of what the person holds, that a citation is a pick of row ids
(`Act.payload["cites"]`, a choice-sourced operand), and that nothing on the board is true because it
is on the board. Until FI-05 lands, `dossier` is `chronicle`'s `beliefs` filtered to one subject.

### 6. The scene pair, for a scene the driver suspends

Five rules, read off the one built instance (`PlayHost`, `CombatTurnView`, `modules/combat/fight.py`):

1. **The view** is a frozen record built by the module entry before any draw of that turn. It carries
   the deciding party's own side in full and of the other side only what the module's own rule lets a
   party see. Never a module object, never `World`.
2. **The choices** are a closed tuple the module owns and the exporter writes
   (`engine/engine_params/battle_orders.json` is the precedent; `TURN_CHOICES` and PC's `APPROACHES`
   join `combat_engine_v1.json`). `game/` holds no list of legal choices.
3. **No decider is the person's own policy**, never a module constant. `decide=None` asks the decider
   the chooser supplies for that person (PC §4); until one exists it is the module default, and that
   interim is a named gap, because a played person who declines to play must fight as an NPC of his
   sheet would.
4. **The outcome carries `trace`**: a tuple of typed steps, at least one per turn, each naming the
   choice each party made and the state both could see after it. The trace is what a played party is
   shown between turns and what a watching party is shown instead of deciding. It is the object GATE
   §3's `trace_digest` pins.
5. **The mode is recorded nowhere** (`PlayHost`'s own rule): no Event, id purpose or carrier names it.

Which subsystem uses which:

| subsystem | kind of play | choice surface | consequence surface |
|---|---|---|---|
| the person's season, governance, settlement | loop-played | `Offer` | `receipt`, `account` |
| contest (hearing, petition, debate) | loop-played | `Offer` (`speak` and its siblings; `cites` from the `dossier`) | `receipt` (SC-P1's ending), `account` |
| inquiry | loop-played | `Offer` (the inquiry verbs) | `receipt` (the finding and its terms), `dossier` |
| duel, and a duel round on a grid | scene-suspended | `CombatTurnView` + `APPROACHES` | the round's `trace`; `receipt` after |
| field | both | before: `MilitaryMenu` and the order of battle; during: MB's `FieldPhaseView` + `PhaseOrder` | the phase `trace`/`report`; `receipt` after |

### 7. What triggers presentation

`04` §C.12 rejection 3 allows one signal per appended Event at the `game/` boundary. **A player-facing
presentation is triggered by an `AccountRow` or a `ReceiptRow` of the seated person, never by a log
Event.** The log is the whole world; the two readings are what he is entitled to. A port that hangs a
cutscene on `scar.taken` in the log shows the player a scar he has not heard of.

### 8. The transcript: one instrument for every playable scenario

`python -m engine.season.harness.play_surface --seed S --person P --seasons K [--scenario NAME]`
seats `P` with `take_ranked`, and per deliberation prints the `Situation` (asked rows), the `Offer`
(rows with terms and odds, withheld rows), the pick, then the `receipt` and `account` since the last
deliberation, and for a suspended scene the `trace`. Every lane's standalone scenario (the valley,
the governance spine, the hearing, the inquiry, the duel, the field) is printed by this runner
instead of by its own `sheet(w)`; a lane's world-reading summary stays what it is, an instrument for
a developer, and is not the player's surface.

## The gate (execution artifacts)

1. The transcript's `content_hash` equals the plain run's at seeds 0–2 (the control exists for the
   sheet today: `5ab73af2…`, seed 0, one season).
2. For one deliberation, the order of `Offer.rows` equals `make_ranker`'s and each row's `terms`
   equals what the `watch` hook reported; a planted claim that changes his belief about one subject
   changes `odds` for acts on that subject only.
3. Every act the seated person resolved has a `ReceiptRow` with at least one kind; a planted act of
   another person yields none. A planted refusal on a world fact he holds no claim on prints the
   conjunct with value `None`; with the claim planted, the value.
4. `account` after a season: a planted told claim reads `own=False` with `claim.teller` set; two
   claims on one cell give the later row a `prior`; an event-kind deposit with no doer reads
   `unattributed=True`.
5. A withheld row appears for a verb whose own-state conjunct is false and for no verb whose
   requirement is the world's; `decision/`'s path scan stays green.

## The falsifier

A value in `ReceiptRow.read` that the person does not hold. An `OfferRow.terms` differing from the
chooser's sum. A `WithheldRow` naming a world-side requirement. A transcript whose hash differs from
the plain run. A scenario that prints through a `World`-reading sheet and calls it the player's view.

## NERS reading (§0.06; E last)

- **N.** Cut `receipt` and a player's act has no visible result unless a witness channel happens to
  carry one (two of fifteen did not). Cut `occasion` and the question-specific acts are lost among
  thirty standing ones. Cut the single protocol and each subsystem is a different game to learn.
  Holds bottom-up (person to player), laterally (six subsystems, one surface) and across scales (the
  same `receipt` closes a duel, a field and a speech).
- **R.** *Impact on the world* is the receipt and the account; *narrative hooks without the player*
  reach him as account rows with their sources, false ones included; *completeness*: a refusal has a
  reason, and an unattributed change says so.
- **S.** *Pauses correctly*: one suspension form, with the played, watched and automated fidelities as
  one call. *Consistent methodology*: one score, shown and used; one pairing of act to outcome.
- **E.** Scored against N and R: five readers and one record split, replacing six proposed shapes and
  three harness re-scorings. A player reads four things in every subsystem: what is asked, what he
  may do, what came of it, what he has heard.

## Cost class

§1, §2, §4: small build (after CHAR's hook and decline). §3, §8: small build. §5: small build after
FI-05. §6: design-first in each module lane; the rules here are an edit to each lane's proposal. §7:
a rule for the other repository, stated here because the oracle's readings are what it binds to.
