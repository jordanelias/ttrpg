# Tactics-Ogre / FFT-style ability slots — the Valoria-combat parallel (PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · the unlock-and-equip exercise**

**Frame: the Tactics-Ogre / Final-Fantasy-Tactics skeleton — a growing *library* of unlocked abilities, a *limited*
set of *categorised* equip slots, and a *class/job* that gates what you unlock and sets your base profile — is the
concrete mechanism for the "bounded, earned customization" the reconciliation landed on. The slot *limit* is the
bound; learning-through-method is the earned cross-training; the categories are the legibility. It is not a turn
away from the prior conclusion — it is its missing apparatus, and it resolves the four tensions the free-flat-atomic
model failed (identity dilution, combinatorial balance, the dial-heavy library, legibility-at-scale). Grounded:
every slot category below maps onto resolution levers the engine *already* exposes (enumerated, not invented).**

`[READ: wrapper.py, systems.py, config.py, tradition.py — the live hook inventory grepped this session]`
`[SELF-AUTHORED — bias risk: continues my own ability-system thread; written to map a precedent, not to defend prior output]`

---

## §1 — The precedent, accurately

Both games share one structure (fine details differ by title; this is the robust core):

- **Job / Class.** A unit *is* a job (Knight, Archer, Wizard…). The job sets the base profile (stats, what equips)
  and the default command set, and gates progression through a **job tree** (prerequisites).
- **Points → learning.** Acting in a job earns points (FFT's JP; TO's skill/class progression). Points *unlock*
  abilities **within that job**, **permanently** — once learned, an ability stays in your library.
- **Limited, categorised equip slots.** You own far more than you can equip. FFT's four categories:
  **Action** (your command set, plus *one secondary* action set borrowed from any unlocked job), **Reaction**
  (one, triggers on an event — Counter, Auto-Potion), **Support** (one, passive — dual-wield, Martial Arts),
  **Movement** (one — Move+1, Teleport). Tactics Ogre: a learned skill pool, a bounded number of equipped skill
  slots, action/auto types, finishing moves on TP.
- **Bounded cross-class.** The depth is the *secondary* set + the borrowed reaction/support — you learn an ability
  in its job, then equip it regardless of current job, **within the slot limit**. That limit is what keeps the
  build space bounded rather than a free soup.

The build decision is therefore never "pick any N of everything" — it is **"which of my unlocked abilities do I
slot, given my class and my limited slots."** That is the whole game of the system.

---

## §2 — The parallel mapping

| Tactics-Ogre / FFT | Valoria personal combat |
|---|---|
| **Job / Class** | **Method** — the 8 historical schools + ~6 mechanical methods (Binder, Duelist, Skirmisher, Breacher, Counter-fighter, Pressure-fighter). Sets the base channel profile + default action set + node-preference. The identity layer. |
| **JP / skill points** (learned per job, permanent) | **Training** — fighting/drilling in a method unlocks its techniques permanently into your library. The method-tree gates which methods you may train. |
| **Action set + 1 secondary** | **Action slots** — your method's core techniques (always present) + a bounded number of slotted techniques, including one cross-method set (the FFT secondary). |
| **Reaction (1)** | **Reaction slot** — one triggered answer to the opponent's commit. |
| **Support (1)** | **Support slot** — one always-on competence. |
| **Movement (1)** | **Footwork slot** — one measure-control technique. |

Your **method** is your job; your **library** grows by training; your **loadout** is four categorised, limited
slots over that library.

---

## §3 — The four slot categories, grounded in real engine levers

Each FFT category maps onto a cluster of levers the engine already fires, at a specific node of the state graph
(Out-of-contact → Closing → Closed exchange → Bind → resolve). The hook names below are **live in source**.

**ACTION — what you do on your beat** *(the Closed-exchange + commit node)*
The offensive maneuvers: the feint (`systems.feint_eval`, weighted by `eff_cw` tempo/visual/precommit), the
bind-initiation (entering the winding), the thrust vs cut shape, the commit-depth style, the burst. Tempo emphasis
on initiative rides `channel_weight(tempo)` at `wrapper:118`. *(Damage-shaping actions — Power-Strike,
Armour-Breach — hook the wound stack and are deferred until the percussion/continuous decision (b) resolves.)*

**REACTION — triggered on the opponent's commit** *(the steal/counter node)*
The single-time counter: *selection* on `ability_factor('counter_select')` (`wrapper:159`), *success* on
`ability_bonus('counter_success')` (`wrapper:191`). The Indes/sen-no-sen Vor-steal scales with
`eff_cw(tactile/leverage/tempo)` via `init_steal_factor` (`systems:266–267`). Displace-and-step-inside vs a
committed thrust (leverage-gated, `wrapper:206`). Kuzushi-on-bind-win (`channel_weight(leverage)`, `wrapper:244`).

**SUPPORT — always-on competence** *(passive, every node)*
The channel competences themselves — measure / tempo / leverage / visual / tactile / precommit / balance — each
live via `eff_cw` at its site (measure→Vor-hold `systems:272`; tempo→grip-keep `systems:278`; tactile+leverage→bind
`systems:234–237`; visual→reads `wrapper:132–133`). Plus `anti_overcommit` (`wrapper:165`), Vor-decay resistance
(`init_hold`), grip/handling resistance. **This is where the passive dials belong** — and the slot *limit*
(one support) is exactly what makes them legitimate: a single chosen competence, not a stacking pile.

