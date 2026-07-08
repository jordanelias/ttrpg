# Term Usage Sweep — Batch 10: Dice-engine terms and the glossary's own Collision/Disambiguation and Deprecated tables

# Batch 10 Audit: Dice-Engine Terms + Glossary Collision/Disambiguation/Deprecated Tables

Method note: all citations below are from direct `Read`/`Grep` of the working tree at `/home/user/ttrpg` on 2026-07-08. Where a term occurs in hundreds of files in an obviously consistent way (TN, Ob, RS as bare token), I opened a representative cross-section of each subsystem/directory rather than every file, per the batch's own summarization allowance — but every **divergence** reported below is independently verified at file:line, not inferred.

---

## 1. Target Number / TN

**Home definition.** `params/core.md:23-30` (canonical, "Dice / resolution" head per `CURRENT.md:56`):
```
## TN Values
| Mode | TN | When |
| Controlled | 6 | Prepared, unhurried, favourable |
| Standard | 7 | Default |
| Desperate | 8 | Duress, exhaustion, existential threat |
Thread operations: TN 7 standard; TN 8 for Locking, Dissolution, and Past-Oriented Pulling.
```
Also `references/glossary.md:137`: "Target Number | TN | **Exception — abbreviation permitted standalone.** The die face threshold for a success (6, 7, or 8 depending on context)." TN is mechanically the face-value floor above which a d10 face counts as +1 success (faces below TN = 0, face 1 always −1, face 10 always +2 — `params/core.md:12-19`).

**Exhaustive usage sweep.** `\bTN\b` hits 250+ files (search capped). Confirmed consistent with the 6/7/8 baseline in: `params/mass_combat.md:18,33,237,367,457` (TN 6 for Volley — explicitly rationalized as the "Controlled/favourable" case), `params/fieldwork.md:163,181,184` (TN 7 throughout), `params/contest.md:25,85,90,288,302` (TN 7 standard, TN 8 "Rushed"), `params/threadwork.md:54-60` (its own more granular "TN Modifiers" table, see divergence below), and pervasively through `designs/scene/*`, `designs/threadwork/*`, `canon/mechanics_index.yaml`, and hundreds of `tests/sim/*.md` simulation-output files (e.g. `tests/sim/sim_ttrpg_batch_07.md`, `tests/sim/sim_thread_01.md` — spot-checked several, all consistent with the same 6/7/8 or 7/8/9 Thread scale).

**Divergence check.**
- `params/threadwork.md:54-60` ("TN Modifiers, PP-619 — canonical") defines a **4th tier not present in `params/core.md`**: standard ops = 7, Binding (Lock/Dissolution) = 8, POP = 8, **"POP Binding (Past-Oriented Lock or Dissolution) = 9"**. `params/core.md:30` only documents "TN 7 standard; TN 8 for Locking, Dissolution, and Past-Oriented Pulling" — it never mentions a TN 9 tier at all. This isn't a contradiction (both agree on 7/8), but core.md is **incomplete relative to its own downstream PULLED consumer** — a reader of core.md alone would not know TN 9 exists.
- **Combat's per-weapon TN matrix is a live currency problem, not a silent divergence.** `designs/scene/combat_v30.md:117-156` and `designs/scene/combat_design_v1.md:124-164` define "Final Hit TN = 7 + reach modifier + weight modifier + type modifier" (TN 5-9 depending on weapon), explicitly cross-referenced by `params/core.md:70` ("Fractional TN (PP-717 Fiore half-step TN already canonical for combat)"). However, **combat_v30.md and combat_design_v1.md are the PARTIALLY SUPERSEDED docs** — the actual current combat head, `designs/scene/combat_engine_v1/` (confirmed via `config.py` — no `TN`/`target_number` token found in it at all), has moved to a continuous d+σ resolver with no discrete TN concept (`designs/scene/combat_engine_v1/README.md:17`: "NOT the v30 model (Agi×2 pool / TN-7 / multiplicative STR)"). So the Weapon TN Matrix is a live-looking mechanic in a still-open, banner-marked-superseded doc that the actual current combat engine doesn't implement at all.

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `params/core.md:23-30` | CANONICAL DEFINITION | — | — |
| `params/mass_combat.md:18,367` | PULLED / REFERENCED | Prose explicitly rationalizes TN 6 as the core "Controlled/favourable" case (`:367`) | Yes |
| `params/fieldwork.md:163,181,184` | HARDCODED DUPLICATE | Restates "TN 7" as a literal in each roll spec, no import mechanism | Yes |
| `params/contest.md:25,85,90` | HARDCODED DUPLICATE | Same — literal "TN 7"/"TN 8" per roll line | Yes |
| `params/threadwork.md:54-60` | HARDCODED DUPLICATE (extension) | Independent "TN Modifiers" table; adds TN 9 unseen in core.md | Partially — agrees on 7/8, silently extends to 9 |
| `designs/scene/combat_v30.md:117-156`, `combat_design_v1.md:124-164` | HARDCODED DUPLICATE, STALE | Independent per-weapon TN table in a doc banner-marked `[PARTIALLY SUPERSEDED]` | No longer live — current combat engine (`combat_engine_v1/config.py`) has no TN concept |
| `tests/sim/*.md` (dozens, e.g. `sim_thread_01.md`, `sim_ttrpg_batch_07.md`) | HARDCODED DUPLICATE (historical output) | Simulation prose citing "TN 7" as flavor text of a rolled scene | Yes, consistent, but these are output logs, not specs |

**Incidental English usage excluded:** none — "TN" does not collide with ordinary English.

---

## 2. Obstacle / Ob

**Home definition.** `params/core.md:32-55`:
```
## Obstacle Scale
| Ob | Difficulty |
| 1 | Routine | 2 | Moderate | 3 | Difficult | 5 | Entrenched | 8 | Structural | 20 | Foundational (cap; no stacking above 20) |
Ob minimum: 1. (PP-232)
...
Overwhelming requires a minimum of 3 net successes regardless of Ob. (PP-232)
Ob 20 exception: Overwhelming unavailable. Partial requires net ≥ 10.
```
`references/glossary.md:138`: "Obstacle | Ob | **Exception — abbreviation permitted standalone.** The number of net successes required for a Success result."

**Exhaustive usage sweep.** Ubiquitous across `params/*`, `designs/*`. `params/threadwork.md:65-101` layers its own additive "Three-Axis Ob System" (Depth + Breadth + Distance, Fibonacci 1-13) on top of the base Ob concept — legitimate elaboration, explicitly its own canonical sub-system, not a redefinition of what "Ob" means. `params/mass_combat.md` and `params/contest.md` don't restate an Ob cap at all (no independent "Ob ≤ N" literal found) — they're silently PULLED against core.md's cap.

