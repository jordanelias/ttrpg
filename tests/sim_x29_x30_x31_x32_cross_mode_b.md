# VALORIA CROSS-MODE SIMULATION BATCH B (NON-OPTIMAL ACTORS)
## SIM-IDs: SIM-X-29, SIM-X-30, SIM-X-31, SIM-X-32 | Date: 2026-04-04
## Prior gaps resolved: GAP-SIM-X26-01/02 (PP-254), GAP-SIM-X27-01 (PP-255), X27-02, X28-02
## Remaining gaps carried: GAP-SIM-X28-01 (ED-153 open), new gaps X29-01, X30-01/02/03

---

## GAP RESOLUTIONS (prior batch)
- GAP-SIM-X26-01 (Stamina exhaustion): RESOLVED PP-254. Stamina 0 = Out of Breath −2D, recover via Take a Breath action.
- GAP-SIM-X26-02 (Momentum carry): RESOLVED PP-255. Carries between scenes within session; resets at session start.
- GAP-SIM-X27-01 (RS decay): RESOLVED PP-255. −1 RS per in-game year baseline, applied at Year-End Accounting.
- GAP-SIM-X27-02 (Presence vs Charisma): RESOLVED. Presence not a separate attribute. Charisma is correct.
- GAP-SIM-X28-01 (Wealth diminishing returns): NOT RESOLVED. No rule defined. ED-153 opened.
- GAP-SIM-X28-02 (Coalition pact partial): CLOSED. SIM construct only; no canonical mechanic exists.
- NEW CONFLICT: params_combat Health formula vs design doc §7. PP-254 + ED-152: design doc wins, PP-232 health formula struck.

---

## SIM-X-29 TTRPG Debate

Actors: Aldric Barr (Church, 11D, Att 3). Non-optimal: cites unverifiable sources 2/4 exchanges.
Selde Mehn (Hafenmark, 8D, Att 4). Non-optimal: misreads Barr genre (Past→Present) Exchanges 1-2.

Exchange outcomes:
| Exch | Barr genre | Mehn genre | Interaction | Outcome |
|------|-----------|-----------|-------------|---------|
| 1 | Past Obscuring | Present Revealing (misread) | CROSS | Both succeed, CT +1 |
| 2 | Past Obscuring | Present Revealing | CROSS | Both succeed (Barr 11D, no memory), CT +2 |
| 3 | Past Obscuring | Past Revealing (corrected) | CLASH | Tie (11D vs 10D), no change |
| 4 | Past Obscuring | Past Revealing | CLASH | Tie again, CT +2 final |

Final: Conviction Track +2 (Church mild advantage). No Composure damage. Inconclusive.

Findings:
F-29-01: CROSS rewards both without producing winner. Mehn's misread accidentally avoided a disadvantageous CLASH (11D vs 8D). Design note: CROSS should not be fully symmetric.
F-29-02: Unverifiable citation costs 2D with no benefit. Only harmful in CLASH, irrelevant in CROSS.
F-29-03: Late genre correction + Memory bonus nearly equalised pool gap. Initiative (Attunement) is primary equaliser for low-Cognition orators.
F-29-04: 2 CROSS + 2 CLASH-ties = CT +2, no Composure damage. Non-optimal play produces correctly indecisive result.
F-29-05: Memory re-citation of same source — no restriction stated. Exploit possible. [GAP-SIM-X29-01]

---

## SIM-X-30 TTRPG Thread Operations

State: RS=48 (+1 Ob all Thread ops).
Actors: Kael Vorn (17D Leap, TS 55). Non-optimal: attempts Structural Weaving (Ob 9, P~6%) twice.
Deva Shan (9D Leap, TS 32). Non-optimal: Partial Leap then proceeds to Weave (Ob stacking).

Operation outcomes:
| Op | Actor | Type | Ob | Pool | Result |
|----|-------|------|----|------|--------|
| 1a | Kael | Leap | 2 | 17D | Overwhelming. Next op Ob −1. TS→56 |
| 1b | Kael | Weaving Structural | 8 (9−1) | 17D | Partial. Composure −2. |
| 2a | Deva | Leap | 3 | 9D | Partial. Composure −2. Op Ob +1. |
| 2b | Deva | Weaving Personal | 4 | 9D | Partial. Composure −2. Op Ob +1 more. |
| 3a | Kael | Leap | 2 | 17D | Overwhelming again. −1 Ob next. |
| 3b | Kael | Weaving Structural | 8 | 17D | Partial. Composure −2. |

Final: Kael Composure 6, Deva Composure 6. RS 48 unchanged (no successful Weavings). Deva Op Ob stack +2.

