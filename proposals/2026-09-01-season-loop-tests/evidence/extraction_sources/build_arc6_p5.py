import json

cases = []

def N(need, why, hardness):
    return {"need": need, "why": why, "hardness": hardness}

# ---------------- SCN-LOOP-A ----------------
cases.append({
  "id": "SCN-LOOP-A",
  "name": "The self-worsening spiral toward world-currency collapse",
  "one_line": "A practitioner's own voluntary ambition starts a reinforcing loop where harder operations cause more failures which cause more difficulty, eventually disabling the one institution positioned to counter it.",
  "scale": "realm",
  "season_requires": [
    N("The loop's root trigger (a practitioner's own choice to attempt larger-scale operations) must be a purely voluntary, repeatable choice with no built-in limiter — the system must not require any external gate before a practitioner can choose progressively larger-scale operations that spend the shared currency.",
      "An externally-gated trigger instead of an unrestricted voluntary one would prevent the loop from being freely re-enterable purely by player ambition, as the source frames it.", "core"),
    N("Once the shared currency crosses a specific threshold, the resulting global difficulty increase must feed BACK into the SAME roll type that spends the currency, such that operations attempted after the threshold crossing are measurably more likely to produce the outcome (failure/partial) that costs MORE of the currency — a genuine reinforcing, not merely additive, feedback loop within the same resource.",
      "An additive-only relationship instead of a true feedback loop would not produce the described self-accelerating spiral distinct from ordinary bad luck.", "core"),
    N("The hazard-spawning consequence of failed operations must be able to, several steps later, raise a public-facing suspicion/credibility metric belonging to a THIRD, otherwise-unrelated tracked axis — the loop must cross from a personal/practitioner-scale resource into a wholly separate faction-scale clock through an intermediate hazard event, not directly.",
      "A direct link instead of a hazard-mediated one would misrepresent how the described chain actually propagates through an intervening observable event.", "important"),
    N("Rising factional instability arising from the above chain must be able to cause a SEPARATE institution's own routine seasonal actions to 'misfire' purely as a side effect of instability, without any single roll dedicated to causing the misfire.",
      "Without an instability-to-misfire link, factional unrest would have no mechanical bite on institutions' own unrelated seasonal actions.", "important"),
    N("A specific institution's own COUNTER-MECHANISM against the loop's root cause must be able to become UNAVAILABLE to that institution specifically because of a DOWNSTREAM consequence of the very loop that mechanism exists to counter — the loop must be able to disable its own antidote as a late-stage consequence of its own progression.",
      "Without this self-disabling property, the loop's stated self-defeating character — the same institution that could stop it loses the ability to as the loop worsens — could not be represented.", "core"),
    N("UNCLEAR: the loop description names no deliberate off-switch of its own — every step is described as either automatic or a worsening feedback, with the sole stated exit routed entirely through a DIFFERENT case's own structural-exit checklist, one of whose required conditions (stop large-scale operations) is in apparent tension with another required condition of that same checklist (a large-scale COLLECTIVE operation must still succeed to mend gaps) — the source does not resolve whether 'large-scale ambition' and 'large-scale collective mending' are the same action-category for eligibility purposes.",
      "If the two conditions are the same action-category, the terminal case's own stated exit path may be internally unsatisfiable once this loop has progressed far enough to trigger it, and nothing in the source resolves this.", "important")
  ],
  "temporal": {
    "span_seasons": "ongoing, multi-season, described as the most common campaign-ending pattern",
    "needs_memory_of": "the shared currency value and its threshold state; the credibility metric; the external-pressure clock; the specific institution's own standing resource, to know if its counter-action is currently gated.",
    "needs_deadline": "no fixed date, but functionally yes since the shared currency's terminal floor is a hard stop"
  },
  "who_acts": ["the practitioner (chooses to attempt large/ambitious operations — the loop's only voluntary step)", "the specific institution (would choose to attempt its counter-action, if able)", "nobody decides any of the threshold crossings, the hazard-to-metric propagation, the instability-to-misfire step, or the standing-resource-to-lockout step — all automatic"],
  "knowledge": ["the loop's propagation from a hazard event to the credibility metric implicitly requires the hazard to be observable/attributable by outside parties, so at least one step depends on the hazard being visible to whichever party's credibility metric it feeds"],
  "ends_when": "UNCLEAR — the source names no terminating condition for the loop itself; it only names where the loop LEADS (a separate case's own terminal state), and that case's own exit path is, per the need above, of unclear simultaneous satisfiability once the loop has progressed far enough to trigger it."
})

