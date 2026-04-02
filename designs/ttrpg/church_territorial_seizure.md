# CHURCH TERRITORIAL SEIZURE — Theocracy Counter 80 Threshold Event
## Date: 2026-03-25 (Session 5)
## Status: Designed — approved
## Integrates with: G-050 (event deck, Theocracy Counter 80 threshold), Church faction card, Löwenritter coup triggers

---

## Trigger
Theocracy Counter reaches 80 at Accounting.

## Eligible Territories
Every territory where Church Mandate > Crown Mandate at the moment Theocracy Counter hits 80.

## Procedure
The Church rolls to seize each eligible territory. One roll per territory, resolved sequentially (Church player or artificial intelligence chooses order of attempts).

**Roll:** Church Influence vs Ob set by territory type.

| Territory Type | Base Ob | Examples |
|----------------|---------|----------|
| Capital | 5 | Valorsplatz |
| Ducal seat | 4 | Hafenstadt |
| Major city | 3 | Sternhaven, Himmelstift |
| Standard | 2 | All others |

**Modifiers (cumulative):**

| Condition | Ob Modifier |
|-----------|-------------|
| Church Fortification present (Templar garrison) | -1 |
| Löwenritter units present | +1 |
| Territory Prosperity >= 6 (wealthy populations resist upheaval) | +1 |
| Territory has Einhir cultural presence (Korntal, Sudwald) | +1 |
| Previous failed seizure attempt on this territory | +1 per attempt |

## Results Per Territory

| Degree | Outcome |
|--------|---------|
| Overwhelming | Church seizes control. Crown Mandate -2 in territory. Church Mandate +1. Population supports transition. |
| Success | Church seizes control. Crown Mandate -1 in territory. Contested — Church Stability check Ob 1 next season (consolidation). |
| Partial | No control change. Church Mandate +1, Crown Mandate -1. Civil unrest: all orders +1 Ob in this territory next season. |
| Failure | Uprising fails. Church Mandate -1 in territory. Crown Mandate +1 (rally effect). Theocracy Counter -2 globally (overreach visible). |

## Systemic Consequences

**Crown impact:** Each territory seized forces a Crown Stability check. Ob = total territories seized this season (cumulative). Three territories seized = Ob 3 Stability check — potential cascade.

**Löwenritter trigger:** If Church seizes ANY Crown-controlled territory, Löwenritter coup trigger #3 is met. Ehrenwall's response depends on whether the Crown can retake the territory. If the Crown fails to respond within 1 season, Löwenritter begins coup preparations.

**Governance:** Seized territories governed under Church Institutional Tendency (expand Piety, suppress heresy, accumulate civil authority). Church framework modifier applies: doctrine-aligned Domain Actions -1 Ob; contradictory actions +1 Ob.

**Ongoing seizure:** While Theocracy Counter remains >= 80, the Church may attempt seizure of additional eligible territories in subsequent seasons using the same procedure. Previous failures on the same territory add +1 Ob per attempt.

## Counter-Play

| Counter | Faction | Mechanic |
|---------|---------|----------|
| Govern to raise Crown Mandate | Crown | Removes territory from eligibility (Crown Mandate >= Church Mandate) |
| Martial Law | Löwenritter | +1 Ob to seizure in that territory |
| Sovereign Authority Doctrine | Hafenmark | Theocracy Counter -2 or -3 — may drop below 80 threshold |
| Influence to shift Mandate | Any | Changes eligibility territory by territory |
| Military recapture | Crown/Löwenritter | March + Battle to retake seized territory (standard military procedure) |
| Economic pressure | Guilds | Economic Leverage in seized territory: Church Wealth -1, complicating governance |

## Co-Movement
The Theocracy Counter 80 seizure event draws a Co-Movement Card (mass institutional upheaval disturbs configurational environment per P-01). Additionally, each individual territory seized draws a separate Co-Movement Card — a successful multi-territory seizure generates significant Thread consequences.

## Canon Compliance
- **P-01:** Co-Movement Cards per seizure enforce inseparability.
- **P-07:** Seizure is a Calamity-class rendered-side event.
- **P-10:** The Church's theological certainty IS epistemic seduction — the seizure is the institutional expression of perceptual capture.
- **P-14:** Thread consequences of mass political upheaval expressed through Co-Movement deck.
