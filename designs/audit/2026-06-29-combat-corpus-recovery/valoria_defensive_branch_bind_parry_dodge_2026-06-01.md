# Valoria — Defensive Branch: Bind / Parry / Dodge
**Class-C proposal · 2026-06-01 (rev 2 — stat composition + degree ladders) · clean-slate combat rebuild**

> **Frame.** Ground-up rebuild. The inherited TTRPG action-economy is **discarded** (no Full Guard, Dodge-action,
> Feint-action, Tie Up, Rescue, Offence/Defence dice-split). The bout is a **state-graph procedure** (already
> canonical); this makes the *defensive* resolutions within it explicit. Build configured beforehand; turn-choice
> is only **approach + technique**; defense **emerges from the configured profile against the situation**.
> `[CONFIDENCE: high on structure — bottom-up from the canonical state graph + ratified σ/degree engine]`
> `[ASSUMPTION: Reflexes = (3·Agi+Att)/4, derived (Jordan-confirmed); weight = the knob]` · Jordan-vetoable · not committed.

## 1 · Canonical state graph (Jordan structural decision)

```
closing  →  engagement  →  disengaged / separation
   ↑__________________________________|   (loops for another round, or the bout ends)
```
- **closing** (approach) — reach-control governs; **variable duration**; a fighter can **refuse** engagement here.
- **engagement** — contact/exchange. **A bind is NOT guaranteed** — binding is one *sub-mode*; strikes, parries,
  binds resolve here; **variable duration** (a long bind extends it).
- **disengaged / separation** — fighters apart (no implied prior contact); loops to **closing** or ends.

**Outcome ontology per engagement:** **single hit** · **simultaneous / double hit** · **no hit**. **Bout length
is emergent** from wounds + stamina **+ time-in-state** (approach length, bind length) — same pair, different-length bouts.

## 2 · Inputs to defense

**Reading** `(Cog+Att)/2` — *anticipatory*, **universal**: feeds all three modes and decides whether you
**pre-position** (read the attack → set up the right defense) or react **cold** (relied on the execution inputs alone).
A feint attacks this channel; beat it and the defender commits to the wrong defense.

Each mode's **execution** then draws on a specific trio (Reading + two others):

| Mode | Reading (anticipate) | Reaction `(3·Agi+Att)/4` | Technique (History/sets) | Footwork (M7) | Strength |
|---|:-:|:-:|:-:|:-:|:-:|
| **Parry** | ✓ | ✓ | ✓ | | |
| **Dodge / Void** | ✓ | ✓ | | ✓ | |
| **Bind / Wind** | ✓ | | ✓ | | ✓ |

→ **Reaction** governs the two in-tempo modes (parry, dodge); **Technique** the two weapon-skill modes (parry,
wind); **Strength** only wind; **Footwork** only dodge. A Reflex fighter parries & dodges but can't wind; a
Strength fighter winds but can't parry/dodge; a reading-heavy fighter defends by every route.

## 3 · The three modes in the graph

| Mode | Graph slot | Requires | Beats | Loses to |
|---|---|---|---|---|
| **Dodge / Void** | **closing** (refuse engagement / force separation) | space + footwork | **heavy / deep-committed** attacks | **cornered**; fast tracking / short; multiple attackers |
| **Parry** | **engagement** resolution (displace the line) | a displacing weapon | **light / fast linear** attacks | **heavy/deep** blows; **bypassed by flails** |
| **Bind / Wind** | **engagement** sub-mode (blades stay in contact) | blade contact at the bind | attacks that **meet the blade** | attacks that **refuse the blade** (thrust-to-gap, void); **flails** |

## 4 · Degree-of-success ladders (each mode fails differently)

One degree engine (`net vs effective_ob → fail / partial / success / overwhelming`); **mode-specific consequence
mapping**. This is where the modes feel distinct.

**Dodge / Void** — *graded, and bleeds damage even on partial failure:*
| Degree | Outcome |
|---|---|
| Overwhelming | clean void **+ smooth counterattack** (attacker overcommitted, fully exposed) |
| Success | evaded clean → **separation / reset** |
| Partial | evaded but **ceded ground / tempo** (cornered further, position lost — M7) |
| Marginal (graze) | *"jumped back and still got nicked"* — **reduced (grazing) hit** |
| Fail | caught flat → **full hit** |

**Parry** — *deflects, but never guarantees immunity:*
| Degree | Outcome |
|---|---|
| Overwhelming | beat the line offline **+ riposte opening** |
| Success | clean deflection, **tempo neutral** |
| Partial | deflected the main line but **still took a graze** (heavy weapon overpowering structure, a second line, or follow-through) |
| Fail | **forced through → full hit** |

