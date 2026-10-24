# Season, persons and the chooser — completion proposal (T02 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item and ask is held back for Jordan's adoption, item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. What it changes in `engine/season/`: nothing, until adopted.
## Written against: HEAD `2decf4a`. Inputs: `proposals/2026-10-22-system-description/2026-10-22-system-description-03-t02-season-persons-choosing.md` (in full) and `…-00-overview.md` §3, §5.2, §6; `research/game_precedent_suite/dispositions/D_T02.md` (every row); `research/game_precedent_suite/THROUGHLINES.md` (in full); `proposals/2026-10-16-verbs/2026-10-16-verbs-01-thesis-and-persons.md` (in full), `-02-attributes.md` (headings), `-18-lexicon-npc-life-and-persons.md` (Suite G, succession; grep), `-04` (D-V6 row); `proposals/2026-10-21-v9-remediation/` part 01 §1.4, part 02 REM-21…REM-25, part 03 §2.8-§2.9, part 04 §3; `workplans/valoria_master_workplan_v9.md` (index rows), `_part4` IN-14, IN-46, IN-47, `_part5` IN-48, IN-57…IN-61 and §A (A-26…A-37); `architecture/meta/01_AXIOMS.md` T-a…T-l; `architecture/ARCHITECTURE_V2.md` §F2; `skills/ners/SKILL.md` §§0-5. Code opened at HEAD: `es/queries/world_q.py` (`endings_reached`, `_ending_edges`, `ambitions`, `goal_referents`, `_goal_referents`, `vacancies`, `seats_named`, `writs_held`, `questions_for` Q4 and the standing-occasion splice), `es/queries/person_q.py::conviction_after_crisis`, `es/decision/budget.py:40-90`, `es/decision/choose.py::declare_intents`, `es/loop/deliberate.py:160-175`, `es/loop/matter.py:285-304`, `es/state/world.py::remove_person`, `es/state/carriers.py` (`Sensation`, `Proposition`, `Office`), `es/harness/play_surface.py`, `es/goals.yaml:1-60, 230-234, 450-471`, `es/hole_register.yaml` H-10 (`:176`), H-92, H-230; `es/verb_table.yaml` (`tenure.closed` emitters); `es/epistemic.py::_ch_chronicle`.

Abbreviations: `es/` = `engine/season/`; "T02" = the system-description tutorial above; "D_T02" = its dispositions (rows cited
`D_T02:#row`); "TL" = `THROUGHLINES.md`; "REM" = `proposals/2026-10-21-v9-remediation/`; "P5" = `workplans/valoria_master_workplan_v9_part5.md`.
Evidence grades are carried from the source, never upgraded. `[UNVERIFIED]` marks a claim whose call site I did not open.

## §0 The genre loop

The yardstick genre is the dynasty/realm and character-driven strategy game (CK3, Old World, Genghis Khan II, King of Dragon Pass, Football
Manager). Its player chooses as one person, against a budget, with a character whose qualities and history change what a choice costs and
returns, toward ambitions that are met or fail, and the line continues past that person's death. Each opportunity is graded on what the
season loop affords **today**, with the evidence grade the source gives.

| # | play opportunity (choose · cost · lasting consequence) | precedent | today | evidence |
|---|---|---|---|---|
| G1 | **Take up an ambition and see it through**: pick an aim, spend seasons on it, and know when it is met or lost | D_T02:#OW5, #A10, #A16, #FM1, #E5d; TL P19, P42, TM12 | **PARTLY**: ambitions pick each person's subject (46 of 46 named persons answer a `need` in round 0, T02 §2.2); nothing tests whether an aim is met (T02 §5a); a `seat_holders` goal whose seat is vacant forms no question at all, whatever its side (`es/queries/world_q.py:2031-2037, :2618`), and a creed or want whose subject has been removed still forms one (`goal_referents` returns `(prop.subject,)` for every Proposition no goal row names, `:2011-2013`) | RUNS-IN-LOOP (attention); completion DESIGN-ONLY |
| G2 | **Earn the turn**: a per-season action pool whose size the person builds by what they hold | D_T02:#OW2, #OW3, #GK1, #A23; TL P05 | **PARTLY**: budget = 5 + live holds − body bands − legs runs; it is filled by paper (mean 5.57 → 7.69 in two ticks, 11 of 74 above the 10-action ceiling, T02 §2.6; H-92) | RUNS-IN-LOOP (pool); earned fill DESIGN-ONLY |
| G3 | **Who you are changes what it costs and how it lands** | D_T02:#GK3; TL P15, P23 | **ABSENT**: `capability` empty on every realm person; every social pool 2 (T02 trap 7) | DESIGN-ONLY (J-T1) |
| G4 | **Choose knowing the stakes**: odds shown at the point of choice | D_T02:#A2, #A13, #A17; TL throughline 2 | **ABSENT**: neither chooser nor callback receives odds (`es/harness/play_surface.py:14-19`) | DESIGN-ONLY |
| G5 | **Deeds move relations**: what you do to someone, and what others see you do, changes how they regard you | D_T02:#E3h, #IX13; TL P11 | **PARTLY**: stance rows dominate the score; only `forgive` and a lost field write them; judged deeds enter `regard` at read (IN-58) but reach choice only under H-194's `declared` arm (P5 IN-58 STATE) | RUNS-IN-LOOP (read); the choice-reaching arm TESTS-ONLY |
| G6 | **Become someone through what happens** | D_T02:#E3d, #E3g, #IX5, #E3f; TL P33, TM01 | **PARTLY**: conviction folds at scar ≥ 3 (5 / 0 / 3 at tick 1, seeds 0-2); pursuit shift ships at 0; RESTABILISE not built (`es/queries/person_q.py::conviction_after_crisis`) | RUNS-IN-LOOP per seed (folds); shift at control |
| G7 | **Start something that lands later** (a scheme, a project) | D_T02:#A1; TL P04, P13, TM06 | **ABSENT** for persons: an act resolves in the round it is released; only record and `oblige` terms mature at MATTER | DESIGN-ONLY |
| G8 | **The line goes on**: on death, control and holdings pass to a successor by rule; a dead line ends the game | D_T02:#GK5, #A9, #OW7; TL P30, TM05 | **ABSENT**: `succeed` declined; the King is dead after tick 0 in every seed and the throne stays vacant; IN-61 stopped at H-230 (no claim ever names a vacated seat; seat ids do not match `offices.yaml`) | DESIGN-ONLY |
| G9 | **Win, lose, or be removed**: a terminal check, and a recoverable failure short of death (expectations missed, office lost) | D_T02:#OW6, #FM1, #KD5, #A10; TL P41, P42 | **PARTLY**: `endings_reached` is read each season and halts nothing; neither row is reached in the realm; no one is commended or removed for an aim | RUNS-IN-LOOP (read); reaching TESTS-ONLY |
| G10 | **The world makes drama unwatched**: rivals pursue aims, kill, rise and fall | D_T02:#A12, #E4d, #IX8, #IX1; TL P38, throughline 6 | **PARTLY**: deaths and feuds happen with nobody watching (`person.died` 9 / 6 / 11); a vacated seat is news to nobody (H-230 limit 1); nobody joins a cause he hears of (`commit` 61/0 on wrong-class referents, T02 §4 A) | RUNS-IN-LOOP (deaths); succession and recruitment DESIGN-ONLY |
| G11 | **Delegate and be advised** | D_T02:#GK4, #FM3, #A11, #A20, #IX3; TL throughline 1 | **PARTLY**: the seam passes `auto` to a callback (`play_surface.py:41-52`); the callback sees one question only (`question_aggregation_rule="first"`, `es/data/fixtures.py:481`) and no in-world delegate exists | TESTS-ONLY |

