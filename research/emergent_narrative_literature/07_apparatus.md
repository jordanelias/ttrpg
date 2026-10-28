# The apparatus — a cross-source instrument for vetting an emergent-narrative design

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-10-28 · Lane: IN (cross-cutting) · Written against `15593ac`
## What changes in `engine/season/`: nothing. If this directory were deleted the game would behave identically.

**What this is.** The 168 per-source tests in entries `01`–`06` regrouped by the *design question* they answer, so that where several independent sources converge on one test the convergence is visible. Each row says what to ask, which tests it draws on, what kind of evidence a verdict needs, and what failure it catches. It is the join of the corpus, not a new set of claims: every row is only as strong as the entries it cites, and rows that rest on secondary sources are marked **(S)**.

**Test ids.** `T04.Q1` is the first test of source `T04_juul2002`: the prefix before the first underscore, then `.Qn`. Entries `01`–`06` hold the full wording, with a *Passes if / Fails if / Detects* clause for each. **Row ids** are a gate letter plus the row number (`G6` is gate G, sixth row; `C10` the tenth of gate C); **source ids** are letter plus two digits (`G06` is Hocking). Do not confuse them.

**Evidence classes** (the last column but one): `doc` a design document or spec; `trace` a seeded run log or telemetry; `rater` a reader or rater working to a time budget; `player` observed play; `ablation` a control run with a subsystem removed or replaced by a baseline; `analysis` an analytic computation over content; `tool` the authoring tool itself. **A verdict on a `rater`, `player` or `ablation` row cannot be reached on paper**: without one, record it as `paper`, never as passed.

## How to use it

| if the design claims… | run gates |
|---|---|
| stories emerge from simulation | A, B, C, then D |
| the engine tells the player what happened (chronicle, log, sifting) | D, E, L |
| there is no GM / the world paces itself | F, H |
| choices matter | G, J |
| the world generates content / endless variety | I, then J |
| the experience is engaging or immersive | K, L |

## Gate A — What narrative is claimed, and what delivers it?

*Before testing anything, make the design say which kind of story it promises and through which structure.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| A1 | For each intended story, which of evoke / enact / embed / emerge carries it, and is the authored-versus-rule-generated split stated? | T05.Q1 · T04.Q1 · T04.Q3 | doc | unattributed narrative; progression disguised as emergence; undeclared hybrid structure |
| A2 | Which user role is served: spectator, participant as a character, or author working with the system? Do the affordances and the evidence match that role? | E07.Q1 · E07.Q2 · E07.Q4 | doc | role conflation; authorship pleasure claimed with no tools; misapplied authority across roles |
| A3 | Where does the design sit on each axis: authorial intent (all authored, constrained by a plot graph, or generated), character autonomy and player modelling; are its claims consistent with that position? | E16.Q2 | doc | undeclared hybrid; claims that cannot all hold |
| A4 | Does the plot shape promised fit what the interaction style affords, and can the ideal sequence be failed? | T07.Q1 · T06.Q2 · T06.Q3 · T07.Q3 | doc | interactivity/plot mismatch; story elements presented as fixed while the player can act; ideal-story monopoly; a plot position nobody would want first-hand (Holodeck gap) |
| A5 | Is narrative the point of play or a prop, and does the design's measure of success match? | T07.Q4 · T06.Q4 · G12.Q1 | doc | narrative as end versus instrument confusion; narrative treated as a mechanism when it is presentation |

## Gate B — Is the emergence real?

*A claim of emergence is cheap; these tests ask what would show it false.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| B1 | For each claimed emergent behaviour, can it be derived from one rule, or does it need simulation or strategy to discover? | T04.Q2 | doc | emergence inflation |
| B2 | Is each important outcome derived from the interplay of separately modelled components, and is a stated cause a recorded fact, a state-derived rationalisation, or invented? **(S)** | E17.Q2 · E12.Q3 · E15.Q2 | doc trace | faked emergence; unlabelled fabricated causality; manager-driven loss of expressive range |
| B3 | Do two sessions converge on the same shape because of the goal or a feedback loop? | T04.Q4 · G03.Q3 | trace player | dominant-strategy collapse; positive feedback that flattens tension |
| B4 | Does the same target situation arise through different causal histories and casts across seeds? | E04.Q2 | trace | a hidden script behind a situation |
| B5 | Are nominal and meaningfully different outcome counts reported separately, and can two world-states following one choice be reconciled coherently? | T03b.Q1 · T07.Q2 | doc trace | cosmetic variety; permutation without coherence (the Aleph fallacy) |
| B6 | At which level of the plot / action-sequence / behaviour hierarchy is variation generated? | T01.Q1 | doc | emergence at the wrong level |

