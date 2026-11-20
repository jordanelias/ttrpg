# Part 1, appendix — the six-step derivation chain for every row

## Status: PROPOSED. Reference only. One entry per row of `01_mapping_table.md`, in the brief's six steps: (1) the problem the tradition says the concept solves, in its own words; (2) the mechanism it claims, apart from the poetry of the name; (3) where that situation arises in the engine; (4) the engine quantity that plays the role, the two nearest where there are two, the observation that would separate them, and whether it was run; (5) whether the engine already provides it without a technique; (6) the cost, from the tradition's own account. Quotations and tags are the research sheets'; `file:line` is this branch's tree.

## Japan

**JP-01 the stopping mind; *fudōchi*.** (1) "the moment your attention is drawn to the slashing blade … your mind becomes attached there … so that you lose your free functioning and can be slain" [HASKEL p.33]. (2) Attention captured by the last event and carried into the next leaves no capacity for the next; immovable wisdom is attention that leaves each attacker behind ("responds ten different times"). (3) In the engine the fighter's capacity to keep responding well across exchanges is the Concentration reserve: drained by a blow taken (`wrapper.py:411` and the pursuit, stop-hit and bind sites) and by a lost riposte (`:445`), read into the response (`mode_sigma`'s LAPSE term, `combat_systems.py:340`), the read (`mental_fatigue`, `:1285-1289`, into `:1004`) and the defence (`:961`). (4) Concentration. Nearest two: Concentration against the read levers (`visual`, `precommit`). Separating observation: a read lever lifts the read before and after a blow alike; a Concentration effect shows as the gap between them. **Run** (Part 7 §7.3): the gap is −0.2 points in the control and the drains switched off do not close anything measurable; the chain table shows why — `mental_fatigue` multiplies the stamina fatigue, so a fresh fighter's read never depends on his reserve. The quantity is the right one and nearly inert. (5) Yes, as attributes (Focus, Spirit) and as the PC-22 growth of Concentration; no school owns it. (6) The tradition names no in-fight price, only years ("ten or twenty years … thirty years more", A19-A20); a drain-reducing technique would therefore be a monotone stat.

**JP-02 *mushin*; the ordinary mind.** (1) "arms, legs, and body know of themselves, and the mind becomes completely unnecessary" (A5); the fault is deliberation: "Once a thought is present in the mind, discriminations and calculations arise" (A7). (2) A right response without perceiving and choosing. (3) The engine's one place where a defender responds without a read is the lost-read branch: a uniform draw over parry, dodge and wind (`combat_systems.py:1016`). (4) A probability, on a lost read only, of taking the best mode instead. Nearest two: this against the agency proposal's guard prior (a fixed favoured mode). Separating observation: a guard prior's gain falls when the opponent's attacks change type (it is a habit); a best-mode probability's does not. Takuan names the habit as the fault ("not attached to a particular stance", A5), so the guard prior is the wrong reading. UBR. (5) No. (6) "cannot be forced" (A6); none in the fight.

**JP-03 water and ice.** (1) "Deluded mind is like ice in that you can't use ice to wash your hands and face" (A8). (2) The stuck mind; the cure is unsticking it. (3), (4), (5) as JP-01: the failure Takuan names is the same captured attention. Rejected: "water" → the `tactile` lever or a yielding mechanic; Takuan's water is the free mind, not contact. (6) As JP-01.

