# PAPACY-C — the ledger of deeds and its keeper: founding instruments at world-gen, and consecration as a hearing that mints a certificate

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-01, X-03, X-05, X-06, X-08) — world-gen Records are rows of `engine/season/instruments.yaml: seeded` (this file's row schema), not a section of `offices.yaml`; a certificate carries `recites` (a list of the deeds it attests, for a seat), not `attests: n`, and its weight is the recited deeds left standing; the order of accomplishment is carried once, as the three founders' seeded deeds (3, 2, 1), so the weights 5, 3, 2 are withdrawn; the Church's archive holds two of the founding papers (the containment charter, form `immunity`, and the first king's consecration), and the two ducal papers are `homage` instruments reciting their founders' deeds in the Chief Parliamentary Clerk's keeping; `person_q.legitimacy` does gain one term, the chain down the seat's holders (`15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`), which answers this file's stated limit and its request for a house carrier (R-17). The `consecration` row, its bands, the goal row, the rule that no house holds its own paper and commemoration as `tell` stand. Every finding below stands.

Re-grounded: 2026-11-12 (audit §15.4 item 11) — no edit of this file changes; two readings are added beside it (`15_INSTITUTIONS_PAPACY_grounding_mechanisms.md` item 6: a reign without the rite; the tainted rite). They are the research's two limits on the claim that the Church's leverage "is that it can decline to": a ruler who took his style "without a Rome coronation", "a deliberate rupture that decoupled imperial legitimacy from papal ratification for good" (`research/governance/governance_modes.md:190`), and a later sentence on the consecrated party's maker, whose "condemnation implied a coronation by a heretic" (`research/social_contest_procedures/02_inquisition_heresy_procedure.md:60`). The Frankish anointing is sourced (`governance_modes.md:142`; `research/rise_to_power_roster_system_research_v1.md:325-328`); a co-signature across two ladders is graded "expressible, unused" in the built predicates (`research/by_lane/NPC_npc_cast.md:78`). The archived design made consecration wait on an off-stage Holy See (`.designs/systems/factions/reference/faction_politics_v30.md:354`); the code has none and this file adds none.

## Status: PROPOSED

Source: Jordan's fixed points of 2026-11-12 (`INSTITUTIONS_BRIEF.md`: nobility by deed; *"royalty by noble
conquest, i.e. the first king had the greatest accomplishment in the secession war, followed by the first
Duke of Hafenmark and the first Duke of Varfell"*); `audits/15_INSTITUTIONS_PAPACY.md` §2, F-PAP-06,
F-PAP-07, §6 row P-3, §12 R-11 to R-13, R-17. Composes on CR-36 (the `resolution` Record kind and the
Record disposal site in `_eff_determine`), SC-P8 and `12_ARCS_cited_evidence.md` (a held Record cited as
proof), `14_VERBS_SOCIAL2_B_a_word_with_content.md` (telling what a held document says). Batch 4.

## What it changes in `engine/season/` at runtime

1. `harness/populated.py::build_realm` mints the Records `offices.yaml: instruments:` lists, each held by
   the holder of the seat its row names. With the section empty or absent: nothing (hash EQUAL). With the
   four rows below: a declared build-hash mover (four Records, four `hold` Tenures, the holders' content
   claims).
2. A `consecration` arrangement row. Hand-built until a computed docket names a row. Under it a
   `determine` at Success mints a `resolution` (CR-36's site); at Partial a lesser one; at Failure none.
3. One goal row for the Church. A declared mover of `goals.yaml`'s seeded goals.

No legitimacy number, no title, no tenure kind, no verb. `queries/person_q.py::legitimacy` is unchanged.

## The problem (evidence)

- Canon: the crown is a *"deed-monarchy, Church-consecrated"*; the ducal houses are *"deed-families"*; the
  presumption is rebuttable; Almud *"has not personally earned the deed-claim"*
  (`canon/03_canonical_timeline.md:78-92`, `:104`, `:117`). Jordan adds the order of accomplishment. No
  file code reads states the order, and canon states it nowhere (audit §2.1).
- `build_realm(0)`: `records by kind: {'works': 2}` (audit E-2). No charter, no attestation, no record of
  any deed before tick 0. The Church's archive (the Cardinal of Temperance's portfolio,
  `rosters.yaml:2282`) holds nothing.
- `legitimacy(p, holder, window)` (`queries/person_q.py:537-563`) sums `p`'s stance toward the holder and
  his pursuits' reading of the holder's deeds among `p`'s recent claims. Claims decay: 34,837
  `claim.decayed` Events in three seasons at seed 0 (E-1). So a deed-founded rank, as the engine computes
  it, lasts as long as the deeds are remembered, and nothing in the world remembers on purpose.
