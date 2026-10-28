# R01 — Is pure bottom-up emergence a problem; can partial top-down guides help (with oatmeal research)

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> Question for how to make emergent narratives be legible and coherent: is it an issue to assume everything works bottom-up? is it possible to use a partial top-down approach to set up narrative arcs with a series of long-term guides for characters through ambitions, factions through some form of goals, offices through some form of duties, cohorts/settlements re politics/identities, etc?
> you are allowed to contravene existing rulings here. please refer to our precedent research on this topic
> especially academic research re oatmeal
> our goal is to answer the question of whether there should be doing dynamic top-down guiding logic with handshakes to bottom-up context driven events
> or should it all work bottom-up from primitives

---

**Verdict.** Use a partial top-down, but not as a director that writes outcomes into the world. The precedent in this repo supports top-down in three places: standing motives held by actors, selection of what the player is shown, and a narrow channel that offers declinable occasions. Every state change stays bottom-up. The measurements also say the bottom-up layer isn't ready to carry guidance yet.

**Why pure bottom-up fails here**
- I rendered the deepest cross-person chain for seeds 0–4 over four seasons (`harness/chronicle.py`). 55 of 67 chain acts end in a refused, blocked, unavailable or empty result (82%). The chains run 11–15 acts deep, and none says why anyone acted.
- That count uses the suffix definition from `proposals/2026-10-13-narration-mechanisms.md`, which over-counts degree bands. Seed 5 hadn't finished when I stopped.
- That proposal's seed-0, two-season readings: 929 of 1,318 acts were refused or null (70.5%). 439 acts (33.3%) aimed at a subject that exists as another kind. The standing-ambition question won 51 of 803 deliberations. 37 of 80 persons carry no pursuits.
- The precedent names this failure. The Tale-Spin effect is state outgrowing expression (Ryan, Mateas and Wardrip-Fruin, as summarized in `08_ch5_what_we_should_not_do.md` row 4). Tracking state is not expressing it (`research/by_lane/WR_world.md` T-WR-4).
- `WR_world.md` T-WR-2 against T-WR-8 gives the other half. "A threshold may never act" combined with dark knobs leaves the world quiet by construction.
- The repo's own oatmeal passage (`10_the_slate_and_salience.md:113`) says the same from the player's side. A hundred true, caused events a season reach the player as noise.

**What the oatmeal research implies**
- Compton separates perceptual differentiation (easy) from perceptual uniqueness (hard). Her budget rule, "not everyone can be a main character", is a top-down act. Something must designate which instances get depth. Her remedy for "alive" is traceable process, which is bottom-up provenance (`07_ch4:239`).
- Top-down templates do not cure oatmeal. The repo's own refutation (`_workings_joined.md:4903-4940`) shows typed arc vectors guarantee only slot-filler divergence. Two seeds that differ in proper nouns are "exactly Compton's oatmeal failure".
- Bottom-up state divergence does not guarantee perceptible divergence either. WFC's coherence is local only, and expressive-range analysis is "necessary and not sufficient" (`08_ch5` §8.4). Nothing certifies generated content as good (N-5).
- So no metric will prove the hybrid right. Only narrower claims can be falsified, and human reading has to close the rest.

**Design**
1. **Motive, inside the actor.** Top-down data that the actor reads as its own state. It names referents, not outcomes, and it needs a lifecycle: form, advance, obstruct, lapse or fire, succeed. That is what `09_ambitions_and_arcs.md` §6 designs. "Dynamic" then means motive turnover, with a successor drawn by predicate when one fires. `goals.yaml` already has the right shape: referents, attention only, never acts (`goals.yaml:9-12`). It has no lifecycle field.
2. **Selection, outside the world.** An observer and the player's slate read the sim and write nothing back. This is the Light Function without the retired Key substrate. Compton's budget rule and your "oatmeal soup" problem are both solved here.
3. **Occasion channel, the only write.** Two forms are lawful:
   - Predicate hooks, per your 2026-08-18 ruling: script the predicate, never the arc.
   - Boot-time authored occasion rows (`narration-mechanisms.md` W8, Rung 2), which raise a question a person may decline.

   Control: with zero rows the world hash must be byte-identical.

**Where I'd contravene a ruling, and where not.** I'd narrow ED-IN-0225's wording, as `narration-mechanisms.md` §3.5 proposes. It closed one question, "what is an arc as an engine-held thing", and was later cited as a prohibition. I'd keep the refusal of need-triggered outcome injection, even with your permission to overrule. The grounds hold: a threshold that acts is an actor, an injected beat has no author and can't be contested, and the storybar would end up measuring its own injections. No drama-manager evidence in the precedent outweighs them. The Wildermyth casting and RimWorld storyteller precedents (P38) are pacing and selection, which channels 2 and 3 already cover.

**Per layer**

| Layer | State in code |
|---|---|
| Character ambition | `ambitions()` exists, but the need question wins about 6% of deliberations. Putting it first starved news: `news.told` fell from 14 to 7 and events from 21,735 to 15,738 (`world_q.py` `attention_key` docstring). The trade-off is measured. |
| Faction goals | 38 rows, mostly faction and body level. Static, no lifecycle. |
| Office duties | `remit_acts` is a licence, not an obligation. Only 2 of 38 goal rows attach to a seat (`goals.yaml:450,468`). Duty is the thinnest layer. |
| Cohort / settlement identity | None. Cohorts carry no wants (`cohorts.yaml:18-23`). Only `harness/decision_spread.py` mentions "temperament" under `engine/season/`. |

**Falsifiers.** Raise ambition weight and measure two things together: the share of chain acts whose winning question was an ambition referent, and `news.told`. The hybrid fails if the first rises and the second collapses. Also run a two-armed ablation of the recognition layer (the CK2 apophenia item), which needs human readers.

[GAP: primary literature — the repo's research states "I verified none". I did not re-fetch Compton, Smith and Whitehead, or Ryan et al. I also did not consult drama-manager work outside the repo, such as Façade or Riedl. The "no comparative evidence a drama manager helps" claim (UP05 T10) is read through `WR_world.md`, not the uploaded file.]
[CONFIDENCE: medium — the chain measurements cover five seeds with no control arm, and the narration figures are one seed over two seasons from uncommitted scratch instruments.]
