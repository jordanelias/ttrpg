# 14 · VERBS · SOCIAL2 · B — a word with content: what is uttered, how a writ is read, to whom a petition goes, which seats a person knows

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-20, C-21, C-30) — §4: `seed_seats_known`, `seat.held` and `seat_holders_known` are not added; the one reader is `person_q.holders_named` and the one build step `seed_seat_news` (`08_FI_01_claim-sourced-referents.md` edits 1 and 6). `construe_obstacle` and `oblige_obstacle` are the roster members `clarity`, `deference` and `establishment` (`U5c_SC_one_obstacle_form.md` §2). `oblige`'s draw against the seat stands (decision register D-31, taken A under Jordan's A-24). §3's petition `to` fans over `holders_named`. §2's construal toward his own interest is Jordan's A-27.

## Status: PROPOSED

Carries `audits/14_VERBS_SOCIAL2.md` §1 (`utter`), §2 (`petition`), §4 (`construe` effect), §9
(`oblige`). Batch S2-B. Depends on S2-A edit 2 for `construe`.

## What this changes in `engine/season/` at runtime

Every computed `utter` mints a Proposition with a subject, a predicate, a value and a mood taken from the
utterer's own ledger or want, where today all are `OUGHT` / `''` / `None`. Every person starts knowing the
seats over his home and who holds them, so `oblige` forms and `petition` is addressed to a seat-holder
instead of to the person it is about. `construe` mints the construer's reading. Three outcomes become
draws: an utterance's uptake by the room, a construal's taking, a seat's admission of an obligee. Each behind a fixture
whose control reproduces today; declared hash movers at the shipped arm in every world.

## The problem (evidence)

