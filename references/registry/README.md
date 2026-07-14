# references/registry/ — target package (WS1 "one registry, one reader")

## Status: PROPOSED

This is a **skeleton/plan doc only.** No data lives under `references/registry/` yet, and
nothing in the working tree has moved. It describes the TARGET end-state of WS1's
consolidation and a proposed fold-in order; it does not itself execute any migration. The
first, already-built increment of WS1 is `tools/registry.py` — a read-only FACADE that
delegates to the three existing resolvers (`tools/names.py`, `tools/descriptor_registry.py`,
`tools/quantity_registry.py`) without moving or copying any of their data. See that module's
docstring for the precedence it uses today. This document is about what comes *after* that,
once the facade has proven itself — not a description of anything currently executable.

---

## 1. Why a package, not one file

The corpus currently spreads name/term/vocabulary data across roughly 20 files in
`references/`, with three different Python readers (`names.py`, `descriptor_registry.py`,
`quantity_registry.py`) each owning a slice, plus a long tail of registries with no live
Python reader at all (see §3). `tools/registry.py`'s docstring already narrates the target
flip: vocabulary data moves into `references/registry/*.yaml`, and the three existing
modules — plus any of the long tail worth keeping — become thin backward-compatible SHIMS
over a single reader (this package + a successor to `tools/registry.py`), instead of each
owning a private slice that a facade merely visits.

A **package** (multiple partitioned files under one directory), not one monolithic YAML,
because the source data has genuinely different shapes and edit cadences (a 9-attribute
scalar roster changes on a different rhythm than a 460-entry proper-noun census), and the
existing co-filing convention (CLAUDE.md §4) already expects registries to split along
content boundaries rather than accrete into one file.

---

## 2. Target package structure

Seven partitioned files, each with a single content domain. Proposed names below; exact
schemas are NOT designed yet (that is separate follow-up work, not part of this skeleton).

| File | Domain | Today's equivalent (current source of truth) |
|---|---|---|
| `names.yaml` | Canonical display names, aliases, legacy/deprecated forms, per-entry enforce tier | `references/names_index.yaml` (read by `tools/names.py`) |
| `descriptors.yaml` | Attribute/aggregate/faction/practitioner/territory/settlement stat descriptors (KIND, scale, source doc) | `references/descriptor_registry.yaml` (read by `tools/descriptor_registry.py`) |
| `entities.yaml` | Proper-noun census — characters, territories, factions, organizations, realms, peoples, concepts, structures | `references/proper_noun_registry.yaml` (+ its triage trail, §3) |
| `glossary.yaml` | Term expansions / abbreviations (e.g. "Thread Sensitivity (TS)") and first-use rules | `references/glossary.md` (currently prose, hand-maintained; needs prose→structured-data conversion, not just a fold — see §5) |
| `aliases.yaml` | Different words for the same mechanical concept; canonical winner per concept | `references/alias_registry.yaml`, `references/synonym_registry.yaml` |
| `deprecated_terms.yaml` | Retired/superseded/censured terms that must not appear in active docs | `references/deprecated_terms_registry.yaml`, `references/censured_vocabulary.yaml`, `references/orphan_terms_registry.yaml` |
| `vocabulary.yaml` | Cross-silo collision ledger / "one term, one silo" enforcement data | `references/name_collision_database.yaml`, `references/collision_registry.yaml` |

**Open question, not decided here:** whether `vocabulary.yaml` also absorbs the *computed*
merge `tools/quantity_registry.py` currently builds at runtime (its `known` dict), or stays
scoped to collision/silo data only, with the merge continuing to be computed by a reader
rather than stored. Deciding this is a later checkpoint (§6), not this skeleton.

---

## 3. Fold-in migration order: frozen/dead registries first, then live-by-reference

