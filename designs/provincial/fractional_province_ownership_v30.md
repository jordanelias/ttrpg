<!-- [PROVISIONAL: ED-711 — PP-666 2026-04-19 new mechanical system, pending smoke-test before CANONICAL] -->
# Fractional Province Ownership (Split-Province Mechanic)

**Status:** PROVISIONAL — approved mechanical design 2026-04-19 (PP-666)
**Supersedes:** Binary province-transfer rule in `settlement_layer_v30 §5.1` ("When the Seat is captured, provincial control transfers")
**Affects:** `settlement_layer_v30 §1.3, §5.1`, `peninsular_strain_v30 §1` (PV/TCV), `faction_layer_v30 §2` (occupation), `victory_v30` (PV victory calculations)
**Canon compliance:** CK3 duchy-consolidation precedent, ROTK partial-province rebellion precedent

---

## §1 Problem

Current canon: capturing a Seat transfers provincial control entirely to the invader. This creates binary ownership — a province is either Hafenmark's or Varfell's, with no intermediate state.

User question: "If Hafenmark seizes a settlement from Varfell, is that province still Varfell?" Logically, the answer is *not entirely* — provincial identity must fracture to match the fractured control.

## §2 Solution: Province Fractionalization

A province with mixed settlement controllers becomes **fractional**. Its name, PV, and political identity divide.

### §2.1 Trigger

A province becomes **fractional** when:
- ≥ 1 settlement in the province is controlled by a faction that is NOT the nominal province controller, AND
- The provincial Seat is NOT controlled by that same faction (Seat controls provincial identity).

If the Seat changes hands, the province's nominal controller changes — it is not fractional, just transferred.

If the Seat is held but another settlement is not, the province fractionalizes.

### §2.2 Province Value (PV) Re-derivation

Each settlement now carries a fraction of the province's PV proportional to its local Prosperity within the province:

**Settlement PV share** = (settlement Prosperity / sum of all settlement Prosperities in province) × province base PV

A faction controlling a settlement holds that settlement's PV share regardless of which faction holds the provincial Seat.

**Province PV totals re-aggregate per faction at Accounting.** A province with base PV 4 and three settlements of Prosperity 3/2/1 distributes 2/1.33/0.67 PV to the controllers of those three settlements (rounded to 1 decimal). A faction controlling all three: gets 4.0 (the full province). A split 2-vs-1: gets 3.33 vs 0.67.

This replaces the current implicit binary (either full 4 PV or 0) with a graduated PV stake.

### §2.3 Greater / Lesser Naming

A fractional province is renamed by geographic plurality:

- **Greater [Province]** = the faction holding the Seat settlement. Retains original name in common parlance.
- **Lesser [Province]** = the faction(s) holding non-Seat settlements. Collectively referred to by directional qualifier.

**Directional qualifiers** (derived from settlement position within province):
- If non-Seat settlements cluster north of Seat: "Northern [Province]"
- South: "Southern [Province]"
- East: "Eastern [Province]"
- West: "Western [Province]"
- If non-contiguous and no clear direction: "Outer [Province]"

**Example:** Hafenmark seizes S-017 Gransol Market Quarter from Varfell-held province T8 Gransol (hypothetical). Province fractionalizes. Varfell retains S-015 Gransol Parliament (Seat) + S-016 Gransol Harbor → "Greater Gransol." Hafenmark holds S-017 → "Eastern Gransol" (assuming Market Quarter is east of Seat).

### §2.4 Consolidation Threshold (CK3 Precedent)

A faction that holds ≥ 75% of a province's PV (weighted by settlement Prosperity share) may declare **Consolidation** as a Domain Action:

**Consolidation Action:**
- **Cost:** Influence pool vs Ob = remaining non-faction-held PV share × 2 (round up).
- **Effect:** Province unifies under this faction. All non-faction-held settlements either:
  - **Submit:** settlement transfers to consolidating faction. Order −2 in that settlement. No battle.
  - **Resist:** settlement triggers mandatory siege or assault next season.
- **Target choice:** non-faction-held settlement's current controller chooses Submit or Resist within 1 season. Default on non-response: Resist.

Consolidation formalizes what has *already* effectively happened (75%+ control) and ends the fractional state.

Below 75% held, no Consolidation is available — the province stays fractional indefinitely.

### §2.5 Effects of Fractional State

On Accord, governance, and mechanics:

