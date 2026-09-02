import json

cases = []

def N(need, why, hardness):
    return {"need": need, "why": why, "hardness": hardness}

# ---------------- SCN-10 ----------------
cases.append({
  "id": "SCN-10",
  "name": "An entity whose existence is itself a sustained action",
  "one_line": "An NPC-type whose perceptibility varies continuously by observer stat, who pays a different resource for wounds than ordinary characters, and whose destabilization runs a fixed escalating countdown with its own hazard side effect.",
  "scale": "person",
  "season_requires": [
    N("An NPC-type entity's perceptibility must vary continuously across at least five distinct bands depending on the OBSERVING character's own stat value, not a single global visibility flag — the same entity must be renderable as 'nothing' to one observer and 'fully detailed' to another, simultaneously, in the same scene.",
      "A single shared visibility state instead of per-observer perception would erase the described gradient where a low-stat bystander and a high-stat practitioner experience the same entity completely differently.", "core"),
    N("This entity type must be able to perform an enhanced version of its base passive effect at a PER-SCENE recurring cost to one of its own resources, distinct from any action-based cost.",
      "Without a scene-scoped ongoing cost, the entity's 'work' of sustaining an enhanced presence would be free.", "important"),
    N("This entity type must be able to perform the same outward-facing action category as ordinary characters while being EXEMPT from a prerequisite step ordinary characters must pass through first, because it structurally already satisfies the state that step exists to establish.",
      "Requiring the normal prerequisite would contradict the entity's described always-already-actualized nature.", "important"),
    N("Taking a wound must cost this entity type a DIFFERENT resource entirely (additional required ongoing effort) rather than the standard dice-pool penalty every other character type takes — the wound-cost resolution path itself must be swappable per character-type.",
      "A single universal wound-consequence would be unable to represent this entity's wounds as a drain on its ongoing sustaining effort rather than on combat effectiveness.", "core"),
    N("A single terminal-sequence trigger must fire from EITHER of two independent conditions (a resource reaching its cap, OR a separate counter reaching a threshold derived from dividing a different stat by two) — an OR-gate between two conditions of entirely different shape.",
      "An AND-gate, or only one trigger path, would misrepresent the described 'either of these independently' rule.", "core"),
    N("Once triggered, the terminal sequence must run as a fixed multi-round countdown where each round applies a qualitatively different, escalating effect, and each round must independently offer its own stabilization roll that can arrest the countdown at that round.",
      "A single all-at-once terminal roll instead of a multi-round countdown with independent stabilization attempts would remove the described tension of a slow, resistible unraveling.", "core"),
    N("The countdown's final round must produce an UNCONDITIONAL terminal outcome with no stabilization roll offered, that ALSO spawns, as a side effect, the SAME hazard-event type used by an entirely different scenario chain.",
      "Without the cross-case hazard spawn, the entity's final unraveling would be isolated from the rest of the world's hazard economy, contradicting the described consequence.", "important"),
    N("A specific targeted hostile action-subtype, when targeting this entity-type specifically, must bypass its normal roll-based outcome table entirely and auto-produce the worst-case consequence unconditionally, because the target structurally lacks a property that action's normal resolution depends on.",
      "Without the auto-produced bypass, this entity would be treated identically to an ordinary target for that action, contradicting its described lack of an accumulated past.", "important"),
    N("The entity's controlling actor must be able to voluntarily choose to end the entity's existence through a distinct action that SKIPS the difficulty penalties the involuntary terminal sequence normally imposes.",
      "Without a cheaper deliberate-ending path, there would be no mechanical difference between choosing to end the entity and being forced to, contradicting the described 'Choice.'", "important")
  ],
  "temporal": {
    "span_seasons": "n/a within a scene for the countdown; the entity's overall existence spans indefinite seasons",
    "needs_memory_of": "the entity's current resource value and wound count, for the OR-gated trigger; which round of the countdown is active, if triggered.",
    "needs_deadline": "yes, once triggered — the countdown resolves within 3 rounds regardless of intervention"
  },
  "who_acts": ["the entity itself (chooses to render beyond-ceiling, to act outward, to attempt stabilization each round, or to voluntarily end itself)", "an opposing character (chooses the targeted hostile action that bypasses the roll)", "observers (their own stat determines what they perceive, not a choice)"],
  "knowledge": ["perceptibility is fundamentally epistemic — different observers hold different true perceptions of the same entity simultaneously, gated purely by the observer's own stat, with no single ground truth visible to all"],
  "ends_when": "mixed — a person chooses (voluntary cessation) for one path; a roll resolves it if a stabilization attempt in rounds 1-2 succeeds; a threshold-fires (no roll offered) for the unconditional round-3 terminus."
})

