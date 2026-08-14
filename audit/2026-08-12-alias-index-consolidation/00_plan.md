# Path-alias finding aid — consolidation plan

## Status: RATIFIED as PLAN OF RECORD (2026-08-13, ED-1094) — still no parser moved, no row rewritten, no format changed.
## Date: 2026-08-12 · Lane: IN (cross-cutting) · ED-IN-0173 (allocated retroactively 2026-08-13 — see below)

> **What the ratification does and does not cover (ED-IN-0173).** Under CLAUDE.md §2 / ED-1094,
> Jordan's review-and-merge of the PR carrying this document ratified it, and the `## Status:` flip
> belongs in that merge rather than a later step nobody triggers. Jordan confirmed 2026-08-13 that
> the flip was mine to make. **Ratified: this document as the plan of record** — the ordering, the
> "consolidate while the markdown is still the source" thesis, the phases. **NOT ratified, and this
> plan is the document arguing they must be settled first: Phase A1's five semantics questions,
> which stay HELD for Jordan.** Ratifying a plan is not ratifying the rulings it requests.
>
> ⚠ **This header cited `ED-IN-0173` while `references/id_reservations.yaml` still read
> `next_free: 173`** — the ID was cited but never allocated, so the register would have handed 0173
> to the next unrelated allocation. Allocated retroactively 2026-08-13; the guard that now catches
> this class is `tests/valoria/test_audit_plan_ids_are_allocated.py` (ED-IN-0174), which also records
> why the blocking citation gate could not see it.
## Opening pass: three independent read-only Fable-5 lenses (parsers · data · blast radius)
## Authored by: Opus, from those three reports. Per CLAUDE.md §10 the audit tier does not author.

> **The one-line version.** `references/restructure_ledger.md` cannot be migrated to structured
> data yet, because **five parsers disagree about what its rows mean** and the disagreements are
> not stylistic — the same row resolves five different ways, two of them inside BLOCKING gates.
> The consolidation `pathres` was written to perform must land **first, while the markdown is
> still the source**. That reduces the eventual format change from a five-parser event to a
> one-module event. Anything else inverts the risk.

---

## 0. Four corrections to the premise this plan was commissioned on

Recorded first, because each changes the work.

1. **There are FIVE parsers, not nine.** I told Jordan "nine modules machine-parse it" — that
   figure counted *filename mentions*, not parsers. Two lenses found this independently. Real
   state: five own a copy of the row regex (`pathres:88`, `broken_dependency_checker:115`,
   `ci_claude_workflow_paths:105`, `vector_audit:418`, `workbench:70`); two consume through
   another module's loader (`build_identifier_census` → pathres; `gen_audit` → bdc); and two
   **never parse it at all** — `build_incompleteness` excludes it *by filename*, and
   `evacuation_plan` only emits prose telling a human to write a row.
2. **`build_incompleteness`'s coupling is to the file's NAME, not its grammar** — a substring
   exclusion (`:409-417`). So renaming or moving the ledger breaks it in a way no schema
   design can prevent, and *keeping* the name protects a file that no longer needs protecting.
   This is the one coupling a format migration cannot reason about from the schema.
3. **The file is 1,038 data rows in FIVE distinct table schemas**, not one table.
4. **`gen_audit` reuses the map but not the resolver** (`:381-386`) — exact-row, zero-hop, no
   prefix, no FORK. Its docstring claims it reuses "the SAME map … for exactly this
   disambiguation". It reuses the map; it re-implements the semantics, differently.

---

## 1. The blocking finding: one row, five meanings

The same FORK row (e.g. `engine/params/` → `FORK:c451bcb`, ledger:1169) resolves as:

