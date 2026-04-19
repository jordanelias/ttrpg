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
| PARLIAMENT_MANOEUVRE_EXISTING | Parliamentary Manoeuvre is Hafenmark's existing Priority-4 Social action. New Parliament convening is a separate Accounting-phase system. See §5.2 for phase placement. |
| OCCUPATION_TCV_UNSPECIFIED | Occupied territories count 0 TCV for both parties. Control transfer (formal or treaty) required for TCV to count. |

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

**PP-403 exception retained:** Suppress action (TC Accounting formula, params_board_game §TC Generation Step 4) Failure → Stability −1. This is a specific named political commitment failure, not a general action failure.

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
| Niflhel operative exposed and captured | −1 to Niflhel (not target) |

---

#### Trigger 5 — Failed Military Engagement: Significant Losses

Three-condition gate. ALL three must be met simultaneously.

**Condition A — Committed force.** Acting faction's Military pool ≥ 4 at time of roll. (Pool 1–3 = raid/skirmish; no Stability consequence on failure.)

**Condition B — Clear defeat.** Roll degree = Failure (net successes ≤ 0). Partial excluded — disciplined withdrawal, no Stability cost.

**Condition C — Severity threshold.** At least one of:
- Net successes ≤ −2 (rout, not mere repulse)
- Engaged pool ≥ 6 (major-force commitment)
- Named officer NPC attached to action and captured or killed in associated scene

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

Phase 5 Step 2 (existing, params_board_game): any faction with ≥2 attribute points lost this season rolls Stability pool vs Ob = magnitude of total attribute loss.

| Result | Effect |
|---|---|
| Failure | Stability −1 (cascade consequence) |
| Partial | No additional loss |
| Success | No additional loss |
| Overwhelming | Stability +1 (faction rallied under pressure) |

This check fires AFTER Trigger 1–5 consequences are applied. It can fire in the same Accounting as a Trigger event.

---

### §1.5 Faction Collapse Exit Procedure (ED-675)

When a faction's Stability reaches 0 at Accounting end, the faction collapses. This section consolidates and supersedes P-15, P-24, and §9.10 (strategic_layer_v30) as the single canonical collapse procedure.

**Step 1 — Attribute snapshot.** Mandate drops to 0 immediately (political legitimacy is gone). All other attributes (Military, Wealth, Influence) freeze at their current values. The Mandate drop occurs before the freeze.

**Step 2 — Territory transition.** All territories controlled by the collapsed faction become Uncontrolled. Accord in those territories drops to 0 (Revolt state). Units in those territories become Masterless — they hold position but take no orders. Any faction may Claim Masterless units via Domain Action (Military Ob 2; Success: units transfer to claiming faction at current strength; Failure: units disband).

**Step 3 — Officer and NPC fate.** Named officer NPCs of the collapsed faction enter Independent status. They retain their Conviction, Beliefs, and Disposition values. They may be recruited by other factions via Social Contest (Ob = Leadership Deviation Ob + 2). Unrecruited officers remain in their home settlement as unaffiliated NPCs and may initiate independent actions per npc_behavior_v30 §4.2.

**Step 4 — Player character transition.** A player character affiliated with the collapsed faction loses all faction dice bonuses (Standing-derived). Standing is preserved as a historical record but grants no mechanical benefit. The player continues as an unaffiliated character. Options:

| Path | Requirement | Mechanical effect |
|---|---|---|
| Join another faction | That faction's Standing 0 initiation gate | Begin at Standing 0 in new faction; old Standing irrelevant |
| Reconstitute collapsed faction | Influence Domain Action, Ob 4, repeated 3 seasons consecutively | Faction re-emerges at Stability 1, Mandate 1, other attributes at 50% of frozen values (round down). Player becomes faction leader. Requires at least 1 territory held or recaptured. |
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
| Accord | Frozen at pre-Occupation value (population loyalty suspended during military contest) | N/A (occupier has no Accord — not yet the controller) |

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

- Pool: Influence
- Ob: floor(occupying faction Mandate / 2) + 1
- Success: Occupation marker removed (territory ungovernable — occupier withdraws)
- Failure: Occupation persists
- Overwhelming: marker removed AND occupying faction Stability −1 (costly suppression)

### §2.6 Political Vacuum Interaction (PP-500 Integration)

