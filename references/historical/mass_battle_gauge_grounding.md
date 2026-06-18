# Mass-Battle Gauge — Historical & Academic Grounding (v2.3)
**Date:** 2026-06-15 (v2); 2026-06-16 (v2.1 — cavalry construction fix); 2026-06-17 (v2.2 — per-subunit stamina / line-relief depth-as-reserve grounding, ED-1017); 2026-06-17 (v2.3 — troop-taxonomy stat home, ED-1018) · **Status:** drives `tests/sim/gauge_mb.py` bands · **Supersedes the band-derivation basis of** `tests/sim/sim_mb_06_v9_historical_spec.md` (the v9 spec's H/R bands stand; its cavalry bands were never in scope and the gauge's later cavalry bands were *fitted to engine output* — this doc re-derives them bottom-up).

This is the bottom-up grounding for the recalibrated gauge bands. Every band is set by **historical precedent + peer-reviewed academic military analysis**, not by engine output. The engine is then validated *against* these bands; where it falls outside, the gauge **flags the divergence** — the band is not lowered to make the engine pass.

`[SELF-AUTHORED — bias risk: the engine fix (ED-1013) and this recalibration are Claude's; the academic sources and the historical record are the independent checks. Emergent figures are the smooth-cohesion engine at multi-mode n=120, SE ≈ 5pp.]`

---

## 1 — The metric change (raw-A% → decisive split)

