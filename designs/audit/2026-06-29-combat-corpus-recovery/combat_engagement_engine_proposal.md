# Applying the Combat-Engagement Psychology Findings to the Engine — Proposal
**2026-06-25 · companion to `combat_engagement_psychology_findings.md` · target: `designs/scene/combat_engine_v1/` @ HEAD · status: PROPOSED, mechanical-tier, Jordan-vetoable · discipline: same NERS distillation as `combat_traditions_ners_distillation.md`**

`[SELF-AUTHORED — bias risk: the temptation here is to turn five psychology findings into five new mechanics — the exact over-granularity that got cut last round. The honest result is the opposite: most of the psychology is *already in the engine*, the research mostly **validates** the existing model, and only one finding earns a new primitive. I have actively resisted manufacturing levers; what I did not propose is in §5.]`

**Headline.** The combat engine already encodes most of the psychology of engagement — feinting, the telegraph/power tension, and the overcommitment-exploit are all built and are confirmed faithful by the literature. The findings therefore yield (a) a **reframe** (the regime contest as the organizing lens — already actioned by the clinch↔disengage pair), (b) a short list of **tunings** to existing mechanics, and (c) **one genuinely new tendency**: hesitation-as-assessment against an unreadable opponent. One new constant, no new subsystem.

> **ERRATUM (2026-06-25, parallel to the findings-doc erratum).** Two items here inherited the findings document's now-retracted "experts are more susceptible to deception" claim and are corrected below: **(1)** the §2 feint tuning that scaled feint payoff with the defender's *reading skill* is **withdrawn** — experts are not more foolable; the feint is a forced-response / timing / expectation-alignment contest, which `feint_eval` already models, so no tuning is needed there. **(2)** the §3 `wariness` mechanic is **re-grounded** from the brainstem "assessing-freeze" to the **deliberative assessment cost** (Hick's law / OODA) against an unpredictable opponent — a cleaner, more defensible basis for a familiarity-scaled caution. The mechanic itself is unchanged and survives; only its justification moved. The shoot-on-commitment hook (§4) was already grounded on commitment *biomechanics* — the correct version — and is unaffected.

---

## §1 — The reframe (a lens, not a mechanic)

The research's central result — *the primary contest is over fighting on your own terms* (findings §5, §6) — is the same object the distillation already adopted: the **regime contest** across the measure/contact/tempo bias-space, with the **clinch ↔ disengage** pair as the contact-axis battle. The MMA literature is near-verbatim confirmation (striker keeps it out / grappler forces it in; the contested mid-range "danger zone"). **No new mechanic here** — but it sets the tuning target: a fighter's weapon × tradition should produce a *legible regime bias*, and the existing systems (reach + approach/reopen for measure, the channel-weights for tempo, clinch/disengage for contact) should be tuned so those biases are felt. The lens earns its keep by telling us what "good" looks like, not by adding apparatus.

---

## §2 — What the research validates (already built — credit + optional tunings)

These are the cases where the honest finding is "the engine already does this, correctly." Each gets at most a **Class-C tuning**, never a new lever.

| Finding | Already in the engine | Validation | Optional tuning (tunable, not a new mechanic) |
|---|---|---|---|
| **Disguise = the feint; it works by forcing a costly response, not by fooling better readers** (findings §1, corrected) | `feint_eval` (`systems.py:194–207`, called `wrapper.py:120`): a feint degrades a fooled defender's read/defence; a defender who *reads* it gains a counter-edge | Faithful — the feint is a credibility/timing contest (`feint_q` vs `def_read`), and a credible threat must be answered | **No tuning — and specifically NOT a "better readers are more foolable" term** (withdrawn; the evidence is that experts read *better*). If anything is tuned, tie feint efficacy to **timing and expectation-alignment** (a fake that rides the opponent's most-probable read is stronger), which the `feint_q` vs `def_read` contest already approximates. `[no change recommended]` |
| **Telegraphing = preparatory power-loading leaks intent** (findings §2) | `legibility` (`systems.py:177–192`, called `wrapper.py:130`): swings/blunt easy to read, thrusts hard, **deeper commit = more readable**, lunge adds legibility | Exactly the power-vs-deception tension — the wind-up announces | Confirm the mapping is calibrated; the "loaded heavy blow telegraphs more" refinement is the **deferred power-source axis (I3)** — leave deferred per the distillation. |
| **Overcommitment is exploited by countering on the commitment** (findings §3) | commit-depth exposure + the in-the-instant steal (`wrapper.py:147–158`) + `overcommit_exposure` feeding the riposte (`wrapper.py:163, 173–198`) | "Shoot/counter on the opponent's commitment" is precisely the read-a-deep-commit → steal-the-lead path | No change needed. Already faithful. |
| **The bout is a range contest with agency on both sides** (findings §5) | reach + the approach/`reopen` system (`wrapper.py:66–85, 217–226`) | The measure axis is emergent and two-sided | Tune so the regime bias is *felt* (the §1 target). No new mechanic. |

