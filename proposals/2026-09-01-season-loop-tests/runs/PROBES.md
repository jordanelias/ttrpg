# THE PROBE LEDGER

**122 probes.** Each is a real execution against `shape.py` that either
completes or raises a typed gap.

## How each verdict was reached

`ARCHITECTURE.md` §34: *overstating the enforcement column is the failure mode.* §47:
*a false claim of enforcement is worse than none, because it stops the next reader from
checking.* So every probe declares its provenance:

| `by=` | means | count |
|---|---|---|
| `construction` | **the shape itself raised** — a gate, a law or a type stopped it. This is evidence | 78 |
| `no-signature` | nothing to call. The design supplies no function by which it could be attempted — which *is* the refusal, but **absence is not a guard** | 25 |
| `convention` | the shape permits it and only a reader stops it. §27.2 is the design's own example and says so out loud | 1 |
| `probe-model` | the probe supplies a model the design does not, to reach the question at all | 18 |

## ⚠ THE ENFORCEMENT SPLIT — the single most important number in this ledger

**Of 59 PROBES that did not pass, 29 were raised BY THE SHAPE ITSELF and 24 exist only because THERE IS NO SIGNATURE TO CALL.**

> ⚠ **THIS COUNTS PROBES, NOT GAP EVENTS, and the two numbers differ.** `results.json`'s `_trace_counts.GAP` is 66 — every gap RAISED during the run, including several inside one probe and several the corpus cases hit. This line counts probes whose VERDICT is not PASS: 59 of 122. Both are honest counts of different populations, and `G10` forbids reporting either without its basis — which this file did until the `W5` adversarial pass read both.

That is close to an even split, and it matters more than any case verdict. A refusal a
gate enforces and a refusal that exists because nobody wrote the function are different
guarantees, and §34 is explicit that *overstating this column is the failure mode*.

**Why the distinction bites hardest at the port.** §47 concedes that [engine] GDScript
has no module system and no visibility modifiers, so the guarantee there is
*unreachable-by-name*, not *unwritable*. Every refusal in the `no-signature` half is one
a contributor closes by simply writing the function — no gate fires, no test goes red,
and the design's own §27.2 admission applies: *enforced by a person noticing*.

**And 14 of 63 PASSes are not by construction
either** — they are listed individually below and should be discounted accordingly. A
`probe-model` PASS means the instrument supplied something the design does not.

## The probes

