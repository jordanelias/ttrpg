# INST-SYN-B — the deed ledger: founders who did things, paper that recites them, keepers who can tell or withhold, and standing that passes down the seat

Reconciled: 2026-11-12, U5d closure — folded **A-17 / A-18**, **A-19** and the land rulings. The Status line's "canon amendment … Jordan's" is answered: the south fought, ranked third and was relegated despite it (A-17), so the seeding ships on option A (Varfell's founding deed held realm-wide at the third confidence, A-18) and the drafted wording A1 to A4 (audit §4.6) is the canon text owed; a canon sentence changes only by that ruling, and no suite lane applies it. The seeded counts keep their `[ASSUMPTION; Jordan to correct]` (only the order is ruled). When the royal line fails the crown goes by the deed race (A-19): this ledger is what sets each claimant's odds, with the founding order a head start. `took_by_force` gains a live producer: a victor who seizes a place takes its seats with it (A-58, A-66; `U5d_FA_land_and_seats_pass_on_a_won_march.md`), and the `rung.seized` deed that names those seats is the dominance deed this helper reads, so a conqueror's standing in the seat starts from his own deeds and nothing before him passes. An occupier who does not seize holds no seat and enters no chain.

## Status: PROPOSED — the canon amendment it drafts is NOT APPLIED and is Jordan's; the seeded counts are `[ASSUMPTION; Jordan to correct]`

Source: Jordan, 2026-11-12, as `INSTITUTIONS_BRIEF.md` records it: *"current kingdom royalty is because of
nobility by deed/achievement"*; *"Royalty by noble conquest, i.e. the first king had the greatest
accomplishment in the secession war, followed by the first Duke of Hafenmark and the first Duke of
Varfell."* `audits/15_INSTITUTIONS_SYNTHESIS.md` §2.1 (X-03 to X-08), §4. Reconciles
`15_INSTITUTIONS_BYZANTINE_A` (edits 1, 2, 5, 6), `15_INSTITUTIONS_PAPACY_C` (edit 1, §1), and
`15_INSTITUTIONS_COLONIAL_D` (edits 1 to 3) into one design; each carries a `Reconciled:` line. Composes
on CR-36 (the `resolution` Record and its disposal site), `12_ARCS_case_on_the_realm.md` (prehistory
through the fold), `14_VERBS_BINDING_C` edit 9 (a person's own reading of who holds a seat),
`14_VERBS_SOCIAL2_B_a_word_with_content.md` (telling what a held document says), SC's evidence weight
(`05_SC_evidence_and_rebuttal_B.md`). Ratifies nothing.

## What it changes in `engine/season/` at runtime

1. `person_q.legitimacy` gains one term, the chain: a discounted share of what the estimating person
   still holds of the deeds of the seat's prior lawful holders. At `presumption_gain` 0 (the shipped
   value of the landing commit) it is today's function exactly.
2. A built realm holds three dead founders, their Secession deeds as Events, and four seeded Records: two
   in the Church's archive, two in the Crown's chancery. A declared build-hash mover.
3. A Record may carry `recites`; a cited certificate weighs in SC's `evidence` term by the recited deeds
   left standing.
4. `off_duchess_hafenmark` is filled by inheritance through a title nobody holds at build.

No legitimacy number is stored. No rank is stored. No title type, tenure kind or verb is added.

## The problem (evidence)

- The fixed point has no carrier. At `build_realm(0)`: Records `{'works': 2}`; 13 persons hold a stance
  row toward the King and none toward either duke, mean regard 0.720, 0.000, 0.000
  (`15_INSTITUTIONS_BYZANTINE.md` E-1); no founder is a person and no Secession deed is an Event
  (`15_INSTITUTIONS_COLONIAL.md` §5.2 row 5).
- `queries/person_q.py::legitimacy` (`:537`, opened this session) is `stance_toward(p, holder)` plus
  `deed_term` over the holder's **own** deeds among `p`'s recent claims. An heir who has done nothing reads
  as stance alone, and canon says of Almud exactly that he "has not personally earned the deed-claim —
  inherits the presumption his father created" (`canon/03_canonical_timeline.md:117`, opened).
- Claims fade: 34,837 `claim.decayed` Events in three seasons at seed 0 (`15_INSTITUTIONS_PAPACY.md`
  E-1). Nothing in the world remembers on purpose.
- The four lanes carried the same fact four ways (audit §1, last row; X-03, X-05, X-06), with three
  different numbers for one order (1.0 / 0.8 / 0.6; 5 / 3 / 2; 3 / 2 / 1) and two functions for one
  quantity.

## The resolution, decided

