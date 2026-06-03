# Martial-Tradition Ability Armature — Valoria Combat Engine
**Provisional · for developing the equippable tradition abilities · companion to `combat_engine_v1`**

This is an **armature**, not a finished ability list: the framework on which abilities are built — the categories an ability can target, the disciplines for grounding it, the per-tradition source material it is drawn from, and the workflow to add one and wire it. It exists so ability development stays consistent, grounded, and invariant-safe instead of ad hoc.

It assumes the scaffold already committed (`7d9fa28`): traditions grant **equippable abilities** that *modulate* the universal combat vocabulary; the channel-weights are the **substrate competences**; abilities are **equipped modulators on top** (`c.equipped`, default empty → no change).

---

## 1. Principles (the disciplines every ability obeys)

1. **Modulate, never unlock.** Every fighter has the whole vocabulary (all phases, all competences) at a baseline. An ability *improves or biases* a competence/phase; it never gates a technique behind a tradition. A fighter with no abilities still fights fully.
2. **Substrate + modulators.** The channel-weights are the baseline competence profile (the substrate). An ability is a learned modulator layered on top. This generalizes the old "8 fixed tradition profiles" into "competence substrate + equipped modulators."
3. **Invariant-safe by construction.** Default (no abilities equipped) = no change. Any ability must be a no-op when unequipped; the validated invariant suite must be byte-identical for a no-ability fighter.
4. **Bottom-up + top-down grounding (mandatory).** Each ability must name (a) a **documented technique** from the tradition (bottom-up) and (b) the **real martial/historical precedent** it models (top-down). An ability that cannot cite both is not earned — do not invent it.
5. **Source-tier honesty + the selection-effect.** Tag each ability with its source tier (S1 primary/critical · S2 peer-reviewed · S3 specialist · S4 general · S5 blog/vendor; a claim's grade ≤ its best source). The corpus's central lesson is the **selection-effect universal**: patterns from the best-documented traditions (German/Italian/Japanese) were over-projected onto all. So abilities are **confident only for the well-anchored core**; priority-gap traditions get **no ability until an S1/S2 anchor exists**. In particular, counterattack-prestige is a **European/Japanese** observation, not universal.
6. **Bounded, Class-C values.** Ability magnitudes are tunable (Class-C, Jordan-vetoable) and must respect the engine's safeguards (e.g. the tanh seizure cap bounds any `seize` ability to ~+8pp). Calibrate against the invariant suite; an ability that breaks an invariant is mis-valued.

---

## 2. The category vocabulary — what an ability can target

An ability targets a **lever**, addressed by two axes: a **phase** (when in the engagement) and a **competence** (which skill). The armature spans the full cross-product; not every cell needs an ability, but every ability lives in one.

### 2a. Phases (the engagement state machine)
| Phase | What happens | Example levers |
|---|---|---|
| **Approach** | gauging, closing the measure, stop-hits from the longer weapon | close-rate, stop-hit, reach-reopen |
| **Initiative / seizure** | who holds the Vor — pre-contact seizure + in-fight Vor/Nach shifts | `seize`, init-decay/hold, Indes steal |
| **Exchange** | the closed tempo-gated contest: read → mode → resolve → counter | read, mode (parry/dodge/wind), commit, counter |
| **Separation / reopen** | creating distance, disengaging, pursuit | reopen, disengage (cavazione), Nachreisen |

### 2b. Competences (the skills, = the channel substrate + mechanics)
| Competence | Substrate channel | Engine surface |
|---|---|---|
| **Measure** | `measure` | closing, reach, the misura/maai distance game |
| **Balance** | `balance` (see §3 — *agi-governed, not a stat*) | dodge, stance, anti-overcommit, footwork |
| **Reading** | `visual` (anticipation) + `tactile` (Fühlen, in the bind) | the read contest, mode selection |
| **Seizing** | `precommit` + `tempo` | seizure score, the Vor |
| **Countering** | `tempo` | single-time counter (Indes), two-time riposte |
| **Parrying / defending** | (mode-shaped) | parry / dodge / wind |
| **Striking** | `leverage` (force) | the blow: degree, target, armour-defeat |
| **Tempo** | `tempo` | cadence, the counter-window, commitment discipline |
| **Leverage / binding** | `leverage` | the bind, Stärke-Schwäche, winding |

### 2c. The lever map (category → engine lever → wiring status)
Live levers are wired at their engine sites *now*; pending levers are registered but inert until the channel-weight sites route through `eff_cw` (the channel-wiring pass).

| Lever | Category | Op | Status |
|---|---|---|---|
| `seize` | initiative / seizing | `+` (bounded ~+8pp by tanh cap) | **live** |
| `counter_success` | exchange / countering | `+` | **live** |
| `counter_select` | exchange / countering | `*` | **live** |
| `anti_overcommit` | exchange / tempo (discipline) | `+` | **live** |
| `measure` | approach / measure | `*` | pending (channel) |
| `tempo` | exchange / tempo | `*` | pending (channel) |
| `leverage` | exchange / binding+striking | `*` | pending (channel) |
| `visual` / `tactile` | exchange / reading | `*` | pending (channel) |
| `precommit` | initiative / seizing | `*` | pending (channel) |
| `balance` | balance (agi-derived) | `*` | pending (channel; see §3) |
| `reopen` / `disengage` | separation | `+`/`*` | **not yet built** (concrete-mechanics queue) |

---

## 3. Balance is a derived competence, not a base statistic

**(Per Jordan, this session.)** Balance is **not** a character stat. It is **governed by the Agility attribute** and **modified by abilities and combat circumstance/context**:

```
effective_balance = f(Agility) × poise(context) × ability_factor('balance')
```

- **Agility** is the attribute source (an agile fighter has better footing). The former `balance` stat is removed; `balance_eff` sources from `agi`.
- **Context** is the dynamic **poise** (kuzushi / off-balance disruption, recovering each beat) plus any circumstance (footing, terrain, crowding — as such context is modelled).
- **Abilities** modulate it via the `balance` lever (e.g. Destreza *compás* footwork).

Consequences for the armature: a "balance" ability is a **competence modulator over an agi-derived quantity**, not a stat buff. (Implementation note: the stat→agi rework is queued; until it lands, `balance` abilities target the same `balance` lever, which simply re-sources from `agi`.)

---

## 4. The ability template

```
'<key>': dict(
    tradition = '<german|italian|spanish|japanese|english|chinese|...>',
    grade     = '<S1/S2|S2|S2/S3|...>',     # source tier — the claim's grade ≤ its best source
    lever     = '<seize|counter_success|measure|...>',  # one lever from §2c
    op        = '<+|*>',                      # additive bonus, or multiplicative factor
    value     = <number>,                     # Class-C, bounded, calibrated vs invariants
    desc      = "<technique name> — <one-line mechanism>",   # the documented technique (bottom-up)
)
# top-down anchor recorded in the desc or the dev log: the real precedent it models.
```

A new ability is legitimate only when it names a documented technique (bottom-up) **and** a real precedent (top-down), carries a source tier, targets one lever, and is a no-op when unequipped.

---

## 5. Tradition source material, by category (the body of the armature)

Each tradition's documented techniques, sorted into the §2 categories, from which abilities are drawn. Confidence follows the source tier. **This is the menu**: not every entry is built yet; build per §6, grounding each.

### German — Kunst des Fechtens / Liechtenauer  ·  **S1/S2** (Anglo 2000; Forgeng eds.; the glosses)
| Category | Technique | Lever | Built? |
|---|---|---|---|
| Seizing | **Vorschlag** (the first strike that takes the Vor) | `seize` | ✅ `vorschlag` |
| Countering / reading | **Indes / Fühlen** (the simultaneous moment; feeling the bind) | `counter_success` (+`tactile`) | ✅ `indes` |
| Binding / striking | **Stärke-Schwäche / Winden** (strong-weak of the blade; winding) | `leverage` | registered `staerke_schwaeche` (pending) |
| Striking / countering | **Meisterhäue** (master-cuts: Zornhau, Krumphau, Zwerchhau, Schielhau, Scheitelhau — break guards / counter in one tempo) | `counter_success` or a strike lever | candidate |
| Separation / pursuit | **Nachreisen** (travelling-after — exploit the recovery) | `reopen`/pursuit | candidate (needs the reopen lever) |
| Parrying | **Versetzen / Absetzen** (displacing; setting-aside parry-riposte) | parry mode | candidate |

### Italian — Fiore/Vadi → Bolognese → rapier (Capoferro, Fabris)  ·  **S2** (Novati 1902; AGEA eds.)
| Category | Technique | Lever | Built? |
|---|---|---|---|
| Tempo / countering | **Mezzo tempo / contratempo** (half-time counter in the opponent's tempo) | `counter_select` (+`tempo`) | ✅ `mezzo_tempo` |
| Measure | **Misura** (distance management) | `measure` | registered `misura` (pending) |
| Binding / measure | **Stringere** (constraining the blade, gaining the line) | `leverage`/`measure` | candidate |
| Parrying / play | **Gioco stretto/largo** (close/wide play register) | mode bias | candidate |

### Iberian — La Verdadera Destreza (Carranza, Pacheco) + common destreza/montante  ·  **S2/S3** (Valle Ortiz; AGEA) — *partly reliable, flagged*
| Category | Technique | Lever | Built? |
|---|---|---|---|
| Measure / leverage | **Atajo** (blade-constraint / measure off the círculo) | `measure` | registered `atajo` (pending; S2/S3) |
| Balance / footwork | **Compás** (the geometric steps) | `balance` (agi-derived, §3) | candidate |
| Measure / geometry | **Ángulos / the círculo** (the geometry of distance) | `measure` | candidate |

### Japanese — koryū (san-dai genryū)  ·  **S2** (budō-gaku / J-STAGE)
| Category | Technique | Lever | Built? |
|---|---|---|---|
| Seizing / countering | **Sen** — *sen-sen-no-sen* (pre-emptive), *sen-no-sen* (simultaneous seize), *go-no-sen* (response counter) | `seize` / `counter_*` | ✅ `sen_no_sen` (seize); *go-no-sen* a counter candidate |
| Measure | **Maai** (combative distance) | `measure` | candidate |
| Reading | **Suki / metsuke** (the opening; the gaze) | `visual` | candidate |
| Separation | **Zanshin** (continued awareness / follow-through) | separation | candidate |

### English — Silver, *Paradoxes of Defence*  ·  **S2**
| Category | Technique | Lever | Built? |
|---|---|---|---|
| Tempo / discipline | **True & false times** (hand-body-foot timing hierarchy) | `anti_overcommit` (+`tempo`) | ✅ `true_times` |
| Measure / judgment | **The four governors** (judgement of distance, time, place, motion) | `measure`/`visual` | candidate |

### Chinese — Ming canon (Qi Jiguang *Jixiao Xinshu*; Cheng Zongyou)  ·  **S2 via Shahar — CAUTION**
The Ming manuals are **mnemonic shorthand**, not recoverable systems (Wetzler; Kennedy & Guo), and Shahar's anchor is **myth-criticism**, not a technique catalogue. Treat Chinese technique-abilities as **provisional/thin**: at most a conservative measure/reach modulator, explicitly flagged. Do not project the European counter-prestige here.

### Mamluk furūsiyya  ·  **S2** (al-Sarraf 2004) — *not currently an engine tradition*
Equestrian-military genre (lance/sword/archery). Recorded here for completeness; build only if a furūsiyya tradition is added to `tradition.py`.

### Priority-gap traditions — **NO abilities until S1/S2 anchored**
Polish szabla, Hungarian sabre, Ottoman matrak, Thai krabi-krabong, Sikh gatka, Indian *Dhanurveda*, Persian *zurkhāneh* — and **Filipino FMA**, which the corpus does **not** anchor at S1/S2 (treat as unanchored: flag heavily or omit). Their "high" grades in earlier corpus rounds were **not earned**. Leaving them unrepresented is the selection-effect discipline in action, not an oversight.

---

## 6. The development workflow (adding an ability)

1. **Pick the cell.** Choose a phase × competence (§2) and the lever it maps to (§2c).
2. **Ground it.** Find the documented technique (bottom-up) and the real precedent (top-down). Record both + the source tier. If you cannot cite both, stop — flag the gap, do not invent.
3. **Define the modulation.** Pick `op` (`+` additive / `*` multiplicative) and a provisional `value`. Add the entry to `ABILITIES` per the §4 template.
4. **Wire it** (if not already): discrete levers hook at their engine site; **channel levers** go live only once that channel's `channel_weight` sites route through `TR.eff_cw(c, ch)` (the channel-wiring pass).
5. **Validate invariant-safety.** With the ability *unequipped*, the full invariant suite must be unchanged. With it equipped, the effect must be directionally correct and bounded.
6. **Calibrate.** Tune `value` against the invariants and the relevant matchups; respect the engine safeguards (caps/tanh). Magnitudes are Class-C.
7. **Log + commit.** Record the bottom-up/top-down anchors and the calibration; commit (Jordan-vetoable).

---

## 7. Current state (scaffolded / live)

- **Live levers:** `seize` (Vorschlag, Sen-no-sen), `counter_success` (Indes), `counter_select` (Mezzo-tempo), `anti_overcommit` (True Times). Each shows a positive, bounded edge; values provisional.
- **Registered but inert (channel-wiring pending):** `staerke_schwaeche`, `misura`, `atajo` — go live with the `eff_cw` sweep across the ~21 channel-weight sites.
- **Not yet built (concrete-mechanics queue):** the `reopen`/`disengage` lever (cavazione/durchwechseln, Nachreisen) and the body-void counter variant.
- **Balance:** to be re-sourced from Agility (§3) — code change queued.

This armature is provisional and meant to be revised; it records the framework and the grounded menu, not a frozen ability set.
