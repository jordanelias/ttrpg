# VALORIA CROSS-MODE SIMULATION BATCH C (NON-OPTIMAL ACTORS)
## SIM-IDs: SIM-X-33, SIM-X-34, SIM-X-35, SIM-X-36 | Date: 2026-04-04
## Patches applied this batch: PP-303, PP-304

---

## SIM-X-33 TTRPG Ranged vs Melee (Reload Rigidity)

Actors: Tora (HP crossbow, 12D). Non-optimal: never switches to sidearm at melee range.
Mund (Short Heavy Blade, 13D). Optimal: closes fast, exploits reload rounds.

Round outcomes:
| Round | Tora action | Mund action | Outcome |
|-------|------------|-------------|---------|
| 1 | Fire (12D TN5 Ob1) | Move (open ground) | Overwhelming. Crit. Mund Wound 1. Health resets. |
| 2 | Reload (full round) | Close to melee | Tora full-pool defence. 50% Mund hits. Most likely: miss. |
| 3 | Illegal ranged attack | 9D offence TN6 | Tora action lost. Mund crit. Tora 2 wounds. Incapacitated. |

Findings:
F-33-01: HP crossbow TN5 vs unarmoured Ob1: near-guaranteed Overwhelming + Crit opener. Correct tradeoff for reload penalty.
F-33-02: Reload round paradox: ranged-at-melee rule grants full defensive pool. Reload round = best defensive round. Unintuitive but coherent.
F-33-03: Illegal ranged attack = wasted action → immediate incapacitation. Weapon rigidity catastrophically punished.
F-33-04: Critical Hit overflow causing 2 wounds in 1 hit — not previously defined. PP-304 applied: overflow wounds allowed (each Health-reset = 1 wound). [GAP-SIM-X33-01 RESOLVED]
F-33-05: Sidearm draw cost not stated. PP-304 applied: ready sidearm = free action. Stowed = Retrieve action. [GAP-SIM-X33-02 RESOLVED]

---

## SIM-X-34 Thread Partial Ob Stacking + Memory Re-Citation

Actors: Rhen (13D Leap, TS 45, RS 55). Non-optimal: chains ops without recovery.
Solt (8D debate). Non-optimal: re-cites same source every exchange.

Op outcomes:
| Op | Leap result | Weaving Ob | Weaving result | Composure |
|----|------------|-----------|----------------|-----------|
| 1 | Partial (+1 Ob) | 5 | Partial (+1 Ob more) | 8 |
| 2 | Success | 5 (stack carried) | Partial (+1 Ob more) | 6 |
| 3 | Overwhelming | 7 (stack 3) | Partial | 4 |

Ob stack at scene end: +3. Composure 4. RS 55 unchanged (no successful Weaving).

Debate: Solt cites same source 3 exchanges. Memory +2D claimed each time. Net CT advantage +3 from exploit.

Findings:
F-34-01: Ob stacking not a death spiral. E[~2 partials before success]. Self-correcting. System cap (20) theoretically reachable but practically negligible. [GAP-SIM-X30-02 RESOLVED — healthy, no cap needed below system cap]
F-34-02: Memory re-citation exploit confirmed. PP-303 applied: same source once per debate. [GAP-SIM-X29-01 RESOLVED]
F-34-03: Partial Ob stack reset not defined. PP-304 applied: resets on success of same type or scene end. [GAP-SIM-X34-01 RESOLVED]
F-34-04: Partial Weaving RS change: none (provisional, PP-304). Substrate unaffected until successful contact. [GAP-SIM-X30-03 RESOLVED provisionally]
F-34-05: Composure 0 threshold still undefined. [GAP-SIM-X34-02 — carried]

---

## SIM-X-35 BG Parliamentary Vote (Card Over-Commitment)

State: Season 9. TC=52. Factions: Crown M5, Church M5 I5, Hafenmark M4, Varfell M4, Guilds M3.

