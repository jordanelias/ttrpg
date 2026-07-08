<!-- SKELETON — mechanical spec only -->
<!-- Infill: faction_layer_v30_infill.md -->
<!-- PP-TBD series — awaiting patch number assignment -->
<!-- Supersedes: PP-403 (Failed DA Stability Cost — REPEALED except §Suppress exception) -->
<!-- Extends: PP-512–514/523 (Crown Treaty), ED-334/335 (Officer Capture), PP-500 (Political Vacuum) -->
<!-- Integrates with: Phase 4 Priority-4 Social actions; Phase 5 Accounting steps 1–13; peninsular_strain_v1.md (Accord, Strain, battle consequences) -->
<!-- Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance) -->
<!-- Date: 2026-04-14 -->

# VALORIA — Faction Layer: Stability, Occupation, Treaties, Negotiation & Parliament
## v1.0 — Canonical design for faction-layer stability and diplomacy mechanics

---

## §0 — AUDIT PATCHES APPLIED IN THIS DOCUMENT

| Conflict resolved | Resolution |
|---|---|
| OFFICER_CAPTURE_CONFLICT | ED-334/335 is canonical for BG/Hybrid officer resolution. New Stability trigger applies additionally. d10 fate table is TTRPG-only (Zoom In). |
| TC_SUPPRESS_STABILITY | Suppress Failure → Stability −1 is RETAINED. It is a named exception to PP-403 repeal, not covered by the new trigger system. |
| CROWN_TREATY_STABILITY_DELTA | Crown Treaty degree effects (victory_v30.md §3.1) are canonical and unchanged. General treaty table in §3 applies to non-Crown-Treaty treaties only. |
| ACCOUNTING_STABILITY_CHECK | Existing Phase 5 Step 2 (Stability pool roll on ≥2 attribute loss) is RETAINED alongside new trigger system. |
| TRIGGER5_POOL_CLIFF (ED-876) | Trigger-5 Condition C clause "Engaged pool ≥ 6" REMOVED from the gate, retained in the cost table as a severity escalator only. Eliminated a non-monotonic battle→Stability exposure (single Command point swinging compound-collapse ~25×). Stage-4 re-tested; routs still penalized, large-force routs still escalate to −2. |
| PARLIAMENT_MANOEUVRE_EXISTING | Parliamentary Manoeuvre is Hafenmark's existing Priority-4 Social action. New Parliament convening is a separate Accounting-phase system. See §5.2 for phase placement. |
| OCCUPATION_TCV_UNSPECIFIED | Occupied territories count 0 TCV for both parties. Control transfer (formal or treaty) required for TCV to count. |
| FACTION_RESOLVER_PROPAGATION (ED-874, W3.3) | Remaining in-scope bare-stat faction checks migrated to the deterministic+stochastic resolver (params/factions/stats_1_7_scale.md §Domain Action Resolution): §1.4 Accounting Stability (M = Stability − loss magnitude), §1.5 Reconstitute (M = Influence − 4), §2.5 Resistance (M = Influence − (floor(opp Mandate/2)+1)), §5.5 Rebuttal (M = Mandate − 2/−3). Completes the ED-865/874 migration begun for treaty Phase 1/3 (§3.3, 270915da). Transformation: legacy "X vs Ob N" → M = X − N; four-degree ladder + named exceptions retained. KEPT (out of ED-874 scope): mass-battle/military pools (Trigger 5, §6.2), TTRPG d10 officer-fate, Mandate vote-tallies. DEFERRED (cross-module, not this commit): §2.7 Church Seizure (CI-coupled) and CI Assert/Suppress (ci_political-owned). |

| Gap closed | Resolution |
|---|---|
| GAP_CASUS_BELLI | Defined in §3.5 |
| GAP_WEALTH_ZERO | Defined in §5.7 |
| GAP_POLITICAL_VACUUM_OCCUPATION | Defined in §2.6 |
| GAP_CHURCH_SEIZURE_OCCUPATION | Defined in §2.7 |
| GAP_BG_OFFICER_FATE | Defined in §6.4 |
| GAP_PARLIAMENT_NPC_VOTES | Defined in §5.8 |

---

## §1 — STABILITY REDESIGNED

### §1.1 Definition

Stability is a faction's capacity to maintain institutional coherence under shock. It does not measure military competence or diplomatic success rate. It measures whether the faction's constituent parts — treasury, army, clergy, guilds, noble houses — remain integrated and functional after significant adverse events.

**PP-403 REPEALED.** Failed Domain Actions no longer cost Stability. See §0 for one named exception (Suppress failure).

**PP-403 exception retained:** Suppress action (CI Accounting formula, params_board_game §CI Generation Step 4) Failure → Stability −1. This is a specific named political commitment failure, not a general action failure.

### §1.2 Stability Triggers (Five Canonical)

Stability changes only from the following triggers. No other domain action or event reduces Stability unless a specific named rule states otherwise.

**The Accounting Stability Check** (existing Phase 5 Step 2) is retained separately. It fires when a faction sustains ≥2 attribute losses in one season. It is a cascade check, not a primary trigger.

---

#### Trigger 1 — Territorial Occupation or Loss

| Event | Stability Δ | Timing |
|---|---|---|
| Own territory placed under Occupation | −1 | Immediate, one-time |
| Own territory Occupied at Accounting start | −1 | Ongoing, each Accounting |
| Territory formally transferred (control lost) | −1 additional | At moment of transfer |
| Capital territory lost (T1, T8, T9, T12) | −2 total (not −1) | Replaces standard −1 |
| Capital territory formally transferred | −3 total | Replaces standard −2 |

Capital territories: T1 Valorsplatz (Crown), T8 Gransol (Hafenmark), T9 Himmelenger (Church), T12 Sigurdshelm (Varfell).

---

## §1.5 Faction Doctrine Notes (canon 2026-04-30, ED-775)

### Crown — most impressive at game start, structurally most fragile

Crown holds the highest perceived strength at game start: highest Mandate, highest Wealth, capital + heartland territory (T1 Valorsplatz, T2 Kronmark, T5 Feldmark, T6 Stillhelm, T14 Ehrenfeld) plus the Löwenritter standing army (see below). It is also the campaign's central locus of structural tension. Almud (Crown leader) is canonically constrained to *choosing the least-bad option* in every season because his position is assailed from every axis simultaneously: Altonia (external invasion threat), Schoenland (naval mediation pressure), Restoration Movement (cultural infiltration in Crown territories T2/T5), Church (Sovereignty axis — Crown vs Theocracy), Hafenmark (commercial competition), Varfell (Vaynard's military and political ambitions), and the Löwenritter Order itself (graduated autonomy → coup pressure). Crown's perceived strength is exactly what makes its fracture the campaign's central dramatic possibility — every faction has reason to press, and Almud cannot resist all simultaneously. The fragility is structural, not stat-based.

