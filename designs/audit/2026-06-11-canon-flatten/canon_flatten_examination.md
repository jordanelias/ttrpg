# Valoria — Flattened Canon Examination
**Date:** 2026-06-11 · **Task:** pull all canon (metaphysics/ontology, setting/world, characters, events), trace every canon↔mechanics interaction, flatten, and identify all uses, conflicts, and interactions.
**Status:** working audit document — NOT committed to the repo. If you want it in-repo, the convention would be `designs/audit/2026-06-11-canon-flatten/`.

---

## §0 Method and Coverage

Reads were full-text unless marked otherwise. The flatten below is built from the files read this session; every conflict cites its sources. Depth legend: **F** = full read · **S** = targeted sections · **I** = index/headings only · **—** = not read (reason given).

| Domain | Files | Depth |
|---|---|---|
| Canon core | 00_philosophical_foundations(+_rules), 01/02 amendments, 02_canon_constraints, 03_canonical_timeline | F |
| World | worldbuilding_v30(+infill), geography_v30(+infill), calamity_radiation_v30(+infill), southernmost_v30(+infill), solmund_v30/_philosophy/_artifacts, solmund_master (index + Parts 7–8 + appendices: S), solmund_voice_v30 (F; Part Three frameworks + Part Seven bodies absent from file), narrative_voice_canon, worldbuilding_canon_audit(+infill), ms_trajectory_v1, insurgency_pipeline_v30 | F/S |
| Characters | character_canon_v30, baralta_v30, edeyja_npc, character_histories(+infill), npc_character_analyses(+infill), npc_roster(+infill), npc_foils(+infill), companion_specification, threadwork_philosophical_reference(+infill), npc_relational_graph (S: §0–3, §6.1, §12–13) | F/S |
| Events / arcs | arcs_28_30 (F), throughline_resolutions_v30 (F), arc_expansion_v30 (F), emergent_campaign_arcs (F), narrative_scenario_chains (F), emergent_arcs_experimental / emergent_scenarios / arcs_16_19 / 20_23 / 24_27 / 31_35 / gm_ref batch files (I — CP14-superseded per directory README; headings catalogued) | F/I |
| Instruments | canon/mechanics_index.yaml (F), designs/architecture/canonical_registry.md (F), conflict_architecture_proposal (S: autonomy, Niflhel), params/bg/clocks.md (F), conviction_track_v30 (S: header, §1–§5 via pattern extraction, supersession markers), victory_v30 (S: header, §0), threadwork_v30 (S: Part Five), miraculous_event_v30 (S: §19–22), settlement_layer_v30 (S: §4.7–4.9) | F/S |
| Not read | references/valoria_index.sql (concept→file map; trace backbone already supplied by mechanics_index + canonical_registry), designs/factions/faction_systems_overview_v30.md (faction stat canon absorbed via registry/timeline/conviction_track/victory), gm_ref CP14 arc bodies (superseded), solmund_master Parts 1–6 bodies (covered by the v30 splits read in full) | — |

`[READ:]` entries for every file above were emitted in-session at fetch time. `[GAP: faction_systems_overview_v30 — skipped; faction stat layer reconstructed from four other canonical sources; residual risk: overview-only glosses missed]`.

---

## §1 Metaphysics / Ontology — Flattened

### 1.1 Foundational structure (canon/00 + amendments)
- **Threads** are the constitutive ground of the rendered world and the condition of its possibility — not objects *in* the world. Three co-moving axes: **actuality, intelligibility, temporality**. Any operation on one moves the others — **Inseparability (A2 / P-01)**.
- **Ein Sof**: infinite positive being beneath the waterline of intelligibility; epistemically inaccessible in principle (A4/A5). The Church's theology is an interpretive community's response to what could not be rendered (P-08: the epistemological barrier makes religious poetry the *correct* register for the inexpressible, and doctrine a category error when it claims mechanism).
- **Rendering** is performed by consciousness (P-03). Three layers of being-persistence; layer 2 is reflexive **self-rendering**, whose integrity is **Coherence** (A11/P-10), with two facings and tridimensional drift (P-12, P-15). Coherence is **orthogonal to Thread Sensitivity** (ED-301 propagated to params/core).
- **The Leap** (canon/02 amendment): suspension of the reflexive layer-2 facing to attain Contact; opens a defined **vulnerability window**.
- **Monstrosity** is ontological, not moral — the Lacanian Real erupting where rendering fails (P-02/P-04). Three emergence modes (P-05). **Threadcut beings** lack layer 1 (P-06) — Solmund is canonically a threadcut being of the third mode.
- **The Calamity** is rendered-side over-drawing; the ground has no agency and does not respond (P-07, A14). The Lurianic shattering/tikkun framing is canon **only as Restoration Movement self-understanding** (solmund_voice §4.4 explicitly subordinates it to P-07).
- **The Forgetting** (P-13): weight of below-the-waterline reality erases retention; permanent at Askeheim (B-03); a Maritime Forgetting zone exists; mechanically a Cognition+Recall TN8 check (PP-234) with TS÷20 bonus dice and a TS-29 resistance gate.
- **Memory pulling** is messy and detectable (P-09). **Operation taxonomy**: restorative / manipulative / destructive — **Mending is the zero-cost restorative pole** and is immune to opposition; the Church's conflation of the taxonomy is a named category error (canon/01 Amendment 5 commentary).
- **Knots** are permanent, bidirectional bindings with a knot-profile mechanic (4 consequences, incl. the MS seismograph: MS −1 per knotted territory on a Coherence-band drop; MS −2 on practitioner death). P-14: all emergence modes express inseparability; MS threshold effects are explicitly cumulative per band (threadwork §5.3 cites P-14).
- **Coherence 0 outcomes are TS-banded** (canon/02): 30–49 freefall · 50–69 relational reconstitution · 70–89 structural reconstitution · 90–100 **Resonant** + reality-strain (a localized Einhir parallel). The **Einhir Catastrophe** is canonically a foundational-scale manipulative operation inverted; threadwork §5.3's Critical-band design note replicates it mechanically and names that as intent.
- **GD constraints** (canon/02 §B): **GD-1** sole victory = Peninsular Sovereignty (8 alternates STRUCK); **GD-2** deterministic threat responses precede stochastic action selection; **GD-3** revolt → insurgency → faction-emergence pipeline.

### 1.2 Canonical vocabulary registers (solmund_voice §16, PROVISIONAL)
Orthodox: Weaving, Loom, Pattern, The Wound, The Unravelling, The Rendering. Suppressed: The Ground, Spooling, The Waterline, The Oscillation, The Leap. Forbidden (heresy-investigation risk): *Ein Sof*, *Einhir* as theology, *Ungrund*. Jordan rejected Gabirol and Abulafia as sources (2026-04-25); Zohar/Luria/Celan/Jabès retained. The Teresian TS-as-holiness frame is canonically **part of the prophylaxis** (actively suppressive).

---
## §2 Setting / World — Flattened

