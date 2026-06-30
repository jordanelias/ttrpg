## Status: CURRENT — audit record (2026-06-30)

> Adversarial ecosystem review run via a 72-agent verification workflow (6 audit dimensions ×
> two independent skeptical lenses per finding). 24 findings survived; the headline items were
> hand-spot-checked against the cited files. Tracked by **ED-1050..ED-1054** in
> `canon/editorial_ledger.jsonl`. This is an audit record, not canon — no mechanic changes here.

# Valoria — Adversarial Review: Godot-Readiness & Repo Health

**Scope:** 24 verified findings, deduplicated and reprioritized by blast radius on the upcoming Godot 4.6 port. The repo's stated bridge to implementation — a typed param layer, a tested Python reference, SHA-pinned canon, and a green parity oracle — is in each case either non-ingestible, untested, decorative, or already broken. Severity ranks by how directly a finding lets *wrong design state reach the game*.

---

## 1. Godot-Readiness (the port cannot start cleanly)

These block or silently corrupt the implementation handoff. Highest priority.

### 1.1 — [CRITICAL] The one ported module already disagrees with its own parity oracle
*(godot-pipeline/pipeline-01)*
The governing strategy makes "Key-log equality vs the Python reference" the master parity gate. Yet module #1 hand-edits that oracle: `combat_config.gd:58` ships `adef_threshold = {light:0.45, medium:0.60, heavy:0.72}` (with an inline `[AUDIT-FIX]` and a concession that "a parity re-sweep is required before this ships"), while the canonical oracle `combat_engine_v1/config.py:29` reads `{light:0.70, medium:0.45, heavy:0.72}`. **Verified — the two differ on `light` and `medium`.** A recorded-draw replay can therefore *never* go green against this skeleton. The single gate that licenses a no-GM deterministic engine is broken at the source.
**Fix:** route the monotonicity correction through the editorial ledger as a *canon* change to `config.py`, regenerate the `.tres`, and never let a port correct its oracle in-place.

### 1.2 — [HIGH] The skeleton is non-compilable and covers 1 of 27 modules
*(pipeline-04, pipeline-06)*
`combat_engine.gd extends BaseEngine` and calls `KeyBus.emit_key`, `GameState.get_actor`, `Resolver.D_SIGMA` — none of `BaseEngine`, `EngineModule`, `Key`, `KeyBus`, `GameState`, `Resolver` is defined anywhere in the corpus. The Gate-0 spine (KeyStore v2, kernel, seeded-RNG) is an *unexecuted precondition*, and the governing strategy doc is itself `status: PROPOSED (Jordan-vetoable throughout)` with an 8-item open register including load-bearing choices (Key as Resource vs RefCounted, autoload set, downward delivery). An agent told "port from the skeleton" hits undefined symbols immediately.
**Fix:** land Gate-0/Stage-1 as real compilable GDScript with the dice kernel green against `d10_success_probabilities.json` *before* presenting any slice as "PORTED"; drive the Part VIII register to closure and re-stamp the strategy CANONICAL.

### 1.3 — [HIGH] ~37% of the module surface has no implementable spec
*(pipeline-03)*
In `module_contracts.yaml`: **10 of 27 modules have `doc: null`** (verified) — including `engine_clock`, the temporal/Accounting spine every system hangs off — and **11 of 27 resolvers are `[ASSUMPTION]`-grade** (verified), meaning the determinism *class itself* is unconfirmed. For a no-GM engine, an unratified resolver enum is an unspecified determinism guarantee. The port is blocked beyond the combat slice.
**Fix:** author the `[GAP]`-home-doc modules in priority order (`engine_clock` first) and run the module-adjudicator to ratify each `[ASSUMPTION]` resolver before the port consumes it.

