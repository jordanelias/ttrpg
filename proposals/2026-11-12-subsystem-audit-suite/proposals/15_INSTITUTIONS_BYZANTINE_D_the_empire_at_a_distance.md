# INST-BYZ-D — the empire at a distance: a centre that is one person, a prince who is a hand, a gate with a keeper, and what `altonian_civics` condemns

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-13, X-14) — the far superior is one seat, shared with `15_INSTITUTIONS_COLONIAL_B_distance.md` §4: id `off_altonian_court`, anchored `{territory: "ALT"}` (this file's own fallback), its holder resident at `ALT-0` at `hops: 3`, with this file's `passes_through: [{seat: off_doux}]`, `off_doux`, the three `obligees` and `factions.head_seat`; `off_altonian_head` is not a second seat. Distance is both the Doux's hand (a person) and `remove` on the court's `issue` (space). Edits 4 to 7 stand. Every finding below stands.

Re-grounded: 2026-11-12 (audit §18) — two additions and one named disagreement. Added (`15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` items 1 and 2): `audit_at_exit` on `off_katepano` and `off_kommerkiarios`; a `deed_doers` goal row by which NPC-090 acts against trade that passes the treaty's gate (the one fragment of the Eparch proposal the tree kept, `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:157`, `:328`). Disagreement, not resolved: `references/npc_registry.yaml:499` gives the Doux "Manuel II Palaiologos archetype"; the archived roster gives Demetrios Palaiologos and names his ethic *oikonomia* (`.designs/systems/npcs/reference/npc_roster_v30_infill.md:67-69`). Sourced now: diplomacy as "a graded protocol of precedence, gifts, and staged audience" (`research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:127`); payments abroad "recorded as imperial largesse" (`proposals/2026-09-05-proceedings-subsystem/source/06-part-V-dossiers.md:39`); containment of a church by recognising its head (`research/governance/governance_modes.md:76-77`, with its verifier's caution at `:59`). The *kommerkiarioi*, the 1082 privilege and hostage heirs stay memory-grade.

Reconciled: 2026-11-12, U5d closure — folded **A-22** and **A-21**. The far superior (`off_altonian_court`) commands its sworn men and the holders of seats it may revoke; an order from it to anyone else is not binding, and a writ from the Doux upward is a petition. Its decrees are proclaimed: their terms reach whoever learns of them, at `border_hops` remove.

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §1.1, §2.6, §2.12, §7.1, §10, §11, §14 item 3;
`audits/12_ARCS_adjudication.md:368` (row 12: off-map superiors, "generate a person", decided by
precedent, "none written"). Batch D. Depends on proposal C (hands), CP-T09-03 (a covenant something
reads), CP-T09-08 (`dispatch` that sends). The names are Jordan's (§14 item 3); every name below is a
placeholder marked for replacement. Ratifies nothing.

## What it changes in `engine/season/` at runtime

In the foreign arm only (`build_realm(foreign=True)`, the shipped default since ED-IN-0310). The
control arm (`foreign=False`) stays byte-identical to the realm with no empire.

1. One more foreign place (the centre) and two more foreign seats exist: a head seat with `issue`
   and `confer`, held by one newly authored person, and the Doux's seat, held by NPC-011, who is cast
   and unseated today. A declared foreign-arm build-hash mover.
2. The head's instruments addressed into or toward the realm pass through the Doux's seat
   (`passes_through`, proposal C): he may enter, hold over or return each, by a draw.
3. The Katepano and the Kommerkiarios gain a revocation basis that the head's seat satisfies, so the
   empire can recall its own officers (a draw, proposal E).
4. `affiliation_engagement` gains sign cells under `altonian_civics`: an observer who holds the
   affiliation is scarred by seeing an order defied or a record destroyed.

## The problem (evidence)

- `offices.yaml:607-632`: two Altonian seats, both `conferral: null`, `revocation: null`, "canon names
  no way the empire fills or strips the post". `rosters.yaml: faction_leaders` makes the Katepano the
  empire's head `[ASSUMPTION]` with "Revert: the Doux (NPC-011) … as head". Nothing stands above her.
