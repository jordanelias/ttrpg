# Refutation notes — finding `sim-conviction-taxonomy-stale`

Role: adversarial skeptic. Verdict: **REFUTED** (literal fact true; finding-as-framed does not hold).
Intent: **DELIBERATE**. Revised severity: **P3** (from P1). Novelty: not novel-untracked — root is KNOWN-TRACKED (ED-1006, open).

## What the code actually says
`sim/personal/conviction.py` lines 46–49: `CONVICTIONS = ("Faith","Order","Reason","Equity","Precedent","Autonomy","Continuity","Community","Warden")` — 9 names.
This is exactly the legacy 9-set (`ED-641`, resolved 2026-04-17: "Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity/Community/Warden"; `ED-515` the 7-core). Canonical PP-684 set (`designs/personal/conviction_taxonomy_v30.md §2`) is 13: Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor. Reason→Scholastic, Autonomy→Liberty, Continuity→composite are superseded labels (`taxonomy_v30 §6`). So the literal claim "tuple is legacy-9 not canonical-13" is **TRUE**.

## Why the finding-as-framed fails

1. **Sim is faithful to its cited still-canonical source section.** `conviction_track_v1.md` header (line 2) supersedes **only §1** (taxonomy); it explicitly states **§2 Scar table + §3 Thread-Operation matrix "remain canonical pending PP-718 review of weight-scaling under PP-684."** The §3 matrix (lines 70–77) — the section the sim implements and its comment (lines 44–45) explicitly says it tracks ("the canonical names used in §3 Thread Operation matrix") — **still uses legacy column names** (Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity). The sim adds Community+Warden per ED-641 = 9. The sim mirrors the un-migrated-but-still-canonical §3; it is not lagging a migrated design.

2. **Causal story inverted.** The finding says the sim "has not been migrated despite the design-level vetting passing." The vetting that passed (`taxonomy_v30 §7`) is of the taxonomy **doc**, not the §3 Scar matrix. Canon itself has **not** rewritten §3 over 13 Convictions. So this is an upstream canon-authoring gap, not a sim porting failure — fixing the sim tuple in place would violate ED-1050 port↔oracle discipline (fix canon, then re-export).

3. **Safeguard present → DELIBERATE.** Comment lines 42–45 explicitly document the legacy/superseded relationship and state the choice to list §3 names. The first-line "Canonical 13-Conviction set" label is sloppy/misleading (it then lists 9) but non-load-bearing; the intent is stated.

4. **Root is KNOWN-TRACKED.** `ED-1006` (status **open**) flags the "3-way piety/conviction_track name collision (substrate SS8.4 vs conviction_track_v1 vs scene/conviction_track_v30)" and conviction_track_v1 "header-CANONICAL but absent from canonical_sources." The conviction subsystem's canonical-currency confusion — the true upstream cause — is already on Jordan's plate. Finding cites neither ED-1006 nor PP-718.

5. **Severity P1 overstated → P3.** `conviction.py` is a cyclic-pair **stub** (module-level `_conviction_state`, multiple `[ASSUMPTION]` markers, no world registry, not wired into `mc_v18` campaigns). Godot port is 1/27 modules (personal_combat only; CLAUDE.md §6) — conviction is **not** in the ported slice, so "Godot-validating reference" is aspirational, not live. The gap is currently **inert**: no running campaign or Godot slice consumes it.

## Residual real issue (preserve, don't inflate)
Once §3 is migrated to 13, the sim's `if conviction not in CONVICTIONS: return magnitude=0` (line 189) would silently no-op Scars on Honor/Virtue/Identity/Authority/Utility — including Honor, load-bearing for sovereign/lowenritter templates (`taxonomy_v30 §8 D1`), suppressing the crisis→arc-transition engine (Ω personal-transformation clause). Genuine emergence debt, but **blocked on canon §3 authoring first**, module inert today → P3 not P1.

## North-Star re-judgment
Fixing the sim tuple alone widens no meaningful choice — it would desync from still-canonical §3. The choice-widening work is authoring the §3 Scar matrix over 13 Convictions (canon), tracked-adjacent via ED-1006/PP-718, then re-export. Finding mis-locates the lever.
