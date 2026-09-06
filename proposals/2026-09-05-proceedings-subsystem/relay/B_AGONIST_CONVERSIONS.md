> ## RELAY STAGE B · THE AGONIST — `opus`, full tools, answerable for every position
> ## Status: **PROPOSED (2026-09-06). NOTHING HERE RATIFIES ON MERGE.**
>
> **Preserved verbatim, including the parts the antagonist stages broke.** Where stage C or D killed
> or wounded a position, the kill is recorded in `17_PLAYABILITY.md` and **is not patched back into
> this file** — a relay whose producer output is silently corrected afterwards has no fidelity to
> report. Read this as what was claimed; read `17` for what survived.
>
> **Every position states its own strongest objection (part vi) and its own falsifier (part v).** That
> is the format's whole discipline: a position that cannot name what would show it wrong is not a
> position. Two of the thirteen name objections the antagonist stages then confirmed independently,
> which is recorded in `17` as convergence rather than as a finding the agonist got credit for
> anticipating.
>
> ⚠ **The agonist did not see the antagonists, and the antagonists did not see this header or the
> agonist's reasoning** — only this document's body. Independence is structural: both antagonists ran
> as `valoria-critic`, whose agent definition grants `Read, Grep, Glob` and no write tool, so neither
> could have edited what it was auditing whatever its prompt said (`CLAUDE.md` §10).

---

# AGONIST CONVERSIONS — thirteen positions turning `proposals/2026-09-05-proceedings-subsystem/` into a game

**Agonist output, 2026-09-06.** An independent antagonist receives this and not my reasoning. Every
position below is stated to be attacked, not to be safe. Where a position is right and blocked, the
block is named **in** the position.

**Inputs.** `FABLE_PLAYABILITY.md` (the census, the precedents, the option surface, the refusals) is
taken as established and is not re-derived. The eighteen proposal files and the study's
`04-part-III-actor.md` / `09-figures.md` were read directly. Live schema read at
`proposals/2026-09-01-season-loop-tests/tracer/shape.py`, `.../2026-09-02-executable-architecture/{verb_table,rosters,write_matrix}.yaml`,
`engine/autoload/{dice_engine,sigma_leverage}.py`.

---

## THE TWO THESES, STATED BEFORE THE POSITIONS SO THEY CAN BE ATTACKED AS A PAIR

> ### **THESIS A — A BINARY IN THIS DESIGN IS ALMOST NEVER A SCHEMA FACT. IT IS A ROW VALUE OR A `requires` CONJUNCT, AND THE GRADIENT IT WANTS IS ALREADY IN THE OBSTACLE.**
> The obstacle is *composed and floored* by ruling (`06_RESOLUTION.md:210-225`, Jordan 2026-09-06).
> That makes it the one lawful sink for every "priced, not precluded" conversion. Thirteen of twenty
> binaries reach it at zero or negative schema cost. **The cost of the whole conversion is therefore
> not primitives; it is obstacle terms, and that is the number to attack.**

> ### **THESIS B — AN OPPORTUNITY NEEDS NO CARRIER, AND THE VENUE IS THE HALF THAT WORKS TODAY.**
> ⭐ **The orchestrator's independent position is ADOPTED WITH CREDIT and is correct as far as it
> goes:** under `AX-1` you cannot make anyone act, but you can change what candidates form for them;
> what you seize afterwards is a `Proposition` they uttered and committed to, immutable and dated.
> **I extend it in one direction and break it in another.**
>
> **Extension:** the venue half needs no other character's decision at all, so it is not blocked.
> The order calls you or does not; the opener's terms are a document somebody carries and somebody
> can burn; a `knot` is a standing information line into a closed room. Four live verbs, no lane
> dependency. **`06`, `09`, `11` are that half.**
>
> **Break:** *"a provocation deposits a claim in their ledger; their `opening_set` forms differently"*
> is **false at this commit and must not be written as if it were true.** `14:182-198` measures
> belief → decision SEVERED — `belief_contradicts` fires only on `predicate ∈ PERSON_PREDICATES ∧
> value is False`, the vocabularies are disjoint, **0 of 4,800 claims can fire.** A deposited claim
> changes nothing about what forms for them. What survives the break is the **seizure** half, which
> runs on *their own committed edges* rather than on their beliefs — and that is `08`.

---

# LANE A · GRADIENTS INSTEAD OF BINARIES

---

## POSITION 1 · [A] Aptness is how the room takes it, not whether the act exists

**(i) THE CLAIM.** `speak`'s genre conjunct must be deleted from `requires`: an inapt speech FORMS,
DRAWS, and is priced by an obstacle term — so a player can refuse the frame, lose the room for it,
and learn what the room heard, where today the Candidate never forms and the turn buys nothing.

**(ii) THE MECHANISM.**

```yaml
# verb_table.yaml — speak.  ONE CONJUNCT REMOVED, none added.
  requires:    "a live occasion at the actor's venue whose docket names the subject"
  requires_typed:
    form: existence, of: subject, kind: DocketItem      # §F.24a form 1 — UNCHANGED
    # ⛔ DELETED: the genre-match conjunct (04_VERBS.md:138-139, 157). `requires` answers
    #    whether there is an occasion to press at. It does not answer how well the pressing fits.
```

```
base_Ob += aptness( speech_kind, genre_set(bench.remit), rung(run) )        # TERM 6
  genre  : speech_kind.apt_genre ∩ genre_set  ==  ∅   →  + MISMATCH        # a set test, not a branch
  rung   : ordinal_distance( speech_kind.apt_rung , rung(run) )  ×  STEP   # rung_kinds is ORDERED
```

```yaml
# rosters.yaml: speech_kinds — the roster 04_VERBS.md:144-148 already promises and that
# `grep -n "speech_kinds" rosters.yaml` returns NOTHING for. Two columns, both content (ID-12).
- kind: refute      · apt_genre: [forensic]                · apt_rung: conjecture
- kind: construe    · apt_genre: [forensic]                · apt_rung: definition
- kind: propose     · apt_genre: [deliberative]            · apt_rung: —
- kind: amplify     · apt_genre: [epideictic, deliberative]· apt_rung: —
  # … the twelve. Adding one is a data edit; nothing branches on a member.
```

**The reading the room forms is NOT a new Event kind.** `Event.observed : tuple` (`shape.py:2136`) is
*"what the fold read to reach this Event"*, the same triple a `Claim` carries. The failed aptness
test IS a read the fold performed, so it lands there with no schema touched, and
`observation_deposit_modes: actor` (`rosters.yaml:305-345`, the mode `P-05` forces) delivers it to
the speaker alone. **The room learns the band (`Event.degree`, `shape.py:2117`); the speaker learns
why.** That split is `AX-2` paying rather than being paid.