| consumer | verdict | site |
|---|---|---|
| `pathres` | `FORKED` (a real terminal status) | `pathres:184-191` |
| `broken_dependency_checker` | INFO — "evacuated, not broken" | `bdc:220-224` |
| `ci_claude_workflow_paths` | **DEAD — fails a BLOCKING gate** | no FORK code path exists |
| `workbench` / `vector_audit` | `missing` — indistinguishable from no row | `workbench:163`, `vector_audit:446` |
| `gen_audit` | `nonexistent` — "genuinely dead, needs human triage" | `gen_audit:381-386` |

`test_forked_status.py:9-17` states the whole point of the FORKED status is that **evacuated is
not the same as never-existed** — the anti-fabrication distinction. Three of five consumers
collapse exactly that distinction, and one of them fails a blocking gate on it.

**Four further semantic disagreements**, each of which must be ruled before any schema is
designed, because a schema encodes an answer to each:

- **Hop count.** Chained-6 (`pathres:90`, `cicwp:107`) vs single-hop (`bdc:142-165`) vs zero-hop
  (`gen_audit:381`). Real 2- and 3-hop chains exist in the data (`params/` → `engine/params/` →
  FORK). Under single-hop that chain terminates at a nonexistent intermediate → BROKEN; under
  chained → FORKED. **Rows were duplicated in the data to paper over this**, and the ledger's own
  comment (`:1178-1182`) says so.
- **FORK payload shape.** `bdc` returns the bare sentinel for an exact row (`:151`) but
  `FORK:<ref>:<original-path>` for a prefix row (`:164`) — two shapes from one function.
  `pathres` returns the bare sentinel in both, **losing the sub-path**.
- **Duplicate-key precedence.** Six real conflicting duplicates exist. Exact-dict parsers are
  last-wins; `pathres`/`cicwp` keep prefix rows in a stable-sorted list where **first-in-file
  wins among equal lengths**, while `bdc` scans a dict where the later row already overwrote the
  earlier. Today's answers coincide only by data accident. **A structured format with unique keys
  cannot be generated until this is ruled** — it is the one finding that hard-blocks schema design.
- **Existence test.** `pathres`/`cicwp` accept a hop target via `os.path.exists` — **true for
  directories**; `bdc`/`gen_audit` test membership in a *file* set — **never true for
  directories**. A row whose target is a directory satisfies one family and not the other.

---

## 2. The fidelity findings that constrain any capture

- ⚠ **The FORK table is split mid-table by a 10-line HTML comment (`:1172-1182`), and the
  following 116 rows have no table header.** A header-keyed parser silently drops **116 of 122**
  FORK rows. This is the single largest loss surface and the first thing a capture must prove it
  did not do.
- **50 "stem" rows** (`sim/personal/fieldwork`, `designs/provincial/mass_battle_v30`) are neither
  files nor `/`-terminated directories. They fit no obvious field type, and one is a **string
  prefix of a real filename** (`…mass_battle_v30` vs `…mass_battle_v30_index.md`) — so treating
  stems as prefixes silently captures the wrong file.
- **~300 rows point at targets that no longer exist**: 232 `tests/…` rows where *neither* endpoint
  survives and no FORK row covers them (status still reads `PENDING`), 64 rows targeting the
  retired `designs/` tree, 41 resolving only through a three-hop chain.
- **Three prose/comment blocks carry machine-relevant semantics**, not just rationale: the
  FORK-is-terminal rule (`:1151-1153`), the single-hop + extractor-scope constraint
  (`:1178-1182`), and a **deliberate ABSENCE** — `tools/registry.py` has no row *on purpose*
  (`:1135-1137`). A rows-only migration loses all three, and the third is unrecoverable from data.
- **`atomization_rules.yaml:398-404` cites this file by LINE NUMBER** (`ledger lines 1257-1258`).
  Any reformat breaks that citation silently.
- Minor but real: a garbage row (`| path | PENDING |`, `:510`), a declared count of 470 against
  472 actual rows, five header-label spellings, two benign duplicate rows.

---

## 3. Blast radius

**Two BLOCKING gates parse it** — `broken_dependency_checker` (`valoria-ci.yml:117`) and
`ci_claude_workflow_paths` (`:113`). Both **fail closed** on total parse loss, which is the safe
direction. The dangerous directions are:

