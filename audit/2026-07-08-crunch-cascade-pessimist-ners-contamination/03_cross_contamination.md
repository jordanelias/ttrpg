> ⚠️ **CURRENCY NOTE — read `../00_workplan.md`'s "CURRENCY DISCLOSURE" section first.** A
> concurrent, more rigorous sibling audit (`designs/audit/2026-07-08-attribute-value-coherence-audit/`,
> ED-IN-0029) covers almost this entire document's territory with an 88-quantity census and a
> critic funnel, and has already been through a Jordan ratification pass that fixed several of the
> items below (glossary Health/Stamina rows, MS 72→60, broken param indexes, clock-registry Torben
> value, and more — see the workplan's hygiene-batch list). **Treat ED-IN-0029 as authoritative for
> naming/quantity coherence; treat every row below as a hypothesis to re-verify, not a confirmed
> live defect.** The genuinely additive rows not covered by ED-IN-0029 are called out in the
> workplan's disclosure (Interaction Type, the larger live-RS-usage finding, and others).

I have verified all the load-bearing claims directly against the working tree. I now have enough to synthesize the definitive document. Returning it as my final response.

---

# Valoria Cross-Contamination Map — Definitive Synthesis

**Scope:** every glossary term, attribute, or derived score whose definition, range, formula, or meaning is inconsistent, collided, or drifted across the corpus. Synthesized from 10 exhaustive usage-sweep batches plus direct re-verification of every striking claim against the working tree at `/home/user/ttrpg` (2026-07-08).

**Currency baseline used for adjudication** (from `CURRENT.md`, last reconciled 2026-07-08): personal-combat head = `designs/scene/combat_engine_v1/`; social-contest head = `designs/scene/social_contest_v30.md` + `params/contest.md` (contest_rebuild kernel at `sim/personal/contest/`); dice head = `params/core.md`; threadwork head = `designs/threadwork/threadwork_v30.md`; the glossary's own header claims content "last swept 2026-04-30, PP-691" — **that date is the single most important fact in this document**: it predates CR3 (2026-06-01), ED-899, ED-694's derived-stat rewrites, PP-234's genre restructure, and the entire contest rebuild, so the glossary is structurally guaranteed to be stale on every post-April-2026 mechanic even though its top-of-file "Last updated: 2026-07-01" line implies otherwise (that touch only repaired a maintenance pointer, ED-1084).

**Verification legend for the table's Status column:**
- **KNOWS-RIGHT** — glossary already flags the collision and is currently accurate.
- **KNOWS-STALE** — glossary flags the term but its content has silently regressed against live canon.
- **PARTIAL** — glossary knows part of the collision but misses another live side of it.
- **NEW** — glossary has no entry / no awareness of the collision at all.

---

## 1. Summary table

| # | Term(s) | Distinct meanings / values found | Files involved (representative) | Severity | Status |
|---|---|---|---|---|---|
| 1 | **Attribute roster** | **7** (Agility/Attunement/Cognition/Endurance/Presence/Spirit/Strength) vs **9** (…Focus/Acuity/Will/Charisma/Bonds) vs **10** (adds **Recall**) vs **7** (alias_registry copy) | `glossary.md:33-41`, `descriptor_registry.yaml:30-44`, `params/core.md:138-145`, `alias_registry.yaml:26-61`, `names_index.yaml:44-53` | **P1** | PARTIAL (glossary flags 7-vs-9; does **not** know the params/core.md 10-roster or "Recall") |
| 2 | **Cognition / Acuity** | descriptor_registry primary = **Acuity** (`[ASSUMPTION]`); every live formula = **Cognition** | `descriptor_registry.yaml:39`, `params/core.md:143,244`, `mass_battle_v30.md:266`, `fieldwork_v30.md:82` | P2 | PARTIAL (under IN-FLUX banner; zero downstream adoption of "Acuity") |
| 3 | **Presence / Charisma** | glossary + alias_registry = **Presence**; descriptor_registry + params/core.md + **all live formulas** = **Charisma** (rename PP-234, already executed) | `glossary.md:39,121`, `alias_registry.yaml:47-51`, `params/core.md:144`, `params/contest.md:3`, `social_contest_v30.md`, `mass_battle_v30.md:266` | P2 | KNOWS-STALE (glossary Part One still "Presence"-only; rename is old) |
| 4 | **Spirit / Will** | descriptor_registry primary = **Will**; every live formula (incl. post-registry ED-1021) = **Spirit** | `descriptor_registry.yaml:40`, `params/core.md:145,214`, `derived_stats_v30.md:66,98,151` | P2 | PARTIAL (registry rename never adopted) |
| 5 | **Focus (kind + role)** | base **attribute** 1-7 (descriptor_registry, params/core.md) vs **derived stat** 1-5+ (glossary, alias_registry); mechanical claim "Contact Rounds = Focus" **retired** (ED-694) | `descriptor_registry.yaml:38`, `params/core.md:143,152`, `glossary.md:52`, `derived_stats_v30.md:249-259`, `names_index.yaml:118-123` | P2 | KNOWS-STALE |
| 6 | **Piety Track / Persuasion Track / Conviction Track** | 0-10 debate tracker = **Persuasion Track** (live) but **"Piety Track (CT)"** in glossary; glossary's cited home (`conviction_track_v1.md`) is actually the **Conviction-Scar** mechanic; **"Piety Track (PT)" 0-5** = unrelated per-territory BG stat | `glossary.md:86`, `social_contest_v30.md:89-93`, `params/contest.md:127`, `resolver.py:79-93`, `conviction_track_v1.md:8-10`, `conviction_track_v30.md:14`, `params/bg/tracks.md:139` | **P1** | KNOWS-STALE (wrong home + wrong name; tracked open as **ED-SC-0003**, needs-Jordan) |
| 7 | **Interaction Type** | **CLASH/AMPLIFY/CROSS/DIVERGE** (glossary + mechanical_terms_index) vs **CLASH/REINFORCE/CROSS/TIE** (kernel + prose + params) | `glossary.md:92`, `mechanical_terms_index.md:602-611,1704`, `dictionaries.py:19,254-322`, `social_contest_v30.md:181-204`, `params/contest.md:106-125` | **P1** | KNOWS-STALE |
| 8 | **Composure (liveness in Debate)** | glossary = live "damage track in Debate"; CR3 (2026-06-01) **RETIRED** it as the contest tracker → split into **Face** + **Concentration**; still live in knots/combat/conviction | `glossary.md:51,89,244`, `social_contest_v30.md:231-254`, `primitives.py:167-169`, `params/core.md:160` | P2 | KNOWS-STALE (glossary never absorbed CR3; "Face" absent from glossary) |
| 9 | **Standing** | **2 distinct mechanics**: (a) contest-kernel **0-10** transient ethos (underlies Face); (b) persistent faction/character rank — and (b)'s range is itself **3-way**: **0-5** (clock_registry, stale) / **0-7** (faction_politics, current) / **0-10** (glossary Part Four) | `primitives.py:31-47`, `faction_politics_v30.md:6,38`, `clock_registry_v30.md:52-53`, `glossary.md:110`, `descriptor_registry.yaml:108` | **P1** | PARTIAL (glossary carries a faction 0-10 that disagrees with live 0-7; contest-kernel collision = NEW) |
| 10 | **Disposition** | **exactly 2**: combat aggression axis **1-7** (combatant.py) vs NPC/relational attitude **−5..+5** (npc_behavior/fieldwork) | `combatant.py:99`, `systems.py:695`, `glossary.md:160`, `fieldwork_v30.md:365`, `npc_behavior_v30.md` | P2 | NEW (combat sense absent from glossary Part Twelve collision table) |
| 11 | **Coherence / cohesion family** | **5 distinct referents**: (a) Thread practitioner Coherence 10→0; (b) mass-battle `cohesion = hp/hp_max`; (c) retired name for unit Discipline; (d) Practitioner-Coherence AI bands — same track as (a) but **divergent boundaries/labels**; (e) node-relational (spatial) cohesion | `threadwork_v30.md:643-648`, `units.py:474`, `mass_battle_v30.md:7`, `npc_behavior_v30.md:503-508`, `config.py:95` | P2 | PARTIAL (glossary has Coherence↔Intelligibility only; nothing on the cohesion family) |
| 12 | **Knot Strain vs Knot bond-strain gauge** | both exist under "strain": (a) scene-scoped opposing-ops Ob/Composure penalty; (b) persistent **−5..+5** bond gauge (ED-912) | `threadwork_v30.md:562-571`, `knots_v30.md:39-58,168,207-220` | P3 | NEW (architecturally reconciled — one feeds the other — but shares the name) |
| 13 | **Thread Debt** | referenced pervasively (fieldwork Remnant "token") with **fragmentary** drain rules (bg/phases RS−1/token; PP-600 expiry) but **no consolidated definition**; corpus's own NEW-OI-64 flags it P1-undefined | `fieldwork_v30.md:650`, `fieldwork_bg_v30.md:25`, `params/bg/phases.md:59`, `params/threadwork.md:167`, `tests/…/throughline_synthesis_holistic.md:321` | **P1** | NEW (no glossary entry; genuinely under-defined, corpus-confirmed) |
| 14 | **MS vs RS** | glossary Part Twelve: "RS survives only as **one** historical annotation in canon/02"; reality: **25** live "RS" in `params/threadwork.md` alone (incl. a canonical "RS Track" section) + 17 in `thread_horizontal_integration_spec.md`; **and** RS = **Resonant Style** is a separate uncatalogued third sense | `glossary.md:245`, `params/threadwork.md` (×25), `thread_horizontal_integration_spec.md`, `npc_behavior_v30.md:711`, `canon/02_…:88` | P2 | KNOWS-STALE (undercount by orders of magnitude) + NEW third sense |
| 15 | **Turmoil vs Strain** | one system, name splits by location: **filename** = strain; **title/§4 heading** = Turmoil; **body §4.1-4.4** = Strain; glossary registers it as "Turmoil"; downstream docs use both | `peninsular_strain_v30.md:1,286,290-326`, `glossary.md:225`, `clock_registry_v30.md`, `victory_v30.md`, `derived_stats_v30.md:333,469` | P2 | NEW (glossary picks "Turmoil", doesn't flag the split) |
| 16 | **Combat Pool** | ≥4 written forms — see §Combat-Pool enumeration below; the **struck** `(Agi×2)+History+3` is **still executed** via a live import | `combat_engine_v1/core.py:30`, `params/core.md:158,161,252,4`, `sim/personal/combat.py:127`, `scene_dispatch.py:96`, `values_master.yaml:212,1150` | **P1** | KNOWS-RIGHT-by-deferral (glossary carries no formula) but a live oracle runs the struck form |
| 17 | **Command (mass battle)** | current `clamp(round((2×Cha+Cog)/3),1,7)` (ED-899) vs glossary `⌈(Presence+Cog)/2⌉` — **doubly** stale (equal-weight formula **and** "Presence" not "Charisma") | `mass_battle_v30.md:266`, `exchange.py:25-34`, `glossary.md:121`, `values_master.yaml:1912` | P2 | KNOWS-STALE |
| 18 | **Health** | glossary `= Endurance, resets per wound` (3 generations stale) vs current `round(WI×(MW+1)+0.25·Str·End)`, non-resetting | `glossary.md:47`, `derived_stats_v30.md:55-93`, `params/core.md:158` | P2 | KNOWS-STALE |
| 19 | **Stamina** | glossary `End+History+1` vs current `(3×End)+(2×Spirit)`; **plus** mass-battle Stamina **0-100** (unrelated scale, uncatalogued) | `glossary.md:48`, `derived_stats_v30.md:94-122`, `params/core.md:159`, `mass_battle config.py:42` | P2 | KNOWS-STALE + NEW scale collision |
| 20 | **Intelligibility** | glossary = live 10→0 personal stat; threadwork §8.1 = **RETIRED** (folded into Coherence, since PP-012 2026-03-27); separately live "**Intelligibility Gradient**" (fieldwork, qualitative) | `glossary.md:50`, `threadwork_v30.md:982`, `fieldwork_v30.md:15`, `alias_registry.yaml:78-81` | P2 | KNOWS-STALE (dead stat presented as live) |
| 21 | **The Rupture** | `victory_v30.md` self-contradicts: §5.1/§628 "campaign continues, recoverable Post-Calamity" vs line 647 "all factions lose"; glossary + `params/bg/*` = "campaign-ending" | `victory_v30.md:557,628,647`, `peninsular_strain_v30.md:463`, `glossary.md:154`, `params/bg/clocks.md:18` | P2 | KNOWS-STALE (matches the wrong side of a live self-contradiction) |
| 22 | **Ob cap exception** | TTRPG **Ob 20 / Partial ≥10** vs BG **Ob 10 / Partial ≥5**, the BG table self-labeled "matches TTRPG" | `params/core.md:55`, `params/bg/core.md:65-75`, `params/bg/ed_resolutions.md:159` | P2 | NEW (cross-params; self-flagged open ED-142-R) |
| 23 | **Overwhelming (BG)** | glossary "≥ Ob+1 (BG, provisional)" vs current BG "2×Ob AND ≥3, matches TTRPG" (PP-249/PP-322 supersede PP-281) | `glossary.md:141`, `params/bg/core.md:65-75`, `params/bg/ed_resolutions.md:83-166` | P2 | KNOWS-STALE |
| 24 | **Genre (Debate)** | glossary "Past/Present/Future" vs current "**Memory/Projection**" (PP-234) | `glossary.md:90`, `social_contest_v30.md:16-58`, `params/contest.md:27-31` | P2 | KNOWS-STALE |
| 25 | **Doubt Marker** | glossary "applied on Obscuring **loss** in **Diverge** state" — wrong trigger direction (fires on Obscuring **win**) + retired state name (Diverge→CROSS) | `glossary.md:88`, `mechanical_terms_index.md:611`, `social_contest_v30.md:200,209-217` | P2 | KNOWS-STALE |
| 26 | **Ranged/Projectile DR (mass battle)** | two irreconcilable tables (mass_battle_v30 PP-188 Heavy=3 vs params/mass_combat PP-104 Heavy=7); melee table row-corrupted (5 cols under 4-col header) | `mass_battle_v30.md:246-256`, `params/mass_combat.md:176-197` | P2 | NEW |
| 27 | **History cap "Memory score"** | glossary + arcs cite cap = "Memory score"; **no attribute "Memory" exists**; live attribute is **Recall** | `glossary.md:158`, `emergent_scenarios.md:242`, `params/core.md:151` | P2 | KNOWS-STALE |
| 28 | **Discipline (name collision)** | per-unit 1-7 organisational stat (mass_battle §A) vs faction-derived **Stability×10** (10-70, §B/derived_stats), both "Discipline" in the Army-Morale formula | `mass_battle_v30.md:169,770`, `derived_stats_v30.md:301,405` | P2 | NEW (flagged 2026-04-29 audit, never resolved) |

---

## 2. Detailed sections

### §A — The attribute-roster conflict (rows 1–5): confirmed three-way (arguably four-witness), not the two-way the glossary admits

**Read firsthand, all three anchors:**

- `references/glossary.md:33-41` — **7 attributes**: Agility, Attunement, Cognition, Endurance, Presence, Spirit, Strength. Carries its own IN-FLUX banner (`glossary.md:31`) that admits a **two-way** conflict only: *"this 7-attribute roster conflicts with `references/descriptor_registry.yaml`'s 9-attribute roster."*
- `references/descriptor_registry.yaml:30-44` — **9 attributes**: Strength, Endurance, Agility / Focus, **Acuity** (aliases Reasoning, Cognition), **Will** (alias Spirit) / Attunement, **Charisma** (aliases Influence, Presence), Bonds. The two renamed mind-attributes are self-graded unstable: line 39 carries `# [ASSUMPTION] legacy 'Cognition' folds to Acuity -- Jordan veto`.
- `params/core.md:137-145` — **10 attributes**: line 138 states verbatim *"Point pool at creation: 31 points across **10 attributes**"*; the table (lines 142-145) lists Physical (Agility, Endurance, Strength), Mental (Cognition, **Recall**, Focus), Social (Attunement, Bonds, Charisma), Metaphysical (Spirit).

**Definitive answer to the task's question.** The true count is **three distinct rosters (7 / 9 / 10)**, with a fourth independent witness (`alias_registry.yaml:26-61`) reproducing the glossary's 7 by hand-copy (its header, line 13, declares "Seed source: references/glossary.md"). **No two of the three primary rosters fully agree.** The closest partial agreement is name-level: params/core.md's 10 and descriptor_registry's 9 both use "Charisma"/"Focus"/"Bonds" (where the glossary's 7 use "Presence" and omit Focus/Bonds) — but they still disagree on **count and membership**, because:
- params/core.md's 10th member is **"Recall"**, which appears as an attribute in **neither** the glossary's 7 nor descriptor_registry's 9 (descriptor_registry has no `attr.*.recall` key anywhere). Recall exists as a load-bearing attribute only in `params/core.md` (governs the History-point cap, line 151; drives Fieldwork Research/Reconstruct, line 245) and in non-canonical vocabulary-audit files.
- descriptor_registry uses **Acuity/Will** as primaries; params/core.md uses **Cognition/Spirit**.

So simple aliasing cannot reconcile them: it is a genuine **7-vs-9-vs-10** conflict on count *and* membership. **The glossary's own IN-FLUX banner is itself incomplete** — it names only the descriptor_registry side and is unaware of the params/core.md 10-roster (the third anchor), which carries **no** hedge, cross-reference, or IN-FLUX marker despite being the batch-nominated live dice head per `CURRENT.md`.

**Downstream adoption verdict (rows 2, 4):** the descriptor_registry renames Cognition→Acuity and Spirit→Will have **zero adoption** in any live mechanical formula. Every current formula that consumes these attributes — including ones ratified *after* the 2026-06-06 registry (e.g. ED-1021's Wound-Interval, 2026-06-18, at `derived_stats_v30.md:66`) — writes "Cognition" and "Spirit". "Acuity" as a formula input appears nowhere; "Will" appears only in the registry pair and its own unit test (`test_descriptor_registry.py`). Row 3 (Presence→Charisma) is the mirror-image failure: that rename was *executed* long ago (PP-234, `params/contest.md:3`) and the live corpus uses "Charisma" everywhere, but the glossary/alias_registry naming-authority files never caught up.

**Focus (row 5) is a double defect:** (i) a *classification* split — descriptor_registry + params/core.md treat it as a base attribute (1-7); glossary + alias_registry file it as a derived stat (1-5+); (ii) params/core.md:152's mechanical claim *"Contact Rounds = Focus score"* names a mechanic (`Contact Rounds`) that `names_index.yaml:118-123` itself lists as **retired legacy vocabulary** (ED-694 replaced it with Thread Fatigue; `derived_stats_v30.md:249-259`).

**Implementer impact (why P1):** `descriptor_registry.yaml` itself declares aggregates `placeholder`/not-wired and the roster "IN FLUX"; a Godot resource cannot bind attribute fields until the count/membership is settled. This is the single highest-severity structural item in the corpus.

---

### §B — Piety Track vs Persuasion Track (row 6): four-way tangle, tracked-open, definitively NOT one mechanic

**Definitive answer:** these are **not** the same mechanic under two names. There are **three genuinely distinct mechanics** plus a residual naming synonym, all confirmed by direct read:

1. **Persuasion Track** — the 0-10 personal-scale debate-position tracker (Side A wins ≥7, Side B ≤3, compromise 4-6). Live home: `social_contest_v30.md:89-93,276`; `params/contest.md:127-128`; kernel `sim/personal/contest/resolver.py:79-93` (`class PersuasionTrack`). This is the mechanic the glossary Part Three row (`glossary.md:86`) actually *describes* — the thresholds match word-for-word.
2. **Piety Track (PT), 0-5, per-territory** — a BG Solmund-orthodoxy stat, unrelated to debate. Home `designs/scene/conviction_track_v30.md:14`; `params/bg/tracks.md:139`; `clock_registry_v30.md:60`.
3. **The Conviction-Scar mechanic** — what `designs/personal/conviction_track_v1.md` **actually contains** (verified: line 8 titles it "Piety Track" but §1-§3 are the per-Conviction Scar/crisis system, and §1 is `[SUPERSEDED 2026-05-10 — PP-717]`).

**The glossary's defect (row 6):** `glossary.md:86` assigns the debate tracker the name **"Piety Track (CT)"** and cites its canonical home as `conviction_track_v1.md` — but (a) the live name is **Persuasion Track**, and (b) that cited file is about Conviction Scars, not a 0-10 win/lose gauge. This is confirmed already-open and needs-Jordan as **ED-SC-0003** (per Batch 4's ledger read) and appears on the P0 decision docket in `handoffs/HANDOFF_SC.md`. Residual "Piety Track" used loosely for the debate tracker survives in `npc_behavior_v30.md`, `params/scale_transitions.md:46`, `faction_politics_v30.md:92` (acknowledged unswept per `silo_cohesion_analysis.md:39`).

---

### §C — Interaction Type (row 7): glossary label set is wrong on two of four labels

**Definitive answer, both sides quoted:**
- Glossary: `glossary.md:92` — `CLASH / AMPLIFY / CROSS / DIVERGE`. Repeated in `mechanical_terms_index.md:602,604,611,1704`.
- Live canon (kernel + prose + params, all agreeing): `sim/personal/contest/dictionaries.py:19` — *"INTERACTIONS_TABLE — InteractionType×4 (CLASH / REINFORCE / CROSS / TIE)"*; `derive_interaction()` at `dictionaries.py:309-322`; prose headers `social_contest_v30.md:181,190,195,204`; `params/contest.md:106-125`.

This is not a cosmetic rename: **AMPLIFY↔REINFORCE** name the same condition (same genre, same orientation), but **DIVERGE↔TIE do not correspond** — DIVERGE was "different genre, same orientation" (a genre case now absorbed into CROSS), whereas TIE is an orthogonal outcome-parity overlay ("equal successes, any interaction type"). ED-133 (`social_contest_v30.md:680`) still tracks DIVERGE's retirement as an *open* cleanup item. **P1** because an implementer coding the glossary's four labels would build the wrong resolver.

---

### §D — Composure liveness (row 8): confirmed glossary-currency defect

**Definitive answer:** the glossary's claim is stale. `glossary.md:51` (Part One), `:89` (Part Three, *"Also the damage track in Debate exchanges"*), and `:244` (Part Twelve, *"Composure (Debate context)"*) all present Composure as the live Debate damage track. CR3 (RATIFIED 2026-06-01) **retired it as the social-contest tracker**, splitting it into **Face** (contest-local ethos) + **Concentration** (stamina): `social_contest_v30.md:231-254`; kernel enforces it — `primitives.py:167-169` `RETIRED_TRACKERS = ("Composure",)`, asserted by CI test `_kernel_tests.py:698-703`. The retirement is scoped: Composure legitimately survives in knots (`knots_v30.md`), combat, and conviction (`social_contest_v30.md:509`), and its base formula `Charisma × 3` (`params/core.md:160`) is unchanged. But the glossary was "swept" 2026-04-30 — *before* CR3 — and never updated; **"Face" has zero glossary entries** (grepped: 0 hits as a game term). Confirmed defect.

---

### §E — Standing (row 9): two distinct mechanics; the persistent one carries three ranges

**Definitive answer to "how many distinct Standing tracks":** **two genuinely distinct mechanics**, and the persistent one is internally three-way on range.

- **(a) Contest-kernel Standing** — `sim/personal/contest/primitives.py:31-47`: `class Standing: LO,HI,START = 0.0,10.0,5.0`; **transient**, per-side, built by ethos moves, feeds Readiness/leak; `Face = Standing` (line 108). Resets at contest end.
- **(b) Persistent faction/character rank-Standing** — the "reputation/rank within a faction" that NPCs hold (`npc_behavior_v30.md` "Church Standing ≥ 3"). Its range is unsettled across three canonical citations:
  - **0-7** (current) — `faction_politics_v30.md:38`: *"Replace the 0–5 Standing track with an eight-position ladder (Standing 0 through Standing 7)"*, with a −1 Dismissed floor (line 55).
  - **0-5** (stale) — `clock_registry_v30.md:53`: `| Standing | 0–5 | bg_v05 §Standing (P-15) |` (self-declared "single source of truth for all clocks," last touched 2026-06-24, i.e. *after* the 0-7 redesign, yet not updated).
  - **0-10** (glossary) — `glossary.md:110`: *"Reputation track. Range 0–10 (exception to 1–7 scale)."* Batch 5 traced this 0-10 to `params/history/board_game.md:75`, a file whose own header says "do not read… it is history, not values."

**Do they collide confusingly for an implementer?** Yes, twice over: (i) both the contest-kernel Standing and the glossary faction Standing are **0-10**, so a Godot dev binding a "Standing" field cannot tell from the name/range which mechanic it is; (ii) `descriptor_registry.yaml:108` files Standing under `tracks` (not `faction_stats`), contradicting the glossary's placement of it *in the faction-stats table*. The contest-kernel-vs-persistent collision is **NEW** (uncatalogued anywhere; `name_collision_database.yaml:139` exempts a *different* Standing/Key-type overlap).

---

### §F — Disposition (row 10): confirmed exactly two, not more

**Definitive answer:** **exactly 2** distinct mechanics named "Disposition":
1. **Combat aggression axis, 1-7** — `combatant.py:99` (verified): `self.disp=disp  # disposition / temperament, aggression axis (1-7, 4=neutral); lean=(disp-4)/3`. Consumed by `systems.py:695` `commit_depth`.
2. **NPC/relational attitude, −5..+5** — `glossary.md:160` ("NPC-attached attitude state"), numeric home `fieldwork_v30.md:365` (*"Disposition range: −5 to +5. Flat per NPC per PC… no Bonds ceiling"*, ED-912), used throughout `npc_behavior_v30.md`.

(Batch 7 additionally noted `combat_v30.md:406-408`'s "Disposition modifier: Offensive +2 / Defensive +4" — but that superseded doc's usage is a **third *label* reuse** of the word for a flat combat-stance bonus, not a third live tracked stat; combat_engine_v1 does not carry it. I count the live mechanics as **2**, with a stale third label lingering in a partially-superseded file.) The collision is **NEW** — the glossary's Part Twelve collision table lists CI/CP/TD/COMP/RS but not Disposition, despite both senses being live.

---

### §G — Coherence / cohesion / Practitioner Coherence (row 11): five referents; two genuinely name-confusable

**Definitive count: five distinct referents**, of which the pairs confusable **by name alone** are flagged:

1. **Coherence** — Thread practitioner personal stat, 10→0. `threadwork_v30.md` Part Three; thresholds §3.3 (`:643-648`): **10-8 Stable / 7-5 Dissonant / 4-3 Fragmented / 2 Fractured / 1 Severed / 0 Rendering Crisis**.
2. **Practitioner Coherence (AI-gating)** — `npc_behavior_v30.md:503-508` (verified): **same 10→0 track**, but **divergent bands**: **10-6 Stable / 5 Dissonant / 4-3 Degraded / 2 Fractured / 1 Severed / 0 Conversion**. This is a real value+label conflict against #1 at 4 of 6 bands (Stable extends to 6 vs 8; Dissonant is 1 pt vs 3; 4-3 is "Degraded" vs "Fragmented"; 0 is "Conversion" vs "Rendering Crisis"). #1 and #2 are the **most confusable pair** — same name, same scale, genuinely different numbers.
3. **cohesion (mass-battle engine-internal)** — `units.py:474` (verified): `@property cohesion: return hp/hp_max` — a 0.0-1.0 troop-fraction feeding the combat pool. Unrelated to #1/#2 except by root-word.
4. **"Cohesion" (retired)** — the pre-PP-232 name for the mass-battle **Discipline** stat; residual as two unswept section headings in `params/mass_combat.md:335,347`.
5. **node-relational cohesion** — `config.py:95` `PC_NODE_COHESION`, a spatial formation-holding concept (`units.py:542`), no design-doc home at all.

**Name-confusable pairs (even where mechanically distinct):** {#1, #2} (identical name+scale, different bands — a live defect); {#3, #4, #5} all share the bare word "cohesion" inside `units.py`/`params/mass_combat.md`; and the whole family shares the coherence/cohesion root, which the glossary addresses only for the Coherence↔Intelligibility pair (`glossary.md:49-50`). The cohesion family is **NEW** to the glossary. (Adjacent: "Discipline" itself collides — row 28 — unit stat vs faction Stability×10, both inside the Army-Morale formula, `derived_stats_v30.md:405`.)

---

### §H — Knot Strain vs the Knot bond-strain gauge (row 12): both exist, share the name, architecturally reconciled

**Definitive answer:** **both exist and share "strain."**
1. **Knot Strain (opposing-ops penalty)** — `threadwork_v30.md:562-571`: a *scene-scoped* Ob + Composure penalty on practitioners in a contested Thread operation (e.g. loser: +1 Ob next Thread op this scene, 2 Composure; FR: +2 Ob, 4 Composure), expiring at scene end.
2. **Knot bond-strain gauge** — `knots_v30.md:39-58`: a *persistent* −5..+5 relationship-wear counter (Distant −2..+5, Close −5..+5), rupture at +5, ED-912.

They are reconciled, not contradictory: `knots_v30.md:168,207-220` explicitly makes the §2.6 opposing-ops event **one contributor** ("+1 strain to the Knot per opposing-operations event") to the persistent gauge, and restates the threadwork table verbatim with matching numbers. Severity **P3** (name-share only; mechanics correctly cross-linked). Not in the glossary collision table.

---

### §I — Thread Debt (row 13): referenced pervasively, never consolidated — corpus-confirmed under-defined

**Definitive answer:** it is **effectively undefined**, but not literally absent — the honest finding is subtler than "undefined anywhere." Verified state:
- **Placement triggers exist**: fieldwork Remnant POI "places a Thread Debt token" — `fieldwork_v30.md:650`, `fieldwork_bg_v30.md:25`, `params/fieldwork.md:250`.
- **Fragmentary drain/expiry rules exist**, scattered and not obviously mutually consistent: `params/bg/phases.md:59` (*"tokens >1 season old: RS −1/token… permanent residual RS −0.5"*), `params/bg/military.md:43` (adjacency modifier), `params/threadwork.md:167` + `params/mass_combat.md:244` (*"Battle-context Thread Debt expires at battle season end (PP-600)"*).
- **No consolidated home definition** of what a Thread-Debt token *is* or does when placed via Survey. The corpus's **own** audit flags this: `tests/…/throughline_synthesis_holistic.md:321` and `tests/stress/emergent_arc_2026-04-17_batch7.md:754` file **NEW-OI-64, P1**: *"Thread Debt token mechanics are not specified in any document… referenced but not defined."*

So: **confirmed genuinely under-defined** (no canonical spec, corpus-acknowledged P1 gap), with the nuance that fragmentary BG-phase drain rules exist that don't tie back to the fieldwork placement site. No glossary entry. **P1** (a Godot importer cannot implement a "token placed" with no token semantics).

---

### §J — MS vs RS (row 14): the glossary's Part Twelve claim has badly regressed

**Definitive answer:** the glossary's claim is **false as written**. `glossary.md:245` (Part Twelve): *"RS appears only as historical annotation in `canon/02_foundations_amendment_leap_mechanism.md` per intentional retention."* Verified reality:
- `params/threadwork.md` — **25 live "RS" occurrences** (grep count verified), including a canonical `## RS Track (PP-603 — canonical)` section. This is a `canonical_sources.yaml`-listed live params head, dated pre-ED-731, never swept.
- `designs/threadwork/thread_horizontal_integration_spec.md` — 17 live "RS" (a `CURRENT.md`-named threadwork co-head).
- The *cited* residual is itself mis-described: `canon/02_…:88` spells out the **full phrase** "formerly Rendering Stability," and contains **zero** bare "RS" tokens. The censured-vocabulary audit that fed the glossary searched the *phrase* "Rendering Stability" (correctly → 1 hit) while the live drift is the bare *abbreviation* "RS."
- **Third, uncatalogued sense**: "RS" = **Resonant Style** in `npc_behavior_v30.md:711-734` (a Debate concept). "Resonant Style" has zero glossary entries.

**KNOWS-STALE** (undercount by orders of magnitude) plus a **NEW** third sense. The MS↔TT opposite-direction note (`glossary.md:63`) is a separate, still-accurate item.

---

### §K — Turmoil vs Strain (row 15): confirmed, and it's a 3+-way split, not 2

**Definitive answer, verified:** in `designs/provincial/peninsular_strain_v30.md`:
- **filename** = `peninsular_**strain**_v30.md`;
- **title** (line 1) = "VALORIA BG — **Turmoil** System v1";
- **§4 heading** (line 286) = "§4 **Turmoil** Counter — NEW";
- **body subsection headers** (lines 290-326) = §4.1 "Advancing **Strain**", §4.2 "Reducing **Strain**", §4.3 "**Strain** Threshold Effects", §4.4 "**Strain** and IP".
- Only **11** "Turmoil" occurrences in the whole file (grep verified) vs pervasive "Strain" in the operative mechanics.

The glossary Part Eleven (`glossary.md:225`) registers the system canonically as **"Turmoil"** and does not flag the split. Downstream, `clock_registry_v30.md` standardized on "Turmoil"; but `params/bg/clocks.md:41`, `victory_v30.md` (both names for the same ≤6 win threshold), and `derived_stats_v30.md:333,469` each carry **both** names for the identical 0-10 counter. So it is at least a four-way inconsistency (filename / title-heading / body / downstream), not a clean two-way. **NEW** to the glossary's awareness.

---

### §K′ — Combat Pool (row 16): definitive enumeration of every form

Verified enumeration of every distinct written definition in the live/near-live tree:

| # | Form | Status | Sites (verified ✓) |
|---|---|---|---|
| 1 | `max(5, Relevant History + 6)` — Agility-independent | **CURRENT canonical** (ED-901, re-ratified ED-900/904) | `combat_engine_v1/core.py:30-32` ✓; `params/core.md:158,161` ✓; `module_contracts.yaml:811`; `combatant.py:117` (present but **dead/unread** per Batch 6) |
| 2 | `(Agility × 2) + Relevant History + 3 (minimum 5)` | **STRUCK** (PP-615/PP-247 era) — but **still executed** | `sim/personal/combat.py:127` ✓ (`[DEPRECATED 2026-06-23]` banner, line 4 ✓) — **live-wired** via `scene_dispatch.py:96` ✓ (`import sim.personal.combat as combat`); `params/core.md:4` changelog ✓; `values_master.yaml:212-217` (Batch 6, filed under nonexistent `params/combat.md`) |
| 3 | `(Agility × 2) + weapon History (points + 3)` | stale extraction, distinct wording | `values_master.yaml:1150-1163` (Batch 6) |
| 4 | `(Primary Attribute × 2) + History bonus` — describing Combat Pool's construction as Agi×2-based | **intra-file contradiction** | `params/core.md:252` ✓ (contradicts line 161 in the *same file*) |

Plus a deliberately-frozen archival copy of form #1 at `tests/sim/v32-combat-balance/r1_sigma_resolution.py:71` (retained for historical parity runs, non-live). The **P1** finding is form #2: the deprecation banner was never backed by removing the import, so any `run_scene_phase`/`dispatch_scenes` path with a `"combat"` scene executes the struck Agility-dependent formula. `canon/mechanics_index.yaml:210-219` asserts the deprecated module is inert — **contradicted** by the live `scene_dispatch.py:96` wiring. The glossary carries no Combat Pool formula (defers), so it is not itself wrong; the defect is oracle-level.

---

### §L — Remaining glossary formula drifts (rows 17–28, condensed evidence)

Each verified against its live head; all are **KNOWS-STALE** unless marked NEW:

- **Command (17):** `glossary.md:121` `⌈(Presence + Cognition) ÷ 2⌉` vs `mass_battle_v30.md:266` (verified) `clamp(round((2 × Charisma + Cognition) ÷ 3),1,7)` + engine `exchange.py:25-34` weights `CMD_CHA_WEIGHT=2/CMD_COG_WEIGHT=1`. Doubly stale (equal-weight + "Presence"). `values_master.yaml:1912` carries the superseded form too.
- **Health (18):** `glossary.md:47` `= Endurance, Resets per wound` vs `derived_stats_v30.md:67` `round(WI×(MW+1)+0.25·Str·End)`, WI=`round(End+4+0.4·Spirit)`, **non-resetting** (line 68). Three generations behind. (Note: `derived_stats_v30.md` even self-contradicts — §3/§13 still print the interim `(End+6)×(MW+1)` — a same-doc drift.)
- **Stamina (19):** `glossary.md:48` `End+History+1` vs `derived_stats_v30.md:98`/`params/core.md:159` `(3×End)+(2×Spirit)`. Plus mass-battle Stamina **0-100** (`mass_battle config.py:42`) — a wholly different scale sharing the name, **NEW** and uncatalogued in glossary/mechanical_terms_index. (Also: `params/core.md:159` states range 5–35 while `derived_stats_v30` states 5–47 for the same formula — a minor co-canonical range mismatch.)
- **Intelligibility (20):** `glossary.md:50` presents a live 10→0 personal stat; `threadwork_v30.md:982` (§8.1 "Systems Replaced") lists Intelligibility as **retired**, folded into Coherence (reconciliation traces to archived PP-012, 2026-03-27). Live "Intelligibility Gradient" (`fieldwork_v30.md:15`) is a *different*, qualitative mechanic. `params/threadwork.md` correctly dropped the stat; only glossary/alias_registry/mechanical_terms_index lag.
- **The Rupture (21):** `victory_v30.md` self-contradicts — §5.1/§628-638 ("no shared loss… campaign continues… recoverable Post-Calamity Era") vs line 647 ("MS 0 = Rupture = all factions lose"). `peninsular_strain_v30.md:463` ("No shared loss") is the declared supersessor. `glossary.md:154` + `params/bg/clocks.md:18` + `params/bg/victory.md:61` all carry the stale "campaign-ending" side. An archived 2026-06-11 audit (F5) already diagnosed this; unactioned.
- **Ob cap (22, NEW):** `params/core.md:55` (Ob 20 / Partial ≥10) vs `params/bg/core.md:65-75` (Ob 10 / Partial ≥5, self-labeled "matches TTRPG", self-flagged `[FLAGGED ED-142-R]`).
- **Overwhelming BG (23):** `glossary.md:141` "≥ Ob+1 (BG, provisional)" vs live `params/bg/core.md:65-75` "2×Ob AND ≥3 (PP-249, matches TTRPG)"; `params/bg/ed_resolutions.md:157-166` explicitly struck the Ob+1 form (PP-322 > PP-281).
- **Genre (24):** `glossary.md:90` "Past/Present/Future" vs `social_contest_v30.md:16` "Memory/Projection" (PP-234, executed 2026-04-04 — *before* the glossary's own sweep date).
- **Doubt Marker (25):** `glossary.md:88` "Obscuring **loss** in **Diverge** state" — both wrong: fires on Obscuring **win** (`social_contest_v30.md:200`), and "Diverge" is the retired state (→ CROSS). `mechanical_terms_index.md:611` duplicates the identical error.
- **Ranged DR (26, NEW):** `mass_battle_v30.md:246-256` (PP-188, Heavy vs Piercing/Blunt = 3/2) vs `params/mass_combat.md:191-197` (PP-104, 4-axis, Heavy = 7/5/6/2) — two irreconcilable ranged-DR tables, both presented as current; plus `params/mass_combat.md:176-181` melee table has a corrupted 5th column under a 4-column header.
- **History cap (27):** `glossary.md:158` + `emergent_scenarios.md:242` cite cap = "Memory score"; no attribute "Memory" exists in any roster; the live cap attribute is **Recall** (`params/core.md:151`).
- **Discipline collision (28, NEW):** `mass_battle_v30.md:169` per-unit 1-7 vs `:770`/`derived_stats_v30.md:301` faction `Stability × 10` (10-70) — both "Discipline," co-located in the Army-Morale formula (`derived_stats_v30.md:405`). Flagged by the 2026-04-29 interdependency audit; never resolved.

---

## 3. Re-verification of the glossary's own Part Twelve and Part Thirteen

### Part Twelve — Collision / Disambiguation table (`glossary.md:239-245`)

| Entry | Glossary's stated resolution | Re-verification verdict |
|---|---|---|
| **CI** (Church Influence vs Piety Track) | "Write CI for Church Influence; Piety Track / **CT** for the debate tracker" | **REGRESSED.** The debate-tracker abbreviation is now empirically **PT** in the live corpus (133 files, e.g. `params/bg/core.md:117`), not "CT"; and "**CT**" independently now denotes **Conviction Track** (`alias_registry.yaml`), a separate unresolved deprecation. The "CT for Piety Track" guidance is both unused and newly-colliding. (Church-Influence-side of the entry still holds.) |
| **CP** (Character Points vs Combat Power) | "CP = Character Points only [ED-136]; residual_count 0" | **REGRESSED.** `censured_vocabulary.yaml` claims residual 0, but live "CP" = Combat Power survives: `combat_v30.md:419,436`, `combat_design_v1.md:354,361`, `combat_v30_infill.md:68`, and one leftover in the otherwise-clean `params/mass_combat.md:313`. The Character-Points sense is fine; the "residual 0" claim is false. |
| **TD** (Thread Depth vs Top-Down Mermaid) | "Thread Depth REMOVED PP-166; `flowchart TD` is Mermaid, not a game term" | **INCOMPLETE.** Both stated senses hold, but the table omits a **third live meaning**: "TD" = **Theological Dissatisfaction** (0-5 Hafenmark track), verified live in `params/bg/tracks.md:18,55,84` and `miraculous_event_v30.md`. Collision table is missing a real current collision. |
| **COMP** (Composure Debate context vs English) | "Write 'Composure' in game documents" | **REGRESSED.** The "Debate context" referent was renamed to **Face** by CR3 (2026-06-01, ED-1056) — the Debate damage track is no longer "Composure." The entry's own label ("Composure (Debate context)") names a role that no longer exists. |
| **RS** (Rendering Stability, renamed MS) | "RS appears only as **one** historical annotation in canon/02" | **REGRESSED — badly.** 25 live "RS" in `params/threadwork.md` alone + 17 in `thread_horizontal_integration_spec.md`; the cited canon/02 line isn't even a bare-"RS" instance; and RS = **Resonant Style** is an uncatalogued third sense. See §J. |

**Part Twelve verdict: 0 of 5 entries fully current.** CI, CP, COMP, RS have all regressed; TD is incomplete. Additionally, three live collisions belong in this table and are absent: **Disposition** (combat 1-7 vs NPC −5..+5), **Standing** (contest-kernel 0-10 vs faction 0-10/0-7/0-5), and **Discipline** (unit 1-7 vs faction 10-70).

### Part Thirteen — Deprecated / Resolved abbreviations (`glossary.md:255-261`)

| Entry | Glossary status | Re-verification verdict |
|---|---|---|
| **CERT** (Certainty) | RESOLVED — active stat | **HOLDS.** No bare "CERT" in live design/params; everyone writes "Certainty." |
| **TLK** (Torben Loyalty Clock) | DEPRECATED — historical only | **HOLDS.** Confined to registry/archive/old sim-logs. |
| **DD** (Deniability Debt) | DEPRECATED — abbreviation not in active use | **HOLDS.** Confined to registry + old stress logs; the full-phrase mechanic survives where retained, as stated. |
| **FSTAT** (Faction Stats) | DEPRECATED — sim code only | **HOLDS.** No live in-game use. |
| **CE** (Combat Endurance) | RESOLVED — active stat | **INCOMPLETE.** The abbreviation "CE" is clean, but the **full phrase "Combat Endurance"** has independently drifted to a second, unrelated live mechanic — an Inquisitor/NPC suspicion-accumulation track in the arcs corpus (`arcs_01_04.md:101` "Klapp Combat Endurance track +1/season"; `arcs_31_35.md:96` "Inquisitor Combat Endurance track"). `silo_cohesion_analysis.md:164` validated the abbreviation and missed the term-identity drift. |
| **INT** (Intel) | RESOLVED — active stat | **HOLDS.** Live usage correctly writes mixed-case "Int"; bare all-caps "INT" appears only as doc-section tags. |

**Part Thirteen verdict: 5 of 6 hold; CE is incomplete** (its abbreviation resolved, but "Combat Endurance" as a full phrase now names two unrelated mechanics — the glossary's Part Five Stamina sub-application vs the arcs' Inquisitor suspicion track).

---

## 4. Cross-cutting closing note (highest-value, load-bearing facts)

1. **The glossary's structural staleness is dateable, not incidental.** Its content sweep predates CR3, ED-899, ED-694, PP-234 and the contest rebuild; every KNOWS-STALE row above is a consequence of that one gap. The highest-leverage single fix is a glossary re-sweep against the post-April-2026 heads, plus wiring a real glossary mirror into `names_index.yaml` + `ci_names_consistency.py` (the glossary's own IN-FLUX banner already identifies this tooling gap).
2. **Two P1 items are live oracle hazards, not just doc drift:** the struck `(Agi×2)+History+3` Combat Pool executes through `scene_dispatch.py:96 → sim/personal/combat.py`; and Thread Debt is a corpus-acknowledged (NEW-OI-64) referenced-but-undefined mechanic that no importer can build.
3. **The attribute roster (P1) blocks the Data→Godot pipeline by construction** — three rosters (7/9/10) with irreconcilable membership (Recall, Acuity/Cognition, Will/Spirit), only one of which (descriptor_registry) even flags itself unstable.
4. **The glossary's collision machinery (Part Twelve/Thirteen) has itself regressed** — the very tables meant to catch cross-contamination are 0/5 current in Part Twelve and miss at least three live collisions (Disposition, Standing, Discipline) plus a second "Combat Endurance" — meaning the corpus's designated collision-detection surface can no longer be trusted as authoritative without the re-verification performed here.
