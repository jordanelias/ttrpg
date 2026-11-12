# COLONIAL-E — two playable scenarios and the report that shows them: "The Farm of the Southern Tolls" and "The Katepano's Latitude"

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-12, X-32) — this file's case-and-report shape is the one scenario style for every institution, and its report `harness/institution` is the one report, widened with the other three lanes' readings (`15_INSTITUTIONS_SYNTHESIS_D_first_playable.md` §1, §3); the farm's maker in the integrated playable is `off_king`, and The Farm of the Southern Tolls is that playable's second cut as well as this family's standalone; the conferred seat carries `audit_at_exit: audit`. Both scenarios, the report's lines and the gate stand. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's research (`unified/RESEARCH_MAP_INSTITUTIONS_B.md`; audit §16). No edit of this file's is changed. What changed: the report this file specifies gains lines, all read-only and all specified in `15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md`: orders sent by bare `issue` against orders carried by a bearer (edit 1); at each audit sitting, what the officer's books declare beside what the residents' claims sum to, and a tag for paired against combined officers (edit 6); six more stories with their folds: the unpaid bond, invited in, the garrison that ate the town, the post let go, the privilege carried off, the hostage who came home another's man (edit 8). The second scenario gains its hold on the frontier governor: a seeded `commission` that forbears war and treaty (edit 5). The one shipped game in the tree's survey that is built on a chartered company, John Company, is now cited in the audit's §15; it models the offices and not the audit, so this file's null on a playable end-of-term hearing stands (`research/valoria_game_precedent_companion_v1_part6.md:165-175`).

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_COLONIAL.md` §8, §9, §12 batch C-5. The standing requirement
(`AUDIT_BRIEF.md`: playable alone, one code path, integrated, no GM). Composes and does not replace
`06_FA_playable_scenario.md`, `05_SC_playable_hearing_B.md` and `07_SE_valley_scenario.md`. Depends on
`15_INSTITUTIONS_COLONIAL_A` to `_D`. Nothing is ratified by being written.

## What it changes in `engine/season/` at runtime

Nothing on the game path. It adds one exercise case and one read-only report. The case is the realm as
built plus one seeded instrument and the seat it confers; every act in it is formed by the one chooser or
by the player-proxy surface the harness already has (`harness/play_surface.py`, `headless.py`,
`exercises.py`).

## Scenario 1 — The Farm of the Southern Tolls

**Ground.** `terr_T6` Stillhelm: Crown, "Calamity-adjacent. Southern Crown gate to Askeheim", S-012
"Population uneasy", S-013 Aschenbach (`valoria_geography_v30.yaml`). Two territory hops from the
capital by the file's edges (T1–T5, T5–T6); `world_q.remove` reads it, not this text.

**Setup delta** (the case file states only what differs from the realm, as `12_ARCS_case_on_the_realm.md`
decides for every case):

```yaml
id: INST-COLONIAL-01
scale: territory
setup:
  instruments:
    - form: farm
      maker_seat: off_lord_treasurer
      grant_ground: terr_T6
      to: <a cast case id resident in the capital>      # the farmer; [ASSUMPTION: content]
      amounts: {advance: 6, rent: 3}                      # units of `coin`; [ASSUMPTION; sweep ×{0.5, 1, 2}]
  stores:
    set_s_012: {grain: 12, coin: 4}                       # until SE's `ground` endowment lands
    set_s_013: {grain: 6,  coin: 1}
seats_offered: [the conferred Farmer seat, off_lord_treasurer, a hearth head of set_s_013]
ends:
  - the farm's term matures and an `audit` is determined (four bands)
  - the Farmer's hold closes before term (recall, release, death, a field)
  - six seasons elapse (MAX_SEASONS)
