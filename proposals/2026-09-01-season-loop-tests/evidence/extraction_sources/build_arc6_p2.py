import json

cases = []

def N(need, why, hardness):
    return {"need": need, "why": why, "hardness": hardness}

# ---------------- SCN-06 ----------------
cases.append({
  "id": "SCN-06",
  "name": "A hazard-event forms and drains the world",
  "one_line": "Multiple unrelated failure conditions converge on spawning the same hazard type, whose severity reads off a shared currency's value at the moment of spawning and which then drains that currency automatically every season it goes unresolved.",
  "scale": "realm",
  "season_requires": [
    N("At least four different failure conditions belonging to OTHER, unrelated action-resolution chains must all be able to converge on spawning the same category of persistent hazard-event, i.e. the hazard-spawning logic cannot be owned by only one of those chains.",
      "If only one action's failure could spawn this hazard, the described convergence from several unrelated action types onto one shared hazard state could not happen.", "core"),
    N("The severity tier of a newly-spawned hazard must be determined by reading a shared currency's CURRENT value at the exact moment of spawning, across at least four severity bands, where the top band spawns the hazard simultaneously across multiple adjacent locations rather than the one location of origin.",
      "A fixed severity independent of the currency's value would erase the described worst-case where a single failure can seed an entire region at once.", "core"),
    N("A lesser precursor stage of the hazard must be resolvable away via a dedicated action, gated by a minimum resource-level requirement on the acting character, before it is allowed to escalate into the full hazard.",
      "Without a precursor stage and its own closing window, every hazard-triggering failure would jump straight to the full, harder-to-resolve state.", "important"),
    N("An unresolved instance of the full hazard must impose an automatic, unconditional recurring cost on the shared currency every season it remains unresolved, with no actor choosing this.",
      "Without automatic ongoing drain, leaving a hazard unresolved would carry no escalating cost, removing the pressure to address it.", "core"),
    N("The difficulty of the dedicated resolution action against a given hazard instance must increase in discrete steps tied to how many consecutive seasons that specific instance has remained unresolved, distinct from the hazard's original severity tier.",
      "Without escalating difficulty over time, an old, neglected hazard would be no harder to fix than a freshly-formed one.", "important"),
    N("The resolution action's own outcome table must have BOTH of its two success-tier branches still cost the shared currency in some form, such that a 'successful' resolution is not guaranteed to be a net positive for every tracked resource.",
      "Without a cost attached even to success, resolving a hazard would be a pure win with no trade-off, contradicting the described net loss on the lesser success branch.", "important"),
    N("One specific success-tier branch of the resolution action must impose a localized, season-long increased difficulty on future attempts to spawn or resolve the same hazard type in the same location.",
      "Without this aftereffect, an overwhelming resolution would leave no trace distinguishing it from an ordinary success.", "flavour"),
    N("A hazard instance's mere existence must feed a SEPARATE public-facing metric, but only conditionally — gated on whether the shared currency is currently below a named threshold at the time, not unconditionally on the hazard's existence alone.",
      "An unconditional feed would make the hazard always visible to the same degree regardless of the wider world's state, losing the described context-dependent framing.", "important"),
    N("The system must be able to sum multiple independent per-season drain sources on the same shared currency into one combined seasonal total, and compare that total against the best available restoration action's typical output, as a first-class computable relationship, to determine whether the currency is on a terminal, unrecoverable trajectory.",
      "Without a computable combined-drain-vs-restoration comparison, 'this cannot be recovered from at this rate' would be an unverifiable narrative claim rather than a checkable game state.", "core")
  ],
  "temporal": {
    "span_seasons": "ongoing until resolved",
    "needs_memory_of": "which hazard instances exist, their severity tier, how many consecutive unresolved seasons each has accrued, and the shared currency's value at each accounting step.",
    "needs_deadline": "no fixed date, but functionally yes — unresolved instances get objectively harder to fix the longer they persist"
  },
  "who_acts": ["the practitioner/group attempting resolution (chooses whether and how to attempt it)", "nobody decides the spawning or the per-season drain — both automatic"],
  "knowledge": ["not primarily epistemic; whether outside observers 'read' the hazard a particular way is gated on the shared currency's threshold state, a form of externally-visible framing rather than hidden information changing hands"],
  "ends_when": "mixed — a roll resolves an individual hazard instance's resolution attempt, but its escalation and per-season drain are threshold-fires with nobody deciding."
})

