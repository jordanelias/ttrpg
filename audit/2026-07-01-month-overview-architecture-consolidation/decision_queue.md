# Jordan Decision Queue — 2026-07-01

## Status: SUPERSEDED AS A LIVE SURFACE (2026-07-05, ED-IN-0006 → ED-IN-0009) — dated snapshot; the live decision surface is workplan v6 §5 (`designs/workplans/valoria_master_workplan_v6.md`), whose tiered register carries every still-open item below with a pointer. Items 1–3 refreshed in place at supersession (they reflected pre-R2 combat physics); 6/18/20 were already struck.

Everything below is **surfaced, not decided**. The consolidation session touched none of
these outcomes. Ordered roughly by how much downstream work each unblocks.

## Scene combat (Track 2 + phases)

1. ~~**wt/spd cost-path de-leak**~~ **REFRESHED 2026-07-05 (ED-IN-0009):** superseded by the
   R2 closing-distance redesign (MERGED PR #72) + R3 weapon-model consolidation (RATIFIED
   plan-of-record). The Track-2 residual survives in R3's terms: damage-path
   ready-except-spear, tempo-path NOT ready (double-counting) — resolved through the R3
   JD-1..8 decision set, sequenced in workplan v6 §4-PC.
2. ~~**`WP.reach()`/`WP.authority()` single-source home**~~ **REFRESHED 2026-07-05:** the
   prepped comparison stands; current recommendation post-R2/R3 is retire-docstrings
   (workplan v6 §4-PC Track-2 residuals) — rule it with the R3 JDs, not as a standalone.
3. ~~**Scene-combat Phase 4a/4b/4c / Phase 5 / WS-7**~~ **REFRESHED 2026-07-05:** context
   superseded — phase4_5 is now explicitly sequenced AFTER the R3 U-series + player-input +
   ED-911 slots (workplan v6 §4-PC; gated on ED-911 + WS-7); the plan file itself is
   unchanged and still the content source.
