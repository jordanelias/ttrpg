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
  - B5 stress test: ED-722 dynamic SW under settlement loss/sack scenarios (e.g., Varfell conquers + sacks Himmelenger Cathedral; predicted SW(T9) 5→2, T9 yield 1→0).
  - engine_v4: per-settlement model (vs engine_v3 per-territory aggregate). Aligns with campaign_architecture_v1 §1.1.
  - AER generation mechanic — still unspecified (B3 gap #9, independent of Piety Yield re-run).
P1-BLOCKER count: 0
