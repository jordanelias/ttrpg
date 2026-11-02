# 08 · The old decks and templates, rewritten into the engine's form

## Status: PROPOSED — HELD BACK. Reference under CLAUDE.md §0.05 until a loader reads it; merging ratifies nothing. Every row is `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]`.
## Lane: IN · Home: CL-OPEN (`02_P1_templates.md`) and CL-EVENTS commits (3) and (4) (`workplans/valoria_master_workplan_v10_part4.md`)

## 0. What this is, and what was run

Jordan's original ask (condensed in `critic_lens3.md`; his verbatim first message is not recoverable from the session records): fill in the game's content by **generative templates** and **event decks**, because pure emergence tells similar stories; scripted **hooks and sequences, never whole arcs**; "templates are permitted, so an unfilled instance is not missing content."

This file does that for the existing decks and the Goldenfurt slice. It is a rewrite of their content into the only forms `engine/season/` carries today: **goal rows** on a seat, body or faction (`goals.yaml` schema), a **per-territory yield scale**, and a **Record held from build**. What the engine cannot carry is listed per card, with the reason.

**Executed, not asserted** (scratch run, `build_realm(0)`, rows swapped in through `goals.rows_replaced`):
- Every row below is accepted by `data/goals.py::parse` on top of the 38 rows of `goals.yaml`: 27 of 27 (each alone, and all together: 65 rows).
- The nine Goldenfurt rows each mint a Proposition and each has exactly one committed person: `gf_commune_against_guild_toll` → NPC-081 (Falkenrath), `gf_guild_holds_the_ford` → NPC-007 (Feldhaus), `gf_law_sides_with_commons` → NPC-074 (Stenskald), `gf_crown_wants_men` → NPC-036, `gf_crown_wants_grain` → NPC-037, `gf_crown_watches_the_comptroller` → NPC-033, `gf_church_draws_near` → NPC-021, `gf_old_rite_in_the_hamlets` → NPC-003, `gf_levy_grievance` → NPC-081.
- The content hash moves with the rows on (`3e31638ef6ee` → `2e7f4f3d01da`): as an on-arm they are a declared mover.
- **Executed (§5):** a three-arm attention reading with a placebo, seeds 0 and 1, three seasons. The rung-aimed rows redirect those persons' acts toward the target settlement; whether that is a story is not shown.
- **Not executed:** the `yield_scale` cards (no loader), the seed Records (no carrier), the docket (no deal effect). They are specified, not tested.

## 1. The six Tensions cards (CL-EVENTS commit 4), in the goals schema

World draws one card at build (commit 3). Each `choose_one` below is expanded to every combination and each combination parses.

| card | engine form | what the old card lost |
|---|---|---|
| 1 Royal Crisis | goal on a plotting faction (Varfell / Restoration Movement / Hafenmark), object `seat_holders` of one royal seat (King / Widow Regent / Heir), stance −1: 9 rows | the S8+ date (T-c), "succeeds when it fires" (T-b) |
| 2 Feldmark Famine | `yield_scale` 0.75 on `terr_T5` (Feldmark) for the world's life | none (matter); bites once CR-22's hunger binds |
| 3 Cardinal Independence | goal on one Cardinal seat, object rung `set_s_001`: 4 rows | "appoints" (no Cardinal seat holds `confer`) |
| 4 Guild Fracture | goal on `off_guild_comptroller`, object rung `set_s_018` | any stance (a rung goal writes none) |
| 5 Einhir Incident | goal on `off_restoration_leader`, objects `terr_T4` and `terr_T13`: 2 rows | any march (T4, T13 are territories) |
| 6 Ministry Crisis | goal on a Church seat, object `seat_holders` [`off_parliamentary_clerk`], stance −1 | the fiat "bureaucracy collapses" |

