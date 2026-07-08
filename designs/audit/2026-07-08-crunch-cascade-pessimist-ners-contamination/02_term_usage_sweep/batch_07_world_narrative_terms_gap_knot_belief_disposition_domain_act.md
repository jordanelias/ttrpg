# Term Usage Sweep — Batch 7: World / Narrative terms: Gap, Knot, Belief, Disposition, Domain Action/Echo

# Batch 7 Usage Sweep: World / Narrative Terms

Method note: I read the four designated primary sources in full (`references/glossary.md` Part Seven, `designs/threadwork/threadwork_v30.md`, `designs/npcs/npc_behavior_v30.md`, `designs/architecture/scale_transitions_v30.md`), then grepped the entire working tree per term. For terms with 50–160+ file hits, I enumerate every canonical-directory (`canon/`, `params/`, `designs/`, `references/`) occurrence I could locate and sampled `tests/`/`archives/`/`deprecated/` occurrences for consistency rather than listing every line — per CLAUDE.md §1/§3, `tests/*.md` prose and everything under `archives/`/`deprecated/` are non-canonical (history/simulation-output, not behavioral contracts or currency signals), so I did not skip them but I did not treat their internal drift as canon-relevant unless it revealed something about a still-live file.

---

## 1. Gap

**Home definition:** `references/glossary.md:150` — "A rupture in the rendered substrate. Severity scales: Micro-Gap, Standard Gap, Entrenched Gap, Catastrophic Gap." The mechanically load-bearing version is `designs/threadwork/threadwork_v30.md` §2.4 Mending Ob table (lines 461–470):

| Gap Type | Ob | Min TS |
|---|---|---|
| Shifting Object (pre-Gap) | 2 | 50+ |
| Micro-Gap (same scene) | 3 | 50+ |
| Standard Gap (1 session–1 season) | 5 | 50+ |
| Entrenched Gap (1+ seasons) | 6 | 70+ |
| Catastrophic Gap (3+ seasons) | 7 | 70+ (Einhir framework/collective) |
| Locked Zone border | 8+ | 70+ (Einhir framework required) |

Formation triggers are scattered through the same doc: Weaving Failure at MS ≤ 40 → Shifting Object, MS ≤ 20 → Gap (line 284); Dissolution Overwhelming/Success/Partial/Failure → Micro-Gap/Gap/Shifting-Object/"Full Gap" respectively (lines 427–430); N-way opposing operations → "Gap forms at target's scale" (line 595).

**Usage sweep:** Canonical: `references/glossary.md:150`, `designs/threadwork/threadwork_v30.md` (dozens, internally consistent — sampled lines 284, 427–430, 461–470, 595, 812, 821, 909), `designs/threadwork/threadwork_v25_historical.md` (superseded predecessor, retains old Ob values under "Rendering Stability" naming — expected, marked historical), `designs/world/calamity_radiation_v30.md`, `params/bg/clocks.md` (MS-band Gap-formation dice, lines 9–20), `params/threadwork_superseded.md` (explicitly superseded per CLAUDE.md §1), `designs/scene/fieldwork_v30.md`, `designs/npcs/npc_behavior_v30.md`, `designs/provincial/mass_battle_v30.md`, `designs/arcs/*` (narrative usage, consistent). 65 files total; ~40 are `tests/sim*`/`tests/stress*` narrative simulation logs and `archives/*` — sampled several (`tests/sim/sim_x_13_pulling_dissolution.md`, `tests/sim/sim_thread_batch_04.md`) and found consistent terminology, no contradicting numeric claims.

**Divergence check:** The BG-mode Mend Ob table (`threadwork_v30.md` lines 927–934) is a **structurally different 4-category ladder** than the TTRPG 5-category-plus-Locked-Zone ladder:

TTRPG: Shifting Object(2) / Micro-Gap(3) / Standard Gap(5) / Entrenched Gap(6) / Catastrophic Gap(7) / Locked Zone border(8+)
BG: Shifting Object(1) / Standard Gap(2) / Entrenched Gap(3) / Catastrophic Gap(4)

