# The character template: what an authored person carries, and what each field must move

## Status: PROPOSED (2026-10-16). Corrected the same day against an independent critic's report (22 findings; reconciliation table at the end of `_part3`). Not ratified; merge ratifies nothing unless Jordan so rules.
## Lane: IN (the carrier, the loader, the seating), with NPC (the cast rows), PC (the `Combatant`), SC (the contest pool), MB (commanders), FI (inquiry), WR (threadwork), GO (the creation screen). IDs: none allocated.
## Read at the working tree of 2026-10-16 (uncommitted edits by sibling sessions present; `proposals/2026-10-16-troop-stock-design.md` was being edited while this was corrected).
## Parts, in reading order: this file (§0–§3) · [`_part2`](2026-10-16-character-template_part2.md) (§3A, the idealized master verb table and the verb × capacity-kind matrix) · [`_part3`](2026-10-16-character-template_part3.md) (§4–§10).

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
**[CHECKED]** means opened in the correction pass. **[CHECKED-draft]** means opened in the drafting
pass and not re-opened since. **[RAN]** means the command was run in the correction pass and its
output is the figure beside it. **[UNVERIFIED]** means named but not opened.

**Words.** A **capacity kind** is a kind of personal quantity a resolver reads to set the odds, the
cost, a gate or an effect's size (the nine registry attributes, practice, Thread Sensitivity,
temperament, Recall, kit; codes in `_part2`). The first draft said "axis"; that word belongs to the
engine's `AXES` roster (`engine/substrate/descriptors.py`) and IN-08's seven axes. The demand rows
are labelled **CD** (code demand) and **PD** (prose demand), and the loader's refusals **LR**, so
that no label shadows canon's P-01..P-15, the season requirements' R-01..R-09
(`engine/season/requirements.yaml`), or v9's D2.

---

## 0. VERDICT

1. **A character template is the authored record world-gen reads to seat one `Person`.** The plan
   already says creation is *"no act; a cast entry the world-gen builder seats"*
   (`workplans/valoria_master_workplan_v9_part4.md:41`, IN-47) [CHECKED-draft]. Today that record exists,
   but split across three files and one harness overlay, and nothing types it as one thing (§1).
2. **Today persons differ in who they are, not in what they can do.** The 46 cast persons are
   authored on wants, pursuits, affiliations, faction, office and home. They are identical in
   capacity, body and age. Measured on `build_realm(0)` [RAN, §10 probe 1]: `Person.capability` is
   empty on 83 of 83 persons; `born` is 0 on all; `body` is 1000 on all. Over the 143 corpus cases,
   `capability` is empty on 429 of 430 built persons and holds `{copying: 3}` on one (NPC-088's
   `p_a`) — the figures `engine/season/requirements.yaml:76-82` records [CHECKED-draft], re-run.
3. **The template is 21 fields. By state today:** 8 authored, 1 derived at build, 3 defaulted,
   2 null on a carrier that exists, 7 not carried (§2 table; the partition rule and its order are
   there).