```yaml
- id: tension_royal_crisis_varfell_off_king
  org: {faction: Varfell}
  object:
    kind: seat_holders
    seats: [off_king]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_royal_crisis_varfell_off_widow_regent
  org: {faction: Varfell}
  object:
    kind: seat_holders
    seats: [off_widow_regent]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_royal_crisis_varfell_off_heir
  org: {faction: Varfell}
  object:
    kind: seat_holders
    seats: [off_heir]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_royal_crisis_restoration_off_king
  org: {faction: Restoration Movement}
  object:
    kind: seat_holders
    seats: [off_king]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_royal_crisis_restoration_off_widow_regent
  org: {faction: Restoration Movement}
  object:
    kind: seat_holders
    seats: [off_widow_regent]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_royal_crisis_restoration_off_heir
  org: {faction: Restoration Movement}
  object:
    kind: seat_holders
    seats: [off_heir]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_royal_crisis_hafenmark_off_king
  org: {faction: Hafenmark}
  object:
    kind: seat_holders
    seats: [off_king]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_royal_crisis_hafenmark_off_widow_regent
  org: {faction: Hafenmark}
  object:
    kind: seat_holders
    seats: [off_widow_regent]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_royal_crisis_hafenmark_off_heir
  org: {faction: Hafenmark}
  object:
    kind: seat_holders
    seats: [off_heir]
  pursuits: {liberty: 0.4, justice: 0.3, honour: 0.3}
  stance: -1
- id: tension_cardinal_independence_off_cardinal_fortitude
  org: {seat: off_cardinal_fortitude}
  object: {kind: rung, rung: set_s_001}
  pursuits: {liberty: 0.4, doctrine: 0.3, individuality: 0.3}
- id: tension_cardinal_independence_off_cardinal_justice
  org: {seat: off_cardinal_justice}
  object: {kind: rung, rung: set_s_001}
  pursuits: {liberty: 0.4, doctrine: 0.3, individuality: 0.3}
- id: tension_cardinal_independence_off_cardinal_prudence
  org: {seat: off_cardinal_prudence}
  object: {kind: rung, rung: set_s_001}
  pursuits: {liberty: 0.4, doctrine: 0.3, individuality: 0.3}
- id: tension_cardinal_independence_off_cardinal_temperance
  org: {seat: off_cardinal_temperance}
  object: {kind: rung, rung: set_s_001}
  pursuits: {liberty: 0.4, doctrine: 0.3, individuality: 0.3}
- id: tension_guild_fracture
  org: {seat: off_guild_comptroller}
  object: {kind: rung, rung: set_s_018}
  pursuits: {wealth: 0.4, liberty: 0.3, reputation: 0.3}
- id: tension_einhir_incident_terr_T4
  org: {seat: off_restoration_leader}
  object: {kind: rung, rung: terr_T4}
  pursuits: {community: 0.4, liberty: 0.3, doctrine: 0.3}
- id: tension_einhir_incident_terr_T13
  org: {seat: off_restoration_leader}
  object: {kind: rung, rung: terr_T13}
  pursuits: {community: 0.4, liberty: 0.3, doctrine: 0.3}
- id: tension_ministry_crisis_off_confessor
  org: {seat: off_confessor}
  object:
    kind: seat_holders
    seats: [off_parliamentary_clerk]
  pursuits: {stability: 0.4, doctrine: 0.3, honour: 0.3}
  stance: -1
- id: tension_ministry_crisis_off_cardinal_prudence
  org: {seat: off_cardinal_prudence}
  object:
    kind: seat_holders
    seats: [off_parliamentary_clerk]
  pursuits: {stability: 0.4, doctrine: 0.3, honour: 0.3}
  stance: -1
```

## 2. The Goldenfurt deck (28 cards): what each became

Goldenfurt's persons (G01–G06) are not added: the cast is closed at 46 (ED-WR-0011). The rows bind to the **seats whose holders live in S-006** instead: Feldhaus (Guild comptroller), Falkenrath (commune rep), Stenskald (Skald-Chief, the one `determine` holder), Haldorsen (Riskbreaker doctrine, whose existing `goal_riskbreakers_prevent_corruption` already hunts `terms.distorted` and `record.destroyed`).

