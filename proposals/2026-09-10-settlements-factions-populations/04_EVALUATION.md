# Part C — evaluation

## Status: **PROPOSED (2026-09-10). HELD BACK IN FULL** — see `00_INDEX.md`.

**Method.** `skills/ners/SKILL.md:36-64` — one cut, four times; **a PASS is
licensed by a named failed attack, not by an absent finding**; and **E is scored last, as a ratio
against what N and R found**, never as an independent axis, because alone it is satisfiable by
amputation (`CLAUDE.md` §0.06).

**The six directions N is tested from**, since §0.06 requires all of them: *top-down* (realm → hearth)
· *bottom-up* (hearth → realm) · *vertical* (zoom) · *diagonal* (a national faction claims one
settlement — the ratified §5.2 case) · *lateral* (settlement ↔ settlement) · *horizontal* (faction ↔
faction at one tier). An N-line holding in one direction is **narrowed, not passing**.

**R is scored in both halves**, including the half with no player in it, plus completeness — a
mechanism breaking at its extremes fails R.

---

## C.1 · P1 · Dearth reaches the body

**N.** *Top-down:* cut it, and a realm-scale `levy` that empties a hearth's larder has no consequence a
person could notice — the extraction-invariance chain (SE-2) becomes unspellable. **Dies.**
*Bottom-up:* a hearth's hunger never becomes a question, so nothing at the hearth reaches the
settlement except by an authored act. **Dies.** *Vertical:* the body-band penalty in `budget()` already
exists; without P1 it reads a constant, so **a wounded duke and a starving duke are
indistinguishable.** **Dies.** *Diagonal:* a Restoration cell recruiting in a starving hamlet has
nobody with a question to recruit. **Dies.** *Lateral:* two settlements on one river, one fed and one
not, are identical. **Dies.** *Horizontal:* a faction whose members starve and one whose members do not
have equal `faction_value`, because P5's weight sum is blind to it. **Dies.**
**The attack that failed:** *"P1 is redundant with `urgency()`."* No — `urgency` cannot move a ranking
(`decision.py:298-302`, *"INERT BY CONSTRUCTION"*); P1 works through **questions and budget**, both of
which move choices. **PASS in all six**, with the residual that the *number* of scenes a hungry person
loses is a swept fixture.

**R.** *Player half:* a governor can starve a town or feed it and see the difference in **who
petitions**; the strategy (spend grain or spend scenes) is real; customisation is nil — P1 is not a
knob; felt impact is direct, since your `transfer` is the thing that ends `body.changed`.
*The half with no player in it:* a rung whose Site wore below `fishing 100` (`rosters.yaml:969`) yields
less → shortfall → its people's bodies fall → questions → `move`, which executes. **A hamlet empties
itself with nobody watching**, and the story is a `causes[]` chain rather than a script.
*Completeness at the extremes:* a rung with stores exactly 0 and 200 weight — every eater's body falls
by the same deficit share; body floors at 0 and the death cascade fires through §15.3. ⚠ **But a cohort
at weight 1 whose `mortality` rounds to 0 never dies — a completeness defect.** The CEN weight
decrement must floor at one death when body is 0, or singletons are immortal to hunger. **Named, not
waved past.**

**S.** Integrates on rows that exist; `causes[]` chains to `stores.changed`; **pauses correctly** — the
write is at MATTER, and the world is frozen before DELIBERATE. It **fixes an S defect**: the two
arithmetics for subsistence (`01_PRIMITIVE_BASE.md` §3.2). One residual S issue, declared: a cohort's
death lands at CENSUS while a singleton's lands at MATTER — **two timings for one quantity**, a
consequence of declining a matrix edit, and swept.

**E, as a ratio.** What N and R found is carried by one new write site, one arithmetic fix, one
referent fix and two fixtures. Nothing is removable without losing a direction. The player intuits it:
*no grain, fewer scenes, then a funeral.* **High relative to N and R — nothing here is overhead.**

