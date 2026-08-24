# Completing the cull, the centralization, and the doc-vs-code conflicts

## Status: PROPOSED (Jordan-requested, 2026-08-24). Ratifies on merge per CLAUDE.md §2.

> **What this is.** Three read-only Fable-5 planners produced completion plans for the three open
> programmes; a fourth, independent Fable-5 antagonist attacked all three against the tree; the
> orchestrator re-verified every load-bearing claim by hand before writing it down. **Refuted claims
> are recorded as refuted, not silently dropped** — the refutations are the most valuable output
> here, and a later session needs to know which attractive-looking plans were killed and why.
>
> Working notes: `scratchpad/closeout/agonist_emit_reachability.md`, `scratchpad/closeout/reconciliation.md`.

---

## 0. What the relay killed — read this before executing anything

Four plausible, well-argued recommendations died under attack. Each would have cost real work.

| killed recommendation | who proposed | why it died |
|---|---|---|
| **"Wire `scene.accord_echo` first — zero new mechanics"** | Planner B | `echo_transport.py:278-283` states the target settlement stays *"a computed-but-unapplied, explicitly recorded outcome **rather than a guessed settlement**"*, and the `scene_type`→outcome fallback was **deliberately deleted** (`:29-33`). Wiring it needs **two invented payload fields at aggregate scale** — the exact `mechanical.mission_shift` trap. It would also trip the UNDECLARED_TYPE floor, since no contract declares this type on either side. |
| **"Cull `test_vacuous_assertion_check.py`"** | an earlier critic; **I relayed it into `error-regions-v1.md` R11-D** | Contradicts a standing Jordan ruling recorded verbatim at `.github/workflows/valoria-ci.yml:246-250`. Culling-plan §5.6 never scheduled it for deletion — it *escalated* it, and the ruling came back KEEP. Corrected in `error-regions-v1.md` at commit `058cd84`. |
| **"A hold marker in CODE outranks any ledger status field"** | Planner C | No surface states such a rank rule, and it is not needed: `editorial_ledger_pc.jsonl:7` shows ED-PC-0016 already carries `needs_jordan: true` **alongside** `status: ratified`. The framing that a ratified row hid a live question elides the flag that was there all along. Keep the *practice* (check the code), drop the *doctrine*. |
| **"The game currently plays an un-ratified Knot Pool formula"** | **my own handoff, repeated to Jordan** | `form_knot` has no campaign call (`mc_v18.py:204-217`, OI-07). The **oracle** plays the wrong formula; the campaign plays none. Still a real defect — the oracle is what the Godot port validates against — but not the live-play claim. |

**And one recommendation the relay restored.** My agonist finding — *no emit edge is both cleanly
emittable and campaign-reachable* — was refuted by Planner B (which found a sixth candidate I had not
enumerated) and then **restored by the antagonist**, which showed B's candidate is not emittable
without invention. The finding stands, now with six candidates checked instead of five.

---

## PART I — COMPLETING THE CULL

### I.0 Corrections to the plan of record. Do not execute from the ratified text.

1. **The method paragraph is unusable.** `culling-plan-v1.md:240` says *"tag, push the tag"*.
   `restructure_ledger.md:1250-1255` records that **tag pushes are refused by this environment's
   proxy**; the executed precedent is an **on-origin-main ref** (`c9b0a86`), chosen because it
   survives squash-merge. Use `REF=$(git rev-parse origin/main)`.
2. **The counts in circulation are wrong in both directions.** `audit/` globs to 231 files, but one
   is an untracked `__pycache__` artifact — **230 tracked**. And the frequently-repeated "16 of 17
   units already forked" is wrong: the plan's heading says 17 while it **enumerates 18**; the ledger
   shows **17 at `FORK:c9b0a86`**, with `audit/2026-08-11-code-leanness/` the deliberate exemption.
   True statement: **17 of 18 went; 1 is exempt.**