| card | engine form | lost |
|---|---|---|
| G101 Only Sons | `gf_levy_grievance`: `deed_doers` of `requisition.taken`, on the commune rep | the widow, the son, the petition, the G501 chain |
| G102 The Toll | the trio `gf_commune_against_guild_toll` (stance −1 on the comptroller), `gf_guild_holds_the_ford`, `gf_law_sides_with_commons` (stance +1 on the commune rep) | the toll itself (no field), Brun, the ruling |
| G103 Famine relief, G402 Famine | a Kronmark famine card: `yield_scale` 0.75 on `terr_T2` | Aldith, Sponsor, Treasury |
| G201 War-Levy | `gf_crown_wants_men` (Royal Marshal, rung `set_s_006`) | the mandatory Directive, the vise |
| G202 Tithe | `gf_crown_wants_grain` (Lord Treasurer) | the Directive |
| G203 Suppress, G605 Public rite | `gf_old_rite_in_the_hamlets` (Restoration leader) | Greta, the Directive |
| G204 Curate's Offer, G603 Chapel→Church | `gf_church_draws_near` (Confessor) | the Geneva trap; a `works` seed is refused (`site_kinds` has no chapel, `mint_planned_works` rejects an unpriced plan) |
| G303 Hedda's alliance | the stance +1 of `gf_law_sides_with_commons` | the offer scene |
| G502 Whisper, G606 Report | `gf_crown_watches_the_comptroller` (Spymaster, object NPC-007) with Haldorsen's existing corruption goal | Konrad, the bribe, the recall |
| G503 Wessel's letter | the same Church row; informing is a `tell` or `petition` the engine already offers | Wessel |
| G602 Orsk's charter | `gf_guild_holds_the_ford` | the charter |
| G505 The Magistrate's Brother | **a Record held from build** by NPC-086 (evidence) — carrier owed (commit 3's "lawful seed") | kinship, the keystone fork |
| G205, G301, G302, G401, G403, G404, G501, G504, G601, G604, G701, G702 | **no engine form**: a Directive with no verb (G205), no event writer (G301, G401, G403, G501), a field force or hostile army (G302, G404), a foreign actor (G504, G604), no province rung (G601), no Thread site at S-006 (G701, G702) | all of each |

Count: 13 cards expressed in whole or part by validated rows, 2 by a `yield_scale` card, 1 by an owed seed Record, 12 with no engine form.

```yaml
- id: gf_commune_against_guild_toll
  org: {seat: off_commune_rep_hm}
  object:
    kind: seat_holders
    seats: [off_guild_comptroller]
  pursuits: {justice: 0.4, community: 0.3, wealth: 0.3}
  stance: -1
- id: gf_guild_holds_the_ford
  org: {seat: off_guild_comptroller}
  object: {kind: rung, rung: set_s_006}
  pursuits: {wealth: 0.5, stewardship: 0.3, reputation: 0.2}
- id: gf_law_sides_with_commons
  org: {seat: off_skald_chief}
  object:
    kind: seat_holders
    seats: [off_commune_rep_hm]
  pursuits: {justice: 0.5, honour: 0.3, community: 0.2}
  stance: 1
- id: gf_levy_grievance
  org: {seat: off_commune_rep_hm}
  object:
    kind: deed_doers
    kinds: [requisition.taken]
  pursuits: {justice: 0.5, family: 0.3, community: 0.2}
- id: gf_crown_wants_men
  org: {seat: off_royal_marshal}
  object: {kind: rung, rung: set_s_006}
  pursuits: {stability: 0.5, honour: 0.3, stewardship: 0.2}
- id: gf_crown_wants_grain
  org: {seat: off_lord_treasurer}
  object: {kind: rung, rung: set_s_006}
  pursuits: {wealth: 0.5, stewardship: 0.3, stability: 0.2}
- id: gf_crown_watches_the_comptroller
  org: {seat: off_spymaster}
  object: {kind: person, case: NPC-007}
  pursuits: {stability: 0.4, honour: 0.3, justice: 0.3}
- id: gf_church_draws_near
  org: {seat: off_confessor}
  object: {kind: rung, rung: set_s_006}
  pursuits: {doctrine: 0.5, community: 0.3, virtue: 0.2}
- id: gf_old_rite_in_the_hamlets
  org: {seat: off_restoration_leader}
  object: {kind: rung, rung: set_s_006}
  pursuits: {community: 0.4, liberty: 0.3, doctrine: 0.3}
```

## 3. The settlement template (generative)

