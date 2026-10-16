# The character template — part 2: §3A, the idealized master verb table and the verb × axis matrix

## Status: PROPOSED (2026-10-16). Not ratified; merge ratifies nothing unless Jordan so rules.
## Parts, in reading order: [head](2026-10-16-character-template.md) (§0–§3) · **this file** (§3A) · [`_part3`](2026-10-16-character-template_part3.md) (§4–§10).

**What this part is for.** Jordan: *"cross reference against a master verb table that is idealized as
if fully designed and built."* The question it answers is which capacity axes the verbs, taken
together, would read if every system were complete. The head's §3 folds the result into the axes and
into Options A and B. This part holds the evidence.

**Discipline.** No verb is invented. Every row names a source that was opened, and the tier tags are
the head's (T1 loop code, T2 stub code, T3 ratified spec or v9 position, T4 design intent). In the
"axis read" column, *today* is T1 only. *When complete* is what a named T2–T4 source says the verb
would read. Where no source names a capacity, the cell says **none named**. An empty cell is not a
claim that the verb needs no capacity. It says only that nothing in the tree says it does.

**How the shipped rows were counted.** `grep -c '^  - verb:' engine/season/verb_table.yaml` → `45`.
Every shipped row's line below is that grep's own `-n` output, and every one was read off it.

**The axis codes.** These are the registry's nine (`references/descriptor_registry.yaml:36-48`)
[CHECKED], each with the alias the stub code spells:

- **STR** Strength.
- **AGI** Agility.
- **END** Endurance.
- **FOC** Focus.
- **ACU** Acuity (code: `cog`, Cognition).
- **WIL** Will (code: `spirit`).
- **ATT** Attunement (code: `att`).
- **CHA** Charisma.
- **BON** Bonds.

Plus four codes that are not on the registry:

- **PRA** practice, or "History", per domain: what training writes.
- **TS** Thread Sensitivity (`descriptor_registry.yaml` `practitioner_stats`).
- **TMP** temperament (combat `disp`).
- **KIT** what a person carries.

**OFF** (office) and **BODY** (condition) are named where a verb reads them. They are not capacity
axes: office is a Tenure and body is live state (§3.3 of the head).

---

## A.1 Status classes, counted

| status class | rows | how counted |
|---|---|---|
| **SHIPPED** (`verb_table.yaml`) | **45** | the grep above |
| **PLANNED** in v9 | **16** | IN-12 steps 6, 7, 9, 10, 13, 5, 5a, 11 name 13 verbs (`workplans/valoria_master_workplan_v9_part5.md:71-78`) [CHECKED]: `seize`, `covenant`, `sabotage`, `tend`, `argue`, `train`, `conceal`, `forgive`, `arrest`, `pardon`, `interrogate`, the charge, `raze`; plus PC-10's `yield` (`_part7.md:58`) [CHECKED]; plus IN-46's player choices `engage` and `withdraw`, an [ASSUMPTION] in the plan (`_part4.md:34`) [CHECKED] |
| **STUBBED** (code outside the season loop) | **19** | 7 thread operations (`systems/threadwork/sim/operations.py:351, :375, :388, :397, :417, :434, :512`) [CHECKED]; 7 contest move kinds (`systems/social_contest/sim/contest/resolver.py:34`) [CHECKED]; `form_knot` (`systems/fieldwork/sim/knots.py:173`) [CHECKED]; 4 mass-battle orders, namely rally (`modules/mass_battle/orchestration.py:288`), recall (`:2585`), charge (`modules/mass_battle/resolution.py:176`) and brace (`:132`) [CHECKED: the defs] |
| **DESIGN-ONLY / lane recommendation** | **3** | `levy` raising troops (`proposals/2026-10-16-troop-stock-design.md:444`, §3.1; K-MB-1, `research/by_lane/MB_mass_battle.md:715`) [CHECKED]; a spoken lie (K-SC-6, `research/by_lane/SC_social_contest.md:710`) [CHECKED]; resigning one's own seat (K-FA-3, `research/by_lane/FA_faction_actions.md:582`) [CHECKED] |
| **total** | **83** | |