3. **`audit/2026-08-11-code-leanness/` is exempt for two independent reasons**
   (`restructure_ledger.md:1257-1261`): `duplication_census.py` is named by `MEASURED-BY:` in ledger
   rows and `ci_claim_provenance_check` tests bare path existence (so a `FORK:` row does **not** save
   it), and `test_audit_plan_ids_are_allocated.py:245` opens `01_plan.md` unconditionally. Any S7
   that "just forks `audit/`" re-breaks what PR #323 stepped around.
4. **Three tests need same-commit re-expression, not one.** `test_evacuation_plan.py:293-304`
   (parity-oracle destination), `:158-166` (`assert moves` — **executing all relocations empties the
   dict and reds it**), `:146-151` (`render_scenarios.py → relocate`).
5. **A shipping-gate test is load-bearing on an `audit/` unit, and nobody's plan named it.**
   `tests/valoria/test_gauge_invariants.py:43-49` puts `audit/2026-07-22-mass-battle-stress-test` on
   `sys.path` and imports `reverse_pair_symmetry` **by bare name**. That unit is in the extract set,
   not delete-outright — but the import must be repointed in whatever commit moves it.
6. **`gauge_mb.py` has ONE importer, not two.** `evacuation_plan.py:176-182` claims two
   (`test_gauge_invariants`, `test_morale_write_sweep`); the second was ported off it on 2026-08-24
   and now only mentions it in a comment. Deleting `gauge_mb.py` produces a **collection error in one
   file**, which still reds the suite — but "stops the whole suite collecting" overstates it.

### I.1 Execution sequence

**Precondition — branch from green.** The current head is a deliberate WIP with 22 `tests/valoria`
failures. A red shipping gate cannot verify a deletion. Either land the port tail first or branch S7
from the last green `main` (`d080a36`).

**Reproduce CI for every check below** — a local green that diffs one commit is vacuous:
```sh
git fetch origin main && export GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main
```

| step | what | gate before proceeding |
|---|---|---|
| **S7.1** | Ledger/tree reconciliation: `structure_metrics.json` (on disk, cited by two live design docs, under a PARTIAL fork row) and `audit/2026-08-03-session-oddities.md` (cited by `build_fork.py:20`, absent, no row) | `broken_dependency_checker` green |
| **S7.2** | Code-home moves: parity oracle → `engine/reference/contest-groundup/`; four MB instruments → `systems/mass_battle/workbench/`. Repoint `gen_sigma_parity_goldens.py:10,102,152`. Re-express the three tests | **`gen_sigma_parity_goldens.py && git diff --exit-code engine/tests/goldens/sigma_leverage_parity.json`** — byte-identical or revert |
| **S7.3** | Churn unit (4 `.md`) → `systems/narrative/`; repoint `CURRENT.md:40`; MOVED rows; retire `AUDIT_KEEP_OVERRIDE` | `grep -c 'audit/2026-07-05' CURRENT.md` → 0; currency gate green |
| **S7.4** | Extractions per subsystem lane (list in the planner output; destinations are `systems/<sub>/reference/`) | `ci_sim_fabrication_check` under CI env — kept tests carry `[canonical: audit/…]` citations |
| **S7.5** | Fork the remainder — **ONE atomic commit**: deletions + rows + test repoints together | recompute `MIN_HEADER_DOCS`/`MIN_DOCS_WITH_IDS` **after** deletion, to ~60% of measured |
| **S7.6** | Retire the migration machinery (`evacuation_plan.py`, its test, `join_audit_workings.py`, `build_fork.py`) | strictly after S7.5 merges green — the planner is S7.5's instrument |

**Two places to verify empirically rather than trust the prose** (the planner flagged both, and they
are exactly where paper reasoning has been wrong before): whether an *exact* `FORK:` row satisfies
`ci_claim_provenance_check` for the code-leanness unit, and whether `ci_sim_fabrication_check`
accepts `[canonical: audit/…]` citations after the cited file moves. **Run the gate before trusting
the sentence.** If the first reds, leave code-leanness as the single exempt residue — that is a valid
terminal state.

