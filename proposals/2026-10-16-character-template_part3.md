# The character template — part 3: §4–§10 (the loader, sourcing, adds and cuts, NERS, decisions, interactions, limits)

## Status: PROPOSED (2026-10-16). Corrected the same day against an independent critic's report (reconciliation table at the end of this part). Not ratified; merge ratifies nothing unless Jordan so rules.
## Tags as in the head: [CHECKED] opened in the correction pass; [CHECKED-draft] opened in the drafting pass only; [RAN] run in the correction pass.
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
| a corpus world's per-seat `capability:` | the case's own `cast:` overlay (e.g. `engine/season/cases/exercises/NPC-088.yaml:29-33`) [CHECKED] | `corpus_run.build_at`, as today. **The template never copies an overlay value** (§4.4) |

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
# engine/season/characters.yaml -- the authored capacity half of the character template.
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
| LR4 | an attribute key not in `ATTRIBUTES`, a value for the pending tenth, or a value not a whole number in `[ATTRIBUTE_FLOOR, ATTRIBUTE_CEILING]` | the leaf (`descriptors.py:50-53`) [CHECKED] |
| LR5 | a practice key not on `practice_roster`, or a value not a whole number ≥ 0 | `corpus_run._check_capability` (`corpus_run.py:335-364`) [CHECKED-draft], which becomes the ONE practice validator both paths call |
| LR6 | a string where a number is due (`'3–4'`, `'~50'`) | §42.2's polarity, quoted in `cast.py:19-24` [CHECKED-draft] |

**Defaults: null, never a guess.**

- An absent or null field means NOT AUTHORED. The template never writes a default value onto a
  person. The READER falls to its own declared default: `pool_default` (H-126), a module's class
  default, or `age_at_build`.