Political Vacuum (PP-500) applies when a faction is eliminated. During Vacuum (1 season): no faction may establish Occupation; no march-in; Fort retained. After Vacuum lifts: territory becomes Uncontrolled; normal march rules apply. **Occupation can only be placed on CONTROLLED territories.** Uncontrolled territories may be claimed (free march, no Battle roll).

### §2.7 Church Seizure and Occupation (Integration)

Church Graduated Seizure (victory_v30.md §3.2) is a legal/spiritual transfer mechanism distinct from military occupation. If Church declares Seizure on a territory currently under Occupation by another faction:

- Seizure roll proceeds normally (Influence + floor(TC/15) vs Ob = 7 − PT)
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

**Phase 1 — Positioning roll.**
Both parties roll Influence vs Ob 2. Higher net successes controls opening terms (sets first demand). Tie: higher current Mandate controls.

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

**Phase 3 — Ratification roll.**
Each signatory rolls Mandate vs Ob 2.

| Result | Effect |
|---|---|
| Failure | Cannot ratify this season; must renegotiate |
| Partial | Ratifies with one clause in dispute (GM adjudicates) |
| Success | Full ratification |
| Overwhelming | Ratifies + may extract one additional concession |

**Guarantor option:** A third faction offers guarantee (Mandate roll Ob 1 to offer). If accepted: both ratification rolls +1D. Guarantor must sanction any breach (military_advance or Parliamentary Censure within 1 season) or loses Mandate −1.

**BG mode (no personal scene):** Phases 1–3 proceed as Domain Actions. Phase 2 is player negotiation at the table (no roll; this is design space). Grand Debate Zoom In unavailable.

**Hybrid/TTRPG mode:** Stalled negotiation may Zoom In to Grand Debate (social_contest_v30.md) at either party's declaration. Grand Debate outcome modifies ratification roll: Overwhelming → +2D; Success → +1D; Partial → 0; Failure → −1D (min 1D).

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
| Varfell | Concealed bottom line | Default | May bluff Phase 2 minimum concession; Niflhel or Varfell Intel op may expose (Truth roll) |
| Niflhel | Intermediary standing | Always | Not listed as signatory; broker role; takes Stability −1 if brokered treaty collapses |
| Löwenritter | Deed-presumption fact | Military advantage demonstrated | Before Positioning roll: opponent must offer ≥1 concession first if Löwenritter's stated military fact is accurate |
| Guilds | Commercial leverage | Wealth ≥ 4 | Indemnity concessions count as ×1.5 Wealth value for treaty scoring |

### §4.2 Grand Debate (Hybrid/TTRPG Only)

When negotiations stall (both parties declare irreconcilable demands), either faction may call Grand Debate (Social Priority 6 action, consuming one action slot). Follows params_contest.md structure. See §3.3 for degree effects on ratification.

---

## §5 — PARLIAMENTARY MECHANICS

### §5.1 Definition and Relationship to Existing Actions

Parliament is the collective institutional forum of all active factions. It is distinct from Hafenmark's **Parliamentary Manoeuvre** (existing Standard Action, params_board_game §Standard Action Ob Reference), which is Hafenmark's individual-faction social action for TC suppression and direct influence plays. Parliamentary Manoeuvre remains unchanged.

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

Church **Sacred Veto:** May cancel any non-military Parliamentary vote once per year (free action; costs Mandate −1 if used against a motion that would have passed). Eligible for Veto: Censure, Embargo, Outlawry, Recognition Challenge, Succession Endorsement, Treaty Ratification. Not eligible: War Authorisation, Blockade, Subsidy.

If Church uses Sacred Veto to block a motion that protects Church interests: additional Mandate −1 (self-interested veto is transparent; reputation cost).

### §5.4 Parliamentary Actions