**(iii) THE COST.** Carriers 0 · edge kinds 0 · verb names 0 · fields 0 · **Event kinds 0**.
Arrangement keys 0. **Obstacle terms +1. New hidden magnitudes +2** (`MISMATCH`, `STEP`), both
`assumption`-grade — inject, declare, sweep at pools {1,4,9,16} (`P-27`'s falsifier).
**Injection site: `proceedings.run`'s obstacle composition, build step 0**, alongside the five that
are already there; the roster loads at step 2. One `requires` conjunct is **removed**.

**(iv) THE PRECEDENT.** **Ace Attorney's *present*.** A wrong present is charged a fraction of a bar
and never refused; the game's whole texture is that you may try the contradiction you believe in.
**What changed to make it lawful:** Ace Attorney's penalty is a flat deduction from a visible meter —
`R-9`/`T-a` refuse both. Here the price composes into the obstacle and is floored at 1 (`P-232`), so
it is never displayed and never gates.

**(v) THE FALSIFIER.** A trace, not a grep. Seed a two-attendee hearing at a **deliberative** bench;
attendee A takes `speak` with `kind: refute`. Required in the log: a Candidate formed; **exactly one**
`continuous_engine_sample` call for that act; a `matter.*` emission carrying a `degree`; A's ledger
carrying an `Observation` naming the genre mismatch; **and B's ledger carrying the band and NOT the
reading.** Then re-run at the same seed with `kind: propose` and require a **different band or a
different margin**. *Shows it wrong:* the Candidate does not form; or the two runs produce identical
margins (the term is inert); or the mismatch reading appears in B's ledger (`AX-2` leak).

**(vi) MY STRONGEST OBJECTION.** **Pricing a category error routes every mistake through standing,
and `14:263-282` demoted the public debate for being about standing only.** If the only consequence
of any inapt move is that people think worse of you, I have converted twelve failure modes into one
currency and re-created the degenerate game as the destination of *every* error. The audit says the
same at §4.6 pt 1 and has no clean answer either. **My partial answer, which I do not think is
sufficient:** the aptness term raises the obstacle, so the immediate consequence is a *worse band on
the matter* — which writes `Person.stance` and moves the rung — before it is standing at all. But a
patient antagonist should press exactly here.

---

## POSITION 2 · [A] The finding carries a strength, and the appeal must beat it

**(i) THE CLAIM.** `determine` writes `Tenure.degree` and the proposal never says what value goes in
it or what reads it; the value is the determiner's **own strongest live claim about the matter**, the
readers are the appeal's obstacle and the disposal's reach, and reading it converts finality from a
key into a price without touching `appeal_basis` at all.

**(ii) THE MECHANISM.** Three moves, none of them a schema change.

1. **The value source, which is a hole nobody has named.** `04_VERBS.md:172` carries
   `writes: ["Tenure.degree"]` on `determine` and says *"⚠ UNCHANGED from the live row"* — and
   `determine` declares **no `contests:`**, so it has no margin and no band. The proposal writes a
   field it cannot fill. **Fill it from the determiner's own ledger:**
   ```
   finding.degree := band( max{ c.confidence : c ∈ actor.ledger, c.subject == matter } )
                     -- form 6, own_ledger. ONE owner, ONE reader, resolver-side.
                     -- bands declared in DATA on their own roster, NOT the ladder's four (T-k).
   ```
   A bench told the matter firsthand and recently finds **strongly**; a bench that has it at third
   hand through `chronicle` finds **weakly** — and `Claim.confidence` (`shape.py:2157`) gains its
   first reader outside eviction.
2. **Reader one — the appeal.** In a nested appeal run the prior finding's strength composes into
   the obstacle as an ordinal (**term 13, nested only**). `appeal_basis: none` is untouched and still
   means *no bench holds the remit* — a structural absence, not a difficulty. **Where an appeal
   exists at all, it is now a contest against how strongly the first bench held it.**
3. **The compromise, and it needs no carrier at all.** Duel of Wits' rule is *the winner gives back
   in proportion to what they lost*. Here the winner's losses are **the descents they were witnessed
   making** — each one an Event every attendee deposited (`00_DERIVATION.md:150-190`). So a matter
   carried at *quality* by a party who descended three rungs leaves three permanent concessions in
   every ledger in the room, and those claims are what the `reception` term reads at their **next**
   proceeding. **The compromise is realised as standing, and it is not stored anywhere.**

**Why this does not repeat the retracted `Tenure.degree` proposal.** `00_DERIVATION.md:275-319`
overturned writing the **rung** into `degree` on a **`commit`** edge, on five grounds. Every one of
the five is about that edge and that value: `Faction.head?` reads `degree` on `commit`s (objection 1);
descents would be non-owner writes on the opener's edge (2); five games have no `open_case` (3); two
senses of one field (4); `payload` is equally unread so the falsifier could not discriminate (5).
**I write a strength onto the FINDING's own Tenure, opened by `determine`, whose subject is the
determiner.** No `commit` edge is touched, no descent writes it, no `open_case` is required, the
sense is `F.4`'s own hypothesis (*degree is a strength*), and the falsifier below discriminates
because `payload` cannot carry an appeal obstacle.

**(iii) THE COST.** Carriers 0 · edge kinds 0 · verbs 0 · **fields 0** · Event kinds 0 (the matrix row
`(Tenure, degree) → tenure.graded` already exists at `write_matrix.yaml:329-335` with `determine` as
its producer). Arrangement keys 0. **Obstacle terms +1, nested-appeal only. Hidden magnitudes +1**
(the band→ordinal coefficient). **One data roster** of finding-strength bands. Two fields gain
readers (`Tenure.degree`, `Claim.confidence`) — two `ID-13` closures.

**(iv) THE PRECEDENT.** **Burning Wheel's Duel of Wits compromise**, plus **Ars Magica's Certamen**
(the winner's margin sets what may be imposed). **What changed:** BoA is a per-side visible track and
`T-a` refuses it as a field. The replacement is the witnessed descent set — which is not a track, is
not visible to everyone identically, and can be **wrong** in a given ledger. So the compromise is not
a number both players agree on; it is a fact each observer holds separately.

**(v) THE FALSIFIER.** Plant two determinations of the same matter at the same seed, differing only
in the determiner's ledger — one holding a `firsthand` claim at high confidence, one holding the same
claim `told_by` at low. Require: two different `Tenure.degree` values on the two findings; then open
an appeal against each and require **different obstacles and, at a fixed draw, different bands**.
*Shows it wrong:* the degrees are equal (the value source is inert); or the appeal obstacles are equal
(the reader is inert); or `Faction.head?` changes behaviour anywhere in the same run (the objection-1
collision is real after all).

**(vi) MY STRONGEST OBJECTION.** **The value source is the weakest joint in this entire document.**
Mapping a `Claim.confidence : int` onto an ordinal band is a second banding of a quantity that is not
a margin, and even on its own declared roster it will read as a shadow ladder — which is `T-k`'s exact
smell and Jordan's 2026-08-15 *"systems should not need different degree bands"*. A defensible
alternative I could not choose between: leave `degree` unwritten and put the appeal's obstacle on the
**count of live findings** the matter carries. **And the second objection is sharper:** a bench that
finds strongly because it was told firsthand means *the winning move is to reach the bench before the
sitting*, which the design already calls corrupt and cannot distinguish from diligence. That may be
the right game. It is not obviously the intended one.

---

## POSITION 3 · [A] Partial is the band that costs, and its content is the run's own log

**(i) THE CLAIM.** `Partial: []` inverts the one precedent that most reliably makes an exchange
playable; Partial must write the actor's own stance and raise the obstacle on their next press, with
the raise derived from *this run's own emissions* and stored nowhere.

**(ii) THE MECHANISM.**

```yaml
  writes:
    Overwhelming: ["Person.stance"]    # the ACTOR'S OWN. See below — this must be bound.
    Success:      ["Person.stance"]
    Partial:      ["Person.stance"]    # ⭐ was []
    Failure:      ["Person.stance"]
  emits:
    Partial:      ["matter.held"]      # unchanged — the rung does NOT move
```

```
base_Ob += HELD_STEP × |{ e ∈ run.emissions : e.kind == "matter.held" ∧ e was this actor's }|   # TERM 7
        -- the intra-run fold, third instance. The design already uses it twice:
        --   rung(run)                        00_DERIVATION.md:298-302
        --   proofs told so far in this run   06_RESOLUTION.md:221
        -- Owned by nobody. Stored nowhere. Dies with the run (T-a, ID-1 one scale down).
```

**⚠ AND `writes` MUST NAME WHOSE STANCE, WHICH THE PROPOSAL DOES NOT.** `04_VERBS.md:72` writes
`Person.stance` at three bands and never says whose. **If it is the hearers', every band is a
non-owner write and the row breaches `AX-4` as written.** It is **the actor's own**, and this position
binds it: a speech that is held moves *you*, visibly straining, which is precisely the corpus's
*visible effort — TERMINAL once seen* (Fig. 3).

**(iii) THE COST.** Carriers 0 · edge kinds 0 · verbs 0 · fields 0 · Event kinds 0.
**Obstacle terms +1. Hidden magnitudes +1** (`HELD_STEP`). Injection site: build step 0; the fold
lives in `proceedings.run`, build step 6. **It also closes an `AX-4` ambiguity for free.**

**(iv) THE PRECEDENT.** **Apocalypse World's 7–9** — *you get it, at a cost, or a lesser version.*
**What changed:** in AW the MC chooses the cost, and there is no MC here (`AX-1`, `R-3`). The cost is
derived from the run's own ordered emissions instead, which is the one construction that can produce
"a lesser version" without anybody deciding it.

**(v) THE FALSIFIER.** ⚠ **This one needs care, because attribution is where levers go to die.** Run a
seeded four-turn hearing in which one actor's first two presses land Partial. Require: the third
press's obstacle is strictly greater than the first's, by exactly `2 × HELD_STEP`; the same actor's
`Person.stance` appears in `changes[]` at every Partial and **no other person's does**; and the
`matter.*` rung is unchanged across all three. *Shows it wrong:* the obstacle is flat (the fold is not
read); or a hearer's `stance` is in `changes[]` (`AX-4`); or the count includes another actor's Partials
— which would mean the fold is reading `Event.subject` for attribution, and `Event.subject` is the
actor **only because `T-d` is violated in mechanism** (`01_AXIOMS.md`, `T-d`; `W24` intends to remove
it). **Build the count from the provider's own loop — it knows whom it called — not from `Event.subject`.**

**(vi) MY STRONGEST OBJECTION.** Three of four bands now write the same field, so the ladder's
information content at the write site collapses to *did the rung move* — and if a Partial and a
Failure both write your stance and neither moves the rung, the player experiences them identically
until they see the fold's effect two turns later. **I think that delay is the design, and I also
think a first-time player will read it as the game not responding.**

---

## POSITION 4 · [A] Advantage is bought, not composed — the σ-channel paid for with a debt you open now

**(i) THE CLAIM.** The design has a whole uniform advantage channel it does not call
(`06_RESOLUTION.md:271`: *"available and not used by the five terms"*), and the lawful thing to spend
in it is a live `oblige` the speaker opened in this run — which is the only player-facing number this
design may legally show.

**(ii) THE MECHANISM.** Two live verbs, one existing engine path, nothing else.

```
turn n    :  oblige   -- eligibility own, requires "—" (verb_table.yaml:357-364).
                         YOU are its subject; YOU owe. No non-owner write anywhere.
                         Witnessed, permanent, closable only by your own `release`.
turn n+1  :  speak    -- the resolver reads: live obliges opened BY the actor IN THIS RUN
                         whose object is present  →  a NAMED LEVEL
             net += net_boost( levels_to_net_sigma(aggressor=[levels]), pool )
                         sigma_leverage.py:190-203.  Δz = soft_cap(net_σ) at EVERY pool size.
                         M_MAX = 1.5, so ~two majors saturate. THE CAP IS THE ENGINE'S, NOT MINE.
```

**Three things this is not.** It is **not** an Ob reduction (`Eff_Ob = base_Ob − eff_σ·σ_N` is F1/ED-884,
forbidden — `R-5`). It is **not** a flat roll bonus (`Δz ∝ 1/√pool`, `R-6`). It **does not** resolve on
`eff_ob()`, which stays display-only and, per `15` PART E, undisplayed.

**⭐ AND IT IS THE ONE NUMBER THE PLAYER MAY SEE.** `R-18` forbids the obstacle, the margin, a band
preview, a percentage — and **permits named levels of the player's OWN advantage** (SKILL §11.5 P-i;
`07:176-178`). *"Moderate advantage: you promised Aldric the mill, in front of the bench"* is the
player's own hand, sourced and dated. **Legible hand, illegible room** — which is the half of Disco
Elysium that survives `AX-2`, and it is the design's answer to its own sharpest experiential risk
(`07` D.1) without showing a single thing about the room.

**(iii) THE COST.** Carriers 0 · edge kinds 0 · verbs 0 · fields 0 · Event kinds 0 · arrangement keys 0
· **obstacle terms 0** (it enters the other channel). **Hidden magnitudes 0.** **Visible magnitudes +1**
— which offer maps to which of the four rostered levels; `LEVEL_SIGMA` supplies the four values
already (`sigma_leverage.py:97-102`). The real cost is a **turn in the order**, which is the scarcest
thing in the room.

**(iv) THE PRECEDENT.** **Blades in the Dark's devil's bargain** — a die now for a complication later,
chosen. **What changed:** Blades' bargain is offered by the GM and its complication is narrated.
Here the player opens it themselves, the complication is a **`Tenure` with a real subject and a real
object** that outlives the proceeding by seasons, and closing it is `release` — witnessed forswearing.

**(v) THE FALSIFIER.** Seeded run, identical in every respect except that in arm B the actor spends
turn 1 on `oblige` to a present party. Require: arm B's turn-2 `net` exceeds arm A's by exactly
`net_boost(level, pool)` for the declared level; the *obstacle* is byte-identical between arms; the
`Tenure` persists into the next season's world; and a third arm with **five** obliges shows the
soft cap biting (`M_MAX = 1.5`), not five times the boost. *Shows it wrong:* the obstacle moves (I have
reintroduced the retracted Ob-reduction form); or the boost scales differently at pools {1,4,9,16}
(the uniformity claim is what the channel is for).

**(vi) MY STRONGEST OBJECTION.** **This may re-open a ruling that was just made.** Jordan ruled
2026-09-06 that the five terms compose the obstacle, after a draft had tried to rewrite all five as
σ-levels and was corrected as an overreach (`06_RESOLUTION.md` §C.0). I read that ruling as scoped to
**room** terms and silent on **bought** advantage, and `§C.2` of that same file says the σ-channel is
*"the channel to move `reception` into if `P-27`'s sweep says so"* — so the channel is live in the
design's own words. **An antagonist may read the ruling wider, and if they are right this position is
a second attempt at a thing that was already refused.** Second objection: *"which promise is worth
which level"* is a magnitude the study cannot source (`R-19`), and unlike an obstacle term it is
**shown to the player**, so getting it wrong is loud rather than quiet.

---

## POSITION 5 · [A] The ladder is two-way, and it always was — the design's prose is what is wrong

**(i) THE CLAIM.** The rung fold as written already admits an opponent's rung, so nothing needs
building: `00_DERIVATION.md:298-302` says *"the lowest rung any emitted `matter.*` Event in THIS run
has named"* — **any**, not *the actor's* — and the sentence in `05:76-86` that makes descent self-only
and one-way is a prose claim the fold does not support.

**(ii) THE MECHANISM.** No edit to the fold. One edit to the prose, and one consequence made explicit:

```
rung(run) := min{ rung named by e : e ∈ run.emissions, e.kind ∈ matter.* }     -- UNCHANGED

  A speaks at CONJECTURE and lands Overwhelming → emits matter.carried @ conjecture
  B's next speak is now at a matter standing where A put it, not where B left it.
  B did not concede. B was PUSHED, and the concession's claims are in the ledgers either way.
```

**The distinction that makes it a game is WHO PAID.** When you descend, you pay: a turn, and a
witnessed concession. When you are pushed down, **your opponent paid** — their turn, their proof,
their draw — and you carry the cost anyway. **That is a raise you must see or give**, and it is the
first mechanism in the design in which one player's spend lands on another player's position.

**Climbing back is still impossible and that is correct**: the claims are already in every ledger
(`AX-2`), and the ladder is finite (*"below quality there is nothing left to concede"*). So the ladder
stays monotone; what changes is that **you are no longer its only operator.**

**(iii) THE COST.** **Zero of everything.** No carrier, no field, no verb, no Event kind, no key, no
obstacle term, no hidden magnitude. It is a prose retraction plus a falsifier. ⚠ **One dependency:**
without **Position 1**, being pushed to a rung where your remaining speech kinds are inapt means your
next act is **refused** rather than expensive, which turns a raise into a stun-lock. `B-1` and `B-14`
must land together or neither should.

**(iv) THE PRECEDENT.** **Dogs in the Vineyard's raise / see / give.** **What changed:** Dogs' raise is
a visible dice pile — `T-a` refuses it as a field. The rung is not a pile; it is a fold over the run's
own emissions, and *seeing* it is speaking at it, *giving* is `repudiate`.

**(v) THE FALSIFIER.** Two-party seeded run. A opens at `conjecture` and is forced (planted seed) to
Overwhelming. Require: the fold reports `rung(run) == conjecture` for **B's** next turn, B's obstacle
carries the rung term at that value, and **no Event attributes a descent to B**. *Shows it wrong:* the
fold is filtered to the acting person's own emissions — in which case the prose was right, the fold is
self-only, and this position is empty. **That single trace decides it.**

**(vi) MY STRONGEST OBJECTION.** It may be a distinction without a difference in play. If the rung
term's magnitude is small, being pushed is a shrug; if it is large, a single lucky Overwhelming
collapses the whole ladder on turn one and the hearing is over before anyone has spent anything.
**The band is `margin ≥ 3` on a fractional obstacle floored at 1, so an Overwhelming is not rare
against a weak opponent**, and the design has no re-roll, no fate point and a soft cap that makes
recovery worse on purpose (`P-26`). **This position may hand the game to the first good draw.**

---

## POSITION 6 · [B] The terms of the proceeding are a document somebody carries, and it can be burned

**(i) THE CLAIM.** `Record.stages` is written by `open_case` and read by nothing; giving it a reader
for **everything except the order** makes the opener's declared terms — the arbiter, the depth cap,
the return day — into a physical object that `carry`, `forge` and `destroy_record` already act on, and
it does this **without** the ruling the audit says `Record.stages`-as-order needs.

**(ii) THE MECHANISM.**

```
open_case.requires : "the act DECLARES the stages and their terms"        # verb_table.yaml:366-375
open_case.writes   : ["Record.exists", "Record.stages"]                   # ALREADY. Read by NOTHING.

proceedings.run reads, from the case Record:
   max_depth        -- ⭐ TODAY THIS IS "caller-supplied, NO DEFAULT" (H-87) and the caller
                       INVENTS it. The Record is where T-n says it lives.
   named arbiter    -- narrows bench_basis to ONE seat. `03:479-481`'s "game before the game",
                       which the proposal names and never plays.
   the return day   -- ⚠ BLOCKED on P-04 (`Tenure` has no `term`). Named, not assumed.

⛔ NOT the order. The order stays `arrangement.order`, from the row, per the seam amendment
   (08_SEAM.md:88-91). R-14's letter is UNTOUCHED and no ruling is required.
```

**And then the live verbs do the work nobody has asked them to do.**

| act | live row | what it does to a proceeding |
|---|---|---|
| `carry` | `verb_table.yaml:83` | the terms travel with a person. **Reach the person, reach the terms** |
| `destroy_record` | `:158` | **burn it before the appeal**: `max_depth` has no source, the appeal returns a typed `Refusal(depth_cap)`, and the refusal EMITS. Witnessed. |
| `forge` | `:229` | a false arbiter, a false cap. `Record.forgery_quality` (`shape.py:2418`) already exists |
| `petition` | `:377` — `requires: "—"`, no dedup, no cap | **demand the seat docket something.** The route to a summons or an adjournment |

**(iii) THE COST.** Carriers 0 · edge kinds 0 · verbs 0 · fields 0 · Event kinds 0 · obstacle terms 0 ·
**hidden magnitudes 0.** One field gains a reader (`Record.stages` — an `ID-13` closure). ⭐ **And it
pays a debt rather than adding one:** `H-87`'s no-default `max_depth` currently has no lawful source
at all, and this supplies one.

**(iv) THE PRECEDENT.** **Republic of Rome's presiding magistrate** — who controls what is proposed
and in what order is a game before the votes. **What changed:** Rome's magistrate controls the order;
mine controls the *terms*, because the order is the seam's and I will not spend a ruling on it. The
second half is **Suzerain's constitution as an amendable document** — except a `Proposition` is
frozen (`shape.py:2425`), so terms are **re-uttered**, never edited, and the old ones stay in the log.

**(v) THE FALSIFIER.** Open a case declaring `max_depth: 2`; run the hearing; `destroy_record` the case
Record in the intervening season; then attempt the appeal. Require: the appeal returns
`Refusal(depth_cap)` **and emits**, the emission's `causes[]` walks back to the `destroy_record` act,
and every attendee of the destruction holds a claim about it. Then re-run with `forge` substituting
`max_depth: 5` and require **five** appeals to be reachable. *Shows it wrong:* the appeal proceeds
after the burn (the cap is not sourced from the Record — the caller still invents it, and the position
is decorative).

**(vi) MY STRONGEST OBJECTION.** **A Record read at RESOLVE is world state, and I have argued the
order out of it while leaving three other terms in.** The seam amendment's *purpose* is that a
provider's behaviour comes from declared data and not from the world; a `max_depth` read from a
burnable document is behaviour from the world by exactly the same argument. **My line — that
sequencing sub-steps is the amendment's subject and parameterising a cap is not — is a reading, and a
strict antagonist will say I have routed around `R-14` rather than honoured it.**

---

## POSITION 7 · [A/B] The advocate's rope is a Proposition, and presence is four degrees

**(i) THE CLAIM.** `GO / SEND / NEITHER` (`07:50-55`) is three options because nobody wrote down the
instructions; the instructions are an immutable `Proposition` the principal utters and the advocate
commits to, which makes presence a gradient **and** deposits an object that can be produced against
the advocate who exceeded it.

**(ii) THE MECHANISM.** The treaty pattern from `14:75-91`, pointed at advocacy.

```
principal :  utter  OUGHT("R speaks for me; R may concede to DEFINITION and no further")
advocate  :  commit  to that Proposition          # requires: the Proposition exists — form 1
advocate  :  oblige  to the principal             # the duty. verb_table.yaml:357
                                                  # → 03_PARAMETERS.md:317's advocate, exactly
```

| degree of presence | the acts | latitude |
|---|---|---|
| **you go** | `move` | full `conduct`; you may concede at any rung |
| **an advocate, narrow rope** | the three above, `payload`-free, rung named in the Proposition | absorbs defeat (`AX-1`); **may not concede below the named rung** |
| **an advocate, wide rope** | same, a lower rung named | absorbs more, concedes more, and you cannot recall them |
| **a letter** | `create_record` + `carry` + a debtor's `tell` | all `brought`, no `conduct` — the *telhīs* |
| **nothing** | the absence of `move` | free, terminal if wrong |

**⭐ AND THE ROPE IS SEIZABLE, WHICH IS THE POINT.** The Proposition is `frozen=True`, authored and
dated. An advocate who concedes below the named rung has been **witnessed contradicting a Proposition
he committed to** — and anyone holding both can produce it. That is Blood on the Clocktower's
mechanism (*a public claim is immutable and contradiction is detectable*) arriving with no deception
subsystem.

**⚠ I DECLINE `Tenure.payload`, WHICH THE AUDIT OFFERED, AND THE REASON IS LOAD-BEARING.**
`write_matrix.yaml:53` records that under `#358` rev.2 §B.8 **`Tenure.payload` is REPLACED by
`term?`**. A reader built on it dies at that migration. The Proposition survives it, is immutable
where a payload is not, and is *produceable* where a payload is private. **Three of the audit's four
unread fields are closed by these positions; the fourth is declined on the record.**

**(iii) THE COST.** Carriers 0 · edge kinds 0 · verbs 0 · fields 0 · Event kinds 0 · keys 0 ·
**obstacle terms 0 · hidden magnitudes 0.** The `reception` term must read *who is speaking* — which it
already must, since reception is composed from the hearers' claims **about the speaker**
(`15` PART C).

**(iv) THE PRECEDENT.** **Diplomacy's press and the stab** — an unenforceable instruction, and
everyone remembers. **What changed:** Diplomacy's press is out-of-band and unrecorded; here the
instruction is *in* the game state, immutable, and its breach is a witnessed contradiction rather than
a social memory.

**(v) THE FALSIFIER.** Seeded run: principal utters the rope at `definition`; advocate is driven to a
losing position and takes `speak` at `quality`. Require: the act **forms and resolves** (it is not
refused — the rope is not a `requires`); the Proposition and the advocate's `commit` to it are both
live in the log; and a later `tell` by any holder of both produces a claim whose subject is that
Proposition. Then require the **principal's** standing is untouched by the defeat and **is** touched
if the principal was the utterer of a discovered lie. *Shows it wrong:* the advocate's defeat writes
the principal's `stance` (`AX-1`/`R-10` breach); or the rope gates the act (I have smuggled a
`requires`).

