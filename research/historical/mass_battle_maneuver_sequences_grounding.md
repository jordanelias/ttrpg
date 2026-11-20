# Grounding note: manoeuvre sequences, step by step, from battles whose pages were read

## Status: FILED — reference, tier 3 (`research/00_INDEX.md` §1) · not canon (CLAUDE.md §0.05) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: MB (historical adjudication lane of `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

Sibling of `mass_battle_casualties_and_results_grounding.md` (**its tier table and source keys apply**) and
of `mass_battle_movement_and_behaviour_grounding.md`. This note sets out, as numbered phases, the manoeuvres
the game needs. It is text, not drawings: no period drill diagram was reached (see "not established").

**How to read a sequence.** Each step cites the page it came from. A step marked `[reading]` is this lane's
connective inference between two cited steps and carries no weight of its own. After each sequence, **"What it
asks of a battle engine"** is this lane's reading of the sequence as inputs, states and draws; it is design
argument, not history.

**Relation to the tree's own sequences.** `research/pre_firearms_formations/02_classical.md:44-58` (Gaugamela),
`03_early_medieval.md:196-218` (Hastings), `04_high_medieval.md:96-130` (Hattin, Arsuf), `:244-262` (Liegnitz,
Mohi), `05_late_med_renaissance_europe.md:162-222` (Crécy, Poitiers, Agincourt),
`10_battle_phase_choreography.md` (the eight-phase frame) and `12_moment_by_moment_dynamic_spacing.md` (nine
battles) are longer and are **memory tier** by their own statement (`12_…:936-940`;
`13_verification_corrections.md:5`, `:275`). File 13 records two factual errors in file 12 that were never
edited back (Panipat sally gaps; Lodi's elephants, `13_…:133-154`) and four under- or mis-statements (Cannae's
frontage, Pharsalus's fourth line, Agincourt's funnel direction, Marignano's duration, `13_…:18-117`). The
sequences below are shorter and each step was page-read on 2026-11-12. Where the two disagree, the entry says so.

## Additional sources

| key | source | tier · read |
|---|---|---|
| W-BAN | `https://en.wikipedia.org/wiki/Battle_of_Bannockburn` (citing Barrow, Reese, Scott, Mackenzie, the *Scalacronica*) | `[T]` (part: first 100,000 of 103,248 characters), 2026-11-12 |
| W-CRE | `https://en.wikipedia.org/wiki/Battle_of_Cr%C3%A9cy` (citing Ayton, Rogers, Sumption, DeVries, Prestwich) | `[T]` (part: first 100,000 of 143,612) |
| W-GAU | `https://en.wikipedia.org/wiki/Battle_of_Gaugamela` (citing Arrian, Curtius, Diodorus, Green) | `[T]` (part: first 100,000 of 138,151) |
| W-SIEGE | `https://en.wikipedia.org/wiki/Siege` | `[T]` (part: first 100,000 of 223,180; several sections tagged as lacking citations) |

---

## 1. Approach and deployment

1. The army arrives by march and the two sides see each other at a distance; a battle is not automatic. At
   Crécy the French "sighted the English around noon" after "a march of about 12 miles"; a council "advised
   attacking the next day". `[T]` W-CRE
2. The side that chose its ground deploys first and rests: the English "had been in position since dawn, so
   [were] rested and fed"; they "dug pits in front of the position" and circled the baggage at the rear. `[T]` W-CRE
3. Deployment is by lines and by wings: heavy foot in the centre in two or three lines, horse on the wings,
   light troops in front (Pharsalus: both sides "formed the traditional three lines"; Zama: light infantry
   and elephants forward, three lines, cavalry on both flanks; Hastings: "archers formed the front, with
   spearmen behind, and the cavalry … held in reserve"). `[T]` W-PHA, W-ZAM, W-HAS
4. Depth and width are a commander's choice made now, against what he sees: Pompey ten deep to hold; Caesar
   six deep, then "further thinned his third line in order to form a fourth line on his right" against the
   massed cavalry he could see opposite; the Romans at Cannae "extra depth rather than breadth". `[T]` W-PHA, W-CAN
5. Standing orders are given before contact: Caesar "ordered the third line not to charge until told to";
   Pompey "ordered his men not to charge, but to wait"; Richard fixed the signal for the charge in advance
   ("six clear trumpet blasts"). `[T]` W-PHA, W-ARS
6. The sides may then stand for hours: at Agincourt about three hours, until Henry moved. `[T]` W-AGI

**What it asks of a battle engine.** A deployment made per unit (post, depth, width) before the first draw;
standing orders with a trigger; the choice to offer, accept or decline; the state each side arrives in (tired
from a march, or rested) as an input. A commander sees the enemy's deployment before fixing his own only if he
deploys second.

## 2. Changing formation on the march and in the presence of the enemy

1. Bodies move in column and fight in line; the change is made as the enemy nears. `[T]` W-NAP
2. The change takes time during which the body is neither: Napoleonic drill figures at second hand are 30 to
   100 seconds for a battalion to form square, "longer" in the field. `[T]` BAL
3. Caught mid-change, the body is beaten: "any unit that tried to change formation in the face of enemy fire
   was in trouble"; squares "formed too late" were ridden down. `[T]` BAL, W-SQ
4. A whole line changes shape only in a pause it has earned: Scipio at Zama recalled his first line by bugle,
   and "re-form[ed] into a single extended line after a prolonged pause". `[T]` W-ZAM
5. The English at Agincourt moved a prepared position forward: the stakes "had to be pulled out of the ground,
   carried to the army's new position, and reinstalled", before the enemy came on. `[T]` W-AGI

**What it asks.** Formation change as an act with a duration in which the body fights at a disadvantage (not
an instant relabelling), cheaper for drilled troops, and unsafe within reach of the enemy. Pre-gunpowder
durations are **not established**; the game sets its own and says so.

## 3. Cavalry charging steady pikes or spears (Courtrai 1302; Bannockburn 1314)

1. The foot choose ground that breaks the charge's order: "ditches and streams" at Courtrai; woodland and the
   burn at Bannockburn. `[T]` W-GS, W-BAN
2. They stand deep, weapons outward: "deeply stacked lines forming a square … with goedendags and pikes
   pointed outward". `[T]` W-GS
3. Missile troops skirmish first and are pulled back to clear the way: Artois "recalled his foot soldiers 'to
   clear the way for 2,300 heavy cavalry'". `[T]` W-GS
4. The horse cross the obstacle and lose order ("a few fell from their steeds"; some of their own foot
   trampled). `[T]` W-GS
5. The line does not run, and the charge stops at it: "the Flemish infantry wall did not flinch as expected
   and a part of the French cavalry hesitated"; most knights "could not break the pike line" and were "knocked
   from their horses and killed". `[T]` W-GS
6. The few who break in meet a held reserve: they "ran right into the Flemish reserves; they were swiftly
   routed and cut down". `[T]` W-GS
7. The attacker's own reserve fails to come up (the rearguard "turned back to protect their vulnerable baggage
   train"), the commander is surrounded and killed, and the rest flee. `[T]` W-GS
8. The foot go over to the attack and pursue on foot ("over 10 km"); at Bannockburn the schiltrons advance
   as "offensive units" and grind the horse back against the burn until it "broke ranks". `[T]` W-GS, W-BAN
9. The counter is missile fire on the block, and its counter is a small mounted reserve: the English and Welsh
   bowmen who "tried to flank the Scots … were dispersed by Sir Robert Keith's 500 Scottish cavalry". `[T]` W-BAN

**What it asks.** The decisive draw is whether the foot stand, taken before contact, shifted by their
steadiness, their depth, the ground and their reserve; if they stand the charge is spent. A stopped horseman
is in a short-weapon fight he is badly placed for. The block is weak to missiles and needs its own screen.

## 4. Cavalry against a line of foot that is not a pike block (Hastings 1066; Arsuf 1191; Pharsalus 48 BC)

1. Missiles first, to little effect against shields and a slope: arrows "either bounced off the shields of the
   English or overshot". `[T]` W-HAS
2. Foot assault, then horse in support; neither breaks the wall. `[T]` W-HAS
3. A wing recoils or flees; part of the defending line leaves its place to chase. `[T]` W-HAS
4. The horse turn on the pursuers in the open and destroy them (see sequence 6). `[T]` W-HAS
5. Repeated over hours with a lull; the wall thins but holds until its leader falls late in the day. `[T]` W-HAS
6. The other way round, at Arsuf: the horse are **held** inside a screen of foot and crossbowmen under
   harassment until the enemy is "fully committed and their horses tiring", then loosed through gaps the foot
   open, "in echelon from rear to van". An enemy "already in close combat and too compact to avoid the charge"
   breaks. `[T]` W-ARS
7. At Pharsalus, horse that has driven off the opposing horse is met by a held reserve of foot using throwing
   spears as thrusting spears; it "panicked", and the reserve then turned the exposed infantry flank. `[T]` W-PHA

**What it asks.** A charge succeeds against foot that is disordered, committed elsewhere or made to leave its
place, and fails frontally against a formed, waiting line; holding horse back until that moment is the
commander's skill, and an unordered charge (Arsuf's Hospitallers) is a draw the commander may lose.

## 5. Archery to hand-to-hand (Agincourt 1415; Crécy 1346)

1. Missile troops are posted on the flanks or in front of dismounted heavy foot, behind an obstacle they
   brought or dug (stakes; pits). `[T]` W-AGI, W-CRE
2. An opening missile exchange is decided by rate and range and by what the shooters lack: the Genoese without
   their pavises and reserve ammunition "fired perhaps two volleys before withdrawing"; they fled back through
   their own cavalry and "many were killed by their own side". `[T]` W-CRE
3. Horse charge the archers and fail on the obstacle and the arrows; wounded horses bolt back through the
   following foot and churn the ground. `[T]` W-AGI, W-CRE
4. The enemy's foot advance under shooting and arrive tired, crowded and disordered ("scarcely lift their
   weapons"). `[T]` W-AGI
5. **The switch.** "When the archers ran out of arrows, they 'dropped their bows' and attacked with 'hatchets,
   swords, spears and the mallets they had used to drive their stakes in.'" `[T]` W-AGI
6. At Crécy the page read does **not** say the archers fought hand to hand: they shot from the flanks and
   "retriev[ed] arrows during pauses", while reserves were fed to the pressed division. `[T]` W-CRE
7. The melee is decided in the press; later lines arrive onto the same narrow ground and fail in turn; the
   last line leaves without fighting. `[T]` W-AGI

**What it asks.** The missile body's change to hand weapons is triggered by **spent ammunition** or by the
enemy being disordered within reach, costs the bow (dropped, not slung), and is worth doing only against a foe
already tired or crowded. Being *reached* while still shooting is the other case and is the charge of step 3
succeeding. The tree's reading that archers "drop bows for mallets" (`05_late_med_renaissance_europe.md:194`,
`:218`) is confirmed for Agincourt and not for Crécy.

