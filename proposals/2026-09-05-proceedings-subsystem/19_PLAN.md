# 19 · THE PLAN — what to build, in what order, and how each step is proved

## Status: **PROPOSED (2026-09-06). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Planner: `fable`, read-only (`relay/H_FABLE_PLAN.md`). Written up and verified here.
## Scope: the session from *"fears"* to now, and the design owner's comments across it.

---

> # THE SHAPE OF IT, IN ONE PARAGRAPH
>
> **Make the ledger able to hold a reading of a person; make this subsystem the single owner of every
> social contest through the seam; then join the two so the obstacle reads what the room holds.** In
> that order — because the first is measurable today on the existing harness with no proceeding in the
> world, the second is now ruled, and the third is where the flowchart becomes a game.
>
> **Twenty-seven instructions in four phases. One new field in the whole plan. Four fields deleted,
> three arrangement keys cut, one dead channel removed.** Every step ends in a run, a hash, or a
> red-then-green test — `§0.2`: a document with a status line counts for nothing.

---

# PART A · THE TWO RULINGS THAT RESHAPED THIS, AND WHAT THEY SETTLED

## A.1 · *"this subsystem obviously owns all social contests"*

**This closed the largest open question in `18_FINDINGS.md`** (PART M item 6), which asked whether the
subsystem owns the contest at all and warned it was *"the one question here that changes everything
downstream."* Three consequences, all now instructions rather than questions:

- **The seam dispatches by row, not by a hardcoded literal.** The manifest row lands (step 8), and
  `personal_combat` keeps working through the same lookup.
- **The two prize rows repoint here** (step 9). `README.md` had recorded that this directory left them
  untouched because repointing supersedes other work by editing one line, and `§2` says that must be
  loud rather than quiet. It has been made loud.
- ⭐ **The obstacle has a single owner.** Several mechanisms were hedged against the possibility that
  another module composed the same quantity. **Every one of those hedges is gone.**

## A.2 · *"of course we accept those shapes"*

**The multilateral tally and the debate score are accepted.** Neither needed new theory:

- **The multilateral disposal's construction was already written down** — `05_PROCEDURE.md:110-116`
  specifies a **Query over the bench's live determinations, evaluated by a later act — somebody
  declares, and the declaration is the write** — and then declines to build it. `P-15` closes.
  Conclaves, votes, majority verdicts and five-party settlements come into range (step 15).
- **The debate score was mostly already licensed** by the owner's own *"why can't we have aggregates
  in a subsystem?"* — inside a proceeding it dies with the run, so it is free (step 14c). Only a
  cross-season version needs a carrier, and that carrier is a **`Record` somebody wrote, carried and
  can burn** (step 26), never a field.
- ⭐ **And it repaired a cut.** `records_dissent` was on the delete list for having no reader. **Under a
  declared disposal it is the tally made visible** — it scopes whether the members' commitments leave
  the room. Withdrawn from the cuts (step 11).

**Every refusal in the directory was re-sorted under this ruling** into *genuinely forced* · *provisional
and now accepted* · *cut for being bad design rather than unlawful*. PART G.

**One boundary was deliberately not extended, and is flagged rather than assumed:** that you cannot make
another person a party, write their interior, or act through them. It is the wall the design rests on —
and it is what makes the fear lever lawful at all, because the coercion happens **inside the target, by
their own reading**, never by your write. It holds throughout; the one mechanism adjacent to it is
escalated in PART H, not built.

## A.3 · The earlier comments this plan is built on

| the comment | what it settled |
|---|---|
| *"Valoria characters are under defined … goals and ambitions, allegiances, memories, beliefs, convictions, ethical stances, pressures, stresses, relationships"* + **"fears"** | the character model is the spine of the plan — PART D |
| *"why can't we have aggregates in a subsystem?"* | ⭐ an aggregate cannot be a **field**; a **Query is its licensed form, not a refusal**; a barrier cache is allowed. **Per-proceeding aggregates are free.** Three of them are built in step 14 |
| *"whatever works best for the subsystem is what goes, so long as it can receive input and give output to seasons"* | ⭐⭐ **the governing ruling.** The zero-new-primitive count is a **tiebreak, never a constraint.** The seam is the only hard boundary — read-only projection, no write token, Events out, a Margin back |
| *"secrets can be threatened for revealing, and they can be contained if closed doors technically"* | a secret is a **distribution fact**; threatening is pressable, revealing spends it, a closed floor contains it — **and all of it is impossible until fan-out stops being total** (step 1) |
| *"naming a fear once only is dumb. fears are leverage that you can press"* | pressable leverage with changing returns. The audit modelled it against the deposit path and **refuted the coordinator on the diminishing return** — it needs a habituation clause (step 5) |
| *"degrees of success … interpolation of states otherwise unavailable"* · *"fail forward"* · *"the wrong choice can still land and the right choice can still fail"* · *"each figure by showing success thereby shows failure"* | the standing principles. Every band must leave the proceeding somewhere the others do not; failure changes course rather than negating |

---

# PART B · THE CRITICAL PATH

**Neither `18_FINDINGS.md`'s ordering nor `12_BUILD_ORDER.md`'s was inherited. Both were tested against
what each step needs in order to RUN, and the result is two independent stems that join once.**

