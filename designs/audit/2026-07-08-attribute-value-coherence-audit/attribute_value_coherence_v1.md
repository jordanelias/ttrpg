# Attribute / Value Coherence Audit — corpus report

## Status: READ-ONLY AUDIT (2026-07-08) · Lane: IN · Anchor: ED-IN-0029 (findings tracked in the ledger; not a ratifiable design doc). [reclassified 2026-07-15, proposal-reconciliation pass — was mis-tagged as a pending proposal]

Quantity-layer extension of the Key & Echo Armature (`designs/architecture/key_echo_armature_v1.md`,
RATIFIED ED-IN-0018). The armature unified the seam layer; this audit covers the quantities those
seams read and write. Nothing here is ratified: the docket (`ed_options.md`) and the extension
(`proposed_quantity_armature_extension.md`) are **held back from merge-ratification per ED-1094**.

---

## 1. Headline stats

- **88 quantities censused** across 6 clusters (C1 attributes/aggregates 14 · C2 derived values 22 ·
  C3 pools 8 · C4 tracks/clocks 14 · C5 faction/settlement stats 12+Mandate · C6 code constants 18),
  plus C7 (cross-index enforcement, no census rows of its own).
- Census statuses: **46 COHERENT · 21 DRIFTED · 10 UNREGISTERED-LOAD-BEARING · 5 ORPHANED ·
  4 AMBIGUOUS · 2 DEAD**. Spot-check 9/10 pass (1 line-citation failure, corrected in C6-F7).
- **75 findings filed** by the 7 dossiers → critic funnel (**54 uphold · 17 soften · 3 sharpen ·
  1 overturn**) + **8 critic-sourced additions** (after dedupe) = **82 confirmed findings:
  18 P1 · 39 P2 · 25 P3** (58 NEW · 18 KNOWN-TRACKED · 6 KNOWN-UNTRACKED).
- **Six census verdicts corrected on verification**: Agility is not ORPHANED (C1-F8), Renown is not
  ORPHANED (C4-F5), Concentration is not AMBIGUOUS (C2-F9 — the `params/core.md:162` "third formula"
  citation is the Thread Fatigue row), STAMINA_REF is not DEAD (C6-F4 — live at
  `designs/scene/combat_engine_v1/wrapper.py:361`, merely unported), the census CI row's
  `params/factions_personal.md` "Clock Starting Values" citation is fabricated (C4-F4), and the
  settlement-weight inputs are prose-defined, not AMBIGUOUS (C5-F11).
- **A17 (stat-vocabulary closure) backlog: ~34/88 quantities (39%)**; **A18 (formula single-source)
  backlog: ~25–27/88 (28–31%)** — seeded baselines, see §5.
- Diagnosis in one line: **individual quantities are mostly well-formed; the debt is in the
  carriers** — stale prose satellites, warn-tier-only naming enforcement, an unvalidated
  `stat_deltas` transport, and a registry whose `not_descriptors` catch-all covers barely half of
  what is actually load-bearing.

---

## 2. The coherence picture, per cluster

### C1 — Personal attributes, aliases & aggregates: **the roster itself is undecidable today**

