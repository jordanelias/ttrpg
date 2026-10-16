# The character template: what an authored person carries, and what each field must move

## Status: PROPOSED (2026-10-16). Not ratified; merge ratifies nothing unless Jordan so rules.
## Lane: IN (the carrier, the loader, the seating), with NPC (the cast rows), PC (the `Combatant`), SC (the contest pool), MB (commanders), FI (competence), WR (threadwork), GO (the creation screen). IDs: none allocated.
## Read at the working tree of 2026-10-16 (uncommitted edits by sibling sessions present). Every `file:line` below was opened in this pass unless marked otherwise.
## Parts, in reading order: this file (§0–§3) · [`_part2`](2026-10-16-character-template_part2.md) (§3A, the idealized master verb table and the verb × axis matrix) · [`_part3`](2026-10-16-character-template_part3.md) (§4–§10).

**What this answers.** Jordan, this session: *"what do characters need so that they can be unique
individuals within context of game actions and choices and options etc?"*, then *"what would a
character template be?"*, then *"draft the character template as a proposal"*. Later in the session:
*"I don't know how to reconcile attributes against the subsystems and office training and
histories"*; *"I don't know what attributes should even exist or what each subsystem best needs"*;
*"work from idealized complete systems that may currently exist as stubbed code"*; *"cross reference
against a master verb table that is idealized as if fully designed and built"*; *"some verbs may
require multiple attributes."*

