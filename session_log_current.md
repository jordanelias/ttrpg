session_id: 2026-04-19-sim-batches-ignition-architecture
session_close: 2026-04-19
phase: 0
status: complete
last_stage: Pass 1 cleanup complete — supersession banners + coverage index. Conflict architecture proposal committed.
next_action:
  skill: Pass 2 Session A — structural foundation specs
  description: >
    Write three-scale resolution model (settlement→province→peninsula) into phases.md or
    settlement_layer_v30. Write bishop appointment action into faction_actions.md + propagate
    to settlement_layer §3.2, ci_seizure.md, npc_behavior §8.2 Church tree. Write PP-666
    spec patches (secession candidate restriction, RM Order=0 threshold). Flag splinter
    Influence split for Jordan design decision.
  blockers:
    - Jordan design decision: splinter Influence split (60/40 or unsplit)
    - Jordan design decision: CI cap vs Piety Yield at T9 (reduce SW or raise cap)
    - Jordan design decision: T2 garrison in Crown priority tree (explicit or accept exposure)
    - Jordan design decision: Almud's father assassination — strike backstory or make live
commits:
  - 6ea1f3e: B1 arc test — PP-666 provisional mechanics, 4 scenarios
  - acfe32d: B2 arc test — 5 design variants, 3 sim bugs fixed
  - 8088bc3: B3 arc test — CI/seizure, RS decay, Fort, IP/Vanguard, suppression race
  - d195dbc: B4 arc test — PI track, RDT/TD, Accord revolt, Löwenritter Coup
  - c5be6fc: early-game ignition analysis (historical precedents, Tensions Deck v1)
  - db953eb: session audit — 7 issues, 20 gaps consolidated
  - 2494e7a: conflict architecture proposal — unified design (3-scale model, bishop appointment,
              graduated autonomy, Niflhel dissolved, Tensions Deck rescoped)
  - ab0365d: Tensions Deck pair validation — 15/15 pass (revised to 6 external bilateral cards)
  - de8769d: Pass 1 cleanup — supersession banners on B1/B3/ignition + sim coverage index
session_highlights:
  - 4 sim batches tested 18 mechanical systems across 20+ scenarios. 20 gap flags surfaced.
    3 spec patches ready. 4 design decisions flagged for Jordan.
  - Core finding: the game already starts on fire — 5 provinces have non-aligned settlements
    at game start. Settlement governance friction IS the ignition system. No new mechanic needed
    for early-game conflict; only recognition that fragmentation checks fire from S1.
  - Three-scale model: Peninsula (victory) → Province (contest) → Settlement (engine). Control
    flows up, pressure flows down. Settlement resolves first each season.
  - Church expansion: bishop appointment action (Ob 1 where Church building ≥ tier 2) gives
    Church a settlement-level territorial path independent of CI timer. Mass Seizure becomes
    formalization of settlement-level reality, not the primary expansion mechanic. Geneva trap:
    factions accept Church infrastructure for Stability bonus → Church claims governance later.
  - Graduated Löwenritter autonomy (4-stage) replaces binary coup. Autonomous stage (de facto
    independent, de jure loyal) is the richest game state.
  - Niflhel struck as faction. Functions distributed to settlement phenomena: black markets
    (Order ≤ 1), intelligence brokers (settlement NPCs), Thread exploitation sites (locations).
  - Tensions Deck: 6 external bilateral cards, draw 2 at game start. Each card is a fuse
    (S0 seed → S8+ fire). Factions: each appears in exactly 3 cards. 15/15 pairs validated
    against belligerent-target-opportunity criteria. Internal tensions (Löwenritter autonomy,
    Guild instability, RM emergence) are emergent downstream of external pressures, not forced.
  - Royal assassination: fuse model (S8+ fire, succeed-on-fire). 3 targets produce 3 different
    mid-games: Lenneth dead → Almud revenge; Torben dead → Elske retrieval/Altonian provocation;
    Almud dead → Lenneth inverts Crown identity (pro-Thread, pro-Einhir).
  - Pass 1 cleanup complete: supersession banners on 3 docs, sim coverage index created with
    reading order + supersession map + consolidated gap list + campaign arc timeline.
open_items:
  - Pass 2 Session A: three-scale model spec, bishop appointment, PP-666 patches
  - Pass 2 Session B: graduated Löwenritter autonomy, Niflhel dissolution
  - Pass 2 Session C: Tensions Deck spec, Royal assassination fuse detail
  - 4 Jordan design decisions pending (splinter Influence, CI cap, T2 garrison, father backstory)
  - 7 unspecified systems (AER, Warden behavior, campaign battle scale, Coup advancement,
    Coup→Mandate, Seizure failure chain, treaty→Strain)
  - 6 data gaps (adjacency map, fractional stake disposition, contender pools, RM disposition,
    consolidation Influence, PI upper-bound)