| probe | verdict | by | § | what it tests |
|---|---|---|---|---|
| `A1` | **FORBIDDEN** | construction | S19.4 | the story must be able to be reconstructed from what caused what |
| `A11` | **FORBIDDEN** | construction | S10.1 | a place must be able to keep a running total so it does not recompute every time |
| `A12` | **FORBIDDEN** | construction | S4 | an expensive derived value must be able to be reused within a step |
| `A14` | **COLLISION** | no-signature | S40.2 | a character must be able to respond inside the same season to something that just happened |
| `A15` | **UNSPECIFIED** | no-signature | S40.1 | a self-feeding situation must be able to stop |
| `A16` | **FORBIDDEN** | no-signature | S40.3 | a region must be able to advance on its own schedule while others wait |
| `A18` | **UNSPECIFIED** | no-signature | S41 | a developer must be able to work one module without reading the world |
| `A19` | **NO-PRODUCER** | probe-model | S43 | a piece of the game must be able to be swapped without editing the engine |
| `A20` | **FORBIDDEN** | no-signature | S44.1 | influence passing between scales must be able to be checked for direction |
| `A21` | **FORBIDDEN** | no-signature | S37.3 | an order from above must be able to reach everyone it applies to |
| `A22` | **UNSPECIFIED** | construction | S27/E2 | each region must be able to run its own slice of the loop |
| `A23` | **FORBIDDEN** | construction | S22.4 | a running total of everything that ever happened must be able to be kept |
| `A27` | **UNOWNED** | no-signature | S22.3 | every value in the game must be able to name who writes it |
| `A29` | **FORBIDDEN** | probe-model | S19.5 | a subsystem must be able to keep its own record of what it did |
| `A3` | **FORBIDDEN** | construction | S3-L4 | the story must be able to conclude when a tracked quantity reaches a value |
| `A30` | **UNGRADED** | construction | S42.2.1 | a piece of the design with no evidence behind it must be able to be used anyway |
| `A31` | **UNSPECIFIED** | construction | S27/E2 | a conclusion drawn from the engine must not depend on a number nobody decided |
| `A33` | **COLLISION** | no-signature | S37.4 | an instruction must be able to be distorted somewhere between issuer and executor |
| `A34` | **FORBIDDEN** | no-signature | S34 | a relationship or a standing must be able to decay from nobody tending it |
| `A36` | **UNSPECIFIED** | construction | S27/E2 | what a character does first must be able to close off what they could have done after |
| `A4` | **UNSPECIFIED** | construction | S27/E2 | the same starting conditions must be able to produce the same history |
| `A6` | **FORBIDDEN** | no-signature | S3-L1 | an institution must be able to take an action |
| `A7` | **UNSPECIFIED** | construction | S39.4 | a fight, a hearing and an argument must be able to be the same machinery |
| `A9` | **FORBIDDEN** | no-signature | S4 | one place must be able to see what is happening in another |
| `F11` | **FORBIDDEN** | no-signature | S38 | a character must be able to know how strong their own faction is |
| `F14` | **FORBIDDEN** | construction | S22.4 | a faction's territory must be countable as it gains and loses ground |
| `F15` | **UNSPECIFIED** | no-signature | S54 item 13 / S61 | a post must be able to employ people whose competence is what actually gets used |
| `F16b` | **FORBIDDEN** | construction | S10.1 | a faction must be able to hold a pooled level of loyalty, unrest or legitimacy |
| `F17` | **UNSPECIFIED** | construction | S27/E2 | a superior's approval must be able to be a formal precondition without which subordinates cannot act |
| `F19` | **NO-PRODUCER** | no-signature | S36.1 | a settlement's needs must be able to surface as demands without a named petitioner |
| `F21` | **UNSPECIFIED** | construction | S61 | a character sitting on a collective body must be able to have their individual position registered distinctly from the body's deci |
| `F3` | **FORBIDDEN** | no-signature | S3-L1 | a faction must be able to take an action of its own |
| `F6` | **UNSPECIFIED** | no-signature | S62 | an order from above must be able to fail to arrive, distinctly from being refused |
| `F7` | **UNSPECIFIED** | probe-model | E2 | someone with no power must be able to get a matter in front of someone who has it |
| `F8` | **UNSPECIFIED** | construction | S61 | the body a matter reaches must be able to decide it |
| `F9` | **UNSPECIFIED** | construction | S27/E2 | a character must be able to spend a whole season putting the same matter to many people |
| `P15` | **UNSPECIFIED** | no-signature | S61 | something said in private must be able to stay private |
| `P17` | **UNSPECIFIED** | probe-model | S22.4 | a character's risk must be able to build up quietly across seasons without anyone acting |
| `P19` | **FORBIDDEN** | construction | S3-L4 | the story must be able to end when a counter reaches a value, with no person choosing |
| `P2` | **UNSPECIFIED** | construction | S27/E2 | a character must be able to take several distinct actions in one season and choose what to leave undone |
| `P25` | **FORBIDDEN** | construction | S15.3 | the world must be able to end a person's position without anyone acting |
| `P26` | **UNSPECIFIED** | probe-model | S22.4 | harm suffered over several seasons must be able to close off options |
| `P29` | **UNOWNED** | no-signature | S22.3 | a character must be able to move from one place to another and be somewhere else next season |
| `P2x` | **FORBIDDEN** | construction | S26.3 | an engine may quietly drop actions a character wanted beyond their budget |
| `P30` | **UNSPECIFIED** | construction | S27/E2 | what a character learned must still be true for them next season |
| `P33` | **UNSPECIFIED** | no-signature | S26.3 | performing a larger or riskier version of an action must be able to cost the actor more |
| `P35` | **UNSPECIFIED** | no-signature | S18.2 | a character must be able to have a standing among people who can never publicly acknowledge them, separate from their public stand |
| `P37` | **UNSPECIFIED** | probe-model | S27/E2 | a character's reaction must be able to be fully determined by their internal state rather than by a choice |
| `P38` | **NO-PRODUCER** | no-signature | S1 | an optimal window, a judgement call or an adjudication must be able to be made by a referee |
| `P41` | **UNSPECIFIED** | no-signature | S2 T7 | a character must be able to cite an established precedent or prior ruling to make a present argument stronger |
| `P43` | **FORBIDDEN** | construction | S22.4 | a quantity held by many characters individually must be able to be totalled across them |
| `P7` | **UNSPECIFIED** | construction | S22.4 | a character must carry lasting moral damage from what they were made to do |
| `P8` | **UNSPECIFIED** | construction | S27/E2 | one character must be able to be blocked by another without either knowing about the other |
| `P9` | **UNSPECIFIED** | construction | E2 | a superior must be able to direct a subordinate, and the subordinate must be able to refuse or deviate |
| `W10` | **FORBIDDEN** | construction | S10.1 | a place must be able to hold a level of discontent that rises and falls |
| `W13` | **FORBIDDEN** | no-signature | S25.1 / S3-L5 | a world-scale tracked quantity must be able to decay on a fixed schedule independent of anyone's actions |
| `W1x` | **UNGRADED** | construction | S42.2.1 | the world must be able to wear down a kind of place nobody wrote a rule for |
| `W3` | **FORBIDDEN** | construction | S3-L4 | a bad season must be able to make people angrier without anyone acting |
| `W5` | **UNOWNED** | no-signature | S22.3 | the harvest must be able to come in, better or worse from season to season |
| `A10` | PASS | construction | S4 | a place must be able to know something summed over everything inside it |
| `A13` | PASS | construction | S4 | a repeated derivation must be able to be computed once per step |
| `A17` | PASS | convention | S27.2 | every outcome in the game must go through one place |
| `A2` | PASS | probe-model | S19.4 | a sequence of related happenings must be able to be read back as one story |
| `A24` | PASS | construction | S35 | a mechanism written for the powerful must be able to work for a whole population |
| `A25` | PASS | construction | S6.2 | a cause that spans several regions must be able to exist with no parent region |
| `A26` | PASS | construction | S38.1 | the engine must be able to walk its own references without looping forever |
| `A28` | PASS | construction | S19.1 | every recorded happening must be able to point at real prior happenings |
| `A31b` | PASS | construction | S42.2.1 | a conclusion about how fast the world decays must not depend on a number nobody decided |
| `A31c` | PASS | construction | S42.2.1 | a conclusion about which actions a place supports must not depend on a number nobody decided |
| `A32` | PASS | construction | S62 | the number of playable moments a character gets must be able to be counted |
| `A35` | PASS | probe-model | S52 | the port must be able to target a decided engine version |
| `A37` | PASS | construction | S27 | movement, binding decisions and social acts must be able to resolve in a fixed order relative to each other |
| `A38` | PASS | construction | S27.4 | an attempt far beyond a character's ability must be refused rather than rolled |
| `A39` | PASS | construction | S39.2 | the outcome of a conflict must be traceable back to the action that started it |
| `A5` | PASS | construction | S32 | the outcome must not depend on the order the engine happened to process things in |
| `A8` | PASS | construction | S39.3 | a conflict must be able to open a conflict inside itself |
| `F1` | PASS | construction | S14.2 | a group of people must be able to share a cause that spans places and outlives its founder |
| `F10` | PASS | probe-model | S54.1 | several live demands on one matter must be able to resolve without cancelling each other |
| `F12` | PASS | construction | S11 | a post must be able to be given and taken away by named people at named occasions |
| `F13` | PASS | construction | S24 | when a post falls empty the process to fill it must be able to start |
| `F16` | PASS | construction | S10 | a faction must be able to hold a pooled resource that its members' actions raise and lower |
| `F18` | PASS | probe-model | S36.1 | a place must be able to generate demands of its own that cut against what the authority above ordered |
| `F2` | PASS | probe-model | S54 item 20 | when everyone abandons a cause, what it held must be able to be taken by someone else |
| `F20` | PASS | probe-model | S14 | a standing agreement between two polities must be able to constrain what people on either side may do |
| `F4` | PASS | construction | S11.1 | holding a post must be able to make an action available that is not available otherwise |
| `F5` | PASS | probe-model | S6.2 | a body with members everywhere and a seat nowhere must be able to issue instructions |
| `P1` | PASS | construction | S3-L1 | a person with no office, post, command, faction rank or standing must be able to act at all |
| `P10` | PASS | construction | S13 | a character must be able to perform a repeated, multi-season task the engine tracks as ongoing |
| `P11` | PASS | construction | S9.2 | skill must supply dice and must never make an action unavailable |
| `P12` | PASS | construction | S17 | the set of things a character may do must be computed, not an authored list |
| `P13` | PASS | probe-model | S18.2 | a character's needs must drive their choices |
| `P14` | PASS | construction | S18.2 | how a character is regarded must be able to differ from how they regard themselves |
| `P16` | PASS | construction | S20 | how a character is seen must be able to differ between people who know different things |
| `P18` | PASS | construction | S3-L5 | a counter reaching an edge must be able to force a named person to answer |
| `P20` | PASS | construction | S29 | a person who was previously part of a crowd must be able to become a named individual |
| `P21` | PASS | construction | S9.1 | a crowd must be able to act, and a person must be able to step out of one, with no conversion |
| `P22` | PASS | construction | S13 | possession of an object must be able to make someone else's action unavailable or costlier |
| `P23` | PASS | construction | S16 | a character must be able to simply vanish or be killed, with no institutional process |
| `P24` | PASS | construction | S15.3 | when a character dies everything they held must end, including things held elsewhere |
| `P27` | PASS | construction | S20 | a character must be able to quietly do less than ordered, discoverable only by investigation |
| `P28` | PASS | no-signature | S20 | no character may read another's memory directly |
| `P2y` | PASS | construction | S26.3 | a character must be able to do several things inside one scene without spending a second scene action |
| `P3` | PASS | construction | S3-L2 | a character must decide from what they believe, which may be wrong, and never from world truth |
| `P31` | PASS | construction | S9 | a character must be able to act on a private motive that consistently skews their judgement, unrecognised by themselves and by the |
| `P32` | PASS | construction | S12 | a character's own condition must be able to degrade across a season so that their available actions narrow predictably |
| `P34` | PASS | construction | S20 | an office-holder must be able to be the only living person who knows a thing, so that removing them destroys it |
| `P36` | PASS | construction | S17 | a discovery must be able to be acted on in several distinct ways, each leading somewhere different |
| `P39` | PASS | probe-model | S15 | two characters must be able to have an ongoing relationship that carries state and changes over seasons |
| `P4` | PASS | construction | S3-L2 | a character must be able to believe something false and act on it as if true |
| `P40` | PASS | probe-model | S15 | a character must be able to hold obligations to two bodies that come into direct conflict |
| `P42` | PASS | construction | S26.3 | a wounded or distant character must be able to get fewer actions in a season than a healthy one at home |
| `P5` | PASS | construction | S19.3 | a character must be able to do something covertly, or be wrongly blamed for what another did |
| `P6` | PASS | construction | S9.3 | a character's moral commitments must be able to change, through argument and consequence |
| `W1` | PASS | construction | S12.1 | a place must be able to fall into disrepair until things can no longer be done there |
| `W11` | PASS | construction | S31.1 | a character must be able to eat from the stores of the place they live in |
| `W12` | PASS | probe-model | S54 item 18 | a world must be able to start with people in it who hold no post |
| `W2` | PASS | construction | S3-L4 | the world must be able to change while no character is doing anything |
| `W4` | PASS | construction | S25 | an environmental or material condition must be able to worsen on its own |
| `W6` | PASS | construction | S31.1 | a disaster must be able to strike many places at once and be one thing that happened |
| `W7` | PASS | construction | S13 | a document must be able to lapse after a time |
| `W8` | PASS | probe-model | S13.1 | a legal or institutional process must be able to advance against a character who is passive |
| `W9` | PASS | construction | S10.3 | a place's population must be able to grow and shrink |

