# Term Usage Sweep — Batch 8: NPC Behaviour and Articulation terms

# Batch 8: NPC Behaviour and Articulation Terms — Cross-Contamination Audit

**Primary sources read in full:** `designs/npcs/npc_behavior_v30.md` (1259 lines), `references/descriptor_registry.yaml` (115 lines), `designs/articulation/articulation_layer_v30.md` (364 lines), `designs/personal/conviction_taxonomy_v30.md`, `designs/personal/conviction_track_v1.md`, `designs/architecture/key_substrate_v30.md` (excerpt), `designs/architecture/player_agency_v30.md` (excerpt), plus targeted excerpts of ~40 other files cited inline below.

---

## 1. Conviction (the 13 canonical values)

**Home definition.** `designs/personal/conviction_taxonomy_v30.md` §2 (lines 25-41), header marked `## Status: CANONICAL`, authority PP-684, promoted from PROVISIONAL "after Stage 10 sim PASS" per the file's own top-of-file banner (line 1). The 13 Convictions, verbatim: **Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor** (lines 29-41). Structure: vector-valued per actor, 1-3 "primary" Convictions weighted 0.6-0.8 + distributed "cultural background" weighted 0.2-0.4, projected onto a 4-axis space (§4, lines 115-131). `npc_behavior_v30.md` §1.2 (lines 24-30) explicitly redirects to this doc as canonical and explicitly marks the **legacy 9-Conviction set** (Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity, Community, Warden) at `conviction_track_v1.md` as **superseded** — "Reason and Continuity are deprecated labels; Autonomy is renamed Liberty" (npc_behavior_v30.md:30).

**Exhaustive usage sweep.** "Conviction" occurs **1,745 times across ≥250 files** (grep capped at 250 files/1745 hits — file list truncated by tool, true corpus total is larger). This is far too large to enumerate exhaustively; I instead traced the specific taxonomy-list restatements (the actual load-bearing risk surface) and sampled representative live-canon vs stale-canon sites:

- **Canonical 13-set restatements/consumers (agree with home):** `references/descriptor_registry.yaml:88` (`by_reference` entry, `conv.*` → source `conviction_taxonomy_v30.md §2`); `params/factions_personal.md:56` ("cascade alignment reads PP-684 13-Conviction projection"); `.claude/wf_social_contest_critique.js:20,36,178` (workflow-script prose citing "the 13-Conviction / 4-axis matrix"); `archives/patches/patch_register_archive_2026_05_10.yaml:9,48,54,581` (PP-684/685 patch entries).
- **Legacy 7/9-value taxonomy still live in prose (superseded but present):** `designs/npcs/npc_behavior_v30.md:1055` (ED-384, an open/unresolved editorial item still asking "Confirm Conviction taxonomy: 7 values… Sufficient?" even though PP-684 answered this on 2026-05-01); `designs/npcs/npc_behavior_system_v1.md` (the pre-v30 file, still on disk, explicitly `## Status: SUPERSEDED` at line 3 — properly marked, historical only); `canon/editorial_ledger_archive.jsonl:294` (ED-515, archived).
- **Player-facing / UI hardcoded restatement:** `designs/ui/valoria_ui_ux_v4.md:2136` — `Resource: StanceTriangle // for NPCs` → `primary_conviction: enum {Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity}`. Same file, lines 349-359, gives full example dialogue-tag text for "all seven Conviction types (npc_behavior §1.2)" including `[ Lisbeth : Autonomy ]` and `[ Edeyja : Continuity ]`.
- **Params-layer hardcoded restatement:** `params/factions/npc_stance_triangles.md:5-14` — a table headed "### Conviction Taxonomy" that independently restates the **same legacy 7 values** (Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity) with an explicit provenance comment at line 3: `<!-- Source: designs/systems/npc_behavior_system_v1.md §2. Canonical. -->`.
- **Genuinely distinct second mechanic sharing the same name — player-facing Conviction:** `designs/architecture/player_agency_v30.md` §2 (lines 65-116). Here "Conviction" means a **player-authored free-text sentence goal** ("I will discover what Haelgrund is hiding from the Church"), 3 per character, with Fulfilled/Failed/Transformed/Unresolved resolution states (lines 91-98) and Momentum rewards — structurally nothing like the 13-named-value vector. Yet line 71 explicitly asserts: *"Vocabulary unification: Player Convictions and NPC Convictions (npc_behavior_v30 §1.2) share the same name because they serve the same function… Both are targetable via Resonant Styles."*
- **Third restatement, conflating the two:** `designs/scene/derived_stats_v30.md:215` — `**Conviction** (per player_agency §2) | Worldview / framework | Drives all major decisions; determines Resonant Style; tracked on Piety Track | Lifetime; shifts only through Scar accumulation` — this cites player_agency §2 (the free-text-sentence mechanic) as its source but describes the NPC-taxonomy mechanic ("determines Resonant Style" is meaningless for a free-text sentence; it only makes sense for a named value from the 13-set).

**Divergence check.**
1. **Stale 7/9-value taxonomy still hardcoded, unflagged, in a params file that claims canonical status.** `params/factions/npc_stance_triangles.md:5-14` independently restates: `| Conviction | Grounding Claim | ... | Faith | ... | Order | ... | Reason | ... | Equity | ... | Precedent | ... | Autonomy | ... | Continuity | ...` — 7 rows, none of Scholastic/Liberty/Identity/Virtue/Honor present, "Reason"/"Autonomy"/"Continuity" present as if still live (all three are explicitly deprecated labels per npc_behavior_v30.md:30). The file's own header (line 3) claims this is sourced from `npc_behavior_system_v1.md §2` and marks itself "Canonical" — but that source file is itself marked SUPERSEDED. No cross-reference anywhere in this params file to PP-684 or the 13-set.
2. **UI/Godot data-serialization spec hardcodes the same stale 7-set as a Resource enum**, dated 2026-04-16 (`designs/ui/valoria_ui_ux_v4.md`, self-declared `## Status: CANONICAL` at line 6, "Godot-development-ready interface specification"), predating PP-684 (2026-05-01). `primary_conviction: enum {Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity}` (line 2136) is a literal Godot `Resource` field enum that would need updating to the 13-set before any Godot port could ingest it, and nothing in the file carries a staleness banner pointing this out (contrast with the `⚠️ STALE / PARTIALLY SUPERSEDED` banners CLAUDE.md §6 says exist on the four `designs/godot/*.md` docs — this UI doc has no equivalent banner despite the same kind of drift).
3. **An unresolved open editorial item (ED-384) in the CANONICAL npc_behavior_v30.md still poses the superseded question** ("Confirm Conviction taxonomy: 7 values…Sufficient?", npc_behavior_v30.md:1055) as if live, even though PP-684 (a different, later doc) answered it with a different, larger set. Nothing marks ED-384 resolved-by-PP-684.
4. **Two structurally different mechanics share the literal name "Conviction"** and are explicitly declared equivalent by player_agency_v30.md:71 ("Vocabulary unification… share the same name because they serve the same function") despite one being a 13-value weighted taxonomy pick and the other a free-text authored sentence with its own resolution-state lifecycle (Fulfilled/Failed/Transformed/Unresolved) that has no analogue in conviction_taxonomy_v30.md at all. `derived_stats_v30.md:215` then blends the two descriptions into one table row, citing the free-text mechanic's source doc while describing the named-value mechanic's behavior.
5. A stale, never-adopted **rename proposal** exists for this same term-cluster: `designs/architecture/canonical_registry.md:216-221` ("COMPLETE RENAME TABLE") proposes `Belief Scar` → `Conviction Wound` and (see Term 6) `Leadership Deviation Ob` → `Authority Challenge Ob`, in a 2026-04-15 doc whose only currency banner (`⚠️ PARTIALLY SUPERSEDED, 2026-07-01, ED-1084`, lines 7-11) explicitly scopes itself to "Combat Pool rows" only — leaving this rename table's status ambiguous. No live doc anywhere uses "Conviction Wound" or "Authority Challenge Ob."

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/personal/conviction_taxonomy_v30.md:25-41` | CANONICAL DEFINITION | This is the named home site (PP-684). | — |
| `references/descriptor_registry.yaml:88` | PULLED / REFERENCED | `by_reference` entry with `source: designs/personal/conviction_taxonomy_v30.md §2`; no independent literal restated. | Yes |
| `params/factions_personal.md:56` | PULLED / REFERENCED | Prose citation "PP-684 13-Conviction projection," no independent list restated. | Yes |
| `designs/npcs/npc_behavior_v30.md:26-30` | PULLED / REFERENCED | Explicit redirect stub naming conviction_taxonomy_v30.md as canonical; also explicitly narrates the legacy-9 supersession. | Yes (correctly describes the supersession) |
| `designs/npcs/npc_behavior_v30.md:1055` (ED-384) | HARDCODED DUPLICATE (stale) | Independently restates "7 values" as an open question, no updated cross-reference to PP-684. | No — asks a question PP-684 already answered differently |
| `designs/npcs/npc_behavior_system_v1.md` (whole doc) | HARDCODED DUPLICATE, properly labeled superseded | File header line 3: `## Status: SUPERSEDED — canonical doc is designs/systems/npc_behavior_v30.md`. Historical-reference only. | No (by design/labeled) |
| `params/factions/npc_stance_triangles.md:5-14` | HARDCODED DUPLICATE | Independent literal table restating the legacy 7-value set; comment claims "Canonical," cites the *superseded* source doc, no PP-684 pointer. | No — actively drifted, unflagged |
| `designs/ui/valoria_ui_ux_v4.md:2136,351` | HARDCODED DUPLICATE | Literal Godot `enum` restating the legacy 7-value set; doc self-declares CANONICAL, no staleness banner. | No — drifted, unflagged |
| `designs/architecture/player_agency_v30.md:65-116` | UNCLEAR / NO CANONICAL SOURCE (distinct mechanic, same name) | Independently defines a structurally different "Conviction" (free-text sentence) and asserts name-equivalence with the taxonomy mechanic without reconciling the structural mismatch. | N/A — not the same mechanic |
| `designs/scene/derived_stats_v30.md:215` | UNCLEAR / NO CANONICAL SOURCE (conflated) | Cites player_agency §2 as source, describes taxonomy-mechanic behavior ("determines Resonant Style"). | Ambiguous — conflates two sources |
| `designs/architecture/canonical_registry.md:216-221` | HARDCODED DUPLICATE (unadopted proposal) | Independent rename proposal table, 2026-04-15, no adoption anywhere else in corpus. | N/A — never adopted |

