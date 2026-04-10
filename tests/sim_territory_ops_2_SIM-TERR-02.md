# Simulation Report: Territory Operations Suite — Round 2
## Test ID: SIM-TERR-02
## Date: 2026-04-09
## Modes: A + D + J + L
## Focus: New scenarios and conditions emerging from PP-500–PP-524 interactions;
##         TCV discrepancy audit; victory condition edge cases under new territory mechanics;
##         CB system under realistic campaign conditions; Diplomatic Transfer exploitation;
##         contested-territory state cascade; post-Battle retreat chain reactions.
## Sources: params_board_game.md (1780 lines), victory_architecture_v1.md (472 lines),
##          valoria_bg_v05 (734 lines), geography_design.md (138 lines),
##          canon/02_canon_constraints.md (25 lines)

---

## FETCH LOG
references/params_board_game.md:              ✓ (1780 lines)
designs/board_game/victory_architecture_v1.md: ✓ (472 lines)
designs/board_game/valoria_bg_v05:            ✓ (734 lines)
designs/setting/geography_design.md:          ✓ (138 lines)
canon/02_canon_constraints.md:               ✓ (25 lines)

---

## PRE-SIMULATION AUDIT: TCV DISCREPANCY

victory_architecture_v1.md §1 TCV table vs params_board_game.md TCV table:

| Territory | victory_architecture TCV | params_board_game TCV | Δ |
|-----------|--------------------------|----------------------|---|
| T8 Gransol | 3 | 4 | −1 |
| T9 Himmelenger | 5 | 3 | +2 |
| T12 Sigurdshelm | 3 | 3 | 0 |
| T1 Valorsplatz | 5 | 5 | 0 |
| T10 Spartfell | 1 | 2 | −1 |
| T3 Lowenskyst | 2 | 2 | 0 |
| T14 Ehrenfeld | 2 | 2 | 0 |
| Total (victory_arch) | 30 | — | — |
| Total (params) | 29 (PP-470) | 29 | 0 |

Also: victory_architecture lists T17 as "Reinstadt" — geography_design.md canonical name is
"Halvarshelm." This is a naming error in victory_architecture_v1.md.

**[FINDING AUD-01 — P1]:** T9 Himmelenger TCV conflict: victory_architecture = 5, params = 3.
Church's starting TCV (victory_arch) = 3 (T9 at 5 matches "Crown 12, Hafenmark 8, Varfell 6,
Church 3" only if T9=3). But victory_arch body lists T9=5. Starting TCV sum in victory_arch =
5+3+5+3+1+2+2+1+1+1+1+1+1+1+1+0 = 29, not 30 as stated. Consistent with PP-470 (total=29).
Both docs agree on total=29 but assign different TCV to T8 and T9. This matters enormously:
Church's starting TCV = 5 (victory_arch T9=5) or 3 (params T9=3). If T9=5, Church starts
at TCV 5 and needs only +3 to reach victory threshold (TCV≥8). If T9=3, Church needs +5.

**[FINDING AUD-02 — P1]:** T8 Gransol TCV conflict: 3 vs 4. Hafenmark starting TCV:
victory_arch (T8=3): 3+1+1+1 = 6. Params (T8=4): 4+2+1+1 = 8.
These are completely different Hafenmark starting positions (6 vs 8). The stated "Starting TCV:
Crown 12, Hafenmark 8, Varfell 6, Church 3" in BOTH documents matches only the params version
(T8=4, T9=3). The victory_arch §1 table body is internally inconsistent with its own starting
TCV summary row.

**Provisional ruling:** params_board_game.md TCV table (T8=4, T9=3) is canonical per
PP-470 verification. victory_architecture_v1.md §1 body table contains errors in T8 and T9
rows. The stated starting TCV summary (Crown 12, Hafenmark 8, Varfell 6, Church 3) in both
documents is the correct anchor — the params table body is consistent with it.

**[FINDING AUD-03 — P2]:** victory_architecture_v1.md T17 listed as "Reinstadt." Canonical
name per geography_design.md: "Halvarshelm." Text error in victory_architecture_v1.md.

---

## ═══════════════════════════════════════════════════════
## SCENARIO 1: CB SYSTEM UNDER CAMPAIGN CONDITIONS
## Season 6 — Crown holds 2 Treaty CBs vs Varfell and Hafenmark;
## Varfell holds PP-501 tactical CB vs Crown (from Seizure attempt);
## Church holds PP-494 tactical CB vs Crown (from Seizure attempt)
## ═══════════════════════════════════════════════════════

### Setup
- Crown: Mandate 5, Military 4, Stability 4. Holds T1, T2, T3, T5, T6, T14.
  TCV = 12. Holds 2 permanent treaty CBs (vs Varfell: T4 pledge betrayal; vs
  Hafenmark: T7 pledge betrayal). Treaty CBs never expire.
- Varfell: Mandate 4, Military 4, Stability 4. Holds T4, T11, T12, T13. TCV = 6.
  Holds 1 tactical CB vs Crown (from failed Graduated Seizure attempt on T5, Season 5).
  CB expires Season 8.
- Church: Mandate 5, Military 4, Stability 5. Holds T9. TCV = 3.
  Holds 1 tactical CB vs Crown (from failed Piety Spread that was contested — actually
  Piety Spread does not generate CB; only Graduated Seizure does per PP-494).
  [CORRECTION: Church has no CB at this point — Piety Spread is not a CB-generating action.]
- Hafenmark: Mandate 4, Military 3, Stability 4. Holds T7, T8, T10, T17. TCV = 8.
  Holds 0 CBs.

### MODE A — CB Bonus Impact

**A1. Crown attacks T4 (Grauwald, Varfell) spending Treaty CB (+2D):**
Crown Military pool: 4D + 2D (CB) = 6D vs Ob = Varfell Military ÷ 2 = 2.
P(Attacker margin > 1 = Ob−1) sufficient for territory capture:

Actually PP-476 margin table: Margin > Ob → opponent unit destroyed + territory captured.
Ob = 2. Need margin > 2 (margin ≥ 3). Crown net − Varfell net ≥ 3.

Crown 6D vs Varfell 4D + Fort 0D = 4D (T4 has no fort).
Expected Crown net: 6 × 0.40 − 6 × 0.10 = 1.80
Expected Varfell net: 4 × 0.40 − 4 × 0.10 = 1.20
Expected margin: 0.60. P(margin ≥ 3) requires significant Crown outperformance.