### 2.1 Timeline spine (canon/03; AG calendar — in-world name open, E-03)
| When | Event |
|---|---|
| ~−12 AG | **Einhir Catastrophe** — foundational-scale manipulative operation inverted; Locked/Oscillating/Snapped zones form; Askeheim becomes the wound (T15). |
| ~−5 → 0 AG | **Solmund**: ~5 years coalescing, ~7 years ministry; dissolution at 0 AG occurs **off-map** (D-3). Canonically a threadcut being, third emergence mode; his works rendered observer-dependently. |
| 0–200 AG | **Church formation** — catalyst model; the perceptual prophylaxis is *emergent*, not designed. |
| ~50–200 AG | **Altonian colonial period**; Church containment grant (Himmelenger); British-India parallel is the design anchor. |
| ~195–200 AG | **Secession Wars** → independence. |
| ~200–218 AG | **First Almqvist's reign** (deed-monarchy founder). |
| ~218 AG | Hunting accident / accession of Almud. **PP-675 struck this backstory** (replaced by a forward-looking Royal Crisis Tension Card, Session C, fuse at S8+) — but canon/03 still carries it live, incl. open item E-01. See conflict register C2. |
| 245 AG | **Game start.** MS 72 (Strained) · CI 22 · IP 20 (Dormant) · Political Stability 0. Timeline carries explicit correction rows: CI 22 (not 0/15); MS 72 via TT→MS inversion 2026-04-20. |

### 2.2 Geography and the wound
- **17 territories**; canonical numbering per geography_design.md: T1 Valorsplatz (Crown seat), T8 Gransol (Hafenmark/Baralta), T9 Himmelenger (Church sovereign city-state, Spiritual Weight 5), T10 Spartfell (NE Altonian pass; Vanguard entry, route T10→T3→T2→T1, PROVISIONAL ED-340), T13 (southern corridor), T14 Ehrenfeld (Löwenritter fortress-city, the graduated-autonomy friction point at S014 Barracks), T15 Askeheim (uncontrolled, Proximity 0, PT permanently 0 per PP-407, Forgetting permanent per B-03), T16 Schoenland (off-board trade actor), T17 Halvarshelm. **Playable set = 15: T1–T14 + T17** (victory_v30 §0).
- **Calamity radiation is dynamic**: fixed node-distance Proximity Ratings (0–5) from T15 × current MS band → per-territory effects (clocks.md lookup; canonical source calamity_radiation_v30). The radiation zone expanding as MS falls *is* the visual of the Catastrophe spreading (canonical_registry). [THREAD]-tagged actions per PP-531; radiation failures queue no Domain Echo (PP-532). Southernmost Surge one-time at MS ≤ 10.
- **Southernmost engagement**: Forgetting Check Cognition+Recall TN8 (PP-234, TS÷20 bonus dice; Overwhelming/Success/Partial/Failure retention ladder); 3-season expedition procedure (approach → three-zone exploration Border-Snapped / Inner-Oscillating / Core-Locked → discovery; TS 50+ auto-Diagnosis); the repair ritual is **[NAME-PENDING: ED-048]** — CP14 docs call it the "Ceiral Ritual" (requirements there: Ceiral Text + Awareness 5+ + TS 60+ lead + 2× TS 20+; outcomes ±: permanent stabilisation → tear + Mode-3 entity). southernmost_v30 remains **entirely in TT scale** (TT≥40 prereq, TT 50 crisis, −10/−6/−3/+8 results, −5/season cap per SIM-STH-E1/PP-635) — see C3.
- **Seam Texts**: Remnant POIs, P-08 comprehension gate, implemented as an annotation layer in Godot.

### 2.3 The world track (one track, four names — see C3)
threadwork_v30 Part Five (heading "RENDERING STABILITY", body "Mending Stability"): range 100→0; degradation table (ops −1/−2; FR Lock −1..−3 + drift; FR Dissolution −3..−8; Past-Pulling −3 min; Gap persisting −4/season; siege −1; winter −1) and restoration (Mending +1/+2 stacking; Community Organizing +1/+2; expedition Mending +2 permanent). Bands: 100–80 Stable · 79–60 Strained · 59–40 Fragile · 39–20 Fractured · 19–1 Critical · 0 **Rupture** ("the world does not end; it becomes unintelligible" — Ein Sof excess, P-aligned). Effects cumulate down-band per P-14. Seasonal cap ±10. **Critical is a designed 2–4-season endgame replicating the Einhir Catastrophe**; Rupture is a legitimate campaign ending. MS trajectory anchors: 5 → 30 (Solmund) → 72 at 245 AG; hysteresis +8, warning window 12 (ED-882 ratified); colonial-revolt / Himmelenger-R-7 / D-4 anchors provisional.

### 2.4 The other clocks
- **CI (Church Influence; old name clobbered — see C4)**: 0–100, start 22 (canon/03; registry says 28 — C5). Generation per tc_political_redesign: conditional passive +1 (Church holds T9 AND Stability ≥3), Piety Yield weighted by Spiritual Weight, Assert +1, Suppress negates; cap ±5/season. Three incompatible threshold schemes on record — clocks.md (30/50/70–74), registry milestones (40/55/65/80/100), CI-75 phase transition (ED-110/PP-413, inside GD-1-struck victory sections) — C12. Baralta's CI suppression requires Mandate ≥4.
- **IP**: 0–100, start 20; tutoring demand fires at 30; preparation 60; Vanguard 75. Expansion of the abbreviation is unstable — Institutional / Imperial / Invasion Pressure across canonical docs (C13).
- **Political Stability / Turmoil / Strain** (one 0–10 track, three names — C14g): +1 battle-season (ED-743 later removed direct battle advancement — clocks.md stale), +2 faction elimination, +1 revolt; bands Peace/Tension/Fracture/Crisis/Collapse; gates universal victory at ≤6.
- **Struck clocks**: Parliament Integrity (PI), Public Instability (registry) — but PI is still load-bearing in chains, conflict_architecture (Split: PI −3) and miraculous_event (RDT prerequisite PI ≥4) — C5.
- **Per-territory**: Accord (0–3 per victory/peninsular_strain; 0–4 per registry — C5), PT/Conviction/Piety (0–5 per PP-406; 0–4 per registry — C5; poles 0=Restoration / 5=Solmund; ±1/season cap; Calamity Drift PP-409 at MS ≤50/35/20; Thread-op drift ED-676; Consecrated status PP-410; Seizure Ob = 2 + Fort + max(0, 3−PT) per PP-411), Prosperity, Fort Level, Spiritual Weight (fixed; J-9 open), Church Attention Pool (0–10, Inquisitor thresholds 3/6, Year-End reset), Territory Value (ex-TCV; 0–5 vs "1–5" — C5).

