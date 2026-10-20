# Verbs, v2 — part 14: Part VI.6, settlements and governance (GV)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · **this file** GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `GV §3.n` (for example `GV §3.9` for its items for Jordan). Gap ids (`GV-G01` …) resolve in Part VII (`verbs-21`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Old file names such as `…synthesis_part8.md` or `_part8` in the body also mean those first-pass files; the suite was later renamed `2026-10-16-verbs-NN-…`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`verbs-03` §III.5; where this section and the roster disagree, the roster governs):

- R-03: GV owns `found`, `build`, `raze`; `fortify` is a content of `build`.
- R-04: `tax` is its own row; `requisition` stays.
- R-05: the rename `dispatch` → `order` is **held for Jordan** (ED-IN-0210 kept `dispatch`); the posting act is FA's `assign`.
- R-11: GV owns `succeed`.
- R-12: `construe` is added to GV's roster.
- R-15: `arrest` is the warrant-bearing key of the custody opener.
- R-16: `release` stays; `renounce` not adopted.
- R-17: the name `pardon` is a defect for a paid release (candidate `free`).
- R-29: `proclaim`, `declare`, `utter`, `issue`, `order` are five acts.

---

# GV — settlements and governance

Status: lane deliverable for the v2 rewrite (Part III by subsystem, Part V's GV table). Written 2026-10-17 against the working tree. Reference, not canon (CLAUDE.md §0.05): nothing here binds the engine; the verb table and its loader do. Sources opened are cited `path:line`; `VT` = `engine/season/verb_table.yaml`, `RO` = `engine/season/rosters.yaml`, `EG` = `engine/season/loop/effects_governance.py`, `GT` = `engine/season/state/gate.py`, `HR` = `engine/season/hole_register.yaml`, `TS` = `proposals/2026-10-16-troop-stock-design.md`, `VCD` = `proposals/2026-10-03-verb-coverage-and-gap-fill.md`, `v2-p4`/`v2-p8` = the v2 synthesis `verbs-04`/`verbs-08`, `WP5` = `workplans/valoria_master_workplan_v9_part5.md`, `XSC` = `research/cross_scale_action_catalogue_v1.md`, `FASE` = `research/fa_se_historical_precedent_research_v1.md`, `PGS` = `research/proactive_governance_scale_research_v1.md`, `COMP-1` = `research/valoria_game_precedent_companion_v1.md`. Gap ids are the register's (Part VII (`verbs-21`)). Etymology sources: **Wikt** (en.wiktionary, via the lookup tool), **L&S** (Lewis & Short, via the tool); anything else is tagged `[UNVERIFIED]`.

**The answer in six lines.**
1. GV ends with 20 rows:
   - 12 shipped. Three of them are rebuilt: `dispatch` renamed `order`, `succeed` re-voiced as the heir's claim, and `build` given its own plan. `release` is shared with other lanes.
   - 3 planned: `arrest`, `pardon`, `raze`.
   - 5 new: `tax`, `ration`, `proclaim`, and `evade` and `defy`, which replace the shipped slash row `evade / defy`.
   - 5 parked: `depose`, `abolish`, `patrol`, `charter`, `assess`.
2. `tax` is a row in its own right, not `issue` + `comply` + `transfer`. The tax-payer's answer is not part of the tax. The tax writes a standing levy (an `edict` Record) on a place, and MATTER reads it each season. The payer's `evade` or `defy` is his own act against that levy.
3. `ration`, `tax` and `proclaim` share one carrier, the `edict` Record kind, and one publication route. They are three rows because their readers and their moral weight differ. Under v2 §V.2.1 the chooser values the verb alone.
4. `arrest` and `pardon` stay rows. v2's folds into `seize` and `revoke` fail the fold test: the actor, the edge kind, the gate basis and the contest all differ.
5. Named folds that pass the test: `appoint`, `designate`, `elect`, `steward` and `rotate` on `confer`; `dismiss` on `revoke`; `amend` on `establish`; `resign`, `abdicate` and `abandon` on `release`; `annex` on `seize`'s Rung half; `fortify` and `improve` on `build`; `relieve` on `transfer`; `warrant` on `issue`; `repeal` on `destroy_record`.
6. Hand-offs: troop raising (`levy`) and garrisoning go to MB/FA; labour assignment and improvement-by-labour go to EC (`work`, and an `assign` that has no mechanic yet); `banish` goes to SC's `determine`; `audit` and `survey` go to FI.

---

## 3.1 Subsystem mechanic (what GV has in the engine today)

**Carriers.** Four carriers do the work:
- `Office`, with `remit_acts`, a `conferral` basis and a `revocation` basis.
- The seat `hold` Tenure, carrying `term` and `granted_acts`.
- `Rung`, with `stores` and a `contain` ladder over `rung_kinds` (person → realm; `RO` `rung_kinds`).
- `Site`, with `condition` against a works ceiling (`site_kinds`: harbour, seam, body, dwelling, garrison).

Records of kind `dispensation` (writs) and `works` (plans) sit beside them (`RO` `record_kinds`). The restraint Tenures `detain` and `ban` were added at SC-03a (`RO` `tenure_kinds`).

**Writers (shipped rows).**
- Seat rows: `confer` opens a seat `hold` (VT:168, `EG:57`); `revoke` closes another's hold under `revocation_bases` (VT:884, `EG:258`); `release` closes one's own edge (VT:845, `EG:207`); `establish` founds or re-remits an Office (VT:283, `EG:144`).
- Writ rows: `issue` mints a dispensation to one executor (VT:441).
- Store and taking rows: `requisition` moves a rung's stores into the seat's treasury (VT:646); `seize` takes a warranted Record or an occupied settlement (VT:898).
- Works rows: `found` and `build` mint a Rung or a Site from a held works (VT:367, VT:390).
- Answer rows: `comply` (VT:144) and `evade / defy` (VT:297) emit only.
- Two more emit only: `dispatch` (VT:268) and `succeed` (VT:935, effect declined).

**Readers.**
- Seat gates: `may_fill`, `may_revoke` and `purview_reaches` (`GT:614`, `GT:599`, `GT:352`, with IN-40's vassalage clause at `GT:388`).
- MATTER's draw and yield (`loop/matter.py:495-525`): yield = the Site's base × condition × the season factor, with no labour term.
- `restrained()` (`queries/world_q.py:1030`), read by `move`/`migrate`, `sides`, `oblige` and `confer`.

**What GV lacks.**
- No standing extraction: no rate, no recurring levy, no legitimacy coupling. FASE:91 says "there is no extraction decision anywhere".
- No act publishes to a purview (VCD §9.7).
- No draw policy.
- No labour input to yield.
- No office referent in computed play (HR H-203).
- No closer for a Rung or a Site (`raze`, planned).
- Custody: no row opens it except `determine`, and no row ends it.

v2-p8:372-375 also records that `requisition` and `revoke` execute 0 times in computed play.

## 3.2 Convention floor

"Shipped" = a verb row exists; "planned" = a workplan position names it; "designed" = only VCD or v2 has it; "absent" = nowhere.

| floor act | precedent (in-tree path:§ and/or game, mechanic) | state | GV verb |
|---|---|---|---|
| Found a settlement | Civilization [MEMORY]: settlers "Found City" create a new holding. PGS:51-64 §2A (endowed foundations) | shipped (VT:367) | `found` |
| Build in a settlement | XSC:233-234 §2.2 Develop / Fortify. PGS §2A S1, S5, S7. Total War [MEMORY]: settlement building slots with tiered chains | shipped (VT:390) | `build` |
| Improve / upgrade a building | Total War [MEMORY]: a built building is upgraded to the next tier in its chain. Mount & Blade: Warband [MEMORY]: village improvements (mill, watch tower) | absent as an act; `work` advances a fabric to its works ceiling (VT:1292) | `improve` folded on `build` (needs M-WORKS) |
| Fortify | XSC:234 §2.2 Fortify (Garrison / Militia / Walls). Jordan's garrison Site (`RO` `site_kinds` note, ED-IN-0279). Birthright [MEMORY]: "Fortify" domain action | shipped through `build` of a garrison Site | `fortify` folded on `build` |
| Assign workers | Banished [MEMORY]: worker counts per workplace. Frostpunk [MEMORY]: workers assigned to buildings. Dwarf Fortress [MEMORY]: labour toggles | absent: yield has no labour term (`loop/matter.py:504-520`) | handed to EC (`assign`, M-LABOUR) |
| Garrison troops | TS `verbs-02` §4.1 (a levy standing at a town defends beside the garrison Site). Total War [MEMORY]: garrisons raise public order and defend | designed (TS) | handed to MB (a `transfer` of a troop stock) |
| Tax | FASE:89-104 T1-T2 (Tilly, Levi, tax farming). XSC:239 §2.2 Levy; XSC:248-261 §2.3 Directive "Tax". Stronghold [MEMORY]: a standing tax rate that costs popularity. Birthright [MEMORY]: seasonal taxation by severity | designed (v2-p8 V145) | `tax` (NEW) |
| Requisition in kind | TS §3.4 (the store act). FASE T3 (Book of Orders force-sales) | shipped (VT:646) | `requisition` |
| Raise troops | TS §3.1 `levy`. PW:45 (feudal levy). COMP-1 §2.3 (RoTK "Conscript" drops Safety) | designed (TS) | handed to MB/FA (`levy`) |
| Ration | PGS:58-59 S8-S9 (assize, narh). Stronghold [MEMORY]: a food-ration level that trades stocks for popularity. Frostpunk [MEMORY]: food laws | designed (v2-p8 V148, parked) | `ration` (NEW) |
| Relieve dearth / open the granary | FASE:105-113 T3 (cura annonae, ever-normal granaries). HCC:296 §5 #5. PGS:60 S10 | designed (v2-p8 V149) | `relieve` folded on `transfer` |
| Decree / law | COMP-1:203-206 §2.4 (decree with a compliance roll). Birthright [MEMORY]: "Decree" domain action. Victoria 3 (COMP-1 §2.2 law enactment) | designed (VCD §9.7 `proclaim`, deferred) | `proclaim`, plus the content rows `tax` and `ration` |
| Appoint | COMP-1:166-169 §2.3 (CK council-seat denial). Crusader Kings 3 [MEMORY]: grant a title or a council seat. XSC:279 §2.5 Grant Subnational Management | shipped (VT:168) | `appoint` folded on `confer` |
| Dismiss | XSC:279 §2.5 Revoke Subnational Management. Crusader Kings 3 [MEMORY]: "Revoke Title" priced in tyranny. FASE T5 (recall) | shipped (VT:884), 0 executions | `dismiss` folded on `revoke` |
| Make an office | Dwarf Fortress [MEMORY]: nobles and positions assigned from a fixed list. Crusader Kings 3 [MEMORY]: create a title | shipped (VT:283) | `establish` |
| Resign / abdicate | Crusader Kings 3 [MEMORY]: "Abdicate" decision. GOV-conf:41 (recusatio) | shipped as `release` of a seat `hold` (`EG:216-220`) | `resign` / `abdicate` folded on `release` |
| Succeed to a seat | FASE:161-167 T9. Crusader Kings 3 [MEMORY]: the heir inherits by succession law | planned (IN-61 re-specifies `succeed`) | `succeed` |
| Annex a place | Civilization [MEMORY]: a captured city is kept or razed. COMP-1:195-200 §2.4 (dedizione vs colour change) | shipped (`seize` Rung half) | `annex` folded on `seize` |
| Raze | Civilization [MEMORY]: "Raze city" | planned (IN-12 step 11) | `raze` |
| Abandon a holding | Civilization [MEMORY]: abandon/raze one's own city (variants) | shipped as `release` of a Rung `hold` | `abandon` folded on `release` |
| Arrest / imprison | VCD:1605-1610 (L.A. Noire, CK3 imprison). Crusader Kings 3 [MEMORY]: imprison | planned (IN-12 step 5) | `arrest` |
| Pardon / free | VCD:1735-1739 (royal pardon, CK3 release). Crusader Kings 3 [MEMORY]: release from prison | planned (IN-12 step 5) | `pardon` |
| Keep order | XSC:235 §2.2 Keep Order. Frostpunk [MEMORY]: "Guard Patrol" law. Total War [MEMORY]: public order | absent: no disorder quantity | `patrol` (PARK) |

The floor is twenty-three acts. Three leave GV: assign workers goes to EC; garrison and raise troops go to MB/FA. Twenty stay in GV as rows or named folds; one of them, keep order, is parked on a missing quantity.

---

## 3.3 Suites

**Fold test.** Each fold below answers three questions: same actor? same subsystem mechanic? differs only in a parameter or a content? A fold must answer yes to all three (the lane brief rule 5).

**Value-term clause.** v2-p8 §V.2.1 says the chooser's value term reads the verb alone. So two acts whose alignment would differ in sign cannot share a row, even when the write is shared. This is v2-p4:161's closest-call-1 test, applied consistently. I count it under "same mechanic".

**NERS** follows `skills/ners/SKILL.md` as CLAUDE.md §0.06 defines it, written tersely:
- **N** is tested from six directions: TD (top-down), BU (bottom-up), V (vertical), D (diagonal), La (lateral), H (horizontal).
- **E** is scored last, as a ratio against N and R.

### Suite 1 — Seats: filling, emptying and making offices

**Host verbs.**
- `confer`: fills a seat (SHIPPED, VT:168).
- `revoke`: empties another's seat (SHIPPED, VT:884).
- `establish`: makes or amends an office (SHIPPED, VT:283).
- `succeed`: the heir takes the throne (SHIPPED row; re-specified by IN-61).
- `release`: the holder lets go. The row is SHIPPED and cross-cutting (VT:845); GV names its seat and place uses.

**Folded acts.**

| act | host | same actor? | same mechanic? | param/content only? | line |
|---|---|---|---|---|---|
| `appoint` | `confer` | yes | yes | yes: basis `appointed` | the plain word for a conferral on an `appointed` seat (`RO` `conferral_bases`) |
| `designate` (heir) | `confer` | yes (the King's remit) | yes | yes: object is the heir title `off_heir` | RS-27, verbatim at WP5:213: *"designated heir is not a verb but a status or title"*. So designation is a conferral of a title; IN-61 authors `off_heir: appointed` |
| `elect` | `confer` | yes (the presiding seat) | yes | yes: basis `elected` | the voters' act is SC's `vote` (= their own `commit`, v2-p8 V127). The fill reads a count; the count reader is missing (M-COUNT) |
| `steward` / regent | `confer` | yes | yes: a termed `hold` on a second seat over the domain | yes: `term` plus a second seat | Layer 1's route as IN-48 restates it (WP5:179): "`establish` a second seat over the domain, `confer` it, IN-10's `Tenure.term`". An early dismissal needs a basis (M-DELEGATE) |
| `rotate` (term limit) | `confer` | yes | yes | yes: `term` | VT:182: "a termed one is REGENCY or a TERM-LIMITED SEAT, matured at MATTER" |
| `dismiss` | `revoke` | yes | yes | no difference | the ordinary word for the act on a person; `revoke` is the word for the act on the appointment. One act |
| `amend` (re-remit) | `establish` | yes | yes: `Office.remit_acts` through `_grant_remit` | yes: an existing id | `EG:197-203` already earns `remit.changed` rather than `office.established` for an existing id. Critic L-07's split is met by naming the fold; a second row would duplicate the effect |
| `resign` / `abdicate` | `release` | yes (the holder) | yes: the holder closes his own edge | yes: the edge is a seat `hold` | `EG:216-220`: "A PERSON CAN NOW RESIGN AN OFFICE". `abdicate` is the same act when the seat is the realm's top seat |

**Not folds** (each test fails):

| candidate | proposed absorber | which test fails | consequence |
|---|---|---|---|
| `succeed` | `confer` | actor and basis: the heir claims by his own act through `inheritance`, and IN-61 makes `may_fill` refuse `inheritance` for `confer` (WP5:213) | stays a row |
| `depose` | `revoke` | basis: the top seat is "stripped by nobody" (`RO` `revocation_bases`) | PARK |
| `depose` | `seize` | object: "A SEAT is never seized" (VT:911) | PARK |
| `abolish` | `establish` (empty remit) | write: closing `Office.exists` is not a remit write, and nothing says what happens to a live hold on a dissolved seat | PARK |

**World effect.** Each host writes the following, and each lacks something:

| host | writes and emits | lacks |
|---|---|---|
| `confer` | `Tenure.since`, `Tenure.until`, `Tenure.term`; emits `tenure.opened` / `tenure.closed` | an office referent in computed play (H-203); a count reader for `elected` (VT `conferral_bases` note: "NOTHING DISCRIMINATES BETWEEN THE THREE YET") |
| `revoke` | `Tenure.until`; emits `tenure.closed` | a reachable remit (H-91), a cost (H-100), and any execution |
| `establish` | `Office.exists`, `Office.remit_acts`, `Tenure.payload`; emits `office.established` / `remit.changed` | — |
| `release` (seat) | `Tenure.until`; emits `tenure.closed` | its own kind: `tenure.closed` has three emitters, so a witnessed resignation is valued at zero (v2-p8 §V.2.4) — M-RESIGN |
| `succeed` | declined | its effect waits on IN-61 (M-INHERIT) |

**NERS** (host set):
- **N.**
  - TD: canon's seat-holders exist only if seats change hands.
  - BU: a person's ambition aims at a seat (`confer` is "the only act that fills a seat", v2-p4:136).
  - V: the realm seat reaches down by `revoke` under `rung_above_*` (`RO` `revocation_bases`).
  - D: delegation (IN-48) and vassalage (`GT:388`) cross faction and rung.
  - La: `oblige` (NP/FA) binds to the seats these verbs fill.
  - H: succession and abdication end a reign at any rung.
  - What dies on a cut: cutting `revoke` leaves seats only resigned or never emptied (the 2026-09 table defect `EG:216-218` names the mirror case). Cutting `succeed` leaves a dead king's throne fillable only by a regent's `confer`, which IN-61 refuses on purpose.
  - False N-line check: `release` does not provide what `revoke` provides; the actors differ.
- **R.** Seats appointed, elected and annexed differ by basis (customization). A termed seat makes regency and term limits (FASE T5 rotation). Abdication and succession make narrative without a player: a death opens a throne that the heir must claim (IN-61 EXIT).
  - Completeness at the extremes fails in two places: the top seat cannot be emptied against its holder, and an elected seat has no count.
- **S.** One gate (`GT`) answers who may fill and who may strip, for every seat. `release` is Layer 1 row 14's generic closer, so no per-kind antonym is grown (`EG:211-214`). Calculations are consistent.
  - Pauses: none required.
- **E** (ratio). Five hosts for some twelve player-facing acts, each named in the player's word. The overhead is two remit acts (`confer`, `revoke`) that also gate other rows (L-18).

**Precedent.** COMP-1:166-176 §2.3 (CK council denial; the Total War governor null). FASE:123-132 T5 (residencia, avoidance, rotation) and FASE:161-167 T9 (interregnum, regency). Crusader Kings 3 [MEMORY]: grant title, revoke title, abdicate. Dwarf Fortress [MEMORY]: appointed positions.

**Gaps.**
- Closed: GV-G07, G08, G17, G18, G19, G20, G22, G38 (term), G44, G45. Each is conditional on a named mechanic; see §3.6.
- Left open or parked: G21 (`depose`), G41 (`abolish`).

**Dispositions.**
- `confer`: KEEP-AS-IS. Falsifier: a computed `confer` never executing once H-203's office referent lands.
- `revoke`: KEEP-AS-IS. Falsifier: `revoke` still at 0 executions after H-91 and H-203 are lifted.
- `establish`: KEEP-AS-IS, with `amend` named. Falsifier: an existing-id establish earning `office.established`.
- `release` (GV uses): KEEP-AS-IS with three named acts.
- `succeed`: REBUILD per IN-61 (actor = heir). Falsifier: IN-61's own (WP5:215), "a hold opened through `inheritance` for an actor who does not hold the registered heir seat".
- `depose`: PARK. Trigger: Jordan rules ARC-40's *replaced* arm in (D-V1).
- `abolish`: PARK. Trigger: a reader of a hold on a closed Office.

### Suite 2 — Writs, orders and the answer

**Host verbs.**
- `issue`: a written writ to one executor (SHIPPED, VT:441).
- `order`: the spoken order; this is the shipped `dispatch` renamed (REBUILD).
- `comply`: answer by doing (SHIPPED, VT:144).
- `evade`: covert refusal (NEW ROW, split from VT:297).
- `defy`: open refusal (NEW ROW, split from VT:297).

**Folded acts.**

| act | host | same actor? | same mechanic? | param/content only? | line |
|---|---|---|---|---|---|
| `warrant` | `issue` | yes | yes: `Record.exists`, kind `dispensation` | yes: `terms` names a person or a Record | `seize` and `arrest` read a held warrant (VT:911; VCD:1580-1583). Not a row |
| `commission` | `issue` | yes | yes | yes: `terms` names a charge | r2's `commission` kind "lands with the effect that mints it" (`RO` `record_kinds` note). Named, not built |

**Not folds** (each test fails):

| candidate | proposed absorber | which test fails |
|---|---|---|
| `evade / defy` | `comply` (v2-p4:146) | value term: the shipped `hierarchical_equal` cells are opposite in sign, +0.9 against −0.6 (v2-p4:161) |
| `evade` | `defy` | mechanic: covert versus open. VCD:4069 says the slash row "collapse[s] into one `compliance.withheld`". `evade` must reach the issuer only on detection; `defy` must reach him at once |
| `order` | `issue` | mechanic: an order mints no Record, so there is no writ to bind (VT:160, `comply`'s note: "ARM (A)'s `dispatch`ed ORDER IS NOT ANSWERED: an order mints no Record"). v2-p8 §V.2.7 kept `dispatch` (`tests/test_fa01_head_seats.py:56-59`) |

**World effect.**

| host | writes and emits | lacks |
|---|---|---|
| `issue` | `Record.exists` (a dispensation held by the issuer); emits `dispensation.issued` | a writ reaching its executor in computed play (H-203); which acts a writ's `terms` may name (H-44) |
| `comply` | writes nothing; emits `compliance.given` (VT:161-162). The performance is the executor's own named act, not a GV composition | — |
| `evade` (new) | writes nothing on a writ; emits `compliance.evaded`. That kind is deposited on the issuer only when a witness sees it (`conceal`, FI, IN-12 step 10). On a tax `edict` it reduces the actor's hearth's share at MATTER (M-TAX) | the detection route (FI `conceal`) |
| `defy` (new) | writes nothing on a writ; emits `compliance.refused` through the issuing seat's `post_remit` channel, so the issuer learns that season. On a tax `edict`, MATTER withholds the rung's take for that season (M-TAX) | the edict carrier (M-EDICT) |
| `order` | writes nothing; emits `order.given`. The kind reaches persons only through the generic channels: chronicle, co-location, and the ordering seat's obligees (`epistemic.py:460-480`, `:563-570`). Nothing addresses it to the person ordered. `person.demanded` on refusal is read by CENSUS (VT:279) | a delivery to the person ordered, and a reader that forms his Candidate from the held claim (M-ORDER). VCD:4048: "no decision reads `order.given`" |

Under criterion 6, `order` is a verb only once M-ORDER exists. Until then it is a named gap, not a cull: FA-01 pins five heads acting through it.

**NERS.**
- **N.**
  - TD: canon's dual authority, where the province demands and the governor answers (XSC:248-261), needs a demand and an answer.
  - BU: the answer is where a ruled person chooses resistance (v2-p4:144).
  - V: a writ crosses rungs by purview (VT:462 `authority`).
  - D: the warrant feeds `seize` and `arrest`.
  - La: `defy` is the open-refusal deed that FA's rebellion and NP's grudges read.
  - H: across seasons, the Scott invariance mechanism (FASE:105-113) needs repeated refusal.
  - What dies on a cut: cutting `evade`/`defy` deletes the one seat of resistance. That is the reason v2's court reversed the tax-into-requisition merge (v2-p8:587).
  - False N-line check: `comply` withheld (silence) is not refusal. Silence emits nothing, and "silence beats refusal" is SC-G04's defect.
- **R.**
  - Covert versus open refusal is the strategic fork that XSC §2.3 builds its suspicion track on.
  - The issuer's response (arrest, requisition, revoke) gives a narrative without a player.
  - At the extremes: a writ to an absent executor refuses (`issue.refused`), which is complete.
- **S.**
  - One answer channel serves writs and edicts.
  - The kinds `compliance.given`, `.evaded` and `.refused` form one family, so witnesses judge each by its own kind.
  - Pauses: none.
- **E.** Five rows for the demand-and-answer cycle. Splitting the slash row adds one row and removes one MISFIT name.

**Precedent.**
- XSC:248-261 §2.3: Comply / Bargain / Defy.
- COMP-1:203-206 §2.4: a decree with a compliance roll; "promulgation did not equal enforcement".
- FASE:89-97 T1: Levi's quasi-voluntary compliance.
- Crusader Kings 3 [MEMORY]: vassals refuse a call to arms when opinion is low.

**Gaps.** Closed: GV-G03, G04, G05, G06, G34, G35. G35 is closed for taxation by `tax`; for other writs the residue sits with v2-p8 §V.2.2's keys channel.

**Dispositions.**
- `issue`: KEEP-AS-IS. Falsifier: a warrant `seize` reads that `issue` cannot mint.
- `comply`: KEEP-AS-IS. Falsifier: a writ whose performance needs a second actor's act to land.
- `evade`: NEW ROW. It is typed on `comply`'s cell, which `60073e75` already wrote (VT:303). Falsifier: `evade` and `defy` earning the same witnessed kind.
- `defy`: NEW ROW, typed the same way and falsified the same way.
- The slash row `evade / defy`: RETIRED in the same commit that adds the two rows. It is the split, not a cull.
- `order`: REBUILD (rename; the remit act stays `dispatch`). Falsifier: a test or reader keyed on the verb string `dispatch` that is not re-keyed.

### Suite 3 — Public law: the edict and its publication

**Host verb.** `proclaim` (NEW ROW; designed at VCD §9.7, deferred at K-50). A seat's statement or rule, addressed to a place in its purview and published to the persons who live there.

**The shared carrier.** VCD:1480 designed the proclamation as a Proposition. It cannot be one here. A Proposition carries no `kind` or `amount` key (v2-p8 §V.2.2, Premise 1), and it cannot be held, seized or destroyed. A standing rule must be repealable, and its holder must be able to lose it. So `proclaim` mints a Record of a new kind `edict` [ASSUMPTION: medium; `dispensation`'s precedent]. Its keys:
- `kind`: one of a roster (`notice`, `tax`, `ration`; later kinds only with their readers);
- `at`: the rung;
- `amount`: a rate or quantity, absent for a notice;
- `until`: a season, or open.

`tax` and `ration` (Suite 4) mint the same kind through their own rows, so there is one carrier and one publication route.

**Why `proclaim` is not `issue`.** `issue`'s `executors` conjunct requires a Person addressee: "a writ addressed to a rung is refused" (VT:462). That is a ruled clause (§37.1, VT:447). A place-addressed edict therefore cannot ride `issue` without overwriting it. The fold test fails on the counterparty class and on delivery: one executor against every resident.

**Folded acts.**

| act | host | same actor? | same mechanic? | param/content only? | line |
|---|---|---|---|---|---|
| `decree` (a notice with no standing reader) | `proclaim` | yes | yes | yes: `kind: notice` | the player's word "decree" for a rule. Any decree whose content changes the world gets its own row when its reader exists (VCD:1452: "a kind ships only with its reader"; VCD:1480-1481 defers embargo, interdict, emergency and edict on exactly that ground) |
| `repeal` | `destroy_record` | yes (the edict's holder) | yes: `Record.exists` false | yes: the Record is an edict | `destroy_record` is shipped (VT:210) but fires on neither eligibility alternative (H-75). Named; waits on H-75 |

**Parked.** `charter`: an edict of exemption granted to a body or a place.
- Its reader is unbuilt. VCD:1484 routes a charter as "a `dispensation` whose `terms` is the grantee" through `issue`, with "a `purview_reaches` exemption (unbuilt)". That route covers a person-grantee only; a town-grantee fails `issue`'s executors clause.
- Its value term is opposite in sign to `tax`'s, so it cannot be a fold.
- Trigger: M-EDICT lands, and `purview_reaches` (`GT:352`) gains an exemption clause read by the edict readers.

**World effect.**
- Writes `Record.exists` (kind `edict`, held by the seat's holder).
- Emits `edict.proclaimed`, deposited to residents of `at`'s subtree. This is a new publication route; the chronicle is slated for deletion at SC-01 step 13 (v2-p8 §V.2.11).
- Lacks: the `edict` kind in `RO` `record_kinds`, and the publication deposit (M-EDICT).

**NERS.**
- **N.**
  - TD: canon's instant-global-decree error, the "single most common error in governance games" (COMP-1:204-205), is avoided only if a decree lands per locality.
  - BU: a resident must be able to learn the law in order to evade or defy it.
  - V: the edict travels down the containment tree.
  - D: tax and ration ride the same carrier.
  - La: SC's `deny` and FA's `declare (war)` need the same public route (v2-p8 §V.2.11).
  - H: a standing edict persists across seasons until repealed.
  - What dies on a cut: a seat "cannot tell its own purview anything" (VCD:2158).
  - False N-line check: `tell` reaches one co-located hearer, not a purview.
- **R.** Repeal-and-reissue is a narrative lever. The quo warranto pattern (FASE T4) arrives later through `charter`.
- **S.** One carrier and one publication route for every standing rule. The calculation is MATTER's alone.
- **E.** One new row and one new Record kind for a family of rules. That is good value, if the roster of `kind`s grows only with readers.

**Precedent.**
- COMP-1:203-206 §2.4.
- FASE:114-121 T4 (charters, quo warranto).
- Birthright [MEMORY]: the "Decree" domain action.
- VCD:2208-2215 §9.7 evidence rows.

**Gaps.**
- Closed: GV-G23, and G24 for the edict and tax halves.
- Parked: G25 (`charter`).
- Flagged to EC: embargo and interdict.

**Dispositions.**
- `proclaim`: NEW ROW. Falsifier: a resident of `at` never holding the edict's claim in the season it is proclaimed.
- `charter`: PARK.
- `repeal`: FOLD.

### Suite 4 — Treasury and dearth

**Host verbs.**
- `tax` (NEW ROW): a standing levy on a place's yield.
- `requisition` (SHIPPED, VT:646): a one-off taking from a place's stock.
- `ration` (NEW ROW): a standing cut to a place's draw.
- `transfer` is EC's row; GV names `relieve` on it.

**The discriminator between `tax` and `requisition`.**

| | `requisition` | `tax` |
|---|---|---|
| when | now, once | each season, standing |
| what it takes | stock (`Rung.stores`) | yield (MATTER's `yield` step) |
| what it writes | `Rung.stores` ×2 at once (`EG:374`) | an `edict` (kind `tax`) that MATTER reads |

Ordinary English draws the same line. To requisition is to demand supplies for official use; a tax is a recurring compulsory levy. A one-shot "tax" of N from stock is a requisition with a different amount. That passes the fold test, so it is not a third act.

**Folded acts.**

| act | host | same actor? | same mechanic? | param/content only? | line |
|---|---|---|---|---|---|
| tax farming, a fixed quota (the *encabezamiento* of XSC:243) | `tax` | yes | yes | yes: `amount` as a fixed sum, not a rate | FASE T2 |
| remission in dearth (Scott) | `tax` | yes | yes | yes: a lower `amount`, or `until` now | FASE:108. Not given its own name, because "remit" collides with `remit_acts` |
| `relieve` | `transfer` (EC) | yes: a seat-holder paying "THROUGH" the seat (VT `transfer` `eligibility_note`) | yes: `Rung.stores` ×2 | yes: the destination is a rung in shortfall; earns `relief.given` beside `transfer.made` | v2-p8 V149, mechanism in v2-p8 §V.2.4. Same sign as upkeep payment, so the value-term clause passes |

**Not folds** (each test fails):

| candidate | proposed absorber | which test fails |
|---|---|---|
| `tax` | `issue` + `comply` → `transfer` (v2-p8 V145) | three actors across three acts (issuer, executor, payer). the lane brief rule 5 forbids that composition. V-15 adds that it rested on a row v2 itself retired |
| `tax` | `requisition` (v2-p4:126) | mechanic: standing against one-off; yield against stock |
| `tax` | `proclaim` | value term: an extraction against a notice; the content needs its own reader |
| `ration` | `transfer` (v2-p4:129) | mechanic: nothing moves between rungs; the draw per mouth changes |
| `ration` | `tax` | mechanic: MATTER's draw step against its yield step; one rung against two |

**World effect.**
- `tax` writes `Record.exists` (`edict`, kind `tax`) and emits `tax.levied`. Each season MATTER moves `amount` of the rung's yield into the issuing seat's treasury, the rung of `Act.via` as for `requisition`, emitting `tax.collected`. A live `defy` that season withholds the take (`tax.withheld`); `evade` reduces it.
  - Legitimacy coupling: FASE:91 gives Levi's yield as rate × base × f(L). f(L) is 1 until IN-23's legitimacy Query exists.
  - Lacks: everything in M-EDICT and M-TAX.
- `ration` writes `Record.exists` (`edict`, kind `ration`) and emits `ration.set`. MATTER's draw per mouth at `at` is cut by `amount`.
  - Lacks: the draw reader (M-DRAW). Jordan's draw-policy ruling (v2-p8 §V.5.1, "Already Jordan's, and now load-bearing") must come first.
- `requisition`: shipped as is.

**NERS.**
- **N.**
  - TD: FASE T1 "war made the state": extraction is the upstream half the corpus lacks (FASE:91).
  - BU: the subsistence ethic (FASE:108) needs a standing demand that can stay invariant under dearth.
  - V: the seat's treasury is fed from rungs below by purview.
  - D: troops eat from the same stores (TS §2.5); `levy` is MB's.
  - La: `evade`/`defy` (Suite 2), `relieve`, and EC's trade read the same stores.
  - H: the tax and the ration persist across seasons.
  - What dies on a cut: cutting `tax` leaves no extraction decision. Cutting `ration` leaves dearth with only one answer (relief) and the hard choice gone. Stronghold's two sliders [MEMORY] are the genre's convention.
  - False N-line check: `requisition` already moves stock to the treasury, but only once. The standing demand and its invariance mechanism are not provided by it.
- **R.**
  - Rate, quota and remission (customization).
  - Tax farming (FASE T2).
  - The Scott detonation: invariance under dearth leads to `defy`, a narrative with no player.
  - At the extremes: a rate of 0 is remission; a rate above yield is capped by stores; a ration of 0 is famine, priced by body.
  - Limit: H-211 says a body only falls, so recovery is silent until its cause 1 is built.
- **S.** MATTER remains the one owner of every per-season quantity. Tax and ration are read there, not computed in the verb. One carrier with Suite 3.
- **E.** Two new rows. Each is one plain word that predicts its outcome. The overhead is the `edict` kind, which they share.

**Precedent.**
- FASE:89-113 T1-T3.
- PGS:58-60 S8-S10.
- XSC:239, :243 §2.2 (Levy, Negotiate Quota).
- HCC:104-116 §2.6.
- Stronghold [MEMORY]: tax rate and ration level against popularity.
- Frostpunk [MEMORY]: food laws.
- Birthright [MEMORY]: tax severity by season.

**Gaps.**
- Closed: GV-G27, G28, G29, G35.
- Parked: G32, G33 (`assess`).
- Out of scope: G01 (stale), G02 (MB/FA), G30.

**Dispositions.**
- `tax`: NEW ROW. Falsifier: with a live tax edict and no defiance, the treasury rung's stores not rising at MATTER.
- `ration`: NEW ROW. Falsifier: the draw at `at` unchanged under a live ration edict.
- `requisition`: KEEP-AS-IS. Falsifier: a requisition that cannot be told from a one-season tax by its writes.
- `relieve`: FOLD. Falsifier: `relief.given` earned for a transfer to a rung with no recorded shortfall.
- `assess`: PARK. Trigger: `tax` reads an assessed base rather than actual yield (XSC:242 Survey's stale-assessment failure mode).

### Suite 5 — Custody and justice

**Host verbs.**
- `arrest` (NEW ROW, planned IN-12 step 5, VCD:1570-1611): take a person into custody under a warrant.
- `pardon` (NEW ROW, planned IN-12 step 5, VCD:1710-1740): end another's `detain` or `ban`.
- `seize` (SHIPPED, VT:898): take a warranted Record, or an occupied settlement.

**Folded acts.**

| act | host | same actor? | same mechanic? | param/content only? | line |
|---|---|---|---|---|---|
| `annex` | `seize` (Rung half) | yes (the occupying seat's holder) | yes: closes the holder's `hold` on the town and opens his own (VT:913 `writes_note`) | yes: the object is a settlement | ordinary "annex" means to take territory as one's own. Re-parenting the town's `contain` under the annexer's ladder is not written; that is a named gap (M-ANNEX) |
| `lift a ban` / `free` a prisoner by grace | `pardon` | yes | yes | yes: the edge kind is `ban` or `detain` | one act. "release a prisoner" is the ordinary phrase, but `release` is the own-edge closer (Suite 1) |

**Not folds** (each test fails):

| candidate | proposed absorber | which test fails |
|---|---|---|
| `arrest` | `seize` (v2-p4:149) | object: `seize` declines anything not a held Record or occupied settlement (VT:911). Write: `detain` against `hold`. Contest: `arrest` is contested ("resisting arrest", VCD:1572) and `seize` is not. Eligibility: `remit:dispatch` (the enforcement seat) against `remit:issue` |
| `pardon` | `revoke` (v2-p4:150) | edge kind: `detain`/`ban` against a seat `hold`. Basis: the determination basis that `GT:1105-1119` already admits for closing restraint kinds, against `revocation_bases`. Value term: mercy against dismissal (v2-p4:164) |
| `pardon` | `release` | actor: `release` is own-only (`EG:248-250`). A prisoner cannot end his own `detain`: `RESTRAINT_KINDS` sits outside `RELEASABLE_KINDS` (`data/rosters.py:462-473`) |
| `detain` (as a verb) | — | not a verb. It is the Tenure kind that `arrest` and `determine` open (criterion 6: an outcome, not an act) |
| `ban` (as a verb) | — | likewise. The act that opens it is `determine`'s disposal (SC). "Banish" names that disposal and is flagged to SC |

**World effect.**
- `arrest` writes `Tenure.since` (kind `detain`, prisoner → the warrant's issuing seat) and emits `arrest.made` / `arrest.resisted`.
- `pardon` writes `Tenure.until` and emits `detention.ended` / `ban.ended`.
- The readers already exist:
  - a detained man cannot `move` or `migrate` (`loop/effects_migration.py:52, :184`) and is struck from sides (`loop/sides.py:123`);
  - a banned man can be neither seated nor sworn (`EG:105`; `loop/predicates.py:397`).
- `pardon`'s write basis is already in the gate: a bench closing `detain`/`ban` on its own seat (`GT:1112-1119`).
- What is lacking:
  - the rows themselves;
  - `arrest`'s contest (it stands at [CONFIDENCE: medium] at VCD:1594);
  - J-8 (is `dispatch` a remit act), which VCD:1578 names.

**NERS.**
- **N.**
  - TD: canon's custody, outlawry and excommunication states (VCD:1466-1468).
  - BU: a person can be taken, held and freed.
  - V: a warrant runs from a seat to its enforcement seat.
  - D: SC's `determine` opens what `pardon` closes, and PC's `fight` is the body half.
  - La: `move`, `sides` and `confer` read the restraint.
  - H: a sentence persists until pardoned.
  - What dies on a cut: without `pardon`, a tribunal's disposal is a ratchet (SC-G47, PS/10 P-12). Without `arrest`, custody opens only after a trial, never before it.
  - False N-line check: `seize` already "takes", but `seize` declines a person.
- **R.** Arrest, trial and pardon form a full loop. Ransom, rescue and capture lean on these rows (v2-p8:706-710). Mercy has its own cells (v2-p4:164).
- **S.** One restraint read, `restrained()`, serves every reader. `pardon` closes on the same gate basis that `determine` opens on.
- **E.** Two planned rows. Each is a plain, current legal word.

**Precedent.**
- VCD:1605-1610 and VCD:1735-1739 evidence rows.
- RHET:289-290 §7.2.
- Crusader Kings 3 [MEMORY]: imprison, and release from prison.
- The English constable (VCD:1609).

**Gaps.**
- Closed: GV-G10, G11, G13.
- Stale: G12.
- Out of scope: G39, G40 (SC and PC).

**Dispositions.**
- `arrest`: NEW ROW (planned). Falsifier, from VCD:1603: "`move` refused for a person holding a live `detain` edge" after a computed arrest.
- `pardon`: NEW ROW (planned). Falsifier, from VCD:1733: the former prisoner's `move` admitted the next season.
- `seize`: KEEP-AS-IS. Falsifier: a settlement taken without the occupier's seat's faction being mustered there.

### Suite 6 — Places and works

**Host verbs.**
- `found` (SHIPPED, VT:367): a new place, which the founder holds.
- `build` (SHIPPED, VT:390): a new fabric in a place. Disposition REBUILD (below).
- `raze` (NEW ROW, planned IN-12 step 11): end a place or a fabric.

**The `found` / `build` / `establish` discriminator** (critic L-07):

| verb | its object | the extra it writes |
|---|---|---|
| `found` | a Rung (a place on the containment ladder) | the founder's `hold` on it (VT:371). This creates a holding, a political object. Ordinary "found a town" |
| `build` | a Site (a fabric) | no hold: "a `hold` never reaches a Site" (VT:406). Ordinary "build a wall, a harbour" |
| `establish` | an Office (Suite 1) | ordinary "establish an office" |

So `found` and `build` differ in mechanic, not only in parameter: one opens a Tenure and the other does not. v2's merge (v2-p4:147) fails the fold test, and both rows stay.

**Folded acts.**

| act | host | same actor? | same mechanic? | param/content only? | line |
|---|---|---|---|---|---|
| `fortify` | `build` | yes | yes | yes: the plan's Site kind is `garrison` | Jordan's "a Site's condition" ruling (`RO` `site_kinds` note, ED-IN-0279); TS `verbs-02` §4.1 reads garrison strength from it |
| `improve` / upgrade | `build` | yes | yes: works → fabric, paid from the works' rung (`works_cost`) | yes: an existing Site of the planned kind, with its ceiling raised | conditional. `build` today refuses a works "already built" (VT:411), and the ceiling belongs to the works. Needs M-WORKS (b). Labour toward the ceiling is EC's `work` (VT:1292) |
| `abandon` | `release` (Suite 1's host) | yes (the holder) | yes | yes: the edge is a `hold` on a Rung | the place persists unheld. De-founding on zero presence is a CENSUS repair, not an act (HR H-166 limit 3) |

**`build` REBUILD.** A player's "build a granary here" is one act. Today it takes two: `create_record` of a works, then `build` (VT:395-404). Rule 5 forbids several steps for one floor act. `build` (and `found`) should accept the plan, `{kind, at}`, as the act's own content and mint the works inside the act when the actor holds none. The separate route stays for a works handed on by `give`; VT:381 notes "so a rival may become master of a works and found it". [ASSUMPTION: medium. The mint inside the act is `issue`'s precedent, where a Record is minted by the act that uses it.]

**Not folds.**
- `raze` → `destroy_record`: object. A Rung or a Site is not a Record.
- `raze` → `seize`: write. Ending a place is not a change of holder.

**World effect.**
- `found` writes `Rung.exists`, `Tenure.since` and `Rung.stores`.
- `build` writes `Site.exists` and `Rung.stores`.
- `raze` (planned) writes `Rung.exists` or `Site.exists` false, and must re-house the persons a Rung contains (HR H-166 limit 3; VCD:1812 "left placeless by the cascade").
- What is lacking:
  - a computed works source (H-165 limit 2);
  - the in-act plan;
  - the existing-Site upgrade;
  - `raze`'s re-housing rule.

**NERS.**
- **N.**
  - TD: canon's settlements grow and fall.
  - BU: a person's works becomes a place he holds.
  - V: a founded Rung joins the ladder under its `at`.
  - D: the garrison Site's condition is the town's defence for MB (TS `verbs-02` §4.1).
  - La: EC's `work` and `restore` raise what `build` made.
  - H: wear lowers condition each season.
  - What dies on a cut: cutting `found` removes holding creation. Cutting `raze` leaves `found`/`build` with no closer, which is H-166 limit 3.
  - False N-line check: `restore` raises condition but makes nothing new.
- **R.** Settlement customization through site kinds and their order. A raze is a narrative event. At the extremes, a full rung grows capacity by building (VT:404).
- **S.** One works → fabric pipeline and one cost table (`works_cost`). Calculations are consistent with `restore`'s rise.
- **E.** Three rows for the place life-cycle. The two-step plan is the overhead the rebuild removes.

**Precedent.**
- PGS:51-64 §2A.
- XSC:233-234 §2.2 (Develop, Fortify).
- Civilization [MEMORY]: Found City / Raze.
- Total War [MEMORY]: building tiers.
- Mount & Blade: Warband [MEMORY]: village improvements.

**Gaps.**
- Closed: GV-G15, G16, G26 (Develop and Fortify).
- Parked: G31 (`patrol`, below).

**Dispositions.**
- `found`: KEEP-AS-IS. Falsifier: a founded Rung with no founder's `hold`.
- `build`: REBUILD (the in-act plan). Falsifier: a `build` that executes without paying `works_cost`.
- `raze`: NEW ROW (planned). Falsifier: a person whose `contain` points at a razed Rung after the act.
- `patrol`: PARK. Trigger: a disorder or hazard quantity exists (IN-23's stability Query is the candidate), together with a reader of co-located guards. Keep order is a floor act (Total War public order, Frostpunk Guard Patrol [MEMORY]), so this is a PARK on a missing quantity, not v2's CUT (v2-p8:480).

---

## 3.4 Lexicon

**Notation.** Etymology sources: **Wikt** = Wiktionary via the tool; **L&S** = Lewis & Short via the tool; a link not checked is tagged `[UNVERIFIED]`. "→" in the status column marks the host of a fold.

**Fit rule.** The fit verdict is by ordinary current usage (ED-IN-0179), never by the root.

| verb | suite | status | mechanic and world effect (carrier) | etymology (sources) | fit | rename |
|---|---|---|---|---|---|---|
| `confer` | 1 | SHIPPED | opens a seat `hold` under the office's `conferral` basis (`Tenure.since`/`term`); `tenure.opened` | EModE *conferre* ← MF *conférer* ← OF *conferer* (Wikt) ← L *cōnferō, cōnferre, contulī, collātum*: (I) 'bring together, collect'; (II) 'apply, direct; confer, bestow, give, grant' (L&S) ← *con-* + *ferō* ← PIE \*bʰer- 'carry' (Wikt) | FITS: one confers a title or an office | — |
| `appoint` | 1 | FOLDED → `confer` | `confer` on an `appointed` seat | ME *apointen* ← OF *apointier* ← LL *appunctō* (*ad* + *punctum*) (Wikt); *punctum* is the neuter of *pūnctus*, ppp. of *pungō, -ere, pupugī, pūnctum* 'prick' ← PIE \*pewǵ- 'prick, punch' (Wikt la *punctum*, *pungō*); no L&S entry for *appunctō* | FITS: "appoint a governor" | — |
| `designate` | 1 | FOLDED → `confer` | `confer` of the heir title `off_heir` (IN-61, RS-27) | L *dēsignātus*, pp. of *dēsignō, -āre, -āvī, -ātum* 'mark out, trace out; designate' (L&S) ← *dē* + *signum*; PIE: Wikt lists \*sekʷ- and \*sek- (unresolved) | FITS: "designate an heir" | — |
| `elect` | 1 | FOLDED → `confer` | `confer` on an `elected` seat once a count of members' `commit`s is read (M-COUNT) | L *ēlēctus*, pp. of *ēligō, -ere, ēlēgī, ēlēctum* 'pick out, choose, elect' (L&S) ← *ē* + *legō* ← PIE \*leǵ- 'gather' (Wikt) | STRAINED: the voters elect; the chair only seats the winner (`succeed`'s defect, VCD:4341) | drop the name from the fill; "elect" names SC's count |
| `steward` (regent) | 1 | FOLDED → `confer` | a termed `hold` on a second seat over the domain (IN-48, Layer 1 route) | Germanic: ME *steward* ← OE *stīġweard* (*stīġ* 'hall, pen' + *weard* 'guard') (Wikt). No Latin | STRAINED: the verb "steward" means manage resources; the act is appointing a regent | `appoint` (to a regency seat) |
| `rotate` | 1 | FOLDED → `confer` | `confer` with `Tenure.term` (VT:182) | L *rotō, -āre, -āvī, -ātum* 'turn a thing round like a wheel; swing round, whirl about' (L&S, poet. and post-Aug.) ← *rota* 'wheel' ← PIE \*Hreth₂- 'run, roll' (Wikt) | FITS: "rotate officials" is current administrative English | — |
| `revoke` | 1 | SHIPPED | closes another's seat `hold` under `revocation_bases` (`Tenure.until`); `tenure.closed` | MF *révoquer* (Wikt) ← L *revocō, -āre, -āvī, -ātum* 'call back, recall' (L&S) ← *re-* + *vocō* 'call, summon' (L&S) ← PIE \*wekʷ- 'speak' (Wikt) | FITS: "revoke an appointment" | — |
| `dismiss` | 1 | FOLDED → `revoke` | as `revoke`; the person named rather than the appointment | ME *dismissen* ← L *dīmissus*, pp. of *dīmittō, -ere, dīmīsī, dīmissum* 'send apart; send away, let go, discharge, dismiss' (L&S), prefix respelled *dis-* in English (Wikt); *mittō* ← PItal \*meitō ← PIE \*meyth₂- 'exchange, remove', an extension of \*mey- 'change' (Wikt la) | FITS | — |
| `establish` | 1 | SHIPPED | founds an Office (`Office.exists`, `remit_acts`); `office.established` | ME *establissen* ← OF *establir* (Wikt) ← L *stabiliō, -īre, -īvī, -ītum* 'make firm, steadfast; fix, establish' (L&S) ← *stabilis* (*stō* + *-bilis*) ← PIE \*steh₂- (Wikt la) | FITS: "establish an office" | — |
| `amend` | 1 | FOLDED → `establish` | re-remits an existing Office; earns `remit.changed` (`EG:197-203`) | ME *amenden* ← OF *amender* ← L *ēmendō, -āre, -āvī, -ātum* 'free from faults, correct, improve, amend' (L&S) ← *ex* + *mendum* 'fault' ← PIE \*mend- (Wikt) | FITS: "amend a commission" | — |
| `succeed` | 1 | SHIPPED, REBUILD (IN-61) | the heir opens the vacant throne's `hold` through `inheritance` | OF *succeder* (Wikt) ← L *succēdō, -ere, -cessī, -cessum* (I) 'go below'; (B) 'follow, take the place of, relieve, succeed' (L&S) ← *sub* + *cēdō* ← PItal \*kezdō; PIE **disputed**, perhaps \*ḱyesdʰ- 'drive away; go away' (Wikt la) | as shipped STRAINED (the holder designates); as rebuilt FITS (the heir succeeds) | — (re-voice, not rename) |
| `release` (GV uses) | 1, 6 | SHIPPED (shared) | the holder closes his own edge (`Tenure.until`); `tenure.closed` | ME *relesen* ← OF *relaissier* / *relaschier* = OF *re-* + *laissier* / *laschier* (Wikt OF) ← L *laxō, -āre* 'loosen, relax' (← *laxus* 'loose, slack'); *laissier* perhaps influenced by OHG *lāzan* (Wikt OF) ← PIE \*(s)leg- (Wikt la *laxus*). L *relaxō* is a parallel Latin compound, not the ancestor | FITS for a `hold` (one releases a right or claim one holds); STRAINED for `commit`/`oblige` (L-08) | — for GV |
| `resign` | 1 | FOLDED → `release` | `release` of a seat `hold`; earns `seat.resigned` (M-RESIGN) | AN, MF *resigner* ← L *resignō, -āre, -āvī, -ātum* 'unseal, open; annul, cancel; (Hor.) give back, resign' (L&S) ← *re-* + *signō*; the specialisation to 'give up an office' is later (French, English) | FITS | — |
| `abdicate` | 1 | FOLDED → `release` | as `resign`, when the seat is the realm's top seat | borrowed 1532 (Wikt) ← L *abdicātus*, pp. of *abdicō, -āre, -āvī, -ātum* 'disown, refuse'; politically *abdicāre sē magistrātū* 'renounce an office, resign, abdicate' (L&S, Liv., Sall.) ← *ab* + *dicō* 'proclaim' (L&S), akin to *dīcō* (Wikt en; Wikt la *dicō* (1st conj.): 'possibly a back-formation from compounds in -dicō') ← PIE \*deyḱ- 'show, point out' via *dīcō* (Wikt la) | FITS: monarchs abdicate | — |
| `abandon` | 6 | FOLDED → `release` | `release` of one's `hold` on a Rung; the place stays, unheld | ME *abandounen* ← OF *abandoner* (*à* + *bandon* 'control') ← LL *bannum* ← Frankish \*ban ← PGmc \*bannaną ← PIE \*bʰeh₂- 'speak' (Wikt). Latin only as a medieval loan of a Frankish word | FITS | — |
| `issue` | 2 | SHIPPED | mints a dispensation Record to one executor (`Record.exists`); `dispensation.issued` | ME, OF *issue*, fem. pp. of *issir* ← L *exeō, exīre, exiī, exitum* 'go out or forth' (L&S) ← *ex* + *eō* ← PIE \*h₁ey- 'go' (Wikt). Intransitive root; the transitive 'send out officially' is the English development (V-13) | FITS: "issue a writ" | — |
| `warrant` | 2 | FOLDED → `issue` | a dispensation whose `terms` names a person or a Record; read by `seize`/`arrest` | Germanic via French: ME *waranten* ← AN *warantir*, OF *guarantir*, built on the noun *guarant* ← Frankish \*warand, pres. ptcp. of \*warjan (Wikt). No Latin | FITS as a content name ("issue a warrant") | — |
| `commission` | 2 | FOLDED → `issue` | a dispensation naming a charge. The kind is unbuilt (`RO` `record_kinds` note) | ME *commissioun* ← OF *commission* ← L *commissiō* ← *committō* + *-tiō* ← *com-* + *mittō*; PIE \*mey- (Wikt en template) | FITS | — |
| `order` | 2 | SHIPPED (as `dispatch`), REBUILD | a documentless order to a named person; `order.given`; needs M-ORDER | verb from the noun: ME *ordre* ← OF *ordre* (Wikt) ← L *ōrdō, ōrdinis* 'a regular row, line, series; order' (L&S); cf. *ōrdinō* 'arrange; rule; ordain, appoint to office' (Wikt la) ← PIE \*h₂er- 'fit', "probably" (Wikt) | FITS: one orders a person to act | rename `dispatch` → `order` |
| `dispatch` (retired name) | 2 | CULLED (name only) | — | Sp. *despachar* and/or It. *dispacciare*; further etymology uncertain; second element probably VL \*pactāre / \*pactiāre or *-pedicāre* ← *pedica* ← *pēs*; first written use 1517 (Tunstall) (Wikt en) | MISFIT: a dispatch is a written message, and the row writes nothing; also 'kill' (L-05) | `order` (the remit act keeps the word) |
| `comply` | 2 | SHIPPED | emits `compliance.given`; writes nothing; the performance is the executor's own act | It. *complire*, Cat. *complir*, Sp. *cumplir* (alt. OF *compli*) ← L *compleō, -ēre, -ēvī, -ētum* 'fill up, fill full' (L&S) ← *com-* + *pleō* ← PIE \*pleh₁- 'fill' (Wikt). The sense 'act in accordance' is a later shift `[UNVERIFIED: century]` | FITS | — |
| `evade` | 2 | NEW (split) | covert non-performance; `compliance.evaded`, deposited on detection; cuts a tax take at MATTER | MF *évader* ← L *ēvādō, -ere, ēvāsī, ēvāsum* 'go or come out' (L&S) ← *ē* + *vādō* ← PIE \*weh₂dʰ- (Wikt) | FITS: "evade a tax" | — |
| `defy` | 2 | NEW (split) | open refusal; `compliance.refused` to the issuing seat; withholds a tax take for the season | OF *desfier* ← VL \**disfīdāre* ← *dis-* + *fīdus*; *fīdō, -ere, fīsus sum* 'trust, rely upon' (L&S) ← PIE \*bʰeydʰ- (Wikt). Sense shifted in the 14th c. from 'be disloyal' to 'challenge' (Wikt) | FITS: "defy an order" | — |
| `evade / defy` (row) | 2 | CULLED (replaced by the split) | — | — | MISFIT as a row (VCD:4069) | `evade`, `defy` |
| `proclaim` | 3 | NEW | mints an `edict` Record (`kind: notice`) published to the residents of `at`; `edict.proclaimed` | ME *proclamen* ← OF *proclamer* ← L *prōclāmō, -āre, -āvī, -ātum* 'call or cry out' (L&S) ← *prō-* + *clāmō*; spelling after *claim* (Wikt); PIE of *prō-* \*per- (Wikt), of *clāmō* \*kelh₁- 'shout' (Wikt la) | FITS | — |
| `decree` | 3 | FOLDED → `proclaim` | a notice-kind edict; a decree with a reader is a row of its own | ME *decre* ← OF *decré* ← L *dēcrētum*, n. pp. of *dēcernō, -ere, dēcrēvī, dēcrētum* 'decide, judge, determine, decree' (L&S) ← *dē* + *cernō* ← PItal \*krinō ← PIE \*krey- 'sieve' (Wikt la) | FITS | — |
| `repeal` | 3 | FOLDED → `destroy_record` | the edict's holder ends it (`Record.exists`); waits on H-75 | ME *repelen* ← AN *repeler* ← OF *rapeler* 'call back', = *re-* + *apeler* (Wikt OF) ← L *appellō, -āre, -āvī, -ātum* 'address, call by name' (Wikt OF, Wikt la) ← *ad-* + *pellō* ← PIE \*pelh₂- (Wikt la). Wikt en's *repellō* is a contrary reading | FITS: "repeal a law" | — |
| `charter` | 3 | PARKED | an exemption edict; waits on a `purview_reaches` exemption | ME *chartre* ← OF *chartre* ← L *chartula* 'a little paper, a small writing' (L&S), dim. of *charta* 'leaf of papyrus, paper' (L&S) ← Gk *χάρτης*. No PIE traced (a Greek loan) | STRAINED: the verb also means 'lease or hire by charter' (Wikt) | none plainer. Keep, with the object (a town, a guild) fixing the sense |
| `tax` | 4 | NEW | mints an `edict` (`kind: tax`, `amount`); MATTER diverts yield to the seat's treasury each season (`Rung.stores` ×2); `tax.levied`, `tax.collected`, `tax.withheld` | ME *taxen* ← AN *taxer* ← L *taxō, -āre, -āvī, -ātum* 'touch sharply; censure, charge; rate, value, appraise' (L&S, from *tangō*) ← PIE \*teh₂g- 'touch' (Wikt) | FITS | — |
| `requisition` | 4 | SHIPPED | moves a rung's stock into the seat's treasury now (`Rung.stores` ×2); `requisition.taken` | ME, OF *requisicion* ← ML *requīsītiō* (Wikt) ← L *requīrō, -ere, requīsīvī, requīsītum* 'seek, search for; ask, demand; need' (L&S) ← *re-* + *quaerō*; PIE uncertain: *quaerō* per Nussbaum and De Vaan from PItal \*kʷaizō ← PIE \*kʷeh₂(y)- 'acquire' (Wikt la). L&S's first gloss is 'seek again' (critic L-01 calls *re-* intensive). The English sense rests on 'ask, demand', not on 'again' | FITS: "requisition grain" | — |
| `ration` | 4 | NEW | mints an `edict` (`kind: ration`); MATTER's draw per mouth at `at` is cut; `ration.set` | F *ration* (Wikt) ← L *ratiō, ratiōnis* 'a reckoning, account, calculation' (L&S) ← *reor*; PIE \*h₂er- (Wikt). The 'fixed allowance' sense is French, and the English verb is late, `[UNVERIFIED: century]` | FITS | — |
| `relieve` | 4 | FOLDED → `transfer` | a seat-paid `transfer` to a rung in shortfall; earns `relief.given` | late ME *releven* ← OF *relever* ← L *relevō, -āre, -āvī, -ātum* 'lift up, raise; lighten; relieve' (L&S) ← *re-* + *levō* ← *levis* 'light' ← PIE \*h₁lengʷʰ- (Wikt la) | FITS: "relieve the famine"; collides with "relieve a siege" (MB) | — |
| `assess` | 4 | PARKED | a cadastral base that `tax` would read | ME *assessen* ← OF *assesser* ← ML *assessāre*, freq. of *assessus*, pp. of *assideō, -ēre, -sēdī, -sessum* 'sit by; sit at one's side as assistant' (L&S) ← *ad* + *sedeō* ← PIE \*sed- 'sit' (Wikt) | FITS: "assess land for tax" | — |
| `arrest` | 5 | PLANNED (IN-12 step 5) | opens `detain` (prisoner → warrant seat), contested; `arrest.made` / `arrest.resisted` | ME *aresten* ← OF *arester* ← VL \**arrestō* ← *ad-* + *restō* (Wikt); *restō, -āre, restitī* 'stay behind, stand still; withstand' (L&S) ← *re-* + *stō* ← PIE \*steh₂- 'stand' (Wikt) | FITS | — |
| `pardon` | 5 | PLANNED (IN-12 step 5) | closes another's `detain`/`ban` under the determination basis (`GT:1112-1119`); `detention.ended` / `ban.ended` | ME *pardonen* ← OF *pardoner* ← LL *perdōnō, -āre, -āvī, -ātum* 'concede, grant, remit, pardon, forgive', attested 350–500 CE (Wikt la) ← *per-* + *dōnō*; ← *dōnō* ← *dōnum* ← PIE \*deh₃- 'give'; possibly calqued into PGmc \*fragebaną, or the reverse (Wikt la) | FITS | — |
| `seize` | 5 | SHIPPED | a warranted Record or an occupied settlement changes holder (`Tenure.until`/`since`); `record.seized` / `rung.seized` | ME *seisen* ← OF *seisir* ← ML *sacīre* (8th c.) ← Frankish \*sakjan ← PGmc \*sakjaną (Wikt). Germanic at root; Latin only as the medieval conduit | FITS | — |
| `annex` | 5 | FOLDED → `seize` | `seize`'s Rung half; re-parenting `contain` is a gap (M-ANNEX) | ME *annexen* ← OF *annexer* ← ML *annexāre*, freq. of *annectō, -ere, -nexuī, -nexum* 'tie or bind to, connect, annex' (L&S) ← *ad* + *nectō* (Wikt); no secure PIE root (*nectō* uncertain, possibly related to *nōdus*, Wikt la) | FITS | — |
| `found` | 6 | SHIPPED | mints a Rung under its works' `at` plus the founder's `hold`; `rung.founded` | ME *founden* ← OF *fonder* ← L *fundō, -āre, -āvī, -ātum* 'lay the bottom, keel, foundation; found' (L&S, 1st conj.) ← *fundus* 'bottom' ← PIE \*bʰudʰmḗn (Wikt la). Distinct from *fundō, -ere, fūdī, fūsum* 'pour, melt, cast' (Wikt) | FITS: "found a town" | — |
| `build` | 6 | SHIPPED, REBUILD (in-act plan) | mints a Site at condition 0, paying `works_cost`; `site.built` | Germanic: ME *bilden* ← OE *byldan* ← PWGmc \*buþlijan ← PGmc \*buþlą 'dwelling' ← PIE \*bʰuH- 'become, be' (Wikt). No Latin | FITS | — |
| `fortify` | 6 | FOLDED → `build` | `build` of a `garrison` Site | late ME *fortifien* ← OF *fortifier* ← LL *fortificō, -āre* 'make strong, strengthen' (L&S, post-classical) ← *fortis* + *-ficō*; PIE \*bʰerǵʰ- or \*dʰerǵʰ- (Wikt, disputed) | FITS | — |
| `improve` | 6 | FOLDED → `build` (conditional) | a works raising an existing Site's ceiling (M-WORKS b) | AN *emprouwer* ← OF *en-* + *prou* 'profit' ← VL *prode* (Wikt). No classical Latin verb | FITS | — |
| `raze` | 6 | PLANNED (IN-12 step 11) | ends a Rung or Site; licensed by occupation; must re-house persons | ME *rasen* ← AN, OF *raser* ← VL \**rāsō* ← L *rāsus*, pp. of *rādō, -ere, rāsī, rāsum* 'scrape, scratch, shave' (L&S) ← PItal \*razdō, perhaps related to *rōdō*; no PIE root given (Wikt la) | FITS: "raze a town" | — |
| `patrol` | 6 | PARKED | guards present at a rung lower disorder (no quantity exists) | F *patrouiller* ← OF *patouiller* ← *patte* 'paw' ← Frankish \*patta (Wikt). Not Latin | FITS | — |
| `depose` | 1 | PARKED (D-V1) | removal of a living top-seat holder by a basis reading two signals (v2-p8 V090) | ME (c. 1300) ← OF *deposer* (*de-* + *poser* ← LL *pausō, -āre* 'halt, cease, pause', L&S); conflated with L *dēpōnō, -ere, -posuī, -positum* 'lay down; give up, resign' (*dēpōnere imperium*, L&S) (Wikt) | FITS | — |
| `abolish` | 1 | PARKED | closes an Office | late ME *abolisshen* ← MF *abolir* ← L *aboleō, -ēre, -ēvī, -itum* 'destroy, efface, abolish' (L&S; orig. 'check the growth of'), with inchoative *abolēscō, -ere, -ēvī* 'decay little by little, vanish' (L&S) ← *ab-* + ?; PIE **disputed**: \*h₂el- 'grow' (Wikt en) or \*h₃elh₁- 'destroy' (Wikt la) | FITS: "abolish an office" | — |
| `detain` | 5 | not a verb (the Tenure kind) | the edge `arrest`/`determine` open; read by `restrained()` | OF *detenir* (Wikt) ← L *dētineō, -ēre, -tinuī, -tentum* 'hold off, keep back, detain' (L&S) ← *dē* + *teneō* ← PIE \*ten- (Wikt) | FITS as the state's name | — |
| `ban` | 5 | not a verb (the Tenure kind) | the edge `determine` opens; read by `restrained()` | Germanic: ME *bannen* ← OE *bannan* / ON *banna* ← PGmc \*bannaną ← PIE \*bʰeh₂- (Wikt). No Latin | FITS as the state's name; collides with EC's "ban term" on a good (v2-p8 §V.2.2) | the EC term → `embargo` |

---

## 3.5 Deduplication and culls

| near-synonyms / one act | what I did | fold-test result and floor check |
|---|---|---|
| `found` / `build` / `establish` | three rows kept, with a stated discriminator: Rung plus `hold` / Site / Office | `found` → `build` fails "same mechanic": `found` opens a Tenure and `build` cannot (VT:371, :406). No floor act lost |
| `tax` / `requisition` | both kept: standing on yield against one-off on stock | a one-shot tax would pass into `requisition` and is not a separate act. Floor kept: taxing |
| `tax` / `issue`+`comply`+`transfer` (v2 V145) | rejected as a composition across three actors | rule 5. The payer's answer becomes his own `evade`/`defy`; the take is MATTER's reading of the edict |
| `tax` / `ration` / `proclaim` | three rows on one `edict` carrier | MATTER's yield step, its draw step, and publication only are three mechanics; the value term differs in sign (§V.2.1) |
| `revoke` / `dismiss` | one row; `dismiss` named | pass (no difference) |
| `revoke` / `depose` | `depose` parked | fails "same basis": the top seat is "stripped by nobody" (`RO` `revocation_bases`) |
| `release` / `resign` / `abdicate` / `abandon` | one host; three names | pass: the holder's own `hold`, differing in object |
| `release` / `pardon` / `revoke` | three rows | different actor (own / bench / rung-above), edge kind (any / restraint / seat) and gate basis. Floor kept: freeing a prisoner |
| `arrest` / `seize` / `detain` | `arrest` and `seize` rows; `detain` is the edge, not a verb | `arrest` → `seize` fails object, write, contest and eligibility (Suite 5) |
| `comply` / `evade` / `defy` | three rows; the slash row retired | value-term sign (+0.9 against −0.6, v2-p4:161); covert against open delivery |
| `order` / `issue` / `dispatch` | `order` (renamed) and `issue` kept | an order mints no Record (VT:160). The name `dispatch` is retired from the verb and kept on the remit |
| `relieve` / `transfer` / `give` | `relieve` named on `transfer` | pass. `give` moves Records, not stores (VT:419-423) |
| `annex` / `seize` | named on `seize` | pass |
| `survey` / `assess` | `survey` stays FI's faction-sheet inquiry; `assess` parked | different objects (a faction against a place's yield); answers critic L-09's neighbour from GV's side |
| `steward` / `appoint` | `steward` names the office; the act is `appoint` | the verb "steward" is STRAINED |
| `elect` / `confer` | the fill stays `confer`; "elect" goes to SC's count | the voters' act and the chair's act are two actors |

**Culls.**
- `evade / defy` as a row: replaced by `evade` and `defy`. Nothing in the floor dies.
- `dispatch` as a name: the row stays as `order`. Falsifier for the cull: a reader that needs the documentless order to read as "sending".
- `detain` and `ban` as verbs: they are outcomes, not acts. The act that opens them is `arrest` or `determine`. Falsifier: a GV act that opens a `detain` edge outside those two.

**Critics' findings on GV verbs.**

| finding | decision | reason |
|---|---|---|
| L-01 (root sense as design) | applied | no merge or gap here rests on a root. Every fold cites the row's reads and writes and the ordinary sense |
| L-03 (`levy`) | applied | the store act is `requisition` (VT:646). The troop act goes to MB/FA (§3.8). Stale `levy` lines in `requirements.yaml` and `hole_register.yaml` are TS-L's re-key (TS:728-736) |
| L-05 (`dispatch`) | applied | renamed `order`. The ruling kept the row, not the word (`dispatch` was "rejected [for] deleting", WP2 J-8, `valoria_master_workplan_v9_part2.md:201`). Renames are precedent: `levy`→`requisition`, `kill / wound`→`fight` (VT:478-485) |
| L-07 (`establish`/`amend`; `found`/`establish`/`build`) | applied | `amend` named; discriminator stated |
| L-08 (`release`) | answered for GV | every GV use closes a `hold`, which is the holder's right and so the legal sense of "release". `commit`/`oblige` uses are flagged to NP/SC |
| L-14 (`comply` gloss) | applied | the row writes nothing (VT:161) |
| L-18 (`remit:issue` gates other acts) | answered | `tax`, `ration` and `proclaim` also take `remit:issue`. That is the declared substitution (VT `requisition` `eligibility_substitution_note`), and it widens H-52's question. Flagged, not decided |
| V-15 (`tax` leans on a retired row) | applied | `tax` no longer depends on `evade / defy`; the slash row is split, not retired into `comply` |
| V-16 (ransom ≠ pardon) | applied | `pardon` is grace; a paid release of a war captive is flagged to FA |
| V-19 (`due` vs `debt`) | applied | the content is named `tax` and the carrier `edict`; no `due` writ |
| V-03 ("each keeps a name") | answered | `abdicate` and `resign` are named folds with an earned kind (M-RESIGN), consistent with v2-p8 §V.2.4 |
| V-13 (`issue` "send out"; `confer` "bear together") | applied | chains above give *exeō* 'go out' and *cōnferō*'s 'bestow' sense |

---

## 3.6 Gap coverage

Columns: closed by · PARKED (trigger) · OUT OF SCOPE (why) · STALE (cite) · DISPUTED (why). Exactly one is filled per row.

| gap | closed by | PARKED | OUT OF SCOPE | STALE | DISPUTED |
|---|---|---|---|---|---|
| GV-G01 | — | — | — | the store row is already `requisition` (VT:646); L-03's stale lines are TS-L's re-key | — |
| GV-G02 | — | — | troop raising is MB/FA's `levy` (TS §3.1); flagged §3.8 | — | — |
| GV-G03 | `evade`, `defy` (and `tax`), once M-EDICT and M-TAX exist | — | — | — | — |
| GV-G04 | the split into `evade` and `defy` | — | — | — | — |
| GV-G05 | `evade`, `defy`, typed on `comply`'s cell (VT:303, `60073e75`), once a Candidate forms on a held writ or edict | — | — | — | — |
| GV-G06 | `order` (rename) | — | — | — | — |
| GV-G07 | `succeed` re-voiced as the heir's claim (IN-61) | — | — | — | — |
| GV-G08 | `succeed`, once M-INHERIT (IN-61's `inheritance` basis) exists | — | — | — | — |
| GV-G09 | — | — | SC: the computed `open_case` naming its arrangement (SC-G01, SC-04 `succession` row) | — | — |
| GV-G10 | `arrest` (planned, IN-12 step 5) | — | — | — | — |
| GV-G11 | `pardon` (planned, IN-12 step 5) | — | — | — | — |
| GV-G12 | — | — | — | readers built at SC-03a: `loop/effects_migration.py:52, :184`; `loop/sides.py:123`; `loop/predicates.py:397`; `EG:105`. `church_standing` not checked | — |
| GV-G13 | `arrest` (the person half); `seize` kept for Record and town | — | — | — | — |
| GV-G14 | — | — | the taker's terms are `covenant` terms (SC/FA) and `surrender` is MB's preset of `give` (v2-p8 V086) | — | — |
| GV-G15 | `raze` (planned, IN-12 step 11), once its re-housing rule exists | — | — | — | — |
| GV-G16 | `build`/`found`, rebuilt to carry their plan, once M-WORKS (a) exists | — | — | — | — |
| GV-G17 | `establish` (an office under an office) and `confer`, once M-OFFICE-REF exists; dissolve → `abolish` (parked) | — | — | — | — |
| GV-G18 | `confer` (`steward` fold), once M-DELEGATE exists | — | — | — | — |
| GV-G19 | `revoke`, once M-OFFICE-REF exists and H-91 is decided | — | — | — | — |
| GV-G20 | `revoke`, once M-COST (IN-31) exists | — | — | — | — |
| GV-G21 | — | `depose`: Jordan rules ARC-40's replaced arm (D-V1) | — | — | — |
| GV-G22 | `resign` / `abdicate` on `release`, once M-RESIGN exists | — | — | — | — |
| GV-G23 | `proclaim`, once M-EDICT exists | — | — | — | — |
| GV-G24 | the edict suite (`proclaim`, `tax`, `ration`) once M-EDICT exists; embargo and interdict flagged to EC and SC | — | — | — | — |
| GV-G25 | — | `charter`: M-EDICT plus a `purview_reaches` exemption | — | — | — |
| GV-G26 | the per-verb map: Develop and Fortify → `build`; Hold Court → SC `determine`; Sponsor → `relieve`/`transfer`; Levy → `tax`/`requisition` (troops MB); Negotiate Quota → `tax` fixed `amount`; Survey → `assess` (parked); Keep Order → `patrol` (parked) | — | — | — | — |
| GV-G27 | `tax`, once M-TAX exists | — | — | — | — |
| GV-G28 | `relieve` (on `transfer`) and `ration`; the granary-shape choice is EC's store model | — | — | — | — |
| GV-G29 | `ration`, once M-DRAW exists | — | — | — | — |
| GV-G30 | — | — | a witness-channel limit (H-160 limit 3), ruled "a balance number, not a blocker" 2026-10-12 (register row); not a verb | — | — |
| GV-G31 | — | `patrol`: a disorder quantity plus a guard reader | — | — | — |
| GV-G32 | — | `assess`: `tax` reads an assessed base | — | — | — |
| GV-G33 | — | `assess`: same trigger | — | — | — |
| GV-G34 | the split (`evade`, `defy`) and the rename (`order`); `comply` answers writs only, since an order mints none (VT:160) | — | — | — | — |
| GV-G35 | `tax` (MATTER performs the take; no `comply`→`transfer` leg). Other writs: the keys channel (v2-p8 §V.2.2) | — | — | — | — |
| GV-G36 | — | — | a knowledge carrier (`held_by` claim producer, H-195), FI/NP; not a verb | — | — |
| GV-G37 | — | — | — | vassalage is read by `purview_reaches`' `oblige` clause since IN-40 (`3f320093`; `GT:388-402`). Office-under-Office stays with G17 | — |
| GV-G38 | `confer` with `Tenure.term` (term limit, rotation: VT:182); veto flagged to SC | — | — | — | — |
| GV-G39 | — | — | `determine`'s disposal kind as state (SC-G24) | — | — |
| GV-G40 | — | — | judicial death is PC `fight` by the enforcement seat (VCD R-1); `execute` is not a verb | — | — |
| GV-G41 | — | `abolish`: a reader of holds on a closed Office (`rescind` = `repeal` on `destroy_record`) | — | — | — |
| GV-G42 | — | — | FA: Layer 1 gives a Faction no verbs; the Govern pass is seated persons' verbs (VCD:2372) | — | — |
| GV-G43 | — | — | FI's `research` on a frozen account (v2-p8 V141); rotation is G38's | — | — |
| GV-G44 | `confer` on an `elected` seat, once M-COUNT exists | — | — | — | — |
| GV-G45 | `confer`, `revoke`, `establish`, once M-OFFICE-REF exists | — | — | — | — |

**Totals** (counted by script over the 45 rows; each row has exactly one disposition):

| disposition | rows |
|---|---|
| closed | 27, of which 16 are conditional on a mechanic in §3.7 |
| parked | 6 |
| out of scope | 9 |
| stale | 3 |
| disputed | 0 |

---

## 3.7 Mechanics GV needs (named gaps)

| id | mechanic | what it must write or read | verbs that wait on it |
|---|---|---|---|
| M-EDICT | Record kind `edict`, plus a publication deposit to the residents of `at`'s subtree | `RO` `record_kinds` gains `edict: [kind, at, amount, until]` (exact keys, `Record.__post_init__`). WITNESS gains a deposit route to residents that survives SC-01 step 13. `comply`/`evade`/`defy` accept an edict as `subject` | `proclaim`, `tax`, `ration`, `charter` (parked), and `evade`/`defy` on edicts |
| M-TAX | MATTER's tax reader | at the yield step, for each live `tax` edict whose issuing seat's purview still reaches `at`: move `amount` × yield (or a fixed sum), capped by stores, into the seat's treasury rung. Writes `Rung.stores` ×2; emits `tax.collected`. Zero for a rung whose seat-holder defied this season (`tax.withheld`); minus the hearth share of an evader. f(legitimacy) = 1 until IN-23. One owner: MATTER (`loop/matter.py`) | `tax`, `evade`, `defy` |
| M-DRAW | MATTER's draw policy | the draw per mouth at `at` cut by a live `ration` edict's `amount`. Waits on Jordan's draw-policy ruling ("Already Jordan's", v2-p8 §V.5.1), and on H-211 cause 1 for recovery to be visible | `ration` |
| M-WORKS | (a) a computed works source; (b) a works raising an existing Site's ceiling | (a) `build`/`found` accept `{plan, at}` and mint the works inside the act when none is held (H-165 limit 2). (b) a works naming an existing Site of its kind writes the ceiling, not `Site.exists` | `build`, `found`, `fortify`, `improve` |
| M-RAZE | `raze`'s re-housing rule | a razed Rung's contained persons re-homed (VCD:1812 GAP); the closer order (H-166 limit 3) | `raze` |
| M-OFFICE-REF | an office referent in computed play | a question whose referent is an Office, from a held Record's `terms` or a `tenure.opened` deposit (HR H-203) | `confer`, `revoke`, `establish`, `succeed` |
| M-COUNT | a count Query over members' `commit`s | the `elected` basis reads it; SC's `vote` = `commit` (v2-p8 V127) | `confer` (`elect`) |
| M-DELEGATE | an early-dismissal basis for a same-rung regency seat | a `revocation_bases` member (Layer 1 data shape, WP5:179) | `confer` (`steward`), `revoke` |
| M-COST | the revocation cost reader | IN-31 / H-100 (`proposals/2026-10-14-in31-revocation-cost-provenance.md`, PROPOSED) | `revoke` |
| M-INHERIT | the `inheritance` basis and the `successions` registry | IN-61's EDITS (WP5:214) | `succeed` |
| M-RESIGN | an earned kind for a seat resignation | `seat.resigned` beside `tenure.closed`, with one `deed:` cell (v2-p8 §V.2.4); K-FA-3's question source | `resign`, `abdicate` |
| M-ORDER | a delivery and a question source for an order | `order.given` deposited to the person ordered; his Candidate formed from it | `order` |
| M-ANNEX | re-parenting a seized town's `contain` under the taker's ladder | a `contain` write under the `seizure` basis (not written today) | `annex` |
| M-LABOUR (EC) | a labour input to yield | MATTER's yield reads workers assigned to a Site | EC's `assign`; GV's floor act "assign workers" |

## 3.8 Cross-subsystem flags

| other lane | verb or fold | the collision or dependency |
|---|---|---|
| MB / FA | `levy` (troops) | TS §3.1 gives the troop act `remit:dispatch`, reading the settlement's `recruits` store. GV hands it over. The seat that raises is GV's; the pool is a settlement store. Do not let it share `tax`'s `edict` carrier: a levy is one-off, like `requisition` |
| MB | garrison | a `transfer` of a troop stock to a town (TS §3.2) passes the fold test into EC's `transfer`. MB should name it |
| MB | `relieve` | the word collides with "relieve a siege". Tell MB before naming the siege act |
| MB | `annex`, `raze` | both are licensed by occupation (`_seize_rung`; IN-12 step 11) |
| EC | `relieve` on `transfer` | GV names it; EC owns the row and the `relief.given` cell |
| EC | `work`, `assign` | improvement by labour is `work` (VT:1292); worker assignment needs M-LABOUR |
| EC | embargo / ban on a good (v2-p8 §V.2.2 "a ban term on a held Record") | should be an `edict` kind on M-EDICT, not a second standing-rule carrier (shape divergence). Name it `embargo`, not "ban", which is the restraint Tenure |
| SC | `determine` | opens `detain`/`ban`; "banish" is its disposal name. `pardon` closes on the same gate basis (`GT:1112-1119`). `interrogate` (IN-12 step 5) is SC's |
| SC | `vote` / count | M-COUNT is the reader `elect` waits on |
| SC | veto (GV-G38), the `succession` arrangement (GV-G09) | SC-04 |
| SC | `deny` on `release` | the same host GV uses for `resign`. One `seat.resigned` kind must not swallow a denial |
| FA | `order` (renamed `dispatch`) | FA-01 pins five heads on the row (`tests/test_fa01_head_seats.py:56-59`). The rename is an atomic key rename with a declared hash move (VT:478-485's precedent) |
| FA | `depose` (D-V1), the abdication question source (K-FA-3), ransom | ransom is not `pardon` (V-16): a paid release of a war captive needs its own name in FA |
| FI | `survey`, `audit`, `conceal` | `survey` stays FI's; `audit` = `research`; `evade`'s detection is `conceal`'s reader |
| NP / IN | `release` for `commit`/`oblige` | L-08: `renounce` is the plain word there; GV's `hold` uses fit |
| IN | `remit:issue` | widened to `tax`, `ration`, `proclaim`. This is H-52's open eligibility question (`RO` `remit_acts` note), not decided here |

## 3.9 For Jordan

Before listing anything, I tried the five tests of CLAUDE.md §0 on every open item.
- Answered by architecture: the `tax` carrier and its MATTER reader, and the `evade`/`defy` split.
- Answered by precedent: the `dispatch` → `order` rename.
- Answered by IN-61: `succeed`.
- Answered by the IN-48 Layer 1 route: the steward.

Two items survive.

1. **D-V1, ARC-40's *replaced* arm** (already Jordan's). Can a living top-seat holder be removed against his will?
   - (a) No: `depose` is cut, and ARC-40 narrows to "act or abdicate".
   - (b) Yes: a removal basis on `revoke` reads two signals.
   - v2-p8 §V.5.1 D-V1 quotes FA research: "a removable king and an unremovable one are materially different games". Jordan's 2026-10-12 ruling covers revocation by the rung above. GV parks `depose` on it.
2. **The draw policy** (already Jordan's and "now load-bearing", v2-p8 §V.5.1). Who eats, in what order and how much, under scarcity? Today `subsistence_draw` walks persons in sorted id order (TS:135, citing `world_q.py:858`). A ration has to cut something that this policy defines, so `ration` cannot be built before it.

Considered and not escalated:
- IN-61's [ASSUMPTION] that only the heir's claim may fill an `inheritance` seat. RS-27 answers it (WP5:213: "the heir still has to claim their throne").
- ED-IN-0292 (2) (about `vacancies`) stays where IN-61 already routes it.

---

**Method and limits.**
- Fan-out: I spawned no agents. One reader could hold the subject (about 20 verb rows and 45 gaps), and splitting it would have bought redundancy, not independence (§10). The cost is that no independent critic has checked these verdicts. The reconciliation (Part III §III.5)'s reconciliation is the first check.
- Etymology: chains were checked with the tool for 49 English words (Wiktionary), 38 Lewis & Short entries, and 3 Latin Wiktionary entries. Links the tool did not reach are tagged `[UNVERIFIED]`.
- Reading limits:
  - I read the verb table's rows through their key fields and selected notes, not every note in full.
  - `hole_register.yaml` rows: heads only.
  - I did not open `church_standing`, `loop/effects_founding.py`, or the IN-31 design document's body.