| Action | Proposer min | Vote | Target effect | Proposer cost | Duration | Rescission |
|---|---|---|---|---|---|---|
| **Censure** | Mandate 2 | Majority | Stability −1; Mandate −1 | None | One-time | N/A |
| **Embargo** | Mandate 3 | Majority | Wealth −1/season | Wealth −1/season | Until lifted | Majority |
| **Blockade** | Military 3, Mandate 3 | Majority | Wealth −2/season; Stability −1 (once) | Military −1 (garrison) | Until lifted | Majority |
| **Combined Embargo+Blockade** | Both | Supermajority | Wealth −2/season; Stability −1/season; Mandate −1 (once) | Wealth −1/season + Military −1 | Until lifted | Supermajority |
| **Outlawry** | Mandate 5 | Supermajority | Mandate −2; Stability −2; CB granted to all | Mandate −1 | Permanent until petitioned | Supermajority; target Mandate ≥ 3 to petition |
| **Subsidy** | Mandate 2 | Majority | Recipient Wealth +1 | Wealth −1 | One-time | N/A |
| **War Authorisation** | Military 2 | Majority | Attacker: first military_advance vs target this season is free action (Casus Belli created) | None | 1 season | N/A |
| **Treaty Ratification** | Any signatory | Majority | Treaty binding on all participating factions | None | Permanent until breach | Majority |
| **Recognition Challenge** | Mandate 4 | Supermajority | Target: −1 TCV from victory calculation (no territory change) | Mandate −1 | Until rescinded | Majority |
| **Succession Endorsement** | Mandate 3 | Majority | Endorsed NPC recognised heir; succession Ob −1 | None | Permanent | Supermajority |

**Embargo/Blockade renewal:** Must be renewed annually (Year-End Accounting). Fails to renew = lapses. Proposing faction below minimum Mandate/Military = lapses automatically.

### §5.5 Target Rebuttal

The targeted faction may Rebuttal any Censure or Outlawry vote:

- Declare Rebuttal in Phase 4 (Social, same season as Motion declared) — costs one action slot
- Roll: Mandate vs Ob 2 (Censure) or Ob 3 (Outlawry)

| Result | Effect |
|---|---|
| Failure | Vote proceeds unmodified |
| Partial | Stability cost halved (round down); Mandate cost unchanged |
| Success | Stability cost negated; Mandate cost halved |
| Overwhelming | Both costs negated; proposer Mandate −1 (reputational damage) + target Stability +1 |

### §5.6 TC Parliament Interaction

Parliamentary actions do NOT directly affect TC.

### §5.6b Peninsular Strain Parliament Interaction

Parliamentary Censure, Embargo, Blockade, and Outlawry reduce target Stability. If Stability drops to ≤ 2, Accord −1 in all territories controlled by that faction (peninsular_strain_v1.md §2.4). Combined Embargo+Blockade (−1 Stability/season ongoing) will erode Accord progressively. Parliament is a legitimacy weapon: sustained institutional pressure degrades governance without triggering battle consequences (no RS cost, no IP cost, no Strain).

Parliamentary vote to lift an Embargo/Blockade: Strain −1 (diplomatic resolution per peninsular_strain_v1.md §4.2). TC changes only through the named TC Accounting formula (Passive, Piety Yield, Assert, Suppress, Hafenmark Structural Suppression). Parliament can indirectly weaken Church (Censure, Embargo) reducing their effective Mandate for Suppress resistance rolls. It cannot directly suppress TC.

### §5.7 Wealth Zero Consequence

When a faction's Wealth reaches 0 at any Accounting:
- Muster (Legionary Inward) action unavailable until Wealth ≥ 1
- Military −1 at each subsequent Accounting while Wealth = 0 (mercenaries unpaid)
- Recovery: any Wealth gain restores stat; Military stat does not auto-recover (must be re-mustered)

This makes sustained Blockade + Embargo an existential threat to Guilds and Hafenmark (Wealth-primary factions).

### §5.8 NPC Vote Behavior

GM controls NPC faction votes (Guilds, Niflhel, and any other NPC-only factions).

**Guilds AI vote rule:** Always votes against Blockade and Combined Embargo+Blockade (threatens Wealth). Votes for Subsidy. Votes against Outlawry (commercial unpredictability). Otherwise votes for whichever outcome reduces the highest Mandate faction's power (competitive commercial instinct).

