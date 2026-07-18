<!-- [PROVISIONAL: ED-712 — PP-666 2026-04-19 new mechanical system, pending smoke-test before CANONICAL] -->
# Generalized Faction Succession Split & Emergence Trajectories
## Status: CANONICAL

**Status:** PROVISIONAL — approved mechanical design 2026-04-19 (PP-666)
**Supersedes:** Baralta-specific succession mechanics in `baralta_crown_claim_v30` are now a special case of the generalized Succession Contest
**Extends:** `faction_layer_v30 §1.5` Faction Collapse Exit Procedure, `settlement_layer_v30 §6.2 Faction Emergence`, `settlement_layer_v30 §6.3 Faction Collapse`, `baralta_crown_claim_v30 §2 Crown Succession Contest`
**Affects:** `faction_layer_v30`, `settlement_layer_v30`, `faction_politics_v30` (rank ladders, Inner Circle), `npc_behavior_v30` (arc state machines)
**Canon compliance:** P-15 (persistence at cultural layer), historical-precedents (succession wars)

---

## §1 Problem

Current canon:
- Faction collapse dissolves the faction or contracts it to city-state (handled by `faction_layer §1.5` + `settlement_layer §6.3`).
- Crown succession is specifically modeled (`baralta_crown_claim_v30`) because Crown has unique Baralta Claim + Löwenritter Coup paths.
- Other faction successions are NOT modeled — if Vaynard falls, Varfell currently follows generic collapse rules (contract to city-state).

User request: generalize succession contests so ALL factions can split between competing successors on leader loss.

## §2 Design: Universal Succession Contest Framework

When a faction leader is eliminated (killed, captured without ransom paid within 2 seasons, deposed, or permanently incapacitated), a **Succession Contest** opens at next Accounting UNLESS the faction has a canonical sole heir with Disposition ≥ +3 to faction apparatus.

### §2.1 Trigger Matrix

| Leader Status | Sole Heir Exists? | Outcome |
|-|-|-|
| Alive and in power | — | No contest. |
| Eliminated (killed/captured/deposed) | Yes, Disposition ≥ +3, Standing ≥ 4 | **Smooth succession.** Heir inherits. Faction Stability −1, no contest. |
| Eliminated | Yes, Disposition < +3 OR Standing < 4 | **Contested succession.** Contest opens. |
| Eliminated | No heir | **Contested succession.** Contest opens. |
| Eliminated | Multiple claimants of comparable Standing | **Contested succession** (mandatory regardless of Disposition). |

### §2.2 Contest Mechanics (Generalized from Baralta Spec)