**JP-04 no hair's breadth.** (1) "When your mind attaches to an attacker's sword, an interval appears. And in that interval you lose your freedom to respond" (A9). (2) The answer is made in the same moment as the attack, so that "your opponent's weapon will become your weapon"; "It's an error to understand this solely as a matter of speed." (3) The engine's answer in the attack's own tempo is the single-time counter: reached for behind `if read_win and commit>=cfg['DEEP_COMMIT']` (`wrapper.py:325-329`), landed by `counter_success_prob` (`combat_systems.py:1296-1301`), voiding the attack (`wrapper.py:361-362`). (4) `counter_select` and `counter_success`. Nearest two: the counter levers against Agility (`reflex`, which feeds the counter's success, `:1300`). Takuan excludes speed, so reflex is rejected by the source, not by a run. (5) The counter is built; the levers are live. But the run (Part 7 §7.1) finds the door nearly shut: in a closed exchange the swing room caps the commit near 4.03-4.09 (`:403-411`, `:993-994`), so about 1% of commits (0.1-1.2% in Part 7 §7.1's cells) reach `DEEP_COMMIT`. (6) Takuan: willed speed "captures the mind"; the engine's price, a missed counter eating the attack undefended (`wrapper.py:363-369`), is the tradition's "interval" made concrete.

**JP-05 *ken-tai*.** (1) "if the mind is in Attack, it will run to excess"; "you obtain the victory by having your opponent make the first move" (B6). (2) Hold one's own commitment back while pressing in, so that the opponent cannot bear it and commits first. (3) Two situations: one's own commitment (`commit_depth`, `combat_systems.py:980-995`) and the opponent's (the same function, called for him). (4) Abiding: temperament, which skews one's own commit and raises one's counter reach (`:989-994`, `:1029`). Enticing: nothing — the opponent's commit reads his own lean and his wariness of an unfamiliar tradition, never the other man's pressure. Nearest two for abiding: temperament against the `counter_select` lever; separated in Part 7 §7.1 (only temperament moves one's own commits). (5) Abiding, yes (temperament is a host input, B18.02's `temper`). (6) Munenori: one who does not expect the attack "will be set upon quickly and severely"; the engine's cautious pole cedes the Vor every beat (`wrapper.py:165`). The run finds this price paid and the payoff absent (CP-06).

**JP-06 *hyōshi*, *muhyōshi*.** (1) A fixed rhythm lets the opponent "use his sword well" (B8). (2) Break the opponent's rhythm so that he falls behind ("If the rhythm is upset, he will not even be able to jump over a ditch"). (3) Who acts when is the readiness race: cadence times anticipation (`wrapper.py:180`; `tempo_pressure`, `combat_systems.py:1173-1198`). (4) The `tempo` factor in `tempo_pressure`'s READ_TEMPO_K term: one's own factor raises one's readiness and enters the opponent's with a minus sign. Nearest two: this against the Vor (`initiative`, the other term of the same function). Separating observation: the Vor is earned and decays; the `tempo` term is standing. **Run** (Part 7 §7.4): at level 3 one's own pressure is 1.356 and the opponent's 0.644 — the opponent is literally put behind. Rejected: "rhythm" → weapon cadence (`weapon_tempo`), which is physics, not a fighter's choice. (5) Yes (the `timing_*` generics). (6) The tradition prices only the lack of it; the lever has no cost anywhere it is read.

**JP-07 hold down the pillow.** (1) "it is bad to be led about by the enemy" (C4). (2) Stop his action at its first syllable. (3) Stopping an action at its start is a counter against a shallow commit; the engine admits a counter only against a deep one (`wrapper.py:325`). (4) The deep-commit gate. (5) No. (6) Musashi: "doing this alone is defensive"; the counter's miss is the engine's price. The jobs set's `counter_shallow` (M-1) is this door exactly.

**JP-08 striking at emptiness.** (1) To strike "at the point where the mind consecrated in the hand has not yet moved" (B13). (2) Catch the opponent in the instant before his action. (3) The engine knows where each fighter is in his readiness (`ready`, `wrapper.py:141`, `:180`, `:279`, `:287`), but the exchange's sigma reads none of it (`attack_sigma`, `assemble_net_sigma`, `combat_systems.py:963-978`). (4) None. (5) No. (6) Rarity and "intense concentration" (Wilson's gloss).

