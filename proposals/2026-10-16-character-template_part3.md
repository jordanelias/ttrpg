# The character template — part 3: §4–§10 (the loader, sourcing, adds and cuts, NERS, decisions, interactions, limits)

## Status: PROPOSED (2026-10-16). Not ratified; merge ratifies nothing unless Jordan so rules.
## Parts, in reading order: [head](2026-10-16-character-template.md) (§0–§3) · [`_part2`](2026-10-16-character-template_part2.md) (§3A) · **this file** (§4–§10).

---

## 4. THE LOADER AND THE RULES (code is the mechanism)

### 4.1 The typed artifact: `engine/season/characters.yaml`

**One new file, holding only what no existing file owns.** The template is an ASSEMBLY, not a copy.

| template part | its one owner (unchanged) | read through |
|---|---|---|
| name, faction, title, pursuits, affiliations | `references/npc_registry.yaml` | `cast.name_of`, `faction_of`, `title_of`, `pursuits_of`, `conviction_of` (`engine/season/data/cast.py:116-271`) [CHECKED] |
| institution, home, want, concerns | `engine/season/npcs.yaml`, generated from the cases and hand-correctable | `build_realm`'s roster read (`populated.py:835-839`) [CHECKED] |
| office, obligees | `engine/season/offices.yaml` | the office seating (`populated.py:1314-1328`) [CHECKED] |
| **birth tick, practice, attributes (Option B), and later kit** | **`engine/season/characters.yaml` (new)** | **`cast.template_of` (new, §4.2)** |

**Why not a new block in either existing file.**

- **`npc_registry.yaml` is canon, and it carries prose where numbers are due.** It holds `'75–80'`,
  `'~50'` and `'3–4'` (§5) and `[GAP]` strings. `cast.py` already declines to edit it: *"Quoting the
  two cells is a fix to the registry, which is canon and not this module's to edit"*
  (`cast.py:147-148`) [CHECKED]. A typed loader that refuses prose would refuse canon rows.
- **`npcs.yaml` is overwritten by its generator.** *"RE-RUNNING `--build` OVERWRITES HAND EDITS"*
  (`engine/season/npcs.yaml:8`) [CHECKED].

**The schema.** Shape only. The one value shown is NPC-088's, which exists today, with its own
stated basis.

```yaml
# engine/season/characters.yaml -- the authored capacity half of the character template.
# One row per cast case (ED-WR-0011: a closed authored cast). Absent or null = NOT AUTHORED.
characters:
  - case: NPC-088
    born: null                      # seasons old at tick 0; null -> Fixtures.age_at_build
    practice:                       # keys: rosters.yaml practice_roster (closed)
      copying:
        value: 3
        source: "engine/season/cases/exercises/NPC-088.yaml:32"
        grade: assumption           # the case says why: "chosen to be visibly non-default" (:25-28)
    attributes: {}                  # OPTION B ONLY; keys: descriptors.ATTRIBUTES; each {value, source}
```

### 4.2 The loader: `cast.template_of(case_id) -> CharacterTemplate`

**It lives in `engine/season/data/cast.py`.** That is the module that already owns reading the cast,
and the loader composes on its functions rather than re-reading anything (§8, single owner).
`CharacterTemplate` is a frozen dataclass, and the loader is lazy, like `cast._rows`
(`cast.py:26-29`, `:90-108`) [CHECKED].

**Refusals.** Each raises `Unspecified`, naming the row and the field, on the `cast.pursuits_of`
model (`cast.py:223-228`) [CHECKED].

| # | refuses | precedent |
|---|---|---|
| R1 | a key outside the closed set (`case, born, practice, attributes`; `kit` only once J-T5 lands) | `corpus_run.CAST_KEYS` (`engine/season/harness/corpus_run.py:312`); `cohort_rows`' extra-key refusal (`populated.py:364-369`) [CHECKED] |
| R2 | a `case` that is not a cast row (`cast.row(case) is None`), or a case twice | ED-WR-0011's closed cast |
| R3 | a non-null value with no `source:` | the registry's own `source:` column; `corpus_run`'s office `why` (W28) |
| R4 | an attribute key not in `ATTRIBUTES`, a value for the pending tenth, or a value not a whole number in `[ATTRIBUTE_FLOOR, ATTRIBUTE_CEILING]` | the leaf (`descriptors.py:50-53`) [CHECKED] |
| R5 | a practice key not on `practice_roster`, or a value not a whole number ≥ 0 | `corpus_run._check_capability` (`corpus_run.py:335-364`) [CHECKED], which becomes the ONE practice validator both paths call |
| R6 | a string where a number is due (`'3–4'`, `'~50'`) | §42.2's polarity, quoted in `cast.py:19-24` [CHECKED] |

