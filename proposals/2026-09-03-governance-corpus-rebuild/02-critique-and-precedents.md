# Critique of the v1 design

**[SELF-AUTHORED — bias risk.]** This is a critique of my own design, so the failures I am least
likely to see are the ones that follow from what I optimised for. I optimised for a *clean* model:
single ownership, pure derivation, bounded quantities, deterministic replay. Every finding below that
begins "it is too clean" is therefore the one to trust least from me and check hardest — which is why
the first and largest is stated as a measurement rather than a judgement, and why an independent
critic was run against the same document.

## Verdict

**The architecture is right as a bookkeeping system and wrong as a drama system.** Its ownership,
derivation and determinism are sound and should survive. But it is **over-damped to the point of
inertia**, it **dropped two of the corpus's five territorial tiers**, and it has **no object for the
thing this game's politics is actually about** — a claim on a title. Three of its headline slogans
are false, two of them contradicted by its own annex. It is salvageable, and the salvage is
structural rather than cosmetic: two tiers restored, one new first-class object, and a deliberate
budget of instability.

---

## 1 · Nothing in the system can run away — and that is the whole game

**Measured across the design and its executable annex:**

| | occurrences |
|---|---|
| **Damping devices** — `clamp` 92 · `cap` 95 · `floor` 43 · `saturating` 6 · `ceiling` 4 · `bounded` 3 · `mean-revert` 2 | **≈ 245** |
| **Amplifying devices** — `spiral` 0 · `positive feedback` 0 · `amplif*` 0 · `compound` 0 · `escalat*` 0 · `snowball` 0 | **0** |

`runaway` appears twice, both times to say runaway is prevented. Every quantity in the model is
clamped to a range, capped per season, floored at zero, saturating by construction, or explicitly
mean-reverting. **There is no mechanism anywhere in the design by which a small disturbance becomes a
large one.**

**This is a regression against the corpus, not a fidelity to it.** The corpus uses *escalat\** 24
times, *spiral* 6, *compound* 9, *accelerat\** 6, and names two "anti-death-spiral floors" — you do
not floor a death spiral unless you believe one is otherwise reachable. It states the amplifying
principle outright:

> "**Resolve Tension A while ignoring Tension B finds Tension B has escalated.** This is the
> historically accurate dynamic: states rarely face one crisis at a time."
> — `early_game_ignition_analysis.md:142`

And it builds ratchets: the three-phase IP escalation, the S1–S7 assassination fuse, the CI curve
whose declaration probability rises as the cube-and-a-third power of pressure, graduated autonomy
that becomes irreversible at Split. **My design kept every one of those as a bounded state machine
and removed the thing that made them frightening — the possibility that they compound.**

**What it costs at runtime.** A campaign in which every quantity is bounded, every feedback loop is
negative, and every cross-scale effect is clamped at ±2 will converge. Not crash — converge. Season
40 will look like season 30. The player will have learned the equilibrium and the world will have
nothing left to do to them. **Stable is not the same as alive**, and I built stable.

**The fix is not to remove the caps.** It is to introduce a small, named, expensive-to-enter set of
**amplifying regimes** — states in which specific feedback loops flip sign — and to make entry rare
and exit costly. A design should be able to name every loop in it and say which way it points. §
*The instability budget* in the rewrite does that.

---

## 2 · Two territorial tiers were dropped, and factions now float free of the map

**The corpus specifies five levels** (`valoria_political_hierarchy_v30.md §1`):

```
Valn (peninsula) → Kingdom of Valoria → Duchy (×3) → Province (×14) → Territory = Settlement (1–3 each)
                                                                     → sub-features (districts, mines, harbours…)
```

**The design has three** — settlement, province, peninsula. Measured: `duch*` appears **5 times** in
the design against **48** in the corpus; **`sub-feature` appears zero times** in the design and zero
in its executable annex, against 16 in the corpus.

**What the duchy tier was carrying, and where its absence shows.**

