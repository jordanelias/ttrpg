# Term Usage Sweep — Batch 2: Derived Character Stats

# Batch 2 — Derived Character Stats: Corpus-Wide Usage Sweep

Method note: all file:line citations below were read directly from the working tree at `/home/user/ttrpg` (Read/Grep/Glob), not from memory or GitHub. Archived/deprecated trees (`archives/`, `deprecated/`) were excluded from the sweep per CLAUDE.md's currency guidance, except where a deprecated file's persistence is itself the finding.

---

## 1. HEALTH

**Home definition.** Canonical source: `designs/scene/derived_stats_v30.md` §4.1, lines 55–93, explicitly labeled "AUTHORITATIVE (PP-716)" and updated by the D-A patch (ED-1021, Jordan-ratified 2026-06-18):
- Wound Interval: `WI = round(Endurance + 4 + 0.4 × Spirit)` (line 66)
- Max Wounds: `min(floor(Endurance/2)+1, 3)` (line 65)
- Health (full): `round(WI × (Max Wounds + 1) + 0.25 × Strength × Endurance)` (line 67)
- Felled at cumulative damage ≥ Health (non-resetting grand total) (line 68)
- Wound penalty: fractional Ob only, **never** −1D pool cut (Jordan ruling **2026-07-08**, ED-PC-0005 — this is dated *today*; combat channel is ED-1041 bilateral +0.15 Ob atk / +0.25 Ob def) (line 72)

**Exhaustive usage sweep** (132 files hit `\bhealth\b` outside archives/deprecated; below are every distinct file carrying a *formula-bearing* Health claim, plus representative index/registry citations):

