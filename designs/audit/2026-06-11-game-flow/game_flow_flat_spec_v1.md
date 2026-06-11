# VALORIA — Game Flow: Flattened Operational Specification
**Date: 2026-06-11 · Companion to `game_flow_analysis_v1.md` (same directory) · Status: ANALYSIS (audit)**
**What this is:** the campaign machine flattened to one addressable level — every state variable (A), every formula (B), every gate (C), the master sequence (D), every cross-system edge (E), every output (F), with the open flags mapped onto the rows they touch (G). Rows cross-reference by ID: a sequence step names the gates it checks (C-nn) and the logic it runs (B-nn); edges name the steps they connect. Citations are block-level (same canonical set as the analysis; full list there). `[RB]` = read-bounded: the element exists canonically but its full table/values were not expanded in this session's read set — do not implement from this row alone. `[F-n]` = carries analysis finding n.

---

## A — STATE REGISTRY (everything the machine reads and writes)

### A1 · World clocks (campaign scope, mostly Accounting-written)
| ID | Variable | Range | Start | Written by | Read by | Source |
|---|---|---|---|---|---|---|
| A1.1 | MS (substrate) | 0–100 | 72 | S2.3 battles (immediate), S5.4 (yearly −1, Strain-Collapse −1, Mending, WC), era logic | C3.x band gates, revelation tier, T.1–T.2, Slate Step 2b | params/bg/clocks.md; peninsular_strain §3.1; ms_trajectory |
| A1.2 | CI (Church) | 0–100 | 28 (P-32) | S5.4 CI sequence (B-14) | C3.5 Seizure gate, C3.6 IP-feed, Parliament weights (B-19) | victory §7; faction_layer §9 |
| A1.3 | IP (Altonian) | 0–100 | 20 | S5.4 (B-16 bands), repulsion/decay events | C3.7–C3.11 milestones/phases, T.3 era | peninsular_strain §3.2; victory §5.2 |
| A1.4 | PI (Parliament Integrity) | 0–20 | 7 | Hafenmark parliamentary pressure; Löwenritter Autonomous −1 / Split −3 (sign as written) | C5.7 auto-resolve ≥20 | params/bg/clocks.md; faction_layer Löwenritter table |
| A1.5 | Strain (a.k.a. Turmoil; GD-1 "Political Stability") [F6 naming] | 0–10 | 0 | S5.4 4d (B-17) | C3.12 threshold bands, C1.1 victory gate | peninsular_strain §4 |
| A1.6 | Torben Loyalty / Elske Loyalty | 0–7 | 7 / 4 | S5.8 loyalty events | diplomacy gates (Elske ≥6 repulsion C3.10) | params/bg/clocks.md |
| A1.7 | Löwenritter Autonomy | categorical: Loyal→Restless→Autonomous→Split (+Coup Counter) | Loyal; CC 0 | C5.8 ladder transitions | Crown military access, PI, faction roster | faction_layer Löwenritter table; clocks.md |
| A1.8 | WC / WR (Warden Cooperation/Recognition) | — `[RB]` | 0 / 0 | S5.8 Warden Cooperation step | MS accelerator (WC 3 → MS +2) | clocks.md; campaign_architecture Warden paths |
| A1.9 | Season index + era flag | ℕ; {Base, Post-Calamity, Occupation, Anarchy} | S1; Base | S5.10 advance; T.1–T.4 transitions | everything time-gated | victory §5; peninsular_strain §6.4 |
| A1.10 | Victory consecutive counter | 0–2 | 0 | S5.10 (C1.1) | C1.1 | canon/02 GD-1 |

### A2 · Territory / settlement (per-unit)
| ID | Variable | Range | Start | Written by | Read by | Source |
|---|---|---|---|---|---|---|
| A2.1 | Territory control + garrison flag | faction/Uncontrolled/Active-Invasion; bool | authored map (15 playable: T1–T14, T17; T15 fixed Uncontrolled; T16 off-board) | battles, Revolts (S5.4 4c), collapse exit, GD-3, occupation transfer (S5.9) | C1.1, C2.1–C2.2, B-16/B-17 counts | victory §0; params/bg/core.md |
| A2.2 | Accord | 0–3 per territory | capitals 3, home 2 | conquest→1; acquisition→2+; S5.4 4c checks; Strain band effects; Accord Echo (E1.2); consolidation | C1.1, C2.1–C2.2, B-16/B-17, Prosperity effects, PV counting (≥2) | victory §0.2; peninsular_strain §2, §7 |
| A2.3 | PT (Piety) | 0–5 per territory | authored (T1=5, T9=5, T8=4, T12=4, T3/T10/T14=3, …, T15=0 — partial enumeration; full table in core.md) | Church actions; OW Seizure +1 | Piety Yield (B-14), Seizure Ob (B-15), GD-3 RM-variant test | params/bg/core.md; victory §7 |
| A2.4 | Settlement L / PS | 0–7 each | authored seeds | settlement dynamics post-first-Accounting `[RB]` | Mandate aggregate (B-13) | settlement_layer §1.8; LPS-2e |
| A2.5 | Settlement Prosperity / Defense / Order; Fort | 0–5 ×3; 0–4 | authored | governance scenes (Order ±1 via Echo scope), DA effects | Accord derivation ⌊mean Order⌋ [F4 clamp unstated]; income; battle Obs | settlement_layer; AUD-SET-02 |
| A2.6 | Occupation duration counter | 0–3/territory | 0 | S5.9 | control transfer at 3rd consecutive season (Accord 1) | faction_layer §2.4 |

