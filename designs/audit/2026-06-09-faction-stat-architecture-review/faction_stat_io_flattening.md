# Faction Statistics — Input / Output Flattening
**Audit deliverable · 2026-06-09 · per-stat: (a) extent as INPUT, (b) input mechanics elaborated, (c) extent as OUTPUT, (d) output mechanics elaborated**

Re-cut of the 2026-06-09 attribute flatten (`flatten_scan`, 23 authoritative docs) into the **input/output** duality:
an **INPUT** site is a mechanic that *reads* the stat (resolution leverage, threshold gate, derivation, accounting
check, NPC AI); an **OUTPUT** site is a mechanic that *writes* it (action degree-effect, event, accounting delta,
Domain Echo, cap). Incidental prose mentions are excluded from input counts. This is the cut that tells you, per stat,
how much rewiring "make it derived" actually costs: write-heavy stats have many outputs to re-route to the substrate;
read-heavy stats are nearly free to express as derived readouts.

---

## 0 — Summary (read this first)

| Stat | INPUT-sites | OUTPUT-sites | Profile | Natural basis | Migration character |
|---|---:|---:|---|---|---|
| **Mandate** | 70 | 78 | balanced — heavy both | settlement L/PS aggregate (**already defined**, `faction_canon L214`) | the F1 backlog: aggregation exists, 78 writes never re-routed |
| **Stability** | 49 | **97** | **write-dominant** | Σ settlement Order + province Accord | **heaviest** — universal failure-sink; 97 writes to re-route |
| **Wealth** | 17 | 35 | write-dominant | Σ settlement Local Economy (`Prosp×50`) | heavy — economic events; clean settlement basis |
| **Influence** | 52 | 23 | read-dominant | national/diplomatic (weak settlement) | light writes; basis is institutional, **not** settlement |
| **Military** | 38 | 17 | read-dominant | Σ settlement Garrison + holdings | light writes; settlement + national casualty events |
| **Intel** | 10 | 5 | read-dominant, low-volume | national/institutional (no settlement basis) | cleanest national-derived; resolution-only |

**Two cross-cutting findings:**

1. **Every OUTPUT mechanic falls into five archetypes, each with a clean re-route target under the derived model** —
   *action_degree* (Success/Failure → ±) → a settlement-stat change at the action's locus, or a national-event modifier;
   *event* (treaty/collapse/breach) → a national-event modifier Key; *accounting* (seasonal drains/checks) → re-derive
   from the updated substrate at Accounting; *domain_echo* (scene) → a settlement-stat change at the scene's locus;
   *cap* (FACTION_STAT_SEASONAL_CAP ±2, hard ceiling 7) → a clamp on the derivation. The migration is therefore
   systematic, not ad-hoc.
2. **"Church Influence" (CI, a 0–100 clock) is conflated with the Influence stat (1–7)** throughout. Much of Influence's
   apparent OUTPUT volume is CI-clock writes (`+1 control`, `+3 resist`), not writes to the base 1–7 stat — base
   Influence is even more read-dominant than the raw count shows. This naming overload is worth a separate cleanup.

---

## 1 — Mandate  (INPUT 70 · OUTPUT 78)

**Role today:** d+σ leverage stat for Crown/Church *authority* actions; eligibility gate; **and** already canonically
defined as a settlement aggregate (`faction_canon L214`: `Mandate(faction) = clamp(round(7·T/(T+K)), 0, 7)`,
`T = Σ controlled-settlement quotient`). The 70/78 balance *is* the C-2 role-conflation made quantitative.

### (a) Input extent — 70 sites: threshold 35 · resolution 15 · accounting 9 · derivation/other 9 · npc 2
### (b) Input mechanics (what reads Mandate)
- **d+σ resolution (15).** Mandate is the acting-stat for authority actions: Suppress (`Mandate vs floor(Church-Man/2)+1`),
  Censure (`Ob 2`) / Outlawry (`Ob 3`), Sovereign Authority Doctrine (`Ob 4`), Excommunication (`M = Mandate − target Mandate`),
  Royal Decree (`M = Mandate − 2`), and treaty positioning/ratification (`M = Mandate − 2`, ED-865/874). *Reading a derived
  Mandate here is fine — the resolver consumes whatever value Mandate holds.*
- **Threshold / eligibility gates (35).** `Mandate ≥ N` gates standing: Parliamentary Motion (`≥2`), Censure (`2`),
  Subsidy / Succession Endorsement (`≥3`), Blockade (`3`), Outlawry (`5`), Sacred actions (`≥3/4`); passive: Baralta
  `Mandate ≥ 4 → CI −1/season`. Mandate is the clout currency for parliamentary + authority eligibility.
