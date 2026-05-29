## Stats (1–7 scale)

Legitimacy / Popular_Support / Influence / Wealth / Military / Intel / Stability

The 7-stat schema. Intel restored as canonical 6th stat (between Military and
Stability) per ED-787 Position A 2026-05-03 — c2effdd Renaissance political-
infrastructure review carried; ED-748 STRUCK ruling overridden. Spy Ob formula
`floor(target Intel / 2) + 1` is no longer broken; institutional intelligence
capacity is now a faction-level mechanical axis (ED-787 closure rationale: see
designs/audit/2026-05-01-stage-10-validation/05_ED-755_resolutions.md §3.1
Addendum).

Seasonal cap: ±2 per stat per season (TTRPG); ±varies (BG — see accounting).

## Starting Stats

| Faction | L (TTRPG) | PS (TTRPG) | L (BG) | PS (BG) | I | W (TTRPG) | W (BG) | Mil | Int | Sta |
|---------|-----------|------------|--------|---------|---|-----------|--------|-----|-----|-----|
| Crown | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 4 |
| Church | 5 | 5 | 5 | 5 | 6 | 5 | 5 | 4 | 4 | 5 |
| Hafenmark | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 3 | 4 |
| Varfell | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| Guilds | 3 | 3 | 3 | 3 | 4 | 6 | 6 | 2 | 4 | 5 |
| Restoration Movement | — | — | — | — | — | — | — | — | — | No faction stats (PP-460). Operates via Presence markers and Community Weaving. Victory via Cultural Uprising of T9 Himmelenger. |
| Löwenritter | — | — | 3 | 3 | 2/3 | — | — | 5/6 | 3 | 5/4 |

**Intel column rationale (ED-787 closure 2026-05-03, Position A applied):**

| Faction | Int | Rationale |
|---------|-----|-----------|
| Crown | 3 | Royal court has some intelligence capacity but not a priority. |
| Church | 4 | Inquisition + nuncio network — institutional intelligence woven into existing diocesan and missionary infrastructure. |
| Hafenmark | 3 | Merchant intelligence (trade routes are information routes), but not institutionalized as primary capability. |
| Varfell | 4 | Pragmatic intelligence use (opportunist/revolutionary) but NOT specialist-themed. The Renaissance review proposed 5 framing Varfell as the Venice-analogue intel-superior faction; ED-787 closure (per Jordan 2026-05-03) revises to 4: Varfell is "press whatever advantage possible" — uses information pragmatically — not the institutionalized intel apparatus that 5 would imply. Their identity axes are anti-Altonian and caste-system-breaking, not intelligence-themed. |
| Löwenritter | 3 | Military order, modest intelligence infrastructure (already authored — pre-ED-787, retained). |
| Guilds | 4 | Trade networks provide intelligence; commercial information flows institutionalize partial intel capacity. |

**Mechanical roles for Intel (per Renaissance review — now restored):**

- **Defensive intelligence** (counter-espionage): `Spy Ob = floor(target Intel / 2) + 1`. Previously broken (referenced struck stat); now operational.
- **Offensive intelligence quality**: Investigate/Intel pool = Intel (not flat Influence as fallback).
- **Counter-espionage detection** at Intel ≥ 4: on enemy Spy attempt in your territory, roll Intel vs Ob 3. Success = you learn the spy action occurred (not its result).
- **Strategic fog**: without successful Intel action, enemy faction stats are hidden. Intel reveals them.

Note: Varfell BG L 4 / PS 4 (post PP-686 v2 split, seed equal per factions_personal.md / faction_behavior_v30 §3.4-3.5) / Wealth 4 is intentional (political isolation at game start, not their full institutional depth). Pre-existing inconsistency: an earlier version of this footnote said "Mandate 3 / Wealth 3" while the Starting Stats table above shows Varfell BG Mandate 4 / Wealth 4. The table is authoritative; this note now matches. [TODO: confirm with Jordan if intent was 3 (footnote) or 4 (table) — flagged as part of ED-784 Phase 2 sweep, not blocking.]