- No edge joins Crown and Church: 0 `oblige` edges to a Church seat (E-2). The *"price the Crown pays"*
  has no carrier.
- The archived design's Consecration Crisis is a threshold on Church Stability
  (`baralta_crown_claim_v30.md`, digest `DG_designs1.md:651`): a fixed function, refused twice over
  (Layer 1's cut of the stored quantity; the standing rule).

## The resolution, decided

**Rank is what persons hold of a person's deeds; the Church is the institution that writes deeds down,
certifies them at a hearing, keeps the writing, and tells it.** Three parts.

### 1. World-gen instruments

`offices.yaml` gains a third section. One row = one Record minted at build, by the one mint
(`_mint_document`'s path), held by the live holder of `held_at`. Unknown keys rejected.

```yaml
instruments:
  - id:      ins_settlement_charter
    kind:    dispensation
    via:     off_king                     # the seat it was issued through
    held_at: off_cardinal_temperance      # the archive
    terms:   {immunity: {territory: "T9"}, forbids: [seize, requisition, arrest, raze]}
    to:      ["NPC-020"]                  # the throne's holder, bound with his officers
    at:      {territory: "T9"}
    source:  "canon/03_canonical_timeline.md:58, :82, :104 (the containment grant, preserved and expanded at the settlement)"
  - id:      ins_roll_valorsmark
    kind:    resolution
    via:     off_confessor
    held_at: off_cardinal_temperance
    terms:   {seat: off_king, attests: 5}
    to:      []
    source:  "Jordan 2026-11-12 (order of accomplishment); canon/03_canonical_timeline.md:78-84"
  - id:      ins_roll_hafenmark
    kind:    resolution
    via:     off_confessor
    held_at: off_cardinal_temperance
    terms:   {seat: off_duchess_hafenmark, attests: 3}
    to:      []
    source:  "Jordan 2026-11-12; canon/03_canonical_timeline.md:90"
  - id:      ins_roll_varfell
    kind:    resolution
    via:     off_confessor
    held_at: off_cardinal_temperance
    terms:   {seat: off_duke_varfell, attests: 2}
    to:      []
    source:  "Jordan 2026-11-12"
```

- `attests` is the Record's weight as a proof, in the unit SC's `evidence` term already uses (item weight;
  `proof_step` per unit). **Only the order 5 > 3 > 2 is Jordan's**; the sizes are
  `[ASSUMPTION; medium; Jordan to correct; sweep {3,2,1}, {5,3,2}, {8,4,2}]`.
- `to: []` on the three rolls: the founders are dead and are no person of the cast. A roll is a proof for
  whoever's petition names the same seat (the heir, a claimant) and cites it while holding it or with its
  holder testifying.
- The rolls sit in the Church's hands, not the houses'. A house that wants its roll in a hearing needs the
  archive's holder to cite or `give` it, a copy (`create_record`, weaker: SC's `subject` term), or
  testimony. That dependence is the Church's standing leverage, and theft, forgery or fire in the
  scriptorium is a political act.
- The charter is the Crown's side of the bargain: an officer who seizes, requisitions, arrests or razes in
  `terr_T9` does a deed the Church's goal (edit 4) acts against. It gates nothing (a decree binds as a
  choice, FA-P1).
- No `oblige` of the King to the Confessor's seat is authored: under the oblige clause
  (`state/gate.py:422-431`) that would put the realm under the Confessor's purview (audit R-13).

### 2. Consecration

```yaml
  - id:               consecration
    disposal:          bench
    bench_basis:        determine
    floor:              open            # a public rite: its outcome is known
    records_dissent:    false
    venue_min_rank:     settlement
    term_required:      false
    appeal_basis:       none
    interposed:         [office, ceremony, document]
    order:              scripted
    proofs:             [record, testimony, oath]
    disposes:           Record
    disposal_reach:      realm
    standard:           demanding       # SC T2
```

The route, all existing acts: the claimant (or his advocate) `petition`s a Church bench, the petition's
`terms` naming the seat; the bench `open_case`s under `consecration`; at the sitting the claimant's side
`speak`s and cites (SC-P8) his deeds and the house's roll; a rival may cite against; a bench member
`determine`s.

| band | effect |
|---|---|
| Overwhelming, Success | a `resolution` with `terms: {seat, attests: n}` and `to: [claimant]`, held by the determiner; `n` = the weight of the cited items left standing |
| Partial | the same with `attests: ceil(n/2)`: a grudging consecration |
| Failure | nothing minted; the matter is dismissed (SC-P6); he may petition again |

