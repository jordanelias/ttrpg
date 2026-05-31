session_id: 2026-05-30-combat-armature-build
session_close: 2026-05-30
status: complete
last_stage: canon-prose propagation (combat_v30 v1.7 + derived_stats §4.2 done; remainder handed off)
next_action: propagate remainder per designs/audit/2026-05-29-combat-armature/propagation_handoff.md (S2, params/core, params/combat, armour atom, ED entries) — ED entries FLAGGED for Jordan's ID-scheme choice (94-conflict backlog); then Martial Tradition mechanic
blockers: NONE blocking. Open items are Jordan design calls (ratify dagger-finish; confirm additive-Strength; ED-ID scheme; in-world naming) — Claude must not invent per the project-owner contract.

# Session Log — Combat Armature Build (continued) — 2026-05-30

**Scope:** simulation. **Handoff continued:** `2026-05-29-combat-armature-sigma-leverage` (was blocked on Jordan's resolution-structure decision — now resolved + built end-to-end). **Repo state:** fully committed; nothing staged.

## What this session did
Jordan settled the resolution structure and granted iterative design authority ("ratify and keep working"). Built, validated, ratified, and partially propagated the full combat armature on the σ-leverage engine — decisive multi-phase resolution, NOT attrition.

### Modules built + committed (tests/sim/v32-combat-balance/, all self-test green)
- **armour_axes.py** (373a1f2) — (attack-head × material) MITIGATION MATRIX reproducing the ratified weapon-vs-armour table exactly (no retcon) + material/coverage axes (4 tiers as presets) + σ-tempo penalty. 7/7. Finding: plate ~95% 1v1 dominance is HISTORICAL; counters = blunt/gaps/grappling, NOT fatigue (the "fatigue erodes the duel" claim was tested + struck).
- **grappling.py** (4741448) — close-combat substrate; unifies canonical actions (Disarm/Tie Up/Escape/Retrieve) + ST1 + the NEW dagger-finish (point→gaps, bypasses mitigation) = the THIRD plate-counter; fills ED-129. 6/6. Context-gated: 0% vs unarmoured spacer / 98% vs plated spacer.
- **damage_model.py** (3bba904) — GROUND-UP rebuild (Jordan: pretend no prior formula). Damage = Impact(STR+heft, ADDITIVE, no STR×weight mult) × Coupling(head-vs-armour, derived from material resistance-per-mode — the matrix EMERGES, folds in the +mod table) × Quality(degree, replaces crit-doubles). 1 calibration const (Success≈1 WI). 8/8. Wound model unchanged.
- **combat_resolution.py** (eb02561) — UNIFIED pipeline composing every module with real ground-up damage. 6/6. INTEGRATION FINDING: the earlier "duel finesse-race" was an artifact of abstract hit-counting; under real damage the mace's heft dominated → FIX (ratified L1): σ-leverage gates hit QUALITY (degree→damage), not just frequency.

### Ratified to canon-of-record (designs/audit/2026-05-29-combat-armature/RATIFIED*)
- A1 armour σ-tempo + A2 material/coverage axes (cbe4360); W5 point-gap + H1 handling (8c13469); D1 ground-up damage (6af989f); L1 leverage→degree (5423fd0). [Earlier in arc: R1/R2/S1/S2/ST1/W1–W4/C1.]

### Canon-PROSE propagation (the batched item — executed where highest-value + safe)
- **combat_v30.md → v1.7** (8eb95c0): R1 pool, D1 damage, W1/W5→Coupling note, L1; STR-mult struck; crit→Quality. SHA refreshed.
- **derived_stats_v30.md §4.2** (bed429e): S1 Stamina=(3×End)+(2×Spirit); resolves armour-atom S⚠. SHA refreshed.
- **Handoff ledger** (213ba1f, designs/audit/2026-05-29-combat-armature/propagation_handoff.md): the REMAINDER, deliberately not rushed at >75% ctx.

## REMAINING (next session — see propagation_handoff.md for exact anchors + method)
1. derived_stats S2 Spirit cross-ref. 2. params/core + params/combat residual damage/Stamina refs (+SHA). 3. armour atom S⚠-resolved note. 4. **Editorial-ledger ED entries — FLAGGED: the 94-conflict ID space is Jordan-adjudicated; Jordan chooses the ID scheme before writing.** 5. Optional: freshness_gate --update SHA re-baseline.

## Open for Jordan (design)
- Ratify the dagger-finish (the one unratified new mechanic) — grappling's plate-finisher.
- Confirm the additive-Strength choice in D1 (no STR×weight synergy) — built additive per the directive; reversible.
- Tunable seeds: DMG_SCALE + resistance grid, LEVERAGE_TO_DEGREE=3.5, the armour σ-tempo magnitude.
- In-world naming (traditions/cultures/armour/weapons) + whether to add a dedicated short-blunt beyond mace+tonfa.
- The Martial Tradition mechanic (seven-axis bias bundles → named sets) remains undrafted — natural next build.

## Method notes that held (carry forward)
Commit cited design specs STANDALONE before the sim that cites them (sim_gate freshness pre-check 404s otherwise — bit the damage module, isolated + fixed). Canon-prose edits: full anchor reads (never from memory), scope replacements to avoid collisions, verify each .replace landed, refresh the doc's canonical_sha as a co-file in the same [editorial] commit. Transient GraphQL 404/FORBIDDEN/CollisionError = routine; collision-safe loop with idempotency guard.