### 1.4 — [MEDIUM] Four `designs/godot/*.md` specs ship superseded schemas with no banner
*(pipeline-05)*
All four docs are dated 2026-04-18, carry no supersession banner, and encode the pre-d+σ / pre-LPS-2e model. `data_serialization_spec.md` still ships `FactionData.mandate` as a writable `@export int` (canon: Mandate is a *read-only derived aggregate*, R4 violation), 34 settlements (canon: 35), and a 3-axis TN weapon model (canon: weapon vectors, d_sigma). An agent implementing `mandate` as a base field directly breaks the derived-write discipline the substrate depends on.
**Fix:** add supersession banners → `godot_conversion_strategy_v1.md`, or move to `deprecated/`; regenerate `data_serialization_spec.md` from `module_contracts.yaml` + the descriptor registry.

---

## 2. Data Management (the numeric layer is non-ingestible and stale)

The canonical values Godot must bind to are untyped prose, stale, or sourced from dead files.

### 2.1 — [HIGH] Every engine parameter is trapped in prose; the "structured" registry stores formulas as free-text English
*(data-01)*
All numbers live in `params/*.md` markdown tables. `values_master.yaml`'s 1245 `formula` fields are byte-identical to `value_raw` — lifted prose strings (`"(Agility × 2) + Relevant History + 3 (minimum 5)"`, durations like `"60–90 min"`, even non-formulas like an armour-Stamina caveat stored under `kind: formula`). No operand/operator/AST decomposition exists. A Godot importer cannot produce `.tres` Resources without writing a natural-language math parser for unicode `×`, en-dashes, and parenthetical clamps. Every value must be hand-transcribed — reintroducing exactly the drift the registry was meant to kill.
**Fix:** author a typed engine-params file (numeric operands, formulas as ASTs or named expression keys with explicit inputs/clamps), generated from prose by a real parser and CI-checked for round-trip equality — or make the typed file the source and render the markdown from it.

### 2.2 — [HIGH] The auto-extracted values index is stale and pulls "canonical" numbers from deprecated/nonexistent files
*(data-03)*
`values_master.yaml` (regenerated 2026-06-21) holds **70 references to `params/combat.md`, a file that no longer exists on disk**, misses 2026-06-28 param edits, and sources 8 entries from `params/threadwork_superseded.md` (including struck-patch notes like "PP-192 struck"). The extractor's own header names "combat.md vs combat_v30.md drift" as the hazard it exists to prevent — now realized. The "extracted, structured" layer is less trustworthy than the prose it indexes.
**Fix:** make `extract_values` regeneration a CI gate (fail if `values_master` is older than any indexed `params/*.md`), exclude `*_superseded.md` and nonexistent sources, repoint the 70 stale entries to `combat_engine_v1`.

### 2.3 — [HIGH] 131 SHA pins are never verified against the working tree; tooling re-fetches from GitHub
*(data-02, overlaps port-debt-01)*
`canonical_sources.yaml` carries 131 `canonical_sha__` pins. No tool computes `git hash-object` on local files to compare; `freshness_gate.py` instead **re-syncs SHAs from live GitHub** (`--update`, "synced from"), directly contradicting CLAUDE.md's "do not re-fetch from the GitHub API … the checkout is fresher than any cache." The integrity signal that tells an ingesting agent "this is the exact canonical version" is decorative — pins can silently point at a commit differing from the checkout the engine is built from.
**Fix:** replace the GitHub-fetch gate with a local `git hash-object` blob-SHA verifier in CI; drop pins for files no longer needing version-locking. *(This is the same API→working-tree port as §3.1.)*

### 2.4 — [MEDIUM] The foundational stat schema is explicitly "IN FLUX" with triple-defined Combat Pool
*(data-05)*
`descriptor_registry.yaml:12` flags the 9-attribute roster "IN FLUX"; aggregates (`agg.body/mind/social`) are `status: placeholder`, "NOT yet wired"; attribute keys are `enforce: warn`, not `block`. Legacy "Stat × 3" multipliers are unretired. **Combat Pool is defined three ways** — `values_master` (`Agility×2 + Relevant History + 3`), `core.md` PP-247 (`Agi + hist_pts + 3`), and `module_contracts` v4 correcting a v30 placeholder. These derived stats are the *first* actor-resource schema Godot models.
**Fix:** ratify one derived-stat path, wire or delete the placeholder aggregates, collapse the Combat Pool triple-definition into one authoritative entry, and flip attribute keys to `enforce: block` before they become Godot field names.

