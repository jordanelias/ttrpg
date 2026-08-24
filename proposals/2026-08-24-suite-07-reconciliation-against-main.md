# Suite 07 — Reconciliation Against `main`

**Status:** RECONCILIATION RECORD. Written 2026-08-24, after rebasing the session branch onto
`origin/main` at `dcf38ef`.

**Why this exists rather than a rewrite.** Suites 00–06 are a dated measurement of the tree as it
stood on 2026-08-23. Between that measurement and this rebase, `main` advanced nine commits, deleted
303 files, and landed three Jordan rulings — and **fixed two of the things the suite reports as
defects**. Editing the originals to hide that would destroy the only useful property a measurement
has: a timestamp. So the suite stands as taken, and this document says exactly what moved under it.

Read this **before** acting on anything in Suites 00–06.

---

## §1 What the rebase did

`git rebase origin/main`, 19 commits replayed, zero lost.

**Conflicts, and how they were resolved.** Every conflict was the same class: `main` deleted a
**generated** artifact that my commits had regenerated.

| Deleted on `main` | Resolution |
|---|---|
| `references/glossary/` — all 21 files **plus `tools/build_glossary.py`** | Accept the deletion. The generator is gone; the outputs cannot be authoritative. |
| `references/ENGINE_ATLAS.md`, `references/engine_atlas.json` | Accept the deletion. The atlas now lives at `systems/_architecture/engine_atlas_v1.md` via `tools/build_engine_atlas.py`. |

Nothing authored was touched. A guard was used while replaying so that only those paths could
auto-resolve; any other conflict would have stopped for manual review. None occurred.

**Side effect worth recording:** the one test that failed at the end of the 2026-08-23 session —
`test_build_glossary.py::test_committed_output_matches_a_fresh_build` — is resolved by the rebase,
because `main` deleted the generator and the test with it. It was correctly reported then as
pre-existing and not caused by the suite.

**The branch is now purely additive:** 19 proposal documents, one edit to an existing proposal, one
ledger line. No generated-file churn.

---

## §2 Two findings are now HISTORICAL — `main` fixed them

### §2.1 The conviction roster — FIXED

**Suite 02 §2.3 and Suite 03 §2.1/§2.2 describe a defect that no longer exists.**

`main` gave Convictions one owner: `references/descriptor_registry.yaml:conviction_roster` →
`tools/export_descriptors.py` (blocking `--check`) → `engine/engine_params/descriptors.json` →
`engine.substrate.descriptors.CONVICTIONS`, which `conviction.py` and `npe.py` now read instead of
retyping. Re-measured on the rebased tree:

```
engine.substrate.descriptors.CONVICTIONS   13
systems.characters.sim.conviction.CONVICTIONS   13   (identical)

registry names used across 46 characters   13
used but NOT in the code roster             []      ← was 7
in code but never used                      []      ← was 3
```

The seven silent no-ops are gone, the three orphaned code names are gone, and the twelve characters
who could not be scarred on anything can now be scarred. `resolve_conviction` **raises** on an
unknown name instead of returning `magnitude=0`, so the silent-failure mode is closed by
construction rather than by discipline.

`knots.py` now passes `'Honor'` rather than `'Loyalty'`, which closes Suite 03 §2.2 — including the
test that could not observe its own failure. `main` replaced it with a falsifier that asserts the
scar **store** moved, and added an AST sweep (`test_conviction_roster_single_owner.py`) that fails on
recurrence.

**What survives from the original finding:** the diagnosis and its consequences were right, and the
fix `main` chose is the one Suite 03 §9's S1 argued for — a single owner, because no roster primitive
existed. Nothing about the analysis needs retracting; it is simply done.

### §2.2 Ruling A — the engine port LANDED, the design question did not

**Suite 01 §1 describes a removal that has since been executed differently and better.**

`main` ported the canon engine (`tests/sim/mass_battle/`, 11,342 lines) **over the top of** Tree A
rather than deleting Tree A and repointing the importer. `systems/mass_battle/sim/` now holds
`orchestration.py`, `core/`, `hierarchy/`, `percell.py`, `geometry.py`, `troop_types/`, `equipment/`
and the rest. `units.py` is gone. `massbattle.py` survives at **146 lines** — 1,905 before — reduced
to the strategic→tactical adapter, so `systems/factions/sim/faction_action.py:462` still resolves and
the campaign never broke at import.