**Divergence check — confirmed and precisely located** (this is the flagged Ob-20-vs-Ob-10 item):
- `params/core.md:55`: **"Ob 20 exception: Overwhelming unavailable. Partial requires net ≥ 10."** (TTRPG mode, post-PP-232 cap raise to 20, dated 2026-04-03 per `archives/patches/patch_register_archive_201_400.yaml:274`).
- `params/bg/core.md:65-75` ("Degree Table (PP-179 + PP-249 — matches TTRPG)"): **"Ob 10 exception: Overwhelming unavailable. Partial requires net ≥ 5."** — half of core.md's values, and the table's own header claims it "matches TTRPG" while using a materially different exception band.
- Same "Ob 10 exception... net ≥ 5" text is **duplicated verbatim** at `params/bg/ed_resolutions.md:159`.
- No file in `params/bg/*` documents an actual BG Obstacle-Scale table with a stated cap of 10 (checked `params/board_game.md`, `params/bg/*.md` broadly) — there is no affirmative design reason for BG's cap to differ from TTRPG's; it reads as a pre-PP-232 leftover that TTRPG's Ob-cap-raise (10→20) never got propagated into the BG-mode exception band.
- **The doc knows it's unresolved**: `params/bg/core.md:75` itself carries `[FLAGGED FOR REVIEW: ED-142-R — confirm 2×Ob canonical; confirm floor of 3 applies to BG; confirm Ob 10 exception carries.]` — open, unresolved as of today.
- Corroborated independently by `designs/audit/2026-07-08-crunch-cascade-cogload-legibility-audit/01_findings_board_game_dice_core.md:50-53,96-99` (a same-day sibling audit): "The Obstacle Scale caps its exception band at Ob 20 in the general table but at Ob 10 in the parallel Board Game Degree Table — a live, self-flagged inconsistency... open."

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `params/core.md:32-55` | CANONICAL DEFINITION (TTRPG) | — | — |
| `params/bg/core.md:65-75` | UNCLEAR / NO CANONICAL SOURCE | Claims "matches TTRPG" (PP-179/PP-249) yet independently states a different (Ob 10) exception band with no resolving citation; carries its own open `[FLAGGED ED-142-R]` | **No** — diverges from TTRPG's Ob-20 band; itself unresolved |
| `params/bg/ed_resolutions.md:159` | HARDCODED DUPLICATE | Verbatim repeat of the Ob-10 exception text, no import back to bg/core.md | Agrees with bg/core.md, disagrees with TTRPG |
| `params/threadwork.md:65-101` | PULLED / REFERENCED (elaboration, not override) | Three-Axis Ob is its own additive formula layered on top of, not contradicting, the base scale | Consistent (additive) |
| `params/mass_combat.md`, `params/contest.md` (no independent cap stated) | PULLED / REFERENCED | No literal Ob-cap restated; implicitly deriving from core.md | Yes (nothing to disagree with) |

---

## 3. Expected Value / EV

**Home definition.** `params/core.md:107-133` ("Expected Value (per die)"): table of E[net]/σ²/σ per die by TN (TN6=0.50/0.65/0.806, TN7=0.40/0.64/0.800, TN8=0.30/0.61/0.781), used to parameterize the continuous-engine Normal(μN, σ√N) sampling (`params/core.md:64`). `references/glossary.md:139`: "Expected Value | EV | Probability-weighted average outcome per die or pool. Used in simulation analysis."

**Exhaustive usage sweep.** Narrow footprint by design — this is a simulation/math term, not a play-facing mechanic name. Confirmed occurrences: `params/core.md:21,64,107-131` (home), `designs/scene/combat_engine_v1/phase4_5_plan_v1.md:141,243` ("the d10 dice-model EV math + game theory... as the payoff substrate"), and scattered `tests/sim/*` / `sim/*` files performing Monte Carlo validation against the E[net] table (e.g. `tests/sim/phase5_continuous_engine_2026-05-15.py`, cited directly by `params/core.md:66`).

**Divergence check.** None found. Every live occurrence either restates the same TN-keyed E[net] table or cites it by reference; no second, conflicting "EV" formula exists anywhere in the corpus. The one thing worth flagging is not a divergence but a **dangling reference**: `params/core.md:133` points to `references/tn_full_tables.md` ("generate via dice-model Task 8 if absent") — **this file does not exist** (`ls` confirms). Any consumer following that pointer today gets nothing.

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `params/core.md:107-133` | CANONICAL DEFINITION | — | — |
| `designs/scene/combat_engine_v1/phase4_5_plan_v1.md:141,243` | PULLED / REFERENCED | Named as "the d10 dice-model EV math" — cites the substrate, states no independent number | Yes (no independent literal) |
| `tests/sim/phase5_continuous_engine_2026-05-15.py` (+ sibling phase*.py) | PULLED / REFERENCED | Validation code explicitly cited by `params/core.md:66` as the source of the "0.029/0.022 max deviation" claim | Yes |
| `references/tn_full_tables.md` (cited, absent) | UNCLEAR / NO CANONICAL SOURCE | File referenced but does not exist on disk | N/A — nothing to agree/disagree with |

---

## 4. Degree of Success

**Home definition.** `params/core.md:46-55` / `references/glossary.md:140`: "Degree of Success | — | Outcome tier: Overwhelming / Success / Partial / Failure." Four-tier structure keyed off `net` vs `Ob`.

**Exhaustive usage sweep.** The four-tier vocabulary (Overwhelming/Success/Partial/Failure) recurs identically across `params/threadwork.md` (Dissolution Gap Creation table, `:132-137`), `params/bg/core.md:65-75`, `params/mass_combat.md`, `designs/threadwork/threadwork_v30.md` (dozens of per-operation degree tables, e.g. `:281-284,341-344,392-395,427-430,476-479`), `designs/scene/combat_v30.md`, `params/fieldwork.md:163` (Knot Formation).

