# Gap-closure G2 — faction-doc verifications

_Archived verbatim from the agent's final message (2026-07-07)._

# Gap-Closure Verification Report — G2

## 1. C-FA-7 (Legitimacy λ formula)

**Read:** `designs/provincial/faction_behavior_v30.md` §3.5 in full (lines 283–397, through §3.6–§3.9 and §4 Mandate).

**Verdict: C-FA-7 FALLS.** §3.5 contains a complete, quantified ΔLegitimacy formula:
```
ΔLegitimacy per season = +λ_continuity × seasons_in_role_uninterrupted
  + λ_procedural × procedural_event_score(faction, this_season)
  + λ_expectation × cascade_fidelity(faction)
  - λ_violation × violation_event_score(faction, this_season)
```
with explicit starting values `λ_continuity=0.05, λ_procedural=0.3, λ_expectation=0.1, λ_violation=0.6` [`faction_behavior_v30.md:290-297`], plus §3.5.1/§3.5.2 fully enumerating the discrete procedural/violation event triggers that feed the score terms [`:299-316`]. The four λ integrators named in `faction_canon_v30.md:157` are **not** unquantified — they're quantified with named starting values ("calibrate at Stage 10" is a tuning note, not an absence). Caveat: the whole section carries a `[SUPERSEDED-BY LPS-1]` banner reclassifying L as per-settlement rather than faction-scalar [`:285`], but the formula itself (now applied per-territory) is intact and quantified, not missing.

## 2. Treasury attribution value

**Read:** `designs/scene/derived_stats_v30.md` §8 "Faction Scale" / §8.1 "Income and Drain" (lines 293–325); cross-checked `designs/territory/settlement_layer_v30.md` lines 43-51 and 159-169.

**Verdict: true canon value is ×10, not ×50.** `derived_stats_v30.md` §8.1 states explicitly: "**Treasury (from Wealth):** Seasonal income: Σ(Prosperity of controlled settlements) × **10** gold/season" [`derived_stats_v30.md:308`]. `settlement_layer_v30.md:169` correctly cites this ("faction Treasury income = Σ settlement Prosperity × 10, derived_stats §8.1"). **`settlement_layer_v30.md:47` is the wrong line** — it mislabels a different derived value: `derived_stats_v30.md:378` defines "Prosperity → Local Economy → Prosperity × 50" as a separate settlement-display metric, and `settlement_layer_v30.md:47` conflates that ×50 "Local Economy" figure with "Gold income contribution to faction Treasury," which is actually the ×10 figure. Note: `derived_stats_v1` (the name cited in `settlement_layer_v30.md:43,499`) does not exist as a file — only `derived_stats_v30.md` is on disk — a stale citation, separate from the ×10/×50 issue.

## 3. C-FA structural characterization (faction_politics_v30.md Parts 3–9)

**Read:** `designs/provincial/faction_politics_v30.md` in full from Part 3 (line 574) through Part 9 (ending ~1010), plus header/status and `module_contracts.yaml:707-720`.

**Verdict: CONFIRMED, not thin.** The doc is CANONICAL (PP-660, approved 2026-04-17), 1,115 lines. Parts 3–9 contain substantial, concrete mechanical content, not stubs:
- **Part 3 (Caste Integration, §3.1–3.6):** full caste×rank advancement table per faction/ladder [`:589-603`], caste-as-Renown-modifier, caste-as-Initiation-Duty-modifier tables, per-NPC Disposition floors [`:630-655`], and a fully numeric caste-transgressive-Conviction mechanic (ED-777, §3.6.1/3.6.2) with concrete Ob/duration/Doubt-Marker effects.
- **Part 4 (Terminology, §4.1–4.4):** the Solmund-naming fix, CV/PT/SW dissolution decision (rename deferred, ED-644), T15 naming, Varfell/Valoria-Peninsula naming — each with editorial IDs.
- **Part 5 (CI×Rank, §5.1–5.4):** full CI-banded effect tables per Church rank and per non-Church faction rank intersection.
- **Part 6 (Baralta Crown Claim, §6.1–6.4):** three full outcome branches (A/B/C) with rank-ladder cascades per faction, plus a new mechanic (Hafenmark-to-Crown Recognition Ceremony, ED-647).
- **Part 7 (Ministry expansion, §7.1–7.4):** Crown Ministries + new Hafenmark Parliamentary Committees, Church Dicasteries, Varfell Jarl Councils, each with jurisdiction/chair/cost tables.
- **Part 8 (Generational Shift Fix):** Torben maturation trigger logic + 5-tier disposition-outcome table + Readiness Track.
- **Part 9 (Cross-Faction Rank Parity):** parity table + audit.
- Plus Part 10 (editorial resolutions) and Part 11 (propagation map).

**Note on the doc:null-flip assessment:** the structural characterization is correct, but flipping `module_contracts.yaml`'s `faction_politics` `doc: null` [`module_contracts.yaml:707-720`] to this file would only resolve "where's the source doc" — it would **not** resolve the underlying registry gap. I searched the full doc body for any of the Key types the module entry tracks (`state.succession`, `state.coup_attempted`, `state.standing_change`, `scene.investigation_resolved`) and found **zero occurrences** — the word "Key" itself never appears. `faction_politics_v30.md` is pure rank-ladder/caste/political mechanics prose; it never specifies Key-emission triggers or payloads. So the doc:null flip is directionally justified (a real, rich home doc exists) but incomplete on its own — the "[ASSUMPTION]-grade resolver" and "boundary vs faction_state unestablished" gap-notes in `module_contracts.yaml:719` would persist even post-flip.

## 4. Citation-count reconciliation (faction_politics_expanded_v1.md, dead path)

