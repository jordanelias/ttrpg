# Digest researchB3

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane scope: research files not read in full by earlier digest lanes (pre_firearms_formations 11-16, proactive_governance_scale_research_v1, and the 2026-08-28 systems-integration-harvest provenance directory). Tier 3 research: shapes and referents, not authority.

### research/pre_firearms_formations/11_throughlines_ners_audit.md
- **What it is:** Audit of the project's 29 throughlines (T-1..T-29) and 8 meta-throughlines (M-1..M-8) against NERS, the six "all directions", and canon P-01..P-15; Mode E of valoria-mechanic-audit adapted to research (no date; chunk 11 of the pre-firearms project).
- **Status:** none stated (no `## Status:` line); closes "Recommended next action: Jordan reviews". Reading: historical research audit; the verdicts (INCLUDE/DEFER/EXCLUDE) were never turned into engine data, so reference only.
- **Bears on:** MB, FA, WR, CORE (doctrine, command timing, morale), PROCESS (NERS method precedent).
- **Content that matters:**
  - Treatment table scores each T/M on N/E/R/S with INCLUDE/DEFER/EXCLUDE/RECONSIDER; "19 of 37" full-fit, 11 partial, 6 DEFER (T-7,T-11,T-16,T-19,T-27,M-3), 1 EXCLUDE (T-20), RECONSIDER T-14, T-21 (:160-215).
  - Top priority named: M-1 doctrine-substrate-opponent triangle ("a game that lets players freely mix doctrines and contexts violates the historical record") and M-4 discipline-timing as "single signature combat-skill mechanic" (:90, :196-199, :350-361).
  - T-3 pike/cavalry/missile RPS is INCLUDE only "conditional, not pure RPS" with terrain/command modifiers (:164, :106); T-26 single-shot heavy-cavalry charge = "spent-resource combat mechanic" (:187, :360).
  - T-28 (grand-formation behaviour emerges from unit mechanics) and T-29 (morale cascade as propagating field) are the bottom-up throughlines; maps to cell-resolved morale (:54-55, :189-190).
  - Four unspecified Thread intersections left as "P2" gaps: Thread-doctrine, rendering x military intelligence, combat-morale x Coherence (P-10), tridimensional propagation of military outcomes (P-12) (:337-340, :380-388).
  - Scale assignment proposal: personal T-9/T-28/T-29/M-4; territory T-1,T-2,T-3,T-5,T-22,T-23,T-24,M-1,M-2,M-7; peninsula T-4,T-5,T-12,T-17,T-18,M-5,M-6 (:365-372).
- **Conflicts / stale:** The "29 throughlines + 8 meta" are defined in files 01-10 (not here); counts "19 of 37" is a doc-derived tally. Uses `canon/editorial_ledger.yaml` (:390) which is not the current ED ledger path [UNVERIFIED]. Frames Thread/Rendering as metaphysical core; no code reads any of this.
- **Open items:** the four P2 Thread-intersection questions; Valoria gunpowder/tech mix for T-14/T-19/T-21; whether Jordan accepts the scale assignments (:376-390). None seem answered in the research tree.