**Not counted as verbs, deliberately.** Three groups stay out of the count:

- The personal-combat bout's internal terms (reading, reflex, bind, counter, initiative). They are
  resolver mechanics inside one `fight`, not acts a person chooses in a season. They appear in §A.4
  as the combination `fight` uses.
- `practice`. It is SUPERSEDED by `train` (`_part7.md:51`) [CHECKED], so counting it would
  double-count one verb.
- The thread operations' lane recommendation (K-WR-2, `research/by_lane/WR_world.md:538`)
  [CHECKED]. It is carried as the lane reference on the 7 STUBBED thread rows, not as rows of its
  own.

---

## A.2 The table

### A.2.1 SHIPPED (45)

The lane is the tree's subsystem lane. `reads today` is T1. Every row also reads BODY indirectly,
through the scene budget (`engine/season/decision/budget.py:57-61`) [CHECKED]. That is one shared
cost, not per verb, so it is not repeated in the rows.

| # | verb (`verb_table.yaml` line) | lane | reads today | reads when complete (source, tier) | target quantity | outcome the capacity would move | lane ref |
|---|---|---|---|---|---|---|---|
| 1 | `carry` :105 | SC | none | none named | docket matter | — | — |
| 2 | `commit` :123 | FA | none | none named | a Proposition | — | — |
| 3 | `comply` :139 | IN | none | none named | — | — | — |
| 4 | `confer` :163 | FA | OFF (the seat exercised, via `Act.via`) | none named | a seat's tenure | OPTIONS (office) | — |
| 5 | `convene` :183 | SC | none | none named | a date | — | — |
| 6 | `create_record` :194 | FI | none | none named | `Record.exists` | — | — |
| 7 | `destroy_record` :205 | FI | none | none named | `Record.exists` | — | — |
| 8 | `determine` :217 | SC | OFF | none named | a docket matter | OPTIONS | — |
| 9 | `dispatch` :263 | IN | OFF | none named | — | OPTIONS | — |
| 10 | `establish` :278 | FA | OFF | none named | `Office.remit_acts` | OPTIONS | — |
| 11 | `evade / defy` :292 | IN | none | none named | — | — | — |
| 12 | `exchange` :307 | SE | none | none named | `Rung.stores` | — | K-SE-4 |
| 13 | `forge` :325 | FI | none | **open**: the row writes `Record.forgery_quality`, and no source says what sets its value | `Record.forgery_quality` | EFFECT (how good the forgery is), if a source rules one | M-FI-2 |
| 14 | `found` :354 | SE | none | none named | `Rung.exists` | — | — |
| 15 | `build` :377 | SE | none | none named | `Site.exists` | — | — |
| 16 | `give` :400 | IN | none | none named | a tenure | — | — |
| 17 | `issue` :428 | FA | OFF | none named | `Record.exists` | OPTIONS | K-FA-12 |
| 18 | `fight` :475 | PC | BODY → `end` (`seam/wrappers/combat.py:130-138`) [CHECKED] | STR AGI END ACU FOC WIL ATT PRA TMP KIT: every `Combatant` field (`modules/combat/combatant.py:93-94`) [CHECKED] (T2) | the opponent's body | ODDS · EFFECT · COST (wounds) | M-PC-1, K-PC-1 |
| 19 | `challenge` :579 | PC | none | none named | — | — | — |
| 20 | `accept` :600 | PC | as `fight` | as `fight` (T2) | as `fight` | as `fight` | M-PC-1 |
| 21 | `requisition` :629 | SE | OFF | none named | `Rung.stores` | OPTIONS | K-SE-5 |
| 22 | `march` :664 | MB | the side's `weight` and stance (`seam/wrappers/mass_battle.py:175-200`) [CHECKED]: no person capacity | the commander's CHA and ACU through `Officer` → `derive_command` (`modules/mass_battle/hierarchy/units.py:2700-2722`; `modules/mass_battle/core/exchange.py:57-66`) [CHECKED] (T2); the troop design routes it (`troop-stock-design_part2.md:71-79`) [CHECKED] (T4) | the field | ODDS (exchange pool `2 × command`, `exchange.py:69-75`) · OPTIONS (span of command) | M-MB-3, K-MB-2, M-NPC-13 |
| 23 | `migrate` :698 | SE | none | none named | residence | — | — |
| 24 | `move` :720 | IN | none | none named | presence | — | — |
| 25 | `oblige` :735 | FA | none | none named | a tenure | — | — |
| 26 | `open_case` :757 | SC | none | none named | a case | — | — |
| 27 | `petition` :782 | SC | none | none named | a Record | — | K-SC-3 |
| 28 | `construe` :806 | SC | none | none named | — | — | — |
| 29 | `release` :822 | FA | none | none named | a tenure's end | — | — |
| 30 | `restore` :839 | SE | none | none named | `Site.condition` | — | K-WR-3 |
| 31 | `revoke` :861 | FA | OFF | none named | a tenure's end | OPTIONS | — |
| 32 | `speak` :875 | SC | PRA (`copying`, `rosters.yaml:1106-1107`); not contested, so the pool is not rolled today | PRA as the contest faculty, CHA as the Face ceiling (`resolver.py:184-195`, `:300`; `primitives.py:138-142`) [CHECKED] (T2) | a hearer's standing | ODDS | M-SC rows, K-SC-2 |
| 33 | `succeed` :886 | FA | none | none named | a seat | — | — |
| 34 | `survey` :917 | FI | none | none named | `Record.exists` | — | — |
| 35 | `tell` :936 | SC | PRA, as an opposed pair: the actor's key → pool, the hearer's same key ÷ 2 → Ob (`sigma.py:97-129`) [CHECKED] | as `speak` (T2) | the hearer's standing | ODDS | K-SC-2, M-NPC-1 |
| 36 | `examine` :1083 | FI | none | competence: AX-7 rules that divergence turns on *"the channel …, the reader's competence, and their prior beliefs"* (`architecture/meta/01_AXIOMS.md:288-289`) [CHECKED] (T3). The competence factor is 1 and unbuilt (`decision/options.py:1205-1209`; H-200) [CHECKED]. **Which axis competence is, is open** | a finding's fidelity | MEMORY (how true what he holds is) | M-FI-3, K-FI-1 |
| 37 | `interview` :1105 | FI | none | as `examine` | as `examine` | MEMORY | K-FI-1 |
| 38 | `research` :1121 | FI | none | as `examine` | as `examine` | MEMORY | K-FI-1 |
| 39 | `surveil` :1137 | FI | none | as `examine` | as `examine` | MEMORY | K-FI-1 |
| 40 | `thread_read` :1157 | FI/WR | none | TS as its precondition: K-3, *"type `thread_read`'s precondition on TS"* (`proposals/2026-09-30-character-and-play-surface/09_the_character_sheet.md:130`) [CHECKED] (T4, ratified as intent by v9) | — | OPTIONS (who can attempt it) | K-3 |
| 41 | `reconstruct` :1171 | FI | none | as `examine` | as `examine` | MEMORY | K-FI-1 |
| 42 | `tie / knot` :1186 | IN | none (H-182: the row has no effect) | BON as a gate, and a disposition toward the other party as a second gate (`systems/fieldwork/sim/knots.py:185-192`) [CHECKED] (T2) | a tie | OPTIONS | M-NPC rows |
| 43 | `transfer` :1198 | SE | none | none named | `Rung.stores` | — | — |
| 44 | `utter` :1218 | IN | none | none named | a Proposition | — | K-FA-1 |
| 45 | `work` :1229 | SE | none | none named | `Site.condition` | — | M-SE-5 |