### A3 · Faction (per-faction; 4–6 active, roster open via GD-3/collapse/Split)
| ID | Variable | Range | Start | Written by | Read by | Source |
|---|---|---|---|---|---|---|
| A3.1 | Mandate | 0–7 **derived** | seed then B-13 each Accounting | S5.1 (B-13) | Parliament votes, Suppress pool, hegemony test, GD-3 promotion, Crown Decree gate ≥3 | LPS-2e §1.8 |
| A3.2 | Legitimacy(L) / PopSupport / Influence / Wealth / Military / Intelligence / Stability | 1–7 each (base) | Crown 5/5/5/4/5/3/4 · Church 5/5/6/5/4/4/5 · Hafenmark 4/4/4/5/3/3/4 · Varfell 4/4/4/4/4/4/4 · Guilds 3/3/4/6/2/4/5 · Löwenritter-at-Split 3/3/2/3/5/3/5 · RM statless (PT+Presence, PP-460) | Domain Echo (E1.1), DA outcomes, Stability triggers (C5.1–C5.5), FSS-LOOP-2 re-muster, attribute changes S5.1 | d+σ pools (B-2), muster, Treasury/Discipline derivation | params/bg/core.md; faction_layer [F2 write-path architecture open] |
| A3.3 | Treasury / Discipline / Legitimacy-pool | W×100 / Stability×10 / formula `[RB]` | derived | drains (Assert/Suppress failure per victory §7 [F10], IP-90 −20, Strain Tension −25) | spend gates | derived_stats_v1 via hierarchy map |
| A3.4 | Treaty set; Casus Belli | pair-typed (Truce/Peace/Alliance/Capitulation/Tributary) | none | S2.3 Priority-4 actions, S5.1 ratification | Strain decay (B-17), hegemony, Trigger 2 | faction_layer §3 |
| A3.5 | Insurgency L (per GD-3 entity) | L ≥ 1 | 1.0 at spawn | S5.7 | promotion gate C2.3 | canon/02 GD-3 |

### A4 · Player character
| ID | Variable | Range | Start | Written by | Read by | Source |
|---|---|---|---|---|---|---|
| A4.1 | Base stats (7-family) | 1–7 | lifepath | advancement `[RB]` | all pools (B-3..B-8), derived (B-9) | derived_stats §3 |
| A4.2 | Health / Stamina / Composure / Concentration | Health `[RB]`; (3End)+(2Spi); form-drift flagged; (3Foc)+(2Spi) ED-902 | full | scene drains/recovery | scene gates, contest exhaustion | derived_stats; hierarchy-map drift register |
| A4.3 | Coherence | 10→0 | 10 | Thread ops (B-11 costs), PP-198 strategic-touch payment | Thread gates, campaign-arc table | campaign_architecture §3.2 |
| A4.4 | TS (Thread Sensitivity) / Certainty | 0–100 / `[RB]` | lifepath | revelation events | Leap gate TS ≥ 30 | campaign_architecture §4 |
| A4.5 | Standing | 0–7 (per faction) | 0 | Duty resolution +1/+2/−1 (floor 1); leadership events | rank gates C7.1, budget mods, succession C7.3 | player_agency §3 |
| A4.6 | Renown | 0–10 | 0 | B-21 sources (cap +2/s; failures −1 cap −2) | C7.2 (7+ pool, 9+ Grand Contest), successor seed | player_agency §5 |
| A4.7 | Momentum | ℕ | 0 | +1 genuine Conviction pursuit | cross-scene spend | player_agency |
| A4.8 | Convictions (3) + resolution states; Duties + Duty state | validator-checked | char-gen | scene outcomes; S0.2 assignment | Slate Step 4 matcher; Portrait gate C8.4; Legacy transform | player_agency §2–3 |
| A4.9 | Disposition (per NPC) / Knots | −4..+Bonds; knot set | authored/0 | fieldwork ladder, Knot scenes | scene access, Witness mode, generational rupture | player_agency; fieldwork |

### A5 · Scene-scope (exist only inside a zoomed scene)
| ID | Variable | Range | Notes | Source |
|---|---|---|---|---|
| A5.1 | Evidence clock | thresholds 3/5/8 by case tier | fieldwork accumulator | fieldwork system |
| A5.2 | Persuasion track | 0–10 | social-contest accumulator | social contest |
| A5.3 | Exposure (vs Cover) | clock | fieldwork risk | fieldwork |
| A5.4 | Battle state machine position | 7 phases (B-12) | mass battle | mass_battle via CSR Part 6 |
| A5.5 | Scene action budget (remaining) | from B-20 | decremented per slate entry opened | player_agency §6 |

### A6 · Campaign-scope event state
| ID | Variable | Notes | Source |
|---|---|---|---|
| A6.1 | Tensions card + fuse state | 1 of 6 drawn at INIT.5; {planted, averted, fired}; fire season randomized S8–S12 | tensions_deck |
| A6.2 | Key log | append-only; **the** save state (= initial conditions + log) | key_substrate §1, §6 |
| A6.3 | Cascade overflow queue | effects beyond depth cap 3 deferred to next Accounting | params/bg/core.md §Cascade Depth Cap |
| A6.4 | Concern queue / Chronicle buffer | articulation read-side | articulation layer (PP-688) |

---

## B — LOGIC REGISTRY (every formula and resolution rule)

### B1 · The five resolvers
| ID | Resolver | Formula / rule | Used by | Source |
|---|---|---|---|---|
| B-1 | (A) Dice pool | d10 vs TN 7; faces 1=−1, 7–9=+1, 10=+2; E[net]=+0.4/die, σ≈0.8/die. Degrees: Failure ≤0 < Partial < Ob ≤ Success; Overwhelming ≥ max(2·Ob, 3). Videogame mode runs the statistically equivalent continuous-Normal (fractional Ob, continuous degrees). Crit: net ≥ 4 (PP-717). | all personal-scale rolls | params/bg/core.md §Dice/§Degree; derived_stats §1 |
| B-2 | (B) d+σ | M = stat − difficulty; P_success = clamp(0.5 + 0.1·M, 0.05, 0.90); banded to the same 4-degree ladder. | every faction-stat action (ED-874) | hierarchy map; ED-874 |
| B-3..B-8 | Pool formulas | Combat max(5, History+6) [ED-901] · Argue (Primary×2)+H+3+style · Thread (Spirit×2)+H+TPS, min 5 · Fieldwork (Primary×2)+H+3 · Knot (Bonds×2)+3 · Mass min(Size,Command)+Command | scene containers | derived_stats §3 via hierarchy map |
| B-9 | (C) Deterministic accounting | ledger formulas, no roll: Mandate (B-13), CI sequence (B-14), Treasury/Discipline/Public Order = W×100 / Stab×10 / Order×20, muster, income | S5.x | derived_stats; faction_layer |
| B-10 | (D) Clock advance | increment toward thresholds; rates in B-14..B-18 | world + scene clocks | clock_registry |
| B-11 | (E) Armature dot-product | interpretation(npc, key) = Σ_axes armature[axis] × key.symbolic_dimensions[axis] × key.impact_vector[npc][axis] over 13-Conviction × 4-axis matrix; cut-scene fire ≥ 0.40 | articulation read-side | hierarchy map; PP-688 |