### research/pre_firearms_formations/12_moment_by_moment_dynamic_spacing.md
- **What it is:** Primary-source reconstruction of dynamic spacing and timing in nine battles plus a spacing vocabulary and design notes (research chunk 12, author-lane: pre-firearm formations project, no date).
- **Status:** none stated (header says "observations, not specifications", :902). Reading: historical research, tier 3; figures are derived (self-flagged :936-940), shapes are the durable finding.
- **Bears on:** MB (cell size, approach/contact distances, charge, density), PC (formation spacing), WR (weather/terrain), FI (battle accounts as memory), GO.
- **Content that matters:**
  - Precedent battles treated (each as a phase sequence with distances/durations): Cannae, Pharsalus, Adrianople, Hastings, Crecy, Agincourt, Marignano, Pavia, Panipat (:180-751). Shapes contributed: Cannae = convex centre + refused wings, controlled retreat, cavalry rear-closing; Pharsalus = hidden fourth-line reserve that is the decisive commit; Adrianople = returning detached cavalry + compression; Hastings = slope + feigned-retreat counter-charge cycles; Crecy/Agincourt = missile killing arc + terrain funnel + mud; Marignano = pike column vs gendarme flank, night pause; Pavia = skirmishing shot in broken terrain masking own artillery; Panipat = chained cart line + gaps + elephant panic + wide encirclement.
  - Ancient file spacing: open 4 cubits (~1.8 m), compact 2 cubits (~0.9 m), locked-shields 1 cubit (~0.45 m); rank depth half the file interval; syntagma 16x16=256; Roman 3 ft/man (:105-132). Swiss square ~5,000 on 65x80 files (:157); Praecepta wedge 20->64 wide, 12 deep, ~504 horse (:142).
  - Generic windows: first-contact distance 250-800 m (:771); skirmish zone 50-300 m (:775); killing arc 30-250 m by weapon (:777-784); lethal pocket density ~12-20 m^2 per man (:799); final gallop only 30-50 m (:801-808); decisive commit window 5-30 min (:810-823); battle 2-9 h active, typical 3-6 h (:825-837).
  - Speed table: heavy infantry 3-4 km/h; mud 1-2 km/h; Swiss pike 5-7 km/h; cavalry charge 16-40 km/h over 30-100 m (:858-867). Phase-duration table (:884-898).
  - Design notes O-1..O-7: 250-800 m as natural battle-scale unit; step-change (non-linear) casualty multiplier in lethal pocket; compress battle to 5-10 min of player time with the decisive commit in a 10-60 s window; no sustained full-speed charge; terrain x weather x time-of-day; doctrinal manuals as a game-economy resource; player-authored battle accounts shape later memory (:906-918).
  - Source-handling rule: every minute figure is derived from speed x distance, not source-stated (:936-938); ancient strengths exaggerated (:5).
- **Conflicts / stale:** Not checked against `modules/mass_battle` cell geometry or `geometry.py` constants [UNVERIFIED]; a pairing with the 25x25 grid (brief) is a design question. Mixed units: "pace" varies by region; Part II notes pace conversions are source-variable. Internal slip: Cannae "~5-6 hours decisive combat" vs "2-3 hours first contact to encirclement" (:236, :253).
- **Open items:** O-3 (compress real battle to 5-10 min player time) and O-7 (player-authored battle accounts) are design hooks nothing in this file resolves; file 13 corrects some of its claims (see next entry).

### research/pre_firearms_formations/13_verification_corrections.md
- **What it is:** Self-authored verification of file 12 against modern scholarship (Goldsworthy, Britannica, LacusCurtius, etc.), plus all-directions pass and limitations (research chunk 13; flagged `[SELF-AUTHORED - bias risk]` :5).
- **Status:** none stated. Reading: historical research erratum for file 12; the corrections were never edited back into file 12 (file 12 still carries the wrong figures).
- **Bears on:** MB (reference figures), PROCESS (self-review method).
- **Content that matters:**
  - Two P1 errors in file 12: Panipat sally gaps are ~150 riders wide at ~90-180 m intervals (not 30-50 m) (:133-144); Lodi's elephants ~1,000 per the Baburnama (not 100+) (:146-154).
  - Four P2: Cannae Roman frontage ~1.95 km (360 m citizen cavalry + 1,050 m infantry + 540 m allied cavalry) and centre depth 24-70 ranks, not "1.5 km / 50+" (:18-28); Pharsalus fourth line 6 cohorts ~3,000 (possibly 8, ~4,000) not ~2,400 (:46-54); Agincourt funnel narrows toward the English end, French deploy ~1.2 km wide to ~800 m (:88-99); Marignano is ~12 h of combat across a 24 h window, not "24+ continuous" (:109-117).
  - Manual primitives (Asclepiodotus 4/2/1 cubit orders; Vegetius 1 m x 2.1 m per legionary; Polybius 18.30 six-foot figure called stylised and rejected) are confirmed; synaspismos feasibility is debated (:166-182).
  - Generic windows from file 12 Part IV (approach window, lethal density, gallop window, decisive-commit window) are "robust regardless" and "can be used as design constants"; specific battle reconstructions are "illustrative, not ground truth" (:286).
  - Precedent-case shapes restated per direction: Cannae, Agincourt, Panipat as three distinct doctrine-substrate-opponent triangles (:224-229).
  - Mentions a companion artifact `battle_visualizer.jsx` (Cannae, Agincourt, Panipat, six phases each, correction panels) (:292-304); not part of this assignment [UNVERIFIED that it exists on disk].