---

## 3. Code Architecture (the validators don't validate; the reference isn't tested)

### 3.1 — [HIGH] Three CI "integrity" gates validate remote `main`, not the diff under test
*(port-debt-01)*
`broken_dependency_checker.py`, `patch_propagation_checker.py`, and `freshness_gate.py` all fetch from the GitHub API at `ref=main`, hard-require `GITHUB_PAT`, and are wired into the CI integrity job. A PR that *fixes* a broken dependency or adds a canonical doc passes/fails on `main`'s state — the gates protecting referential integrity (the contracts a port reads) are blind to the diffs they exist to validate, and break entirely if the PAT is absent or rate-limited.
**Fix:** port all three to the local checkout (`os.walk` / `git hash-object`), drop the PAT and urllib/GraphQL layer.

### 3.2 — [HIGH] The 11,444-line sim reference — the explicit 1:1 GDScript source — has zero tests and no oracle
*(sim-untested-04, overlaps sim-03/sim-05)*
`find sim -name 'test_*.py'` returns nothing; the `sim/tests/` directory `CONVENTIONS.md` mandates does not exist. **No CI job ever executes the simulator** — `pytest tests/valoria -q` targets only CI tooling (all 38 test functions). `mc_v18`'s self-test times out >60s. 19 modules still `raise NotImplementedError`. Running `mc_v18.run_batch(8, seed=42)` yields **Varfell 87.5% / Church 0% / Hafenmark 0%** — a degenerate balance asymmetry no assertion catches. The stated bridge to Godot is an untested, partly-stubbed reference with no oracle to validate ports against.
**Fix:** add a deterministic seeded `sim/tests/` suite (smoke + bounded win-share assertions + a pinned golden batch), profile/cap `mc_v18` so the canonical self-test runs in CI, and track the `NotImplementedError`-stub count as a coverage metric.

### 3.3 — [HIGH] ~2,500 LOC of tooling is dead — imports a deprecated module or hardcodes `/home/claude`
*(dead-tools-02)*
`github_ops.py` exists only under `deprecated/`; 7 live tools import it (`extract_values`, `valoria_collator`, `compliance_check`, `freshness_gate`, …) and fail at import. `engine_audit_harness.py` does `sys.path.insert('/home/claude')` and `from github_ops import quick_bootstrap` — wholly unrunnable. `file_lookup.py` depends on a SQLite DB at `/home/claude/valoria.db` that doesn't exist. Agents can't distinguish live validators from corpses; the engine-audit harness — the independent check on the dice/sigma engine the combat resolver depends on — provides zero protection.
**Fix:** port to the working-tree model or move to `deprecated/`; annotate each tool's runnability in `tools/README.md`; quarantine `engine_audit_harness.py` and `file_lookup.py` until rebuilt.

### 3.4 — [MEDIUM] The flagship "every rule lives once" guarantee is already falsified
*(rule-twice-03)*
Token-size enforcement runs in two CI jobs with two threshold sources that have drifted: `ci_register_size_check.py:52` caps `patch_register_active.yaml` at **20,000** while `atomization_rules.yaml` caps it at **15,000** — two gates, different limits, same file. This directly contradicts CLAUDE.md's "every rule lives once, in `tools/`."
**Fix:** delete the hardcoded `THRESHOLDS` dict; read all limits from `atomization_rules.yaml`; collapse the compliance-check size logic into the one enforcer.

### 3.5 — [MEDIUM] Tooling docs misrepresent the code state
*(stale-docs-05)*
`sim/README.md` and `CONVENTIONS.md` both say "Status: scaffold … All modules are stubs" — but sim is 11,444 LOC with 11 CANONICAL modules and a runnable campaign engine. `tools/README.md` lists ~12 of ~38 tools, omitting `validate_ed_citations`, `ci_vetting_check`, `ci_supersession_check`, the `tools/observability/` subtree, and presents the API-dependent gates as working. Agents are instructed to trust these as the navigation surface.
**Fix:** regenerate both from directory scans / `Status:` flags, annotating each module/tool as runnable/dead/local-only.

---

