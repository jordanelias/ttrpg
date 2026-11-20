# Grounding note: how bodies of troops moved and behaved in a pre-gunpowder battle

## Status: FILED — reference, tier 3 (`research/00_INDEX.md` §1) · not canon (CLAUDE.md §0.05) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: MB (historical adjudication lane of `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

Sibling of `mass_battle_casualties_and_results_grounding.md` (same date; **its tier table and its source keys
KR, SA, DP, CL, ACOUP and the `W-` battle pages apply here unchanged**). This note covers **movement** (rates,
frontage, formation change, fatigue) and **behaviour** (the decision to engage, command and signals, cohesion,
giving ground, rout, rally, pursuit, reserves, flank action).

## Additional sources

| key | source | what it is | tier · read |
|---|---|---|---|
| W-GAIT | `https://en.wikipedia.org/wiki/Horse_gait` | encyclopedia article | `[T]` 2026-11-12 |
| W-LOAD | `https://en.wikipedia.org/wiki/Loaded_march` | encyclopedia article; its Vegetius figures are cited to two hobby sites, not to the text | `[T]` |
| W-RIT | `https://en.wikipedia.org/wiki/Roman_infantry_tactics` | encyclopedia article citing Polybius, Vegetius, Goldsworthy, Taylor | `[T]` (part: first 100,000 of 231,719 characters) |
| W-PHX | `https://en.wikipedia.org/wiki/Phalanx` | encyclopedia article citing Phifer, Goldsworthy | `[T]` |
| W-NAP | `https://en.wikipedia.org/wiki/Napoleonic_tactics` | encyclopedia article | `[T]` |
| W-SQ | `https://en.wikipedia.org/wiki/Infantry_square` | encyclopedia article | `[T]` |
| W-PIKE | `https://en.wikipedia.org/wiki/Pike_square` | encyclopedia article resting on one source | `[T]` |
| W-CHG | `https://en.wikipedia.org/wiki/Charge_(warfare)` | encyclopedia article, tagged as needing citations | `[T]` |
| W-FR | `https://en.wikipedia.org/wiki/Feigned_retreat` | encyclopedia article | `[T]` |
| W-WD | `https://en.wikipedia.org/wiki/Withdrawal_(military)` | encyclopedia article | `[T]` |
| W-ROUT | `https://en.wikipedia.org/wiki/Rout` | encyclopedia article | `[T]` |
| W-MON | `https://en.wikipedia.org/wiki/Mongol_military_tactics_and_organization` | encyclopedia article | `[T]` |
| W-STR | `https://en.wikipedia.org/wiki/Strategikon_of_Maurice` | encyclopedia article (contents by book only) | `[T]` |
| BAL | "Battalion line, column, and square – Tactical formations during the Napoleonic Wars", balagan.info, `https://balagan.info/battalion-line-column-and-square-tactical-formations-during-the-napoleonic-wars` | a wargamer's compilation citing Nafziger (1996), Nosworthy (1995), Haythornthwaite (2001, 2008), Griffith (2007), Muir (1998) | `[T]`; second-hand for every figure |
| SN-PACE | search result, 2026-11-12, for Napoleonic infantry paces (summarising an 1807 British manual and a note in the Hamilton Papers, `founders.archives.gov`) | snippet | `[S]` |
| SN-CAV | search result, 2026-11-12, for cavalry charge stages (a forum quotation of British *Cavalry Training* 1904; a blog on an 1883 US manual) | snippet | `[S]` |
| SN-ENG | search result, 2026-11-12, for Donald Engels, *Alexander the Great and the Logistics of the Macedonian Army* (1978) march rates, as reported by a wargame design appendix and a review | snippet | `[S]` |

**Sought and not reached:** Vegetius's own text (two addresses: one now serves unrelated content, one 404);
the *Strategikon* and Leo's *Tactica* in translation (the encyclopedia page gives contents only); Engels's book;
Nafziger, *Imperial Bayonets*; any drill regulation; "Erwin on march rates" (**not identified**: this lane
could not tell which author is meant and found nothing under that name; nothing is attributed to it).

## What is established

### A. Rates of movement