Verdict: **INCOHERENT at the roster level; COHERENT per-attribute below it.** Four mutually
incompatible rosters coexist: glossary's 7 (`references/glossary.md:33-41`, missing Focus and
Bonds), the registry's folded 9 (`references/descriptor_registry.yaml:30-44`), and two independent
un-folded 10-tables carrying **Recall** (`params/core.md:140-145`;
`designs/architecture/canonical_registry.md:138-140`) that CURRENT.md never indexes (C1-F1, P1,
KNOWN-UNTRACKED — ED-IN-0008 names only 2 of the 4). Recall is fully load-bearing (History cap
`params/core.md:151`, Appraise pool `params/contest.md:23,141`, Southernmost pools
`params/southernmost.md:15,95`) with zero registry presence (C1-F2, P2). Both contested registry
folds are inverted in practice: ED-899's live Command formula ratifies **Cognition** with named
engine constants (`params/mass_combat.md:139,361,369`; `tests/sim/mass_battle/config.py:155-159` —
C1-F3, P1, KNOWN-TRACKED ED-IN-0008), and **zero** live formula uses "Will" — every consumer uses
Spirit (`references/module_contracts.yaml:827-828`; `designs/scene/combat_engine_v1/config.py:61` —
C1-F4, P1). Critic-sourced: the fold-target **Acuity** has zero consumers anywhere *and* the bare
word is already spent on an explicitly rejected Fieldwork resource
(`designs/architecture/integration_proposal_v30.md:200-204` — C1-M1, P3). Glossary's formula
content is two supersessions stale for both Health (`references/glossary.md:47` vs
`designs/scene/derived_stats_v30.md:59-68`, ED-1021 — C1-F5, P1) and Stamina
(`references/glossary.md:48` vs `derived_stats_v30.md:98` — C1-F6, P1). All of it is CI-invisible:
every attr/agg/fac/set key is `enforce: warn` and glossary sits outside the names_index mirror
(`references/names_index.yaml:44-73` — C1-F10, P2). Census correction: **Agility is not orphaned**
— live tempo/initiative/maneuver consumer (`combat_engine_v1/config.py:64`;
`designs/scene/combat_design_v1.md:102-108` — C1-F8).

### C2 — Derived values: **byte-coherent at the newest seam, rotting with distance from it**

Verdict: **COHERENT at the design↔contract↔sim triangle for personal combat; STALE in the params/
and glossary satellites.** Health and Stamina match exactly across
`designs/scene/derived_stats_v30.md` §4, `references/module_contracts.yaml:819-829`, and
`combat_engine_v1/combatant.py:35-47`. But `params/core.md:158`'s Health row is the ED-826 fix now
itself superseded by ED-1021 (C2-F2, softened to P2 — the cell's own Notes column routes to the
authoritative doc), and the Mandate prose in `params/factions_personal.md` + `params/bg/*` is a full
ruling-generation behind LPS-2e (C2-F1, softened to P2 — `CURRENT.md:39` routes correctly; no
engine path reads these files). The cluster's one confirmed P1 (sharpened): **combat_v30.md §7
self-contradicts a same-day ruling** — line 298 states ED-PC-0005's fractional-Ob reversal, line 307
still asserts the superseded PP-716 −1D, and ED-PC-0005's own ledger entry
(`canon/editorial_ledger.jsonl:377`) **falsely claims §7 was rewritten** (C2-F3). Critic-sourced:
`designs/provincial/mass_battle_v30.md:313-314` carries a **third**, pre-PP-716 wound-penalty
formulation never swept — ED-PC-0005's scope list omits the design-doc layer entirely (C2-M1, P2).
Also: Concentration absent from params/core.md's master table (C2-F5), Face has no registry key
(C2-F6), and the settlement derived values are gated live by contracts while their own home doc
disclaims them as "Not canonicalized" (C2-F4).

### C3 — Pools: **Combat Pool is the best-documented case, not the worst**

