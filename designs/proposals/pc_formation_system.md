# P-C — Compositional Formation System (design-capture)

**Status: PROPOSAL — pending Jordan structural sign-off.** Not canon yet. Date 2026-06-02.
Intended home on acceptance: `designs/` (formation system) + reconciliation into `mb_engine_workplan.md` P-C body.

---

## 0. Provenance (what this is grounded in)

- **`[READ:]` engine, this session** — `tests/sim/mass_battle/{config,geometry,orchestration,percell,resolution}.py`: the emergent primitives (`oriented_pattern`, `octagon_angle`, `_support_along_vector`, `_defender_depth`, `_lanchester_strength`, `cell_speed`, `_charge_shock_sigma`, `_momentum_speed`), the `MIN_DISCIPLINE` gate, and the now-**retired** `SHAPE_OFF_MOD`/`SHAPE_DEF_MOD` (commit `e677a11f`).
- **ED-814 + prior conversation** — the formation grid is *not* a hand-authored 9-cell grid; it is an **adjustable allocation surface** (set intent → engine auto-distributes → manual override). "The Football Manager analogy is exact." The three-level surface + team-instruction layer + intervention-window model are recorded design, not invented here.
- **This session's emergence work** — Lanchester laws (form emerges from frontage/concentration), Command-only sigma base (quality from Command, not Size), and the SHAPE-mod retirement establish the through-line this doc extends.
- **Jordan principles (this conversation)** — (1) the Discipline/Command/Morale governance split; (2) **formations grant no flat bonuses — a template is a shape, effects emerge bottom-up.**
- Canonical mechanic references below tagged *(canon §A.x — recovered from prior design; verify/reconcile on canonization)* are not fresh-read this session and must be confirmed against `mass_battle_v30.md` before any canon edit.

---

## 1. Foundational principle — emergence, not decree

A formation is a **shape**: an arrangement of subunit cells on the grid (+ facing + roles). It carries **no flat dice/σ bonus**. Every tactical property emerges from how that shape meets the enemy, processed by the existing engine:

| Emergent channel | Engine primitive |
|---|---|
| numerical edge is *frontage-limited* (linear law) | `_lanchester_strength` (engaged contact columns) |
| depth backs the front rank | `_defender_depth`, `_support_along_vector` |
| facing/angle of attack matters | `octagon_angle`, `ANGLE_DEF_MOD` |
| penetration / shock / wrap | `cell_speed` (tip speed), `_charge_shock_sigma`, `_momentum_speed` |
| massed fire concentrates (square law) | volley square term (`K_SQUARE × shooter size`) |

This is the same discipline as the rest of the engine: **target the goal (emergent advantage), never the form (a decreed +2D).**

---

## 2. The three-level compositional surface (FM model, ED-814)

| Level | FM analogue | Valoria object | Governed by |
|---|---|---|---|
| **L1 — Army doctrine** | team mentality / tempo | standing posture across all units: **Aggression** (Cautious / Balanced / Pressing), **Cohesion-priority** (Hold-shape / Adapt-to-pressure) | **Command** |
| **L2 — Unit formation (shape)** | team formation (4-4-2 / custom) | a **shape** — default template (Line / Wedge / Column / Horseshoe / Arrowhead / Refused-flank / Gapped-line / …) **OR a custom allocation** (set %composition + shape intent; engine auto-distributes to cells; manual cell override). **A shape is arrangement only — no behavior, no bonus.** | adopt-gated by **Discipline** (`MIN_DISCIPLINE`) |
| **L3 — Subunit role + instructions** | player role + player instructions | each subunit is assigned a **role drawn from a menu gated by its troop type** (the FM position→role model, §3.5). A role bundles a typical shape + an **instruction package** (brace / hold / advance / charge / skirmish / refuse / lure …). E.g. heavy-infantry → **Shield Wall** (dense line + *brace*); cavalry → **Shock** (wedge + *charge*) or **Feint** (*lure*). | menu gated by **troop type**; adherence gated by **Discipline**; concerted ploys executed + capped by **Command** |

L2's "custom allocation" **is** ED-814's adjustable surface, and the canonical A.6 formations become **shape templates** here — names for arrangements, **with no dice rules and no behavior attached**. Behavior lives at L3 as instructions (§3.5); the flat-bonus parts of A.6 are superseded (§8). **"Shield wall" is therefore a *role* (heavy-infantry + brace), not a shape** — see §3.5.

