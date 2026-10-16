# The character template — part 3: §4–§10 (the loader, sourcing, adds and cuts, NERS, decisions, interactions, limits)

## Status: PROPOSED (2026-10-16). Corrected three times the same day against three independent critics' reports (all three reconciliation tables at the end of this part). Not ratified; merge ratifies nothing unless Jordan so rules.
## Tags as in the head: [CHECKED] opened in the fourth pass (the third correction); [CHECKED-3] opened in the third pass only; [CHECKED-2] opened in the second pass only; [CHECKED-draft] opened in the drafting pass only; [RAN] run, with its artifact named in §10.
## Parts, in reading order: [head](2026-10-16-character-template.md) (§0–§3) · [`_part2`](2026-10-16-character-template_part2.md) (§3A) · **this file** (§4–§10).

---

## 4. THE LOADER AND THE RULES (code is the mechanism)

### 4.1 The typed artifact: `engine/season/characters.yaml`

**One new file, holding only what no existing file owns.** The template is an ASSEMBLY, not a copy.

| template part | its one owner (unchanged) | read through |
|---|---|---|
| name, faction, title, pursuits, affiliations | `references/npc_registry.yaml` | `cast.name_of`, `faction_of`, `title_of`, `pursuits_of`, `conviction_of` (`engine/season/data/cast.py:116-271`) [CHECKED-draft] |
| institution, home, want, concerns | `engine/season/npcs.yaml`, generated from the cases and hand-correctable | `build_realm`'s roster read (`populated.py:835-839`) [CHECKED-draft] |
| office, obligees | `engine/season/offices.yaml` | the office seating (`populated.py:1314-1328`) [CHECKED-draft] |
| **birth tick, practice, Thread Sensitivity (J-T1a), attributes (Option B), and later kit** | **`engine/season/characters.yaml` (new)** | **`cast.template_of` (new, §4.2)** |
| a corpus world's per-seat `capability:` | the case's own `cast:` overlay (e.g. `engine/season/cases/exercises/NPC-088.yaml:29-33`) [CHECKED-2] | `corpus_run.build_at`, as today. **The template never copies an overlay value** (§4.4) |

**Why `engine/season/` and not `references/`.** `CLAUDE.md` §0.05 clause 1 names YAML under
`references/` or a single Python owner as the head of a fact code reads. The season's own runtime
registries already sit beside the loop (`rosters.yaml`, `offices.yaml`, `npcs.yaml`), so this follows
that precedent. If the tree should move all of them, that is a separate decision; this proposal does
not take it.

**Why not a new block in either existing file.**

- **`npc_registry.yaml` is canon, and it carries prose where numbers are due.** It holds `'75–80'`,
  `'~50'` and `'3–4'` (§5) and `[GAP]` strings. `cast.py` already declines to edit it: *"Quoting the
  two cells is a fix to the registry, which is canon and not this module's to edit"*
  (`cast.py:147-148`) [CHECKED-draft]. A typed loader that refuses prose would refuse canon rows.
- **`npcs.yaml` is overwritten by its generator.** *"RE-RUNNING `--build` OVERWRITES HAND EDITS"*
  (`engine/season/npcs.yaml:8`) [CHECKED-draft].

**The schema.** Shape only. No value is shown, because none exists today under §5's sourcing rule:
NPC-088's `copying: 3` stays in its overlay, its one owner (`CLAUDE.md` §0.05 clause 3), and is not
copied here.

```yaml
# engine/season/characters.yaml -- the authored personal-input half of the character template.
# One row per cast case, while ED-WR-0011 (provisional by its own terms) stands. Absent or null = NOT AUTHORED.
characters:
  - case: NPC-001
    born: null                      # seasons old at tick 0; null -> Fixtures.age_at_build
    practice: {}                    # keys: rosters.yaml practice_roster (closed); each {value, source, grade}
    thread_sensitivity: null        # J-T1a; lands with its first reader; {value, source}
    attributes: {}                  # OPTION B ONLY; keys: descriptors.ATTRIBUTES; each {value, source}
```

### 4.2 The loader: `cast.template_of(case_id) -> CharacterTemplate`

**It lives in `engine/season/data/cast.py`.** That is the module that already owns reading the cast,
and the loader composes on its functions rather than re-reading anything (§8, single owner).
`CharacterTemplate` is a frozen dataclass, and the loader is lazy, like `cast._rows`
(`cast.py:26-29`, `:90-108`) [CHECKED-draft].

**Refusals.** Each raises `Unspecified`, naming the row and the field, on the `cast.pursuits_of`
model (`cast.py:223-228`) [CHECKED-draft].

| # | refuses | precedent |
|---|---|---|
| LR1 | a key outside the closed set (`case, born, practice, thread_sensitivity, attributes`; `kit` only once J-T5 lands; `thread_sensitivity` only once its first reader lands) | `corpus_run.CAST_KEYS` (`engine/season/harness/corpus_run.py:312`); `cohort_rows`' extra-key refusal (`populated.py:364-369`) [CHECKED-draft] |
| LR2 | a `case` that is not a cast row (`cast.row(case) is None`), or a case twice | ED-WR-0011's closed cast, provisional by its own terms (head §1) |
| LR3 | a non-null value with no `source:` | the registry's own `source:` column; `corpus_run`'s office `why` (W28) |
| LR4 | an attribute key not in `ATTRIBUTES`, a value for the pending tenth, or a value not a whole number in `[ATTRIBUTE_FLOOR, ATTRIBUTE_CEILING]` | the leaf (`descriptors.py:50-53`) [CHECKED-2] |
| LR5 | a practice key not on `practice_roster`, or a value not a whole number ≥ 0 | `corpus_run._check_capability` (`corpus_run.py:335-364`) [CHECKED-draft], which becomes the ONE practice validator both paths call. **It refuses only keys off the roster**, so it keeps a non-practice key off a character row only while `practice_roster` does not list that key (§9, the troop design row) |
| LR6 | a string where a number is due (`'3–4'`, `'~50'`) | §42.2's polarity, quoted in `cast.py:19-24` [CHECKED-draft] |

**Defaults: null, never a guess.**

- An absent or null field means NOT AUTHORED. The template never writes a default value onto a
  person. The READER falls to its own declared default: `pool_default` (H-126), a module's class
  default, or `age_at_build`.