4. **Capacity is the one block that cannot be written without a ruling.** Two Jordan rulings pull
   apart: *"it will be 10 attributes"* (2026-08-14, ED-IN-0185 Q7, in an entry headed *"THE AGENDA
   IS CLOSED; DO NOT RE-RAISE IT"*) and J-13's *"It's a derived score that is used for the subsystem
   for a character, but it is not a character attribute in and of itself"* (2026-09-06). §3 drafts
   **Option A (derived: the template stores practice, office and kit, and capacity is a query)** and
   **Option B (stored: the template carries the ruled attributes on a closed roster, and every
   subsystem figure is derived from them)**. Each leaves cells open, and they are named (§3.5,
   §3.6). Two further options exist in the tree and are set out beside them (§3.7). The choice is
   **DECISION J-T1**, Jordan's. It is not made here.
5. **One finding narrows J-T1 without deciding it.** The two rulings conflict only on a BROAD reading
   of J-13 ("nothing about capacity is stored"). On a NARROW reading ("the subsystem's figure, such as
   the social pool, is not itself an attribute"), Option B satisfies both: attributes are stored, and
   every pool, command and competence is derived at read and never stored. The plan already glosses
   J-13 that narrow way: *"a social figure is derived, not stored"* (`workplans/valoria_master_workplan_v9_part5.md:433`)
   [CHECKED]. Which reading Jordan meant is the real question of J-T1 (§3.4).
6. **The demand side is measured from the verb table.** The idealized master verb table (§3A,
   `_part2`) has **65 rows** under one inclusion rule (§3A.1): 45 shipped (37 resolvable, 8 not),
   12 planned in v9, 7 in stub code outside the loop, 1 design-only. In four seeded realm seasons, 25
   verbs executed [RAN, §10 probe 6]. In code the season loop runs, exactly two capacity reads
   exist: `tell` reads one `capability` key, and `fight`/`accept` read the body band. (`speak` is
   mapped to the same key and reads nothing: it is not contested.) Read as complete systems, the
   stubs and designs read all nine registry attributes, a per-domain practice ("History"), Thread
   Sensitivity, a combat temperament and, in the fieldwork design only, Recall. Each of the nine has
   at least one T2 reader; Charisma's only one is `derive_command`. None of the nine has a T1
   reader (§3.2).
7. **The rest of the template is valid under either option.** Identity, placement, wants, values,
   ties, office, age and body do not depend on J-T1. The loader (§4) is written so the capacity block
   is the only part whose schema the ruling selects.
8. **What it adds and cuts (§6).** It adds one typed artifact, one loader function, one seating
   step, and `Person` fields: under either option `thread_sensitivity` (J-T1a, K-3's field), and
   under Option B also `attributes`. Each field lands only with its first reader. It stops treating
   the cast registry's unread `stats:`/`ts:` cells as a source the engine might read. It leaves the
   corpus overlays as the owner of their `capability:` values and copies none of them. It adds no
   subsystem.

---

## 1. WHAT A TEMPLATE IS AND IS NOT

Three things in the tree are called, or behave as, "templates". They must be kept apart, because
each seats a different kind of fact and has a different reader.

| | the CHARACTER template (this proposal) | the FACTION ROLE template | the COHORT template |
|---|---|---|---|
| **what it is** | the authored record for one named person, read once at world-gen | a weighted pursuit vector a faction expects of its members | one authored row per populated rung: a `Person` at `weight > 1` |
| **what it is in code today** | not one thing. Spread over `references/npc_registry.yaml` (name, faction, pursuits, affiliations, title), `engine/season/npcs.yaml` (institution, home, want, concerns), `engine/season/offices.yaml` (holder, obligees) and, in corpus worlds only, a case's `cast:` overlay (`capability`) | `rosters.yaml: role_templates`: six templates in `values:`, five of them assigned across six factions in `by_faction:` (Varfell and Löwenritter share `military-order`), and `intelligence-diplomatic` claimed by none (`engine/season/rosters.yaml:1425-1465`, the lists at `:1446-1465`) [CHECKED]; `Guilds` and `Schoenland` have none | `engine/season/cohorts.yaml` rows `{rung, weight}`, schema-checked by `cohort_rows` (`engine/season/harness/populated.py:335-385`) [CHECKED-draft] |
| **where it is seated** | `build_realm`'s cast loop (`populated.py:864-896`) [CHECKED-draft]; corpus worlds: `build_at` (`engine/season/harness/corpus_run.py:536-539`) [CHECKED-draft] | never seated on a person: it is a comparison target | `seat_cohorts` mints `Person(pid, name, weight=wt)` (`populated.py:439`) [CHECKED-draft] |
| **what reads it** | the readers in §2, field by field | `cast.loyalty` (`engine/season/data/cast.py:323-364`) [CHECKED-draft] turns the cosine between a member's pursuits and the template into a 0–100 loyalty; `stance_from_loyalty` (`cast.py:376-396`) turns that into one stance row, appended at build (`populated.py:1047-1049`) [CHECKED-draft] | `world_q.subsistence_draw` and `population` read `weight` (named in H-170's `site:`, `engine/season/hole_register.yaml:3722`) [CHECKED: the row; the readers not opened] |
| **what it must not become** | a second home for a faction's expectations or a population's size | a per-person field: a role template is a property of the faction, not of the office or the person (`rosters.yaml:1449-1452`) [CHECKED-draft] | a carrier of a named person's facts: a cohort *"traces to no case, so it carries none of"* the cast's fields (`populated.py:369`) [CHECKED-draft] |

**What the character template is NOT.**

- **Not a creation act.** IN-47's review found creation arm C1 *"cannot be carried out through the
  cast shape (no `pursuits` key; `corpus_run.py` `CAST_KEYS` is closed)"*
  (`valoria_master_workplan_v9_part4.md:41`) [CHECKED-draft]. The template is that shape, so a creation
  screen (K-GO-8) can write a template row and world-gen seats it. That is a precondition for C1,
  not C1 itself.
- **Not a progression system.** A template seeds tick 0. Change after tick 0 is the verbs' work
  (`train` at IN-12 step 9; `_scar_witnesses`; the bodies pass). §2 names each field's live writer.
- **Not a stat block for display.** A field with a carrier and no reader that moves an outcome is
  marked so in §2, not kept for show.
- **Not the troop stock.** A raised company is a cohort `Person` whose grade sits in its own
  `capability` (`proposals/2026-10-16-troop-stock-design.md:378`; that design is PROPOSED, `:3`)
  [CHECKED]. The character template
  does not author companies. It authors the commander whose qualities the order of battle reads (§9).

**Where the closed cast comes from.** ED-WR-0011, ruled 2026-09-13: *"World-gen NPC count, for now,
is just the 46 NPCs we built"*, option A, *"A CLOSED AUTHORED CAST"*
(`registers/editorial_ledger_wr_archive.jsonl:14`) [CHECKED]. The same entry calls itself
*"PROVISIONAL BY ITS OWN TERMS"*: *"a future session may not treat 46 as canon"*. So the template
has one row per cast case **for as long as that ruling stands** (46 today), and its loader reads the
count from the cast, never from a constant. A person CENSUS mints mid-campaign gets no template and seats on defaults
(`engine/season/loop/census.py:105`) [CHECKED-draft].

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
→ `13` [RAN]. The class is at `engine/season/state/carriers.py:642-721` [CHECKED-draft].

Registry counts in this table come from one command over `references/npc_registry.yaml`
(`yaml.safe_load`, counting rows where the key is present, and rows where it is neither null nor a
`[GAP…]` string) [RAN]. The command and its full output are in §5.

| # | field | carrier | reader (what moves) | state today (46 cast rows) | moves | falsifier (control: the same pair with the field equal) |
|---|---|---|---|---|---|---|
| F1 | identity: case id, name | `Person.id`, `Person.name` | `id` is every lookup's key. **`name`: no reader that moves an outcome** (a label) | **authored**: 46/46 (`first_name` 46, `last_name` 44 non-null: two mononyms) | — | none possible for `name`, and none is owed: it is identity, not a mechanism |
| F2 | home (where he lives and stands) | `contain` + `reside` Tenures on `Person.tenures` (`carriers.py:707`), minted at `populated.py:866-870` [CHECKED-draft] | presence decides who witnesses and who can be acted on; `world_q.residence_of` reads `reside` (named at `populated.py:867-869`) [reader not opened: UNVERIFIED] | **authored**: `npcs.yaml` `home` 46/46 | OPTIONS · MEMORY | two persons differing only in home: different witness sets for one act (deposit counts per holder) |
| F3 | institution | **no `Person` carrier**: a build-time input to F2 and F6 (seat lookup `populated.py:850-860`; tie pool `:1387-1390`) [CHECKED-draft] | build only | **not carried** (a build input: `npcs.yaml` `institution` 28/46 non-null; 18 null by design, *"null for an unaffiliated life"*) | via F2, F6 | covered by F2's and F6's falsifiers |
| F4 | faction membership | a `commit` Tenure to the faction's creed Proposition, plus the loyalty stance row (F10) | Q4 raises a standing question from every live `commit` to an OUGHT (`populated.py:914-916`, comment) [CHECKED-draft]; `mass_battle.field_input` reads loyalty toward the creed's utterer (`engine/season/seam/wrappers/mass_battle.py:175-200`) [CHECKED-draft] | **authored**: registry `faction` 46/46; 6 rows resolve to no roster faction (`cast.py:66`) [CHECKED-draft] | CHOICE · ODDS (morale) | two members of different factions: different Q4 questions; in a field, a different morale start |
| F5 | office | a `hold` Tenure whose `payload` carries the grant (`granted_acts`, `carriers.py:118-157`) [CHECKED-draft] | `person_side_eligible` (`engine/season/decision/options.py:352`) admits remit acts; `budget` adds `budget_office_bonus` per live `hold` (`engine/season/decision/budget.py:57-58`) [CHECKED-draft] | **authored**: `engine/season/offices.yaml` holders; probe [RAN, §10 probe 3]: 31 of 46 cast hold ≥ 1 `hold` at build (47 holds in all). Registry `title` 7/46 | OPTIONS · COST (scenes) | a holder and a non-holder: the holder forms remit candidates the other cannot, and has more scenes |
| F6 | want and tie | an OUGHT Proposition about the tied person, and a `commit` Tenure to it (`populated.py:1439-1441`) [CHECKED-draft] | `world_q.ambitions` → Q4 (`engine/season/queries/world_q.py:1586`) [CHECKED-draft]. **The want's TEXT has no reader**: Q4 reads the subject only (H-185, `hole_register.yaml:4162`) [CHECKED-draft] | **authored**: `npcs.yaml` `want` and `concerns` 46/46 | CHOICE | two persons tied to different people: different Q4 referents, so different candidate subjects |
| F7 | pursuits (values) | `Person.pursuits` (`carriers.py:653`), from `cast.pursuits_of` (`cast.py:183-229`), which refuses fewer than all fifteen [CHECKED-draft] | `options.project` (`options.py:274`) and `person_q.crisis_weights` (`engine/season/queries/person_q.py:497`) score every candidate; `regard` judges others' deeds by them (`person_q.py:335`) [CHECKED-draft] | **authored**: 46/46, a full fifteen-pursuit vector each (IN-64) | CHOICE · MEMORY (how he judges) | two persons differing in one pursuit weight: different candidate scores; at `choice_temperature` 0, a different top act where the pursuit is celled |
| F8 | affiliations (religious and civic convictions) | `Person.conviction` (`carriers.py:695`), from `cast.conviction_of` (`cast.py:232-263`), which refuses a row lacking any concern [CHECKED-draft] | scar counting on affiliation violations; `confliction` (`person_q.py:446`) damps the pursuit pull, **inert at the shipped `confliction_weight=0`** (`engine/season/data/fixtures.py:651`) [CHECKED-draft]; the crisis at scar 3 rewrites it (`person_q.py:568`) [CHECKED-draft] | **authored**: 46/46 | CHOICE (only once armed) · MEMORY | two persons differing in one affiliation: different scar counts after the same witnessed act. Under the shipped arm, identical scores: this field moves CHOICE only once `confliction_weight` > 0 |
| F9 | the registry's `goals:` list | **not carried** | **none** (the season's organization goals come from `goals.yaml`, keyed by organization, not this list) | **not carried** (the file holds it: present on 30 rows, non-null on 17; nothing seats it) | — | none possible. Carrying it would need a reader first (ID-13) |
| F10 | stance toward persons and seats | `Person.stance` (`carriers.py:652`) | `stance_toward` (`person_q.py:66`), `regard` (`:335`), the chooser's stance term, `teller_weight`, a field side's morale [CHECKED-draft] | **derived at build**, not authored: one loyalty row per committed member (§1). Probe [RAN, §10 probe 3]: 35 of 46 cast hold ≥ 1 row (rows per person: 0×11, 1×5, 2×22, 3×6, 6×2). No row is authored person-to-person | CHOICE · ODDS (morale) · MEMORY | two persons differing in one stance row toward X: different scores on candidates whose subject is X |
| F11 | obligations sworn | an `oblige` Tenure, minted from `offices.yaml` `obligees:` (`populated.py:1314-1328`) [CHECKED-draft], with no term (`offices.yaml:128`) [CHECKED] | four readers [CHECKED]: `purview_reaches`' oblige clause widens a seat's purview to the grounds its sworn (not `imposed`) obligees' seats reach (`engine/season/state/gate.py:355-370`, through `sworn_to`, `:384-393`); `world_q.establishment_of` (`queries/world_q.py:1534`), read by `epistemic.py:541` [body not opened]; `_req_oblige` clause 4, one edge per person and seat (`loop/predicates.py:394-395`); the renewal walk on a `transfer` (`loop/effects_economy.py:302-305`), which reads termed edges only, so not the two seeded ones. `faction_q.superiors` (`:194-196`) has a test caller and no production caller | **authored**: 2 `oblige` Tenures at build [RAN, §10 probe 3], from two rows that name an obligee: `offices.yaml:191` (NPC-070) and `:591` (NPC-041) [CHECKED] | OPTIONS (a seat holder's purview) | a seat whose holder has a sworn obligee, against the same seat with the `obligees:` row emptied: `purview_reaches` over the obligee's ground differs. Not run here; `engine/season/tests/test_fa04_oblige_purview.py` covers the NPC-070 edge [file named, not run] |
| F12 | known claims at tick 0 | `Person.ledger` (`carriers.py:657`) | `LedgerReader` (`person_q.py:662`) and the question sources read a person's own claims [CHECKED: the class] | **null**: probe [RAN, §10 probe 3], 0 of 46 cast hold a claim at build | CHOICE · MEMORY | two persons, one seeded with a claim about X: only he forms candidates on X in season 1 |
| F13 | birth tick (age) | `Person.born` (`carriers.py:675`) | `age_of` → `body_hazard` (`world_q.py:771-790`) [CHECKED-draft]; **dark**: `age_step` and `illness_rate` ship 0 (`fixtures.py:542-544`) [CHECKED-draft] | **defaulted**: `born = -age_at_build = 0` on all 83 realm persons [RAN, §10 probe 1]. Registry `age`: present on 29, non-null on 0 | COST (death hazard) once armed | two persons differing only in `born`, `age_step` > 0: different death draws over N seeds. At the shipped 0, identical |
| F14 | body | `Person.body` (`carriers.py:667`), default `condition_scale` 1000 | `body_band_penalty` → scenes (`budget.py:64-76`) and combat `end` (`engine/season/seam/wrappers/combat.py:130-138`) [CHECKED-draft] | **defaulted**: 1000 on all 83 [RAN, §10 probe 1] | COST (scenes) · ODDS (combat) | probe [RAN, §10 probe 4]: `party_end` is 4 at body 1000 and 2 at body 100 |
| F15 | capacity (`capability`) | `Person.capability` (`carriers.py:651`) | `sigma._capability` (`engine/season/seam/wrappers/sigma.py:82-94`) → pool (`:97-109`) and, for a person subject, Ob = score/2 (`:112-129`), reached through `contest_input` (`:132-147`), so by contested verbs only [CHECKED]. `tell` and `speak` map to `copying` (`rosters.yaml:1106-1107`) [CHECKED]; only `tell` declares `contests:` (`verb_table.yaml:953`) [CHECKED], so `speak`'s mapping reaches nothing | **null**: empty on 46/46 cast, 83/83 realm persons [RAN, §10 probe 1] | ODDS | probe [RAN, §10 probe 4]: `tell` pool 2 with `{}` and 5 with `{copying: 5}`; Ob 2.0 against the first (that is `obstacle_default`, since he brings no key) and 2.5 against the second |
| F16 | the ruled attributes | **not carried**: no `Person` field. The roster ships nine, scale 1–7, default 1, *"the tenth is UNNAMED"* (`references/descriptor_registry.yaml:27-48`) [CHECKED-draft]; exported as `ATTRIBUTES` (`engine/substrate/descriptors.py:50-51`) [CHECKED-draft] | **none in the season loop**: `ATTRIBUTES` has no importer in `engine/`, `modules/`, `systems/` or `tools/`; one test reads it (§10 probe 5) [RAN]. T2 readers exist under aliases (§3.2) | **not carried** (the file holds it: registry `stats:` present on 29, non-null on 1, NPC-001: `cognition 5, focus 5, endurance 4, social '3–4'`; nothing seats it) | ODDS · COST · EFFECT (once read) | §3 |
| F17 | Thread Sensitivity; Coherence | **not carried**. `(Person, coherence)` has a write-matrix row (`engine/season/write_matrix.yaml:171-172`) [CHECKED-draft] and no field | **none in the loop**. T2: the thread pool reads `ts` (`systems/threadwork/sim/operations.py:235-247`) and the knot's party gate reads it (`systems/fieldwork/sim/knots.py:195-198`) [CHECKED]. T4: `thread_read`'s gate and pool, `examine`'s Buried depth (`fieldwork_v30.md:301`, `:305`) [CHECKED] | **not carried** (the file holds it: registry `ts` present on 32, non-null on 10, of which 8 are integers and 2 are prose, `'75–80'`, `'~50'` [RAN]; nothing seats it) | ODDS · GATE · COST (once read) | §3.1 row CD5 |
| F18 | kit (weapon, armour, techniques) and retinue | **not carried** on a person | **none in the loop**. T2: `Combatant(…, weapon='arming', armor='light', skills, equipped, tradition)` (`modules/combat/combatant.py:93-94`) [CHECKED-draft] | **not carried** | ODDS · EFFECT (once read) | §3.1 row CD2 |
| F19 | temperament; per-person scar thresholds | **not carried**. The scar thresholds are ruled constants, 2 and 3 (`person_q.py:468-469`, ED-IN-0261) [CHECKED-draft] | T2: combat `disp`, a lean of `(disp-4)/3` (`modules/combat/combat_systems.py:183`) [CHECKED-draft]. The scar COUNT itself is live: `Person.scar` (`carriers.py:686`) | **not carried** (a scar is history, not template: it starts empty by design) | CHOICE (combat aggression, once read) | per-person thresholds: **none offered**, since a per-person threshold would overwrite a ruled constant. Temperament: §3.1 row CD2 |
| F20 | kin and lineage | **not carried**. The Tenure kinds are `hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban` (`rosters.yaml:101`; values read with `yaml.safe_load`); none is kin | **none** | **not carried** | — | none possible today: J-T3 (§8) |
| F21 | weight | `Person.weight` (`carriers.py:647`), default 1 | the larder draw, `population`, a field side's troops (`mass_battle.py:190-191`) [CHECKED-draft] | **defaulted**: 1 for every cast person; the cohort template authors it (§1) | COST · ODDS (fields) | belongs to the cohort template, not this one |