Verdict: **DRIFTED — the worst single formula collision in the audit is here.** **Knot Pool has
four live, mutually contradicting formation formulas**: `designs/personal/knots_v30.md:37` table
(Bonds×2)+3 vs its own §3.2 procedure Spirit×2+History(Rel) at :76, vs
`designs/scene/fieldwork_v30.md:473` bare Spirit×2, vs the running oracle
`sim/personal/knots.py:213-215` (spirit×2+history_rel) — and ED-912 never touched the pool formula
(C3-F1, P1). The oracle's formula has zero regression coverage (`sim/tests/test_knots_ed912.py`, no
pool assertion — C3-F2, P2). The word "pool" itself names two disjoint kinds across
`descriptor_registry.yaml:106-112` (dice-size) and `module_contracts.yaml`'s `bucket: pool`
(resource meter), which also disagree on Stamina's kind (C3-F3, P2). Combat Pool's triple-carriage
is confirmed per baseline plus one intra-doc addition: `derived_stats_v30.md:515` (§13 "What Does
NOT Change") states the struck (Agi×2)+History+3 form as current while :584 says it was struck
(C3-F10, P2, KNOWN-TRACKED ED-1084/F-REG-001). threadwork_v30.md carries the struck
Attunement+Focus Mending pool as current at :968 and :1008 (C3-F7, P2). "Faction Political Pool"
is an 8th uncatalogued pool-named quantity — and prior art the dossier missed already names it
"Political Pool" (`references/mechanical_terms_index.md:192`; `references/collision_registry.yaml`
— C3-F4 softened to KNOWN-UNTRACKED; C3-M1, P2, critic-sourced). Positive control:
`params/fieldwork.md:9-12` propagated ED-1084 correctly.

### C4 — Tracks & clocks: **a self-declared canonical registry nobody indexes, and BG surfaces gating on struck stats**

Verdict: **DRIFTED, with the corpus's worst name collision.** `designs/provincial/clock_registry_v30.md`
declares itself the "single source of truth for all clocks/tracks/counters", is cited by four
module_contracts modules (`references/module_contracts.yaml:255,517,644,663`), yet is absent from
CURRENT.md (C4-F1, softened to P2) **and is itself stale** — its Torben Loyalty row still carries
PP-498's superseded start=3 vs PP-599's 7 (`params/bg/core.md:82` — C4-F2, P1, KNOWN-UNTRACKED via
`handoffs/HANDOFF_IN.md:177`). CI's starting value has **four non-agreeing assertions** (BG=28
triangulated; `params/campaign_modes.md:46` TTRPG=15 citing a nonexistent file; factions_personal.md
silent; clock_registry unqualified 28 — C4-F3, P1). `params/campaign_modes.md:42-47` also mislabels
the BG MS start (72) as TTRPG (canonical TTRPG=60, `params/core.md:101` — C4-F10, P1). **Standing**
is sharpened to P1: beyond the personal(0-10)/BG-faction homonym, glossary (`references/glossary.md:110`,
0-10) and clock_registry (:48-53, 0-5) disagree on the range of the *same* BG faction track (C4-F9 +
absorbed C4-M1). VTM is STRUCK (PP-663) yet still numerically gates victory and Southernmost access
(`params/bg/victory.md:13-15,52-53`; `params/bg/geography.md:270-403` — C4-F12, P2). TC (Theocracy
Counter) survives as a second live clock beside its renamed successor CI
(`module_contracts.yaml:256`; un-renamed co-file `conviction_track_v30_infill.md:7,23-26` — C4-F6,
P2). Critic-sourced: **Coup Counter** (censured, ED-781) has untracked residuals beyond
`censured_vocabulary.yaml`'s stale count of 6 (C4-M2, P2). Census corrections: Renown is defined
(`derived_stats_v30.md:409-420`; closure trail `references/orphan_terms_registry.yaml:59-61`) — the
real open item is its cap (C4-F5, P1); the Bonds attr-vs-gate situation is a crosswalk gap, not a
collision — a prose cross-map exists at `designs/personal/knots_v30.md:17,28` (C4-F7, softened P2).

### C5 — Faction & settlement stats + Mandate: **raw stats registered, derived layer ungoverned**