### I.2 The Churn decision — settled, no Jordan input needed

`narrative_engine_design_v2_churn.md` is `RATIFIED`, referenced by `CURRENT.md:40`, and implemented
nowhere. **It moves to `systems/narrative/`; it does not fork and it is not de-ratified.** Three rules
select this and none of them is a judgement call:

- Culling plan `:220-222` already ruled *"must move, not fork"*.
- §0.05 explicitly *"does not license deleting design docs. They stay as reference."*
- Jordan's 2026-08-24 ruling: *"unbuilt mechanic proposals are kept — code that doesn't exist yet is
  still code to me."*

Under §0.2 the narrative juncture is simply **not done**, whatever its header says. Moving the doc
changes nothing about that; deleting it would delete the only spec of a ratified, sequenced layer.

### I.3 Stopping rule — falsifiable, and one of them is a tripwire on the cull itself

1. `git ls-files 'audit/*' | wc -l` → **0**, or exactly the 4 code-leanness files if the empirical
   gate forced the exemption. No other nonzero is permitted.
2. Under CI env: `pytest tests/valoria engine/tests` green, every blocking validator green,
   `broken_dependency_checker` green.
3. `gen_sigma_parity_goldens.py` regenerates its golden **byte-identically from the new home**.
4. `grep -c 'audit/' CURRENT.md` → 0.
5. Every item (S7.1–S7.6, M1, M2, 6c, 6d, triage) carries a commit SHA or a ledger row citing closure.
6. **The negative control:** `git diff origin/main --stat -- tools/ tests/valoria/` over the whole
   cull shows **no new checker or guard file**. A cull that minted a guard has re-entered §0.3's loop.

### I.4 6d is closable without a ruling — but not for the reason the ledger gives

The recorded blocker (`restructure_ledger.md:1088-1093`) says `name_collision_database.yaml` stays
separate because `build_lexicon.py` consumes it. **`build_lexicon.py` was deleted in culling wave 1.**
That reason is dead — but the file's separateness survives anyway on an independent ratification:
`vocab_store.py:47-49` cites a RATIFIED *"permanent historical snapshot, no live regeneration path"*
(ED-IN-0029 docket, OPT-AV-14), so folding it as a generated view would overturn a ruling.

**So: close 6d by folding the six foldable registries and keeping `name_collision_database.yaml`
separate on the ratification, not on the dead reason.** Also **exclude `descriptor_registry.yaml`** —
it became an exporter *source* on 2026-08-24 and folding it would churn a day-old engine-params chain.

---

## PART II — COMPLETING THE CENTRALIZATION

### II.0 The headline finding, after two rounds of attack

**There is no emit edge that is both cleanly emittable and campaign-reachable.** Six candidates
checked:

| candidate | payload buildable from existing state? | campaign-reachable? |
|---|---|---|
| `mechanical.mission_shift` | **NO** — engine has no mission concept | YES |
| `scene.accord_echo` | **NO** — needs an invented `scene_outcome` *and* a guessed `target_settlement`; the module refuses both by design | nearly |
| `state.scar_acquired` | YES but for `triggering_event_key` | **NO** — sole caller is an honest deferral |
| `meta.knot_formed` | **contract is wrong** — registry demands `Loose\|Medium\|Close`, ruled code tiers are `Distant/Close` (ED-912) | **NO** |
| `scene.combat_resolved` | partially | **NO** — `DISPATCH_COMBAT_BRIDGE` default OFF, and no `queue_scene("combat")` site exists |
| `scene.combat_felled` | seam does not expose it (PC-lane boundary) | **NO** |

**Therefore the emit-side gap is not a wiring backlog.** It sits downstream of two different things:

