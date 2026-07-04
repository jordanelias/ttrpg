# REFUTE — deterministic-priority-trees

## Finding under test
Claim: all 9 faction Priority Trees (npc_behavior_v30 §8.1–§8.10) are fixed deterministic
if-then ladders with "no stochastic branching beyond embedded contest rolls," letting a
corpus-literate player predict faction action every season → tension with Ω non-dominance.
criterion Omega · direction top-down · P2 · NEW.

## What the text actually says
- §8.1 template + §8.2–§8.10 ARE ordered IF-THEN priority ladders. The *structural* premise
  (deterministic selection ordering) is TRUE of these tables in isolation.
- BUT the trees only rank *candidate types*; they read a large body of state that is (a) hidden
  and (b) mutated by stochastic/emergent processes in the SAME doc:
  - Hidden stats: Tribune Investigate "against faction with highest hidden stats" (§8.5 P3);
    hidden TS — Vaynard "10 (hidden)", Haelgrund "12 (hidden)" (§7.10).
  - Stochastic fuse: Royal Assassination sub-roll 1–6 at game start picks Almud/Lenneth/Torben
    target → Almud Arcs D/E/F, wholesale Crown-behavior divergence (§2.8, §5.2). NOT a contest roll.
  - Contested-asset emergence: Torben Conviction window ED-618 — which faction reaches Disp ≥ +2
    first sets his Conviction, re-shaping the Crown tree's Priority-2 trigger (§2.8).
  - Arc state machine (§5) + §9.2/§9.3: "Belief Scar produced → NPC faction's Priority 2 trigger
    updates immediately… all future BG seasons use the new trigger." Trees are NOT static.
  - Framework Drift (§7), Constrained sub-arc ED-586 (§5.1), Coherence gate ED-665 (§4.3) all
    mutate the state the trees evaluate.
  - §4.1 Decision Fork Scar ≥ 2 → Conviction-crisis d6 table (stochastic, non-contest).

## Decisive intent evidence (finder missed)
- **GD-2 (canon/02_canon_constraints.md §B, line 39), title: "Deterministic threat response
  PRECEDES stochastic action selection."** Canonical faction AI = mandatory deterministic pass
  THEN "stochastic candidate generation." Jordan hard rule HR-9. This directly contradicts the
  claim of "no stochastic branching." The Priority-Tree ladders are the deterministic
  selection-ordering skeleton; the current canonical engine explicitly layers stochastic
  selection on top.
- **Backwards-direction staleness in the finding:** npc_behavior_v30 is 2026-04-13 (CANONICAL
  2026-04-17). GD-2 is 2026-05-17; ED-874 (Jordan-ratified faction Domain-Action resolver,
  "aggregate / deterministic+stochastic", 2026-05-31) postdates it. Reading §8 as the whole
  faction-AI picture ignores the supervening canon.
- **ED-693 (AUD-NPC-03):** 10-season 4-faction priority-tree sim — "Church repetition (Assert)
  is intentional — correct single-minded institutional behavior. Cross-faction reactivity
  confirmed." The repetitive/legible per-faction behavior is a ratified design intent; emergence
  is sourced from cross-faction collision, exactly the charter's "collisions are the emergent
  narrative engine."
- **ED-865/ED-874:** GD-2 "governs action-SELECTION ordering only"; resolver re-justified on
  CK3/EU/Stellaris/KoDP/Six Ages precedent — acclaimed non-dominance-robust strategy games all
  use legible deterministic-priority AI. Precedent explicitly cited as adequate.
- **GD-3:** emergent Revolt→Insurgency→Faction pipeline injects NEW factions mid-game — the
  faction roster itself is non-static, further defeating season-ahead predictability.

## Category error on Omega
Ω non-dominance = "no solvable *player* strategy" (throughlines_meta, PP-672/674). That is a
property of the player's strategy space, not of NPC-AI stochasticity. Legible actors are a
charter VIRTUE: the dramatic-legibility bar demands you can answer "what happens if no one acts
next season" — which requires reasonably predictable factions. The "fix" the finding implies
(inject randomness into NPC choice) would HARM dramatic legibility, cutting against the North
Star. Non-dominance is preserved structurally by: GD-2 stochastic stage, GD-3 emergence, hidden
state, stochastic fuses, arc-trigger mutation, and multi-agent collision — not by making any one
faction's per-season action a coin-flip.

## Verdict
REFUTED. Core factual premise ("no stochastic branching beyond embedded contest rolls") is false
against current canon (GD-2 mandates stochastic action selection; §8 is the pre-GD-2
deterministic-ordering skeleton). Intent DELIBERATE + safeguarded (GD-2/GD-3/ED-693/ED-874). The
inference determinism→predictable→anti-Ω is a category error. Residual (out of scope of this
finding): §8 could carry a pointer to GD-2 — trivial doc-currency debt, backwards direction, P3.