**The founders are persons who did deeds; the deeds are Events; what survives of them is paper in two
institutions' keeping and memory in ledgers; standing is each person's own reading, and it passes down
the seat at a discount.** Ladder: step 3 (the brief: "extend it; do not invent a parallel"; canon
`:78-92`, `:145`), step 4 (ARCS §6 row 16 for prehistory; CR-36 for the hearing-made Record;
`off_king`'s IN-61 shape for Hafenmark), step 5 (one function for one quantity).

## Exact edits, by owner

### 1. `engine/season/queries/person_q.py::legitimacy`

Signature gains `seat: Optional[str] = None, fx=None`. After the existing sum:

```python
    g = float(fx.get("presumption_gain")) if (seat is not None and fx is not None) else 0.0
    if g:
        axis_w = projected_axes(p, scar_shift)
        weight, successor = g, holder
        for prior in prior_holders(p.ledger, seat, holder):      # newest first; p's own reading
            if took_by_force(p.ledger, successor, seat):         # p believes `successor` seized the seat:
                break                                            #   nothing from before him passes
            for c in attributed_deeds(p.ledger, prior):          # NOT windowed: age is the claim's own fade
                total += weight * deed_term(p, axis_w, c)
            weight, successor = weight * g, prior
```

- `prior_holders(ledger, seat, holder)`: the persons whose `hold` on `seat` closed before `holder`'s
  opened, in `p`'s own `tenure.opened` / `tenure.closed` claims naming the seat, newest first. It is the
  same reading `14_VERBS_BINDING_C` edit 9 (`seat_belief_declines`) and the narrative lane's
  believed-holder need; one helper, beside `attributed_deeds`. `[UNVERIFIED]` that a `tenure.closed`
  claim's subject names both the person and the seat for a `hold` (`20_NARRATIVE_CHURN.md` F-NARR-02
  reads `epistemic.claim_subjects` as doing so for a `hold` edge and for no other kind).
- `took_by_force(ledger, person, seat)`: `p` holds a `standing_routes.kinds.dominance` deed attributed to
  `person` whose subject is `seat` or its rung (`15_INSTITUTIONS_BYZANTINE_A` edit 6's helper, applied
  at each link and not only at the present holder).
- Person-side, no World (AX-2). The two existing callers pass no `seat` and are unchanged.
- `person_q.accomplishment` (`15_INSTITUTIONS_COLONIAL_D` edit 1) is not added. Its two readers
  (`world_q.standing_crossed`; `world_q.reception` where the subject of the act is a seat) call
  `legitimacy` with the seat.
- `data/fixtures.py: presumption_gain`: ships 0; proposed 0.5; sweep {0, 0.5, 0.75, 1.0}; NUMBER row,
  graded `assumption`.

### 2. Prehistory: three founders and their deeds