## Every gap, with the law that produced it

### `A1` — causes[] is required and non-empty  ·  **FORBIDDEN**  ·  `S19.4`  ·  by `construction`
**what:** Event thing.happened emitted with causes=[]

**needs:** causes: [ROOT] for an antecedent-free emission
**law:** S19.4 -- causes[] is REQUIRED AND NON-EMPTY; [ROOT] makes the empty list unrepresentable rather than merely discouraged

### `A11` — a rung stores that aggregate  ·  **FORBIDDEN**  ·  `S10.1`  ·  by `construction`
**what:** Rung.density assigned -- not a declared field of S10's record

**needs:** a Query over the containment subtree, owned by Nobody
**law:** L3 -- every aggregate is a function, never a field. S22.1 -- if the aggregate is a function it CANNOT go stale and CANNOT be initialised and then forgotten, because there is nothing to initialise

### `A12` — a cache is built inside the parallel map  ·  **FORBIDDEN**  ·  `S4`  ·  by `construction`
**what:** cache 'k' built inside a parallel map

**law:** S4 -- the cache is built AT A BARRIER; NOTHING INSIDE A PARALLEL MAP BUILDS ONE

### `A14` — a person reacts within the season to what another just did  ·  **COLLISION**  ·  `S40.2`  ·  by `no-signature`
**what:** 'no reaction inside a season' vs the seam's nested DELIBERATE