- This is the polarity `cast.py` states (*"It READS and VALIDATES; it does not translate and it
  does not guess"*, `cast.py:19-24`) [CHECKED-draft], and the one `npcs.yaml` states for its rows
  (`npcs.yaml:12-16`) [CHECKED-draft].
- **ED-WR-0011 is cited for the cast, not for the default.** It rules the cast CLOSED and AUTHORED
  (`editorial_ledger_wr_archive.jsonl:14`) [CHECKED], so there are template rows only for cast
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
  implies (head §3.5, write rule; `04_CODE_ARCHITECTURE.md:1153`) [CHECKED]. F.6's *"world-gen
  writes it once; nothing else does"* is the ASSUMED column of a failure table, not a rule, and is
  not cited as one.
- **Corpus `build_at`.** The `cast:` overlay keeps its shape (`CAST_KEYS`) and **stays the one owner
  of its `capability:` values**. The template copies none of them: NPC-088's `copying: 3`
  (`cases/exercises/NPC-088.yaml:32-33`) [CHECKED] stays where it is, and the realm's `p_npc_088`
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
- **The reach, counted** [RAN], over tracked source files only, so no `__pycache__/*.pyc` copy is
  counted:
  `for d in engine/season/tests engine/tests tests/valoria; do git grep -l content_hash -- "$d/*.py" | wc -l; done`
  → `17`, `0`, `2`: **19 source files** mention it. (The first draft's `grep -rlE … | wc -l` gave
  `55` because it counted compiled copies; re-run, it still prints `55`.)
  `git grep -lE '[0-9a-f]{32}' -- 'engine/season/tests/*.py' 'engine/tests/*.py' 'tests/valoria/*.py' | xargs git grep -l content_hash --`
  → one source file pins a 32-hex digest beside it (`engine/season/tests/test_season_weather.py`).
  Golden JSON pins elsewhere were **not** enumerated [UNVERIFIED].

---

## 5. SOURCING DISCIPLINE

**What a template author may fill, and from what.** A value enters `characters.yaml` only with a
`source:` of one of four kinds:

- **(a) a case's TEXT, never its overlay value:** `path:line` in `engine/season/cases/` where the
  case's prose names a vocation or a magnitude. A value a case already seats through its `cast:`
  overlay stays there and is not repeated (§4.4): NPC-088's `3` is such a value, and an
  `assumption` by its own text (`NPC-088.yaml:23-28`) [CHECKED].
- **(b) a ruling:** an `ED-…` id or a v9 `RS-…` row whose text gives the number.
- **(c) a value Jordan supplies:** a dated quote.
- **(d) a registry cell:** `path:line` in `references/npc_registry.yaml`, and only where the cell is
  a number on the target scale under a registry name.

Everything else stays null. No author converts prose ("75–80", "~50", "3–4") into a number. That
conversion is a ruling, not authoring.

**How the 46 cast rows would read under the template.** The command, re-run in the correction pass
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
| `practice` | (a)–(d) | **0** | 46 | the one case naming a vocation `verb_capability` covers is NPC-088 (`_part5.md:73`) [CHECKED], and its value stays in its overlay (§4.4); no ruling, Jordan value or registry cell gives another |
| `attributes` (B) | (d) `stats` | **1** row, **3** values (NPC-001: `cognition 5` → ACU via an `[ASSUMPTION]` alias; `focus 5`; `endurance 4`) (`npc_registry.yaml:57-61`) [CHECKED-draft] | 45 | `social: '3–4'` refused: prose, and not a registry name |
| TS, if carried (J-T1a, §8) | (d) `ts` | **8** integers (NPC-003 25, NPC-004 15, NPC-005 35, NPC-020 28, NPC-030 0, NPC-070 0, NPC-075 60, NPC-080 0) | 38 | NPC-001 `'75–80'` and NPC-002 `'~50'` refused as prose |
| Coherence (WR's carrier) | (d) `coherence` | 1 (NPC-001: 9) | 45 | outside this template; listed so it is not lost |
| kit | none in the tree | 0 | 46 | waits on J-T5 |
| kin | none | 0 | 46 | waits on J-T3 |

**So the template ships nearly empty, and that is the honest state.** Under either option it changes
no outcome until someone supplies values under (a)–(d); it can seat at most NPC-001's three
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
| `npc_registry.yaml`'s `stats:` and `ts:` as an ENGINE source | subsumed: the typed home is `characters.yaml`; the registry cells stay as canon reference, not deleted | **no**: no engine code reads them today, so nothing is removed; the cut is of a future misuse | no game Python reads them [RAN]: `git grep -nE '\bstats\b\|\bts\b' -- 'engine/season/*.py'` matches the docstring at `cast.py:6` and two local variables named `ts` in tests (`test_h134_candidate_per_seat.py:117-120`, `test_season_shape.py:14963`); and they hold prose ranges |
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

**Not touched.** The faction role template and the cohort template (§1), `Person`'s other twelve
fields, and the scene budget.

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
| `characters.yaml` + `template_of` | cut it and **the game cannot seat an authored capacity, age or kit on a named person**; every person rolls at `pool_default` | bottom-up (person → roll); top-down (creation screen → person) | assume it gone: does anything else seat practice on a realm person? `build_realm` seats none (`populated.py:864-896`), and the overlay is corpus-only | **N HOLDS** |
| the practice block | cut it and `train` raises a key world-gen never seeded: every person starts untrained, and the same act's odds never differ at tick 0 | vertical (template → `train`) | does `capability` already carry it? Yes, the CARRIER does; the template is its only authored SOURCE in the realm | **N HOLDS, NARROWED**: it is a source, not a carrier |
| `Person.attributes` (B) | cut it and the stubs' nine attribute channels never vary by person | bottom-up (person → `Combatant`, `Officer`) | do practice or body supply the same differences? No: `Combatant`'s seven attribute fields and `Officer`'s two have no practice or body input (§3.3) | **N HOLDS at T2, and does not hold at T1**: no season reader exists until K-1 or K-6 lands. Under the plan's rule for K-2 (*"builds only with its first reader"*, `_part7.md:44`) [CHECKED] it ships with its first reader or not at all |
| `Person.thread_sensitivity` (J-T1a) | cut it and TS has no carrier: `thread_read` stays unattemptable, and the knot's party gate and the thread pool read their `getattr` defaults (0 and 30) | bottom-up (person → `thread_read`, knot, thread pool) | does `capability` carry it? It could, under a `ts` key; K-3 chose a field, ratified as intent | **N HOLDS at T2/T4, not at T1**: lands with its first reader (H-85's typed gate) |
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
  Under A a player reads "practised in X" and predicts X. Both are legible. B adds multi-kind
  combinations the player cannot see (§3A.4: reading is `(2·cog + att)/3 + …`). **E-LEGIBILITY
  FINDING under B**: the sheet shows attributes, and the outcome turns on blends. The repair is
  K-GO-6's derivation view, an existing recommendation, not a new object.

### 7.3 R — both halves

- **R-COMPLETE.** FINDINGS: five **open** verb cells (§3A: `forge`'s quality, `restore` and
  `work`'s `× f(degree)`, `argue`, `interrogate`) and PD1b's competence kind. Under A, the knot's
  gate and roll (BON, WIL) have no input (§3.3). Under B, `research` and `reconstruct` read REC,
  which is not among the nine unless J-T2 names it.
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
  (CD3): not through the exchange pool, which at the defaults reads troop quality and numbers only,
  but through the reform gate, the recall and feint rolls and the morale-erosion divisors (§3A.4).
  A fight between two NPCs varies by who they are. **The half with no player is where the template
  pays most.** How a field holds, rallies and pursues depends on who commands it, with no player
  present; how hard each side hits does not.

### 7.4 S — six directions, plus pause and methodology

| direction | test | verdict |
|---|---|---|
| bottom-up | template → `Person` → each input builder (§3.1) | PASS by shape; under B, K-1 and K-6 are the carriers each step needs |
| top-down | a field's command → the commander's template | PASS under both (B: CHA, ACU; A: PRA[command]) |
| vertical | world-gen → `train` → the same key | PASS: one carrier, two writers in sequence; the shape 04 F.6's repair (*"a `practice` verb"*, superseded by `train`) implies |
| lateral | a person vs a person in one contest | PASS: the opposed pair already reads the same key on both sides (`sigma.py:112-129`) |
| horizontal | contest vs combat vs threadwork | **FINDING (methodology)**: one quantity, PRA, becomes dice by three conventions. Sigma: pool = the value (`sigma.py:109`). Combat: pool = `max(5, history + 6)` (`core.py:54-56`). Threadwork: `min(3, history + 3)` inside a sum (`operations.py:246`) [CHECKED-draft]. Under S's *"calculations consistent in methodology"* this is three ladders for one quantity. Not repaired here. The three are NOT equally ruled: combat's is ratified (*"ED-901; re-ratified ED-900/904"*, `core.py:55`) [CHECKED]; threadwork's cites PP-624 (`operations.py:245`) [CHECKED]; sigma's "pool = the value" is an `assumption`-graded mapping (H-126; *"an `assumption` grade means inject the default"*, `sigma.py:105-107`; NPC-088's magnitude, `NPC-088.yaml:23-28`) [CHECKED]. Raised as J-T6 |
| diagonal | an office holder's practice vs his office's remit | PASS: kept apart by §3.3 (office grants options and scenes, never capacity) |
| pause | — | N-A: the template acts at world-gen only |

### 7.5 The design's own falsifier, and the self-audit

- **§4.5 test 4** (no accepted key without a reader) is the template's own falsifier. Run by hand
  against §2:
  - F9 hits, and is not carried;
  - F13 passes at T1 (dark);
  - F16 hits at T1 under B, and is held behind K-1 and K-6;
  - **0 unhandled hits.**
- **9a (backward propagation).** §0 item 3's count (8/1/3/2/7) was re-derived against §2's
  partition after the table was corrected: equal, and every F-row appears in exactly one class.
  §0 item 6's verb counts were re-derived against §3A.1: 37 + 8 + 12 + 7 + 1 = 65, and the
  capacity-kind split against §3A.3: 11 + 2 + 6 + 46 = 65.
- **9b (my additions).** `practice_roster` absorbs an existing roster (disqualifier 1 checked: it
  is not a second home, because `verb_capability`'s values move into it). `seat_template` is one
  call beside an existing seating block. `Person.attributes` is K-2's, which the plan already gates
  behind its first reader; `Person.thread_sensitivity` is K-3's; this proposal ships neither
  without a reader.
- **What an independent reviewer would add.** An independent critic did re-open the per-verb
  lines (22 findings, reconciled at the end of this part). Still owed: a seeded OUTCOME comparison
  (not just inputs) for one practice key, and the quarantined combat, threadwork and contest
  designs this pass did not open (§10).

---

## 8. DECISIONS FOR JORDAN

**Each was put through `CLAUDE.md` §0's five answers first.** Escalated only where none answered it.

| id | decision | options | effect on the game | what waits | §0 test result |
|---|---|---|---|---|---|
| **J-T1** | the capacity source | **A** derived (practice, body, kit, office) · **B** stored ten attributes + practice · **A-1** six faculties + Recall and Bonds as gates (2026-08-15 `:191`) · **J-13 (ii)** a ruled rank scale for practice values, orthogonal to the others (`_part5.md:433`) [CHECKED] | A: persons differ only by practice; the ruled ten is overwritten. B: persons differ innately; J-13 read narrowly. A-1: innate difference on six faculties; Focus and Charisma cut, so the ruled ten is overwritten and `derive_command` loses its primary input | R-09 by-person; K-1, K-6; the troop design's commander; K-GO-8 | **escalated**: defensible options that lead to materially different games, and A and A-1 overwrite a ruling. Escalating does not re-raise ED-IN-0185's closed agenda unless Jordan chooses an option that overwrites it (head §3.4) |
| **J-T2** | the tenth attribute's name (B only) | candidates with a T2 reader: TMP (`disp`), TS, `resilience`. Recall has T4 readers (`research`, `reconstruct`, `fieldwork_v30.md:303`, `:306`) [CHECKED] and is left off on the sibling proposal's judgement that it is *"a capacity, not attribute"* (`10_verbs_and_attributes.md:152-156`) [CHECKED], which Jordan may overrule | decides which subsystem gains a by-person input | B's roster closes; Godot fields bind (`CLAUDE.md` §5) | **escalated**: already Jordan's (ED-IN-0193; `_part5.md:444`) |
| **J-T3** | does kin or lineage enter the template | (i) no; (ii) a kin Tenure kind with a reader (inheritance through `succeed`, feud through stance) | (ii) gives the world dynasties and blood feuds without a player | F20; succession reads | **escalated**: no carrier, no ruling, no precedent; a live design choice |
| J-T4 | do attributes change after tick 0 (B only) | none · age · wounds | none: training is the only growth. Age or wounds: the bodies pass reaches capacity | B's write rule | **answered at step 3, by design documents [medium; Jordan to correct]: none.** The contest code records Charisma as a *"BUILD-TIME attribute … set by the player at creation, not by moment-to-moment play"* (`resolver.py:191-192`; `primitives.py:139-141`) [CHECKED]; K-2 is *"seeded with nothing"* at world-gen (`09_the_character_sheet.md:129`) [CHECKED]; and 04 F.6's repair for a character who never improves is *"a `practice` verb"*, not an attribute writer (`04_CODE_ARCHITECTURE.md:1153`) [CHECKED]. Age and wounds already act through `born` and `body`. Revert: Jordan rules that age or wounds move an attribute |
| J-T1a | TS's carrier | a `thread_sensitivity` field on `Person` (K-3) | — | the thread rows; `examine`'s depth gate; the knot's party gate | **answered by ratification**: K-3 is *"RATIFIED AS INTENT (v9)"* (`_part8.md:207`) [CHECKED]. Take K-3's field, not a `capability` key. **It adds a `Person` field under either option**, landing with its first reader; the hash consequence is §4.6's |
| J-T5 | kit's carrier | `hold` Tenures on equipment objects (K-5) · the person-rung's `Rung.stores` (the troop design's choice for companies) | — | F18 | **deferred, not answered.** There is no precedent the tree decided: the troop design is PROPOSED (`troop-stock-design.md:3`) [CHECKED], U-2 is about merging equipment catalogues, not where a person's kit lives (`08_mass_battle_units.md:126`) [CHECKED], and K-5 is unscheduled behind K-2 (`_part7.md:44`) [CHECKED]. Nothing reads kit off a person until K-1 lands, so nothing waits on this sooner; it is asked with K-1, and escalated then if §0's five answers still leave two options |
| J-T6 | one ladder from practice to dice | keep three subsystem formulas · one shared conversion | §7.4's methodology finding | — | **not escalated separately.** Combat's and threadwork's are their subsystems' formulas (ED-901; PP-624). Sigma's is an `assumption`-graded mapping (H-126), whose scale is already open as J-13's remainder (`_part5.md:443`) [CHECKED-draft]; the shared-ladder question rides with that ruling. Recorded as a known S defect |
| J-T7 | the player-character template vs the NPC one | the same template; the creation screen writes a row | — | K-GO-8 | **answered by precedent**: IN-47's review takes the fallback that the player picks a seated person (`_part4.md:41`) [CHECKED-draft]. One template, one class (S9.1, `carriers.py:644`) [CHECKED-draft] |
| J-T8 | commanders and troops | commanders: the character template; companies: the cohort template | — | the troop design | **answered by architecture**: one `Person` class; a company is a cohort (`troop-stock-design.md:326`, its chosen candidate C) [CHECKED] |
| J-T9 | which capacity kind AX-7's competence at deposit reads (PD1b) | ACU · ATT · PRA[`inquiry`] only | how every witness, not only an investigator, credits what he hears | K-FI-1, H-200 | **folded into J-T1/J-T2**: under A it is PRA, and under B it needs one of the nine. Asked with J-T1, not separately. (The five inquiry verbs are NOT part of this question: the fieldwork design maps them, PD1a) |

---

## 9. INTERACTIONS

| id | what it is | how the template meets it |
|---|---|---|
| **IN-12 step 9** (`_part5.md:73`) | `train` writes `Person.capability` | the template seeds the SAME keys at world-gen; `practice_roster` is the shared key set. Under J-13 (iii) `train` writes only where a case names a vocation; the template does not widen that, it gives it a place to start from |
| **IN-47** (`_part4.md:39-44`) | the character-sheet spaces | creation is a template row, and C1's blocker (*"no `pursuits` key; `CAST_KEYS` is closed"*) is met by the template carrying the authored fields |
| **IN-46** (`_part4.md:32-37`) | the grid suspension | its DEPS name *"IN-47's carriers where a party is built from a person"*; under B that is K-1 reading the template's attributes |
| **IN-64** | every NPC carries 15 pursuits and the three concerns | composed on, not repeated: `pursuits_of` and `conviction_of` already refuse incomplete rows |
| **IN-34** / H-208 | ageing, dark | `born` becomes authorable; the rates stay Jordan's |
| **K-2** (`_part7.md:44`) | `Person.attributes`, *"not ratified"*, only with its first reader | Option B is K-2 with its readers named; it does not ship ahead of K-1 or K-6 |
| **MB commanders** (K-6, U-4; M-MB-3) | `Officer` from the commander | CD3; the troop design's §4 defers the commander's capacity to *"R-C-1/J-13"* (`troop-stock-design_part2.md:75-76`) [CHECKED-draft], which is J-T1. At the defaults Command reaches gates, rolls and divisors, not the exchange pool (§3A.4) |
| **the troop-stock design** (`proposals/2026-10-16-troop-stock-design.md`, PROPOSED, read in part; under a sibling's edit while this was corrected) | a company's grade in its own `capability` (`:378`) [CHECKED] | **a key-space interaction**: character practice keys and a company's grade key share one carrier. `practice_roster` must either list the grade key or keep a disjoint namespace. The template loader refuses the grade key on a character row (LR5) |
| **SC-01 / SC-02**, K-SC-2 | proceedings own the obstacle; the contest faculty | CD1: the contest reads PRA only; Charisma's Face view moves no outcome, so there is nothing for the proceedings subsystem to "land" from CHA unless a ruling gives Face a reader |
| **FI**, H-200, K-FI-1 | the inquiry verbs; competence at deposit | PD1a (sourced), PD1b and J-T9 (open) |
| **WR**, K-3, K-WR-2 | TS, Coherence; thread operations as acts | CD5, CD6, J-T1a |
| **GO**, K-GO-8 | the creation screen writes a cast entry | the template is that entry |
| **R-06, R-07, R-09** (`requirements.yaml:954`, `:1152`, `:1281`) | built characters; feelings and relationships; a probabilistic chain | R-06 gains the capacity and age halves of "robustly built"; R-07 is unchanged (stance and regard are not template work); R-09's by-person conjunct moves only with J-T1 plus authored values (§5) |
| hole rows | H-185 (F6's predicate), H-200 (PD1b), H-208 (F13), H-170 (the cohort template's weight), H-49 (`weight`'s runtime writer, closed by the troop design's raising verb), H-182 (CD6: `tie / knot` has no effect), H-85 (`thread_read`'s TS gate, J-T1a's first reader), H-164 (`restore`/`work`'s `× f(degree)`) | each is named at its field; the template closes none of them alone |

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
  (K-rows), `2026-10-16-troop-stock-design.md` (§0, §2.2–§2.3) and `_part2` (§4 items 4–5).
- **Research and scratch:** `research/by_lane/` (rows grepped, not whole files), scratch
  `briefs/JORDAN_STATEMENTS.md`, and `critics/*.md` and `out/UP*.md` (grepped).

**Opened in the correction pass** (tagged [CHECKED]): every locator the critic's 22 findings name;
`verb_table.yaml` (the 45 row lines, `speak`, `tell`'s `contests:`, the typed cells of `comply`,
`give`, `survey`, `reconstruct`, `thread_read`, `tie / knot`, the decline notes); `sigma.py:75-150`;
the contest `resolver.py:180-236`, `primitives.py:116-149`, `modes.py:414-450`, `wrapper.py:60-200`
and `agon_harness.py` (by grep); `knots.py:45-60`, `:170-225`; `operations.py:150-160`, `:230-275`;
`exchange.py:50-130`; `config.py:246-247`, `:530-533`, `:550-560`; `orchestration.py:282-330`,
`:2580-2600`; `units.py:2695-2722`, `:2795-2818`; `resolution.py:132`, `:176`;
`effects_migration.py:190-198`; `effects_economy.py:110-122`, `:292-305`; `predicates.py:380-396`;
`gate.py:355-393`; `faction_q.py:186-196`; `options.py:1196-1212`; `rosters.yaml:1098-1110`,
`:1440-1465`; `offices.yaml:128`, `:189-191`, `:589-591`; `NPC-088.yaml:18-36`;
`descriptor_registry.yaml:27-48`, `:61-65`; `descriptors.py:48-54`; `combatant.py:93-94`;
`core.py:54-56`; `fight.py:45`; `fieldwork_v30.md:296-308`, `:351` (quarantined, read for intent
only); `10_verbs_and_attributes.md:100-160`; `09_the_character_sheet.md:127-133`; the 2026-08-15
proposal `:112`, `:122-125`, `:147`, `:150-162`, `:170`, `:188-203`; v9 `_part4.md:34`,
`_part5.md:70-79`, `:433`, `:444`, `:465-471`, `_part7.md:44`, `:51`, `:58`, `_part8.md:207`;
`04_CODE_ARCHITECTURE.md:1144-1156`; the ED-IN-0185, ED-IN-0193 and ED-WR-0011 lines;
`troop-stock-design.md` (by grep, under a sibling's edit); `research/by_lane/SC_social_contest.md:710`,
`FA_faction_actions.md:582`.

**Probes run (read-only; scripts in the session scratchpad, not committed). All six were run in the
correction pass and printed what is shown [RAN].**

1. `python <scratchpad>/tmpl/cap_count.py` (all 143 corpus cases via `corpus_run.build_at`, then
   `build_realm(0)`) printed `cases 143`,
   `corpus persons 430 nonempty capability 1 [('NPC-088', 'p_a', {'copying': 3})]` and
   `realm persons 83 cohorts 37 nonempty capability 0 distinct born [0] distinct body [1000] nonempty conviction 46 nonempty pursuits 46 nonempty stance 35`.
2. `python <scratchpad>/tmpl/change_probe.py 4` (4 realm seasons, seed 0, `populated.run`) printed
   `seasons 4 persons at build 83 at end 63 {'conviction': 0, 'pursuits': 0, 'body': 4, 'stance': 0, 'capability': 0, 'scar_nonempty': 27}`.
   This compares the 63 present at the end. Why 20 are gone was not examined.
3. An inline `build_realm(0)` walk over the 46 non-cohort persons printed `cast 46 nonempty ledger 0`,
   tenure kinds `{'contain': 46, 'reside': 46, 'commit': 141, 'hold': 47, 'oblige': 2}`,
   `cast holding>=1 hold 31`, and stance rows per person `[(0, 11), (1, 5), (2, 22), (3, 6), (6, 2)]`.
4. An inline call of `sigma._pool_of`, `sigma._obstacle_of` and `combat.party_end` on three realm
   persons (`capability` `{}` and `{copying: 5}`; `body` 100 on the third) printed
   `pool tell a,b 2 5 | pool fight b 2`, `ob vs a,b 2.0 2.5`, `party_end a,c 4 2`, with
   `pool_default 2 obstacle_default 2`.
5. `git grep -nE 'import[^#]*\bATTRIBUTES\b|descriptors\.ATTRIBUTES|ATTRIBUTE_(FLOOR|CEILING)|ATTRIBUTES_PENDING' -- '*.py'`
   (excluding the owner) printed three lines, all in `tests/valoria/test_descriptors_runtime.py`:
   no importer in `engine/`, `modules/`, `systems/` or `tools/`. (The first draft's grep matched the
   English word in a comment, `state/gate.py:1269`.)
6. `aperture.measure_world(populated.build_realm, 0, 4)` printed `control hash equal: True acts 2432 2432`,
   `executed verbs: 25` and `attempted verbs: 35`, with the per-verb counts in §3A.2.1. The
   `resolvable_verbs()` count (37) and the 8 unresolvable rows were printed by
   `python -c "from engine.season.loop.driver import resolvable_verbs; …"`.

Every grep quoted in this proposal runs over tracked source files (`git grep -- '*.py'` or a named
file), so a `__pycache__/*.pyc` copy is never counted. The one that did not (§4.6's hash reach) is
corrected there.

**Not checked.**

- No pytest run (no test reads these files: `git grep -l character-template -- tests engine tools`
  prints nothing [RAN]). No seeded OUTCOME comparison (probes 4 and 5 are inputs only).
- The quarantined designs: threadwork, personal-combat reference, social-contest parameters. **Not
  opened.** Fieldwork's §4.2 and §4.5 were opened in the correction pass.
- The uploads behind `out/UP*.md`: not opened; cited as scratch extracts.
- The mass-battle `brace` body; `world_q.residence_of`; `epistemic.py:541`'s use of
  `establishment_of`; `build_army`'s span check body (`systems/mass_battle/sim/engine.py:271-329`,
  located by grep only).
- Golden JSON pins.
- The lane reference for PD2.
- The 2026-08-15 proposal's measured attribute spreads (not re-run).
- The plan's 17 executed verbs in `corpus_run` (`_part5.md:471`): cited, not re-run.

**Locator corrections.**

- The brief's pointers to `_part5` around `:504` and `:515` do not exist in this tree
  (`wc -l` → 475). The J-13 text is at `:433`, and the ten-attribute evidence at `:444`.
- The research suite's *"[CHECKED p5:515]"* (`00_COMPARATIVE_ANALYSIS.md:78, :214, :528`) and the
  critics' `_part5:504` and `:514` point at the same missing lines.

**Locator count, and the brief's aim of at most 70.** The aim is NOT met. The added demand table,
the when-complete stub sources and the master verb table each brought their own sources.

The count, re-taken after the correction [RAN], by
`grep -oE '[A-Za-z0-9_./-]+\.(py|yaml|md|jsonl):[0-9]+' <file> | sort -u | wc -l` (distinct) and
``grep -oE '`:[0-9]+' <file> | wc -l`` (bare continuations, every occurrence):

| file | distinct `path:line` locators | bare continuation locators (`` `:NNN ``) |
|---|---|---|
| the head | 148 | 40 |
| `_part2` | 73 | 58 |
| this part | 107 | 40 |

Most of `_part2`'s come from one reproducible command, `grep -n '^  - verb:' engine/season/verb_table.yaml`.

---

## Critic reconciliation

The independent critic's report (scratch `critics/CHAR_TEMPLATE.md`, 22 findings; verdict *"does
not meet 100% accuracy"*) was read in full, and each finding's locator was re-opened before any text
changed. **Applied**: the finding reproduced and the text now says what the locator says.
**Narrowed**: it reproduced in part, and the part that did not is stated with its evidence.
**Rebutted**: it did not reproduce. No finding was rebutted outright.

| # | finding | verdict | where |
|---|---|---|---|
| 1 | Recall and the inquiry verbs' kinds are sourced, not "open" | **applied.** The fieldwork design's §4.2 maps `examine`/`surveil` → Cognition, `interview` → Attunement, `research`/`reconstruct` → Recall, `thread_read` → Spirit with TS (`fieldwork_v30.md:301-306`, `:351`); `examine` gates its Buried depth on TS ≥ 10. J-T2 now rests on the sibling's *"a capacity, not attribute"* (`10_verbs_and_attributes.md:152-156`), not on "no reader". AX-7's competence is split off as a per-deposit question (PD1b), which stays open | head §0.6, §3.1 PD1a/PD1b/PD5, §3.2, §3.3; `_part2` §A.2.1 rows 36–41, §A.3; §8 J-T2, J-T9 |
| 2 | Charisma's Face ceiling moves no outcome | **applied.** Charisma's one outcome-moving reader is `derive_command`. Also found: the v30 adjudicator-primary attribute (`modes.py:426-431`) is a label read only by a print (`agon_harness.py:229`) | head §0.6, §3.1 CD1, §3.2, §3.3, §3.6; `_part2` row 35, §A.4; §9 SC row |
| 3 | `form_knot` reads TS, a `bonds // 2 + 1` cap and a `spirit × 2 + history` roll | **applied.** `tie / knot` reads 4 kinds | head §3.1 CD6, §3.3; `_part2` row 42, §A.3, §A.4 |
| 4 | Command is not in the default exchange pool | **applied, and narrowed.** The orchestrator's brief said Command reaches "span, recall, reform only". Re-opened, it also reaches the feint-recognition roll (`orchestration.py:2598`), the morale-erosion divisors (`:2252`, `:2835`; `core/state.py:96`), yield eligibility (`core/state.py:105`), `h_per_size` (`units.py:2815`) and rout at 0 (`:2893`). The span check was located by grep, not opened | head §3.1 CD3, §3.3; `_part2` row 22, §A.4; §7.3 R-WORLD |
| 5 | `speak` reads nothing today; its "when complete" mapping is invented | **narrowed.** Today: applied, `speak` reads nothing. When complete: the CHA half was invented and is gone; a PRA reading has a source: *"`speak` becomes the contest"* (`10_verbs_and_attributes.md:123`) plus the existing `speak: "copying"` mapping (`rosters.yaml:1107`), tagged T4 and conditional | head §0.6, §3.1 CD1, F15; `_part2` row 32 |
| 6 | rally is an empty hook; the Command gate is `reform_check`'s | **applied** | `_part2` §A.1 (rally folded into `march`), §A.4 |
| 7 | the verb table's inclusion rule is uneven; non-verbs counted | **applied.** One rule, five exclusion classes, applied to every candidate. Excluded beyond the critic's list, by the same rule: the spoken lie (an arm of `tell`), resigning (composes on `release`), `form_knot` (the stub of row 42), and the seven contest moves and four mass-battle checks. **65 rows**; capacity-kind split **11 / 2 / 6 / 46** | `_part2` §A.1, §A.3; head §0.6; §7.5 |
| 8 | the overlay is both folded and not folded; `copying: 3` copied | **applied.** The overlay stays the owner; the template copies no overlay value; the realm person seats none | head §0.8, §3.5 tests; §4.1, §4.4, §4.6, §5 |
| 9 | Option A does add a `Person` field (J-T1a) | **applied.** `thread_sensitivity` under either option; the hash moves when it lands | head §0.8, §3.5, §3.6; §4.5, §4.6, §6, §7.1, §8 J-T1a |
| 10 | the field-state rule is not a partition | **applied.** Five ordered tests, first match wins: **8 / 1 / 3 / 2 / 7** (F3 moves to not carried) | head §0.3, §2 |
| 11 | F11 has two obligee rows and four readers | **applied, and narrowed.** Two rows (`offices.yaml:191`, `:591`). Of the four readers, `faction_q.superiors` has only a test caller, and the renewal walk reads termed edges, which the two seeded ones are not | head §2 F11 |
| 12 | the hash-reach count included `.pyc` copies | **applied.** 19 source files (17 / 0 / 2), by `git grep -- '*.py'`; the `stats`/`ts` grep's two test hits named | §4.6, §6, §10 |
| 13 | SHIPPED is a row count, not execution | **applied, and widened.** `resolvable_verbs()` drops 8 rows, not 6: `carry` and `construe` too. The realm run executed 25 verbs; the plan's corpus figure of 17 is cited | `_part2` §A.1, §A.2.1; head §0.6 |
| 14 | J-T5 is not answered by precedent | **applied.** Deferred to K-1, with reasons | §8 J-T5 |
| 15 | J-T4 may be answerable | **applied.** Answered at step 3, [medium; Jordan to correct], with a revert | §8 J-T4 |
| 16 | J-T1's framing omits ED-IN-0185's closure, the plan's narrow gloss, and material for A | **applied** | head §0.4, §0.5, §3.2, §3.4; §8 J-T1 |
| 17 | 04 F.6 is the ASSUMED column of a failure table | **applied.** Cited now for its repair (a practice verb), not its assumption | head §3.5; §4.4; §7.4 |
| 18 | sigma's "pool = value" is assumption-graded | **applied** | §7.4; §8 J-T6 |
| 19 | "axis" and P1–P5 / R1–R6 collide with tree terms | **applied.** "capacity kind"; CD1–CD9, PD1–PD5, LR1–LR6 (no hits for any of these in the tree before this edit, by `git grep -lE`) | all three files |
| 20 | options framed as complete; A-1 and J-13 (ii) omitted | **applied.** Each option's open cells named; A-1 and J-13 (ii) added | head §0.4, §3.7; §8 J-T1 |
| 21 | the meta-rule cut column overstates | **applied.** A column says which cuts remove anything: one does | §6 |
| 22 | minor items | **applied**: role templates (six in `values:`, five assigned, one unclaimed); A-4 is an option, not history; ED-IN-0193 does not list the nine; ED-WR-0011's provisional qualifier; person-held reads on `migrate`, `comply`, `survey`, `reconstruct`, `give` (and `tell`); `restore`/`work` **open** | head §1, §3.2; `_part2` §A.2.1; §4.2 |
| — | found in this pass, not by the critic | `practice`'s supersession is at `_part8.md:207`, not `_part7.md:51` (the critic had confirmed the wrong line); troop-stock line numbers moved under a sibling's edit and were re-taken; the ATTRIBUTES grep's one "hit" was an English word | `_part2` §A.1; head §1, §3.2; §10 probe 5 |