4. ~~**ED-1042**~~ **STRUCK 2026-06-28** (superseded_by ED-1021; ledger canon/editorial_ledger.jsonl) — reconciliation ticket ED-PC-0004; residual wound-Ob / dead pool_penalty drift re-filed as ED-PC-0005 (2026-07-07).
5. **ED-1050 residual** — re-export RESIST/GAP_EXPOSURE/gap-game logic to
   `weapon_resource.gd`/`strike_module.gd`; Key-log parity stays known-red until done.
   (2026-07-02 docket adjudication, ED-IN-0002: this is the ONLY still-open part of
   ED-1050 — the ADEF_THRESHOLD monotonicity question is separately RESOLVED, config.py
   and combat_config.gd verified byte-identical monotonic; don't re-raise it as a decision.)

## Mass battle / simulation

6. **Coordinate-field flip (field-ON)** — ~~unratified candidate behind default-OFF toggles;
   gauge OFF 5/13 → ON 4/13 with new H2/H9 divergences (PR #45).~~ **RESOLVED — Jordan-ratified
   2026-07-02 ("yes, field movement is default."), executed as ED-1089:** FIELD_MOVEMENT/
   PC_NODE_COHESION now default ON; grid stays the byte-exact oracle via explicit `=0` pins (CI
   gate updated accordingly); field golden digests re-recorded post-LC-8. The gauge-band gap was
   known and accepted at ratification (attributed to unbuilt control-hierarchy depth, not the
   substrate).
7. **`orchestration.py` decomposition Stages 3-6** (ED-1043) — each stage gated.
8. **Sim degenerate win-share** — a seeded batch yields one faction ~87%, two at 0%, and
   nothing flags it; balance tuning + a wider regression oracle are design calls.
9. **`sim/` vs `tests/sim/` vs `tests/sim_framework/` rename** — documented collision,
   high blast radius (PR #49).

## Godot conversion

10. **The strategy doc's 8-item open register** (`designs/audit/2026-06-10-godot-conversion-strategy/`)
    — downward Key delivery (ED-1006), Python end-state, faction-stat inversion, Key runtime
    form (needs K8), autoload ruling, first module target, D6 Church 4/4-vs-5/5, standing
    dockets. All unruled as of 2026-07-01.
11. **Gate-0 preconditions** — KeyStore v2 (valoria-game frozen since 05-04), spine base
    classes, RNG service, K8 performance verdict. None executed.
12. **ED-1051** — module-contract closure priorities: 11/27 modules doc:null (start with
    `engine_clock`, the temporal spine), 13/27 resolvers [ASSUMPTION]-grade (both counts
    grew since 2026-06-30 — re-measured 2026-07-02, docket adjudication ED-IN-0002). The
    top-priority module now has a head start: `engine_clock` has a CANDIDATE home doc
    (`designs/architecture/propagation_spec_v1.md`, ED-1093, CANONICAL) — its `gap_notes`
    explicitly keep `doc: null` unflipped until this item is ruled. Authoring is
    effectively done for `engine_clock`; only ratification/ordering remains for it, and
    the other ~10 modules + 13 resolvers are untouched.

## Canon / editorial

13. **Attribute-roster ratification** — `descriptor_registry.yaml` 9-attribute roster IN
    FLUX; alias folds (Cognition→Acuity, Spirit→Will) are Jordan-vetoable; `agg.*`
    placeholders await the R7/derived-stats §14 migration decision. The names_index mirror
    added this session is warn-tier only, pending this ruling.
14. **`needs_jordan` ledger items** — the open set in `canon/editorial_ledger.jsonl`
    (includes ED-1051; NPC naming; ID-collision reconciliations).
15. **contest_rebuild Stage 1+ gates** — each stage ratified individually (Gate 0 ratified
    2026-06-30; ED 1055-1079 / PP 800-809 reserved).
16. **`contest.py` fabrication-debt triage** — 19 uncited constants block the J-31
    terminology propagation into code.
17. **values_master.yaml successor** — quarantined this session (step 6); decide: port the
    generator to working-tree reads and regenerate, or retire it in favour of typed
    engine-params exports (step 8's discipline) as coverage grows.

## Orchestration / workflow (new this session)

18. **~~Propagation-spec authorship~~ — RATIFIED 2026-07-02 (pre-staged, ED-1093/ED-1094).**
    `designs/architecture/propagation_spec_v1.md` (ED-1093, CANONICAL) now exists —
    aggregate-up transform, distribute-down transform, ordering/determinism spine
    (supplies `engine_clock`'s candidate home doc; the `doc: null`/[ASSUMPTION] grade stays
    unflipped until ED-1051 is separately resolved), and a termination guarantee that is
    explicitly TERMINATION-ONLY (cross-tick convergence NOT proven, conditional on an
    unspecified `decay()` + the D.6 double-count / OF-D6 ruling). Went through one full
    adversarial round (3 independent critics found real holes; repair pass closed them; 2
    independent re-verifications confirmed the repair) plus a whole-corpus Fable review that
    retired the OF-PERPETUAL framing (ED-749 hysteresis already rules the flagship
    perpetual-scene risk; residual is a sim-compliance hygiene audit, OF-HYSTERESIS-AUDIT, not
    a Jordan decision) and surfaced RNG-MODEL-COLLISION (three unreconciled RNG contracts in
    the corpus). Per ED-1094 merge-ratifies-by-default, the flip to CANONICAL was pre-staged
    in the same PR as the ratifying merge rather than left as after-the-fact text — its own
    explicit PROVEN-vs-NOT-PROVEN scope markers and open flags stand as ratified-with-caveats,
    not resolved. See the doc's own §5 consolidated decision queue for the ranked open items
    (OF-7/OF-B1 amendments first, then D.6/OF-D6, decay() spec, RNG-MODEL-COLLISION, cap
    constants, ORD-3/ORD-4).
19. **Agent-Teams / subagent-roster adoption** — the ingested workflow spec (§6-§7)
    prescribes promoting recurring roles into `.claude/agents/` only on recurrence; none
    created this session. Decide if/when a standing conformance-scanner or emergence-auditor
    role has recurred enough to earn a definition.
20. **~~Doctrine ratification~~ — RESOLVED 2026-07-02.** `holonic_container_doctrine_v1.md`
    ratified (ED-1083, ED-1094) via the newly-adopted merge-ratifies-by-default convention:
    Jordan's approval + merge of PR #55 (which contained the doctrine) constitutes
    ratification of its PROPOSED contents. Item 18/J-38 (the propagation-spec transform the
    doctrine defers) is now ALSO ratified — see item 18 — under the same convention.

## Housekeeping

21. **Stale merged branches** (`design/scene-combat-v1`, `origin/scene-combat-track2-cleanup`)
    — deletion offered, not performed.
22. **Duplicate compilation homes** (found during the ED-1084 Combat Pool sweep): the
    Revision-2 (2026-04-15) compilations exist twice each —
    `designs/architecture/canonical_registry.md` ≡ `references/valoria_canonical_definitive_r2.md`
    and `designs/architecture/complete_systems_reference.md` ≡
    `references/valoria_complete_systems_r2.md`. All four now carry PARTIALLY
    SUPERSEDED banners (their combat sections predate d+σ); decide which home each pair
    keeps and which copy retires to `archives/`.
23. **Live ledger entries carrying pre-restructure paths** (ED-640/644/648/649/650/651/658):
    the revived dependency checker resolves them via `references/restructure_ledger.md`
    (INFO, not violations); rewriting the entries' `affects` paths in the append-only ledger
    is a canon edit reserved for Jordan.

## Docket adjudication (2026-07-02, ED-IN-0002)

24. **ED-1052's broader question — typed params layer scope/fence** (distinct from item 17,
    which is narrowly about `values_master.yaml`'s own successor). Still fully open: whether
    to build a typed, Godot-ingestible layer over `params/*.md` prose, and if so, whether to
    fence it to genuinely-settled non-combat values only (the original recommendation) or
    another scope. `tools/export_engine_params.py` (this session) is NOT that layer — it
    mechanically mirrors the live `config.py` Class-C oracle, sidestepping the settled-vs-
    in-flux dilemma entirely rather than resolving it, and by its own docstring does not
    parse `params/*.md` prose at all. Worth using as the template for whatever comes next,
    but the scope decision itself is untouched.
25. **ED-1054's residual, narrowed** — retired-session-file relocation (part iii of the
    original residual) is DONE via ED-1084 (`deprecated/session_machinery/`). Still open:
    (a) relocate the ~850KB of narrative markdown mislabeled as tests
    (`tests/emergent_arc_skeleton_test_2026-04-17_batch*.md`,
    `tests/sim_framework/session_audit_2026-04-19.md`) to `designs/audit/` or `archives/`;
    (b) regenerate `sim/README.md` (currently self-flags stale rather than being rewritten
    accurate), `sim/CONVENTIONS.md` (still `[PROVISIONAL — Pass 2l armature scaffold
    2026-05-17]`, describes stub anatomy the package has outgrown), and `tools/README.md`
    (missing `currency_consistency_check.py`, `ci_module_shape_check.py`,
    `export_engine_params.py`, `validate_ed_citations.py`).
