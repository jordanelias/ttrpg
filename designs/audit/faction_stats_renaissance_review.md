# Faction Stats vs Renaissance Political Infrastructure — Review
**Date:** 2026-04-28 | **Requested by:** Jordan | **Context:** Should Intelligence return?

---

## Current 5-Stat Lineup

| Stat | Range | Renaissance Analogue | Load-Bearing? |
|---|---|---|---|
| Mandate | 0–7 | Political legitimacy — papal bulls, imperial investiture, dynastic claims, constitutional authority | Yes — Wars of the Roses, Avignon papacy, Investiture Contest |
| Influence | 1–7 | Diplomatic reach — patronage networks, alliances, court politics, soft power | Yes — Medici banking diplomacy, Venetian diplomatic service, balance-of-power system |
| Wealth | 1–7 | Economic resources — trade revenue, taxation, treasury, mercenary funding | Yes — condottieri required payment, wars won by treasuries, Florentine banking |
| Military | 1–7 | Armed forces — standing armies, fortification networks, martial capacity | Obviously |
| Stability | 0–7 | Internal cohesion — succession clarity, factional unity, resistance to coups | Yes — Pazzi conspiracy, Visconti-Sforza succession, Borgia papal instability |

**Assessment:** All five map cleanly to load-bearing Renaissance dynamics. Nothing here is fantasy imposition. The set covers governance (Mandate), diplomacy (Influence), economy (Wealth), force (Military), and cohesion (Stability).

---

## What's Missing: Intelligence

### The Renaissance case

Renaissance intelligence was institutional, not just personal:

- **Venice's Council of Ten** — the most sophisticated pre-modern intelligence apparatus. Maintained agents, informants, and cryptographers across Europe and the Ottoman Empire. Venice survived for centuries with the smallest territory among the major Italian powers. Intelligence superiority was arguably their primary strategic asset.
- **Papal intelligence** — nuncios served dual diplomatic/intelligence roles. The Inquisition functioned partly as an information network.
- **Florentine intelligence** — Machiavelli himself served as Secretary of the Second Chancery, effectively a diplomatic intelligence officer. The Medici banking network was an intelligence network.
- **Information asymmetry decided wars** — knowing enemy troop dispositions, financial state, alliance negotiations, and internal politics was decisive. The fall of Constantinople was partly an intelligence failure.

### The current mechanical problem

When Intelligence was struck, two things broke:

1. **Spy Ob formula is dead.** `floor(target Intel / 2) + 1` references a non-existent stat. Currently Spy has no valid defensive Ob. This is a live bug in the design docs.

2. **No faction-level intelligence differentiation.** Investigate/Intel is flat Ob 2 for everyone. Venice and Milan have identical espionage capability. This contradicts the historical record where intelligence capacity varied enormously between states.

3. **Varfell lost its identity axis.** Starting stats are 4/4/4/4/4 — completely flat. Before Intelligence, Varfell was differentiated as the information-superiority faction (2× Tribune cards, Intelligence Hegemony victory path). Without the stat, Varfell's only differentiation is geographic (mountains) and card composition — but the cards' effectiveness is undermined by flat Ob.

### What fieldwork Investigation + VTM replaced

The strike rationale was: intelligence gathering is personal-scale (individual agents), not institutional. VTM captures Varfell's specific advantage.

This is *partially* right. Individual spying IS personal-scale. But:

- **Institutional intelligence capacity** (how good is your spy network? how hard are you to spy on?) is a faction-level property. Venice didn't have better individual spies — they had a better system.
- **VTM is Varfell-only.** Other factions have no intelligence progression mechanism at all. Church can build Inquisition infrastructure (Attention Pool), but Crown and Hafenmark have nothing.
- **Fieldwork Investigation** is about the Southernmost, not inter-faction espionage. It's the wrong system for "what does Crown know about Varfell's military?"

---

## Recommendation: Restore Intelligence (1–7)

### Mechanical roles

