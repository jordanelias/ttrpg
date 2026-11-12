# Decisions for Jordan — every question the suite leaves to you, in plain words

## Status: REFERENCE (a decision register for the suite; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of 2026-11-12. Lane: decision register (Jordan, 2026-11-12: *"Prompt me with context to resolve all decisions"*).

**What this is.** Every decision the audits, addenda and proposals in this suite hand to you, merged so that
one question appears once, wherever it was raised. Each entry says what the game does today, asks one
question, gives the options with what each feels like to play and what it costs, says which option the
raising lane recommends (and where this lane disagrees, why), says what the suite assumes if you say
nothing, and what waits on it. Lane ids, finding ids and file paths are kept out of the prose and put in
the **Sources** line at the end of each entry.

**How to answer.** `DECISIONS_QUICKSHEET.md`, beside this file, gives one line per decision with the
recommended answer. A reply of the form *"accept all recommendations except D-04 (take B) and D-19 (take
A)"* is enough.

**Order.** By how much work each decision blocks, most first. Decisions that only make sense together sit
under one heading, with their shared context written once.

**A note on the three Layer 1 questions you said were unclear** (auto-resolve, units, the duel round). They
are now at D-01 to D-03, rewritten in the plain readings you asked for. The short version: in all three,
every lane's recommendation keeps Layer 1 as it stands, and gives you the experience you described anyway.
You only need to amend Layer 1 if you want the *other* reading.

**STATUS 2026-11-12 (later): every decision except D-34 and D-35 is now answered or ladder-closed. Each entry below begins with its status line; `DECISIONS_ANSWERED.md` governs where they differ from the entry's text, including the recommendations and 'if you do not answer' lines, which are now historical.**

**Answered at first drafting (2026-11-12, recorded in `DECISIONS_ANSWERED.md`, which governs where they differ):**
D-01 (A, the same resolver run automatically), D-02 (A, a row), D-03 (A, nested), D-04 (A, won/lost/drawn),
D-05 (**B**, the bell curve everywhere), D-06 (B, score plus a base), D-07 (**B**, two numbers). Their
entries stay below for the record, each marked. D-08 is re-recommended in the light of D-05.

**Not yours** (answered by the five checks — superseded, irrelevant, settled by a design document, by
precedent, or by what the architecture clearly needs — and listed so you can see they were not dropped):

| question a lane once raised | answer | what settled it |
|---|---|---|
| Is a plain fight to the death, or does a beaten fighter have a way out? | Neither by rule: a felling is a mortal-wound *draw*, and yielding is a draw on the fighter's spirit, for every party | your standing rule *"we do not do deterministic"* (later than the question) |
| Is any matchup certain (the 95% cap that the world never sees)? | No: the upset happens inside the fight, at the deciding blow, where the record sees it | the same standing rule |
| May a settlement's population recover? | Yes, bounded by food and room | your ruling of 2026-09-17 on what bounds growth (it presupposes growth) |
| Do the social-contest kernel's ratified features survive the kernel's retirement? | They lapse with their subject, item by item; the weighted ballot and the armature are re-expressed only where a live proposal carries them | the later, general retirement ruling |
| Minimum cells per unit, or a renderer for tiny formations? | Neither: bodies are laid out at the density the battle engine was calibrated at | the archived design's own scale rule and the calibration precedent |
| May an office be sold; is lay investiture lawful; do the Crown's bureaux take an oath that bars them; who sits at the empire's centre; is a roll ever closed by blood; Schoenland's constitution; may a house be its own faction; is an order answerable at issue or at entry | Each closed by the institutions synthesis: as composition, per-row content, odds, or marked placeholders you may later overwrite as content | precedent and architecture (institutions synthesis §10 table) |

Four more appear below with a recommendation that this lane thinks *is* answerable without you (D-30,
D-36, D-48, D-74); they are kept in the list because a lane raised them as yours, and a one-word "agree"
closes each. Three others (D-27, D-28, D-31) this lane also thinks are answered by your standing rule; they
are kept because the answer overwrites text you ruled, and D-26 asks you once for all three.

---

## Summary

| id | decision | area | recommendation | blocks |
|---|---|---|---|---|
| D-01 | Auto-resolve: the same battle run for you, or a quicker sum | MB, CORE | ANSWERED A (A-1) — the same battle, run on your standing orders | every unwatched battle; the managed-battle surface; the order-of-battle verbs |
| D-02 | A unit: a line on the army's sheet, or a thing in the world | MB | ANSWERED A (A-2) — a line on the sheet | the army hierarchy, loadouts, the four order-of-battle verbs, ARC-07 |
| D-03 | A duel inside a battle: called from inside, or played as separate acts | PC, MB | ANSWERED A (A-4) — called from inside, counted as a nested contest | the duel round's last step; grid squad combat; duels in a field |
| D-04 | What a battle reports: won/lost/drawn, or how decisively | MB | ANSWERED A (A-3) — won, lost or drawn | the battle's typed result and everything that reads it |
| D-05 | Which dice the non-combat rolls use | DICE | ANSWERED B (A-5) — the bell curve everywhere | the exported dice rules; every non-combat roll; the port |
| D-06 | What a skill score is worth outside a fight | DICE, SC | ANSWERED B (A-6) — score plus a base, as combat does | every non-combat band in the game |
| D-07 | Talent and training: one number or two | PC, CHAR | ANSWERED B (A-7) — two numbers | the combat pool and obstacle; character sheets |
| D-08 | What a wound costs a roll | DICE, PC | B — a level against, now that D-05 put every roll on the bell curve | the wound rows of the dice map |
| D-09 | A turn: a round of simultaneous choices, or short chains of acts | CORE | B — short chains | the season fold order; R-09; scene play |
| D-10 | Governance: the season loop's own verbs, or a separate module | FA | A — the loop's own verbs | how the faction game stands alone |
| D-11 | May training gate an act (only a surgeon may operate)? | CORE, CHAR | A — training changes odds, never access | the capability authoring surface |
| D-12 | May rank or office add to a roll? | institutions, SC | A — rank changes who you are to the room, not a bonus die | the institutions kit's rolls; the bench's dice |
| D-13 | Three new facts on a seat (whose clerks, audit at exit) | institutions | B — accept the three keys as a Layer 1 amendment | the institutions kit's chancery and audit |
| D-14 | A vote: a draw on the voter, or the voter's own act | institutions, SC | A — a draw on the voter | ballots and elections |
| D-15 | Natural death: on or off | WR | A — on, after ages are authored | succession, vacancies, the happenings ring |
| D-16 | May a person commit murder? | PC, FI | A — yes, rarely, from grievance and hatred, by draws | the detective game's supply of crimes |
| D-17 | The founding order and canon's line on the south in the Secession War | canon, institutions | A — reword canon: the south fought, ranked third, and was slighted | the institutions kit's seeding; every southern character |
| D-18 | Who holds the first Duke of Varfell's deed as true | canon, institutions | follows D-17 (A → everyone, third confidence) | the deed seeding |
| D-19 | When the royal line fails, who may claim the crown | FA, canon | B — the deed race, with the founding order as a head start | succession; the interregnum |
| D-20 | Does winning a battle take the land? | MB, FA | A — presence only; title passes by an act of seizure | march, raze, seize; the war loop |
| D-21 | Whose word ends a war | FA | B — the seats that wage it | war and peace; succession as peace |
| D-22 | Is a decree public, or paper that must be carried? | FA, SC | A — proclaimed, for decrees; covenants stay in person | orders and obedience batch |
| D-23 | Do orders run down the chain only? | FA, verbs | B — command authority | issue and dispatch |
| D-24 | Does prison silence a ruler's office? | SE, FA | B — custody suspends acts through the seat | arrest as a political act |
| D-25 | Must an officer be present to arrest? | FI, verbs | A — no; the court's reach suffices | the arrest verb |
| D-26 | The standing rule against earlier rulings (one blanket answer) | CORE | yes — the standing rule governs | D-27, D-28, D-31 at once |
| D-27 | A crisis of faith: by rule or by draw | CHAR | B — drawn and seen | conviction, narrative churn |
| D-28 | A scruple: a line or a tendency | CHAR | B — a tendency, drawn | refusals and temptation |
| D-29 | Do favourable circumstances lower the obstacle or raise the speaker? | SC, DICE | B — they raise the speaker | the social obstacle composer |
| D-30 | What an equal opponent costs in argument | SC | A — keep your ruling (half the score) | none new |
| D-31 | Swearing to a seat: a draw, or the joiner's right | verbs, FA | A — a draw | oath, service |
| D-32 | What a man reading a contract tries to read into it | verbs, SC | A — his own interest | construal |
| D-33 | Split the tie verb into tie and knot | verbs, WR | A — split | the verb roster count |
| D-34 | Luck in battle: decides it, or tips it | MB, DICE | B — luck as one named factor among others | battle balance; the battle report |
| D-35 | Do troop numbers stay in the melee dice? | MB | A — no; numbers act through frontage and depth | the melee law |
| D-36 | Three verbs for organising an army, or one | MB, verbs | A — three | military verbs |
| D-37 | The same seed, the same world, on every machine? | GO | B — declare floats now; integer state stays possible later | the port gate; saves and shared seeds |
| D-38 | One random generator for the port, or one draw per key | GO | A — one draw per key | the port's parity tests |
| D-39 | How long a fight lasts | PC | B — long enough to have a position | the duel approach; the grid |
| D-40 | Fighting style: a lean only, or also a trade of attack for defence | PC | A first, B behind a dial | the approach menu |
| D-41 | Does striking first give an edge? | PC | B if D-16 is A (surprise gives a first-exchange edge); else A | ambush, murder |
| D-42 | Who learns of a change of office, and how fast | FI | A — realm-wide, now; B as the test arm | the rumour and claims work |
| D-43 | Does news of a death travel with news of the empty seat? | FI | B — apart | pretenders, false reports |
| D-44 | May a rumour name the wrong person? | FI | A — loss only | rumour |
| D-45 | May an honest investigator reach a wrong conclusion? | FI, verbs | A — no; every error has an author | the detective game |
| D-46 | Does a man learn from failing to find someone? | verbs | B — yes, he alone | dead ends |
| D-47 | Can a person be wrong about himself? | CHAR | B — yes | NPC-004, NPC-012, NPC-021 |
| D-48 | Forgetting: computed, or recorded each season | CORE | A — computed | the claim store |
| D-49 | May a campaign's end reveal what the person never knew? | GO | B — yes, after the line ends | the ending screen |
| D-50 | May the Church's head strip a Church officer? | institutions, FA | B — yes, by a resistible draw | NPC-038; Church politics |
| D-51 | Can anyone judge the Confessor? | institutions | B — a council with the Crown's concurrence | the Confrontation arc |
| D-52 | Forced labour keyed on caste | canon, institutions | your call (tone of canon) | the colonial kit's corvée |
| D-53 | Franchise: a territory's political weight | FA, canon | A — leave archived until something votes | nothing now |
| D-54 | May a convict walk away from a sentence of service? | SC | B — no; the bench or the term ends it | trials |
| D-55 | Who a verdict is for | SC | B — the petitioner | courts as something people want |
| D-56 | Appeal: as of right, or on new grounds | SC, FI | B — on grounds | the appeal row |
| D-57 | Does the world itself wear down (the Thread)? | WR, canon | A — yes, as ground | 49 Thread cases; generation |
| D-58 | What happens to a practitioner at zero coherence | WR, canon | your call | ARC-28 to ARC-30 |
| D-59 | One river of strife, or several stories | WR | B — several stories | the chronicle |
| D-60 | Is leaving a side a move in the realm's strife? | WR | B, narrowed — only leaving a faction's cause or head | the Split |
| D-61 | Arcs that end when a counter fires | WR, CORE | A — a threshold raises a question, never decides | eight arcs and nineteen forced ones |
| D-62 | One question at a time, or a list to choose from | GO, CHAR | B — a list for the player | the scene slate |
| D-63 | The cast: 46, or 46 plus a generated supporting cast | WR, canon | B — with a cap you set | cases, local seats |
| D-64 | Does the seed change the starting realm? | WR | B — some starting state is drawn | replay variety |
| D-65 | How deep the past goes | WR | A — one simulated year | world generation |
| D-66 | New business in a long game | WR, FA | B — after a test shows the world runs dry | late-game churn |
| D-67 | What happens to a world that fails its checks | WR, GO | A by default, B behind a setting | world generation |
| D-68 | Is farm work an act someone chooses? | SE | B — yes | yield, the steward's game |
| D-69 | Does a lasting famine keep speaking? | SE | A — reported once, repaired edge | famine as news |
| D-70 | How the world's own motion draws | SE, WR | B — on the one ladder | weather, harvest, wear |
| D-71 | May a town be founded or die? | SE | A — the map is fixed; a founded household can fail | founding |
| D-72 | A lord over an empty land | SE, FA | A — leave it | famine as politics |
| D-73 | The common people: full actors or a few heavy moves | CHAR, SE | B — a few heavy moves | cohort deliberation |
| D-74 | The witness step reads more than Layer 1 lists: fix the code or the list | CORE, FI | B — fix the code (answerable without you) | one Layer 1 row |