Odds: `standard` + `evidence` (his cited items minus the standing answers, T5) + `reception` (the bench's
disposition to him). A claimant with great deeds and a hostile Church, and one with thin deeds and a
friendly one, are both uncertain. Consecration opens no `hold` and gates no `succeed`.

What reads the certificate: (a) the `succession` contest (CR-35) and any deposition motion (CR-37), as a
cited proof; (b) the next consecration of the same seat; (c) whoever `research`es the archive or is told;
(d) the Church's own tellers: a seat-holder holding a living person's certificate has its content claims
and can `tell` them, which is commemoration (audit §2.2 item 3, with its stated limit).

### 3. The Church's goal for its liberties

```yaml
  - id: goal_church_liberties_kept
    org: {faction: Church of Solmund}
    text: the Church keeps its liberties -- whoever a churchman knows to have seized, requisitioned or arrested at Himmelenger
    object: {kind: deed_doers, kinds: [rung.seized, record.seized, requisition.taken, arrest.made]}
    pursuits: {stability: 0.5, doctrine: 0.3, justice: 0.2}
    source: "PAPACY-C; canon/03_canonical_timeline.md:58 (the grant's terms). [ASSUMPTION; medium; Jordan to correct -- the weights]"
```

`[UNVERIFIED: the `kinds:` form has no place filter, so this row as written acts against such deeds done
anywhere a churchman hears of them, which is broader than the charter. The narrowing (deeds whose claim
subject lies under a named rung) is a fourth `deed_doers` form and belongs to `data/goals.py`'s owner; it
is requested, not built here. Until then the row ships OFF.]`

## Exact edits

1. `engine/season/offices.yaml`: the `instruments:` section above; `meta.source` line updated.
2. `engine/season/harness/populated.py::build_realm`: one pass after seats are held: for each row, resolve
   `held_at` to its live holder (a vacant seat: the row is skipped and reported, never re-homed), mint the
   Record through the existing mint with the row's `kind`, `terms`, `to`, `at`, and open the holder's
   `hold`. A loader in `data/` refuses an unknown key, a `kind` off `record_kinds`, a `via` or `held_at`
   that is no seat row, and a field the kind does not declare.
3. `engine/season/arrangements.yaml`: the `consecration` row. (`resolution` in `record_kinds` and the
   Record disposal site are CR-36's; this proposal needs CR-36's site to mint under any `disposes: Record`
   row whose docketed petition names a seat, which is how CR-36 states it.)
4. `engine/season/goals.yaml`: the row above, shipped off until the place filter exists.
5. Cross-lane requests, not edits: to SC-P8's owner, *a cited `resolution`'s weight is its `terms.attests`*
   and *a `resolution` is a proof for the side whose petition names the same seat*; to FA, the house
   carrier of audit §2.2 item 3.

## Gate

- Build: `build_realm(0)` holds four more Records; `ins_roll_*` weights read 5, 3, 2; all four are held by
  the Cardinal of Temperance's holder; his ledger has their content claims. Control: section absent, base
  hash.
- Planted hearing (hand-built, real fold): the heir petitions for consecration to `off_king`. Arm A: his
  side cites `ins_roll_valorsmark` (given him by its holder). Arm B: no roll. Exact odds printed for both
  from the module's distribution: P(Success or better) in A exceeds B; 200 seeds per arm show all four
  bands in both. Arm C: a rival cites a contrary Record against the roll: A's advantage shrinks.
- Planted order: the same hearing for a Hafenmark claimant citing `ins_roll_hafenmark` and a Varfell
  claimant citing `ins_roll_varfell`, same bench and reception: the three exact odds are ordered as the
  rolls are.

## Falsifier

A roll cited under a row whose `proofs:` does not admit `record` and still moving the odds. A consecration
whose outcome is the same in every seed for a given state. A build in which a house's head holds its roll
(the dependence on the archive would be gone). Any reader that treats a `resolution` as opening or gating
a `hold`.

## NERS reading

N: cut the instruments and the realm has no past a person can touch: the fixed point has no carrier, the
deed-monarchy is a sentence in a canon file, and the Church has nothing the Crown needs. Cut the hearing
and a new accomplishment has no way to be recognised except by being witnessed. R: a player can win rank
by deeds and then must get them written; can steal, forge or burn a roll; can be refused; a Church player
chooses whom to attest and whom to preach. With no player a disputed succession turns on who holds which
paper. It fails gracefully: no Record, the hearing still runs on testimony. S: one Record kind (CR-36's),
one disposal site, the SC evidence term, the existing `legitimacy`; nothing is computed twice. E (last):
one YAML section, one row, one goal row; the player's rule of thumb is *deeds must be seen, or written
and kept*.

## Cost class

Small build (edits 1-3); edit (4); the house carrier is design-first and FA's.
