# CROSS-GAME AND HISTORICAL PRECEDENT — ammunition for the from-scratch design

## THE NULLS — where we are INVENTING, not adapting. Most important section.
N-1 NO GAME MODELS THE CONTENT OF AN ARGUMENT. Burning Wheel abstracts to a scalar Body of
    Argument; Ace Attorney reduces to one correct pair; Victoria 3 substitutes faction arithmetic;
    Diplomacy leaves it to players' mouths. **T7 and T9 sit on this null.** The material is in the
    HISTORICAL corpus (stasis theory, Nyaya nigrahasthana, the ordo iudiciarius), not in games.
N-2 NO EXPRESSION CHANNEL FOR INTERIOR STATE. The field's own literature calls it "perhaps the
    hardest challenge": physics has graphics, nothing equivalent exists for mood, grudge, loyalty
    or ambition. Every attempted solution NARROWS SCOPE rather than generalising (Dwarf Fortress
    templated text over a facet band; Nemesis's closed trait vocabulary; Wildermyth's hand-written
    variants, explicitly not procedural). **T2 and T3 sit on this.** TRACKING IS NOT EXPRESSING and
    the field failed at the second.
N-3 PERSONAL-SCALE LEVERAGE ACROSS THREE ORDERS OF MAGNITUDE OF N IS UNSOLVED. Every mechanism is
    either SCALE-BLIND (Dominions' commander anchor, Total War's lord aura - dominates a small mass,
    evaporates in a large one) or FULLY FUSED (Mount & Blade - consistent, and the personal actor
    becomes irrelevant as N grows). Well-funded teams tried. **T1, T5, T6 sit on this.**
N-4 AUTO-RESOLVE CALIBRATION. Creative Assembly never published a target in twenty years. The real
    diagnosis: the played path is a PROCESS and the fast path is a FORMULA - two different slices
    cannot be calibrated to agree, only made to agree on average, which twenty years of complaints
    say is insufficient.
N-5 CERTIFYING GENERATED CONTENT IS *GOOD*. Only *varied* is measurable. Fourteen years on,
    "interesting" and "characterful" have NO PROPOSED MEASUREMENT AT ALL.
N-6 LEGIBILITY VS DEPTH. "No shipped game in this domain has found a formula-legible system that
    critics also called deep, nor a deep system that critics also called clear."
N-7 THE APPOINTED GOVERNOR. Total War added, removed and re-added it THREE TIMES for three
    different reasons across twenty years. "There is no convergent answer - a real unsettled design
    tension, not a solved problem you are behind on."
N-8 NOBODY CAPS UNIT *QUALITY*. 4/4 franchises cap quantity by rank or title and let effectiveness
    climb open-endedly.
N-9 FOG OF WAR FOR SOCIAL STATE IS ESSENTIALLY UNATTESTED IN GAMES. Every information-asymmetry
    steal below is a HISTORICAL distillation. **No surveyed game ships an NPC acting on knowingly
    false political information. T3 and T4 are the most exposed throughlines in the brief.**

