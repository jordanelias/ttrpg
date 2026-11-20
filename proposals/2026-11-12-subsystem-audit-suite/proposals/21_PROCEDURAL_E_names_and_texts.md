# 21 · PROCEDURAL E — names by grammar, and the document templates generation needs

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row names_and_texts CONFORMS, §2 (no ruling binds it), §7, 7b; `unified/U3_DEPENDENCY_ORDER.md` §1 item 39, §3.1). Changed: tests named; the `--names` flag stated as an edit to `harness/worldgen.py` (PROC_A (d)); the name lists marked INCOMPLETE at the item with the blocking reason; dependency, batch and tier lines. No body text is superseded.

Depends on: `21_PROCEDURAL_B_cast_and_seats.md` (B39; `generate_person` calls `name_for`); `21_PROCEDURAL_A_worldgen_tables_and_ground.md` (B39; `harness/worldgen.py`).
Lands in batch: B39 (lane WR), after `21_PROCEDURAL_B`; the loader and checks one commit (inert while the lists are empty); the lists when authored, one commit each.
Tier: sonnet / high for the loader, checks and tests; the lists are content (Jordan's, or opus-drafted for his correction).

## Status: PROPOSED (2026-11-12; Fable design lane; ratifies nothing; reference under CLAUDE.md §0.05)

Carries `audits/21_PROCEDURAL_GENERATION.md` §4.9; plan batch **PG-8**. Depends on
`21_PROCEDURAL_B_cast_and_seats.md` (the person generator that calls it). The chronicle is not here: it is
`proposals/09_WR_B_chronicle_that_tells.md`'s.

## 1. What changes in `engine/season/` at runtime

With no generated person (`variable=False`): nothing.
With the generated cast on: each generated person's `Person.name` is drawn from a grammar for his
heritage; each generated Record (a pedigree, a letter of debt, a charter of a local seat) carries a
structured `subject_matter` from which its text can be rendered. Names enter the world hash (they are
`Person.name`); display-only colour does not.

## 2. The problem, with evidence

- A generated person needs a name that is not a role label, does not collide with canon or the cast, and
  sounds of its place. Until this lands, proposal B names a person by role and settlement ("the reeve of
  Goldenfurt"), which is unique and is furniture.
- The naming gate is blocking and must keep passing: the canonical name is Solmund; the deprecated name is
  refused by `tools/ci_naming_check.py` and at edit time by `tools/hook_naming_guard.py`;
  `references/names_index.yaml` and `references/proper_noun_registry.yaml` own definition and proper-noun
  names.
- Heritage is a closed set of five (`engine/substrate/descriptors.py::HERITAGES`: `northern_einhir`,
  `central_einhir`, `southern_einhir`, `altonian`, `schoenlander`), authored today for 4 of 83 persons
  (audit §12, P3).
- The precedents: Caves of Qud's replacement grammar stored as nested data and threaded by a domain symbol
  (`E15`); Compton's warning that outputs can be "mathematically distinct yet perceptually samey" (`P01`).
  Neither licenses asserting a cause the engine did not record (`E15.Q2`).

## 3. The resolution, decided

1. **A replacement grammar per heritage, as data.** Given name, plus one of byname, patronymic or
   toponym, each a weighted list. No Markov chain, no model call: every output is a concatenation of
   authored fragments, so every possible name can be enumerated and checked before a world is ever built.
2. **Refusal, not repair.** A drawn name that collides is redrawn with the next attempt key; after
   `max_attempts` the role label is used and the sheet reports it. The lists are checked once at import
   against the reserved sets, so a fragment that *is* a reserved name can never be drawn.
3. **A house device as the thread.** Each generated house (a kin group from proposal B) draws one device
   word; its pedigree and letters carry it. This is Qud's domain symbol at the scale of a family: cheap
   coherence across a house's documents.
4. **Texts render recorded facts only.** A Record's text is a template over its own `subject_matter`; a
   pedigree's ancestral deed is rendered as tradition ("it is held in the house that…"), never as fact.
5. **Colour is display-only and declared so.** Physique, speech and the device's blazon live under a
   `colour:` key that the build stores outside the fields the content hash folds, or is not stored at all
   and is re-derived from the person's key at display time (preferred: nothing to store, nothing to drift).

## 4. Exact edits

**(a) New file `engine/season/worldgen_names.yaml`** (authored for play; every list is content for Jordan
to correct; the lists below show the shape only and are placeholders, not proposals of names):

```yaml
meta: {authority: "AUTHORED FOR PLAY. Not canon. Read by engine/season/data/worldgen.py::name_for."}
max_attempts: 6
form_weights:                      # which second element a name takes, per heritage
  northern_einhir: {patronymic: 5, toponym: 2, byname: 1}
  central_einhir:  {toponym: 4, byname: 3, patronymic: 1}
  southern_einhir: {byname: 4, toponym: 3, patronymic: 1}
  altonian:        {byname: 3, toponym: 3, patronymic: 2}
  schoenlander:    {toponym: 4, byname: 2, patronymic: 2}
given:                             # per heritage: {fragment: weight}; a fragment is a whole given name
  northern_einhir: {}
  central_einhir: {}
  southern_einhir: {}
  altonian: {}
  schoenlander: {}
patronymic_suffix: {northern_einhir: [], central_einhir: [], southern_einhir: [], altonian: [], schoenlander: []}
byname: {northern_einhir: {}, central_einhir: {}, southern_einhir: {}, altonian: {}, schoenlander: {}}
toponym: from_home                 # the person's home settlement's canon name, read from the geography file; never authored here
device: {}                         # {word: weight}: a house's thread symbol
templates:                         # Record kinds generation mints; each field is a key of the Record's subject_matter
  pedigree:  ["{house}", "{ancestor}", "{deed_kind}", "{device}"]
  debt:      ["{creditor}", "{debtor}", "{amount}", "{term_season}"]
  local_charter: ["{post}", "{settlement}", "{conferred_by_post}"]
```

The heritage keys are exactly `HERITAGES`; the loader refuses a missing or an extra one. An empty `given`
list for a heritage that the generator can draw is refused when `variable` is on (a heritage with no name
would silently fall back to role labels and report the grammar built).

**INCOMPLETE (the lists), blocked on content:** the `given`, `patronymic_suffix`, `byname` and `device`
lists are names in the setting's languages; no source in the repository supplies them, and authoring them
is Jordan's (or a drafted list for his correction). Until they exist the loader, the checks and the tests
land and the generator keeps proposal B's role labels.

**(b) `engine/season/data/worldgen.py`:**

```python
def reserved_names() -> frozenset[str]: ...
    # canon and cast: every `canonical`, `aliases` and `legacy` string of references/names_index.yaml and
    # references/proper_noun_registry.yaml (through tools/names.py's readers' data, read via the data
    # package's own loader), every `name` in npcs.yaml and references/npc_registry.yaml, every settlement
    # and territory name in the geography file.
def name_for(seed: int, key: str, heritage: str, home_name: str, tables: dict, taken: frozenset[str]) -> str: ...
def enumerate_names(tables: dict, heritage: str) -> Iterator[str]: ...     # every name the grammar can produce, for the import-time check
```

At import, with the lists non-empty: no fragment and no enumerable full name is in `reserved_names()`;
refused naming the fragment. `legacy` strings are included in the reserved set so that a deprecated name
cannot be produced by concatenation either. `name_for` draws the form, then the parts, each by `pick`
keyed on the person's slot key; `taken` is the set of names already used in the same settlement.

**(c) `generate_person`** (proposal B (b)) calls `name_for`; kin share the house's second element where
the form is a byname or toponym, and take the parent's given name as the stem where it is a patronymic.

**(d) Records:** the generated pedigree, debt and local-charter Records (proposals B (h), B (a), B (f))
carry `subject_matter` as a mapping with exactly the template's keys. Rendering is the presentation
layer's and the chronicle's; the engine stores the structure, never a sentence.

## 5. Gate

Tests: NEW `engine/season/tests/test_worldgen_names.py`: `test_no_enumerable_name_is_reserved`,
`test_planted_reserved_fragment_is_refused_by_name`, `test_same_seed_same_names`,
`test_missing_or_extra_heritage_key_is_refused`. The `--names N --seed S` flag is an edit to
`harness/worldgen.py` (proposal A (d)'s instrument), in this commit.

- Import-time: with the lists filled, `enumerate_names` over all five heritages yields 0 members of
  `reserved_names()`; a planted reserved fragment is refused by name (the falsifier for the check).
- `python -m engine.season.harness.worldgen --names 1000 --seed 0`: 1,000 drawn names, 0 collisions with
  the reserved set, 0 hits from `tools/ci_naming_check.py` run over the printed list, and the duplicate
  rate within one world printed against the size of the name space (so a list that is too short is seen).
- A perceptual check that can fail and is Jordan's to read: the sheet prints twenty names per heritage
  side by side; if two heritages cannot be told apart, the lists are wrong.
- Same seed twice: equal names.

## 6. Falsifiers

- A generated person named as a canon person: the reserved set is incomplete.
- More than a stated share of role-label fallbacks in a world: the grammar is too small for the cast.
- A rendered pedigree stating an ancestor's deed as fact: the template leaked tradition into record.

## 7. NERS reading

- **N:** cut it and generated people are "the reeve of Goldenfurt" forever; RimWorld's finding is that
  names and kin labels are where a reader's attachment forms. The cut is not free and is cheap to avoid.
- **R:** a house's device across its documents gives the world something to recognise with no player
  present. Complete at the extreme that matters: every producible name is checked before any world exists.
- **S:** the heritage roster that exists; the reserved-name owners that exist; structure in the engine,
  sentences in the presentation layer.
- **E, last:** one file and two functions. No model, no corpus, no runtime text generation.

## 8. Cost and dependencies

Edit-class once the lists are authored (the lists are the work, and they are content: Jordan's, or drafted
for his correction). After proposal B. No dependency on any other lane; the chronicle
(`09_WR_B_chronicle_that_tells.md`) is a reader of the names, not a precondition.
