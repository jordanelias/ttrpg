# The character template: what an authored person carries, and what each field must move

## Status: PROPOSED (2026-10-16). Corrected three times the same day against three independent critics' reports (22 findings, then 20, then 13; all three reconciliation tables are at the end of `_part3`). Not ratified; merge ratifies nothing unless Jordan so rules.
## Lane: IN (the carrier, the loader, the seating), with NPC (the cast rows), PC (the `Combatant`), SC (the contest pool), MB (commanders), FI (inquiry), WR (threadwork), GO (the creation screen). IDs: none allocated.
## Read at the working tree of 2026-10-16 (uncommitted edits by sibling sessions present). `proposals/2026-10-16-troop-stock-design.md` and its `_part2` are being rewritten by a sibling session, so this proposal cites them by J-number and section number first, and quotes a heading only as it reads at this pass, never by line.
## Parts, in reading order: this file (§0–§3) · [`_part2`](2026-10-16-character-template_part2.md) (§3A, the idealized master verb table and the verb × personal-input matrix) · [`_part3`](2026-10-16-character-template_part3.md) (§4–§10).

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
(module or `systems/*/sim` stubs, dark knobs, class defaults). **T3** a ratified spec, a Layer 1 row,
a v9 position's WHAT/EXIT, or a proposal the plan records as RATIFIED AS INTENT. **T4** design intent
only: proposals not ratified, quarantined designs, the `research/by_lane/` suite, the session's upload
extracts. Under `CLAUDE.md` §0.05 only T1 shows a behaviour is correct; T2–T4 are admitted here as
evidence of INTENT, and every row says which it is. **Where two sources disagree, the higher tier
wins, and the loser is recorded, not counted.** **Where two sources of the SAME tier disagree, the
cell is open and counts as 0, and both are recorded** (added in the fourth pass, for `speak`). **An
inference from a source is not that source**: a reading this proposal infers is tagged as an
inference and does not override a stated reading at any tier.

**Tags.** **[CHECKED]** opened in the FOURTH pass (this one, the third correction). **[CHECKED-3]**
opened in the third pass (the second correction) and not re-opened since. **[CHECKED-2]** opened in
the second pass (the first correction) and not re-opened since. **[CHECKED-draft]** opened in the drafting pass
only. **[RAN]** run in a correction pass, with the printed figure beside it; §10 names the artifact
on disk where one exists. **[UNVERIFIED]** named but not opened.

**Words.** A **personal input** is a quantity a resolver reads off a person to set the odds, the
cost, a gate or the size of an effect: one of the nine registry attributes, practice, Thread
Sensitivity, temperament, resilience, Recall, or kit (codes in `_part2`). **One rule, everywhere:**
live state the season writes (BODY, the body band), an office held by a Tenure (OFF), and
person-held quantities (a claim in his ledger, a Record he holds, his `weight`, a stance row, his
values) are named where a resolver reads them and are **never** counted as personal inputs. **Not to
be confused with `PersonalCombatInput`** (`engine/season/queries/inputs.py:45`) [CHECKED], the combat
seam's input record: its `ends` field is BODY-derived (*"each party's one derived field, `end`"*,
`:51`) [CHECKED], so what that class carries is not a personal input in this proposal's sense. The
first draft said "axis", the engine's `AXES` roster's word (`engine/substrate/descriptors.py`). The
second said "capacity kind", which collides twice: the 2026-08-15 census's tier *"Capacities (gate
what you may hold, never roll)"*, which it sets apart from attributes
(`proposals/2026-08-15-character-and-faction-stats-and-progression.md:124`) [CHECKED-3], and
`world_q.capacity(w, rung_id)`, a settlement's room (`engine/season/queries/world_q.py:1096`)
[CHECKED-3]. `git grep -il "personal input"` over the whole tracked tree printed nothing before this
edit [RAN]. The demand rows are labelled **CD** (code demand) and **PD** (prose demand), and the
loader's refusals **LR**, so that no label shadows canon's P-01..P-15, the season requirements'
R-01..R-09 (`engine/season/requirements.yaml`), or v9's D2.

---

## 0. VERDICT

1. **A character template is the authored record world-gen reads to seat one `Person`.** The plan
   already says creation is *"no act; a cast entry the world-gen builder seats"*
   (`workplans/valoria_master_workplan_v9_part4.md:41`, IN-47) [CHECKED-3]. Today that record exists,
   but split across three files and one harness overlay, and nothing types it as one thing (§1).
2. **Today persons differ in who they are, not in what they can do.** The 46 cast persons are
   authored on wants, pursuits, affiliations, faction, office and home. They are identical in
   personal inputs, body and age. Measured on `build_realm(0)` [RAN, §10 probe 1]: `Person.capability`
   is empty on 83 of 83 persons; `born` is 0 on all; `body` is 1000 on all. Over the 143 corpus cases,
   `capability` is empty on 429 of 430 built persons and holds `{copying: 3}` on one (NPC-088's
   `p_a`) — the figures `engine/season/requirements.yaml:76-82` records [CHECKED-2], re-run.
3. **The template is 21 fields. By state today:** 8 authored, 1 derived at build, 3 defaulted,
   2 null on a carrier that exists, 7 not carried (§2 table; the partition rule and its order are
   there).
4. **The personal-input block is the one block that cannot be written without a ruling.** Two
   Jordan rulings pull apart: *"it will be 10 attributes"* (2026-08-14, ED-IN-0185 Q7, in an entry
   headed *"THE AGENDA IS CLOSED; DO NOT RE-RAISE IT"*) and J-13's *"It's a derived score that is used
   for the subsystem for a character, but it is not a character attribute in and of itself"*
   (2026-09-06). §3 drafts **Option A (derived: the template stores practice, office and kit, and
   every subsystem figure is a query over them)** and **Option B (stored: the template carries the
   ruled attributes on a closed roster, and every subsystem figure is derived from them)**. Each
   leaves cells open, and they are named (§3.5, §3.6). Two further options exist in the tree and are
   set out beside them (§3.7). The choice is **DECISION J-T1**, Jordan's. It is not made here.