---

## 3. Governance — which stat gates what (your split)

The three stats form a triangle: **Command orchestrates → Discipline holds → Morale sustains.**

**Discipline — the subunit's ability to MAINTAIN its formation and ADHERE to its tactics.**
- Adopt-gate: a complex shape requires the drill to hold it — `MIN_DISCIPLINE` (Line 1 / Refused-flank 3 / Arrowhead 4 / Horseshoe 5 / Gapped-line 5) *(canon ED-815 — in code)*.
- Hold-under-stress: Discipline degrades under pressure, flanking, and enemy stratagems; at **0 the formation breaks** (the only state that removes all combat capability) *(canon §A.6/§A.12 — recovered)*.
- Resist enemy stratagems: e.g. the pursuit decision in a False Retreat is the pursuer's **Discipline** check.
- Persists between battles *(canon PP-712 — recovered)*; it is the unit's drilled cohesion, not its mood.

**Command — orchestration, interpretation, and stratagem.** Command (= **derived: Charisma primary + Cognition secondary**, committed `2cf3feb6` / ED-899; drives the sigma-leverage base) is what a general *does*:
- **maintain / adapt Strategy** — set and change L1 doctrine and L2 assignments through the battle;
- **interpret battlefield events** — recognise an enemy stratagem (e.g. a feint) before committing (a Command check);
- **reinforce Discipline** and **rally Morale** — the general's interventions restore the other two stats;
- **run concerted stratagems / ploys** — execute False Retreat, Envelopment, Hammer-&-Anvil (a Command check to execute);
- **orchestrate subunits for cohesiveness** — the **sub-unit coordination limit** (how many subunits can act in concert) scales with Command; beyond it, subunits act without coordination.

**Morale — will to fight.** The rout resource: degrades on triggers, **rallied by Command**, resets each battle *(PP-711 — recovered)*. It produces the historically-correct *rout-decided, not annihilation* ending (validated this session: mirror ends ~30% casualties, loser routs at ~70% strength).

> Net: a formation's *shape* and *tactics* are only as good as the **Discipline** holding them; a *plan* and its *stratagems* are only as good as the **Command** running them; and the whole thing lasts only as long as **Morale** endures.

---

## 3.5 Roles, instructions, and troop-type gating (the FM position→role model)

**A role is not a shape.** A role = a **troop-type-gated** package of a typical shape + an **instruction set**; its effects emerge from primitives, never a flat bonus. "Shield wall" is the canonical example of the category error this fixes — it is *heavy-infantry + brace*, not a shape.

**Troop type gates the role menu** (FM position→role): a unit can only be assigned a role its type permits.

| Troop type (FM "position") | Gated roles — shape + instructions | Emerges via | Image |
|---|---|---|---|
| **Heavy infantry** | **Shield Wall** (dense line + *brace*), **Hold** (line + *hold*), **Anvil** (line + *hold-to-pin*), **Push** (line + *advance*) | density (B), frontage, depth-backing | 🟣 guard line |
| **Light infantry** | **Skirmish** (loose + *harass*), **Gap** (gapped line + *channel*), **Pursue** | low density, gap-channeling | 🟠 gap infantry |
| **Cavalry** | **Shock** (wedge + *charge*), **Flanker** (column + *envelop*), **Feint** (line + *lure/retreat*), **Screen** | charge-shock, speed, momentum/wrap | 🔴 cavalry; 🟡 shock-arrowhead |
| **Archers / ranged** | **Volley line** (line + *volley-hold*), **Harass** (loose + *shoot-move*) | square-law volley | 🟢 archers |
| **Any (held)** | **Support / Reserve** (*hold back + reinforce*) | depth backing | 🔵 support |

**Instructions are the behavior layer, and they modulate primitives — never add a flat number:**
- *brace* → close ranks: **raises effective density** (B) → penetration-resistance + steady front + charge-shock absorption; sets `cell_speed → 0` (the emergent "can't advance"). **Heavy-infantry-gated; held by Discipline.**
- *skirmish* → **lowers density**: flank-immune (no contiguous flank) but fragile to concentration.
- *charge* → concentrates density + speed at the point → shock + penetration.
- *hold / refuse / lure* → posture/positioning whose effects emerge from facing, geometry, and the stratagem chain (§5).

