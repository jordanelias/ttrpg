# CORE — one authoring surface for character capabilities

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-08, C-U5a-11) — the home proposed here (`references/descriptor_registry.yaml: capabilities`, the verb-row column) is the decided one: `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §1. Changed by that file and by Jordan's answers: Edit 1's `kinds` drops `attribute`, `untrained_rules` is `[default, none]`, every row carries `gloss`, `growth_rules` gains `fixed`; Edit 8's values are U1 §5's (`arrest: arms`, `lie: deception`, `determine: law`, each `none` with a note until its definition row exists); Edit 9 is kept as `max(untrained score, rank)` and its `untrained: attribute` arm is removed (A-7: talent and training are two inputs, never folded); **Part three is withdrawn** (A-11: a capability never gates an act). The roll these rows feed is U1 §4; the ordered plan is `U5a_capability_home_and_two_inputs.md`.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row 1, §2 row 1, §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-07, ledger C-02, C-03, C-04, C-09; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2, §3, §5, §11 batch U1-A; `unified/U3_CONFLICT_LEDGER.md` C3-N27). The body now follows the head it already carried: Edit 1's block is U1 §2's (`kinds [skill, aptitude, trait]`, `grows_by [train, practice, use, fixed]`, `untrained [default, none]`, `scale: [0, 7]`, `gloss` required); Edit 2's row and refusals carry `gloss`; Edit 8's table is U1 §5's; Edit 9 is `max(untrained score, rank)` with no `untrained: attribute` arm; Part three's body is replaced by a one-line pointer (A-11); the "Not here" paragraph names U1 §3's columns; named tests, the check's hash caveat (B01 moves the pin) and lands-it and tier are added. Layer 1: the verb-row column meets `04` §B.13 against §C.4 (AMBIGUOUS); U1 §1 picks the column under B4's third disposition (a missing value is a load refusal, MECHANICAL); nothing in `04` is edited. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "vocation" → "capability" in prose (glossary *capability*; tree ids keep their names).

**Lands in batch:** B04 (Part one; Edit 8's values with CAP A2/A3), Edit 9 in B05 (CAP Part B, U1-B). **Depends on:** B02 (`01_CORE_tests_one_golden_owner.md`, the one pin file); `10_DICE_capability_axiom_map.md` (B04); `U5a_capability_home_and_two_inputs.md` Part A (B04); each new capability's definition row before any verb cell names it (`deception`, `law`: `05_SC_hearing_capabilities.md`, B04).

## Status: PROPOSED

Source: `audits/01_CORE_audit_addendum_B.md` §5 (the brief's §14), F-CORE-15. Read at `785bc62`.

## What it changes in `engine/season/` at runtime

Part one changes nothing a season computes: the same pools, the same obstacles, the same content hash at
shipped data. It moves where three facts are authored and adds a refusal at load. Part two moves play
(each edit a declared hash mover with its control). Part three is withdrawn (A-11: a capability never gates an act).

## The problem, with evidence

`seam/wrappers/pool.py::faculty` is the one pool reader and is sound. The facts it reads have no single
author and no definition:

| fact | file |
|---|---|
| which capability a verb's roll draws on | `engine/season/rosters.yaml: verb_capability` (keyed by verb, outside the verb's row) |
| which attribute a capability starts from, and which opposes it | `rosters.yaml: vocation_attribute` (`values`, `opposed_by`; the second is `{}`) |
| the attribute roster, scale and names | `references/descriptor_registry.yaml: attributes` |
| which capabilities a background grants | `rosters.yaml: lifepaths`, `tables.lifepath_templates` |
| who holds what | `references/npc_registry.yaml` (`stats:`, `lifepath:`), case overlays (`cast: capability:`) |
| the untrained default and the growth numbers | `engine/season/data/fixtures.py` |
| combat's attribute keys and defaults | `modules/combat/attributes.py` |

Measured on the tree: 11 contested verbs, 9 with a capability row, and of the contested ones `arrest`,
`determine`, `lie`, `march` and `interrogate` have none, so every person rolls `pool_default` on them.
`loop/effects_combat.py:262-268` refuses to mint a capability key because a first rank (1) would replace
the untrained default (2) and lower the pool, so no skill is acquired in play. `attr.body.endurance` has
a default of 1 in the registry, 4 in the combat spec and a literal 4 at `seam/wrappers/combat.py:151`.
Nowhere does a row say what a capability *is*.

## The resolution

One block, `capabilities:`, in `references/descriptor_registry.yaml`, on the chain the attributes
already use (exporter with a blocking `--check`, read through `engine/substrate/descriptors.py`). The
verb's side is a column on the verb's own row. The character's side is the cast row. The existing
loaders derive the maps every reader already imports. Nothing is added to `faculty`.

## Part one — the surface (hash EQUAL)

### Edit 1 · owner `references/descriptor_registry.yaml` — new block

```yaml
capabilities:
  source: "U1; A-6, A-7, A-11 (2026-11-12)"
  kinds:    [skill, aptitude, trait]              # closed. The ten attributes are defined in `attributes:` and are not re-defined
  grows_by: [train, practice, use, fixed]         # closed; each names a rule the engine implements
  untrained: [default, none]                      # closed; what a non-holder brings (U1 §4)
  rows:
    copying: {kind: skill, gloss: "Carries a text or a message on exactly as it was given.", base: attr.mind.focus,      opposed_by: none,           untrained: default, grows_by: [train, practice],      scale: [0, 7], source: "rosters.yaml vocation_attribute (CR-20)"}
    argue:   {kind: skill, gloss: "Makes a case to someone's face and moves them by it.", base: attr.social.charisma, opposed_by: attr.mind.will, untrained: default, grows_by: [train, practice], scale: [0, 7], source: "rosters.yaml vocation_attribute (CR-20); ED-IN-0350"}
    inquiry: {kind: skill, gloss: "Finds things out: from a record, a place or a watched person.", base: attr.mind.acuity,     opposed_by: attr.mind.will, untrained: default, grows_by: [train, practice],      scale: [0, 7], source: "rosters.yaml vocation_attribute (CR-20)"}
    arms:    {kind: skill, gloss: "Fights with a weapon in hand.", base: attr.body.agility,    untrained: default, grows_by: [train, practice, use], scale: [0, 7], source: "rosters.yaml vocation_attribute (CR-20); CP-T03-04 (iv)"}