**Incidental usage.** None excluded — every occurrence sampled above is the game-mechanical Conviction system; I did not encounter "conviction" used as an ordinary-English word (e.g., "acted with conviction") in the sampled sites, though given 1,745 raw hits across the corpus it is likely some exist in narrative prose I did not open; I flag this rather than claim certainty.

---

## 2. Resonant Style (cross-check against descriptor_registry.yaml's deprecated block / ED-IN-0025 correction)

**Home definition.** `designs/npcs/npc_behavior_v30.md` §1.3 "Resonant Style Taxonomy" (lines 32-40), part of a document whose own `## Status: CANONICAL — approved 2026-04-17` (line 6). Four values: **Evidence, Consequence, Authority, Solidarity**, each with an NPC-vulnerability description and a "Contest mapping" column tying it to the *different* contest_style axis (Memory/Projection × Revealing/Obscuring). Consumed mechanically in §6 "Resonant Style in the Contest System" (lines 677-738): +1D targeting bonus, Piety-Track bypass effects, Doubt Marker placement, stacking rules capped at +5D total positional bonus (§6.5, line 738).

**The precise flagged contradiction (as instructed to trace).** `references/descriptor_registry.yaml` §`deprecated` (lines 99-100):
> `resonance_style -> DEPRECATED`... "Was the 'most-persuasive mode of argument'. Superseded by contest_style (social_contest Step 2-3) + Conviction-driven interpretation. **Never canonically enumerated** (player_agency §2 references but does not define it). Retired 2026-06-06 (Jordan). ⚠️ **CORRECTION (ED-IN-0025, 2026-07-07, C-VERIFY-20): the 'never canonically enumerated' premise is factually FALSE** — npc_behavior_v30.md §1.3's Resonant Style Taxonomy **is CANONICAL (approved 2026-04-17)** and player_agency_v30.md:71 treats it as live, bidirectional, load-bearing. Whether the retirement should stand given this is a Jordan design call (NEEDS-JORDAN), not re-litigated here; **retirement status left unchanged**."

I traced this and it is confirmed unresolved and, moreover, contradicted by *subsequent, dated-after-the-original-deprecation* canonical activity:
- `params/contest.md:164` (live, current head per CURRENT.md §Social contest row) — describes a brand-new "Adjudicator Armature" mechanism, **ratified by Jordan at Gate C, 2026-07-02** (i.e. a month *after* the 2026-06-06 "retirement"), and explicitly writes: *"Gated off in asymmetric proceedings… to avoid double-counting the existing opponent-aimed Resonant Style targeting"* — treating Resonant Style targeting as a live, currently-operative mechanic requiring careful non-collision engineering, not something retired weeks earlier.
- `designs/scene/social_contest_v30.md:171,176` — same Gate C material: *"distinct from... the existing opponent-aimed Resonant Style targeting (npc_behavior_v30.md §1.3/§6.3), which fires on the party you are arguing against"* and *"the existing opponent-aimed Resonant Style targeting is not double-counted."*
- `params/contest_extensions.md:29-39` — "## Resonant Style Targeting (from npc_behavior_system_v1.md §6)" — an active Appraise-reveal table still governing play.

So: the descriptor_registry.yaml deprecation (2026-06-06) was never actually enforced anywhere in the contest subsystem, which kept building *new* features around Resonant Style as a live mechanic through at least 2026-07-02, and the registry's own later correction (2026-07-07) concedes the deprecation's premise was false — yet leaves the DEPRECATED flag standing. This is a genuinely live, unresolved self-contradiction in the corpus, exactly as flagged.

