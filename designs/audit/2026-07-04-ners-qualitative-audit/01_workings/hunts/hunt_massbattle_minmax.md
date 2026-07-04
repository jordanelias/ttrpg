# Mass-Battle Min-Max Hunt — Working Notes

Lane: massbattle_minmax (adversarial munchkin). Arena: massbattle_minmax.
Read: designs/provincial/mass_battle_v30.md, designs/provincial/mass_battle_integration_v30.md,
designs/architecture/scale_transitions_v30.md §3.6–§3.8, §4.
North Star: myriad meaningful choices; Omega non-dominance (no solvable strategy).

## Brief vectors
1. Scene-bonus (§3.8) stacking/farming before battles
2. General Duel abuse (§3.7) to bypass mass layer
3. Thread-op cost arbitrage at War scale (§A.10)
4. Siege/fort degenerate lines (§A.9)

---

## LINE 1 — General-Duel decapitation (the crown jewel). P1, HIGH.

Permitting rules:
- scale_transitions §3.7: General Duel is a Personal Action available every battle turn
  (Priority 8), 1 exchange/turn, max 5 exchanges; enemy general's Command **suspended** while
  in personal combat (PP-232).
- mass_battle §A.1 design axiom: "**Generalship dominates. ... The general is the battle.**"
- mass_battle §A.5 (ED-898) two-stage incapacitation: wounds → Stage 1 (Command halved) →
  Stage 2 (**Command = 0, all units uncommanded**). §A.6/PP-273: uncommanded units fight at
  **1-die floor, Line formation, no tactics, Discipline 1 floor**.
- mass_battle §A.5 / Part D header **ED-898: "No mass-battle mechanic kills a player or named
  character."** Worst PC outcome = incapacitation, and capture *only if their side loses the
  field*. A winning duelist never loses the field → recovers.