**Stem A** (the season loop's witness and deliberate barriers) and **Stem B** (the seam) do not depend
on each other to execute. Everything in Phase 1 runs on the existing harness **with no proceeding in the
world**; everything in Phase 2 runs through the contest call **with an empty ledger**. They meet at
`reception`, which needs both a composed obstacle to enter and attributed, differentiated claims to read.

## B.1 · Two corrections to the findings' order, both from the code, both verified here

**1 · Fan-out comes off `total` BEFORE attribution, not after.** Attribution doubles deposits per
witnessed speech, and the risk is ledger inflation at the 200 cap. **But at `total` the cap is already
saturated** — `test_tracer_is_honest.py:3089` asserts the control arm's fullest ledger sits at
**exactly** the cap, with a comment recording that `>=` was a missing falsifier and `==` is deliberate.
**So measuring attribution's inflation at `total` measures the flood, not the attribution.** Narrow
first, then attribute, then measure.

**2 · The ledger-cap question is not a proceeding question.** The concession is the fiction; the
mechanism is the eviction key, and that key is measurable on any planted claim in an existing test
world. **So the debt is paid in Phase 1, before a single proceeding exists** — and the prediction is
sharp enough to falsify: the key is **recency-dominated**, so a season-1 claim at full confidence ranks
below a season-10 claim at the same confidence. **The cap forgets the oldest thing first regardless of
what it is about** — which is exactly wrong for a recurring cast pricing each other across seasons.

## B.2 · The four phases

| phase | delivers | why the boundary is here | is it the game? |
|---|---|---|---|
| **1 · The ledger holds a reading of a person** (1–7) | fan-out narrowed · attribution · hearsay minted · the cap measured · the want/fear term with habituation · the press traced to its terminus · the speech-kind roster | runs on the existing harness with no seam. **It is where the owner's central ask lives**, and it makes the *world* a story-generator before any proceeding runs | ⭐ **the world becomes a story instead of a log** |
| **2 · The subsystem owns the contest** (8–16) | the manifest row and the prize repoint · the bench Query · the arrangements loader with the multilateral disposal · the composed obstacle and the licence extension · the two verb rows · the provider with its three in-run aggregates · the reach in code | nothing here needs Phase 1 to **run**; all of it needs Phase 1 to be a **game**. Doing 1 first means the first end-to-end proceeding is run against a world whose ledgers already differ — a game-shaped test rather than a flowchart test | the structure exists and resolves |
| **3 · The room reads you** (17–21) | `reception` reads the bench's ledgers · proofs weighed by remove and discounted by the mirror · the investigation product deposit · route erosion · Failure severity by observer set | **the join.** `reception` is the only hidden load-bearing term and cannot exist before both stems | ⭐⭐ **THIS IS THE PHASE THAT MAKES IT A GAME** |
| **4 · Forty seasons stop looking like four** (22–27) | the one new field, with the return day and defiance · pressure crossings · conviction moved by consequence · the forged record examined · cross-season momentum priced · the deletions | polish in the exact sense that it is a game without them — **but without them every loop damps and season 40 resembles season 30** | polish that prevents convergence |

---

# PART C · THE INSTRUCTIONS

**Conventions.** Cost is in the design's own units — fields · verb rows · roster members · obstacle
terms · score terms · magnitudes · Event kinds, plus grammar entries and arrangement keys. **Every
injected magnitude gets a register row with its site and three sweep points, and every declared sweep
must be EXECUTED by a test** — there is already a test whose whole job is to catch declared-and-unrun
sweeps, and that is the laundering it exists to stop.

## PHASE 1 · THE LEDGER HOLDS A READING OF A PERSON

### 1 · Take fan-out off `total`

**Change.** The fixture flips from `total` to the four-channel set. `total` stays in the roster as the
control arm of its existing sweep. **Do not touch the channel list itself** — it is a sweep's arm set.

**Why here.** Every secret, lie and rumour is impossible while everyone holds everything. It is one
fixture, and it is the precondition for measuring anything about deposits.

**Artifact.** The existing channel sweep stays green with the arms re-labelled, **plus one new
assertion: after two seasons there exist two persons whose ledgers differ in at least one
(subject, predicate) pair.** ⭐ *That assertion is the first secret in the world.* The corpus
re-baselines and the deltas are printed rather than hidden.

**Cost.** Zero of everything — a default flip with a sweep already behind it.

**Breaks if wrong.** The propagation loop may starve: telling becomes the only transport, and telling
requires the teller to hold the claim. If the claim→question→act chain drops to zero on the NPC lane,
the narrowing is too tight and two channels are matching nobody.

**Falsifier.** The ledgers-differ assertion passes at `total` (it cannot — `total` fans identically),
or the propagation chain collapses on the narrowed arm.

### 2 · Attribution — a witnessed act that names a subject deposits the actor too

**Change.** A fourth deposit rule under which the actor is **prepended** rather than **replaced**.
Today, when an act names a subject, the actor is dropped from the deposit entirely. Make the new rule
the default; keep the current one as an arm, since the measured reason it replaces is on the record.

**Why here.** ⭐ **Every mechanism in this plan is a reader of the row this writes.** With step 1 done,
its cost is measurable rather than lost in the flood.

**Artifact.** Under the new rule a witness's ledger holds a claim whose subject is **the speaker** for
a witnessed speech that named a record; under the old rule it does not. The sweep gains a fourth arm
and all four run.

**Cost.** One roster member. **Deposits per witnessed speech double** — that is the whole risk.

**Breaks if wrong.** Exactly the defect already measured once: the extra claims evict the decayed ones
first and the decay sweep goes inert. **Step 3 exists to see it, and if it fires the fix is the
eviction key, not reverting the rule.**

**Falsifier.** The decay-inertness test goes red on the narrowed arm under the new rule.

### 3 · Measure the ledger cap, with steps 1–2 on

**Change.** No mechanism. One test: build the seeded world with both changes live, plant a claim
*about a person* in season 1, run twelve seasons, report the first season it is absent, and sweep the
cap × the decay rate as a 3×3. **Print the table.**

**Why here.** The inflation is a measured risk, not a theoretical one — and the prediction is sharp.
**The eviction key multiplies confidence by recency, so a season-1 claim at full confidence ranks below
a season-10 claim at the same confidence.** The cap forgets the oldest first regardless of subject.

**Artifact.** The printed table; the gap register's row moves from *open* to *measured* with numbers.

**Falsifier of the prediction.** The claim survives twelve seasons at the current cap — then the cap is
not the problem and no change is warranted.

**3b, conditional — only if it evicts before season 4.** Weight the eviction key by subject kind, so a
claim about a **person** outlives a claim about an **event**. One magnitude, swept. ⭐ **This is the
precedent's identity-embedded-memory mechanism applied to eviction rather than to a field**, and it is
explicitly *not* a cap raise — raising the cap does not couple the read to a decision.

### 4 · Hearsay — mint `told_by` from the channel, at the teller's own confidence

**Change.** Three lines in the deposit. **(a)** The observer walk returns *(person, channel)* pairs
rather than bare persons, with a declared precedence so that someone admitted by two channels is
credited to the stronger. **(b)** The claim's source is set from a channel→source map: presence gives
firsthand, a knot gives knot-sourced, and a document or a remit gives **told_by**. And for a *telling*
event specifically, even co-located hearers get **told_by** — they heard it told, they did not see the
thing. **(c)** For a telling, the deposited confidence is **the teller's own held confidence on that
subject**, not the default. That is what the design already claims happens.

**Why here.** Hearsay does not exist today; the standing Query reads for hearsay and never sees one;
the source ordinal that two later steps weight by is never minted.

**Artifact.** A tells B about a record: B holds it as **told_by at A's confidence**, while a witness
who saw the speech directly holds it **firsthand**. And the standing Query returns something other than
its maximum for the first time.

**Cost.** Zero fields · two roster members · one map · one signature change.

**Breaks if wrong.** If a remit maps to hearsay, an office-holder who *was in the room* is downgraded —
which is what the precedence is for. Test both channels admitting one person.

**Falsifier.** Every deposit in a three-season run is still firsthand; or a told claim carries full
confidence for a teller who held it at less.

### 5 · The want/fear term, with the habituation clause inside it

**Change.** One person-side term in the candidate scorer. For each live commitment to an OUGHT, evaluate
its **(subject, predicate, value)** as a typed cell against the holder's own ledger — the same call the
contradiction filter already makes — and boost candidates about that subject when the want is unmet.

- **Polarity.** A fear is the same object with the value negated: satisfied by default, boosting only
  when a claim lands that makes it false. ⭐ **So a fear names the PRECURSOR — fear the case, not the
  sentence.** A fear of the outcome is inert until the outcome, which is a fear that never protects.
- **Habituation.** The boost is divided by a count of prior identical claims in **the holder's own
  ledger**, discounted by their decayed confidence. **A count over live rows, person-side, nothing
  stored.** This is what the audit's second pass found missing: without it, press 2 is identical to
  press 1.

**Why here.** ⭐ **Initiation — the one thing no character does today.** It reads only person-side state,
so the no-world-in-a-decision rule holds.

**Artifact.** Two characters at one seed, one committed *for* a thing and one *against* it, both
witnessing the same event: **their ranked candidate lists differ in first position.** A second test
presses one fear twice and prints both boosts, the second strictly smaller. ⭐ **The sweep must run
against the all-questions aggregation, not the first-only fixture, or it measures the fixture.**

**Cost.** One score term · one magnitude · zero fields · zero verbs.

**Breaks if wrong.** Large enough to beat a docketed date and characters are monomaniacal; small enough
not to, and it is another term that never moves a ranking. **Both ends of the sweep must flip at least
one verdict** or the magnitude is inert.

**Falsifier.** Identical rankings at every sweep point; or press 2's boost equal to press 1's.

### 6 · Run the fear press to its terminus — no new mechanism

**Change.** None. One seeded eight-season test. A holds a claim on B's committed fear and names it each
season. Observe: **press 1** — B's question fires, B's promoted candidates are about the feared thing;
**press 2** — the boost falls; **press N** — the habituated boost drops below B's own conviction
baseline and the verbs his weights favour take over. ⭐ **B repudiates his own commitment — "let them
excommunicate me" — the fear leaves the set his questions read, and press N+1 lands a claim and raises
nothing.** Print the season of repudiation. Then the symmetric test: name the **wrong** fear, get no
question at all, and be on record as having threatened with nothing.

**Why here.** It executes the owner's correction rather than describing it, and it proves **the
terminus needs nothing new**: the lever is spent by *him*, at a moment his convictions chose and the
presser could not see coming.

**Artifact.** The printed press table — season · B's top candidate · boost · did the question fire —
and the repudiation season, at three sweep points.

**Breaks if wrong.** If B never repudiates at any sweep point, the lever is infinite — which is
precisely the *escalation with no terminus* the precedent survey names as the failure mode. Then the
habituation denominator is too weak.

**Falsifier.** A question fires after repudiation; or the wrong-fear press fires one.

### 7 · Author the speech-kind roster, with reachable bands

**Change.** The roster the design promised and never wrote. Columns: the kind · which genres it is apt
in · which rungs it is apt at · ⭐ **and which bands it can reach at all.** That last column is the
figure adjudication's finding: **impugning a motive is Partial by construction** (it does not answer
the charge), and **a procedural objection has no Success** — it is granted, referred, or reads as
evasion. Ten members; the two starred kinds are not rostered.

