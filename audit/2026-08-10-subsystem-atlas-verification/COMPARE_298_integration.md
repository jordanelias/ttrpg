# A (#298 contract/key indexes) × B (flow skeletons) — integration assessment

Branch `claude/game-subsystem-skeletons-16cm23` @ `b24a1e9` (merge of `d36498f` #298 into B's `0b7bf8a`).
Read in full: `tools/build_contract_index.py`, `tests/valoria/test_contract_index.py`,
`tests/valoria/test_flow_skeletons.py`, `systems/_architecture/subsystem_flow_skeletons_v1.md`,
`references/CONTRACT_INDEX.md`, and the `npcs`/`combat`/`social_contest` skeletons.

## 0. Staleness check — A is NOT stale. No integration defect of that kind.

```
$ python3 tools/build_contract_index.py --check
[contract-index] both indexes are current                       # exit 0
$ python3 tools/build_key_graph.py --check                      # exit 0 (transitive input also fresh)
$ python3 -m pytest tests/valoria/test_contract_index.py tests/valoria/test_flow_skeletons.py -q
83 passed in 0.83s
```

`--check` exists (`main()`, `tools/build_contract_index.py:591-598`: rebuild in memory, byte-compare
against the committed file) and is itself pinned by `test_indexes_are_current`.

**Why B could not have staled A, structurally:** A's entire input set is
`references/{key_graph.json,module_contracts.yaml,wiring_manifest.yaml,canonical_sources.yaml}`,
`systems/_architecture/key_type_registry_v30.md`, and the adjudicator script. B changed none of
them — `git diff --name-only origin/main...HEAD` is 15 skeletons + the format spec + `CURRENT.md` +
generated glossary + `id_reservations.yaml` + `test_register.json` + `editorial_ledger_in.jsonl` +
`HANDOFF_IN.md`. The 15 new docs are invisible to A by design. **A is a registry renderer; it does
not see the doc tree.** So the two are decoupled in the A-goes-stale direction — but *not* in the
other direction (§2 below), which is the asymmetry that matters.

## 1. Rule duplication between the guards — NO. Verdict: clean.

The two guards are disjoint in surface, property, and mechanism.

| | A's guard | B's guard |
|---|---|---|
| surface | 2 generated files in `references/` | 15 hand-written docs in `systems/*/` |
| property | output == fresh rebuild; anchors resolve; nothing truncated | anchors land on their symbol in real code; sections present+ordered |
| mechanism | regenerate-and-diff | resolve `path:line symbol` against the tree |

Neither re-implements a rule the other owns, and neither re-implements a `tools/` module:

- **A imports rather than re-implements**, and pins that it did: `adjudicate()` execs
  `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py` (checks A1–A12), and
  `test_adjudicator_verdicts_are_imported_not_reimplemented` fails if the rendered violation count
  ever diverges from the adjudicator's. This is §8-compliant to the letter, including the guard
  against future divergence.
- **A's guard deliberately re-implements one thing and says why.** `_slug()` duplicates the
  builder's `anchor()` with the comment "Kept independent of the builder's own `anchor()` ON
  PURPOSE: a shared helper would make both sides wrong together and the test would still pass."
  That is correct test design, not a §8 violation — §8 forbids two owners of a *rule*, and a
  guard that shares its subject's implementation asserts nothing.
- **B's anchor resolver has no existing owner.** I checked the plausible candidates:
  `tools/ci_claim_provenance_check.py` is JSONL-ledger-scoped and only checks that a
  `MEASURED-BY:` path *exists*; `tools/broken_dependency_checker.py` extracts path refs from
  `propagation_map.md` / `canonical_sources.yaml` / the ED ledgers and never reads `systems/*.md`;
  `tools/validate_ed_citations.py` is ED-scoped. Nothing in `tools/` resolves `path:line symbol`.
  The symbol-within-window check is genuinely new.
- **B's roster has one owner** (`subsystem_flow_skeletons_v1.md` §3), and
  `test_format_spec_is_the_single_owner_of_the_roster` walks `systems/` to fail on a second list.

*Minor, not a finding:* both test modules privately implement markdown heading/table extraction.
That is boilerplate, not a rule.

## 2. Content duplication — YES, and it is one-directional. B restates what A generates.

Every item below is a fact whose single owner is `references/module_contracts.yaml` (rendered live
by A) and which B copied by hand at a commit. A regenerates; B does not. These are the rot spots.

1. **The `**Contracts:**` header line, all 15 files.** B hand-names the module contracts per
   subsystem. A already renders the module↔subsystem↔doc mapping (the `subsystem` / `design doc`
   columns of "Modules with no home", plus the per-module `### <module>` detail block).
   **It is already wrong in one file:** `systems/social_contest/` declares
   `**Contracts:** systems.social_contest.sim.contest (kernel package), …parliamentary_vote,
   …parliamentary_stay` — those are Python module paths, not contracts. The real contract
   `social_contest` exists in A (`### social_contest`: scales `scene`, resolver `dice_pool`,
   authority `code`, build `gated`, 1 IN / 4 OUT, doc `systems/social_contest/social_contest_v30.md`)
   and that skeleton never mentions `module_contracts.yaml` at all (`grep -c` → 0). Measured
   coverage: of A's 27 modules, **19 are named by some skeleton header and 8 are not** —
   `audit, campaign_architecture, clock_registry, domain_actions, scenario_authoring, scene_slate,
   scene_timer, social_contest`. Seven of those are A's own "no home" rows and legitimately have no
   subsystem to trace; `social_contest` is a plain miss. Several other headers are hedged prose
   inside the contract slot ("`piety_track` (conviction), no…", "`fieldwork_knots` (only…",
   "`engine_clock` (declared in…"), which is unverifiable by either guard.
2. **37 line-number anchors into `references/module_contracts.yaml`, across 13 of 15 skeletons.**
   e.g. `references/module_contracts.yaml:126-141 npc_behavior`,
   `references/module_contracts.yaml:1018-1021`, `…:341 threadwork`. Each pins a line in a
   1,108-line authored YAML that A renders stably by *name* with a durable
   `CONTRACT_INDEX.md#<module>` anchor. Any insertion above a cited line shifts all of them. B's
   guard will catch that loudly (good), but the resulting churn is pure re-verification of facts
   that never changed.
3. **§7 rows restating declared contract shape.** `npcs` §7 row 3 restates `npc_behavior`'s whole
   declared `consumes`/`emits`/`state`/`gates` shape against `sim_module: none`, plus `npc_memory`'s
   `doc: null, sim_module: none` — A renders all of it (`sim module: — none`, `authority: prose`,
   the 31-row IN table). `combat` §7 row 1 restates `personal_combat`'s declared emit/consume
   triples. `npcs` §7 also carries `A6`-shaped cross-scale observations that A's review queue
   already enumerates as 20 adjudicator violations.
4. **Anchors into other churn-prone non-code surfaces:** `CURRENT.md:163` (×3 tree-wide),
   `registers/mechanics_index.yaml:<line>` (×3), `references/canonical_sources.yaml` (×2),
   `audit/**/structure_metrics.json:<line>` (×4). `CURRENT.md` is hand-reconciled and reordered
   routinely; a line anchor into it is the most fragile citation in the corpus.
5. **`**Traced at:**` is already inconsistent and unguarded** — 12 files say `6545067`, 3 say the
   full `654506799c637e83eae33377a7b0974317721b0a`, and HEAD is now `b24a1e9`. Nothing checks the
   field's format or its meaning.

**What B does NOT duplicate, and A cannot produce:** entry points and their real call sites, the
ordered S1/S2 flow with `[gate]`/`[branch]` tags, reachability (`no live trigger ever queues a
combat scene`), default-off flags (`DISPATCH_COMBAT_BRIDGE`), dead branches
(`hidden_allegiance` computed and never passed), uncalled functions, and the code home for a
subsystem whose folder holds no code. None of that is in any registry.

## 3. Should B cite A? — Yes, for the declared half only.

**Replace with a citation:**

- The `**Contracts:**` header slot becomes a link per module —
  `[`npc_behavior`](../../references/CONTRACT_INDEX.md#npc_behavior)` — and carries the module
  name and nothing else. No parenthetical hedges, no `module_contracts.yaml:<line>`. A owns
  scales / resolver / doc / sim_module / authority / build status; B must not restate any of them.
- The 37 `module_contracts.yaml:<line>` anchors become `CONTRACT_INDEX.md#<module>` links wherever
  the fact cited is "what the contract declares". Both of A's guards keep those anchors live
  (`test_every_anchor_link_resolves`, `test_every_contract_module_and_key_type_is_rendered`), so
  the link is strictly better-guarded than the line number it replaces.
- Key-level claims cite `KEY_INDEX.md#<keytype>` rather than re-listing producers/consumers.

**B must keep** (A cannot produce any of it): every `path:line symbol` anchor into *code*; §1–§6
entirely; and the §7 rows' **evidence** — the code-side half of a divergence. The right §7 shape is
"A declares X ([link]); the traced code does Y (`code.py:NNN sym`); therefore divergence", where B
owns only the second clause. That keeps §7's job (recording disagreement) while removing its copy
of A's side of the disagreement.

## 4. Direction of authority — currently unstated by both. B wins on as-built; A wins on declared.

Neither artifact names the other: `grep flow_skeleton references/CONTRACT_INDEX.md` → 0, and
`grep 'CONTRACT_INDEX\|KEY_INDEX' systems/*/*_flow_skeleton_v1.md` → none. B's spec §5 gets close
("A skeleton traces what the code does; §7 records where the two disagree. Neither edits the
other") but names `module_contracts.yaml`, i.e. A's *source*, not A. A gets close via its derived
`authority` column (code > prose, Jordan 2026-08-02) but that ranks *sources*, not artifacts.

The honest precedence is **split, and each is authoritative only within its half**:

- On *what the engine is declared to do* — keys, edges, scales, resolver, build status — **A wins
  unconditionally**, because A is regenerated from the authored registries and B is a snapshot.
- On *what the code actually does at the traced commit* — **B wins**, because A never opens a `.py`
  file; A's `authority: code` only means a declared `sim_module` path resolves on disk.
- When they disagree about a module, that disagreement **is the finding** and belongs in B §7.

**Recommended sentence for A** (in `BANNER` or the header prose of `render_modules`, so it is
generated, not hand-added):

> This index renders what the contracts **declare**; for what the code as-built actually does in a
> subsystem, read that subsystem's `systems/<x>/<x>_flow_skeleton_v1.md`, which wins on any
> question of executed behaviour.

**Recommended sentence for B** (in the spec's §5 table row for the contracts, inherited by every
skeleton's header block):

> `references/CONTRACT_INDEX.md` is the always-fresh rendering of the declared contracts and wins
> on every declared fact (keys, edges, scales, resolver, build status); this skeleton wins only on
> traced code behaviour at the commit in `**Traced at:**`, and restates no declared fact it can
> link to instead.

## 5. Redundant? — No. Genuinely complementary, on an axis neither currently names.

Neither subsumes the other, and the test is cheap: A cannot answer "is this branch ever reached?"
(it has never opened a `.py` file); B cannot answer "who else declares they consume
`state.succession`?" (it traces one subsystem at a time and does not join across the registry).
Their overlap is confined to the §2 restatements, which are removable without loss.

**The one sentence a newcomer needs:**

> `CONTRACT_INDEX.md`/`KEY_INDEX.md` are the *declared* engine — regenerated from the registries,
> always current, never opened a source file; the `*_flow_skeleton_v1.md` files are the *as-built*
> engine — hand-traced from code at a named commit, guarded against rot by anchors that must land
> on their symbols. Read A for what the system is supposed to be, B for what it currently is, and
> B's §7 for the list of places those differ.

The deeper point: A's freshness is *free* (regenerate) and B's is *expensive* (re-trace), so every
declared fact B copies imports A's subject matter at B's maintenance cost with none of A's
freshness guarantee. That is the whole of the integration defect, and it is fixed by citation.

## Recommended edits to B (not applied)

1. **`systems/social_contest/social_contest_flow_skeleton_v1.md`** — the header names Python
   modules where contracts belong. Set `**Contracts:** social_contest` and add the §7 divergence
   rows its contract warrants (A: authority `code`, build `gated`, 1 IN / 4 OUT).
2. **All 15 headers** — reduce the `**Contracts:**` slot to bare module names linked to
   `references/CONTRACT_INDEX.md#<module>`; strip the hedging parentheticals in `_architecture`,
   `characters`, `fieldwork`, `world`, and the inline `module_contracts.yaml:341` in `threadwork`.
   `ui`'s "none found" is correct — keep it, ideally as "no module contract (verified against
   CONTRACT_INDEX.md)".
3. **Replace the 37 `references/module_contracts.yaml:<line>` anchors** with
   `CONTRACT_INDEX.md#<module>` links wherever the cited fact is a declaration; keep a line anchor
   only where the *wording* of the YAML (e.g. a gap note's text) is the evidence.
4. **Rewrite §7 divergence rows** to the two-clause form: link A for the declared side, keep a code
   anchor for the traced side. Concretely in `npcs` (rows 3, 8) and `combat` (row 1).
5. **Re-home the churny non-code anchors** — `CURRENT.md:163`, the 3 `mechanics_index.yaml` line
   anchors, the 2 `canonical_sources.yaml` ones. Cite by row/key name, not line.
6. **Normalize `**Traced at:**` to a full 40-char sha** across all 15 (12 are short, 3 are full)
   and add a guard asserting the format — a snapshot claim whose commit field is unvalidated is
   the one claim in the format nothing checks.
7. **Add the §4 precedence sentence** to `subsystem_flow_skeletons_v1.md` §5 and to the per-file
   header template, so every skeleton carries it.
8. **Optional, cheap, high value:** extend `tests/valoria/test_flow_skeletons.py` with a check that
   every module name in a `**Contracts:**` header exists as a `### <module>` heading in
   `CONTRACT_INDEX.md`. That converts the class of defect found in item 1 from invisible to
   blocking, and it is the guard §0.1 point 5 asks for. Note it makes B depend on A's output — the
   right direction, since A is the regenerated side.
9. **Do not** add coverage of A's 7 homeless modules (`audit`, `domain_actions`, `scene_slate`, …)
   to B. They have no subsystem folder to trace; A's "Modules with no home" section already owns
   that fact and B claiming them would recreate the duplication this assessment recommends removing.