- CALIBRATION: personal-combat spear/polearm dominance 84–96% (KNOWN-TRACKED, PR#72/#76).

The line, as a munchkin states it: "Every battle I bring one spear-optimised PC and open with a
General Duel. My PC **cannot die** (ED-898) — worst case I'm captured, which is a recoverable
world-layer event — while the enemy NPC general I hit goes Stage 1 → Stage 2 → Command 0. With
the general gone, their whole army drops to the 1-die floor, Line only, no tactics. Since 'the
general IS the battle', I've won before formations, composition, thread, or discipline ever
mattered. I never invest in the mass layer at all."

Which choice tree collapses: the **entire Part A apparatus** — formation counters (§A.6),
tactics (§A.8), thread ops (§A.10), unit composition/Military-tier investment (§A.4), discipline
management (§A.13). All become optional flavour behind one dominant opening.

Which Omega clause breaks: **non-dominance** (a solvable strategy exists) and **personal
transformation vs. cross-scale consequence** — the cross-scale bridge is one-directional and
exploitable.

Structural vs tuning: the 84–96% spear number is tuning (calibration), BUT the dominance
**survives retuning** because it rests on the *structural* asymmetry ED-898 (PC no-death /
NPC-general-incapacitable) × the §A.1 "general is the battle" axiom × §A.6 uncommanded-floor.
Even at a 55% duel win-rate the risk-free downside (no death) makes repeated dueling positive-EV
and dominant over investing in the mass layer. => P1 structural.

Load-bearing dependency / uncertainty: §3.7 is thin — it does not state whether the enemy
general can *decline* the duel or exactly how the PC reaches an embedded general. §A.7/PP-101
(embedded practitioners are subject to Phase-5 targeting as fighters) is the closest analog and
implies a front-line general is reachable. Even if declinable, the no-death asymmetry keeps every
*accepted* duel positive-EV, so the line degrades gracefully but does not disappear. Flag the
reachability/decline rule as the one gap to close to fully rate severity.

Novelty: NEW. Spear-dominance itself is KNOWN-TRACKED; the *diagonal exploit* (ED-898 no-death +
§3.7 + §A.1 axiom converting the duel into a risk-free mass-battle bypass) is a distinct
structural finding not on the calibration list. Intent gate: NOT-INTENDED (ED-898's rationale is
narrative jeopardy, not a combat-bypass license; the interaction is unflagged).

---

## LINE 2 — PP-508 canon-admitted split-dominance. P2, HIGH.

Permitting rule: mass_battle §A.8, Splitting doctrine (PP-508, ED-358 resolved): "**Split
dominates concentration by +9% to +45% win-rate**... Splitting is suboptimal ONLY when
[Narrow Pass terrain] or [Size=1 edge]." The doc *states in canon* that one option dominates
across almost the whole matchup space.

Munchkin line: "I always split across all simultaneous engagements. Canon says it beats
concentration by up to 45%, and the only counter is a terrain type (Narrow Pass) the defender
must happen to hold. Concentration is a trap option."

Choice tree that collapses: the **concentrate-vs-split** decision (§A.8 Concentration tactic,
Fibonacci stacking) — a headline tactical axis reduced to a single correct answer outside a rare
terrain exception. Omega **non-dominance** breaks by the doc's own admission.

Structural: survives retuning — the +9–45% band is broad; the dominance is qualitative, not a
knife-edge number. The "counter is Narrow Pass or Feigned Retreat" is terrain-luck, not a
standing counter-strategy. Intent gate: DELIBERATE-but-unexamined — ED-358 "resolved" it as
*intended*, but resolution never applied the Omega non-dominance lens. Novelty: KNOWN-UNTRACKED
(documented in ED-358 as a resolution, but no artifact frames the resulting flattening as a
non-dominance defect).

---

## LINE 3 — Thread scale-cost arbitrage + cap contradiction. P3 (P2 if cap-text wins). MED.

Permitting rules:
- §A.10 scale table: Skirmish/Company Coherence auto-cost **0/op**; Battle/Campaign −1/op;
  War **−2/op**.
- Immediately below: "The Coherence cap (**−1 per operation**, threadwork_v30 §3.2)... **No
  additional surcharge.**"
- PP-501 worked example assumes **1 Coherence/turn** (7 turns → 7 lost).

Two exploits:
(a) **Contradiction**: the War row (−2/op) contradicts the −1/op cap and PP-501. A min-maxer
reads the cap as controlling → War-scale thread costs only −1/op, *erasing the intended
higher-scale substrate gradient*. Either the table or the note is wrong; nothing reconciles them.
(b) **Scale arbitrage**: substrate cost is keyed to *battle scale*, and scale is set by force
size (§A.3). Split a War-scale force into Company-scale engagements to pay **0 Coherence/op**
instead of −2. This **compounds with PP-508** (splitting already wins militarily) — the same
split that maximizes win-rate also zeroes thread cost. Double-dominant.

Choice tree: the "when do I risk the substrate for a thread op" cost/benefit axis (a P-14
threadwork juncture) is void at small scale and self-contradicting at large. Omega non-dominance
+ cross-scale-consequence weakened. Structural (the keying of cost to scale + free split is
architectural), but headline severity is muted because raw op magnitude is small — P3, rising to
P2 if the cap-text reading stands (War thread free-riding). Novelty: NEW (contradiction not on
calibration list). Threadwork juncture verdict: PRESENT-but-mispriced.

---

## LINE 4 — Siege turtle: Walls × Shield Wall × no-idle-penalty. P3 (N-caveat). MED.

Permitting rules:
- §A.9 Walls/fortifications: **Defender +3 DR; no flanking; Slow cannot advance.**
- §A.6 Shield Wall: **+2D Def**, negates one flank; §A.6/PP-500 the +2D applies to *all*
  simultaneous defensive pools.
- §A.7 Phase 7 idle-army clock **terrain exception**: a defender "behind Walls with no available
  advance" does **NOT** take the −1 idle Morale. Turtling is cost-free morale-wise.
- §A.13/PP-711 Morale resets between battles anyway.

Munchkin line: "Defender in Shield Wall behind Walls: +3 DR + +2D Def on every engagement, no
flanking possible, and the idle-clock that's supposed to punish passivity is explicitly waived
for me. I sit. My only real threat is enemy Artillery — which their §A.14b Campaign Supply
(−100 Treasury/season, +attrition in Prosperity-0 land) bleeds them to bring and sustain."

Choice tree: the *besieged defender's* decision tree collapses to a single move (hold), and it's
strictly optimal with no morale downside. Attacker options survive (Artillery, starve-out,
thread, assault), so it's dominant-but-counterable at the attacker's side.

Structural vs N: sieges favouring the defender is **N-grounded** (real Renaissance dynamic) — so
flag, don't reject. The specific defect is the *combination* (Shield-Wall-cannot-advance +
Walls-no-flank + idle-penalty-waiver) that removes even the "you must eventually sortie or rot"
tension, making the hold a no-cost dominant. P3 debt with N-caveat; would become P2 if the
attacker's economic counter (Artillery + supply drain) turns out under-tuned. Novelty: NEW.
Intent gate: UNDETERMINED (idle-exception is deliberate terrain realism; the emergent no-downside
turtle is unflagged).

---

## LINE 5 — Scene-bonus triple-stack pre-battle ritual (§3.8). P3, MED.

Permitting rule: scale_transitions §3.8 (PP-261, ED-151): Social win → +1D unit Command;
Investigation win → +1D first Volley; Combat win → one free Reform action. "Modifier to most
relevant unit; **1 turn duration**." No cost, no per-battle cap on feeder scenes, three
*different* bonus channels.

Munchkin line: "Before every battle I clear a soft social scene AND a soft investigation scene
AND a soft combat scene — I stack +1D Command, +1D first Volley, and a free Reform on turn 1,
free, every time. It's not a choice; it's a mandatory pre-battle ritual any optimal player runs."

Choice tree: mild non-dominance erosion — the scene-vs-battle *tempo* choice degenerates to
"always farm scenes first." Bounded hard by +1D / 1-turn / turn-1-only, so magnitude is small.
Structural (the bridge is uncapped-in-count and player-pace-controlled) but low-impact => P3.
Novelty: NEW. Intent gate: DELIBERATE bridge, unexamined for farming.

---

## Severity summary
- P1: General-Duel decapitation (Line 1) — NEW diagonal.
- P2: PP-508 split-dominance (Line 2) — KNOWN-UNTRACKED.
- P3: thread scale/cap (Line 3, NEW); siege turtle (Line 4, NEW, N-caveat);
  scene-stack (Line 5, NEW).