The guiding principle: fold the registries with **zero or near-zero blast radius first** —
proving the package shape and the shim pattern on files nothing currently depends on
changing — before touching the registries live tooling and CI gates actively read today.
Classification below reflects what was actually verified in the working tree while drafting
this doc (grep for consumers, header/disposition comments in the source files themselves,
and CLAUDE.md §8's own dead-tools list), not assumption.

### Phase 1 — frozen / orphaned (fold first)

Confirmed **no live regeneration path**, by the source files' own disposition notes
(RATIFIED 2026-07-08, ED-IN-0029 docket, OPT-AV-14 — "permanent historical snapshot"):
  - `references/mechanical_terms_index.md` — its would-be regenerator, `tools/valoria_collator.py`,
    is itself dead (CLAUDE.md §8's retired-tools list).
  - `references/collision_registry.yaml`, `references/orphan_terms_registry.yaml`,
    `references/synonym_registry.yaml`, `references/deprecated_terms_registry.yaml` — all
    extracted FROM `mechanical_terms_index.md` (2026-05-10) and inherit its frozen status;
    the latter two are also explicitly named as one-time "seed" sources already folded into
    `names_index.yaml`/the drift lint (per `names_index.yaml`'s own header comment), not
    registries anything re-reads on an ongoing basis.

Confirmed **orphaned** — the one consumer named in the file's own header is itself dead or
retired (verified by direct grep, not inferred from the registry's self-description alone):
  - `references/alias_registry.yaml` — its stated consumer, `tools/valoria_collator.py`, is
    in CLAUDE.md §8's dead-tools list.
  - `references/name_collision_database.yaml` — its stated consumer,
    `abbreviation_registry_gate` in `valoria_hooks.py`, lives under
    `skills/valoria-orchestrator/scripts/`, and that skill directory no longer exists at a
    live path (confirmed: only present under `deprecated/skills/valoria-orchestrator/`).
    `tests/hooks/test_abbreviation_registry_gate.py` still imports from the old live path.

One-time triage/batch artifacts (drained queues or decision logs already applied):
  - `references/proper_noun_candidates.yaml` (`total_candidates: 0` as of this writing —
    an emptied review queue).
  - `references/proper_noun_triage_decisions.yaml`, `references/proper_noun_triage_round2.yaml`
    (decision logs already applied to `proper_noun_registry.yaml`; historical provenance,
    not a live input).

Not confirmed either way — flagged for verification before folding, not asserted:
  - `references/censured_vocabulary.yaml` — a point-in-time population (PP-691, 2026-04-30)
    following a vector-audit; no live Python reader was found by grep while drafting this
    doc, but that is a "not found," not a proof of absence. Verify before treating as frozen.

### Phase 2 — live-by-reference (fold last, highest blast radius)

Each of these has a confirmed live reader today; folding any of them requires the
"old resolver becomes a shim" step (not yet built — this is planning only) to land in the
**same change**, so no consumer ever sees a gap:
  - `references/proper_noun_registry.yaml` — read by `tools/ci_names_consistency.py`
    (mirror-consistency gate against `names_index.yaml`'s `world.*` entries).
  - `references/glossary.md` — no automated reader, but explicitly documented as hand-
    maintained "in the same commit as any file that introduces or retires a term" —
    editorially live even without a Python consumer. Highest-EFFORT item in this table: it
    is prose today, not data, so folding it is a content transformation, not just a file
    move (see §5).
  - `references/descriptor_registry.yaml` — read by `tools/descriptor_registry.py` directly,
    and by `tools/quantity_registry.py` (via that module), and scanned by the A17 quantity-
    vocabulary CI check.
  - `references/names_index.yaml` — read by `tools/names.py`, `tools/quantity_registry.py`,
    `tools/ci_naming_check.py` (block-tier hard gate), `tools/ci_names_check.py` (warn-tier
    drift lint), `tools/valoria_rename.py`, and `tools/ci_names_consistency.py`. Widest
    blast radius of any single file in this table — fold last of all, and only once every
    dependent tool's shim has landed and been verified green.

### Explicitly out of scope for this migration

  - `references/values_master.yaml` — a *values* registry (mechanical parameter numbers),
    not a *names/vocabulary* registry, and separately already flagged quarantined-stale
    (CLAUDE.md §1/§4, ED-1084). Different problem; do not conflate with this package.
  - `references/scope_vocabulary.md` — a *dev-process* vocabulary (commit scopes / session
    scopes), not game-mechanical term naming. Unrelated axis.
  - `references/id_reservations.yaml`, `references/canonical_sources.yaml`,
    `references/module_contracts.yaml`, and other structural registries — different
    concerns (ID allocation, canonical-source pointers, module I/O contracts), not naming.

---

## 4. What this migration does NOT change (invariant across every phase)

  - No consumer-visible behavior changes as a *result of moving a file* — every fold-in
    step pairs the data move with a shim in the old reader module in the *same* change, so
    `import names; names.canonical(...)` (etc.) keeps working, unchanged, for every existing
    caller across the corpus.
  - No new ID/ledger allocation is implied by this doc itself; each phase's actual
    execution is its own future piece of work, entitled to its own `ED-<LANE>` citation
    when it happens.
  - This doc does not commit Jordan to the fold-in order above — it is the AGONIST's
    proposal for review, explicitly marked PROPOSED, not a ratified plan.

---

## 5. Known hard part: `glossary.md` is prose, not data

Every other row in §2's table has a structured YAML source already (even the frozen ones).
`glossary.md` does not — it is 283 lines of hand-written markdown with usage rules,
abbreviation-parenthetical conventions, and per-section prose. Converting it to
`glossary.yaml` is a genuine authoring/extraction task, not a mechanical file move, and
should be scoped and sequenced as its own step when Phase 2 is actually executed — not
assumed to be free because every other fold-in in this doc is (relatively) mechanical.

---

## 6. Follow-on decisions this doc deliberately leaves open

  - Exact YAML schema per target file (key names, whether `descriptors.yaml` keeps
    `descriptor_registry.yaml`'s domain-partitioned shape or normalizes further).
  - Whether `tools/registry.py` itself becomes the permanent reader, or is superseded by a
    generated/typed reader once the package exists (see CLAUDE.md §5's parallel discussion
    of a typed engine-params layer — the same "prose/derived-data now, typed data later"
    arc may apply here too).
  - Whether `quantity_registry.py`'s runtime-computed merge becomes precomputed data in
    `vocabulary.yaml` or stays a computed view (§2).
  - The precise commit sequencing of "data moves" vs. "shim lands" per file (this doc
    asserts they must land together; it does not choreograph the actual PRs).

None of the above blocks today's increment (`tools/registry.py`); they are follow-up
checkpoints for whoever picks up WS1's next phase.