BG collapses/omits **Micro-Gap** and **Locked Zone border** as categories entirely. This may be an intentional BG abstraction (faction-level Mend doesn't need same-scene resolution), but it is not stated as such — a reader could reasonably ask whether Micro-Gaps simply can't be Mended at BG scale, or are silently folded into "Standard Gap." Flagging as an unexplained structural asymmetry rather than a contradiction (the doc doesn't claim these ladders should match).

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees with canonical today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:461-470` | CANONICAL DEFINITION | This is the named home site | — |
| `designs/threadwork/threadwork_v30.md:927-934` (BG table) | HARDCODED DUPLICATE (partial) | Independently restates a 4-tier Ob ladder for the same concept, no cross-reference to the 5-tier table above it in the same doc | Diverges in structure (omits 2 of 6 TTRPG categories); not numerically contradictory since BG Ob values are lower by design, but the category mismatch is unexplained |
| `references/glossary.md:150` | PULLED/REFERENCED | Cites only the severity-name list, no Ob numbers restated | Agrees (no numbers to drift) |
| `params/bg/clocks.md:9-20` | PULLED/REFERENCED | Cites `designs/world/calamity_radiation_v30.md` as "Canonical source" explicitly (line 4) | Agrees — genuine reference, not restatement |
| `params/threadwork_superseded.md` | HARDCODED DUPLICATE, explicitly superseded | File is named/flagged superseded; CLAUDE.md §1 flags `values_master.yaml` pulls 8 stale values from this file | Known-stale by design; do not use |
| `designs/threadwork/threadwork_v25_historical.md` | HARDCODED DUPLICATE, historical | Predecessor doc, same Ob values under "Rendering Stability" naming | Superseded terminology (RS→MS per ED-731), expected drift |
| `tests/sim/*` (~40 files) | PULLED/REFERENCED (narrative use) | Simulation logs citing threadwork_v30's Ob table in play-by-play | Consistent in samples checked |

No incidental-English "gap" usages were counted (I filtered out ordinary-English "gap" hits like "gap between X and Y" — the grep pattern targeted the four capitalized severity terms specifically, which are unambiguously game-mechanical).

---

## 2. Shifting Object

**Home definition:** `references/glossary.md:151` — "Pre-Gap substrate instability. Less severe than a Gap; addressable by Mending." Mechanical anchor: `designs/threadwork/threadwork_v30.md` Mending Ob table, "Shifting Object (pre-Gap) | Ob 2 | Min TS 50+" (line 465), and formation triggers: Weaving Partial (line 283 "Mending Stability −1... Shifting Object risk" contextually) and Weaving Failure at MS≤40 (line 284), FR-both-fail-scaling table (§2.6, lines 579–585 — d6 risk scaling by scale), Locking's "sudden configurational release" risk on long-standing releases (line 412).

**Usage sweep:** 121 files. Canonical: `params/threadwork.md`, `designs/threadwork/threadwork_v30.md` (dozens of consistent uses — sampled §2.4 lines 283–284, 298, 306, §2.6 lines 554–591), `designs/scene/fieldwork_v30.md`, `designs/npcs/npc_behavior_v30.md`, `designs/provincial/mass_battle_v30.md`/`_infill.md`, `designs/world/southernmost_v30.md`, `designs/world/character_histories_v30.md` (Coherence erosion → "Shifting Object" risk framing), `designs/world/ms_trajectory_v1.md`, `designs/world/calamity_radiation_v30.md`, `sim/thread/opposing.py`, `references/values_master.yaml`. Remainder mostly `tests/sim*` (dozens) and `archives/*` — sampled `tests/sim/sim_mending_coherence_2026-04-17.md`, `tests/sim/sim_x_21_collective_weaving_brittleness.md`: consistent with canon.

**Divergence check:** No numeric contradiction found for the Ob=2/TS50+ definition across canonical files. One naming-generation note: `params/threadwork_superseded.md` retains "Thread Tension" instead of "Mending Stability" throughout its Shifting Object risk language (pre-ED-731 rename) — expected, file is explicitly superseded. No live-doc divergence found.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:465` | CANONICAL DEFINITION | Named home (Ob table) | — |
| `references/glossary.md:151` | PULLED/REFERENCED | One-line description, no formula | Agrees |
| `designs/npcs/npc_behavior_v30.md` (scattered) | PULLED/REFERENCED | Uses term as narrative-trigger flag only, no independent Ob restated | Agrees |
| `designs/provincial/mass_battle_v30.md` | PULLED/REFERENCED | Cites Shifting Object as MS-band consequence, imports threadwork's risk framing without restating Ob | Agrees |
| `params/threadwork_superseded.md` | HARDCODED DUPLICATE, superseded | Independent restatement under old TT naming | Superseded, do not use |
| `tests/sim/*` (~30 files) | PULLED/REFERENCED | Play-by-play citing canonical Ob | Consistent in samples |

No incidental-English collisions ("shifting" + "object" as ordinary words) were found in a scan of the hit list — every occurrence I opened was the capitalized game term.

---

## 3. Locked Zone

**Home definition:** `references/glossary.md:152` — "Territory or object subjected to Forced Resolution Lock." Mechanical origin: `designs/threadwork/threadwork_v30.md` §2.4 Locking, "Chronic consequences" table (lines 397–404): "Permanent (never reversed) | Substrate adapts. Mending Stability drift ceases. Permanent +1 Ob to adjacent operations. **This is how Locked Zones form.**" Plus the Mending Ob table's "Locked Zone border | Ob 8+ | 70+; requires Einhir framework" (line 470), and the Einhir-framework prerequisite note at line 161.

**Usage sweep:** 50 files. Canonical: `designs/threadwork/threadwork_v30.md` (home, consistent — lines 161, 397–412, 470), `designs/scene/conviction_track_v30.md`, `params/threadwork_superseded.md` (superseded), `designs/provincial/factions_personal_v30.md`, `designs/arcs/*` (narrative arc references — `arcs_24_27.md`, `arc_expansion_v30.md`, `gm_ref/arcs_46_55_resolved.md`), `canon/00_philosophical_foundations.md`. Remainder `tests/sim*`/`tests/stress*` (sampled `tests/sim/sim_thread_combat_extreme.md`, `tests/sim/arc_branch_simulation.md` — consistent).

**Divergence check:** No numeric or definitional contradiction found. The BG Mend table (see term 1 above) omits "Locked Zone border" as a Mend target entirely, which is consistent with the TTRPG rule that Locked Zone Mending is Einhir-framework-gated (Ob 8+) — a BG abstraction wouldn't handle a near-solo-impossible operation, so the omission reads as intentional rather than contradictory here.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:397-412,470` | CANONICAL DEFINITION | Named home | — |
| `references/glossary.md:152` | PULLED/REFERENCED | Terse description only | Agrees |
| `designs/scene/conviction_track_v30.md` | PULLED/REFERENCED | Cites Locked Zone as narrative/Conviction-trigger context | Agrees |
| `designs/arcs/*` (narrative) | PULLED/REFERENCED | Narrative usage, no independent mechanical restatement | Agrees |
| `params/threadwork_superseded.md` | HARDCODED DUPLICATE, superseded | Independent restatement, old naming | Superseded |

No incidental English usage found ("locked zone" is not a common English phrase; every hit was the game term).

---

## 4. Monstrous Incursion

**Home definition:** `references/glossary.md:153` — "Entity manifestation triggered by low Mending Stability or severe Dissolution failure." Mechanical trigger points, both in `designs/threadwork/threadwork_v30.md`: Dissolution Failure degree (line 430 — "Monstrous Incursion immediately"), and the MS-band table's Fractured row (line 821 — "Monstrous Incursion risk in all territories with existing Gaps").

**Usage sweep:** 163 files, but the term functions everywhere purely as a **narrative trigger flag** — I found no dedicated stat block, encounter table, or resolution mechanic anywhere in the corpus (checked `designs/world/calamity_radiation_v30.md`, `params/`, `designs/npcs/`). Canonical occurrences: `params/core.md`, `params/fieldwork.md`, `params/mass_combat.md`, `params/threadwork.md`, `designs/threadwork/threadwork_v30.md` (lines 430, 812, 821), `designs/scene/fieldwork_v30.md`, `designs/scene/combat_v30.md`, `designs/personal/knots_v30.md` (§7 N-way opposing ops), `designs/threadwork/thread_horizontal_integration_spec.md:122` ("Monstrous Incursion (spontaneous, radiation) | CV −1"), `designs/scene/conviction_track_v30.md:94` (identical CV −1 framing), `designs/arcs/arc_expansion_v30.md:525,717` (arc-specific consequences), `canon/editorial_ledger_archive.jsonl`. Remainder is `tests/`/`archives/` — sampled `designs/audit/2026-05-15-mb-comparative-audit/audit.md:1138`, consistent.

**Divergence check:** No divergence found — every occurrence I opened (canonical and sampled test/archive) treats it identically as an immediate/risk-based narrative trigger with no independent numeric spec. Worth flagging as its own finding per the audit's step 1 allowance ("no real canonical source exists is itself worth flagging"): the term has a trigger condition but **no resolution mechanic anywhere** — what a Monstrous Incursion actually *is* mechanically (combat stats, threat level, duration) is undefined in the corpus. This is a completeness gap, not a contradiction.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:430,821` | CANONICAL DEFINITION (trigger only) | Named home for the trigger condition; no resolution mechanic exists anywhere | — |
| `references/glossary.md:153` | PULLED/REFERENCED | One-line gloss | Agrees |
| `designs/threadwork/thread_horizontal_integration_spec.md:122`, `designs/scene/conviction_track_v30.md:94` | PULLED/REFERENCED | Both cite identical "CV −1" consequence, consistent with each other and importing the trigger, not redefining it | Agrees |
| `designs/arcs/arc_expansion_v30.md:525,717` | PULLED/REFERENCED (narrative) | Cites the trigger as an arc-specific consequence | Agrees |
| `params/threadwork_superseded.md` | HARDCODED DUPLICATE, superseded | Old TT-naming restatement | Superseded |

No incidental usage found.

---

## 5. The Rupture

**Home definition:** `references/glossary.md:154` — "Campaign-ending event when Mending Stability reaches 0." This is the **most significant divergence found in this batch** — see below.

**Usage sweep (canonical):** `params/core.md:101` ("MS floor: 0 (Rupture). MS ceiling: 100."), `params/factions/stats_1_7_scale.md:380`, `params/bg/core.md:81` ("Mending Stability (MS) | 72 | 0–100 | Rupture = shared loss"), `params/bg/clocks.md:18` ("MS 0 = Rupture (campaign ends, all factions lose)."), `params/bg/victory.md:61,139` ("Shared Loss Conditions. Per victory_v30.md §5. MS = 0 (Rupture)..."), `designs/provincial/victory_v30.md` (the actual §5, lines 555–647 — see contradiction below), `designs/architecture/complete_systems_reference.md:220` (explicitly `[SUPERSEDED-BY: GD-1]`, correctly self-flagged), `tools/observability/guide/EXECUTIVE_GUIDE.md:283`.

**Divergence check — a live, three-way contradiction:**

`designs/provincial/victory_v30.md` (the CURRENT.md-designated head for Victory) contains **directly contradictory statements about what MS=0 does, within the same file**:

> Line 557: **"No shared loss. No fade to black. Every crisis becomes a new chapter. The campaign continues."**
> Lines 559–569 (§5.1 "MS=0 → Post-Calamity Era"): MS=0 suspends faction acquisition for 3 seasons, doubles Mending Domain Echo, and is explicitly **recoverable** ("Recovery: MS restored to 20 within 10 seasons"). The only stated true terminal is a *separate* condition: "Second Calamity fires only after 10 seasons sustained at MS ≤ 5" (line 569).
> Lines 628–638 ("The Rupture Scene," ED-630): "When MS reaches 0 at Accounting, the Rupture Scene fires **as a narrative transition into the Post-Calamity Era**" — i.e., a phase change, not an ending.

versus, **later in the same document**:

> Line 647: **"MS 0 = Rupture = all factions lose."**

This second statement is not reconciled with lines 557/628–638 anywhere in the file — it reads as an un-updated holdover from an earlier design pass that ED-630's Rupture-Scene mechanic (Post-Calamity Era, recoverable) superseded in-place but did not fully overwrite.

This same stale "campaign ends / all lose" framing is then **independently restated as a hardcoded duplicate** in three other live params files that all cite victory_v30.md §5 as their source but reproduce the pre-ED-630 reading of it:
- `params/bg/clocks.md:18`: "MS 0 = Rupture (campaign ends, all factions lose)."
- `params/bg/victory.md:61,139`: "Shared Loss Conditions. Per victory_v30.md §5. MS = 0 (Rupture)..."
- `designs/provincial/peninsular_strain_v30.md` (which explicitly states at line 4 it "Supersedes... victory_v30.md §5 (shared loss retained with modifications)") instead reinforces the *corrected* reading: line 463 "**No shared loss. No fade to black.**" and line 467: "Post-Calamity Era | MS = 0 at Accounting | Substrate tears... Recovery: MS to 20 within 10 seasons."

An archived audit already found exactly this contradiction and recommended a fix that does not appear to have been applied to the live files: `archives/audit/2026-06-11-game-flow/game_flow_analysis_v1.md:198` — *"F5 · Shared-loss residue. params/bg/clocks.md ('MS 0 = Rupture, campaign ends, all factions lose') and complete_systems_reference Part 7 ('Shared loss: Rupture / Altonian Conquest / Anarchy') contradict the governing canon (victory §5 + peninsular_strain §6.4 'No shared loss'; campaign_architecture supersedes all shared-loss framing). A VictoryManager refit reading clocks.md would implement a deleted fail state."* and `archives/audit/2026-06-11-game-flow/game_flow_flat_spec_v1.md:351`: *"F5 (P2) | C3.4 / T.1 | clocks.md 'MS 0 = campaign ends' is dead text; VictoryManager must implement era transition, not fail state."* — flagged 2026-06-11, still unresolved in the live params files as of this sweep (2026-07-08).

The glossary's own entry (`references/glossary.md:154`, "Campaign-ending event when Mending Stability reaches 0") **restates the stale reading**, not the corrected peninsular_strain_v30.md/ED-630 one.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees with the corrected canon (peninsular_strain_v30 + victory_v30 §5.1/§628-638) today? |
|---|---|---|---|
| `designs/provincial/victory_v30.md:628-638` (Rupture Scene, ED-630) | CANONICAL DEFINITION | Named mechanic, cites its own ED | — (this IS the correction) |
| `designs/provincial/victory_v30.md:557,559-569` | CANONICAL DEFINITION (consistent w/ above) | Same file, same section | Agrees with itself |
| `designs/provincial/victory_v30.md:647` | HARDCODED DUPLICATE, internally contradictory | Independent restatement in the same file, no cross-ref to §5.1/ED-630 | **Diverges** — says "all factions lose," contradicting lines 557/628-638 two pages earlier |
| `designs/provincial/peninsular_strain_v30.md:463,467` | CANONICAL DEFINITION (declared supersessor of victory_v30 §5) | Explicit supersession statement at file header line 4 | Agrees (this is the corrected reading) |
| `params/bg/clocks.md:18` | HARDCODED DUPLICATE | Independent restatement, no import of ED-630/peninsular_strain | **Diverges** — stale "campaign ends" framing |
| `params/bg/victory.md:61,139` | HARDCODED DUPLICATE (mis-cited) | Cites "Per victory_v30.md §5" but reproduces the superseded reading of that section, not its current text | **Diverges** |
| `params/bg/core.md:81` | HARDCODED DUPLICATE | Terse restatement ("Rupture = shared loss") | **Diverges** |
| `params/core.md:101` | PULLED/REFERENCED (partial) | States only "MS floor: 0 (Rupture)" — names the event but does not claim campaign-ending | Neutral/agrees (doesn't make the false claim) |
| `references/glossary.md:154` | HARDCODED DUPLICATE | Independent one-line restatement | **Diverges** — "Campaign-ending event" is the stale reading |
| `designs/architecture/complete_systems_reference.md:220` | HARDCODED DUPLICATE, self-flagged superseded | Explicitly tagged `[SUPERSEDED-BY: GD-1]` inline | Known-stale, correctly marked |
| `archives/audit/2026-06-11-game-flow/*` | N/A — archived audit, not canon | Diagnostic-only; already identified this exact defect | Correctly diagnosed, unactioned |

This is the single highest-value finding in this batch: a live, CURRENT.md-designated canonical file (`victory_v30.md`) contradicts itself across ~90 lines, and three other live params files independently duplicate the stale side of that self-contradiction while citing the corrected file as their source.

---

## 6. Knot (bond-strain gauge, −5 to +5, ED-912)

**Home definition:** Per the batch prompt's own framing this is ED-912 (2026-06-28), synthesized canonically at `designs/personal/knots_v30.md` (a Pass-2g unified-canon doc that "does NOT supersede; it synthesizes" 9 fragments — its own words, line 326). The numeric home: `knots_v30.md:39-58` — Distant tier strain range −2…+5 (starts 0), Close tier −5…+5 (starts −2), rupture at +5 both tiers, −5 = Tempered (Close only, absorbs next rupture once). Break Composure damage = 4 (line 56). Disposition itself (separate from Knot strain) is a flat −5..+5, NOT Bonds-capped — restated at `designs/scene/fieldwork_v30.md:365` ("**Disposition range: −5 to +5.** Flat per NPC per PC... no Bonds ceiling") and `designs/npcs/npc_behavior_v30.md:364` editorial note.

**Usage sweep:** 96 files hit "ED-912"/"Knot Lifecycle" directly. Canonical: `references/glossary.md:155`, `sim/tests/test_knots_ed912.py`, `sim/personal/knots.py`, `params/core.md:147-149`, `params/fieldwork.md`, `params/threadwork.md`, `references/module_contracts.yaml`, `designs/scene/fieldwork_v30.md` (§5.6a/§5.6b, the actual first canonization site per ED-773), `designs/scene/derived_stats_v30.md`, `designs/personal/knots_v30.md` (synthesis), `designs/npcs/npc_relational_graph_v30.md`, `designs/scene/social_contest_v30.md` §4 Corroborate, `designs/articulation/articulation_layer_v30.md`, `canon/mechanics_index.yaml`, `canon/supersession_register.yaml`, `canon/editorial_ledger.jsonl`, `handoffs/HANDOFF_IN.md`, `handoffs/HANDOFF_WR.md`.

**Divergence check — confirmed stale duplicate in a live, non-archived file:**

`designs/architecture/complete_systems_reference.md` contains **two sections about the same mechanic that flatly contradict each other**, and only one is correctly labeled:

> Line 188 (Part 5, "Socializing," cites PP-632): **"Disposition −4 to floor(Bonds/2)+1."** — the OLD Bonds-capped, asymmetric range.
> Line 228 (Part 8, "Knots," explicitly cites ED-912): **"Knots (ED-912 strain model — supersedes PP-632 tier-cost)... Disposition itself is a flat −5..+5 (no Bonds ceiling)."**

Both statements are in the same document; Part 8 has been updated to ED-912 and explicitly says it supersedes PP-632, but Part 5 (nine sections earlier in the same file) still states the pre-ED-912 PP-632 formula as if live, with no cross-reference or strikethrough. The file's own supersession banner (line 2: "PARTIALLY SUPERSEDED (combat sections)") **only scopes to combat**, so this Disposition/Knot inconsistency is not covered by the banner and would not be caught by a reader trusting the banner's stated scope.

Separately, `knots_v30.md` §11 documents (and marks CLOSED) three prior canon-vs-canon contradictions it found during its own synthesis pass: TIER-DRIFT-001 (PP-632 3-tier Loose/Medium/Close vs ED-773 2-tier Distant/Close), COMPOSURE-DRIFT-001 (articulation §2.4 cited "5" vs fieldwork's "4" Composure), TRUNC-DRIFT-001 (a truncated table row). All three are stated RESOLVED 2026-06-28 (ED-841/842/843/912), with propagation into `knots_v30.md` §6.1/§6.2 completed 2026-07-07 per ED-FI-0003 — but the doc itself flags one **residual, still-open** item: §6.2's "mandatory −1 Coherence on rupture" rule is marked `⚠️ [UNVERIFIED post-ED-912]` (line 203) because no live citation for it could be found after PP-632 (its original source) was struck.

Also found: `designs/npcs/npc_behavior_v30.md:457` (§3.5.4, the ED-664 original source) still reads **"Disposition resets to −4 with the advisor"** — but both downstream synthesis docs that cite this exact rule state it was revised: `knots_v30.md:197` — *"the ED-912 betrayal-rupture value within the −5..+5 range, revised from the prior −4"* [i.e., now −3] — and `fieldwork_v30.md:519` states the identical revision. **The originating file (`npc_behavior_v30.md`) was never actually updated to −3; it still says −4, even though two other canonical docs both assert the −4→−3 revision was already propagated.**

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees with ED-912 today? |
|---|---|---|---|
| `designs/scene/fieldwork_v30.md:361-525` (§5.1, §5.6a/b) | CANONICAL DEFINITION | Original ED-773/ED-912 canonization site | — |
| `designs/personal/knots_v30.md` (whole doc) | CANONICAL DEFINITION (synthesis) | Explicit "does not supersede; it synthesizes" (line 326); binds to `sim/personal/knots.py` | Agrees; documents its own residual gap (§6.2 Coherence rule) |
| `references/glossary.md:155` | PULLED/REFERENCED | Terse gloss, no numeric range restated | Agrees |
| `params/core.md:147-149` | PULLED/REFERENCED | Cites ED-912 explicitly, restates the Bonds≥5/Knot-count formulas with citation | Agrees |
| `designs/architecture/complete_systems_reference.md:228` (Part 8) | PULLED/REFERENCED (correct) | Explicitly cites ED-912 and supersession of PP-632 | Agrees |
| `designs/architecture/complete_systems_reference.md:188` (Part 5) | HARDCODED DUPLICATE, stale | Independent restatement citing old PP-632, uncorrected, same file as the correct Part 8 text | **Diverges** — direct intra-document contradiction |
| `designs/npcs/npc_behavior_v30.md:457` | HARDCODED DUPLICATE, stale | Original rule text never propagated to reflect the −4→−3 revision two other docs claim was applied | **Diverges** — still says −4; two downstream docs assert this was fixed |
| `sim/personal/knots.py` | HARDCODED DUPLICATE, self-acknowledged stale | `knots_v30.md:359` states this "still runs the pre-ED-912 constants (C-TW-12)... tracked as Stratum-B work" | Known-diverges, explicitly tracked |
| `designs/articulation/articulation_layer_v30.md` §2.4 | PULLED/REFERENCED (corrected) | Composure value corrected to 4 per COMPOSURE-DRIFT-001 resolution | Agrees (post-fix) |

---

## 7. Knot Strain (the OPPOSING-OPERATIONS penalty)

**Home definition:** `designs/threadwork/threadwork_v30.md` §2.6, subsection "### Knot Strain" (lines 562–571):

| Scenario | Losing/Tied Practitioner | Winning Practitioner |
|---|---|---|
| Standard (Weave/Pull) | +1 Ob next Thread op this scene. 2 Composure. | 1 Composure. |
| FR (Lock/Dissolution) | +2 Ob. 4 Composure. If winner Dissolved: +1 Wound. | 2 Composure. |
| Both meet Ob (tie) | Both: +1 Ob, 2 Composure (FR: +2 Ob, 4 Composure). | N/A |
| Both fail | Both: 1 Composure. | N/A |

"Composure restores at scene change. Ob penalty expires after next Thread operation or at scene end." (line 571)

**Confirmed: this is a different mechanic from the Knot bond-strain gauge (term 6), sharing only the word "strain."** The threadwork_v30.md §2.6 "Knot Strain" is a **per-scene Ob/Composure penalty applied to practitioners in a contested Thread operation** (a combat-adjacent tactical debuff), scoped to "this scene" and expiring at scene end. The Knot (bond-strain) gauge in `knots_v30.md`/`fieldwork_v30.md` §5.6b is a **persistent −5..+5 relationship-wear counter on a specific NPC-PC bond**, accumulated across seasons, that determines Break/Rupture. `designs/personal/knots_v30.md` §5 and §7 makes the terminological overlap explicit and resolves it by treating the threadwork §2.6 event as one **contributor** to the persistent gauge, not as the same object: "Strain accrues as Knot history of use... Knot strain from contested Thread operations (threadwork §2.6) | +1 Ob next Thread op this scene + 2 Composure (per loser/tied)... **+1 strain to the Knot per opposing-operations event**" (`knots_v30.md:168`). So the threadwork §2.6 penalty is a *transient, scene-scoped Ob/Composure cost that ALSO, separately, adds +1 to the persistent bond-strain gauge* — two numbers fire from one trigger, under one name.

**Usage sweep:** `designs/threadwork/threadwork_v30.md:554-591` (home + FR-both-fail-scaling §, N-way §), `designs/personal/knots_v30.md:158-220` (§5 Strain Accumulation, §7 "Knots in Opposing Thread Operations" — a near-verbatim restatement of the threadwork table), `designs/audit/2026-07-08-crunch-cascade-cogload-legibility-audit/01_findings_threadwork.md`, `designs/audit/2026-07-07-unaddressed-areas-audit/01_workings/cluster_C-TW.md`, `params/threadwork.md`.

**Divergence check:** `knots_v30.md` §7 (lines 207-220) restates the exact threadwork §2.6 table verbatim with matching numbers (+1 Ob/2 Composure standard, +2 Ob/4 Composure FR) — this is a clean, correct restatement, explicitly marked "Per threadwork §2.6" (line 209), not an independent divergent copy. No numeric contradiction found between the two. The only genuine risk is conceptual, not numeric: a reader searching "Knot strain" without noticing the scene-scoped-Ob-penalty-vs-persistent-gauge distinction could conflate the two mechanics, which is exactly what the audit prompt flagged as a prior-audit finding — I confirm that finding is accurate and the two mechanics are real, distinct, and both currently live, correctly cross-linked via `knots_v30.md`'s explicit accounting of "the opposing-operations event" as one of several persistent-strain sources (not identical to it).

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:562-571` | CANONICAL DEFINITION | Named home for the scene-scoped Ob/Composure penalty | — |
| `designs/personal/knots_v30.md:207-220` (§7) | PULLED/REFERENCED | Explicitly "Per threadwork §2.6," numbers match exactly | Agrees |
| `designs/personal/knots_v30.md:168` (§5 accumulation table) | CANONICAL DEFINITION (for the *persistent-gauge* contribution) | This is the site that defines the "+1 strain to the Knot" conversion from the transient event — a genuinely separate fact from the Ob/Composure table | — |
| `designs/threadwork/threadwork_v30.md:591` (Sustained Opposition) | CANONICAL DEFINITION | "Knot strain Ob stacks with sequential penalty" — same scene-scoped mechanic | Agrees with itself |
| `designs/threadwork/threadwork_v30.md:595` (N-Way) | CANONICAL DEFINITION | "knot strain +2 Ob, 4 Composure" for 3+-way collapse | Consistent with the base table's FR row |

No divergence found in the numbers; the naming collision itself (two mechanics called "Knot strain") is real and confirmed, but is architecturally reconciled (one feeds the other) rather than contradictory.

---

## 8. Belief

**Home definition:** `references/glossary.md:156` — "Player-authored character conviction. Mechanical driver for Momentum and Character Points. Distinct from Inspiration." This is a thin stub. The fuller mechanical treatment is scattered and **explicitly incomplete**: `designs/scene/derived_stats_v30.md:216` (§5.3.4 table) cites its own source as "per character_histories Stage 4 + valoria_ttrpg_complete §10.2 — **TODO: full propagation pending**." I confirmed `valoria_ttrpg_complete.md` **does not exist anywhere in the working tree** (not in `deprecated/`, not in `archives/`) — the citation points at a file that is not present in this checkout. Belief-revision procedure lives in `designs/npcs/npc_behavior_v30.md` §3.2 (revision fires when a Contest produces a decisive outcome AND used the NPC's Resonant Style) — but that's NPC-Belief revision, a parallel but separate mechanic from PC-Belief.

**Usage sweep:** Canonical: `references/glossary.md:156`, `params/core.md:86` (Momentum "Gain: Overwhelming success OR Belief achieved"), `designs/world/character_histories_v30.md:22,30` (Stage 4 produces "starting Belief"), `designs/scene/social_contest_v30.md:562-563` (§9.5 "Beliefs Integration" — "Winning an exchange while arguing for a position aligned with the orator's stated Belief counts as a Belief achievement for Momentum"), `designs/scene/derived_stats_v30.md:209-221` (§5.3.4, cross-system distinction table), `designs/npcs/npc_behavior_v30.md` §3.1-3.2 (NPC Belief formation/revision), `designs/architecture/player_agency_v30.md` (conceptual framing only, no mechanical numbers), `references/mechanical_terms_index.md:115` (itself a pulled index citing "glossary §7").

**Divergence check — a live design doc gives specific CP-award numbers not found (or contradicted) anywhere else:**

`designs/arcs/emergent_scenarios.md:210-218` (SCENARIO 5, "BELIEF / INSPIRATION CHAIN") gives a concrete CP-award table:
> "BELIEF PURSUED in meaningful scene → +2 CP; BELIEF CHALLENGED by events → +2 CP; BELIEF GENUINELY REVISED in response to events → +4–5 CP... BELIEF COMPLETED → Option: convert to Inspiration at 1 point (no CP; conversion is the reward)."

This is the **only place in the corpus** I found specific CP-per-Belief-event numbers. No other canonical doc (`derived_stats_v30.md`, `glossary.md`, `player_agency_v30.md`) restates or contradicts these specific values — they exist in exactly one file, with no import mechanism tying them to a ledger PP/ED citation, and the file's own framing note (line 3) says "All values per compiled ruleset (Stage 1–12)" — a pre-v30-flatten naming convention, suggesting this table may predate the current generation and was never re-verified against it. This is a **HARDCODED DUPLICATE with no live cross-reference**, not confirmed-consistent with anything, and its own header hints it is a stale compiled-era artifact.

The same file (`emergent_scenarios.md:222-223`) also states "Inspiration = active at full value → Spend to add auto-successes (non-Thread) / 1 Inspiration point = 1 auto-success before roll" — this **directly contradicts** the canonical Inspiration-spend mechanic (see term 9 below: Ob −1, not an auto-success). This strengthens the assessment that `emergent_scenarios.md` is a stale, pre-reconciliation scenario map that was never updated when Inspiration's mechanic was formalized in `derived_stats_v30.md` §5.3 (ED-779, 2026-04-25).

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `references/glossary.md:156` | CANONICAL DEFINITION (only clean stub) | Named Part Seven entry | — |
| `designs/scene/derived_stats_v30.md:216` | UNCLEAR/NO CANONICAL SOURCE | Cites a non-existent file (`valoria_ttrpg_complete.md §10.2`) as one of its two sources, explicitly marked "TODO: full propagation pending" | Cannot be verified — the cited source doesn't exist in the tree |
| `designs/world/character_histories_v30.md:22,30` | PULLED/REFERENCED | Narrative-generation context (Stage 4 produces a Belief), no independent mechanical formula | Agrees (doesn't conflict) |
| `designs/scene/social_contest_v30.md:562-563` | PULLED/REFERENCED | Restates "Belief achievement → Momentum," consistent with `params/core.md:86` | Agrees |
| `params/core.md:86` | CANONICAL DEFINITION (for Momentum's Belief trigger specifically) | Named Momentum entry | — |
| `designs/arcs/emergent_scenarios.md:210-218` | HARDCODED DUPLICATE, likely stale | Independent CP-award numbers, no PP/ED citation, file self-describes as "compiled ruleset (Stage 1–12)" (pre-v30) | **Unverifiable / likely stale** — no other doc corroborates or contradicts these exact numbers |
| `designs/arcs/emergent_scenarios.md:222-223` | HARDCODED DUPLICATE, contradicts canon | Describes Inspiration-spend as "auto-success," contradicting `derived_stats_v30.md`/`fieldwork_v30.md`'s "Ob −1" | **Diverges** |
| `designs/npcs/npc_behavior_v30.md` §3.1-3.2 | CANONICAL DEFINITION (NPC-Belief, parallel mechanic) | Named home for NPC-side Belief revision | — (distinct from PC Belief, not a divergence) |

---

## 9. Inspiration

**Home definition:** The glossary stub (`references/glossary.md:157`, "Named focus that grants bonus dice... Distinct from Belief and History per ED-779") is actually a **downstream summary of a much fuller spec**: `designs/scene/derived_stats_v30.md` §5.3 (lines 164–221), explicitly propagated there per ED-779 (editorial note at line 221: "Closes propagation defect: canonical Inspiration spec existed only in deprecated/valoria_ttrpg_complete.md §10.4... Now consolidated in §5.3"). This is the real home: Formula = "Total Inspiration value ≤ Spirit attribute (Resolve cap)"; Range 0 to Spirit per focus, cumulative cap = Spirit; spend mechanic = **+1D genuine-pursuit bonus and Ob −1 when spent strategically** (line 166, cross-referencing `fieldwork_v30.md §2.2`); Recovery max 2 points/season; acquisition via two-scene+Spirit-check or "CP shortcut" (4 CP, line 188); loss/Grief-Scene mechanic (§5.3.3). `params/core.md:165` gives the derived cap: "Resolve | Spirit | 1–7 | Maximum total Inspiration value." `params/fieldwork.md:227-228` gives the spend rule: "Inspiration Spend / 1 Inspiration before rolling → Ob −1 (min 1)."

**Usage sweep:** Canonical: `designs/scene/derived_stats_v30.md:164-221` (home), `params/core.md:165`, `params/fieldwork.md:227-228`, `params/scale_transitions.md:54` ("Second scope action in same round: +1 Inspiration spend"), `references/mechanical_terms_index.md:116` (pulled, cites "glossary §7"), `references/glossary.md:157`.

**Divergence check:** As noted under Belief (term 8), `designs/arcs/emergent_scenarios.md:222-227` gives Inspiration a **completely different spend mechanic** — "1 Inspiration point = 1 auto-success before roll" plus an "INSPIRATION ATTACK (Debate, Character Style) / Defender net ≤ 0 → Inspiration −1" combat-style mechanic that appears nowhere in `derived_stats_v30.md` or `fieldwork_v30.md`. This is a direct, quotable contradiction:

> `derived_stats_v30.md:166`: "Inspirations grant +1D bonuses to actions taken in genuine pursuit of the focus and **reduce Ob by 1** when spent strategically (per fieldwork_v30 §2.2)."
> `params/fieldwork.md:228`: "1 Inspiration before rolling → **Ob −1** (min 1)."
> vs.
> `designs/arcs/emergent_scenarios.md:222-223`: "Inspiration = active at full value → Spend to add **auto-successes** (non-Thread) / 1 Inspiration point = **1 auto-success** before roll."

These describe mutually exclusive resolution effects (Ob reduction vs. auto-success injection) for spending the identical resource. `emergent_scenarios.md` is dated to the pre-v30 "Stage 1–12" convention per its own framing note and was almost certainly never reconciled after ED-779 (2026-04-25) consolidated the mechanic into `derived_stats_v30.md` §5.3.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/scene/derived_stats_v30.md:164-221` | CANONICAL DEFINITION | ED-779 named propagation target | — |
| `params/core.md:165` | PULLED/REFERENCED | Cites "Resolve = Spirit, max Inspiration" without restating the full mechanic | Agrees |
| `params/fieldwork.md:227-228` | CANONICAL DEFINITION (co-equal, for the spend-effect specifically) | Original site cited by derived_stats §5.3 itself | Agrees with derived_stats (same rule, same number) |
| `references/glossary.md:157` | PULLED/REFERENCED | Terse summary | Agrees |
| `designs/arcs/emergent_scenarios.md:222-227` | HARDCODED DUPLICATE, contradicts canon | Independent, incompatible spend mechanic (auto-success vs Ob−1), no citation to derived_stats/fieldwork | **Diverges** — direct mechanical contradiction |

---

## 10. History (skill-equivalent, not the English word)

**Home definition:** `references/glossary.md:158` — "Skill-equivalent. Specific experiential knowledge that grants bonus dice. **Cap = Memory score.**" Mechanical home: `designs/world/character_histories_v30.md` (the Lifepath system) + `params/core.md:151` — **"Recall (Rec): Knowledge, experience, retention. Sets the per-History point cap — a History can never hold more points than the character's Recall score."**

**Divergence check — a stale attribute name still live in the glossary and at least one other design doc:**

The glossary's own History entry (`references/glossary.md:158`) says the cap is "Memory score." But **no attribute called "Memory" exists anywhere in the current 7-, 9-, or 10-attribute rosters I found** (glossary Part One's 7-attribute list, `references/descriptor_registry.yaml`'s 9-attribute list, or `params/core.md:140-145`'s 10-attribute list — Physical/Mental/Social/Metaphysical groups: Agility, Endurance, Strength / Cognition, **Recall**, Focus / Attunement, Bonds, Charisma / Spirit). The attribute that actually governs the History cap, per both `params/core.md:151` and `designs/world/character_histories_v30.md:26-27` ("Recall as skill gatekeeper... Learning speed: floor(Recall/2) bonus dice on all spark checks"), is unambiguously **Recall**, not "Memory."

"Memory score" as the History cap also appears, independently, in `designs/arcs/emergent_scenarios.md:242` — "History +1: 3 CP (capped at Memory score total)" — the same stale label, in a different file, suggesting "Memory" was likely a pre-rename label for what the corpus now calls "Recall" and the rename was never propagated into either the glossary or this arcs doc. (`tools/observability/DECISIONS.md:53` records an unrelated but adjacent rename: a Debate *Genre* option once also called "Memory" was renamed to "Precedent" specifically "to avoid collision with Recall" — confirming "Recall" was already the live attribute name at that point, and reinforcing that "Memory" surviving as the History-cap label in the glossary/arcs doc is leftover drift, not a second legitimate attribute.)

**Usage sweep:** Canonical: `references/glossary.md:158`, `params/core.md:143,151,159,161,247,252` (all consistently "Recall," never "Memory," except the History-cap gloss doesn't appear in params/core.md at all — core.md never uses the word "Memory" for this purpose), `designs/world/character_histories_v30.md` (dozens of consistent "Recall" uses, e.g. lines 26-27, 33, 35), `designs/scene/derived_stats_v30.md` (Recall-based Concentration formula, consistent), `designs/arcs/emergent_scenarios.md:242` (the one other "Memory score" occurrence).

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees with the live attribute (Recall)? |
|---|---|---|---|
| `params/core.md:151` | CANONICAL DEFINITION | Names Recall explicitly as the History-cap-setting attribute | — |
| `designs/world/character_histories_v30.md:26-27` | CANONICAL DEFINITION (co-equal, mechanical usage) | "Recall as skill gatekeeper" | Agrees with params/core.md |
| `references/glossary.md:158` | HARDCODED DUPLICATE, stale | Independently states "Cap = Memory score" — no attribute named Memory exists | **Diverges** — stale/renamed term never fixed in the glossary |
| `designs/arcs/emergent_scenarios.md:242` | HARDCODED DUPLICATE, stale | Same "Memory score" phrasing, independent of the glossary | **Diverges** — same stale term surfacing a second time |
| `references/mechanical_terms_index.md` | PULLED/REFERENCED | Cites "glossary §7" for History, inheriting the stale phrasing by reference rather than independent restatement | Inherits the glossary's error by citation, not duplication |

Incidental-usage note: "History" as the ordinary English word (e.g., "canonical timeline," "historical," `canon/03_canonical_timeline.md`) is extremely common in this corpus and was excluded — I only counted capitalized, skill-context uses (adjacent to Recall, Spark, dice-bonus language, or Stage/Vocation framing).

---

## 11. Character Point / CP

**Home definition:** `references/glossary.md:159` — "Advancement currency earned through Beliefs and session milestones. **CP refers to Character Points only** (ED-136); see PART TWELVE collision entry." Part Twelve (`glossary.md:242`): "CP | Character Points (advancement currency) | ~~Combat Power~~ (renamed Power — PP-232) | CP = Character Points only [ED-136]. Use 'Power' for the unit offensive stat."

**Usage sweep:** The full phrase "Character Point[s]" is rare in `designs/` — only 2 hits: `designs/provincial/strategic_layer_v30.md:752-755` (§9.12 "CP Awards from Board Game Successes," ED-874-adjacent G-089) and `designs/audit/2026-04-30-architecture-session/14_significance_canonical_integration.md`. The bare abbreviation "CP" appears in 22 `designs/` files, mostly as the Character-Points advancement currency (`designs/scene/derived_stats_v30.md:188,190,216`, `designs/provincial/factions_personal_v30.md:428`, `designs/architecture/hybrid_gaps_v30.md:97`, `_infill.md:52`) — consistent with the glossary.

**Divergence check — a live, non-archived combat doc still uses the deprecated CP=Combat Power meaning:**

`designs/scene/combat_design_v1.md:354` (Unit Stat Block): **"Power (CP): Dice pool ceiling."** This restates "CP" as the abbreviation for the unit offensive stat "Power" — exactly the deprecated usage the glossary's Part Twelve collision table exists to warn against ("CP = Character Points only [ED-136]. Use 'Power' for the unit offensive stat"). The file's own header (line 4) says "Status: WORKING DESIGN — not compiled," and it predates the PP-232 rename it half-applies (it already renamed "Strength→Size" is absent — actually it still uses "Strength" for headcount at line 353, one PP-232 rename behind `combat_v30.md`, which already reads "Size" for the same stat). This file sits in `designs/scene/` (not moved to `archives/`/`deprecated/`), so it is discoverable by a plain grep for "CP" without any banner warning a reader that its terminology is pre-PP-232/pre-ED-136. The current combat doc, `designs/scene/combat_v30.md` (itself now superseded again by `combat_engine_v1/` per CURRENT.md), correctly drops the "(CP)" parenthetical: line ~389 reads "Power (Power): Dice pool ceiling" — awkward but at least free of the CP collision.

By contrast, `designs/provincial/mass_battle_v30.md:7` correctly documents the rename as history, not live usage: "PP-232 (renames: Strength→Size, **CP→Power**, Cohesion→Discipline, CR→Command)" — this is a changelog note, not a live re-use of "CP" for Power, so it is not itself a divergence.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees with ED-136 (CP=Character Points only)? |
|---|---|---|---|
| `references/glossary.md:159,242` | CANONICAL DEFINITION | Named home + collision-table ruling | — |
| `designs/scene/derived_stats_v30.md:188,190,216` | PULLED/REFERENCED | Uses "CP" consistently as Character Points, ties into the Inspiration-acquisition mechanic | Agrees |
| `designs/provincial/strategic_layer_v30.md:752-755` | CANONICAL DEFINITION (co-equal, BG-bridge specific) | Named §9.12, defines the BG→CP bridge rule | Agrees |
| `designs/provincial/mass_battle_v30.md:7` | PULLED/REFERENCED (historical note) | Changelog citing the PP-232 rename, not a live re-use | Agrees (correctly documents the rename, doesn't violate it) |
| `designs/scene/combat_v30.md` (~389) | PULLED/REFERENCED (corrected) | Drops the "(CP)" label post-rename | Agrees |
| `designs/scene/combat_design_v1.md:354` | HARDCODED DUPLICATE, stale/deprecated meaning | Independent restatement of "CP" as Combat-Power abbreviation, in a still-present (non-archived) file | **Diverges** — exactly the collision ED-136 exists to forbid |

---

## 12. Disposition (NPC-relationship attitude state)

**Home definition:** The glossary (`references/glossary.md:160`) names `designs/npcs/npc_behavior_v30.md` as canonical with "no separate first-class doc" — but I confirmed the actual numeric range/mechanical spec (§5.1 "Disposition Track") **lives in `designs/scene/fieldwork_v30.md:361-540`, not in npc_behavior_v30.md**, which only *uses* Disposition values (Stance Triangles, arc conditions) without defining its range anywhere in the ~1259-line file I reviewed. `fieldwork_v30.md:365`: **"Disposition range: −5 to +5. Flat per NPC per PC — the same fixed swing for every character; no Bonds ceiling. Asymmetric."** (ED-912/ED-841, editorial note at line 364).

**Usage sweep:** Extremely broad — 163 files hit "Disposition" project-wide (via the earlier "Domain Action" query's overlap, "Disposition" itself independently returns comparable volume). Canonical: `designs/scene/fieldwork_v30.md` (home, §5.1-§5.7, dozens of consistent uses), `designs/npcs/npc_behavior_v30.md` (dozens of Stance Triangle uses, consistent with the −5..+5 range — e.g. line 359 "−1," line 431 "−4 with principal," line 457 "−4" [flagged below]), `designs/personal/knots_v30.md`, `params/core.md:147-149`, `designs/architecture/scale_transitions_v30.md` (Sufficient Scope §7 "Reaching Disposition +4/+5"), `designs/architecture/complete_systems_reference.md` (both sites, contradictory — see below), `designs/scene/social_contest_v30.md`, `canon/mechanics_index.yaml`.

**Divergence check — two distinct, serious findings:**

**(a) A genuine cross-domain term collision, confirmed per the prompt's instruction to cross-check against Batch 6's combat disposition.** `designs/scene/combat_v30.md:406-408` and `designs/scene/combat_design_v1.md:364-366` (PP-218/PP-086, mass-combat personal-scale abstraction) define an entirely unrelated mechanic also named "Disposition":

> `combat_v30.md:406`: "Damage = max(0, net successes − Ob) + **disposition_modifier**. (PP-218 clarification)"
> `combat_v30.md:408`: "**Disposition modifiers: Offensive +2 flat; Defensive +4 flat.**"

This is a flat tactical-stance bonus (Offensive/Defensive posture selection in mass-combat abstraction) — completely unrelated to the NPC-attitude gauge, sharing only the bare word "Disposition." Both meanings are simultaneously live in the corpus with no disambiguation note in either file pointing at the other. This confirms the batch prompt's suspicion of a collision with "Batch 6's combat disp."

**(b) The same internal self-contradiction already documented under Knot (term 6) recurs here, because Disposition's range is the shared fact both sections describe:** `designs/architecture/complete_systems_reference.md:188` ("Disposition −4 to floor(Bonds/2)+1," PP-632, uncorrected) directly contradicts `complete_systems_reference.md:228` ("Disposition itself is a flat −5..+5, no Bonds ceiling," ED-912, explicitly superseding PP-632) — same document, ~40 lines apart, only one side updated.

**(c) A stale numeric value in the rule's own originating file:** `designs/npcs/npc_behavior_v30.md:457` (§3.5.4, the ED-664 source text) still reads "Disposition resets to **−4** with the advisor," while both `designs/personal/knots_v30.md:197` and `designs/scene/fieldwork_v30.md:519` independently assert this exact value was revised under ED-912 to **−3** ("the ED-912 betrayal-rupture value within the −5..+5 range, revised from the prior −4"). The originating file was never actually edited to match the revision two other canonical docs believe already happened.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/scene/fieldwork_v30.md:361-365` | CANONICAL DEFINITION | §5.1 Disposition Track, the actual numeric home (glossary misattributes this to npc_behavior_v30.md) | — |
| `designs/npcs/npc_behavior_v30.md` (Stance Triangles, general use) | PULLED/REFERENCED | Uses Disposition values without restating the range formula | Agrees |
| `references/glossary.md:160` | PULLED/REFERENCED (mis-citation) | Names npc_behavior_v30.md as canonical, but the range itself lives in fieldwork_v30.md | Citation is imprecise but not numerically wrong |
| `params/core.md:147` | PULLED/REFERENCED | Cites ED-912 explicitly | Agrees |
| `designs/architecture/complete_systems_reference.md:228` | PULLED/REFERENCED (correct) | Explicit ED-912 citation, correct value | Agrees |
| `designs/architecture/complete_systems_reference.md:188` | HARDCODED DUPLICATE, stale | Independent PP-632 restatement, same file as the corrected Part 8 text, no cross-reference | **Diverges** |
| `designs/npcs/npc_behavior_v30.md:457` | HARDCODED DUPLICATE, stale | Original rule text, unrevised, contradicted by two downstream docs that both claim it was fixed | **Diverges** |
| `designs/scene/combat_v30.md:406-408`, `combat_design_v1.md:364-366` | UNCLEAR / different mechanic entirely (name collision) | "Disposition" here names a combat-stance flat bonus (PP-218), unrelated to the NPC-attitude gauge | Not a numeric divergence — a term collision; both meanings are live with no disambiguation |

---

## 13. Domain Action

**Home definition:** Glossary (`references/glossary.md:161`) explicitly states "no separate first-class doc," naming `designs/architecture/scale_transitions_v30.md` + `designs/provincial/faction_layer_v30.md` as canonical. The *procedural* definition (what a Domain Action is, as a cross-scale unit) lives in `scale_transitions_v30.md` §3.2/§3.4/§3.5 (Personal→Faction, Scene→Faction, Thread→Faction handoffs) and §5 (Domain Echo, its output). The *resolution mechanic* (what number crunching actually happens) has a genuine, single, dated canonical home: **`params/factions/stats_1_7_scale.md:56-97`, "Domain Action Resolution (deterministic+stochastic) — CANONICAL (ED-874, ratified 2026-05-31)."** This explicitly supersedes an older bare-stat dice method retained at the same file lines 99-105 under a "SUPERSEDED" banner: "Ob = floor(relevant stat / 2) + 1" — kept only as "legacy/Zoom-In reference."

**Usage sweep:** 163 files. Canonical: `params/factions/stats_1_7_scale.md` (home resolver, ED-874), `designs/provincial/faction_layer_v30.md` (dozens of specific Domain Actions — Assert, Claim Masterless, Reconstitute, Resistance check — lines 45, 192, 213, 222, 294, 296, 368, 382), `designs/architecture/scale_transitions_v30.md` (§3.2-§3.9, §5, §9), `designs/provincial/factions_personal_v30.md:40,99,428`, `params/bg/ministry.md:41`, `params/bg/parliament.md:61`, `params/bg/ed_resolutions.md:16`, `params/factions/riskbreakers_identity.md:236`, `canon/patch_register_index.md:78`. Remainder is dominated by `tests/stress/emergent_arc_*` and `tests/emergent_arc_skeleton_test_*` narrative-scenario files (30+ occurrences, sampled `tests/stress/thread/threadwork_stress_test_batch5.md:219-227`, `tests/stress/emergent_arc_2026-04-17_batch2.md:170,178,948,1017` — all pre-ED-874, using the old bare-stat-vs-Ob framing, expected since these are historical test-batch narrative logs, not currency-bearing).

**Divergence check:**

The ED-874 resolver migration (2026-05-31) was applied **inconsistently within the single live doc `faction_layer_v30.md`**: most Domain Action citations were updated to the new "M = stat − difficulty (legacy: Ob N)" dual-notation form (lines 192, 222, 296 all show this pattern), but line 213 — "Any faction may Claim Masterless units via Domain Action (**Military Ob 2**; Success: units transfer to claiming faction at current strength; Failure: units disband)" — was **not** updated to the resolver notation and presents the pre-ED-874 bare "Ob 2" framing as if still current, with no "(legacy: ...)" qualifier the way its sibling lines do. This is a small but real inconsistency in currency-of-update within a single canonical file.

Separately, `tests/stress/thread/threadwork_stress_test_batch5.md:227` makes an explicit design observation still true today: **"The Domain Action system has no Thread interface... direct Thread targeting of an in-progress Domain Action is undefined."** — not itself a numeric divergence, but a genuine documented gap the audit should note as "no canonical source exists" for that specific cross-system interaction.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees with ED-874 today? |
|---|---|---|---|
| `params/factions/stats_1_7_scale.md:56-97` | CANONICAL DEFINITION | Named resolver, ED-874, explicitly supersedes the legacy method in the same file | — |
| `params/factions/stats_1_7_scale.md:99-105` | CANONICAL DEFINITION (retained, explicitly SUPERSEDED banner) | Marked "[SUPERSEDED 2026-05-31, ED-874]... retained only as legacy reference" | Correctly self-flagged, not a hidden divergence |
| `designs/provincial/faction_layer_v30.md:192,222,296` | PULLED/REFERENCED | Explicitly cites "resolver (params/factions/stats_1_7_scale.md §Domain Action Resolution)" with dual legacy/new notation | Agrees |
| `designs/provincial/faction_layer_v30.md:213` | HARDCODED DUPLICATE, un-migrated | Bare "Ob 2" framing, no resolver citation, inconsistent with sibling lines in the same file | **Diverges from the file's own updated convention** — not wrong per se (Ob 2 → difficulty 2 is a valid legacy mapping) but presented without the resolver citation its neighbors all have |
| `designs/architecture/scale_transitions_v30.md` §3.2-§3.9, §5 | CANONICAL DEFINITION (procedural/cross-scale layer) | Named home for the handoff mechanism and Domain Echo output | Agrees; doesn't need updating since the resolver's output ladder (Failure/Partial/Success/Overwhelming) is explicitly unchanged by ED-874 (stats_1_7_scale.md:86: "Output is unchanged") |
| `tests/stress/emergent_arc_*` (~15 files) | PULLED/REFERENCED (narrative, pre-ED-874) | Bare-stat "Ob N" framing throughout | Expected/historical drift — pre-dates ED-874, non-canonical test corpus |

---

## 14. Domain Echo

**Home definition:** `designs/architecture/scale_transitions_v30.md` §5 (lines 173-236): §5.1 Trigger ("One Domain Echo maximum per scene per faction (PP-329)"), §5.2 Amount ("Overwhelming ±2 / Success ±1 / Partial narrative-only / Failure −1... Cap: ±2 per stat per Echo. (ED-071 resolved by PP-329: one Echo/scene/faction prevents compounding)"), §5.4 Debate→Domain Echo, §5.5 Accord Domain Echo, §5.6 Thread Domain Echo. Its own §5.6 flags an explicit known gap: "no season-level aggregate ceiling — a faction generating many qualifying scenes in one season... can stack Echoes without limit" (ED-IN-0025, 2026-07-07).

**Usage sweep:** Canonical: `designs/architecture/scale_transitions_v30.md` (home, §3.4, §5 whole, §9, §12.4), `params/scale_transitions.md:29-46` (co-filed params doc — see contradiction below), `designs/provincial/faction_layer_v30.md`, `designs/provincial/strategic_layer_v30.md`, `designs/scene/combat_v30.md` (Domain Echo from combat-scene outcomes), `designs/architecture/hybrid_gaps_v30.md:138`, `designs/architecture/videogame_mode_spec.md`, `designs/npcs/npc_behavior_v30.md`, `references/glossary.md:162` (terse: "Faction-level consequence triggered by decisive Debate outcomes" — note this describes only the §5.4 Debate case, not the full §5.1-§5.6 scope), `canon/patch_register_index.md`, `tools/observability/DECISIONS.md:557`.

**Divergence check — a genuine, internally self-contradictory params file, and a cross-file cap-rule mismatch:**

`params/scale_transitions.md` is the co-filed params doc for `scale_transitions_v30.md`. Its own header (line 1) reads: `<!-- version: v0.14-ST2-R1 ... last_updated: 2026-04-03 --><!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->` — the file explicitly warns it may be stale and self-demands a version check before use, which nobody appears to have acted on (the corpus is at "Generation v40" per CURRENT.md).

Within this one file, the Domain Echo cap is stated **two contradictory ways**:
> Line 34: **"Cap: ±2 per scene."** [PROVISIONAL — pre-ledger, accepted as canonical per 2026-04-26 audit]
> Line 42: **"Multiple Domain Echoes (same scene): Fire in the order they occurred... cap resets per stat per Echo (not per scene total)."**

Line 34 says the cap is scoped "per scene" (implying a scene-wide total); line 42 explicitly says the opposite — "not per scene total," but per-stat-per-Echo. These cannot both be true as written.

This params file's cap language also mismatches the current design-doc head: `scale_transitions_v30.md:187` states "Cap: ±2 per stat per Echo. (ED-071 resolved by PP-329: **one Echo/scene/faction** prevents compounding)" — i.e., the real mechanism preventing runaway stacking is the *count* restriction (one Echo per scene per faction, PP-329), with the ±2 being a per-stat-per-Echo ceiling, not an independent "per scene" cap. `params/scale_transitions.md` predates PP-329 (its "known gap" footnote, added later on 2026-07-07 per ED-IN-0025, is the only part of the file that has been touched since 2026-04-03) and never absorbed that resolution — its body text still argues with itself about which cap model is right.

Additionally, `params/scale_transitions.md:74-81` ("Domain Echo — Debate Outcome Mapping") states the Debate→Domain Echo target stat as **"+1 in contested axis (L procedural / PS populist)"** — using stat abbreviations "L" and "PS" that do not appear in any current attribute/faction-stat table I found (glossary Part Four's faction stats are Mandate/Influence/Wealth/Military/Intel/Stability/Standing — no "L" or "PS"). The current design-doc head instead specifies concretely: `scale_transitions_v30.md:197` "Winner faction: **+1 Mandate**. Loser faction: **−1 Mandate** if they held institutional authority." This is a clear, quotable numeric/target divergence between the params file and the design-doc head it's supposed to accompany — the params file appears to predate the current Mandate-based Debate→Echo rule and never got updated past whatever "L"/"PS" scheme preceded it.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees with the current design-doc head today? |
|---|---|---|---|
| `designs/architecture/scale_transitions_v30.md:173-236` | CANONICAL DEFINITION | Named home, cites PP-329/ED-071 | — |
| `references/glossary.md:162` | PULLED/REFERENCED (incomplete scope) | Describes only the Debate-triggered case, omits §5.5/§5.6 (Accord/Thread Echo) | Not wrong, just partial |
| `designs/provincial/faction_layer_v30.md`, `strategic_layer_v30.md` | PULLED/REFERENCED | Use Domain Echo consequences without restating the cap formula independently | Agrees |
| `params/scale_transitions.md:34` | HARDCODED DUPLICATE, stale/self-contradictory | Independent cap restatement ("±2 per scene"), file self-flagged v0.14/stale | **Diverges internally (contradicts its own line 42) and from the current head's "per stat per Echo + one-Echo-per-scene" model** |
| `params/scale_transitions.md:42` | HARDCODED DUPLICATE, partially aligned | States cap is "not per scene total" — closer to current canon but still not identical wording/mechanism (doesn't mention the PP-329 one-Echo-per-scene-per-faction count-limit as the actual compounding guard) | Partially agrees, poorly reconciled with its own line 34 |
| `params/scale_transitions.md:74-81` | HARDCODED DUPLICATE, stale | Independent Debate→Echo target-stat claim ("L"/"PS" axes), not found in any current stat roster | **Diverges** — contradicts `scale_transitions_v30.md:197`'s "Mandate" target |
| `designs/architecture/scale_transitions_v30.md:235` / `params/scale_transitions.md:44` (the ED-IN-0025 "known gap" notes) | PULLED/REFERENCED (mutually consistent) | Both independently, but identically, flag the no-season-cap gap — the params file's note is dated 2026-07-07, clearly a later patch bolted onto an otherwise 2026-04-03 file | Agrees with each other (this specific note was kept in sync even though the surrounding body text was not) |

---

## 15. Grievance Marker

**Home definition:** `references/glossary.md:163` — "Token placed on a faction after hostile covert action. Originally scoped to Niflhel hostile action; Niflhel-as-faction struck per ED-764, scope extended to any covert/hostile action." No dedicated mechanical spec doc exists (confirmed: no hits outside the glossary and two narrative arc files).

**Usage sweep (exhaustive — only 3 occurrences total in the entire corpus):**
- `references/glossary.md:163` (home)
- `designs/arcs/gm_ref/arcs_10_18.md:292` — "Military suppression: CV +0 but Grievance Marker (persists 4 seasons; RM Community Weaving −1 Ob while present)."
- `designs/arcs/arcs_31_35.md:37,79` — "Assassination fails → Operative exposed → intelligence broker Intel −1, **Grievance Marker**" (no duration or effect given).

**Divergence check:** The two narrative usages are consistent with the post-ED-764 widened scope (neither is Niflhel-specific; one is a Church/RM Einhir-suppression consequence, the other an "intelligence broker" — the post-Niflhel-dissolution successor mode — covert-action consequence). However, they are **not mechanically consistent with each other**: `arcs_10_18.md` gives the marker an explicit duration and effect ("persists 4 seasons; RM Community Weaving −1 Ob while present"), while `arcs_31_35.md` applies "Grievance Marker" with **no stated duration or mechanical effect at all**. Since there is no dedicated spec doc defining a single canonical duration/effect for a Grievance Marker, each narrative author appears to have improvised their own instance-specific consequence — consistent with the glossary's implicit admission that this term has "no separate first-class doc" (it doesn't even say that explicitly the way Disposition/Domain Action entries do, but the absence of any doc confirms it).

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `references/glossary.md:163` | CANONICAL DEFINITION (the only clean definition site; no mechanical spec exists) | Named Part Seven entry | — |
| `designs/arcs/gm_ref/arcs_10_18.md:292` | UNCLEAR / NO CANONICAL SOURCE for the specific numbers used | Independently invents "persists 4 seasons; −1 Ob" with no citation to a governing spec (because none exists) | Cannot be checked against a formula — there is none |
| `designs/arcs/arcs_31_35.md:37,79` | UNCLEAR / NO CANONICAL SOURCE | Applies the marker with zero stated mechanical effect, inconsistent in specificity with the other usage | Cannot be reconciled with `arcs_10_18.md`'s duration — no shared source to arbitrate |

This term is a clean example of the audit's step-1 caveat: no real single canonical source exists beyond the glossary's one-line gloss, and the two narrative instantiations are not mutually consistent because there is nothing binding them together.

---

## 16. Co-Movement Card

**Home definition:** `designs/threadwork/threadwork_v30.md` §7.1 (lines 916-943) — "### Revised Co-Movement Card Deck (18 cards)." "Cards 1–15: retained (all Thread Tension references become Mending Stability, inverted). Cards 16–18 added" (16. Substrate Settling, 17. Scar Trace, 18. Residue Condensation). The actual card list itself (1-15) lives at `threadwork_v30.md:751` per the index ("Co-Movement Cards 1–15 (ED-577 — canonical card list)"). Trigger: BG-mode "Mend" order success/failure draws a card (line 925); more broadly, any BG-scale ("strategic phase") Thread order draws a card, as the BG-mode equivalent of TTRPG's personal Version-C co-movement auto-effects.

**Usage sweep:** Canonical, all internally consistent on "18 cards": `designs/threadwork/threadwork_v30.md:82,751,925,936,969`, `designs/threadwork/threadwork_v30_index.md:70,88,157,175`, `designs/threadwork/threadwork_v30_infill.md:177`, `designs/threadwork/threadwork_v25_historical.md:76,560,910,921,962` (predecessor, same count), `designs/threadwork/threadwork_v25_historical_index.md:87,173`, `designs/architecture/hybrid_gaps_v30.md:138`, `designs/architecture/hybrid_gaps_v30_infill.md:21`, `designs/architecture/videogame_mode_spec.md:78,152`, `designs/architecture/campaign_modes_v30.md:157-158`, `designs/provincial/strategic_layer_v30.md:691`, `designs/provincial/strategic_layer_v30_infill.md:70,155`, `designs/provincial/factions_personal_v30.md:333`, `designs/scene/fieldwork_v30.md:789`, `designs/scene/fieldwork_summary.md:15`, `designs/ui/valoria_ui_ux_v4.md:1650`, `designs/videogame/godot_architecture_specification.md:894`, `designs/arcs/emergent_campaign_arcs.md:113`, `designs/audit/valoria_workplan_final_index.md:31` (ED-577-01/02/03/04, flagged "HARD DEPENDENCY FOR PHASE 4"), `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_threadwork.md:34,208` and its companion `ners_verdict_threadwork.md:152` (both PASS the mechanic as "discrete trigger, bounded variance").

**Divergence check:** No numeric or definitional contradiction found — every one of the ~20 canonical-directory citations I checked consistently states "18 cards," consistently distinguishes "Personal: Version C auto-effects" vs "Strategic: Co-Movement Card draw," and consistently cites ED-577 for the canonical card list. This is the healthiest term in the batch: a clean PULLED/REFERENCED chain throughout, confirming the healthy case exists alongside the more numerous divergent ones documented above.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:751,916-943` | CANONICAL DEFINITION | Named home, ED-577 card list + the 18-card deck spec | — |
| `designs/threadwork/threadwork_v30_index.md:70,88,157,175` | PULLED/REFERENCED | Index/co-file pointing at the same ED-577 list, no independent numbers | Agrees |
| `designs/architecture/hybrid_gaps_v30.md/_infill.md`, `videogame_mode_spec.md`, `campaign_modes_v30.md` | PULLED/REFERENCED | All cite "18 cards" / "Co-Movement Card" consistently, cross-referencing threadwork_v30 §7.1/§3.2 explicitly (e.g. `videogame_mode_spec.md:78`: "threadwork_v30 §7.1, §3.2") | Agrees |
| `designs/provincial/strategic_layer_v30.md/_infill.md`, `factions_personal_v30.md` | PULLED/REFERENCED | BG-side consumption of the mechanic, no independent restatement | Agrees |
| `designs/scene/fieldwork_v30.md:789`, `fieldwork_summary.md:15` | PULLED/REFERENCED | Cross-mode comparison table citing the same trigger | Agrees |
| `designs/threadwork/threadwork_v25_historical.md` (predecessor) | HARDCODED DUPLICATE, historical | Same 18-card count under old RS naming | Expected supersession drift, not live-canon-relevant |
| `designs/audit/2026-05-28-resolution-diagnostic/*` | PULLED/REFERENCED (diagnostic) | Independently verifies the mechanic is "discrete trigger, bounded" — a NERS audit PASS, not a redefinition | Agrees |

---

## 17. Zoom In

**Home definition:** `designs/architecture/scale_transitions_v30.md` §4.1 (lines 96-108): "Legal entry points (PP-103): After Phase 1 (declarations), After Phase 3 (movement), After Phase 6 Step 1 (damage application)." Non-battle Zoom In "fires at end of current Domain Action being resolved" (ED-073 resolved). Scene Opportunity table: Board FAILURE → scene Ob +1, SUCCESS → scene Ob −1, OVERWHELMING → scene Ob −2. §4.3 enumerates Mandatory (Priority 0) and World-State (Priority 1) Zoom In triggers in detail (lines 117-152).

**Usage sweep:** Canonical: `designs/architecture/scale_transitions_v30.md` (home, §1, §3.1-§3.9, §4.1-§4.4, §6.2-§6.3, §9-§10), `params/scale_transitions.md:20,58,60-64` (co-filed, consistent on entry points/PP-103), `designs/npcs/npc_behavior_v30.md:547` ("11 Zoom In triggers," cross-referencing `arc_expansion_v1_2026-04-16.md`), `designs/architecture/player_agency_v30.md:499-525` (Scene Slate as the generalized Zoom-In-trigger mechanism, explicitly "solves ED-545... the Scene Slate IS the Zoom In system"), `designs/architecture/campaign_modes_v30.md:134`.

**Divergence check:** No numeric contradiction found. `player_agency_v30.md`'s framing ("Scene Slate Priority 1 IS the Zoom In system... solves ED-545 (only 5 Zoom In triggers) structurally") is a documented **generalization**, not a contradiction — it explicitly supersedes a narrower earlier "5 triggers" count by making Zoom In emergent from any interesting state-change, which is consistent with (not competing against) `scale_transitions_v30.md` §4.3's more specific Mandatory/World-State trigger tables (which read as concrete instances of the general Scene Slate mechanism, not a rival system). No collision found with the npc_behavior_v30.md "11 Zoom In triggers" figure either — these are simply enumerated per-arc triggers layered on top of the same general mechanism, at different points in the corpus's evolution (ED-545 "5 triggers" → later 11 arc-specific triggers → Scene-Slate generalization), consistent with an expanding-not-contradicting history.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/architecture/scale_transitions_v30.md:96-152` | CANONICAL DEFINITION | Named home | — |
| `params/scale_transitions.md:58-64` | PULLED/REFERENCED (mostly) | Restates entry points (PP-103) consistent with the design doc — this specific sub-section of the otherwise-stale params file agrees | Agrees |
| `designs/architecture/player_agency_v30.md:499-525` | CANONICAL DEFINITION (generalizing extension, explicitly reconciled) | Explicitly named as resolving ED-545, cites the Scene Slate as the generalized trigger system | Agrees — documented supersession, not silent drift |
| `designs/npcs/npc_behavior_v30.md:547` | PULLED/REFERENCED | Cites an external arc-expansion doc for the specific "11 Zoom In triggers" count | Agrees, doesn't conflict |
| `designs/architecture/campaign_modes_v30.md:134` | PULLED/REFERENCED | Table entry citing the mechanism in a mode-comparison context | Agrees |

---

## 18. Zoom Out

**Home definition:** `designs/architecture/scale_transitions_v30.md` §4.2 (lines 110-115): "Definition: Transition from TTRPG scene back to BG layer. State transfer: Personal scene outcomes translate to BG consequences via Domain Echo (§5)... PC incapacitation consequences (Stage 1) apply immediately on Zoom Out (ED-159). Contested Figure wound → +1 Ob to commander's BG tactic rolls for remainder of battle (ED-167). Phase 6 continuation: Steps 2–6 resolve after Zoom Out using the updated state from the personal scene (PP-110)."

**Usage sweep:** Canonical: `designs/architecture/scale_transitions_v30.md` (home, §4.2, §6.3, §10, §11), `params/scale_transitions.md:61,63` (co-filed, consistent: "Hybrid → TTRPG: zoom-out; board state updated from personal scene results" / "Phase 6 continuation: Steps 2–6 resolve after Zoom Out using updated state (PP-110)"), `designs/architecture/campaign_modes_v30.md:134`.

**Divergence check:** No divergence found. Both the design-doc head and its co-filed params doc agree verbatim on the PP-110 Phase-6-continuation rule, which is reassuring given how badly the same params file diverges on Domain Echo caps (term 14) — this specific sub-section of `params/scale_transitions.md` was evidently kept in sync even though others in the same file were not, underscoring that the staleness in that file is partial/uneven rather than blanket.

**Classification table:**

| Site (file:line) | Classification | Mechanism/evidence | Agrees today? |
|---|---|---|---|
| `designs/architecture/scale_transitions_v30.md:110-115` | CANONICAL DEFINITION | Named home | — |
| `params/scale_transitions.md:61,63` | PULLED/REFERENCED | Restates the PP-110 rule identically, no independent number | Agrees |
| `designs/architecture/campaign_modes_v30.md:134` | PULLED/REFERENCED | Mode-comparison table entry | Agrees |

---

## Summary of the highest-value findings for downstream synthesis

1. **The Rupture** — `victory_v30.md` contradicts itself (line 557/628-638 "no shared loss, campaign continues" vs. line 647 "all factions lose"), and three live params files (`params/bg/clocks.md:18`, `params/bg/victory.md:61,139`, `params/bg/core.md:81`) plus the glossary all independently duplicate the stale "campaign-ending" reading — even though an archived 2026-06-11 audit already diagnosed this exact defect and it was never fixed in the live files.
2. **Disposition / Knot** — `designs/architecture/complete_systems_reference.md` contains two sections (line 188 vs. line 228) that directly contradict each other on Disposition's range (Bonds-capped PP-632 vs. flat −5..+5 ED-912), and the file's own supersession banner only scopes to "combat sections," silently missing this. `npc_behavior_v30.md:457` still states a "−4" rupture value that two other canonical docs (`knots_v30.md:197`, `fieldwork_v30.md:519`) both assert was already revised to "−3."
3. **Domain Echo** — the co-filed `params/scale_transitions.md` is an admittedly-stale (self-flagged "v0.14," 2026-04-03) file that contradicts itself on the Echo cap model (line 34 "per scene" vs. line 42 "not per scene total") and states a Debate→Echo target stat ("L"/"PS" axes) that doesn't match the current design doc's "Mandate" target.
4. **Disposition (term collision)** — confirmed a genuine, undisambiguated collision between the NPC-attitude gauge (−5..+5) and an unrelated combat-stance flat bonus ("Disposition modifiers: Offensive +2/Defensive +4," PP-218) in `combat_v30.md`/`combat_design_v1.md`.
5. **History / "Memory score"** — the glossary and one arcs doc both cite a cap attribute ("Memory") that does not exist in any current attribute roster; the live attribute is "Recall."
6. **Belief / Inspiration** — `designs/arcs/emergent_scenarios.md` gives Inspiration-spend and Belief-CP-award mechanics that are either uncorroborated anywhere else or directly contradict the canonical `derived_stats_v30.md` §5.3 spec (auto-success vs. Ob−1 for Inspiration spend); its own header phrasing ("Stage 1-12") suggests it predates the current generation and was never reconciled.
7. **Character Point / CP** — `combat_design_v1.md:354` still uses the deprecated "CP" = Combat Power abbreviation the glossary's ED-136 collision table explicitly forbids.
8. **Domain Action** — `faction_layer_v30.md:213` (Claim Masterless) wasn't migrated to the ED-874 resolver notation its sibling lines all received.
9. **Co-Movement Card / Zoom In / Zoom Out** — clean, no divergence found; confirms the audit method also surfaces the healthy cases, not only the broken ones.
