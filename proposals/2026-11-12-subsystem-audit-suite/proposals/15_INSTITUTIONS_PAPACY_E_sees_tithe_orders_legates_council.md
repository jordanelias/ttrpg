# PAPACY-E — the Church at a distance: sees, the tithe, exempt houses, legates, and (design-first) the council and the schism

## Status: PROPOSED (items 1-4 are content and small edits; items 5 and 6 are DESIGN-FIRST and item 5 waits on Jordan)

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
4. Items 5 and 6 change nothing until designed and ruled.

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
    revocation: null                        # `head_of_faction` if PAPACY-B item 4 is ruled
    patronage:  [purview, own_faction]      # the lord and the Confessor may each fill it
    holder:     null                        # built vacant
    obligees:   []
    source:     "canon/03_canonical_timeline.md:50 (diocesan structure). [ASSUMPTION; medium; Jordan to correct: one see per duchy, the post name, the remit]"
    note:       "[NEW] PAPACY-E."
```

and the same for `{duchy: "Hafenmark"}` and `{duchy: "Varfell"}`. `[UNVERIFIED: that `build_realm` admits
a seat row with `holder: null`; if it does not, the row is minted by the `instruments`-style skip-and-report
pass of PAPACY-C edit 2, generalised to seats, or the three sees are founded in play by `establish`.]`

What a see is, in the engine's terms, with no new rule:

- **Reach**: its `rung` is a duchy, so its `issue`, and its bench, reach that duchy (purview and
  `scope_rung` both default to the rung). The Church cites, publishes a sentence, and withholds service
  there through the see-holder, who chooses.
- **Investiture**: `patronage: [purview, own_faction]` lets the Duke (purview over his duchy, `confer` in
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

The Cardinal of Prudence `issue`s a `dispensation` to the see-holders: `terms: {render: {kind: grain,
share: [1, 10]}, to: {territory: "T9"}}`. Each see-holder answers (FA-P1): `comply` is his own
`requisition` on his rung and a `transfer` toward Himmelenger; `evade / defy` keeps it. The alms it funds
are the Cardinal's and the sees' `transfer`s to hearths in shortfall, which an interdict withholds
(PAPACY-D).

- `share` is a ratio of the season's yield at the see's rung; first value `[1, 10]`
  `[ASSUMPTION; sweep 1/20, 1/10, 1/5]`; owner: the writ's `terms` (content), so a Cardinal who raises it
  issues a new writ and each see answers again.
- The `render` form is a third member of PAPACY-D's `writ_terms_forms` roster. Its execution is the
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
    revocation: null
    patronage: [own_faction]
    holder: null
    obligees: []
```

with its holder, once seated, added to `off_cardinal_fortitude.obligees`. This is the archived *Jarnstal
Drift* as structure: the Cardinal of Fortitude's power is the houses sworn to *him* rather than to the
Confessor, and it is visible in who owes whom.

### 4. Legates

A legate is a seat the Confessor founds by `establish` on a rung his reach admits (a see's ground, a
sworn house's ground, or by leave of the lord: a `covenant`), with a `term:` (FA-P3) and a remit he
chooses from his own (the verb lane: Partial founds it with half). At term the hold matures and the seat
is empty. `off_archbishops_rep` is the resident form and NPC-034's need (the sole conduit) holds while it
is the only Church seat reaching `terr_T1`: with `patronage: [own_faction]` (PAPACY-B) the Crown cannot
replace him, and with `issue` on his row (FA-P2) his seat can act.

### 5. (DESIGN-FIRST; Jordan, audit §13 item 2) The council

```yaml
  - id:               general_council
    disposal:          declared
    quorum_share:       [2, 3]
    bench_basis:        determine
    floor:              admitted
    records_dissent:    true
    venue_min_rank:     settlement
    term_required:      true
    appeal_basis:       none
    interposed:         [procedure, ceremony, document]
    order:              rank
    proofs:             [record, testimony]
    disposes:           Record
    disposal_reach:      realm
    standard:           hard
```

Bench: every Church seat granting `determine` (the sees included, which is what makes multiplying sees
change who controls a council). It disposes a `resolution` (CR-36's site). Two uses: a doctrinal or
disciplinary resolution the head then acts on; and, if Jordan takes option (B), the motion that with the
throne's concurrence strips `off_confessor` (CR-37's `joint_concurrence` route, its `concurring_bodies`
roster keyed by the stripped seat's faction: `{Valorsmark: [Holy See], "Church of Solmund": [<the
throne's body>]}`). Not built until ruled.

### 6. (DESIGN-FIRST) Schism

A schism is two live head seats of one creed. The route from existing parts: a `conclave` ends Partial (a
provisional hold) and is not confirmed; the dissenting electors `establish` a second seat of post
`Confessor`; persons `release` their `commit` to the Church's Proposition and `commit` to a second
faction Proposition whose head seat it is. What is missing is the second Proposition: a faction is a
Proposition plus its commits, and no verb mints a faction Proposition in play (GD-3's pipeline and the
FA lane's emergent-faction ruling own that). When it exists, nothing Church-specific is needed: PAPACY-A's
signature, PAPACY-B's `own_faction` and PAPACY-D's answers all key on the seat's faction, so each
obedience's sentences bind those who answer its writs. Recorded as a dependency on the FA lane, not built.

## Exact edits

1. `engine/season/offices.yaml`: the three see rows (after PAPACY-B's `patronage:` key exists).
2. `engine/season/rosters.yaml: writ_terms_forms` (PAPACY-D edit 5): member `render: [kind, share, to]`.
3. `engine/season/goals.yaml: goal_cardinal_prudence_tithes`: `text` gains *"-- by a standing writ to the
   sees, each rendering a share of its rung's yield"*; no key changes.
4. `engine/season/offices.yaml`: the house row, commented out, with its `[ASSUMPTION]`.
5. `engine/season/arrangements.yaml: general_council`: not added until §13 item 2 is ruled.

## Gate

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
terms form for the whole diocesan layer; the council and the schism are deferred because each needs a
decision or a carrier this lane does not own.

## Cost class

Content edit (1, 3, 4); small build inside PAPACY-D's roster (2); design-first (5, 6).