> A parry is never total immunity: circumstance (a heavier weapon breaking your structure, a follow-up line, bad
> footing) can leak a hit even on an otherwise-good parry.

**Bind / Wind** — *win = initiative, NOT lockout; the opponent keeps their weapon:*
| Degree | Outcome |
|---|---|
| Overwhelming | **dominate the bind** → control + riposte / winding-strike / disarm — *opponent may still abandon to grapple or strike with the off-end* |
| Success | **win the bind** — initiative is yours, *but the opponent retains a degraded option: disengage (cede tempo), pommel / half-sword / off-end strike, grapple, or counter-wind* |
| Partial | **bind locked / contested** — neither dominates, **extends engagement** (the long bind that varies bout length) |
| Fail | **lose the bind** → exposed → hit |

> **Universal principle (defense is never absolute):** no defensive success fully removes the opponent's agency
> or guarantees immunity. Winning the bind grants initiative, not a freeze — the loser still has their weapon and
> a (degraded) option. Defense shifts advantage and modulates damage; it never zeroes the opponent out.

## 5 · Tradition / ability / skill modulation

Martial tradition and equipped named sets **tilt the degree→consequence** for their signature mode — same roll,
better outcome band:
- **German / Bind Fighter** → shifts **wind** outcomes upward (more Overwhelming control/disarm).
- **Italian / Thrust Duelist · Counter-time** → shifts **parry** toward riposte.
- **Japanese-koryū / reading** → shifts **dodge** toward the smooth counterattack.
- **FMA / Continuous-flow** → chains a successful defense into the next strike (sustained tempo).
Abilities/skills layer on top (e.g. a footwork skill widens the dodge success band; a winding technique raises the
bind ceiling). Modulation moves the *band*, it does not bypass the contest.

## 6 · Resolution procedure

On an attack's **angle+style technique**, in the current state:
1. **Anticipation** — `Reading_def` vs the attack's deception. Win → pre-positioned (full available choice + setup
   bonus). Lose → cold (choice limited to Reaction/stance/grip-allowed; no setup bonus).
2. **Availability gate** — {Dodge, Parry, Bind} ∩ **(weapon/grip)** ∩ **(current state)**.
3. **Selection** — counter the attack's character; Reading-led if anticipated, best-available Reflex-led if cold.
4. **δσ contest** → degree → **mode-specific consequence** (§4), modulated by tradition (§5). May be single /
   simultaneous / no hit.
5. **State transition** — per the outcome; failure → D1 damage model. Wounds + stamina persist.

## 7 · The robustness payoff
Bind fighter (Str/German) controls the blade, helpless vs a voider who refuses the bind. Parry-tempo fighter
(Reflex/Italian) cleans light lines, forced through by the heavy commit. Void fighter (Reading+Reflex/koryū) slips
the deep commit for the counter, dies cornered. Reflex brawler reacts to all, eats every feint. **Same engine,
different configured profiles → unique fights.**

## 8 · Gates (weapon/grip → modes) — seed
| Weapon / grip | Bind | Parry | Dodge |
|---|:-:|:-:|:-:|
| Longsword (versatile) | ✓ | ✓ | ✓ |
| Rapier + dagger | weak | ✓✓ | ✓ |
| War-hammer / poleaxe (half-sword) | ✓✓ | ✓ | weak |
| Flail | ✓ | — *(bypasses parries)* | ✓ |
| Spear / staff | ✓ | ✓ | ✓ (reach voids) |
| Paired short (FMA) | weak | ✓✓ | ✓ |

## 9 · NERS / open items
- **Necessary/Elegant** — three modes + one universal sense-channel + one shared degree engine (mode-specific
  outcome tables, not new machinery). Guard against over-splitting.
- **Sim-fidelity gaps for the rebuild:** the session harness used fixed sub-actions (no variable time-in-state),
  forced alternating single strikes (no simultaneous/no-hit), and treated "breaking" as a reset. The corrected
  graph + degree ladders + simultaneity all need building before calibration.
- **Not calibrated** — δσ magnitudes, Reflexes weight, degree-band cutoffs, tradition shift sizes, and gate
  strengths are **seeds**; tune against the state-graph harness once it models the above.
- **Top-down grounding** — *Winden* / *Versetzen* / void (*Abnehmen*, *tai-sabaki*, Destreza); flail-bypasses-parry
  historical; simultaneous hit = the feared *Doppelhau*; reading-vs-reflex = anticipation vs raw speed.

## Discarded (recorded)
Full Guard · Dodge-action · Feint-action · Tie Up · Rescue · O/D dice-split · the `in_bind`/`breaking` node names.
Intents survive as emergent outputs within the canonical state graph.