5. **One finding narrows J-T1 without deciding it.** The two rulings conflict only on a BROAD reading
   of J-13 ("nothing a person brings to a roll is stored"). On a NARROW reading ("the subsystem's
   figure, such as the social pool, is not itself an attribute"), Option B satisfies both: attributes
   are stored, and every pool, command and competence is derived at read and never stored. The plan
   already glosses J-13 that narrow way: *"a social figure is derived, not stored"*
   (`workplans/valoria_master_workplan_v9_part5.md:433`) [CHECKED-3]. Which reading Jordan meant is
   the real question of J-T1 (§3.4).
6. **The demand side is measured from the verb table.** The idealized master verb table (§3A,
   `_part2`) has **65 rows** under one inclusion rule (§3A.1): 45 shipped (37 resolvable, 8 not), 12
   planned in v9, 7 in stub code outside the loop, 1 design-only. In four seeded realm seasons, 25
   verbs executed and 35 were attempted [RAN, §10 probe 6]. **In code the season loop runs, exactly
   one verb reads a personal input:** `tell` reads one `capability` key (the teller's as pool, the
   hearer's ÷ 2 as Ob). `fight`/`accept` read the body band, which is live state and is not counted
   (the rule above). Read as complete systems, the stubs read all nine registry attributes, a
   per-domain practice ("History"), Thread Sensitivity, a combat temperament, a threadwork
   resilience and a combat kit (`weapon`, `armor`). Each of the nine has at least one T2 reader;
   Charisma's only one is `derive_command`. None of the nine has a T1 reader (§3.2). **Jordan's
   2026-09-05 ruling is five words, *"ignore their use of attributes"*, and what they strike is one
   source table's pool column** (`proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:462-467`)
   [CHECKED]. The sentence that gives the dice to `capability` is the proceedings design author's,
   not Jordan's, and it covers that design's five inquiry rows (`:473-476`) [CHECKED]; `thread_read`
   has no row there. The design is listed as ratified as intent (`_part8.md:202`) [CHECKED] while its
   own Status line says *"superseded in part by 21"* (`04_VERBS.md:3`) [CHECKED], so its tier is
   contestable (§3.1.1). Read so, the fieldwork design's attribute column is overridden for the five
   and not for `thread_read`, and **Recall has no reader in any source above T4** (J-T2, §3.2).
7. **The rest of the template is valid under either option.** Identity, placement, wants, values,
   ties, office, age and body do not depend on J-T1. The loader (§4) is written so the attribute
   block is the only part whose schema the ruling selects.
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
| **what it is in code today** | not one thing. Spread over `references/npc_registry.yaml` (name, faction, pursuits, affiliations, title), `engine/season/npcs.yaml` (institution, home, want, concerns), `engine/season/offices.yaml` (holder, obligees) and, in corpus worlds only, a case's `cast:` overlay (`capability`) | `rosters.yaml: role_templates`: six templates in `values:`, five of them assigned across six factions in `by_faction:` (Varfell and Löwenritter share `military-order`), and `intelligence-diplomatic` claimed by none (`engine/season/rosters.yaml:1425-1465`, the lists at `:1446-1465`) [CHECKED-2]; `Guilds` and `Schoenland` have none | `engine/season/cohorts.yaml` rows `{rung, weight}`, schema-checked by `cohort_rows` (`engine/season/harness/populated.py:335-385`) [CHECKED-draft] |
| **where it is seated** | `build_realm`'s cast loop (`populated.py:864-896`) [CHECKED-draft]; corpus worlds: `build_at` (`engine/season/harness/corpus_run.py:536-539`) [CHECKED-draft] | never seated on a person: it is a comparison target | `seat_cohorts` mints `Person(pid, name, weight=wt)` (`populated.py:439`) [CHECKED-draft] |
| **what reads it** | the readers in §2, field by field | `cast.loyalty` (`engine/season/data/cast.py:323-364`) [CHECKED-draft] turns the cosine between a member's pursuits and the template into a 0–100 loyalty; `stance_from_loyalty` (`cast.py:376-396`) turns that into one stance row, appended at build (`populated.py:1047-1049`) [CHECKED-draft] | `world_q.subsistence_draw` and `population` read `weight` (named in H-170's `site:`, `engine/season/hole_register.yaml:3722`) [CHECKED-2: the row; the readers not opened] |
| **what it must not become** | a second home for a faction's expectations or a population's size | a per-person field: a role template is a property of the faction, not of the office or the person (`rosters.yaml:1449-1452`) [CHECKED-draft] | a carrier of a named person's facts: a cohort *"traces to no case, so it carries none of"* the cast's fields (`populated.py:369`) [CHECKED-draft] |

**What the character template is NOT.**

- **Not a creation act.** IN-47's review found creation arm C1 *"cannot be carried out through the
  cast shape (no `pursuits` key; `corpus_run.py` `CAST_KEYS` is closed)"* and took its own fallback,
  *"the player picks a person the builder already seated"* (`valoria_master_workplan_v9_part4.md:41`)
  [CHECKED-3]. The template is the shape C1 lacked, so a creation screen (K-GO-8) COULD write a template
  row for world-gen to seat. That is a precondition for C1, not C1; whether C1 is taken is IN-47's
  held review, which only Jordan releases (J-T7, §8).
- **Not a progression system.** A template seeds tick 0. Change after tick 0 is the verbs' work
  (`train` at IN-12 step 9; `_scar_witnesses`; the bodies pass). §2 names each field's live writer.
- **Not a stat block for display.** A field with a carrier and no reader that moves an outcome is
  marked so in §2, not kept for show.
- **Not the troop stock.** What a raised troop is, is that proposal's open **J-1** (its §2.4, which
  reads at this pass *"The troop body under the pool: the candidates and their full footprint
  (J-1)"*) [CHECKED, by heading]. Its default there is **A, a troop stock on the settlement rung**,
  which mints no `Person`, and whose grade is a matter kind on the rung's stores (its §2.7, *"Troop
  kind and grade"*) [CHECKED, by heading]; its alternative **P** is a company `Person` (its `_part2`
  §4.8). The design is PROPOSED (its Status line) [CHECKED]. The character template authors
  no troops under either. It authors the commanders whose qualities the order of battle reads (§9).

**Where the closed cast comes from.** ED-WR-0011, ruled 2026-09-13: *"World-gen NPC count, for now,
is just the 46 NPCs we built"*, option A, *"A CLOSED AUTHORED CAST"*
(`registers/editorial_ledger_wr_archive.jsonl:14`) [CHECKED-2]. The same entry calls itself
*"PROVISIONAL BY ITS OWN TERMS"*: *"a future session may not treat 46 as canon"*. So the template
has one row per cast case **for as long as that ruling stands** (46 today), and its loader reads the
count from the cast, never from a constant. A person CENSUS mints mid-campaign gets no template and
seats on defaults (`engine/season/loop/census.py:105`) [CHECKED-draft].

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
→ `13` [RAN]. The class is at `engine/season/state/carriers.py:642-721`; its docstring is *"S9. A
COHORT IS A PERSON AT weight > 1. ONE CLASS (S9.1)."* (`:644`) [CHECKED-3].

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
| F11 | obligations sworn | an `oblige` Tenure, minted from `offices.yaml` `obligees:` (`populated.py:1314-1328`) [CHECKED-draft], with no term (`offices.yaml:128`) [CHECKED-2] | four readers [CHECKED-2]: `purview_reaches`' oblige clause widens a seat's purview to the grounds its sworn (not `imposed`) obligees' seats reach (`engine/season/state/gate.py:355-370`, through `sworn_to`, `:384-393`); `world_q.establishment_of` (`queries/world_q.py:1534`), read by `epistemic.py:541` [body not opened]; `_req_oblige` clause 4, one edge per person and seat (`loop/predicates.py:394-395`); the renewal walk on a `transfer` (`loop/effects_economy.py:302-305`), which reads termed edges only, so not the two seeded ones. `faction_q.superiors` (`:194-196`) has a test caller and no production caller | **authored**: 2 `oblige` Tenures at build [RAN, §10 probe 3], from two rows that name an obligee: `offices.yaml:191` (NPC-070) and `:591` (NPC-041) [CHECKED-2] | OPTIONS (a seat holder's purview) | a seat whose holder has a sworn obligee, against the same seat with the `obligees:` row emptied: `purview_reaches` over the obligee's ground differs. Not run here; `engine/season/tests/test_fa04_oblige_purview.py` covers the NPC-070 edge [file named, not run] |
| F12 | known claims at tick 0 | `Person.ledger` (`carriers.py:657`) | `LedgerReader` (`person_q.py:662`) and the question sources read a person's own claims [CHECKED-2: the class] | **null**: probe [RAN, §10 probe 3], 0 of 46 cast hold a claim at build | CHOICE · MEMORY | two persons, one seeded with a claim about X: only he forms candidates on X in season 1 |
| F13 | birth tick (age) | `Person.born` (`carriers.py:675`) | `age_of` → `body_hazard` (`world_q.py:771-790`) [CHECKED-draft]; **dark**: `age_step` and `illness_rate` ship 0 (`fixtures.py:542-544`) [CHECKED-draft] | **defaulted**: `born = -age_at_build = 0` on all 83 realm persons [RAN, §10 probe 1]. Registry `age`: present on 29, non-null on 0 | COST (death hazard) once armed | two persons differing only in `born`, `age_step` > 0: different death draws over N seeds. At the shipped 0, identical |
| F14 | body | `Person.body` (`carriers.py:667`), default `condition_scale` 1000 | `body_band_penalty` → scenes (`budget.py:64-76`) and combat `end` (`engine/season/seam/wrappers/combat.py:130-138`) [CHECKED-2] | **defaulted**: 1000 on all 83 [RAN, §10 probe 1]. Live state, written every season, so NOT a personal input (the rule under "Words"); the template authors only its tick-0 value | COST (scenes) · ODDS (combat) | probe [RAN, §10 probe 4]: `party_end` is 4 at body 1000 and 2 at body 100 |
| F15 | practice (`capability`) | `Person.capability` (`carriers.py:651`) | `sigma._capability` (`engine/season/seam/wrappers/sigma.py:82-94`) → pool (`:97-109`) and, for a person opponent, Ob = score/2 (`:112-129`), reached through `contest_input` (`:132-147`), so by contested verbs only [CHECKED-3]. For `tell` the opponent is the hearer, the row's `counterparty: to`, not the topic (`engine/season/verb_table.yaml:950-951`; `engine/season/loop/resolve.py:740-744`) [CHECKED-3]. `tell` and `speak` map to `copying` (`rosters.yaml:1106-1107`) [CHECKED-3]; only `tell` declares `contests:` (`verb_table.yaml:953`) [CHECKED-3], so `speak`'s mapping reaches nothing | **null**: empty on 46/46 cast, 83/83 realm persons [RAN, §10 probe 1] | ODDS | probe [RAN, §10 probe 4]: `tell` pool 2 with `{}` and 5 with `{copying: 5}`; Ob 2.0 against the first (that is `obstacle_default`, since he brings no key) and 2.5 against the second |
| F16 | the ruled attributes | **not carried**: no `Person` field. The roster ships nine, scale 1–7, default 1, *"the tenth is UNNAMED"* (`references/descriptor_registry.yaml:27-48`) [CHECKED-draft]; exported as `ATTRIBUTES` (`engine/substrate/descriptors.py:50-51`) [CHECKED-draft] | **none in the season loop**: `ATTRIBUTES` has no importer in `engine/`, `modules/`, `systems/` or `tools/`; one test reads it (§10 probe 5) [RAN]. T2 readers exist under aliases (§3.2) | **not carried** (the file holds it: registry `stats:` present on 29, non-null on 1, NPC-001: `cognition 5, focus 5, endurance 4, social '3–4'`; nothing seats it) | ODDS · COST · EFFECT (once read) | §3 |
| F17 | Thread Sensitivity; Coherence | **not carried**. `(Person, coherence)` has a write-matrix row (`engine/season/write_matrix.yaml:171-172`) [CHECKED-draft] and no field | **none in the loop**. T2: the thread pool reads `ts` (`systems/threadwork/sim/operations.py:235-247`) [CHECKED-3] and the knot's party gate reads it (`systems/fieldwork/sim/knots.py:195-198`) [CHECKED-2]. T3: K-3 types `thread_read`'s TS precondition (RATIFIED AS INTENT, `_part8.md:207`) [CHECKED-3]. T4: `examine`'s Buried depth, *"Buried (3) if TS ≥ 10"* (`.designs/systems/fieldwork/reference/fieldwork_v30.md:301`) [CHECKED-3] | **not carried** (the file holds it: registry `ts` present on 32, non-null on 10, of which 8 are integers and 2 are prose, `'75–80'`, `'~50'` [RAN]; nothing seats it) | ODDS · GATE · COST (once read) | §3.1 row CD5 |
| F18 | kit (weapon, armour, techniques) and retinue | **not carried** on a person | **none in the loop**. T2: `Combatant(…, weapon='arming', armor='light', skills, equipped, tradition)` (`modules/combat/combatant.py:93-94`) [CHECKED-2] | **not carried** | ODDS · EFFECT (once read) | §3.1 row CD2 |
| F19 | temperament; per-person scar thresholds | **not carried**. The scar thresholds are ruled constants, 2 and 3 (`person_q.py:468-469`, ED-IN-0261) [CHECKED-draft] | T2: combat `disp`, a lean of `(disp-4)/3` (`modules/combat/combat_systems.py:183`) [CHECKED-draft]. The scar COUNT itself is live: `Person.scar` (`carriers.py:686`) | **not carried** (a scar is history, not template: it starts empty by design) | CHOICE (combat aggression, once read) | per-person thresholds: **none offered**, since a per-person threshold would overwrite a ruled constant. Temperament: §3.1 row CD2 |
| F20 | kin and lineage | **not carried**. The Tenure kinds are `hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban` (`rosters.yaml:101`; values read with `yaml.safe_load`); none is kin. An heir is a TITLE, not kin (RS-27, RS-29; J-T3) | **none** | **not carried** | — | none possible today: J-T3 (§8) |
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
controls). Not carried, with readers only in T2 stub code or T3/T4 designs: F16, F17, F18. Not
carried, with no reader: F9.