**Why here.** Needed regardless of everything else, it is data, and three later steps read it.

**Artifact.** The loader refuses a kind whose reachable bands name a band outside the ladder. The one
kind with no figure behind it carries a *thin warrant* note rather than a fabricated one.

**Cost.** One roster with three typed columns — a schema addition, counted.

**Breaks if wrong.** ⚠ **Reachable bands are a per-kind CAP applied as a demotion by the seam's one
band extension — never a lookup that RETURNS a band.** The second is a second ladder.

**Falsifier.** Impugning ever resolves above Partial in any run.

## PHASE 2 · THE SUBSYSTEM OWNS THE CONTEST

### 8 · The manifest row lands, and the seam dispatches by row rather than by `if`

**Change.** The hardcoded `if module == "personal_combat"` in the contest call is replaced by a lookup
on the manifest, resolved at boot. Combat keeps working through the same lookup. The refusal for any
prize no row routes survives untouched.

**Why here.** The ruling — and the seam document already argues why a *second* `if` would break
resolution-by-declaration in three places at once.

**Artifact.** Booting a world whose manifest lacks the row fails **naming the row**; with the row, the
contest reaches this provider and does not raise. ⭐ **Combat's byte-exact goldens are the control and
must not move.**

**Cost.** Zero verbs · one manifest row · one provider module.

**Falsifier.** A grep for a module-equality comparison inside the contest call returns any line.

### 9 · The two prize rows repoint here

**Change.** The two prizes currently routed to the old module route to this provider, and the prize
this subsystem's speech verb contests is added. The other two remain claimed by no verb — leave them
routed; collapsing three prizes into one is an engineering call for after the bar runs, not before.

**Why here.** The ruling, and it is one line each. The objection recorded in the README — that
repointing supersedes other work quietly — is answered by the ruling being loud.

**Artifact.** A seeded contest on a repointed prize resolves through the seam without raising.

**Cost.** Two roster edits · one roster member.

**Breaks if wrong.** ⚠ **Whatever those rows previously reached is orphaned.** That disposition is the
owner's (PART H, D-1) and **the orphaned tree is not to be opened** — the scope ban stands.

**Falsifier.** The routing lookup still returns the old module; or the contest still raises.

### 10 · The bench Query — three parameters

**Change.** The function that currently raises unconditionally becomes the walk the design already
specifies: seats whose remit acts contain the arrangement's basis, whose scope contains the venue by the
containment walk, holding a live seat. The third parameter extends the live two-parameter signature.

**Why here.** Buildable today; the gap register already carries its default and its three-arm sweep.

**Artifact.** A bench resolves over a planted seat roster; removing the remit empties it; a purview walk
one rung up still finds it; **the three-arm sweep runs.**

**Breaks if wrong.** A venue-only bench makes two different matters before one bench return one answer.

**Falsifier.** Two docketed matters with disjoint remit coverage return the same seats.

### 11 · The arrangements loader — with the multilateral disposal, and three keys fewer

**Change.** The row as specified, edited:

- ⛔ **Delete `stakes_grade`** — already the most likely deletion, and step 21 replaces it with the
  study's own rule.
- ⛔ **Delete `verdict_reasons`** — its only lawful mechanism is identical to the dissent key's (which
  of the bench's emissions reach the ruling's audience), so one key carries both.
- ⛔ **Delete `registers[]`** — the roster never existed, the 7→7 map is a forbidden lookup, and the
  idea folds into aptness.
- ✅ **Add a `declared` disposal value and a quorum key** (an integer or a fraction; data).
- ⭐ **Keep the dissent key — withdrawn from the cuts.** Under a declared disposal **it is the tally
  made visible**: it decides whether the members' individual commitments leave the room with the
  ruling, or only the declaration does.

Net: **fifteen keys minus three plus one = thirteen.**

**Artifact.** Twelve rows load; a fourteenth key fails **naming the row**; the thirteenth game loads
with no code change; **a declared-disposal row with no quorum fails the load.**

**Falsifier.** The closure scan finds any comparison against an arrangement's name in the provider.

### 12 · The composed obstacle, the injected magnitudes, and the licence as one band extension

**Change.**

**(a)** Rule the latitude question as **pool-only** — this file's own recommendation, and the term count
is wrong until it is ruled. It needs the owner's confirmation (PART H, D-2); the build proceeds on it
with the alternative as a swept arm. The obstacle is then **four room terms plus aptness**, floored at 1.

**(b)** The pool is *brought + conduct × latitude*, fractional, floored at one die, drawn **once per
interaction** through the continuous path — **never the discrete one.**

**(c)** Aptness reads step 7's roster: a genre mismatch and a rung mismatch each add a step. ⭐ **The
manner-misreading idea from the deleted register key folds in here as the same term**, rather than
becoming a second one.

**(d)** ⭐ **The licence conditions are ONE band extension, not four obstacle terms.** It demotes when
any conjunct fails **or** when the speech kind's reachable bands exclude the top band. Demote-only by
construction.

**(e)** The display-only effective obstacle is never resolved on.

**Why here.** It is step 0 of the build order, and the band edges are already ruled and pinned.
⭐ **With ownership settled the obstacle has exactly one home**, and the de-saturation extension that
lives elsewhere is not this provider's.

**Artifact.** A seeded margin produces the same band twice; planted margins either side of each edge
band differently; a composed obstacle never falls below 1; a licence failure on a margin at the top
threshold returns the band below; the extension's context validator refuses an undeclared key. **A
register row for every magnitude, each with three swept points, each executed.**

