# Combat Stress Test — Chunk 2/7
## Variants and opportunities from acclaimed combat systems

**Method:** survey 30+ shipped systems, map each to canonical Valoria mechanics, score adoption fit (Lift / Adapt / Inspiration / Reject) per architecture (A: map+move · B: DD slot · C: duel).
**Constraint:** any adoption must preserve the canonical resolution math — Combat Pool, weapon TN matrix, damage = net hits + STR + weapon mod − DR, Wound Interval, Stamina formula. Variants can change presentation, time-shape, action economy, and UI; they cannot fork the underlying math.

---

## 1. Sid Meier's Pirates! duel — deep dive (the asked example)

**Mechanism:** 1v1 real-time fencing on a 2D side-on plane. Three vertical guards (high / middle / low). Three attacks per guard (slash / thrust / parry / feint depending on edition). Footwork along a single ground axis. Pushing the opponent off the edge of the deck (or into the captain's cabin's far wall) ends the fight. Reading opponent's guard change is the core loop.

**Maps to Valoria canon:**

| Pirates! element | Valoria canonical equivalent |
|---|---|
| Three guards (high/mid/low) | Pool split commit — Offence-heavy / Balanced / Defence-heavy. Stance IS the visualization of the canonical pool allocation. |
| Three attacks per guard | Action selection (Strike / Feint / Disarm) — different stance enables different actions per round |
| Footwork (closing/retreating along ground axis) | Establish Distance + Reach Rules (§5) — closing into Melee range from Ranged distance |
| Edge push (off deck / wall) | Stunt (§4) — environmental finish; canonical N=5 max; explicitly authored per duel arena |
| Cinematic location backgrounds (deck / captain's cabin / town square) | Authored duel arena → Stunt opportunity tag + audience composition (witnesses for §13.2 Reputation Cascade) |
| Captain rank / treasure stake | Wager system — net-new canon content but a clean fit for Valoria's Conviction/Renown layer |
| Tiredness over prolonged combat | Stamina (§7) — Pirates! tracks it implicitly via animation; Valoria can surface it directly |

**Adoption fit:** **Lift wholesale into C.** Pirates! is the highest-fit reference for Valoria's duel architecture because:
- It already maps Valoria's pool-split mechanic to a stance UI without needing to invent presentation.
- Its three-guard structure naturally surfaces Feint as the read-and-counter loop (commit a guard → opponent reads → you can feint your guard change).
- Edge-push = Stunt is a direct translation. Valoria-flavor: cliff edge in Eisengrund, fountain in Himmelstift cathedral square, throne dais in royal court.
- Cinematic backgrounds satisfy "duels are public" — the audience composition for Reputation Cascade is built into the location selector.

**Rejected aspects:** Pirates!' arcade-pace (sub-second reactions) is too fast for Valoria's deeper canonical math (Combat Pool calc, Wound Interval, weapon TN matrix). C should slow Pirates!' tempo to a Sekiro-like beat-by-beat exchange where each "stance change" is a Valoria round (6–10s).

---

## 2. Other duel / 1v1 systems → C architecture

| System | Mechanism | Valoria mapping | Fit | Recommendation |
|---|---|---|---|---|
| **Sekiro** (FromSoftware) | Deflect window, posture meter (break = killable), mikiri counter on thrusts, resurrection economy | Posture = Stamina; deflect = Defence dice spike; mikiri = Feint counter on telegraphed thrust | C only | **Lift the posture-as-resource pattern** — Stamina becomes the visible duel metric, fights end by Stamina exhaustion *or* HP zero, mirroring §7 Out of Breath as a fight-ender |
| **Bushido Blade** (Square 1995) | One-hit kill, four stances per weapon, location-specific damage (limb crippling), no HP bar | Locations + crippling map to Wound Interval but with body-part state | C only | **Inspiration only** — Valoria's Wound Interval is statistical not locational; partial-limb adaptation is high cost for niche payoff |
| **For Honor** (Ubisoft) | Three-direction guard (top/left/right), feints commit on animation, Revenge meter on outnumbered | Three-guard ≈ pool split; outnumbered Revenge ≈ Fibonacci defender bonus *(net-new — canonical Fibonacci is attacker-side only)* | C primary, B inspiration | **Adapt** the directional guard → high/mid/low for C stance UI. **Reject** Revenge — would invert Fibonacci. |
| **Nidhogg** (Messhof) | Fencing with three height bands, instant-kill, divefly tackle, momentum push | Height bands ≈ stance + reach interaction | C inspiration | **Inspiration** — height-band pacing is too arcade for canonical Wound math |
| **Mount & Blade duel** | 4-direction attack/block, weapon momentum, footwork | Direction = stance; momentum tracks Stamina-like resource | C primary | **Adapt** — duel approach phase + 4-direction guard with one-tier-up animation read |
| **Punch-Out!!** (Nintendo) | Pattern recognition, dodge windows, star-punch on perfect tells | Tell-window = canonical "lower-init declares first" inverted → C uses opponent's declared stance as the tell | C inspiration | **Adapt** the visible-tell loop — make canonical init transfer into a visible "advantage" the player can read |
| **Absolver** (Sloclap) | Combat deck (4 stances × 4 attack-direction slots = 16 customizable abilities), stance flow | Customizable deck ≈ skill loadout per Conviction/History | C extension | **Inspiration** — Conviction-themed dueling decks are a strong Valoria-flavor extension but net-new content |
| **Way of the Samurai 4** (Acquire) | Multi-stance per weapon class, parry-counter, sheathed-draw stance | Sheathed-draw = Initiative gambit | C extension | **Inspiration only** — high implementation cost |
| **The Witcher 1** (CDPR) | Three styles (group/strong/fast), rhythmic click-on-flash | Three styles ≈ pool split visualization | C primary | **Adapt** — rhythmic flash window is a clean way to time Defence allocation in C without breaking canonical phase order |
| **Pyre** (Supergiant) "rites" | Mystical 3v3 sport-as-duel, pyre-extinguishing, banishment | Practitioner Thread duel framing | C extension | **Inspiration** — Practitioner-vs-Practitioner Thread duels could borrow Pyre's ritual framing |

---

## 3. Group / tactics / formation systems → A or B architecture

| System | Mechanism | Valoria mapping | Fit | Recommendation |
|---|---|---|---|---|
| **XCOM 2** (Firaxis) | 2-action economy, cover (full/half/none), overwatch, percentage-shot UI | 2-action ≈ Offence/Defence allocation but discretized; overwatch = canonical Reactive trigger | A primary | **Lift the cover system directly** — Soft/Hard cover from §5 maps cleanly to XCOM's full/half. Reject 2-action economy — Valoria's pool split is more granular and more legible. |
| **Into the Breach** (Subset) | Perfect-information turn (player sees all enemy moves before committing), tile-puzzle resolution | Reverses canonical "blind simultaneous declare" — opposite philosophy | A inspiration | **Reject for general combat** — kills Feint mind-games. **Adapt for tutorial / accessibility mode** where enemy intent is shown |
| **Final Fantasy Tactics** | Height affects accuracy/damage, facing matters, CT (charge time) per action | Facing/height — net-new spatial axes | A extension | **Inspiration** — height could fold into Stunt N rather than be a top-level axis |
| **Battle Brothers** (Overhype) | Hex grid + morale + injury locations + multi-turn skills + fatigue | Morale = canonical mass-combat thing; injury locations = body-part Wounds (already canon-adjacent via §7 incapacitation stages) | A extension | **Adapt morale system into B's rank-collapse rules** — when front rank breaks, rear-rank Composure check |
| **Wartales** (Shiro) | Initiative bar with movable order, opportunity attacks, cohesion (party slots active simultaneously) | Cohesion ≈ Fibonacci structural inverse — defender side gets bonus if linked | A inspiration | **Reject cohesion** — would conflict with attacker-Fibonacci. **Lift movable initiative bar UI** — canonical "winner holds, loser declares first" displayed as a tempo bar |
| **Pillars of Eternity 2** (Obsidian) | RTwP, recovery time per action, engagement (disengagement attacks) | Recovery time = canonical round 6–10s but continuous; engagement = Tie Up | A primary | **Adapt** — RTwP is a viable A time-model variant; engagement = canonical Tie Up §4 already handles |
| **BG3** (Larian) | Strict D&D 5e turn-based on grid, action+bonus+reaction, advantage/disadvantage | Strict turn order; advantage ≈ Fibonacci dice bonus | A primary | **Reject grid** — Valoria's reach matrix is continuous-friendly. **Adapt advantage/disadvantage** — already covered by Fibonacci and wound penalty |
| **Mutant Year Zero** (Bearded Ladies) | Pre-combat sneaking → silent eliminations → combat triggered when detected | Fieldwork → Combat Exposure transition (§11.5) — *direct match* | A primary | **Lift** — silent stealth eliminations resolve Exposure as 0; detection escalates by canonical quiet/conspicuous/public ladder |
| **Wasteland 3** (inXile) | Grid + call-shots + percentage hits + companion conflicts | Call-shots ≈ Wound location | A inspiration | **Inspiration only** — call-shots add depth but canonical Wound system is non-locational |
| **Persona 5 Royal** (Atlus) | Weakness exploit → 1-more action; All-Out Attack on full down | Weakness = mismatched weapon-class vs armour-tier (already canon §5 damage table); All-Out = canonical Multi-Engagement | B primary | **Inspiration** — the visible "weakness" callout when player exploits canonical weapon-vs-armour mismatch is a clean legibility win |
| **Octopath Traveler** (Square Enix) | Break (exploit weakness types) + Boost (save BP for big actions) | Boost ≈ saving Stamina for Heavy attack | B inspiration | **Adapt** — Stamina-banking for big attacks is canon-adjacent already (Heavy attack costs 8 Stamina, §7) |
| **Honkai: Star Rail / Sea of Stars** | Timed-hit JRPG inputs that increase damage on perfect timing | Timing window = active player skill layer atop dice | B/C extension | **Adapt for C** — timed inputs reward duel-like attention without forking math; cap damage bonus to single +1 net hit to preserve canonical scale |
| **Grandia** (Game Arts, PS1) | IP gauge + interrupt window when enemy reaches "act" notch | **Direct match for canonical phase resolution** — declare-then-resolve becomes a visible IP timeline; interrupt = Feint consuming opponent's pool next round | A and B both | **Lift for A and B** — Grandia's IP timeline is the cleanest visualization of Valoria's "blind declare → priority resolution" loop. Strong recommendation. |
| **Valkyria Chronicles BLiTZ** (Sega) | Turn-based command layer + real-time third-person aiming during unit's action | Hybrid time-shape | A extension | **Reject** — third-person shooter mechanics are off-genre |
| **Wakfu / Dofus** (Ankama) | Grid + AP (Action Points) and MP (Movement Points) separated | Discretizes pool further; AP/MP separation = Combat Pool / Stamina | A inspiration | **Inspiration** — Stamina-as-MP is canon-adjacent; explicit AP/MP separation would over-discretize Valoria's continuous pool |
| **Wildermyth** (Worldwalker) | Tactical combat + persistent narrative consequence (lost limb → permanent) | Wound permanence — canon currently says "Wounds clear at end of session" (§4 PP-284/ED-177) | A inspiration | **Tension flag** — Wildermyth's permanent-consequence model is more dramatic but conflicts with canonical recovery rule. Surface for Jordan's review. |
| **Triangle Strategy** (Square Enix) | Conviction-axis decisions interrupt tactical battles with branching | Conviction Scar / Conviction Track integration | A extension | **Inspiration** — battle-pause Conviction prompts are a canonical-adjacent UX pattern for §13.3 Death Cascade moments |

---

## 4. Time-shape variants (cross-cutting)

| System | Time model | Valoria fit | Notes |
|---|---|---|---|
| **Strict turn-based (BG3, XCOM 2)** | Each actor acts in initiative order, full info | Compatible with A and B | Highest tactical legibility; loses simultaneity flavor of canonical §2 |
| **Phase-locked simultaneous (Frozen Synapse, Combat Mission)** | Both sides plan, then resolve simultaneously | **Direct match for canonical §2** | Frozen Synapse is the closest existing time-model to canonical Valoria. Worth deep study for A. |
| **RTwP (Pillars 2, BG2, Pathfinder: WotR)** | Real-time with pause-anytime, queue actions | Compatible with A | Recovery times replace round structure; phases become approximate |
| **Active-time (Grandia, Final Fantasy IV/IX, Sea of Stars)** | Continuous timer, act when ready | Compatible with all three | Grandia's IP gauge is the strongest variant for Valoria — see §3 |
| **Reactive real-time (Sekiro, Dark Souls)** | Pure continuous, deflect/dodge windows | C only | High canonical math friction unless heavily simplified |
| **Perfect-information turn (Into the Breach)** | See all enemy moves before committing | Compatible with A and B | Kills canonical Feint mind-games; reject for general combat |

---

## 5. Action / resource economy variants

| System | Economy | Valoria fit |
|---|---|---|
| **2-action (XCOM 2)** | Each turn: 2 actions, certain abilities cost 1 or 2 | Reject — Valoria's pool split is more granular |
| **AP/MP split (Wakfu/Dofus)** | Action Points + Movement Points separately | Inspiration — Stamina already does Movement-Point work |
| **BP boost (Octopath)** | Save BP, spend N for ×N effect | Adapt — Stamina-banking for Heavy attack |
| **Stance flow (Absolver, Way of Samurai)** | Each attack ends in a stance that gates next attack | Adapt for C — duel stance progression |
| **Card hand (Slay the Spire, Wildfrost)** | Draw → play → discard, deck construction | Reject for scene combat — Valoria's strategic-layer Card Hand is a separate scope (BG layer) |
| **Posture / Stance breaking (Sekiro)** | Stamina-like meter that ends fight on break | **Lift for C** — see §2 |
| **Cohesion / link (Wartales, Persona All-Out)** | Adjacent allies link for bonus | Inspiration — but Valoria's Fibonacci is the canonical group bonus and it's attacker-side; defender-side cohesion would invert |

---

## 6. UI / surface variants worth pulling

| Pattern | Source | Valoria use |
|---|---|---|
| **Visible initiative bar / tempo meter** | Wartales, Grandia, Sea of Stars | Surface canonical "winner holds initiative" as tempo indicator across A/B/C |
| **Percentage-shot UI** | XCOM 2 | Possibly for ranged in A — show TN-vs-pool probability inline |
| **Tell animations on enemy commit** | Punch-Out!!, Sekiro, Soulsborne | C — make Feint reads visible |
| **Cover icon on geometry** | XCOM 2, Phoenix Point | A — surface Soft/Hard cover from §5 directly |
| **Wound visualization (limp, blood, dropped guard)** | Bushido Blade, Mordhau, Kingdom Come | All three — canonical Wound Interval becomes visible |
| **Reputation/audience reaction bar in duels** | Pyre, Hades dialogue beats | C — Reputation Cascade (§13.2) live during duel |
| **Outnumbered camera framing** | For Honor, Hyrule Warriors | A and B — visible cue for Fibonacci active |

---

## 7. Outliers and crossover ideas

| System | Crossover idea |
|---|---|
| **Disco Elysium "glass-bottle"** | One-roll life-or-death scene resolution — Valoria has this mode already (Stage 2 Dying, single Medicine Ob 3). Could surface as a deliberate "glass-bottle" duel option — single Combat Pool roll, no rounds, instant resolution. Niche but flavorful for desperate scenes. |
| **Solium Infernum / CK3 duel events** | Conviction wager on duel outcome → loser takes Scar even on survival. Direct Valoria fit for C wager system. |
| **King Arthur RPG / Battle Brothers tactics card system** | Pre-battle tactic card selection (commit a deceit / ambush / hold ground). Valoria's BG layer already has Tactic cards — at scene scale, a single pre-combat tactic card would link layers cleanly. |
| **South Park: The Stick of Truth** | Quick-time block layered on JRPG turns. Adapts as optional reflex bonus for C without breaking math (cap at +1 net hit). |
| **FFXII gambits** | Programmable AI for party members. Companion behavior for A and B — companions act per Conviction/temperament directives rather than direct player control. |
| **Crusader Kings 3 / EU4** | Combat fully abstracted to general traits + tactic dice. Valoria's mass combat is closer to this; scene combat is not. Inspiration only. |
| **Massive Chalice** | Aging + bloodline succession over campaigns. Outside scene combat scope — but Wildermyth-adjacent point: if Wounds become permanent (§7 amendment), generational stakes emerge. |

---

## Top 10 highest-fit picks for Valoria — ordered

1. **Sid Meier's Pirates! duel** → C — three-stance + footwork + edge-push directly maps to canonical pool split + Establish Distance + Stunt. Highest single-fit reference.
2. **Sekiro posture meter** → C — Stamina becomes the visible duel-ender; canonical Out of Breath earns dramatic weight.
3. **Grandia IP gauge** → A and B — visualizes blind-declare/priority-resolve as a tempo timeline; cleanest UI surface for canonical §2.
4. **XCOM 2 cover system** → A — direct lift of Soft/Hard cover from canonical §5 with established UX language.
5. **Mutant Year Zero stealth-to-combat** → A — direct match for Fieldwork → Combat Exposure ladder (§11.5).
6. **Pillars of Eternity 2 RTwP + engagement** → A — viable time-model for general scene combat; Tie Up = engagement is already canonical.
7. **Battle Brothers morale + injury** → A and B — morale plug-in for B's rank-collapse rules; injury locations as inspiration for §7.
8. **For Honor directional guard** → C — three-direction stance UI, Pirates!-adjacent.
9. **Frozen Synapse phase-locked simultaneous** → A — closest existing time-model to canonical §2 phase structure.
10. **Wartales movable initiative bar** → All three — visible tempo meter for canonical initiative transfer.

---

## Architectural implications

- **C duel architecture is highly references-rich.** Pirates! + Sekiro + For Honor + Witcher 1 + Mount&Blade duel all converge on the same family of mechanics (stance + tell + footwork + commit). Valoria's canonical math fits this family natively.
- **A map architecture has strong references for cover, stealth-transition, and tempo UI** but no single reference dominates. Closest single match: Frozen Synapse for time-shape + XCOM 2 for cover.
- **B slot architecture's main reference is Darkest Dungeon itself**, with Persona/Octopath as JRPG cousins. The slot abstraction's strongest argument is **lower implementation cost per encounter** for Valoria's high-volume routine combat.

---

## Canon gaps surfaced

1. **Wager system for duels.** Pirates!/Solium Infernum/CK3 patterns have no canonical equivalent. If C is adopted, canon needs a duel-wager spec (Conviction stake, Renown stake, item stake).
2. **Wound permanence.** Wildermyth raises a tension with canonical recovery (§4 PP-284). Currently Wounds clear at end of session — should some scars be permanent for narrative weight?
3. **Stamina-as-fight-ender.** Sekiro posture pattern. Canonically Out of Breath is −2D but does not end combat; in C, Stamina depletion could canonically end a duel by yielding. Would need a new rule.
4. **Stealth pre-combat phase.** Mutant Year Zero's stealth-to-combat transition is not specified in canon. Currently §11.5 specifies Exposure tiers (quiet/conspicuous/public) but not the *process* of moving between them mid-encounter.
5. **Tactic card pre-combat tap-in.** BG-layer Tactic cards exist canonically; their connection to scene combat is not specified. A pre-scene single-card tap would bridge layers cleanly.

---

## Godot implementation notes

- C is the lowest-cost architecture to prototype — limited scene scope, fixed actor count, side-on 2D rig. Pirates!-style stance UI is days-to-weeks of work.
- B is medium cost — DD-style slot UI is well-documented, but rank-reach matrix and per-character ability authoring scale with party/enemy variety.
- A is highest cost — top-down map, pathfinding, LoS occlusion, projectile physics, full reach matrix evaluation, plus integration with fieldwork/settlement layers on the same map.

If implementation cost gates rollout: **C first** (high payoff per dollar, canonical-math-respecting, strong references), then **B for routine encounters**, then **A as the unifying layer** that absorbs B's encounters once map tech matures.

End Chunk 2.