### B2 · Named formulas and rule blocks
| ID | Formula / rule | Source |
|---|---|---|
| B-12 | Mass battle: 7-phase machine Strategy→Volley→Manoeuvre→Thread→Engagement→Cascade→Reform; auto-resolve (Part B): Martial pool vs Battle Ob; conquest result → Accord 1; splitting exploit countered by terrain/tactic gates | mass_battle via CSR Part 6 |
| B-13 | Mandate (LPS-2e): q_s = 0.5·L_s + 0.5·PS_s; T = Σ W_s·(q_s/7); Mandate = clamp(round(7T/(T+6)), 0, 7) — saturating, mean-reverting | settlement_layer §1.8 |
| B-14 | CI seasonal sequence (Accounting order): (1) Momentum +1 → (2) Piety Yield = floor(Σ: +1 per Church-Prominent PT-5 territory, +0.5 per PT-4; Prominent = Church Mandate > controller Mandate) → (3) Assert (Church, optional): Influence vs Ob 2, Success CI +1 → (4) Suppress (opponent, optional): Mandate vs Ob ⌊Church Mandate/2⌋+1, Success negates step 1 → (5) Baralta structural −1 while her Mandate ≥ 4. Caps ±3 player-initiated / ±5 total. **Failure penalty divergent [F10]: faction_layer §9 "Stability −1" vs victory §7 "Discipline −15".** | victory §7; faction_layer §9 |
| B-15 | Mass Seizure: gate CI ≥ 60, one-shot, no second attempt; P(declare) = ((CI−60)/40)^3.3 per season (1%@70, 10%@80, 39%@90, 100%@100); on declaration every Church-building territory is a simultaneous target; pool = Influence + ⌊CI/15⌋; Ob = 10 − PT − infrastructure (floor 1); requires Prominence + Church Mandate ≥ 4; OW: PT +1; one Emergency Session season of response; seized governance at Accord 1–2 | victory §7, §3.2; campaign_architecture §1.3 |
| B-16 | IP advance (ED-743): per Accounting, count playable-faction territories at Accord ≤ 1 → 0–1: +0 · 2–3: +1 · 4–5: +2 · 6+: +3; CI ≥ 60 sustained: +2/season; faction elimination: +2 one-time. NPC-faction battles don't advance IP directly but their Accord ≤ 1 products count. Decay: Vanguard-Commander Social Contest Success −3; no battle 3 seasons → −1/season; repulsion resets: military OW retreat one phase, ×2 consecutive OW → full withdrawal IP=60 (cap 80 for 10 seasons); diplomatic (Elske ≥ 6, contest vs VC Ob 4, IP < 80) → 40, OW → 20 + 20-season Non-Aggression; resistance (UN Mandate ≥ 3 + Governorate Accord 0 everywhere + battle Success+) → 30; any of these = permanent defeat, IP frozen | peninsular_strain §3.2; victory §5.2 |
| B-17 | Strain update (ED-743): +1 per Accord ≤ 1 playable-held territory (cap +3/season); +2 per elimination; +1 per Revolt (both uncapped, discrete); decay −1 if no territory-instability advance this season; −1 per active Treaty pair (cap −2/season); −1 public diplomatic resolution (max 1/season). Löwenritter exemption: coup = +1 not +2; first 2 post-activation seasons' battles exempt | peninsular_strain §4.1–4.3 |
| B-18 | MS deltas: per battle on Valorian soil −1 (Campaign/War −2; siege −1; uprising −1; Vanguard battle −1; Seizure-with-battle −1; covert/ungarrisoned-seizure 0); −1/year baseline; Strain-Collapse band −1/season; Mending +1..+2 per active Mender by Spirit tier (OW to +5); WC 3 → +2; seasonal net cap ±10. Hysteresis (ED-882): bands fall at 60/40/20, recover at 68/48/28; leading warnings within 12 of an edge and at MS ≤ 12 (PST-1) | peninsular_strain §3.1; ms_trajectory §5.1; clocks.md |
| B-19 | Parliament: votes = Mandate; Church bloc +⌊CI/20⌋; anti-Church −⌊CI/30⌋; Sacred Veto cadence 1 per 4 seasons; action set Censure / Embargo / Blockade / Outlawry / Subsidy / War Authorisation (+ Rebuttal §5.5) `[RB: per-action effects]`; Winter Year-End renewals for Embargo/Blockade | faction_layer §5 |
| B-20 | Scene economy: actions/season Narrative 5 · Normal 4 · Hard 3, ± Standing/Knot/Wound modifiers; slate size Narrative 4–5 · Normal 5–7 · Hard 7–9 (ED-747 pruning to size); travel 1 action/province | player_agency §6.1, §4.2 |
| B-21 | Renown sources: +1 per resolved Conviction · exceeded Duty · Domain Echo · influenced arc · Complex+ case · battle presence · Accord improvement · Knot; cap +2/season; governance failures −1, cap −2/season | player_agency §5 |
| B-22 | Standing deltas: Duty succeed +1 / exceed +2 / fail −1 (floor 1); Initiation Duty is the 0→1 gate | player_agency §3 |
| B-23 | Threadwork costs: Mending 0 · Lock 1 · Dissolution 2 · Binding 2 Coherence; in-scene pool fatigue Fibonacci; cross-scene fatigue +2 Ob/scene; P-01 co-movement auto-effects always fire; Leap gated TS ≥ 30 | campaign_architecture §3.2, §3.2a |
| B-24 | Social contest exchange: Appraise → Declare → Corroborate → Argue → Resolve; drains Composure/Concentration; accumulates Persuasion (A5.2); calibration: ±1 Charisma ≈ 25–30% win-rate swing | CSR Part 3 |
| B-25 | Fieldwork: Evidence accumulation to 3/5/8; Exposure vs Cover; Disposition ladder Neutral→Bonded ≈ 6–8 actions over 3–4 seasons; investigation pacing 3–5 scenes per 5-threshold case | CSR Part 5; fieldwork |
| B-26 | Domain Echo: qualifying scene (C6.5) emits ±1 Success / ±2 Overwhelming to most-relevant faction stat; −1 own faction on Failure; caps 1 Echo/scene/faction and ±2/stat (PP-329); Accord Echo ±1/territory/Zoom-In, queued to Accounting (AUD-SET-02); Thread Echo per ED-673 table `[RB: values]`; PP-198: declaring practitioner pays Coherence for strategic-touching Thread ops | scale_transitions §7; PP-329 |
| B-27 | Generational transfer: world state persists wholesale; 1 Legacy Conviction transfers transformed; Resources = floor(half) + new-start; Standing/Renown/Coherence reset; Knots rupture (strain to Knotted NPCs); Obligations → institution; predecessor Renown ≥ 7 → +1 successor seed | generational_transition |