- **Conflicts / stale:** Part III item 1 counts "6 European" but lists seven; Hastings and Adrianople were not web-checked (:314). File 12 is not corrected, so anyone citing file 12 numbers inherits the P1/P2 errors.
- **Open items:** edits to file 12 are "recommended in any revision"; none made. Jordan ratification of corrections assumed, not given (:312).

### research/pre_firearms_formations/14_methodology_audit.md
- **What it is:** Self-audit of a proposed "bottom-up design (L0 soldier -> L1 unit -> L2 formation -> L3 army -> L4 battle), top-down verification by reproducing six canonical battles" methodology; adds T-30..T-43, M-9..M-13, G-1..G-13 (research chunk 14; `[SELF-AUTHORED - bias risk]` :7).
- **Status:** none stated; proposals tagged `[PROPOSED]` until Jordan accepts (:262). Reading: historical research proposal; the L0..L4 stack and six-battle suite are not the shape of `modules/mass_battle` as built [UNVERIFIED against code].
- **Bears on:** MB, PC, CORE (verification-as-regression-net), CHAR/FA (AI play silent), PROCESS.
- **Content that matters:**
  - Verification suite of six: Cannae double-envelopment, Pharsalus reserve ambush, Agincourt funnel, Panipat tulughma + firepower, Hastings slope rotation, Marignano interruption (:19, :131-138). Precedent games: none (historical battles only).
  - Anti-pattern T-30/T-40/M-9: no "Cannae button"; a failing verification test traces to a primitive, never a special-case rule (:77, :97, :113). This is the same rule as CLAUDE.md "scripting drift".
  - Primitives proposed: step-change lethal-density non-linearity (T-32), facing as first-class (T-33), cohesion->rout->pursuit kill pipeline (T-34), sub-tile vector positions (T-35), reserves as a held/committed unit state (T-38), terrain-formation lossy interaction (T-37) (:81-97).
  - Calibration proposal: 5-minute turns, ~36-72 turns per battle, 50 m tile; decisive window is 1-6 turns (T-36, T-43) (:89, :103). T-42: a "soldier" may equal 1, 10 or 50 men.
  - Gameplay opportunities G-1..G-13: named plays (Cannae, Pharsalus, Agincourt funnel, Panipat, Marignano, Hastings), counter-plays (G-7..G-9), doctrine selection as strategic commit, doctrinal-manual economy, historical battles as PvE scenarios, replay "battle accounts" (:131-154).
  - NERS findings: R-06 counter-play discoverability (P2), S-03 simultaneous-resolution reveal window (P3), S-04 battle-level only (P2), E-04 sub-tile visualisation (P2), E-05 multi-objective calibration tractability (P2) (:208-218).
  - Self-stated limits: silent on AI play, no mechanism for "calibrated divergence" from history, no effort estimate (:228-240).
- **Conflicts / stale:** Proposes sub-tile vector positions; the brief's mass-battle intent is a cell grid (25x25) with per-cell resolution, so T-35 / N-05 conflicts with the cell-based direction unless cells are the "tile" [UNVERIFIED which the code does]. Says "Six tests: 5 European" but lists Cannae, Pharsalus, Agincourt, Hastings, Marignano (5) + Panipat (:236) -- consistent here, inconsistent with file 13's count.
- **Open items:** command latency as an L2.5 primitive (:31-33); shared-primitive cross-test analysis (:48-50); AI-play problem (:238); file 15 is the resolution pass for these.

