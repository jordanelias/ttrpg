# Subsystem completion proposals — index, rulings between files, order and asks (T00 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item, ruling and ask here is held back for Jordan's adoption, item by item, as edits to the v9 parts each file names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2). On adoption an item becomes a v9 position and its file is deleted with a `FORK:` row. **Home of v10 positions** since the v10 adoption (`ED-IN-0299`): this file holds the full spec of the v10 positions whose plan row names it (rows: `workplans/valoria_master_workplan_v10_part3.md` §1; handles: `workplans/valoria_master_workplan_v10_part12.md` §1; where `workplans/valoria_master_workplan_v10_part13.md` amends a home, the amendment governs), and is deleted with a `FORK:` row when its last position lands (v10 head §9 step 6).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. What it changes in `engine/season/`: nothing, until adopted. IDs allocated: none (handles `CP-T##-nn` are provisional).
## Written against: HEAD `2decf4a`. Inputs: `research/game_precedent_suite/` (866 compared rows; dispositions `D_T01`..`D_T10`), `proposals/2026-10-22-system-description/`, `proposals/2026-10-21-v9-remediation/`, `proposals/2026-10-16-verbs/`.

## 0. What this is, and how far to trust it

Jordan asked for design proposals that complete each gameplay subsystem, from the precedent work. The system description (T01..T10) found most subsystems thin where they meet the engine; each file below takes one subsystem, closes (or declines, with a five-step answer) every LACKS row and every risk-bearing DIFFERS row the dispositions hold for it, and proposes items that compose the suite's primitives (P01..P42) on the engine's own owners.

**Method, stated so the reader can weigh it.** Ten Opus authors, one per tutorial, each working alone from the brief; then **one** independent critic pass (four read-only critics, grouped by shared joins); then **one** fix pass in which each author applied its own critic's findings under a shared ruling sheet (§2). The fixes were not audited a second time (`CLAUDE.md` §0: review runs one round). Consequences the reader should carry:

- Each file's line-number citations were opened by its author and by a critic on a sample, not exhaustively. A cite is a pointer to check, not a proof.
- Several measurements are `[MEASURED-HEAD]` or `[computed]` from probe scripts that are **not in the repository**; they cannot be re-run from the tree.
- The four critics found real defects in every file (BLOCKS: 7, 4, 4, 4 and SHOULD: 10, 15, 16, 17, for the groups T01/T02/T05, T03/T04/T10, T06/T07/T08, T09). The fix pass applied nearly all of them and declined a few with evidence, but a file may still hold defects the critics did not reach.
- `tools/validate_ed_citations.py` run per file reports `OPEN_AS_BASIS` for `ED-IN-0202` (file 01, `status=open`) and `ED-WR-0011` (file 10, `status=ruled`, which the validator does not accept as resolved). The repository-wide default scan (what CI runs) does not reach `proposals/`; the two are noted here, not hidden.
- This index and the rulings in §2 are the orchestrator's calls under the five-step ladder, made to settle collisions between files. Jordan may overturn any of them.

## 1. The ten files

| # | subsystem | file | items live / total | rows addressed | asks |
|---|---|---|---|---|---|
| 01 | resolution and dice | `…-01-resolution-and-dice.md` | 6 / 6 (a seventh cut as a false N-line) | 28 of 38 | AQ-X1 |
| 02 | season, persons, chooser | `…-02-season-persons-choosing.md` | 8 / 8 | 39 | AQ-T02-1 |
| 03 | personal combat | `…-03-personal-combat.md` | 9 / 12 (`06` and `10` parked, `11` cut into IN-59) | 30 | none (carries JQ-2, ED-IN-0296, AQ-X1, T04 Ask B) |
| 04 | mass battle | `…-04-mass-battle.md` | 9 / 10 (`09` cut) | 30 | Asks A, B, C |
| 05 | social contest | `…-05-social-contest.md` | 5 / 5 | 24 | none |
| 06 | fieldwork and information | `…-06-fieldwork-and-information.md` | 8 / 9 (`08` parked on JA-1) | 29 | JA-1 |
| 07 | threadwork | `…-07-threadwork.md` | 11 / 11 | 24 | A1 (what a person becomes on crossing) |
| 08 | settlements, governance, economy | `…-08-settlements-governance-economy.md` and `_part2.md` | 9 / 10 (`09` withdrawn for T02) | 88 | none (knobs held at JQ-6) |
| 09 | factions, war, diplomacy | `…-09-factions-war-diplomacy.md` | 9 / 9 | 90 | A1 (who may declare war; verbs-15 Q3) |
| 10 | world, travel, survival, NPC life | `…-10-world-travel-survival-npc-life.md` | 9 / 9 | 89 | none |