- `params/core.md:158`
- `references/glossary.md:47, 267`
- `references/mechanical_terms_index.md:90, 1583`
- `references/values_master.yaml:222-226`
- `references/module_contracts.yaml:820, 829-831`
- `references/valoria_interdoc_audit.md:64-69` (an audit doc *about* two conflicting old Health formulas)
- `references/valoria_complete_systems_r2.md:131`
- `references/silo_cohesion_analysis.md:103`
- `references/propagation_map.md:13`, `references/propagation_map_archive_2026-05-10b.md:279` (identical propagation note)
- `designs/scene/combat_v30.md:285, 300`
- `designs/scene/combat_design_v1.md:271`
- `designs/scene/combat_engine_v1/combatant.py:20-42, 63, 119`
- `designs/scene/combat_engine_v1/REARCHITECTURE_v1.md:82`
- `skills/valoria-combat-simulator/references/combat_params.md:26, 119, 120`
- `skills/valoria-combat-simulator/scripts/combat_sim.py:115, 298`
- Roughly 20 files under `designs/audit/2026-05-28-*`, `designs/audit/2026-06-13-combat-bottomup/`, `designs/audit/2026-06-29-combat-corpus-recovery/`, `designs/audit/2026-06-11-orchestration/valoria_master_workplan_v4.md:80` and `valoria_authoritative_graph_v1.md:55` — all historical NERS/audit snapshots, consistently citing the R2/D1/D-A wound-model chain (e.g. `combat_engine_cross_reference.md:66,135,222`, `unified_damage_model_NERS_and_ratification_candidate_2026-05-31.md:51,109,125`, `damage_model_design.md:10`) — these post-date PP-717 but most (dated 2026-05-28 through 2026-06-13) *pre-date* the 2026-06-18 D-A update, so their `Health=WI×(MW+1)`, `WI=End+6` framing is a faithful snapshot of canon-at-the-time, not a live contradiction today.
- `designs/world/calamity_radiation_v30.md:116` (Gap-entity "Health pool = Spirit × 2" — a distinct, narrower rule for non-practitioner Gap entities, not in tension with the PC formula since it's a different subject)
- `designs/ui/valoria_ui_ux_v4_1_max_audit.md:299`, `valoria_ui_ux_v4_2_workplan.md:288` (unrelated "Rendering Strain capped at Health" usage — consistent, no divergence)
- Incidental English usage excluded: `designs/npcs/npc_behavior_v30.md:325,344,346` ("Public Health," "cognitive health reports" — Ministry census flavor text, not the game stat).

**Divergence check** — this term has the richest confirmed divergence set in the batch:

- **Glossary is drastically stale.** `references/glossary.md:47`: `| Health | HP* | = Endurance | Wound track. Resets per wound. *HP not standalone — write Health.* |` This is not even the pre-D-A `(End+6)×(MW+1)` formula — it's a much older, simpler one (`Health = Endurance`, resets per wound), directly contradicted by derived_stats_v30.md's own line 68: "Non-resetting grand total." The glossary header claims "Last updated: 2026-07-01," i.e., current, yet carries a formula three generations behind canon.
- **`params/core.md:158`** states: `Health | (End+6) × (MW+1), MW = min(floor(End/2)+1, 3) | 14–48 (cap MW=3)` — this is the **post-PP-717/pre-D-A** formula (flat `End+6`, no Spirit term in WI, no Strength buffer). It does append "**See `designs/scene/derived_stats_v30.md` §4.1 as authoritative.**" — but it also independently restates a literal formula, and that literal has drifted from the doc it cites as authoritative.
- **Intra-file self-contradiction inside the authoritative document itself.** `designs/scene/derived_stats_v30.md` gives the current D-A formula at §4.1 (lines 66-67) but then, in the *same file*:
  - §3 Multiplier Tiers table, line 44: "Note: Health uses non-multiplier `(End+6)×(MW+1)`" — the old formula, contradicting §4.1 twelve lines later.
  - §13 "What Does NOT Change," line 516: "Wound Interval: End + 6" — flatly contradicts §4.1's `WI = round(End+4+0.4×Spirit)`.
  This means the canonical head disagrees with itself about its own authoritative value.
- **`designs/scene/combat_v30.md:285`**: `**Health (full) = (Endurance + 6) × (Max Wounds + 1)**` — pre-D-A formula. The file carries a `[PARTIALLY SUPERSEDED 2026-06-04, Jordan / ED-900]` banner (line 1) and does point to derived_stats_v30 §4.1, but its own Status line (line 10) still reads "WORKING DESIGN — not compiled. This is the design-layer source for personal combat," creating a currency signal conflict (banner says superseded, Status line says working/live).
- **`designs/scene/combat_design_v1.md:271`**: identical old formula, **no supersession banner anywhere in the file**, no citation to derived_stats_v30 at all (cites only PP-232/ED-438) — an unflagged stale duplicate, and this file isn't even referenced in `references/canonical_sources.yaml` (only `combat_v30.md` is), suggesting it's an orphaned precursor doc nobody marked dead.
- **`skills/valoria-combat-simulator/references/combat_params.md`** (lines 26, 119): `Health = End + 6` — the oldest formula of all (pre-PP-716, no Max-Wounds multiplier whatsoever). The file's own header (line 2) calls itself "*Source of truth for all simulation runs*" with "*Last updated: 2026-03-31*" — yet the same file's Combat Pool line (line 26 area) has been hand-updated to the *current* ED-901 pool formula with a citation to "ED-1084 propagation." So the file was touched post-ED-1084 for Combat Pool but Health/Stamina were never brought forward — a partial, inconsistent update.
- **`skills/valoria-combat-simulator/scripts/combat_sim.py:115,298`**: `health = end + 6` — the stale formula is not just documented but **executed** by this skill's live simulator script.
- **`references/values_master.yaml:224-226`**: cites `section: "params_combat.md — Personal Combat > Pool Formula"` — this file is **confirmed nonexistent** (CLAUDE.md §5, and verified directly: `ls params/combat.md` → No such file or directory). `value_raw: "(Endurance + 6) × (max Wounds + 1)"` — old formula sourced from a file that doesn't exist.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/scene/derived_stats_v30.md:67` (§4.1) | CANONICAL DEFINITION | The declared authoritative spec ("§4.1 is the authoritative spec," line 20) | — (is canon) |
| `designs/scene/derived_stats_v30.md:44` (§3) | HARDCODED DUPLICATE | Independent literal `(End+6)×(MW+1)` inside the same file as §4.1 | **NO** — contradicts its own §4.1 |
| `designs/scene/derived_stats_v30.md:516` (§13) | HARDCODED DUPLICATE | Independent literal "Wound Interval: End + 6" | **NO** — contradicts its own §4.1 |
| `params/core.md:158` | HARDCODED DUPLICATE | Independent literal formula + citation link to §4.1 (citation present but doesn't exempt the restated literal) | **NO** — pre-D-A value |
| `designs/scene/combat_v30.md:285` | HARDCODED DUPLICATE | Independent literal, citation to §4.1, but file self-flags "PARTIALLY SUPERSEDED" | **NO** — pre-D-A value |
| `designs/scene/combat_design_v1.md:271` | HARDCODED DUPLICATE | Independent literal, no citation to §4.1 at all, no supersession banner | **NO** — pre-D-A value |
| `designs/scene/combat_engine_v1/combatant.py:40-42` | HARDCODED DUPLICATE | Independent Python literal (`STR_HEALTH_W=0.25`, `WOUND_INTERVAL_BASE=4`, `SPI_WI_W=0.4`), no exporter reads derived_stats_v30.md (a markdown file) into this code | **YES** — matches D-A exactly, with explicit inline citation comments |
| `references/glossary.md:47` | HARDCODED DUPLICATE | Independent literal `= Endurance` | **NO** — three generations stale |
| `references/mechanical_terms_index.md:90` | PULLED / REFERENCED | Bare citation "glossary §1", no independent number beyond copying glossary's stale text | Inherits glossary's staleness |
| `references/values_master.yaml:224-226` | HARDCODED DUPLICATE | Independent literal, cited section belongs to a nonexistent file (`params_combat.md`) | **NO** — pre-PP-717/D-A value |
| `references/module_contracts.yaml:829-831` | HARDCODED DUPLICATE (documentation-grade) | Independent textual restatement in a `derivations:` YAML field, cites "ED-1041 / derived_stats_v30 §4.1" | **YES** — matches D-A exactly |
| `skills/valoria-combat-simulator/references/combat_params.md:26,119` | HARDCODED DUPLICATE | Independent literal `End + 6`, in a doc that separately DOES cite the current Combat Pool via ED-1084 propagation (selective staleness) | **NO** — oldest formula found in the sweep |
| `skills/valoria-combat-simulator/scripts/combat_sim.py:115,298` | HARDCODED DUPLICATE | Independent Python literal `end + 6`, executed at runtime | **NO** |
| `designs/audit/2026-05-28-*` and `2026-06-13-*` snapshot docs (representative: `combat_engine_cross_reference.md:66`) | HARDCODED DUPLICATE (historical) | Independent literal, but dated **before** the 2026-06-18 D-A patch — faithful to canon-at-the-time | Was correct when written; now superseded, presented as historical audit record not live rules |

---

## 2. STAMINA

**Home definition.** `designs/scene/derived_stats_v30.md` §4.2 (lines 94-122) and §14.1 (line 538): `Stamina = (3 × Endurance) + (2 × Spirit)`, RATIFIED 2026-05-29 "S1," range 5–47, drains down, depleted-at-0 = "Out of Breath" (−2D all combat rolls), recovery = `(Endurance + relevant combat History) × 2`. Explicitly stated to replace `End + History + 1 − armour`. Also stated identically in `params/core.md:159`: `Stamina | (3 × Endurance) + (2 × Spirit) | 5–35 | ... (ED-694)` — **note the range itself differs between the two "current" sources: derived_stats_v30 says 5–47, params/core.md says 5–35** (both cite the same formula and same ED, but disagree on the stated numeric range — likely params/core.md wasn't updated when the formula range was recalculated, itself a minor but real divergence between two co-canonical docs).

**Exhaustive usage sweep** (representative, excluding archives/deprecated):
- `params/core.md:159`
- `references/name_collision_database.yaml:97`
- `references/valoria_interdoc_audit.md:55,57,289`
- `references/valoria_complete_systems_r2.md:131`
- `references/module_contracts.yaml:823`
- `references/mechanical_terms_index.md` (general index entries)
- `skills/valoria-combat-simulator/references/combat_params.md:30,86,128`
- `skills/valoria-combat-simulator/scripts/combat_sim.py:58-60,116-117`
- `designs/scene/combat_v30.md:303`
- `designs/scene/combat_engine_v1/combatant.py:26-27,45-47,122`
- `designs/scene/combat_engine_v1/config.py` (CONC_* constants reference Focus+Spirit, adjacent but not Stamina itself)
- `designs/scene/combat_engine_v1/systems.py`, `state_graph.py`, `wrapper.py` (consume `stamina_max`/`.stamina` at runtime)

**Divergence check** — a genuine three-way split, worse than Health because the oldest layer is *still executing*:

1. **Current canon**: `(3×End)+(2×Spirit)` — `params/core.md:159`, `derived_stats_v30.md §4.2/§14.1`, `module_contracts.yaml:823` ("3*End+2*Spirit (full port; not in the slice)"), `combatant.py:45-47` (`stamina_max = STAMINA_PER_END*end + STAMINA_PER_SPIRIT*spirit`).
2. **Superseded intermediate**: `designs/scene/combat_v30.md:303`: `**Stamina = Endurance × 5** (range 5–35). ... (ED-694, replaces composite formula.)` — this is the ED-694 form that derived_stats_v30 §12 explicitly says was itself superseded by the "S1" ratification (`Stamina = End × 5 [SUPERSEDED by RATIFIED S1: now (3×End)+(2×Spirit)]`, derived_stats_v30.md:505). combat_v30.md was never updated past ED-694 even though it's supposedly the personal-combat design-layer source.
3. **Oldest, pre-ED-694 formula, still literally running**: `skills/valoria-combat-simulator/references/combat_params.md:30,86,128`: `Stamina = Endurance + Relevant History + 1 (modified by armour)` — and `skills/valoria-combat-simulator/scripts/combat_sim.py:58-60`:
   ```
   def stamina_max(ar, end, history_points):
       _, _, stam_mod = ARMOURS[ar]
       return max(1, end + history_points + 1 + stam_mod)
   ```
   This is exactly the formula `derived_stats_v30.md §4.2` labels "**Eliminates:** Current formula `End + History + 1 − armour_mod`." The skill's own reference file even states elsewhere (line 26-29, same file) the *current* ED-901/ED-1084 Combat Pool formula — so the file was partially maintained (Combat Pool updated) while Stamina/Health were left at the oldest possible layer, two supersession-generations behind. **This script is executable and would be invoked by anyone running the `valoria-combat-simulator` skill today, producing Stamina and Health values that don't match any currently-ratified canon.**
4. `references/valoria_complete_systems_r2.md:131`: `Stamina: End+1, min 2 (armour mod)` — yet a **fourth**, even more truncated variant, distinct from all three above (drops History entirely). This looks like an intermediate-patch snapshot (references PP-248's "corrected to End+1" note visible in `params/core.md:5`) frozen in an old reference doc.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/scene/derived_stats_v30.md §4.2/§14.1` | CANONICAL DEFINITION | Declared authoritative ("RATIFIED 2026-05-29 S1") | — |
| `params/core.md:159` | HARDCODED DUPLICATE | Independent literal, same formula, but states range 5–35 vs canon's 5–47 | Formula: YES; range: **NO**, mismatched |
| `references/module_contracts.yaml:823` | HARDCODED DUPLICATE (documentation-grade) | Independent inline comment `3*End+2*Spirit` | YES |
| `designs/scene/combat_engine_v1/combatant.py:26-27,45-47` | HARDCODED DUPLICATE | Independent Python literal, no exporter ties it to the markdown source | YES, exactly, with citation comments |
| `designs/scene/combat_v30.md:303` | HARDCODED DUPLICATE | Independent literal `End × 5`, superseded intermediate | **NO** — one generation stale (ED-694, not S1) |
| `skills/valoria-combat-simulator/references/combat_params.md:30,86,128` | HARDCODED DUPLICATE | Independent literal `End+History+1`, pre-ED-694 | **NO** — two generations stale |
| `skills/valoria-combat-simulator/scripts/combat_sim.py:58-60` | HARDCODED DUPLICATE | Independent, executable Python literal, same pre-ED-694 formula | **NO** — and it's live code, not just a stale doc |
| `references/valoria_complete_systems_r2.md:131` | HARDCODED DUPLICATE | Independent literal `End+1, min 2` | **NO** — a distinct fourth variant |
| `references/valoria_interdoc_audit.md:55-57,289` | UNCLEAR / NO CANONICAL SOURCE (as a historical artifact) | This is itself an audit document *cataloging* the combat_v30/params_combat divergence — it's diagnostic, not a live restatement, but it's also not simply a citation | N/A — historical audit record |

---

## 3. COHERENCE (personal / Thread practitioner sense)

**Home definition.** `designs/threadwork/threadwork_v30.md` PART THREE (lines 602-670): range 10 (fully coherent) → 0 (rendering crisis), starting value 10 for all practitioners (non-practitioners untracked), §3.2 Coherence Reduction table (Object/Personal 0, Relational/Territorial −1, Structural −2, FR surcharge −1 additional cap-exempt, Mending 0 per ED-871), §3.3 Coherence Thresholds (10-8 Stable, 7-5 Dissonant, 4-3 Fragmented, 2 Fractured, 1 Severed, 0 Rendering Crisis), §3.5 Recovery. Cross-referenced philosophically in `canon/00_philosophical_foundations.md` (Coherence as layer-two self-rendering integrity) and `canon/02_canon_constraints.md:19` (P-10 compliance test).

**Exhaustive usage sweep** (634 files hit `coherence` case-insensitively repo-wide — the great majority are the *ordinary-English* sense "logical coherence," "narrative coherence," "coherence of the design," etc., which I have excluded as incidental per instruction 5; below are the files carrying the actual **game-mechanical Coherence track**):
- `designs/threadwork/threadwork_v30.md` (dozens of consistent uses, e.g. lines 53, 92, 133, 262, 283-284, 343-344, 370, 394-395, 429-430, 446, 476-479, 524, 554-559, 575, 595, 602-670, 704-729, 760, 765, 778, 898, 907, 957, 960, 970, 982)
- `params/threadwork.md:14,50,164,278`
- `params/threadwork_superseded.md` (retired file, "RS"-era terminology, ~15 hits)
- `canon/00_philosophical_foundations.md` (philosophical layer-two definition, ~10 hits)
- `canon/02_foundations_amendment_leap_mechanism.md`, `canon/02_canon_constraints.md`, `canon/01_foundations_amendment_self_rendering.md`
- `canon/patch_register_index.md:19` (PP-012, archived, "Intelligibility track / Coherence track" reconciliation)
- `references/glossary.md:49,563` (Part One + §14.2 Tracks table)
- `references/module_contracts.yaml:288,343`
- `references/values_master.yaml` (many entries, citing "params_threadwork.md" and "params_core.md")
- `sim/thread/operations.py:41,102-113,180-194,282-331`
- `sim/thread/coherence.py` (imported by operations.py — the actual state-mutation module)
- `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_threadwork.md:156`

**Divergence check** — three separate, precisely dated findings:

1. **The design doc's own inline commentary about the sim is now stale.** `designs/threadwork/threadwork_v30.md:624`:
   > "Mending | 0 (restorative operation type — ED-871 ... **Sim `sim/thread/operations.py` still charges −1/−2 — SIM-CODE fix deferred to Stratum B**, entangled with the C-TW-3 blanket-penalty bug and lacking test coverage)"

   But `sim/thread/operations.py:316-324` (`attempt_mending`) reads:
   > "Per ED-871 (2026-05-31) + canon/02 Amendment 3: Mending is a RESTORATIVE operation type and costs 0 Coherence at every degree ... (Was -1, the pre-ED-871 value; **the doc side was propagated to threadwork_v30 §3.2 + params/threadwork.md on 2026-07-07, and the sim is closed here.**)"

   and `params/threadwork.md:278` independently corroborates: "...noted here for co-file provenance after the **2026-07-07 propagation that fixed threadwork_v30 §3.2's stale −1**." All three agree the Mending-cost *value* is now 0 everywhere — but threadwork_v30.md's own §3.2 parenthetical claiming the sim fix is "deferred to Stratum B" was **not updated** when the actual fix landed the very next day (today is 2026-07-08). This is a live, dated documentation-currency defect inside the canonical head itself.

2. **An independently-discovered code bug, found while verifying finding #1.** `sim/thread/operations.py:224-245` (`attempt_leap`) states in its own docstring: "Failure does NOT cost Coherence per §3.2 (Leap is the rendering-suspension act, not yet an operation)," and the Leap call itself passes `coherence_delta=0` (line 245). But the shared resolution path `_resolve_operation` (lines 180-191) applies a blanket rule: `if degree in ("Partial", "Failure") and operation != "Mending": effective_coh -= 1`. Since `operation == "Leap"` (not `"Mending"`), a Failed or Partial Leap **will** be charged −1 Coherence despite the function's own docstring and comment ("Leap itself has no Coherence cost") saying otherwise. The code's own comment at lines 186-188 acknowledges a related defect exists ("The broader C-TW-3 defect — this blanket penalty also mis-hits Leap against its own docstring — is NOT fixed here") — confirming this is a known, still-open bug, not a misreading on my part.

3. **`canon/patch_register_index.md:19`**: `| PP-012 | archived | | 2026-03-27 | Intelligibility track / Coherence track (§4.5 vs §5.10) |` — evidence that Coherence has absorbed/replaced a separate "Intelligibility" track since as far back as 2026-03-27 (see §4 below for the live consequence of this).

4. **`references/values_master.yaml`** Coherence-loss table entries (lines ~3023-3086) cite `section: "params_threadwork.md — Thread Operations (v2.5) > Coherence (10→0)"` with values and terminology ("Rendering Stability," pre-ED-871 Mending cost of −1) that match `params/threadwork_superseded.md` far more closely than the live `params/threadwork.md` — consistent with CLAUDE.md §5's documented warning that values_master.yaml "pulls 8 values from `params/threadwork_superseded.md`." Not independently re-derived here byte-for-byte, but the term "Coherence" is one of the contaminated entries.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md §3.1-3.5` | CANONICAL DEFINITION | Declared home; all other docs point here | — |
| `params/threadwork.md:14,50,164,278` | PULLED / REFERENCED (mostly) with one HARDCODED restatement | Line 14/50/164 restate range/values as a params table (independent literal, but co-file-maintained in lockstep — confirmed by the 2026-07-07 sync note at line 278) | YES |
| `canon/00_philosophical_foundations.md`, `canon/02_*` | CANONICAL (philosophical layer, different register) | These define Coherence's *ontological* meaning (layer-two self-rendering), not a duplicate of the numeric mechanic — complementary, not competing | N/A (no numeric formula restated) |
| `references/glossary.md:49` | HARDCODED DUPLICATE | Independent short-form restatement ("10→0... Starts at 10") | YES — this entry (unlike Intelligibility/Composure below) is actually current |
| `references/module_contracts.yaml:288` | HARDCODED DUPLICATE (flagged) | Bucket classified `[ASSUMPTION bucket]`, independent | Unverified per its own flag |
| `sim/thread/operations.py:104-112` (`COHERENCE_COST_BY_SCALE`) | HARDCODED DUPLICATE | Independent Python dict literal, inline-cited `[canonical: threadwork_v30 §3.2]` | YES for the scale-cost table; **NO** for the Leap-Failure bug (see divergence #2) |
| `sim/thread/operations.py:316-331` (Mending) | HARDCODED DUPLICATE | Independent Python literal `coh = 0` | YES (matches ED-871, and per its own comment, is *more* current than threadwork_v30.md's stale parenthetical) |
| `references/values_master.yaml` (Coherence-loss rows) | HARDCODED DUPLICATE (contaminated) | Cites "params_threadwork.md" but content pattern matches the retired `params/threadwork_superseded.md` | **NO** — pre-ED-871 values (Mending −1/−2) |
| `canon/patch_register_index.md:19` | HARDCODED DUPLICATE (historical, archived status) | Independent one-line historical note, `status: archived` | N/A — self-flagged as archived |

---

## 4. INTELLIGIBILITY

**Home definition — contested.** `references/glossary.md:50` (Part One, Derived Character Stats, "last updated 2026-07-01"):
> `| Intelligibility | — | 10→0 | How legibly reality presents to a fractured practitioner. **Intelligibility is what they perceive of the breakage**. Non-practitioners sense wrongness at threshold. |`

This presents Intelligibility as a **live, distinct, separately-tracked 10→0 personal stat**, conceptually paired with (but distinct from) Coherence. **This is directly contradicted by the actual canonical Threadwork head.** `designs/threadwork/threadwork_v30.md` §8.1 "Systems Replaced" (lines 976-990):
> `| Intelligibility (§4.5, 10→0) | Coherence (10→0) | All character sheets, all Thread operation tables |`

This table explicitly lists "Intelligibility" as an **"Old System" that has been REPLACED BY Coherence** — i.e., per the canonical Threadwork head itself, Intelligibility as a separate numeric character track **no longer exists**; it was folded entirely into Coherence, with no separate tracking. Corroborating this retirement: `canon/patch_register_index.md:19` shows `PP-012 | archived | 2026-03-27 | Intelligibility track / Coherence track (§4.5 vs §5.10)` — the reconciliation happened as far back as **2026-03-27**, over three months before the glossary's own "last updated 2026-07-01" stamp.

**A second, genuinely distinct mechanic shares the same word.** `designs/scene/fieldwork_v30.md:15,20`, `fieldwork_v30_infill.md:11,13,18`, `fieldwork_rationale.md:11,13`, `fieldwork_godot.md:33,35`: "**Intelligibility Gradient**" — a world/substrate-scale design *principle* ("how much of the Thread substrate is intelligible to a given consciousness," varying by TS band, distance from settled centres, MS level). This has **no numeric 10→0 character track** at all — it's a qualitative gradient governing which Points of Interest/information a character can perceive, not a depleting personal resource. This is a second, unrelated mechanic sharing the "Intelligibility" name with the (retired) personal stat.

**Exhaustive usage sweep** (63 files hit `\bintelligibility\b`; key distinct sites):
- `references/glossary.md:50` (stale, treats as live)
- `references/mechanical_terms_index.md:94,775,865` (line 94 treats as live *and* miscites its source as "threadwork §3, fieldwork §1" — §3 is the Coherence section, not an Intelligibility section, and "fieldwork §1" is actually about the unrelated Intelligibility Gradient)
- `references/alias_registry.yaml:78-81` (also treats as live: `category: stat, range: "10->0"`)
- `references/throughlines_complete.md:22,269` (uses "Intelligibility" loosely to mean the fieldwork Gradient concept)
- `designs/threadwork/threadwork_v30.md:982` (the retirement table itself)
- `designs/scene/fieldwork_v30.md`, `fieldwork_v30_infill.md`, `fieldwork_rationale.md`, `fieldwork_godot.md`, `fieldwork_v30_index.md` (all "Intelligibility Gradient" — the distinct mechanic)
- `canon/00_philosophical_foundations.md` (philosophical epistemic-accessibility sense — "the Intelligibility Dimension," §1.2 — a *third*, purely philosophical register, foundational to both mechanical uses but not itself a numeric track)
- `params/threadwork_superseded.md:371` (old, retired file — one incidental cross-reference)
- No hits at all in `sim/` for `intelligibility` (the retired stat was never implemented in code, consistent with its retirement) or in `params/threadwork.md` (the live params file has already dropped it, consistent with the retirement)

**Divergence check:**

- **The glossary is stale by over three months on a fully-retired mechanic.** Glossary line 50 presents Intelligibility as a live, distinct, mechanically-defined 10→0 stat; threadwork_v30.md §8.1 (the canonical Threadwork head per `CURRENT.md`) says it was fully folded into Coherence, and the retirement traces back to archived patch PP-012 (2026-03-27). Note `params/threadwork.md` (the current live params doc) has *already* dropped Intelligibility entirely — it isn't in that file at all — so the params layer is already correctly current; only the glossary (and its dependents below) lag.
- **`references/mechanical_terms_index.md:94`** compounds the error: it not only repeats the stale glossary definition but miscites "threadwork §3" (the Coherence section) as Intelligibility's home, and "fieldwork §1" (the unrelated Gradient concept) as a second home — conflating two distinct mechanics into one row.
- **`references/alias_registry.yaml:78-81`** independently corroborates the glossary's stale view (`category: stat, range: "10->0"`), suggesting the staleness has propagated across at least three reference files (glossary, mechanical_terms_index, alias_registry) rather than being an isolated typo.
- **Two distinct mechanics share one name**, exactly as the audit brief anticipated: (a) the retired 10→0 personal stat (glossary/mechanical_terms_index/alias_registry's view, dead per threadwork_v30 canon), and (b) the live "Intelligibility Gradient" world-perception principle (fieldwork_v30's actual current usage, no numeric character track).

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:982` | CANONICAL DEFINITION (of the *retirement*) | This is the authoritative statement that the old Intelligibility-as-stat no longer exists | — |
| `references/glossary.md:50` | HARDCODED DUPLICATE | Independent restatement of a fully retired mechanic as if live | **NO** — describes a dead system as current |
| `references/mechanical_terms_index.md:94` | HARDCODED DUPLICATE | Independent restatement + miscited sources | **NO** |
| `references/alias_registry.yaml:78-81` | HARDCODED DUPLICATE | Independent YAML entry, `category: stat` | **NO** |
| `designs/scene/fieldwork_v30.md` etc. ("Intelligibility Gradient") | CANONICAL DEFINITION (of a *different* mechanic) | This is the live, correct usage — but of a different concept than what glossary/mechanical_terms_index/alias_registry describe | N/A — not the same mechanic |
| `canon/00_philosophical_foundations.md` §1.2 | CANONICAL (philosophical register) | Foundational epistemic-accessibility concept underlying both mechanical senses; not itself a numeric duplicate | N/A |
| `params/threadwork.md` | (absent) | Correctly does not carry the retired stat at all | N/A |
| `sim/` (any package) | (absent) | Never implemented, consistent with retirement | N/A |

---

## 5. COMPOSURE

**Home definition — bifurcated by design.** Two legitimately different scopes coexist:
1. **General derived-stat home:** `designs/scene/derived_stats_v30.md` §5.1 (lines 128-145) and §14.1 (line 539): `Composure = Charisma × 3`, range 3–21, strain accumulates toward threshold, Rattled when strain ≥ Composure. Also `params/core.md:160`: identical formula and range, "(ED-694, replaces Cha+6)."
2. **Contest-tracker home — explicitly RETIRED.** `designs/scene/social_contest_v30.md` §4 (lines 231-251, 481-512) and `params/contest.md:133,137,143,148,151,161,308`: **"CR3 (RATIFIED 2026-06-01)"** retires the single Composure buffer *as the social-contest tracker*, splitting it into **Face** (contest-local ethos/standing, bound to the kernel's `Standing` primitive) and **Concentration** (stamina). The Charisma×3 magnitude itself is retained unchanged (now called Face_max), but the tracker's *name and role* in Debate/contest is Face, not Composure. This is corroborated in code: `sim/personal/contest/primitives.py:167-169`: `RETIRED_TRACKERS = ("Composure",)`, and `sim/personal/contest/_kernel_tests.py:714-719` asserts as a CI-enforced test: `ck("CR3: Composure is retired (listed in RETIRED_TRACKERS, absent from the live TRACKERS)", "Composure" in _RETIRED and "Composure" not in _TRK)`.

The retirement is **explicitly scoped**: `social_contest_v30.md:509`: "Composure references in **knots**, **combat**, and **conviction** are deliberately NOT rewritten here" — so Composure legitimately remains live in those other systems; only its role as *the contest damage/endurance track* is retired.

**Exhaustive usage sweep** (289 files hit `composure`; key distinct sites beyond the two homes above):
- `references/glossary.md:51,89,244` (Part One, Part Three, Part Twelve collision table)
- `references/module_contracts.yaml:343` (knots_v30 propagation note, not a state field)
- `references/descriptor_registry.yaml:53,107` (derived_values list)
- `references/values_master.yaml:692,812-826,1136-1143,2554-2562` (cites `params_contest.md — Social Contest System (v2)`, an old version-2 label)
- `designs/scene/social_contest_system_v2.md:207,281,368` — **SUPERSEDED** doc (Status line: "SUPERSEDED — canonical doc is `designs/scene/social_contest_v30.md`... DO NOT CITE AS LIVE RULES"), correctly self-flagged, contains the pre-ED-694 `Composure = Charisma + 6` formula.
- `designs/personal/knots_v30.md:47,56,98,124,126-127` (§4.2 "Knot-as-Composure-buffer" — deliberately NOT rewritten per the CR3 scope decision)
- `designs/threadwork/threadwork_v30.md:554-559,595` (Composure as Knot-strain currency during Thread lattice-collapse events — outside the contest-tracker scope, unaffected by CR3)
- `sim/personal/contest/primitives.py:58-169`, `_kernel_tests.py:698-719`, `wrapper.py:24,283,293-294` (the CR3 retirement machinery)

**Divergence check — this is the flagged finding the task explicitly asked me to verify, and I confirm it as real:**

- **`references/glossary.md:51`** (Part One): `| Composure | — | varies | Social endurance track. **Used in Debate.** Rattled at ≤ 2; concession forced at 0. |`
- **`references/glossary.md:89`** (Part Three, Debate System Terms): `| Composure | — | varies | Social endurance (see Part One). **Also the damage track in Debate exchanges.** |`

Both entries present Composure as the live, current Debate/contest damage track. This directly contradicts the canonical contest head, `designs/scene/social_contest_v30.md:231`: **"the single Composure buffer is RETIRED as the social-contest tracker"** — a ratified decision (CR3, 2026-06-01) that predates the glossary's own "last updated 2026-07-01" stamp by over a month. The glossary was touched *after* the retirement and still didn't reflect it. This is a clean, dated glossary-currency defect exactly analogous to (and compounding) the Intelligibility finding above — two of eight terms in this batch have the *same class* of defect (glossary lagging a ratified retirement by 1+ months), suggesting a systemic glossary-maintenance gap rather than two isolated slips.
- **`references/glossary.md:244`** (Part Twelve collision table): `| COMP | Composure (Debate context) | Computation / Composition (general English) | Write "Composure" in game documents. |` — same stale "Debate context" framing, a third glossary location repeating the error.
- **`derived_stats_v30.md` §5.1** itself (dated 2026-04-18, i.e., predates CR3 by over a month) presents Composure under the header "Personal Scale: Social Contest Resources" with no acknowledgment that its contest role was later retired — this doc is dated in a way that explains (but doesn't excuse, since nothing has gone back to annotate it) its staleness; it's a live-cited authority for the Charisma×3 *magnitude* (which CR3 explicitly preserves) but stale on the *tracker role* question.
- **`references/module_contracts.yaml`**: the `social_contest` module's declared `state:` list (line 447, `- {name: "persuasion_track", bucket: clock, writable: true}`) lists **only** persuasion_track — neither the old Composure nor the new Face/Concentration trackers appear in the formal module contract at all. This is a silent gap, not a contradiction, but it means the module contract itself offers zero help in resolving which of the two pictures (old Composure vs new Face/Concentration) is authoritative for a Godot implementer reading only that file.
- **`references/values_master.yaml`** cites `"params_contest.md — Social Contest System (v2)"` (e.g. line 692) — "Social Contest System (v2)" is the old `social_contest_system_v2.md` naming, itself confirmed SUPERSEDED — reinforcing that this reference file's Composure entries trace to a doubly-stale lineage.
- **`designs/personal/knots_v30.md` §4.2** ("Knot-as-Composure-buffer") is *correctly* still using "Composure," per the CR3 scope decision — this is **not** a divergence, it's an intentionally-preserved usage, explicitly cross-referenced and acknowledged as pending harmonization in `social_contest_v30.md:508-512`'s own "OPEN-DECISION" note (resolved 2026-07-01 as "scoped-rename-only, no further change").

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/scene/derived_stats_v30.md §5.1` | CANONICAL DEFINITION (magnitude only) | Declared source for the Charisma×3 formula, which CR3 explicitly preserves | Formula: YES; contest-tracker-role framing: **NO**, predates CR3 |
| `params/core.md:160` | HARDCODED DUPLICATE | Independent literal `Charisma × 3`, "(ED-694, replaces Cha+6)" | YES (magnitude only; silent on CR3) |
| `designs/scene/social_contest_v30.md §4` | CANONICAL DEFINITION (of the *retirement* / Face rename) | Declared authoritative for the contest-specific role change | — |
| `params/contest.md:133-161` | PULLED / REFERENCED + restatement | Explicitly co-file-synced with social_contest_v30 (cites CR3/ED-1056 throughout), functions as the params mirror of the same ratified decision | YES |
| `references/glossary.md:51,89,244` | HARDCODED DUPLICATE | Three independent restatements, all presenting the retired "Debate context" framing as current | **NO** — retired over a month before glossary's own "last updated" date |
| `designs/scene/social_contest_system_v2.md:207,281,368` | HARDCODED DUPLICATE (self-flagged superseded) | Independent literal `Cha + 6`, but file's own Status line says "SUPERSEDED... DO NOT CITE AS LIVE RULES" | **NO**, and correctly self-flagged as such |
| `designs/personal/knots_v30.md §4.2` | HARDCODED DUPLICATE (intentionally preserved) | Independent restatement, but explicitly acknowledged and scoped-exempted by social_contest_v30.md's own Gate-A ruling | Not contradictory — deliberately out of CR3's scope |
| `sim/personal/contest/primitives.py:167-169` | CANONICAL DEFINITION (of the code-level retirement) | `RETIRED_TRACKERS = ("Composure",)`, CI-enforced by `_kernel_tests.py:714-719` | — |
| `references/module_contracts.yaml` (social_contest state list) | UNCLEAR / NO CANONICAL SOURCE | Silent on Composure/Face/Concentration entirely — offers no adjudication either way | N/A |
| `references/values_master.yaml:692,812-826` | HARDCODED DUPLICATE | Independent literal, cites the superseded "Social Contest System (v2)" naming | **NO** |

---

## 6. FOCUS (contact-duration derived use)

**Home definition — actively contested within the very document that changed it.** `references/glossary.md:52` (Part One, Derived Character Stats): `| Focus | — | 1–5+ | Contact duration in Thread operation rounds. |`

But `designs/scene/derived_stats_v30.md` §6.1 (lines 249-259) and §12 (line 508), the doc that authored the change (ED-694), states:
> "**Focus role change:** Focus no longer sets contact duration. Contact Rounds eliminated. Focus sets maximum operations per contact session, preserving current `Focus − 1` cap" — with duration now governed by **Thread Fatigue = Spirit × 5** (§6.1, line 231).

`params/core.md:162` agrees with the *new* framing: "Focus sets max operations per session (Focus − 1). (ED-694, replaces Contact Rounds = Focus)."

**Exhaustive usage sweep:**
- `references/glossary.md:52` (old framing — "Contact duration")
- `references/mechanical_terms_index.md:97` ("Focus | ... | Contact duration in Thread operation rounds. | threadwork §2.3" — old framing, citing the *correct section* but stating the *superseded content of that section*)
- `references/alias_registry.yaml:89-...` (`focus:` entry, category stat)
- `references/descriptor_registry.yaml:38` (`{key: attr.mind.focus, name: Focus, aliases: []}` — the 9-attribute roster's "mind" bucket)
- `params/core.md:162` (new framing)
- `params/threadwork.md:16` ("Focus | 1–7 | Contact Rounds duration only. Not a pool dice contributor." — **old framing**, in the file that is otherwise the live/current threadwork params doc)
- `designs/threadwork/threadwork_v30.md:191,200,205,207-214` (new framing: "Focus role: Focus no longer sets contact duration...") **and** `:455,458` (old framing: "Focus continues to govern Contact Rounds (duration), not pool dice") — **both inside the same document**
- `designs/threadwork/threadwork_v30.md:968,1008` (Board-Game/Hybrid comparison tables still listing the Mending pool as "Att + Focus + Thread Pool Score" — a formula the same document's line 458 says is struck: "Attunement and Focus struck from pool dice")
- `designs/scene/derived_stats_v30.md §5.2,§14.1` (Focus as a component of the Concentration formula `(3×Focus)+(2×Spirit)` — a *different*, Debate-context use of Focus, not contact duration)
- `designs/scene/combat_engine_v1/config.py:60-61,128`, `systems.py:826-853`, `combatant.py:93-141` (Focus used as a general attribute affecting poise/structure recovery and disruption resistance in **personal combat** — a third, non-Thread application)
- `sim/personal/contest/primitives.py:98-103` (Focus feeding Concentration's canonical `(3×Focus)+(2×Spirit)`, correctly cited)

**Divergence check:**

- **Glossary is stale on the specific point this batch flagged it for.** `glossary.md:52`'s "Contact duration in Thread operation rounds" is precisely the role `derived_stats_v30.md:249` says was eliminated ("Focus no longer sets contact duration. Contact Rounds eliminated").
- **`references/mechanical_terms_index.md:97`** cites "threadwork §2.3" as Focus's source — this is the *correct* section (Focus's role-change subsection is inside §2.3, confirmed at `threadwork_v30.md:180` "### Contact Duration (ED-694: Thread Fatigue replaces Contact Rounds)" and `:142` "## 2.3 The Leap"). But the index's own stated content ("Contact duration in Thread operation rounds") is exactly the value that same section says is superseded — a citation to the right place with the wrong (superseded) value copied out of it.
- **`params/threadwork.md:16`**, a file otherwise treated as the live threadwork params doc (distinct from the retired `threadwork_superseded.md`), still states: "Focus | 1–7 | **Contact Rounds duration only.** Not a pool dice contributor." — directly contradicting `derived_stats_v30.md §6.1`'s ratified role change.
- **Intra-document self-contradiction inside the canonical Threadwork head itself**, mirroring the Health/Coherence pattern found above: `threadwork_v30.md:191` ("Focus no longer sets contact duration... sets max operations per contact session") directly contradicts the same file's `:455,458` ("Focus continues to govern Contact Rounds (duration), not pool dice... The prior Attunement + Focus construction is struck"). Two different sections of one canonical document assert opposite things about what Focus currently does.
- **Struck formula still visible in summary tables.** `threadwork_v30.md:968,1008` present the Mending pool as "Att + Focus + Thread Pool Score" in Board Game / Hybrid comparison tables, even though line 458 (same document) says "Attunement and Focus struck from pool dice" per PP-616/PP-625, and the actually-current pool formula (confirmed independently in `sim/thread/operations.py:145-157`) is `(Spirit × 2) + History + TPS` with no Focus or Attunement term at all.
- **Structural classification conflict, not just a value conflict.** `references/descriptor_registry.yaml:38` lists Focus as a first-class 1–7 **attribute** (`attr.mind.focus`), part of the 9-attribute roster CLAUDE.md's ED-IN-0025 note already flags as conflicting with the glossary's 7-attribute Core Attributes table (which does *not* include Focus at all — glossary's Core Attributes table lists only Agility, Attunement, Cognition, Endurance, Presence, Spirit, Strength). Live usage in `combat_engine_v1/combatant.py:93-97` treats `self.focus` exactly like the other attribute fields (`cog`, `att`, `spirit`), reinforcing that in practice Focus behaves as a general character attribute (used in Thread contact rules, Debate Concentration, *and* Combat poise/disruption resistance) rather than the glossary's narrow single-purpose "Derived Character Stat" framing.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/scene/derived_stats_v30.md §6.1/§12` | CANONICAL DEFINITION | Authors the ED-694 role change | — |
| `params/core.md:162` | HARDCODED DUPLICATE | Independent restatement of the new framing | YES |
| `designs/threadwork/threadwork_v30.md:191,207-214` | HARDCODED DUPLICATE | Independent restatement, new framing | YES |
| `designs/threadwork/threadwork_v30.md:455,458` | HARDCODED DUPLICATE | Independent restatement, old framing — **same file** as the row above | **NO** — contradicts its own §2.3 elsewhere |
| `designs/threadwork/threadwork_v30.md:968,1008` | HARDCODED DUPLICATE | Independent restatement of a struck pool formula in a summary table | **NO** |
| `params/threadwork.md:16` | HARDCODED DUPLICATE | Independent literal, old framing, in an otherwise-live params file | **NO** |
| `references/glossary.md:52` | HARDCODED DUPLICATE | Independent restatement, old framing | **NO** |
| `references/mechanical_terms_index.md:97` | HARDCODED DUPLICATE | Independent restatement, correctly-cited section, wrong (superseded) content | **NO** |
| `references/descriptor_registry.yaml:38` | UNCLEAR / NO CANONICAL SOURCE (structural) | Classifies Focus as an attribute; no file adjudicates attribute-vs-derived-stat status between this and glossary | Conflicts with glossary's classification, not just its value |
| `sim/personal/contest/primitives.py:98-103` | PULLED / REFERENCED | Explicit citation chain "ED-901 (STRUCK Focus*3) + ED-902 ... + ED-933," no independent Focus-duration claim | N/A (doesn't touch contact-duration question) |
| `designs/scene/combat_engine_v1/combatant.py:97,systems.py:826-853` | HARDCODED DUPLICATE (different domain) | Independent use of `self.focus` as a general combat-poise/disruption modifier, unrelated to contact duration | N/A — a third, non-conflicting but unacknowledged expansion of Focus's scope |

---

## 7. CERTAINTY

**Home definition.** `params/core.md` §Certainty Track (lines 183-214), "PP-551 — redesigned from PP-289": range 0–5 oscillating, 5 = Full Solmund orthodoxy, 0 = Full Thread acceptance, six-point label table (Orthodox→Accepted), starting value assigned by background, movement triggers, mechanical effects by band, Church-interaction-by-level table. Line 197: "All player characters. Named NPCs at GM discretion. Factions do not hold Certainty." Line 212: "**Relationships: Independent of Coherence** (operational resource) and Thread Sensitivity (perceptual depth)." Line 214: "**Spirit is unrelated to Certainty.**"

**Exhaustive usage sweep** (318 files hit `certainty`; excluding ordinary-English "with certainty"/"uncertain" usage which is common in analysis prose and was excluded as incidental — the mechanical stat appears consistently in):
- `params/core.md:163,183-214` (home)
- `references/glossary.md:53,255` (Part One + Part Thirteen "RESOLVED — active stat")
- `references/mechanical_terms_index.md:98`
- `references/values_master.yaml:1188-1191` (range 0-5)
- `designs/provincial/faction_politics_v30.md`, `faction_canon_v30.md` (7-8 hits, Certainty as a factor in Church/faction NPC interactions — consistent, no independent formula restated)
- `designs/scene/investigation_systems_v30.md` (22 hits, e.g. lines 40,65-66,256-259,275,290,330-332,385-414,430,441 — all consistent value-band gating logic, no formula restatement)
- `designs/scene/fieldwork_v30.md`, `fieldwork_v30_infill.md`, `fieldwork_exploration.md`, `fieldwork_godot.md` (6 hits each area — consistent usage)
- `designs/world/character_histories_v30.md` (34 hits — starting-value assignment by background lifepath, e.g. lines 59,95,97,111,115,136,138,180,190,203,216,229,254,267, all consistent with the params/core.md background-assignment framework)
- `designs/world/solmund_master_document.md` (14 hits, narrative/lore usage, consistent)
- `designs/scene/social_contest_v30.md` (4 hits)
- `designs/scene/conviction_track_v30_infill.md` (2 hits)

**Divergence check:**

- **A direct, quotable contradiction between two currently-canonical heads.** `params/core.md:212` states Certainty is "**Independent of Coherence**," and line 214 adds "**Spirit is unrelated to Certainty.**" But `designs/threadwork/threadwork_v30.md:646` (§3.3 Coherence Thresholds, the "2 Fractured" row) states: "**Certainty maximum reduced by 1 per Coherence level below 3.**" This is a direct mechanical interaction between Coherence and Certainty asserted by the current Threadwork head, flatly contradicting the current Dice-engine head's explicit "Independent of Coherence" claim. Both `params/core.md` and `designs/threadwork/threadwork_v30.md` are listed as live current heads in `CURRENT.md` — this is a contradiction between two documents CURRENT.md itself certifies as canonical, not a stale-vs-live mismatch.
- No divergence found in the numeric range, formula, or starting-value framework itself across the wide usage sweep — every design doc and narrative doc sampled applies the 0–5 band consistently with `params/core.md`'s table.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `params/core.md §Certainty Track` | CANONICAL DEFINITION | Declared home, PP-551 | — |
| `references/glossary.md:53` | HARDCODED DUPLICATE | Independent short restatement | YES (range/description match; silent on the Coherence-interaction contradiction) |
| `references/mechanical_terms_index.md:98` | HARDCODED DUPLICATE | Independent restatement, cites "conviction_track, glossary §1" | YES |
| `designs/threadwork/threadwork_v30.md:646` | HARDCODED DUPLICATE (contradictory) | Independent mechanical claim asserting a Coherence-Certainty interaction | **NO** — contradicts params/core.md's explicit independence claim |
| `designs/scene/investigation_systems_v30.md` (22 sites) | PULLED / REFERENCED | Applies value bands (≥4, ≤2, =3) without restating the underlying formula/range as an independent literal | YES, consistent |
| `designs/world/character_histories_v30.md` (34 sites) | PULLED / REFERENCED | Applies the background-assignment framework (`params/core.md:199`'s "Starting value: Assigned at creation by background") without redefining it | YES, consistent |
| `references/values_master.yaml:1188-1191` | HARDCODED DUPLICATE | Independent literal range restatement, cites "params_core.md" | YES |

---

## 8. MOMENTUM

**Home definition.** `params/core.md:84-93,170-181` (§Momentum, §Momentum Carry Rule PP-255, §Momentum Auto-Success Interaction PP-243): range 0–4, gained +1 on Overwhelming (net ≥ 2×Ob AND net ≥ 3), spent 1 Momentum = 1 automatic success (non-Thread rolls only, added to not replacing the roll), resets to 0 at start of each **session** (not scene), carries between scenes within a session, cannot bank across sessions. `references/glossary.md:54`: "Momentum | — | 0–4 | Tactical resource. Gained on Overwhelming success or Belief achieved. Spent for automatic successes (non-Thread only)." — this glossary entry is **current and accurate**, no divergence found here.

**Exhaustive usage sweep and the specifically-requested verification:**

**Re-confirmed independently: combat_engine_v1 has ZERO real Momentum touchpoints.** Direct grep of the entire `designs/scene/combat_engine_v1/` package for `momentum` (case-insensitive) returns exactly two hits, both incidental physics English, not the game mechanic:
- `core.py:110`: "...is LINEAR in (perc/PERC_AUTH_REF) (E=1.0, **momentum-like**)..." — a physics-metaphor comment about force scaling, not the Momentum resource.
- `phase4_5_plan_v1.md:131`: "**angular-momentum** arrest time (Δω=τt/I)" — literal rotational physics, not the game mechanic.

I further confirmed this by reading `combatant.py`'s full state-variable list (lines 59-141): the `Combatant`/`WoundTracker` classes track `stamina`, `conc` (Concentration), `ready`, `initiative`, `poise`, `grip_position`, `lunge_depth`, etc. — there is **no `self.momentum` attribute anywhere**, and `references/module_contracts.yaml`'s formal `personal_combat` module contract (lines 805-825) enumerates its declared `state:` fields explicitly (Health, cumulative_damage, Wounds, Stamina, Initiative, Poise) — **Momentum is not among them.** This is a clean, doubly-confirmed absence, not a grep miss: Momentum has no code path, no state field, and no formal contract entry anywhere in the current personal-combat resolver.

Meanwhile, the **superseded** combat docs still define combat-specific Momentum-granting triggers that were never carried forward: `designs/scene/combat_v30.md:104` and `designs/scene/combat_design_v1.md:109,328-329,336` (identical text in both files) — "**Rescuer Momentum (PP-406):** Gains 2 Momentum on successful intercept... **Martyr Rule (PP-407):** ...+1 Momentum" — these are Rescue-action Momentum awards that exist only in the two pre-combat_engine_v1 documents (one explicitly banner-flagged `[PARTIALLY SUPERSEDED ED-900]`, the other with no supersession banner at all). Neither the Rescue action itself nor its Momentum payout appears anywhere in `combat_engine_v1`. This gap is **not flagged by any ED, TODO, or gap-note anywhere in the corpus** — it is a silent, unacknowledged mechanical omission, distinct from (and not softened by) the fact that Momentum's *general* definition in `params/core.md` remains intact and current.

**Other sweep sites:**
- `designs/scene/social_contest_v30.md:169,292,563,664` and `params/contest.md:178,220` — Momentum used correctly and consistently in the Debate/contest system (spend for auto-successes, +1 Momentum on Total Victory, Belief-alignment cap 1/contest) — genuinely applies the canonical mechanic, no divergence.
- `designs/scene/fieldwork_v30.md:225,281,307,413,445-446` — Momentum used correctly (Overwhelming/Belief-aligned triggers, cap 4) in fieldwork resolution — consistent.
- `sim/personal/beliefs.py:8-10,39-46,96,157-232` — the actual, correctly-implemented game mechanic: `MOMENTUM_CAP = 4` (line 41, citing fieldwork_v30 §5.5), `BELIEF_MOMENTUM_PER_CONTEST_CAP = 1` (line 44, citing social_contest_v30 §9.5) — matches canon exactly.
- `sim/personal/contest_legacy_stub.py:241` — `current_momentum = getattr(winning_actor, 'momentum', 0)` — correctly wired to the real mechanic.

**Two genuinely distinct mechanics share the "Momentum" name, excluded from the above as a different concept (flagged per instruction 5, not merged into the sweep):**
- `sim/peninsular/ci_track.py:10,39-41,106,142,152` and `sim/peninsular/season.py:64` — "**Institutional Momentum**," a named +1/season passive step in the Church Influence (CI) political-clock formula (PP-412 Step 1). Confirmed in the design doc itself: `designs/scene/conviction_track_v30.md:177`: "**Step 1 — Institutional Momentum (passive):** CI +1. (Unchanged from PP-402.)" This is a faction/world-clock sub-component wholly unrelated to the personal 0–4 tactical resource — a genuine second mechanic sharing the word, correctly excluded from the classification table below.
- `sim/provincial/massbattle.py:610,811,841,926-927` (`_momentum_speed`) — literal physics momentum in a formation-combat model (mass×velocity term for puncture-bonus calculation) — pure incidental/physics usage, excluded.
- `sim/personal/contest/dictionaries.py:639-752`, `modes.py:101-126`, `_kernel_tests.py:311-344` — "the room's momentum," "running adv is the room's MOMENTUM (drama)" — a colloquial/metaphorical usage describing the persuasion-track trend in a jury-trial sim (whether the running advantage "drives" the eventual verdict or is "un-fused" from it). This is **not** the game-mechanical Momentum resource at all — it's ordinary English describing rhetorical momentum — excluded as incidental per instruction 5, though it is worth noting the term collision could confuse a future reader searching this codebase for the real mechanic.

**Single-source classification:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `params/core.md:84-93,170-181` | CANONICAL DEFINITION | Declared home (PP-243/PP-255) | — |
| `references/glossary.md:54` | HARDCODED DUPLICATE | Independent short restatement | YES — accurate, no divergence found |
| `designs/scene/social_contest_v30.md:169,292,563` | PULLED / REFERENCED | Applies the mechanic ("per core engine §1.7"), explicit citation, no independent range/formula restated | YES |
| `designs/scene/fieldwork_v30.md:225,281,307,413,445-446` | PULLED / REFERENCED | Applies the mechanic with cap citation, no independent formula | YES |
| `sim/personal/beliefs.py:41,44` | HARDCODED DUPLICATE | Independent Python literal `MOMENTUM_CAP = 4`, explicitly cited to fieldwork_v30 §5.5 / social_contest_v30 §9.5 | YES |
| `designs/scene/combat_v30.md:104` | HARDCODED DUPLICATE (orphaned) | Independent PP-406/PP-292 Rescue-Momentum rule; no successor implementation exists | Formula itself unchanged, but its trigger action (Rescue) and payout are **absent from the current resolver** — functionally dead canon |
| `designs/scene/combat_design_v1.md:109,328-329,336` | HARDCODED DUPLICATE (orphaned) | Same PP-406/PP-407 rules, no supersession banner at all on this file | Same as above — unimplemented in current engine |
| `designs/scene/combat_engine_v1/` (entire package) | ABSENT — no site to classify | Confirmed via full-package grep + Combatant state-variable read + module_contracts.yaml state-list read: zero real Momentum implementation | N/A — this is the actual finding: canon (params/core.md + combat_v30's Rescue rules) describes a mechanic the current personal-combat engine does not implement at all |
| `sim/peninsular/ci_track.py` ("Institutional Momentum") | UNCLEAR / NO CANONICAL SOURCE relative to *this* term | Distinct, independently-named mechanic; not a duplicate of the 0-4 personal resource, but shares the bare word "Momentum" with no disambiguating registry entry anywhere | N/A — different mechanic |

---

## Cross-cutting observations (raw, not editorialized)

Two structural patterns recur across multiple terms in this batch and are worth surfacing as raw facts, since they showed up independently under more than one term:

1. **The same canonical head contradicts itself intra-document** for three of eight terms: `derived_stats_v30.md` (Health: §3/§13 vs §4.1), `threadwork_v30.md` (Coherence: §3.2's Mending-sim claim vs `operations.py`'s own dated fix-note; Focus: §2.3's role-change statement vs its own later Mending-pool subsection).
2. **`references/glossary.md` (Part One and Part Three), despite a "last updated 2026-07-01" stamp, is stale on three of eight terms** — Intelligibility (retired since archived PP-012, 2026-03-27), Composure (contest role retired by CR3, 2026-06-01), and Focus (contact-duration role eliminated by ED-694/derived_stats_v30 §6.1) — all three staleness gaps predate the glossary's own claimed last-touch date, and in two cases (Composure, Intelligibility) the underlying retirement was itself formally ratified well before that date.