# ---------------- SCN-07 ----------------
cases.append({
  "id": "SCN-07",
  "name": "An individual practitioner's stability degrades in bands",
  "one_line": "A personal resource with no passive recovery degrades from several sources into ordered bands with qualitatively different penalties, terminating at a bottom band that converts the character away from player control if unresolved.",
  "scale": "person",
  "season_requires": [
    N("A per-character resource must start at a fixed ceiling and be reducible from at least three independently-triggered sources: the failure branch of an unrelated roll, an automatic penalty attached to one specific action type regardless of outcome, and a difficulty increase on a DIFFERENT future roll that itself raises that future roll's own chance of causing further reduction.",
      "Without the third source, the described feedback loop where degrading the resource makes further degradation more likely could not exist.", "core"),
    N("The resource must have NO passive or automatic recovery of any kind — every increase must trace to a deliberate, named action taken by a character.",
      "Passive recovery would undercut the described irreversibility that drives the rest of the chain's tension.", "core"),
    N("The resource's current value must be divisible into at least five ordered bands where the mechanical consequences differ in KIND between bands, including at least one band whose penalty is expressed as an accruing stress cost to a DIFFERENT character's relationship-resource on a fixed time interval.",
      "Uniform scaling instead of kind-differentiated bands would erase the described qualitative shifts (narrative flicker vs. dissociation vs. belief co-authorship) between bands.", "core"),
    N("At least two of the lowest bands must each trigger a ONE-TIME random-outcome check specifically on the transition INTO that band, distinct from that band's ongoing penalties.",
      "Without a one-time transition check, entering and remaining in a band would be mechanically identical to merely passing through it.", "important"),
    N("The lowest defined value (0) must be a distinct terminal state requiring deliberate narrative resolution by the acting player, with an explicit default consequence (the character's ownership status changing) if unresolved by a fixed cutoff (the end of the current season).",
      "Without a hard default consequence, hitting the floor would have no forcing function and could be left unresolved indefinitely.", "core"),
    N("Recovery must be restricted to exactly two paths: full abstention from the specific triggering action-type across an entire season, and a paired two-character scene gated behind its own roll, which itself costs a resource belonging to the SECOND character.",
      "If helping someone recover cost the helper nothing, the described relational stake in another character's degradation would be missing.", "important"),
    N("The resource must be hard-capped at its starting ceiling and categorically unpurchasable by the general advancement currency that buys other character improvements.",
      "If the resource could be bought up like a stat, its described status as an unrecoverable-by-normal-means resource would be false.", "important")
  ],
  "temporal": {
    "span_seasons": "ongoing",
    "needs_memory_of": "the resource's current value; which band the character currently occupies, to detect a new transition into a band vs. remaining in one; whether the current season has had zero uses of the triggering action type.",
    "needs_deadline": "yes — the bottom-band default consequence fires specifically at season end if unresolved"
  },
  "who_acts": ["the practitioner (chooses whether to use the triggering action, whether to attempt narrative resolution at the bottom band, whether to abstain for recovery)", "a bonded second character (chooses to spend the paired recovery scene, at their own cost)", "GM/system (fires the automatic degradation sources and the band-transition checks)"],
  "knowledge": ["not primarily epistemic; other characters may perceive the degrading character differently as bands worsen, but this is not gated on hidden information changing hands"],
  "ends_when": "UNCLEAR — the resource itself has no terminal 'ends' as such; each individual descent to the bottom band ends either by a person choosing a narrative resolution, or absent one, by a threshold-fires default (ownership-status conversion) at season end."
})

