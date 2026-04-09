# Valoria — Named NPC Roster
## ED-358 Resolution | Date: 2026-04-08 | Status: DESIGN
## [EDITORIAL: All NPC identities, motivations, and arc trajectories flagged for user review.]

---

## Design Principle

Every named NPC except Edeyja carries a structural compromise: a conflict between personal ethics and faction loyalty, an exposure to Thread Sensitivity they cannot control, a behavioral flaw in their decision-making, or a position that makes them a spoiler target. These compromises are emergent arc triggers — they create the moments where player intervention changes outcomes.

Each NPC has a **Behavioral AI Profile** governing their autonomous decisions (BG NPC AI, GM guidance for TTRPG). The profile includes a named flaw that produces suboptimal play and creates consequences the players can exploit or mitigate.

---

## 1. Edeyja — Warden-Chief (Southernmost)

**Existing design:** designs/ttrpg/edeyja_npc.md (canonical). TS 75–80. Coherence 9.

**Compromise:** None. Edeyja is the moral anchor of the setting. Her conviction (Continuity) is uncompromised and her judgment is sound. She is the standard against which other practitioners measure themselves. Players who reach her find someone who will not bend — and that rigidity is itself a narrative force.

**Disposition toward peninsula politics:** Contempt is too strong a word. Irrelevance is closer. Edeyja has spent decades maintaining the substrate while factions argue over who gets to sit in which chair. Crown, Church, Hafenmark, Varfell — from Askeheim, they are children fighting over furniture in a house that is on fire. She does not hate them. She does not care about them. The only point at which their politics becomes real to her is when their strife produces Thread tension, knots, and frays that make her job harder — and it always does. Every war, every Heresy Investigation that disrupts a practitioner's work, every Church suppression of Thread knowledge, every intelligence operation that creates collateral Thread damage is another tear she has to mend with fewer wardens and less time. The factions are not her enemies. They are an environmental hazard.

**Behavioral AI:** Evidence-driven. Will not act on political appeals, emotional urgency, or abstract moral claims. Only responds to demonstrated Thread competence and concrete substrate data. **Flaw: None.** Edeyja's "flaw" is that she is correct and the world is dying anyway. PCs who approach her with faction goals get nothing. PCs who approach her with substrate data get her full attention. The gap between these two responses is absolute.

---

## 2. Maret Uln — Varfell Practitioner / Succession Fallback

**Existing references:** params_factions §Varfell Succession (PP-486). TS ~50. Vaynard's intelligence operative and Thread-sensitive agent.

**Historical echo:** Richard Sorge — Soviet intelligence operative in Tokyo who developed genuine sympathy for the society he was infiltrating. Sorge's dual loyalty was not performative; he genuinely cared about Japan while serving Moscow. Maret's sympathy for the Restoration Movement carries the same structural weight: it is real, it conflicts with her mission, and it will eventually force a choice.

**Compromise: Dual loyalty.** Maret is personally sympathetic to the Restoration Movement — she grew up near Einhir communities in the western fjords and considers the Forgetting a tragedy. But she serves Vaynard, whose intelligence-first approach treats RM as a tool for Varfell's political objectives. Maret must choose between Vaynard's pragmatic exploitation of RM sentiment and her own belief that the Restoration deserves genuine autonomy. If Vaynard is eliminated, Maret takes over Varfell and aligns with RM goals (PP-486) — but this alignment comes at the cost of Varfell's intelligence apparatus (VTM resets to 0).

**Ethics:** Rawlsian — veil of ignorance. She believes in equity, but she serves an intelligence faction that weaponises information asymmetry. The contradiction is structural and inescapable while Vaynard leads.

**Behavioral AI — CONFLICTED:** When Varfell and RM interests diverge, Maret hesitates. She delays actions that would harm RM by 1 season (rationalising as "gathering more intelligence"). This hesitation is exploitable — opponents who recognise the pattern can predict when Varfell will fail to act against RM activity.
**Consequence:** Varfell intelligence operations against RM-adjacent targets are consistently 1 season behind optimal timing. If Vaynard notices (Vaynard Influence vs Ob 2 at Year-End), Maret's loyalty is questioned — Varfell Stability −1.

**TS exposure:** TS ~50 means Maret perceives Thread-level phenomena during intelligence operations. She cannot unsee what she observes in RM communities — the damage the Forgetting does to cultural continuity. Each successful Tribune Inward in an RM-presence territory forces a private Belief check (Spirit TN 7 Ob 1). Failure: Maret's next action must benefit RM or be neutral. Success: proceeds as ordered.

---

## 3. Maret Vossen — Restoration Movement Leader

**Existing references:** params_factions §ED-005 (PP-286). Primary RM NPC contact.

**Historical echo:** Rosa Luxemburg — revolutionary leader whose visibility was both her political power and her death warrant. Luxemburg could not lead from hiding because the movement required a public face. Vossen occupies the same structural trap: the movement needs her visible, and visibility is what the Church targets.

**Compromise: Visibility as vulnerability.** As the named leader of a movement that the Church considers heretical, Vossen is a permanent Heresy Investigation target. Every season she operates publicly, Church gains +1 Attention Pool (AP) toward her location. She cannot lead from hiding — the movement requires visible leadership to sustain Popular Will — but visibility is what kills her.

**Ethics:** Rawlsian social contract — consistent with RM's ethical framework. Vossen genuinely believes in equity and cultural restoration. But the movement's survival sometimes requires alliances with factions (Varfell, Niflhel) whose ethics she finds repugnant. Every alliance of convenience costs RM Stability −1 (the base fractures when leadership compromises principles).

**Behavioral AI — IDEALIST:** Vossen prioritises CV reduction (cultural shift) over defensive Presence marker management. She will spend actions spreading the movement's message even when consolidation would be strategically optimal. **Consequence:** RM Presence markers are consistently spread thin. Church Heresy Investigations succeed more often because Vossen's markers are in 5 territories at 1 each rather than 3 territories at 2 each. The movement is culturally influential but institutionally fragile.

**TS:** 25 — just above the practitioner threshold but below the Forgetting resistance gate (29). She can sense Thread-touched artefacts but cannot fully resist the Forgetting when operating near the Southernmost. Her cultural knowledge is partially self-erasing — she must re-learn fragments each time she returns from T13/T15 proximity.

---

## 4. Sæmund Haelgrund — Church Inquisitor (Cardinal Justice)

**New NPC.** Reports to Cardinal Olafsson (Justice). Senior Inquisitor — leads Heresy Investigations in the field.

**Historical echo:** Robert Bellarmine — the Inquisitor who examined Galileo, privately found heliocentrism compelling, but followed institutional duty to its conclusion. Haelgrund is Bellarmine after the trial: the evidence is in, his private conclusions contradict his public role, and he continues to serve because the alternative is institutional collapse.