**The count, and its rule.** 21 fields. The state is the state of the CARRIER on the 46 cast
persons at build. Each field takes the FIRST of these five tests it passes, in this order, so every
field lands in exactly one class:

1. **not carried**: no `Person` field and no Tenure kind holds it after seating. (A value present in
   a file that nothing seats is still *not carried*; the row says what the file holds.)
2. **null**: a carrier exists, and every cast person's value is empty.
3. **defaulted**: a carrier exists, and every cast person holds one constant the code supplies.
4. **derived at build**: a carrier exists, and world-gen computes its values from other fields.
5. **authored**: a carrier exists, and at least one cast person's value comes from a file.

- **Not carried (7):** F3, F9, F16, F17, F18, F19, F20.
- **Null on an existing carrier (2):** F12, F15.
- **Defaulted (3):** F13, F14, F21.
- **Derived at build (1):** F10.
- **Authored (8):** F1, F2, F4, F5, F6, F7, F8, F11.

7 + 2 + 3 + 1 + 8 = 21. (The first draft's 9/1/3/2/6 counted F3 as authored with no carrier; the
order above is the tie-break it did not state.)

**Carrier exists, reader does not (or not in the loop), marked as such and given no invented reader:**
F1's `name` (a label); F13 and F8's `confliction` term (readers exist and ship dark at their
controls). Not carried, with readers only in T2 stub code or T4 designs: F16, F17, F18. Not
carried, with no reader: F9.