**Gameplay, in concrete seasons.** S1: the levy takes 40 grain. S2: `stores.changed`, then
`body.changed` ×3 at the hearth, one crossing `limited 500` → Carin's budget is 4 rather than 5, and
her question is about the hearth; she `petition`s. S3: the mayor's ledger holds the petition claim, if
it was carried. **The decision that gets harder:** *levy or don't* — it now costs bodies you will hear
about. **What gets easier and should not:** nothing found; a lord who never levies is not rewarded,
only unblamed.

**Emergent narrative, traced through the mechanism.** `levy.taken(R)` → `stores.changed(Hh)` →
`body.changed(p_low)` → `condition.band_crossed(p_low, limited)` → Q3 for `p_low`, referent `Hh` →
`speak`/`petition` → witnessed → a claim in `p_mid`'s ledger → Q2 → `p_mid` acts. **Four links, two
persons, no authoring** — the standard Reading 09 §1.3 sets. **Met.**

**Cost.** *Forbids:* a world where named persons cannot die of hunger. *Makes unspellable:* "a famine
that raises unrest" — there is no unrest. *Corpus:* none broken; ARC cases with `person.died` endings
gain a second cause of death a `causes[]` walk can distinguish. *Convergence:* **P1 is damping, and
alone it makes season 40 resemble season 30** — which is exactly why P2 must follow it.

---

## C.2 · P2 · The bodies clock

**N.** *Top-down:* a realm with no growth has no reason to found, levy or tax differently across forty
seasons. **Dies.** *Bottom-up:* a hearth that cannot grow cannot become a community, so P4's kind
ladder has nothing to climb. **Dies.** *Vertical:* zoom out and every settlement's `population()` is a
world-gen constant forever — `W_s` never moves, so **§5.1's "number of people" is static**. **Dies.**
*Diagonal:* a national faction claiming a growing town and a shrinking one are equivalent bets.
**Dies.** *Lateral:* migration by `move` between two settlements has a source and a sink only if one
grows. **Dies.** *Horizontal:* two factions' `faction_value` diverge over time only if their held
people multiply. **Dies.**
**The attack that failed:** *"P4 alone supplies growth — more Sites."* No: Sites yield **matter**, not
weight; without P2, nothing new ever holds a `commit`. **PASS, six directions.** Residual: the *rate*
is a fixture, and a rate of 0 (the control arm) removes P2 with no error — **which is the correct null
arm, not a false N-line.**

**R.** *Player:* strategy across the long game — feed a town now for a levy in twelve seasons; **the
Banished trap** (a boom you did not plan for) becomes a real emergent hazard; customisation none.
*No player:* a fed hamlet doubles, outgrows its larder, and P1 thins it — **a Malthusian wave nobody
scripted**, witnessed as `envelope.changed` by persons present, as a fact rather than a mood.
*Completeness:* an envelope of all zeros stays zero — no immaculate birth, since `births ∝
envelope[grown]`. ⚠ Integer counts at small N need a declared rounding rule: `floor` starves small
hearths, `round` can double them — `assumption`, swept. ⚠ **And the period is longer than
`MAX_SEASONS` today** (`H-33`), so **P2 is unobservable until `W29`** — a completeness gate, not a
design flaw, and stated as such.

**S.** The envelope eats through P1's draw — **one arithmetic**. Bodies-before-larders honours §25's
order. It pauses correctly, at MATTER, before the freeze. ⚠ **One S hazard, named:** `population()`
counts envelope **plus** persons, so a season in which P3 mints 40 and CENSUS decrements 40 must net to
zero **across the barrier** — the reconciliation and the mint must be one write, or the Query
double-counts for one step.

**E.** Three fixtures, one roster, one pass, one Query, against six N directions. The player intuits
*fed towns grow, and then they are hungry* from one number they can see at a venue, since
`envelope.changed` is witnessable. **High.**

