# VALORIA — Session Master (consolidated)

**Date:** 2026-05-28 · **Task:** audit (bootstrapped). **This is the single document to read.** Produced per PI `<document_consolidation>`: the session's ~18 artifacts collated → reconciled → consolidated here. Detailed backing docs remain as evidence; the **Supersession Manifest** (§5) says which are current vs historical. Nothing was silently resolved — substantive design forks are surfaced as owner-decisions (§3), and generated files (`valoria_index.sql`) are regenerated, not hand-merged (conflict-resolution #9).

All repo writes below are **B6-blocked** (branch protection) → **staged for Jordan to push.** `[CONFIDENCE: high on infra (tested green); high on audit structure; low on absolute MS pacing numbers — illustrative pending the repo mc engine.]`

---

## 0. What this session did, in one paragraph
Made the repo's SQLite file-index (`references/valoria_index.sql`) the **governing interface** for repo interaction: completed the curated manifest (49→**82 concepts** / 189→**231 concept_files** / 334 aliases), fixed the regenerator's schema round-trip bug (**F2**), and built + tested a bootstrap **enshrinement** module that rebuilds the machine layer from HEAD each session and validates coverage. Then ran a full **NERS audit with a new historical-precedent validation axis** over every system there was canonical grounding for, validated the **MS / Force-3** bound by Monte-Carlo, locked Jordan's MS-model decisions, and upgraded the `valoria-resolution-diagnostic` skill with a **Stage 5 (historical-precedent validation)**.

---

## 1. INFRASTRUCTURE — SQL-index enshrinement (state + push checklist)
*Consolidates: `A3_enshrinement.md`, `A1_census_reconciliation.md`, `repo_traversal_action_plan.md`.*

**State (all verified green this session):**
- **`valoria_index.sql`** — completed manifest, **82 concepts / 231 concept_files / 334 aliases**, round-trip-loadable. (Correction of record: my earlier "empty manifest / 0 rows" claim was a grep error — the dump uses `INSERT OR REPLACE INTO`, which an `INSERT INTO` grep missed. It was never empty; it was orphaned-at-bootstrap.)
- **`regenerate_file_index.py`** — `open_db` **F2 fix**: `executescript()` tripped a deferred FK check (one implicit transaction + embedded `PRAGMA foreign_keys=ON` + FTS5 trigger/shadow-table creation). Replaced with a statement-by-statement autocommit loader (`_split_sql`, triggers kept atomic). Committed dump now round-trips.
- **`index_bootstrap.py`** — NEW. `load_index(g)` rebuilds `files` from HEAD (drift-proof), loads curated, `validate()`; TTL-cached (600s, zero-API on hit). `concept_files()` / `which_concepts()` / `search()` query interface. Halts on malformed dump; `strict=True` halts on any drift; otherwise warns.
- **`test_index_bootstrap.py`** — offline round-trip + query smoke test, passing.
- Census (folded from A1): **1882 indexable files** in `ttrpg` (`valoria-game` not indexed — deferred extension); all 61 `canonical_sources` design docs present (0 phantom).

**Final machinery check:** regenerator F2-fixed ✓ · completed index loads 82c/231cf ✓ · malformed-dump halt ✓ · smoke test PASS ✓ → **green.**

**PUSH / APPLY CHECKLIST (Jordan):**
1. Push 3 repo files: `references/valoria_index.sql`, `skills/valoria-orchestrator/scripts/regenerate_file_index.py`, `skills/valoria-orchestrator/scripts/index_bootstrap.py` (+ add the smoke test under `tests/index/`).
2. Push the skill patch: `skills/valoria-resolution-diagnostic/SKILL.md` (Stage 5 — see §4).
3. Apply PI/architecture text edits verbatim from `A3_enshrinement.md` (the `<bootstrap_script>` 3-line addition + `<post_bootstrap_calls>` routing note + architecture `<reference_files_pattern>` / `<enforcement_spectrum>` rows) and the one-line `safe_commit` cache-invalidation (`os.remove('/home/claude/.index_cache.json')` on tree-changing commits).

**Two benign drift items the validator flagged against live HEAD (refinements, not blockers):**
- 3 dangling = `canon/editorial_ledger*` — exist on HEAD but the classifier files them as data, not active design docs; the `editorial` concept's paths and the classifier's domain map disagree. *Refinement:* reconcile the `editorial` concept's member paths with the classifier, or whitelist these.
- 1 uncovered = `designs/audit/2026-05-28-combat-reframe/ners_verdict_combat_v32.md` — a **new audit artifact created on HEAD today**, correctly flagged as unregistered (proof the HEAD-rebuild self-heals). *Refinement:* `validate`'s `uncovered` filter should exclude `designs/audit/` paths (audit outputs belong in `files`, not system concepts).