**A correction carried from the lane critics.** The NPC lane draft said every mechanism that changes
a person ships at its control. The critic contradicted it (scratch `critics/NPC.md`, item 1) and the
critic is right. Regard moves live: `judged_gain` and `told_valence_gain` ship at 0.5
(`fixtures.py:748`, `:750`) [CHECKED-draft]. The stance term's weight ships at 1 (`stance_gain`,
`:773`) [CHECKED-draft]. Four realm seasons at seed 0, each surviving person's fields compared with
build [RAN, §10 probe 2]: body moved on 4 persons. 27 persons held a non-empty scar. Stored `stance`,
`pursuits`, `conviction` and `capability` moved on none. What ships static, then, is VALUES
(pursuits and convictions: the scar counts, but the threshold-2 shift is at 0 and no crisis fired in
four seasons), PRACTICE (no writer) and AGE (dark). Body moves. Regard moves at read, and the ledger
moves at every deposit.

---

## 3. THE PERSONAL-INPUT BLOCK, WRITTEN BOTH WAYS

Jordan: *"I don't know how to reconcile attributes against the subsystems and office training and
histories"*; *"I don't know what attributes should even exist or what each subsystem best needs"*.
So the block starts from DEMAND: what each resolver would read from a person if its system were
complete (§3.1). It groups that demand into personal inputs (§3.2), states one reconciliation rule
that obeys the plan's standing rule V-2 (§3.3), reads the two rulings against each other (§3.4), and
only then drafts the options (§3.5–§3.7). The full evidence, verb by verb, is §3A in
[`_part2`](2026-10-16-character-template_part2.md).

### 3.1 The demand table: what each resolver reads from a person

Code-stub rows (T1/T2) and prose-only rows (T3/T4) are kept in separate tables. Column (a) is what
the season loop reads TODAY (T1). Column (b) is what the resolver reads WHEN COMPLETE, with its
source and tier. The codes are §3A's (STR AGI END FOC ACU WIL ATT CHA BON are the registry's nine;
PRA practice per domain; TS Thread Sensitivity; TMP temperament; RES resilience; REC Recall; KIT
what a person carries). The *lane ref* column holds `research/by_lane/` ids only, or **none** where
a grep of that suite found no row naming the demand.

**Code rows.**