83 live items of 89 headings. Row counts are each author's own re-tally after the fix pass; a row can sit in more than one gap, and "closed" means closed by an item, a remediation item or a scheduled v9 position, not "done".

What each file adds, by its item titles (the files hold the mechanisms, falsifiers, controls and hash-mover lines):

- **01** one faculty owner for the social roll's pool; a practice arm; one exact-odds function with two input modes; the fraction of a margin; `effort`; a ceiling solved per pool.
- **02** a death names the seats it empties; a built seat keeps its authored id; an ambition can be met or breached; the superior hears of it; causes a person has heard of are ambitions on offer; the seated person's line continues or ends; the seated person sees every question and the true odds of a contested act.
- **03** both parties of a fight take their band (the repair, CP-T03-00); cohorts are never a party; the Event says how the fight ended; kit and training (only under JQ-2 (a)); combat odds as an input to 01; a lasting mark (`body_ceiling`); `tend` forms on the wounded; `capture`.
- **04** a side is its persons; `marshal`; retreat in good order; the field fought a round after it is declared (Ask C); graded walls; `besiege`; `surrender`; `field_estimate` for the player's display; raise and keep a force (Ask A).
- **05** the verdict hears the bench; the bench remembers the hearing and the accused may answer; a failed telling is realised; formation for the proceedings verbs; questioning is part of the hearing.
- **06** a deed that writes a place or an alias leaves a trail; `surveil` finds covert deeds at its place; a Partial closes the deed, not the hand; a failed inquiry teaches its actor his reads; the person questioned answers by his own act; the `inquiry` key; a cover can borrow another's name; the room files a covered deed under the hand.
- **07** the practitioner on the Person; the Leap stage and one working host; `weave` and `lock` on Sites; `mend`; equilibrium decided by place; recovery as a projection; permanent set; the crossing as a witnessed breach; every thread row celled; what `thread_read` finds; `ward`.
- **08** hands make the yield; places endowed by ground; spoilage; `craft`; a price read off the place and trade between places; the settlement's mood (`unrest`); a standing levy by the `tax` edict, collected by act; the upkeep question; holding costs past a limit.
- **09** allegiance follows opinion; `declare`; alliance and peace as acts on the war Proposition; unheld land taken by plurality occupation (unfought towns only); land rewards the sworn; the Valorsmark seat refilled (data only); `recruit` and the seat's obligees in its army; `dispatch` sends; `conspire`.
- **10** the journey priced by its route; the Calamity costs the traveller; the year turns; recovery costs time and care; bodies clock wounds before they kill; kin; an estate passes by its heir's claim; `marry`; deeds done to me and mine.

## 2. Rulings between the files

The ten authors worked alone, so their files collided on shared quantities. These rulings settled the collisions before the fix pass; each file now follows them. The ruling sheet itself was a session scratch file and is not in the repository, so the rulings are recorded here.

