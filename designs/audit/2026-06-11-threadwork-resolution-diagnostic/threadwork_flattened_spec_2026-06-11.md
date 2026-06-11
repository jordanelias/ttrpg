# Threadwork — Comprehensive Flattened Specification — 2026-06-11
**Scope.** Every input, gate, logic rule, process, sequence, interdependency, and output of the threadwork system as canon stands today, including its cross-system surfaces (combat, social contest, mass battle, investigation, mass-battle saturation, faction echo, articulation). **Supersedes** the 2026-06-10 master analysis §3 as the working flatten (per `<document_consolidation>`); that section remains in its file as the audit-trail original. Contested cells are flagged, never silently resolved.

**Flag legend.** ⚑N*n* / ⚑RD-*n* = open finding (day-1 / day-2 registers); ⚑ED-*nnn* = open ledger item; ⚑FORK = competing canonical values, both legs shown; ⚑STALE = ruled-but-unpropagated (ruled value shown, stale doc noted); ⚑STUB = canon delegates to a legacy/absent home; ⚑NEW = cell-level defect first isolated by this flatten (staged proposal, Jordan-vetoable).

[READ this session: params/threadwork.md (TN table full, three-axis full, PP-603/604/605/606/607/610/632/633, probability reference); params/core.md (face rule, degrees, Continuous Engine, Momentum, PP-255/261, Ob ladder); threadwork_v30 §§2.1, 2.3 (Leap + visibility + ED-677 matrix), 2.4 (all five operation blocks), 2.5, 2.6 (+ N-way head), 3.2–3.7, 4.1–4.4 + CM deck, 5.2, 5.3, 5.6, 6.3 (threadcut externals), fatigue ED-694, P-17 note; infill ll.36–44, 89, 121; derived_stats §1/§4.1/§13/§14 row; knots_v30 §3 table + §3.4; integration spec ED-673 full, ED-676 full, ED-678 full, header registry ED-673–681; combat_v30 §10; social_contest §9.4/9.4b; mass_battle §A.7/A.10; investigation Case Board layer; articulation §2.4/§3.1]
[Day-1 verified, carried with cites (transcript 2026-06-11-05-11-07): Lock chronic drift values; infill POP gate (TS 70+ / MS ≤ 60); Mending ceiling-8 infill lines; Crisis arc §3.7 full text; knots strain caps Option A; Fallout tables; ED-681 beat structure]
[CORRECTION carried: TN ladder is 7/8/9 (POP Binding = 9, params TN table row 4); this session's earlier 7/8-only note is reversed in the diagnostic §0.]

---

## §1 INPUTS

### 1.1 Character inputs
| Input | Range / form | Source of value | Consumed by |
|---|---|---|---|
| Spirit | 1–7 | attributes (params/core) | pool ×2; fatigue threshold ×5; dissociative checks; Belief-opposition check; meditation recovery |
| Focus | 1–7 | attributes | max operations per contact session = Focus − 1 (ED-694) |
| Cognition | 1–7 | attributes | concealment roll (§2.3); helper dice floor(Cog÷2) (§2.5) |
| Relevant History bonus | up to +3D | character histories | pool term |
| Thread Sensitivity (TS) | 0–100; creation per ED-678 (base 0; lifepath mods; Formation 2F = +10 post-First-Leap) | lifepath + play growth (+1 on Leap Ovw, training, Discovery) | TPS = TS÷10 ⌊⌋ → pool term; gates 30/50/70/90 (Depth & Distance minima); Leap Ob 2 (30–49) / 1 (50+); visibility bands; Crisis −1 TS permanent |
| **Approach Training tag** | binary | creation Formation 2F; season training (mentor TS≥50, Disp≥+2, Spirit TN7 Ob2); First-Leap catalyst | hard gate on all operations (§2.1); +1D Leap; advanced: Partial loses its +1 Ob rider |
| Certainty | 0–5; creation per ED-678 (base 4) | lifepath; play | adjudicator response row (§9.4b); capped by Coherence < 3 (−1 per level, §3.3) |
| Coherence | 10→0 continuous | starts 10; ledger §4.1 | band penalties (§3.3); Leap gate ≥1; Crisis at 0 |
| Wounds / Health | per derived_stats §4.1 | combat etc. | −1D per Wound to **all** Thread pools (PP-716); Leap gate Health > 0; mid-contact incapacitation ⌈Health÷2⌉ (v30 l.219 — ⚑N11 vs l.150 binary) |
| Thread Fatigue | 0 → Spirit×5 | per-op accrual (§4.2 schedule) | involuntary contact break at threshold |
| Knot roster (tier, strain, Bonds) | per knots_v30 ⚑ED-841 tier fork | socializing | Crisis arc pool; Anchoring recovery; opposing-op strain target; Composure absorption; remote Thread-Read |
| Bonds / Disposition | Bonds 1–7; Disposition ceiling = Bonds (PP-684) | play | Close-Knot gate Bonds ≥ 5 (knots §3.2 prereq 5, ED-780); Knot formation Ob offset |
| Beliefs / Convictions / Scars | conviction_track (13 Convictions ⚑N10 vs 7-column Scar matrix) | play | collective-op alignment checks; Scar accrual on witness; Belief Co-Authorship at Coherence 2 |
| Momentum | 0–4 | session economy | **not spendable on Thread rolls** (params/core — deliberate exclusion) |
| Dissolution residue (carried) | Potency 1–5 | prior Dissolutions | +Potency exploding-9/10 dice; −1 Coh/use; 1/contact; +1 Ob per prior use of same source (§3.4) |

### 1.2 World inputs
| Input | Range / form | Consumed by |
|---|---|---|
| Mending Stability (MS/RS) | 100→0; start 60 (TTRPG) / 72 (BG) ⚑N12 dual default | band effects (§4.5); Weave-failure escalation (≤40 Shifting Object, ≤20 Gap); POP gate MS ≤ 60 (infill, day-1); Revelation curve |
| Gap inventory | per-Gap: scale n, age, territory | drains; Mending targets; Monstrous Incursion risk; Dissonance factors; territory card (mass battle EDGE-05) |
| Active Locks | per-territory, Lock strength | chronic drift (§4.4); CM-14 strengthens |
| Over-Actualisation marks | per-configuration (Weave §2.4) | +1 Ob follow-ups; Structural OA: +1 MS degradation/season persisting; PP-208 transition rule |
| Residue sites / intensity | per-territory | CM-07/15; harvesting |
| Territory Thread Debt | +Ob tokens | CM-12 clears; battle debt expires at battle-season end (PP-606) |
| Substrate Saturation counter | per battle | §5.5 mass-battle modifiers (PP-606) |
| Co-movement deck state | 18-card global deck (ED-577) | 1 draw/op (2 if Witness Node); reshuffle on exhaustion (~3–4 season cycle) |
| Thread Witness Nodes | per-territory | double draw; CM-05/11; Church Attention Pool feeds |
| WR / WC | 0–3 / 0–3 (PP-605) | WC1: +1D all Thread ops peninsula-wide (WR≥2); WC2: all RS drain from Gaps **and** Locks halved (WR≥2); WC3: Edeyja actively Mending, RS +2/season (WR 3) — the L2 damper ladder |
| Settlement / territory context (controlling faction, Prosperity, VTM, Church territory) | settlement & faction layers | Domain Echo routing (ED-673); spontaneous-Gap targeting (lowest Prosperity); CV drift (ED-676) |

### 1.3 Situational inputs
| Input | Consumed by |
|---|---|
| Opponent practitioner TPS | opposing engagement modifier +⌊TPS÷2⌋ min 1 (§2.6) |
| Helpers (count, Cognition, Beliefs, Reserve status in battle) | collective pool; fracture threshold; Belief checks; A.10 Reserve gate |
| Threadcut being present at Gap | Mending +Ob = ⌈being's TS÷20⌉ max +4 (P-17) |
| Einhir proximity / artifact / stimulant herbs | fatigue ±: +3/rd / −1/rd / threshold +5 (ED-694) |
| Witnesses (TS, Convictions, Certainty, adjudicator?) | visibility tables; Scars; §9.4b response; CV drift (concealment-exempt) |
| Battle scale & phase | A.10 table (TS minimum, flat three-axis Ob, auto-cost) |
| Melee engagement state | Leap eligibility bar (infill l.38) |
| Investigation Depth of active question | Thread-Read Evidence gate (Depth ≥ 4, P1-16) |

---

## §2 GATES (ordered chains)

### 2.1 Operation eligibility chain (evaluated in order, all must pass)
1. **Approach Training tag held** (§2.1 — binary; without it TS-sensitives perceive but cannot act).
2. **TS ≥ 30** (Leap floor) **and** TS ≥ Depth minimum (30/30/50/50/70/90 by Depth) **and** TS ≥ Distance minimum (30/50/70/90 by Distance band) — params three-axis.
3. **Coherence ≥ 1** (v30 §2.3).
4. **Health > 0** (PP-232). Wounds then apply −1D each to the pool (the min-5 formula floor does **not** survive this; engine floor 1D).
5. **Not in melee with an opponent who has declared an attack this round** (infill l.38) — combat context only.
6. **Fatigue headroom**: current Fatigue + op cost ≤ Spirit×5, and ops this session < Focus − 1 (ED-694).
7. **Operation-specific gates:** POP additionally requires TS 70+ and MS ≤ 60 (infill, day-1 read ⚑N8 stranded). **Mending requires TS 50+ and a valid target class (Gap, Shifting Object, or Locked-Zone border — v30 §2.4 Mending block)** and obeys the **scale-hierarchy rule**: cannot hold at scale X while a deeper (X+1+) disruption persists in the same area — work deepest-first (params PP-604). Locked-Zone border Mending (Ob 8+) additionally requires the Einhir framework triple gate (Knowledge + Technique + ...; v30 §2.3 P-26 note).
8. **Battle context:** scale row's Min TS per A.10; helpers must be in Reserve; Devout general cannot use or counter (EDGE-01).

### 2.2 Collective gates (§2.5)
Anchor = highest-TS practitioner, rolls full pool; each helper needs own active contact window and Approach Training (Relational+ per §2.1); helper with **directly opposing** Belief must pass pre-Leap Spirit TN7 Ob1 or drop out; tangentially conflicting Beliefs: dice cannot count 10 as +2 (non-chaining clause, §2.5); pool below half Anchor's solo pool (after drops) ⇒ +1 Ob lattice fracture; no Forking for helpers or acting Anchor.

### 2.3 Formation / acquisition gates
- **Approach Training (in-campaign):** mentor TS ≥ 50 and Disposition ≥ +2; one full season exclusive; Spirit TN7 Ob2 (Success = tag +1 TS; Partial = tag next Accounting; Failure = retry next season, different mentor).
- **Close Knot:** PC Bonds ≥ 5 (knots §3.2 prereq 5 — derived from Disposition-ceiling = Bonds PP-684; surfaced by ED-780); formation roll per ⚑N9 fork (params PP-632 (Bonds×2)+3, Ob = tier − Disposition; vs knots §3.2 Spirit×2+History TN7 Ob2 → Distant).
- **Crisis arc entry (Coherence 0):** withdraw one season from practice → requires Close Knots for the 3 Anchoring Scenes — **no-Close-Knot case unstated ⚑RD-3**; sequencing vs PP-261's immediate-NPC line unreconciled ⚑RD-3 (the §3.3 row's own "if unresolved by season end: NPC" supports arc-first).

