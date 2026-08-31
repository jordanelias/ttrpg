# Arcs 41–55, the emergent corpus, and the scenario chains

## Status: LANE REPORT (2026-08-30) — Arc Lane 3. Read-only assessment. No mechanism proposed.
## Corpus: `gm_ref/arcs_41_45` · `gm_ref/arcs_46_55` + `_resolved` · `emergent_arcs_experimental` ·
## `emergent_campaign_arcs` · `emergent_scenarios` · `narrative_scenario_chains` · `throughline_resolutions_v30`
## Tested against: `proposals/2026-08-29-valoria-from-scratch/` (01, 02, 03, 05, 06, 07, 08, 09, 10, 12, 13, 14)
## Cross-read: `proposals/2026-08-30-play-space-coverage/09_GAP_REPORT.md`

---

## 1. The tally

52 units examined. Nine of them are rules flowcharts rather than arcs (`emergent_scenarios` 1, 2, 3,
5, 6, 7, 13, 14, 15 diagram combat, Thread operations, wounds, belief, gaps, coherence, collective
operations, scale transition and mode collision — they make no narrative claim and cannot be scored
on STORY). **43 units carry a story and are scored.**

| verdict | n | share |
|---|---|---|
| **REPRODUCED-BETTER** | 18 | 42% |
| REPRODUCED | 0 | — |
| **TRANSFORMED** | 10 | 23% |
| **LOST** | 7 | 16% |
| **NEVER-WORKED** | 8 | 19% |

**MECHANISM: NO across the entire band.** Not one arc's stated causal chain survives contact with the
new design, and in almost every case the refusal is by name and with a reason. The band nonetheless
returns 65% REPRODUCED-BETTER or TRANSFORMED, which is the two-layer result the brief predicted:
**the old machinery was scaffolding almost everywhere it was a track, a counter, or a faction stat.**

**The seven LOST arcs share one blocker, and it is not thresholds.** All seven — 48, exp-8's
prerequisite, ARC 5 (Torben), ARC 7 (Southernmost), Scenario 9/Loop A, Scenario 11, Loop D — die on
either *a world-substrate quantity the new design does not have* (five) or *an actor the new design
cannot instantiate* (two). Neither is a threshold problem. §5 separates the two claims, because the
corpus has been conflating them.

---

## 2. The resolved pair: what the old design thought resolution was

`arcs_46_55.md` and `arcs_46_55_resolved.md` are the same ten arcs before and after the design's own
resolution pass. The pair is the most valuable object in my corpus and it does not say what the lane
brief expected.

**The resolution log resolves eleven `[UNVERIFIED]` items, and six of them come back FALSE:**

| id | what the pass found | consequence |
|---|---|---|
| U-01 | Elske Loyalty has **no** Coup Counter link | Arc 47 **rebuilt** around three different triggers |
| U-04 | Warden Cooperation gives **no** Ob reduction on Suppress | Arc 49's mechanical seed **removed** |
| U-05/06 | Experience at Focus 1 costs **zero** Coherence and fires no co-movement | Arc 51's entire causal chain **rebuilt** — its engine was fictional |
| U-09 | there is no "Read Intel" Domain Action | Arc 54 **reframed** onto a different act |
| U-10 | Guild Favour moves **only** on Guild Economic Leverage failure; Crown and Church actions do not touch it | Arc 55's causal chain **replaced wholesale** |
| U-11 | "mercantile efficiency" as the Guilds' framework **was invented** | reference deleted |
| U-07 | PI per-action contribution values exist in **no source** | Arc 52 **unfixable**; flagged as a design gap |
| U-02, U-03 | thresholds cited at RS 50/40 and Coherence-broadcast Intelligibility do not exist | Arcs 48, 54 corrected |
| U-08 | wound → Domain Action propagation **confirmed** | Arc 53 stands |

**Of ten arcs, only 46 and 53 came through untouched.** Six were built on mechanics that did not
exist; one (52) could not be repaired. **The first-draft NEVER-WORKED rate inside this batch was
60%.** That is the measurement the brief asked for about the experimental band, and it is the
band-level answer: *the more experimental the arc, the more of its cited machinery was invented at
the point of writing.*