| # | resolver | (a) reads TODAY (T1) | (b) reads WHEN COMPLETE (source, tier) | inputs (from b) | lane ref |
|---|---|---|---|---|---|
| CD1 | the contested social roll (`tell`; any verb routed to the sigma roll) | for `tell`: one `capability` key, `copying`, as pool; the HEARER's same key ÷ 2 as Ob: the opponent is the row's `counterparty: to`, *"not its topic"* (`sigma.py:97-129`, through `contest_input`, `:132-147`; `verb_table.yaml:950-951`; `loop/resolve.py:740-744`) [CHECKED-3]. For `speak`: **nothing**: it declares no `contests:` (`verb_table.yaml:875-885`) [CHECKED-2], so its `copying` mapping (`rosters.yaml:1107`) [CHECKED-3] is never reached | the contest kernel's `Contestant(faculty, …, charisma)` (`systems/social_contest/sim/contest/resolver.py:184-195`) [CHECKED-2]: `faculty` → pool and leverage (`:300-301`) [CHECKED-2] — **T2**, a kernel the sibling proposal calls *"retiring"*, with attributes *"none bound"* (`proposals/2026-09-30-character-and-play-surface/10_verbs_and_attributes.md:144`) [CHECKED-3] — **T4**. `charisma` moves no outcome: Charisma is *"a BUILD-TIME attribute (in player control), used only to derive Face_current's ceiling"* (`resolver.py:191-192`) [CHECKED-3], and the derived Face leaves Standing, Readiness and leak *"bit-identical either way"* (`resolver.py:226-229`; `primitives.py:128-131`) [CHECKED-2]. The quarantined v30 contest design's attribute reads (Appraise *"Attunement + Recall"*, Concentration *"(3 × Focus) + (2 × Spirit)"*; `social_contest_v30.md:155`, `:267`) [CHECKED-3, by grep] are superseded by that kernel and are not counted | PRA | K-SC-2, M-NPC-1, K-IN-1 |
| CD2 | personal combat (`fight`, `accept`) | `end` only, from the body band (`seam/wrappers/combat.py:129-138`) [CHECKED-2]; every other field the class default (`modules/combat/fight.py:45`) [CHECKED-2] | every `Combatant` field: `strength, agi, end, cog, att, spirit, focus, history, disp, weapon, armor, skills, equipped, tradition` (`combatant.py:93-94`) [CHECKED-2], read through the bout's per-beat terms (§3A.4) — **T2** | STR AGI END FOC ACU WIL ATT, PRA (`history`), TMP (`disp`), KIT | M-PC-1, K-PC-1 (K-1 is a plan position under PC-06, not a lane ref, so it is not listed here) |
| CD3 | a field's commander (`march`; the reform, recall and feint checks and the span check inside it) | the side's members' `weight`, stance and loyalty; no commander (`mass_battle.py:175-200`) [CHECKED-draft] | `Officer(name, command=4, charisma, cognition)`, which derives `command` from the two while `COMMAND_SIGMA_ENABLED` (default on) (`units.py:2700-2722`; `exchange.py:57-66`; `config.py:530`) [CHECKED-2], clamped to 1–7 (`exchange.py:54`, `:65`) [CHECKED-3] — **T2**. **At the defaults Command is not in the exchange pool**: `POOL_QUALITY_MODEL` is on (`config.py:556`) and *"Command is absent from this branch entirely"* (`exchange.py:103-126`) [CHECKED-2]. A derived Command reaches the reform gate, the recall and feint rolls, the morale-erosion divisors, `h_per_size` and the span of control (§3A.4). It cannot reach yield eligibility or rout at Command 0, because a derived Command is never below 1 (§3A.4). The troop design names the season's general and officers from the persons present, and holds every season commander's Command at the constant 4 *"until R-C-1 names a source"* (its `_part2` §4.2, "What a side is: an order of battle", steps 4–7) [CHECKED-3, by heading] — **T4** | CHA, ACU | M-MB-3, M-NPC-13, K-MB-2 |
| CD4 | a field's troop quality | none: a side is one Line at fixed quality (JORDAN_STATEMENTS 3: *"a stub"*) | per-subunit `power, discipline, morale, dr` (`units.py:553-557`) [CHECKED-draft] — **T2**; under the troop design's J-1 default, a troop stock's grade, a matter kind on the settlement rung with discipline and morale offsets (its §2.7, *"Troop kind and grade"*) [CHECKED, by heading and its first bullet] — **T4** | **none on a character** | M-MB-2, M-MB-16 |
| CD5 | threadwork (the 7 operations) | none: no TS carrier | `spirit × 2 + min(3, history + 3) + ts // 10` (`operations.py:235-247`) [CHECKED-3]; `resilience` resists the Coherence cost, at a shipped gain of 0 that returns *"before the attribute is read"* (`:157`, `:249-274`) [CHECKED] — **T2**. **Mending never reads `resilience`**: its cost is 0 at every degree (`MENDING_COHERENCE_COST`, `:451`; exempt from the Partial/Failure −1, `:316-323`; passed at `:567-569`), and `resist_coherence_cost` returns a cost ≥ 0 before reading the attribute (`:260`, `:269`) [CHECKED]. Leap's base cost is 0 (`:364`, `:372`), so it reaches RES only through the −1 on a Partial or Failure [CHECKED] | WIL, PRA (`history`), TS; RES on six of the seven (not Mending) | M-WR-1, K-WR-2 |
| CD6 | knots (`tie / knot`, through `form_knot`) | none: the row has no effect (H-182) | `bonds ≥ 5` (`knots.py:185-187`); a disposition ≥ 5, a stance not an input (`:189-193`); either party `ts ≥ 30` (`:195-198`); a cap of `bonds // 2 + 1` knots (`:200-203`); then the roll `spirit × 2 + history_relationships`, TN 7 (`:212-222`) [CHECKED-2] — **T2** | BON (gate, cap), TS (gate), WIL, PRA (roll) | K-NPC-6 (kinship as a tie kind, `research/by_lane/NPC_npc_cast.md:516`) [CHECKED-3] bears on the row; no lane row names the knot's inputs |
| CD7 | the scene budget (every verb) | body bands, live `hold` count, travel legs (`budget.py:57-61`) [CHECKED-draft] | the same: the directions are #353's, *"not open"* (`budget.py:46-47`) [CHECKED-draft] — **T1** | **none**: BODY and OFF, both excluded by the rule | none |
| CD8 | the chooser (every verb) | pursuits through `crisis_weights`, the confliction damp, the stance term (`engine/season/decision/choose.py:115-127`) [CHECKED-draft] | the same, plus the refusal axis (H-146, unarmed) and a self-interest weight (M-NPC-12) — **T3** | **none**: values, not inputs | M-NPC-3, M-NPC-12 |
| CD9 | the bodies pass (age, illness) | `born`, rates at 0 (`world_q.py:771-790`) [CHECKED-draft] | the same with rates set (H-208) — **T1 dark** | **none**: age | M-NPC-3 |

**Prose-only rows (no code reads these yet).**