**JP-09 returning the mind; *zanshin*.** (1) The struck opponent rallies "like an angry boar" (B14). (2) Keep watch after one's own blow. (3) The situation does not arise: a landed blow takes no riposte branch (`wrapper.py:410-419`); the struck man loses the Vor and his poise (`:413-415`). (4) None needed. (5) — . (6) "negligence will equal defeat" — a defeat the engine cannot produce. The "strike a second and third time" half is the burst, decided by tempo (`:471-480`).

**JP-10 the three *sen*.** (1) "you have effectively won when you forestall the enemy" (C3). (2) Take the lead by attacking first, by answering his attack, or by joining it. (3) The Vor (`initiative_sigma`, `combat_systems.py:951-956`); the Indes steal and the counter (`:1019-1029`); the aggressor's selection (`wrapper.py:264-270`). (4) As named in the row; joining is absent because each exchange has one aggressor and a tie of readiness is broken by a draw. (5) The first two, yes. (6) "This does not mean that you always attack first"; the Vor-holder still pays overcommit.

**JP-11 move the shade; trial attacks; do not repeat a third time.** (1) "used when you cannot see the enemy's spirit" (C8). (2) A feint draws information that the next action uses. (3) The feint is dissolved into commit depth and legibility (`wrapper.py:298-301`); each exchange forgets the last. (4) None. (5) No. (6) "If you are negligent you will miss the timing."

**JP-12 pass on.** (1) "infect the enemy with a bored, careless, or weak spirit" (C9). (2) Build a lull, then attack. (3) The defender's read reads nothing about the aggressor's past behaviour (`combat_systems.py:1004`). (4) None. (5) No. (6) Not stated.

**JP-13 the body of a rock.** (1)-(2) "ten thousand things cannot touch you" (C12). (3) Damage and wounds. (4) Forbidden target (agency proposal §5 Class A). (5) — . (6) Mastery; the anecdote's price is a pupil willing to die, a will the engine has no state for.

**JP-14 the twofold gaze; *metsuke*.** (1) Not to be distracted "by insignificant movements of his sword" (C14); fixing on one part "you might be dead" (F9). (2) A wide gaze that small movements do not capture. (3) The engine's distracting movements are an ornament's motion and a false edge's hidden return, both lowering the defender's read through legibility (`combat_systems.py:815-816`). (4) A defender's factor below 1 on those two terms. Nearest two: this against the `visual` lever. Separating observation: the `visual` lever's gain is the same against a plain blade and a feathered or double-edged one; the gaze's should be zero against the plain blade. UBR. (5) No. (6) Time ("You cannot master this ability quickly").

