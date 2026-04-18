## Balance Findings — Status Update
**BAL-04, BAL-05/06, BAL-08, BAL-09 (all P1):** Superseded by victory_v30.md redesign. Crown victory restructured (TCV ≥ 16 + political conditions, per victory_v30.md). Church primary restructured (TC 75 phase transition + seizure). Varfell Path B redesigned. TC dynamics recalibrated.
**BAL-10 (P2):** Varfell T13 (now T13 Oastad) dominant opening — still relevant for monitoring under new TCV system.
See victory_v30.md §10 for Monte Carlo win probability assessment.
[SIM-DEBT: Full faction-AI simulation needed to validate multi-faction interaction under new victory architecture.]

## Concurrent Zoom In — Ordering (ED-072 resolved 2026-04-03)
If multiple factions trigger Zoom In simultaneously: faction-turn Accounting sequence order applies.
First battle completes before second begins.


## ED-019 Resolution (PP-261) [FLAGGED FOR DESIGNER REVIEW]
Faction unique tactic cards (2 per faction, provisional):
| Faction | Tactic A | Tactic B |
|---------|----------|----------|
| Crown | Royal Prerogative: +2D one Mandate roll | Iron Decree: cancel one opposing Domain Action (1/campaign) |
| Church | Sanctuary: protect one NPC from targeting for 1 season | Inquisition: force one faction to reveal one hidden stat |
| Hafenmark | Trade Leverage: +1D all Wealth rolls for 1 season | Constitutional Check: reduce one Crown action Ob by 2 |
| Varfell | Intelligence Supremacy: learn one faction's full stat block | Patience Protocol: pass; bank +2D for any future roll |
[FLAGGED: these are placeholder designs. Full design required before BG compilation.]


## ED-056 Resolution (PP-268)
Zoom In TC win-delay exploit: if a player triggers Zoom In specifically to suspend Accounting when TC ≥ 75 (Church phase transition), the Accounting still checks victory conditions at suspension point before Zoom In resolves.
Rule: **Victory condition check fires at the moment the threshold is crossed, not at Accounting completion.**
Zoom In cannot retroactively prevent a threshold that was crossed before the interrupt was declared.


## ED-072 Resolution (PP-269)
Confirmed from params_board_game: concurrent Zoom In ordering resolved by PP-112 (faction-turn Accounting sequence). Faction that triggered the Zoom In resolves first; others queue in Mandate order (descending). ED-072 resolved — already in params.


## ED-080 Resolution (PP-270)
Baralta Conviction text (Amendment2): "Faith is not mediated — it is immediate, or it is nothing."
Mechanical effect: Baralta gains +1D on any roll made in defence of direct Church authority (unmediated from doctrine). Loses −1D on rolls requiring institutional compromise.
[FLAGGED: confirm wording and mechanical expression.]


## ED-081 Resolution (PP-271)
Vaynard Conviction text (Amendment2): "The strongest thread is the one that does not know it is being pulled."
Mechanical effect: Vaynard gains +1D on any Intel-based action where his involvement is not publicly known. −1D if his faction affiliation is openly declared before rolling.
[FLAGGED: confirm wording.]


## ED-083 Resolution (PP-272)
VTM 5 ability (choose Actualized dimension of one Co-Movement card): P-14 compliance confirmed. Amendment2 "allows pre-draw selection" = choosing which of the two card dimensions becomes the outcome. This is not card manipulation — it is outcome selection from the existing draw. P-14 (Co-Movement must be genuine) is satisfied because the card was drawn legitimately; VTM 5 only selects the dimension, not the card. ED-083 resolved.


## ED-085 Resolution (PP-273)
Reformed Settlement Church responses confirmed (three options):
1. **Resist:** Church contests the settlement. Mandate −1 but TC gain continues; Hafenmark gains Deed.
2. **Accommodate:** Church accepts. TC gain suspended for 1 season. Parliament Integrity +1.
3. **Ignore:** Church neither contests nor accepts. No mechanical effect; sets up future escalation. TC gain halved for 1 season.
[FLAGGED: confirm Mandate −1 for Resist and PI +1 for Accommodate.]


## ED-086 Resolution (PP-274)
BG Co-Movement Resolution Protocol (P-14 compliance):
1. Declare Thread order type.
2. Roll faction stat pool (TN 7, Ob per order type).
3. Apply degree result (Overwhelm/Success/Partial/Failure from BG degree table PP-249).
4. Draw Co-Movement card.
5. Apply Actualized dimension first, then Temporal dimension.
6. Apply any VTM/ability modifications to outcome selection (not card draw).
7. Record RS change and attention pool change.
All BG Thread operations follow this sequence. No shortcuts.


## ED-108 Resolution (PP-277) [FLAGGED FOR DESIGNER REVIEW]
Crown territory names (provisional): T2 = **Kronmark** (NW of Arcansheim), T5 = **Sudmarken** (SE border).
[FLAGGED: confirm names before map publication.]


## ED-109 through ED-113 Resolution (PP-278) [FLAGGED FOR DESIGNER REVIEW]
**ED-109 — Crown victory front-loaded:** Remove 1 pre-met deed from Crown starting conditions. Crown starts with 2 of 5 deeds met (not 3). Rebalances opening tempo.
**ED-110 — Church primary victory inaccessible:** Add fallback: if TC reaches 70 and Church holds 2+ territories, Church may declare Ecclesiastical Mandate victory (partial win, shared with one ally). Unblocks solo Church win path.
**ED-111 — Varfell Path B under-gated:** Require VTM ≥ 4 (not 3) to seize T6 via Path B. +1 VTM threshold gate.
**ED-112 — TC lock:** Hafenmark suppression capped at −1/season total (cannot be stacked via multiple actions). Church TC gain from T9 remains +1/season. Net: Church can advance TC by investing elsewhere.
**ED-113 — Varfell T6 opening dominance:** Add Fort 1 to T6 at game start (not Fort 0). Increases seizure Ob from 0-fort to Fort 1 resistance (+1D to defender).
[FLAGGED: all balance adjustments require playtesting confirmation.]