The same five **opening kinds** serve every settlement; each names the *slots* it needs, and a slot is a **seat or body role**, never a name. The Goldenfurt rows above are the instance for S-006.

| opening kind | slots | Goldenfurt instance | eligible by TYPE (buildings serving the body) | and a cast person homed there today |
|---|---|---|---|---|
| market dispute | trade body seat · commons seat · law seat | comptroller · commune rep · Skald-Chief | 36 of 37 (Guild) | 12 |
| levy grievance | commons seat | commune rep | every settlement | those with a commons holder |
| church draws near | church seat | Confessor | 37 (Church) | 13 |
| old rite | Restoration seat | Restoration leader | 32 (Einhir) | 10 |
| law sides | law seat · another slot | Skald-Chief · commune rep | 20 (court or Parliament) | 9 |

Rules the template must keep:
1. A slot binds to a seat's live holder wherever the seat is anchored. Today every opening binds to a seat anchored elsewhere (duchy, T1, T9): **no seat is anchored at a settlement** (`offices.yaml:98`). With E2's Mayor seats, a slot can name the local Mayor seat as its referent, and the referent follows an appointment.
2. Eligibility reads the building map of the settlement's type (`venues.yaml`), not the geography prose. Type-eligibility reaches 36 of 37 for a market dispute; with a person homed there it reaches 12. The gap is the case for generated local people (ED-WR-0011 reopened).
3. Ids are minted per instance (`parse` refuses duplicates): `<kind>_<settlement>_<slot>`.
4. Motives live in pursuits and goal rows, never in a cast `want:` (scored 0.0 salience).

## 4. The seasonal docket (specified, not tested)

The same rows are dealt in play: a named seat-holder's `convene` draws one card from the pool attached to their seat or settlement, once a season. A card writes only goal rows or a Record; any due season is declared by the convening act. One schema serves both deal times: `deal: build | convene`. Goldenfurt cards suited to the docket: G101, G102, G103, G303, G503. What it needs, none built: a `convene` effect that deals, a write-matrix row, a keyed draw (`draw_factory`, seed·tick·convener·"docket"), the Proposition-carried visibility of drawn goals (so `goal()` finds a template by id and the minted Proposition carries the live referent), and plan-text amendments (B10-18's "no step of the season loop reads a card"; B10-19's "no dealing per season").

## 5. What this does not do

- Rows make people **attend**; acts decide. A stance row of −1 makes `fight` form on the referent (`goals.yaml` header). Whether the Goldenfurt rows produce a story is NOT shown. What was measured is attention (below); no one has yet classified the acts it produced, counted cross-person chains, or separated executed acts from refused ones.

**Attention reading (executed, `populated`'s own `SeasonDriver` and chooser, three seasons, rows swapped in through `goals.rows_replaced`).** Three arms per seed: rows off; the nine Goldenfurt rows on; a placebo that keeps every row but aims the five rung-targeted rows (Guild comptroller, Royal Marshal, Lord Treasurer, Confessor, Restoration leader) at S-007 instead of S-006. Count: acts by those five persons whose subject is S-006 (the rung, its buildings, or a person homed there) or S-007.

| seed | arm | all acts | the five persons' acts | subject in S-006 | subject in S-007 |
|---|---|---|---|---|---|
| 0 | off | 2088 | 127 | 11 | 0 |
| 0 | on | 2059 | 131 | **29** | 0 |
| 0 | placebo | 2072 | 133 | 9 | **23** |
| 1 | off | 2080 | 118 | 4 | 0 |
| 1 | on | 2143 | 130 | **21** | 0 |
| 1 | placebo | 2170 | 129 | 3 | **17** |

Reading: the rows move where those persons act. S-006 falls back to its baseline when the target moves, and S-007 takes the attention: the effect follows the target, not the presence of rows. Their total acts barely change, so the rows redirect and do not add. Limits: two seeds and three seasons; the S-006 count includes acts on persons homed there (the comptroller among them, so some are self-acts, present in every arm); the verbs are not classified; the thresholds for "enough" are Jordan's.
- The 12 unexpressed cards stay unexpressed until the engine has the writer, the verb or the field they need.
- The settlement template needs a loader (`settlement_openings`) and the corrected goals visibility before it generates anything.