Approximating: P(Crown net ≥ 3 AND Varfell net ≤ 0) ≈ 15% × 25% ≈ 4%.
P(Crown net ≥ 4 AND Varfell net ≤ 1) ≈ 8% × 45% ≈ 4%.
Rough P(margin ≥ 3): ~12–15%.

Compare without CB: Crown 4D vs Varfell 4D.
P(Crown net − Varfell net ≥ 3): ~6–8%.

CB +2D roughly doubles the probability of a decisive victory (12–15% vs 6–8%).

**[FINDING CB2-A-01 — P2]:** CB +2D bonus is meaningful but not dominant at even Military.
The primary value of CB is at asymmetric fights: Crown Military 4 vs Varfell Military 4+Fort,
where the +2D compensates for the fort disadvantage. T4 has Fort 0 — CB here is a nice bonus
but not a game-changer. CB is most impactful against fortified territories where the fort dice
create significant Ob disadvantage. This is good design: CBs matter most precisely when
military aggression is most politically legitimated (taking fortified positions requires both
military capability and political will).

**A2. Varfell spends CB vs Crown attacking T5 (Feldmark):**
Varfell Military 4D + CB 2D = 6D vs Crown Military 4D + Fort 0 = 4D. Ob = Crown Mil ÷ 2 = 2.
Same analysis as A1: Varfell has ~12–15% chance of decisive victory.
T5 is Feldmark (Crown Breadbasket, TCV=1). Varfell spending a 3-season expiry CB to
take a TCV=1 territory: strategically expensive. Varfell needs T5 only if chasing TCV≥10
(Path A) and has exhausted other routes.

**[FINDING CB2-A-02 — P2]:** CB cap (2 per faction pair, PP-501) creates an interesting
meta-game: factions must decide whether to accumulate CBs (max 2 treaty + tactical) for
a decisive strike or spend tacticals quickly before expiry. Treaty CBs never expire, so
treaty-betrayal CBs are long-game insurance. Tactical CBs (3-season window) create
pressure: use them within 3 seasons or lose them.

### MODE D — Edge Cases

**D1. CB and Diplomatic Token interaction (PP-518): dual-faction targeting**
Crown holds Treaty CB vs Varfell. Hafenmark has placed a Diplomatic Token on Crown's mat
(from Diplomat card, prior season). Crown declares March into Varfell T4 spending CB.
PP-518: Diplomatic Token suppresses CB spending for one season — but the Token is on
CROWN's mat (placed by Hafenmark). The Token says "target faction counts as Support in
Parliamentary Sessions." PP-518 says "a faction holding a Diplomatic Token on a TARGET
FACTION'S mat cannot spend a CB against THAT faction."

Wait — re-reading PP-518: "A faction that holds a Diplomatic Token on a target faction's
mat." The Hafenmark Diplomat card places a token on the TARGET faction's mat (PP-432:
"Place 1 Diplomatic Token on target mat"). Hafenmark targeted Crown → token is on Crown's
mat, held by whom? The token is ON Crown's mat, meaning Crown is the target.

PP-518 says "a faction holding a Diplomatic Token on a target faction's mat cannot spend
CB against that faction." This means: if Varfell had placed a Diplomatic Token on Crown's
mat, Varfell cannot spend CB vs Crown. But the token is Hafenmark's, placed on Crown's mat.