The takeaway worth stating plainly: **the engine's psychological model is sound.** That is a finding, not a non-finding — it means the previously-proposed clinch/disengage pair sits on a base that already represents disguise, telegraphing, and the commitment-exploit correctly.

---

## §3 — The one new tendency the research earns: **wariness (assessment under unpredictability)**

The single psychological primitive the engine does **not** represent is **assessment-cost under unpredictability** (findings §4, mechanism 1): facing an opponent whose next action you cannot predict, you must weigh more live possibilities and decide slower — **Hick's law** and Boyd's **OODA loop** — a *deliberative* caution, not a brainstem freeze. The engine has the perfect existing hook for "unpredictability": the **`familiarity` system** (`tradition.py:62–67`) — a fighter reads an *unfamiliar* tradition worse (0.85 default / 0.93 adjacent / 1.0 same-or-none).

**Proposal — `wariness`: against a less-familiar opponent, a fighter commits more cautiously and initiates less eagerly.** A tendency, scaled by `(1 − familiarity)`, so it is **exactly zero at full familiarity** (same/known/neutral matchups and the mirror are byte-identical — invariant-safe) and small at low familiarity.

- **`[MODIFY @ wrapper.py:98–106]` (commit-depth pick):** shade the commit distribution toward shallower against a low-familiarity opponent — the assessing brake on over-extension. Concretely, fold a `WARINESS_K*(1 − TR.familiarity(aggressor.tradition, defender.tradition))` term into the disposition commit-skew so an unreadable opponent pulls the distribution toward {2,3}. No-op at familiarity 1.0.
- **`[MODIFY @ wrapper.py:87–93]` (aggressor selection), optional:** a slightly higher effective `ACT_THRESHOLD` against an unreadable opponent — a beat of assessment before initiating. Bounded, no-op at full familiarity.
- **`[ADD @ config.py CFG]`:** one constant, `WARINESS_K` (Class-C, collision-checked against the 150 live keys).

**Grounding.** Bottom-up: the existing commit-skew + aggressor-selection machinery + the `familiarity` system. Top-down: the **deliberative choice-reaction cost** — more credible alternatives → slower, more cautious commitment (Hick's law; Boyd's OODA loop) — which is the combat-relevant hesitation (findings §4, mechanism 1), **not** the brainstem defense-cascade freeze (which the findings flag as an extrapolation to a voluntary bout). **NERS:** one tendency over existing machinery, no-op when the opponent is readable, Class-C tunable — it *adds* a real, felt, grounded behaviour (a fighter is visibly more cautious against an unfamiliar style, and looser against a known one) without a new subsystem. It also deepens an existing system (familiarity) rather than bolting on a parallel one — the elegant direction.