### Crown standing military force — Löwenritter

Crown's standing army is the Löwenritter Order. All Crown military operations field Löwenritter units pre-coup. Crown faction Military stat 5 is expressed through Löwenritter Power 5 / Discipline 6 elite units (per stats_1_7_scale; military_layer §1.3 Power ceiling). The Löwenritter row in mass_battle §B.4 faction tactic table exists to represent the post-coup scenario where the Order acts as an independent faction (graduated autonomy → Coup Counter trigger → Löwenritter playable). Pre-coup, Crown's tactic options include Löwenritter unit fielding by default; post-coup, Löwenritter cards become available to a new player. This is the unique-faction-promotion mechanic; no other faction in canon has this structure.

### Hafenmark — equipment quality from mining and smithing

Hafenmark Military stat 4 is mid-tier numerically but expressed mechanically as *equipment quality*. Hafenmark's mining (T17 Halvarshelm Northern Mines) and smithing infrastructure (T8 Gransol metalworking) produce superior arms and armour. Hafenmark-mustered units field above-quality-tier weapons and armour relative to peers at the same Military stat. The exact mechanical expression — weapon damage modifier, effective Armour tier shift, or both — is **TBD via simulation testing** (ED-776 standing flag). Doctrine canon is fixed; mechanic calibration is open.

### Varfell — cunning + proud, classical stratagem doctrine

