# INST-BYZ-GROUNDING — what the tree's own research adds to the Byzantine design: an ordered plan

## Status: PROPOSED (an executable plan for a later session; ratifies nothing; nothing here is built)

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §18 (the re-grounding of 2026-11-12);
`unified/RESEARCH_MAP_INSTITUTIONS_A.md` §1, §3, §4. Composes on proposals `15_INSTITUTIONS_BYZANTINE_A`
to `_F` as reconciled by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2, and adds no verb, no carrier, no
tenure kind, no stored quantity and no new key: every item is content on a key another proposal
already introduces, a goal row, a reading in the scenario report, or a design-first note.

Research is tier 3 (`research/00_INDEX.md` §1). Each item below cites the file that describes the
mechanism; the citation says why the shape is worth building, never that a behaviour is correct
(CLAUDE.md §0.05). Every figure in the sources is a lead.

## What it changes in `engine/season/` at runtime

| item | change at runtime | when absent |
|---|---|---|
| 1 audit at exit on fiscal and frontier seats | a hearing is docketed when the `hold` on three named seats closes | hash EQUAL |
| 2 the treaty gate's goal | NPC-090 forms `open_case` against persons he knows breached the treaty staple | his present orientation row stands; no case forms |
| 3 readings (five lines in the scenario report) | none: the report reads the log | — |
| 4 the precedent file | none new: a gate that the existing `evidence` term reads an entered instrument | — |
| 5 design-first notes for batch G | none | — |

Items 3 and 4 change nothing at runtime and say so.

## The problem (evidence)

The Byzantine audit wrote §2 largely from memory and marked it so, on the statement that the tree
"has no Byzantine research of its own depth" (§15). The tree holds nine files on the subject (map §1).
Read against them, the design is sound in its primitives and short of eleven mechanisms the research
states with their failure modes (audit §18.4). Four of the eleven need an edit or a gate; five are
stories the scenario report can already show or fail to show; two belong to other lanes. Without
them the court of precedence has honours, pay, hands and distance, and lacks: a consequence when a
fiscal officer leaves; any use for the Kommerkiarios' strictness; a way to see who refused to attend;
and the two endings the research gives the throne-barred servant.

## The resolution, decided, in landing order

### Item 1. Audit at exit on the seats that hold money or a frontier (content; after B)

*Mechanism and source.* An official's account is taken when he leaves: the Venetian review of a dead
doge, with fines "against his estate before his heirs could inherit"
(`research/governance/governance_modes.md:329`); the residencia, in which "the outgoing official
stayed put while a judge collected sworn complaints from the governed"
(`research/fa_se_historical_precedent_research_v1.md:127`); the Ming ledger kept in triplicate
(`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:53`).

*Decided.* Use the kit's one encoding (synthesis X-12: key `audit_at_exit: <arrangement id> | null`,
row `audit`, occasion "any close of a hold on such a row"). This proposal only names the Byzantine
seats that declare it:

```yaml
# engine/season/offices.yaml — added to three existing rows, nothing else on them changes
  - id: off_lord_treasurer      # NPC-037; the fisc of proposal B
    audit_at_exit: audit
  - id: off_katepano            # NPC-089; the frontier post of proposal D
    audit_at_exit: audit
  - id: off_kommerkiarios       # NPC-090; the treaty gate
    audit_at_exit: audit
```

`[ASSUMPTION; medium; Jordan to correct — which seats. Revert: delete the three lines.]` The two
foreign seats are audited by the far superior's seat (`off_altonian_court`, synthesis X-13), which
is who "may open" under X-12's rule; whether that seat's holder does is his own choice.

*What is drawn.* The hearing is X-12's `audit` row: graded verdicts, the SC lane's obstacle, the
departed holder's `requisition` and `transfer` Events as `evidence`. Nothing here adds a term.