**A correction carried from the lane critics, re-checked here.** The NPC lane draft said every
mechanism that changes a person ships at its control. The critic contradicted it (scratch
`critics/NPC.md`, item 1) and the critic is right. Regard moves live: `judged_gain` and
`told_valence_gain` ship at 0.5 (`fixtures.py:748`, `:750`) [CHECKED-draft]. The stance term's weight
ships at 1 (`stance_gain`, `:773`) [CHECKED-draft]. Four realm seasons at seed 0, each surviving
person's fields compared with build [RAN, §10 probe 2]: body moved on 4 persons. 27 persons
held a non-empty scar. Stored `stance`, `pursuits`, `conviction` and `capability` moved on none.
What ships static, then, is VALUES (pursuits and convictions: the scar counts, but the threshold-2
shift is at 0 and no crisis fired in four seasons), CAPACITY (no writer) and AGE (dark). Body moves.
Regard moves at read, and the ledger moves at every deposit.

---

## 3. THE CAPACITY BLOCK, WRITTEN BOTH WAYS

Jordan: *"I don't know how to reconcile attributes against the subsystems and office training and
histories"*; *"I don't know what attributes should even exist or what each subsystem best needs"*.
So the capacity block starts from DEMAND: what each resolver would read from a person if its system
were complete (§3.1). It clusters that demand into capacity kinds (§3.2), states one
reconciliation rule (§3.3), reads the two rulings against each other (§3.4), and only then drafts
the options (§3.5–§3.7). The full evidence, verb by verb, is §3A in
[`_part2`](2026-10-16-character-template_part2.md).

### 3.1 The demand table: what each resolver reads from a person

Code-stub rows (T1/T2) and prose-only rows (T3/T4) are kept in separate tables. Column (a) is what
the season loop reads TODAY (T1). Column (b) is what the resolver reads WHEN COMPLETE, with its
source and tier. The capacity-kind codes are §3A's (STR AGI END FOC ACU WIL ATT CHA BON are the
registry's nine; PRA practice per domain; TS Thread Sensitivity; TMP temperament; REC Recall; KIT
what a person carries).

**Code rows.**