**Why this and not a "freeze mechanic."** The combat-relevant hesitation is the deliberative assessment cost above, not the brainstem freeze or tonic immobility (the late, circa-strike shutdown the findings flag as an extrapolation to sport). So the mechanic is a **bias on commitment/initiation**, not a stun or a skipped turn. A literal freeze-state would be both unfun and a misreading of the science; the tendency is the faithful form.

---

## §4 — One optional connective hook (no new mechanic): regime-shift on the opponent's commitment

The MMA finding "**shoot the takedown on the opponent's strike/forward-commitment**" (findings §5) is the meeting point of §2's overcommit-exploit and the clinch/disengage pair. It needs **no new mechanic** — only a *wiring*: gate the (already-proposed) `clinch`/`disengage` triggers on the **existing** `overcommit_exposure` signal (`wrapper.py:163`), so a fighter is best able to *change the regime* (force the clinch, or slip to distance) at the moment the opponent has overcommitted. `[INSERT @ wrapper.py:214–226]` region, reusing the existing exposure value. This makes "impose your terms by catching them committed" emergent from two things the engine already computes. Optional; ship after the clinch/disengage pair lands.

---

## §5 — NERS check, and what I deliberately did NOT propose

**Did not propose (resisting the granularity that got cut last round):**
- No "deception lever family," no "telegraph lever," no "morale/intent stat." Disguise and telegraphing are *already* the feint and legibility systems — tuned, not multiplied.
- No literal freeze/stun state (a misreading of the science; unfun).
- No new emotion/arousal subsystem — fatigue already drives reach/lunge, and disposition already carries temperament; "wrath → overcommit" is covered by the existing commit-skew + fatigue.
- No re-opening of the deferred power-source axis (the "loaded blow telegraphs" refinement stays deferred).

**NERS verdict on the proposal:**
- **N:** the one new item (`wariness`) is necessary — it is the only psychological primitive with no existing home, and it catches a real, felt behaviour. The tunings are optional and removable.
- **R:** adds a separable, intuitable behaviour (caution scales with the unknown) without false depth.
- **S:** integrates by *deepening* the existing `familiarity` system, no category-boundary friction.
- **E:** one constant, no subsystem; "you fight more carefully against a style you can't read" is immediately intuitable.

**Re-test (does wariness re-introduce over-granularity?):** No — it is a single tendency over an existing system, no-op at full familiarity, one constant. It is the opposite of the lever-pile that was cut: it makes an *existing* number (familiarity) do *more* work.

---

## §6 — Layer boundary & status

Mechanical-tier: the `wariness` tendency, the wiring hook, and the tunings are all biases over machinery already in `engagement()`, grounded bottom-up + top-down, Jordan-vetoable. **Untouched (Jordan's):** roster, flavour, and the metaphysical layer. The findings document is descriptive; this proposal is the only place new mechanics are suggested, and it suggests precisely one.

**Not committed.** Both this proposal and the findings document sit in outputs alongside the session's other deliverables. A session checkpoint (`canon/session_checkpoint.md`) already records the arc. Landing any of it as canon is a `safe_commit` + `Citations:` pass under `designs/audit/2026-06-25-combat-traditions-morphology/` on your go — not done unprompted.

- `[CORRECTION: §2's feint tuning (scale feint payoff with defender reading-skill) is withdrawn, and §3's `wariness` is re-grounded from the brainstem freeze to the deliberative assessment cost (Hick's law / OODA) — both inheriting the findings-doc erratum. The wariness mechanic is unchanged; only its justification moved. The shoot-on-commitment hook (§4) was already correctly grounded on commitment biomechanics.]`
- `[CONFIDENCE: high]` that the engine already encodes disguise/telegraphing/overcommit-exploit (anchored to lines read first-hand this session). `[CONFIDENCE: high]` that `wariness` is the single missing primitive and that `familiarity` is its correct home. `[CONFIDENCE: medium]` on the exact tuning magnitudes (Class-C, uncalibrated).
- `[GAP: no sims run — `wariness` needs the invariant pass (no-op at full familiarity) + calibration before it lands; combatant.py still not read in full.]`
