# INST-VENICE-D — houses, rectors, charters; the content rows; and the playable scenario "The Counting-House"

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-10, X-11, X-12, X-15, X-32) — what §3 calls a charter (a trade privilege at a named market) is the form `staple` of `engine/season/instruments.yaml`; `charter` in the kit is a body's self-rule; no obstacle term `charter` is asked of the MATERIAL lane: a held live `staple` cited on an `exchange` is an `evidence` item; a rector's commission is the form `commission`; the row `exit_audit` is not added and every `audit_at_exit: exit_audit` below reads `audit`; `enrolment_ballot` and `security_bench` are tallied by the one rule for `declared` rows; the scenario is a case file with `base: spine` read by the one report (`15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` §1), so `counting_house.py` is not written, and its first cut (one loan, one harvest, one reckoning) is the first cut of the integrated playable. The `{venue:}` anchor, the house, the branch, the content rows and the scenario's seats and endings stand. Every finding below stands.

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_VENICE.md` §1.7–§1.9, §2.3–§2.6, §3, §4.3, §6.1 part 5, §10, §11, §13,
§14.2. Batch D. Depends on proposals A, B and C of this lane; FA-P2 (`06_FA_remit_grant_by_row.md`, the
Guild leader's row), FA `06_FA_office_capabilities.md` (founding content as data), the WR lane's
M-ABROAD place for Schoenland, and `audits/14_VERBS_MATERIAL.md` for `exchange`. Not ratified by being
written. **Every content row below is `[ASSUMPTION; medium; Jordan to correct]`; no canon name is coined:
posts and bodies are functional labels owed a row in `references/names_index.yaml` before they ship.**

## What it changes in `engine/season/` at runtime

1. A seat can be anchored on a building (a `hearth` rung): houses, counting-houses, guildhalls and yards
   get a head.
2. Content: head seats for the Guilds' houses; a commune council in Hafenmark; Schoenland's seats; three
   arrangement rows.
3. A held charter is a favourable term on the rate roll of an `exchange` at the market it names.
4. One scenario fixture and its headless reading.

Items 1 and 3 with no row or charter using them: hash EQUAL. Each content row is a declared mover.

## The problem (evidence)

- The title ladder is total down to the hearth (`offices.yaml: titles.domains`: "Family Head": hearth)
  and **no seat sits on a hearth or a community** (audit E-1: seats by rung kind territory 17, duchy 10,
  realm 4, settlement 2). The anchor resolver has four forms (realm, duchy, territory, settlement;
  `offices.yaml` header, "ONE resolver over the four forms") and none for a building, though 211 hearth
  rungs are built.
- The Guilds have two seats, both duchy-anchored (`off_guild_comptroller`; `off_npc_084` unrowed), and no
  place of their own; ARC-15, ARC-08, NPC-007, NPC-084 and NPC-085 turn on a guild house.
- Schoenland: "its persons act from their own seats and goals" (`canon/03_canonical_timeline.md`
  §Schoenland) and no seat, body or `foreign_cast` row exists (`rosters.yaml: foreign_factions` note).
- A charter has nothing to act on: `exchange` is `own`-eligible between any two rungs with stores
  (`verb_table.yaml`, `exchange` row), "attempted and never executed" in the corpus
  (`audits/12_ARCS_adjudication.md` §4 rank 12).
- No scenario exercises credit, a roll or a rotating body (standing requirement: playable alone).

## The resolution, decided

### 1. The house: a hearth with a head seat

No new carrier (audit §6.1 part 5). **Edit:** `harness/populated.py::resolve_anchor` gains a fifth form,
`{venue: "<building id>"}`, resolving to the `hearth` rung `venues.yaml` builds, by the same rule as the
other four (it names exactly one live rung of the kind it says). A head seat's row:

```yaml
- id:         off_house_<x>
  post:       "Family Head"          # on titles.domains (hearth); a title, so no body (refuse_a_title_in_a_body)
  rung:       {venue: "<building id>"}
  body:       null
  faction:    "<the house's faction>"   # authored: every house belongs to one (audit §14.2 survivor 3, option a)
  remit_acts: [issue, confer]        # covenant and warrant; appoint a branch manager
  conferral:  null                   # the line's own business; succession is CHAR's continuation_ties
  revocation: null
  holder:     "<case id>"
  upkeep:     null                   # the fixture default