**needs:** a ruling on which sentence binds
**law:** S34.1 says 'NO REACTION INSIDE A SEASON AT PERSON SCALE -- you anticipated, or you are late'. S40.2 says a contest 'runs the same steps over a smaller person set on a shorter clock' INSIDE RESOLVE, and 'a contest can open a contest', so DELIBERATE RE-RUNS INSIDE RESOLVE against a partially-moved world. BOTH SENTENCES ARE IN THE CHAIN and the design has NOT reconciled them

### `A15` — a spiral terminates  ·  **UNSPECIFIED**  ·  `S40.1`  ·  by `no-signature`
**what:** a termination argument per self-feeding loop

**needs:** a CROSS-SEASON bound
**law:** S40.1 -- FOUR ARCS PLUS THE KING ARE SPIRALS; NOTHING BOUNDS ONE. That debt is CROSS-SEASON and no within-tick argument touches it in either direction. `max_depth` bounds nesting WITHIN a tick and says nothing across ticks

### `A16` — a container runs its own clock  ·  **FORBIDDEN**  ·  `S40.3`  ·  by `no-signature`
**what:** a per-container clock

**needs:** nothing -- the parallelism it would buy is ALREADY AVAILABLE: DELIBERATE is a pure map at Godot 4.0
**law:** S40.3 -- a per-container clock is A NESTING FORM WITHOUT A CAP ARGUMENT: it has no `depth`, no `max_depth`, and no caller to supply one. It voids (1) the frozen world, (2) the canonical act order, (3) the non-decreasing season index. Rung's declared fields are ['dates', 'envelope', 'id', 'judging_set_rule', 'kind', 'records', 'sites', 'stake', 'stores', 'transmission'] -- there is no tick, by construction. THE CLOCK BUYS NOTHING AND COSTS THREE INVARIANTS

### `A18` — a module declares what it may receive and emit  ·  **UNSPECIFIED**  ·  `S41`  ·  by `no-signature`
**what:** the contract descent

**needs:** one validated parent over authored registries, generated, gated by a blocking round-trip
**law:** S41 -- T5 needs to know PER MODULE what it may RECEIVE; T6 needs to know what it may EMIT; R-2's 'no module reaches through another' is the same requirement as a prohibition. NO SURFACE IN THE CHAIN ANSWERS IT FOR ANY MODULE, which means R-1 AND R-2 ARE TODAY UNENFORCEABLE IN PRINCIPLE, not merely unenforced

### `A19` — a missing provider is a startup failure with a name in it  ·  **NO-PRODUCER**  ·  `S43`  ·  by `probe-model`
**what:** role(s) ['witness_channels'] have no provider in the manifest

**needs:** a registry row naming a role and its provider
**law:** S43 -- the engine names the ROLE; the registry names the MODULE; RESOLUTION HAPPENS BY STRING AT BOOT. A missing provider is a startup failure with a name in it. THE MANIFEST IS THE SEAM; A PATH LITERAL IN A BODY IS NOT

### `A20` — a wrapper checks what crosses a rung boundary  ·  **FORBIDDEN**  ·  `S44.1`  ·  by `no-signature`
**what:** a wrapper checking direction on a Key crossing a rung boundary

**needs:** nothing -- THE RULE WAS STATED OVER A FIELD THAT DOES NOT EXIST
**law:** S44.1 -- THERE IS NOTHING TO CHECK. Event's fields are ['causes', 'changes', 'degree', 'emitted_at', 'id', 'kind', 'subject']: no target, no actor. 'The only transport the suite defines IS a chain of `tell` acts; there is no non-act news transport anywhere in the shape.' Observers are computed at WITNESS from presence; THE EMITTER DECLARES NO RECIPIENT. Three independent lanes killed this, and the fix that suggests itself -- add a target field -- is the twin of the attribution field the design DELIBERATELY REMOVED

### `A21` — a dispensation is broadcast to every descendant  ·  **FORBIDDEN**  ·  `S37.3`  ·  by `no-signature`
**what:** broadcasting a dispensation to all descendants

**needs:** publish as a `tell`, which DISTORTS IN TRANSIT; the person's own opening_set does the rest
**law:** S37.3 -- it deletes T3 AND T6 AT ONCE: everyone would receive IDENTICAL, UNDISTORTED terms. 'It travels by being noticed, NOT DOWN A CHAIN OF POSTS.' And SCOPE ENUMERATES EXECUTORS, NOT PLACES, so there is no descendant set to broadcast to in the office-cluster case

### `A22` — the loop's steps partition per container  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'act' is on no row of the verb table

**needs:** a row in verb_table.yaml, ruled before it is added
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids

### `A23` — an aggregate over ended edges is monotone  ·  **FORBIDDEN**  ·  `S22.4`  ·  by `construction`
**what:** aggregate 'revocations_ever' composed over 1 ENDED edge(s)

**needs:** filter to until == null before summing
**law:** L3 clause 3 -- ended Tenures PERSIST as historical claim subjects (S15.2), so a count over live AND ended rows is monotone non-decreasing. That is a ratchet built entirely out of 'structural' edges

### `A27` — every value the game needs has an owner  ·  **UNOWNED**  ·  `S22.3`  ·  by `no-signature`
**what:** 4 values named in the ownership table's OWN gap list