---

## §3 ENGINE LOGIC

### 3.1 Dice engine (discrete, canonical for TTRPG-mode)
Face rule (params/core, PP-246): **1 = −1 · (2..TN−1) = 0 · (TN..9) = +1 · 10 = +2 · no chain.** Per-die statistics:

| TN | E[net] | σ | Used by |
|---|---|---|---|
| 6 | 0.50 | 0.806 | (combat conventions) |
| 7 | 0.40 | 0.800 | standard ops, Leap, Mend, Community Weave |
| 8 | 0.30 | 0.781 | Binding (Lock/Dissolution), POP |
| 9 | 0.20 | 0.748* | POP Binding (params TN table row 4) — *σ computed this session; **core's EV table omits the TN 9 row ⚑NEW-P3** |

Degree ladder (params/core, PP-232): **Overwhelming** net ≥ 2·Ob AND ≥ 3 (+1 Momentum — unspendable back into Thread); **Success** net ≥ Ob; **Partial** 0 < net < Ob; **Failure** net ≤ 0 (negatives do not compound). Ob 20 exception: no Overwhelming; Partial needs net ≥ 10. Ob floor 1.
Exception dice: **residue dice explode on 9–10** (§3.4) — the game's only exploding dice; E[net]/die ≈ 0.5 at TN 7.

