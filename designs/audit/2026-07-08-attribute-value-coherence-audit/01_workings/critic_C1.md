# Critic pass — C1 (Personal attributes, aliases & aggregates)

Antagonist relay over `dossier_C1.md` (independent read-only verification; producer reasoning not shared).

## Verdicts

| target | verdict | reason (condensed, evidence-cited) |
|---|---|---|
| F1 | **uphold** | Four rosters verified byte-for-byte: descriptor_registry.yaml:30-44 (9, folded); glossary.md:33-41 (7, no Focus/Bonds); params/core.md:140-145 (10, un-folded, Recall); canonical_registry.md:138-140 (10 — the PARTIALLY-SUPERSEDED banner covers its combat-pool rows, not the attribute table). CURRENT.md doesn't index the latter. Calibration KNOWN-UNTRACKED accurate: ED-IN-0008's ledger text (editorial_ledger.jsonl:326) names only glossary-vs-registry. |
| F2 | **uphold** | Recall load-bearing (params/core.md:151,245; params/contest.md:23,141,288,302; contest_extensions.md:57; southernmost.md:15,95); zero hits in descriptor_registry/names_index. No ED names the registry absence (ED-894 is scoped to one Concentration formula). |
| F3 | **soften** (calibration NEW→KNOWN-TRACKED) | Facts confirmed exactly (mass_combat.md:139,361,369; mass_battle_v30.md:266; tests/sim/mass_battle/config.py:155-159 use Cognition with CMD_CHA_WEIGHT/CMD_COG_WEIGHT vs registry:39's [ASSUMPTION] fold). But ED-IN-0008 explicitly names "mass_combat's Command formula written against legacy attribute names" — rule-(c) violation as filed. P1 stands. |
| F4 | **uphold** | Exhaustive sweep holds: zero bare "Will" as attribute outside registry/names_index/dead-test/audit files; "Spirit" pervasive (module_contracts.yaml:827-828; params/core.md:159,162,247; config.py:61). Correctly KT (ED-IN-0008). |
| F5 | **uphold** | Three-way Health divergence at cited lines (glossary.md:47 =Endurance; params/core.md:158 pre-ED-1021 with self-routing note; derived_stats_v30.md:59-68 = module_contracts.yaml:827-828). No tracking ED for glossary's staleness; NEW reasonable. |
| F6 | **uphold** | glossary.md:48 "Endurance+History+1 (armour-modified)" vs ratified (3×End)+(2×Spirit) (derived_stats_v30.md:98 RATIFIED S1 = params/core.md:159 = contracts:822). "Two full supersessions" consistent with the documented History-form → End×5 → 3End+2Spirit chain. |
| F7 | **soften** (claim narrowed) | Half miscited: glossary has exactly ONE Focus row (:52, derived-stat sense); Focus is NOT in glossary's attribute table — so "two unrelated quantities on the same glossary surface" is false as written. The REAL collision is cross-surface (registry/params attribute Focus 1-7 vs glossary derived Focus 1-5+). Second half confirmed (params/core.md:152 vs :162 unmarked pre-ED-694 rule beside its replacement). P2 survives on the corrected framing. |
| F8 | **uphold** | Good census correction: Agility live via tempo/initiative (combat_v30.md:35; config.py:64 AGI_TEMPO_K) + maneuver rolls (combat_design_v1.md:70,102-108,437,442). Census conflated "struck from Combat Pool" with "no consumer anywhere" — and the fix cites live consumers, not build metadata (rule-b clean). |
| F9 | **soften** (calibration NEW→KNOWN-TRACKED) | Substance confirmed: npc_behavior_v30.md §1.3 (:32-34,53-54,73-74,94-95) canonically enumerates the 4-value taxonomy; conviction_track_v1.md is [SUPERSEDED PP-717] at its own top line — census miscitation real. But ED-IN-0008 names this contradiction AND descriptor_registry.yaml:100 carries an ED-IN-0025 inline correction flagged NEEDS-JORDAN — doubly KNOWN-TRACKED; rule-(c) violation as filed. Narrow value retained: the census's specific miscitation. |
| F10 | **uphold** | Matches verified baseline: names_index.yaml:44-73 all enforce:warn; tests/registry/test_descriptor_registry.py defines no test_* (pytest collects zero). Framed as aggregation, not re-argument. |
| F11 | **uphold** | attr.social.charisma alias "Influence" (registry:43; names_index:52) vs fac.influence (registry:65; names_index:61); no disambiguation tag; no tracking ED found. |
| U1 | **soften** (internal inconsistency) | "Adopt the registry's 9" as-is re-bakes the Acuity/Will folds that U2/U3 — on the same F3/F4 evidence — recommend reversing. Not a fork-ruling violation (correctly parked to queue-13/ED-IN-0008), but a self-contradicting docket. Reconciled in OPT-AV-1: registry's 9-key *structure* with U2/U3 naming corrections + Recall. |
| U2 | **uphold** | Recommended default properly framed; ED-899 rationale accurate per F3. |
| U3 | **uphold** | Same basis; zero live "Will" usage per F4; feeds ED-IN-0008, not ruled. |

## Missed findings

**M1 · P3 · collision · NEW** — The registry's fold-target **Acuity has ZERO live-formula
consumers** anywhere (grep across params/, designs/scene, designs/provincial, module_contracts,
sim/, config.py: hits only in registry/names_index/dead-test/audit artifacts) — a starker version
of F4: BOTH contested mind-fold primaries (Acuity, Will) are unconsumed. Worse, the bare word is
already spent on a wholly different, **explicitly rejected** proposed quantity: the Fieldwork
depletion resource "Acuity (Cognition + Focus)" (comprehensive_system_audit_2026-04-15.md:469,478,528),
rejected at integration_proposal_v30.md:200-204 ("Acuity should not be introduced... would
double-penalize investigation"). Evidence: descriptor_registry.yaml:39; the greps above.

## Conformance note

No invented finding-kinds or KIND categories originate in the dossier; build-state correctly used
only as routing (F8 *fixes* an upstream build-state-as-verdict error — the right move under rule
b). No fork ruled: roster/naming picks parked as options feeding queue-13/ED-IN-0008 (rule e); no
lane-scoping violation. Two defects: (1) calibration errors F3/F9 — KNOWN-TRACKED items (ED-IN-0008;
ED-IN-0025) re-argued as NEW (rule-c violation), though the added file:line verification has
standalone value; (2) U1 vs U2/U3 self-contradiction (docket hygiene). Separately: the census (and
F9's prose) uses a `practitioner_stat` KIND absent from descriptor_registry's declared enum — the
dossier inherits and repeats it (including in a registry_delta candidate) without flagging it;
carried into extension §1's note.