### 2.5 Solmund-facing world systems
- **Miraculous Event** (ex-RWCE; dual-status header — C14a): Mending at Ob ≥6 within Proximity ≤2 of T15 → event; radius scales with Ob (6 local / 7 +Prox 1 / 8+ +Prox 2); each faction with presence: **SA +1** (one-time); local Proximity-rating −1 for RS-band lookup until Accounting; +1 Accord in radius. Grants awareness, not knowledge — physically identical in kind to Solmund's witnessed works. Faction pathways: Church Miracle Investigation (assert-vs-accommodate aporia: CI +1/RM −1 vs CI −1/SA +1), Baralta sovereign-communion reading, RM tikkun reading.
- **SA (Southernmost Awareness)**: faction stat, gates table SA1–5; starts Crown 0 / Church 0 / Hafenmark 1.
- **Insurgency pipeline** (GD-3): Latent-RM trigger **WA ≤ −2 AND ≥3 territories PT ≤ 1 AND MS ≤ 50** (conviction_track §5/PP-416 — the canonical statement; throughline §3.4 mis-cites "CV ≤ 1" — C14h); 4-stage pipeline, ED-881 four-path dissolution (RAND-validated), 7 INSURGENCY-* forward flags; promoted-RM with PT<3 emergence is extra-parliamentary and cannot cast Parliamentary votes (mechanics_index GD-3 note).
- **Niflhel is struck** (Session B / CR-STRIKE-2026-04-19): functions distributed to settlement layer — Black Markets (Order ≤1 or no governor; Wealth +0.5 / Accord −0.5), independent Intelligence Brokers (Ems-Dispatch fabrication pattern; Dalla Virke canonical broker), Thread Exploitation Sites (Proximity ≤2; harvest = RS −0.5/season, Wealth +1). Propagation gaps catalogued at C8.

### 2.6 Caste
Northern / Central / Southern Einhir; southern exclusion with geographic stigma gradient. Canonical **Viability Matrix** (throughline §1.3) binds caste × faction × branch at character creation: Southern Einhir structurally **closed** from Crown-Administrative and Church-Fortitude/Justice; **favored** in Wardens, Riskbreakers, Varfell-Cultural (and the matrix still carries a Niflhel row — C8). Informed-consent display text is canonical verbatim (§1.5).

---

## §3 Characters — Flattened