### 3.2 Continuous engine (canonical for Godot, Decision E)
`net ~ Normal(μ·N, σ·√N)` per the TN table; fractional Ob/TN; degree by `net − Ob` gauge. **⚑RD-1/ED-873:** as specified (no continuity correction) it understates discrete P(net ≥ Ob) by up to 10.0pp at 5D Ob 2 — the Leap's modal cell; `net ≥ Ob − 0.5` restores ≤ 1.01pp (sigma_results T6/T10). params/threadwork's own probability reference already computes "with continuity correction" — the staged fix imports house practice into core.

### 3.3 Pool & difficulty
**Pool = (Spirit × 2) + relevant History bonus + TPS (TS÷10 ⌊⌋), formula floor 5** (Pool Notice PP-616–625; derived_stats §14: range 5–17D+), then situational dice: −1D/Wound; +1D Approach (Leap); +1D WC1 peninsula-wide; +⌊Cog÷2⌋/helper (Anchor only); +Potency residue dice; −1D TPS rest-of-scene after Leap failure (PP-232). Engine pool floor 1D.
**Total Ob = Depth + Breadth + Distance** (params PP-622/623; full tables §1 above), then the modifier stack:

| +Ob source | Value | Scope |
|---|---|---|
| Coherence band | +1 (Fragmented) / +2 (Severed) | all ops incl. Leap (§3.3) |
| MS band | +1 affected territories (Fragile) / +1 worldwide (Critical, cumulative per P-14) | all ops (§5.3) |
| Leap Partial rider | +1 next operation (waived by advanced Approach Training) | that op |
| Over-Actualisation | +1 same configuration (1 season; halved duration on Ovw) | follow-ups (§2.4 Weave) |
| Overweaving | +1 cumulative per additional op, same contact window | that window (§2.4 Weave) |
| Sequential failure (opposing) | +1 if target state changed between rounds | pre-declared ops (§2.6) |
| Opposing engagement | +⌊opponent TPS÷2⌋ min 1 (to **both**) | contested ops (§2.6) |
| Knot-strain rider | +1 (std) / +2 (FR) next Thread op this scene | post-contest loser/tie (§2.6) |
| Threadcut at Gap | +⌈being TS÷20⌉ max +4 | Mending that Gap (P-17) |
| Saturation | +1 then-+2 battle-zone regimes | mass battle (PP-606) |
| Mending seasonal fatigue | +1 per consecutive Mending in the same **season**, cumulative; resets seasonally (v30 §2.4) | Mending |
| Healing accelerated Overweave (R-56) | +2 per repeat healing op in same contact window (1st Ob 1, 2nd 3, 3rd 5, 4th 7) | W-08 healing variants |
| Gap age | +1 established / +2 entrenched | Mending (PP-604) |
| Residue depletion | +1 per prior use, same source | residue ops (§3.4) |
| Prior-use Ob on Knot remote read | +1 strain (not Ob) per use | bookkeeping note (PP-632) |

