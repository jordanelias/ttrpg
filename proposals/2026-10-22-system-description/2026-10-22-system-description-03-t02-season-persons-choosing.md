# Tutorial: The season, the person and how an actor chooses — what a turn is, who acts, and how to predict what any person will do with it

Repo `jordanelias/ttrpg` at HEAD `a4ca9a5`; **revised in round 3 against `51d7b05` (PR #494 landed between) and the precedent suite
(`research/game_precedent_suite/`)**. §0a and the round-3 edits were opened at `51d7b05`; every other line cite in this file is as of
`a4ca9a5`, and `### Round-3 corrections` (end of §8) lists the ranges PR #494 moved. All code paths are under `engine/season/` unless
they start with another top-level directory. "The realm" is `harness/populated.py::build_realm(seed)`; "the control run" is
`ctl/realm_seed{0,1,2}_2seasons.txt` beside this file (2 seasons per seed). "My probe" means this audit's throwaway scripts, which are
not committed (§9).

## 0 Before you start

**The frame.** In the code there is no player character and no GM. Every person is a chooser that spends a scene-action budget each season
(5 at base, plus 1 per live hold) on acts drawn from a closed table of verbs. A plain scene costs one action and carries one act; an
extended scene costs two and carries up to three; the driver releases one scene per round over five rounds. "You" in this tutorial is
the acting person: a player's character if one is seated later, an NPC today. So the tutorial teaches (a) what an actor can do,
(b) what the rules do with it, and (c) what an actor has to arrange to reach a goal.

**What you need from other subsystems.** Nothing upstream: this is the turn structure every other subsystem plugs into. Seven verb
rows hand a contested act to another subsystem for a degree: `fight`/`accept` to personal combat, `march` to mass battle, and `tell`,
`argue`, `speak`, `determine` to the social-contest roll. Three inquiry rows (`research`, `examine`, `surveil`) are graded by the
same roll (`rosters.yaml` `contest_subsystems`, `graded_inquiries`). Those resolvers are taught in their own tutorials; here they are
black boxes that return a degree.

**Status: RUNS-IN-LOOP.** The season loop, the person record, the chooser and 22 verbs that produce non-refusal outcomes at seed 0
all execute in `SeasonDriver.season` over the realm. Two qualifications. The chooser is built only by harness code: `make_chooser`
has no call site in `loop/`. And several of its terms are RUNS-IN-LOOP **at control**, which means they run but are inert at the
shipped values: scar weight shift, confliction damping, declared intent, and the urgency term. Their non-control arms (the swept
values) are TESTS-ONLY. The conviction crisis is RUNS-IN-LOOP per seed: 5 folds at seed 0 and 3 at seed 2, all at tick 1, and none at
seed 1 in two ticks (§9, probe7). Grades follow the errata rule (G1): a refusal firing is not the verb executing. Execution is
stated per seed.

## 0a How it plays

Precedent forms used for shape: `research/game_precedent_suite/tutorials/T01_realm.md` (Old World), `T13_koei.md` (Genghis Khan II) and
`T16_managers_narrative.md` (King of Dragon Pass, Six Ages, Football Manager 26). Figures are seed 0 unless a seed is named; every code line
in this section was opened at `51d7b05`. The as-built text comes first, then a `[PROPOSED]` block.

**Setup choices.** The one input is the world seed. `harness/populated.py::build_realm(seed)` seats 83 persons (46 named, 37 cohorts) and
32 offices, all held at build, and mints 64 OUGHT Propositions: 46 personal wants (`prop_npc_*`), 6 faction creeds (`fac_*`) and 12
organization goals (23 of the 35 `goals.yaml` rows are `orientation` and mint nothing; `harness/populated.py:473-476`, `goals.yaml:1-30`).
Its other parameters (`cap`, `from_roster`, `goals`, `goals_complete`, `:629-630`) are builder switches, not choices. There is no
difficulty, nation or character pick; the remaining knobs are fixture arms (temperature `data/fixtures.py:286`, scar shift `:707`,
confliction `:715`), swept controls rather than choices. A client that registers a person in `overrides` chooses for that person at each
deliberation. Its callback receives the Person, a View (the last 12 own claims and the question), a Sensation (two scalars, subsistence and
standing; `state/carriers.py:388`), the budget query and `auto`, the shipped chooser (`harness/play_surface.py:14-19`). It may return any
of the 47 resolvable verbs with any payload. DELIBERATE raises on an over-budget return (`loop/deliberate.py:202`), a scene of more than 3
acts (`:220`) and an act whose actor is someone else (`:281`); a verb whose precondition the fold cannot evaluate (`exchange`) raises
`Unspecified` and aborts the season (`loop/resolve.py:282-290`).

**The loop (one tick).** 1 CALENDAR: dates due this tick fire. 2 MATTER: terms mature (`loop/matter.py:294-304`), claims lose 5 confidence
(errata G8), cohorts draw food, sites yield and wear (§2.1); hunger, ageing and illness are coded and ship at 0 (`matter.py:513-520`,
`:549`; `data/fixtures.py:594, 606-607`). 3 Five rounds (`loop/driver.py:449-456`), each DELIBERATE (every person answers one question and
returns scenes; nothing is written), RESOLVE (all released acts in stratum order), ENCOUNTER (declared marches fought) and WITNESS (events
become claims). 4 CENSUS. 5 `tick += 1` (`driver.py:445-456, 514-519`; §2.1 gives the step order). Everything is automated: persons not in
`overrides` are chosen by `make_chooser`; nothing pauses and nothing waits for a human.

**The choice menu.** Every act costs its share of a scene: 1 alone, 2 for a scene of two or three acts (`decision/choose.py:643-658`;
`data/fixtures.py:488-489`), against a budget of 5 + 1 per live hold − body bands − travel legs (`decision/budget.py:57-61`), at most one
scene per round (`loop/deliberate.py:252-259`). A person picks a verb whenever it is formable on the question's subject; which one comes
first is the pursuit term when the subject is shared and the stance term when it is not, then noise at τ = 0.1 (`choose.py:130-151`,
`:376-392`). The full menu is §4; the verbs a person reaches most:

| verb | cost | effect | when a person picks it | ctl att/ok s0 · s1 · s2; grade |
|---|---|---|---|---|
| `utter` | scene share | mints a Proposition and a maker's hold (+1 budget) | any question; never refused | 39/39 · 39/39 · 49/49; RUNS-IN-LOOP |
| `create_record` | scene share | a Record you hold (+1 budget) | any question; never refused | 87/87 · 88/88 · 89/89; RUNS-IN-LOOP |
| `commit` | scene share | a membership edge to a Proposition | formed mostly on persons, then refused | 61/0 · 56/1 · 63/1; RUNS-IN-LOOP at s1, s2 |
| `release` | scene share | closes a tenure of your own | toward a referent you hold an edge to | 45/3 · 44/5 · 46/3; RUNS-IN-LOOP |
| `forgive` | scene share | deletes your negative stance rows on the subject | only toward someone you hold a grudge row on | 1/1 · 2/2 · 2/2; RUNS-IN-LOOP |
| `oblige` | scene share | a 4-season service edge to a seat | on a seat your ledger names | — · 24/22 · —; RUNS-IN-LOOP at s1 |
| `move` | scene share, then −1 budget per leg | moves your `contain` | toward a referent with a path | 42/16 · 35/17 · 40/12; RUNS-IN-LOOP |
| `tell` | scene share, contested | the hearer receives your chosen claim | a co-located hearer and a claim to say | 23/4 · 25/7 · 19/6; RUNS-IN-LOOP |
| `petition` | scene share | a petition Record you hold (+1 budget) | `to` a living person | 42/14 · 31/7 · 34/11; RUNS-IN-LOOP |
| `fight`, `accept` | scene share, contested | Felled / Wounded / Untouched on the subject | any living referent; `accept` needs no challenge | 7/4 and 18/11 (s0); RUNS-IN-LOOP |
| `train`, `tend` | scene share | +1 capability; body to 1000 | a co-located person | 0 ok in all seeds; TESTS-ONLY |

("att" counts acts that reached the fold; contested acts refused at admission are not counted, trap 9.)

**First tick, step by step (Sæmund Haelgrund, `p_npc_004`, seed 0; the numbers are §3's, whose control run is byte-identical at `51d7b05`).**
1. Build: budget 5 + 1 hold (his seat) = 6; the realm's budgets are 5 for 52 persons, 6 for 27, then 7, 10, 10 and 13 (round-3 probe).
2. MATTER at tick 0 changes nothing for him (no stores at his rung, urgency 0).
3. Round 0: his ledger is empty, so his question is his most salient `need`: the Restoration's leader Yrsa (salience 0.95055;
   `queries/world_q.py:2295-2310`).
4. 30 of 46 verbs survive the gates on Yrsa; the stance term (−8) is common to all, so pursuit gaps and noise order them: the sampled head
   is `petition, open_case, create_record`.
5. Packed 2 + 2 + 2; round 0 releases the first scene, spending 2 (`loop/deliberate.py:252-259`).
6. RESOLVE: Arnlod's `accept` on Yrsa (contested_physical) runs before Sæmund's social acts and Fells her; his `create_record` lands (+1
   hold), `petition` is refused (no living `to`), `open_case` is `case.unauthorized`.
7. WITNESS: he holds a firsthand claim about Arnlod, the referent of his personal want, so round 1 asks a tier-0 question about Arnlod
   (`queries/world_q.py:2217-2341`); `open_case` on Arnlod lands, `train` and `commit` are refused.
8. Over five rounds he releases 4 scenes, spends 8 actions, resolves 11 acts with 3 non-refusals and ends the tick holding 3 Records:
   budget 9 at tick 1 (round-3 probe: 9). Realm-wide in that tick: 676 acts formed, 535 reached the fold, 83 → 78 persons alive.

**What changes later.** Budgets climb with paper (mean 5.57 → 6.41 → 7.69 over two ticks; 11 of 74 above the 10-action release ceiling
after tick 1). Convictions fold at tick 1 (5 at seed 0, 0 at seed 1, 3 at seed 2). Seats empty and some stay empty: 8, 7 and 10 seats
are vacated in two seasons (8, 6 and 10 still vacant; one refill, in seed 1), the King (`p_npc_020`) is dead after the first season at all
three seeds, and seven null-conferral seats cannot be refilled. Ledgers fill (13 of 74 at the 200 cap, ctl). In the natural run nothing is
founded or built and no field is fought (ctl `field.*` 0; a hand-built `march` at a settlement does run the battle oracle in the loop).
Persons acquire no skills (`train` 0 ok) and their pursuits never move (scar shift 0, `data/fixtures.py:707`).

**Failure and ending.** None for the world. The season returns `endings` (`world_q.endings_reached`, a read added by PR #494; `loop/driver.py:518,
532`) over two `rosters.yaml: endings` rows (`peninsular_sovereignty`, the victory row, and `theocracy`; `rosters.yaml:2494-2552`); the realm
as built reaches neither (`endings` was `[]` after both ticks at seed 0), and nothing halts on it, so the loop runs as many ticks as its
caller asks. A person ends only by being Felled; MATTER kills nobody at shipped values (errata G9). No goal is ever met, because no code
tests one (`goals.yaml:11-12`: a goal "never acts, and nothing aggregates"). A seated person has no continuation: `succeed` is not
resolvable (§7).

**Consequential vs cosmetic choices.**
- Consequential: whom the question puts in front of you (tier, then salience); your stance toward that subject, which outweighs values by
  one to two orders of magnitude (§2.4); how many holds you keep (every Record and Proposition is +1 budget, up to the ceiling);
  co-location for `tell`, `give`, `tend`, `train`; the stratum order, which lets a movement or a duel change the world before your social
  act is checked.
- Cosmetic or inert: pursuit gaps under about 0.1 (reversed one time in four, §2.5); urgency (the same for every candidate); the value
  term of the 13 uncelled verbs; a cohort's order (pure noise); the confliction damper and the scar shift (both at control).
- Wasted by construction: whole families formed on the wrong class of subject (`work` 77/0, `migrate` 81/0, `commit` on persons); a
  budget above 10.

**[PROPOSED] Playing it as proposed.** IN-46: the driver suspends at ENCOUNTER for a played fight (`workplans/valoria_master_workplan_v9_part4.md:32-34`);
IN-47: creation is "a cast entry the world-gen builder seats" (`:39-41`; D-2 ruled yes, the design held PROPOSED); REM-21..25 and REM-2C
stamp right-class referents (RB-2a); L1-6 option B removes urgency (REM-44); D-V6 adds a contents-aware value term; J-T1 attributes. None
is built; D-2 ruled the two RB-3 designs to proceed (errata G16). §7 lists the waits.

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| **season** (tick) | one call to `SeasonDriver.season`, advancing `w.tick` by 1 | 7 steps, 4 write barriers, 5 rounds | `loop/driver.py:370-528` (step calls `:447-515`) |
| **round** | one DELIBERATE → RESOLVE → ENCOUNTER → WITNESS pass inside a season | `rounds = scene_budget` = 5 | `loop/driver.py:449-456` |
| **person** | the only kind of actor: a named individual (weight 1) or a cohort (weight > 1) | realm: 46 named + 37 cohorts = 83 | `state/carriers.py:655` |
| **cohort** | one `Person` standing for the people of one settlement rung | 37 rows, `weight: 2`; no pursuits, no stance rows | `cohorts.yaml`; probe (§9) |
| **pursuits** | what a person wants: weights over 15 named pursuits | community … wealth; **not normalized** (Sæmund's sum to 1.31) | `data/cast.py:188-218` (from `references/npc_registry.yaml`); `data/pursuits.py:60-89` |
| **axes** | the 7 bipolar value axes pursuits are projected onto | 15×7 matrix `pursuit_projection` | `rosters.yaml` `tables.pursuit_projection`; `data/pursuits.py:60-89` |
| **alignment cell** | how a verb sits on one axis | values in [−1, +1]; 40 of 53 verbs celled, 13 uncelled | `rosters.yaml` `tables.alignment`; `data/verbs.py:1663-1672` |
| **conviction** | intensity 0–5 per religious/civic affiliation (5 affiliations) | `solmund_orthodoxy` incompatible with 3 others | `data/affiliations.py:38-113` |
| **stance** | rows `(referent, valence −5..+5, weight 0..5)` saying whom you favour | `stance_toward` = Σ valence × weight, max 25 | `queries/person_q.py:68-77`; `data/cast.py:372-381` |
| **scar** | count per pursuit or affiliation, raised in witnesses of an act that violates a held element | shift at 2 (dormant), crisis at 3 | `loop/resolve.py::_scar_witnesses`; `queries/person_q.py:580-581` |
| **conviction crisis** | at scar ≥ 3 on an affiliation, it folds into an incompatible heir or is destroyed | RESTABILISE branch not built; folds observed: seed 0 5, seed 1 0, seed 2 3 (all tick 1) | `queries/person_q.py:680-720`; probe7 |
| **ledger** | the person's own beliefs: a list of `Claim`s | cap 200; confidence starts at 100 (or the teller's), is lowered by refraction for witnesses other than the actor (gain 0.5), then −5 per tick at MATTER | `loop/witness.py:234-242`; `data/fixtures.py:231,293` |
| **claim** | one belief: `subject, predicate, value, confidence, source, chain, doer` | sources firsthand / told_by / inferred … | `state/carriers.py:291` |
| **body** | integer condition, 1000 = whole | floors 800 / 500 / 100 cut the budget | `decision/budget.py:64-83` |
| **tenure** | the one edge type, owned by its subject | kinds `knot, hold, commit, tie, ban, oblige, contain, reside, succeed, detain` | `state/carriers.py:77` |
| **hold** | a tenure of possession: a seat, a territory, a Record or a Proposition | every live hold adds 1 to the budget; minted by `create_record, issue, open_case, petition, survey, forge, utter` (and `conceal`'s cover Record) | `decision/budget.py:57-58`; `loop/effects_information.py:125-139` |
| **Rung** | one node of the place/polity ladder: person, hearth, community, settlement, territory, province, duchy, realm | a Rung owns stores and yield; aggregates are queries | `state/carriers.py` |
| **Record** | a document carrier: text, dispensation, petition, works, faction_sheet, cover | possessed through a `hold` | `state/carriers.py` |
| **Proposition** | an immutable utterance with a **mood** (OUGHT, HOLDS, WAR) | made only by `utter` or at world-gen | `loop/effects_information.py:1010-1034` |
| **Office / purview** | a seat with remit acts; its purview is its rung plus everything below | `remit:` rows check the seat's grants and purview | `queries/faction_q.py:157-177` |
| **"with"** | the relation "the two persons are at the same place" | `place_of(a) == place_of(b)` | `queries/world_q.py:2717` |
| **commit** | membership/adherence edge to a Proposition | a faction *is* its Proposition plus its commits | `queries/world_q.py:1365` |
| **ambition** | a live `commit` to an OUGHT Proposition | creed `fac_*`, org goal `goal_*`, personal want `prop_npc_*` | `queries/world_q.py:1817` |
| **goal** | an organization's authored aim; 12 of the rows are minted as OUGHT Propositions at world-gen, the 23 `orientation` rows mint nothing | 35 rows; changes attention only, never acts | `goals.yaml:1-12`; `data/goals.py` |
| **question** | the one thing a person deliberates about this round | sources `claim_landed`, `need`; one per deliberation | `queries/world_q.py:2249`; `decision/questions.py:45-76` |
| **attention tier** | order in which a person's questions are taken | 0 ambition referent · 1 own tenure/purview · 2 valued deed · 3 need · 4 rest | `queries/world_q.py:2092-2135` |
| **view** | the ledger ids `choose` may see | last 12 claims (`view_k`) | `decision/questions.py:22-42` |
| **candidate** | one formable option: `(verb, subject, operands)` | one per granting seat | `decision/options.py:55-340` |
| **score** | pursuit term + stance term + urgency | stance gain 1.0 doubles the stance term | `decision/choose.py:130-151` |
| **temperature τ** | noise scale of the Gumbel (Plackett–Luce) ordering | 0.1 | `data/fixtures.py:286`; `decision/choose.py:350-390` |
| **scene budget** | scene actions a person may spend this season | `max(1, 5 + holds − body bands − travel legs)` | `decision/budget.py:57-61` |
| **scene** | a bundle of ≤ 3 acts released together | costs 1, or 2 if it holds more than one act | `decision/choose.py:640-669`; `data/fixtures.py:488-489` |
| **act** | one intended verb application by one person | id `H(seed, tick, actor, "act:…")` | `state/carriers.py:598` |
| **verb row** | one line of the action menu: eligibility, precondition, writes, emits, refusals | 53 rows; 47 resolvable; menu 46 | `verb_table.yaml`; `loop/driver.py:101-200` |
| **eligibility** | who may attempt: `own` (anyone), `remit:<act>` (a seat granting it), `hold:<x>`, `presence:<x>` | `presence:` always declines | `loop/resolve.py:103-166` |
| **precondition** | the typed cell (or hand predicate) checked against the world at RESOLVE | any non-True refuses | `loop/resolve.py:270-283` |
| **degree** | a contested act's outcome band | social: Overwhelming/Success/Partial/Failure; combat: Felled/Wounded/Untouched; field: Declared/Won/Lost/Unopposed | `verb_table.yaml` per row |
| **stratum** | resolution order class of a verb | movement < binding_decision < contested_physical < uncontested_material < social | `rosters.yaml:436-445`; `loop/resolve.py:57-58` |
| **event** | what an act (or the clock) did, with causes | refusals are events, never errors | `loop/resolve.py:1137-1173` |
| **witness channel** | who perceives an event | 5, strongest first: co_located, witness_key, document_key, chronicle, post_remit | `rosters.yaml:378-390` |

## 2 How it works

The order below is the order an actor meets the rules in one season.

### 2.1 The season: seven steps, five rounds

| # | step | runs | what it does to you |
|---|---|---|---|
| 1 | CALENDAR | once | Dates due this tick fire; a sitting with a holder forms an empty docket slot (`loop/calendar.py:28-70`). |
| 2 | MATTER | once | The actorless clock: record terms mature, tenure terms close, every claim loses 5 confidence, cohorts eat from the nearest larder, sites yield into stores, travel legs end, sites wear. Hunger, ageing and illness are coded but ship at 0 (`body_step=0`, `age_step=0.0`, `illness_rate=0.0`), so MATTER kills nobody (`loop/matter.py:165-710`, `:513-554`). |
| 3a | DELIBERATE | each round | You sense, receive one question, see your last 12 claims, and `choose` returns scenes. Nothing is written. |
| 3b | RESOLVE | each round | Every released act in the world resolves in one global order: stratum first, then a seeded hash (`loop/resolve.py:57-58`). |
| 3c | ENCOUNTER | each round | Declared `march` acts are fought (mass battle). |
| 3d | WITNESS | each round | Each event is fanned to its observers and deposited as claims in their own ledgers. |
| 4 | CENSUS | once | A person named by an order but not yet in the world is individuated; otherwise nobody is generated. |
| 5 | `tick += 1` | once | The only clock advance. |

Since PR #494 the season also calls `world_q.endings_reached(w)` between CENSUS and `tick += 1` and returns it as `endings`: a read with
no token, Event or write, on which the run does not halt (`loop/driver.py:515-519, 532`; the function is `queries/world_q.py:1764`).

Because WITNESS runs every round, what happened in round 0 is already in your ledger when you deliberate in round 1. Within one
round all persons choose simultaneously, against the same frozen world; the world only changes at RESOLVE.

[precedent: `research/game_precedent_suite/tutorials/T16_managers_narrative.md`, King of Dragon Pass §2] The rhythm is the one King of Dragon
Pass uses (the world answers after each action), at a higher rate: KoDP gives a clan two actions a season ("time will pass only when you
initiate an action"); a Valoria person releases up to five scenes of up to three acts, and at seed 0 an acting person formed 8.1 acts in
tick 0 and 9.4 in tick 1 (§2.6): four to five times KoDP's two, and 7.5 times at the 15-act ceiling.

### 2.2 A question arrives

You do not survey the world and pick a goal. Each round the driver hands you a sorted list of questions built from your own state
(`queries/world_q.py:2249`), and the shipped aggregation rule `first` keeps only the top one (`data/fixtures.py:481`).

- **`need` questions.** One per ambition (a live `commit` to an OUGHT Proposition) whose referents are non-empty. The referent is the
  ambition's subject: the faction head for a creed, the goal's object for an organization goal (a person, a rung, the holders of
  named seats, or the doers of a named kind of deed found in your own ledger), the named person for a personal want.
- **`claim_landed` questions.** One per claim deposited since you last deliberated whose subject, place or named party lies within
  your reach (yourself, your purview, the rungs above your home).
- **Standing occasions** (vacant seats you may fill, seats or places you have heard of, writs you hold, larders your seat may
  requisition) are stamped onto the first question as extra referents.

The sort key is the attention tier (§1), then, inside tiers 0 and 3, **salience**: the cosine between your projected pursuits and
what the organization expects (its role template plus its goals' pursuits). Your own personal want always has salience 0.0, so a
member whose values fit the organization answers the organization's goal first. This "salience" is value fit (the `pursuit_cosine_axes`
call, `queries/world_q.py:2295-2310`), not the storylet sense of the rule matching the most conditions
[precedent: `research/game_precedent_suite/dispositions/D_T02.md`, row E5c].

At world build every ledger is empty, so **in round 0 every named person's question is a `need`** (my probe: 46 of 46). Cohorts
have no ambitions and no questions at build; they start acting once claims land on them (probe: 234 of 535 tick-0 acts are by
cohorts).

### 2.3 Forming candidates

`opening_set` walks every verb row and keeps a candidate only if it passes all of these gates, in order (`decision/options.py:55-340`):

1. the verb is in the menu: resolvable (47 rows) and not withheld (`destroy_record` is withheld), so 46 verbs;
2. person-side eligibility: `own` admits everyone; `remit:<act>` admits only if one of your live holds grants that act; `presence:`
   never admits;
3. the subject is one of the question's referents, of the class the row accepts (some rows take only a Record, an Office or a Rung);
4. per-verb narrowing: `forgive` only toward someone you hold a negative stance row against; `tell` only if you hold a claim to say;
5. every operand can be derived (`to`, `site` and `subject` all bind the question's referent; `from` is where you are; `kind` defaults
   to grain, `amount` to 1). Some rows fan out: a row whose `to` is a known person forms one candidate per person your ledger knows,
   and `train` forms one per vocation (`decision/options.py:267-280`). You are never your own opponent on a contested row, nor your
   own counterparty (`:261-262`, `:302-303`);
6. the **known-false veto**: dropped if your *own* claims contradict the precondition (`decision/options.py:308`). Not knowing is not
   a veto.

So every candidate in one deliberation is about the same one or two subjects, and nearly every `own` verb is formed whatever the
subject is. The chooser does not check the precondition against the world; the world checks it at RESOLVE.

### 2.4 Scoring

For each candidate `c` (`decision/choose.py:130-151`):

    score(c) = damp · Σ_axis axis_w[axis] · align(c.verb, axis)   +   (1 + stance_gain) · stance(c.subject)   +   urgency

- `axis_w` = your 15 pursuit weights projected onto the 7 axes (`data/pursuits.py:60-89`). The `doctrine` weight is first multiplied
  by your religious intensity (highest held church or Einhir affiliation ÷ 5). At shipped values there is no scar shift.
- `damp` = 1 at the shipped `confliction_weight = 0`.
- `stance(subject)` = Σ valence × weight over your stance rows naming the subject (the shipped `legacy` arm), counted twice because
  `stance_gain = 1.0` (`data/fixtures.py:823,837`).
- `urgency` = subsistence ÷ 1000, the same for every candidate, so it cannot change any order (`decision/choose.py:217-238`).

What the score cannot see: the odds, the precondition, the opponent, witnesses, the clock, what the act would contain, and whether it
advances any goal. 13 verbs have no alignment cell and score 0 on the pursuit term for everyone.

**Magnitudes decide the game.** Seeded stance rows carry valence ±1 and weight up to 5; in the realm's round 0 the stance terms I
observed were 0, ±4, 6, ±8, 10, 12, 16 and 20, while a pursuit term for the cast lies within about ±0.3 (§3). When candidates have different subjects, stance decides. When they share a subject, which
is the round-0 case, the stance term cancels and only the pursuit term and the noise separate verbs.

### 2.5 Ordering: noise at τ = 0.1

The candidates are sorted by score, then re-ordered by Plackett–Luce sampling (`decision/choose.py:381-390`): for each candidate draw
`u` from a stream keyed to `(person, "choice:verb:subject")`, set `g = −ln(−ln u)`, and sort ascending on `−(score/τ + g)`. This is
sampling without replacement with probabilities ∝ `exp(score/τ)`. For two candidates A and B:

    P(A before B) = 1 / (1 + exp(−(score_A − score_B)/τ))

At τ = 0.1 a pursuit gap of 0.1 gives 73% / 27%; a gap of 0.3 gives 95%; a stance gap of 2 gives effectively 100%. The noise is a
property of the candidate, so the same candidate in the same tick gets the same draw.

### 2.6 Budget and packing

Your budget is in scene actions (`decision/budget.py:57-61`):

    budget = max(1, 5 + 1 × (live hold tenures) − (body floors 800/500/100 you are below) − 1 × (travel legs))

Every live `hold` counts: a seat, a held territory, every Record you hold and every Proposition you uttered. The minters are
`create_record`, `issue`, `open_case`, `petition`, `survey`, `forge` and `utter` (`loop/effects_information.py:125-139`), plus
`conceal`'s cover Record; `loop/deliberate.py:105-109` states the Record case. `choose` receives your **season remainder** and packs
the ordered list greedily into chunks of 3. A chunk of more than one act is extended and costs 2; if only 1 action is left, the chunk
is trimmed to one act (`decision/choose.py:640-669`). So budget 5 buys scenes costing 2 + 2 + 1 (7 acts) and budget 6 buys 2 + 2 + 2
(9 acts); one travel leg drops a budget-6 holder to 5, i.e. 9 acts become 7. The ceiling is 5 released scenes × cost 2 = 10 actions.
Budgets drift up, because every Record and every uttered Proposition is a hold: at seed 0 the mean budget is 5.57 at build, 6.41 after
tick 0 and 7.69 after tick 1, and after tick 1 eleven of 74 persons hold a budget above 10, an excess no round can release (round-3
probe, §9). The tree's own comment calls the count "WIDER THAN OFFICES", against S26.3's by-office budget, and files it as H-92
(`loop/deliberate.py:95, 107-109`; `hole_register.yaml:1142`).
Observed at seed 0, per tick, over the persons alive at the start of the tick (every one of them formed at least one act): in tick 0,
83 persons formed 676 acts and 535 reached the fold (8.1 and 6.4 per person); in tick 1, 78 persons formed 731 and 597 reached the fold
(9.4 and 7.7). In each tick at least one person formed 15 acts, the 5-scene × 3-act ceiling. "Reached the fold" is the control run's
"attempted" basis (trap 9); "formed" is the unique acts in `w.acts`. The two-tick totals are 1,132 reached and 1,407 formed.

### 2.7 Release and resolution

The driver releases at most **one scene per round** (`scenes_per_round = 1`, `loop/deliberate.py:247-262`), so at most 5 scenes per
season. Unreleased scenes wait in your queue; you are asked again only if your inputs changed (a 7-term fingerprint: question,
subsistence, tenures, some claims, body, travel, names). A refused act stays retryable; a succeeded opportunity is dropped from later
queues.

At RESOLVE each act goes through the fold:

1. the actor must still exist (else `act.ineligible`);
2. world-side eligibility, then the precondition evaluated against the world as the earlier acts in this fold left it. True passes;
   False or Unknown refuses (`loop/resolve.py:270-283`);
3. a contested or graded row calls its resolver for a degree;
4. the row's `writes` for that degree go through the write gate; an effect that changes nothing is a refusal;
5. the row's `emits` (success) or `emits_on_refusal` (refusal) become events, with the act as their first cause.

A refusal costs the scene action you spent, emits an event, and deposits an observation in **your** ledger (observation mode
`actor`), which is how you can later veto it as known-false.

### 2.8 Acts become events, events become beliefs

At WITNESS each event goes to the observers each channel admits; the first channel that admits a person sets the claim's source.
Persons in the room get firsthand claims. The `chronicle` channel is a **kind filter**: any event whose kind appears in some
`binding_decision` row's `emits` is deposited in everyone alive, as hearsay (`told_by`). That covers `order.given`, `date.scheduled`
and `tenure.closed`, including MATTER's own term lapses (`epistemic.py:649-686`). `news.told` carries the teller's chosen claim to the hearer as `told_by`. A refused
or failed inquiry (`finding.none`) deposits nothing (`rosters.yaml:1145`). Ledgers cap at 200 and evict by `eviction_key(confidence, when)`
(`state/ledgers.py`). Separately, the fold itself (at RESOLVE, not WITNESS) raises **scar** in observers whose held pursuits or
affiliations the act's alignment violates; at scar ≥ 3 on an affiliation the conviction crisis folds it into an incompatible heir.

The loop that closes every round: **act → event → claim in observers → new `claim_landed` question → next choice.**

### 2.9 Predicting what a person will do (the rules of thumb)

1. Find their question: round 0 is their most salient `need`; later rounds favour claims about their ambitions' referents (tier 0),
   then about their own tenures or purview (tier 1).
2. The subject is that question's referent. Every eligible verb is formed on it. In one line: the attention tier and, inside tiers 0
   and 3, salience pick whom you face; weighted sampling (∝ exp(score/τ), `decision/choose.py:376-392`) picks what you do to them.
3. If there is one subject, the order of verbs is their pursuit-term order, blurred by noise. A verb 0.1 ahead of another is placed
   before it about three times in four (pairwise); being placed **first among ~30** is much rarer: Sæmund's top-scoring verb had
   P(first) = 0.17.
4. If there are several subjects, all verbs on the subject they favour most come first; the subject they hate most comes last.
5. Their first scene is the top three; the next round's scene comes from a fresh deliberation if anything changed.
6. Whether the act lands is a world question the chooser never asked: wrong-class subjects (a person given to a site verb) refuse.
7. Cohorts have no pursuits and no stance, so their order is uniform noise.

## 3 A worked example: Sæmund Haelgrund, Senior Inquisitor, tick 0

Every number below was printed by my probe on `build_realm(0)` under the control-run recipe (§9).

**The sheet (`p_npc_004`).** Pursuits: doctrine 0.60, stability 0.20, justice 0.10, honour 0.08, virtue 0.06, scholastics 0.05,
reputation 0.04, community 0.03, stewardship 0.03, the other six 0.02 each. Convictions: solmund_orthodoxy 5, thread_truth 1,
altonian_civics 1, einhir_restoration 0 (a held rejected pole). Tenures: `contain` and `reside` at `b_s_036_cathedral` (under
`terr_T9`); `hold` on `off_senior_inquisitor` (remit `determine`, seat rung `terr_T9`); `commit` to `fac_church_of_solmund`,
`prop_npc_004`, `goal_inquisitors_find_heresy`, `goal_church_suppress_restoration`. Stance rows: `(p_npc_021, +1, 4)` (the faction
head) and `(p_npc_003, −1, 4)` (Yrsa Vossen, holder of `off_restoration_leader`). Body 1000. Budget = 5 + 1 hold = **6**.
Subsistence reads 0 (his home rung has no stores), so urgency = 0.

**Step 1: the question.** His four ambitions give three `need` questions; the heresy goal names the doers of Einhir-engaging deeds
found in his own ledger, which is empty, so it gives none. All three sit in tier 3, ordered by salience:

| question | referent | salience | key |
|---|---|---|---|
| `q:need:goal_church_suppress_restoration` | `p_npc_003` (Yrsa) | 0.95055 | (3, −0.95055, …) **first** |
| `q:need:fac_church_of_solmund` | `p_npc_021` | 0.9453 | (3, −0.9453, …) |
| `q:need:prop_npc_004` (personal want) | `p_npc_038` (Arnlod) | 0.0 | (3, −0.0, …) |

**Step 2: candidates.** 30 of the 46 menu verbs survive the gates, all with subject Yrsa. Dropped: 10 for lack of remit (`confer,
convene, covenant, dispatch, establish, issue, march, requisition, revoke, seize`: his seat grants only `determine`), 3 for referent
class (`comply` needs a Record, `oblige` an Office, `migrate` a Rung), and `argue, give, tell` at the later gates (no Proposition, no
held Record, nothing to say). `determine` and `open_case` survive because the seat grants `determine`.

**Step 3: the axis weights.** One axis worked by hand, partisan_equitable, using the projection column for that axis:
doctrine 0.60×0.2 + stability 0.20×0.4 + justice 0.10×0.8 + virtue 0.06×0.3 + scholastics 0.05×0.4 + honour 0.08×(−0.3) + the rest
(−0.068 together) = **0.226**. Religious intensity is 5/5 = 1.0, so doctrine is not rescaled. The full vector: precedent_substantive
−0.141, hierarchical_equal −0.019, partisan_equitable +0.226, selfish_selfless +0.021, rigid_flexible −0.124, grandiose_humble
+0.053, deontological_instrumental −0.192.

**Step 4: score two candidates.**

| | `open_case` on Yrsa | `petition` to Yrsa |
|---|---|---|
| cells | prec_sub −0.4, hier_eq −0.5, part_eq +0.3 | hier_eq −0.4, grand_humble +0.3 |
| pursuit term | (−0.4)(−0.141) + (−0.5)(−0.019) + (0.3)(0.226) = 0.0564 + 0.0095 + 0.0678 = **0.1337** | (−0.4)(−0.019) + (0.3)(0.053) = 0.0076 + 0.0159 = **0.0235** |
| stance term | (1 + 1.0) × (−1 × 4) = **−8** | **−8** |
| urgency | 0 | 0 |
| score | **−7.8663** | **−7.9765** |

The stance term is the same for both (same subject), so the 0.110 pursuit gap decides the odds:
P(`open_case` before `petition`) = 1 / (1 + e^−1.102) = **0.75**.

**Step 5: the draw.** `petition`: u = 0.95046 (raw 0.9504574; not the salience 0.9505464 above, which merely rounds alike), g = −ln(−ln 0.95046) = 2.980, key = −(−79.765 + 2.980) = 76.785. `open_case`: u = 0.8335,
g = 1.703, key = 76.960. The lower key goes first, so **`petition` precedes `open_case`**: the 25% outcome. Across all 30 the
deterministic leader was `commit` (pursuit 0.2032; P(first) = 16.6%), and it was sampled ninth. The sampled head was
`petition, open_case, create_record | research, restore, utter | accept, build, commit`.

**Step 6: pack and release.** Budget 6, greedy chunks of three, cost 2 each: three extended scenes, 6 actions. Round 0 releases the
first: `[petition, open_case, create_record]`, spending 2.

**Step 7: resolve (round 0).** The fold runs in stratum order across the whole realm. Before any of his acts, Arnlod Olafsson
(`p_npc_038`, same Church, same cathedral) resolved `accept` on Yrsa, a contested_physical act, so it goes before social acts, and the
combat seam returned **Felled**: `person.died`, Yrsa is removed. Then:

| act | stratum | check at RESOLVE | event | state written |
|---|---|---|---|---|
| `create_record` | uncontested_material | none | `record.created` | a Record exists; Sæmund holds it, so his budget rises by 1 |
| `petition` to Yrsa | social | `to` is an existing Person: **False** (dead) | `petition.refused` | none |
| `open_case` on Yrsa | social | seat purview (`terr_T9`) reaches the matter's place: **no** (she was at `b_s_004_market` under `terr_T2`, and now has no place) | `case.unauthorized` | none |

**Step 8: witness and round 1.** Sæmund is co-located with Arnlod, so he holds a firsthand `proposition.uttered` claim about Arnlod
from round 0. Arnlod is the referent of Sæmund's personal want (`prop_npc_004`), so that claim is a **tier-0** question and outranks
every `need`. Budget is now 5 + 2 holds − 2 spent = 5, packed 2 + 2 + 1. Released: `[train, open_case, commit]` on Arnlod.
`open_case` now lands (`case.opened`: Arnlod is inside `terr_T9`), a case file is minted and held (budget +1 again); `train` is refused
(no capability key to raise); `commit` is refused (Arnlod is not a Proposition).

**The season's ledger.** Over rounds 0–4 his remaining budget read 6, 5, 4, 3, 1; he released 4 scenes, spent 8 actions, and resolved
11 acts with 3 non-refusals (two `record.created`, one `case.opened`). Round 4's only candidate had already been realised, so
nothing was released. He ends the season holding his seat and 3 Records (budget 9 at tick 1). His scar counts rose on every pursuit
(justice 18, liberty 17, love 16 …) and on 3 affiliations to 1 each: below the crisis threshold, and pursuit scars are inert at the
shipped shift 0. His stance rows and pursuits are unchanged. Nothing records progress on either goal.

## 4 What you can do: the action menu

How to read a row. **May** = eligibility (`own` = anyone; `remit:x` = a seat whose grants include x). **Needs** = what RESOLVE checks
against the world: the typed cell `requires_typed`, not the prose `requires:` string. Where half a precondition is untyped, it is
said: `speak` types only "a docket item names the subject" (the venue half is not checked), and `determine` types the party, docket,
bench and quorum but not the fired date. **Does** = writes and success event; contested rows by degree. **Refused as** = the refusal
event. **Run** = control run `attempted/ok` for seeds 0 · 1 · 2. "Attempted" means admitted to the fold (`loop/resolve.py:377-379`),
so acts refused at admission are uncounted (trap 9); for contested and graded rows "ok" means Partial or better; `—` = none admitted.
Every act costs its share of a scene. ✗ = not in the menu (not resolvable, or withheld). Row text from `verb_table.yaml` (dump in §9).

**A. Take a stand: allegiance and feeling**

| verb | may | needs | does | refused as | run s0 · s1 · s2 |
|---|---|---|---|---|---|
| `utter` | own | nothing | mints an immutable Proposition and a maker's hold on it (+1 budget) | — | 39/39 · 39/39 · 49/49 |
| `commit` | own | subject is a Proposition | opens a `commit` edge (membership, adherence) | `commitment.refused` | 61/0 · 56/1 · 63/1 |
| `release` | own | you hold a releasable tenure toward the subject | closes it (`tenure.closed`, `commitment.ended`) | `release.refused` | 45/3 · 44/5 · 46/3 |
| `forgive` | own | you hold a negative stance row on the subject | deletes those rows (`stance.moved`) | `forgive.refused` | 1/1 · 2/2 · 2/2 |
| `oblige` | own | subject is a seat whose `binds` admits you; you do not hold it and owe it nothing yet | `oblige` edge with a 4-season term (`duty.taken`) | `duty.refused` | — · 24/22 · — |
| `tie / knot` ✗ | own | — | would open a bond | — | not resolvable |

**B. Find things out**

| verb | may | needs | does | refused as | run |
|---|---|---|---|---|---|
| `interview` | own | subject is a Person | `finding.made` | `finding.none` | 32/11 · 16/2 · 39/11 |
| `reconstruct` | own | you hold a claim on the subject | `finding.made` | `finding.none` | 39/33 · 52/46 · 55/49 |
| `survey` | own | you hold a claim on the subject, and it coheres under one faction | a `faction_sheet` Record | `survey.refused` | 57/13 · 38/5 · 59/13 |
| `research` (graded) | own | subject is a Record | degree → `finding.made` (O/S/P) or `finding.none` | `finding.none` | 14/7 · 8/1 · 4/2 |
| `surveil` (graded) | own | subject is a Rung and you are present at it | as `research` | `finding.none` | 30/5 · 29/9 · 22/5 |
| `examine` (graded) | own | subject's `site` is a Site you are present at | as `research` | `finding.none` | never pass admission: 0 admitted at s0, s1, s2 (formed 62 at s0) |
| `thread_read` ✗ | own | Thread Sensitivity ≥ 30 (no carrier) | — | — | not resolvable |

**C. Shape what others believe**

| verb | may | needs | does | refused as | run |
|---|---|---|---|---|---|
| `tell` (contested: a standing) | own | you hold a claim on the subject; the hearer `to` is with you | O/S/P: `news.told` (content moves at WITNESS; Partial may garble it); F: `news.untold` | `news.untold` | 23/4 · 25/7 · 19/6 |
| `argue` (contested: a proposition) | own | subject is an uttered Proposition; hearer with you | O/S: hearer's pursuits move toward yours; P: won, no move; F: `argument.lost` | `argument.refused` | never pass admission: 0 admitted at s0, s1, s2 (formed 10 at s0) |
| `create_record` | own | nothing | a Record you hold (+1 budget) | — | 87/87 · 88/88 · 89/89 |
| `forge` | own | you hold a claim on the subject; it coheres under one faction | a forged Record with a `forgery_quality` | `forge.refused` | 52/12 · 51/6 · 57/15 |
| `conceal` | own | nothing | a `cover` Record (`cover.assumed`) | — | 19/19 · 34/34 · 28/28 |
| `construe` ✗ | own | — | would distort terms | — | not resolvable |

**D. Bring a matter before authority**

| verb | may | needs | does | refused as | run |
|---|---|---|---|---|---|
| `petition` | own | `to` is a living Person; `from` (where you are) is a Rung | a `petition` Record you hold | `petition.refused` | 42/14 · 31/7 · 34/11 |
| `carry` | own | subject is a petition Record you hold | puts it on a docket | `carry.refused` | 28/0 · 32/0 · 34/0 |
| `open_case` | remit:determine | your seat's purview reaches the matter's place | a case Record + a docket item | `case.unauthorized` / `case.refused` | 12/6 · 2/1 · 9/5 |
| `convene` | remit:convene | subject is a rung above the person tier, or none | schedules a Date (a sitting) | `convene.refused` | 1/0 · — · 5/1 |
| `speak` (contested: a matter) | own | a docket item names the subject | O `matter.carried` · S `.advanced` · P `.held` · F `.turned`; writes nothing | `speech.unheard` | 3/3 · — · 2/2 |
| `determine` (contested: a proposition) | remit:determine | subject is a party with a docket item; you sit on the bench; bench meets quorum | O/S: tenure, docket matter, degree, pursuits; P: no pursuits; F: `matter.undetermined` | `determine.refused` | — (formed 2, none admitted) · 1/1 · — |
| `comply` | own | a dispensation Record whose terms you hold a claim on | `compliance.given` | `compliance.impossible` | never formed (0 in `w.acts`, s0) |
| `evade / defy` ✗ | own | — | — | — | not resolvable |

**E. Govern from a seat** (only seat-holders form these). The remit roster contradicts itself: `rosters.yaml:315` calls the remit
acts "the CLOSED five … plus `convene`" and `:316` declares `open: true` (`verb_table.yaml:922` also says CLOSED). Some seats' grants
come from `rosters.yaml: remit_default`, which the register calls "a testing fixture, not canon" (`hole_register.yaml:1306`). Sæmund's
authored seat grants only `determine`.

| verb | may | needs | does | refused as | run |
|---|---|---|---|---|---|
| `dispatch` | remit:dispatch | the named person exists (an unnamed one is demanded and individuated at CENSUS) | `order.given` | `dispatch.refused` / `person.demanded` | 18/6 · 18/7 · 10/10 |
| `issue` | remit:issue | executor is a Person in your purview; you hold a claim of the terms | a dispensation Record | `issue.unauthorized` / `issue.refused` | 6/5 · 12/5 · 14/8 |
| `confer` | remit:confer | the office's conferral basis; conferee alive; seat empty or revocable | opens/closes the seat's `hold` | `confer.refused` | — · 5/1 · — |
| `establish` | remit:confer | conferral basis and a rung to put the office at | a new Office | `establish.refused` | — · 5/0 · 4/0 |
| `revoke` | remit:revoke | a revocation basis and a live hold on the office | closes the hold | `revoke.refused` | 6/0 · — · 4/0 |
| `covenant` | remit:issue | `to` is a Person; terms are an uttered Proposition | a covenant Record offered | `covenant.refused` | 13/0 · 4/0 · 1/0 |
| `requisition` | remit:issue | purview reaches the rung; its stores ≥ amount | moves stores to you | `requisition.unauthorized` / `.refused` | 2/0 · 5/0 · 5/0 |
| `seize` | remit:issue | purview reaches the Record or settlement; a held warrant names it | takes the hold | `seize.unauthorized` / `.refused` | never formed (0 in `w.acts`, s0) |
| `march` (contested: a field) | remit:dispatch | subject is a Rung | Declared at RESOLVE; at ENCOUNTER Won/Lost/Unopposed move bodies, stance, tenures | `march.refused` | 21/21 · 10/10 · 4/4 (all `march.declared`; 0 field events) |

**F. Confront and harm**

| verb | may | needs | does | refused as | run |
|---|---|---|---|---|---|
| `challenge` | own | subject is another living Person | `challenge.issued`; writes nothing | `challenge.refused` | 23/6 · 22/6 · 33/12 |
| `fight` (contested: the body) | own | subject is a living Person | Felled: subject dies · Wounded: body loss · Untouched: `contest.undecided` | `kill.refused` | 7/4 · 5/5 · 8/5 |
| `accept` (contested: the body) | own | subject is a living Person; **no prior challenge is checked** | as `fight` | `accept.refused` | 18/11 · 9/6 · 12/10 |
| `sabotage` | own | the `site` is a Site you are present at | lowers its condition | `sabotage.refused` | 34/0 · 22/0 · 33/0 |

**G. Make, keep and move goods**

| verb | may | needs | does | refused as | run |
|---|---|---|---|---|---|
| `work` | own | site condition ≥ its floor; a rise only where a live works Record names the site | raises condition | `work.unavailable` | 77/0 · 70/0 · 63/0 |
| `restore` | own | the `site` is a Site you are present at | raises condition | `restore.refused` | 23/0 · 31/0 · 30/0 |
| `build` / `found` | own | subject is a `works` Record you hold | a Site / a new Rung | `build.refused` / `found.refused` | build 19/0 · 17/0 · 21/0; found 24/0 · 27/0 · 23/0 |
| `transfer` | own, remit:issue, hold | the giver's stores ≥ amount (default 1 grain) | moves stores | `transfer.refused` | 45/1 · 37/0 · 43/5 |
| `give` | own | you hold the Record; receiver is with you | hands its hold over | `give.refused` | 16/0 · 21/0 · 19/1 |
| `destroy_record` ✗ | own | a Record you hold | removes it | — | withheld by fixture |
| `exchange` ✗ | own | — | — | — | not resolvable |

**H–J. Persons, movement, succession**

| verb | may | needs | does | refused as | run |
|---|---|---|---|---|---|
| `tend` | own | subject is a Person with you | restores body to 1000 (refused if already whole) | `tend.refused` | 34/0 · 22/0 · 19/0 |
| `train` | own | subject is a Person with you | +1 to a capability key the subject already holds | `train.refused` | 38/0 · 30/0 · 30/0 |
| `move` | own | a containment path to `to` | moves your `contain`, adds a travel leg | `travel.blocked` | 42/16 · 35/17 · 40/12 |
| `migrate` | own | a path to `to`, and room there | moves your `reside` | `travel.blocked` / `migrate.refused` | 81/0 · 143/0 · 143/0 |
| `succeed` ✗ | own | — | would name an heir | — | not resolvable |

**What the run column says.** At seed 0, 22 verbs produced an outcome (counting `march`'s declarations as none). Seed 1 adds
`commit`, `confer`, `determine` and 22 successful `oblige`s; seed 2 adds `commit`, `convene`, `give`. Every row that builds, repairs,
heals, trains, migrates, requisitions or offers a covenant refused in all three seeds.

## 5 Pursuing goals here

**(a) What a goal is in code.** A person has three kinds of aim, and the code represents each differently:

| aim | representation | how it reaches choice |
|---|---|---|
| values | `pursuits` (15 weights) → 7 axis weights | the pursuit term of every score |
| allegiance | a `commit` to a faction Proposition `fac_*` (subject: the faction head) | a `need` question about the head; stance rows toward the head seeded from loyalty |
| organization goal | a `commit` to an OUGHT Proposition minted from `goals.yaml` (35 rows, of which 12 mint a Proposition; faction, body or seat level) | a `need` question about its referents; `stance: ±1` signs the members' seeded stance toward the target |
| personal want | a `commit` to `prop_npc_*`, an OUGHT Proposition about one named person | a `need` question with salience 0.0 |

Goals change **what a person attends to, never what they value** (`goals.yaml:11-12`): the score has no goal term. No code tests
whether a goal is met; a grep of `data/goals.py`, `queries/world_q.py`, `decision/` and `loop/` for completion logic finds none, and the
loop halts on no ending: PR #494's `endings_reached` (§2.1) is a read over the `rosters.yaml: endings` rows, not over goals, and the realm as
built reaches none (errata G17; `endings` was `[]` after both ticks at seed 0, round 3). A goal of kind `orientation` mints nothing and only shifts salience.

**(b) Plays.** "Pursuing" a goal means getting its referent in front of you and having the right act formable and admissible on it:

1. **Strike at a rival person.** Needs nothing but a referent and `own`: `fight` or `accept` reaches the combat seam (§4 F). This is
   how the realm's deaths happen; Yrsa died in round 0 of seed 0 to an `accept` by a fellow Inquisitor. Risk: the seam can fell you
   instead (errata C1 reports about half of mirror fights).
2. **Put someone before a court.** Hold a seat granting `determine` whose purview contains the person's place → `open_case`
   (case Record + docket item) → a sitting must be convened (`convene`, a seat granting it) and fire at CALENDAR → `speak` at the
   sitting → `determine` by a bench member at quorum. Refusals at each step: wrong purview (`case.unauthorized`), no docket item
   (`speech.unheard`), no bench or quorum (`determine.refused`). Only one `determine` succeeded across three seeds.
3. **Bind yourself or others to a cause.** `utter` a Proposition (always succeeds, and you keep a maker's hold on it), then `commit`
   to it. The hold is the only route by which a Proposition, which has no place, can become a question's referent
   (`loop/effects_information.py:1010-1023`). In play `commit` almost always forms on a person instead and is refused: attempted/ok
   61/0 at seed 0, 56/1 at seed 1, 63/1 at seed 2. No code gate stops a cohort committing; none did in these runs.
4. **Take service under a seat.** `oblige` on an Office you have heard of (it forms only on referents your ledger names): 22 of 24
   succeeded at seed 1, none were formed at seeds 0 and 2.
5. **Learn about a target.** `interview` (any living person) and `reconstruct` (anyone you hold a claim on) are the reliable finders;
   `survey` turns a faction-coherent subject into a faction sheet. Graded inquiries need Record, Rung or Site subjects (B).
6. **Grow your budget.** `create_record` and `utter` have no precondition and always succeed (87/87 and 39/39 at seed 0), and each
   leaves you a hold. Each one adds a scene action from the next round (Sæmund 6 → 9 over tick 0). The ceiling is 10 actions
   (5 scenes × 2); a budget above 10 is unspendable (H-92, §2.6).

**(c) Costs, risks, counter-play.** Every act costs budget whether or not it lands, and a refused act is retried in later rounds
(Sæmund attempted `train` on Arnlod twice). Other people's acts resolve in the same fold: anything in an earlier stratum (movement,
binding decisions, combat) changes the world before your social or material act is checked, which is how Yrsa's death refused
Sæmund's petition. Seen acts scar the witnesses whose values they violate, and three scars on an affiliation fold it. Any event whose kind a
`binding_decision` row emits is deposited realm-wide as hearsay by the chronicle channel (a kind filter, §2.8), so governance is never
private.

**(d) What the mechanics structurally reward and punish.**
- Stance outweighs values by one to two orders of magnitude; whom you face is decided by the question, and which verb by a small
  pursuit gap plus noise.
- The 13 uncelled verbs (`argue, carry, conceal, covenant, examine, forgive, interview, restore, sabotage, tell, tend, thread_read,
  train`) score 0 on values for everyone. Only `tell` and `thread_read` are uncelled by design; `restore`'s note says its premise is
  stale and its cells are owed (`rosters.yaml:2979-2985`). In effect: a Church inquisitor ranks `forgive` toward the Restoration's leader as readily as any
  neutral verb (Aldric Tormann forgave her in round 0, `stance.moved`).
- Wrong-class subjects make whole families dominated: site verbs (`work, restore, sabotage, examine`), place verbs (`migrate`) and
  Proposition verbs (`commit, argue, covenant`) are formed on persons and refused.
- `accept` is an unprovoked duel: its precondition cannot ask whether a challenge was issued (`verb_table.yaml` `accept`
  `requires_note`).
- `train` can only raise a capability key the subject already holds, and no realm person holds one, so it always refuses.
- Cohorts (37 of 83 persons) choose by pure noise.

**(e) What success leaves.** Records and the holds on them, docket items, Propositions, `commit` and `oblige` edges, deaths (the
subject and its tenures removed), body loss, and claims in every witness's ledger, which become other people's questions. Pursuits
did not change in any run I made, and stance changed only through `forgive`. Convictions did change: 5 folds at seed 0 and 3 at seed 2
at tick 1 (e.g. Hedda Kronvald's orthodoxy 3 folded into einhir_restoration, 1 → 4), none at seed 1.

## 6 How it connects

- **Feeds out.** Contested rows hand a typed input to combat (`fight`, `accept`), mass battle (`march`, at ENCOUNTER) and the
  social-contest roll (`tell`, `argue`, `speak`, `determine`, graded inquiries); each returns one degree, which picks the row's writes.
  Pools default to 2 dice because no person has capabilities.
- **Draws in.** Settlement stores and yield (MATTER) feed `transfer` and `requisition`; seats and purview (governance) gate every
  `remit:` row; the docket and bench (proceedings) gate `speak` and `determine`; the fieldwork trail turns findings into claims.
- **Combinations that work today:** seat + purview → `open_case`; a co-located hearer + a held claim → `tell`; a known seat → `oblige`;
  any referent → `fight`/`accept`.

## 7 Playing it as proposed

[PROPOSED] items are intent, not available rules. Each names what it waits on.

- **A seated player.** IN-47 (character-sheet space: creation is "a cast entry the world-gen builder seats") and IN-46 (grid-mode
  suspension: a played fight) are scheduled as REM-30 / REM-31 in batch RB-3 (decision D-2, ruled yes; designs held PROPOSED). Today
  the only seam into the season loop is the harness `dispatching_chooser` (`harness/play_surface.py:41-52`, exercised only by tests:
  `tests/test_play_surface_dispatch.py`, `tests/test_combat_trace_returned.py`). Outside the loop,
  `systems/social_contest/sim/contest/agon_harness.py` lets a human play Side A of one social contest from stdin against an AI policy
  (`_raw_input`, `:148-155`, calls `input()`; it drives the contest kernel, which no season reaches), and the combat and mass-battle
  workbenches (`systems/combat/combat_engine_v1/workbench/server.py`, `systems/mass_battle/sim/workbench/server.py`) are HTTP designer
  tools that trace one duel or one battle (the combat trace's branch events carry the alternate branches and their odds); none of
  them seats a person in the realm. As built, a seated person would receive the person's View, Sensation, budget query and the shipped
  chooser's proposal (`auto`), and no odds (`harness/play_surface.py:14-19`); a candidate set 22 to 56 verbs wide at round 0, 30 for
  Sæmund (§3 step 2), up to five times a season; and no continuation if the person dies: `succeed` is not resolvable (§4 H–J) and the
  King, `p_npc_020`, was dead after the first season in all three seeds probed in round 3 (§9). Crusader Kings II, Genghis Khan II and
  Old World continue the player through an heir (precedent: `research/game_precedent_suite/tutorials/T12_paradox_classical.md`,
  Crusader Kings II §2; `T13_koei.md`, Genghis Khan II §6; `T01_realm.md`, Old World §2).
- **Right-class referents.** REM-21..REM-25 and REM-2C (batch RB-2a; REM-26, `move` paths, opens RB-2b) would stamp Site, Record and Rung referents onto questions, so
  `restore`, `examine`, `research`, `found`, `build` and `petition` form on the things they act on; REM-29 (`migrate` capacity) and
  REM-2A (`transfer`) in RB-2b. Waits on the referent-class roster.
- **No urgency.** L1-6 option B (ruled) removes `subsistence` from the sensation; REM-44 deletes `urgency`, `benefits_me` and the
  chain. Unbuilt.
- **A smarter score.** D-V6 (open): a contents-aware value term or a `(verb, kind)` alignment key, so that what an act says or
  targets matters. A risk term over believed odds is named in the verbs proposal (D05) and unscheduled. JQ-1 / REM-12: an instrument and
  threshold for how often noise rather than inclination decides.
- **Values for everyone.** ED-IN-0296 (2): cohort pursuit vectors. J-T1 (default Option B): stored attributes 1–7, read only through
  `faculty(domain)` on rows with `contests:`; a `characters.yaml` template (D03). Waits on the J-T1 ruling.
- **Swept arms shipped at control** (the control runs in the loop; the non-control arms are TESTS-ONLY): stance arms `regard`/`declared` (H-194), scar weight shift (H-187), confliction
  damp (H-188), declared intent (H-190), value-refusal gate (H-146), packing rules `one_per_scene`/`by_subject`.
- **Verb roster.** The 92-verb proposal (renames such as `move→travel`, `oblige→pledge`, `carry→lodge`, `surveil→watch`; suites such
  as `fight` hosting `assassinate`, `capture`). It "predicts nothing about play until the mechanics … exist".
- **Inert or refused today:** `presence:` eligibility (always declines); `capability` (empty on every person); the scene-release
  ceiling question (H-92); never formed: `comply`, `seize`; refused at admission every time: `argue`, `examine`; withheld:
  `destroy_record`; not resolvable: `construe, evade / defy, exchange, succeed, thread_read, tie / knot`.

## 8 Common mistakes and traps

1. **"The chooser picks the act that advances my goal."** No. The goal picks the subject; the verb is picked by value alignment and
   noise. Nothing scores consequences or odds.
2. **"The highest-scoring act is chosen."** At τ = 0.1, Sæmund's top-scoring `commit` came ninth. Read the scores as odds (§2.5).
3. **"Five scenes means five acts."** Scenes hold up to three acts; Sæmund resolved 11 acts in tick 0.
4. **"A budget above 5 is wasted."** Draft A1 §2.2 says so, citing `loop/deliberate.py:89-97`. Errata G11 recorded an in-tree
   dispute (`data/fixtures.py:497-502` treats the remainder as a cost budget). Round-2 ruling C1 resolves it in this tutorial's
   reading: what is capped is **scenes** (5 released, one per round); the excess **actions** pay for extended scenes (ceiling 10), and
   Sæmund spent 8 actions in 4 scenes. A budget above 10 is the one that is wasted (§2.6, H-92). A travel leg does cost a seat-holder
   acts (9 → 7).
5. **"Holds are offices."** `budget` counts every live hold, including every Record created and every Proposition uttered
   (`decision/budget.py:57`; `loop/effects_information.py:125-139`).
6. **"`accept` answers a challenge."** It is a duel on anyone living (§5 d).
7. **"Persons have stats."** `capability` is empty on every realm person; every social pool is the default 2.
8. **"Personal wants are character desires."** `prop_npc_*` predicates are design-requirement sentences (Sæmund's: "A completed
   investigation must be able to produce a plausible-but-wrong conclusion …"), aimed at one named person.
9. **"The control run's `attempted` column counts everything formed."** `ctl/control.py` counts `d.resolved`, which only acts that
   reached `_fold` enter. A contested or graded act refused at admission, and any act whose actor died, is missing. Seed 0, from
   `w.acts`: `research` 125 formed vs 14 in ctl, `examine` 62 vs 0, `surveil` 51 vs 30, `speak` 22 vs 3, `fight` 19 vs 7,
   `accept` 34 vs 18, `argue` 10 vs 0, `march` 25 vs 21, `tell` 27 vs 23 (probe6). The `ok` column is unaffected. I used ctl as
   instructed (G2; ruling C2: "attempted" = admitted) and show formation counts only here and in the never-pass-admission cells. A
   formed act that is refused at admission was formed and attempted; it simply never passes admission.

**Corrections to the draft appendices (A1, A2) made in this tutorial:**
- A2 §A.2 table and A2 §A.3: scar "written at WITNESS". It is written by the fold at RESOLVE (`loop/resolve.py::_scar_witnesses`;
  errata G7).
- A2 §A.3: stance written "via `fight`/`accept`/`march`/`forgive`". At runtime only `march` and `forgive` write stance (errata C1;
  `loop/effects_combat.py:425-450`).
- A2 §A.2: regard's "judged/told gains 0.5 live". The gains are 0.5, but the shipped arm `legacy` never calls `regard`
  (`decision/choose.py:89-92`), so they do not reach choice.
- A2 §C (heading, §C.3) and draft §1: "47 admitted" as the menu. The chooser's menu is 46 (`destroy_record` withheld; errata G3).
  C04's "43 typed, 10 untyped" is 37 typed, 6 `requires_typed: none`, 10 with no key (my dump agrees; G3).
- A2 §C.3 run counts: replaced by ctl attempted/ok (G2): e.g. `work` 77/0 not 78/0, `sabotage` 34/0, `survey` 57/13, `fight` 7/4,
  `accept` 18/11, `commit` 61/0. A2's attempt column is in fact the `w.acts` formation count (trap 9).
- A1 §2.2: "a person whose `budget()` exceeds 5 cannot spend the excess" (trap 4; G11).
- A2 §B.3: `work` refuses "on wrong-class referents". Errata C5: `work` has no presence clause, and a rise is staged only where a live
  works Record names the site (`loop/effects_economy.py:103-104`), so it refuses with `work.unavailable` regardless.
- A2 §B.3 and §C.7: the uncelled list is correct, but "value-blind" is by design only for `tell` and `thread_read`
  (`rosters.yaml:2969-2978`). `restore`'s note says its premise is stale and its cells are owed (`:2979-2985`; this overturns errata G13
  for `restore`, per ruling C6). The gaps the proposals target are `carry`, `examine` and `interview`.
- A2 §A.4 and §B.4 grades: rows shipped at control are "RUNS-IN-LOOP at control", not TESTS-ONLY, when the code runs in the loop
  (urgency, damp at weight 0). Swept arms that only tests exercise stay TESTS-ONLY (errata G1).
- Draft §1 and A1: "seed 0 never attempts `oblige`" is seed-0 only; seed 1 executes 22 of 24 (G2).

**§8 Round-2 corrections** (audit2 J, L and CROSS; each cited line opened by me unless marked):
- J-F4 / C1 (accepted, `loop/effects_information.py:125-139, 1010-1034` opened): `utter` and every Record minter leave a hold, so
  `utter` is a budget lever like `create_record`. Added to §1, §2.6, §4 A, §5 b and trap 5.
- J-F8 / C6 (accepted, `rosters.yaml:2966-2986` opened): `restore` is not uncelled by design. Fixed in §5 d and in the G13 bullet above.
- J-F10 (accepted): pursuit weights are not normalized. Sæmund's sum to 1.31 (0.60 + 0.20 + 0.10 + 0.08 + 0.06 + 0.05 + 0.04 +
  2×0.03 + 6×0.02). §1 had said "≈ 1".
- J-F11 (accepted on D01 K1's batch list): REM-26 belongs to RB-2b, not RB-2a. §7 fixed.
- J-F14 (accepted, `decision/options.py:258-282` opened): known-person fan-out, per-vocation `train`, and the self-opponent and
  self-counterparty declines added to the gates in §2.3.
- J-F15 (accepted): §0 and §7 now say the non-control arms are TESTS-ONLY.
- J-F17 (accepted): §2.9 confused pairwise order with being first. Pairwise 0.73 for a 0.1 gap; P(first among 30) for the leader 0.17.
- J "u = 0.9505 equals salience" (checked, no copy error): raw u = 0.950457371 (probe2 re-derives the chooser's own stream
  `draw(p_npc_004, "choice:petition:p_npc_003")`, and its g and key reproduce the sampled order the chooser returned); salience =
  0.950546369. They agree only at four decimals. Both are now printed to five.
- J "acts per person-season ~6-8" (accepted with basis): §2.6 gives 6.8–7.6 over admitted acts and 8.5–9.5 over formed acts, seed 0.
- L-X15 (measured, probe7): conviction crisis graded RUNS-IN-LOOP per seed. Folds: seed 0 five, seed 1 zero, seed 2 three, all at
  tick 1, none at tick 0, no "destroyed" outcome. Snapshot method: persons who died in the same tick are not compared. Added to §0, §1
  and §5 e.
- L-X17 / C5 (accepted, `epistemic.py:649-686` opened): chronicle is an event-kind filter delivering `told_by` hearsay to everyone,
  including MATTER's `tenure.closed`. §2.8 and §5 c fixed.
- L-X19 / C2: every run column is now attempted/ok, per seed.
- L-X21 (kept 22): `speak` formed 22 times at seed 0, counted as unique act ids in `w.acts` over 2 ticks (probe6). T05's 21 uses a
  basis I cannot see; the admitted count is 3.
- L-X23 (accepted, `loop/witness.py:234-242` and `decision/options.py:1426-1440` opened): deposit confidence is refracted below 100 for
  witnesses other than the actor. §1 fixed. I did not re-derive audit L's 67 / 50 values; the firsthand claim Sæmund held stayed 100.
- C3: worked-example season labels are now ticks. C4: the remit-roster contradiction and `remit_default` are noted at §4 E.
  C10: §4 states it teaches the typed cell and names the untyped halves of `speak` and `determine`.
- C11: one-clause definitions of Rung, Record, Proposition/mood, Office/purview and "with" added to §1.

## 9 Checks

Opened: `decision/choose.py:54-160, 217-240, 330-482, 640-669`; `decision/budget.py:40-83`; `queries/world_q.py:2092-2135, 2249-2262`;
`loop/deliberate.py:86-117, 166-206, 247-262`; `loop/resolve.py:55-59, 270-284`; `decision/options.py:300-312`;
`loop/effects_combat.py:371-451`; `loop/effects_economy.py:96-108`; `data/fixtures.py` (defaults at :228, 231, 234, 286, 293, 414,
481, 488-489, 492-503, 511, 526, 707, 715, 725, 800, 823, 837, 923); `rosters.yaml:378-390, 436-445, 1145-1148`;
`verb_table.yaml` rows `commit` (:167), `create_record` (:281), `open_case` (:900), `petition` (:925), `accept` `requires_note`, `work`
(:1506-1520); `goals.yaml:1-30`. Extracts C02, C04, C05; draft A1 §2, A2 §A-C; `audit/ERRATA.md`.

Ran (throwaway scripts of this audit, not committed; `cd /home/user/ttrpg`, HEAD `a4ca9a5`; round-3 re-runs are listed in the last paragraph):
- `probe1.py`: 83 persons, 46 named; per-person pursuits, stance, convictions, holds, commits.
- `probe2.py "" 1`: every named person's round-0 question was a `need`; candidate counts 22–56; scenes.
- `probe2.py p_npc_004 1`: Sæmund's 5 deliberations, 30 candidates with score terms, u, g, keys; 11 acts and their events
  (`s004.json`).
- `probe3.py`: stance rows `(p_npc_021,+1,4)`, `(p_npc_003,−1,4)`; office `off_senior_inquisitor` (remit `determine`, rung `terr_T9`);
  3 questions; budget 6 → 9 after the season; Yrsa absent after the season.
- `probe4.py`: ancestries (market under `terr_T2`, cathedral under `terr_T9`); `person.died` on `p_npc_003` caused by `p_npc_038`
  `accept`, log index 414, before Sæmund's `petition.refused` (503) and `case.unauthorized` (506).
- `probe5.py`: salience 0.95055 / 0.94528 / 0.0; cohorts 0 ambitions, 0 questions at build, 234 of 535 tick-0 acts; round-1 claim
  `3982fec7770d646e` = firsthand `proposition.uttered` about `p_npc_038`.
- `probe6.py`: `w.acts` 1,407 unique vs `d.resolved` 1,132 over 2 seasons at seed 0 (trap 9).
- Softmax over the 30 candidates: P(first) `commit` 0.166, `determine` 0.102, `open_case` 0.083, `petition` 0.0275; pairwise
  P(`open_case` before `petition`) = 0.751.
- PyYAML dump of all 53 verb rows (`rows.txt`): typed cells, writes, emits, refusal kinds; 37 typed, 6 `none`, 10 absent.
- `probe7.py <seed>` for seeds 0, 1, 2: conviction snapshots per tick; folds 5 / 0 / 3, all at tick 1.
- Raw draw check on `s004.json`: petition u = 0.9504573708922568, g = 2.979623377346043, key = 76.78537662265394.
- Not confirmed: which clause (death or purview) decided `case.unauthorized` on Yrsa. Both map to the same kind and both fail.
  The errata's "about half of mirror fights fell the actor" is not re-run here.
