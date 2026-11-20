# COLONIAL-C — the audit at the end of a term and the calling-in of a grant: two arrangement rows, one fixture, and terms on the seats a grant confers

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-12) — the seat-row key is `audit_at_exit: <arrangement id>` (the Venetian lane's, which names its room), not `audited: true`; a form's `confers:` block carries `audit_at_exit: audit`; the occasion is `world_q.audits_due` (this file's: any close of the hold, to a person who holds the `tenure.closed` claim; widened to the Venetian lane's set of who may open). This file's `audit` row is the kit's one audit row. `quo_warranto`, `prescription_seasons` and the closing cell requested of SC stand. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's research (`unified/RESEARCH_MAP_INSTITUTIONS_B.md`; audit §16). No edit of this file's is changed. What changed: (1) the audit row has six more sources than the two themes it cited: the prosecution of returning governors on a ledger of demanded against delivered (`research/governance/political_hierarchy_standing.md:139`); the buyer of an office caught according to how much a rival invests in prosecuting him (`research/rise_to_power_roster_system_research_v1.md:483-486`); **the audit that weakens with distance, and the officer's ally on the reviewing bench** (`:518-521`), which sources edit 2's rule that the opener's `remove` enters the hearing; the three itinerant audits and the inspection as theatre (`.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:118-122`, `:465-469`); the end-of-term audit that bills the appointer (`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:207`); the magistrate laid over a sitting council (`:217`). (2) **`prescription_seasons = 8` is not new:** an archived design wrote the same mechanism with a slope of `floor(charter_age_seasons / 8)` and a public contest past about sixteen seasons (`.designs/systems/settlements/reference/settlement_layer_v30.md:621-625`), and called both uncalibrated (`:642-644`); it is intent and vocabulary, never the reason the value is right, and edit 3's sweep stands. (3) Additions carried elsewhere: the `audit` row's Record recites the seat that conferred the audited one (`15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` edit 3); the gate gains a sweep of how often against how hard (`15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` edit 6); `farm` hardens, so edit 3's reader has a second kind of instrument to weigh (grounding F edit 4).

Reconciled: 2026-11-12, U5d closure — folded **A-13**: `audit_at_exit` is a ruled seat fact; a seat declaring none is not audited. No step changes.

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (COL_C: closing arm AMBIGUOUS, fallback stated; `audited` stale), §2 (A-39 row), §7, 7b.0, 7b.7 ("`audited` -> `audit_at_exit`; `quo_warranto` closing arm: take the file's fallback … unless the conferring seat's `revocation` basis reaches"); `U3_CONFLICT_LEDGER.md` C3-C10 (`proof_step` is deleted; a cited Record is a `proofs` level); `U1_OWNERS_AND_VOCABULARY.md` D-U1-11k (`distance`). Changed: the body now follows this file's first `Reconciled:` line (`audit_at_exit: audit`, `world_q.audits_due`; `audited:` removed); `quo_warranto` ships the fallback (`ban` at Overwhelming and Success) and the closing arm requested of SC is withdrawn (where the grantor's seat holds a `revocation` basis over the conferred seat, his own `revoke` is the route, `04` §C.2 T-o); the appeal is on new grounds only (A-39); the gate's control is `proof_level: None`; `remove` → `distance`.

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B33**, after COLONIAL-B (`U3_DEPENDENCY_ORDER.md` §1 item 33). Depends on: `05_SC_acquittal.md` and `05_SC_arrangement_rows_that_bind.md` (B27: SC-P6, SC-P4's band map), `05_SC_obstacle_difficulty_and_modifiers_B.md` (B05), `06_FA_seat_terms_and_turnover.md` (B21, FA-P3), `15_INSTITUTIONS_VENICE_C` (B32, `audit_at_exit` and `audits_due`); CR-60 and CR-61 are v11 plan positions, MISSING until `STAGES.md` step 5 (the realm reading waits on them). Lane tag: FA. Tier: `sonnet` producer, effort `high`; one `opus` read of the 400-and-400 arms. Named test: `engine/season/tests/test_audit_and_charter.py` (as named below). Standing sentences: *Pool* — the bench's `determine` is SC's roll on the one pool rule (A-6, A-7, A-8). *Failure writes* — an audit's Failure is an acquittal, whose quittance is a Record the officer holds and the room witnessed (A-81). *Draw keys* — no draw is added (`determine`'s key is SC's, A-30).

Source: `audits/15_INSTITUTIONS_COLONIAL.md` §2.1, §6.2, §8, §12 batch C-3. Depends on and does not redo:
SC-P4 (`proposals/05_SC_arrangement_rows_that_bind.md`: a band-keyed `disposes:`), SC's hearing reach
(`05_SC_playable_hearing_B.md`; hole row H-254), `05_SC_acquittal.md`, `05_SC_evidence_and_rebuttal_B.md`
(evidence as a weighted, answerable term; **that file's deterministic entry is the SC lane's to repair
under the standing rule; this file uses only the item weight that enters the roll as `proofs` levels, C3-C10**), SC-B (the obstacle
form), FA-P3 (`06_FA_seat_terms_and_turnover.md`: `term:` on an `offices.yaml` row), FA-P1
(`06_FA_decree_binds.md`: the recall occasion; it names "the Recall as a scene" and "`Submit to audit`"
as not built: this file is those two). Nothing is ratified by being written.

## What it changes in `engine/season/` at runtime

1. `open_case` may docket a matter under two new arrangement rows, `audit` and `quo_warranto`. A
   `determine` under either **rolls**, as every `determine` does, and opens what its band names.
2. Under `quo_warranto`, an instrument whose form `hardens` weighs more as a cited item (`proofs` levels)
   the longer it has been held.
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
    appeal_basis:       determine       # admitted on new grounds only (A-39)
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
    appeal_basis:       determine       # admitted on new grounds only (A-39)
    interposed:         [person, procedure, document]
    order:              rank
    proofs:             [record, testimony, oath]
    standard:           demanding
    disposes:           {Overwhelming: ban, Success: ban, Partial: oblige}   # the fallback, taken
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
  Success → a `ban` on the holder from that one seat (FA-P3's scoped ban bars him from the conferred seat
  and its like), **the file's own fallback, taken** (`R4_READ.md` 7b.7). `release` is not a `disposes:`
  value (the enum is `<tenure kind> | Record | none`, `arrangements.yaml:27-28`) and no listed gate basis
  lets a bench close a `hold` (`04` §C.2), so the closing arm once requested of SC is withdrawn. Where
  the grantor's own seat holds a `revocation` basis over the conferred seat (T-o, `04` §C.2), the
  calling-in can also be his `revoke`, an act with its own draw (BINDING-C); the bench is the route when
  it does not. Partial → the grant stands for a fee: an `oblige` whose `due` is one `transfer.made` to
  the grantor's rung. Failure → the grant stands; the docket's closing Record is the holder's evidence
  in any later calling-in.

**2. Who may open, and where** — no new predicate; three facts already asked:

- `open_case` is `remit:determine` (`verb_table.yaml`). An `audit` is opened through a seat whose purview
  reaches the audited seat's rung; the bench is `judging_set`'s. **The opener's `distance` from the
  audited ground enters every `determine` and `speak` in the hearing** (`…_B_distance.md`; OBS member 20), so an audit
  held from the capital is a weaker instrument than one held on the spot, and the inspector is a man
  `dispatch`ed there who holds a `determine` seat (the *visita*; the Carolingian *missus*).
- The occasion: `world_q.audits_due` (SYNTHESIS-A §4; X-12), `world_q.vacancies`' sibling. When a
  `hold` on a seat whose row carries `audit_at_exit: audit` closes (term matured, revoked, released,
  died), for a person who holds the `tenure.closed` claim and may open (VENICE-C §4's set), the departed
  officer and the arrangement ride his question as `Party` referents, read when read. He may open the
  audit, or not: a successor who needs the old governor's friends often does not.
- `offices.yaml`: the seat-row key is `audit_at_exit: <arrangement id>` (A-13; X-12), not `audited:`.
  A form's `confers:` block carries `audit_at_exit: audit` into the established seat (SYNTHESIS-A §1),
  and it is proposed for `off_lord_treasurer` (BYZANTINE-GROUNDING item 1), `off_royal_marshal`,
  `off_military_commander_hm` `[ASSUMPTION; content; Jordan to correct]`.

**3. `engine/season/data/fixtures.py: prescription_seasons = 8`** (seasons per unit of item weight;
sweep {4, 8, 16}; NUMBER row, graded `assumption`). Reader: where SC's evidence weight function weighs a
cited Record (an item entering the roll as `proofs` levels, C3-C10) that is a `dispensation` whose form
has `hardens: true`, its weight is
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
  bands**. Control: `proof_level: None` (OBS §3; `proof_step` is deleted) equalises the arms within
  sampling.
- **Age is odds, not outcome.** Under `quo_warranto`, the same instrument held 0 seasons and 16 seasons:
  400 rolls each; the older arm's Failure share (the grant stands) is higher; both arms contain a band in
  which the grant falls.
- Distance: the same audit determined at `distance` 0 and at `distance` 3: shares differ in the direction
  of the term.
- Appeal (A-39): an appeal of an `audit` verdict naming no new ground is refused; one naming an excluded
  testimony is admitted.
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
- **E, last.** Two rows and one fixture; the seat key is A-13's `audit_at_exit`. No code beyond the
  evidence weight's one clause: the calling-in ships on the existing `ban`.

## Cost class

Edit (rows, fixture, key); the closing arm once requested of SC is withdrawn.