**Cost.** Four room terms + aptness · about six magnitudes · one extension subclass · zero fields.

**Breaks if wrong.** ⚠ **Every flat obstacle term swings a weak speaker far more than a strong one.**
The pool sweep is measurement M-3, and it decides whether reception alone moves to the other channel.

**Falsifier.** Any path in the provider that returns a band; any obstacle below 1; an extension that
ever promotes.

### 13 · The two verb rows land

**Change.** The speech row as specified, with one addition: **the Partial's docket write takes the
speech's own operand**, so the speaker names the subsidiary question and a Partial is a docketing the
bench did not choose. The determination row as specified **plus a contest declaration** — without one it
writes a degree it cannot compute, which is the hole the adversarial pass found. The suspended question
of *whose score the obstacle is half of* gets its declared default, swept, and is not re-escalated.

**Artifact.** A speech with no live occasion forms no candidate; the four write and emit key sets are
equal; a Partial emits a docket formation carrying **the speaker's operand**; an unseated actor's
determination emits its refusal.

**Breaks if wrong.** ⚠ **The corpus says that before a superior the credit for a carried matter belongs
to the SOVEREIGN, not the speaker** — and writing another person's stance is forbidden. **So the
sovereign's adoption is expressed by the sovereign's own later commitment to the counsel's proposition,
not by a write.** State that in the row's note and build no workaround.

**Falsifier.** The Partial's docket item carries an empty matter instead of the speaker's operand.

### 14 · The provider — the nested run, with three in-run aggregates, all free

**Change.** Order the attendees from the arrangement row; each forms candidates from what they hold with
no view of the world; each act is folded with a degree the provider computed from **one draw** against
the composed obstacle. Events go to the same log. **The run ends when nobody acts, the term matures, the
ladder bottoms out, or the depth cap returns a typed refusal. There is no turn limit and there must not
be one** — a round cap is a clock nobody wound. **The provider never writes.**

⭐ **Three aggregates, each a fold over this run's own emissions, owned by nobody, dying with the run —
licensed outright by the owner's aggregates question and by the theorem's own correction:**

- **14a · The two-fold rung.** Your **own** rung is the lowest any of your emissions named at any band;
  the **forced** rung is the lowest an opponent's top-band emission named. The obstacle reads the lower.
  ⭐ **This replaces the band-blind shared fold and answers the worry that it was a cross-holder tally —
  the comparison is intra-run.**
- **14b · Proofs told so far.** Unchanged.
- **14c · Momentum — the accepted debate score.** Carried +2, advanced +1, held 0, turned −1, summed over
  your own emissions this run, entering the obstacle as one term. ⭐ **The player in the room can count
  the emissions — they witnessed them. The coefficient is hidden.**
- **14d · Silence priced.** A step added to an attendee's next obstacle **only where the provider formed
  a non-empty lawful candidate set and they took none.** ⭐ That converts it from *punishing having no
  options* into *pricing a choice*. The carve-out comes from the arrangement row as data, never a
  membership test in the provider, and it is falsified on the buildable speaking order.

**Artifact — THE BAR.** One seeded proceeding runs end to end **with zero authored acts, twice,
byte-identical including the world hash**, and the causal chain walks from the determination back to the
date that raised it. Plus: **permute the speaking order and the outcome moves; permute anything else
about the sub-steps and it does not.** Plus: at the depth cap the refusal is reachable without a crash.

**Cost.** One provider module · two obstacle terms · two magnitudes — **and the silence step must be
swept jointly with the held step** (M-4).

**Breaks if wrong.** If the provider evaluates any precondition outside the fold it is a second
resolver. **A scan of the provider for writes and for precondition evaluation is the guard.** If
momentum and the rung fold read the same emissions with the same sign, they double-count.

**Falsifier.** The hash differs between two runs at one seed; or the provider writes; or a proceeding
advances with no act taken.

### 15 · The multilateral disposal — a Query read by a declaring act

**Change.** The construction the design already wrote. **Each bench member's finding is their own
commitment** to a disposition — their edge, nobody else's. **The declaring act is the determination**,
whose precondition gains a third conjunct: *a cardinality of live commitments to this subject, held by
members of the bench, of at least the quorum.* ⭐ **This widens the precondition grammar by two entries
— counted as a design change and taken because it is what works best** (the governing ruling). The
declaration writes the disposal; the dissent key scopes whether the members' commitments travel with it.
**No count is stored anywhere.** The gap closes.

**Why here.** It is the ruling — and it gives **two fields their first readers in one step**: the
finding's degree (a writer and no reader until now) and the dissent key.

**Artifact.** Five seats; three commit; the presiding seat's determination succeeds. With two it emits a
no-quorum refusal. Dissent recorded fans three commitments to the ruling's audience; not recorded fans
only the determination. ⭐ **A grep for any field named count, tally, votes or quorum-reached returns
nothing.**

**Cost.** Two grammar entries · one refusal kind · zero fields · zero verbs.

**Breaks if wrong.** ⚠ **A member's dissenting commitment is witnessed by everyone co-located regardless
of the key** — the commitments happen *in the room*, and the player is in the room. **The key governs
what LEAVES.** State it so nobody tries to hide a commitment from someone standing there.

**Falsifier.** The declaration succeeds below quorum; or a stored count appears; or one member's
commitment changes another's.

### 16 · The disposal's reach, in code

**Change.** Landed in design this morning, not yet in the tracer. The disposal's existing emissions
compute their witness set from the reach key rather than from presence — the room, the body's remit
holders, or the containment walk to a named tier. One more channel keyed on event kind. ⭐ **And with it,
delete the dead public channel** — it matches nobody, and the reach does its job.

**Artifact.** The same excommunication at *room* versus *realm* deposits into a handful of ledgers versus
dozens — **while the argument's emissions deposit identically in both, because they scope by the floor.**

**Falsifier.** Any argument emission's deposit count changes with the reach.

## PHASE 3 · THE ROOM READS YOU — ⭐ the phase that makes it a game

### 17 · `reception` is composed from the bench's ledgers and convictions, resolver-side

**Change.** A Query taking the world first, living beside the other resolver-side Queries and **never
importable from decision code.** For each seat-holder: claims whose subject is the speaker, each
weighted by **an ordinal of remove** (firsthand > knot-sourced > told > inferred) times its decayed
confidence, with valence from the holder's own convictions against the axes the recorded act aligns
with. Summed over the bench and scaled into the obstacle.

⚠ **The valence source is itself the swept choice, and the conflation is recorded rather than glossed.**
Arm 1 reuses the existing alignment table, which conflates *what this hearer prefers to do* with *how
this hearer regards someone who did it.* Arm 2 is a dedicated regard table keyed on event kind. **The
sweep decides.**

**Why here.** The join. It is the only hidden load-bearing term, and with steps 1–4 there is finally
something for it to read.

**Artifact.** Two benches of identical seats and identical convictions, differing **only** in one
member's ledger, produce different bands for the same seeded draw. A told claim moves the obstacle
strictly less than the same claim firsthand. **An AST test that the Query takes the world first and that
no decision-side module imports it.**

**Breaks if wrong.** The weak speaker's room becomes a lottery — M-3 is the check, and its remedy is
moving **reception alone**, not the other four terms, to the other channel.

**Falsifier.** A bench's obstacle is invariant under any change to its members' ledgers; or the Query is
reachable from a decision.

### 18 · A proof is weighed by its remove and discounted by the mirror