- Almud is *simultaneously* monarch of Valoria and Duke of Valorsmark; Baralta holds Hafenmark;
  Vaynard holds Varfell. The three secular factions **are** duchies. Dropping the tier turns a
  feudal relation — *the Dukes owe fealty and administer their own duchies day-to-day* — into an
  undifferentiated `controller` pointer on each settlement.
- With no duchy, there is no structural difference between a faction losing a province at its core
  and losing one at its edge; no seat of a duchy; no unit of vassalage to grant, revoke or usurp.
- The Löwenritter's whole arc is that it **holds territory without holding a title**. That is exactly
  what the missing tier would have expressed, and instead the design carries it as a bespoke
  four-state ladder.
- Three entities sit *outside* the duchy structure by explicit design — Himmelenger (Church
  city-state), Askeheim (unincorporated), Schoenland (foreign tributary). In a three-tier model they
  are three unexplained special cases. In a five-tier model they are one rule: **a province with no
  de jure duchy.**

**Sub-features are worse, because they were dropped silently.** Harbours enable sea routes, barracks
produce units, cathedrals project piety, mines yield wealth, watchtowers extend vision. That is the
entire source of *settlement differentiation* — the reason taking Gransol's Market Quarter is a
different act from taking a village. The design replaced it with a `type` enum and a `FacilityTier`
integer, which cannot express "this settlement has a harbour and a mine but no barracks".

**Cost at runtime.** Without sub-features every settlement of the same type is mechanically
identical, so the map is 37 copies of nine templates and the strategic layer is about *quantity of
holdings* rather than *which holdings*. That is the difference between a map that rewards reading and
a map that rewards counting.

---

## 3 · There is no Claim, and this is a game about claims

The design has **zero** occurrences of `title` and **one** of `casus belli`.

The corpus builds, separately and without noticing they are one thing:

| corpus mechanic | what it actually is |
|---|---|
| Casus Belli (generated, held, consumed, expiring) | a claim licensing an attack |
| Baralta Crown Claim, Consecration Crisis | a claim on the Kingdom title |
| Succession Contest — blood claim, contender strength, heir Disposition ≥ +3 | competing claims on a faction's leadership |
| Parliamentary Transfer of a province | a claim prosecuted by vote instead of by army |
| Insurgency → Promoted Faction | a claim acquiring recognition |
| Bishop Appointment; Ecclesiastical Appointment | a claim on a settlement's governance, prosecuted administratively |

**Six mechanics, one object.** A `Claim` — subject (what is claimed), claimant, strength, basis
(blood / conquest / charter / office / recognition), and the routes by which it can be prosecuted
(war, vote, appointment, marriage, purchase) — collapses all six and immediately answers questions the
corpus leaves open: what a Casus Belli's duration means, what a promoted insurgency *has* that it
did not before, why a parliamentary transfer and a conquest produce the same end state by different
means.

**It also creates the thing the design most lacks — an object that persists, accumulates, and can be
traded.** Claims are the durable political substance of every game in this genre, and this design has
none.

---

## 4 · Three headline claims are false, two contradicted by my own annex

**"One writable tier. Every political write in the game lands on a settlement."** — Part IV.
Contradicted directly by the annex it summarises: *"A province stores only what has no settlement
analogue: stabilisation and vacuum windows, Attention, Thread Debt, the trade-route token,
temperament drift"*; *"A polity stores its five stats, its hand, its mission and its offices"*; *"The
peninsula stores only clocks and campaign-arc state."* All of those are written every season. The
true rule — which the same document also states — is **one owner per quantity**. The slogan is a
stronger, wrong version of a correct rule, and it is the headline of the section.

**"Effects never fire effects within a phase"** — used to retire the corpus's Cascade Depth Cap.
False of the design's own tick, which says *"PH-08 onward are Accounting phases that apply their own
effects at the end of each phase through the same commit routine."* A threshold crossed in PH-09
fires a pipeline in PH-10 which emits effects which commit — that is an effect firing an effect. The
cap was retired on a premise the design does not honour.