- **Accounting checks (9).** Turmoil Mandate check (`Ob 2/3`, Fail → −1); CI-driven opposing-Mandate reduction at high CI
  (`−3/faction at CI 100`); Legitimacy-0 Mandate check.
- **Derivation / other (9).** The LPS-2e aggregation itself (`L214`); the `Mandate cap 7` ceiling; Parliament vote-weight
  = current Mandate (`faction_layer §5.3`); `Govern Success: +Mandate × 5` feeding Legitimacy.

### (c) Output extent — 78 sites: other_write 38 · event 18 · action_degree 18 · accounting 4
### (d) Output mechanics (what writes Mandate)
- **Events (18).** Treaty breach (`−2`), Faction Collapse (`→0` immediate), Excommunication threat, crown-break, partition.
  Discrete political shocks.
- **Action degree-effects (18).** Assassination Success (`−1`), Censure (`−1`), Outlawry (`−2`), failed Church intervention
  (`−1`), Absolution (Church pays `−1`, target `+1`), proposer reputational `−1` on Overwhelming.
- **Other / accounting (42).** Collapse attribute-snapshot (`→0`); treaty unique-action costs; Govern recovery (`+1` in
  capital, PP-174); Crisis penalty (`−1` at next Accounting); the `M = Mandate − 2` positioning writes.
- **The point:** all 78 directly mutate a value `L214` defines as a settlement aggregate. Under the inversion each routes
  to settlement L/PS (governance, suppression, occupation effects) or to a decaying national-event modifier (treaties,
  collapse, decrees). Nothing should write `Mandate` itself.

---

## 2 — Stability  (INPUT 49 · OUTPUT 97 — the most-written stat)

**Role today:** the universal *consequence sink* — nearly every Domain Action Failure costs `Stability −1` — plus the
seasonal solvency gate (the Accounting Stability Check). Write-dominant by a wide margin.

### (a) Input extent — 49 sites: threshold 27 · accounting 14 · resolution 6 · other 2
### (b) Input mechanics (what reads Stability)
- **Threshold gates (27).** `Stability ≥ 2` (mutual-peace treaty term), `≤ 1` (Capitulation `−3`), `≤ 2` (Absolution target
  eligibility), and low-Stability vulnerability bands. Stability gates treaty terms and exposure.
- **Accounting Stability Check (14).** Fires when a faction loses `≥ 2` attribute points in a season: roll a Stability pool
  vs `Ob = magnitude of loss`; Failure → `Stability −1`; at 0 → Collapse. The core seasonal solvency mechanic.
- **d+σ / pool resolution (6).** The Accounting check's pool roll; committed-force conditions reading Stability.

### (c) Output extent — 97 sites: action_degree 45 · other_write 33 · event 8 · accounting 8 · cap 3
### (d) Output mechanics (what writes Stability)
- **Action degree-effects (45).** The dominant source: **`Failure → Stability −1` on nearly every Domain Action**;
  Suppress Failure `−1` (the retained PP-403 exception); `Overwhelming → +1` (rally); occupation recapture effects.
- **Other / events / accounting (49).** FSS-LOOP-1 deterministic low-Stability floor (2026-05-30); parliamentary penalties
  (Censure/Embargo/Blockade/Outlawry `−1/−2`); treaty breach (`−1`), crown-break (`−2`), target-break; occupation
  (`−1/season` accumulating); Institutional Consolidation (`+1`); PI ≥ 8 (`+1` on passed checks).
- **Cap (3).** `FACTION_STAT_SEASONAL_CAP = ±2`; PI-driven gains capped `+2/season`.
- **The point:** 97 writes, overwhelmingly action-Failure penalties. Under the inversion, Stability derives from
  `f(Σ settlement Order, province Accord)` plus national stability events (successions, coups, suppressions, breaches).
  The 45 action-Failure writes become Order/Accord perturbations at the action's locus or national-event modifiers; the
  Accounting Stability Check becomes a check on the *derived* Stability. **This is the heaviest single migration** — but
  the basis is sound and the writes are homogeneous (mostly `−1` on Failure), so the re-route is mechanical.

---

## 3 — Wealth  (INPUT 17 · OUTPUT 35)

**Role today:** d+σ stat for economic actions; capacity gate; feeds the spendable Treasury (`×100`). Write-dominant.

