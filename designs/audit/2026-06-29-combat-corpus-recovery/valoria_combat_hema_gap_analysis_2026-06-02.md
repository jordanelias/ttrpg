# Valoria Combat Engine — HEMA / Academic Gap Analysis
**2026-06-02 · what the literature deems critical, mapped against the engine, severity-ranked**

`[READ: Liechtenauer corpus (Five Words Vor/Nach/Stark/Schwach/Indes; Hauptstücke; four openings; bind handwork — Ringeck/Danzig glosses, Keith Farrell, James Colton, hema101); Italian rapier (Capoferro/Fabris/Giganti — tempo, contratempo/time-thrust, stringering, cavazione, body voids — Leoni "Understanding Tempo", renfence, Colton); academic experimental (Jaquet et al., PLOS One / Acta Periodica Duellatorum — armour energetics + range of motion)]`
`[SELF-AUTHORED — bias risk: assessing my own engine; surfacing gaps an independent HEMA reviewer would raise, worst-first, no false balance.]`

## VERDICT
The engine models the **physical substrate** well (reach, measure, leverage, bind mechanics, armour-defeat, geometry,
guards, tempo, fatigue). The biggest gaps are **not physical — they are tactical-temporal**: the literature's single
most-emphasised idea (INITIATIVE — Vor/Nach/Indes) and its Italian twin (CONTRATEMPO — striking in the opponent's
tempo) are only partially present. These are deemed *the core of the art* by the sources, so they are the highest-
value additions. Everything else is secondary.

---

## CRITICAL (the literature calls these foundational)

### G1 — INITIATIVE as a persistent, seizable state (Vor / Nach / Indes). **PARTIAL → the #1 gap.**
Every German source: *"Initiative is the most important concept… whoever has the initiative can win; whoever lacks it
must first seize it."* The Five Words (Vor, Nach, Stark, Schwach, Indes) are said to contain "the complete Art."
- **In the engine:** an aggressor is assigned each beat (a momentary proxy for the Vor), and Stark/Schwach is present
  in the bind (leverage + tactile). 
- **Missing:** initiative as a *state that persists and is contested* — the Vor isn't held, pressed, or *stolen*. And
  **Indes** (acting in the instant — in the middle of the opponent's action — to seize the Vor) is absent entirely.
  Right now defence is parry/dodge/wind/displace; there is no "act *during* the opponent's committed action to take
  the initiative." This is the engine's largest conceptual gap vs the literature.
- **Fix (emergent):** an `initiative` state (who holds the Vor) that (a) confers a standing edge while held, (b) is
  lost by over-committing / being read / losing a bind, (c) can be STOLEN *indes* by a fighter who wins the read in
  the opponent's tempo. Reading already gates much of this — initiative would give those reads a persistent stake.

### G2 — CONTRATEMPO / single-time counterattack (the time-thrust). **PARTIAL.**
Italian masters: *"it is safest to attack DURING an opponent's tempo"*; the time-thrust "strikes and shuts out the
line at the same time" (one tempo, not parry-then-riposte). Most of Fabris/Capoferro is contratempo.
- **In the engine:** there is a riposte (strike *after* a successful defence = two-tempo) and a stop-hit in the
  approach (gap-proportional). 
- **Missing:** the **single-time counter** — defending and striking in ONE action by closing the line (opposition),
  and the **body void** counter (passata sotto / inquartata: evade by displacing the body, not the blade, and hit in
  the same tempo). The engine voids with the weapon (parry/displace) but never with the *body*.
- **Fix:** a single-tempo counter option in the defender's mode set (gated on reading + a committed/over-extended
  attacker), resolving attack-and-defence in one exchange with line-closure; and a body-void defence distinct from
  weapon-parry. The displacement primitive is the closest existing hook.

### G3 — STRINGERING / closing the line before attacking (constraint of the blade). **MISSING (rapier-class).**
Capoferro: *"never strike without stringering first, or you leave the opponent free to strike simultaneously."*
Engaging/constraining the opposing blade (gaining leverage on the foible) is the precondition for a safe rapier
attack; the counters are the disengage (cavazione) and reversing the leverage.
- **In the engine:** the bind models leverage/Stark-Schwach once blades are crossed, but there is no *pre-attack
  blade engagement* (gaining the line) and no **disengage (durchwechseln / cavazione)** to escape a bind by passing
  under to the other line. Disengage is also a core German Hauptstück (Durchwechseln) — so this gap spans both
  traditions.