**JP-15 *kiri-otoshi*.** (1) The Ittō-ryū's defining technique: "cutting down the center line during an opponent's cut in order to displace their attacker's sword and gain victory" [SECONDARY]. (2) One cut that is attack and defence. (3) The engine's one action that is both is the landed counter (`wrapper.py:361-362`). (4) `counter_select`, `counter_success`. Nearest two: this against the proposed guard prior on parry (the jobs set's filing). Separating observation: a guard prior acts only on a lost read; a counter needs the read won — kiri-otoshi watches the cut and meets it, so it needs the read. (5) Yes, behind JP-04's door. (6) No gap allowed; the engine's miss penalty.

**JP-16 the three shouts; *kiai*.** (1) "to disturb the enemy" (C10). (2) A sound that unsettles before the cut. (3) The engine's only "unsettled" state is Concentration, drained only by blows. (4) A drain on the opponent's reserve before the exchange. (5) No. (6) Musashi: not simultaneous with the cut; the engine's natural price is a beat of readiness.

**JP-17 *yaburu*.** (1) The strong unreflective fighter keeps the over-conscious defender "in check" (D7). (2) Spontaneous, full commitment. (3) Commitment and its exposure. (4) Aggressive temperament. (5) Yes. (6) Chōzan: "he will be tricked by an opponent with superior technique"; the engine wires the overcommit exposure and riposte, but measured temperament monotone (agency proposal D3), so the price does not bite.

**JP-18 *ki-ken-tai-icchi*.** (1) Without shout, sword and step together, no point (F6). (2) A synchronised strike. (3) The strike is one roll (`core.resolve`, `core.py:108-117`). (4) None needed. (5) — . (6) — . Rejected: "becoming the blade" → a weapon lever (`spine_press`, `leverage`): nothing in the source concerns the weapon's physics.

## China — philosophy and martial theory

**CP-01 soft overcomes hard; water.** (1)-(2) A general law; "The text is not about fighting" (sheet). (3) No fight situation is named. (4) None. (5) — . (6) "no one is able to carry it out in practice." Rejected: water → `tactile` or yielding; the martial reading is CP-04's and carries its own chain.

**CP-02 avoid the strong, strike the weak.** (1) "attack places which are undefended" (VI.7). (2) Take the line of least resistance. (3) The engine's attacker already takes the best-coupling head against the armour (`select_mode`); its defender who reads the attack takes the best mode. (4) The selection functions. (5) Yes, for everyone: the concept gives no school an identity. (6) "there are no constant conditions."

**CP-03 double weighting.** (1) "if you are doubly weighted you are stuck … controlled by others." (2) Weight committed fully and evenly cannot change. (3) Commitment that the body cannot recover from is the overcommit exposure, curbed by footwork (`anti_overcommit`, `combat_systems.py:180`, `:1038-1039`). (4) The `balance` axis inside `balance_eff`. Nearest two: the axis against the `anti_overcommit` bonus (`true_times`). Separating observation: the axis also moves dodge and the footwork contests; the bonus moves only exposure. The Taiji fault is structural (weight), so the axis. UBR. (5) Yes. (6) "years of pure work" do not protect; no in-fight price.

**CP-04 yield and stick.** (1) "when the other is hard and I am soft, this is called yielding"; the faults are losing contact and butting (commentary). (2) Feel the opponent's force through contact and give way to it while keeping contact. (3) The bind (`bind_sigma`, `combat_systems.py:926-945`; loop `wrapper.py:420-443`). (4) Feel: the `tactile` term. Yield: a branch on the opponent's hardness, absent. Nearest two: `tactile` against `leverage`; separated in Part 7 §7.2. (5) Feel, yes. (6) "give up oneself, follow the other" — the initiative; the engine gives the Vor to the bind winner (`wrapper.py:427-428`), so a yield would forgo it.

**CP-05 four ounces.** (1) "clearly it is not victory by strength … what could speed have to do with it?" (2) The small force wins *because* the large one is large. (3) The bind's force terms. (4) None: **run** (Part 7 §7.2) — the feel's gain in log-odds is 0.285 at the opponent's Strength 4 and 0.285 at 7; it does not grow with his force. The engine also gives Strength little weight in the bind (50.0% to 48.8% from Strength 4 to 7). (5) No. (6) "a hair's difference becomes an error of a thousand li."

**CP-06 stillness controls movement.** (1) The external school "is chiefly about striking people, and people can exploit that"; the internal "uses stillness to control movement; whoever attacks it falls" (1669). (2) Do not break one's own posture; his first movement is his break. (3) One's own commitment; the door that his commitment opens (`wrapper.py:325`). (4) Temperament. Nearest two: temperament against `counter_select`; **run** (Part 7 §7.1): temperament alone moves one's own deep commits (0.7% → 0.1%) and σ (0.015 → −0.124); the lever alone moves the reach. (5) Yes. (6) "waiting costs the initiative": the Vor drift; the run also finds more of the still fighter's weak attacks answered by a riposte (13.3% → 14.9%). The payoff is not reproduced.

**CP-07 first make yourself unbeatable.** (1) "the opportunity of defeating the enemy is provided by the enemy himself." (2)-(4) As CP-06. (5) Yes. (6) "standing on the defensive indicates insufficient strength."

**CP-08 he does not know me.** (1) "he does not know me, I alone know him; the hero's irresistibility all comes from this." (2) An asymmetry of reading. (3) The read contest. (4) `visual` sits on both sides of it (`combat_systems.py:1004`, `:1011`). Nearest two: `visual` against `tactile` (the passage is set in contact). Separating observation: `tactile` acts only in the bind and only on one's own reading; `visual` acts in every exchange on both halves. UBR. (5) Yes. (6) "weight must be fluid"; none in the fight.

**CP-09 *shi*; store like a bow.** (1) The falcon's "self-restraint which keeps the bird from swooping … until the right moment". (2) Commit only when the moment comes. (3) The commit is drawn each exchange from temperament and wariness only (`combat_systems.py:989-994`). (4) None. (5) No. (6) "the right moment" and prior arrangement.

**CP-10 maiden, then hare; the Maiden of Yue.** (1) "exhibit the coyness of a maiden, until the enemy gives you an opening". (2) A lull, then sudden speed. (3) The aggressor's suddenness is in the read (`AGI_READ_K`, `combat_systems.py:1011`); the lull has no state. (4) Agility for the hare; none for the maiden. (5) The hare, yes. (6) Waiting.

**CP-11 no parry, just one strike.** (1) "fall into parry and block and there are ten". (2) Answer the attack with a strike, not a defence. (3) The counter (`combat_systems.py:1026-1029`). (4) `counter_select`. (5) Yes, behind JP-04's door. (6) Qi's cost is the guard given up; the engine's miss is exactly that.

**CP-12 courage first.** (1) "once fear fills the middle, the limbs stagnate outside." (2) Fear disables skill. (3) No fear state exists in the bout; the engine's "limbs stagnate" is the drained Concentration. (4) Concentration. (5) Yes, near-inert (JP-01). (6) "seven-tenths is lost" to fear in practice; none wired.

## China — myth and the wuxia genre

**CM-01 the wooden cockerel.** (1)-(2) "no other cock dares answer; they turn and run." (3) An opponent's exit by choice is the decider's `withdraw`, which sees only wound state (`fight.py:207-209`). (4) None in combat. (5) — . (6) Four stages of display unlearned. It belongs to the season's challenge layer.

**CM-02 Gai Nie's glare.** (1) An opponent in a dispute about swords; "Gai Nie, angered, glared at him". (2) Presence alone makes the other leave. (3) Leaving is the decider's `withdraw`, which reads no quality of the other fighter (`fight.py:207-209`). (4) None in combat. (5) No. (6) The withdrawer's yielded standing; it belongs to the season's challenge and the social contest.

**CM-03 "show emptiness … arrive before him".** (1) The swordsman shows an opening as a lure. (2) Lure the commitment, then arrive first. (3) The counter; the opponent's commitment. (4) Counter levers; nothing for the lure (N-3). (5) The counter, yes. (6) The lower sword's waste.

**CM-04 *qinggong*.** (1) Lightness: to move swiftly and evade ("my body was as light as the wind"). (2) Mobility and evasion. (3) Evasion is the dodge; mobility is cadence and the close. (4) Agility. Nearest two: Agility against the `balance` lever. **Run** (Part 7 §7.4): Agility 5 lifts the dodge σ from 0.041 to 0.153 and the close rate from 0.250 to 0.298; `footing_refined` at level 2 leaves both untouched and moves only the footwork contest (0.000 → 0.281). Rejected: "clouds" → `balance`. (5) Yes (attribute). (6) None stated.

**CM-05 iron shirt.** (1) Blows and blades. (2) "directing energy to parts of the body can reinforce these parts of the body to take blows". (3) Damage and wounds (`core.strike`; `combatant.py:47-95`). (4) None: agency proposal §5 Class A forbids an ability on them. (5) The engine's iron shirt is the armour tier, a loadout fact. (6) Training only.

**CM-06 striking the points.** (1)-(2) A strike to a point disables ("death points, dizzy points, mute points", 1669). (3) Damage (`core.strike`, coupling). (4) None: Class A. (5) Gap precision is the weapon's (`geo['gap']`). (6) The 1934 precepts against misuse.

**CM-07 no move beats move.** (1) A fixed sequence lets the opponent "predict and counter". (2) Formlessness defeats reading. (3) The one style a reader knows is the tradition (`familiarity`, `traditions.py:40-48`). (4) None, and the engine's rule runs the other way: **run** (Part 7 §7.4) — a German defender reads a `none` attacker at 68.6%, a Japanese one at 55.3%, and an attacker facing an unfamiliar defender commits shallower (Beta 1.038, 1.362) while one facing a `none` defender does not. The formless fighter is the most legible. (5) No. (6) Understanding over memory.

## Europe, the Mediterranean, the Norse and the Irish

**EU-01 the Lynx.** (1)-(2) A virtue: sight and measure. (3) Sight is the read; measure is the measure contest. (4) Perception; the `measure` lever. (5) Yes. (6) Not stated. Fiore attaches no technique to the animals; the row maps a virtue to attributes, not to a lever.

**EU-02 the Tiger.** (1)-(2) Speed: "so quick to run and turn" that nothing catches it. (3) Speed of acting is cadence (`combat_systems.py:107`), of evading the dodge (`:327`), of closing the close rate (`:1225`). (4) Agility, which feeds all three; CM-04's run separates it from the `balance` lever. (5) Yes (attribute). (6) Not stated.

**EU-03 the Lion; "a despondent heart".** (1) "regardless of all skill". (2)-(5) As CP-12. (6) Exclusion from training, a host-side `requires`.

**EU-04 the Elephant.** (1) "I neither fall to my knees nor lose my footing." (2) Not toppled. (3) Being toppled is losing poise. (4) Resistance to the break, absent; recovery (Focus) present. Nearest two: break resistance against `balance_eff` (Strength and Agility). Separating observation: `balance_eff` moves the dodge and footwork, never the size of a poise break. (5) Recovery, yes. (6) None in Fiore.

**EU-05 Before and After.** (1) "the entire art of fencing is based upon it." (2) The one who takes the lead keeps the other answering. (3) The Vor. (4) The contest structure. (5) Yes, for everyone. (6) Meyer's "caught and rushed past in their own cut" is the overcommit exposure, wired.

**EU-06 *Indes*.** (1) "the key which unlocks the art". (2) At the instant of contact, feel and act. (3) The Indes steal, open and in the bind (`combat_systems.py:1019-1024`, `:1055-1057`; bind entry `wrapper.py:424-428`). (4) As named. (5) Yes: in the bind it fires at every bind entry; in the open behind JP-04's door. (6) Readiness at the instant.

**EU-07 *Fühlen* and the windings.** (1) "test the bind no more than soft or hard". (2) The feel selects the next action: double against the strong, mutate against the soft [HEMA sheet §3]. (3) The bind; `bind_sigma` is the quantity the glosses condition on. (4) Feel: `tactile`; the selection: absent. (5) Feel, yes. (6) "do not be overeager in the war".

**EU-08 the true and false fight.** (1) The foot moved first binds the hand "to the time of the foot". (2) Hand before foot. (3) Two engine readings: reach on the approach (`true_time_edge`) and commitment (`true_times` on `anti_overcommit`). (4) Both exist. Nearest two: these two; separating observation: `true_time_edge` changes with the reach gap and fades with armour; `true_times` changes with commitment. Paradox 14 speaks of the order of hand and foot, which is closer to commitment (a lunge is the foot first); the engine's docstring argues reach. UBR. (5) Yes. (6) The hand's lost freedom: the lunge's exposure and legibility.

**EU-09 the governors; the twofold mind.** (1) "impossible to fight safe" without them. (2) Advance with the readiness to fly back. (3) Commitment's exposure. (4) `anti_overcommit`. (5) Yes. (6) None named; the real price would be a shallower press.

**EU-10 Fabris on weak and strong.** (1) The cut "requires greater strength … if it misses, is thrown into disorder". (2) Subtlety over strength; the thrust is safer. (3) Legibility, retraction and swing room (`combat_systems.py:803`, `:210`, `:219-220`). (4) The weapon's own physics. (5) Yes, for everyone who holds a thrusting weapon; no technique. (6) The cut's disorder, wired as the swing's recovery.

**EU-11 *berserkr*.** (1) The sources state effects, not a problem: the rush, the blow, invulnerability. (2) Frenzy. (3) Commitment; the armour chosen; Strength; wounds. (4) Temperament; loadout; Strength; Class A for invulnerability; nothing for the crash. (5) The rush, yes. (6) "when the fever abated they were weak": a state with an end, absent (N-7).

**EU-12 *ríastrad*.** (1)-(2) A transforming fury that overthrows fifty. (3) No bout state persists across exchanges except the trackers, initiative and poise. (4) None. (5) No. (6) The fury must be quenched from outside (three vats): a state ended by others, which N-7 would need.

**EU-13 *geis*.** (1) Keeping it "is believed to bring power". (2) A vow conditions power. (3) The host composes the board. (4) A board condition. (5) Yes, host-side. (6) The vow itself.

**EU-14 *Gáe Bulg*.** (1)-(2) An attack no defence answers. (3) The defence (`mode_sigma`, `defence_sigma`, the neutralise draw `wrapper.py:344`). (4) None: removing the defence sets an outcome (agency proposal §5.1 rule 2). (5) — . (6) The kin it kills.

**EU-15 Destreza's circle.** (1) Moving straight at him meets his point. (2) Step off the line. (3) The close and the standing target: the facing state. (4) `facing_regime`. (5) The geometry, yes; the lever is held bare by Jordan's 2026-11-01 ruling, so no content is proposed. (6) Rigidity.

## South Asia and the Sikh tradition

**SA-01 one-pointed aim; Drona's test.** (1) "The archer should totally fix his mind on the object, only then he never fails." (2) Attention narrowed to the mark. (3) The attacker's attention is the `consistency` term of his attack. (4) Concentration, a reserve. Takuan's opposite rule lands on the same number: the engine cannot tell narrow from spread attention. (5) The reserve, yes. (6) Exclusion of the one who sees the scene.

**SA-02 "the body becomes all eyes".** (1) The master is "looking for the gaps" when a gaze lapses. (2) A lapse is an opening; the adept has none. (3) The lapse is the drained reserve; nobody sees it. (4) Concentration; seeing the gap needs N-2. (5) The lapse, yes. (6) The state is temporary.

**SA-03 breath.** (1) Kumbhak "enables one to achieve great strength and stamina". (2) Regulated breath spends less. (3) The stamina economy. (4) `act_cost`. Nearest two: the reserve against the cost per action; breath is per action. UBR. (5) No technique; the reserve is an attribute. (6) None named.

**SA-04 the *astra* and its recall.** (1) One who cannot recall the weapon is destroyed by it. (2) Casting requires the counter. (3) Curriculum order. (4) `requires`, host-side. (5) Yes. (6) Training; for the weapon itself the canon has no carrier.

**SA-05 *sākā*.** (1)-(2) No quarter. (3) The terms and the choice set. (4) Terms `death`, no `withdraw`. (5) Yes. (6) Death.

**SA-06 *avadhya*.** (1)-(2) Whom not to strike. (3) The disposition of a yielded man. (4) The host's. (5) Yes. (6) Cowardly speech loses heaven.

**SA-07 *śakti* and *bal*.** (1)-(2) Two kinds of strength. (3) Strength; nothing moral. (4) Strength for bal. (5) Bal, yes. (6) Shakti is lost by conduct: no carrier.

## Southeast Asia, Persia and the Islamic world

**SE-01 the lotus.** (1)-(2) The soft thing is unharmed. (3) The void. (4) The dodge mode; the engine chooses it when it is best. UBR against JP-02. (5) Yes. (6) None stated.

**SE-02 Kumango's three attacks.** (1) Evade and advise thrice. (2) Escalation counted across attacks. (3) No refusal to strike; no count. (4) None. (5) No. (6) The challenger's injury.

**SE-03 *Siku 12*.** (1) The attacker "collapses from exhaustion". (2) Evade until he tires. (3) The aggressor's `act_cost`; the collapse separation. (4) Stamina. (5) Exhaustion, yes; the win, no. (6) A taunt accepted.

**SE-04 the charms.** (1)-(2) Protection that holds while the taboo is kept. (3) Wounds and damage. (4) None (Class A); the condition is a host-side rule, as EU-13. (5) — . (6) Loss on breach or theft. Part 5: the canon gives world-altering effect only to threadwork.

**SE-05 *juramentado*.** (1)-(2) An oath-bound charge that keeps coming after wounds. (3) Commitment; the wound impairment and the felling threshold. (4) Temperament for the charge; nothing for the endurance (trauma physiology, Class A). (5) The charge, yes. (6) The oath is to die: terms `death`.

**SE-06 *sinawali*.** (1) Continuous alternating strike and counter. (2) Flow without a reset. (3) The burst, decided by readiness. (4) `tempo`. (5) Yes. (6) Not stated.

**SE-07 *pahlavan*.** (1)-(2) Strength that must rest on purity. (3) Strength (Part 3). (4) Nothing conditions Strength on conduct. (5) — . (6) — . No canon carrier.

## Africa, the Afro-Atlantic, the Americas and the Pacific

**AF-01 *malícia*.** (1) To understand intentions and misdirect. (2) Reading plus deception. (3) The read contest; no memory. (4) `visual`; N-1. (5) Reading, yes. (6) "too clever a fighter confuses himself."

**AF-02 *ginga*.** (1) A still target is easy. (2) Motion that both evades and masks. (3) The dodge; the attacker's suddenness. (4) Agility. Rejected: footwork → `balance` (CM-04's run). (5) Yes. (6) Standing still.