**(vi) MY STRONGEST OBJECTION.** **The rope binds nothing.** Under `T-m` and `AX-1` the advocate may
exceed it freely and the only consequence is reputational — so "how much rope" is a decision whose
outcome does not depend on the rope. In CK3 or Suzerain the instruction would constrain; here it only
records. **That may be exactly right (a principal who could bind an agent's speech would be acting
through them, which `AX-1` forbids), or it may mean the whole gradient is flavour.** I cannot
distinguish those two readings from the design as it stands.

---

## POSITION 8 · [B] A proof is apt in proportion to the statement it contradicts

**(i) THE CLAIM.** The fifth obstacle term counts proofs; it must **weigh** them, and the weight is
whether the claim's subject is a `Proposition` the opposing party committed to **in this run** — which
makes the sequence *provoke a commitment, then produce the contradiction* a real two-turn play using
only live rows.

**(ii) THE MECHANISM.** No new term. A weight function on term 5, in the grammar the design already
has (`§F.24a` **form 5** — a relation between actor and subject over prior acts, `03:191-198`):

```
term5 :=  Σ over  t ∈ { tell acts by this actor in this run } :
             DIRECT   if ∃ commit by the opposing party, in this run, to a Proposition p
                      with  t.claim.subject == p.id                # shape.py:2151 / :2426
             INDIRECT otherwise
   -- Claim.subject, Proposition.id and the run's own ordered emissions ALL EXIST.
   -- The mirror test stays the PLAYER'S: a symmetric proof is DIRECT and still moves nothing,
      because the opposing party can produce its mirror on their turn. The engine never checks it.
```

