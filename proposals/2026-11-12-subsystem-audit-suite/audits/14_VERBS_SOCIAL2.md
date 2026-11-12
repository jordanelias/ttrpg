# VERBS · SOCIAL2 — build-out of the information, evidence and argument rows

## Status: REFERENCE (a verb build-out audit; resolves nothing at runtime, CLAUDE.md §0.05)
Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: 7289ef2 (working tree)

Work order: `VERBS_BRIEF.md`, FAMILY = SOCIAL2. Verbs (rows of `engine/season/verb_table.yaml`, stratum
`social`): `oblige`, `open_case`, `petition`, `construe`, `speak`, `tell`, `interview`, `interrogate`,
`tie / knot`, `utter`. Binding design, cited and not redone: `proposals/08_FI_05_evidence-interface_B.md`
(E-1..E-8, "FI-05B"), `proposals/05_SC_evidence_and_rebuttal.md` (edits 1–6, "SC-P8"),
`proposals/05_SC_playable_hearing_B.md` ("SC-P3B"), `proposals/08_FI_02_rumour-that-travels.md` ("FI-02"),
`proposals/08_FI_06_testimony-names-a-hand.md` ("FI-06"), `proposals/08_FI_08_knots-season-form.md`
("FI-08"), `proposals/08_FI_03_playable-inquiry.md` ("FI-03"), `proposals/05_SC_acquittal.md` ("SC-P6"),
`proposals/12_ARCS_cited_evidence.md`. The exact edits are in the four proposals of §0.4; this file holds
the premise, the state today with its reading, the decided build-out, and the family's order.

## 0. Verdict and reading

### 0.1 Verdict