---

## 2. DESIGN AUDIT — consolidated findings
*Consolidates: `passB_master.md`, `passC_synthesis.md`, `passC_ms_force3_validation.md`, `decisions_1to5_resolution.md`, `NERS_historical_validation.md`. Supersedes the loop_cascade_map W-series, the three passB batch files, and ms_dynamics_reference.*

### 2a. MS engine + Force-3 bound (LOCKED + validated)
- **Locked (Jordan):** game-time MS **net-decays by default**; **start MS = 60**; **passive Warden Mending**, degradable by Warden interruption (canon already has the hooks — Sanctuary +1/s needs the Outpost near the Southernmost; WC3 +2/s is Edeyja). Resolves the DC-2 contradiction cluster (ms_trajectory "always positive" = historical-only; clock_registry 72→60; sim −1/yr sign confirmed).
- **Two-force model:** Force 1 baseline-positive but *small* (~+13/257yr); Force 2+ tearing (warfare flat cap −3/s; Gap-bleed per-scale 1/2/3/5; Foundational ×3 multiplier). Maintain mitigation: WC2 halves, WC3 +2/s, Sanctuary +1/s, active Mending ops.
- **Force-3 bound (validated by Monte-Carlo):** the **−10/s net-loss cap is the guardrail** — climax tearing crashes MS in **6 seasons from 60, 4 from the Fragile floor (40)** → satisfies "not 0 in ~4 seasons." Heavy threadwork saturates the cap; warfare alone (−3/s) cannot approach it → *threadwork is the crash driver, warfare can't*, exactly as locked. `[ASSUMPTION: cap = −10/s; the params-struck-vs-§5-±10 contradiction is the one MS decision still formally open — recommend adopting −10/s as the explicit guardrail.]`
- **Precedent validation (ecological regime-shift, Holling/Scheffer):** strong match — MS bands = ball-in-cup basins; the *maintain-requires-de-escalation* property **IS hysteresis** (the documented signature: reversing the cause doesn't restore the state). **New precedent finding (P3):** real regime-shifts emit *leading warning signals* and have *asymmetric* collapse/recovery thresholds → recommend a legible MS warning trend + (owner decision) explicit hysteresis (recovery threshold > collapse threshold).

### 2b. Loop inventory (final — supersedes the W-series)
Scale-anchored to canon (DC-7 fix): Object · Personal · Relational · Field · Structural · Foundational × personal/settlement/territory/peninsula.

| Loop | Verdict | Basis |
|---|---|---|
| **MS / threadwork** | **Bounded** (−10/s cap; intrinsic Force-1) | Monte-Carlo + ecological-regime-shift precedent |
| **Faction-collapse** | **Bounded — corrects diagnostic "Lesson 5"** | Stability recovery +1/s · Survival Exception · reconstitution≠extinction · Military sticky; **Tainter** (collapse=simplification+reconstitution) |
| **L-CONV** conviction | Bounded single-path; cascade tail `[INTENT UNDETERMINED]` | 1 Scar/s cap; attitude-change precedent |
| **L-SPLIT** succession | Bounded; cooldown PROVISIONAL | re-merge + cooldown; succession-war precedent (Diadochi/Roses/Sengoku) |
| **mass-battle morale** | **Bounded** | braked rout contagion; Ardant du Picq/surrender-cascade precedent |
| **L-MIRACLE** | Bounded | one-time Accord + TD counter; Weber charismatic-authority precedent |
| **L-DEFECT** npc | **Fail R — UNBUILT** (B1.2 hooks-only) | near-exact match to defection-cascade poli-sci → build it |
| **L-INSURG** GD-3 | **Fail R — no down-path** | RAND *How Insurgencies End* → multi-path dissolution |
| F-series (BG fuses), L-CONV→faction, Varfell ratchet | **UNREAD** | DC-3 / DC-6 / DC-11 — not yet read |

### 2c. NERS verdicts (with precedent; from `NERS_historical_validation.md`)
- **Threadwork/MS:** compliant *iff the −10/s cap holds* (else fails R — instakill). The cap decision is load-bearing for the verdict.
- **Faction action layer:** **non-compliant** — bare-stat 1–7D roll on pivotal/irreversible outcomes fails R (precedent: real political contests are structure-driven, not coin-flips) → **Lesson 3**. *The collapse loop is NOT the defect — Lesson 5 retracted.*
- **Mass battle (design):** compliant (sim has separate P0 engineering stubs).
- **L-DEFECT / L-INSURG:** fail R on **incompleteness** (unbuilt / no down-path), not instability → build / author.
- **L-CONV / L-SPLIT / L-MIRACLE / faction-collapse:** pass (per matrix).
- **PENDING (no verdict issued — honest):** personal combat, social contest, investigation/fieldwork, victory/peninsula, diplomacy. These had only the skill's *untested hypotheses*; precedent lens pre-assigned, awaiting bottom-up reads.

---

## 3. OPEN OWNER-DECISIONS (consolidated — yours, not mine)
1. **MS seasonal cap** (the one MS decision still open): adopt **−10/s** as the explicit Force-3 guardrail (recommended; resolves params-struck-vs-§5-±10), or keep struck?
2. **MS hysteresis** (new, precedent-driven): add asymmetric collapse/recovery thresholds + a legible warning trend? *(P3; improves R/S/E.)*
3. **Maintain-victory closure threshold** (`[GAP]`): how many successful Foundational (Askeheim) Mends = "Calamity resolved"? Grind rate provided (~0.4–0.6 MS/s, ~28% per attempt) so you can set the bar. *(Decision 3 itself — keep "maintain = de-escalate+heal" — is RESOLVED: don't buff WC; the tradeoff is the long game.)*
4. **Insurgency dissolution** (GD-3 down-path): confirm **multi-path** (military / sponsor-withdrawal / amnesty / else-persist); sponsor-withdrawal is the precedent-strongest add.
5. **Defection cascade** (B1.2/B1.3): schedule the build (validated as precedent-correct; + fragility-multiplier + suppression-brake).

---

## 4. SKILL UPGRADE — Stage 5 (done, staged)
`SKILL_resolution_diagnostic_PATCHED.md` (231→261 lines): adds **STAGE 5 — Validate Against Historical Precedent** (the external NERS-R axis the pipeline lacked: identify the modeled phenomenon → cite real precedent → compare *behavior* → match=R-evidence, divergence=finding; metaphysical layer validated analogically only). Adds the **"validate against reality, not genre"** guardrail and updates the front-matter. Front-matter YAML + structure verified. → push to `skills/valoria-resolution-diagnostic/SKILL.md`.

---

## 5. SUPERSESSION MANIFEST (collation result)
**CURRENT — canonical detail docs (keep):**
- `VALORIA_MASTER.md` (this) · `A3_enshrinement.md` (infra push detail) · `passB_master.md` (system reads) · `passC_synthesis.md` (loop map + DC-1..12 fold) · `passC_ms_force3_validation.md` (MS sim) · `decisions_1to5_resolution.md` (decision detail + precedent) · `NERS_historical_validation.md` (NERS matrix) · `loop_map_doublecheck.md` (source of DC-1..12; reference).
- Code: `valoria_index.sql`, `regenerate_file_index.py`, `index_bootstrap.py`, `test_index_bootstrap.py`, `SKILL_resolution_diagnostic_PATCHED.md`.

**SUPERSEDED — historical, safe to archive (do not work from):**
- `loop_cascade_map.md` → superseded by `passC_synthesis.md` §1 (loop map).
- `passB_threadwork_and_force3.md`, `passB_batch2_omitted_loops.md`, `passB_batch3_faction_collapse_and_MS.md` → folded into `passB_master.md`.
- `ms_dynamics_reference.md` → superseded by `passB_master.md` §2 + `passC_ms_force3_validation.md`.
- `A1_census_reconciliation.md`, `repo_traversal_action_plan.md` → folded into §1 above (census done; plan executed).

(Per the consolidation rule, originals are preserved — none deleted; this manifest marks status.)

---

## 6. RESUME-FROM-HERE
**Pushed by Jordan, then:** the index governs; route system reads through `ix.concept_files(name)`.
**Audit completion (remaining, index-driven):**
- Bottom-up reads + NERS+Stage-5 for the 5 PENDING systems (combat, social, investigation, victory, diplomacy).
- Per-loop **gain computations** (DC-8) for loops still lacking one (only MS is computed).
- **clock_registry/DC-12** bounds cross-check (settles the cap + any residual start-value drift); **BG fuses/DC-3**; **faction_behavior §3.2/DC-6**; faction remainder (12 files).
- Real **`mc`-engine run** with canonical tearing distributions for true MS pacing.
**Staged ED cluster (B6-blocked):** MS cap (P1) · start-MS 60 (resolved→annotate) · defection-unbuilt (P2) · insurgency-dissolution (P2) · maintain-mitigation (resolved) · MS-hysteresis (P3) · RS/MS label drift · Gap-bleed model · stale v25 cross-ref · conviction_track supersession · the 2 index-classifier refinements (§1).