| # | demand | (b) WHEN COMPLETE (source, tier) | inputs | lane ref |
|---|---|---|---|---|
| PD1a | the six inquiry acts (`examine`, `interview`, `research`, `surveil`, `reconstruct`, `thread_read`) | **Jordan's words, 2026-09-05, are five:** *"ignore their use of attributes"*, striking the source table's pool column (`proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:462-467`) [CHECKED]. **The rest is the design author's sentence, not Jordan's:** *"What is taken from the pool column is nothing. Every row below therefore says what it contests and not what it contests with; `capability` supplies the dice, its keys are content by `ID-12`"* (`:473-476`) [CHECKED], scoped to *"every row below"*, the five rows of §B.3.2 (`:487`, the rows at `:528-581`) [CHECKED]. Tier: **T3 if** the design is read as the plan lists it, RATIFIED AS INTENT (`workplans/valoria_master_workplan_v9_part8.md:202`) [CHECKED]; its own Status line says *"00–20 reference, superseded in part by 21"* (`04_VERBS.md:3`) [CHECKED], so the tier is **contestable** (§3.1.1). For the five: PRA, as the design author states (T3, contestable). **For `thread_read`: no statement.** It has no row in §B.3.2 (the design registers its precondition rather than writing it: *"The sixth is not, and is registered rather than forced"*, `:485`; its §B.3.1 cell is `contests: —`, `:460`) [CHECKED]; that it rolls `capability` is this proposal's **inference**, and does not override the fieldwork design's pool, *"(Spirit × 2) + History + TPS"* (`fieldwork_v30.md:305`, `:351`) [CHECKED] (T4), which therefore stands: WIL, PRA (History), TS. **TS gates**: K-3 types `thread_read`'s *"TS ≥ 30"* precondition (T3); `examine` reaches the Buried depth *"if TS ≥ 10"* (`fieldwork_v30.md:301`) [CHECKED] (T4). **Overridden for the five, and recorded:** the fieldwork *"Primary Attribute"* column, Cognition for Examine and Surveil, Attunement for Interview, Recall for Research and Reconstruct (`fieldwork_v30.md:299-306`) [CHECKED] (T4), restated by the sibling proposal (`10_verbs_and_attributes.md:145`) [CHECKED] (T4). **Open, not counted:** the fieldwork concealment pool, *"(Cognition × 2) + relevant History"*, rolled by the CONCEALING party, sets a Concealment Ob that *"each investigation action faces"* (`fieldwork_v30.md:361-363`) [CHECKED] (T4): a DIFFICULTY read of the opponent on all six, which the shipped row's note also records (*"canon makes ALL SIX contestable"*, `verb_table.yaml:1085`) [CHECKED] while the live roster says the six are *"not a contest"* (`rosters.yaml:1051`, `:1074-1077`) [CHECKED] | PRA (all six: five T3, `thread_read` T4); WIL (`thread_read`, T4); TS (`thread_read` gate T3 and pool T4; `examine` gate T4) | M-FI-3, K-FI-1 |
| PD1b | AX-7's competence, at EVERY deposit | AX-7: divergence turns on *"the channel …, the reader's competence, and their prior beliefs … all three together"* (`01_AXIOMS.md:288-289`) [CHECKED-draft] — **T3**. The factor sits in `refracted_confidence`, which runs for every claim landing in any ledger, not only for inquiry verbs; it is 1, unbuilt (`options.py:1198-1211`; H-200) [CHECKED-2]. No stub reads it | **open**: no source names the input behind a reader's competence at deposit. The 2026-08-15 proposal groups ACU and ATT as *"Perception {Cognition, Attunement}"* (`2026-08-15-…-progression.md:112`) [CHECKED-3] — **T4**, a grouping, not a mapping. V-2 binds verbs, not deposits, so it neither admits nor bars an attribute here | M-FI-3, K-FI-1 |
| PD2 | governance and administration (a governor, a settlement's seat) | the 2026-08-15 proposal's role table: *"Governor — position — AP × compliance + Ledger — and a settlement"*, pool *"administrative practice"* (`:147`, `:170`) [CHECKED-2] — **T4**; no `systems/settlements/sim/` exists (`ls` printed nothing) | PRA (administration); OFF is named and not counted | none: a grep of `research/by_lane/` for administration and governor rows found M-FA-2 (delegation beside a living principal, `FA_faction_actions.md:366`) [CHECKED-3, the row's first line], which is about who governs, not what a governor brings |
| PD3 | the persuasion actor and standing | the session's upload extracts (scratch `out/UP24_standing_persuasion_actor.md:41-42, :76, :106`; `out/UP07_critique_standing_persuasion.md:20`) — **T4, scratch, the uploads themselves not opened**: standing in four regimes (*"A1 ascribed, A2 accumulated, A3 performed, A4 staged"*); *"trainability belongs to the environment"*; political skill measured as *"networking, influence, apparent sincerity"*, while *"social astuteness did not"* predict; charisma tactics trained (UP24 `:53`) | PRA (per proceeding), CHA; standing derived from office and record, **not** an attribute | K-SC-2 |
| PD4 | inquiry as access | the upload extract `out/UP17_mechanics_of_inquiry.md:93` — *"P29 Background flag … P30 Attribute voice"* — **T4, scratch** | PRA (a background as an access flag) | M-FI-3 |
| PD5 | breadth of what a person may hold | the 2026-08-15 census's *"Recall — how many Histories you may hold active and how fast you learn"*, in a class it calls *"Capacities (gate, never roll)"* (`:124-125`, `:202`) [CHECKED-3], and its census row *"CAPACITY, not attribute — equip slots + learning rate; never rolled"* (`:475`) [CHECKED-3] — **T4**. No source above T4 reads Recall (§3.1.1) | REC | none |

#### 3.1.1 What *"ignore their use of attributes"* governs — decided here, with the reasoning

- **Jordan's words, and only those.** Five words, *"ignore their use of attributes"*, recorded in the
  proceedings design under *"THE POOL COLUMN IS NOT ADOPTED — RULED BY JORDAN, 2026-09-05"*
  (`04_VERBS.md:465-466`) [CHECKED]. *"Their"* is the source table's: the design took the six acts'
  NAME, PRODUCT and COST from `08_FUNCTION_SURFACE.md` §3.3 (citing KTI) and struck that table's
  fifth column, a pool per act (`04_VERBS.md:448-467`) [CHECKED]; that column gave Thread-Read
  *"Thread Pool + Attunement"* (`proposals/2026-08-31-unified-code-shape/08_FUNCTION_SURFACE.md:164`)
  [CHECKED]. The fieldwork §4.2 column is a different source table, and Jordan's words do not name it.
- **The design author's sentences, which are not Jordan's.** The vocabulary the pool column used,
  *"Acuity · Charisma · Attunement · Focus · Agility · Will · Thread Pool"*, and the ground, a roster
  *"not settled"* (`:466-471`) [CHECKED], are the author's gloss on the ruling. So is the operative
  sentence: *"Every row below therefore says what it contests and not what it contests with;
  `capability` supplies the dice"* (`:473-476`) [CHECKED]. Its scope is *"every row below"*: the five
  rows of §B.3.2 (`:487`, `:528-581`) [CHECKED]. Thread-Read has none (its precondition is
  *"registered rather than forced"*, `:485`; its §B.3.1 cell is `contests: —`, `:460`) [CHECKED].
  And the sentence assumes the five are contests (each row carries a `contests:` value), which the
  live roster rejects: investigation is *"ITS OWN KIND — not a contest"*, its seam UNRULED, *"The
  blanks are Jordan questions"* (`engine/season/rosters.yaml:1051`, `:1056-1060`) [CHECKED], and
  *"INVESTIGATION MUST NOT BE MADE A CONTEST TO BECOME GRADEABLE"* (`:1074-1077`) [CHECKED]; the
  ratified verb-coverage suite says the same, *"investigation, ruled not a contest"*
  (`proposals/2026-10-03-verb-coverage-and-gap-fill.md:378`) [CHECKED].
- **The tier is contestable.** The plan lists `04_VERBS.md` among the three files RATIFIED AS INTENT
  (`_part8.md:202`) [CHECKED]; the same row, and the file's own Status line, say *"00–20 reference,
  superseded in part by 21"* (`04_VERBS.md:3`) [CHECKED], and `04` is numbered inside 00–20. This
  proposal reads it as T3, because the plan's row names the file explicitly, which is the more
  specific clause. Read the other way (T4), the design author's sentence and the fieldwork column
  meet at equal tier, and by the equal-tier rule (head, "Evidence tiers") the five acts' dice become
  **open**; that recount is not made here.
- **So, as counted here.** `examine`, `interview`, `research`, `surveil`, `reconstruct`: PRA, from
  the design author's sentence (T3, contestable). The fieldwork attribute column for those five is
  overridden by it. **`thread_read`: no T3 source states its dice.** That it rolls `capability` is
  an **inference** from the ruling's evident intent, and under the rule on inferences (head,
  "Evidence tiers") it overrides nothing: the fieldwork pool, *"(Spirit × 2) + History + TPS"*
  (`fieldwork_v30.md:305`, `:351`) [CHECKED] (T4), stands, and `thread_read` reads WIL, PRA and TS.
  **TS gates survive**, on a narrower ground than the third pass gave: the struck vocabulary
  includes *"Thread Pool"* (`04_VERBS.md:466`) [CHECKED], the TS-derived pool term
  (`floor(TS / 10)`), so the ruling reached a TS-derived POOL term in its own table; a GATE on TS
  (`thread_read` ≥ 30, K-3; `examine` ≥ 10) is not a pool term, and no source says the ruling
  reaches it.
- **What it does not settle.** The author's ground is conditional: a roster *"not settled"*. Under
  Option B, once J-T2 names the tenth, that ground lapses, but Jordan's words do not. Whether
  attributes may then reach the inquiry acts is not answered by any source; it is listed as a B open
  cell (§3.7) and asked with J-T1. V-2 would admit an attribute only on a row with `contests:`; the
  shipped rows *"declare no `contests:`, no obstacle column and no roll"*
  (`verb_table.yaml:1040-1047`) [CHECKED-3], and the roster forbids making them contests (above). So
  even with a settled roster, an attribute reaches an inquiry act only if Jordan amends V-2 or rules
  their seam a contest. (This bars WIL from `thread_read` under B as well: the row declares no
  `contests:`.)
- **Effect on the counts** (§3A.3): `examine` reads PRA and TS; `interview`, `research`, `surveil`,
  `reconstruct` read PRA (were ATT, REC, ACU, REC); `thread_read` reads WIL, PRA and TS (the third
  pass's override of its WIL rested on the inference and is withdrawn). With the fourth pass's other
  corrections (`speak` open, `determine` sigma-routed at T3), the buckets are **11 / 2 / 9 / 43**
  (§3A.3 shows every step from the third pass's 10 / 3 / 10 / 42).
- **Effect on J-T2 (Recall).** Recall's only readers were the fieldwork design's `research` and
  `reconstruct`, which the design author's sentence overrides for those rows, and the v30 contest
  design's Appraise pool, superseded by the kernel (CD1). The *"+2D Recall bonus"* the fieldwork
  design names (`fieldwork_v30.md:108`, `:327`) [CHECKED] is classed by the contest design as a
  *"non-attribute"* bonus (`social_contest_v30.md:97`) [CHECKED], *"Binary"*, for citing a named,
  verifiable claim (`:177`) [CHECKED]; but the same design also says *"Recall contributes to the
  Appraise pool and the citation bonus"* (`:155`) [CHECKED], so it is internally inconsistent on
  whether the bonus reads Recall. Either way it is T4, and the contest it belongs to is superseded by
  the kernel. **So no source above T4 reads Recall**, and by ID-13 it is not a candidate for the
  tenth unless Jordan gives it a reader. The census's class for it, *"CAPACITY, not attribute …
  never rolled"*, stands unopposed above T4.

**(a) is a strict subset of (b).** Today the loop reads, of any person:

- one PRA key (`copying`, for one verb, `tell`: the teller's and the hearer's);
- BODY (live state, not counted);
- `weight`;
- stance and values;
- person-held quantities: his own ledger (`tell`, `comply`, `survey`, `reconstruct`), a Record he
  holds (`give`), his `weight` against a destination's room (`migrate`) (§3A.2.1) [CHECKED-2].

It reads none of the nine attributes, no TS, no TMP, no RES, no REC and no KIT. Every personal
input below is a column (b) demand.

### 3.2 The personal inputs the demand implies

**The glance table** (resolver | when-complete reads | inputs | tier):

| resolver | when complete it reads | inputs | tier |
|---|---|---|---|
| social contest roll | faculty (charisma derives a view that moves nothing) | PRA | T2 (a retiring kernel) |
| personal combat | 9 attributes' aliases, history, disp, kit | STR AGI END FOC ACU WIL ATT, PRA, TMP, KIT | T2 |
| commander | charisma, cognition → Command → gates, rolls, divisors, span (not the default exchange pool) | CHA, ACU | T2 (+T4 wiring) |
| troop quality | power, discipline, morale; a troop stock's grade | none on a character | T2 / T4 |
| threadwork operations | spirit, history, ts; resilience on six of the seven (Mending's cost is 0, so it never reads it) | WIL, PRA, TS; RES (not Mending) | T2 |
| `thread_read` | the fieldwork Leap pool `(Spirit × 2) + History + TPS`, which no stated source above T4 overrides; TS gate | WIL, PRA, TS | T4 (+T3 gate, K-3) |
| knots | bonds (gate, cap), ts (party gate), spirit and history (roll) | BON, TS, WIL, PRA | T2 |
| the five inquiry verbs | `capability` dice (the proceedings design author's sentence); TS for `examine`'s depth | PRA; TS | T3, contestable (+T4 gate) |
| sigma-routed verbs of the ratified suite (`determine`, `arrest`, `argue`, `interrogate`) | `capability` dice through the sigma roll | PRA | T3 |
| `speak` | **open**: contested at T3 in two sources, uncontested at T3 in a third (§3A row 32) | none counted | T3 conflict |
| competence at deposit | competence | **open** | T3 |
| administration | administrative practice | PRA | T4 |
| persuasion actor | practice, charisma, standing | PRA, CHA | T4, scratch |

**Clustered.** Read from column (b), the demand falls into four groups:

1. **Nine attributes, every one with a T2 reader.** These are exactly the registry's nine
   (`references/descriptor_registry.yaml:36-48`) [CHECKED-2], under the aliases the stubs spell:
   - **Body**: STR (combat impact, health, balance), AGI (tempo, reflex, balance, initiative),
     END (wounds, stamina).
   - **Mind**: ACU = `cog` (combat reading; Command), FOC (poise recovery, disruption resistance),
     WIL = `spirit` (wounds, stamina; the thread pool; the knot roll; `thread_read`'s Leap pool at
     T4).
   - **Social**: ATT = `att` (combat reading, reflex), CHA (Command only: its contest Face view
     moves no outcome, §3A.4), BON (the knot's gate and cap).

   **No attribute in the nine is left without a reader** (ID-13 holds at T2). **CHA is the
   thinnest**: one T2 reader, `derive_command`. At T4 the fieldwork design also rolls Charisma for
   three social actions and a cover identity and sets Composure from it (`fieldwork_v30.md:409`,
   `:411-412`, `:577`, `:620`, `:640`) [CHECKED-3]; none of those is a verb row (§3A.1's sixth
   exclusion class), so none is counted. **None of the nine has a T1 reader**, so ID-13 does not yet
   hold in the game.
2. **PRA, one key per domain.** Contest faculty, combat `history`, thread `history`, knot
   `history_relationships`, `copying`, the inquiry dice, administration, command practice. It is read
   by CD1, CD2, CD5, CD6, PD1a, PD2, PD3 and PD4. It is what training writes. **It is a family of keys,
   not one input**, so it cannot fill one roster slot (§3A.4.1).
3. **Further personal inputs outside the nine:**
   - **TS**: a practitioner stat on its own 0–100 scale (`descriptor_registry.yaml:61-65`)
     [CHECKED-2]. Read in the thread pool and the knot's party gate (T2), as `thread_read`'s gate
     (T3) and in its Leap pool (T4), and as `examine`'s depth gate (T4). Not single-subsystem.
   - **TMP**: combat's `disp`, a 1–7 lean (T2).
   - **RES** (`resilience`): threadwork's R-14 input, a per-actor integer that resists the Coherence
     cost, dark at the shipped gain 0 (`operations.py:157`, `:249-274`) [CHECKED] (T2). Read by six
     of the seven operations: Mending's cost is 0, so `resist_coherence_cost` returns before reading
     it (`:260`, `:269`, `:316-323`) [CHECKED]. The plan names *"'spirit' (resilience, R-14)"* as
     *"a candidate input only"* for the tenth (`_part5.md:444`) [CHECKED-3].
   - **KIT**: what a person carries, `Combatant.weapon`, `armor` (T2). It has no carrier on a
     person (F18), and IS counted, because a resolver reads it per person. The troop design keeps a
     levy's kit in the settlement rung's stores, *"Kit is the town's"* (its §2.7) [CHECKED, by
     heading and the bullet], and the character-sheet proposal's K-5 proposes `hold` Tenures on
     equipment objects (`09_the_character_sheet.md:132`) [CHECKED-2]. That choice for a person is
     J-T5 (§8).
   - **REC** (Recall): **no reader above T4** (§3.1.1). Kept as a code so the overridden readings
     can be named.
4. **Not personal inputs: OFF, BODY, age, values, weight, held claims and Records.** Each already
   has, or should have, its own carrier.

**How many genuinely distinct inputs.** **Nine storable attributes**, plus **one family of practice
keys**, plus **four further inputs with a T2 reader** (TS, TMP, RES, KIT). REC has none above T4. The
matrix (§3A.3) confirms the nine: every one is read by at least one verb row.

**The ten.** Jordan ruled the COUNT: *"it will be 10 attributes"* (ED-IN-0185 Q7, 2026-08-14,
`registers/editorial_ledger_in_archive.jsonl:137`) [CHECKED-2], in an entry headed *"RULED IN FULL,
2026-08-14. THE AGENDA IS CLOSED; DO NOT RE-RAISE IT."* **No source records him naming them.**

- The registry ships nine, and says *"The TENTH IS UNNAMED … Do not infer the tenth from the
  aliases"* (`descriptor_registry.yaml:27-31`) [CHECKED-2].
- ED-IN-0193 recorded the count, that *"NINE are defined"*, and that *"THE TENTH IS UNNAMED"*; it
  does not list the nine (`editorial_ledger_in_archive.jsonl:145`) [CHECKED-2].
- The plan asks him for the name: *"you have given no name"* (`_part5.md:444`) [CHECKED-3].
- The 2026-08-15 proposal set five roster options side by side (`:191-195`) [CHECKED-3]: A-1, *"Six
  faculties + two capacities"* (Str, Agi, End, Cog, Att, Spi; Recall and Bonds), eight in all, which
  it RECOMMENDED; A-2, *"Ratify the 10 unchanged"*, a ten that includes Recall, Focus and Charisma;
  A-3; A-4, *"The registry's 9 (drop Recall)"*, which it marked REJECT; A-5. (A-4 is an option, not a
  record that the registry "later dropped Recall": the registry's nine already existed.)

**By ID-13, the tenth must have a reader.** The demand offers three candidates with a T2 reader that
are not already among the nine: **TMP, TS, RES** (KIT is a carried thing, not a quality of the
person, so it is not one). **Recall has no reader above T4** once the
2026-09-05 ruling is applied (§3.1.1); the census classes it *"CAPACITY, not attribute — equip slots
+ learning rate; never rolled"* (`2026-08-15-…-progression.md:475`) [CHECKED-3], which the sibling
proposal quotes (`10_verbs_and_attributes.md:154-155`) [CHECKED-3] and reads as *"evidence for D2, not a
candidate for it"* (`:155-156`). Naming the tenth is **J-T2**, Jordan's. This proposal does not pick.

⚠ **Locator correction carried from the research suite.** `00_COMPARATIVE_ANALYSIS.md:78`
(RC-1), `:214` (X-14) and `:528` (J-C-3) cite the ten-attribute ruling as *"[CHECKED p5:515]"*.
The scratch critics (`critics/NPC.md:21`, `critics/COMPARATIVE.md:41`) and the SC lane's K-SC-2 row
cite J-13 at `_part5:504` and `:514`. `wc -l workplans/valoria_master_workplan_v9_part5.md`
→ `475`, so those lines do not exist in this tree. In the tree read here, J-13 is at `_part5.md:433`
(and the §J.2 remainder at `:443`), and the ten-attribute evidence at `:444`.

### 3.3 The reconciliation rule

Jordan's question was how attributes, subsystems, office, training and histories fit together. One
rule, with the ruled-on cell marked. **It obeys two standing rules from the sibling proposal**,
which it did not cite before:

- **V-2**: *"An attribute reaches a verb only through a faculty, and only if the verb's row has
  `contests:`. Record `contests:` for every new verb as the deciding column"*
  (`10_verbs_and_attributes.md:198`) [CHECKED]. The plan carries it as binding on the author of every
  row IN-08 and IN-12 add, and names the rows declaring `contests:` as read 2026-10-06: `fight`
  "the body", `march` "a field", `tell` "a standing" (`workplans/valoria_master_workplan_v9_part7.md:51`)
  [CHECKED] (T3). The shipped table now has four, `accept` added: `:485`, `:610`, `:676` and `tell`'s
  `contests: "a standing"` at `:953` (`engine/season/verb_table.yaml`) [CHECKED].
- **V-3**: `faculty(domain)` is *"the single owner of the aptitude slot"*: *"every pool reads
  `faculty(domain)`; none reads a bare attribute"* (`10_verbs_and_attributes.md:199`) [CHECKED-3]. The
  plan holds it LEAVE until `Person.attributes` exists (`_part7.md:51`) [CHECKED-3]. It restates the
  2026-08-15 proposal's *"no system reads a bare one"* (`:201`) [CHECKED-3] (T4).

```
WHAT IS STORED        Option B: the ten attributes (1-7, closed roster), slow-moving.
                      Option A: nothing attribute-shaped.
                      BOTH:     practice, one key per domain (Person.capability), authored and trained.

WHERE AN ATTRIBUTE    Option B only (V-2, V-3): through faculty(domain) = f(the domain's attributes,
MAY BE READ           practice in that domain), owned ONCE per domain in the resolver's module; and
                      only by a verb whose row declares `contests:`. Today four rows do: fight,
                      accept ("the body"), march ("a field"), tell ("a standing"). tell's kernel
                      binds no attribute, so it admits one only if a domain names it. A gate or cap
                      on a bare attribute (the knot's BON) is outside both rules: proposed
                      amendment V-2a, Jordan's (§3.7).

WHAT TRAINING DOES    `train` (IN-12 step 9) raises PRACTICE: one domain key per act.
                      It never raises an attribute under A (there are none).
                      Under B, whether anything raises an attribute (age, a wound, nothing) is J-T4.

WHAT OFFICE GRANTS    OPTIONS (the remit, carried on the hold Tenure's payload: `granted_acts`),
                      SCENES (`budget_office_bonus` per live hold),
                      a TREASURY (`seat_rung`). Under the troop design, a seat that may raise levies.
                      Never an attribute, never practice. A proceeding MAY rule that an office
                      changes an obstacle; no code does today (the obstacle's owner is the
                      proceedings subsystem, ED-SC-0033 (3), per `sigma.py:122-124`) [CHECKED-3].

WHAT STAYS DERIVED    Every subsystem figure, at read, never stored:
                      the contest pool, every Combatant term, Command, competence,
                      loyalty, regard, age, confliction, standing.
                      (J-13's "a derived score ... not a character attribute" is THIS line.)
```

Shown per subsystem, under each option:

| subsystem figure | Option B: derived from | Option A: derived from |
|---|---|---|
| contest pool (CD1) | PRA[proceeding faculty]; no attribute (CHA's Face view moves no outcome) | PRA[proceeding faculty] |
| `Combatant` (CD2) | the arms faculties (the bout's per-beat terms) over STR AGI END FOC ACU WIL ATT + PRA[`combat`] + TMP + KIT; `end` keeps its body derivation. Row: `contests: "the body"` | PRA[`combat`] → `history`; BODY → `end`; KIT; **every other field the class default** |
| Command (CD3) | faculty(command) = `derive_command(CHA, ACU)`, reaching the reform gate, the recall and feint rolls, the erosion divisors, `h_per_size` and the span of control (not the default exchange pool). Row: `contests: "a field"` | PRA[`command`] → `Officer.command` directly (the class accepts a given `command`, `units.py:2711`) [CHECKED-2] |
| the five inquiry acts (PD1a) | PRA[`inquiry`] (dice) + TS (`examine`'s gate), as under A, while the design author's sentence stands | PRA[`inquiry`] (dice) + TS (gate) |
| `thread_read` (PD1a) | the fieldwork pool's WIL is **barred by V-2** (the row declares no `contests:`); PRA[`thread`] + TS (gate, and the TPS term) | PRA[`thread`] + TS; WIL has no input |
| competence at deposit (PD1b) | **open**: no source names its input | PRA[`inquiry`], if a ruling says so; **open** |
| thread pool (CD5) | faculty(substrate) over WIL + PRA[`thread`] + TS; RES against the cost (six operations; Mending's cost is 0). **Needs a row with `contests:` for each operation (V-2)**: none has a row yet | PRA[`thread`] + TS; `spirit` the module default 4 (`operations.py:241`) [CHECKED-3] |
| knot (CD6) | the roll: WIL + PRA[relationships] through a faculty whose domain V-3 does not name, **which needs `contests:` on `tie / knot` (V-2)**: the row declares none. The gate and cap: bare BON, **outside V-2/V-3 unless V-2a is ruled**; TS (party gate), not an attribute | **BON and WIL have no input.** The gate reads `bonds`, which under A sits at its `getattr` default 0, below the minimum of 5, so no knot forms; the roll's `spirit` falls to its default 3 (`knots.py:185`, `:214`) [CHECKED]. TS comes from J-T1a's field; PRA[relationships] could feed `history_relationships`. A must rule a replacement for the gate. **Open** |

### 3.4 The two rulings, read against each other

- **"It will be 10 attributes"** (ED-IN-0185 Q7, 2026-08-14) [CHECKED-2]: a count, ruled, with no
  names, in an entry that closes its agenda: *"THE AGENDA IS CLOSED; DO NOT RE-RAISE IT"*
  (`editorial_ledger_in_archive.jsonl:137`) [CHECKED-2].
- **J-13's constraints** (2026-09-06, RS-16, `workplans/valoria_master_workplan_v9_part8.md:329`)
  [CHECKED-draft], quoted in the plan's J-13 row (`_part5.md:433`) [CHECKED-3]:
  - *"pool only it is, but ensure you don't go so far as to deprive player of a chance at winning"*;
  - *"It's a derived score that is used for the subsystem for a character, but it is not a character
    attribute in and of itself"*, which the plan glosses as *"a social figure is derived, not
    stored"*.
  - The row's three options were (i) the registry's `stats:`, (ii) *"a rank scale you rule"* and
    (iii) `pool_default` everywhere a case names no vocation. The plan adopted (iii) as the interim
    and named (ii) as a revert.

**They pull apart only on the broad reading.**

- **BROAD:** "nothing a person brings to a roll is stored; everything is derived". Then Option A,
  and the ruled ten is overwritten.
- **NARROW:** "the subsystem's figure (the social pool he was discussing) is derived, not an
  attribute". Then Option B satisfies both. The ten are stored, and every pool is derived from them
  at read. **The plan's own gloss is the narrow one.**

**Material that supports A, which the first draft did not cite.** The 2026-08-15 proposal: *"the
roles are not distinguished by aptitude — they are distinguished by practice, instruments, and
office"*, and combat, *"the one role Valoria expresses well"*, *"uses no attribute in its pool"*
(`proposals/2026-08-15-character-and-faction-stats-and-progression.md:152-162`) [CHECKED-2]. The
sibling proposal: every verb outside five domains *"needs **no** attribute"*
(`10_verbs_and_attributes.md:148-150`) [CHECKED-3]. And the proceedings design author, glossing
Jordan's 2026-09-05 ruling, takes five inquiry acts' dice from `capability` (§3.1.1).

The NPC critic flagged that K-NPC-1 cited neither reading (scratch `critics/NPC.md`, item 9). The
comparative critic flagged that J-C-3 would overwrite the ten (`critics/COMPARATIVE.md`, item 4).
**J-T1 is, in substance, the question: which reading did Jordan mean?** Escalating it does not
re-raise ED-IN-0185's closed agenda: the count stands under B, and J-13 (ii) does not touch it; **A
and A-1 would each overwrite it** (A stores none; A-1 stores eight), and only Jordan may (`CLAUDE.md`
§0's fifth answer does not reach a ruling's overwrite).

*"Pool only"* binds the contest roll under either option. A personal input enters the sigma roll as
dice, and never as an Ob shift on the actor's own act. (The OPPONENT's practice enters as Ob, per
Jordan's 2026-08-14 *"score/2 plus modifiers"*, `sigma.py:112-129` [CHECKED-3]; for `tell` the
opponent is the hearer.)

### 3.5 OPTION A — derived personal inputs

| part | content |
|---|---|
| **carrier** | the existing `Person.capability` (`carriers.py:651`), re-keyed from verb keys to PRACTICE keys on a closed roster (`rosters.yaml: practice_roster`, which would absorb `verb_capability`'s values; `verb_capability` becomes verb → practice key). **Plus one new `Person` field, `thread_sensitivity`** (J-T1a, K-3's field): TS needs a carrier under A as under B. It lands only with its first reader (a typed `thread_read` gate, H-85) |
| **readers** | each subsystem's host input builder derives its figure (§3.3's column A): `sigma._pool_of` unchanged; `seam/wrappers/combat.py` sets `history` from PRA[`combat`] beside `end`; the order of battle sets `Officer.command` from PRA[`command`]; the inquiry acts from PRA[`inquiry`]; a typed `thread_read` and the thread operations from PRA[`thread`] and `thread_sensitivity`. V-2 and V-3 bind nothing under A: no attribute exists to reach a verb |
| **write rule** | world-gen seats the template's `practice:`; `train` (IN-12 step 9) is the one runtime writer. This is the shape 04 F.6's REPAIR implies: F.6 records the gap *"`capability`'s season writer"*; its ASSUMED column, *"world-gen writes it once; nothing else does"*, is the assumption it says fails (*"a character never improves at anything"*); and its repair *"is a `practice` verb, not a field"* (`architecture/meta/04_CODE_ARCHITECTURE.md:1146`, `:1153`) [CHECKED-2], which `train` supersedes (`_part7.md:51`; `_part8.md:207`) [CHECKED-3]. The write-matrix row comes off `retired:` (`write_matrix.yaml:394-395`) [CHECKED-draft], as step 9 already plans |
| **defaults** | an absent key is "not practised". The reader falls to its declared default (`pool_default`, H-126; the module's class default). The template never fills a guess |
| **tests** | (1) an all-null template leaves the act log and every event identical to the pre-change tree at a fixed seed, at build and after N seasons. **The content hash moves structurally once J-T1a's field lands**, because `Person`'s `repr` gains a field and `_entity_digest` hashes the `repr` (`engine/season/state/world.py:167-177`) [CHECKED-draft]: a declared re-pin, the `Tenure.term` precedent (`carriers.py:103-105`) [CHECKED-draft]. Before that field lands, the hash is unchanged. (2) NPC-088's corpus world still seats `{copying: 3}` from its own overlay, which stays the owner (§4.4); the realm person seats none, as today. (3) two persons differing in one practice key diverge in that verb's pool (the probe in F15) and, over N seeds, in its success rate, against the equal-key control |
| **what it does to the game** | persons differ by what they have PRACTISED, their BODY and their KIT, and by nothing innate. Two untrained persons are identical in every roll. Physical difference enters only through body condition and kit. Combat's measured attribute spreads (the 2026-08-15 proposal reports +6.0 to +20.4 pp per attribute, `:122-123`, **T4, not re-run**) are not reachable, because every `Combatant` attribute stays at its default. Training is the only route to being better, which makes `train` very strong in the chooser. **It overwrites ED-IN-0185 Q7**: only Jordan may |

### 3.6 OPTION B — stored attributes

| part | content |
|---|---|
| **carrier** | a new `Person.attributes: dict`, keyed by registry keys (`attr.body.strength` …), **seeded with nothing**: K-2's shape (`09_the_character_sheet.md:129`) [CHECKED-draft]. Plus `Person.capability` as the practice store, and `Person.thread_sensitivity` (J-T1a), exactly as in A. A `write_matrix.yaml` row `(Person, attributes)`, world-gen class |
| **roster** | the leaf `ATTRIBUTES` (`engine/substrate/descriptors.py:50`) and its scale (`:52-53`, floor 1, ceiling 7) [CHECKED-draft], the single owner. The tenth slot stays PENDING (`ATTRIBUTES_PENDING_TENTH`, `:51`) until J-T2. The loader refuses a value for an unnamed slot |
| **readers** | each lands WITH ITS FIRST READER, as the plan already rules for K-2 (*"K-2 … builds only with its first reader (K-1/K-6)"*, `_part7.md:44`) [CHECKED-3], and each reads an attribute only through `faculty(domain)` on a row that declares `contests:` (V-2, V-3): (1) the combat host builder fills every `Combatant` attribute from the person through the arms faculties, keeping `end`'s body derivation (K-1; `fight`, `accept` declare `contests: "the body"`, `verb_table.yaml:485`, `:610`) [CHECKED-3]; (2) the order of battle builds `Officer(charisma, cognition)` from the commander, faculty(command) (K-6, U-4; `march` declares `contests: "a field"`, `:676`) [CHECKED-3]; (3) the thread operations read WIL through faculty(substrate) (V-3's *"substrate"* domain, `10_verbs_and_attributes.md:146`) [CHECKED-3], and the knot roll reads WIL through a faculty whose domain no source names (V-3's five domains omit knots, and the sibling says the `tie / knot` row *"has no precondition and no draw"*, `:168`) [CHECKED-3]; each **only once it has a row declaring `contests:`** (the operations have no rows; `tie / knot` declares none), and the knot's BON gate and cap only if V-2a is ruled; (4) **no inquiry act reads an attribute**: the five while the design author's sentence stands, and `thread_read` because its row declares no `contests:`, so V-2 bars the fieldwork pool's WIL (§3.1.1). **The contest roll reads no attribute**: the kernel binds none (`10_verbs_and_attributes.md:144`) [CHECKED-3] and Charisma's Face view moves no outcome (`resolver.py:226-229`) [CHECKED-2] |
| **write rule** | world-gen only. Whether anything later moves an attribute is J-T4 (§8), escalated: none (attributes are set at creation), age (through `born`), or a wound (through the bodies pass) |
| **defaults** | an absent key is "not authored". The reader falls to the MODULE's own default (`Combatant`'s 4/3, `combatant.py:93-94`; `Officer`'s 4), never to a template-side fill. Registry `default: 1` (`descriptor_registry.yaml:35`) [CHECKED-draft] is **not** used as a seat-time fill: it would make every unauthored person a 1, below every module's default |
| **tests** | (1) loader refusals (§4); (2) all-null attributes: the act log and every event are identical to the pre-change tree at a fixed seed. **The content hash moves structurally**, because `Person`'s `repr` gains `attributes` (and, with J-T1a, `thread_sensitivity`) and `_entity_digest` hashes the `repr` (`engine/season/state/world.py:167-177`) [CHECKED-draft]: a declared re-pin, the `Tenure.term` precedent (`carriers.py:103-105`) [CHECKED-draft]; (3) two persons differing in one attribute build different `Combatant` fields and, over N seeds, different fight outcomes, against the equal-attribute control |
| **what it does to the game** | persons differ innately and by practice. Who wins a fight and who holds a line vary by person **before** anyone trains; who forms a knot does too, once `tie / knot` gains `contests:` and V-2a is ruled. Multi-input verbs keep their stub combinations (§3A.4), owned as faculties. The cost is authoring: 46 × 9 values. **Today one cast row carries any attribute-like values**: NPC-001's `cognition 5, focus 5, endurance 4` map to ACU, FOC and END, the first through an alias the registry marks *"[ASSUMPTION] … Jordan veto"* (`descriptor_registry.yaml:42`) [CHECKED-draft]; `social: '3–4'` is refused (a prose range, and not a registry name). So under B the shipped template is all-null for 45 rows and changes no outcome until values are supplied (§5) |

### 3.7 DECISION J-T1 — the source of personal inputs (Jordan's)

- **(A)** derived: the only personal inputs are practice and kit (and TS on its own field, J-T1a);
  persons also differ through body and office, which are NOT personal inputs (the rule under
  "Words") and act through their own carriers. Overwrites the ruled ten. Open cells: the knot gate
  (§3.3), competence at deposit (PD1b), the combat attributes' derivation (§3A.4.2).
- **(B)** stored: the ten (nine plus J-T2's tenth) and practice. Reads J-13 narrowly. Open cells:
  the tenth (J-T2); competence at deposit (J-T9); whether attributes may reach the inquiry acts once
  the roster is settled (§3.1.1); `contests:` on `tie / knot` and on the thread operations' rows
  (V-2); and **V-2a**, the proposed amendment admitting a gate or cap on a bare attribute (the knot's
  BON), without which B's knot gate has no lawful input.
- **(A-1)** the 2026-08-15 proposal's recommendation, *"Six faculties + two capacities"*: Strength,
  Agility, Endurance, Cognition, Attunement, Spirit, rolled only through blends, plus Recall and
  Bonds as gates that never roll (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:191`,
  `:197-203`) [CHECKED-3]. **Eight in all, so it overwrites the ruled ten as A does**: it drops Focus
  and Charisma, adds Recall (which no source above T4 reads, §3.1.1), and leaves `derive_command`
  without its primary input.
- **(J-13 ii)** *"a rank scale you rule"* for `capability` (`_part5.md:433`) [CHECKED-3]: the plan's
  named revert for J-13. It is orthogonal to A and B: it rules the SCALE of practice values, which
  both options store, and it leaves the count of ten untouched. It is listed so the choice is not
  framed as A or B alone.

**What waits on it:**

- R-09's by-person conjunct;
- K-1 and K-6 (U-4);
- the troop design's commander source (its `_part2` §4.2, step 6, "Command before R-C-1") [CHECKED,
  by grep on the step];
- K-GO-8's creation screen fields;
- the template's `attributes:` block (§4).

**What does not wait:**

- every other template field;
- the practice block, which is the same under both;
- the loader and its refusals.