## Gate C — Does the system supply story material?

*Emergent narrative needs raw material with stakes; these tests ask whether the simulation produces it at all, and how often.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| C1 | Do characters have conflicting drives, specified relationships and events outside their control, and does a play log then yield a recognisable story at a measured rate? | T01.Q2 | trace rater | unmeasured emergence rate |
| C2 | Can the design name its target situations (roles with conflicting aims, not plots), show each is reachable, and report how often each occurs? | E04.Q1 · E04.Q3 | trace | reachability claimed without evidence; recurrence eroding eventfulness |
| C3 | Can conflict potential be computed from content before any run, with reachable conflict distinguished from merely existing, and each action's effect on pairs of ideals classed? | E05.Q1 · E05.Q2 · E05.Q3 | doc analysis | unmeasured conflict supply; conflict-free content masquerading as drama |
| C4 | Do events read and write a small shared set of entity properties, and do independent subsystems read each other's recorded history? | E15.Q1 · E02.Q3 | trace | disjointed event sequences; visible seams between subsystems |
| C5 | Does each generated actor carry a seed that gives random events a recognisable character? | E15.Q3 | doc | voiceless randomness |
| C6 | In an emergent mode, which authored ingredients make narrative likely (conflicting drives, legible objects, consequence traces), and which are missing? | T05.Q3 | doc | sandbox without hooks |
| C7 | Do the simulated domains include stakes and motivations at a granularity players care about, with components rich enough to carry meaning? **(S)** | E12.Q4 | doc | boringness; granularity extremes |
| C8 | Are the entities players should care about few and persistent enough to remember, with readable labels that carry small consequences? **(S)** | G13.Q1 · G13.Q2 | doc player | diluted attachment; labels without consequence |
| C9 | Which story-bearing facts are modelled, and which exist only in the player's head? Do incidents have duration and overlap? **(S)** | G14.Q2 · G14.Q4 | doc | narrative superimposed on a mechanically empty simulation; one-shot events that cannot compound |
| C10 | Does the output offer evocative, underdetermined hooks a player can extrapolate from, and which story types does it support? | E11.Q1 · E11.Q2 | rater | output that is over-determined or inert for narrativization; log-reading only |

## Gate D — Can anyone find and retell the stories?

*Ryan's argument, as reported by Short, is that raw simulation output rarely has story structure; this gate asks what stands between output and a telling.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| D1 | Is there an explicit stage that selects, orders and frames events as a telling, with a stated criterion? Does a retelling keep the events and say what it loses? **(S)** | E12.Q1 · T06.Q1 · E07.Q3 | doc | raw simulation trace presented as narrative; translation loss ignored |
| D2 | Can a designer ask a new question of the event record without new code; can a pattern match interleaved events and the absence of an event; can a non-match be debugged? | E08.Q1 · E08.Q2 · E08.Q3 | doc tool | authoring bottleneck; brittle literal-sequence recognition; opaque sifting |
| D3 | Can a developing sequence be recognised while open; is the set of in-progress candidates bounded; is the temporal scope of each constraint stated; can the sifter run without modifying the generator? | E09.Q1 · E09.Q2 · E09.Q3 · E09.Q4 | doc trace | retrospective-only recognition; unbounded candidates; temporal-scope ambiguity; coupling |
| D4 | When many matches exist, what decides which are surfaced: is the rule better than random in a blind comparison, measured against matches of the same pattern, discounting rarity the world's own rules expect? | E10.Q1 · E10.Q2 · E10.Q4 | rater | unranked output; context-blind novelty; correlated-unlikelihood false positives |
| D5 | For a major outcome, can the engine name the finite set of prior conditions that enabled it, as a stored record? **(S)** | E12.Q2 | doc trace | diffuse causality |
| D6 | Does the system itself retell, faithfully to recorded events, and is the viewpoint of each telling nameable? | E01.Q4 · T11.Q2 | doc trace | system-side retelling that fabricates; events with no one positioned to experience them |
| D7 | Given a time budget and only the system's records, can a reader who did not build it find and write a tellable account? | E04.Q4 | rater | story potential that exists only in the author's head |

