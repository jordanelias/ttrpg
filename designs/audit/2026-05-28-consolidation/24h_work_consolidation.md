# Valoria — 24-Hour Work Consolidation

**Window:** 2026-05-27 23:06 → 2026-05-28 23:06 UTC
**Source:** `jordanelias/ttrpg` main — 15 commits, 0 PRs; `jordanelias/valoria-game` untouched
**Compiled:** 2026-05-28 · session token `c93a36df` (bootstrap) / `174e63d8` (re-bootstrap)
**Scope:** all 15 commits in. `.sql` exclusion moot (no `.sql` in window). Combat thread included per Jordan.

`[SELF-AUTHORED — bias risk]` Nearly all audited content is prior-Claude output committed by Jordan; reviewed here as external work. The corpus already contains a same-day self-audit that caught one overclaim — that pattern recurs (§3).

---

## 0. Orientation

The 24h work is **six overlapping efforts from ≥3–4 concurrent sessions** that collided once and rebased cleanly (per the PT+Treaty review §5): infrastructure/roadmap, PT/treaty Pass-A cleanup, an engine-replacement audit chain, a 7-system resolution diagnostic, a combat reframe + v31 baseline, and a PT+Treaty build-readiness review.

**Substantively the work is sound.** The engine verdict, the faction-layer diagnosis, and the combat reframe are each well-reasoned and largely self-correcting. The live risks are almost entirely **documentation-integrity and stale-repo-state**: committed artifacts that disagree with their own later corrections, and a commit-blocking claim the commits themselves disprove (§3.1). None of the ten conflicts below is a design error in the underlying systems; they are reconciliation and propagation defects.

---

## 1. Commit inventory

| # | Thread | SHA | Title |
|---|---|---|---|
| 1 | A · infra | `8bf338a4` | add `references/roadmap_state.yaml` (in-repo roadmap pointer) |
| 2 | A · infra | `d0649060` | bootstrap Status Block surfaces ROADMAP POSITION (`report_roadmap` wiring) |
| 3 | A · infra | `4cb2db90` | document ROADMAP POSITION in SKILL.md + registry co-files |
| 4 | A · infra | `0a948ec3` | roadmap: Phase 1 complete (9/9); advance to Phase 2 |
| 5 | B · cleanup | `281debe2` | correct stale canon-pending annotations on treaty/PT/vote stubs (Pass A) |
| 6 | C · engine | `d78dbfbe` | engine replacement audit (v1) — 9-system assessment + precedent |
| 7 | C · engine | `56e83862` | engine replacement audit — reconciled v2 (closes ER-2) |
| 8 | C · engine | `cb32edb5` | external audit of `engine_replacement_reconciled` (GD-2 miscite + 0-P1 overclaim) |
| 9 | D · diagnostic | `e1050f38` | add `valoria-resolution-diagnostic` skill (NERS wrapper) |
| 10 | D · diagnostic | `05f523a3` | resolution diagnostic batch 1 (combat/faction/mass-battle/threadwork) |
| 11 | D · diagnostic | `76bdf992` | resolution diagnostic batch 2 (social/investigation/peninsula-victory) |
| 12 | D · diagnostic | `1184b216` | resolution diagnostic correction + ledger staging (closeout) |
| 13 | E · combat | `bd2fcb45` | combat reframe analysis (blueprint, attribute weight, derived stats, matchup, modifier) |
| 14 | E · combat | `6c0b0457` | checkpoint combat_v31 proposal (pre-reframe baseline) |
| 15 | F · pt-treaty | `6aaeadaa` | PROVISIONAL — PT+Treaty build-readiness review (companion to Pass A) |

---

## 2. Per-thread synthesis

### A — Infrastructure / roadmap (commits 1–4)

A `references/roadmap_state.yaml` was introduced as the in-repo "where are we" pointer the bootstrap consumes, with `report_roadmap` wiring added to `github_ops.py` and a ROADMAP POSITION block now printed in the Status Block (verified live this session). Phase 1 ("stale-claim cleanup," 9/9) closed; **Phase 2 ("document undocumented subsystems," 0/11)** is in progress. Phases 3–7 not started. Six decisions are pending: **D0** branch-protection rulesets (disabled 2026-05-25; recommend leave disabled), **D2** M3 completeness_gate (build reduced-scope or cut), **D3** M4 citation enforcement (downgrade to soft-warn — recommended), **D4** `canon/task_manifests/` YAML (cut — recommended; in-code dict canonical), **D5** session-log migration, **D6** scope-vocabulary unification.