- **Reachability** — the modules that could emit cleanly are not reached by the campaign. Each is a
  separately-ruled deferral (`world.knots`, `world.npcs`, the combat bridge), not a chore.
- **Missing state / wrong contract** — the reachable module declares a Key the engine cannot build,
  and one candidate's registry entry contradicts a ruling.

**Do not emit any of these to move `observed` from 3 to 4.** A Key emitted with invented payload
moves the number and makes the instrument lie — optimising the measurement instead of the thing.

### II.1 What to do instead, in order

1. **Registry hygiene first (session).** Fix `meta.knot_formed`'s tier vocabulary to ED-912's
   `Distant|Close` in `key_type_registry_v30.md`, re-export `key_types.json`. Note the stale roster
   has a second surface: `fieldwork_editorial.md:56` still lists "Close 5 / Medium 2 / Loose 1".
   Declare or strike `mechanical.mission_shift`'s emit edge.
2. **Declare the two undeclared types** (`scene.accord_echo`, `meta.cascade_cluster_event`) in
   `module_contracts.yaml`, re-export, **then wire `contract_runtime_conformance.py --check` into CI**.
   Today it is wired nowhere — under §0.05 an unwired instrument is not a mechanism.
3. **The `Faction.adjust` emit spine (session).** 30 of 31 call sites bypass the bus. **One Key per
   game *event*, not per arithmetic write** — the live precedent already has this shape
   (`echo_transport.py:454-457`), and the tree already ruled the principle: *"a request for a computed
   answer stays a call; an announcement that something HAPPENED is a Key."* First migration is
   pre-identified: `faction_action.py:485-489` says the loser-Legitimacy write "belongs to
   faction_state reacting to this emission." Attach it as `apply=` on the already-firing
   `scene.battle_concluded`. This moves write timing to the accounting boundary — a §0.1 pt 1
   read/write asymmetry hazard — so extend the existing `.adjust(` census in
   `test_faction_l_reconstruction.py:140` into a shrink-only ratchet rather than minting a new guard.
4. **Read side, parallelizable:** migrate the 10 remaining `module_contracts.yaml` parsers onto the
   cooked artifact; cook the 13×4 conviction-axis matrix (its first consumer is already written and
   waiting — `npe.py:314-323` says the uniform draw is a placeholder "until it is cooked").
5. **The constants (255 uncited of 420).** §0.05 gives exactly two legal homes: a typed artifact
   behind an exporter, or a single Python owner. **Per-subsystem `config.py` single owners**,
   following the combat precedent — *not* one bulk exporter, which reproduces `params_tables.yaml`,
   a capture nobody reads.
   *Instrument note:* the count comes from `tools/export_sim_params.py:244-246`
   (`citation_coverage`). §0.05's "321" predates the mass-battle port.

### II.2 Definition of done — and why the obvious target is wrong

**`declared == observed` is the WRONG target**, for three verified reasons:

1. 29 edges belong to modules with no implementation path — an authoring backlog, unobservable.
2. **A centralized carrier is scored `ownership_mismatch` forever.** The instrument says so itself:
   acting on that label as a defect *"would decentralize the hub"*. Driving it to zero would
   **dismantle the architecture Jordan asked for.**
3. `observed` is seed-conditional — `da.public_governance` is a real emitter that dropped to zero at
   seed 42 after the MB port.

**The right DONE**, as numbers from the instrument:
- `undeclared_type == 0` on both sides **and `--check` wired as a blocking CI job**.
- `unclaimed_emitters == {}` — every emitting file is claimed by a contract path.
- Every `declared_only` edge falls in the `unobservable` bucket (the rest wired or struck).
- Every `ownership_mismatch` names a **declared carrier** — add a `carrier:` field to the registry so
  the triage partitions into hub (fine) and true mismatch (must be 0).
- Read-side mirror: `AUTHORED_PARSERS['module_contracts.yaml']` shrunk to the exporter alone.

---

