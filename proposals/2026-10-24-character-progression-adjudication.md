# Character progression — one adjudication from first principles

## Status: PROPOSED (2026-10-24); **partly superseded since by the ratified v10 plan** (M2 / ED-IN-0301: nine stored attributes on 1-7 with practice live; CR-18 takes the practice arm of `2026-10-23-subsystem-completion` CP-T01-02; CR-20 keeps the `max(held key, base)` floor). Read those rows before the six-attribute roster and the cut of accrual below. Not ratified; merging ratifies nothing unless Jordan so rules. Reference under CLAUDE.md §0.05 — prose is not a mechanism.
## Lane: IN, with PC, SC, MB, SE, FA as sources. IDs: none allocated.
## Read at HEAD `b7a1e1b`
## Builds on: `engine/season/state/carriers.py` (`Person`) · `engine/season/loop/effects_combat.py` (`_eff_train`) · `engine/season/seam/wrappers/sigma.py` · `engine/season/seam/wrappers/combat.py` · `engine/season/seam/wrappers/mass_battle.py` · `engine/season/seam/wrappers/` siblings by grep · `engine/season/harness/play_surface.py` · `engine/season/decision/choose.py` · `engine/season/decision/options.py` · `engine/season/data/fixtures.py` · `engine/season/data/cast.py` · `engine/season/loop/census.py` · `engine/season/verb_table.yaml` · `engine/season/rosters.yaml` · `modules/combat/core.py`, `combatant.py`, `traditions.py`, `combat_systems.py`, `config.py` · `systems/combat/combat_engine_v1/workbench/build_levers.py` · `references/npc_registry.yaml` · `registers/editorial_ledger_in_archive.jsonl` (ED-IN-0185) · `research/game_precedent_suite/dispositions/D_T10.md` · `proposals/2026-08-15-character-and-faction-stats-and-progression.md` · `proposals/2026-10-16-verbs/2026-10-16-verbs-01-thesis-and-persons.md` and `-02-attributes.md` · `proposals/2026-09-30-character-and-play-surface/09_the_character_sheet.md` (house style)

**What this is.** One reasoned answer to the question *how should a person in Valoria change over a
life, and what makes the player's person different from any other?* It was produced by a read-only
agent reasoning from first principles, then written out here and checked against the tree at the
HEAD above. It is not a plan. It edits nothing, allocates no id, schedules nothing, and asks no one
to build anything. Where it says what would show a decision wrong, that is a falsifier — reference
for judging the decision, not a task. §1–§9 are the adjudication; §10 is an addendum written at
Jordan's request by the orchestrating session, not by the adjudicating agent, and it disputes one of
the adjudication's choices without changing it.

**What it deliberately ignores.** The adjudication was reasoned with the following rulings set
aside, so that its answer is not merely their restatement. §8 says how each is overridden.

| ruling | what it rules, in one line |
|---|---|
| ED-IN-0185 (Q7) | *"it will be 10 attributes"*; the tenth was unnamed when ruled [CHECKED: `registers/editorial_ledger_in_archive.jsonl`, the ED-IN-0185 row's Q7] |
| J-13 interim (iii) | `train` never mints a capability key the subject does not already hold [CHECKED: `engine/season/loop/effects_combat.py:426-431`] |
| J-T1, J-T2, J-T4 | open decisions: where personal inputs come from (derived or stored); the tenth attribute; whether attributes change after tick 0 [READER: `proposals/2026-10-16-verbs/2026-10-16-verbs-01-thesis-and-persons.md:49-53`]. J-T3 (kin) is outside this question. The adjudicating agent did not read these [GAP] |
| "capability gates nothing" | capability supplies dice and is never an eligibility test [CHECKED: `engine/season/rosters.yaml:1210-1212`; `engine/season/decision/options.py:464`, `:589-590`] |
| ED-PC-0023 | technique efficacy emerges from an invested level, not tradition membership; the imposition gate retired [CHECKED: `modules/combat/combatant.py:116`; `systems/combat/combat_engine_v1/workbench/build_levers.py:174-176`] |

**Marks.** [CHECKED] — opened at the cited line at HEAD `b7a1e1b` while writing this. [READER] —
taken from a document, not re-derived. [REASONED] — inference. `.designs/` is quarantined
(ARCHIVED-NOT-CANON, ED-IN-0231); it is named here for intent and vocabulary only, never as authority.

**Terms coined here, defined once.**

- **ceiling** — the highest value a capability key may hold for a person, a function of one stored
  attribute. Used in §3, §4.1, §4.3, §4.7.
- **floor** — the pool a person rolls on a key he does not hold, a function of one stored attribute;
  it replaces the fixture's single `pool_default` for that person. Used in §3, §4.1, §8.
- **decisive-event writer** — a write to `capability` at RESOLVE, made only when a contested row ends
  decisively (§3 element 2). Used in §3, §4.3, §7.
- **seat** — the person the player currently controls; mechanically, a person id in the `overrides`
  mapping of `engine/season/harness/play_surface.py::dispatching_chooser`, whose `choose` call goes to a
  callback instead of the shipped chooser (§2.6, §4.6). Not the same word as an office seat (a `Tenure`);
  where an office is meant, this document says *office*.

---

## 1. What this answers and what it ignores

**The question.** Valoria has no GM; every person runs the same rules; the player may take any person.
Under those three premises, the adjudication answers eight questions:

1. Should persons have innate attributes, and if so what do they do?
2. What is a person's *History* (§2 separates the three senses of the word)?
3. How does practice raise a skill?
4. Where do tradition and technique live?
5. How does a person change over a life — growth, decline, death?
6. What, if anything, makes the player's person exceptional, and how is switching seats bounded?
7. Where does challenge come from if the player's person improves?
8. How does personal progression reach the settlement, faction and mass-battle scales?

**The owner's views this session, as inputs — not findings.** Jordan raised four points; the
adjudication addresses each, and none is presented here as settled:

1. A freeform History lacks legibility in a videogame unless it is bundled into skills or attributes;
   it is a tabletop device for emergent events that a GM adjudicates.
2. Use-based progression implies that every character continually improves.
3. Attributes should probably be able to improve or decline over a life, to some degree.
4. Open: player exceptionality when any person is playable; challenge against outgrowing it; what
   challenge-scaling says about the world's coherence.

The adjudication departs from view 3 (§4.1, §4.5): it holds attributes fixed and puts change over a
life on capability and body. That departure is the adjudication's, recorded as it was made.

**What it ignores.** The rulings in the table above. It does not ignore the code: every premise in §2
is a fact about the tree at `b7a1e1b`, and where the adjudication's own citations were wrong, §9
records it.

---

## 2. The premises it keeps and the evidence it stands on

### 2.0 Three senses of *History* — kept apart throughout

The word has three unrelated senses in the tree. This document never uses the bare word; it writes one
of the three names below.

| name used here | what it is | where |
|---|---|---|
| **lifepath History** | a character-creation document: four stages, starting skills, a narrative remainder (Knots, Truth, Beliefs), SaGa-style *sparking* after scene rolls, Recall-gated equip slots, skill levels 1–3, and a separate attribute-allocation step | `.designs/systems/characters/reference/character_histories_v30.md` — quarantined, ARCHIVED-NOT-CANON; named for vocabulary only [READER; its scope line at `:15` opened] |
| **`Combatant.history`** | the personal-combat score: it sets the combat pool and the defender's obstacle | `modules/combat/combatant.py:94`, `:98` (class default `3`); read by `modules/combat/core.py:54-56`, `:100-115` [CHECKED] |
| **practice layer** | the August proposal's name for skill growth in +0.1D steps (*"Practice (the History layer)"*) | `proposals/2026-08-15-character-and-faction-stats-and-progression.md:242` [READER] |

The adjudication's own decision 2 ("History = the ledger + scar + tenures") is a fourth use. It is
written below as **recorded history**: what the carrier already holds about what happened to a person.

### 2.1 `Person` — what a person is in code

`engine/season/state/carriers.py:655-729` [CHECKED]. One class; a cohort is a person at `weight > 1`
(`:656`). Its fields: `id`, `name`, `weight`, `capability`, `stance`, `pursuits`, `ledger`, `body`,
`born`, `scar`, `conviction`, `thread_sensitivity`, `travel_leg`, `tenures`.

- **No attribute field, no lifepath-History field, no tradition field** [CHECKED: the field list above
  is the whole class body, `:657-729`].
- `born` is the birth tick; age is a query (`w.tick - born`), never stored, and its one reader is
  `queries/world_q.py::age_of` → `body_hazard` (`:680-687`) [CHECKED for the comment; the reader not
  opened].
- `thread_sensitivity` is filled once at build from the cast's authored `ts:` through
  `data/cast.py::thread_sensitivity_of`, *"`conviction_of`'s precedent"*, and has no write row, so the
  gate refuses any write in play (`:708-717`) [CHECKED]. **This is the build-only-store precedent the
  adjudication composes attributes on.**
- `conviction` is filled at build from the cast's `affiliations:` (`data/cast.py::conviction_of`,
  `data/cast.py:238`) and written in play only by the crisis at scar threshold 3 (`carriers.py:699-707`)
  [CHECKED].

