# GO — the player-surface contract: what the oracle types so that the port only renders

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-21) — §4 only. The write-matrix rows already declare `scar.taken` on `(Person, scar)` and `conviction.moved` on `(Person, conviction)`; no row "gains" a kind and `conviction.folded` is not created (`17_CENSUS_REST_3_corrections.md` C-5). The one edit §4 asks to be "one edit" is split between two carriers and made once each: `scar.taken` is passed at `_scar_witnesses` by `16_PESSIMIST_CORE_the_record_holds_what_changed.md` edit 2, landing after `02_CHAR_scar_cap_and_regard_unit.md`'s cap (883 scar writes in three seasons at seed 0 otherwise become 883 Events); `conviction.moved` is emitted, witnessed, by `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` item 4 (Jordan's answer A-24). GO's own closure owns the rest of this file.

Reconciled: 2026-11-12, U5d closure — superseded by `11_GO_player_surface_contract_B.md` (the addendum's R50–R57). Nothing here is to be built from; the rulings A-48, A-49 and A-9 are folded there.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.4 SURF row and §7 (SUPERSEDED by `_B`, **except §2 `explain`, restated nowhere else and live**: the status line now says so; the other sections stand as the superseded record and are not an instruction); `U1_OWNERS_AND_VOCABULARY.md` D-U1-11n is not needed here (this file has no `receipt`); `R1_READ.md` §2 row A-30 (the chooser table's draw row loses "replayed in parity"); §2's argument typed `PersonInterior` (`U5a_CORE_owed_edits.md` §E item 1, B03), replacing the `Person` assumption; test 9 for §2 only (tests, lands-it, tier). `U3_DEPENDENCY_ORDER.md` B34.

**Depends on (§2):** `U5a_CORE_owed_edits.md` §E item 1 (B03: the frozen `PersonInterior`). **Lands in batch:** B34 (`B34-go-surface`), with `11_GO_player_surface_contract_B.md`.

## Status: SUPERSEDED by `11_GO_player_surface_contract_B.md`, except §2 (`explain`), which is live and lands in B34

