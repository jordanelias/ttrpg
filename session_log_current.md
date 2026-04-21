# SESSION LOG: 2026-04-20 ATOMIZATION RUN
## Status: ACTIVE — atomization workplan 2026-04-20 mostly executed; tier-2 sweep + ED-726 remap pending

last_stage: Atomization workplan 2026-04-20 — Batches 0/1/2/3/4/5§5.1+§5.2+§5.4/6/7/8 complete. D-1..D-7 + PR-1..PR-15 all resolved and committed. Canon is coherent w.r.t. finitude pivot, Leap mechanism taxonomy, MS terminology (core files), MS trajectory, timeline (L16/L21/L32/L129/L179/L181), worldbuilding §3.7 practitioner witness, NPC §6 Baralta theology, throughlines T-26..T-30.

next_action:
  skill: editorial
  description: >
    (1) Tier-2 RS→MS sweep across remaining ~44 active files (provincial, arcs, params/, npcs/, scene/, architecture/, skills/, designs/videogame/). One known straggler: NPC §10 Virke. canon/02 "formerly Rendering Stability per ED-731" is intentional historical annotation — DO NOT sweep.
    (2) ED-726 correction committed this pass — site-network three-layer model (D-5) target is designs/world/ NOT canon/02. Create designs/world/einhir_site_network.md or expand calamity_radiation_v30.md as separate workplan.
    (3) rs_budget.md → ms_budget.md filename rename (content swept; filename pending). Update all cross-refs that name the file explicitly.
    (4) Complete throughlines_complete.md COMPLETENESS CHECK table rows for T-26..T-30.
    (5) Remaining [PROVISIONAL:] markers across repo cleanup — audit to produce list, then per-marker resolution.
    (6) RWCE / Miracle Investigation / SA-gating full integration per ED-735 — separate atomization workplan (touches params/bg/faction_actions, clocks, NPC priority trees, Tension Cards deck).
    (7) D-3, D-4, D-6, D-7 integration (timeline / worldbuilding / NPC updates per ED-724/725/727/728).
  blockers: []

commits_this_sequence:
  - 976e1e8a: '[editorial] Batch 6 §6.1 — Ob 7 AND→OR fix in consolidated Solmund guide L387'
  - e642f195: '[editorial] D-1 cascade — 12y emergence / 7y ministry: timeline L32 + Solmund guide L246'
  - dc6e39ac: '[editorial] Ledger split + register D-1..D-7 + PR-1..PR-15 resolutions (ED-722..ED-737)'
  - 8f8388e9: '[editorial] D-2 + PR-15 — pre-Calamity governance correction (timeline L16 + worldbuilding §7.1) + Seam Text metadata frame'
  - 39069744: '[editorial] Batch 1 — PR-1 Finitude Pivot integrated as foundations §4.3 (Option A)'
  - 46da2d13: '[editorial] Batch 2 — PR-2 Leap Mechanism amendment created + threadwork anchors + foundations §5.3 cross-ref + canonical_sources registration'
  - 576e9fea: '[editorial] Batch 5 §5.4 + §5.2 — PR-3 ED-731 RS→MS sweep (core canonical) + timeline L129/L179 TT→MS inversion'
  - f2b5d143: '[editorial] Batch 3 — MS trajectory v1 created (D-1 + PR-3) + timeline L21/L181 Catastrophe dating fix + canonical_sources registration'
  - 239c1d3b: '[editorial] Batch 7 — PR-11 BA-1 Baralta theology + PR-12 B-1 Cardinal emanation + PR-13 S-1 RM Lurianic + PR-14 Finding 7 (worldbuilding §3.7)'
  - a7cffdc0: '[editorial] Batch 8 — throughlines dedup: extend T-02 (TL-1/TL-6), T-08 (TL-2); append T-26..T-30 (TL-3/TL-4/TL-5/TL-7/TL-8)'

## Atomization state at end of sequence

- Canonical homes for all new doctrine (PR-1 Finitude §4.3; PR-2 Leap amendment canon/02) established.
- MS terminology propagated across 5 core files (calamity_radiation, threadwork_v30, clocks, glossary, rs_budget) — tier 2 (~44 files) pending.
- Timeline corrections: L16 (pre-Calamity governance/Altonian overlay), L21 (~12y Catastrophe), L32 (7y ministry), L129 (TT 28 → MS 72 Strained), L179 (inversion note), L181 (7y ministry correction cell).
- Worldbuilding §7.1 heading corrected ("Three Indigenous Nations" → "Three Altonian Provinces"). New §3.7 Practitioner Witness Tradition.
- NPC §6 Baralta theology supplement (direct communion + reconciliation + prophylaxis cracking).
- Consolidated Solmund guide §3.2 (Ficinian Cardinal canonical), §4.4 (RM Lurianic canonical), §11.2 (Finding 7 de-flagged), §12 (Seam Text metadata frame).
- MS trajectory v1 (13,409 chars) canonical — 3 of 5 decision points resolved, 2 provisional items flagged.
- canon/02 Leap Mechanism amendment (14,707 chars) canonical — 6 amendments, cross-refs to canon/00 §4.3, §5.3, §9; canon/01; threadwork §2.3 and §31.
- Throughlines: +T-26..T-30 novel, extensions on T-02 and T-08. 32 canonical entries total (was 27).
- Editorial ledger: split into main (~1,747 tokens, active) + archive. 16 new resolution entries (ED-722..ED-737).

## Ledger corrections this commit

- ED-726 (D-5 site-network three-layer) integration target corrected from "canon/02_foundations_amendment_leap_mechanism.md" to "designs/world/ (worldbuilding)". D-5 is about Einhir site-network operational layers, NOT practitioner rendering layers. Prior mis-mapping logged as correction, not re-resolution.

## Valoria/Valorsmark canonical clarifications (Jordan 2026-04-20)

- Valoria = Altonian colonial-era province name (central-north).
- Valorsmark = current Valorian duchy name (same geography).
- Pre-Calamity Einhir-era name for this region: unknowable (D-2 ED-723).
- Analogous: Baiamont→Hafenmark, Lupicco→Varfell. Workplan "Valfell" typo caught before commit.