**A second wrinkle the registry's framing obscures:** `contest_style` (the claimed "successor," `descriptor_registry.yaml:92` — Precedent/Suppression/Vision/Insinuation = Memory|Projection × Revealing|Obscuring, source `social_contest_v30.md` Step 2-3) is **not the same thing** as Resonant Style even under npc_behavior_v30's own mapping table (§1.3, line 34-39): Resonant Style is an NPC-specific *vulnerability* category (which of the NPC's Beliefs/Convictions can be targeted) layered *on top of* a contest_style choice, not replaced by it — §6.3 (line 694-701) shows both operating simultaneously ("Required form: Memory + Revealing (Precedent)" *and* the Resonant Style bonus stacks separately from genre/audience bonuses in §6.5). Calling contest_style a "supersession" of Resonant Style conflates two co-existing, differently-scoped mechanics.

**Exhaustive usage sweep.** 189 files match "Resonant Style" — sampled: `references/module_contracts.yaml:231` (gate transition text, PULLED); `references/values_master.yaml:740` (section-pointer citation only, PULLED); `designs/godot/data_serialization_spec.md:74` (`@export var primary_rs: String # Resonant Style` — a Godot field stub, no independent value list, PULLED-shaped though the spec itself is flagged stale per CLAUDE.md §6); `params/contest.md`, `params/contest_extensions.md`, `params/factions.md:34`, `designs/scene/social_contest_v30.md` (all consistent, all cite npc_behavior_v30 as source, no independent re-enumeration of the 4 values); `params/factions/npc_stance_triangles.md:18-26` (an independent restated 4-row table — Evidence/Consequence/Authority/Solidarity, matches home exactly, still a literal duplicate not an import); `designs/ui/valoria_ui_ux_v4.md` (dozens of hits, e.g. lines 351, 783, 800 — treats Resonant Style as a live UI-rendered field, consistent).

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/npcs/npc_behavior_v30.md:32-40` | CANONICAL DEFINITION | Home site. | — |
| `references/descriptor_registry.yaml:99-100` | UNCLEAR / NO CANONICAL SOURCE | The registry's own deprecation is admitted-wrong by its own later correction, yet retirement status is left standing with no positive `by_reference` entry pointing to npc_behavior_v30 §1.3 (contrast with `conv.*` at line 88, which does get a proper by_reference entry). | N/A — registry entry itself is the contradiction |
| `params/contest.md:164`, `designs/scene/social_contest_v30.md:171,176` | PULLED / REFERENCED | Explicit citation "(npc_behavior_v30.md §1.3/§6.3)"; no independent re-listing of the 4 values, only architectural cross-talk about non-double-counting. | Yes — and actively engineered around as live |
| `params/contest_extensions.md:29-39` | PULLED / REFERENCED | Header cites "from npc_behavior_system_v1.md §6"; restates *effects* (Appraise reveal thresholds) not the definition of the 4 styles themselves. | Yes |
| `params/factions/npc_stance_triangles.md:18-26` | HARDCODED DUPLICATE | Independent 4-row literal table, no import mechanism. | Yes, currently agrees (4 values, same names/descriptions) |
| `designs/godot/data_serialization_spec.md:74` | PULLED / REFERENCED (comment-only) | Bare `String` field annotated `# Resonant Style`, no enumerated values to drift. | N/A (doc itself flagged stale per CLAUDE.md §6) |
| `designs/ui/valoria_ui_ux_v4.md` (e.g. 351, 800) | HARDCODED DUPLICATE (consistent) | Restates example NPC:style pairings independently (companion commentary examples); currently consistent with home. | Yes |

**Incidental usage.** None found — "Resonant Style" is a coined term with no ordinary-English collision risk.

---

## 3. Scar / Scar count

**Home definition.** Split across two docs with an explicit hand-off:
- `designs/personal/conviction_track_v1.md` §2 (lines 32-58), status banner: `<!-- STATUS: CANONICAL — extracted from designs/npcs/npc_behavior_v30.md §1.2 + §3.3 + §3.4 -->`, authority PP-681/ED-768. **PP-718 clarification (line 34, dated 2026-05-10): "Scar accumulation is per-Conviction, not aggregate.** The thresholds below apply to Scar count *on a specific Conviction*." Table (lines 40-43): 0 Scars = default; 1 Scar = destabilizes, Decision Forks increase; 2 Scars = weight may shift, Resonant Style for that Conviction activates permanently; **3+ Scars = "Conviction crisis on X"** (d6 crisis table, lines 47-53).
- `designs/npcs/npc_behavior_v30.md` §3.3 (lines 398-402) is now a **redirect stub**: "*The Scar accumulation table… have been promoted to their own canonical doc per PP-681. See `designs/personal/conviction_track_v1.md` §2…*"

**Exhaustive usage sweep.** ≥250 files match \bScar\b (grep-capped). Key sites opened: `designs/npcs/npc_behavior_v30.md` §4.1 (lines 481-489, Decision Fork table), §5.1 (536), §9.5 Step 4 (1023-1028), §11 roster panel (1225, 1252); `designs/scene/combat_v30.md:457-458,586`; `designs/threadwork/threadwork_v30.md:115`; `designs/architecture/key_substrate_v30.md:3,107,458,514`; `designs/architecture/key_type_registry_v30.md:71,473`; `designs/architecture/player_agency_v30.md:224,344,411`; `references/module_contracts.yaml:211,240`; `designs/ui/valoria_ui_ux_v4.md:2130-2142`; `designs/npcs/character_canon_v30.md`.

**Divergence check — the significant find: aggregate vs per-Conviction model mismatch.**
`conviction_track_v1.md:34` (PP-718, dated 2026-05-10) explicitly overturns the aggregate model: *"Under PP-684 structured concentration… Scar accumulation is per-Conviction, not aggregate."* But `npc_behavior_v30.md` §4.1's Decision Fork table (lines 484-489) — in the **same document**, and never updated after this clarification — still reads as a single flat tracker:
> `| Scar count = 0 | Conviction (personal) over Framework (institutional) | ... |`
> `| Scar count = 1 | Whichever Conviction (primary or secondary) the most recent Scar did NOT address | ... |`
> `| Scar count ≥ 2 | GM uses Conviction crisis table (§3.3) | ... |`

This table has no "on Conviction X" qualifier anywhere — it reads exactly like the pre-PP-718 aggregate model the clarification explicitly retired. No editorial marker in §4.1 flags this as needing reconciliation with the later per-Conviction correction. By contrast, **`references/module_contracts.yaml:226-236` has the corrected model wired in** — its `gates` block explicitly uses `"Scars on Conviction X = 2"` / `"Scars on Conviction X >= 3"` phrasing and cites `"conviction_track_v1 §2 (PP-718 per-Conviction)"` directly (line 236) — meaning the module-contract layer (later-maintained, `[READ: 2026-06-10]` per its own sources list, line 243) has already adopted the correction that npc_behavior_v30.md §4.1 itself has not propagated back into.

**Second finding — excluded incidental usage.** `designs/threadwork/threadwork_v30.md:506,763,942` use "Scar"/"Scar Trace" to mean a **visible environmental trace left in the Thread substrate** after Mending ("Mended area retains a trace… perceive a scar in the substrate," line 506; "Scar Trace — Mended territory retains visible Thread scar," line 942) — this is a *different*, purely descriptive/environmental sense of "scar," unrelated to the Conviction-Scar mechanic. I exclude these three instances as incidental/homonymous rather than mechanical Conviction Scars.

**Third finding — properly-flagged 3-way name collision adjacent to this term.** `references/module_contracts.yaml:240` (gap_notes) independently documents: *"NAME COLLISION (3-way) [OPEN — Jordan]: substrate §8.4 'Piety Track' (this personal scar system… home designs/personal/conviction_track_v1.md) vs designs/scene/conviction_track_v30.md which is the TERRITORIAL 'Piety Track & Church Victory Redesign' (PP-406-418, CV per territory) — two different systems share both names."* Not itself the Scar term, but the tracking mechanism the Scar count lives on (Piety Track) is name-collided with an unrelated territorial system, which materially affects how confidently a reader can trust any bare "Piety Track" citation near a Scar reference.

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/personal/conviction_track_v1.md:32-58` | CANONICAL DEFINITION | Home site, PP-681/PP-718. | — |
| `designs/npcs/npc_behavior_v30.md:398-402` (§3.3) | PULLED / REFERENCED | Explicit redirect stub naming the promoted doc. | Yes (stub is accurate) |
| `designs/npcs/npc_behavior_v30.md:484-489` (§4.1) | HARDCODED DUPLICATE (stale) | Independent decision-fork table using aggregate "Scar count," not updated after PP-718's per-Conviction correction in the doc it itself redirects to. | **No** — describes the pre-PP-718 aggregate model |
| `references/module_contracts.yaml:226-236` | PULLED / REFERENCED | Gate conditions literally phrased "Scars on Conviction X," explicit citation "(PP-718 per-Conviction)." | Yes — correctly reflects PP-718 |
| `designs/architecture/key_type_registry_v30.md:473` | PULLED / REFERENCED | `description: NPC takes a Conviction Scar.` — bare Key-type description, no independent threshold restated. | Yes |
| `designs/architecture/player_agency_v30.md:224,411` | HARDCODED DUPLICATE | Independently restates "Scar count ≥ 2 (conviction crisis)" (line 224) using aggregate phrasing, same staleness as §4.1 above. | No — same aggregate-model drift |
| `designs/scene/combat_v30.md:457-458,586` | HARDCODED DUPLICATE (consistent) | Independent restatement of the death→Scar consequence; doc is `PARTIALLY SUPERSEDED` for *resolution* mechanics only (ED-900) — this is flavor/consequence content explicitly retained per its own banner. | Yes, currently consistent |
| `designs/ui/valoria_ui_ux_v4.md:2130-2142` | HARDCODED DUPLICATE | `scars: int (0-3)` and `scars_by_conviction: Dictionary<ConvictionEnum, int>` — interestingly *already* models a per-Conviction dict despite predating (2026-04-16) the PP-718 clarification (2026-05-10). | Currently consistent by coincidence, not by traceable derivation |
| `designs/threadwork/threadwork_v30.md:506,763,942` | Excluded — incidental/different meaning | "Thread scar"/"Scar Trace" = environmental residue, not Conviction Scar. | N/A |

---

## 4. Standing (per-NPC, per-faction-pair) — 3-/4-way collision cross-check

**Home definition (this batch's sense).** `designs/npcs/npc_behavior_v30.md` uses "Standing" as a **per-actor, per-faction scalar** governing institutional access/authority — e.g. "Church Standing ≥ 1" / "≥ 3" / "≥ 5" (lines 333-335), "Hafenmark grants only if the accused has Standing 0" (line 293), "Varfell Standing ≥ 3" (line 294), "the flag gates Church Standing (heretic cannot hold Standing ≥ 1)" (line 297). No numeric range is stated in npc_behavior_v30.md itself — it borrows the range from elsewhere, which is where the collision surfaces.

**Cross-check — genuinely a 3-to-4-way collision, confirmed by direct reading.**

1. **`references/glossary.md:100,110`** (module_contracts.yaml also echoes this at line ~"tracks: [...Standing...]" in descriptor_registry.yaml's not_descriptors block): *"Standing is the exception (0–10)... No in-game benefit above 7; 10 is cosmetic maximum."*
2. **`designs/provincial/faction_politics_v30.md:6,38`** (PP-660, `## Status: CANONICAL (approved Jordan 2026-04-17)`) — an explicit **redesign**: *"Replace the 0–5 Standing track with an eight-position ladder (Standing 0 through Standing 7)."* This is the per-actor-per-faction rank ladder (Skyrim-guild-style progression), and it is what npc_behavior_v30.md's NPC-level Standing references (Church/Ministry/Varfell/Hafenmark Standing) most plausibly resolve to.
3. **`designs/provincial/clock_registry_v30.md:52-53`** — self-declared `## Status: CANONICAL`, "Single source of truth for all clocks, tracks, and counters," last touched **2026-06-24** (more than 2 months *after* PP-660's 2026-04-17 redesign) — yet still lists: `| Standing | 0–5 | bg_v05 §Standing (P-15) |`, citing an old Board Game v5 doc, i.e. **exactly the pre-redesign range PP-660 says it replaced**, never updated despite the file's own recent-maintenance claim.
4. **A genuinely distinct fourth mechanic sharing the identical name and range**: `sim/personal/contest/primitives.py:31-40` — `class Standing: LO, HI, START = 0.0, 10.0, 5.0` — a **transient, per-contest ethos-build primitive**, the kernel underlying "Face" in the current contest rebuild. `designs/scene/social_contest_v30.md:236,239,252` states this explicitly: *"Face_current = round(Standing ÷ 10 × Face_max), where Standing is the unchanged kernel 0–10 ethos-built value"* and *"Face ≠ Disposition and Face ≠ Reputation: Disposition/Reputation are persistent cross-scene relationship stats; Face is a within-contest tracker that resets at contest end."* The doc is careful to disambiguate Face/Standing from persistent Disposition/Reputation — but **never disambiguates its own internal "Standing" primitive from the persistent faction-rank "Standing" it shares a name (and, coincidentally, an identical 0-10 range) with.**

**Divergence check.** Three numeric ranges attach to the persistent sense of "Standing" alone (0-5 clock_registry / 0-7 faction_politics / 0-10 glossary+module_contracts), with faction_politics_v30's redesign (2026-04-17) never propagated into clock_registry_v30 despite that file's much later maintenance touch (2026-06-24) and self-declared single-source-of-truth status. Separately, a fourth, conceptually unrelated transient contest-primitive literally named `Standing` in code (`sim/personal/contest/primitives.py`) risks being confused with the persistent NPC/faction Standing npc_behavior_v30.md references — the two mechanics are never cross-disambiguated anywhere I found, even though social_contest_v30.md goes out of its way to disambiguate Face from Disposition/Reputation specifically.

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/provincial/faction_politics_v30.md:6,38` | CANONICAL DEFINITION (for the persistent per-actor-per-faction sense) | Explicit PP-660 redesign statement. | — (0-7) |
| `references/glossary.md:100,110` | HARDCODED DUPLICATE | Independent literal range statement, 0-10, no citation of PP-660's 0-7 redesign. | **No** — disagrees with faction_politics_v30 |
| `designs/provincial/clock_registry_v30.md:52-53` | HARDCODED DUPLICATE (stale) | Independent literal range statement citing a legacy `bg_v05` doc; self-claimed single-source-of-truth, updated 2026-06-24, still not reconciled. | **No** — reproduces the pre-PP-660 0-5 range |
| `designs/npcs/npc_behavior_v30.md` (various per-faction Standing thresholds) | UNCLEAR / NO CANONICAL SOURCE | Never states which range it assumes; thresholds used (0,1,3,5,7) are compatible with any of the three ranges, so silently ambiguous. | Cannot determine |
| `designs/provincial/faction_canon_v30.md:325` | PULLED / REFERENCED | "These are Standing tracks parallel to the main faction Standing ladder" — cites faction_politics_v30 Part 2 by name. | Yes |
| `sim/personal/contest/primitives.py:31-40` + `designs/scene/social_contest_v30.md:236-253` | UNCLEAR / NO CANONICAL SOURCE (distinct mechanic, same name, unreconciled) | A genuinely different transient contest primitive, explicitly disambiguated from Disposition/Reputation but never from the persistent faction-rank Standing it shares a name with. | N/A — not the same mechanic |
| `designs/provincial/faction_canon_v30.md:420,584` ("Standing Mission") | Excluded — incidental | "Standing Mission" = a persistent/ongoing Mission, ordinary-English adjectival use of "standing," not the tracked stat. | N/A |
| `designs/provincial/faction_layer_v30.md:77,79` ("Löwenritter standing army/military force") | Excluded — incidental | "standing army" = ordinary-English military idiom, unrelated to the Standing track. | N/A |

---

## 5. Practitioner Coherence (NPC AI-gating, 0-10) — same tracker as Thread Coherence, or distinct?

**Home definition (this batch's site).** `designs/npcs/npc_behavior_v30.md` §4.3 "NPC Practitioner Coherence Decision Thresholds (ED-665)" (lines 497-513): a 6-tier table keyed to "Coherence": `10–6 Stable / 5 Dissonant / 4–3 Degraded / 2 Fractured / 1 Severed / 0 Conversion`, each with an "NPC Decision Rule" (behavioral gate, e.g. "Cease Thread operations" at 4-3). Explicitly applies "TTRPG (GM guidance) and BG/Hybrid (NPC AI)."

**Answer to the specific question posed:** this **is the same underlying tracker** as Thread Coherence — the canonical Coherence(10→0) practitioner track defined at `designs/threadwork/threadwork_v30.md` Part Three (line 602, "PART THREE: COHERENCE (10→0)"), not a separate NPC-only stat — but **npc_behavior_v30 §4.3 restates the band *boundaries and labels* independently, and they diverge from the threadwork_v30 canonical thresholds.**

**Divergence — quoted verbatim both sides.**
`designs/threadwork/threadwork_v30.md` §3.3 (lines 639-648), the canonical Coherence Thresholds table:
> `10–8 | Stable | ...` / `7–5 | Dissonant | ...` / `4–3 | Fragmented | −1D to all social rolls...` / `2 | Fractured | ...` / `1 | Severed | ...` / `0 | Rendering Crisis | Campaign event...`

`designs/npcs/npc_behavior_v30.md` §4.3 (lines 501-508), the NPC decision-gating table:
> `10–6 | Stable | Operate freely...` / `5 | Dissonant | Self-limit to defensive Thread ops only...` / `4–3 | Degraded | Cease Thread operations...` / `2 | Fractured | Seek withdrawal...` / `1 | Severed | Crisis mode...` / `0 | Conversion | NPC Transition per params_core PP-261.`

The two tables disagree at every band except "Fractured"/"Severed" at 2/1:
- **Stable band boundary**: 10-8 (threadwork) vs 10-6 (npc_behavior) — npc_behavior extends "Stable" down through Coherence 6 and 7, which threadwork classifies as "Dissonant."
- **Dissonant band**: 7-5 (threadwork, 3 points) vs 5-only (npc_behavior, 1 point) — same label, different width.
- **4-3 band label**: "**Fragmented**" (threadwork) vs "**Degraded**" (npc_behavior) — same numeric band, different name.
- **0 band label**: "**Rendering Crisis**" (threadwork, applies to PCs — "Reality as commonly rendered is no longer accessible… If unresolved by season end: Non-Player Character") vs "**Conversion**" (npc_behavior, citing `params_core PP-261`).

Checking that PP-261 citation: `params/core.md:82-83` — *"## Coherence 0 — NPC Transition (PP-261): At Coherence 0: character becomes NPC (100% functional, player agency ends)."* This is specifically a **PC→NPC conversion rule** (a player character losing agency and becoming a non-player character) — npc_behavior_v30 §4.3 reuses this exact citation to describe what happens when an NPC (already an NPC) hits Coherence 0, without clarifying what "NPC Transition" even denotes for an actor that is not a PC. This is a citation applied outside its defined scope, not merely a relabeling.

**Independent corroborating evidence of the drift**: `tests/sim/sim_batch_5_2026-04-16.md:244` (and other stress-test material) uses **"Fragmented"** — the threadwork label — for the 4-3 band when discussing practitioner Coherence Ob modifiers, i.e. the corpus's own test material follows threadwork_v30's labeling, not npc_behavior_v30's "Degraded" relabeling, showing the divergence is live and inconsistently propagated even within test/stress documentation.

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:639-648` | CANONICAL DEFINITION | Home site for the Coherence(10→0) tracker itself. | — |
| `designs/npcs/npc_behavior_v30.md:497-513` | HARDCODED DUPLICATE | Independently restates band boundaries/labels for NPC-AI-gating purposes rather than importing threadwork_v30's table; explicitly named "NPC Practitioner Coherence Decision Thresholds" as if a distinct spec. | **No** — boundaries and labels diverge at 4 of 6 bands |
| `params/core.md:82-83` (PP-261) | CANONICAL DEFINITION (of NPC Transition, PC-scoped) | Home site for the Coherence-0 PC→NPC conversion rule. | — |
| `designs/npcs/npc_behavior_v30.md:508` ("Conversion... per params_core PP-261") | HARDCODED DUPLICATE (mis-scoped) | Cites a PC-scoped rule to describe an NPC-scoped outcome, without adaptation. | Ambiguous — the citation doesn't actually define NPC-side behavior |
| `tests/stress/thread/threadwork_stress_test_batch5.md:244` | HARDCODED DUPLICATE (consistent with threadwork, not npc_behavior) | "Practitioner Coherence Fragmented (4–3): +1 Ob = 8" — uses threadwork's "Fragmented" label. | Agrees with threadwork_v30, disagrees with npc_behavior_v30's relabeling |
| `references/wc_survival_spine.md:67` | PULLED / REFERENCED (loosely) | Names "Practitioner Coherence" as a resource-tension row; a later sim finding (`tests/sim/sim_mending_coherence_2026-04-17.md:141,152`) flags this row as "now partially wrong" (Mending no longer competing for Coherence budget) — an independently-noted staleness. | Partially stale, separately flagged |
| `designs/npcs/character_canon_v30.md:265` | PULLED / REFERENCED | "Per-NPC Coherence baselines exist for some named NPCs (Edeyja: 9)… `[ASSUMPTION: default 8 Stable]`" — consumes the Coherence scale without restating band thresholds. | Yes |

---

## 6. Leadership Deviation Ob

**Home definition.** `designs/npcs/npc_behavior_v30.md` — introduced per-NPC throughout §2 (e.g. Almud: 2, line 62; Confessor Arne: 3, "highest," line 83; Baralta: 1, "lowest — she IS the institution," line 103; Vaynard: 2, line 124; Ehrenwall: 2, line 145; Vossen: 2, line 164; Haelgrund: 1, line 317), consumed mechanically in the §4.1 Decision Fork table (lines 484-489: "Leadership Deviation Stability check at next accounting" / "Leadership Deviation if Framework-contradicting"). No single formula is given — it is an authored per-NPC Ob value representing the cost of an NPC deviating from institutional Framework toward personal Conviction.

**Faction-default companion table.** `params/factions/stats_1_7_scale.md:145-147` — "## Leadership Deviation Stability Check Obs": `Crown: 2 | Church: 3 | Hafenmark: 2 | Varfell: 2 | Guilds: 2 | Restoration Movement: 2 | Löwenritter: 2`.

**Divergence — direct numeric conflict.** Cross-checking per-NPC values against this faction-default table: Crown(Almud)=2 matches; Church(Himlensendt)=3 matches; Varfell(Vaynard)=2 matches; Löwenritter(Ehrenwall)=2 matches; Restoration(Vossen)=2 matches — **but Hafenmark=2 in the faction-default table directly conflicts with Baralta's explicitly-authored Leadership Deviation Ob of 1** (`npc_behavior_v30.md:103`, restated again at line 612: *"Leadership Deviation Ob still 1 (she IS the institution — the institution follows her, not the other way around)"*). The npc_behavior_v30.md text narratively justifies this as an intentional special case, but `params/factions/stats_1_7_scale.md:147` gives no footnote acknowledging Baralta/Hafenmark as an exception to its own default-value table — a reader consulting only the params table would get the wrong number for the single most narratively load-bearing instance of this stat in the corpus.

**A second, unadopted rename proposal** (same file flagged for Term 1): `designs/architecture/canonical_registry.md:221` — "COMPLETE RENAME TABLE": `| Leadership Deviation Ob | **Authority Challenge Ob** | Clearer |`. Dated 2026-04-15, never adopted anywhere else in the corpus (I grepped and found zero live uses of "Authority Challenge Ob"); the file's only currency banner scopes itself to combat rows, leaving this table's status ambiguous by omission.

**Companion-NPC values in a separate but complementary doc (not a divergence, but a distributed-canon risk):** `designs/arcs/arc_expansion_v30.md` supplies Leadership Deviation Ob values for NPCs npc_behavior_v30.md itself doesn't give one for directly (Cardinal of Justice=5, line 246; Cardinal of Prudence=1, line 289; Cardinal of Temperance=2, line 330; Jarnstal=1, line 431) — npc_behavior_v30.md §5.2 (line 547) explicitly names arc_expansion_v1 as "the canonical source for… Cardinal Officers," so this is properly-distributed canon, not an unflagged duplicate — but it means the Leadership Deviation Ob for roughly a third of named NPCs lives *only* in arc_expansion_v30.md and not in npc_behavior_v30.md's own per-NPC tables, a fact a reader consulting only npc_behavior_v30.md for a Cardinal's value would miss.

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/npcs/npc_behavior_v30.md` (per-NPC values, e.g. lines 62,83,103,124,145,164,317) | CANONICAL DEFINITION | Per-NPC authored values, home site. | — |
| `params/factions/stats_1_7_scale.md:145-147` | HARDCODED DUPLICATE | Independent literal per-faction default table, no cross-reference to npc_behavior_v30's per-NPC exceptions. | **No for Hafenmark** (2 vs Baralta's explicit 1); yes for the other 6 factions |
| `designs/architecture/canonical_registry.md:221` | HARDCODED DUPLICATE (unadopted rename proposal) | Independent rename table, never adopted. | N/A |
| `designs/arcs/arc_expansion_v30.md:204,246,289,330,397,411,431` | CANONICAL DEFINITION (for NPCs not covered by npc_behavior_v30 directly) | npc_behavior_v30.md §5.2 explicitly designates arc_expansion_v1 canonical for these NPCs. | — (complementary, not divergent) |
| `tests/sim/*.md` instances (e.g. `sim_companions_2026-04-16.md:99,397,415`, `sim_arc_g01_g05_capitals.md:36`) | PULLED / REFERENCED | Consume the authored per-NPC values in simulation prose; no independent re-derivation. | Yes |

**Incidental usage.** None — "Leadership Deviation Ob" is a fully coined compound term with no ordinary-English collision.

---

## 7. Roster tier

**Home definition.** `designs/npcs/npc_behavior_v30.md` §11 "Named NPC Roster Tracking Capacity (PP-661)" (lines 1217-1258). Three tiers: **Active** (tracked: Disposition/PC, Availability, active-Duty ref, Scar count, action flag; soft cap **~35**, line 1231), **Passive** (Disposition + Availability only; line 1226), **Background** (identity only, unlimited; line 1227). §11.6 (line 1256): *"Capacity at these weights: ~35 Active + ~30 Passive + unlimited Background."*

**Exhaustive usage sweep.** Consistent restatement at `designs/arcs/throughline_resolutions_v30.md:258,277,282-284` (same 35/30 language, same tier names, dated same day 2026-04-17 as PP-661's own approval — this is essentially the doc PP-661 was extracted from/into, so treat as a paired canonical source, not a duplicate); `designs/npcs/character_canon_v30.md:349` (bare citation, "Per npc_behavior_v30 §11 (PP-661)"); `designs/territory/settlement_layer_v30.md:63` uses "PP-661" for a *different* mechanic (Institutional Facility Tiers) — same patch ID, unrelated subject, worth noting as a PP-ID-reuse-for-two-different-mechanics wrinkle but not a term collision on "Roster tier" itself.

**Divergence — a previously-identified, independently-confirmed numeric drift.** `designs/audit/2026-07-05-emergent-narrative-engine/01_workings/dossier_combinatorial_census.md:80-96` (a prior corpus audit) already found and I independently verified by direct read:
> *"A further drift: `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md` lines 136-137 give the Passive cap as **~50**, not ~30 — a second, unreconciled version of the same PP-661 number living in an older audit doc."*

I opened the cited file directly and confirmed verbatim: `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md:128,136-139`:
> `System scope: ~35 named Active NPCs + ~50 named Passive NPCs + statistical population NPCs.`
> `| **Passive** | ~50 named NPCs (parish priests, settlement mayors, junior officers) | Lite architecture... |`
> `| **Population** | All others | Statistical only... |`

This doc also uses a **third tier name** — "Population" instead of "Background" — for the unlimited-identity-only tier, i.e. it independently re-derives the whole 3-tier stratification concept with a different Passive cap (50 vs 30) and a different name for the third tier, without citing or reconciling against npc_behavior_v30.md §11 even though it postdates PP-661's approval window and is clearly discussing the same design space (Active/Passive/unlimited-background NPC tracking cap).

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/npcs/npc_behavior_v30.md:1217-1258` | CANONICAL DEFINITION | Home site, PP-661. | — |
| `designs/arcs/throughline_resolutions_v30.md:258,277,282-284` | HARDCODED DUPLICATE (consistent, paired-canon) | Independent literal restatement, same numbers/names, same-day patch. | Yes |
| `designs/npcs/character_canon_v30.md:349` | PULLED / REFERENCED | Bare citation "Per npc_behavior_v30 §11 (PP-661)," no independent numbers restated. | Yes |
| `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md:128,136-139` | HARDCODED DUPLICATE | Independent literal restatement with a different Passive-tier cap (50) and a third-tier renamed "Population." | **No** — Passive cap disagrees (50 vs 30); tier-3 name disagrees (Population vs Background) |
| `tools/observability/DECISIONS.md:1729` | UNCLEAR / NO CANONICAL SOURCE (self-flagged) | `[ASSUMPTION: Tier-1 vs Tier-2 vs Tier-3 NPC tracking from npc_behavior §11 reflects current intent — basis: PP-661 spec; verify against current player-facing roster decisions.]` — an explicit hedge already present in the corpus. | Flagged as unverified by its own author |

**Incidental usage.** None — "roster tier" is fully game-mechanical throughout the sampled sites.

---

## 8. Hooks

**Home definition.** `designs/npcs/npc_behavior_v30.md` §9.5 "NPC RECRUITMENT PROCEDURE (PP-642)," subsection "### Hooks" (lines 1030-1041). **Weak Hook**: "Suggestive but not irrefutable leverage… −2 Ob on recruitment… not burned" if it fails (line 1033). **Strong Hook**: "Irrefutable leverage… Reduces recruitment Ob to 1… burned" on failed use, with "recruiting faction takes Mandate −2" (line 1035). Acquisition: "Tribune Spy Overwhelming on NPC's territory → Weak Hook" or narrative GM decision (lines 1037-1039). "Hooks are tracked on the NPC's entry in the NPC roster. Maximum one Hook per NPC at a time" (line 1041).

**Exhaustive usage sweep.** `designs/architecture/complete_systems_reference.md:121` and its byte-identical twin `references/valoria_complete_systems_r2.md:121` both compress the same formula ("Offer... Strong Hook → Ob 1"); `designs/arcs/arc_expansion_v30.md:304-305` gives worked examples ("Guilds gain a Strong Hook on Tormann"; "discovering Tormann's embezzlement... gives the player a Weak Hook"), consistent with home; `tests/sim/sim_faction_ambition_2026-04-16.md:427` and `designs/audit/2026-06-22-npc-comprehensive-audit.md:2270-2271` reference the same concept consistently.

**Divergence / gap findings.**
1. **The claimed storage location does not actually exist.** npc_behavior_v30.md:1041 asserts "Hooks are tracked on the NPC's entry in the NPC roster" — I grepped `designs/npcs/npc_roster_v30.md` for "hook" and found **zero occurrences**. The roster file that is supposed to carry this per-NPC field contains no trace of it. This is not a value-divergence but a claimed-cross-reference that doesn't resolve to any actual data location in the design corpus — an UNCLEAR/NO CANONICAL SOURCE case for the storage mechanism specifically (the mechanic's *rules* are canonical; its *data home* is not).
2. **No module-contract registration.** I grepped `references/module_contracts.yaml` and `references/descriptor_registry.yaml` for "hook" and found zero hits in either — Hooks have no formal data-model/contract entry anywhere in the registry layer, unlike most other tracked NPC state (Disposition, Scar count, Standing all appear in `descriptor_registry.yaml`'s `not_descriptors` tracks list or `module_contracts.yaml`).
3. **Duplicate-file risk already flagged elsewhere in corpus.** `designs/architecture/complete_systems_reference.md` and `references/valoria_complete_systems_r2.md` are literal duplicates of each other (confirmed via matching banner text: the latter's header explicitly says `## Status: PARTIALLY SUPERSEDED (combat sections) + DUPLICATE COPY` and "⚠️ DUPLICATE COPY (2026-07-01, ED-1084). This file duplicates..." — already self-acknowledged, not a new finding, but it means the Hooks restatement at line 121 exists as two copies of one hardcoded duplicate, not two independent ones).

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/npcs/npc_behavior_v30.md:1030-1041` | CANONICAL DEFINITION | Home site, PP-642. | — |
| `designs/architecture/complete_systems_reference.md:121` | HARDCODED DUPLICATE | Independent compressed literal restatement of the formula. | Yes |
| `references/valoria_complete_systems_r2.md:121` | HARDCODED DUPLICATE (self-flagged as a duplicate-copy of the previous row) | Byte-identical text; file self-declares `DUPLICATE COPY` per ED-1084 banner. | Yes (same text) |
| `designs/arcs/arc_expansion_v30.md:304-305` | PULLED / REFERENCED (worked example) | Applies the mechanic to specific NPCs without restating the Ob-modifier rules. | Yes |
| `designs/npcs/npc_roster_v30.md` (expected but absent) | UNCLEAR / NO CANONICAL SOURCE | npc_behavior_v30.md claims this is the storage site; zero "hook" hits found there. | N/A — claimed cross-reference does not resolve |
| `references/module_contracts.yaml`, `references/descriptor_registry.yaml` (absent) | UNCLEAR / NO CANONICAL SOURCE | No registry/contract entry for Hooks at all. | N/A |

**Incidental usage.** I excluded ordinary uses of "hook" as a narrative-writing term (e.g. "story hook," "plot hook" in prose-writer skill references) and as Claude-Code/git tooling hooks (`.claude/settings.json`, `.githooks/`) — none of those are the NPC-recruitment-leverage mechanic and are unrelated homonyms.

---

## 9. significance() and significance_universal (articulation)

**Home definition.** `designs/articulation/articulation_layer_v30.md` §3.2 "Significance function" (lines 125-137):
```
significance(key) =
    stakes_weight(key)                    # 1-5
  + protagonist_alignment(key)            # 0-3
  + cascade_event_weight(key)             # 0-2
  + accumulated_narrative_weight(key)     # 0-3
```
Range 0-13; cut-scene length scales 5s/10s/15s by score band (line 137). §4.3 "Significance function for Tier 3" (lines 207-216) defines **significance_universal**:
```
significance_universal(key) =
    stakes_weight(key)
  + cascade_event_weight(key)
  + accumulated_narrative_weight(key)
```
— the same formula minus the `protagonist_alignment` term, explicitly labeled "no protagonist_alignment term" (line 209).

**Important caveat on the home document's own currency status** — independently confirmed via a same-day (2026-07-08) prior audit I cross-checked by direct read (`designs/audit/2026-07-08-crunch-cascade-cogload-legibility-audit/01_findings_articulation_npc_behaviour.md:3-5`): *"Canonical heads: `designs/articulation/articulation_layer_v30.md` (**self-contradicting status lines: CANONICAL at L6, PROVISIONAL at L2/L9/L363** — confirmed verbatim, unresolved by CURRENT.md)."* I verified this directly: line 6 says `## Status: CANONICAL`; line 2 says `STATUS: PROVISIONAL — Class A canonical document`; line 9 says `**Status:** PROVISIONAL.`; line 363 says `**End spec. PROVISIONAL pending ratification.**` This is a genuine, internally self-contradicting currency status on the very document I am treating as the home site for this term — worth flagging prominently since it undermines confidence in calling anything here unambiguously "canonical" pending Jordan resolution.

**Exhaustive usage sweep and divergence.**
1. `designs/architecture/key_type_registry_v30.md:965,988,1009,1029` and `designs/provincial/political_dynamics_keys_migration_v30.md:453,478,500,521` declare `articulation_significance: stakes_weight X-Y` annotations per new Key type — these supply *inputs* to the canonical `stakes_weight()` term, not independent restatements of the significance formula itself. PULLED/REFERENCED.
2. `designs/audit/2026-05-01-stage-10-validation/sims/stage10_articulation_sim.py:320-340` implements `significance_t2()` and `significance_t3()` — functionally faithful ports of `significance()`/`significance_universal()` (docstrings explicitly cite "§3.2 + §3.5 K/B/I bumps" and "§4.3 ... no protagonist alignment term," lines 321,334) — legitimate PULLED/REFERENCED reference implementation.
3. **But this same reference-implementation file is stale relative to the current spec on an adjacent, directly-coupled mechanism**: its `trigger_match()` function (lines 342-359) is explicitly commented `"# 8-trigger predicates per §3.1"` and implements exactly 8 trigger conditions (scar_acquired, coup_attempted, succession, mission_shift, covert_betrayal, knot_formed, knot_ruptured, peninsular_strain_shock) — but the *current* `articulation_layer_v30.md` §3.1 (lines 77-92) has **10 triggers**, having added Trigger 9 (cascade clustering) and Trigger 10 (`state.belief_revised`) on 2026-05-01/05-02. Since `significance()`/the cut-scene pipeline only fires *after* `trigger_match()` succeeds (per §5 pseudocode, line 256, and confirmed independently by the 2026-07-04 NERS audit dossier I cross-checked, `designs/audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_articulation.md:44-52`), the very sim that "validated" this document's promotion to CANONICAL (the doc's own header: "promoted from PROVISIONAL after Stage 10 sim PASS, 12/14 battery") **never actually exercised the current 10-trigger ruleset** — it validated an 8-trigger predecessor. This is a genuine validation-basis/spec drift on the mechanism the significance functions feed into.
4. **A previously-identified, independently-confirmed functional gap directly touching `significance()`**: the same 2026-07-04 and 2026-07-08 audits (both cross-checked by direct read) found: *"§3.3's `unarticulated_weight` accumulator is claimed to prevent an NPC whose Keys never match one of the ten §3.1 trigger types from going permanently unrendered... Tracing the actual §5 pseudocode: the accumulator only feeds `accumulated_narrative_weight`, one term inside `significance()` — and `significance()` is computed only after `matches_trigger_ruleset(key)` already succeeded. There is no code path by which accumulated weight alone can cause a non-matching Key to fire."* (`01_findings_articulation_npc_behaviour.md:22-30`; corroborated near-verbatim at `dossier_articulation.md:44-52`.) This is treated in more depth under Term 10 below since it's really an `unarticulated_weight` finding, but it materially bears on what `significance()`'s `accumulated_narrative_weight` term can and cannot do.

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/articulation/articulation_layer_v30.md:125-137,207-216` | CANONICAL DEFINITION | Home site — but self-contradicting Status lines (CANONICAL vs PROVISIONAL) within the same doc. | — |
| `designs/architecture/key_type_registry_v30.md:965,988,1009,1029` | PULLED / REFERENCED | `articulation_significance: stakes_weight X-Y` — supplies one input term, no independent formula restated. | Yes |
| `designs/provincial/political_dynamics_keys_migration_v30.md:453,478,500,521` | PULLED / REFERENCED | Same mechanism as above, different Key types. | Yes |
| `designs/audit/2026-05-01-stage-10-validation/sims/stage10_articulation_sim.py:320-340` | PULLED / REFERENCED (faithful port) | Docstrings explicitly cite §3.2/§3.5/§4.3; functionally equivalent formula, cosmetic rename (`significance_t2`/`significance_t3`). | Yes, for the formula itself |
| `designs/audit/2026-05-01-stage-10-validation/sims/stage10_articulation_sim.py:342-359` (`trigger_match`) | PULLED / REFERENCED but STALE | Explicitly implements only 8 of the current 10 triggers; the validation basis for the doc's CANONICAL promotion predates triggers 9-10. | **No** — lags current spec by 2 trigger types |
| Prior-audit findings I cross-checked (`01_findings_articulation_npc_behaviour.md`, `dossier_articulation.md`) | (not a corpus "usage" site, but a verification source I independently confirmed) | Direct-read confirmed both the Status self-contradiction and the trigger-gating gap. | Confirmed accurate on both points |

---

## 10. unarticulated_weight

**Home definition.** `designs/articulation/articulation_layer_v30.md` §3.3 "Accumulated narrative weight" (lines 139-153):
```
on_key_emitted(key):
    for actor in key.targets:
        actor.unarticulated_weight += stakes_weight(key)

# at trigger fire:
weight = actor.unarticulated_weight
actor.unarticulated_weight = 0
```
Stated purpose (line 141): "Effect: if a Bonded NPC accumulates many low-stakes Keys with no cut scene fired, eventually a routine Key triggers a higher-significance cut scene." Consumed inside `significance()`'s `accumulated_narrative_weight` term (§3.2) and reset on cut-scene fire (§5 pseudocode, line 259: `reset_unarticulated_weight(key.targets)`).

**Exhaustive usage sweep.** Live design/audit sites: `designs/audit/2026-07-05-emergent-narrative-engine/01_workings/arch_A_minimal_detector.md:213`, `refute_determinism_replay.md:70`, `arch_B_arc_vector_engine.md:193,214`, `refute_veto_and_drift.md:132`, `spec_sections/s2_q3_arcs.md:298`, `arch_C_director_layer.md:142,200`, `00_grounding/02_prose_render_stack.md:35` — a whole downstream design-exploration effort (a proposed "Director layer"/"Arc vector engine") treats `unarticulated_weight` as an existing, load-bearing primitive to build on top of, e.g. `arch_C_director_layer.md:142`: "Rides `articulation §3.3`'s per-actor `unarticulated_weight` starvation accumulator." Reference implementation: `designs/audit/2026-05-01-stage-10-validation/sims/stage10_articulation_sim.py:373-388` (`run_articulation_pass`, faithfully accumulates and resets per §3.3).

**Divergence — a confirmed functional contradiction between the mechanic's stated purpose and its actual wiring**, independently found by two separate recent audits and independently re-verified by me via direct read of the cited pseudocode:

`designs/audit/2026-07-08-crunch-cascade-cogload-legibility-audit/01_findings_articulation_npc_behaviour.md:22-30` ("Cascade check — the Bonded-NPC starvation path"):
> *"Confirmed as a genuine, unflagged control-flow gap, control-flow trace independently verified. §3.3's `unarticulated_weight` accumulator is claimed to prevent an NPC whose Keys never match one of the ten §3.1 trigger types from going permanently unrendered ('eventually a routine Key triggers a higher-significance cut scene'). Tracing the actual §5 pseudocode: the accumulator only feeds `accumulated_narrative_weight`, one term inside `significance()` — and `significance()` is computed only after `matches_trigger_ruleset(key)` already succeeded. There is no code path by which accumulated weight alone can cause a non-matching Key to fire."*

`designs/audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_articulation.md:44-52` (independently, three days earlier):
> *"§3.3 prose: 'if a Bonded NPC accumulates many low-stakes Keys with no cut scene fired, eventually a routine Key triggers a higher-significance cut scene.' But the only emission gate is `matches_trigger_ruleset(key)` (§5 pseudocode, L256); `unarticulated_weight` is consumed purely as an additive term inside `significance()` (§3.2, `accumulated_narrative_weight`) — it can only raise the significance score of an already-firing trigger, never cause a non-matching Key to fire one. A background Bonded NPC whose Keys never intersect one of the 10 §3.1 types can accumulate unboundedly and will never receive a cut scene under the stated mechanism. This reads as a genuine spec/implementation gap inside the canonical doc, not an intentional simplification (no `[ASSUMPTION]` or Jordan-vetoable flag on it...)."*

I independently traced articulation_layer_v30.md's own §5 pseudocode (lines 253-268) and confirmed this reading is correct: `on_key_emitted_articulation(key)` calls `matches_trigger_ruleset(key)` as the sole gate for `emit_cut_scene`/`reset_unarticulated_weight`; the `else` branch (line 261) only calls `accumulate_unarticulated_weight(key)` — there is no code path anywhere in the pseudocode where accumulated weight alone, absent a trigger match, causes a cut-scene emission. §3.3's own prose describing the mechanism ("a routine Key triggers a higher-significance cut scene," line 141) is not literally false if read as "a routine Key that *also happens to match a trigger*," but the plain-language framing ("eventually... triggers") strongly implies a starvation-escape-valve that the wiring does not provide.

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/articulation/articulation_layer_v30.md:139-153,253-268` | CANONICAL DEFINITION | Home site — internally, the §3.3 prose promise and the §5 pseudocode wiring do not match each other (see divergence above), a self-inconsistency within the canonical doc itself, not a cross-file duplicate issue. | — |
| `designs/audit/2026-05-01-stage-10-validation/sims/stage10_articulation_sim.py:373-388` | PULLED / REFERENCED (faithful port of the actual wiring, not the prose promise) | Implements exactly the gated behavior (accumulate else-branch, reset on trigger-fire) — i.e. faithfully reproduces the mechanism as wired, which is the version that does *not* deliver the anti-starvation guarantee. | Yes, to the (gapped) implementation |
| `designs/audit/2026-07-05-emergent-narrative-engine/01_workings/arch_C_director_layer.md:142,200` and sibling dossier files | PULLED / REFERENCED | Cite `articulation §3.3`'s accumulator as an existing primitive to extend; do not re-litigate the gap (built on top of it, treating it as functioning as advertised in places). | Assumes the prose promise holds; some sibling docs in the same audit set (see below) explicitly flag that it doesn't |
| Prior-audit findings (`01_findings_articulation_npc_behaviour.md:22-30`; `dossier_articulation.md:44-52`) | (verification sources, independently re-confirmed by my own pseudocode trace) | Both independently identify the same control-flow gap; I confirm the underlying pseudocode trace is accurate. | Confirmed accurate |

---

## 11. awareness (the articulation Key field)

**Home definition — and a genuine circular/cross-attributed citation.** `designs/articulation/articulation_layer_v30.md` §5.1 "Awareness update" (lines 272-274):
> *"Per PP-687 §4.1 step 7: when a Key has `causes[]`, each cause Key's `awareness` field increments (`+0.1` clamped 0–1). High awareness on a cause Key indicates 'this earlier Key has been recently woven into a chain'; significance computation reads awareness as part of stakes_weight."*

This attributes the mechanism to **PP-687** (the Key-substrate patch). But the actual pseudocode implementing it lives in `designs/architecture/key_substrate_v30.md:214-217`:
```
    # 7. Awareness update for caused Keys (PP-688 §6 extension)
    for cause_id in key.causes:
        cause_key = KEY_LOG.lookup(cause_id)
        cause_key.awareness = clamp(cause_key.awareness + 0.1, 0, 1)
```
— and the substrate document's own inline comment labels this step **"(PP-688 §6 extension)"**, i.e. attributes authorship to PP-688 (the articulation layer itself), not PP-687. So the two canonical documents cross-attribute the same mechanism to each other: articulation_layer_v30.md says "Per PP-687," while the literal step-7 pseudocode inside key_substrate_v30.md (which articulation_layer_v30.md is citing) says the step exists there specifically *because* PP-688 extended it. This is plausibly resolvable as "step 7 is a positional citation within PP-687's numbered procedure, into which PP-688 was folded" (i.e., not strictly a contradiction, just an easily-misreadable citation direction) — but as written, a reader following articulation_layer_v30.md's citation to "PP-687 §4.1 step 7" would reasonably conclude the substrate itself originated the awareness field, when the substrate's own comment says the opposite. I flag this as worth resolving rather than asserting it is definitely wrong.

**Exhaustive usage sweep.** The bare English word "awareness" occurs in 183 files (mostly incidental — "Thread awareness," "player awareness," ordinary usage — see disambiguation below). The specific mechanical field/mechanism is far narrower:
- `designs/architecture/key_substrate_v30.md:217` — CANONICAL pseudocode site (the actual implementing code).
- `designs/audit/2026-05-01-stage-8-sim/sims/pp_phase_b_stage_8_sim.py:134` and `pp_phase_b_stage_8b_sim.py:134` — both contain the identical line `kk.awareness = min(1.0, kk.awareness + 0.1)`, a faithful reference-implementation port (note: uses `min(1.0, ...)` rather than the spec's `clamp(...,0,1)` — functionally equivalent since awareness only ever increases via this code path, so the floor-clamp is dead code in this direction, not a divergence in outcome).
- `designs/audit/2026-06-28-narrative-state-articulation/00_key_io_review.md:48` — `KEY_LOG[c].awareness = clamp(+0.1, 0, 1)` — this line is subtly different from the canonical formula: it clamps `+0.1` as an absolute value rather than `cause_key.awareness + 0.1` as an increment — i.e., as literally written this would *reset* awareness to a flat 0.1 rather than *increment* it by 0.1. This reads as a probable transcription slip in an audit working-doc rather than a deliberate mechanic change (the surrounding prose in that file otherwise describes the same "+0.1 per causal reference" mechanic), but as a literal string it is a divergence from the canonical increment formula.

**Divergence check summary.** (a) The PP-687-vs-PP-688 authorship cross-citation, flagged above for Jordan-level resolution rather than asserted as definitely broken. (b) The `pp_phase_b_stage_8_sim.py`/`8b_sim.py` port's `min(1.0, ...)` vs canonical `clamp(...,0,1)` — functionally identical given awareness is monotonically increasing in this code path, not a live risk. (c) `00_key_io_review.md:48`'s literal `= clamp(+0.1, 0, 1)` (assignment, not increment) — a literal-text divergence from the canonical `+=`-style formula, most likely a documentation transcription error rather than an intended alternate mechanic, but I did not find anything in that file explicitly flagging it as a typo, so I report it as-is.

**Step 4 — classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/architecture/key_substrate_v30.md:214-217` | CANONICAL DEFINITION | The actual pseudocode implementing the field; inline-commented "(PP-688 §6 extension)." | — |
| `designs/articulation/articulation_layer_v30.md:272-274` (§5.1) | CANONICAL DEFINITION (companion) / citation ambiguity | Cites "Per PP-687 §4.1 step 7" for the same mechanism the substrate doc's own comment attributes to PP-688 — a cross-attribution worth Jordan-level resolution, not confidently classifiable as either "wrong" or "fine." | — |
| `designs/audit/2026-05-01-stage-8-sim/sims/pp_phase_b_stage_8_sim.py:134` | PULLED / REFERENCED (faithful port, cosmetic clamp-direction difference) | `kk.awareness = min(1.0, kk.awareness + 0.1)` — functionally equivalent given monotonic increase. | Yes |
| `designs/audit/2026-05-01-stage-8-sim/sims/pp_phase_b_stage_8b_sim.py:134` | PULLED / REFERENCED (identical to above) | Same line, same file pair. | Yes |
| `designs/audit/2026-06-28-narrative-state-articulation/00_key_io_review.md:48` | HARDCODED DUPLICATE (literal-text divergence) | `KEY_LOG[c].awareness = clamp(+0.1, 0, 1)` — assignment rather than increment as literally written. | **No, as literally written** (assignment vs increment); likely a transcription slip, not confirmed intentional |

**Disambiguation of incidental usage.** The large majority of the 183 "awareness" hits are ordinary/adjacent-but-different usages I excluded from the mechanical-field analysis above: "Thread awareness" / "practitioner awareness of the substrate" (a narrative/perceptual-state concept in threadwork_v30.md, fieldwork_v30.md, miraculous_event_v30.md, conviction_track_v30.md — related to Thread Sensitivity/Certainty, not the Key `.awareness` field), "player awareness" (UX/legibility discussions in valoria_ui_ux_v4.md/v4_1.md), and general-English "awareness" in audit prose (e.g., "raise awareness of this gap"). None of these are the specific `Key.awareness` float field defined in key_substrate_v30.md §5.1/PP-688 §6, and I did not count them toward the divergence analysis above.