### B — Cleanup / PT Pass A (commit 5)

Behavior-neutral annotation cleanup across five files (`treaty.py`, `parliamentary_transfer.py`, `parliamentary_vote.py`, `coverage_matrix.md`, `module_manifest.md`): removed stale "canon authoring pending Pass 2h" markers that became false when PT/Treaty canon landed 2026-05-17, and corrected `treaty.py`'s incorrect claim that `World` had no `treaties` field (it does). This is "Pass A" of the PT+Treaty build (thread F).

### C — Engine replacement (commits 6–8)

A three-step chain on a single question — *should the d10/TN/Ob core engine be replaced?*

- **v1** (`engine_replacement_audit.md`): nine-system assessment with per-system precedent (Battle Brothers, CK3, KoDP, Citizen Sleeper, Mage). Verdict: **do not replace**; the engine is already scale-fragmented and graded, fits where pools are healthy, is correctly absent where deterministic. 1 P1 (ER-2, continuous-engine equivalence unvalidated at faction scale — filed as debt, **not run**), 4 P2, 4 P3. No paradigm finding.
- **reconciled v2** (`engine_replacement_reconciled.md`): ran ER-2's deferred small-pool test (MC 300k), **closed ER-2** by showing the discrete↔continuous divergence (2.7–4.4× below 5D) is a missing continuity correction (`Ob − 0.5`), not a CLT failure — downgraded P1→P3. Disentangled ER-1 (resolver design) from ER-2 (engine implementation). Reconciled with the resolution diagnostic and claimed **"0 P1, firmer than v1."** Verdict unchanged: don't replace; the one real change is the faction-scale resolver (Jordan's call).
- **external AUDIT** (`engine_replacement_reconciled_AUDIT.md`): independently **exact-convolution-verified** the §2 table and confirmed the verdict is correct — but found two P1 defects in v2 (§3.2 below) plus ten lesser findings.

**Net:** do not replace the engine (robustly corroborated three ways). Faction resolver is the single genuine change; continuity correction recommended but its spec is incomplete (§3.8).

### D — Resolution diagnostic (commits 9–12)

The new `valoria-resolution-diagnostic` skill (a three-stage NERS-compliance wrapper) was added, then run on all **7 resolution-bearing systems**:

| System | Verdict (as committed) | Headline finding(s) |
|---|---|---|
| Faction action layer | **NON-COMPLIANT** (R/S/E fail) | bare-stat pool on pivotal actions; inert anti-death-spiral floor; unbounded collapse loop; Ob-formula + stat-schema contradictions |
| Personal combat (v30) | **COMPLIANT** (handoff caveat) | PP-717 D2 Pool DR not propagated to canon (P1); L2/L3 trade-off explicitly accepted |
| Threadwork | **COMPLIANT** | Mending Coherence-cost contradiction (Foundations vs §3.2, P1); Knot tier-drift (= ED-841, pre-flagged) |
| Mass battle | **COMPLIANT** (backlog) | no Pool Floor (novel P1); 8 decisions + 27 PROVISIONALs from the 2026-04-29 audit |
| Social contest | **COMPLIANT** | 3 pre-flagged P2s, post-patch status unverified |
| Investigation / fieldwork | **COMPLIANT** | exemplar Lesson-4 routing; no new findings |
| Peninsula / victory | **COMPLIANT** | deterministic clocks, no dice |

The closeout (`...correction_and_ledger_staging.md`) is the keystone: it **corrects defects now live in the committed verdict files** (README staleness, faction probabilities, NERS-S rubric ambiguity, T6 over-claim) and **stages 13 editorial-ledger candidates (ED-865–877)** without filing them, because the editorial-ledger-consolidation handoff is active.

**Net:** the faction action layer is the sole non-compliant system and the priority remediation target; the other six are compliant under the lenient reading of Smooth (see §3.4). All findings are staged, none filed.

### E — Combat reframe + v31 (commits 13–14)

Two coexisting combat artifacts:

- **`combat_v31_proposal.md`** (dated 2026-05-25, committed as a *"pre-reframe baseline"*): a full eight-phase, Bout-centric rewrite that **replaces combat_v30 §§1–4 on ratification** (status: PROPOSAL — **not yet canon**). It preserves the d10/PP-717 substrate but its §12.3 composes an **uncapped sum of fractional-Ob modifiers** (Stance Counter + Reaction-aspect + Reading + coherence + weapon + Facing + Signal).
- **The reframe** (`reframe_blueprint.md` + four analysis files): restructures v31 around Jordan's 2026-05-28 vision — a **probability-weighted state graph** (deterministic Setup tier + probabilistic 6–10s Bout tier), facing→field-of-view perception (Facing-Ob becomes *emergent*), weapon ease-of-use handling, and an equip-loadout layer with named sets. **Piece 1** tested matchup-table derivability (Reaction-aspect derivable to 2 params; aspect-coherence partial via clusters; Stance Counter *not* derivable — keep authored). **Piece 2** specs a **σ-space + soft-cap (tanh) + state-gating** modifier system to fix the uncapped-stacking problem; σ-space (Option A) is accepted under Jordan's attribute-weight-equivalence principle (~0.30σ/pt; combat = thread = 0.302σ/pt verified).

**Net:** combat is in active design exploration. `combat_v30` remains canon and was diagnosed COMPLIANT; the v31 proposal is mid-flight and its reframe (which supersedes much of it) is specced but **not yet implemented into the proposal**. Per the open scene-combat handoff, this overview surfaces trade-offs only and recommends no direction.

### F — PT+Treaty build-readiness (commit 15)

A provisional ground-up review (dated 2026-05-26, committed 2026-05-28) that corrects the prior handoff framing: "two stubs need filling" is wrong — it is a **4–6 commit coupled build** (Passes A–F). The PT/Treaty canon docs exist and are clear; the sim does not (~half the substrate missing or stubbed). The v12c balance target (24.7 / 28.6 / 24.2 / 22.5) is a **five-mechanic equilibrium**; PT+Treaty alone (2 of 5) cannot reach it. Six findings F1–F6 (blocking + canon-vs-schema), F7 resolved in Pass A, and F8 enumerates **5 provisional-canon items requiring ratification**. Two open decisions: provisional-canon handling (a/b/c) and balance target (x/y/z), defaults declared but not applied.

---

## 3. Cross-thread reconciliation — conflicts & resolutions

Severity-ranked, worst-first. Each: what conflicts → which source is authoritative → action.

### 3.1 [HIGH] "B6 branch protection blocks commits" is stale, repeated across ~7 documents
Seven committed docs — engine v1 (§9), the AUDIT (§5), README batch-1, and **all four** resolution-diagnostic verdicts (faction, combat, threadwork, mass-battle) — stage ledger entries inline citing *"commits blocked by B6 branch protection."* But `roadmap_state.yaml` **D0 records branch protection disabled 2026-05-25**, and **15 commits landed directly on main on 2026-05-28** (no PRs) — main is demonstrably writable. The operative reason ledger entries aren't filed (stated cleanly only in the **correction file** §2/§3) is the **active editorial-ledger-consolidation handoff**, not branch protection. engine v1 §9 and the AUDIT §5 name *both* (B6 and the mid-consolidation); the reconciled v2 (§8) names neither (it stages for "a dedicated ledger session"). PI V2.2 `<core_rules>`/`<final_reminders>` and the architecture spec also still carry the B6-blocked caveat.
→ **Authoritative:** roadmap D0 + the commit log (protection off); the correction file (handoff is the real gate). **Action:** strike the B6-blocked rationale from the affected docs, PI, and architecture — the only operative blocker on filing is the consolidation handoff. This is a confidently-wrong repo-state claim — the project's named worst failure mode — propagated across the batch; only the correction-file closeout states the reason correctly.

### 3.2 [HIGH] `engine_replacement_reconciled` carries two P1 defects flagged by its own same-day audit
- **A1 — GD-2 misattribution.** Reconciled §0/§6/§7 cite GD-2 three times as canon "already mandating" a deterministic+stochastic *resolver*. GD-2 (`canon/02`) actually reads *"deterministic threat response precedes stochastic action **selection**"* — a selection-ordering rule, silent on resolution (verbatim-verified by the AUDIT). A manufactured canonical mandate underpinning the §7.1 resolver recommendation.
- **A2 — manufactured "0 P1."** The diagnostic rated faction with 5 P1 + 2 P1-canon findings. Reconciled reaches "0 P1" by closing ER-2 legitimately, then **dropping F4/F5/F8/F9, demoting F2 to a footnote, and silently downgrading F1**, mostly unargued.

→ **Authoritative:** the AUDIT (exact convolution + verbatim canon). The "do not replace engine" verdict is correct and corroborated; its **completeness claim and GD-2 justification are not**. **Action:** the det+stochastic resolver direction must stand on design merit (CK3/EU/KoDP precedent), not GD-2; re-issue the reconciled finding register with explicit in-scope/out-of-scope tagging for each diagnostic finding.

### 3.3 [HIGH] Committed faction verdicts state wrong numbers; corrected only in a separate note
`ners_verdict_faction.md` (R: FAIL) and `resolution_diagnostic_faction.md` state pivotal Domain Actions are *"P ≈ 0 / deterministic death spiral."* The correction file (C-2) fixes this to **P = 0.070 (Ob 3) / 0.010 (Ob 4)**, *"probabilistic, heavily loss-weighted"* — both earlier passes used a simplified die model ignoring the authoritative face-1 = −1 / face-10 = +2 rule. The verdict files were **not edited**; a reader of the committed verdict gets the retracted "deterministic" framing. The AUDIT (A8) recommends `[SUPERSEDED-BY]` markers on the upstream files — not applied.
→ **Authoritative:** the correction file (MC 300k, μ sanity-checked; AUDIT-confirmed by exact convolution = 0.0700 / 0.0100). **Action:** add `[SUPERSEDED-BY]` markers to the two faction files so the corrected number is canonical at source.

### 3.4 [HIGH] NERS-S rubric is internally contradictory; the batch's headline tally is unresolved
The diagnostic skill defines **Smooth** as "calculations consistent in methodology with other mechanics" yet also scopes consistency-checking out ("that's the mechanic-audit's job"). A canon contradiction is therefore simultaneously an S-failure and out-of-scope. The verdicts silently picked the lenient reading via the undisclosed phrase *"under resolution-fitness lens."*
- **Lenient-S** (resolution-smoothness only): **6/7 compliant**, faction non-compliant.
- **Strict-S** (includes consistency): **2/7 compliant** (social, investigation); of the other 5, one is mechanically broken (faction) and four are mechanically sound but documentation-inconsistent (combat, threadwork, mass battle, peninsula) — different remediation classes.

→ **Authoritative:** unresolved — the correction (C-3) flags it `[GAP]`, **Jordan ruling required; it swings the tally.** **Action:** the committed READMEs' "broadly compliant, 6 of 7" headline must be read with this ambiguity attached until ruled.

### 3.5 [MED] "F-finding" namespace collision
Faction findings are F1–F12 (resolution diagnostic); combat-proposal findings are F1–F7 (reframe). "F1" = *bare-stat faction pool* in one thread and *non-uniform combat-modifier impact* in the other; "F6" = *unbounded faction collapse loop* vs *combat per-moment complexity*. A genuine cross-reference hazard across committed docs.
→ **Action:** namespace the two sets (e.g., `FAC-Fn` / `CMB-Fn`) in any consolidated ledger or future reference.

### 3.6 [MED] v31 baseline and its own reframe-critique coexist, unreconciled
`combat_v31_proposal.md` (pre-reframe baseline, with the uncapped §12.3 stacking the diagnostic flagged) is committed beside the reframe + Pieces 1/2 that prescribe restructuring it (state graph, σ-space, derivable tables). The proposal revision implementing the reframe is **not done** (per reframe blueprint §9.2 sequencing). Separately, v31's F-findings derive from a **v31 diagnostic not present in the 24h commit set** (the resolution-diagnostic batch diagnosed combat *v30*; v31 is 2026-05-25) — a provenance gap.
→ **Authoritative:** combat_v30 (current canon, COMPLIANT). The committed v31 is the version its own companion docs supersede. **Action (no direction recommended, per handoff):** when v31 is revised, fold the reframe + Pieces 1/2 and re-run the resolution diagnostic on the new chassis. Locate or commit the v31 diagnostic that the F-findings reference.

### 3.7 [MED] Ledger candidates staged in three places, inconsistent numbering, incomplete, none filed
The correction stages 13 pre-numbered **ED-865–877** ("live ledger ends at ED-864"); the individual verdict files separately stage their own *"ED-NEW (assign on commit)"* entries; the AUDIT stages 3 more *"ED-NEW (A1/A2/A8)."* Same findings, multiple numbering schemes. Faction P2s **F4 (non-uniform stat damage) and F9 (shallow Parliamentary clock)** are present in the verdict but **absent from the correction's digest**. None is filed (consolidation handoff), and `canon/editorial_ledger.yaml` is **over-threshold (3,822 / 2,000 tokens)** with auto-fix blocked (compliance violation at bootstrap; tool stub at `compliance_check.auto_fix` line 527).
→ **Action:** the consolidation owner ingests one de-duplicated, renumbered set from ED-865; ensure F4/F9 and the three AUDIT entries (GD-2 strike, register re-issue, faction `[SUPERSEDED-BY]`) are included; ED-841 is **not** re-filed (already present).

### 3.8 [MED] The "Ob − 0.5" continuity fix is under-specified and leaves residual
Reconciled (§2/§7) specifies only the **Success-threshold** shift. The AUDIT notes (A5) a *consistent* correction must also shift Overwhelming (`2·Ob`), Partial, and the `net − Ob` magnitude gauge by 0.5, or the degree bands desynchronise; and (A3) that a ~**15% relative residual** persists at 1D Ob 2 (15.4%) and 2D Ob 4 (14.9%) — the finite-N/non-normality error continuity cannot remove, at exactly the small-pool stress points. The correction's ED-873 still calls it a clean "one-line edit (P3)."
→ **Authoritative:** the AUDIT (exact convolution). **Action:** spec the correction across all four degree bands + the gauge; tag it "one-line *per threshold*," not one-line total; note the irreducible small-pool residual (practical impact small — absolute probabilities are tiny).

### 3.9 [LOW] `roadmap_state.yaml` violated its own update discipline
Committed 2026-05-28 with the Phase 1→2 advance (`0a948ec3`), but the `updated: 2026-05-26` field was **not bumped**, despite the file's stated rule to bump on phase completion. Neither engine-side fix (continuity correction; faction resolver) appears in any phase (correction C-7).
→ **Action:** bump `updated`; slot the continuity correction (Phase-0-class) and the faction resolver (Phase 3/4, gated on the Ob-formula decision) — Jordan assigns phases.

### 3.10 [LOW→MED] PT+Treaty: scope corrected, target unreachable, ratifications pending
Forward-looking gaps rather than contradictions: the "two stubs" framing was wrong (4–6 commit build); v12c is unreachable with 2/5 mechanics; F8 lists 5 provisional-canon items needing ratification; §4 carries two open decisions (defaults declared, not applied). The review's §5 also documents the cross-session `CollisionError` (HEAD `82887dc` → `0a948ec` via the four infra commits, rebased clean) that links this thread to thread A.
→ **Action:** Jordan ratifies §4 (a/b/c, x/y/z) and the F8 items before Pass B; treat collisions as normal reconcile signals (refresh fetch-HEAD before each commit).

---

## 4. Consolidated decision queue for Jordan

Surfaced across the 24h work, gathered here:

1. **NERS-S ruling** (§3.4) — does Smooth include canon-consistency? Determines whether the batch verdict is 6/7 or 2/7. *Highest-leverage single decision.*
2. **Faction resolver direction** (§2C, §3.2) — aggregate the pool (mass-battle ER-9 model) or deterministic+stochastic (CK3/EU/KoDP). The one genuine engine-adjacent change. Prerequisite: the **Ob-formula contradiction** (FAC-F2) must resolve first.
3. **Continuity correction** (§3.8) — apply `net ≥ Ob − 0.5` *across all degree bands + gauge*; cheap, recommended, but complete the spec.
4. **Combat direction** — *deferred to the scene-combat handoff; no recommendation here.* When chosen, fold the reframe + Pieces 1/2 into the v31 revision and re-run the diagnostic.
5. **PT+Treaty** (§2F) — provisional-canon handling (a/b/c) and balance target (x/y/z); ratify the 5 F8 items.
6. **Roadmap decisions D0–D6** (§2A) — branch protection, M3, M4 soft-warn, task_manifests, session-log migration, scope-vocab unification.
7. **Ledger consolidation** (§3.7) — ingest one de-duplicated, renumbered ED-865+ set via the active consolidation handoff; raise the over-threshold ledger.

---

## 5. Open / blocked

- **Editorial ledger** is over-threshold and auto-fix is blocked; the consolidation handoff is the real gate on filing the ~13–16 staged findings (not B6).
- **B6 staleness** (§3.1) should be corrected corpus-wide (audit docs + PI + architecture) to stop propagating a false commit-blocking claim.
- **v31 proposal revision** is pending; the reframe + Pieces 1/2 are specced but not implemented into the proposal, and the v31 diagnostic that grounds the F-findings is not in the commit set.
- **F4 / F9** (faction P2) are missing from the correction's staged digest (§3.7).
- **Unverified statuses** carried forward: social SC3/4/5 post-patch; mass-battle MB1–MB4/MB9 resolution (no commit-log scan performed in the diagnostic batch).

---

## 6. Net repo state after 24h

- **Engine:** keep (corroborated three ways). One scale-local resolver change pending (faction); one cheap engine fix pending (continuity correction, spec to complete).
- **Faction action layer:** the single NON-COMPLIANT system — priority remediation; gated on the Ob-formula decision.
- **Personal combat:** `combat_v30` canon and COMPLIANT; PP-717 D2 propagation gap open (FAC/CMB ledger). `combat_v31` is an in-flight proposal whose reframe is specced but not yet implemented.
- **Threadwork / mass battle / social / investigation / peninsula:** compliant (lenient-S) or documentation-inconsistent (strict-S); each carries propagation/canon-cleanup items, none mechanically broken.
- **Infrastructure:** roadmap now surfaced at bootstrap; Phase 2 (0/11) in progress; D0–D6 open.
- **PT+Treaty:** Pass A landed; Passes B–F scoped and pending ratification.
- **Ledger:** ~13–16 findings staged, none filed; consolidation handoff is the gate.

---

## Sources consulted (this session)

Resolution diagnostic: `resolution_diagnostic_README{,_batch2}.md`, `resolution_diagnostic_correction_and_ledger_staging.md`, `ners_verdict_{faction,combat,threadwork,mass_battle,social_contest}.md`, the 7 `resolution_diagnostic_*.md` detail files (via READMEs + correction + AUDIT verbatim verification). Engine: `engine_replacement_audit.md`, `engine_replacement_reconciled.md`, `engine_replacement_reconciled_AUDIT.md`. Combat: `reframe_blueprint.md`, `attribute_weight_standard.md`, `derived_stats_audit.md`, `matchup_derivation_analysis.md`, `modifier_system_spec.md`, `combat_v31_proposal.md` (§0/§4/§7/§12 + TOC). Infra/PT: `references/roadmap_state.yaml`, `designs/audit/2026-05-26-pt-treaty-build-readiness/findings.md`, commit `281debe2`. Framework: `canon/02_canon_constraints.md` (GD-2, P-01–P-15), `skills/valoria-mechanic-audit/SKILL.md`, `skills/valoria-resolution-diagnostic/SKILL.md`.

`[CONFIDENCE: high]` — §3.1 (commit log + roadmap D0), §3.2/§3.3 (AUDIT exact convolution + verbatim canon), §3.4 (correction C-3 text), §3.7 (multi-doc cross-read). `[CONFIDENCE: medium]` — §3.6 v31-diagnostic provenance (absence inferred from the 24h set; may exist uncommitted/prior-session); the precise lenient-vs-strict per-system split in §3.4 pending the S ruling.