---

## Group 1 · Layer 1 and how battles are fought: auto-resolve, units, the duel round, the battle's result

**The common context.** Layer 1 (the code architecture you ratified) has three rules that meet your
2026-11-12 battle intent (Football Manager, Total War, Bannerlord, Ogre Battle, Unicorn Overlord):

- *One resolver.* "No second resolver. No auto-resolve formula. No fast path." A fight is decided by
  exactly one function, at every depth of play, and a summarised fight and a played fight "agree exactly,
  because they are the same slice" (not on average).
- *No unit class.* Soldiers are persons, counted at weight. Your ruling of 2026-10-28 (ED-IN-0306)
  amended this for armies: a faction's order of battle (formations, subformations, troop types, tactic,
  strategy) is now a typed record the season loop reads. A unit is a grouping row on that record.
- *Grid squad combat is the same thing one scale down*: the squad is the faction's members present, each
  one a person.

Your intent asks for "auto-resolve", for a hierarchy of army, unit, subformation and troops, and for duels
inside battles. Every lane that looked found that your own sentence, *"the cell-level battle that a player
commands and the auto-resolved battle must run the same cell-based resolver"*, already reconciles the
first two with Layer 1 as written. The options below exist because the *referent games* do it the other
way, and you should choose knowingly.

### D-01 · Auto-resolve: the same battle run for you, or a quicker sum · MB, CORE
**ANSWERED** (A-1): The same resolver, run automatically


> **ANSWERED 2026-11-12: A** (`DECISIONS_ANSWERED.md` A-1).

**The situation.** Today a battle the player does not watch runs the same cell-by-cell battle engine as a
watched one; an estimate before battle is that engine sampled a few hundred times. Total War, by contrast,
"auto-resolves" a battle by comparing the two armies' statistics in one quick sum, which is why its
auto-resolved and played battles often disagree.

**The question.** When you say "auto-resolve", do you mean the full battle run for you, or a separate
quick calculation?

**Option A — the same battle, run for you.** The battle you skip is the battle engine run on your
standing orders (or the approach you picked); a battle you command is the same call with your decisions
at each window; a recorded battle replays exactly.
- *Feels like:* war is the same whether or not anyone watches. Your standing orders, formations and
  loadouts matter to every battle, including the ones you skip.
- *Costs:* every unwatched battle costs a full run (about 20 ms for 600 a side); an estimate costs samples
  of it. Layer 1 stands untouched.

**Option B — a quick sum.** A separate cheaper comparison of the two armies for battles nobody plays.
- *Feels like:* unwatched war is fast and the estimate is free, but a played and a skipped battle agree
  only on average, and standing orders and arrangement stop mattering in any battle you skip.
- *Costs:* amends Layer 1's one-resolver rule (holonic §27.2) and the fidelity rule (§C.4); the four
  order-of-battle verbs decide nothing in skipped battles.

**Recommendation.** A (mass-battle addendum and military verbs lane): your own "one path" sentence and the
2026-07-08 doctrine both say it. This lane agrees.

**If you do not answer.** A is assumed; nothing in the suite builds toward B.

**Blocks.** The managed-battle surface; the delegated battle with standing orders; the four
order-of-battle verbs; the estimate's sampling budget; removal of the old second battle path in the
registered tree.

**Sources.** `audits/04_MB_audit_addendum_B.md` §B5.4 (a), §B11 item 1; `audits/14_VERBS_MILITARY.md` §9
item 2; `audits/11_GO_audit.md` §5.2; `architecture/holonic_ARCHITECTURE.md` §27.2 (:984-990);
`architecture/meta/03_VERBS_AND_LOOPS.md` §C.4 (:146-153); `architecture/meta/04_CODE_ARCHITECTURE.md`
:761, :788.

### D-02 · A unit: a line on the army's sheet, or a thing in the world · MB
**ANSWERED** (A-2): A row of data


> **ANSWERED 2026-11-12: A** (`DECISIONS_ANSWERED.md` A-2).

**The situation.** Your hierarchy is army, unit, subformation, troops. Today a unit is a row on the army's
record that names the persons it draws on and how many; inside a battle, the engine builds temporary unit
values and throws them away at the end. ARC-07 asks for "a condition on a unit" (a regiment that is
cursed, famous or feared).

**The question.** Is a unit a row on the army's record, or a thing with its own identity that people can
know, fear, swear to and remember?

**Option A — a row.** A unit is a grouping of persons' headcounts with columns: kind, arrangement,
loadout, orders, officer, experience, pay arrears.
- *Feels like:* "the regiment that held the bridge" is a story about its officer and its men, carried in
  their memories. A unit has no memory but theirs.
- *Costs:* nothing to Layer 1 (as amended on 2026-10-28). ARC-07 is re-read as claims held by the men.

**Option B — a thing.** A unit has identity: people hold beliefs about it, swear to it, fear it; it carries
its own history, reputation and training; forming, training and disbanding act on it.
- *Feels like:* regiments become characters of the world, as in Ogre Battle's named squads with a
  reputation.
- *Costs:* amends Layer 1's "no unit class" rule (04 §C.5.1) a second time; the knowledge model gains a new
  kind of thing a belief can be about; every reader of beliefs must handle it.

**Recommendation.** A (mass-battle addendum, military verbs): it is what you ruled on 2026-10-28. Note that
Ogre Battle's "small squads of named characters" are already Option A: a squad of named persons is exactly
what Layer 1 describes, and the suite builds it on the duel round (D-03), not as a unit. This lane agrees.

**If you do not answer.** A is assumed.

**Blocks.** The army hierarchy columns; unit loadout and weapon-in-hand; the four order-of-battle verbs;
ARC-07.

**Sources.** `audits/04_MB_audit_addendum_B.md` §B5.4 (b), §B11 item 2; `audits/14_VERBS_MILITARY.md` §9
item 1; `architecture/meta/04_CODE_ARCHITECTURE.md` :802, :813 (ED-IN-0306);
`proposals/04_MB_cell_hierarchy_as_data.md`; `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md`.

### D-03 · A duel inside a battle: called from inside, or played as separate acts · PC, MB
**ANSWERED** (A-4): Called from inside the battle, as a nested contest


> **ANSWERED 2026-11-12: A** (`DECISIONS_ANSWERED.md` A-4).

