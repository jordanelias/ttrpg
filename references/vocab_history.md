# vocabulary registers — history

Companion to the vocabulary registers under `references/`. **The YAML files are STATE; this one is HISTORY.**
Reference only: no code consumes it as a fact (CLAUDE.md §0.05); `tools/validate_ed_citations.py` scans it like every `references/*.md`. It is not read at session start.

## Why the split (B-X, 2026-10-06)

Jordan, 2026-10-06: *"you can extract all edit histories/discussion from .yaml files in references and
just make those a supplement"*. The precedent is `references/id_reservations_history.md`. Dated narrative,
rationale and provenance moved here **verbatim, not rewritten; nothing was deleted**. What stayed in each
YAML is its title or purpose statement, schema, field definitions, anything a loader, validator or test reads, and a pointer
line to this file.

**Which file is the head.** `alias_registry.yaml` and `censured_vocabulary.yaml` are GENERATED views
(`tools/vocab_store.py --build`); their header comments are the `view_headers:` strings in
`references/definitions/vocab_source.yaml`, the authored head. So the text below was moved out of
`vocab_source.yaml`'s `view_headers:` block and the two views were re-derived with `--build`, never
hand-edited. `proper_noun_registry.yaml` and `action_vocabulary.yaml` are hand-authored.

**Files of the family left whole, and why** (each reader opened before deciding):

- `name_collision_database.yaml` — RATIFIED a permanent historical snapshot, left exactly as ratified
  (ED-IN-0029 docket, OPT-AV-14). Its inline `# COLLISION` / `# NOTE` comments are READ AS DATA:
  `tools/vocab_store.py` `_frozen_data` lifts them into `note:` fields and `--check` compares them with
  the mirror in `vocab_source.yaml`; `tests/valoria/test_vocab_store.py` asserts the file stays untouched.
- `deprecated_terms_registry.yaml`, `synonym_registry.yaml` — GENERATED, and their comments are only the
  generator's two-line stamp, which `test_views_are_generated_stamped` reads. No history in them.
- `silo_overlap_matrix.yaml` — no comments; its narrative is data values (`verdict_+_rationale`), part of a
  ratified frozen snapshot. Moving them would change the data.

**Adding here, not there.** New dated narrative about one of these registers goes in this file under its
heading, not back into the YAML's comments.

---

## alias_registry.yaml

Moved from `vocab_source.yaml` `view_headers.alias_registry`. What stayed in the generated header: the
title, the Purpose paragraph, "source of truth for how mechanical terms may be written", the schema block,
a one-line statement that `tools/valoria_collator.py` does not exist, and the pointer.

```
Valoria Alias Registry — Mechanic Naming

Purpose: canonical name → aliases/abbreviations/legacy names for mechanical
terms (distinct from the proper noun registry which handles world entities).

This file is the source of truth for how mechanical terms may be written.
WARNING (2026-09-16): tools/valoria_collator.py DOES NOT EXIST, and this header
claimed for months that it enforced this file. The three checks below are a
SPECIFICATION of what a collator would do, never a description of what runs.
The live readers of the generated alias_registry.yaml are ci_naming_check.py and
validate_ed_citations.py, and neither performs them. Nothing under engine/ or
systems/ reads this registry at runtime at all. Bearing on ED-IN-0025, the open
7-vs-9 core-attribute split: only ONE side of it is live, since the nine in
descriptor_registry.yaml are cooked behind a blocking --check and read at
runtime while these seven are enforced by nothing. That does not decide
ED-IN-0025, which is a design question with a ledger row, but the two rosters
are not peers and a session weighing them should know it.
The collator (tools/valoria_collator.py) checks every design/params file
against this registry and flags:
  - Uses of an alias without the canonical term on first use in a section
  - Uses of a legacy/collision abbreviation that must not appear alone
  - Uses of an unknown abbreviation not registered anywhere

Seed source: references/glossary.md (2026-04-02)
```

## censured_vocabulary.yaml

Moved from `vocab_source.yaml` `view_headers.censured_vocabulary`.

```
Authoritative term-governance store referenced by PP-675 / ED-783 (Canon Rectification, 2026-04-25).
Populated 2026-04-30 (PP-691) following terminology vector-audit.
```

## proper_noun_registry.yaml

Hand-authored. Moved from `proper_noun_registry.yaml`. What stayed: the title, the Categories line, and at
each of the two entries below a one-line comment saying the row is a mirror of `names_index.yaml`, which is
authoritative.

Header, lines 1-4 of the file (the first line, `Valoria Proper Noun Registry`, stayed):

```
Auto-triage round 2: 466 candidates fully classified
```

`factions.faction_x` (comment above `canonical: "faction x"`):

```
⚠⚠ A TEST FACTION, NOT CANON — RULED by Jordan 2026-09-18: "place them all under 'faction x'
as a test faction". THIS FILE IS A MIRROR: `references/names_index.yaml` is authoritative
and `tools/ci_names_consistency.py` refuses a divergence, which is how this entry came to
exist — the gate caught the missing mirror on the same commit that authored the index row.
It exists so `engine/season/harness/governance_spine.py`'s generic governance spine can seat offices:
`office_faction` refuses an office naming neither a `body` nor a `faction`, so a fully
generic seat is forbidden by design (`H-99` + §42.2's polarity rule).
```

`factions.church` (comment above `canonical: "Church of Solmund"`):

```
⭐ RULED by Jordan, 2026-09-13: "the church is Church of Solmund." Kept in step with
`references/names_index.yaml`, which is authoritative and which `tools/ci_names_consistency.py`
enforces this mirror against — the gate caught this row the moment the index moved, which is
the gate working. `Church` becomes an alias, not a deprecation: the short form stays lawful
prose and the 256 occurrences below are not a rename backlog.
```

## action_vocabulary.yaml

Hand-authored. Moved from the head comment. What stayed: the title, the "Central home" paragraph, the `da.*`
distinction paragraph, a one-line PROVISIONAL statement, and the `awaiting/pending` comment above
`blocked_on:` — that one stays because `tools/validate_ed_citations.py` classifies `ED-FA-0002` by the words
around it and the comment supplies them.

The `STATUS: PROVISIONAL` paragraph:

```
⚠️ STATUS: PROVISIONAL. This is NOT the authoritative domain-action registry — the
`domain_actions` subsystem home is unbuilt (doc:null, zero code; module_contracts.yaml
port_rank 8, resolver d_sigma). The verbs below are curated from the module_contracts
ED-FA-0006 verb note + the faction_state wiring note's "conquest/muster/govern/uniques" enumeration,
exactly as they were previously hand-listed in the audit. When the domain_actions home
is authored (ED-FA-0002), that becomes the source of truth and this roster should be
regenerated from / folded into it — treat this file as the relocation of a provisional
hand-list, not a design ratification.
```