- **Fix:** a "gain the line / constrain" pre-attack action (raises attack safety, opposed by disengage), and a
  `disengage` option out of an unfavourable bind (escape the leverage at a tempo cost). Pairs naturally with G1/G2.

---

## SECONDARY (real, lower priority — refinements, not foundations)

### G4 — Targeting the FOUR OPENINGS. **MISSING (abstracted).**
Liechtenauer divides the foe into four quarters (openings) and the whole bind game is "strike the most convenient
opening / from one opening to the other." The engine resolves to a single hit pool with no high/low / inside-outside
target geography, so feints-to-one-opening-and-strike-another and overrunning (high line beats low) aren't modelled.
*Acceptable abstraction for now* — adds real depth but also real complexity; revisit if duels need finer texture.

### G5 — ARMOUR'S ENERGETIC / MOBILITY COST (academic, quantified). **PARTIAL.**
Jaquet et al. (PLOS One): armour raises the energy cost of locomotion *in slight excess of its added weight* and
*reduces range of motion at the joints*. The engine has generic fatigue (tempo decay) but **armour itself imposes no
extra stamina drain or mobility/footwork penalty** — a plate fighter tires like an unarmoured one. Empirically wrong.
- **Fix (cheap, grounded):** an armour-scaled stamina-drain multiplier + a small footwork/range-of-motion penalty in
  armour. Has real tactical consequence (the unarmoured fighter's late-fight endurance edge — a documented duel
  reality) and a published number to calibrate against.

### G6 — GUARDS / WARDS as positions with transitions (vom Tag/Ochs/Pflug/Alber; Italian guardia). **MISSING.**
Both traditions start from named guards with distinct line-coverage and transition costs; the master-strikes are
defined relative to them. The engine has stance-stability but no guard *position* governing which lines are
open/closed or what a transition costs. *Lower priority* — large modelling surface; the openings (G4) would come
first.

### G7 — NACHREISEN ("chasing" / following the recovery). **MISSING (minor).**
Striking into the opponent's withdrawal/recovery after a missed or over-committed action. The over-commit-recovery
window exists (it feeds re-opening); chasing would let the *aggressor* exploit it offensively, not just let the
defender re-open. Minor; falls out of G1 if initiative is modelled.

---

## WHAT THE ENGINE ALREADY DOES WELL (vs the literature)
Fühlen/Stark-Schwach in the bind (tactile read + leverage) ✓; binding/winding with hilt-dependent catch ✓;
displacement/absetzen (set aside a committed thrust) ✓; measure & tempo theory, conditional tempo ✓; the half-sword
for armour (mit dem kurzen Schwert) ✓; armour-defeat rotation (cuts die, thrust/percussion rise, gap-thrust
precision, percussion authority) ✓; reach→clinch reality in armour ✓; cross-tradition cognitive modelling ✓;
feinting (capped, readable) ✓; geometry-derived cut/thrust/force-concentration ✓.

## PRIORITISED RECOMMENDATION (worst-first; emergent, validated top-down — NOT parity-seeking)
1. **G1 Initiative (Vor/Nach/Indes)** — the literature's #1 concept; currently the engine's largest gap. Highest value.
2. **G2 Contratempo / single-time counter + body void** — the Italian core; pairs with G1.
3. **G3 Stringering + disengage (cavazione/durchwechseln)** — precondition/escape of the blade game; spans both schools.
4. **G5 Armour energetic cost** — cheap, academically quantified, real tactical consequence (endurance).
5. (later) G4 openings, G6 guards, G7 nachreisen — depth refinements, larger surfaces, lower priority.

`[CONFIDENCE: high on the gap identification — these are the explicitly-foundational concepts across the primary HEMA
and academic sources; the engine's coverage was checked against the current committed modules. Severity is judged by
how central each source deems the concept, not by matrix impact.]`
