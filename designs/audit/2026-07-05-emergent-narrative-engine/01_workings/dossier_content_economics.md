# Dossier — Content Economics of the Template Banks (Lane: Q4 bake sizing)

## Status: WORKING NOTES (not canonical). Author: sonnet subagent, 2026-07-05.
## Question: how big is the bake, really? Is C1 (authored-templates-only) feasible at the
## anti-oatmeal bar, and what factoring makes it so?

---

## 0. Method note

Per charter method rules (`00_engine_charter.md` "Method rules"), KNOWN items from the ratified
2026-07-04 NERS audit are context not discoveries; numbers marked `[OPEN — Jordan tuning]` are
calibration not structure. This dossier cites file+section for every count; anything I could not
pin to a source is tagged `[UNGROUNDED]`.

---

## 1. The axes, counted from source

### 1.1 Key-types-that-render

`designs/architecture/key_type_registry_v30.md` §9 declares **Total 44** registered types across
7 families. I parsed the file directly (`grep -c '^### '`) and found **48 physical `###` entries**
— a 4-entry drift (scene.combat_strike, scene.combat_hit, scene.combat_felled physically present
under §7 but not counted in the §9 family table's arithmetic, which sums cleanly to 44 without
them). The registry's own §9 footnote already names this class of problem ("the pre-existing
declared-vs-parsed header drift, master item 11 / A9, is out of J-2 scope") — **this is a KNOWN
drift, not a new discovery**, but it means "44" is a soft number; treat the true count as
44–48 depending on whether you trust the declared total or the parse.

Of the 48 physical entries, I checked `consuming_systems:` for literal `articulation` membership:

- **43 list `articulation`** (explicitly, or via `consuming_systems: [all]` /
  `[all subscribing systems]` for `mechanical.season_change` and `env.crisis`, counted as
  implicit-yes).
- **5 explicitly do NOT**: `mechanical.scene_skipped` (§4, consumers `[scene_timer, audit]`),
  `env.population_change` (§6, consumers `[faction_layer, settlement_economy]`),
  `scene.combat_strike` (§7, consumers `[personal_combat]`), `scene.combat_hit` (§7, consumers
  `[personal_combat]`), `meta.legacy_event` (§8, consumers `[legacy-aware consumers only]`, a
  pruned Phase-B wrapper).

**Working number: ~43 Key-types are the articulation-relevant subset** (of 44 declared / 48
physically present). This is the base of the "Key-type" axis in every combinatoric below.

### 1.2 Trigger / beat classes

`designs/articulation/articulation_layer_v30.md` §3.1: **10 Tier-2 triggers** (8 initial per D10,
+#9 cascade clustering 2026-05-01, +#10 belief_revised 2026-05-02). Each trigger names a specific
Key type/condition (e.g. `state.scar_acquired`, `state.coup_attempted`) — the triggers are mostly
a **flagged subset of the Key-type axis**, not an independent orthogonal dimension.

§3.2: significance range **0–13**, splitting into **3 numeric length bands**: 5s (0–4), 10s (5–9),
15s (10–13). But §3.4 ("Cut scene rendering") only names **2 authored template STYLES**: "5–10
second style (flash)" and "10–15 second style (scene)" — i.e. the 5s and 10s numeric bands share
one template structure. **This is itself a collapse**: 3 significance thresholds → 2 authored
render-structures. §4.3: Tier-3 chronicle reuses the Tier-2 significance *form* minus
`protagonist_alignment` (a "universal track") — Tier 3 is not a third render-structure, it's the
same numeric machinery pointed at a different aggregation window (annual, peninsula-scope, top-N).

**Working number: 2 authored template structures per Key-type (flash / scene)** is the real
multiplier for "trigger/beat classes" once §3.4's actual authored surface is read, not 3 (numeric
bands) and not 10 (triggers, which are conditions-on-Key-type, not template-shape drivers).

### 1.3 Coherence bands (6) — confirmed exact match