```

- **Clients, factors, apprentices**: their own `oblige` to that seat (termed; renewed by the head's
  `transfer` of `upkeep` out of the house's stores). Proposal A makes the edge odds.
- **A branch**: another building's head seat, held by a **manager who is sworn to the parent head**.
  `purview_reaches`' oblige clause then gives the parent ground over the branch, **one edge deep**: the
  branch's own dependants are the manager's, not the parent's (`state/gate.py:432-440`, the "ONE EDGE
  DEEP" clause, itself an assumption with a named revert), which is the separate liability of the branch
  partnership. The manager's commission is a `dispensation`; his books
  are a `survey` Record he `give`s upward; his recall is the parent letting his term lapse.
- **A league chapter (Kontor)**: the same seat in a building inside another faction's settlement, with
  `faction` the league's.
- **A hired company**: a captain's `oblige` to the employer's seat with `upkeep`; the advance is a
  `debt` the employer's treasurer issues to him (proposal B); the commissary is a seat-holder the employer
  `dispatch`es to the camp (CP-T09-08). No row here.

### 2. The rector: a seat held at distance

A row pattern, no code beyond proposal C's keys:
`conferral: appointed`, `revocation: rung_above_in_holdings`, `term: 8`, `cooling_off: 8`,
`audit_at_exit: exit_audit`, `remit_acts` split by row as FA-P2 allows (a judge's `[determine, issue]`;
a captain's `[dispatch, convene]`), on a `{settlement: …}` anchor the appointing seat's holder holds.
First use: Schoenland's line and yard seats below.

### 3. The charter: a favourable term, not a gate

A charter is a `dispensation` whose `terms` is a market rung and whose `to` is the grantee, issued by a
seat whose purview reaches that rung; its validity is its unmatured stages. **This lane requires of the
MATERIAL lane's rate roll for `exchange` one term**: `charter`, favourable, when the actor (or the seat
he is sworn to) holds a live charter naming the `to` rung; and one venue key on the market's row, a
`standard` (SC's `difficulty_levels`) the host faction's seat-holder may raise by `establish` (an
embargo is the market's standard raised and its charters left to lapse). Trade without a charter is
attempted at worse odds, and its Failure band forfeits the goods offered to the market's rung. Nothing is
refused outright: under the standing rule a smuggler sometimes gets through. `[ASSUMPTION; the roll and
its bands are MATERIAL's; if `exchange` stays unrolled this item has no owner to land in and is held.]`

### 4. Content rows (data)

**`engine/season/rosters.yaml: office_bodies`** (only what a seat below needs; the file's own restraint):
`"Commune Council": "Hafenmark"` ("An elected council of a chartered town."), `"Assembly": "Schoenland"`
("Every enrolled citizen. Elects; does not debate."), `"Senate": "Schoenland"` ("Votes on the College's
written opinions; cannot initiate."), `"Security Council": "Schoenland"` ("Secret bench for offences
against the state.").

**`engine/season/offices.yaml: seats`**: (i) `off_house_feldhaus` at the guildhall NPC-007 is homed in
(`npcs.yaml`: `b_s_006_guildhall`), `faction: "Guilds"`, holder NPC-007, beside her existing
`off_guild_comptroller`. (ii) A guild roll seat `off_guild_roll` (`{duchy: "Hafenmark"}`, `body: "Guild"`,
`binds: members_by_warrant`, `remit_acts: [issue]`, `conferral: lot`, `eligible_from: off_guild_roll`,
`term: 4`, `cooling_off: 4`, vacant at build), and `eligible_from: off_guild_roll` on
`off_guild_comptroller` and FA-P2's `off_guild_leader`. (iii) Three commune council seats on one
Hafenmark settlement (`body: "Commune Council"`, `conferral: lot`, `eligible_from: off_guild_roll`,
`term: 4`, `cooling_off: 4`, `audit_at_exit: exit_audit`, `remit_acts: [determine, convene]`), vacant at
build; `eligible_from: off_guild_roll` on `off_commune_rep_hm`.

**`engine/season/offices.yaml: foreign_seats`** (built only with `foreign=True`, as Altonia's are; needs
a `foreign_cast` row for Schoenland minting one place, WR's): a head (`post` a functional label,
`body: null`, `faction: "Schoenland"`, `remit_acts: [convene]`, `conferral: elected`, `revocation: null`:
elected for life, presides, initiates nothing); two councillors and two sages on `Senate`
(`remit_acts: [issue]`, `conferral: lot`, `term: 2`, `cooling_off: 2`: the college that drafts); three on
`Security Council` (`remit_acts: [determine]`, `conferral: elected`, `term: 4`, `cooling_off: 4`); one
advocate (`remit_acts: [determine]`, `body: "Assembly"`: opens cases on any holder; the suspending
officer); one line seat and one yard seat on the rector pattern. Holders are new cast rows: **nine
persons this lane does not name.** `rosters.yaml: factions.head_seat` gains `"Schoenland": <the head's
row id>`.

**`engine/season/arrangements.yaml`**: three rows that dispose kinds existing sites open today.

```yaml
- id: security_bench        # the secret bench: denunciation, no accused in the room, no appeal
  disposal: declared
  quorum: 3
  bench_basis: determine
  floor: closed
  records_dissent: false
  venue_min_rank: settlement
  term_required: false
  appeal_basis: none
  interposed: [office, document]
  order: scripted
  proofs: [testimony, confession, record]
  disposes: detain
  disposal_reach: realm

- id: exit_audit            # the outgoing holder accounts; subjects' complaints are the evidence
  disposal: bench
  bench_basis: determine
  floor: open
  records_dissent: true
  venue_min_rank: settlement
  term_required: true
  appeal_basis: determine
  interposed: [person, document]
  order: alternating
  proofs: [record, testimony]
  disposes: ban
  disposal_reach: body

- id: enrolment_ballot      # a body votes a candidate onto its roll; his deeds are the evidence
  disposal: declared
  quorum: 3
  bench_basis: determine
  floor: admitted
  records_dissent: false
  venue_min_rank: settlement
  term_required: true
  appeal_basis: none
  interposed: [procedure]
  order: rank
  proofs: [record, testimony]
  disposes: oblige
  disposal_reach: body
```

`enrolment_ballot` uses what `determine` already does (a finding opens an `oblige` owned by the party on
the judging seat): carried, the candidate is in `establishment_of` the roll seat. Two further rows are
**named and not seeded**, for the reason the file's own header gives: a senate's decree disposes a
`Record` and an election a `hold`, and `_disposal` has no site for either until CR-36 and CR-35. After
an advocate suspends an act, the matter returns to the same body's docket for a fresh ballot at its
next sitting (audit §14.1 row 14); no row is needed. Unanimity (the three inquisitors) is not
expressible without a new key and is not taken.

### 5. The playable scenario: "The Counting-House"

On the spine fixture (`governance_spine.yaml`, `faction x`; no canon person or place), one settlement
(`lr_settlement_a`) gains: a counting-house and a rival house (two buildings with head seats, stores
stocked in grain and salt), a guildhall with a roll seat (eight enrolled, by warrant), three council
seats by lot from the roll (`term: 4`, `cooling_off: 4`, `audit_at_exit: exit_audit`), and the
settlement's Mayor short of grain before the harvest. Two factors are sworn to the player's house.

- **Entry**: `harness/play_surface.py` with the player-proxy as the counting-house's head; headless, the
  same seat through the one chooser.
- **Choice surface** (the ordinary aperture, nothing bespoke): lend (to whom, what kind, how much,
  payable where); pay upkeep or let a client lapse; seek enrolment; canvass before a ballot; present a
  bond, extend it, sue on it, hand it on; tell.
- **Legibility**: every roll's term list (SC-P1) names `obligation`, `evidence`, `regard` where they
  applied; the chronicle shows `lot.seen`, `debt.lapsed`, `tenure.closed` by term.
- **Stakes**: the chest (conserved stores), the roll, the council.
- **Endings** (read by the harness, scored by nothing): a majority of the council's members hold a live
  obligation to the house (it rules from behind); the house's bonds lapse while its own fall due (it
  fails); the head carries a `ban` under the council's purview (barred); or twelve seasons pass.
- **One code path**: the registered modules and the season loop; the fixture adds data only.
- **First cut** (needs A and B only): the Mayor, one loan, one harvest, one reckoning.

## Exact edits, by owner (summary)

1. `engine/season/harness/populated.py::resolve_anchor`: the `venue` form.
2. `engine/season/offices.yaml`, `rosters.yaml` (`office_bodies`, `factions.head_seat`),
   `arrangements.yaml`: the rows of §4.
3. The MATERIAL lane's rate roll: the `charter` term; `venues.yaml` market rows: `standard`.
4. `engine/season/governance_spine.yaml` (or a sibling fixture file the spine loader reads, FA-P4's
   shape `[UNVERIFIED: 06_FA_playable_scenario.md not opened]`): the scenario's rungs, seats, stores.
5. `engine/season/harness/`: one reading script, `counting_house.py`, printing per seed and season the
   council's holders, each house's obligees and bonds, the largest share of the council obliged to one
   person, and the ending reached; output only, no assertion that a story occurs.

## Gate (execution artifact)

- `resolve_anchor`: a row with a `venue` anchor seats on the named hearth; a row naming an unknown
  building is refused at build.
- Scenario, headless, seeds 0–2, twelve seasons, `PYTHONHASHSEED=0`: the reading above, with the control
  arm `obligation_step: 0` and no `debt` kind. **Reported, not asserted**: which ending each seed
  reaches. **Asserted**: stores conserved; every council holder was on the roll and outside his
  cooling-off; at least one roll in the run carries a non-zero `obligation` term at the live arm and none
  at the control; the three seeds are not identical in the council's sequence of holders.
- Content: a realm built with the foreign cast seats Schoenland's rows; `queries/faction_q.py::head`
  answers a person for Schoenland's Proposition; the realm's pre-item hash is unchanged with the rows
  absent.

## Falsifier

- A scripted ending: if any ending is reached at the control arm with the same frequency and by the same
  chain of acts as at the live arm, the scenario shows nothing about obligation; the reading prints both
  arms side by side so this is visible.
- Planted: stock the rival house only; the player's house must not be able to lend (conservation).
- Mutation: anchor a head seat on a settlement; clients' upkeep then draws on the town's stores and the
  conservation reading names the wrong rung.

## NERS reading

- **N.** Without a seat on a building, a firm, a bank, a guild chapter and a foreign factory have no
  head, chest or dependants: the family's institutions are unbuildable. Vertical: hearth to realm on one
  seat type. Lateral: the same row pattern is a monastery's prior, a manor's steward, a company's factor.
- **R.** A player founds a house, places a manager abroad, buys or loses a charter, packs a roll. With no
  player, houses lend, lapse, are audited and barred. Complete: a house with empty stores pays no upkeep
  and its clients lapse on the clock.
- **S.** One anchor resolver, one purview rule (one edge deep is already the code's), one arrangement
  loader. The scenario zooms from a hearth's chest to a settlement's council and back on the same loop.
- **E, last.** One anchor form, data rows, one term on another lane's roll, one fixture, one reading
  script. The content is the bulk and is all revertible by deleting rows.

## Cost class

Edit (rows) and small build (anchor form, fixture, reading script). The charter term is held until the
MATERIAL lane's rate roll exists.