**Defaults: null, never a guess.**

- An absent or null field means NOT AUTHORED. The template never writes a default value onto a
  person. The READER falls to its own declared default: `pool_default` (H-126), a module's class
  default, or `age_at_build`.
- This is the polarity `cast.py` states (*"It READS and VALIDATES; it does not translate and it
  does not guess"*, `cast.py:19-24`) [CHECKED], and the one `npcs.yaml` states for its rows
  (`npcs.yaml:12-16`) [CHECKED].
- **ED-WR-0011 is cited for the cast, not for the default.** It rules the cast CLOSED and AUTHORED
  (`editorial_ledger_wr_archive.jsonl:14`) [CHECKED], so there are template rows only for cast cases,
  and nothing generates one.

### 4.3 Relation to `npcs.yaml` and the cases

Names and wants stay the cases' own. `npcs.yaml` keeps generating `name` and `want` from the cases,
and `tools/export_npc_roster.py` is untouched. `characters.yaml` repeats none of those four fields.
A case added ahead of its registry row (the normal authoring order, `populated.py:883-888`)
[CHECKED] has no template row and seats on defaults, as it does today.

### 4.4 The seating step

- **`build_realm`.** Directly after the convictions are seated (`populated.py:896`) [CHECKED], one
  call, `seat_template(w, pid, cast.template_of(cid))`, writes three things and nothing else:
  - `born = -value` where `born` is authored;
  - `capability` from `practice`;
  - under B, `attributes`.

  Under 04 F.6 world-gen is that field's one seat-time writer (`04_CODE_ARCHITECTURE.md:1153`)
  [CHECKED]; `train` is the only runtime writer of `capability`.
- **Corpus `build_at`.** The `cast:` overlay keeps its shape (`CAST_KEYS`). Its `capability:` is
  validated by the same R5 validator, so one rule checks practice keys on both paths. Folding
  overlays into `characters.yaml` is NOT proposed: the overlays seat anonymous corpus seats (`p_a`),
  not cast case ids.
- **CENSUS.** `_individuate` mints with no template (`census.py:105`) [CHECKED].

### 4.5 Tests and falsifiers

These go in one new file, `engine/season/tests/test_character_template.py`.

1. **Refusals.** One planted row per R1–R6, each asserting the refusal names its row. The mutation
   check: delete the refusal and the test goes red.
2. **The all-null control.**
   - **Option A:** at `build_realm(0)`, and after 2 seasons, `World.content_hash()` equals the
     pre-change tree's, with the template file emptied.
   - **Option B:** the act log is equal under the same conditions. The hash is re-pinned, because
     `Person`'s `repr` gains `attributes` and `_entity_digest` hashes the `repr`
     (`state/world.py:167-177`) [CHECKED]. That is a declared structural move, the `Tenure.term`
     precedent (`carriers.py:103-105`) [CHECKED].
3. **One field, one divergence.** For each authored family (a practice key; an attribute under B;
   `born` at an `age_step` > 0 arm), two persons identical but for that field produce a different
   reader output, and over N seeds a different outcome rate. The control is the same pair with the
   field equal. The input half already ran in this pass (F14 and F15 probes).
4. **No field without a reader.** The test holds a table, accepted template key → the reader function
   it feeds. It fails on a key with no entry. This is load-bearing on the game: it is the template's
   own ID-13. It is not a guard on another guard (`CLAUDE.md` §0.1 pt 5).

### 4.6 The golden and hash consequences, declared

- **Option A.** Nothing moves until a value is authored, with one exception, and the exception is
  real. `build_realm` today seats NO `capability` for NPC-088's `p_npc_088`: the overlay is read
  only by corpus `build_at`. Through the template, the realm person would carry `copying: 3`, so the
  realm's content hash moves, and its `tell`/`speak` pools move for that one person. That is a
  behaviour change. Re-record and say so (`CLAUDE.md` §7).
- **Option B.** Everything in A, plus a structural move of every content hash for any world holding
  a `Person`.
- **The reach, counted.** `grep -rlE 'content_hash' engine/season/tests engine/tests tests/valoria | wc -l`
  → `55` files mention it. `grep -rlE '[0-9a-f]{32}' engine/season/tests engine/tests | xargs grep -l content_hash`
  → one source file pins a 32-hex digest beside it (`engine/season/tests/test_season_weather.py`).
  Golden JSON pins elsewhere were **not** enumerated [UNVERIFIED].

---

## 5. SOURCING DISCIPLINE

**What a template author may fill, and from what.** A value enters `characters.yaml` only with a
`source:` of one of four kinds:

- **(a) a case:** `path:line` in `engine/season/cases/`. The value carries the case's own grade
  (NPC-088's `3` is an `assumption` by its own text).
- **(b) a ruling:** an `ED-…` id or a v9 `RS-…` row whose text gives the number.
- **(c) a value Jordan supplies:** a dated quote.
- **(d) a registry cell:** `path:line` in `references/npc_registry.yaml`, and only where the cell is
  a number on the target scale under a registry name.

Everything else stays null. No author converts prose ("75–80", "~50", "3–4") into a number. That
conversion is a ruling, not authoring.

**How the 46 cast rows would read under the template.** The command, re-run for this table:

```
python - <<'EOF'
import yaml, collections
rows = yaml.safe_load(open("references/npc_registry.yaml"))["characters"]
present, nonnull = collections.Counter(), collections.Counter()
for r in rows:
    for k, v in r.items():
        present[k] += 1
        if v not in (None, "", [], {}) and not (isinstance(v, str) and v.strip().startswith("[GAP")):
            nonnull[k] += 1
EOF
```

It gave 46 rows. Present / non-null, per key:

| key | count |
|---|---|
| `id`, `first_name`, `faction`, `role`, `status`, `convictions`, `affiliations`, `source` | 46 / 46 |
| `last_name` | 46 / 44 |
| `arc_trajectory` | 42 / 36 |
| `ts` | 32 / 10 |
| `territory` | 31 / 7 |
| `goals` | 30 / 17 |
| `age` | 29 / 0 |
| `birthplace` | 29 / 5 |
| `coherence` | 29 / 1 |
| `stats` | 29 / 1 |
| `resonant_style` | 18 / 18 |
| `cultural_label` | 17 / 17 |
| `notes` | 15 / 15 |
| `certainty` | 8 / 8 |
| `title` | 7 / 7 |
| `self_other_initial` | 2 / 2 |

(`cultural_label` and `self_other_initial` are counted where they sit inside `convictions:` on most
rows. This top-level count sees only the rows that carry them at top level.)

| template field | source class | rows fillable today | rows null | note |
|---|---|---|---|---|
| `born` | (d) `age` | **0** | 46 | `age` non-null on 0 of 46 |
| `practice` | (a) a case naming a vocation `verb_capability` covers | **1** (NPC-088) | 45 | the plan's own count (`_part5.md:73`) [CHECKED]; NPC-088's magnitude is an `assumption` by its case text |
| `attributes` (B) | (d) `stats` | **1** row, **3** values (NPC-001: `cognition 5` → ACU via an `[ASSUMPTION]` alias; `focus 5`; `endurance 4`) (`npc_registry.yaml:57-61`) [CHECKED] | 45 | `social: '3–4'` refused: prose, and not a registry name |
| TS, if carried (J-T1a, §8) | (d) `ts` | **8** integers (NPC-003 25, NPC-004 15, NPC-005 35, NPC-020 28, NPC-030 0, NPC-070 0, NPC-075 60, NPC-080 0) | 38 | NPC-001 `'75–80'` and NPC-002 `'~50'` refused as prose |
| Coherence (WR's carrier) | (d) `coherence` | 1 (NPC-001: 9) | 45 | outside this template; listed so it is not lost |
| kit | none in the tree | 0 | 46 | waits on J-T5 |
| kin | none | 0 | 46 | waits on J-T3 |

**So the template ships nearly empty, and that is the honest state.** Under either option it changes
one realm person's pools (NPC-088) until someone supplies values under (a)–(d). R-09's by-person
conjunct therefore does not move on the template alone. It moves on J-T1 plus authored values. This
proposal invents none.

---

## 6. WHAT IT ADDS AND WHAT IT CUTS (the meta-rule)

**Added.**

| object | kind | under |
|---|---|---|
| `engine/season/characters.yaml` | one typed artifact | A, B |
| `cast.template_of` + `CharacterTemplate` | one loader function and its frozen record, in an existing module | A, B |
| `seat_template` | one world-gen call | A, B |
| `rosters.yaml: practice_roster` | one closed roster, absorbing `verb_capability`'s values | A, B |
| `Person.attributes` + its `write_matrix.yaml` row | one carrier field | B only |
| `engine/season/tests/test_character_template.py` | the falsifiers of §4.5 | A, B |

**Cut or subsumed.**

| object | what happens | why |
|---|---|---|
| `npc_registry.yaml`'s `stats:` and `ts:` as an ENGINE source | subsumed: the typed home is `characters.yaml`; the registry cells stay as canon reference, not deleted | no Python reads them: `grep -rnE '\bstats\b\|\bts\b' engine/season --include=*.py` finds only the docstring at `cast.py:6`; and they hold prose ranges |
| `verb_capability`'s value list as its own vocabulary | subsumed into `practice_roster`; the verb → key mapping stays | one roster of practice keys, not one per verb family |
| the corpus overlay's `capability:` validator as a second rule | folded: `_check_capability` becomes the one practice validator | `CLAUDE.md` §8, a rule lives once |
| `(Person, capability)` on `write_matrix.yaml`'s `retired:` list | comes off it, as IN-12 step 9 already plans | a carrier with a reader and two writers is not retired |
| the registry's `goals:` list as a template field | **not carried** (F9) | no reader; carrying it is the ID-13 defect |
| per-person scar thresholds | **not offered** | they would overwrite ruled constants (`person_q.py:468-469`) |
| the registry attribute `default: 1` as a seat-time fill | **not used** | it would make every unauthored person worse than every module default |

**Not touched.** The faction role template and the cohort template (§1), `Person`'s other twelve
fields, and the scene budget.

**The meta-rule check.** The addition is one file, one function, one call and one roster, plus one
field under B. No subsystem, no new act, no new Tenure kind.

---

## 7. NERS PASS (`skills/ners/SKILL.md`)

`[SELF-AUTHORED — bias risk]`. INSTRUMENTS: A (the shape) + read-only probes. GRADE: **paper**,
with input-level probes run (§10). No outcome distribution was measured.

### 7.1 N — the N-line ledger

| object | N-line | direction the loss falls in | attack run | verdict |
|---|---|---|---|---|
| `characters.yaml` + `template_of` | cut it and **the game cannot seat an authored capacity, age or kit on a named person**; every person rolls at `pool_default` | bottom-up (person → roll); top-down (creation screen → person) | assume it gone: does anything else seat practice on a realm person? `build_realm` seats none (`populated.py:864-896`), and the overlay is corpus-only | **N HOLDS** |
| the practice block | cut it and `train` raises a key world-gen never seeded: every person starts untrained, and the same act's odds never differ at tick 0 | vertical (template → `train`) | does `capability` already carry it? Yes, the CARRIER does; the template is its only authored SOURCE in the realm | **N HOLDS, NARROWED**: it is a source, not a carrier |
| `Person.attributes` (B) | cut it and the stubs' nine attribute channels never vary by person | bottom-up (person → `Combatant`, `Officer`) | do practice or body supply the same differences? No: `Combatant`'s seven attribute fields and `Officer`'s two have no practice or body input (§3.3) | **N HOLDS at T2, and does not hold at T1**: no season reader exists until K-1 or K-6 lands. Under PC-06's rule it ships with its first reader or not at all |
| `born` authoring | cut it and every person is the same age | lateral (person vs person) | the hazard ships at 0 (`fixtures.py:542-544`) | **FALSE N-LINE TODAY**, by disqualifier 2: no producer moves an outcome while the rates are 0. Kept as a template key with a null default, because its reader exists and is one fixture away |
| a `name` field as template content | — | — | it is identity, not mechanism | not an N-line object; carried as identity |
| F9 `goals` | "a person's goals" | — | is it carried elsewhere? Ambition is the OUGHT `commit` (F6), and `goals.yaml` carries organization goals | **FALSE N-LINE**, by disqualifier 1 |
| per-person scar thresholds | "persons break at different points" | — | ruled constants | **FALSE N-LINE**, by disqualifier 3 (already ruled) |
| registry `stats:` as a source | "the cast's authored stats" | — | 1 of 46 rows, legacy keys, a prose range | **FALSE N-LINE** as a source of the attribute block, by disqualifier 2 (no producer for 45 rows); kept as a source class for the one row |

### 7.2 E (scored last, as a ratio)

- **E-OVERHEAD.** The template adds one file and one function against N lines that hold for the
  practice block and the artifact. The denominator (§5.1 of the skill) is authoring: 46 rows × the
  practice keys, and under B × 9 attributes, of which 0 and 3 exist. **The ratio is favourable for
  the shape and unfavourable for B's content until values exist.** That is a finding, not a pass.
- **E-LEGIBILITY.** Under B a player can read "stronger, quicker" off a sheet and predict combat.
  Under A a player reads "practised in X" and predicts X. Both are legible. B adds multi-axis
  combinations the player cannot see (§3A.4: reading is `(2·cog + att)/3 + …`). **E-LEGIBILITY
  FINDING under B**: the sheet shows attributes, and the outcome turns on blends. The repair is
  K-GO-6's derivation view, an existing recommendation, not a new object.

### 7.3 R — both halves

- **R-COMPLETE.** FINDINGS: four open cells (§3A: `forge`'s quality, `argue`, `interrogate`, the
  lie) and P1's competence axis. Under A, the knot gate has no input (§3.3).
- **R-VARIETY.**
  - Today: **FINDINGS**. Persons vary in choice and never in odds, so "a single build answers
    everything": every build is the same build.
  - Under A: varies by practice only.
  - Under B: varies by attribute and practice.
- **R-PLAYER.** The creation screen (K-GO-8) writes a template row. The player's customization is
  exactly the template's authored fields. Under A it is practice, values, ties, home and office;
  under B, also the ten. **R-PLAYER at the creation seat is NOT SCORABLE** until J-T1.
- **R-WORLD** (drama with no player): today, NPCs who differ only in wants and values produce
  different choices and identical contests. Under A and B the commander's quality reaches a field
  (D3), and a fight between two NPCs varies by who they are. **The half with no player is where
  the template pays most.** A field's outcome depends on who commands it, with no player present.

### 7.4 S — six directions, plus pause and methodology

| direction | test | verdict |
|---|---|---|
| bottom-up | template → `Person` → each input builder (§3.1) | PASS by shape; under B, K-1 and K-6 are the carriers each step needs |
| top-down | a field's command → the commander's template | PASS under both (B: CHA, ACU; A: PRA[command]) |
| vertical | world-gen → `train` → the same key | PASS: one carrier, two writers in sequence (04 F.6) |
| lateral | a person vs a person in one contest | PASS: the opposed pair already reads the same key on both sides (`sigma.py:112-129`) |
| horizontal | contest vs combat vs threadwork | **FINDING (methodology)**: one quantity, PRA, becomes dice by three conventions. Sigma: pool = the value (`sigma.py:109`). Combat: pool = `max(5, history + 6)` (`core.py:54-56`). Threadwork: `min(3, history + 3)` inside a sum (`operations.py:246`) [CHECKED]. Under S's *"calculations consistent in methodology"* this is two (three) ladders for one quantity. Not repaired here: each is its subsystem's ruled formula. Raised as J-T6 |
| diagonal | an office holder's practice vs his office's remit | PASS: kept apart by §3.3 (office grants options and scenes, never capacity) |
| pause | — | N-A: the template acts at world-gen only |

### 7.5 The design's own falsifier, and the self-audit

- **§4.5 test 4** (no accepted key without a reader) is the template's own falsifier. Run by hand
  against §2:
  - F9 hits, and is not carried;
  - F13 passes at T1 (dark);
  - F16 hits at T1 under B, and is held behind K-1 and K-6;
  - **0 unhandled hits.**
- **9a (backward propagation).** §0 item 3's count (9/1/3/2/6) was re-derived against §2's list
  after the table was written: equal. §0 item 6's verb counts were re-derived against §3A.1:
  45/16/19/3 = 83.
- **9b (my additions).** `practice_roster` absorbs an existing roster (disqualifier 1 checked: it
  is not a second home, because `verb_capability`'s values move into it). `seat_template` is one
  call beside an existing seating block. `Person.attributes` is K-2's, which PC-06 already gated;
  this proposal does not ship it without a reader.
- **What an independent reviewer would add.** Re-open each of `_part2`'s per-verb lines. Run a
  seeded outcome comparison (not just inputs) for one practice key. Read the quarantined
  combat/threadwork/contest designs this pass did not open (§10).

---

## 8. DECISIONS FOR JORDAN

**Each was put through `CLAUDE.md` §0's five answers first.** Escalated only where none answered it.

| id | decision | options | effect on the game | what waits | §0 test result |
|---|---|---|---|---|---|
| **J-T1** | the capacity source | **A** derived (practice, body, kit, office) · **B** stored ten attributes + practice | A: persons differ only by practice; the ruled ten is overwritten. B: persons differ innately; J-13 read narrowly | R-09 by-person; K-1, K-6; the troop design's commander; K-GO-8 | **escalated**: two defensible options, materially different games, and one overwrites ratified canon |
| **J-T2** | the tenth attribute's name (B only) | candidates WITH a T2 reader: TMP (`disp`), TS, `resilience`; Recall has none | decides which subsystem gains a by-person input | B's roster closes; Godot fields bind (`CLAUDE.md` §5) | **escalated**: already Jordan's (ED-IN-0193; `_part5.md:444`) |
| **J-T3** | does kin or lineage enter the template | (i) no; (ii) a kin Tenure kind with a reader (inheritance through `succeed`, feud through stance) | (ii) gives the world dynasties and blood feuds without a player | F20; succession reads | **escalated**: no carrier, no ruling, no precedent; a live design choice |
| **J-T4** | do attributes change after tick 0 (B only) | none · age · wounds | none: training is the only growth. Age or wounds: the bodies pass reaches capacity | B's write rule | **escalated**: changes what `train` is worth |
| J-T1a | TS's carrier | a `thread_sensitivity` field on `Person` (K-3) | — | the thread rows | **answered by ratification**: K-3 is *"RATIFIED AS INTENT (v9)"* (`_part8.md:207`) [CHECKED]. Take K-3's field, not a `capability` key |
| J-T5 | kit's carrier | `hold` Tenures on equipment objects (K-5) · the person-rung's `Rung.stores` (the troop design's choice for companies) | — | F18 | **answered by precedent [medium; Jordan to correct]**: the troop design keeps a company's kit in its person-rung's stores (`troop-stock-design.md:326`), which needs no new object kind. One kit model for both scales (U-2's "one equipment model") favours the same. Its cost: a specific named sword has no identity |
| J-T6 | one ladder from practice to dice | keep three subsystem formulas · one shared conversion | §7.4's methodology finding | — | **answered by architecture**: each formula is its subsystem's ruled one. Recorded as a known S defect, not escalated |
| J-T7 | the player-character template vs the NPC one | the same template; the creation screen writes a row | — | K-GO-8 | **answered by precedent**: IN-47's review takes the fallback that the player picks a seated person (`_part4.md:41`) [CHECKED]. One template, one class (S9.1, `carriers.py:644`) [CHECKED] |
| J-T8 | commanders and troops | commanders: the character template; companies: the cohort template | — | the troop design | **answered by architecture**: one `Person` class; a company is a cohort (`troop-stock-design.md:317-328`) [CHECKED] |
| J-T9 | which axis competence reads (B only) | ACU · ATT · PRA[`inquiry`] only | how witnesses and investigators differ | K-FI-1, H-200 | **folded into J-T1/J-T2**: under A it is PRA, and under B it needs one of the nine. Asked with J-T1, not separately |

---

## 9. INTERACTIONS

| id | what it is | how the template meets it |
|---|---|---|
| **IN-12 step 9** (`_part5.md:73`) | `train` writes `Person.capability` | the template seeds the SAME keys at world-gen; `practice_roster` is the shared key set. Under J-13 (iii) `train` writes only where a case names a vocation; the template does not widen that, it gives it a place to start from |
| **IN-47** (`_part4.md:39-44`) | the character-sheet spaces | creation is a template row, and C1's blocker (*"no `pursuits` key; `CAST_KEYS` is closed"*) is met by the template carrying the authored fields |
| **IN-46** (`_part4.md:32-37`) | the grid suspension | its DEPS name *"IN-47's carriers where a party is built from a person"*; under B that is K-1 reading the template's attributes |
| **IN-64** | every NPC carries 15 pursuits and the three concerns | composed on, not repeated: `pursuits_of` and `conviction_of` already refuse incomplete rows |
| **IN-34** / H-208 | ageing, dark | `born` becomes authorable; the rates stay Jordan's |
| **K-2 / PC-06** (`_part7.md:44`) | `Person.attributes`, *"not ratified"*, only with its first reader | Option B is K-2 with its readers named; it does not ship ahead of K-1 or K-6 |
| **MB commanders** (K-6, U-4; M-MB-3) | `Officer` from the commander | D3; the troop design's §4 defers the commander's capacity to *"R-C-1/J-13"* (`troop-stock-design_part2.md:75-76`) [CHECKED], which is J-T1 |
| **the troop-stock design** (`proposals/2026-10-16-troop-stock-design.md`, present, read in part) | a company's grade in its own `capability` | **a key-space interaction**: character practice keys and a company's grade key share one carrier. `practice_roster` must either list the grade key or keep a disjoint namespace. The template loader refuses the grade key on a character row (R5) |
| **SC-01 / SC-02**, K-SC-2 | proceedings own the obstacle; the contest faculty | D1: CHA's Face ceiling waits on the proceedings subsystem |
| **FI**, H-200, K-FI-1 | competence | P1 and J-T9 |
| **WR**, K-3, K-WR-2 | TS, Coherence; thread operations as acts | D5, J-T1a |
| **GO**, K-GO-8 | the creation screen writes a cast entry | the template is that entry |
| **R-06, R-07, R-09** (`requirements.yaml:954`, `:1152`, `:1281`) | built characters; feelings and relationships; a probabilistic chain | R-06 gains the capacity and age halves of "robustly built"; R-07 is unchanged (stance and regard are not template work); R-09's by-person conjunct moves only with J-T1 plus authored values (§5) |
| hole rows | H-185 (F6's predicate), H-200 (P1), H-208 (F13), H-170 (the cohort template's weight), H-49 (`weight`'s runtime writer, closed by the troop design's `levy`), H-182 (F, D6: `tie / knot` has no effect) | each is named at its field; the template closes none of them alone |

---

## 10. LIMITS

**Opened in this pass** (each locator cited above was opened unless marked [UNVERIFIED]):

- **Code:** `state/carriers.py`, `data/cast.py`, `harness/populated.py`, `harness/corpus_run.py`,
  `seam/wrappers/sigma.py`, `seam/wrappers/combat.py`, `seam/wrappers/mass_battle.py`,
  `decision/budget.py`, `decision/choose.py` and `decision/options.py` (by grep and line),
  `queries/person_q.py` and `queries/world_q.py` (by grep and line), `loop/census.py`,
  `loop/resolve.py` (the scar and crisis bodies), `state/world.py` (`_entity_digest`,
  `content_hash`), `data/fixtures.py` (the person knobs), `modules/social_contest/roll.py`,
  `modules/combat/combatant.py`, `modules/combat/core.py`, `modules/combat/combat_systems.py`
  (lines cited), `modules/combat/fight.py:45`, `modules/mass_battle/hierarchy/units.py`,
  `modules/mass_battle/core/exchange.py`, `modules/mass_battle/orchestration.py` (the two checks),
  `modules/mass_battle/resolution.py` (the charge), `systems/threadwork/sim/operations.py`,
  `systems/fieldwork/sim/knots.py`, `systems/social_contest/sim/contest/resolver.py` and
  `primitives.py`, `engine/substrate/descriptors.py`.
- **Data:** `engine/season/rosters.yaml` (verb_capability, role_templates, faction_leaders, tenure
  kinds), `verb_table.yaml` (row list, `forge`), `write_matrix.yaml`, `npcs.yaml`, `offices.yaml`,
  `requirements.yaml` (R-06, R-07, R-09 and the scales note), `hole_register.yaml` (the named rows,
  by parse), `cases/exercises/NPC-088.yaml`, `references/npc_registry.yaml`,
  `references/descriptor_registry.yaml`.
- **Layer 1 and plan:** `01_AXIOMS.md` (ID-13, AX-7), `04_CODE_ARCHITECTURE.md:1153`, v9
  (`_part4`, `_part5`, `_part7`, `_part8` at the lines cited).
- **Ledgers:** ED-IN-0185, ED-IN-0193, ED-WR-0011.
- **Proposals:** `2026-08-15-…-progression.md` (§1.3–§3), `2026-09-30-…/09_the_character_sheet.md`
  (K-rows), `2026-10-16-troop-stock-design.md` (§0, §2.2–§2.3) and `_part2` (§4 items 4–5).
- **Research and scratch:** `research/by_lane/` (rows grepped, not whole files), scratch
  `briefs/JORDAN_STATEMENTS.md`, and `critics/*.md` and `out/UP*.md` (grepped).

**Probes run (read-only; scripts in the session scratchpad, not committed).**

1. `cap_count.py` over all 143 corpus cases and `build_realm(0)` printed
   `corpus persons 430 nonempty capability 1 [('NPC-088', 'p_a', {'copying': 3})]` and
   `realm persons 83 cohorts 37 nonempty capability 0 distinct born [0] distinct body [1000] nonempty conviction 46 nonempty pursuits 46 nonempty stance 35`.
2. `change_probe.py 4` (4 realm seasons, seed 0) printed
   `persons at build 83 at end 63 {'conviction': 0, 'pursuits': 0, 'body': 4, 'stance': 0, 'capability': 0, 'scar_nonempty': 27}`.
   This compares the 63 present at the end. Why 20 are gone was not examined.
3. The inline build check printed: cast 46, non-empty ledger 0; live tenure kinds on the cast
   `commit 141, hold 47, contain 46, reside 46, oblige 2`; 31 cast hold ≥ 1 `hold`.
4. The inline sigma and combat probe printed `pool tell a,b 2 5 | pool fight b 2`,
   `ob vs a,b 2.0 2.5`, `party_end a,c 4 2`.
5. The `ATTRIBUTES` importer grep printed one hit, a comment in `state/gate.py:1269`, and no
   importer.

**Not checked.**

- No pytest run. No seeded OUTCOME comparison (probes 4 and 5 are inputs only).
- The quarantined designs: `.designs/` threadwork, personal-combat reference, social-contest
  parameters, fieldwork. **Not opened**: the demand table's T4 rows rely on proposals and scratch
  extracts instead.
- The uploads behind `out/UP*.md`: not opened; cited as scratch extracts.
- The bodies of the contest moves `pass` and `rebut`, the mass-battle `brace`,
  `world_q.residence_of`, and the readers of an `oblige` beyond `imposed`.
- Golden JSON pins.
- The lane reference for P2.
- The 2026-08-15 proposal's measured attribute spreads (not re-run).

**Locator corrections.**

- The brief's pointers to `_part5` around `:504` and `:515` do not exist in this tree
  (`wc -l` → 475). The J-13 text is at `:433`, and the ten-attribute evidence at `:444`.
- The research suite's *"[CHECKED p5:515]"* (`00_COMPARATIVE_ANALYSIS.md:78, :214, :528`) and the
  critics' `_part5:504` and `:514` point at the same missing lines.

**Locator count, and the brief's aim of at most 70.** The aim is NOT met. The added demand table,
the when-complete stub sources and the master verb table each brought their own sources.

The count, by `grep -oE '[A-Za-z0-9_./-]+\.(py|yaml|md|jsonl):[0-9]+' <file> | sort -u | wc -l`:

| file | distinct `path:line` locators | bare continuation locators (`` `:NNN ``) |
|---|---|---|
| the head | 120 | 23 |
| `_part2` | 55 | 38 |
| this part | 45 | 8 |

Most of `_part2`'s come from one reproducible command, `grep -n '^  - verb:' engine/season/verb_table.yaml`.