**needs:** an ownership row each
**law:** S22.3 -- named rather than glossed: season_factor's distribution (BLOCKS yield); the cohort's construal spread (rule stated, representation not); the object-side Tenure index (Nobody, by rule -- a barrier-built cache); travel legs (in the write matrix AND the churn ledger AND no ownership row)

### `A29` — two logs share a causes chain  ·  **FORBIDDEN**  ·  `S19.5`  ·  by `probe-model`
**what:** an Event in log A naming an Event in log B as its cause

**needs:** ONE LOG
**law:** S19.5 -- World has exactly 1 log. Two logs CANNOT share a causes[] chain, so T3's multiple perspectives on one event AND arcs-as-provenance-chains BOTH break at the seam. The seam returns contest Events INTO THE SAME LOG. The non-circular grounds: WITNESS is ONE GLOBAL PASS, and the design's predecessor loop was RETIRED because its WITNESS was not global

### `A3` — an arc ends at a counter with nobody deciding  ·  **FORBIDDEN**  ·  `S3-L4`  ·  by `construction`
**what:** (Person, stance) written during MATTER

**needs:** one of ['RESOLVE']
**law:** L4 / S25 -- NO SOCIAL QUANTITY MOVES AT MATTER. 'The world may silt a harbour; IT MAY NOT SOUR A TOWN'S MOOD.' This is the design refusing, not the design failing to say

### `A30` — an ungraded value is used anyway  ·  **UNGRADED**  ·  `S42.2.1`  ·  by `construction`
**what:** harness fixture 'a_number_nobody_ruled' is not registered

**needs:** inject it, grade it assumption, name the injection site, sweep it
**law:** S42.2.1 -- a silent default does not fail; it answers, plausibly and wrongly, forever

### `A31` — a verdict is stable across a fixture sweep  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'v0' is on no row of the verb table

**needs:** NOTHING FROM THE DESIGN -- #353 does not name 'v0' as a verb. This is the CALLER'S invention and the gap is the caller's
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids. ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)

### `A33` — refraction has a side  ·  **COLLISION**  ·  `S37.4`  ·  by `no-signature`
**what:** emitter-side vs receiver-side refraction

**needs:** pick one, write it down beside the code, and expect the choice to be revisited
**law:** S37.4 -- R-2 says downward influence is 'EMITTING a refraction' (EMITTER-side); the act vocabulary puts `refract` at the RECEIVING end, beside `comply`, `evade`, `defy`. THE CHAIN HAS NOT RECONCILED THESE and emitter-side and receiver-side distortion ARE DIFFERENT GAMES

### `A34` — a social quantity sinks by neglect alone  ·  **FORBIDDEN**  ·  `S34`  ·  by `no-signature`
**what:** a scheduled social recovery or decay

**needs:** a ruling -- S62 lists this as a LIVE DESIGN CHOICE affecting three arcs
**law:** S34 -- 'no scheduled social recovery' is STRUCTURAL BY PHASE MEMBERSHIP: of ['CALENDAR', 'MATTER', 'DELIBERATE', 'RESOLVE', 'WITNESS', 'CENSUS'], MATTER moves no social quantity (L4), DELIBERATE writes nothing, RESOLVE needs an act, WITNESS writes only ledgers, CENSUS is demand-driven. THERE IS NO STEP IN WHICH A RESTORING TIMER COULD RUN, so a design that wanted one HAS NOWHERE TO PUT IT

### `A36` — a person's act order is the order it resolves in  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'buy_grain' is on no row of the verb table

**needs:** NOTHING FROM THE DESIGN -- #353 does not name 'buy_grain' as a verb. This is the CALLER'S invention and the gap is the caller's
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids. ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)

### `A4` — two runs of the same seed produce the same log AND the same hash  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'do' is on no row of the verb table

**needs:** a row in verb_table.yaml, ruled before it is added
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids

### `A6` — an institution acts  ·  **FORBIDDEN**  ·  `S3-L1`  ·  by `no-signature`
**what:** 'The Church excommunicates'

**needs:** 'the Confessor, at a venue, issues'
**law:** L1 -- NO INSTITUTION ACTS, NO FACTION ACTS, NO THRESHOLD ACTS. An institution acts BY A NAMED PERSON AT A VENUE. `Act.actor` is one person id and `resolve` takes no institution; the first sentence IS NOT SPELLABLE

### `A7` — a contest is the season loop nested  ·  **UNSPECIFIED**  ·  `S39.4`  ·  by `construction`
**what:** the degree ladder's margin model

**needs:** a margin -- pool, obstacle, and the four band edges read off it
**law:** S39.4 -- ONE degree ladder for every scale, FOUR BANDS READ OFF THE MARGIN, never off the obstacle's size. No in-chain document supplies the margin model, and S27.2 refuses a second resolver, an auto-resolve formula and a fast path -- so a band computed here without a margin IS the second resolver

### `A9` — a rung reads a sibling's state  ·  **FORBIDDEN**  ·  `S4`  ·  by `no-signature`
**what:** a rung reading a sibling's or a descendant's state directly

**needs:** an R-1 compute-on-demand aggregate over its OWN descendants
**law:** R-1 -- a rung may read its own state and any message addressed to it; it MAY NOT read a sibling's or a descendant's state directly. A cross-rung read is THE SINGLE EASIEST WAY TO DESTROY T5 AND T6, because ONCE THE REALM CAN READ A PERSON DIRECTLY THERE IS NO REASON FOR THE LADDER TO EXIST AND EVERY INTERMEDIATE RUNG QUIETLY BECOMES DECORATION