---

## C — GATE REGISTRY (every conditional the machine checks)

### C1 · Victory / terminal
| ID | Gate | Condition | Fires → | Checked at | Source |
|---|---|---|---|---|---|
| C1.1 | GD-1 Peninsular Sovereignty (sole victory) | 11+/15 territories (direct, treaty-bound, Submitted, or institutionally dominated: rival Mandate ≤ 1 ∧ hegemon Mandate ≥ 5) ∧ Accord ≥ 2 in all directly-controlled ∧ Strain ≤ 6, all simultaneous, held 2 consecutive Accountings (A1.10 counter) [F6: victory §0 text still "all 15"; three names for the Strain gate] | campaign victory | S5.10 | canon/02 GD-1; victory §0 |
| C1.2 | Second Calamity (only terminal) | 10 consecutive seasons at MS ≤ 5 **inside Post-Calamity Era** | campaign ends | S5.10 (era-scoped) | victory §5.3; peninsular_strain §6.4 |

### C2 · Strategic mandatories & emergence (canon/02 enforcement set)
| ID | Gate | Condition | Fires → | Checked at | Source |
|---|---|---|---|---|---|
| C2.1 | GD-2(a) mandatory Muster | owned territory at Accord ≤ 3 with no garrison [F3: Accord range is 0–3, so clause is universally true for ungarrisoned holdings — INTENT UNDETERMINED] | Muster scheduled before any stochastic action (≤3 mandatories/faction/season) | S2.1 | canon/02 GD-2 |
| C2.2 | GD-2(b) mandatory Govern | owned territory at Accord ≤ 2 with garrison | Govern scheduled likewise | S2.1 | canon/02 GD-2 |
| C2.3 | GD-3 insurgency spawn / promotion | spawn: 2+ contiguous Uncontrolled territories sustained 2 seasons → Insurgency L=1 (territorial, non-parliamentary). Promotion: L ≥ 3 ∧ 2+ territories ∧ avg Accord ≥ 4 ∧ 2 seasons → full faction; avg PT < 3 → RM-variant (extra-parliamentary) | roster grows | S5.7 (post-Accord-aggregation) | canon/02 GD-3 |
| C2.4 | NPC anti-spiral gates (PP-NPC-01..04) | e.g. Crown Decree requires Mandate ≥ 3 `[RB: remaining three]` | blocks self-destructive AI picks | S2.2 | CSR §1.4–1.10 |
| C2.5 | Altonian Alignment | NPC faction at Mandate ≤ 2 → chance of secret contact | IP +5 immediate; collaborator −2 Ob during Occupation; if exposed (Evidence ≥ 4 investigation): Accord→0 all its territories, Strain +3, universal Casus Belli | world event | victory §5.2 (ED-684) |

### C3 · Clock thresholds
| ID | Gate | Condition | Fires → | Source |
|---|---|---|---|---|
| C3.1 | MS band fall edges | MS falls through 60 / 40 / 20 | revelation tier shifts (Strained→Fragile→…); Slate Step 2b mandatory Thread-state scene at MS ≤ 20 in-territory | ms_trajectory (ED-882) |
| C3.2 | MS band recovery edges | climbs to 68 / 48 / 28 | band restores (hysteresis +8) | ms_trajectory |
| C3.3 | MS leading warnings | trend within 12 of an edge; MS ≤ 12 (PST-1 toward MS 0) | diegetic warning events | ms_trajectory §5.1 |
| C3.4 | MS 0 | at Accounting | Rupture Scene → Post-Calamity Era (T.1) | victory §5 (ED-630) |
| C3.5 | Seizure window | CI ≥ 60 (one-shot armed) | per-season declaration roll on B-15 curve; CI 100 = mandatory declaration | victory §7 |
| C3.6 | CI dominance feed | CI ≥ 60 sustained | IP +2/season | peninsular_strain §3.2 |
| C3.7 | IP visibility milestones | 60 / 80 / 90 | intelligence report (Slate P2) / emergency session (P1) + coalition contests / "imminent" + warring factions Discipline −20 | victory §5.2 |
| C3.8 | Vanguard arrival | IP 75 | Vanguard presence; 80+ sustained skirmishes | clocks.md IP bands |
| C3.9 | Invasion phase gates | Phase 1 @ IP 100 (T3/T10 corridor) → Phase 2 @ sustained 85+ ×3 seasons (T1/T17, Governorate faction M2/Mil4/Stab3, Underground Network arms) → Phase 3 @ 80+ ×3 more (T4/T7, Governorate M3/Mil5/Stab4, +2 Ob occupied DAs) | escalation | victory §5.2 |
| C3.10 | Phase retreat / repulsion gates | IP < 85 (Ph1 stalls) / < 75 (Ph2 abandons) / < 60 (Ph3 recovery); repulsion paths per B-16 | de-escalation, possibly permanent | victory §5.2 |
| C3.11 | Occupation Era trigger | IP ≥ 100 ∧ Altonian diplomacy ≤ 1 at Accounting | T.3 era | peninsular_strain §6.4 |
| C3.12 | Strain threshold bands | 3–4 Tension: all factions Legitimacy-pool −25 · 5–6 Fracture: Accord −1 in one territory each (lowest first) · 7–8 Crisis: Accord −1 all non-capital + Mandate check Ob 2 · 9–10 Collapse: non-capital Accord cap 2 + Mandate check Ob 3 + MS −1/season | band effects at Accounting | peninsular_strain §4.3 |
| C3.13 | PI auto-resolve | PI ≥ 20 | Crown elimination | clocks.md |
| C3.14 | Tensions fuse | not averted by end S7 → fires in randomized season S8–S12, succeed-on-fire; Royal Crisis sub-roll: 1–2 Lenneth / 3–4 Torben / 5–6 Almud | mid-game event | tensions_deck; royal_assassination |