| # | claim | tier |
|---|---|---|
| M1 | Horse: walk "averages about 7 kilometres per hour"; trot "about 13"; canter "16–27 km/h"; gallop "about 40 to 48". "Horses seldom will gallop more than 1.5 to 3 kilometres … before they need to rest"; they "can only canter and gallop for short periods at a time". | `[T]` W-GAIT |
| M2 | A second reading of the gaits for horse under a soldier: walk 4 mph, trot 8 mph, "normal rate of gallop" 15 mph (British *Cavalry Training* 1904, as quoted on a forum). Slower than M1's unladen averages at the gallop. | `[S]` SN-CAV |
| M3 | Infantry drill paces around 1800: ordinary 75 paces a minute and quick 108, on a 30-inch pace (British 1807; Prussian the same); French 1791 about 76 and 100. By arithmetic on those figures: 57 m and 82 m a minute, 3.4 and 4.9 km/h. | `[S]` SN-PACE; the conversion is this lane's arithmetic |
| M4 | Roman training march as usually quoted from Vegetius: 20 Roman miles (29.6 km) in five summer hours at the military step, 24 (35.5 km) at the full step, under a load of about 20.5 kg. The article notes five summer hours is about six modern hours. That is about 4.9 and 5.9 km/h for a training march, **not a battlefield advance**. | `[T]` W-LOAD, W-RIT; Vegetius's text itself not read |
| M5 | An army's daily march (Engels on Alexander, second-hand): about 15 miles a day average for the whole force, 19.5 the highest recorded for the whole force; small mounted detachments far more. | `[S]` SN-ENG; a lead only |
| M6 | A Crusader fighting march under harassment (Arsuf, 1191): marched "only in the morning, before the heat, with frequent rests beside water"; "the pace was deliberately slow"; one day's stretch named as 10 km; rest days taken. | `[T]` W-ARS |
| M7 | Mongols: "three or four horses" a man; rotation of mounts let them "travel at high speed for days". No daily distance on the page read. | `[T]` W-MON |
| M8 | Kriegsspiel (1824), a professional army's own planning figures for a two-minute turn: a cavalry squadron moves 400 paces on open ground, 250 through light forest, 100 up inclines (a pace about 63 cm): about 7.6, 4.7 and 1.9 km/h. No infantry rate on the page read. | `[T]` `mass_battle_wargame_models_grounding.md` K1 |
| M9 | **Battlefield advance rate of formed heavy infantry: not established** by any page read. The tree's own figures (`research/pre_firearms_formations/10_battle_phase_choreography.md:300-318`: 3–4 km/h advancing, 5–7 for a Swiss attack; `12_…:858-867`) are memory tier and self-described as derived (`12_…:936-938`). M3's ordinary pace (3.4 km/h) is the nearest sourced figure and is from another era. | — |
| M10 | **Terrain multipliers: not established** beyond M8's Kriegsspiel ratios (light forest 0.62 of open; uphill 0.25, for cavalry) and Agincourt's qualitative mud ("scarcely lift their weapons", W-AGI). | — |

### B. Space a man and a body take up

| # | claim | tier |
|---|---|---|
| F1 | Roman legionary: Polybius (18.29–30) six feet of frontage a man; Vegetius (3.14) three. Sabin: "the truth may be that legionaries could vary their own frontage between three and six feet, perhaps by the simple expedient of having every second rank step into or out of the gaps in the rank in front", with close order the rule in massed combat. | `[D]` SA p. 10 |
| F2 | Macedonian phalangites "could form a special 'locked shields' formation with a frontage of only eighteen inches each". Hoplites: about 1.8–2 m in marching order, half that in dense order, "as small as 0.45 metres" with locked shields. | `[D]` SA p. 10; `[T]` W-PHX |
| F3 | Depth: hoplites "eight men or more"; Macedonian phalanx 16, sometimes 32; Thebans 25 deep at Delium and 50 at Leuctra; Pompey ten deep and Caesar six at Pharsalus; Seleucids 32 at Magnesia; French 16 deep at Agincourt. | `[T]` W-PHX, W-PHA, W-AGI; `[D]` SA pp. 1, 7 |
| F4 | A Roman "infantry battle array a mile long and containing tens of thousands of troops". | `[D]` SA p. 11 |
| F5 | Napoleonic foot: 22 inches (56 cm) a man officially, up to 27–30 in battle; 600 men in two ranks "about 180 yards". | `[T]` BAL, second-hand |
| F6 | Intervals between sub-units: Roman maniples 10–20 m (Taylor); elephants at Zama about 30 m apart; Hannibal's third line about 200 m behind his second. | `[T]` W-RIT, W-ZAM |
| F7 | Agincourt: the English held "a 750-yard (690 m) part of the defile" with 6,000–9,000 men. Infantry square of 500 men in four ranks: "less than 20 m long on any side". | `[T]` W-AGI, W-SQ |