## Clock Starting Values

| Clock | TTRPG | BG (bg_v05 P-32) | Shared Loss |
|-------|-------|-----------------|-------------|
| Church Influence | 0 | 28 | — |
| Mending Stability | 60 | 72 | Mending Stability = 0 |
| Institutional Pressure | 20 | 20 | — |
| Public Instability | — | 5 | — |

## Domain Action Resolution (deterministic+stochastic) — CANONICAL (ED-865/874, ratified 2026-05-29)

**This is the canonical resolution method for faction Domain Actions and bare-stat faction checks.** It supersedes the bare-stat-pool-vs-Ob dice approach (retained below for legacy/Zoom-In reference only). Jordan-directed ratification of the Stage-1/4/5-tested candidate (`designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md`).

**Why deterministic+stochastic.** The bare-stat d10 pool gave neither legible odds nor uniform leverage at the small pools faction stats produce (1–7), making *noise* decisive on pivotal, irreversible outcomes where structure should be. Validated against precedent (Stage 5): the COIN / political-contest literature (`ners_historical_precedent_matrix.md` entry 2) finds real seizures/votes/coups are **structure-decisive with a stochastic tail, not low-variance coin-flips** — exactly what this resolver produces. It also restores consistency with the faction layer's deterministic-accounting spine.

**Resolver.**

```
margin  M = acting_stat − difficulty
   difficulty = the contested target's relevant stat (contested actions),
                OR a fixed action-difficulty rating (non-contested actions).
   Legacy Ob mapping: an action previously "vs Ob O" has difficulty D = max(1, (O−1)·2).

P_success(M)        = clamp(0.50 + 0.10·M, 0.05, 0.90)            # at-least-Success
P_overwhelming(M)   = clamp(0.50 + 0.10·M − 0.35, 0, 0.55)
P_atleast_partial   = clamp(0.50 + 0.10·M + 0.20, P_success, 0.97)

draw r ~ U[0,1)  (lower = better):
   r < P_overwhelming                     → Overwhelming
   P_overwhelming ≤ r < P_success         → Success
   P_success ≤ r < P_atleast_partial      → Partial
   r ≥ P_atleast_partial                  → Failure
```

**Canonical parameters** (ratified; tunable by future Jordan-logged ratification): BASE 0.50 (even contest is fair), SLOPE **0.10 — leverage is +10% per stat-point of margin, CONSTANT across the whole 1–7 range** (this is what closes the σ-leverage non-uniformity, ED-874; no dice pool can — leverage ∝ 1/√N is irreducible for pools), FLOOR 0.05 (punching-up is hard but never impossible — fixes the ~1% wall), CAP 0.90 (overmatch reliable but never certain), plus the band offsets above. Live leverage zone M ∈ [−4, +4]; beyond, FLOOR/CAP clamp.

**Output is unchanged.** The resolver emits the same four-degree ladder (Failure/Partial/Success/Overwhelming) the dice system did, so Domain Echo (`scale_transitions_v30` §5: Success +1, Overwhelming +2, cap ±2) and all cost tables are untouched — only the resolution *method* changes.