`skills/prose-writer/references/coherence-tiers.md`: **10-8 Stable / 7-5 Dissonant / 4-3
Fragmented / 2 Fractured / 1 Severed / 0 Rendering Crisis** = 6 bands, tied to `threadwork_v30
§3.3`. Confirmed against `02_prose_render_stack.md` (a).1.

### 1.4 An axis the task formula omits but the corpus requires: Thread Sensitivity (3 bands)

`coherence-tiers.md`'s own per-tier weight tables are keyed **jointly** by Coherence × TS, and TS
itself has **3 explicit bands: TS 0-29 / TS 30-49 / TS 50+** (repeated at every Coherence tier's
table header). The NLG proposal's own bake key (`03_articulation_nlg_architecture.md` §8: "per
(Key-type × X/Y band × focalizer)", where X=Coherence, Y=TS per §2.2) **already includes TS in the
frozen-fragment key** — so the task's 7-factor formula (which has no TS term) understates the
corpus's own stated bake key by one axis. I keep this separate below because it turns out **not to
explode the fragment count** (see §2.2) — it's absorbed into an existing weight table, not new
authored prose — but it is a real omission worth flagging.

### 1.5 Certainty registers (6, as given) — but the source table is 5 rows and doesn't cleanly cover the mechanical range

Two Certainty definitions coexist and don't line up:
- **Mechanical** (`params/core.md` §Certainty Track, PP-551, cited at
  `02_prose_render_stack.md` (d)): **0–5, 6 discrete values** ("5 Orthodox … 0 Accepted").