### C4 · Territory state checks (Accounting 4c)
| ID | Gate | Condition | Fires → | Source |
|---|---|---|---|---|
| C4.1 | Accord erosion | Accord 1 ∧ no garrison | Accord → 0 | peninsular_strain §7 4c.1 |
| C4.2 | Revolt | Accord 0 | Popular Uprising: garrison fights (Military vs Ob 2) or retreats; territory → Uncontrolled; Strain +1; MS −1 (uprising battle) | §7 4c.2 |
| C4.3 | Passive normalisation | garrison present ∧ no hostile action, 2 consecutive seasons | Accord +1 (cap 2) | §7 4c.3 |
| C4.4 | Control transfer | occupation 3rd consecutive season | occupier takes control at Accord 1 | faction_layer §2.4 |
| C4.5 | Institutional Consolidation | faction season with zero Stability triggers | Stability +1 and Accord +1 in one territory | faction_layer §1.3 |

### C5 · Faction stability ladder
| ID | Gate | Condition | Fires → | Source |
|---|---|---|---|---|
| C5.1–C5.5 | Stability Triggers 1–5 | T1 Territorial Occupation or Loss · T2 Unfavourable Treaty Terms · T3 Antagonistic Parliamentary Vote · T4 Major Subterfuge · T5 Failed Military Engagement: Significant Losses | Stability check / loss per trigger spec `[RB: per-trigger magnitudes]` | faction_layer §1.2 |
| C5.6 | Accounting Stability Check | ≥ 2 attribute points lost this season → Stability pool vs Ob = loss magnitude; **FSS-LOOP-1 floor: at Stability ≤ 2 this check cannot reduce Stability** (collapse only via active Triggers 1–5) | possible Stability −1 | faction_layer §1.4 |
| C5.7 | Collapse | Stability 0 → §1.5 exit: Mandate→0, territories Uncontrolled @ Accord 0, units Masterless, officers Independent, player Standing benefits void; one-time Survival Exception at Stability 1; elimination feeds Strain +2 / IP +2 | faction exits | faction_layer §1.5 (ED-675) |
| C5.8 | Löwenritter Autonomy ladder | Loyal → **Restless** (Crown Stability ≤ 3 ∨ no military action 4+ seasons ∨ Crown loses a province; S014 defensive-only, Crown +1 Ob offensive, T14 fragmentation Ob +1) → **Autonomous** (Crown Stability ≤ 2 ∨ Ehrenwall Disposition to Almud < 0 ∨ 4+ seasons Restless; S014 ignores Crown, Crown Military −T14 garrison, no Fort 3, PI −1) → **Split** (Crown attacks ∨ Crown eliminated ∨ 4+ seasons Autonomous; T14 → Löwenritter as separate faction 3/3/2/3/5/3/5, PI −3, Crown Military → 2 + unit loss, PV −3) + Coup path via Coup Counter `[RB: coup thresholds]` | monarchy re-bases; roster grows | faction_layer Löwenritter table; core.md |
| C5.9 | Wealth-0 ratchet damper | FSS-LOOP-2: re-muster +1 Military/Accounting while Wealth ≥ 1, up to pre-collapse value | bounds L2 | faction_layer (ratified 2026-05-30) |

### C6 · Zoom & slate gates
| ID | Gate | Condition | Fires → | Source |
|---|---|---|---|---|
| C6.1 | Mandatory Zoom-In (Priority 0, undeclinable) | Accord-0 territory crisis · active Heresy Investigation on player · mass battle in player's territory · faction-leader removal · Stability Crisis (ED-749 hysteresis) · Knot partner crisis · companion arc · rank recognition | scene inserted at next legal entry point | scale_transitions §4.3.2 |
| C6.2 | World-state Zoom (Priority 1, optional) | world-state trigger set §4.3.3 | offered scene | scale_transitions §4.3.3 |
| C6.3 | Legal entry points | after battle Phase 1 / Phase 3 / Phase 6 Step 1; otherwise end of the Domain Action | zoom timing | scale_transitions §4.1 |
| C6.4 | Board-degree shading | Board FAILURE → scene Ob +1 · SUCCESS → −1 · OVERWHELMING → −2 | scene difficulty | scale_transitions §4.1 |
| C6.5 | Sufficient Scope (Echo eligibility) | named faction leader involved · institutional challenge · Complex+ investigation completed · Relational+ Thread op · combat victory over faction officer · Disposition +4/+5 with officer · settlement governance Order ±1 | scene may Echo (B-26) | scale_transitions §7 |
| C6.6 | Witness overflow (ED-745) | mandatory scenes > action budget | excess resolve by NPC AI with player present: one free Read/Appraise, no Echo, no Momentum/Coherence | player_agency §4.2 |
| C6.7 | Retrospective | event entirely missed last season | free "Where Were You?" scene next season | scale_transitions §4.4 |
| C6.8 | Slate Thread-state mandatory | MS ≤ 20 in player's territory | Step 2b entry (max 1) | player_agency §4.2 |
| C6.9 | Unpursued-entry resolution | slate entry not opened | AI resolves per §4.5 consequence table (duty undone → Standing −1; revolt unattended → garrison strength; thresholds propagate) | player_agency §4.5 |