**AF-03 *corpo fechado*.** (1)-(2) A closed body that blades and bullets do not harm. (3) Wounds and damage. (4) None (Class A). (5) — . (6) A ritual dagger defeats it; Part 5.

**AF-04 counting coup.** (1) Touch a living, unhurt man and leave him alive. (2) Honour from exposure. (3) The terms. (4) `blood`, the nearest; no touch term. (5) Nearly. (6) Close approach under fire.

**AF-05 the dog rope.** (1) Fixed to one spot. (2) A vow forbids retreat. (3) The decider; the fighting withdrawal. (4) The choice set; the `withdraw_band` narrowed. (5) The first. (6) No retreat.

**AF-06 Crazy Dogs.** (1)-(2) A man tired of life vows to "rush into danger and deliberately seek death" for a season. (3) Commitment; the choice set; the terms. (4) Temperament at its aggressive pole; terms `death`; no `withdraw`. (5) Yes, host-side. (6) Death, renewable; in the engine D3 leaves the aggressive pole under-priced, so the vow costs less than the tradition says.

**AF-07 *mau rākau*.** (1) "avoiding blow and thrust"; feint with the point, strike with the butt. (2) Avoidance; the feint; recovery. (3) Agility; `select_mode`; recoverability. (4) As named; N-1 for the feint. (5) Mostly. (6) Ritual.

**AF-08 *haka*.** (1) To render "a human shape frightful". (2) Intimidation. (3) The opponent's Concentration, full at the fight's start. (4) N-4. (5) No. (6) An error is unlucky.

**AF-09 *dônga*.** (1) Self-restraint; the referee. (2) A duel that does not kill. (3) The terms and `Yield`. (4) As named. (5) Yes. (6) Compensation for a death.