**Gameplay.** Seasons 1 to `band_seasons`: nothing visible but `envelope.changed` Events. Season
`band_seasons + 1`: the grown band jumps, the larder draw jumps, and `short` appears at a hearth that
was fine. **The decision that gets harder:** *found or feed* — P4's stake competes with the mouths.
**What gets easier and should not:** a lord who levies hands (P3) from a booming town pays nothing
visible until the wave passes. **The delay is the point** (it is Banished's whole lesson) — and it is
also where a player can exploit ignorance. **Named.**

**Emergent narrative.** `envelope.changed(S)` chains to itself; at the crossing season
`stores.changed(S)` → P1's `body.changed` for the **individuated** persons at S, so the crowd's hunger
reaches the named → their questions. The story *"the town grew until the harbour silted"* is a
`causes[]` walk from a `condition.worn` Event through yield to bodies. **Nobody scripted it. Met.**

**Cost.** *Forbids:* a static-population campaign — though the control arm restores it. *Makes
unspellable:* a **chosen** birth ("we married; a child") — birth is envelope weight, not a `create`,
and from-scratch's *"Producer: birth… all acts"* (`04_hearth_and_community.md:155`) is refused, and
named in `05_` §2 row 3. *Corpus:* none broken; **every golden hash re-records**, because envelope
Events enter the log. *Convergence:* **this is the anti-convergence term** — and it is the one that can
spiral if P1 is absent, which is why its `LOOP` row's `default:` names P1 first.

---

## C.3 · P3 · Individuation is a refusal

**N.** *Top-down:* a King who `dispatch`es a bailiff to a hamlet with no persons gets
`dispatch.refused` and nothing else, forever. **Dies.** *Bottom-up:* a crowd at weight 200 that cannot
produce a spokesman cannot `carry` a petition. **Dies.** *Vertical:* **the seam between the statistical
and the named is exactly this**; cut it and the game is elite-only — ideal-v2's named cost
(`01_ARCHITECTURE.md:573-579`). **Dies.** *Diagonal:* a national faction "claiming a settlement" (§5.2)
needs someone there to commit. **Dies.** *Lateral:* a settlement sending settlers (P4 at a distance)
needs a founder minted from its envelope. **Dies.** *Horizontal:* two factions recruiting in one town
compete for the same grown band. **Dies.**
**The attack that failed:** *"`W27`'s authored cast makes runtime individuation unnecessary."*
`W27` builds the cast **the case names**; it cannot mint the smuggler the praefect fines in season 4.
**PASS.**

**R.** *Player:* naming someone is now something you *do*, by acting on "a smuggler"; conscription is a
real strategic act with a visible cost, the grown band; customisation of the minted person is nil —
capability is empty, a named residual against `F.6`. *No player:* the world's cast grows **exactly
where acts happened and nowhere else** — a bailiff's `dispatch` populates the road he uses.
*Completeness:* an empty grown band refuses (§42.2); a demand for weight greater than the band refuses
**whole**, with no partial mint, declared. ⚠ **De-individuation of a person the *player* is looking at**
— ideal-v2's "view assembly" generation trigger (`02:960-961`) must count as a rememberer, **or the
protagonist's contact vanishes between seasons.** Named as a rule P3 must carry.

**S.** Shares `(Person, exists)` at CEN with `W27`; one mint; `F.30` satisfied in the same write.
`W29`'s tenure cache is a **hard** prerequisite — an 11-actor case already exceeds the ceiling.

**E.** A roster and a CENSUS body. The player intuits *if you act on a crowd, someone steps out of it.*
**High.** The nine-member target roster is the only overhead, and it is **marked incomplete rather than
invented**.

**Gameplay.** S1: `levy` for 40 hands → `levy.refused`, nobody to take. CENSUS: a cohort
`Person(weight=40)` at the settlement, contained. ⚠ Who *holds* the levied cohort is `oblige` — which
has no effect today (`W31(a)`); `hold` would be wrong. S2: the cohort has five scenes and a question if
anything landed. **The decision that gets harder:** levy hands from a town you will need to feed.
**Easier and should not be:** a player can farm individuation by spamming `dispatch` at empty rungs —
bounded by scenes and refusals, and `03_VERBS_AND_LOOPS.md` §C.3:136-144 rules that a season spent that
way **is the mechanism, not an exploit**.

**Emergent narrative. ⚠ CORRECTED BY THE ADVERSARIAL PASS — the first draft's trace was impossible.**
It read: *"`levy(R→S)` → `levy.refused` → `person.individuated(crowd_1, weight 40)` → the crowd's Q2
fires on a claim about the levy → `speak` → … **Met.**"* **The crowd's Q2 cannot fire on the levy,
ever.**

The season is `matter → deliberate → resolve → log → witness → census` (`driver.py:1391-1399`). WITNESS
deposits at `:1249-1252`, iterating persons who exist **then**; CENSUS runs after it (`:1399`). **A
Person minted in `census()` therefore has an empty ledger for the season that demanded them**, and Q2
additionally requires `c.when == w.tick - 1` (`world_q.py:194-197`).

> **⚠ AND THE COROLLARY IS GENERAL, AND THIS SET STATED THE OPPOSITE IN THREE PLACES: EVERY EVENT
> EMITTED AT CENSUS IS UNWITNESSABLE**, because WITNESS takes `matter_events + events` and has already
> returned (`driver.py:1398`). That reaches **P3's `person.individuated` / `individuation.refused`**,
> **P2's CENSUS reconciliation emission** — against §C.2's *"`envelope.changed` is witnessable"*, which
> is true only of the MATTER writes — and **P5's crossing "computed at the RESOLVE barrier's end and at
> CENSUS"**, whose CENSUS half nobody can witness.

**The honest trace:** `levy(R→S)` → `levy.refused` → at CENSUS, `person.individuated(crowd_1, weight
40)`. **The cohort's first possible question is `t+2`, and only via a fresh deposit** — someone must
`tell` them, or an act they witness must land. The conscripted-cohort-becomes-the-revolt story is
**available at two seasons' remove, not at one**, and the set should not have claimed the shorter chain.
**Repair, and it costs nothing:** move every emission a proposal wants witnessed into the MATTER step or
into `resolve`'s returned event list.

**Cost.** *Forbids:* a persistent cast unconnected to acts — de-individuation prunes it. *Makes
unspellable:* "a child is born and grows up" as an individual arc; the envelope carries children, and
individuals appear by demand. *Corpus:* cases whose `who_acts` names a person the loop must invent
mid-run become runnable; none broken. *Convergence:* neutral — **P3 is the bridge** between P2's growth
and P5's politics.

---

## C.4 · P4 · Founding and building

**N.** *Top-down:* a Duke cannot plant a colony — SE-9(a)'s lawful half — without a founding act.
**Dies.** *Bottom-up:* a grown hearth cannot split, and its second son has nowhere to go. **Dies.**
*Vertical:* zoom in and any settlement's Sites are world-gen forever; zoom out and no settlement's
yield ever rises. **Dies.** *Diagonal:* the Restoration founding a community at a settlement it does
not hold — the §5.2 cross-scale claim's **physical** form — is impossible. **Dies.** *Lateral:* two
towns, one building a harbour, are identical. **Dies.** *Horizontal:* two factions' `holdings` grow
only by conferral; **a faction cannot make a holding.** **Dies.**
**The attack that failed:** *"`work`/`restore` supply growth."* They move `condition`, never existence;
**a razed site cannot be rebuilt.** **PASS.**

**R.** *Player:* **the first true management act** — where to build, and with what. The method choice is
the stake's *source* (`from` your own hearth, or a Guild member's via `exchange`), which is Goldenfurt's
`Develop: funding=guild` in Layer 1 vocabulary: the counterparty's `hold`/`oblige` edges **are** the
"standing claimant". Customisation of settlements begins here — a harbour town and a mining town differ
by their Site set. *No player:* an NPC with an `OUGHT` about their hearth and enough grain founds, and
**Q4 fires every quiet season** (`world_q.py:223-231`), so the world builds without the player.
*Completeness:* founding at a rung with no parent (a realm) is refused by `presence`; building on a Site
kind with `site_yield = {}` (`body`) is allowed, yields nothing, and is still **a place with a purpose**,
since `band_floors.body` gates verbs. ⚠ **An extreme not handled:** a hearth founded with weight 1 (the
founder) and no envelope share has an empty envelope, so P2 gives it no births. ideal-v2 says it is
*"initialised from its parent Rung's"* (`02:1057`). `assumption`; sweep
`[none, a fixed share, proportional to weight moved]`.