### 3.1 Framework (canonical)
13-Conviction taxonomy (PP-684; migration roster PP-685 primary on conflicts per D1; axis matrix; effective_convictions PP-686 §3.7) · Self-Other scalar · 4 **Resonant Styles** — Evidence / Consequence / Authority / Solidarity — with the **TS Gate** (Thread evidence is invalid against TS 0 interlocutors). *Registry renamed Resonant Style → "Pressure Point" (2026-04-15); nothing else adopted it — C5.* · Belief / **Conviction Scar** / Crisis (ED-663/664; **Mending never Scars**; Faith-primary characters Scar from any op except Mending; registry's "Conviction Wound" rename likewise unadopted) · Four orthogonal axes: **TS** 0–100 (Forgetting-resistance gate 29), **Coherence** 0–10 (ED-665 NPC decision rules; MS ≤20 Warden override; Coherence-0 → NPC transition PP-261), **Spirit** 1–7 (Beckett↔Lispector pole; default 4 [ASSUMPTION] D5), **Certainty** 0–5 (PP-551 redesign) · Arc state machine (npc_behavior §5) + transformation knot strain (AUD-NPC-02, P-12) · Roster capacity ~35 Active / 30 Passive / unlimited Background (npc_behavior §11 via PP-661); inner-circle NPCs structurally Active · Disposition −4..floor(Bonds/2)+1, Ob = max(1, base − Disposition) (PP-632) · Knots: pool (Bonds×2)+3, max floor(Bonds/2)+1, tiers 5/2/1, rupture at Disp −4, loss = Coherence −1 (unified knots_v30, Pass 2g).

### 3.2 Canonical figures (anchors + earned-state notes)
- **Almud Almqvist** (Crown): **TS 28** (verified this session in character_canon — my earlier working note "TS 0" was a compaction error, corrected), Certainty band pragmatist-with-doubt; Manuel I Komnenos anchor; Virtue framework −1 Ob on public honourable action; Belief 2 = the sovereign constraint (Einhir sympathy locked by CI+3 / Mandate−2 / IP costs; erosion paths canonical in chains Arc 2); Longevity 3.
- **Lenneth** (Queen): sea-republic origin; revivalist; Catherine the Great anchor; **TS ceiling 10–20, SA-gated** (D-6/ED-727); holds the pre-Altonian coastal-survey archive with a first-person thread-perception account — the account's date is internally inconsistent across docs (C11b); hidden funding network ("Revolution" naming stale — ED-061 Restoration).
- **Torben** (heir): Loyalty clock (start 3 per registry vs 8 per chains — C14j); tutoring demand at IP 30; TS 8 near-Inert, three unexplained experiences; Conviction-emergence window mechanic (ED-609) — first faction to Disposition ≥+2 in the window sets his primary Conviction.
- **Elske**: in Altonia, married to Doux Laskaris' border duke; Family-vs-Self-Determination unresolved; Evidence RS; Loyalty 0–7 start 4; stance triangle still open (J-4); TS not established.
- **Himlensendt** (Confessor): sincere keystone; Evidence RS; destabilisation trigger = the Church's relics include **originary Locks** (three Cardinals requested reassignment after handling them); consecration-crisis foil ED-407.
- **Cardinals** (named canonical per ED-758): **Jarnstal** (Fortitude, Templar; Certainty 4), **Olafsson** (Justice, Inquisitor-General; Certainty 5, highest in game; Niflhel-tool institutional history with operative Solvind Brak), **Aldric Tormann** (Prudence; Deviation Ob 1; embezzlement arc), **Klapp** (Temperance; 11-year TS-prevalence dataset; contradictory state across docs — C10).
- **Baralta** (Hafenmark): Henry VIII/Isabella anchor; direct-communion theology (PR-11/ED-732); **pure adversary to RM**; prophylaxis-cracker throughline T-D; Crown Claim doc + Generational interaction table (throughline §4.2.3); successor undesigned (ED-610).
- **Duke Magnus Vaynard** (Varfell): **canonical identity = Reinhardt-von-Lohengramm-coded military conqueror** (victory_v30 banner 2026-04-19; CR-STRIKE; varfell_mandate_action contamination note): "Varfell expands through military conquest, period"; Thread/RM is political constituency and genuine ethical cause, **not** a force multiplier. Environmental TS (ED-775/PP-699 Magnus canonical; ED-787 opportunist). The scholar-collector TK/VTM arc layer survives un-struck in CANONICAL arc docs — C7. Longevity 2 (expected death S12–20); successor **Maret Uln** (TS ~50, CONFLICTED, PP-486).
- **Lisbeth Ehrenwall** (Löwenritter): TS 0 (ED-392), Certainty 5 (ED-393); deed-logic; six-criteria private journal (discoverable T14 Evidence 5); **graduated autonomy** Loyal→Restless→Autonomous→Split replaces her Coup Counter (conflict_architecture; clock-registry path cited for it is dangling — C9); post-coup calculus foil ED-406; succession candidates Torsvald / Templar Knight / Torben (ED-611).
- **Torsvald** (Riskbreaker): TS 35 (roster, canonical) vs 20+ (arc_expansion — superseded value, C7c); Autonomy/Continuity; Deviation Ob 1.
- **Edeyja** (Warden-Chief): TS 75–80, Coherence 9 anchor; WR ladder 1–4 (access→trust→collaboration→teaching at +5 TS/season); at CI 100 her successor "cannot be publicly identified" (Warden×CI scale).
- **Warden Orm**: TS 60, Mending pool 19D, +0.55 RS/season baseline output (his death accelerates Rupture ~7 seasons); death-Mending arc seals one Catastrophic Gap permanently (+5). Third warden **intentionally unnamed** (the death preceding contact).
- **Yrsa Vossen** (RM): TS 25 IDEALIST; Equity-primary; **Aldric Hann** (logistics; Autonomy secondary; strain track to schism) — note near-collision with Aldric Tormann (C14k).
- **Haelgrund**: TS 12 PROCEDURALIST, Bellarmine anchor. **Brandt Aetius**, **Feldhaus + Virke** (Thread-touched supply chain link; Virke now the independent broker), **Almstedt**, **Strand** (flattery −1 Ob), **Laskaris** (oikonomia; IP sandbagging + flip), **Solberg** (homesick), **Solvei Kaldring** (Southern Einhir elder; RM-Std 5 endorser).
- **Ruler Diamond** foils canonical (ED-393–401): four axes, six pairings, subjective views, four triangles.
- **Lifepath** canonical (ED-374; Origin/Formation/Vocation/Catalyst + sparking; Mira Sondhal test character TS 61); open items ED-375–391 (incl. ED-377 Intuitive Threadwork vs P-01, ED-388 Smite the Heretic, ED-389 Investigator TS+3, ED-390 war events).
- **Companion spec** canonical (cap 2 active; ED-666 Thread-departure triggers).
- **Relational graph** (PP-724, PROVISIONAL): six edge types (sworn-bond / liege-vassal / kinship / patronage / rivalry / feud) with strain capacities 3/5/7 (patronage 2/4/6), knot-lifecycle mirror, feud auto-transmission along strong kinship, Honor-crisis network cascade, FR-Dissolution "memory-bond" mutation (+1 Coherence damage), NPC-NPC Disposition derived; residence-derivation canon (§6.1: Almud→S-001 Valorsplatz, Baralta→S-018 Gransol, Confessor→S-036 Himmelenger, Vaynard→S-031 Sigurdshelm, Löwenritter→S-014 Ehrenfeld, RM→S-026 Grauwald Lodge, Wardens→Askeheim Ruins via S-012 Stillhelm); B1.2 defection cascade / B1.3 faction-Cascade / B1.4 distance-strain / B2 edge instantiation deferred; cites a non-existent "М-3/М-9" rule series (C14e).

---

## §4 Events — Flattened

### 4.1 Settled past (canonical, with one strike in flight)
Catastrophe (−12) → Solmund ministry (−5→0, dissolution off-map) → Church catalyst formation (0–200) → Altonian colonial period + Himmelenger grant (50–200) → Secession Wars (195–200) → deed-monarchy founder reign (200–218) → 218 accession of Almud → 245 game start. The 218 hunting-accident/assassination complex was first **resolved as genuinely accidental** (chains full-evidence branch: 27 years of load-bearing political structures built on a false assumption) and then **struck from pre-game canon entirely** (PP-675), replaced by the forward Royal Crisis Tension Card — canon/03 not yet updated (C2).

### 4.2 Forward fuses (live mechanics that generate events)
Royal Crisis card (S8+) · Altonian ladder: tutoring demand (IP 30) → Torben Loyalty clock → preparation (IP 60) → Vanguard (IP 75; ED-340 PROVISIONAL, route T10→T3→T2→T1) · Generational Shift (4 triggers) × graduated autonomy × IP × Baralta Crown Claim (throughline §4 interaction tables + sequencing: Succession → Coup-resolution → IP) · Church schism cascade (Himlensendt Arc C → four Cardinals fracture four ways; successor determined by Cardinal arc states) · Insurgency pipeline (GD-3) · Miraculous Events (SA escalator) · Southernmost cracking clock (3+3 seasons → ritual window) · Longevity table (ED-567 proposal: Vaynard 2, Almud/Ehrenwall/Vossen 3, Himlensendt/Baralta 4) with named succession arcs.

### 4.3 Arc corpus — status map
- **CP14 layer** (designs/arcs/arcs_16_19…31_35, emergent_campaign_arcs, emergent_arcs_experimental, emergent_scenarios, gm_ref batches 01–55): declared "superseded design input — NOT live" by the directory README, **but** the README is itself a misplaced copy titled `designs/gm_ref_cp14/` (a directory that does not exist), gm_ref/README claims the folder is empty (false), and canon/01 Amendment 5 still binds arcs_28_30 — C6/C14b. Partial retrofits exist (PP-675 strike banners in chains; full Niflhel/Coup strike banner in arc_expansion).
- **Canonical layer**: arc_expansion_v30 + throughline_resolutions_v30 (both 2026-04-17), each carrying day-after staleness (Niflhel rows, Coup Counter tables) — C8/C9.
- **arcs_28_30 (Coherence-0 trilogy)**: the "Ontological Correction" (rendering-as-expansion, not loss) is canon-aligned for the **90–100 Resonant** band only; the doc predates the TS-banded outcome taxonomy and supplies neither TS-at-failure nor reality-strain — Amendment 5's explicit requirement is unmet (C6). Cross-arc table and the Almud/Lenneth/Vaynard branch logic remain the richest extant statement of endgame tone.
- **Endgame configuration** (chains): nine simultaneous conditions = STABLE; zero = "the Einhir Catastrophe repeats — not literally; the conditions that produced it are recreated."

---

## §5 Canon → Mechanics Interaction Map

| Canon rule / entity | Mechanical expression (module per mechanics_index) | Notes |
|---|---|---|
| P-01 Inseparability | `co_movement` (Version C, 15 cards); every op draws | Chains/conviction_track route even *recovery* through co-movement |
| P-02/P-04 monstrosity ontological | Monstrous Incursions (radiation + Gap tables) | Mode-3 entity on ritual failure |
| P-03 rendering by consciousness | `rendering_stability` | Rupture text = unintelligibility |
| P-05 three emergence modes | `threadcut_beings` + incursion typing | Solmund = third mode |
| P-06 threadcut (no layer-1) | `threadcut_beings` | Solmund claim arc leverages this |
| P-07 Calamity rendered-side | `rendering_stability` + calamity radiation lookup | Lurianic frame canon-subordinated (RM theology only) |
| P-08 epistemological barrier | Forgetting Check (PP-234) · Seam Texts gate · Inert Knowledge · **TS Gate** (thread evidence invalid vs TS 0) | Voice doc: religious poetry is the *correct* register |
| P-09 memory pulling detectable | `thread_past_pulling` (−3 MS min) | |
| P-10/P-15 Coherence | `coherence_track`; `coherence_zero_transition` (PP-261) | ED-301 orthogonality in params/core |
| P-12 knots/inseparability | `knots` (PP-632) · knot-profile (MS seismograph) · relational-graph §3.3 dyadic mirror | Transformation knot strain AUD-NPC-02 |
| P-13 Forgetting | B-03 permanence at Askeheim · Maritime zone · expedition retention ladder | TS-29 resistance gate |
| P-14 cumulative expression | MS band-effect cumulation (threadwork §5.3 cites it) | |
| GD-1 sole victory | `victory_check_service` + `peninsular_sovereignty`; strikes in conviction_track §4.2/4.3/6/7 and victory_v30 §0.1/3.1–3.6/4/8; `mass_seizure` = territorial conversion, **not** a win trigger | Threshold contradiction → C1 |
| GD-2 deterministic-first | `faction_action_dispatch` + mandatory `govern`/`muster` (Accord triggers) | ≤3 mandatories/faction/season |
| GD-3 insurgency pipeline | `insurgency_pipeline` + `restoration_movement` (PT decay 0.35/arc) + `parliamentary_vote` eligibility gate | Stage-name divergence noted (C14m) |
| Calamity / Askeheim | Proximity 0–5 × MS-band lookup (clocks.md); PP-531 [THREAD] tags; PP-532 no-echo; Vanguard-independent | Registry: radiation expansion is the Catastrophe's visual |
| Solmund's works | `miraculous_event` (Mending Ob≥6, Prox≤2) → SA, Accord, local Prox-mod | Triple interpretation (Church/Baralta/RM) is the design |
| Witness traditions (ED-735) | SA gates + witness-Conviction mechanic | Master-doc Appendix B status stale (C14n) |
| Caste canon | Viability Matrix (creation) · ladder gates · Initiation Duty Ob · lifepath origins | Southern closure rows canonical |
| Coherence-0 taxonomy | PP-261 transition + arcs 28–30 narrative layer | Arcs defective vs Amendment 5 (C6) |
| Leap mechanism (canon/02) | `thread_leap` + Discovery Events + vulnerability window | Spirit TN7 checks throughout arc layer |
| Residence canon | Relational-graph §6 settlement coupling; officer reassignment | Hop-distance strain scaling |
| PT (Conviction/Piety) | Seizure Ob (PP-411) · Calamity Drift (PP-409) · Thread-op drift (ED-676) · **presentation layer §11** (environmental narration per PT shift; Godot art hooks) | World→player bridge |
| CI | Warden×CI pressure scale (throughline §3.2) · milestones · Attention Pool · legitimacy bonus floor(CI/20) | Scheme conflict C12 |
| MS | Seismograph (knot-profile) · Calamity Drift · radiation · Critical-band +1 to coup/succession trigger pools · MS≤20 Warden Coherence override | One-track/four-names C3 |
| Arc conditioner catalogue | RS-band transitions · TC milestones · Strain levels · cross-NPC chains (Confessor↔Cardinals, Crown succession, Warden↔Vaynard) · obligation triggers · longevity | arc_expansion Part IV (CANONICAL) |
| Intent_of_game loop | Articulation layer (PP-688) · Domain Echo (ED-300) · zoom triggers (arc-adjacent additions ED-606/607) | The positive-feedback spec itself |

---
## §6 Conflict Register (severity-ranked, worst first)

Severity: **P1** = canon-level contradiction or unpropagated strike that will corrupt downstream work · **P2** = canonical-doc inconsistency needing an editorial call · **P3** = defect/drift, low blast radius. Each row: finding → sources → remediation pointer. All are Jordan-adjudication unless marked mechanical-tier.

### P1

**C1 — GD-1 victory threshold contradicts its own canonical implementation.** canon/02 §B GD-1 and mechanics_index (`peninsular_sovereignty` note) say "**11+ of 15** territories, Accord ≥2, Political Stability ≤6, 2 seasons." victory_v30 §0 (the doc both of them cite) says "**All 15 playable territories (T1–T14, T17)** — directly or via effective hegemony," Accord ≥2 in directly-controlled, Turmoil ≤6, 2 consecutive Accountings. 11+ vs all-15 changes the entire endgame difficulty curve. *Remediation: Jordan picks the number; propagate to canon/02, mechanics_index, victory §0 in one commit.* `[READ: canon/02 (prior session), victory_v30 §0, mechanics_index]`

**C2 — PP-675 backstory strike not propagated to the canonical timeline.** canon/03 still carries three live rows for the ~218 AG hunting accident plus open item "E-01: perpetrator TBD — campaign revelation candidate." PP-675 struck the whole backstory (chains Arc-1 banner: "no longer pre-game canon… all branch logic below is invalidated"), replacing it with the Royal Crisis Tension Card (Session C, S8+). Compounding: E-01 was *also* resolved as "genuinely accidental" (chains Collision-D banner) before the strike — so the repo simultaneously says TBD, accidental, and struck. Intra-doc: the chains Arc-1 **Discovery Chain remains un-struck** ("the investigation proceeds normally") directly under the banner claiming all branches invalidated. *Remediation: strike the three timeline rows + E-01; strike or banner the Discovery Chain; record the accidental-resolution → strike lineage in the ledger.*

**C3 — World-track naming fracture: one track, four names, plus one doc with inverted arithmetic.** The track is single (canonical_registry lists one global clock; threadwork Part Five defines it). Names in live use: **TT** (Thread Tension — southernmost_v30 wholesale; conviction_track §5.3 and insurgency §3.3 Community Weaving "Ob = Thread Tension ÷ 20" inside CANONICAL docs), **RS** (threadwork Part-Five *heading*, conflict_architecture, settlement_layer §4.9 "RS −0.5", arc_expansion "RS Band Transitions", npc docs "RS 60"/"RS ≤ 55", calamity infill headers), **MS = Mending Stability** (threadwork Part-Five *body*, clocks.md, canon/03, conviction_track, mechanics_index `ms_track`), **MS = Metaphysical Stability** (canonical_registry rename 2026-04-15, adopted nowhere). mechanics_index carries **both `rs_track` and `ms_track` as separate mechanics** — a duplicate pair from the unfinished merge. Worst instance: **narrative_scenario_chains** had TT labels text-swapped to MS without inverting arithmetic — "Ceiral success: MS −10" as a *good* outcome, "MS +1/season from cracking" as *bad*, yet "MS above 40" as good in the same doc, plus TS band names (Stirring/Wakening) applied to MS. *Remediation: one canonical name (ED-303 in my prior notes was mis-keyed — ED-303 is the CI-cap item per victory header; the naming ED needs locating or opening), then a verified sweep that inverts arithmetic where the source was TT-semantics; merge the index pair.*

**C4 — Rename-sweep self-clobbering (≥5 sites): the old names were erased from the notes that record the renames.** (a) canonical_registry rename table: "Church Influence → **Church Influence**" (old name — almost certainly "Theocratic Control (TC)", which is what the arc layer still uses — destroyed); (b)+(c) chains and conviction_track glossaries: "CI = Church Influence… **renamed from Church Influence** per ED-782"; (d) ED-644 note: "**PT ≡ PT** terminology equivalence" (originally Conviction ≡ Piety or CT ≡ PT); the same glossary line "Piety Track **(CT)**" mixes both halves; (e) miraculous_event title "**Miraculous Event (Miraculous Event)**" — the atom slug preserves the lost old name: *Rendered World Change Event (RWCE)*. Consequence: the repo no longer records what TC, CT, RWCE were, except by archaeology. *Remediation: restore old names inside the rename notes from git history / atom slugs; add a hook-side regex for "X (X)" and "renamed from X … X" patterns.*

**C5 — canonical_registry (Rev 2, 2026-04-15) conflicts with newer canon on at least seven values and none of its renames propagated.** (i) CI start **28** vs canon/03 **22** (timeline has an explicit correction row rejecting other values); (ii) Piety **0–4** + Seizure Ob **6−Piety** vs conviction_track PP-406/411 **PT 0–5** + Ob **2+Fort+max(0,3−PT)** (registry's own J-6/J-7 left open); (iii) Accord **0–4** (Aligned=4) vs victory §0.2 / peninsular_strain **0–3** (Aligned=3); (iv) Territory Value "Simpler. Range **1–5**" vs "Range **0–5** (Askeheim = 0)" in the same subsection; (v) lists **Coup Counter 0–4** as a live track, superseded three days later by graduated autonomy; (vi) renames (Mending→Metaphysical Stability, Resonant Style→Pressure Point, Belief Scar→Conviction Wound, Leadership Deviation→Authority Challenge Ob, Turmoil→Political Stability, Memory→Precedent/Projection→Prospect) adopted by **zero** downstream docs — arc_expansion, dated one day later, uses the old names throughout; (vii) registry **struck PI and RDT**, yet conflict_architecture (CANONICAL, Split row "PI −3"), chains ("PI ≥ 5", "PI −2"), and miraculous_event (2026-04-25: "RDT advancement… PI ≥ 4") use both afterward. The registry is simultaneously self-titled "Definitive" and the single most drifted instrument in the repo. *Remediation: either re-ratify the registry against current canon (one pass, Jordan call per rename) or demote its status header; it is one of the 6 stale canonical sources bootstrap already flags.*

**C6 — canon/01 Amendment 5's requirement on arcs 28–30 is unmet.** The amendment requires the three Coherence-0 arcs to specify (a) TS at failure and (b) reality-strain. arcs_28_30.md: no TS-at-failure anywhere (prerequisites put Vaynard/Almud near TS 30 at *Discovery*, unpinned at failure); no reality-strain; a single uniform outcome (identity intact, rendering expanded, optional chosen transformation) that matches only the **90–100 Resonant** band of the canon/02 taxonomy — a TS-50–69 failure should instead produce *relational reconstitution*. The doc is also header-stamped "Not valid against any post-CP14 ruleset" while canon binds it, and uses struck/stale apparatus (TK 5, Combat Endurance, "Revolution", "Ceiral"). *Remediation: regenerate arcs 28–30 against the TS-banded taxonomy with explicit TS-at-failure + strain per branch; this is the one CP14 file canon explicitly depends on.*

**C7 — Vaynard identity bifurcation across canonical docs.** Canonical (victory_v30 banner 2026-04-19; CR-STRIKE-2026-04-19 in supersession register; varfell_mandate_action contamination note): **military conqueror, Reinhardt-coded; "Varfell expands through military conquest, period"; VTM struck as a placeholder; Cultural Reformation struck; Thread/RM = constituency + ethics, not multiplier; mead-hall/Tribune/Heorot/Althing framing flagged as Claude-overreach contamination.** Still standing un-struck: the scholar-collector layer — arc_expansion (CANONICAL) Arc A/B/C built on TK/VTM advancement, Private-Collection-centric play, "Niflhel-Vaynard Contact clock"; chains Arc 9 (TK 0–5 ladder with CI effects); emergent arcs Arc 2. Sub-findings: (a) TK→VTM rename half-applied (both names in one Arc-A paragraph); (b) Torsvald TS 20+ (arc_expansion) vs **35** (roster, later/canonical); (c) Vaynard "TS 14 dormant hidden" vs ED-775/787 environmental-TS canon — relationship unstated. The pending "editorial rewrite of Varfell victory paths, faction actions, and NPC priority trees" named in the victory banner has not landed. *Remediation: execute that rewrite; banner or strike chains Arc 9 and arc_expansion Vaynard arcs pending it.*

**C8 — Niflhel strike (Session B) propagation gaps, consolidated.** Properly retrofitted: arc_expansion (DEAD/SUPERSEDED banner; operative sections struck), conflict_architecture + settlement_layer §4.7–4.9 (successor systems), chains Collision-D (partial banner). Still live, un-struck: throughline_resolutions §1.3 **Viability Matrix "Niflhel (informal) ★★★" row (CANONICAL doc)**; chains Arc 4 (Olafsson–Niflhel exposure chain, Solvind Brak) and Arc 6 Widowing option; emergent_campaign_arcs Arc 3 (the Niflhel drain is the arc's premise); npc_roster infill #10 (live constellation description); BG card texts ("Niflhel trade +1 Ob"; Feldhaus "syndicate presence"); character_histories Tideward Knot "dockworker arm"; canon/03 faction starting-stat table Niflhel row; axis table; and — generated **after** the strike — solmund_voice §18 Certainty table "Böhme, **Niflhel plain speech**" (2026-04-25). The post-strike regeneration carrying the struck faction shows the atom pipeline reproduced stale master content. *Remediation: single sweep keyed off the supersession register; the broker/black-market re-skins are already specified, so most fixes are mechanical-tier re-labels (loggable, Jordan-vetoable); the canon/03 row and Viability Matrix row are Jordan calls.*

### P2

**C9 — Coup-Counter → graduated-autonomy supersession gaps.** throughline_resolutions §4 (CANONICAL, 2026-04-17) builds its three-clock Generational interaction tables on Counter-fires-at-3, one day before the replacement. arc_expansion's banner gives only a "rough mapping for reader translation." The banner cites **`params/clocks/clock_registry_v30.md` — a path that does not exist** (the clock file is `params/bg/clocks.md`, which contains **no** autonomy spec; the four-stage track lives only in conflict_architecture_proposal). Residual numeric incoherence in the struck model itself: fires at 3 (chains/throughline/emergent arcs) vs range 0–4 (registry) vs "Counter ≥ 4 → instant" (conflict_architecture's restatement); chains "COUNTER NEVER DECREMENTS" vs arc_expansion obligation row "Coup Counter −1." *Remediation: migrate throughline §4 tables onto Loyal/Restless/Autonomous/Split triggers; fix the dangling path; decide where the autonomy spec canonically lives (params/bg/clocks.md is the natural home).*

**C10 — Cardinal Klapp is two incompatible characters, and three Cardinals carry residual pre-ED-758 names.** arc_expansion: Klapp **she**, TS **8** undiscovered, Certainty 3, Temperance scholar with the 11-year dataset. chains: Klapp **he**, TS **31** approaching Stirring, "CE 4" (Combat Endurance as a conversion metric — CP14 stat), archive keys, Trajectory B/C conversion track. Gender, TS, and mechanism all conflict. Same docs retain stale names beside the ED-758 canonical ones: **Voss** (×4) for Olafsson, **Vorn** for Tormann, **Kald** (×3) for Klapp — an incomplete rename sweep inside one CANONICAL file. Prior audit's Temperance-vs-Scholarship title wobble persists. *Remediation: pick Klapp's canonical state (the arc_expansion version is the later-approved one); name-sweep Voss/Vorn/Kald; log ED.*

**C11 — Timeline arithmetic errors inside canonical arc content.** (a) Olafsson Belief 3: Einhir texts "condemned in the **4th Century**" — 300s AG is the *future* (game start 245); (b) Olafsson Arc C: "a **400-year-old** canonical text" → −155 AG, pre-Catastrophe, impossible for a Church (0–200 AG) document; (c) Lenneth's archive account dated three ways: **~180 AG** (chains Arc 3), **180 years old** (arcs_28_30, ≈65 AG), **245 years old** (arcs_28_30 same arc, ≈0 AG); (d) southernmost_v30 §6.2 still says "game start, **45 AG**" — pre-dating the 200-year timeline shift (canonical start 245 AG). *Remediation: fix (a)/(b)/(d) to in-range dates (mechanical-tier, loggable); (c) is a Jordan call — the account's date is load-bearing for what its author could have witnessed.*

**C12 — Three incompatible CI-threshold schemes.** clocks.md effect bands 30 / 50 / **70–74 ("Seizure protocol pending")** and nothing above 74 · canonical_registry milestones **40/55/65/80/100** with named effects + legitimacy formula · CI-**75** phase transition (ED-110/PP-413) inside GD-1-struck victory sections, with mass_seizure's `P(declare) = ((CI−60)/40)^3.3` (supersession 250715f) as the live declaration rule. The arc layer keys NPC conditioners to the 40/55/65/80 set ("TC milestones"). mechanics_index already flags mass_seizure's three sources as "potentially drifted; Pass 2f reconciliation pending." *Remediation: Pass 2f should also pick the one threshold scheme; clocks.md needs its >74 bands authored.*

**C13 — "IP" expands three ways in canonical docs.** Institutional Pressure (throughline_resolutions, npc layer) · Imperial Pressure (mechanics_index `ip_track`: "Altonian Imperial Pressure") · Invasion Pressure (canonical_registry). One clock, three official names. *Remediation: one-line Jordan pick + sweep.*

### P3 (defects and drift, grouped)

**C14a — Status-integrity defects.** miraculous_event header: "## Status: CANONICAL" immediately above "**Status:** PROVISIONAL — pending Jordan editorial review" — both, in one block. conviction_track status line has two dates concatenated mid-token ("…(2026-05-17 — peninsula-only victory)2026-04-17 (ED-643)"). arc_expansion's strike banner closes with `-->` but no `<!--` opens it (orphaned comment terminator; the banner renders as body text).
**C14b — designs/arcs README misplacement.** The README is titled `designs/gm_ref_cp14/` and describes that directory's structure; `designs/gm_ref_cp14/` does not exist; gm_ref/README says "currently empty" above 17 files; arcs_31_35 points readers at the nonexistent path. The CP14-supersession claim also collides with Amendment 5's dependence on arcs_28_30 (C6).
**C14c — clocks.md content duplicated verbatim** (MS/CI/IP sections + battle consequences + Vanguard block appear twice in full), and its battle-consequences paragraph mixes **Turmoil +1** and **Strain +2** as if distinct, while ED-743 (battles no longer advance the track directly) postdates it.
**C14d — solmund_voice split-integrity loss.** "PART THREE: PHILOSOPHICAL FRAMEWORKS — Five frameworks…" is followed by zero frameworks (the bodies didn't survive the Stage-4 split), and "PART SEVEN: SOUTHERNMOST ENGAGEMENT DESIGN" is an empty terminal heading.
**C14e — Dangling rule citations in PP-724.** npc_relational_graph grounds edges in "М-3 (substrate grounds all)" and "М-9 (clinical-trauma vocabulary)" — no M-series exists in canon/00 (both files), canon/01, or canon/02 amendments (grepped this session). `[CONFIDENCE: medium — an M-series could live in an unread file, but the canonical rule namespace is A/P/GD]`.
**C14f — "Ceiral" vs ED-048.** The ritual name is canonically [NAME-PENDING: ED-048]; CP14 arcs and chains use "Ceiral Ritual"/"Ceiral Text" as settled.
**C14g — Turmoil / Strain / Political Stability tri-naming** for the 0–10 track (registry renamed; victory §0 "Turmoil"; arc_expansion "Strain"; clocks.md both in one paragraph).
**C14h — throughline §3.4 mis-cites the RM trigger as "CV ≤ 1"**; the canonical stat (conviction_track §5/PP-416) is PT ≤ 1. No "CV" stat exists.
**C14i — Insurgency stage-name divergence**: insurgency_pipeline_v30 four-stage (Latent…) vs mechanics_index note "disorganized → emergent → extra-parliamentary | parliamentary."
**C14j — Torben Loyalty start**: 8 (chains clock) vs 3 on a 0–7 scale (registry).
**C14k — Name near-collision**: Aldric **Hann** (RM) vs Aldric **Tormann** (Prudence Cardinal) — two load-bearing Aldrics introduced in the same doc.
**C14l — Strike-date wobble**: banners say Session B 2026-04-18; the register ID is CR-STRIKE-2026-04-**19** (likely session vs commit; record once).
**C14m — Settlement-ID format drift**: S-014 (relational graph) vs S014 (conflict_architecture).
**C14n — solmund_master Appendix B lists the two-witness-traditions question as open** while worldbuilding_v30 §3.7 already integrated it as canonical (ED-735).
**C14o — Prior-audit residue still standing** (worldbuilding_canon_audit): stage13 "Reach" = stale Influence; Baralta CI-suppression Mandate 4+ vs >5; Klapp Temperance/Scholarship; "Piety" undefined in stage13; Almaic Kyriakos new-content flag (ED-NEW-07); territory-numbering lore table (§9.1, old PP-199/stage7 numbers, ED-NEW-09); Klapp trigger "T3" stage7-vs-PP-199.
**C14p — solmund_voice path-drift class**: references to `designs/setting/calamity_radiation.md` and `solmund_cultural_guide_consolidated.md`; edeyja_npc stale "TK 5"; conviction_track_v1 cited by relational graph §3.9 (vs _v30).
**C14q — Further rename residue**: chains Arc 3 contains three "**Solmund/Solmund**" doubled-name artifacts (a collapsed old-name/new-name pair, same family as C4); the dissolved faction's old name "Revolution"/"People's Revolution" persists in southernmost §6.2, chains, and arcs 28–30 against the ED-061 **Restoration** naming.

---
## §7 Provisional / Open Inventory

### 7.1 PROVISIONAL documents (pending Jordan ratification)
solmund_master_document + all Stage-4 splits (solmund_v30 / _philosophy / _artifacts / **_voice**) · **miraculous_event_v30** (dual-status, C14a) · character_canon_v30 · baralta_v30 · narrative_voice_canon_v30 (also index-drift: registered to no concept) · **npc_relational_graph (PP-724)** and its whole B-track · Vanguard mechanics (ED-340/PP-568) · MS-trajectory provisional anchors (colonial revolts, Himmelenger R-7, D-4 conquest dating).

### 7.2 Open editorial / design items surfaced by this flatten
| Item | What's open |
|---|---|
| E-03 | In-world calendar name |
| ED-048 | Ritual name (replaces "Ceiral") |
| ED-302 | PT track name (Conviction vs Devotion/Orthodoxy/Glaube) |
| ED-375–391 | Lifepath batch (incl. ED-377 Intuitive Threadwork vs P-01; ED-388; ED-389 Investigator TS+3; ED-390 war events) |
| ED-567 | Longevity Track ratification (the succession-arc layer depends on it) |
| ED-609–613 | Torben emergence spec · Baralta successor · Ehrenwall succession · Faction Fracture rule · Vaynard recovery gate |
| ED-629 | Thread stress test — 28 P0 blockers; Warden ladder carries a confirmatory-audit dependency |
| ED-647 | Rank dismissal mechanics (partial) |
| J-1–J-9 | Registry open decisions, incl. J-4 stance triangles (Lenneth/Elske/Haelgrund), J-6/J-7 territory-scale confirmation (now a live conflict, C5), J-9 Spiritual Weight values |
| SIM-POL-R01–05 | Deferred; discoverability entry in coverage_matrix |
| ED-538/539 | Compound-effect validations flagged UNVALIDATED in registry |
| Pass 2d–2n | Canon-authoring + contamination audits (Varfell pair, tactic_cards, npc_ai priority stacks, hafenmark_equipment, mass_battle v22 port, mass_seizure tri-source reconciliation) |
| B1.2–B2 | Relational-graph deferred tranche + `canon/relational_edges_v30.yaml` (file not yet created) |
| Marriage mechanic | Kinship formation author-only until marriage_v30 |
| Ministry NPCs | Flagged design debt (arc_expansion Part VII) |
| conviction_track [GAP] rows | RM-emergence frequency stress test · Community-Weaving dual-effect loop check · Consecrated×seizure interaction · Secular-Governance PT floor |
| Tier-3 prose-feedstock deficit | ~14 NPCs × 3 fields (character framework) |

### 7.3 Active strikes whose propagation is incomplete (cross-ref §6)
PP-675 (assassination backstory → C2) · CR-STRIKE-2026-04-19 Niflhel (→ C8) · Coup Counter → graduated autonomy (→ C9) · VTM + Cultural Reformation (→ C7) · GD-1 alternate victories (clean: SUPERSEDED-BY banners present in conviction_track and victory_v30 — see §8 NULL list) · TT→MS inversion 2026-04-20 (→ C3) · registry strikes of PI/RDT/Intel (→ C5; "Intel" actions also persist throughout CP14 arcs).

---

## §8 Honest-Findings Block

**Examined and found sound** (each verdict has the read trail behind it):
- `[NULL: P-rule violations in worldbuilding v3 — examined via worldbuilding_canon_audit(+infill) full read; the prior audit's no-P-violation verdict stands and nothing read this session contradicts a P-rule; the Lurianic frame is correctly subordinated to P-07 in solmund_voice §4.4]`
- `[NULL: GD-1 strike hygiene in the two victory-bearing docs — conviction_track §4.2/4.3/6/7 and victory_v30 §0.1/3.1–3.6/4/8 all carry explicit SUPERSEDED-BY: GD-1 banners with supersession-trail preservation; the strikes themselves are clean (the *threshold* conflict is C1, a different defect)]`
- `[NULL: GD-2/GD-3 enforcement-boundary consistency — canon/02 §B, mechanics_index gd_constraint_coverage, and faction_action_dispatch/insurgency notes agree on the boundary modules; only stage-name drift (C14i) found]`
- `[NULL: Cardinal naming canon — ED-758 names (Jarnstal/Olafsson/Tormann/Klapp) consistent across roster, throughline, arc_expansion headers; residue is the stale-alias layer (C10), not the canon itself]`
- `[NULL: Residence canon §6.1 vs geography/settlements — faction-HQ assignments consistent with territory canon (T1/T8/T9/T14/T15 anchors) and with the registry's Spiritual Weight territories]`
- `[NULL: Coherence-0 ontological direction — arcs_28_30's expansion-not-loss correction matches canon/01-02 for the Resonant band; the defect is band-coverage and missing Am-5 fields (C6), not the ontology]`
- `[NULL: MS band arithmetic in arc_expansion conditioners — 79→59/59→39/39→19 transitions match the canonical band edges despite the RS label]`

**Corrections to my own working state:** `[CORRECTION: compaction note "Almud TS 0" — wrong; character_canon says TS 28 (verified by grep this session); Ehrenwall is the canonical TS-0 figure (ED-392)]` · `[CORRECTION: my prior gloss "ED-303 = MS naming deferred" — victory_v30's dependency line defines ED-303 as the CI-cap-at-100 item; the MS-naming deferral ED was not located this session]`

**Gaps:** `[GAP: references/valoria_index.sql — not read; concept→file mapping would strengthen the interaction map's path coverage but registry + mechanics_index supplied the substance]` · `[GAP: faction_systems_overview_v30 — not read; reason in §0]` · `[GAP: M-series existence — canon/02_canon_constraints not re-grepped this session for "М-"; C14e confidence capped at medium accordingly]` · `[GAP: gm_ref CP14 arc bodies (01–55) — headings only; any canon-bearing detail unique to those bodies is uncovered, accepted because the README declares them non-live]` · `[GAP: threadwork Parts 1–4/6 — not re-read this session; Leap/Coherence/co-movement content taken from canon/01-02 + prior-session reads + mechanics_index]`

**Confidence:** `[CONFIDENCE: high]` on C1–C12 and the flatten sections (§1–§5) — every load-bearing claim traces to a full or sectional read this session or the prior session's full reads. `[CONFIDENCE: medium]` on C14e (M-series) and C4a's reconstruction of "TC" as the clobbered old name (inference from arc-layer usage + emergent_campaign_arcs' interchangeable TC/CI thresholds; git history would settle it).

---

## §9 Suggested Order of Remediation (proposal only — every canon call is yours)

1. **C1** (GD-1 threshold) — one number, three files; everything downstream of victory depends on it.
2. **C2** (PP-675 → canon/03) — the canonical timeline is the most-fetched canon file; carrying a struck backstory there contaminates every session that reads it.
3. **C3 + C4** together — the world-track rename and the clobbered rename-notes are one archaeology task; do the TT-arithmetic inversion check file-by-file (southernmost, chains, conviction §5.3, insurgency §3.3).
4. **C5** — re-ratify or demote canonical_registry; it is the "definitive" instrument and currently the least definitive document in the repo.
5. **C7** — the Varfell rewrite already ordered in the victory banner; until it lands, arc-layer Vaynard content should carry an interim banner.
6. **C8 sweep** — mostly mechanical re-skins with the broker/black-market replacements already specified.
7. **C6** — regenerate arcs 28–30 (the only CP14 file canon binds).
8. Then the P2/P3 queue in register order.

*End of document. Built from session reads 2026-06-11; uncommitted; supersedes nothing.*