**Divergence check.** The base four-tier vocabulary is consistent everywhere I sampled. But **Debate/Contest content has grown a second, unrelated degree taxonomy that the glossary's "Degree of Success" entry never acknowledges exists**: `designs/npcs/npc_behavior_v30.md:719-728` (§6.4.2, ED-775) maps Piety-Track outcomes to a **six-tier** scale — "Total Victory ≥9 / Decisive 7-8 / Compromise 5-6 (mid) / Compromise 4 (barely) / Partial 3 / Failure ≤2" — driven by the Piety Track's 0-10 gauge, not by net-vs-Ob at all. This is a legitimate subsystem-specific elaboration (Debate resolves on a position track, not a single roll), but it means "Degree of Success" is not a single closed vocabulary corpus-wide, and the glossary doesn't cross-reference or disambiguate the two systems anywhere.

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `params/core.md:46-55` | CANONICAL DEFINITION | — | — |
| `designs/threadwork/threadwork_v30.md` (dozens of per-op tables) | PULLED / REFERENCED (instantiation) | Each op-specific table reuses the same 4-tier labels applied to its own consequence set | Yes |
| `params/bg/core.md:65-75` | HARDCODED DUPLICATE | See Term 2 — restates the tier logic with a divergent Ob-10 exception band | Partially (see Term 2) |
| `designs/npcs/npc_behavior_v30.md:719-728` | UNCLEAR / NO CANONICAL SOURCE (parallel taxonomy) | Six-tier Piety-Track mapping; not derived from or reconciled with the glossary's 4-tier "Degree of Success" entry anywhere | N/A — different structure, not "agreement" or "disagreement," just uncatalogued |

---

## 5. Overwhelming

**Home definition.** `params/core.md:49,54-55`: "Overwhelming | Net ≥ 2× Ob AND net ≥ 3 (+1 Momentum)... Overwhelming requires a minimum of 3 net successes regardless of Ob. (PP-232)." `references/glossary.md:141`: **"Overwhelming | — | Net successes ≥ 2× Ob AND ≥ 3 minimum (TTRPG, PP-232); ≥ Ob + 1 (BG, provisional)."**

**Exhaustive usage sweep.** Confirmed consistent (2×Ob AND ≥3) in `params/core.md:49,54,176-180`, `params/fieldwork.md:163` (Knot Formation), `params/threadwork.md:42,132-137` (Knot/Dissolution tables), `designs/threadwork/threadwork_v30.md` (all per-operation tables), `params/bg/faction_actions.md:146` ("Enhancement (Overwhelming only — net ≥ 2×Ob AND ≥3)").

**Divergence check — the glossary's own home-adjacent entry is stale.** `params/bg/ed_resolutions.md` contains **two contradictory "final" BG-Overwhelming rulings in the same file**:
- `params/bg/ed_resolutions.md:83-87` ("BG Overwhelming Threshold — Final, PP-281/PP-299"): *not* struck — "BG Overwhelming = Ob+1 surplus... ED-031 correct. PP-179 was documentation error."
- `params/bg/ed_resolutions.md:157-166` ("ED-142 Resolution PP-322" + "BG Overwhelming — Final Ruling PP-262"): explicitly **`[STRUCK — superseded by PP-249: BG Overwhelming = net ≥ 2×Ob AND net ≥ 3.]`** — i.e., a later patch reverses the Ob+1 ruling back to matching-TTRPG.