**One of the ten works as its plain meaning promises in part (`open_case`), seven execute or form and do
not do what the word says, and two never reach the fold (`interrogate`, `tie / knot`).** The family's
common defect is not refusal but emptiness: the verbs that execute most write things nobody can read as
what was said. `utter` executes 68–73 times a season at three seeds and every Proposition it mints is
`OUGHT` with an empty predicate and no value; `petition` files 12–14 a season and every one is addressed
to the person it is about; `interview` executes and, being ungraded, finds nothing; `speak` and `tell`
form on hearers and matters the actor could have known were not there. **The single largest obstacle is
that no act in this family can carry content**: a computed act binds one referent (`H-94`, cited in the
`petition` row's `requires_typed_note`), so a word has a topic and no assertion, a petition a subject and
no addressee, an interview a person and no question. The evidence interface FI-05B and SC-P8 decided
(cited items, the case file, contradiction) is sound and buildable, and it has nothing to consume until
the family's acts carry what was said.

### 0.2 What this is read against

- HEAD `7289ef2`, working tree (one untracked proposal of another lane, not read).
- Instrument readings, all `PYTHONHASHSEED=0`, realm arm, scratchpad
  `runs/VERBS_SOCIAL2/`: `aperture 1 0` (`aperture_1_0.txt`, taken by the Fable lane before the cut-off;
  re-read here), `corpus_run` (`corpus_run.txt`, same), and a read-only state probe
  (`probe_state.py`, written by the Fable lane, which failed on `ModuleNotFoundError` because it ran
  without `PYTHONPATH`; re-run here at seeds 0, 1, 2, one season each: `probe_state_s{0,1,2}_1.txt`).
  One season per seed is a reading of a trajectory, not a rate (CLAUDE.md §0.1 pt 4); nothing below is a
  balance claim.

### 0.3 State today, one line per verb

`elig` = persons eligible at build (seated / unseated); `formed / att / ex / ref` from `aperture 1 0`
(seed 0); "probe" from the three-seed probe.

| verb | elig | formed | att | ex | ref | deciding read of the refusals | probe (seeds 0 / 1 / 2) | verdict |
|---|---|---|---|---|---|---|---|---|
| `utter` | 33/50 | 83 | 73 | 73 | 0 | — | 73 / 69 / 68 Propositions, all `OUGHT`, predicate `''`, value `None` | **executes and asserts nothing** |
| `petition` | 33/50 | 45 | 12 | 12 | 0 | — | `to == subject` 12/12, 14/14, 13/13; 2 carried each seed | **executes; addressed to the wrong person** |
| `open_case` | 8/0 | 8 | 11 | 6 | 5 | `write` 3 (already docketed), `authority` 2 | opened 6 / 8 / 5 | **works in part**; the case file is empty |
| `speak` | 33/50 | 83 | 8 | 1 | 7 | `exists:DocketItem=0` 7 | unheard 7 / 9 / 13; executed 1 / 5 / 4 | **forms on what is not docketed** |
| `tell` | 33/50 | 51 | 20 | 4 | 16 | clause `hearer` 16 | `tell.refused` 20 / 43 / 4; `news.told` 2 / 1 / 0 | **forms on absent hearers** |
| `interview` | 33/50 | 83 | 19 | 5 | 14 | `exists:Person=0` 14 | subjects Person 5/3/5 of 19/8/19; one self-interview (seed 1) | **forms on non-persons; executes and finds nothing** |
| `construe` | 33/50 | 45 | 4 | 0 | 4 | `exists:dispensation=0` 4 | subjects: `faction_sheet`, `cover`, `petition`, `text`; never a writ, though 15 / 10 / 8 exist | **forms on the wrong document; never executes** |
| `oblige` | 33/50 | 0 | 0 | 0 | 0 | — | `seats_named` non-empty for 0 persons, before and after | **unreachable** (nobody is told of a seat) |
| `interrogate` | 8/0 | 0 | 0 | 0 | 0 | — | live `detain` 0 | **unreachable** (no custody exists) |
| `tie / knot` | 33/50 | 83 | 0 | — | — | — | not in `resolvable_verbs()`; live edges 0 | **stub by ruling** (no effect; `H-182`) |

`corpus_run` (143 cases, seed 0): executed `petition`, `speak` (19 degrees: 16 Failure, 3 Partial), `tell`
(158: 120 / 28 / 10), `interview`, `utter`; only refused `construe`; never attempted `interrogate`,
`oblige`, `open_case`. Its *emits and writes nothing* list names `construe`, `interrogate`, `interview`,
`speak` as untagged and `tell` as deposit-only by ruling. Pools: `speak` and `tell` rolled pool 2 for every
actor (no `copying` key held by anyone; `aperture` POOLS ROLLED).

### 0.4 The proposals that carry the edits

| file | verbs | batch |
|---|---|---|
| `proposals/14_VERBS_SOCIAL2_A_formation_on_what_is_known.md` | `speak`, `interview`, `construe`, `tell` (formation), `open_case` (docket) | S2-A |
| `proposals/14_VERBS_SOCIAL2_B_a_word_with_content.md` | `utter`, `construe` (the reading), `petition` (the addressee), `oblige` (seats known) | S2-B |
| `proposals/14_VERBS_SOCIAL2_C_case_question_confession.md` | `open_case` (the charge), `speak` (bands), `interview` (the prompt), `interrogate`, `tell` (bands) | S2-C |
| `proposals/14_VERBS_SOCIAL2_D_tie.md` | `tie / knot` | S2-D |

## 1. `utter`

**1 Premise.** *A person says something in so many words, and what he said is now a fixed statement others
can hold him to.* Links: (a) the speaker has something to say (a belief, a demand, an intention); (b) the
statement carries its content (about whom, what, which way, in which mood: is / ought / will); (c) it is
public to those present; (d) it is immutable and citable; (e) he can be held to it (`commit`), it can be
contradicted, and others can act on it (`covenant`, `issue`, `petition` as terms).

**2 State today.** Row: `own`, `requires: —`, writes `Proposition.exists`, emits `proposition.uttered`, no
refusal, ungraded. Effect `loop/effects_information.py:1214-1249` (`_eff_utter`): mints
`Proposition(pid, mood or "OUGHT", subject or actor, predicate or "", value, tick)` and the utterer's
`hold`. A computed act carries `subject` only (probe: payload keys `('subject',)` on 73/73), so every
Proposition is `OUGHT` / `''` / `None`. Readers of content: `world_q.py:759` (a judge's ambition votes
only when `predicate == disposes`), `aim_state` and `goal_referents` (`world_q.py:3760`, `:3928`, `:4160`),
`_req_interrogate`'s waiting `HOLDS` form (`predicates.py:546-549`). None can be satisfied by a computed
utterance. What does read it: `commit` executes on it (37 / 23 / 23 live commits on a fresh Proposition),
so the only consequence of a word is a vow to nothing. **Verdict: executes and asserts nothing** (links a,
b, e broken; d holds structurally; c holds by WITNESS).

**3 Build-out, decided.** The act carries its content, derived person-side from the question the person
answers, by one rule: *a person says what he holds.*
- **Formation.** On the question's referent as today. The cell is derived, never chosen freely: the row
  gains a NAMED own-ledger conjunct (`holds`), so the Candidate carries `said` — the `Said` (subject,
  predicate, value) `person_q.said_of` picks from the actor's own ledger, exactly as `tell`'s does (T4).
  The mood is derived from the question's source by a new closed table, `rosters.yaml:
  utter_mood_by_source`, the one owner of source → mood: `claim_landed` → `HOLDS` (he voices a belief),
  `need` → `OUGHT` (he voices a demand). `WILL` has no question source and is not formed (named).
- **Requirement.** That `holds` conjunct: he holds a claim on what he speaks of, so a word about nothing
  he knows is not formed; refusal `utterance.empty` for a hand-built act only.
- **Roll.** None. An utterance is a fiat of the speaker (it may be false; nothing verifies, FI-05B §7).
- **Effects.** As today plus content. Not graded: there is no degree to saying something.
- **Writes / emits.** `Proposition.exists` (unchanged), the maker's `hold` (unchanged);
  `proposition.uttered`. WITNESS deposits on those present a told-shaped claim of the Proposition's cell
  with the utterer on its chain, through FI-05B E-3's deposit (an utterance is a telling to the room;
  `loop/witness.py`'s told-deposit trigger gains "the act mints a `HOLDS` Proposition").
- **Cost.** A held `hold` (budget, `H-92`), and exposure: an uttered `HOLDS` is a citeable item against its
  utterer (FI-05B E-1's `oath` kind applies only once he `commit`s; the bare word is cited as the
  witnesses' told claim).
- **Unlocks.** `commit` to a real statement; `covenant`/`issue`/`petition` terms with content; the
  contradiction rule (`decision.agreement`) between two persons' utterances; judges' ambition votes
  (`world_q.py:759`); `interrogate`'s `HOLDS` charge form.
- **Reason trail.** The Proposition records `subject/predicate/value/mood/when`; the act's `occasioned_by`
  names the claim it was derived from.
- **Readers named.** `commit`, `covenant`, `issue`, `petition`, `construe` (§4), `determine` votes, SC-P8's
  contradiction, `aim_state`.

**4 Scales.** Person (the word), settlement / faction (a creed Proposition is an uttered `OUGHT` with a
faction leader as subject: the builder's creeds use the same carrier), realm (a decree's terms). A player
chooses which held belief or want to voice and where (the question aperture); the engine derives the
cell. NPCs choose `utter` through the one chooser; its `utter` pursuit lean (`rosters.yaml:3755`, `:4502`)
stays the scorer.

**5 Tuning hooks.** Mood by source: `rosters.yaml: utter_mood_by_source` (new). Personality: the existing
pursuit leans on `utter` (`rosters.yaml`). Venue: whether a room hears it is presence (WITNESS). Evidence:
the derived cell's confidence is the source claim's. Season: none.

**6 Exact edits.** Proposal S2-B §1.

**7 Gate and falsifier.** Gate: `build_realm(0..2)`, one season, on-arm: the fraction of computed
Propositions with a non-empty predicate is ≥ 0.9 and each `HOLDS` Proposition's cell equals a claim its
utterer held at the act; at least one `determine` ambition vote or one `decision.agreement` disagreement
between two utterances is read in two seasons at one of three seeds. Control: fixture
`utter_content: off` reproduces today's hash. Planted failure: an act whose `about` claim is removed from
the ledger before the fold must not mint a Proposition with that cell.

**8 Cases.** Every case that needs a vow or a creed to mean something: NPC-082 (Torberg's commitment to
the cause; `audits/12_ARCS_adjudication.md` §5 stage 2), the M-LATENT goal stages (§5 stage 5), the 25 e1
cases where a cited item may be a held statement, and the creed-vote reading of `judging_set`. `[case
files not opened; ids from the adjudication]`

**9 NERS.** N: without content, `commit`, `covenant`, `issue` and every hearing vote are empty from every
direction (top-down a statement is the unit of argument; bottom-up the carrier exists and is frozen;
lateral FI-05B's told deposit is the same channel). R: the world fills with positions people hold and can
be held to, with no player present. S: one carrier, one derivation rule, the told channel's arithmetic.
E, last: three derived operands against a carrier that today holds nothing. **Cut test:** removing
`utter` removes every Proposition minted in play; merging it into `commit` would make every statement a
vow (no lie, no retraction by silence) — keep.

## 2. `petition`

**1 Premise.** *A person asks someone with power over his place to act on a matter, in writing.* Links:
(a) a grievance or want (the matter); (b) an addressee who can act (a seat-holder whose purview reaches the
petitioner's place); (c) a document with terms, to, from; (d) it reaches the addressee; (e) the addressee
answers: puts it before a room (`carry`), denies it (closes the document), or ignores it (it lapses);
(f) the petitioner may withdraw it.

**2 State today.** Row: `own`, `referent_class: Person`, `counterparty: to`, typed `existence(to, Person)`
and `existence(from, Rung)`, writes `Record.exists`, emits `petition.filed` / `petition.refused`. Effect
`_eff_petition` (`effects_information.py:706-725`): `_mint_document(w, a, "petition", ...)` with the
maker's `hold`. `to` and `subject` both bind the question's one referent (`H-94`; row note), so the
petition is addressed to the person it is about: probe 12/12, 14/14, 13/13. Two per seed are docketed by
`carry` (`effects_information.py:448-508`), by the petitioner himself. The closers (withdraw, deny) are
`destroy_record`, which cannot fire (`H-75`, row docstring). **Verdict: executes; link (b) is broken in
every act, (d)–(f) are absent.**

**3 Build-out, decided.**
- **Formation.** `subject`: the question's Person- or Rung-classed referent (a person is a grievance about
  him, a rung a need of the place). `to`: fanned over the **seat-holders the petitioner knows hold a seat
  whose ground holds his home**, read off his own ledger (`person_q.seat_holders_known(ledger)`, new,
  World-free: the `(seat, seat.held, holder)` claims of S2-B §4), excluding the actor and the subject.
  A petitioner who knows no such holder forms none (no dead end: the refusal he could have read is moved
  into formation).
- **Requirement.** As today (`existence` of both sides). No roll: a filing is a fiat; its success is the
  addressee's response.
- **Effects.** The Record, as today, with `to` now a holder. Delivery is `give` (plan position 16): the
  petition is in the petitioner's hand and `give`'s `to` fan offers the addressee; the receiver, once
  holding it, forms `carry` (accept) or `destroy_record` (deny, `H-75`'s cross-family closer). Unanswered,
  it lapses at its stages (`Record.stages`, `H-80`'s default), which MATTER already matures.
- **Reason trail.** `{terms, to, from}` on the Record; `occasioned_by` names the question.
- **Readers.** `carry`, `give`, `interrogate`'s charge (`_req_interrogate` clause 3 reads `terms`), the
  addressee's question (the held petition is a `Record`-classed referent, REM-25), SC-P8's `record` proof.

**4 Scales.** Person → settlement (the addressee's seat). Composes upward through `carry` onto a
docket and `determine`. Player: choose matter and addressee from the fanned Candidates. NPC: the chooser.

**5 Tuning hooks.** Who counts as an addressee: the seats known over the home (S2-B §4; no second
addressee roster, one owner). Which arm: fixture `petition_addressee` (`data/fixtures.py`). Personality:
the `petition` pursuit leans. Season: `H-80` stage default.

**6 Exact edits.** Proposal S2-B §3.

**7 Gate and falsifier.** Gate: `build_realm(0..2)`, two seasons: `to == subject` 0 of all petitions;
`to` holds a seat reaching `from` for every petition; at least one petition is given to its addressee and
carried by him (not by the petitioner) at one of three seeds. Control: fixture `petition_addressee:
referent` reproduces today. Planted failure: a petitioner whose seat-holder claim is deleted forms no
petition.

**8 Cases.** ARC-04 (Maret's petition to Vaynard dropped or carried; adjudication §5 stage 3), the M-SIT
cases of stage 3, NPC-088 (a petition as a held document). `[case files not opened]`

**9 NERS.** N: a petition to the accused is not a petition; without an addressee the M-SIT chain starts
from nothing. R: whom to petition and whether to deliver is a choice; an addressee who ignores it is a
story. S: one fan rule shared with `oblige` (seats known); delivery is `give`. E: one reader and one fan
against a row that already executes. **Cut test:** merged into `create_record` it would lose `to`/`from`
and the `carry` route — keep.

## 3. `open_case`

**1 Premise.** *An official who may judge brings a charge against a person and puts the matter before his
bench.* Links: (a) a seat with the remit to judge; (b) a party within its reach; (c) a charge: what he is
said to have done, on what ground; (d) a case file drawn up; (e) the matter goes on the docket under a
procedure; (f) the case file is what the hearing records into and what can be reopened.

**2 State today.** Row: `remit:determine`, `referent_class: Person`, typed `basis(subject, purview)`,
writes the case file (`Record`, kind `text`, no content) and the docket item, emits `case.opened`;
refusals keyed by clause. Effect `effects_information.py:366-445`. A computed case carries no arrangement
and no petition (both `None`). `aperture`: 11 attempts, 6 opened, 3 `case.refused` (the matter already
docketed: the docket question stamps its docketed persons `Person`, `world_q.py:418-426` names this
limit 3), 2 `case.unauthorized` (purview). Probe opened 6 / 8 / 5. `determine` reads the docket.
**Verdict: works in part** — (a), (b), (d), (e) hold; (c) and (f) are empty: the file holds nothing, so
the charge is the party's name.

**3 Build-out, decided.**
- **Formation.** As today on a `Person` referent, minus docketed matters (S2-A §3: the docket question
  carries its matters as class `Matter`, not plain, so `own_referents_of_class` no longer stamps them
  `Person`). The 2 `authority` refusals stay: whether the party lives within the seat's reach is a fact
  the opener may be wrong about, and the refusal teaches it (clause 4's epistemic reading).
- **Content.** The case file is a Record of a new kind `case` with content `{terms, charge, arrangement}`:
  `terms` the party; `charge` the `Said` of the opener's newest deed claim about the party
  (`person_q.said_of`, FI-06's widened pool), the first entered item of FI-05B E-2; `arrangement` the
  venue's default row (SC lane, `05_SC_arrangement_rows_that_bind.md`; until it lands, `None` as today).
  `ABOUT_KEYS["case"] = "terms"`. The docket item names the case file (CR-61's edit, as SC-P6 requires).
- **Requirement.** Adds `own_ledger(subject)`: he holds a claim about the party (a charge needs a
  ground). Refusal `case.refused`.
- **Roll.** None (opening is a remit act); the contest is the hearing (`determine`).
- **Effects / writes.** `Record.exists`, `Record.stages`, `DocketItem.*` as today; content as above.
- **Cost.** The opener is on the chain of the charge (FI-05B E-7: citing costs disclosure).
- **Readers.** `determine`, `interrogate` (the charge, through `ABOUT_KEYS`), SC-P8's stages, SC-P6's
  dismissal (the item's case file), `speak`'s `Matter` referent.

**4 Scales.** Settlement seat (a magistrate) up to realm (a crown court) through `via.scope`'s purview.
Player: choose whom to charge from his ledger. NPC: the chooser; office duty (CR-88) is the scorer.

**5 Tuning hooks.** Arrangement per venue (`venues.yaml`, SC lane); the `case` record kind
(`rosters.yaml: record_kinds`); stage default (`H-80`).

**6 Exact edits.** S2-A §3 (formation); S2-C §1 (the case file's content).

**7 Gate and falsifier.** Gate: `build_realm(0..2)` two seasons: `case.refused` on the `write` clause 0;
every case file has `charge` naming a claim its opener held; `interrogate` and `determine` read the case
file's `terms` (S2-C gate). Control: `case_content: off`. Planted failure: an opener holding no claim on
the party forms no case.

**8 Cases.** ARC-04 (a case against Maret matures by stage), ARC-10, NSC-03, the 25 e1 cases (the charge
is the first cited item), e5 (a reopenable file). `[ids from the adjudication]`

**9 NERS.** N: a case with no charge is a docket entry; with it, the hearing has something to answer. R:
whom to charge and on what; a wrong charge binds as hard (e3). S: the charge is FI-05B's entered item,
one carrier. E: one content dictionary on an existing mint. **Cut test:** folding into `carry` (a seat
carrying its own petition) loses the remit path and the official's initiative — keep.

## 4. `construe`

**1 Premise.** *A person who has received an order reads it his own way, and from then on acts on that
reading.* Links: (a) he holds the writ; (b) the writ has terms; (c) he forms a reading that differs; (d)
the reading is his (a belief, not a change to the writ); (e) his later compliance or defiance is judged
by his reading, while the issuer judges by the terms — a dispute two held items can carry.

**2 State today.** Row: `own`, `referent_class: Record`, `referent_named`, typed `existence(subject,
dispensation)` + `own_ledger(subject)`, writes `[]`, emits `terms.distorted` / `construal.impossible`.
No effect (emission-only by `writes_note`). The `Record` class is shared across held kinds (REM-25,
`rosters.yaml: referent_classes`), so the row forms on a held faction sheet, cover, petition or text and
the fold refuses it: probe subjects `faction_sheet` 4 (seed 0), `faction_sheet` 2 + `cover` 1 (seed 1),
`faction_sheet` 4 + `petition` 1 + `text` 1 (seed 2); dispensations in the world 15 / 10 / 8. The row
note concedes the falsifier (*two holders of one writ holding different content values*) is unbuilt
(`H-36`'s magnitude half). **Verdict: forms on the wrong document; never executes; and executed, it
would deposit only that a distortion happened.**

**3 Build-out, decided.**
- **Formation.** On a held `dispensation` only (S2-A §2: the Record class is stamped by sub-kind, so a row
  whose typed `existence` names a Record kind forms on that kind alone). And only where the reading can
  differ: the construer holds, in his own ledger, a claim on the terms' cell `(subject, predicate)` with
  a value other than the terms' (a person-side read once `utter` carries content, S2-B §1).
- **Effect (new `_eff_construe`).** Mints the construer's reading as a `HOLDS` Proposition: the terms'
  subject and predicate with **his own held value** (*a person reads an order as meaning what he already
  believes*), with his maker's `hold`; and writes nothing on the writ. Writes `Proposition.exists`.
  Emits `terms.distorted`; WITNESS deposits it with the reading's id, so whoever is present holds that he
  read it so. Declines (`construal.impossible`) where the writ's `terms` is no Proposition or he holds no
  differing value (a hand-built act).
- **Downstream.** `comply` / `evade / defy` (another family's rows) judge the act against the actor's
  reading where he holds one (his own ledger, as their `own_ledger` conjunct already reads); the issuer's
  terms and the construer's reading are two held items on one cell with different values, so SC-P8's
  contradiction rule makes the construal answerable before a bench (*"he twisted my order"*).
- **Cost.** His reading is on record; citing it against him is a contradiction a judge weighs.
- **No roll.** A reading is a fiat of the reader; the contest is the later hearing.

**4 Scales.** Person (the reader) against settlement / faction / realm (the issuing seat). Player: choose
to construe a writ he holds. NPC: the chooser; a person whose pursuits oppose the terms is likelier
(existing pursuit lean on `construe`).

**5 Tuning hooks.** None new: the reading's value is the construer's own; personality through the
pursuit lean; evidence through SC-P8.

**6 Exact edits.** S2-A §2 (formation), S2-B §2 (effect, row).

**7 Gate and falsifier.** Gate: a hand-built world (one issuer, one writ with `HOLDS` terms, one holder
believing otherwise): `construe` executes, two holders of the writ hold different readings (the row's
own falsifier), and a `comply` by the construer is admitted on his reading while the issuer's `determine`
reads the contradiction. `build_realm(0..2)`: `construal.impossible` on non-dispensations 0. Control:
`construe_reading: off`. Planted failure: a construer holding the same value as the terms forms none.

**8 Cases.** NPC-004 (a confident wrong reading), the evade/defy and comply arcs of M-SEAT where an order
is obeyed in letter. `[case files not opened]`

**9 NERS.** N: without a reading, the comply / evade / construe triple is two verbs and a label; Jordan's
refraction ruling (signified vs signifier, row `naming_note`) has no mechanism. R: obedience in letter,
loopholes, disputes no player starts. S: the reading is an ordinary Proposition; the dispute is SC-P8's
contradiction. E: one effect reusing `utter`'s mint. **Cut test:** merging into `utter` loses the writ
binding and the comply reading — keep, but `_eff_construe` calls `_eff_utter`'s mint, no second mint.

## 5. `speak`

**1 Premise.** *A person addresses the room on a matter before it, to move the bench.* Links: (a) a
sitting or docket with the matter on it; (b) the speaker is at the venue; (c) he puts items and argument
(cited evidence, FI-05B / SC-P8); (d) the bench is moved by degree; (e) the case file records what was
said; (f) the opposing side may answer.

**2 State today.** Row: `own`, typed `existence(subject, DocketItem)`, contested `a matter` (social contest
provider), `subject_may_be_self`, writes `[]` at every band (`H-63`'s stop), emits `matter.carried /
advanced / held / turned`, refusal `speech.unheard`. Forms on every plain referent (no class): `aperture`
8 attempts, 7 `exists:DocketItem=0`; probe unheard 7 / 9 / 13 against executed 1 / 5 / 4; pool 2 for
every speaker. Bands are witnessed and nothing reads them but the hearers' ledgers. **Verdict: forms on
what is not docketed; when it executes it moves nothing a later act reads.**

**3 Build-out, decided.** Formation is this family's (S2-A §1): `referent_class: Matter`, the docket
question's matters. Everything inside the room is SC's and is cited, not redone: `cites` operand (FI-05B
E-1), case-file stages per cited item at `Success`+ (E-2, SC-P8 edit 2), citation as telling (E-3),
answering by contradiction and impeachment (E-5, SC-P8 edit 3), counting through `world_q.hearing` (SC-P8
edit 4), and the hearing as the module's scene (SC-P3B). The band writes this audit decides, so the row is
not empty: `Overwhelming` / `Success` / `Partial` append a band stage to the case file (`Record.stages`,
SC-P3B's "band stage"; the carrier the gate can receipt, which `H-63` lacked); `Failure` writes `[]`.
The `Person.stance` write `H-63` names stays unbuilt (no value source). The venue half (*at the actor's
venue*) is a `with`/`present_at` conjunct once a docket item carries its date's venue (SC lane); named,
not built here.

**4 Scales.** Settlement / faction / realm benches; the person is the speaker. Player: which matter, which
items to cite, whether to answer. NPC: the chooser forms the `cites` variants (SC-P3 edit 2).

**5 Tuning hooks.** `copying` capability (`rosters.yaml: verb_capability`); arrangement `proofs:`
admission (SC-P8); `reception` (judges' pursuits); venue rules of who may speak (SC lane, e4).

**6 Exact edits.** S2-A §1 (formation), S2-C §2 (band writes).

**7 Gate and falsifier.** Gate: `build_realm(0..2)` two seasons: `speech.unheard` on `exists:DocketItem=0`
0; every executed `speak` at `Partial`+ adds one case-file stage; SC-P8's gate (a)–(c) on SC-P3's world.
Control: `speak` without the class (revert). Planted failure: a docketed matter removed from the docket
before the fold refuses with `speech.unheard`.

**8 Cases.** The 25 e1 cases (citing), e4 (who may speak), ARC-04, NPC-086 (Bergvall's hearing),
NPC-088. `[ids from the adjudication]`

**9 NERS.** N: the hearing's one move. R: what to cite and what to hold back. S: the class is the
existing partition; the stages are SC-P8's carrier. E: one column and one stage write. **Cut test:**
merging into `argue` loses the room (argue is a two-person contest of pursuits) — keep.

## 6. `tell`

**1 Premise.** *A person passes something he knows to someone he is with.* Links: (a) he holds the claim;
(b) the hearer is present; (c) he chooses what to pass on; (d) the hearer comes to hold it, discounted by
one hop, with the teller on its chain; (e) disclosure costs (confidence broken where the claim was
another's secret); (f) a paired deed carries its hand.

**2 State today.** Row: `own`, typed `own_ledger(subject, holds)` + `relation(to, with, hearer)`,
`counterparty: to`, contested `a standing`, writes `[]`, emits `news.told` + `confidence.broken` (three
bands) / `news.untold`, refusals keyed. Deposit-only by ruling (WITNESS told deposit). `aperture`: 20
attempts, 16 refused on clause `hearer`; probe `tell.refused` 20 / 43 / 4, `news.told` 2 / 1 / 0; told
claims with a chain 7 / 0 / 0, all one hop; pool 2 for all. FI-02 measured the same three attritions
(absent hearer, the roll, nothing new to say). **Verdict: forms on absent hearers; the roll fails two
times in three; chains do not grow.**

**3 Build-out, decided.** The design is FI-02's and FI-06's and is cited: the `to` fan over
`person_q.present_persons` (FI-02 edit 5; the refusal moved into formation), the `unshared` slant
(edits 2–4), and the pairing that travels (FI-06). This family decides the one thing left open by FI-02
edit 6 (*whether an ordinary telling between two people who are together should fail two times in
three*): **an uncontested telling to a hearer who holds no opposing standing does not roll.** The row
contests `a standing` only where the hearer holds a claim on the same cell with a different value (he
must be persuaded); otherwise it resolves at `Success` without a draw. The test cannot read the hearer's
ledger (F8 admits a resolver-side read of the actor's own ledger only), so it is made on the TELLER's own
ledger: whether he holds a claim that the hearer believes otherwise on that cell (a told or seen claim
whose holder-of-record is the hearer). The teller's belief decides whether he expects to argue; a wrong
expectation is a roll he did not need, or a persuasion he did not attempt and whose told copy the hearer
then holds beside his own contrary claim (the contradiction is the hearer's to weigh, through
`decision/options.py::record`). `confidence.broken` stays (the band kinds are the ruling's).

**4 Scales.** Person to person; composes to settlement and faction through chains (FI-02's gate: two-hop
chains above 0). Player: whom to tell what. NPC: the chooser with FI-02's slant.

**5 Tuning hooks.** `said_slants` (FI-02), `telling_hearers` fixture (FI-02), `copying` capability, hop
discount (`teller_weight`), `told_pairing` (FI-06).

**6 Exact edits.** S2-A §4 (adopts FI-02 edit 5 as this row's formation; no second edit), S2-C §4 (the
roll only where opposed).

**7 Gate and falsifier.** Gate: FI-02's (two-hop chains above 0 at one of three seeds); `tell.refused` on
clause `hearer` below 25% of attempts; `news.told` ≥ `news.untold` where the teller holds no opposing
claim. Control: `tell_unopposed_roll: always` (today). Planted failure: a hearer moved away between
formation and fold still refuses.

**8 Cases.** c7 (29 cases: tell or withhold a held fact for a reason), M-INFO (33 cases), NPC-088.
`[ids from the adjudication]`

**9 NERS.** N: the information economy's one channel. R: disclosure is a choice with a cost. S: the told
deposit is the same as a citation's (FI-05B E-3). E: no new verb, one formation fan and one roll rule.
**Cut test:** none proposed.

## 7. `interview`

**1 Premise.** *An investigator questions someone he is with about a matter, and learns what that person
chooses to tell him.* Links: (a) the person questioned is present; (b) there is a topic; (c) the
questioned person decides: tell, lie, or refuse; (d) the investigator holds what he was told, with the
source; (e) a lie can later be caught (FI-03 §2: checking a telling is investigating).

**2 State today.** Row: `own`, typed `existence(subject, Person)`, writes `[]`, emits `finding.made` /
`finding.none`, ungraded (`rosters.yaml:1425`: a prompt, K-36). No referent class: forms on any referent;
`aperture` 19 attempts, 14 `exists:Person=0`; probe subjects Person 5 / 3 / 5 of 19 / 8 / 19, Rung,
Record, Proposition the rest, one self-interview at seed 1 (the row note concedes the grammar admits it).
An ungraded `finding.made` "reaches the row and finds nothing" (`rosters.yaml:3295`). **Verdict: forms on
non-persons; executes and finds nothing.**

**3 Build-out, decided.** CP-T06-05 as planned (FI-03 §2's table): *the questioned person answers by his
own `tell` or `lie`*. Built as a prompt through the one chooser, not a scripted answer.
- **Formation.** `referent_class: Person` (REM-21's stamp, `petition`'s and `open_case`'s precedent);
  `counterparty: subject` (no self-interview: the existing person-side decline); and a `with` conjunct
  on `subject`, fanned person-side over `present_persons` (FI-02 edit 5's reader) so an absent subject is
  not formed.
- **Topic.** The operand `on`: the subject of the claim that raised the investigator's question
  (`Question.about`), else the interviewee himself (what he did: FI-06's widened `said_of` pool).
- **Effect.** No `_eff_interview`: a Question is not world state, so there is nothing to write. The
  row stays ungraded and write-free; WITNESS deposits on the
  interviewee a claim `(asker, interview.asked, on)` (`interview.asked` replaces `finding.made` as the
  row's emitted kind, so the inquiry roster's `finding.made` no longer claims an ungraded verb), and
  `world_q.questions_for` gains a source `asked` (`rosters.yaml: question_sources`) raising, for a person
  holding such a claim from this tick, a Question whose referents are `(on,)` and whose `about` is the
  claim; `tell`'s and `lie`'s `to` fan includes the asker (present by the `with` conjunct). His chooser
  then answers by `tell`, `lie`, or by nothing (silence is the null choice). The investigator's product
  is the told claim, with the interviewee on its chain.
- **Refusals.** `finding.none` renamed `interview.refused`, for a hand-built act whose subject is absent.
- **Cost.** A scene of each; the interviewee learns what the investigator is asking about (disclosure,
  FI-05B E-7's logic).

**4 Scales.** Person; composes into a case (the answer is a citeable testimony, FI-05B E-1). Player: whom
to question on what; as the questioned, what to answer. NPC: the chooser on both sides.

**5 Tuning hooks.** `question_sources` (the `asked` row and its attention tier, `attention_key`);
personality (the interviewee's leans on `tell` / `lie`); relationship (`teller_weight`'s relation term,
S2-D's tie).

**6 Exact edits.** S2-A §5 (formation), S2-C §3 (the prompt).

**7 Gate and falsifier.** Gate: hand-built `inquiry_world` (FI-03 §1): the interviewee forms `tell` or
`lie` to the asker in the same season at ≥ 1 of 3 seeds, and the asker holds the answer with the
interviewee on its chain; `build_realm(0..2)`: `interview` on a non-person 0. Control: `asked` source
off. Planted failure: an interviewee absent at the fold produces no `asked` claim.

**8 Cases.** The 25 investigation cases (adjudication §10), NPC-004 (a confident wrong conclusion from a
lie), NSC-01. `[ids from the adjudication]`

**9 NERS.** N: the investigation's conversation; without it testimony is overheard only. R: the
questioned person is an agent, so a lie is his choice and a story. S: the answer is an ordinary telling.
E: one emitted kind, one question source, against an act that today yields nothing. **Cut test:**
folding into `tell` (the investigator tells the subject he wants to know) loses the prompt — keep.

## 8. `interrogate`

**1 Premise.** *A judge questions a prisoner in his custody on the charge, and may extract a confession.*
Links: (a) custody (a live `detain`); (b) a charge (the case); (c) the judge's remit; (d) a contest of
wills; (e) a confession by degree; (f) the confession is evidence before the bench and known to those
present; (g) a cost to the prisoner and a mark on the interrogator.

**2 State today.** Row: `remit:determine`, `referent_class: Detainee` (formed only on a person in a live
`detain` on the asker's seat), predicate `_req_interrogate` (`predicates.py:528-563`: person, custody,
a docketed petition naming him), contested `a proposition`, writes `[]` at every band (`H-226`), emits
`confession.full / made / partial / withheld`, refusal `interrogation.refused`. Live `detain` 0 at three
seeds; formed 0. **Verdict: unreachable**, by the absence of custody (PHYSICAL's `arrest` / `capture`)
and of a `detain` disposal (`determine` under a `detain` arrangement, SC-03a).

**3 Build-out, decided.**
- **Formation.** Unchanged (the Detainee class is the right shape).
- **Charge.** `_req_interrogate` clause 3 reads the docket item's case file as well as its petition,
  through `ABOUT_KEYS` (S2-C §1's `case` kind), so an `open_case`d matter is a charge, not only a carried
  petition.
- **Roll.** As today; the prisoner opposes (`counterparty: subject`); pool `inquiry` or `pool_default`.
- **Effects.** `Overwhelming` / `Success` / `Partial` write one case-file stage `proof:confession`
  (SC-P8 edit 2's carrier; FI-05B E-1's `confession` kind) and the bands' kinds are deposited at WITNESS
  as today; `Failure` writes `[]` and emits `confession.withheld`. So `_eff_interrogate` exists for the
  three winning bands (the case file is the receipted subject), closing `H-226` by route (b) for this row.
- **Cost.** The prisoner's regard of the interrogator falls through the witnessed deed (existing
  `regard`); a confession at `Partial` withholds the hand (FI-05B's partial-copy rule).
- **Readers.** `world_q.hearing` (SC-P8 edit 4), `determine`, the bench's ledgers.

**4 Scales.** Settlement / faction bench. Player: interrogate or not; the prisoner (if a player) resists.
NPC: the chooser.

**5 Tuning hooks.** `verb_capability: interrogate` (new row, `inquiry`), arrangement admission of the
`confession` kind (SC-P8), `regard` weights.

**6 Exact edits.** S2-C §5.

**7 Gate and falsifier.** Gate: SC-P3's `build_hearing` world plus one `detain` (planted by a `determine`
under `arrangements.yaml`'s `detain` row): `interrogate` forms, executes, and at a planted `Success` the
case file gains one `proof:confession` stage and `hearing` rises by `proof_step`. Realm reach waits on
PHYSICAL's `arrest`/`capture`. Control: no detain → formed 0. Planted failure: a prisoner with no charge
on the docket is refused before the draw.

**8 Cases.** e1 cases with a confession (adjudication §10), ARC-07, NPC-008. `[ids from the adjudication;
case files not opened]`

**9 NERS.** N: the confession is the third proof kind with no producer. R: coercion as a choice with a
cost. S: one stage carrier. E: one effect for three bands. **Cut test:** merging into `interview` loses
custody and the contest — keep.

## 9. `oblige`

**1 Premise.** *A person enters the service of a seat (swears to it) and owes it duty for a term.* Links:
(a) he knows of the seat; (b) its `binds` admits him; (c) he is not its holder; (d) the oath opens a
service edge with a term; (e) the service is renewed by upkeep or lapses; (f) the seat's establishment
grows, and he gains what service brings (learning through the seat, protection, standing).

**2 State today.** Row: `own`, `referent_class: Office`, `referent_named`, untyped with `_req_oblige`
(`predicates.py:466-525`, five clauses), writes `Tenure.since` / `Tenure.term`, emits `duty.taken` /
`duty.refused`. Effect `_eff_oblige` (`effects_governance.py:461`). The row forms on a seat the person
was told of (`seats_named`, `world_q.py:3146-3161`); probe: persons with a seat named 0 before and after
the season at three seeds. **Verdict: unreachable** — link (a) has no source at build, and before any
seat changes hands nothing deposits one (the row's own `formation_decline_note`).

**3 Build-out, decided.** A person knows the seats over his own home and who holds them. Built as a
build-time deposit on CR-81's precedent (`harness/populated.py::seed_acquaintances`): for each person,
one firsthand claim `(seat, seat.held, holder)` per seat whose purview reaches his home rung. Then
`seats_named` is non-empty for every person under a seat, `oblige` forms on those seats, and `petition`'s
addressee fan (§2) reads the same claims. In play, the same claim is deposited by WITNESS of a
`tenure.opened` (already the case). The five clauses stay; why someone obliges is the chooser's (pursuit
leans; a want for protection or office). No roll.

**4 Scales.** Person → seat (settlement to realm). Player: whom to serve. NPC: the chooser.

**5 Tuning hooks.** Fixture `seats_known_at_build` (`data/fixtures.py`: `home_purview` / `none`
(control)); upkeep and term (`oblige_term`, `H-159`); `binds_bases`.

**6 Exact edits.** S2-B §4.

**7 Gate and falsifier.** Gate: `build_realm(0..2)` two seasons: `oblige` formed > 0, executed ≥ 1 at one
of three seeds, and the new obligee appears in `establishment_of` and pays or lapses at MATTER. Control:
`seats_known_at_build: none`. Planted failure: a person whose seat claims are removed forms no `oblige`.

**8 Cases.** M-SEAT (39 cases need a seat's business done; adjudication c5), NPC-082 (service to a
cause), the retinue arcs. `[ids from the adjudication]`

**9 NERS.** N: service is how a seat grows a following; without it `establishment_of` is the builder's.
R: who serves whom drifts with no player. S: the same claim feeds `petition`. E: one build step and no
new verb mechanism. **Cut test:** none proposed.

## 10. `tie / knot`

**1 Premise.** *A person binds himself to another (a sworn friendship, a pact; for `knot`, a Thread bond
through which he senses the other).* Links: (a) a partner he is with and knows; (b) a directed edge he
owns; (c) the bond changes how he weighs the partner's word, regard, and (knot) what he witnesses; (d)
strain may break it; (e) he can release it.

**2 State today.** Row: `own`, `requires: —`, writes `Tenure.since`, emits `bond.formed`, no refusal; no
effect; not in `resolvable_verbs()`. `H-182` (row `effect_decline_note`): IN-32 built `_eff_tie` and was
reverted because nothing read a tie (`teller_weight`'s relation term never ran: no chained told claims);
`knot` has a reader (`epistemic._ch_witness_key`) that reads it undirected; the row binds no partner
operand and names two kinds for one opener. **Verdict: stub by ruling.**

**3 Build-out, decided.** FI-08's order is adopted: the reader first (FI-02's two-hop chains), then
IN-32's effect re-lands. This family decides the row's shape: **split it into `tie` and `knot`** — two
kinds, two meanings, two readers; one opener writing either kind would need an operand to pick the kind,
a scale-local dialect. `tie` (social, this family): `counterparty: to`, typed `relation(to, with)` and
`own_ledger(to)`, fanned over `present_persons`; writes `Tenure.since` (kind `tie`, owned by the actor);
emits `bond.formed`, refusal `bond.refused`; readers `teller_weight`'s relation term (IN-32's `tied`
term), `regard` (a tie raises regard of the partner, the existing reader one term over), and `release`.
`knot` stays declined and moves to the Thread lane (FI-08 §1, `29f`), its row text kept with
`stratum: thread` and its decline note.

**4 Scales.** Person to person; a tie network is a faction's informal structure (`thread_read` reads it,
FI-03 table). Player: whom to bind. NPC: the chooser.

**5 Tuning hooks.** `tie_gain` (IN-32's fixture), `regard` weights, knot strain (FI-08 §4, design-first).

**6 Exact edits.** S2-D.

**7 Gate and falsifier.** FI-08 §3's two conditions, then: `build_realm(0..2)` two seasons, `tie`
executed > 0 and `teller_weight` called with a tied relation > 0 times, with `tie_gain` 0 vs 0.5 hashing
differently. Planted failure: `tie_gain` 0 must hash as the control.

**8 Cases.** Typed relationships (adjudication §7: sworn bond, kin, rivalry), Kreutz / Ehrenwall /
Torberg's personal loyalty (M-REGARD). `[ids from the adjudication]`

**9 NERS.** N: a bond a person chooses, distinct from a seat (`oblige`) and a vow (`commit`). R: networks
form without a player. S: owner-directed edges, `release` closes. E: one row split, one effect re-landed.
**Cut test:** removing `tie` loses the only chosen person-to-person bond; folding `knot` into `tie` would
make every friendship a Thread channel — split, as decided.

## 11. Family order

### 11.1 Dependency graph (inside the family)

```
S2-A formation (speak Matter class, interview Person class, construe sub-kind, open_case off docket, tell present_persons)
      │
S2-B content:  utter content ──► construe reading
               seats known ───► oblige ; petition addressee
      │
S2-C case & question: open_case charge (case kind) ──► interrogate charge ; speak band stages ; interview prompt ──► tell (unopposed)
      │
S2-D tie (after FI-02's chain gate)
```

`utter` content precedes `construe`, the `HOLDS` charge form and every Proposition-reading verb.
`open_case`'s `case` kind precedes `interrogate`'s charge reading and SC-P6's dismissal of an
`open_case`d matter.

### 11.2 Cross-family dependencies

- PHYSICAL: `arrest` / `capture` make custody (`interrogate` reach). `14_VERBS_PHYSICAL.md` P-A.
- BINDING / SOCIAL1 (whichever owns them): `comply`, `evade / defy` read the construer's reading;
  `commit`, `covenant`, `issue` consume `utter`'s content; `destroy_record` (`H-75`) is `petition`'s
  deny closer; `give` delivers a petition.
- The same Record sub-kind stamp (S2-A §2) fixes `comply`'s 16 and `evade / defy`'s 1 wrong-sub-kind
  refusals and `accept`'s 17 (`aperture`: record_subkind) — owned there, landed here once.
- FI lane: FI-02 (edits 2–5), FI-06, FI-03 §1 (`inquiry_world`), FI-08.
- SC lane: SC-P8, SC-P3B, SC-P6, CR-61, `05_SC_arrangement_rows_that_bind.md`.

### 11.3 Landing order

| batch | lands | gate |
|---|---|---|
| S2-A | formation fixes (proposal A) | `build_realm(0..2)` 1 season: `speech.unheard`/`exists:DocketItem=0`, `interview`/`exists:Person=0`, `construal.impossible` on non-dispensations, `case.refused`/write all 0; executions of each not lower than baseline |
| S2-B | content (proposal B) | utter content ≥ 0.9; `oblige` formed > 0; `to == subject` 0 |
| S2-C | case, question, confession (proposal C), after CR-61 and FI-02 edit 5 | interview prompt answered; case file charge; interrogate stage on SC-P3's world |
| S2-D | `tie` (proposal D), after FI-02's chain gate | FI-08 §3 and S2-D's gate |

### 11.4 Decisions that survive to Jordan

1. **`tell` rolls only when the teller expects opposition** (§6). Options: (a) as decided — an unopposed
   telling resolves without a draw, so information flows and the contest is reserved for persuasion;
   (b) every telling rolls `copying` (today) — telling is a skill, information is scarce and a silver
   tongue matters even among friends. Materially different games: (a) is a world that talks, (b) a world
   that mostly fails to. Not answered by ladder steps 1–5: FI-02 edit 6 left it open and no ruling or
   precedent decides it.
2. **`construe` reads the writ as the construer already believes** (§4). Options: (a) as decided — a
   reading is motivated by held belief, which makes every construal a contradiction a bench can try;
   (b) construal as the issuer-side distortion of the content claim per holder (`H-36`'s magnitude half,
   the row's own falsifier), a random or pursuit-weighted drift with no held counterpart. (a) makes
   construal argued; (b) makes it noise. Jordan's refraction ruling (*signified vs signifier*) is
   compatible with both.
3. **Split `tie / knot`** (§10). Options: (a) split, `knot` to the Thread lane; (b) one row with a `kind`
   operand. Ladder step 5 favours (a) (no operand dialect), but a row split changes the verb count the
   R-05 instrument reads (67 → 68), which is Jordan's roster.