**⭐ THE CREATE HALF, AND WHERE IT BREAKS.** *Creating* the opening means getting them to commit —
`speak` with a person subject under Fig. 26, or an `utter` they must answer. **The orchestrator's
claim that a deposited claim changes what forms for them is FALSE at this commit** (`14:182-198`,
`H-72`, 0 of 4,800). **What is true and is enough for now:** a party who is a party *has already
committed* (`03:312-320` — a party is a live `commit`), so the opposing commitments this term reads
**exist by construction in every contested proceeding**, with no belief edge required. The seizure
runs today; the provocation waits on `H-72`, and the honest first act toward it is closing that edge
in the lane that owns it.

**(iii) THE COST.** Carriers 0 · edge kinds 0 · verbs 0 · fields 0 · Event kinds 0 · **obstacle terms 0**
(term 5's weight function changes) · **hidden magnitudes +1** (`DIRECT : INDIRECT` ratio).
`B-4`'s `proofs: []` / `proofs: [...]` key survives as an **admissibility set** and does its real job:
`proofs: []` at a deliberative bench means the term is identically zero, which is Fig. 23 rather than
a switch.

**(iv) THE PRECEDENT.** **Ace Attorney's *press vs present*** — the contradiction is the object, and
what you present it *against* is the whole game. **What changed:** AA's statements are authored by the
game; here they are `Proposition`s real people uttered and committed to for their own reasons, in a
run whose log is the only transcript there is.

**(v) THE FALSIFIER.** Seeded two-party run. Arm A: the actor `tell`s a claim whose subject is a
Proposition the opponent committed to on turn 1. Arm B: the same claim, same seed, same pool, against
a Proposition **nobody** committed to. Require: different obstacles, and at a fixed draw a different
band. Then a third arm in which the opponent `repudiate`s the commitment before the `tell` — require
the obstacle reverts to arm B's. *Shows it wrong:* arms A and B are identical (the weight is inert);
or arm C does not revert (the term reads a dead edge).

**(vi) MY STRONGEST OBJECTION.** **It rewards baiting, and baiting is what the study calls a
category error.** The dominant line becomes *say something designed to make them commit, then produce
the contradiction* — which is a solved two-turn combo, and `15` PART A's whole complaint is about
solved lines. My defence is that the bait itself draws and can fail, and that their commitment is
theirs rather than something you can force. **I do not think that defence is strong, and this is the
position most likely to produce a degenerate opening every player learns.**

---

## POSITION 9 · [B] Silence when the order reaches you is priced by the room, and is still not an act

**(i) THE CLAIM.** Under a calling order — `rank`, `scripted`, `alternating` — being reached and
returning nothing raises your own obstacle for the rest of this occasion, and it does so **without an
act, an Event, a write, a verb or a field**, because the provider that called you knows it called you.

**(ii) THE MECHANISM.**

```
base_Ob += PASS_STEP × passes(actor, run)                                    # TERM 8
  passes := the number of times THIS PROVIDER'S OWN LOOP reached this attendee
            in this run under order ∈ {rank, scripted, alternating}
            and the attendee returned no act.
  order == free       →  nobody was CALLED  →  passes ≡ 0. Silence is invisible, correctly.
  order == written_only → no floor to hold  →  passes ≡ 0.
```

**⭐ AND IT STANDS ON NOTHING BROKEN, WHICH IS RARE HERE.** It needs **no** `Event.subject`
attribution, so unlike Positions 3 and 5 it does not rest on `T-d`'s violation-in-mechanism
(`01_AXIOMS.md`, `T-d`; `W24` will remove it). The provider sequences the attendees from
`arrangement.order` — the one thing `08_SEAM.md:88-91` licenses it to do — and it observes its own
return values. `R-14` is honoured exactly.

**And `withhold` stays un-invented.** `04:149-151` is right that silence *"is not an act at all"*: it
emits nothing, writes nothing, deposits nothing, and is forgotten when the run ends. What it does is
make the room harder for you **while you are still in it** — which is Liudprand at Constantinople,
who *"said nothing at the time because of the pain in his heart"* and whose silence cost him the room
he was standing in.

**(iii) THE COST.** Carriers 0 · edge kinds 0 · verbs 0 · **speech kinds 0** (`withhold` is not
rostered) · fields 0 · Event kinds 0 · keys 0. **Obstacle terms +1. Hidden magnitudes +1**
(`PASS_STEP`). ⭐ **And it gives `order` a second job**: five enum values that until now only sequenced
turns now also decide whether not-speaking is visible.

**(iv) THE PRECEDENT.** **Dogs in the Vineyard's *give*** — declining is a first-class move with a
price. **What changed:** in Dogs, giving ends the conflict. Here it does not end anything; it costs
you position in the room you are still in, and it is free the moment the order stops calling on you.

**(v) THE FALSIFIER.** Seeded five-turn run under `order: rank`, actor passes on turns 1 and 2, speaks
on turn 3. Require: turn 3's obstacle exceeds a control run (same seed, actor absent from turns 1–2
because they never travelled) by exactly `2 × PASS_STEP`; **the log contains no Event for the two
passes**; and no ledger anywhere holds a claim about them. Re-run under `order: free` and require the
obstacles to be equal. *Shows it wrong:* an Event exists for a pass (silence has become an act); or
the `free` arm also charges (the term is reading something other than the calling order).