| # | resolver | (a) reads TODAY (T1) | (b) reads WHEN COMPLETE (source, tier) | kinds (from b) | lane ref |
|---|---|---|---|---|---|
| CD1 | the contested social roll (`tell`; `speak` only if it becomes contested) | for `tell`: one `capability` key, `copying`, as pool; the subject's same key ÷ 2 as Ob (`sigma.py:97-129`, through `contest_input`, `:132-147`) [CHECKED]. For `speak`: **nothing**: it declares no `contests:` (`verb_table.yaml:875-885`) [CHECKED], so its `copying` mapping (`rosters.yaml:1107`) is never reached | the contest kernel's `Contestant(faculty, …, charisma)` (`systems/social_contest/sim/contest/resolver.py:184-195`) [CHECKED]: `faculty` → pool and leverage (`:300-301`) [CHECKED-draft] — **T2**, a kernel the sibling proposal calls *"retiring"*, with attributes *"none bound"* (`proposals/2026-09-30-character-and-play-surface/10_verbs_and_attributes.md:144`) [CHECKED] — **T4**. `charisma` moves no outcome: it derives a Face view that leaves Standing, Readiness and leak *"bit-identical either way"* (`resolver.py:226-229`; `primitives.py:128-131`) [CHECKED]. For `speak`: *"`speak` becomes the contest"* (`10_verbs_and_attributes.md:123`) [CHECKED] — **T4** | PRA | K-SC-2, M-NPC-1, K-IN-1 |
| CD2 | personal combat (`fight`, `accept`) | `end` only, from the body band (`seam/wrappers/combat.py:129-138`); every other field the class default (`modules/combat/fight.py:45`) [CHECKED] | every `Combatant` field: `strength, agi, end, cog, att, spirit, focus, history, disp, weapon, armor, skills, equipped, tradition` (`combatant.py:93-94`) [CHECKED], read through the bout's terms (§3A.4) — **T2** | STR AGI END FOC ACU WIL ATT, PRA (`history`), TMP (`disp`), KIT | M-PC-1, K-PC-1, PC-06 K-1 |
| CD3 | a field's commander (`march`; the reform, recall and feint checks inside it) | the side's members' `weight`, stance and loyalty; no commander (`mass_battle.py:175-200`) [CHECKED-draft] | `Officer(name, command=4, charisma, cognition)`, which derives `command` from the two while `COMMAND_SIGMA_ENABLED` (default on) (`units.py:2700-2722`; `exchange.py:57-66`; `config.py:530`) [CHECKED] — **T2**. **At the defaults Command is not in the exchange pool**: `POOL_QUALITY_MODEL` is on (`config.py:556`) and *"Command is absent from this branch entirely"* (`exchange.py:103-126`) [CHECKED]. It reaches the reform gate, the recall and feint rolls, the morale-erosion divisors, yield eligibility, `h_per_size` and rout (§3A.4) [CHECKED]. The season's general is the marching actor or the defending seat-holder (`troop-stock-design_part2.md:68-79`) [CHECKED-draft] — **T4** | CHA, ACU | M-MB-3, M-NPC-13, K-MB-2 |
| CD4 | a field's troop quality | none: a side is one Line at fixed quality (JORDAN_STATEMENTS 3: *"a stub"*) | per-subunit `power, discipline, morale, dr` (`units.py:553-557`) [CHECKED-draft] — **T2**; a company's grade in ITS OWN `capability` (`troop-stock-design.md:378`) [CHECKED] — **T4** | **none on a character**: a company's PRA, held by a cohort | M-MB-2, M-MB-16 |
| CD5 | threadwork (the 7 operations; `thread_read`) | none: no TS carrier, `thread_read` untyped | `spirit × 2 + min(3, history + 3) + ts // 10` (`operations.py:235-247`); `resilience` resists the cost (`:249-274`, gain 0 at `:157`) [CHECKED] — **T2**. `thread_read`: *"(Spirit × 2) + History + TPS"*, TPS = TS ÷ 10, *"TS ≥ 30 required"* (`fieldwork_v30.md:305`, `:351`) [CHECKED] — **T4**; K-3 types its TS precondition (`09_the_character_sheet.md:130`) [CHECKED] — **T4** | WIL, PRA (`history`), TS | M-WR-1, K-WR-2, K-3 |
| CD6 | knots (`tie / knot`, through `form_knot`) | none: the row has no effect (H-182) | `bonds ≥ 5` (`knots.py:185-187`); a disposition ≥ 5, a stance not a capacity (`:189-193`); either party `ts ≥ 30` (`:195-198`); a cap of `bonds // 2 + 1` knots (`:200-203`); then the roll `spirit × 2 + history_relationships`, TN 7 (`:212-222`) [CHECKED] — **T2** | BON (gate, cap), TS (gate), WIL, PRA (roll) | — |
| CD7 | the scene budget (every verb) | body bands, live `hold` count, travel legs (`budget.py:57-61`) [CHECKED-draft] | the same: the directions are #353's, *"not open"* (`budget.py:46-47`) [CHECKED-draft] — **T1** | **none**: BODY and OFF | — |
| CD8 | the chooser (every verb) | pursuits through `crisis_weights`, the confliction damp, the stance term (`engine/season/decision/choose.py:115-127`) [CHECKED-draft] | the same, plus the refusal axis (H-146, unarmed) and a self-interest weight (M-NPC-12) — **T3** | **none**: values, not capacity | M-NPC-3, M-NPC-12 |
| CD9 | the bodies pass (age, illness) | `born`, rates at 0 (`world_q.py:771-790`) [CHECKED-draft] | the same with rates set (H-208) — **T1 dark** | **none**: age | M-NPC-3 |

**Prose-only rows (no code reads these yet).**

