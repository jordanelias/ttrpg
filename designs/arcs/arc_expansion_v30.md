# VALORIA — Arc Expansion: Emergent Conditioners and Triggers v1.0
## Date: 2026-04-16
## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance). Comprehensive arc density expansion accepted.
## Resolves: Gap analysis across all factions and sub-factions
## Methodology: Follows npc_behavior_v30 §5 Arc Emergence State Machine.
##   Each arc has: (A) default, (B) branch-condition transformation, (C) crisis/collapse.
##   Conditioners reference game-state variables (TC, RS, Strain, Stability, Mandate, Coup Counter, WR, Certainty, Scar count).
##   Cross-NPC conditioners specify when one NPC's arc triggers a transition in another.
##   Environmental conditioners bind arcs to world-track thresholds.

---

## PART I: METHODOLOGY REFERENCE

### Arc Structure (canonical from npc_behavior_v30 §5)

Every arc profile defines:
- **Branch condition:** the game-state trigger(s) that move the NPC from one arc state to another
- **Conviction shift:** what changes in the NPC's primary/secondary Conviction
- **Resonant Style shift:** what changes in which attacks are effective
- **Behavioral consequence:** how the Priority Tree and institutional behavior change
- **Risk:** what the arc transformation costs or threatens

### Conditioner Types

| Type | Example triggers | Mechanic |
|------|-----------------|---------|
| **Scar-based** | 1/2/3 Scars from decisive RS contests | §3.3 Scar accumulation table |
| **Environmental** | RS ≤ 40, TC ≥ 65, Strain ≥ 7 | World-track thresholds |
| **Political** | Faction Mandate collapse, Coup fires, Seizure succeeds | Faction stat events |
| **Relational** | PC Knot at Close, Disposition ≥ +4, NPC death among Knotted | Knot/Disposition mechanics |
| **Generational** | Longevity roll failure, successor activation | Proposed ED-567 mechanic |
| **Cross-NPC** | NPC A's arc triggers arc event in NPC B | Named NPC interdependence |
| **Thread-state** | TS threshold crossing, Coherence crisis, Gap in home territory | Thread mechanics |
| **Obligation** | Obligation violated by faction, Obligation honored publicly | Social contest §6.1 |

---

## PART II: FILLED ARC SKELETONS (EXISTING NPCS WITH INCOMPLETE ARCS)

---

### Almud Almqvist — Full Arc Expansion

**Existing:** Arc A (Reformer), Arc B (Fortress), Arc C (Overthrown) — present but thin.

---

#### Arc A: The Reformer (Branch Condition Expansion)

**Branch condition (complete):** Almud's Certainty reaches 1 OR 0 AND Löwenritter Coup Counter ≤ 1 AND at least one of:
- PC has won a Decisive Contest against Almud via Consequence RS, citing specific RS data
- Almud has witnessed a Thread phenomenon directly (fieldwork/personal scene in RS ≤ 55 territory produces Certainty check: Spirit 4D TN7 Ob 2; success = Certainty −1)
- Torben returns from Altonia with Thread-credible testimony (Torben Loyalty ≤ 2 to Crown AND player has invested in Torben with Evidence RS)

**Arc A transformation mechanics:**
1. Almud issues a private Exemption for Thread practitioners in Crown-held territories. Not a public edict — plausible deniability. Church can file Heresy Investigation regardless, but Crown will not assist.
2. TC −1 immediately (Crown withdrawing cooperation with Church institutional enforcement).
3. Löwenritter Coup Counter +1 if the Exemption becomes public (Ehrenwall views it as Crown losing the theological argument).
4. Almud's Priority 5 updates: "If TC ≥ 50 AND Crown Mandate ≥ 4 → Suppress Church" replaces "Thread Liaison declaration."
5. Almud's Resonant Style primary shifts: Order fades, Reason emerges. Evidence RS becomes effective again (Reason Conviction = evidence-responsive).

**Arc A Decision Fork — The Public Edict:** When Certainty reaches 0, Almud faces a Decision Fork: make the Exemption public (Full Reformer, Coup Counter +1 + TC −2 + Church Excommunication eligible) or keep it private (Half Reformer — benefits Thread practitioners but risks institutional exposure). Player can influence this Fork via Solidarity RS (personal appeal through Knot with Almud) — with a Knot at Close, the appeal tips toward public.