**(vi) MY STRONGEST OBJECTION.** **The room forgets.** The fold dies with the run, so nobody
remembers next season that you sat silent through a hearing — and Liudprand's point is precisely that
they *did*. A design that prices silence only inside the occasion has taken the shallow half of the
example. **The deep half needs an Event, and an Event for a non-act is `AX-1` broken.** I take the
shallow half deliberately and I concede it is the shallow half.

---

## POSITION 10 · [A] The licence veto is four obstacle terms and one declared `BandExtension`

**(i) THE CLAIM.** Fig. 26's four conjuncts must be four prices and one structural ceiling, not one
boolean: failing one is *an attack*, failing four is *an attack, a standing contest, a characterization
and a bargain at once*, and today those are received identically.

**(ii) THE MECHANISM.**

```
base_Ob += Σ  { GOODWILL if no demonstrated prior goodwill (form 5)          # TERMS 9-12
              ; PRIVACY  if a third party is contained at the venue (form 1)
              ; REPEAT   if a prior live charge by this actor on this subject (form 4)
              ; STAKE    if the actor holds a stake the disposal would move (form 5) }
        -- the four forms are 03_PARAMETERS.md:186-198's own typing. Nothing new is grammared.

class UnlicensedFrankness(BandExtension):          # dice_engine.py:95-138 — the ONE legal power
    name = "unlicensed-frankness"
    context_keys = ("licence_failures",)
    def may_overwhelm(self, net, ob, licence_failures=0): return licence_failures == 0
        -- demotes 3 → 2 ONLY. An unlicensed frank speech cannot land as a triumph.

⛔ DELETE  `veto : bool`  from the seam signature (08_SEAM.md:17, 42).
   It is a SECOND HOME for a demotion the engine already owns — T-k, and the audit's B-2.
```