That approach sidesteps four of the five guards Suite 01 §1.3 enumerated, because the module path
never disappeared. The guard analysis was correct for the deletion strategy it analysed; `main` chose
a different strategy.

**What survives, and it is the important half.** Suite 04 Q2 asked *"what is a strategic army, in
cells?"* and called it the blocker. `main`'s own commit reaches the same conclusion independently,
in the adapter's docstring:

> *"the faction → Unit construction below is still the old engine's minimum-viable default … the
> canon engine can express far more than that — troop types, equipment, formations, multi-subunit
> hierarchies, orders of battle. Every one of those is a design question about what a faction's army
> IS at the strategic scale, and none of them is answered by porting an engine."*

**Q2 is unchanged and is now the sole remaining blocker on mass battle.** The engine arrived; the
army did not.

---

## §3 Three rulings that change the FRAME, not the measurements

Jordan ruled on 2026-08-24, after the suite was written. All three bear on how it should be read.

### §3.1 §0.05 — code is the mechanism, prose is reference

> *"whatever mechanisms we have that rely on prose are worthless. we rely on code ONLY for the game
> work. our design documents in .MD are reference and information only."*

The test: **if this document were deleted, would the game behave differently?**

**This resolves a whole class of the suite's findings outright.** Every doc-versus-doc disagreement
is answered by the code, and is a reference-quality issue rather than a design conflict:

| Finding | Under §0.05 |
|---|---|
| Suite 01 §3.2 / Suite 03 V10 — `fieldwork_v30.md:475` vs `knots_v30.md:76` disagree on the Knot pool | **Answered.** `knots.py` is the formula. The doc is stale reference; fix it, do not adjudicate it. |
| Suite 01 §3.2 — `fieldwork_v30.md:477-478` states absolute-net degree bands against the ruled margin ladder | **Answered.** `dice_engine.degree_from_net` is the ladder. |
| Suite 03 §5.1 Church threshold, §5.2 Gap scale — already overturned | Unchanged; §0.05 makes the class moot anyway. |
| Suite 03 §6 — the voice doc's `status: provisional` in `canonical_sources.yaml` | **Demoted.** A status field on a reference document is not a mechanism. The real finding — *no code cites the voice canon* — stands, and under §0.05 it is the only part that was ever load-bearing. |

**And it sharpens Ruling C.** Suite 01 §3.4 recommended the pool document be a document. Under §0.05 a
document of formulas is *reference by definition* and cannot be the owner. **Q5 should be re-asked:
the single owner has to be typed data with an exporter and a blocking round-trip — the shape `main`
just used for Convictions — not a markdown file that subsystems are asked to honour.** That is a
material change to what Ruling C means, and it is the most consequential line in this document.

### §3.2 `needs_jordan` is not a parking space

Five tests now precede any escalation: superseded · irrelevant · answered by a design document ·
answered by precedent · answered by architecture.

`main` then triaged the queue adversarially: **154 rows on effective status, of which 31 are genuine
Jordan decisions (20%), 34 are work needing no ruling, and 89 are not decisions at all.** Of the 89,
20 die to §0.05 alone as doc-versus-doc value disagreements.

**Suite 06 §5's figures (254 open / 110 `needs_jordan`) are superseded.** My filter and `main`'s
differ, and `main`'s is the one attached to a ruling. What survives from Suite 06 §5 is the *shape*
finding, which `main`'s triage independently confirms: the queue is not stale — 96 of my 110 were
July or August, and `main` found 58% were never decisions rather than old ones. Both readings agree
the problem is queue hygiene, not age.

**Suite 00 §3 and Suite 04 §6's seven questions should be re-run through the five tests.** My reading
of how they fare — but Jordan's call, not mine:

| | Survives the five tests? |
|---|---|
| **Q1** what is a character at runtime | **Yes** — a design fork with two defensible answers, blocking five chains |
| **Q2** what is a strategic army in cells | **Yes** — and `main`'s adapter docstring says so independently (§2.2) |
| Q3 chronicle home + callback output channel | **Probably architecture** — answerable by the Key-bus design without Jordan |
| Q4 should Binding be harder than Weaving | **Yes** — genuine design fork, and §4.2 below shows Ob cannot substitute |
| Q5 pool document: record or normalise | **Re-ask under §0.05** — "document" is no longer an available answer (§3.1) |
| Q6 ratify the belief layer | **Yes** — authorial |
| Q7 author `engine_clock` | **Work, not a ruling** — a named target with no design fork |

