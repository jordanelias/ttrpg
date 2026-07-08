# Term Usage Sweep — Batch 5: Faction Stats, Settlement Stats, and Turmoil vs Strain

# Batch 5 Usage Sweep: Faction Stats, Settlement Stats, Turmoil vs Strain

## Scope note (read before the term sections)

Every term in this batch returned 150–250+ distinct files on a repo-wide grep (the tool caps list results at 250; several terms hit that cap, meaning the true total is higher still). This corpus is dominated by three non-canonical strata that CLAUDE.md itself instructs be treated as history/derivative, not sources of truth: `archives/` and `deprecated/` (history only, never canonical), the `tests/sim/*.md` and `tests/emergent_arc_skeleton_test_*.md` narrative logs (explicitly "prose, not executable specs"), and the `designs/audit/*/01_workings/*` dossier/critic/lens files (audit *artifacts* — themselves prior sweeps' output, not primary design docs). Exhaustively line-citing every occurrence in all ~250 files per term across 16 terms is not achievable at any reasonable depth in one pass, so for each term below I:

1. Establish the home definition from the cited primary source.
2. Give the **exact file count** the grep returned (noting when it hit the 250 cap) and enumerate **every hit in the mechanically load-bearing corpus** (`designs/provincial/`, `designs/territory/`, `designs/scene/derived_stats_v30.md`, `params/`, `references/*.yaml`, `sim/*.py`, `canon/`, `tools/observability/` generated artifacts) individually with line citations.
3. Bucket the remainder (audit dossiers, archives, deprecated, tests narrative logs, `references/valoria_*_r2.md` legacy compiled mega-docs) by category and sample several — I flag explicitly wherever a sample surfaces a *new* divergence rather than just repeating known canon, and I flag explicitly wherever I did not open a file.
4. Run the four-part method (divergence check, classification table, disambiguation) against everything I actually opened.

This is a scoping compromise made necessary by corpus size, not a shortcut taken for convenience — I want that tradeoff visible rather than silently made.

---

## 1. Mandate

**Home definition.** Canonical name **Mandate**. Range **0–7**. Formula (settlement-aggregate, LPS-2e, ratified by Jordan 2026-05-30): `designs/territory/settlement_layer_v30.md:165-168` —
`q_s = 0.5·L_s + 0.5·PS_s` (per settlement, 0–7); `W_s = base(Type) + Prosperity_s + FacilityTier_s` (§1.8, line 159); `T = Σ_s W_s·(q_s/7)`; **`Mandate = clamp(round(7·T/(T+K)), 0, 7)`, K = 6**. This is the *sole* current canonical home — `designs/provincial/faction_canon_v30.md:213-221` (§5.1/§5.2) restates the identical formula and explicitly cites settlement_layer §1.8 as authoritative, and both `references/module_contracts.yaml:600` and `references/descriptor_registry.yaml:70` point to the same place ("Mandate is a size-weighted derived aggregate of settlement L/PS -- NOT a base attribute"). `params/factions/stats_1_7_scale.md:1-3` confirms: "Faction stats (6): Mandate / Influence / Wealth / Military / Intel / Stability. Mandate is the headline (DERIVED...)."

**Exhaustive usage sweep.** Repo-wide grep (excluding `tests/`) hit the 250-file cap; including `tests/` also hits 250. Core corpus, every file opened or grep-context-checked:
- `designs/territory/settlement_layer_v30.md` §1.8 (canonical definition, above).
- `designs/provincial/faction_canon_v30.md` — §5.1/§5.2/§5.3 (formula + per-faction "Mandate (derived)" row in every faction sheet, e.g. Crown 5, Church 5, lines 451/616); §8.3 Collapse ("Mandate → 0 immediate"); §9 Tactic table (Royal Decree M = Mandate−2, Excommunication M = Mandate − target Mandate).
- `params/factions/stats_1_7_scale.md` — lines 1-3, 56-95 (d+σ resolver uses Mandate in multiple governed-check margins), 266-273 (Mandate Recovery, per-settlement).
- `designs/provincial/faction_behavior_v30.md`, `faction_state_authoring_v30.md`, `faction_layer_v30.md`, `faction_politics_v30.md`, `factions_personal_v30.md` — all reference Mandate as the faction headline stat consistent with the 6-stat lineup.
- `designs/provincial/peninsular_strain_v30.md` — "Mandate check Ob 2/3" at Strain thresholds (§4.3), "target faction Mandate −1" (Dynastic Proclamation §5.3).
- `designs/provincial/ci_political_v30.md`, `victory_v30.md`, `military_layer_v30.md` — CI-60 Seizure formula, victory thresholds (Mandate ≥ 3 for co-victory).
- `designs/scene/derived_stats_v30.md:295-335,467-495,554` — "Legitimacy (from Mandate)" derived meter = `Mandate × 20`; explicit footnote at line 554 reconciling with LPS-2e.
- `designs/architecture/scale_transitions_v30.md`, `key_echo_armature_v1.md`, `propagation_spec_v1.md`, `player_agency_v30.md` — Domain Action / Domain Echo framing references Mandate.
- `references/descriptor_registry.yaml:70`, `references/module_contracts.yaml:87,563,598-604,664,686,899`, `references/canonical_sources.yaml:199-522` (the LPS-1→LPS-2e migration changelog, lines 205-208, 346, 383, 516-522).
- `references/glossary.md:104` (Part Four: "Mandate | M | Institutional authority and political legitimacy. 0 = Collapse state" — no explicit range given, but table preamble at line 100 says "Most stats below tracked on 1–7 scale (0 = collapse)").
- `params/bg/core.md`, `params/bg/faction_actions.md`, `params/bg/clocks.md`, `params/bg/ed_resolutions.md` — legacy Domain Action rules, largely superseded framings retained for patch history.
- **Sim code** (this is the important one): `sim/autoload/game_state.py:7-9`, `sim/territory/registry.py:41-63`, `sim/peninsular/ci_track.py`, `sim/peninsular/accounting.py:11-12`, `sim/provincial/crown_initiative.py:14-15,90,99,138,177,200`, `sim/provincial/mass_seizure.py:27,66,123,135-137,169,193`, `sim/provincial/absolution.py:6,33`, `sim/provincial/excommunication.py:42`, `sim/provincial/council_solmund.py:50,60`, `sim/provincial/varfell_mandate_action.py`, `sim/personal/parliamentary_vote.py:8-33,62,98,154-206`, `sim/personal/contest/faction.py:3-131`, `sim/cross_scale/domain_echo.py:186-190`.
- `tools/observability/*` (lexicon/graph/decisions JSON+JS+HTML+MD): these are **generated artifacts** of a corpus-graph tool, not authored canon.
- Bulk narrative/audit-artifact corpus not individually itemized: ~180+ additional files across `designs/audit/*/01_workings/`, `tests/sim/*.md`, `tests/emergent_arc_skeleton_test_*.md`, `archives/`, `deprecated/`, `references/valoria_*_r2.md`. Sampled `archives/audit/2026-05-30-lps-mandate-ners-audit/lps_mandate_comprehensive_ners_audit.md` and `archives/audit/2026-05-01-mandate-consumer-audit/00_audit.md` — both are prior audits *of* the LPS migration and post-date/pre-date it consistently; no new divergence found beyond what's below.

**Divergence check.**
1. **ORACLE/DOC divergence (the big one, and it is self-flagged in-repo, not hidden).** The canonical doc model (settlement_layer §1.8, faction_canon §5) has Mandate as a **pure derived aggregate** — there is no stored "Mandate" scalar; it's computed each Accounting from per-settlement L/PS + Weight. The `sim/` oracle instead stores **`Faction.L`** as a flat scalar and treats `Mandate == Faction.L` throughout — e.g. `sim/personal/parliamentary_vote.py:13,20-33`: *"Mandate is stored as the scalar Faction.L... this Faction.L-as-Mandate-pool convention is the pre-LPS-1..."*; `sim/autoload/game_state.py:7-9`: *"(L/Sta/W/I/Mil; no Mandate / PS / Treasury / da.* Keys) implements the pre-LPS-1 SUPERSEDED faction stat model — this is literally where 'no Mandate' lives... Do NOT port this schema."* This is explicitly labeled PRE-LPS-1/PORT-BLOCKING (ED-FA-0004, 2026-07-07) in half a dozen sim files. It is a real, live, unresolved divergence between doc-canon and code-oracle — just one that the repo already knows about and has fenced off rather than silently carrying.
2. **Stale resolution-method framing in `values_master.yaml:1234-1365`.** Entries like `"Mandate pool, Ob 2"` and `"vs target Mandate (or Ob 2 if non-leader)"` describe the *pre-ED-874* bare-stat-dice-pool method. `params/factions/stats_1_7_scale.md:56-98` establishes that as of ED-874 (ratified 2026-05-31) the canonical resolution method for all these checks is the deterministic+stochastic "d+σ" resolver (`P_success = clamp(0.50+0.10M,...)`), not a dice pool "vs Ob." `values_master.yaml` was not updated after ED-874 — CLAUDE.md §5 already flags this file as "auto-extracted and partly stale," and this is a concrete instance.
3. No numeric-range divergence found for Mandate itself (0–7 is consistent everywhere it's stated as a range).

**Step 4 — Single-source classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `designs/territory/settlement_layer_v30.md:147-180` | CANONICAL DEFINITION | — | — |
| `designs/provincial/faction_canon_v30.md:213-221,241-243` | PULLED/REFERENCED | Explicit inline citation "(settlement_layer §1.8)" + front-matter states this file "references, does not duplicate" (line 1) — though it does restate the formula as literal text alongside the citation | Yes |
| `params/factions/stats_1_7_scale.md:1-3` | PULLED/REFERENCED | One-line pointer ("Mandate is the headline (DERIVED...)"); does not restate the formula | Yes |
| `references/module_contracts.yaml:600,563` | HARDCODED DUPLICATE (cited) | Literally restates `Mandate = clamp(round(7T/(T+6)),0,7)` as a YAML string with a parenthetical citation to settlement_layer §1.8 — restated, not imported/generated | Yes (no drift yet) |
| `designs/scene/derived_stats_v30.md:297,554` | PULLED/REFERENCED | `Mandate × 20` is a distinct *display-meter* derivation (explicitly disclaimed as "not a 0-100 master scale"), and line 554 explicitly cites and reconciles with settlement_layer §1.8 rather than re-deriving Mandate itself | Yes |
| `references/descriptor_registry.yaml:70` | PULLED/REFERENCED | One-line note citing settlement_layer §1.8; no formula restated | Yes |
| `references/canonical_sources.yaml:199-522` | PULLED/REFERENCED | Changelog/provenance narrative of the LPS migration, not a live restatement | Yes (historical) |
| `references/values_master.yaml:1234-1365` | HARDCODED DUPLICATE | Independent literal ("Mandate pool, Ob 2") with no citation or regeneration mechanism; auto-extracted per CLAUDE.md §5 | **No — stale**: describes the pre-ED-874 bare-dice-pool method, superseded 2026-05-31 |
| `sim/autoload/game_state.py:7-9`, `sim/personal/parliamentary_vote.py`, `sim/provincial/crown_initiative.py`, `mass_seizure.py`, `absolution.py`, `excommunication.py`, `council_solmund.py`, `ci_track.py` | HARDCODED DUPLICATE (self-flagged) | Independently implements `Mandate == Faction.L` scalar with no aggregation code; explicitly commented as PRE-LPS-1/PORT-BLOCKING, i.e. the repo itself has already flagged this as a known, not-yet-fixed duplicate-model | **No — known divergent**: implements the superseded pre-LPS-1 model, not the settlement-aggregate model |
| `sim/territory/registry.py:41-67` | HARDCODED DUPLICATE (partial) | Declares `legitimacy`/`popular_support` fields per §1.8 bounds (0-7) but per its own comment (lines 60-63) they are "declared but NEVER READ OR WRITTEN anywhere in sim/" — an inert stub, and no Weight/Mandate-aggregation code exists in this file at all | N/A — unimplemented, not merely duplicated |
| `tools/observability/lexicon.json`, `graph.json`, `decisions.json` (+ their `.js`/`.html` renderings) | PULLED/REFERENCED (generated) | Produced by a corpus-indexing tool reading the design docs; not hand-authored | Yes, as of last regeneration |
| `designs/audit/*` dossiers (~30 files sampled/listed above), `archives/*`, `deprecated/*`, `tests/sim/*.md` (~150+ files, not individually itemized) | Mixed PULLED/REFERENCED and narrative citation | Audit prose citing the ratified formula/status; archives are explicitly non-canonical per CLAUDE.md | Consistent where sampled |

---

## 2. Influence (faction)

**Home definition.** Canonical name **Influence**. Range **1–7** (cannot drop below 1 per glossary: "Cannot drop below 1 (faction remains extant)" — `references/glossary.md:105`). Home mechanical source: `references/descriptor_registry.yaml:61-69` (`fac.influence`, scale "1-7", source `params/factions/stats_1_7_scale.md`) and `params/factions/stats_1_7_scale.md:1-24` (Starting Stats table). No derived formula — it's a base attribute, unlike Mandate.

**Exhaustive usage sweep.** Grep hit the 250-file cap (both including and excluding `tests/`). Core corpus:
- `params/factions/stats_1_7_scale.md` — Starting Stats table (line 17-25: Crown 5, Church 6, Hafenmark 4, Varfell 4, Guilds 4, Löwenritter 2/3), used throughout as a resolver input (Assert M = Influence−2, Reconstitute M = Influence−6, CI Seizure pool = Influence + floor(CI/15)).
- `designs/provincial/faction_canon_v30.md` — every faction's Stats table (e.g. Crown Influence 5, Church 6, lines 446/611); §9 Tactic table; §5.1 range table "Influence | 1–7."
- `designs/provincial/faction_behavior_v30.md`, `faction_layer_v30.md`, `faction_politics_v30.md`, `ci_political_v30.md`, `victory_v30.md`, `military_layer_v30.md` — Domain Action pool usages, Treaty positioning (M = own Influence − target Influence), CI-60 Seizure roll.
- `designs/scene/derived_stats_v30.md:337+` — "Reputation (from Influence)": `Influence × 15`.
- `references/descriptor_registry.yaml:65`, `references/module_contracts.yaml` (faction_state block), `references/canonical_sources.yaml`.
- `sim/peninsular/ci_track.py`, `sim/provincial/crown_initiative.py`, `sim/provincial/parliamentary_transfer.py`, `sim/provincial/mass_seizure.py` — pool usage in resolvers.
- `params/bg/*` (institutions, ministry, npc_priority_trees, parliament, stress_patches, faction_actions, victory, ci_seizure), `params/factions_personal.md`, `params/factions/npc_stance_triangles.md`, `params/factions/riskbreakers_identity.md`.
- Also heavily used **incidentally** in an unrelated mechanical sense: "Influence" is also a component of *fieldwork* (`params/fieldwork.md`, `designs/scene/fieldwork_v30.md`, `fieldwork_bg_v30.md`) and *combat/social contest design* docs discuss "influence" as an ordinary-English verb/noun ("attempts to influence..."), and `designs/scene/combat_v30.md`, `combat_design_v1.md`, `conviction_track_v30.md` use it descriptively, not as the faction stat.
- Bulk: ~200 additional files (audit dossiers, arcs, archives, `tests/`) not individually itemized; sampled `designs/audit/2026-05-16-faction-ners-all-directions.md` and `designs/audit/faction_stats_renaissance_review.md` — both consistent with the 1–7 range, no new divergence.

**Divergence check.** No numeric-range or formula divergence found for the faction stat itself — every mechanical citation checked uses 1–7 consistently, and the "floor" rule (cannot go below 1) is not contradicted anywhere sampled. The only "divergence" is the ordinary-English homograph noted above, which is a disambiguation matter, not a mechanical inconsistency.

**Disambiguation note.** Excluded as incidental: generic-English "influence" in prose narrative/arc docs (`designs/arcs/*`), in fieldwork/social-contest prose describing a PC "influencing" an NPC (a *different*, non-faction-stat mechanic — social contest pools), and in audit prose ("this finding influences the workplan"). Only faction-stat capital-letter "Influence" tied to a faction sheet/pool is counted above.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `params/factions/stats_1_7_scale.md:1-24` | CANONICAL DEFINITION | — | — |
| `references/descriptor_registry.yaml:65` | PULLED/REFERENCED | `source: params/factions/stats_1_7_scale.md` field, no value restated | Yes |
| `designs/provincial/faction_canon_v30.md` (per-faction Stats tables) | HARDCODED DUPLICATE (cited) | Restates each faction's starting Influence value as a literal table cell; provenance line says "reproduced from current canonical sources (stats_1_7_scale.md Starting Stats table)" (§5.2) | Yes |
| `designs/scene/derived_stats_v30.md` (Influence×15 Reputation) | PULLED/REFERENCED | Distinct derived-meter formula, not a restatement of the base stat range | Yes |
| `sim/peninsular/ci_track.py`, `sim/provincial/crown_initiative.py`, etc. | PULLED/REFERENCED | Reads `faction.I` field at runtime; does not hardcode the 1–7 bound anywhere I found in these files (no `I_MIN/I_MAX` constant analogous to registry.py's `STAT_MIN/MAX`) | N/A (no bound enforced in code to check) |
| `params/bg/*`, `params/factions_personal.md` | HARDCODED DUPLICATE | Independent per-faction Influence figures in BG-mode tables, no cross-reference mechanism found | Believed consistent (not exhaustively cross-checked cell-by-cell) |
| Audit dossiers / archives (~200 files, sampled only) | PULLED/REFERENCED (narrative citation) | Prose analysis citing the stat, not independent redefinition | Consistent where sampled |

---

## 3. Wealth (faction)

**Home definition.** Canonical name **Wealth**. Range **1–7**; "0 = cannot Trade or fund Wealth-requiring actions" (`references/glossary.md:106`). Home source: `references/descriptor_registry.yaml:66` (`fac.wealth`) + `params/factions/stats_1_7_scale.md` Starting Stats table (TTRPG/BG columns, e.g. Crown 4/4, Church 5/5, Hafenmark 5/5).

**Exhaustive usage sweep.** Grep hit the 250-file cap. Core corpus: `params/factions/stats_1_7_scale.md` (Starting Stats + Hafenmark Wealth Sink §"ED-064b"), `designs/provincial/faction_canon_v30.md` (Stats tables + Guilds "Economic Leverage" M = Wealth − target Wealth), `faction_behavior_v30.md`, `faction_layer_v30.md`, `factions_personal_v30.md`, `military_layer_v30.md` (military upkeep costs), `designs/scene/derived_stats_v30.md:298,323` ("Treasury" = `Wealth × 100`), `references/descriptor_registry.yaml:66`, `references/module_contracts.yaml`, `sim/provincial/faction_action.py`, `sim/provincial/mass_seizure.py`, `sim/peninsular/*`, `params/bg/core.md`, `params/bg/faction_actions.md`, `params/bg/tracks.md`. Also incidental generic-English "wealth" appears in world-building prose (`designs/world/worldbuilding_v30.md`, `southernmost_v30.md`, `character_histories_v30.md`) describing setting economics narratively, not the stat.

**Divergence check.** No range/formula divergence found. `designs/scene/derived_stats_v30.md:298`: "Wealth | Treasury | Wealth × 100, starting = stat × 100" is consistent with `references/canonical_sources.yaml:520`'s note that Treasury×100 is one of several *per-system* derived-meter multipliers (Mandate×20 Legitimacy, Influence×15 Reputation, Stability×10 Discipline), explicitly "no 0-100 master scale" — internally consistent framing, not a divergence.

**Disambiguation.** Excluded: ordinary-English "wealth" in worldbuilding/history prose describing in-fiction economic conditions rather than the tracked faction stat.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `params/factions/stats_1_7_scale.md` Starting Stats table | CANONICAL DEFINITION | — | — |
| `references/descriptor_registry.yaml:66` | PULLED/REFERENCED | Pointer only | Yes |
| `designs/provincial/faction_canon_v30.md` Stats tables | HARDCODED DUPLICATE (cited) | Restated literal per-faction values, cites stats_1_7_scale.md as source in Provenance sections | Yes |
| `designs/scene/derived_stats_v30.md:298,323` | PULLED/REFERENCED | Distinct derived buffer formula, cross-referenced in canonical_sources.yaml:520 | Yes |
| `sim/provincial/*.py` | PULLED/REFERENCED | Reads `faction.W` at runtime | N/A |
| `params/bg/*` tables | HARDCODED DUPLICATE | Independent BG-mode figures | Believed consistent, not cell-checked |

---

## 4. Military

**Home definition.** Canonical name **Military**. Range **1–7**; "0 = cannot Muster" (`references/glossary.md:107`). Home: `references/descriptor_registry.yaml:67` (`fac.military`) + `params/factions/stats_1_7_scale.md` Starting Stats (Crown 5/6 with a footnote at line 19: "Mil: Crown fields the Löwenritter (5/6); prior value 4 struck per ED-869").

**Exhaustive usage sweep.** Grep (excl. tests) returned 202 files. Core corpus: `params/factions/stats_1_7_scale.md`, `params/bg/military.md`, `designs/provincial/military_layer_v30.md`, `mass_battle_v30.md`, `faction_canon_v30.md` (Stats tables + "Crown faction Military 4 expressed through Löwenritter Power 5/Discipline 6" line 453), `faction_layer_v30.md` ("Military Stat Change on Unit Destruction," "Military Seasonal Cap"), `designs/scene/derived_stats_v30.md:299` ("Levies Available" = `Military × 2`, ceiling), `sim/provincial/massbattle.py`, `references/descriptor_registry.yaml:67`, `references/module_contracts.yaml`. Also very heavily incidental: "Military" appears as an ordinary adjective/domain-label throughout `designs/provincial/mass_battle_v30.md`, `military_layer_v30.md`, `params/history/mass_combat.md`, `research/pre_firearms_formations/*` (historical-precedent research files describing "military formations," "military history" — not the faction stat at all), and combat/godot docs referencing "military" generically.

**Divergence check.** No range divergence for the stat itself. One noteworthy internal correction already tracked in-repo: `params/factions/stats_1_7_scale.md:19` documents that Crown's Military value was corrected from 4 → 5/6 (ED-869, 2026-05-31) to reflect the Löwenritter standing-army fielding — this is a *resolved* historical divergence, not a live one, but worth naming since older snapshots elsewhere in the bulk corpus (not individually re-verified here) may still carry the pre-ED-869 value of 4.

**Disambiguation.** Excluded: the entire `research/pre_firearms_formations/*` directory (historical martial-arts/formation research, not game mechanics), and generic "military" adjective usage in mass_battle/military_layer prose describing the domain rather than citing the stat value.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `params/factions/stats_1_7_scale.md:17-25` | CANONICAL DEFINITION | — | — |
| `references/descriptor_registry.yaml:67` | PULLED/REFERENCED | Pointer | Yes |
| `designs/provincial/faction_canon_v30.md` Stats tables | HARDCODED DUPLICATE (cited) | Literal restatement, cited provenance | Yes |
| `designs/scene/derived_stats_v30.md:299` | PULLED/REFERENCED | Distinct derived formula | Yes |
| `sim/provincial/massbattle.py` | PULLED/REFERENCED | Runtime field read | N/A |
| `params/bg/military.md`, `designs/provincial/military_layer_v30.md` | HARDCODED DUPLICATE (risk) | Independent per-faction Military figures in BG tables; not verified cell-by-cell against the ED-869-corrected 5/6 Crown value — **flagged as an unverified drift risk**, not confirmed drift | Not independently confirmed either way |

---

## 5. Intel

**Home definition.** Canonical name **Intel** (full term "Intelligence capacity"). Range **1–7** (Faction stat table, `references/glossary.md:108`). Home mechanical source: `params/factions/stats_1_7_scale.md:1-42` — this is the *origin* file for the stat's restoration: "Intel restored as canonical stat... per ED-787 Position A 2026-05-03... Spy Ob formula `floor(target Intel / 2) + 1`." Full per-faction rationale table at lines 27-37.

**Exhaustive usage sweep.** Grep (excl. tests) returned 161 files. Core corpus: `params/factions/stats_1_7_scale.md` (canonical), `designs/provincial/faction_canon_v30.md` (Stats tables; Varfell "The Private Collection" M = Intel−2), `faction_behavior_v30.md`, `faction_layer_v30.md`, `references/descriptor_registry.yaml:68` (`fac.intel`), `references/module_contracts.yaml`, `sim/personal/tribunal.py`, `sim/peninsular/ci_track.py`, `sim/provincial/crown_initiative.py`. Also glossary Part Thirteen (`references/glossary.md:260`) notes "INT (track code) | Intel (`Int` faction stat) | RESOLVED — active stat" — confirming there's no longer a naming collision. Also incidental: "Intel" in the ordinary sense of "intelligence" in narrative/arc prose (`designs/npcs/*`, `designs/arcs/*`) describing spycraft narratively, distinct from the stat.

**Divergence check.** None found in range/formula. Worth flagging as a **resolved-but-fragile history**, not a live divergence: Intel was previously STRUCK (ED-748) and only restored by ED-787 — any bulk-corpus file predating 2026-05-03 that still frames Intel as struck/absent (I did not exhaustively verify every one of the ~140 unsampled bulk files for this) would be a stale holdover; I did not find such a holdover in the core corpus I opened, but flag the risk given the number of files not opened.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `params/factions/stats_1_7_scale.md:1-42` | CANONICAL DEFINITION | — | — |
| `references/descriptor_registry.yaml:68` | PULLED/REFERENCED | Pointer | Yes |
| `designs/provincial/faction_canon_v30.md` Stats tables | HARDCODED DUPLICATE (cited) | Literal restatement w/ provenance citation | Yes |
| `references/glossary.md:108,260` | PULLED/REFERENCED (glossary entry) | Cross-references ED-787/the stat table | Yes |
| `sim/personal/tribunal.py`, `sim/peninsular/ci_track.py` | PULLED/REFERENCED | Runtime field reads (`Church.Int`, etc.) | N/A |

---

## 6. Stability (faction)

**Home definition.** Canonical name **Stability**. Range **0–7** (per `faction_canon_v30.md:203-211` stat table, superseding the older 1–7 framing in the glossary's blanket "1–7 scale" statement — settlement/faction docs consistently show Stability able to reach 0 as "Collapse trigger"). Home: `references/descriptor_registry.yaml:69` (`fac.stability`) + `designs/provincial/faction_canon_v30.md §8` (Stability Mechanics — 5 triggers, recovery paths, collapse procedure) + `params/factions/stats_1_7_scale.md` (Leadership Deviation Obs, Failed DA Stability Cost).

**Exhaustive usage sweep.** Grep (excl. tests) returned 250 files (cap hit). Core corpus: `params/factions/stats_1_7_scale.md` (Failed Domain Action Stability Cost §, Leadership Deviation Obs table line 147, "Stability 1 edge case"), `designs/provincial/faction_canon_v30.md §8.1-8.3` (5 triggers, recovery, Collapse — the fullest canonical procedure), `faction_layer_v30.md §1` (the original stability-trigger source faction_canon consolidates from), `faction_behavior_v30.md`, `ci_political_v30.md`, `victory_v30.md` (Stability 0 = "Submitted" for effective hegemony), `designs/scene/derived_stats_v30.md` ("Discipline (from Stability)" = `Stability × 10`), `references/descriptor_registry.yaml:69`, `references/module_contracts.yaml`, `sim/provincial/*` (multiple files reference `.Sta`). Note: "Stability" is *also* the name of a completely different mechanic — **Mending Stability (MS)**, the world clock (glossary Part Two, `references/glossary.md:73`), 100→0 scale. These are two distinct, both-canonical, both-live mechanics sharing the bare word "Stability" (only disambiguated by "Mending" prefix or context) — this is a real naming collision I flag per instructions, though not a *divergence* (both are separately, consistently defined; it's an overload, not a conflict).

**Divergence check.** No numeric divergence found for the faction stat itself once separated from the MS collision above. `designs/provincial/faction_canon_v30.md:279-303` (§8.1-8.3) is the single fullest procedural statement (triggers, recovery caps ±2/season, Collapse six-step procedure) and is explicitly sourced from `faction_layer_v30.md §1` — I did not find the two texts to diverge in the passages I compared, though faction_canon presents itself as the "consolidated" restatement (i.e., a duplicate with citation, not a pure reference).

**Disambiguation.** Two things explicitly excluded/flagged: (1) **Mending Stability (MS)** — a different, both-canonical world clock, not this faction stat, distinguished only by the "Mending" qualifier; conflating the two in a search is a real hazard this audit is built to catch, and I flag it rather than silently merging counts. (2) Ordinary-English "stability" in narrative prose (world/character docs) describing setting conditions, excluded.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/provincial/faction_layer_v30.md §1` | CANONICAL DEFINITION (original) | — | — |
| `designs/provincial/faction_canon_v30.md §8` | HARDCODED DUPLICATE (cited consolidation) | Restates the 5 triggers/recovery/collapse procedure as its own numbered list, citing `faction_layer_v30 §1.2-1.5` throughout | Yes, matches sampled passages |
| `references/descriptor_registry.yaml:69` | PULLED/REFERENCED | Pointer | Yes |
| `designs/scene/derived_stats_v30.md` (Stability×10 Discipline) | PULLED/REFERENCED | Distinct derived-meter formula | Yes |
| `params/factions/stats_1_7_scale.md` (Leadership Deviation Obs, Failed DA cost) | HARDCODED DUPLICATE (cited) | Independent per-faction Ob table, ties back via prose citation to faction_layer | Yes |
| `sim/provincial/*.py` | PULLED/REFERENCED | Runtime `.Sta` field reads | N/A |

---

## 7. Standing (faction, 0–10 per glossary Part Four)

**Home definition as claimed by the batch prompt:** `references/glossary.md:98-112` (Part Four), listing Standing among the faction stats: *"Standing | — | Reputation track. Range 0–10 (exception to 1–7 scale). No in-game benefit above 7; 10 is cosmetic maximum."*

**This is the most significant finding in this batch.** That glossary entry does **not** correspond to any currently-live canonical faction-stat mechanic. Tracing it:

- `references/descriptor_registry.yaml:61-70` — the `faction_stats:` block (explicitly the authoritative descriptor list) lists only `fac.influence, fac.wealth, fac.military, fac.intel, fac.stability` — **five entries, no Standing, and no Mandate** (Mandate is separately derived). Standing is entirely absent from the faction-stats descriptor set.
- `references/descriptor_registry.yaml:108` — Standing is explicitly filed under `not_descriptors: tracks: [Piety, Disposition, Renown, Standing, Persuasion]` — i.e., the registry classifies it as a **track**, not a faction stat, at all.
- `params/factions/stats_1_7_scale.md:1` — "Faction stats (6): Mandate / Influence / Wealth / Military / Intel / Stability." Standing is not in the list.
- `designs/provincial/faction_canon_v30.md:203-211,241-243` (§5.1/§5.3) — "the faction stat lineup is 6-stat... Legitimacy and Popular Support are per-settlement... not faction stats" — an explicit ruling that narrowed the lineup, and Standing isn't even mentioned as a candidate seventh stat here.
- The **live, actually-used** "Standing" mechanic is a **per-character (PC/NPC) rank-within-faction ladder**, canonically defined in `designs/provincial/faction_politics_v30.md:6,38-94`: *"Replace the 0–5 Standing track with an eight-position ladder (Standing 0 through Standing 7)... Standing can fall below 1... drops to Standing **−1** (Dismissed-with-Dishonor)"* — i.e. the currently-canonical range is **0–7, with a −1 "Dismissed" floor state**, and this document explicitly frames itself as replacing a still-earlier **0–5** version. `faction_canon_v30.md §3.2` (cascade formula) also uses `npc.standing` as a per-NPC weight in the same 0–7-ish rank sense, and settlement_layer's Facility Tier gates ("Standing 3+ unlock," "Standing 6+ requires a Wing slot," §1.4.2-1.4.3) all use this same character-rank meaning.
- The literal string **"Standing 0-10"** does exist in the corpus — but only at `params/history/board_game.md:75`, a file whose own header (lines 1-4) reads: *"# params_board_game — Patch History... Do not read this file in simulations — it is history, not values."* That is, the glossary's "0–10" figure traces to an explicitly-deprecated patch-history snapshot, not to any live mechanical doc.

So: three different pictures of "Standing" coexist with no reconciliation —
(a) glossary Part Four: a **faction-level** 0–10 "Reputation track" (top 3 points cosmetic);
(b) `params/history/board_game.md` (explicitly non-canonical history): the same "0–10" figure, likely the glossary's actual source;
(c) `faction_politics_v30.md` (live, current canon): a **per-character** rank ladder, 0–7 with a −1 floor, explicitly described as replacing a prior 0–5 version.

None of these three is the same claim, and the descriptor registry's own classification (Standing = "track," not a faction stat at all) contradicts the glossary's placement of it in the *faction stats* table in the first place.

**Exhaustive usage sweep** (excl. tests, cap 250 hit for bare `\bStanding\b`): core corpus beyond what's quoted above includes `designs/provincial/faction_politics_v30.md` (extensively — rank ladders for all six factions' hierarchies, §1.1b/§1.1c Crown branches, demotion tables lines 65-92), `faction_canon_v30.md §3.2,§10` (cascade weight + sub-organization Standing-gated unlocks), `params/bg/parliament.md:66-74` (PP-515 Open/Closed Pledge "+1 Standing" honour rewards — same per-faction-leader-action-reward sense as faction_canon's Hafenmark sheet), `designs/territory/settlement_layer_v30.md §1.4.2-1.4.3` (Wing-slot gating by Standing), `references/descriptor_registry.yaml:108`, `references/glossary.md:110,259` (Part Thirteen: "CE... RESOLVED"/"INT... RESOLVED" — Standing itself has no Part Thirteen resolution entry despite arguably needing one).

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with glossary's claimed 0–10? |
|---|---|---|---|
| `references/glossary.md:110` (Part Four) | **UNCLEAR / NO LIVE CANONICAL SOURCE** for the 0–10 claim as a *faction* stat | The only textual source for "0–10" is a file marked non-canonical patch history; no live faction-stats descriptor list includes Standing at all | No — nothing live agrees |
| `params/history/board_game.md:75` | Historical (excluded from canon by its own header) | "Do not read this file in simulations — it is history, not values" | N/A — self-disclaimed |
| `designs/provincial/faction_politics_v30.md:6,38` | CANONICAL DEFINITION (of the *actually-live* mechanic, which is a different-scoped thing: per-character rank, 0–7 / −1) | Explicitly "Replace the 0–5 Standing track with..." | Diverges from glossary — 0–7 (+ −1 floor), not 0–10 |
| `references/descriptor_registry.yaml:108` | Classification authority | Files Standing under `tracks`, not `faction_stats` | Contradicts glossary's placement in the faction-stats section entirely |
| `designs/provincial/faction_canon_v30.md §3.2, §10` | HARDCODED DUPLICATE (of the per-character sense) | Uses `npc.standing` and "Standing 3+"/"Standing 6+" gating consistent with faction_politics_v30's ladder | Consistent with (c), not with glossary's (a) |
| `params/bg/parliament.md:66-74` | PULLED/REFERENCED (of the per-character sense) | "+1 Standing" reward, consistent with faction sheets' usage | Consistent with (c) |

**Disambiguation note.** I excluded ordinary-English "standing" (e.g., "standing army," "long-standing," "the player's standing in the community" used loosely in prose) wherever the capitalized game-term markers (a numeric value, a rank-ladder reference, or "Standing N") weren't present.

---

## 8. Legitimacy

**Home definition.** Canonical name **Legitimacy (L)**. Range **0–7**, **per-settlement** (not faction-level — this is itself the resolution of a prior design defect, LPS-1→LPS-2e). Home: `designs/territory/settlement_layer_v30.md:147-180` §1.8 — "institutional/constitutional acceptance (slow-moving...)" — and `references/descriptor_registry.yaml:75-82` (`settlement_stats:` block, `set.legitimacy`, scale "0-7", source cited as `designs/territory/settlement_layer_v30.md §1.8`).

**Exhaustive usage sweep.** Grep (excl. tests) returned 161 files. Core corpus: `settlement_layer_v30.md §1.8` (canonical), `faction_canon_v30.md §3.4,§5,§9` (per-faction sheets' "Legitimacy | 5 | 5" row for Crown/Church etc., and the LPS-1/LPS-2e revision notices embedded throughout: "these dynamics operate per controlled settlement" e.g. lines 491, 667), `faction_behavior_v30.md §3.4` (original PP-686 v2 Legitimacy definition, since re-gra);leveled by LPS-2e), `faction_state_authoring_v30.md §8` (per-faction seed values), `params/factions/stats_1_7_scale.md` (Starting Stats "L" columns, "Mandate Recovery (L + PS independently)" section), `designs/scene/derived_stats_v30.md:325-335,554` (Legitimacy meter = Mandate×20 — the *display buffer*, a different "Legitimacy" than the per-settlement 0-7 stat, reconciled at line 554), `references/descriptor_registry.yaml:78`, `references/module_contracts.yaml:559,567`, `sim/provincial/mass_seizure.py`, `sim/personal/tribunal.py:74,91,102` (`Church.L`), `sim/peninsular/ci_track.py:69-87`.

**Divergence check.** Two things worth flagging as real, non-trivial:
1. **Naming/level overload, resolved but with a lingering display-buffer collision.** There are now *two* things named "Legitimacy": (a) the per-settlement 0–7 political-acceptance stat (canonical, §1.8), and (b) the "**Legitimacy** meter" in `derived_stats_v30.md` which is `Mandate × 20` — a **faction-level display buffer of a different quantity**, sharing the exact same English name. `derived_stats_v30.md:554` explicitly flags and reconciles this: "the faction Legitimacy meter = Mandate × 20 is the displayed aggregate... its footnote claiming 'PP-686 split Mandate into faction-level L+PS' is corrected by this section." So the collision is *known and annotated*, but it means any bare grep for "Legitimacy" mixes two distinct 0-range quantities (0-7 per-settlement stat vs. 0-140 derived display buffer) under one name — worth flagging per the audit's instructions on "two genuinely distinct mechanics sharing one name."
2. **Sim-code non-implementation** — as documented under Mandate above, `sim/territory/registry.py:60-64` explicitly states the `legitimacy`/`popular_support` fields are declared with the correct 0–7 bounds but are "NEVER READ OR WRITTEN anywhere in sim/" — an inert stub, not a working per-settlement pipeline. `sim/`'s actual working Legitimacy proxy is `Faction.L` (pre-LPS-1 scalar, per Mandate section above) — the same divergence propagates here.
3. No conflicting *numeric range* found (0–7 is consistent everywhere the per-settlement stat is named with a range).

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/territory/settlement_layer_v30.md §1.8` | CANONICAL DEFINITION | — | — |
| `references/descriptor_registry.yaml:78` | PULLED/REFERENCED | Pointer, scale annotated | Yes |
| `designs/provincial/faction_canon_v30.md` (per-faction sheets) | HARDCODED DUPLICATE (cited) | Restates per-faction seed L values, explicit "[Per LPS-1 (settlement_layer §1.8)]" citations throughout | Yes |
| `designs/scene/derived_stats_v30.md:297,325-335,554` | Distinct mechanic sharing the name (flagged above, not a simple PULLED/REFERENCED) | Explicitly reconciled at line 554 as "the displayed aggregate," not a re-derivation of the per-settlement stat | Yes, but only because of the explicit reconciliation note — without it this would read as a silent conflict |
| `sim/territory/registry.py:59-65` | HARDCODED DUPLICATE (inert) | Declares `L_PS_MIN,MAX=0,7` bounds citing §1.8, but self-flags as unwired | Bounds agree; pipeline doesn't exist |
| `sim/provincial/mass_seizure.py`, `sim/personal/tribunal.py`, `sim/peninsular/ci_track.py` | HARDCODED DUPLICATE (self-flagged pre-LPS-1) | Uses `Faction.L` as the working proxy, the superseded scalar model | No — implements the pre-LPS-1 model, not settlement-grain L |

---

## 9. Popular Support

**Home definition.** Canonical name **Popular Support (PS)**. Range **0–7**, per-settlement. Same home as Legitimacy: `designs/territory/settlement_layer_v30.md §1.8` + `references/descriptor_registry.yaml:79` (`set.popular_support`).

**Exhaustive usage sweep.** "Popular Support" (as a phrase, excl. tests) returned 69 files. Core corpus overlaps almost entirely with Legitimacy's: `settlement_layer_v30.md §1.8`, `faction_canon_v30.md §3.4,§5,§9` (per-faction PS rows and dynamics sections), `faction_behavior_v30.md §3.4` (original PP-686 v2 formula: `ΔPopular_Support = α·attributed_mission_outcome + β·cascade_fidelity·outcome_polarity_gate + γ·shock`), `faction_state_authoring_v30.md §8`, `params/factions/stats_1_7_scale.md` ("Mandate Recovery (L + PS independently)"), `references/descriptor_registry.yaml:79`, `references/module_contracts.yaml:559`, `designs/personal/conviction_taxonomy_v30.md`, `sim/territory/registry.py:65`.

**Divergence check.** No numeric divergence found (0–7 consistent). The formula for its *seasonal change* (Δ per season, quoted above from `faction_behavior_v30.md §3.3` / mirrored verbatim in `faction_canon_v30.md §3.3.2`'s surrounding text, "ΔPopular_Support per season = α_temperament × attributed_mission_outcome... + β_temperament × cascade_fidelity... + γ × shock") is consistent between the two files I compared it in. Same sim-oracle non-implementation caveat as Legitimacy applies (registry.py field inert, `sim/` actually tracks a scalar equivalent under the pre-LPS-1 model where PS doesn't independently exist — the code files I grepped for Mandate/Legitimacy above reference only `.L`, not a parallel `.PS` field on `Faction`, meaning **Popular Support has even less code-side existence than Legitimacy** in the current oracle — worth flagging as a slightly deeper gap than Legitimacy's, since Legitimacy at least has an inert stub field on `Settlement` while Popular Support's *faction*-level proxy doesn't appear on `Faction` at all in the files sampled).

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/territory/settlement_layer_v30.md §1.8` | CANONICAL DEFINITION | — | — |
| `references/descriptor_registry.yaml:79` | PULLED/REFERENCED | Pointer | Yes |
| `designs/provincial/faction_canon_v30.md §3.4,§5,§9` | HARDCODED DUPLICATE (cited) | Restates Δ-formula and per-faction PS values with citations | Yes |
| `designs/provincial/faction_behavior_v30.md §3.4` | CANONICAL DEFINITION (of the Δ-formula specifically — this is the PP-686 v2 origin faction_canon consolidates from) | — | — |
| `sim/territory/registry.py:65` | HARDCODED DUPLICATE (inert) | `popular_support: int = 0` field declared, unused per its own comment | Bound agrees; unimplemented |

---

## 10. Prosperity

**Home definition.** Canonical name **Prosperity**. Range **0–5**, per-settlement. Home: `designs/territory/settlement_layer_v30.md:41-61` §1.3 ("Economic output and quality of life... Each point of settlement Prosperity adds to the province's Prosperity pool") + `references/descriptor_registry.yaml:80` (`set.prosperity`, scale "0-5").

**Exhaustive usage sweep.** Grep (excl. tests) returned 207 files. Core corpus: `settlement_layer_v30.md §1.3,§1.8` (also used inside the Settlement Weight formula, `W_s = base(Type)+Prosperity_s+FacilityTier_s`), `designs/scene/derived_stats_v30.md:378` ("Local Economy" = `Prosperity × 50`), `references/module_contracts.yaml:557,587-588` (`formula: "Prosperity × 50"`), `references/descriptor_registry.yaml:80`, `designs/territory/governance_play_redesign_v1.md:43-60` ("Develop" verb: "Prosperity +1"), `sim/territory/registry.py:41,54` (`STAT_MIN,MAX=0,5`), `designs/provincial/peninsular_strain_v30.md §2` (Accord/Effective Prosperity — see divergence below), `designs/provincial/faction_canon_v30.md §5.1` (Weight formula restatement), `designs/provincial/military_layer_v30.md`, `mass_battle_v30.md`, `params/history/mass_combat.md`.

**Divergence check — a genuine, previously-unflagged gap.** `designs/provincial/peninsular_strain_v30.md:49-62` §2 ("Accord — Per-Territory Attribute") defines **"Effective Prosperity"** as: *"A territory's base Prosperity (from params_board_game.md territory table) is modified by Accord"* (line 53), with an Accord-based modifier table (Aligned/Compliant = full; Resistant = 0; Revolt = territory Uncontrolled). I grepped `params/board_game.md` for "Prosperity" (case-insensitive) and got **zero hits** — the "territory Prosperity table" this canonical, CANONICAL-status doc cites **does not exist in the file it names**. This reads as a stale citation surviving the settlement-layer migration: Prosperity was relocated to be a per-*settlement* stat (0–5, §1.3) as part of the LPS/settlement-layer redesign, and `peninsular_strain_v30.md §2`'s "base Prosperity... territory table" framing was never updated to point at the new source or to specify how per-settlement Prosperity aggregates up to a "territory's base Prosperity" (settlement_layer §1.3 only specifies this aggregation for **Order** → province Accord, via `floor(mean(settlement Order))` — no analogous aggregation rule for Prosperity → territory Prosperity is stated anywhere I found). This means "Effective Prosperity" as used in the Accord table is currently **UNCLEAR / NO CANONICAL SOURCE** for how it's computed from the settlement-grain Prosperity that is otherwise canonical — a live gap, not merely stale prose, since the Accord mechanic actively depends on it every Govern/Trade Ob calculation (`peninsular_strain_v30.md:62`: "Govern Ob and Trade Ob use base Prosperity").

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/territory/settlement_layer_v30.md §1.3` | CANONICAL DEFINITION (settlement-grain, 0-5) | — | — |
| `references/descriptor_registry.yaml:80` | PULLED/REFERENCED | Pointer | Yes |
| `designs/scene/derived_stats_v30.md:378` | PULLED/REFERENCED | Distinct derived formula (Local Economy) | Yes |
| `references/module_contracts.yaml:557,587-588` | HARDCODED DUPLICATE (cited) | Restates `Prosperity × 50` literally | Yes |
| `sim/territory/registry.py:41,54` | HARDCODED DUPLICATE (cited) | `STAT_MIN,STAT_MAX = 0,5` constant, comment cites §1.3 | Yes |
| `designs/provincial/peninsular_strain_v30.md §2 ("Effective Prosperity")` | **UNCLEAR / NO CANONICAL SOURCE** | Cites `params/board_game.md territory table`, which contains no "Prosperity" text at all (verified by direct grep) — a dangling reference with no stated settlement→territory aggregation rule | Cannot be evaluated — the source it names doesn't exist |
| `designs/territory/governance_play_redesign_v1.md:43` | PULLED/REFERENCED | Uses settlement-grain Prosperity consistent with §1.3 (the "Develop" verb) | Yes |

---

## 11. Defense (settlement)

**Home definition.** Canonical name **Defense**. Range **0–5**, per-settlement. Home: `designs/territory/settlement_layer_v30.md:41-61` §1.3 ("Fortification and garrison readiness... Defense 0 = undefended (auto-capture). Defense 5 = major fortress") + `references/descriptor_registry.yaml:81` (`set.defense`, scale "0-5").

**Exhaustive usage sweep.** Grep `\bDefense\b|\bDefence\b` (excl. tests) returned 250 files (cap hit) — but this is heavily inflated by incidental usage: "Defense" appears as an ordinary English/military-domain word throughout `designs/provincial/mass_battle_v30.md`, `military_layer_v30.md`, combat design docs ("Damage Resistance," "defensive branch," siege "defenders"), and the entire `research/pre_firearms_formations/*` historical-research corpus (0 hits there in my targeted check, but the broader `\bDefense\b` sweep pulls in many combat/mass-battle files using the word generically). Core, mechanically-precise corpus for the *settlement stat*: `settlement_layer_v30.md §1.3,§1.8` (also feeds Settlement Weight indirectly — no, actually Weight uses Prosperity+FacilityTier, not Defense, per §1.8 formula — Defense is *not* a Weight input, only Prosperity and FacilityTier are), `designs/scene/derived_stats_v30.md:379,422-430` ("Garrison Strength" = `Defense × 20 + Fort Level × 30`; "Settlement Combat Defense Feedback" table), `references/module_contracts.yaml:557,591-592` (`formula: "Defense × 20 + Fort × 30"`), `references/descriptor_registry.yaml:81`, `sim/territory/registry.py:41,55` (`STAT_MIN,MAX=0,5`; `defense: int = 0` field, `fort_level` tracked separately). Notably `designs/provincial/military_layer_v30.md` itself returned **zero** hits for "Defense" in my targeted grep — siege/attack mechanics there apparently route through "Fort Level" rather than citing the settlement Defense stat by name in that file, which is at minimum a legibility gap (the settlement stat that's supposed to determine "Ob for attackers," per settlement_layer §1.3, isn't named in the doc that would operationalize sieges) though I did not find a contradicting alternate definition there.

**Divergence check.** No numeric-range divergence found for the stat itself (0–5 consistent). The derived formula (`Defense × 20 + Fort Level × 30`) is consistent between `derived_stats_v30.md:379` and `module_contracts.yaml:591-592`. The one soft finding is the military_layer_v30.md silence noted above — not a contradiction, but a possible missing propagation link.

**Disambiguation.** Excluded: the large incidental "Defense/defensive" usage across combat and mass-battle docs describing combat-branch mechanics (parry/dodge/"defensive branch"), Damage Resistance (a *combat* term, Part Five of the glossary, not this settlement stat), and generic military-domain prose in `mass_battle_v30.md`/`military_layer_v30.md`.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/territory/settlement_layer_v30.md §1.3` | CANONICAL DEFINITION | — | — |
| `references/descriptor_registry.yaml:81` | PULLED/REFERENCED | Pointer | Yes |
| `designs/scene/derived_stats_v30.md:379,422-430` | PULLED/REFERENCED (formula match) but also HARDCODED DUPLICATE in the literal sense (restates the formula, not merely cites it) | `Defense × 20 + Fort Level × 30`, no explicit "see §1.3" citation attached at this exact line (contrast with Mandate's line 554 which does cite) | Yes |
| `references/module_contracts.yaml:591-592` | HARDCODED DUPLICATE (cited) | Restates formula, tagged "§1.3" | Yes |
| `sim/territory/registry.py:41,55` | HARDCODED DUPLICATE (cited) | `STAT_MIN,MAX` constant + `fort_level` separate field | Yes |
| `designs/provincial/military_layer_v30.md` | Gap (no occurrence) | Siege rules don't name the Defense stat at all in this file | Cannot confirm consistency — nothing to check |

---

## 12. Order (settlement — excluding incidental non-mechanical uses)

**Home definition.** Canonical name **Order**. Range **0–5**, per-settlement. Home: `designs/territory/settlement_layer_v30.md:41-61` §1.3 ("Local institutional stability and compliance... Order 0 = local revolt. Order 3+ = stable governance. Feeds upward into province Accord") + `references/descriptor_registry.yaml:82` (`set.order`, scale "0-5"). Critically distinguished from **Accord** (a *different*, province-level 0–3 attribute) by `peninsular_strain_v30.md:142-148` §2.4b, which is itself the canonical disambiguation: *"Accord (0–3) is a province-level attribute... Order (0–5) is a settlement-level attribute... They are independent... Both can reach 0 simultaneously"* — and by an explicit aggregation rule: **Province Accord = floor(mean(settlement Order))** (settlement_layer §1.3, restated at `peninsular_strain_v30.md:61,218,240`).

**Exhaustive usage sweep.** `\bOrder\b` (excl. tests) returned 250 files (cap hit) — the overwhelming majority of this is **incidental English usage** ("in order to," "Resolution Priority Order," alphabetical/sequence "order," religious "Order" as in "Templar Order"/"Cardinal... Order," "Ministry Order," mermaid `flowchart TD` note in the glossary's own Part Twelve collision table about "Top-Down" vs the retired "Thread Depth" abbreviation). I explicitly excluded all of these. Mechanically-precise "Order" (the settlement stat) core corpus: `settlement_layer_v30.md §1.3` (canonical), `designs/scene/derived_stats_v30.md:380,552` ("Public Order" = `Order × 20`), `references/module_contracts.yaml:557-558,568-573` ("Prosperity/Defense/Order" bucket, "when: settlement Defense = 0" — note this trigger condition names Defense not Order, worth a light gap-flag but not investigated further), `designs/provincial/peninsular_strain_v30.md §2.1,§2.4b,§2.5` (extensive: Accord derivation *from* Order, ED-626's explicit scale distinction, §2.5 "Settlement Targeting Specification" Category A/B tables specifying exactly which settlements' Order values change for each trigger type), `designs/territory/governance_play_redesign_v1.md:45,49,60,122` ("Keep Order" verb: Order+1; "Levy": Order−1; `settlement.Order <= 2` condition), `sim/territory/registry.py:41,56` (`order: int = 0` field, same 0–5 bound as Prosperity/Defense).

I explicitly verified `params/board_game.md`'s one "Order" hit (line 217, "Phase 4 Resolution Priority Order") is incidental, not the stat — confirmed by direct read.

**Divergence check.** No numeric divergence found once incidental hits are filtered — 0–5 is consistent everywhere the settlement stat is actually meant. The Order/Accord distinction is unusually *well*-documented for this corpus (an explicit ED-626 section exists specifically to prevent the two being confused, `peninsular_strain_v30.md §2.4b`) — this is a case where the corpus pre-empted the exact confusion this audit looks for, worth noting as a positive counter-example rather than a defect. One soft note: `module_contracts.yaml:571` ("when: settlement Defense = 0") — the derived-value-zero trigger is stated for Defense in this line but the surrounding bucket comment groups "Prosperity/Defense/Order" together; I did not find a parallel explicit "Order = 0" trigger condition stated at this exact site (settlement_layer's own prose does state "Order 0 = local revolt" as the trigger elsewhere) — a minor completeness gap in module_contracts.yaml's contract listing, not a contradiction.

**Disambiguation.** Excluded explicitly: "in order to" and similar connective phrases; "Resolution Priority Order" (params/board_game.md:217, sequencing, not the stat); religious/institutional "Order" (Templar Order, Church "Four-Cardinal structure," Löwenritter "Order," Riskbreaker/Inquisitor sub-orders — a proper-noun sense unrelated to the stat); the glossary's own `flowchart TD` Mermaid-syntax disambiguation note (Part Twelve) which is about an unrelated "TD" abbreviation collision, not "Order" itself, but appeared adjacent in some greps.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/territory/settlement_layer_v30.md §1.3` | CANONICAL DEFINITION | — | — |
| `references/descriptor_registry.yaml:82` | PULLED/REFERENCED | Pointer | Yes |
| `designs/scene/derived_stats_v30.md:380,552` | HARDCODED DUPLICATE (uncited at this line) | Restates `Order × 20` without an inline citation back to §1.3 at this specific line (contrast Mandate's explicit line-554 citation) | Yes |
| `references/module_contracts.yaml:557-558,568-573` | HARDCODED DUPLICATE (cited) | Restates bucket + derivation, tagged §1.3 | Yes |
| `designs/provincial/peninsular_strain_v30.md §2.1,§2.4b,§2.5` | PULLED/REFERENCED (explicitly, and unusually well) | Cites `settlement_layer_v30 §1.3` by name for the Accord-derivation rule; ED-626 section is dedicated disambiguation prose, not an independent restatement of Order's own definition | Yes |
| `sim/territory/registry.py:41,56` | HARDCODED DUPLICATE (cited) | `STAT_MIN,MAX=0,5` shared constant across Prosperity/Defense/Order | Yes |
| `designs/territory/governance_play_redesign_v1.md:45,49,122` | PULLED/REFERENCED | Uses Order consistently as the settlement-grain stat | Yes |

---

## 13. Settlement Weight

**Home definition.** Canonical name **Settlement Weight (W_s)**. No fixed range stated as a closed interval — "undeveloped Outpost W=1 → fully-developed Seat W=11" (an open-ended, developmentally-bounded value). Formula: `designs/territory/settlement_layer_v30.md:158-163` §1.8 — `W_s = base(Type) + Prosperity_s + FacilityTier_s`, where `base(Type)` ∈ {Seat 3, City 3, Cathedral 3, Town 2, Fortress 2, Port 2, Village 1, Mine 1, Outpost 1}, `Prosperity_s` ∈ 0–5, `FacilityTier_s` ∈ 0–3. This is the sole canonical home; the term is coined in this section and doesn't pre-exist elsewhere.

**Exhaustive usage sweep.** "Settlement Weight" as an exact phrase returned only **7 files**: `designs/territory/settlement_layer_v30.md` (canonical), `designs/provincial/faction_canon_v30.md:216,221` (§5.1 restates the formula inline: *"Settlement Weight W and full spec authoritative in settlement_layer §1.8, LPS-2e"* — explicitly deferring, not claiming independent authority), `designs/audit/2026-07-08-pessimist-action-audit/01_workings/dossier_SE.md` (audit dossier, sampled — cites the term consistently), and four archive/session-log files (`archives/session/session_log_audit_2026-05-31_...md`, `archives/handoffs/2026-05-29-...yaml`, `archives/audit/2026-06-06-architecture-map/valoria_system_hierarchy_map.md`, `archives/audit/2026-05-30-lps-mandate-ners-audit/lps_mandate_comprehensive_ners_audit.md` — all historical/non-canonical per CLAUDE.md, sampled for consistency, none contradicted the formula). The bare word "Weight" alone (not searched exhaustively here, would pull in unrelated hits like dice-pool "weighting" language) was not separately swept — flagged as a scope limitation.

**Divergence check.** No divergence found — this is a narrow, recently-coined (2026-05-30, LPS-2e) term with a single restatement site (`faction_canon_v30 §5.1`) that explicitly defers to settlement_layer rather than claiming independent authority, and `references/module_contracts.yaml:600` (`"W_s = base(Type)+Prosperity+FacilityTier"`) matches exactly.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/territory/settlement_layer_v30.md §1.8` | CANONICAL DEFINITION | — | — |
| `designs/provincial/faction_canon_v30.md:216,221` | HARDCODED DUPLICATE (explicitly self-deferring) | Restates the formula as literal text but explicitly appends "authoritative in settlement_layer §1.8" in the same breath | Yes |
| `references/module_contracts.yaml:600` | HARDCODED DUPLICATE (cited) | Restates formula in the damper/derivation blocks | Yes |
| `designs/audit/2026-07-08-pessimist-action-audit/01_workings/dossier_SE.md` | PULLED/REFERENCED | Audit-prose citation | Yes |
| Archive/session-log files (4, sampled) | PULLED/REFERENCED (historical) | Changelog/audit narrative | Consistent where sampled |

---

## 14. Facility Tier

**Home definition.** Canonical name **Facility Tier (FacilityTier_s)**. Range **0–3**: "0 billets only / 1 Chambers / 2 Suites / 3 Wings" (`designs/territory/settlement_layer_v30.md:162`, §1.8), operationalized against the fuller slot-capacity table at §1.4.1 (`settlement_layer_v30.md:67-79`, "Wing/Suite/Chamber/Billet Slots by Settlement Type").

**Exhaustive usage sweep.** "Facility Tier" as an exact phrase returned only **1 file**: `designs/territory/settlement_layer_v30.md` itself. The related internal variable name `FacilityTier` (no space) appears in `references/module_contracts.yaml:600` (`"W_s = base(Type)+Prosperity+FacilityTier"`). The related concept "Institutional Facility Tiers (PP-661)" heading (`settlement_layer_v30.md:63`) and "facility_tier" as a code field appears in `sim/territory/registry.py:67` (`facility_tier: int = 0`) — declared but, notably, **without a corresponding `FACILITY_TIER_MIN/MAX` bound constant** analogous to `STAT_MIN/MAX` (0-5) and `L_PS_MIN/MAX` (0-7) defined two lines above it (lines 41-42) — i.e. even the code-side "hardcoded duplicate" of the settlement-stat bounds is **incomplete**: it duplicates the 0–5 and 0–7 bounds but not the 0–3 Facility Tier bound. No other file in the repo (including the ~15 previously-seen "Facility Tier" grep hits from the broader "Facility Tier" search reported by the tool earlier, which actually returned only these plus generic-English "tier" mentions I did not open) restates a competing range.

**Divergence check.** No competing definition found. The one real finding is the code-side asymmetry just described: Facility Tier's bound (0–3) is the *only* one of the three "§1.4/§1.8 formula input" bounds (Prosperity 0–5, FacilityTier 0–3, and the L/PS 0–7 used downstream) that has **no enforcement constant anywhere in `sim/`** — a gap in the "hardcoded duplicate" pattern rather than a conflicting duplicate.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/territory/settlement_layer_v30.md §1.4,§1.8` | CANONICAL DEFINITION | — | — |
| `references/module_contracts.yaml:600` | PULLED/REFERENCED (bare variable name, no range restated) | Only names `FacilityTier` inside the Weight formula string; does not state its 0–3 bound independently | Yes (nothing to disagree with) |
| `sim/territory/registry.py:67` | HARDCODED DUPLICATE (incomplete) | `facility_tier: int = 0` field exists, but unlike the two sibling bound-constants at lines 41-42, **no min/max constant is defined for it anywhere in the file** | N/A — the duplicate is missing its bound, so there's nothing to compare for agreement/drift; this is itself the finding |

---

## 15. Cascade Fidelity

**Home definition.** Canonical name **Cascade Fidelity**. Range **[−1, +1]** (cosine similarity). Formula, originally defined at `designs/provincial/faction_behavior_v30.md:210-216` §3.3.2 (this is the true origin — PP-686 v2): `cascade_fidelity(faction) = cosine_similarity(aggregate_effective_convictions(faction), expected_convictions(faction.role))`. "1 = perfect role fidelity; 0 = orthogonal; -1 = inverse."

**Exhaustive usage sweep.** "Cascade Fidelity" as an exact phrase returned **23 files**. Core corpus: `designs/provincial/faction_behavior_v30.md §3.3.2` (canonical origin, plus its use in the ΔPopular_Support and ΔLegitimacy formulas at lines 233-237, 292-298, and the violation-scoring list at lines 313-317, and edge-case handling at line 394: "Cosine similarity zero-magnitude vectors | cascade_fidelity = 0 (mathematical fallback)"), `designs/provincial/faction_canon_v30.md §3.3` (verbatim restatement, "Range [-1, +1]. 1 = perfect role fidelity; 0 = orthogonal; -1 = inverse" — matches faction_behavior exactly), `designs/architecture/key_type_registry_v30.md`, `references/module_contracts.yaml:65` (`cascade_fidelity: <-1..+1>` — the Key/registry type declaration), `designs/personal/conviction_axis_matrix_v30.md`, `designs/personal/conviction_track_v1_pp718_vetting.md`, `designs/npcs/character_canon_v30.md`, `designs/proposals/2026-05-25-mechanics-integration-v3_1.md`. Remainder (~13 files) are audit dossiers/critique docs (`designs/audit/2026-05-08-*`, `2026-04-30-architecture-session/*`) discussing/citing the mechanic, and 2 archive files — sampled, consistent.

**Divergence check.** None found. This is a clean case: `faction_behavior_v30.md` is the unambiguous single origin (it's where PP-686 v2 was authored), `faction_canon_v30.md` explicitly frames itself as consolidating from faction_behavior (front-matter line 1: "consolidates... references, does not duplicate" — though again it does restate the formula as literal text, same pattern as elsewhere in this batch), and `module_contracts.yaml`'s bare range annotation matches. I found no instance of a different formula, different range, or a stale pre-cosine-similarity version surviving anywhere.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees today? |
|---|---|---|---|
| `designs/provincial/faction_behavior_v30.md §3.3.2` | CANONICAL DEFINITION | — | — |
| `designs/provincial/faction_canon_v30.md §3.3` | HARDCODED DUPLICATE (cited consolidation) | Verbatim-matching restatement, cites source in front matter | Yes |
| `references/module_contracts.yaml:65` | PULLED/REFERENCED | Bare range annotation only, no formula restated | Yes |
| `designs/architecture/key_type_registry_v30.md` | PULLED/REFERENCED | Key-type registry entry citing the mechanic | Yes |
| `designs/personal/conviction_axis_matrix_v30.md`, `character_canon_v30.md` | PULLED/REFERENCED | Prose usage consistent with the formula, no independent redefinition | Yes |
| Audit dossiers (~13, sampled) | PULLED/REFERENCED | Analysis citing the ratified mechanic | Consistent where sampled |

---

## 16. Turmoil (glossary Part Eleven's top-level system name) vs Strain (the term dominating peninsular_strain_v30.md's body)

**Home definition, as named.** `references/glossary.md:225` (Part Eleven) declares: *"Turmoil | `designs/provincial/peninsular_strain_v30.md` | Cross-cutting world-scale pressure system (T-07 throughline). Multi-graph hub..."* — i.e. the glossary's canonical name for the system housed in `peninsular_strain_v30.md` is **Turmoil**. But `peninsular_strain_v30.md` itself is titled **"VALORIA BG — Turmoil System v1"** (line 1) and its operative section is **"§4 Turmoil Counter — NEW"** (line 286: *"Global track, range 0–10. Starts at 0."*) — yet virtually the entire body text under that heading calls the same track **"Strain"**: §4.1 is titled **"Advancing Strain"** (line 290), §4.2 **"Reducing Strain"** (line 302), §4.3 **"Strain Threshold Effects"** (line 314, with named bands "Strain 0-2 Peace... Strain 9-10 Collapse"), §4.4 **"Strain and IP — Shared Signal, Independent Aggregation"** (line 326). The word "Turmoil" occurs only a handful of times in this 602-line document (title, §4 heading, §6.1/§6.3 victory-condition thresholds "Turmoil ≤ 6," §7 step 4d heading "Turmoil update," and the Accord-checks step "Turmoil +1" at line 483) — every other operative mechanical mention (advancement triggers, decay triggers, threshold-effect table, the IP/Strain shared-signal reconciliation) says **"Strain."**

**This exact tension — "Turmoil" as the section/system title vs. "Strain" as the operative body-text name — is the single most load-bearing inconsistency in this whole batch, and it is not confined to peninsular_strain_v30.md.** It propagates into at least two other canonical documents:

- **`designs/provincial/clock_registry_v30.md:19`** (the canonical clock registry): `| Turmoil | 0–10 | 0 | ↑ (bad) | peninsular_strain_v30.md §4. Replaces Parliament Integrity...` — uses "Turmoil" exclusively, consistent with the glossary.
- **`params/bg/clocks.md:41`** — a single sentence switches names mid-stream for what is unambiguously the same counter: *"Each season with inter-faction battle: IP +2. Each season with inter-faction battle: **Turmoil** +1. Faction elimination: **Strain** +2. Territory Revolt (Accord 0): **Strain** +1."* Three consecutive clauses about the same track use "Turmoil" once and "Strain" twice.
- **`designs/provincial/victory_v30.md`** — line 22 ("See also: ... peninsular_strain_v1.md (Accord, **Turmoil**, universal victory condition...)"), lines 45/65 (win-condition table: **"Turmoil ≤ 6"**), line 88 (§0.3 heading **"Turmoil Counter"**), line 90 (body: *"Global track (0–10). Advances from territory-instability... Direct battle-occurrence no longer advances **Strain** (ED-743)"* — heading says Turmoil, very next sentence says Strain), line 94 (*"~~Strain +1~~ STRUCK... IP and Strain advance from Accord-based..."*), and then at **line 752**, in the actual Victory Conditions summary table, the same "peninsula not in crisis" threshold that lines 45/65 called **"Turmoil ≤ 6"** is restated as **"Strain ≤ 6"** — i.e. the identical numeric win-condition is given under both names in the same file with no cross-reference reconciling them.
- **`designs/scene/derived_stats_v30.md`** also carries both names for what reads as the same mechanic: line 333 "**Turmoil** Mandate check failure: Legitimacy −25 AND Mandate −1" vs. line 469 "**Strain** 3–4: Mandate check → Mandate −1" and line 495 "**Turmoil** ≥7: Mandate check."

**Exhaustive usage sweep.** "Turmoil" (excl. tests) returned 182 files; bare "Strain" (excl. tests, which also catches unrelated English "strain" usage e.g. "strains the down-tier" in governance_play_redesign) returned 243 files. Given the scale, the core canonical corpus is: `peninsular_strain_v30.md` (title + §4, both names as shown above), `clock_registry_v30.md:19` (Turmoil only), `params/bg/clocks.md:41` (both, same sentence), `victory_v30.md` (both, same file, same threshold — shown above), `derived_stats_v30.md` (both, shown above), `references/module_contracts.yaml:664` ("MS / IP / CI / **Turmoil** / Accord / Mandate..." — Turmoil only), `references/glossary.md:225` (Turmoil only, the nominal canonical name), `faction_canon_v30.md` §3.4 ("Strain shifts territories toward outcomes-only" — Strain, describing the same world-pressure effect on faction temperament), `designs/provincial/ci_political_v30.md`, `faction_layer_v30.md` (both terms appear in supporting mechanical cross-references, not independently re-verified line-by-line here given volume). Filename itself (`peninsular_strain_v30.md`) uses "Strain," while its in-file title and the glossary's Part Eleven registration both use "Turmoil" — a third axis of the same inconsistency (filename vs. title vs. body).

**Divergence check.** This is not a numeric-range divergence (0–10 is consistent under either name, in every citation I found) — it is a **naming-identity divergence on the system's own canonical name**, occurring *within single documents*, at the filename/title/heading/body-text level simultaneously, and propagating into at least three other canonical files (`clock_registry_v30.md` picked "Turmoil" consistently; `params/bg/clocks.md` and `victory_v30.md` and `derived_stats_v30.md` did not standardize on either). Per the audit's own framing (term 16's prompt: "the term a prior audit found dominates the file's actual body text"), this confirms and extends that prior finding — the split runs deeper than "title says Turmoil, body says Strain": even the *files that are supposed to be citing the system consistently* (clocks.md, victory_v30.md, derived_stats_v30.md) inherited the same internal split rather than resolving to one name.

**Step 4 classification.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees on identity? |
|---|---|---|---|
| `designs/provincial/peninsular_strain_v30.md` (title, line 1) | CANONICAL DEFINITION — declares itself "Turmoil System v1" | — | Title says Turmoil |
| `designs/provincial/peninsular_strain_v30.md §4` (lines 286-333, body) | Same document, same section — restates as "Strain" throughout | Self-contradiction within one canonical file; not a separate site so much as the file disagreeing with its own heading | Body says Strain |
| `references/glossary.md:225` (Part Eleven) | PULLED/REFERENCED (registers the system's canonical name) | Cites peninsular_strain_v30.md as the doc, names the system "Turmoil" | Agrees with the file's title, not its body |
| `designs/provincial/clock_registry_v30.md:19` | HARDCODED DUPLICATE (cited) | Restates range (0-10) and start (0) as literals, cites "peninsular_strain_v30.md §4"; picked "Turmoil" | Internally consistent, matches glossary |
| `params/bg/clocks.md:41` | HARDCODED DUPLICATE | Independent restatement, uses **both names in one sentence** for the same track | Internally inconsistent |
| `designs/provincial/victory_v30.md` (multiple lines: 22,45,65,88,90,94,752) | HARDCODED DUPLICATE | Independent restatement of the same win-condition threshold under **both names within the same file** (lines 45/65 "Turmoil ≤ 6" vs. line 752 "Strain ≤ 6") | Internally inconsistent — same numeric threshold, two names, no cross-reference |
| `designs/scene/derived_stats_v30.md:333,469,495` | HARDCODED DUPLICATE | Independent restatement of threshold-triggered Mandate-check consequences under **both names** | Internally inconsistent |
| `references/module_contracts.yaml:664` | PULLED/REFERENCED | Bare enumeration ("...Turmoil..."), no formula restated | Uses "Turmoil" only |
| `designs/provincial/faction_canon_v30.md §3.4` (Public Temperament) | PULLED/REFERENCED | "Strain shifts territories toward outcomes-only" — references the pressure system's *effect*, using "Strain" | Uses "Strain" only |
| Filename `peninsular_strain_v30.md` itself | N/A — structural artifact | The file's own filename encodes "strain," while its in-file title encodes "Turmoil" — a third, orthogonal axis of the same unresolved naming split | Disagrees with its own title line |

---

## Cross-cutting observations surfaced by this batch (raw material, not synthesis)

A few patterns recurred across multiple terms above and are worth naming as bare facts, since they bear directly on the "single-source" diagnostic this audit series is built around, without editorializing on remediation:

- **The `sim/` oracle is running an entire generation behind the doc corpus for the faction/settlement layer**, and — unusually for this kind of drift — the repo already knows it and has fenced it with explicit `[PRE-LPS-1 / PORT-BLOCKING — ED-FA-0004]` comments in half a dozen files (`game_state.py`, `parliamentary_vote.py`, `crown_initiative.py`, `accounting.py`, `registry.py`). Mandate, Legitimacy, and Popular Support are all affected; the settlement-side `legitimacy`/`popular_support` fields exist as declared-but-unwired stubs, and Facility Tier's bound isn't even stubbed.
- **The "restate the formula but also cite the source" pattern** (module_contracts.yaml, faction_canon_v30.md, derived_stats_v30.md) recurs for nearly every derived formula in this batch (Mandate, Prosperity, Defense, Order, Settlement Weight, Cascade Fidelity). Per the audit's classification rules this counts as HARDCODED DUPLICATE rather than PULLED/REFERENCED, because a literal copy exists independent of the citation — the citation reduces drift risk but does not eliminate the duplicate-maintenance surface.
- **Term 7 (Standing) is the one place in this batch where the glossary's own "home definition" does not correspond to any live mechanic** — the 0–10 figure traces only to a file whose header says not to treat it as canonical, while the actually-operative mechanic (a 0–7 rank ladder with a −1 floor, in `faction_politics_v30.md`) is a different, unreconciled thing that the descriptor registry files under a different category (`tracks`, not `faction_stats`) entirely.
- **Term 16 (Turmoil/Strain) is not a two-way split but at least a four-way one**: filename ("strain"), in-file title/section-heading ("Turmoil"), in-file operative body text ("Strain"), and downstream citing documents that inherited the split rather than resolving it (clocks.md, victory_v30.md, derived_stats_v30.md each use both names for the identical mechanical quantity within a single file).
