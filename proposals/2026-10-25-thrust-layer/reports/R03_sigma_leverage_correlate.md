# R03 — Is there a sigma-leverage correlate for the likelihood of subsequent events (preliminary findings)

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> The engine use a sigma leverage technique to adjust the probability of success/failure for a dice outcome against an obstacle by accounting for standard deviation (or something).
> 
> I am aware that "by chance" for legible narrative concerns a string of discrete events that could be construed together.
> 
> However, if we have any guides like character ambitions, office duties, faction goals, settlement challenges, possible arc decks (like event decks but that assign arcs?), etc... are those something that could be used to alter the probability of subsequent events..? like, is there a correlate to sigma leverage in what may call the likelihood of subsequent events?
> 
> like, if each event/action for a character is truly emergent from primitives, then it will always be a discrete series of actions that may be construable by chance
> 
> and the ambitions etc may bias this discrete series into being more construable
> 
> but what if we were to calculate the likelihood of SUBSEQUENT events for each choice? as well as the likelihood of other characters etc being involved? what if the game were to invisibly calculate the DEPTH of consequences to character choices to one or more levels, and then based upon those intensive computational branches, bias all potential actors towards a branch that can be narratively construed?
> (sent mid-turn) what about defining ambitions as an overall thrust for a character, but having a series of short- or medium-term goals?
> (sent mid-turn) Provide preliminary findings

---

**Preliminary findings.** Yes, a correlate of sigma leverage exists, and the chooser already has a slot for it. In the toy world I tested, though, lookahead-biased choice was the weakest way to get arcs. A ladder of goals under each ambition, closed by a threshold-raised decision, matched the scripted director without writing any outcome.

**The sigma-leverage correlate**
- `engine/season/decision/choose.py::_sample_order` already orders an actor's candidate acts by `softmax(score/τ)` with `choice_temperature = 0.1`. The noise is keyed per candidate, which keeps forks attributable.
- A narrative term added to the score would be the correlate:
  - Express it in τ units and soft-cap it as `soft_cap` does in `sigma_leverage.py`.
  - Keep it on the choice stage, never the dice resolution.
  - Never remove an option.
- That is the same "shift the mean, never the obstacle" rule the dice engine follows.

**Toy results.** The world is a toy I built. Everything below is exploratory unless marked, and nothing involved human readers. The lookahead and goal-ladder-plus-tribunal arms were not pre-registered.

| Arm | Arc rate | Arc minus shuffled null | Closure | Complete beats | Outcomes injected |
|---|---|---|---|---|---|
| Bottom-up | 0.09 | −0.02 | 0.31 | 0.11 | none |
| Ambition alone | 0.06 | −0.02 | 0.23 | 0.11 | none |
| Ambition ladder, 3 tiers | 0.14 | +0.00 | 0.38 | 0.18 | none |
| Ladder + threshold-raised tribunal | 0.38 | +0.09 [+0.04, +0.15] | 0.85 | 0.43 | none |
| Scripted replanning director | 0.35 | +0.10 [+0.04, +0.16] | 0.85 | 0.76 | forced |
| Utility chooser, no leverage (120 seeds) | 0.02 | −0.01 | 0.15 | 0.04 | none |
| Lookahead leverage, strength 4 (120 seeds) | 0.09 | −0.08 [−0.14, −0.01] | 0.49 | 0.22 | none |

The last two rows use a different base chooser from the rows above them, so compare them only with each other.

1. **Your ladder idea helps modestly on its own.**
   - A three-tier ladder lifts the arc rate over ambition alone by +0.09 [+0.04, +0.14], and keeps the "why" legible (0.72).
   - Depth matters: two tiers give about the same as three, and one tier does nothing.
   - It has no ordering signal beyond chance by itself.
   - Per ambition, 27% complete fully, 42% end mixed, and 4% never meet a stage.
2. **The ladder plus a closure engine is the best lawful result.**
   - A threshold raises a tribunal, each party may decline, and a decider actor rules.
   - Its ordering signal equals the scripted director's.
   - Sixteen of 21 comparisons aside, the difference to the director is −0.03, and the interval spans zero.
   - Cost is one threshold check per season.
3. **Lookahead leverage works against its own goal.**
   - Strength 4 means 126 leveraged decisions per run, about 3,200 rollouts, and roughly 270 times the run time.
   - 32% of leveraged decisions flipped.
   - Closure rose from 0.15 to 0.49, complete beats from 0.04 to 0.22, and cross-person chain depth from 18 to 31. That depth is what the proxy rewards, so it is partly circular.
   - The shuffled null rose faster than the arc rate, so there is no ordering signal.
   - Explained motive fell from 0.58 to 0.29. The tilt moves choices the actor's own scores did not favour, so the "why" weakens.
4. **Both lawful routes collapse on a mostly-refusing substrate.** At 80% refusal, the real engine's rate, the ladder-plus-tribunal arm falls to 0.21. The forced director holds at 0.71.

**Preliminary recommendation.** Build goal ladders under ambitions and threshold-armed, declinable decisions first. Keep lookahead leverage as a bounded option for a few thread-bearing actors. Fix the substrate's refusal rate before either: it is about 80% in the chains I rendered, and it defeats both.

The v2 narrative-engine rules R-AI and F8 would be overridden by lookahead leverage; I did not touch them. If you adopt it, F8 becomes a dosimeter: report the change in outcome probability per unit of leverage.

[GAP: two-level lookahead, other value proxies, and any human judgement of "construable" were not tested.]
[CONFIDENCE: low-medium — the model and metrics are mine. The arc test passes a lone closing event at any season, so read arc rate beside the null. The ladder predictions scored 4 of 7, with H1, H4 and H7 falsified.]

Files are in `proposals/2026-10-25-thrust-layer/toy/`: `lookahead.py`, `regimes5.py`, `exp_ladder_out.txt` and `lb_more_out.txt`.