**Arc A secondary trigger — Cardinal of Temperance Testimony:** If the Cardinal of Temperance has reached Scar 1 AND approaches Almud privately (triggered when Temperance's Conviction crisis fires — see Cardinal arcs below), this can substitute for the full RS contest requirement. Temperance delivering internal Church evidence of RS degradation is an Authority appeal Almud cannot dismiss (the source is Church-internal, his Virtue Ethics framework values institutional honesty).

---

#### Arc B: The Fortress (Expanded Behavioral Consequences)

**Missing from existing arc:** What does the Fortress actually DO? The current entry states Conviction doubles down and Authority-only RS, but lacks behavioral specifics.

**Arc B Behavioral cascade (full):**
1. Almud's Priority Tree inserts a new Priority 1.5: "IF any Territory changes controller via non-military means (Treaty, Seizure, Reformation) → Issue Royal Decree targeting that faction: Mandate −1, Standing −1. This is a reflexive institutional response — control must not shift without Crown's endorsement."
2. Almud refuses all private audiences with Thread practitioners and their known associates. PC with Thread-adjacent Belief cannot seek audience without triggering Heresy Investigation filing (Almud's Attention Pool +1 from the request alone).
3. Almud's Beliefs update: Belief 2 replaces with "The Restoration is an existential threat — I cannot distinguish truth from sedition." Any RM Outreach in Crown territory now triggers Priority 2 (Conviction-critical) responses.
4. Ehrenwall Disposition toward Almud: +1 (Fortress Almud validates Ehrenwall's worldview — order is strength). Coup Counter does NOT advance — Almud is behaving as Ehrenwall wants.
5. The Fortress is self-reinforcing: every season Almud maintains Fortress, Crown NPCs at Certainty ≥ 3 gain +1 Certainty (Virtue Ethics Drift). The institution hardens while Almud hardens.

**Arc B exit condition (how to get Almud OUT of Fortress):** The only exit is Ehrenwall. If the player has a Knot at Intimate with Ehrenwall AND Ehrenwall's Solidarity RS is active AND Ehrenwall delivers a Consequence argument ("The Fortress is producing the instability you exist to prevent") — this is the only RS attack Almud can hear in Arc B because it comes through Authority. Ehrenwall is the authority Almud respects.

---

#### Arc C: The Overthrown (Post-Exile State)

**Missing from existing arc:** What does Almud do as an exile? The current entry stops at "Almud becomes an exile."

**Arc C Post-Exile States (three trajectories):**

**C-i: The Abdicant** (Coup Counter 3, Almud Certainty ≥ 2 at exile):
- Almud formally abdicates. He releases Crown legitimacy to Torben.
- Behavior: retires to a monastery or private estate. Thread Sensitivity 28 becomes a quiet development — he starts perceiving, without framework, alone.
- Mechanical: Crown faction continues under Torben/Löwenritter. Almud is removed from political play. BUT: 1/season GM roll d10. On 10: Almud writes a document — a private theological refutation of Solmund doctrine based on his unguided Thread perception. If this document reaches the player (Fieldwork OW Investigation in Almud's location), it is a campaign-altering Evidence artifact (+3 Evidence on any investigation targeting Church theology).

**C-ii: The Pretender** (Coup Counter 3, Almud Certainty 1 at exile, Löwenritter Mandate ≤ 3):
- Almud does NOT accept the coup. He organises a loyalist faction among Masterless Crown units.
- Behavior: Priority Tree shifts to: Priority 1 — Reconstitution (march toward T1). Priority 2 — Recruit (Mandate-building in territories Löwenritter has not fully absorbed). Priority 3 — Diplomacy (seek Hafenmark support — Baralta's Precedent conviction may sympathise with legitimate succession).
- Risk: Pretender war creates Strain +1/season. Almud at Certainty 1 may Collapse to Arc C-iii under sustained military failure.
- Player opportunity: supporting Almud's pretender claim is a legitimate co-victory path variant — Almud restored = Crown faction reinitialised under reformed leadership, TC −3, RS stabilisation commitment possible.

**C-iii: The Broken** (Coup Counter 3, Almud Certainty 0 at exile, Stability ≤ 1):
- Almud's framework has completely collapsed. He no longer functions as a political actor.
- Behavior: withdraws entirely. Certainty 0 → Authority RS only (old framework void). He has no authority to appeal to — every framework has failed him.
- Thread consequence: Thread Sensitivity 28 with Certainty 0 + no framework = unguided Thread contact risk. GM roll at Year-End: d10 ≥ 7 = Almud has his First Leap, alone, without training. This is an ontological crisis event. If unassisted: 40% chance he reaches Coherence 5 (Dissonant) within 2 seasons, creating a wandering NPC who perceives things and cannot render them. If player reaches him (Expedition/Fieldwork in exile location): opportunity to become his framework — teaching him to integrate what he perceives. This is the campaign's most intimate possible arc payoff.

---

### Magnus Vaynard — Arc A and Arc B (Filled)

**Existing:** Arc A (The Scholar), Arc B (The Awakened) — both empty stubs. Arc C (Consumed) has one line.

---

#### Arc A: The Scholar (Full)

**Branch condition:** Default arc. No PC expedition to Varfell's Private Collection. No VTM advancement challenge. Vaynard is an intellect consuming information without transformation.

**Arc A behavior:**
1. Vaynard pursues VTM advancement purely instrumentally (Tribune Intel, Private Collection). No Certainty movement. Consequentialist Pragmatism remains stable.
2. His Priority 2 fires reliably: Intel opportunities always taken before any other action.
3. Vaynard acquires Thread knowledge without Thread perception. He knows facts about Thread without experiencing Thread. This is the most dangerous configuration: competence without wisdom.
4. Arc A stable state: VTM 2–3 reached by Season 8–10 through reliable Intel. No RS care — Varfell's Thread operations (if any) are purely extractive.
5. Framework Drift: TK +0.5/season accumulating, capping at TK 3 without PC interaction. At TK 3: Vaynard is the most theoretically knowledgeable non-practitioner on the peninsula. He attracts Niflhel interest (Niflhel can use his knowledge to build Thread extraction tools — this is the Southernmost supply chain threat from ST-06 fieldwork sim).

**Arc A passive threat conditioner:** Every season Vaynard is in Arc A with VTM ≥ 2 AND no PC contact: Niflhel Arm 4 (the theoretical arm, distinct from the operational arms) advances its agenda. GM tracks a hidden Niflhel-Vaynard Contact clock (0–4). At Contact 4: Niflhel has successfully accessed Vaynard's Private Collection knowledge — campaign-altering intelligence transfer that accelerates Southernmost threat by 4 seasons. Player has 4-season window to intercept (Tribune Spy OW in Vaynard's territory reveals Contact clock ≥ 2).

---

#### Arc B: The Awakened (Full)

**Branch condition:** Thread Sensitivity 14 (Dormant, hidden) crosses 10 → Stirring (30). How does this happen?

Three triggering events (any one sufficient):
1. PC practitioner performs Thread operation targeting Vaynard's configuration at Personal scale (Weaving or Pulling) — Vaynard's dormant sensitivity activates under direct Thread exposure. Spirit check TN 7, Ob 1: success = TS advances from 14 to 22 immediately (partial activation). Repeat exposure pushes to 30.
2. Vaynard spends 2 seasons in T15 Askeheim (the Calamity ground) during an Expedition. Calamity proximity at T15 forces Certainty check AND TS check regardless of prophylaxis. TS advances +8 per season in T15. By Season 2 of T15 exposure: TS 30 (Stirring).
3. Private Collection discovery: if Vaynard accesses a specific artifact (Einhir Thread-active device — placed by GM based on Fieldwork discovery) without practitioner supervision, the device triggers forced TS activation. TS: 14 → 35 in one scene.

**Arc B transformation:**
1. Vaynard begins perceiving Thread configurations. Not deliberately — involuntarily. His Cognition-primary worldview (everything is a hypothesis to test) now applies to Thread data he cannot control.
2. Certainty: 3 → 2 (empirical encounter with Thread reality confirms the hypothesis but destabilises the framework — his model was too neat).
3. Resonant Style: Consequence remains primary. Evidence gains a new vector — he can now cite Thread perception as evidence. This makes him simultaneously MORE persuadable (Thread evidence now hits his Evidence RS) and MORE interesting as a political ally.
4. Behavioral change: Vaynard's Priority 2 updates. Alongside Intel operations: "IF TS ≥ 30 AND Discovery Event roll not yet taken this season → Private Collection use triggers Spirit check for Discovery Event." He is no longer able to study Thread dispassionately — the study studies him back.
5. Framework Drift new source: +1D on all Thread-adjacent investigations (he perceives what he investigates). This makes Vaynard an extraordinary investigator — 2D above normal for any Thread-related fieldwork.

**Arc B secondary emergence — The Collaborator:** If player has built Disposition ≥ +3 with Vaynard in Arc B AND offers genuine Thread education (player has TS ≥ 30 AND spends a scene teaching Vaynard formal Approach Training): Vaynard's Certainty → 1. He begins formal Thread study. VTM and Thread Sensitivity advance in parallel. Within 3 seasons, he reaches TS 35 (Maret Uln level) with Approach Training. This creates a Varfell that can field practitioners, dramatically accelerating Path C and making Varfell+Crown co-victory viable.

---

#### Arc C: Consumed (Full Expansion)

**Branch condition:** Vaynard reaches TS 30+ WITHOUT guidance AND Certainty drops to 0 (empirical worldview cannot integrate what he perceives).

**Arc C cascade:**
1. First unguided Leap in a scene alone — Spirit 4D TN7 Ob 2. On failure: Rendering Crisis begins immediately (Coherence 10 → 5 from unguided contact). On success: brief contact, terrifying, productive. Either outcome advances the Consumed trajectory.
2. Vaynard's Consequentialist Pragmatism: "I will use what I learn." Coherence degradation = he is using what he learns at the cost of his own coherence. He knows this. He continues anyway.
3. Certainty 0: his framework has not been disproved — it has been confirmed. The Thread IS real. And now he cannot stop perceiving it. The confirmation destroys him more thoroughly than disproof would have.
4. Behavioral: Vaynard's Priority Tree collapses entirely. His actions become Thread-compelled rather than politically rational. He takes actions that make no strategic sense because he perceives configurations that require addressing. He becomes an NPC the GM must manage as an agent of the Thread itself, not of Varfell's interests.
5. Vaynard at Coherence ≤ 3 (Fragmented): −1D all social rolls. Cannot execute Consequentialist Pragmatism (requires rational assessment of outcomes). His Leadership Deviation Ob effectively becomes 1 (the institution cannot predict him).
6. Knot strain propagation (§5.0b): TS 30+ in active crisis → Close Knot +1 strain/season to all Knotted NPCs. If Vaynard has a Knot with the PC (likely at Disposition +3): PC takes +1 Coherence strain per session in Vaynard's presence.

**Arc C recovery gate:** The only exit from Consumed is Edeyja. If Vaynard reaches T15 in Consumed state AND Edeyja is in Arc B (Collaboration) AND Edeyja agrees to treat him: Recovery arc begins. Edeyja's TS 75+ provides the framework Vaynard's Reason cannot build for itself. Recovery takes 3 seasons. Vaynard emerges with Certainty 1, Coherence 6, TS 40 — a genuine practitioner, no longer Scholar, no longer Consumed. A third state that has no name yet.

---

## PART III: SUB-FACTION FULL ARC SETS

---

### CARDINAL OFFICERS — Full Arc Profiles

Cardinals activate as independent NPCs during Church Stability ≤ 2. Existing entry (§2.13) gives schism behavior only — no arcs, no Beliefs, no transition mechanics. Expanding all four.

---

#### Cardinal of Fortitude (Templar Order) — Arc Profiles

**Full Stance Triangle:**

| Attribute | Value |
|-----------|-------|
| Name | [Canonical: not named. Propose: Cardinal Gunnar Stark] |
| Primary Conviction | Faith | "The Temple defends what Solmund has sanctified. We are the sword, not the debate." |
| Secondary Conviction | Order | When Faith fails to justify, the institutional chain of command takes over. Stark follows orders from his superiors even when he disagrees with them — until the orders violate what he understands as the Temple's martial purpose. |
| Ethical Framework | Martial Divine Command | Aligned: −1 Ob on any action that physically defends Church territory or personnel. Contradictory: +1 Ob on diplomatic, theological, or administrative actions. |
| Primary Resonant Style | Consequence | Show him that the Templar deployments are producing worse outcomes than restraint — that the military posture is feeding the resistance it claims to suppress. A general who loses faith in his strategy is reachable. |
| Secondary Resonant Style | Solidarity | Stark's soldiers are his family. Any appeal invoking specific Templars — their names, their sacrifices, how they've been used and spent — reaches him where strategic argument cannot. |
| Thread Sensitivity | 0 | Non-practitioner. Active theological prophylaxis. |
| Certainty | 4 | Military piety — faith as discipline, not theology. |
| Leadership Deviation Ob | 3 during schism / 4 during normal Church operations | He subordinates himself to Himlensendt absolutely during stability. |

**Beliefs:**
1. "The Temple serves Solmund. If Solmund's representative on earth orders it, the Temple does it."
2. "A soldier who questions his orders in the field is a soldier who gets his brothers killed."
3. "I have watched the Confessor send men to die for a theology he debates in comfort. I do not debate."

**Arc A: The Instrument (Default)**
- Branch condition: Church Stability ≥ 3. Stark executes Himlensendt's orders without question.
- Behavior: Templar deployments proceed per Church Priority 6 (Templar in PT ≥ 3 Prominent territories). Stark is invisible — he does what he is told.
- Trigger for arc movement: either Church Stability drops to 2 (Arc B) OR Himlensendt enters Arc B (Crisis of Faith) — when the orders stop making theological sense, Stark's instrument status becomes complicated.

**Arc B: The Questioning Sword**
- Branch condition: Church Stability ≤ 2 OR Himlensendt has ≥ 2 Scars publicly known OR player defeats Templar forces in T9 (Himmelenger home territory) AND Stark was present.
- Transformation: Stark's Faith conviction faces the Consequence attack point — is the Temple achieving anything? Certainty: 4 → 3. He begins counting costs that he previously refused to count.
- Behavior: Stark takes 1 independent action per season not directed by Himlensendt. He uses this to: (a) assess the military situation accurately (Tribune Investigate on enemy Military, not Intel from Himlensendt), (b) personally meet with Templar soldiers and listen to their experience on the ground.
- New Belief: "I was told we were winning. I am starting to wonder what winning means."
- Decision Fork trigger: If Himlensendt in Arc C (Confrontation) attempts to order Stark to suppress his own congregation (arrest devout citizens for political reasons), Stark faces a Decision Fork. He cannot suppress people he has sworn to defend. He will disobey that specific order (Leadership Deviation check Ob 3 — he usually succeeds in resisting because his Order conviction supports institutional defiance on grounds of clear harm).

**Arc C: The Schismatic General**
- Branch condition: Church Stability 0 OR Himlensendt's Arc C (Confrontation) becomes public AND Stark independently assesses the situation as institutionally fatal.
- Transformation: Stark splits from Church hierarchy. He does NOT abandon Faith — he splits from the institutional hierarchy on grounds of institutional self-destruction. "The Temple exists to protect Valoria. The Church has become a threat to Valoria. The Temple cannot serve both."
- Behavioral consequence: Stark's Templar units become an independent military force — not Crown, not Church, not Löwenritter. They garrison the most contested territory and refuse to move without a credible justification that serves civilian protection.
- Campaign impact: 2 Templar units (Martial 5, Discipline 6) become a neutral military pole. Any faction can attempt to negotiate Stark's support (Solidarity RS — personal appeal — OR Consequence — show him that supporting your faction protects the most civilians). Stark will not be bribed (he is Order-adjacent — institutional purity matters) but he can be argued.
- Risk: Löwenritter will attempt to absorb the Templars (Ehrenwall sees a military opportunity). Crown will attempt to ally (Almud sees a Church-counter opportunity). Church will attempt to reassert (Cardinal of Justice may try to Excommunicate Stark — which would make Stark a de facto ally of any anti-Church coalition).

---

#### Cardinal of Justice (Inquisitor-General) — Arc Profiles

**Full Stance Triangle:**

| Attribute | Value |
|-----------|-------|
| Name | [Propose: Cardinal Theodric Voss] |
| Primary Conviction | Faith (hardline) | "Solmund's law is exact. Deviation from it is not error — it is transgression. Transgression requires correction." |
| Secondary Conviction | Order | The Inquisition IS the Church's order-maintenance mechanism. If Faith's purity goal conflicts with Order's stability goal, Voss chooses purity. Every time. |
| Ethical Framework | Divine Command (hardline variant) | Aligned: −1 Ob on any investigation, prosecution, or punishment of doctrinal deviation. Contradictory: +1 Ob on mercy, accommodation, or pragmatic exception. |
| Primary Resonant Style | Authority | Voss is himself an authority — he yields only to higher authority within his framework. The Holy See (distant, unreachable), a direct canonical text he cannot reinterpret, or (in extremis) a miraculous event he personally witnesses could move him. No human argument moves him. |
| Secondary Resonant Style | Evidence | His hardline Faith claims to be empirically grounded in Scripture. Evidence that Scripture does not say what he claims it says — documented, authenticated textual evidence — is the only argumentation vector. |
| Thread Sensitivity | 0 | Prophylaxis at maximum. He has seen the consequences of Thread exposure and actively maintains theological inoculation. |
| Certainty | 5 | He is the highest Certainty NPC in the game. First Coherence loss nullified per session. +2D on Faith-aligned actions during schism. |
| Leadership Deviation Ob | 5 | Effectively never deviates from Faith framework. Conviction crisis table rolls still apply at 3+ Scars, but Scar accumulation requires Total Victory via Evidence RS. |

**Beliefs:**
1. "Heresy is contagion. One infected community spreads to three. The cure is always proportionate to the disease."
2. "The Confessor is too gentle. Gentleness is theology's greatest vulnerability."
3. "I have read the documents. There is nothing in the Einhir texts that Scripture does not account for, explain, and warn against."

**Arc A: The Instrument of Purity (Default)**
- Behavior: Voss prosecutes Heresy Investigations systematically. Any named practitioner who appears in a Church Attention Pool at ≥ 3 becomes a Voss target. His investigations are thorough, documented, and procedurally correct. He is not cruel — he is precise.
- Game mechanic: Voss-prosecuted Heresy Investigations use Ob 1 (he is the best investigator the Church has). His Argue pool in tribunal: Cognition 5, Church Domain Expertise +1D, Certainty 5 bonus +2D = formidable. Player faces the hardest possible Tribunal opponent when Voss prosecutes.
- Arc A passive conditioner: Every 4 seasons in Arc A, Voss completes one Structural Investigation on the Thread practitioner network (Evidence Track advancing +2/season automatically from Inquisition resources). At Evidence 8, he has a Structural Finding implicating a named PC-affiliated NPC. This generates an automatic Priority 2 (Heresy Investigation) against that NPC.

**Arc B: The Zealot in Question**
- Branch condition: Voss personally witnesses a Thread phenomenon he cannot explain within his theology. Specifically: a Gap closure (Mending) producing RS +2 in his presence. He perceives the settling (TS 0, but co-movement epistemic auto-effect is perceptible to all). He knows the world improved. He knows it was the act of a practitioner. He cannot integrate this.
- Transformation: Voss does not Believe. But he begins to investigate the phenomenon rather than condemning it. His Evidence-secondary RS activates. He will consider textual evidence from non-canonical sources IF they are authenticated within his scholarly framework.
- Behavior: One Heresy Investigation per season is quietly suspended — not cancelled, just perpetually deferred. He is conducting parallel research.
- New Belief: "Solmund's law is exact. I am examining whether I have been reading it exactly."
- This is extraordinarily dangerous. A Voss who begins to doubt his textual interpretation while retaining his Faith and his Authority RS is a Voss who might find his way to Truth and become its most powerful institutional defender. OR: a Voss who inverts and becomes the most destructive force for the Church — because his perfectionism applied to internal Church corruption would burn the institution down.

**Arc C: The Inquisitor's Inquisition**
- Branch condition: Voss's research produces a Finding he cannot suppress: Church documents HAVE been selectively edited. A 400-year-old canonical text has an Einhir passage removed. The removal is documented in the Church archive. Voss authenticated the document himself. His Evidence RS now attacks his own framework.
- Transformation: Voss turns the Inquisition on the Church. He opens investigations into Himlensendt (who knew?), Prudence (who approved the removal?), Fortitude (who helped cover it?).
- This is the most catastrophic Church event possible — the Inquisitor-General investigating the Confessor. Church Stability −3 immediately. TC −4 (Voss publishes his findings; institutional credibility collapses).
- Behavioral: Voss becomes an independent judicial actor. He will prosecute anyone, any faction, any NPC, for institutional dishonesty. He is not converted to Thread acceptance — he is converted to the proposition that his Church has been lying to itself. He cannot forgive that.
- Player opportunity: Voss in Arc C is paradoxically the best possible ally against Church domination. He will pursue truth regardless of political consequence. A player who provides him with Evidence (Fieldwork Finding, authenticated) can direct his Inquisition anywhere they choose.
- Risk: Voss in Arc C will eventually prosecute the player too if the player has been deceptive in any documented way. He makes no political exceptions.

---

#### Cardinal of Prudence (Tithes/Finance) — Arc Profiles

**Full Stance Triangle:**

| Attribute | Value |
|-----------|-------|
| Name | [Propose: Cardinal Elsa Vorn] |
| Primary Conviction | Order | The Church endures because its institutions endure. Institutions endure because they are funded. Theology is the justification; wealth is the infrastructure. |
| Secondary Conviction | Autonomy | Vorn is the only Cardinal who would survive the Church's collapse — she has contingency plans, personal wealth networks, and diplomatic relationships with Guilds and Schoenland that predate her Church service. If Order fails, she defects. |
| Ethical Framework | Divine Command (institutional variant) | Aligned: −1 Ob on any action that increases Church wealth or institutional stability. Contradictory: +1 Ob on any action that sacrifices Church resources for theological purity. |
| Primary Resonant Style | Evidence | Show her the fiscal data. Specific numbers, documented ledgers, projected deficits. Her framework claims to be reality-grounded (the institution must be funded). Evidence that the institution cannot fund its current trajectory moves her. |
| Secondary Resonant Style | Consequence | Project the consequences of financial ruin. She has already run these numbers. Hearing them stated by someone outside the Church — especially a Guild representative — forces public confrontation with what she privately fears. |
| Thread Sensitivity | 0 | Pragmatic non-interest. She has no theological position on Thread. If Thread practitioners paid tithes reliably, she would probably tolerate them. |
| Certainty | 3 | Pragmatic believer. Faith is institutional habit and social infrastructure. She does not experience it as revealed truth. |
| Leadership Deviation Ob | 1 | Lowest of all Cardinals. She is the most independent operator in the Church. Her institution is finance, not theology. |

**Beliefs:**
1. "A Church that cannot pay its garrison is a Church that will lose its territory. Theology does not pay soldiers."
2. "The Confessor's Heresy Investigations cost more than they generate. I have the numbers."
3. "The Guilds are our natural allies, not our enemies. Someone should tell the Confessor."

**Arc A: The Pragmatist (Default)**
- Behavior: Vorn runs the Church's finances quietly. She is the reason the Church has Wealth 4 instead of Wealth 2 — her Consul actions (Trade/Govern in high-Prosperity territories) consistently outperform other Cardinals' contributions.
- Arc A passive conditioner: Vorn tracks the cost of every Heresy Investigation (1 Wealth/Investigation, from her internal accounting). When total Investigation cost exceeds Church Wealth 3 in a single season, she files an internal objection (no BG effect, but GM plants the information as a Fieldwork Finding for any player who investigates Church finances).
- Trigger for movement: Church Wealth drops to ≤ 1 from combined Heresy Investigation costs + Embassy maintenance + Blockade effects. At Wealth 1: Arc B activates (Vorn can no longer internally manage).

**Arc B: The Administrator in Conflict**
- Branch condition: Church Wealth ≤ 1 OR Church Stability ≤ 2 AND Himlensendt overrides Vorn's budget objections twice in one season.
- Transformation: Vorn's Autonomy secondary activates. She begins making independent financial arrangements — quietly, deniably. Guild Favour +1 in T9 (she is diverting Church tithe funds to Guild accounts as insurance against Church collapse). This is embezzlement on a sovereign scale. It is also the most rational thing she could do.
- Behavior: Vorn's Priority 7 updates: "DEFAULT → Secret tithe diversion to Guild accounts." This accumulates as Guild Favour +1 every 2 seasons. At Guild Favour 5 in T9: Guilds have enough leverage over Vorn to threaten her with exposure. Guilds gain a Strong Hook on Vorn.
- Player opportunity: discovering Vorn's embezzlement (Fieldwork, Evidence Track threshold 5 on "Church internal finances") gives the player a Weak Hook. Using it: Vorn can be directed to redirect funds to player-allied causes (RM community support, practitioner shelter) rather than Church purposes. She is incorruptible toward ideology — she is perfectly corruptible toward financial self-preservation.

**Arc C: The Defection**
- Branch condition: Vorn's embezzlement is discovered by Cardinal of Justice (Voss Arc A passive investigation) OR Church Stability reaches 0.
- Transformation: Vorn defects. She formalises her Guild relationships, transfers remaining Church assets she controls to Guild accounts, and steps down from Cardinal office.
- Behavioral: Vorn becomes a Guild sub-NPC — the most financially sophisticated person in the Guild network, with detailed knowledge of Church operations.
- Campaign impact: Church Wealth −2 immediately (the asset transfer). Church loses its most competent administrator. Subsequent Church Accounting phases are more vulnerable to Wealth depletion. Vorn as a Guild NPC gives Guilds Priority 2 intelligence access to Church operations — the Guilds know exactly what Church can and cannot afford.
- Risk for players who ally with Vorn: she will not sacrifice herself for anyone. If exposure threatens her, she will redirect whatever Hook the player holds toward someone else. Vorn's Autonomy is real — she survives regardless.

---

#### Cardinal of Temperance (Scholar) — Arc Profiles

**Full Stance Triangle:**

| Attribute | Value |
|-----------|-------|
| Name | [Propose: Cardinal Sigrid Kald] |
| Primary Conviction | Reason | Truth is discoverable. Solmund's revelation and empirical investigation should converge if both are correctly practised. She has spent her life finding the convergences. She is running out of places to look. |
| Secondary Conviction | Faith | Kald would not be a Cardinal if she didn't believe. She believes. But she believes in what she has investigated and found credible — not in what she has been told and accepted. The distinction is critical. |
| Ethical Framework | Divine Command (scholarly variant) | Aligned: −1 Ob on any action that advances knowledge or AER maintenance. Contradictory: +1 Ob on any action that suppresses evidence or prevents scholarly access. |
| Primary Resonant Style | Evidence | Show her specific, documented, authenticated facts she cannot explain within her theological framework. She is looking for these already. She will receive them as gifts rather than attacks. |
| Secondary Resonant Style | Authority | Within her framework: a canonical text she has not seen, authenticated by multiple chains of custody, citing Thread phenomena in non-condemnatory terms, would be Authority that forces framework revision. She knows such texts may exist — the Einhir archive at T15 is her greatest unresolved question. |
| Thread Sensitivity | 8 | Undiscovered. Her scholarly engagement with Thread-adjacent texts has produced micro-TS development she has not attributed correctly. She occasionally perceives things she explains as spiritual intuition. |
| Certainty | 3 | Precisely balanced. She holds Faith and Reason in an equilibrium that requires constant maintenance. Any strong evidence in either direction tips the balance. |
| Leadership Deviation Ob | 2 | She operates independently when scholarly integrity requires it. |

**Beliefs:**
1. "Solmund's revelation and the natural world must agree. When they appear not to, I have been reading one of them incorrectly."
2. "The Einhir texts that the Church condemned in the 4th Century — I have not been permitted to examine them. This troubles me more than I allow."
3. "Thread Sensitivity appears in our congregation with statistical regularity. I have been recording the cases for eleven years. I have not told Himlensendt."

**Arc A: The Investigator (Default)**
- Behavior: Kald pursues AER maintenance, Temperance declarations, scholarly projects. She is the least militaristic Cardinal — her actions are consistently non-invasive and knowledge-oriented.
- Arc A passive: Kald has an 11-year dataset on Thread Sensitivity prevalence in Church congregations. This dataset exists as a Structural Finding available to any player who investigates Church archives (Evidence Track 8, Fieldwork at T9, Research action, Depth 3 — the dataset is buried). The dataset proves Thread Sensitivity is heritable, widespread, and not pathological. If this Finding reaches Himlensendt: Arc B for Himlensendt (Authority RS trigger — the Cardinal of Temperance IS an authority he must hear).

**Arc B: The Crisis of Evidence**
- Branch condition: Kald's TS reaches 10 (fieldwork or direct Thread exposure) AND she performs a Thread-Read involuntarily (at TS 10, perceptive encounters begin without deliberate Leap — she perceives Thread configurations during scholarly work). OR: Player provides Kald with authenticated Einhir text evidence.
- Transformation: Kald's framework breaks — not toward rejection of Faith but toward integration of Thread reality within a revised framework. Her Reason conviction was always leading here. She has arrived.
- Behavior: Kald drafts a private theological treatise: "Thread Sensitivity as Solmund's Gift: A Reconciliation." She shows it to no one yet. She is building the case from within.
- Arc B trigger for Himlensendt: If Kald shares the treatise with Himlensendt AND the player has built the groundwork (Evidence RS, prior Scars on Himlensendt) — the combination of an internal Church scholarly authority presenting Thread-integrated theology creates the Authority trigger needed for Himlensendt's arc shift. This is the canonical path to Himlensendt's Arc B that does not require the player to defeat him in direct contest.

**Arc C: The Theologian at the Boundary**
- Branch condition: Kald presents her treatise publicly (Kald's Conviction crisis: 3 Scars from internal Church pressure to abandon research, OR Voss Arc A passive investigation uncovers the dataset).
- Transformation: Kald publicly advocates for Thread acceptance within Church doctrine. She does not leave the Church — she contests it from within.
- Campaign impact: Church Stability −2 (a Cardinal publicly advocating heresy). TC −2. But AER +1 (Altonian academic community, which has Thread-aware scholars, perceives Kald's work positively).
- Risk: Cardinal of Justice (Voss) opens Heresy Investigation against Kald. If Voss is in Arc A (Instrument): Investigation proceeds and Kald is convicted (Church expels her). If Voss is in Arc B (Questioning): he delays the investigation and reads the treatise himself — with potentially transformative consequences.
- Player opportunity: Kald in Arc C is the only Church NPC who can publicly validate Thread practice with institutional standing. Her endorsement does not stop Church persecution (Himlensendt or Voss will override), but it creates a Faction Fracture — a formal Church sub-faction (the Temperance Order) that tolerates Thread practice and can provide safe harbour in Church-adjacent territories.

---

### LÖWENRITTER — Full Arc Expansion

---

#### Lisbeth Ehrenwall — Full Arc Profiles

**Existing:** Conviction and RS defined. Arc stated as 2+ Arcs implied but not specified.

**Full Stance Triangle (complete):**

| Attribute | Value |
|-----------|-------|
| Thread Sensitivity | 0 (confirmed per ED-392 resolution) |
| Certainty | 5 (confirmed per ED-393: Deed-logic worldview is self-reinforcing) |
| Coherence | N/A |

**Beliefs:**
1. "Valoria endures, whatever the cost — I will ensure it."
2. "Almud is faltering — I must be ready to act when he cannot."
3. "The Riskbreakers exist for the situations where honour is a luxury."
4. (Hidden) "I have counted six kings who failed Valoria. I am the seventh attempt at a solution."

**Arc A: The Watchman (Default)**
- Branch condition: Coup Counter ≤ 1. Ehrenwall serves Crown loyally. She is exactly what she says she is: the sword that remains sheathed because it trusts its wielder.
- Behavior: Priority Tree executes as specified. No independent action. No deviation. She is the most predictable NPC in the game when Coup Counter is low — because she has CHOSEN predictability. It is not passivity; it is discipline.
- Arc A passive conditioner: Every season, Ehrenwall evaluates Almud against 6 criteria (documented in her private journal, discoverable via Fieldwork Evidence Track 5 in T14):
  1. Crown Stability maintained
  2. IP below 50
  3. No Church territory acquired without Crown response
  4. Torben protected from Altonian influence
  5. Parliament functioning (PI ≥ 5)
  6. At least one military victory or deterrence achieved per arc
  Each criterion failed: Coup Counter advances +0.5. This reveals the Coup Counter's internal logic — it is Ehrenwall's assessment, not random.
- Trigger for Arc A exit: Coup Counter reaches 2 (she has evaluated Crown as failing on 4 of 6 criteria over the game's arc).

**Arc B: The Instrument at the Edge**
- Branch condition: Coup Counter = 2. Ehrenwall has committed mentally to the possibility of the coup. She is now preparing without deciding.
- Transformation: Order conviction remains primary. Autonomy secondary activates — she begins taking small independent actions not directed by Almud. These are individually justifiable; collectively they position Löwenritter for the coup she has not yet committed to.
- Behavior:
  1. Ehrenwall begins moving Löwenritter units toward T1 adjacency — "border patrol exercises." BG effect: Löwenritter units in T14 and T3 without hostile intent (within their existing territory). This is legal and unremarkable.
  2. She makes private contact with Torben. Not seduction of loyalty — she is assessing whether Torben can lead. This is a Fieldwork Intelligence gathering action by the GM, not a player-visible event. (If player has Surveillance on T14: Tribune Spy may discover the contact.)
  3. Her Leadership Deviation Ob: 2. But in Arc B, the Deviation checks are at Ob 1 (she has partially committed — the institution is starting to follow the direction she is already leaning).
- Player opportunity: a player who discovers the Arc B positioning and intervenes — presenting Ehrenwall with a Consequence argument ("The coup will produce the instability you exist to prevent") — can push Coup Counter back to 1. She IS reachable via Consequence RS. The argument must be specific and backed with evidence (Consequence RS requires projected outcomes). Solidarity RS is secondary but accessible via Knot at Close.

**Arc C: The Regency (Post-Coup)**
- Branch condition: Coup Counter = 3. Coup fires.
- Transformation: Ehrenwall's Order conviction FULLY activates — she executes the coup as a constitutional act. "I am not overthrowing the Crown. I am fulfilling the Crown's obligation when the Crown cannot."
- Behavioral cascade (full):
  1. Ehrenwall takes Crown faction administration. All Crown cards become Löwenritter-administered.
  2. Torben evaluation: if Torben Loyalty ≥ 4 AND Torben Conviction has emerged (not blank): Ehrenwall installs Torben as a figurehead regent with genuine authority. She serves as Lord Marshal — Torben rules, she enforces. If Torben Loyalty < 4 OR Conviction blank: Ehrenwall governs directly. Torben is protected but not empowered.
  3. Ehrenwall's Priority Tree post-coup:
     - Priority 1: Reconstitute Parliament (PI 0 → 4, 4+ seasons).
     - Priority 2: Secure Torben's succession (Torben Loyalty ≥ 6 required for clean Regency victory).
     - Priority 3: Suppress all non-LR military presence in former Crown territories.
     - Priority 4: Maintain TC < 50 (Church growing in power is the second existential threat she has spent her career opposing).
  4. Ehrenwall as Regent: Leadership Deviation Ob drops to 1. The institution IS her now. Nothing deviates from her assessment of what Valoria requires.
- Arc C secondary trajectory — The Failed Regency: If LR Stability drops to ≤ 1 within 4 seasons of coup (Church counterattacks, Varfell opportunism, Hafenmark constitutional challenge), Ehrenwall faces a Decision Fork: double down (military consolidation) OR release (nominate Torben fully and step back). With 3+ Scars from post-coup political defeats: she releases. This is her most surprising possible act — the martial leader who chooses to limit her own power when the alternative is destroying what she fought to protect. This is Soldier's Honor resolving itself through restraint, not force.

---

#### Torsvald (Riskbreaker) — Full Arc Profiles

**Context:** Riskbreakers are the Löwenritter's covert operations arm — the Consequence-tolerant operatives who "exist for the situations where honour is a luxury." Torsvald is the named Riskbreaker, TS 20+.

**Full Stance Triangle:**

| Attribute | Value |
|-----------|-------|
| Primary Conviction | Autonomy | "I carry out orders. But I decide how." The Riskbreakers are not directed — they are tasked and trusted. Torsvald interprets missions at the operational level with total freedom. |
| Secondary Conviction | Continuity | If Autonomy fails (he is constrained, captured, compromised), Torsvald defaults to the work. The mission outlasts the operative. |
| Ethical Framework | Martial Honour (Löwenritter, modified) | Aligned: −1 Ob on actions that achieve mission objectives by any means. Contradictory: +2 Ob on actions that harm civilians directly. He has a line. It is further than most people's. |
| Primary Resonant Style | Consequence | Show him that his operations are producing worse outcomes than alternatives — that the Riskbreaker approach to a problem is creating the threat it's supposed to solve. Operationally pragmatic minds respond to demonstrated failure. |
| Secondary Resonant Style | Evidence | Present specific operational intelligence about his network's compromises — Niflhel infiltration of a Riskbreaker cell, Church surveillance that has been two steps ahead. His operational pride is the entry point. |
| Thread Sensitivity | 20+ (active, hidden) | He has perceived Thread phenomena during operations in the Southernmost adjacent zones. He calls it "reading the ground." He does not have a framework for what he experiences. |
| Certainty | 2 (Skeptic) | Operational awareness of Thread reality — he has seen too much to dismiss it and too little to integrate it. He operates empirically: what works, not what it means. |
| Leadership Deviation Ob | 1 | He is the most operationally independent NPC in the game. Ehrenwall tasks him and looks away. |

**Beliefs:**
1. "Every mission I accept, I commit to fully. Every commitment costs something. I keep a running count."
2. "The Southernmost is not an absence. It is a presence that doesn't want to be seen."
3. "I have done things that would end Ehrenwall's career if she knew. She knows. She doesn't ask."

**Arc A: The Operative (Default)**
- Behavior: Torsvald executes Löwenritter covert objectives — intelligence gathering, targeted disruption of rival operations, specific personnel actions (not assassination without direct order, but everything short of it).
- Arc A passive conditioner: Torsvald's TS 20+ is developing. Every Southernmost-adjacent operation (T13, T15 vicinity): Spirit check TN 7 Ob 2. Success = TS advances +1. Failure = no change. At TS 30 (Stirring): Arc B conditions are met.
- Trigger: TS crosses 30 OR player makes contact through Investigation (finding Torsvald's operational trail via Fieldwork Evidence Track in Niflhel-active territories — Torsvald and Niflhel have overlapping operational zones in T6 and T13).

**Arc B: The Operative Who Sees**
- Branch condition: TS ≥ 30 AND (either) direct Thread exposure during operation OR player reveals Torsvald's TS development to him explicitly.
- Transformation: Torsvald begins perceiving Thread configurations during operations. This is not mystical to him — it is data. He processes it as intelligence. "The configuration in T13 has been disturbed. Someone worked on it from the inside. That's not Niflhel — Niflhel doesn't have practitioners. It was Restoration."
- Behavior: Torsvald becomes the most dangerous intelligence asset in the game — an operative with Thread perception who reads operational fields at Thread depth (Fieldwork Investigation Depth 3 auto-access because he perceives Buried-depth Thread data as normal environmental reading).
- New capability: Torsvald can provide Thread-verified intelligence on any territory he has operated in within 2 seasons. This intelligence is Verified tag — the most reliable possible quality.
- Decision Fork: Torsvald discovers Niflhel's Southernmost Thread extraction operation (the supply chain from ST-06 fieldwork sim). He now has Thread-verified evidence of what Niflhel is doing in T15. Does he: (a) report to Ehrenwall (operational duty), (b) report to the player if they have a Knot (relational duty), (c) use the knowledge operationally to bargain with Niflhel (Autonomy conviction).

**Arc C: The Riskbreaker at Risk**
- Branch condition: Torsvald's Thread exposure produces 3 Discovery Events (his TS 30+ triggers Discovery Events per threadwork §2.3 Spirit check during Private Collection use). After 3 Discovery Events without formal Thread training: Coherence begins degrading.
- Transformation: Torsvald is experiencing what Vaynard experiences in Arc C but without the scholarly framework — and with the operational discipline to function despite it. He compartmentalises. He operates. The Coherence degradation shows in operational choices that are slightly wrong — excellent tactics, but occasional moments of perceptual overlay where Thread and tactical reality blur.
- The risk: Torsvald in Arc C makes one major operational error per campaign arc — a miscall that costs someone their life or a mission its objective, because he saw a Thread configuration and responded to that rather than physical reality. The GM determines the error. The player cannot prevent it if they have not found Torsvald and offered Thread education.
- Player intervention: offering Torsvald formal Approach Training (same as Vaynard Arc B) — if player has TS ≥ 30 AND has established Knot at Close with Torsvald — creates the only clean resolution. Torsvald trained is one of the most formidable NPCs in the game: operational discipline + Thread perception + investigative intelligence + full Löwenritter tactical asset.

---

### RESTORATION MOVEMENT — Expanded Arc Set

---

#### Yrsa Vossen — Full Arc Expansion

**Beliefs (complete):**
1. "Power is not taken — it is grown. We grow it in every household where we are trusted."
2. "The Church has made Thread practice heresy. The same Church once made literacy heresy. We know how this ends."
3. "Violence is the tool of the powerful — the movement wins through community, not force."
4. (Hidden) "If Hann goes further than I have asked him to go, I will have to choose between the movement and him. I am not ready for that choice."

**Arc A: The Organiser (Default)**
- Behavior: Vossen builds RM Presence in low-PT territories through community outreach, practitioner protection, and social fieldwork. Her Rawlsian framework generates Presence markers at +1 adjacent territory per season when Stability ≥ 3.
- Arc A passive: Vossen's Leadership Deviation Ob = 2 but her institution is decentralised — cells operate semi-independently. Every 3 seasons: GM roll d6. On 6: one cell takes an action Vossen did not authorise (Hann's Autonomy secondary expressing itself at the cell level). This may be beneficial (cell provides intelligence) or disruptive (cell's action triggers Church AP accumulation). Vossen cannot consistently control what the cells do.

**Arc B: The Strained Leader**
- Branch condition: Hann takes an unauthorised violent action AND it becomes public (Church AP +3 in the relevant territory, Vossen's movement loses 2 Presence markers) OR Church crushes 2 RM cells in one season AND RS ≤ 50 (the world is failing and the peaceful approach isn't working fast enough).
- Transformation: Vossen's Equity-primary Conviction is being tested. She has always said violence is the powerful's tool. She is now confronting evidence that the powerful are using it effectively and she is not. Her Solidarity RS becomes primary vulnerability: the communities depending on her cannot afford her principled pacifism if they are being disappeared.
- Decision Fork: "Do I ask the movement to take risks it did not sign up for?" — a formal decision point where the player, if they have a Knot with Vossen, can influence whether she shifts toward allowing targeted defensive violence or remains committed to her founding principle. Both are principled choices; both have mechanical consequences.
- If she shifts toward defensive violence: Continuity secondary activates. She is no longer Equity-primary — she is now a leader doing what must be done. The movement gets operationally effective AND loses its moral authority in the territories that valued it. Presence marker spread rate: +1 (effectiveness) −1 (credibility loss) = neutral net but different distribution. She gains operational cells and loses cultural roots.
- If she holds: Solidarity RS intensifies. She becomes reachable only through the communities themselves — players who build relationships in RM-connected territories can channel community pressure through Vossen's Solidarity RS to produce specific outcomes.

**Arc C: The Legacy**
- Branch condition: Vossen is captured (Church Heresy Investigation succeeds, Tribunal guilty) OR Vossen is killed in a Niflhel operation targeting RM leadership OR Hann's operational divergence produces a schism (Hann leaves with half the cells, Vossen retains the cultural core).
- Transformation: The movement continues without Vossen in a form she shaped but can no longer control.
- C-i: Captured Vossen — The RM's most powerful moment. A public trial of the movement's founder produces a Solidarity RS crisis for EVERY NPC who has Disposition ≥ +1 with Vossen (per companion_specification §6.3). All those NPCs receive a mandatory Scene Slate entry — the player experiences 5–7 NPCs simultaneously confronting what Vossen meant to them. The trial itself is a Grand Contest (Voss prosecuting, player defending, maximum stakes). Vossen's conviction produces TC +1 (Church authority demonstrated). Her acquittal (player wins Total Victory) produces TC −3 (Church authority challenged at its own institution) AND Vossen's Solidarity RS becomes accessible to the player permanently — she is deeply Knotted now.
- C-ii: Killed Vossen — Death cascade (combat §13.3) fires. All NPCs Knotted to Vossen: Knot rupture, Disposition toward killer −3. Hann becomes RM leader. But Hann's Autonomy secondary means his leadership is operationally effective and ideologically less coherent — the movement fragments into cells that share goals but not methods. Each cell becomes a separate NPC actor with its own Priority Tree (simplified: Autonomy primary, Equity secondary for each).
- C-iii: Schism — Vossen leads the cultural wing (Presence markers + community relationships). Hann leads the operational wing (covert cells + intelligence network). They do not oppose each other — they disagree on method. The player can work with either or both. Co-victory Hafenmark+RM requires Vossen's cultural wing specifically (the Solidarity RS pathway). Varfell+RM co-victory can proceed with either wing.

---

#### Aldric Hann — Full Arc Expansion

**Arc A: The Infrastructure (Default)**
- Behavior: Hann builds RM logistics — safe houses, supply routes, communication networks. He is the reason cells survive — Vossen's inspiration keeps people committed; Hann's organisation keeps them alive.
- Arc A passive: Hann's Circles in logistics and street-level networks generate 1 Intelligence Finding per 2 seasons as a passive effect (he hears things through the network). These Findings are available to any player who establishes contact with Hann (Fieldwork Interview, Disposition ≥ +1, Evidence Track +2 per contact scene).

**Arc B: The Operator**
- Branch condition: 2 RM cells are compromised in one season (Niflhel infiltration OR Church AP ≥ 6) AND Vossen refuses to escalate AND Hann's Autonomy conviction overrides loyalty.
- Transformation: Hann begins running operations Vossen has not authorised. These are not violent — they are intelligence operations, supply interdiction (disrupting Niflhel's supply chain through RM's own network), and pre-emptive cell exposure prevention (moving compromised members before Church arrests them). Operational effectiveness is real. But each operation Hann runs without Vossen's knowledge adds +1 strain to their relationship.
- At strain 3: Vossen discovers Hann's independent operations. The scene that follows is mandatory (companion_specification §6.2 equivalent): a reckoning where both their Beliefs are stated fully. Player can intervene (Solidarity RS to both simultaneously — a Joint Contest that the contest system doesn't formally handle; proposed as a new contest type: Mediation, resolving two opposed parties rather than defeating one).

**Arc C: The Fractured Operator**
- Branch condition: Vossen and Hann's relationship strain reaches 5 AND one of Hann's operations directly contradicts Vossen's stated principles (defensive violence, even if justified).
- Transformation: Hann separates. Not with hostility — with clarity. "I love what she built. I cannot keep building it her way."
- Behavioral consequence: Hann's cells become the RM's intelligence arm, formally independent of the cultural wing. Hann's Priority Tree simplifies: Priority 1 = cell survival; Priority 2 = intelligence superiority over Church Inquisition; Priority 3 = Autonomy preservation (no faction subordination).
- Hann as independent NPC: he is recruitable by any faction via the standard §9.5 recruitment procedure. His Ob: Disposition toward any institutional faction (Crown, Church, Hafenmark) = −3 (ideological hostility), meaning Ob = floor(−3÷2)+1 → Ob minimum 1. But his Autonomy makes him recruitable at any Ob — he will work with anyone who respects his operational independence and does not demand institutional loyalty. A player who recruits Hann gains: intelligence on Church Inquisition operations (1 Verified Finding per season), access to RM logistics network (Expedition time −1 per scene in RM-active territories), and the most effective covert operator available outside Niflhel.

---

### SOUTHERNMOST WARDENS — Expanded Arc Set

---

#### Edeyja — Arc B Expansion (fuller specification)

**Arc B: The Collaboration — Full trigger sequence:**

**Stage 1 — Access (WR 1):** Player reaches T15 via Expedition (Tribune Outward Expedition, Ob 2, multiple seasons). First contact with Edeyja is not warm. She evaluates competence. The evaluation scene is a Fieldwork Investigation in T15 — but the investigation target is the player (she is reading them). GM runs Edeyja's Appraise roll vs player's Thread-relevant attributes. Failure: she dismisses them. Success: she acknowledges them. OW: she shows them one thing they could not find themselves.

**Stage 2 — Trust (WR 2):** Player must demonstrate Thread competence that Edeyja can evaluate. Evidence RS trigger: the player performs a Thread operation in T15 in Edeyja's direct observation. The operation need not succeed — but it must be real (genuine Leap attempt, TS ≥ 30 required, otherwise Edeyja perceives the pretension and Disposition −2). If the Leap succeeds: WR +1. If OW: WR +2 (she has seen something she has not seen from an outsider before).

**Stage 3 — Collaboration (WR 3):** Edeyja shares specific knowledge: the Locked Zone's structure, the Einhir site network, the three remaining wardens' locations, the mechanism by which the Calamity damage can (theoretically) be reversed. This is campaign-altering Intelligence (Structural Finding, Evidence Track 8, Thread-verified tag).

**Stage 4 — The Teaching (WR 4):** Edeyja offers formal training. TS growth at +5/season while under her instruction (the fastest possible TS advancement). A practitioner who spends 2 seasons under Edeyja's instruction reaches TS 50 (Deep Active) from any starting TS ≥ 30. This is the mechanical path to the highest practitioner capability in the game.

**Arc B Ongoing conditioner — Warden death:** One additional warden dies for every 2 seasons that T15 faces Thread phenomena at RS ≤ 40 (Fractured band Monstrous Incursion risk). At Warden count 0 (Edeyja alone): Arc C trigger fires regardless of WR level.

---

#### The Remaining Wardens — Named Sub-NPCs

**Three wardens beyond Edeyja are referenced but not named. Providing full profiles for 2; the third remains intentionally blank (the one the player never meets, whose death is the campaign's first tangible warden loss).**

---

##### Warden Orm (Second Senior Warden)

| Attribute | Value |
|-----------|-------|
| Primary Conviction | Continuity | The work. Only the work. He has been at the Southernmost for 31 years. He does not know what he would do elsewhere. |
| Secondary Conviction | Equity | He grew up in a fishing village. The people who suffer most from the Calamity's boundary effects are not the powerful factions — they are the coastal communities. He does not say this often. |
| Thread Sensitivity | 60 | Second only to Edeyja. He perceives configurations she cannot reach because his perception is less structured — he feels the substrate's mood rather than reading it. Complements Edeyja's technical precision. |
| Certainty | 0 | Thread reality is the only reality. He has not thought about Solmund in twenty years. |
| Resonant Style | Evidence | Show him specific RS data — the numbers, the drift rates. His worldview is calibrated to exact metrics. |
| Leadership Deviation | N/A | Answers to Edeyja and to the work. No other authority. |

**Arc A: The Anchor**
- Orm is the Southernmost's continuity when Edeyja is occupied with players. He runs the daily Gap maintenance — Mending 2–3 Micro-Gaps per season as baseline operational output. His Mending pool (Spirit 5 × 2 + Thread History + TPS 6) = 19D — he succeeds on almost everything at Ob 2–4.
- Arc A passive output: Orm's Mending generates RS +0.55/season (same rate as player practitioner, established in ST-10 sim). Without Orm: RS declinesbyline 0.55/season faster. His death accelerates Rupture by 7 seasons if not replaced.

**Arc A conditional:** If player reaches WR 3 (Edeyja sharing knowledge), Orm becomes accessible. His Evidence RS is reachable — he will test the player with specific Thread questions before trusting them.

**Arc B: The Exhausted**
- Branch condition: RS ≤ 35 AND Warden count has decreased to 2 (one warden already dead) AND Orm has been running solo maintenance for 3+ seasons.
- Transformation: Orm's Continuity conviction has been stripped of its hope. He continues the work but has stopped believing it will matter. His Coherence: 9 (starting) → 7 (sustained grief/exhaustion). He makes one unusual operational decision per season that reflects this — sometimes brilliantly adaptive (exhaustion strips pretense and his perception is raw), sometimes catastrophically miscalculated.
- Player access: Solidarity RS (requires Knot at Close with Orm — achievable only via Stage 3 Edeyja access) can arrest Arc B. The appeal: "The work matters. We are here because the work matters." Solidarity + Continuity is the exact resonance required.

**Arc C: The Last Stand**
- Branch condition: Warden count = 1 (Edeyja alone) OR RS ≤ 20.
- Transformation: Orm chooses where to die. He walks to the most active Gap in T15 and performs a continuous Mending arc — permanent contact, no breaks, Coherence sacrificed to hold the Gap closed for as long as possible. This is a narrative death, not a combat death. The departure scene fires as the player watches.
- Campaign impact: Orm's death-Mending seals one Catastrophic Gap permanently (requires no further maintenance — the sealing is complete). RS +5 permanent. But the Gap sealed is the one Orm specifically judged most dangerous — which may not be the one the player would have chosen. A player who has built the Knot with Orm can request a specific Gap. Otherwise: Orm chooses.

---

### NIFLHEL — Named Arm Operatives

Niflhel's four-arm structure has no named NPCs beyond the collective. Providing one named operative per arm — the NPC the player encounters when Niflhel interactions become personal.

---

#### The Quartermaster (Arm 1 — Finance and Supply)

| Attribute | Value |
|-----------|-------|
| Name | Geirr Soln (never uses this name professionally; known as "the Quartermaster") |
| Primary Conviction | Autonomy | "I am not affiliated. I provide services. That is the entire relationship." |
| Secondary Conviction | Continuity | He keeps running because systems keep running. The Niflhel supply chain is his life's technical work. He cares about its elegance. |
| Thread Sensitivity | 0 | No interest or exposure. |
| Certainty | 4 | Pragmatic conventional piety — enough to operate without suspicion in Church territories. |
| Resonant Style | Consequence | Show him that his supply chain is producing operational failures that he hasn't accounted for. His professional pride is attached to the supply chain's effectiveness, not to any outcome it produces. |
| Leadership Deviation | N/A — individual operative, reports to Arm 1 directorate |

**Arc A: The Service Provider**
- Contact trigger: Player's Fieldwork investigation reaches Evidence Track 5 on Niflhel's supply chain (ST-06 fieldwork sim finding). At Evidence 5: player identifies the Quartermaster as the contact point. Approach requires Niflhel contact protocol: Investigation-triggered (Tribune Spy OW → Niflhel makes contact next season per prior session's proposed rule).
- Behavior: The Quartermaster will provide exactly what he is asked for at market rates. He will not volunteer information. He will not participate in anything that compromises his operational infrastructure. He is a professional.

**Arc B: The Professional Confronted**
- Branch condition: Player provides the Quartermaster with Verified Evidence that his supply chain is delivering Thread-extraction equipment to the Southernmost (the Altonian-labeled goods finding from ST-06). The Consequence RS trigger fires: his supply chain is producing a consequence he did not account for — accelerated RS decline potentially destroying the infrastructure his supply chain relies on.
- Transformation: The Quartermaster does not abandon Niflhel. But he becomes willing to negotiate what he will and will not supply. He will not supply Thread-extraction equipment for any client. This creates a fracture within Arm 1 — the directorate did not authorise this decision.
- New access: The Quartermaster will trade operational information (what Niflhel is doing in specific territories) in exchange for the player providing him with RS data (he is now tracking RS as a professional risk indicator). This creates an intelligence relationship — not loyalty, not alliance, but mutual usefulness.

**Arc C: The Defector**
- Branch condition: Arm 1 directorate overrides the Quartermaster's supply restriction AND continues delivering Thread-extraction equipment. He has made a professional judgment; his directorate has overruled it. He has two choices: comply or leave.
- Transformation: He leaves. Quietly. Takes nothing that isn't his. He does not report Niflhel's operations to any faction — that would be a betrayal of professional standards he genuinely holds. But he is no longer a Niflhel operative.
- Player access: A Quartermaster who has left Niflhel is recruitable (§9.5 standard recruitment, Ob 1 — he has no current faction Disposition). His value: complete operational knowledge of Niflhel Arm 1's supply network, delivery schedules, and client list. This is campaign-defining intelligence that can expose every Niflhel operation currently running.

---

#### The Quiet One (Arm 2 — Operations/Thread Extraction)

| Attribute | Value |
|-----------|-------|
| Name | Unknown. Operatives in Arm 2 use no names. Known only by their operational signature. |
| Primary Conviction | Autonomy | Mission, completion, extraction. No ideology. No sentiment. |
| Secondary Conviction | [None — Arm 2 operatives have no fallback. They are the Niflhel arm designed to have no conscience. When Autonomy fails: they fracture into independent survival.] |
| Thread Sensitivity | 35 (active practitioner — this is why Arm 2 can operate Thread-extraction) |
| Certainty | 1 | Full Thread awareness. Operational clarity — Thread is a resource, not a reality. The most dangerous practitioner Conviction possible. |
| Resonant Style | Evidence | Show them that the Thread they are extracting is responding — that the substrate is registering their operations as damage, not as neutral extraction. Thread evidence (from Edeyja or a Structural Finding) is the only argumentation vector. |

**Arc A: The Extractor (Default)**
- Behavior: Arm 2 runs Thread operations in T15 adjacency, harvesting configurations for Altonian clients. Each operation: RS −1 (Lock or Dissolution of Thread configurations without Mending follow-up). The Quiet One has TS 35 and does not know what Dissolution costs — they were trained to extract, not to understand what they extract from.
- Arc A passive threat: Every 3 seasons of continuous Arm 2 operation: RS −3 additional from extraction (over and above normal Lock drift). This is the systematic RS attack the supply chain enables.

**Arc B: The Witness**
- Branch condition: The Quiet One performs an extraction operation that produces a Monstrous Incursion (Dissolution Failure at RS ≤ 40 — they are now operating in damaged substrate). They witness what their extraction produces. First direct encounter with the consequences of their work.
- Transformation: Not moral awakening — operational recalibration. The Incursion is a risk they have not accounted for. Certainty 1 (Thread as resource) is strained when the resource fights back. Evidence RS fires: Thread evidence showing what the extracted configurations were doing (protecting the substrate from deeper damage) is now registerable.
- New behavior: The Quiet One requests intelligence on what they are extracting before each operation. This is not conscience — it is professional risk management. But it means they will refuse operations in territories where the extraction evidence suggests catastrophic failure risk. They now have limits.

**Arc C: The Consequence**
- Branch condition: Arm 2 produces a catastrophic extraction failure (RS ≤ 30, Dissolution Failure, Gap opens, Monstrous Incursion at Campaign scale). The Quiet One survives. Everyone near them does not.
- Transformation: The operational framework fails. They cannot recalibrate from a mass casualty event caused by their extraction. Autonomy without consequence-framework collapses into — nothing. Certainty 1 becomes Certainty 0 in a single scene. Full Thread awareness with no framework: the most dangerous epistemic state in the game.
- If player reaches them in the immediate aftermath (Mandatory Zoom In: "PC who has Thread Sensitivity ≥ 30 and is within 2 territories perceives the catastrophic Gap formation"): intervention is possible. Offering the Quiet One a framework — any framework, even contested — is better than the void. They are at the edge of a First Leap they did not choose.

---

## PART IV: NEW EMERGENT CONDITIONER CATALOGUE

### Environmental Arc Conditioners

These fire across multiple NPCs simultaneously when world-track thresholds are crossed. New category — not currently in npc_behavior_v30.

---

#### RS Band Transitions (New Systematic Conditioner)

When RS crosses a band boundary at Accounting, the following arc effects fire across all named NPCs:

| RS Transition | NPC arc effects |
|--------------|----------------|
| 72 → Strained (79→59) | No arc effect. (Starting band in most campaigns.) |
| Strained → Fragile (59→39) | Vaynard: TS check if in Arc A — if TS ≥ 14, Spirit check TN7 Ob 2; success = TS +5 (Calamity proximity effect). Edeyja: Belief 1 intensifies — she cannot accept visitors until Warden Cooperation ≥ 1. All Church Cardinals: Certainty −1 (the world's visible degradation undermines the "Solmund's creation is complete and whole" theology). |
| Fragile → Fractured (39→19) | All NPCs with TS ≥ 30: Discovery Event risk fires regardless of other conditions (the substrate is generating its own encounters). Himlensendt: if still in Arc A, mandatory Conviction check — he must publicly explain the visible world degradation within his theology. If he cannot (Cognition 4 roll vs Ob 3, failure = public contradiction): Scar 1 fires automatically regardless of player action. Torsvald: TS 20+ → Stirring (30) guaranteed within 1 season. Vossen: Continuity secondary fully activates ("the work must survive even if the movement doesn't"). |
| Fractured → Critical (19→1) | All NPC factions enter Arc C or their existing Arc C accelerates. No new arc movement — this is the end state. Edeyja: if in Arc A (no collaboration): she abandons the Southernmost. If in Arc B: she performs the last warden action (a permanent structural Mending attempt, campaign climax, OW required or RS → 0 immediately from her failure). Almud (in any state): Certainty forced to 0 regardless of previous trajectory (the world's collapse shatters the Order Conviction that claimed to protect it). |

---

#### TC Milestone Arc Conditioners

When TC crosses a milestone, the following arc effects fire:

| TC Milestone | NPC arc effects |
|-------------|----------------|
| TC 40 (Church Assertive) | Baralta: Certainty check (Categorical Imperative framework claims to prevent this — if it hasn't, something is wrong). Attunement 4D TN7 Ob 2; failure = Certainty −1. Ehrenwall: Coup Counter check trigger — if Crown Stability ≤ 3 at TC 40 crossing: Coup Counter +1 (Church growing AND Crown weak = existential threat to Valoria). |
| TC 55 (Church Prominent) | Torben: Loyalty check — if Loyalty ≤ 3 to Crown AND TC 55: Torben begins seeking information about Thread independently (his curiosity, previously dormant, activates under environmental stress). TS: 0 → 5 (environmental exposure begins). Kald (Cardinal of Temperance): her private dataset gains 2 new entries. She presents a truncated summary to Himlensendt — not the full dataset, just the trend line. This is an Authority trigger attempt that Himlensendt can accept (Scar) or dismiss (no change). |
| TC 65 (Church Dominant) | Baralta: if in Arc A (Constitutional Triumph path) AND TC 65: the constitutional framework has failed by her own definition. Baralta automatically enters Arc B (The Pragmatist) — no player action required. The system itself produced the proof her framework predicted would never come. Vossen: RM Presence markers in TC-prominent territories: survival check. Presence markers in TC ≥ 65 territories face Church suppression — −1 Presence marker per Church-Prominent territory per Accounting unless player protects. |
| TC 80 (Church Ascendant) | Almud (any arc): Belief 3 crisis — "Torben must be kept from Altonian influence." TC 80 PT drift means the entire peninsula is more pious. If Almud is in any arc, this produces a forced Decision Fork: accept the new theological reality (Certainty −1) or reassert Order (Coup Counter +1 if Ehrenwall perceives Crown as theologically capitulating). Both consequences fire regardless of what the player has done. The milestone is the trigger. |

---

#### Peninsular Strain Conditioners

| Strain Level | NPC arc effects |
|-------------|----------------|
| Strain 3–4 (Tension) | Hann: Priority 2 trigger updates. "Protect RM cells from Strain effects by pre-positioning." He begins moving cell members without authorisation from Vossen. Strain 3 is the beginning of Vossen/Hann relationship tension even with no player involvement. |
| Strain 5–6 (Fracture) | Vorn (Cardinal of Prudence): Wealth projection update. Fracture-level Strain threatens Guild trade. Vorn's embezzlement timeline accelerates — if Arc A: begins planning. If Arc B: begins executing. All Niflhel arms: Priority 7 updates to "assess operational sustainability." 3 consecutive Fracture seasons: Niflhel consolidates — all 4 arms pool resources and slow operations, reducing RS threat but making them harder to detect. |
| Strain 7–8 (Crisis) | Ehrenwall: Coup Counter forced check. At Strain 7 with Crown Stability ≤ 2: Coup Counter automatically reaches 3 (the crisis itself is the final proof that current governance has failed). This is an accelerated coup path — the world crisis produces the coup, not player manipulation. Guildmaster Council: Moral Relativism framework crisis. Guilds can't trade in a world at Strain 7. The Council faces a Decision Fork: engage politically (join a faction coalition) or withdraw (cease all peninsular operations and protect Schoenland trade routes only). |
| Strain 9–10 (Collapse) | All named NPCs: Autonomy override fires (§5.1 Faction Stability ≤ 1 equivalent — the world is at ≤ 1 Stability). Every NPC's Belief set reduces to its survival core. The most complex NPCs become the most simple. The most idealistic become the most ruthless. Edeyja at Collapse: leaves T15 permanently ("The Southernmost is already lost — I must preserve what I can of the knowledge, not the location"). This is the campaign's final arc event for the warden system. |

---

### Cross-NPC Arc Conditioners (New Category)

These fire when one NPC's arc produces a direct consequence in another NPC's arc, regardless of player action.

---

#### The Confessor and His Cardinals

| NPC A arc event | NPC B triggered |
|----------------|----------------|
| Himlensendt Scar 1 (publicly known) | Cardinal of Fortitude: Leadership Deviation Ob → 2 (reduced — Stark's independence increases when Himlensendt's authority is publicly questioned). |
| Himlensendt Scar 2 (publicly known) | Cardinal of Justice: Voss opens an internal investigation of the Confessor himself — not a Heresy Investigation but a canonical competence review. This is within his authority. Himlensendt cannot stop it. |
| Himlensendt enters Arc B (Crisis of Faith) | Cardinal of Temperance: Kald's Arc B triggers — she receives implicit permission from the Confessor's crisis to share her dataset with him. The shared Belief space opens. |
| Himlensendt enters Arc C (Confrontation — public) | All Cardinals: simultaneous arc acceleration. Justice → Arc C (his Inquisition against Himlensendt — the Church prosecutes its own Confessor). Fortitude → Arc C (Schismatic General — Templars withdraw from Himlensendt's command). Prudence → Arc B (embezzlement accelerates). Temperance → Arc C (treatise published). The four Cardinals fracture in four directions simultaneously. This is the Church schism event. |
| Himlensendt exits via any arc | Successor determination: the four Cardinals' current arc states determine who leads the Church next. Justice Arc C = trial/judicial chaos. Fortitude Arc C = military Church. Prudence Arc C = commercial Church. Temperance Arc C = scholarly/reformed Church. Player who has invested in specific Cardinals has shaped what the post-Himlensendt Church becomes. |

---

#### Crown Succession Chain

| NPC A arc event | NPC B triggered |
|----------------|----------------|
| Almud enters Arc B (Fortress) | Torben: Loyalty check (he senses his father's rigidity increasing). If Loyalty ≤ 3: Torben's Conviction-formation accelerates — whichever faction has built Disposition ≥ +2 with Torben sets his primary Conviction permanently in this season. This is the critical window. |
| Almud enters Arc C (Overthrown) | Torben: Loyalty transfers to Ehrenwall (if Coup Counter 3). Torben's Conviction shifts to match the faction Ehrenwall directs him toward. Ehrenwall is practical — she will mould Torben to produce the most stable successor. |
| Almud dies (Longevity roll failure — ED-567) | Torben: Crown leader. Conviction that emerged through play now governs Crown's entire Priority Tree. The 5–8 seasons of Torben-investment by various factions determines the faction the Crown becomes. The game's central political rivalry (Crown vs Church, Crown vs Löwenritter, Crown + Hafenmark) is now determined by who most invested in a prince they met 20 sessions ago. |
| Torben Conviction = Order (Ehrenwall's influence) | Ehrenwall: Coup Counter reset to 0. The institutions are aligned again. Ehrenwall has succeeded in producing the leader she needed without a coup. This is her Arc A resolution — a triumph that required no force. |
| Torben Conviction = Reason (Varfell's influence) | Vaynard (or Maret Uln if succession): Arc B cross-trigger. Varfell and Crown share intellectual framework — a co-victory path (Crown + Varfell) suddenly has a Conviction basis it previously lacked. |
| Torben Conviction = Equity (RM's influence) | Vossen: Arc B resolution triggers toward The Strained Leader's positive branch. RM has won the cultural argument without winning the institutional one. The movement's decades of groundwork have produced a king who believes what they believe. |

---

#### Warden-Vaynard Dependency

| NPC A arc event | NPC B triggered |
|----------------|----------------|
| Vaynard dies (Longevity or Arc C) | Edeyja (if in Arc B): receives the news through Thread perception (she perceives the TS 40 configuration dissipating). Belief 2 update: "An outsider approached competence and it destroyed him. This is why I keep the threshold high." WR requirement for next player: starts at −1 (Edeyja is more cautious, not less open — but the bar rose). |
| Edeyja enters Arc C (Crisis — Warden count 0) | Vaynard (if in Arc B/C): his TS development, untethered from any possible Warden instruction, accelerates into Consumed. The only stable TS development path was Edeyja's teaching. Without it: Consumed is the only terminal state for high-TS non-practitioners. |
| Orm dies (any Arc) | Edeyja: Coherence −1 (Knot rupture, even without formal Knot mechanic — they have worked together for decades). If Arc B: Edeyja becomes less willing to delegate to outsiders. Player must re-establish WR +1 (the trust she extended to Orm's judgment about the player must be rebuilt directly with her). |

---

#### Löwenritter-Niflhel Proximity

| NPC A arc event | NPC B triggered |
|----------------|----------------|
| Torsvald (Riskbreaker) discovers Niflhel Southernmost operation | Quartermaster (Arm 1): Priority 1 update — "Riskbreakers have identified our supply chain." Niflhel Arm 1 goes to operational silence for 2 seasons (no supply runs, operatives in safe houses). RS threat temporarily arrested. |
| Niflhel Arm 2 produces catastrophic extraction failure (Arc C) | Torsvald: mandatory Discovery Event (the catastrophic Gap formation is perceptible at TS 20+). Forces Arc B trigger regardless of TS check result — the scale of the event accelerates his TS development. |
| Ehrenwall (post-coup, Arc C) establishes Löwenritter control over T14 | Quartermaster: T14 was Niflhel's primary logistics hub. Löwenritter garrison in T14 forces Arm 1 to relocate. Next 2 seasons: supply chain disrupted, RS threat reduced 50%. Quartermaster reaches out to player (if player has Contact established) to negotiate neutral territory — he needs a new hub. |

---

### Generational Arc Conditioners (Longevity-Based)

These fire from the Longevity Track mechanic (ED-567 proposal — Longevity 1–5, Year-End roll 2d10 TN7 vs Ob = 6−Longevity).

---

#### NPC Longevity Profiles and Succession Arcs

| NPC | Longevity | P(mortality event/Year) | Expected death season | Successor arc |
|-----|-----------|------------------------|----------------------|--------------|
| Almud | 3 | ~12% | S25–35 | Arc C Torben succession |
| Himlensendt | 4 | ~6% | S35–50 | Cardinal fracture (see cross-NPC above) |
| Baralta | 4 | ~6% | S35–50 | Hafenmark heir (unnamed, Conviction: Precedent) |
| Vaynard | 2 | ~25% | S12–20 | Maret Uln activation |
| Ehrenwall | 3 | ~12% | S25–35 | Löwenritter succession crisis |
| Vossen | 3 | ~12% | S25–35 | Hann leadership transition |
| Edeyja | — | N/A | Lives until Warden count 0 OR RS ≤ 20 | Arc C: Final Stand |

**Ehrenwall succession arc (unfilled):** On Ehrenwall's Longevity death, Löwenritter enters Leadership Crisis (Mandate −2, Stability −1, Priority 7 for 1 season). Succession candidates:
- Torsvald (Riskbreaker): Conviction = Autonomy. Would run Löwenritter as a covert operations network rather than a military force. Reputation and overt military deterrence collapse. Intelligence capabilities triple.
- Senior Templar Knight (non-named, if Cardinal of Fortitude in Arc C): Conviction = Faith + Order. Creates a Church-adjacent Löwenritter — the opposite of what Ehrenwall intended.
- Torben (if Coup Counter never reached 3 AND Torben Loyalty ≥ 5 to Löwenritter): Conviction = whatever developed through play. The most open outcome.

The player who has invested in Torsvald, Torben, or Templar relationships determines which succession trajectory fires — their Disposition investments are the tiebreaker.

---

### Obligation-Triggered Arc Conditioners

These fire when specific Obligations are honored or violated (social_contest §6.1).

---

| Obligation event | NPC arc effects |
|-----------------|----------------|
| Church Obligation honored (Himlensendt complies): "No Inquisitors in T6 for 2 seasons" | Kald: observes the compliance. Her internal assessment updates — "Himlensendt can be negotiated with. This is new information." Her Evidence RS check (Arc B trigger) requires 1 fewer Scar to fire than baseline. |
| Church Obligation violated: Himlensendt sends Inquisitors to T6 despite Obligation | Baralta: mandatory Parliamentary Manoeuvre next season (constitutional violation of a treaty equivalent). Hafenmark Mandate +1 from successful protest (even if the Manoeuvre fails the roll — the act of filing is the political win). |
| Crown Obligation honored toward Löwenritter: "Maintain garrison in T10" | Ehrenwall: Coup Counter −1 (Crown demonstrating reliability on a specific commitment is exactly what her assessment tracks). |
| Crown Obligation violated: fails to maintain T10 garrison | Ehrenwall: Coup Counter +1. One criterion failed on her internal 6-criteria assessment. |
| Varfell Obligation honored toward Warden (per negotiation with Edeyja): "Provide RS data to Wardens for 3 seasons" | Edeyja: WR +1 (the Obligation's fulfillment is Evidence — Varfell did what it said). WR advancement through demonstrated reliability, not just competence. |
| Any Grand Contest Obligation violated by NPC faction | All NPCs with Disposition ≥ +1 toward the violating faction: −1 Disposition. The breach is public. The relational network contracts. |

---

## PART V: ZOOM IN TRIGGER ADDITIONS (Arc-Adjacent)

The following new Zoom In triggers are proposed for scale_transitions §4.3.2 (Mandatory) and §4.3.3 (World-State Priority 1), beyond the existing list.

---

### New Mandatory Zoom In Triggers (§4.3.2)

| Trigger | Condition | Scene Content |
|---------|-----------|---------------|
| Cardinal Schism | Church Stability reaches 0 AND any Cardinal activates as independent NPC | The player witnesses the Church's institutional fracture directly. Each Cardinal present pursues their arc trajectory simultaneously. The player is in the middle. Scene choices: align with one Cardinal (Solidarity RS scene), investigate the chaos (Fieldwork Evidence +3), or flee (Endurance check Ob 2 or caught in crossfire). |
| Niflhel Catastrophic Extraction | Arm 2 produces catastrophic Gap (RS −8 in one operation, Monstrous Incursion immediate) | Mandatory if player is within 2 territories. Scene: the Incursion. The player encounters a Monstrous Incursion that is not random — it is specifically the consequence of what was extracted. The investigation (Fieldwork, Thread-Read) reveals what Niflhel did. This is the evidence that makes the Southernmost supply chain prosecution possible. |
| Warden Death | Any named Warden dies AND the player has WR ≥ 1 | The player perceives the TS dissipation through Thread (if practitioner, TS ≥ 30). Or: receives news through the social network (if non-practitioner, Disposition ≥ +2 with a Warden). Scene: grief, assessment of remaining Warden capacity, decision whether to proceed to T15 immediately or address other priorities. The scene does not require intervention — it requires witnessing. |
| Torben Conviction Emergence | Torben's Conviction solidifies (any faction's investment tips him past the emergence threshold — see arc above) | The player is invited to an audience. If they have invested in Torben: the scene is the payoff. They learn what Torben has become. If they have not invested: they learn what other factions have made him. Scene: one Contest exchange (not a full Contest — a single Argue roll representing the player's final opportunity to influence Torben's final Conviction before it locks). |
| Riskbreaker Operational Failure | Torsvald's Arc C produces the one major operational error (mass casualty event from Thread perceptual overlay) | The player witnesses the aftermath. Mandatory if in adjacent territory (2 steps). Scene: Torsvald is in crisis. His Autonomy conviction has failed — an operation done correctly produced wrong results because his perception was wrong. This is the one moment where Solidarity RS is available to Torsvald without any prior Knot (the scale of the failure creates relational openness). |
| The Quartermaster's Offer | Niflhel Arm 1 Quartermaster enters Arc B (defection state) AND player has Investigation contact established | The Quartermaster makes contact. Not an Outreach — a professional negotiation proposal. He has left. He has information. He wants something reasonable. Scene: private negotiation (Attunement-primary, No Adjudicator). The player can refuse; he will find another buyer. |

---

### New World-State Zoom In Triggers (§4.3.3 Priority 1)

| Trigger | Condition | Scene Content |
|---------|-----------|---------------|
| Vorn's Embezzlement Trail | Player reaches Evidence Track 5 on "Church internal finances" | The numbers tell a story. An administrative NPC in the Church archive is nervous. Fieldwork leads to a document that doesn't add up. The scene: the player follows the trail to its origin. Vorn is at the end. This is the discovery scene — she knows the player knows. Negotiation available. |
| Kald's Dataset Discovery | Player reaches Evidence Track 8 in T9 Church archives, Research action, Depth 3 | The dataset. Eleven years of Thread Sensitivity prevalence data, buried in a tithe subsidiary ledger. The player finds it. Kald may or may not know the player found it. The scene: the player must decide what to do with evidence that could simultaneously liberate Thread practitioners, break Himlensendt, and destroy Kald's career. |
| Orm's Final Maintenance | RS ≤ 35 AND player has WR ≥ 2 | Orm is working on a Gap that is beyond standard maintenance. He is holding something closed that he has been holding for 3 seasons. The player can see it — the effort it requires. Scene: Orm says nothing, but everything is visible to TS ≥ 30. To TS 0 observers: an old man doing hard work alone. The scene is witnessing. The player may assist (Thread operation contributes alongside Orm's — collective operation per threadwork §2.5). |
| The Confessor's Doubt | Himlensendt has ≥ 1 Scar AND Kald has presented her dataset to him | Himlensendt is in T9 sanctuary. He will not see anyone. But the player, if they have Disposition ≥ +2 with him (from prior interactions — difficult, but possible), receives a note: "I have questions." The scene: a private audience. Not a Contest — a conversation. Himlensendt is asking, not arguing. For the first time in the campaign, the Inquisitor wants to be answered, not to answer. |

---

## PART VI: EDITORIAL ITEMS GENERATED

| ED | Description | Priority |
|----|-------------|---------|
| ED-591 | Cardinal of Fortitude (Stark) full arc — proposed here. Requires user approval before commit. | P2 |
| ED-592 | Cardinal of Justice (Voss) full arc — proposed here. Requires user approval. | P2 |
| ED-593 | Cardinal of Prudence (Vorn) full arc — proposed here. Requires user approval. | P2 |
| ED-594 | Cardinal of Temperance (Kald) full arc — proposed here. Requires user approval. | P2 |
| ED-595 | Ehrenwall full arc (A/B/C) — proposed here. Requires user approval. | P2 |
| ED-596 | Torsvald (Riskbreaker) full arc — proposed here. Requires user approval. | P2 |
| ED-597 | Vossen full arc expansion — proposed here. Requires user approval. | P2 |
| ED-598 | Hann full arc expansion — proposed here. Requires user approval. | P2 |
| ED-599 | Orm (Warden second) full arc — proposed here. Requires user approval. | P2 |
| ED-600 | Niflhel named operatives (Quartermaster, The Quiet One) arcs — proposed here. | P2 |
| ED-601 | Almud Arc C three-trajectory expansion (Abdicant/Pretender/Broken) — proposed here. | P2 |
| ED-602 | Vaynard Arc A and Arc B full specification — proposed here. | P2 |
| ED-603 | Environmental arc conditioners (RS/TC/Strain — NPC systematic effects) — new category, proposed here. | P2 |
| ED-604 | Cross-NPC arc conditioners (Confessor-Cardinals, Crown Succession, Warden-Vaynard, LR-Niflhel) — new category. | P2 |
| ED-605 | Obligation-triggered arc conditioners — proposed here. | P2 |
| ED-606 | 6 new Mandatory Zoom In triggers (§4.3.2) — proposed here. | P2 |
| ED-607 | 5 new World-State Zoom In triggers (§4.3.3) — proposed here. | P2 |
| ED-608 | Mediation contest type (Vossen/Hann reckoning scene) — new contest format where player resolves two opposed NPCs simultaneously. | P2 |
| ED-609 | Torben Beliefs and Conviction emergence mechanic (first faction to reach Disposition ≥ +2 in specified window sets initial Conviction) — formal specification required. | P2 |
| ED-610 | Baralta successor (unnamed Hafenmark heir) — requires design. | P3 |
| ED-611 | Ehrenwall succession candidates (Torsvald / Templar Knight / Torben) — formal specification. | P2 |
| ED-612 | Faction Fracture sub-faction spawning rule (Kald's Temperance Order as post-Arc C Church sub-faction) — formal specification. | P2 |
| ED-613 | Vaynard Arc C recovery gate (Edeyja as only exit) — confirms cross-NPC dependency and requires RS-state conditional. | P2 |

---

## PART VII: ARC DENSITY ASSESSMENT (POST-EXPANSION)

| Faction / Sub-faction | Before | After |
|----------------------|--------|-------|
| Crown (Almud) | A/B/C thin | A/B/C fully specified + Arc C 3-trajectory expansion |
| Crown (Torben) | No arcs, no Beliefs | Full Conviction emergence mechanic + Zoom In trigger |
| Church (Himlensendt) | A/B/C present | Cross-NPC conditioners from Cardinals, RS/TC environmental triggers added |
| Church — Cardinal of Fortitude | Schism behavior only | Full A/B/C arc set |
| Church — Cardinal of Justice | Schism behavior only | Full A/B/C arc set |
| Church — Cardinal of Prudence | Schism behavior only | Full A/B/C arc set |
| Church — Cardinal of Temperance | Schism behavior only | Full A/B/C arc set |
| Hafenmark (Baralta) | A/B/C present | TC milestone conditioners added; successor flagged |
| Varfell (Vaynard) | A stub, B stub, C 1 line | A/B fully specified; C expanded with recovery gate |
| Varfell (Maret Uln) | Succession only, no arcs | Cross-NPC conditioners from Torben/Almud succession |
| Löwenritter (Ehrenwall) | Arcs implied, not specified | Full A/B/C + succession arc |
| Löwenritter (Torsvald / Riskbreakers) | 1 paragraph profile | Full A/B/C arc set |
| Restoration Movement (Vossen) | A/B/C partial | Full expansion including Arc C 3-trajectory |
| Restoration Movement (Hann) | A/B partial | Full A/B/C arc |
| Southernmost Wardens (Edeyja) | A/B/C present | Arc B full trigger sequence (4 stages); Warden death conditioners |
| Southernmost Wardens (Orm) | Not named | Full A/B/C profile |
| Southernmost Wardens (Third Warden) | Not named | Intentionally unnamed (the death that precedes contact) |
| Guilds | No arcs | Strain conditioners; Vorn Arc C acquisition |
| Niflhel | No NPC arcs | Quartermaster A/B/C; The Quiet One A/B/C |
| Ministry | No NPCs | Flagged as design debt (ED-pending) |
| Schoenland/Altonian | Observer | Cross-NPC: Kald's treatise AER +1 (Altonian academic response) |
| **Cross-NPC conditioners** | None | Confessor-Cardinals chain; Crown Succession chain; Warden-Vaynard dependency; LR-Niflhel proximity |
| **Environmental conditioners** | None | RS band transitions; TC milestone effects; Strain level effects |
| **Obligation conditioners** | None | 6 Obligation-triggered arc effects |
| **Generational conditioners** | Proposed (ED-567) | Full Longevity table + succession arc for all named NPCs |

*End of document.*