**`engine/season/rosters.yaml: prehistory`** (new; the owner of what happened in the realm before tick
0; `12_ARCS_case_on_the_realm.md`'s row shape, for the realm base):

```yaml
prehistory:
  source: "Jordan 2026-11-12 (the order of accomplishment); canon/03_canonical_timeline.md:78-90"
  note: >-
    ONLY THE ORDER IS JORDAN'S. The counts (3, 2, 1) carry the order and nothing else; the deed kind
    (`field.won`) is [ASSUMPTION; medium; Jordan to correct]: canon says "wartime deeds" and no more.
  founders:
    off_king:              {case: "<new registry id>"}     # the first Almqvist
    off_duchess_hafenmark: {case: "<new registry id>"}     # the first Duke of Hafenmark
    off_duke_varfell:      {case: "<new registry id>"}     # the first Duke of Varfell
  deeds:
    - {id: deed_secession_k1, seat: off_king,              kind: field.won}
    - {id: deed_secession_k2, seat: off_king,              kind: field.won}
    - {id: deed_secession_k3, seat: off_king,              kind: field.won}
    - {id: deed_secession_h1, seat: off_duchess_hafenmark, kind: field.won}
    - {id: deed_secession_h2, seat: off_duchess_hafenmark, kind: field.won}
    - {id: deed_secession_v1, seat: off_duke_varfell,      kind: field.won}
```

**`references/npc_registry.yaml`**: three rows, `status: proposed`, ids from
`references/id_reservations.yaml` at landing, each dead before tick 0. No name is proposed for the two
first Dukes; canon names none.

**`engine/season/harness/populated.py::build_realm`**, a prehistory block before tick 0: for each
founder, a `hold` on his seat opened and closed; for each `deeds` row, an Event of its kind with the
founder as doer, placed at the realm rung, written through the gate; the first Almqvist's death a
`person.died` with no doer (canon `:116`). The present holders' holds open after their founders' close,
so `prior_holders` reads one step for each seat `[ASSUMPTION; intermediate holders, if Jordan names any,
are further rows and lengthen the chain]`.

**How the cast comes to hold them.** By the fold's own deposits and no constructed Claim (ARCS §6 row
16): the Events are witnessed at their place by the persons the kind's reach admits. `[UNVERIFIED]` what
reach `field.won` carries today and under CR-29's map; the requirement this file states is that **at
build every cast person under the realm root holds a told claim of each seeded deed and of each founder's
closed hold**, because the founding is the one story the whole realm was raised on; from tick 1 those
claims fade like any other. If the kind's reach is narrower than the realm, the block adds one `tell` per
keeper per deed-set, folded under the pinned roll (the fixture style's rule 5), and the reading in gate 2
reports who was reached instead of asserting everyone was.

### 3. `engine/season/instruments.yaml: seeded` — four rows

```yaml
seeded:
  - id:      ins_containment_charter
    kind:    dispensation
    form:    immunity
    via:     off_king
    held_at: off_cardinal_temperance
    to:      ["NPC-021"]                         # the Confessor
    at:      {territory: "T9"}
    source:  "canon/03_canonical_timeline.md:58, :104 (the containment grant, preserved and expanded at the settlement)"
  - id:      ins_consecration_first_king
    kind:    resolution
    via:     off_confessor
    held_at: off_cardinal_temperance
    to:      []
    recites: {for: off_king, deeds: [deed_secession_k1, deed_secession_k2, deed_secession_k3]}
    source:  "canon/03_canonical_timeline.md:82 (the Church consecrates the first king)"
  - id:      ins_settlement_hafenmark
    kind:    dispensation
    form:    homage
    via:     off_king
    held_at: off_parliamentary_clerk
    to:      ["NPC-050"]
    recites: {for: off_duchess_hafenmark, deeds: [deed_secession_h1, deed_secession_h2]}
    source:  "canon/03_canonical_timeline.md:88-90; cases/exercises/NPC-008.yaml (custody of the sole surviving record of the settlement's terms)"
  - id:      ins_settlement_varfell
    kind:    dispensation
    form:    homage
    via:     off_king
    held_at: off_parliamentary_clerk
    to:      ["NPC-052"]
    recites: {for: off_duke_varfell, deeds: [deed_secession_v1]}
    source:  "canon/03_canonical_timeline.md:88; Jordan 2026-11-12"
```

- The two `homage` rows are the instruments the built oaths of NPC-050 and NPC-052 to `off_king` are
  held under (`15_INSTITUTIONS_COLONIAL_D` edit 3's purpose). The `obligees:` list keeps bare ids; the
  mapping form `{case, form}` is not added, because the instrument and its parties are already stated
  here. The Grand Master's oath has no instrument.
- **No house holds its own paper** (`15_INSTITUTIONS_PAPACY_C`'s falsifier, kept and widened to the
  chancery). The parties hold content claims, which is what `dues` and `kept` read.
- `ins_consecration_first_king` needs `resolution` in `record_kinds`. If CR-36 has not landed, this
  proposal lands the roster row alone (kind and keys), and CR-36 lands its disposal site.

### 4. `recites`, and what a certificate weighs

- Content key `recites: {for, deeds}` on `resolution` and on a `dispensation` whose form says `recites:
  true` (`15_INSTITUTIONS_SYNTHESIS_A` edits 1 and 2). In play the list is written by the act that mints
  the Record: `determine` under a `disposes: Record` row writes the cited deed claims left standing at
  Overwhelming and Success and the first half of them, in cited order, at Partial
  (`15_INSTITUTIONS_PAPACY_C` §2's bands, with a list in place of `attests: n`); `issue` and `covenant`
  of a reciting form write the deed claims the act cites.
- **Request to SC's evidence owner** (`05_SC_evidence_and_rebuttal_B.md`; not edited), in that file's
  own terms: citing a Record that carries `recites` files **one item per recited deed**, each the cell
  `(doer, kind, True)` at a Record's weight (1) and with the certifying act's seat as its origin, in place
  of the citer's own told claim of that deed at its hop-discounted weight. That is all a certificate is in
  a hearing: it lets old deeds be put before a room at full weight. Each item is answerable as any item
  is; an impeachment of the paper (a held `record.forged` claim) that draws Overwhelming strikes every
  item of its origin, which is the whole certificate. It is admissible for the side whose petition names
  the same seat or person. PAP-C's requests ("a cited `resolution`'s weight is its `terms.attests`") are
  replaced by this.
- **Commemoration needs no code.** A seat-holder who holds a certificate holds its content claims and may
  `tell` them (`14_VERBS_SOCIAL2_B`); hearers receive told deed claims with the founder as doer, weighed
  by their regard for the teller; those claims are what the chain reads. The keeper chooses, through the
  one chooser, whom to tell and of whom.

### 5. Dignities

`15_INSTITUTIONS_BYZANTINE_A` edits 3 and 7 stand (six vacant dignity rows; a `confer` on one requires
the conferee's oath and a cited deed, and tells the deed on success), with the row's draw the BINDING
lane's (audit X-23) and no `roll` beside them. A dignity leaves no paper: it is a `hold`, it ends with
its holder, and it works by what it told.

### 6. Hafenmark's seat can pass

`15_INSTITUTIONS_COLONIAL_D` edit 4, unchanged: `off_duchess_hafenmark.conferral: null → inheritance`;
`rosters.yaml: successions` gains `off_duchess_hafenmark: off_heir_hafenmark`; a title row
`off_heir_hafenmark`, vacant at build. `[ASSUMPTION; medium; Jordan to correct; revert: the three edits
together]`. `[UNVERIFIED]` that the loader admits a seat row with `holder: null` (three family files
raise the same question; the first of them to land settles it for all).

### 7. Canon

Not edited. The amendment text is drafted in the audit, §4.6 (A1 to A4), under the two readings of §10
item 1.

## Gate (execution artifacts)

`PYTHONHASHSEED=0` throughout.

1. **Control.** `presumption_gain` 0, `prehistory` and `seeded` empty: `build_realm(0)` hash equals the
   pre-item hash; `legitimacy` returns today's value for every (person, holder) pair of the cast.
2. **The order, per observer.** After edits 1 to 3 at `presumption_gain` 0.5: the probe prints, per cast
   person, how he orders the three holders by `legitimacy(p, holder, seat)`. Pass: among persons holding
   claims of all six seeded deeds, a majority order them king, Hafenmark, Varfell, **and at least one
   does not** (unanimity would mean pursuits are not read). Planted: swap the Hafenmark and Varfell
   counts; the majority ordering swaps.
3. **The chain.** Hand-built: an heir whose predecessor `p` knows reads own + 0.5 × the predecessor's;
   one whose predecessor `p` has never heard of reads own; a third holder reads 0.25 of the founder; a
   holder `p` believes took the seat by force reads own only, and so does everyone after him for what
   came before him.
4. **Memory fades and telling restores it.** Realm, seeds 0 to 4, eight seasons, two arms: the keepers'
   `tell` of certificate content withheld (through `Fixtures withheld_verbs` scoped by a planted
   question, never by a person's id) and not withheld. Reported per season: the mean chain term for the
   three holders. Pass: it falls in both arms and falls further in the withheld arm at some season. A
   reading over five trajectories; no rate is claimed.
5. **The paper is odds.** PAP-C's planted hearing, unchanged in shape: a consecration petition with and
   without the predecessor's certificate cited; exact odds printed from the module's distribution; the
   cited arm is better; all four bands occur in both arms over 200 seeds; a rival's contrary Record cited
   against it shrinks the advantage.

## Falsifier

- The order encoded twice: any reader that takes the order from somewhere other than the seeded deeds
  (a `founding.order` key, an `attests` number).
- `prior_holders` read from the world's Tenures instead of `p`'s claims: gate 3's "never heard of" arm
  reddens.
- A build in which a house's head holds the paper that recites his house's deeds.
- A `legitimacy` that differs from today's at `presumption_gain` 0.
- A certificate that opens or gates a `hold`.

## What it does not do

It ranks nobody. It makes no one king. It does not make the Church tell or the clerk keep: each is a
person's choice through the one chooser. It gives a dead founder's deeds to no living person: they are
the founder's, and what the living holder gets is a discounted reading of them in other people's eyes.
It does not decide who credits the south (§10 item 1 of the audit).

## NERS reading

- **N.** From above: a king's authority is what people still remember his house did, and two bodies hold
  the paper that can remind them. From below: a villager who has heard only of the duke's founder rates
  the duke above the king. Laterally: three houses are compared by one function and disagreeing ledgers.
  Diagonally: a clerk's custody and a Cardinal's sermon move a throne's odds. Remove it and every heir is
  a nobody, deed-monarchy is a sentence in a canon file, and neither Church nor chancery holds anything a
  ruler needs.
- **R.** A player wins rank by deeds and then must get them written, kept and told; can steal, forge or
  burn a certificate; can be refused consecration. With no player the founders fade at different rates
  in different places and a disputed succession turns on who still remembers what. Complete at the
  extremes: unknown predecessor, own deeds only; no deeds, stance alone; no paper, the hearing runs on
  testimony.
- **S.** One function, `deed_term`'s scoring, the existing fade, the existing mint, SC's evidence term.
  The chain replaces a second function, a claim class with a seat as its subject and a confidence table.
- **E, last.** One term in one function, one roster block, four seeded rows, one content key. A player
  can say it in a sentence: *deeds must be seen, or written and kept and told; and what your predecessors
  did is worth half what you do.*

## Cost class

Small build (the chain and its helper; the prehistory block; the seeded pass). The seeding is a declared
mover with re-pins. Edit 6 is content in FA's file.