### `F11` — a person knows their faction's true strength  ·  **FORBIDDEN**  ·  `S38`  ·  by `no-signature`
**what:** reading faction strength from inside choose()

**needs:** `leaders_as_claimed` / `norm_as_claimed` -- what they CLAIM about it
**law:** S38 -- every lateral traversal is RESOLVER-SIDE (['descendants', 'lateral', 'presence', 'r1_aggregate', 'hold_force']), World FIRST, and `choose` has no World, so the call fails at the call site for want of an argument. The person-side surface is ['assemble', 'opening_set', 'budget', 'entrenchment']. THIS IS NOT A LIMITATION TO WORK AROUND: it is why a person CANNOT know their faction's true strength, only what they claim about it

### `F14` — a faction's holdings-ever are counted  ·  **FORBIDDEN**  ·  `S22.4`  ·  by `construction`
**what:** aggregate 'held_ever' composed over 1 ENDED edge(s)

**needs:** filter to until == null before summing
**law:** L3 clause 3 -- ended Tenures PERSIST as historical claim subjects (S15.2), so a count over live AND ended rows is monotone non-decreasing. That is a ratchet built entirely out of 'structural' edges

### `F15` — an establishment does the office's work  ·  **UNSPECIFIED**  ·  `S54 item 13 / S61`  ·  by `no-signature`
**what:** establishment size

**needs:** how many people an office employs, and how they are chosen
**law:** S61 -- one of FOUR BLOCKING GAPS DROPPED FROM THE OPEN REGISTER and folded back as `grade: absent`. S11.1 makes the pool `capability of the dispatched establishment member(s) ACTUALLY PERFORMING IT`, so with an empty establishment an office has no pool source at all

### `F16b` — a faction-wide SOCIAL quantity is pooled and stored  ·  **FORBIDDEN**  ·  `S10.1`  ·  by `construction`
**what:** Rung.legitimacy assigned -- not a declared field of S10's record

**needs:** a Query over the containment subtree, owned by Nobody
**law:** L3 -- every aggregate is a function, never a field. S22.1 -- if the aggregate is a function it CANNOT go stale and CANNOT be initialised and then forgotten, because there is nothing to initialise

### `F17` — an authorization precedes the act it authorises  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'raid' is on no row of the verb table

**needs:** NOTHING FROM THE DESIGN -- #353 does not name 'raid' as a verb. This is the CALLER'S invention and the gap is the caller's
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids. ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)

### `F19` — a place produces a demand with nobody petitioning  ·  **NO-PRODUCER**  ·  `S36.1`  ·  by `no-signature`
**what:** a demand originating from a place rather than a person

**needs:** a named person who wants it, and a named person who carries it
**law:** S36.1 -- 'a want -> Petition(petitioner, ...)'. EVERY ARROW IS A PERSON'S ACT OR A CALENDAR FACT: no automatic promotion, no queue drain, no priority function -- and therefore NO PRODUCER for a placeless want. A Rung owns `matter`, `dates`, `envelope`, `stake` -- arrangements, not wants

### `F21` — a member's individual position is recorded in a body's collective output  ·  **UNSPECIFIED**  ·  `S61`  ·  by `construction`
**what:** judging_set_rule

**needs:** who decides at a sitting
**law:** S61 -- NOTHING IS DECIDED AT A SITTING. T5's 'filtered at a rung' runs straight through it, and S10.2's 'arrangements, not choices' cannot be confirmed until it is

### `F3` — a faction acts  ·  **FORBIDDEN**  ·  `S3-L1`  ·  by `no-signature`
**what:** a faction taking an action of its own

**needs:** a named person at a venue
**law:** L1 -- `resolve` has NO FACTION PARAMETER and a faction has NO VERBS. `Act.actor` is a single id (str) and a faction IS a Proposition plus commit edges (S14.2), which is not an actor. 'The Church excommunicates' IS NOT SPELLABLE

### `F6` — a dispensation reaches a person who never heard it  ·  **UNSPECIFIED**  ·  `S62`  ·  by `no-signature`
**what:** how much a dispensation distorts in transit

**needs:** a distortion model, and a ruling on emitter- vs receiver-side refraction
**law:** T6 says it distorts; NOTHING SPECIFIES BY HOW MUCH (S62). The structural half works -- publishing is a `tell`, delivery is not assumed, and an executor who never received it is DISTINCT from one who received it and refused -- but the distortion itself has no model, and S37.4 records that the chain uses `refraction` TWO WAYS

### `F7` — a demand rises from a hearth to a duchy  ·  **UNSPECIFIED**  ·  `E2`  ·  by `probe-model`
**what:** 'carry' has a precondition the fold cannot evaluate: 'a Petition exists; costs budget like any act'

**needs:** a predicate in REQUIRES_PREDICATES, or a `requires:` the table states structurally rather than in prose
**law:** §E2 -- `requires` is checked IN THE FOLD. Stated as prose it is the same defect `resolve` had, one column along: a rule the code cannot read

### `F8` — the sitting decides  ·  **UNSPECIFIED**  ·  `S61`  ·  by `construction`
**what:** judging_set_rule

**needs:** who decides at a sitting
**law:** S61 -- NOTHING IS DECIDED AT A SITTING. T5's 'filtered at a rung' runs straight through it, and S10.2's 'arrangements, not choices' cannot be confirmed until it is

### `F9` — petition spray  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'petition2' is on no row of the verb table

**needs:** NOTHING FROM THE DESIGN -- #353 does not name 'petition2' as a verb. This is the CALLER'S invention and the gap is the caller's
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids. ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)

### `P15` — a person's private act stays private  ·  **UNSPECIFIED**  ·  `S61`  ·  by `no-signature`
**what:** four of the five witness channels have no predicate: ['post_remit', 'witness_key', 'document_key', 'chronicle']