**Change.** The proofs term weights each told claim by the source ordinal and **discounts to zero any
claim the opposing party can mirror** — a Query over two ledgers, resolver-side. ⭐ **The player cannot
run the mirror, because they cannot read the other ledger. They guess it — and that guess IS the
hoard-or-spend decision.**

**Artifact.** A telling of a claim the opponent also holds moves the obstacle by exactly zero; one they
do not moves it by the step times its remove.

**Falsifier.** The mirrored proof moves the obstacle.

### 19 · The investigation acts deposit their PRODUCT, at a confidence keyed on the degree

**Change.** The five rows land. Today the actor's deposit carries what the **precondition** read — for
an interview, co-location, not the disposition. So each row gains a **product** column naming the
predicate its finding deposits: an interview deposits a stance, an examination a retention, research a
record, a reconstruction an inference, surveillance a presence. At witness, the actor's deposit carries
that product at a confidence keyed on the degree — ⭐ **and a misread deposits at the SAME confidence
with the WRONG value.** Never silence: absence must not be legible.

**Why here.** Without it nobody has a reason to ask anybody anything, and the obstacle they would be
estimating now exists.

**Artifact.** An interview about a record deposits a stance into the asker's ledger; on a misread the
sign is wrong and the confidence identical; **and the subject's ledger records that they were asked.**

**Falsifier.** A read and a misread are distinguishable by anything except the value.

### 20 · Route erosion, derived from the hearers' claims

**Change.** Inside reception, partition each hearer's claims about the speaker by the **kind of act they
record** — coercive acts versus conferred ones — as a data mapping. ⭐ **A failure against a
dominance-standing speaker zeroes that hearer's dominance-sourced weight: the single called bluff.**

**Artifact.** The lord who governs by fear is challenged by a nobody. The nobody's failure leaves him
intact; the nobody's **one** success collapses him in every witness's ledger.

**Falsifier.** A called bluff leaves the weight unchanged.

### 21 · Failure's severity is the observer set — and an inert field is deleted