## 6. The feigned retreat (Hastings; the Kalka 1223)

1. A body breaks contact and runs, or seems to: at Hastings "a general retreat began, blamed on the Breton
   division"; whether the first flight was a ruse is not claimed by the page. `[T]` W-HAS
2. The enemy pursues, leaving its line or its ground. `[T]` W-HAS, W-KAL
3. Over a short distance (Hastings) or a long one ("nine days", the Kalka) the pursuers string out and lose
   their order; their fastest part outruns the rest. `[T]` W-KAL
4. The runners turn, or a waiting force stands, on ground of its choosing; the pursuers' van is hit before
   their rear arrives ("the coalition rout began incredibly quickly' as the front ranks dissolved before the
   rear had arrived"). `[T]` W-KAL
5. The broken van runs back through its own following troops and disorders them (the Cumans). `[T]` W-KAL
6. Done deliberately it can be repeated: William of Poitiers "says the tactic was used twice"; some historians
   doubt it, "most historians agree". `[T]` W-HAS
7. Its cost: it "requires well-disciplined soldiers" and "undisciplined troops are likely to lose coherence
   and the rout will become genuine". Its counter: "Do not pursue an enemy who simulates flight" (Sun Tzu, as
   the page quotes). `[T]` W-FR

**What it asks.** Three draws, none certain: do the feigners keep their order while running (their
discipline); does the enemy take the bait (its commander's judgment against its troops' urge to chase, and a
standing order "do not pursue"); does the turn succeed. A failed first draw is a real rout. The tree's engine
already has the second draw (`modules/mass_battle/orchestration.py::feigned_retreat_recognized`) and no path
that reaches it (`proposals/2026-11-12-subsystem-audit-suite/proposals/16_PESSIMIST_MB_rout_has_two_exits.md`).