**The test every field must pass.** A template field exists only if it has a CARRIER on `Person`
and a READER that moves an outcome (`architecture/meta/01_AXIOMS.md:561`, ID-13: *"A DECLARED FIELD
MUST REACH A READER, OR IT IS NOT DECLARED"*). A difference between two persons that the template
authors must change at least one of five things: what a person CAN do (the option set), what he
CHOOSES, the ODDS of the same act, its COST or EFFECT SIZE, or what the world REMEMBERS of him.

**Evidence tiers used throughout.** **T1** code the season loop runs. **T2** code outside the loop
(module or `systems/*/sim` stubs, dark knobs, class defaults). **T3** a ratified spec, a Layer 1 row
or a v9 position's WHAT/EXIT. **T4** design intent only: proposals, quarantined designs, the
`research/by_lane/` suite, the session's upload extracts. Under `CLAUDE.md` §0.05 only T1 shows a
behaviour is correct; T2–T4 are admitted here as evidence of INTENT, and every row says which it is.
**[CHECKED]** means opened in this pass; **[UNVERIFIED]** means named but not opened.

---

## 0. VERDICT

1. **A character template is the authored record world-gen reads to seat one `Person`.** The plan
   already says creation is *"no act; a cast entry the world-gen builder seats"*
   (`workplans/valoria_master_workplan_v9_part4.md:41`, IN-47) [CHECKED]. Today that record exists,
   but split across three files and one harness overlay, and nothing types it as one thing (§1).
2. **Today persons differ in who they are, not in what they can do.** The 46 cast persons are
   authored on wants, pursuits, affiliations, faction, office and home. They are identical in
   capacity, body and age. Measured this pass on `build_realm(0)`: `Person.capability` is empty on
   83 of 83 persons; `born` is 0 on all; `body` is 1000 on all (probe, §10). Over the 143 corpus
   cases, `capability` is empty on 429 of 430 built persons and holds `{copying: 3}` on one
   (NPC-088's `p_a`) — the same figures `engine/season/requirements.yaml:76-82` records, re-run.
3. **The template is 21 fields. By state today:** 9 authored, 1 derived at build, 3 defaulted,
   2 null on a carrier that exists, 6 not carried at all (§2 table; the count rule is there).
4. **Capacity is the one block that cannot be written without a ruling.** Two Jordan rulings pull
   apart: *"it will be 10 attributes"* (2026-08-14, ED-IN-0185 Q7) and J-13's *"It's a derived score
   that is used for the subsystem for a character, but it is not a character attribute in and of
   itself"* (2026-09-06). §3 drafts **Option A (derived: the template stores practice, office and
   kit, and capacity is a query)** and **Option B (stored: the template carries the ruled attributes on
   a closed roster, and every subsystem figure is derived from them)** as complete alternatives. The
   choice is **DECISION J-T1**, Jordan's. It is not made here.
5. **One finding narrows J-T1 without deciding it.** The two rulings conflict only on a BROAD reading
   of J-13 ("nothing about capacity is stored"). On a NARROW reading ("the subsystem's figure, such as
   the social pool, is not itself an attribute"), Option B satisfies both: attributes are stored, and
   every pool, command and competence is derived at read and never stored. Which reading Jordan meant
   is the real question of J-T1 (§3.4).
6. **The demand side is now measured, from the verb table.** The idealized master verb table (§3A,
   `_part2`) has 83 rows: 45 shipped, 16 planned in v9, 19 in stub code outside the loop, and 3
   design-only or lane recommendations. In code the season loop runs, exactly two capacity reads
   exist: `tell`/`speak` read one `capability` key, and `fight`/`accept` read the body band.
   Read as complete systems, the stubs read all nine registry attributes, a per-domain practice
   ("History"), Thread Sensitivity and a combat temperament. Each of the nine has at least one T2
   reader. None of the nine has a T1 reader (§3.2).
7. **The rest of the template is valid under either option.** Identity, placement, wants, values,
   ties, office, age and body do not depend on J-T1. The loader (§4) is written so the capacity block
   is the only part whose schema the ruling selects.
8. **What it adds and cuts (§6).** It adds one typed artifact, one loader function, one seating
   step, and under Option B one `Person` field. It cuts the second, unread `stats:`/`ts:` vocabulary in
   the cast registry as a source the engine might read, and folds the corpus overlay's `capability:`
   into the template. It adds no subsystem.

---

## 1. WHAT A TEMPLATE IS AND IS NOT

Three things in the tree are called, or behave as, "templates". They must be kept apart, because
each seats a different kind of fact and has a different reader.

| | the CHARACTER template (this proposal) | the FACTION ROLE template | the COHORT template |
|---|---|---|---|
| **what it is** | the authored record for one named person, read once at world-gen | a weighted pursuit vector a faction expects of its members | one authored row per populated rung: a `Person` at `weight > 1` |
| **what it is in code today** | not one thing. Spread over `references/npc_registry.yaml` (name, faction, pursuits, affiliations, title), `engine/season/npcs.yaml` (institution, home, want, concerns), `engine/season/offices.yaml` (holder, obligees) and, in corpus worlds only, a case's `cast:` overlay (`capability`) | `rosters.yaml: role_templates`, six templates keyed by faction (`engine/season/rosters.yaml:1425-1465`) [CHECKED]; `Guilds` and `Schoenland` have none | `engine/season/cohorts.yaml` rows `{rung, weight}`, schema-checked by `cohort_rows` (`engine/season/harness/populated.py:335-385`) [CHECKED] |
| **where it is seated** | `build_realm`'s cast loop (`populated.py:864-896`) [CHECKED]; corpus worlds: `build_at` (`engine/season/harness/corpus_run.py:536-539`) [CHECKED] | never seated on a person: it is a comparison target | `seat_cohorts` mints `Person(pid, name, weight=wt)` (`populated.py:439`) [CHECKED] |
| **what reads it** | the readers in §2, field by field | `cast.loyalty` (`engine/season/data/cast.py:323-364`) [CHECKED] turns the cosine between a member's pursuits and the template into a 0–100 loyalty; `stance_from_loyalty` (`cast.py:376-396`) turns that into one stance row, appended at build (`populated.py:1047-1049`) [CHECKED] | `world_q.subsistence_draw` and `population` read `weight` (named in H-170's `site:`, `engine/season/hole_register.yaml:3722`) [CHECKED: the row; the readers not opened] |
| **what it must not become** | a second home for a faction's expectations or a population's size | a per-person field: a role template is a property of the faction, not of the office or the person (`rosters.yaml:1449-1452`) [CHECKED] | a carrier of a named person's facts: a cohort *"traces to no case, so it carries none of"* the cast's fields (`populated.py:369`) [CHECKED] |

**What the character template is NOT.**

- **Not a creation act.** IN-47's review found creation arm C1 *"cannot be carried out through the
  cast shape (no `pursuits` key; `corpus_run.py` `CAST_KEYS` is closed)"*
  (`valoria_master_workplan_v9_part4.md:41`) [CHECKED]. The template is that shape, so a creation
  screen (K-GO-8) can write a template row and world-gen seats it. That is a precondition for C1,
  not C1 itself.
- **Not a progression system.** A template seeds tick 0. Change after tick 0 is the verbs' work
  (`train` at IN-12 step 9; `_scar_witnesses`; the bodies pass). §2 names each field's live writer.
- **Not a stat block for display.** A field with a carrier and no reader that moves an outcome is
  marked so in §2, not kept for show.
- **Not the troop stock.** A levied company is a cohort `Person` whose grade sits in its own
  `capability` (`proposals/2026-10-16-troop-stock-design.md:328`) [CHECKED]. The character template
  does not author companies. It authors the commander whose qualities the order of battle reads (§9).

**Where the closed cast comes from.** ED-WR-0011, ruled 2026-09-13: *"World-gen NPC count, for now,
is just the 46 NPCs we built"*, option A, *"A CLOSED AUTHORED CAST"*
(`registers/editorial_ledger_wr_archive.jsonl:14`) [CHECKED]. So the template has exactly one row
per cast case (46 today). A person CENSUS mints mid-campaign gets no template and seats on defaults
(`engine/season/loop/census.py:105`) [CHECKED].

---

## 2. THE FIELD TABLE

**How to read it.** One row per field the template could carry. *Carrier* is the `Person` field (or
the Tenure kind) that holds it after seating; *reader* is the function that turns it into an outcome.
*State* is what the 46 cast rows carry TODAY. *Moves* is which of the five outcome kinds it changes
(OPTIONS · CHOICE · ODDS · COST/EFFECT · MEMORY). The *falsifier* names two persons differing in this
field alone, the observable, and the control (the same pair with the field equal).

The `Person` class has 13 fields (`id, name, weight, capability, stance, pursuits, ledger, body,
born, scar, conviction, travel_leg, tenures`), counted with
`python -c "import dataclasses; from engine.season.state.carriers import Person; print(len(dataclasses.fields(Person)))"`
→ `13`. The class is at `engine/season/state/carriers.py:642-721` [CHECKED].

Registry counts in this table come from one command over `references/npc_registry.yaml`
(`yaml.safe_load`, counting rows where the key is present, and rows where it is neither null nor a
`[GAP…]` string). The full output is in §5.

| # | field | carrier | reader (what moves) | state today (46 cast rows) | moves | falsifier (control: the same pair with the field equal) |
|---|---|---|---|---|---|---|
| F1 | identity: case id, name | `Person.id`, `Person.name` | `id` is every lookup's key. **`name`: no reader that moves an outcome** (a label) | **authored**: 46/46 (`first_name` 46, `last_name` 44 non-null: two mononyms) | — | none possible for `name`, and none is owed: it is identity, not a mechanism |
| F2 | home (where he lives and stands) | `contain` + `reside` Tenures on `Person.tenures` (`carriers.py:707`), minted at `populated.py:866-870` [CHECKED] | presence decides who witnesses and who can be acted on; `world_q.residence_of` reads `reside` (named at `populated.py:867-869`) [reader not opened: UNVERIFIED] | **authored**: `npcs.yaml` `home` 46/46 | OPTIONS · MEMORY | two persons differing only in home: different witness sets for one act (deposit counts per holder) |
| F3 | institution | **no `Person` carrier**: a build-time input to F2 and F6 (seat lookup `populated.py:850-860`; tie pool `:1387-1390`) [CHECKED] | build only | **authored**: `npcs.yaml` `institution` 28/46 non-null; 18 null by design (*"null for an unaffiliated life"*) | via F2, F6 | covered by F2's and F6's falsifiers |
| F4 | faction membership | a `commit` Tenure to the faction's creed Proposition, plus the loyalty stance row (F10) | Q4 raises a standing question from every live `commit` to an OUGHT (`populated.py:914-916`, comment) [CHECKED]; `mass_battle.field_input` reads loyalty toward the creed's utterer (`engine/season/seam/wrappers/mass_battle.py:175-200`) [CHECKED] | **authored**: registry `faction` 46/46; 6 rows resolve to no roster faction (`cast.py:66`) [CHECKED] | CHOICE · ODDS (morale) | two members of different factions: different Q4 questions; in a field, a different morale start |
| F5 | office | a `hold` Tenure whose `payload` carries the grant (`granted_acts`, `carriers.py:118-157`) [CHECKED] | `person_side_eligible` (`engine/season/decision/options.py:352`) admits remit acts; `budget` adds `budget_office_bonus` per live `hold` (`engine/season/decision/budget.py:57-58`) [CHECKED] | **authored**: `engine/season/offices.yaml` holders; probe: 31 of 46 cast hold ≥ 1 live `hold` at build (47 holds in all). Registry `title` 7/46 | OPTIONS · COST (scenes) | a holder and a non-holder: the holder forms remit candidates the other cannot, and has more scenes |
| F6 | want and tie | an OUGHT Proposition about the tied person, and a `commit` Tenure to it (`populated.py:1439-1441`) [CHECKED] | `world_q.ambitions` → Q4 (`engine/season/queries/world_q.py:1586`) [CHECKED]. **The want's TEXT has no reader**: Q4 reads the subject only (H-185, `hole_register.yaml:4162`) [CHECKED] | **authored**: `npcs.yaml` `want` and `concerns` 46/46 | CHOICE | two persons tied to different people: different Q4 referents, so different candidate subjects |
| F7 | pursuits (values) | `Person.pursuits` (`carriers.py:653`), from `cast.pursuits_of` (`cast.py:183-229`), which refuses fewer than all fifteen [CHECKED] | `options.project` (`options.py:274`) and `person_q.crisis_weights` (`engine/season/queries/person_q.py:497`) score every candidate; `regard` judges others' deeds by them (`person_q.py:335`) [CHECKED] | **authored**: 46/46, a full fifteen-pursuit vector each (IN-64) | CHOICE · MEMORY (how he judges) | two persons differing in one pursuit weight: different candidate scores; at `choice_temperature` 0, a different top act where the pursuit is celled |
| F8 | affiliations (religious and civic convictions) | `Person.conviction` (`carriers.py:695`), from `cast.conviction_of` (`cast.py:232-263`), which refuses a row lacking any concern [CHECKED] | scar counting on affiliation violations; `confliction` (`person_q.py:446`) damps the pursuit pull, **inert at the shipped `confliction_weight=0`** (`engine/season/data/fixtures.py:651`) [CHECKED]; the crisis at scar 3 rewrites it (`person_q.py:568`) [CHECKED] | **authored**: 46/46 | CHOICE (only once armed) · MEMORY | two persons differing in one affiliation: different scar counts after the same witnessed act. Under the shipped arm, identical scores: this field moves CHOICE only once `confliction_weight` > 0 |
| F9 | the registry's `goals:` list | **not carried** | **none** (the season's organization goals come from `goals.yaml`, keyed by organization, not this list) | **not carried**: present on 30 rows, non-null on 17 | — | none possible. Carrying it would need a reader first (ID-13) |
| F10 | stance toward persons and seats | `Person.stance` (`carriers.py:652`) | `stance_toward` (`person_q.py:66`), `regard` (`:335`), the chooser's stance term, `teller_weight`, a field side's morale [CHECKED] | **derived at build**, not authored: one loyalty row per committed member (§1). Probe: 35 of 46 cast hold ≥ 1 row (rows per person: 0×11, 1×5, 2×22, 3×6, 6×2). No row is authored person-to-person | CHOICE · ODDS (morale) · MEMORY | two persons differing in one stance row toward X: different scores on candidates whose subject is X |
| F11 | obligations sworn | an `oblige` Tenure, minted from `offices.yaml` `obligees:` (`populated.py:1314-1328`) [CHECKED] | `Tenure.imposed` separates a sentence from an oath (`carriers.py:112-115`) [CHECKED]; who else reads an oath was not traced [UNVERIFIED] | **authored**: 2 `oblige` Tenures at build; one row names an obligee (`engine/season/offices.yaml:191`, NPC-070) [CHECKED] | OPTIONS (presumed) | not stated: its readers were not traced in this pass |
| F12 | known claims at tick 0 | `Person.ledger` (`carriers.py:657`) | `LedgerReader` (`person_q.py:662`) and the question sources read a person's own claims [CHECKED: the class] | **null**: probe, 0 of 46 cast hold a claim at build | CHOICE · MEMORY | two persons, one seeded with a claim about X: only he forms candidates on X in season 1 |
| F13 | birth tick (age) | `Person.born` (`carriers.py:675`) | `age_of` → `body_hazard` (`world_q.py:771-790`) [CHECKED]; **dark**: `age_step` and `illness_rate` ship 0 (`fixtures.py:542-544`) [CHECKED] | **defaulted**: `born = -age_at_build = 0` on all 83 realm persons (probe). Registry `age`: present on 29, non-null on 0 | COST (death hazard) once armed | two persons differing only in `born`, `age_step` > 0: different death draws over N seeds. At the shipped 0, identical |
| F14 | body | `Person.body` (`carriers.py:667`), default `condition_scale` 1000 | `body_band_penalty` → scenes (`budget.py:64-76`) and combat `end` (`engine/season/seam/wrappers/combat.py:130-138`) [CHECKED] | **defaulted**: 1000 on all 83 (probe) | COST (scenes) · ODDS (combat) | probe [RAN]: `party_end` is 4 at body 1000 and 2 at body 100 |
| F15 | capacity (`capability`) | `Person.capability` (`carriers.py:651`) | `sigma._capability` (`engine/season/seam/wrappers/sigma.py:82-94`) → pool (`:97-109`) and, for a person subject, Ob = score/2 (`:112-129`) [CHECKED]; only `tell` and `speak` map to a key, `copying` (`rosters.yaml:1105-1107`) [CHECKED] | **null**: empty on 46/46 cast, 83/83 realm persons (probe) | ODDS | probe [RAN]: `tell` pool 2 with `{}` and 5 with `{copying: 5}`; Ob 2.0 vs 2.5 against them |
| F16 | the ruled attributes | **not carried**: no `Person` field. The roster ships nine, scale 1–7, default 1, *"the tenth is UNNAMED"* (`references/descriptor_registry.yaml:27-48`) [CHECKED]; exported as `ATTRIBUTES` (`engine/substrate/descriptors.py:50-51`) [CHECKED] | **none in the season loop**: `ATTRIBUTES` has no importer in `engine/`, `modules/`, `systems/` or `tools/` (grep, §10). T2 readers exist under aliases (§3.2) | **not carried**. Registry `stats:` present on 29, non-null on 1 (NPC-001: `cognition 5, focus 5, endurance 4, social '3–4'`) | ODDS · COST · EFFECT (once read) | §3 |
| F17 | Thread Sensitivity; Coherence | **not carried**. `(Person, coherence)` has a write-matrix row (`engine/season/write_matrix.yaml:171-172`) [CHECKED] and no field | **none in the loop**. T2: the thread pool reads `ts` (`systems/threadwork/sim/operations.py:235-247`) [CHECKED] | **not carried**. Registry `ts`: present on 32, non-null on 10, of which 8 are integers and 2 are prose (`'75–80'`, `'~50'`) | ODDS · COST (once read) | §3.1 row D5 |
| F18 | kit (weapon, armour, techniques) and retinue | **not carried** on a person | **none in the loop**. T2: `Combatant(…, weapon='arming', armor='light', skills, equipped, tradition)` (`modules/combat/combatant.py:93-94`) [CHECKED] | **not carried** | ODDS · EFFECT (once read) | §3.1 row D2 |
| F19 | temperament; per-person scar thresholds | **not carried**. The scar thresholds are ruled constants, 2 and 3 (`person_q.py:468-469`, ED-IN-0261) [CHECKED] | T2: combat `disp`, a lean of `(disp-4)/3` (`modules/combat/combat_systems.py:183`) [CHECKED]. The scar COUNT itself is live: `Person.scar` (`carriers.py:686`) | **not carried** (a scar is history, not template: it starts empty by design) | CHOICE (combat aggression, once read) | per-person thresholds: **none offered**, since a per-person threshold would overwrite a ruled constant. Temperament: §3.1 row D2 |
| F20 | kin and lineage | **not carried**. The Tenure kinds are `hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban` (`rosters.yaml:101`; values read with `yaml.safe_load`); none is kin | **none** | **not carried** | — | none possible today: J-T3 (§8) |
| F21 | weight | `Person.weight` (`carriers.py:647`), default 1 | the larder draw, `population`, a field side's troops (`mass_battle.py:190-191`) [CHECKED] | **defaulted**: 1 for every cast person; the cohort template authors it (§1) | COST · ODDS (fields) | belongs to the cohort template, not this one |