| Mechanic | Effect of Fractional State |
|-|-|
| Province Accord | Recalculated per `settlement_layer §1.3` (floor-average of Order across all settlements). Fractional state tends to produce mixed Order → low Accord. |
| PT track | PT applies per-settlement. Province PT = floor-average. Fractional state → mixed PT. |
| Domain Actions | The faction holding the Seat issues province-level Domain Actions. Non-Seat-holders issue only settlement-level actions within settlements they hold. |
| Calamity radiation | Applies to whole province regardless of fractional state (radiation does not care about political boundaries). |
| Military movement | Armies move along settlement adjacency graph (per `settlement_adjacency_v30`). Settlement controllers determine which edges are friendly/hostile. |
| Taxation / Wealth income | Each faction taxes the settlements it controls. Province-level tax bonuses (Trade Network, Mine Income) scale by PV share. |
| Victory PV count | Each faction's PV total includes fractional shares. Universal Victory Condition (Peninsular Sovereignty) re-scored with fractional PVs. |

### §2.6 Resistance and Collapse of Fractional States

Fractional provinces are politically unstable. At Accounting, each fractional province rolls a **Fragmentation Check**:

- **Pool:** Seat-holding faction's Influence
- **Ob:** 2 + (number of non-Seat-held settlements)

Outcomes:
- **Overwhelming:** Province stabilizes as fractional for 4 seasons (no further Fragmentation Check during that window).
- **Success:** Province stays fractional. No change.
- **Partial:** A random non-Seat-held settlement's Order drops −1.
- **Failure:** A non-Seat-held settlement's controller may invoke **Secession**: the settlement becomes a de facto independent subnational holding. The original province controller loses that settlement's PV share permanently until reconquest.

Secession creates a persistent fracture — the settlement is neither "the Seat-holder's" nor "the invader's" but effectively a client or independent holding. This is the RM-settlement-emergence pathway already in `settlement_layer §6.2 Stage 2`.

**Secession candidate restriction (PP-TBD):** Secession candidates are limited to settlements controlled by a national faction (Crown, Hafenmark, Varfell, Church, Löwenritter, Guilds, Schoenland). Settlements already held by a subnational faction (RM, Wardens) or marked Uncontrolled are NOT valid Secession candidates. If all non-Seat alien settlements are subnational, the Failure outcome produces no Secession — treat as Partial instead (Order drop).

---

## §3 Worked Example

T8 Gransol (Hafenmark, base PV 4, three settlements: Parliament P=3, Harbor P=2, Market P=1, sum=6).

**Starting state:** Hafenmark controls all three. Hafenmark holds full PV 4.0 (3/6 × 4 + 2/6 × 4 + 1/6 × 4 = 2.0 + 1.33 + 0.67 = 4.0).

**Event:** Varfell assault captures S-017 Gransol Market Quarter (Prosperity 1) without taking Seat.

**Fractional state:**
- Hafenmark retains Parliament + Harbor → "Greater Gransol" → PV 2.0 + 1.33 = 3.33
- Varfell holds Market → "Eastern Gransol" → PV 0.67
- Province is now fractional.

**Consolidation path:** Hafenmark holds 3.33/4.0 = 83% PV share. Above 75% threshold. Hafenmark may declare Consolidation.
- Influence vs Ob = (0.67 × 2) = 1.33 → round up to Ob 2.
- Varfell (Market controller) chooses Submit or Resist.
- Submit: Market transfers back to Hafenmark at Order −2. Province unifies.
- Resist: Next season, Hafenmark must Assault S-017. Mass battle at settlement scale per `settlement_adjacency_v30`.

**Fragmentation Check each Accounting until consolidated:**
- Pool: Hafenmark Influence (say 5).
- Ob: 2 + 1 (one non-Seat-held settlement) = 3.
- Roll 5d10 vs Ob 3. Roughly Success rate.
- Overwhelming: fractional state holds 4 seasons.
- Failure: Varfell may declare Secession of Eastern Gransol — permanent loss for Hafenmark.

---

## §4 Implementation (Videogame)

- Strategic map displays fractional provinces with split color regions (Greater Gransol = Hafenmark color on Seat + Harbor; Eastern Gransol = Varfell color on Market).
- Tooltip shows PV breakdown per faction per province.
- Victory progress UI displays fractional PV accumulation.
- Consolidation is a Domain Action offered in the UI when PV threshold is met.

---

## §5 Open Items

- **PV share rounding:** currently 2-decimal. Consider integer-only (round fractional to nearest whole) for simplicity. Flag for smoke-test.
- **Multiple non-Seat controllers:** if three factions each hold one non-Seat settlement, Fragmentation Check multiplies Ob. Current spec: +1 Ob per additional non-Seat controller. Needs balance verification.
- **Settlement-level Casus Belli:** when Hafenmark seizes Varfell's Market settlement, does Varfell gain Casus Belli against Hafenmark for the whole province or just the settlement? Current spec: Casus Belli at settlement scope (per `faction_layer §3.5` extension — one Casus Belli per settlement transferred).