### C7 · Player progression gates
| ID | Gate | Condition | Grants | Source |
|---|---|---|---|---|
| C7.1 | Standing rank gates | 1 via Initiation Duty; 2 open intelligence; 3 council voice; 4 sub-commands +1 action; 6 inner circle +2 actions; 7 succession eligibility | institutional reach | player_agency §3 |
| C7.2 | Renown gates | 7+: floor(Renown/2) substitutes institutional dice; 9+: may call Grand Contest | independent path | player_agency §5.3 |
| C7.3 | Leadership acquisition | Standing 7 offer · 5–6 succession contest · 4+ challenge; player eligible for throne from Standing 5+ in succession (SUC-01..03 `[RB]`) | Duty system → direct command; AI becomes advisor | player_agency §5; faction_layer §3.6a |
| C7.4 | PC embedding bonus | PC physically in territory | +1D on one faction Domain Action there per season | scale_transitions §9 |

### C8 · Era & continuity gates
| ID | Gate | Condition | Fires → | Source |
|---|---|---|---|---|
| C8.1 | Post-Calamity entry | C3.4 | Rupture Scene (3 steps: world-state narration · Last Declaration: Belief, expressing act, "again?" · era begins); acquisition suspended 3 seasons; Mending doubled; recovery target MS 20 within 10 seasons | victory §5 (ED-630) |
| C8.2 | Anarchy entry | all factions Stability 0 | direct governance (Charisma pool, not faction card); Founded Organizations claim Presence free; new faction at Mandate 3 + 2 territories + Accord ≥ 2 ×2 seasons → Founding Declaration; recovery = Parliament quorum (2+ formal factions) | victory §5.3 |
| C8.3 | Generational transition | PC death or Retirement | B-27 transfer | generational_transition |
| C8.4 | Portrait availability | 2 of 3 starting Convictions resolved | "Conclude this story" at every season transition; Draft Portrait always available | player_agency §7 |

### C9 · Engine guards
| ID | Gate | Condition | Fires → | Source |
|---|---|---|---|---|
| C9.1 | Cascade depth cap | > 3 immediate mechanical effects from one resolution step | overflow queues to next Accounting (A6.3) | params/bg/core.md |
| C9.2 | MS seasonal net cap | |ΔMS| > 10 in a season | clamp ±10 | clocks.md |
| C9.3 | Echo caps | per B-26 | clamp | PP-329; AUD-SET-02 |
| C9.4 | CI caps | ±3 player-initiated / ±5 total per season | clamp | faction_layer §9 |
| C9.5 | Strain source caps | +3 instability / −2 treaty / −1 diplomatic per season | clamp | peninsular_strain §4 |

---

## D — MASTER SEQUENCE (the campaign, flat and strictly ordered)

Format: `STEP — process | inputs | gates checked | logic run | outputs (state written · Keys emitted)`.

### D0 · Initialization (Season 0 → live)
| Step | Process | Inputs | Gates | Logic | Outputs |
|---|---|---|---|---|---|
| INIT.1 | Difficulty & parameters | player choice | — | sets B-20 economy | campaign params |
| INIT.2 | World seed | authored map data | — | — | A2.1–A2.5 seeded (15 territories, 35 settlements / 14 provinces / 3 duchies [F9 count drift], PT table, Accord capitals 3 / home 2, Proximity d0–d5) |
| INIT.3 | Faction seed | core.md stat table | — | B-13 (first Mandate from seeds) | A3.1–A3.2 seeded; RM statless; Löwenritter dormant |
| INIT.4 | Clock seed | clocks.md | — | — | A1.1–A1.8 = 72/28/20/7/0/7·4/Loyal/0 |
| INIT.5 | Ignition seed | Tensions deck | — | draw 1 of 6; Royal sub-roll if drawn | A6.1 fuse planted, visible S0–S1; baseline friction: 5 provinces non-aligned |
| INIT.6 | Character creation | lifepath; 3 Convictions (personal/factional/relational) | Step-4 keyword validator | — | A4.x seeded; Coherence 10; Standing 0 |
| INIT.7 | First tick | all above | — | → SEASON loop | S1 opens; `mechanical.season_change` Key |

### D1 · SEASON.0 — Season open
| Step | Process | Inputs | Gates | Logic | Outputs |
|---|---|---|---|---|---|
| S0.1 | Season-change Key | A1.9 | — | engine_clock | `mechanical.season_change` |
| S0.2 | Duty assignment | leader AI stack; player location/skills/faction urgency | Standing ≥ 1 (else Initiation Duty only) | AI selection | A4.8 Duty set |
| S0.3 | Slate generation (8 steps, deterministic) | full world state read-down | C6.1 (Step 1 Mandatory Crisis P0) · clock crossings / Accord ≤ 1 nearby / NPC Scar ≥ 2 (Step 2 P1) · C6.8 (Step 2b) · Duty match (Step 3) · Conviction keyword/role match, max 3 (Step 4) · NPC outreach (Step 5) · Territorial (Step 6) · Ambient (Step 7) | ED-747 cross-step pruning to B-20 slate size | slate of 4–9 entries; overflow → C6.6 Witness set |

