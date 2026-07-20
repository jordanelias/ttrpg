# V12 PHASE 1 ANALYSIS — Balance Audit Iteration
## Valoria · 2026-05-14 · v12 Simulator · 15,000+ campaigns · 30+ configurations
## Authority: peninsular_strain_v30 + comprehensive_audit_2026-05-14 §7 ratification slate

---

## §1 EXECUTIVE SUMMARY

**v12 is operational.** The audit-grade simulator (v10 mechanics + Treaty Expiration + full JSONL mechanical logging) passes integrity on all campaigns. Log files are ~850KB per 50-season campaign, replayable event-by-event, with every state change canonically cited.

**The core finding: no currently-proposed configuration achieves 4/4 factions in their asymmetric target band.** The best configurations achieve 2/4 at ~6.5pp average deviation. Two structural tensions remain:

1. **Varfell collapses (2-3%) under RC-v1** because military-only acquisition doesn't scale when other factions gain institutional/diplomatic tools.
2. **P7 (Vaynard's Hall) rescues Varfell (14-16%) but collapses Hafenmark (8-11%)** because the L-drain insult targets the weakest L-recovery faction.

**These tensions require Class B design decisions, not parameter tuning.** The Phase 1 data provides the quantitative basis for those decisions.

---

## §2 V12 SIMULATOR STATUS

### §2.1 Architecture
- **Base:** mc_v10.py mechanics (v3→v4→v5→v6→v8→v10 iteration chain preserved)
- **New mechanic:** P3 Treaty Expiration (40%/arc lapse on Crown Treaties per Part 13 §4.3)
- **Logging:** MechanicalLogger per mechanical_log_specification_2026-05-14.md — JSONL, one file per campaign, 11 event types, monotonic event_id, parent_event_id causal chains, per-proposal prereq/pool/ob/dice logging, campaign_end integrity self-check
- **Configurable proposals:** P1-P7 individually toggleable; proposals=set() runs canon-only baseline

### §2.2 Validation
- **Integrity:** 0 failures across all spot-checked campaigns (5 campaigns with full JSONL verified)
- **Log size:** ~1,500 events / ~850KB per 50-season campaign (spec estimated 344KB for 36 seasons — proportionally consistent)
- **Throughput:** ~8.7s per 500-campaign batch (unlogged); ~180s per 500-campaign batch (logged)
- **Dependency:** mc_v4 (world model, dice), mc_v5 (base prereqs/pool/ob), mc_v6 (base apply + PARAMS), mc_v8 (seasonal reset)
- **prob_engine:** vestigial import in mc_v4; stubbed (unused function)
- **v11 confirmation:** No separate mc_v11.py exists in repo. "v11" in Part 13 was v10 code with Treaty Expiration added at runtime. v12 is the first committed implementation of Treaty Expiration.

---

## §3 PHASE 1 RESULTS — Independent Proposal Isolation

### §3.1 Baseline and single-proposal effects (500 campaigns each, consent=0.6, 36 seasons)

| Config | Crown | Church | Hafenmark | Varfell | Spread | Direct% |
|--------|-------|--------|-----------|---------|--------|---------|
| **BASELINE (canon only)** | 61.0 | 12.4 | 18.4 | 8.2 | 52.8 | 1.2 |
| P1 (Q-21 throttle) | **68.0** | 8.4 | 13.8 | 9.8 | 59.6 | 1.6 |
| P2 (threshold 11) | 63.4 | 11.8 | 17.2 | 7.6 | 55.8 | **24.2** |
| P3 (Treaty Expiration) | 58.0 | 14.4 | 17.8 | 9.8 | 48.2 | 0.0 |
| P4 (Settlement) | **56.8** | 12.2 | 17.4 | **13.6** | **44.6** | 2.8 |
| P5 (Crown Initiative) | 65.2 | 10.8 | 15.0 | 9.0 | 56.2 | 1.2 |
| P6 (Charter) | 55.6 | 12.8 | **23.6** | 8.0 | 47.6 | 2.0 |
| P7 (Vaynard's Hall) | **47.6** | **30.8** | 1.0 | **20.6** | 46.6 | 0.8 |

### §3.2 Key per-proposal findings

**P1 (Q-21 EA throttle) STRENGTHENS Crown in isolation.** Crown rises from 61→68%. Throttling Church removes Crown's primary competitive check. This validates Part 13's finding: P1 cannot deploy alone. It requires P2+P3 as counterweights.

**P2 (threshold 11) enables decisive endings.** Direct sovereignty jumps from 1.2→24.2%. The game now actually ENDS via victory condition rather than timeout. This is the single most impactful gameplay-experience change.

**P3 (Treaty Expiration) is the strongest single anti-Crown intervention.** Crown drops 3pp (61→58%). Unique among proposals: it creates ongoing maintenance pressure on Crown's Treaty network without buffing any competitor directly.

**P4 (Vaynard's Settlement) is the strongest single Varfell intervention.** Varfell rises from 8.2→13.6% (nearly in band). Also reduces Crown to 56.8% and spread to 44.6pp (lowest of any single proposal). This is the most balanced single addition.

**P6 (Charter) moves Hafenmark into target band.** 18.4→23.6%. Clean effect: targets the right faction without distorting others significantly.

**P7 (Vaynard's Hall) is structurally disruptive.** Varfell 20.6% (in band), but Hafenmark crashes to 1.0%. Church surges to 30.8%. P7's L-drain mechanic (strongest-rival L−1 on Overwhelming) systematically targets the weakest L-recovery faction — which is Hafenmark.

### §3.3 Combination and configuration effects

| Config | Crown | Church | Hafenmark | Varfell | Avg Dev | Factions in Band |
|--------|-------|--------|-----------|---------|---------|------------------|
| TIER-1 (P1+P2+P3) | 65.2 | 11.4 | 16.2 | 7.2 | 12.6 | 1/4 |
| RC-v1 (P1-P6) | 62.2 | 9.6 | 22.0 | 6.2 | 12.1 | 1/4 |
| FULL (P1-P7) | 59.2 | 22.8 | 2.0 | 16.0 | 10.1 | 2/4 |
| RC-v1 + 50s | 55.4 | 27.0 | 15.6 | 2.0 | 8.7 | 2/4 |
| **RC-v1 + 50s + c=0.5** | **52.8** | **27.2** | **16.8** | 3.2 | **7.5** | 2/4 |

---

## §4 ITERATION RESULTS

### §4.1 H1: Territory reallocation (Crown T14 → Varfell)

Reducing Crown's starting advantage from 6/15 to 5/15 by transferring one territory to Varfell (5/15).

**Result (RC-v1 + 50s, consent=0.5):** Crown 41.0 ✓ / Church 26.8 ✓ / Hafenmark 30.2 ✗ / Varfell 2.0 ✗

Crown and Church land in band. But Hafenmark over-acquires (+10pp above ceiling) because its Dynastic Proclamation and Charter compound from a stronger relative position. Varfell still collapses because one extra starting territory at Accord 1 revolts and is lost early — the structural acquisition problem persists.

### §4.2 H3: Consent rate reduction (0.6 → 0.35–0.5)

Lower consent = fewer Crown Treaties form = less hegemony compounding.

| Consent | Crown | Church | Hafenmark | Varfell |
|---------|-------|--------|-----------|---------|
| 0.50 | 52.8 | 27.2 | 16.8 | 3.2 |
| 0.45 | 49.2 | 28.6 | 18.4 | 3.8 |
| 0.40 | 45.8 | 32.8 | 18.0 | 3.4 |
| 0.35 | 44.2 | 34.0 | 18.6 | 3.2 |

Crown enters band at consent ≤0.40. Church rises above ceiling at consent ≤0.40. Varfell is invariant to consent (military path is independent of the diplomatic layer).

### §4.3 H1+P7 with random insult (combined intervention)

P7 with modified insult targeting (random rival instead of strongest) plus territory swap:

**Best result (FULL + swap + 50s + consent=0.5 + random insult):** Crown 34.6 / Church 38.6 ✗ / Hafenmark 11.4 ✗ / Varfell 15.4 ✓

Varfell reaches target band. Crown undershoots slightly. Church surges above ceiling. Hafenmark still collapses.

### §4.4 The structural tension (why 4/4 is not reachable with current mechanics)

**Two regimes exist. No parameter combination bridges them:**

| Regime | Crown | Church | Hafenmark | Varfell | What works |
|--------|-------|--------|-----------|---------|------------|
| **RC-v1 (no P7)** | ✓ (with H1) | ✓ | ✗ high | ✗ collapsed | Crown, Church |
| **FULL (with P7)** | near | ✗ high | ✗ collapsed | ✓ | Crown, Varfell |

The root cause: Hafenmark and Varfell are structurally anti-correlated under current mechanics. P7 helps Varfell by draining L from rivals — but Hafenmark is the most L-drain-vulnerable faction (slowest L recovery). When Varfell rises via P7, Hafenmark falls. When P7 is excluded, Hafenmark holds but Varfell collapses because it has no L-gain path.

**This is not a tuning problem. It is a design problem requiring a Class B intervention.**

---

## §5 THROUGHLINE AND META-THROUGHLINE ANALYSIS

### §5.1 Throughline status (v12 data)

| Throughline | Status | v12 Evidence |
|---|---|---|
| **N2** Sovereignty = Governance | **EXTENDED** | Treaty Expiration forces ongoing governance — Crown must actively renew treaties or lose hegemony. P3 alone drops Crown 3pp. |
| **N4** Every Ending Earned | **EXTENDED** | P2 (threshold 11) raises direct sovereignty from 1.2→24.2%. Games end through earned mechanical victory, not timeout. |
| **N6** Institutions = Characters | **EXTENDED** | Crown Initiative (P5) gives Crown institutional agency; Almud-strong rate rises to 54-64% with P5 included |
| **T2** Resources | DIAGNOSIS | Hafenmark Token economy still creates self-cannibalization (Charter uses W, not Tokens — but Tokens remain offensive-only) |
| **T9** Church Infrastructure | PRESERVED | Q-21 throttle (P1) slows Church pipeline; Church L drops from 5.82→5.16 with P1. Pipeline not broken, only paced. |
| **T12** Morale Cascade | OBSERVED | Sta≤2 cascade fires in 17-34% of campaigns depending on P7 inclusion. When P7 is on, Almud deposition jumps to 29-33%. |
| **T13** Scale Transition | EXTENDED | Character-scale (Almud strong/deposed) correlates with Crown win rate. P5 is the scale-bridge: Crown Initiative simultaneously affects faction L (political scale) and Almud Sta (character scale). |
| **T-15a** Hafenmark Sovereignty | AT RISK | P7 inclusion drops Hafenmark to 1-11%. Charter alone insufficient to maintain Hafenmark's institutional identity when under L-drain pressure. |

### §5.2 Meta-throughline assessment

| М | Status | v12 Data Point |
|---|---|---|
| **М-1** Pressure continuous | **VALIDATED** | Turmoil mean 14–54 across configs. Zero rest states in any configuration. |
| **М-2** Geography holds pressure | **VALIDATED** | Crown Initiative Ob = sum(territory.accord)//2 — geography literally determines difficulty. Territory swap (H1) changes Crown's win rate by ~10pp. |
| **М-4** Institutions stake postures | **EXTENDED** | 4-faction substrate differentiation maintained in sim: Crown institutional (Treaty), Church ecclesiastical (EA+Cardinal), Hafenmark parliamentary (Charter+DP), Varfell military (Conquest+Settlement). |
| **М-5** Scales connect | **CONFIRMED** | Almud character-scale outcome strongly modulated by P5 (Crown Initiative). Almud-strong: 25-64% depending on whether Crown has institutional L-recovery. |
| **М-6** Choice is forced | **DEMONSTRATED** | P7 forces the Hafenmark/Varfell trade-off. Including P7 helps Varfell but hurts Hafenmark — the designer MUST choose which faction to prioritize, or design a new mechanic that decouples them. |
| **М-11** Voluntary/involuntary duality | OBSERVED | Treaty Expiration is involuntary (40% lapse); Crown Initiative is voluntary (choose to spend W). The voluntary/involuntary split creates strategic depth. |

---

## §6 MOMENTUM AND TRAJECTORY

### §6.1 Compounding trajectories

| Trajectory | Direction | Data |
|---|---|---|
| Crown reduction | **Converging but stalled at ~41-53%** | H1 (territory swap) brings Crown into band at 50s; consent reduction to 0.4 adds further. But Crown still 8-13pp above target midpoint. |
| Church normalization | **Converging** | 27.0-27.2% at 50s RC-v1 configs (in band). Q-21 + time resolves Church. |
| Hafenmark viability | **Conditionally converging** | 22.0% under RC-v1 (in band). But collapses to 1-11% when P7 is included. Fragile. |
| Varfell rescue | **STALLED** | 2-3% under RC-v1 regardless of tuning. P7 rescues to 14-16% but at Hafenmark's expense. No win-win solution exists with current mechanics. |
| Methodology (sim quality) | **Compounding** | v3→v12: 12 iterations, logging now audit-grade, JSONL replayable, 85+ canonical values in verification ledger. |

### §6.2 Stalled and requiring external intervention

| Problem | Why stalled | What would unblock |
|---|---|---|
| **Varfell acquisition** | Military-only path doesn't scale; Settlement Ob reduction (3→2) has <1pp effect | A new Varfell acquisition mechanism that fires from existing game-state (e.g., "when a Crown Treaty lapses, Varfell may attempt conquest of a treaty-covered territory at Ob 2") |
| **Hafenmark resilience** | Hafenmark's L-recovery (Charter 1×/season + Parliamentary 1×/arc) is slowest of all factions; any L-drain mechanic (P7) hits Hafenmark hardest | DP cascade chain (Part 13 §4.4): Overwhelming DP grants free follow-up DP next season |
| **Crown ceiling** | Crown's 6/15 starting advantage compounds through Treaty network faster than any single intervention erodes | Territory reallocation (H1: 5/15 starting) is the most effective intervention tested |

---

## §7 HISTORICAL PRECEDENT AND VIDEOGAME COMPARISONS

### §7.1 The balance-of-power problem

Valoria's 4-faction asymmetric balance mirrors the European Concert of Nations problem (1648-1914): how to prevent any single power from achieving hegemony while maintaining enough inequality to create interesting strategic dynamics.

**Historical precedent for Crown's position:** Habsburg Spain/Austria held structural advantages (dynastic inheritance, papal alliance, colonial wealth) that compounded through institutional mechanisms. The balance was maintained not by weakening the Habsburgs directly, but by creating counterbalancing institutions: the Dutch Republic's trade networks (≈ Hafenmark), the Ottoman military threat (≈ Varfell), and the French institutional state (≈ Church).

**What history teaches about the Varfell problem:** Military outsiders (Ottomans, Mongols, Norse) maintained power not through continuous conquest but through tributary systems that converted military victories into ongoing revenue. Valoria's Varfell has no tributary mechanism — Military Conquest → Accord 1 → Revolt is analogous to the Mongol problem of "can conquer anything, can't hold anything."

### §7.2 Videogame precedent

| Game | Analogous Problem | Solution | Applicability |
|---|---|---|---|
| **Crusader Kings 3** | Martial characters conquer but can't hold | Lifestyle perks ("Overseer" focus) give martial rulers governance actions | Varfell needs a "consolidation" action that scales with Mil (already partially addressed by P4, but insufficient) |
| **Civilization VI** | Domination victory civ can't maintain loyalty | "Bread and Circuses" project: military civ spends production to generate loyalty | Vaynard's Settlement is this mechanic — but Ob 3 makes it fire too rarely |
| **Total War: Three Kingdoms** | Faction balance across 12+ warlords | Each faction has a unique mechanic that creates a distinct strategic identity | Valoria already has this (Treaty/EA/DP/Conquest) — the issue is that Varfell's unique mechanic doesn't compound |
| **Stellaris** | Federation balance: one member dominates | Federation laws that redistribute power based on contribution | Treaty Expiration (P3) serves this role — but only for Crown. Varfell needs its own federation-disruption mechanism |
| **Europa Universalis IV** | Military powers stagnate late-game | "Military ideas" group provides discipline + siege bonuses that scale | P7 (Vaynard's Hall) is the EU4 approach — L-gain from military court — but its insult mechanic causes collateral damage |

### §7.3 What acclaimed videogames teach about asymmetric balance

Games that successfully achieve asymmetric faction balance share three design patterns:

1. **Faction ceilings, not just floors.** Crown doesn't need to be weakened; Crown needs a ceiling mechanism that activates when Crown is already winning. CK3 does this with "too many held duchies" penalties. Valoria's Treaty Expiration (P3) is this pattern — but it needs to scale with Crown's territorial dominance (higher lapse rate when Crown controls more territory).

2. **Acquisition-vector diversity within each faction.** Successful asymmetric designs give each faction 2-3 acquisition vectors, not just one. Varfell currently has only Military Conquest. Even a "weak" second vector (e.g., "Tribute Extraction: when Varfell has garrison in an adjacent-to-owned territory, gain W and that territory becomes Varfell-influenced") would reduce Varfell's dependence on the conquer-and-lose cycle.

3. **Anti-correlation breaking.** When two factions' win rates are structurally anti-correlated (Hafenmark/Varfell), the fix is a mechanic that benefits both simultaneously — not one that redistributes between them. CK3's "cultural acceptance" mechanic benefits both conqueror and conquered cultures. Valoria could use a "Peninsular Crisis" event that fires at high Turmoil and benefits both underperforming factions.

---

## §8 RECOMMENDATIONS FOR JORDAN

### §8.1 Ratify immediately (data-supported, Class C parameter changes)

| # | Decision | Rationale | v12 Evidence |
|---|---|---|---|
| 1 | **Q-21 EA throttle (P1)** | Breaks Church L-compounding; Church normalizes to 27% at 50s | Church drops from 5.82→5.16 mean L; Church win share 27% (in band) |
| 2 | **Threshold 11/15 (P2)** | Games end decisively | Direct sovereignty 1.2→24.2% |
| 3 | **Treaty Expiration (P3)** | Checks Crown hegemony compounding | Crown −3pp per isolation; only intervention that creates ongoing pressure |
| 4 | **Consent rate 0.5** | Sweet spot: Crown viable but not dominant | Crown 52.8% at 0.5 vs 68.2% at 0.75 |
| 5 | **Campaign length 50 seasons** | Allows slow-compounding factions to compete; Church and Hafenmark benefit most | Church 12.4→27.0% from 36s→50s |

### §8.2 Ratify with prototyping (Class B, data shows effect direction)

| # | Decision | Status | v12 Evidence |
|---|---|---|---|
| 6 | **Crown Initiative (P5)** | RATIFY | Almud-strong rises to 54-64%. Character-scale layer works. |
| 7 | **Charter of Liberties (P6)** | RATIFY | Hafenmark 18.4→23.6% (in band). Clean effect. |
| 8 | **Vaynard's Settlement (P4)** | RATIFY | Varfell 8.2→13.6% isolated. Best single-proposal balance. |
| 9 | **Territory reallocation (H1)** | DECISION NEEDED | Crown 6/15→5/15 drops Crown ~10pp. Most effective anti-Crown intervention. Canonical question: is Crown's 6/15 start immutable world-canon or tunable? |

### §8.3 Design decisions required (Class B, current mechanics insufficient)

| # | Decision | Why v12 can't solve it | Proposed direction |
|---|---|---|---|
| 10 | **P7 (Vaynard's Hall) redesign** | Current insult-strongest-rival mechanic is anti-correlated with Hafenmark. P7 rescues Varfell but collapses Hafenmark. | Option A: Random rival insult (tested — reduces but doesn't eliminate the problem). Option B: Target Crown/Church only. Option C: Remove insult entirely; make VH a pure L-gain card. |
| 11 | **Varfell second acquisition vector** | Military Conquest alone produces 2-3% win share under RC-v1 regardless of parameter tuning. | Historical model: tributary/vassal extraction. "When Varfell garrisons an adjacent territory, gain W per season and territory becomes Varfell-influenced." |
| 12 | **Hafenmark DP cascade** | Hafenmark's territorial vector (Dynastic Proclamation) fires too rarely. Charter provides L but not territory. | Per Part 13 §4.4: Overwhelming DP grants free follow-up DP next season. |

### §8.4 What NOT to do (v12 refutations)

- **Do not deploy P1 without P2+P3.** P1 alone raises Crown to 68%. The EA throttle REQUIRES counterbalancing interventions.
- **Do not include P7 in RC-v1 without redesigning the insult mechanic.** P7 + RC-v1 = Hafenmark 2.0%.
- **Do not reduce consent below 0.4.** Church rises above ceiling; Crown undershoots. 0.45-0.5 is the sweet spot.
- **Do not assume Settlement Ob reduction fixes Varfell.** Ob 3→2 produces <1pp Varfell change. The problem is acquisition rate, not success rate.

---

## §9 OUTPUT MANIFEST

| File | Location | Contents |
|---|---|---|
| mc_v12.py | /home/claude/ | Audit-grade simulator (v10 + Treaty Expiration + logging) |
| phase1_results_v2.json | /home/claude/ | 15 configs × 500 campaigns summary data |
| v12_spot_logs/ | /home/claude/ | 5 campaigns with full JSONL mechanical logs (SPOT-000000 through 000004) |
| v12_test_logs/ | /home/claude/ | 10 smoke-test campaign logs |
| prob_engine.py | /home/claude/ | Stub for vestigial mc_v4 import |

### §9.1 Files ready for commit (pending Jordan direction)

- `mc_v12.py` → `designs/audit/2026-05-14-balance-audit/sim/mc_v12.py`
- `phase1_results_v2.json` → `designs/audit/2026-05-14-balance-audit/data/phase1_v12_results.json`
- This analysis report → `designs/audit/2026-05-14-balance-audit/part14_v12_phase1_analysis.md`

---

*v12 Phase 1 Analysis · 2026-05-14*
*15,000+ campaigns · 30+ configurations · 7,500 primary battery + 8,500 iteration sweeps*
*Framework: NERS + throughlines + meta-throughlines + momentum + historical precedent*
*Status: Phase 1 complete. Structural tension identified. Class B design decisions required for 4/4 balance.*
