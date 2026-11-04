# Strife kinds for S3's person reading: a draft for Jordan to edit

## Status: PROPOSED (2026-11-04). The five open calls were resolved the same day, on the ground of which answer yields the better emergent narrative, at Jordan's instruction (§6); the rest stands as drafted. Reference under CLAUDE.md §0.05, not a mechanism. Nothing reads this file; it is the content S3 needs before code is written.
## Lane: IN

**What this is.** The Opus critic's finding F1 on the Fable plan: the person reading sees an Event *kind* and nothing else, and the registry's `kinds` columns are upper bounds (PR #553, `harness/strife_moves.yaml`; PR #554 added the residue and the `accept` and foreign-field signatures). Used as the definition of a move, they would make everyday kinds (`news.told`, `travel.moved`, `duty.taken`) into strife, and strands into ordinary life. S3 therefore needs an explicit list of which kinds may **open** a strand and which may only **join** one. This draft proposes it from three sources: the study's own tests for each code (the artifact, "Mechanics of Strife to c. 1600", primitives table), what PR #553's master says each kind is (master §3 openings, §4 terminal codes, §9), and what the shipped realm actually emits (measured below).

**Evidence.** `build_realm(seed)` on the shipped default (`foreign=True`), 4 seasons, seeds 0 and 1 (73,277 and 85,183 Events), `Counter(e.kind)` against each kind's codes in the registry and the verbs whose `emits:` name it (`VERB_TABLE`). One run per seed; default play only; a count of 0 is a finding about default play, never proof of absence.

## 1. The rule proposed

- **OPENS**: a kind whose presence alone meets the study's test for a strife move, so one claim of it can start a strand.
- **JOINS**: a kind that is a strife move only in company (a petition after a seizure, a treaty after a siege, a death in a siege). It may attach to a strand an OPENS kind started, through linking (master §4), and may conclude it; it never starts one.
- **NEVER**: everyday or refusal kinds. They are not moves in the person reading.

*Why "joins, never opens".* It keeps the study's detours and endings (settlement, concession, pardon, a death, a petition) in the strands that own them without letting a petition or a treaty create a strand out of nothing. `[ASSUMPTION; medium; Jordan to correct; revert: OPENS and JOINS merged into one list, which F1 predicts collapses strands]`.

The **world reading** is side-aware and may open on more (a `march.declared` with side R or O, §4 below); the person reading is kind-level only.

## 2. The list

### OPENS (9 kinds). Each meets a study test by kind alone.

| kind | codes (registry) | emitted by | seed 0 / 1 | the study's test, and why the kind alone suffices |
|---|---|---|---|---|
| `field.won` | WA WR WN OW | `march` | 0 / 0 | WA "fall of a rebel stronghold; a rebel assault repulsed"; WN "sieges and blockades". A fought field between factions is a battle by construction |
| `field.lost` | WA WR WN OW | `march` | 1 / 1 | same; the attacker's own outcome |
| `rung.seized` | OP SZ XN | `seize` | 0 / 0 | SZ "taking a place by force, entry, expulsion or surrender" |
| `rung.razed` | OP PC PU VI | `raze` | 0 / 0 | VI "any such act whose doer is not the authority's official"; PC "laws after the conflict that penalize the defeated" |
| `record.seized` | BR SZ | `seize` | 0 / 0 | BR "dismissal ... when the challengers did not demand it"; a seizure of papers under a warrant is coercion |
| `arrest.made` | BR CA PU | `arrest` | 0 / 0 | CA "leader captured"; PU "repression at any point in the case" |
| `compliance.withheld` | RF RU | `evade / defy` | 0 / 0 | RF "rejection of a pardon or armistice offered by the authority" |

The table's seven plus two more, because a coercive levy and a sabotage meet the IM and VI tests by construction: `requisition.taken` (IM PC VI; `requisition`; 2 / 3) and `site.damaged` (VI; `sabotage`; 0 / 0). `[ASSUMPTION]`

### JOINS (kinds that need company)

| kind | codes | emitted by | seed 0 / 1 | why it only joins |
|---|---|---|---|---|
| `march.declared` | FR OP OW WN XA | `march` | 44 / 86 | the army verb; the kind cannot tell reinforcement (FR) from invasion (OW) or rising (OP). **Opens in the world reading by side R or O, joins in the person reading** |
| `army.arrived` | FR | `march` | 10 / 8 | the arrival of a march; a result |
| `field.unopposed` | SB SZ | `march` | 10 / 8 | by `loop/sides.py` it is what a march answers when the target's holder is the actor's own faction or nobody holds it: mostly own-ground movement, not seizure |
| `person.died` | DN DR KL XE | `accept` `fight` `march` | 9 / 8 | a death is strife only if violent or of an office-holder; the claim carries no cause (`Claim.doer` is set only on the holder's own deeds) |
| `succession.claimed` | CL IN XN | `succeed` | 0 / 0 | strife only if rival (master §3 "a seat emptied, then `succeed` or a rival claim"); a lone claim is routine |
| `petition.filed`, `petition.carried` | PT | `petition`, `carry` | 22, 3 / 25, 3 | PT "drafting and adopting a list of demands"; a plain petition is ordinary civic life |
| `covenant.offered`, `matter.determined` | NG XS PU | `covenant`, `determine` | 0 / 0 | talks and settlements: endings and detours, never beginnings |
| `dispensation.issued` | CO IM PC XS | `issue` | 12 / 21 | the kind cannot tell a burden from a grant (the study's IM and CO differ only in content) |
| `rung.ceded` | SB XN | `give` | 0 / 0 | a surrender or cession ends; it cannot begin |
| `detention.ended`, `ban.ended` | AM | `pardon` | 0 / 0 | AM "pardon offered and refused" follows a detention |
| `record.given`, `transfer.made` | CO CP | `give`, `transfer` | 1, 5 / 1, 11 | concession and co-option are gifts in company |
| `record.destroyed` | RV | `destroy_record` | 0 / 0 | RV "repeal of the challengers' reforms" |
| `tenure.closed`, `tenure.opened` | BR RV, CP IN | `revoke` `succeed` `accept` ... | 13, 2 / 17, 3 | a closure is a death, an expiry or a dismissal; the kind cannot say which |
| `office.established`, `rung.founded` | RG | `establish`, `found` | 0 / 0 | RG only against an incumbent |
| `army.recruited`, `army.formed`, `army.assigned` | MO SP | `recruit` `form_unit` `assign_troops` | 0 / 0 | MO "any gathering or preparation by the challengers"; routine garrison upkeep otherwise |

### NEVER (everyday or refusal kinds)

| kind | codes | seed 0 / 1 | why |
|---|---|---|---|
| `duty.taken` | IM | 221 / 165 | `oblige`: taking an ordinary duty. **PR #553's openings table lists this as a tax opening; it is not a burden by kind** |
| `duty.refused` | RU | 388 / 379 | a refusal at admission, produced by the gate, not a defiance |
| `news.told` | XA | 16 / 14 | `tell`: ordinary speech. XA's kind-only bound counts it |
| `travel.moved`, `residence.changed` | FA RT | 29, 8 / 30, 12 | ordinary movement. FA and RT need context the kind does not hold |
| `commitment.made`, `commitment.ended`, `stance.moved` | SP DA | 6, 0, 0 / 6, 0, 0 | an oath, a vow, a grudge: personal, not a strife move by kind |
| `argument.won`, `argument.lost` | NG | 0 / 0 | debate is ordinary social contest |
| `order.given`, `date.scheduled` | FR MO | 14, 11 / 13, 13 | a command and a sitting are routine governance |

## 3. What the draft changes in PR #553's master

1. **§3 openings table.** It names `dispensation.issued`, `requisition.taken`, `duty.taken` as a tax opening. By this draft only `requisition.taken` opens; `dispensation.issued` joins and `duty.taken` is never. In default play `requisition.taken` is 2 or 3 per seed, so a **tax raised is mostly invisible to the person reading by kind**. Reading it needs a content test on the writ's terms, not a kind. That is a real gap in the openings the master promised, closed by ruling 5 in §6 (the world reading opens it on the writ's terms).
2. **§4 conclusion.** A strand concludes at the person reading only on a kind that can attach: `rung.ceded`, `detention.ended`, `ban.ended`, `covenant.offered`, `matter.determined`, `dispensation.issued`, `record.given`, `transfer.made` or a field outcome. A kind is terminal only if every code it maps to is terminal (F1's rule); `dispensation.issued` maps to CO IM PC XS and IM is terminal in the study (4 cases), so check it against the S3 tests before relying on it.
3. **Default play opens almost nothing.** With these nine openers, seeds 0 and 1 give 3 and 4 opening Events in four seasons (`field.lost` 1 and 1, `requisition.taken` 2 and 3; the rest 0). The shipped realm is quiet at the kind level; the foreign and challenger marches (H-233: they do march in natural play) are visible only to the world reading. This is a finding about the openers, not a defect to patch by widening the list.

## 4. The world reading's openers (for contrast)

Side-aware: Tier OPENS, plus `march.declared` by side R or O (a challenger or foreign march), plus `person.died` by a lethal `fight` or `accept` of a free victim (KL) or a held one (XE). It has the act, the verb and the faction; the person reading has the kind.

It also carries the three **content openers** that rulings 4 and 5 (§6) assign to it, because the non-violent flow types (a rival succession, a petition movement, a levy) cannot open on a kind: a second `succession.claimed` on one seat; a second `petition.filed` on one matter; a `dispensation.issued` whose terms are a burden. Each reads the *record's* `subject_matter` (`Record.subject_matter`, the field `queries/world_q.py::writs_held` already reads), not the Event: measured, 22 of 22 and 25 of 25 `petition.filed` Events carry a distinct change subject (the freshly minted record), and 44 of 44 and 86 of 86 `march.declared` Events carry no change at all, so no test on an Event's own change can say *same matter* or *toward what*.

## 5. The machine-readable form S3 would load

Where it lives is settled by the critic's F7: a block in `rosters.yaml` read by `roster_map`, so the loop reads a roster and not the harness's `[UNVERIFIED]` grading file.

```yaml
strife_kinds:
  opens: [field.won, field.lost, rung.seized, rung.razed, record.seized, arrest.made, compliance.withheld, requisition.taken, site.damaged]
  joins: [march.declared, army.arrived, field.unopposed, person.died, succession.claimed, petition.filed, petition.carried,
          covenant.offered, matter.determined, dispensation.issued, rung.ceded, detention.ended, ban.ended, record.given,
          transfer.made, record.destroyed, tenure.closed, tenure.opened, office.established, rung.founded,
          army.recruited, army.formed, army.assigned]
```
Every other kind is NEVER. A loader check refuses a kind absent from `EVENT_KINDS`, a kind in both lists, and any kind the registry names that appears in neither list (a deliberate decision per kind, not a default).

## 6. Rulings (2026-11-04): the five calls, resolved for emergent narrative

The test applied to each: which answer makes a flow the characters can *live inside, mishear, resist and be surprised by*, without flows becoming the weather of every season. Three consequences of the user's rulings carry the argument: awareness of a flow is not required for it to condition a person (R7), so what the person reading admits governs only what a person can *know and say*, not whether the flow acts on them; a flow folds when too many are live (R3), so an opener that fires in every season starves the flows that matter; and every type of strife must be able to occur (R1).

1. **`march.declared`: joins at the person reading; opens in the world reading by side R or O.** Narratively the lag is a gain: a province learns of the invasion from the first burned granary or the first refugee, not from the muster, which is how rumour, denial and late warning arise. The kind cannot say where a march goes (44 of 44 and 86 of 86 carry no change) or whose it is, and 44 to 86 openers per run would fold every era into the last march. Foreign and challenger marches still condition people, factions and offices at once through the world reading.
2. **`requisition.taken`: opens.** A collector at the door is the moment a tax becomes a person's own grievance; at 2 or 3 per run it cannot saturate, and each is a hook with a named victim.
3. **`compliance.withheld`: opens.** Verified at `verb_table.yaml` (`evade / defy`) and `queries/world_q.py::writs_held`: the verb forms only on a writ the person holds and is addressed by, so it is defiance of a writ by construction, not a skipped errand. Its count of 0 is a fact about supply: a writ reaches its addressee only by a `give`, and `writs_held` is `()` for nearly everyone. Refusal of an order is the study's own hinge (RU, RF), the best seed of a personal drama, and it must remain able to start a flow when the supply grows.
4. **"Joins, never opens": kept for the person reading, but not as the only route.** Kept because a petition, a treaty or a death would otherwise manufacture strands from ordinary life. Corrected because, taken alone, it makes a rival succession and a petition movement unopenable except through an act of violence, which breaks R1. Those open in the **world reading by content** (§4): two claims on one seat; two petitions on one matter. A lone claim or a lone petition stays civic life; the second is the movement. The person then knows of the movement once a joining kind reaches their ledger while the world holds the strand open. `[GAP: person-side attachment of a joining claim to a world-held strand — S3 must confirm the ledger carries enough to link them; if it does not, the person learns of these flows only from a terminal or an opening kind]`
5. **Tax and burden: invisible by kind at the person reading; opened in the world reading on the writ's terms; known to a person when it bites.** The tax then arrives as the study's taxes do: first as a rumour and a decree, then as the collector (`requisition.taken`), then as defiance (`compliance.withheld`), then as the rising. Making `dispensation.issued` an opener instead would fire on every grant, 12 and 21 times per run, so that gifts and levies would be indistinguishable and the fold would be busy with charity. `[GAP: which term in a writ's `subject_matter` marks it a burden — S3 reads the record and names the field before coding the test]`

`[ASSUMPTION; medium; revert: rulings 1 to 5 reverse independently, each by moving one kind between the §5 lists or striking one §4 content opener]`

`[UNVERIFIED]`: the study's test phrases are quoted from the artifact's primitives table as I read it earlier in this session, not re-opened for this draft.