**The situation.** Your personal-combat intent asks for duels and grid skirmishes that can happen inside a
mass engagement, played or automatic. The duel round proposal keeps one resolver: the automatic duel, the
grid attack, a duel inside a battle and an unwatched fight are all the same personal-combat function, with
the fighting approach supplied by a chooser (you, or the NPC's own temperament). That part is not in
question. What is open is *how a battle reaches a duel*. Layer 1 caps how deeply one contest may run
another inside itself, without saying what the cap is.

**The question.** When two officers meet inside a battle, does the battle call the duel from inside itself,
or does each attack become its own separate act in the season?

**Option A — called from inside, as a nested contest.** The battle hands the duel function in; a duel is
counted against the nesting cap, with a clear error if the cap is reached. Each kind of decider handed in
(the player, the NPC, a squad member's standing order) is declared once as one class of input.
- *Feels like:* a duel between two captains happens in the middle of the battle turn, and its result
  feeds the next turn of the battle at once.
- *Costs:* a default nesting cap must be set; Layer 1's adapter row is read as admitting "callables
  supplied for persons" as one declared class.

**Option B — separate acts.** The grid or battle runs no person-scale loop of its own: each attack is its
own act with its own call, and the fight's state (wounds, position) is written to the world between acts.
- *Feels like:* a grid battle unfolds across scenes; a duel is its own beat in the season.
- *Costs:* a carrier for a fight's in-progress state (the held "seeded damage" question) and a rule for a
  battle that spans acts. No nesting at all.

**Recommendation.** No lane chose; the personal-combat addendum lists both. This lane recommends A: it
keeps a battle one act and its duels inside it, needs no new carrier, and the cap is a single number.

**If you do not answer.** The duel round's steps 1 to 4 (the round, the private stream, the approaches,
the chooser) proceed; step 5 (handing the duel to a battle) waits.

**Blocks.** Duels inside a field; grid squad combat; the ruled pause-for-a-decision contract, which covers
one pause per call and not a consult inside a round (the same answer settles that); the deferred
"discrete player-action menu" reopen condition of ED-PC-0007, which three approaches fire.

**Sources.** `audits/03_PC_audit_addendum_B.md` §B4 (table "Where it does not fit cleanly"), §B10;
`proposals/03_PC_duel_round_and_approach_B.md` §6, §8 items 3–5, 7; `audits/04_MB_audit.md` §15;
`architecture/holonic_ARCHITECTURE.md` §39.3 (:1397-1402), §44.3 (:1679-1686).

### D-04 · What a battle reports: won/lost/drawn, or how decisively · MB
**ANSWERED** (A-3): An end state: won, lost or drawn


> **ANSWERED 2026-11-12: A** (`DECISIONS_ANSWERED.md` A-3).

**The situation.** Every other contest in the game reports a margin graded on one four-step ladder
(overwhelming, success, partial, failure). The battle engine returns only a winner, and the season makes
two outcomes from it. Layer 1 says a contest returns a margin. You already allowed personal combat to
report won/lost (2026-09-03).

**The question.** Should a battle report only who won, or how decisively, on the same ladder as everything
else?

**Option A — won, lost or drawn.** Read off which side broke or conceded, as combat's is.
- *Feels like:* a battle is won or not; how hard it was shows in the casualties and the report.
- *Costs:* extends the 2026-09-03 combat exemption to battles (needs your word, as combat's did).

**Option B — a margin on the one ladder.** The battle returns a net (for example the difference of the
two sides' broken shares) and the ladder grades four outcomes, each with its own consequences.
- *Feels like:* a crushing victory can take a title where a narrow one only holds the field; battles
  differ in kind.
- *Costs:* new design for four outcomes' consequences, and thresholds nobody has calibrated.

**Recommendation.** A (mass-battle addendum), by the combat precedent. This lane agrees for now; B is a
good later step once D-20 (does a win take land) is settled.

**If you do not answer.** A.

**Blocks.** The battle's typed result; the season's reading of it; the delete of the module's uncalibrated
four-way label.

**Sources.** `audits/04_MB_audit_addendum_B.md` §B5.4 (c), §B11 item 3; `architecture/meta/04_CODE_ARCHITECTURE.md` :774-786, :1050.

---

## Group 2 · The dice and the score: what a roll is made of

**The common context.** Two rulings point in different directions. ED-833 (2026-05-15) adopted a smooth
bell-curve sampler for every system. The social roll was later built on whole dice you can count, and
ED-IN-0351 withdrew combat's ratification and reopened "what a score is worth" for combat and the social
contest. These four questions decide what every non-combat roll in the game feels like; answer D-05 and
D-06 together.

### D-05 · Which dice the non-combat rolls use · DICE
**ANSWERED** (A-5): The bell curve everywhere (against the register's recommendation)


> **ANSWERED 2026-11-12: B, the bell curve everywhere** (`DECISIONS_ANSWERED.md` A-5), against the
> recommendation below. D-06's answer is the re-centring.

**The situation.** Personal combat draws from a bell curve; the social roll and the battle use whole dice
with exact, countable odds. At the shipped settings the whole dice fail 74% of the time and the bell curve
86%: they are not interchangeable.

**The question.** Do non-combat rolls keep whole dice, or move to the bell curve as ED-833 says?

**Option A — whole dice, as built.**
- *Feels like:* odds a player can count ("two dice, two successes needed"), exact and displayable.
- *Costs:* the port carries two samplers. Narrows ED-833 to combat.

**Option B — the bell curve everywhere.**
- *Feels like:* fractional pools and obstacles are natural and leverage is exactly even at every size;
  there are no dice to show.
- *Costs:* every non-combat act becomes about ten points harder unless the sampler is re-centred; the exact
  odds table and the fraction rule are deleted; every season hash moves.

**Recommendation.** A (dice audit). This lane agrees.

**If you do not answer.** A; the exported dice rules are written for it.

**Blocks.** The exported face rule and band edges; the social roll; the port's sampler list.

**Sources.** `audits/10_DICE_audit.md` §11; `proposals/10_DICE_exported_face_rule_and_band_edges.md`;
`proposals/10_DICE_one_roller_one_fraction_rule.md`.

### D-06 · What a skill score is worth outside a fight · DICE, SC
**ANSWERED** (A-6): Score plus a base, floor five


> **ANSWERED 2026-11-12: B** (`DECISIONS_ANSWERED.md` A-6), calibrated together with D-05.

**The situation.** Outside combat the score *is* the dice pool: two equal opponents succeed 28% of the
time, and one point of skill is worth about eleven percentage points. Combat instead uses the score plus a
base, with a floor of five dice.

**The question.** Should non-combat rolls use the score alone, or the score plus a base as combat does?

**Option A — the score is the pool (as built).**
- *Feels like:* social acts are hard; each point of skill is a big jump.
- *Costs:* nothing now; the bell-curve approximations behave poorly at small pools.

**Option B — the score plus a base, floor five.**
- *Feels like:* equals succeed about 65% of the time; a point is worth about five; skill is a steady edge
  rather than a cliff.
- *Costs:* every non-combat outcome band moves; it is two numbers on one row, so an edit, not a build.

**Recommendation.** The dice lane gives both without choosing. This lane recommends B: one way of turning
a score into dice across combat and everything else (a calculation consistent with its siblings), and it
gives the "we do not do deterministic" task draw room to matter (the draw delivers only 16–42% of its
intended effect at today's small pools, 49–70% at five dice).

**If you do not answer.** A stays.

**Blocks.** Every non-combat band; the task draw for uncontested verbs; social contest calibration.

**Sources.** `audits/10_DICE_audit_addendum_B.md` §5.6 item 2; `audits/16_PESSIMIST_DICE.md` §6 (last
paragraph); ED-IN-0351.

### D-07 · Talent and training: one number or two · PC, CHAR
**ANSWERED** (A-7): Two numbers (against the register's interim recommendation)


> **ANSWERED 2026-11-12: B, two numbers** (`DECISIONS_ANSWERED.md` A-7), against the interim
> recommendation below.

**The situation.** A fighter's dice and obstacle come from one number: the larger of his natural attribute
and his trained skill, plus practice. A gifted untrained man and a trained ungifted man are the same number.

**The question.** Should talent and training enter a roll as one number or two?

**Option A — one number (as built).**
- *Feels like:* simple; a fighter is one figure.
- *Costs:* talent and schooling cannot be different kinds of fighter.

**Option B — two.** For example the attribute sets dice and the skill sets the obstacle one is attacked
against.
- *Feels like:* the brawler and the fencing master are different in kind.
- *Costs:* a second input on every contest; re-calibration.

**Recommendation.** No lane chose; already your open question under ED-IN-0351. This lane recommends A until
D-06 is answered, since B multiplies the work D-06 already moves.

**If you do not answer.** A.

**Blocks.** The combat pool and obstacle; held "seeded damage" step; character sheets.

**Sources.** `audits/03_PC_audit.md` §11 item 2; ED-IN-0351.

### D-08 · What a wound costs a roll · DICE, PC
**ANSWERED** (A-8): B: a level against the roll, as combat spends it (register's recommendation)


**The situation.** As ruled (ED-PC-0005, ED-PC-0006), a wound adds a small fixed fraction to the obstacle
(0.15 per wound). That bites most on a middling roll and fades for an expert (2.4 points at eight dice).
Combat itself spends wounds as a level against the roll's spread.

**The question.** Keep the fixed fraction, or make a wound cost the same share of any roll?

**Option A — a small fixed cost (as ruled).** Experts shrug off wounds.
**Option B — a level against.** A wound costs 5 to 10 points at every pool, stacking under the soft cap with
other disadvantages; experts feel wounds as much as novices.

**Recommendation.** The dice addendum was written for A, under whole dice. Now that every roll is on the
bell curve (D-05 answered B) and scores carry a base (D-06), this lane recommends B: a wound then costs
the same share of the roll's spread as every other disadvantage, through the same capped channel, which is
how combat already spends it. A fixed fraction of the obstacle would be a second ladder for one quantity.

**If you do not answer.** A, as ruled (ED-PC-0005, ED-PC-0006).

**Blocks.** The wound rows of the capability-to-dice map.

**Sources.** `audits/10_DICE_audit_addendum_B.md` §5.6 item 1, §5.4.

---

## Group 3 · Other places where your stated intent meets ratified Layer 1

**The common context.** Each of these is a sentence of yours (a requirement, the institutions brief, the
standing rule) against a ratified Layer 1 row. Layer 1 is never edited to match code; it is edited only
when you choose the reading that needs it.

### D-09 · A turn: a round of simultaneous choices, or short chains of acts · CORE
**ANSWERED** (A-9): A short sequence (register's recommendation)


**The situation.** One of the nine requirements says "chains of events within a scene are probabilistic".
Today a season round collects everyone's choices and then applies them in one fixed global order (Layer 1
ratifies that order); a "scene" is a slot in a person's budget, not a sequence. So nothing inside a scene
can hang on how the step before it went: of 525 acts measured, the order matched the chooser's intent no
more often than chance.

**The question.** Is a scene a budget slot in a round of simultaneous choices, or a short sequence in which
each step depends on how the last one landed?

**Option A — a budget slot.** Keep the global order; read the requirement as chains *across* rounds.
- *Feels like:* a turn is everyone choosing at once, then the world resolving.
- *Costs:* the requirement keeps a subject only across seasons; "he argued, failed, and so drew his sword"
  cannot happen within one scene.

**Option B — a short sequence.** A scene's steps are applied in the chooser's order, and a step can hang on
the band of the one before; the ratified order becomes an order over scenes.
- *Feels like:* scenes have shape: persuade, and if that fails, threaten; sneak in, and if seen, run.
- *Costs:* re-keys the ratified fold order (#353 §27); one re-pin of every seeded result.

**Recommendation.** B (core pessimist lane). This lane agrees: it is the only reading under which the
requirement means something inside a scene.

**If you do not answer.** A; the proposal is held.

**Blocks.** The fold order; the requirement's measurement; any conditional play inside a scene (the duel's
approach per phase, the hearing's moves).

**Sources.** `audits/16_PESSIMIST_CORE.md` §6 (survivor); `proposals/16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md`;
`engine/season/requirements.yaml` R-09.

### D-10 · Governance: the season loop's own verbs, or a separate module · FA
**ANSWERED** (A-10): The loop's own verbs


**The situation.** Your standing requirement says every subsystem should be a registered module (typed
input, typed outcome, no held state, reached by a composition row). Layer 1 says an institution never acts
(only persons do) and your ruling ED-IN-0283 says the faction scale "has no code of its own". Governance
today is the season loop's own verbs: issue, convene, confer, revoke.

**The question.** Is governance the loop's own verbs (its standalone game a scenario on the season loop),
or a separate module of pure functions?

**Option A — the loop's own verbs.** One code path; the faction game stands alone as a scenario.
**Option B — a governance module** holding the authority checks and the succession and election tallies,
reached by composition rows. Puts the write gate's own rules behind a string-resolved role and gives them a
second home.

*The games do not differ; the architectures do.*

**Recommendation.** A (governance lane, institutions synthesis). This lane agrees: B duplicates rules that
live once today.

**If you do not answer.** A; no governance module is built.

**Blocks.** How the governance game "stands alone"; the institutions kit's home.

**Sources.** `audits/06_FA_audit.md` §11 item 2; `audits/15_INSTITUTIONS_SYNTHESIS.md` §8.2 L-5.

### D-11 · May training gate an act (only a surgeon may operate)? · CORE, CHAR
**ANSWERED** (A-11): No, as ruled


**The situation.** Layer 1 rules that a capability supplies dice and gates nothing; the one exception is
Thread Sensitivity. So anyone may try anything; skill changes the odds. An unlettered man may try to forge
a writ and will usually fail.

**The question.** May a verb require a trained capability before it can be attempted?

**Option A — no (as ruled).** Expertise shows as outcome, never as access.
**Option B — yes, by declaration.** A verb may name a capability threshold. Professions become access: only
a trained advocate pleads, only a surgeon tends a grave wound; different people get different menus.
Overwrites a ratified Layer 1 row (D-33, §B.7).

**Recommendation.** No lane chose; the proposal builds A in full and specifies B's one grammar edit as held.
This lane recommends A: B is the strongest lever on player variety the tree does not pull, but it adds a
second way to block an act, and access by profession can be reached later through seats (only the court's
advocate may plead *in that court*).

**If you do not answer.** A.

**Blocks.** The capability authoring surface's `requires` grammar.

**Sources.** `audits/01_CORE_audit_addendum_B.md` §9; `proposals/01_CORE_capability_authoring_surface.md`
Part three.

### D-12 · May rank or office add to a roll? · institutions, SC
**ANSWERED** (A-12): YES: a seat carries a modifier (against the register's recommendation)


**The situation.** The institutions brief asks every institutional act to state "what roll and what
modifiers (personality, affiliation, office, evidence, publicity)". Layer 1 §B.7 says a seat adds no verb
and no modifier ("rank supplies dice and gates nothing"). Two proposals add a rank term anyway: one for how
far a person stands above or below the seat he exercises, and a die for a seat on the bench.

**The question.** May holding an office make a roll easier?

**Option A — no.** Office decides *what you may do* and *how others regard you* (regard, legitimacy,
standing in the room), which already reach the odds through the hearer; no flat bonus. The two proposals
are rewritten to read regard.
**Option B — yes.** A seat carries a modifier; amends a ratified Layer 1 row graded STRUCTURAL.

**Recommendation.** The synthesis names it without choosing. This lane recommends A: the brief's "office"
modifier is already met through regard, and B is a second channel for the same effect.

**If you do not answer.** The kit adds no office modifier; the two other proposals stay as written until
reconciled.

**Blocks.** The institutions kit's rolls; the bench's dice table; the turnover proposal's standing term.

**Sources.** `audits/15_INSTITUTIONS_SYNTHESIS.md` §8.2 L-1; `proposals/14_VERBS_BINDING_C_turnover.md`;
`proposals/13_SC_tuning_tables.md` T4.

### D-13 · Three new facts on a seat · institutions
**ANSWERED** (A-13): YES (register's recommendation)


**The situation.** Layer 1 lists what a seat is (post, body, scope, remit, conferral, revocation, upkeep).
The institutions kit needs three things the list does not hold: whose clerks an order must pass through
before it binds, what hands a paper needs, and an audit when the holder leaves. Earlier changes to this list
were your rulings.

**The question.** May the seat gain these three facts?

**Option A — no.** The kit drops its chancery and exit audit; orders bind at issue.
**Option B — yes.** Layer 1's seat list is amended by ruling; a seat that declares none behaves as today.

**Recommendation.** No lane chose. This lane recommends B: each key is optional data, and the synthesis has
already used it to close another question (whether an order binds at issue or at entry) as "both, by row".

**If you do not answer.** The keys stay in the proposals as written, unapplied.

**Blocks.** The institutions kit's chancery, paper and audit.

**Sources.** `audits/15_INSTITUTIONS_SYNTHESIS.md` §8.2 L-2, §10 table row 1.

### D-14 · A vote: a draw on the voter, or the voter's own act · institutions, SC
**ANSWERED** (A-14): A: a draw on the voter, inside the presiding person's act


**The situation.** Your standing rule forbids a vote that is a fixed count of commitments. The ballot now
draws each member's vote inside the presiding person's act. Layer 1 says only a person acts, by his own
choice.

**The question.** Is a member's vote a draw on his inner state (like his score when opposed), or an act he
forms himself?

**Option A — a draw on the voter.** Cheap; one act decides the ballot; conformant under that reading.
**Option B — his own act.** Each member forms a vote verb; the tally reads those. Costs a scene per voter.

**Recommendation.** A (synthesis reading). This lane agrees.

**If you do not answer.** A.

**Blocks.** Elections, councils, sentencing benches.

**Sources.** `audits/15_INSTITUTIONS_SYNTHESIS.md` §8.2 L-3.

---

## Group 4 · Where deaths come from

**The common context.** Today nobody dies except by another's act, and with duels refused and murder not
built, seats never empty: zero deaths in six seasons at seed 0. Succession, vacancy, inheritance, the
detective game and most of the provided arcs wait on someone dying. Natural death was deferred by your
ruling ED-IN-0317, which leaves the values to you; ED-IN-0337 makes violence exceptional and names
"criminal contexts" without building one. Answer these two together.

### D-15 · Natural death: on or off · WR
**ANSWERED** (A-15): A: on, after the 46 ages are authored


**The situation.** The illness and ageing mechanisms exist and are switched off; every person's age is
zero.

**The question.** Should people die of illness and age?

**Option A — on, after the 46 ages are authored.** About one to three natural deaths in a twelve-season
campaign, almost all after a season of visible illness.
- *Feels like:* the cast turns over; seats empty with nobody to blame; vacancy, obligation and conferral
  follow.
- *Costs:* you author the cast's ages and set (or accept) a rate; seeded results move once.

**Option B — off, as now.** Successions open only when someone is killed; a realm of permanent incumbents
until violence works.

**Recommendation.** A (happenings lane; the world-motion proposal; the game-level pessimist puts it first in
its order). This lane agrees.

**If you do not answer.** B (the mechanism is reshaped as a drawn fall of the body, but stays dark).

**Blocks.** Succession and inheritance in play; the happenings "first ring"; the throne question (D-19)
being reachable at all; the narrative churn's succession family.

**Sources.** `audits/09_WR_audit.md` §11 item 2; `audits/22_HAPPENINGS.md` §4 item 1;
`audits/16_PESSIMIST_GAME.md` §7.2 step 1; `audits/20_NARRATIVE_CHURN.md` §10 (note);
`proposals/09_WR_world_motion.md` edit 4; `proposals/16_PESSIMIST_WR_C_illness_on_the_body_ladder.md`;
`proposals/22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md`.

### D-16 · May a person commit murder? · PC, FI
**ANSWERED** (A-16): A: yes, rarely


**The situation.** Violence today is war, duel, arrest and self-defence. Two provided cases (NPC-088,
ARC-31) ask for a killing with no institutional context. The detective game currently investigates only
crimes seeded at world-build.

**The question.** May a person, of his own motive, try to kill another?

**Option A — yes, rarely.** Only where he has both a grievance (a deed he holds against the target, or a
rival claim to the target's seat) and hatred below a threshold; reaching a guarded target is a draw, and a
failure means he is caught and detained. Held to fewer than one attempt per seed-season by its gate.
- *Feels like:* a ruler dies by a hand only when someone hates him enough; murders arise from the world and
  feed the investigation game.
**Option B — no.** Murders exist only as seeded history and case seeds.

**Recommendation.** A (happenings lane). This lane agrees.

**If you do not answer.** B.

**Blocks.** The detective game's supply of fresh crimes; NPC-088 and ARC-31; the "striking first" question
(D-41) only matters if A.

**Sources.** `audits/22_HAPPENINGS.md` §4 item 2; `proposals/22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md`;
`audits/03_PC_audit.md` §11 (named conflict with ED-IN-0337).

---

## Group 5 · The founding order, the crown's succession, and how wars end

**The common context.** Your fixed point (2026-11-12): nobility is by deed, and the Secession War's
accomplishments ranked the first King first, the first Duke of Hafenmark second and the first Duke of
Varfell third. Canon's timeline (ratified) says the coalition was "primarily northern", the south
"peripheral", and the caste against the southern Einhir is the consequence of "the south's exclusion from
the war coalition's leadership". All four institutions lanes found the two cannot both be read literally.
D-17 must be answered before D-18; D-19 depends on how D-17 and D-15 land; D-20 and D-21 decide what a war
can change.

### D-17 · Canon's line on the south in the Secession War · canon, institutions
**ANSWERED** (A-17): A: fought, ranked third, relegated despite it


**The situation.** If the first Duke of Varfell won the war's third-greatest deed, the south was not simply
excluded from it. The suite has drafted (not applied) the canon wording for each reading.

**The question.** Did the south fight and get slighted, or was its deed recognised only later?

**Option A — fought, ranked third, relegated despite it.** Canon lines 76, 90 and 96 are reworded: the south
fought and won the third deed, and the settlement ranked it last and seated none of its commanders.
- *Feels like:* the founding is one story the whole realm holds; Varfell's grievance is a deed
  under-rewarded, on the same ledger as Baralta's; Vaynard is a claimant inside the order.
- *Costs:* three ratified canon sentences change.

**Option B — acknowledged late and grudgingly.** Canon stands, with one sentence added: the north
acknowledged Varfell's deed late; the south never doubted it.
- *Feels like:* the caste is a gradient in legitimacy itself; Vaynard is a great lord at home, tolerated at
  court, and a revolutionary against the order.
- *Costs:* one added canon sentence; one seeding change in the kit.

**Recommendation.** The kit is written for A; no lane takes it, since it is canon. This lane: either is a
good game; A is the cleaner fit to your "nobility by deed" statement, B keeps more of existing canon and
gives the south a sharper story. Your call.

**If you do not answer.** Canon is untouched (B's added sentence is not applied either); the kit's seeding
ships marked as assumption under A.

**Blocks.** The institutions kit's seeding of founding deeds (and the three founding attestations' counts,
offered as 5, 3, 2 with only the order yours); D-18; D-19's odds; every southern character's arc.

**Sources.** `audits/15_INSTITUTIONS_SYNTHESIS.md` §4.6 (drafted wording A1–A4), §10 item 1;
`audits/15_INSTITUTIONS_COLONIAL.md` §11 item 1; `audits/15_INSTITUTIONS_PAPACY.md` §13 item 4;
`audits/15_INSTITUTIONS_VENICE.md` §4.4; `proposals/15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`;
`proposals/15_INSTITUTIONS_COLONIAL_D_accomplishment.md`; `canon/03_canonical_timeline.md` :76, :90, :96.

*Separately, offered as housekeeping with no game choice in it:* canon line 92 names a "Coup Counter", a
stored counter Layer 1 refuses; the synthesis offers replacement wording (A4).

### D-18 · Who holds the first Duke of Varfell's deed as true · canon, institutions
**ANSWERED** (A-18): Follows D-17 A: realm-wide, at the third confidence


**The situation.** The founding deeds are seeded as beliefs people hold at some confidence.

**The question.** Is Varfell's founding deed held realm-wide, or at full in the south and thinly in the
north?

**Option A — everyone, at the third confidence.** One fact, realm-wide; the caste is separate from the
house's standing.
**Option B — the south at full, the north discounted.** Legitimacy itself is a gradient; Vaynard's arc
grounds in it.

**Recommendation.** Follows D-17: A with A, B with B (Byzantine lane).

**If you do not answer.** Follows D-17's default (A in the seeding).

**Blocks.** The deed ledger's seeding.

**Sources.** `audits/15_INSTITUTIONS_BYZANTINE.md` §14 item 2.

### D-19 · When the royal line fails, who may claim the crown · FA, canon
**ANSWERED** (A-19): B: the deed race


**The situation.** Today one row says the heir succeeds the King. The built realm reaches a failed line in
two deaths, and nothing says what happens next.

**The question.** When the line fails, is there an ordered line of houses, or a race decided by deeds?

**Option A — an ordered line.** The heir's title, then Hafenmark's seat, then Varfell's; a later title may
claim only when every earlier one is vacant; each claim is a draw and may be contested.
- *Feels like:* dynastic. Killing or discrediting an heir is a move toward a crown; Varfell is always
  third.
**Option B — the deed race.** The heir, the consort, the princess and the heads of both houses may each
claim; odds come from what others believe of each claimant's deeds, so the founding order is a head start,
not a right.
- *Feels like:* a marshal who wins the war of the interregnum can be King; Hafenmark can be passed over.
**Option C — the royal family only.** A house takes the throne by conquest or not at all.

**Recommendation.** The governance pessimist lists A and B without choosing; the happenings lane recommends
the deed race (B). This lane agrees with B: it is "nobility by deed" applied to the crown.

**If you do not answer.** Only the heir row exists; a failed line leaves the throne empty.

**Blocks.** The throne-is-never-stranded proposal; the founders' deed seeding; turnover and succession
draws.

**Sources.** `audits/16_PESSIMIST_FA.md` §5; `audits/22_HAPPENINGS.md` §4 item 3;
`proposals/22_HAPPENINGS_B_the_throne_is_never_stranded.md`.

### D-20 · Does winning a battle take the land? · MB, FA
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A: a won battle gives presence only; title passes by a separate act of seizure


**The situation.** As built (and per #453), winning a field gives presence; title passes only when someone
seizes it afterwards. Layer 1's faction contract says a defeat can cost "holdings and seats". The two
contradict each other.

**The question.** Does a won battle transfer title?

**Option A — no.** Presence only; title passes by a separate act of seizure.
- *Feels like:* winning a battle opens a door; holding the land is another act, which can fail.
**Option B — yes.** What a defeat costs includes holdings and seats directly.
- *Feels like:* decisive battles; conquest is faster.

**Recommendation.** The physical verbs lane names it; the governance addendum carries it. This lane
recommends A: it keeps one owner of title (seizure) and makes occupation a story of its own.

**If you do not answer.** A, as built.

**Blocks.** March, raze and seize; what a defeat's result writes (with D-04).

**Sources.** `audits/14_VERBS_PHYSICAL.md` §10.4 D-2; `architecture/10_FACTIONS_AND_DEPLOYMENT.md` §3.

### D-21 · Whose word ends a war · FA
**ANSWERED** (A-20): B: the seats that wage it


**The situation.** Layer 1 says a realm is at war while anyone still holds a live commitment to the war.
With rallying built, most wars would never end: one zealot keeps it alive.

**The question.** Does a war live while anyone is committed to it, or while the seats that wage it are?

**Option A — any committer (as ratified).** War is a popular fact; peace is a negotiation with every
zealot.
**Option B — the seats that wage it.** War lives while someone who can order a muster is committed; it
passes to his successor; it ends by the word of those officers. Popular commitment is how many come when
called.
- *Feels like:* wars begin and end by named persons in named seats, and a succession can be a peace.

**Recommendation.** B (governance addendum). This lane agrees. It narrows a ratified Layer 1 sentence.

**If you do not answer.** B is held behind its revert.

**Blocks.** The war-lives-in-seats proposal; the binding verbs' batch E.

**Sources.** `audits/06_FA_audit_addendum_B.md` §B6.2 item 1; `proposals/06_FA_war_lives_in_seats_B.md`;
`proposals/14_VERBS_BINDING_E_war_seats.md`; Layer 1 D-48 and `04` :460.

---

## Group 6 · Orders and obedience: how far a ruler's word reaches

**The common context.** Your ruling ED-IN-0292 (1) refused to place a writ in its addressee's hand ("just
say no for now"). The code then required the addressee to hold the writ before he could answer it, so no
decree is ever answered. Under your standing rule, obeying is always a choice and a draw; these questions
decide who can be ordered, how the order arrives, and what removing a ruler does. Answer D-22 and D-23
together.

### D-22 · Is a decree public, or paper that must be carried? · FA, SC
**ANSWERED** (A-21): A: proclaimed


**The situation.** A ruler issues a decree; today nobody can answer it.

**The question.** How does a decree reach the person it orders?

**Option A — proclaimed.** Whoever learns a decree was issued knows its terms and may answer it without
holding the paper. Covenants and challenges stay in person.
- *Feels like:* authority is legible and cheap; defiance is public; a decree cannot be lost, intercepted or
  forged on the road.
- *Costs:* mints no paper into anyone's hand, so it keeps the ruling's text.
**Option B — delivered by hand (the ruling as it stands).** Only a held writ binds; the issuer or a
messenger must give it.
- *Feels like:* orders are logistics: they miss, are stolen, forged, arrive late. Obedience is rare and
  local.
- *Costs:* a delivery occasion and a long-range give (one execution in two seasons today).
**Option C — served by office.** A writ from a seat whose reach covers the addressee is placed in his hand
directly; answering is the next round.
- *Feels like:* realm-wide obedience as a mechanic. *Costs:* reopens your "no" for writs.

**Recommendation.** A (governance lane), keeping B's shape for covenants. The social verbs lane works under
B and asks whether to reopen to C. This lane recommends A. If your "no" meant that an addressee should not
learn a writ's terms without holding it, A is wrong and the answer is B with a delivery occasion.

**If you do not answer.** A for decrees (the proposal as written).

**Blocks.** The orders-and-obedience batch; the decree-binds proposal; the governance playable scenario;
the Byzantine chancery (D-13).

**Sources.** `audits/06_FA_audit.md` §11 item 1; `audits/14_VERBS_SOCIAL1.md` §15 D1;
`audits/15_INSTITUTIONS_BYZANTINE.md` §14 item 1; `audits/14_VERBS_BINDING.md` §13.4 item 2;
`proposals/06_FA_decree_binds.md`; `proposals/14_VERBS_SOCIAL1_B_documents_and_obedience.md`.

### D-23 · Do orders run down the chain only? · FA, verbs
**ANSWERED** (A-22): B: command


**The situation.** By your ruling ED-IN-0256 (4), a seat may order whoever stands in its land. Read
literally, any official whose district contains the King's residence may order the King.

**The question.** Is authority territorial, or a chain of command?

**Option A — territorial (today).** A seat orders whoever stands in its land; the King's officers command
him in his own city.
**Option B — command.** A seat orders its sworn men, the holders of seats it may revoke, and the unseated in
its land. A writ to a superior is a petition, not a command.

**Recommendation.** B (binding verbs lane), behind its revert. This lane agrees. It narrows a ruled basis
for two verbs only.

**If you do not answer.** B ships behind its revert.

**Blocks.** Issue and dispatch; the binding verbs' batch D.

**Sources.** `audits/14_VERBS_BINDING.md` §13.4 item 1; `proposals/14_VERBS_BINDING_D_orders.md`.

### D-24 · Does prison silence a ruler's office? · SE, FA
**ANSWERED** (A-23): B: custody suspends acts through the seat


**The situation.** A detained duke cannot travel but can still issue decrees, convene and dispatch through
his seat, since acts through a seat need no presence.

**The question.** Does custody stop a ruler acting through his office?

**Option A — travel only.** A captive ruler rules by writ from his cell; removing him needs a revocation.
Arrest is leverage, not deposition.
**Option B — custody suspends acts through the seat.** Arrest is a coup's first move; whoever holds the
prisoner holds the office's silence.

**Recommendation.** No lane chose. This lane recommends B: it gives arrest a political meaning and costs one
check where acts through a seat are formed.

**If you do not answer.** A, as built.

**Blocks.** Arrest and capture as political acts; coups.

**Sources.** `audits/07_SE_audit.md` §11 S-SE-2; `audits/07_SE_audit_addendum_B.md` §5 (last paragraph).

### D-25 · Must an officer be present to arrest? · FI, verbs
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A: an arrest needs no officer beside the prisoner (the court's reach suffices)


**The situation.** An officer may arrest anywhere his court's reach extends; the seat stands in for its
constables.

**The question.** Does an arrest need the officer beside the prisoner?

**Option A — no (as built).** A realm-wide police.
**Option B — yes.** Arrests happen only where the officer stands; a capital court reaches only the capital
unless its officers travel.

**Recommendation.** The physical verbs lane proceeds on A. This lane agrees.

**If you do not answer.** A.

**Blocks.** The arrest verb and warrant reach.

**Sources.** `audits/14_VERBS_PHYSICAL.md` §10.4 D-1.

---

## Group 7 · Your standing rule against your earlier rulings, and the social obstacle

**The common context.** Your standing rule of 2026-11-12, *"we do not do deterministic"*, says no
consequential outcome may be a fixed function of state: anything that could go either way is a graded draw.
The suite applied it as superseding earlier text everywhere (a fight's death, tending a wound, every
settlement verb, succession, inheritance). Three earlier rulings of yours fix an outcome by rule, and the
lanes would not overwrite them without asking. D-26 asks once for all three.

### D-26 · Does the standing rule override earlier rulings that fixed an outcome by rule? · CORE
**ANSWERED** (A-24): A: yes, everywhere


**The question.** Where an earlier ruling of yours makes an outcome a fixed rule (a crisis of faith that
"rolls nothing", a scruple as a threshold, swearing to a seat as the joiner's right), does "we do not do
deterministic" replace it with a draw?

**Option A — yes, everywhere.** D-27, D-28 and D-31 all take the draw.
**Option B — case by case.** Answer D-27, D-28 and D-31 separately.

**Recommendation.** A. This lane considers it already answered by the order of your rulings (the later,
emphatic, general rule) and by consistency: the suite applied it that way everywhere else, and keeping three
exceptions would itself be the inconsistency.

**If you do not answer.** The three are held; the rest of the suite proceeds.

**Blocks.** D-27, D-28, D-31.

**Sources.** `AUDIT_BRIEF.md` (standing rule); `audits/18_DETERMINISM_SWEEP.md` §1.

### D-27 · A crisis of faith: by rule or by draw · CHAR
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): B / B / A (a drawn and seen crisis of faith; a drawn scruple; swearing to a seat a draw against the seat)


**The situation.** By ED-IN-0261 the engine chooses who suffers a crisis of conviction "by a rule over state
… and rolls nothing". Everyone who sees the same deeds breaks alike, at the same count, into the creed the
rule names, and nobody knows it happened.

**The question.** Is a crisis of faith a rule, or a draw others can see?

**Option A — the rule stands.** Convictions are a slow, uniform tide set at world-build.
**Option B — drawn and seen.** A creed under strain is tried; firm believers usually hold and sometimes
break, weak ones the reverse; a breaking is an event its owner, and sometimes a witness, holds.
- *Feels like:* faith is something people lose in front of each other; a zealot who kept faith through a
  scandal is a character.

**Recommendation.** B (narrative churn lane, character pessimist). This lane agrees.

**If you do not answer.** A; only the selector and the event edits land.

**Blocks.** The crisis proposal's draw; narrative churn's conviction beats.

**Sources.** `audits/16_PESSIMIST_CHAR.md` §6 item 1; `audits/20_NARRATIVE_CHURN.md` §10 item 1;
`proposals/16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md`; `proposals/20_NARRATIVE_E_the_year_and_the_reason.md` edit 3.

### D-28 · A scruple: a line or a tendency · CHAR
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): B / B / A (a drawn and seen crisis of faith; a drawn scruple; swearing to a seat a draw against the seat)


**The situation.** ED-IN-0261 words a person's moral refusal as "a threshold for certain actions": a man's
line is exact and his refusals are predictable from his sheet.

**The question.** Is a scruple a fixed line or a drawn tendency?

**Option A — a line.** Knowable characters; a man crosses his line only if his pursuits move.
**Option B — a tendency.** The same man sometimes gives way; giving way is an event with witnesses. A game
of temptation.

**Recommendation.** B (character pessimist). This lane agrees.

**If you do not answer.** A (the draw's temperature stays zero).

**Blocks.** The scruple proposal's draw.

**Sources.** `audits/16_PESSIMIST_CHAR.md` §6 item 2; `proposals/16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md` (For Jordan).

### D-29 · Do favourable circumstances lower the obstacle or raise the speaker? · SC, DICE
**ANSWERED** (A-25): B: they raise the speaker; hostile ones raise the obstacle


**The situation.** Your clarification of 2026-11-12 (relayed, not yet in a ledger): *the social obstacle is
the task's difficulty plus all associated modifiers*. Your earlier rulings ED-884 and ED-934 say advantage
is never a cut to the obstacle; it raises the actor. The social proposal subtracts favourable items (proofs,
favour) from the obstacle; the social pessimist moves them to the speaker's side.

**The question.** Do evidence and favour make the task easier, or the speaker stronger?

**Option A — the task easier.** Floored at the minimum obstacle; at a small pool a room has only three
states.
**Option B — the speaker stronger.** Bounded by the soft cap; every proof counts at every pool.

**Recommendation.** B (social pessimist, by your earlier rulings). This lane agrees: "all modifiers" then
means the hostile ones in the obstacle and the favourable ones on the speaker, which honours both
statements. Please also confirm the clarification itself, so it can be recorded in a ledger.

**If you do not answer.** B.

**Blocks.** The one social obstacle composer.

**Sources.** `audits/16_PESSIMIST_SC.md` §5 item 1; `audits/05_SC_audit_addendum_B.md` §B8;
`proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`;
`proposals/16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage.md`.

### D-30 · What an equal opponent costs in argument · SC
**ANSWERED** (A-26): B: 0.4 per point (against the register's recommendation)


**The situation.** Ruled (2026-08-14): the opponent's obstacle is half his score. That makes a defence worth
more than an equal attack, increasingly with skill; the status quo holds.

**The question.** Keep half the score, or price an opponent at the dice's own average (0.4 per point) so
equals are even?

**Option A — keep (as ruled).** A world of entrenchment; moving anyone is uphill.
**Option B — 0.4 per point.** The better arguer usually wins; asymmetry comes from the room and the proofs.

**Recommendation.** A. The later lanes (the contest interrogation and the social addendum) treat it as ruled
and build around it; the proposal that would change it is held and superseded. This lane considers it
answered unless you want to reopen it.

**If you do not answer.** A.

**Blocks.** Nothing new.

**Sources.** `audits/05_SC_audit.md` §11 item 1; `audits/13_SC_contest_interrogation.md` (survivors: none);
`proposals/05_SC_opposed_obstacle_parity.md` (held, superseded).

---

## Group 8 · The oath, contract and tie verbs

**The common context.** Three questions on the social verbs that bind people: swearing service to a seat
(oblige), reading a contract's terms (construal), and the tie verb that today covers both personal bonds
and Thread knots.

### D-31 · Swearing to a seat: a draw, or the joiner's right · verbs, FA
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): B / B / A (a drawn and seen crisis of faith; a drawn scruple; swearing to a seat a draw against the seat)


**The situation.** By a ruled roster value, anyone may swear to any seat that admits him; only his later
service is uncertain.

**The question.** Does admission to a seat's service take a draw against the seat's holder?

**Option A — a draw.** The seat's holder (or its difficulty) is drawn against; a partial result is
probation. Service is something a seat grants.
**Option B — the joiner's right (as ruled).** Service is something a person takes.

**Recommendation.** A (social verbs lane, by the standing rule). This lane agrees; see D-26.

**If you do not answer.** Follows D-26.

**Blocks.** Oath and service; the formation proposal.

**Sources.** `audits/14_VERBS_SOCIAL2.md` §11.4 item 1; `proposals/14_VERBS_SOCIAL2_A_formation_on_what_is_known.md`.

### D-32 · What a man reading a contract tries to read into it · verbs, SC
**ANSWERED** (A-27): A: his own interest


**The situation.** A draw decides whether a reading of a contract's terms takes. What he *attempts* is
still a design choice.

**The question.** Is a construal a motivated reading, or random drift?

**Option A — his own interest.** He reads the terms toward his own held value; a court can test it against
the terms. Construal is argued.
**Option B — drift.** Each holder's copy of the terms drifts by a pursuit-weighted distortion. Construal is
noise.

**Recommendation.** A (social verbs lane). This lane agrees.

**If you do not answer.** A.

**Blocks.** Construal and contract disputes.

**Sources.** `audits/14_VERBS_SOCIAL2.md` §11.4 item 2.

### D-33 · Split the tie verb into tie and knot · verbs, WR
**ANSWERED** (A-28): A: split


**The situation.** One verb row covers a personal bond and a Thread knot.

**The question.** Split it in two (knot goes to the Thread lane), or keep one row with a kind?

**Option A — split.** No special operand; the verb count the requirement instrument reads goes from 67 to
68.
**Option B — one row with a kind operand.**

**Recommendation.** A (social verbs lane). Raised to you only because the verb roster is yours. This lane
agrees.

**If you do not answer.** A.

**Blocks.** The tie proposal; the Thread lane's knot.

**Sources.** `audits/14_VERBS_SOCIAL2.md` §11.4 item 3; `proposals/14_VERBS_SOCIAL2_D_tie.md`;
`proposals/08_FI_08_knots-season-form.md`.

---

## Group 9 · Battle balance: luck, numbers and organisation

### D-34 · Luck in battle: decides it, or tips it · MB, DICE
**OPEN** — held for the mass-battle history adjudication (`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`)


**The situation.** Each army's dice in a battle are multiplied by one hidden random factor drawn before
contact (the ruled "friction", spread 1.1, fitted to the historical win-rate curve). Measured: the result
is the draw 96 times in 100; a 2-to-1 army is upset about a quarter of the time, for reasons nothing a
commander did explains. Your 2026-11-12 intent is that composition and orders become legible causes of
victory.

**The question.** Should luck stay a hidden multiplier that largely settles a battle, or become one named
factor among ground, morale, fatigue and orders?

**Option A — keep the multiplier, owned and reported.** Its spread becomes a typed value and its draw is
written on the result ("fortune favoured the left").
- *Feels like:* battles are weather; a commander's art is choosing *when* to fight, never *how*.
- *Costs:* nothing to tune.
**Option B — luck as a named level.** Each side draws a signed amount of "fortune of the day" that enters
through the same capped channel as morale and fatigue, and is reported afterward.
- *Feels like:* a good plan usually beats a bad one, luck still overturns it, and the record says which.
- *Costs:* changes a calibrated ruling (ED-MB-0016's magnitude); the historical upset curve must be
  re-measured and may not be reachable.

**Recommendation.** B (mass-battle and dice pessimists: the architecture favours it); the first mass-battle
audit wrote its estimate proposal for A. This lane recommends B: it is the only option under which your
standing orders and composition (D-01, D-02) decide much.

**If you do not answer.** A, with the multiplier made a typed fact and reported.

**Blocks.** Battle balance; the battle report's account of why; the estimate's meaning.

**Sources.** `audits/04_MB_audit.md` §11 item 2; `audits/16_PESSIMIST_MB.md` §5 (survivor);
`audits/16_PESSIMIST_DICE.md` §6.

### D-35 · Do troop numbers stay in the melee dice? · MB
**OPEN** — held for the mass-battle history adjudication (`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`)


**The situation.** Your directive of 2026-07-08 says battle pools come "solely from the subunit troop type,
quality and numbers". The engine puts numbers in the melee dice with a steep exponent, so a bigger army
also hits harder per man in contact and size snowballs.

**The question.** Do numbers act through the dice, or through frontage, envelopment and endurance?

**Option A — numbers out of the dice.** Melee is linear: a bigger army wins by overlapping, enveloping and
outlasting. The smaller side can hold a line; depth, reserves and frontage become the decisions.
**Option B — numbers in the dice.** Concentration beats positioning; unequal battles end fast.

**Recommendation.** A (mass-battle lane, which found it already decided by a later ruling). This lane
agrees; it is listed because it narrows your directive's plain words.

**If you do not answer.** A.

**Blocks.** The melee law proposal and its partition-fairness test.

**Sources.** `audits/04_MB_audit.md` §11 item 1; `proposals/04_MB_cr12_linear_law.md`; `audits/16_PESSIMIST_MB.md` §5 rows 1, 8.

### D-36 · Three verbs for organising an army, or one · MB, verbs
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A: three organising verbs


**The situation.** The military verbs lane built form unit, assign troops and disband unit as three verbs,
each with its own draw (drill, obedience, the body's pride).

**The question.** Three verbs, or fold forming and disbanding into assigning troops?

**Option A — three.** Each survives the cut test by one outcome band.
**Option B — one.** A commander spends fewer scenes on his roll.

**Recommendation.** A (military verbs lane): the requirement asks for the rows built. This lane considers it
answerable without you.

**If you do not answer.** A.

**Blocks.** The order-of-battle verbs.

**Sources.** `audits/14_VERBS_MILITARY.md` §9 item 3; `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md`.

---

## Group 10 · The same seed, the same world (the port)

**The common context.** Whether "this seed is this world, on any machine" is a property of Valoria. Two
ratified texts disagree with each other and with the code: Layer 1 says the Godot shell is done when a
headless run prints the Python oracle's hash "in the integer domain", and names a seeded generator threaded
like the world; the adopted port plan says the first slice is not integer, and resolves parity by replaying
recorded draws; the Python oracle actually draws one value per named key and folds over a thousand floats a
season into its hash. Answer together.

### D-37 · Integer state, or declared floats · GO
**ANSWERED** (A-29): B: declared floats now


**The question.** Do the floating-point parts of the state become fixed-point integers, so a run is exactly
reproducible everywhere?

**Option A — integer state.** Replays and shareable seeds are safe on any machine. *Costs:* a design-first
rework and one re-pin, with marginal changes of choice.
**Option B — declared floats.** Layer 1's step 13 is amended to name the float contract. Nothing in the game
moves; a save is a state snapshot and a seed is not a shareable artefact across machines.

**Recommendation.** B now (the float lane). This lane agrees, with D-38 A, which keeps the door to A open.

**If you do not answer.** Neither text changes; the port gate stays ambiguous.

**Blocks.** The port gate's step 13; save format.

**Sources.** `audits/11_GO_audit.md` §11; `proposals/11_GO_float_contract.md`.

### D-38 · One random generator, or one draw per key · GO
**ANSWERED** (A-30): A: one draw per key


**The question.** Does the port draw each random value as a function of its key (as the oracle does), or
keep one threaded generator and test parity by replaying recorded draws?

**Option A — one draw per key.** No recorder; parity at any seed; the shipped game draws exactly as the
tested one did. *Costs:* one re-pin of every seeded result; a Layer 1 row rewritten; the port implements the
same hash function it already needs for ids.
**Option B — the plan as written.** No re-pin now; parity only on recorded slices; a seed played on the
oracle and on the port diverges at the first draw.

**Recommendation.** A (port pessimist). This lane agrees.

**If you do not answer.** B (the plan).

**Blocks.** The port's parity tests; the one-draw-owner proposal.

**Sources.** `audits/16_PESSIMIST_GO.md` §7; `proposals/16_PESSIMIST_GO_keyed_draw_no_recorder.md`;
`proposals/11_GO_one_draw_owner.md`.

---

## Group 11 · What a personal fight feels like

### D-39 · How long a fight lasts · PC
**ANSWERED** (A-31): B: longer


**The situation.** As coded, fights are fast and lethal: about three turns and three blows; the first solid
blow usually decides. Your 2026-11-12 intent (an approach per phase of a duel) presupposes a fight long
enough to change course.

**The question.** Fast and lethal, or long enough to have a position?

**Option A — fast and lethal.** The choice that matters is before the fight (the kit, whether to fight);
the per-phase approach becomes "per fight".
**Option B — longer.** Lower the damage scale so a success is one wound interval (as the engine's own
notes say it is): about 4.6 turns, a lead change in 44% of fights instead of 34%, undecided under 1%.
*Costs:* a recalibration; the obstacle is left alone.

**Recommendation.** No lane chose; the personal-combat pessimist sets out both. This lane recommends B: it is
what your duel intent assumes.

**If you do not answer.** A; the approach work is built after the commit-window proposal and after this
is ruled.

**Blocks.** The duel approach (steps 3a–3e); grid play; the combat calibration.

**Sources.** `audits/16_PESSIMIST_PC.md` §6.3 J-1, §6.1 R-6.

### D-40 · Fighting style: a lean only, or also a trade of attack for defence · PC
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A now; B behind a dial at zero, set after D-39


**The situation.** The proposed approach (aggressive, normal, defensive) leans on the engine's own draws:
commit depth, counter choice, breaking a bind. Measured, it is a small edge whose sign depends on the
weapon.

**The question.** Should an approach also shift weight between a fighter's attack and his defence?

**Option A — leans only.** Obeys the formations principle (an instruction modulates, adds no flat number);
real for a player who knows his weapon, nearly invisible otherwise.
**Option B — leans plus a conserved transfer.** Legible to anyone (it is the old pool split in the engine's
unit); fight length and the winner's wounds move with the two fighters' summed intensity. A term no
primitive produces.

**Recommendation.** The proposal builds A first and B behind a dial set to zero. This lane agrees; set the
dial after D-39.

**If you do not answer.** A, with B's dial at zero.

**Blocks.** The approach menu's last step.

**Sources.** `audits/03_PC_audit_addendum_B.md` §B10 item 4; `proposals/03_PC_duel_round_and_approach_B.md` §7 step 3c.

### D-41 · Does striking first give an edge? · PC
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): B (first-exchange edge on an unexpected opener)


**The situation.** An assault is a fair duel: who acts first is worth nothing (50.7% against 50.1%).

**The question.** Should the opener of a fight the other did not expect get an edge on the first exchange?

**Option A — no.** Violence is symmetric at personal scale; ambush belongs to the battlefield and to
fieldwork.
**Option B — yes.** A first-exchange edge (a level on the first exchange, or an exchange he cannot answer)
when the target did not expect it. *Costs:* a reader for "expected it" that nothing supplies today.

**Recommendation.** No lane chose. This lane recommends B if you take D-16 A (murder needs ambush to mean
anything), otherwise A.

**If you do not answer.** A.

**Blocks.** Ambush; murder's shape.

**Sources.** `audits/16_PESSIMIST_PC.md` §6.3 J-2.

---

## Group 12 · What people know, and how they come to be wrong

**The common context.** Characters are not omniscient (a requirement): everything a person knows is a
belief with a source and a confidence. These questions decide how fast news travels, whether the mechanics
themselves may create an error, and whether a person can be wrong about himself. D-42 and D-43 are two
halves of one question; D-44 and D-45 share one principle (does every error have an author in the world?).

### D-42 · Who learns of a change of office, and how fast · FI
**ANSWERED** (A-32): A: realm-wide shipped; B built as the test arm


**The situation.** Today every seat change is known everywhere at once. Your ledger already ruled that a
vacancy reaches a person as a belief through channels, and left open "offices as common knowledge" as a
channel's reach.

**The question.** When a seat changes hands, does the whole realm learn it, or only those present, those
whose seats cover it, and those told?

**Option A — realm-wide.** Politics is legible and fast; only what crosses a border is late.
**Option B — by presence, jurisdiction and telling.** A plot can run against a dead man for seasons; a king
can be the last to learn; a messenger matters.

**Recommendation.** A as the shipped setting, B as the tested alternative (fieldwork lane), because B cannot
be judged until tellings travel well. This lane agrees.

**If you do not answer.** A.

**Blocks.** One reach row for seat changes; the rumour work's load-bearing role.

**Sources.** `audits/08_FI_audit.md` §11 item 1; `proposals/08_FI_01_claim-sourced-referents.md`.

### D-43 · Does news of a death travel with news of the empty seat? · FI
**ANSWERED** (A-33): B: apart from the seat's news


**The situation.** Today the seat is known everywhere at once and the death nowhere.

**The question.** Should a death travel with the seat change, or separately?

**Option A — together.** The realm knows its King is dead the day he dies; the killer is the only unknown.
**Option B — apart.** The seat by its reach, the death only by presence, trail and telling. The realm knows
the throne is empty and argues for a season about why: pretenders, false reports of death, an investigation
that matters.

**Recommendation.** No lane chose. This lane recommends B: it is the detective and noir game you described,
and it does not have to match D-42.

**If you do not answer.** A for the seat (per D-42), and the death as today (nowhere).

**Blocks.** False reports of death; succession disputes; investigations of royal deaths.

**Sources.** `audits/16_PESSIMIST_FI.md` §5 S-PES-FI-2.

### D-44 · May a rumour name the wrong person? · FI
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A: a rumour may lose the doer, not replace him


**The situation.** A retold deed loses detail at a partial telling: quantities drift, the fact of the deed
does not, and the doer's name can be dropped ("someone killed him").

**The question.** May a garbled telling *replace* the doer with someone else the teller knows was there?

**Option A — loss only.** Nobody is wrongly named by accident; a false accusation needs a liar.
**Option B — substitution.** Innocents are named by the mechanics of retelling; feuds and wrongful
proceedings arise with nobody lying. Needs a rule for who may be substituted.

**Recommendation.** A (fieldwork pessimist, shipped as the default). This lane agrees, for the principle in
D-45.

**If you do not answer.** A.

**Blocks.** The rumour proposal's distortion table.

**Sources.** `audits/16_PESSIMIST_FI.md` §5 S-PES-FI-1; `proposals/16_PESSIMIST_FI_A_what_a_rumour_can_garble.md` (For Jordan).

### D-45 · May an honest investigator reach a wrong conclusion? · FI, verbs
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A: no engine-authored wrong conclusions


**The situation.** A failed reconstruction of a deed produces nothing; a wrong conclusion arises only from
wrong evidence (a lie, a forgery, a drifted report).

**The question.** May a failed draw produce a plausible but wrong conclusion that names someone his own
beliefs place at the scene?

**Option A — no.** Every error in the world has an author.
**Option B — yes.** The investigator misreads true evidence; this is the archived design's intent and gives
NPC-004 its case from honest evidence. The engine becomes the author of an error, which no other verb is.

**Recommendation.** A (material verbs lane, shipped). This lane agrees: A and D-44 A make one rule (only
people cause errors), and wrong conclusions remain plentiful through lies and forgeries.

**If you do not answer.** A.

**Blocks.** The reconstruct verb's failure band; NPC-004's honest-evidence case.

**Sources.** `audits/14_VERBS_MATERIAL.md` §19 J-M2.

### D-46 · Does a man learn from failing to find someone? · verbs
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): B: his refusal teaches him, privately


**The situation.** If a man seeks someone who is not there, his act is refused and he learns nothing, so
he may repeat it.

**The question.** Should his own refusal teach him, and only him, that the person was not there?

**Option A — no (today).** Belief changes only with new sightings.
**Option B — yes, privately.** He records that the person was absent at that place and time; witnesses
learn nothing. He stops seeking someone where he already failed to find him.

**Recommendation.** No lane chose. This lane recommends B: it removes a dead end at the cost of one firsthand
belief.

**If you do not answer.** A.

**Blocks.** Repeated failed acts; the social verbs' formation proposal.

**Sources.** `audits/14_VERBS_SOCIAL1.md` §15 D2.

### D-47 · Can a person be wrong about himself? · CHAR
**ANSWERED** (A-34): B: a belief, built narrowly


**The situation.** A person's own state is known to him by construction. NPC-004's core need is a man with a
perceptual gift he does not know he has and misattributes; NPC-012 has a motive he does not recognise; a
design passage writes a man unaware of his effect on others.

**The question.** Is self-knowledge a belief like any other, that can be missing or false?

**Option A — own state is known (today).** Simple and built; drama is between people.
**Option B — self-knowledge is a belief.** A person can lack it, hold a false one, and be told. Makes
NPC-004, NPC-012 and NPC-021 playable as written; costs a second answer on every own-state read and a rule
for how a person learns what he is.

**Recommendation.** No lane chose. This lane recommends B, built narrowly: first for gifts and motives the
provided cases name, not for every own-state read.

**If you do not answer.** A.

**Blocks.** Three provided cases; "a voice that was wrong about oneself".

**Sources.** `audits/02_CHAR_audit.md` §11; `audits/02_CHAR_audit_addendum_B.md` §B6.3.

### D-48 · Forgetting: computed, or recorded each season · CORE
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A: forgetting computed when read


**The situation.** A belief's confidence fades with time.

**The question.** Is fading computed when read, or written to the record each season?

**Option A — computed.** The record holds what people did, learned and lost; long campaigns stay affordable.
A chronicle cannot cite the season a belief weakened.
**Option B — recorded.** One "faded" event per person per season; a story could say "by the third winter he
had lost the thread".

**Recommendation.** A (core lane, by precedent: a crossing is recorded, a level is not). Nothing asks for B.
This lane considers it answerable without you.

**If you do not answer.** A.

**Blocks.** The claim store.

**Sources.** `audits/01_CORE_audit.md` §11; `proposals/01_CORE_claim_fade_as_read.md`.

### D-49 · May a campaign's end reveal what the person never knew? · GO
**ANSWERED** (A-49): B: reveal after the line ends, on top of never-reveal in play


**The situation.** In play, the player sees only what his person believes (ruled). The end of a campaign is
not covered. The archived ending design asks for "the world they leave" and a counterfactual footprint; the
oracle already renders the true causal chain for developers.

**The question.** After a line ends, may the player see the truth?

**Option A — never.** The portrait is what he believed, false beliefs included; mystery is permanent and a
second campaign can still be surprised.
**Option B — at the end.** After the line ends (and only if no continuation is taken), the player learns
which beliefs were false and whose hand was behind an unattributed fall: the detective genre's closing
reveal.

**Recommendation.** The port lane builds A now because it needs nothing; B is one reading at one moment and
can be added without touching A. This lane recommends B, as an add-on after A.

**If you do not answer.** A.

**Blocks.** The ending screen only.

**Sources.** `audits/11_GO_audit_addendum_B.md` §B6.3; `proposals/11_GO_fidelity_and_campaign_modes.md` §4.

---

## Group 13 · The Church, caste and franchise

**The common context.** Seven Church and Löwenritter seats were ruled unremovable (`revocation: null`,
2026-10-11) because no same-faction seat stands above them. The Church therefore has no internal check.
The caste against the southern Einhir is "informal" in canon. D-50 and D-51 are a pair (who checks the
Church, inside and out).

### D-50 · May the Church's head strip a Church officer? · institutions, FA
**ANSWERED** (A-35): B: yes, by a resistible draw


**The situation.** Cardinals leave only by death or resignation. NPC-038 (the Cardinal of Justice removed on
exposure), NPC-004 and NPC-070 need those seats removable.

**The question.** May the holder of a faction's head seat remove an officer of that faction?

**Option A — keep null.** The Church is a set of barons for life; those arcs end by violence or not at all.
**Option B — the head of the faction may revoke**, by a draw the officer can resist. The Confessor
disciplines Cardinals; the Church has internal politics, purges and the fear of them. A general rule over
existing data; the Löwenritter stay unstrippable until they have a head seat.

**Recommendation.** B (governance lane, papacy lane, synthesis). This lane agrees. It overwrites the
2026-10-11 ruling.

**If you do not answer.** A; the proposal's item 4 stays held.

**Blocks.** NPC-038, NPC-004, NPC-070; the papacy kit's discipline.

**Sources.** `audits/06_FA_audit.md` §11 item 3; `audits/15_INSTITUTIONS_PAPACY.md` §13 item 1;
`audits/15_INSTITUTIONS_SYNTHESIS.md` §10 item 2; `proposals/15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md` item 4.

### D-51 · Can anyone judge the Confessor? · institutions
**ANSWERED** (A-36): A: nobody (against the recommendation)


**The situation.** The head of the Church leaves only by death or resignation. The throne, by contrast, can
be stripped by a motion with the Holy See's concurrence.

**The question.** Is there a lawful way to remove the Confessor?

**Option A — nobody.** A bad Confessor is answered by schism or violence; the Church is the one institution
with no check, which is what makes Himlensendt "the most dangerous person on the peninsula".
**Option B — a council with the Crown's concurrence**, mirroring the throne's rule. Crown and Church each
check the other; the archived Confrontation arc gets a lawful route.

**Recommendation.** No lane chose. This lane recommends B, for the symmetry with the throne; A is a strong
choice if you want Himlensendt untouchable.

**If you do not answer.** A; the council is design-first and waits.

**Blocks.** The papacy kit's council (item 5); the Confrontation arc.

**Sources.** `audits/15_INSTITUTIONS_PAPACY.md` §13 item 2; `audits/15_INSTITUTIONS_SYNTHESIS.md` §10 item 3;
`proposals/15_INSTITUTIONS_PAPACY_E_sees_tithe_orders_legates_council.md` item 5.

### D-52 · Forced labour keyed on caste · canon, institutions
**ANSWERED** (A-41): Neither offered option. Jordan: "express caste not only in regard, but also vote blocks and informally tiered rights/privileges/wealth"


**The situation.** The historical colonial family includes labour drafts on a subject people; Valoria's
subject people (the southern Einhir) is canon, and their caste is informal, acting only through regard.

**The question.** Is there an instrument by which southern labour can be drafted?

**Option A — a corvée form.** A cohort's seasons of work owed to a grantee's site, issuable over southern
ground. The caste becomes an institution with seats and an audit, and its abolition a fight over an
instrument.
**Option B — no instrument.** The caste stays informal, acting only through regard; nobody can grant or
abolish it.

**Recommendation.** None; the lanes call it a decision about the tone of canon. This lane offers no
recommendation.

**If you do not answer.** B.

**Blocks.** The colonial kit's corvée; any abolition arc.

**Sources.** `audits/15_INSTITUTIONS_COLONIAL.md` §11 item 3; `audits/15_INSTITUTIONS_SYNTHESIS.md` §10 item 4.

### D-53 · Franchise: a territory's political weight · FA, canon
**ANSWERED** (A-42): Taken as B (author it) from A-41's 'vote blocks' (his own words, ladder step 1); confirm when convenient


**The situation.** An archived draft (never ruled) gives each territory a political weight, lowered for the
southern Einhir and movable by good rule and caste reform: the only place the design gives caste a
strategic expression. Nothing votes yet.

**The question.** Leave it archived until something votes, or author it now?

**Option A — leave it archived.** **Option B — author it now** so faction weight reads where a member sits.

**Recommendation.** A (governance addendum default). This lane agrees.

**If you do not answer.** A.

**Blocks.** Nothing now.

**Sources.** `audits/06_FA_audit_addendum_B.md` §B6.2 item 2.

---

## Group 14 · Courts and verdicts

### D-54 · May a convict walk away from a sentence of service? · SC
**ANSWERED** (A-37): B: no


**The situation.** As ruled, a sentence of service is a penance the convict may discharge himself: one free
release, the same season. Detention and banishment are not self-releasable.

**The question.** May a convicted man end his own sentence of service?

**Option A — yes (as ruled).** Trials bind only by custody or ban.
**Option B — no.** An imposed service is ended by the bench's pardon or its term, as its two siblings are.

**Recommendation.** No lane chose. This lane recommends B: a sentence the convict can walk away from the same
season is not a sentence.

**If you do not answer.** A.

**Blocks.** Sentencing outcomes.

**Sources.** `audits/16_PESSIMIST_SC.md` §5 For Jordan item 2.

### D-55 · Who a verdict is for · SC
**ANSWERED** (A-38): B: the petitioner (or a seat he names)


**The situation.** A verdict creates an obligation from the convicted party to the judge's seat. The
petitioner who brought the case gets nothing.

**The question.** Where a case came from a petition, is the verdict owed to the petitioner?

**Option A — the court (as ruled).** The petitioner's satisfaction is not modelled.
**Option B — the petitioner** (or a seat he names). Winning a case becomes something a person can want.

**Recommendation.** No lane chose. This lane recommends B: it is what makes courts a tool for characters.

**If you do not answer.** A.

**Blocks.** Courts as goals; the verdict-names-its-party proposal.

**Sources.** `audits/16_PESSIMIST_SC.md` §5 For Jordan item 3; `proposals/16_PESSIMIST_SC_C_a_verdict_names_its_party.md`.

### D-56 · Appeal: as of right, or on new grounds · SC, FI
**ANSWERED** (A-39): B: on new grounds only


**The situation.** An appeal row exists with a placeholder ("appeal to a higher authority").

**The question.** Is a reversal a second draw on the same case, or only on new grounds?

**Option A — appeal as of right.** Any decided case may be appealed once per level, re-weighing the same
file. A game of forum and patronage: who can reach a higher bench decides more than the evidence.
**Option B — appeal on grounds.** Admitted only with excluded evidence, a voided stage, or a new item from a
distinct source. A game of evidence after the verdict that sends play back to the field.

**Recommendation.** No lane chose. This lane recommends B: it ties the court to the detective game.

**If you do not answer.** The proposal's shape works for either; its gate waits.

**Blocks.** The verdict ladder and reversal proposal.

**Sources.** `audits/19_LACUNA_investigation_to_proceedings.md` §11 S-19-1;
`proposals/19_LACUNA_verdict_ladder_and_reversal.md`.

---

## Group 15 · The world's story: the Thread, strife, arcs and world generation

**The common context.** Forty-nine of the 143 provided cases turn on the Thread; the code has no carrier for
the world's own condition. The realm's strife is read as strands of linked moves; generation decides how
many people exist and how much the seed changes. D-57 must come before D-58 and before the generation
question on Thread content; D-63 to D-67 are world generation's five and are best answered together.

### D-57 · Does the world itself wear down (the Thread)? · WR, canon
**ANSWERED** (A-40): A: ground, a real condition of places


**The situation.** Twenty-five cases depend on a world quantity (the Thread wearing), twenty-six on how
persons perceive it. Nothing in code carries the world side.

**The question.** Is the Thread's decay a real condition of places, or only a matter of perception and belief?

**Option A — ground.** One site per territory whose condition wears with the season, is damaged by three
verbs' failures and repaired by one, and whose state sets those verbs' floors. No new kind of entity. The
world can run down; survival and sovereignty compete for the same scenes.
**Option B — not built.** The world is misunderstood, not dying; the twenty-five cases are recorded as
outside the game.

**Recommendation.** A (arcs lane, taken as the working answer for sequencing only). This lane agrees.

**If you do not answer.** A for sequencing; no Thread content is generated.

**Blocks.** Twenty-five Thread cases; Thread-bearing generation (the generation lane recommends waiting on
this); the threadwork module.

**Sources.** `audits/12_ARCS_adjudication.md` §11 S-1; `proposals/12_ARCS_substrate_as_ground.md`;
`audits/21_PROCEDURAL_GENERATION.md` §11 D-4; `proposals/09_WR_threadwork_module.md`.

### D-58 · What happens to a practitioner at zero coherence · WR, canon
**ANSWERED** (A-43): Neither offered option. Jordan: "zero coherence means that the person is no longer able to be understood within the bounds of human rationality. they may still hold…


**The situation.** The last adopted design says a practitioner at zero returns to the common mass (loss of
self). ARC-28, ARC-29 and ARC-30 retract that in favour of expansion: full continuity, with a lossy way of
speaking. Code follows neither.

**The question.** Is the end of a practitioner's road loss of self, or transformation?

**Option A — loss.** The career ends in de-individuation; three arcs become other stories.
**Option B — expansion.** The person keeps his seat and goals, and what he can tell to whom changes; needs a
per-listener telling the engine does not have.

**Recommendation.** None; canon. This lane notes that B costs a new mechanism and A costs three arcs.

**If you do not answer.** Neither is built.

**Blocks.** ARC-28 to ARC-30.

**Sources.** `audits/12_ARCS_adjudication.md` §11 S-2; `proposals/12_ARCS_substrate_as_ground.md` (second
decision).

### D-59 · One river of strife, or several stories · WR
**ANSWERED** (A-45): B: several strands that can each end


**The situation.** By the ratified strife rule, any two deeds of one doer link into one strand. At six
seasons one strand holds all 234 moves and 55 doers.

**The question.** Should the realm's strife be one continuous "troubles", or several named stories that can
each end?

**Option A — keep.** One river, legible as mood, with no sub-plots.
**Option B — bound the link.** A doer's later deed joins a strand he opened, or joins by its subject: several
strands beneath the era, each able to conclude.

**Recommendation.** The world lane could not choose between two sentences of one ruling. This lane recommends
B: the ruling's own second half asks for "narrative chains within it at lower levels".

**If you do not answer.** A.

**Blocks.** The chronicle; strand conclusion.

**Sources.** `audits/09_WR_audit.md` §11 item 1; `proposals/09_WR_strand_conclusion.md` edit 3.

### D-60 · Is leaving a side a move in the realm's strife? · WR
**ANSWERED** (A-46): B, narrow: only leaving a faction's creed or head seat


**The situation.** The ratified strife roster lists ending a commitment as "never" a strife move. So a
rising cannot be read as having split a faction.

**The question.** Should leaving a side count?

**Option A — never (as ratified).** Defection is everyday life.
**Option B — joins.** A defection attaches to its strand and can conclude nothing; the Split becomes a move
of the era. Risk: every routine release joins strands; the narrow form (only leaving a faction's creed or
head seat) needs its own wording.

**Recommendation.** B in its narrow form (narrative lane). This lane agrees.

**If you do not answer.** A; the edit is held.

**Blocks.** The Split; the narrative "his own side" proposal.

**Sources.** `audits/20_NARRATIVE_CHURN.md` §10 item 2; `proposals/20_NARRATIVE_D_his_own_side.md` edit 4.

### D-61 · Arcs that end when a counter fires · WR, CORE
**ANSWERED** (A-47): B: a threshold may open a mandatory scene, never decide it (against the recommendation)


**The situation.** Eight of the fifty provided arcs close when a counter crosses a threshold, and nineteen
are forced by one. The standing rule and the engine's own law forbid a crossing that decides an outcome.

**The question.** May a threshold force a moment?

**Option A — a threshold raises a question** that a person answers by a drawn act; the arcs are restated.
**Option B — a threshold may open a mandatory scene,** never decide it. The world can corner a character.

**Recommendation.** No lane chose. This lane recommends A: it is the engine's present law and your standing
rule; B is a reasonable later addition.

**If you do not answer.** A (the engine's law); the arcs stay unrestated.

**Blocks.** The endings of the eight threshold-closed arcs and the nineteen threshold-forced ones.

**Sources.** `audits/16_PESSIMIST_GAME.md` §7.3 J-3.

### D-62 · One question at a time, or a list to choose from · GO, CHAR
**ANSWERED** (A-48): B: a list of questions for the player; NPCs take the first


**The situation.** A person is offered one question per scene, the engine's pick, for player and NPC
alike. Your ruling ED-SC-0013 says "choosing what to attend is the gameplay".

**The question.** Should the player see the sorted list of questions and choose?

**Option A — one question.** A game of answering what arrives.
**Option B — a list for the player,** the first item to NPCs. A game of triage; player and NPC are no longer
served identically.

**Recommendation.** No lane chose. This lane recommends B, by your ruling.

**If you do not answer.** A.

**Blocks.** The scene slate; the player surface.

**Sources.** `audits/09_WR_audit.md` §11 item 3; `proposals/11_GO_player_surface_contract_B.md` §1.

### D-63 · The cast: 46, or 46 plus a generated supporting cast · WR, canon
**ANSWERED** (A-44): B: about 94 generated persons plus kin, capped


**The situation.** The cast is a closed authored 46 (ED-WR-0011: "for now … we will return much later").

**The question.** Should the game generate a capped supporting cast?

**Option A — 46 only.** A small, fully authored drama; every culprit is a principal; kin and rivals must be
authored or absent.
**Option B — about 94 generated persons plus kin, capped.** A village has a reeve and a debtor; doubles a
season's cost; the player cannot know every face.

**Recommendation.** B with the cap as the dial (generation lane). This lane agrees.

**If you do not answer.** A; the cast-and-seats proposal is held.

**Blocks.** Cases, succession and local seats needing people; the cast proposal.

**Sources.** `audits/21_PROCEDURAL_GENERATION.md` §11 D-1; `proposals/21_PROCEDURAL_B_cast_and_seats.md`.

### D-64 · Does the seed change the starting realm? · WR
**ANSWERED** (A-50): B: some starting state drawn, small and bounded


**The situation.** Every seed builds the same persons, seats and attitudes; the seed moves only chance.

**The question.** Should the seed also draw some starting state (who holds a grudge, which granary is low,
who is ill)?

**Option A — no.** Valoria is authored; replay variety must come from play (today it does not).
**Option B — yes.** Variety from the first season.

**Recommendation.** No lane chose. This lane recommends B, small and bounded, since replay variety does not
come from play today.

**If you do not answer.** A.

**Blocks.** Replay variety; world cards.

**Sources.** `audits/16_PESSIMIST_GAME.md` §7.3 J-4; `proposals/21_PROCEDURAL_D_world_cards_and_churn.md`.

### D-65 · How deep the past goes · WR
**ANSWERED** (A-51): Neither offered option. Jordan: "five years"


**The question.** One simulated year before play (everything older as tradition and hearsay), or a
generational pass (births, ageing, deaths, successions)?

**Option A — one year.** Cheap; contestable pedigrees. **Option B — generations.** Legends; needs ageing and
birth built and a second cadence.

**Recommendation.** A now (generation lane). This lane agrees.

**If you do not answer.** A.

**Blocks.** The prologue.

**Sources.** `audits/21_PROCEDURAL_GENERATION.md` §11 D-2; `proposals/21_PROCEDURAL_C_prologue_and_case_seeds.md`.

### D-66 · New business in a long game · WR, FA
**ANSWERED** (A-52): B: a docket read inside convening, after a test shows cards-at-build runs dry


**The situation.** World cards are read at build only (plan text). After they are spent, new business comes
from storms, arrivals and succession; a long game may run dry.

**The question.** May a seat-holder's convening draw new business from a docket in play?

**Option A — cards at build only.** **Option B — a docket read inside convening,** with repeats suppressed;
institutions keep producing business. Amends two plan lines.

**Recommendation.** B, after a test shows A runs dry (generation lane). This lane agrees.

**If you do not answer.** A; the docket section is held.

**Blocks.** Late-game churn.

**Sources.** `audits/21_PROCEDURAL_GENERATION.md` §11 D-3; `proposals/21_PROCEDURAL_D_world_cards_and_churn.md` §5.

### D-67 · What happens to a world that fails its checks · WR, GO
**ANSWERED** (A-53): A: next seed by default; play-it behind a setting


**The question.** If a generated world fails its quality bars after the retries, does the player get the
next seed, or play it with a sheet saying what it lacks?

**Option A — next seed** (a curated game). **Option B — play it** (quiet worlds admitted).

**Recommendation.** A by default, B behind a setting (generation lane). This lane agrees.

**If you do not answer.** A.

**Blocks.** World generation's acceptance step.

**Sources.** `audits/21_PROCEDURAL_GENERATION.md` §11 D-5.

---

## Group 16 · Land and people

### D-68 · Is farm work an act someone chooses? · SE
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): B: farm work an act, sequenced after the cohorts' heavy moves land


**The situation.** A site's yield reads the hands present at the place; "work" is a construction verb. A
people feeds itself without choosing to.

**The question.** Is production labour presence, or an act that puts hands on a producing site?

**Option A — presence (built).** Sturdy with a weak chooser; allocation is not play; a steward's levers are
stock and buildings.
**Option B — an act.** A cohort that riots, flees or mends walls is not working the harbour, and yield falls
for a reason with an author. Puts the realm's food on the chooser; the colony-sim precedents converge on it.

**Recommendation.** The material verbs lane built A. This lane recommends B, but only after D-73 (cohorts
with a few heavy moves), since "work" is one of those moves.

**If you do not answer.** A.

**Blocks.** Yield; the steward's game; work versus restore.

**Sources.** `audits/14_VERBS_MATERIAL.md` §19 J-M1.

### D-69 · Does a lasting famine keep speaking? · SE
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A: famine reports once, never-stocked edge repaired


**The situation.** By a ruling (2026-10-12), a place reports its fall into dearth once and is then silent.
In one test, eleven towns starved and nobody learned of it, because they were never stocked and so never
"fell".

**The question.** Reported once, or every season it lasts?

**Option A — once, with the edge repaired.** A never-stocked place reports at its first short season;
then silence; famine depends on memory and rumour.
**Option B — every season.** Famines stay in view; belief volume rises.

**Recommendation.** A (settlements pessimist; consistent with the ruling). This lane agrees.

**If you do not answer.** Neither; only the missed exact-drain report is repaired.

**Blocks.** Famine as news.

**Sources.** `audits/16_PESSIMIST_SE.md` §6.2 J-1.

### D-70 · How the world's own motion draws · SE, WR
**ANSWERED** (A-54): B: the one four-band ladder


**The question.** Do weather, harvest and wear draw from simple multiplier tables, or on the one four-band
ladder (a place's endurance as the pool, the season's hardship as the obstacle, so a harvest is
"overwhelming" or "a failure" and a steward's skill can bear on it)?

**Option A — tables.** Three numbers; consistent with the weather draw. **Option B — the ladder.** The
settlement layer joins the one resolution system; costs a pool and an obstacle per clock.

**Recommendation.** No lane chose; the standing rule's wording ("a graded, recoverable result (the
four-band ladder)") reads toward B. This lane recommends B.

**If you do not answer.** A (the world-draws proposal).

**Blocks.** Weather, hunger, wear; the world-draws proposal.

**Sources.** `audits/16_PESSIMIST_SE.md` §6.2 J-2; `proposals/16_PESSIMIST_GAME_the_world_draws.md`.

### D-71 · May a town be founded or die? · SE
**ANSWERED** (A-55): A: fixed map; an empty founded household may lapse


**The situation.** A settlement-map ruling holds "never adding nodes": founding makes households and
communities inside the 37 settlements, and nothing ends one.

**The question.** Is the map fixed, or can towns be founded and abandoned?

**Option A — fixed.** 37 settlements forever; a founded household that stands empty is put to a draw each
season and may lapse. The court game on a fixed board.
**Option B — grows and shrinks.** Settlements can be built and abandoned at zero population. The colony game.

**Recommendation.** No lane chose. This lane recommends A, which keeps the ruling and gives founding a
second outcome.

**If you do not answer.** A without the lapse.

**Blocks.** Founding.

**Sources.** `audits/16_PESSIMIST_SE.md` §6.2 J-3.

### D-72 · A lord over an empty land · SE, FA
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): A: leave a lord over an empty land


**The situation.** With every commoner of a place dead, the persons seated over it are untouched.

**The question.** Does a seat with no living people beneath it lose its powers?

**Option A — leave it.** Depopulation is felt through yield, levy and stability. Famine is an economic
story.
**Option B — loses its remit until people return.** A blight can unseat a duke; famine is political.

**Recommendation.** No lane chose. This lane recommends A until yield, levy and stability bind.

**If you do not answer.** A.

**Blocks.** Little.

**Sources.** `audits/16_PESSIMIST_GAME.md` §7.3 J-1.

### D-73 · The common people: full actors or a few heavy moves · CHAR, SE
**ANSWERED** (A-56): B: a few heavy moves (petition, migrate, work, tend, comply or refuse, riot)


**The situation.** The 37 commoner groups are persons offered the whole verb table: they make 43% of all
acts (including 34 forgeries to the named persons' 18) and almost nobody answers them. Removing their
deliberation entirely changes 5 of 798 named persons' acts and no seat, site or person.

**The question.** Should a population have the full verb table, or a short list (petition, migrate, work,
tend, comply or refuse, riot)?

**Option A — full.** The realm's log is mostly the populace's paperwork.
**Option B — a few heavy moves.** The named persons act against a populace that moves in a few heavy ways.
Costs the present game nothing it can show.

**Recommendation.** No lane chose. This lane recommends B.

**If you do not answer.** A.

**Blocks.** Cohort deliberation; D-68.

**Sources.** `audits/16_PESSIMIST_GAME.md` §7.3 J-2.

---

## Layer 1 housekeeping

### D-74 · The witness step reads more than Layer 1 lists · CORE, FI
**CLOSED BY THE FIVE-STEP LADDER, not by Jordan; reversible on his word** (ladder table): B: fix the witness code, not Layer 1


**The situation.** Layer 1 lists four things the witness step may read; the code reads nine, five declared
as exceptions in the file.

**The question.** Amend Layer 1 to list them, or bring the code back to the list?

**Option A — amend the row** to name all of them.
**Option B — restore the row:** move the refraction and credit arithmetic behind a per-holder projection
built at the barrier, so the step imports nothing from the decision layer; amend only for the two reads no
refactor removes.

*The game is identical either way.*

**Recommendation.** B (fieldwork lane, by "a spec edited to match its implementation checks nothing"). This
lane considers it answered by that rule; listed because the row is ratified.

**If you do not answer.** B.

**Blocks.** One Layer 1 row; the fieldwork small-edits proposal §6.

**Sources.** `audits/08_FI_audit.md` §11 item 2; `proposals/08_FI_04_small-edits.md` §6;
`architecture/meta/04_CODE_ARCHITECTURE.md` §A.2 (`loop/witness` row).