## BG Overwhelming Threshold — Final (PP-281 / PP-299)
Supersedes PP-179 (which incorrectly stated 'matches TTRPG').
BG Overwhelming = Ob+1 surplus (margin ≥ Ob+1 after ties → attacker wins).
BG Overwhelming floor: net ≥ 3 (PP-249 canonical — matches TTRPG PP-232 floor). Supersedes prior net ≥ 2 proposal.
ED-031 correct. PP-179 was documentation error. ED-142 resolved.


## ED-056 Resolution (PP-293) — Zoom In TC Win-Delay Exploit
Victory condition check fires at the moment a threshold is crossed, not at Accounting completion.
Zoom In cannot retroactively prevent a threshold crossed before the interrupt was declared.
[FLAGGED: confirm implementation in BG rules before compilation.]



## ED-072 Resolution (PP-294) — Concurrent Zoom In Ordering
Concurrent Zoom In order: faction that triggered the Zoom In resolves first; others queue
in Mandate order (descending). PP-112 confirmed. Already in params_board_game.
ED-072 resolved — no change needed.



## ED-080 Resolution (PP-295) — Baralta Conviction Text [FLAGGED]
"Faith is not mediated — it is lived. Anyone who tells you otherwise is selling something."
Mechanical effect: +1D when defending direct Church authority (unmediated from doctrine). −1D on institutional compromise rolls.
[FLAGGED: confirm wording and mechanical expression before NPC compilation.]



## ED-081 Resolution (PP-296) — Vaynard Conviction Text [FLAGGED]
"The strongest thread is the one others cannot see being pulled."
Mechanical effect: +1D on Intel actions where Varfell involvement is not publicly known. −1D if faction affiliation declared before rolling.
[FLAGGED: confirm wording before NPC compilation.]



## ED-083 Resolution (PP-297) — VTM 5 P-14 Compliance
VTM 5 ability (choose Actualized dimension of one Co-Movement card): P-14 compliant.
Amendment2 "pre-draw selection" = choosing which dimension becomes the outcome, not which card is drawn.
Card is drawn legitimately; VTM 5 selects the dimension only. P-14 satisfied. ED-083 resolved.



## ED-085 Resolution (PP-298) — Reformed Settlement Church Responses [FLAGGED]
Three Church responses confirmed:
1. Resist: Mandate −1; TC gain continues; Hafenmark gains Deed.
2. Accommodate: TC gain suspended 1 season; PI +1.
3. Ignore: TC gain halved 1 season; no other effect.
[FLAGGED: confirm Mandate −1 and PI +1 values before compilation.]



## ED-086 Resolution (PP-299) — BG Co-Movement Resolution Protocol
Protocol (P-14 compliance): 1) Declare order type. 2) Roll faction pool TN7. 3) Apply degree result.
4) Draw Co-Movement card. 5) Apply Actualized then Temporal dimension. 6) Apply VTM/ability to outcome selection.
7) Record RS and Attention changes. All BG Thread operations follow this sequence.



## ED-108 Resolution (PP-302) — Crown Territory Names [FLAGGED]
T2 = **Kronmark** (NW of Ehrenfeld, buffer territory). T5 = **Sudmarken** (SE border zone).
[FLAGGED: confirm names before map and BG board publication.]



## ED-109–113 Resolution (PP-303) — BG Balance Adjustments [FLAGGED]
**ED-109 Crown front-loaded:** Remove 1 pre-met deed. Crown starts with 2/5 (not 3). Rebalances opening.
**ED-110 Church primary inaccessible:** Fallback: if TC ≥ 70 + Church holds 2+ territories → Ecclesiastical Mandate (partial shared victory).
**ED-111 Varfell Path B under-gated:** Require VTM ≥ 4 (not 3) to seize T6 via Path B.
**ED-112 TC lock:** Hafenmark suppression capped at −1/season total (cannot stack). Church TC from T9 remains +1/season.
**ED-113 Varfell T6 dominance:** Add Fort 1 to T6 at game start (+1D to defender, raising seizure difficulty).
[FLAGGED: all balance adjustments require playtesting confirmation before publication.]



## ED-142 Resolution (PP-322) — BG Overwhelming Threshold [FLAGGED]
BG Overwhelming: net ≥ 2×Ob AND net ≥ 3 (PP-179 canonical + PP-232 floor). ED-031 superseded.
Ob 10 exception: Overwhelming unavailable; Partial requires net ≥ 5.
[FLAGGED: confirm 2×Ob canonical; confirm floor of 3 applies to BG before BG compilation.]


## BG Overwhelming — Final Ruling (PP-262)
[STRUCK — superseded by PP-249: BG Overwhelming = net ≥ 2×Ob AND net ≥ 3.]
Floor: net ≥ 2 (not 3 — TTRPG floor of 3 is personal-scale drama; BG abstraction warrants lower floor).
PP-179 ('matches TTRPG') was a documentation error. ED-031 (Ob+1) is correct.
