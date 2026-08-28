# GATE A CORRECTIONS — apply silently into the master; do NOT file as findings

## DROP (verified stale against disk — the fix already landed)
H1-038  mass_seizure accord write     → FIXED, ED-FA-0037, `t.accord = ACCORD_MAP[...]`, 4 regression tests
H3-028  Faction.adjust [0.5,7.0]      → FIXED 2026-08-22/23, reads descriptors.faction_bounds(); all six stats floor 0 ceiling 7
H3-045  massbattle roll_pool honours tn → FIXED 2026-08-25 ED-IN-0196; moved to resolution.py; now `assert tn == 7`
H3-073  conviction.py legacy 9        → FIXED 2026-08-24, `CONVICTIONS = descriptors.CONVICTIONS`
H3-074  npe.py 8-member roster        → FIXED 2026-08-24, same single owner
H3-075  knots.py scars 'Loyalty'      → FIXED 2026-08-24, passes 'Honor'

## CLOSE AGAINST RULING (settled, presented as open)
ED-IN-0046 D3 (2026-07-13) "Compact models as a recurring Debt subtype, not a 6th TAG_KINDS family: RULED"
  → closes H8A-058, H8A-078, H8B-028, H8B-037, H8B-047, H8B-057, H8B-061, H8B-062
  → ⚠ D3's own text says it UNBLOCKS §1.3a. H8A-078 asserts the opposite.
  → ⚠ MY OWN BASELINE cross_scale_action_catalogue_v1.md:263-267 restates the PRE-ruling list. Fix separately.
ED-IN-0047 / scale_hierarchy_v1 → B12 Territory/Province resolved; H7A-1539 is the resolution, H1-020 + H9-406 the open version
D5 (governance_consolidation) → §1.0d ≡ G606; H7A-908 rules, H8A-761 still asks

## MERGE KEYS (dedupe before flatten)
H4↔H8A ~30 pairs: same source text, two vintages (40_roster_officer_system.md ≈ rise_to_power_research_v1.md)
  keys: M1..M8 · power_base · consolidation_progress · shared-ladder · player_seats_are_contestable
        · rise_to_power §5 gaps 1-5 · Organization entity · Territory entity · Relay Tier · Reserve Pool
        · Grant Ledger · Muster tag · Cordon-Complete · BYZ-6+IT-5 · Reach-Cap · officer collision
        · Embargo · Ever-Normal Granary · Water Board
H8A↔H8B ~10 pairs: key = the proposal id itself (BYZ-n/CHN-n/HAB-n/IT-n/HRE-n/VEN-SE-n/SE-JP-n/FA-JP-n)
Cross-lane clusters: ledger TAG_KINDS (11 recs/7 lanes) · Standing homonym (11) · L/PS inert (8)
  · Mandate–Faction.L conflation (9) · npc_registry no loader (8) · Π homeostat (7) · treaty inert (5)
  · succeed_governor unreached (4) · casus_belli zero writers (4) · T16/Schoenland (4)

## RE-TAG
slice: ruling with empty provenance → not a Jordan decision; re-grade to gap  (H1-006, H1-009, H1-011, H2-017)
slice: gap + status encoding build state (117 records) → collapse; the status already says it
H3 proposed_ref (14) → the taxonomy's genuine hole: an unratified OPTION in an unresolved fork
H3 audit_ref (8)     → repo measurements, not game content; drop from the game flatten
H7B status: gap (14) + slice: stub (1) → field confusion; status unknown
H5 missing status: on 21 G-block records → status unknown, do not null-fill
parliament-politics: ~24 genuinely parliamentary → faction-strategy; ~27 mis-parked → re-home
  BUT keep the sub-cluster "Parliament has no state of its own" (H9-1330/612/1549) explicit

## STANDING LIMITS (state in the master, do not paper over)
- Six lanes (H1 H2 H3 H4 H8B H9) emitted code-level status_evidence without opening code. Advisory.
- systems/fieldwork/ (21 docs) and systems/social_contest/ (6 docs + ~18 modules) on NO manifest.
- The 5 fieldwork-investigation records are mistagged knot/faction facts, not fieldwork.
- Genuine strong-sense gaps ≈150-190 of 471, not 471.
