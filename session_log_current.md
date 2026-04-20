session_id: 2026-04-20-refresh-state
session_close: 2026-04-20
phase: 0
status: complete
last_stage: Session B/C residual cleanup — ED-717 formal closure, factions_personal_v30 Niflhel strike, npc_behavior_v30 incidentals, assassination target Arc Maps (Almud/Torben/Lenneth)
next_action:
  skill: Re-run B3/B4 simulations on corrected engine_v3
  description: >
    All substantive Session B/C residuals resolved. CI cap vs Piety Yield blocker
    resolved per ED-721 (Jordan editorial permission, 2026-04-20): formula
    ambiguity in 'PT_tier × SW/5'. Canonical PT_tier table formalized
    (PT 5 → 1.0; PT 4 → 0.5; PT 3 → 0.25; PT 2 → 0.10; PT ≤ 1 → 0).
    engine_v3.py corrected. Next: re-run B3/B4 batches; previous results
    (saturating cap from S1) are invalidated by formula correction.
  blockers: []
commits:
  - cce9147: ED-717 formal closure — status open → resolved in active ledger (resolution note cites T-15a/b/c additions)
  - 040ac2d: factions_personal_v30 Niflhel dissolution — §8.7 struck, Starting Values row removed, Partial sheets line updated, Royal Decree example, Axis 7, Baralta Leadership Deviation, TK channel, Revolution deviation comparison
  - 6272909: npc_behavior_v30 incidentals — Ehrenwall RS / ED-672 Almud window / Kreutz updated to Löwenritter Autonomy; Hann evidence / Kolbrun Thale / Baralta Arc B / Wardens Priority 2 updated to intelligence brokers; §8.11.3 Niflhel row relabeled Intelligence Brokers
  - f63c0b4: Royal assassination target propagation — Almud Arc D (roll 5–6), Torben Arc Map + Arc D (roll 3–4), Lenneth Arc Map + Arc D (roll 1–2). Cross-ref params/bg/royal_assassination.md
session_highlights:
  - ED-717 formally closed in editorial_ledger.yaml (was status: open despite cb50098 mechanical closure in Session B). Resolution block cites all three throughline commits (5537bc9 + cb50098).
  - factions_personal_v30 Niflhel fully struck — §8.7 replaced with STRUCK banner + redirect to settlement_layer_v30 §4.7–4.9 (Black Markets, Intelligence Brokers, Thread Exploitation Sites); all incidental refs updated.
  - npc_behavior_v30 incidentals swept — Coup Counter refs in Ehrenwall/ED-672/Kreutz now reference Löwenritter Autonomy track; Niflhel refs in Hann/Kolbrun/Baralta Arc B/Wardens now reference intelligence brokers or independent settlement actors; §8.11.3 Outreach table row relabeled.
  - Royal assassination fuse (params/bg/royal_assassination.md) propagated into npc_behavior_v30 §5.2 Arc Maps. Almud gains Arc D (roll 5–6 → Lenneth accession). New Arc Maps added for Torben (Arc A Bought / B Contested / C Uncommitted / D Roll 3–4 Elske retrieval) and Lenneth (Arc A Reformist Queen / B Archive Keeper / D Roll 1–2 revenge arc).
  - Patch 7 backstory strike VERIFIED already complete per 7da338a; session_log open_item was stale. No residual Almud-father-assassination refs remain in character_histories_v30, worldbuilding_v30, or npc_character_analyses_v30 (only explicit STRUCK banners).
  - ED-667 open_item also stale: archived in editorial_ledger_archive_1001_1200.yaml:788 and closed by graduated autonomy in Session B.
open_items:
  - Broader balance pass — Crown-conquest-vs-Church-CI timing (ED-726 flagged but deferred). Three candidate levers: Crown conquest dampening / Church CI acceleration / Altonian Conquest threshold loosening.
  - engine_v4.1–v4.4 (per-settlement Mass Seizure, Capture sequence, Bishop appointment, black markets / intel brokers / Thread sites) — deferred until specific stress tests require.