`interposed: [office]` waives all four, as data, exactly as `03:B.4` already argues — *a censor is
expected to repeat himself in public.* The four named readings (**hostile · competing · characterizing
· bargaining**) ride in `Event.observed` and deposit to the speaker under mode `actor`; the room gets
the band.

**(iii) THE COST.** ⚠ **This is the expensive one and I am not hiding it.** Carriers 0 · edge kinds 0 ·
verbs 0 · fields 0 · Event kinds 0. **Obstacle terms +4. Hidden magnitudes +4.** Plus **one declared
`BandExtension` subclass** — and against that, the seam signature **loses** `veto: bool`, so the seam
gets shorter and `T-k` gets its single owner back.

**(iv) THE PRECEDENT.** **Blades' position × effect declared before the roll.** **What changed:**
Blades declares position openly and the player trades against it; here the four terms are hidden and
the *ceiling* is the only thing the mechanism guarantees. The player is told nothing and can still
reason about all four, because all four are facts about **their own** prior acts and their own stake.

**(v) THE FALSIFIER.** Four seeded runs, identical but for the number of failed conjuncts (0,1,2,4).
Require: four distinct obstacles, monotone increasing; the 0-failure run **reaches** Overwhelming at a
planted margin ≥ 3; the 1-, 2- and 4-failure runs at the **same planted margin** return Success; and
`validate_context` **raises** on a misspelled context key. *Shows it wrong:* two failure counts give
the same obstacle (the terms are not separable); or the extension promotes anything, ever
(`R-7`); or a `veto: bool` survives anywhere in the seam (the duplicate is still there).

**(vi) MY STRONGEST OBJECTION.** **Four terms for one figure is a third of my whole magnitude budget
spent on the frank-criticism case, and frank criticism is one speech kind among twelve.** A tighter
design would compose one `licence` term from a count of failures — one magnitude instead of four —
and I chose four only because the study names four *distinct readings*. **If the sweep shows the four
are not separable in play, three of them are dead weight in a twelve-term obstacle, and the antagonist
should demand the sweep before the build.**

---

## POSITION 11 · [B] A closed floor defers the concession's price; it does not delete it — and `knot` is how you collect

**(i) THE CLAIM.** `P-41` ("descent is free in 6 of 12 rows, 3 of them terminal") is right about the
**timing** and wrong about the **amount**: `floor:` restricts `co_located` and touches none of the
other four witness channels, so a closed room's concessions arrive later, garbled, and through people
— and `tie / knot`, a live verb nobody has pulled, is a standing line into rooms you cannot enter.

**(ii) THE MECHANISM.** Nothing is built. Two facts are connected and one verb is pointed at them.

```
witness_channels : [post_remit, co_located, witness_key, document_key, chronicle]  # rosters.yaml:104-110
  floor: closed    →  co_located shrinks to the bench, the parties, the clerk.
                      IT DOES NOT TOUCH THE OTHER FOUR.
  document_key     →  whoever holds the case Record learns THAT it changed, NOT who changed it
  witness_key      →  ⭐ a live `knot` to the event's subject makes you a witness
                      (`_ch_witness_key`, shape.py:4360-4364 — verified by hand, not cited)
  chronicle        →  whoever is later told, at the TELLER'S confidence, possibly false
```

⚠ **AND WHAT THE KNOT DELIVERS DEPENDS ON A DEFECT, WHICH I SAY HERE RATHER THAN LET THE
ANTAGONIST FIND.** `_ch_witness_key` matches on `e.subject`, and the fold sets `Event.subject` **to
the actor** — `T-d` honoured in a field name and violated in mechanism (`01_AXIOMS.md`, `T-d`).
So today a knot to the clerk delivers *events the clerk caused*; after `W24` makes `subject` the
changed object, it will deliver *events that happened to the clerk*. **Those are different levers**,
and the second is the one this position wants. Building on the first is building on a scheduled repair.

**⭐ SO THE PLAY IS: `tie / knot` THE CLERK, THE SEASON BEFORE.** `tie / knot` is a rostered tenure
kind (`rosters.yaml:84-87`) with its own witness channel and no reader in this design. Knot yourself
to a person who will be in the closed room, and you learn what happens to them there — **without
travelling, without being admitted, and without anybody choosing to tell you.** That is the one
information lever in the design that does not run through another character's decision, and therefore
the one that is **not blocked on `H-72`** — for a **player**, who is their own decision procedure
(`07` PART D). For an NPC, learning still reaches no choice, so the knot makes the world legible to
the player and does not yet make NPCs act on what they overhear.

**And it corrects the catalogue rather than the schema.** The six closed-floor rows do not make
descent free. They make it *cheap now and expensive later*, which is the study's own **▣ bounded in
time** (Fig. 3): *"low standing suppresses reception now and does not reliably suppress it later."*

**(iii) THE COST.** Zero of everything — no carrier, field, verb, key, term or magnitude. ⚠ **One
dependency named:** the `witness_key` predicate is `H-33`, graded `assumption` with **total fan-out as
the default and the control**. Under total fan-out this lever is indistinguishable from doing nothing,
because everyone already learns everything. **So the position is real only once `H-33` is specified,
and it is an argument FOR specifying it.**