- **Partial parse** — a format change that still matches *some* rows. This is the
  `patch_propagation_checker` failure exactly: a blocking-tier parser whose format assumption
  drifted and which "examined zero items for weeks while sitting in the blocking tier".
- **Fail-open readers** — `workbench:73-75` and `vector_audit:423-425` return `{}` on a missing
  file, and **nothing in CI runs them**. That is the ED-IN-0122 "went inert rather than breaking"
  class, with no gate to notice.

**Local/CI asymmetry is live and points the wrong way.** `valoria_local --staged` does **not run
`broken_dependency_checker` at all** and runs `ci_claude_workflow_paths` **report-only** while CI
has it blocking. A migration branch can be fully local-green and CI-red on both blocking parsers.
This session hit that exact asymmetry twice today.

**Pinned behaviour that must stay green** — and note two of these are *format*-coupled, not
content-coupled:

| pin | property | format-safe? |
|---|---|---|
| `test_pathres.py:236-240` | >100 exact + ≥10 prefix rows parse | **No** — the only loud alarm on total parse loss |
| `test_pathres.py:109-112` | `max_hops=1` reproduces bdc exactly | **This is the expected-delta instrument for the bdc port** |
| `test_forked_status.py:41-91` | every FORK ref is a real commit containing the content | Only if bdc's API survives |
| `test_gen_audit.py:66` | object-identity one-owner routing | Must be re-pointed deliberately |
| `test_status_reader_one_owner.py` | the file **exists at that exact path** with a readable `## Status:` | **No** — a rename or a header-less generated view fails it |
| `test_tool_input_paths_resolve.py` | prose `designs/…` citations must NOT be rewritten | Guards against over-eager migration |

---

## 4. The window problem, and why it decides the sequencing

The convention "a deletion writes an alias row **in the same commit**" is instructed from at
least six places (`evacuation_plan.py:515`, `test_retired_tree_apparatus.py:740`,
`test_tool_input_paths_resolve.py:224`, `ci_claude_workflow_paths.py:55`, CLAUDE.md §3 rows).
Jordan's 2026-08-12 ruling — *"dead files get moved to deprecated"* (ED-IN-0171) — **increases
the write rate on this file.**

So: after the source flips to generated data, a session following those instructions writes its
row into the **rendered view**, and the next regeneration deletes it. **A lost row degrades
silently** — it surfaces only if some live citation happens to name the orphaned path, and the
`>100/≥10` floor detects total loss, *not* single-row loss.

Three consequences, all binding:
1. The rendered-view drift `--check` must be **blocking from the flip commit itself**, not added
   after.
2. **Every "write a row here" instruction site updates in the flip commit.**
3. The file is append-hot at unpredictable times, so a long-lived migration branch carries
   standing merge-conflict exposure — the same pressure that forced the HANDOFF and ledger
   lane-splits.

---

## 5. The plan

**Governing shape, from the closest precedent (ED-IN-0139):** capture-with-gate FIRST, source
dies later, and the gate carries a named retirement condition. Every step below is
independently shippable and leaves `main` green.

### Phase A — consolidate the parsers, while markdown is still the source

*No format change. This is the whole risk reduction: five parsers → one.*

- **A1 · Rule the five semantics.** FORK verdict, FORK payload shape, hop count, duplicate-key
  precedence, existence test. **These are Jordan's calls, not an agent's** — each changes what a
  BLOCKING gate does. Deliverable: a decision table, nothing else. *Blocks everything after it.*
- **A2 · Make `pathres` the actual sole reader.** Port `vector_audit` and `workbench` first —
  trivial, since their local loaders exist only for root-parameterisation and
  `pathres.load_alias_map(root)` already takes a root. One shape mismatch to bridge
  (`(exact, prefix)` vs one flat dict). **Zero expected delta** — assert it.