**The count, and its rule.** 21 fields. A field counts as *authored* when at least one cast row
carries a non-default value from a file, *derived at build* when world-gen computes it from authored
fields, *defaulted* when every person receives one constant, *null* when the carrier exists and every
cast person's value is empty, *not carried* when no carrier exists.

- **Authored (9):** F1, F2, F3, F4, F5, F6, F7, F8, F11.
- **Derived at build (1):** F10.
- **Defaulted (3):** F13, F14, F21.
- **Null on an existing carrier (2):** F12, F15.
- **Not carried (6):** F9, F16, F17, F18, F19, F20.

**Carrier exists, reader does not (or not in the loop), marked as such and given no invented reader:**
F1's `name` (a label); F9 (neither); F11 beyond `imposed` (untraced); F13 and F8's `confliction`
term (readers exist and ship dark at their controls); F16, F17, F18 (readers only in T2 stub code).

**A correction carried from the lane critics, re-checked here.** The NPC lane draft said every
mechanism that changes a person ships at its control. The critic contradicted it (scratch
`critics/NPC.md`, item 1) and the critic is right. Regard moves live: `judged_gain` and
`told_valence_gain` ship at 0.5 (`fixtures.py:748`, `:750`) [CHECKED]. The stance term's weight
ships at 1 (`stance_gain`, `:773`) [CHECKED]. This pass ran four realm seasons at seed 0 and
compared each surviving person's fields with build (probe, §10). Body moved on 4 persons. 27 persons
held a non-empty scar. Stored `stance`, `pursuits`, `conviction` and `capability` moved on none.
What ships static, then, is VALUES (pursuits and convictions: the scar counts, but the threshold-2
shift is at 0 and no crisis fired in four seasons), CAPACITY (no writer) and AGE (dark). Body moves.
Regard moves at read, and the ledger moves at every deposit.