**(iv) THE PRECEDENT.** **CK3's *secret*** — a fact you hold that they do not know you hold.
**What changed:** in CK3 you spend the secret with a button. Here the holder-side act is a non-owner
write (`T-m`, `R-10`, the audit's §3.4 row 1), so what you can do with what the knot tells you is
`tell` it, or hold it — which is slower, more political, and less satisfying. **I am not claiming
otherwise.**

**(v) THE FALSIFIER.** Seeded run of the excommunication row (`floor: closed`, three terminal stakes).
Actor X is not admitted and does not travel; X holds a live `knot` to bench member Y. Require: after
the descent, X's ledger holds a claim about it, sourced `firsthand_via_knot`; a control actor Z with
no knot and no record holds **nothing**; and the record-holder holds *that it changed* and **not who
changed it**. *Shows it wrong:* Z learns it anyway (total fan-out is still the arm, and the position is
inert); or X learns the attribution as well as the change (the channel is over-delivering and `T-d` is
leaking further than known).

**(vi) MY STRONGEST OBJECTION.** **I have converted a sharp finding into a defence of the status quo,
and that is the move an author makes when they do not want to change a catalogue.** `P-41` says the
core tactical decision is cheapest exactly where the stakes are terminal. Saying "ah, but the price
arrives next season through a chronicle at somebody else's confidence" **concedes that the decision is
cheap at the moment it is taken**, which is the moment the player takes it. A stronger position would
change the six rows' floors and pay for it. I did not, and I am not confident that was right.

---

## POSITION 12 · [A] `verdict_reasons` is a channel setting, not a switch on learning

**(i) THE CLAIM.** The key cannot gate learning and does not: a bench member holds the reasons as
claims and `tell` is `eligibility: own`, so **any bench member can always leak** — what the key
actually sets is whether the determination's reads fan out *without anyone choosing to*, which makes
the leak a move and `interview` of a bench member worth a scene.

**(ii) THE MECHANISM.**

```
verdict_reasons: given     →  the determination's Event.observed deposits at TOTAL fan-out
verdict_reasons: withheld  →  it deposits to the DETERMINER ALONE (mode `actor`)
   -- both are existing values of `observation_deposit_modes` (rosters.yaml:305-345)
   -- Event.observed already carries "what the fold read to reach this Event" (shape.py:2118-2136)

In BOTH arms:  a bench member may `tell` what they hold.  `withheld` does not stop them.
               It only means somebody has to ACT for the room to learn — and be witnessed doing it.
```

Fig. 13's three columns stop collapsing to one boolean (`P-38`), because *learning why* now has three
distinguishable routes — fanned out, told by a member who chose to, or bought with an `interview` at
the price of a turn in front of everybody.

**(iii) THE COST.** Carriers 0 · fields 0 · verbs 0 · Event kinds 0 · keys 0 · obstacle terms 0 ·
hidden magnitudes 0. ⚠ **One real cost, and it is a process cost:** it turns `observation_deposit_modes`
from a **global sweep arm** (`H-122`, whose control arm `none` is the current behaviour) into a
**per-arrangement datum**, which pre-empts a measurement that has not been run. The sweep can still
run with the row values as its arm, but it is no longer the clean three-arm comparison `H-122`
designed.

**(iv) THE PRECEDENT.** **Tyranny's Edicts and its per-faction verdicts** — the same ruling is a
different fact to each party. **What changed:** Tyranny's factions receive an authored variant; here
the variation is a *channel*, so the difference is in who was reached and through what, not in what
was written for them.

**(v) THE FALSIFIER.** Two seeded determinations, identical but for `verdict_reasons`. Require: under
`given`, every attendee's ledger carries the `Observation` triple; under `withheld`, only the
determiner's does — **and in both arms a subsequent `tell` by a bench member deposits it into the
teller's audience**, with the telling itself witnessed. *Shows it wrong:* `withheld` prevents the
`tell` (the key has become a gate on a verb, which no key may be); or `given` and `withheld` produce
identical ledgers (the key is inert).

**(vi) MY STRONGEST OBJECTION.** **This is the position I am least sure is even mechanically
available**, and it is the one to attack first on facts rather than on design. `Event.observed`'s own
comment says the common case is `()` — *"a verb on `REQUIRES_PREDICATES` reads the world through a
hand-written predicate that records nothing"* — so `determine`'s reads may not reach `observed` at all
until it is typed, and `determine`'s typing is blocked on `P-03` (`Act` has no `via`). **If `observed`
is empty for `determine`, both arms of this position deposit nothing and the whole thing is prose.**

---

## POSITION 13 · [A] Two keys are deleted, and the deletion IS the gradient

**(i) THE CLAIM.** `registers[]` and `stakes_grade` are binaries that convert by removal, not by
grading: the first is a second home for an obstacle term that already exists, the second is a summary
of something derivable — and deleting both takes the arrangement from fourteen keys to twelve while
making the design *more* graded, not less.

**(ii) THE MECHANISM.**

```
⛔ registers: [ <subset of seven> ]      -- DELETED.  ID-2: a second home.
   `register fit` is ALREADY obstacle term 4 (06:220) — "which misreading this manner invites,
   before this room". The set turns a gradient into an in-or-out. And the roster does not exist
   in data at all: `grep -n "registers" rosters.yaml` returns ONE hit — line 238, the English
   verb inside a note about `H-76` — and no roster key. There is nothing to delete but a promise. What replaces it: Fig. 8's 7→7 misreading map as the term's weight family,
   applied as A RISK THE MANNER RUNS rather than a lookup of what occurred (P-39).

⛔ stakes_grade: terminal | costly | free  -- DELETED.  The proposal's own P-09, and ID-13.
   The stake IS what `disposes` writes, with terminal/costly/free falling out of whether that
   write is closable by some act. A grade is a summary of a fact the row already carries.
```

**Five of the twelve rows carry `registers: [restricted]` and three carry `[all seven]` — a set-valued
key used, in eight of eleven live rows, as a removal.** That is the census's own signature of a key
that wants to be a term.

**(iii) THE COST.** **Negative.** Arrangement keys **14 → 12**. Carriers 0 · fields 0 · verbs 0 ·
Event kinds 0 · obstacle terms 0 · **hidden magnitudes 0** (term 4's weight family already needed
magnitudes; this does not add one). ⚠ **What it costs in content:** the Fig. 8 map has to be authored
as data — seven manners × seven readings — and `P-07`'s question (*does anything break if the roster's
membership changes?*) becomes answerable by running the design's own falsifier: **change the roster's
membership and see what breaks.**

**(iv) THE PRECEDENT.** **Fallen London, inverted.** Fallen London gates storylets on qualities;
`R-9` and `rosters.yaml:131-142` refuse eligibility-by-stat by name and the loader raises. Deleting
`registers` is refusing the same shape one level up: **a manner is never unavailable, it is only
badly received.** That is `§A.2` — *"`if skill < N: return []` deletes the best thing about the option
set"* — applied to a data key instead of to a body.

**(v) THE FALSIFIER.** Load the twelve rows with both keys removed and require: **all twelve load**;
a thirteenth (the examination, `03` §F.1) loads with no code change; **a fifteenth key fails the load
naming the row**; and the closure scan is red on a planted `if arrangement.id == "tribunal"`. Then run
one hearing per register at a fixed seed and require **seven different obstacles**. *Shows it wrong:*
any of the twelve rows becomes indistinguishable from another once the keys are gone — which would
mean the keys were separating something after all, and `03` §E.1's *"six keys do the separating"*
claim needs a sixth and seventh.

**(vi) MY STRONGEST OBJECTION.** **Deleting a key is not converting a binary; it is declining to
answer.** `registers: [restricted]` in the interrogation row is doing real fictional work — *the
subject does not choose their manner* — and moving that into an obstacle term means the subject
*may* choose a forbidden manner and merely pay for it. **In an interrogation, "you may speak however
you like, at a price" is arguably the wrong fiction**, and this is the one place in the catalogue
where I think a refusal might genuinely be right and I have converted it anyway.

---

# THE BINARIES I DO **NOT** CONVERT — where the forbidding is the game

**A design that converts every binary has stopped having a shape.** Each row names what would be lost.

| # | the binary | why the refusal IS the mechanism |
|---|---|---|
| **B-7** `appeal_basis: none` | ⭐ **The worked case, and the orchestrator names it correctly.** *No appeal is what arbitration IS* (`03:479`). Grade it and arbitration becomes a slow trial, and the real game — *"a player who wins the choice of arbiter has usually won"* (`07:256`) — evaporates, because choosing the arbiter only matters when the choice is final. **Position 2 grades what a finding COSTS, which is orthogonal, and leaves the key alone.** |
| **B-6** `disposal: bench \| mutual \| none` | A multilateral disposal is a **tally across holders** — `T-a`, `R-1`. The lawful cousin (a later act reads a Query and declares) is **a different game in which one person decides**, not a gradient of this one. What is lost is real and should be stated as a coverage bound: conclaves, votes, majority verdicts, five-party peace (`P-15`, regraded at `14:92-95`). |
| **B-18** you cannot make anyone a party | `AX-1`. Every route into the room is first-person and **must be**. A second-person lever is the difference between a world of people and a puppet show, and the design's whole claim is the former. The lawful shape is the provocation — weaker on purpose, and **Position 8** says exactly how much of it works. |
| **B-19** the creditor has no verb | `T-m`: closure is ownership. A `call_in(hook)` is a non-owner write (`R-10`) and costs an **amendment to a theorem**, not a row. ⭐ **And `P-36` is the same ruling from the other end** — *forgiveness is currently inexpressible* — so the two halves should be ruled together or not at all. What survives: publicity (`tell` that the debt exists) and mercy (a counter-`oblige`). A CK3 player will feel this as *"my hook does nothing"*, and they will be right. |
| **B-9** `term_required: false` | ⭐ *"The whole horror of it, and it is one boolean"* (`03:530`) is correct as fiction: **authored indefiniteness**, lawful under `AX-6`, and playable only because whoever set it can be reached (`T-c`). Not expressible as a gradient today in any case — `Tenure` has no `term` (`P-04`). Once built, the gradient is *how far away the closer is*, which is `T-c`'s handles, not a bool. |
| **B-11** whose `Person.stance` | Not a binary to convert — **an `AX-4` ambiguity to close.** Position 3 closes it: the actor's own. |
| **R-18** never show a number | Not a binary. The one exception is **Position 4's named level**, which `R-18` explicitly permits and which is the only number any position here shows. |

---

# RANK, BUILD ORDER, AND THE TWO COUNTS

## Ranked by how much they change the play

