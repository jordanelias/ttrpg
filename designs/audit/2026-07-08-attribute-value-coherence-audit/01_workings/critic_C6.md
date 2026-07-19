# Critic pass — C6 (Code constants & the export pipeline)

Antagonist relay over `dossier_C6.md` (independent read-only verification).

## Verdicts

| target | verdict | reason (condensed, evidence-cited) |
|---|---|---|
| C6-F1 | **uphold** | keys.py:84 defines Target.stat_deltas; _validate (:300-356) checks impact_vector against AXES (:321-327) but has no stat_deltas check anywhere. P2 right (unvalidated field, not yet a live wrong value). |
| C6-F2 | **soften** (claim split; see M1) | Exporter scope gap confirmed (derive() at export_engine_params.py:69 serializes only config.CFG). But "currently byte-identical" is FALSE for RESIST: core.py:86-89 (post-2026-06-30 grounding edit, 4 cells changed per its own comment) reads cloth={.12,.45,.12}, mail.shear=.85 vs combat_config.gd:34-38's pre-edit cloth={.10,.35,.15}, mail.shear=.80 — an active materialized divergence, and a KNOWN-TRACKED one (ED-1050 residual per combat_config.gd:53-56 + CLAUDE.md §6). That half is re-filed as C6-M1 at P1/KT. The DECISIVE_OB/POOL_FLOOR/BASE_POOL/etc. round-trip gap (those ARE byte-identical on inspection) stands as filed, P2/KNOWN-UNTRACKED. |
| C6-F3 | **uphold** | All 7 keys (config.py:6,54,61,82,101) verified unconsumed across every combat_engine_v1/*.py (CHOKE_GRIP_MIN's config copy inert; weapon_physics.py:522-523 forked its own GRIP_SHORT); all 7 present in combat_engine_v1.json:41,51,76,79,150,154,183. Same failure shape as the fixed DAMAGE_SCALE=4.0 (combat_config.gd:4-5 self-documents). |
| C6-F4 | **uphold** | Census conflated two stamina constants: combatant.py:45-47's stamina_max uses STAMINA_PER_END/STAMINA_PER_SPIRIT; STAMINA_REF (config.py:56) is genuinely read at wrapper.py:361 (recovery formula); no stamina_ref in the .gd. Real-but-unported ≠ dead — correct rule-(b) framing. |
| C6-F5 | **OVERTURN** | False contradiction. workbench/presets.py:18 and probabilities.py:14 carry an inline comment: the harness "reaches into the FROZEN v32 validation station BY DESIGN (dev tooling; doctrine container-hygiene exclusion, ED-1085)" — the same ED-1085 invoked as forbidding the dependency explicitly sanctions it for workbench tooling. core.py's ED-1085 note (:5-9) scopes to the engine runtime, not the tree. Documented carve-out, not drift. (C6-U4 falls with it.) |
| C6-F6 | **soften** (counts/citation) | Directionally verifiable, but ED-PC-0002 is at config.py:11 (not :15; :35/:165 check out) and the "18/181" mixes units (file is 174 lines; 181 = CFG keys); independent grep lands in the 10-20 tagged-line ballpark, not a reproducible 18. P3, corrections applied. |
| C6-F7 | **uphold** | Both census mis-citations verified: modes.py:5-6 is venue prose, real defs :450-451; primitives.py:18-31 is the Stasis class, SEED constants scattered ~:50-255. Values not in dispute. |
| C6-F8 | **soften** (calibration KT→NEW) | Ob-20 exception real (dice_engine.py:94-113; params/core.md "Ob 20 exception") and omitted from the census row (quantity_census.md:109). But "KNOWN-TRACKED · F-SIM-05" misapplies the schema — F-SIM-05 is a sibling finding-ID from this audit's own census, not an ED. The omission has no owning ED → NEW. |

## Missed findings

**C6-M1 · P1 · export-drift · KNOWN-TRACKED (ED-1050 residual)** — combat_config.gd's RESIST is
not "unverified for future drift": it has **already drifted in 4 of 12 cells** from core.py's
current oracle (core.py:77-89 grounding-edit comment: cloth.shear .35→.45, cloth.puncture
.15→.12, cloth.percussion .10→.12, mail.shear .80→.85; live dict cloth={.12,.45,.12},
mail.shear=.85) vs combat_config.gd:34-38 (still {.10,.35,.15}, .80). combat_config.gd:53-56 and
CLAUDE.md §6 flag the re-export as deferred/known-red, but neither states the port carries the
STALE pre-grounding numbers — a live wrong-value ingestion for any Godot consumer today.

**C6-M2 · P3 · other · NEW** — GAP_EXPOSURE (core.py:105, consumed at :121-125) and GAP_PREC_REF
(:106) are entirely absent from combat_config.gd — not stale like RESIST, never carried at all;
the export gap is wider than the dossier's RESIST-only headline.

## Conformance note

No invented criteria; no ruled forks — U1–U4 present defaults with alternatives, and U1's
warn-before-block posture matches the repo's existing enforcement discipline. One rule-adjacent
problem: F2's "currently byte-identical" was an unverified factual assertion presented as settled
— the dossier's own file:line methodology would have caught it with an actual diff (became M1).
F5/U4 is the direct conformance failure: a documented, in-line-cited, deliberate ED-1085 exception
flagged as undisclosed inconsistency — the inverse-of-rule-(b) family (misreading an explicit
doctrine carve-out as unexamined drift). Lane scoping respected throughout.