## 4. Sim & Test Integrity (the anti-fabrication guard is defeatable)

The owner's stated "#1 simulation failure mode" — fabricated uncited constants reaching the reference implementation and being ported verbatim — is not actually guarded.

### 4.1 — [HIGH] The fabrication guard whitelists numbers by bare value, globally
*(sim-01)*
`ci_sim_fabrication_check.py` collects only `e['value']` into a set and accepts any constant whose integer appears *anywhere in any ledger*, ignoring variable name, file, and quoted text. **Proven:** `FABRICATED_CRIT_MULTIPLIER = 25` passes silently because some unrelated variable also equals 25; only `712` is flagged. The checker's own docstring admits "a matching number with a different meaning would pass."

### 4.2 — [HIGH] Floats are split into integer tokens, so fabricated float constants pass
*(sim-02)*
The numeric pattern matches digit-runs only; `1.7` becomes tokens `1` and `7`. `genuine_violations('LETHALITY = 1.7', {'7'})` returns `[]` — a fabricated lethality coefficient passes because the ledger contains `7`. **Most balance/tuning constants are floats** — exactly the values most needing provenance before being baked into combat tuning.

### 4.3 — [HIGH] Ledgers use ≥3 incompatible schemas; only one field is ever read; no SHA pins the generating code
*(sim-04)*
14 ledger files span 3 schemas; the checker reads only `value`, ignoring `sim_variable`/`canonical_source`/`quoted_text`. No ledger records a git SHA. A porter cannot determine which sim revision produced a constant or whether it's still valid; the provenance fields that would answer rot unchecked.

> **Consolidated fix for 4.1–4.3 + sim-05:** match ledger entries by `(sim_variable AND value)` *co-located to the specific file*; tokenize numeric literals including decimal points and signs; define one ledger schema carrying `schema_version` + the generating sim git SHA; verify `quoted_text` exists in the cited source; add a *periodic full-corpus* scan (not just changeset). Wire a schema linter into CI.

### 4.4 — [LOW] `tests/` conflates the real pytest suite with ~850KB of narrative markdown
*(sim-06)*
15 top-level `*.md` (`emergent_arc_skeleton_test_*` batches, `audit_three_day_*`, and `commit_test.md` containing literally a session token) sit beside the only executable suite (`tests/valoria/`, 5 files). An agent mining `tests/` for executable specs wades through unexecutable prose and may mistake "skeleton test" scenarios for verified contracts.
**Fix:** move narrative/audit markdown to `designs/audit/` or `archives/`, delete `commit_test.md`, reserve `tests/` for executable suites.

---

## 5. Claude Code Ergonomics (the navigation surface lies)

The first files an onboarding agent reads point at retired machinery — anchoring whole sessions on dead state.

### 5.1 — [HIGH] Retired orchestrator machinery is documented as currently "built" with a live Public API
*(ergo-02)*
`references/subsystems/{handoff,checkpoint,session_log}_subsystem.md` each carry `Status: built` and full read/write/close API specs sourced from `skills/valoria-orchestrator/scripts/github_ops.py` — a skill **retired to `deprecated/`** (CLAUDE.md:99). `roadmap_state.yaml:54–57` still lists these as active items. None carries a deprecation banner. This is the highest-friction stale doc: detailed enough to be trusted, so an agent wastes turns calling functions in a dead skill.
**Fix:** move to `deprecated/` or prepend a "RETIRED — superseded by HANDOFF.md + git" banner; purge the live `roadmap_state.yaml` items.

### 5.2 — [HIGH] README.md is stale on every navigational pointer
*(ergo-03)*
The conventional first-read file points at a **2-generations-stale workplan** (`valoria_workplan_v3_consolidated.md`; CURRENT.md names `valoria_master_workplan_v5.md`), a **retired GraphQL bootstrap protocol**, a "Phase 0 in progress" line with no v40 context, `archives/` mislabeled as a working "Session logs" dir, and a "7-job CI pipeline" vs the larger gate set. An agent trusting it anchors on retired state before reaching CURRENT.md.
**Fix:** rewrite README.md to *defer* — "For current state see CURRENT.md; for workflow see CLAUDE.md; for next actions see HANDOFF.md" — dropping the bootstrap, v3, Phase-0, and 7-job claims.