- `utter`: probe seeds 0 / 1 / 2, one season: 73 / 69 / 68 Propositions, moods `{OUGHT}`, predicates
  `{''}`, values `{None}`; payload keys `('subject',)` only. `_eff_utter`
  (`loop/effects_information.py:1238-1243`) defaults each missing operand. Content readers that can
  therefore never fire on a computed word: `queries/world_q.py:759` (a judge's vote), `aim_state`
  (`:3760`), `loop/predicates.py:546-549` (`interrogate`'s `HOLDS` charge, which waits for *a `mood`
  source for a computed `utter`*).
- `petition`: `to == subject` 12/12, 14/14, 13/13 (the row's own note: `H-94`'s single referent binds
  both).
- `oblige`: persons with `seats_named` non-empty: 0 before and after the season at three seeds.
  `queries/world_q.py:3146-3161` reads the seats among `ledger_names`; at build no ledger names a seat.
- `construe`: no effect; the row's falsifier (two holders, two readings) unbuilt (`H-36`).

## The resolution, decided

**A person says what he holds, tries to read an order as what he believes, and knows who rules his
home; whether he is believed, whether his reading takes, and whether a seat admits him are draws**
(`AUDIT_BRIEF.md` standing rule: state sets the odds, the draw sets a graded, recoverable outcome). Every
content operand is derived from the actor's own ledger by machinery that exists (`said` on a named
own-ledger conjunct, T4; CR-81's build-time acquaintance deposit), so the chooser and a player pick from
the same Candidates and no free value is invented. Ladder: step 4 (T4's `said`; CR-81's
`seed_acquaintances`), step 5 for the mood table.

## Exact edits, by owner

### §1 `utter`

- `engine/season/verb_table.yaml` `utter`:
  ```yaml
  - verb:        "utter"
    stratum:     social
    eligibility: [own]
    beneficiary: none
    requires:    "the speaker holds a claim on what he speaks of"
    requires_typed: {form: own_ledger, of: subject, conjunct: holds}
    contests:    "a standing"          # against the room: whether he is believed (standing rule)
    writes:
      Overwhelming: ["Proposition.exists"]
      Success:      ["Proposition.exists"]
      Partial:      ["Proposition.exists"]
      Failure:      ["Proposition.exists"]
    emits:
      Overwhelming: ["proposition.uttered", "proposition.believed"]
      Success:      ["proposition.uttered", "proposition.believed"]
      Partial:      ["proposition.uttered"]
      Failure:      ["proposition.uttered"]
    emits_on_refusal: {holds: ["utterance.empty"]}
    grade:       assumption
  ```
  (notes carried forward; `writes_note` gains: *the cell is the `said` the named `holds` conjunct
  carries; the mood is `rosters.yaml: utter_mood_by_source`'s for the question's source; that he said
  it is not in doubt, so every band mints; whether the room believes it is the draw, and only
  `proposition.believed` triggers the told deposit*). The standing rule (`AUDIT_BRIEF.md`, Jordan
  2026-11-12) is why the row is contested: a statement being believed could go either way.
- `rosters.yaml: contest_subsystems.prizes`: `a standing` already routes to the `social_contest`
  provider (`tell`'s); the opponent is the room — `obstacle_default` plus one step per hearer present
  whom the speaker's own ledger holds as believing the contrary (`sigma.py::contest_input`, the speaker's
  own-ledger read, F8) plus the venue modifier. `verb_capability: utter → copying` (new row).
- `engine/season/rosters.yaml`: new closed table `utter_mood_by_source` (keys: `question_sources`
  members, validated at load): `claim_landed: HOLDS`, `need: OUGHT`. A source with no row forms no
  `utter`.
- `engine/season/decision/options.py::_derive_operand`: operand `mood` → the table's value for
  `q.source`. (No branch on the verb: any row naming a `mood` operand gets it.)
- `engine/season/loop/effects_information.py::_eff_utter`: content from `payload["said"]` (`Said`:
  subject, predicate, value) and `payload["mood"]`; the existing defaults kept only for a hand-built act
  with neither (fixture `utter_content: off` is the control: ignore both, today's behaviour).
  Typed in: `Act` with `said: Said | None`, `mood: str | None`. Out: `Change` naming the Proposition.
- `engine/season/loop/witness.py`, the told deposit: fires for an `utter` Event only when its kind
  includes `proposition.believed` (Ov / Su), depositing the told copy on those present with the utterer
  on its chain (FI-05B E-3's channel); at Pa / Fa the ordinary deposit of `proposition.uttered` about the
  speaker is all that lands. `[UNVERIFIED: whether the trigger keys on the payload's `said` or on the
  verb; either way it gains the band-kind condition for this row.]`
- Fixture `utter_content: on | off` in `engine/season/data/fixtures.py`.

### §2 `construe` (after S2-A edit 2)

- `verb_table.yaml` `construe`: `contests: "a proposition"` (against the writ; the standing rule:
  whether a reading takes could go either way); `writes:` `Proposition.exists` at Ov / Su / Pa, `[]` at
  Fa; `emits:` Ov `[terms.construed, construal.credited]`, Su `[terms.construed]`, Pa
  `[terms.construed, terms.distorted]`, Fa `[construal.failed]`; `emits_on_refusal:
  [construal.impossible]` (requirement checks only); `writes_note` replaced: *the construer attempts a
  `HOLDS` reading of the terms' subject and predicate with his own held value; the draw decides whether
  it takes; the writ is unchanged*; `referent_class: Record.dispensation`. `terms.distorted` keeps its
  name and moves to Pa, where witnesses hold the reading as a twist.
- `rosters.yaml: verb_capability`: `construe: "argue"`. Obstacle: `obstacle_default` plus
  `rosters.yaml: construe_obstacle` (new, two keys: `clear_terms` (a terms Proposition with predicate and
  value) +1, `issuer_standing` +1 where the construer holds the issuer above him by `regard`).
- `loop/effects_information.py`: new `_eff_construe(w, a, res) -> Change`, called by the fold at Ov /
  Su / Pa only:
  1. read the writ `w.records[subject]`, its `terms` (a Proposition id via `ABOUT_KEYS["dispensation"]`);
     decline `NO_CHANGE` (→ `construal.impossible`) if no Proposition;
  2. the construer's own value on `(terms.subject, terms.predicate)`: the newest such claim in his own
     ledger (`person_q` `LedgerReader`, the one comparator) — decline if none or equal to `terms.value`;
  3. mint `Proposition(f"prop:{a.id}", "HOLDS", terms.subject, terms.predicate, his_value, w.tick)` and
     `_makers_hold` — the same two lines `_eff_utter` performs, called through a shared
     `_mint_proposition(w, actor, prop)` helper (safe to share: it opens a `hold`, whose literal stays in
     the helper, `_mint_document`'s precedent; `_derive_openers_from_effects` reads `hold` there).
  The receipt names the Proposition, earning the band's kinds. Steps 1–2 are asked again in the
  row's predicate before the draw, so a refused act costs no draw (`_req_interrogate`'s placement).
- `comply` / `evade / defy` (other family): their `own_ledger(subject)` conjunct already reads the
  actor's own claims; no edit is needed for them to see the reading, but their effect's test of
  compliance must read the construer's Proposition where he holds one. Named for the owning lane.

### §3 `petition` (after §4)

- `queries/person_q.py`: new `seat_holders_known(claims) -> tuple[(seat, holder)]`, World-free: the
  `(seat, seat.held, holder)` claims the holder holds (newest per seat).
- `decision/options.py::operand_bags`: for a row whose counterparty operand is `to` and which declares
  `to_from: seat_holders` (new row column, validated by `data/verbs.py`; `petition` alone today), fan
  `to` over the holders of `seat_holders_known(p.ledger)`, minus `p.id` and the subject. Else the
  existing `known_persons` fan. The column names a reader, never a verb.
- `verb_table.yaml` `petition`: `to_from: seat_holders`; `requires_typed_note` gains *`to` is fanned over
  the seat-holders the petitioner knows (`seat_holders_known`); `H-94`'s single referent now binds
  `subject` alone*.
- `rosters.yaml: petition_addressees` is **not** added (the audit floated it): the seats known are the
  seats over the home, which is the addressee rule; a second filter would be a second owner.
- Fixture `petition_addressee: seat_holders | referent` (control `referent`: today).

### §4 Seats known (serves `oblige` and §3)

- `engine/season/harness/populated.py`: new build step `seed_seats_known(w)` beside
  `seed_acquaintances` (CR-81's precedent and its eviction note apply verbatim): for each person, for each
  seat whose purview reaches his home rung (`state/gate.py::purview_reaches`, the one owner), one claim
  `Claim(f"c_seat_{who}_{seat}", who, seat, "seat.held", <holder or None>, 0, "firsthand", conf, "own")`.
  A vacant seat is known as vacant (`None`).
- `rosters.yaml`: `seat.held` added to the claim-kind roster that `ledger_names` and `known_persons` read
  (`known_person_operands` is not widened: a holder becomes known through the value, read only by
  `seat_holders_known`). `[UNVERIFIED: the roster name that admits a build-time predicate; CR-81 used
  `KNOWN_PERSON_CLAIM`.]`
- `loop/witness.py`: a `tenure.opened` / `tenure.closed` on a seat already deposits a claim about the
  seat (`epistemic.claim_subjects`' Tenure expansion, K-25); it additionally carries `seat.held` with the
  new holder, so knowledge of who rules is kept current by the same channel `[UNVERIFIED: the expansion's
  predicate; if it is the event kind, `seat_holders_known` reads that kind instead and no deposit
  changes]`.
- Fixture `seats_known_at_build: home_purview | none` (control `none`).
- `oblige`: `seats_named` now returns the home's seats; `_req_oblige`'s five clauses stay as eligibility.
  **Admission becomes a draw** (the standing rule names *any "binds" effect with no resolution roll*):
  `verb_table.yaml` `oblige` gains `contests: "a standing"` with the seat's live holder as opponent
  (`counterparty: subject` resolves to the seat; `sigma.py::_opposition_of` takes the seat's holder, else
  `obstacle_default` for a vacant seat), obstacle modifiers `rosters.yaml: oblige_obstacle` (new: rank
  gap per rung, the holder's `regard` of the joiner, establishment size per 5 obligees); `writes:`
  `Tenure.since`, `Tenure.term` at Ov / Su / Pa, `[]` at Fa; `emits:` `duty.taken` at Ov / Su,
  `duty.probation` at Pa, `duty.refused` at Fa. `_eff_oblige` opens the edge with `degree=res.degree`
  and, at Pa, half `oblige_term` (the term's one owner, `H-159`, read and halved, no second constant).
  ⚠ Conflict with the ruled `binds_bases: members_by_admission` (*the joiner's own act admits him*):
  named, listed for Jordan (`audits/14_VERBS_SOCIAL2.md` §11.4 item 1); the fiat arm is kept as fixture
  `oblige_admission: fiat` for the ruling's sake.

## Order of landing

§4 → §3 → §1 → §2 (after S2-A edit 2). §1 and §4 are independent.

## Gate (execution artifact)

`build_realm(s)`, s = 0, 1, 2, two seasons, `PYTHONHASHSEED=0`, on-arm against each fixture's control:
- §1: ≥ 90% of computed Propositions carry a non-empty predicate; every `HOLDS` cell equals a claim its
  utterer held at the act tick; ≥ 1 judge vote (`world_q.py:759`) or ≥ 1 `decision.agreement`
  disagreement between two utterances read at one seed.
- §1, the draw: across the three seeds `proposition.believed` is emitted for some utterances and not
  for others (a fraction strictly between 0 and 1); a planted `Failure` mints the Proposition and
  deposits no told copy.
- §4: `oblige` formed > 0 at every seed, attempted ≥ 1; across seeds at least one `duty.taken` or
  `duty.probation` and the obligee in `establishment_of`; a planted `Failure` opens no edge.
- §3: `to == subject` 0; every `to` holds a seat reaching the petition's `from`.
- §2 (hand-built: issuer, writ with `HOLDS` terms, two holders, one believing otherwise): at a planted
  `Success` the two holders hold different readings (the row's falsifier, `H-36`); at a planted
  `Partial` witnesses hold `terms.distorted`; at a planted `Failure` no Proposition is minted;
  `construal.impossible` (no draw) for the holder who agrees. Over seeds 0–9 with the shipped odds, all
  four bands occur.
- Controls: each fixture at its control reproduces the pre-edit hash at the three seeds.

## Falsifiers

- §1: an act whose `said` claim was evicted between formation and fold refuses `utterance.empty`, never
  mints the cell.
- §3: a petitioner with his seat claims deleted forms no petition.
- §4: a person whose home no seat reaches holds no `seat.held` claim.
- §2: a construer whose value equals the terms forms none.

## NERS reading

N: without content the Proposition, the commit, the petition's addressee and the reading of an order are
labels; with it the argument layer (SC-P8's contradiction, FI-05B's citing) has statements to compare,
from every direction (top-down a statement is the unit; bottom-up the carriers are frozen and exist;
lateral `said` already flows on `tell`). R: people hold positions, petition their lords, enter service and
read orders their way with no player present. S: one derivation (`said`), one build step (CR-81's), one
mint helper. E, last: one roster, two readers, one build step, one effect, against four verbs that today
produce nothing a later act reads.

## Cost class

Small build (§1, §3, §4); small build after S2-A (§2).