- Case NPC-011, need 4 (`important`): "receive directives from a nominal imperial superior and …
  deliberately delay, dilute, or fail to execute them, without immediate open rebellion". The case
  overlay seats "the Altonian imperial authority" as a person with no office. NPC-089's need 6 is
  UNCLEAR on "whether her decision … requires authorization from a more senior authority". ARC-45
  needs a demand "suppressed while an intermediary withholds signals" (FA audit §13).
- NPC-011 holds no seat; his registry `territory` is null; the archived campaign design places him
  over "T11/T12 Altonian provinces" (`campaign_architecture_v30.md:187`), which are Varfell
  territories in `valoria_geography_v30.yaml`. **A disagreement in the tree, named:** the archived
  line cannot be right against the geography; this file seats him off the map.
- `npcs.yaml:293-301` homes him at Lowenskyst's barracks in the realm derivation; `populated.py:1307`
  moves every foreign-faction person to the foreign settlement.
- `altonian_civics` has a roster row, four `incompatible` cells (all null) and no engagement cell:
  it is held (0 to 5 on every cast row) and read by nothing but the conviction machinery's generic
  paths. NPC-090's case needs his "conviction toward established precedent and order" to "bias him
  toward strict, by-the-letter enforcement … in a way his counterparty can anticipate".

## The resolution, decided

