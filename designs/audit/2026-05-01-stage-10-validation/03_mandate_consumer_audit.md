# Mandate-Consumer Audit (post-PP-686 v2)

**Date:** 2026-05-01
**Session:** 2026-05-01-stage-10-validation
**Trigger:** session_log next_action item 7 — "Mandate-consumer audit (catch leftover Mandate references post-PP-686 v2)"
**Source:** PP-686 v2 (`designs/provincial/faction_behavior_v30.md`) §3.4 Popular Support + §3.5 Legitimacy supersedes Mandate-as-single-scalar
**Search:** `Mandate repo:jordanelias/ttrpg` → 572 matches across project
**Scope:** canonical params files only — `params/`. Designs/, archives/, audit/, sims/, history/, skills/, tools/, references/ excluded as design-time, history-time, or tool-time references not requiring migration.

---

## §1 Summary

| Bucket | File count | Mandate refs | Migration burden |
|---|---|---|---|
| CONSUMER (mechanics that read/modify Mandate) | 9 | 188 | per-site classification needed |
| REFERENCE (named in tables, examples, prose) | 8 | 56 | mostly mechanical replacement |
| **Total in canonical params** | **17** | **244** | |

This audit lists every CONSUMER site and classifies each by which PP-686 v2 component it should migrate to:

- **L (Legitimacy)** — institutional procedural authority; slow-moving; built by procedural events; eroded by violations (§3.5)
- **PS (Popular Support)** — active populace backing; faster-moving; driven by attributed outcomes + cascade fidelity (§3.4)
- **strictness** — derived: `clamp(0.4 + 0.5·(L/7) − 0.3·(PS/7), 0, 1)` (§3.6)
- **L+PS** — both, or formula combining
- **L_proxy** — backward-compat shim where the literal `Mandate` value should be reconstructed for one-shot rolls; treat as `(L + PS)/2` clamped to faction's printed Institutional Mandate range. Use sparingly; prefer explicit L or PS routing.

The classifications here are **proposed**; Jordan signoff required before commits to canonical params.

---

## §2 Consumer files — per-site migration plan

### §2.1 `params/factions/stats_1_7_scale.md` (38 refs)

The faction stat block `Mandate / Influence / Wealth / Military / Intel / Stability` is the canonical 1-7 stat list. PP-686 v2 splits Mandate into two stats.

**Proposed:** stat block becomes `Legitimacy / Popular_Support / Influence / Wealth / Military / Intel / Stability` (7 stats). All authored faction stat values need to be split into L+PS pairs.

| Site type | Migration |
|---|---|
| BG faction starting stats (e.g., "Varfell BG Mandate 3") | **Author decision** — split each printed Mandate into L and PS values; Jordan creative call per faction |
| Roll pools (e.g., "Mandate vs Ob 2") | Default to **L** for procedural actions, **PS** for populist/active actions; per-site judgment below |
| Stat-modify effects (`Mandate −1`) | Default to **PS** for outcome-driven losses (most are populace reaction); **L** for procedural-violation losses |

Crown Royal Decree (L79) "Mandate vs Ob 2" — procedural authority → **L**.
Church Excommunication (L80) "Mandate vs target Mandate" — religious-procedural authority → **L** for both sides.
Church CI Territorial Seizure (L81) "Mandate vs floor(owner's Mandate / 2) + 1" — institutional Church authority → **L** (Church side); **L** (target — institutional defence).
Restoration Movement (L82) "Mending Mandate prerequisite: Mandate ≥ 1" — populist mending → **PS** (faction needs popular base to mend).
Baralta Suppression (L103) "Church Mandate −1/season while Mandate ≥ 4" — institutional erosion → **L**.

### §2.2 `params/bg/faction_actions.md` (30 refs)

Action-resolution rolls. Most "Mandate vs Ob" rolls are procedural — use **L**. Stability-impacting failures are PS reactions:

L17 "Mandate vs Ob = floor(controlling faction Mandate / 2) + 1 + Fort Level" (military hold) → **L** vs target **L**.
L32 "Mandate vs Ob = floor(territory Stability / 2) + 1" (territory action) → **L**.
L86 "Mandate vs Ob 2 (−1 Ob if PI ≥ 5 → Ob 1 minimum)" (Crown legislative) → **L**.
L95 "Failure | Stability −1 + Church Mandate +1" (Crown failure benefits Church institution) → Church **L** +1.
L106 "Majority Support | PI +1 + Hafenmark Mandate +1" — popular victory → Hafenmark **PS** +1.
L116 "Influence vs Ob = floor(target Mandate / 2) + 1" — Influence rolls vs target's institutional position → target **L**.
L132 "Mandate vs Ob = floor(territory Prosperity / 2) + 1" + L133 "Max floor(Mandate / 2) + 1 active Charters" — economic governance, **L**.