Findings:
F-30-01: Structural Weaving at RS 48 = 6% success for 17D. Correctly calibrated. Non-optimal to attempt without RS improvement.
F-30-02: Sequential Partial Ob stacking no defined cap. [GAP-SIM-X30-02]
F-30-03: Composure drain spiral from serial failures. No exit except scale reduction. Correct design.
F-30-04: RS unchanged across 3 ops (all partials). Baseline decay still applies at Year-End.
F-30-05: RS change on Partial Weaving undefined. [GAP-SIM-X30-03]

New gaps: [GAP-SIM-X30-01]: Leap Partial contact sufficiency for subsequent ops (treated provisionally as yes with Ob +1).

---

## SIM-X-31 Hybrid Mass Battle + General Duel

State: Crown vs Varfell river crossing. Arend duels Vath Turn 1 (Command Pool blackout). Mira joins wrong flank.

Unit outcomes:
| Turn | Crown Left | Crown Right | Varfell Centre | Varfell Right |
|------|-----------|------------|----------------|--------------|
| 1 | Wins (Coh 4) | Loses (Coh 3) | Holds | Retreats |
| 2 | Wins+Mira (Coh 4) | Routs (Coh 1→0, morale fail) | Advances | Routed |
| 3 | Takes flank (Coh 3) | — | Flanks Crown Left | — |

Duel: Arend wins (Vath 2 wounds, incapacitated). But battle: Crown strategically defeated.

Findings:
F-31-01: General duel causes Command Pool blackout. Crown Right routs directly from lack of +1D bonus. Opportunity cost mechanically real.
F-31-02: Pyrrhic duel win. Individual excellence without strategic command produces bad collective outcome.
F-31-03: Two independent non-optimal decisions (duel + wrong flank) combine multiplicatively. Worse than additive. Healthy emergent interaction.
F-31-04: 3-turn battle resolution may compress decision space. Design note.

---

## SIM-X-32 BG Seasonal Accounting at Crisis Thresholds

State: TC=58 (2 from seizure 60), RS=67, IP=45. Crown M5 (Policy Instrument active). Church Standing cap approaching.

Season 12-13 + Year-End outcomes:
- Church delayed TC advance (Wealth push Season 12). TC went 58→57 (Restoration −1)→59→58 (Restoration −1 again).
- Church never crossed TC 60 across 2 seasons. Standing capped at 5.
- Crown Policy Instrument against Church Influence (Ob 5, P~18%): partial, no effect. Timing irrelevant.
- RS decay: −1 at Year-End (67→66). PP-255 confirmed working.
- Hafenmark Influence 5 emerged during great-power hesitation.

Findings:
F-32-01: Smaller factions benefit from great-power hesitation. Hafenmark I→5 during Crown/Church delay.
F-32-02: Policy Instrument at Ob 5 = 18% regardless of timing. Needs lower Ob ceiling or pool scaling.
F-32-03: Restoration Thread ops offset Church TC advance by −2 net across 2 seasons. Effective counter-pressure. Healthy.
F-32-04: RS baseline decay (PP-255) confirmed: −1 at Year-End. RS 67→66. Reaches Thread penalty threshold ~Year 13.
F-32-05: Church Standing cap + stalled TC = win condition blocked by conservative play. Correct consequence.

---

## Cross-Mode Summary

| Finding | Mode | Type |
|---------|------|------|
| CROSS interaction too symmetric — no genre-contextual edge | TTRPG | Design note |
| Memory re-citation exploit (same source, no restriction) | TTRPG | Gap |
| Partial Leap contact sufficiency undefined | TTRPG | Gap |
| Partial Weaving Ob stacking no cap | TTRPG | Gap |
| RS change on Partial Weaving undefined | TTRPG | Gap |
| General duel as Command Pool blackout — mechanically consequential | Hybrid | Healthy |
| Two sub-optimal choices combine multiplicatively | Hybrid | Healthy emergent |
| RS baseline decay confirmed working at Year-End | BG | Confirmed |
| Policy Instrument Ob 5 too high for credible threat | BG | Design note |
| Restoration counter-pressure on TC effective and healthy | BG | Healthy emergent |

---

## New Gaps Registered

| Gap ID | Description | Mode | Priority |
|--------|-------------|------|----------|
| GAP-SIM-X29-01 | Memory bonus re-citation of same source — no restriction | TTRPG | P2 |
| GAP-SIM-X30-01 | Leap Partial — does it establish contact for subsequent ops? | TTRPG | P2 |
| GAP-SIM-X30-02 | Partial Ob stacking — no defined cap | TTRPG | P2 |
| GAP-SIM-X30-03 | RS change on Partial Weaving undefined | TTRPG | P2 |
