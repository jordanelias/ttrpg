# PAPACY-E — the Church at a distance: sees, the tithe, exempt houses, legates, and (design-first) the council and the schism

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-02, X-11) — the `render` terms form is the form `tithe` of `engine/season/instruments.yaml` (one `due` clause `by: addressee`, `every: 1`, `to: named_rung`; the share is the instrument's `amounts`), so edit 2 adds no roster member; a legate's leave is the form `commission`. The sees, the exempt house, the legate, and the held council and schism stand. Every finding below stands.

Re-grounded: 2026-11-12 (audit §15) — two content amendments and four referents (`15_INSTITUTIONS_PAPACY_grounding_mechanisms.md` items 4 and 8). Amended: an exempt house's `oblige` to the head seat is termed, so exemption lapses unless renewed ("relitigable if Standing lapses", `research/proactive_governance_scale_research_v1.md:80`); visitation is `interview` and `research` at a see by the head's or a Cardinal's holder (`:72`). Referents: the archived ladder's territory-scale rung is the Bishop's Delegate (`.designs/systems/factions/reference/faction_politics_v30.md:337`; no canon name follows from it); "Where a benefice is unfilled … there is no priest, so there is no channel" (`proposals/2026-08-30-play-space-coverage/03_seasons_church.md:314-316`), so the scenario should hold one vacant see; the legate "with full powers", recallable, and the legation split when too heavy (`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:113`, `:211`); the schism as a split of the electors, with the ruler's counter of a rival claimant up the same ladder (`research/governance/conflicts_power_struggles.md:272`; `research/rise_to_power_roster_system_research_v1.md:536`). A caution from the tree's own closure: a proposal that imported "Catholic diocesan structure" at Cardinal rank was struck because "the Four Cardinals are arm-heads at Himmelenger" (`.audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:120`); this file's sees sit below the Cardinals and do not make a Cardinal a diocesan. Item 5's council had, at build, a bench of three (audit §15.3 C-1) and is since dropped by Jordan's ruling D-51 (`unified/DECISIONS_ANSWERED.md` A-36). Annates stay out and stay memory-grade; the indulgence pledged to a banker is sourced (`rise_to_power…:498-501`) and stays out.

Reconciled: 2026-11-12, U5d closure — folded **A-36** (against the recommendation): item 5 (the council that may judge the Confessor) no longer "waits on Jordan"; it is dropped, with its procedure P-13, and the Confrontation arc gets no lawful route. Item 6 (schism) stays design-first and gains weight: with no council, a rival seat or violence is the answer to a bad Confessor. The seat-row comment "`head_of_faction` if PAPACY-B item 4 is ruled" is live for every Church officer but the Confessor (A-35). Items 1 to 4 are unchanged.

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (PAP_E: "item 5 and `general_council` stale"; `render` = form `tithe`), §2 (PAP_E/SYN_E row: A-36, A-35), §7 (INCOMPLETE: item 5 dropped; `holder: null`), 7b.0, 7b.7 ("delete item 5 and the `general_council` row"); `U3_CONFLICT_LEDGER.md` §9 ("`15_INSTITUTIONS_PAPACY_E` item 5 … (A-36, A-41)"), C3-L9 (`patronage` is a table entry, PAPACY-B as reconciled); `OWED_TO_UNIFICATION.md` §B ("papacy proposal E still includes the council A-36 dropped"). Changed: **item 5 (the council) and its `general_council` row are deleted from the body**, not left beside the ruling that dropped them (the Status line, the title's "and (design-first) the council", "What it changes" item 4 and edit 5 follow); the see and house rows name the `head_of_faction` revocation (A-35) and carry no `patronage:` key (the table holds it); the `render` terms form is the kit's form `tithe` (this file's first `Reconciled:` line; edit 2 withdrawn); the `holder: null` question is settled at the tree (BYZANTINE-A carries the edit). The title keeps its file name; the council is gone from its subject.

## Status: PROPOSED (items 1-4 are content and small edits; item 6 is DESIGN-FIRST; item 5, the council, is dropped by A-36)

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B33**, after PAPACY-D (`U3_DEPENDENCY_ORDER.md` §1 item 33: "`_E` (item 5 deleted, A-36)"); PAPACY-GROUNDING item 4 lands with it. Depends on: `15_INSTITUTIONS_PAPACY_B` (B32, `tables.patronage`, `head_of_faction`), `15_INSTITUTIONS_BYZANTINE_A` (B32, the vacant-row build edit), `15_INSTITUTIONS_SYNTHESIS_A` (B32, the form `tithe`), `06_FA_decree_binds.md`, `06_FA_remit_grant_by_row.md`, `06_FA_seat_terms_and_turnover.md`, `14_VERBS_BINDING_A_formation.md` (B21); CP-T08-07 (the standing levy, a v11 plan position: MISSING until `STAGES.md` step 5; the tithe gate waits on it). Lane tag: FA. Tier: `sonnet`, effort `medium` (content); one `opus` read of the see gate's `Act.via` table. Named test: `engine/season/tests/test_inst_pap_e.py`. Standing sentences: *Pool*, *Draw keys* — no roll or draw is added; `confer`'s and `requisition`'s are their lanes' (A-6 to A-8, A-30). *Failure writes* — this file adds no contested row; a see-holder's `evade / defy` of the tithe is `compliance.withheld`, a deed the Cardinal's body holds (A-81).

Source: `audits/15_INSTITUTIONS_PAPACY.md` F-PAP-01, F-PAP-07; §3.6 to §3.12; §4.1; §6 rows P-11 to P-13;
§9 items 2, 6, 9, 12; §13 (ARC-36, NPC-013, NPC-034). Composes on PAPACY-B (`patronage:`), FA-P1, FA-P2,
FA-P3 (a `term:` on an office row), `audits/14_VERBS_BINDING.md` §5 (`establish` as a draw), CP-T08-07 (the
standing levy) and the material verb lane for `requisition` / `transfer`. Batch 6.

## What it changes in `engine/season/` at runtime

1. Three seat rows: one Church see on each duchy rung, built vacant. A declared build-hash mover (three
   Offices). With the rows absent: nothing.
2. One goal row for the Cardinal of Prudence's body naming the tithe as a writ; no code.
3. Nothing at runtime for the exempt house and the legate: both are constructions from existing parts,
   stated so that content can author them (one house row is offered, shipped off).
4. Item 6 changes nothing until designed; item 5 is dropped (A-36).

## The problem (evidence)

- The Church's acting reach (`purview_reaches`) and judging reach (`sits_over`) end at `terr_T9`; one seat
  stands elsewhere, `off_archbishops_rep` at `terr_T1`, with `remit_acts: []` (audit E-2). Canon gives the
  Church a *"diocesan structure"* by 200 AG (`canon/03_canonical_timeline.md:50`); the engine authors none.
- The body note for the Cardinal of Prudence reads *"Tithes, charities, Church land management"*
  (`rosters.yaml:2281`) and the goal row `goal_cardinal_prudence_tithes` exists (`goals.yaml:277-284`);
  no levy route exists and Himmelenger's rung chain holds no stores at build (E-2: the stores read was of
  the Confessor's mis-homed chain, `{}` at every rung; `[UNVERIFIED]` for `terr_T9` itself). NPC-013's
  `core` need is a repeatable seasonal act that scales with the territories it is applied to.
- CR-60 gives three benches the realm to judge in and states its own limit: the Church still *acts* only
  where its `rung` reaches.

## The resolution, decided

### 1. Sees: a Church seat on a lord's ground

```yaml
  - id:         off_see_valorsmark          # ids and posts are content; canon names no see
    post:       "Bishop"                    # a member of harness/populated.py::TITLES already
    rung:       {duchy: "Valorsmark"}
    body:       null
    faction:    "Church of Solmund"
    remit_acts: [issue, determine]
    conferral:  appointed
    revocation: head_of_faction             # A-35 (PAPACY-B item 4, ruled)
    holder:     null                        # built vacant (BYZANTINE-A's vacant-row edit)
    obligees:   []
    source:     "canon/03_canonical_timeline.md:50 (diocesan structure). [ASSUMPTION; medium; Jordan to correct: one see per duchy, the post name, the remit]"
    note:       "[NEW] PAPACY-E."
```

and the same for `{duchy: "Hafenmark"}` and `{duchy: "Varfell"}`; each named `[purview, own_faction]` in
`rosters.yaml: tables.patronage` (the lord and the Confessor may each fill it; PAPACY-B §1 as
reconciled). **`holder: null` is settled at the tree:** `build_realm` refuses it today
(`harness/populated.py:1771-1776`); BYZANTINE-A's edit (B32, before this batch) admits a vacant row.

What a see is, in the engine's terms, with no new rule:

- **Reach**: its `rung` is a duchy, so its `issue`, and its bench, reach that duchy (purview and
  `scope_rung` both default to the rung). The Church cites, publishes a sentence, and withholds service
  there through the see-holder, who chooses.
- **Investiture**: the `tables.patronage` entry `[purview, own_faction]` lets the Duke (purview over his duchy, `confer` in
  his remit) and the Confessor (`own_faction`) each fill it by the `confer` draw. A see built vacant is
  the first occasion. A lord's man in the see answers the lord's regard; the Confessor's man, his.
- **Benefice**: the see's holder may `requisition` on his rung (`remit:issue`, presence) and `transfer`
  from the stores he holds. The office and its income are already two things (a `hold` on an Office;
  stores on a Rung), so a deposed bishop who still controls the store is the historical case.
- **Simony and pluralism** are not rules. A candidate's `covenant` with the conferrer and a `transfer` to
  him around a `confer` are deeds in ledgers; a churchman who knows of them has a matter for his bench
  under the existing heresy goal's vow column (`forge`, `evade / defy`) only if the bargain was a vow
  broken. A goal row that names the pattern needs a deed pairing no reader has; it is recorded as not
  built. One person holding two sees is lawful as built (`hold` is one per object, not per person).

### 2. The tithe: a writ, and as many renders as there are sees

The Cardinal of Prudence `issue`s a `dispensation` of the kit's form `tithe` (SYNTHESIS-A §1: one `due`
clause `by: addressee`, `every: 1`, `to: named_rung`) to the see-holders, its `amounts` the share
(`grain`, `[1, 10]`) and its named rung `terr_T9`. Each see-holder answers (FA-P1): `comply` is his own
`requisition` on his rung and a `transfer` toward Himmelenger; `evade / defy` keeps it. The alms it funds
are the Cardinal's and the sees' `transfer`s to hearths in shortfall, which an interdict withholds
(PAPACY-D).

- `share` is a ratio of the season's yield at the see's rung; first value `[1, 10]`
  `[ASSUMPTION; sweep 1/20, 1/10, 1/5]`; owner: the writ's `amounts` (content), so a Cardinal who raises
  it issues a new writ and each see answers again.
- The form is the kit's `tithe` (no `writ_terms_forms` roster exists; X-02). Its execution is the
  standing levy of CP-T08-07 and the material verb lane's `requisition` draw (a settlement that resists is
  theirs to state). This proposal authors the terms form and the goal row and builds no levy.
- NPC-013's need is then met by construction: one act of his, repeated each season, whose yield is the
  number of sees that comply.

### 3. Exempt houses: reach by oath

An order's house is a seat on a lord's ground whose holder owns a live `oblige` to `off_confessor` (or to
a Cardinal's seat). By the oblige clause (`state/gate.py:422-431`) the seat sworn to then reaches that
house's ground. So the Confessor's acting reach inside a duchy is exactly the set of houses sworn to him
there, and it ends house by house when a head `release`s (the Löwenritter's oath to the throne is the
built precedent, `offices.yaml:196`). Content, offered and shipped off:

```yaml
  - id: off_templar_preceptor_hafenmark     # [ASSUMPTION; Jordan to name]
    post: "Preceptor"
    rung: {duchy: "Hafenmark"}
    body: "Cardinal of Fortitude"
    faction: null
    remit_acts: [dispatch]
    conferral: appointed
    revocation: head_of_faction     # A-35
    holder: null
    obligees: []
```

(its `tables.patronage` entry `[own_faction]`; termed `oblige` to the head seat per PAPACY-GROUNDING
item 4, so the exemption lapses unless renewed)

with its holder, once seated, added to `off_cardinal_fortitude.obligees`. This is the archived *Jarnstal
Drift* as structure: the Cardinal of Fortitude's power is the houses sworn to *him* rather than to the
Confessor, and it is visible in who owes whom.

### 4. Legates

A legate is a seat the Confessor founds by `establish` on a rung his reach admits (a see's ground, a
sworn house's ground, or by leave of the lord: a `covenant`), with a `term:` (FA-P3) and a remit he
chooses from his own (the verb lane: Partial founds it with half). At term the hold matures and the seat
is empty. `off_archbishops_rep` is the resident form and NPC-034's need (the sole conduit) holds while it
is the only Church seat reaching `terr_T1`: with its `tables.patronage` entry `[own_faction]` (PAPACY-B) the Crown cannot
replace him, and with `issue` on his row (FA-P2) his seat can act.

### 5. (Dropped, A-36) The council

Jordan ruled that nobody judges the Confessor (A-36, D-51, against the recommendation): he leaves only by
death or resignation, and schism or violence answers a bad one. The council this item designed, its
`general_council` arrangement row, procedure P-13 and the CR-37 `joint_concurrence` strip motion are
**deleted**, not held; the Confrontation arc gets no lawful route. No arrangement row is added for it.

### 6. (DESIGN-FIRST) Schism

A schism is two live head seats of one creed. With the council dropped (A-36), it is with violence the
only answer to a bad Confessor, which gives this item weight (A-80: a held chair is pressure others act
on). The route from existing parts: a `conclave` stays
inconclusive for seasons, or elects by a margin the losers will not accept; the dissenting electors
`establish` a second seat of post
`Confessor`; persons `release` their `commit` to the Church's Proposition and `commit` to a second
faction Proposition whose head seat it is. What is missing is the second Proposition: a faction is a
Proposition plus its commits, and no verb mints a faction Proposition in play (GD-3's pipeline and the
FA lane's emergent-faction ruling own that). When it exists, nothing Church-specific is needed: PAPACY-A's
signature, PAPACY-B's `own_faction` and PAPACY-D's answers all key on the seat's faction, so each
obedience's sentences bind those who answer its writs. Recorded as a dependency on the FA lane, not built.

## Exact edits

1. `engine/season/offices.yaml`: the three see rows (after BYZANTINE-A's vacant-row edit and PAPACY-B's
   `head_of_faction`); `rosters.yaml: tables.patronage`: their three entries.
2. (Withdrawn, X-02: the form is `tithe` in `engine/season/instruments.yaml`; no roster member.)
3. `engine/season/goals.yaml: goal_cardinal_prudence_tithes`: `text` gains *"-- by a standing writ to the
   sees, each rendering a share of its rung's yield"*; no key changes.
4. `engine/season/offices.yaml`: the house row, commented out, with its `[ASSUMPTION]`.
5. (Deleted, A-36: no `general_council` row.)

## Gate

- Vacant rows (first, red before BYZANTINE-A's edit): `build_realm(0)` with the three rows raises
  `Unspecified` naming the row; after the edit it builds.
- Sees: `build_realm(0)` has three more Offices, each vacant, each fillable through `off_confessor` and
  through its duke's seat and through no other faction's (`may_fill` table). In a three-season run at
  seeds 0-2 with the verb lane's `confer` draw and CR-88's vacancy duty landed: at least one see is filled
  at some seed, and the `Act.via` that filled it is reported (which side won is a reading, not a bar).
  Control: rows absent, base hash.
- Reach: after a see is held, `sits_over(off_see_hafenmark, <a Hafenmark settlement>)` True and a
  `dispensation` issued through it names a Hafenmark resident as addressee.
- Tithe (after the levy lands): one writ, three sees; stores at `terr_T9` rise by the sum of the renders
  of the sees whose holders complied; a defying see's rung keeps its stores. Control: no writ.
- Exempt house: with the house row on and its holder sworn, `purview_reaches(off_cardinal_fortitude,
  duchy_hafenmark)` True; after his `release`, False.

## Falsifier

A see filled by a seat of a third faction. A tithe that moves stores with no `requisition` act by a
see-holder. Reach through a house that survives its head's `release`.

## NERS reading

N: cut the sees and the Church is a city (today): no investiture, no local sentence, no tithe, no
interdict, and CR-89's Church Influence has nothing local to count. R: a duke decides whether to invest
his own bishop and what it will cost him; a bishop serves two masters and chooses each season; a Cardinal
builds a following by oaths. With no player a vacant see is a standing prize. S: a see is an ordinary
seat; its reach is the ordinary purview; the tithe is an ordinary writ. E (last): three rows and one
form row for the whole diocesan layer; the council is dropped by ruling (A-36) and the schism is
deferred because it needs a carrier this lane does not own.

## Cost class

Content edit (1, 3, 4); design-first (6). Edit 2 withdrawn; item 5 dropped (A-36).