**Compromise: Evidence he cannot report.** Haelgrund is an effective investigator. Too effective. His investigations have uncovered evidence that Thread Sensitivity is not demonic possession or heretical corruption — it is a natural capacity that some people have. This evidence directly contradicts Church doctrine (the rendered world is all there is; claims of "threads" are heretical). Haelgrund believes in the Church's mission to protect the faithful, but he can no longer believe in its ontological claims. He continues to investigate because the alternative — admitting the Church is wrong about the nature of reality — would destroy the institution he serves.

**Ethics:** Deontological — duty to the institution. Personally, he operates with procedural integrity (does not fabricate evidence, does not torture). But his duty requires him to suppress evidence that would exonerate practitioners. The suppression is the compromise.

**Behavioral AI — PROCEDURALIST:** Haelgrund follows protocol to the letter, even when protocol produces bad outcomes. He will not cut corners, improvise, or act on intuition. **Consequence:** Heresy Investigations he leads take 1 additional season to resolve (he documents everything, cross-references everything, builds an airtight case). This gives targets time to flee, destroy evidence, or seek player intervention. But when his investigations DO resolve, they are Overwhelming — the case is unassailable.

**TS:** 12 — barely above the practitioner threshold. Haelgrund does not know he is Thread Sensitive. He attributes his "hunches" to investigative instinct. If his TS is revealed (Diagnosis by a practitioner, or accidental Leap), his entire worldview collapses and he becomes a potential defector — the Church's best investigator turning against them.

**Arc trigger:** Any PC with TS ≥ 30 who interacts with Haelgrund during an investigation can attempt Diagnosis (Cognition vs Ob 2). Success reveals Haelgrund's TS to the PC. What the PC does with this information is the arc.

---

## 5. Sigrid Torsvald — TS Riskbreaker (Löwenritter Covert)

**New NPC.** Riskbreaker operative. Officially does not exist. Knows Lenneth Almqvist from a prior covert assignment protecting the Queen's archive.

**Historical echo:** Christine Granville (Krystyna Skarbek) — Polish-British SOE agent who operated so deep undercover that her personal identity was consumed by the role. Torsvald's TS development while undercover is analogous: the role changed her at a level she cannot reverse, and the institution she serves cannot accommodate who she has become.

**Compromise: Thread Sensitivity in an anti-Thread institution.** TS 35. Torsvald's TS developed during prolonged exposure to Thread-touched artefacts in Lenneth's archive — objects the Riskbreakers were tasked with cataloguing and securing. The Löwenritter (and by extension the Riskbreakers) are loyal to Valoria-as-concept, not to Thread metaphysics. If Torsvald's TS were discovered, the Lions' Table would consider her compromised — not because they think TS is evil, but because they cannot trust that her perception of reality is the same as theirs.

**Ethics:** Consequentialist (aligned with Riskbreaker doctrine). The mission justifies the method. But Torsvald's TS means she can perceive the damage that Riskbreaker operations cause at the Thread level — collateral Coherence damage to bystanders, RS effects from covert Thread-adjacent activities. She knows the cost of every operation in a way her colleagues cannot. This knowledge makes her hesitate on operations with high Thread collateral.

**Behavioral AI — RISK-AVERSE ON THREAD COLLATERAL:** Standard Riskbreaker operations: decisive, efficient, no hesitation. Operations in Thread-active zones or near practitioners: Torsvald over-assesses risk. She will abort or delay operations when Thread collateral exceeds her personal threshold, even if the mission is critical. **Consequence:** Riskbreaker operations in Thread-active territories have a ~30% abort rate when Torsvald leads. Ehrenwall (or her successor) notices the pattern. Deniability Debt +1 when aborted operations leave evidence.

**Lenneth connection:** Torsvald spent 3 seasons securing Lenneth's archive. She knows the archive contains pre-Altonian accounts of Thread perception written by sea-republic scholars — evidence that Thread Sensitivity was once a publicly acknowledged capacity. This knowledge, combined with her own developing TS, makes her a potential bridge between Lenneth's intellectual curiosity and the practitioner world. If Lenneth's archive arc fires, Torsvald is the natural escort/protector — and her divided loyalty (Löwenritter mission vs personal Thread awakening) becomes the arc's central tension.

---

## 6. Halvar Brandt — Löwenritter Officer (Lions' Table)

**New NPC.** Second-in-command to Ehrenwall. Career military officer. If Ehrenwall falls, Brandt is the succession candidate (provisional rule F-30).

**Historical echo:** Flavius Aetius — the "Last Roman," who won every external battle while Rome's internal politics rotted. Aetius focused obsessively on the Hunnic threat and was murdered by the emperor he served because his single-mindedness made him politically uncontrollable. Brandt's border fixation produces the same structural problem: militarily invaluable, politically dangerous.

**Compromise: He fought in the last border war.** Brandt commanded the rearguard during the Altonian incursion 12 years ago. He held Lowenskyst pass for three days against a force that should have overwhelmed him in hours. He lost most of his command. The experience left him with a specific conviction: the peninsula's political factions are playing games while the real threat masses at the border. Church politics, Hafenmark procedure, Crown diplomacy — none of it matters if Altonia comes through the passes again. This conviction makes him an excellent military strategist and a terrible political actor. He cannot take internal Valorian conflicts seriously because he has seen the alternative.

**Ethics:** Protective consequentialism — the peninsula must survive, and survival is a military problem. He is not ambitious in the personal sense. He does not want command. He wants Ehrenwall to act faster because he has calculated how long it takes Altonia to mobilise and he believes the window is closing. His urgency is genuine, not performative.

**Behavioral AI — EXTERNAL THREAT FIXATED:** Brandt evaluates every action against the Altonian threat metric. He supports actions that strengthen the peninsula militarily (even if they destabilise it politically) and opposes actions that weaken it militarily (even if they stabilise it politically). **Consequence:** If Brandt succeeds Ehrenwall, Löwenritter's military posture shifts from political-coup-instrument to border-defence-prioritisation. Martial Law still fires, but Brandt redirects Löwenritter military assets toward T3 (Lowenskyst) and T10 (Spartfell) — the invasion corridors — instead of using them for internal political control. This leaves Crown territories under-garrisoned against internal threats (Church Seizure, Hafenmark expansion) while over-defending against an Altonian invasion that may or may not come. IP-focused players benefit from Brandt; internal-politics players are harmed.

---

## 7. Annika Feldhaus — Guilds Representative

**New NPC.** Senior Guildmaster of the Artisans' Compact (the largest guild consortium). Guilds NPC AI primary decision-maker.