The higher patch number (PP-322 > PP-299/281) and the fact that **`params/bg/core.md:65-75`'s actual live Degree Table is explicitly labeled "PP-179 + PP-249 — matches TTRPG"** confirm the currently-operative BG rule is 2×Ob AND ≥3 (matching TTRPG), not Ob+1. Yet **`references/glossary.md:141` — the term's own dictionary entry — still cites the superseded "≥ Ob + 1 (BG, provisional)" formula**, contradicting both `params/bg/core.md`'s live table and the later of the two ed_resolutions.md rulings. This is a direct, precisely-locatable currency failure in the home glossary entry itself, not just a downstream doc.

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `params/core.md:49,54-55` (TTRPG) | CANONICAL DEFINITION | — | — |
| `params/bg/core.md:65-75` | CANONICAL DEFINITION (BG-mode parallel head) | Self-labeled "PP-179 + PP-249 — matches TTRPG"; still carries open `[FLAGGED ED-142-R]` | Yes, internally, but see Term 2 for the Ob-10 exception-band conflict |
| `references/glossary.md:141` | HARDCODED DUPLICATE, **STALE** | Independently states "≥ Ob + 1 (BG, provisional)" — the superseded ED-031/PP-281 formula | **No** — contradicts the live `params/bg/core.md` table and the later PP-322 ruling |
| `params/bg/ed_resolutions.md:83-87` | HARDCODED DUPLICATE, superseded-but-unmarked | States the Ob+1 rule as "Final" with no strike banner, even though a later entry in the same file supersedes it | No (superseded by the file's own later entry) |
| `params/bg/ed_resolutions.md:157-166` | CANONICAL-ADJACENT (latest ruling) | Explicitly struck/superseded chain, ends at "matches TTRPG" | Yes (this is the correct current state) |
| `designs/threadwork/threadwork_v30.md`, `params/threadwork.md`, `params/fieldwork.md` | PULLED / REFERENCED | Each instantiates the 4-tier table per-operation without restating the general formula independently | Yes |

---

## 6. Partial

**Home definition.** `params/core.md:51`: "Partial | Net > 0 but < Ob." `references/glossary.md:142`: "Partial | — | Net successes > 0 but < Ob."

**Exhaustive usage sweep.** Consistent everywhere the 4-tier degree table is instantiated (see Term 4/5 citations). Additional Ob-cap-exception instances: `params/core.md:55` ("Ob 20 exception... Partial requires net ≥ 10"), `params/bg/core.md:74` ("Ob 10 exception... Partial requires net ≥ 5" — see Term 2's divergence).

**Divergence check.** Beyond the already-documented Ob-20-vs-Ob-10 exception-band split (Term 2), one further structural divergence: `params/mass_combat.md:322-327` ("BG Battle Partial outcome, PARAMS-GAP-06-MC resolved") defines Partial via **margin between two opposed rolls**, not net-vs-Ob at all: `"Margin = |attacker net − defender net|... Margin ≤ 1 (either direction) → Partial: no territory change, Attacker Stability −1."` This reuses the word "Partial" for a genuinely different formula (opposed-margin comparison, not single-roll-vs-Ob) in a different game mode. It is explicitly self-flagged as unconfirmed: `[PROVISIONAL — pre-ledger: confirm Partial threshold and Stability cost]` — so it's a known-open item, not a silent drift, but it does mean "Partial" denotes two structurally different mechanics (single-roll-vs-Ob vs. opposed-margin) under one label, uncatalogued by the glossary.

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `params/core.md:51` | CANONICAL DEFINITION | — | — |
| `params/bg/core.md:70,74` | HARDCODED DUPLICATE | See Term 2/5 — Ob-10 exception band diverges from core.md's Ob-20 | Partially (base formula agrees; exception band diverges) |
| `designs/threadwork/threadwork_v30.md`, `params/threadwork.md:132-137` | PULLED / REFERENCED | Instantiates the tier in per-op tables | Yes |
| `params/mass_combat.md:322-327` | UNCLEAR / NO CANONICAL SOURCE (structurally distinct mechanic, same name) | Margin-based opposed-roll formula, self-flagged `[PROVISIONAL]`, not reconciled with the net-vs-Ob "Partial" definition | N/A — different mechanism entirely, open/provisional by its own admission |

---

## 7. CI (glossary Part Twelve collision entry)

**Home definition.** `references/glossary.md:74`: "Church Influence | CI | 0-100 | ALL | 0 (TTRPG) / 28 (BG) | ... Per `designs/provincial/ci_political_v30.md` §2.1 (canonical)." Collision table at `references/glossary.md:241`: "CI | ~~Church Influence~~ (renamed CI per ED-782) | ~~Piety Track~~ (now CT) | **Do not use CI.** Write `CI` for Church Influence; `Piety Track` (or `CT` in technical contexts) for the debate tracker." (Note the entry's own wording is self-contradictory shorthand — "do not use CI... write CI for Church Influence" — meaning: don't use CI *for Piety Track*, CI-for-Church-Influence is fine.)

**Exhaustive usage sweep.** `\bCI\b` hits 331 files. Sampled broadly across `params/bg/*`, `designs/provincial/*`, `canon/*` — overwhelmingly "CI" = Church Influence, consistent with the home table. The glossary's own currency claim is backed by `references/censured_vocabulary.yaml:102-110` ("TC (as Church Influence)" entry): residual_count 2 as of 2026-04-30 (post-PP-691 sweep), located in `npc_character_analyses_v30.md` (1) + `mass_battle_v30.md` (1) — i.e. the ambiguous *old* abbreviation "TC" (not bare "CI") is what's tracked as residual, and it's down to 2 instances.

**Divergence check.** The collision-resolution note's own claim about the *other* side of the collision doesn't hold up: it says the debate/Piety-Track abbreviation is "CT" (also stated as the Part Three home entry, `glossary.md:86,94`: "Piety Track | CT* | ... `CT` is the preferred abbreviation"). But a corpus sweep shows **live usage overwhelmingly prefers `PT`, not `CT`**, for Piety Track: `grep -rl '\bPT\b'` returns 133 files (`params/bg/core.md`, `params/bg/ci_seizure.md`, `params/bg/victory.md`, `params/board_game_misc.md`, `params/contest_extensions.md`, `designs/provincial/ci_political_v30.md`, `designs/provincial/clock_registry_v30.md`, `designs/provincial/victory_v30.md`, etc.), e.g. `params/bg/core.md:117` "**Starting Piety Track (PT) values**" and `params/bg/ci_seizure.md:31` "Ob = 10 − PT − infrastructure modifiers." By contrast `grep -rl '\bCT\b'` (excluding Mermaid/English false positives) returns only ~25 files, and spot-checking shows most of those "CT" hits are *not* about Piety Track at all — `references/alias_registry.yaml:169-181` and `references/censured_vocabulary.yaml:169-181` instead track **"CT (abbreviation for Conviction Track)"** as its own separate, still-unresolved deprecated abbreviation (a *different* term than Piety Track, per that same registry: `"CV (abbreviation for Conviction Track)... rename pending"`). So the glossary's own CI-collision resolution text cites an abbreviation ("CT" for Piety Track) that (a) essentially nobody in the live corpus actually uses for that purpose, and (b) collides with a *third*, separately-tracked, still-unresolved "CT = Conviction Track" abbreviation that the glossary's Part Twelve table never lists at all. Also worth noting: `designs/personal/conviction_track_v1.md` — the doc the glossary cites as Piety Track's canonical home (`glossary.md:86`) — is itself titled "Valoria — Piety Track" but its actual content (line 8-12) describes **Conviction Scars / Conviction crisis**, not a 0-10 win/lose debate gauge — suggesting "Piety Track" and "Conviction Track" may be tangled/conflated at the source-doc level, not just at the abbreviation level. (This last point is adjacent to, not strictly inside, this batch's assigned term list; flagged for completeness since it directly undermines the CI-collision entry's own resolution text.)

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/glossary.md:74` (Church Influence) | CANONICAL DEFINITION | — | — |
| `designs/provincial/ci_political_v30.md` §2.1 | CANONICAL DEFINITION (design-doc home, per glossary's own citation) | — | — |
| `params/bg/*.md`, `designs/provincial/*.md` (CI-for-Church-Influence, hundreds of sites) | PULLED / REFERENCED / HARDCODED mixed | Numeric thresholds (40/55/60/65/80/100) mostly restated as literals per-file, not imported | Yes, broadly consistent |
| `references/censured_vocabulary.yaml:102-110` | PULLED / REFERENCED (tracking registry) | Explicit residual count (2) for the old "TC" abbreviation | Accurately tracked, small residual |
| `references/glossary.md:86,94,241` (CT = Piety Track claim) | HARDCODED DUPLICATE, **STALE / not reflective of live usage** | Asserts "CT" as preferred Piety-Track abbreviation; corpus predominantly uses "PT" instead (133 files) | **No** — doesn't match actual corpus practice |
| `references/alias_registry.yaml:169-181` / `censured_vocabulary.yaml:169-181` | UNCLEAR / NO CANONICAL SOURCE | Tracks "CT" as an abbreviation for a *different* term (Conviction Track), unresolved/pending rename, never cross-referenced against the glossary's CI collision entry | N/A — a live, uncatalogued second collision |

---

## 8. CP (Part Twelve collision — verify no live "Combat Power" usage remains)

**Home definition.** `references/glossary.md:159,242`: "CP = Character Points only [ED-136]. Use 'Power' for the unit offensive stat." Confirmed by `references/alias_registry.yaml:531-535` and `references/censured_vocabulary.yaml:52-60` ("Combat Power" residual_count: **0** as of 2026-04-30).

**Exhaustive usage sweep — the claim does NOT hold today.** Legitimate "CP = Character Points" usage is confirmed live in `designs/provincial/strategic_layer_v30.md:752-792` ("§9.12 CP Awards from Board Game Successes"), `designs/provincial/factions_personal_v30.md:428`, `designs/scene/derived_stats_v30.md:188-221`, `designs/videogame/godot_architecture_specification.md:367,449`. **But bare "CP" meaning the old, struck "Combat Power" stat is also still live**:
- `designs/scene/combat_v30.md:419`: "Roll Artillery **CP** vs Ob..."
- `designs/scene/combat_v30.md:436`: "Rally the Broken (W-33): Effective only for **CP ≥ 3** units."
- `designs/scene/combat_design_v1.md:354`: "**Power (CP):** Dice pool ceiling." — using "CP" as if it were Power's own abbreviation (a third variant).
- `designs/scene/combat_design_v1.md:361` and `designs/scene/combat_v30_infill.md:68`: "**Effective CP = min(CP, current Strength).**" — "current Strength" is itself a pre-PP-232 term (renamed to Size), confirming this text predates the rename and was never swept.
- `designs/scene/combat_design_v1.md:377,391`: "Roll Artillery CP vs Ob..." / "effective only for CP ≥ 3 units" (duplicate of combat_v30.md's phrasing in its sibling doc).
- `params/mass_combat.md:313`: "Sling: effective **CP** −2D; ammo modifier per unit table above." — a single residual instance in an otherwise fully-renamed file (the rest of `params/mass_combat.md` consistently uses "Power").

**Divergence check.** This directly contradicts the censured_vocabulary.yaml's "residual_count: 0" claim and the glossary's flat assertion that CP is unambiguous. The residual sits in `designs/scene/combat_v30.md` / `combat_design_v1.md` / `combat_v30_infill.md` (all personal-combat docs banner-marked `[PARTIALLY SUPERSEDED]` for *resolution* content, but the Artillery/Rally/pool-ceiling passages read as live prose, not obviously excluded by that banner's scope) plus one line in the currently-uncontested `params/mass_combat.md`.

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/glossary.md:159,242` | CANONICAL DEFINITION | — | — |
| `designs/provincial/strategic_layer_v30.md:752-792`, `designs/scene/derived_stats_v30.md:188-221` | HARDCODED DUPLICATE (legitimate sense) | Independent prose using CP = Character Points, matches canon | Yes |
| `references/censured_vocabulary.yaml:52-60` | PULLED / REFERENCED (tracking registry) | Asserts residual_count 0 — **this is itself stale/wrong** per the finds below | **No** — contradicted by live residue |
| `designs/scene/combat_v30.md:419,436` | HARDCODED DUPLICATE, **live residual of struck sense** | Independent "CP" as Combat-Power-successor stat, in a doc marked partially-superseded but not for this content | No — reintroduces the struck CP=Combat-Power sense |
| `designs/scene/combat_design_v1.md:354,361,377,391` | HARDCODED DUPLICATE, **live residual, third variant** | Uses "CP" both as Power's own abbreviation and the old pool-ceiling sense; no supersession banner on this file at all | No |
| `designs/scene/combat_v30_infill.md:68` | HARDCODED DUPLICATE, **live residual** | Same "Effective CP = min(CP, current Strength)" line, co-file of combat_v30.md | No |
| `params/mass_combat.md:313` | HARDCODED DUPLICATE, **live residual** | Single leftover "CP" in an otherwise fully "Power"-renamed file | No |

---

## 9. TD (Part Twelve collision — verify no live Thread-Depth usage outside historical sense)

**Home definition.** `references/glossary.md:62,243`: "Thread Depth | TD | **REMOVED (PP-166)**... phantom definition... Not tracked." Collision resolution: "TD | Thread Depth (REMOVED) | Top-Down (Mermaid) | ... not a game term." Confirmed by `references/censured_vocabulary.yaml:72-80`: residual_count **0** as of 2026-04-30, and `params/threadwork_superseded.md:34-35` explicitly documents the strike.

**Exhaustive usage sweep.** "Thread Depth" the phrase does not reappear as a live mechanic anywhere current — confirmed 0 in `designs/threadwork/threadwork_v30.md`, `params/threadwork.md`. All corpus hits for the phrase are either the strike-annotation itself, tracking registries, or old audit-finding prose calling it a "dead stat" (`tests/audit/aud_ttrpg_01.md:36,75` — historical). Bare `\bTD\b` as Mermaid syntax is legitimate and separate.

**Divergence check — the collision table itself is incomplete, and this is the more important finding.** Bare **"TD" has a third, live, active meaning the glossary never lists at all: "Theological Dissatisfaction (TD)"**, a Hafenmark-specific faction track, range 0-5, defined at `params/bg/tracks.md:1,13-88` ("## TD (Theological Dissatisfaction) (PP-181, v04 B5 confirmed)... ## Hafenmark — RDT/TD Tracks (ED-321 RESOLVED)... Reformed Doctrine Track (RDT) — Range 0–5... Theological Dissatisfaction (TD) — Range 0–5. Activates at RDT 2. Advances: +1 per arc..."), also referenced live in `designs/scene/miraculous_event_v30.md:80,82,104,136` ("RDT/TD interaction... TD escalation penalises Church assertion. At TD 3...") and `designs/world/solmund_master_document.md:448,470,496` (identical passages). `params/board_game.md:270-278` cross-lists both "RDT (Reformed Doctrine Track)" and "TD (Theological Dissatisfaction)" as confirmed PP-181/v04-B5 tracks. This is a genuinely live, actively-cited abbreviation collision (Thread Depth-removed vs. Mermaid-syntax vs. Theological-Dissatisfaction-live) that `references/glossary.md:243`'s two-way collision table doesn't capture at all. Tangentially, `designs/architecture/canonical_registry.md:130-132` (a different, partially-superseded registry, dated 2026-04-15) separately claims **"Struck: ... RDT ..."**, directly contradicting `params/bg/tracks.md`'s "ED-321 RESOLVED" active status for the same track — a further live cross-doc conflict about whether RDT/TD even still exists, unrelated to the Thread-Depth sense.

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/glossary.md:62,243` | CANONICAL DEFINITION (Thread-Depth-removed sense only) | — | — |
| `references/censured_vocabulary.yaml:72-80` | PULLED / REFERENCED (tracking registry) | residual_count 0 for "Thread Depth" phrase — accurate for that phrase | Yes, for the phrase it tracks |
| `params/bg/tracks.md:13-88` | CANONICAL DEFINITION (**separate, uncatalogued sense**) | Defines "TD" = Theological Dissatisfaction as an active track | N/A — a live third meaning absent from the collision table |
| `designs/scene/miraculous_event_v30.md:80-136`, `designs/world/solmund_master_document.md:448-496` | HARDCODED DUPLICATE (of the TD=Theological-Dissatisfaction sense) | Independent restatement of "RDT/TD" interaction prose in two sibling docs | Consistent with each other; both uncatalogued by the glossary |
| `params/board_game.md:270-278` | PULLED / REFERENCED (TOC/index pointer) | Table-of-contents-style citation into `params/bg/tracks.md` | Consistent |
| `designs/architecture/canonical_registry.md:130-132` | HARDCODED DUPLICATE, **conflicting** | Claims RDT is struck, contradicting tracks.md's "ED-321 RESOLVED" active status | No — direct cross-doc conflict, unrelated to the Mermaid/Thread-Depth collision but compounding TD's overall ambiguity |

---

## 10. COMP (Part Twelve collision)

**Home definition.** `references/glossary.md:51,89,244`: "Composure | — | varies | Social endurance track. Used in Debate. Rattled at ≤2; concession forced at 0" (Part One) and "Composure | — | varies | Social endurance (see Part One). **Also the damage track in Debate exchanges**" (Part Three). Collision resolution: "COMP | Composure (Debate context) | Computation/Composition (general English) | Write 'Composure' in game documents."

**Exhaustive usage sweep.** All-caps "COMP" is rare and confined to `references/mechanical_terms_index.md`, `references/alias_registry.yaml:541-545`, `references/silo_overlap_matrix.yaml`, `references/glossary.md`, and old `tests/sim/sim_ttrpg_batch_*.md` output logs (as shorthand). Separately, mixed-case **"Comp"** (an informal shorthand, distinct from the registered all-caps abbreviation) is used **12 times in `params/threadwork.md`** (e.g. `:223,224,227,236,245,251`: "Coh 3.2; +1 Ob, 2 Comp") and 9 times in `params/threadwork_superseded.md`, plus a few in `tests/sim/sim_d05_debate_resim.md` and `designs/threadwork/threadwork_v25_historical.md` — an undocumented variant abbreviation the glossary's collision table doesn't mention at all.

**Divergence check — the collision entry's own guidance ("Write 'Composure' in game documents" for the Debate context) is stale relative to a ratified rename.** `params/contest.md:133,137,143-161` documents: **"CR3 (RATIFIED 2026-06-01) retires Composure as the social-contest tracker and splits it into Concentration (stamina) + Face (contest-local ethos/standing)."** `designs/scene/social_contest_v30.md:229-254,481-499` confirms the same, repeatedly and explicitly (ED-1056): *"the single Composure buffer is RETIRED as the social-contest tracker and split into the two distinct trackers whose roles it conflated... Face is the social analogue of standing/composure... this is a RENAME of the contest buffer's role (Composure → Face-as-standing)."* This is scoped ("Composure references in unrelated systems — knots, combat, conviction — are NOT touched by CR3," `social_contest_v30.md:247`), so Composure remains valid in those other contexts (matching Part One's broader definition) — but **Part Three's specific claim that Composure is "the damage track in Debate exchanges" is now wrong**: the Debate/Contest damage track is "Face," not "Composure," as of a ratification (2026-06-01/2026-07-01, ED-1056) that postdates the glossary's own last full sweep (`glossary.md:3`: "content last swept 2026-04-30, PP-691"). Confirmed: `grep -c "Face\|CR3\|ED-1056" references/glossary.md` = 0 — the glossary has never been touched to reflect this rename, despite CLAUDE.md's stated convention that the glossary should update "in the same commit as any file that introduces or retires a term."

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/glossary.md:51,89,244` | CANONICAL DEFINITION | — | — |
| `references/alias_registry.yaml:541-545` | PULLED / REFERENCED | Restates the same collision resolution ("Write 'Composure' in game documents") | Stale in the same way as the glossary (see below) |
| `params/contest.md:133-161` (CR3/ED-1056) | CANONICAL DEFINITION (**live head, supersedes the glossary's Part Three claim**) | Ratified 2026-06-01, explicit retirement + split | — |
| `designs/scene/social_contest_v30.md:229-254,481-499` | CANONICAL DEFINITION (co-file, consistent with contest.md) | Repeated, explicit ED-1056 rename documentation | Consistent with contest.md; **both contradict glossary Part Three** |
| `references/glossary.md:89` ("Also the damage track in Debate exchanges") | HARDCODED DUPLICATE, **STALE** | Independent claim, never updated post-ED-1056 | **No** — the Debate damage track is now "Face," not "Composure" |
| `params/threadwork.md` (12×, e.g. `:223-251`), `params/threadwork_superseded.md` (9×) | HARDCODED DUPLICATE (undocumented variant) | Informal "Comp" shorthand for Composure damage, not itself tracked as an abbreviation anywhere | Agrees with the *unretired* (knots-context) sense of Composure, which CR3 explicitly leaves untouched |

---

## 11. RS (Part Twelve collision — quantify the glossary-currency gap)

**Home definition (per the glossary's claim).** `references/glossary.md:73`: "Mending Stability | MS | 100→0 | ALL | ... **Renamed from Rendering Stability (RS) per ED-731.**" Collision table `references/glossary.md:245`: "RS | ~~Rendering Stability~~ (renamed MS per ED-731) | — | Use Mending Stability (MS). **RS appears only as historical annotation in `canon/02_foundations_amendment_leap_mechanism.md` per intentional retention.**" This exact claim is echoed verbatim in `references/synonym_registry.yaml:9-10`: "Historical RS retained only in canon/02 annotations by intentional design," and tracked in `references/censured_vocabulary.yaml:82-90` with **residual_count: 1** (audited 2026-04-30), located at `canon/02_foundations_amendment_leap_mechanism.md (1)`.

**First correction: even the "1 historical annotation" isn't a bare "RS" token.** `canon/02_foundations_amendment_leap_mechanism.md:88` reads: "...§5 (Mending Stability; **formerly Rendering Stability** per ED-731)..." — the full phrase spelled out, not the abbreviation "RS" at all. `Grep '\bRS\b' canon/02_foundations_amendment_leap_mechanism.md` returns **zero matches**. So the tracked "residual" isn't even an instance of the abbreviation in question — the censured_vocabulary.yaml audit was tracking the full phrase **"Rendering Stability"**, not the bare token **"RS"**, and those are two different search targets that the glossary/registry conflate.

**Exhaustive usage sweep — bare `\bRS\b` is pervasive, not singular.** Corpus-wide: 6,934 raw token matches across ~474 files (`grep -c` by directory: 199 `tests/`, 158 `designs/`, 57 `archives/`, 27 `references/`, 10 `tools/`, 10 `params/`, 7 `deprecated/`, 3 `canon/`, 2 `sim/`, 1 `handoffs/`). Restricting to the two files this batch specifically asks about:
- **`params/threadwork.md`: 27 bare "RS" occurrences** — `:3,4,27,81,117,133,139,141,142,166,186,187,221,223,224,225,227,245,251,270,271,272,273,283,287` — including its own dedicated **"## RS Track (PP-603 — canonical)"** section (`:139-142`: "Range 100→0... Starting: videogame canonical 60... RS = 0: Rupture (shared loss)").
- **`designs/threadwork/thread_horizontal_integration_spec.md`: 17 bare "RS" occurrences** — `:16,35,70,73,96,102,126,194,195(×2),199,202,206` — e.g. `:70`: "RS ≤ 20 (Critical) in current territory | Thread Crisis scene..."; `:194`: "Priority gate: If RS ≤ 25, reduce all offensive Thread operations to defensive only... RS preservation overrides tactical advantage."

**Both files are declared canonical today**, not historical relics: `references/canonical_sources.yaml:112-116` lists `params: params/threadwork.md` as the canonical params file for threadwork; `references/canonical_sources.yaml:484-487` lists `designs/threadwork/thread_horizontal_integration_spec.md` as a canonical design doc; and `CURRENT.md:46` names the Threadwork current head as `designs/threadwork/threadwork_v30.md` **"(+ thread_horizontal_integration_spec.md)."** Both predate the 2026-04-20 ED-731 rename (`params/threadwork.md` is self-dated "CANONICAL STATE 2026-04-14"; `thread_horizontal_integration_spec.md` is dated 2026-04-17, "Status: CANONICAL") and were simply never swept afterward.

**Quantifying the gap precisely:** the glossary/registry claim is **1** residual, historical-only, of the *full phrase* "Rendering Stability." The actual count of the *bare abbreviation* "RS" (the thing actually being used to mean the same track) is **44** in just the two files this batch names, **0** of which are historical annotations — all 44 are live active-mechanic prose in currently-declared-canonical documents. Corpus-wide the bare-token count is in the thousands, spread across `designs/` non-audit files alone in 44 distinct files (sampled: `designs/npcs/npc_behavior_v30.md` — see below, a different sense; `designs/territory/settlement_layer_v30.md:449,563-564`; `designs/architecture/scale_transitions_v30.md:102,212,222,293`; `designs/scene/combat_v30.md:458,562,594,603` — the last two explicitly stating "RS=72"/"RS=60," matching core.md's TTRPG-60/BG-72 Mending-Stability starting values verbatim; `designs/scene/miraculous_event_v30.md:41,134`; `canon/patch_register_index.md:74,128`; `references/module_contracts.yaml:691` which itself flags a second-order stale-index bug: *"RS_v30_index.md STALE: §5.1 indexed as 'RS=0' but doc reads 'MS=0'"*).

**Second, unflagged collision discovered in the sweep: "RS" also means "Resonant Style," entirely uncatalogued.** `designs/npcs/npc_behavior_v30.md` (the current NPC-behaviour canonical head per `CURRENT.md:51`) uses bare "RS" at least 7 times (`:461,711,713,714,723,734×2`) meaning **"Resonant Style"** (a Debate/Contest concept — §6.4.1 "RS Declaration Timing," §6.4 "Wrong-Style Penalty"), e.g. `:711`: "the orator cannot switch RS mid-Contest," `:723`: "Orator's RS proved adequate regardless of style choice." The phrase "Resonant Style" does not appear anywhere in `references/glossary.md` at all (`grep` returns zero hits) — so this is a third live sense of bare "RS" (Rendering/Mending-Stability, Resonant Style, and the coincidental `flowchart` non-issue is a different abbreviation TD not RS) with zero glossary coverage.

**Root cause of the gap:** `references/censured_vocabulary.yaml`'s audit methodology (and by extension whatever fed the glossary's claim) appears to have searched for the **full phrase** "Rendering Stability" rather than the bare **abbreviation** "RS" — a full-phrase text search would correctly find only 1 hit (the canon/02 full-phrase annotation) while completely missing every file that used the bare two-letter abbreviation without ever spelling out the retired full name.

**Classification table** (representative — full per-file breakdown of all 474 files is impractical; every row below is independently verified):

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/glossary.md:73` (MS = renamed-from-RS) | CANONICAL DEFINITION | — | — |
| `references/glossary.md:245`, `references/synonym_registry.yaml:9-10` | UNCLEAR / NO CANONICAL SOURCE (claim doesn't match corpus) | Asserts RS = 1 historical-only residual; based on a full-phrase (not abbreviation) search | **No** — 44+ bare "RS" hits found in just the two files named in this batch, none historical |
| `canon/02_foundations_amendment_leap_mechanism.md:88` | CANONICAL-ADJACENT (the cited "residual" itself) | Spells out "formerly Rendering Stability" in full — not even a bare "RS" token | N/A — mislabeled as "the" RS residual when it isn't an RS-abbreviation instance at all |
| `params/threadwork.md` (27×, e.g. `:139-142`) | HARDCODED DUPLICATE, **live, un-swept, canonical** | Independent "RS Track" section with its own starting values, drain rules, thresholds — no import mechanism back to `params/core.md`'s "Mending Stability" | Same underlying track/values as MS (RS=60/72 matches MS=60/72), but under the retired name |
| `designs/threadwork/thread_horizontal_integration_spec.md` (17×, e.g. `:70,194,195,202,206`) | HARDCODED DUPLICATE, **live, un-swept, canonical** | Independent prose using bare "RS" for threshold/priority-gate logic, declared canonical in CURRENT.md | Same, under the retired name |
| `designs/scene/combat_v30.md:458,562,594,603` | HARDCODED DUPLICATE, **live** | "RS=72"/"RS=60" as literal starting-value citations | Values agree with MS; name is stale |
| `designs/npcs/npc_behavior_v30.md:461,711-734` | CANONICAL DEFINITION (**separate, uncatalogued sense**) | "RS" = Resonant Style, a live Debate mechanic never listed in the glossary at all | N/A — a wholly different, undocumented collision |
| `references/module_contracts.yaml:691` | PULLED / REFERENCED (flags a downstream consequence) | Notes an index file stale on "RS=0" vs body's "MS=0" | Documents that the RS/MS drift has already caused a real index/body mismatch elsewhere |
| `designs/threadwork/threadwork_v30.md` (current design head) | CANONICAL, **correctly swept** | Consistently uses "Mending Stability" in full throughout (spot-checked ~40 lines) | Yes — contrast case showing the design doc *did* get swept while its co-cited params/spec siblings did not |

---

## 12. CERT, TLK, DD, FSTAT, CE, INT (Part Thirteen deprecated abbreviations)

**Home definitions.** `references/glossary.md:255-262`:
```
CERT | Certainty (0–5; PP-551). See Part One. | RESOLVED — active stat
TLK  | Torben Loyalty Clock (10→0; F72 gap). | DEPRECATED — historical only
DD   | Deniability Debt (Niflhel Operative). | DEPRECATED — abbreviation not in active use
FSTAT| Faction Stats (collective). | DEPRECATED — simulator code, never in-game term
CE (track code) | Combat Endurance. See Part Five. | RESOLVED — active stat
INT (track code)| Intel (Int faction stat). See Part Four. | RESOLVED — active stat
```
Full-form homes: Certainty `glossary.md:53` (Part One); Combat Endurance `glossary.md:120` (Part Five: "Stamina resource tracking in extended combat. Sub-application of Stamina; not a separate stat track"); Intel `glossary.md:108` (Part Four, column abbreviation "Int"). `references/alias_registry.yaml:561-579` is the declared authority for TLK/DD/FSTAT.

**Exhaustive usage sweep and divergence check, per term:**

- **CERT**: bare all-caps "CERT" found only in `references/glossary.md` (3×, all as the "not standalone" exception notes) and `references/mechanical_terms_index.md` (1×). Zero live occurrences of the bare abbreviation in any design/params doc — everyone correctly writes "Certainty" in full, matching the glossary's own instruction ("*CERT not standalone — write Certainty.*"). **No divergence.**

- **TLK**: bare "TLK" appears only in `references/deprecated_terms_registry.yaml`, `references/mechanical_terms_index.md`, `references/alias_registry.yaml`, `references/glossary.md` (all tracking/registry docs, correctly labeling it deprecated) and in historical `archives/session/session_log_archive_part_5.md`/`part_7.md` and old `tests/sim/sim_ttrpg_batch_02/04/legacy_03.md` stress-test logs (2026-04-era, pre-dating the deprecation). **No live design/params doc uses it. No divergence.**

- **DD**: same pattern — confined to registry files and old `tests/sim/sim_ttrpg_batch_02/07/08/09/10.md` / `sim_thread_batch_06.md` / `sim_cascade_01.md` stress logs. Spot-checked `tests/sim/sim_ttrpg_batch_09.md:240-265`: discusses "DD" (Deniability Debt) for the Riskbreaker/Niflhel mechanic in a pre-strike (Niflhel not yet struck) context — consistent with the registry's account that DD's *mechanic* (Deniability Debt, full name) survives in isolated retained contexts but the *abbreviation* is not live. **No divergence found in current canon**, though note the full phrase "Deniability Debt" (not the abbreviation) is explicitly still permitted per `alias_registry.yaml:568-573` where "the mechanic survives... Mechanic functions redistributed to settlement-broker."

- **FSTAT**: same pattern — confined to registry docs plus a very large number of old `tests/sim/sim_ttrpg_batch_*.md` files (2026-04 stress-test logs, e.g. `sim_ttrpg_batch_02` through `_10`, `sim_combat_batch_11.md`, `sim_mass_battle_batch_11.md`). Zero live design/params occurrences. **No divergence.**

- **CE**: Part Five's "Combat Endurance = sub-application of Stamina" is not actually restated anywhere as a mechanic — `grep "Combat Endurance" designs/scene/derived_stats_v30.md` returns nothing; the term has no independent design-doc home beyond the glossary's own one-line description. **A second, wholly different, undocumented "CE" surfaces live in the arcs corpus**: `designs/arcs/arcs_31_35.md:119,122,123,193,197,337,340`, `designs/arcs/narrative_scenario_chains.md:745`, `designs/arcs/arcs_24_27.md:25,33`, `designs/arcs/gm_ref/arcs_01_04.md:102`, `designs/arcs/arcs_28_30.md:147` all use "**Combat Endurance**" (the full phrase, not just "CE") as an **Inquisitor long-running suspicion/exposure-accumulation track** against Thread-sensitive NPCs (e.g. "Klapp Combat Endurance track... §13.6... Heresy Investigation filed within 2 seasons," "Inquisitor Combat Endurance dossier on Maret for two seasons") — a multi-session narrative-surveillance mechanic with **zero relation** to "Stamina resource tracking in extended combat." No expansion of what this second "CE" stands for is given anywhere in the corpus (checked `references/mechanical_terms_index.md`, `canon/patch_register_index.md:24` ["CE track — accumulation procedure," 2026-03-27, archived, no expansion], and the archived patch registers — none define it). `references/silo_cohesion_analysis.md:164` explicitly checked off "CE | Combat Endurance | §5 | ✓" as consistent — that audit validated only the *abbreviation*, and missed that the *full phrase* "Combat Endurance" had independently drifted to mean an unrelated mechanic in the arcs design layer. This is a genuine "two distinct mechanics sharing one name" case the batch instructions ask to surface loudly.

- **INT**: bare all-caps "INT" essentially doesn't occur outside a doc-section version tag (`designs/provincial/strategic_layer_v30.md:20`: "ST-BG/INT" — a citation tag, not the stat) and the glossary itself. Live Intel usage correctly uses mixed-case "Int" (matching Part Four's column header convention, `glossary.md:108,112`). **No divergence.**

**Classification table.**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `references/glossary.md:53,120,108,255-262` (CERT/CE/INT home entries) | CANONICAL DEFINITION | — | — |
| `references/alias_registry.yaml:561-579` (TLK/DD/FSTAT) | CANONICAL DEFINITION (declared authority) | — | — |
| `references/deprecated_terms_registry.yaml`, `mechanical_terms_index.md`, `censured_vocabulary.yaml` (TLK/DD/FSTAT tracking) | PULLED / REFERENCED | Registry entries citing the same status | Yes |
| `tests/sim/sim_ttrpg_batch_*.md`, `archives/session/*` (TLK/DD/FSTAT residuals) | HARDCODED DUPLICATE (historical output, excluded from currency claim) | Old 2026-04 simulation/session logs pre-dating deprecation | Consistent with "historical only" framing |
| `designs/arcs/arcs_31_35.md:119-340`, `arcs_24_27.md:25-33`, `narrative_scenario_chains.md:745`, `gm_ref/arcs_01_04.md:102`, `arcs_28_30.md:147` | UNCLEAR / NO CANONICAL SOURCE (**undocumented second sense of "CE"/"Combat Endurance"**) | Live, repeated use of the full phrase for an Inquisitor-suspicion mechanic; no defining doc found anywhere in the corpus | N/A — not "agreement," a wholly separate uncatalogued mechanic reusing the name |
| `references/silo_cohesion_analysis.md:164` | PULLED / REFERENCED, **incomplete audit** | Marks "CE" abbreviation-consistent (✓) without checking the full-phrase drift above | Passed the abbreviation check, missed the term-identity collision |
| `designs/provincial/strategic_layer_v30.md:20` (INT) | Not a term occurrence (excluded) | "ST-BG/INT" is a doc-section version tag, not the Intel stat | N/A |

---

### Note on incidental-English filtering (applies across all 12 terms)
I excluded from all counts above: "CI" hits that are section-heading citations to the doc `ci_political_v30.md` by filename only (not a bare abbreviation use); "CE"/"INT"/"CT" hits inside patch/PP/ED identifiers, file paths, or Mermaid `flowchart TD` directives; and generic-English "face," "order," "focus," "composure" (lowercase, non-game-term prose) wherever they appeared in narrative flavor text rather than as a stat name. Every table row above reflects a genuine game-mechanical usage, not an incidental-English or citation-only hit.
