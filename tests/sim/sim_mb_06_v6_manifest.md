# SIM-MB-06 v6 Module Manifest
# Iteration: v5 → v6 (Jordan-directed bug-hunt + facing architecture)
# Date: 2026-05-12
# Status: EXPLORATORY (continued from v5 — three open tensions B-ii/C/E)
#
# CHANGES FROM v5:
#
# 1. HALT-CELL BUG FIX (critical, source of Side A bias)
#    run_battle's halt logic used raw pattern coords (orig_r) without
#    applying mirror for Side B. Result: Side B halted the WRONG cells
#    (orig_r=4 instead of orig_r=0 at row 12 contact). Front cells kept
#    walking through enemy formation; back cells froze. Caused Side A to
#    win 80% of Line-vs-Line mirror matches.
#    Fix: halt logic now uses oriented_pattern() for mirror-aware lookup.
#    Verified at n=200: bias collapsed from 80/20 to ~52/48 (within noise).
#
# 2. PER-CELL FACING (architectural — Jordan request 2026-05-12)
#    Each cell has a front-face direction. cell_facing(advance_dir) returns
#    (dr, dc) unit vector — currently uniform across formation = advance_dir.
#    Required for pincer/encirclement mechanics to be meaningful.
#
# 3. ENGAGEMENT ANGLE MODIFIER (consequence of facing)
#    engagement_angle(defender_pos, defender_facing, attacker_pos) classifies
#    contact as FRONT / FLANK / REAR via cosine of approach vector vs facing.
#    ANGLE_DEF_MOD = {FRONT: 0, FLANK: -1, REAR: -2} applied to defender pool.
#    Side effect: Cannae (Horseshoe vs Arrowhead) now works at 62% naturally
#    via wings wrapping → flank/rear attacks → reduced Arrowhead defense.
#    The "B-ii curving wings" tension may be obsoleted by this mechanic.
#
# 4. PHASE C POOL FORMULA — variant selectable via POOL_VARIANT global
#    - "baseline": original Bii (base × troop_frac × engage_frac)
#    - "C-i": drops troop_frac (overcorrects)
#    - "C-ii": max(50% of base×engage_frac, baseline) — VALIDATED, default
#    Composite-vs-Uniform: 5% → 38.3% (closer to balanced)
#
# RESULTS WITH FIX:
#   - Side A bias: GONE (52/48 at n=200)
#   - Composite balance: 38.3% (was 5%, target 35-50%)
#   - Cannae: 62% (was 80% pre-fix, now reflects real angle-attack dynamics)
#   - Lethality: 9.7 turn mean (still outside 3-6 target — different issue)
#
# REMAINING TENSIONS:
#   - Arrowhead vs Line: 0% (E tension — tip races forward, dies isolated)
#   - Horseshoe vs Line: 0% (unknown — thin center collapses too fast?)
#   - Battle duration too long (lethality target unmet)
#
# NOT YET CANONICAL — atom architecture still EXPLORATORY.
# ED-814 remains the canonical mechanic; this would supersede if ratified.