## Gate E — Is the process visible enough to earn its complexity?

*Wardrip-Fruin's Tale-Spin and Eliza effects are the corpus's sharpest overbuild questions; Sylvester's argument (as reported) is the same in practitioner terms.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| E1 | What fraction of significant internal events reach the player in any form? Does the player see evidence that past events changed later behaviour? | T13.Q1 · E08.Q4 · E10.Q3 | doc player | Tale-Spin effect: capability the audience cannot see |
| E2 | Does the surface imply more intelligence than the process has? Trace the three most impressive outputs to their source. | T13.Q2 | doc trace | Eliza effect |
| E3 | When a component fails, does the visible error reveal a systems cause, and is each such failure traceable? Can a player learn the model by experiment? | T13.Q3 · T08.Q3 | trace player | undiagnosable breakdowns that hide design gaps; expectation gap |
| E4 | Does every depicted trait correspond to an input of the decision process? Does every simulated variable have a player-visible effect or a one-layer-down quantity that does? | T13.Q4 · E17.Q1 | doc | inert depicted inner life; worthless-noise complexity |
| E5 | Does each subsystem have a stated real-world referent that was consulted when it misbehaved, and can a designer change a parameter and see the response in a short loop? | E17.Q3 · E17.Q4 | doc tool | unanchored model; overplanned, un-iterated model |
| E6 | Can the player observe the causal chain at the time scale and attention they actually have, and tell what hidden state their actions changed? **(S)** | G14.Q1 · T03b.Q3 · G13.Q3 | player | invisible simulation depth; opaque state; hidden-information failure |
| E7 | Ablation: with one subsystem disabled or replaced by a baseline, are stories measurably harder to tell or less coherent? | E11.Q3 | ablation rater | a narrative mechanism that does nothing the player can use |

## Gate F — Pacing and direction without a game master

*Where a design says there is no GM, these tests name the GM functions and ask what carries each.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| F1 | Does the story-steering component have a defined set of intervention types with stated triggers, and is the plot provisional with a logged rule for rewriting it? | T12.Q1 · T12.Q2 | doc | undefined narrative control; brittle fixed plot |
| F2 | Which steering functions are human out-of-character negotiation, and are they replaced or silently dropped? Is enjoyment monitored, or is the inability stated? | T12.Q3 · T12.Q4 | doc | lost GM functions; unfounded claims of GM equivalence |
| F3 | Is there an explicit pacing target or tension variable with named inputs, a decay rule and thresholds that a log can show? | T03a.Q1 · G10.Q1 | trace | pacing asserted but not mechanised |
| F4 | Is there an alarm for the pacing mechanism running out of suitable content, and a designed low-pressure phase after a peak? | T03a.Q2 · G10.Q2 | trace | content starvation hidden by a selector that always picks something; monotone escalation |
| F5 | Does pacing act on frequency or on difficulty (stated)? Is the proxy for player state validated? Does an event generator damp severity when a run goes badly, and is that disclosed? **(S)** | G10.Q3 · G10.Q4 · G14.Q3 · G13.Q4 | doc trace | rubber-banding disguised as pacing; unvalidated stress proxy; undisclosed director behaviour |
| F6 | What happens when the planned continuation is made impossible, and is the criterion for a good trajectory written down? | E16.Q1 · E16.Q3 | trace | unhandled boundary problem; steering with no stated quality model |
| F7 | If the system selects scenes from world state, is there a source of dramatic shape outside that selection? | G07.Q3 | doc | accidental ending; dead or dominant content |

## Gate G — Agency and choice