### (a) Input extent — 17 sites: threshold 10 · resolution 3 · derivation 3 · other 1
### (b) Input mechanics (what reads Wealth)
- **Threshold gates (10).** `Wealth ≥ 4` (Guild commercial leverage, indemnity ×1.5); `Wealth 0` → Muster (Legionary Inward)
  unavailable until `≥ 1`, and Military `−1/season` (unpaid mercenaries); indemnity transfers (1/2/3 points at signing).
- **d+σ resolution (3).** Trade / Consul Outward (`M = Wealth − difficulty`); Economic Leverage (`M = Wealth − target Wealth`).
- **Derivation (3).** `Treasury = Wealth × 100` (the spendable gauge); Trade Success `+Wealth × 25` / Overwhelming `+Wealth × 50` gold.

### (c) Output extent — 35 sites: action_degree 14 · other_write 12 · accounting 9
### (d) Output mechanics (what writes Wealth)
- **Action degree-effects (14).** Embargo (`−1/season`), Blockade (`−2/season`), Subsidy (recipient `+1`, payer `−1`),
  Trade Success (`+1`) / Overwhelming (`+2`, seasonal-capped).
- **Accounting / other (21).** Prudence action (`+1/season`); "stressed" penalty (`−1` when expenditure < 2× rolled net);
  Wealth-0 recovery restores the stat; Church Wealth comparisons at Accounting.
- **The point:** 35 writes, mostly economic actions/events. Under the inversion, Wealth = `Σ settlement Local Economy`
  (`Prosperity × 50`) + national economic-event modifiers (trade deals, indemnities, sanctions). Trade/Embargo become
  changes to the targeted settlements' Prosperity; Subsidy is a transfer event; Treasury is the settlement-economy
  aggregate (spendable), dissolving C-3. **Clean settlement basis.**

---

## 4 — Influence  (INPUT 52 · OUTPUT 23 — read-dominant)

**Role today:** the dominant d+σ stat for diplomacy/assertion. **Caveat:** "Church Influence" (= CI, a 0–100 clock) is
conflated with the 1–7 Influence stat in many sites; most "Influence" writes are CI-clock writes, so the base stat is
even more read-leaning than 52/23 suggests.

### (a) Input extent — 52 sites: resolution 34 · threshold 10 · derivation 2 · other/accounting 6
### (b) Input mechanics (what reads Influence)
- **d+σ resolution (34).** Assert (`Influence vs Ob 2`), Reconstitute collapsed faction (`Influence Ob 4`, ×3 seasons),
  Church Territorial Seizure (`Influence + floor(CI/15) vs Ob = 7 − PT`), Economic/diplomatic actions, Parliamentary
  inquiry (`Crown Influence + Mandate`). Influence is the primary assertion/diplomacy leverage stat.
- **Threshold gates (10).** CI brackets (`CI 60` seizure, `CI 30/80` Ob modifiers) and `Reconstitute Ob 4` — note several
  are CI-clock thresholds, not base-stat gates.
- **Derivation (2).** `+Influence × 5` (Intel/Spy) / `+Influence × 10` (Diplomacy) → Reputation capital.

### (c) Output extent — 23 sites: other_write 13 · accounting 4 · action_degree 4 · cap/event 2
### (d) Output mechanics (what writes Influence)
- **CI-clock writes (most of the 23).** `Church Influence +1` (territory control), `+3` (resist), `+0.5` (attention),
  `−1/season` (Baralta suppression) — these move **CI**, the clock, not the base Influence stat.
- **Capital feedback (a few).** Reputation 0 → diplomatic/Intel `+1 Ob`; sustained 0 → `Influence −1` (the `§14` erosion).
- **The point:** the base 1–7 Influence stat is rarely written directly; it is a near-pure resolution INPUT. It is an
  excellent derived-readout candidate — **but its basis is national/diplomatic (alliances, parliamentary standing,
  recognition), not a settlement aggregate.** Forcing a settlement sum here would be invented; Influence derives from a
  thin structural base (capital prominence / reach) plus a dominant national-event ledger. Resolve the CI/Influence
  naming overload alongside.

---

## 5 — Military  (INPUT 38 · OUTPUT 17 — read-dominant)

**Role today:** combat resolution stat and the ceiling on unit quality; feeds the Levies fielding cap (`×2`). Read-dominant.