```

The four rows are today's four capabilities (the tree's `VOCATIONS`) with today's attributes, moved; `opposed_by` values are U1 §2's
table (`copying: none`, OBS §2; `argue` and `inquiry` `attr.mind.will`; `arms` absent, which reads `base`).
`gloss` is required and non-empty on every row (the exporter refuses an empty one); its text is
`02_CHAR_capability_definitions.md` Edit 1's. `use` is `_grown`'s rule (a fight that drew blood); `fixed`
is a trait's (it does not grow). `untrained: none` means a non-holder brings nothing (a trait). The ten
attributes stay where they are in the same file and are not a capability kind: an attribute is the
**talent** input of U1 §4, a capability's rank its **training** input (A-7), never folded.

### Edit 2 · owner `tools/export_descriptors.py`, `engine/substrate/descriptors.py`

The exporter cooks the block into the existing artifact; the leaf gains

```python
CAPABILITIES: Mapping[str, CapabilityRow]     # frozen; id -> (kind, gloss, base, opposed_by, floor, ceiling, untrained, grows_by)
def capability(name) -> CapabilityRow         # raises ValueError naming the roster, as resolve_pursuit does
```

The exporter's `--check` (a `_capability_roster(reg)` validator beside `_heritage_roster`, U1 §11 U1-A step 1)
refuses a `base` or `opposed_by` that is none of the ten attribute keys or `none`, a `kind`, growth rule or
`untrained` value outside its closed set, an empty `gloss`, and a `scale` that is not `[int, int]` with floor
≤ ceiling. `engine/engine_params/descriptors.json` is re-derived with the tool, never by hand.

### Edit 3 · owner `engine/season/verb_table.yaml`, `engine/season/data/verbs.py` — a `capability:` column

`VerbRow` gains `capability: str = ""`. The nine rows that have a `verb_capability` line today gain
`capability: <the same key>`. The loader refuses (as it refuses a missing `beneficiary:`): a contested
or graded row with no `capability:` key; a value that is neither a `CAPABILITIES` id nor `none`; `none`
without a `capability_note:`; a `capability:` on a row that neither contests nor is graded (a column
nothing reads) unless the row declares `magnitude: rate` (U1 §11 U1-A step 2; D-U1-09). The task's
difficulty is the sibling column `difficulty:` on the same row (D-U1-04), landed by OBS §4 step 1a in B05, not here. In part one the five undeclared contested rows carry `capability: none` and a note that
says so plainly (*"undeclared at authoring; every person rolls the untrained default"*), which is their
behaviour today.

### Edit 4 · owner `engine/season/data/rosters.py` — derive, and delete the two rosters

```python
VERB_CAPABILITY      = {row.verb: row.capability for row in VERB_TABLE.values() if row.capability not in ("", "none")}
VOCATIONS            = frozenset(VERB_CAPABILITY.values())
VOCATION_ATTRIBUTE   = {k: CAPABILITIES[k].base for k in VOCATIONS}
VOCATION_OPPOSED_BY  = {k: CAPABILITIES[k].opposed_by for k in VOCATIONS if CAPABILITIES[k].opposed_by}
```

These three bindings move to `data/verbs.py` (the verb table loads there; `rosters.py` cannot import it)
and `rosters.py` re-exports nothing of them; `pool.py`, `sigma.py`, `effects_combat.py`, `world_q.py`
and `corpus_run.py` change one import line each. `rosters.yaml: verb_capability` and
`vocation_attribute` are deleted in the same commit, with `_load_vocation_attribute` and
`_load_vocation_opposed_by` (their closure checks are now the exporter's and the verb loader's).
`tables.lifepath_templates` keeps its place in `rosters.yaml`; its `holds:` check reads the capability
ids off the leaf (`descriptors.CAPABILITIES`) instead of `VOCATIONS`, because `rosters.py` loads before
the verb table and may not import it. A template may then grant a capability no verb yet tests, which
the old check refused; the verb loader reports (does not refuse) a capability no row names, as
`tenure_kinds_without_an_opener` reports an unopened kind.

### Edit 5 · owner `references/npc_registry.yaml`, `engine/season/data/cast.py` — the character's side

A cast row may carry `capabilities: {<id>: <whole number>}` beside `stats:`. `cast.capabilities_of(r)`
validates each id against `CAPABILITIES` and each value against the row's scale, refusing as
`attributes_of` does. `capability_of(r, pool_default)` (the lifepath expansion) is unchanged and the two
are merged by the builder with the authored value winning. The case overlay's `cast: capability:` is
validated through the same function (`corpus_run._check_capability` calls it instead of re-checking
keys against `VERB_CAPABILITY`). No row is authored by this proposal: the CHAR lane owns the content.

### Edit 6 · owner `engine/season/decision/sheet.py` — show what is rolled

`DevelopmentSheet` gains `attributes` (a frozen copy, as `CreationRow` has). No derived pool is stored on
the sheet; the play surface asks `View.odds` per candidate as the chooser does.

### Edit 7 · owner `engine/season/seam/wrappers/combat.py:151` — one Endurance default

`party_end` reads the combat spec's default for `end` through the module's typed export
(`engine/engine_params`, section `attributes`, which `tools/export_engine_params.py` already writes) in
place of the literal `4`. The registry's `default: 1` is the scale's floor value for an unauthored
attribute in a *sheet*; the fight's default is the module's. Two different facts, each with one owner;
the literal was a third copy of the second.

**Gate (part one).** `python tools/export_descriptors.py --check` passes; the driver constructs; a
same-seed `headless --case NPC-088 --seasons 2 --seed 0` prints hash `5405522c36b0399247f83fd9f6d29494`
(the first audit's reading at the working tree before B01; every such pin moves at B01, so re-read it on the
batch's base and quote that, C3-N27); `corpus_run` seed 0 reproduces its executed-verb and degree tallies.
**Named tests** (new file `engine/season/tests/test_u1_capability_surface.py`, U1 §11 U1-A):
`test_deleting_the_block_refuses_the_load`, `test_a_contested_row_with_no_capability_is_refused_naming_it`,
`test_a_capability_naming_no_definition_is_refused`, `test_derived_vocation_maps_equal_the_retired_rosters`
(`==` against the retired rosters' values captured as literals, not `approx`).
**Falsifier.** Delete `capability:` from `argue`'s row: the load refuses naming the row. Change
`argue`'s `base` to a name outside the ten: the exporter's `--check` refuses. Either passing silently
falsifies the edit. **Control.** The batch's base tree (hash EQUAL).

## Part two — the two things that move play (each its own commit)

### Edit 8 · the five undeclared contested rows declare a capability

| verb | prize | decided (U1 §5) | ground |
|---|---|---|---|
| `lie` | a standing, counterparty `to` | `deception` on whichever row resolves a lie; `capability: none` with a note until the `deception` definition row lands (`05_SC_hearing_capabilities.md`, B04) | the verb is SC's; a lie is not a faithful copy (U1 §5) |
| `determine` | a proposition | `law`; interim `argue` until `law`'s definition row lands | one thing gets one name; FA's `judgment` collides with the role `judgement` (U1 §5; C-U5a-11) |
| `interrogate` | a proposition, a detained subject | `inquiry` (the row's `opposed_by` is the definition row's, `attr.mind.will`) | unanimous across lanes (U1 §5) |
| `arrest` | a standing, by `remit:dispatch` | `arms` | FA (the verb's lane), DICE and lane A agree; `capture`'s precedent (U1 §5) |
| `march` | a field | `none`, noted | the field's capability enters at the `field` site, on the commander's record (`27_MB_A`) |

Each is one value on one row, shipped behind the row's own revert. Lane A's interim `verb_capability`
rows (`interrogate: inquiry`, `arrest: arms`, `determine: argue`) move to this column (D-U1-07). **Gate.** `corpus_run` seed 0, 1, 2
before and after: the share of `Failure` among graded `determine`/`lie` outcomes for persons who hold
the key against persons who do not (a difference with the same-seed control is the reading; no balance
claim is made from it).

### Edit 9 · a first rank is never a loss, so a skill can be acquired

The score (`seam/wrappers/pool.py::score`, U1 §8) becomes: for a holder of the capability,
`max(untrained score, rank)`; for a non-holder, the untrained score, which is `pool_default` under
`untrained: default` and nothing under `untrained: none`. The attribute is never a fallback for the score
(A-7: talent and training are two inputs; talent enters as levels, U1 §4). At shipped data every held key is at
`pool_default` or above, so this is hash EQUAL until someone holds a rank below it. Then
`raised_capability` may mint: a non-holder's `train` writes `{key: 1}` and his pool is unchanged until
the rank passes the default, and the rank never passes the row's `scale` ceiling. `[ASSUMPTION; medium; Jordan to correct; revert: restore the never-minted
rule]`. **Gate.** A seeded two-season realm run in which a person with no `argue` key trains it:
`capability.raised` is emitted, his `argue` pool is not lower than before, and a second training raises
it; named test `engine/season/tests/test_u1_two_inputs.py::test_a_first_rank_never_lowers_a_pool` (U1 §11
U1-B). **Falsifier.** His pool after the first rank is below `pool_default`. Lands in B05 with CAP Part B.

### Not here · where a capability enters a person's own choice

Which attribute grades a told claim (`decision/options.py:1627`, a name in code) and the
Thread-Sensitivity gate's two hard-wired stems are the decision layer's uses of a capability. The CHAR
lane's `02_CHAR_capability_uses_table.md` resolves both with one table of uses, `rosters.yaml:
tables.capability_uses` (columns `use, role, key, side, when, level, per, against, gain, add, floor`;
U1 §3), and is their owner; this proposal does not repeat them. The two fit by construction: that
table's `key` is a capability id, a registry key (an attribute or a practitioner stat), or the selectors
`verb` / `verb.base` (U1 §3 amendment 1), so a use row may name a skill exactly as it names an attribute.

## Part three — withdrawn

Withdrawn by A-11 (a capability never gates an act; Thread Sensitivity is the one `gate`, at two use
sites, U1 §3 amendment 5). Nothing here is built.

## NERS reading (definitions: `CLAUDE.md` §0.06)

- **N.** Top-down: a designer adds a skill by adding a row and naming it on the verbs that test it;
  today that is four files. Bottom-up: `faculty` reads the same four maps. Lateral: the combat module
  reaches the definition through the leaf it already reads. Removing the block returns the six-file
  spread; removing the column returns verb facts keyed outside the verb. Holds in the directions tried.
- **R.** Customisation of characters is the point: a capability becomes a thing a character sheet can
  list with its meaning. Completeness: the five silent rows and the unacquirable skill are the two
  extremes at which the present design breaks, and part two closes both.
- **S.** One methodology for a pool (the same `faculty`), one ladder; the verb row is the only place a
  verb's facts live, which is the table's own rule. The module seam is untouched.
- **E (last, against N and R).** One block and one column replace two rosters and two loader functions;
  a reader can say which capability fed a roll from the verb row alone.

## Cost class

Part one: edit plus a small build (the exporter and the leaf). Part two: two edits, each a hash mover
(Edit 8 per row; Edit 9 inside CAP Part B's one re-pin). Part three: withdrawn.

**Lands it.** Part one: the B04 batch (U1 §11 U1-A), a `methodology-execute` batch with one commit per edit,
author `valoria-author` on `sonnet` (`high`), close `methodology-close` with its terminal `opus` critique
once per batch. Edit 8: the same batch, one commit per row, each a declared mover said plainly as a
re-record (CLAUDE.md §7). Edit 9: the B05 batch (U1-B), same tiers.