**needs:** a channel predicate that can EXCLUDE a person
**law:** S61 -- WITNESS AS SPECIFIED FANS EVERY EVENT TO EVERY PERSON. Nothing said in private is private. A WRAPPER DOES NOT FIX THIS AND MUST NOT BE PRESENTED AS FIXING IT

### `P17` — hidden exposure accumulates across seasons  ·  **UNSPECIFIED**  ·  `S22.4`  ·  by `probe-model`
**what:** the closed `axis` registry L3 clause 1 requires (asked for 'suspicion')

**needs:** a closed roster of axes, and a write-matrix row admitting the increment
**law:** L3 clause 1 permits a monotone counter PER (Person, axis) -- 'legal, since every increment is in the holder's own ledger' -- but ONLY where `axis` is ON A CLOSED REGISTRY. No such registry exists in the chain, and no S30 row admits the write. S54 item 6 adds that the axis must not be spelled `exposure` bare, or it collides with the need scalar

### `P19` — a threshold produces an outcome with nobody deciding  ·  **FORBIDDEN**  ·  `S3-L4`  ·  by `construction`
**what:** (Person, stance) written during MATTER

**needs:** one of ['RESOLVE']
**law:** L4 / S25 -- NO SOCIAL QUANTITY MOVES AT MATTER. 'The world may silt a harbour; IT MAY NOT SOUR A TOWN'S MOOD.' This is the design refusing, not the design failing to say

### `P2` — the scene budget is ~5 and the PERSON chooses what to leave undone  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'v4' is on no row of the verb table

**needs:** NOTHING FROM THE DESIGN -- #353 does not name 'v4' as a verb. This is the CALLER'S invention and the gap is the caller's
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids. ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)

### `P25` — a storm ends a tenure  ·  **FORBIDDEN**  ·  `S15.3`  ·  by `construction`
**what:** an actorless row wrote Tenure.until with no (Person, exists) change of its own

**needs:** the same row must cause the death it ends a tenure through
**law:** S15.3 -- a plague that kills the praefect ends his tenure THROUGH THE DEATH; A STORM CANNOT TOUCH IT. A second such seam means the column is the wrong mechanism

### `P26` — accumulated harm changes what a person may do  ·  **UNSPECIFIED**  ·  `S22.4`  ·  by `probe-model`
**what:** the closed `axis` registry L3 clause 1 requires (asked for 'harm_borne')

**needs:** a closed roster of axes, and a write-matrix row admitting the increment
**law:** L3 clause 1 permits a monotone counter PER (Person, axis) -- 'legal, since every increment is in the holder's own ledger' -- but ONLY where `axis` is ON A CLOSED REGISTRY. No such registry exists in the chain, and no S30 row admits the write. S54 item 6 adds that the axis must not be spelled `exposure` bare, or it collides with the need scalar

### `P29` — a person travels between rungs  ·  **UNOWNED**  ·  `S22.3`  ·  by `no-signature`
**what:** travel legs

**needs:** an ownership row
**law:** S22.3/S31.1 -- travel legs are IN THE WRITE MATRIX and IN THE CHURN LEDGER and IN NO OWNERSHIP ROW. And they move a person BETWEEN rungs, which is a fourth cross-owner operation MATTER's own list of three does not name

### `P2x` — the engine truncates an over-budget SCENE list  ·  **FORBIDDEN**  ·  `S26.3`  ·  by `construction`
**what:** p_king returned 6 scenes costing 6 against a budget of 5 scene actions

**needs:** `choose` is bounded by budget(person, view) -- the PERSON chooses what to leave undone
**law:** S26.3, re-stated in scenes per Jordan's 2026-09-02 ruling -- at one scene NOBODY EVER CHOOSES WHAT TO LEAVE UNDONE; the budget exists to create triage. An engine that silently discards the tail has made the choice instead of the person, which is L1. ⚠ THE UNIT MATTERS: eight INTERACTIONS across five scenes is LAWFUL and was refused before the ruling

### `P30` — a claim survives the season  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'do' is on no row of the verb table

**needs:** a row in verb_table.yaml, ruled before it is added
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids

### `P33` — an act costs more when it is bigger  ·  **UNSPECIFIED**  ·  `S26.3`  ·  by `no-signature`
**what:** act cost beyond budget consumption

**needs:** a cost model; the budget is a FLAT COUNT of acts
**law:** S26.3 -- 'a petition consumes budget LIKE ANY ACT, AND THAT IS THE WHOLE OF THE PRICING'. There is no per-act cost scalar anywhere in Part II, so a cheap act and a ruinous one cost a character the same

### `P35` — a private track of regard runs separately from a public one  ·  **UNSPECIFIED**  ·  `S18.2`  ·  by `no-signature`
**what:** an audience-scoped second standing

**needs:** a second standing scalar, or an owner for an audience-scoped one
**law:** S18.2 -- Sensation is EXACTLY TWO FLOATS and S46.1 makes widening it structural in Godot ('nobody can add a third field to Vector2'). A second, audience-scoped standing has NO CARRIER and S22 gives NO OWNER for one -- and the first standing does not compute either (see P14)

### `P37` — a person's response is a lookup on their own state, not a deliberation  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `probe-model`
**what:** verb 'purge' is on no row of the verb table

**needs:** NOTHING FROM THE DESIGN -- #353 does not name 'purge' as a verb. This is the CALLER'S invention and the gap is the caller's
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids. ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)

### `P38` — an outcome is judged by a referee  ·  **NO-PRODUCER**  ·  `S1`  ·  by `no-signature`
**what:** a GM, referee or adjudicator

