# Canon-Prose Propagation — Status & Remaining Ledger (2026-05-30)

Propagation of the ratified combat-armature decisions into canonical prose. **Done this session; remainder is a precise executable ledger below** (handed off rather than rushed — editing the editorial-ID space + remaining docs deserves full headroom). `[CONFIDENCE: high on what's done — each edit verified anchor-replaced + committed.]`

## DONE (committed)
- **combat_v30.md → v1.7** (`8eb95c0`): R1 pool (`max(5, History+6)`, Agility-independent, supersedes the (Agi×2)+History+3 form + PP-247); D1 damage (`Impact×Coupling×Quality`, supersedes the STR-multiplier formula; STR-mult lookup struck; crit-doubles-PP-211 → Quality); W1/W5 weapon-vs-armour table annotated subsumed-by-Coupling (values retained as the relationship reference); L1 leverage→degree note. `canonical_sha` refreshed.
- **derived_stats_v30.md §4.2** (`bed429e`): S1 Stamina = `(3×End)+(2×Spirit)` (formula block + range 5–47 + summary-table row + audit-mapping annotation); armour stays a per-action drain modifier (resolves the armour-atom S⚠). `canonical_sha` refreshed.
- All **RATIFIED addenda** committed earlier (R1/R2/S1/S2/ST1/W1–W5/A1/A2/D1/L1/H1): `designs/audit/2026-05-29-combat-armature/RATIFIED*.md`.

## REMAINING (executable ledger — do with full headroom)

1. **derived_stats_v30 — S2 (Spirit expanded).** S1 now makes Spirit feed Stamina; S2 ratified a broader Spirit role. Add a short note in §4.2 / the Spirit rows (≈L164, L225, L531–535) that Spirit now contributes to Stamina (conditioning-of-will) in addition to Resolve/Inspiration-cap and Thread-Fatigue. No formula change beyond S1; this is a cross-reference. *Anchor: the Spirit summary-table rows.*

2. **params/core.md — Spirit + residual damage refs.** (a) If params/core states a Stamina/Spirit formula, align to S1. (b) Search params/core for any `STR × multiplier` / `weapon modifier doubled` / crit damage language and annotate as superseded by D1 (the combat_v30 §damage is the source-of-truth; params/core should point to it). *Anchors: grep params/core for `multiplier`, `× 2`, `crit`, `Stamina`, `Spirit`.* Likely 1–2 surgical edits + SHA refresh (`canonical_sha__params__core_md` if tracked).

3. **params/combat.md — weapon-vs-armour / damage.** Grep for the weapon-vs-armour mod table or damage formula; annotate subsumed-by-Coupling / superseded-by-D1, pointing to combat_v30 §damage. SHA refresh (`canonical_sha__params__combat_md`).

4. **The armour atom** `references/atoms_pending/2026-04-25/valoria_master_document/14__3-4-armour.md`: add a one-line note that the **S⚠ flag is RESOLVED** (ratified S1 Stamina = 3·End+2·Spirit; armour = per-action drain, not base reduction) and that material/coverage axes + the mitigation matrix (A2) now underlie the four tiers. *(Atom is pending-prioritization, low-risk.)*

5. **Editorial-ledger ED entries — HANDLE CONSERVATIVELY (Jordan-adjudicated).** Record R1/R2/S1/S2/ST1/W1–W5/A1/A2/D1/L1 in the editorial ledger. **The ID space has a 94-conflict backlog under Jordan's adjudication — do NOT mint contested IDs.** Options: (a) reserve a clearly-new high ID block for the armature decisions and flag for Jordan; or (b) record them under a single dated armature-batch marker rather than individual ED-NNN IDs. **Flagged for Jordan to choose the ID scheme before writing.**

6. **SHA hygiene:** the per-doc `canonical_sha__…` fingerprints in canonical_sources.yaml were already drifted before this session (the freshness gate keys off the manifest, not per-doc); a `freshness_gate --update` pass would re-baseline all of them. Optional housekeeping.

## Method reminder (so the remainder stays safe)
Fetch each doc → find exact anchors (print context) → surgical string replace, scoped to avoid collisions (e.g. multiple `×5`/`×2` refs) → verify the replacement landed (`.replace` no-op trap) → commit via `task_gate('editorial')` + `[editorial]` scope + refresh that doc's `canonical_sha` in the same commit (co-file) → verify via re-fetch. Collision-safe loop with an idempotency guard.