## 7. The flanking march and envelopment (Cannae 216 BC; Pharsalus; Zama 202 BC; Gaugamela 331 BC)

1. One part of the army is deployed to **hold without winning**: Cannae's centre of Spaniards and Gauls,
   advanced as a crescent; Parmenion's wing at Gaugamela "tasked with a holding action". `[T]` W-CAN, W-GAU
2. The mobile arm wins its own fight first: at Cannae the cavalry on one wing beat the Roman horse, and the
   other wing "kept the allied cavalry occupied" until the first came round behind it. `[T]` W-CAN
3. The holding part **gives ground in order**: "Hannibal held the weak centre in a controlled retreat, so the
   … crescent bent inward step by step"; the attacker, pushing into it, "compressed and lost cohesion as
   reserves pushed into the gaps". `[T]` W-CAN; `[D]` SA p. 6
4. The fresh bodies held on the flanks turn inward on a signal: "At this decisive point, Hannibal ordered his
   African infantry to turn inwards and advance against the Roman flanks." `[T]` W-CAN
5. The cavalry returns on the rear; this takes time ("at least an hour, and probably a lot longer"), during
   which the frontal fight must not be lost. `[D]` SA pp. 4–5; `[T]` W-CAN, W-ZAM
6. Crowding does the killing: the enveloped cannot "re-establish the 'safety distance'" and are "slaughtered
   without inflicting similar casualties in return". `[D]` SA pp. 6, 16