**Niflhel AI vote rule:** Votes against Outlawry (network exposure). Votes against Recognition Challenge (legitimacy destabilisation creates unpredictable clients). Abstains on War Authorisation. Otherwise votes for the motion that most benefits the weakest active faction (network dependency protection).

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
  Step 2:  Accounting Stability check (≥2 attribute loss → Stability pool roll vs Ob)
           Includes Trigger 1–5 and Parliament consequences. Collapse check (§1.5) fires here.
  Step 3:  Cooldown track advance
  Step 4:  Clock advances (RS, TC formula, IP, PI)
           TC formula: Passive +1 → Piety Yield → Assert → Suppress [failure→Stab−1] → Baralta
           Church Prominence update
  Step 5:  Church Attention Pool resolution
           Thread Debt drain; Thread Resonance markers cleared
  Step 6:  Peninsular Strain accounting:
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
- NPC factions: Guilds, Niflhel, Löwenritter (pre-coup), Schoenland, Altonia
- Löwenritter enters as playable faction only after coup (Coup Counter = 4)
- No personal scenes: all mechanics resolve as Domain Actions or Accounting consequences
- Treaty Phase 2 (Concession declaration) = player negotiation at table; no roll
- Grand Debate: unavailable in BG mode
- Officer fate: ED-334/335 only; d10 table not used
- Starting values per mode: see params_board_game (TC=28, PI=7, RS=72)

### §8.2 TTRPG Mode

- No faction-layer victory conditions tracked (narrative campaign)
- All five triggers active
- Personal scenes central; Domain Actions produce consequences via Domain Echo (§3.4 scale_transitions_v30.md)
- Grand Debate available for stalled treaty negotiations
- d10 officer fate table active
- Starting values: TC=0, PI=0, RS=60

### §8.3 Hybrid Mode

- BG strategic layer + TTRPG personal scenes via Zoom In protocol (scale_transitions_v30.md §4)
- Parliament motions may be influenced by personal scene outcomes (Social Contest → Domain Echo → +1D on Rebuttal roll or Ratification roll)
- Treaty stalling may trigger Zoom In to Grand Debate; outcome feeds back as Ratification modifier
- Officer capture: ED-334/335 applies at BG layer; Zoom In resolves personal scene; d10 fate table active
- Both mode starting values active simultaneously (Hybrid uses BG starting values per params_board_game)

---

## §9 — TC FORMULA (FULL, for sim integration)

Complete TC Accounting sequence (Phase 5 Step 4), superseding partial references elsewhere:

1. **Institutional Momentum:** TC +1 (always, cannot be negated below this baseline by player actions; only events can)
2. **Piety Yield:** For each territory where Church Mandate > controlling faction's Mandate (Church Prominent): PT 5 = +1, PT 4 = +0.5 (fractional; accumulated, floored at Year-End). Territories: T9(PT start 5), T6(PT 2), others per params.
3. **Assert** (optional Church action, Phase 4 Priority 6): Influence vs Ob 2. Success: TC +1. Failure: Church Stability −1.
4. **Suppress** (optional opponent action, Phase 4 Priority 4): Mandate vs Ob = floor(Church Mandate/2)+1. Success: negate Step 1 passive this season. Cannot reduce TC below value at season start. **Failure: Stability −1 to suppressing faction.**
5. **Hafenmark Structural Suppression (Baralta):** While Inge Baralta NPC Mandate ≥ 4: TC −1/season automatically. This is Baralta's institutional expertise; requires no action slot. Fires regardless of other suppression.
6. **TC seasonal cap (PP-504):** ±3/season from player-initiated Domain Actions. ±5/season from all sources combined.

---

## §10 — OPEN ITEMS AND EDITORIAL FLAGS

| ID | Description | Status |
|---|---|---|
| ED-NEW-001 | Casus Belli: confirm CB consumes on use vs expires after 1 season | PROVISIONAL |
| ED-NEW-002 | Occupation Partial (contested foothold): confirm −1 Ob for follow-up attack | PROVISIONAL |
| ED-NEW-003 | Church Seizure on Occupied territory: confirm Seizure overrides occupation marker | PROVISIONAL |
| ED-NEW-004 | Parliament Combined Embargo+Blockade: confirm Stability −1/season ongoing (not one-time) | PROVISIONAL |
| ED-NEW-005 | Wealth Zero Military drain: confirm −1 Military per season (not per Accounting) | PROVISIONAL |
| ED-NEW-006 | Institutional Consolidation recovery: confirm +1 Stability only if ALL triggers 1–5 unfired vs ANY unfired | FLAGGED |
| ED-NEW-007 | Ransom refusal = Subterfuge: confirm this doesn't double-count with existing ED-334 NPC-kill rule | FLAGGED |
| BALANCE-NEW-001 | Stability recovery (+1 clean season) may make long campaigns too stable. Simulation required. | Simulation pending |
| BALANCE-NEW-002 | Blockade + Embargo combined could eliminate Guilds/Hafenmark within 4 seasons from Wealth 0. Confirm intended. | Simulation pending |
