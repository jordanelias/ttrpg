# INST-VENICE-D — houses, rectors, charters; the content rows; and the playable scenario "The Counting-House"

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-10, X-11, X-12, X-15, X-32) — what §3 calls a charter (a trade privilege at a named market) is the form `staple` of `engine/season/instruments.yaml`; `charter` in the kit is a body's self-rule; no obstacle term `charter` is asked of the MATERIAL lane: a held live `staple` cited on an `exchange` is an `evidence` item; a rector's commission is the form `commission`; the row `exit_audit` is not added and every `audit_at_exit: exit_audit` below reads `audit`; `enrolment_ballot` and `security_bench` are tallied by the one rule for `declared` rows; the scenario is a case file with `base: spine` read by the one report (`15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` §1), so `counting_house.py` is not written, and its first cut (one loan, one harvest, one reckoning) is the first cut of the integrated playable. The `{venue:}` anchor, the house, the branch, the content rows and the scenario's seats and endings stand. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's research (`unified/RESEARCH_MAP_INSTITUTIONS_B.md`; audit §17). What changed: the rector, the Kontor, the house's branch, the hired company and the yard, written here from the audit's memory, are now sourced in the tree (`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:87-117`; `research/proactive_governance_scale_research_v1.md:23`, `:76`, `:78`; `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:138-140`). The sources add content this file lacks, carried by `15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` and not by edits here: §2's rector "split by row" becomes **two rows on one place** with a combined row only for a far seat (edit 1); each subject commune holds **a submission pact** (edit 2); a **citizen roll and a chancery** of secretaries who hold without a term (edit 4); the yard's `upkeep` (edit 5); a **brotherhood** for those the council's roll shuts out (edit 7). **One cell of this file is narrowed by that proposal, marked there as an assumption:** §4 (ii)'s `off_guild_roll`, anchored at `{duchy: "Hafenmark"}`, keeps the warrant and loses the guild's rule-making `issue`, which moves to the hall's head seat, because a duchy-anchored seat's purview is every Hafenmark settlement and a guild's statute would then bind the town without any outside assent (edit 7). The Kontor's defining feature in the tree, that the host's officer loses jurisdiction over its members (`…proactive_governance_scale_research_v1.md:78`), is what §1's "a building inside another faction's settlement" already produces through purview. The *commenda*, the galley lines and the bank's legal form stay memory-grade.

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (VEN_D), §7 (INCOMPLETE: `exit_audit`; `charter` held on MAT_B), 7b.0, 7b.7 ("`exit_audit` -> `audit`; `charter` term held (MAT_B rate roll)"), §2 (A-44 row: authored persons outside the generated cap); `U3_CONFLICT_LEDGER.md` C3-N19 (34 seats, one on no rung), C3-L9 (the lot and the keys as tables, see VENICE-C), C3-C10 (a held privilege is a level, not a term); `U3_DEPENDENCY_ORDER.md` §6 (`counting_house.py` named but not in the tree). Changed: the body follows this file's own first `Reconciled:` line, which it had not (the `exit_audit` row is deleted; §3 is the `staple` form read as a `proofs` level; §5's script is not written and the reading is the one report's); `conferral: lot` becomes `conferral: elected` with `tables.selection: lot`, and `eligible_from` and `cooling_off` move to their tables; the control arm is `obligation_level: None`; the A-80 reading is added. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "obligee" → "sworn man" in prose (glossary *sworn*).

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B33**, after VENICE-B (`U3_DEPENDENCY_ORDER.md` §1 item 33); the scenario's reading lands with SYNTHESIS-D in **B40**. Depends on: `15_INSTITUTIONS_VENICE_A`, `_B` (B33), `_C` (B32, the tables and the lot), `06_FA_office_capabilities.md` (B04), `06_FA_remit_grant_by_row.md` (B21), `14_VERBS_MATERIAL_B_stores.md` (B12, `exchange`'s draw; §3 waits on it); the WR lane's place for Schoenland (`09_WR_*`, M-ABROAD; the foreign rows wait on it). Lane tag: FA. Tier: `sonnet` for rows and the anchor form, effort `medium`; `sonnet` `high` for the scenario, one `opus` read of its report. Named test: `engine/season/tests/test_inst_ven_d.py` (the anchor gate and the content gate); the scenario's run is `harness/institution.py`'s, quoted in the commit. Standing sentences: *Pool* — every roll is an existing verb's on the one pool rule (A-6, A-7, A-8). *Failure writes* — this file adds no contested row; the scenario's Failures are the verbs' (A-81). *Draw keys* — no draw is added; the lot's key is VENICE-C's (A-30). *Entrenchment* — see the scenario's gate (A-80).

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
3. A held live `staple` (the kit's form for a trade privilege at a named market) is a `proofs` level on
   the draw of an `exchange` at the market it names, once `exchange` draws (MATERIAL-B).
4. One scenario case file, read by the one report (SYNTHESIS-D §1).

Items 1 and 3 with no row or charter using them: hash EQUAL. Each content row is a declared mover.

## The problem (evidence)

- The title ladder is total down to the hearth (`offices.yaml: titles.domains`: "Family Head": hearth)
  and **no seat sits on a hearth or a community** (audit E-1: seats by rung kind territory 17, duchy 10,
  realm 4, settlement 2, and one seat on no rung: 34; C3-N19). The anchor resolver has four forms (realm, duchy, territory, settlement;
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
`conferral: appointed`, `revocation: rung_above_in_holdings`, `term: 8`, `tables.cooling_off: 8`,
`audit_at_exit: audit`, `remit_acts` split by row as FA-P2 allows (a judge's `[determine, issue]`;
a captain's `[dispatch, convene]`), on a `{settlement: …}` anchor the appointing seat's holder holds.
First use: Schoenland's line and yard seats below.

### 3. The trade privilege: a level, not a gate

A trade privilege at a named market is an instrument of the kit's form `staple` (X-10), issued by a seat
whose purview reaches that rung; its validity is in force while `world_q.in_force` says so. **No obstacle
term is asked of the MATERIAL lane** (this file's first `Reconciled:` line; C3-C10): a held live `staple`
naming the `to` rung, cited on an `exchange` by the actor (or held by the seat he is sworn to), is a
`proofs` level for the actor on `exchange`'s draw (`U5c_SC_one_obstacle_form.md` §3). One venue key on
the market's row, a `standard` (SC's `difficulty_levels`) the host faction's seat-holder may raise by
`establish`, stands against every trader there (an embargo is the market's standard raised and its
privileges left to lapse). Trade without the privilege is attempted at worse odds, and its Failure band
forfeits the goods offered to the market's rung (a durable write, A-81). Nothing is refused outright:
under the standing rule a smuggler sometimes gets through. **Held** until `exchange` draws
(`14_VERBS_MATERIAL_B_stores.md`, B12, shape (a) with its `exchange_terms` table; `R4_READ.md` 7b.4):
the draw and its bands are MATERIAL's.

### 4. Content rows (data)

**`engine/season/rosters.yaml: office_bodies`** (only what a seat below needs; the file's own restraint):
`"Commune Council": "Hafenmark"` ("An elected council of a chartered town."), `"Assembly": "Schoenland"`
("Every enrolled citizen. Elects; does not debate."), `"Senate": "Schoenland"` ("Votes on the College's
written opinions; cannot initiate."), `"Security Council": "Schoenland"` ("Secret bench for offences
against the state.").

**`engine/season/offices.yaml: seats`**: (i) `off_house_feldhaus` at the guildhall NPC-007 is homed in
(`npcs.yaml`: `b_s_006_guildhall`), `faction: "Guilds"`, holder NPC-007, beside her existing
`off_guild_comptroller`. (ii) A guild list seat `off_guild_roll` (`{duchy: "Hafenmark"}`, `body: "Guild"`,
`binds: members_by_warrant`, `remit_acts: [issue]`, `conferral: elected`, `term: 4`, vacant at build;
in the tables: `selection: lot`, `eligible_from: off_guild_roll`, `cooling_off: 4`), and
`tables.eligible_from: off_guild_roll` for `off_guild_comptroller` and FA-P2's `off_guild_leader`.
(iii) Three commune council seats on one Hafenmark settlement (`body: "Commune Council"`,
`conferral: elected`, `term: 4`, `audit_at_exit: audit`, `remit_acts: [determine, convene]`; in the
tables: `selection: lot`, `eligible_from: off_guild_roll`, `cooling_off: 4`), vacant at build;
`tables.eligible_from: off_guild_roll` for `off_commune_rep_hm`. (The id `off_guild_roll` keeps its name;
prose calls the membership a list, U1 glossary *roll*.)

**`engine/season/offices.yaml: foreign_seats`** (built only with `foreign=True`, as Altonia's are; needs
a `foreign_cast` row for Schoenland minting one place, WR's): a head (`post` a functional label,
`body: null`, `faction: "Schoenland"`, `remit_acts: [convene]`, `conferral: elected`, `revocation: null`:
elected for life, presides, initiates nothing); two councillors and two sages on `Senate`
(`remit_acts: [issue]`, `conferral: elected`, `term: 2`; tables `selection: lot`, `cooling_off: 2`: the
college that drafts); three on `Security Council` (`remit_acts: [determine]`, `conferral: elected`,
`term: 4`; table `cooling_off: 4`); one advocate (`remit_acts: [determine]`, `body: "Assembly"`: opens
cases on any holder; the suspending officer); one line seat and one yard seat on the rector pattern.
Holders are new cast rows: **nine persons this lane does not name**, authored content outside A-44's
generated cap (`ED-WR-0011`: the cast is closed and authored); U1 counts them with the other authored
additions (`R4_READ.md` §2, A-44 row). `rosters.yaml: factions.head_seat` gains `"Schoenland": <the head's
row id>`.

**`engine/season/arrangements.yaml`**: two rows that dispose kinds existing sites open today.

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

# `exit_audit` is not added (X-12): the audit at exit is the colonial lane's `audit` row
# (`15_INSTITUTIONS_COLONIAL_C` edit 1), named by `audit_at_exit: audit`.

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
stocked in grain and salt), a guildhall with a list seat (eight enrolled, by warrant), three council
seats by lot from the list (`term: 4`, `cooling_off: 4`, `audit_at_exit: audit`), and the
settlement's Mayor short of grain before the harvest. Two factors are sworn to the player's house.

- **Entry**: a case file with `base: spine` (SYNTHESIS-D §1), `play(... situation=<case id>)` with the
  player-proxy as the counting-house's head; headless, the same seat through the one chooser.
- **Choice surface** (the ordinary aperture, nothing bespoke): lend (to whom, what kind, how much,
  payable where); pay upkeep or let a client lapse; seek enrolment; canvass before a ballot; present a
  bond, extend it, sue on it, hand it on; tell.
- **Legibility**: every roll's recorded levels and terms (SC-P1) name `obligation`, `proofs`, `regard`
  where they applied; the chronicle shows `lot.seen`, a bond's matured last stage with `owed > 0` (the
  lapse, read when read; VENICE-B), `tenure.closed` by term.
- **Stakes**: the chest (conserved stores), the list, the council.
- **Endings** (read by the harness, scored by nothing): a majority of the council's members hold a live
  obligation to the house (it rules from behind); the house's bonds lapse while its own fall due (it
  fails); the head carries a `ban` under the council's purview (barred); or twelve seasons pass.
- **One code path**: the registered modules and the season loop; the fixture adds data only.
- **First cut** (needs A and B only): the Mayor, one loan, one harvest, one reckoning.

## Exact edits, by owner (summary)

1. `engine/season/harness/populated.py::resolve_anchor`: the `venue` form.
2. `engine/season/offices.yaml`, `rosters.yaml` (`office_bodies`, `factions.head_seat`),
   `arrangements.yaml`: the rows of §4.
3. No term on the MATERIAL lane's draw (§3: the `staple` is a `proofs` level; held until `exchange`
   draws); `venues.yaml` market rows: `standard`.
4. `engine/season/cases/exercises/INST-VENICE-01.yaml` (a case file with `base: spine`, SYNTHESIS-D §1's
   schema): the scenario's rungs, seats, stores, the tables' rows and its `setup.instruments`.
5. No reading script: `counting_house.py` is not written (this file's first `Reconciled:` line; it is
   not in the tree, `U3_DEPENDENCY_ORDER.md` §6). The readings named here (per seed and season the
   council's holders, each house's sworn men and bonds, the largest share of the council obliged to one
   person, the ending reached) are added as rows of `harness/institution.py`'s report (SYNTHESIS-D §1);
   output only, no assertion that a story occurs.

## Gate (execution artifact)

- `resolve_anchor`: a row with a `venue` anchor seats on the named hearth; a row naming an unknown
  building is refused at build.
- Scenario, headless, `python -m engine.season.harness.institution INST-VENICE-01 12 <seed>` for seeds
  0, 1, 2 (SYNTHESIS-D §1's command; `PYTHONHASHSEED=0`): the reading above, with the control arm `obligation_level: None`
  and no `debt` kind. **Reported, not asserted**: which ending each seed reaches. **Asserted**: stores
  conserved; every council holder was on the list and outside his cooling-off; at least one roll in the
  run carries an `obligation` level at the live arm and none at the control; the three seeds are not
  identical in the council's sequence of holders.
- Entrenchment (A-80): an arm in which every contested act resolves at its control band (positions
  hold); the report prints the count of acts whose question cites a bond, a lapse, a closed list or an
  audit, by season. Expected reading: non-zero in every seed (held positions are referents others act
  on); the count is the story census's instrument (`23_STORY_D`).
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
- **E, last.** One anchor form, data rows, one case file, report rows. The content is the bulk and is
  all revertible by deleting rows.

## Cost class

Edit (rows) and small build (anchor form, case file). §3 is held until `exchange` draws (MATERIAL-B).
