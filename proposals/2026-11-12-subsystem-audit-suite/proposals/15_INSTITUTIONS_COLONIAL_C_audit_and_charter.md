# COLONIAL-C — the audit at the end of a term and the calling-in of a grant: two arrangement rows, one fixture, and terms on the seats a grant confers

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-12) — the seat-row key is `audit_at_exit: <arrangement id>` (the Venetian lane's, which names its room), not `audited: true`; a form's `confers:` block carries `audit_at_exit: audit`; the occasion is `world_q.audits_due` (this file's: any close of the hold, to a person who holds the `tenure.closed` claim; widened to the Venetian lane's set of who may open). This file's `audit` row is the kit's one audit row. `quo_warranto`, `prescription_seasons` and the closing cell requested of SC stand. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's research (`unified/RESEARCH_MAP_INSTITUTIONS_B.md`; audit §16). No edit of this file's is changed. What changed: (1) the audit row has six more sources than the two themes it cited: the prosecution of returning governors on a ledger of demanded against delivered (`research/governance/political_hierarchy_standing.md:139`); the buyer of an office caught according to how much a rival invests in prosecuting him (`research/rise_to_power_roster_system_research_v1.md:483-486`); **the audit that weakens with distance, and the officer's ally on the reviewing bench** (`:518-521`), which sources edit 2's rule that the opener's `remove` enters the hearing; the three itinerant audits and the inspection as theatre (`.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:118-122`, `:465-469`); the end-of-term audit that bills the appointer (`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:207`); the magistrate laid over a sitting council (`:217`). (2) **`prescription_seasons = 8` is not new:** an archived design wrote the same mechanism with a slope of `floor(charter_age_seasons / 8)` and a public contest past about sixteen seasons (`.designs/systems/settlements/reference/settlement_layer_v30.md:621-625`), and called both uncalibrated (`:642-644`); it is intent and vocabulary, never the reason the value is right, and edit 3's sweep stands. (3) Additions carried elsewhere: the `audit` row's Record recites the seat that conferred the audited one (`15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` edit 3); the gate gains a sweep of how often against how hard (`15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` edit 6); `farm` hardens, so edit 3's reader has a second kind of instrument to weigh (grounding F edit 4).

Reconciled: 2026-11-12, U5d closure — folded **A-13**: `audit_at_exit` is a ruled seat fact; a seat declaring none is not audited. No step changes.

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_COLONIAL.md` §2.1, §6.2, §8, §12 batch C-3. Depends on and does not redo:
SC-P4 (`proposals/05_SC_arrangement_rows_that_bind.md`: a band-keyed `disposes:`), SC's hearing reach
(`05_SC_playable_hearing_B.md`; hole row H-254), `05_SC_acquittal.md`, `05_SC_evidence_and_rebuttal_B.md`
(evidence as a weighted, answerable term; **that file's deterministic entry is the SC lane's to repair
under the standing rule; this file uses only the `evidence` term's sign and unit**), SC-B (the obstacle
form), FA-P3 (`06_FA_seat_terms_and_turnover.md`: `term:` on an `offices.yaml` row), FA-P1
(`06_FA_decree_binds.md`: the recall occasion; it names "the Recall as a scene" and "`Submit to audit`"
as not built: this file is those two). Nothing is ratified by being written.

## What it changes in `engine/season/` at runtime

1. `open_case` may docket a matter under two new arrangement rows, `audit` and `quo_warranto`. A
   `determine` under either **rolls**, as every `determine` does, and opens what its band names.
2. Under `quo_warranto`, an instrument whose form `hardens` weighs more as evidence the longer it has
   been held.
3. A seat conferred by a grant carries the grant's term (content; FA-P3's mechanism).
4. With no matter docketed under either row nothing moves (the rows are data; a computed `open_case`
   writes `DOCKET_ARRANGEMENT: None` today, `05_SC_arrangement_rows_that_bind.md` problem 3, and CR-60 /
   CR-61 are the plan's repair). Seeded hash EQUAL until then.

## The problem (evidence)

- Nothing ends a governor's term (`audits/06_FA_audit.md` §0: over three seasons at three seeds no seat
  was conferred, revoked or inherited) and nothing examines one when it ends. FA-P1 builds the recall as
  an occasion and leaves the hearing unbuilt.
- A grant, once made, has no venue in which it can be called in or defended. `revoke` executes or is
  refused by a structural rule (`state/gate.py::REVOCATION_RULES`); the holder's long possession counts
  for nothing, and under the standing rule a revocation that could go either way must go by a draw.
- The research's governor toolkit is convergent across four civilisations
  (`research/fa_se_historical_precedent_research_v1.md` T5: residencia, visita, rule of avoidance,
  Censorate, timar rotation) and its charter findings name prescription and quo warranto (T4). Tier 3:
  shape and vocabulary, never authority.

## The resolution, decided

Ladder step 4: a proceeding is a row (`arrangements.yaml`'s own claim), and SC-P4's band-keyed disposal
is the method for graded verdicts. No verb, no `audit` effect, no stored suspicion.

## Exact edits, by owner

**1. `engine/season/arrangements.yaml`** — two rows, in the thirteen-key shape plus SC-B's `standard:`
and SC-P4's mapped `disposes:`.

```yaml
  # ── audit — an officer answers, on the ground he governed, to those he governed ───────────────
  - id:               audit
    disposal:          bench
    bench_basis:        determine
    floor:              open            # the governed may speak
    records_dissent:    true
    venue_min_rank:     settlement
    term_required:      true
    appeal_basis:       determine
    interposed:         [office, procedure, document]
    order:              rank
    proofs:             [testimony, record]
    standard:           demanding
    disposes:           {Overwhelming: ban, Success: oblige, Partial: Record}
    disposal_reach:      body

  # ── quo warranto — by what warrant do you hold? ───────────────────────────────────────────────
  - id:               quo_warranto
    disposal:          bench
    bench_basis:        determine
    floor:              open
    records_dissent:    true
    venue_min_rank:     duchy
    term_required:      true
    appeal_basis:       determine
    interposed:         [person, procedure, document]
    order:              rank
    proofs:             [record, testimony, oath]
    standard:           demanding
    disposes:           {Overwhelming: release, Success: release, Partial: oblige}
    disposal_reach:      realm
```

Notes on the cells, each `[ASSUMPTION; medium; this lane's; a data edit reverts it]`:

- `audit`, by the band of the **bench's** `determine` on the proposition "the officer misgoverned":
  Overwhelming → a `ban` on the officer (scoped to the banning seat's purview, FA-P3 change 3); Success →
  an `oblige` of the officer to the opening seat, whose instrument is a `tribute`-shaped restitution
  (`15_INSTITUTIONS_COLONIAL_A_instruments.md`; the `due` is a `transfer.made` to the governed ground's
  rung); Partial → a `Record` (an admonition; SC-P4's own note is that a `Record` disposal has no opener
  until a Record disposal site exists [`arrangements.yaml:270-271`], so this cell waits on that site and
  is inert before it); Failure → nothing is opened and `05_SC_acquittal.md`'s quittance is the officer's.
- `quo_warranto`, by the band of the bench's `determine` on "the holder has no warrant": Overwhelming and
  Success → the conferred seat's `hold` is closed. **`release` is not a `disposes:` value today** (the
  enum is `<tenure kind> | Record | none`, `arrangements.yaml:27-28`): a *closing* disposal is a
  new cell value this row needs and SC-P4 does not supply. Stated as the one code dependency this file
  adds to the SC lane: `loop/effects_information.py::_disposal` gains a closing arm for a row whose
  band cell is `release`, closing the `hold` the docketed matter names under the gate's existing
  `determination` closure basis (`arrangements.yaml:198-200` records that arm admitting a bench's
  closure of a `ban`) [UNVERIFIED: that the basis admits a `hold`; if it does not, the row ships with
  `Overwhelming: ban, Success: ban` on the holder from that one seat, which FA-P3's scoped ban makes
  equivalent]. Partial → the grant stands for a fee: an `oblige` whose `due` is one `transfer.made` to
  the grantor's rung. Failure → the grant stands; the docket's closing Record is the holder's evidence
  in any later calling-in.

**2. Who may open, and where** — no new predicate; three facts already asked:

- `open_case` is `remit:determine` (`verb_table.yaml`). An `audit` is opened through a seat whose purview
  reaches the audited seat's rung; the bench is `judging_set`'s. **The opener's `remove` from the
  audited ground enters every `determine` and `speak` in the hearing** (`…_B_distance.md`), so an audit
  held from the capital is a weaker instrument than one held on the spot, and the inspector is a man
  `dispatch`ed there who holds a `determine` seat (the *visita*; the Carolingian *missus*).
- The occasion: `world_q.vacancies`' sibling. When a `hold` on a seat whose row carries `audited: true`
  closes (term matured, revoked, released, died), the closing is a `tenure.closed` claim; for a holder
  of the conferring seat who holds that claim, the departed officer and the seat ride his question as
  `Person` and `Office` referents, by the same stamp FA-P1's `recalls` uses. He may open the audit, or
  not: a successor who needs the old governor's friends often does not.
- `offices.yaml`: a seat row may carry `audited: true | false` (default false; loader refuses another
  value). Set true on every seat an instrument `confers:` (the form carries it into the established
  seat) and proposed for `off_lord_treasurer`, `off_royal_marshal`, `off_military_commander_hm`
  `[ASSUMPTION; content; Jordan to correct]`.

**3. `engine/season/data/fixtures.py: prescription_seasons = 8`** (seasons per unit of evidence weight;
sweep {4, 8, 16}; NUMBER row, graded `assumption`). Reader: where SC's `evidence` term weighs a cited
Record that is a `dispensation` whose form has `hardens: true`, its weight is
`1 + min(3, held_seasons // prescription_seasons)`, `held_seasons` read from the citing party's own
`hold` on the Record (`Tenure.since`). One clause at the single owner of evidence weight
(`05_SC_evidence_and_rebuttal_B.md`'s weight function; until it lands, `world_q.proofs`). The cap is the
`3` in that expression and is the same fixture row's second field (`prescription_cap`, sweep {1, 3, 5}).

**4. Terms.** `instruments.yaml` `confers:` blocks carry `term:` equal to the form's `term`; `_eff_confer`
reads it by FA-P3's rule. Proposed content on existing seats, by FA-B3's table of which seats end on a
clock (`06_FA_seat_terms_by_body_B.md`): none. This file adds terms **only** to seats a grant creates,
so no seat in the built realm changes.

## Gate (execution artifact)

`engine/season/tests/test_audit_and_charter.py` and one seeded reading:

- both rows load; a fourteenth key or a band cell off the enum is refused naming the row.
- **The verdict is a draw.** On a hand-built hearing under `audit` (one officer, a bench of one, three
  residents each holding a firsthand `requisition.taken` claim of the officer's doing): 400 seeded
  `determine` rolls with the three testimonies cited and 400 with none. Printed: band shares per arm.
  Pass: the cited arm's Overwhelming + Success share is higher, **and each arm contains at least three
  bands**. Control: `proof_step: 0` equalises the arms within sampling.
- **Age is odds, not outcome.** Under `quo_warranto`, the same instrument held 0 seasons and 16 seasons:
  400 rolls each; the older arm's Failure share (the grant stands) is higher; both arms contain a band in
  which the grant falls.
- Distance: the same audit determined at `remove` 0 and at `remove` 3: shares differ in the direction of
  the term.
- Realm reading (after CR-60/61 and FA-P3): seeds 0–4, six seasons, with one `farm` seeded
  (`…_E_scenario.md`): the report prints whether an audit was opened at the term's end and its band.

## Falsifier

- Planted: read `held_seasons` from the Record's creation instead of the citing party's hold; a charter
  seized last season by a stranger then pleads its full age, and the hand-built "the seizer cites it at
  weight 1" assertion reddens.
- Planted: force the band to Success; the "three bands" assertions redden.
- A row with no docketed matter moves nothing: seeded hash EQUAL.

## What it does not do

No automatic audit (it is opened by a person or not at all). No suspicion carrier. No rotation rule (a
term is the only clock; the rule of avoidance, service away from one's home ground, is the bureaucracy
lane's if it wants it: a `confer` candidate filter is a chooser term, FA-P6 edit 4). No venal
appointment (audit §11 item 2). No peninsula-wide "revocation echo" modifier: other chartered holders
react because they hold a claim of the verdict and judge the mover by it, each by his own ledger.

## NERS reading

- **N.** Above: a grantor can discipline what he cannot see. Below: the governed have a room in which
  what was done to them counts. Lateral: every other holder of a like grant watches. Without it the
  term's end is silent and a grant is eternal or arbitrary.
- **R.** Choices on every side (open or not; testify or keep quiet; forge the accounts; pack the bench);
  it generates trials with no player; complete at the extremes (no testimony: a default-odds hearing;
  a dead officer: no one to docket).
- **S.** Rows in the one proceedings file; the one `determine` roll; hands back to the season by the
  Tenure its band opens.
- **E, last.** Two rows, one fixture, one seat key, one closing arm requested of SC. The closing arm is
  the only code; if SC declines it the fallback is data.

## Cost class

Edit (rows, fixture, key); one small build requested of the SC lane (the closing arm).