**This resolves the §1 A/B/C question.** Since shield-wall = *heavy-infantry + brace*, the toughness question becomes "what does the brace instruction do through primitives":
- **A (depth-as-defense) — rejected as the brace mechanism.** Depth is a *shape* property, instruction-blind; it would make a marching column as tough as a braced wall. (A may persist as a minor *general* arrangement primitive — a separate decision — but it does **not** encode "brace.")
- **B (density-as-defense) — the mechanism.** The brace *instruction* raises effective density; density confers the defense, and it **generalizes** (skirmish lowers it, charge concentrates it, rout collapses it). The per-cell layer already tracks troop density + depth-damping, so B is partly present — the build is **instruction-modulated density**.
- **C (braced line) — the architecture.** Correct *placement* (role = shape + instruction); B is the *mechanism* that fills it. **C + B compose; A is out.**

Gating summary: **troop type** bounds what's selectable · **Discipline** holds a role's instructions under stress (brace breaks → density collapses → wall fails) · **Command** executes concerted ploys across roles and caps how many subunits coordinate.

---

## 4. Shapes — intent → emergent mechanism (no dice rules)

*(Shapes are arrangement only; behavior is the L3 instruction layer, §3.5. "Shield wall" lives in §3.5 as a role, not here.)*

| Shape | Geometry | Effect emerges from | (NOT) |
|---|---|---|---|
| **Line** | even, single-deep frontage | baseline frontage | — |
| **Wedge / Arrowhead** | narrow point, tip faster (`cell_speed`=2) | concentrates contact on a narrow enemy frontage (local Lanchester superiority) + penetration (momentum / charge-shock) | ~~+2D Off~~ |
| **Skirmish** | loose, spread (low density) | no contiguous flank to turn (flank-immune) **but** weak per-cell backing (fragile to concentrated heavy) | ~~−1D vs Heavy~~ |
| **Refused flank** | one wing withdrawn / anchored | no exposed flank cell that side; cost = fewer cells forward | ~~flat immunity~~ |
| **Horseshoe** | concave | contacts a penetrating enemy on three sides (envelopment / wrap geometry — Cannae) | ~~bonus~~ |
| **Gapped line** | line with intervals | channels the enemy into the gaps (local concentration against the lured) | ~~bonus~~ |
| **Column** | deep, narrow | speed/penetration on the march; brittle frontage if caught | ~~+1 speed flat~~ (emerges from `cell_speed`) |

Every "(NOT)" cell is a flat bonus that is **gone** — the property now emerges or it doesn't exist.

---

## 5. Tactics & stratagems — declarable, Command-executed, Discipline-resisted

The canonical A.8 tactics become **declarable maneuvers/stratagems** at L1/L2, each a Command-run ploy resolved against the opponent's Command (to recognise) and Discipline (to resist) — **not** flat modifiers:

| Stratagem | Execute (Command) | Opponent counter | *(recovered canon)* |
|---|---|---|---|
| **Envelopment** | commit fast wing to a flank | Refused-flank geometry negates | A.8 |
| **False / Feigned Retreat** | disengage to lure | recognise (Command) → else pursue is a Discipline check; success re-engages on the broken pursuer | A.8 + stress-test chain |
| **Ambush** | from terrain/concealment | scouting | A.8 |
| **Concentration** | mass on one target | exposes own flanks | A.8 |
| **Hammer & Anvil** | pin + fast envelop | break the anvil first | A.8 |

These are *concerted ploys the Command runs*, exactly your "run concerted strategems/ploys like a False Retreat." Open question (ED-136 vector): should some stratagems degrade the **opponent's Discipline** directly (organisational disruption, not casualties)? — see §9.

---

## 6. Worked example — your uploaded asymmetric formation

Reading the 15×15 image by role:

| Colour | Role | Shape / position | Intent |
|---|---|---|---|
| 🟡 yellow | **aggressive arrowhead** | wedge, top — pointed at one side | break that side hard |
| 🟠 orange | **gap infantry** | two blocks with a gap, upper | pin / channel the centre |
| 🔵 blue | **support & buffer** | mid blocks behind the line | back the front, absorb |
| 🟢 green | **archers** | mid blocks, ranked | volley (square-law) onto the pinned centre |
| 🟣 purple | **guard line** | verticals + base bar | anchor / hold the formation's spine |
| 🔴 red | **cavalry (flank)** | left verticals, fast | envelop once a flank opens |

