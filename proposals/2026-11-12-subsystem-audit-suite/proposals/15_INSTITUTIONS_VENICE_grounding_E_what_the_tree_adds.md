# INST-VENICE-E (grounding) — what the tree's own research adds to the merchant-republic kit: thirteen mechanisms on existing owners

## Status: PROPOSED (an executable plan for a later session; not ratified by being written, CLAUDE.md §2)

Source: `audits/15_INSTITUTIONS_VENICE.md` §17 (the re-grounding of 2026-11-12) and
`unified/RESEARCH_MAP_INSTITUTIONS_B.md` §2.1, §4 (rows M-1 to M-13). Batch E of that audit's plan.
Depends on and does not redo: this lane's proposals A to D; `15_INSTITUTIONS_COLONIAL_A_instruments.md`
with `15_INSTITUTIONS_SYNTHESIS_A_one_kit.md` edit 1 (the registry `engine/season/instruments.yaml`, its
`forms:` rows and readers); `15_INSTITUTIONS_COLONIAL_C_audit_and_charter.md` (the arrangement row
`audit`); FA-P2 and FA-P3 (`06_FA_remit_grant_by_row.md`, `06_FA_seat_terms_and_turnover.md`).

Short names for sources as in the map: `CGR`
`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md`; `PMP`
`.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md`; `PHS`,
`GM`, `CPS` the three files of `research/governance/`; `PGS`, `HCC`, `RTP`, `FASE` the proactive,
historical-concerns, rise-to-power and precedent research files. All of it is tier 3: it says what
institutions did, and is never the reason a behaviour is correct (CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime

**With every row of this batch absent, nothing: the world hash equals the post-D hash.** With the rows
present: one more form in `instruments.yaml` (`condotta`), one more arrangement row (`guild_debt_suit`),
one content key read on the `audit` row's Record (`recites` gains the conferring seat), and content rows
in `offices.yaml`, `rosters.yaml: office_bodies` and `arrangements.yaml`. No verb, no obstacle term, no
tenure kind, no Record kind, no stored social quantity, no MATTER pass. Every consequential outcome
touched here is already a draw under proposals A to D (the ask, the ballot, the suit, the audit); this
batch changes who sits where and what documents they hold, which is to say the odds.

## The problem (evidence)

1. The Venice lane wrote the sea state, the Arsenal, the bank, the captains and the guild from memory
   and marked them `[M]`. The tree held sources for most of it (map §0 item 1), and those sources
   describe mechanisms the design does not carry. The lane's own E-4 records the skip.
2. Three of the missing mechanisms were found **by play** to be wrongly cut from an earlier pass: the
   stress run reproduced the Sforza seizure "with no resolver to cover it", found the negotiated cap of
   the submission pact wanting in four seeds of seven, and found the roving audit's independent record
   wanting in two (`.audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:146-148`).
   That is the only execution evidence in this file, it is from a retired model (the 2026-07-12
   settlement stress run), and it is cited as a reason to look, not as a result about this engine.
3. Proposal D already has the rector "split by row as FA-P2 allows" (D §2) and his books as "a `survey`
   Record he `give`s upward" (D §1). It authors neither as a pair on one place, gives the subject place
   no pact, and gives the audit no memory of who appointed the man. Those are the gaps.

## The resolution, decided

Thirteen items in seven edits. Each item: source; who acts, by what verb, what is written, who reads it.

### Edit 1 — the paired officers, near and far (M-1, M-2) · `engine/season/offices.yaml` · content

Source: `PMP:138-140`, `:513-516` ("the governor is split into two rivalrous offices so that neither can
defect alone"); `PGS:148`; `CGR:99` (fixed terms, no self-succession, contact with subjects restricted);
`CGR:102` (near provinces a civilian under oversight, far ones a combined governor).

On every subject settlement where D authors a rector, **two** rows on the same anchor, both
`conferral: appointed`, `revocation: rung_above_in_holdings`, `term: 8`, `cooling_off: 8`,
`audit_at_exit: audit`, each holding a `commission` (the kit's form):

```yaml
- id: off_<place>_justice        # post label is Jordan's (names_index); functional here
  remit_acts: [open_case, determine, issue]
- id: off_<place>_captain
  remit_acts: [dispatch, convene, requisition]     # the garrison and the purse
```

Remits are disjoint by construction (the loader already refuses nothing here; the convention is content).
**Near and far** is a convention on the author, stated once in the file's header comment and enforced by
nothing: a place whose conferring seat stands one territory hop away gets the pair; a place farther off
(Schoenland's line seat, any seat beyond a border) gets one row holding both remits. No reader. The
combined seat is the stronger one and is what the colonial lane's "over-mighty warden" reading watches.

What is written and read: each officer's `tell` to the conferring seat's holder is his own claim; the
centre's ledger holds two accounts of one place. Nothing reconciles them.

### Edit 2 — the submission pact (M-3) · `engine/season/instruments.yaml: seeded` · content

Source: `CGR:94` (*dedizione*: statutes, exemptions, guild privileges and councils preserved for loyalty
and appellate supremacy); `PMP:508-511` ("conquest should produce a negotiation, not a colour change");
`CPS:314` (the cities opened their gates when a defeat met a prior deficit of consent).

No new form. The subject commune's head seat holds, at build, a seeded Record of the kit's existing form
`capitulation` (terms on which a place was given up) made by the superior's seat, whose `forbears`
clauses bind the grantor: `tenure.closed` by `revoke` and `tenure.opened` by `confer` over the commune's
own seats, and `requisition.taken` over the place. The colonial lane's readers do the rest: a rector who
levies inside the pact is rolled as any levy, is witnessed, and stands as a breach in the commune's
members' `kept` (`audits/15_INSTITUTIONS_COLONIAL.md` §4.2: "an immunity is not a wall"). One row in `seeded:` per subject commune D
authors; `grade: assumption`.

### Edit 3 — the appointer answers; the inspection is seen (M-4, M-5) · `arrangements.yaml` row `audit`; the document mint · small build

Source: `CGR:109`, `:207` (the end-of-term *sindacato* "bills the appointing faction's Legitimacy, not
just the podestà"); `PMP:119`, `:465-469` (the syndics travel as a visible company and proclaim their
arrival: "the inspection's legitimacy effect on the inspected population is separate from, and often
larger than, its informational effect").

- **The recital.** The Record the `audit` row mints at Partial (the admonition), and the `ban`'s or
  `oblige`'s opening claim at Success and Overwhelming, carry in `recites` the id of the seat through
  which the audited hold was conferred, read from the hold's own opening Event (`tenure.opened`'s
  `via`) `[UNVERIFIED: that a conferral's opening Event carries the conferring seat in a field the mint
  can read; if it does not, the recital reads the audited seat row's `revocation` basis and names the
  seat that basis resolves to, which is the same seat for every appointed row]`. One line where the
  row's disposal builds the Record's content (owner: the single document mint,
  `loop/effects_information.py::_mint_document`, as COL-C uses it). `recites` is the kit's existing
  content key (SYN-A edit 1); this is its fourth use.
- **Who reads it.** Nobody by rule. A person who holds the Record holds a deed of the appointer's
  (he seated a man the bench condemned); `person_q.deeds_judged` values it as it values any deed. The
  appointer's next `confer` is asked of people who think less of his judgment.
- **The inspection as theatre** is a reading, not an edit: COL-C's row already sits on the governed
  ground with `floor: open`. The gate below reports the governed cohort's regard for the conferring
  seat's holder before and after a sitting, against a control row with `floor: sealed`.

### Edit 4 — the secretary order and the standing report (M-6, M-7) · `offices.yaml`, `rosters.yaml: office_bodies` · content

Source: `PHS:362` (the citizens "drafted and often substantively conducted diplomacy that patrician
ambassadors … merely fronted"; the Grand Chancellor "elected for life … the single highest office
structurally open to a non-noble"); `PHS:341-343` (three orders, each with a ceiling); `CGR:96`;
`PMP:150-152`, `:459-463` (the report is cumulative, inherited, and "itself stealable").

- One roll seat `off_<republic>_citizen_roll` (`binds: members_by_warrant`, `remit_acts: [issue]`),
  distinct from the council's roll. One body `"Chancery"` in `office_bodies`. Two secretary seats on it:
  `conferral: appointed` by the head seat, **no `term`**, `eligible_from: off_<republic>_citizen_roll`,
  `remit_acts: [issue]`; and `eligible_from` on every council seat stays the council's roll, so a
  secretary can never be drawn for one. That is the ceiling, and it is two existing keys.
- The college's written menu (audit §1.4) is `issue`d through a secretary's seat: the drafter is not the
  proposer. No mechanism: `Act.via` already names the seat.
- **The standing report.** The `commission` form's `due` (`record.given every 4, to: grantor_rung`,
  SYN-A) is the report. This edit states what the Record is and where it rests: a `survey` product of
  the place, `give`n to the Chancery's rung, where the secretary holds it with its predecessors. The
  successor may be `give`n it; a held report of a place is an `evidence` item on his graded acts there
  (the colonial lane's levy and order rows already read a held assessment). It fades as every claim
  fades (`01_CORE_claim_fade_as_read.md`); it can be seized, concealed, forged (FI's verbs).

### Edit 5 — the contract in phases; arrears; the works' wage (M-8, M-9) · `instruments.yaml: forms`; `offices.yaml` · small build + content

Source: `CGR:110`, `:208` and compendium `tier3:103` (*Ferma → Aspetto → Lapsed*: bound, then a reserve
at reduced pay in which the captain may be poached, then non-aggression); `HCC:67` (unpaid three
seasons, the garrison sacked its own host, and every settlement that heard of it trusted garrisons
less); `FASE:192-196` (the army is paid whether or not the muster prospers); `CGR:91`, `:198` (the
state yard's wage liability "fires every season regardless of use").

```yaml
  - id: condotta                # a hired captain's contract with an employer's seat
    made_by: covenant
    grantor_act: dispatch       # the employer's seat must be one that can send men
    term: 4                     # the bound stage, in seasons
    renewal: grantor            # the employer's option opens the reserve stage
    due:
      - {by: grantor, kind: transfer.made, every: 1, to: grantee_rung}     # pay; half in the reserve stage
    forbears:
      - {by: grantee, kind: duty.taken,     over: named}        # bound stage only: no second employer
      - {by: grantee, kind: march.declared, over: grant_ground} # for `term` seasons after lapse
    lapse: stands
    hardens: false
    grade: assumption
    source: "15_INSTITUTIONS_VENICE.md §17.2 item 8; CGR:110, :208"
```

The captain's side is his own `oblige` to the employer's seat, as D §1 has it. **The one build:** a
form's clause may carry `stage: <n>` (default: every stage), read by `world_q.clauses_binding` against
the Record's current stage (`Record.stages`, matured at MATTER, exists). With it, the second `forbears`
row binds after the last stage and the first does not bind in the reserve stage: an offer taken there is
no breach. If the key is refused, the fallback is two forms (`condotta`, `condotta_reserve`) and a
`covenant` at the turn; the story survives, the single document does not.

**Arrears** need no edit: the employer's missed `due` is a breach in the captain's `kept`; his `release`
then costs him no regard (`audits/15_INSTITUTIONS_COLONIAL.md` §4.2, reader 3), and a released company's
next acts are the chooser's:
`oblige` elsewhere, or `requisition` at the settlement he resides in.

**The works' wage**: the yard seat D authors carries `upkeep: 2` (twice the fixture default; sweep {1,
2, 3}; owner the row), so its establishment is the costliest standing charge on its chest.

### Edit 6 — the pledge; the merchants' court (M-10, M-11) · `arrangements.yaml` · content, and a gate with no edit

Source: `HCC:161` (the loan for the imperial election bought "a Debt tag AND a Concession tag — mining/
extraction rights transferred"); `CGR:190` (a loan "secured against a named extractive right");
`CGR:117` (the guilds "jointly funded a dedicated merchant court with its own enforcement arm");
`GM:201-202` (two courts with overlapping jurisdiction produce forum-shopping).

- **The pledge is composed and needs no edit.** At the making of a `debt` the debtor `give`s the creditor
  a bearer instrument he holds; at discharge the creditor `give`s it back. D-5 holds: there is no lien
  and no creditor verb; possession is the security. A creditor who keeps it after the debt is met
  (proposal B's `debt_state: met`) holds what he was `give`n: recovery is the debtor's suit, with his
  own discharging `transfer.made` as his evidence. The
  chooser must be able to *form* the pair, which is `14_VERBS_SOCIAL2_A`'s formation rule (an act forms
  on what the actor holds and knows); this edit adds a gate that it does.
- **The merchants' court.** One row beside proposal B's `debt_suit`:

```yaml
- id: guild_debt_suit           # the same matter before the guild's own bench, in its own hall
  # every key as proposal B's `debt_suit` (opened at 15_INSTITUTIONS_VENICE_B edit 6), except:
  venue_min_rank:  hearth       # sits in the guildhall, not the town's court
  disposal_reach:  body         # the judgment is heard by the guild, not the settlement
```

  The thirteen keys have no key that names a bench by body; a bench is `bench_basis: determine` read at
  the venue. So the guild's bench is the `determine` seats that sit at the guildhall: the row needs one
  guild seat with `determine` in its remit anchored there (`rung: {venue: "<guildhall>"}`, D's anchor
  form), which this edit adds beside D's `off_house_*` rows. `[UNVERIFIED: that the judging set at a
  hearth venue leaves out the commune's `determine` seats, whose purview contains that hearth by
  containment (`state/gate.py::judging_set`, not opened by this pass). If it does not, the two benches
  have the same members and this row is held until SC's venue work can tell them apart.]` Either bench
  may be asked by `open_case`; where the members differ, `regard` and `obligation` differ. The debtor
  who owes the guild's own Comptroller wants the town's court.

### Edit 7 — the outside assent; the body of the excluded (M-12, M-13) · `arrangements.yaml`, `offices.yaml`, `rosters.yaml` · content

Source: `CGR:97` (Venetian guilds govern themselves, and no statute of theirs takes force without one
magistracy's ratification); `CGR:129`, `:223` (a ratified entry rule can lock an exclusion in as the
town's policy); `CGR:98`, `PGS:81` (a brotherhood for those shut out of the ruling roll, with its own
ladder and chest, "a release valve").

- **The outside assent is composed, on one condition of anchoring.** A guild's statute is an `issue`
  through its head seat. Where that seat is anchored at the guildhall (a `hearth`, D's `{venue: …}`
  form), its purview is the hall and, one edge deep, its sworn members (`purview_reaches`): the statute
  addresses members only. To bind the town it must be `issue`d through a seat whose purview contains the
  town, so the guild's head `petition`s the commune's justice seat (edit 1) and that holder's answer
  (issue it, issue it altered, refuse) is the ratification: an ask, rolled, with `obligation` and
  `regard` as its terms. No row and no key. **The condition:** D anchors `off_guild_roll` at
  `{duchy: "Hafenmark"}`, whose purview by containment is every Hafenmark settlement; a statute issued
  through *that* seat needs no assent. This edit therefore asks one content decision of D's rows: the
  guild's **rule-making** remit (`issue`) sits on the hall's head seat, and the duchy-anchored roll seat
  keeps only the warrant. `[ASSUMPTION; Jordan or FA to correct: it narrows a remit D authored.]`
- A brotherhood: one `community`-rung body in `office_bodies` (`"Brotherhood"`, faction as its town's),
  a roll seat by warrant, a head seat `conferral: elected`, `term: 4`, `eligible_from` its own roll,
  `remit_acts: [issue, convene]`, an establishment and a chest as any house. Three rows. Nothing ties it
  to the council; that is the point.

## Exact edits, by owner (summary)

| # | file (single owner) | edit | class |
|---|---|---|---|
| 1 | `engine/season/offices.yaml` (FA) | paired officer rows on each subject place D authors; one combined row for a far seat; header comment stating the convention | edit |
| 2 | `engine/season/instruments.yaml: seeded` (kit) | one `capitulation` Record per subject commune | edit |
| 3 | `engine/season/arrangements.yaml` row `audit` (SC/COL-C) and the mint | `recites` the conferring seat | small build |
| 4 | `offices.yaml`, `rosters.yaml: office_bodies` | citizen roll, `Chancery`, two secretary seats | edit |
| 5 | `engine/season/instruments.yaml: forms`; `data/instruments.py`; `queries/world_q.py::clauses_binding` | form `condotta`; clause key `stage` | small build |
| 5b | `offices.yaml` | `upkeep: 2` on the yard seat | edit |
| 6 | `arrangements.yaml`; `offices.yaml` | row `guild_debt_suit`; one guild seat with `determine` at the hall | edit |
| 7 | `offices.yaml`, `rosters.yaml` | the guild's `issue` remit on its hall seat only; the brotherhood's three rows | edit |

Order: 2 and 5 after COLONIAL C-1; 3 after COLONIAL C-3; 1, 4, 6, 7 after this lane's D. One batch
(shared files `offices.yaml`, `arrangements.yaml`).

## Gate (execution artifacts, each with a control; `PYTHONHASHSEED=0`)

1. **Control (the whole batch):** with batch E's rows absent, `build_realm(0)` and a one-season run hash
   EQUAL to the post-D hash.
2. **The pair:** a spine fixture with one subject town, seeds 0 to 2, eight seasons, the chooser in both
   seats. Report per season the claims each officer `tell`s the conferring seat about the town and
   whether any pair has opposite content; report the centre's next act toward the town. Control: the
   same town with one combined officer. **A reading, not a pass mark;** it fails as an instrument if the
   two arms print the same lines.
3. **The recital:** a hand-built `audit` sitting forced to Partial; the minted Record's `recites` holds
   the conferring seat's id; `deeds_judged(p, conferrer)` for a person given the Record differs from the
   same person without it. Planted failure: drop the recital and the two values are equal.
4. **The contract:** a hand-built fold over three stages: in the bound stage a rival `oblige` deposits a
   breach in the employer's `kept`; in the reserve stage it does not; after lapse a `march.declared` on
   the employer's ground does. Planted failure: remove `stage` from the first `forbears` row and the
   reserve-stage case deposits a breach.
5. **The pledge:** on the Counting-House fixture, seeds 0 to 2, twelve seasons, count `debt` mintings in
   whose season the debtor `give`s the creditor a bearer instrument. The gate is that the count is
   reported and that at least one hand-built case folds (given, discharged, returned; given, lapsed,
   kept). If the seeded count is zero in all seeds, that is recorded as a formation gap for the SOCIAL
   verb lane, not hidden.
6. **Forum:** 400 seeded `determine` draws of one hand-built suit before each bench; the band shares
   differ and both have spread.

## Falsifier

- For "no change with the rows absent": gate 1.
- For "the pair generates disagreement": gate 2 printing identical lines in both arms across the three
  seeds.
- For "the reserve stage is a real window": gate 4's planted failure not reddening.
- For "the research's shape transfers at all": if, on the Counting-House fixture, no chooser in any seed
  ever takes a pledge, hires in reserve, sues in the guild's court or opens an audit, the mechanisms are
  expressible and unplayed, and the finding is about the chooser's candidates (CHAR's
  `02_CHAR_offer_what_can_be_done.md`), not about this batch.

## NERS reading (definitions CLAUDE.md §0.06; E last, as a ratio)

- **N.** Cut the pair and a subject place has one voice to the centre; the disagreement that makes
  governing at one remove a matter of judgment is gone (top-down: the centre; bottom-up: the subjects
  who may petition either officer; lateral: the two officers). Cut the recital and appointment costs the
  appointer nothing. Cut the phases and a hired captain is either bound or free, with no season in which
  buying him is lawful. Cut the pledge and credit has no security but regard. The secretary order and the
  brotherhood are **narrowed**: each holds in one direction only (the excluded man's route up) until a
  scenario shows a second, and they are the first to drop if the batch must shrink.
- **R.** With no player: two reports that differ; a commune that reads its pact when the rector levies;
  a company bought in its reserve season; a yard that drains its chest in peace. Completeness: every
  item degrades to today's behaviour with its row absent.
- **S.** No second ladder, no second obstacle composer, no new clock. The one new key (`stage` on a
  clause) reads a clock that exists. Pauses: none of it runs outside a person's act.
- **E (against what N and R found).** Seven edits, one small key, one recital line, for thirteen
  mechanisms, eleven of them content. The ratio is good because the five parts were the right ones; it
  would be poor if `stage` grew a second use that a second form could not serve.

## Cost class

Edit (content) for 1, 2, 4, 5b, 6, 7. Small build for 3 (one line at the mint and its test) and 5 (one
clause key, one reader branch, the loader's refusal of an unknown stage). Design-first: none. The pledge
(edit 6, first half) costs a gate and nothing else.

## What is not in this proposal, and why

The *commenda*, the merchant galleys, the Monte, the bill of exchange and the bank's partnership form
remain memory-grade (map §3); nothing here is built on them. The Sforza seizure (an obligee who takes
the seat he served) is the colonial lane's `annex` by conquest (COL-D edit 5) and is not redone. A
wealth-threshold ladder, a stored purchaser's tag and a scope counter on the secret bench are refused in
the audit's §17.2.