## PART III — RESOLVING DOC-VS-CODE

### III.1 The decision procedure

Classify first. **§0.05 tells you which surface is the mechanism; it does not tell you which value
was decided last.**

- **A — doc vs code, code implements *a* value.** Does either side trace to a dated ruling? Doc's
  value is later → **fix the CODE** (§0.05: *"resolved by deciding and then CHANGING THE CODE"*).
  Code traces and doc is stale → fix the doc. Neither traces → code stands, doc corrected.
- **B — doc vs doc, code implements one.** Code's side wins unless the other doc records a later ruling.
- **C — doc vs doc, code implements NEITHER.** §0.05 is silent — this is the limit a prior session got
  wrong. Run the five-test ladder over the two docs, including in-file CANONICAL/PROVISIONAL labels.
- **D — code vs code.** §0.05 cannot arbitrate. Decide on (a) reachability, (b) which side is
  maintained/canon vs self-declared `[SEED]`/stub. One side a placeholder → consolidate to a single
  owner and delete the loser in the same commit. Both claim authority, or a ratified row reserved it
  → **Jordan**.
- **E — ratified doc, no code.** Not a conflict. An unexecuted juncture (§0.2). Do not file a row.

⚠ **Do not adopt "a code hold marker outranks the ledger" as doctrine.** It is unsupported, and
unnecessary — the flag was already in the ledger. Check the code as *practice*; don't invent a rank rule.

### III.2 The seven conflicts

| # | conflict | class | resolution | whose call |
|---|---|---|---|---|
| 1 | **Knot Pool** — `knots_v30.md:37` ratifies `+3, min 5`; `knots.py:216` implements neither; the test guards prose and claims "no sim/ oracle" (false) | A | `pool = max(5, (spirit*2) + history_rel + 3)`; fix `knots_v30.md:76`; **rewrite the test to execute the oracle** | **Session** — Jordan already ruled (ED-FI-0005) |
| 2 | **ED-SC-0004 Argue pool** — two live formulas | D | Prepare the docket. Note the third option nobody spotted: ED-FI-0005's ratified shape **is the merge of the two candidates** | **Jordan** — explicitly reserved |
| 3 | **Knot-break "both partners"** — `knots_v30.md:189` vs `knots.py:317,361` single actor. Same gap covers the 4 Composure at `:186` | A | Apply to both `knot.actor_a` and `actor_b`; falsifier in `test_knots_ed912.py` | **Session** |
| 4 | **`da.*` "ZERO emitter"** — `module_contracts.yaml:814-817` vs `parliamentary_transfer.py:230` | A | Update the registry row **and** diagnose the post-port silence — it is 3 of the 22 red tests | **Session**, inside the port tail |
| 5 | **MB armour** — disputed cells implemented by neither surface | C | Resolved by the tree's own labels: the Ranged DR table is CANONICAL, `§B.2` PROVISIONAL. Annotate §B.2. **Wiring is Class E roadmap** | **Session** for the doc; roadmap for the wiring |
| 6 | **Churn engine** — ratified, no code | **E** | **Nothing to resolve.** Filing it as a conflict is the misfiling class that got a prior session reverted | — |
| 7 | **PC degree ladder** — `core.py:58-83` held at the pre-2026-08-14 model | D/F | Put it to Jordan **together with** the score/2 obstacle migration — the code says deciding them separately is work thrown away | **Jordan** |

⚠ #7 is **not a new discovery**, despite being presented as one — it is a docketed hold recorded in
ED-IN-0187, ED-IN-0194 F8, and `test_degree_ladder_single_owner.py`. It is, however, the biggest.

### III.3 Draining the 154-row queue