- **Voice-register table** (`designs/world/solmund_voice_v30.md` §18 "Tonal Calibration by
  Certainty"): **5 rows** — `1-2` (Böhme/Niflhel, one row covering two values) / `3` / `4` / `5` /
  `6+ (with TS 30+)` (John of the Cross/Teresa). This table **never assigns a register to
  Certainty 0** and references a **"6+"** value that is out of range for the stated 0-5 mechanical
  scale. `02_prose_render_stack.md` (a).3 repeats the same "6+ w/ TS30+" framing.

**This is a genuine, previously-unflagged schema gap** (distinct from the six gaps already named
in `02_prose_render_stack.md` (e)): the register table that would drive lexicon selection has a
coverage hole at Certainty 0 and a value ("6+") that doesn't exist on the mechanical track it's
supposedly keyed to. I use the task-given **6** (matching the mechanical 0-5 range) for the
formula below, but the actual authored register asset is **5 named clusters, one with a
coverage gap**, so the real lexicon-table size is smaller (5), not larger.

### 1.6 Spirit split (2, low-Coherence only) — confirmed, and it's a 3-way split with a free middle

`coherence-tiers.md` "Spirit Axis Interaction": Spirit is audible only at Coherence ≤4. The table
is actually **3-way** (High 5-7 / Mid 3-4 / Low 1-2), but **Mid explicitly needs no distinct
prose** ("No specific Spirit-axis effect. Tier's standard weighting applies.") — so the *authored*
branch count is exactly the task's given **2** (High-Beckett / Low-Lispector); Mid is free
(default tier prose, zero incremental cost). Applies to 4 of the 6 Coherence bands (4-3, 2, 1, 0);
the top 2 bands (10-8, 7-5) need no Spirit variant at all.

### 1.7 Focalizers (5) — confirmed, and already-authored, not new bake cost

`skills/prose-writer/SKILL.md` line 151: **4 canonical chroniclers** (Church Cert-5/TS0, Hafenmark
Cert-4/TS0, Restoration Cert-2/TS0, Warden Cert-0/TS70+) **+ protagonist frame** = 5. Two
consequences worth flagging:
- Each chronicler has a **fixed** Certainty value baked into its identity. When focalizer =
  chronicler, the Certainty axis (§1.5 above) is **already resolved by the focalizer choice** —
  you don't cross 4 chroniclers × 6 Certainty registers (24 combos); you get 4 fixed
  chronicler/Certainty pairs. Certainty-as-independent-axis only applies to protagonist-focalized
  content.
- The chronicler voice profiles are **already fully authored** as design prose
  (`narrative_voice_canon_v30.md`, `solmund_voice_v30.md`, `prose-writer/SKILL.md`) — applying a
  focalizer at splice time is a voice-TAG operation on existing assets, not new per-Key-type
  prose, per the NLG thesis (`03_articulation_nlg_architecture.md` §2.3: "the voice tag *is* the
  inter-fragment transition, so no connective generation is required").

### 1.8 Per-NPC overlays — bounded, not combinatorial

`designs/npcs/npc_behavior_v30.md` §11 (PP-661): the peninsula supports **~35 named NPCs at
Active tier** at any time (soft cap; demotion at 36th). **~30 Passive** get compact tracking only
(no full lexicon/voice-register overlay implied — §11.1's storage column for Passive omits voice
register). **Background is unlimited but "Identity only"** — zero overlay cost by design (§11.4:
"They have no tracked state"). This is the key structural fact for feasibility: the per-NPC axis
is **capped at 35 by an existing mechanical rule**, not open-ended — it cannot blow up the bake
past a fixed, small ceiling.

### 1.9 Per-arc specificity — the corpus's own comparable-scale precedent

`01_arc_corpus.md` (a): **~110 arc IDs** across `references/arcs/` (5 files, ~69KB total —
verified: `arc_register_clocks.md` 4.4K, `_threads.md` 5.3K, `_territory.md` 11.6K,
`_factions.md` 41.8K [87 of the ~110 entries], `_events.md` 6.2K). Each entry follows a **uniform
anatomy** (ID/title/header → trigger → mechanical effects → one "Direction:" causal sentence) —
i.e. the register itself already demonstrates that ~110 distinct arcs can be given individually
identifiable causal color at roughly 400–500 bytes / 60-90 words each.

The deeper hand/LLM-authored prose analysis layer, `designs/arcs/gm_ref/` (8 files, verified
**~300KB total** — `arc_narrative_analysis.md` 48K, `arcs_01_04.md` 36K, `arcs_05_09.md` 28K,
`arcs_10_18.md` 56K, `arcs_36_40.md` 48K, `arcs_41_45.md` 56K, `arcs_46_55.md` 40K,
`arcs_46_55_resolved.md` 40K — despite its own README claiming "currently empty," per
`01_arc_corpus.md` (c)), gives ~2.7KB (~400-450 words) of specific narrative color per arc across
roughly 55+ arc entries covered by these files.

The `tests/` narrative-regression corpus (charter's "~850KB, decision-queue item 25a") is larger
than the charter's estimate once measured directly: **`emergent_arc_skeleton_test_*` batches
2–8 alone total 769,581 bytes** (verified via `wc -c`; no batch 1 file exists in the tree), and
`tests/sim/sim_arc_*.md` adds another ~280KB on top of that (8 files, 4K–60K each) — combined
comfortably over 1MB, not 850KB. This is prose/audit material per CLAUDE.md §3, not executable
spec, but it IS an existing proof-point that this repo has already produced arc-specific narrative
color at a rate of hundreds of words per arc, at a scale (~100+ arcs) comparable to what the
articulation bake would need for "per-arc specificity" (charter's anti-oatmeal criterion 3: "the
arc_test_batch seed method as NARRATIVE regression — 5 seeds must yield chronicles differing in
named actors, stakes, outcomes").

**Working conclusion: arc-specific color is a DATA-substitution problem (targets[]/causes[] named
entities), not a new prose-fragment-per-arc problem** — the causal "Direction:" sentence pattern
already in `references/arcs/` is the model: one authored sentence-shape per arc family, entity
names filled from the arc register at bake or runtime, not one bespoke fragment per
(arc × Coherence × Certainty × focalizer).

---

## 2. Combinatorics — three ways to count it

### 2.1 Naive full cross-product (never build this — the oatmeal trap named at `03_...` §2)

Using the task's given axis values literally:

```
43 (Key-types) × 10 (§3.1 triggers) × 6 (Coherence) × 6 (Certainty) × 2 (Spirit) × 5 (focalizer) × 35 (per-NPC)
= 43 × 10 = 430
  × 6     = 2,580
  × 6     = 15,480
  × 2     = 30,960
  × 5     = 154,800
  × 35    = 5,418,000
```

**~5.4 million** distinct fragments if every combination got unique authored prose. This is
absurd on its face and is exactly the failure mode `03_articulation_nlg_architecture.md` §2 names:
"The combinatorial trap is baking finished sentences per (type × tier × focalizer × …)."

Even a more charitable naive reading — using the corrected axis granularities from §1 (2 template
STYLES not 10 triggers, drop per-NPC as a full multiplier since it's mostly name-substitution) —
still gives:

```
43 × 2 (styles) × 6 (Coherence) × 6 (Certainty) × 2 (Spirit) × 5 (focalizer)
= 86 × 6 = 516 × 6 = 3,096 × 2 = 6,192 × 5 = 30,960
```

**~31,000** — still 2+ orders of magnitude beyond anything this repo has produced for comparable
prose corpora (gm_ref: ~110 arcs / 300KB; skeleton-test corpus: ~1MB across 15 files covering many
fewer than 31,000 distinct narrative beats).

### 2.2 The factored/orthogonal strategy (what `03_articulation_nlg_architecture.md` §2/§8 actually proposes)

The proposal's thesis is explicit: keep the four factors "orthogonal and compose at runtime — a
product becomes a sum." Applying that discipline with the corrected per-axis counts from §1:

**(a) Backbone slot-templates** — the only axis that should vary TEMPLATE STRUCTURE:
`Key-type (43) × render-style (2, §3.4 flash/scene)` = **~86 slot-templates**. (If Jordan wants
the numeric 3-band split preserved instead of the 2-style collapse: ~129. Either way, low
hundreds, not thousands.)

**(b) Shared lexicon/register overlays — reused across ALL 86 templates, not copied per-template:**
- Coherence × TS author-weight table: **already exists**, `coherence-tiers.md` — 6 Coherence
  bands × 3 TS bands = 18 cells × 12 author-weight percentages = 216 numbers. This is a numeric
  weighting table, not prose; it costs nothing incremental per new Key-type. This is the concrete
  mechanism by which the omitted TS axis (§1.4) is absorbed WITHOUT multiplying fragment count.
- Certainty register lexicon: **5 named clusters** (`solmund_voice_v30.md` §18), shared.
- Spirit closing-register table: **2 variants** (Beckett/Lispector) × the 4 low-Coherence bands
  where it's audible — `coherence-tiers.md` already gives worked closing-line exemplars per band
  (e.g. C1 High-Spirit "she can't go on. she goes on."; C1 Low-Spirit "the feet move.") — call it
  **~8 shared closing-register exemplars**, reused across every template, not per-Key-type.
- Focalizer voice profiles: **5**, but these are ALREADY AUTHORED assets (voice canon docs) being
  referenced at splice time, not new bake cost (§1.7).

Total shared-layer authored units: roughly **216 (numeric, near-zero marginal cost) + 5 + 8 ≈ a
few dozen genuinely new small text units**, applied everywhere via substitution — this is the
actual mechanism of the "product becomes a sum" claim.

**(c) Per-NPC overlay** — bounded by the 35-Active-NPC cap (§1.8): a handful of idiolect/voice
quirks per NPC (not full fragment sets), estimate **~3-5 authored micro-units × 35 NPCs ≈
100-175 units**, reused across every template that names that NPC (name + a couple of lexical
swaps, not a new fragment per NPC-per-Key-type-per-Coherence-band).

**(d) Per-arc specificity** — absorbed as data substitution (targets[]/causes[] entity names)
plus arc-flavored causal color at the SAME rate the register already demonstrates
(~110 arcs × one "Direction:"-style sentence-shape ≈ **~110 authored sentence-templates**, entity
names filled from data, not per-arc-per-axis fragments) — §1.9.

**Factored-strategy total: roughly 86 (backbone) + ~30-50 (shared lexicon net-new) + ~100-175
(per-NPC) + ~110 (per-arc sentence-shapes) ≈ 350-450 authored units**, order of magnitude
**low hundreds**, not the 31,000-5,400,000 of §2.1. This is a ~2-4 order-of-magnitude collapse,
achieved entirely by treating Coherence/TS/Certainty/Spirit as swappable lexicon layers and
focalizer as a voice-tag over existing assets, rather than baking one fragment per full
combination — exactly the "compose, don't multiply" discipline `03_...` §2 names as the fix.

---

## 3. Where it genuinely does NOT collapse (the real risk)

1. **Per-NPC voice, if done for real ("recognizable-yet-dynamic NPCs," charter Q3) genuinely
   needs distinguishing content**, not just a name swap, or the anti-oatmeal bar fails: two
   Bonded NPCs both getting `state.scar_acquired` cut scenes must not read as the same template
   with a name swapped in. The 35-NPC cap bounds the COUNT but not the AUTHORING EFFORT PER NPC —
   if each Active NPC genuinely needs several idiolect-specific fragment variants across the ~10
   triggers that can fire for them, effort is closer to 35 × 10 × (a few variants) than 35 flat.
   This is the honest "explodes" case the task asked me to find: **bounded in cardinality (good),
   NOT bounded in per-unit authoring cost (open risk)**.
2. **Per-arc specificity, if the capstone's "causes[] continuity" requirement (charter Q3
   "Coherence as A narrative") and "two-seed chronicle comparison... must differ in named actors,
   stakes, outcomes" (capstone #11) are read strictly**, generic slot-fill risks producing
   structurally-identical prose across arcs that only differ in proper nouns — exactly Compton's
   oatmeal risk (`03_...` §9). The register's existing "Direction:" sentences (§1.9) are short and
   formulaic BY DESIGN (arc-generator skill's mandatory hard rules per `01_arc_corpus.md` (c)) —
   good enough for a mechanical register, not obviously good enough for player-facing prose
   without additional arc-specific authored color beyond simple substitution.
3. **The NLG proposal's own bake key omits Certainty entirely** (`03_...` §8: "per (Key-type ×
   X/Y band × focalizer)" — X=Coherence, Y=TS, no Z=Spirit or Certainty term in that specific
   sentence, though Spirit is discussed elsewhere in the same doc), while the charter's Q4
   restatement of the SAME bake explicitly includes **both** "Coherence/TS/Spirit band" AND
   "Certainty register" as separate factors (`00_engine_charter.md` Q4, "Prose realizer:
   graduate the NLG proposal (template/slot schema; offline bake per Key-type × Coherence/TS/
   Spirit band × Certainty register × focalizer...)"). **This is an unresolved factor-count
   discrepancy between the two most-authoritative sources on the bake key**, not something I can
   resolve by picking one — it needs Jordan's call before the real bake is scoped, because if
   Certainty must gate the FROZEN FRAGMENT pool (not just a runtime lexicon swap), §2.2's backbone
   estimate should multiply by up to ~5-6× (the Certainty register count), pushing the low-
   hundreds estimate into the low-thousands. Distinct from the six gaps already named in
   `02_prose_render_stack.md` (e) — none of those six items name this specific mismatch.

---

## 4. Numbers used, with citations (recap for the structured output)

| Axis | Count | Source |
|---|---|---|
| Key-types-that-render | ~43 (of 44 declared / 48 physically parsed) | `key_type_registry_v30.md` §9 + direct `consuming_systems:` grep |
| Tier-2 triggers | 10 | `articulation_layer_v30.md` §3.1 |
| Authored render-styles (not numeric bands) | 2 (flash 5-10s / scene 10-15s) | `articulation_layer_v30.md` §3.4 (vs. 3 numeric bands in §3.2) |
| Coherence bands | 6 | `coherence-tiers.md`; `threadwork_v30 §3.3` |
| TS bands (omitted from task formula, present in bake key) | 3 (0-29/30-49/50+) | `coherence-tiers.md` per-tier tables; NLG §8/§2.2 |
| Certainty registers | 6 given (mechanical 0-5); table has 5 rows w/ coverage gap at 0 and an out-of-range "6+" | `params/core.md` §Certainty Track (PP-551); `solmund_voice_v30.md` §18 |
| Spirit split | 2 authored (High/Low); Mid is free | `coherence-tiers.md` "Spirit Axis Interaction" |
| Focalizers | 5 (4 chroniclers, fixed Certainty each, + protagonist) | `skills/prose-writer/SKILL.md` line 151 |
| Active-tier NPC cap | ~35 (soft cap, PP-661) | `npc_behavior_v30.md` §11.2 |
| Passive-tier cap | ~30 (compact, no full overlay) | `npc_behavior_v30.md` §11.6 |
| Arc register size | ~110 IDs / ~69KB across 5 files | `01_arc_corpus.md` (a); direct `ls -la` |
| gm_ref prose corpus | 8 files, ~300KB (confirmed, not "empty" per its own stale README) | `01_arc_corpus.md` (c); direct measurement |
| emergent_arc_skeleton + sim_arc test corpus | 769,581 bytes (batches 2-8) + ~280KB sim_arc = >1MB (charter's "~850KB" is an undercount by direct measurement) | direct `wc -c` / `du -sh` |

No authoring-throughput number (fragments/hour, words/session) exists anywhere in the corpus
searched — **[UNGROUNDED]** beyond the comparable point that gm_ref's ~300KB / ~110-arc corpus and
the ~1MB skeleton-test corpus are the largest prose assets of this genre actually produced in this
repo, and both sit at the SAME low-hundreds-of-arcs / low-hundreds-of-KB order of magnitude as the
factored bake estimate in §2.2 — i.e., the factored strategy's ~350-450 authored-unit target is not
a novel scale for this project, it's roughly what's already been done once for the arc corpus.

---

## 5. Verdict

**C1 (authored-templates-only, no runtime LLM) is FEASIBLE at the anti-oatmeal bar — but only
under the factored/orthogonal-composition discipline `03_articulation_nlg_architecture.md` §2/§8
already proposes, and only if two open items get closed:**

1. **Never bake per-full-combination fragments.** The naive cross-product is 31,000-5,400,000
   depending on which axis granularities you take literally (§2.1) — infeasible by any authoring
   method, offline-LLM or hand. The factored strategy collapses this to an estimated **low hundreds
   of authored units** (§2.2: ~86 backbone slot-templates + shared lexicon layers reused
   everywhere + ~35-NPC-bounded overlay + ~110-arc-bounded causal color), a 2-4 order-of-magnitude
   reduction, achieved by making Coherence/TS/Certainty/Spirit swappable LEXICON layers (mostly
   already-existing weight tables and voice-canon documents, not new prose) and focalizer a
   voice-TAG applied at splice time, rather than multiplying the backbone.
2. **Close the Certainty-in-bake-key discrepancy** (§3 item 3) before scoping the real build —
   the NLG proposal's stated bake key and the charter's Q4 restatement disagree on whether
   Certainty gates the frozen fragment pool; this swings the estimate by up to ~5-6×.
3. **The per-NPC and per-arc axes are the genuine (not merely apparent) risk** (§3 items 1-2):
   cardinality is bounded (35 NPCs, ~110 arcs, both hard/soft caps that already exist in the
   corpus), but per-unit AUTHORING EFFORT to hit "recognizable-yet-dynamic" (Q3) and "differ in
   named actors, stakes, outcomes" (capstone #11) without oatmeal is not something the combinatoric
   math can certify — it's a writing-craft question the existing gm_ref corpus suggests is
   achievable (it's already been done once, at comparable scale) but which the current design docs
   don't yet budget for as a distinct bake-effort line item.