| rank | position | what changes |
|---|---|---|
| **1** | **P1 · aptness is reception** | every turn of every proceeding; the design's headline binary; the one it *defends* rather than asserts |
| **2** | **P3 · Partial costs** | the shape of every exchange; the middle band stops being empty |
| **3** | **P4 · the σ-bargain** | gives the player a lever that is theirs, and the only legible number in the game |
| **4** | **P2 · the graded finding** | what *winning* means, and whether an appeal is worth opening |
| **5** | **P5 · the ladder is two-way** | the descent stops being a ratchet you turn alone |
| **6** | **P6 · the terms are a document** | opens a whole season-scale game on the venue format; sources `H-87` |
| **7** | **P8 · proof against a statement** | makes producing evidence a targeted act instead of a counter |
| **8** | **P10 · licence → four terms** | four named failures stop being received identically |
| **9** | **P7 · the advocate's rope** | presence becomes a gradient and deposits a seizable object |
| **10** | **P9 · silence priced** | gives `order` a second job and makes not-acting a decision |
| **11** | **P13 · two keys deleted** | −2 keys; a manner becomes a risk instead of a permission |
| **12** | **P11 · the deferred price** | corrects a reading of the catalogue; unlocks `knot` |
| **13** | **P12 · reasons as a channel** | makes the leak a move — **if `observed` is non-empty, which is unproven** |

## The three I would build first, and where they land

⭐ **P1 + P3 + P5, as one commit, at build steps 0 and 6.**

They are the same two rows and the same fold. Step 0 delivers *"the composed obstacle and the injected
magnitudes"*; step 6 delivers *"`speak` with its `requires` and its four bands"*. Between them these
three convert **five** of the twenty binaries (`B-1`, `B-13`, `B-11`, `B-14`, and `B-3` by
consequence) for **two new obstacle terms, three new magnitudes and zero primitives**, and they close
one `AX-4` ambiguity the proposal left open. **P5 is free and must ship with P1** — pushed to a rung
where your remaining moves would be *refused* is a stun-lock; pushed to a rung where they are
*expensive* is a game.

**Their shared falsifier harness is one seeded run with four planted margins**, which is also step 9's
bar (*one seeded proceeding end to end, twice, byte-identical including the hash*). So the three
positions and the milestone's own execution artifact are the same instrument.

**Next, and separable:** **P6** at step 2 (it needs only the loader and it sources `max_depth`, which
today is invented), then **P2** at step 7 (it needs `determine`, which is blocked on `P-03` for the
`via` conjunct but **not** for the degree write).

## What I could not make lawful, and what each would cost

| wanted | refused by | cost of having it |
|---|---|---|
| **CK3's hook, spent by its holder** | `T-m` · `AX-4` · `R-10` | **an amendment to a theorem**, not a row. Rule it with `P-36` (forgiveness) or leave both. |
| **a multilateral settlement** | `T-a` · `R-1` | breaking `T-a` for one case. ⚠ The audit's `T-h` reading — *a treaty everyone joined is a faction* — is worth Jordan's attention and **I could not certify it**: `T-h` carries its own retraction about a memberless faction leaving territory held by a banner nobody carries. |
| **the provocation's payoff** | `H-72`, **measured** | nothing here. 0 of 4,800 claims can fire. Every create-then-seize lever running through another character's *decision* is half-built until that lane closes it, and **saying so is the honest state of Jordan's second requirement.** |
| **`Record.stages` as the ORDER** | `R-14`'s letter (`08:88-91`) | a ruling. **I routed around it** — Position 6 reads everything but the order — so the venue's *terms* are seizable and its *sequence* is not. |
| **`Tenure.payload` as a carrier** | not refused — **declined** | `write_matrix.yaml:53`: it is REPLACED by `term?` under `#358` rev.2 §B.8. A reader built on it dies at the migration. Position 7 uses an immutable `Proposition` instead. |
| **a debate score, a momentum bar, a vote count** | `T-a` · `R-1` | the whole politics layer. Not wanted. |
| **a percentage, a band preview, the obstacle** | `AX-2` · `R-18` | a solved proceeding, whatever the resolver does. |
| **the room remembering your silence** | `AX-1` | an Event for a non-act. Position 9 takes the shallow half and says so. |

## ⭐ THE TWO COUNTS, STATED PLAINLY BECAUSE THEY WILL BE ATTACKED

### New primitives: **ZERO.**

**0 carriers · 0 edge kinds · 0 verb names · 0 fields · 0 Event kinds.** Every demotion, held speech,
compromise and refusal emits a kind the proposal already declares, and every reading rides in
`Event.observed`, which exists.

**What is added that is not a primitive, itemised so the antagonist need not dig:**

| addition | kind | net |
|---|---|---|
| `UnlicensedFrankness(BandExtension)` | one declared engine-side policy class | **+1**, and it **deletes** the seam's `veto: bool` — the seam signature gets shorter and `T-k` regains a single owner |
| `speech_kinds` with `apt_genre` / `apt_rung` | data roster the design already promised and never authored | **+1 roster**, `ID-12` content |
| Fig. 8's misreading map + Fig. 26's four readings | data | **+1 roster**, content |
| finding-strength bands (P2) | data | **+1 roster**, content |
| `Tenure.degree` · `Record.stages` · `Claim.confidence` | **fields given readers** | **+3 `ID-13` closures**; `Tenure.payload` declined on the record |
| arrangement keys | `registers`, `stakes_grade` deleted | **14 → 12** |

### New hidden magnitudes: **TEN**, taking the obstacle from **five terms to twelve** (thirteen in a nested appeal).

| term | # | magnitudes | position |
|---|---|---|---|
| latitude · reception · rung · register fit · proofs told | 1–5 | existing | proposal |
| **aptness** | 6 | `MISMATCH`, `STEP` — **2** | P1 |
| **partials so far** | 7 | `HELD_STEP` — **1** | P3 |
| **called and silent** | 8 | `PASS_STEP` — **1** | P9 |
| **licence: goodwill · privacy · repetition · stake** | 9–12 | **4** | P10 |
| **prior finding's strength** *(nested appeal only)* | 13 | **1** | P2 |
| *(term 5's weight function)* | — | `DIRECT : INDIRECT` — **1** | P8 |

**Plus one VISIBLE magnitude** — which offer buys which named σ-level (P4). It is the only number any
of this shows the player, and `R-18` permits it by name.

**Every one is `assumption`-grade: inject, declare, sweep** (`ID-6`). **Injection site: the obstacle
composition in `proceedings.run`, build step 0** — one function, one place, no second home.
**Sweep: pools {1, 4, 9, 16}**, which is `P-27`'s own falsifier, because `Δz = X/(0.8·√pool)` means
every one of these matters more to a weak speaker than a strong one.

**⚠ AND THE TWELVE-TERM OBSTACLE IS THE THING TO ATTACK, NOT THE PRIMITIVE COUNT.** The audit
predicted *"up to 12"* independently and called it *"the real cost, and it is an audit surface (`R-18`),
not a schema"*. I reached twelve from the other end, which is corroboration and not comfort. **The
defence:** the twelve compose into one number nobody sees; the sum is non-stationary because
`reception` moves without the player's knowledge (`15` PART C.1); and each term is separately
sweepable. **The attack I would make on myself:** twelve terms is twelve places a port can leak, one
`eff_ob` call from being displayed; and a patient player with forty seasons of observations can
estimate eleven of the twelve, because eleven are properties of the room and of their own hand.
**Only `reception` is genuinely hidden. If `reception` is ever weak, the whole obstacle is legible and
`15` PART A's solver comes back.**

---

## THE RESIDUE, SAID ONCE

**These thirteen make the room GRADED. They do not make it GENERATIVE.** Six of them
(`P6`, `P7`, `P8`, `P9`, `P11`, and the seizure half of Thesis B) are the "create then seize" surface,
and **five of the six run on the venue, on your own prior acts, or on edges the other party already
committed** — deliberately, because the sixth route, through another character's *decision*, is
measured-severed at `H-72`. **The honest first act toward Jordan's second requirement is closing that
edge, and it is not this subsystem's lane.** Everything above is what can be built without it.
