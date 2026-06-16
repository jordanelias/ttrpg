# Comprehensive proposal — ability library + traditions / classes / jobs mapped to the combat state graph

**2026-06-13 · status: PROPOSED, Jordan-vetoable · the build-out of the abilities-primary direction**

Goal: many traditions / classes / jobs, built from abilities / modifiers / techniques that hook **most or all**
of the state-graph components, composable into unique builds.

`[SELF-AUTHORED — bias risk]` Large content proposal. Read the two lines in §0 before the content — they bound
what is mine to propose.
`[READ: combat_engine_v1/{wrapper,systems,core,tradition}.py — the components hooked + the ability schema]`

---

## §0 — Two lines this proposal respects

1. **Mechanical vs corpus/creative.** I propose the *mechanical* layer — the ability schema, the hooks into
   state-graph components, the build/balance system, and **mechanical archetypes** (playstyle classes defined
   by which components they command). The **8 historical schools** and their identities are the corpus's. The
   **world, cultures, and lore** are yours: the classes below are mechanical playstyles, **not** world
   factions — rename, reskin, or attach them to Valoria's cultures as you see fit.
2. **The historical-anchor discipline (from `tradition.py`).** The engine refuses to invent historical
   techniques for under-documented traditions ("priority-gap traditions get NO ability until an S1/S2 anchor
   exists"). I honour it: historically-named abilities (Winden, mezzo tempo, atajo, sen-no-sen, true-times)
   stay attached to their documented schools and carry their source grade; everything else is graded **`M`
   (mechanical / game-design archetype, no historical claim)**. Under-documented schools (Chinese, Filipino)
   are filled only with `M` abilities, flagged — not fabricated history.

So the "many" comes from **mechanical archetypes + mix-and-match**, not from inventing pseudo-historical
schools. Authoring more *historical* traditions is your call (your world, your sources).

---

## §1 — Ability schema (extended)

The current schema is `dict(tradition, grade, lever, op, value, desc)` with `op ∈ {+, *}` and
`ability_bonus`/`ability_factor` aggregating per lever. The prior exploration established that conditionality
and cost are needed for vacuum-balance. Proposed extension (additive, invariant-safe — defaults reproduce
today's behaviour):

```
ability = dict(
  name, grade,                 # 'M' (mechanical) | 'S1'..'S3' (historical reliability tier)
  hook,                        # the state-graph component it modulates (a lever / σ-site / transition)
  op, value,                   # '+' bonus | '*' factor | 'gate' (route a transition)
  trigger = 'always',          # NEW: the node/state it fires in (out_of_contact|closing|closed|bind|reopen|counter|burst|on_hit|holding_vor|deep_commit|vs_armour|...)
  cost    = {'slot':1},        # NEW: slot + optional per-use {stamina|exposure|poise|tempo}
  prereq  = None,              # NEW: affinity/skill threshold gating equip
)
```

`trigger` makes value **conditional** (an in-bind ability is inert in the open → context-bounded power, C1).
`cost` makes power **paid for** (slots + per-use resource → self-balancing). `prereq` gates equip on the
affinity budget. Channel-lever abilities go live once the ~19 `eff_cw` sites are wired (the pending pass).

---

## §2 — State-graph coverage map (the target)

Every component an ability can hook, by phase (from the stat/weapon breakdown). The library in §3 covers each.

| Phase | Components (hooks) |
|---|---|
| **Approach / measure** | `reach_sigma` · `approach_displace` · `close_rate` · `reopen_prob` · `weapon_tempo`/`close_tempo` |
| **Reading / feint** | `reading` · read-contest (`read_a`/`read_d`) · `legibility` · `feint_eval` |
| **Defence** | `mode_sigma` parry/dodge/wind · `GATE` caps · `handling_penalty` · guard terms (`blade_guard`/`hand_guard`) |
| **Bind** | `bind_sigma` (leverage/tactile/catch/Str) · `init_steal_factor`(bind) · bind-loop entry/exit |
| **Initiative (Vor)** | `initiative_sigma` · `init_steal_factor`(open) · `init_hold_decay` · `init_overcommit_loss` |
| **Commit / counter** | `overcommit_exposure`/`anti_overcommit` · single-time counter · two-time riposte · indes steal |
| **Structure / economy** | `poise_factor` (kuzushi) · `balance_eff` (footwork) · `stamina_max`/`act_cost` · concentration/`mental_fat` |
| **Damage / finish** | `coupling`/`HEFT`/`percussion`/`gap` · `armor_defeat_sigma` · the decisive blow (degree) |
| **Stance / form** | `disp_lean` (commit) · `grip` (choke/lunge) · half-sword form switch |

---

## §3 — The ability library (by component; grade M unless an anchor is named)

Compact: **Ability · Hook · Effect (op) · Trigger · Cost**. ~55 modulators/techniques; every §2 component covered.

### Approach / measure
| Ability | Hook | Effect | Trigger | Cost |
|---|---|---|---|---|
| Measure Hold | `init_hold_decay`,`reach_sigma` | `*`measure↑ (hold distance) | out_of_contact | slot1 *(anchor: atajo/misura S2/S3)* |
| Void Step | `close_rate`(opp)↓ | `+`evade-back, denies close | closing | slot1 + stamina |
| Measure Bait | `legibility` | invite a committed entry → counter | out_of_contact | slot1 |
| Explosive Entry | `close_rate`↑ | `*`rush the close | closing | stamina(high) |
| Beat-Aside | `approach_displace`↑ | `*`set aside a point, close safely | closing vs point | slot1 + leverage prereq |
| Sticky Close | `reopen_prob`(opp)↓ | keep it closed | closed | slot1 |

### Tempo / cadence
| Quickening | `weapon_tempo`↑ | `*`faster cadence | always | slot1 |
|---|---|---|---|---|
| Broken Rhythm | `legibility`(self)↓ | harder to read your cadence | aggressor | slot1 |
| Choke Agility | `close_tempo` | offset the pole close-penalty | closed+pole | slot1 |
| Lunge Extension | reach + `overcommit_exposure` | reach now, pay exposure | attack | exposure |

### Reading / feint
| Keen Read | `reading`↑ (visual) | `*`out-anticipate | always | slot1 |
|---|---|---|---|---|
| Feint Mastery | `feint_eval` | `*`feint success & debuff↑ | aggressor | stamina |
| Invitation | bait → counter | present a false line, punish the commit | defender | slot1 *(It./Jp. flavour)* |
| Read-the-Feint | `feint_eval`(def_read)↑ | not fooled; small counter-edge | defender | slot1 + precommit prereq |

### Defence (parry / dodge / wind) + handling
| Parry Master | `mode_sigma`parry + GATE↑ | `+`reliable cross-parry | defending | slot1 |
|---|---|---|---|---|
| Void Master | `mode_sigma`dodge↑ | `+`displace off-line | defending | slot1 |
| Winding Master | `mode_sigma`wind↑ | `+`win the bind-defence | defending/bind | slot1 *(Winden S1/S2)* |
| Mode Flux | GATE off-mode penalty↓ | use a non-native mode cleanly | defending | slot2 |
| Strong Grip | `handling_penalty`↓ | wield a demanding weapon | always | slot1 + Str prereq |
| Guard Displacement | opp `blade/hand_guard`↓ | beat the guard aside | bind/parry | slot1 |

### Bind / winding
| Bind Dominance | `bind_sigma`↑ | `*`win the winding | bind | slot1 *(Winden S1/S2 / M)* |
|---|---|---|---|---|
| Stärke-Schwäche | `leverage` | feel strong/weak, redirect | bind | slot1 *(S1/S2)* |
| Blade-Catch | `bind_sigma`catch↑ | quillons/rings control the blade | bind | slot1 + blade_guard |
| Wrench / Disarm | bind-win → disarm/break | end the bind decisively | bind-win | slot2 + exposure |
| Bind-Steal (Indes) | `init_steal_factor`(bind)↑ | steal the Vor in the bind | bind + read-win | slot1 *(Indes S1/S2)* |

### Initiative / Vor
| Seize (Vorschlag) | `seize`↑ | `+`take the Vor first | first exchange | slot1 *(S1/S2)* |
|---|---|---|---|---|
| Sen-no-sen | `seize` at opp commit | `+`pre-emptive seize | opp commits | slot1 *(S2 Jp.)* |
| Hold the Vor | `init_hold_decay`↓ | `*`keep the Vor longer | holding_vor | slot1 *(Destreza S2/S3)* |
| True Times | `init_overcommit_loss`↓ | `+`lose less Vor on commit | deep_commit | slot1 *(S2 Eng.)* |
| Relentless | `initiative_sigma`↑ | `+`press the Vor edge | holding_vor | stamina |
| Tempo-Steal | `init_steal_factor`(open)↑ | `*`steal in the open | open + read-win | slot1 *(mezzo tempo S2)* |

### Commit / counter
| Committed-but-Safe | `anti_overcommit`↑ | `+`commit deep, exposed less | deep_commit | slot1 *(true times S2)* |
|---|---|---|---|---|
| Bait-the-Overcommit | punish opp exposure | counter their deep commit | opp deep_commit | slot1 |
| Stop-Hit | counter_success/select↑ | `+`/`*`in-tempo counter at measure | opp commits | slot1 *(S2 It.)* |
| Counter-Time | counter on opp tempo | beat the feint/second-intention | opp feint/commit | slot2 *(S2 It./Eng.)* |
| Riposte Master | two-time riposte↑ | `+`strike after a clean defence | post-defence | slot1 |
| Indes Seize | indes steal scaling↑ | `*`fuller flip on a deep-commit read | read-win vs deep | slot1 *(S1/S2)* |

### Structure / economy
| Kuzushi | opp `poise_factor`↓ | break their structure on bind/hit | bind-win/on_hit | slot1 *(Jp./judo flavour)* |
|---|---|---|---|---|
| Rooted Stance | `poise` loss↓ | hard to unbalance | always | slot1 + tempo cost |
| Structure Recovery | `poise` recovery↑ | re-base faster (Focus) | between exchanges | slot1 |
| Conditioning | `stamina_max`↑ | bigger reserve | passive | slot1 |
| Economy | `act_cost`↓ | cheaper acts | always | slot1 |
| Mental Fortitude | `mental_fat` resist↑ | read/defend under fatigue | under_fatigue | slot1 |
| Footwork Master | `balance_eff`↑ | `+`compás/measure footwork | always | slot1 *(Sp. flavour)* |
| Mobile Stance | `balance_eff`+tempo | mobility over root | open | poise cost |

### Damage / finish / armour
| Power Strike | `coupling`/HEFT↑ | `*`heavier blow | on_hit | exposure |
|---|---|---|---|---|
| Precision Thrust | `gap`↑ | `*`thrust accuracy | thrust | slot1 |
| Armour-Breach | `armor_defeat`(blunt)+`percussion` | defeat plate | vs_armour | slot1 |
| Half-Sword Mastery | half-sword form + `gap`/leverage | murder-stroke vs plate | closed + vs_armour | slot1 *(Harnischfechten S1/S2)* |
| Öffnen (the opening) | degree↑ on read-win | strike the exposed line | read-win | slot1 |
| Gap-Finder | `armor_defeat`(point/gap)↑ | thread the gaps | vs_armour | slot1 |

### Stance / form
| Controlled Aggression | `disp_lean` | commit deep, stay disciplined | aggressor | slot1 |
|---|---|---|---|---|
| Baited Caution | `disp_lean` | draw the opponent out | defender | slot1 |
| Grip-Shift Mastery | `grip` | free choke/lunge/normal, no tempo loss | always | slot1 |
| Form-Switch | half-sword switch | switch form fluidly by range/armour | range/armour change | slot1 |

---

## §4 — The 8 historical schools (anchored bundles; the corpus's identities)

Each = a preferred node + an ability bundle (anchored where documented). Weakness = the matchup that exploits it.

| School | Node | Signature bundle | Weakness (exploited by) |
|---|---|---|---|
| **German** (Bind Fighter) | bind | Bind Dominance · Stärke-Schwäche · Bind-Steal · Seize · Half-Sword | kept at measure (Duelist/Spanish) |
| **Italian** (Thrust Duelist) | measure/counter | Measure Hold · Stop-Hit · Counter-Time · Invitation | dragged into the bind (German/Closer) |
| **Spanish** (Destreza) | measure-hold | Measure Hold (atajo) · Hold the Vor · Footwork Master · Void Step | the close/pressure (Closer/Pressure) |
| **Japanese** (koryū) | pre-commit counter | Sen-no-sen · Invitation · Kuzushi · Read-the-Feint | sustained attrition (Pressure) |
| **English** (Silver) | clean counter | True Times · Committed-but-Safe · Counter-Time · Stop-Hit | the grapple/bind (Closer) |
| **Chinese** (Burst) ⚑ | burst from reach | Explosive Entry · Relentless · Precision Thrust *(all `M`)* | out-fought in the open (Duelist) |
| **Filipino** (Continuous-flow) ⚑ | flow | Broken Rhythm · Mobile Stance · Riposte Master *(all `M`)* | the bind/root (Binder/Stoic) |
| **None** | — | (no abilities — neutral baseline) | everything; the floor |

⚑ Chinese/Filipino bundles are **mechanical fill** (grade `M`) pending S1/S2 anchors — not historical claims.

---

## §5 — Classes / jobs (mechanical archetypes; the "many")

Playstyle bundles over the §3 library, each owning a node + a coverage. Mechanical (rename/reskin freely). The
explicit weaknesses form a balanced web (no globally-best — §7).

| Class | Node | Signature bundle | Strong at | Weak to |
|---|---|---|---|---|
| **Binder** | bind | Bind Dominance · Blade-Catch · Wrench · Kuzushi | the winding war | kept at measure |
| **Duelist** | measure/counter | Measure Hold · Stop-Hit · Precision Thrust · Void Step | open point-fighting | the bind / grapple |
| **Skirmisher** | reopen/mobility | Void Step · Mobile Stance · Quickening · Sticky-Close(deny) | distance & recovery | pinned / attrition |
| **Breacher** | armour-defeat | Armour-Breach · Power Strike · Half-Sword · Gap-Finder | vs armour | fast unarmoured duelists |
| **Counter-fighter** | riposte/indes | Bait-the-Overcommit · Riposte Master · True Times · Invitation | punishing aggression | a patient non-committer |
| **Pressure-fighter** | Vor-hold/burst | Relentless · Explosive Entry · Conditioning · Sticky Close | relentless tempo | a clean counter-fighter |
| **Measure-master** | measure-hold | Measure Hold · Hold the Vor · Footwork Master · Void Step | denying the close | breacher/closer who eats the hit |
| **Closer / Grappler** | close/bind | Explosive Entry · Beat-Aside · Bind Dominance · Half-Sword · Kuzushi | collapsing measure | a measure-master with footwork |
| **Feint-fighter** | read/feint | Feint Mastery · Broken Rhythm · Invitation · Öffnen | opening the guard | a keen reader (Read-the-Feint) |
| **Stoic / Rock** | defence/structure | Rooted Stance · Parry Master · Structure Recovery · Conditioning · Mental Fortitude | defensive attrition | breacher (ignores defence) / feint-fighter |
| **Tempo-thief** | initiative | Tempo-Steal · Sen-no-sen · Indes Seize · Quickening | owning the Vor | a disposition-disciplined fighter |
| **Power-fighter** | damage | Power Strike · Öffnen · Controlled Aggression · Strong Grip | ending exchanges | a skirmisher who won't trade |

8 schools + 12 classes = 20 archetypes, all bundles over one shared library; mix-and-match (§6) makes the set
effectively open.

---

## §6 — Mix-and-match builds

A **build = an affinity point-buy + an ability loadout**:
- **Affinities** — a fixed point-buy over the seven channels (equal budget for all → balanced; the §1
  exploration's fix for the vacuum-imbalance). Affinities (a) gate ability `prereq`s and (b) give modest
  in-node competence.
- **Ability slots** — a fixed slot budget; abilities cost slots (and some cost per-use stamina/exposure/poise).
  You **cannot equip everything** — that is the core balance lever.
- **Presets** — schools and classes are starting loadouts; the player **reallocates affinities and swaps
  abilities** for a unique build.
- **Cross-school hybrids are legal** (trained in two schools) and **bounded** by slots + cost + the familiarity
  web (a hybrid reads as both, its own trade-off). Examples:
  - *Binder + True Times* — a bind-fighter who buys the counter-fighter's commitment discipline to cover the
    "kept-at-measure" weakness (costs slots otherwise spent on bind depth).
  - *Duelist + Half-Sword* — a measure-duelist who can answer armour, paying slots that weaken the open game.
  - *Skirmisher + Stop-Hit* — hit-and-run that punishes the chase.

Power is bounded by: slot count, per-use cost, **conditional value** (an in-node ability is dead out of node →
raw power self-limits and context-flips, C1), opportunity cost, and the affinity budget.

---

## §7 — Balance, loop-safety, over-engineering, validation

- **Vacuum-balance (no globally-best — ratified C1).** Enforced by: the equal affinity budget; the slot/cost
  budget; **conditional value** (context-bounded power); and the **cyclic** matchup web — every archetype's §4/§5
  weakness is another's strength (bind ⟶ counter ⟶ measure-hold ⟶ bind; pressure ⟶ counter; breacher ⟶ stoic ⟶
  feint-fighter ⟶ …). Context (weapon, armour, duel-vs-field) flips the *conditional* advantage; the
  *unconditional* mean must be flat.
- **Loop-safety.** The feedback structures abilities touch already carry the engine's dampers/caps: the Vor
  economy (`init` decay + `INIT_CAP`), kuzushi (`poise` floor + recovery), pressure (stamina drain + `BURST_MAX`).
  Abilities **modulate within** these bounds; an ability that removes a damper or cap is rejected.
- **Over-engineering guard (NERS-E).** The library must *earn* its size: every ability hooks a real §2
  component and adds a **distinct** choice. Any ability that only re-skins another, or hooks nothing the player
  can perceive/exploit, is cut. Legibility is a requirement — the player must see the technique act.
- **Validation (the gate).** None of this is balance-validated. The test: extend the harness to
  archetype/build matchups; measure each build's **unconditional win-rate** flat within the parity noise floor
  (±2–3 pp at N≈3000); tune affinity budget, slot count, cost schedule, and the cyclic relation until flat.

---

## §8 — Honesty / the lines / decisions

- `[CONFIDENCE: high]` on the **hooks** (every ability targets a real, named state-graph component) and on the
  **coverage** (§2 components all hooked). `[CONFIDENCE: medium]` on the **archetype roster** (a reasonable,
  game-design-anchored set, not a unique one). `[GAP: unvalidated]` — no win-rates measured; sizing/tuning is
  the sim step.
- **The lines.** The ability *hooks* and the *mechanical archetypes* are mine to propose (mechanical tier,
  bottom-up on the engine + top-down on game-design/martial-style). The **historical schools** and their
  anchored techniques are the corpus's; under-documented schools are filled only with `M` abilities, flagged —
  **no fabricated history**. The **world, cultures, and lore** are yours: these classes are mechanical
  playstyles to rename/reskin/attach as you decide.
- **Decisions for Jordan:**
  - (a) Adopt the schema extension (`trigger`/`cost`/`prereq`)? It is required for conditional, costable,
    vacuum-balanced abilities.
  - (b) Slot count + affinity budget + cost schedule (the balance dials — sim-tuned).
  - (c) Which classes to adopt / rename / merge, and whether to bind them to Valoria's cultures (your world).
  - (d) The under-documented-school policy: keep `M`-filled (mechanical) or author historical anchors (your
    sources).
  - (e) The cyclic matchup relation + per-use costs (carried from the gate/representation work; sim-tuned).
  - (f) Which abilities to wire first — the `eff_cw` channel-lever pass unlocks the channel-hooked abilities;
    the live levers (`seize`/`counter_*`/`anti_overcommit`) already work.

Provisional; the canon engine is unchanged. Pairs with the tradition-gate reconciliation (which-fight) and the
representation exploration (abilities-primary) — this is the content layer over both.