# ---------------- SCN-11 ----------------
cases.append({
  "id": "SCN-11",
  "name": "An external pressure clock accrues from many sources toward invasion",
  "one_line": "One clock fed by at least five independent trigger sources escalates through named bands with distinct one-time and ongoing effects, cappable only via three structurally different decrease paths.",
  "scale": "realm",
  "season_requires": [
    N("A single clock must accrue from at least five independent, structurally different trigger sources simultaneously in the same season: a per-observed-event trigger, a fixed jump tied to a DIFFERENT case's own delay condition exceeding a count, and multiple separate cross-clock feeds keyed to two other clocks' own threshold states.",
      "Fewer independent sources would understate the described convergence of unrelated systems all pushing the same clock at once.", "core"),
    N("Crossing INTO a specific band of the clock must fire a ONE-TIME, uniquely-named demand event distinct from that band's ongoing ambient effects, which creates a standing obligation with its own resolution cost feeding back into TWO SEPARATE clocks at once when left unresolved.",
      "Without a distinct one-time entry event, the demand's own escalating feedback into two other clocks would be indistinguishable from the band's regular ambient effects.", "important"),
    N("A higher band must activate an internal multi-part structure within the opposing side (multiple named internal sub-factions) that can each apply pressure independently against different targets, with a named counter-requirement (unity on the receiving side) needed to resist them as a bloc.",
      "Without the multi-actor pressure and its unity counter-requirement, the described vulnerability of a divided response could not be represented.", "important"),
    N("A still-higher band must remove an internal MODERATING presence on the opposing side, described as that side's primary internal brake, as an automatic consequence of the clock's own value crossing that band.",
      "Without automatic removal of the internal moderate, the clock's approach to its cap would lack the described acceleration once the last restraint disappears.", "important"),
    N("The clock's maximum value must trigger an unconditional, irreversible campaign-defining event with no roll or further condition once reached.",
      "A conditional or roll-gated cap event instead of an unconditional one would contradict the described inevitability of reaching the maximum.", "core"),
    N("At least three structurally different decrease paths must exist for the same clock: one that only pauses its drift for a fixed single-season duration without reducing its value, one that permanently reduces its value at a fixed rate while removing a moderating structure's political cover as a side cost, and one that is a single decisive scene gated behind a compound prerequisite combining a faction-dominance condition, a minimum value on one institutional resource, and a minimum value on the shared world-health currency, all three at once.",
      "A single generic decrease path instead of three structurally distinct ones would erase the described trade-offs between a temporary pause, a costly permanent reduction, and a hard-to-reach decisive resolution.", "core"),
    N("That compound-prerequisite decisive scene, if won, must both FREEZE the clock's further movement AND unlock access to an entirely separate resolution mechanism not otherwise available.",
      "Without unlocking a distinct resolution mechanism, winning the decisive scene would only pause the clock rather than opening the described peace-treaty path.", "important")
  ],
  "temporal": {
    "span_seasons": "ongoing",
    "needs_memory_of": "the clock's current value and band; whether the one-time demand event has already fired; the delay-count for the cross-referenced succession case.",
    "needs_deadline": "yes for the one-time demand event's own obligation window; the clock's cap is an unconditional endpoint with no fixed date but is reachable"
  },
  "who_acts": ["the observing opposing agents (trigger the per-event feed)", "the receiving institution (chooses how to respond to the demand, and whether to pursue a decrease path)", "the opposing side's internal sub-factions (choose whether to apply pressure)", "nobody decides the automatic cross-clock feeds or the band-crossing removal of the moderating presence"],
  "knowledge": ["the per-event trigger requires the triggering action to be OBSERVED by the opposing agents specifically — a genuine visibility gate distinct from the action simply occurring"],
  "ends_when": "mixed — the clock's cap is threshold-fires and unconditional; the decisive peace-scene path is a roll conditional on the compound prerequisite; the pause and permanent-reduction paths are both person-chooses."
})

