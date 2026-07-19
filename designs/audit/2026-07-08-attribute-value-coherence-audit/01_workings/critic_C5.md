# Critic pass — C5 (Faction & settlement stats + Mandate seam)

Antagonist relay over `dossier_C5.md` (independent read-only verification).

## Verdicts

| target | verdict | reason (condensed, evidence-cited) |
|---|---|---|
| C5-F1 | **uphold** | params/factions_personal.md:14 gives linear round(0.5L+0.5PS) citing "faction_behavior_v30 §4"; that section (REVISED by LPS-2e) now states the size-weighted saturating form matching faction_canon_v30.md:213-216 and module_contracts.yaml:598-601. Citation genuinely stale; P1 — an engine reading factions_personal.md verbatim gets the wrong formula. *(C7 critic adds ED-784 context: the linear personal view was blessed as deliberate — the fix is marking, not adjudication; see OPT-AV-10.)* |
| C5-F2 | **uphold** | settlement_layer_v30.md:43 cites nonexistent "derived_stats_v1 §4"; derived_stats_v30.md §9 heading "(PENDING)" + "Not canonicalized" for the identical formulas; module_contracts.yaml:556-597 wires g_dv0 live on them. Circular/broken canonicity; P1 — contracts consumers treat disclaimed-pending formulas as live canon. |
| C5-F3 | **soften** (P1→P2; kind→enforcement-gap) | Facts confirmed (bg/core.md:200-207 floors: Influence 1, Wealth/Military/Stability 0, Intel omitted; registry:62 blanket "1-7", unlike settlement_stats' per-entry scales :78-82). But no two sources give competing values for the same stat — registry precision loss, not live divergence. |
| C5-F4 | **uphold** | mass_battle_v30.md:169 per-unit Discipline (1-7, rout/formation mechanics, ED-1018/1024/1026/1027) vs derived_stats_v30.md (~:298,545) faction Discipline = Stability×10. No cross-reference anywhere. Real, previously uncaptured. |
| C5-F5 | **uphold** | registry:107 lists 9 derived_values (incl. "Mandate", not even a §14.1 row); §14.1 tables 16 — missing TroopCount, Legitimacy(derived), Treasury, Levies Available, Reputation, Discipline, Intelligence Holdings, Public Order. Bonus: the census row for Treasury/Reputation/Discipline/Levies falsely tags Registered=not_descriptors — census claim wrong, strengthening the finding. |
| C5-F6 | **uphold** | settlement_layer_v30.md:22 keeps Fort Level province-level; geography gives one Fort value per province (17 T-nodes, 0-4); yet the Garrison formula (contracts:591-592; §1.3) consumes it per-settlement (36 nodes) with no inheritance rule. |
| C5-F7 | **uphold** | Undersold if anything: zero "Public Support" hits in settlement_layer_v30.md (line 631 correctly "Popular Support") — the tracked residual citation (name_collision_database.yaml:469) is stale; real untracked residual doubly live at mechanical_terms_index.md:196 AND :1167 (deprecated name + pre-LPS-2e model). |
| C5-F8 | **soften** (P2→P3) | scale_transitions_v30.md carries an explicit "Settlement targeting (AUD-SET-02)" note above the §5.5 table stating Accord changes target settlement Order, cross-referencing peninsular_strain §2.5. The flagged "direct delta" is table-row shorthand below an in-document disambiguation. Gap real but small. |
| C5-F9 | **soften** (half struck) | Ceiling half confirmed (clock_registry:141 declares 0-250; max = 5×20+4×30 = 220). Prosperity-ambiguity half unsupported by its own citation: registry:80,81 contains ONE Prosperity entry (:81 is Defense); the territory-tier 1-7 Prosperity lives in clock_registry:62, which itself disambiguates "Settlement Prosperity" (:129). Struck that half; ceiling stands at P3. |
| C5-F10 | **uphold** | bg/core.md:170 Löwenritter Wealth=3 vs stats_1_7_scale.md:19-25 W(BG)='—'. Minor cross-surface divergence; P3. |
| C5-F11 | **uphold** | §1.8 (~:155-165) unambiguously defines base(Type)/Prosperity_s/FacilityTier_s with per-type values. Census "AMBIGUOUS" overstated; real gap = contract-layer non-declaration. Good correction. |
| C5-F12 | **uphold** | stats_1_7_scale.md:3 declares 6-stat lineup excluding L/PS but the :15-19 table carries L/PS columns; seed-caveat exists only at :266+, far from the table. P3 fair. |
| C5-F13 | **uphold** | bg/core.md:172 footnote (2026-05-30) "UNRESOLVED... See ED-869" vs stats_1_7_scale.md:19 resolution applied (5/6, 2026-05-31). Correctly KT (ED-869). |

## Missed findings

**C5-M1 · P2 · collision · NEW** — attr.social.charisma's alias list includes "Influence"
(registry:43) — the exact bare name of fac.influence (:65) in the same file, no cross-reference.
Same failure class as F4 but intra-document. *Synthesis note: deduped into C1-F11 (identical
finding filed there); counted once.*

**C5-M2 · P2 · stale · NEW** — params/factions_personal.md's Starting Values table still shows
Intel='—' for Crown, Church, Hafenmark, Varfell, Guilds (:23-27; file header dated 2026-04-13,
no later reconciliation), despite ED-787 (2026-05-03) restoring Intel with concrete values
(stats_1_7_scale.md:27-36) and bg/core.md:172's 2026-05-30 RECONCILED gap-fill for the same
factions. The TTRPG-mode carrier never got the equivalent update — broader than the
single-faction F10. |

## Conformance note

Mostly clean. No invented kinds; no build-state-as-verdict — the "PENDING/Not canonicalized"
labels leaned on in F2 are the source doc's own canonicity markers, legitimate evidence. Design
forks (Fort inheritance U6, Discipline rename U4, Intel floor U3) correctly left as options with
defaults (rule e). One soft violation: C5-U2's "Promote to CANONICAL" default goes past
bookkeeping — §9 explicitly hedges the multipliers as design-pending, so the default leans toward
settling a live settlement-balance question that is SE-lane content; the option must flag the SE
feed (done in OPT-AV-18). Two census-correction claims (F7, F11) independently verified correct.
F9 mixed a confirmed claim with an unsupported one in a single bullet — evidence-hygiene lapse.