**Historical echo:** Jacques Cœur — medieval French merchant whose commercial empire grew so large he could not know what every branch was doing. Cœur was eventually destroyed when the Crown discovered his network had entangled itself in activities he hadn't authorised. Feldhaus's Thread-touched supply chain is her Jacques Cœur moment waiting to happen.

**Compromise: Thread-touched supply chain.** The Guilds' most profitable trade goods include items sourced through Niflhel's black market network — which, per canon, unknowingly includes Thread-woven artefacts (Niflhel trades items condemned as heretical by the Church, some of which are Thread-touched). Feldhaus knows that ~15% of the Guilds' luxury goods revenue depends on this supply chain. She does not know the goods are Thread-touched — she thinks they're just contraband antiquities. If the Church or a practitioner reveals the Thread connection, Feldhaus faces ruin: the Guilds' economic model is built on heretical goods.

**Ethics:** Utilitarian — greatest good for the greatest number of guild members. Feldhaus genuinely cares about artisan livelihoods. But her utilitarianism blinds her to the specific harm of Thread-touched goods entering non-sensitive households (potential low-grade Coherence effects on prolonged exposure — a design gap, but a narratively rich one).

**Behavioral AI — PROFIT-MAXIMISING:** Feldhaus optimises for Guilds Wealth above all other stats. She will sacrifice Guilds Mandate (political standing) and Stability (institutional cohesion) to protect revenue streams. **Consequence:** Guilds Wealth remains high, but Guilds Mandate trends toward 2 (political irrelevance). The Guilds become economically powerful but politically marginalised — they can fund anyone but influence no one.

---

## 8. Peder Almstedt — Ministry Bureaucrat

**New NPC.** Chief Parliamentary Clerk. The Ministry's operational brain. Places AP-tokens, manages PI recovery, facilitates Parliamentary Manoeuvres.

**Historical echo:** The Byzantine *logothetes* — senior bureaucrats who outlived every dynasty because removing them would collapse the administrative apparatus. Almstedt is not powerful. He is necessary. The distinction protects him from every faction that would prefer he did not exist.

**Compromise: Institutional preservation over justice.** Almstedt has served under three monarchs. His loyalty is to the institution of Parliament, not to any faction or ruler. He will facilitate procedural outcomes that preserve Parliamentary function even when those outcomes are unjust — blocking Hafenmark reforms that would destabilise procedure, shielding Crown Emergency Powers from Parliamentary review because "the precedent of review is more dangerous than the abuse." He is the system's immune response, and the system is not always good.

**Ethics:** Procedural — the process is sacred. If the process produces a bad outcome, the process must be reformed through process. Never bypassed. This makes him an obstacle to every faction that wants rapid change, including the player characters.