```

**What the player in the farmer's seat chooses each season** (each is an existing verb's candidate, so
an NPC in the seat chooses among the same): where to stand (`move`: `remove` to S-012 is 0 if he lives
there); which settlement to levy and for what share (`requisition`, rolled: yield by band); whether to
commission a `survey` first (evidence for the roll); whether to pay his men (`transfer` from the seat's
rung renews their `oblige`); whether to send the rent (`transfer` to the capital, rolled at `remove` 2:
arrival by band); whether to remit in a lean season and fall short on the rent (the grantor's `kept`
then reads a breach, **if he hears of it**); whether to answer a petition.

**What the grantor chooses:** to grant and to whom; to levy inside the farm himself (his own breach);
to `dispatch` an inspector; to open the `audit` at term or let it lie; to renew.

**What a hearth head chooses:** to hide stores (`conceal`), to `petition`, to speak at the audit, to
`migrate`, to swear to the farmer's seat or to another.

**Legibility.** Every rolled act's Event carries its obstacle terms (SC-P1, as SC-B states), so the
client can say *why* a levy fell short: "share demanded: half (+0.5); the people's regard (+0.4); you
were two territories away (+0.5); assessment held (−0.25)". The audit's verdict cites the testimonies
and records weighed.

**Stakes and endings.** By the audit's band: banned from the grantor's seats; bound to restitution;
admonished; quit with a clean record (which is evidence for his next bid). Or no audit: he keeps what he
took and the ground remembers.

## Scenario 2 — The Katepano's Latitude

`build_realm(S, foreign=True)` with the court seat (`…_B_distance.md` §4). Seats offered:
`off_katepano`, `off_altonian_court`, `off_king`. The court issues orders that roll at `remove` 3 and
hears only what somebody travels to tell it; the Katepano may `march` through T3, offer a `tribute` or a
`wardship` by `covenant` to a Crown seat, or `construe` an order that arrived open to reading. Endings:
the roster's (`peninsular_sovereignty`, `theocracy`, `reabsorption`), her recall, six seasons.
Dependencies beyond scenario 1: CR-29 (the border), FA-B1 (a war lives in seats), MB's field, ED-IN-0317's
march cap. It is second because it has more of other lanes in it.

## The report (read-only; `harness/strife.py`'s kind; not a guard, not a standing corpus)

`python -m engine.season.harness.institution <case> <seasons> <seed>`, output to a path the caller gives.
Per season it prints, from the Event log and the two parties' ledgers:

| line | read from |
|---|---|
| levies attempted through the conferred seat, each with its band and term list | Events of `requisition.*` with `Act.via` the seat |
| rent and tribute `transfer`s, each with its band and what arrived | Events of `transfer.*` between the two rungs |
| `kept` as the grantor reads it and as the grantee reads it | `person_q.kept` on each party's own ledger |
| `dues` stamped and acts occasioned by one | question referents; `occasioned_by` |
| petitions filed naming the seat or its holder; residence changes out of the ground | `petition.filed`, `residence.changed` |
| the establishment of the conferred seat against the grantor's local establishment | `world_q.establishment_of` |
| the audit: opened or not, by whom, the bench, proofs weighed, band | `case.opened` under the row; the `determine` Event |

## Gate (execution artifact) — the gate for the family's whole plan

Seeds 0–4, six seasons, `PYTHONHASHSEED=0`, the NPC chooser in every seat:

1. **Varied outcomes from one fixture:** across the five seeds at least two different audit dispositions
   occur (counting "not opened" as one), and at least one levy lands in each of three bands.
2. **The two ledgers disagree somewhere:** in at least one seed-season the grantor's and the grantee's
   `kept` differ in sign or size.
3. **Consequence is read downstream:** at least one act by a person who is neither party is
   `occasioned_by` an Event of the farm (a petition, a migration, an oath).
4. **Control:** the same seeds with the instrument absent: no Farmer seat, no levy through it, and the
   realm hash equals the base realm's at each season.
5. **Planted failure:** every roll's band forced to Success. Conditions 1 and 2 must then fail; if they
   still pass, the variety was coming from somewhere other than the draws and the reading is void.

Five seeds are five trajectories. No rate, no balance claim, no tuning value is taken from them
(CLAUDE.md §0.1 pt 4); tuning is `13_SC_calibration.md`'s method on the fixtures each proposal names.

## Falsifier for "playable alone"

A human at `harness/headless.py` in the farmer's seat, offered the season's candidates, can reach each of
the four audit endings on some seed by choosing differently (press hard and forge the accounts; press
hard and be honest; remit; abscond). If two of those policies cannot be told apart by their outcome
distributions over 20 seeds each, the choice is not a choice and the scenario fails. That reading is
manual and is the close's, not a test's.

## Landing order for the family (batches; each closes with its one test file; the suite once at the end)

| order | batch | proposal | lands after (other lanes) | hash |
|---|---|---|---|---|
| 1 | C-1 instruments | A | `covenant` and `issue` formation (SOCIAL, BINDING verb lanes) | EQUAL with the file empty; mover per seeded row |
| 2 | C-2 `remove` and the four graded rows | B §1–§2 | SC-B; FA-P6's vocation pattern; the MATERIAL lane's rows | declared mover |
| 3 | C-2 reach rows, court seat, ending | B §3–§5 | CR-29 | mover with `foreign=True`; EQUAL in the control arm |
| 4 | C-3 audit and calling-in | C | SC-P4; SC's hearing reach; FA-P3; CR-60/61 | EQUAL until a matter is docketed |
| 5 | C-4 the ledger | D | C-1; ARCS' prehistory; audit §11 item 1 for the counts | declared mover |
| 6 | C-5 scenario 1 and the report | E | 1, 2, 4; SE treasury; CHAR regard | none (harness and a case) |
| 7 | C-5 scenario 2 | E | 3; FA-B1; MB field; ED-IN-0317 | none |

## NERS reading

- **N.** It is the standing requirement's instrument for this institution; without it the family is five
  proposals nobody has seen run.
- **R.** Three seats, four endings, policies that differ; an NPC-only run produces the stories of audit
  §8 or shows that it does not.
- **S.** The season loop and nothing else; SC's hearing is entered and returned from by the docket.
- **E, last.** One case file and one report.

## Cost class

Small build (the report); the case is an edit.