Motion outcomes:
| Motion | Proposer | Church | Crown+Varfell | Guilds | Result |
|--------|---------|--------|--------------|--------|--------|
| 1 Assert TC+3 | Church (3 cards, 8D) | All in | 12D (oppose) | Abstain | FAIL. Church Std -1. Church hand exhausted. |
| 2 Crown Policy Inst | Crown (2 cards) | No cards left | 12D Yes | Abstain | PASS. Crown Std +1. |
| 3 Hafenmark Trade | Hafenmark (1 card) | Exhausted | Exhausted | Abstain (3 cards unused) | PASS. Hafenmark Wealth +1. |

Findings:
F-35-01: Full-hand commitment to lost motion = Standing -1 + hand exhaustion. Correctly punished.
F-35-02: Guilds abstain in Motion 2 allows Crown power-grab. Abstaining faction still adds dice to blocking coalition even with low Mandate.
F-35-03: Guilds hoarded 3 cards unused across all motions — maximally self-defeating. System punishes passivity correctly.
F-35-04: Card exhaustion sequencing creates strategic depth. Core mechanic working well.
F-35-05: No rule for all-faction-abstain or zero-support motion. [GAP-SIM-X35-01]

---

## SIM-X-36 Hybrid Domain Echo Misattribution

State: RS=55, IP=45. Crown M4, Varfell Military 5.
PC Almud discovers Vael supply coordination. Scene success (9D, net 3). Standard Echo (+1D one Domain Action). Torben misreads — targets Guilds Wealth (Ob6) not Varfell Military (Ob5).

Crown Domain Action: 5D vs Ob 6. P<1%. FAILURE. Guilds Wealth unchanged. Guilds suspicious of Crown.
Varfell Domain Action (rational): 5D vs Ob 2. P~69%. SUCCESS. Varfell Military 5→6.

Findings:
F-36-01: Misattributed Domain Action mechanically identical to correct failed action. System cannot enforce narrative fidelity. Domain Echo framing lost through info degradation. Player responsibility.
F-36-02: Crown sub-1% action vs Varfell 69% rational action: Military 5→6 uncontested. Asymmetric rational play compounds.
F-36-03: Domain Echo mechanical flow correct. Misattribution is upstream of system. Healthy.
F-36-04: Social pool formula undefined — Cognition×2+History proxied. [GAP-SIM-X36-01]
F-36-05: Domain Echo Overwhelming magnitude undefined. [GAP-SIM-X36-02]

---

## Patches Applied This Batch

| ID | Description | Resolves |
|----|-------------|---------|
| PP-303 | Memory bonus: same source once per debate. Challenge rule added. | GAP-SIM-X29-01 |
| PP-304 | Critical Hit overflow wounds; sidearm draw free action; Partial Ob stack reset at success/scene-end; Partial Weaving = no RS change; Partial Leap = contact with Op Ob +1 | GAP-SIM-X33-01/02, GAP-SIM-X30-02/03, GAP-SIM-X34-01 |

## Open Gaps (new this batch)

| Gap ID | Description | Mode | Priority |
|--------|-------------|------|----------|
| GAP-SIM-X34-02 | Composure 0 threshold effect undefined | TTRPG | P2 |
| GAP-SIM-X35-01 | All-faction abstain / zero-support motion outcome undefined | BG | P2 |
| GAP-SIM-X36-01 | Social pool formula undefined (Cognition×2+Hist proxied) | TTRPG/Hybrid | P2 |
| GAP-SIM-X36-02 | Domain Echo Overwhelming magnitude undefined | Hybrid | P2 |

## Carried Gaps (resolved)

| Gap ID | Resolution |
|--------|-----------|
| GAP-SIM-X29-01 | PP-303 |
| GAP-SIM-X30-01 | PP-304 (Partial Leap = contact + Op Ob +1) |
| GAP-SIM-X30-02 | Healthy — no intermediate cap needed |
| GAP-SIM-X30-03 | PP-304 provisional (no RS change on Partial) |
| GAP-SIM-X33-01 | PP-304 (overflow wounds) |
| GAP-SIM-X33-02 | PP-304 (sidearm free action) |
| GAP-SIM-X34-01 | PP-304 (stack resets on success or scene end) |