### D2 · SEASON.1 — Personal Phase (player turn)
| Step | Process | Inputs | Gates | Logic | Outputs |
|---|---|---|---|---|---|
| S1.1 | Spend scene actions | slate; budget B-20 | C6.6 if mandatories > budget | player triage (the season's one strategic decision) | opened scenes |
| S1.2 | Scene resolution (per scene, container-matched) | A4.x, A5.x, NPC state | scene-internal gates (Leap TS ≥ 30; Exposure; Composure floors) | B-1 pools per B-3..B-8; B-23/B-24/B-25 subsystem rules; chaining allowed | scene outcome Keys; A4/A5 deltas; Echo candidates (C6.5); Momentum +1 on Conviction pursuit |
| S1.3 | Unpursued entries | remaining slate | C6.9 | NPC AI per §4.5 table | consequences (Standing −1 undone Duty, etc.) |

### D3 · SEASON.2 — Strategic Phase (per active faction, AI or player-led)
| Step | Process | Inputs | Gates | Logic | Outputs |
|---|---|---|---|---|---|
| S2.1 | GD-2 mandatory pass | A2.1/A2.2 holdings | C2.1, C2.2 | schedule ≤ 3 mandatories first | Muster/Govern slots consumed |
| S2.2 | Priority-stack selection | faction state, Convictions, posture | C2.4 anti-spiral | 7-step leader stack (Survival → Existential → Framework → Institutional → Secondary → Reactive → Pass) then posture ladder (Existential → Defend → Consolidate → Counter-threat @ CI ≥ 55 → Expand → Opportunistic) | action list |
| S2.3 | Resolution by priority class | action list | Trigger-5 gate on battle; treaty gates | class order: 1 Intel/Tribune → 2 Military/Battle (B-12; Occupation established) → 3 Domain (Consul/Muster/Govern/Trade/Fortify) → 4 Social (B-19 motions, treaties) → 5 Thread ops → 6 Special (Royal Decree, Excommunication, Church Seizure B-15) → 7 Projects; **all faction-stat actions on B-2 d+σ**; player presence C7.4 +1D; Standing 4+ sub-commands; leader-player replaces stack | DA outcome Keys; battle results (Accord 1 conquests; MS deltas immediate per B-18); stat deltas [F2 write-paths open] |

### D4 · INT — Zoom interrupts (the SEASON.3 slot of the four-phase structure, flattened as interrupts because zooms interleave D2/D3 rather than follow them; the BG clock never pauses — PP-110)
| Step | Process | Inputs | Gates | Logic | Outputs |
|---|---|---|---|---|---|
| INT.1 | Zoom-In | trigger event | C6.1 mandatory / C6.2 optional; C6.3 entry points | C6.4 degree shading sets scene Ob | personal scene inserted into resolution sequence |
| INT.2 | Zoom-Out | scene outcome | — | resume strategic sequence with updated state | scene Keys; Echo candidates; Accord Echo queued |
| INT.3 | Missed-event retrospective | last season's unseen events | C6.7 | free scene next season | narrative delivery (no mechanical state change) |

### D5 · SEASON.4 — Cascade Phase
| Step | Process | Inputs | Gates | Logic | Outputs |
|---|---|---|---|---|---|
| S4.1 | Domain Echo application | queued C6.5-qualified scenes | C9.3 caps | B-26 | faction stat ±1/±2; Accord ±1 queued; Thread Echo; Coherence paid (PP-198) |
| S4.2 | Cascade depth guard | all immediate effects | C9.1 | cap 3 | overflow → A6.3 |

### D6 · SEASON.5 — Accounting (10 steps, strict order)
| Step | Process | Gates / Logic | Outputs |
|---|---|---|---|
| S5.1 | Pending attribute changes; Parliamentary votes; treaty ratifications | B-19; Sacred Veto cadence; Trigger 2/3 consequences (C5.2/C5.3) | stat deltas; treaty set (A3.4) |
| S5.2 | Stability checks | C5.6 (FSS-LOOP-1 floor); C5.7 collapse + Survival Exception | Stability deltas; possible faction exit (→ Strain/IP one-times; territories Uncontrolled) |
| S5.3 | Cooldowns advance | — | timers |
| S5.4 | Clock advances | B-14 CI [F10] → MS yearly (B-18) → PI → **4c** C4.1–C4.3 → **4d** B-17 + C3.12 → **4e** (battle MS already applied; ED-743 struck battle-IP) | A1.1–A1.5 updated; Revolts resolved; band effects applied |
| S5.5 | Church Attention Pool; Thread Debt drain | `[RB: magnitudes]` | resource ticks |
| S5.6 | Turmoil consolidation | (4c/4d/4e block bookkeeping) | — |
| S5.7 | Threshold events; Milestones; Warden Emergence; **GD-3 check** | C2.3; C3.x crossings | insurgencies spawn/promote; event cards |
| S5.8 | Warden Cooperation; Torben/Elske loyalty events | `[RB: event tables]` | A1.6/A1.8 deltas |
| S5.9 | Occupation duration; Institutional Consolidation | C4.4; C4.5 | control transfers; Stab/Accord recovery |
| S5.10 | **Victory check**; season advance; Winter → Year-End | C1.1 (2-consecutive counter); C1.2 (era-scoped); C8.x era triggers; Embargo/Blockade renewals; fractional Piety floors | win / era transition / next season (→ S0.1) |

### D7 · T — Terminal & era transitions (fire from S5.10 evaluations)
| Step | Trigger | Effect |
|---|---|---|
| T.1 | C3.4 MS 0 | Rupture Scene → Post-Calamity Era (C8.1) — campaign continues |
| T.2 | C1.2 | Second Calamity — campaign ends (sole terminal) |
| T.3 | C3.11 | Occupation Era — phased per C3.9; winnable per C3.10/B-16 |
| T.4 | C8.2 | Anarchy Era — recoverable via quorum |
| T.5 | C8.3 | Generational transition (B-27) — world persists, new character |
| T.6 | C8.4 accepted | Portrait Sequence → player-authored end of chapter; Lineage Acts (Mentorship / Succession / Thread Legacy) |

---

## E — INTERDEPENDENCY EDGES (directed; the cross-scale wiring)

### E1 · Personal → Strategic (deliberately narrow bandwidth)
| ID | Edge | Mechanism | Cap |
|---|---|---|---|
| E1.1 | scene → faction stat | B-26 Domain Echo via C6.5 scope | 1/scene/faction; ±2/stat/season |
| E1.2 | scene → territory Accord | Accord Echo, queued to Accounting | ±1/territory/Zoom-In |
| E1.3 | scene → Thread/MS layer | Thread Echo (ED-673) `[RB]`; PP-198 Coherence payment | per table |
| E1.4 | player presence → faction DA | C7.4 +1D | 1 DA/territory/season |
| E1.5 | player rank → faction orders | Standing 4+ sub-commands; leader replaces AI stack | rank-gated |
| E1.6 | scene verdicts → CI/Legitimacy | N-gate wiring (Jordan-owned per conversion strategy) | `[RB]` |

### E2 · Strategic → Personal (the down-channel)
| ID | Edge | Mechanism | Status |
|---|---|---|---|
| E2.1 | world state → Scene Slate | S0.3 reads clocks, Accord, Scars, Duty, Convictions | built (presentation channel) |
| E2.2 | board outcome → scene difficulty | C6.4 degree shading | built |
| E2.3 | strategic events → forced presence | C6.1 mandatory zooms; C6.6 Witness; C6.7 retrospectives | built |
| E2.4 | strategic outcomes → personal-scale **Keys** | which Keys, payloads, mandatory effects on the present player | **[F1 / ED-1006: NO canonical rule — all nine scale_transitions §3 rules run upward. The single largest flow hole; blocks Wave-S/4 module specs.]** |

### E3 · Intra-strategic couplings
| ID | Edge | Mechanism |
|---|---|---|
| E3.1 | settlement L/PS/W → faction Mandate | B-13 each Accounting (saturating) |
| E3.2 | Accord ≤ 1 counts → Strain & IP | B-17 / B-16 (same world-state, separate aggregation) |
| E3.3 | CI ≥ 60 → IP | C3.6 (+2/season) — the Church–Altonia coupling, the campaign's central pacing valve |
| E3.4 | battles → MS | B-18 immediate, in-phase |
| E3.5 | Strain bands → Legitimacy/Accord/Mandate/MS | C3.12 |
| E3.6 | collapse → Strain/IP/territories/insurgency | C5.7 → C2.3 (L6 amplifier, intent-gated) |
| E3.7 | treaties → Strain decay; Trigger 2 | B-17; C5.2 |
| E3.8 | Parliament → faction stats/treaties | B-19; Trigger 3 (C5.3) |
| E3.9 | Crown weakness → Löwenritter ladder → PI/roster | C5.8 |
| E3.10 | territory loss/battle loss → Stability | C5.1/C5.5 → L1 loop |

### E4 · Loop closures and dampers (defect test: undamped ∧ unbounded)
| ID | Loop | Damper / bound | Status |
|---|---|---|---|
| L1 | losses → Stability → losses → collapse | FSS-LOOP-1 floor (C5.6); Consolidation (C4.5); Survival Exception | damped (ratified; P(collapse) 0.41→0.97 only under sustained triggers) |
| L2 | Wealth 0 → Military ratchet | FSS-LOOP-2 (C5.9) | damped |
| L3 | territory → Mandate → territory | B-13 saturation + clamp + mean reversion | bounded |
| L4 | Accord ≤ 1 → Strain/IP → Accord loss | C9.5 caps; C4.3 normalisation; treaty decay | bounded (ED-743) |
| L5 | war → MS ↓ → harder world | flat B-18 (×3 struck); Mending; C3.2 hysteresis + C3.3 warnings; Post-Calamity recovery path | damped + warned |
| L6 | neglect → Uncontrolled → Insurgency → invasion | promotion gates C2.3 | intended amplifier, gated |
| L7 | `intent_of_game` (player ↔ world investment) | Slate surplus + Witness budget protection | by design |

---

## F — OUTPUT REGISTRY

| ID | Output | Producer | Consumer |
|---|---|---|---|
| F.1 | **Keys** — `{id, type, source_actor, emitted_at{season,sub_step}, causes[], targets[](role, impact_vector[4], stat_deltas), scale_signature[], symbolic_dimensions[4], visibility, time_horizon, permanence, payload}`; 7 families ≈ 30 subtypes; emission is the **only** state-mutation path; RNG seeded per emission, deterministic ordering | every D-step | A6.2 log; E-resolver (B-11) |
| F.2 | Save file = initial conditions + Key log; load = deterministic replay | engine | persistence; golden-master parity tests |
| F.3 | Concern queue · threshold cut-scenes (fire ≥ 0.40) · annual Chronicle | B-11 over A6.2 | player-facing narrative |
| F.4 | Scene Slate (next season) | S0.3 over updated world | the player — the campaign's visible face |
| F.5 | Victory / era-transition / terminal declarations | S5.10 | campaign resolution |

---

## G — FLAG MAP (analysis findings → flat-spec rows they touch)

| Finding | Touches | One-line consequence for implementation |
|---|---|---|
| F1 (P1, ED-1006, OPEN — Jordan) | E2.4; D4; F.1 consumers | down-channel Key delivery unspecified; Wave-S/4 modules (scene_slate, articulation, npc Key consumption) blocked from clean spec |
| F2 (P1, OPEN — Jordan) | A3.2 write-paths; S2.3 outputs | faction-stat architecture (aggregate-of-holdings vs authored) decides every Wave-2 write-path; parameterize |
| F3 (P2, INTENT UNDETERMINED) | C2.1 | "garrison everything" vs "garrison the restive" — one-line Jordan confirmation before `mandatory_actions()` |
| F4 (P2) | A2.2 ← A2.5 | ⌊mean Order⌋ (0–5) → Accord (0–3) clamp unstated; first-port (settlement_layer) relevant |
| F5 (P2) | C3.4 / T.1 | clocks.md "MS 0 = campaign ends" is dead text; VictoryManager must implement era transition, not fail state |
| F6 (P2) | C1.1; A1.5 | victory §0 "all 15" lags GD-1's 11+/15; pick one name for the Strain quantity |
| F7 (P3) | B-18 | videogame_mode_spec ×3 MS residue — flat −1/−2 is canonical |
| F8 (P3) | INIT.4; B-20 | campaign_modes CI 15 / "2–3 scenes" stale; 28 and 3–5-by-difficulty govern |
| F9 (P3) | INIT.2 | settlement count 35/36/37 — data table wins |
| F10 (P3) | B-14; S5.4 | Assert/Suppress failure cost: Stability −1 vs Discipline −15 — CI module needs one |

---

*Method note: every row derives from this session's canonical read set (citations per block; consolidated list in `game_flow_analysis_v1.md`). `[RB]` rows name canonical elements whose full value tables were not expanded here — fetch before implementing. No values invented; divergences are carried visibly, not resolved silently.*