### C. Changing formation

| # | claim | tier |
|---|---|---|
| X1 | Napoleonic drill times, second-hand: column to square "would take only 60 seconds" (Nafziger); line to square "within 100 seconds" (French regulations, per napoleonistyka); attack column to square "30 seconds"; the compiler adds that field times were longer. Line-to-column and column-to-line times: **not established**. | `[T]` BAL |
| X2 | "Any unit that tried to change formation in the face of enemy fire was in trouble" (Griffith); deploying from column to line under heavy fire was impossible (Haythornthwaite). A square broke when it was "formed too late" (Acosta Ñu) or caught incomplete (Ramu). | `[T]` BAL, W-SQ |
| X3 | Changing formation is tied to the enemy's nearness: column to move, line to fight foot, square against horse; a square "was slower than a column". | `[T]` W-NAP |
| X4 | A Roman army re-formed in the middle of a battle only in a pause: at Zama, Scipio recalled the pursuing hastati by bugle and "re-form[ed] into a single extended line after a prolonged pause" before meeting the veterans. Devereaux treats this as "an unusual, ordered pause". | `[T]` W-ZAM, ACOUP |
| X5 | A well-drilled pike square "could change direction very quickly"; when stationary it could "point pikes in any direction". The Hellenistic phalanx, by Polybius, was vulnerable "to differential advances and retreats". | `[T]` W-PIKE; `[D]` SA p. 6 |
| X6 | **Pre-gunpowder formation-change times: not established.** | — |

### D. Fatigue

| # | claim | tier |
|---|---|---|
| T1 | "If the contests could drag on for hours, it is impossible to imagine individual front-rankers managing the sustained physical effort required"; hence lulls. Sabin's model: a "default state" of stand-off at a small separation, "punctuated by periodic and localized charges into contact"; a flurry ends "when one side got the worst of the exchange" and steps back. | `[D]` SA pp. 10, 14–16 |
| T2 | The limit of continuous contact is asserted, not measured: Devereaux says the claim that contact beyond "thirty-or-so minutes" is impossible "is always made without evidence". **How long a flurry lasts is not established.** | `[T]` ACOUP |
| T3 | Fatigue strikes everyone in the fighting line, not only those striking: "all ranks would be subjected to intense and prolonged physical and emotional stress". Holding the supports "back outside javelin range" kept them fresh. | `[D]` SA p. 16 |
| T4 | Fresh against tired is the Roman advantage (results note D3). Du Picq, as Sabin quotes him: "the best dispositions were those that made easiest a succession of efforts by assuring the relief by ranks of units in action, actually engaging only the necessary units and keeping the rest as a support or reserve outside of the immediate sphere of moral tension." | `[D]` SA pp. 7, 16–17 |
| T5 | Heat, load and ground: Arsuf's march only in the cool; Agincourt's mud; the French at Crécy attacked the same afternoon after "a march of about 12 miles" against an army "rested and fed" "in position since dawn". Caesar's men at Pharsalus, finding the enemy would not advance, "stopped to rest and regroup before continuing the charge". | `[T]` W-ARS, W-AGI, W-CRE (`mass_battle_maneuver_sequences_grounding.md`), W-PHA |
| T6 | Horses tire within one to three kilometres of gallop (M1); Richard held his charge at Arsuf until the enemy's "horses [were] tiring". | `[T]` W-GAIT, W-ARS |
| T7 | Carrying more costs more: **no sourced figure** for the fatigue or speed cost of a second weapon. The Roman training load (M4) and "about 27 kilograms" of kit (W-RIT, unsourced there) are the only load figures read. | — |

### E. The decision to engage, and command