P1-BLOCKER count: 0
session_highlights_2026_04_20_final:
  - ED-726 RESOLVED (no canonical change, audit): Mass Seizure declaration curve is mechanically sound; Crown conquest timeline (S6–S20) dominates Church accumulate-speed before CI reaches declaration reliability (80+). Mass Seizure declared in only 4/20 runs. Deferred balance levers documented.
  - ED-727 RESOLVED: engine_v4.0 foundational migration implemented at tests/sim_framework/engine_v4.py. 34 settlements populated from §1.6a seed table. Territory.sw is now a derived property. v3/v4 S1 parity verified. All 16 territory SWs match seed table.
  - ED-728 RESOLVED: B6 Cathedral-construction acceleration test executed on engine_v4.0. Key finding: Church infrastructure investment has a **two-step payoff** — build (step 1) → destabilize controller's Mandate (step 2) → Prominence activates yield. Construction in non-Prominent territories is stored value, not immediate yield. SW cap at 5 verified. Rebuild fully restorative.
commits_2026_04_20_final:
  - e7e1681: ED-723/724/725 (AER wiring + engine_v4 proposal + B5 batch)
  - e722dcc: engine_v4_per_settlement_proposal index
  - (this commit): ED-726 audit + ED-727 engine_v4.0 + ED-728 B6 batch
session_highlights_2026_04_20_late:
  - ED-721 RESOLVED (Jordan editorial permission): CI cap vs Piety Yield formula ambiguity. PT_TIER non-linear lookup (PT 5 → 1.0; PT 4 → 0.5; PT 3 → 0.25; PT 2 → 0.10; PT ≤ 1 → 0). T9 yields 1 CI/season floored — Assert remains relevant. Propagated to ci_political_v30 §1, params/bg/ci_seizure.md, params/bg/geography.md, engine_v3.py PT_TIER dict.
  - ED-722 RESOLVED (Jordan editorial permission, option B): Spiritual Weight unified with settlement Religious Building axis. SW(t) = min(5, Σ building_tier per settlement) where None=0/Chapel=1/Church=2/Cathedral=3. Geography SW table seeds starting state; runtime mutates via construction/destruction. Propagated to ci_political_v30 §1, params/bg/geography.md, settlement_layer_v30 §1.5+§1.6a (per-settlement seed table totaling 32 across all territories).
  - ED-723 RESOLVED (Jordan editorial permission): AER mechanic gap #9 was a sim implementation gap, not design gap. Spec already in tracks.md PP-181/PP-565 + institutions.md (Cardinal of Temperance row). engine_v3 wired: P5 Temperance declaration (Mandate vs Ob ⌊AER/2⌋+1 in T9), Year-End decay if not maintained, Altonian Conquest loss condition (IP ≥ 100 + AER ≤ 1).
  - ED-724 RESOLVED (Jordan editorial permission): engine_v4 per-settlement architecture proposal documented at designs/architecture/engine_v4_per_settlement_proposal.md. Five-phase migration plan; v4.0 foundational is high-priority, v4.1–v4.4 deferred.
  - ED-725 RESOLVED: B5 stress test batch executed on engine_v3 with ED-722 mutator helpers. Findings: −1.15 CI/season per Cathedral lost (matches predicted yield collapse 1→0); compound Cathedral+Templar loss = −2.15/season; non-Prominent territory desacralization has zero immediate effect (stored value); recovery via Ecclesiastical Appointment fully reversible; AER mechanic verified working. Document: tests/sim_framework/arc_test_b5_2026-04-20.md.
commits_2026_04_20_late:
  - 6dab223: ED-721 PT_TIER table — formula ambiguity resolved
  - 13fed6f: ci_political_v30 index regen
  - c7399a5: ED-722 SW unification — dynamic infrastructure aggregate
  - 603222e: ci_political + settlement_layer indexes regen
  - 6947834: audit invalidation banners (B3/B4 results, sim_coverage_index)
  - 00e471e: ED-721/722 re-run (arc_test_rerun_2026-04-20.md)
  - a1709d7: settlement_layer index regen + open_items update
  - (this commit): ED-723 AER wiring + ED-724 engine_v4 proposal + ED-725 B5 batch + arc_test_b5_2026-04-20.md
P1-BLOCKER count (post 2026-04-20 late session): 0