An empire governs at a distance through a person who writes, a person the writing passes, and a
person who acts on the last writing she received. That is three seats and one hand. The centre's
person is authored content (the cast is closed and authored, ED-WR-0011); ladder step 4 decided the
shape (the two existing foreign seats). No Altonian body is invented (`rosters.yaml`: "inventing a
body here would be indistinguishable from canon"); a hand may be a seat id (proposal C, edit 1).

## Exact edits

**1. `references/npc_registry.yaml`** — one row, `status: proposed`, the next free NPC id (allocated
at landing from `references/id_reservations.yaml`, not here): faction `Altonia`; role
`[PLACEHOLDER] head of the imperial centre`; `cultural_label: altonian_imperial`; `affiliations:
{solmund_orthodoxy: 1, einhir_restoration: 1, altonian_civics: 5}`; pursuits led by `stability` and
`reputation` `[ASSUMPTION; medium; Jordan to author]`. No name is proposed.

**2. `rosters.yaml: foreign_cast.by_faction."Altonia"`** — add `centre: {code: "ALT-0"}`, a second
settlement under `ALT`. `[UNVERIFIED]` which keys `build_realm(foreign=)` reads off this mapping
(`data/rosters.py::FOREIGN_CAST`); the reader gains the key. `faction_leaders."Altonia"` moves from
NPC-089 to the new person; `factions.head_seat` gains `"Altonia": off_altonian_head`.

**3. `offices.yaml: foreign_seats`** — two rows added, two edited:

```yaml
  - id:         off_altonian_head
    post:       "[PLACEHOLDER] head of the imperial centre"
    rung:       {settlement: "ALT-0"}
    body:       null
    faction:    "Altonia"
    remit_acts: [issue, confer, revoke]
    conferral:  null
    revocation: null
    passes_through: [{seat: off_doux}]
    holder:     "<the new NPC id>"
    obligees:   ["NPC-089", "NPC-090", "NPC-011"]
    source:     "ARCS adjudication row 12; cases/exercises/NPC-011.yaml ('the Altonian imperial authority')"
    note:       "[NEW]. No `dispatch`: the centre does not march; its governors do."

  - id:         off_doux
    post:       "Doux"
    rung:       {settlement: "ALT-1"}
    body:       null
    faction:    "Altonia"
    remit_acts: []
    conferral:  appointed
    revocation: rung_above_same_faction
    holder:     "NPC-011"
    obligees:   []
    source:     "references/npc_registry.yaml NPC-011 (`title: Doux`; goals: 'Sandbag imperial directives')"
    note:       "[NEW]. Seated at the staging post beside the Katepano [ASSUMPTION; medium; Jordan to place him: his province is off the map]. An empty remit: in this world his power is the hand."
```

On `off_katepano` and `off_kommerkiarios`: `conferral: null` → `appointed`; `revocation: null` →
`rung_above_same_faction`. `[UNVERIFIED]` that `seated_on_the_rung_above` finds `off_altonian_head`
from `ALT-1`: both settlements sit under the territory `ALT`, so the head is on a **sibling** rung,
not the parent, and the rule as written (`offices.yaml:69-81`) would fail on rung as the Church's
seats failed on faction. If so the head's seat is anchored at `{territory: "ALT"}` instead, which
makes it the parent rung of `ALT-1`; the centre settlement is then only where its holder lives.

**4. Distance.** `rosters.yaml: office_bodies.term` cannot carry a seat hand, so proposal C's map
gains a sibling under `offices.yaml: seats[]`: `hand_term:` on the row that **is** the hand
(`off_doux: hand_term: 2`), seasons a document may wait for that seat. Sweep 1 / 2 / 4. A writ of
the head's is thus answerable two or more seasons after it is written, or returned.

**5. The gate and its keeper.** No new rule. The Kommerkiarios's seat is already at the interface;
what the case needs is a paper for him to rule on. `offices.yaml: off_kommerkiarios` gains
`hand_term: 1`, and the realm's trade seat that faces him names him as a hand on its instruments
across the gate: `off_guild_comptroller: passes_through: [{seat: off_kommerkiarios}]`
`[ASSUMPTION; medium]` (NPC-007, "Guilds Representative"; the registry's named counterparty,
"Solberg", has no seat and is content debt). A request for an exception is then an `issue` or a
`petition` he enters, holds or returns, by proposal C's draw, with his `altonian_civics` (4) and his
regard for its maker in the odds. The treaty itself is CP-T09-03's `covenant`; nothing here builds
it.

**6. The tutoring demand (ARC-45).** The head's demand is a `covenant` offer addressed to the King
(`verb_table.yaml: covenant`: the counterparty is a person, the terms an uttered Proposition; no
purview is asked, "a covenant reaches across"). Minted through `off_altonian_head`, it carries the
Doux's hand like any instrument of that seat. While he holds it over or returns it, the King holds
no claim of it. Nothing is added for the arc: the suppression is a person's act at a hand.

**7. `rosters.yaml: tables.affiliation_engagement`** — a column `altonian_civics`, sign cells:

```yaml
      altonian_civics:
        "evade / defy":  -1
        destroy_record:  -1
        forge:           -1
        comply:           1
        carry:            1
```

`[ASSUMPTION; medium; Jordan to correct]`. `[UNVERIFIED]` that none of these five verbs carries a
cell in the shared column `sacred` (`data/affiliations.py::_load_engagement` refuses a verb with
both, `:189-192`); a verb that does is dropped from this column. Its one reader today is the scar
(`person_q.elements_violated_by`): a holder who sees an order defied takes a count on
`altonian_civics`. That is the anticipable strictness NPC-090's case asks for, by data.

## Gate (execution artifacts)

1. *Control.* `build_realm(0, foreign=False)`: `content_hash` unchanged.
2. *The hand.* Foreign arm, seeds 0 to 19, six seasons: the head's instruments issued; at the Doux's
   hand, the counts entered, held over, returned by him and returned by the clock; the lag in ticks
   from issue to answerable for those entered. All of entered and not-entered occur across the seeds.
3. *The prince.* The same run in two arms differing only in the Doux's stance row toward NPC-030
   (Elske): his entry rate differs between the arms (his regard for a person in the realm weighs
   against his hand). A planted control with the stance row toward an unrelated person shows no
   difference.
4. *Recall.* A hand-placed `revoke` of `off_katepano` through `off_altonian_head`: admitted at
   eligibility (it is refused today: `revocation: null`); its bands are proposal E's.

## Falsifier

Delete `passes_through` from the head's row: every instrument is answerable at issue and gate 2's
lag is zero. Set the Doux's `altonian_civics` to 5 and his stance toward everyone to zero: his entry
rate rises toward the Katepano's own compliance rate; if it does not, the affiliation is not in the
odds.

## NERS

N: cut the centre and Altonia is one person's temperament; NPC-011's fourth need, NPC-089's sixth
and ARC-45 stay unreached. Holds top-down (orders), bottom-up (a governor acting on stale orders),
laterally (the two trade officials). The `altonian_civics` cells hold in one direction only today
(the scar): **narrowed** until a chooser term reads engagement. R: the Doux's three answers; the
no-player half is the stale order and the sandbagging prince. S: every piece is proposal C's hand,
the gate's existing bases, `covenant`. E, against that: one person, one place, two rows, two edited
rows, one row key, five cells.

## Cost class

Edit (content) plus the small build of `hand_term` and the `centre` key. Movers: the foreign-arm
build hash.
