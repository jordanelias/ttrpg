# Hunt — social_minmax (munchkin lane)

Arena: social_contest. Working tree at read time. Role: adversarial min-max player looking for
lines that FLATTEN the decision tree (Omega non-dominance).

## Sources read
- designs/scene/social_contest_v30.md (full, 711 lines)
- params/contest.md (full)
- sim/personal/contest/dictionaries.py, armature.py, appraise.py
- charter + 03_threadwork_surface.md

## Dominant lines found

### L-A. Recall +2D per-exchange stacking (Formal Contest) — bonus-source stacking flattens the pool
- §4 Step 3 (v30:166): "Recall bonus: +2D when citing a specific, named, verifiable claim. Binary."
- Grand Contest nerfed to once-per-source (PP-NEW/ED-617, v30:168); **Formal explicitly RETAINS
  per-exchange** ("Formal Contests (3 exchanges) retain per-exchange Recall").
- genre+audience boost is capped at +2D combined (v30:85). Recall is OUTSIDE that cap. So are
  Corroborate +1D/exchange (§2b), Prep +1D and Findings +2D (§9.1, Ex1), and Momentum auto-successes.
- Munchkin: Ex1 pool = base(Cha×2) + Recall2 + Findings2 + Prep1 + genre1 + boost1 + corrob1 = +8D
  over base. Sustained +5D/exchange. Base attribute roll becomes noise.
- STRUCTURAL: the asymmetry (some channels capped, Recall/corrob/prep/findings uncapped) survives
  retuning. Magnitude is tuning; the missing GLOBAL cap is structure. → Omega / Q-robust. NEW.

### L-B. Appraise's boost-read is a solved public lookup (answers brief Q2)
- §4 Step 1 (v30:149-155): Appraise bands 0-2 only reveal the AUDIENCE BOOST. But the boost is a
  DETERMINISTIC function of the dominant faction (params §Faction Boosts / v30:70-78:
  Church=Obscuring, Crown=Revealing, Varfell=Projection, Hafenmark=Memory, Restoration=Revealing,
  Löwenritter=Projection) and the Guilds case is engine-deterministic (dictionaries.guilds_boost_for,
  logos→Memory/pathos→Projection/ethos→Revealing).
- Faction identity + venue are public world-state. So the +1D-boost dimension of the style choice is
  pre-solved by memorizing a 7-row table; Appraise is skippable for bands 1-2. Even a FAILED Appraise
  (misleading read) can't hurt a player who never consults it.
- The designers PROTECTED the *armature* against exactly this (appraise.py PARTIAL-reveal, "not a
  solved lookup"), but the armature is (a) gated off in the 2 asymmetric proceedings, (b) only a
  ≤0.50σ δσ nudge (armature.ARMATURE_MAX_DSIGMA). The protection is on the *smaller* lever; the
  bigger lever (+1D boost) stays a lookup. → Omega non-dominance (solved-strategy). NEW.

### L-C. Obscuring strictly dominated → 4-style tree collapses to 2 (KNOWN-TRACKED ED-1060)
- Corpus admits it: dictionaries.DOUBT_MARKER "Suppression is strictly dominated by Precedent,
  Insinuation by Vision, in every single-exchange contest" (EV-0 marker, no next exchange).
- Worse in current code: DOUBT_MARKER scope_note + v30:217 "the resolver does NOT yet consume
  orientation" — orientation is INERT in all resolution; and CR5 self-Face backfire IS wired
  (params:123 rhetoric.cr5_self_backfire) → failed Obscuring = pure downside, no upside anywhere.
- Munchkin always picks Revealing (Precedent/Vision). Two of four styles dead. → Omega. KNOWN-TRACKED
  ED-1060 (open, unratified). New scope: it's not single-exchange-only; orientation is inert corpus-wide
  in code + CR5 adds asymmetric downside.

### L-D. Coalition REINFORCE ≫ solo CLASH (~5 vs ~0/exchange) (KNOWN-TRACKED ED-297)
- params §"P1 Findings — Resolved 2026-05-17": ED-297 RATIFIED coalition dominance as intended.
  §9.2 shared Concentration pool (PP-237) sums members → larger margins.
- CLASH stalls at median (ED-295; "resolved" via resistance erosion every 2 exchanges — but in a
  3-exchange Formal or single-exchange, erosion barely fires, so solo CLASH stays ~0).
- Munchkin never argues solo; always coalition-REINFORCE. The CLASH/CROSS/solo interaction-type tree
  becomes a dead branch. RATIFICATION examined "reward alliances" but not that it makes solo advocacy
  a dominated non-choice. → Omega. KNOWN-TRACKED, new severity/scope.

### L-E. Face/Rattled buffer is inert → no defensive tradeoff, no cost to losing exchanges
- §4 Step 6 honesty note + §8 Stage-1d status: "strain does not yet consume it in code"; Standing/Face
  is "monotonic-up"; the general strain→Rattled→−1D cascade "remains a v30-surface spec not yet
  realized." Only CR5's narrow failed-Obscuring strip fires.
- Munchkin dumps Focus/Spirit — you never get Rattled, so losing exchanges accrues no penalty, and the
  Focus-defence / Concentration management sub-game is decorative (Spent is the only live drain).
- The RATIFIED omega line-20 stamina/standing/merits three-way tradeoff does not exist in play. →
  Q-robust (a whole tracker inert; resource-decision collapse). KNOWN-UNTRACKED (documented pending,
  no ED tracks it as a live defect).

### L-F. Synthesis — the four games DO collapse to one play pattern (brief Q5)
- Across all four adjudicator types the invariant optimum is: bring a coalition, pick the Revealing
  style matching the KNOWN faction boost + stasis-primary genre, spam Recall citations, skip Appraise,
  never pick Obscuring, dump defensive stats. The adjudicator type only changes WHICH attribute you
  doubled (Cha/Cog/Att) — the PLAY PATTERN is venue-invariant. That is the Omega non-dominance failure
  at the subsystem level. top-down. Medium-high.

## Notes / non-findings
- Charisma is a near-god-stat for Crowd venues (pool Cha×2 + Face Cha×3 + strain Cha-mod), enabling
  venue-shopping when the player controls proceeding type — folded into L-F, not filed separately.
- Panel weighted-by-standing: juror bench-weights are not player-controllable → not exploitable. Skip.
- Momentum auto-successes bypass variance but farming is cross-system, out of arena. Noted only.