The previous gauge checked **raw A%** (A's win-rate over *all* trials, draws included). This conflated two independent quantities — *who wins* and *whether anyone wins* — so a perfectly symmetric mirror failed its band purely because draws pulled raw-A% down (the Line mirror is 53/47 among decisive outcomes, yet raw-A% ≈ 32% with 40% draws). The recalibrated gauge checks the **decisive split**:

> `decA = A_wins / (A_wins + B_wins)` — "who wins **when** a result is reached."

The draw rate is validated **separately**, as a decisiveness dimension (`draw_exp`), because the quantitative combat-modelling literature establishes that **a high draw rate near parity is expected, not a defect**:

- Hillestad, Owen & Blumenthal (1995), *Naval Research Logistics* 42(2), DOI [10.1002/1520-6750(199503)42:2<209::AID-NAV3220420206>3.0.CO;2-M](https://doi.org/10.1002/1520-6750(199503)42:2%3C209::AID-NAV3220420206%3E3.0.CO;2-M): combat-outcome variance is *most pronounced in the "fair fight" regime in which the force balance is nearly even.*
- Taylor (1979), *NRLQ* 26(2), DOI [10.1002/nav.3800260216](https://doi.org/10.1002/nav.3800260216); Taylor (1983), *NRLQ* 30(1), DOI [10.1002/nav.3800300109](https://doi.org/10.1002/nav.3800300109): victory is *not guaranteed even when the force ratio is always changing to the advantage of one combatant.*
- Armstrong & Sodergren (2015), *Social Science Quarterly* 96(4), DOI [10.1111/ssqu.12178](https://doi.org/10.1111/ssqu.12178): the Lanchester square law yields an exact **tie** when `aC₀² = bU₀²`; Lanchester models are the validated quantitative framework for tactical engagements (Weiss applied them across 64 Civil War battles).

So: **even matchups** (mirrors, subtle formation edges) → `draw_exp='high'` (high draws OK); **gross-asymmetry matchups** (envelopment, cavalry vs braced/shaken) → `draw_exp='low'` (the matchup should resolve).

**One refinement (v2.1, 2026-06-16):** a *repelled* charge is a HOLD, not a decisive result. When braced infantry breaks a frontal cavalry charge, most trials end in a **draw** — the wall holds, but a hold-stance line cannot itself rout the cavalry (exactly the Waterloo squares, which held all day without destroying the French cavalry). For these rows (C2/C6) the decisive split is uninformative (the decisive *n* is tiny) and high draws are *expected*, so they are judged on **raw cavalry win-rate, which must be LOW** — `metric='rawA'`. Every other row keeps the decisive split.

---

## 2 — The grounding sources

**Generalship / force-employment dominates numbers.**
- Biddle, *Military Power: Explaining Victory and Defeat in Modern Battle* (Princeton, 2004), rev. Wirtz (2006), *Journal of Politics* 68(2), DOI [10.1111/j.1468-2508.2006.00420_5.x](https://doi.org/10.1111/j.1468-2508.2006.00420_5.x): victory goes to whoever masters combined-arms force employment, *relatively insensitive to the numerical and technological balance.*
- `references/historical/precedents_warfare.md` §1.1 (Crécy 1346, Agincourt 1415, Austerlitz 1805): command quality, not numbers, decided. → **engine command-decisiveness (cmd6-vs-2 → 40-0) is correct.**

**Full envelopment is the one geometric edge that reliably tells.**
- Cannae 216 BC (double envelopment); Sidnell, *Warhorse: Cavalry in Ancient Warfare* (2006), rev. Basler (2008), *Historian* 70(3), DOI [10.1111/j.1540-6563.2008.00221_61.x](https://doi.org/10.1111/j.1540-6563.2008.00221_61.x): heavy cavalry was decisive in a **shock role** via physical + psychological effect *against the right target*.

**Formation geometry ALONE is a weak edge at strictly equal command.**
- Burkholder (2007), *History Compass* 5(2), DOI [10.1111/j.1478-0542.2007.00394.x](https://doi.org/10.1111/j.1478-0542.2007.00394.x): the cavalry-dominance and formation-dominance narratives (Oman, Fuller) are *overstated*; outcomes depended on a "dizzying array of factors," not one formation or weapon system. → wedge/oblique/manipular edges are **modest, near-even at equal stats**.

**Frontal cavalry vs STEADY close-order infantry is contested, not a cavalry win.**
- Burkholder (2007): *a horse will not run headlong into a solid object like a line of infantry*; foot were *perfectly capable of withstanding cavalry attacks* (Carolingian cavalry annihilated by Saxon infantry, 782); cavalry's killing was of **broken or flanked** foot, and its main weapon was the *feigned retreat* (Hastings 1066) — a ruse to make infantry break ranks. → **the old C1 band (52-80) encoded the popular misconception this source debunks.**

**Braced / squared infantry DEFEATS frontal cavalry.**
- Waterloo squares 1815; Bannockburn schiltrons 1314; Barua (2011), *Historian* 73(1), DOI [10.1111/j.1540-6563.2010.00284.x](https://doi.org/10.1111/j.1540-6563.2010.00284.x): British infantry *deployed in squares by which [Mysorean cavalry] could easily be beaten off* — Baillie's square (1780) the rare exception. → cavalry vs braced **LOW**.

**Cavalry is decisive vs SHAKEN/disordered foot and in the pursuit.**
- Boddy (2015), *Critical Quarterly* 57(4), DOI [10.1111/criq.12231](https://doi.org/10.1111/criq.12231): at Waterloo the Household Cavalry **dispersed 15,000 disordered French infantry**, then was itself destroyed once it over-pursued and lost cohesion (only 77 of 235 2nd Life Guards survived) — both cavalry's decisiveness vs disorder *and* its cohesion-fragility. → cavalry vs shaken **HIGH**.

---

## 3 — Per-band grounding (decisive split)

| ID | Band | draw_exp | Grounding |
|----|------|----------|-----------|
| H1 | 42–58 | high | Mirror symmetry. ±8pp = residual contact-asymmetry + sampling SE (the ED-1013 fix cut raw bias 21.7→3.3pp; residual is ~±6pp, *shape-dependent and opposite-signed* across H1/C3 = noise, not structural). |
| H2 | 48–62 | high | Wedge (cuneus) modest edge at equal command (v9 §A.6 +2D off; Biddle — geometry alone weak). |
| H3 | 55–72 | high | Full envelopment reliably tells (Cannae; Sidnell). The one geometric edge that survives equal command. |
| H4 | 45–62 | high | Cannae proper (envelopment vs single-axis wedge); tight — the wedge tip can punch a holding centre. |
| H5 | 48–62 | high | Refused flank / oblique as the explicit envelopment counter (Leuctra 371 BC). |
| H6 | 48–60 | high | Oblique order edge (Leuthen 1757). Modest. |
| H7 | 48–62 | high | Manipular checkerboard flexibility (Pydna 168 BC). |
| H8 | 50–65 | high | Maniples absorb wedge penetration and flank it. |
| H9/H10/H11 | inverse bands | high | Reverses of H2/H3/H4 (asymmetry confirmation). |
| R1 | 0–30 | low | Open-field ranged loses to melee that closes (Crécy/Agincourt won only with terrain/stakes — out of scope). `low`: melee should *close decisively*, not stand off. |
| R3 | 42–58 | high | Ranged mirror — symmetry sanity. |
| C1 | **35–55** | high (decA) | Frontal cavalry vs steady unbraced close-order foot is **contested** (Burkholder). **REBASELINE from 52-80** — the old band was the misconception. Emergent 45.7%, now distinct from C2 (brace) and C5 (shock). |
| C2 | **0–30 (raw cav-a)** | high · `rawA` | Frontal cavalry vs a BRACED wall (hold+disc8+**brace tactic**) — the wall REPELS; cavalry rarely breaks it (Waterloo squares; Barua "easily beaten off"; Burkholder "a horse will not run into a solid object"). Judged on raw cav-a LOW (a repulse is a HOLD → high draws expected). |
| C3 | 42–58 | high (decA) | Cavalry mirror — side-symmetry control. |
| C4 | 75–95 | low (decA) | Mounted envelopment of an unbraced line — devastating (Cannae rear-charge; Adrianople 378; Boddy). Near-decisive, not literally certain (a few infantry wins). |
| C5 | **65–98** | low (decA) | Cavalry vs a genuinely SHAKEN line (morale 2 of start 6) — exploitation + pursuit. **Ceiling 90→98**: cavalry vs disordered foot is NEAR-TOTAL (Boddy dispersed 15,000; Hastings post-feint). The Phase-2 ceiling was set when this row was inert. |
| C6 | **0–30 (raw cav-a)** | high · `rawA` | Braced-shallow foot (hold+disc8+**brace**) — a faced brace still repels frontally. = C2. |
| C7 | **65–100** | low (decA) | Cavalry envelops a HOLDING line — brace bypassed from flank/rear; an immobile line that cannot turn to face is ANNIHILATED when resolved (Cannae/Adrianople) → decA saturates to 100. **Ceiling 90→100** (encirclement of the immobile is total). |

---

## 4 — Validation report (smooth-cohesion engine, multi, n=120; cavalry re-run 2026-06-16)

### 4.1 — Cavalry block: 7/7 (the 3 former "engine-defect" flags were GAUGE-CONSTRUCTION defects)

The three Phase-2 DIVERGE-hard flags (C2/C5/C6) were **re-diagnosed bottom-up** by reading the engine resolution code (`mass_battle/resolution.py`, `orchestration.py`). The result **inverts** the Phase-2 verdict: the engine's frontal-cavalry mechanics were already grounded and correct; the **gauge was not triggering them**.

- The brace-recoil (`PC_CHARGE_RECOIL=6`, calibrated vs Courtrai/Swiss/Waterloo) that punishes a charge into a prepared wall fires only on the **`brace` instruction** (`_unit_braced`). Phase-2 built "braced" as `hold`+disc8 *without* that instruction → the recoil never fired → the square held but never repelled. **Fix (gauge, not engine):** C2/C6 defenders carry `instructions=('brace',)`.
- The shaken-shock amplifier (`PC_SHOCK_SHAKEN_GAIN`) and `_morale_sigma` key off **`morale / morale_start`** ("shaken" = cohesion eroded *below* start — du Picq, relative not absolute). Phase-2's `make_unit` forced `morale_start = morale`, so C5's morale-2 line read as 100% relative morale — not shaken at all. **Fix (gauge, not engine):** `make_unit` accepts `morale_start`; C5 is morale 2 of start 6.

Neither fix touches the engine. With correct construction the historical behavior **emerges**, and the engine *differentiates* every regime:

| ID | emergent | verdict | history |
|----|----------|---------|---------|
| C1 contested | decA 45.7 | OK | frontal vs steady foot — contested (Burkholder) |
| C2 braced (+brace) | raw cav-a **1.7** | **REPELLED** | the square Ney could not break (Waterloo; Barua) |
| C3 mirror | decA 43.7 | OK | side-symmetry |
| C4 envelopment | decA 93.8 | OK | Cannae rear-charge (Sidnell; Boddy) |
| C5 shaken (m2/start6) | decA 95.6 (94.8 @ n=240) | OK | near-total rout of disordered foot (Boddy; Hastings) |
| C6 braced-shallow (+brace) | raw cav-a **1.7** | **REPELLED** | a faced brace repels (= C2) |
| C7 envelop holding line | decA 100.0 | OK | encirclement of the immobile is annihilating (Cannae) |

Braced-repulse (~2%) ≠ contested (~46%) ≠ shaken-shock (~95%) ≠ envelopment (~94–100%): the differentiation is **emergent from the already-grounded mechanics**, not band-fitting. C1/C3/C4 raw cav-a are unchanged from Phase-2; the `make_unit` additions are byte-exact for every instruction-less / `morale_start`-unset row (**H1 identical at 52.8**).

### 4.2 — Originals unchanged (Phase-2 tally stands)

The `make_unit` additions (`morale_start=None`, `instructions=()`) default to the prior hardcoded behavior, so the 13 H/R rows are byte-identical. Phase-2 holds: **VALIDATED H1, H3, H8, H10, H11; DIVERGE-soft H2, H4, H5, H6, H7, H9** — subtle formation edges washed to ~even by the ED-1013 cohesion pool (defensible per Biddle/Burkholder "geometry alone weak at equal command," but below the v9 §A.6 modest edge; a genuine residual, flagged not fitted, candidate future engine refinement). **Ranged: R1** loses open-field (directionally correct) but too-drawish; **R3** mirror unresolvable in 20 turns — ranged-resolution engine gaps. **Single mode:** all-draws at the 18-tick cap (tick-cap artifact; bands evaluated in multi).

### 4.3 — Latent engine flag (out of scope; NOT triggered by the gauge)

The reciprocal charge-recoil (`orchestration.py` ~L1647) does **not** zone-gate — it fires on any momentum differential into a `_unit_braced` defender, including a flank/rear charge. Historically a brace cannot repel what it cannot face (Burkholder). C7 therefore deliberately uses **hold-only** (no `brace` instruction), so the envelopment is not wrongly recoiled; a truly-braced-then-enveloped unit would expose this. **Fix candidate:** gate the recoil on the frontal (GREEN) octagon zone. Flagged, not fixed here.

---

## 5 — Open judgment calls (Jordan-vetoable)

1. **Metric switch** raw-A% → decisive split — structural; raw-A% was provably broken on symmetric mirrors. Draw rate retained as a separate validated dimension.
2. **`rawA` metric for the braced-repel rows (C2/C6)** — a repulse is a HOLD (high draws expected), so these are judged on raw cavalry win-rate LOW, not decA (which saturates at a tiny decisive *n*). New refinement (2026-06-16).
3. **C1 rebaseline** 52-80 → 35-55 — the old band encoded the cavalry-beats-unprepared-infantry trope Burkholder (2007) debunks. **Now validated** by differentiation: the engine produces C1 contested (46%) ≠ C5 shock (95%) ≠ C2 brace (2%), all emergent.
4. **The former C2/C5/C6 "engine defects" were GAUGE-CONSTRUCTION defects** — fixed by setting the `brace` instruction (C2/C6) and a genuine shaken `morale_start` (C5). The engine's brace-recoil and shaken-shock were already grounded/correct and are **untouched**; the historical behavior now emerges. (Supersedes the Phase-2 §4 "engine-defect, future-work" framing.)
5. **C5 ceiling 90→98** — cavalry vs disordered foot is near-total (Boddy 15,000 dispersed; Hastings); the Phase-2 ceiling was set when the shock was inert.
6. **C7 ceiling 90→100** — encirclement of an immobile (hold-stance) line that cannot turn to face is annihilating (Cannae); decA saturates to 100 when infantry is shut out.
7. **Latent: the charge-recoil does not zone-gate** (§4.3) — a fix candidate (gate on the frontal zone), flagged not fixed.
8. **Per-subunit stamina / line relief (§6, ED-1017)** — stamina pushed onto the Subunit; an engaged subunit drains while a reserve stays fresh, and the fresh reserve relieves the exhausted front (Sabin/Zhmodikov/du Picq/Clausewitz). Byte-exact single-subunit; `_fatigue_sigma` deliberately left unchanged (already sub-unit-scoped at its call site — NERS-E).
9. **Troop-taxonomy stat home (§7, ED-1018)** — the canonical §B.2 per-type stats (Power/Discipline/Morale) wired onto the per-subunit fields via `TROOP_TYPE_STATS` + `Subunit.of_type`. Pure gap-fill (transcribes an existing canonical table into a constructor); byte-exact. Deliberately maps only the three unambiguous integers — Armour→`dr` and Endur→`stamina` are left to inherit (no confirmed scale bridge), flagged here not guessed.

---

## 6 — Per-subunit stamina & line relief (depth as reserve) — ED-1017

**Mechanic (Jordan directive 2026-06-17).** Stamina moves from the Unit onto the **Subunit** as optional state (`None` inherits the parent Unit, so single-subunit / homogeneous units stay byte-exact). Each subunit drains its own stamina by *its* cells in contact and rests/recovers when not engaged; the combat pool reads the *contacting subunit's* stamina (`subunit_combat_pool` → `_stamina_pool_penalty(atom.eff_stamina)`). An engaged front subunit therefore tires while a rear reserve stays fresh, and rotating the fresh reserve forward restores the pool the exhausted front had lost — **depth becomes a stamina reserve**.

**Why this is historically real** (the top-down anchor required by the project-owner contract; the bottom-up anchor is the traced engine code, not a guess):

- **Roman battles were long, and sustained by line relief rather than one exhausting clash.** Sabin (2000), *Journal of Roman Studies* 90, 1–17, DOI [10.2307/300198](https://doi.org/10.2307/300198): Roman infantry combat lasted *hours*, resolving as a sequence of surges and lulls, and one of the four mechanics that structure it is the **role of the supporting troops behind the front line** — the *triplex acies* by which an engaged first line admits or withdraws through its supports (hastati → principes → triarii). A model in which a tiring front is **relieved by fresh ranks drawn from depth** is precisely what makes the long Roman battle intelligible.
- **The fighting line was rotated and relieved, not fought to destruction in place.** Zhmodikov (2000), *Historia* 49/1, 67–78: Republican heavy infantry fought in repeated short clashes with the forward ranks relieved — the reserve lines are a fatigue-management instrument, not merely a numerical backstop.
- **A tiring front loses combat effectiveness; depth that rotates fresh ranks sustains it.** Ardant du Picq, *Battle Studies* (the engine's existing `_fatigue_sigma` anchor): combat power is a function of cohesion and freshness; a thin line that cannot rotate wears out where a deep one does not.
- **Reserves renew and prolong the combat.** Clausewitz, *On War* III.12 ("The Reserve"): the reserve exists for the *prolongation and renewal* of the fight — the doctrinal generalisation of the same idea.

**Engine mapping.** Optional `Subunit.stamina/stamina_max`; `eff_stamina/eff_stamina_max` (own value else inherit Unit); `drain_stamina/recover_stamina` route writes to own-stamina-if-set, else to the inherited Unit (so a single-subunit unit reproduces the old `Unit.stamina` arithmetic exactly); `agg_stamina` (troop-weighted) for the unit-level reads (exhaustion-morale, `base_combat_pool`, the run report). Per-tick drain, phase-boundary recovery (`stamina_check` via a per-subunit `_subunit_depth`), and between-turn recovery all became per-subunit. The per-column fatigue sigma (`_fatigue_sigma`, a *second* fatigue channel) is **unchanged**: its call site already passes the *engaged subunit's* contact columns, so it is already sub-unit-scoped — adding an `atom` parameter would be unused apparatus (NERS-E).

**Validation.** Byte-exact against a clean pre-edit engine across 9 matchups (melee mirror / asymmetric / envelopment, ranged / volley, cavalry charge / braced / envelopment / shaken) × 20 seeds in the resolving multi-turn mode — identical state-vector digest. Rotation demonstrated: an engaged front subunit drained to 32/100 while a held reserve stayed at 100/100 (a divergence impossible under the old shared `Unit.stamina`), and the fresh reserve yielded a larger combat pool than the exhausted front.

`[mechanical-tier, Jordan-vetoable: which consumers go per-subunit, and that reserve relief is positional (the engine has no reserve-hold AI — a held reserve is shown via target_delay_ticks), are design calls — built bottom-up from the engine, anchored top-down on Sabin/Zhmodikov/du Picq/Clausewitz, logged for veto.]`

---

## 7 — Troop-taxonomy stat home (per-type per-subunit stats) — ED-1018

**Gap (2026-06-16 completeness audit).** The engine carried a troop-type *label* (`Subunit.troop_type`) and an inert role scaffold (`TROOP_TYPE_ROLES` / `ROLE_SPEC`), but a subunit's troop type had **no effect on its combat stats** — there was no "stat home" connecting a type to its Power / Discipline / Morale. With per-subunit stats (ED-1016) and per-subunit stamina (ED-1017) now in place, the subunit can finally *carry* a type's stats.

**Mechanic (Jordan directive 2026-06-17).** A canonical preset table, `orchestration.TROOP_TYPE_STATS`, transcribes the **TTRPG Power / Discipline / Morale** columns of the canonical BG unit table (`mass_battle_v30.md §B.2`) keyed to the existing snake_case taxonomy. `orchestration.stats_for(troop_type)` returns a type's preset (case-insensitive; `None` for an unknown type), and the constructor `Subunit.of_type(troop_type, shape, tier, starting_position, **kw)` fills `power` / `discipline` / `morale` / `morale_start` from that preset unless the caller overrides them. An unknown type fills nothing — the fields stay `None` and inherit the parent Unit, so nothing that does not call `of_type` changes (**byte-exact**).

**Source is the canon table itself; this is the purest gap-fill.** The bottom-up anchor is not a guess — it is the verbatim §B.2 table (Levy P1/D1/M2, Light Infantry P3/D3/M4, Heavy Infantry P4/D4/M5, Cavalry P5/D5/M5, Archer/Crossbow P3/D3/M3, Sling/Artillery P2/D2/M3, Knights Templar P5/D6/M6). The work is wiring an already-canonical, already-historically-grounded table into a constructor.

**Why the *ordering* is sound** (the top-down check required by the project-owner contract):

- **Differentiated troop quality and type is the settled basis of military history and of validated battle-modelling.** Sabin, *Lost Battles* (2007) — the same Philip Sabin as the §6 *JRS* source — reconstructs ~35 ancient battles with a model whose units are rated separately by **type** (heavy infantry, light infantry, cavalry, …) and by **quality** (levy / average / veteran), and that model reproduces historical outcomes. The §B.2 ordering this ED transcribes is the same shape: professional heavy foot steadier and more disciplined than levy, missile troops lighter and less able to hold a line, shock cavalry highest in single-blow power. The heavy / light / missile distinction itself is foundational and uncontested.

**Engine mapping.** `TROOP_TYPE_STATS` (data, in `orchestration` beside its accessor `stats_for` and constructor `of_type` — where the role accessors `roles_for` / `role_allowed` already live; the role *scaffold* data `TROOP_TYPE_ROLES` / `ROLE_SPEC` remains in `config`); `stats_for` (accessor, mirrors `roles_for`); `Subunit.of_type` (classmethod constructor). Only the three §B.2 integers are mapped. `dr` (the §B.2 Armour column) and `stamina` (the Endur column) are **deliberately left to inherit**: §B.2's Armour maps to a vs-Piercing DR scale (orch L413–417: None=0 / Light=1 / Medium=2 / Heavy=3) whose identity with the `Subunit.dr` field is unconfirmed, and Endur (1–6) has no clean bridge to the 0–100 stamina pool. Mapping either would be a guess at a scale; both are flagged for an explicit follow-up rather than invented.

**Validation.** Byte-exact: the 9-matchup × 20-seed multi-turn battery digest is unchanged from the pre-edit engine (`fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69`) — `of_type` is additive and unused by the gauge constructors. Differentiation demonstrated: `of_type` reproduces every §B.2 row exactly, and the stats separate combat on both channels — the combat **pool** via discipline (Levy 6 dice → Cavalry / Knights Templar 8 dice) and **damage** via the `(1+Power)` multiplier (Levy ×2 → Cavalry ×6). Caller overrides beat the preset; unknown types inherit the Unit.

`[mechanical-tier, Jordan-vetoable: the snake_case key set and the decision to map only Power/Discipline/Morale (deferring Armour→dr and Endur→stamina) are design calls — built bottom-up from the canonical §B.2 table, anchored top-down on Sabin's validated troop-type model, logged for veto. of_type maps stats only; unit_type (melee vs ranged) stays caller-controlled, since it is a role, not a stat.]`