| # | demand | (b) WHEN COMPLETE (source, tier) | kinds | lane ref |
|---|---|---|---|---|
| PD1a | the five inquiry verbs (`examine`, `interview`, `research`, `surveil`, `reconstruct`) | the fieldwork design's §4.2 *"Primary Attribute"* column: Examine and Surveil → Cognition, Interview → Attunement, Research and Reconstruct → Recall; Examine reaches the Buried depth only *"if TS ≥ 10"* (`fieldwork_v30.md:301-306`) [CHECKED] — **T4**, a quarantined design. The shipped rows cite the same section (`verb_table.yaml:1170`, `:1185`) [CHECKED-draft]. The sibling proposal maps them the same way (`10_verbs_and_attributes.md:145`) [CHECKED]. Interview's row is kept only as *"the current mechanical baseline"*: ED-FI-0004 folds it into the Dialogue Lattice (`fieldwork_v30.md:308`) [CHECKED] | ACU (examine, surveil), ATT (interview), REC (research, reconstruct); TS as `examine`'s depth gate | M-FI-3, K-FI-1 |
| PD1b | AX-7's competence, at EVERY deposit | AX-7: divergence turns on *"the channel …, the reader's competence, and their prior beliefs … all three together"* (`01_AXIOMS.md:288-289`) [CHECKED-draft] — **T3**. The factor sits in `refracted_confidence`, which runs for every claim landing in any ledger, not only for inquiry verbs; it is 1, unbuilt (`options.py:1198-1211`; H-200) [CHECKED]. No stub reads it | **open**: no source names the capacity kind behind a reader's competence at deposit. The 2026-08-15 proposal groups ACU and ATT as *"Perception {Cognition, Attunement}"* (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:112`) [CHECKED] — **T4**, a grouping, not a mapping | M-FI-3, K-FI-1 |
| PD2 | governance and administration (a governor, a settlement's seat) | the 2026-08-15 proposal's role table: *"Governor — position — AP × compliance + Ledger — and a settlement"*, pool *"administrative practice"* (`:147`, `:170`) [CHECKED-draft] — **T4**; no `systems/settlements/sim/` exists (`ls` printed nothing) | PRA (administration), OFF | [lane ref UNVERIFIED] |
| PD3 | the persuasion actor and standing | the session's upload extracts (scratch `out/UP24_standing_persuasion_actor.md:41-42, :76, :106`; `out/UP07_critique_standing_persuasion.md:20`) — **T4, scratch, the uploads themselves not opened**: standing in four regimes (*"A1 ascribed, A2 accumulated, A3 performed, A4 staged"*); *"trainability belongs to the environment"*; political skill measured as *"networking, influence, apparent sincerity"*, while *"social astuteness did not"* predict; charisma tactics trained (UP24 `:53`) | PRA (per proceeding), CHA; standing derived from office and record, **not** an attribute | K-SC-2 |
| PD4 | inquiry as access | the upload extract `out/UP17_mechanics_of_inquiry.md:93` — *"P29 Background flag … P30 Attribute voice"* — **T4, scratch** | PRA (a background as an access flag) | M-FI-3 |
| PD5 | breadth of what a person may hold | the 2026-08-15 proposal's *"Recall — how many Histories you may hold active and how fast you learn"*, in a class it calls *"Capacities (gate, never roll)"* (`:124-125`, `:202`) [CHECKED] — **T4**. The fieldwork design instead rolls Recall as a primary attribute (PD1a). The two designs disagree on whether Recall is rolled | REC | — |

**(a) is a strict subset of (b).** Today the loop reads, of any person:

- one PRA key (`copying`, for one verb, `tell`);
- BODY;
- `weight`;
- stance and values;
- person-held quantities that are not capacity: his own ledger (`tell`, `comply`, `survey`,
  `reconstruct`), a Record he holds (`give`), his `weight` against a destination's room (`migrate`)
  (§3A.2.1) [CHECKED].

It reads none of the nine attributes, no TS, no TMP, no REC and no KIT. Every capacity kind below
is a column (b) demand.

### 3.2 The capacity kinds the demand implies

**The glance table** (resolver | when-complete reads | kinds | tier):

| resolver | when complete it reads | kinds | tier |
|---|---|---|---|
| social contest roll | faculty (charisma derives a view that moves nothing) | PRA | T2 (a retiring kernel) |
| personal combat | 9 attributes' aliases, history, disp, kit | STR AGI END FOC ACU WIL ATT, PRA, TMP, KIT | T2 |
| commander | charisma, cognition → Command → gates, rolls, divisors (not the default exchange pool) | CHA, ACU | T2 (+T4 wiring) |
| troop quality | power, discipline, morale; a company's grade | (a company's PRA, not a character's) | T2 / T4 |
| threadwork | spirit, history, ts, resilience | WIL, PRA, TS | T2 |
| `thread_read` | spirit, history, TPS; TS gate | WIL, PRA, TS | T4 |
| knots | bonds (gate, cap), ts (party gate), spirit and history (roll) | BON, TS, WIL, PRA | T2 |
| the five inquiry verbs | one primary attribute each; TS for `examine`'s depth | ACU, ATT, REC; TS | T4 |
| competence at deposit | competence | **open** | T3 |
| administration | administrative practice | PRA, OFF | T4 |
| persuasion actor | practice, charisma, standing | PRA, CHA | T4, scratch |

**Clustered.** Read from column (b), the demand falls into four groups:

1. **Nine attributes, every one with a T2 reader.** These are exactly the registry's nine
   (`references/descriptor_registry.yaml:36-48`) [CHECKED], under the aliases the stubs spell:
   - **Body**: STR (combat impact, health, balance), AGI (tempo, reflex, balance, initiative),
     END (wounds, stamina).
   - **Mind**: ACU = `cog` (combat reading; Command; in the fieldwork design, `examine` and
     `surveil`), FOC (poise recovery, disruption resistance), WIL = `spirit` (wounds, stamina; the
     thread pool; the knot roll).
   - **Social**: ATT = `att` (combat reading, reflex; in the fieldwork design, `interview`), CHA
     (Command only: its contest Face view moves no outcome, §3A.4), BON (the knot's gate and cap).

   **No kind in the nine is left without a reader** (ID-13 holds at T2). **CHA is the thinnest**:
   one T2 reader, `derive_command`. **None of the nine has a T1 reader**, so ID-13 does not yet hold
   in the game.
2. **PRA, one key per domain.** Contest faculty, combat `history`, thread `history`, knot
   `history_relationships`, `copying`, administration, command practice. It is read by CD1, CD2,
   CD5, CD6, PD2 and PD3. It is what training writes. **It is a family of keys, not one kind**, so it
   cannot fill one roster slot (§3A.4.1).
3. **Four further capacities outside the nine:**
   - **TS**: a practitioner stat on its own 0–100 scale (`descriptor_registry.yaml:61-65`)
     [CHECKED]. Read in the thread pool, the knot's party gate, and in the fieldwork design by
     `thread_read` and `examine`'s depth gate. Not single-subsystem.
   - **TMP**: combat's `disp`, a 1–7 lean.
   - **`resilience`**: threadwork's R-14 input. The registry folds Spirit into Will, and the plan
     names *"'spirit' (resilience, R-14)"* as *"a candidate input only"* for the tenth
     (`_part5.md:444`) [CHECKED].
   - **REC** (Recall): `research` and `reconstruct` in the fieldwork design only (T4); no code.
4. **Not capacity: KIT, OFF, BODY, age, values.** Each already has, or should have, its own carrier.
   KIT has none (F18), though it is counted as a capacity kind in the matrix because a resolver
   reads it per person. The troop design (PROPOSED) puts a cohort's kit in its own person-rung's
   `Rung.stores` (`troop-stock-design.md:376`) [CHECKED], and the character-sheet proposal's K-5
   proposes `hold` Tenures on equipment objects (`09_the_character_sheet.md:132`) [CHECKED]. That
   choice is J-T5 (§8).

**How many genuinely distinct kinds.** **Nine storable attributes**, plus **one family of practice
keys**, plus **four further capacities** (TS, TMP, resilience; REC in a design only). The matrix
(§3A.3) confirms the nine: every one is read by at least one verb row.

**The ten.** Jordan ruled the COUNT: *"it will be 10 attributes"* (ED-IN-0185 Q7, 2026-08-14,
`registers/editorial_ledger_in_archive.jsonl:137`) [CHECKED], in an entry headed *"RULED IN FULL,
2026-08-14. THE AGENDA IS CLOSED; DO NOT RE-RAISE IT."* **No source records him naming them.**

- The registry ships nine, and says *"The TENTH IS UNNAMED … Do not infer the tenth from the
  aliases"* (`descriptor_registry.yaml:27-31`) [CHECKED].
- ED-IN-0193 recorded the count, that *"NINE are defined"*, and that *"THE TENTH IS UNNAMED"*; it
  does not list the nine (`editorial_ledger_in_archive.jsonl:145`) [CHECKED].
- The plan asks him for the name: *"you have given no name"* (`_part5.md:444`) [CHECKED].
- The 2026-08-15 proposal set five roster options side by side (`:191-195`) [CHECKED]: A-1, *"Six
  faculties + two capacities"* (Str, Agi, End, Cog, Att, Spi; Recall and Bonds), which it
  RECOMMENDED; A-2, *"Ratify the 10 unchanged"*, a ten that includes Recall, Focus and Charisma;
  A-3; A-4, *"The registry's 9 (drop Recall)"*, which it marked REJECT; A-5. (The first draft read
  A-4 as a record that the registry "later dropped Recall". It is an option, and the registry's
  nine already existed when it was written.)

**By ID-13, the tenth must have a reader.** The demand offers three candidates with a T2 reader that
are not already among the nine: **TMP, TS, `resilience`**. **Recall has readers, at T4**: the
fieldwork design rolls it for `research` and `reconstruct` (PD1a). It is left off the T2 list on
a different ground: the sibling proposal judges it *"a capacity, not attribute"*, *"evidence for
D2, not a candidate for it"*, following the August census's class (`10_verbs_and_attributes.md:152-156`)
[CHECKED]. That is a judgement, and Jordan may overrule it. Naming the tenth is **J-T2**, Jordan's.
This proposal does not pick.

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
                      proceedings subsystem, ED-SC-0033 (3), per `sigma.py:122-124`) [CHECKED-draft].

WHAT STAYS DERIVED    Every subsystem figure, at read, never stored:
                      the contest pool, every Combatant term, Command, competence,
                      loyalty, regard, age, confliction, standing.
                      (J-13's "a derived score ... not a character attribute" is THIS line.)
```

Shown per subsystem, under each option:

| subsystem figure | Option B: derived from | Option A: derived from |
|---|---|---|
| contest pool (CD1) | PRA[proceeding faculty]; no attribute (CHA's Face view moves no outcome) | PRA[proceeding faculty] |
| `Combatant` (CD2) | STR AGI END FOC ACU WIL ATT + PRA[`combat`] + TMP + KIT + BODY | PRA[`combat`] → `history`; BODY → `end`; KIT; **every other field the class default** |
| Command (CD3) | `derive_command(CHA, ACU)`, reaching the reform gate, the recall and feint rolls and the erosion divisors (not the default exchange pool) | PRA[`command`] → `Officer.command` directly (the class accepts a given `command`, `units.py:2711`) [CHECKED] |
| the inquiry verbs (PD1a) | ACU, ATT or REC by verb, per the fieldwork design; REC is not among the nine, so under B `research` and `reconstruct` have no stored input unless J-T2 names Recall + PRA[`inquiry`] | PRA[`inquiry`] |
| competence at deposit (PD1b) | **open**: no source names its kind | PRA[`inquiry`], if a ruling says so; **open** |
| thread pool (CD5) | WIL + PRA[`thread`] + TS | PRA[`thread`] + TS; `spirit` the module default 4 (`operations.py:241`) [CHECKED] |
| knot (CD6) | BON (gate, cap) + TS (party gate) + WIL and PRA[relationships] (roll) | **BON and WIL have no input.** The gate reads `bonds`, which under A sits at its `getattr` default 0, below the minimum of 5, so no knot forms; the roll's `spirit` falls to its default 3 (`knots.py:185`, `:213`) [CHECKED]. TS comes from J-T1a's field; PRA[relationships] could feed `history_relationships`. A must rule a replacement for the gate. **Open** |

### 3.4 The two rulings, read against each other

- **"It will be 10 attributes"** (ED-IN-0185 Q7, 2026-08-14) [CHECKED]: a count, ruled, with no
  names, in an entry that closes its agenda: *"THE AGENDA IS CLOSED; DO NOT RE-RAISE IT"*
  (`editorial_ledger_in_archive.jsonl:137`) [CHECKED].
- **J-13's constraints** (2026-09-06, RS-16, `workplans/valoria_master_workplan_v9_part8.md:329`)
  [CHECKED-draft], quoted in the plan's J-13 row (`_part5.md:433`) [CHECKED]:
  - *"pool only it is, but ensure you don't go so far as to deprive player of a chance at winning"*;
  - *"It's a derived score that is used for the subsystem for a character, but it is not a character
    attribute in and of itself"*, which the plan glosses as *"a social figure is derived, not
    stored"*.
  - The row's three options were (i) the registry's `stats:`, (ii) *"a rank scale you rule"* and
    (iii) `pool_default` everywhere a case names no vocation. The plan adopted (iii) as the interim
    and named (ii) as a revert.

**They pull apart only on the broad reading.**

- **BROAD:** "a capacity is never stored; everything is derived". Then Option A, and the ruled ten
  is overwritten.
- **NARROW:** "the subsystem's figure (the social pool he was discussing) is derived, not an
  attribute". Then Option B satisfies both. The ten are stored, and every pool is derived from them
  at read. **The plan's own gloss is the narrow one.**

**Material that supports A, which the first draft did not cite.** The 2026-08-15 proposal: *"the
roles are not distinguished by aptitude — they are distinguished by practice, instruments, and
office"*, and combat, *"the one role Valoria expresses well"*, *"uses no attribute in its pool"*
(`proposals/2026-08-15-character-and-faction-stats-and-progression.md:152-162`) [CHECKED]. The
sibling proposal: every verb outside five domains *"needs no attribute"*
(`10_verbs_and_attributes.md:148-150`) [CHECKED].

The NPC critic flagged that K-NPC-1 cited neither reading (scratch `critics/NPC.md`, item 9). The
comparative critic flagged that J-C-3 would overwrite the ten (`critics/COMPARATIVE.md`, item 4).
**J-T1 is, in substance, the question: which reading did Jordan mean?** Escalating it does not
re-raise ED-IN-0185's closed agenda: the count stands under B, A-1 and J-13 (ii); only A would
overwrite it, and only Jordan may (`CLAUDE.md` §0's fifth answer does not reach a ruling's
overwrite).

*"Pool only"* binds the contest roll under either option. Capacity enters the sigma roll as dice,
and never as an Ob shift on the actor's own act. (The subject's capacity enters as Ob, per Jordan's
2026-08-14 *"score/2 plus modifiers"*, `sigma.py:112-129`.) [CHECKED]

### 3.5 OPTION A — derived capacity

| part | content |
|---|---|
| **carrier** | the existing `Person.capability` (`carriers.py:651`), re-keyed from verb keys to PRACTICE keys on a closed roster (`rosters.yaml: practice_roster`, which would absorb `verb_capability`'s values; `verb_capability` becomes verb → practice key). **Plus one new `Person` field, `thread_sensitivity`** (J-T1a, K-3's field): TS needs a carrier under A as under B. It lands only with its first reader (a typed `thread_read` gate, H-85) |
| **readers** | each subsystem's host input builder derives its figure (§3.3's column A): `sigma._pool_of` unchanged; `seam/wrappers/combat.py` sets `history` from PRA[`combat`] beside `end`; the order of battle sets `Officer.command` from PRA[`command`]; the inquiry verbs from PRA[`inquiry`]; a typed `thread_read` and the thread operations from PRA[`thread`] and `thread_sensitivity` |
| **write rule** | world-gen seats the template's `practice:`; `train` (IN-12 step 9) is the one runtime writer. This is the shape 04 F.6's REPAIR implies: F.6 records the gap *"`capability`'s season writer"*; its ASSUMED column, *"world-gen writes it once; nothing else does"*, is the assumption it says fails (*"a character never improves at anything"*); and its repair *"is a `practice` verb, not a field"* (`architecture/meta/04_CODE_ARCHITECTURE.md:1146`, `:1153`) [CHECKED], which `train` supersedes (`_part8.md:207`) [CHECKED]. The write-matrix row comes off `retired:` (`write_matrix.yaml:394-395`) [CHECKED-draft], as step 9 already plans |
| **defaults** | an absent key is "not practised". The reader falls to its declared default (`pool_default`, H-126; the module's class default). The template never fills a guess |
| **tests** | (1) an all-null template leaves the act log and every event identical to the pre-change tree at a fixed seed, at build and after N seasons. **The content hash moves structurally once J-T1a's field lands**, because `Person`'s `repr` gains a field and `_entity_digest` hashes the `repr` (`engine/season/state/world.py:167-177`) [CHECKED-draft]: a declared re-pin, the `Tenure.term` precedent (`carriers.py:103-105`) [CHECKED-draft]. Before that field lands, the hash is unchanged. (2) NPC-088's corpus world still seats `{copying: 3}` from its own overlay, which stays the owner (§4.4); the realm person seats none, as today. (3) two persons differing in one practice key diverge in that verb's pool (the probe in F15) and, over N seeds, in its success rate, against the equal-key control |
| **what it does to the game** | persons differ by what they have PRACTISED, their BODY and their KIT, and by nothing innate. Two untrained persons are identical in every roll. Physical difference enters only through body condition and kit. Combat's measured attribute spreads (the 2026-08-15 proposal reports +6.0 to +20.4 pp per attribute, `:122-123`, **T4, not re-run**) are not reachable, because every `Combatant` attribute stays at its default. Training is the only route to being better, which makes `train` very strong in the chooser. **It overwrites ED-IN-0185 Q7**: only Jordan may |

### 3.6 OPTION B — stored attributes

| part | content |
|---|---|
| **carrier** | a new `Person.attributes: dict`, keyed by registry keys (`attr.body.strength` …), **seeded with nothing**: K-2's shape (`09_the_character_sheet.md:129`) [CHECKED-draft]. Plus `Person.capability` as the practice store, exactly as in A. A `write_matrix.yaml` row `(Person, attributes)`, world-gen class |
| **roster** | the leaf `ATTRIBUTES` (`engine/substrate/descriptors.py:50`) and its scale (`:52-53`, floor 1, ceiling 7) [CHECKED-draft], the single owner. The tenth slot stays PENDING (`ATTRIBUTES_PENDING_TENTH`, `:51`) until J-T2. The loader refuses a value for an unnamed slot |
| **readers** | each lands WITH ITS FIRST READER, as the plan already rules for K-2 (*"K-2 … builds only with its first reader (K-1/K-6)"*, `_part7.md:44`) [CHECKED]: (1) the combat host builder fills every `Combatant` attribute from the person, keeping `end`'s body derivation (K-1); (2) the order of battle builds `Officer(charisma, cognition)` from the commander (K-6, U-4); (3) the thread pool and the knot roll read WIL as `spirit`, and the knot gate reads BON; (4) the inquiry verbs read ACU or ATT per the fieldwork design, once they are rolled. **The contest roll reads no attribute**: the kernel binds none (`10_verbs_and_attributes.md:144`) and Charisma's Face view moves no outcome (`resolver.py:226-229`) [CHECKED] |
| **write rule** | world-gen only. Whether anything later moves an attribute is J-T4 (§8): none (attributes are set at creation), age (through `born`), or a wound (through the bodies pass) |
| **defaults** | an absent key is "not authored". The reader falls to the MODULE's own default (`Combatant`'s 4/3, `combatant.py:93-94`; `Officer`'s 4), never to a template-side fill. Registry `default: 1` (`descriptor_registry.yaml:35`) [CHECKED-draft] is **not** used as a seat-time fill: it would make every unauthored person a 1, below every module's default |
| **tests** | (1) loader refusals (§4); (2) all-null attributes: the act log and every event are identical to the pre-change tree at a fixed seed. **The content hash moves structurally**, because `Person`'s `repr` gains `attributes` (and, with J-T1a, `thread_sensitivity`) and `_entity_digest` hashes the `repr` (`engine/season/state/world.py:167-177`) [CHECKED-draft]: a declared re-pin, the `Tenure.term` precedent (`carriers.py:103-105`) [CHECKED-draft]; (3) two persons differing in one attribute build different `Combatant` fields and, over N seeds, different fight outcomes, against the equal-attribute control |
| **what it does to the game** | persons differ innately and by practice. Who wins a fight, who holds a line and who forms a knot vary by person **before** anyone trains. Multi-kind verbs keep their stub combinations (§3A.4). The cost is authoring: 46 × 9 values. **Today one cast row carries any attribute-like values**: NPC-001's `cognition 5, focus 5, endurance 4` map to ACU, FOC and END, the first through an alias the registry marks *"[ASSUMPTION] … Jordan veto"* (`descriptor_registry.yaml:42`) [CHECKED-draft]; `social: '3–4'` is refused (a prose range, and not a registry name). So under B the shipped template is all-null for 45 rows and changes no outcome until values are supplied (§5) |

### 3.7 DECISION J-T1 — the capacity source (Jordan's)

- **(A)** derived: practice, body, kit and office only. Overwrites the ruled ten. Open cells: the
  knot gate (§3.3), competence at deposit (PD1b), the combat attributes' derivation (§3A.4.2).
- **(B)** stored: the ten (nine plus J-T2's tenth) and practice. Reads J-13 narrowly. Open cells:
  the tenth (J-T2), competence at deposit (J-T9), Recall's two inquiries unless J-T2 names it.
- **(A-1)** the 2026-08-15 proposal's recommendation, *"Six faculties + two capacities"*: Strength,
  Agility, Endurance, Cognition, Attunement, Spirit, rolled only through blends, plus Recall and
  Bonds as gates that never roll (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:191`,
  `:197-203`) [CHECKED]. It is a stored option with a different roster: it drops Focus and Charisma,
  so it overwrites the ruled ten as A does, and it leaves `derive_command` without its primary input.
- **(J-13 ii)** *"a rank scale you rule"* for `capability` (`_part5.md:433`) [CHECKED]: the plan's
  named revert for J-13. It is orthogonal to A and B: it rules the SCALE of practice values, which
  both options store. It is listed so the choice is not framed as A or B alone.

**What waits on it:**

- R-09's by-person conjunct;
- K-1 and K-6 (U-4);
- the troop design's commander source (`troop-stock-design_part2.md:75-76`) [CHECKED-draft];
- K-GO-8's creation screen fields;
- the template's `attributes:` block (§4).

**What does not wait:**

- every other template field;
- the practice block, which is the same under both;
- the loader and its refusals.