**"No subsystem names another."** True of the *code* and false of the *content*, which is where it
matters: the design's own exemplar card carries `settlement.has_subnational(RM)` as a trigger
predicate, and its directive generator maps `Counter-threat → Suppress(RM|Church)`. Named factions in
rules is precisely the scripting drift the design's own throughline TL-9 forbids. The honest position
is that predicates must reference **roles and relations**, not identities — `has_presence(inst) where
inst.hostile_to(controller)` — and the design does not say so.

---

## 5 · The abstraction that would have prevented half of this: de jure vs de facto

The corpus contains **two incompatible fracture models** — Greater/Lesser by PV share with a
Consolidation action, and geographic northern/southern with automatic re-merge — and the v1 design
punts the choice to its open-questions list.

Both are the same mechanism, badly named. A province has a **de jure** extent (fixed, slowly
drifting, defines what a title *means*) and a **de facto** control (fast, contested, defines who is
*obeyed*). Fracture is divergence between them; consolidation is convergence; the "unification bonus"
is the reward for closing the gap; a Casus Belli is a licence to close it by force.

That single distinction, borrowed from a game that has run it for a decade, resolves the two models,
removes the need for Greater/Lesser naming, explains why Himmelenger and Schoenland are exceptions
(no de jure parent), and gives the insurgency pipeline its terminal state (de facto control acquiring
de jure standing = promotion).

---

## 6 · The emergence engine is underpowered where the corpus is strongest

The corpus's best generative idea is the settlement's Local Actors — a Magistrate, a Priest, a
Guildmaster with **orthogonal Convictions** so that any ruling pleases one and wrongs another, plus
ambitions that advance whether or not the player engages. The design preserves the *shape* (NPC
dossiers, ambition, trajectory) and leaves them as **dispositions**: scalars that go up and down.

Dispositions do not generate politics. **Blocs with demands generate politics.** The distance is
small and the payoff is large: give each settlement a handful of interest groups with an *approval*
level and a small set of *demands* keyed to settlement state, and the Π homeostat stops being an
abstract scalar and becomes a readable summary of who is angry and why. Revolt stops being a die roll
against Order and becomes what it is historically — a coalition of the disaffected crossing a
threshold.

---

## 7 · Nothing is genuinely scarce

Administration Points are scarce *within* a settlement-season. Card plays are scarce *within* a
faction-season. Neither is scarce *across* the campaign, and nothing is contested between factions
except territory itself.

Strategy games in this tradition earn their tension from a resource that is finite, shared and
depleting — supply throughput, manpower, legitimacy, cash. Valoria has Treasury and Military as
numbers on a faction sheet with no stated production limit, no logistics constraint, and no shared
pool. Consequently every plan is affordable and the only real cost is time.

---

## 8 · Smaller, still real

- **The Mandate ↔ L/PS loop is explicitly a stable fixed point** (the corpus's own Stage-4 sim
  confirms convergence). It is presented in the design as a virtue. It is also the reason a faction
  cannot experience a legitimacy collapse: the loop drags every settlement back toward the realm mean.
- **Institutions are both components and peers** — the Church is presence inside settlements *and* a
  polity. The design has `presence[inst]` and a `Polity` and no statement of how they relate.
- **Provinces are runtime-variable containers** (they fracture) but are modelled as static ones.
- **No failure-mode analysis.** The design never says what a *bad* campaign looks like, which means
  it cannot be tuned against one.
- **The tick's determinism story is incomplete** for simultaneous battles: "battles resolve
  simultaneously per territory" with casualties read back within the phase is order-dependent.

---

# Precedents — the specific object each game has that this design lacks