### 5.3 — [MEDIUM] The retired continuity machinery is still live in the working tree
*(ergo-01)*
CLAUDE.md:31 and HANDOFF.md both declare session-log/checkpoint machinery retired. Yet git-tracked at root: `session_log_current.md`, `session_log_archive.md`, `session-handoff-2026-05-06.md`, `session_logs/index.md`, `handoffs/` (3 live YAMLs), and `canon/session_checkpoint.md` whose frontmatter reads **`status: active`, created 2026-06-26** — an "active" checkpoint persisting after retirement (verified; bulk archive copies also live under `archives/session/`). An agent may resume from the stale active checkpoint or write into `session_logs/`, diverging from the single HANDOFF.md the SessionStart banner actually reads.
**Fix:** move the root-level files and `canon/session_checkpoint.md` under `deprecated/`; remove their `ci_register_size_check.py` entries. Keep exactly one live continuity surface: HANDOFF.md.

---

## 6. Structural Debt

### 6.1 — [LOW] The `_v30` generation-marker scheme is self-contradicting
*(struct-05)*
CURRENT.md:36 says `_v30` "marks the current generation," but the current combat head is the **non-`_v30`** `combat_engine_v1/` (verified at CURRENT.md:20), while `combat_v30.md` is `[PARTIALLY SUPERSEDED]` and internally stamps three versions (filename `_v30`, title "v1", "Version: v1.7"). Plus a "Generation v40" marker that is deliberately *not* a suffix (0 files carry it). Three orthogonal version axes with no 1:1 mapping force every currency decision through hand-maintained CURRENT.md — exactly the tribal-knowledge dependency that breaks when it drifts.
**Fix:** pick one currency axis — drop generation markers from filenames, rely on location (`archives/` = dead) plus a CI-enforced in-file `## Status: CURRENT|SUPERSEDED→<path>` header. At minimum, `_SUPERSEDED`-rename `combat_v30.md` so a `_v30` name never points at a non-current doc.

---

## Top 5 Actions Before Godot Implementation

1. **Fix the broken parity oracle (1.1).** Correct `config.py` ADEF_THRESHOLD in canon via the editorial ledger, regenerate the `.tres`, and get module #1's Key-log replay green. Without a green oracle, *no* port can be certified — this gates everything downstream.

2. **Land the Gate-0 spine + author `engine_clock` (1.2, 1.3).** Build `BaseEngine`/`EngineModule`/`GameState`/`KeyStore v2`/seeded-RNG as compilable GDScript with the dice kernel green against `d10_success_probabilities.json`, and author the 10 `doc: null` modules starting with the temporal spine. The skeleton is illustrative pseudocode until this exists.

3. **Make the numeric layer ingestible and verified (2.1, 2.2, 2.4).** Author a typed engine-params file (numeric operands, AST/named-expression formulas) as the Godot ingestion source, CI-gate `extract_values` freshness, exclude `*_superseded.md` + the 70 dead `combat.md` refs, and resolve the Combat Pool triple-definition. Hand-transcription is the drift vector the registry was meant to eliminate.

4. **Make the integrity gates actually validate the diff (2.3, 3.1, 3.2, 4.1–4.3).** Port the three GitHub-API gates to the local checkout, replace decorative SHA pins with a `git hash-object` verifier, fix the fabrication guard to match by `(variable, value, file)` and tokenize floats, and add a deterministic seeded sim regression suite that runs in CI. Today, fabricated balance constants and stale canon versions can reach the port with green CI.

5. **Repair the navigation surface (5.1, 5.2, 5.3, 4.4).** Rewrite README.md to defer to CURRENT.md/CLAUDE.md/HANDOFF.md, banner-or-deprecate the three "built" orchestrator subsystem docs and the four stale `designs/godot/*.md` specs, retire the live session-log/checkpoint files (including the stale `status: active` checkpoint), and clear narrative markdown out of `tests/`. An agent must not anchor a Godot session on retired state before it reaches the canonical index.
