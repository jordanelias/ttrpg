<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: varfell_path_b_v30_infill.md -->

<!-- v30 baseline — renamed from designs/board_game/varfell_path_b_redesign_ed311.md on 2026-04-13 -->
# Varfell Path B — Southernmost Dominion (Redesign Proposal)

<!-- [SUPERSEDED 2026-04-19] VAYNARD THREAD MASTERY (VTM) STRUCK -->
<!-- Per Jordan decision 2026-04-19 (session): VTM was a placeholder mechanic with no canonical advancement rule. -->
<!-- Cultural Reformation (Varfell's primary territorial action) was also STRUCK — incompatible with Vaynard's identity. -->
<!-- Vaynard is a military conqueror (Reinhardt von Lohengramm parallel). Thread/RM is political constituency + genuine -->
<!-- ethical cause, NOT a combat/territorial force multiplier. Varfell expands through military conquest, period. -->
<!-- All VTM references and Cultural Reformation references below this line are SUPERSEDED. Pending: editorial rewrite -->
<!-- of Varfell victory paths, faction actions list, and NPC priority trees. See commits: 297f892 (engine), 13b8f30 (workplan). -->

## ED-311 | Status: AWAITING USER REVIEW
## Date: 2026-04-06
## Context: Full-spectrum review FLAG 18 — 7-condition path reduced for cognitive load

---

## Problem

Path B currently has 7 simultaneous conditions:
1. TCV ≥ 8
2. Control T4 (Vargstad)
3. Garrison or Tribune in T15 (Askeheim)
4. VTM ≥ 3
5. Warden Cooperation (WC) ≥ 1
6. Warden's Accord (WA) ≥ +1
7. T4 CV ≤ 1

WC and WA are mechanically similar (both measure Warden relationship) but on different tracks.
T4 CV ≤ 1 adds a cultural gate that must be actively maintained against natural CV drift.
7 conditions exceeds what players can track without a reference card.

---

## Proposed Redesign — 4 Conditions

**Victory conditions (all simultaneous at Accounting, 2 consecutive):**

| Condition | Threshold | What it measures |
|-----------|-----------|-----------------|
| TCV held | ≥ 8 | Minimal territorial control from the fjords |
| Control T4 (Vargstad) AND T13 (Stillhelm) | both held | Southern gateway to the Southernmost secured |
| VTM | ≥ 3 | Thread awareness sufficient for Warden engagement |
| Warden Recognition | ≥ 2 | Wardens acknowledge Vaynard's stewardship |

**Warden Recognition (WR)** replaces both WC and WA. WR is a single track 0–4:
- WR 0: Wardens unaware or indifferent.
- WR 1: Wardens have observed Vaynard (at least 1 successful Expedition).
- WR 3: Wardens actively cooperate (+1D Thread ops peninsula-wide, per §6 Warden effects).
- WR 4: Edeyja has made substantive contact (Overwhelming Forgetting Check result).



- WA ≥ +1 and WC ≥ 1 → collapsed into WR ≥ 2.

---

## Option B — Keep WA/WC, drop CV gate (5 conditions)

If you prefer to keep WA and WC as separate visible tracks:

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 8 |
| Control T4 AND T13 | both held |
| VTM | ≥ 3 |
| Warden Cooperation (WC) | ≥ 1 |
| Warden's Accord (WA) | ≥ +1 |


---

## Option C — Minimal (3 conditions)

For maximum accessibility:

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 8 |
| Control T4 AND T13 | both held |
| Warden Recognition (WR) | ≥ 2 |


---

## Recommendation

**Option A (4 conditions with WR track)** — Cleaner than current, preserves all narrative dimensions, single track replaces two. WR track is a natural fit for Vaynard's arc (recognition, not metrics). Requires adding WR as a new track to Varfell's mat.

---

## Effect on win probability


**Blocked if RM emerged** (WR collapses on Warden withdrawal) — preserved in all options.