*Agency here is the Mateas / Wardrip-Fruin account: formal reasons and material affordances matched, not freedom of choice.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| G1 | At each decision point, what does the world afford and what reasons does the story give to prefer one action? | T02.Q1 · T08.Q1 | doc | formal/material imbalance |
| G2 | Does an action change what the player intended, predictably; does a failed plan leave the player something to do? | T02.Q2 · T08.Q4 | player | false agency; agency broken by plan-failure resets |
| G3 | When the player tries something outside the model, does the fiction continue and does the surface correspond to something in the model? | T08.Q2 | player | surface divorced from model |
| G4 | What share of sampled actions gets a specific immediate response, a generic one, or none; and do acts shape the arc as well as the moment? | T03b.Q2 · T03a.Q3 | trace player | unmeasured local agency; agency only local (hollow) or only global (unreadable) |
| G5 | For named choices: framing, options and outcomes stated? How many choices are false, flavor or delayed? Does a choice survive a second, analytical playthrough? Is influence separated from agency? | T10.Q1 · T10.Q2 · T10.Q3 · T10.Q4 | doc player | blind choices; choice inflation; false choice fragile under replay |
| G6 | Do plots differ across early choices in ways not traceable to visible branch points, and does each run still end coherently? Can the player see why NPCs act as they do? | T02.Q3 · T02.Q4 | trace player | agency/variety conflict unresolved; unreadable agents |
| G7 | Where is player choice over means and goals, and is it informational rather than controlling? | G01.Q2 | player | autonomy thwarting |

## Gate H — Memory, persistence and the world's traces

*Whether history is stored somewhere a player or an agent can meet it.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| H1 | What story state survives save/restore, undo or reload; can consequences be skipped without coherence loss? | T11.Q1 · T01.Q3 | doc | undo-induced loss of narrative coherence |
| H2 | Do non-user characters remember and respond to the user's behaviour in role; what tells the player which behaviour helps a story emerge? | T11.Q4 · T01.Q4 | player | absent social presence; user-role gap |
| H3 | Which events occur off-stage, and how do they reach the user (gossip, news, recap)? | T11.Q3 | doc player | off-stage activity that is invisible or uncomputed |
| H4 | If a player misses or reorders any one element, is the essential information still delivered elsewhere? | T05.Q2 | player | single-point information loss in non-linear play |
| H5 | Do past events leave readable traces that point to a recoverable cause, change what the player or an agent does next, persist, and can be read by non-player agents? | T05.Q4 · G04.Q1 · G04.Q2 · G04.Q3 · G04.Q4 · G05.Q3 | doc player | invisible history; set-dressing standing in for history; one-way trace system; unsourced scenery |
| H6 | Is the player oriented within moments, are world rules consistent, and do places visibly change when the player returns? | G05.Q1 · G05.Q2 · G05.Q4 | player | orientation failure; world-rule inconsistency; static world |

## Gate I — Variety and the range of generated output

*Statistical uniqueness is not perceived difference (Compton); range has to be measured, not asserted (Smith & Whitehead).*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| I1 | Per artifact kind, are good outputs and deal-breakers written in checkable terms, and does the chosen method have the skills the design needs? | P01.Q1 · P01.Q4 | doc | unspecified success criteria; method-requirement mismatch |
| I2 | Show 20 consecutive outputs to someone who has not seen the generator: can they tell them apart and say how? | P01.Q2 | rater | the oatmeal problem: unique in fact, the same in perception |
| I3 | For each constraint, is it enforced by construction, by generate-and-test, or not at all, with what rejection rate? Is failure tolerance matched to whether the content is necessary? | P01.Q3 · P03.Q1 | trace | unenforced constraints; catastrophic failure on necessary content |
| I4 | Run at volume and score outputs on at least two metrics that are not generator inputs; is any intended region empty; was the histogram regenerated after each tweak; are metrics validated against perceived differences? | P02.Q1 · P02.Q2 · P02.Q3 · P02.Q4 | trace rater | unmeasured output range; holes in expressive range; proxy-metric overreach |
| I5 | What does the evaluation function compute? Can the representation reach everything promised, with small changes producing small differences? Is randomness chosen and reproducible? | P03.Q2 · P03.Q3 · P03.Q4 | doc trace | evaluation-function mismatch; unreachable regions; uncontrolled variation |
| I6 | If the generator is justified by replayability, which dynamic does it actually give; can a player learn a mapping from action to output; is the generator core, framing or decorative; at what level does repetition show? | P04.Q1 · P04.Q2 · P04.Q3 · P04.Q4 | doc player | unanalysed replayability claim; misplaced load on generated content; perceptible repetition |
| I7 | What fraction of authored content does one run reach? Do two sessions from the same start give players something to compare? Is coherence tested on players who see several fragments together? | T03a.Q4 · T03b.Q4 · E01.Q3 · E15.Q4 | trace player | volume mistaken for variety; low variance that kills comparison; author satisfaction mistaken for reception |

## Gate J — Content structure and authoring burden