**FOOTWORK — measure control** *(the Closing / reopen node)*
Closing rate (`close_rate`), reopening the measure (`reopen_prob`, the longer weapon's game), the point-displace on
approach (`approach_displace`), measure-holding (`eff_cw(measure/balance)` at `foot_measure`, `systems:171–173`).
Distance and the measure are a whole slot, as movement is in FFT.

The existing `config.ABILITIES` schema — `dict(grade, lever, op∈{'+','*'}, value, desc)` consumed by
`ability_bonus`/`ability_factor`/`eff_cw` — is **already the modulator mechanism**. The new build is the layer
*above* it: categories, the unlock library, and the bounded loadout.

---

## §4 — Unlock model + loadout (the bound)

**The library grows; the loadout is bounded.**
- **Method tree** gates which methods you may train (FFT-style prerequisites — e.g., a pressure method opens a
  breach method).
- **Training** in a method permanently unlocks its techniques into your library. Cross-method techniques unlock by
  training *that* method — the earned cost that keeps borrowing real (the FFT secondary-skillset depth).
- **Loadout**, mirroring FFT's shape (counts are balance parameters, sim-tunable):
  **method-core action set** (fixed by method) **+ 1 slotted action** (incl. one cross-method) **+ 1 reaction
  + 1 support + 1 footwork.**

The slot limit is the load-bearing bound: the build space is now the set of *loadout configurations* over a method,
not C(library, k). Balance is validated over methods × a small number of slot choices — tractable — rather than
over an unbounded free mix.

---

## §5 — Worked loadouts (FFT-style; every slot a real lever)

**German Binder** *(method: Kunst des Fechtens)* — base channels tactile + leverage.
- Action: **Winden** (bind-initiate) + slotted **Zornhau** (wrath-cut: feint→deep commit).
- Reaction: **Indes-steal** (`init_steal_factor`, tactile/leverage in the bind).
- Support: **Fühlen** (tactile competence — feeling the bind, `eff_cw(tactile)`).
- Footwork: **Closing** (`close_rate`).
→ closes the measure, wins the winding, steals the Vor through the contact.

**Italian Duelist** *(method: Bolognese)* — base channels tempo + measure.
- Action: **Stop-hit** + slotted **Punta** (thrust).
- Reaction: **Single-time counter** (`counter_select` × `counter_success`).
- Support: **Tempo** (initiative competence, `channel_weight(tempo)`).
- Footwork: **Measure-hold** (`eff_cw(measure)` → `init_hold`).
→ holds distance, reads the commit, punishes it in tempo.

**Cross-trained hybrid** *(method: Bolognese, one German action trained)* — Italian base, **slots Winden** in the
cross-action slot (unlocked by training German).
→ a duelist who holds measure but can bind when forced close — the FFT secondary-skillset depth, paid for by the
cross-training. The Italian base profile persists; the German action is an accent, not a conversion.

---

## §6 — How the slot structure resolves the open tensions

| Reconciliation finding (the free-flat-atomic failure) | Resolved by the slot model |
|---|---|
| **Identity dilution** | The **method** sets an always-on base profile (channels + action set + node-preference); slotted borrows accent but never overwrite it. A German stays German. |
| **Combinatorial balance intractable** | The **slot limit** bounds the build to loadout-configurations; validate methods × slot choices, not C(library, k). |
| **Dial-heavy library** | Passive dials become the **one Support slot** — a single chosen competence, not a stacking pile. The limit is what legitimizes them. |
| **Dead conditional slots** | FFT's reaction/support/footwork are each at-least-weakly always relevant, and the **player chooses** the slot — they pick what fits their method. |
| **Legibility at scale** | **Four labelled slots** over a method read at a glance (every FFT player knows their loadout); not a 55-ability soup. |
| **Schema weight** | The modulator schema **already exists** (`config.ABILITIES` + the hook fns); only the slot/library/loadout layer is new. |
| **Physics coupling** | Damage-shaping **Action** techniques stay deferred until decision (b); the non-damage slots are independent of it. |

The key result: **the FFT/TO structure is the answer to the freedom-vs-identity dial.** It *is* mix-and-match —
you slot what you unlock — but bounded (limited slots) and identity-preserving (method base profile). The dial the
reconciliation left to you resolves cleanly toward "structured freedom" rather than either pole.

---

## §7 — Honesty / decisions

- **Mechanical, not creative.** The methods-as-jobs and the technique library are **mechanical playstyles**. Which
  factions or cultures train which method — the world-fiction — is **yours**; the mechanical methods (Binder,
  Duelist…) are not world cultures and do not assert any.
- **Historical-anchor discipline.** Historically-named techniques (Winden, Zornhau, the atajo, the stop-hit) stay
  anchored to documented schools; mechanical-fill techniques are graded `M`; no fabricated history. The 8 schools
  are the anchored set; the ~6 mechanical methods are explicit game-design archetypes.
- `[CONFIDENCE: high]` that the slot model is the right apparatus and that it resolves the four tensions (each
  mapped to a real lever). `[CONFIDENCE: medium]` on the specific loadout shape (FFT-mirrored is a reasonable start,
  not a unique one). `[GAP: unvalidated]` — the slot counts, the method tree, and per-category library sizes need
  the sim balance test (methods × slot-configs, win-rate flat within ±2–3 pp at N≈3000).
- **Decisions for you:** (a) the **loadout shape** — mirror FFT's 1-secondary/1-reaction/1-support/1-movement, or
  set different counts; (b) the **unlock/training economy** — how techniques are earned (per-method practice, a
  point currency, mastery gates); (c) the **method tree** — prerequisites and which methods gate which; (d) the
  **library size per category**; (e) defer damage-shaping Action values to physics decision (b); (f) the **sim
  validation plan**.

Provisional; canon engine unchanged. Continuation of the reconciliation — the slot model is the concrete form of
its "bounded, earned customization," and supersedes nothing.

*Offer: I can build an interactive FFT-style equip screen (a loadout mock-up — four slots, a method picker, a
technique library, live-resolving against the engine) as the visual companion, the way the tick-by-tick visual
followed the combat trace.*