# ---------------- SCN-12 ----------------
cases.append({
  "id": "SCN-12",
  "name": "A succession crisis branches into distinct resolution paths",
  "one_line": "A single succession decision offers several structurally different resolution paths, one of which trades an immediate outcome for a deferred, unresolved-timing complication, and a coup path cross-referencing a different case's own fracture condition.",
  "scale": "faction",
  "season_requires": [
    N("A single succession decision must present multiple, mutually exclusive named resolution paths (at minimum four: accept an external demand, install one of several named heirs, resolve via a formal contested vote, or a coup), each with its own independent consequence chain rather than a single unified roll.",
      "A single roll instead of several structurally distinct paths would erase the described branching where each path has qualitatively different downstream consequences.", "core"),
    N("One resolution path must trade an immediate, present-tense benefit for a DEFERRED consequence explicitly recorded as 'seeded' now but whose actual resolution/payoff is left for an unspecified LATER point in the campaign.",
      "Without a genuine deferred-consequence mechanic, 'a future complication seeded' could not be distinguished from an ordinary immediate effect.", "core"),
    N("The REFUSAL branch of that same choice must impose both an IMMEDIATE unconditional cost and a SEPARATE, CONDITIONAL additional cost that only applies if a different, otherwise-unrelated clock is currently within a specific band at the moment of the choice.",
      "Without the conditional additional cost, refusing would carry the same fixed price regardless of the wider world's state, contradicting the described cross-clock contingency.", "important"),
    N("At least one contender-path's outcome must be able to retroactively trigger an entirely SEPARATE scenario chain as a direct consequence, plus independently increase a specific evidentiary/credibility-tracking resource, both from the same single triggering event.",
      "Without the dual trigger, a heir's Thread-sensitivity being revealed would only feed one downstream system instead of the described two.", "important"),
    N("Individual NAMED characters must be able to carry succession-relevant state/flags that this rule chain references but does not itself fully resolve, deferring their resolution to a separate, character-specific record.",
      "Without deferrable, per-NPC-authored resolution paths, the document's own explicit cross-reference to a separate character record would have nothing to point at.", "important"),
    N("A formal multi-exchange contested resolution must be able to have its EFFECTIVE DIFFICULTY reduced by a THIRD PARTY's support, invoked via a specific named appeal-category, distinct from either principal party's own roll.",
      "Without third-party difficulty modification, an ally's support for one succession claimant would have no mechanical effect on the outcome.", "important"),
    N("A coup-availability condition must be gated behind a DIFFERENT institution's own internal resource crossing its zero/floor value, cross-referencing the SAME structural-fracture condition used elsewhere in a wholly different case, rather than the coup having its own independent trigger logic.",
      "A coup path with its own independent trigger instead of reusing the cross-case fracture condition would duplicate logic the source explicitly reuses.", "core"),
    N("Individual NAMED characters must be able to carry a bespoke, individually-authored CONDITIONAL BONUS to a specific roll, activating only once a SHARED, GLOBAL world-state value crosses a specific low band.",
      "Without per-character custom rules keyed to global clock state, the described coup-trigger NPCs whose odds improve specifically as the world destabilizes could not be represented.", "important"),
    N("A repeatable, once-per-season action restricted to exactly one specific actor/role must have a success/failure branch where failure costs that actor's OWN resource, and must independently accumulate an escalating difficulty tax on its OWN future uses purely from consecutive-season repetition, decoupled from whether prior uses succeeded or failed.",
      "Without a repetition-triggered (not outcome-triggered) tax, the described 'decree fatigue' penalty for repeated use regardless of success could not be distinguished from an ordinary failure penalty.", "important")
  ],
  "temporal": {
    "span_seasons": "ongoing, resolves over multiple seasons depending on path chosen",
    "needs_memory_of": "which succession path, if any, has been committed to; the deferred-complication flag from the accept-demand path, with no resolution timer named; the consecutive-use count for the unique institutional action.",
    "needs_deadline": "UNCLEAR for most paths — no explicit deadline is stated for when succession must resolve, only that a delay itself (exceeding two campaign arcs) is a tracked trigger feeding a different clock."
  },
  "who_acts": ["the Crown/succession-holder (chooses accept/refuse)", "each named contender (their own path's events occur, some via roll, some via authored NPC-specific content)", "a third-party supporter (chooses to lend an appeal)", "a coup-attempting faction (chooses to act, if eligible)", "the unique institutional actor (chooses whether to use their once-per-season action)"],
  "knowledge": ["not primarily epistemic, though a contender's Thread-sensitivity becoming known is explicitly a knowledge-state change feeding a credibility/evidence resource"],
  "ends_when": "mixed across paths — person-chooses for the accept/refuse fork and the coup attempt; a roll resolves it for the contested vote and the unique institutional action; the deferred-complication branch's own resolution timing is UNCLEAR — the source names no point at which it comes due."
})

with open("/tmp/claude-0/-home-user-ttrpg/e2c0050d-067c-5d41-a0c2-ee97ae491748/scratchpad/part3.json", "w") as f:
    json.dump(cases, f)
print(len(cases), "cases in part 3")