**Per row:** resolve the effective (last) row → open **every artifact it names** → look for LIVE
signals (`held for Jordan`, `HELD`, `deliberately NOT wired`, `NO DEFAULT`, an unruled packet, a
`[SEED]` on the disputed value) vs DEAD signals (artifact forked/deleted; a later ED implements one
option; the row's tail says EXECUTED with a citation) → apply the five tests **in order** → append a
closure row citing the first that fires. **Never edit history.**

**Batching without repeating the 17-row mis-cull:** never close on a status pattern; every closure
quotes disk evidence; batch **by lane, ≤20 rows per PR**; anything whose artifact you cannot open goes
to `blocked`, not `closed`. **A survivor must leave the drain carrying a proposed answer** — the
measured disease is evidence-rich, answer-poor.

**Estimate: 20–30 of 154 are genuinely Jordan's.** Confident survivors: `ED-SC-0004`, `ED-SC-0005`,
`ED-PC-0016`, `ED-IN-0187`, `ED-IN-0113`, S8 Half B, the tenth-attribute name, the Godot 4.3-vs-4.6 ruling.

### III.4 The DONE condition — and the instrument that must be fixed first

⚠ **The obvious grep is the wrong instrument.** A proposed DONE condition of *"every
`held for Jordan|HELD|awaiting ruling` hit maps to a `needs_jordan` row"* was tested: it finds **5**
genuine sites (not the 2 claimed) — `weapons.py:912,919`, `combat_systems.py:872`, `core.py:58,75`,
`sigma_leverage.py:321` — and **misses at least 13 more** code-resident holds phrased differently
(`varfell_mandate_action.py:14,36`, `dictionaries.py:203` "OPEN DECISION FOR JORDAN",
`core/contact.py:363` "pending Jordan", `mass_battle/sim/config.py:122,126,236,247,256`, …).

**Fix the pattern before binding a DONE condition to it**, or the condition is satisfiable while most
holds stay unmapped. That is a check that cannot observe what it excludes — the session's signature defect.

DONE is: an execution artifact per conflict, green under CI env; the bidirectional map verified once
with the *corrected* pattern and pasted in the PR body (not committed as a tool — prose guards fail
§0.1 pt 5); the queue count recomputed with every survivor carrying options.

---

## 4. What is genuinely blocked on Jordan

Everything else above is answerable by ruling, document, precedent, or architecture.

1. **ED-SC-0004** — the Argue-pool fork, explicitly reserved.
2. **ED-IN-0187 + the obstacle model** — the degree-ladder hold and the score/2 migration, together.
3. **The knot/NPC reachability deferrals** — whether campaign-scale world-gen may carry personal-scale
   actor fields. This is what actually gates the emit side, and inventing the schema is a design
   choice with materially different games on each side.
4. **Whether to build the PP-686 mission mechanic at all** — milestone scoping.
5. **ED-PC-0016** (half-sword auto-switch) and **ED-PC-0049** (`ADEF_POINT` 1.2 vs ~1.53).
6. **S8 Half B** — suspended; listed so nobody launders it into the cull.

---

## 5. Sequencing across all three programmes

```
[branch from green: d080a36, or land the 22-test port tail first]
  ├─ III.2 #1, #3  Knot Pool + both-partners        (session, unblocked, GAME code)
  ├─ III.2 #4      da.* registry + silent emitter   (inside the port tail)
  ├─ II.1 step 1-2 registry hygiene + wire --check   (makes the conformance floor real)
  ├─ I.1  S7.1 → S7.6                                (the cull; gates at each step)
  ├─ II.1 step 3   Faction.adjust emit spine         (the actual hub-and-bus work)
  ├─ II.1 step 4-5 read side + constants
  └─ III.3 queue drain, by lane, ≤20 rows/PR
Jordan docket (§4) compiled ONCE, at the end, with options and recommended defaults.
```

**Why this order:** the two unblocked game fixes go first because they are game code and cost nothing
to verify; registry hygiene precedes the cull because the cull's gates read those registries; the
emit spine follows the cull because S7 changes what the conformance instrument sees; the queue drain
goes last because S7 and the merges kill subjects first, converting judgement-calls into citations.