Judged against games the corpus itself names (Crusader Kings III, EU4, Victoria, KOEI *Romance of the
Three Kingdoms*, Shadow Empire, Mount & Blade, Manor Lords, Disco Elysium, Pathologic 2, Pentiment)
plus four it does not (Dwarf Fortress, Frostpunk, Democracy 4, Into the Breach). In each case the
question is not "what is that game like" but **what object exists in it that does not exist here, and
what work does that object do.**

## Hierarchical shape → **Crusader Kings III: the title**

**The object.** A *title* — barony, county, duchy, kingdom — with three separate facts attached: who
**holds** it, what its **de jure** contents are, and what it **de facto** controls. Titles are things
you create, grant, revoke, usurp and inherit. A realm is a *tree of titles*, and vassalage is the
edge between two nodes of that tree.

**The work it does.** It makes the map political instead of geometric. Losing a county at your core
and losing one at your border are different events because they sit differently in the tree. A vassal
is not a smaller country next to you; it is a node below you holding a title you granted.

**What it replaces here.** The v1 design's `controller` pointer on each settlement, its bespoke
four-state Löwenritter ladder, and its three unexplained special-case entities. Valoria's own corpus
already specifies the tree — Kingdom → Duchy ×3 → Province ×14 → Settlement — and the v1 design
discarded two levels of it.

**What is lost.** Title trees are heavy in CK3 because it runs thousands of them across a continent.
Valoria has one kingdom, three duchies and fourteen provinces. **The structure is nearly free at this
scale**, which is the argument for taking it.

## Ownership → **Victoria 3: goods live in the market, not in countries**

**The object.** A *market*. No country holds a stockpile of coal; the market holds the coal and the
country buys from it at a price the market sets. There is exactly one place any good exists.

**The work it does.** Because a quantity has one home, price can *emerge* rather than be authored, and
no two systems can disagree about how much coal there is.

**What it replaces here.** Nothing — this is the one axis where the v1 design is already right in
principle. But it corrects the *statement* of the rule. Victoria's rule is "one owner per quantity",
not "one owner per tier". The v1 slogan ("every political write lands on a settlement") is the
tier version and it is false; provinces, polities and the peninsula all hold state that is written
every season.

## Nesting → **EU4: estates** (component and peer at once) and **orthogonal partitions**

**The object.** An *estate* — Clergy, Nobility, Burghers — which is simultaneously **inside** your
country (it holds a share of your crownland, you grant it privileges, it gives you a cut of what it
holds) and **an agent facing you** (it has loyalty and influence, it makes demands, and at low loyalty
it revolts). One entity, two interfaces: a component interface and an agency interface.

**The second idea, from the same game.** Provinces belong to an *area*, a *region*, a *trade node* and
a *culture group* — **four orthogonal partitions over the same units**, not one nesting. Questions
that would fight over a single hierarchy each get their own.

**The work it does.** It resolves exactly the problem the v1 design leaves open: the Church, the
Guilds, the Ministry and the Löwenritter are all *presence inside settlements* and *polities in their
own right*, and the design has a `presence[inst]` field and a `Polity` type with nothing said about
how they relate. EU4 answers: they are one object with two interfaces, and the loyalty on the agency
side is what makes the presence on the component side dangerous.

**What is lost.** Estates in EU4 are a fixed roster of three; Valoria wants five or six with
faction-specific flavour. The mechanism generalises, the tuning does not transfer.

## Dependencies → **Democracy 4: the simulation *is* a signed, weighted, delayed graph**

**The object.** A *node* (a measurable quantity) and an *edge* (a signed influence of one node on
another, with a strength and a lag). Nothing else. Policies are nodes, voter groups are nodes,
crime is a node; every causal claim in the game is an edge you can inspect in the UI.

**The work it does.** No subsystem contains a reference to another subsystem, because there are no
subsystems — there is an evaluator and a graph. Content authors add edges; programmers never touch
them. And because the graph is data, the game can *show the player why* something happened, which is
the hardest thing a political simulation has to do.