7. Counters seen: a held reserve against the flanking horse (Caesar's fourth line); a second line facing
   rear, and wings "echeloned back at 45 degrees" (Alexander); lanes for what cannot be stopped (Scipio's
   "broad avenues" for the elephants; the phalanx "opened lanes" for scythed chariots). `[T]` W-PHA, W-GAU, W-ZAM
8. Failure modes seen: the winning horse leaves the field (the Persian cavalry at Gaugamela "raided the camp";
   pursuit that does not return); the holding part breaks before the wings close. `[T]` W-GAU

**What it asks.** No "envelopment" order: a holding unit with an order to give ground, wing units with a held
order released by signal, horse with an order to return after winning. Each is separately a draw, and the
manoeuvre is the conjunction. The tree's rule against a "Cannae button"
(`research/pre_firearms_formations/14_methodology_audit.md:77`) is the same finding. Cannae's frontage and
depth are not stated on the page read; file 13's correction (about 1.95 km; 24 to 70 ranks) stands as that
file's own claim.

## 8. Line relief and the committed reserve (Zama; Pharsalus; Sabin)

1. The first line fights; the second stands "outside javelin range" so that it is not worn by the stand-off. `[D]` SA p. 16
2. In a lull the lines are a few yards apart, and a tired sub-unit can be passed or replaced: "it is much more
   plausible to imagine forward sub-units fighting with gaps in their line, covered at a distance by supporting
   sub-units". `[D]` SA p. 16
3. The second line either moves up "into the intervals … to fight alongside the first line or to take over
   the burden of the combat". `[D]` SA p. 16
4. Where the second line refuses the first, the first breaks around it (Zama's mercenaries). `[D]` SA p. 15; `[T]` W-ZAM
5. The last reserve is committed at the moment the enemy's line is exposed (Caesar's third line at Pharsalus
   "broke Pompey's left wing troops"). `[T]` W-PHA

**What it asks.** Relief only when not in contact (a window), by an order to the rear unit; a reserve that is
fresh because it was held out of reach, at the price of not fighting.

## 9. The fighting march and the withdrawal in order (Arsuf; the general case)

1. The column keeps a fixed order of march: horse inside, foot outside toward the enemy, missile troops
   outermost, baggage on the safe side; foot divisions "rotated to stay fresh". `[T]` W-ARS
2. The enemy harasses to make it stop or charge: "arrows at them from all sides to annoy them, and force them
   to charge". The column's task is "keeping ranks intact"; crossbowmen answer "shooting while walking
   backwards". `[T]` W-ARS
3. Pressure concentrates on the rear; the rearguard "lost cohesion". `[T]` W-ARS
4. The commander refuses to fight until the enemy has committed; a subordinate breaks ranks; the commander
   converts it. `[T]` W-ARS
5. A withdrawal in order is disengaging "while maintaining unit cohesion, discipline, and command-and-control",
   by "coordinated movement, rear-guard actions, and maintaining contact with the enemy at a controlled pace";
   it is "relatively risky … requiring discipline to keep from turning into a disorganized rout". `[T]` W-WD
6. A line may also step back facing the enemy inside a battle ("stepped back gradually while still facing the
   enemy", Polybius 2.68–9; Appian BC 4.128). `[D]` SA p. 6

**What it asks.** Withdrawal as an ordered state distinct from rout, slower than flight, still fighting to its
front, with a draw each interval on whether it holds together, harder for the unit nearest the enemy. The
tree's proposal `proposals/mass_battle_fighting_withdrawal_v1.md` is this shape.

## 10. Rout and pursuit

1. A part breaks (from the rear ranks first) and the break spreads along the line. Results note D6, D7.
2. The broken throw away what slows them. `[D]` SA p. 5
3. The victor's choice: hold his order and let them go (the Greek habit, KR p. 20), or pursue.
4. Horse and light troops pursue furthest, "into the following day"; foot pursue a few kilometres. `[T]` W-ROUT, W-GS
5. The pursuer disperses and is exposed: Richard stops after about 1.5 km and re-forms; a rearguard turns at
   the Malfosse; James d'Avesnes "was killed in the scattered pursuit". `[T]` W-ARS, W-HAS
6. The beaten side's ends, all attested: scattered and cut down (Zama's third line); a stand around the leader
   (Hastings); a rally out of reach (Celts, Helvetii, SA p. 6); a withdrawal to a camp that is then stormed or
   besieged (Pharsalus, the Kalka); drowning against an obstacle (Bannockburn).
7. Night ends it. `[T]` CL Book IV ch. XII

**What it asks.** Pursuit as the winner's decision with a price (the pursuing body is out of the battle and
disordered), a recall draw, a rally draw for the beaten that is easier for light troops and when out of reach,
and terrain behind the loser as a multiplier.