**S.** Two-sided stores writes preserve conservation; the stratum is `uncontested_material`, so it folds
after `movement` and `binding_decision`; `causes[]` runs from `rung.founded` back to the act. **The Rung
closer is CONVENTION and is said to be.**

**E.** Two rows, two effects. The player intuits *grain in, a hearth out.* **High.** The ruin-not-closer
choice is the only argued residual.

**Gameplay.** S1: `found` with 20 grain → a hearth. S2: it draws subsistence and yields nothing, having
no Site. S3: `build` a seam with timber. S4: `yield.taken` ore. **The decision that gets harder:** the
founding stake against the mouths (P2). **Easier and should not be:** a player can chain-found to
multiply `presence` slots — each costs a scene and a stake, so not an exploit under §C.3.

**Emergent narrative.** The colony story: `found` → `move` (settlers, P3-minted) → `site.built` →
`yield.taken` → `stores.changed` → a `levy` from the realm now has a new target → `levy.refused` or
`levy.taken` → the colony's question. **Met.**

**Cost.** *Forbids:* `Prosperity` and `FacilityTier` as **stats** — they are Site sets, i.e. a Query.
*Makes unspellable:* "the town develops" as a single stat pump; `Develop` is gone as a verb and returns
as a hundred `build`s. *Corpus:* the fixed 37-settlement registry is untouched — hearths only.
*Convergence:* an amplifying term bounded by wear, and **a world where every Site is built and worn to
equilibrium is the convergence risk** — `season_factor`'s distribution (`H-26`, a constant today) is the
real anti-stall lever, and it is Layer 1's own named blocker (`holonic:856`).