| # | claim | tier |
|---|---|---|
| E1 | Friction: "Everything is very simple in War, but the simplest thing is difficult"; "Activity in War is movement in a resistant medium"; a battalion "always remains composed of a number of men", any of whom may delay it; fog hides the enemy and "stops batteries and reports from working on time"; rain turns a three-hour march into eight. | `[T]` CL Book I ch. VII |
| E2 | A battle was often offered and declined: "often engagements … would be resolved by one side fleeing before the battle" (hoplites); the English and French at Agincourt stood about three hours before Henry moved; a French council at Crécy advised waiting a day and was overridden. | `[T]` W-PHX, W-AGI, W-CRE |
| E3 | Orders were carried by sound and sign, and were few: Richard's signal for the charge at Arsuf was "six clear trumpet blasts"; Scipio recalled a pursuit "by trumpet"; Mongols "utilized signal flags and horns". | `[T]` W-ARS, W-ZAM, W-MON |
| E4 | Orders were disobeyed at the decisive moment: the Hospitallers at Arsuf charged without the signal and Richard, "determined to hold his army together", turned it into the general charge; the French knights at Crécy pressed forward against the plan; Gloucester at Bannockburn attacked on a taunt. | `[T]` W-ARS, W-CRE, W-BAN |
| E5 | Delay by design in a professional's game: the Kriegsspiel umpire "decides how troops would interpret and execute a given order" and can hold "a player's message for a round or two". | `[T]` wargame note K4 |
| E6 | The commander's own act is to hold and release reserves: "the number of fresh reserves is always the chief point to be looked at by both Commanders"; du Picq: "Have reserves to threaten with, held with an iron hand"; "commanders can hold out decisive reserves only if the enemy has been forced to commit his". | `[T]` CL Book IV ch. IX; DP |
| E7 | The culminating point (the attack that outruns its strength) is Clausewitz Book VII ch. 5 by attribution only; **its text was not read**. | `[T]` `https://en.wikipedia.org/wiki/Culminating_point` |

### F. Cohesion, giving ground, rout

| # | claim | tier |
|---|---|---|
| R1 | Du Picq, as Sabin quotes him: "Man does not enter battle to fight, but for victory. He does everything that he can to avoid the first and obtain the second." "Discipline keeps enemies face to face a little longer, but cannot supplant the instinct of self-preservation". | `[D]` SA p. 13 |
| R2 | Morale is interactive between the two lines: "if one side could nerve itself to launch a bayonet charge in the conviction that the enemy would not stand, the enemy did indeed break before contact". Bayonet charges "rarely" made contact; "one side usually fled before actual bayonet fighting ensued". | `[D]` SA p. 13; `[T]` W-CHG, W-NAP |
| R3 | Three outcomes short of destruction are real and distinct: holding; being **pushed back** while in order (results note D4); **breaking**. A line "can be 'pushed' backward while still in cohesion" (Devereaux). | `[D]` SA p. 6; `[T]` ACOUP |
| R4 | A break starts at the rear and spreads from the point struck (results note D6, D7). A second line that will not receive the first makes it worse: at Zama the second Carthaginian line "blocks [the first's] retreat, so survivors escape around the flanks". | `[D]` SA p. 15 (Livy 30.34); `[T]` W-ZAM |
| R5 | Triggers of a break, in Sabin's list: "the breaching of their line, a psychological shock such as the death of the general, or the sheer accumulation of casualties and fatigue." Examples read: Harold's death late at Hastings ("Leaderless, the English broke"); Darius's flight at Gaugamela; Edward II led off the field at Bannockburn; the Cumans breaking and disordering the Rus' at the Kalka. | `[D]` SA p. 15; `[T]` W-HAS, W-GAU, W-BAN, W-KAL |
| R6 | A rout is "a collapse in a given unit's command authority, unit cohesion and combat morale"; "a routed formation will often cause a complete breakdown in the entire front". Routed men throw away their kit (hoplites "had thrown away their heavy shields"). | `[T]` W-ROUT; `[D]` SA p. 5 |
| R7 | Not every beaten body routs: a household may stand and die around its lord (Hastings); a rearguard may turn on the pursuit (the Malfosse); part may withdraw to a camp and hold three days (Kalka); a defeated Roman army "could leave 'in good order'" if its last line held. | `[T]` W-HAS, W-KAL, W-RIT |

### G. Rally and pursuit