### 2.2 `capability`, `train`, and the pool

- **One read, two callers.** `seam/wrappers/sigma.py::_capability` (`:104-116`) maps a verb through
  `VERB_CAPABILITY` and returns the entity's value or `None`. `_pool_of` (`:119-131`) returns that value
  or `fx.get("pool_default")`. `_opposition_of` (`:134-145`) returns the **subject's** value on the
  **same verb's key**, or `None`, which the social-contest module turns into `obstacle_default`
  [CHECKED]. The adjudication's claim that the opposition side reads the subject's capability on the
  same key holds.
- **`sigma.py` is the social-contest seam**, not a general one: `_PROVIDER = "social_contest"`,
  `_RESOLVER = "d10_sigma"` (`:100-101`) [CHECKED].
- **`pool_default = 2`, `obstacle_default = 2`** (`engine/season/data/fixtures.py:414`, `:416`), both
  graded `assumption` (H-126, H-127) [CHECKED].
- **`_eff_train`** (`engine/season/loop/effects_combat.py:421-446`) raises one vocation key by one, and
  only where the subject already holds it; it never mints a key, because *"a minted `{copying: 1}`
  would replace `pool_default` and LOWER his pool"* (`:426-431`) [CHECKED]. With `pool_default = 2`, a
  minted `{copying: 1}` makes `_pool_of` return 1 instead of 2 [CHECKED: `sigma.py:131` with
  `fixtures.py:414`]. The docstring's account of the interaction is correct.
- **`verb_capability` maps two verbs, both to one key:** `tell: "copying"`, `speak: "copying"`
  (`engine/season/rosters.yaml:1232-1233`) [CHECKED].
- **One of 430 built persons holds any capability** (NPC-088, `{copying: 3}`), a count the roster note
  dates 2026-10-02 (`rosters.yaml:1224-1227`) [CHECKED that the note says so; READER for the count,
  not re-run].
- **Nothing in the decision path reads `capability`.** In `engine/season/decision/` and
  `engine/season/queries/`, the only mentions are `options.py`'s refusals of it as an eligibility kind
  (`:201-203`, `:464`, `:589-590`) and `queries/inputs.py:48`'s description of `opposition` [CHECKED by
  grep].

### 2.3 Lifespan fixtures and death

- `age_step = 0.0`, `illness_rate = 0.0`, `age_at_build = 0` — the shipped control
  (`engine/season/data/fixtures.py:606-608`) [CHECKED].
- A person minted mid-run is `age_at_build` old at that tick: `born = w.tick - age_at_build`
  (`engine/season/loop/census.py:106`) [CHECKED].
- Most registry rows carry no authored age (`references/npc_registry.yaml`: `age: null [GAP]`), which
  is why `age_at_build` is a declared default (`carriers.py:683-685`) [CHECKED for the comment].
- With `succeed` declined, death only subtracts: seats vacated and not refilled
  (`research/game_precedent_suite/dispositions/D_T10.md:102`, row 90) [CHECKED that the row says so;
  its counts are READER].

### 2.4 Which verbs contest

`engine/season/verb_table.yaml` holds 56 verb rows under `verbs:`; 8 declare `contests:` — `argue`,
`arrest`, `determine`, `fight`, `accept`, `march`, `speak`, `tell` [CHECKED by loading the YAML]. Of
those eight, two (`tell`, `speak`) have a `verb_capability` row (§2.2); the other six roll on defaults.

### 2.5 The combat seam and combat's formulas

- **The season's combat seam derives exactly one `Combatant` field from a person:** `end`, from body
  bands (`engine/season/seam/wrappers/combat.py:129-137`, `party_end`) [CHECKED]. Every other field —
  including `history` and `tradition` — is the class default (`combat.py:34-39`) [CHECKED]:
  `history = 3`, `tradition = 'none'` (`modules/combat/combatant.py:94`) [CHECKED].
- **Combat's pool:** `resolution_pool(history) = max(POOL_FLOOR, int(round(history)) + BASE_POOL)`,
  `POOL_FLOOR = 5`, `BASE_POOL = 6` (`modules/combat/core.py:51-56`) [CHECKED]. So every season-scale
  fighter rolls `max(5, 3 + 6) = 9` [REASONED from the two lines].
- **Combat's obstacle:** `ob_from_defender(defender)` returns `defender.history / 2.0`
  (`modules/combat/core.py:100`, `:115`) [CHECKED]. Its docstring refuses any instance modifier folded
  in silently: *"If a genuine per-instance Ob modifier is ever needed here, it is a NEW term with its
  own owner"* (`:108-114`) [CHECKED].