**The plan, and how it emerges (not decreed):**
1. **Pin the centre** — purple guard line + orange gap infantry present a dense, deep frontage; the enemy that engages it makes little progress (Lanchester frontage cap + depth-damping). Green archers volley the pinned mass (square-law concentration).
2. **Break one side** — the yellow arrowhead concentrates contact on a narrow slice of the enemy's flank (local numerical superiority via the linear frontage term) and penetrates (tip `cell_speed` + charge-shock). The formation is **asymmetrically biased** — more committed force on the breaking side.
3. **Envelop** — once that flank gives, the red cavalry (speed advantage) turns the exposed edge and works inward (momentum / wrap geometry), the horseshoe/Cannae outcome.

The whole sequence is gated by your split: **Command** sets the asymmetric doctrine, recognises when the flank has broken, and times the cavalry commit; **Discipline** keeps the arrowhead and guard line in shape under pressure (and `MIN_DISCIPLINE` lets them adopt those shapes at all); **Morale** decides when the broken enemy side routs (which is what actually opens the envelopment).

---

## 7. Bottom-up engine mapping

- **`Formation` on `Unit`** — `template_id | custom_allocation_grid`; drives cell layout (the allocation→cells **solver** replaces the hardcoded `*_cells` selection). Auto-distribution = the solver (ED-814 core); manual override = per-cell edit.
- **`troop_type` → role gating + `role` + `instructions` on `Subunit`** (§3.5) — a `TROOP_TYPE_ROLES[troop_type]` table gates the selectable roles (FM position→role); a `role` sets a shape + an `instructions` set; **instructions modulate primitives** (brace → +density, skirmish → −density, charge → point-concentration), never add flat numbers. The one behavior-cascading addition is the **density primitive (B)**: how much `brace` raises effective density and how much density damps penetration — calibrated + validated against the gauge (it will move the bands).
- **`doctrine` on the army/side** — L1 Aggression + Cohesion-priority.
- **No per-shape σ injection.** Effects flow **only** through the resulting geometry into the existing primitives (§1 table). This is the load-bearing constraint: the solver outputs cells; the engine does the rest. (The retired SHAPE mods guarantee no flat shortcut exists.)
- **Control cadence** — deploy → set doctrine → assign roles → **~5–20 intervention windows per battle** (Command actions: rally / reinforce / execute stratagem / adapt doctrine), *not* per-tick control. Matches historical generalship and the recorded SI/FM pivot.

---

## 8. Canon reconciliation required (flagged, not done here)

- **Remove the flat dice rules from canonical A.6** (Shield-wall +2D Def, Wedge +2D Off, Skirmish −1D vs Heavy, Column +1 speed, …) — top-down assertions the engine already ignores and this commit retired. Same treatment as PP-233.
- **Reconcile A.5 Command** — the canon doc still reads `⌈(Cha+Cog)/2⌉` (equal weight); the engine now uses Charisma-primary `round((2·Cha+Cog)/3)` (ED-899). Update the doc.
- Both fold into the ED-899 canon-doc reconciliation already flagged.

---

## 9. Open — Jordan decisions

**Resolved this turn:** shield-wall is a *role* (heavy-infantry + brace), not a shape — `ShieldWall`-as-shape reverted. Roles are **troop-type-gated instruction packages** (FM position→role, §3.5). The §1 toughness question is settled: **C (architecture) + B (density-via-brace-instruction); A rejected** as instruction-blind. Bracing is an instruction; troop type gates the role menu; Discipline holds it.

Still open:
1. **Density primitive (B) magnitude** *(new, the key one)* — how strongly does `brace` raise effective density, and how strongly does density damp penetration? This is the one behavior-cascading mechanism; calibrate it so a braced shield wall is a genuine frontal fortress (not my failed narrow-geometry attempt) **without** over-tuning. Validate on the gauge; it will shift the bands.
2. **Confirm the troop-type→role gating table** (§3.5) + the instruction vocabulary (brace / hold / advance / charge / skirmish / refuse / lure / harass). Add/cut roles per troop type.
3. **`MIN_DISCIPLINE` as a hard gate vs smooth emergence** — discrete adopt-threshold, or smooth drift the further Discipline sits below a shape/role's complexity?
4. **Do stratagems degrade opponent Discipline directly?** (ED-136 vector.)
5. **Intervention cadence** — fixed windows, or Command-count-derived?
6. **Custom-allocation UX granularity** — %composition + shape intent only, or full cell-level authoring as the power tier?
7. **Subunit coordination limit** — scales with Command (cap?); TTRPG cap was 3.