---

## C.5 · P5 · Commit share and the faction view

**N.** *Top-down:* a King's dispensation to a settlement whose people are committed against him lands on
executors who defy, and without the share nobody can *see* that it will. **Dies** — the resolver cannot,
and Reading 09 says the mayor **should not**, but the **world** must, for bands to emit. *Bottom-up:* a
hamlet's commitments never sum to anything a Duke could lose. **Dies.** *Vertical:* §5.1's *"number of
people and weight of their positions"* has no arithmetic. **Dies.** *Diagonal:* a national faction
claiming a settlement (§5.2) **is** a commit share crossing a band at that rung — **the ratified
mechanic has no other spelling.** **Dies.** *Lateral:* a proposition spreading town to town by `tell`
has no measure of where it has taken. **Dies.** *Horizontal:* two factions' relative strength is a
scoreboard nobody can compute. **Dies.**
**The attack that failed:** *"`members(faction)` is enough; the share is decoration."* `members` is a
**set**; the share is a **ratio at a rung**, which is what §5.2 and Reading 09 both require. **PASS.**

**R.** *Player:* strategy is now recruitment by scenes — `utter`, `speak`, `tell` — and **the player
cannot read the number**, which is `AX-2` and also the game (Reading 09 §2.2). Customisation of
factions: the proposition's `subject`/`predicate`/`value` **is** the faction's identity, authored by an
`utter`. *No player:* NPC factions form because someone with an `OUGHT` (`W27`'s `one_line`) speaks in a
hungry town, and the crossing changes who may act. *Completeness:* zero persons at the rung → the share
is **undefined and raises**, not 0; a person committed to *both* incompatible propositions counts in
`num` — a live contradiction (`09:15-16`), declared. ⚠ **A cohort at weight 200 commits as one mind.**
That is `F.19`'s unsolved half — the "construal spread", ideal-v2's `K = 3` View — and P5 **inherits**
it. **Named as the largest residual in the set.**

**S.** The view resolver is the one Layer 1 named and the code lacks, so filling it is **convergence,
not friction**. `commit_count_guard` guards the sum. The band fires at the barrier and **pauses
correctly** — no person reads it mid-map. ⚠ **S hazard:** two blends for one quantity would return if
anyone re-added `q_s`; `05_` §2 row 4's ruling is that L and PS are **two Queries** blended only at a
consumer.

**E.** Two Queries, one effect, one view, one band row. The player intuits *recruit, and the town turns*
from what they can see: who committed **in front of them**. **High.**

**Gameplay.** S1: the rival `utter`s `OUGHT(S, holder, Y)`. S2: three persons present `commit` — three
scenes. S3: the share at S crosses `third` → `commit_share.band_crossed`, witnessed by those present →
the mayor, **if present**, holds a *claim that a crossing happened*, not the number. **The decision that
gets harder:** for the mayor — `revoke` or `open_case` on rumour, or feed the town (P1) and starve the
recruitment. **Easier and should not be:** under `fan_out_mode=total` the mayor would hold every
commitment — but the ruled default is `all_five` (R7, `fixtures.py:200-207`), so no.

**Emergent narrative.** The civil war: *"ENOUGH NAMED PEOPLE, EACH CHOOSING, IN A SEASON"* (`09:71-72`)
— **P5 is the count of them, and the crossing is the moment**; the `causes[]` walk runs crossing →
commitments → claims → tellings → the utterance. **Nobody scripted it. Met.**

**Cost.** *Forbids:* any stored L/PS/Order/unrest — the whole `registry.py:74-79` block, already inert.
*Makes unspellable:* "the town is 60% loyal" **as a fact a governor knows**; he knows what he was told.
*Corpus:* the 47 faction-scale cases become **behaviourally** representable once re-scaled (`W28`) —
this is their behaviour. *Convergence:* amplifying, bounded by scenes, presence, repudiation and decay;
a world where everyone commits to one proposition converges — **and that world is a realm at peace,
which is a legitimate ending.**

---

## C.6 · P6 · Forswearing costs

**N.** *Top-down:* a King whose Duke defects can do nothing unless the defection **reaches** him; cut P6
and defection is free and invisible. **Dies.** *Bottom-up:* a hearth's head cannot leave a faction at
all today, since there is no effect. **Dies.** *Vertical and diagonal:* a settlement "becoming
independent" (§5.2) **is** its people's commits moving (`holonic:575-576`) — no `repudiate`, no
independence. **Dies.** *Lateral and horizontal:* factions cannot lose members. **Dies.**
**The attack that failed:** *"`revoke` alone models expulsion."* Expulsion is the **superior's** act; P6
is the **subject's** act, and `T-m` says both must exist. **PASS.**

**R.** *Player:* switching sides is a real, priced choice — **priced in exposure and history, not in a
number that can be farmed back**; customisation none. *No player:* an NPC whose scoring now ranks the
rival's `OUGHT` higher repudiates in a quiet season (Q4) — **factions bleed without a script.**
*Completeness:* repudiating a proposition you never committed to is refused. ⚠ Repudiating the **war**
declaration (`10_FACTIONS` §2) is peace by the declarer, and P6 does not reach the case where the
declarer is dead.

⚠ **CORRECTED — an earlier draft of this row said *"`F.32`'s gap stands: the declarer's death leaves a
war nobody can end"*, and a Jordan ruling falsifies it.** `references/design_rulings_2026-09-06.md`
**R1** rules: *"war supersedes the character, typically, but if the casus belli is purely based upon the
character running it, then the inheritors of that war will have justification in negotiating its end."*
The reading recorded there is that **the war is uttered THROUGH THE SEAT, so it survives its declarer
and the successor inherits standing (`T-o`)** — and that this **closes `F.32`**, *"the last surviving
escalation before this ruling."* **So `F.32` is ruled, not open.** What remains true is narrower and is
a bookkeeping fact rather than a design gap: **Layer 1's own `F.32` row is unswept** — `04_CODE:1136`
still reads *"the declarer dies and the war can be ended by nobody"* and still calls for *"an edge
subjected to the seat's holder"*. P6 neither implements R1 nor is blocked by it; **the row wants the
sweep, and the ruling wants a `commit` subjected through the seat, which is a proposal this set does
not make.**

**S.** One effect; the closer half of `commit` (`ID-14`). Pauses correctly. **Consistent in methodology
with `revoke`** — both write `until`.

**E.** One effect and one Query. **The highest ratio in the set.**

**Gameplay.** The Duke repudiates the King's proposition in S3; in S4 the bailiff who saw it `tell`s the
King, spending a scene; in S5 the King's `opening_set` offers `revoke` — **if** the duchy is in his
holdings (`predicates.py:63-67`), which it may not be. *"A King with authority but not holdings cannot
unmake a Duke — a structural stalemate, free"* (`09:32`). **The decision that gets harder:** defect **in
front of whom**.

**Emergent narrative.** That stalemate **is** the story, and it is `T-g`'s obstruction-without-a-verb at
faction scale. **Met.**

**Cost.** *Forbids:* Demotion Magnitude tables, Coup Counters, "Dishonored" states, "Standing 0 in the
new faction". *Makes unspellable:* a **quantified** loyalty — `Tenure.degree` exists
(`carriers.py:58`) and P6 leaves it alone; from-scratch's *"degree of commitment"* would use it, and
that is a separate proposal not made here. *Convergence:* damping.

---

## C.7 · P7 · A dispensation is a document

**N.** *Top-down:* **the entire downward mechanism** (`F.15`) — cut it and nothing above a settlement can
*ask* anything of it. **Dies.** *Bottom-up:* a governor cannot defy what was never issued. **Dies.**
*Vertical:* §3's governance cascade (RATIFIED) has no executable content. **Dies.** *Diagonal:*
Parliament and the Crown "bypassing the chain" (§5.3) **is** an `issue` whose executors are anywhere —
**the scope-enumerates-executors rule IS the bypass.** **Dies.** *Lateral:* a writ carried from one town
to the next is `H-84`. **Dies.** *Horizontal:* the Church's excommunication (Reading 09 §3) is the same
verb. **Dies.**
**The attack that failed:** *"`dispatch` (order.given) covers it."* `dispatch` names a **person** and has
**no terms**; a Directive has terms and executors. **PASS.**

**R.** *Player:* **the vise NPC-083 asks for** — comply, bargain or defy — where the up-tier cost is
*what the issuer learns* and the down-tier cost is what compliance *is* (`extract → transfer` from the
town's larder → P1). Customisation: the terms roster **is** the governance vocabulary. *No player:* an
NPC King with an `OUGHT` about revenue issues; an NPC governor with convictions defies; the King's ledger
fills; he revokes — **or doesn't, because he lacks the holding.** *Completeness:* a dispensation whose
executor died — the Record persists, `comply` refuses for want of an actor. ⚠ A **forged** writ:
`forge`'s row exists, its effect does not, and `forgery_quality` is on the Record with
`[GAP: no reader established]`. ⚠ **The "Sack" fork (ED-FA-0013c) is a term this roster cannot seed** —
it needs Jordan and is left there.

**S.** **Collapses an unmodelled dict kind into `Record`** — fewer shapes, not more. Suspicion becomes
one ledger, and **the two competing accountability instruments (ED-FA-0021 and G606) become one Query.**
Pauses correctly: the compliance contest is per executor at RESOLVE, ordered by the fold. ⚠ **S
residual:** `bargain` = `petition` + `carry` + a Date + `determine`, and it is **blocked on
`H-32`/`W26`** until the sitting decides.

**E.** One Record kind, one roster, effects for verbs that exist. The player intuits *a writ is paper;
paper can be lost, burned, forged, or ignored.* **High.**

**Gameplay.** S1: the Crown `issue`s `extract 40 grain` to the mayor; the bailiff `carry`s it, spending
a scene (`W24`). S2: the mayor holds the claim; `comply` → `transfer` from the town's larder (→ P1), or
`defy` → `compliance.withheld`. S3: the bailiff `tell`s the Crown. S4: `revoke` enters the Crown's
candidates. **The decision that gets harder:** defy, and in front of whom; comply, and starve whom.
**Easier and should not be:** with no mandatory Directive, a lazy Crown NPC issues nothing. Layer 1 says
**that is the game** — but the cost is that NPC-083's *"a Directive response is owed every season"*
(`NPC2.yaml:128`) becomes *"owed whenever one was issued"*, **which is a change to the case's
expectation.** Named.

**Emergent narrative.** *"A mayor excommunicated and ignored is a mayor who is fine"* (`09:154-155`) —
the same mechanism yields *"a writ nobody carried was never defied"*. **Met.**

**Cost.** *Forbids:* the Directive as a clock; `suspicion` as a field; the PA priority tree. *Makes
unspellable:* "the Crown always presses" — it presses when a person spends a scene. *Corpus:* NPC-083's
third and fifth needs are met; **its seventh — self-adjusting pressure — is not met by P7 and is
refused** (`05_` §1 row 1). *Convergence:* damping.

---

## C.8 · The set, read together

Three things are true of the seven that are not true of any one:

1. **The amplifying loops all bound each other.** P2 is bounded by P1; P3 by scenes and P2's grown band;
   P4 by wear; P5 by scenes, presence, P6 and decay. **No `+` row's `default:` cell names a fixture
   nobody has measured** — each names an existing mechanism. That matters because `G13`'s clause 3 is a
   presence check that would accept `"TBD"` (`register.py:329-333`).
2. **The set's weakest axis is expression, and it is unbudgeted.** `08_ch5` §8.2's Tale-Spin finding —
   *"tracking interior state and expressing it as legible drama are different problems, and every
   precedent that solves expression does so by narrowing scope, never generally"* — applies directly:
   P2's envelope Events and P5's crossings are **tracked**, and nothing in this set expresses them
   beyond the log. **Named as the set's one unbudgeted line item**, rather than discovered later.
⚠ **AND A MEASURED CONTROL THIS SET CITES EIGHT LINES OF AND STOPS IMMEDIATELY BEFORE.** `04_` and
`03_` both cite `engine/season/data/fixtures.py:200-207` for `fan_out_mode = all_five`. **That comment
block continues, and the continuation is adverse to P5, P6 and P7's central property**
(`fixtures.py:221-235`): *"**THE COST IS LARGER THAN THE REASON, AND THIS COMMENT FIRST SAID THE
OPPOSITE**… `W-D`, 89 worlds, 1,467 genuine forks… `all_five` (SHIPPED) **0 of 1467**… **Zero of 1,467
is not noise.** At the shipped arm a fork NEVER changes a later decision."* The diagnosis at `:237-265`
sharpens rather than rescues it: *"Every clause-4 drop in the entire corpus… is the verb `move`
refusing on a `contain.path:<person>` belief… **the real defect it exposes is that §F1 clause 4 has
exactly ONE reachable instance in the corpus.**"* **Nothing in P1–P7 adds a second.**
P6's *"forswear unnoticed… that is the epistemic game"* and P7's *"a writ nobody carried was never
defied"* are claims that **knowledge changes outcomes**, made against a tree whose only measurement of
that property reads **zero**. It does not refute them — P7's differentiation runs through **clause 3**
(referents), not clause 4, and is untested — but the set should have cited `:221-269` and said which
clause each epistemic claim runs through. **Recorded here because it is the strongest adverse evidence
against this set's own thesis, and it was found by the critic and not by the author.**

3. **Four of NPC-083's seven `season_requires` are met, two are met in vocabulary only, and one is
   refused with its price.** ⚠ **The first draft scored it "six of seven met" and the adversarial pass
   overturned that on the set's own disclosures.** **Need 3** (`NPC2.yaml:107-109`) asks for a directive
   answerable comply/negotiate/defy *"with **repeated defiance accumulating toward a threshold that
   eventually forces a reckoning**"* — and P7 refuses exactly that second half (*"no threshold recalls
   anyone; a person with the remit **chooses** `revoke`"*), by **the same `T-b` argument used to refuse
   need 7**. **Need 2** (method choice) is met in vocabulary only: its re-expression ends *"effects for
   `exchange` and `levy` are `W31`"* — unbuilt, and not proposed here, which under §0.2 is not met.
   That is the honest score against the only settlement-scale case the corpus has.