| # | claim | tier |
|---|---|---|
| P1 | Rally of troops who have run is attested for lighter troops and doubted for heavy ones: Celtic retirements where "the troops simply turned and ran, and then rallied once they had temporarily outdistanced pursuit (Livy 22.47; Caesar, BG 2.23)"; "it is hard to envisage more heavily equipped troops succeeding with such an approach in the face of an active opponent". The Helvetii "fell back no less than a mile … before resuming fierce resistance". | `[D]` SA p. 6 |
| P2 | A leader stops a panic in person: William at Hastings, on the rumour of his death, "rode through his lines to show he was alive, then counter-attacked". | `[T]` W-HAS (part) |
| P3 | Pursuit is done by the fast: defeated troops "mercilessly slaughtered from behind by faster enemy cavalry"; "lightly equipped troops such as light cavalry, auxiliaries, partisans or militia … could often keep up the pursuit into the following day". Foot pursued too, at their own pace: the Flemings chased the French "over 10 km". | `[D]` SA p. 5; `[T]` W-ROUT, W-GS |
| P4 | Pursuit is a risk to the pursuer and commanders limited it: the Greeks feared "a reversal if the troops dispersed" (KR p. 20); Richard "halted the pursuit after about 1.5 km" at Arsuf, re-formed on his reserve, and charged twice more; Scipio recalled the hastati and so, on one reading, "avoided the trap"; the English who chased the Bretons downhill at Hastings were cut off and killed. Clausewitz grades pursuit in three degrees (cavalry alone; an advance guard of all arms; the whole army) and notes "night usually ends pursuit". | `[D]` KR p. 20; `[T]` W-ARS, W-ZAM, W-HAS, CL Book IV ch. XII |
| P5 | Cavalry that wins its wing and pursues is absent from the main fight until it comes back: at Cannae and Zama its return on the infantry's rear decided the day; at Gaugamela cavalry that broke through "raided the camp" instead of taking the phalanx in rear. | `[T]` W-CAN, W-ZAM, W-GAU; `[D]` SA pp. 4–5 |
| P6 | A feigned flight exploits the pursuer's urge (see the manoeuvre note): it "requires well-disciplined soldiers" and risks that "the rout will become genuine". | `[T]` W-FR |

### H. Horse against foot

| # | claim | tier |
|---|---|---|
| H1 | Keegan, as the page reports him: cavalry charges "often failed against infantry, with horses refusing to gallop into the dense mass of enemies"; success came from "the defending formation breaking up (often in fear) and scattering"; pikemen "with high morale 'could stave off all but the best cavalry charges'". Du Picq: "There never was an encounter between cavalry and infantry"; of horse against horse, when "close enough to recognize faces, these cavalrymen slackened their gait and both turned their backs". | `[T]` W-CHG, DP Part I ch. I, V |
| H2 | Steady foot held: Waterloo's four-rank squares "withstood eleven cavalry charges"; at Courtrai "the Flemish infantry wall did not flinch as expected and a part of the French cavalry hesitated". Squares broke through accident (a dying horse crashing in), lateness, wet powder or surprise. | `[T]` W-SQ, W-GS |
| H3 | A square or pike block pays for its safety against horse: it is "slower than a column and more vulnerable to musket and cannon fire"; "the most effective way to break a square was … artillery". | `[T]` W-NAP, W-SQ |
| H4 | A charge was built up by gait and released late: gallop "within 50 yards" (a nineteenth-century drill text, snippet); an 1883 practice field of 250 yards walked, trotted and then galloped; "cavalry could cover 'the final 50 yards (46 m)' and receive only a single volley". **Stage distances for a medieval charge are not established**; the tree's figures (`04_high_medieval.md:22-36`) are memory tier. | `[S]` SN-CAV; `[T]` W-NAP |

## What this note does NOT establish

- Any battlefield speed for formed infantry before 1700, any terrain multiplier other than Kriegsspiel's, any
  pre-gunpowder time to change formation, any duration for a bout of hand-to-hand fighting.
- Any number for what a second weapon costs in fatigue or speed (T7). That trade is Jordan's design and has
  no historical magnitude filed anywhere in the tree.
- Command delay as a number. E3–E5 establish that orders were few, coarse, slow and sometimes ignored.
- Anything from the *Strategikon*, Leo's *Tactica*, Vegetius's own text, Delbrück, Oman, Hanson, Goldsworthy,
  Engels or a drill regulation at first hand.
- The `[S]` rows (M2, M3, M5, H4) are leads. M3 and M2 are used in the adjudication only as order-of-magnitude
  checks on ratios (horse to foot), never as values.

## What it is for

The adjudication rows on movement and behaviour in
`proposals/2026-11-12-subsystem-audit-suite/audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` and the tables in
`proposals/26_MASS_BATTLE_movement_and_fatigue_as_data.md` and `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`.
