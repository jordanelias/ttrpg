# Faction / Political — Findings (adversarially verified)

**Canonical head:** `faction_canon_v30.md` + `faction_layer_v30.md` + `faction_behavior_v30.md` +
`faction_state_authoring_v30.md` (overview: `faction_systems_overview_v30.md`).

**Currency correction:** the producer claimed "every one of the four core canon docs carries an
internal CANONICAL/PROVISIONAL contradiction." The critic pass found this is **3 of 4, not 4 of
4** — `faction_layer_v30.md` has exactly one clean status line (CANONICAL, approved 2026-04-17,
zero PROVISIONAL occurrences in 642 lines). The other three (`faction_canon`, `faction_behavior`,
`faction_state_authoring`) do genuinely self-contradict (CANONICAL header, PROVISIONAL body).
Also newly surfaced: **ED-FA-0004 (2026-07-07)** rules "this DOC is correct canon; the ORACLE
lags it" — a recent ruling that partly reframes the PROVISIONAL markers as sim-lag notices rather
than live not-yet-canon status.

## 1. Tracker inventory

Mandate 0–7 (`clamp(round(7·T/(T+6)),0,7)`); Legitimacy/Popular Support 0–7 per-settlement;
Influence/Wealth/Military/Intel 1–7; Stability 0–7 (deterministic floor at ≤2, FSS-LOOP-1);
Cascade Fidelity [-1,+1]; Standing 0–7 per-faction-pair; Conviction Scars (no stated numeric
range/cap); Church Influence, Mending Stability, Institutional Pressure, Public Instability (world
clocks); Accord 0–3 (the one tracker with a dedicated player-facing presentation-layer spec);
Turmoil/Strain 0–10 — **the doc titled "Turmoil System v1" uses "Strain" throughout its body, with
"Turmoil" only at section headers/victory citations; no line declares them the same track.**

## 2. Interaction chain map

- **Domain Action** has no single home doc (`domain_actions` is `doc: null` in
  `module_contracts.yaml`) — fragmented across `params/bg/core.md`, `params/bg/faction_actions.
  md`, and the resolver.
- **Stability Triggers → Collapse (5–6 links)** — was genuinely unbounded until two separate
  2026-05 patches (ED-876 removed a non-monotonic gate; FSS-LOOP-1 added a deterministic floor at
  Stability≤2, sim-tested P(collapse) 0.41→0.97 across pressure levels). Now bounded. The
  residual risk is process (two loop-closing rulings landed within one week of each other,
  suggesting new faction mechanics aren't routinely checked for unbounded feedback before
  ratification), not live mechanics.
- **Wealth=0 → Military drain** — was a one-way ratchet, closed by FSS-LOOP-2 (coupled recovery to
  solvency).
- **Parliamentary Vote NPC-controlled-faction gap — downgraded from "engine-breaking" to P3,
  confirmed by the critic pass as a real refutation.** `faction_layer_v30.md:490`'s "GM controls
  NPC faction votes" line is stale wording only — a deterministic AI rule already exists for the
  one live NPC-only faction (Guilds), and Niflhel is struck (doesn't vote). The residual —
  Schoenland/Altonia's Parliamentary-seat status/vote behavior is unstated — is thin and genuinely
  undocumented, but not the corpus-wide engine-breaking gap it might first appear.
- **Mandate ↔ Settlement L/PS feedback** — circular by design, explicitly damped (saturating
  form) and Stage-4 sim-tested for 30-season convergence — the one loop in the lane with an actual
  cited before/after test.
- **CI Mass Seizure mechanic drifts across three canon sources** (`conviction_track §2`,
  `ci_political §7.6`, `victory_v30 §3.2`) — "reconciliation pending Pass 2f," still open, no
  later ED found closing it.
- **Multi-root Cascade / Institutional Consolidation** — both confirmed degenerate in practice:
  every canonical faction defaults to single-root convictions (multi-root deferred to "Stage 10
  sim observation"), and "no trigger fired this season" is a guaranteed Stability+Accord reward
  that makes pure inaction competitive with active play. Both are honestly logged in the doc's own
  Decision Log as known, undecided trade-offs.

## 3. Cascade check

No chain found with an active, undocumented unbounded-growth risk — the lane's two genuine
cascade risks (Stability collapse, Military/Wealth ratchet) were already caught and fixed by named
rulings within the last several weeks. Turmoil/Strain thresholds are explicitly capped at
+3/season from the territory-instability source by deliberate design.

## 4. Cognitive load

One informed strategic faction-turn decision requires consulting Mandate, Stability, Wealth,
Military, Intel, active Parliamentary motions, active treaties/Casus Belli, Occupation/Accord
state, CI trajectory, and one's own Cascade Fidelity/expectation drift — **9–10 distinct trackers,
against the corpus's own stated strategic ceiling of 7** (treat this count as directional,
±2, not exact — it's the producer's own enumeration, not a corpus-cited figure). "Whose position
is at risk" is genuinely unanswerable from a single line or stat: 5 named Stability Triggers exist
with no surfaced at-risk threshold display anywhere.

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P2 (downgraded from producer's P1) — No maintained player-facing UI model for faction/
  political.** The critic pass found the repo's own 2026-07-04 audit already files this exact gap
  at P2, and the producer's framing of `valoria_ui_ux_v4_1.md` as "the only canonical UI doc" is
  imprecise (the sibling `v4.md` remains authoritative per its own header for content-level UI
  specification). Substance is real — no maintained model exists — but the severity and framing
  needed correction.
- **P1 — Faction count itself is unreconciled (4–8 across four docs)**, fork 10/ED-FA-0001, open,
  no default — confirmed, genuinely blocks any faction-scoped binding work.
- **P2 — Turmoil vs. Strain naming collision**, unresolved in-file.
- **P2 — CI Mass Seizure 3-source canon drift**, open since 2026-05-17.
- **P2 — Derived-stat/formula visibility** — Mandate, Cascade Fidelity, strictness, and the
  expectation-alignment modifier are all formula-computed gates on concrete outcomes with no
  declared UI surface anywhere.
- **P2 (corrected scope) — Status-line self-contradiction is 3 of 4 docs, not 4 of 4** (see
  currency correction above) — still a real currency/legibility defect undermining the
  CURRENT.md-first resolution protocol, just not universal across the lane.
- **P3 — NPC vote coverage gap for Schoenland/Altonia** — thin but genuinely undocumented.
- **P3 — Conviction Scars has no stated numeric range or cap** despite being an active mechanical
  input.
- **P3 — Institutional Consolidation "reward inaction" and single-root Cascade collapse** —
  honestly logged as known, undecided trade-offs in the doc's own Decision Log.