- **A3 · Port `gen_audit`** — exact-only → prefix + FORK-aware. **Real delta**: findings move
  between `moved` and `nonexistent`. Ships with the enumerated diff.
- **A4 · Port `broken_dependency_checker`** (BLOCKING). Single-hop → whatever A1 ruled.
  `test_pathres.py:109-112` already exists as the equivalence instrument — that is why it was
  written. Ships with a per-reference status diff, every delta individually accounted, in the
  `test_status_reader_one_owner` shape.
- **A5 · Port `ci_claude_workflow_paths`** (BLOCKING). Gains FORK awareness → changes DEAD
  verdicts. Its `alias_fatal` policy (`:53-67`) is **consumer semantics and must survive** — a
  unified resolver that normalises it away silently loosens or tightens a gate.
- **A6 · The recurrence guard.** A test that fails when a *new* independent parser of the source
  appears. Without it the pattern returns — it already did once: `pathres` was written as the
  owner and four parsers remain. §0.1 point 5: *if you cannot write the guard you have not
  understood the pattern.*

**Phase A is valuable on its own and can stop here.** It removes the five-way semantic
disagreement, closes the anti-fabrication hole, and leaves the file exactly as it is.

### Phase B — capture to structured data

- **B1 · Lossless capture with a positive control.** Emit YAML/JSONL from the 1,038 rows. The
  gate must prove **1,038 in / 1,038 out**, with the 116 header-less FORK rows explicitly
  counted, and a planted-omission control (ED-IN-0139's F3 lesson: a control that does not
  exercise the branch carrying the claim is decoration).
- **B2 · Carry what is actually load-bearing.** Union of machine-read fields: `old`, `new`,
  `kind` (exact / prefix / stem — currently encoded *only* by a trailing slash), `fork_ref`.
  Plus, as data rather than prose: section provenance (date, ED), the three semantic prose
  blocks, and **negative rows** (`tools/registry.py` has no alias *on purpose*).
- **B3 · Generate the markdown view from the data**, with a blocking `--check`, on the
  `export_engine_params --check` pattern.
- **B4 · Resolve the `build_incompleteness` name-coupling** — the one thing schema design cannot
  fix. Either keep the substring in the filename or repoint that exclusion. Decide explicitly.

### Phase C — the flip

One commit, atomic: `pathres` reads the data; the view becomes generated-only; **every
row-writing instruction site is updated**; the drift `--check` goes blocking; the `## Status:`
header survives for `test_status_reader_one_owner`.

---

## 6. What I would NOT do

- **Do not start at Phase B.** Migrating the format under five disagreeing parsers converts a
  visible disagreement into an invisible one — the same error #304's A7 LEAVE list exists to
  prevent, and the same one this session already made once by folding a divergent copy.
- **Do not clean the data during the capture.** The ~300 dead-target rows, the garbage row, the
  count mismatch and the duplicates are *findings*, not migration work. Capture them faithfully,
  then fix them as their own change with their own controls. Flattening the multi-hop chains at
  migration time would bake today's disk state into the data permanently.
- **Do not let this branch run long.** The file is append-hot and the write rate is about to rise.

---

## 7. Honest limits of this plan

- **The three lenses were read-only and could not execute anything.** No claim here has been
  verified by running a parser against a modified file. The row counts, the five-way FORK
  divergence and the 116-row header split are all read-off-the-page findings — strong, but the
  first executable step should be a harness that *reproduces* the five-way divergence, because
  that is the claim the whole plan rests on.
- **One lens could not verify Jordan's "dead files" ruling** and correctly flagged it
  UNVERIFIABLE-BY-ME — it was given in session and is now registered as ED-IN-0171. The
  increased-write-rate argument in §4 depends on it.
- **Effort is not estimated.** Phase A is five ports, two of them touching blocking gates, each
  needing its own expected-delta artifact. That is the bulk of the work and it is deliberately
  front-loaded, because it is the part that reduces risk rather than spending it.
