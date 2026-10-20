Coded = a row exists in engine/season/verb_table.yaml today. It does not mean every effect is built. Proposed (planned) = a workplan position with no row yet; Proposed (new) = the v2 synthesis adds it.
Source: proposals/2026-10-16-verbs-03-standards-roster-and-reconciliation.md (section III.3 roster, III.4 suites, III.5 rulings) and the lane sections 2026-10-16-verbs-09 to -18 (justifications from each lane's sections 3.2 to 3.4). The roster governs where a lane differs.
"Folded in" names have no row of their own. "Parked" names wait on a trigger the lane names.

## PC — personal combat

### Attack — one body contest, the only way a person harms or takes another

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `fight` | Runs the body contest. Felled writes the subject's body, existence and tenures plus a death Event; Wounded writes body; Untouched writes nothing. Rebuilt to write both parties. | Coded, to rebuild: writes both parties, adds Event payload | Floor act: attack a person. Without it no person can harm another, and the combat module has no way into the world. |
| `assassinate` | Runs the same contest with aim death (yields refused), a held cover and first move; witnesses are denied the actor's name by the cover's degree. | Proposed (new) | Floor act (Republic of Rome, CK3 Murder scheme). Otherwise a killing whose author the world cannot name is inexpressible, and treachery cannot be priced apart from open attack. |
| `capture` | Runs the same contest with aim alive; a felled or yielded subject is taken into custody (`person.captured`, kind name assumed). | Proposed (new) | Floor act (CK3 imprison, Mount & Blade prisoners). Without it violence can only harm; field capture, kidnap, ransom and rescue lose their producer. |

Folded in (no row of their own): ambush, shoot.

### Duel — a fight offered, answered and bound by terms

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `challenge` | Mints a `challenge` Record (terms, stakes, who it is for) held by the challenger; lapses unanswered before witnesses. Today it only emits `challenge.issued`. | Coded, to rebuild: mints a challenge Record | Floor act: challenge to a duel (Three Kingdoms duels, wager of battle). Without it a fight cannot be offered and refused before witnesses; honour-bound violence dies. |
| `accept` | Requires a live challenge naming the actor, closes it, fights under its terms, writes both parties' bodies and a duel Event so witnesses tell it from assault. | Coded, to rebuild: requires a held challenge | A consenting duel must be priced differently from an assault by the chooser and every witness. A key on fight's effect, not a second mechanism; name is strained. |

Folded in (no row of their own): champion.

### Protection and rescue — standing by a person, freeing a captive

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `guard` | Writes a protective edge (a `guard` tenure) from guard to ward and `guard.taken`; the guard joins the fight when his ward is attacked. Needs a new tenure kind. | Proposed (new) | Floor act: protect another person (CK3 bodyguard). Without it protection exists only as a seat's service; a seatless friend cannot be defended. |
| `rescue` | Closes a live detention by force against the custodian's guards, moves the prisoner out with the rescuer; `prisoner.freed`. The case Record and any ban stay. | Proposed (new) | Floor act: rescue a captive (Mount & Blade). Otherwise a prisoner leaves only by his seat's act; fight-then-travel is a composition, and a dead gaoler leaves the detention running. |

## MB — mass battle (the force and the field)

### Raising and keeping the force — soldiers from the land, kept or sent home

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `levy` | A settlement act: moves recruits into raw troops in the settlement's store and sets the local cohort's stance toward the seat's faction; `levy.raised`. | Proposed (new) | Floor act: raise men by obligation (feudal levy, CK3). Without it no army exists at realistic scale; the stance row carries the consent cost. |
| `muster` | A settlement act: moves troop kinds from one settlement to another the faction holds; `army.mustered`, seen by witnesses. | Proposed (new) | Floor act: assemble and garrison. Without it an army is only the levy of the town its general stands in, and a threatened town cannot be garrisoned. |
| `drill` | A settlement act: raises troops one grade on the same settlement, capped below the top grade; `troops.drilled`. | Proposed (new) | Floor act: drill men (Swiss militia). Without it experience has no producer short of the field; a seat can buy quality with time instead of blood. |
| `disband` | A settlement act: returns troops of a grade to the recruit pool, up to the pool's ceiling; grade is lost; `army.disbanded`. | Proposed (new) | Floor act: disband (raise, fight, disband). Without it a levy is a food sink whose only ends are hunger or death. |

Folded in (no row of their own): conscript and recruit-for-coin (a terms parameter of `levy`, R-01), garrison.

### Ordering the force — the standing order of battle

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `marshal` | A settlement act: writes the `order_of_battle` Record that the field reads whenever the force fights, attacking or defending; `army.marshalled`. | Proposed (new) | Floor act: arrange the army. Without it the defender, who does not march, has no chooser, and the reserve commit stays a constant. |

Folded in (no row of their own): rally, pursue, retreat, withstand, the reserve and its release, formation and who leads which subunits (MB lane places these under `marshal`; section III.4 lists them under `march`).

### The campaign — marching, feeding the force, living off the land

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `march` | Moves the force onto a place with its posture, carries its troop stocks, reads the order; writes stocks and the garrison's condition. | Coded, to rebuild: posture, carries force, reads order | The only act that contests ground. Most territory changed hands through siege, not field battle (PW:80), so a besieging posture is needed. |
| `supply` | Moves stores from a settlement in the seat's purview into the force's own stores; `force.supplied`. | Proposed (new) | Floor act: supply a force (supply lines lift sieges). Without it a force away from home lives only by foraging. |
| `forage` | Moves stores from the occupied settlement into the force's stores; the residents' larder falls; `stores.foraged`. | Proposed (new) | Floor act: live off the land (Attila raiding stance). Without it nothing carries the land's food away or strips a district to deny it. |

Folded in (no row of their own): besiege, storm (postures of `march`); provision, equip (into `supply`); sack (into `forage`).
Parked: reconnoitre, the MB half of ambush.

### The place given up — a holder yields a settlement on terms

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `surrender` | The holder yields a place under siege or occupation: the hold passes to the besieger, defending stocks stand down, sack is barred; `place.surrendered`. | Proposed (new) | Floor act: surrender on terms (most sieges ended in negotiated surrender). Without it a siege ends only by storm or starvation. |

## SC — social contest

### Telling — passing on what one holds

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `tell` | Contested against the hearer's standing; the told claim is deposited in the hearer's ledger with the teller on its chain; `news.told`, `confidence.broken`. | Coded | Floor act: inform and spread news (Crusader Kings secrets). The only act that moves an unwritten claim, a rumour or confidence, from one person to another. |

Folded in (no row of their own): testify, confess, confide, warn, confront, praise, flatter, insult, counsel.
Parked: lie.

### Persuasion — one person changes what another wants

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `persuade` | Contested; moves the hearer's pursuits (`pursuit.moved`), by reason or by appeal. Renamed from the planned `argue`. | Proposed (planned) | Floor act: persuade (Duel of Wits, Sway). Pursuits have no writer otherwise, so nobody can talk anybody round; the convert and the turned envoy die. |

Parked: preach.

### Declaration — putting a proposition on the record

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `utter` | Mints an immutable Proposition with a mood (ought, holds, threat and so on) and the declarer's hold. | Coded | The only creator of a Proposition, which `commit` requires. Without it there is no motion, vote or cause to swear to. Rename still open (R-06). |

Folded in (no row of their own): propose, allege, threaten.

### Binding oneself — a person ties himself to a Proposition

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `commit` | Opens a `commit` tenure binding the holder to a Proposition. | Coded | Floor acts vote and swear: a vote is a member's commit to the motion, an oath a commit to a claim. Adds no row; FA and NP share it. |

Folded in (no row of their own): vote, swear.

### Petition and complaint — the seatless person's upward channel

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `petition` | Mints a `petition` Record held by the petitioner, addressed to a person and from a place. | Coded | Floor act: petition the ruler (Royal Audience). The only act by which a person with no seat asks anything of a seat. |
| `lodge` | Re-winds a held petition's stages and appends a docket item naming it. Renamed from `carry`. | Coded, to rebuild: renamed from carry | Without it only a seat can docket a matter; giving a petition to the docket fails, since giving needs a person present. "Carried" reads as adopted. |

Folded in (no row of their own): accuse (a petition naming the accused).

### The sitting — who sets it, what is said, who decides

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `convene` | Writes the sitting's date and the convening condition. | Coded | Floor act: hold a sitting; the venue is the engine. Narrowed: dates fire vacant today, so nothing yet depends on it. |
| `open_case` | A seat with the determine remit opens a case file and a docket item on its own motion. | Coded | The seat's own-motion route (the inquisitio) and the interval between charge and judgment. Cut it and a seat cannot bring a case itself. |
| `speak` | Planned: contested on "a matter" at a docketed sitting, moving its issue rung. Writes nothing today. | Coded, to rebuild: contested, moves the issue rung | Floor act: plead a case before a court. Kept though it writes nothing today, because pleading is floor and the sitting step builds it contested. |
| `determine` | Opens the docketed row's disposal tenure (obligation, detention or ban) on a person, by bench and quorum. | Coded, to rebuild: adds a Record disposal | Floor act: judge and sentence. The only writer of a disposal by a bench; cut it and no court binds anyone. |

Folded in (no row of their own): adjourn (into `convene`); plead, refute, concede, object, define (into `speak`); arbitrate (into `determine`).
Parked: negotiate, mediate, filibuster.

### Questioning under custody — no suite in the SC lane; placed by R-07

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `interrogate` | Questioning of a person in custody, contested against his resistance; `confession.made`. | Proposed (planned) | Floor act: interrogate a person held (Disco Elysium pressing). Not a fold of `interview`: it needs custody and a contest, which inquiry may not carry. |

## FI — fieldwork and inquiry

### The scene — what happened where the actor stands

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `examine` | Reads the log at the place where the actor stands and deposits `seen` claims of earlier Events in his own ledger; refuses with `inquiry.refused`. | Coded, to rebuild: binds the place; writes seen claims | Floor act: search a place. Without it nobody can learn what happened before he arrived; the only source of a doer's name for a charge besides an eyewitness. |

Folded in (no row of their own): search, track.

### The record — reading documents without holding them

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `research` | Reads a Record the actor consults, held or not, and deposits its content as a claim; tells a forgery from a true one. | Coded, to rebuild: consult deposit, forgery read | Without it a forgery can never be found out and `forge` becomes a dominant act; a document could be learned only by taking it. |

Parked: decipher.

### Watching — keeping a place under watch

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `watch` | Keeps a place under watch for the season; the true doer of covered acts is rolled against the cover's grade; the watcher is seen watching. | Coded, to rebuild: renamed from surveil; pierces covers | Floor act: observe. Without it nothing pierces a cover but the coverer's own failure. Plain word, and no longer one letter from survey. |

Parked: shadow, eavesdrop, intercept.

### Questioning — asking what a person knows

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `interview` | Asks a person about a matter; his claims on it are deposited as `told` claims, and the question is deposited with him. | Coded, to rebuild: counterparty clause, told yield | Floor act: question a person (Pentiment, Disco Elysium). Without it one learns what another knows only by waiting for him to tell. |

### Reasoning — working out who did it

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `reconstruct` | Deposits a deed claim naming the best-supported doer from the actor's own ledger; on failure it names another candidate. | Coded, to rebuild: yields a deed claim from candidates | Without it observations never become an accusation, and the honest mistake (the Foscarini case) has no home. The lane's strongest hook with no player. |

### The commissioned picture — a written account of a power or place

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `survey` | Mints a faction sheet (or a place sheet) Record into the surveyor's hold and its content into his ledger. | Coded, to rebuild: adds place sheet and presence | Floor act: scout or survey a power. Without it the faction-scale picture has no in-world source: a document that can be wrong, burned or handed on. |

Folded in (no row of their own): audit, census, scout.

### Cover — hiding who one is

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `conceal` | Mints a `cover` Record naming the actor and carrying its grade, so his acts are put down to an alias. | Proposed (planned) | Floor act: conceal oneself (Riskbreaker Identity, CK3 secrets). Nine other verdicts lose their read without it; the deniable act dies. |
| `infiltrate` | Opens a duty edge to a seat's service while a live cover stands; the act is put down to the alias. Its own effect, to be specified before building. | Proposed (new) | Floor act: infiltrate (planting an agent, double agent). Otherwise the agent in a rival's service is two steps the chooser never joins. |

Folded in (no row of their own): disguise.

### Documents made, falsified and burned

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `forge` | Mints a false sheet in the forger's hold and writes its forgery quality; shares the honest twin's Event kind so witnesses cannot tell. | Coded, to rebuild: writes forgery quality, shared kind | Floor act: forge a document (CK3 fabricate claim). Without it a document cannot be falsified and the forgery reader has nothing to find. |
| `create_record` | Marks a Record as existing. | Coded | The lane gives only that FI owns it (R-14) and that its CRUD name is kept (no retrofit). |
| `destroy_record` | Marks a Record as no longer existing. | Coded | Without it evidence is permanent and the burn that closes a conspiracy dies. It forms for nobody yet, until record-holding eligibility is typed. |

### Inducement — paying a person to act

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `bribe` | Moves stores from payer to payee and deposits the terms of the inducement to the two of them only. Needs a payee-side reader. | Proposed (new) | Floor act: bribe (Shadows of Doubt, Assassin's Creed II). Without it an official cannot be bought. Kept apart from gifts so creeds and witnesses price them differently. |

Parked: suborn.

## TW — threadwork

### Perceive — reading the thread layer

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `thread_read` | Rolls the Thread-Read pool through the Leap stage; deposits a claim in the actor's own ledger; forms a knot; costs Coherence at Relational and above. | Coded, to rebuild: gate, cost and resolve write | Floor act: perceive the magical (Ars Magica Intellego). Without it nobody perceives the substrate and Thread Sensitivity gates nothing. |

Folded in (no row of their own): trace, diagnose.

### Cohere — taking on a held shape

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `weave` | Takes on a held load: a `weave` tenure on the target while held, a Coherence cost by scale, and a knot. Live weaves feed the Calamity's strain. | Proposed (new) | Floor act: make or bind (Creo, Rego). The only chosen act that takes on a held load; without it person-made strain and the manipulative branch of canon die. |

Parked: pull (with past-pulling).

### Preclude and unmake — freezing or ending a target

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `lock` | The target cannot become: a Site's condition is refused change until mended. Coherence cost with surcharge; a knot; a `lock` tenure read by the write gate. | Proposed (new) | Floor act: hold or fix (Rego, Skyrim Paralyze). The one act that freezes a place; its cost regime differs from `weave`, so it is not a fold. |
| `dissolve` | Ends the target: a Site's condition driven to the floor, or a held shape's tenure closed; leaves a residue mark; Coherence cost with surcharge; a knot. | Proposed (new) | Floor act: destroy or unmake (Perdo, Entropy). Without it there is no destructive operation and no way to unmake a lock except by mending. |

### Mending — repairing what magic broke

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `mend` | Repairs by target: closes a lock or another's weave, raises a lattice Site, moves a person's resting point or body; costs no Coherence; forms a knot. | Proposed (new) | Floor act: heal or repair what magic broke. Without it every Locked Zone is permanent and nothing chosen holds back the Calamity. |

Folded in (no row of their own): heal.

### Protect — a standing defence against hostile workings

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `ward` | Writes a `ward` tenure on a person or Site for a season; hostile workings aimed at it resolve in an opposed roll against the warder; forms a knot. | Proposed (new) | Floor act: protect or counter (Parma Magica). Without it a party not acting has no protection. Built when the first hostile operation executes. |

### Bond — a chosen thread bond

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `knot` | Opens the actor's directed `knot` tenure to a partner, with a strain gauge; carries remote reads and drift. | Coded, to rebuild: split from tie / knot row | Floor act: bond through magic (familiar's bond). Without it every knot is involuntary and the chosen bond dies. Split from `tie`, a social edge. |

## GV — settlements and governance

### Seats — filling, emptying and making offices

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `confer` | Opens a seat hold under the office's conferral basis (since, term); `tenure.opened`. | Coded | The only act that fills a seat; canon's seat-holders exist only if seats change hands. Appoint, designate and elect are bases of it. |
| `revoke` | Closes another's seat hold under a revocation basis; `tenure.closed`. | Coded | Floor act: dismiss (CK3 Revoke Title). Without it seats are only resigned or never emptied. It has not yet executed in a run. |
| `establish` | Founds an office with its remit acts; `office.established`. | Coded | Floor act: make an office (CK3 create title). Seats must exist before they can be filled. |
| `succeed` | The heir opens the vacant throne's hold through the inheritance basis. | Coded, to rebuild: actor becomes the heir | Floor act: succession (CK3 heir). Designation is only a title; the heir must claim the throne (RS-27), and `confer` is barred from that basis. |
| `release` | The holder closes his own edge; `tenure.closed`. | Coded | Floor act: resign or abdicate (CK3 Abdicate). The generic closer of one's own edge, so no per-kind antonym grows. |

Folded in (no row of their own): appoint, designate, elect, steward, rotate (into `confer`); dismiss (`revoke`); amend (`establish`); resign, abdicate, abandon, and SC's deny and withdraw (`release`).
Parked: depose, abolish.

### Writs, orders and the answer — demand and response

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `issue` | Mints a dispensation Record (a writ) held by the issuer, to one executor; `dispensation.issued`. | Coded | The written writ: the warrants that `seize` and `arrest` read. Not a fold of `order`, since an order mints no Record to bind. |
| `order` | A documentless order to a named person; `order.given`. Needs a reader before the person acts on it. | Coded, to rebuild: renamed from dispatch | Order with no document; five heads act through the shipped `dispatch`. Until Jordan rules (R-05), the shipped name stands. |
| `comply` | Writes nothing; emits `compliance.given`; the performance is the executor's own act. | Coded | The answer by doing. The demand-and-answer cycle (province demands, governor answers) needs an answer, the place where a ruled person chooses. |
| `evade` | Covert non-performance; `compliance.evaded` reaches the issuer only on detection; cuts a tax take at MATTER. | Coded, to rebuild: split from evade / defy row | Covert versus open refusal is the strategic fork. Split from `comply` because its value cell is opposite in sign. |
| `defy` | Open refusal; `compliance.refused` goes to the issuing seat at once; withholds a tax take for the season. | Coded, to rebuild: split from evade / defy row | Open refusal feeds rebellion and grudges; the Scott mechanism needs repeated refusal. Kept apart from `evade` because the issuer must learn at once. |
| `construe` | The receiver's reading of a writ; writes nothing. | Coded | Third answer to a writ beside `comply` and `evade` / `defy`. Moved from SC (R-12); interpreting terms is ruled neutral. |

Folded in (no row of their own): warrant, commission (into `issue`).

### Public law — the edict and its publication

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `proclaim` | Mints an `edict` Record (a notice) published to the residents of a place; `edict.proclaimed`. | Proposed (new) | Without it a seat cannot tell its purview anything, and a decree must land place by place. `issue` cannot carry it: a writ must name a person. |

Folded in (no row of their own): decree.
Parked: charter.

### Treasury and dearth — taking and cutting

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `tax` | Mints an `edict` of kind tax; each season the settlement's yield is diverted into the seat's treasury; `tax.levied`, `tax.collected`, `tax.withheld`. | Proposed (new) | Floor act: tax (Stronghold rate, Levi). Without it no extraction decision exists. `requisition` takes stock once; `tax` is a standing levy on yield. |
| `requisition` | Moves a settlement's stock into the seat's treasury now, once; `requisition.taken`. | Coded | Floor act: requisition in kind (Book of Orders). The one-off twin of `tax`; kept as shipped. |
| `ration` | Mints an `edict` of kind ration; the draw per mouth at the place is cut; `ration.set`. | Proposed (new) | Floor act: ration (Stronghold, Frostpunk food laws). Without it dearth has one answer, relief, and the hard choice is gone. Needs a draw-policy ruling first. |

Folded in (no row of their own): relieve (into EC `transfer`).
Parked: assess.

### Custody and justice — taking and freeing a person

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `arrest` | Opens a detention (prisoner to the warrant's seat), contested; `arrest.made` or `arrest.resisted`. | Proposed (planned) | Floor act: arrest (CK3 imprison). Without it custody opens only after a trial, never before; `seize` cannot take a person. |
| `pardon` | Closes another's detention or ban under the determination basis; `detention.ended` or `ban.ended`. | Proposed (planned) | Without it a tribunal's disposal is a ratchet. The name is a defect (R-17: a pardon is remission by authority); candidate plain word `free`. |

### Places and works — founding, building, ending

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `found` | Mints a settlement (a Rung) under its works' place, plus the founder's hold; `rung.founded`. | Coded | Floor act: found a settlement (Civilization Found City). Without it no new holding is made; it opens a hold, which `build` does not. |
| `build` | Mints a Site at condition 0, paying the works' cost; `site.built`. | Coded, to rebuild: plan accepted inside the act | Floor acts: build, fortify, improve. Without it the world only decays; fortify and improve are contents of it. |
| `raze` | Planned: ends a settlement or a Site; licensed by occupation; must re-house its persons. | Proposed (planned) | Floor act: raze (Civilization). Without it `found` and `build` have no inverse and conquest cannot burn a town. |

Folded in (no row of their own): fortify, improve (into `build`).
Parked: patrol.

## FA — faction actions

### Covenant — binding agreements between seats

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `covenant` | A seat's offer or seal of terms: writes a Proposition, a dispensation Record and the party's own edge; in force while both parties' edges are live. | Proposed (planned) | Floor acts: treaty, alliance, truce, tribute (EU4 diplomacy). Without it every inter-seat agreement dies; `utter` plus `commit` is only a private promise. |

Folded in (no row of their own): treaty, peace, alliance, truce, tribute, vassalage, league, ransom terms, cession terms.
Parked: hostage, marriage alliance.

### Declaration — a seat's public stance toward another faction

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `declare` | A seat's public stance toward another faction: writes a Proposition (mood war first) and the declarer's own edge; a public binding decision. | Proposed (new) | Floor act: declare war. Without it `at_war` has no lawful producer. Differs from `utter` in actor and stratum: a private war-mood `utter` must not make a war. |

Folded in (no row of their own): war (built first).
Parked: embargo, condemnation, sanction.

### Recruitment — taking persons into a seat's service

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `recruit` | The recruiter's contested offer of service; on a win it writes the recruit's duty edge (with a term) to the seat. | Proposed (new) | Floor act: recruit persons (RoTK Recruit, CK3 Invite to Court). No seat can start the joiner's `pledge` otherwise; the merge into `tell` was rejected. |

Folded in (no row of their own): enlist, retain.
Parked: turn.

### Intrigue — a plot against a seat

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `conspire` | Draws a person into a plot against a seat: mints the plot Proposition and, on a win, opens his edge to it. | Proposed (new) | Beyond the floor, strong convention (CK3 schemes). Without it no many-person covert act exists, since `covenant` is seat-only and public. |

Folded in (no row of their own): plot, scheme, coup.

### Orders and posting — placing a person under the seat

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `assign` | Posts a named obligee to a place with a task: writes the posting on his duty edge and, for a posting elsewhere, moves his containment. | Proposed (new) | Floor act: set assignments (RoTK posting, CK3 council tasks). The shipped `dispatch` writes nothing, and five heads act through it. |

Folded in (no row of their own): post, envoy, garrison a man.

### Territory — taking and holding places

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `seize` | Takes a Record under warrant or a settlement under occupation: one hold closed, one opened. | Coded | Floor act: hold territory. Without it occupation never changes title. |

Folded in (no row of their own): annex (from GV's lane; conquer and take are names for its settlement half).

### Covert damage — lowering a Site

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `sabotage` | Lowers a Site's condition (the mirror of repair); `site.damaged`. | Proposed (planned) | The only act that lowers a Site's condition; cheap asymmetric harm to deny a rival's muster or works (RoTK VIII schemes). |

## EC — economy, trade and craft

### Production — labour at a producing place

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `work` | Rebuilt: the worker's labour is staged on a Site for the season and read by the yield step (labour tally to yield to stores). | Coded, to rebuild: labour staged, read by yield | Floor act: produce (Banished workers). Without it no person act touches what a place produces; "fewer hands, less food" has no carrier. |

Folded in (no row of their own): cultivate, mine, fish, hunt.

### Making — converting goods at a workshop

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `craft` | Converts goods at a workshop: input stores down, the chosen product up, in the settlement's stores; `goods.made`. | Proposed (new) | Floor act: make (Dwarf Fortress workshops, Anno chains). Without it nothing converts goods: no arms producer, so a levy cannot be equipped. |

Folded in (no row of their own): mint.

### Repair — raising a worn Site

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `restore` | Raises a worn Site that no works names, up to full scale; `site.restored`. | Coded, to rebuild: narrowed to Site fabric only | Floor act: repair (Civilization worker repair). Without it wear is answered only by a new works with a cost; cheap repair dies. Medium confidence. |

### Moving stores — consensual movement of matter

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `transfer` | Moves stores between two settlements; through a seat it also renews obligation terms; `transfer.made`. | Coded | The one conserving mover of matter by consent. Without it there is no upkeep, relief or delivery; `give` moves holds, `requisition` only into a treasury. |

Folded in (no row of their own): pay, repay, haul, relieve, tribute.
Parked: smuggle, toll, hoard.

### Trade — swapping stores at a price

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `exchange` | Swaps two settlements' stores at a price read from the settlement's stock (four store writes); declined if the price is not met. | Coded, to rebuild: price operand, builds the effect | Floor act: trade (Patrician, Mount & Blade). Without it a settlement can be given to or taken from but never buy; two transfers cannot make an atomic trade. |

Folded in (no row of their own): trade, buy, sell, barter, bargain.

### Hiring — paid service

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `hire` | Opens the hireling's service edge (since, term) and pays the first wage from the employer's settlement to his. | Proposed (new) | Floor act: hire labour (Mount & Blade tavern, CK3 mercenaries). Without it wealth cannot become labour or soldiers by the payer's choice; `pledge` is the joiner's act. |

### Credit — advancing goods against a debt

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `borrow` | Moves an advance from the creditor's settlement to the debtor's and mints a `debt` Record held by the creditor; `debt.made`. | Proposed (new) | Floor act: lend and borrow (CK3 loans, EU4). Without it no seat can spend ahead of its yield; insolvency is only a refusal. |
| `lend` | As `borrow`, with the creditor acting. | Proposed (new) | The creditor's voice of the same act. A fold needs the same actor, so two rows; one effect owner, so the arithmetic lives once. |

## WT — world, travel and survival

### The journey — moving oneself between places

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `travel` | Closes and opens the traveller's containment tenure, appends to his travel leg; `travel.moved`, `.blocked`, `.ended`. Priced by route once a route model exists. | Coded, to rebuild: renamed from move; priced by route | Floor act: travel from place to place. Without it no person can change where he is. Renamed to match its own Events. |

Folded in (no row of their own): navigate, ride, sail.
Parked: camp (with encamp), evacuate.

### Resettlement — changing one's home

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `migrate` | Moves a person's containment and re-homes his residence, throttled by the settlement's capacity; `residence.changed`. | Coded | Floor act: move house (Dwarf Fortress migrants). The only act that re-homes residence; RR-2 ruled it a verb persons take. |

### Discovery — finding what the map holds

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `explore` | Presence in a territory reveals an authored point of interest (a Site or Record) to the explorer's ledger; `site.discovered`. Needs authored POIs. | Proposed (new) | Floor act: explore and discover (Kingmaker hexes). The one act that makes the map grow; secrets lead to FI, remnants to threadwork. |

## NP — NPC life and persons

### Care — raising a body

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `tend` | Raises `Person.body`; `body.tended`. | Proposed (planned) | Floor act: tend the wounded (Pendragon First Aid, CK3 physician). The only act that raises a body; otherwise every wound is permanent. |

Folded in (no row of their own): heal, recover.

### Formation — developing a person

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `train` | Writes `Person.capability` for self or a pupil; `capability.raised`. | Proposed (planned) | Floor act: train a person (CK3 education). The only development of a person. Inert until combat and choice read capability. |

Folded in (no row of their own): study, teach.

### Grievance — ending one's own grudge

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `forgive` | Removes the actor's own negative `Person.stance` rows toward the subject; `stance.moved`. | Proposed (planned) | Floor act: end one's own grudge. The only closer of a stance row; a grudge nobody can end is escalation with no release valve. |

### Bonds — a typed regard edge between persons

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `tie` | Opens a directed `tie` tenure from the actor to a partner; `bond.formed`. Declined until its readers exist. | Coded, to rebuild: split from tie / knot; partner operand | Floor act: form a personal bond (RoTK oaths, CK3 friend). Kept only if a reader gates on tie type; else it duplicates stance and should be cut. |

### Marriage and kin

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `marry` | Opens two directed `kin` tenures (content spouse), one per spouse, in one write; `marriage.made`. Needs a kin tenure kind. | Proposed (new) | Floor act: marry (CK3 arrange marriage). Binds persons across a change of faction, which a `covenant` cannot; the lane calls it the strongest world-hook generator among designed verbs. |

Folded in (no row of their own): wed.
Parked: court, betroth, rear.

### Service and allegiance — binding oneself, changing sides

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `pledge` | Opens the joiner's duty tenure to a seat (since, term); `duty.taken`. | Coded, to rebuild: renamed from oblige | Floor act: pledge service or fealty (CK3 vassals). English "oblige" runs the other way, so the self-binding act is named `pledge`. |
| `defect` | Closes the actor's commitment or duty to faction A and opens one to B in one write; `allegiance.changed`. | Proposed (new) | Floor act: change sides (RoTK, Bannerlord). Atomic, so the turncoat is never nobody's; the Event is what witnesses judge as treachery. Medium confidence. |

Folded in (no row of their own): swear (into `pledge`).
Parked: consecrate (with crown; Devotion suite, no verb row).

### Gifts — title moving by consent

| verb | effect on the game world | coded or proposed | justification |
|---|---|---|---|
| `give` | Closes the giver's hold and opens the receiver's in one effect; `record.given`. | Coded, to rebuild: widened to settlements | Floor act: give a gift or holding (CK3 Send Gift). The only consensual route by which title moves; cession of a settlement is the same act. |

Folded in (no row of their own): cede.