- **Familiarity** is `modules/combat/traditions.py::familiarity` (`:47-55`): 1.0 if the traditions match
  or either is `'none'`, else an adjacent or default value [CHECKED]. It enters combat as a multiplier
  on each side's read (`modules/combat/combat_systems.py:1057-1059`, `:1128`) and as a commit-caution
  bias, `wary = WARINESS_K * (1 - familiarity(...))` (`:1116`), with `WARINESS_K = 1.5`
  (`modules/combat/config.py:279`) [CHECKED]. **It does not touch the obstacle.**
- The workbench sweep of this lever is `systems/combat/combat_engine_v1/workbench/build_levers.py::familiarity`
  (`:173-183`); its docstring: an ability-less tradition differs from another *"ONLY through
  traditions.familiarity() feeding WARINESS_K"* [CHECKED].
- **Consequence today:** because the season seam leaves every combatant at `tradition = 'none'`,
  familiarity is 1.0 for every season fight and the `WARINESS_K` term is zero [REASONED from
  `combat.py:34-39`, `combatant.py:94`, `traditions.py:51-52`].
- **Two ladders exist today:** the social-contest pool (`capability` or `pool_default = 2`) and the
  combat pool (`Combatant.history` through `max(5, history + 6)`). `Person.capability` reaches the
  first and not the second [REASONED from the reads above].

### 2.6 The player's seat

`engine/season/harness/play_surface.py::dispatching_chooser` (`:41-56`) is *"the whole single-player
hook"*: a `choose` that sends person ids in `overrides` to a callback and everyone else to the shipped
chooser; the callback sees only what `choose` sees, and the seam adds no rule [CHECKED: module docstring
`:1-33`]. `overrides` is read at each call, so a client may add or remove a person between seasons
(`:44-47`) [CHECKED]. `engine/season/decision/choose.py:433` is the shipped chooser's inner
`choose(p, v, s, ask_budget)` closure inside `make_chooser` (`:407`) — the automated person's
deliberation, not the handoff [CHECKED]. It ranks a person's **candidate acts**
(`score_order`, `:399-404`), never persons [CHECKED].

### 2.7 Mass battle

`seam/wrappers/mass_battle.py::field_input` reads each side's member **weights** and the side's
weight-mean **stance**; nothing in it reads `capability` or a leader's score (`:126-146`, `:177-192`)
[CHECKED by grep for `capability`, `weight`, `leader`]. `march` has no `verb_capability` row
(`rosters.yaml:1232-1233`) [CHECKED].

### 2.8 Cast authoring

`references/npc_registry.yaml` holds 46 rows; `data/cast.py`'s docstring counts 29 carrying `stats:`
and 32 carrying `ts:` (measured 2026-09-13; `data/cast.py:3-6`) [CHECKED that it says so; READER for
counts]. The `stats:` keys are registry-vocabulary names with ranges allowed (`cognition: 5`,
`focus: 5`, `endurance: 4`, `social: 3–4`; `npc_registry.yaml:57-61`) [CHECKED], and the header says
*"Stats are deferred"* (`:27`) [CHECKED]. A corpus person with no registry row has no authored value of
any kind (`carriers.py:712-714`) [CHECKED for the comment].

### 2.9 Measured figures carried from the August proposal

All [READER], from a stub resolver measured before ED-PC-0058 retired the fixed decisive obstacle; they
are orders of magnitude, not current values.