| Role | Formula | Renaissance Precedent |
|---|---|---|
| **Defensive intelligence** (counter-espionage) | Spy Ob = floor(target Intel / 2) + 1 | Already written, currently broken |
| **Offensive intelligence quality** | Investigate/Intel pool = Intel (not flat Influence) | Venice's superior spy network |
| **Counter-espionage detection** | At Intel ≥ 4: on enemy Spy attempt in your territory, roll Intel vs Ob 3. Success = you learn the spy action occurred (not its result) | Council of Ten's counter-intelligence |
| **Strategic fog** | Without successful Intel action, enemy faction stats are hidden. Intel reveals them. | Information asymmetry was THE strategic variable |

### Starting values

| Faction | Intel | Rationale |
|---|---|---|
| Crown | 3 | Royal court has some intelligence capacity but not a priority |
| Church | 4 | Inquisition + nuncio network |
| Hafenmark | 3 | Merchant intelligence (trade routes = information routes), but not institutionalized |
| Varfell | 5 | Tribune-heavy hand, Intelligence Hegemony path, Vaynard's personal information network |
| Löwenritter | 2 | Military order, minimal intelligence infrastructure |
| Guilds | 4 | Trade networks provide intelligence |

### What this fixes

1. **Spy Ob formula works again.** No design doc bugs.
2. **Varfell has a stat identity.** Intel 5 differentiates them from the 4/4/4/4/4 flatline.
3. **Path A re-gate resolves naturally.** "Intelligence ≥ 4" → already achievable for Varfell (start 5), but other factions would need to invest to reach it. Keeps the path thematically coherent.
4. **Strategic fog creates meaningful decisions.** "Do I spend my Tribune on Intel to reveal Crown's Military before I March, or save it for Spy to learn their diplomatic intentions?" — this is a real Renaissance decision.
5. **6 stats, 6 card types.** Tribune = Intelligence. Legionary = Military. Consul = Wealth. Senator = Influence/Mandate. Pontifex = special (Church/Thread). Balanced.

### N-tier assessment

- **Dynamic modeled:** Information asymmetry as institutional strategic resource.
- **Already covered?** Only at personal scale (fieldwork). Faction-level gap.
- **Different player situations?** Yes — invest in Intel vs Military is a real strategic axis.
- **Load-bearing historically?** Extremely. Venice survived on intelligence superiority.
- **Abstractable through existing mechanics?** No — Influence covers diplomatic soft power, not espionage. Different domains.

### What's NOT recommended

- Intelligence as a per-territory stat (too granular)
- Intelligence as a track like VTM (too narrow — should be universal)
- Merging Intelligence into Influence (different dynamics — diplomacy ≠ espionage)

---

## Other Gaps Considered

| Dynamic | Current Coverage | Missing? |
|---|---|---|
| Administrative capacity | Consul Govern action + Accord system | Adequate — governance quality is emergent from Prosperity/Accord |
| Naval power | Abstractable through Military + geography | Adequate — Valoria is a peninsula but naval operations aren't a separate domain |
| Religious authority | CI track (peninsula-wide) + Church Attention Pool | Adequate — CI is the institutional-authority equivalent |
| Trade network intelligence | Covered by Consul actions + Hafenmark Diplomat | Would benefit from Intelligence stat (trade routes = information routes) |
| Mercenary hiring | Implicitly Military + Wealth | Could be explicit but abstractable — complexity cost not justified |

**Only Intelligence emerges as a clear gap.** The other five stats cover their Renaissance analogues well. The non-stat tracks (CI, VTM, WC, Accord, etc.) handle the faction-specific dynamics that don't generalize to all factions.

---

## Decision Needed (Jordan)

1. **Restore Intelligence as 6th faction stat?** If yes, starting values above. This unblocks Varfell Path A, fixes Spy Ob, and differentiates Varfell's stat profile.
2. **If no:** Spy Ob needs a replacement formula. Varfell Path A needs a non-Intelligence re-gate. Varfell needs some other stat differentiation.