That is seven reduced to roughly four.

### §3.3 Markdown may no longer be swept

`.claude/settings.json` now runs `tools/hook_md_sweep_guard.py` on every `Grep`/`Glob`. Broad
markdown globs and unscoped repo-wide greps are blocked; `Read` of a named file and code-scoped
searches are permitted. The allowlist is **derived** — `triage_work_items.machine_read_inputs()`
scans code for read contexts, so a `.md` becomes searchable exactly when code reads it.

**Method note for Suite 06 §1.** The suite's stage-1 discipline was "parse, never pattern-match,"
which this hook now enforces mechanically for the markdown half. Suites 02–04's *design-doc* claims
were produced by reading named files, which remains permitted. But under §0.05 those claims are
claims about reference material, and their weight should be discounted accordingly — the code claims
are the load-bearing ones, and they are the ones §4 re-verified.

---

## §4 What still stands — re-measured on the rebased tree

Every claim below was re-run against `main` at `dcf38ef`, not carried forward.

### §4.1 Verified unchanged

| Claim | Re-measured |
|---|---|
| **`world.npcs` is empty; nothing loads the character registry** | `world.npcs == {}`. Readers of `references/npc_registry.yaml`: **one** — `tests/valoria/test_references_yaml_parse.py`. **Stronger than reported:** `tools/observability/build_decisions.py` was culled, so the documentation generator is gone too. |
| **T15 / T16 mirror holes** | 16 territories, 37 settlements, 16 provinces. No settlement in `T15`; no territory for `T16`. Unchanged. |
| **Treaty system wholly inert** | AST sweep for `process_treaty_expirations` / `register_treaty` / `get_active_treaties`: **no callers anywhere.** |
| **Settlement ledger unreachable** | AST sweep for `add_tag` / `has_tag` / `tags`: **no callers anywhere**, tests included. |
| **`[ASSUMPTION]` resolver count** | 27 modules · **11** `[ASSUMPTION]` resolvers (11 distinct) · **9** `doc: null`. Suite 03 §7.1 holds exactly: CLAUDE.md's `11/27` is right; only the `10/27 → 9/27` half of the queued edit should land. |
| **TN: `roll_pool` is TN-blind** | `dice_engine.py:75-84` unchanged — `tn` stored, never read. |
| **TN: the non-7 declarations** | `operations.py:47-50` unchanged — `TN_STANDARD=7`, `TN_BINDING=8`, `TN_POP=8`, `TN_POP_BINDING=9`. **All of Suite 01 §2 stands.** |
| **Articulation omits both emitted types** | `_TRIGGER_TYPE_IDS` is 13 entries and contains neither `scene.contest_resolved` nor `scene.battle_concluded`. |

### §4.2 Independently confirmed by `main`, and sharpened

`main` built `tools/contract_runtime_conformance.py` — the first instrument in this tree that asks
the **engine** what it emits rather than comparing declarations to declarations. Seeded, n=2:

```
EMITS      declared 60   observed  3   matched 0
CONSUMES   declared 82   observed 13   matched 0
397 emissions from exactly THREE call sites
   217 x scene.contest_resolved   engine/cross_scale/echo_transport.py::emit_scene_echo
   175 x scene.battle_concluded   systems/factions/sim/faction_action.py::_emit_battle_concluded
```

This is **better evidence than Suite 04 §5's structural reading**, and it makes the finding much
worse than reported: not merely that two emitted types are missing from one roster, but that **zero
of sixty declared edges match anything the engine actually does.**

It also corrects my attribution. Suite 04 §5 named `parliamentary_bridge.py:212` as the
`scene.contest_resolved` emitter; the runtime says `echo_transport.py::emit_scene_echo`. Where a
structural read and a runtime measurement disagree, the measurement wins.

### §4.3 The one design consequence nothing has answered