---

## 10. Citations

- `[READ:]` `tests/sim/mass_battle/{config,geometry,orchestration,percell,resolution,engine}.py` (this session).
- ED-814 (adjustable allocation surface), ED-815 (`MIN_DISCIPLINE`), ED-899 (Command-only base; emergence), ED-136 (Discipline-via-stratagem, open).
- Prior conversation: the three-level FM surface + SI/FM intervention pivot + team-instruction layer (recorded design).
- This session (Jordan, 2026-06-02): shield-wall is a *role* not a shape; roles = troop-type-gated instruction packages (FM position→role); bracing is an instruction; the §1 toughness resolution C+B / reject A.
- `mass_battle_v30.md` §A.5 (Command), §A.6 (formations), §A.8 (tactics), §A.12 (rout/morale) — *recovered; verify on canonization.*


## 11. Validation status & emergent counter-cycle (measured top-down vs the research; 2026-06)

**Committed mechanics** (engine `tests/sim/mass_battle/`):
- Report-grounded taxonomy + `ROLE_SPEC` (role = shape + instruction package) + `mounted_archers` — commit `dd3d7a1b`.
- **Brace mechanism** — commit `7691eb6a`. The brace instruction (a) engages the charge-shock gate without the hold-stance offense penalty, and (b) adds a reciprocal charge-recoil (`PC_CHARGE_RECOIL`, prep = discipline x depth): a charge into a braced+deep+disciplined wall shatters the charger. Gated by the brace instruction so instruction-less scenarios are byte-exact.
- **Missile-density coupling** — commit `a6ae38ad`. Volley casualties scale with the target formation's `col_grid` density (`_volley_density_mult`): packed/deep columns bleed more, dispersed/shallow less. Ranged-only path so melee is byte-exact.

**Emergent counter-cycle**, validated on `gauge_mb` (40 seeds, `PER_CELL=1`), no flat bonuses:

| Edge | Status | Measured |
|---|---|---|
> Validation anchors are restricted to the research report's in-period (pre-firearms) battles. Earlier drafts cited Waterloo/Albuera (historically apt but Napoleonic, outside the report's scope) — corrected to the report's own anchors.

| pike-beats-cavalry (frontal, prepared) | EMERGENT (brace mechanism) | braced+deep+disc 75% / shallow-green ridden down 0% (post arch-fix #1) / braced-vs-inf neutral. Courtrai/Swiss/Hussite. |
| cavalry-rides-the-shaken | EMERGENT (`PC_SHOCK_SHAKEN_GAIN`) | the same prepared wall, wavering, 75% -> 28%. Hastings (once the wall broke)/Adrianople. |
| cavalry-catches-archers | EMERGENT (`RANGED_MELEE_SIGMA`) | ranged in melee vs cavalry: defender 55% -> 5%. |
| missiles-attrit-the-dense | WIRED, direction-correct | mult Line-t4 1.43 / t2 0.5; dense -0.6pp / shallow +0.5pp ON-vs-OFF. Small in single-engagement (volley is a brief DR-eaten chip); compounds at the standoff/multi-turn scale. Carrhae/Agincourt. |

**Measured baseline** (the finding that drove the brace mechanism): the pre-brace primitives did NOT produce pike-beats-cavalry. A braced *shape* / hold-stance dented a charge but the hold-stance was net-negative (traded offense for too little protection), and depth — not brace — was the de-facto anti-cavalry primitive; the charger paid no cost for hitting a braced wall. The brace mechanism supplies the missing reciprocal term.

**Open gaps** (not closed here):
- **KITING** (the research's #1 troop type): mobility-missile standoff / retreat-and-shoot at the multi-turn scale; also the amplifier that makes missile-density decisive. Next priority.
- **TERRAIN** (the research's #1 variable): a separate scene/territory layer, not P-C.
- Restore the `0.806/0.800/0.781` EV entries to the reconstructed `sim_verification_ledger.json`.