# ---------------- SCN-08 ----------------
cases.append({
  "id": "SCN-08",
  "name": "Three world clocks cross-feed each other",
  "one_line": "Three parallel numeric clocks each rate-modify one another across tiered thresholds, compound when several are past threshold at once, and trigger a named campaign phase when all three pass their midpoints together.",
  "scale": "realm",
  "season_requires": [
    N("At least three independent numeric clocks must run in parallel, each with a distinct starting value and valid range/direction, with one clock's threshold-crossing changing ANOTHER clock's per-season accrual RATE going forward, not merely triggering a one-time effect.",
      "A one-time-only cross-clock effect instead of a rate change would erase the described compounding acceleration once a threshold is crossed.", "core"),
    N("A single clock must have at least two ordered threshold levels, where crossing the second (more extreme) threshold REPLACES the rate-effect from the first threshold rather than stacking additively with it.",
      "Additive stacking instead of replacement would produce a different, faster-runaway numeric outcome than the source's explicit 'total, replaces the +1' rule.", "important"),
    N("A clock crossing a threshold must introduce an ongoing per-season CHANCE of spawning a hazard instance belonging to an entirely different case-chain, at a location selected by querying which specific location currently holds the WORST value of a third, otherwise-unrelated tracked per-location stat.",
      "Without cross-referencing the worst-off location on an unrelated stat, hazard placement would have to be random or fixed rather than targeting the world's weakest point as described.", "core"),
    N("When two specific clocks are BOTH simultaneously past their own named thresholds at once, the system must support a distinct COMPOUND effect (both accelerating to a maximum rate) that is not simply the sum of their two individual threshold effects.",
      "A merely additive combination instead of an explicit compound-to-maximum rule would understate the described 'fast path to dual campaign events.'", "important"),
    N("When ALL of a fixed set of clocks are simultaneously past a shared reference point (their midpoints) at once, this combined condition must trigger a discrete, named CAMPAIGN-WIDE PHASE CHANGE distinct from any single clock's own threshold effects.",
      "Without a distinct combined-condition trigger, there would be no way to represent the endgame phase as something more than 'all three clocks happen to be high.'", "core"),
    N("Each clock must independently support at least three ordered bands that each activate or deactivate an entirely different RULE-SET while active, not a single numeric penalty scaling smoothly.",
      "Smooth scaling instead of qualitatively different rule-sets per band would erase the described mix of pure random-hazard risk, flat difficulty tax, and new recurring institutional checks appearing at different bands.", "core"),
    N("Multiple distinct, named institutions must each hold their OWN bespoke recurring action whose mechanical effect is to move one or more of the shared clocks, i.e. the clocks must be modifiable from many different actor-specific action definitions, not just from automatic threshold-driven sources.",
      "Without actor-specific clock-moving actions, players/factions would have no deliberate lever on the clocks at all, only passive automatic drift.", "important"),
    N("At least one faction-specific clock-moving action must be SELF-UNDERMINING: its own use moves a shared clock in the faction's favor, while a SEPARATE tracked value belonging to that same faction, on crossing its own threshold at its zero/minimum, strips the faction's access to that very action going forward.",
      "Without this self-undermining property, the described irony of a faction losing access to its own best lever exactly when needed could not be represented.", "important")
  ],
  "temporal": {
    "span_seasons": "ongoing",
    "needs_memory_of": "the current value of all three clocks; the current band/threshold state per clock, to detect transitions; per-faction tracked values gating faction-specific actions.",
    "needs_deadline": "no fixed date"
  },
  "who_acts": ["named factions/institutions (each choosing whether to use their own clock-moving action each season)", "nobody decides the automatic threshold-crossing rate changes and random hazard rolls"],
  "knowledge": ["not primarily epistemic"],
  "ends_when": "threshold-fires — all the clock-rate changes and the endgame-phase trigger are pure comparisons nobody decides, though individual faction actions that move the clocks are person-chooses."
})