Suite 01 §2.4 stands untouched and is worth restating because Q4 depends on it. A TN step is
**pool-proportional** (per-die mean 0.40 at TN 7, 0.30 at TN 8, so the mean net falls by 0.10 × N);
an Ob step is flat. **There is no constant Ob increment that reproduces a TN increment across pool
sizes** — a Spirit-7 practitioner and a Spirit-2 novice would need +1.8 and +0.7 respectively.

Collapsing TN to 7 therefore removes a difficulty lever that scaled with competence, and it cannot be
replaced by a flat Ob bump. Since `roll_pool` has always been TN-blind, that lever has in fact never
worked. The ruling makes the code honest; whether Binding *should* be harder than Weaving, and on
which axis, is Q4.

---

## §5 Citation rot

Twelve cited paths were deleted by `main`'s culling. Line numbers were checked mechanically: **zero
citations point past end-of-file**, so no quoted line has silently shifted onto different code.

| Cited path | Status |
|---|---|
| `systems/mass_battle/sim/units.py` | **Deleted** — the engine port (§2.2). Suite 01's pool formula 7 has no home; the mass-battle pool now lives in the ported engine. |
| `engine/autoload/echo_transport.py` | **Wrong path in Suite 04** — it is and was `engine/cross_scale/echo_transport.py`. My error, not a move. |
| `systems/factions/sim/faction_action.py:452` | Now **`:462`** — line drift only; the import is unchanged. |
| `tools/review_core.py`, `tools/observability/build_decisions.py` | Culled. Suite 01 §1.3's bookkeeping rows are moot. |
| `references/key_graph.json`, `registers/patch_register_index.md`, `systems/_architecture/conviction_axis_matrix_v30.md`, `systems/npcs/faction_canon_v30.md` | Culled. The claims resting on them (Suite 03 §5.2 provenance, Suite 04 §3.5's dual-Status line) are now unverifiable in-tree and should be treated as historical. |
| `tests/valoria/test_knots_ed912.py` | **Moved** to `engine/tests/` and rewritten as a real falsifier (§2.1). |
| `audit/2026-08-11-divergence-audit/02_remediation_plan.md` | Culled. **Suite 01 §2.3(b)'s warning is discharged** — the docket that recommended the opposite of Ruling B no longer exists. |
| `tests/valoria/test_tn_single_owner.py` | Still does not exist. Suite 01 reported it as planned-not-built; unchanged. |
| `tests/sim/sim_mb_06_v22.py` | Culled with the old engine's provenance trail. |

Suite 05 is unaffected — its external precedent claims are not about this tree.

---

## §6 The standing position after the rebase

**Superseded — do not act on:** the conviction roster defect (§2.1); Tree A's deletion plan
(§2.2); Suite 06 §5's queue figures (§3.2); Suite 01 §3.4's recommendation that the pool owner be a
document (§3.1).

**Standing and re-measured:** the zero population and its five blocked chains; T15/T16; the treaty,
ledger, Mandate and succession orphans; the whole TN analysis; the `[ASSUMPTION]` count and its
correction-to-a-correction; the articulation roster gap, now much sharper as 0-of-60.

**The live questions, reduced from seven to about four:** Q1 what a character is at runtime · Q2 what
a strategic army is in cells · Q4 whether Binding stays harder than Weaving and on which axis ·
Q5 re-asked as *typed data with an exporter*, not a document · plus Q6 as authorial ratification.
Q3 and Q7 look like architecture and work respectively, and under §0.05's five tests should not be
sitting in Jordan's queue.

**And one thing this rebase demonstrated about the method.** Two of the suite's findings were fixed
by another session within a day of being written, one of them by exactly the mechanism Suite 03 §9
argued for. The measurements were right and the diagnosis held. What did not hold was the *framing* —
the pool document, the deletion strategy, the queue arithmetic — all of which assumed a doctrine that
changed the next morning. **A measurement dated and re-verifiable survived that; a recommendation
written as though it were permanent did not.**

---

_Rebased and re-measured 2026-08-24 against `origin/main` at `dcf38ef`. Every §4 figure re-derived
from the rebased working tree. `main`'s runtime-conformance numbers in §4.2 are quoted from its own
commit, not independently re-run. Safety ref for the pre-rebase state:
`pre-rebase-backup-2026-08-24` at `1e41421`._
