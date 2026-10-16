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

---

## 3. THE CAPACITY BLOCK, WRITTEN BOTH WAYS

Jordan: *"I don't know how to reconcile attributes against the subsystems and office training and
histories"*; *"I don't know what attributes should even exist or what each subsystem best needs"*.
So the capacity block starts from DEMAND: what each resolver would read from a person if its system
were complete (§3.1). It clusters that demand into axes (§3.2), states one reconciliation rule
(§3.3), reads the two rulings against each other (§3.4), and only then drafts the two options
(§3.5, §3.6). The full evidence, verb by verb, is §3A in
[`_part2`](2026-10-16-character-template_part2.md).

### 3.1 The demand table: what each resolver reads from a person

Code-stub rows (T1/T2) and prose-only rows (T3/T4) are kept in separate tables. Column (a) is what
the season loop reads TODAY (T1). Column (b) is what the resolver reads WHEN COMPLETE, with its
source and tier. The axis codes are §3A's (STR AGI END FOC ACU WIL ATT CHA BON are the registry's
nine; PRA practice per domain; TS Thread Sensitivity; TMP temperament; KIT what a person carries).

**Code rows.**

| # | resolver | (a) reads TODAY (T1) | (b) reads WHEN COMPLETE (source, tier) | axes (from b) | lane ref |
|---|---|---|---|---|---|
| D1 | the contested social roll (`tell`, `speak`) | one `capability` key, `copying`, as pool; the hearer's same key ÷ 2 as Ob (`sigma.py:97-129`; `rosters.yaml:1105-1107`) [CHECKED] | the contest kernel's `Contestant(faculty, standing_start, reserve_max, dossier, evidence, charisma)` (`systems/social_contest/sim/contest/resolver.py:184-195`): `faculty` → pool and leverage (`:300-301`); `charisma` → the Face ceiling, `charisma × 3` (`systems/social_contest/sim/contest/primitives.py:138-142`) [CHECKED] — **T2** | PRA (the social faculty), CHA | K-SC-2, M-NPC-1, K-IN-1 |
| D2 | personal combat (`fight`, `accept`) | `end` only, from the body band (`seam/wrappers/combat.py:130-138`); every other field the class default (`modules/combat/fight.py:45`) [CHECKED] | every `Combatant` field: `strength, agi, end, cog, att, spirit, focus, history, disp, weapon, armor, skills, equipped, tradition` (`combatant.py:93-94`), read through the bout's terms (§3A.4) [CHECKED] — **T2** | STR AGI END FOC ACU WIL ATT, PRA (`history`), TMP (`disp`), KIT | M-PC-1, K-PC-1, PC-06 K-1 |
| D3 | a field's commander (`march`; rally, recall) | the side's members' `weight`, stance and loyalty; no commander (`mass_battle.py:175-200`) [CHECKED] | `Officer(name, command=4, charisma, cognition)`, which derives `command` from the two (`units.py:2700-2722`; `exchange.py:57-66`) [CHECKED] — **T2**; the season's general is the marching actor or the defending seat-holder (`troop-stock-design_part2.md:68-79`) [CHECKED] — **T4** | CHA, ACU | M-MB-3, M-NPC-13, K-MB-2 |
| D4 | a field's troop quality | none: a side is one Line at fixed quality (JORDAN_STATEMENTS 3: *"a stub"*) | per-subunit `power, discipline, morale, dr` (`units.py:553-557`) [CHECKED] — **T2**; a company's grade in ITS OWN `capability` (`troop-stock-design.md:328`) [CHECKED] — **T4** | **none on a character**: a company's PRA, held by a cohort | M-MB-2, M-MB-16 |
| D5 | threadwork (the 7 operations; `thread_read`) | none: no TS carrier, `thread_read` untyped | `spirit × 2 + min(3, history + 3) + ts // 10` (`operations.py:235-247`); `resilience` resists the cost (`:269-274`, gain 0 at `:157`) [CHECKED] — **T2**; K-3 types `thread_read` on TS (`09_the_character_sheet.md:130`) [CHECKED] — **T4** | WIL, PRA (`history`), TS | M-WR-1, K-WR-2, K-3 |
| D6 | knots (`tie / knot`) | none: the row has no effect (H-182) | `bonds ≥ KNOT_BONDS_MIN` and disposition ≥ its minimum (`knots.py:185-192`) [CHECKED] — **T2** | BON | — |
| D7 | the scene budget (every verb) | body bands, live `hold` count, travel legs (`budget.py:57-61`) [CHECKED] | the same: the directions are #353's, *"not open"* (`budget.py:46-47`) [CHECKED] — **T1** | **none**: BODY and OFF | — |
| D8 | the chooser (every verb) | pursuits through `crisis_weights`, the confliction damp, the stance term (`engine/season/decision/choose.py:115-127`) [CHECKED] | the same, plus the refusal axis (H-146, unarmed) and a self-interest weight (M-NPC-12) — **T3** | **none**: values, not capacity | M-NPC-3, M-NPC-12 |
| D9 | the bodies pass (age, illness) | `born`, rates at 0 (`world_q.py:771-790`) [CHECKED] | the same with rates set (H-208) — **T1 dark** | **none**: age | M-NPC-3 |