⛔ **CORRECTION TO `18_FINDINGS.md`, VERIFIED HERE.** That document proposed `Claim.visibility` as the
carrier for the corpus's *terminal = being seen at it* rule. **The field is inert.** `grep -n
"visibility" shape.py` returns **exactly one line — the declaration.** No writer by name, no reader. The
findings document is wrong and is corrected.

**Change.** The honest carrier is **the size of the observer set for the failing event at witness, minus
the actor** — a barrier-scoped aggregate, licensed. A failure witnessed by nobody writes the actor's own
stance and stops there; one witnessed by enough others additionally fires the row's terminal write. One
floor, no other coefficients. ⛔ **And delete the inert field**, or give it a roster and a reader.

**Why here.** It replaces the deleted grade key with the study's own rule at the cost of a single floor.

**Artifact.** The same failure in a two-attendee closed room and a twelve-attendee open one writes the
costly consequence in both and the terminal one only in the second.

**Falsifier.** A discovered lie in an empty room fires the terminal write.

## PHASE 4 · FORTY SEASONS STOP LOOKING LIKE FOUR

### 22 · `Tenure.term` — the one new field in the whole plan

**Change.** A tenure gains an optional term carrying *when it matures*, *the act that declared it*, and
*who may close it*. **The unread payload field is deleted in the same change** — its replacement is
already scheduled. Maturation happens at the matter barrier and **cites the declaring act as its cause**,
so it is one causation-bound seam rather than a fourth clock.

**Then, all at once:** a summons declares a return day · **defying it is contumacy, and in canon and
common law contumacy IS the finding** · surveillance gets its interval · an overdue obligation becomes a
pressure source · and the inquisition row's indefiniteness becomes something **the subject can feel**.
⭐ **The three kinds of absence become derivable with no ruling** — declined (there is an event), could
not (no event, not present), not admitted (the floor refused).

**Why here.** It is the best-value field in the register and it touches the substrate, so it comes after
the game exists.

**Artifact.** A summons matures with no act and closes **citing the act that wound it**; defiance emits
and the contumacy finding is formable next season.

**Cost.** One field · minus one field.

**Falsifier.** A term matures citing the root rather than its declaring act.

### 23 · Pressure surfaces as a standing band crossing — about someone

**Change.** The crossing question reads only site crossings today. Add person-keyed ones: recompute the
standing gap over past claims versus all claims; if the band differs, record a crossing whose causes are
**the deposits that composed the gap.** ⭐ **The question's referents are the people whose claims made it
— so pressure surfaces as a question ABOUT SOMEONE.** That is the difference between *his stress is 7*
and *he has decided it was the archdeacon.* Two further sources: contradictory commitments (computable
today, no reader) and overdue obligations (needs step 22).

**A crossing changes what can be chosen and never what happens.**

**Artifact.** The bailiff is told three things about himself; his standing crosses; his first question
next season names the tellers; **he opens a case against one of them — who may have said nothing.**

**Breaks if wrong.** The standing measure is a **gap**, so a hated man who knows he is hated feels
nothing. Whether that polarity is right is PART H, D-4; the mechanism is identical either way.

**Falsifier.** A crossing produces a write rather than a question.

### 24 · Conviction moves by consequence

**Change.** The determination gains a degree-keyed write to **the determiner's own** convictions — a live
row with no producer until now, and owner-clean because the writer is the actor. The axis moved is the
one the determination aligns with: the top band hardens, success moves a little, a held matter moves
nothing, **and a failure moves the determiner AGAINST their own axis** — the judge who ruled and
regretted it.

**Artifact.** Three lenient findings move one judge's weight by a printed amount, and the same
arrangement on the same seats then produces a different obstacle for the same speaker. ⭐ **And the test
that witnessing never touches a conviction stays green** — the write is at resolution, by the actor's own
act, never at witness.

**Breaks if wrong.** A positive loop hardens a judge into a caricature; a negative one converges every
bench. **The forty-season run is the only way to know** (M-5).

**Falsifier.** A conviction moves at witness; or the emission cites a deposit rather than an act.

### 25 · The forged record is a proof until it is examined

**Change.** Examination contests the record's forgery quality — **written by forging, read by nothing**
— as well as its retention. Finding it deposits the forgery as a claim; finding nothing leaves it
standing **and the examiner was witnessed examining.** Until examined, a telling from a forged record
enters the proofs term at a record's weight.

**Artifact.** A grant forged at high quality carries a written-only appeal; an examination that finds it
makes the forger's exposure terminal by step 21's rule.

**Falsifier.** The forgery quality still has zero readers after this lands.

### 26 · Cross-season momentum — what the accepted debate score costs if it must survive

**Change.** **None by default.** In-run momentum dies with the run, and an adjourned hearing resumes at
the top of the ladder — a cost the design already names. ⭐ **If the owner wants a debate's state to
carry, the lawful carrier is a `Record` the presiding clerk wrote** — a document, carried, forgeable,
burnable, and **claimable**, so what it says about last season's debate is something a witness holds
rather than a truth. **Cost if wanted:** one clerk's scene per adjournment · one write on an existing
field · the resumed opener reads it **as a proof, not as state.**

**Why here.** So the accepted shape has its cross-barrier form stated once, and **so nobody builds a
momentum field** — which is the forbidden shape sneaking in through the accepted one.

**Artifact.** If built — a resumed hearing whose clerk's record was burned starts at the top; one whose
record was forged starts where the forger says.

**Falsifier.** Any momentum value surviving a barrier outside a record.

### 27 · Delete the dead carriers

**Change.** Four fields and one channel. **Beliefs** (zero readers; already scheduled — a belief is a
commitment to an OUGHT). **Marks** (zero readers; a second home for self-claims the standing Query
already reads from the ledger, and step 19 writes the vocabulary properly). **The tenure payload**
(step 22). **The claim visibility** (step 21). **The dead public channel** (step 16). ⭐ **The inert
urgency term stays** — it is inert by construction and the code says the null result *is* the
measurement.

**Artifact.** The dead-carrier tests pass with four fewer fields; **the corpus hash moves, and the move
is recorded rather than hidden.**

**Falsifier.** A reader appears for any of them in the same diff that deletes it.

## C.1 · The twelve variants, mapped to the step that gives each its distinct play

**Three had no distinct play as the code stood. Each now has one step, and none needed a new mechanism.**

| variant | the play | lands at |
|---|---|---|
| negotiation | the offer ladder; mutual generalised to all parties | live · 11 |
| by envoys | the rope | live |
| arbitration | the game before the game | 10 |
| legal trial | descend and be seen | 2 · 14a · 22 |
| tribunal | ⚠ **a bench that drifts** | **24** |
| interrogation | ⚠ **what not to say** | **14d** |
| inquisition | ⚠ **indefiniteness the subject can feel** | **22** |
| excommunication | deciding about someone absent, on claims you cannot check | 4 · 16 · 17 · 22 |
| parliamentary debate | which of many to address; the vote; the losers on record | 5 · 11 · 15 |
| council of state | **the hidden profile** | **1** |
| audience / embassy | say nothing here, tell it elsewhere | 4 |
| appeal | the cap is a term somebody set | 22 |

---

# PART D · THE CHARACTER MODEL, IN FULL

> **The owner's list:** *goals and ambitions, allegiances, memories, beliefs, convictions, ethical
> stances, pressures, stresses, relationships … fears.*

> ### ⭐ **THE GOVERNING FINDING: every one of these already has a carrier except pressure's third
> source. What was missing was not carriers but READERS — which is the precedent survey's exact named
> failure mode, *memory that never surfaces*.**

| the thing | what it is, mechanically | where it lives | what reads it, after this plan | cost · step |
|---|---|---|---|---|
| **memories** | claims — *who holds it · about whom · what · when · from what source · at what confidence* | the holder's own ledger, and nobody else's | the question producer · the contradiction filter · standing · the want term · reception · the mirror | today every memory is *(what was named, event kind, true, firsthand, full)* and **forgets who acted.** Steps 1–4 · step 3 decides whether it forgets the right things |
| **goals and ambitions** | ⭐ **a live commitment to an OUGHT** — and the loop already turns it into a standing question every season | the tenure edges, not a field | the question fires today and reads **only the subject**; **step 5 supplies the direction** | 1 score term · 1 magnitude · **0 fields** |
| **fears** | the same carrier with the value negated; satisfied by default; boosting when the **precursor** lands; **pressable indefinitely because nothing is spent**; ⭐ **the terminus is his own repudiation** | the tenure edges | step 5's term with habituation · step 6 traces it to the end · the licence conjunct prices the presser · reception prices him in every later room | 0 beyond steps 2 and 5. ⭐ **What a fear makes available is a SUBJECT, not a verb** |
| **secrets** | ⭐ **a distribution fact** — a claim few ledgers hold. Threatening is the same lever as pressing a fear; **revealing spends it**; a closed floor contains it while the reach proclaims the ruling | nowhere new — **the ABSENCE of a claim from most ledgers** | everything that reads ledgers — **and it is impossible until step 1** | 0. Step 1 is the whole precondition |
| **allegiances** | a live commitment to a faction's proposition — a faction *is* a proposition plus its edges | the tenure edges | the question producer's own-set · the quorum counts them · a speech on a subject the faction opposes fires the member's own question | 0. **A claim about a dead edge is a stale belief nothing marks — that is the epistemics working** |
| **relationships** | typed edges — owes · bound (a knot is a witness channel **both ways**) · holds · succeeds. ⭐ **The typed record the precedent ranks #1, and it already exists** | the tenure edges | eligibility · the channels · release | 0 new kinds. **What stays refused: acting on another's edge** (PART H, D-5) |
| **convictions** | weights over the closed moral axes — what a person holds **right** | a field | ⭐ **the candidate scorer — the one live reader.** Reception reads the *hearer's*. **Step 24 gives it a producer** | 1 write · 1 magnitude. **Never moved by evidence; moved by the person's own determinations** |
| **ethical stances** | posture toward a subject | a field | the scorer; written by the speech bands — **the actor's own, only** | 0. ⭐ **Failure writes it adversely — the study's whole fault catalogue in one column** |
| **beliefs** | ⛔ **not a field.** A belief is a commitment to an OUGHT | deleted, step 27 | — | −1 field |
| **pressures** | ⭐ **a Query, never a number** — the gap between what you are told about yourself and what you hold; contradictory commitments; overdue obligations | **nowhere.** Computed at sensing, stored nowhere | **step 23** adds crossings, with **the people who told as the referents** | 0 fields for two sources · **the one field for the third** |
| **stresses** | ⭐ **the crossing, not a meter.** A band change admits repudiation, defiance, flight, a case — through their own weights — **and never produces an outcome** | nowhere | step 23 | 0. **The forbidden shape is refused because nothing is spent** — and it is the precedent's named failure mode |
| **ethos — what others take you to be** | ⛔ **not a field.** Claims in *other people's* ledgers whose subject is you, **each of which may be wrong** | their ledgers | reception; standing from your side | 0. **Step 2 is what lets a ledger hold one** |
| **bias** | ⛔ **not a field, and must never become one.** The divergence between a ledger and the world, plus the weights convictions put on the axes | nowhere | it changes the finding **and nobody can read it** | 0 |
| **identity-embedded memory** | the precedent's #4 — a scar, a byname. Here: a person's own firsthand self-claims, which standing already pairs | the marks field is **deleted**; the vocabulary stays in its roster; step 19 writes it; **step 3b makes person-claims outlive event-claims in eviction** | — | −1 field |
| **attributes / efficacy** | capability — **supplies dice and gates nothing.** Two keys, content | a field | the pool | 0 |

**What the model refuses, so it stays a model of people rather than of stats:** nine capacities as
stats · a per-proceeding skill · an office bonus · a bias field · a stress scalar · a reputation number ·
a want the grammar cannot ask. **Every one is refused on the same ground — a value with two readers, or a
threshold that acts — and every one has a lawful cousin above.**

⚠ **The one honest bound, named rather than contorted:** a want must be expressible in the seven
precondition forms to be *evaluable*. *"Hold Vellenmark"* is. **"Be loved" is not**, and is not faked
through stance. An eighth form is a design change — **named and declined.**

---

# PART E · MEASUREMENT DEBTS

**Each must run before the thing after it is built. A number without a control is not a measurement in
either direction — every row names its control.**

| # | debt | before building | the experiment | the number that decides |
|---|---|---|---|---|
| **M-1** | **the ledger cap** | anything reading a person-claim across seasons (17 · 20 · 23) | step 3: both changes live, plant a person-claim in season 1, twelve seasons, cap × decay as a 3×3 | **evicts before season 4** → the key is recency-dominated → do 3b. **Survives twelve** → the cap is not the problem |
| **M-2** | **the want magnitude** | step 6, and everything depending on initiation | step 5's sweep **at the all-questions aggregation**, three points, two characters; count verdict flips per arm | **zero flips** → inert. **Flips at every arm** → monomania. The usable window is what the sweep prints |
| **M-3** | ⭐ **the weak-speaker swing** | step 20, and any further obstacle term | the five terms at four pool sizes, **one term at a time**, seeded; record band by pool | a rank advantage swings a small pool more than a large one **and it reads wrong in play** → move **reception alone** to the other channel. Not the other four — they are properties of the room |
| **M-4** | **silence versus the held step** | shipping 14d | a joint 3×3 on the buildable order; count runs where silence is chosen | **silence step ≥ held step** → silence is strictly dominated and the decision does not exist. **Too small** → a shrug. ⭐ **The ratio, not either constant** |
| **M-5** | **standing concentration over forty seasons, and the conviction loop's sign** | step 24's magnitude; any claim the loops are bounded | forty seasons, twelve persons, three seeds; the inequality of reception per season; each judge's weight per season | **rising monotonically** → the standing loop is unbounded, and three of its four bounds are corpus properties with no column to turn. **Judges converging** → the conviction loop is negative; diverging → positive |
| **M-6** | **starvation on the narrowed fan-out** | making step 1 the shipped default rather than an arm | the corpus at both arms: the claim→question→act chain on the NPC lane | **the chain falls** → two channels are matching nobody and the narrowing is too tight |

---

# PART F · WHAT NOT TO DO

**A plan that only adds is how a tree gets the way this one got.**

| the attractive thing | why not |
|---|---|
| **a stress meter · a capital pool · a reputation number** | a per-person scalar with two readers that gates or is spent — **and it is the precedent's named failure: memory into a number that gates nothing.** The crossing is the lawful cousin |
| **a bias field · showing "the room is hostile"** | it makes prejudice legible in a game whose epistemic layer exists to make it illegible |
| **capacity stats · a per-proceeding skill · an office bonus** | models the half of the variance the study says is not there |
| **a proceeding object · a verdict type · a role enum** | derivations, not omissions |
| **a hook-call verb · a creditor closing a debtor's obligation** | a non-owner write. **It is the second-person lever, and it is PART H D-5, not a step** |
| **widening the question set so the cornered man retaliates at the presser** | not an axiom breach — but a design change to candidate formation, and **the audit says the feared thing is the better story.** PART H, D-3 |
| **an eighth precondition form for "be loved"** | a new thing a precondition can ask. Wants the grammar cannot ask are authored as stances or not at all |
| **raising the ledger cap as the memory remedy** | ⭐ **the fix is coupling the read to a decision point** — and, if the measurement says so, weighting eviction. **Not more slots** |
| **a per-pair table — kind × game, register × register** | the rule count grows with the pair count. **144 numbers nobody measured** |
| **a second `if` in the seam · a local degree function · a fifth band · renamed bands** | a draft renamed the bands once and **it could not have loaded** |
| **a turn limit · a round cap · "the hearing concludes after N"** | a clock nobody wound |
| **reception computed person-side, or shown as a number** | **legible hand, illegible room** |
| **a cast list · an absence flag** | presence is whoever travelled |
| **a public channel that matches everyone** | it collapses the narrowed arm back into total and the sweep measures nothing |
| **restoring the three cut keys** | each is a summary, a duplicate, or a lookup of a roster that never existed |
| ⛔ **opening the orphaned social-contest tree** | the standing scope ban — **and its disposition is the owner's** |

**The cuts that pay:** the grade key (severity is whether it was *seen*) · the reasons key (its mechanism
is the dissent key's) · the register key and its term (the roster never existed) · the dead channel (the
reach does its job) · four dead fields · the deposit rule that **replaces** the actor where it should
**join** him · the band-blind shared fold.

---

# PART G · THE REFUSALS, RE-SORTED UNDER THE SECOND RULING

## G.1 · Genuinely forced — these hold

A readable disposition meter · a GM or a fourth clock · a view of the room inside a decision · an
obstacle below 1 or advantage as an obstacle reduction · a flat un-scaled bonus · **a second ladder or a
promoted band** · eligibility by stat · ⭐ **a non-owner edge write** · an arrangement that declares a
cast · a disposal that writes only a Query · an event carrying an actor or a target · a mutated
proposition · evidence moving a conviction directly · **making someone a party** · the creditor's verb ·
a disposal with no author · ⭐ **a shared transcript** — the largest refusal, and the one that buys every
mechanism this game has for politics · a proceeding that advances because time passed (recovered by
step 22) · a magnitude sourced to the study rather than injected and swept.

## G.2 · Provisional — and now accepted

| refusal | what changed | lands at |
|---|---|---|
| ⭐ **a shared visible track · debate score · momentum · vote count** | the owner's aggregates question, and the theorem's own correction. **In-run: accepted, free.** A **field** is still forbidden; a cross-barrier version costs a record | 14a–c · 26 |
| ⭐ **the multilateral disposal** | the construction was already written; the ruling accepts it | 15 |
| a counted vote | the same construction — **one declarer reads the Query.** The earlier pass called it "a different game"; it is the accepted one | 15 |
| a multilateral binding settlement | a treaty is a proposition plus N commitments — **a faction everyone joined.** No breach | 11 |
| **zero new primitives** | ⭐ **downgraded from constraint to tiebreak by the governing ruling** | 7 · 15 · 19 · 22 each add a counted thing **because it works best** |
| finality as a wall | not forced — derivable from the finding's degree and the declared cap | 22 |
| indefiniteness as a virtue | **misfiled — a build blocker dressed as a design choice** | 22 |
| order from declared data (the record tension) | narrowed: **a record the opener wrote IS declared data.** What stays refused is order from a capability or a body default | noted, not built |
| the two-party bound on mutual disposal | the ruling | 11 |
| the dissent key on the cut list | ⭐ **it is the tally made visible.** Withdrawn | 11 |

## G.3 · Cut for being bad design, not for being unlawful

A per-pair rule table · capacity stats and per-proceeding skills · a stress scalar · a proceeding object
· the dead public channel · a twelfth game whose only prize is standing · showing the obstacle.

## G.4 · Does *"all social contests"* widen the twelve?

⭐ **No. Ownership of the CONTEST KIND is not a mandate to host every social interaction.** Telling,
uttering, committing, petitioning, obliging and knotting stay season-loop verbs with no contest
declaration. What routes here is any verb declaring a prize the roster maps here — today the speech verb,
and the two repointed prizes once a verb claims them. **The catalogue stays eleven games and one
degenerate case, plus the examination, plus whatever a data row can express under thirteen keys — now
including conclaves, votes and five-party settlements.**

---

# PART H · WHAT IS GENUINELY JORDAN'S

**Each survived all five tests — superseded · irrelevant · answered by a design document · answered by
precedent · answered by what makes sense for the architecture. ⭐ Ownership is NOT here: it is settled,
and its consequences are steps 8–9.**

**D-1 · What happens to the code the repointed rows previously reached.**
Repointing orphans whatever was reachable through those two rows. **Blocks nothing** — the rows repoint
regardless. **Options:** leave it unreferenced with a note that its rows are gone · retire it under the
culling precedent · migrate anything in it this provider lacks. ⛔ **This plan cannot assess the third
without opening the tree, and will not.**

**D-2 · Where latitude lives.** The resolution file **implements one option, says it implements a
second, and recommends a third.** The term arithmetic in every magnitude row is wrong until it is ruled.
**Options:** *pool only* — an interposed room is one where **who you are matters less**, four room terms,
and it is the study's claim stated exactly (recommended, and the build proceeds on it); *both* — harder
**and** flatter, which double-counts. **Blocks:** the term count everywhere.

**D-3 · Where the cornered man's drastic act lands.** He breaks in the direction of his own convictions —
**toward the feared thing**, never toward the presser, unless a live edge already binds them. Retaliation
at the presser needs the question set widened; that is person-side, so **not an axiom breach**, but it
changes every character's questions. **Blocks nothing** — the default ships without it. **Options:** keep
the audit's picture (the study's picture, zero cost) · widen it (one clause; every grudge becomes a
question about a person, which is the rival flag from the precedent — **and every character gets
noisier**).

**D-4 · The polarity of pressure.** The standing measure is a **gap**, so *everyone reads you as you read
yourself* is **zero pressure** — a hated man who knows he is hated feels nothing. **That may be exactly
right** (the study's inhibition is about knowing and acting anyway) **or backwards.** The mechanism is
identical under either; the arm is one line. **Options:** the gap — *a man is pressed by what he does not
yet believe about himself*; the adverse sum — *a man is pressed by how badly he is thought of, whether or
not he agrees.*

> ### ✅ **D-5 · RULED 2026-09-06 BY JORDAN — *"second-person lever stays refused."* THE WALL HOLDS.**
>
> **What is now settled, permanently rather than pending:** no creditor verb · no `call_in` · no
> obligee-side closer on an obligation · **no hook.** `T-m` is not amended, and forgiveness is
> **inexpressible as clemency** — that absence is now *accepted and stated* rather than open. `P-36`
> closes as ruled.
>
> **What survives, and it is not nothing.** *Publicity* — the creditor tells that the debt exists,
> which is an act on their own ledger and is witnessed. And *mercy as a new edge the creditor owns* —
> a counter-obligation. **Slower, more political, and visible to the room. That is the trade, and it
> is the one the design was built for.**
>
> ⭐ **AND THIS IS WHY THE FEAR LEVER IS LAWFUL AT ALL.** You cannot move a man. You can name what he
> dreads, and **his own decision procedure does the rest** — the coercion happens inside the target,
> by their own reading, never by your write. **A design that had granted the second-person lever would
> not have needed to find that, and would have been much worse for it.** Every mechanism in PART D
> that reaches another person reaches them through what they themselves hold.

**D-6 · The one corpus fault that does not reconcile with fail-forward.** *"Whoever touches it is
killed"* is the single terminal fault with no corpus-supplied next move. **Options:** treat it as the one
place the ladder's failure is not the outcome — the outcome is removal from the world, which is a
different contest entirely — or soften the corpus. **Handed forward unsoftened.** **Blocks:** one row of
the speech-kind roster.

**D-7 · Two corpus-versus-evidence branches.** Whether a detailed denial outperforms a brief one; whether
displayed anger extracts concessions — **and the study marks the evidence for the second unverified
itself.** Data authoring, per branch, low stakes, sweepable either way. **Blocks:** two roster rows.

**D-8 · One-tick trials — listed so it can be vetoed, not escalated.** A hearing and its judgment cannot
share a season, because of where the strata sit. **This passes test 4 and is therefore NOT a decision
request** — but if one-tick trials are wanted, **the row to argue about is the strata roster, not this
subsystem.**

**Closed by the five tests rather than escalated, recorded so the closures are visible:** the three kinds
of absence (derivable after step 22) · whether the per-actor rung is a forbidden tally (the aggregates
ruling) · the tribunal ratchet (the determiner's own release closes it) · register position (moot after
step 11) · refuse-versus-demote (always demote) · whose score the obstacle halves (inject and sweep) ·
the nine unopened conviction axes (ruled open) · whether the three prizes collapse to one (engineering,
after the bar).

---

# PART I · WHERE THIS PLAN IS WEAKEST

**Handed forward rather than hidden.**

1. ⭐ **The outer act's degree is not specified anywhere in the design.** The speech opens the contest and
   the seam returns **one** margin — but a proceeding is six draws. This plan chooses **the opening
   speech's margin** as what the outer fold bands, with every inner act folded with a provider-computed
   resolution. **That is a choice this plan made; the design does not state it**, and the alternative
   (the disposal's degree) is defensible. **It must be stated on the row before the bar runs.**
2. **The narrowed fan-out as the shipped default is a corpus-wide change with one sweep behind it.**
   Dozens of baselines move. If two of the four channels match nobody, the narrowed arm is
   presence-only and **every character learns only what happens in front of them.** M-6 is the only check.
3. **Reception's valence reuses the alignment table**, which conflates *what I prefer to do* with *how I
   regard someone who did it.* Arm 2 is a second table. **If the sweep does not separate them, the term
   is decoration wearing a person's name.**
4. **The quorum widens the precondition grammar** on the one form nobody has ever exercised. If the
   cardinality cannot be evaluated without reaching a resolver-side Query, **the fold would be evaluating
   a Query inside a precondition, which is new.**
5. ⛔ **`18_FINDINGS.md`'s severity carrier was wrong, and this plan corrects it.** That document proposed
   the claim's visibility field; **it is inert — one occurrence in the whole module, the declaration.**
   Step 21 substitutes the observer set. **The findings document is corrected in the same commit.**
6. **The habituation loophole is assumed symmetric.** *Press, wait, press* decays his habituation and
   your infamy on one clock. ⚠ **But under step 3b, your record about HIM is a person-claim and outlives
   his record of the event — and the clocks stop being symmetric.** Steps 3b and 5 must be swept
   together, and this plan orders them apart.
7. **A dissenting commitment cannot be hidden from the room** — every co-located attendee witnesses it
   regardless of the key. So the council row's *"consensus discourages the disagreement from forming at
   all"* is a **person-side** effect (a member who wants no record does not commit), not the key's.
   **That is probably right, and the row's prose says otherwise.**
8. **A told claim carries the teller's MAXIMUM held confidence**, so a teller holding one thing at full
   confidence and another at low tells at full. **Which of the two was told is not distinguished** —
   that is the *content of a told claim does not exist* problem, and step 19 fixes only the investigation
   half. ⚠ **Telling's own product column is not planned here and probably should be.**
9. **The forty-season run has never been done**, and three of the standing loop's four bounds are corpus
   properties with no column to turn if it concentrates.
10. **The verb-lookup for a claim's valence assumes every event kind sits on exactly one verb's emit
    column.** Two body literals remain and refusal kinds are shared. **Claims whose predicate is a refusal
    get zero valence, silently.**

---

> ## THE PLAN IN SIX LINES
>
> **Phase 1 makes the world a story instead of a log** — narrow the fan-out, name the actor, mint
> hearsay, measure the cap, give characters a want and a fear that can be pressed, and write the roster.
> **Phase 2 makes the structure exist and resolve** — the row, the repoint, the bench, the loader with a
> real quorum, the composed obstacle, the two verbs, and a provider whose three aggregates are free
> because they die with the run. **Phase 3 is the one that makes it a game** — the room reads you, and
> what it holds about you moves the obstacle you cannot see. **Phase 4 keeps season forty from looking
> like season thirty.**
>
> **One new field. Four deleted. Three keys cut. Six measurements that must run before what stands on
> them. Five decisions that are genuinely yours.**