- This is the polarity `cast.py` states (*"It READS and VALIDATES; it does not translate and it
  does not guess"*, `cast.py:19-24`) [CHECKED-draft], and the one `npcs.yaml` states for its rows
  (`npcs.yaml:12-16`) [CHECKED-draft].
- **ED-WR-0011 is cited for the cast, not for the default.** It rules the cast CLOSED and AUTHORED
  (`editorial_ledger_wr_archive.jsonl:14`) [CHECKED-2], so there are template rows only for cast
  cases, and nothing generates one. It is *"PROVISIONAL BY ITS OWN TERMS"* (same line), so LR2 reads
  the cast from `cast.row`, never from a count of 46.

### 4.3 Relation to `npcs.yaml` and the cases

Names and wants stay the cases' own. `npcs.yaml` keeps generating `name` and `want` from the cases,
and `tools/export_npc_roster.py` is untouched. `characters.yaml` repeats none of those four fields.
A case added ahead of its registry row (the normal authoring order, `populated.py:883-888`)
[CHECKED-draft] has no template row and seats on defaults, as it does today.

### 4.4 The seating step

- **`build_realm`.** Directly after the convictions are seated (`populated.py:896`) [CHECKED-draft], one
  call, `seat_template(w, pid, cast.template_of(cid))`, writes these and nothing else:
  - `born = -value` where `born` is authored;
  - `capability` from `practice`;
  - `thread_sensitivity`, once J-T1a's field lands with its reader;
  - under B, `attributes`.

  World-gen seeds and `train` is the only runtime writer of `capability`: the shape 04 F.6's repair
  implies (head §3.5, write rule; `04_CODE_ARCHITECTURE.md:1153`) [CHECKED-2]. F.6's *"world-gen
  writes it once; nothing else does"* is the ASSUMED column of a failure table, not a rule, and is
  not cited as one.
- **Corpus `build_at`.** The `cast:` overlay keeps its shape (`CAST_KEYS`) and **stays the one owner
  of its `capability:` values**. The template copies none of them: NPC-088's `copying: 3`
  (`cases/exercises/NPC-088.yaml:32-33`) [CHECKED-2] stays where it is, and the realm's `p_npc_088`
  seats no capability, as today. The overlay's values are validated by the same LR5 validator, so one
  rule checks practice keys on both paths. Folding overlays into `characters.yaml` is NOT proposed:
  the overlays seat anonymous corpus seats (`p_a`), not cast case ids, and folding would make two
  owners of one fact.
- **CENSUS.** `_individuate` mints with no template (`census.py:105`) [CHECKED-draft].

### 4.5 Tests and falsifiers

These go in one new file, `engine/season/tests/test_character_template.py`.

1. **Refusals.** One planted row per LR1–LR6, each asserting the refusal names its row. The
   mutation check: delete the refusal and the test goes red.
2. **The all-null control.**
   - **Option A, before J-T1a's field lands:** at `build_realm(0)`, and after 2 seasons,
     `World.content_hash()` equals the pre-change tree's, with the template file emptied.
   - **Option A once `thread_sensitivity` lands, and Option B always:** the act log is equal under
     the same conditions. The hash is re-pinned, because `Person`'s `repr` gains a field and
     `_entity_digest` hashes the `repr` (`state/world.py:167-177`) [CHECKED-draft]. That is a
     declared structural move, the `Tenure.term` precedent (`carriers.py:103-105`) [CHECKED-draft].
3. **One field, one divergence.** For each authored family (a practice key; an attribute under B;
   `born` at an `age_step` > 0 arm), two persons identical but for that field produce a different
   reader output, and over N seeds a different outcome rate. The control is the same pair with the
   field equal. The input half ran (F14 and F15 probes, §10 probe 4) [RAN].
4. **No field without a reader.** The test holds a table, accepted template key → the reader function
   it feeds. It fails on a key with no entry. This is load-bearing on the game: it is the template's
   own ID-13. It is not a guard on another guard (`CLAUDE.md` §0.1 pt 5).

### 4.6 The golden and hash consequences, declared

- **Option A.** No behaviour moves until a value is authored: the template copies no overlay value,
  so NPC-088's realm person keeps seating no `capability`. **The content hash moves structurally
  once J-T1a's `thread_sensitivity` field lands** (a new `Person` field in the `repr`), and not
  before. (The first draft said A adds no field and moves no hash, and also proposed carrying
  NPC-088's `copying: 3` into the realm. Both are withdrawn.)
- **Option B.** A structural move of every content hash for any world holding a `Person`, when
  `attributes` lands; and J-T1a's, as under A.
- **The reach, counted** [RAN, second pass], over tracked source files only, so no
  `__pycache__/*.pyc` copy is counted:
  `for d in engine/season/tests engine/tests tests/valoria; do git grep -l content_hash -- "$d/*.py" | wc -l; done`
  → `17`, `0`, `2`: **19 source files** mention it. (The first draft's `grep -rlE … | wc -l` gave
  `55` because it counted compiled copies.)
  `git grep -lE '[0-9a-f]{32}' -- 'engine/season/tests/*.py' 'engine/tests/*.py' 'tests/valoria/*.py' | xargs git grep -l content_hash --`
  → one source file pins a 32-hex digest beside it (`engine/season/tests/test_season_weather.py`).
  Golden JSON pins elsewhere were **not** enumerated [UNVERIFIED].

---

## 5. SOURCING DISCIPLINE

**What a template author may fill, and from what.** A value enters `characters.yaml` only with a
`source:` of one of four kinds. **A magnitude never comes from prose.**

- **(a) a case's TEXT naming a vocation, for the KEY only:** `path:line` in `engine/season/cases/`
  where the case's prose names a vocation. It licenses WHICH practice key a person holds; its VALUE
  must come from (b), (c) or (d). A number read out of a case's prose is a conversion, which the
  rule below forbids. A value a case already seats through its `cast:` overlay stays there and is
  not repeated (§4.4): NPC-088's `3` is such a value, and an `assumption` by its own text
  (`NPC-088.yaml:23-28`) [CHECKED-2].
- **(b) a ruling:** an `ED-…` id or a v9 `RS-…` row whose text gives the number.
- **(c) a value Jordan supplies:** a dated quote.
- **(d) a registry cell:** `path:line` in `references/npc_registry.yaml`, and only where the cell is
  a number on the target scale under a registry name.

Everything else stays null. No author converts prose ("75–80", "~50", "3–4", or a case's
description of how good someone is) into a number. That conversion is a ruling, not authoring.

**How the 46 cast rows would read under the template.** The command, re-run in the second pass
[RAN] (its output below is the run's, and matches the drafting pass):

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
| `practice` | key: (a); value: (b)–(d) | **0** | 46 | the one case naming a vocation `verb_capability` covers is NPC-088 (`_part5.md:73`) [CHECKED-3], and its value stays in its overlay (§4.4); no ruling, Jordan value or registry cell gives another value |
| `attributes` (B) | (d) `stats` | **1** row, **3** values (NPC-001: `cognition 5` → ACU via an `[ASSUMPTION]` alias; `focus 5`; `endurance 4`) (`npc_registry.yaml:57-61`) [CHECKED-draft] | 45 | `social: '3–4'` refused: prose, and not a registry name |
| `thread_sensitivity` (J-T1a's field, either option) | (d) `ts` | **8** integers (NPC-003 25, NPC-004 15, NPC-005 35, NPC-020 28, NPC-030 0, NPC-070 0, NPC-075 60, NPC-080 0) | 38 | NPC-001 `'75–80'` and NPC-002 `'~50'` refused as prose |
| Coherence (WR's carrier) | (d) `coherence` | 1 (NPC-001: 9) | 45 | outside this template; listed so it is not lost |
| kit | none in the tree | 0 | 46 | waits on J-T5 |
| kin | none | 0 | 46 | not carried: no reader (J-T3, answered at step 5) |

**So the template ships nearly empty, and that is the honest state.** Under either option it changes
no outcome until someone supplies values under (b)–(d); it can seat at most NPC-001's three
attribute values under B and eight integer TS values once J-T1a lands. R-09's by-person conjunct
therefore does not move on the template alone. It moves on J-T1 plus authored values. This proposal
invents none.

---

## 6. WHAT IT ADDS AND WHAT IT CUTS (the meta-rule)

**Added.**

| object | kind | under |
|---|---|---|
| `engine/season/characters.yaml` | one typed artifact | A, B |
| `cast.template_of` + `CharacterTemplate` | one loader function and its frozen record, in an existing module | A, B |
| `seat_template` | one world-gen call | A, B |
| `rosters.yaml: practice_roster` | one closed roster, absorbing `verb_capability`'s values | A, B |
| `Person.thread_sensitivity` + its `write_matrix.yaml` row (J-T1a, K-3) | one carrier field, landing with its first reader | A, B |
| `Person.attributes` + its `write_matrix.yaml` row | one carrier field | B only |
| `engine/season/tests/test_character_template.py` | the falsifiers of §4.5 | A, B |

**Cut or subsumed.**

| object | what happens | removes something that exists? | why |
|---|---|---|---|
| `npc_registry.yaml`'s `stats:` and `ts:` as an ENGINE source | subsumed: the typed home is `characters.yaml`; the registry cells stay as canon reference, not deleted | **no**: no engine code reads them today, so nothing is removed; the cut is of a future misuse | no game Python reads them [RAN, second pass]: `git grep -nE '\bstats\b\|\bts\b' -- 'engine/season/*.py'` matches the docstring at `cast.py:6` and two local variables named `ts` in tests (`test_h134_candidate_per_seat.py:117-120`, `test_season_shape.py:14963`); and they hold prose ranges |
| `verb_capability`'s value list as its own vocabulary | subsumed into `practice_roster`; the verb → key mapping stays | **no**: relocated, one list moves into another | one roster of practice keys, not one per verb family |
| the corpus overlay's `capability:` validator as a second rule | folded: `_check_capability` becomes the one practice validator | **no**: relocated; it was the only validator, and it gains a second caller | `CLAUDE.md` §8, a rule lives once |
| `(Person, capability)` on `write_matrix.yaml`'s `retired:` list | comes off it, as IN-12 step 9 already plans | **yes**: one `retired:` entry, and IN-12 step 9 already removes it | a carrier with a reader and two writers is not retired |
| the registry's `goals:` list as a template field | **not carried** (F9) | **no**: it was never carried | no reader; carrying it is the ID-13 defect |
| per-person scar thresholds | **not offered** | **no**: never existed | they would overwrite ruled constants (`person_q.py:468-469`) |
| the registry attribute `default: 1` as a seat-time fill | **not used** | **no**: nothing uses it today | it would make every unauthored person worse than every module default |

**So the cut column is thin, and says so.** Of seven rows, four remove nothing that exists (they
decline to build or use something: `stats:`/`ts:` as a source, `goals:`, scar thresholds,
`default: 1`), two relocate a list or a rule, and one removes a `retired:` entry that IN-12 step 9
removes anyway. The template's net effect on the tree is additive.

**Not touched.** The faction role template and the cohort template (§1); `Person`'s other **eleven**
fields (13 less `born` and `capability`, the two existing fields `seat_template` writes, §4.4); and
the scene budget.

**The meta-rule check.** The addition is one file, one function, one call and one roster, plus
`Person` fields: `thread_sensitivity` under either option (J-T1a), and `attributes` under B, each
landing only with its first reader. No subsystem, no new act, no new Tenure kind.

---

## 7. NERS PASS (`skills/ners/SKILL.md`)

`[SELF-AUTHORED — bias risk]`. INSTRUMENTS: A (the shape) + read-only probes. GRADE: **paper**,
with input-level probes run (§10). No outcome distribution was measured.

### 7.1 N — the N-line ledger

| object | N-line | direction the loss falls in | attack run | verdict |
|---|---|---|---|---|
| `characters.yaml` + `template_of` | cut it and **the game cannot seat an authored practice, attribute, age or kit on a named person**; every person rolls at `pool_default` | bottom-up (person → roll); top-down (creation screen → person) | assume it gone: does anything else seat practice on a realm person? `build_realm` seats none (`populated.py:864-896`), and the overlay is corpus-only | **N HOLDS** |
| the practice block | cut it and `train` raises a key world-gen never seeded: every person starts untrained, and the same act's odds never differ at tick 0 | vertical (template → `train`) | does `capability` already carry it? Yes, the CARRIER does; the template is its only authored SOURCE in the realm | **N HOLDS, NARROWED**: it is a source, not a carrier |
| `Person.attributes` (B) | cut it and the stubs' nine attribute channels never vary by person | bottom-up (person → `Combatant`, `Officer`) | do practice or body supply the same differences? No: `Combatant`'s seven attribute fields and `Officer`'s two have no practice or body input (§3.3) | **N HOLDS at T2, and does not hold at T1**: no season reader exists until K-1 or K-6 lands. Under the plan's rule for K-2 (*"builds only with its first reader"*, `_part7.md:44`) [CHECKED-3] it ships with its first reader or not at all; under V-2 only on rows declaring `contests:` |
| `Person.thread_sensitivity` (J-T1a) | cut it and TS has no carrier: `thread_read` stays unattemptable, and the knot's party gate and the thread pool read their `getattr` defaults | bottom-up (person → `thread_read`, knot, thread pool) | does `capability` carry it? It could, under a `ts` key; K-3 chose a field, ratified as intent | **N HOLDS at T2/T3, not at T1**: lands with its first reader (H-85's typed gate) |
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
  Under A a player reads "practised in X" and predicts X. Both are legible. B adds multi-input
  combinations the player cannot see (§3A.4: reading is `(2·cog + att)/3 + …`). **E-LEGIBILITY
  FINDING under B**: the sheet shows attributes, and the outcome turns on blends. The repair is
  K-GO-6's derivation view, an existing recommendation, not a new object.

### 7.3 R — both halves

- **R-COMPLETE.** FINDINGS: three **open** verb cells (§3A: `forge`'s quality, `restore` and
  `work`'s `× f(degree)`) and PD1b's competence input. Under A, the knot's gate and roll (BON, WIL)
  have no input (§3.3). Under B, the knot's BON gate has no lawful input unless V-2a is ruled, and
  the knot roll and the thread operations need rows declaring `contests:` (V-2).
- **R-VARIETY.**
  - Today: **FINDINGS**. Persons vary in choice and never in odds, so "a single build answers
    everything": every build is the same build.
  - Under A: varies by practice only.
  - Under B: varies by attribute and practice, on the verbs V-2 admits.
- **R-PLAYER.** If IN-47's creation arm C1 is taken (J-T7), the creation screen (K-GO-8) writes a
  template row, and the player's customization is exactly the template's authored fields. Under A it
  is practice, values, ties, home and office; under B, also the ten. **R-PLAYER at the creation seat
  is NOT SCORABLE** until J-T1 and IN-47's hold are both answered.
- **R-WORLD** (drama with no player): today, NPCs who differ only in wants and values produce
  different choices and identical contests. Under A and B the commander's quality reaches a field
  (CD3): not through the exchange pool, which at the defaults reads troop quality and numbers only,
  but through the reform gate, the recall and feint rolls, the morale-erosion divisors, `h_per_size`
  and the span of control (§3A.4). A fight between two NPCs varies by who they are. **The half with
  no player is where the template pays most.** How a field holds, rallies and pursues, and how many
  subunits one commander can hold, depend on who commands it, with no player present; how hard each
  side hits does not.

### 7.4 S — six directions, plus pause and methodology

| direction | test | verdict |
|---|---|---|
| bottom-up | template → `Person` → each input builder (§3.1) | PASS by shape; under B, K-1 and K-6 are the carriers each step needs |
| top-down | a field's command → the commander's template | PASS under both (B: CHA, ACU; A: PRA[command]) |
| vertical | world-gen → `train` → the same key | PASS: one carrier, two writers in sequence; the shape 04 F.6's repair (*"a `practice` verb"*, superseded by `train`) implies |
| lateral | a person vs a person in one contest | PASS: the opposed pair reads the same key on both sides, the teller's as pool and the hearer's as Ob (`sigma.py:112-129`) [CHECKED-3] |
| horizontal | contest vs combat vs threadwork | **FINDING (methodology)**: one quantity, PRA, becomes dice by three conventions. Sigma: pool = the value (`sigma.py:109`) [CHECKED-3]. Combat: pool = `max(5, history + 6)` (`core.py:54-56`) [CHECKED-2]. Threadwork: `min(3, history + 3)` inside a sum (`operations.py:246`) [CHECKED-3]. Under S's *"calculations consistent in methodology"* this is three ladders for one quantity. A fourth split would follow only if `thread_read`'s dice came from `capability`, which is an inference from the 2026-09-05 ruling and not a stated source (§3A row 40); as counted, `thread_read` keeps the Leap pool the seven stub operations use (§3A.4), with a different History ladder (`min(3, history + 3)` in the stub, a bare History in the fieldwork design). Not repaired here. The three ladders are NOT equally ruled: combat's is ratified (*"ED-901; re-ratified ED-900/904"*, `core.py:55`) [CHECKED-2]; threadwork's cites PP-624 (`operations.py:245`) [CHECKED-3]; sigma's "pool = the value" is an `assumption`-graded mapping (H-126; *"an `assumption` grade means inject the default"*, `sigma.py:105-107`) [CHECKED-3]; NPC-088's magnitude is a judgement call by its own text (`NPC-088.yaml:23-28`) [CHECKED-2]. Raised as J-T6 |
| diagonal | an office holder's practice vs his office's remit | PASS: kept apart by §3.3 (office grants options and scenes, never a personal input) |
| pause | — | N-A: the template acts at world-gen only |

### 7.5 The design's own falsifier, and the self-audit

- **§4.5 test 4** (no accepted key without a reader) is the template's own falsifier. Run by hand
  against §2:
  - F9 hits, and is not carried;
  - F13 passes at T1 (dark);
  - F16 hits at T1 under B, and is held behind K-1 and K-6;
  - **0 unhandled hits.**
- **9a (backward propagation).** §0 item 3's count (8/1/3/2/7) was re-derived against §2's
  partition: equal, and every F-row appears in exactly one class. §0 item 6's verb counts were
  re-derived against §3A.1: 37 + 8 + 12 + 7 + 1 = 65, and the personal-input split against §3A.3:
  11 + 2 + 9 + 43 = 65, with every step from the third pass's 10 + 3 + 10 + 42 shown there, and the
  counts under the readings not adopted (`speak` contested; the `thread_read` inference).
- **9b (my additions).** `practice_roster` absorbs an existing roster (disqualifier 1 checked: it
  is not a second home, because `verb_capability`'s values move into it). `seat_template` is one
  call beside an existing seating block. `Person.attributes` is K-2's, which the plan already gates
  behind its first reader; `Person.thread_sensitivity` is K-3's; this proposal ships neither
  without a reader.
- **What an independent reviewer would add.** Three independent critics re-opened the per-verb lines
  (22 findings, then 20, then 13; all reconciled at the end of this part). Still owed: a seeded OUTCOME
  comparison (not just inputs) for one practice key, and the quarantined combat and threadwork
  designs this proposal did not open (§10).

---

## 8. DECISIONS FOR JORDAN

**Each was put through `CLAUDE.md` §0's five answers first.** Escalated only where none answered it.

| id | decision | options | effect on the game | what waits | §0 test result |
|---|---|---|---|---|---|
| **J-T1** | the source of personal inputs | **A** derived (the personal inputs are practice and kit, with TS on its own field; body and office still differ by person but are not personal inputs) · **B** stored ten attributes + practice, read only through `faculty(domain)` on rows declaring `contests:` (V-2, V-3), with **V-2a** (a gate or cap may read a bare attribute) asked alongside for the knot · **A-1** six faculties + Recall and Bonds as gates, eight in all (2026-08-15 `:191`) [CHECKED-3] · **J-13 (ii)** a ruled rank scale for practice values, orthogonal to the others (`_part5.md:433`) [CHECKED-3] | A: persons differ only by practice; the ruled ten is overwritten. B: persons differ innately on the verbs V-2 admits; J-13 read narrowly. A-1: innate difference on six faculties; Focus and Charisma cut, Recall added, so the ruled ten is overwritten and `derive_command` loses its primary input | R-09 by-person; K-1, K-6; the troop design's commander; K-GO-8 | **escalated**: defensible options that lead to materially different games, and A and A-1 each overwrite a ruling. Escalating does not re-raise ED-IN-0185's closed agenda unless Jordan chooses an option that overwrites it (head §3.4) |
| **J-T2** | the tenth attribute's name (B only) | candidates with a T2 reader: TMP (`disp`), TS, RES (`resilience`). **Recall has no reader above T4**: the fieldwork design's `research` and `reconstruct` readings are overridden by the proceedings design author's sentence for those rows (T3, contestable), the v30 contest design's Appraise pool is superseded by the kernel, and the *"+2D Recall bonus"* is classed *"non-attribute"* by that design (`:97`, `:177`) though it also says Recall *"contributes to … the citation bonus"* (`:155`) [CHECKED]: T4 either way (head §3.1.1) | decides which subsystem gains a by-person input | B's roster closes; Godot fields bind (`CLAUDE.md` §5) | **escalated**: already Jordan's (ED-IN-0193; `_part5.md:444`) [CHECKED-3]. By ID-13, Recall is a candidate only if Jordan also gives it a reader |
| J-T3 | does blood kinship enter the template | (i) no; (ii) kin as a relation with a reader (feud carried through stance; a `tie` kind or a new Tenure kind) | (ii) gives the world blood feuds without a player | F20 | **escalated, narrowed.** Step 1 answers the inheritance half: *"designated heir is not a verb but a status or title. the heir still has to claim their throne"* (RS-27, `workplans/valoria_master_workplan_v9_part8.md:340`) [CHECKED-3], and RS-29 ratified the heir carrier, *"the `successions` registry naming the throne's heir seat; the title"* (`_part8.md:342`) [CHECKED-3]; the plan re-specifies `inheritance` to match (`_part5.md:432`; IN-61, `:244-246`) [CHECKED-3]. So an heir needs no kin field. **The remainder, re-run in the fourth pass (third critic, finding 13): answered for the template, not escalated.** Step 2: kin is not irrelevant, but nothing reads it at any tier (F20: no Tenure kind, no stub, no design reader). Step 3: ID-13, *"A DECLARED FIELD MUST REACH A READER, OR IT IS NOT DECLARED"* (`architecture/meta/01_AXIOMS.md:561`) [CHECKED], a Layer 1 rule (T3), decides what the TEMPLATE may carry: a field with no reader is not declared. Step 4: the template's own precedent, F9 (`goals:`), not carried for the same reason. Step 5: the research row places the live half elsewhere: *"R-07's relationships are carried by IN-32's `tie / knot`; whether kin is a tie kind is a design option (K-NPC-6), not a missing area"* (`research/by_lane/NPC_npc_cast.md:516`) [CHECKED]. So **(i) for the template**: kin is not carried. Whether kin becomes a `tie` kind with a reader is the `tie / knot` row's question (IN-32, K-NPC-6), not this proposal's; if that is ruled, the template gains a kin field WITH its reader. [medium; Jordan to correct]. Revert: Jordan rules kin a carried relation with a named reader |
| **J-T4** | do attributes change after tick 0 (B only) | none · age · wounds | none: training is the only growth, and age and wounds act only through `born` and `body`. Age or wounds: the bodies pass reaches every attribute it is wired to | B's write rule | **escalated** (B only). Re-run: step 1, nothing supersedes it. Step 2, it is live under B. Step 3 answers nothing: no head, Status line or spec rules it. K-2 is *"not ratified"* (`_part7.md:44`) [CHECKED-3]. The contest code's lines are the retiring kernel's, about Charisma alone: *"Charisma is a BUILD-TIME attribute (in player control)"* (`resolver.py:191-192`) and *"Build-time attribute — set by the player at creation, not by moment-to-moment play"* (`primitives.py:139-141`) [CHECKED-3], two files, quoted separately. 04 F.6's repair is about `capability`, *"a `practice` verb, not a field"* (`04_CODE_ARCHITECTURE.md:1153`) [CHECKED-2], not about attributes. Step 4: no precedent in the tree moves an attribute. Step 5 leans to none (no writer exists; age and wounds already have carriers, and a second channel for one effect would be an S defect), but the options lead to materially different games. **Interim, until ruled: none**, which is the code's state |
| J-T1a | TS's carrier | a `thread_sensitivity` field on `Person` (K-3) | — | the thread rows; `examine`'s depth gate; the knot's party gate | **answered by ratification**: K-3 is *"RATIFIED AS INTENT (v9)"* (`_part8.md:207`) [CHECKED-3]. Take K-3's field, not a `capability` key. **It adds a `Person` field under either option**, landing with its first reader; the hash consequence is §4.6's |
| J-T5 | kit's carrier for a person | `hold` Tenures on equipment objects (K-5) · a stores kind on a rung (the troop design's choice for a levy's kit: *"Kit is the town's"*, its §2.7) | — | F18 | **deferred, not answered.** There is no precedent the tree decided: the troop design is PROPOSED (its Status line) [CHECKED-3, by heading], and keeps kit on a settlement, not a person; U-2 is about merging equipment catalogues, not where a person's kit lives (`08_mass_battle_units.md:126`) [CHECKED-2]; and K-5 is unscheduled behind K-2 (`_part7.md:44`) [CHECKED-3]. Nothing reads kit off a person until K-1 lands, so nothing waits on this sooner; it is asked with K-1, and escalated then if §0's five answers still leave two options |
| J-T6 | one ladder from practice to dice | keep the subsystem formulas · one shared conversion | §7.4's methodology finding | — | **not escalated separately.** Combat's and threadwork's are their subsystems' formulas (ED-901; PP-624). Sigma's is an `assumption`-graded mapping (H-126), whose scale is already open as J-13's remainder (`_part5.md:443`) [CHECKED-3]; the shared-ladder question rides with that ruling. Recorded as a known S defect |
| J-T7 | the player-character template vs the NPC one | one template and one class; whether the creation screen writes a row | — | K-GO-8 | **half answered, at step 5; half already Jordan's.** One template, one class: architecture, *"ONE CLASS (S9.1)"* (`carriers.py:644`) [CHECKED-3]. Whether creation writes a row is IN-47's arm C1, and IN-47's review took the opposite fallback, *"the player picks a person the builder already seated"*, in a design *"HELD BACK from ratification-on-merge"* whose hold *"is released only by Jordan"* (`_part4.md:41`) [CHECKED-3]. So that half is not precedent for this proposal; it is not re-escalated, because it is already Jordan's inside IN-47. ⚠ The template does not by itself remove C1's blocker: its pursuits still come from the registry row (`cast.pursuits_of`, §4.1), so a created person would also need that row, or a pursuits key this proposal does not add |
| J-T8 | commanders and troops | commanders: the character template; troops: whatever the troop design's J-1 rules | — | the troop design | **commander half answered at step 5; troop half not this proposal's.** One `Person` class (`carriers.py:644`) [CHECKED-3], and the troop design names the general and officers from the persons present (its `_part2` §4.2, steps 4–5) [CHECKED-3, by heading]. What a troop is, is that proposal's **J-1**, open and Jordan's (its §2.4): default A, a troop stock on the rung that mints no `Person`; alternative P, a company `Person` (a cohort). This proposal decides neither |
| J-T9 | which personal input AX-7's competence at deposit reads (PD1b) | ACU · ATT · PRA[`inquiry`] only | how every witness, not only an investigator, credits what he hears | K-FI-1, H-200 | **folded into J-T1/J-T2**: under A it is PRA, and under B it needs one of the nine. V-2 binds verbs, not deposits, so it neither admits nor bars one. Asked with J-T1, not separately. (The inquiry acts' own dice are NOT part of this question: the proceedings design author's sentence gives the five `capability`, and `thread_read` keeps the fieldwork Leap pool, PD1a) |

---

## 9. INTERACTIONS

| id | what it is | how the template meets it |
|---|---|---|
| **IN-12 step 9** (`_part5.md:73`) | `train` writes `Person.capability` | the template seeds the SAME keys at world-gen; `practice_roster` is the shared key set. Under J-13 (iii) `train` writes only where a case names a vocation; the template does not widen that, it gives it a place to start from |
| **IN-47** (`_part4.md:39-44`) [CHECKED-3] | the character-sheet spaces | creation is *"a cast entry the world-gen builder seats"*; C1's blocker (*"no `pursuits` key; `CAST_KEYS` is closed"*) is narrowed by the template (one typed record over the assembled cast) and not removed (pursuits stay on the registry row). The review's fallback stands until Jordan releases the hold (J-T7) |
| **IN-46** (`_part4.md:32-37`) | the grid suspension | its DEPS name *"IN-47's carriers where a party is built from a person"*; under B that is K-1 reading the template's attributes |
| **IN-64** | every NPC carries 15 pursuits and the three concerns | composed on, not repeated: `pursuits_of` and `conviction_of` already refuse incomplete rows |
| **IN-34** / H-208 | ageing, dark | `born` becomes authorable; the rates stay Jordan's |
| **IN-61**, RS-27, RS-29 (`_part5.md:244-246`; `_part8.md:340`, `:342`) [CHECKED-3] | succession: the heir is a title, claimed by the heir's own act | the template carries no heir field: the carrier is the title (J-T3) |
| **K-2** (`_part7.md:44`) | `Person.attributes`, *"not ratified"*, only with its first reader | Option B is K-2 with its readers named; it does not ship ahead of K-1 or K-6 |
| **V-2, V-3** (`10_verbs_and_attributes.md:198-199`; `_part7.md:51`) [CHECKED-3] | an attribute reaches a verb only through a faculty, and only on a row with `contests:`; `faculty(domain)` owns the aptitude slot | Option B obeys both (head §3.3); the knot's bare-BON gate needs the proposed V-2a; `tie / knot` and the thread operations need `contests:` rows before WIL reaches them |
| **MB commanders** (K-6, U-4; M-MB-3) | `Officer` from the commander | CD3; the troop design holds every season commander's Command at 4 *"until R-C-1 names a source"* (its `_part2` §4.2, step 6) [CHECKED-3, by heading], which is J-T1. At the defaults Command reaches gates, rolls, divisors and the span of control, not the exchange pool (§3A.4) |
| **the troop-stock design** (`proposals/2026-10-16-troop-stock-design.md` and `_part2`, PROPOSED, being rewritten; cited by J-number and section number, headings quoted as they read in the fourth pass) | a raised troop is its J-1, default A, a troop stock on the rung (its §2.4); a stock's grade is a matter kind, `troops_<id>`, derived from `troop_grades` (its §2.7) [CHECKED-3, by heading] | **no key-space interaction under that design as it reads now**: no grade key enters any person's `capability` or `verb_capability`. If that changes, `practice_roster` must not list a grade key, because LR5 refuses only keys off the roster (§4.2). (The second pass's claim that LR5 refuses the grade key is withdrawn.) |
| **SC-01 / SC-02**, K-SC-2 | proceedings own the obstacle; the contest faculty | CD1: the contest reads PRA only; Charisma's Face view moves no outcome, so there is nothing for the proceedings subsystem to "land" from CHA unless a ruling gives Face a reader |
| **FI**, H-200, K-FI-1 | the inquiry verbs; competence at deposit | PD1a (`capability` dice for the five, by the design author's gloss on the 2026-09-05 ruling; the fieldwork Leap pool for `thread_read`; the concealer's Ob open), PD1b and J-T9 (open) |
| **WR**, K-3, K-WR-2 | TS, Coherence, resilience; thread operations as acts | CD5, CD6, J-T1a |
| **GO**, K-GO-8 | the creation screen writes a cast entry | the template is that entry, if IN-47's C1 is taken (J-T7) |
| **R-06, R-07, R-09** (`requirements.yaml:954`, `:1152`, `:1281`) | built characters; feelings and relationships; a probabilistic chain | R-06 gains the practice, attribute and age halves of "robustly built"; R-07 is unchanged (stance and regard are not template work); R-09's by-person conjunct moves only with J-T1 plus authored values (§5) |
| hole rows | H-185 (F6's predicate), H-200 (PD1b), H-208 (F13), H-170 (the cohort template's weight), H-49 (`weight`'s runtime writer; under the troop design's J-1 default `Person.weight` stops being a battle input, its §2.6), H-182 (CD6: `tie / knot` has no effect), H-85 (`thread_read`'s TS gate, J-T1a's first reader), H-164 (`restore`/`work`'s `× f(degree)`) | each is named at its field; the template closes none of them alone |

---

## 10. LIMITS

**Opened in the drafting pass** (each locator tagged [CHECKED-draft] was opened then):

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
  (K-rows), the troop-stock design (as it read then).
- **Research and scratch:** `research/by_lane/` (rows grepped, not whole files), scratch
  `briefs/JORDAN_STATEMENTS.md`, and `critics/*.md` and `out/UP*.md` (grepped).

**Opened in the second pass** (tagged [CHECKED-2]): every locator the first critic's 22 findings
name; `verb_table.yaml` (the 45 row lines, `speak`, the typed cells of `comply`, `give`, `survey`,
`reconstruct`, `thread_read`, `tie / knot`, the decline notes); the contest `resolver.py:180-236`,
`primitives.py:116-149`, `modes.py:414-450`, `wrapper.py:60-200` and `agon_harness.py` (by grep);
`knots.py:45-60`, `:170-225`; `config.py:246-247`, `:530-533`, `:550-560`;
`orchestration.py:282-330`; `units.py:2695-2722`; `resolution.py:132`, `:176`;
`effects_migration.py:190-198`; `effects_economy.py:110-122`, `:292-305`; `predicates.py:380-396`;
`gate.py:355-393`; `faction_q.py:186-196`; `options.py:1196-1212`; `rosters.yaml:1440-1465`;
`offices.yaml:128`, `:189-191`, `:589-591`; `NPC-088.yaml:18-36`; `descriptor_registry.yaml:27-48`,
`:61-65`; `descriptors.py:48-54`; `combatant.py:93-94`; `core.py:54-56`; `fight.py:45`;
`09_the_character_sheet.md:127-133`; the 2026-08-15 proposal `:147`, `:150-162`, `:170`;
`04_CODE_ARCHITECTURE.md:1144-1156`; the ED-IN-0185, ED-IN-0193 and ED-WR-0011 lines;
`research/by_lane/SC_social_contest.md:710`, `FA_faction_actions.md:582`.

**Opened in the third pass** (tagged [CHECKED-3]):

- **Designs and plan:** `.designs/systems/fieldwork/reference/fieldwork_v30.md`, **read in full**
  (quarantined; read for intent only); `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:425-580`
  and `06_RESOLUTION.md:40-80`; `10_verbs_and_attributes.md:110-205`; the 2026-08-15 proposal
  `:105-130`, `:185-206`, `:475-476`; `2026-10-03-verb-coverage-and-gap-fill.md` (its Status line,
  `:1826-1851`, and every §9 `contests:` line by grep); v9 `_part4.md:39-44`, `_part5.md:66-79`,
  `:244-246`, `:428-444`, `_part7.md:40-59`, `_part8.md:195-210`, `:340`, `:342`;
  `research/by_lane/NPC_npc_cast.md:514-518`; `FA_faction_actions.md:366` (first line).
- **The troop-stock design, by heading only** (being rewritten): its heading list; §2.4–§2.7;
  §3.1; `_part2` §4.2–§4.4, §4.7–§4.8, §9.
- **Code and data:** `sigma.py:75-150`; `rosters.yaml:1051-1082`, `:1098-1112`; `verb_table.yaml:936-960`,
  `:1040-1048`, `:1083-1085`, and its `contests:` lines by grep; `loop/resolve.py:730-750`;
  `exchange.py:50-66`; `core/state.py:100-108`; `orchestration.py:2216-2228`, `:2585-2600` (the
  `roll_pool` lines); `units.py:2739`, `:2815`, `:2888-2896`; `systems/mass_battle/sim/engine.py:88-99`,
  `:269-345` (by grep on `command`); `operations.py:150-160`, `:233-275`; `resolver.py:186-196`;
  `primitives.py:136-143`; `carriers.py:640-648`; `seam/wrappers/combat.py:130-136`;
  `engine/season/harness/aperture.py:104-236`; `world_q.py:1096-1097`.
- **The quarantined v30 contest design, by grep only:** `social_contest_v30.md:97`, `:155`, `:177`,
  `:267`, `:511`.

**Opened in the fourth pass** (tagged [CHECKED]), each at the third critic's locators and beside them:

- **Plan and designs:** v9 `_part8.md:199-208`; `_part6.md:22-26`, `:60-68` (SC-01, step 12);
  `_part7.md:51` (the V-2 entry); `2026-10-03-verb-coverage-and-gap-fill.md:1-3`, `:331`, `:356`,
  `:370-382`, `:405`, `:1295-1370`, `:2070`; `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:1-5`,
  `:55-75`, `:440-490`, and its `contests:` lines by grep; `21_RECONCILIATION.md` (`speak` by grep);
  `06_RESOLUTION.md:398-406`; `08_FUNCTION_SURFACE.md:164`; `10_verbs_and_attributes.md:138-150`,
  `:196-200`; `09_the_character_sheet.md:128-131`; the 2026-08-15 proposal `:145-148`, `:168-171`;
  `fieldwork_v30.md:108`, `:296-308`, `:327`, `:349-363`, `:615-619`; `social_contest_v30.md:97`,
  `:155`, `:177`; `architecture/meta/01_AXIOMS.md:559-563`.
- **Research rows:** `research/by_lane/WR_world.md:536-540`; `SC_social_contest.md:149`, `:205`,
  `:370-378`; `NPC_npc_cast.md:514-518`.
- **The troop-stock design** (being rewritten): its heading list, Status and header lines, §2.6,
  §2.7, §3.1's opening and illustrative row, `_part2` §9 (the J table), and a grep for `R-C-1`,
  `trim_to_command`, *"Kit is the town's"* and `conscript`.
- **Code and data:** `engine/season/queries/inputs.py:40-60`; `engine/season/rosters.yaml:1049-1078`;
  `verb_table.yaml:950-954`, `:1083-1086`, and its `contests:` lines by grep;
  `systems/threadwork/sim/operations.py:249-275`, `:310-325`, `:451`, `:505-575`, and its
  `attempt_*` and `coherence_delta=` lines by grep; `systems/fieldwork/sim/knots.py:183-187`,
  `:210-216`.

**Probes run (read-only; scripts in the session scratchpad,
`/tmp/claude-0/-home-user-ttrpg/3f6de207-94f6-530b-a5b4-52aac53c2712/scratchpad/tmpl/`, not
committed). Every figure below is the artifact's printed output [RAN].**

1. `tmpl/cap_count.py` → `tmpl/cap_count.out` (second pass): `cases 143`,
   `corpus persons 430 nonempty capability 1 [('NPC-088', 'p_a', {'copying': 3})]` and
   `realm persons 83 cohorts 37 nonempty capability 0 distinct born [0] distinct body [1000] nonempty conviction 46 nonempty pursuits 46 nonempty stance 35`.
2. `tmpl/change_probe.py 4` → `tmpl/change_probe.out` (second pass): `seasons 4 persons at build 83 at end 63 {'conviction': 0, 'pursuits': 0, 'body': 4, 'stance': 0, 'capability': 0, 'scar_nonempty': 27}`.
   This compares the 63 present at the end. Why 20 are gone was not examined.
3. `tmpl/probes345.py` → `tmpl/probes345.out` (third pass; the second pass ran it inline with no
   artifact, and the figures reproduce): `cast 46 nonempty ledger 0`; tenure kinds
   `{'commit': 141, 'contain': 46, 'hold': 47, 'oblige': 2, 'reside': 46}`; `cast holding>=1 hold 31`;
   stance rows per person `[(0, 11), (1, 5), (2, 22), (3, 6), (6, 2)]`.
4. Same artifact, three realm persons (`capability` `{}` and `{copying: 5}`; `body` 100 on the third):
   `pool_default 2 obstacle_default 2`, `pool tell a,b 2 5 | pool fight b 2`, `ob vs a,b 2.0 2.5`,
   `party_end a,c 4 2`.
5. Same artifact: `git grep -nE 'import[^#]*\bATTRIBUTES\b|descriptors\.ATTRIBUTES|ATTRIBUTE_(FLOOR|CEILING)|ATTRIBUTES_PENDING' -- '*.py' ':!engine/substrate/descriptors.py'`
   printed three lines, all in `tests/valoria/test_descriptors_runtime.py`: no importer in
   `engine/`, `modules/`, `systems/` or `tools/`. (The first draft's grep matched the English word in
   a comment, `state/gate.py:1269`.)
6. `tmpl/aperture4.py` → `tmpl/aperture4.out` (third pass): `resolvable_verbs 37` and the 37 names;
   `seasons 4 seed 0`; `acts measured 2432 control 2432`; `control hash equal True`;
   `executed verbs 25`; `attempted verbs 35`; the per-verb counts in §3A.2.1; `executed not
   resolvable []`; `attempted not resolvable []`. **The second pass's on-disk output was a
   traceback**, `KeyError: 'executed'`: it indexed `aperture.measure()`'s top-level dict, which nests
   the realm under `'realm'`. Its figures therefore had no artifact. The script now calls
   `aperture.measure_world(populated.build_realm, 0, 4)` directly, and every figure reproduced.

Every grep quoted in this proposal runs over tracked source files (`git grep -- '*.py'` or a named
file), so a `__pycache__/*.pyc` copy is never counted.

**Not checked.**

- No pytest run (no test reads these files: `git grep -l character-template -- tests engine tools`
  prints nothing [RAN, second pass]). No seeded OUTCOME comparison (probe 4 is inputs only).
- The quarantined threadwork and personal-combat designs: **not opened**. The v30 contest design:
  five lines by grep only.
- The uploads behind `out/UP*.md`: not opened; cited as scratch extracts.
- The mass-battle `brace` body; `world_q.residence_of`; `epistemic.py:541`'s use of
  `establishment_of`; `build_army` as a whole function (its Command checks seen by grep only).
- Golden JSON pins.
- The CONTENT of the research lane rows cited as lane refs (each id exists; what each says beyond the
  rows quoted here was not re-read).
- The 2026-08-15 proposal's measured attribute spreads (not re-run).
- The plan's 17 executed verbs in `corpus_run` (`_part5.md:471`): cited, not re-run.

**Locator corrections.**

- The brief's pointers to `_part5` around `:504` and `:515` do not exist in this tree
  (`wc -l` → 475). The J-13 text is at `:433`, and the ten-attribute evidence at `:444`.
- The research suite's *"[CHECKED p5:515]"* (`00_COMPARATIVE_ANALYSIS.md:78, :214, :528`) and the
  critics' `_part5:504` and `:514` point at the same missing lines.
- `verb_table.yaml:1040-1045` cites `rosters.yaml:482`, `:487-491` and `:505-508` for three
  passages; in this tree they are at `rosters.yaml:1051` (investigation's seam, *"ITS OWN KIND — not
  a contest"*), `:1056-1060` (*"The blanks are Jordan questions"*) and `:1074-1077` (*"INVESTIGATION
  MUST NOT BE MADE A CONTEST TO BECOME GRADEABLE"*) [CHECKED-3]. Not corrected there: outside this
  proposal's paths.

**Locator count, and the brief's aim of at most 70.** The aim is NOT met. The added demand table,
the when-complete stub sources and the master verb table each brought their own sources.

The count, re-taken after the fourth pass's edits [RAN], by
`grep -oE '[A-Za-z0-9_./-]+\.(py|yaml|md|jsonl):[0-9]+' <file> | sort -u | wc -l` (distinct) and
``grep -oE '`:[0-9]+' <file> | wc -l`` (bare continuations, every occurrence):

| file | distinct `path:line` locators | bare continuation locators (`` `:NNN ``) |
|---|---|---|
| the head | 178 | 85 |
| `_part2` | 113 | 128 |
| this part | 172 | 112 |

---

## Critic reconciliation (first critic, against the draft)

The independent critic's report (scratch `critics/CHAR_TEMPLATE.md`, 22 findings; verdict *"does
not meet 100% accuracy"*) was read in full, and each finding's locator was re-opened before any text
changed. **Applied**: the finding reproduced and the text now says what the locator says.
**Narrowed**: it reproduced in part, and the part that did not is stated with its evidence.
**Rebutted**: it did not reproduce. No finding was rebutted outright. **The figures in this table are
the second pass's; the third pass changed several (the next table).**

| # | finding | verdict | where |
|---|---|---|---|
| 1 | Recall and the inquiry verbs' kinds are sourced, not "open" | **applied.** The fieldwork design's §4.2 maps `examine`/`surveil` → Cognition, `interview` → Attunement, `research`/`reconstruct` → Recall, `thread_read` → Spirit with TS (`fieldwork_v30.md:301-306`, `:351`); `examine` gates its Buried depth on TS ≥ 10. J-T2 now rests on the sibling's reading of the census's *"CAPACITY, not attribute"* (`10_verbs_and_attributes.md:152-156`; quotation made verbatim in the third pass), not on "no reader". *(Reversed in the third pass: J-T2 now rests on "no reader above T4", once the inquiry acts' fieldwork attributes were overridden; second table, finding 1, as narrowed by the third table, finding 2.)* AX-7's competence is split off as a per-deposit question (PD1b), which stays open | head §0.6, §3.1 PD1a/PD1b/PD5, §3.2, §3.3; `_part2` §A.2.1 rows 36–41, §A.3; §8 J-T2, J-T9 |
| 2 | Charisma's Face ceiling moves no outcome | **applied.** Charisma's one outcome-moving reader is `derive_command`. Also found: the v30 adjudicator-primary attribute (`modes.py:426-431`) is a label read only by a print (`agon_harness.py:229`) | head §0.6, §3.1 CD1, §3.2, §3.3, §3.6; `_part2` row 35, §A.4; §9 SC row |
| 3 | `form_knot` reads TS, a `bonds // 2 + 1` cap and a `spirit × 2 + history` roll | **applied.** `tie / knot` reads 4 kinds | head §3.1 CD6, §3.3; `_part2` row 42, §A.3, §A.4 |
| 4 | Command is not in the default exchange pool | **applied, and narrowed.** The orchestrator's brief said Command reaches "span, recall, reform only". Re-opened, it also reaches the feint-recognition roll (`orchestration.py:2598`), the morale-erosion divisors (`:2252`, `:2835`; `core/state.py:96`), yield eligibility (`core/state.py:105`), `h_per_size` (`units.py:2815`) and rout at 0 (`:2893`). The span check was located by grep, not opened. *(Third pass: yield and rout withdrawn, span restored; second table, finding 10.)* | head §3.1 CD3, §3.3; `_part2` row 22, §A.4; §7.3 R-WORLD |
| 5 | `speak` reads nothing today; its "when complete" mapping is invented | **narrowed.** Today: applied, `speak` reads nothing. When complete: the CHA half was invented and is gone; a PRA reading has a source: *"`speak` becomes the contest"* (`10_verbs_and_attributes.md:123`) plus the existing `speak: "copying"` mapping (`rosters.yaml:1107`), tagged T4 and conditional | head §0.6, §3.1 CD1, F15; `_part2` row 32 |
| 6 | rally is an empty hook; the Command gate is `reform_check`'s | **applied** | `_part2` §A.1 (rally folded into `march`), §A.4 |
| 7 | the verb table's inclusion rule is uneven; non-verbs counted | **applied.** One rule, five exclusion classes, applied to every candidate. Excluded beyond the critic's list, by the same rule: the spoken lie (an arm of `tell`), resigning (composes on `release`), `form_knot` (the stub of row 42), and the seven contest moves and four mass-battle checks. **65 rows**; capacity-kind split **11 / 2 / 6 / 46** *(third pass: six classes; 10 / 3 / 10 / 42)* | `_part2` §A.1, §A.3; head §0.6; §7.5 |
| 8 | the overlay is both folded and not folded; `copying: 3` copied | **applied.** The overlay stays the owner; the template copies no overlay value; the realm person seats none | head §0.8, §3.5 tests; §4.1, §4.4, §4.6, §5 |
| 9 | Option A does add a `Person` field (J-T1a) | **applied.** `thread_sensitivity` under either option; the hash moves when it lands | head §0.8, §3.5, §3.6; §4.5, §4.6, §6, §7.1, §8 J-T1a |
| 10 | the field-state rule is not a partition | **applied.** Five ordered tests, first match wins: **8 / 1 / 3 / 2 / 7** (F3 moves to not carried) | head §0.3, §2 |
| 11 | F11 has two obligee rows and four readers | **applied, and narrowed.** Two rows (`offices.yaml:191`, `:591`). Of the four readers, `faction_q.superiors` has only a test caller, and the renewal walk reads termed edges, which the two seeded ones are not | head §2 F11 |
| 12 | the hash-reach count included `.pyc` copies | **applied.** 19 source files (17 / 0 / 2), by `git grep -- '*.py'`; the `stats`/`ts` grep's two test hits named | §4.6, §6, §10 |
| 13 | SHIPPED is a row count, not execution | **applied, and widened.** `resolvable_verbs()` drops 8 rows, not 6: `carry` and `construe` too. The realm run executed 25 verbs; the plan's corpus figure of 17 is cited | `_part2` §A.1, §A.2.1; head §0.6 |
| 14 | J-T5 is not answered by precedent | **applied.** Deferred to K-1, with reasons | §8 J-T5 |
| 15 | J-T4 may be answerable | **applied.** Answered at step 3, [medium; Jordan to correct], with a revert *(third pass: withdrawn; J-T4 is escalated, second table, finding 8)* | §8 J-T4 |
| 16 | J-T1's framing omits ED-IN-0185's closure, the plan's narrow gloss, and material for A | **applied** | head §0.4, §0.5, §3.2, §3.4; §8 J-T1 |
| 17 | 04 F.6 is the ASSUMED column of a failure table | **applied.** Cited now for its repair (a practice verb), not its assumption | head §3.5; §4.4; §7.4 |
| 18 | sigma's "pool = value" is assumption-graded | **applied** | §7.4; §8 J-T6 |
| 19 | "axis" and P1–P5 / R1–R6 collide with tree terms | **applied.** "capacity kind"; CD1–CD9, PD1–PD5, LR1–LR6 (no hits for any of these in the tree before this edit, by `git grep -lE`) *(third pass: "capacity kind" also collided and is now "personal input")* | all three files |
| 20 | options framed as complete; A-1 and J-13 (ii) omitted | **applied.** Each option's open cells named; A-1 and J-13 (ii) added | head §0.4, §3.7; §8 J-T1 |
| 21 | the meta-rule cut column overstates | **applied.** A column says which cuts remove anything: one does | §6 |
| 22 | minor items | **applied**: role templates (six in `values:`, five assigned, one unclaimed); A-4 is an option, not history; ED-IN-0193 does not list the nine; ED-WR-0011's provisional qualifier; person-held reads on `migrate`, `comply`, `survey`, `reconstruct`, `give` (and `tell`); `restore`/`work` **open** | head §1, §3.2; `_part2` §A.2.1; §4.2 |
| — | found in the second pass, not by the critic | troop-stock line numbers moved under a sibling's edit and were re-taken; the ATTRIBUTES grep's one "hit" was an English word. *(Third pass: this row also claimed that `practice`'s supersession is at `_part8.md:207` and not `_part7.md:51`, and that the critic had confirmed the wrong line. That was false: `_part7.md:51` reads *"K-4 (… a `practice` verb …) is SUPERSEDED by IN-12 step 9's `train`"*, and the critic was right. The claim is withdrawn here and in `_part2` §A.1.)* | `_part2` §A.1; head §1, §3.2; §10 probe 5 |

---

## Second critic reconciliation (third pass, against the first correction)

The second critic's report (scratch `critics/CHAR_TEMPLATE_2.md`, 20 findings; verdict *"does NOT
meet 100% accuracy"*) was read in full, and every locator it names was re-opened before any text
changed. Verdicts as in the first table. **The figures in this table are the third pass's; the fourth
pass changed several (the next table): the buckets are now 11 / 2 / 9 / 43, not 10 / 3 / 10 / 42, and
finding 1's reading of the 2026-09-05 ruling is narrowed.**

| # | finding | verdict | where |
|---|---|---|---|
| 1 | the inquiry acts' attributes ignore Jordan's 2026-09-05 *"ignore their use of attributes"* (T3) | **applied.** It governs the six acts: the operative sentence names what they roll (*"`capability` supplies the dice"*, `04_VERBS.md:475-476`), its ground (an unsettled roster) applies a fortiori to a column whose Recall is not on the registry, and T3 outranks the fieldwork design's T4 column, which is overridden and recorded. TS gates survive (TS is not an attribute). Not settled: whether attributes may reach the acts once J-T2 settles the roster (a B open cell; the live roster also forbids making them contests, `rosters.yaml:1074-1077`). Effect: `thread_read` 3 → 2 inputs; four inquiry verbs read PRA, not ATT/REC/ACU; **Recall has no reader above T4**, so J-T2 lists it only if Jordan gives it a reader | head §0.6, §3.1 PD1a, §3.1.1, §3.2, §3.3, §3.6; `_part2` rows 36–41, §A.3, §A.4; §8 J-T2, J-T9 |
| 2 | V-2 and V-3 never cited | **applied, and narrowed.** Cited and obeyed: B reads an attribute only through `faculty(domain)` on a row declaring `contests:`; `fight`, `accept`, `march` qualify; `tie / knot` and the thread operations need `contests:` rows; the knot's bare-BON gate needs a proposed V-2a (Jordan's, inside J-T1 B). Narrowed: under the ruling the inquiry acts read no attribute, so V-2 does not bite there; and V-3 is LEAVE in the plan (`_part7.md:51`), so it binds B's design, not today's code | head §3.3, §3.6, §3.7; `_part2` §A.4.2; §8 J-T1; §9 V-2/V-3 row |
| 3 | the fieldwork design read selectively: CHA readers, `conceal`, TS depth gating, the +2D Recall bonus, the social acts | **narrowed.** Applied: fieldwork read in full; CHA's T4 readers (Converse, Impress, Rumour, cover setup, Composure) recorded; BON rolled for Connect recorded; `conceal` now records the fieldwork cover roll and Cover (CHA, ACU, PRA) and says why they are not counted (T3 row: `contests: none`; V-2); a sixth exclusion class, *scene-scale only*, lists every fieldwork social, exploration and concealment act with its reads. TS gating: the general rows gate every investigation at Buried (`:44-45`, `:447`), the per-action column narrows it; this proposal takes the per-action column and shows the count the other reading gives (10 / 5 / 8 / 42). **Rebutted in part:** the *"+2D Recall bonus"* is not a read of Recall; the contest design calls it a *"non-attribute"* citation bonus (`social_contest_v30.md:97`, `:177`) | `_part2` §A.1, rows 37–39, 52, §A.3 thinness, §A.4 `examine`; head §3.1.1, §3.2 |
| 4 | A-1 both keeps and overwrites the ruled count | **applied.** A-1 is eight; it overwrites the ten, as A does. One sentence everywhere | head §3.4, §3.7; §8 J-T1 |
| 5 | the "found in this pass" claim about `_part7.md:51` is false | **applied.** `_part7.md:51` supports the supersession; the first critic was right. Both lines are now cited, and the false row is corrected in place | `_part2` §A.1; the first table's last row |
| 6 | troop-stock locators stale; J-T8's "candidate C" wrong | **applied.** Every troop-stock reference is now a section heading or J-number. Re-read by heading, the design changed: its default troop body is **A, a troop stock** (J-1, open), not a company `Person`; a grade is a matter kind on the rung (§2.7), not a key in a company's `capability`; kit is the town's. J-T8 says the troop body is Jordan's open J-1 there | head §1, §3.1 CD3/CD4, §3.2, §3.7; `_part2` §A.1, row 65; §8 J-T5, J-T8; §9 |
| 7 | J-T7 is not answered by precedent | **applied.** The one-class half is answered at step 5 (`carriers.py:644`). The creation-row half is IN-47's held review, whose fallback is the opposite; not re-escalated because it is already Jordan's. Found with it: the template narrows C1's blocker and does not remove it (pursuits stay on the registry row) | head §1; §7.3 R-PLAYER; §8 J-T7; §9 IN-47, GO rows |
| 8 | J-T4 is not answered at step 3 | **applied.** Re-run step by step: steps 1–4 answer nothing; step 5 leans to none; the options make different games, so **escalated**, interim none. The spliced quote is split into its two files | §8 J-T4; head §3.6 |
| 9 | "capacity kind" collides (census tier; `world_q.capacity`) | **applied.** Replaced by **personal input**, which `git grep -il` finds nowhere in the tracked tree; "kind" dropped with it. "Capacity" survives only in quotations of the census and as `world_q.capacity`'s sense on row 23. The census quote is now verbatim (*"CAPACITY, not attribute — equip slots + learning rate; never rolled"*, `2026-08-15-…-progression.md:475`, quoted at `10_verbs_and_attributes.md:154-155`) | all three files |
| 10 | narrowing #4 over-reaches | **applied.** A derived Command (clamped ≥ 1, `exchange.py:54`, `:65`) cannot reach yield eligibility or rout at 0; Command 0 is the capture state (`orchestration.py:2221-2226`). Span of control restored (`engine.py:93`, `:327-345`) | head §3.1 CD3, §3.3; `_part2` row 22, §A.4; §7.3 |
| 11 | BODY counted and not counted | **applied.** One rule, stated once in each part: BODY, OFF and person-held quantities are never personal inputs; §0.6 now says ONE verb reads a personal input in the loop (`tell`) | head "Words", §0.6, F14, §3.1; `_part2` "Words", §A.2.1 |
| 12 | `tell`'s Ob is the hearer's | **applied** (`verb_table.yaml:950-951`; `loop/resolve.py:740-744`) | head F15, CD1, §3.4; `_part2` row 35; §7.4 lateral |
| 13 | probe 6 has no artifact | **applied.** Re-run with the KeyError fixed (`aperture.measure()` nests the realm under `'realm'`; the script calls `measure_world`). Every figure reproduced: 37 resolvable, 2432 acts each arm, hashes equal, 25 executed, 35 attempted. Probes 3–5 also re-run to an artifact | §10 probes 3–6; `_part2` §A.1 |
| 14 | K-3 mis-tiered T4 | **applied.** T3 (ratified as intent, `_part8.md:207`) | `_part2` row 40; head F17, CD5 |
| 15 | LR5 cannot refuse the troop grade key | **applied, and the premise moved.** LR5 refuses only off-roster keys, as the critic says; the claim is withdrawn. Re-read by heading, the troop design no longer puts a grade key in any `capability`, so no key-space interaction remains under it; §4.2 states what would keep LR5 meaningful if one returned | §4.2 LR5; §9 troop row |
| 16 | `speak`/`determine` uneven; `resilience` half-included | **applied.** `determine` treated as `speak` (PRA, T4, conditional). RES gets a code, a matrix column and a place in §0.6 and J-T2. The same rule applied to every planned verb routed to the sigma roll adds `arrest`, `argue`, `interrogate` (PRA, T3): beyond the critic's count, which is why the buckets are 10 / 3 / 10 / 42, not 11 / 2 / 7 / 45 | `_part2` rows 8, 50, 54, 56, §A.3; head §0.6, §3.2 |
| 17 | eleven untouched fields, not twelve | **applied** | §6 |
| 18 | source class (a) admits a prose magnitude | **applied.** (a) licenses a KEY only; a value needs (b)–(d) | §5 |
| 19 | RS-27/RS-29 answer J-T3's inheritance half | **applied.** J-T3 narrowed to blood kinship as a relation (K-NPC-6) and still escalated | §8 J-T3; §9 IN-61 row; head F20 |
| 20 | lane-ref column mixes #453 "retires" ids with research refs; four demand rows carry none | **applied.** Planned rows carry a separate *retires* column; every demand and verb row carries a research lane ref or **none**; PD2's search is stated | head §3.1; `_part2` §A.2.1, §A.2.2 |
| — | found in this pass, not by the critic | the template does not remove IN-47's C1 blocker (pursuits stay on the registry row); `verb_table.yaml:1040-1041` cites stale `rosters.yaml` lines; `arrest`, `argue`, `interrogate` route to the sigma roll (their §9 `contests:` rows), so `argue` and `interrogate` are no longer **open**; the span-of-control reach was never in the first critic's object list but is restored with finding 10 | head §1, §3.1.1; `_part2` §A.2.2; §8 J-T7; §10 |

---

## Third critic reconciliation (fourth pass, against the second correction)

The third critic verified about 350 locators and re-derived the probe figures and the matrix row by
row, then reported 13 residual findings. Each locator it names was re-opened in this pass, with the
lines beside it, before any text changed (the list is §10, "Opened in the fourth pass"). Verdicts as
in the first table. **The figures in this table are the fourth pass's.**

| # | finding | verdict | where |
|---|---|---|---|
| 1 | `speak` and `determine` are mis-sourced against the ratified verb-coverage suite; under the higher-tier rule `speak` reads nothing (10 / 3 / 9 / 43) and `determine` is T3, sigma-routed; the T3-vs-T3 conflict over `speak` (`04_VERBS.md:67` vs `:1334`) is unrecorded | **applied for `determine`; narrowed for `speak`.** `determine`: `contests: "a proposition"` (`2026-10-03-verb-coverage-and-gap-fill.md:1309`), sigma-routed (`:2070`), one of seven contested rows (`:1362-1363`): PRA at T3, moved to the sigma-routed matrix row. `speak`: the critic's T3 row reproduces (`:1334`, `:405`), but the contested side has T3 support too: v9's SC-01 step 12 schedules *"`speak` — a typed cell, `contests: "a matter"`, four bands"* (`workplans/valoria_master_workplan_v9_part6.md:65`), beside `04_VERBS.md:67`. Higher-tier-wins does not decide an equal-tier conflict, so this pass adds the rule that it is **open** and counts 0, and records both sides. The count change is the critic's (1 → 0); the ground is the new rule, not a T3 win | head "Evidence tiers", §3.1.1, §3.2 glance table; `_part2` "Discipline", rows 8, 32, §A.3 |
| 2 | the reading of *"ignore their use of attributes"* goes beyond Jordan's text; `thread_read`'s T3 mark is an inference; `04_VERBS.md`'s tier is contestable; *"Thread Pool"* is in the struck vocabulary | **applied, and widened.** Jordan is credited with his five words only, which strike the source table's pool column (`04_VERBS.md:462-467`); *"`capability` supplies the dice"* is the design author's sentence, scoped to the five rows (`:473-476`, `:487`, `:528-581`), on rows whose contest shape the roster rejects (`rosters.yaml:1051`, `:1056-1060`, `:1074-1077`; verb-coverage `:378`). The tier is flagged contestable (`04_VERBS.md:3` vs `_part8.md:202`) and read as T3, with the T4 reading's consequence named. The TS claim is softened: the ruling struck a TS-derived POOL term in its own table; nothing says it reaches a GATE. **Widened past the critic's recount:** once `thread_read`'s PRA-only reading is an inference, it overrides nothing, so the fieldwork Leap pool (WIL, PRA, TS; T4) stands and `thread_read` moves 2 → 3. Buckets **11 / 2 / 9 / 43**; the critic's 10 / 3 / 9 / 43 is shown as the count if Jordan accepts the inference | head §0.6, PD1a, §3.1.1, §3.2, §3.3, §3.4, §3.6; `_part2` rows 36–41, §A.3, §A.4, §A.4.1, §A.4.2; §7.4 horizontal; §8 J-T2, J-T9; §9 FI row |
| 3 | the V-2 "today" list omits `tell` | **applied.** `tell` (`contests: "a standing"`, `verb_table.yaml:953`) added; the plan's V-2 entry names three rows as read 2026-10-06 (`_part7.md:51`), and the table now has four, `accept` added; `tell`'s domain binds no attribute | head §3.3 (V-2 bullet, code block); `_part2` §A.4.2 |
| 4 | Mending never reads `resilience` | **applied.** Cost 0 at every degree (`operations.py:451`, `:316-323`, `:567-569`), and `resist_coherence_cost` returns a cost ≥ 0 before reading it (`:260`, `:269`). Also found: Leap's base cost is 0 (`:364`, `:372`), so it reaches RES only on a Partial or Failure. Mending 4 → 3 inputs; no bucket change | head CD5, §3.2, §3.3; `_part2` RES code, rows 58, 64, §A.3, §A.4, §A.4.1 |
| 5 | three stale troop-stock heading quotes; the troop verb is now `levy` | **applied.** §2.4 *"…the candidates and their full footprint (J-1)"*, §2.7 *"Troop kind and grade"*, §3.1 *"`levy`: raise troops from a settlement's pool"*; every `conscript` mention replaced; J-3 recorded as answered (`levy`), and the store act as `requisition` (row 21). Citations now lead with J-numbers and section numbers | head line 5, §1, CD4, §3.2 KIT; `_part2` §A.1 (DESIGN-ONLY), row 65; §9 troop row |
| 6 | the +2D Recall rebuttal omits `social_contest_v30.md:155` | **applied; the conclusion stands.** `:155` says *"Recall contributes to the Appraise pool and the citation bonus"*, against `:97` (*"non-attribute"*) and `:177` (*"Binary"*): the T4 design is inconsistent on whether the bonus reads Recall. Either way it is T4 and superseded, so "no reader above T4" holds | head §3.1.1; §8 J-T2 |
| 7 | J-T1 (A) lists body and office as personal inputs; KIT omitted from §0.6 and from "three further inputs" | **applied.** (A) now names practice and kit (and TS) as its personal inputs, and body and office as differences that are not; KIT moved into §3.2's group 3, so "four further inputs" (TS, TMP, RES, KIT), and §0.6's list gains kit; KIT is not a tenth-attribute candidate | head §0.6, §3.2, §3.7; §8 J-T1 |
| 8 | `knots.py` spirit default at `:214`; `fieldwork_v30.md:617` has no History; PD2 re-punctuates a table row | **applied.** `:214`; `:361` (the pool, with History) and `:617` (*"Cognition × 2, Ob 2"*) separated; PD2 quotes the Governor row cell by cell | head §3.3 knot row, PD2; `_part2` §A.1 |
| 9 | lane refs: K-WR-2 on the Pull rows; row 32's non-id; CD2's plan position | **applied, K-WR-2 narrowed.** K-WR-2 does not exclude Pull; it defers it (*"Pull only once P-09's detectable orphan has a carrier"*, `WR_world.md:538`), so rows 60–61 carry it as deferred. Row 32 now cites M-SC-3, which names SC-01 step 12's `speak` (`SC_social_contest.md:372`). CD2's `PC-06 K-1` removed from the lane-ref column | head CD2; `_part2` §A.1, rows 32, 60, 61 |
| 10 | the first table's row 1 still says J-T2 rests on the census, "not on no reader" | **applied.** Annotated as reversed in the third pass | first table, row 1 |
| 11 | "personal input" sits beside `PersonalCombatInput` | **applied.** A one-line note: that class carries the BODY-derived `ends` (`inputs.py:45`, `:51`), not a personal input in this sense. Not renamed: `git grep -il "personal input"` found no other use (head, "Words") | head "Words"; `_part2` codes |
| 12 | the fieldwork concealment pool sets every investigation action's Ob | **applied.** Recorded as an **open** DIFFICULTY read on rows 36–41 (`fieldwork_v30.md:361-363`; `verb_table.yaml:1085`), neither overridden (the design author keeps the obstacle side, `04_VERBS.md:462-463`) nor admitted (the roster: not a contest). Adds 0; no bucket change | head PD1a; `_part2` §A.1, rows 36–41, §A.3, §A.4 |
| 13 | J-T3's remainder may be answerable at step 5 through ID-13 | **applied.** Re-run: ID-13 (`01_AXIOMS.md:561`) bars a field with no reader, F9 is the precedent, and the research row places kin-as-tie with `tie / knot` (`NPC_npc_cast.md:516`). Answered for the template, (i) not carried, [medium; Jordan to correct], with a revert; no longer escalated | §8 J-T3; §5 kin row |
| — | found in this pass, not by the critic | v9's SC-01 step 12 (the T3 source finding 1 missed); the `thread_read` consequence of finding 2 and its count; the equal-tier and inference rules, added to the head's tier paragraph so both are stated once; the plan's V-2 entry predates `accept`'s `contests:`; Leap reaches RES only on a Partial or Failure; the troop design's header records the `levy` → `requisition` rename of the store act; `04_VERBS.md` line references corrected (the ruling at `:465-466`, the struck column `:462-467`, the author's sentence `:473-476`); every third-pass **[CHECKED]** tag renamed **[CHECKED-3]** so that **[CHECKED]** means this pass | all three files |