# ---------------- SCN-LOOP-B ----------------
cases.append({
  "id": "SCN-LOOP-B",
  "name": "One institution's rise removes the counter-pressure against it",
  "one_line": "A rising suspicion metric triggers an institutional response that further raises the same metric, while punishing a rival institution strips the very counter-options that could push back, ending only in an unconditional invasion.",
  "scale": "realm",
  "season_requires": [
    N("The loop's own START condition must be gated on a DIFFERENT clock's state as a prerequisite — this metric's threshold-crossing effect must only be active while a SEPARATE clock is below its own separate threshold, meaning the loop can be interrupted or never begin purely by that second clock's value, without any action targeting the metric itself.",
      "Without the cross-clock start-gate, the loop's onset would be independent of the world-health state the source ties it to.", "important"),
    N("A rising metric crossing one threshold must trigger an institution offering a 'mediation' action whose EFFECT is to further increase the SAME metric that triggered it — the institution's own response to the metric's rise must be a net contributor to that same rise, not a mitigation.",
      "If the offered mediation reduced the metric instead of raising it further, the loop's described self-reinforcing character would not exist.", "core"),
    N("One institution's resource crossing a threshold must unlock a PUNITIVE capability specifically targeting members of a SEPARATE, rival institution, and the punitive action's effect on those targeted members must reduce the rival institution's OWN separate resource.",
      "Without the cross-institution punitive mechanic, one institution's rise could not mechanically diminish a rival's standing.", "important"),
    N("A rival institution's resource, once reduced by the above, must REMOVE a class of counter-actions that would otherwise have been available against the ORIGINAL rising metric — damage to one institution's standing must shrink the total space of actions ANY actor could use to push back on an unrelated tracked value, not just actions belonging to the damaged institution.",
      "Without this removal of counter-options, the loop's described self-worsening property (the rival's weakening removes 'anti-CI options' generally) would collapse into a merely local effect on the rival alone.", "core"),
    N("The same metric crossing a SECOND, higher threshold must simultaneously trigger a further rate increase on a THIRD clock and start a distinct, separately-tracked preparation/documentation process attributable to one named external actor, both firing off the same single threshold-crossing event.",
      "A single effect instead of two simultaneous ones from the same crossing would understate the described compounding of consequences at the higher threshold.", "important"),
    N("A separate clock reaching a sufficiently high value must remove an internal MODERATING presence within a fourth, otherwise-external institution, where that moderating presence's disappearance is described as removing the 'primary brake' — an institution's OWN internal composition must be representable as containing a counter-pressure sub-faction whose continued existence depends on an external clock staying below a threshold.",
      "Without a representable internal moderating sub-faction, the described collapse of the external institution's own internal restraint could not occur.", "important"),
    N("UNCLEAR: the loop's own chain, as described end to end, names no point at which any of its four moving parts (the original metric, the second clock, either institution's own resource) reverses or is reversible from within the loop's own steps — every named consequence pushes in the same direction, and the loop terminates only in an unconditional invasion event at the third clock's cap, not in a resolution.",
      "If nothing within the loop's own described steps can reverse it, and generic decrease paths for the driving clock are named only elsewhere for a different scenario and never invoked by this loop's own text, it is unclear whether this specific chain, once started, can be interrupted at all.", "important")
  ],
  "temporal": {
    "span_seasons": "ongoing, multi-season",
    "needs_memory_of": "the credibility metric's value; the world-health clock's value, as start-gate; the external-pressure clock; both institutions' resource values; whether the moderating sub-faction is currently intact.",
    "needs_deadline": "no fixed date, but the terminal invasion event is an unconditional cap-triggered event once the external-pressure clock reaches its maximum"
  },
  "who_acts": ["the mediating institution (chooses to offer mediation, though framed as near-automatic once the threshold is crossed)", "the punitive institution (chooses to act on excommunication threats)", "the named external individual/institution (chooses to begin documentation)", "nobody decides any of the threshold crossings themselves"],
  "knowledge": ["not primarily epistemic within the loop's own text"],
  "ends_when": "UNCLEAR — the source names no reversal or exit condition anywhere within the loop's own description; it concludes only in an unconditional cap-triggered invasion event (a threshold-fires outcome), and the closest thing to a counter-mechanism (generic decrease paths for the driving clock, named elsewhere in the document for a different scenario) is never referenced by this loop's own text, so whether it can interrupt this specific chain once already in progress is itself unclear."
})

