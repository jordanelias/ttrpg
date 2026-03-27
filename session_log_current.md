session_close: 2026-03-26
checkpoint: 14-editorial
model: claude-sonnet-4-6
completed_stages:
  - Cross-reference audit CP14 TTRPG vs BG (10 passes, 62 findings)
  - P1 editorial resolution (7 items)
  - P2/P3 editorial round (16 items A-P)
  - Full correction push to both CP14 and BG

commits:
  cp14: 2325655348e0
  bg: c49141521803

corrections_applied:
  cp14:
    - Territory names: all 15 canonical (from map + user corrections)
    - Forced Resolution → Locking and Snapping throughout
    - Rattled: wound-equivalent track (-1D per accumulation)
    - Coherence: full spec with Coherence 2 consult, Coherence 0 monstrous, saving attempt rule
    - Monstrous entities: excess undifferentiated Thread via gaps (not beings from Ein Sof)
    - Knots: +1 Strain for +2D, presence/narration required, closer bonds = higher capacity
    - Domain Ob: direct (1-7), pool adds faction stat if leadership position held
    - Co-movement: d10 replacing d6, no supplements, TPS added to all Thread pools
    - TPS = TS / 10 (round down) added to Leap, Weaving, Pulling, Locking/Snapping pools
    - Renown: full 0-10 table with permission tiers
    - Vaynard: Ambition Track (0-100, 20-point bands), TK 4-5 redesigned, TS acquisition via collection, Southernmost immunity at TK5+TS75+
    - Vaynard victory: Path A (all 15) or Path B (10+ territories + Stillhelm + TK5 + TS75+)
    - Niflhel: four competing networks (Sollvik, Hafenbund, Bernweg, Stiltsift) with supremacy mechanic
    - Eidur Sjostrom: Southernmost elder NPC added
    - Hakan Reusfoldt: Revolution organiser NPC added
    - TC pause threshold: Stability <= 4 (was 5 in §14.7)
    - Attribute pool: 31 points
    - Reach → Influence in §16.3
    - Co-movement deck: 20 cards noted in §12.5
    - History Resonance and Flashback Anchoring supplements removed from co-movement
    - Siege in §12.5: confirmed single roll (already correct)
    - 245 AG (After Galbados) gloss added on first use
    - Church territorial TC: flat scores, expansion lock at TC<70, Valorsplatz ceiling
    - C-03 threshold: 70 (was 80)
    - Rupture as Healing: full narrative canon
    - S-16 through S-20 seasonal events added
    - Grief half-CP refund confirmed
  bg:
    - TC start: 15 (was 22)
    - TN 7 combat (was TN 5)
    - C-03 threshold: 70
    - Church victory B3: removed 'regardless' clause
    - Church territorial TC flat scores added
    - Varfell victory: Path A and Path B
    - Territory names throughout
    - S-16 through S-20 added
    - Rupture as Healing narrative
    - Niflhel four-network structure
    - Eidur Sjostrom and Hakan Reusfoldt in Revolution NPC AI

editorial_still_pending:
  - S-08 Einhir site name (deferred)
  - Co-movement d10 table in BG (uses card system; d10 is TTRPG only - note for next session)
  - E-01 assassination perpetrator (intentionally unresolved)
  - Vaynard Private Collection transfer Shocking Event scene procedure (design pending)
  - Niflhel Supremacy Mechanic seasonal resolution procedure (design pending)
  - Coherence 0 saving attempt procedure (design pending)

next_action:
  recommended: Apply corrections to project-files CP14 (currently out of sync with GitHub version) then proceed to Phase 3 simulation or CP15 compilation
  model: Sonnet 4.6
  note: Project files still show old CP14 - GitHub is now canonical