**Prose-only rows (no code reads these yet).**

| # | demand | (b) WHEN COMPLETE (source, tier) | axes | lane ref |
|---|---|---|---|---|
| P1 | witness and inquiry competence (`examine`, `interview`, `research`, `surveil`, `reconstruct`) | AX-7: divergence turns on *"the channel …, the reader's competence, and their prior beliefs … all three together"* (`01_AXIOMS.md:288-289`) [CHECKED] — **T3**. The factor is 1, unbuilt (`options.py:1205-1209`; H-200) [CHECKED]. No stub reads it | competence: **which axis is open**. Candidates: ACU and ATT, the pair the 2026-08-15 proposal groups as *"Perception {Cognition, Attunement}"* (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:112`) [CHECKED] — **T4** | M-FI-3, K-FI-1 |
| P2 | governance and administration (a governor, a settlement's seat) | the 2026-08-15 proposal's role table: *"Governor — position — AP × compliance + Ledger — and a settlement"*, pool *"administrative practice"* (`:147`, `:170`) [CHECKED] — **T4**; no `systems/settlements/sim/` exists (`ls` printed nothing) | PRA (administration), OFF | [lane ref UNVERIFIED] |
| P3 | the persuasion actor and standing | the session's upload extracts (scratch `out/UP24_standing_persuasion_actor.md:41-42, :76, :106`; `out/UP07_critique_standing_persuasion.md:20`) — **T4, scratch, the uploads themselves not opened**: standing in four regimes (*"A1 ascribed, A2 accumulated, A3 performed, A4 staged"*); *"trainability belongs to the environment"*; political skill measured as *"networking, influence, apparent sincerity"*, while *"social astuteness did not"* predict; charisma tactics trained (UP24 `:53`) | PRA (per proceeding), CHA; standing derived from office and record, **not** an attribute | K-SC-2 |
| P4 | inquiry as access | the upload extract `out/UP17_mechanics_of_inquiry.md:93` — *"P29 Background flag … P30 Attribute voice"* — **T4, scratch** | PRA (a background as an access flag) | M-FI-3 |
| P5 | breadth of what a person may hold | the 2026-08-15 proposal's *"Recall — how many Histories you may hold active and how fast you learn"* (`:202`) [CHECKED] — **T4**; read by no verb row (§3A.3) | none with a reader | — |

**(a) is a strict subset of (b).** Today the loop reads, of any person:

- one PRA key (`copying`, for two verbs);
- BODY;
- `weight`;
- stance and values.

It reads none of the nine attributes, no TS, no TMP and no KIT. Every axis below is a column (b)
demand.

### 3.2 The axes the demand implies

**The glance table** (resolver | when-complete reads | axes | tier):

| resolver | when complete it reads | axes | tier |
|---|---|---|---|
| social contest roll | faculty, charisma | PRA, CHA | T2 |
| personal combat | 9 attributes' aliases, history, disp, kit | STR AGI END FOC ACU WIL ATT, PRA, TMP, KIT | T2 |
| commander | charisma, cognition | CHA, ACU | T2 (+T4 wiring) |
| troop quality | power, discipline, morale; a company's grade | (a company's PRA, not a character's) | T2 / T4 |
| threadwork | spirit, history, ts, resilience | WIL, PRA, TS | T2 |
| knots | bonds, disposition | BON | T2 |
| competence | competence | ACU or ATT (open) | T3 |
| administration | administrative practice | PRA, OFF | T4 |
| persuasion actor | practice, charisma, standing | PRA, CHA | T4 |

**Clustered.** Read from column (b), the demand falls into four kinds of axis:

1. **Nine attributes, every one with a T2 reader.** These are exactly the registry's nine
   (`references/descriptor_registry.yaml:36-48`) [CHECKED], under the aliases the stubs spell:
   - **Body**: STR (combat impact, health, balance), AGI (tempo, reflex, balance, initiative),
     END (wounds, stamina).
   - **Mind**: ACU = `cog` (combat reading; Command), FOC (poise recovery, disruption resistance),
     WIL = `spirit` (wounds, stamina; the thread pool).
   - **Social**: ATT = `att` (combat reading, reflex), CHA (Command; the Face ceiling), BON (the
     knot gate).

   **No axis in the nine is left without a reader** (ID-13 holds at T2). **None of the nine has a
   T1 reader**, so ID-13 does not yet hold in the game.
2. **PRA, one key per domain.** Contest faculty, combat `history`, thread `history`, `copying`,
   administration, command practice. It is read by D1, D2, D5, P2 and P3. It is what training
   writes. **It is a family of keys, not one axis**, so it cannot fill one roster slot (§3A.4.1).
3. **Three single-subsystem axes:**
   - **TS**: threadwork, a practitioner stat on its own 0–100 scale
     (`descriptor_registry.yaml:61-65`) [CHECKED].
   - **TMP**: combat's `disp`, a 1–7 lean.
   - **`resilience`**: threadwork's R-14 input. The registry folds Spirit into Will, and the plan
     names *"'spirit' (resilience, R-14)"* as *"a candidate input only"* for the tenth
     (`_part5.md:444`) [CHECKED].
4. **Not capacity: KIT, OFF, BODY, age, values.** Each already has, or should have, its own carrier.
   KIT has none (F18). The troop design's precedent puts a cohort's kit in its own person-rung's
   `Rung.stores` (`troop-stock-design.md:326`) [CHECKED], and the character-sheet proposal's K-5
   proposes `hold` Tenures on equipment objects (`09_the_character_sheet.md:132`) [CHECKED]. That
   choice is J-T5 (§8).

**How many genuinely distinct axes.** **Nine stored-able attributes**, plus **one family of practice
keys**, plus **three single-subsystem capacities** (TS, TMP, resilience). The verb × axis matrix
(§3A.3) confirms the nine: every one is read by at least one verb row. Recall is read by none.

**The ten.** Jordan ruled the COUNT: *"it will be 10 attributes"* (ED-IN-0185 Q7, 2026-08-14,
`registers/editorial_ledger_in_archive.jsonl:137`) [CHECKED]. **No source records him naming them.**

- The registry ships nine, and says *"The TENTH IS UNNAMED … Do not infer the tenth from the
  aliases"* (`descriptor_registry.yaml:27-31`) [CHECKED].
- ED-IN-0193 recorded the count and the nine (`editorial_ledger_in_archive.jsonl:145`) [CHECKED].
- The plan asks him for the name: *"you have given no name"* (`_part5.md:444`) [CHECKED].
- The 2026-08-15 proposal's option A-2, *"Ratify the 10 unchanged"* (`:192`) [CHECKED], is an
  earlier ten that includes Recall. The registry later dropped Recall (*"A-4 The registry's 9 (drop
  Recall)"*, `:194`) [CHECKED].

**By ID-13, the tenth must have a reader.** The demand offers three candidates with a T2 reader that
are not already among the nine: **TMP, TS, `resilience`**. It offers none for Recall. Naming the
tenth is **J-T2**, Jordan's. This proposal does not pick.

⚠ **Locator correction carried from the research suite.** `00_COMPARATIVE_ANALYSIS.md:78`
(RC-1), `:214` (X-14) and `:528` (J-C-3) cite the ten-attribute ruling as *"[CHECKED p5:515]"*.
The scratch critics (`critics/NPC.md:21`, `critics/COMPARATIVE.md:41`) and the SC lane's K-SC-2 row
cite J-13 at `_part5:504` and `:514`. `wc -l workplans/valoria_master_workplan_v9_part5.md`
→ `475`, so those lines do not exist in this tree. In the tree read here, J-13 is at `_part5.md:433`
(and the §J.2 remainder at `:443`), and the ten-attribute evidence at `:444`.

### 3.3 The reconciliation rule

Jordan's question was how attributes, subsystems, office, training and histories fit together. One
rule, with the ruled-on cell marked:

```
WHAT IS STORED        Option B: the ten attributes (1-7, closed roster), slow-moving.
                      Option A: nothing attribute-shaped.
                      BOTH:     practice, one key per domain (Person.capability), authored and trained.

WHAT TRAINING DOES    `train` (IN-12 step 9) raises PRACTICE: one domain key per act.
                      It never raises an attribute under A (there are none).
                      Under B, whether anything raises an attribute (age, a wound, nothing) is J-T4.

WHAT OFFICE GRANTS    OPTIONS (the remit, carried on the hold Tenure's payload: `granted_acts`),
                      SCENES (`budget_office_bonus` per live hold),
                      a TREASURY (`seat_rung`). Under the troop design, a company to command.
                      Never an attribute, never practice. A proceeding MAY rule that an office
                      changes an obstacle; no code does today (the obstacle's owner is the
                      proceedings subsystem, ED-SC-0033 (3), per `sigma.py:122-124`) [CHECKED].

WHAT STAYS DERIVED    Every subsystem figure, at read, never stored:
                      the contest pool, every Combatant term, Command, competence,
                      loyalty, regard, age, confliction, standing.
                      (J-13's "a derived score ... not a character attribute" is THIS line.)
```

Shown per subsystem, under each option:

| subsystem figure | Option B: derived from | Option A: derived from |
|---|---|---|
| contest pool (D1) | PRA[proceeding faculty] (+ CHA for the Face ceiling) | PRA[proceeding faculty] |
| `Combatant` (D2) | STR AGI END FOC ACU WIL ATT + PRA[`combat`] + TMP + KIT + BODY | PRA[`combat`] → `history`; BODY → `end`; KIT; **every other field the class default** |
| Command (D3) | `derive_command(CHA, ACU)` | PRA[`command`] → `Officer.command` directly (the class accepts a given `command`, `units.py:2711`) [CHECKED] |
| competence (P1) | ACU or ATT (open) + PRA[`inquiry`] | PRA[`inquiry`] |
| thread pool (D5) | WIL + PRA[`thread`] + TS | PRA[`thread`] + TS; `spirit` the module default 4 (`operations.py:241`) [CHECKED] |
| knot gate (D6) | BON | **no input**: the gate reads `bonds`, and under A it would sit at its `getattr` default 0, below the minimum, so no knot forms. A must rule a replacement. Open |

### 3.4 The two rulings, read against each other

- **"It will be 10 attributes"** (ED-IN-0185 Q7, 2026-08-14) [CHECKED]: a count, ruled, with no
  names.
- **J-13's constraints** (2026-09-06, RS-16, `workplans/valoria_master_workplan_v9_part8.md:329`)
  [CHECKED]:
  - *"pool only it is, but ensure you don't go so far as to deprive player of a chance at winning"*;
  - *"It's a derived score that is used for the subsystem for a character, but it is not a character
    attribute in and of itself"*.
  - The plan adopted (iii), `pool_default` everywhere a case names no vocation, as the interim
    (`_part5.md:433`) [CHECKED].

**They pull apart only on the broad reading.**

- **BROAD:** "a capacity is never stored; everything is derived". Then Option A, and the ruled ten
  is overwritten.
- **NARROW:** "the subsystem's figure (the social pool he was discussing) is derived, not an
  attribute". Then Option B satisfies both. The ten are stored, and every pool is derived from them
  at read.

The NPC critic flagged that K-NPC-1 cited neither reading (scratch `critics/NPC.md`, item 9). The
comparative critic flagged that J-C-3 would overwrite the ten (`critics/COMPARATIVE.md`, item 4).
**J-T1 is, in substance, the question: which reading did Jordan mean?**

*"Pool only"* binds the contest roll under either option. Capacity enters the sigma roll as dice,
and never as an Ob shift on the actor's own act. (The subject's capacity enters as Ob, per Jordan's
2026-08-14 *"score/2 plus modifiers"*, `sigma.py:115-120`.) [CHECKED]

### 3.5 OPTION A — derived capacity

| part | content |
|---|---|
| **carrier** | the existing `Person.capability` (`carriers.py:651`), re-keyed from verb keys to PRACTICE keys on a closed roster (`rosters.yaml: practice_roster`, which would absorb `verb_capability`'s values; `verb_capability` becomes verb → practice key). No new `Person` field |
| **readers** | each subsystem's host input builder derives its figure (§3.3's column A): `sigma._pool_of` unchanged; `seam/wrappers/combat.py` sets `history` from PRA[`combat`] beside `end`; the order of battle sets `Officer.command` from PRA[`command`]; `refracted_confidence`'s competence from PRA[`inquiry`]; a typed `thread_read` and the thread operations from PRA[`thread`] and TS. **TS needs a carrier under A too**: a practitioner stat, on `capability` under a `ts` key or its own field. That sub-choice is J-T1a |
| **write rule** | world-gen seats the template's `practice:` (04 F.6: *"world-gen writes it once; nothing else does"*, and its repair *"is a `practice` verb, not a field"*, `architecture/meta/04_CODE_ARCHITECTURE.md:1153`) [CHECKED]; `train` (IN-12 step 9) is the one runtime writer. The write-matrix row comes off `retired:` (`write_matrix.yaml:394-395`) [CHECKED], as step 9 already plans |
| **defaults** | an absent key is "not practised". The reader falls to its declared default (`pool_default`, H-126; the module's class default). The template never fills a guess |
| **tests** | (1) an all-null template reproduces today's `World.content_hash()` exactly, at build and after N seasons, because no field is added; (2) NPC-088's `copying: 3` survives the move from the overlay; (3) two persons differing in one practice key diverge in that verb's pool (the probe in F15) and, over N seeds, in its success rate, against the equal-key control |
| **what it does to the game** | persons differ by what they have PRACTISED, their BODY and their KIT, and by nothing innate. Two untrained persons are identical in every roll. Physical difference enters only through body condition and kit. Combat's measured attribute spreads (the 2026-08-15 proposal reports +6.0 to +20.4 pp per attribute, `:122-123`, **T4, not re-run**) are not reachable, because every `Combatant` attribute stays at its default. Training is the only route to being better, which makes `train` very strong in the chooser. **It overwrites ED-IN-0185 Q7**: only Jordan may |

### 3.6 OPTION B — stored attributes

| part | content |
|---|---|
| **carrier** | a new `Person.attributes: dict`, keyed by registry keys (`attr.body.strength` …), **seeded with nothing**: K-2's shape (`09_the_character_sheet.md:129`) [CHECKED]. Plus `Person.capability` as the practice store, exactly as in A. A `write_matrix.yaml` row `(Person, attributes)`, world-gen class |
| **roster** | the leaf `ATTRIBUTES` (`engine/substrate/descriptors.py:50`) and its scale (`:52-53`, floor 1, ceiling 7) [CHECKED], the single owner. The tenth slot stays PENDING (`ATTRIBUTES_PENDING_TENTH`, `:51`) until J-T2. The loader refuses a value for an unnamed slot |
| **readers** | each lands WITH ITS FIRST READER, as PC-06 already rules for K-2 (*"builds only with its first reader"*, `_part7.md:44`) [CHECKED]: (1) the combat host builder fills every `Combatant` attribute from the person, keeping `end`'s body derivation (K-1); (2) the order of battle builds `Officer(charisma, cognition)` from the commander (K-6, U-4); (3) the thread pool reads WIL as `spirit`; (4) competence reads its axis once P1's open choice is ruled. The contest roll does not read an attribute until the proceedings subsystem lands CHA's Face ceiling |
| **write rule** | world-gen only (04 F.6, as A). Whether anything later moves an attribute is J-T4: none (attributes are innate), age (through `born`), or a wound (through the bodies pass) |
| **defaults** | an absent key is "not authored". The reader falls to the MODULE's own default (`Combatant`'s 4/3, `combatant.py:93-94`; `Officer`'s 4), never to a template-side fill. Registry `default: 1` (`descriptor_registry.yaml:35`) [CHECKED] is **not** used as a seat-time fill: it would make every unauthored person a 1, below every module's default |
| **tests** | (1) loader refusals (§4); (2) all-null attributes: the act log and every event are identical to the pre-change tree at a fixed seed. **The content hash moves structurally**, because `Person`'s `repr` gains a field and `_entity_digest` hashes the `repr` (`engine/season/state/world.py:167-177`) [CHECKED]: a declared re-pin, the `Tenure.term` precedent (`carriers.py:103-105`) [CHECKED]; (3) two persons differing in one attribute build different `Combatant` fields and, over N seeds, different fight outcomes, against the equal-attribute control |
| **what it does to the game** | persons differ innately and by practice. Who wins a fight, who holds a line and who reads a lie vary by person **before** anyone trains. Multi-axis verbs keep their stub combinations (§3A.4). The cost is authoring: 46 × 9 values. **Today one cast row carries any attribute-like values**: NPC-001's `cognition 5, focus 5, endurance 4` map to ACU, FOC and END, the first through an alias the registry marks *"[ASSUMPTION] … Jordan veto"* (`descriptor_registry.yaml:42`) [CHECKED]; `social: '3–4'` is refused (a prose range, and not a registry name). So under B the shipped template is all-null for 45 rows and changes no outcome until values are supplied (§5) |

### 3.7 DECISION J-T1 — the capacity source (Jordan's)

- **(A)** derived: practice, body, kit and office only. Overwrites the ruled ten.
- **(B)** stored: the ten (nine plus J-T2's tenth) and practice. Reads J-13 narrowly.

**What waits on it:**

- R-09's by-person conjunct;
- K-1 and K-6 (U-4);
- the troop design's commander source (`troop-stock-design_part2.md:75-76`) [CHECKED];
- K-GO-8's creation screen fields;
- the template's `attributes:` block (§4).

**What does not wait:**

- every other template field;
- the practice block, which is the same under both;
- the loader and its refusals.