**Governed checks (migration, ratified 2026-05-29).** The following faction bare-stat checks resolve via this method, with their named outcome-hooks preserved on the corresponding degree:
- **All faction Domain Actions** (Assert, Reconstitute, Govern, Claim Masterless, etc.). Assert: M = Influence − 2 (legacy Ob 2 → difficulty 2). Reconstitute: M = Influence − 6 (legacy Ob 4 → difficulty 6).
- **Suppress** — M = Mandate − (Church-L difficulty); **Failure → Stability −1 retained** (the PP-403 named exception attaches to the resolver's Failure degree).
- **Parliamentary Rebuttal** — **Overwhelming → +1 effect retained** (attaches to the resolver's Overwhelming degree).
- **§1.4 Accounting Stability Check** — M = Stability − loss_magnitude; resolves via this method. **Co-designed with §1.3 Institutional Consolidation recovery (CC-4):** §1.4 is the cascade-DAMAGE check (Failure → −1); §1.3 is the deterministic clean-season +1 recovery. They operate on different triggers and do not double-count.

**Scope boundary.** This method governs **bare-stat faction checks only.** Healthy dice systems — personal combat, social contest (pools 5–18D), aggregated mass battle — **remain dice** (NERS-N/E: replacing them would add complexity without fixing a defect). Trigger-5 (mass-battle resolution, ED-876) is dice and **orthogonal** to this resolver.

## Domain Action Rules (TTRPG) — SUPERSEDED for faction Domain Actions (legacy / Zoom-In reference)

> **[SUPERSEDED 2026-05-29, ED-865/874]** For faction Domain Actions, the deterministic+stochastic resolver above is canonical. The bare-stat-pool-vs-Ob method below is retained only as the legacy reference and for any explicit TTRPG-era Zoom-In context.

Ob = floor(relevant stat / 2) + 1.
Attacker bonus dice: own faction's relevant stat if holding faction leadership.
Non-Player Character faction rolls: relevant stat as d10 pool, TN 7.

## CI Passive Advance (PP-402)

Church Influence (CI) advances by **+1 per season** from institutional momentum, regardless of Church action.
Applied at Accounting before Assert/Suppress resolution.

| Action | CI effect |
|--------|-----------|
| Passive baseline | +1 (always) |
| Assert (Church) | +2 total (replaces passive; not additive) |
| Suppress (Crown or Hafenmark Domain Action) | Negates passive +1 for that season only. CI does not decrease. Ob = floor(Church L / 2) + 1 ÷ 2 (round up, min 1). |

Suppress may be declared once per season by one faction. It cannot reduce CI below its value at season start.
TTRPG: same rule applies. BG: same rule applies; Suppress is a Standard Action consuming one card.

## Failed Domain Action Stability Cost (PP-403)

A Domain Action that results in **Failure** (net successes ≤ 0) costs the acting faction **−1 Stability**.
Partial success (net > 0 but < Ob): no Stability cost.
Success/Overwhelming: normal effect, no cost.

**Scope exclusions:**
- Does not apply to self-improvement Domain Actions (acting faction targeting own stats).
- Does not apply to TTRPG personal scene rolls or Thread operations.
- Does not apply to Restoration Movement (RM has no Stability — PP-460).
- Applies to faction-layer Domain Actions only.

**Stability 1 edge case:** If Stability is already 1, a Failure reduces it to 0, triggering an immediate Stability Check (existing mechanic). Factions with low Stability are further discouraged from sub-threshold gambles.

## ~~Ethical Framework Ob Modifiers~~ — SUPERSEDED 2026-05-02 (PP-686 v2 / ED-784)

<!-- [SUPERSEDED 2026-05-02 — SUPERSESSION-PP686-002] Replaced by triadic decomposition in designs/provincial/faction_behavior_v30.md §3.7: mission_alignment_modifier + cascade_alignment_modifier + expectation_alignment_modifier, clamped at ±2 (was ±3 — sim v2 confirmed ±3 produced dominant-strategy at high alignment). Strictness functions only as deviation-cost modulator (Crown Policy gate). See ED-784, params/bg/core.md (struck 2026-05-01 SUPERSESSION-PP686-001), params/factions_personal.md (struck 2026-05-01 same supersession), and audit §2.1. Retained below struck for patch-history reference only — do not implement. -->

~~| Condition | Modifier |~~
~~|-----------|---------|~~
~~| Action aligned with framework | −1 Ob |~~
~~| Action contradicts framework | +1 Ob |~~
~~| Church only: reveals Thread truth | +2 Ob |~~

## Leadership Deviation Stability Check Obs

Crown: 2 | Church: 3 | Hafenmark: 2 | Varfell: 2 | Guilds: 2 | Restoration Movement: 2 | Löwenritter: 2

## Unique Actions (TTRPG, from stage6)

| Faction | Action | Roll | Effect |
|---------|--------|------|--------|
| Crown | Royal Decree | L vs Ob 2 | One faction stat ±1 immediate. Consecutive: +1 Ob/season. Cannot target Intel. |
| Church | Excommunication | L vs target L (leader) / Ob 2 (non-leader) | Strips Circles bonus; target faction L −1. Reversal: Grand Debate (5 exchanges) or new Confessor. |
| Church | Church Influence 60 Territorial Seizure | L vs floor(owner's L / 2) + 1 | Per-territory roll. Success: administrative control. Failure: Church L −1. |
| Restoration Movement | Community Weaving | Presence markers −1 Ob (base Ob 2) | Mending PS prerequisite: PS ≥ 1 |
| [Others] | See stage6_factions.md §8.4–8.9 | — | Hafenmark, Varfell, Guilds, Löwenritter unique actions not extracted |

## Nine Political Axes (qualitative — not tracked numerically)

1. Sovereignty: Crown authority vs Church authority
2. Knowledge: Thread truth accessible vs suppressed
3. Legitimacy: Constitutional monarchy vs Theocratic governance
4. Cultural identity: Einhir recovery vs Colonial settlement
5. Economic control: Guild autonomy vs State/Church taxation
6. Military authority: Ducal/Crown vs Templar independence
7. Information: Transparency vs Secrecy
8. External threat: Accommodation vs Resistance to Altonia
9. Ontological: World as it appears vs World is more

## Faction Non-Player Character Trigger Conditions (key)

| Non-Player Character | Trigger | Effect |
|-----|---------|--------|
| Ehrenwall | Coup trigger | Martial Law; Crown Loyalty check |
| Vaynard | TK threshold | Research acceleration |
| Baralta | Church Influence suppression | Church L −1/season while Baralta L ≥ 4 |
| Schoenland | Active spoiler | Various faction disruptions |

Mending Stability ≤ 10 adds +1 to coup/succession trigger check pools.

## Unique Actions — All Factions (PP-168)

### Crown — Royal Decree
Roll: L vs Ob 2. Once per season.
| Degree | Result |
|--------|--------|
| Overwhelming | One faction stat ±1 immediate; consecutive seasons: +1 Ob/season |
| Success | One faction stat ±1 immediate; consecutive seasons: +1 Ob/season |
| Failure | — |
Cannot target Intel. Effect is immediate and unilateral.

### Church — Excommunication
Roll: L vs floor(target L / 2) + 1 (faction leader) or Ob 2 (non-leader).
| Degree | Result |
|--------|--------|
| Success | Strips target's Circles bonus; target faction L −1 |
| Failure | — |
Reversal: Grand Debate (5 exchanges) or new Confessor appointed.

### Church — CI 60 Territorial Seizure
Trigger: Church Influence (CI) reaches 60. Fires once per territory.
Roll: L vs floor(owner's L / 2) + 1.
| Degree | Result |
|--------|--------|
| Success | Administrative control of territory. Domain Actions vs Church authority require +2 Ob. Flat Church Influence value fires immediately. |
| Failure | Church L −1 |
Riskbreaker exposure removes seized territory and prevents re-seizure for one season.

### Hafenmark — Sovereign Authority Doctrine
Roll: L vs Ob 4. Once per campaign arc.
| Degree | Result |
|--------|--------|
| Overwhelming | Church Influence −3; Church L −1; Heresy Investigation blocked this season; +1D social vs Church for the arc |
| Success | Church Influence −2; Church L −1; Heresy Investigation opens (Ob 4 to pursue) |
| Partial | Church Influence −1; Heresy Investigation opens immediately; Church Influence +1 |
| Failure | Church Influence +1; Heresy Investigation immediate; Baralta's L −1 |
CI Suppression: while Baralta's L ≥ 4, Church Influence −1/season. Suppression ends if L < 4 or excommunication (CI +4 immediately).

### Varfell — The Private Collection
Roll: Intel vs Ob 2. Once per season.
| Degree | Result |
|--------|--------|
| Success (choose one) | +2D to one Thread-related Domain Action this season; OR reveal one hidden faction attribute; OR −1 Ob to one Einhir Research action this season |
| Failure | Artefact's Thread signature detected by a practitioner; Church Intel +1D vs Varfell for 1 season; Thread Tension +1 |
Long-term cost: each use: +1 to Vaynard's hidden Thread Sensitivity (TS). At Thread Sensitivity 14+, each use triggers Spirit check TN 7 Ob 1 for a Discovery Event.
Player Character takeover: collection transfers as institutional asset; triggers mandatory Discovery Event for new leader (Spirit TN 7 Ob 1; Success: Thread Knowledge (TK) +1; Failure: Certainty −1, new Belief offered).

### Guilds — Economic Leverage
Trigger: Guild Favour ≥ 5 in target territory (1–7 territory track).
Roll: Wealth vs target faction's Wealth.
| Degree | Result |
|--------|--------|
| Overwhelming | Target loses 1 Wealth + 1 Prosperity in that territory |
| Success | Target faction loses 1 Wealth for 1 season |
| Failure | Guild Favour −1 in that territory |
Cannot target factions in territories where Guild Favour < 5.

<!-- §Niflhel — The Quiet Network deleted 2026-04-30 — was STRUCK per conflict_architecture_proposal §Niflhel Dissolution. Functions distributed to settlement-level intelligence brokers (settlement_layer §4.7-4.9). -->


### Restoration Movement — Community Weaving [SUPERSEDED by PP-616]

> **SUPERSEDED:** This spec is superseded by `params/threadwork.md` PP-616 (Community Organizing — Canonical Pool). PP-616 unifies all Thread operations under a single pool formula: `(Spirit × 2) + History + TPS`, supersedes the Influence-pool framing, replaces Thread Tension effect with direct MS effect, and removes the Domain Action framing ("Not a Domain Action — a Thread operation"). Co-Movement card draw per P-01 remains canonical. Retained below for patch-history reference only — do not implement.

Roll: Influence vs Ob = Thread Tension ÷ 20 (round up).
Requires: at least one practitioner with Thread Sensitivity (TS) 30+ affiliated with the Restoration Movement.
| Degree | Result |
|--------|--------|
| Overwhelming | Thread Tension −2 |
| Success | Thread Tension −1 |
| Partial | Thread Tension unchanged; Stability −1 |
| Failure | Stability −1; Thread Tension +1 |
Co-Movement Card drawn on every result (P-01 compliance).
Prerequisite: PS ≥ 1 for Mending prerequisite (see stage6 §8.8).

### Löwenritter — Martial Law / Coup Trigger
No standard Unique Action roll — Löwenritter action is triggered by Graduated Autonomy reaching 4.
**Graduated Autonomy increments (+1 each):**
- Church Influence reaches 40 while Crown took no action to reduce it that season
- Torben's loyalty reaches 3–2 or lower
- Crown loses 2+ territories in one season without a military response Domain Action
Counter never decrements. Fires at next seasonal accounting once at 4. (PP-577: threshold unified to 4, per params_board_game canonical)
**Martial Law effects:** All non-Military Domain Actions in Crown territories require secondary Military check (Löwenritter Military pool, TN 7, Ob 2); failure blocks the action. Persists until players remove it (Influence vs Ob = Löwenritter Military ÷ 2, round up, min Ob 3) or Church Influence drops below 40.

## Mandate Recovery (L + PS independently, ED-066b resolved — provisional, post PP-686 v2)

Factions with L < starting value recover +1 L/season AND factions with PS < starting value recover +1 PS/season independently when:
- No hostile Domain Action targeting that faction this season
- Stability ≥ 2
Cap: neither L nor PS can recover above its starting value via this mechanic. [PROVISIONAL]

## Hafenmark Wealth Sink (ED-064b resolved — provisional)

Wealth above 5 may be spent as bonus dice on trade-adjacent Domain Actions:
- 1 Wealth token → +1D on Trade or Diplomacy Domain Action (max +2D per action)
- Token is consumed on spend
[PROVISIONAL]

## Military Stat Change on Unit Destruction (ED-017 resolved — provisional)

When a unit is destroyed in TTRPG mass combat: Faction Military −1 (immediate). Cap: −2 per season from destruction. [PROVISIONAL]

## Military Seasonal Cap (ED-039 resolved — provisional)

Military stat cap: ±2/season from all Domain Actions combined. Hard cap = faction Military rating (cannot exceed starting value +1 via Domain Actions alone). [PROVISIONAL]

## Institutional Mandate Trigger (L-only per audit Q2; ED-003 resolved — provisional)

Institutional Mandate (L) fires when:
- Faction L ≥ 4, AND
- A Domain Action directly challenges the faction's core institutional authority:
  Crown: sovereignty or legal authority; Church: spiritual authority or excommunication power;
  Guilds: trade monopoly or taxation; Hafenmark: guild autonomy; Varfell: territorial governance;
  Restoration: community organizing; Löwenritter: military authority.
[PROVISIONAL]

## PC Faction Embedding — BG Layer (ED-075 resolved — provisional)

PCs are always mechanically present in their primary faction between Zoom Ins.
Effect: the PC's faction gains +1D on one Domain Action per season in territories the PC is physically located in (narrative confirmation required). [PROVISIONAL]

## Institutional Mandate — Uphold / Appease (PP-189; L-only per audit Q2)

Trigger: L ≥ 4 AND Domain Action directly challenges faction core institutional authority.
| Choice | Timing | Effect | Cost |
|--------|--------|--------|------|
| Uphold | Before roll | Roll proceeds | None |
| Appease | Before roll | Action cancelled | L −1 |
NPC: Appease if L ≥ 4 AND Stability ≤ 3.

## Community Weaving — Procedure (PP-195) [SUPERSEDED by PP-616]

> **SUPERSEDED:** This procedure is superseded by `params/threadwork.md` PP-616 (Community Organizing — Canonical Pool). PP-616 changes: (1) pool formula from `Mandate + History` to `(Spirit × 2) + History + TPS` unifying all Thread operations; (2) removes Domain Action framing — Community Organizing is a Thread operation, not a DA ("One per contact window round. Not a Domain Action."); (3) removes the Failure → Mandate −1 consequence. PS ≥ 1 prerequisite retained (Mending PS). The [PROVISIONAL] tag is removed — PP-616 is final. Retained below for patch-history reference only — do not implement.

Revolution Domain Action. Pool: PS (as dice) + History, TN 7, Ob 3. Prerequisite: PS ≥ 1.
| Degree | MS Effect | Other |
|--------|-----------|-------|
| Overwhelming | MS +2 | PS unchanged |
| Success | MS +1 | PS unchanged |
| Partial | MS +0 | Wasted action |
| Failure | MS +0 | PS −1 |
Frequency: once per season. Consumes 1 Domain Action.

## Simultaneous Catastrophe Rule (PP-199 — ED-077)

If MS=0 AND IP≥80 both trigger in the same Accounting phase:
1. MS=0 resolves first (Shared Loss: game-ending Thread collapse condition).
2. IP≥80 Altonian invasion pressure resolves second.
Both are independent effects. Priority: MS=0 > IP threshold. If MS=0 triggers Shared Loss end condition, IP escalation is moot.

## Reformed Settlement Standing Effect (PP-201 — ED-081)

When Reformed Settlement is in force (Church Influence ≥ 40 and Church has Resisted):
- All Diplomacy Domain Actions targeting Hafenmark: permanent +1 Ob (Church institutional antagonism).
- Effect persists until Church Influence drops below 40 OR Reformed Settlement is withdrawn.
[Source: bg_v05 Cascade Test 2 simulation]

## Restoration Movement — Named NPCs (ED-005 resolved 2026-04-03)

1. **MARET VOSSEN** — Primary contact. Grassroots organiser. TS 0, Charisma 5+, Circles 3+ in working-class networks. Non-practitioner. Full stat block deferred to campaign development.
2. **ALDRIC HANN** — Operational doer. Lower Charisma than Vossen, higher Circles in logistics and street-level networks. Full stat block deferred.

## Riskbreakers — Identity Confirmed (ED-006 resolved 2026-04-03)

Extralegal arm of the Löwenritter. Small-cadre elite consequentialists loyal to Valoria as concept — not to Crown, institution, or faith.
Will go extralegal (blackmail, hostage, theft, murder) when judged necessary for Valoria's survival.
Existence known only to Crown and Lions' Table. Active concealment is core doctrine.
Some members are Thread Practitioners. Operate alone or in small teams; present as ordinary people.
Will not permit Valoria to fall under weak-willed, foreign, or religious rule.
Parallel archetype: Shadow Warriors (Sousou no Frieren).
Individual profiles and stat blocks deferred to campaign development.

---
<!-- PP-236 applied 2026-04-04: Crown covert actions rule -->
<!-- PP-237 applied 2026-04-04: Public Instability Hybrid definition -->
<!-- PP-238 applied 2026-04-04: Lowenritter reactive Military NPC guidance -->
<!-- PP-241 applied 2026-04-04: Crown-Lowenritter covert delegation rule (PROVISIONAL) -->
<!-- PP-244 applied 2026-04-04: Scene→Mass transition modifier table (PROVISIONAL) -->
<!-- PP-246 applied 2026-04-04: Lowenritter ethical framework modifiers extracted; Niflhel struck per CR-STRIKE-2026-04-19. -->

## Crown Covert Actions (PP-236) [PROVISIONAL — pre-ledger, accepted as canonical per 2026-04-26 audit]

Crown has NO Intel stat. Crown covert actions (investigation, sabotage, intelligence gathering) use the **Influence** pool at **+1 Ob**. This is a faction design constraint: Crown is institutionally weakest at covert operations. The +1 Ob penalty applies to all Crown-initiated covert Domain Actions regardless of the action's formal label.

## Crown-Lowenritter Covert Delegation (PP-241) [PROVISIONAL — pre-ledger, accepted as canonical per 2026-04-26 audit]

When Crown delegates a covert Domain Action to Lowenritter, the roll uses **Lowenritter Intel** pool. The Crown covert +1 Ob penalty does NOT apply — the constraint is institutional, not operational. Lowenritter acts as Crown's deniable agent. Political consequences of Lowenritter action discovery fall on Crown, not Lowenritter.

## Public Instability — Hybrid Mode (PP-237) [PROVISIONAL — pre-ledger, accepted as canonical per 2026-04-26 audit]

Public Instability is a Hybrid-mode secondary clock.
- Range: 0–10. Starting value: 5.
- In TTRPG mode: not a separate clock. Effects folded into Institutional Pressure.
- Hybrid increases: +1 per season Revolution Agitation resolves (any degree); +1 per season IP increases while CI > 40.
- Hybrid decreases: −1 per season Crown or Guilds completes successful social Domain Action in contested territory.
- Threshold 8: Revolution gains one free Agitation action at no Domain Action cost.
- Threshold 10: Shared loss condition check (Institutional collapse — distinct from MS=0 Rupture).

## Lowenritter Reactive Military NPC Guidance (PP-238)

Lowenritter NPC AI priority: if any bordering faction's Military exceeds Lowenritter Military, Lowenritter NPC AI prioritises Military Consolidation (internal) the following season. This is a guidance rule, not a threshold mechanic — no automatic trigger fires.

## Scene→Mass Transition Modifiers — Hybrid (PP-244) [PROVISIONAL — pre-ledger, accepted as canonical per 2026-04-26 audit]

When a personal combat scene precedes or overlaps a Strategic Phase mass action:
- PC Overwhelming success: mass action at −1 Ob (officer neutralised, morale advantage)
- PC Success: no modifier
- PC Partial: mass action at +1 Ob (position degraded)
- PC Failure: mass action at +2 Ob (PC captured/incapacitated; morale cost)
Mid-combat zoom: pause combat. Resolve Strategic Phase. Apply mass outcome as context. Resume personal combat next session.

## ~~Ethical Framework Modifiers — Löwenritter (PP-246)~~ — SUPERSEDED 2026-05-02 (PP-686 v2 / ED-784)

<!-- [SUPERSEDED 2026-05-02 — SUPERSESSION-PP686-003] Per-faction Ethical Framework table superseded alongside the general framework (SUPERSESSION-PP686-002 above). Löwenritter's Mission/cascade/expectation tags now authored in faction state per faction_behavior_v30.md §3.7 (Mission "Honour the Crown's institutional authority"; cascade narrow alignment with Crown procedural decisions; populist expectations track populist Crown loyalty). The previous binary "aligned vs contradict" framing is replaced by the triadic decomposition. Retained below struck for patch-history reference only — do not implement. -->

~~| Faction | Framework | Aligned (−1 Ob) | Contradict (+1 Ob) |~~
~~|---------|-----------|----------------|-------------------|~~
~~| Löwenritter | Martial Honour | Military actions + Crown-loyal actions | Political manipulation; acting against Crown interest |~~

## PP-242 — Seasonal cap timing

±2 cap applied at accounting. Multiple actions within a season tally; net clipped at accounting.

## PP-243 — Royal Decree partial-sheet

Decree may only target stats present on target faction's sheet.

## PP-244 — PC excommunication succession

Excommunicated PC faction leader: faction reverts to NPC institutional tendency until PC reinstated (Reversal) or replacement designated (Influence DA Ob 2 or GM succession).

## PP-246 — DA→Contest escalation

DA always produces outcome. Contest escalation only when: (a) both parties present, (b) stakes contested, (c) DA roll = Partial. On Partial: Contest at Piety Track 5. On Success/Failure: no Contest.

## PP-254 — CI seizure classification

Territory seizure CI gains = distinct category (not DA). All CI sources subject to ±5/season combined cap. ±3 DA sub-cap does not apply to seizure.

## PP-255 — Public Instability full design (BG)

Range 0–10. Start 5. Accrual: +1/season any faction PS < 3 at accounting. Recovery: −1/season zero hostile Stability-targeting DAs. PI ≥ 8: revolt check (Stability ≤ 3 factions → Stability Ob 2; fail → PS −1). PI = 10: GM narrative uprising event.

## ED-174 provisional — PI cascade brake

At PI ≥ 8: factions passing Stability Ob 2 gain Stability +1. PI increase cap +2/season from all sources combined. Awaiting user confirmation.

## PP-281 — PI cascade brake

At PI ≥ 8: revolt-pass → Stability +1. PI increase rate cap: +2/season max from all combined sources.

## ED-005 Resolution (PP-286) — Restoration Movement Leader [FLAGGED]

Primary NPC contact: **Yrsa Vossen** (confirmed existing). Secondary: **Aldric Hann**.
Full stat blocks deferred to campaign development. Names canonical from existing params.
[FLAGGED: stat blocks required before NPC roster compilation.]