## 11. Assault on a fortified place

1. The usual course is not assault: "sieges involve surrounding the target to block provision of supplies";
   "sieges can often be decided by starvation, thirst, or disease", which "can take many months or even
   years"; the besieger "could very well be threatened with the disease and starvation intended for the
   besieged". `[T]` W-SIEGE
2. Terms are offered first: attackers "might offer generous terms to a defender who surrendered quickly";
   "the defending troops would be allowed to march away unharmed". Treachery is tried ("a well-placed bribe to
   a disgruntled gatekeeper"). `[T]` W-SIEGE
3. The means of forcing an entry, each a separate attempt: ladders ("to escalade over the defenses"), rams and
   hooks at gates or walls, a tower to "fire down upon the defenders", a mine "beneath the foundations", which
   the defenders counter-mine. `[T]` W-SIEGE
4. If a breach is stormed after terms were refused, "the defenders could expect no mercy" (stated on the page
   for the gunpowder era; for the Mongols a three-day ladder of worsening terms). `[T]` W-SIEGE
5. Durations read: Carchemish eight days; Tyre seven months. `[T]` W-SIEGE
6. **How an escalade or a breach assault proceeded step by step in the ancient and medieval periods is not
   established** by the page read (the stepwise account there is of gunpowder-era parallels).

**What it asks.** The season-scale choice (invest, offer terms, storm) is the real one; a storm is a field
fought at a heavy disadvantage on a narrow front, with a sack as its consequence. The engine's `besiege`
posture and `walls` terrain row (`04_MB_audit.md` §1.2) carry the first two; nothing here supports modelling
ladders and towers as cells.

## What this note does NOT establish

- **No period drill diagram or manual was read**: nothing from Vegetius, Asclepiodotus, the *Strategikon*,
  Leo's *Tactica*, Swiss or Landsknecht ordinances, a tercio manual or a Napoleonic regulation at first hand.
  The Roman maniple and cohort drills, phalanx file and rank changes, the cavalry wedge, the tulughma and the
  Napoleonic column-line-square transitions are therefore **not** set out as drill here; what is set out is
  what battle pages say happened.
- Hattin, Grunwald, Lepanto, Mohi and Liegnitz were not page-read by this lane; the tree's accounts of Hattin,
  Liegnitz and Mohi (`04_high_medieval.md`) remain memory tier.
- Durations of any single step, and distances, except where a cell above quotes one.
- Every sequence is from one encyclopedia page, most of them read in part. A step is a lead to the historian
  the page cites, not that historian's words.