### (a) Input extent — 38 sites: resolution 17 · derivation 10 · npc_ai 9 · threshold/accounting 2
### (b) Input mechanics (what reads Military)
- **d+σ / pool resolution (17).** Committed-force condition (`Military pool ≥ 4` to commit to battle; pool 1–3 = uncommitted);
  siege pool (`Attacker Military + 3`); mass-battle engagement pools.
- **Derivation (10).** `Military stat → unit Power ceiling + starting Discipline ceiling` (`§1.3` table); `Levies = Military × 2`
  (fielding cap). Military caps what units a faction can field and how good they are.
- **NPC AI (9).** `Military → Command rating` for NPC generals; reactive-Military guidance; invasion-threshold targeting.

### (c) Output extent — 17 sites: other_write 9 · accounting 4 · cap 2 · action_degree/event 2
### (d) Output mechanics (what writes Military)
- **Battle casualties (9).** `Defender Military −1` (loss margin `−2+`); `Attacker Military −1` (defender wins); per-unit
  destruction in TTRPG mass combat (`Military −1`, cap `−2/season`).
- **Wealth-0 coupling (4).** `Military −1/season` while `Wealth = 0` (unpaid mercenaries) — a cross-stat economic event.
- **The point:** read-dominant; the 17 writes are combat casualties + the Wealth coupling. Under the inversion, Military =
  `Σ settlement Garrison Strength` (`Defense×20 + Fort×30`) + territory holdings + national muster/casualty events.
  Casualties reduce the relevant settlements' garrisons (or a national casualty modifier); Levies is the garrison
  aggregate. **Settlement + national basis, clean.**

---

## 6 — Intel  (INPUT 10 · OUTPUT 5 — lowest volume, resolution-only)

**Role today:** the covert-operations resolution stat. Lowest input/output volume of any faction stat, and the only one
with effectively **no settlement basis**.

### (a) Input extent — 10 sites: resolution 8 · accounting/other 2
### (b) Input mechanics (what reads Intel)
- **d+σ / pool resolution (8).** Investigate / Counter-intelligence pool (`Intel vs Ob 3`); covert Domain Actions;
  `M = Intel − 2` (Varfell "Private Collection"). `Investigate/Intel pool = Intel` — recently split from an
  Influence-fallback (`stats_1_7_scale L41`), confirming Intel is now its own institutional axis.

### (c) Output extent — 5 sites: accounting 2 · other_write 2 · action_degree 1
### (d) Output mechanics (what writes Intel)
- `M = Intel − 2` unique actions (d+σ); `Church Intel +1D` (anti-Varfell detection). Almost nothing writes Intel.
- **The point:** Intel is a near-pure covert-ops INPUT with no territorial basis. It **strongly confirms the review's
  qualification**: Intel is national/institutional (spy networks, Council-of-Ten-style apparatus) and should be derived
  from institutional state + national events, **never** a settlement aggregate. It is the cleanest national-derived case.

---

## 7 — What this means for the derived-stat inversion

The input/output split maps directly onto migration cost and cleanliness:

- **Read-dominant stats (Influence, Military, Intel) are nearly free to make derived** — few writes to re-route, and their
  many reads (d+σ resolution, unit ceilings, covert pools) simply consume whatever the derived value holds. *Reading a
  derived stat was never the problem; only writing it was.* Of these, **Military** has a clean settlement basis (Garrison
  aggregate); **Influence and Intel do not** and must derive from institutional/national state — the one place the
  generalization is not settlement-shaped (and must not be forced to be).
- **Write-dominant stats (Stability, Wealth) carry the migration weight** — 97 and 35 outputs respectively — but their
  writes are homogeneous and their bases are clean (Order/Accord; Local Economy). The work is volume, not ambiguity.
- **Mandate is the worked precedent**: its aggregation is already canonical (`L214`), so its 78 writes are pure backlog —
  the template for what the inversion does to every other stat.

And because all OUTPUT mechanics reduce to five archetypes (§0), each with a defined re-route target, the migration is a
**bounded, mechanical pass over the write-sites** behind two structural decisions only: the Influence/Intel derivation
basis, and the national-event-modifier semantics. The reads need no change.

---
*Flattening only. Source: `flatten_scan` / `flatten_io` over 23 authoritative docs (faction_layer, faction_canon,
faction_behavior, ci_political, victory, strategic_layer, military_layer, faction_politics, stats_1_7_scale,
derived_stats §14, settlement_layer, peninsular_strain, tracks, faction_actions, et al.). Counts exclude incidental prose
mentions from inputs. Site lists are representative, not exhaustive; the full grep is on disk.*