This is the yardstick: an item below exists only if it moves one of G1-G11 toward AFFORDED, or is the substrate one of them needs. G2,
G3, G5, G6 and G11's delegate half are already owned elsewhere (§1); this file builds G1, G4, G8, G9, G10 and the Act-interface half of G11.

## §1 Gap ledger

Rows addressed: **39** — all 30 LACKS rows and the 9 DIFFERS rows that carry a risk (OW4, OW5, GK2, FM2, KD4, E3b, E3c, E5c, A23; A5
records no risk). The 8 CONTRADICTS rows (OW7, GK7, FM4, FM5, E3e, C1, C2, C3) are corrections to documents, owned by the suite's own
Part 2 edits; none is a game gap, except that OW7's legacy rule is composed below by CP-T02-05 with CP-T02-06. Ending of each gap:
**item** (this file), **named** (a remediation item or a v9 position), **declined** (five-step answer), **ask** (§6).

| gap | rows | ending |
|---|---|---|
| **Γ1 An aim can be met or lost** | OW5 (DIFFERS), E5d, FM1 | **item** CP-T02-03. The goal still never acts (A-31 holds): a Query changes which questions form (T-b) |
| **Γ2 Duty: commended or removed for an office's aim** | A10, FM1 | **item** CP-T02-04 (the occasion); the removal itself is `revoke`, whose reach is T08's |
| **Γ3 Causes spread; ambitions on offer** | OW5, A16 (HAS, risk-free), OW7 (composition) | **item** CP-T02-05, on REM-21's stamper registry and REM-23 |
| **Γ4 A vacated seat is news; the heir can claim** | GK5, A9, OW6 (world half) | **items** CP-T02-01, CP-T02-02 (H-230 limits 1 and 2), which unblock IN-61; the ending rows themselves are IN-27's (B-U, landed) — reference, not repeated |
| **Γ5 The seated person's line continues or ends** | GK5, A9, OW6 (player half) | **item** CP-T02-06; **ask** AQ-T02-1 (which ties pass control) |
| **Γ6 Choosing knowing the odds** | A2, A13, A17 (odds half) | **item** CP-T02-08: the Act interface shows the TRUE odds by calling T01's `odds_of` (CP-T01-03); no second odds function. Whether expected success enters the NPC score is T01's consolidated ask **AQ-X1** (cited, not re-asked) |
| **Γ7 The seated person's menu** | KD3 (partly), FM2 (DIFFERS) | **item** CP-T02-07 (the question list). KD3's width itself: **declined**, step 3 (ARCHITECTURE_V2 §F1: the opening set is every eligible candidate; its third clause is "the whole epistemic design"). FM2: **declined**, step 5 — the fingerprint skip already re-asks a person when an input changes (`es/loop/deliberate.py:167-170`), which is "advance until something needs you"; IN-46 adds the fight suspension |
| **Γ8 Earned budget** | OW3, A23 (DIFFERS), OW4 (DIFFERS, ruled unit) | **named**: IN-14 (shape delegated-ruled 2026-10-12: count holds with non-empty `granted_acts`; more rounds; `_part4` IN-14 STATE). OW4's price-per-scene is ruled (`es/decision/budget.py:19-20`); its paper-minting risk dies with IN-14 |
| **Γ9 Actor quality** | GK3 | **named**: J-T1 (attribute block; overlap, not repeated) |
| **Γ10 Setup and seat choice** | OW1, KD1 | **named**: IN-47 / REM-30 (D-2 ruled yes; creation arm C1 falls back to "the player picks a person the builder seated", `_part4` IN-47) |
| **Γ11 Played scale shift** | A3, A6 | **named**: IN-46 / REM-31 |
| **Γ12 Material pressure that can end a person** | KD5 | **named**: RB-5 (REM-50…REM-52; JQ-6 holds the magnitude) |
| **Γ13 Delegation that can fail in character** | IX3, A15, A20 | **named**: IN-48 (design first again, on Layer 1's `establish` + `confer` + `Tenure.term` route, P5 IN-48) |
| **Γ14 The killer gains; relations follow deeds** | E3h | **named**: IN-58 (judged deeds at read, built), H-194's `declared` arm (ED-IN-0296, held), and T03's actor-write fix (verbs-09 M1; overview §6 #7) |
| **Γ15 One load-bearing slot; noise** | IX13, E3b (DIFFERS), IX6 | **named**: JQ-1 (τ), JQ-3 (H-187 shift), D-V6 (contents-aware value), H-194. The score shape is ruled Layer 1 (`ARCHITECTURE_V2.md:508-528`; REM DEC-2) — the chooser-consequence items; not repeated. Any expected-success term is T01's **AQ-X1** |
| **Γ16 Wrong families formed (L2 cost)** | E3c (DIFFERS) | **named**: REM-21…REM-25, REM-2C |
| **Γ17 Failure-modal contests** | IX7 | **named**: T01's roll and J-13's remainder (JQ-2). CP-T02-08 makes the odds visible |
| **Γ18 Age changes capacity** | GK2 (DIFFERS) | **declined**, step 1: #457 D2 answered IN-34 as a hazard reader (delegated, [medium]); JQ-3 holds H-208's rates. Not re-raised |
| **Γ19 A recoverable inner state** | E3f | **declined**, step 3: T-a forbids a stored gauge (`01_AXIOMS.md:327`); the scar count per `(Person, element)` is the licensed carrier and ED-IN-0261 ruled the crisis an engine rule over state (`person_q.py::conviction_after_crisis` docstring). RESTABILISE's missing write is a magnitude (pursuit shift, H-187), held by JQ-3 |
| **Γ20 Escalation coupled to success; a director** | E4d, IX8 | **declined**, step 3: T-c — a clock no act wound is "what a GM is" (`01_AXIOMS.md:376-388`). The wound forcing sources are IN-35 and IN-36; attention to the prosperous already exists (`seat_holders` goals) |
| **Γ21 Authored content keyed to persons** | A8, KD4 (DIFFERS) | **declined**, step 3: scripting drift (`CLAUDE.md` §0); the occasion is generated from state (`attention_key`) |
| **Γ22 Schemes that land later** | A1 | **declined here**, step 4: the lexicon gives the plot to faction actions (`conspire`, DESIGN-ONLY, overview §3 FA row) and IN-59's access gate (B-Y) already makes preparation (learn, travel, strike) necessary. T09's proposal owns it |
| **Γ23 Surfacing causes** | IX11 | **declined**, step 3: REM DEF-6 defers `explain(p, v)` to M3, where the UI is its first reader; the causal log runs (D_T02:#IX2) |
| **Γ24 The word "salience"** | E5c (DIFFERS) | **declined**, step 2: a vocabulary risk in a tutorial; no game artifact reads it |

## §2 Items

Shared rules for every item: no new tenure kind, no new verb row, no new Event field, no stored aggregate (T-a), no threshold that
writes an outcome (T-b); every new closed set lives in `es/rosters.yaml` beside the roster it extends; every Query is in
`es/queries/world_q.py` (World first, Nobody's) or `es/queries/person_q.py` (person-side). Layer: all are **Layer 2** (game code and
the data it reads at runtime); CP-T02-06 and CP-T02-07 also touch the play-surface seam (`es/harness/play_surface.py`, Layer 2 harness).

### CP-T02-01 · A death names the seats it empties (H-230 limit 1)

- **Adds.** This item owns H-230's sweep arm 2 (R4). When the death cascade (`es/state/world.py::World.remove_person`, the one owner,
  three callers: `_eff_kill` for `fight`/`accept`, `_eff_march`'s `total` arm, MATTER's `_die`) closes a live `hold` whose object is an
  **Office**, that same death write earns one `tenure.closed` per such hold, by the per-subject earning the gate already has
  (`Subject.earns`, `es/state/gate.py:1439-1446`: "`confer` opens one edge (`tenure.opened`) and closes another (`tenure.closed`)"
  from one write): the person subject earns `person.died`, each closed seat hold earns `tenure.closed`. It must stay ONE write: the
  closures and the `pop` "must stay in one `apply()`. Split them across two writes and every closure is refused" (`world.py:740-744`).
  Only Office holds earn it; Records and Rungs the dead held are not listed among a broadcast Event's changes (T10's estate route is
  separate and non-broadcast, R4). `tenure.closed` is a `binding_decision` emit, so `_ch_chronicle` deposits it in everyone alive
  (`es/epistemic.py::_ch_chronicle`; emitters `es/verb_table.yaml:276, :1036, :1076`).
  **What the code does today, corrected:** `remove_person` returns `[who]` (`world.py:783`), not the ids it touched; it runs only inside
  an already-open write and raises otherwise (`:745-754`); it sets `until` on every live edge naming the dead (`:755-759`). Edges
  OTHERS own (an `oblige` to his seat) stay in `w.tenures` with `until` set; edges HE owns (his `hold` on the throne) leave the
  owner-first view when `persons.pop` runs (`:760`; `tenures` iterates `self.persons`, `:283-295`) — which is H-230 limit (1). So the
  claim must carry the seat id itself (the Receipt's `changes` naming the Office the closed hold was on), not a Tenure id WITNESS can no
  longer expand; that carrier choice is the design-first step.
  **`emits:` cells that change:** `fight` and `accept` `Felled:` gain `tenure.closed` beside `person.died` (`verb_table.yaml:734`,
  `:794`); `march`'s degrees whose `total` arm calls `remove_person` gain it (`:860-861` `[UNVERIFIED which degrees reach the
  arm]`); MATTER's `_die` passes `emits="person.died"` as one kind (`es/loop/matter.py:158-162`) and must move to the per-subject form;
  `write_matrix.yaml`'s `(Person, body)` and `(Person, exists)` rows list `tenure.closed` (`:174`, `:239`).
- **Owner.** `World.remove_person` returning the closed Office holds (a new return, its callers ignore the old one), and the death
  writes of its three callers, each naming those holds as earning subjects. Layer 2. T08 (CP-T08-09) and T10 cite this item.
- **Primitives.** P27 (knowledge that spreads), P30's precondition (the successor learns), IX4 (permanent state made public).
- **Reads / writes.** Reads the dead person's live Office holds inside the death write. Writes nothing new: the `until` it already
  sets; adds earned kinds to the existing write.
- **Joins.** T08 governance: every vacated seat becomes a claim, so `seats_named` stamps it (`world_q.py::seats_named`) and refill acts
  (`confer`, `oblige`, `succeed` after IN-61) form; T08 must keep `vacancies`/`may_fill` the gate. T09: a vacated throne is a war aim.
- **Decision handed to the chooser.** Every person now holds "the throne's hold closed" as hearsay and may act on the seat (claim it,
  fill it, swear to it, march on it). Unwatched: every seat-holder's death becomes a succession scramble the realm hears about.
- **Falsifier.** In a seeded season, a planted death of a seat-holder: every living person's ledger holds a claim whose expansion names
  the seat, and `seats_named` returns it for a person who was not present → else not built. A death closing only `commit` edges earns
  no `tenure.closed` → else the item over-reaches.
- **Control.** Paired seeds (0-2), item on vs off: off reproduces today's hashes; the count of `tenure.closed` Events with a death as
  cause is 0 off and equals the number of seat holds closed by death on (the 8 / 7 / 10 seats vacated in two seasons, T02 §0a, are the
  expected order of magnitude).
- **Hash.** Mover, declared (every death's Events and every ledger; H-230 sweep arm 2 names it). **Revert:** the emission helper off.
- **Size.** S.

### CP-T02-02 · A built seat keeps its authored id (H-230 limit 2)

- **Adds.** `harness/populated.py` names a loop-built seat by its `offices.yaml` row id wherever a row exists (today it mints
  `off_<holder slug>` and keeps the map only in `w._office_census["authored"]`, which the loop never reads; H-230). The throne becomes
  `off_king`, the heir seat `off_heir`, so a `successions` registry keyed on row ids (IN-61) reads the realm's seats. Not an `Office`
  field: `04` §B.7's seat fields are Jordan's (A-29), so the fix is the id, not a column. A seat with no row (`off_npc_084`, the guild
  leader `harness/populated.py:1240-1250` builds without one) keeps its slug id: authoring a row for it is IN-61's content decision
  (R4), not this item's.
- **Owner.** `es/harness/populated.py` (world-gen); the ten `Office(` construction sites outside tests (grep of assignments, not
  readers, per `CLAUDE.md` §0.1 pt 1; only `populated.py:1400` mints slug ids `[UNVERIFIED for the other nine]`). Layer 2 world-gen.
- **Primitives.** none new; the precondition of P30.
- **Reads / writes.** World-gen only.
- **Joins.** IN-61 (its registry becomes readable); `goals.yaml` `seat_holders` rows and `Proposition.scope` (the seeding map becomes
  the identity map and can be deleted at its owner's commit, a deletion).
- **Decision handed to the chooser.** None directly; it is the substrate for the heir's `succeed`.
- **Falsifier.** `build_realm(0)`: every seat with an `offices.yaml` row has that row's id; `goal_referents` for
  `goal_crown_peninsular_sovereignty` returns the same holder before and after → else the seeding map was load-bearing elsewhere.
- **Control.** The same world built twice, old and new ids: the multiset of (post, rung, holder) is equal; only ids differ.
- **Hash.** Mover (ids fold into every hash), declared; pins naming `off_npc_*` re-recorded. **Revert:** the slug ids, and IN-61
  resolves `successions` through the census map at world-gen instead (`Proposition.scope`'s precedent).
- **Size.** M (pins).

### CP-T02-03 · An ambition can be met or breached (the aim state)

- **Adds.** `world_q.aim_state(w, p, prop) -> "open" | "met" | "breached"`, beside `goal_referents` (the one owner of what an ambition
  is about becomes the owner of whether it still has work). The rule is per goal object kind, a column `aim:` on the existing closed
  roster `rosters.yaml: goal_object_kinds` (`:1810`), so the kinds and their tests are one roster:

  | object kind | stance | `met` when | `breached` when |
  |---|---|---|---|
  | `seat_holders` | +1 | — | a listed seat has no live hold |
  | `rung` | any | the rung's `governing_hold` is held by a person committed to the goal's org | — |
  | `seat_holders` −1, `deed_doers`, `person`, and every creed, want and computed OUGHT (no goal row) | — | — | — |

  `seat_holders` −1 has no row because today's read already does its work: a vacant listed seat names nobody, so `goal_referents`
  returns `()` and Q4 forms no question (`world_q.py:2031-2037, :2618`). `orientation` mints nothing. No state is stored: each read
  recomputes from live `hold`s and `commit`s (T-a). **AX-6 clause 3** (`01_AXIOMS.md:345`, a Query monotone in the ENDED-edge set is a
  ratchet): both states read live edges only and each is undone by an act (a seat filled, a rung lost), so neither is monotone. A third
  state, `spent` (every referent a removed person), was drafted and is **dropped**: under the closed cast (ED-WR-0011, provisional, "for
  now") a removed person never returns, so `spent` is monotone in exactly the removals that end edges, and clause 3 refuses it.
  Creeds and wants about the dead therefore keep forming their question, as today; the fold refuses what forms, and that refusal is the
  person's feedback.
  **Reader 1, Q4 (`questions_for`):** `met` forms no `need` question; `breached` forms a `need` question whose referents are the goal's
  listed seats as Office-classed referents (the `vacancies` splice's shape), so the members of a faction whose throne is empty face the
  throne itself — today they face nothing (`:2031-2037`). **Reader 2:** CP-T02-04. (A third reader, offering a met ambition for
  `release`, was drafted and is dropped: `release` declares no referent class, CP-T02-05.)
- **Owner.** `world_q.aim_state`; the `aim:` column in `goal_object_kinds`; `data/goals.py` (its one loader) refuses a kind with no
  `aim:` entry. Layer 2.
- **Primitives.** P42 at person scale (a terminal check over state, per aim), P02's line-crossing (the crossing changes what can be
  chosen, never an outcome), TM12's "which stock first" via `rung` goals.
- **Reads / writes.** Reads live `hold`s and `commit`s. Writes nothing.
- **Joins.** B-U / IN-23: `legitimacy` and `stability` may read `aim_state` as an input (interface offered, not required). T09:
  `seat_holders` and `rung` aims are the faction war aims; T09 owns which goals exist. ED-IN-0292 (2) (pending): `seat_holders` is
  already a World read with no claim behind it (`world_q.py:2002-2009`); `aim_state` follows that answer, and becomes a read of the
  claims the person holds (CP-T02-01 supplies them for vacancies) if the answer comes back AX-7.
- **Decision handed to the chooser.** A met aim frees the person's attention for his next question; a breached aim puts the object in
  front of him (claim it, defend it, march on it). Unwatched: when the King dies, every Crown member's
  `goal_crown_peninsular_sovereignty` is breached, so the Crown turns on the vacant throne the same season.
- **Falsifier.** Two hand-built worlds through the real Q4: (a) a +1 `seat_holders` goal whose seat is vacant forms a `need` carrying the
  seat as `Office` (today it forms none); (b) a `rung` goal whose rung the org's member holds forms no `need`. Either forming today's
  question → fail. Mutation: drop the `aim:` column; the loader refuses.
- **Control.** Paired seeds 0-2, two seasons, item off vs on: the count of Office-classed `need` referents is 0 off and > 0 on in every
  seed where a +1 seat is vacated (the King, after tick 0, at all three). Formations on removed persons are recorded by question source
  as context and are not credited to this item (their source is not located here; the Church's −1 goal is not it, above).
- **Hash.** Mover, declared (Q4's output). **Revert:** drop reader 1; `aim_state` then has no reader and goes with it (ID-13).
- **Size.** M.

### CP-T02-04 · The superior hears an office's aim met or breached

- **Adds.** When `aim_state` changes for an ambition a person holds **by his seat** (a body or seat goal, A-32), the holders of the seats
  he owes a live `oblige` to (`faction_q.superiors`, the one superior relation, `01_AXIOMS` §E.1.5) get him and his seat stamped onto
  their first question as a standing occasion, after the vacancies (IN-53's splice). The change is read at deliberation from the
  current state against the subordinate's ambition, not stored; "changed" is approximated by the state being `met` or `breached` now
  (a standing occasion like a vacancy, re-offered while it holds; the scene tax H-203 records for `oblige` applies).
- **Owner.** `world_q.questions_for`'s standing-occasion splice, composing `aim_state` and `faction_q.superiors`. Layer 2.
- **Primitives.** P29's offence-to-consequence without a table (the consequence is a person's act), FM's board (D_T02:#FM1), TM04's
  defection arm inverted, TM12's promotion step.
- **Reads / writes.** Reads `oblige`, `hold`, `aim_state`. Writes nothing.
- **Joins.** T08 governance: `revoke` must be reachable by a superior (today one usable seat, vacant from tick 0, overview §3 GV row);
  `confer` of a second seat is the promotion. Without T08's reach, the occasion forms `forgive`, `give`, `fight` and refused `revoke`s.
- **Decision handed to the chooser.** The superior chooses: remove, reward, forgive, or ignore. Unwatched: a governor who loses his
  town is stripped or kept by his lord's inclination, with no rule deciding it.
- **Falsifier.** A hand-built world: a sworn subordinate whose seat goal is breached appears as a referent on his superior's first
  question and not on a stranger's → else not built; the superior's `revoke` executes through the real fold where T08's basis admits it.
- **Control.** Same world, the subordinate's `oblige` closed: the occasion disappears (it recomputes from tenures; a stored flag would not).
- **Hash.** Mover where any sworn office-holder's aim is met or breached; equal otherwise. **Revert:** drop the splice term.
- **Size.** S.

### CP-T02-05 · Causes a person has heard of are ambitions on offer

- **Adds.** One stamper in REM-21's registry for the `Proposition` class: `oughts_named(w, p)` = the OUGHT Propositions among
  `person_q.ledger_names(p.ledger)` (a witnessed `proposition.uttered`, a told claim naming one, a held document whose terms name one),
  It is `seats_named`'s shape one class over: a person can take up any cause he has heard of. Rows that form on it are those declaring
  `referent_class: Proposition`: `commit` (REM-23, remediation part 02:381-385) and `argue` (T05's CP-T05-04, which classes it). A row
  takes one class only (REM C4), and `release` is **not** among them: it declares no class and its domain is `[hold, commit, oblige,
  succeed, tie, knot]` (`es/verb_table.yaml:1028-1037`), so classing it `Proposition` would stop it forming on seats and kill the
  releases of `oblige`, FA-04's Split among them (`es/offices.yaml:191`). Letting go of a finished cause stays `release` as built.
  **T05's stopping rule** ("do not widen the stamper" if `argue` stays at 0 after its class, T05 file :230) binds T05's own stamper; this
  stamper is a separate widening by this lane, declared as such, and `argue`'s formations on heard-of Propositions are counted in this
  item's mover, so T05 reads its control on both arms. **T09's opinion gate** (R9) filters this stamper's creed output (a creed is
  offered only where T09's join gate admits it); it is a filter on this one route, not a second route to membership.
- **Owner.** `world_q.oughts_named` registered with `@stamps("Proposition")` (REM-21). Layer 2.
- **Primitives.** P27 (knowledge spreads), OW5's ambition offer (D_T02:#OW5), KD7's standing occasion.
- **Reads / writes.** Reads the person's own ledger and `w.propositions` (mood only). Writes nothing.
- **Joins.** T09 factions: this is the one route to recruitment (R9; a faction is its creed plus its commits, T-h); T09's opinion gate
  filters it, and T09 decides whether a second live membership is admitted (D_T09 #23 records it is today). T05: `argue`'s class is
  CP-T05-04's. REM-21 and REM-23 are prerequisites, not repeated.
- **Decision handed to the chooser.** Join a cause or pass it by; the seated player's ambition menu is the causes he has heard
  of. Unwatched: a movement spreads by being witnessed and told; a dead leader's uttered cause keeps its followers (a Proposition is
  never destroyed, §14), which is Old World's legacy rule (D_T02:#OW7) in this engine's terms.
- **Falsifier.** A person who witnessed one `utter` of an OUGHT forms `commit` on it next deliberation and the act executes → else not
  built; a person who heard of none forms none.
- **Control.** Paired seeds 0-2: `commit` executions on a Proposition the actor did not utter, off vs on (today 0 / 1 / 1 in two
  seasons, T02 §4 A, almost all of them wrong-class); the share of ledgers naming any creed is read first, because if it is near 0 the
  item affords nothing at build and the control says so.
- **Hash.** Mover, declared. **Revert:** unregister the stamper.
- **Size.** S.

### CP-T02-06 · The seated person's line continues, or ends

- **Adds.** `world_q.continuations(w, p) -> tuple[person id]`: the living persons who would carry on `p`'s line, in the order of a new
  closed roster `rosters.yaml: continuation_ties` — (1) `heir_title`: holders of `successions[s]` (IN-61's registry) for each seat `s`
  `p` holds; (2) `sworn`: persons with a live `oblige` to a seat `p` holds; (3) `follower`: persons with a live `commit` to a
  Proposition on which `p` holds the maker's hold (`_makers_hold`, IN-11). The client of the play surface reads it each season while
  `p` lives (a Query on the living: the edges the dead man OWNED, his seat holds and maker's holds, leave the owner-first `w.tenures`
  view when he is popped, `es/state/world.py:283-295, :760`, while edges others own toward him stay with `until` set, `:755-759`) and, when `p` dies, re-binds its callback
  to the chosen successor between seasons — `overrides` is already "read at each call, not copied, so a client may add or remove a
  person between seasons" (`play_surface.py:45-46`). An empty last reading ends that client's run: the line is extinct. No world ending
  row is added (the `endings` roster is about the realm, not a controller).
- **Owner.** `world_q.continuations`; `rosters.yaml: continuation_ties` (closed, `open: false`); the re-bind is the client's, on the
  existing seam. Layer 2; Layer 2 harness for the seam.
- **Primitives.** P30 (heir transfer), TM05 (dynastic relay: spend on the heir or the present), P42 (a dead line).
- **Reads / writes.** Reads `hold`, `oblige`, `commit`, `successions`. Writes nothing; the hash moves only through what the successor
  then chooses.
- **Joins.** IN-61 (the `successions` registry and the heir's `succeed`, after CP-T02-01/02). T08: holdings pass by `succeed` and by
  refill, never by this Query. IN-47: the successor is "a person the builder already seated", creation arm C1's fallback. Births stay
  set aside (ED-WR-0011 Option A): every successor is an existing person.
- **Decision handed to the chooser.** While alive: whom to make your successor — confer the heir title, take oaths, gather followers
  (TM05's choice, spent now for later). At death: which of them to continue as. Unwatched: none — the NPC line goes on through IN-61
  and refill, not control.
- **Falsifier.** A seated person dies with one sworn retainer alive: the client continues as him, and a season run with the callback
  re-bound equals the run where that retainer was seated from the start of the next season → else the re-bind leaks state. A person with
  no ties dies: `continuations` was `()` at its last reading.
- **Control.** `auto` behind the callback before and after the re-bind reproduces the shipped hash (the seam's own control,
  `test_play_surface_dispatch.py`).
- **Hash.** Equal (a read; the seam is the shipped one). **Revert:** delete the Query and the roster.
- **Size.** S (M if AQ-T02-1 picks the widest roster and needs a fourth tie).

### CP-T02-07 · The seated person sees every question, in order

- **Adds.** The `View` DELIBERATE builds carries the full `questions_for` list in `attention_key` order, not only `question_aggregation_rule`'s
  pick. `auto` reads the first, so the shipped run is byte-identical; a callback may build a View on any listed question and ask `auto`
  for its proposal there (the GK2 advisor shape, D_T02:#GK4). Standing occasions stay on `out[0]` as today.
- **Owner.** `decision/questions.py` (the View's builder) and the `View` value object `[UNVERIFIED: whether `View` is ruled in `04`
  §B.9; a layer-conformance read is owed before adoption]`. Layer 2.
- **Primitives.** EN V.2's offer-all selection function for the player, weighted-salience for everyone else (D_T02:#E5b); KD7's concerns.
- **Reads / writes.** Reads what Q1-Q4 already compute. Writes nothing; not world state.
- **Joins.** None required.
- **Decision handed to the chooser.** The seated person decides what to attend to this round (the throne, the cause, the rival), not
  only how to answer the engine's pick. Unwatched: unchanged.
- **Falsifier.** A callback that always picks the first question reproduces the shipped hash; one that picks the second moves it.
- **Control.** That pair is the control.
- **Hash.** Equal. **Revert:** the View carries one question again.
- **Size.** S.

### CP-T02-08 · The Act interface shows the true odds of a contested act (a caller of T01's odds)

- **Adds.** No odds function. T01 owns the one odds reader (R1; CP-T01-03: `band_odds`, `odds_of(w, act)`, `estimated_odds(p, c)`). This
  item is the Act interface's contract for it: for each contested or graded candidate a seated person is offered, the client shows
  `odds_of(w, act)` — the TRUE odds of the act as it would resolve, built from the same `SocialContestInput` the roll reads. That is
  AX-7's reading: "No state is hidden from the player" binds the character, not the player (`architecture/meta/01_AXIOMS.md:299-304`).
  The callback itself receives no World (T-f; `play_surface.py`'s docstring), so the true odds come through a closure the client holds
  over its own World — "what a callback closes over is the client's own" (`play_surface.py:16-18`) — not through `choose`'s arguments.
  The draft's person-side `believed_degree_odds` is **withdrawn**: it would have been a second odds function, and it claimed to reuse
  `contest_input`, which takes the World (`seam/wrappers/sigma.py:149-151`) and cannot be called person-side.
  **The NPC half is not this item's.** An NPC chooses on believed inputs only (AX-2), which is T01's `estimated_odds`; no claim carries
  another person's capability, so for a person-opposed act (`tell`'s counterparty is the hearer's standing, `es/verb_table.yaml:1269`)
  the believed opponent factor is `None`, and no number is shown for it. Whether expected success enters the NPC score at all is T01's
  consolidated ask **AQ-X1** (cited, not re-asked); the score's shape is ruled (`architecture/ARCHITECTURE_V2.md:508-528`).
  **Effort** (T01 CP-T01-05: an act filling `1 + e` interaction slots) is not carried here: T01 states the rule and owns the edit to
  `decision/choose.py::pack_scenes`, and DELIBERATE's existing bounds refuse a scene over `interactions_per_scene`.
- **Owner.** T01's `odds_of` (`seam/wrappers/sigma.py`); the client's display; nothing in `engine/season/decision/`. Layer 2 (the reader)
  and the client.
- **Primitives.** P23 with shown odds (throughline 2: exact, not bent).
- **Reads / writes.** Reads what `odds_of` reads. Writes nothing.
- **Joins.** T01: `odds_of(w, act)` exact over `degree_from_net`. T03 and T04: the true-odds reader per prize ("the body", "a field"),
  or an explicit `None` until one exists; until then combat and field candidates show no odds.
- **Decision handed to the chooser.** Whether a contested act is worth the scene, seeing what it will actually face. Unwatched: none.
- **Falsifier.** For a hand-built `tell` the number shown equals the band frequencies of 10^5 seeded rolls of the real resolver on the
  same act within sampling error; a display fed by the Gaussian stand-in (`sigma_leverage.p_success`, which understates
  Partial-or-better by 10-15 points, overview §6 #13) fails the same test, so the test can fail.
- **Control.** That pair.
- **Hash.** Equal (a read). **Revert:** the client stops calling it.
- **Size.** S, after T01's `odds_of`.

**Write matrix (all items).** New writes: CP-T02-01 adds Events (no new field); CP-T02-02 changes world-gen ids. Every other item
writes nothing. New closed sets: `goal_object_kinds.aim` (a column on an existing roster), `continuation_ties` (new). New Queries:
`aim_state`, `oughts_named`, `continuations`; no new odds reader (CP-T02-08 calls T01's). Deleted at adoption: `Proposition.scope`'s
seeding map once CP-T02-02 makes it the identity (its owner's call). The asymmetry hazard (`CLAUDE.md` §0.1 pt 1): no item changes a
getter whose setters write another source; CP-T02-02 changes an id at construction, so its sweep is over the `Office(` assignments.

## §3 NERS

Method: `skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06. Each N-line is attacked by assuming the item gone and naming the carrier
of each step.

| item | N-line | attack, and verdict |
|---|---|---|
| CP-T02-01 | cut it and **no one ever learns a seat fell empty by death**, so no succession, refill or seizure is a choice anyone faces | Attack: `vacancies` stamps vacant seats — but only for a `confer` grantee and never an `inheritance` throne (`world_q.py::vacancies`, H-230 (1)); `seats_named` needs a claim, and none exists. No carrier. **N holds** (all directions: down to persons, up to factions and endings, lateral to T08) |
| CP-T02-02 | cut it and **the heir rule cannot name the realm's throne** | Attack: IN-61's revert resolves `successions` through the census map at world-gen. That carrier exists (`Proposition.scope`'s precedent). **N holds, narrowed**: the loss is one route of two; the item is the simpler one (an id, not a second map). Kept as the default, the revert named |
| CP-T02-03 | cut it and **an aim can neither be met nor lost**: members of a faction whose throne is empty never face it | Attack: disqualifier 1 (carrier exists?) — `goal_referents` follows a succession and a vacant throne "names nobody" (`world_q.py:1996-1997`), which is the defect, not a carrier. The −1 `seat_holders` row WAS carried by that same `()` (`:2031-2037, :2618`): a **false N-line, cut**; the drafted `spent` state is cut by AX-6 clause 3; disqualifier 4 (second thumb?) — it adds no score term. **N holds** (top-down: faction goal → members; bottom-up: a person's death → the faction's attention; lateral: legitimacy may read it) |
| CP-T02-04 | cut it and **no superior is ever confronted with a subordinate's success or failure** | Attack: tier 1 already admits claims about persons inside a seat's purview (IN-57). But no claim reports an aim's state; a vacancy is not a failure of the holder. Disqualifier 2 (producer): the removal act is `revoke`, reachable by one seat today. **N holds, narrowed**: the occasion is real, the consequence is T08's; until T08 widens `revoke` it yields mostly refusals. Kept, ordered after T08 (§5) |
| CP-T02-05 | cut it and **no one joins a cause he hears of** | Attack: `commit` already forms on one's own uttered Proposition (IN-11's maker's hold); REM-21 (iv) stamps a question's *own* Proposition referents. Is the second a carrier? Only where the question is about the Proposition, which a `proposition.uttered` claim is not (its subject is the actor, T-d's note, `01_AXIOMS.md:396-402`) `[UNVERIFIED for every Proposition-naming claim kind]`. **N holds, narrowed** to "causes heard of but not the subject of the current question"; if REM-21 (iv) is shown to carry them, this item is a **false N-line** and is cut — the falsifier in §2 tests exactly that |
| CP-T02-06 | cut it and **a seated player's game ends at the first death with no rule**, against CK2, GK2, Old World (D_T02:#GK5, #A9) | Attack: `overrides` can already be re-keyed by hand; the missing piece is which persons may be chosen, a game fact (a roster) that must not live in a client. **N holds, narrowed** to the player half (R-PLAYER); R-WORLD is IN-61's. Disqualifier 2 holds for tie (3) only while utterances by named persons are rare |
| CP-T02-07 | cut it and **the seated person can answer only the question the engine picked** | Attack: a callback can already return any act on any id (DELIBERATE checks budget, bound and actor only). But it cannot know the other questions without reading the World, which the seam forbids. **N holds, narrowed** (player only) |
| CP-T02-08 | cut it and **the player chooses contested acts blind** | Attack: disqualifier 1 — T01's `odds_of` is the carrier; is this item anything beyond it? Only the contract that the Act interface shows the TRUE number (AX-7) and not the believed one. **N holds, narrowed** to that contract; it adds no function (the drafted second odds function was cut as a duplicate of T01's) |

**False N-lines found:** one — CP-T02-03's −1 `seat_holders` row (cut); CP-T02-08's drafted odds function was a duplicate of T01's (cut to a contract); CP-T02-05 is conditional and its own falsifier decides it. **Cuts proposed:** (i) CP-T02-04's
"met" half could be cut, leaving only "breached" (removal) — what dies is the promotion occasion (TM12's step), which no other
carrier offers; kept. (ii) CP-T02-03's `rung` row could be cut (4 authored rung goals) — what dies is the Katepano's "presses on the
capital" ever being met; kept, it is one row. (iii) CP-T02-02 could be replaced by its revert; kept as default, revert named.

**R.** R-WORLD gains in CP-T02-01, -03, -05 (succession scrambles, factions turning on an empty throne, causes spreading) with no
player present. R-PLAYER gains in -06, -07, -08 and the menu half of -05. No item creates a dominant option: each hands a choice to a
person and resolves nothing itself. Residual: if the chronicle channel is deleted (H-214 holds it), CP-T02-01's reach shrinks to those
present at the death, and -03's `breached` question is then the only route by which the Crown faces its throne.

**S.** S-UP: a death (person) → seat (office) → faction aim (faction) → ending (`theocracy` needs a live King post, `_ending_edges`)
— the chain is continuous after CP-T02-01/02/03 + IN-61. S-DOWN: a faction goal's state reaches each member's question (Q4) without a
faction acting (T-h). Lateral: CP-T02-04 hands T08 its occasion; -05 hands T09 recruitment. Pauses correctly: nothing here pauses;
IN-46 owns the one suspension. Calculations consistent: every new read is a Query over live edges, the shape of `vacancies`,
`seats_named` and `endings_reached`; no second ladder. **One S risk named:** CP-T02-03 and `endings_reached` both test "is this seat
held by this org"; the `rung` row must call `governing_hold` and `faction_holding`, the endings' own readers, not a copy.

**E (last, as a ratio).** Objects added: 3 Queries, 1 roster, 1 roster column, 1 stamper registration, 1 Event
emission site; objects removed: 0 now, 1 at adoption (the seeding map). Verbs added 0; Events kinds added 0; fields added 0. The
vocabulary gains two words (`aim state`, `continuation`), each defined where it is invoked. Against N: every item
holds an N-line, four narrowed; the E ratio is acceptable for -01, -03, -05 (one Query each, large R-WORLD gain), thin for -08 until
J-T1 (one module for a constant today). By the meta-rule, -02 is the only one that is mostly a deletion (a map becomes the identity);
the others add a read, none adds a store, gauge or guard.

## §4 One season, after

Seed 0, tick 0 and 1, the realm with every item built and IN-61 landed. Event order and the King's death are the control run's
(overview §5.2: at tick 0 the King `p_npc_020` is Wounded to body 450 by `p_npc_006` and Felled the same tick by `p_npc_032`'s
`accept`). Everything after the death is **illustrative**: no code produces it yet.

1. **The seated person.** A client seats the Prince, `p_npc_031`, holder of the heir seat (`off_heir` under CP-T02-02; `off_npc_031`
   today, H-230). His `continuations` at build (CP-T02-06): no seat of his has a `successions` row, so (1) is empty; (2) and (3)
   depend on oaths and followers he has none of — `()`. His line ends with him unless he acts (illustrative).
2. **Round 0, tick 0.** The Queen's `accept` fells the King in the contested_physical stratum. CP-T02-01: the death earns
   `tenure.closed` on the King's hold on `off_king`, chronicled to everyone alive. The Prince was not present; the hearsay claim reaches
   him anyway.
3. **Round 1.** CP-T02-07: the Prince's View lists his questions: the throne (stamped by `seats_named`, an Office), the Crown's breached
   goal (CP-T02-03: `goal_crown_peninsular_sovereignty` now names `off_king` itself), and a tier-0 claim about the Queen, the doer of
   the deed. CP-T02-08 shows no odds for `succeed` (not contested); for a `tell` the client would show T01's `odds_of` for that act, which no code produces yet, so no number is given here. He picks the
   throne and `succeed` (IN-61's claim); the gate admits it because he holds the heir title and the throne has no live hold. He holds
   the throne; his budget rises by one (a seat with grants; IN-14's count).
4. **Unwatched, the same rounds.** Every other Crown member's breached aim also names the throne; the Widow Regent cannot `confer` it
   (`may_fill` refuses `inheritance`, IN-61 (3)) and her routes are the tribunal or force. Church members' `theocracy` row
   (`rosters.yaml: endings`) is reachable again because a King post is held — by a Crown man, so not met. The Church's
   `goal_church_suppress_restoration` (`seat_holders` −1, `goals.yaml:230-234`) already forms no question once Yrsa's seat is vacant
   (`world_q.py:2031-2037`), today as after; this proposal changes nothing there.
5. **Tick 1.** The Prince now holds the throne; CP-T02-06's reading lists the persons sworn to it (the throne's `obligees:` is NPC-070, the
   Grand Master, `offices.yaml:191`). He spends a scene on `confer` of the heir title to one of them — the TM05 choice, buying a
   successor with a scene now. A witness who saw a Restoration member `utter` an OUGHT may `commit` to it (CP-T02-05); a movement
   grows by being seen.

Numbers the code can produce today: the King's death, its tick and its killer (control run). Everything else in this section is
illustrative until the items and IN-61 exist.

## §5 Order and dependencies

**Within this proposal:** CP-T02-01 → CP-T02-03 (its `breached` question is most useful once deaths name seats, though it does not need
it) → CP-T02-04. CP-T02-02 beside CP-T02-01; both before IN-61's build. CP-T02-05 after REM-21 and REM-23. CP-T02-06 after IN-61
(tie 1) — ties 2 and 3 can land first. CP-T02-07 and CP-T02-08 are independent; CP-T02-08 after T01's function.

**Batch placement (proposed):** CP-T02-01 and -02 ride the batch that unblocks IN-61 (IN-61's BATCH line: "rides the first batch that
gives the heir a claim naming a vacated seat … and a row-id to realm-seat map"); CP-T02-03 and -04 share `queries/world_q.py` with B-U's
successors and IN-30, so serial with them (`_part3` §C.2); CP-T02-05 in RB-2a beside REM-23 (same rows); CP-T02-06…-08 with RB-3a
(IN-47, the seated person's build), which already touches the play surface.

**What this needs from other subsystems (interface as I expect it):**
- **T01 resolution:** `odds_of(w, act)` (CP-T01-03), the true odds, exact over `degree_from_net`, one owner (R1); AQ-X1 for any score use.
- **T03 personal combat / T04 mass battle:** a true-odds reader per prize, through T01's function, or an explicit `None`; T03's actor write (verbs-09 M1),
  so a death's doer and a duel's loser are both recorded.
- **T08 governance:** `revoke` reachable by a superior over a sworn subordinate's seat; refill of vacated seats through `vacancies` and
  `may_fill` (the gate stays T08's). The death-write broadcast and the seat ids are this file's (R4): T08's CP-T08-09 (1)(2) cite
  CP-T02-01/-02, its loader rule (3) moves into IN-61, and the `off_npc_084` row is IN-61's. T10's estate route is its own and
  non-broadcast; it does not share CP-T02-01's change.
- **T09 factions:** which goals exist and their `stance:`; whether a second live membership is admitted; `conspire` (Γ22).
- **T05 social contest:** `argue` on a heard-of Proposition as its venue (CP-T02-05).

**What this gives them:** `aim_state` (T09's war aims, B-U's legitimacy input, T08's removal occasion); vacated seats as public claims
(T08, T09); a person's continuation set (IN-47's seated player); the Act-interface odds contract (every contested subsystem's player surface).

## §6 Jordan asks, and the rulings the items touch

**AQ-T02-1 · Which ties carry a seated player's line past his death?**
- **Options.** (a) **Heir title only** (`heir_title`): CK3-strict; most persons have no heir seat, so most seated games end at the first
  death unless the player confers one. (b) **Title, then oath** (`heir_title`, `sworn`): continuation through retainers; the throne's
  obligees keep a royal game alive. (c) **Title, oath, then followers** (all three): continuation through anyone committed to a cause the
  dead uttered; a seated game almost never ends.
- **Consequence.** (a) makes death the game's main risk and the heir the main investment (TM05 at full strength). (c) makes death a
  change of body, closer to Bannerlord's clan than CK3's dynasty. They are materially different games.
- **Ladder.** 1: not superseded (RS-27/RS-29 rule the throne's heir is a title, not who a player continues as). 2: not irrelevant
  (IN-47 seats a player; D-2 ruled yes). 3: no design document states it (IN-47's creation and development spaces do not reach death).
  4: IN-61's single-title line is precedent for the throne only. 5: the architecture cannot choose how forgiving death is.
- **Recommendation.** (b): it uses the one ratified superior relation (`oblige`, `01_AXIOMS` §E.1.5) and keeps the heir title primary.
  **Unblocks:** CP-T02-06's roster.

**Asks not raised (one line each):**
- Make the conviction crisis a choice rather than a rule — step 1: ED-IN-0261 (Jordan, 2026-10-06) ruled the engine chooses per case.
- Births or children as heirs — step 1: ED-WR-0011 Option A (closed cast "for now").
- A per-controller ending row in `rosters.yaml: endings` — step 5: the roster is about the realm; a controller's end is the client's.
- A goal term or risk term in the score — step 3: the score shape is ruled Layer 1 (`ARCHITECTURE_V2.md:510-525`); D-V6 and D05 are
  already held.
- Whether `aim_state` may read the World for `seat_holders` — step 4: follows ED-IN-0292 (2), already pending; not duplicated.
- An `Office.row` field instead of authored ids (CP-T02-02) — step 3: `04` §B.7's seat fields are Jordan's (A-29); the id route needs no
  ruling.
- Age reducing the budget (GK2) — step 1: #457 D2, delegated; JQ-3 holds the rates.
- JQ-1…JQ-6 of the remediation are referenced, not repeated (JQ-1 τ; JQ-2 per-person inputs; JQ-3 shift magnitudes; JQ-5 IN-46/47
  ratification; JQ-6 hunger).

**Rulings the items touch:** RS-27 / RS-29 (the heir is a title; CP-T02-01/02 make it reachable, change nothing in it); A-31 (a goal
never acts — CP-T02-03 keeps that: the Query changes questions only); A-32 (who holds a goal by his seat — CP-T02-04 reads it); D-2
(IN-46/47 build — CP-T02-06…-08 extend IN-47's development space); ED-WR-0011 (closed cast — CP-T02-06 works inside it); the scene unit
(Jordan 2026-09-02) and IN-14's delegated shape (budget untouched here).

## §7 Risks, and what this deliberately does not do

**Risks.**
- **Cross-formation cost.** CP-T02-01 makes every vacated seat a claim in every ledger; `seats_named` then stamps it on everyone's first
  question, and `confer`/`oblige` form on it and mostly refuse (the scene tax H-203 already records). Measure formed-and-refused
  counts on the throne at the batch's close; if it crowds out other acts, the stamp narrows to persons holding a `confer` grant or a
  `successions` title (`vacancies`' own narrowing), not the Event.
- **Chronicle deletion (H-214).** If held deletion lands, CP-T02-01's reach falls to those present.
- **Id churn (CP-T02-02).** Every pin naming an `off_npc_*` id moves; the revert is a second map, not a rollback of IN-61.
- **CP-T02-05 may be false.** If REM-21's own-referent stamp already carries heard-of Propositions, the item is cut (§3).
- **CP-T02-08 waits on T01's `odds_of`**, and on T03/T04 for combat and field; until then the interface shows no odds rather than a stand-in.
- **`aim_state` is a World read for `seat_holders`** and inherits ED-IN-0292 (2)'s answer.

**Deliberately not done.** No new verb, tenure kind, Event field, stored gauge or guard. No score term (the chooser-consequence items are
D-V6, D05, JQ-1, JQ-3, H-194 — held elsewhere; expected success in the score is T01's AQ-X1). No odds function (T01's). No
`pack_scenes` effort slot count (T01 CP-T01-05 owns it). No attribute block (J-T1). No budget change (IN-14). No ending row and no legitimacy
Query (IN-27, IN-23; B-U). No births (ED-WR-0011). No scheme carrier (T09's `conspire`). No screens: every item is an input to, or a read
for, the Act interface.