**[FINDING CB2-D-01 — P1]:** PP-518 ownership ambiguity. The Diplomatic Token is placed
on the TARGET faction's mat by the ACTING faction. PP-432: "Place 1 Diplomatic Token on
target mat." PP-518 references "a faction holding a Diplomatic Token on a target faction's
mat." The token physically sits on Crown's mat — does Hafenmark "hold" it (they placed it)
or does Crown "hold" it (it's on their mat)?

Interpretation A (placer holds): Hafenmark holds the token on Crown's mat → Hafenmark
cannot spend CB vs Crown. Crown is free to spend CB vs others.
Interpretation B (host holds): Crown holds the token on their own mat → Crown cannot
spend CB vs whoever placed it (Hafenmark).

Interpretation A is correct (the Diplomat faction "holds" the relationship represented by
the token). But Interpretation B is what a player reading "token on Crown's mat" would
assume. The rule needs explicit clarification: "The faction that placed the Diplomatic
Token cannot spend a CB against the faction whose mat the token sits on."

**D2. [FINDING CB2-D-02 — P2]:** CB and Battle sequence within contested territory (PP-519).
Crown's T5 is contested (Varfell unit present from a prior Partial battle). Varfell holds
CB vs Crown and declares March into T5 (which they're already in as contesters). Does "March"
apply to a territory Varfell's unit already occupies? Per PP-519: contesting unit persists
until "Legionary Outward withdrawal or next Battle loss." A new Legionary Outward card
targeting T5 while already contested would trigger a new Battle — but Varfell is already
the contesting force. Does Varfell play a Legionary card to initiate a "conquest attempt"
from their contested position, or is the contesting state itself the ongoing assertion?
No rule clarifies whether a contesting faction can formally "upgrade" their occupation
attempt with a new Legionary card play (spending CB) or whether they must wait for the
controller to attempt to dislodge them.

**D3. Riskbreaker burns Varfell Patience Protocol CB (PP-524):**
Riskbreaker Priority 6: "If Varfell holds an active Patience Protocol CB AND Riskbreakers
have intel on Varfell Tribune operations this season (Priority 1 Investigate fired
successfully): Riskbreakers burn the CB."
Riskbreaker Priority 1: "Investigate" — no target or territory specified.
If Riskbreakers investigate in a territory where Varfell has NO Tribune active this season,
does Priority 1 "fire successfully"? Only if investigation yields a result. A successful
Investigate with no Tribune activity would find nothing relevant to Patience Protocol.
**[FINDING CB2-D-03 — P2]:** PP-524 Priority 6 requires Priority 1 "fired successfully"
— but "successfully" is undefined in the context of Riskbreaker NPC AI actions. Priority 1
Investigate needs a success threshold (is it an automatic success? Ob-based? Against whom?).

---

## ═══════════════════════════════════════════════════════
## SCENARIO 2: DIPLOMATIC TRANSFER EXPLOITATION
## Crown offers T6 (Stillhelm, TCV=1) to Varfell in exchange for Varfell
## ceding T4 (Grauwald, TCV=1) to Crown — simultaneous bilateral transfer.
## Both factions approaching co-victory threshold (Crown+Varfell).
## ═══════════════════════════════════════════════════════

### Setup (Season 10)
- Crown: TCV = 11 (needs 12 for co-victory). Holds T1,T2,T3,T5,T14.
- Varfell: TCV = 7 (needs 8 for co-victory). Holds T4,T11,T12,T13.
- Co-victory (Crown+Varfell) condition: Crown TCV ≥ 12 AND Varfell TCV ≥ 8 AND VTM ≥ 3 AND RS ≥ 50.
- Current RS: 58. VTM: 3. Both co-victory thresholds require TCV gains.

### MODE A — Transfer Mechanics

**A1. Bilateral Diplomatic Transfer procedure (PP-505):**
Both factions declare mutual agreement in Phase 2 Planning.
Crown transfers T6 to Varfell; Varfell transfers T4 to Crown.
Both resolve at Phase 4 Priority 4 (Social tier).

Post-transfer state:
- Crown: loses T6 (TCV −1), gains T4 (TCV +1). Net Crown TCV: 11 − 1 + 1 = 11. No change.
- Varfell: loses T4 (TCV −1), gains T6 (TCV +1). Net Varfell TCV: 7 − 1 + 1 = 7. No change.

Wait — T6 Stillhelm is TCV=1 and T4 Grauwald is TCV=1. A straight swap produces no TCV change
for either faction. Co-victory conditions remain unmet.

But: T6 is adjacent to T13 (Varfell-held Oastad), and controls Southernmost access. T4 is
adjacent to T14 (Crown-held Ehrenfeld). Both have strategic value beyond TCV:
- Crown gains T4: now controls T4+T14, creating a western corridor.
- Varfell gains T6: now controls T6+T13, locking both Southernmost access gates (Varfell
  needed T6 for Path B — control T4 AND T13. Wait: Path B requires T4 AND T13. Varfell
  just gave away T4! Path B blocked.)

**[FINDING DT-A-01 — P2]:** Bilateral transfer can be self-defeating if factions don't
verify Path prerequisites before trading. Varfell swapping T4 for T6 breaks Varfell Path B
(requires T4 AND T13). A faction cannot recover a traded territory quickly (1-season TCV
freeze, and Crown now controls T4 with no incentive to return it). Players need to check
all Path prerequisites before agreeing to any transfer.

**A2. Non-bilateral transfer: Crown gives Varfell T6 for free (strategic gift).**
Crown TCV: 11 − 1 = 10. Varfell TCV: 7 + 1 = 8. Varfell now meets co-victory TCV ≥ 8.
Crown does not yet meet TCV ≥ 12.

PP-505: transferred TCV frozen for 1 season (Transfer Marker). Varfell's new T6 TCV does
NOT count toward co-victory for 1 season. So at Accounting: Varfell's effective co-victory
TCV = 7 (T6 frozen). Threshold not met this season.

Season 11: Transfer Marker lifted. Varfell effective TCV = 8. Crown must reach TCV = 12 by
Season 11 Accounting to declare co-victory. Crown at TCV 10 needs +2 more. Options: March
into two Hafenmark territories (T7, T17 — both TCV 1), or T8 Gransol (TCV 4 — would bring
Crown to TCV 14, sufficient). Battle required.

**[FINDING DT-A-02 — P2]:** Free territory gifts in service of a co-victory path work
mechanically. The 1-season TCV freeze is the correct gate: it forces the co-victory to
require 2-season holding, not same-season declaration. Crown giving T6 to Varfell then
immediately needing 2+ more TCV creates a genuine Season 11 race. This is the correct
design tension — co-victories require genuine coordination across multiple seasons, not
same-season transfers.

**A3. Transfer TCV interaction with co-victory 2-season confirmation:**
Suppose Crown reaches TCV ≥ 12 and Varfell reaches TCV ≥ 8 in Season 11. Both conditions
met. Accounting Step 12: co-victory check fires. Season 12 Accounting: second confirmation.
If either faction loses TCV between Season 11 and Season 12: co-victory resets (first
Accounting confirmation lost). T6 Transfer Marker has lifted (1 season = done after Season 11
Accounting). No interaction between Transfer Marker and the 2-season holding requirement.
Clean: transfer freeze and holding confirmation are independent timers.

### MODE D — Edge Cases

**D1. [FINDING DT-D-01 — P1]:** Bilateral transfer priority — which resolves first?
Crown transfers T6 to Varfell; Varfell transfers T4 to Crown. Both resolve at Phase 4
Priority 4 (Social tier), within-tier: descending Stability. Crown Stability 4 = Varfell
Stability 4: simultaneous resolution per within-tier tie rules.

When simultaneous: both transfers fire at the same moment. Crown loses T6 and gains T4;
Varfell loses T4 and gains T6. In theory, both transfers are interdependent — at the moment
Crown's transfer fires, T4 is still Varfell's. At the moment Varfell's transfer fires, T6
is still Crown's. Simultaneous resolution means both transfers are declared against the
pre-resolution state. This is valid — the transfers reference the declared agreement, not
the live board state.

However: if Crown's transfer fires FIRST (tiebreak scenario: Crown > Varfell per tiebreak
order PP-502): T6 now belongs to Varfell before Varfell's transfer fires. Varfell's transfer
of T4 to Crown then fires — Varfell still holds T4 (the transfer hasn't fired yet), so T4
transfer is valid. Both complete. Net: identical to simultaneous.

But what if Crown Stability > Varfell Stability at resolution time? Crown's T6 transfer
fires. Now T6 is Varfell's. Varfell has gained TCV +1. If Varfell's T4 transfer is somehow
blocked (e.g., Varfell withdraws consent between Phase 2 and Phase 4 resolution): Crown
has given away T6 and received nothing. Is consent withdrawal possible between Phase 2 and
Phase 4? No rule prevents a faction from declaring withdrawal of consent during Phase 4
before their action resolves.

**[FINDING DT-D-02 — P1]:** Consent withdrawal between Phase 2 and Phase 4 is undefined
for Diplomatic Transfer. If both parties declare simultaneously in Phase 2, can one party
renege before Phase 4 Priority 4? If yes: the reneging faction exploits the other's transfer
and keeps their territory. The reneging faction earns a CB (PP-505), but a Treaty-CB is
permanent only for treaty betrayal. PP-505 creates a 3-season tactical CB from the transfer
initiation, not treaty law. This is insufficient deterrent against tactical reneging.

**D2. [FINDING DT-D-03 — P2]:** Diplomatic Transfer and Hafenmark Parliamentary Session (PP-432).
If Hafenmark calls a Parliamentary Session and Crown votes "Oppose" while holding a Diplomatic
Token from Hafenmark: the Token says "count as Support regardless of declared vote" (PP-432).
But Crown declared Oppose. The Token overrides Crown's declared vote to Support. However,
Crown is also simultaneously planning a Diplomatic Transfer with Varfell in Phase 2.

The Diplomatic Transfer and Parliamentary Session are both Phase 2 declarations. Can Crown
declare Oppose in the Parliamentary Session AND declare Diplomatic Transfer with Varfell in
Phase 2 simultaneously? Both are Phase 2 declarations. There's no restriction — they're
different actions. But the Diplomatic Token forcing Crown's vote to Support in the
Parliamentary Session while Crown is diplomatically active with Varfell creates an odd
political situation (Crown appears to support Hafenmark publicly while conducting a private
deal with Varfell). No mechanical issue, but worth noting for faction AI.

**D3. [FINDING DT-D-04 — P2]:** Diplomatic Transfer and Formal Crown Treaty (PP-423 / victory_architecture §3.1).
"Formal Crown Treaty: Senator Outward, Crown only. Cannot combine with Diplomatic Outreach
to Schoenland same season." Can Crown play a Formal Crown Treaty with Varfell AND execute a
Diplomatic Transfer with Varfell in the same season? Treaty uses Senator Outward card.
Diplomatic Transfer uses no card. These are different action types — Treaty consumes Crown's
Senator card; Transfer is card-free. Both can fire in the same season. This creates a
powerful combo: Crown proposes Treaty to Varfell (political relationship) AND transfers
T6 as a goodwill gesture in the same season (no card cost). No prohibition stated.

---

## ═══════════════════════════════════════════════════════
## SCENARIO 3: CONTESTED-TERRITORY STATE CASCADE
## Varfell attacks T14 (Ehrenfeld, Crown, Fort 3) — gets Partial.
## Contested state fires. Crown then Governs T14. Hafenmark attacks T8.
## Multiple contested states simultaneously across the board.
## ═══════════════════════════════════════════════════════

### Setup (Season 8)
- T14 Ehrenfeld: Crown control, Fort 3. Crown Military 4 + Fort 3 = 7D defensive pool.
- Varfell Military 4D (no CB) vs Crown 4D + 3D Fort = 7D. Ob = Crown Mil ÷ 2 = 2.
- T8 Gransol: Hafenmark capital, Fort 1. Hafenmark Military 3 + Fort 1 = 4D defensive.
- Crown Military 4D vs Hafenmark 4D. Ob = 2.

### MODE A — Partial Battle Cascade

**A1. Varfell attacks T14: probability of Partial**

Varfell 4D: E(net) = 1.20. P(≥1 net) ≈ 74%. P(≥3 net) ≈ 15%.
Crown 7D: E(net) = 2.10. P(≥1 net) ≈ 97%. P(≥3 net) ≈ 54%.

PP-476 margin: margin = Varfell net − Crown net (if positive).
P(Varfell margin > Ob=2) = P(Varfell net − Crown net ≥ 3): roughly P(Varfell net ≥ 4 AND Crown net ≤ 1) ≈ 8% × 3% ≈ 0.24%. Near-impossible.
P(Partial — Varfell margin 1–2): P(Varfell net − Crown net = 1 or 2): ~5–8%.
P(Crown wins): ~88–92%.
P(Draw): ~3–5%.

More likely: Crown wins outright (margin > 2 in Crown's favor). Varfell unit retreats per PP-506.

But let's consider: Varfell uses CB (+2D) against Crown. Now Varfell 6D vs Crown 7D.
Varfell E(net): 1.80. Crown E(net): 2.10.
P(Varfell decisive win): ~3–5%. P(Partial — Varfell margin 1): ~15%. P(Crown wins): ~70%.

So even with CB, attacking Fort 3 is a long shot. The contested state (Partial) occurs in
roughly 15% of CB-backed attacks. More commonly, Varfell retreats (PP-506).

**A2. Contested state at T14 (Partial case):**
Varfell unit remains in T14 (PP-519). Crown's Domain Actions in T14 at +1 Ob.
Crown plays Consul Inward (Govern) T14: Mandate 5D vs Ob = Prosperity ÷ 2 + 1 (contested) + round up.
T14 Prosperity = 4 (starting). Govern Ob = 4÷2 = 2 + 1 contested = 3.
Crown pool = 5D (Mandate). P(≥3 net from 5D) ≈ 42%.

Crown Govern T14 contested: 42% success vs 85% uncontested. Significant degradation.
If Govern fails: Prosperity −1. T14 drops to Prosperity 3. Repeated failed Governs
spiral the territory into decline while the contesting unit remains.

**[FINDING CONT-A-01 — P2]:** Contested-state +1 Ob degrades Govern significantly.
A fort-3 territory under contested occupation becomes difficult to govern. The intended
consequence — military pressure impairs civil administration — is mechanically correct.
The spiral risk (fail Govern → Prosperity drops → Govern Ob drops but Prosperity penalties
compound) is a natural mechanic but should be noted for reference cards.

**A3. Simultaneous contested states: T14 (Varfell contesting Crown) AND T8 (Crown contesting Hafenmark):**

T8 Gransol (Hafenmark capital ★). Crown attacks: Battle resolves Crown Partial.
Crown unit remains in T8. Hafenmark Govern T8 Gransol: Mandate 4D vs Ob = Prosperity ÷ 2 + 1
(contested). T8 starting Prosperity 5: Ob = 3 + 1 = 4. P(≥4 net from 4D) ≈ 8%.

Hafenmark capital under contested occupation: nearly ungovernable. 8% Govern success.
Hafenmark Wealth generation from T8 degrades dramatically. Hafenmark's Parliamentary
Sovereignty victory requires TCV ≥ 12 + Mandate ≥ 4 + PI ≥ 5 + Crown Mandate ≤ 3.
With Crown contesting T8, Hafenmark cannot reliably Govern its own capital. Mandate
recovery via Govern Overwhelming in own capital (PP-174): Mandate +1 in own capital,
but Govern is at 8% success rate. Mandate starvation.

**[FINDING CONT-A-02 — P1]:** Capital contested state creates a near-permanent
administrative lock. T8 Gransol (Prosperity 5) under contestation: Govern Ob = 4,
Pool = Mandate 4D, P(Suc) = 8%. This is not a temporary disruption — it's a near-permanent
governance failure until the contesting unit is dislodged. Hafenmark's only recourse:
play Legionary to initiate a Battle to dislodge Crown's unit. But Hafenmark Military 3
vs Crown Military 4 at T8 (Hafenmark capital): Ob = Crown Military ÷ 2... wait.

Re-reading PP-476 and Battle setup: Battle Ob = DEFENDER Military ÷ 2. In a dislodgement
Battle (Hafenmark attacks Crown's contesting unit in T8): who is the "attacker" and who is
the "defender"? Crown's unit is CONTESTING — not the territory controller. Hafenmark
controls T8. Crown's unit is the occupying force.

**[FINDING CONT-A-03 — P1]:** Dislodgement Battle role ambiguity. When a territory
controller fights to remove a contesting unit: who is attacker and who is defender?
The contesting unit is physically in the territory but does not control it. The controlling
faction attacking their own territory to remove a hostile unit is structurally unusual.
Options:
(a) Territory controller is always "defender" in Battle: Hafenmark is defender vs Crown contester-attacker. Ob = Hafenmark Military ÷ 2 = 2. Crown contester rolls (as attacker). But Crown is the contesting unit trying to HOLD ground, not take it.
(b) The faction that initiated the contestation is always "attacker": Crown is always attacker, Hafenmark always defender, regardless of who called the Battle.
(c) The faction playing the Legionary card that triggers the Battle is "attacker." Hafenmark plays Legionary to dislodge → Hafenmark is attacker vs Crown defender. Ob = Crown Military ÷ 2 = 2. Hafenmark Military 3 + Fort 1 (it's their own fort) = 4D. Crown Military 4D (no fort benefit — they don't control the fort). Hafenmark 4D vs Crown 4D at Ob 2.

Option (c) is most mechanically consistent with "Battle = Legionary card play initiates." But option (c) means Fort benefits apply to Hafenmark when ATTACKING Crown's unit in their own territory — which makes thematic sense (Hafenmark knows the fortress layout) but is mechanically novel.

### MODE D — Edge Cases

**D1. [FINDING CONT-D-01 — P1]:** What is the contesting unit's "Discipline" in BG context?
PP-519 says the contesting unit "persists until Legionary Outward withdrawal or next Battle
loss." PP-514: Discipline loss cumulates within a season, resets at Year-End. A contesting
unit that was damaged in the initial Partial Battle (it took Discipline loss per PP-476
Partial margin) enters the contested state at reduced Discipline. Its next Battle starts
at this reduced Discipline. If Discipline reaches 0: unit is destroyed (PP-514: Formation
Break). Does a unit destroyed in a dislodgement Battle simply cease to exist in the
contested territory, ending the contested state? Yes — this is the expected behavior, but
not explicitly stated in PP-519.

**D2. Contested state + Accounting Discipline reset:**
PP-514: "Discipline resets at Year-End Accounting." A contesting unit that survived 3
seasons in contested state (accumulated Discipline from repeated Partial battles) resets
at Year-End. The unit enters Season 5 at full Discipline — refreshed for a new engagement.
This means Year-End is a strategic reset for contested situations: all units in contested
states return to full fighting capacity. Sieges cannot be maintained purely through
attrition; they reset annually.

**[FINDING CONT-D-02 — P2]:** Year-End Discipline reset makes multi-year contested
states persistent with no attrition toward resolution. A faction that wants to maintain a
contested state indefinitely (blocking Govern, preventing capital recovery) can do so at
no ongoing cost — their unit simply sits in the territory, refreshing at Year-End. The only
resolution mechanisms are: (a) Battle (dislodgement or conquest), (b) voluntary withdrawal
(Legionary Outward). There is no "contested state decays over time" mechanic. This may
be intentional (persistent occupation as a valid strategy) but creates a scenario where a
faction can permanently lock another faction's capital governance without ever winning the
territory.

**D3. [FINDING CONT-D-03 — P2]:** Multiple contested states and card economy.
Hafenmark needs to play Legionary to dislodge Crown from T8 AND defend T7/T10/T17 from
other threats. Hafenmark starts with 1 Legionary card. The contested state forces Hafenmark
to spend their single Legionary card on dislodgement — sacrificing any other military
action this season. For Military-weak factions (Hafenmark Mil 3, one Legionary), a single
contested capital state consumes the entire military budget. This is either a correct
design (contested capitals are existential crises for low-Military factions) or overly
punishing (a single Crown unit locks Hafenmark's entire military for the season).

**D4. Govern void rule interaction (PP-504) with contested state:**
Suppose Crown declares Govern T14 AND Battle vs Hafenmark T8 in Phase 2. Phase 4 Priority 2:
Crown attacks T8. If Crown wins T8 (territory captured), this doesn't affect T14. Crown's
Govern T14 still fires at Priority 3. If Crown loses T8 battle (territory not captured):
Crown Govern T14 still fires. PP-504 voids Domain Actions only for territories the losing
faction LOSES CONTROL OF. Crown doesn't lose T14 in any of these scenarios — Crown
governs T14 regardless of T8 outcome. Clean.

But: what if Varfell attacks T14 AND Crown attacks T8 in the same Phase 4? Priority 2 is
simultaneous for all Battles. If Varfell wins T14 (extremely unlikely given Fort 3, but
possible): Crown's Govern T14 (Priority 3) is voided per PP-504. Crown loses T14 at
Priority 2 → Crown Govern T14 at Priority 3 = void. Good — PP-504 fires correctly.

### MODE J — Cognitive Load

**J1. [FINDING CONT-J-01 — P2]:** Contested state tracking requires a physical marker
(contesting unit token in the territory). Standard territory tokens show only the controlling
faction. A second distinct token for the contesting force is needed. The territory card
would show: control token (Hafenmark) + contesting unit token (Crown). Players must track:
(a) which faction controls, (b) which faction is contesting, (c) contesting unit's current
Discipline. This is triple-layered information on one territory card. A dedicated
"Contested Territory" tracker card listing all contested territories and their state would
reduce table confusion.

### MODE L — Precedent / Cross-System

**L1. Contested territory and TC Territorial Seizure (Church):**
Church wants to seize T14 (under Crown control, contested by Varfell). PP-510: "Battle
trigger on Seizure success in contested territory." But the territory is ALREADY contested
(Varfell present). Church's Seizure success would add a third faction's claim — Church
Seizure Claim token + Varfell contesting unit + Crown control marker. Three factions
simultaneously relevant to one territory.

**[FINDING CONT-L-01 — P1]:** Three-faction territory state undefined. PP-510 addresses
Church Seizure firing a Battle (next season). PP-519 defines two-faction contested state.
If a territory is already contested (two factions) when Church achieves Seizure Success,
the subsequent Battle (PP-510) must involve three factions. This is exactly the three-way
Battle scenario (PP-503): sequential. But PP-503's sequence assumes two attackers vs one
defender. In a contested territory with a Seizure Claim:
- Who is the "defender" in the PP-510 Battle? Crown (controller) vs Church (Seizure claimant)?
- What happens to Varfell's contesting unit during the Church-Crown Battle?
- If Church wins: does Varfell's contesting unit persist in Church-controlled T14?
No rules address this combination.

---

## ═══════════════════════════════════════════════════════
## SCENARIO 4: POST-BATTLE RETREAT CHAIN REACTION
## Hafenmark loses T8 (capital). Retreat per PP-506. Nearest friendly
## territories: T7, T10, T17. All examined for chain reactions.
## ═══════════════════════════════════════════════════════

### Setup
Hafenmark: controls T7, T8★, T10, T17. Crown attacks T8 decisively (margin > 2).
Hafenmark unit retreats per PP-506.

### MODE A — Retreat Resolution

**A1. Adjacent friendly territories from T8:**
T8 adjacent: T7 (Hafenmark), T9 (Church), T10 (Hafenmark), T17 (Hafenmark).
Friendly: T7, T10, T17. Three valid retreat destinations.

PP-506: "Nearest friendly adjacent territory." If multiple adjacent friendly territories
exist: "nearest" is ambiguous — all adjacencies are equal (no distance metric in BG
adjacency graph; all adjacencies are one hop). No tiebreaker for retreat destination choice.

**[FINDING RET-A-01 — P1]:** Retreat destination when multiple adjacent friendly
territories exist: undefined. Does the retreating faction choose? Does some mechanical
priority apply (highest Fort? Lowest TCV? First alphabetically)?

If retreating faction chooses: they select strategically (e.g., T17 to threaten Church's
T9 adjacency, or T10 to shore up the northern border against Altonian invasion). This
is tactically rich but gives the defeated faction significant post-Battle agency.

If mechanical priority: automatic selection removes player anguish but may produce
counterintuitive retreats (unit retreating to a TCV-1 territory when a Fort-2 territory
is also adjacent).

**A2. Retreat to T10 (Spartfell, Fort 2, Hafenmark control):**
Hafenmark unit retreats to T10. T10 is adjacent to T8 (newly Crown-controlled) and T11
(Varfell). Varfell holds T11. Now T10 has a Hafenmark unit (retreated) AND is adjacent to
both a new Crown territory (T8) and Varfell (T11). If Crown pursues (next season Legionary
into T10): Hafenmark now defends T10 with Military 3 + Fort 2 = 5D (including retreating
unit) vs Crown 4D. Ob = Hafenmark Mil ÷ 2 = 2. Better defensive position than T8 (no fort).

**A3. Chain reaction: Crown takes T8, pursues to T7 same season:**
Crown has 1 Legionary card. Crown plays it to attack T8 (Phase 4 Priority 2). Crown wins T8.
Can Crown immediately pursue into T7 (adjacent) in the SAME season? Crown has no second
Legionary card. Standard March requires Legionary card. Crown cannot pursue T7 same season
with one Legionary card — they've expended it.

Unless: "Overextended" from the Feigned Retreat tactic card (BG §B.4): "On loss: opponent's
winning units are Overextended (−2D next season in same territory)." Does a clean victory
(not via Feigned Retreat) trigger Overextended? No — Overextended is only from Feigned
Retreat specifically. Crown's clean victory at T8 has no Overextended penalty.

PP-506 says defender retreats. Attacker occupies. No "free pursuit" mechanic exists.
Multi-territory offensive in one season requires multiple Legionary cards or Senate Market
purchase. Crown's default hand has 2× Legionary — if they used one for T8, they have one
more. Crown could attack T7 with the second Legionary card in the same Phase 4.

**[FINDING RET-A-02 — P2]:** Two-Legionary attack chains are possible and understated.
Crown starts with 2× Legionary. A faction with 2 Legionary cards can attack TWO territories
in the same Phase 4. Both Battles resolve at Priority 2 (Military), within-tier by Stability
order. If Crown attacks T8 AND T7 simultaneously: T8 Battle resolves first (say, Stability
tiebreak). Crown wins T8. Then T7 Battle fires — at the time T7 Battle resolves, Hafenmark's
unit from T8 may have already retreated to T7 (Retreat fires at Priority 2 resolution).

**[FINDING RET-A-03 — P1]:** Retreat timing within Phase 4 Priority 2. If Crown attacks
T8 AND T7 simultaneously (two Legionary cards), and T8 resolves first: the retreating
Hafenmark unit from T8 goes to T7. Now T7 has the retreating unit present when the T7
Battle resolves. Does the retreating unit participate in the T7 Battle? If yes: Hafenmark
effectively gets a reinforcement from their own retreat — the T8 unit bolsters T7's defense.
If no: the retreating unit arrives after T7 Battle resolves (timing ambiguity).

This matters enormously: Crown could be attacking a T7 that has 0 units (if Hafenmark
has no Legionary in T7 this season) or a T7 that now has a retreated unit from T8. The
retreat timing within Phase 4 Priority 2 determines whether Crown's two-front attack is
efficient or self-defeating.

### MODE D — Edge Cases

**D1. [FINDING RET-D-01 — P2]:** Encirclement and self-destruction. If Hafenmark loses
T8 and ALL adjacent territories are also lost (T7 captured by Varfell earlier this season,
T10 captured by some other action, T17 held by no Hafenmark unit and currently contested):
PP-506 says "If completely encircled with no retreat path: unit destroyed (Military −1)."

T17 Halvarshelm is Hafenmark territory — it IS a valid retreat destination even if contested
(PP-506: "retreat to non-attacker adjacent territory" when no friendly territory exists).
Wait — re-reading PP-506: Retreat priority:
1. Nearest friendly adjacent territory.
2. If no adjacent friendly: retreat to "non-attacker adjacent territory (contested)."
3. If completely encircled: unit destroyed.

T17 (Hafenmark-held) counts as friendly → retreat goes there first. Only if T17 is also
controlled by an enemy does option 2 apply. True encirclement of T8 requires all four
adjacencies (T7, T9, T10, T17) to be non-Hafenmark. T9 is Church — counts as non-attacker
non-friendly. So T9 would be a valid option-2 retreat target (move into Church-held T9 as
a contested state). This means Hafenmark's unit could retreat INTO Church territory and
create a contested state there.

**[FINDING RET-D-02 — P2]:** Retreat into an enemy-controlled adjacent territory (PP-506
option 2) creates a contested state IN THAT ENEMY'S TERRITORY. If Hafenmark retreats into
T9 (Church capital): Hafenmark unit is now contesting T9 Himmelenger. Church must now play
Legionary to dislodge Hafenmark. This is a mechanic that produces contested states in
unexpected locations — a retreating army ending up in the Church's cathedral city. This
seems design-intentional (desperate retreats create chaotic situations) but may surprise
players who expect retreating units to simply disappear.

**D2. Retreat destination selection for the retreating faction (question from RET-A-01):**
Examining precedent: BG unit decisions are generally in the controlling player's hands.
There's no automatic routing. Ruling implied by game design: **retreating faction chooses
retreat destination** from valid options. This is consistent with TTRPG mass battle Rout
rules (PP-rout) where the routing faction's player nominates a destination. Apply same
principle to BG.

**D3. [FINDING RET-D-03 — P2]:** Retreat and Ministry AP-tokens. If a faction retreats
into a territory containing a Ministry AP-token: the AP-token is not disturbed (NPC asset,
PP-488). However, the Ministry NPC AI Priority 3 ("If territory with AP-token is threatened
by Church Seizure") — does an enemy military unit constituting a "threat" to the AP-token
trigger Ministry Priority 3? A non-Church hostile unit in a Ministry-AP territory is not a
Church Seizure — Priority 3 doesn't fire. Ministry continues to operate normally.

---

## ═══════════════════════════════════════════════════════
## SCENARIO 5: CHURCH GRADUATED SEIZURE + FORT LEVEL (PP-509)
## New Ob formula: (7−CV) + Fort Level. Testing against real territories.
## ═══════════════════════════════════════════════════════

### MODE A — Updated Ob Table for All Territories (TC=75, Influence=6, Pool=11D)

| T# | Territory | CV (est) | Fort | Ob (7−CV+Fort) | Pool | P(OW) | P(Suc) | P(Fail) |
|----|-----------|----------|------|-----------------|------|-------|--------|---------|
| T1 | Valorsplatz | 4 | 2 | 5 | 11 | 0.247 | 0.221 | 0.296 |
| T2 | Kronmark | 3 | 1 | 5 | 11 | 0.247 | 0.221 | 0.296 |
| T3 | Lowenskyst | 3 | 3 | 7 | 11 | 0.029 | 0.070 | 0.753 |
| T4 | Grauwald | 2 | 0 | 5 | 11 | 0.247 | 0.221 | 0.296 |
| T5 | Feldmark | 3 | 0 | 4 | 11 | 0.467 | 0.236 | 0.119 |
| T6 | Stillhelm | 2 | 0 | 5 | 11 | 0.247 | 0.221 | 0.296 |
| T7 | Rendstad | 3 | 0 | 4 | 11 | 0.467 | 0.236 | 0.119 |
| T8 | Gransol | 3 | 1 | 5 | 11 | 0.247 | 0.221 | 0.296 |
| T9 | Himmelenger | 5 | 2 | 4 | — | — | — | — |
| T10 | Spartfell | 3 | 2 | 6 | 11 | 0.099 | 0.147 | 0.533 |
| T11 | Halvardshelm | 2 | 0 | 5 | 11 | 0.247 | 0.221 | 0.296 |
| T12 | Sigurdshelm | 2 | 1 | 6 | 11 | 0.099 | 0.147 | 0.533 |
| T13 | Oastad | 2 | 0 | 5 | 11 | 0.247 | 0.221 | 0.296 |
| T14 | Ehrenfeld | 3 | 3 | 7 | 11 | 0.029 | 0.070 | 0.753 |
| T17 | Halvarshelm | 2 | 0 | 5 | 11 | 0.247 | 0.221 | 0.296 |

Note: T9 (Church capital) cannot be seized by Church (Church controls it — no prominence
possible; PP-473 dead zone). T15/T16 excluded per existing rules.

CV estimates: starting territory CV values not explicitly listed in any fetched doc.
Using inferred values from geography (Church capital T9=5; border/southernmost lower).
These require confirmation.

**[FINDING SEI2-A-01 — P2]:** CV starting values are not stated in any fetched canonical
document. The TCV table exists; CV starting values do not. Church's seizure strategy
depends entirely on CV distribution — a territory at CV=2 vs CV=3 is the difference between
Ob=5 and Ob=4 (significant probability shift). Church needs a CV starting value table to
plan seizure strategy. Currently: the table above uses inferred CV values and may be wrong.

**A2. Fort 3 impact (PP-509):**
T3 Lowenskyst (Fort 3, CV=3): Ob = 4 + 3 = 7. Pool 11D. P(Fail) = 0.753.
T14 Ehrenfeld (Fort 3, CV=3): Ob = 4 + 3 = 7. Pool 11D. P(Fail) = 0.753.

The two Fort-3 territories are essentially impervious to Church Seizure at TC 75.
75% Stability drain rate per attempt. Church cannot sustain attacking T3 or T14 more than
2–3 seasons before Stability collapse. PP-509 correctly implements the intent of ED-355:
"physical fortifications defend against seizure."

**[FINDING SEI2-A-02 — P2]:** PP-509 Fort Level Ob cap (+3 max). At Fort 4 territories:
the contribution is +3 (capped), not +4. Fort 4 territory at CV=3: Ob = 4 + 3 = 7 (same
as Fort 3). The cap means Fort 4 provides no additional seizure resistance vs Fort 3.
This might be intentional (Fort 4 is already impervious at Ob=7) or an oversight (the
hardest fortresses should be hardest to seize). If intentional, correct as written. If not:
raise Fort 4 cap contribution to +4 (Ob=8 at CV=3 Fort 4). An Ob-8 seizure would require
net successes ≥ 8 against Pool 11 — roughly P(OW) = 0.001 (essentially impossible). This
is probably the right design for the scenario where Church wants to seize the primary
Altonian border fortress (T3 Lowenskyst). Recommend confirming cap.

**A3. Optimal seizure targets (Church maximizing CV gains):**
Highest P(OW) at TC=75: T5 Feldmark (P=0.467) and T7 Rendstad (P=0.467). Both Fort 0,
CV=3 (inferred). CV +1 on Overwhelming → CV 4. After 3 successful Overwhelmings on T5:
CV = 5 (max). Church then holds high-CV territory with lower future seizure difficulty
(CV rising means Ob drops — but Church Seizure Ob decreases as CV increases, meaning
Church makes high-CV territories EASIER to seize... wait.)

Re-reading: Ob = 7 − CV. CV=5 → Ob=2 (easiest). CV=3 → Ob=4. As CV rises, territory
becomes MORE amenable to Church Seizure. This is correct: higher CV = more pious = easier
for Church to assert authority.

**[FINDING SEI2-A-03 — P2]:** Church Seized territory becomes easier to seize again.
If Church seizes T5 (CV 3→4 from OW), T5's Ob drops from 4 to 3 on future attempts.
Church Seized and then LOST T5 (Battle outcome): the CV=4 is retained on the territory
(CV is a territory property, not Church's property). The next faction to control T5 faces:
Church Seizure Ob=3 (easier for Church to re-seize). Church losing a high-CV territory
is strategically costly but not permanently so — the territory's piety level remains
high, making reconquest easier. This creates a ratchet mechanic: once Church invests in
raising territory CV, it becomes progressively easier to re-seize even if militarily lost.

---

## ═══════════════════════════════════════════════════════
## CONSOLIDATED FINDINGS REGISTER — SIM-TERR-02
## ═══════════════════════════════════════════════════════

| ID | Sev | System | Description | Action |
|----|-----|--------|-------------|--------|
| AUD-01 | P1 | TCV | T9 Himmelenger TCV conflict: victory_arch=5 vs params=3 | Patch required |
| AUD-02 | P1 | TCV | T8 Gransol TCV conflict: victory_arch=3 vs params=4 | Patch required |
| CONT-A-02 | P1 | Contested | Capital contested state: near-permanent governance lock | Design note |
| CONT-A-03 | P1 | Contested | Dislodgement Battle role ambiguity (attacker/defender) | Patch required |
| CONT-L-01 | P1 | Contested | Three-faction territory state: Seizure Claim + contested unit + controller | ED required |
| RET-A-03 | P1 | Retreat | Retreat timing within Phase 4 Priority 2 (multi-attack turn) | Patch required |
| DT-D-01 | P1 | DT | Bilateral transfer priority — simultaneous Stability tie for both sides | Patch required |
| DT-D-02 | P1 | DT | Consent withdrawal between Phase 2 and Phase 4 undefined | Patch required |
| CB2-D-01 | P1 | CB | Diplomatic Token ownership ambiguity in PP-518 (placer vs host) | Patch required |
| AUD-03 | P2 | TCV | T17 named "Reinstadt" in victory_arch — should be "Halvarshelm" | Text fix |
| CB2-A-01 | P2 | CB | CB +2D meaningful but non-dominant at parity — calibrated correctly | Design note |
| CB2-A-02 | P2 | CB | CB accumulation meta-game: treaty (permanent) vs tactical (3-season) well-differentiated | Design note |
| CB2-D-02 | P2 | CB | Contesting faction initiating second Battle from contested position undefined | Patch required |
| CB2-D-03 | P2 | CB | Riskbreaker Priority 1 "success" undefined for PP-524 CB burn | Patch required |
| DT-A-01 | P2 | DT | Bilateral transfer can break Path prerequisites — design note | Design note |
| DT-A-02 | P2 | DT | 1-season TCV freeze correctly gates co-victory exploitation | Design note |
| DT-D-03 | P2 | DT | Diplomatic Token + Parliamentary Session vote simultaneously with Transfer | Design note |
| DT-D-04 | P2 | DT | Formal Crown Treaty + Diplomatic Transfer same season: legal combo | Design note |
| CONT-A-01 | P2 | Contested | Contested +1 Ob correctly degrades Govern — calibrated | Design note |
| CONT-D-01 | P2 | Contested | Contesting unit Discipline at 0 → destroyed, contested state ends | Patch (confirm) |
| CONT-D-02 | P2 | Contested | Year-End Discipline reset makes contested states persistent — no attrition decay | Design decision |
| CONT-D-03 | P2 | Contested | Single contested capital consumes entire Legionary budget for low-Mil factions | Design note |
| CONT-J-01 | P2 | Contested | Contested state needs dedicated territory tracker card | Infrastructure |
| RET-A-01 | P1 | Retreat | Retreat destination choice: undefined when multiple friendly adjacencies exist | Patch required |
| RET-A-02 | P2 | Retreat | Two-Legionary offensive chains understated — powerful but correct | Design note |
| RET-D-01 | P2 | Retreat | Encirclement retreat to enemy territory creates unexpected contested states | Design note |
| RET-D-02 | P2 | Retreat | Retreat into enemy territory (option 2) produces contested states in non-obvious locations | Design note |
| RET-D-03 | P2 | Retreat | Ministry AP-tokens not disrupted by retreating hostile units | Design note |
| SEI2-A-01 | P2 | Seizure | CV starting values not defined in any canonical document | ED required |
| SEI2-A-02 | P2 | Seizure | Fort 4 cap contribution (+3 max) — same Ob as Fort 3 | Confirm |
| SEI2-A-03 | P2 | Seizure | CV ratchet: seized then lost territory easier to re-seize — possibly intentional | Design note |

**P1 total: 9 | P2 total: 22**

---

## WHAT IS WORKING

- CB +2D calibration is correct: meaningful at fortified targets, non-dominant at parity.
- CB 3-season expiry vs permanent treaty CB creates a genuine meta-game (accumulation vs use).
- Diplomatic Transfer 1-season TCV freeze correctly prevents same-season co-victory
  exploitation.
- PP-504 (Domain Action void on territory loss) fires cleanly in all scenarios tested.
- PP-509 Fort Level addition to Seizure Ob creates correct impenetrability at T3/T14.
- CV ratchet mechanic (seized territory easier to re-seize after CV raised) is elegant.
- Contested state +1 Ob on Govern is correctly calibrated to degrade but not eliminate
  governance in contested territories.
- Retreat chain reaction (retreat into adjacent enemy territory) is functionally sound —
  desperate retreats produce appropriate chaos.