The contest opens at next Accounting. All contenders stake claims. A contender must have at least one of:
- Rank in the faction's Inner Circle (`faction_politics_v30 §1.Nd`) with Standing ≥ 3
- Blood claim (named canonical heir per `npc_character_analyses_v30`)
- Institutional claim (holds a ministerial / committee / dicastery / council position per `faction_politics §7`)
- External backing (another faction's Diplomat action declaring support — costs Diplomatic Token)

**Contender strength** (deterministic; no roll) per claim type:

| Contender Type | Strength |
|-|-|
| Blood heir | Mandate + Influence |
| Institutional candidate | Influence + faction's rank-specific stat (Crown=Mandate, Hafenmark=Influence, Church=Influence, Varfell=Intelligence) |
| External-backed candidate | Diplomatic backer's Influence + own Standing |

**Resolution (two-stage; ED-865/874 resolver, FSS-1 2026-05-30).** The succession answers two *independent* questions — **who leads** and **whether the realm fragments** — so it resolves in two stages rather than collapsing both onto one roll-margin (the prior "highest net successes; split if margin < 2" conflated them, letting dice variance alone decide fragmentation — see §2.3 rationale).

- **Stage 1 — Who leads (contested resolver).** Between the two highest-strength contenders, resolve M = strength(top1) − strength(top2) via the deterministic+stochastic resolver (`params/factions/stats_1_7_scale.md §Domain Action Resolution`). Success/Overwhelming → top1 leads; Failure → the runner-up (top2) takes the lead instead (a weaker claimant *can* prevail, but the FLOOR/CAP keep it a tail, not a coin-flip). Multi-contender fields resolve pairwise from the top down. Tie in strength: faction's dominant stat decides which is "top1" for the roll (Military→military candidate, Mandate→political candidate, etc.).
- **Stage 2 — Whether it splits (deterministic strength gap G = strength(top1) − strength(top2)).** See §2.3.

### §2.3 Outcomes

Outcomes are keyed to the **deterministic strength gap G = strength(top1) − strength(top2)** (Stage 2), with the Stage-1 roll degree as a bounded tail. **Rationale:** historically, succession *fragmentation* tracks the balance of power among claimants — near-equal claimants partition the realm (Carolingian *divisio*, the Diadochi, contested Ottoman successions), a clearly dominant claimant consolidates it. Fragmentation should therefore follow the strategic gap, not raw dice variance; the prior "split if roll-margin < 2" let a one-success swing fragment a realm at ~50% of all near-peer successions regardless of the actual power balance.

**G ≥ 3 — decisive dominance → UNIFIED.**
- The Stage-1 leader becomes faction leader; runner-up submits. Faction continues unified. Stability −1, Mandate −1 (legitimacy turnover).
- *Dice tail:* a Stage-1 **Failure** by the leader → fractious Regency this Accounting instead (the dominant claimant stumbled publicly).

**G = 2 — dominant but contested → UNIFIED, fractious.**
- Leader inherits unified. Runner-up Disposition check: Disposition ≥ 0 → accepts (unified); below 0 → **splits** (see §2.4).
- Stability −1, Mandate −1.

**G ≤ 1 — near-peer claimants → SPLIT.**
- Faction **splits** (§2.4). The Stage-1 leader holds the formal faction name and ~60% of assets; the runner-up takes a faction-splinter with ~40%.
- *Dice tail:* a Stage-1 **Overwhelming** by the leader → the realm holds UNIFIED instead (a decisive personal victory consolidates an otherwise even contest).

**No qualifying contender (no contender meets a §2.2 claim basis, or all candidates' strength is 0):**
- Regency. Faction operates under NPC council governance. No leader stat bonuses. Faction may attempt another contest at next Accounting.
- If 3 consecutive Accountings produce no winner: faction collapses per `faction_layer §1.5`.

*(Ob 3 / net-success counting is retired for the succession fork: Stage 1 uses the resolver's four-degree ladder; Stage 2 uses the deterministic gap. The contest is decided by claimant strength with dice as a tail, not by a small-pool success-count margin.)*

### §2.4 Faction Split Mechanics

When a faction splits, the asset division:

| Asset | Split |
|-|-|
| Provinces | Geographic split. Winner takes faction's historical capital province + adjacent provinces. Splinter takes remaining provinces. Concretely: winner holds the capital Seat; each contested non-capital province goes to the nearer contender (proximity measured through settlement adjacency graph). |
| Settlements | Follow province unless a settlement's governor has Disposition ≥ +3 toward a specific contender — that settlement follows the contender regardless of province assignment. |
| Mandate | Winner: 60% (round down). Splinter: 40% (round down). Remainder burns (political legitimacy lost in succession crisis). |
| Influence | Winner: 60% (round down). Splinter: 40% (round down). Remainder lost (institutional capacity fragmented in succession crisis). Follows same split ratio as Mandate. |
| Wealth | Winner takes 70% (round down). Splinter takes 30% (round down). |
| Military units | Each unit rolls Loyalty check: Loyalty = (Commander Disposition toward contender) + (unit Discipline). Higher-Loyalty contender wins unit. Ties: unit disbands. |
| Stability | Winner: current − 1. Splinter: 2 (new entity always starts fragile). |
| Rank ladder NPCs | Each Inner Circle NPC chooses based on their Disposition. Non-Inner-Circle NPCs default to the contender whose province they're located in. |
| Faction name | Winner retains original. Splinter renames (typically "[Leader] Faction" or geographic-descriptor: e.g., "Southern Varfell," "Uln's Varfell"). |

### §2.5 Split Persistence

A splinter faction begins with:
- Partial faction sheet (as per `faction_layer §1.5 Step 4` reconstitution — 50% of frozen parent values, or as allocated per §2.4).
- Stability 2 (fragile).
- Victory conditions of the parent faction available but reset (no progress inherited).
- Ability to pursue Stage 2→5 emergence per `settlement_layer §6.2` to re-consolidate.

Splinters may:
- Re-merge with parent via treaty (`faction_layer §3` — requires both at Mandate ≥ 3).
- Pursue independent victory.
- Be absorbed by a third faction via conquest or submission.
- Collapse per `faction_layer §1.5` standard rules.

---

## §3 Worked Example: Vaynard Falls

Duke Magnus Vaynard (Varfell leader) is killed in mass battle, Season 12.

**Contender assessment at next Accounting:**

| Contender | Claim Type | Disposition | Standing | Pool |
|-|-|-|-|-|
| Maret Uln | Blood heir (canonical per `npc_character_analyses §2`) | +2 toward Varfell apparatus | 4 | Mandate 3 + Influence 4 = 7 |
| Tribune Captain (NPC officer) | Institutional claim (senior Tribune) | +4 toward apparatus | 3 | Influence 4 + Intelligence 5 = 9 |
| RM-backed candidate | External backing (Yrsa Vossen declares support — if RM emerged) | n/a | 2 | RM Influence 3 + Standing 2 = 5 |

Rolls (hypothetical):
- Maret Uln: 7d10 vs Ob 3 → 3 net successes (Success).
- Tribune Captain: 9d10 vs Ob 3 → 4 net successes (Success).
- RM candidate: 5d10 vs Ob 3 → 1 net success (Partial).

Under FSS-1 (2026-05-30): strengths are Tribune Captain 9 (Influence 4 + Intelligence 5) vs Maret Uln 7 (Mandate 3 + Influence 4), so **gap G = 2** — *dominant but contested*. Stage 1 (resolver, M = 9 − 7 = +2) → Tribune Captain leads. Stage 2 (G = 2) → **UNIFIED but fractious**, pending Uln's Disposition check: Uln at Disposition +2 toward the apparatus (≥ 0) → **accepts; Varfell stays unified** under the Tribune Captain. *(Had Uln's Disposition been below 0, the realm would split per §2.4 — the example below illustrates the split asset-division for that branch.)*

**Asset split:**
- Tribune Captain takes Varfell historical capital (Sigurdshelm T12 + Oastad T13). Name retained: Varfell.
- Maret Uln takes splinter. Takes Halvardshelm T11 + Grauwald T4 (geographically nearer her power base). Name: "Uln's Varfell" or by direction: "Eastern Varfell."
- Mandate: Varfell (Tribune) 60% of Vaynard's 5 = 3. Eastern Varfell (Uln) 40% = 2.
- Wealth: Varfell 70% of 4 = 2 (rounded down). Eastern Varfell 30% = 1.
- Military units each Loyalty-check per commander Disposition.
- RM candidate's 1 net success partial: RM gets a one-season Ob −1 on all actions against either Varfell splinter (momentum of political moment).

Outcome: Varfell is now two factions. Both pursue Peninsular Sovereignty independently. They may merge again if either reaches Mandate 3+ AND offers treaty of reunification. RM's partial success gave them a transient political advantage.

---

## §4 RM Emergence Trajectory (Formalization of Existing Stage 2→5 Pathway)

User asked whether RM can emerge from populist movement → subfaction → settlement governance → faction. Per `settlement_layer §6.2`, this pathway is already canonical:

- **Stage 1 Cell:** RM exists as Presence markers (no settlements).
- **Stage 2 Organization:** RM captures one settlement (via `peninsular_strain §2.5` RM exception or Secession per `fractional_province_ownership §2.6`).
- **Stage 3 Movement:** RM controls 2+ settlements, cross-settlement coordination, partial faction sheet.
- **Stage 4 Faction:** RM controls 4+ settlements across 2+ provinces OR holds 1+ provincial Seat via Cultural Uprising (`victory §3.5 Phase 2`). Full faction sheet at this point.
- **Stage 5 Hegemon:** RM controls 2+ provinces. Universal Victory applies.

**New clarification (this ED):** RM's emergence can now formally fire per-settlement rather than requiring the province-scale Cultural Uprising. If a settlement's Order = 0 (not merely ≤ 1) AND PT ≤ 1 AND local Disposition toward Yrsa Vossen is ≥ +3, RM may declare **Settlement Emergence** — taking governance of that settlement without firing Phase 2 Uprising. This gives RM a gradual emergence path instead of an all-or-nothing Phase 2 gate. Order = 0 is a hard threshold — Order 1 settlements are degraded but still governed; Order 0 represents complete governance collapse, which is the prerequisite for RM's alternative governance to fill the vacuum.

**Threshold:** Settlement Emergence may fire at most once per province per 4 seasons. Prevents RM explosive emergence across whole peninsula.

---

## §5 Implementation (Videogame)

- **Succession Contest UI:** On leader elimination, a contest scene opens. Contenders are named. Player selects backing. Roll resolves. Results visible.
- **Split display:** When faction splits, the second faction appears on the strategic map with its own color palette. UI shows "Varfell" and "Eastern Varfell" as distinct.
- **Re-merger:** Available as a Treaty action per `faction_layer §3`.

---

## §6 Open Items

- **Player-led contender:** If the player character is a contender, the contest becomes a player-action opportunity (rally support via NPC scenes in the 2-season window before Accounting). Specific mechanics deferred — scene-layer scope.
- **Simultaneous succession:** if two factions lose leaders in same season, order of resolution matters (winner of one contest may affect the other's diplomatic backing). Current spec: resolve in descending pre-loss Mandate order.
- **RM Settlement Emergence 4-season cooldown:** flagged for smoke-test balance. Too slow may let suppression win; too fast may let RM cascade.
- **Baralta Crown Claim relationship:** this ED's generalized Succession Contest subsumes `baralta_crown_claim_v30 §2`. Baralta's specific Deed-claim and Consecration Crisis remain as Crown-specific modifiers on top of the generic framework.