**And here is the finding that matters for the resolution question.** Not one of the ten arcs gained
an *ending* between the two files. Every resolved arc still terminates at a threshold crossing
(CI 60 → Seizure available), a branch fan (`[Players aware]` / `[Players unaware]`), or an admitted
absence (Arc 51: *"No internal pressure creates the crisis — it must be created by external forcing
events"*). **"Resolution" in the old design meant verifying that the cited mechanics exist. It never
meant closure.** The resolved file is an anti-fabrication pass wearing the word "resolved."

So the comparison the lane was set up to make — *old design resolves, new design only continues* —
cannot be made as posed, because the old design demonstrably did not know what its own arcs resolved
to. §3 answers the real question instead.

---

## 3. Does the new design resolve an arc, or only continue it?

**It resolves, and it resolves harder than the old design did, everywhere an arc's stake can be
brought before a room on a date. It does not resolve — and does not start — the arcs whose stake was
a world quantity.**

**What the old design used to force a position.** A threshold fires and the state machine leaves no
continuation: `Coup Counter = 3` → the coup happens; `CI ≥ 60` → Seizure is available; `PI ≥ 20` →
Parliament auto-resolves; `MS < 24` plus a failed Dissolution → the Rupture. This is forcing, and it
works, but its narrative content is *and then the thing happened*. Nobody is named, nothing is
argued, and the arc's own text says so: Arc 46 — *"When the Seizure threshold is crossed, the Church
does not announce it."*

**What the new design uses instead — four mechanisms, none of which the old corpus had:**

1. **The standing date** (`01` §5.3). A container's calendar makes a proposition contestable, because
   petitions and dispensations addressing the same proposition before the same date are in conflict
   *and both sides know when the argument ends*. Its own N-line names the loss: "deadlines, and with
   them the whole class of politics that exists because two sides know when the argument ends."
2. **Force-close on a named fault** (`08` §3). Twelve computable faults, each with a severity —
   `strike`, `descend`, `close`. **"Force-close is the normal ending. A sitting that runs its full
   budget without a fault is the *unusual* case."** An argument ends because somebody was *caught*
   doing something with a name — F7 rootless ground, F4 shifting the ground, F6 the quibble — not
   because a meter filled. The document's own N-line: *"A threshold roll cannot distinguish 'he was
   wrong' from 'he was caught lying,' and the second is the interesting one."*
3. **Both outcomes bind** (`08` §5). The winner concedes in proportion to the stasis rung he is
   standing on. A motion carried from rung 3 carries *at half the stake, with the other half deferred
   to the next standing date*. There is no clean win, so there is always a next position.
4. **Recorded defeat** (`08` §6), including `CARRIED-WITHOUT-FORCE` — a motion that got its majority
   and was vetoed. It changes no terms, is fully citable forever, enters later sittings at grade G4
   ("the room agreed"), names the vetoer, and arms F2 against him permanently.

That is a stronger forcing apparatus than a threshold in three specific ways. It is **dated** — the
argument has a moment it must end. It is **adversarial** — a position falls because a person attacked
it successfully. And it is **permanent** — the loss becomes an object in someone's custody that arms
a fault check against the loser in every future room.

Add the fifth, from the tick: **one act per season** (`09` §1.1). Arc 45's best beat is Lenneth's
choice between her Einhir programme and her son, and the old design had to *narrate* it — "every
Mandate point spent on diplomacy is a Mandate point not spent on the programme." The new design makes
it the tick's central scarcity, and its N-line is exact: *"A Free Master who can both stand for the
guild seat and answer his Einhir cousin's petition is never Southern Einhir in any way that costs."*

**Where this leaves the arcs.** Arcs 42, 46, 47, 49, 53, 54, 55, the Tribunal (exp-6), the succession
paths (S12) and the Baralta claim all resolve better under the new design than under the old one,
because each has a room, a date and an opponent. Arcs 43, 48, exp-8, ARC 7 and Scenario 9 do not
resolve — but the honest statement is that they do not *continue* either. They are absent, because
their subject matter has no object (§5).

**The one thing a threshold bought that the new design has not replaced.** A threshold *guarantees the
confrontation arrives*. `narrative_scenario_chains` promises this explicitly and repeatedly:
"COLLISION C: Torben at Loyalty 3 coincides with Ceiral Ritual failure"; "the campaign's central
dramatic question answers itself when at least three of the following are true simultaneously." That
is a designer promising the campaign's crises will land together. The new design guarantees only that
*if* they land together, the standing date forces them to fight — because two petitions and a
dispensation before the same date are in conflict by construction and no collision needs authoring.
Whether the peninsula ever *produces* a season with three live crises is an emergent question with no
floor, and nothing in the suite argues that it will. `09` §8.4 runs a recoverability check on a single
grievance loop; **there is no equivalent check that the world produces convergence.** That is the
sharpest unmeasured claim I found, and it is not a threshold problem — it is a question about whether
the tick generates enough coincidence to be a campaign.

---

## 4. Arcs 41–55, individually

### 41 — The Inquisitor's Unravelling · REPRODUCED-BETTER
*A heresy investigator with hidden TS 12 begins perceiving what he has spent a career prosecuting,
and his own proceduralism builds the case against himself.*
Stated mechanics: hidden TS 12 · calamity radiation at node distance 2 during the Fractured MS band ·
PROCEDURALIST flaw · Diagnosis vs Ob 2 · a Defection event card.
Refused: the MS track and the radiation band table (no world-substrate quantity exists); the
behavioural flaw (`02` §3.2 keeps exactly two personality scalars, credulity and obstinacy, and
refuses a trait vector as "a second copy that can disagree with the first"); the event card.
New route: Haelgrund is a person with TS 12 and an Identity conviction. `03` §9's registration floor
gives him rendering-side facets he can register but not construe, because his `admitting_share` is
low — *catechesis is a witness-time term*, so the Church is the unwitting suppressor of his own
perception with no prohibition anywhere. His practice is `examine` and `reconstruct`; each deposits
claims; and **claim identity is a tuple with a mandatory interval, so his new claims collide with the
doctrinal claims he already holds automatically. No designer needs to notice.** That is
"the PROCEDURALIST builds the case against himself," produced by the collision rule the design built
for the 1218 revelation.
Cost: the *simultaneity*. MS is global, so the old arc unravelled him peninsula-wide the season the
band changed. Rendering facets are emitted by events, so the new trigger is *he investigates where
practitioners actually worked* — more causal, more local.

### 42 — The Debate That Changed the World · TRANSFORMED
*A parliamentary debate about whether Thread sensitivity is real heals the world as a side effect.*
Stated mechanics: Memory-genre win → MS +1 if a Thread-sensitive is present · Recall bonus +2D for a
cited verifiable claim · Decisive outcome → faction Mandate +1 · CI passive +1/season.
Refused: the MS track; faction Mandate; the genre/resonance system.
Reproduced better: Lenneth's archive evidence is a **G4 instrument in custody** and beats testimony by
construction. Haelgrund's testimony is a firsthand root against a doctrinal ground with none —
**F7 rootless ground → strike**, which is the arc's "devastating" testimony, computed. Almstedt's
procedural objection is a rung-4 jurisdiction play, and `08` §2 prices it exactly: standing there has
conceded the substance to buy a delay until the next date. Baralta's suppression against Lenneth's
precedent is rung 2 against rung 1 with the concession arithmetic attached. And the debate leaves a
record row that is citable forever, which the old version could not produce.
**LOST, and it is the arc's title:** *the world heals from the argument.* Thread co-movement in the
new design lands on the operator's Coherence (`10` §8.3), never on a world quantity, so "the debaters
who win also heal the world; the debaters who lose also heal the world; the world does not care who
won" has no carrier. The politics improve; the theme is gone.

### 43 — The Battle That Ate the South · TRANSFORMED
*A fight over a farmland corridor becomes an ontological catastrophe because Thread operations in
mass battle cost triple.*
Refused: the ×3 multiplier, MS, the Rupture loss condition, and every faction military stat
(`12` §10 refuses "an army object, a faction military stat, or any national strength scalar").
Reproduced better: the *strategic vacuum* is real rather than narrated — force is a sum over persons,
and Brandt's redeployment removes them. `12` §1.1's Hold, §1.2's willingness term, §2.2's
apportionment by a named person at every rung, and §3.1's commander-changes-the-option-set all
compose. The battle is fully reachable and better modelled.
**LOST: the world-scale stake.** A practitioner's operations in the battle cost *him* Coherence and
nothing else. There is no shared substrate to damage, and no shared loss condition — **the campaign
cannot end in a Rupture.** The arc's thesis, "the generals who chose the battlefield did not know they
were choosing the world's fate," has no object.

### 44 — The Invisible Majority · REPRODUCED-BETTER
*Conviction erodes across territories from three unrelated directions; no faction's strategic lens
spans all three; the population has decided before the institutions react.*
Refused: a per-territory Conviction scalar (`01` §6 refuses "an unrest, loyalty or morale gauge on a
settlement" by name), and the 8-of-15 victory threshold.
New route, direction by direction: tithe extraction → arrears in the creditor's ledger, distraint,
and the neighbours' "we're next" inference (`13` §7); Lenneth's cultural programme → a proposition
travelling by telling, which `05` §5.1 states needs no member to travel with it; the Forgetting's
failure → *thinned to a stub*, recoverable only as `admitting_share` de-concentrating, which nothing
ambiently causes.
The arc's real subject — **nobody can see the aggregate** — is the design's own §1.3 rule: the true
profile may be read by nobody; every observer holds an estimate built from their own ledger.
Almstedt's blindness stops being a flaw script and becomes *his ledger holds no rows about hamlet
sentiment, because nobody told him.* And the threshold is replaced by `05` §5.2's postcondition:
acts are chosen for other reasons and the comparison describes how they came out.

### 45 — The Tutoring Demand That Started a War · TRANSFORMED, two live blockers
*An imperial demand for the Crown Prince arrives the season Crown military capacity, intelligence
security and political attention have all been consumed by other arcs.*
Refused: IP as a global pressure clock with automatic event cards; the Torben Loyalty track; the
Coup Counter; "Mandate −1 for public perception of capitulation."
Reproduced better: the intelligence leak (`03` §7 concealment, §8 correspondence filtering — "the
servant who outranks the ministers"); Lenneth's fork (one act per season); the Crown's structural
weakness, which `14` §6 derives rather than asserts — *"a Crown that conferred few offices can revoke
few offices,"* and levies, consecration, Hafenmark and soldiers are all things it must ask for.
**Blocker 1:** the demand itself has no actor. `00_INDEX` §3.3 names this as genuinely open —
"an off-board polity acting without a person to carry it… 'Generate a person' and 'allow an actorless
pressure' are different games."
**Blocker 2:** the hostage has no play. The play-space exercise verdicts Torben the only SPECTATOR in
55 characters, and D-9 records that "vacancy-by-absence is empty at every rung."

### 46 — The Quiet Seizure · REPRODUCED-BETTER
*An institution wins by continuing to exist while its opponent exhausts itself failing to stop it.*
Refused: CI as a faction-wide scalar; passive advance (`09` §8.3 — "every social quantity moves only
when an act causes an event," enforced by P1's phase membership, not by discipline); Suppress as a
faction Domain Action.
New route: the Church's growth is many `commit` operations and its density profile rises continuously.
The Crown's failing Suppress becomes *its carriers stop carrying*, because each carriage costs the
carrier regard with his own judging set — `09` §8.4: "which way the fork resolves depends on the
carrier's address." "Winning on momentum alone" becomes "winning because no individual's private
cost-benefit favours opposing you," which is a better version of the same story and needs no scalar.
The Seizure at CI 60 becomes conferral conversion — `14` §6 names the Church's operation on
`sovereign_fraction` as "raise the numerator for the Confessor's root," one office at a time, at a
venue, against a holder who contests it.

### 47 — The Counter She Keeps · REPRODUCED-BETTER (best conversion in the band)
*Three independent triggers arm a private counter nobody can see; it never decrements; the coup fires
because attention was elsewhere.*
Refused: the counter — a hidden threshold object with automatic increments read off true state.
New route: `09` §9's latency ruling is this arc. *"A latent act is a stance toward a proposition of
the form `act(…)`, held above the commitment threshold, whose act is not in the person's option set
until they hold an enabling claim."* Ehrenwall holds `act(demand_or_depose)`. Her three triggers
become three *claims that must reach her ledger* — and here the new design is strictly better,
because **she may be wrong.** In the old design the counter reads true state. In the new one, her
estimate of Crown competence is built from her ledger; a rival can `plant` a claim that arms her, or
a true one may never reach her. "The counter never decrements" is derived rather than declared —
stance rows do not decay, because no phase exists in which a restoring timer could run. "Private"
becomes "in one woman's head," which is the strongest possible form of private.

### 48 — The Practitioner Economy · **LOST**
*Individual optimisation degrades shared infrastructure; the degradation raises the difficulty, which
raises the failure rate, which accelerates the degradation.*
Refused: MS, and every band effect on it.
Partial: the *personal* half survives and is well built — `10` §8.3's Coherence drift, with the
recoverability check run at the extremes and Severed reachable in ten seasons (2–3 under
contested-op-heavy play). `13` §5's slow fuses reproduce the *shape* (a hidden shared variable
degrading, discoverable only by investigation, dooming a settlement decades later) in **material**
terms — ore grade, harbour siltation.
**Blocking mechanism, stated precisely: there is no world-substrate state that any person's act can
degrade.** The material version exists (`09` §8.3 explicitly allows matter to be clock-driven, and
`13` §5 proves it). The metaphysical version does not, and no player act accelerates the material
one. The arc's thesis — *the commons that practitioners deplete by practising* — has no home.

### 49 — The Mediator's Debt · REPRODUCED-BETTER
*A party acquires leverage it never sought, because it is the only one who can perform an operation
everyone needs, and now every faction must keep it stable.*
Refused: faction Domain Actions, the ethical-framework Ob modifier, the `[PROVISIONAL]` Hafenmark
Stability gate.
New route: the carrier. A Hafenmark burgher whose own judging set *rewards* carrying against Church
overreach carries reliably where a Crown officer's set punishes him for it — `09` §8.4 states this in
those words. Both the Crown and the Church now need *that man* to keep carrying, so both must protect
his standing. And the arc's Stability gate is replaced by something far better: `02` §5.2's Fractured
band — *"you may not `carry` a petition — nobody will let you speak for them."* The disqualification
becomes social rather than numeric, and lands on a person rather than a faction.

### 50 — The Counter That Runs Backward · TRANSFORMED
*Varfell's correct play for its own goal mechanically accelerates the enemy it is playing against.*
Refused: both tracks and the PP-563 coupling constant.
New route: the self-defeat survives as an *arithmetic* property. `14` §6 names Varfell's operation on
the sovereignty fraction as "delete a whole cluster from the scope: expel the Church's offices,
shrinking the denominator and the numerator together" — genuinely self-undermining, and derived.
What changes is the **discovery**. The old arc's best beat is that the link is invisible without an
Audit action or an NPC disclosure. In the new design the fraction is computable by anyone — but only
over offices they hold claims about, and `14` §6 says nothing stores it. So the discovery beat is
partly recovered through the view budget rather than through a hidden constant.

### 51 — The Weight of Sight · REPRODUCED-BETTER
*A practitioner whose perception outruns their capacity to act, at a widening gap, with no internal
pressure to close it.*
The pre-resolution form was fictional (Coherence decay from Experience does not exist). The rebuilt
form is honest and admits it has no engine: *"No internal pressure creates the crisis — it must be
created by external forcing events."*
New route: the new design supplies the engine and a second failure mode. Per the play-space report,
verbs gate on a practice at rank 3+, so high perception with no practice is an empty verb set rather
than a weaker pool — the Focus-1 case exactly. And **the gap report found the same shape
independently**: "Thread Sensitivity is non-monotone… below 30 you cannot hold the informal channel
at all, and far above the rendering floor you hold content nobody can receive. The Warden-Chief at
the highest living TS and the control at TS 4 are both structurally inaudible, for opposite reasons."
The old arc's tragedy is *I can see and cannot act*. The new one adds *and cannot tell*, because a
rendering claim degrades on deposit into any ledger with no address for a configuration.

### 52 — Parliament as Weather · **NEVER-WORKED**
*An institution collapses from the aggregate of everyone's legitimate normal operations.*
Its own resolved file kills it: the per-action PI contribution values "are not specified in any
fetched source" and remain "a design-layer gap requiring a future table." An arc whose entire chain
is `+N per action` with N undefined has no chain — and the two PI tracks bearing the same name
(0–10 TTRPG, 0–20 BG start 7) are incompatible.
Story assessment, recorded separately per the brief: **partially reachable, currently obstructed.**
`08` §7.2's `pattern` counter gives accumulation-from-legitimate-use with no decay timer — "a
proposition carried-without-force four times is a different political object from one raised once."
The coordination problem is `09` §8.4's carrier fork. But the *collapse* is blocked by a known
defect: D-5, "a councillor has nowhere to stand — inner councils and jarl councils appear in no venue
table, so they can neither contest nor argue. This is the most populous character type in Valoria."

### 53 — The Wound Economy · REPRODUCED-BETTER (the corpus's own best evidence)
*A scene combat nobody thought much about becomes a faction-layer crisis three seasons later.*
The only arc in the batch the resolution pass confirmed outright, because it was already
person-rooted. **The new design does not reproduce it — it makes the alternative inexpressible.**
There is no faction pool to propagate *into*: containers do not decide, factions do not decide, and a
wounded duke's acts are worse because *his* pool is worse. The old design needed a rule to make a
personal wound matter at the strategic layer; the new one cannot express a world where it does not.
`12` §10 refuses the faction military stat that supplied the arc's "bonus dice," so the arc gets more
extreme, not less — the leader *is* the pool. Add one act per season: a wounded duke spends it on
recovery or on the duchy, never both.

### 54 — What The Unaffiliated Know · REPRODUCED-BETTER (strongest convergence)
*Distributed observers independently report an anomalous figure; cross-referenced, the reports
produce a real but categorical profile; the party is in the file before it knows.*
Refused: Intel as a faction stat, the Intel Advancement Counter, the hypothesised observation action.
New route: `03` §5's corroboration-fails-closed is this arc's thesis, made checkable. *"Two claims
are independent only if their firsthand roots differ. A rumour with no findable origin is given a
single synthetic root shared by every retelling, so one story told three times corroborates exactly
once."* The old design asserted that scattered reports become a pattern; the new one computes whether
they do. `surveil` deposits firsthand rows over an interval; `reconstruct` performs root
identification. And the profile is categorical rather than numeric **because the type conversion
loses the number** — a non-sensitive's ledger has no address for a configuration, so what deposits is
`CONDITION(the man, wrong)` at 0.2 — rather than because a canon note says P-08 forbids it.
Two designs, four months apart, derived the same object from opposite directions.

### 55 — The Withdrawal · REPRODUCED-BETTER
*A third party you relied on stops being able to act, through its own failures, with no input from
you and no path to repair.*
The pre-resolution form was fully fictional. The rebuilt form is a single binary eligibility gate at
Guild Favour 5 with no upward path, and its own file flags the missing restoration mechanic as a
design gap.
New route: `02` §5.2's Fractured band and `05` §4's carriage give the withdrawal — Free Masters whose
judging sets have turned will not carry, so the guild's petitions stop entering the settlement and
the Crown's buffer evaporates without anyone deciding to remove it. **And the arc's own flagged gap
closes by construction:** regard is per-person and moves on acts, so a Crown that wants the buffer
back must spend acts on named men — which is `09` §8.4's sixteen-act-slot trade, "essentially
Goldenfurt's whole governing capacity for the season."

---

## 5. The experimental and emergent sets, and the two blockers

### The experimental four (Threadweaving v2.5 / Debate v1 / Mass Battle v3)

**Exp-5 The Brittle Peace · TRANSFORMED.** Over-actualisation, Relational Gaps and a
`GM rules: brittleness applies` node all vanish. But the irony survives, relocated: `08` §2's rule
that *opening at rung r writes every rung above r into the record as conceded* means the strongest
opening is the one with the most to lose, and a party that wins at rung 1 has conceded nothing and
must survive every challenge to its denial. **That is over-actualisation brittleness, derived, at the
level of the record instead of the substrate.** The GM node disappears because the fault checklist is
computable.

**Exp-6 The Tribunal and the Temporal Shimmer · REPRODUCED-BETTER.** `08` is a better tribunal than
the one the arc describes. The accused's structural disadvantage stops being a missing debate phase
and becomes the venue's admissible-proof table, enforced by F10 (speaking without standing → strike)
and F12 (inadmissible challenge → descend), whose own worked example is "impeaching an Archives
register in the Doctrinal Dicastery." F11 adds a weapon the old design lacked: an accused whose
Coherence band is Fractured has **all** his grounds struck, so the Church can win by driving him
there. The shimmer's *world* consequence is lost with the substrate; its *epistemic* consequence is
strengthened — the sensitives who witnessed cannot tell anyone, because the claim degrades on
deposit. A type conversion replaces a Certainty check.

**Exp-7 The Rendering Debt · REPRODUCED-BETTER.** The best-served arc in my corpus, because its costs
were always person-scale. `10` §8.3 gives the drain with the recoverability check run; `02` §5.2's
bands change structure rather than dice; and **Severed is a harder and better Rendering Crisis than
"becomes an NPC"** — *"you stop individuating. You return to cohort fidelity, cannot originate
petitions, cannot hold office. A person has become an object."* The belief-blocked recovery becomes a
second practitioner's willingness, which is a decision rather than a pre-op check, and `02` §5.3 caps
Knot contagion at one step per season so the cascade the arc feared cannot become an extinction event.

**Exp-8 The Temporal Window · TRANSFORMED.** The MS ≤ 60 prerequisite is lost. The rest survives and
improves: `09` §9's latency makes the window open **when the enabling claim arrives, not when a track
crosses**, which is the same "the window opens as a side effect of everything else" with a per-person
carrier. And Temporal Disjunction is kept by name — P-09 memory-pulling writes an orphaned
configuration, *and* the SAID rows that pointed at the deleted claim now dangle, so `reconstruct`
reports the erasure. **Two detection channels, one supernatural and one clerical**, where the old arc
had a Certainty check.

### The four original emergent arcs

**Emergent-1 The Coup That Wasn't Supposed to Happen · NEVER-WORKED** — its file's own header records
that Löwenritter Autonomy was replaced by graduated autonomy. Its story is Arc 47's.
**Emergent-2 The Vaynard Revelation Cascade · TRANSFORMED** — "helping him raises a clock you must
suppress" needs a clock. The substitute is that a patron's rise is offices conferred, and conferral
is `admit()`, which names you. Reachable, materially different.
**Emergent-3 The Invisible Drain · NEVER-WORKED** — Niflhel dissolved by canon. Grace note: the gap
report records that the new design handles a struck institution correctly, because every consumer
reads persons and no decision function reads a registry.
**Emergent-4 The Axis 9 Resolution · TRANSFORMED, and it is the corpus's most interesting change.**
The arc's terminus is "Thread knowledge enters the public record; Inert Knowledge upgrades for
non-sensitives who held it." **The new design makes that structurally unreachable, deliberately** —
`03` §9: *"give him the sensitive's own written testimony, in the sensitive's own hand, and nothing
changes… The only thing that changes it is TS crossing the floor — the hearer becoming able to
witness, not to learn."* The political fight is fully reproducible; the winner simply cannot make the
peninsula *know*. They can only make it *rule*. The old design's ending was epistemic; the new one's
is institutional, and it is truer to P-08 — but it is a change, not a reproduction, and the arc is
the evidence.

### The two blockers, stated once

**Blocker A — no world-substrate quantity.** Eleven of my 43 units run on MS, Gaps, Shifting Objects,
monstrous incursion, or the Rupture. The new suite has **none of them**: no MS, no Gap object, no
world loss condition. "Locked Zone" survives only as a place name and a practice provenance.
Crucially, `09` §12's refusal list — which is otherwise exhaustive and names morale bars, unrest
meters, grievance thresholds and simulation radii — **does not name it.** This is an omission, not a
reasoned refusal, and it is the single largest finding this lane returns.

**Blocker B — no actor for an off-board polity.** Arcs 45, ARC 5, ARC 11, COLLISION C. The suite names
it open in `00_INDEX` §3.3 and does not choose.

Neither is a threshold. **Which brings me to the sharpest single question the brief asked.**

### Does the refusal of thresholds cost stories? In this band, no.

Every threshold in my corpus that gates a *person's decision* is replaced by something strictly
better: the Coup Counter becomes one woman's private and fallible ledger; Guild Favour 5 becomes a
judging set that will not let a man speak for them; CI 60 becomes conferral conversion at a venue;
PI 20 becomes a `pattern` counter with no decay. Every threshold that *reports a world state* — the
MS bands, RS 0, the Rupture — is lost, **and the loss belongs to the variable, not to the threshold.**
Give the new design a substrate quantity and it would need no threshold to make it matter, because
`05` §5.2 already shows how to make a comparison a postcondition rather than a trigger.

The corpus has been conflating these. They should be reported as two independent findings: *the
threshold refusal costs nothing here*, and *the missing world quantity costs seven arcs.*

---

## 6. The scenario chains, and the two chaining architectures

This is the cleanest architectural comparison available, and it decisively favours the new design
while exposing exactly one thing it has not replaced.

**Old chaining — by shared global variable, with authored conjunctions.** An arc node states a
trigger on global state (`IP ≥ 30`, `CI reaches 40`, `Coup Counter = 3`, `MS 50`) and downstream arcs
are wired by hand: `→ FEEDS Arc 42`. Arcs 41–45 ship a **35-row Trigger Inventory** and a
**Convergence Timeline by season**. `narrative_scenario_chains` ships a **CROSS-ARC COLLISION MAP**
with exactly five named collisions, A through E. So: the coupling is via scalars, the chain graph is
authored, and **a collision exists because somebody wrote it down**.

**New chaining — by claim arrival into one named person.** A claim enters a ledger; P0 recomputes
option availability from claims; an act-proposition held above the commitment threshold enters that
person's option set. `09` §9 is explicit that this needs no new object: *"there is no flag object;
dormancy IS an act-proposition with an unmet enabling claim."*

Three consequences, all in the new design's favour:

1. **Chains are per-person.** The same event chains differently for two people, because it lands in
   two ledgers as two claims with different construals. The old design cannot express this at all,
   because the coupling variable is global — when MS drops, it drops for everybody.
2. **Collisions need no authoring.** Two petitions and a dispensation addressing the same proposition
   before the same standing date are in conflict *by construction* (`01` §5.3). The five hand-written
   collisions become a property of the calendar.
3. **A chain can be armed by a lie.** Ehrenwall's counter increments on true state in the old design;
   in the new one it increments on a claim, which can be planted (`03` §6, `plant`), distorted in
   transit, or never delivered. That is a whole class of play the old architecture forbids.

**What the old architecture bought that the new one has not replaced:** the guarantee that
convergence occurs (§3, last paragraph). The Convergence Timeline is a designer promising the
campaign will get interesting in seasons 7–8. Nothing in the new suite makes that promise or measures
it.

**Chain-by-chain (nine chains, five collisions):**

- **ARC 1 The Hunting Accident · NEVER-WORKED** — struck in its own file by PP-675. But it is the
  **single strongest piece of evidence in this exercise**, because `09` §9 takes the 1218-AG hunting
  accident as its own worked example and runs it end to end: the huntsman's firsthand claim, the
  written carrier in the Dicastery archive, sixty years of nobody able to read the world's true event
  record, `search(archive)`, the automatic contradiction from tuple-identity, and Inge Baralta's
  claim banked at her marriage entering her option set the season the enabling claim lands. The old
  arc's best beat — *"partial investigation produces confident wrong answers,"* because each
  faction's trail was built to implicate its rival — is `03` §5's corroboration rule exactly: the
  trails' roots collapse to each faction's own informants, and F7 strikes the ground.
- **ARC 2 Almud's Sympathies · REPRODUCED-BETTER** — a sum of three faction-scalar penalties becomes
  a structural constraint: one act per season, plus `14` §6's list of what the Crown *must ask for*.
  The gap report independently verdicts Almud THIN with the largest remit and the thinnest reach,
  which is a warning about playability rather than a refutation — this is an arc about a man who
  cannot act.
- **ARC 3 Baralta and the Solmund Claim · NEVER-WORKED** — carries `[EDITORIAL — no canon source]`
  and `[EDITORIAL: Ob and effects TBD]`. Its successor exists (`08` §10.1 is titled "The Baralta
  Crown Claim, composed") and is a **named defect**: the gap report records that Inge has eleven live
  acts and none touches the article her whole claim turns on.
- **ARC 4 Niflhel Exposes the Church · NEVER-WORKED** on the actor (Niflhel struck). Story fully
  reachable: the SAID-row graph, F7, record rows, and `12` §6.3 on an office-holder whose orders are
  not obeyed.
- **ARC 5 Torben in Altonia · LOST** — a Loyalty clock decrementing on a schedule is refused by name;
  and the deeper blocker is D-9, vacancy-by-absence, empty at every rung.
- **ARC 6 Elske · REPRODUCED-BETTER** — "Resonant Style: Evidence — show her proof; abstract appeals
  fail" is graded proof plus credulity and stance-toward-speaker, computed rather than declared. Her
  two unresolved Convictions are priors; her being genuinely torn and controlled by nobody is the
  needs split between world-reading and view-reading.
- **ARC 7 The Southernmost Spiral · LOST** — Blocker A, and it also carries GM-set thresholds.
- **ARC 8 Ehrenwall's Coup · REPRODUCED-BETTER** — see Arc 47.
- **ARC 9 Vaynard's Knowledge Ladder · REPRODUCED-BETTER** — TK 0–5 with authored per-level effects
  and a *forced* Belief revision at TK 5 becomes a ledger and an obstinacy check. And the arc's own
  best line — a failed Discovery Event makes "Vaynard more dangerous in his confusion than in his
  clarity" — is `03` §6.1's stated risk of `reconstruct` verbatim: *"the risk is that a wrong
  reconstruction deposits at real confidence and is acted on."* A third four-month-apart convergence.
- **Collisions: A** (Church double fracture) REPRODUCED-BETTER; **B** (Einhir Practitioner King)
  TRANSFORMED per Emergent-4; **C** (Tutoring + ritual failure) LOST on both blockers; **D**
  INVALIDATED in its own file by PP-675; **E** NEVER-WORKED (depends on an NPC "not yet canonised").
- **Emergent scenarios:** Scenario 8 / Loop B (Church dominance lock) TRANSFORMED onto power bases
  and the sovereignty fraction; Scenario 9 / Loop A (the Einhir Spiral, the file's "most common
  campaign-ending pattern") **LOST**; Scenario 11 (Altonian chain) **LOST** on Blocker B;
  Scenario 12 (succession) REPRODUCED-BETTER via `14` §2, including "there is no interim and no regent
  object," except the Torben branch; Loop C (Coherence cascade) REPRODUCED-BETTER, with the contagion
  cap as the fix for its runaway; Loop D ("the window closes precisely when it's needed most")
  **LOST** on mechanism, its irony partially recovered by `13` §6's cordon that saves lives and
  manufactures the next crisis.

---

## 7. What `throughline_resolutions_v30.md` actually is, and what it revealed

**First, a correction the lane brief needs.** This file is not about the nine throughlines the new
suite was built on. It is a 2026-04-17 document resolving **ten second-order integration questions**
raised by a faction-politics rank-ladder expansion — caste onboarding, Standing 0 duty
reconciliation, the Warden ladder, clock convergence, NPC roster capacity, hall tiers, and three
process items. The name collision is unfortunate and a later session reading the filename cold would
be misled.

It is nonetheless the most useful file in my corpus, because six of its ten are structural questions
the new design must also answer — and comparing the answers is the cleanest available test of whether
the two designs reach the same place.

| # | what the old design resolved it to | where the new design lands |
|---|---|---|
| **TL-1 caste onboarding** | a static 20×3 Viability Matrix shown at character creation, with ✕ Closed cells and a verbatim "why this matters" note | `02` §1.3 — *"Caste is not a rule. It is a distribution of stance across the persons who hold gates."* The ✕ cells become the committee's stances and **change when they change**. Better — but see the loss below |
| **TL-2 Standing 0 / duty** | an Initiation Duty carve-out and floor-protected ranks | remit and establishment plus community admission. Rank-floor protection dissolves into per-person regard. No loss |
| **TL-3 Warden × CI; the RM ladder** | a CI-indexed Ob pressure table; and an RM ladder built to rank 5 and then **refused above it on ideological grounds** — "a formal rank ladder would violate the movement's design premise" | `07`'s secrecy and exposure replace the table. The RM's anti-ladder is `14` §6: *"shrink the denominator to nothing: dissolve offices with binding power so that no root can hold them… the only operation available to a faction with no Mandate, no wealth and no soldiers."* **Convergent, and the new answer is principled where the old one was apologetic** |
| **TL-4 clock convergence** | a hand-written precedence order for same-accounting collisions — succession, then coup, then IP — justified as preserving narrative coherence | `09` §1.4's five resolution strata, ordered by *causal dependency* rather than narrative importance, with social acts last "because they are about what happened." The new principle is right. **But see the gap below** |
| **TL-5 NPC roster capacity** | a cap of ~35 Active NPCs with four ordered demotion triggers, justified by "companion-app tracking plus GM narrative load" | `01` §2 / `09` §8.2 — *"A person persists exactly as long as somebody remembers them,"* de-individuating when no role, no Knot, no live petition and **no other person's ledger names them**. Same problem, same solution shape, **and the new design derives the bound from the world's memory instead of a display constant.** The strongest convergence in the file |
| **TL-6 Hall Tier** | Institutional Facility slots per settlement type, allocated by the controlling authority, durable across seasons, blocking advancement when full, with an Expand-Capacity act and a decaying "Prince-in-Waiting" provisional rank | **Nothing.** This object does not exist in the new suite |

**Three findings from this table.**

**(1) TL-6 is a throughline where the old material has an answer the new design lacks — and the
play-space exercise found the same hole from the opposite direction.** Its gap report names, as its
second-strongest predictor of a thin character, "an empty or unreachable *establishment*, never a
small remit," and concludes: **"the design prices remit and forgets establishment."** TL-6 is
precisely an establishment mechanic: finite, contested, durable, politically charged when full, with
a named act for expanding it and a named provisional state for waiting. Two exercises that could not
see each other, four months apart, converging on one missing object is the strongest signal this
process produces. **This is the single most actionable item in my report.**

**(2) TL-1 costs one small, real thing: informed consent at character creation.** The new design's
answer is better in every respect except that a player choosing Southern Einhir plus Church Justice
receives no signal that the combination is effectively closed, because there *is* no cell — the
closure is emergent from committee stances. The design already owns the rule that would fix it
(`03` §10: "publish every input, publish a band, never publish the trigger point"), and nothing says
it applies at creation.

**(3) TL-4 exposes a shape the new design may not cover.** Its Scenario C is a **four-claimant
contested succession** firing in one accounting step. `08`'s chamber takes a motion with a mover and
a respondent, and `08` §9.2 handles "what happens when the sides are not close" — but four
simultaneous claimants at one standing date is not obviously the same object. Flagged, not
adjudicated.

---

## 8. NEVER-WORKED, and what the corpus wants

**NEVER-WORKED count: 8 of 43 scored units (19%).** That is a floor, not a ceiling, and the file-level
evidence is considerably worse than the arc-level count:

- `emergent_campaign_arcs.md` carries a header striking two of its four arcs as referencing
  dissolved systems.
- `narrative_scenario_chains.md` strikes its own ARC 1 (PP-675) and invalidates COLLISION D, and
  marks ARC 3 and COLLISION E as `[EDITORIAL]` with no canon source.
- Both `emergent_arcs_experimental.md` and `emergent_campaign_arcs.md` carry "Not valid against any
  post-CP14 ruleset."
- `arcs_46_55.md` ships an eleven-row `[UNVERIFIED]` table, and **six of those eleven resolved to
  "this mechanic does not exist."**

**The measurement the brief asked for: within arcs 46–55, the first-draft NEVER-WORKED rate was 60%.**
Six of ten arcs were built on invented machinery, and only a dedicated verification pass brought that
to one unfixable arc. The experimental band's high scaffolding rate is real, and it is a finding about
the old corpus rather than about the new design.

**What the corpus demands that the new design has no object for**, ordered by how many units want it:

1. **A world-substrate quantity that acts degrade and that degrades options in return** — 11 units.
   Not refused; omitted. `09` §12's otherwise-exhaustive refusal list does not mention it.
2. **An off-board polity that acts** — 4 units. Named open by the suite itself.
3. **A guarantee that crises converge** — every collision block in the corpus. The new design
   guarantees a *forced decision when* they converge and nothing about *whether* they do. `09` §8.4
   runs a recoverability check; there is no convergence check.
4. **An establishment/capacity object** (TL-6) — the throughline file and the play-space exercise
   independently.
5. **A person removed from the board** — 4 units (Torben, Elske's extraction, Almud's absence). D-9.

**One caution on how to read my verdicts.** At least five of my arcs run on a character the play-space
exercise verdicts BLOCKED-CORE: Lenneth (Arcs 44, 45), Vossen (Arc 44 — "seven verbs, and her season
reduces to *speak, and hope*"), Inge Baralta (ARC 3, COLLISION E), Maret Uln (Arc 43 — "agency in her
own defining conflict is zero"), and Torben (Arc 45, ARC 5, S12 — the only SPECTATOR in 55). Haelgrund
in Arc 41 has Torsvald's exact SPLIT shape: rich as an investigator, blocked as an advocate. **Arc
reachability and character playability are different properties.** A REPRODUCED-BETTER verdict says
the story is reachable by composition; it does not say the person at its centre can pursue what they
want. Where the two exercises meet, the arc survives and the protagonist does not.

---

## 9. What I would hand Jordan from this band

1. **The missing world-substrate quantity is the one real architectural hole**, it costs seven arcs
   and eleven units, and it is an omission rather than a decision. It should be *decided*, either way,
   in the refusal list where the other twenty-odd refusals live. `13` §5's slow fuses prove the design
   can hold a shared, hidden, investigable, act-independent quantity; nothing decides whether the
   Thread gets one.
2. **The threshold refusal costs nothing here.** Report it as a success. Every person-gating threshold
   in this corpus is replaced by something strictly better, and the design's four forcing mechanisms
   — standing dates, force-close on named fault, both-outcomes-bind, and the record row — resolve
   arcs harder than a threshold ever did.
3. **Nobody has measured whether the world converges.** That is the one property the old architecture
   guaranteed by authoring and the new one leaves to emergence. It is measurable — run a seeded
   campaign and count seasons carrying three or more live crises at one standing date — and it is
   more load-bearing on whether this is a game than anything else in my band.
4. **Build the establishment object (TL-6).** Two independent exercises found the hole.
5. **The resolved pair is worth keeping as a method artefact**, not as canon. It is the only place in
   this repository where somebody checked a design document's citations against the mechanics they
   named, and it found six fabrications in ten arcs.