Carries audit findings F-GO-07 and F-GO-08, and the audit's §13 and §14 (`audits/11_GO_audit.md`).
Lane: GO, IN (the readers live in `engine/season/decision/` and `queries/person_q.py`, which are IN's
and CHAR's files; GO states the interface the port needs). The NPC and chooser intent it relies on is
the CHAR lane's to state (`audits/02_CHAR_audit.md`); this proposal cites it and restates none of it.

## What it changes in `engine/season/` at runtime

Nothing in the automated run: every addition is a person-side reader that writes nothing, and the
chooser is re-expressed over one of them with the hash EQUAL (the control below). A played run gains
three readings it lacked: why a candidate ranks, what the person believes the odds are, and what his
acts did as he came to know it.

## The problem, with evidence

The oracle types the player's surface in `engine/season/decision/sheet.py`, and it works: seated at
seed 0 for one season, `development_space` with `take_ranked` reproduces the automated hash
(`5ab73af2…`), and a reversed pick moves it (`0cddf258…`, 749 → 739 folded acts; 821 attempted at the plain run, U4 F-02). What it shows:

- `DevelopmentSheet.candidates`: 22 and 32 candidates at the two deliberations sampled. A `Candidate`
  carries `verb`, `subject`, `operands`. No term, no odds, no cost.
- `Chronicle`: the person's ledger as held (119 claims, 49 beliefs), `conviction`, `scar`, as present
  values; "no field records when, or by whose act, a count rose" (`sheet.py:183-186`).

What is absent (each a grep or a read, run):

- `score_terms(p, c, fx, memo, odds)` (`decision/choose.py:193`) returns the two numbers the chooser sums;
  no sheet carries them. A port wanting to show "why this is first" would redo the arithmetic in
  GDScript: a second owner of the score.
- `View.odds` exists and "closes over the World" by CONVENTION (`sheet.py:40-41`); nothing packages the
  believed odds of a candidate for display.
- `explain(p : PersonInterior, v : Value) -> Derivation`, ratified in `04` §C.11 (`:871`), does not exist
  (`grep -rnE "def explain|Derivation" engine modules` → 0).
- Nothing relates an act to what the actor then learned. The seated person's 15 Events reach him as
  `claim.deposited` rows among 119.
- `harness/chronicle.py` reads the whole log and is an observer outside the simulation, by its own head.
- `corpus_run` prints `WAITS-ON-PLAYER 16 cases name a player the engine does not supply`.

## The resolution, decided

Ladder step 3 (§C.11 is ratified and states the signature and its limit) and step 4 (`sheet.py`'s own
rule: a space "ranks and selects; it never forms", copies not references, no `World`). **The port
renders typed readings; it computes none.** Four readers, all under `decision/` or `person_q`, all
taking no `World` (the path scan in `tests/test_season_shape.py` already covers `decision/`).

### 1. The offer carries its terms (`decision/sheet.py`, extending `DevelopmentSheet`)

```
@dataclass(frozen=True)
class OfferRow:
    candidate: Candidate          # a deep copy, as today
    pursuit: float                # score_terms(...)[0]
    stance: float                 # score_terms(...)[1]
    odds: Optional[tuple]         # the believed band shares View.odds gives for this candidate, or None
    cost: int                     # the interaction slots it takes (Scene.cost's unit)
```

`DevelopmentSheet.candidates: tuple[Candidate]` becomes `offer: tuple[OfferRow]`, in `make_ranker`'s
order. `make_ranker` already computes the score once per candidate (`choose.py:556-574`); it returns the
terms beside the order instead of discarding them, so **the chooser and the sheet read one computation**.
`OfferRow.odds` is the person's belief (it comes from his `View`), so it may be wrong, and two persons
holding different claims about one subject see different odds for one act.

### 2. `explain` (`queries/person_q.py`), as §C.11 states it

```
def explain(p: PersonInterior, v: Value) -> Derivation      # no World; no walk of causes[] -> Act.actor
@dataclass(frozen=True)
class Derivation:
    value: Value
    terms: tuple          # (claim_id, source, confidence, when, contribution) per own Claim that fed it
    unattributed: bool    # True where the value moved and no claim of his names an author
```

First `Value`s, in the order a player meets them: an `OfferRow`'s `pursuit` and `stance`; a belief the
chronicle shows; the person's own `body` and `stores` readings. *(W3-1.)* The argument is the frozen
`PersonInterior` that `U5a_CORE_owed_edits.md` §E item 1 builds in `state/carriers.py` (B03, before this
batch); the `Person` interim is withdrawn.

**Build (W3-1, §2 only; the live section).** Order: (1) write `tests/valoria/test_explain.py` with
`test_explain_takes_no_world` (a signature test, as `choose`'s: `inspect.signature(person_q.explain)` has
exactly the parameters `p`, `v`, and `p`'s annotation is `PersonInterior`) and
`test_a_fact_held_by_no_claim_appears_in_no_derivation` (plant a `World` fact his ledger holds no claim of;
expect it in no `Derivation.terms`); both fail first (`explain` does not exist). (2) Add `Derivation` and
`explain` to `engine/season/queries/person_q.py`, reading only `p`'s own ledger. (3) Gate: both tests pass,
and the realm hash at seed 0, one season is EQUAL (a reader that writes nothing). Falsifier: a `Derivation`
naming an actor the person holds no claim about fails the second test; control: the EQUAL hash. Hash
movers: none. Lands it: the GO lane's B34 session (IN reviews `person_q`); `sonnet`, small build.

### 3. The aftermath (`decision/sheet.py`, beside `chronicle`)

```
def aftermath(p: Person, since: int) -> tuple[AftermathRow, ...]
@dataclass(frozen=True)
class AftermathRow:
    own_act: Optional[str]        # the act id of his that the claim's chain names, else None
    claim: Claim                  # as held: subject, predicate, value, source, confidence, when
    unattributed: bool
```

Read from the person's own ledger: the claims with `when >= since`, grouped by whether `Claim.chain` or
`Claim.doer` names one of his own act ids (both fields exist on `Claim`). It shows what he *learned*
his act did, which may be less than what it did. **It also gives an NPC's reasons their only lawful
display**: a player sees why another person acted exactly to the extent his own ledger holds claims
about it (`told_by`, `seen`), never from the other's interior.

### 4. Scars and crises get an Event at their writer (IN's edit, named here because the surface needs it)

`loop/resolve.py::_scar_witnesses` and `_conviction_crisis` call `World.write` without `emits`
(`sheet.py:27-33`), so no ledger can ever hold when a person changed. The row's `emits:` gains
`scar.taken` / `conviction.folded` for the person himself. A declared mover (new Events). CHAR's
F-CHAR-03 and F-CHAR-04 bear on the same writers; the two lanes' edits must be one edit.

### 5. The seat is any person; "a player" is not a kind of actor

For the 16 `WAITS-ON-PLAYER` cases and the 53 case needs that name a player: the engine has one agent
type and two sources of choice (`04` §C.11: "for a player character the player IS the decision
procedure"). A need of the form "a player must be able to X" is met when **X is in the offer of a
person so placed**. `harness/corpus_run.py`'s `WAITS-ON-PLAYER` class is re-read as `OFFER-CONTAINS`:
for a case entry naming a player, seat the named role's person and assert that his
`DevelopmentSheet.offer` holds the verb on the subject the need names. No scripted player is introduced;
a headless player who "plays the arc" would be scripting drift.

### 6. Scenes are hosted through one typed decider, as the duel already is

A registered module becomes playable in the port when its entry takes a decider and hands it a typed
turn view, and not otherwise (`queries/inputs.py::PlayHost`, `CombatTurnView`; `loop/driver.py:434-441`;
`seam/wrappers/combat.py:395`). The port hosts a module's scene **only** through that call-out. Mass
battle, the social contest and fieldwork have none; their lanes design the decision points (a typed
`Orders` record and a per-tick view for the field; a move for the contest; a lead for the inquiry).
For a managed battle the port then shows four things, each a typed reading the module returns: the
orders in force and the vocabulary to change them (`battle_orders.json`); the field per tick; the
intervention point (the decider's call); and the after-action reading (`massbattle.py::_person_report`
today: who broke first, each person's survivors; a fuller one is MB's). The three fidelities the tree's
doctrine names (ED-SC-0013: played, witnessed, auto) are then one call: with a decider; without one,
with the per-tick reading and the aftermath shown; without one, with the aftermath alone. No fidelity
has its own formula, so none can be chosen for a better expected outcome.

**Intent read, not loaded.** The quarantined UI set (`valoria_ui_ux_v4_1.md`) is written against phases
and clocks the season loop retired, and nothing here makes code read it. Two of its rules survive as
tests of this proposal: Oath II's third violation test ("Does the UI reveal information the character's
perception cannot render? If yes → FAIL") is what `explain`'s no-`World` signature enforces; and its
Slate dock's cap of twelve visible entries is a presentation rule over the offer (22 and 32 rows in the
sampled deliberations), which the port applies to `OfferRow`s in rank order without dropping any from
the reading.

## What is data and what is code, for the chooser

| | port consumes as data | port re-implements | where it runs |
|---|---|---|---|
| what a person may do | `verb_table.yaml`, `rosters.yaml`, `offices.yaml`, `arrangements.yaml` (GO-09) | `decision/options.py::opening_set` and its operand derivations | in the core, inside DELIBERATE's per-person map, with no `World` |
| what a person wants | `goals.yaml`, `cohorts.yaml`, `npcs.yaml`, the pursuit cells in `verb_table.yaml` | `decision/choose.py::score_terms`, `_sample_order` | same |
| the draw | — | `Draw.u` (the keyed mix, A-30) and the Gumbel transform through `fmath` | same; parity by the `(key, n) → u` vectors |
| the player's pick | — | nothing: `release` packs indices | `game/` supplies the indices through the callback |

The chooser never runs in `game/`. `game/` holds no rule about who may do what.

## The gate (execution artifacts)

1. `development_space` with `take_ranked` reproduces `content_hash` at seeds 0–2 after the `OfferRow`
   change (the control exists today and passes at seed 0: probe E7 in the audit).
2. For one seated person and one deliberation, `sum(row.pursuit + row.stance)` ordering equals
   `make_ranker`'s order; a planted claim that changes his belief about a subject changes `row.odds` for
   acts on that subject and for no other.
3. `explain` takes no `World` (a signature test, as `choose`'s); a fact planted in `World` and held by
   no claim of his appears in no `Derivation`.
4. `aftermath(p, t)` after a season in which he acted returns at least one row with `own_act` set, and a
   row for an effect whose author he cannot name with `unattributed=True`.
5. `corpus_run` prints `OFFER-CONTAINS n of 16`, with the cases that fail naming the verb their person
   was not offered.

## The falsifier

A term on an `OfferRow` that differs from what the chooser summed (two computations): gate 2. A
`Derivation` naming an actor the person holds no claim about: gate 3. An `OFFER-CONTAINS` pass produced
by a harness that hands the person the act: the test must build the offer through `make_ranker` and
nothing else.

## NERS reading (§0.06; E last)

- **N.** Cut the offer's terms and a player's choice is knowable only by taking it; cut `explain` and
  the port owns a second copy of the arithmetic; cut the aftermath and emergence is unread. Holds
  bottom-up (person to player) and horizontally (the played and the automated person share one ranker).
- **R.** *Makes players feel they impact the world* needs the aftermath; *narrative hooks without player
  involvement* reach a player only through his ledger, which is what item 3 reads.
- **S.** *Pauses correctly* is item 6: one suspension form, reused. *Consistent methodology*: one score,
  shown and used.
- **E.** *Intuit complex outcomes from simple choices* is this proposal's whole subject. Scored against
  N and R: four small readers and one field change; no new store, no new verb, no rule in `game/`.

## Cost class

Items 1, 3, 5: small build. Item 2: small build once `PersonInterior` exists, else as assumed. Item 4:
edit, a declared mover. Item 6: design-first in each module's lane.