### §2.3 `params/bg/ministry.md` (24 refs)

Ministry's "Mandate" is institutional integrity of the administrative apparatus — pure **L** in nearly all consumer sites.

L10 "| Mandate | 3 | Institutional legitimacy of the administrative apparatus |" — the description literally calls it institutional legitimacy → **L**.
All "Ministry Mandate < 2" gates → **L**.
"Ministry Collapse (Mandate 0)" → Ministry **L** = 0.
Cross-faction "Crown Mandate ≥ 4" gates (L47) → Crown **L**.

Ministry has no Popular Support component because Ministries are not populist actors. Migration: Ministry stat block uses L only (PS=N/A).

### §2.4 `params/bg/institutions.md` (21 refs)

Institutional gates and BG mechanics. Pure-procedural → **L** throughout.
"Roll: Mandate vs Ob 3. Once per season" (L117, L146) → **L**.
"Failure | PI = 0. Stability −1. Church Mandate +1" (L124, L153) → Church **L** +1 (institutional vacuum benefits Church).

### §2.5 `params/bg/parliament.md` (16 refs)

Crown Policy is a procedural-legitimacy mechanic.

L5 "Full Parliament. Crown Policy requires Mandate ≥ 4" → **L** ≥ 4.
L16 "Crown may issue one Policy if Mandate ≥ 4" → **L** ≥ 4.
L21 "Mandate Recovery (PP-174)... Mandate +1" (Govern Overwhelming in own capital) — recovery from procedural action → **L** +1.
L26 "All Domain Actions targeting another faction's Mandate stat use Ob = floor(target Mandate / 2) + 1" — must be specified per DA (PP-296). Default for "Mandate-suppression" DAs targeting institutional structures → target **L**; for populist attack DAs → target **PS**.
L42 "Institutional Mandate Uphold/Appease (PP-189)" — institutional → **L**.

### §2.6 `params/bg/ci_seizure.md` (12 refs)

Church Influence + seizure mechanics. Church Mandate is institutional/religious authority → **L**:

L5, L11, L20, L32, L33, L55: all Church-Mandate gates → **L**.
"Political pool = Mandate + floor(CI/20)" (L19) for Church motions → **L**.
"Political pool = Mandate − floor(CI/30)" (L20) for non-Church anti-Church motions → those factions' **L**.
"Political pool = Mandate (no CI modifier)" (L21) → **L**.

### §2.7 `params/bg/stress_patches.md` (9 refs)

Mixed:

L18 "Church Prominence = Church Mandate > controlling faction Mandate" — institutional contest → both **L**.
L24 "Hafenmark Structural Suppression (passive -1/season from Baralta Mandate >= 4)" — institutional → Baralta **L** ≥ 4.
L29-L31 "Submission + Mandate 0 Ruling" — submission is populist surrender (the populace stops defending the faction) → **PS** = 0 ruling. **Author decision**: this could equally be L=0; Jordan must decide which represents "the faction has nothing left."
L70-L71 (sub-unit roll variance tables) → split into per-stat author values.

### §2.8 `params/bg/tracks.md` (11 refs)

AER + faction-track mechanics. Mostly **L** (institutional):

L11 "Mandate vs Ob = floor(AER/2)+1" (Cardinal Temperance AER advance) → **L**.
L30 "Ob = floor(target Mandate / 2) + 1" → target **L**.
L54-L56, L82-L84 (faction-track tier effects) → **L** for institutional effects, **PS** for popular reform-track entries.
L135 "All factions: Mandate check at Accounting (pool vs Ob 1)" — Tension state Accounting roll. Pool is faction's institutional pool → **L**. But the "failure: Mandate −1" → which? **Author decision**: tension-state losses likely affect both; default **PS** −1 (popular reaction to crisis); leave **L** untouched unless specified.
L137 "All factions: Accord −1 + Mandate check Ob 2" — Crisis state. Same as Tension; **PS** at risk.

### §2.9 `params/factions_personal.md` (11 refs)

The PERSONAL-scale view of faction stats. PP-686 v2's **L+PS** split is a faction-level mechanic; from a personal-scale character's perspective, they observe a single integrated "Mandate" that's a function of both.

**Proposed:** add a derived `personal_mandate_view = round((L + PS) / 2)` column. Keep "Mandate" as personal-scale shorthand pointing to this derived value. Personal-scale rolls don't need to distinguish L from PS — they're at a different scale.

L10 "| Mandate | Public legitimacy and popular support |" — note: the description ALREADY says "legitimacy and popular support." This row should split into two columns post-migration; the personal_mandate_view shim sits alongside.

### §2.10 `params/bg/phases.md` (2 refs)