# ---------------- SCN-LOOP-C ----------------
cases.append({
  "id": "SCN-LOOP-C",
  "name": "A practitioner's degrading stability erodes the relationship that could save it",
  "one_line": "One resource's own degradation makes the actions that degrade it more likely to fail further, while spreading strain to a bonded second character whose own strain removes one of the resource's two recovery paths.",
  "scale": "person",
  "season_requires": [
    N("A specific costly sub-action's use must GUARANTEE a fixed loss to an individual resource as a direct, certain cost, distinct from the SAME resource's other loss sources which are roll-gated.",
      "A roll-gated-only loss instead of a guaranteed one would remove the described certainty of this specific sub-action's toll, distinguishing it from the resource's other, chancier loss sources.", "important"),
    N("The resource crossing a specific band must impose a difficulty penalty specifically on THE SAME ACTION CATEGORY that spends it (including the specific sub-action that started this chain), creating a loop where the resource's own degradation makes the actions that degrade it further MORE likely to trigger their own worse outcomes.",
      "Without the self-targeting difficulty penalty, there would be no mechanical loop at all — merely a resource dropping over time from unrelated causes.", "core"),
    N("The resource's degradation must be able to propagate OUT of the acting character entirely, imposing an accruing strain cost on a bonded SECOND character's own separate relational resource, on a fixed recurring interval, purely as a consequence of the first character's resource band.",
      "Without cross-character propagation, the loop would remain entirely self-contained to one character and could not threaten the bonded relationship the source describes as being eroded.", "core"),
    N("That second character's relational resource, once sufficiently strained, must REMOVE the first character's access to one of their own resource's named recovery paths (the one depending on that bonded relationship being intact) — damage to a RELATIONSHIP resource must be able to gate access to an otherwise-unrelated PERSONAL resource's own recovery mechanic.",
      "Without this cross-resource gating, the bonded relationship's own strain would have no mechanical bearing on the degrading character's ability to recover, contradicting the described 'no Anchoring Scenes possible if Knots broken.'", "core"),
    N("UNCLEAR: the loop's own narration states 'No Coherence recovery path' once the relational-support recovery path is gone, but the underlying resource (established elsewhere) names a SECOND, independent recovery path (full-season abstention from the triggering action) that nothing in this loop's own chain explicitly removes or blocks — the source does not resolve whether that second path remains genuinely available once the loop has progressed this far.",
      "If the abstention path genuinely remains available, the loop's own stated conclusion ('no recovery path') is an overstatement the source itself does not reconcile with the resource's own separately-defined two-path recovery rule.", "important"),
    N("Reaching the resource's absolute floor must trigger a distinct, campaign-level consequence changing the character's ownership/control status, firing as the ENDPOINT the entire cascading loop was building toward.",
      "Without a defined terminal consequence at the floor, the cascade would have no concrete endpoint distinguishing it from an indefinitely worsening but never-concluding decline.", "core")
  ],
  "temporal": {
    "span_seasons": "ongoing, can complete within or across seasons",
    "needs_memory_of": "the practitioner's resource value and current band; the bonded second character's own relational-strain value; whether the paired-scene recovery path is currently accessible.",
    "needs_deadline": "no fixed date; the floor-triggered ownership-status change is itself the terminal event, not seasonal"
  },
  "who_acts": ["the practitioner (chooses to use the costly sub-action, the initiating step)", "nobody decides any subsequent step in the chain (the retention roll failing, the band crossing, the relational strain accruing, the recovery-path removal, or the floor-triggered conversion) — all automatic once the first choice is made"],
  "knowledge": ["not primarily epistemic"],
  "ends_when": "UNCLEAR — the loop's own chain names the terminal state it produces (an ownership-status conversion) but names no point at which the cascade itself can be interrupted or reversed from within its own steps; per the need above, whether the resource's OTHER, independently-established recovery path remains usable partway through this specific cascade is left unresolved by the source."
})