Verdict: **COHERENT at the raw-stat layer; BROKEN canonicity in the derived layer.** Two P1s:
(1) **Mandate's linear form cites a source that no longer says it** — `params/factions_personal.md:14`
cites faction_behavior_v30 §4 for round(0.5L+0.5PS), but that section now carries the LPS-2e
saturating aggregate matching `module_contracts.yaml:598-601` and `faction_canon_v30.md:213-216`
(C5-F1; note C7 critic context: ED-784 blessed a *deliberate* simplified personal view — the docket
item is to mark it as such, not to adjudicate a fork). (2) **Local Economy / Garrison Strength /
Public Order have circular, broken canonicity**: `settlement_layer_v30.md:43` cites the nonexistent
"derived_stats_v1 §4"; the real home (`derived_stats_v30.md` §9) disclaims the identical formulas as
"Not canonicalized"; `module_contracts.yaml:556-597` gates on them live (g_dv0) (C5-F2). The
registry's blanket faction-stat "1-7" scale loses per-stat floors (`params/bg/core.md:200-207`:
Wealth/Military/Stability floor 0, Influence 1, Intel omitted — C5-F3, softened to P2
enforcement-gap). **Discipline** is a live name collision (per-unit mass-battle stat
`mass_battle_v30.md:169` vs faction meter Stability×10 `derived_stats_v30.md:298,545` — C5-F4, P2).
The registry's `not_descriptors.derived_values` lists only 9 of §14.1's 16 rows (C5-F5, P2). Fort
Level is a province-tier stat consumed per-settlement with no inheritance rule (C5-F6, P2). The
tracked "Public Support" residual citation (`name_collision_database.yaml:469`) is stale — the real
untracked residual is `mechanical_terms_index.md:196,1167` (C5-F7, P2). Critic-sourced:
`params/factions_personal.md:23-27` still shows Intel='—' for 5 factions despite ED-787 values
existing (C5-M2, P2).

### C6 — Code constants & the export pipeline: **one green round-trip, one already-drifted port**

Verdict: **COHERENT inside `config.CFG`'s CI-blocked export; DRIFTED outside its fence.** The
sigma families (PER_DIE/LEVEL_SIGMA/M_MAX/SIGMA_N_COEFF) verify byte-identical across three
surfaces. The sharpest confirmed P1 is critic-sourced: **combat_config.gd's RESIST dictionary has
already drifted in 4 of 12 cells** from `core.py:77-89`'s 2026-06-30 grounding edit (cloth
.10/.35/.15 vs oracle .12/.45/.12; mail.shear .80 vs .85) — a live wrong-value ingestion for any
Godot consumer today, KNOWN-TRACKED as the ED-1050 residual but nowhere stated as *stale values*
rather than "not yet ported" (C6-M1). The exporter covers only `config.CFG`; ~15 co-equal core.py
constants reach the port by hand (C6-F2, P2, corrected: not "byte-identical" — RESIST already
diverged). 7/181 CFG keys are dead-but-exported (the DAMAGE_SCALE failure shape — C6-F3, P2).
GAP_EXPOSURE/GAP_PREC_REF are simply never carried (C6-M2, P3). `stat_deltas` accepts any string
(`sim/substrate/keys.py:83-84,300-356` — C6-F1, P2). **Overturned:** the workbench
m1_dice_sigma_core imports are an explicit, in-line-documented ED-1085 dev-tooling exception, not a
contradiction (C6-F5 dropped).

### C7 — Cross-index consistency & enforcement: **2 of 28 pairwise relationships checked; the rest is trust**