### A.2.2 PLANNED in v9 (16)

| # | verb | lane · position | reads when complete (source) | target | outcome | lane ref |
|---|---|---|---|---|---|---|
| 46 | `seize` | IN · IN-12 step 6 (`_part5.md:71`) | none named | a warrant, then a rung hold | — | — |
| 47 | `covenant` | FA · step 7 (`:72`) | none named | a dispensation | — | K-FA-2 |
| 48 | `sabotage` | SE · step 9 (`:73`) | none named | `Site.condition` | — | — |
| 49 | `tend` | SE · step 9 (`:73`) | none named. The row writes `Person.body` up | `Person.body` | — | — |
| 50 | `argue` | SC · step 9 (`:73`) | none named. The row writes `Person.pursuits` | the hearer's pursuits | **open**: a persuasion that moves values is a natural PRA or CHA reader, but no source says so | — |
| 51 | `train` | IN · step 9 (`:73`) | **a writer, not a reader**: *"`train` forms and writes `Person.capability` only where a case names a vocation"* | `Person.capability` (PRA) | raises PRA | M-NPC-1, H-NPC-1 |
| 52 | `conceal` | IN · step 10 (`:74`) | none named | witness keys | — | — |
| 53 | `forgive` | SC · step 13 (`:75`) | none named | stance | — | — |
| 54 | `arrest` | SC · step 5 (`:76`) | none named | `detain` | — | — |
| 55 | `pardon` | SC · step 5 (`:76`) | none named | `detain`, `ban` | — | — |
| 56 | `interrogate` | SC · step 5 (`:76`) | none named. An inquiry under coercion is a natural competence reader (AX-7, as `examine`), **open** | testimony | MEMORY (if competence lands) | M-FI-3 |
| 57 | the charge | SC · step 5a (`:77`) | none named | a petition's terms | — | K-SC-4 |
| 58 | `raze` | MB · step 11 (`:78`) | none named | `w.rungs` | — | — |
| 59 | `yield` | PC · PC-10 (`_part7.md:58`) | a stop rule under duel terms; no capacity named | the bout | — | — |
| 60 | `engage` | PC · IN-46 (`_part4.md:34`, [ASSUMPTION] in the plan) | none named | the bout | — | — |
| 61 | `withdraw` | PC · IN-46 (as above) | none named | the bout | — | — |