# ---------------- SCN-LOOP-D ----------------
cases.append({
  "id": "SCN-LOOP-D",
  "name": "A destabilizing world-state opens a window that its own consequences can close",
  "one_line": "A rising world-condition metric that is harmful elsewhere is also what unlocks new practitioner access, and the one group positioned to close the window deliberately can lose that ability to the instability the window itself generates.",
  "scale": "realm",
  "season_requires": [
    N("A shared world-condition metric's own RISE (framed elsewhere as destabilizing/negative) must be able to be the SAME event that OPENS a capability gate, making a previously-unavailable action type newly available to characters who could not use it below the threshold — the same metric must carry both a negative framing in other consequences and a positive-unlock framing in this one, simultaneously.",
      "If the metric could only ever be framed as harmful, the described double-edged nature of the window — bad for stability, good for access — could not be represented as arising from the SAME value.", "core"),
    N("A character becoming newly eligible for the gated action must be trackable per-character (a durable 'was this character below or above the threshold when it opened' or equivalent), not merely as a global on/off switch, since the text specifies 'previously dormant' characters specifically becoming able to act.",
      "A purely global switch instead of per-character eligibility tracking would be unable to distinguish characters who were already capable from those newly unlocked by this specific event.", "important"),
    N("The newly-eligible characters' USE of the unlocked action must be OBSERVABLE by an external institution as a distinct triggering event, feeding a rise in that institution's own suspicion/credibility metric, separate from and in addition to any other trigger of that same metric.",
      "Without observability as a distinct trigger, the newly-visible practitioners could not feed the described rise in outside suspicion.", "important"),
    N("A specific group's OWN deliberate, dedicated action must be able to REDUCE the SAME originating metric that opened the access window, and that action's SUCCESS must be the loop's one explicitly-intentional counter-mechanism, distinct from any of the loop's other, automatic steps.",
      "Without a named deliberate counter-action, the loop would have no player-controllable off-switch at all, contradicting the source's explicit framing of this as the loop's stated counter.", "core"),
    N("That SAME specific group's own separate institutional-standing resource must be able to be DRIVEN DOWN by the very factional instability that this loop's own automatic steps generate, creating a path by which the loop damages the standing of the one actor positioned to stop it.",
      "Without this causal path, the loop's self-undermining property — its own progression harming its own cure — could not exist.", "core"),
    N("That group's institutional-standing resource crossing its OWN floor must strip the group's access to its one counter-action specifically, at the same time as (or as a consequence of) the instability that the loop's own progression produced — the disabling condition and the loop's own automatic progression must share a common cause.",
      "Without a shared cause linking the standing collapse to the loop's own progression, the disabling of the counter-action would read as coincidental rather than as the loop actively defeating its own antidote.", "core"),
    N("UNCLEAR: the source states the access window 'closes precisely when it's needed most' but does not specify the actual closing MECHANISM — whether the originating metric falls back below the access threshold automatically (and by what rule, since no decay/reduction source for that metric is named elsewhere in this specific chain), or whether 'closing' refers only to the counter-group's action becoming unavailable while ordinary-character eligibility remains open.",
      "The two readings imply different game states (everyone loses access vs. only the counter-group loses its cure while others can still act), and the source does not say which is meant.", "important")
  ],
  "temporal": {
    "span_seasons": "ongoing",
    "needs_memory_of": "the originating metric's value, to know if access is open; per-character eligibility state; the specific group's institutional-standing value, to know if its counter-action is currently available.",
    "needs_deadline": "no fixed date, but functionally yes — the window is explicitly stated as capable of closing on its own"
  },
  "who_acts": ["newly-eligible characters (choose whether to act, now that access is open)", "the specific group's leadership (chooses whether to attempt the counter-action, when able)", "nobody decides the metric's own rise, the observability-driven credibility increase, the factional-instability propagation, or the standing-resource threshold strip — all four automatic"],
  "knowledge": ["the newly-unlocked action's use must be perceivable by the external institution as a condition of the credibility-rise step — a genuine epistemic gate, the institution must be able to perceive that the previously-dormant capability is now being exercised"],
  "ends_when": "the specific group succeeds at its counter-action before its own standing collapses, reversing the metric and holding the window open — or its standing collapses first (a threshold firing, nobody deciding), closing the counter-path and leaving the underlying destabilization to continue via the loop's other, automatic effects — or, per the UNCLEAR need above, it is not fully specified whether 'the window closing' additionally means ordinary access reversing on its own."
})

with open("/tmp/claude-0/-home-user-ttrpg/e2c0050d-067c-5d41-a0c2-ee97ae491748/scratchpad/part5.json", "w") as f:
    json.dump(cases, f)
print(len(cases), "cases in part 5")