Ran all three counting methods against the current working tree (repo root, excluding `.git`):

| Method | Command | Result |
|---|---|---|
| Files | `grep -rl` | **33 files** |
| Occurrences | `grep -ro \| wc -l` | **104** |
| Matching lines (summed) | `grep -rc` summed | **99** |

Restricted to `designs/`+`references/`+`canon/` (excluding archives/tests/deprecated): 21 files / 73 occurrences / 71 matching lines. Restricted to `designs/` alone: 18 / 47 / 45.

**Verdict: none of the three methods reproduce exactly 57**, nor do they exactly reproduce C-FA's own "36 files/101 occurrences." My full-repo occurrence count (104) is close to C-FA's 101 but not identical; my file count (33) is below C-FA's 36. The C-FA dossier itself already flags this as unreconciled ("Not reconciled to the exact 57" — `cluster_C-FA.md:125`). Root cause of the drift: the corpus is a **moving target across audit sessions** — e.g. `designs/audit/2026-07-07-unaddressed-areas-audit/01_workings/cluster_C-FA.md` itself now contains 2 citations of the dead path (it discusses the bug), meaning each successive audit's own artifact inflates the next resweep's count. This is self-referential contamination, not a counting-method distinction — no single method (files/occurrences/matching-lines) lands on 57 today. All three independent counts (ep-14's 57, C-FA's 36/101, mine 33/104/99) agree only in confirming the same underlying stalled-rename defect (`restructure_ledger.md:165` PENDING) at a consistent order of magnitude (20–40 files, 70–140 occurrences).

## 5. C-FA-5 massbattle-middle defender-advantage check

**Read:** `sim/provincial/massbattle.py` lines 1026–1788 in full (Manoeuvre/Engagement resolution end, Volley phase, `run_battle`, `run_multi_turn_battle`, pursuit mechanics, `run_multi_unit_battle` with morale cascade/freed-attacker/rout-contagion).

**Verdict: no fort/terrain/home-territory defender advantages or defender morale floors found in this range — absence confirmed.** The only "defender" concept present is the **per-tick tactical octagon facing mechanic** (`_rotate_defender_facing`, `octagon_angle`, lines ~446-557, 885-897) — this labels whichever atom is currently being attacked as "defender" for GREEN/YELLOW/RED flanking-angle purposes, symmetric to both sides regardless of which faction is territorially attacking/defending. One comment block (`:675-701`) invokes historical precedent (Crécy/Agincourt, Leuctra) to justify a **speed-based cell-contention tiebreak** ("higher-speed cell wins"), not a fort/terrain/territorial-ownership bonus. No garrison, fortification, siege-defender, or home-morale-floor logic executes anywhere in lines 1026–1788. (Outside this assigned range, line 35's module-level docstring references a `terrain` parameter on `resolve_mass_battle(faction_a, faction_b, terrain, world)`, but that function and any terrain-effect logic live before line 1026, outside the requested read window.) This supports C-FA-5's undamped-conquest-snowball claim for this stretch of code.

## 6. ED-1006 exact scope/status

**Read:** `canon/editorial_ledger.jsonl` line 392, ED-1006 entry in full.

**Verdict:** ED-1006 — **status: "open"** (unresolved), `date_found: 2026-06-10`, severity `mechanical`. Scope: Stage-1 module-contract extraction (module_contracts v2, 27 modules: 25 extracted/2 stubs), bundling two Jordan-veto decisions (political_dynamics consolidation into npc_behavior; campaign_architecture reclassification) plus a set of "Headline adjudication findings (all OPEN, none normalized)," one of which is exactly the tracked collision: **"3-way piety/conviction_track name collision (substrate SS8.4 vs designs/personal/conviction_track_v1 vs designs/scene/conviction_track_v30)"** [`editorial_ledger.jsonl:392`]. Decision field: "Pending Jordan: veto/ratify the consolidation + reclassification; adjudicate the A6 top-down transition gap...; name-collision resolution; registry SS10 extensions..." — i.e. the collision is one line item within a larger open, multi-part adjudication, not resolved on its own. Cross-check: ED-912 (resolved 2026-06-28) closed a *different* 3-way split (fieldwork Disposition/Knot/Ob canonical-line contradiction) — not this piety/conviction naming collision. A related but distinct fork, ED-SC-0003 (open, `needs_jordan: true`, filed 2026-07-05), separately tracks a "Piety Track" naming collision (Persuasion Track / debate-tracker Piety Track / BG per-territory Piety Track) — overlapping subject matter but citing different docs (`social_contest_v30`, `glossary.md:84`, `params/bg/core.md:117`) than ED-1006's substrate SS8.4/conviction_track_v1/v30 triad. ED-1006 itself remains open and unresolved.

## 7. C-STUB churn-amendments check

**Read:** `designs/audit/2026-07-05-emergent-narrative-engine/spec/churn_amendments.md` in full (93 lines, RATIFIED 2026-07-05, ED-IN-0011).

**Verdict: nothing there changes C-STUB-2's claim.** The file is entirely v2-delta content for the narrative-engine's five normative chapters (s1_q1_q2 casting/render, s2_q3_arcs taxonomy/detector, s3_q4_render surfaces/bake, s4_substrate conformance rules, s5_season_trace fixtures) — it never mentions "stub," "NotImplementedError," or "Layer-B" anywhere in its text. It is silent on the sim-stub-to-milestone mapping entirely. C-STUB-2's finding — "'~19 sim stubs on Layer-B paths' over-claims: only 11 of 19 are plausibly Layer-B paths; the other 8 are personal/scene/world-track content stubs" [`designs/audit/2026-07-07-unaddressed-areas-audit/01_workings/cluster_C-STUB.md:95`] — stands unchallenged and unaddressed by this source.