**needs:** a named person inside the world, or a rule the engine can evaluate
**law:** THE ENGINE RESOLVES EVERYTHING -- there is no GM anywhere in the shape. S1: 'EVERY ACTION IN THIS GAME IS PERFORMED BY A PERSON'. A 'GM-judged optimal window' has no carrier: it is neither a person's act, nor a Query, nor a licensed clock. Part VIII refuses scene-device machinery for the same reason -- forced dilemmas, letter-versus-spirit compliance and timing windows are DRAMATURGY, what a designer does WITH primitives, not primitives

### `P41` — a precedent is cited to strengthen an argument  ·  **UNSPECIFIED**  ·  `S2 T7`  ·  by `no-signature`
**what:** the argument layer's named faults, and how a cited precedent bears on one

**needs:** the fault roster, and a rule by which a prior Event or Record strengthens a present argument
**law:** T7 says 'the argument layer resolves BY NAMED FAULT, not by a persuasion threshold' -- and the roster of faults is nowhere in Part II. The prior ruling EXISTS as an Event in the log and a person may hold a Claim about it, but no signature relates a cited precedent to a present contest, and S39.4's ladder reads off a MARGIN whose model is also unspecified

### `P43` — a cohort-wide tally is summed across its holders  ·  **FORBIDDEN**  ·  `S22.4`  ·  by `construction`
**what:** resolver-side Query 'cohort_unrest' aggregates per-person tallies ACROSS HOLDERS

**law:** L3 clause 2 -- THAT IS STORED, MONOTONE, NEVER-DECAYING UNREST IN ALL BUT NAME -- worse than the field L3 banned, because the banned field could at least go down

### `P7` — a per-conviction scar  ·  **UNSPECIFIED**  ·  `S22.4`  ·  by `construction`
**what:** the closed `axis` registry L3 clause 1 requires (asked for 'Mercy')

**needs:** a closed roster of axes, and a write-matrix row admitting the increment
**law:** L3 clause 1 permits a monotone counter PER (Person, axis) -- 'legal, since every increment is in the holder's own ledger' -- but ONLY where `axis` is ON A CLOSED REGISTRY. No such registry exists in the chain, and no S30 row admits the write. S54 item 6 adds that the axis must not be spelled `exposure` bare, or it collides with the need scalar

### `P8` — an ambition is blocked with no obstruct verb  ·  **UNSPECIFIED**  ·  `S27/E2`  ·  by `construction`
**what:** verb 'take_seat' is on no row of the verb table

**needs:** NOTHING FROM THE DESIGN -- #353 does not name 'take_seat' as a verb. This is the CALLER'S invention and the gap is the caller's
**law:** §E2 -- the resolver's body IS the table. A verb the table does not carry has no semantics, and inventing them at the call site is the second resolver §27.2 forbids. ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)

### `P9` — an order is the subordinate's own choice  ·  **UNSPECIFIED**  ·  `E2`  ·  by `construction`
**what:** 'dispatch' has a precondition the fold cannot evaluate: 'the named person exists'

**needs:** a predicate in REQUIRES_PREDICATES, or a `requires:` the table states structurally rather than in prose
**law:** §E2 -- `requires` is checked IN THE FOLD. Stated as prose it is the same defect `resolve` had, one column along: a rule the code cannot read

### `W10` — a settlement holds a level of discontent  ·  **FORBIDDEN**  ·  `S10.1`  ·  by `construction`
**what:** Rung.morale assigned -- not a declared field of S10's record

**needs:** a Query over the containment subtree, owned by Nobody
**law:** L3 -- every aggregate is a function, never a field. S22.1 -- if the aggregate is a function it CANNOT go stale and CANNOT be initialised and then forgotten, because there is nothing to initialise

### `W13` — a background quantity decays on a schedule nobody wound  ·  **FORBIDDEN**  ·  `S25.1 / S3-L5`  ·  by `no-signature`
**what:** a fourth clock-driven quantity

**needs:** an author -- a nameable act that wound it, so it can be bribed, delayed, burned, or killed
**law:** S25.1 -- THE THREE LICENSED CLOCKS ARE EXHAUSTIVE: ['matter', 'bodies', 'the confidence of a memory']. Nobody wound any of the three and YOU CANNOT BRIBE SILT. EVERYTHING OUTSIDE THIS LIST NEEDS AN AUTHOR (L5's second paragraph). A quantity that advances on its own with no author is A SHADOW ACTOR -- unbuyable, undelayable, unkillable -- exactly the actor L1 forbids, arriving through a side door. S13.1 is the worked case: an act-DECLARED term does the same job lawfully AND gives the arc handles (bribe the clerk who set the term, burn the record that carries it, kill the man who must renew it)

### `W1x` — wear answers for an unregistered site kind  ·  **UNGRADED**  ·  `S42.2.1`  ·  by `construction`
**what:** wear for site kind 'reliquary' is not registered

**needs:** a per-kind wear row; S22 assigns `wear per site kind` to params
**law:** S42.2.1 -- 'a wear table that returns 20 for an unregistered site kind does not fail -- it answers, plausibly and wrongly, forever'

### `W3` — the world sours a mood  ·  **FORBIDDEN**  ·  `S3-L4`  ·  by `construction`
**what:** (Person, stance) written during MATTER

**needs:** one of ['RESOLVE']
**law:** L4 / S25 -- NO SOCIAL QUANTITY MOVES AT MATTER. 'The world may silt a harbour; IT MAY NOT SOUR A TOWN'S MOOD.' This is the design refusing, not the design failing to say

### `W5` — yield is produced  ·  **UNOWNED**  ·  `S22.3`  ·  by `no-signature`
**what:** season_factor's distribution

**needs:** an owner for the distribution
**law:** S22.3 -- THIS BLOCKS `yield`. `yield` is written ONLY at MATTER (S30, the one single-cell row in the whole matrix) and there is nothing to write, because the distribution that would drive it has no owner