| # | collision | ruling | owner |
|---|---|---|---|
| R1 | three odds functions (01, 02, 05) and two methods (03, 04) | **one** odds function. The player's Act-interface display shows the **true** odds (AX-7: "no state is hidden from the player", `architecture/meta/01_AXIOMS.md:299-304`); an NPC's choosing uses **believed** inputs only (AX-2). No file adds a chooser score term (the shape is ruled, `ARCHITECTURE_V2.md:508-528`). Whether expected success enters the NPC score at all is **AQ-X1**, asked once | 01 |
| R2 | the H-213 obstacle ceiling changed in 01, treated as fixed in 05, asked about in 06 | one owner, CP-T01-06. The author found the first-drafted cap (`2·pool`) produces 302 pool/obstacle cells where more dice do worse, so the cap is the highest obstacle that keeps pool 1's shipped chance; pools 0 and 0.5 keep today's ceiling. 06's ask is dropped; 05 states controls under both arms; 09 runs falsifiers uncapped | 01 |
| R3 | one person-capacity quantity, three mechanisms (01 `faculty(p, verb)`, 06 `inquiry`, 07 `spirit`/`history`) | `faculty(p, verb)` is the one function; explicit `verb_capability` rows, not a code rule; 06's key and 07's addends register through it; 07's stored Spirit is gated on JQ-2 | 01 |
| R4 | the death write and seat ids claimed by 02, 08 and 10 | 02 owns the Office-only `tenure.closed` broadcast and the seat-id preservation (H-230 limits 1 and 2); 08 withdrew its copy; 10's estate route is separate and non-broadcast (`w._estates`); the `off_npc_084` row is IN-61's content decision | 02 |
| R5 | two recovery caps for one body (03, 10) | `body_ceiling` is 03's; 10's rising arm and `tend` heal toward it | 03, 10 |
| R6 | R-M1 (both fighters take their band) had no carrier | made item CP-T03-00, a declared hash mover that roughly doubles combat deaths in a closed cast | 03 |
| R7 | the winner write after a field | ED-IN-0279 is resolved for the loser only (casualties, morale, a grudge token); T04's option (b) overwrites no ruling; **Ask B** is the single question; 03 cites it | 04 |
| R8 | Layer 1 touches bundled into agent items (04 cross-round read; 07 `mend` closing another's edge; 08 MATTER levy) | 04's becomes **Ask C**; 07 reshaped so `mend` never closes another's Tenure (a `locked` Site field); 08 collects the levy by act (`levy_due` question and the existing `requisition`) | 04, 07, 08 |
| R9 | joining a faction (09) vs the causes-heard-of stamper (02) | one route, 02's stamper; 09's opinion gate filters its creed output | 02, 09 |
| R10 | obstacle terms and ids | 09's terms are a demand on `roll.py::obstacle`, which 05 owns; the births ruling is cited by id as ED-WR-0011, described as provisional ("for now") | 05, 10 |
| R11 | who owns `dispatch` (09 CP-T09-08, 10 `:82`, 08) | `dispatch` is an FA host row (verbs-15 S5), so 09 owns the rebuild; 10's line is corrected to say so; 08 no longer mentions it | 09 |
| R12 | who counts effort slots (01 vs 02) | 01 (CP-T01-05 names `deliberate.py` and `carriers.py`); 02 does not carry it | 01 |

## 3. Order of landing

Authors declared their dependencies; the orders below are those declarations merged, not independently derived. Adoption puts each item into a v9 batch; this index does not.

1. **Shared owners first** (everything else reads them): 01 CP-T01-01 (`faculty`), -03 (the odds function), -06 (the ceiling, after -04's fraction rule); 02 CP-T02-01 and -02 (the death write and seat ids, which unblock IN-61 and are read by 08, 09, 10); 03 CP-T03-00 (the repair, before REM-31's goldens are re-pinned).
2. **Persons and reach**: 02 CP-T02-03..05 (ambitions, the superior hearing, causes heard of) before 09's joining filter; 07 CP-T07-01 (the practitioner on the Person) with J-T1.
3. **Per-subsystem builds** in lane order, each after the remediation items it names (REM-21..25 formation classes, REM-2B, REM-31, IN-59..61, IN-35).
4. **Ask-gated items last**: 03 CP-T03-03/-04 (JQ-2 (a)), 04 CP-T04-04 (Ask C) and -10 (Ask A), 06 CP-T06-08 (JA-1), 07's crossing slot (A1), 09's declarer (A1).

Dependencies on **stopped or unscheduled** work that the files say they cannot get around: IN-61 (succession; STOPPED), REM-2B (restores `evade`/`defy`), IN-06/IN-35 (the oracle's cost and the Calamity band), H-209 (a killing starts no war until a dead victim's claim is asked about), ED-IN-0296 (stance polarity; gates the grudge and the join).

## 4. Asks that survived the five steps

Eight, none new to the remediation's JQ-1..JQ-6 (those are referenced, not re-asked). Each file holds the options, consequence and ladder; this table only lists them.

| ask | file | question |
|---|---|---|
| **AQ-X1** | 01 | does expected success enter the NPC chooser's score at all? (materially different games; consolidates what 01, 03 and 04 each wanted) |
| **AQ-T02-1** | 02 | which ties carry a seated player's line past his death: heir title, then oath, then followers? (the author recommends title then oath) |
| **Ask A** | 04 | what is a raised troop? (the troop-stock design's J-1, carried; no plan schedules it) |
| **Ask B** | 04 | what may a fought field write beyond casualties, morale and a grudge on the loser? (J-5, J-C-4, plus captives) |
| **Ask C** | 04 | may ENCOUNTER fight a field declared in an earlier round? (a Layer 1 amendment: `04_CODE_ARCHITECTURE.md:177`, `:541-545`) |
| **JA-1** | 06 | may a holder burn what he holds? (H-156, `destroy_record`) |
| **A1** | 07 | what does a person become when he crosses the threadwork latch? (the slot ships empty) |
| **A1** | 09 | who may declare war: any `dispatch` seat, or the creed subject's faction head? (verbs-15 Q3) |

Carried, not re-asked: JQ-1, JQ-2, JQ-6, J-13's remainder, J-C-6 (the lie), ED-IN-0296, H-156.

## 5. Hash movers and Layer 1 touches, in one place

- **Schema movers** (a new `Person` or Site field moves `content_hash` whatever the arm, H-208): `body_ceiling` (03); the `locked` Site field and the resting-band field carried on `Person` (07); the place index (06, captured in `World._on_logged`; whether `content_hash` covers it is unverified); the estate record `w._estates` (10); `travel_leg` becoming `(dest, points, path)` (10; its off arm writes bare ids).
- **Declared behaviour movers**: CP-T03-00 (roughly doubles combat deaths); extra `train` candidates from new `verb_capability` rows (01, 03); 09's `at_war` edit (only a declared war counts); 09's `raze` refusal.
- **Layer 1**: Ask C (04); the `cession` gate permission in 04's `surrender` (whether it counts as Layer 1 is unverified in the file); 03's rescue basis (parked); the AX-2 passage of 10's `estates_named` stamper (unverified).

## 6. Left open on purpose

- Two interface demands the fix pass did not reconcile: 10 accepted 04's siege leg through `relocate=False`, but 04 then dropped the leg (10's acceptance is moot); 03 parked `rescue`, so any reference elsewhere to rescuing a captive by force has nothing to land on.
- 06's own ledger reads "asked 0" while the file carries JA-1; the row it rests on is counted elsewhere.
- Four items exist only under an answer: 03 CP-T03-03/-04 (JQ-2 (a)), 04 CP-T04-04 (Ask C) and -10 (Ask A).
- `CLAUDE.md` §5 cites `engine/autoload/dice_engine.py`, which does not exist (the description's defect #9). That is a Layer 0 edit outside this task; it is named here and not made.
- Nothing here proposes a player-facing client. Every file designs for the Act interface; the Godot port stays blocked on canon (`CLAUDE.md` §6).
