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