*How content is selected, and what each new piece costs.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| J1 | Per content unit: a stated selection rule (player-chosen, system-chosen, system-routed)? Does writing a new unit raise or lower the burden on existing ones? | G07.Q1 · G07.Q2 · G09.Q4 | doc | undefined selection structure; combinatorial explosion; unreviewed unseen content |
| J2 | Can every unit be stated as content + prerequisites + effects on named state; can one be added without editing others; is content gated by route; can play performance change the state units test? | G11.Q1 · G11.Q2 · G11.Q3 · G11.Q4 | doc | opaque unit state; poor extensibility; time-cave cost; story disconnected from play |
| J3 | Which pattern does the structure follow and does the claimed experience match it? Where branches rejoin, do later units read earlier choices? For trunkless designs, is the no-through-line claim counted against content volume? | G09.Q1 · G09.Q2 · G09.Q3 | doc trace | choice illusion; obliterated consequence; collapse to a linear system |
| J4 | How does authoring cost grow with decision points, and who maintains progression state: the engine or the author by hand? | E16.Q4 · G07.Q4 | doc | authoring intractability; bookkeeping debt |

## Gate K — Engagement, and fit between rules and story

*What the player is meant to feel, and whether mechanics and narrative agree about it.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| K1 | Is there an observable route to competence (graded challenge, legible feedback), relatedness with real or simulated others, and, if immersion is claimed, a play-level basis for it? | G01.Q1 · G01.Q3 · G01.Q4 | player | competence starvation; immersion asserted without a play-level basis; unsupported relatedness claim |
| K2 | For each mechanic, can the design name the dynamic it should produce and the aesthetic that serves; are target aesthetics stated; is there a recorded tuning step? | G03.Q1 · G03.Q2 · G03.Q4 | doc | feature-driven design with no experiential target; untuned design asserted as balanced |
| K3 | Do the rules reward what the story praises; does the narrative require anything the mechanics let the player decline; is commentary on the player consistent with what they were shown; does a moral choice have different mechanical payoffs? | G06.Q1 · G06.Q2 · G06.Q3 · G06.Q4 | doc player | ludonarrative dissonance; forced-choice override; choice without consequence |
| K4 | How much authored content is consumed per hour; does the system generate new problems without new content; is feedback proportionate to the problem solved? | G12.Q2 · G12.Q3 · G12.Q4 | doc trace | content-bound design; feedback-heavy, problem-light design; exploitative feedback |

## Gate L — Evidence discipline for any verdict above

*Retelling-based evidence is easy to over-read; these tests govern how a verdict on gates A-K is reached.*

| # | ask | tests | evidence | catches |
|---|---|---|---|---|
| L1 | Are retellings classified by stance (celebratory, neutral, ironic or critical) and not only counted; are in-joke and narrative-length retellings reported separately; is each incoherent output given a recorded disposition? | E02.Q1 · E02.Q2 · E02.Q4 | rater | retelling volume mistaken for success; incoherence excused as emergent charm; sampling bias |
| L2 | Does retelling frequency control for community size and novice acclimation, and does any retelling exist at all that describes events the system itself produced? | E11.Q4 · E01.Q1 | rater | confounded retelling metrics; tellability claimed without observed retelling |
| L3 | Can each retold event be located in the code, story or discourse layer, so credit is not misallocated between system and player? | E01.Q2 | rater doc | credit misallocation |
| L4 | Are stated design goals encoded as checkable properties and verified, rather than described? | E05.Q4 | doc analysis | unfalsifiable design intent |
| L5 | Is each source's authority checked against the user role under review (participant or author)? | E07.Q4 | doc | misapplied authority across the participation/authorship divide |

## Where the sources disagree

A reviewer who cites one source here as settled authority has chosen a side. These are the splits that matter, each with the gate that tests it.