| figure | value | where |
|---|---|---|
| one +0.1D step | ≈ +1.6pp | `2026-08-15-…-progression.md:72`, `:242` |
| one whole attribute point | +6 to +20pp | `:43`, `:243` |
| technique ladder | ~0pp aggregate, ~12–13% per-fight texture | `:241` (the 12–13% corrected from 16–28%, `:328`) |
| an acquisition layer the policy cannot see | *"a stat block, not an acquisition layer"* | `:736-747` (§13.1; the case is the social contest's `ContestView`, which carries no school or technique) |

### 2.10 Outside literature and games, with grades

| source | grade | what it is used for here |
|---|---|---|
| Juul 2002, *The Open and the Closed* | read | emergence versus progression as two structures |
| Hunicke & Chapman 2004 | read | reactive difficulty adjustment risks disrupting disbelief; proactive adjustment is hard to evaluate and can spiral; dynamic difficulty adjustment *"takes control away from the designer"* |
| Ryan, Rigby & Przybylski 2006 | abstract only | names competence, autonomy and relatedness as needs — **competence, not growth as such** |
| Brändle et al. 2025, *Scientific Reports* | read | enjoyment peaks at intermediate difficulty, with expectation-matching; it studies authored levels in puzzle, racing and platformer games, **not power growth** |
| Lundblade 2024, DiGRA | abstract only | does not address player-character questions; cited for nothing load-bearing |
| CK3, Ars Magica, RimWorld, Battle Brothers, Shadow of Mordor, Mount & Blade: Warband, Kenshi, Pendragon, Football Manager, GURPS, Burning Wheel | community-grade or from memory | precedent shapes only; none is evidence that a decision here is correct |

---

## 3. The architecture

The adjudication's recommended architecture, element by element. Every element is a design assertion
[REASONED] unless a cell cites the tree. Where the tree contradicts a cell, the cell is kept as the
adjudication wrote it and §9 carries the correction.

| # | element | store | writer | reader | bound / exit |
|---|---|---|---|---|---|
| 1 | **Attributes** — six stored integers, immutable in play: **Body, Hand, Wit, Nerve, Presence, Sense** | `Person.attributes`, a dict, authored at build from `data/cast.py` the way `thread_sensitivity_of` is | build only | a **ceiling** and a **floor** per capability key; never a dice term | fixed roster of six; each 1–5 |
| 2 | **Capability (skills)** — the only dice source; one ladder at all scales | `Person.capability`, exactly as `_pool_of` reads it | `train` (instruction), plus one new **decisive-event writer** at RESOLVE on a decisive contested row (`degree >= full success`, or a loss that writes a `scar`): +1, at most once per key per season | `_pool_of`, with `pool = max(floor(attr), capability[k])` replacing `pool_default` (§4.1) | `capability[k] <= ceiling(attribute)`; a key not exercised for N seasons decays by 1 toward its attribute floor |
| 3 | **Recorded history** — the ledger, the scar and the tenures; nothing else authored | `Person.ledger`, `Person.scar`, `Person.tenures` | the existing RESOLVE writers | the chooser through `OwnStateReader`; the UI as the character sheet | no lifepath bundle; the "bundle at creation" is the cast overlay writing capability and attributes |
| 4 | **Tradition / technique** — a label on a capability key | the capability-key namespace, e.g. `fight:germanic` | `train`, with `kind` | the seam's opposition read (`sigma.py` ~134–146) and combat's `familiarity` → `WARINESS_K` | a modifier on the opponent's obstacle, not a second pool |
| 5 | **Change over a life** — capability decay plus injury-driven `body`; attributes never move | `Person.capability`, `Person.body` | element 2's decay; the existing body writers | as elements 1–2 | **exit:** mortality on (`age_step`, `illness_rate` non-zero) **only once** `age_at_build` is authored from the registry **and** a successor write exists for `tenures` |
| 6 | **Player exceptionality** — none mechanical | — | — | the player's **seat** is the `choose` handoff, and that is all it is | — |

**What the architecture adds to `Person`:** one field, `attributes`. Everything else composes on fields
the carrier already has (§2.1) [CHECKED for the existing fields; the addition is REASONED].

**What it adds to the loop:** one writer (the decisive-event write and its decay, element 2) and one
change to a read (`_pool_of`'s fallback, element 2). `train`'s refusal to mint a key is lifted, because
once the fallback is `max(floor, capability)` a minted low key can no longer lower a pool (§4.1, §8)
[REASONED].

**Notes the tree adds to the table** (detail in §9):

- Element 4's two readers are in different resolvers: `sigma.py`'s `_opposition_of` serves the social
  contest, and familiarity lives in personal combat; and in combat, familiarity reaches the read and the
  commit bias, not the obstacle (§2.5; §9 C-2).
- Element 6's `choose` handoff is `harness/play_surface.py::dispatching_chooser`; the adjudication's
  citation (`decision/choose.py` ~433) is the shipped chooser (§2.6; §9 C-3).
- Element 2's "one ladder, all scales" is a target, not today's state: combat's pool reads
  `Combatant.history`, not `capability` (§2.5; §9 C-4).

---

## 4. The eight adjudications

Each is given as the adjudication gave it: **decision**, **reason**, **strongest counter** (with the
adjudication's answer where it gave one), **falsifier**. Falsifiers are reference: they state what
observation would show the decision wrong. Marks are on the claims; the decisions themselves are
[REASONED].

### 4.1 Attributes

**Decision.** Yes: six, stored, immutable. They set ceilings and floors on capability and do nothing
else, at any scale.

**Reason.**

- An attribute that is a dice term double-counts with capability on the same roll: `_pool_of` is one
  read (§2.2) [CHECKED for the read; REASONED for the double count].
- A ceiling gives innate difference its one legible, non-additive job: *how far can this person go.*
  [REASONED]
- Six stays below the nine, eleven and fourteen of the earlier rosters, which grew because each lane
  wanted its own axis [REASONED; the rosters themselves READER, §5].
- Cost and access at settlement and faction scale read capability, not attributes [REASONED].

**Strongest counter.** GURPS and Burning Wheel [memory-grade] use attribute-relative skills and still
put attributes in the roll for untrained acts. **The adjudication's answer:** the floor *is* the
untrained roll — `pool = max(floor(attr), capability[k])` replaces `pool_default`.

**Falsifier.** Build the 430 persons with authored attributes and run 20 seasons. If 90% or more of
capability keys sit at their ceiling, the ceiling is a no-op and this decision is wrong (the
adjudication's words: the ceiling *"should be cut"*).

### 4.2 Recorded history

**Decision.** History is **recorded only** (the adjudication's option (b)). Authored material enters as
initial capability, attributes and conviction — never as a text History.

**Reason.**

- The lifepath History's Knots/Beliefs remainder needs an adjudicator, and Valoria has no GM (§2.0)
  [READER for the lifepath document's content; REASONED for the need].
- CLAUDE.md §0.05: prose is not a mechanism [CHECKED].
- The carrier already holds `ledger`, `scar`, `conviction` and `tenures`, and the chooser reads them
  (§2.1; `choose.py:416-420` lists `pursuits`, `scar`, `stance`, `conviction` as the chooser's
  person-side inputs) [CHECKED].

**Strongest counter.** Legibility: a ledger is a log, not a sheet. **Answer:** the sheet is the ledger
filtered through the epistemic contract — the player sees exactly what the person holds.

**Falsifier.** If playtest readers cannot say why a person acted from ledger, scar and conviction alone,
this decision is wrong, and option (a) — a labelled summary layer — is the answer it concedes to.

### 4.3 Practice

**Decision.** One ladder, `capability`. Its writers are instruction (`train`) and the decisive-event
writer. **Not** per-use accrual.

**Reason.**

- Per-use accrual makes everyone rise (owner view 2) [REASONED].
- +0.1D is about +1.6pp, inside the noise for the player's read (§2.9) [READER].
- Event-based writes are rare, legible (*"you won the duel, Fight 3 → 4"*) and bounded by the attribute
  ceiling [REASONED].

**Strongest counter.** Event-based rewards favour risk-seeking: the chooser will seek fights. **Answer:**
that is drama, and the scar and mortality side pays for it.

**Falsifier.** Count capability writes per season across the 430 persons. If the median key moves more
than once per season, the gate is too loose.

### 4.4 Tradition

**Decision.** Tradition is an **input**, through familiarity on the opponent's obstacle; a **label** for
the UI; never a separate output.

**Reason.**

- The August proposal's §13.1: an acquisition layer the policy cannot see is a stat block (§2.9)
  [READER].
- Familiarity already exists as a lever (`build_levers.py` ~173–176) and the opposition read already
  exists at the seam; composing on both costs no new primitive and works zoomed out [CHECKED that both
  exist — `build_levers.py:173-183`, `sigma.py:134-145`; see §9 C-2 for what each actually does].

**Strongest counter.** Technique ladders give 12–13% per-fight texture that a flat edge loses (§2.9)
[READER]. **Answer:** accept the loss. Texture is a good of the played duel; the seam is zoomed out.

**Falsifier.** An `arms`-style n-seed comparison of a tradition-mismatched pair against a matched pair.
If no obstacle separation appears, the edge is dead.

### 4.5 Change over a life

**Decision.** Capability decays; `body` injures; attributes are fixed.

**Reason.**

- Age curves are unauthorable today: `age_at_build = 0` (§2.3) [CHECKED].
- A derived `f(body)` attribute double-counts wounds: combat already derives `end` from body bands
  (§2.5) [CHECKED for the derivation; REASONED for the double count].
- Decay is legible (*unused*) and symmetric with growth [REASONED].

**Strongest counter.** Physical decline with age, Football Manager-style [memory-grade], is a genre
expectation. **Answer:** defer until age is authored; it is then one more writer on capability, not on
attributes.

**Falsifier.** Author ages, turn `age_step` on, and confirm death subtracts without leaving vacancies.

### 4.6 Exceptionality and switching

**Decision.** No mechanical specialness for the player's person. The switching exploit — take the
strongest seat, or hop to whichever person is best placed — is answered by **position as difficulty**
plus a **switch cost**: the loss of the epistemic view (a new seat is a new ledger; the player knows
nothing the new person does not), and no switch while a contest is open.

**Reason.**

- CK3 [community-grade] shows that pick-any works when the seat is the difficulty.
- The epistemic contract already makes a switch costly at no extra cost: the callback sees only what
  `choose` sees (§2.6) [CHECKED for the seam; REASONED for the cost].

**Strongest counter.** Players will still pick the strongest. **Answer:** "strongest" is readable only
from inside a seat, which is the exploit's own brake.

**Falsifier.** If the automated chooser ranks persons by capability sum and a player can see that list,
the exploit is live. At `b7a1e1b` the chooser ranks a person's candidate acts, not persons (§2.6)
[CHECKED], so the falsifier's first condition does not hold today.

### 4.7 Challenge

**Decision.** Combine a fixed world, same-rules progression for every non-player person (under the same
ceilings), and mortality. Reject any threat keyed on the player's state, and any scaling.

**Reason.**

- Same rules is the premise [REASONED].
- Ceilings answer the objection that non-player persons ratchet forever, which would otherwise
  contradict a world that is already wide at tick 0 [REASONED].
- Mortality is the exit for everyone [REASONED].
- A state-keyed threat is a director under another name [REASONED]. Support added in this write-up,
  not cited by the adjudication: Hunicke & Chapman 2004 record that dynamic adjustment *"takes control
  away from the designer"* and that reactive adjustment risks disrupting disbelief (§2.10) [read].

**Strongest counter.** No-scaling games — Mount & Blade: Warband, Kenshi [memory-grade] — go stale late;
they are the pole that accepts the overlevel, not a solution to it. **Answer:** mortality and tenure
churn are the late-game content, *if succession ships*.

**Falsifier.** A 50-season run. If the player seat's capability sum exceeds every non-player person's by
season 15 and nobody dies, the architecture has failed.

### 4.8 Multi-scale

**Decision.** A cohort is a person at `weight > 1`. A unit's power is the leader's capability on the
`march` verb multiplied by weight, the seam reading the same `_pool_of`. Offices read capability as an
eligibility floor, never as a modifier. (The adjudication wrote "seats"; it means offices, `Tenure`
edges, not the player's seat.)

**Reason.**

- It composes on S9 (a cohort is a person, `carriers.py:656`) [CHECKED] and on the existing contest read
  [CHECKED for `_pool_of`; see §9 C-5 for `march`].
- A flat per-scale modifier is the shape divergence CLAUDE.md §10 forbids [CHECKED].

**Strongest counter.** Mass battle wants formation and equipment, not a leader stat. **Answer:** those
are class defaults today and stay there.

**Falsifier.** If `march`'s resolve never reads `capability[march]`, personal progression is severed from
mass scale. At `b7a1e1b` it does not: `field_input` reads weights and stance only, and `march` has no
`verb_capability` row (§2.7) [CHECKED]. The falsifier describes today's tree; the decision asserts a
read the tree does not yet have (§9 C-5).

---

## 5. How the six relate to the nine, the eleven and the fourteen

**This section is exposition, not a decision.** The adjudication named six attributes and gave no
mapping. The table below is this write-up's [REASONED] reading of where each earlier roster's members
would fall under the six, so a reader can compare them. It allocates nothing and decides nothing; where
a member has no clear home, the cell says so.

Sources: the registry's nine are `references/descriptor_registry.yaml:36-48` [CHECKED]. The eleven is
the Derivation's (v1's) recommendation: the nine plus Thread Sensitivity and Recall
(`proposals/2026-10-16-verbs/2026-10-16-verbs-02-attributes.md:20-23`, `:110-122`) [READER]. The
fourteen is the from-scratch derivation's (`proposals/2026-10-16-attributes-from-scratch_part4.md:34-35`)
[CHECKED], placed against the nine as verbs-02's mapping column places it (`:112-125`) [READER];
verbs-02 holds it void until rerun blind (`:215-267`) [READER].

| the six | registry nine | the eleven adds | from-scratch fourteen | notes |
|---|---|---|---|---|
| **Body** | Strength, Endurance | — | bodily force, toughness | the name collides with the field `Person.body` (§9 C-8) |
| **Hand** | Agility (alias Dexterity) | — | quickness, fine hand | verbs-02 records `dexterity` as having no reader [READER] |
| **Wit** | Acuity (alias Cognition), part of Focus | Recall | reasoning, forethought, part of watchfulness | Recall has no Python field [READER: verbs-02 `:122`] |
| **Nerve** | Will (alias Spirit), part of Focus | — | constancy, composure, nerve | verbs-02 files *nerve* as temperament, a field beside the attributes [READER: `:124`]; disputed in §10 |
| **Presence** | Charisma (alias **Presence**), Bonds | — | presence, warmth | `Presence` is already a registry alias of Charisma (`descriptor_registry.yaml:47`) [CHECKED] |
| **Sense** | Attunement (alias Perception) | — | reading people, part of watchfulness | — |
| *(none)* | — | Thread Sensitivity | thread perception | **not placed by the adjudication** [GAP]. `Person.thread_sensitivity` exists as its own build-only field (§2.1); this table does not move it into Sense or anywhere else |

**What the comparison shows, and only this** [REASONED]: the six fold Focus across Wit and Nerve and
fold Bonds into Presence; they leave Thread Sensitivity where it already is; and every earlier roster's
growth came in the mind and social rows, which is where the adjudication's *"each lane wanted its own
axis"* (§4.1) points.

---

## 6. What is cut or never built, and why

| cut | why (the adjudication's reason; marks on the support) |
|---|---|
| per-use +0.1D accrual | everyone rises (owner view 2); each step ≈ +1.6pp, below what a player reads (§2.9) [READER for the figure] |
| any attribute in the dice pool | double-counts with capability on the one read `_pool_of` makes (§2.2) [CHECKED for the read] |
| derived `f(body)` attributes | double-counts wounds; combat already derives `end` from body bands (§2.5) [CHECKED] |
| lifepath / Knot text History | needs an adjudicator Valoria does not have; prose is not a mechanism (CLAUDE.md §0.05) |
| Recall-gated slots | belong to the lifepath History; Recall has no Python field [READER] |
| a technique ladder as a seam-visible layer | the policy cannot see it, so it is a stat block (§2.9) [READER] |
| any scale-local progression dialect | shape divergence (CLAUDE.md §10) [CHECKED] |
| a threat director keyed on player wealth or power | a director under another name; it breaks *same rules for every person* |
| flipping `age_step` before succession exists | with `succeed` declined, death only subtracts — vacancy, not churn (§2.3) [CHECKED that D_T10 says so] |

---

## 7. The three likeliest failure modes of the recommendation

The adjudication named these against itself.

1. **Ceilings make the world static.** If authored attributes cluster, capability saturates against the
   ceilings, decay and growth cancel, and nothing happens offstage [REASONED]. This is the same
   observation §4.1's falsifier is built to catch.
2. **The decisive-event writer starves.** Only 8 of 56 verbs contest, and only `tell` and `speak` map to
   a capability key (§2.2, §2.4) [CHECKED]. The writer would then fire rarely, and progression would
   exist on paper and not execute — the failure CLAUDE.md §0.2 defines as *not done* [REASONED].
3. **Decay without a visible cause reads as punishment.** The player sees *Fight 4 → 3* with no event —
   unless the decay also writes a ledger claim that the person can hold and the sheet can show
   [REASONED].

---

## 8. Rulings overridden, assumptions, [GAP]s

### 8.1 Rulings overridden

| ruling | how the adjudication overrides it |
|---|---|
| ED-IN-0185 Q7 (ten attributes) | six, as ceilings and floors, not dice terms |
| J-13 interim (iii) (`train` never mints a key) | minting is safe once `pool = max(floor, capability)`: a minted low key can no longer fall below the floor [REASONED; holds only for a person who has an authored floor — see 8.2] |
| J-T1, J-T2, J-T4 | not read by the adjudicating agent [GAP]; overridden only insofar as they bind progression to a technique ladder. On their face (§1 table) J-T1 is answered *stored*, J-T2 is answered *no tenth, six in all*, and J-T4 is answered *attributes never change* [REASONED reading of the adjudication against the one-line descriptions] |
| "capability gates nothing" | overridden for office eligibility only (§4.8); capability still gates no verb |
| ED-PC-0023 | the adjudication names it as "tradition"; tradition becomes a familiarity input, not an output. What ED-PC-0023 actually placed in code is graded technique investment and the retired imposition gate (§1 table; §9 C-6) |

### 8.2 Assumptions

- **`_opposition_of`'s read can carry a familiarity term without a new field** [REASONED by the
  adjudication]. The tree places `_opposition_of` in the social-contest seam and familiarity in personal
  combat (§9 C-2), so the assumption names the wrong seam for a combat edge.
- **The cast overlay can author attributes**, on the `conviction_of` / `thread_sensitivity_of`
  precedent [CHECKED that the pattern exists, `data/cast.py:238`, `:283`, and that `Person` documents it,
  `carriers.py:708-711`; not run]. The precedent returns `None` for a person with no registry row
  (`data/cast.py:283-287`) [CHECKED], and most built persons have no row (§2.8). What a person without
  authored attributes has for a floor and a ceiling is not stated by the adjudication [GAP].
- **The attribute bound is 1–5.** The registry's authored `stats:` use other names and allow ranges
  (`social: 3–4`, §2.8) [CHECKED]; the adjudication does not say how they map onto the six [GAP].
- **N** (the seasons without exercise before decay) is unspecified by the adjudication.

### 8.3 [GAP]s

The adjudicating agent left two; this write-up opened both.

| gap as the adjudication left it | what the tree shows at `b7a1e1b` |
|---|---|
| `march`'s resolve path not opened | closed: `field_input` reads member weights and side stance; no capability, no leader score (§2.7, §9 C-5) [CHECKED] |
| the chooser's own ranking of persons not opened | closed: the chooser ranks a person's candidate acts; nothing ranks persons (§2.6, §9 C-7) [CHECKED] |

Still open: J-T1..J-T4 unread by the adjudicating agent; Thread Sensitivity's place among the six
(§5); floors and ceilings for persons with no authored row (8.2); the stats-to-six mapping (8.2).

---

## 9. Corrections found while writing this up

Each correction gives the evidence, the decision it bears on, and whether that decision still follows.
No decision above was changed. §10 disputes retaining Nerve, which the adjudication keeps.

**C-1. Combat's formulas were verifiable; the adjudicating agent searched a moved path.** It searched
`systems/combat/` and reported combat's pool and obstacle formulas as unverified. The engine moved to
`modules/combat/`: `resolution_pool(history) = max(5, int(round(history)) + 6)` at
`modules/combat/core.py:51-56` and `ob_from_defender(defender) = defender.history / 2.0` at
`core.py:100`, `:115` [CHECKED]. *Bears on:* §4.4 (the obstacle), §4.8 and element 2 (one ladder).
*Still follows:* yes; no decision rested on the formulas being unverified.

**C-2. Familiarity does not reach the obstacle, and the opposition read is not combat's.**
`seam/wrappers/sigma.py::_opposition_of` (`:134-145`) belongs to the social-contest seam
(`_PROVIDER = "social_contest"`, `:100`) and returns the subject's capability on the verb's key with no
familiarity term [CHECKED]. In combat, familiarity multiplies each side's read and sets the commit
bias `WARINESS_K * (1 - familiarity)` (`modules/combat/combat_systems.py:1057-1059`, `:1116`, `:1128`)
[CHECKED]; the obstacle is `defender.history / 2.0`, whose docstring requires any per-instance modifier
to be *"a NEW term with its own owner"* (`core.py:108-114`) [CHECKED]. The season seam leaves every
combatant at `tradition = 'none'`, so familiarity is 1.0 in every season fight (`combat.py:34-39`,
`combatant.py:94`, `traditions.py:51-52`) [CHECKED]. *Bears on:* §4.4 and element 4. *Still follows:*
the decision (tradition as an input and a label, never an output) still follows. Its reason *"costs no
new primitive"* does not hold as written: an obstacle modifier is a new term by `core.py`'s own rule,
and any season-scale effect needs the seam to derive a tradition — a second derived `Combatant` field,
where the seam's discipline is exactly one (`combat.py:34-36`) [REASONED]. Through the existing channel
(read and commit bias), the §4.4 falsifier's *obstacle* separation is absent by construction, so the
falsifier as worded would fire whatever the edge is worth [REASONED].

**C-3. The seat's handoff is `dispatching_chooser`, not `choose.py:433`.** `decision/choose.py:433` is
the shipped chooser's inner `choose` inside `make_chooser` (`:407`) [CHECKED]. The handoff is
`harness/play_surface.py::dispatching_chooser` (`:41-56`), which adds no rule and reads `overrides` at
each call (`:45`) [CHECKED]. *Bears on:* §4.6 and element 6. *Still follows:* yes — the seam is exactly
"the `choose` handoff, and that is all it is". One consequence the adjudication did not state: because
the seam adds no rule, *no switch while a contest is open* is not something the seam holds today
[REASONED].

**C-4. "One ladder, all scales" is a target; today there are two.** The social-contest pool reads
`capability` or `pool_default = 2` (§2.2); the combat pool reads `Combatant.history`, class default 3,
through `max(5, history + 6)` (§2.5) [CHECKED]. `Person.capability` reaches no combat roll [CHECKED: the
combat seam derives only `end`]. *Bears on:* §4.1 (the floor replaces `pool_default`, which exists only
on the social-contest ladder), §4.3 and §4.8. *Still follows:* yes, as a design claim; the floor as
written is defined against the social-contest ladder only, and combat already carries its own floor on a
different scale (`POOL_FLOOR = 5`) [CHECKED] — the "two ladders for one quantity" case §0.06's S
criterion names [REASONED].

**C-5. `march` reads no capability.** `seam/wrappers/mass_battle.py::field_input` reads each side's
member weights and weight-mean stance (`:126-146`, `:177-192`); nothing in the file reads `capability`
or a leader score; `march` has no `verb_capability` row (`rosters.yaml:1232-1233`) [CHECKED]. *Bears
on:* §4.8. *Still follows:* as a design claim, yes; its reason *"composes on … the existing contest
read"* does not hold for mass battle, because the contest read (`_pool_of`) is the social-contest seam's
and the field seam has none. §4.8's own falsifier is met at `b7a1e1b`: personal progression is severed
from mass scale today [CHECKED].

**C-6. ED-PC-0023 is not a "tradition as output" ruling as such.** In code it reads: technique *"efficacy
emerges from the invested level, not tradition membership"* (`modules/combat/combatant.py:116`), and the
imposition gate is retired (`build_levers.py:174-176`) [CHECKED]. *Bears on:* §8.1 and §4.4. *Still
follows:* yes; what the adjudication overrides is the graded technique ladder as a seam-visible layer,
which its cut list (§6) already names.

**C-7. The chooser ranks acts, not persons.** `score_order` (`choose.py:399-404`) sorts a person's
candidates [CHECKED]. *Bears on:* §4.6's falsifier. *Still follows:* yes; the falsifier's first
condition does not hold today.

**C-8. Two attribute names already mean something in the tree.** *Body* collides with `Person.body`, the
condition field (`carriers.py:679`) [CHECKED] — §4.5's *"body injures; attributes fixed"* uses both
senses in one sentence. *Presence* is a registry alias of Charisma (`descriptor_registry.yaml:47`)
[CHECKED]. A third: the registry already has an aggregate named *Body*, `agg.body` (`descriptor_registry.yaml:53`; its members include Agility, which the table at :460-461 gives to Hand) [CHECKED]. Under CLAUDE.md §4's word-choice rule a reader with no memory of this repository would not
land on one meaning [REASONED]. *Bears on:* §3 element 1, §4.1, §4.5. *Still follows:* yes; the names are
the adjudication's and are kept here unchanged.

**C-9. The cast overlay reaches registry rows only.** `thread_sensitivity_of` returns `None` for a person
with no row (`data/cast.py:283-287`), and most built persons have none (`carriers.py:712-714`) [CHECKED].
*Bears on:* §4.1's falsifier (*"build 430 persons with authored attributes"*) and element 1's writer.
*Still follows:* yes; the falsifier presupposes an authoring source for persons the registry does not
list, which the adjudication does not name (§8.2) [GAP].

**C-10. The addendum's overlap figures reproduce.** §10.3's Jaccard figures were re-run for this
write-up (reproducer in §10.3) and match the figures supplied with the addendum to two decimal places;
no discrepancy [CHECKED: run at `b7a1e1b`].

---

## 10. Addendum — the from-scratch fourteen against the decision matrix

**This section is not part of the adjudication.** The orchestrating session wrote it at Jordan's
request, after the adjudication; it changes none of the adjudication's decisions. Its one disagreement
with the adjudication is stated in §10.6 and left unresolved.

### 10.1 The decision matrix as it exists

- **The score.** A candidate's score is the sum of three terms: `damp * Σ_axis axis_w[axis] *
  align(verb, axis)` over the seven axes, a stance term, and an urgency term identical for every
  candidate (`engine/season/decision/choose.py:130-151`, `score_terms`) [CHECKED].
- **Pursuits to axes.** A person's weights over the fifteen pursuits (`references/descriptor_registry.yaml:134`)
  reach the seven bipolar axes (`:168`) only through `engine/season/rosters.yaml: tables.pursuit_projection`
  (15 rows, `:2880`) [CHECKED]. Each verb has an alignment cell per axis (`tables.alignment`, `:3041`)
  [CHECKED].
- **The refusal gate is dormant.** `refuses()` (`engine/season/decision/options.py:446`) is the
  person-side refusal; it is dormant because `refusal_axis` ships unset (`options.py:427-432`;
  `data/fixtures.py:749`, `refusal_axis=None`) [CHECKED].
- **Budget is a count.** `budget` (`engine/season/decision/budget.py:18`) returns scene actions:
  base, plus an office bonus per held `hold` tenure, minus a body-band penalty, minus a travel-leg penalty
  (docstring, `:36-38`) [CHECKED].
- **What the score lacks.** It has no risk term and no timing term (at HEAD; v10 CR-17, B10-09, adds believed odds to the alignment term; **Jordan ruled 2026-10-29 that persons differ in risk appetite and in short-, medium- or long-term horizon, so a risk term and a timing term are wanted**) — its three terms are the whole
  return (`choose.py:149-151`) [CHECKED] — and no lookahead: it scores each candidate once, at the
  moment of deliberation [REASONED from the same lines]. `choice_temperature` is a global sampling-noise
  setting (`data/fixtures.py:286`, `0.1`; read in `_sample_order`, `choose.py:241`, `:350`) [CHECKED].
- **R7.** The projection is linear in the weights, so two persons with identical weights are identical
  on every projected axis, and *"any quantity that must vary at fixed weights cannot be a projected
  axis"* (`proposals/2026-09-18-character-decision-layer/PROPOSAL.md:55-58`) [READER; its source,
  `adjudication_register.yaml:223-228`, not opened].

### 10.2 The fourteen against the matrix

The fourteen are defined in `proposals/2026-10-16-attributes-from-scratch_part4.md` §6.3 (`:42`
onward) [CHECKED]. **Decision-side** means the attribute describes whether a person chooses an act, which
is the chooser's work; **resolver-side** means how well an act he has chosen goes. Both terms are
defined here for this section only.

| attribute | decision-matrix analogue | verdict |
|---|---|---|
| **Nerve** | partial. Alignment cells exist for `challenge` (grandiose_humble −0.6, precedent_substantive −0.3, deontological_instrumental −0.3), `accept` (rigid_flexible −0.3, grandiose_humble −0.2, deontological_instrumental −0.4) and `evade / defy` (hierarchical_equal +0.9, precedent_substantive +0.5, deontological_instrumental +0.7) [CHECKED by loading `tables.alignment`]. No axis names danger or risk (`descriptor_registry.yaml:168` onward) [CHECKED] | **decision-side.** Its draw is access, 16 of 20 (part 4 `:123`, and its coverage row `3/1/16/0`) [CHECKED]; capability, and so an attribute through it, gates no verb (`options.py:464`) [CHECKED]; its own entry says it *"may belong in the chooser"* (`:125-126`) [CHECKED] |
| **Constancy** | `rigid_flexible`, whose negative pole is glossed *"unwilling to deviate in the face of difficulties"* (`descriptor_registry.yaml:177`) [CHECKED]; cells `commit` −0.4, `comply` −0.4, `oblige` −0.3, `accept` −0.3, `tie / knot` −0.2 on that axis; `commit` is −0.8 on deontological_instrumental; `honour` projects −0.6 onto rigid_flexible [CHECKED by loading both tables] | **decision-side.** What remains is the time cost of long acts, which is budget, not a capacity [REASONED] |
| **Forethought** | none | **mixed.** Timing and choice (choosing the moment; `counsel`, `abdicate`, `withdraw`) is decision quality; `provision`, `tax`, `ration`, `audit`, `appraise` are execution, which the Derivation classed as practice (planning, numeracy) [READER for the classification; the verb list CHECKED at part 4 `:110-114`]. The effects of `provision`, `tax`, `ration` and `audit` were not opened [GAP: whether their effect half has any reader] |
| **Warmth** | `selfish_selfless`; the love, family and stewardship pursuits; stance | **mixed.** Caring is disposition; being liked is other persons' stance toward you, which is world state; little remains as a capacity (`tend`, `heal`, `rear`) [REASONED] |
| **Composure** | none | **resolver-side**: steadiness under scrutiny (part 4 `:140-147`) [CHECKED]. The registry's nine already house it, as Focus through Poise regathering (F16; `proposals/2026-10-16-attribute-derivation.md:187`) or as Will [READER] |
| **Watchfulness** | none. Observation is deposited by channel at WITNESS, not by a person's roll: WITNESS reads the log, presence and channel predicates (`engine/season/loop/witness.py:30`, `:44`), and its one draw (`:131`) is a confide rate, reading no capability [CHECKED] | a capacity whose reader would be information intake, not decision [REASONED] |
| **Bodily force, Quickness, Fine hand, Toughness** | none | capacities [REASONED] |
| **Reading people, Reasoning, Presence** | none directly; hierarchical_equal and grandiose_humble describe a style, not what works | capacities [REASONED] |
| **Thread perception** | none | separate: `Person.thread_sensitivity` (§2.1) [CHECKED] |

### 10.3 Composure and Nerve: are they one trait?

Jordan argued that they are. The measurement below is the overlap between the attributes' verb lists in
part 4's *recommended (14)* coverage table (`:226-243`), as the Jaccard index of verb-id sets [CHECKED:
re-run at `b7a1e1b`].

| pair | shared verbs | Jaccard |
|---|---|---|
| quickness / bodily force | 10 | 0.48 (the highest of the 91 pairs) |
| reading people / composure | 7 | 0.21 |
| nerve / quickness | 6 | 0.21 |
| nerve / composure | 3 (V011, V121, V129) | 0.09 |
| nerve / constancy | 1 (V118) | 0.02 |
| forethought / reasoning | 1 (V156) | 0.02 |

**Caveats, which bound everything the table can say.**

- The verb lists are the from-scratch author's judgement, and verbs-02 judges that set contaminated by
  its brief (`proposals/2026-10-16-verbs/2026-10-16-verbs-02-attributes.md:215-267`) [READER].
- Overlap measures acts demanded together, not variance shared across persons. It neither confirms nor
  refutes equivalence [REASONED].
- What it does show: the document does not support the equivalence *as it states the two*, because its
  lists split by situation — danger against scrutiny (part 4 `:120-122` against `:140-142`) [CHECKED].

**What supports Jordan's reading is the source's own line.** Part 4 splits Nerve from Composure as
*whether* against *how well* (`:125`; Composure is *"Not daring (nerve)"*, `:141`) [CHECKED]. That is the
line between chooser and resolver, so one trait — steadiness — appears at both layers [REASONED]. The
chooser half (Nerve) has no home today (§10.1); the resolver half (Composure) fits Will or Focus. A
further piece of support, found while writing this up: the Derivation already folds both into
`concentration` — *"absorbs composure and nerve (Merges)"* (`proposals/2026-10-16-attribute-derivation.md:384`,
row T06) [READER].

**Position:** not both as attributes.

**Reproducer** (`python3 -I`, from the repository root): read
`proposals/2026-10-16-attributes-from-scratch_part4.md`; take the text between `**recommended (14)**`
and `**smaller (8)**`; match each table row for the attribute name and its trailing `V\d+` list; compute
the Jaccard index for every pair. The script parses 14 rows whose set sizes equal the table's
*verbs served* column (constancy 30 … fine hand 11) [CHECKED].

### 10.4 The from-scratch document contradicts itself

- **P7** says an attribute is what a person *can* do, and what he *wants* to do is a value (part 4
  `:22`) [CHECKED]. Nerve is defined as *"willingness and ability to act in the face of danger"*
  (`:120`) [CHECKED]; reading Nerve and Constancy as willingness, both breach P7 [REASONED].
- **§6.4** sends access-movers to the chooser: values move access in 14 of 21 verbs (`:178`), and
  standing is excluded for moving access in 37 of 40 (`:185`) [CHECKED]. Nerve moves access in 16 of 20
  and is kept as an attribute (`:123`) [CHECKED].
- The Derivation had already classed boldness and patience as temperament — *"`disp` carried beside the
  attributes, not among them"* (`proposals/2026-10-16-attribute-derivation_aptitudes.md:50`, the
  *Not primaries* table) [CHECKED].
- Combat already carries a risk lean: `Combatant.disp`, 1–7, the aggression axis
  (`modules/combat/combatant.py:94`, `:99`) [CHECKED]. The season loop carries none: `Person` has no
  such field (§2.1) [CHECKED], and the season's combat seam leaves `disp` at its class default
  (`engine/season/seam/wrappers/combat.py:37-38`) [CHECKED].

### 10.5 Moving them is not free

- **There is no axis for risk.** Adding one changes `axis_roster`, the 15 × 7 projection and every verb's
  alignment cells (§10.1) [REASONED].
- **Under R7**, a risk appetite that varies independently of a person's pursuits must be a separate
  scalar — like `disp`, or a per-person `choice_temperature` — not an eighth projected axis [REASONED
  from R7 as quoted, READER].
- **Forethought has no decision-side home either.** The chooser scores one step; a person-level quality
  of foresight would have to enter through `budget`, the breadth of the option set, or temperature
  [REASONED].

### 10.6 Count, and the tension with the adjudication

Dropping Nerve and Constancy and splitting Forethought and Warmth leaves about ten capacities
[REASONED: a count, not a finding]. That lands near Verbs v2's nine plus Thread Sensitivity, which is
coincidence unless shown otherwise.

**The tension, recorded and not resolved.** The adjudication's six attributes — Body, Hand, Wit, Nerve,
Presence, Sense (§3 element 1) — retain Nerve. This addendum argues that Nerve is decision-side. The
adjudication's decisions stand as written above.