## THE STEALS
INFORMATION AS AN ACT
  * CORRESPONDENCE FILTERING (Claudius's freedmen). All petitions/intrigues route THROUGH a named
    person before reaching the principal; disposition approved|suppressed|surfaced. Influence is
    measured in VOLUME OF THINGS FILTERED, not rank - a servant with Standing 0 structurally
    outranks ministers, with no power stat. T3/T4/T5/T7.
  * THE FORGED SUCCESSION EDICT (Zhao Gao). In a vacancy window whoever holds the Mandate token can
    fabricate the record; IF UNCONTESTED IT IS WRITTEN TO CANON AS GENUINE UNTIL DISCOVERED, and
    discovery retroactively flips legitimacy. Cleanest "world believes a false thing" primitive.
  * RUMOUR -> COMMITMENT WINDOW (Day of the Dupes). An unwitnessed decision is a rumour, reversible
    until ratified; during the window anyone who publicly commits to the rumoured winner is tagged
    REGARDLESS OF OUTCOME. Makes acting on incomplete information the whole mechanic, not a penalty.
  * CONCEALMENT: hidden/concealed visibility revealed only by an audit; a regent who can DELAY
    emitting the death-notice; a paired hidden Exposure counter that rises as you extract and is
    discovered PROPORTIONAL TO A RIVAL'S ACTUAL INVESTIGATION SPEND, never automatically.
DEMANDS TRAVELLING UP
  * PETITION-AS-OBJECT, NOT STAT-CHANGE (Pliny/Trajan): the action produces a petition object the
    superior may APPROVE / DEFER / CONDITION. T5 in one line.
  * The English SC 8 corpus: 17,000 appeals split COMMON (communal grievance) vs PRIVATE
    (individual ask); success depends partly on WHO CARRIES IT - an intercessor's standing modifies
    the roll. Form is RANK-INDEXED (al-Qalqashandi's Subh al-a'sha is literally a rank x rank
    protocol table).
  * TWO INSTRUMENTS, NOT ONE: supplique (subject->sovereign, seeks grace) vs remontrance
    (institution->Crown, contests a measure), the latter with a real escalation ladder:
    remonstrance -> lettre de jussion -> remontrances iteratives -> lit de justice. Gives opposition
    a legitimate form that AFFIRMS the authority it opposes.
  * AGGREGATE LOW-RANK LEVERAGE = ONE HIGH-RANK REVOLT (Sened-i Ittifak): mid-rank actors coalescing
    force the same governance shift a single top-rank defector would. Paired with RANK = SECESSION
    BLAST-RADIUS: how far a defection propagates is a function of the defector's rank AND THE
    THINNESS OF THE LAYER ABOVE THEM. Directly serves T5 + the containment axiom.
DECISIONS LANDING ON A NAMED INDIVIDUAL
  * PATRONAGE CASCADE VOIDED (Woodville): every person carries standing_source and patron_id; when
    the patron dies ONE event fans out into N individual demotions. T6.
  * DECREE-WITH-COMPLIANCE: a decree lands in each locality as a COMPLIANCE ROLL, not an effect -
    grounded in the capitulary record repeatedly re-prohibiting the same abuses. The survey names
    instant-global-decree "THE SINGLE MOST COMMON ERROR IN GOVERNANCE GAMES."
  * THOMPSON'S TARGETING ORDER: a dearth riot targets MILLERS AND FORESTALLERS FIRST, then the
    governor. A downward shock resolves onto named local actors before it reaches the ruler.
SMALL GROUP -> LARGE GROUP CONTINUOUSLY  (this is Jordan's A-4, already solved historically)
  * POWER_BASE AS ONE TYPED FIELD. Seven climb-drivers: patronage / merit / kinship / bureaucratic /
    military / purchased / ideological. One loop. THE GIFT: the same field that types the rise types
    THE EXPLOITABLE VULNERABILITY. Patronage chains collapse top-down; credentialed merit is
    reversible by rewriting the criteria; kinship flips generationally; bureaucratic chokepoints are
    undone by a single bypass. Consolidation is SELF-LIMITING BY CONSTRUCTION, not by a balance
    patch. Discipline: the vulnerability must be READABLE BY THE PLAYER VIA INVESTIGATION or it is a
    coin-flip, not a mechanic.
  * COALITION THRESHOLD: below a clients_sponsored threshold an ordinary challenge works; above it
    ONLY A MULTI-PERSON COALITION can act. Power is never dominant - it is EXPENSIVE TO UNWIND, and
    the cost is paid by whoever waited too long.
  * SHADOW_STANDING (Yoritomo): an off-ladder accumulation track that past a threshold COMPELS THE
    FORMAL HOLDER TO LEGALISE IT in one stroke. Dual legitimacy, not replacement. Two brothers
    become a house become a faction without ever changing object type.
  * FRAGMENTATION-ON-DEATH (Yuan Shikai): network scale is recursive; on the patron's death each
    top-tier client with its own sub-network SPINS OFF as an independent standing-holder. Growth and
    fission on one field.
  * RECOGNITION-FISSION -> REAGGREGATION (1870 Bulgarian Exarchate firman): a NEGOTIATED charter
    splitting a bloc out, followed by a long CONTESTED-ALLEGIANCE PERIOD rather than instant
    resolution.
FAMILIES AND LINEAGES
  * Lineage-scoped objects ABOVE THE PERSON LIFESPAN: dynastic_leverage accruing across five reigns
    (Wang Mang); family Entrenchment on a lifetime tax-farm (malikane) where reclaiming BEFORE a
    threshold is administrative and AFTER it fires a rebellion crisis. Needs only accounting-cadence
    ticking plus the relationship graph.
  * CONTINGENT CLAIM BANKING (Habsburg): a marriage banks a DORMANT claim on an OCCUPIED seat that
    auto-fires on a watched vacancy. AND: a claim with no enforcement resolves to OPEN WAR, not
    automatic inheritance.
  * KINSHIP PRECEDENT (Fujiwara) decays automatically if the lineage fails to place a daughter for a
    generation - DEMOGRAPHIC failure, not violence.
  * KANTOROWICZ'S TWO BODIES: the corporate crown fiction was ENGINEERED TO ABOLISH THE INTERREGNUM.
    Normal succession preserves acceptance; CONTESTED succession RE-OPENS EVERY SETTLEMENT'S
    acceptance for renegotiation.
DEBATE WITH ATTACKABLE PROVENANCE  (the answer to null N-1)
  * NYAYA NIGRAHASTHANA: 22 ENUMERATED DEFEAT CONDITIONS - self-contradiction, evasion, silence when
    pressed - at which the debate FORCE-CLOSES. Resolution by NAMED FAULT AGAINST A CHECKLIST, not
    by a threshold roll. And RESORTING TO A QUIBBLE IS ITSELF A DEFEAT TRIGGER, which self-gates
    tactics without a rule saying so.
  * STASIS AS TERRAIN: diagnose WHAT THE FIGHT IS ABOUT before choosing a tactic - fact / definition
    / quality / JURISDICTION. Read as a STRONGEST-TENABLE-RUNG FALLBACK LADDER: deny the act ->
    deny the label -> admit-and-justify -> challenge the venue.
  * THE ORDO IUDICIARIUS: libellus -> litis contestatio -> a GRADED HIERARCHY OF PROOF -> verdict,
    with positiones/articuli as formal assertions EACH OF WHICH MUST BE SEPARATELY PROVED. Closest
    thing anywhere to attackable-provenance claims.
  * BURNING WHEEL'S SCALED COMPROMISE: the winner concedes IN PROPORTION to how much of his own
    position was destroyed. ONE RULE converts a "both roll, one wins" contest into one where BOTH
    OUTCOMES BIND.
  * INVENTORY-AS-ARGUMENT (Ace Attorney): claims are objects you hold, spend and lose.
  * SKILLS-AS-INTERLOCUTORS (Disco Elysium): a player's COMMITTED POSITIONS get voices that argue
    back when expedience beckons. T2.
CHEAP AND STRUCTURAL
  * RECORDED DEFEAT (senatus auctoritas): a motion that carried and was vetoed persists WITH NO
    FORCE AND FULL CITABILITY. "Very few games have this and it is nearly free." Survived the
    survey's own adversarial pass with no attached failure. T7.
  * THE VIEW SLICE: JA2 v1.13's audit tool changed no mechanic and is the most-cited fix in the
    personnel research; Shogun 2's VISIBLE BAND OVER A HIDDEN PRECISE VALUE. The rule: PUBLISH EVERY
    INPUT, PUBLISH A BAND, NEVER PUBLISH THE TRIGGER POINT. The corpus's only direct answer to
    having no GM, and it costs zero mechanics.

## THE REFUSALS
* CK3'S AMBIENT POPULATION MODEL. ~6-7 parentless sixteen-year-olds monthly; late saves past 24,000
  characters; two community mods pulling in OPPOSITE directions. GENERATE ON DEMAND, NOT ON A CLOCK.
* A SECOND RESOLVER OF ANY KIND. Dominions and M&B achieve consistency by never offering one; Total
  War is the only precedent with two paths and the only one with a twenty-year unsolved divergence.
  "Don't build a second resolver at all" is the FIRST option on the table, not a corner case.
* CONTRADICTION-MATCHING AS PRIMARY POLITICAL RESOLUTION. Excellent tension, ZERO political
  modelling - and in a political trial the winner is often the side whose evidence is worse.
* MANOEUVRE SETS DIFFERENTIATED BY DAMAGE OUTPUT. Duel of Wits players converged on two moves and
  stopped. The precise constraint: A MANOEUVRE MUST ALTER A PRIMITIVE, NOT JUST APPLY A FORMULA.
* ANY MANOEUVRE LAYER AT A LARGE POOL GAP. At 21-vs-11 it degenerates to "the bigger number wins
  fast." A rich option space earns its complexity ONLY WHILE THE SIDES ARE CLOSE.
* RELATIONSHIP MODIFIERS LARGE ENOUGH TO DISSOLVE STRUCTURAL CONFLICT. The CK3 critique: opinion
  bonuses paper over structural factors, so "you can generally succeed at things kings wanted to do
  but were unable to pull off." SOME CONFLICTS MUST BE POSITIONAL AND UNBUYABLE.
* BUYING THE OUTPUT OF AN EARNED RELATIONSHIP. Shadow of War's War Chests corroded the system FOR
  NON-PAYERS TOO by breaking the causal chain. Every durable tag needs PROVENANCE BOUND TO THE
  CAUSING EVENT.
* A MECHANISM ENGINEERED NOT TO FIRE. EU4's estates: legible, well-motivated, loyalty floor near 40
  and nothing crossed it. A MECHANISM TUNED NEVER TO REACH ITS FAILURE STATE IS INDISTINGUISHABLE
  FROM ONE THAT DOES NOT EXIST. Its mirror: Imperator's governors lost 20+ loyalty on appointment
  alone and bled regardless of play; scrapped in four months. THE TEST: run MAXIMUM available
  mitigation against MAXIMUM accrual and check the net is recoverable.
* GATING CAPABILITY ON BIOGRAPHY. Gate on a CLASS/ROLE and losing a person is a promotion
  opportunity; gate on "the officer with Cavalry History" and losing one person costs you cavalry
  permanently.
* A LEADER AS A FLAT BONUS ON A ROLL. A flat shift of size X is worth X/(0.8*sqrt(Pool)) - MORE TO A
  SMALL POOL THAN A LARGE ONE, so a leader trait is worth systematically more to a weak faction. The
  in-band form: THE LEADER CHANGES THE OPTION SET AND THE POOL SOURCE, NEVER ADDS A MODIFIER.
* A SCHEDULED RECOVERY TICK. Promotion and demotion must be caused by SPECIFIC EVENTS. A timer
  restoring standing on a cadence converts a consequence system into a treadmill.
* PARALLEL-TRACK PROLIFERATION. The disciplined answer is ONE SHARED RANK SPACE plus a bounded,
  named set of auxiliary meters that substitute-in at specific gates - never a second seat-space.
* TREATIES THAT BIND AUTOMATICALLY. Diplomacy has NO ENFORCEMENT MECHANISM WHATEVER and everything
  interesting follows from that one omission. CHEAP TALK IS THE DEFAULT; BINDING INSTRUMENTS ARE THE
  EXPENSIVE EXCEPTION.
* "WE HAVE THE SUBSTRATE" AS "WE HAVE EMERGENT NARRATIVE."

## SCALE COUPLING — the hardest problem, everything known
THE HARD FINDING: "No precedent demonstrates a mechanism whose personal-scale contribution is
provably leverage-in-band across the full range from N=1 to N=1000+." Two poles, both failures.
Mount & Blade is SIMULTANEOUSLY the game closest to this scope, the game the coupling ambition
defines itself AGAINST, and one of the two failure poles - and those are THE SAME DEFECT AT
DIFFERENT DISTANCES. A personal actor whose contribution does not scale is WHY the two layers read
as isolated.
WHAT HELD:
  * FOOTBALL MANAGER: every fixture is SPECIFIC (this match, these players, this rivalry), resolved
    at three fidelities of THE SAME ENGINE, calibrated so instant ~ played. Instant-result is the
    same PROCESS run headless, NOT a formula approximating it.
  * XCOM sits between: the strategic slate surfaces SPECIFIC missions; you play the ones that matter.
  * THE REFRAME WORTH MORE THAN EITHER: the AUTO tier is the EASIER problem, because the player made
    no choices to compress. The WITNESSED tier - present, one light roll - is the dangerous one,
    structurally closest to scalar collapse. So DO NOT TOLERANCE-TEST THE MEAN; TEST THE FAILURE
    MODE. The right question is "does auto ever produce a result a player who did play it out would
    call UNRECOGNISABLE?" - a distribution-SHAPE question. And because these scenes may never recur,
    err toward LEGIBLE, COARSE-GRAINED AND INSPECTABLE - a short list of factors the player can see
    feeding the roll.
  * THE ONLY CONCRETE ANTI-LEVERAGE RULE IN THE CORPUS: a personal->unit effect MUST BE A FRACTION
    OF THE UNIT'S OWN SIZE OR COHESION, NEVER A FLAT AMOUNT.
DOWNWARD COUPLING THAT SHIPPED: decree-with-compliance; dearth resolving onto millers and merchants
BEFORE the governor; the intendant overlay that SUPERSEDES WITHOUT REPLACING rank; the
Cordon-Complete flag where ONE settlement below threshold drops the bonus for the whole chain;
Relay/Beacon as genuine inter-settlement propagation; the TERRITORY REACH CAP - past a
settlement-count the aggregate genuinely represents "the governor can't reach everyone."
UPWARD COUPLING: rank-as-blast-radius; aggregate-mid-rank-mass; THE INSTABILITY ACCUMULATOR THAT
DOES NOT RESET BETWEEN SUCCESSION CRISES, so each collision fires at a LOWER threshold until a
STRUCTURAL rather than personnel fix lands; and THE SUPPRESSION RULE - a cultural-suppression action
that "solves" an unrest event should convert the grievance into a DORMANT, GENERATIONAL FLAG THAT
RE-ARMS AT A *LOWER* TRIGGER THRESHOLD, making the problem harder each time.
THE STRUCTURAL WARNING: "No surveyed precedent defends a cross-scale bridge whose DEFAULT STATE IS
INDISTINGUISHABLE FROM ITS ABSENCE." Every surveyed game either has no such seam or ships an
explicit, imperfect one.
TWO CONTAINER PRIMITIVES FOR THE AXIOM: ORGANIZATION (a membership cutting ACROSS places it does not
own - a guild in three cities) and TERRITORY (a place-cluster held as one aggregate) are ORTHOGONAL
AXES. The Ottoman sanjak vs the akinci corps on the same frontier: same ground, two management
objects, and the corps CAN START AN INTERNATIONAL INCIDENT THE BEY NEVER ORDERED. And: EVERY BOARD
GAME THAT MODELS CONTESTED POWER IS BUILT ON AN ENTITY THAT IS CONTESTED RATHER THAN OWNED -
Kremlin's politicians belong to nobody; John Company's ventures need several offices held by
different players. The genre solved shared control decades ago BY NOT MAKING OWNERSHIP A SCALAR
FIELD.