# ---------------- SCN-09 ----------------
cases.append({
  "id": "SCN-09",
  "name": "The terminal decline of the world-health currency",
  "one_line": "Once the shared currency enters its lowest band, several automatic drains stack faster than the best restoration action can offset, and escaping requires four structural conditions to hold at once — one of which is internally in tension with the drains that got the currency here.",
  "scale": "realm",
  "season_requires": [
    N("A shared currency's lowest band must activate SEVERAL simultaneous, independently-summed automatic per-season drains (at minimum: a per-hazard-instance drain, a per-locked-instance drain, a flat passive drain, and a chance-based new-hazard-spawn check), all computed together at the same seasonal accounting step.",
      "Summing only one drain source instead of several would understate the described 'combined −6 to −10+/season' compounding decline.", "core"),
    N("A SEPARATE per-season institutional check, independent of the currency's own drains, must run in the same band, with an ordinary failure reducing an institutional resource and — specifically once that resource reaches its own floor — a distinct, more severe failure consequence (a structural split of the institution).",
      "Without a second, escalating failure tier at the institutional resource's floor, faction fracture would have no distinct trigger from ordinary Mandate loss.", "important"),
    N("The single restorative action's own success probability at this band's difficulty must be representable as an explicit RANGE varying with pool size, and the system must be able to state/compute that even the best-case typical seasonal outcome with active restoration is still net-negative for the currency.",
      "Without a computable net-negative comparison, the described hopelessness of the terminal band would be unverifiable narrative color rather than a checkable game fact.", "important"),
    N("Exiting this band's terminal spiral must require satisfying MULTIPLE (here: four) named structural conditions simultaneously — the system must support AND-gating a scenario resolution behind a checklist of conditions belonging to different subsystems, not any single roll or threshold.",
      "A single-roll or single-threshold exit instead of an AND-gated checklist would trivialize what the source frames as a structural, multi-part escape.", "core"),
    N("One of those structural exit conditions must itself be a COMPOUND action: multiple separate actors pooling their individual capability into one shared attempt, with an explicit rule for what happens when two contributing actors hold conflicting internal states (either refusing to combine, or requiring an extra pre-check roll before combination).",
      "Without the conflict-resolution rule, the required cooperative mending attempt could not represent characters whose own beliefs actively clash while trying to cooperate.", "core"),
    N("A restorative action's WORST outcome branch must apply a large fixed penalty to the shared currency that, when the currency is already at its floor, is explicitly capable of driving the currency past its own floor into a DISTINCT, separately-defined terminal state rather than clamping at the floor.",
      "Clamping at the floor instead of overshooting into a terminal state would remove the described possibility of a failed last-ditch attempt itself causing the ending.", "core"),
    N("That terminal state must be representable as categorically different from an ordinary win/loss for any single actor or faction — an ending that is neither a faction victory nor a faction defeat, but a transformation of the shared setting/state itself.",
      "Forcing the terminal state into a normal win/loss frame would misrepresent the source's explicit 'no faction wins... the world does not end, it becomes unintelligible.'", "important")
  ],
  "temporal": {
    "span_seasons": "ongoing, potentially ending the campaign",
    "needs_memory_of": "all active hazard/lock instances feeding the drains; the current institutional resource value; the current currency value, to know if at floor.",
    "needs_deadline": "no fixed date, though the compounding drains make time itself an adversary"
  },
  "who_acts": ["cooperating practitioners (choose to attempt the compound restorative action)", "an institution's own automatic seasonal check (nobody decides)", "nobody decides the summed automatic drains"],
  "knowledge": ["not primarily epistemic"],
  "ends_when": "mixed — the four structural exit conditions being met is a combination of person-chooses (attempting the compound action) and a roll resolving it; failing to exit ends in the currency crossing its floor via a failed restorative attempt, which is a roll whose framing is a threshold-fires outcome (the resulting terminal state, not the roll itself, is what nobody decides)."
})

with open("/tmp/claude-0/-home-user-ttrpg/e2c0050d-067c-5d41-a0c2-ee97ae491748/scratchpad/part2.json", "w") as f:
    json.dump(cases, f)
print(len(cases), "cases in part 2")