Varfell Military stat 4 is mid-tier (matches Hafenmark, one below Crown). Their advantage is *cunning in service of pride* — Vaynard ("Magnus Vaynard, the White Wolf") presses every available advantage but refuses anything publicly seen as cowardly. Acceptable register: classical battlefield stratagem (Hannibal at Trasimene, Belisarius reading Persians, Mongol envelopment reads, oblique order, recognized terrain exploitation, calculated retreat). Unacceptable register: assassination, civilian targeting, breaking parley, sneak-thievery. Varfell's Intel-stat advantage expresses as Talleyrand-style diplomatic intelligence, not espionage. Their tactic card Stratagem (mass_battle §B.4, PP-690) and Calculated Retreat both encode this prestige-doctrine framing. Varfell's actions are **not restricted to military means**: like every faction it can take **all universal faction actions**, and it additionally has the non-military **Cultural Reclamation** action (`conviction_track_v30`, Movement Actions — Influence vs Ob 2; on success the target territory's **Piety Track shifts −1** toward the Einhir Restoration pole; available where Varfell controls the territory or the territory has Einhir cultural presence). Cultural Reclamation acts on a territory's **religious/cultural alignment (Piety), not its control** — at PT 0 (Einhir Restoration) orthodox seizure of that territory becomes nearly impossible, but no control transfers from the action itself. **It is not a path to victory.** Per **GD-1**, the **sole** victory condition — for Varfell and every other faction — is **Peninsular Sovereignty** (control of 11+ of 15 territories); there is no faction-specific, religious, or otherwise non-military victory path. VTM (Vaynard Thread Mastery) remains struck (a placeholder with no canonical advancement); Cultural Reclamation is **VTM-free** (Influence-based), which is why it is canonical and live. [CORRECTION 2026-05-29, ED-880: supersedes the prior "Varfell expansion is purely military / does not convert populations ideologically" framing (the 2026-04-19 Cultural **Reformation** strike rationale). That strike validly removed the VTM-dependent Cultural Reformation; the Conviction-Track redesign reintroduced the ideological-conversion capability VTM-free as Cultural **Reclamation**, which shifts Piety alignment only — no control transfer, no victory path.]

---



---

#### Trigger 2 — Unfavourable Treaty Terms

Crown Treaty (PP-512–514/523) has its own degree effects per victory_v30.md §3.1 and is not governed by this table.

| Treaty type | Conditions | Stability Δ (receiving party) |
|---|---|---|
| Mutual peace | Both parties Stability ≥ 2; neither dictating | +1 |
| Truce | Temporary suspension; no territory or stat change | 0 |
| Minor cession | ≤1 territory OR indemnity ≤1 Wealth | −1 |
| Major cession | 2+ territories OR indemnity ≥2 Wealth | −2 |
| Capitulation | Signing at Stability ≤1 OR losing ≥50% of held territories | −3 |
| Tributary | Annual Wealth obligation accepted | −1/year while active |

**Treaty breach:** Breaching faction: Mandate −2, Stability −1, all co-signatories gain Casus Belli (§3.5). Faction at Stability 1 facing elimination: Mandate cost waived (survival exception); Stability and CB costs still apply.

**Accord on treaty-based control transfer (peninsular_strain_v1.md §2.3):**
- Territory ceded via Truce or Peace: Accord set to 2 (diplomatic legitimacy).
- Territory ceded via Capitulation: Accord set to 1 (population views cession as humiliation, resists new ruler).
- Territory ceded via Tributary: Accord set to 2 (institutional continuity maintained).

**Treaty types and effective hegemony (peninsular_strain_v1.md §6.1):**
Treaties that count toward "effective hegemony" for universal victory: Peace, Alliance, Capitulation, Tributary (these represent genuine subordination). Truce and Commercial treaty do NOT count (temporary/economic only, no political submission).

---

#### Trigger 3 — Antagonistic Parliamentary Vote

Parliamentary vote effects on target faction. See §5 for full Parliament mechanics.

| Action | Stability Δ | Mandate Δ |
|---|---|---|
| Censure | −1 one-time | −1 |
| Blockade | −1 one-time | 0 |
| Combined Embargo+Blockade active | −1/season ongoing | 0 |
| Outlawry | −2 one-time | −2 |

---

#### Trigger 4 — Major Subterfuge

| Outcome | Stability Δ (target) |
|---|---|
| Sabotage success (Intel vs Stability, Success degree) | −1 |
| Assassination of named officer NPC, Success | −2; Mandate −1 |
| Assassination Overwhelming (clean, no evidence) | −2; no Mandate cost |
<!-- Niflhel operative row deleted 2026-04-30 — Niflhel struck. Replacement: settlement-broker exposure handled per settlement_layer §4.7-4.9 broker compromise rules. -->

---

#### Trigger 5 — Failed Military Engagement: Significant Losses

Three-condition gate. ALL three must be met simultaneously.

**Condition A — Committed force.** Acting faction's Military pool ≥ 4 at time of roll. (Pool 1–3 = raid/skirmish; no Stability consequence on failure.)

**Condition B — Clear defeat.** Roll degree = Failure (net successes ≤ 0). Partial excluded — disciplined withdrawal, no Stability cost.

**Condition C — Severity threshold.** At least one of:
- Net successes ≤ −2 (rout, not mere repulse)
- Named officer NPC attached to action and captured or killed in associated scene

> **[ED-876 patch, 2026-05-28]** The former Condition-C clause "Engaged pool ≥ 6 (major-force commitment)" has been **removed from the gate** and retained only in the cost table below as a *severity escalator*. Rationale: as a gate clause it auto-fired Trigger 5 on *any* failure once a faction's pool reached 6D, making battle→Stability exposure non-monotonic in faction strength — a single Command point (2→3, pool 4D→6D) raised compound-collapse probability ~25× (mid-tier factions became the most collapse-prone, weakest the most shielded). With the clause moved to cost-only, the gate fires on a genuine rout (net ≤ −2) or officer loss; a large force that fails *without* routing (net 0/−1) takes no Stability hit — consistent with Condition B's "disciplined withdrawal, no Stability cost." Stage-4 re-test: firing rate flattened to monotonic; 100% of genuine routs still penalized; large-force routs still escalate to −2 via the cost table. See `designs/audit/2026-05-28-resolution-diagnostic/faction_remediation_development.md`.

**Costs when gate met:**

| Severity | Stability Δ |
|---|---|
| Gate met: net −1 or −2, pool 4–5 | −1 |
| Gate met: net ≤ −3 OR pool ≥ 6 | −2 |
| Named officer NPC killed | −1 additional |
| Named officer NPC captured (ransom unpaid) | −1 ongoing per season |
| Attacking own capital territory and failing | −1 additional |
| Maximum single-event total | −4 |

---

### §1.3 Stability Recovery

| Recovery path | Condition | Stability Δ |
|---|---|---|
| Mutual peace treaty | Both parties Stability ≥ 2 | +1 |
| Recapture own occupied territory | Military_advance Success | +1 |
| Rebuttal roll Overwhelming (Parliament) | See §5.5 | +1 |

**Settlement targeting (AUD-SET-02):** Accord ±N rules in this document target specific settlements per peninsular_strain_v30 §2.5. Province-level "Accord set to N" (transfers, cession) resets all settlement Order values. Incremental changes (±1) target the settlement specified in §2.5 Category B table.
| Institutional consolidation | No Trigger 1–5 fired against this faction this season at Accounting | +1 (also: Accord +1 in one territory at controller choice, cap 2 — stable governance builds trust) |
| Church Absolution (Church unique action) | Target Stability ≤ 2; costs Church Mandate −1 | +1 to target; Church Influence +1 |
| Löwenritter public endorsement | Löwenritter Stability ≥ 3, Military ≥ 4 | +1 to target; Löwenritter Mandate +1 |

**Seasonal cap:** FACTION_STAT_SEASONAL_CAP = ±2 applies. No more than +2 Stability per season from any combination of sources.

**Institutional consolidation note:** This recovery path (+1 for a "clean" season) replaces the abstract simulator recovery rule introduced during development. It is now formally canonical.

---

### §1.4 Accounting Stability Check (Existing — Retained)

Phase 5 Step 2 (existing, params_board_game): any faction with ≥2 attribute points lost this season resolves an Accounting Stability check via the deterministic+stochastic resolver (params/factions/stats_1_7_scale.md §Domain Action Resolution): **M = Stability − (magnitude of total attribute loss)** (legacy: Stability pool vs Ob = loss magnitude). It emits the same four-degree ladder below.

| Result | Effect |
|---|---|
| Failure | Stability −1 (cascade consequence) |
| Partial | No additional loss |
| Success | No additional loss |
| Overwhelming | Stability +1 (faction rallied under pressure) |

This check fires AFTER Trigger 1–5 consequences are applied. It can fire in the same Accounting as a Trigger event.

**Deterministic low-Stability floor (FSS-LOOP-1, 2026-05-30 — resolution-diagnostic ratification; supersedes the §8.12 / factions_personal "Stab ≤ 2 → treated as Ob 4" floor and subsumes the §1.5 Survival Exception's check-path protection).** When a faction is at **Stability ≤ 2**, the Accounting Stability Check **cannot reduce Stability** (it resolves at minimum Partial; an Overwhelming may still raise it). Rationale (NERS-R / Lesson 3 + Lesson 5): the prior "treated as Ob 4" floor was non-functional — a 2D pool vs Ob 4 succeeds ~1% of the time (1D at Stab 1 ≈ 0%), so the "window to intervene" the floor promised was ~1% wide and the passive dice-decay arm of the death-spiral ran essentially unchecked. The deterministic floor removes the **passive** (random-check) path to collapse entirely. **Collapse (Stability 0) remains reachable only via Trigger 1–5 consequences (§1.2) or direct attribute reduction** — i.e. by *active* pressure (occupation, lost battles, hostile votes, subterfuge), never by a bad Accounting roll. This bounds the spiral short of extinction (Lesson 5) while preserving active collapse and therefore the GD-3 Revolt → Insurgency → Faction emergence pathway (canon/02 §GD-3). Historical anchor: polities in crisis are pushed under by active defeat (Byzantine 1204; Habsburg state bankruptcies shrink but do not delete the army), not by passive institutional decay — the floor models a regency/receivership breathing space, deterministic by nature. Stage-4 sim (2026-05-30): under the fixed floor a besieged faction holds at Stab 1–2 and climbs via Institutional Consolidation (§1.3) once trigger pressure relents, while sustained triggers still drive active collapse (P(collapse) 0.41 → 0.97 across rising pressure). **Composes with F5:** Institutional Consolidation (§1.3, +1 for a trigger-free season) is the **universal** recovery path every faction has — the floor makes it reachable by stopping the bleed; no new per-faction recovery apparatus is added (would fail NERS-N/E).

---

### §1.5 Faction Collapse Exit Procedure (ED-675)

When a faction's Stability reaches 0 at Accounting end, the faction collapses. This section consolidates and supersedes P-15, P-24, and §9.10 (strategic_layer_v30) as the single canonical collapse procedure.

**Step 1 — Attribute snapshot.** Mandate drops to 0 immediately (political legitimacy is gone). All other attributes (Military, Wealth, Influence) freeze at their current values. The Mandate drop occurs before the freeze.

**Step 2 — Territory transition.** All territories controlled by the collapsed faction become Uncontrolled. Accord in those territories drops to 0 (Revolt state). Units in those territories become Masterless — they hold position but take no orders. Any faction may Claim Masterless units via Domain Action (Military Ob 2; Success: units transfer to claiming faction at current strength; Failure: units disband). **[ED-FA-0006, 2026-07-08 — DISTILL]** This is not a separate mechanic: "Claim Masterless" is a **target-type variant of March/Conquest** (Action 4). A Masterless target resolves at Military Ob 2 with disband-on-failure instead of the standard battle-engine path — the player's decision (spend a Military-gated action to take a territory, accepting a stated failure risk) is Conquest's own target-selection, not a distinct §1.5 rule. Retained here as the collapse-aftermath *entry point*; the resolution folds into Conquest's target handling.

**Step 3 — Officer and NPC fate.** Named officer NPCs of the collapsed faction enter Independent status. They retain their Conviction, Beliefs, and Disposition values. They may be recruited by other factions via Social Contest (Ob = Leadership Deviation Ob + 2). Unrecruited officers remain in their home settlement as unaffiliated NPCs and may initiate independent actions per npc_behavior_v30 §4.2.

**Step 4 — Player character transition.** A player character affiliated with the collapsed faction loses all faction dice bonuses (Standing-derived). Standing is preserved as a historical record but grants no mechanical benefit. The player continues as an unaffiliated character. Options:

| Path | Requirement | Mechanical effect |
|---|---|---|
| Join another faction | That faction's Standing 0 initiation gate | Begin at Standing 0 in new faction; old Standing irrelevant |
| Reconstitute collapsed faction | Influence Domain Action via resolver (**M = Influence − 4**; legacy Ob 4), repeated 3 seasons consecutively | Faction re-emerges at Stability 1, Mandate 1, other attributes at 50% of frozen values (round down). Player becomes faction leader. Requires at least 1 territory held or recaptured. |
| Remain unaffiliated | None | No faction actions available; personal-scale play only; may act as independent agent or mercenary |

**Step 5 — Parliamentary removal.** The collapsed faction loses its Parliamentary seat. Any active Motions proposed by the collapsed faction lapse. Treaties with the collapsed faction remain in force only if the faction reconstitutes within 4 seasons; otherwise they dissolve automatically.

**Step 6 — Victory path closure.** The collapsed faction's victory conditions are no longer evaluable. If the faction reconstitutes, victory conditions reactivate but all progress counters (TCV, PI, etc.) reset to 0 — reconstitution is a fresh start for victory purposes.

**Collapse immunity:** A faction at Stability 1 that would be reduced to 0 by an Accounting Stability Check (§1.4) may invoke a one-time Survival Exception: Stability remains at 1, but Mandate −1 (minimum 0) and one territory of the attacking faction's choice becomes Contested (Accord → 1). This exception can fire once per faction per campaign.

**Engine note:** Collapse is evaluated at Accounting Step 2 (after trigger consequences, after §1.4 cascade check). The engine checks Stability = 0 after all modifiers resolve. If multiple factions collapse simultaneously, process in descending Mandate order (highest Mandate collapses last — they had the most political capital to burn).


## §2 — TERRITORIAL OCCUPATION

### §2.1 Definition

Occupation is military presence in a territory without formal administrative control. It is distinct from political control (who governs, taxes, and levies). A faction can Occupy a territory it does not formally control, and vice versa (brief window after control transfer while administration transitions).

### §2.2 Occupation Establishment

Military_advance against an enemy-controlled territory:

| Degree | Outcome |
|---|---|
| Failure | No occupation established; Trigger 5 gate checked |
| Partial | Contested: occupier gains foothold but no occupation marker (must follow up next season at −1 Ob) |
| Success | Occupation marker placed; control not yet transferred |
| Overwhelming | Immediate control transfer; no occupation phase |

Ob for military_advance = 2 + (defending territory's Fort level).

| Territory | Fort | March Ob |
|---|---|---|
| T3 Lowenskyst | 3 | 5 |
| T14 Ehrenfeld | 3 (max 4) | 5 |
| T10 Spartfell | 2 | 4 |
| T8 Gransol | 1 | 3 |
| T9 Himmelenger | 2 | 4 |
| T12 Sigurdshelm | 1 | 3 |
| T1 Valorsplatz | 2 | 4 |
| All others (Fort 0) | 0 | 2 |

### §2.3 Occupation Effects

| Effect | On displaced faction | On occupying faction |
|---|---|---|
| TCV | 0 (occupied territory stripped from TCV of both) | 0 |
| Wealth | −1/season | 0 (extraction inefficient) |
| Military | No recruitment from territory | Garrison cost: −1 pool per occupied territory |
| Stability | See Trigger 1 | — |
| Accord | May decline during Occupation from Stability effects (faction_layer §1.2 Trigger 1) — NOT frozen. Accord resets at control transfer per peninsular_strain §7b table. (Prior "Accord frozen" text struck — superseded by peninsular_strain §7b 2026-04-29.) | N/A (occupier has no Accord until control transfers) |

**Accord on Occupation resolution (peninsular_strain_v1.md §2):**
- Occupation → automatic control transfer (3 seasons): Accord set to 1 (Resistant). Population endured 3 seasons of military occupation — they do not welcome the new ruler.
- Occupation → treaty cession: Accord set to 2 (diplomatic transfer carries legitimacy).
- Occupation → Overwhelming military recapture by displaced faction: Accord restored to pre-Occupation value (population rallies behind liberator).
- Occupation → Success military recapture: Accord set to max(pre-Occupation − 1, 1) (liberation is welcome but the territory suffered).
- Church Seizure overriding Occupation (§2.7): Accord per Church Seizure formula (PP-648).

### §2.4 Occupation Duration and Control Transfer

| Duration | Resolution trigger | Outcome |
|---|---|---|
| 1 season | — | Occupation active; control retained by displaced faction |
| 2 seasons | — | Occupation active; displaced faction Stability −1/season accumulating |
| 3 seasons (end of third Accounting without resolution) | Automatic | Control transfers to occupying faction |
| Any duration | Treaty cession | Control transfers immediately |
| Any duration | Recapture (Success) | Occupation marker removed; control restored |
| Any duration | Recapture (Overwhelming) | Occupation marker removed; occupying faction Stability −1 (costly suppression) |

### §2.5 Resistance Check

Once per Accounting while territory is Occupied, displaced faction may declare a Resistance check (does not cost a Domain Action slot; it is a free Accounting action):

- Resolver (params/factions/stats_1_7_scale.md §Domain Action Resolution): **M = Influence − (floor(occupying faction Mandate / 2) + 1)** (legacy: Pool Influence vs Ob floor(occupying Mandate/2)+1)
- Success: Occupation marker removed (territory ungovernable — occupier withdraws)
- Failure: Occupation persists
- Overwhelming: marker removed AND occupying faction Stability −1 (costly suppression)

### §2.6 Political Vacuum Interaction (PP-500 Integration)

Political Vacuum (PP-500) applies when a faction is eliminated. During Vacuum (1 season): no faction may establish Occupation; no march-in; Fort retained. After Vacuum lifts: territory becomes Uncontrolled; normal march rules apply. **Occupation can only be placed on CONTROLLED territories.** Uncontrolled territories may be claimed (free march, no Battle roll).

### §2.7 Church Seizure and Occupation (Integration)

Church Graduated Seizure (victory_v30.md §3.2) is a legal/spiritual transfer mechanism distinct from military occupation. If Church declares Seizure on a territory currently under Occupation by another faction:

- Seizure roll proceeds normally (Influence + floor(CI/15) vs Ob = 7 − PT)
- Success or Overwhelming: Seizure succeeds; Occupation marker removed; Church gains control
- Failure: Occupation marker remains; Church loses Mandate −1 (failed intervention exposed their overreach)
- The occupying faction may contest via military_advance in the following season (Casus Belli against Church for the marker removal)

---

## §3 — TREATY MECHANICS

### §3.1 Treaty Types

Crown Treaty is governed exclusively by victory_v30.md §3.1 (PP-512–514/523). The following applies to all other inter-faction treaties.

| Type | Duration | Primary content |
|---|---|---|
| Truce | Fixed 2–4 seasons | Suspension of hostilities; no stat or territory change |
| Peace | Indefinite until breach | Settlement; may include territory, indemnity, PT clauses |
| Alliance | Indefinite; annual renewal | Mutual military obligation; casus foederis defined |
| Commercial treaty | Indefinite | Trade rights; Guilds/Hafenmark most common |
| Capitulation | Permanent | Dictated submission; losing party has no real options |
| Tributary arrangement | Annual | Wealth transfer obligation; hegemon provides recognition |

### §3.2 Initiating a Treaty

Any active faction may declare treaty intent as a **Senator (Social) action** in Phase 4, consuming one action slot. Target must:
- Accept negotiation (→ §3.3), or
- Refuse (initiating faction gains Casus Belli if they hold occupied territories or PI ≥ 10)

### §3.3 Negotiation Structure (Three Phases)

> **[ED-865/874 migration, 2026-05-30]** Phase-1 positioning and Phase-3 ratification resolve via the deterministic+stochastic resolver (params/factions/stats_1_7_scale.md §Domain Action Resolution), not bare d10 pools. Precedent: early-modern treaty-making is power-structure-decisive (terms track the Mandate/Influence balance; chance is a tail) — the resolver's shape, and it removes the small-pool ratification wall (a Mandate-2 faction no longer fails to ratify its own negotiated treaty ~84% of the time).

**Phase 1 — Positioning roll (resolver, contested).**
Initiator resolves **M = own Influence − target Influence**. Success or Overwhelming → initiator controls opening terms (sets first demand); Partial → terms split, neither controls (tie-break: higher current Mandate controls); Failure → target controls opening terms.

**Phase 2 — Concession declaration.**
No roll. Players/GM declare demands and concessions. Available concession categories:

| Category | Content |
|---|---|
| Territory | Cede Occupation marker; cede formal control; remove troops |
| Indemnity | Wealth transfer at signing (1, 2, or 3 points) |
| Status restoration | Withdraw Parliamentary action |
| Hostages | Named NPC transferred (prevents attacker from military_advance vs signatory while held) |
| Military restriction | No military_advance vs specified territories for N seasons |
| Recognition | Formal acknowledgment of territorial claim |

**Phase 3 — Ratification roll (resolver).**
Each signatory resolves **M = Mandate − 2** (legacy Ob 2 → difficulty 2).

| Result | Effect |
|---|---|
| Failure | Cannot ratify this season; must renegotiate |
| Partial | Ratifies with one clause in dispute (GM adjudicates) |
| Success | Full ratification |
| Overwhelming | Ratifies + may extract one additional concession |

**Guarantor option:** A third faction offers guarantee (Mandate roll, difficulty 1, to offer). If accepted: each ratifier gains **+1 to M**. Guarantor must sanction any breach (military_advance or Parliamentary Censure within 1 season) or loses Mandate −1.

**BG mode (no personal scene):** Phases 1–3 proceed as Domain Actions. Phase 2 is player negotiation at the table (no roll; this is design space). Grand Debate Zoom In unavailable.

**Hybrid/TTRPG mode:** Stalled negotiation may Zoom In to Grand Debate (social_contest_v30.md) at either party's declaration. The Grand Debate itself remains a **dice social contest** (pools 5–18D; resolver scope boundary). Its outcome modifies the ratification **margin M**: Overwhelming → **+2 M**; Success → **+1 M**; Partial → 0; Failure → **−1 M** (FLOOR 0.05 subsumes the old 'min 1D').

### §3.4 Treaty Effects on Stability

See §1.2 Trigger 2 table. Crown Treaty: see victory_v30.md §3.1.

### §3.5 Casus Belli

Casus Belli (CB) is a formal standing right to act against a specific faction without the usual action economy cost. It is granted by: treaty breach, Outlawry vote, Hafenmark Diplomatic Token override (PP-509 related), or Church Excommunication.

| CB effect | Duration |
|---|---|
| First military_advance against the target: 0 Domain Action slots consumed (free action) | 1 season |
| First military_advance: Ob −1 | 1 season |

CB is consumed upon first use or after 1 season of non-use (expires). A faction may hold multiple CB (one per distinct source). Each is consumed separately.

---

## §4 — NEGOTIATION MECHANICS (EXTENDED)

### §4.1 Faction-Specific Negotiation Bonuses

| Faction | Mechanic | Trigger | Bonus |
|---|---|---|---|
| Crown | Royal Guarantee | Instead of third-party Guarantor | Treaty proceeds without Guarantor; Crown Mandate −1; breach cost doubled |
| Church | Sacred Compact | Both parties consent at signing | Breach triggers Excommunication threat immediately (Mandate −1 to breacher before other costs) |
| Hafenmark | Deed-claim | Prior Intel op documented legal claim | Positioning roll +1D; Ratification Ob −1 |
| Varfell | Diplomatic stratagem | Default | May withhold maximum concession until Phase 2 (Talleyrand-style political reading); Varfell Intel op may expose with Truth roll. Vaynard frames withholding as recognized diplomatic art, not bluff. |
<!-- Niflhel treaty row deleted 2026-04-30 — Niflhel struck per CR-STRIKE-2026-04-19. Settlement-broker intermediary role redirected to settlement_layer §4.7-4.9 — does not appear at faction-treaty layer. -->
| Löwenritter | Deed-presumption fact | Military advantage demonstrated | Before Positioning roll: opponent must offer ≥1 concession first if Löwenritter's stated military fact is accurate |
| Guilds | Commercial leverage | Wealth ≥ 4 | Indemnity concessions count as ×1.5 Wealth value for treaty scoring |

### §4.2 Grand Debate (Hybrid/TTRPG Only)

When negotiations stall (both parties declare irreconcilable demands), either faction may call Grand Debate (Social Priority 6 action, consuming one action slot). Follows params_contest.md structure. See §3.3 for degree effects on ratification.

---

## §5 — PARLIAMENTARY MECHANICS

### §5.1 Definition and Relationship to Existing Actions

Parliament is the collective institutional forum of all active factions. It is distinct from Hafenmark's **Parliamentary Manoeuvre** (existing Standard Action, params_board_game §Standard Action Ob Reference), which is Hafenmark's individual-faction social action for CI suppression and direct influence plays. Parliamentary Manoeuvre remains unchanged.

Parliament adds a collective vote layer: motions that require multiple factions to agree before taking effect.

### §5.2 Phase Placement

**Phase 4 (Social, Priority 4):** Any faction with Mandate ≥ 2 may declare a **Parliamentary Motion** as a Senator action. Declaration consumes the action slot. Multiple motions may be declared by different factions in the same season (max 3 active motions per Accounting).

**Phase 5 Accounting, Step 1.5** (between Step 1 attribute changes and Step 2 Stability checks): Parliamentary votes resolve. Effects applied. Then Step 2 Stability check may fire on any resulting changes.

### §5.3 Vote Mechanics

Each active faction contributes votes equal to its current Mandate. The targeted faction does not vote on motions naming them as subject.

| Threshold | Definition |
|---|---|
| Majority | Strictly > 50% of participating Mandate |
| Supermajority | ≥ 60% of participating Mandate |

Church **Sacred Veto:** Cadence — available once per 4 consecutive seasons (ED-751). Reset triggers on the season when used (e.g., used Season 12 → next available Season 16). Per-Veto-use cooldown, not per-game-year cycle. Free action; costs Mandate −1 if used against a motion that would have passed. Eligible for Veto: Censure, Embargo, Outlawry, Recognition Challenge, Succession Endorsement, Treaty Ratification. Not eligible: War Authorisation, Blockade, Subsidy.

If Church uses Sacred Veto to block a motion that protects Church interests: additional Mandate −1 (self-interested veto is transparent; reputation cost).

**CI institutional weight (cross-ref):** in motions, Church's vote contribution is **Mandate + ⌊CI/20⌋**; a faction voting against Church in a motion targeting Church contributes **max(0, Mandate − ⌊CI/30⌋)** (floored at 0). See ci_political_v30 §3.3/§3.4.

### §5.4 Parliamentary Actions

**[ED-FA-0006, 2026-07-08 — pessimist-action audit DISTILL] The five *punitive* motions below — Censure · Embargo · Blockade · Combined Embargo+Blockade · Outlawry — are one parameterized action, "Parliamentary Sanction," at ascending severity tiers, not five independent mechanics.** They share an identical decision structure — *propose* (at a minimum stat) → *vote* → *apply* a Stability/Wealth/Mandate penalty → *renew-or-lapse* — and differ only in the tier parameters shown in the table (proposer threshold, vote bar, penalty magnitude and duration) plus two tier-specific riders: **Blockade's Military-3 gate** and **Outlawry's "CB granted to all."** The player's choice among them is a severity dial ("how hard to hit this target"), not five qualitatively different moves. The tier names are retained because downstream rules key off them by name — the Sacred Veto eligibility list, the Casus Belli grants, the Guilds' AI vote rule, and the §5.6 Stability→Accord erosion rule all cite specific tiers; this reframe removes the authoring/balance/port cost of five discrete rules, not the tiers or their hooks. The *constructive* motions further down the table (Subsidy, War Authorisation, Treaty Ratification, Recognition Challenge, Succession Endorsement) remain genuinely distinct actions, each with its own object — they are **not** part of this parameterization.

| Action (Parliamentary Sanction tier, then constructive motions) | Proposer min | Vote | Target effect | Proposer cost | Duration | Rescission |
|---|---|---|---|---|---|---|
| **Censure** *(Sanction — Mild)* | Mandate 2 | Majority | Stability −1; Mandate −1 | None | One-time | N/A |
| **Embargo** *(Sanction — Trade)* | Mandate 3 | Majority | Wealth −1/season | Wealth −1/season | Until lifted | Majority |
| **Blockade** *(Sanction — Naval; Military-3 gate)* | Military 3, Mandate 3 | Majority | Wealth −2/season; Stability −1 (once) | Military −1 (garrison) | Until lifted | Majority |
| **Combined Embargo+Blockade** *(Sanction — Total)* | Both | Supermajority | Wealth −2/season; Stability −1/season; Mandate −1 (once) | Wealth −1/season + Military −1 | Until lifted | Supermajority |
| **Outlawry** *(Sanction — Maximal; CB-to-all rider)* | Mandate 5 | Supermajority | Mandate −2; Stability −2; CB granted to all | Mandate −1 | Permanent until petitioned | Supermajority; target Mandate ≥ 3 to petition |
| **Subsidy** *(constructive)* | Mandate 2 | Majority | Recipient Wealth +1 | Wealth −1 | One-time | N/A |
| **War Authorisation** | Military 2 | Majority | Attacker: first military_advance vs target this season is free action (Casus Belli created) | None | 1 season | N/A |
| **Treaty Ratification** | Any signatory | Majority | Treaty binding on all participating factions | None | Permanent until breach | Majority |
| **Recognition Challenge** | Mandate 4 | Supermajority | Target: −1 TCV from victory calculation (no territory change) | Mandate −1 | Until rescinded | Majority |
| **Succession Endorsement** | Mandate 3 | Majority | Endorsed NPC recognised heir; succession Ob −1 | None | Permanent | Supermajority |

**Embargo/Blockade renewal:** Must be renewed annually (Year-End Accounting). Fails to renew = lapses. Proposing faction below minimum Mandate/Military = lapses automatically.

### §5.5 Target Rebuttal

The targeted faction may Rebuttal any Censure or Outlawry vote:

- Declare Rebuttal in Phase 4 (Social, same season as Motion declared) — costs one action slot
- Resolver (params/factions/stats_1_7_scale.md §Domain Action Resolution): **M = Mandate − 2** (Censure) or **M = Mandate − 3** (Outlawry) (legacy: Mandate roll vs Ob 2 / Ob 3)

| Result | Effect |
|---|---|
| Failure | Vote proceeds unmodified |
| Partial | Stability cost halved (round down); Mandate cost unchanged |
| Success | Stability cost negated; Mandate cost halved |
| Overwhelming | Both costs negated; proposer Mandate −1 (reputational damage) + target Stability +1 |

### §5.6 CI Parliament Interaction

Parliamentary actions do NOT directly affect CI.

### §5.6b Turmoil Parliament Interaction

Parliamentary Censure, Embargo, Blockade, and Outlawry reduce target Stability. If Stability drops to ≤ 2, Accord −1 in all territories controlled by that faction (peninsular_strain_v1.md §2.4). Combined Embargo+Blockade (−1 Stability/season ongoing) will erode Accord progressively. Parliament is a legitimacy weapon: sustained institutional pressure degrades governance without triggering battle consequences (no RS cost, no IP cost, no Strain).

Parliamentary vote to lift an Embargo/Blockade: Strain −1 (diplomatic resolution per peninsular_strain_v1.md §4.2). CI changes only through the named CI Accounting formula (Passive, Piety Yield, Assert, Suppress, Hafenmark Structural Suppression). Parliament can indirectly weaken Church (Censure, Embargo) reducing their effective Mandate for Suppress resistance rolls. It cannot directly suppress CI.

### §5.7 Wealth Zero Consequence

When a faction's Wealth reaches 0 at any Accounting:
- Muster (Legionary Inward) action unavailable until Wealth ≥ 1
- Military −1 at each subsequent Accounting while Wealth = 0 (mercenaries unpaid)
- Recovery: any Wealth gain restores the Wealth stat. **Military re-muster (FSS-LOOP-2, 2026-05-30 — resolution-diagnostic ratification; Lesson 5, couple the damper to the degrading dimension):** while **Wealth ≥ 1**, Military restores **+1 per Accounting** (re-muster), up to the Military value the faction held at the Accounting when Wealth **first** reached 0, subject to the normal Muster (Legionary Inward) prerequisites and the ±2 Military seasonal cap. Re-muster does not exceed the pre-collapse value (recovery, not growth). Rationale: the prior rule left Military as a one-way ratchet (Military −1 per Accounting at Wealth 0, with no coupled recovery), so a temporary blockade inflicted **permanent** Military loss — an undamped loop on the Military dimension. Coupling recovery to solvency bounds it. Historical anchor: the early-modern fiscal-military cycle — bankrupt states demobilize and **re-muster when bullion returns** (Spanish Habsburg bankruptcies). Stage-4 sim (2026-05-30): a 3-season blockade takes Military 5 → 2; under the coupled rule it recovers 2 → 5 over the subsequent solvent seasons, vs the prior rule pinning it at 2 permanently.

This makes sustained Blockade + Embargo a serious — but no longer permanently crippling — threat to Guilds and Hafenmark (Wealth-primary factions).

### §5.8 NPC Vote Behavior

GM controls NPC faction votes (Guilds, Niflhel, and any other NPC-only factions).

**Guilds AI vote rule:** Always votes against Blockade and Combined Embargo+Blockade (threatens Wealth). Votes for Subsidy. Votes against Outlawry (commercial unpredictability). Otherwise votes for whichever outcome reduces the highest Mandate faction's power (competitive commercial instinct). **Settlement-broker influence (ED-752):** Guild Council members operating in broker-influenced settlements (per settlement_layer_v30 §4.7-4.9) may shift Guilds' net vote by −1 per influenced settlement (max 2-vote shift), reflecting broker pressure on commercial leadership.

**Niflhel — STRUCK** (per CR-STRIKE-2026-04-19 + PP-DISSOLVE). Settlement-broker NPCs (per settlement_layer §4.7-4.9) do not hold Parliamentary seats and do not vote. The prior Niflhel AI vote rule is dead — no replacement faction-level voting behavior exists for Niflhel. Niflhel's residual influence on Parliamentary outcomes operates through the Guilds settlement-broker mechanism above, not through direct vote. (ED-752)

---

## §6 — OFFICER CAPTURE AND SIGNIFICANT LOSS

### §6.1 Integration with ED-334/335

ED-334 and ED-335 (params_board_game §Command Event) remain canonical for BG and Hybrid BG-layer effects. The new Trigger 5 (§1.2) adds Stability consequences that are ADDITIVE to ED-334/335, not replacements.

### §6.2 Three-Condition Gate (Trigger 5 Full Spec)

**Condition A:** Acting faction Military pool ≥ 4 at time of roll.
**Condition B:** Roll degree = Failure (net ≤ 0).
**Condition C:** At least one: net successes ≤ −2 OR pool ≥ 6 OR named officer NPC attached and capture/death outcome.

All three must be simultaneously true. If any is false, no Stability consequence fires.

### §6.3 Ransom (Integration with ED-334/335)

BG-canonical ransom per ED-334: 2 Wealth per named general, both factions agree.

Per new doc: captured officer costs capturing faction's target Stability −1/season ongoing until ransom paid or resolved.

**Ransom refusal (capturing faction refuses negotiation):** Counts as Subterfuge (Trigger 4 category): capturing faction Stability −1, Mandate −1. This represents violation of the norms of conduct that sustain the military system's legitimacy.

**Maximum capture duration:** If ransom unpaid for 3 seasons, capturing faction must choose: execute (officer killed, Stability −1 additional to displaced faction; capturing faction loses the ransom opportunity) or continue holding.

### §6.4 BG Mode Officer Fate (No Zoom In)

In pure BG mode (no personal scenes): officer fate is resolved per ED-334/335 only. The d10 fate table below applies TTRPG/Hybrid only (when Zoom In to personal scene occurs around the associated battle).

**TTRPG/Hybrid d10 fate table** (roll after mass battle scene resolves, if Trigger 5 gate is met and officer is attached):

| d10 | Outcome |
|---|---|
| 1–4 | Wounded; withdrawn from field. No further consequence this season. |
| 5–7 | Captured. Ransom mechanic activates (§6.3). |
| 8–9 | Killed. Permanent; Stability −1 additional to their faction. |
| 10 | Heroic survival. Morale effect: faction Stability +1. |

---

## §7 — TURN SEQUENCE INTEGRATION REFERENCE

Complete sequence showing where new mechanics sit within existing BG turn structure:

```
PHASE 4 — ACTION RESOLUTION
  Priority 1: Intel/Tribune
  Priority 2: Military/Battle → [Occupation established; Trigger 5 gate checked]
  Priority 3: Domain (Consul, Muster, Govern, Trade, Fortify)
  Priority 4: Social (Senator)
    ├── Parliamentary Motion declarations (consume action slot)
    ├── Hafenmark Parliamentary Manoeuvre (existing, unchanged)
    ├── Treaty initiation (Positioning roll + Concession declaration)
    └── Crown Treaty (PP-512–514/523, unchanged)
  Priority 5: Thread operations
  Priority 6: Special/Unique (Royal Decree, Excommunication, Church Seizure)
  Priority 7: Project advancement

PHASE 5 — SEASONAL ACCOUNTING (10 steps) [ED-678: collapsed from 13, PP-472]
  Step 1:  Apply all pending attribute changes from resolved orders
           Parliamentary votes resolve → Trigger 3 effects applied
           Treaty ratification rolls (Phase 3) → Trigger 2 effects applied
  Step 2:  Accounting Stability check (≥2 attribute loss → resolver, M = Stability − loss magnitude; §1.4)
           Includes Trigger 1–5 and Parliament consequences. Collapse check (§1.5) fires here.
  Step 3:  Cooldown track advance
  Step 4:  Clock advances (RS, CI formula, IP, PI)
           CI formula: Passive +1 → Piety Yield → Assert → Suppress [failure→Stab−1] → Baralta
           Church Prominence update
  Step 5:  Church Attention Pool resolution
           Thread Debt drain; Thread Resonance markers cleared
  Step 6:  Turmoil accounting:
           → Accord checks (garrison, Revolt, passive normalisation)
           → Strain update (battle/Revolt decay, diplomatic resolution)
           → Battle consequence accounting (IP, RS)
  Step 7:  Threshold events / Event Cards; Milestone Bonus check
           Warden Emergence check; Vaynard-Edeyja same-season rule
  Step 8:  Warden Cooperation check; Torben/Elske Loyalty events
  Step 9:  Occupation duration check:
           → 3rd consecutive season Occupation → control transfer; Trigger 1 applies; Accord 1
           → Institutional Consolidation: no Trigger 1–5 this season → Stability +1
  Step 10: Victory condition check (2 consecutive Accounting)
           Season marker advances → Winter: Year-End Accounting
```

---

## §8 — MODE VARIATIONS

### §8.1 BG Mode

- Playable factions: Crown, Church, Hafenmark, Varfell (2–4 players); RM optional (5 players)
- NPC factions: Guilds, Löwenritter (pre-coup), Schoenland, Altonia
- Löwenritter enters as playable faction only after coup (Coup Counter = 4)
- No personal scenes: all mechanics resolve as Domain Actions or Accounting consequences
- Treaty Phase 2 (Concession declaration) = player negotiation at table; no roll
- Grand Debate: unavailable in BG mode
- Officer fate: ED-334/335 only; d10 table not used
- Starting values per mode: see params_board_game (CI=28, PI=7, RS=72)

### §8.2 TTRPG Mode

- No faction-layer victory conditions tracked (narrative campaign)
- All five triggers active
- Personal scenes central; Domain Actions produce consequences via Domain Echo (§3.4 scale_transitions_v30.md)
- Grand Debate available for stalled treaty negotiations
- d10 officer fate table active
- Starting values: CI=0, PI=0, RS=60

### §8.3 Hybrid Mode

- BG strategic layer + TTRPG personal scenes via Zoom In protocol (scale_transitions_v30.md §4)
- Parliament motions may be influenced by personal scene outcomes (Social Contest → Domain Echo → +1D on Rebuttal roll or Ratification roll)
- Treaty stalling may trigger Zoom In to Grand Debate; outcome feeds back as Ratification modifier
- Officer capture: ED-334/335 applies at BG layer; Zoom In resolves personal scene; d10 fate table active
- Both mode starting values active simultaneously (Hybrid uses BG starting values per params_board_game)

---

## §9 — CI FORMULA (FULL, for sim integration)

Complete CI Accounting sequence (Phase 5 Step 4), superseding partial references elsewhere:

1. **Institutional Momentum:** CI +1 (always, cannot be negated below this baseline by player actions; only events can)
2. **Piety Yield:** For each territory where Church Mandate > controlling faction's Mandate (Church Prominent): PT 5 = +1, PT 4 = +0.5 (fractional; accumulated, floored at Year-End). Territories: T9(PT start 5), T6(PT 2), others per params.
3. **Assert** (optional Church action, Phase 4 Priority 6): Influence vs Ob 2. Success: CI +1. Failure: Church Stability −1.
4. **Suppress** (optional opponent action, Phase 4 Priority 4): Mandate vs Ob = floor(Church Mandate/2)+1. Success: negate Step 1 passive this season. Cannot reduce CI below value at season start. **Failure: Stability −1 to suppressing faction.**
5. **Hafenmark Structural Suppression (Baralta):** While Inge Baralta NPC Mandate ≥ 4: CI −1/season automatically. This is Baralta's institutional expertise; requires no action slot. Fires regardless of other suppression.
6. **CI seasonal cap (PP-504):** ±3/season from player-initiated Domain Actions. ±5/season from all sources combined.

---

## §10 — OPEN ITEMS AND EDITORIAL FLAGS

<!-- Updated 2026-04-19 PP-668 — PP-667 resolutions propagated. See designs/audit/gap_resolution_2026-04-19.md §2.4 -->

| ID | Description | Status (PP-667) |
|---|---|---|
| ED-NEW-001 | Casus Belli: consumes on use vs expires after 1 season. | **RESOLVED** — consumes on use. Auto-expires after 3 seasons if unused. |
| ED-NEW-002 | Occupation Partial −1 Ob follow-up attack. | **RESOLVED** — confirmed; −1 Ob next season. |
| ED-NEW-003 | Church Seizure overrides occupation. | **RESOLVED** — confirmed. Occupying faction loses presence but gains Casus Belli against Church. |
| ED-NEW-004 | Parliament Embargo+Blockade: ongoing Stability penalty? | **RESOLVED** — Stability −1/season ongoing while both active. Ends when either ends. |
| ED-NEW-005 | Wealth Zero Military drain per season. | **RESOLVED** — confirmed; −1 Military per season. |
| ED-NEW-006 | Institutional Consolidation recovery: ALL vs ANY unfired. | **RESOLVED** — ALL unfired required. High bar; partial history disqualifies. |
| ED-NEW-007 | Ransom refusal vs ED-334 double-count. | **RESOLVED** — no double-count. Ransom refusal is independent Stability trigger; ED-334 is separate Mandate penalty. They stack because they measure different failures. |
| BALANCE-NEW-001 | Stability recovery pace. | **DEFERRED** to engine_v4 smoke-test. |
| BALANCE-NEW-002 | Blockade + Embargo Guilds/Hafenmark collapse rate. | **DEFERRED** to engine_v4 smoke-test. |
