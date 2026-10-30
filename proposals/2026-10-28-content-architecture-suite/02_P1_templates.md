# P1 · Templates: three coherent packages

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Part 02 of the suite. Base: `rd_070744_P1_templates.md` (the session's read at 07:07:44, line numbers stripped). `heredoc_070810` (adds the part title and the first corrections) was replayed against it and the result is byte-identical to the session's later read `read_072308_02_P1_templates.md` and to `p1_clean.md`, which validates the method. Then replayed in time order, all applied: `heredoc_072419`, `heredoc_072426`, `heredoc_072811`. None failed. One residue of the original sweep is kept as found: line 23 reads `04:801/:802` (the sweep's `and :802` pattern did not match it); the other citations in the suite read `:810`. The suite was written in a session of 2026-10-28 that committed nothing; its files existed only in that session's scratchpad. This directory is a reconstruction from the session transcript's surviving reads and patch scripts, not the original files. Not recovered: the lens-3 (directive-compliance) critic report, parts 05, 06, 07a to 07d and appendices A1 to A5. Edits the session made by tools other than Bash heredocs (Edit-tool calls) were not captured, so the text may differ from the session's final file in ways not recorded here. Where this text and the tree disagree, the tree wins; every figure and line citation is as of the session's HEAD (`ttrpg` be24c71) and is unre-verified.

---

*Part 02 of the review suite. Corrected after the conflict adjudication (07a to 07d).*
Repo `be24c71`. Proposals only; nothing here is built or ruled. Drafted instances carry `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]`.

**Verdict.** All three share §1 (dossiers, order menu, minigame seam, troop and kit templates). They differ in how much authored story sits above emergence. **Recommended: B.** A is the baseline: it can be built first, and B adds to it. B differs from A in one respect that matters to your sameness concern: B's stories are drawn from pools when the world is built, so two worlds do not tell the same tale.

| item | A · Dossiers only | B · Set pieces + pools | C · Dockets + fixed beats |
|---|---|---|---|
| set piece | goal rows + 1 seed claim, the same in every world | the same bundle, drawn from pools at world build, so worlds differ | fixed beats and cast roles; a card may set a date |
| event deck | Tensions: 1 card per world, at build | pools on a seat or place; a few cards drawn per world at build; nothing is drawn in a season | seasonal docket drawn by a seat-holder's `convene` |
| troops (M3 A) | stock only | stock, then field force (M-1) | field force (M-1) from the start |
| kit carrier (J-T5) | stores kind on a rung | `hold` on an Item (persons); stores (troops) | Items for persons and troop kit |
| ratified texts amended | 04:801/:802 (M3) | M3, the B10-19 clause, the Tensions schema widened, and a plan-text amendment (`part12:276`: a row may quote an arc in `source:`) | M3, T-c (reopening the confirmed default), AX-5's fourth motion, ED-WR-0011, and arcs as loaded templates, which is the whole-arc scripting you excluded |
| arcs reachable (of 55) | ≈25 | ≈36 with `foreign` off (the confirmed default); ≈40 if you turn it on | ≈46 |
| set pieces / cards to author | 16 / 6 | 16 / 72 | 36 / 102 |

## 1. Common to all three

**In plain words.** A *dossier* is one sheet per character, faction or town, written once and read when the world is built. A **field** is a value on the sheet ("Klapp holds the Temperance seat"). A **query** is a question the game asks fresh each time ("how many are loyal to the Crown now?"): always right, with no sheet to edit. The *dossier report* prints the sheet beside the live answers, so everything about the Crown is on one page.

**Authoring-layer rule.** A field is true at the start, has one author, and no act has touched it yet. Anything that counts, sums or compares, or that an act in season 1 could make wrong, is a query. A starting value for something that changes later (stores, body, stance) is compiled into its owning record at build, and the dossier is not read again. The dossier becomes the head: `npc_registry.yaml`, the person fields of `npcs.yaml` and the holder column of `offices.yaml` move into it, behind an exporter `--check`. It lives in `engine/season/dossiers/` with one loader, pending a `layer-conformance` check against 04 row 27a.

**Character dossier.** Source: the `character_canon_v30.md` §2 sheet, keeping only fields that have a reader.
- *Identity:* id, name, heritage, born, home (becomes `reside`).
- *Position:* offices (`hold`), faction (`commit` to the creed), oaths (`oblige`), ties.
- *Capability:* the attribute block, whose keys follow the M2/J-T2 ruling (nine today; the demand-derived eight and #505's six are in part 03); practice keys; TS; starting body; kit.
- *Ambition:* goal rows, a ladder (`goal_stages`, M20(b)), a catalyst want.
- *Values:* pursuits, conviction, stance seeds.
- *Personality:* three offsets, built behind a spread-0 control.
- *Knowledge:* up to 12 seed claims.
- *History:* a lifepath key (origin, formation, vocation, catalyst). It expands into the fields above at build and is never stored.
- *Colour (read by nothing):* beliefs, speech, physique. Cut [RETIRED]: Ethical Disposition, Behavioral AI, the arc state machine.
- Queries: standing, regard, prowess, current stage, wealth, exposure.

**Faction dossier.** Fields: creed (becomes the creed Proposition), founding leader, role template, seats with bodies, starting land (`hold`), goal rows, relations at start, HQ, foreign flag, colour. Queries: members, strength (`mustered`), wealth, cohesion, standing per viewer, `at_war`.
*Crown (worked):*
- creed: the dynasty holds the peninsula (`goals.yaml:41-45`)
- leader: NPC-020 Almud Almqvist (`rosters.yaml:1667`)
- role template: `sovereign` (`rosters.yaml:1633`)
- seats: `off_king`, `off_duke_valorsmark`, …
- goals: `goal_crown_peninsular_sovereignty`, `goal_crown_resist_altonia`, Inner Circle
- sub-orgs: Lion's Table, Royal Investigators, Riskbreakers; report today: 11 members, 6 rungs, 11 seats, no head

**Settlement dossier.** Fields: parent, geography row, type (which sets quarters and buildings, from `venues.yaml`). The Prosperity/Defence/Order triplet is used only as build seeds, for starting stores, garrison condition and cohort stance. Also: cohort seeds (pursuits, conviction, stance), a local Mayor seat (vacant, E2), planned works (M5), site endowment, colour. Queries: population, larder, defence, prosperity, unrest, the holder's standing.
*Goldenfurt S-006 (worked):* T2, Town, Crown, triplet [2,0,2]: "tolled river-ford; Guild toll dispute" (`valoria_geography_v30.yaml:288-294`). Drafted: cohort wealth .4 and community .3, stance −1 toward the toll's holder, Mayor seat vacant.

**Management order.** Fields: author (the seated person), seat, verb, subject, delegate, amount. Which verbs count as orders is decided in one place only, the `management:` column on the verb row (below); no prose list is authoritative. The built seat verbs that are candidates are `confer`, `revoke`, `establish`, `dispatch`, `issue`, `requisition`, `transfer`, `seize` and `covenant`. `tax`, `ration` and formation orders are unbuilt. What a seat can order depends on that seat's `remit_acts`, not on its rank: the Confessor (a rung-1 seat) holds `confer` and `revoke`, while Klapp's and the Lord Steward's seats offer `issue`, `covenant`, `requisition` and `seize` (measured, part 04 §1). This is the weak reading (the seated person is the author of record), so AX-1 is unchanged; part 01 §13 gives the choice between the weak and the strong reading.
- **What "free of the scene budget" means, in plain words.** Today every act a person takes in a season draws on a small budget of scenes. You asked that management orders not draw on it. If the order is only a rule on a verb row, it applies to every person in the simulated world, so every lord and cardinal also gets free orders and the whole world changes. The alternative, free orders for the player's person only, breaks the rule that the player's options are exactly what the computer would give that person. Either way it changes a number you ruled on 2026-09-02 (`decision/budget.py:19-20`), so it is a ruling (part 01 §11, item 10). It should live in the one place that owns the budget and the release count (`Scene.cost`, `deliberate.py:252-258`), not in a new column that a second place also reads.
- **What the order does.** An order writes exactly what its verb row writes, no more. Orders that another person carries out (`dispatch`, and the executors of an `issue` dispensation) spend that person's budget. Orders that write a holding directly (`confer` writes the seat Tenure itself; `seize`, `transfer`, `requisition` move holdings) have no delegate and cost what the verb costs in the world (a revocation cost, a spent treasury).
- Falsifier: a scripted list equal to the chooser's picks reproduces `content_hash`.

**Minigame provider row.** Fields: role, verb, provider, `module_entry`, input type, decision moments, result, write cells. Built roles: `contest`, `inquiry` (`manifest/registry.py:38-39`). Three fidelities, one resolver, parity per moment.

**Troop stock (M3 option A).** Precedents: RTK's officer and troop count (T13:47, :78); Total War's unit card [FROM MEMORY]. Nothing here is built (TS-1..12).
- Fields stored: commander (a person: the seat-holder or a sworn officer); type (one of the 10 rows of `TROOP_TYPE_STATS`); count; kit kind (a `TROOP_LOADOUT` row); home rung. That is a stock by kind and a count, nothing more.
- Read as queries, never stored: grade (raw, drilled, seasoned, veteran), discipline, morale and upkeep. Layer 1 refuses a stored discipline value on a Rung (`holonic_ARCHITECTURE.md:384`, T-i), and a population that grows by itself is not one of the world's three motions (AX-5). So replenishment happens only through an act (a levy or a recruit) or through the cohort's weight (J-C-2); there is no regrowth timer.
- *Worked (illustrative; corrected after adjudication):* Ehrenfeld S-014: pike, drilled, 300 men, medium armour, commanded by NPC-072 Olaf Geirson, who is Löwenritter, homed at S-014, and holds Hafenmark's Military Commander seat (`offices.yaml:456-463`). `[ASSUMPTION; example only; revert: delete]`
- **This amends ratified 04:801 ("units = PersonId[] … NO unit class") and :810. It needs Jordan's explicit yes (M3).**

**Kit: tactical-RPG structure, values from physics.**
- *Item template:* a `modules/combat/weapons.py` record (54 keys): mass, part positions, head length, grip, hands, head, geometry. Performance figures come from `weapon_physics.py` (built); none is set by hand. Armour is a tier and reduces damage only.
- *Structure:* slots (main hand, off hand, body); proficiency as practice keys per weapon family; no fixed weapon triangle: matchups fall out of the physics (bind, reach, armour) and are learned by fighting, shown to the player only as the character's own familiarity, never as a preview or forecast; condition that wears; coin upkeep; acquired by loot (`seize`), craft (`work` at a forge) or purchase (`transfer`). Precedents: JA2 T14:26-41; Battle Brothers T02:170.
- *Worked:* NPC-072's sword: template `arming` (`weapons.py:90`), point of balance about 11 cm, medium armour, `blade` practice.

**Variety instrument (NEW, `harness/variety.py`, reusing `storybar.chains`, :374).** Run N world seeds for S seasons. Per world, sign every cross-person chain of depth ≥3 as (verb sequence, actor role classes, subject kind), keyed by role, not name. Report mean pairwise Jaccard between worlds and the **stock share** (signatures in at least half the worlds).
- Controls: the same seed twice must read 1.0; `draw_seed_arm` gives the dice-only floor.
- Falsifier, two-sided: a proposal fails if its content does not lower the mean similarity by more than the seed spread, **or** if it raises the stock share. Jordan sets the bar.

**Klapp facts every form uses.**
- Klapp holds `off_cardinal_temperance`; the registry's "candidate" loses to the code.
- He shares `b_s_036_cathedral` with Haelgrund (NPC-004, Senior Inquisitor, `determine`) and Olafsson.
- Built: `research` puts a finding in the researcher's own ledger; `open_case` declares its stages (`verb_table.yaml:963`); `inquisition_hearing` disposes `ban` (`arrangements.yaml:234`).
- **Gap in every form:** TS is "written by none" (`harness/loops.py:96`). The fix is **one** TS writer, on Klapp's own `research` of a Thread-significant Record at RESOLVE, on the `train` precedent. It needs a write-matrix row and a magnitude sourced from canon (his starting TS is `null`, a [GAP], at `npc_registry.yaml:1032`); it does not wait on J-T2, since TS is already a field on `Person`. No other step writes TS.
- **"Exposure" has one meaning in this suite.** `exposure(I, Klapp)` is a query: the number of claims in Inquisitor I's own ledger about Klapp's restricted handling. Co-located witnessing deposits them (built), so each Inquisitor's count differs. `conceal` lowers it; `tell` raises it. It is never a Record kind and never a track.

## 2. P1-A · Dossiers over the existing carriers
**Premise.** Author only starting facts, compiled into Propositions, Tenures and Rungs. Every story still comes from persons acting on those facts.

**Klapp.** Its rows exist in every world.
- *Roles, bound by seat query:* scholar = Temperance seat; inquisitor = Senior Inquisitor seat; presider = Confessor; witness = anyone present with TS ≥ gate.
- *Precondition:* two drafted lock-object Records in the archive.
- *Beats:*
  1. Klapp's goal row (object: the locks) makes him `research` them; each act deposits a finding and adds TS.
  2. Co-located witnesses deposit claims about him.
  3. The player's `thread_read` at the archive yields a finding (a finding about a person is NEW).
  4. **The choice:** the player's `tell` to Klapp, or to Haelgrund, or `conceal`.
  5. Klapp's own chooser then picks: keep researching, `tell` Himlensendt, or `conceal`.
  6. Haelgrund's seat goal (`deed_doers`) raises the question. If he chooses, `open_case` opens a hearing; `determine` ends in `ban` or nothing.
- Every write belongs to an act.

**Elsewhere.** Goldenfurt has no local cast. Troops are stock only (a won march arrives without its men). Kit is a stores kind (`arms_<class>`, `armour_<tier>`); a person fights with the best class at his rung: no new object, but no heirlooms. Tensions: 6 cards, one drawn at build.

**Resolves:** M16(b) kept; M20(b) used; M3 A. **Rulings:** M3 and J-T2; nothing else ratified. **Plan:** a DOSSIER position after B10-10 and before B10-S (B10-S itself sits after B10-10 so that attributes exist); VARIETY with the B10-02 instruments; the TS writer in CL-ATTR; CL-TROOP on M3's yes.

**Cells to fill:**
- 46 persons × 15 open fields ≈ 690
- 10 factions × 5 = 50
- 37 settlements × 6 = 222
- 16 set pieces × 5 = 80
- Agents draft them all; Jordan checks attribute values and ladders first.

**Arcs ≈25:** the plan's 17, plus family G through TS and part of I. **Risks:** Klapp's story runs in every world, which is a stock story; variety rests on 1 Tensions card in 6 plus personality. **Falsifier:** the variety instrument, A's content on vs off; A is expected to raise the stock share. **Precedent:** `goals.yaml`; B10-18; narration W8 rung 2.

## 3. P1-B · Dossiers plus pools drawn at world build
**Premise.** A set piece is a bundle of role-bound goal rows and one seeded claim that hangs on a seat or a place. Each world draws a few bundles from the pools **when it is built**, and only a person's own act ever opens the story. Nothing is drawn during a season, and no clock ever emits an event.

*Redrafted after the lawfulness review.* The first draft drew cards inside a person's act and staged Records with a Thread-Sensitivity step at each stage. That breaks three standing texts: B10-18:183 ("a card is a world-generation draw: read once at build, by no step of the season loop"), B10-19:95 (no stage store; no dealing per season) and the T-c default you confirmed on 2026-10-26 (ED-IN-0301). It is kept below as the variant B+, which needs those reopened.

**Pool card fields:** id, family, `source:` (an arc quote), eligible (a build query), attach (seat or place), roles (queries to seats), goal rows (role-bound), one seed claim in one ledger, and `opens_with` (the name of an existing verb the opener may choose; the verb declares its own stages, e.g. `open_case`, `verb_table.yaml:963`). Nothing on the card is a date, deadline, firing condition or outcome, and B10-18:183's "may not be data" list is kept whole. The two changes are that goal rows may be role-bound and that a card may carry one seeded claim.

**Klapp.**
- *Pool:* the archive (6 cards). A world that draws "the uncatalogued lock" at build has a Klapp story; a world that does not has none, which is where the variety comes from.
- *If drawn:* Klapp's seat gets a goal row (research the locks); one seeded claim sits in the ledger of the person the card names. His `research` then deposits findings in his own ledger and, through the single TS writer (§1), adds Thread Sensitivity.
- *Discovery:* at TS above the gate Klapp can form `thread_read` himself and finds out by his own act. **The choice:** the player can tell him before then.
- *His ladder (M20(b)):* conceal → seek counsel → disclose or convert. These stages only add referents to his own `need` question; they write nothing.
- *Inquisitor:* Haelgrund's seat already carries a goal row (`deed_doers`), bound at build by seat query. Whether a band on his own ledger (the count of claims about Klapp) raises the question is B4.1, which the plan holds with no owner; without it he opens a case only when his ordinary chooser picks `open_case`, which declares the stages of the hearing.
- *Endings:* none authored. Persons choose among `ban`, retention, conversion (`commit` to the Restoration creed, `move` toward Maret) or disclosure.
- *Rendstad:* a second instance on the Doctrinal Compliance seat's pool (part 01 §8).

**B+ (not recommended now).** Cards read inside an act, with staged `exposure` Records and a Thread-Sensitivity step at each stage's maturation. It needs: B10-18:183 and :193 amended (a loop step would read a card); B10-19:95 amended (a stage store); the T-c default reopened (a term a card authored falls due after build, `loop/matter.py:336-339` says terms are act-declared only); and the `research` verb row, which writes `[]`, given writes. It is closer to C than to B.

**Elsewhere.** Goldenfurt: a court pool of 6 cards re-bound from G101–G606, drawn at build and opened only by a person's `convene`; roles bind to seats, and Hedda's local cast needs ED-WR-0011 (a ruling that only P1-C charges today; B needs it too if Goldenfurt's cast is added). Crown: a council pool on `off_king`. Troops: stock first (M3). Field force (M-1, amends 04 further) is a later step. Kit: a person's Item held by `hold` (lost, looted, given, witnessed); troop kit in stores; the Item kind needs `layer-conformance`, and your yes if 04 §B.7 closes `hold`'s objects. Minigames add a fieldwork case board and a `working` role.

**Rulings:**
- M3 (reopens the default confirmed 2026-10-26); J-T2.
- A plan-text amendment to `part12:276`: a row may quote an arc in `source:`. ED-IN-0225 itself refuses only an arc carrier and M20(b) already narrowed it, so this is not a question for you.
- B10-19 clause: "a scenario is world-generation data read once by `build_realm`, opened mid-game only by a bound person's own act".
- The Tensions schema widened to role-bound goal rows plus one seeded claim.
- B4.1 given an owner (optional: without it, the Inquisitor acts on his ordinary chooser).

**Plan:** CL-SETPIECE after CL-EVENTS commit 4 (loader, then the build-time draw, then 8 rows); B4.1 into B10-19; the Item kind after K-1.

**Cells:** the common cells, plus 16 set pieces × 8 and 12 pools × 6 = 72 cards. A world draws k bundles from pools of size P; keeping P at least k² keeps the expected overlap between two worlds under one (part 01 §8). Because the draw happens once at build, repeated visits to one place cannot empty a pool.

**Arcs ≈36 with `foreign` off (the confirmed default), ≈40 with it on:** families B (summons), G, the NEVER arcs; D needs `foreign`. **Risks:** a bundle opens only if someone chooses to act on it (in the one stored two-season run at seed 0, 327 of 1,132 attempted acts produced an event other than a refusal, `proposals/2026-10-22-system-description/ctl/realm_seed0_2seasons.txt:1-40`, so many bundles may sit unopened); cards may drift into scripting. **Falsifier:** similarity between worlds falls and the stock share does not rise; control: empty pools give an identical hash. **Precedent:** narration W8; Goldenfurt's Hold Court.

## 4. P1-C · Authored set pieces and per-season docket decks
**Premise.** Each season, named seat-holders draw a docket by their own `convene`. Set pieces have fixed beats and cast roles. A card may write a *situation* on a date (a Record or a claim with a due season), never an outcome.

**Amends** (the last item conflicts with your instruction that arcs be scripted as hooks and sequences, not whole):
- **T-c** (`01_AXIOMS.md:376-388`): a term a card authored may fall due after build. Buys dated beats.
- **AX-5's fourth motion** (M16 §1a): a card may write a situation with no actor. Buys pacing and guaranteed exposure to set pieces.
- ED-IN-0225: arcs as loaded templates, which is the scripted whole arc you excluded.
- ED-WR-0011: local casts.
- B10-19.

**Klapp.**
- Season 1: an intro scene is offered to the player.
- Seasons 2–3: Klapp's `research` adds TS; **the choice window** is open.
- Himlensendt's season-1 docket card "archive audit" writes an audit Record due in season 4. Then the Senior Inquisitor's question is raised and a hearing goes to `determine`. The outcomes remain persons' acts.
- Card fields: B's, plus `due_in` and `situation`.

**Elsewhere.** Goldenfurt gets its six local dossiers (G01–G06) and its 28 cards re-bound. The Crown has a realm docket of 24. Troops are a field force from the start, and grade rises by surviving a field (TS-10, J-5). Items cover persons and troop stacks, and travel with the force.

**Cells:** the common cells, plus 48 local persons × 15, 36 set pieces and 102 cards.

**Arcs ≈46:** dated situations stand in for THRESHOLD arcs; the lost four still need the substrate. **Risks:** dates feel scripted; same set piece in every world; two axioms fall; largest content load. **Falsifier:** as above; control: dates off gives B's hash. **Precedent:** KoDP's 544 events (T16:230); Triangle Strategy (T19:24).

## 5. Recommendation and the common items
**B.** It answers the sameness concern with authored *openings* drawn at build while every outcome stays a person's act. It needs M3, the B10-19 clause, the widened Tensions schema and one plan-text amendment; it needs none of the axioms reopened. Take C's dated docket later, only if the variety instrument shows B's bundles going unopened.

**Common to all three:** the dossier layer and its report; the management-order surface (§1); the provider row; the troop template (M3); the kit template; the TS writer; the variety instrument. Arc counts are family-level estimates [CONFIDENCE: low]. Cell counts are design estimates.