L54 "Church Prominence update... any territory where Church global Mandate exceeds that territory's controlling faction" → both **L** (institutional Church authority vs institutional controlling-faction authority).
L76 "Crown upheld Mandate 2+ consecutive seasons →+1" (Torben Loyalty modifier) — sustained procedural authority → **L**.

---

## §3 REFERENCE files (no migration burden, only nominal renames)

These files mention Mandate in tables, examples, victory conditions, NPC priority trees, etc., but do not contain mechanics that "consume" Mandate. Migration is mechanical text replacement once the bucket above is settled:

- `params/factions/riskbreakers_identity.md` (16) — Crown ability descriptions
- `params/bg/ed_resolutions.md` (9) — same
- `params/bg/victory.md` (8) — victory conditions; "Hafenmark Mandate ≥ 4" → **L** ≥ 4 most likely (constitutional victory is procedural)
- `params/bg/core.md` (7) — table headers, Tension/Crisis state checks (covered by tracks.md classification)
- `params/bg/npc_priority_trees.md` (5) — NPC decision priorities
- `params/bg/npcs_special.md` (5) — special NPC clauses
- `params/scale_transitions.md` (3) — examples
- `params/bg/parliament.md` reference subset

---

## §4 Migration sequencing recommendation

**Phase 1 (this audit, no commits):**
- Survey complete; per-site classifications in §2 above.
- Hand off to Jordan for ratification.

**Phase 2 (after Jordan signoff):**
- params/factions/stats_1_7_scale.md: split Mandate column into Legitimacy + Popular Support; author per-faction L+PS values from existing Mandate.
- params/factions_personal.md: add personal_mandate_view derived column; update faction stat block.
- params/bg/core.md: strike "Ethical Framework Modifiers" section (PP-686 v2 §3.4/3.5 supersede).
- All consumer files: per-site migrations from §2.

**Phase 3 (after Phase 2):**
- Reference files: nominal text replacements.
- Update editorial ledger ED-755 (P1 blocker) with resolution note.
- Promote PP-684/685/686/687/688 PROVISIONAL → canonical.

**Phase 4 (deferred):**
- Author Mission/cascade/temperament for 6 factions + 30-50 territories (session_log next_action item 5; creative authoring).
- Per-system Key migration (PP-687 phased rollout, item 6).

---

## §5 Open questions for Jordan

1. **§2.7 Submission ruling (PP-475):** "If Submitting faction's halved Mandate = 0: Submission supersedes Faction Collapse." Should the threshold migrate to L = 0, PS = 0, or `(L + PS) / 2 = 0`? (Recommends: PS = 0, since submission is populist capitulation.)
2. **§2.5 PP-189 Institutional Mandate Uphold/Appease:** the printed Institutional Mandate per faction is currently a single value. Does it migrate to per-faction L and PS pairs, or remain single (L only)? (Recommends: L only, since "Institutional" is in the name.)
3. **§2.4 Failure clause "Church Mandate +1":** when a non-Church action fails and benefits Church institutionally, is that gain in Church L only or Church PS too? (Recommends: L only — institutional vacuum benefits Church procedural authority, not populist support.)
4. **§2.9 personal_mandate_view formula:** is `(L+PS)/2` the right combination, or should the formula be `max(L,PS)`, `min(L,PS)`, or weighted? (Recommends: average; but Jordan's call.)
5. **Strictness threshold gates:** several BG mechanics gate on `Mandate ≥ 4`. Should these become `L ≥ 4`, `PS ≥ 4`, or `strictness ≥ 0.5`? (Recommends: per-mechanic — Crown Policy = L ≥ 4; populist actions = PS ≥ 4; deviation cost gates = strictness threshold.)

---

## §6 Editorial entries (proposed, not yet logged)

These would be added to canon/editorial_ledger.yaml after Jordan ratifies the audit:

- **ED-779** P1: "Mandate→L+PS migration per Mandate-consumer audit; per-site classifications in designs/audit/2026-05-01-stage-10-validation/03_mandate_consumer_audit.md §2"
- **ED-780** P2: "Update reference files (params/factions/riskbreakers_identity.md, ed_resolutions.md, victory.md, core.md, npc_priority_trees.md, npcs_special.md, scale_transitions.md) with nominal Mandate→L/PS replacements per audit §3"
- **ED-781** P2: "Author personal_mandate_view derived field in params/factions_personal.md per audit §2.9"
- **ED-782** P3: "Resolve open questions §5 (5 items) in next session"

ED-755 (existing P1) gates on this audit's completion.

---

## §7 Status

- **Survey:** complete; 17 canonical-params files audited; 9 consumer + 8 reference.
- **Per-site classifications:** drafted in §2.
- **Open questions:** 5 in §5 awaiting Jordan.
- **No canonical changes committed.** All migrations gate on Jordan signoff.
- **Carry-forward:** Phase 2 migrations enter the next session's queue.