### A.2.3 STUBBED, code outside the loop (19)

| # | verb | lane | reads in the stub (source, T2) | target | outcome | lane ref |
|---|---|---|---|---|---|---|
| 62 | Leap `attempt_leap` (`operations.py:351`) | WR | the thread pool: WIL, TS, PRA (`operations.py:235-247`) [CHECKED]; Coherence cost resisted by `resilience` (`:269-274`) [CHECKED], whose gain ships 0 (`:157`) [CHECKED] | a target state | ODDS · COST | M-WR-1, K-WR-2 |
| 63 | Weaving `attempt_weaving` (`:375`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 64 | Pulling `attempt_pulling` (`:388`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 65 | Past-pulling `attempt_past_pulling` (`:397`) | WR | as Leap | a past moment | ODDS · COST | K-WR-2 |
| 66 | Locking `attempt_locking` (`:417`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 67 | Dissolution `attempt_dissolution` (`:434`) | WR | as Leap | a thread | ODDS · COST | K-WR-2 |
| 68 | Mending `attempt_mending` (`:512`) | WR | as Leap | a configuration | ODDS · COST | K-WR-2, K-WR-3 |
| 69 | contest move `advance` (`resolver.py:34`) | SC | PRA as `faculty` → `Pool.size(faculty)` and `Leverage.net(faculty)` (`resolver.py:300-301`) [CHECKED] | standing | ODDS | K-SC-2 |
| 70 | contest move `hard` (`:34`) | SC | as `advance` | standing | ODDS | K-SC-2 |
| 71 | contest move `shift` (`:34`) | SC | as `advance` | standing | ODDS | K-SC-2 |
| 72 | contest move `support` (`:34`) | SC | as `advance` | standing | ODDS | K-SC-2 |
| 73 | contest move `pass` (`:34`) | SC | none: passing rolls nothing [UNVERIFIED: the move's body not opened] | — | — | — |
| 74 | contest move `evidence` (`:34`) | SC | the `Contestant`'s evidence items (`resolver.py:184-195`) [CHECKED]: kit, not capacity | standing | ODDS | K-SC-2 |
| 75 | contest move `rebut` (`:34`) | SC | as `advance` [UNVERIFIED: the move's body not opened] | standing | ODDS | K-SC-2 |
| 76 | `form_knot` (`knots.py:173`) | FI | BON ≥ `KNOT_BONDS_MIN` and a disposition toward the other ≥ its minimum (`knots.py:185-192`) [CHECKED] | a knot | OPTIONS | — |
| 77 | rally / reform (`orchestration.py:288`) | MB | the general's Command must be at least one above the unit's Discipline, and at least 2 (comment, `orchestration.py:298-300`) [CHECKED] → CHA, ACU through `derive_command` | a unit's Discipline | OPTIONS (gate) | M-MB-3 |
| 78 | recall (`orchestration.py:2585`) | MB | `roll_pool(pursuer.command)` against Ob 2 (`:2589`) [CHECKED] → CHA, ACU | a pursuing unit | ODDS | M-MB-3 |
| 79 | charge (`resolution.py:176`) | MB | unit state only (discipline, depth, morale; `resolution.py:179-184`) [CHECKED]: no person | the defender | ODDS | M-MB-2 |
| 80 | brace (`resolution.py:132`) | MB | unit state [UNVERIFIED: the body not opened] | the unit | ODDS | M-MB-2 |

### A.2.4 DESIGN-ONLY / lane recommendation (3)

| # | verb | lane | reads (source, T4) | target | outcome | lane ref |
|---|---|---|---|---|---|---|
| 81 | `levy` (raise a company) | MB/SE | OFF (the levying seat). The company's grade sits in its own `capability`, and the commander is the seat holder, not stored (`troop-stock-design.md:324-328`) [CHECKED]. **No actor capacity named** | a cohort's weight | OPTIONS | K-MB-1, K-SE-5 |
| 82 | a spoken lie | SC | an arm of `said_of`; no capacity named (K-SC-6) | what a teller passes on | MEMORY (what the hearer holds) | M-SC-7, K-SC-6 |
| 83 | resign one's own seat | FA | no capacity named (K-FA-3) | the seat | OPTIONS | M-FA-3, K-FA-3 |

---

## A.3 The verb × axis matrix

Only rows with at least one sourced axis appear. ● means the axis is read by a T2 stub or a T3
rule. ○ means the axis is read today (T1). ◐ means the source names the quantity but not which
axis it is (competence).

| verb (rows) | STR | AGI | END | FOC | ACU | WIL | ATT | CHA | BON | PRA | TS | TMP | KIT | axes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `fight`, `accept` (18, 20) | ● | ● | ● | ● | ● | ● | ● | | | ● | | ● | ● | 10 |
| `tell` (35) | | | | | | | | ● | | ○● | | | | 2 |
| `speak` (32) | | | | | | | | ● | | ○● | | | | 2 |
| `march` (22) | | | | | ● | | | ● | | | | | | 2 |
| rally, recall (77, 78) | | | | | ● | | | ● | | | | | | 2 |
| the 7 thread operations (62–68) | | | | | | ● | | | | ● | ● | | | 3 |
| `thread_read` (40) | | | | | | | | | | | ● | | | 1 |
| inquiry: `examine`, `interview`, `research`, `surveil`, `reconstruct` (36–39, 41) | | | | | ◐ | | ◐ | | | | | | | 1 (competence; axis open) |
| contest moves `advance`, `hard`, `shift`, `support`, `rebut` (69–72, 75) | | | | | | | | | | ● | | | | 1 |
| contest move `evidence` (74) | | | | | | | | | | | | | ● | 1 |
| `tie / knot` (42), `form_knot` (76) | | | | | | | | | ● | | | | | 1 |

`train` (51) is the PRA **writer** and reads no axis. CHA's Face ceiling is a bout-level term of
the contest, read once per bout, not per move. It is shown on `tell`/`speak` and not on the move
kinds.

**Verbs by number of axes read (when complete), and the counting rule.** One verb row counts once.
Competence counts as one axis, since its identity is open. KIT counts as an axis. OFF and BODY do
not.

| axes read | verbs | count |
|---|---|---|
| **3 or more** | `fight`, `accept`, and the 7 thread operations | **9** |
| **2** | `tell`, `speak`, `march`, rally, recall | **5** |
| **1** | 5 inquiry verbs, `thread_read`, 5 contest moves, `evidence`, `tie / knot`, `form_knot` | **14** |
| **0 named, or open** | the remaining rows: 33 shipped, all 16 planned, `pass`, charge, brace, all 3 design-only | **55** |
| total | | **83** |

**Axes no verb uses.** Every one of the nine registry axes has at least one verb row. The thin ones:

- **BON**: only `tie / knot` and `form_knot`, both gates.
- **FOC**: only `fight`/`accept`.
- **TMP**: only `fight`/`accept`.
- **TS**: only `thread_read` and the 7 thread operations.

**Recall**, the 2026-08-15 proposal's capacity (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:191`)
[CHECKED], is read by **no** verb row. Neither is any axis that would be "the tenth".

**Verbs that need no capacity.** Under the counting rule, 55 of 83 rows name none. That is a finding
about the SOURCES, not about the game. Two kinds sit in that 55:

- Most are office-, presence- or ownership-gated acts. Their OPTIONS turn on OFF or a held Tenure:
  `capability` *"supplies dice and GATES NOTHING"* (`options.py:478-479`) [CHECKED].
- A few are natural capacity readers that no source has yet tied to an axis. `forge`'s quality,
  `argue`, `interrogate` and the lie are marked **open**, not none.

---

## A.4 The multi-axis verbs: roles and how the axes combine

Jordan: *"some verbs may require multiple attributes."* For each verb reading two or more axes, this
table gives the role each axis plays and the combination as the source fixes it. The roles are:

- **ODDS**: pool, or dice.
- **DIFFICULTY**: Ob, or what stands against.
- **COST**: wounds, Coherence or stamina.
- **GATE**: eligibility.
- **EFFECT**: the size of what lands.

| verb | axes → role | combination as the source fixes it | fixed or open |
|---|---|---|---|
| `fight` / `accept` | PRA → ODDS: the resolution pool `max(5, history + 6)` (`modules/combat/core.py:54-56`) [CHECKED]. ACU, ATT, PRA → reading: `(2·cog + att)/3 + K·(history − 3)` (`combat_systems.py:171`) [CHECKED]. AGI, ATT → reflex, a weighted mean (`:172`) [CHECKED]. AGI → tempo (`:113`) [CHECKED]. AGI, STR → balance, `½agi + ½str − 1 + skill` (`:188`) [CHECKED]. END, WIL, STR → COST: wound interval and health, `wound_interval(end, spirit)`, `health_full(end, spirit, strength)` (`combatant.py:30-40`) [CHECKED: the defs]. FOC → poise recovery and disruption resistance (`combat_systems.py:1436`, `:1452`) [CHECKED]. TMP → an aggression lean `(disp − 4)/3` (`:183`) [CHECKED]. AGI, PRA → initiative (`:1419-1421`) [CHECKED]. KIT → weapon and armour vectors | **per-term weighted sums**, each term a separate channel of one bout. No single "fight score" exists | **fixed by the stub** (T2). Open on the season path: `fight.py:45` builds every field but `end` at the class default [CHECKED] |
| `tell` / `speak` | PRA → ODDS (pool); the hearer's PRA → DIFFICULTY (Ob = score ÷ 2) | **an opposed pair**: actor's key against the subject's same key, halved (`sigma.py:97-129`) [CHECKED]. When complete: PRA (as `faculty`) → pool and leverage (`resolver.py:300-301`); CHA → the Face ceiling `charisma × 3` (`primitives.py:138-142`) [CHECKED], a bout-level cap | today's pair: **fixed** (an `assumption`-graded mapping, H-126). Which season verb maps to which contest faculty, and whether CHA enters the season roll: **open** |
| `march` | CHA, ACU → ODDS (Command → the exchange pool) | **a weighted mean**, rounded and clamped 1–7: `derive_command(charisma, cognition)` (`exchange.py:57-66`); then `2 × command` (`:69-75`) [CHECKED] | **fixed by the stub** (T2); the season wiring is the troop design's (T4) |
| rally / recall | CHA, ACU (via Command) → GATE (rally) or ODDS (recall) | **one-then-other**: the attributes make Command once, and Command then gates or rolls | **fixed by the stub** (T2) |
| the 7 thread operations | WIL, PRA, TS → ODDS; `resilience` → COST | **a sum**: `spirit × 2 + min(3, history + 3) + ts // 10` (`operations.py:235-247`) [CHECKED]. Resilience subtracts from the Coherence cost, floored at 0 (`:269-274`) [CHECKED] | **fixed by the stub** (T2). Whether `resilience` is WIL, or a tenth axis, is **open** (the plan: *"'spirit' (resilience, R-14) is a candidate input only"*, `_part5.md:444`) [CHECKED] |
| `tie / knot`, `form_knot` | BON → GATE; disposition toward the other → GATE | **a conjunction of two gates** (`knots.py:185-192`) [CHECKED] | **fixed by the stub** (T2). The season row has no effect yet (H-182) |

### A.4.1 The roster tested against co-occurrence

Jordan's test: an axis pair that always co-occurs is a merge candidate; an axis used only alongside
another is a sub-term.

- **STR, AGI, END, FOC, ATT and TMP co-occur only in `fight`/`accept`** (ATT also enters reading).
  **At the VERB level, they are merge candidates.** Inside the bout they never merge, because each
  feeds a different term with a different role (impact and health; tempo, reflex and balance;
  wounds; poise; reading; aggression), and the stub keeps them separate. **The verb-level test cannot
  see inside a resolver**, and here it would recommend a cut the resolver contradicts. So "merge"
  stays a candidate, not a finding.
- **CHA and ACU co-occur in `march`, rally and recall, and only through `derive_command`.** But CHA
  also appears alone, as the Face ceiling (`tell`/`speak`), and ACU alone, in combat reading. So
  neither is a sub-term of the other.
- **WIL appears in combat (wounds, stamina) and in the thread pool.** It is not a sub-term.
- **TS appears only with WIL and PRA** (thread operations), or alone as a gate (`thread_read`). The
  registry already scales it differently (0–100, a practitioner stat), and nothing here argues for
  folding it into the nine.
- **BON appears alone, as a gate.** The 2026-08-15 proposal's class *"capacity (gate, never roll)"*
  (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:124-125`) [CHECKED] fits it.
- **PRA appears with everything**, and its key differs by verb: `copying`, the contest `faculty`,
  combat `history`, threadwork `history`. **It is not one axis but one axis per domain.** That is
  exactly why it cannot be one of the ten (§3.3 of the head).

### A.4.2 What each option does to a multi-axis verb

- **Option B (stored).** Each verb's resolver names its attribute inputs and fixes their combination
  in its own module. The stubs already do this: `derive_command(charisma, cognition)`, the thread
  pool's sum, the combat terms. The template supplies the attributes; the verb, not the template,
  owns the combination. So a multi-axis verb costs nothing extra in the template.
- **Option A (derived).** Each verb names the PRACTICES (histories) it reads, plus BODY and KIT.
  - **Combat** collapses to one combat practice key, plus body, plus kit. The eight `Combatant`
    attributes then either sit at the class default for everyone, or must be derived from practice.
    No source gives that derivation, so it is **open** and would have to be ruled.
  - **Command** collapses to a command practice. `derive_command(charisma, cognition)` loses its
    inputs, and either the stub is rewritten to read practice, or it reads the class default 4 for
    every general.
  - **Under A, multi-axis verbs are where differences between persons disappear first.** That is
    the measurable cost of A (§3.4 of the head).