Verdict: **the enforcement layer cannot catch any of the above.** Only `ci_names_consistency.py`'s
two mirror pairs are automated (`tools/ci_names_consistency.py:4-15` — C7-F4, P2); the drift lint
matches only the empty `legacy:` fields, so it has zero matchers for the whole attr/fac/set family
(`tools/names.py:91-108`; `names_index.yaml:41-72` — C7-F3, P2). The secondary indices' regeneration
path is severed, not stalled (dead collator + quarantined values_master — C7-F5, P2). The CT/CV/PT
abbreviation contradiction is P1 but heavily KNOWN-TRACKED (ED-644, ED-1006, ED-1009, ED-919 —
recalibrated by the critic; `module_contracts.yaml:238-239,272` carries its own OPEN gap_note).
**Coherence** (sharpened): ED-830 *resolved* its classification as Track, yet descriptor_registry
never received it and module_contracts tags it `bucket: pool` — a 3-way bucket disagreement hung off
a resolved ruling that never propagated (C7-F2, P1). `keys.py` validates field presence, never stat
names (C7-F6, P1). Mandate's linear/saturating split recalibrates to KNOWN-TRACKED/stale/P3 at this
layer (ED-784's deliberate dual view — C7-F8). Critic-sourced: **seven more naming registries in
`references/` have zero live tool consumers** (censured_vocabulary, collision_registry,
orphan_terms_registry, proper_noun_triage×2, alias_registry, proper_noun_candidates — C7-M1, P2).

---

## 3. Registers

### 3.1 Collision register (same name, different formula/definition) — 11 confirmed

| # | Quantity | The collision | Sev | Calib | Evidence |
|---|---|---|---|---|---|
| C1-F1 | Attribute roster | 7 vs 9 vs 10 vs 10 rosters | P1 | KU (ED-IN-0008 covers 2/4) | descriptor_registry.yaml:30-44; glossary.md:33-41; params/core.md:140-145; canonical_registry.md:138-140 |
| C1-F3 | Cognition/Acuity | ED-899 ratifies Cognition live vs registry fold | P1 | KT ED-IN-0008 | params/mass_combat.md:139,361,369; descriptor_registry.yaml:39 |
| C1-F7 | Focus | attribute (1-7) vs derived contact-duration stat (1-5+), cross-surface; plus unmarked pre-ED-694 rule beside its replacement | P2 | NEW | descriptor_registry.yaml:38; glossary.md:52; params/core.md:152,162 |
| C1-M1 | Acuity | zero consumers + name spent on rejected Fieldwork resource | P3 | NEW (critic) | integration_proposal_v30.md:200-204; comprehensive_system_audit_2026-04-15.md:469-528 |
| C3-F1 | Knot Pool | four live formation formulas | P1 | NEW | knots_v30.md:37 vs :76; fieldwork_v30.md:473; sim/personal/knots.py:213-215 |
| C3-F10 | Combat Pool | triple-carriage + intra-doc §13-vs-§14.4 contradiction | P2 | KT ED-1084 | derived_stats_v30.md:515 vs :584; params/core.md:4,161; values_master.yaml:212,1150 |
| C4-F3 | Church Influence start | 28 / 15 / silent / unqualified 28 | P1 | NEW | params/bg/core.md:82; campaign_modes.md:46; clock_registry_v30.md:17 |
| C4-F8 | IP full name | Invasion vs Institutional Pressure | P2 | KT FIX-03 | params/bg/core.md:83; campaign_modes.md:47; mass_combat.md:381-382 |
| C4-F9 | Standing | 0-10 vs 0-5 on the *same* BG faction track + cross-scale homonym | P1 (sharpened) | NEW | glossary.md:100,110 vs clock_registry_v30.md:48-53; params/contest.md:144 |
| C5-F4 | Discipline | per-unit MB stat vs faction Stability×10 meter | P2 | NEW | mass_battle_v30.md:169; derived_stats_v30.md:298,545 |
| C7-F1 | CT/CV/PT | collision-DB rules PT; glossary prescribes CT; contracts use CV; names_index has none | P1 | KT ED-644/1006/1009/919 | name_collision_database.yaml:465-467; glossary.md:94; module_contracts.yaml:254,238-239 |

### 3.2 Synonym register (different names, one concept) — 3 confirmed (+ MS/RS and Turmoil/Strain carried in 3.3)

| # | Names | Sev | Calib | Evidence |
|---|---|---|---|---|
| C1-F11 (=C5-M1) | "Influence": Charisma alias vs fac.influence, intra-registry, no disambiguation | P2 | NEW | descriptor_registry.yaml:43 vs :65 |
| C3-F8 | Argue Pool boundary: style dice in-pool vs added-at-Step-3 | P3 | NEW → feeds ED-SC-0004 | social_contest_v30.md:85-88,490 vs derived_stats_v30.md:585 |
| C3-M1 | "Political Pool" prior art vs dossier's fresh "Parliamentary Vote Tally" — two uncoordinated proposals | P2 | KU (critic) | mechanical_terms_index.md:192; collision_registry.yaml:6-9 |

### 3.3 Stale register (superseded value/name still carried live) — 21 confirmed; the P1/P2 core:

| # | Carrier | Stale content | Sev | Calib |
|---|---|---|---|---|
| C1-F5 | glossary.md:47 (+params/core.md:158) | Health = Endurance / pre-ED-1021 form | P1 | NEW |
| C1-F6 | glossary.md:48 | Stamina two supersessions behind | P1 | NEW |
| C2-F3 | combat_v30.md:307 (vs :298) | PP-716 −1D beside its same-day ED-PC-0005 reversal; ledger falsely claims §7 rewritten (editorial_ledger.jsonl:377) | P1 (sharpened) | NEW |
| C2-M1 | mass_battle_v30.md:313-314 | third, pre-lineage wound-penalty carrier, outside ED-PC-0005's sweep list | P2 | NEW (critic) |
| C2-F1 | params/factions_personal.md:8,14 + params/bg/* | flat PP-686 v2 Mandate | P2 (softened) | NEW |
| C2-F2 | params/core.md:158 | ED-826-era Health (self-routing note present) | P2 (softened) | NEW |
| C4-F2 | clock_registry_v30.md (Torben row) | PP-498 start=3 vs PP-599 start=7 | P1 | KU (HANDOFF_IN.md:177) |
| C4-F10 | campaign_modes.md:42-47 | BG MS=72 mislabeled TTRPG; 3 nonexistent citations | P1 | NEW |
| C4-F6 | module_contracts.yaml:256 + conviction_track_v30_infill.md:7 | TC (Theocracy Counter) live beside renamed CI; ED-782 miscited | P2 | NEW |
| C4-F11 | params/bg/victory.md:14,53,89,130 | WA gates never updated to WR (geography.md:408-431) | P2 | KT ED-311 |
| C4-F12 | victory.md/geography.md | STRUCK VTM still gating thresholds | P2 | KT PP-663 (non-propagation) |
| C4-M2 | arc_register_events.md, numeric_bounds_report.yaml, throughlines_complete.md | Coup Counter residuals beyond stale censured count | P2 | KT ED-781 (critic) |
| C5-F7 | mechanical_terms_index.md:196,1167 | "Public Support" as canonical (tracked residual citation itself stale) | P2 | NEW |
| C5-M2 | params/factions_personal.md:23-27 | Intel '—' for 5 factions vs ED-787 values | P2 | NEW (critic) |
| C3-F5/F7 | derived_stats_v30.md:589; threadwork_v30.md:968,1008 | uncaveated PP-233 MC-pool row; struck Att+Focus Mending pool | P2 | KU/NEW |
| MS/RS (census C4 row) | params/threadwork.md:139-142; values_master.yaml:190; mechanics_index.yaml:778 | pre-ED-731 "RS" undefined in live files | P2 | KU (F-PARAMS-01) |

(P3 stale rows — C5-F10 Löwenritter Wealth, C5-F12 L/PS seed columns, C5-F13/ED-869 footnote,
C2-F7 broken section citation, C7-F8 Mandate dual-view marking — in the dossiers.)

### 3.4 Export-drift register (prose vs oracle vs port) — 3 confirmed

| # | Surface pair | Drift | Sev | Calib |
|---|---|---|---|---|
| C6-M1 | core.py:77-89 vs combat_config.gd:34-38 | **RESIST already drifted 4/12 cells** (cloth .12/.45/.12 vs .10/.35/.15; mail.shear .85 vs .80) | **P1** | KT ED-1050 residual (critic) |
| C5-F1 | params/factions_personal.md:14 vs faction_behavior_v30.md §4 | linear Mandate citing a rewritten source | P1 | NEW (ED-784 context: mark as deliberate view) |
| C5-F2 | settlement_layer_v30.md:43 vs derived_stats_v30.md §9 vs module_contracts.yaml:556-597 | circular canonicity; contracts gate on "Not canonicalized" formulas | P1 | NEW |

### 3.5 Enforcement-gap / unregistered core (P1–P2)

- **C7-F6 (P1)** `sim/substrate/keys.py:239-251` — stat_deltas/impact_vector keys never checked
  against any registry (impact_vector *is* axis-checked at :321-327; stat_deltas is not — C6-F1).
- **C7-F2 (P1)** Coherence: ED-830 ruled Track; registry absent; contracts say pool.
- **C7-F3/F4 (P2)** drift lint has zero matchers for the attr/fac/set family; only 2/28 pairwise
  index relationships automated.
- **C1-F10 (P2)** warn-tier everything + dead `tests/registry/test_descriptor_registry.py` (no
  test_* collected) + glossary outside the mirror.
- **C5-F5 (P2)** registry derived_values list covers 9/16 of §14.1.
- Unregistered-load-bearing: Recall (C1-F2), TS/TPS (F-REG-006/007), Fort Level (F-C-007), WI/MW
  (F-C-009), FacilityTier/base(Type)/W_s (F-C-005), Persuasion Track linkage (F-REG-009),
  cumulative_drift (F-C-004), Knot Pool key (F-REG-013), Face (C2-F6).
- **C7-M1 (P2, critic)** seven more `references/` naming registries with zero live tool consumers.

---

## 4. Census corrections (audit-integrity register)

| Census claim | Correction | Finding |
|---|---|---|
| Agility ORPHANED | Live tempo/initiative/maneuver consumer; struck from one formula only | C1-F8 |
| Resonant Style defined by conviction_track_v1.md | That doc is SUPERSEDED (PP-717); canonical 4-value taxonomy is npc_behavior_v30 §1.3; ED-IN-0025 already corrects the premise inline | C1-F9 (KT) |
| Concentration AMBIGUOUS (3rd formula at params/core.md:162) | Line 162 is Thread Fatigue; no Concentration row exists; formula-coherent everywhere it appears | C2-F9 |
| Renown ORPHANED, "defined nowhere" | Defined at derived_stats_v30.md:409-420; sweep-closed; open item is the cap | C4-F5 |
| CI TTRPG start=0 per factions_personal "Clock Starting Values" | No such table/value exists in that file | C4-F4 |
| Settlement-weight inputs AMBIGUOUS | Prose-defined at settlement_layer_v30.md §1.8; real gap is contract-layer under-registration | C5-F11 |
| STAMINA_REF DEAD | Live at wrapper.py:361; unported to .gd (build-state, not deadness) | C6-F4 |
| Contest Track Start at modes.py:5-6; Readiness at primitives.py:18-31 | Real defs at modes.py:450-451; primitives constants scattered :50-255 | C6-F7 |
| Knot Pool single-formula | Census never followed mechanics_index:343's pointer into the 4-way split | C3-F9 |

---

## 5. The A17 / A18 measured backlogs (C7)

- **A17 — stat-vocabulary closure** (every quantity named in a Key payload, contract state/derivation,
  params table, or engine constant resolves to a registry key): fails for **~34/88 (39%)** censused
  quantities; hand-trace of `module_contracts.yaml` state/derivation declarations fails **~23/34
  (68%)**; the Key-substrate `stat_deltas` layer is **unsampleable today** (zero vocabulary
  validation, `sim/substrate/keys.py:239-251`).
- **A18 — formula single-source** (each formula has exactly one defining surface; all other carriers
  cite it): fails for **~25–27/88 (28–31%)**. Registration does not prevent it — Mandate is
  registered on 8/8 surfaces and still dual-formed (C7-F8).
- **Caveat (critic, cardinal rule a):** these percentages are cluster-prose seeds without per-item
  file:line backing; treat them as sizing baselines. The checks themselves (extension §3) must
  re-derive the backlog mechanically before any flip-to-blocking. A18's input tooling — the
  **prose-formula drift detector** — does not exist (CLAUDE.md §5: no tool parses `params/*.md`).

---

## 6. What this feeds (KNOWN-TRACKED open items — what the audit adds)

| Open item | What this audit adds to its decision surface |
|---|---|
| **workplan v6 T1 queue-13** (roster ratification) + **ED-IN-0008** | The full 4-roster evidence set (C1-F1), the Recall gap (C1-F2), live-usage inversions for both folds (C1-F3/F4/M1), and a coherent decision surface: OPT-AV-1. The 7-vs-9 framing understates the problem. |
| **values_master retire-vs-regenerate** (2026-07-01 queue 17) | Retire-leaning evidence: struck Combat Pool ×2, old Stamina, RS-era labels; generator dead; regeneration would re-couple to quarantined data (C7-F5). OPT-AV-2. |
| **ED-1050** (port↔oracle) | The residual is not "unported" but **stale-valued**: RESIST 4/12 cells drifted (C6-M1). OPT-AV-15. |
| **ED-1051** (contracts doc:null) | Adjacent new class: contract formulas referencing undeclared inputs (Health's Endurance/Spirit/Strength, F-C-003; WI/MW comment-only, F-C-009; mass_battle `state: []`, C3-F6). |
| **ED-1052** (typed engine-params scope) | Concrete next slice: widen exporter to core.py constants (C6-F2/U2); prune 7 dead CFG keys (C6-F3); A18 detector spec (extension §3). |
| **ED-PC-0003** (sigma band-discipline) | Degree-threshold split (F-SIM-05) catalogued; no new ruling needed here. |
| **ED-PC-0005/0006** (wound fractional-Ob) | Two unswept carriers: combat_v30.md:307 and mass_battle_v30.md:313-314; ledger resolution text partially false (C2-F3/M1). Feeds PC + MB. |
| **ED-FA-0003 / ED-FA-0004** | The params/-prose half of the Mandate/L/PS rewiring the sim ED doesn't cover (C2-F1/C5-F1); Intel '—' backfill (C5-M2). Feeds FA. |
| **ED-SC-0004 / ED-SC-0008** | Argue-pool boundary evidence (C3-F8); Face registry key (C2-F6); Standing personal-scale half (C4-F9). Feeds SC. |
| **ED-644 / ED-1006 / ED-1009 / ED-919** (Piety/CT) | Consolidated 4-referent map + the enforcement finding that names_index has no key at all (C7-F1). Decision surface: OPT-AV-13 — **not ruled here** (ED-644 defers pending cost-benefit). |
| **ED-920** (Knot fieldwork deviation) | The wider 4-formula collision (C3-F1) — flagged that folding it into ED-920 widens that ED's stated scope; OPT-AV-9 (feeds FI). |
| **ED-IN-0025** (Resonant Style, NEEDS-JORDAN) | Registration gap + census miscitation only (C1-F9); disposition untouched. |
| **ED-869 / ED-311 / PP-663 / ED-781 / ED-830 / ED-784 / ED-1056** | Residual-propagation instances catalogued (C5-F13, C4-F11, C4-F12, C4-M2, C7-F2, C7-F8, C2-F10) — the recurring shape: **the ruling landed, the sweep didn't**. |

---

*Full verdicts: `01_workings/dossier_C*.md` + `01_workings/critic_C*.md`. Tallies:
`finding_status.md`. Docket: `ed_options.md`. Extension: `proposed_quantity_armature_extension.md`.*