**Behavioral AI — CONSERVATIVE:** Almstedt resists change. Any Domain Action that would alter Parliamentary structure (Crown Emergency Powers, Hafenmark Reform, Löwenritter Reconstitution) faces Ministry opposition: Almstedt's NPC action is always "Stabilise" — PI recovery, AP-token maintenance, procedural challenge to radical proposals. **Consequence:** PI recovers 1 point faster per season when Almstedt is active (he's good at his job). But Parliamentary reform actions (any action that changes how Parliament functions) are at +1 Ob (he's blocking them through procedure). Players who want institutional change must either co-opt Almstedt (Influence vs Ob 3) or remove him (scandal, retirement, or worse).

---

## 9. Gerik Strand — Crown Minister (Lord Steward)

**New NPC.** Minor lord of Feldmark (T5 — the breadbasket, productive but unglamorous). Appointed Lord Steward by Almud because Strand is competent and the Crown needs administrators who can actually run a treasury. The appointment elevated him above his station. He knows it. Everyone at court knows it.

**Historical echo:** William Marshal began as a landless younger son who rose through tournament prowess and relentless performance. Strand is a provincial landowner who rose through administrative competence and relentless performance. Both men are defined by the gap between their merit and their birth — and by the knowledge that the gap never fully closes.

**Compromise: Conditional position in an unconditional world.** Strand is surrounded by Almud's inner circle (born to it), Hafenmark's parliamentary grandees (institutional weight), and Church Cardinals (divine mandate). His position is royally appointed — which means royally revocable. Theirs is inherited or institutional. If Strand stops outperforming everyone, he's recalled to count wheat yields in Feldmark. If they stop performing, they're still Duke of Something. This structural insecurity drives everything he does.

**Ethics:** Meritocratic — competence should determine standing. Genuine. Strand believes the peninsula would be better governed if ability mattered more than lineage. This belief is correct and makes him enemies. He is not jealous of specific people — he is jealous of the *principle* that birth outweighs ability. Every aristocratic courtesy he is denied, every committee he is excluded from, every decision made without consulting him confirms that the system is broken. His drive to impress is his proof that the system is wrong.

**Behavioral AI — OVERPERFORMER:** Strand takes on too much, executes at high quality, takes credit aggressively, and cannot delegate. Delegating means someone else demonstrates competence, which means Strand becomes dispensable. **Consequence:** Crown administrative efficiency is high when Strand is active — Treasury actions +1D, Accounting errors reduced (fewer misapplied clock changes). But Strand creates institutional brittleness: he IS the Crown's administrative capacity. If he is removed, incapacitated, or turned, Crown Domain Actions that require administrative execution (Tax, Trade, Policy) are at +1 Ob for 2 seasons until a replacement stabilises. He is also susceptible to flattery from anyone who treats him as a peer rather than an appointee — Church diplomatic overtures, Hafenmark parliamentary invitations, even Varfell intelligence approaches that frame him as a "man of substance." Strand will give more access than he should to anyone who makes him feel like he belongs.

**Flattery vulnerability (mechanical):** Social actions targeting Strand that include genuine acknowledgment of his competence (not transparent manipulation — Strand is smart enough to detect lies): −1 Ob. This makes him the easiest Crown court figure to influence, despite being the most capable.

---

## 10. Dalla Virke — Syndicate Broker (Niflhel)

**New NPC.** Operates for the Virke family — one of several competing syndicate houses that collectively constitute what Valorians call "the Niflhel." The Niflhel is not a coordinated faction: it is a colloquial name for the constellation of criminal families, smuggling networks, and black market syndicates that operate across the peninsula's margins. The Virke family specialises in antiquities, contraband luxury goods, and discreet logistics. They compete with at least three other major syndicates (unnamed — GM discretion) for territory and clients.

**Historical echo:** The Medici bank's branch managers operated semi-autonomously — each branch was technically part of the Medici network but practically an independent fiefdom run on personal relationships. When branch managers prioritised local clients over Florence's directives, the tension between personal loyalty and institutional control defined the bank's politics. Virke is a branch manager whose branch is more loyal to her than to the family.

**Compromise: Thread-touched supply chain she built personally.** Virke's most profitable line is antiquities sourced from Einhir ruins and southern communities — goods condemned as heretical by the Church, which is what makes them valuable. Some of these items are Thread-woven. Virke has no TS (TS 0) and no concept of Thread metaphysics. She selected these goods herself, vetted the sources herself, built the supply chain herself. If the Thread connection is revealed, it is not an institutional failing she can blame on the family — it is her personal judgment that was wrong. Her professional reputation, the thing that distinguishes her from every other syndicate broker, is built on the claim that she knows what she's selling. She didn't.

**Ethics:** Honour among operators — your word is your network. Virke has built genuine relationships with Valorian trade partners over a decade. She knows their families. She extended credit during hard seasons. Her network runs on personal trust, and this trust is why the Virke family's peninsula operation outperforms larger syndicates. The compromise: her personal loyalty to partners sometimes conflicts with family directives. She will protect a trade partner from rival syndicates and even from her own family's enforcement if she judges the partner's default was justified. This has cost the family revenue twice. A third time, the family sends someone to manage her.

**Behavioral AI — NETWORK PROTECTOR:** Virke's first priority is her relationship network, second is family revenue. She will not burn a source — ever — because the network IS her value. She will sell intelligence about non-partners freely. **Consequence:** Factions inside Virke's trust network get protection. Factions outside it get exploited. But Virke's protectionism also means she withholds information from the Virke family's senior partners. If the family discovers she's shielding Valorian clients from family intelligence operations, they replace her with someone who has no loyalty to anyone on the peninsula — and the trust network collapses overnight.

---

## 11. Doux Alexios Laskaris — Altonian Prince (married to Elske)

**New NPC.** Altonian *doux* (provincial governor-general) whose province borders T4 (Grauwald). Married to Princess Elske Almqvist. The marriage was arranged by the Altonian imperial court as a dynastic insurance policy on Valorian compliance.

**Historical echo:** Demetrios Palaiologos, last Despot of Morea, surrendered his province to the Ottomans partly to protect his family — a decision that was simultaneously rational and treasonous. Laskaris occupies the same structural position: his duty to the empire and his duty to the person he was given as a political instrument are diverging, and he is choosing the person.

**Compromise: Genuine attachment to an assigned asset.** Laskaris was given Elske as leverage. The imperial court expects him to use Elske's dynastic claim to pressure Valoria — Torben Tutoring Demands, succession interference, implied annexation threats. Laskaris has instead developed genuine regard for Elske's autonomy and intelligence. He delays Tutoring Demands, softens ultimatums, and has twice leaked imperial court intentions to Elske (who passed them to Crown through her own channels). He is not a romantic fool — he is a competent administrator who has decided that his province's long-term stability depends on a functional Valoria more than on imperial directives that treat Valorians as subjects-in-waiting.

**Ethics:** Oikonomia — the Byzantine principle that strict application of law can be suspended when pastoral care demands it. Laskaris applies this to statecraft: the empire's formal claim on Valoria is legally valid, but enforcing it would destroy the peninsula that makes the claim valuable. He is loyal to Altonia's *interests* while quietly subverting Altonia's *policies*. The distinction is real to him. It would not survive imperial review.

**Behavioral AI — PROTECTIVE:** Laskaris's priority is Elske's safety and his province's stability. Actions that reduce IP and protect Elske: he enables them. Actions that increase IP or threaten Elske: he resists. **Consequence:** IP rises ~1 point slower per season when Laskaris is the active Altonian representative (he is sandbagging imperial directives). But if Elske is threatened (Elske Loyalty ≤ 2, or Return attempt fails), Laskaris flips — IP +3 immediately as he stops shielding Valoria and prioritises Elske's extraction to his province. The protective instinct that benefits Valoria can catastrophically reverse.

**Naming note:** Altonian names follow Greek/Macedonian conventions. "Doux" = provincial military governor. "Laskaris" = noble dynasty (historical: Empire of Nicaea). Imperial court titles, religious terminology (Almaic Kyriakos), and military ranks should use Greek forms in all Altonian contexts.

---

## 12. Rikard Solberg — Schoenland Factor

**New NPC.** Schoenland's trade factor (commercial ambassador) in Valorsplatz. Manages Schoenland's interests on the peninsula.

**Historical echo:** The homesickness that shaped Xenophon's *Anabasis* — ten thousand Greeks fighting their way home because no strategic objective mattered as much as returning. Solberg is not fighting, but the motivational structure is identical: every professional decision is unconsciously filtered through "does this bring me closer to going home?"

**Compromise: He wants to go home.** Solberg is Schoenland-born and Schoenland-loyal. He does not have secret Valorian sympathies. His problem is simpler: Schoenland's profit-from-chaos model means his posting never ends. As long as Valoria is unstable, Solberg is too valuable to recall. Stable Valoria = Solberg goes home to his family. Unstable Valoria = Solberg stays indefinitely. He has been on this posting for 7 years. His children are growing up without him. He is unconsciously steering Schoenland policy toward outcomes that would let him leave — which means outcomes that stabilise Valoria, which means outcomes that harm Schoenland's long-term interests.

**Ethics:** Institutional loyalty — he serves Schoenland. But his personal desire for stability has infiltrated his professional judgment in ways he cannot fully see. He genuinely believes his policy recommendations are correct for Schoenland. They are not. They are correct for a man who wants to go home.

**Behavioral AI — STABILITY-SEEKING:** Solberg unconsciously favours actions that reduce peninsula tension. Arms shipments to all factions: he recommends conservative quantities ("oversupply invites escalation"). Intelligence reports to Schoenland central: he downplays instability ("the situation is manageable"). Trade terms: he offers slightly better deals to whichever faction is currently losing (stabilising the balance of power). **Consequence:** Schoenland's peninsula policy is ~1 season behind optimal aggression. If a genuinely neutral Schoenland agent replaced him, arms flows would increase, intelligence would be sharper, and Schoenland would extract more value from the chaos. Players who discover Solberg's motivation can leverage it: offer him a plausible path to recall (e.g., a Valorian-Schoenland stability treaty) and he will work actively to make it happen — becoming a genuine Crown/Hafenmark asset. But the treaty must be real. Solberg is not stupid and will not believe a false promise.

---

## 13. [NAME PENDING] — Fourth Cardinal (Prudence)

**New NPC.** Cardinal of Prudence (economic portfolio). The unnamed fourth Cardinal referenced in ED-007. Manages tithes, charities, Church land.

**Historical echo:** Suger of Saint-Denis — the 12th-century abbot who ran his abbey like a commercial enterprise, maximised revenue, invested in unprecedented infrastructure (the first Gothic cathedral), and created friction with Cistercian reformers who believed the Church should be austere. Suger's logic was "wealth is God's instrument" — exactly the Prudence Cardinal's operating philosophy. Both men are right about the ends and destructive about the means.

**Compromise: The tithe maximiser.** The Prudence Cardinal genuinely cares about the faithful — and his method of caring is to extract every possible coin from the Church's economic apparatus and redistribute it. He runs the Church's finances like a commercial enterprise: renegotiating Parish tithe quotas upward, auditing monastery expenditures, consolidating Church landholdings for efficiency, and pressuring Parish leaders who fall short of revenue targets. The redistribution is real — Church charities are well-funded, Church hospitals function, the poor are fed. But the extraction creates institutional friction: Parish leaders resent being treated as revenue centres, local clergy feel squeezed, and communities that once gave willingly now give resentfully. He is producing the Church's best charitable outcomes while eroding the Church's grassroots loyalty.

**Ethics:** Stewardship — wealth exists to be deployed for the faithful, and deployment requires maximisation. He is not greedy. He lives simply. Every coin he extracts goes back out. But he cannot see that the relationship between the Church and its flock is not a balance sheet. The friction he creates is invisible to him because his metrics all point upward.

**Behavioral AI — OPTIMISER:** The Prudence Cardinal maximises Church Wealth throughput. Tithe collection is aggressive — Church Wealth recovers +1 per season when he is active (baseline is +0). But territorial Church Mandate erodes: in any territory where the Prudence Cardinal has increased tithe quotas (GM tracks — typically 2–3 territories per season), Church Mandate suffers −0.5 (tracked fractionally, applied at Year-End: −1 per 2 territories squeezed). **Consequence:** Church is flush with resources but losing popular support. Parish leaders who feel squeezed become RM recruitment targets — CV erosion accelerates in over-tithed territories by +1 per Year-End (the people resent the institution). The Prudence Cardinal is inadvertently funding the Church's charitable mission while undermining its cultural authority — the exact inversion of what the Church needs to win via Conviction Yield.

---

## Summary Table

| # | Name | Faction | Compromise | AI Flaw | Key Consequence |
|---|------|---------|------------|---------|-----------------|
| 1 | Edeyja | Wardens | None (exempt) | None | Moral anchor |
| 2 | Maret Uln | Varfell | Dual loyalty (RM sympathy) | CONFLICTED (hesitates vs RM) | Varfell intel 1 season late on RM |
| 3 | Maret Vossen | RM | Visibility = target | IDEALIST (spreads thin) | Presence markers vulnerable |
| 4 | Sæmund Haelgrund | Church | Evidence he can't report | PROCEDURALIST (slow) | Investigations +1 season but Overwhelming |
| 5 | Sigrid Torsvald | Löwenritter (covert) | TS 35 in anti-Thread org | RISK-AVERSE on Thread | ~30% abort rate in Thread zones |
| 6 | Halvar Brandt | Löwenritter | Border war trauma → threat fixation | EXTERNAL THREAT FIXATED | Redirects military to borders, neglects internal |
| 7 | Annika Feldhaus | Guilds | Thread-touched supply chain | PROFIT-MAXIMISING | Wealthy but politically marginalised |
| 8 | Peder Almstedt | Ministry | Preserves system over justice | CONSERVATIVE (blocks reform) | PI recovers faster but reform +1 Ob |
| 9 | Gerik Strand | Crown Court (Lord Steward) | Conditional position, unconditional world | OVERPERFORMER (can't delegate) | Crown admin +1D but brittle; flattery −1 Ob |
| 10 | Dalla Virke | Virke syndicate (Niflhel) | Thread-touched supply chain she built | NETWORK PROTECTOR | Shields partners; withholds intel from own family |
| 11 | Doux Alexios Laskaris | Altonia | Genuine attachment to assigned asset | PROTECTIVE (shields Elske) | IP +1/season slower; flips if Elske threatened |
| 12 | Rikard Solberg | Schoenland | Wants to go home | STABILITY-SEEKING | Schoenland policy ~1 season behind optimal |
| 13 | [Name Pending] | Church (Prudence) | Tithe maximiser alienates parishes | OPTIMISER | Church Wealth +1/season but Mandate erodes in squeezed territories |

---

## Cross-Reference: Faction Axis Positions

Per worldbuilding_integration_v3 §axis system, each NPC sits on 2–3 of the 9 axes:

| NPC | Axis 1 | Axis 2 | Axis 3 |
|-----|--------|--------|--------|
| Edeyja | 9 (world is more) | — | — |
| Maret Uln | 7 (transparency) | 9 (world is more) | 4 (change) |
| Maret Vossen | 3 (equity) | 4 (change) | 9 (world is more) |
| Haelgrund | 5 (order) | 9 (world is what it appears → crumbling) | 2 (institutional faith) |
| Torsvald | 5 (order) | 9 (world is more → awakening) | 8 (resistance) |
| Brandt | 5 (order) | 6 (ducal/Crown command) | 8 (resistance) |
| Feldhaus | 3 (prosperity) | 4 (stability) | 7 (pragmatic secrecy) |
| Almstedt | 5 (order) | 1 (institutional legitimacy) | 4 (stability) |
| Strand | 3 (meritocracy vs birth) | 1 (Crown legitimacy — conditional) | 5 (institutional order — proves worth through) |
| Virke | 7 (secrecy — syndicate) | 3 (prosperity — network) | — |
| Laskaris | 8 (oikonomia — imperial law vs pastoral care) | 6 (Altonian authority) | — |
| Solberg | 3 (prosperity) | 4 (stability — personal need) | — |
| Prudence Cardinal | 3 (prosperity — maximisation) | 2 (institutional faith) | 5 (order — institutional friction) |

---


---

## Mode Interface Matrix

Every NPC must have meaningful presence in at least 2 of 3 modes. Their compromise and behavioral flaw must produce consequences in each mode they appear in.

### Legend
- **Full**: Named character with stat block, dialogue, personal scenes
- **Event Card**: Named Character Event in the BG deck — triggers on game-state conditions
- **Modifier**: Always-active NPC effect on faction stats or action Obs
- **Abstracted**: NPC's effects are present but the character is not directly represented
- **Absent**: Not present in this mode

---

### 1. Edeyja (Wardens)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Thread operations mentor. Highest-TS living practitioner. PCs who reach Askeheim interact with her directly. Provides Diagnosis, training, and narrative framing for the metaphysical stakes. Moral anchor — she will not compromise, which forces PCs to meet her standard or accept they cannot. |
| Hybrid | **Full → Modifier** | Personal scenes with Edeyja (Zoom In at T15/T6) generate Domain Echoes: successful Thread training → WC +1 at next Accounting. Edeyja refuses requests that compromise Warden neutrality — PCs cannot weaponise her for faction goals. |
| BG | **Abstracted** | Edeyja does not appear as a card or token. Her effects are embedded in the WC/WR tracks and the Askeheim Expedition mechanics. Warden Emergence check (Accounting Step 9) is her threshold for engaging with the peninsula at all. |

**Mode bridge:** In Hybrid, the PC's relationship with Edeyja is the human face of the WC track. WC +1 is not an abstract advancement — it is Edeyja deciding that this faction's practitioner has demonstrated sufficient competence and integrity to warrant cooperation. The BG abstraction conceals a personal judgment.

---

### 2. Maret Uln (Varfell)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Intelligence operative. Practitioner (TS ~50). Dual loyalty arc — PCs who discover her RM sympathy can exploit it, reinforce it, or try to resolve it. Belief checks when ordered to act against RM interests. Personal Thread operations during intelligence missions (co-movement fires). |
| Hybrid | **Full → Event** | CONFLICTED flaw: Varfell intelligence actions targeting RM-adjacent territories are delayed 1 season when Maret leads them (she hesitates). PCs can Zoom In to confront or support her during the hesitation. If Vaynard is eliminated, Maret succession fires as a Domain Echo — VTM resets, Varfell realigns. |
| BG | **Event Card** | *Card: Varfell Succession.* Trigger: Vaynard eliminated (Loyalty 0 + Mandate 0). Effect: Maret takes leadership. VTM → 0. Varfell cannot target RM. Varfell Stability −1 (faction reorientation). Counter-play: prevent Vaynard's elimination. |

**Mode bridge:** In TTRPG, Maret's hesitation is a personal choice the player witnesses. In BG, it's a 1-season delay on Varfell intelligence actions in RM-adjacent territories. The Hybrid Zoom In lets the player see why the delay happened.

---

### 3. Maret Vossen (Restoration Movement)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | RM leader. Founding Agent candidate. PCs who affiliate with RM interact with her directly. Her visibility compromise creates tension — every public appearance risks Church AP accumulation. TS 25 means she can sense Thread-touched artefacts but cannot resist the Forgetting near T13/T15. |
| Hybrid | **Full** | Key figure in Founding Mechanic. If she is the Founding Agent, her Influence roll determines RM's starting stats. Her IDEALIST flaw (spreads Presence thin) means Hybrid RM is culturally broad but institutionally fragile — Domain Echoes from personal scenes spread markers rather than consolidating them. |
| BG | **Absent** | RM is not a player faction in BG-only mode (PP-478). Vossen does not appear. Presence markers are environmental tokens with no named NPC driving them. |

**Mode bridge:** Vossen exists only in modes where RM can be player-facing. Her absence from BG-only mode is the mechanical expression of the design principle that RM is a player/NPC-led mid-game emergence, not a starting faction.

---

### 4. Sæmund Haelgrund (Church — Inquisitor)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Inquisitor antagonist/ally. Hidden TS 12. PROCEDURALIST: investigations are slow but thorough. PCs can Diagnose his TS (Cognition vs Ob 2), creating a defection arc. Social scenes with Haelgrund use the contest system — he argues from evidence, not dogma, making him harder to dismiss than a zealot. |
| Hybrid | **Full → Modifier** | Heresy Investigations Haelgrund leads take +1 season to resolve but resolve at Overwhelming if they complete. Zoom In during an investigation lets PCs intervene (warn the target, plant counter-evidence, attempt Diagnosis). Domain Echo: if Haelgrund's TS is revealed, Church Stability −1 + Heresy Investigation suspended 1 season. |
| BG | **Event Card** | *Card: Haelgrund Investigation.* Trigger: Church opens Heresy Investigation in any territory. Effect: investigation takes +1 season (Haelgrund is thorough). If it resolves: treat as Overwhelming regardless of roll. Counter-play: any faction may spend 1 Intel action in the target territory to plant counter-evidence (investigation resolves as Partial instead). *Card: Haelgrund Defection.* Trigger: Thread operation Overwhelming within 1 territory of Haelgrund's current investigation AND Church has no active Inquisitor suppression. Effect: Haelgrund removed from Church service. Church Heresy Investigation Ob +1 permanently (best investigator lost). Haelgrund becomes available as a neutral NPC practitioner (TS 12 — low but symbolically devastating for Church). |

**Mode bridge:** In TTRPG, the Diagnosis scene is a dramatic personal moment. In BG, it's the Defection card trigger — a Thread operation near his investigation that finally cracks his worldview. The Hybrid Zoom In is where the player makes it happen.

---

### 5. Sigrid Torsvald (Löwenritter — Riskbreaker)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Undercover operative. TS 35. Lenneth archive connection. PCs encounter her during covert operations or through Lenneth's arc. Her RISK-AVERSE flaw on Thread collateral means she may abort mid-mission — PCs present during an abort can try to resolve the situation she couldn't. |
| Hybrid | **Modifier** | Riskbreaker operations in Thread-active territories: ~30% abort rate when Torsvald leads. Aborted operations leave evidence → Deniability Debt +1. Domain Echo from a Torsvald abort: Crown covert capability −1D for 1 season. Zoom In: PCs can accompany Torsvald on a Riskbreaker operation and handle the Thread-collateral problem she can't. |
| BG | **Abstracted** | Torsvald's effects are embedded in the Riskbreaker Exposure card (Deniability Debt tracker). Her abort rate is the reason the Debt accumulates faster than Ehrenwall expects. She does not appear as a named card — Riskbreakers are deniable by design. |

**Mode bridge:** Torsvald is invisible in BG because that's what Riskbreakers are. The Deniability Debt rising "for no apparent reason" in BG is explained by Torsvald's aborts in Hybrid/TTRPG. The player who Zooms In discovers why Crown's covert arm keeps failing.

---

### 6. Halvar Brandt (Löwenritter)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Military officer. Border war veteran. PCs encounter him at T3 (Lowenskyst) or T14 (Ehrenfeld). His EXTERNAL THREAT FIXATED flaw means he interprets every situation through the Altonian lens — useful when the threat is real, catastrophic when it isn't. Personal combat stats: high (career soldier). |
| Hybrid | **Event** | If Ehrenwall falls, Brandt succession fires. Military assets redirect from internal control to border defence (T3/T10). Domain Echo: Crown-held territories lose Martial Law garrison coverage. PCs can Zoom In to persuade Brandt to maintain internal garrison (Influence vs Ob 3 — his fixation resists). |
| BG | **Event Card** | *Card: Brandt Succession.* Trigger: Ehrenwall removed (death, player action, or Lions' Table Mutiny). Effect: Löwenritter military redirects — Military actions in T3/T10 at −1 Ob (border focus), Military actions in all other territories at +1 Ob (internal neglect). Coup Counter mechanic continues but Brandt's threshold is 2 not 3 (he acts sooner). Counter-play: Crown Treaty with Löwenritter (Influence vs Ob = Brandt's Military stat) convinces Brandt to maintain balanced deployment. |

**Mode bridge:** Ehrenwall's coup is a political instrument. Brandt's coup is a military instrument aimed at the wrong target. The BG Event Card mechanises the consequence; the TTRPG/Hybrid scenes reveal why Brandt is wrong (or prove him right, if Altonia actually invades).

---

### 7. Annika Feldhaus (Guilds)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Guildmaster. PCs interact with her for trade, contracts, supply access. Her Thread-touched supply chain is discoverable through investigation (Intel + Thread Diagnosis on guild goods, Ob 3). Social contest scenes: she is shrewd, PROFIT-MAXIMISING, and will trade anything for the right price — except her reputation. |
| Hybrid | **Full → Event** | Thread-touched goods revelation: if a PC Diagnoses guild merchandise during a Zoom In, the Domain Echo is devastating: Guilds Wealth −1, Guilds Stability −2, Feldhaus's network exposed. Church gains grounds for Heresy Investigation targeting Guilds. Alternatively, PCs can quietly warn Feldhaus — she owes them, creating a leverage relationship. |
| BG | **Modifier + Event Card** | *Modifier (always-active):* Guilds Wealth recovery +1/season (Feldhaus is effective). Guilds Mandate trends toward 2 (she neglects politics). *Card: Supply Chain Exposure.* Trigger: Intel Overwhelming targeting Guilds in territory with Niflhel syndicate presence. Effect: Guilds Wealth −1, Stability −2. Church opens free Heresy Investigation vs Guilds. Virke family network disrupted (Niflhel trade actions +1 Ob for 2 seasons). Counter-play: Guilds may pre-emptively audit supply chain (spend 1 Wealth + 1 Stability at Accounting) to remove Thread-touched goods quietly. No public scandal but revenue drops permanently (Wealth recovery bonus lost). |

**Mode bridge:** The Thread-touched supply chain connects Feldhaus to Virke. Exposing one affects both. In TTRPG, this is a personal investigation. In BG, it's a card trigger. In Hybrid, it's a Zoom In that produces cascading Domain Echoes across two factions.

---

### 8. Peder Almstedt (Ministry)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Parliamentary Clerk. PCs encounter him when navigating Crown bureaucracy — permits, hearings, procedural challenges. His CONSERVATIVE flaw means he blocks radical action through procedure, not force. Social contest scenes with Almstedt are procedural debates (Cognition-heavy, not Presence-heavy). |
| Hybrid | **Modifier** | PI recovery +1/season when Almstedt is active (he stabilises Parliament). Reform actions +1 Ob (he obstructs them). PCs can Zoom In to co-opt Almstedt (Influence vs Ob 3) or remove him (requires scandal or Crown dismissal — Domain Echo: PI recovery bonus lost for 2 seasons). |
| BG | **Modifier (always-active)** | Almstedt is the Ministry's operational expression. His effects are the Ministry NPC AI's baseline: AP-token placement, PI recovery, Parliamentary Manoeuvre facilitation. If Ministry Mandate drops to 0, Almstedt is effectively sidelined — PI recovery bonus lost, reform Ob penalty lifted. He is not a card because he doesn't trigger — he persists. Removing him requires destroying the Ministry itself. |

**Mode bridge:** Almstedt is the system. In TTRPG, he's a person you can argue with. In BG, he's the reason PI recovers and reforms are slow. The Hybrid Zoom In is where the player decides whether the system deserves to persist.

---

### 9. Gerik Strand (Crown — Lord Steward)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Court minister. PCs encounter him in Crown administrative scenes — treasury disputes, resource allocation, diplomatic logistics. His flattery vulnerability (−1 Ob to social actions acknowledging his competence) makes him the easiest Crown figure to influence. His OVERPERFORMER flaw means he's running every important task — PCs who need Crown cooperation go through Strand. |
| Hybrid | **Modifier** | Crown administrative Domain Actions (Tax, Trade, Policy) at +1D when Strand is active. If Strand is removed/turned: Crown admin actions at +1 Ob for 2 seasons. Zoom In: any faction can target Strand with social approaches — flattery vulnerability creates low-Ob influence opportunities that produce Domain Echoes (intelligence leak, resource redirect, schedule manipulation). |
| BG | **Modifier (always-active)** | Crown Treasury actions +1D. If Strand is removed (Event Card or player action): Crown Tax/Trade/Policy +1 Ob for 2 seasons. *Card: Strand Turned.* Trigger: any non-Crown faction succeeds on Intel action targeting Crown Court with Overwhelming. Effect: Strand has been compromised — intelligence leak. Non-Crown faction learns Crown's full stat line + planned actions for next season. Strand removed. Crown admin penalty applies. Counter-play: Crown may run counter-intelligence (Intel vs Ob 2) each season to detect the approach before it succeeds. |

**Mode bridge:** Strand's competence makes Crown efficient. His insecurity makes Crown vulnerable. In BG, this is a +1D bonus with a Turned-card downside. In TTRPG, it's a person whose need to belong makes him open doors he shouldn't. Hybrid connects the two: a Zoom In scene where a player flatters Strand into sharing Crown plans produces a Domain Echo that IS the Turned card.

---

### 10. Dalla Virke (Virke syndicate)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Syndicate broker. PCs interact with her for black market access, contraband, intelligence. Her trust network creates asymmetric access — PCs who've built a trading relationship get protection; newcomers get exploited. Thread-touched goods investigation arc: Diagnosis on her merchandise reveals the Thread connection. |
| Hybrid | **Full → Event** | Virke's trust network determines which factions get favourable Niflhel trade terms in BG. PC actions in Zoom In (building or burning the trust relationship) produce Domain Echoes that modify Niflhel trade Obs for specific factions. Thread-touched revelation: Domain Echo cascades to Feldhaus (Guilds) via shared supply chain. |
| BG | **Modifier** | Niflhel trade actions use Virke's network. Factions inside the trust network (determined by prior Hybrid interactions, or GM-set in BG-only): trade Ob −1. Factions outside: no modifier. *Card: Supply Chain Exposure* (shared with Feldhaus — see #7). If Virke is recalled by her family (trust network collapse), all Niflhel trade actions +1 Ob for remainder of campaign (replacement has no local relationships). |

**Mode bridge:** Virke's trust network is built in TTRPG scenes, expressed as BG trade modifiers, and can be destroyed by a single Hybrid revelation. She is the living connective tissue between the criminal economy and the political board.

---

### 11. Doux Alexios Laskaris (Altonia)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full (conditional)** | PCs encounter Laskaris only if they travel to T4 border or engage with the Altonian diplomatic channel. His PROTECTIVE flaw: scenes involving Elske's safety override his political judgment. PCs can leverage this — threaten Elske's position to force Laskaris's cooperation, or protect Elske to earn his trust. |
| Hybrid | **Modifier** | IP modifier: IP rises ~1/season slower when Laskaris is the active Altonian representative (he sandbangs imperial directives). If Elske Loyalty ≤ 2: Laskaris flips — IP +3 immediately (Domain Echo). Zoom In at T4: PCs can influence Laskaris's disposition toward Valoria. A successful social scene (Influence vs Ob 2) delays the next Tutoring Demand by 1 season. |
| BG | **Modifier (always-active) + Event Card** | *Modifier:* IP generation rate −1/season (Laskaris sandbagging). *Card: Laskaris Flip.* Trigger: Elske Loyalty ≤ 2 at Accounting OR Elske Return attempt fails. Effect: IP +3 immediately. Laskaris replaced by imperial-loyal governor. IP generation returns to baseline. Elske's off-board card locked (no further Contact attempts until new diplomatic channel opened — Crown Influence vs Ob 4). Counter-play: maintain Elske Loyalty ≥ 3. |

**Mode bridge:** Laskaris is the IP clock's human face. In BG, IP just rises slower. In TTRPG/Hybrid, a person is making it rise slower because he doesn't want to hurt the woman he was told to use as a weapon. The flip — when Elske is threatened — transforms the IP track from slow-burn to crisis in a single Accounting step.

---

### 12. Rikard Solberg (Schoenland)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Trade factor in Valorsplatz. PCs encounter him in commercial/diplomatic scenes. His STABILITY-SEEKING flaw makes him a natural ally for any PC pursuing peace — and a natural obstacle for any PC pursuing escalation. His motivation (homesickness) is discoverable through social interaction (Read action, Ob 2). |
| Hybrid | **Modifier** | Schoenland arms shipments: Solberg recommends conservative quantities to all factions (stability-seeking). Domain Echo from Zoom In: PCs who offer a credible stability treaty gain Solberg as an active Crown/Hafenmark asset (Schoenland trade terms improve for the treaty faction). PCs who threaten Solberg's recall leverage gain nothing — he's more afraid of staying than of them. |
| BG | **Modifier (always-active)** | Schoenland policy modifier: arms supply to all factions −1 unit/season vs optimal (Solberg understates demand). Intelligence reports to Schoenland central: downplayed (Schoenland's external response to crises is 1 season delayed). If Solberg is recalled (discovery of bias, or Schoenland central reassessment): arms supply normalises, intelligence sharpens. All factions receive +1 unit/season. Schoenland becomes a more dangerous neutral actor. |

**Mode bridge:** Solberg's homesickness makes Schoenland less dangerous. His removal makes Schoenland more dangerous. In BG, this is a supply-rate modifier. In TTRPG, it's a man counting the days until he sees his children. The player who understands the personal story can manipulate the strategic reality.

---

### 13. [Name Pending] — Prudence Cardinal (Church)

| Mode | Presence | Interface |
|------|----------|-----------|
| TTRPG | **Full** | Church internal politics. PCs encounter him in tithe disputes, charitable operations, Parish leader complaints. His OPTIMISER flaw is visible in every scene: he runs the Church's finances brilliantly and creates friction doing it. PCs aligned with the Church must navigate his Parish conflicts; PCs opposing the Church can exploit the friction. |
| Hybrid | **Modifier** | Church Wealth recovery +1/season (his tithe efficiency). But: in territories where he has increased tithe quotas, Church Mandate −0.5 at Year-End (fractional, tracked). CV erosion accelerates +1 in over-tithed territories at Year-End (resentful communities become RM recruitment targets). Zoom In at a Parish in an over-tithed territory: PCs can witness the friction firsthand and either support the Parish (Church Mandate preserved but Wealth bonus lost in that territory) or support the Cardinal (Wealth maintained but Mandate loss confirmed). |
| BG | **Event Card (revised Prudence Crisis)** | *Card: Prudence Crisis.* Trigger: Church Wealth ≤ 2 (tithe income insufficient despite the Cardinal's efforts — external pressure has overwhelmed his optimisation). Effect: Church charities collapse in territories with Prosperity ≤ 3. Church Mandate −1 in each. RM gains +1 Influence in those territories. *Card: Parish Revolt.* Trigger: ≥ 3 territories where Prudence Cardinal has increased tithes AND Church Mandate ≤ 3 in any of them. Effect: Parish leaders refuse collection. Church Wealth −2 for 1 season. CV −1 in all affected territories (communities reject Church authority). TC −1 (institutional fracture). Counter-play: Church spends 1 Stability to discipline Parish leaders (tithes restored but Mandate −1 in affected territories permanently). |

**Mode bridge:** The Prudence Cardinal's efficiency creates two BG event risks that are invisible until they fire. In TTRPG, the Parish friction is visible immediately — PCs see communities struggling under the extraction. The Hybrid Zoom In is where the player decides whether to intervene in a problem that will eventually become a BG crisis.

---

## Mode Coverage Summary

| NPC | TTRPG | Hybrid | BG | Modes Active |
|-----|-------|--------|-----|-------------|
| Edeyja | Full | Full→Modifier | Abstracted (WC/WR) | 2.5 |
| Maret Uln | Full | Full→Event | Event Card | 3 |
| Maret Vossen | Full | Full | Absent (PP-478) | 2 |
| Haelgrund | Full | Full→Modifier | Event Card ×2 | 3 |
| Torsvald | Full | Modifier | Abstracted (Debt) | 2.5 |
| Brandt | Full | Event | Event Card | 3 |
| Feldhaus | Full | Full→Event | Modifier + Card | 3 |
| Almstedt | Full | Modifier | Modifier | 3 |
| Strand | Full | Modifier | Modifier + Card | 3 |
| Virke | Full | Full→Event | Modifier + Card | 3 |
| Laskaris | Full (conditional) | Modifier | Modifier + Card | 3 |
| Solberg | Full | Modifier | Modifier | 3 |
| Prudence Cardinal | Full | Modifier | Event Card ×2 | 3 |

All NPCs active in ≥ 2 modes. 10 of 13 active in all 3 modes.

## Stat Blocks

Deferred to next session. Each NPC requires: 10 TTRPG attributes, TS, Coherence, Beliefs (2), Inspirations (1–2), Resonant Style, and BG Event Card design where applicable.

[EDITORIAL: Full roster flagged for user review. Names, motivations, compromises, and behavioral profiles are provisional. User may modify any element. Stat blocks will be generated after identities are confirmed.]