| question | one position | another position | gate |
|---|---|---|---|
| Where does a game's story live? | Juul (T04): storytelling ambition lives in progression; emergence is a structure of variation. | Aylett (T01, T11): narrative can emerge bottom-up from interacting characters. Ryan, as reported by Short (E12, S): raw simulation output rarely has story structure, so curate. | A, B, D |
| Does a retelling prove success? | Eladhari (E01): retellings are a fourth narrative layer and their occurrence indicates a well-designed system. Kreminski et al. (E11) echo this, offering retellings as an evaluation method with small samples acknowledged. | Sych (E02): a significant subset are themselves critical, mocking incoherent output, so retelling is not simply a marker of quality. | L |
| Should anything steer the story? | Façade (T03a, T03b) and Riedl & Bulitko (E16): a manager sequences content toward a target. | Ryan, as reported (E12, S), is wary of bending the simulation; Short reports the argument without taking the hard line. Aylett (T01) scripts no plot and builds from character behaviour. | F, D |
| How much simulation should show? | Wardrip-Fruin (T13): a hidden process offers an audience less than a visible error, so make the process show. | Sylvester, as reported (G13, G14, S), and Adams (E17): build only what the player can perceive; Adams says to operate at the level of what the player sees or one layer below. The positions converge on perceivability and differ on the remedy. | E |
| Is narrative a mechanic? | Koster (G12): narrative is a form of feedback, not a mechanic. | Mateas (T02, T08): story structure is a formal constraint that gives reasons to act. Hocking (G06): when ludic and narrative contracts conflict, both suffer. | G, K |
| Does replayability justify generation? | Juul (T04): emergence games are replayable by structure. | Smith (P04): replayability is too broad and incomplete a justification. Compton (P01): the commonest failure is output that is unique but perceptually the same. | I |

## Crosswalk to the 26–28 October working survey

Jordan's working survey (a file outside the repository: `critical_apparatus_survey.md`, Part A tests **N1–N15**) was supplied mid-session and used as the baseline. This corpus read its sources independently and did not see its entries until after the readers finished. *Supported* means an entry here contains a test of the same shape, from an independent reading; it does not mean every sentence of the two accounts agrees.

| survey test | in this instrument | status |
|---|---|---|
| N1 which hooks are emergent vs embedded progression | A1 (T05.Q1, T04.Q1, T04.Q3) | supported |
| N2 share of runs that yield a recognisable story | C1 (T01.Q2); extended by C2 (E04.Q3) | supported |
| N3 identity, relationships, precipitating event, exogenous events, affect | C1 (T01.Q2); C3 adds computing conflict potential before any run (E05) | supported, extended |
| N4 can the player assemble events into an account | D1, D6 (E12.Q1, E01.Q4, T11.Q2); A2 separates the player's role (E07) | supported, extended |
| N5 persistence, no restart, agents that remember | H1, H2 (T11.Q1, T11.Q4, T01.Q3) | supported |
| N6 what routes off-stage events to the player | H3 (T11.Q3); E6 (G13.Q3, S) | supported |
| N7 which engine object carries each GM function | F1, F2 (T12.Q1–Q4). T12's own base is one Game Master | supported, narrow |
| N8 authored vs experienced content; meaningful variation | I7, B5 (T03a.Q4, T03b.Q1, T03b.Q4, T07.Q2) | supported |
| N9 can the player read hidden state | E6, E3, G6 (T03b.Q3, T08.Q3, T02.Q4, G14.Q1) | supported |
| N10 if a process were simpler, could the audience tell | E1, E2, E7 (T13.Q1, T13.Q2, E11.Q3) | supported; E7 supplies the ablation |
| N11 ablation plus retellings | E7, L1, L2 (E11.Q3, E11.Q4, E02.Q1, E02.Q4) | supported; E02 adds that retellings can be ironic |
| N12 does authored narration crowd out player-made stories | no source here tests displacement directly; nearest are T05.Q3 (C6) and G13.Q4 (F5, S) | **weakly supported**; the survey cites Jenkins quoting Lynch |
| N13 aesthetics-first scoping; loops that flatten tension | K2, B3 (G03.Q1–Q4) | supported |
| N14 is a recogniser or sifter surfacing storyful moments | D1–D4 (E12, E08, E09, E10) | supported, and far more developed than the survey's abstract-only entry |
| N15 dominant strategy and the sessions it produces | B3 (T04.Q4, G03.Q3) | supported |

**Beyond N1–N15** this instrument adds gates I (generated variety), J (content structure and authoring burden), K (engagement and rule/story fit), most of D, F and G, and the evidence-discipline gate L. The survey's overbuild (CODE) and human-capacity (COG) parts are outside this corpus.

## Tests held in the entries but not grouped above

Listed so that nothing is silently dropped. They remain valid per-source tests; they are omitted here because another row already covers the same question or the test is source-specific.

(none)