**σ-leverage hierarchy (⚑RD-7, unstated in canon):** +1 Ob ≈ 2.5× the probability impact of +1D at every pool, both decaying 1/√N; TN steps are the only modifier whose σ-impact grows with pool (0.125√N). The stack above is therefore Ob-dominant by design — the Einhir asymmetry in probability form.

---

## §4 COST & LEDGER LOGIC

### 4.1 Coherence cost sources (per operation event)
| Source | Cost | Cap status |
|---|---|---|
| Scale (body taxonomy ⚑N2): Object/Personal 0 · Relational −1 · Territorial −1 · Structural −2 · **Field/Foundational undefined** | per §3.2 | inside cap |
| Mending | **0** — Amendment 3 ruling is **already carried by the §2.4 Mending block** (every degree row "Coherence: 0" + Asymmetry paragraph); only the §3.2 cost-table row still prints −1 ⚑N1-refined (one stale row, not an unpropagated ruling) | n/a |
| FR surcharge (Lock/Dissolution) | −1 additional; **FR totals: Obj/Pers −1 · Rel/Terr −2 · Struct −3** | **exempt** (PP-196 / ED-103) |
| POP | −1 additional | inside cap (TW-05: "total POP cost = −1 max regardless of scale") |
| Residue use | −1 per use | distinct event, cap-absorbed at Relational+ (§3.4 text) |
| Degree-table outcomes | −1 on Partial/Failure rows (Weave/Pull); Lock/Dissolution rows annotated "(cap)" | inside cap per row annotations |
| History-Resonance risk die showing 1; Flashback anchoring | −1 each | §3.2 rows; procedures ⚑STUB (§4.4 → legacy R37/R38) |
| Structural-Gap proximity | −1 per season | §3.2 |
| Mass battle auto-cost | per A.10 row (0/0/−1/−1/**−2**) | **⚑RD-2:** the −2 War row conflicts with the four-witness total-cap reading (infill l.121; §3.4 "Relational+ base = −1, already capped"; TW-05; PP-196 arithmetic). Flatten presents the cap as: **non-FR total −1/op; FR exempt per the PP-196 totals; A.10 War row = the outlier cell pending Jordan** |
| Knot Loss | −1 (params PP-632) — vs knots §6.2 assigning −1 to **Rupture** ⚑FORK (ED-841 packet) | n/a |
| Unguided First Leap (catalyst) | −1 + 1 Conviction Scar (§2.1) | n/a |
| Collective helper, battle context | −1 per collective op (A.10) | n/a |

### 4.2 Thread Fatigue (ED-694; threshold Spirit×5; reset on full rest; meditation −Spirit)
Leap entry 3 · passive sensing 2/rd · Mending 4/rd · Pulling 5/rd · Locking 7/rd · Dissolution 10/rd; artifact −1/rd; Einhir proximity +3/rd; stimulants +5 threshold (temp). Ops/session ≤ Focus − 1. Throughput consequence (T8): Spirit 3 sustains exactly one Dissolution round per contact.

### 4.3 MS/RS write rules
**Per-operation degree tables (v30 §2.4, exact):**
| Op | Ovw | Succ | Partial | Failure |
|---|---|---|---|---|
| Weave | full; **MS +1 (Rel+ only)**; +1 TS | full; MS 0 | partial; MS −1; Coh −1 | collapse; MS −2; Coh −1; **at MS ≤ 40 ⇒ Shifting Object; at MS ≤ 20 ⇒ Gap** |
| Pull | full, extended; MS 0 | full; MS 0 | partial/short; MS −1; Coh −1 | snap-back **1 Wound (no armour)**; MS −2; Coh −1 |
| Lock | permanent; MS −1; +1 TS | locked; MS −1 | partial; MS −2; Coh −1 (cap) | collapse-on-self **2 Wounds (no armour)**; MS −3; Coh −1 (cap); adjacency rigidity +1 Ob rest of season |
| Dissolution (v30 leg ⚑N4) | clean; **MS −3**; micro-Gap closes in-scene | **MS −5**; Gap one scene | **Shifting Object; MS −6**; Gap persists w/o Mending; Coh −1 (cap) | **full Gap; MS −8; Monstrous Incursion; practitioner Incapacitated**; Coh −1 (cap) |
| Dissolution (params PP-604 leg ⚑N4) | Gap closes in-scene; breach n only | Gap at n | Gap at **n+1** | Gap at **n+2** ⚑RD-4 (n=5 ⇒ off-table) |
| Mend (v30 block + params tiers) | Gap closes cleanly; **RS +2**; Coh 0; mended zone +1 Ob vs future Gap formation 1 season; Master tier additionally closes Gap on Ovw with −1 Ob to adjacent Gaps | Gap closes; **RS +1** (RS +2 at Adept/Master tier); Coh 0 | Gap reduced one severity category; RS 0; Coh 0; second Mend required | Gap unchanged; **RS −2**; Coh 0 |

**Other world writes (v30 §5.2 + params PP-604):** Gap breach = n RS one-time; **Gap drain = n RS/open season (params, canonical-marked) ⚑NEW-FORK vs v30 §5.2's flat "−4/season" row**; self-closure 1/2/4/8/32 seasons by n (Object n=0 closes in 1 season, no drain); Lock chronic drift Obj 0 / Pers −1/s / Rel −1→−2 (s4+) / Field −2→−3 / Struct −3→−5 per territory; POP −3 minimum; micro-Gap surviving to Accounting −1; siege −1/season; Structural OA persisting −1/season; collapsed overweave −3; Saturation battle-end −1 (hard cap 1/battle); **baseline decay −1/year (PP-255)**; CM deck deltas (−3..+2 per card); WC3 **+2 RS/season** (the standing damper); RS floor 0 = Rupture; seasonal cap **STRUCK** (PP-603) ⚑N3 residuals in §5.3 design note/§5.5/PP-198 quote.

### 4.4 Band tables (full effects)
**Coherence (§3.3):** 10–8 Stable — none · 7–5 Dissonant — narrative flicker; Close Knots +1 strain/3 sessions · 4–3 Fragmented — −1D social & Recall (PP-234); all Knots +1 strain/2 sessions; **+1 Ob all ops incl. Leap**; Fragmented Fallout on entry (d6, **face 3 undefined ⚑RD-6**) · 2 Fractured — −2D social & Recall; +1 strain/session; per-scene-with-op dissociative check Spirit TN7 Ob1 (fail = lose 1 round); **Certainty max −1 per level below 3; Belief Co-Authorship begins**; Fractured Fallout on entry (d6, **face 1 undefined ⚑RD-6**) · 1 Severed — −2D; episodes every scene (at scene start); +2 strain/session; **+2 Ob all ops** · 0 Rendering Crisis — campaign event; unresolved by season end ⇒ NPC (⚑RD-3 record split).
**MS (§5.3, cumulative per P-14):** 100–80 Stable · 79–60 Strained (TS-10+ unease at old sites) · 59–40 Fragile — 1 spontaneous Shifting Object/season; **+1 Ob in affected territories** · 39–20 Fractured — spontaneous Gap 1d10 (1–2; lowest-Prosperity territory); Incursion risk at Gap territories; non-practitioner rendering failures · 19–1 Critical — spontaneous Gap on 1–4; **+1 Ob worldwide**; faction Stability checks Ob 1/season (fail ⇒ Mandate −1; at Mandate 0 ⇒ **Faction Fracture**); Discovery Events common; **coup/succession triggers +1 at MS ≤ 10** · 0 Rupture — campaign ends; no faction wins. Canon's own endgame math (design note): net −8..−15 MS/season at Critical; Mending at MS 1 ≈ 17–34% success.
**Revelation curve (§5.6):** per-band non-practitioner perception + political impact table — the master narrative driver (folklore → anomalies → public fear/Church scramble → "the stories were true" crisis → existential reorientation; the faction integrating Thread reality fastest gains decisive advantage).

### 4.5 Recovery economy (§3.5 + ED-694)
Coherence: +1 per full non-practice season · +1 per Anchoring Scene (Bonds TN7 Ob2; **costs that Knot +1 strain** — the L3 trade) · Einhir techniques (late-campaign) · ceiling 10 · **no CP purchase**. Fatigue: full rest → 0; meditation −Spirit. Composure: restores at scene change (§2.6). Knot strain: −1/season rest (threadcut-strain rule, PP-632). TS: never recovers from the Crisis −1 (permanent; PP-206 disclosure safeguard).

---

## §5 PROCESSES & SEQUENCES

### 5.1 Operation lifecycle (scene scale, canonical order)
1. **Declare** intent + target configuration (Depth/Breadth/Distance set the Ob; "Diagnosis" as a named step is struck per ED-134/124 ⚑N7 residuals in prose; mass battle retains Diagnosis-at-Phase-1 wording ⚑N7-reach).
2. **Gate chain** §2.1 evaluates (training → TS minima → Coherence ≥ 1 → Health > 0 → melee bar → fatigue/session headroom → op-specific gates).
3. **Leap roll** — pool + Approach +1D − wounds; TN 7; Ob 2/1 by TS; band +Ob applies. Outcomes: Ovw = clean, next op Ob −1, +1 TS · Succ = contact · Partial = contact, op +1 Ob (waived by advanced training), 2 Composure · Failure = no contact, −1D TPS rest of scene (retry permitted, degraded). Fatigue +3 on entry.
4. **Contact loop** (while fatigue < Spirit×5 and ops < Focus−1 and no exit event): declare operation → modifier stack (§3.3) → roll vs TN (7/8/9 by type) → **degree table writes** (§4.3) → **co-movement draw** (1 card; 2 if Witness Node; per §2.6, opposed/compound events draw once) → Coherence event (§4.1, cap rule) → fatigue accrual → visibility/witness processing (tables §2.3 + ED-677; concealment = Cognition roll; adjudicator table §9.4b if formal proceeding; CV drift queue ED-676; Scar checks npc §3.4; Domain Echo queue ED-673).
5. **Exit:** voluntary · fatigue threshold (involuntary, no re-entry until rest) · incapacitation (current op → Failure) · scene end.
6. **Scene close:** Composure restores; scene-scoped Ob riders expire; Leap-failure TPS penalty ends.
7. **Seasonal Accounting (world tick, ordered):** Gap self-closure timers ↓ → Gap drains (n/season ⚑NEW-FORK) → Lock chronic drift → Structural-OA persistence drain → baseline decay −1 applied at Year-End Accounting (PP-255) → WC3 credit +2 → MS band re-evaluate → spontaneous events by band (Shifting Object @Fragile; Gap d10 @Fractured/Critical; faction Stability checks @Critical) → Domain Echo + CV drift resolve (queued; caps 1/scene/faction and ±2/territory/season) → Crisis-arc season events (withdrawal seasons count; unresolved Coherence 0 ⇒ NPC) → recovery ticks (Coherence non-practice +1; Knot strain −1 resting) → Saturation/battle Thread Debt expiry → deck continues (global, no seasonal reset).

### 5.2 Sub-procedures
- **Opposing operations (§2.6):** both declare → engagement modifier +⌊opp TPS÷2⌋ min 1 to each → both roll → 6-row resolution table (meet/meet ⇒ **Shifting Object** at target scale, worst-degree MS cost +1, both pay; meet/partial ⇒ winner resolves degraded-from-Ovw; partial/partial ⇒ d6 1–2 Shifting Object one scale down; etc.) → Knot-strain consequence table (std: loser +1 Ob & 2 Composure, winner 1; FR: +2 Ob & 4 Composure, Dissolved-against victim +1 Wound) → co-movement once for the compound event. Multi-round: +1 Ob sequential-failure if target state changed; double Shifting Object ⇒ deterioration tier advance (1d3 seasons → 1d3 sessions → end of scene). N-way (3+): §2.6 extension.
- **Collective (§2.5):** all Leap same round (Priority 5) → Anchor fail ⇒ no lattice (helpers individual) → helper fails subtract dice; < half Anchor solo ⇒ +1 Ob → Anchor rolls pool + Σ⌊Cog÷2⌋ → costs: each battle-context helper −1 Coherence (A.10).
- **Crisis arc (§3.7 PROVISIONAL, PP-194 ⚑RD-3):** withdraw 1 season → 3 Anchoring Scenes (each Bonds TN7 Ob2; each +1 strain to that Knot) → resolution roll (best Close-Knot Bonds + successful scenes, TN7 Ob3) → Ovw Coh 4 + perm −1 TS · Succ Coh 3 + perm −1 TS · Partial Coh 1, may retry next season · Failure NPC at season end. Live odds (Bonds 5–7 per the Close gate): P(NPC) 9–14% (sigma_results T5). PP-206: TS 30/31 holders receive explicit disclosure (the −1 TS may end Thread access).
- **Residue use (§3.4):** declare during op → +Potency exploding-9/10 dice → −1 Coh distinct event (cap-absorbed at Relational+) → 1/contact → same-source +1 Ob per prior use.
- **First Leap:** event scene (§2.3); in mass battle resolves Phase 6, failed = unavailable rest of battle (EDGE-03); catalyst route grants training tag + Scar + Coh −1 (§2.1).
- **Threadcut beings (§6.3):** no Leap; external op = standard pool/Ob (text prints "Spirit + History + TPS" — missing the ×2 vs Pool Notice ⚑NEW-STALE?) ; cost +1 Rendering Strain per external op → De-Actualisation (§6.4). The Solmund dilemma: acting begins ceasing.

### 5.3 Per-system sequence variants
| System | Slotting | Key rules | Resolver status |
|---|---|---|---|
| **Scene combat** | Leap = full-round Priority 5; all pool to Defence; reactive Parry/Dodge-Backwards only; melee bar (infill l.38; combat §10.1) | W-24/W-33 named applications; §10.2 perception; §10.3 cross-system fire table | **⚑ED-911 — interface without resolver** (engine resolves 1v1 melee only; §10 on superseded layer; op timing/targeting/contact-persistence undefined) |
| **Social contest** | ops **between exchanges**; effects before next Read; genre dice fixed at setup | PP-351 temporal-axis conflict ⇒ TN 8 both orators; §9.4b Certainty-indexed adjudicator response; visibility-gated; formal proceedings only | complete (two P3 statement gaps: mid-exchange ops; §2.6-in-contest join) |
| **Mass battle** | own offensive phase between Manoeuvre/Engagement (ED-050 D); Diagnosis Phase 1; Leap Phase 4/5 (PP-101); damage defers to Cascade 6.1 | A.10 scale table; Saturation (PP-606); command cost; battle co-movement d3 tables; Reserve collectives; EDGE-01/02/03/05 | complete; ⚑N2/⚑RD-2 record cells (LA-8/J-9 docket) |
| **Investigation** | Thread-Read = fieldwork action firing co-movement; standard Leap | TW-05 cap ruling; TW-10 FR-exclusivity; **Depth ≥ 4 Evidence gate (P1-16)**; ED-680 dual-depth Case Board, +1 Evidence insight (1/investigation); remote read via Knots | complete; ⚑LA-1 stat-line split; fieldwork-vs-investigation_systems cite drift |

---

## §6 INTERDEPENDENCIES

### 6.1 Write→read matrix (threadwork output × consumer)
| Threadwork writes | Consumed by |
|---|---|
| Coherence Δ / band | social & Recall pools (PP-234); Certainty cap; Knot strain pacing; op +Ob; mass-battle Severed-general EDGE-02; NPC transition |
| MS/RS Δ | band effects on **all** Thread play; Weave-failure escalation; spontaneous events; faction Stability checks + Mandate/Fracture (Critical); Revelation curve → every faction's politics; victory layer (RS→MS naming ⚑N11) |
| Gap inventory | territory cards; Mending economy; Incursion spawns; Dissonance exposure; CM card targets |
| Locks / OA marks / residue sites / Thread Debt | drift & follow-up Ob; CM-07/12/14/15 |
| Knot strain / rupture / loss | Composure (PP-633 cap); Disposition → −4; Coherence −1 (leg per ⚑FORK); articulation triggers #6/#7 |
| Composure & Wounds (Pull/Lock failures, FR-rupture, battle co-movement) | combat & social layers |
| TS growth (+1 Ovw events) / TS −1 (Crisis) | gates, pool, visibility — self-reinforcing competence loop, capped by the cost economy |
| Scars / Belief rewrites / Belief-revision Keys | conviction track (⚑N10 matrix); articulation trigger #10 (state.belief_revised); companion departure (§10.3) |
| Domain Echo (±1 faction stat) / CV drift / Church Attention Pool | faction layer (queued to Accounting; caps); Church investigation pressure |
| Evidence Δ (Thread-Read, insight bonus, §9.4b C2–0 row) | investigation track |
| Articulation/event keys: meta.knot_formed (#6), meta.knot_ruptured (#7), state.belief_revised (#10) | articulation layer §3.1 — **scene.thread_operation key itself is pending registration (LC-0b/J-2)** ⚑ |
| Fallout effects / dissociative episodes / Discovery Events | scene presentation; TS growth checks for witnesses |

### 6.2 Read←write (inbound dependencies)
Wounds/Health ← combat · Bonds/Disposition/Knots ← socializing & fieldwork · Convictions/Certainty ← conviction track & lifepath (ED-678) · territory control/Prosperity/VTM ← faction & settlement layers · WR/WC ← Warden relations (expeditions, Forgetting Checks; decreases: T15 military, RM emergence, 3-season absence) · battle scale/phase/Reserve ← mass battle · investigation Depth ← case structure · adjudicator Certainty ← NPC sheets.

### 6.3 Loop register (from the 06-11 resolution diagnostic, Phase 4)
L1 personal spiral — damped ×3 (cap, fatigue, recovery), bounded by the Crisis arc · L2 world spiral — deliberate, conditionally damped (WC ladder: WC2 halves Gap/Lock drains, WC3 +2 RS/season; the WC3-or-Rupture endgame, §F + sims; Weave-failure escalation at MS ≤ 40/20 is an additional loop edge **inside** the same safeguard analysis) · L3 Knot-recovery strain — designed trade, roster-bounded · L4 combat coupling — one-directional with enumerated wound returns (Pull-fail 1W, Lock-fail 2W, FR-rupture +1W, battle co-movement 1W) · L5 MS→faction return edge — none found; flagged to ED-679 to keep it that way.

---

## §7 OUTPUTS (by ledger, exact deltas)
**Practitioner:** Coherence (per §4.1 + cap), Fatigue (§4.2), Composure (Leap Partial 2; contest tables 1/2/4), Wounds (degree-table rows), TS (±1 events; Crisis −1 permanent), Fallout effects (band entry), Belief rewrites (Coherence 2), Scars (witness/catalyst events), Momentum (+1 on Ovw — spendable elsewhere only), residue inventory.
**World:** MS/RS (per §4.3 rows incl. CM deck −3..+2), Gap inventory (create n / n+1 / n+2 ⚑N4-RD-4; micro-Gaps; spontaneous), Shifting Objects (Weave-fail ≤40; opposed ties; deterioration ladder), Locks + strength, OA marks, residue sites/intensity, Thread Debt, Saturation counter, Witness-Node states, deck position.
**Political:** faction stat ±1 (Domain Echo six-row table, cap 1/scene/faction), Mandate −1 / Faction Fracture (Critical checks), CV ±(≤2/territory/season), Church Attention Pool +1 events, coup-trigger +1 (MS ≤ 10), Revelation-band position, WR/WC movement.
**Narrative/engine:** articulation Keys (#6/#7/#10; scene.thread_operation pending ⚑), Scene Slate thread-state factor (ED-674), Case Board substrate nodes + insight Evidence (ED-680), Crisis beats (ED-681), Discovery Events, companion departure triggers, adjudicator proceeding outcomes (§9.4b incl. voiding), Monstrous Incursions, NPC-transition (Coherence 0 ⚑RD-3).

---

## §8 CONTESTED-CELL REGISTER (every flag above, one line each)
| Flag | Cell | Status |
|---|---|---|
| ⚑N1/STALE (refined) | Mending Coherence 0 — §2.4 block already carries the ruling; **§3.2 table row alone** prints −1 | one-row fix pending |
| ⚑N2 | body taxonomy (Territorial; Field/Foundational costs undefined) — reaches mass_battle A.10 + integration ED-673(c) | Jordan ruling pending |
| ⚑N3 | struck ±10 cap residuals (§5.3 design note, §5.5, PP-198 quote) | sweep pending |
| ⚑N4 + RD-4 | Dissolution degree fork (v30 MS-flat/Shifting-Object leg vs params n-ladder leg) + n+2>5 undefined | both legs printed §4.3 |
| ⚑N5 | Mending Ob fork incl. params-internal (ceiling 8 vs Foundational 12 key) | Jordan |
| ⚑N7 | struck "Diagnosis" residuals (incl. mass-battle Phase-1 wording) | sweep |
| ⚑N8 + RD-2 | infill-stranded values (per-op cap, POP gate, ceiling 8, melee line) + A.10 cap contradiction + dangling cite | hoist after/with N2 |
| ⚑N9 | Knot formation fork + params "Max Disposition" mislabel + rupture-vs-loss Coherence leg | ED-841 packet |
| ⚑N10–N13, N15 | Scar matrix; hygiene; RS/MS naming; starting-MS dual default; era language; carried opens | day-1 docket |
| ⚑RD-1/ED-873 | continuous-engine continuity correction (10pp → ≤1.01pp) | staged; severity revisit |
| ⚑RD-3 | Coherence-0 record split + no-Close-Knot silence | Jordan |
| ⚑RD-5/6/7 | stale core quick-ref; Fallout d6 holes; leverage hierarchy unstated | staged |
| ⚑NEW-P3 | params/core TN summary + EV table omit TN 9 (POP Binding) | staged this flatten |
| ⚑NEW-FORK | Gap drain: params n/season (canonical-marked) vs v30 §5.2 flat −4/season | staged this flatten — params leg presented as governing, Jordan-vetoable |
| ⚑NEW-STALE? | §6.3 threadcut external pool prints "Spirit + History + TPS" (missing ×2) vs Pool Notice | staged this flatten |
| ⚑STUB | §4.4 History Resonance / Flashback = pointer to legacy R37/R38; §2.1 cites "§2.6 visibility" (table lives at §2.3) | staged this flatten |
| ⚑ | scene.thread_operation event key unregistered | LC-0b / J-2 |

[CONFIDENCE: high on every numeric cell — each traces to a file+section read this session or a day-1 read with transcript record; the three ⚑NEW cells are this flatten's own surfacing, staged as proposals, none executed. No fork resolved silently; the RD-2 cap presentation states the four-witness reading and marks the outlier rather than choosing.]