**What it replaces here.** The v1 design claims "no subsystem names another" and this is true of its
code and false of its content: its own exemplar card carries `settlement.has_subnational(RM)` and its
directive generator maps `Counter-threat → Suppress(RM|Church)`. Named factions in rules is the
scripting drift its own throughline forbids. Democracy's discipline forces the fix — predicates
reference **roles and relations** (`presence(inst) ∧ hostile(inst, controller)`), never identities.

**What is lost.** A pure influence graph cannot express sequence, and Valoria genuinely needs
sequence: sieges, successions and votes are procedures, not equilibria. The graph is right for the
*clock layer*; the procedures stay procedures.

## State changes → **Into the Breach: total, visible, deterministic resolution order**

**The object.** A *fully previewed* turn. Before committing, the player sees exactly what every enemy
will do and in what order, because the resolution order is total and public and the outcomes are
deterministic given it.

**The work it does.** It converts a simulation from something that happens *to* the player into
something the player reasons about. In a no-GM engine this is not a luxury: **the engine has replaced
a human whose main job was explaining why things happened**, and preview is the only substitute.

**What it replaces here.** The v1 design's determinism story is engine-facing — seeded streams, a
single commit, a state hash — and stops there. It never asks whether the *player* can see the chain.
Its own honest gap: "battles resolve simultaneously per territory" with casualties read back inside
the phase is order-dependent and unspecified.

**What is lost.** Full preview is impossible where hidden information is the point, and Valoria has
covert actors, concealment rolls and fog of war. The rule that survives is narrower and still worth
having: **the consequence chain of the player's own committed action is always shown before
commitment**; hidden actors are hidden in their *existence*, never in their *arithmetic*.

## Emergence → three objects, from three games

### **Crusader Kings III: the scheme**
A *scheme* is a durable, progressing, often secret intention held by one character against another —
murder, seduce, claim-fabricate — with a success chance, a secrecy value, agents who can join it, and
a **discovery** event that fires if secrecy fails.

The corpus already has three-quarters of this in the NPC `ambition` (goal, method, timeline, progress)
and `trajectory` (what they do when thwarted). What it lacks is the fourth quarter, and it is the
important one: **an ambition can be found out.** In v1 an ambition advances in private and then fires.
In CK3 the drama is almost never the murder; it is learning about the murder in time.

### **Victoria 3: radicalism**
Pops made poor or ignored become *radicals*; radicals raise a revolution's progress; the revolution
changes the government; the new government's laws make a different set of pops unhappy. **A genuine
positive feedback loop with an expensive, state-changing exit.**

This is the shape the v1 design has nowhere. Valoria's own corpus wants it — "Resolve Tension A while
ignoring Tension B finds Tension B has escalated" — and v1 replaced it with a homeostat whose entire
purpose is to prevent that.

### **Shadow Empire: administrative strain**
The larger your realm, the more administrative capacity it costs to hold, and capacity is finite. **Growth
is self-limiting through a mechanism the player can see and plan against**, rather than through the
opponent AI happening to gang up.

The v1 design has **no scaling penalty for success at all.** Mandate saturates — a large faction's
legitimacy stops growing — but nothing makes a large faction *harder to run*. The corpus supplies the
missing half already and does not use it: **GD-2's mandatory threat response** is a coalition trigger
sitting unused in the insurgency pipeline. Strain plus coalition is the anti-snowball.

## Two more, briefly

**KOEI *Romance of the Three Kingdoms*: the officer roster.** Officers are the unit of politics —
recruited, promoted, trusted, and defecting *with their holdings* when loyalty falls. The corpus
cites this precedent by name and then models NPCs as dispositions attached to settlements. An officer
network is a graph over people, and defection cascades run along its edges.

**Frostpunk: the law ratchet.** Laws are permanent and each opens two further, mutually exclusive
laws. The campaign's shape comes from an irreversible path through a tree, not from a state that can
be tuned back. Valoria has exactly one ratchet — the Ledger of Consequence — and treats it as
bookkeeping rather than as the spine of the campaign's identity.