*Depends on.* `15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md` or `15_INSTITUTIONS_COLONIAL_C_audit_and_charter.md`
landing the key and the row (whichever the synthesis's plan schedules first); proposal B for a
treasurer who has collected anything.

*Gate (execution artifact).* On the `roga` case file (proposal F), seeds 0 to 199: plant a `revoke`
of the treasurer in season 4. Read: a matter docketed under `audit` naming her in every seed in
which the `revoke` closes the hold; verdict bands over seeds, none empty and none above 0.9; in the
arm where she collected nothing, the `evidence` term reads 0. *Control:* the three lines absent,
`content_hash` equal to proposal F's own run.

*Falsifier.* If the audit is docketed in a seed where the hold did not close (the `revoke` drew
Failure), the occasion is wrong. If the verdict distribution is the same with and without recorded
collections, the hearing reads nothing and the item is decoration.

*Cost.* edit (content), once X-12's key exists.

### Item 2. The treaty gate breeds its own offence (goal row; after D and the kit's `staple` form)

*Mechanism and source.* The one fragment of the Eparch proposal the tree kept after cutting the
rest: "foreign-merchant channeling → smuggling"
(`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:157`, `:328`;
`.audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:149`, `:319`).

*Decided.* The Kommerkiarios' goal today is an orientation that "mints no Proposition"
(`engine/season/goals.yaml`, `goal_kommerkiarios_treaty_order`). It gains a sibling of the shape the
Inquisitors' and the Riskbreakers' rows already use (`object: {kind: deed_doers, …}`,
`goals.yaml:117`, `:129`, `:144`):

```yaml
  - id: goal_kommerkiarios_side_roads
    org: {seat: off_kommerkiarios}
    text: the Kommerkiarios acts against whoever he knows to have traded past the treaty's gate
    object: {kind: deed_doers, kinds: [<the breach kind of the treaty staple>]}
    pursuits: {stability: 0.6, justice: 0.3, wealth: 0.1}
    derives: {from: goal_kommerkiarios_treaty_order, kind: establishes}
    source: >-
      INST-BYZ-GROUNDING item 2. [ASSUMPTION; medium; Jordan to correct -- the weights and that the
      strictness is a goal at all. Revert: delete the row.]
```

The kind in angle brackets is **not invented here**. It is the Event kind the kit emits when an
instrument of form `staple` is breached (synthesis X-09, X-10: `breaches` over forms; the form is
`15_INSTITUTIONS_COLONIAL_A_instruments.md`'s). The executor reads that proposal's emitted kind and
writes it; the loader refuses a kind outside `data/verbs.py::DEED_KINDS`, which is the check that it
exists.

*Gate.* Hand-built on the realm with `foreign=True`: one person holds a claim of a breach by a
merchant; the Kommerkiarios is told it. Over 200 seeds his chooser forms `open_case` against the
merchant in some seeds and not all (his `stability` and `altonian_civics` set the ranking; the
sample decides). *Control:* the row absent: no such case forms in any seed.

*Falsifier.* The case forming in every seed (a trigger, not a person), or forming against persons
he holds no claim about.

*Cost.* edit. *Depends on.* proposal D; the kit's `staple` form.

### Item 3. Five readings added to the scenario report (no game code; with F)

Each is one line of the report `15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` §1 prints, computed
from the log, with what would show the story did not occur.

| reading | computed from | source of the story | it fails when |
|---|---|---|---|
| **who stayed away** | for each sitting under `acclamation` (proposal E), the sworn of the conferring seat not present at the venue that tick | "ceremony absorbs contests over standing, not substance … `attend / not attend` as the lever" (`research/by_lane/SC_social_contest.md:59`); the seating of 968 (`proposals/2026-09-05-proceedings-subsystem/source/06-part-V-dossiers.md:39`) | attendance is total in every seed (presence carries no choice) |
| **what the hand took** | `transfer` Events received by a holder of a `passes_through` seat from the makers of instruments then in that hand | the purchased toll-post, "maximally vulnerable to legislative removal once visible" (`research/rise_to_power_roster_system_research_v1.md:493-497`) | no such transfer in any seed, or no difference in entry rate between papers with and without one |
| **the servant after the reign** | after a `succeed` on a seat, the `revoke`s by the new holder against seats on its `passes_through`, split by whether each old holder also holds a dignity | the succession cascade, sparing those with "independently-earned transferable Standing" (`rise_to_power…:391-394`) | the split shows no difference over seeds |
| **what he kept** | stores at rungs a departed hand's holder moved goods to, before and after his `hold` closed | the endowment that "is NOT auto-stripped" (`rise_to_power…:292-294`) | — (a count; reported, not gated) |
| **the lord who outgrew his minister** | `revoke`s of a chamberlain-class seat by the holder of the seat it serves, with no opposing act | Basil Lekapenos' removal, "distinctively non-violent" (`rise_to_power…:256-258`) | only meaningful if §14 item 4 is taken as (B); otherwise omitted |

*Gate.* The report prints the first two on `chancery` and `roga` at seeds 0 to 19. *Control:* the
same lines on the base realm print zeros (no `passes_through`, no `acclamation`).

*Cost.* small build, in the harness only.

### Item 4. The register as a precedent file (a gate, no edit; with C and SC's cited evidence)

*Mechanism and source.* "The excerpts on embassies constitute a precedent file, which is a
negotiating advantage before either party speaks" (`06-part-V-dossiers.md:39`).

*Decided.* Nothing is added. Proposal C makes an entry a Record a hand's holder holds; SC's cited
evidence (`05_SC_evidence_and_rebuttal*.md`, the SC-P8 the audits cite) lets a held Record enter the
`evidence` term. The plan is to show that the two compose.

*Gate.* A planted hearing before the Sovereign's seat on a petition to amend the founding papers,
two arms over 200 seeds: the clerk cites an entered instrument he holds; he cites nothing. The
exact `evidence` term differs between arms (no draw needed to see it) and all four bands occur in
both. *Falsifier.* Equal terms: an entry is not citable and proposal C's "the entry is the proof"
is prose.

*Cost.* small build (a test fixture), after C and SC-P8.

### Item 5. Design-first notes carried into batch G (nothing to build now)

Audit §12 holds batch G until A to C have readings. These are the research's statements of what G
must contain when it is designed, so that it is designed once.

1. **Consolidation and its brake are one design.** "Decide and author them together, never one
   alone" (`.audit/…comparative_governance_research_v1.md:280`; theme-splitting,
   `research/proactive_governance_scale_research_v1.md:142`). The brake is the centre's `establish`
   of a sibling seat over part of the ground and its `confer` elsewhere; the consolidated holder's
   reply is the opposition in that draw, and he holds the split as a deed against the centre ("a
   reactive split reads as accusation").
2. **A revenue grant hardens with age.** One row, not a subsystem
   (`tier3_proposal_status_closure.md:122`: "one new grantee-type row … zero new tags, zero new
   resolvers"); the age of the grant is a term in the odds of revoking it
   (`research/fa_se_historical_precedent_research_v1.md:262-266`); the centre "that intervenes early
   still wins cleanly" (`rise_to_power…:526`).
3. **The barred servant is an oath, and has two endings.** Audit §14 item 4 and §18.3 C-2, C-4.
   If Jordan takes (B), the form is the ruled one (an oath of renunciation as a collateral of the
   succession rule), and the readings of item 3 are its gate.
4. **A settler garrison answers a muster by its own regard.** `proactive_governance…:104`;
   `research/pre_firearms_formations/04_high_medieval.md:156`. An interface to the MB and FA lanes:
   the answer to a `dispatch` is the addressee's draw. Not designed here.
5. **Do not grow a controller edge.** The convergence that office against dignity rests on is
   graded over-claimed, and a delegation without a hold was built and reverted
   (`research/by_lane/IN_infrastructure.md:142`). G adds seats and oaths, never a relation by which
   one person controls another's hold.

## Exact edits, by file and owner

| # | file (owner of the fact) | edit | item |
|---|---|---|---|
| 1 | `engine/season/offices.yaml` | `audit_at_exit: audit` on `off_lord_treasurer`, `off_katepano`, `off_kommerkiarios` | 1 |
| 2 | `engine/season/goals.yaml` | the row `goal_kommerkiarios_side_roads`, with the kit's breach kind | 2 |
| 3 | the scenario report of `15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` §1 (harness) | five reading lines | 3 |
| 4 | a test fixture beside proposal C's gate | the two-arm hearing | 4 |

No edit to `verb_table.yaml`, `rosters.yaml`, `arrangements.yaml`, `state/` or `loop/`.

## Order and dependencies

After A, B, C (their own order). Item 3's first two readings with F. Item 1 after B and after
X-12's key lands. Item 4 after C and SC-P8. Item 2 after D and the kit's `staple` form. Item 5
waits with batch G.

## NERS (definitions `CLAUDE.md` §0.06; E last, as a ratio)

- *N.* Cut item 1 and a fiscal officer's departure costs him nothing, which removes the reason to
  recall one and the reason to fear recall (top-down: a king's check; bottom-up: the governed are
  heard; lateral: his successor reads the verdict). Cut item 2 and NPC-090's strictness, a `core`
  need of his case, has no act. Items 3 and 4 are instruments: cut them and the stories of audit
  §10 cannot be seen to fail.
- *R.* A player in the treasurer's seat now weighs what she takes against the account she will give;
  with no player, audits and smuggling cases arise from persons' acts. Completeness: a seat with no
  one able to open the audit produces no hearing and nothing breaks.
- *S.* One audit encoding (the kit's), one goal shape (the existing `deed_doers`), one report. No
  second ladder, no private unit.
- *E, against that.* Three content lines, one goal row and five report lines buy the departing
  officer's reckoning, the gate's offence and four legible stories.

## What stays out

The grades and counts of the order of precedence, the chrysobull's chain, the fiscal vocabulary, the
hippodrome factions and the rest of audit §18.5 are memory-grade and carry no edit. The
*Strategikon*'s doctrine belongs to whoever authors Altonia's goal weights. Nothing here reads
`.audit/` or `.designs/` at runtime; they are cited as referents only.
