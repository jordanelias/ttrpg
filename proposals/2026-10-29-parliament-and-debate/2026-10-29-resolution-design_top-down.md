# Resolution design — the top-down designer's contracts (reference input to the handshake)

## Status: **REFERENCE (2026-10-29).** Written independently of the bottom-up design, from purposes and Layer 1 downward; **superseded wherever `2026-10-29-resolution-design.md` differs** (that file records the handshake and the second round of attack). Kept because the resolution design cites its acceptance properties AP-1..AP-9, its invariants and its contracts I1..I12. Verdicts of fit are in the adjudication; none of this is a plan.



---

# TOP-DOWN DESIGN — parliament and debate, derived from purposes and Layer 1

Contracts derived downward from the three goals, `01_AXIOMS.md` and `04_CODE_ARCHITECTURE.md`; no code edits.
A primitive I EXPECT to serve is for the bottom-up designer to verify. Opened to confirm: `verb_table.yaml`
`issue` (remit:issue, mints a Record addressed `to` an executor), `comply` (emission-only; the writ's named act
performs), `evade / defy` (emits `compliance.withheld`; untyped, 0 computed executions), `seize` (remit:issue,
purview, warrant reading), `speak` (writes `[]`, H-63); Layer 1: `Seat.remit(acts[], binds)` (§B.7), AX-7's scope
clause (*a remit, an office, an eligibility is held with certainty*, 01 :292-297), the gate's bases (§C.2).

---

## 1. ACCEPTANCE PROPERTIES

Properties of a PLAYED world (seeded runs of `engine/season/`). A control identical to its arm by
construction measures nothing (CLAUDE.md §7).

**AP-1 · Operands come from the world.** A motion's Proposition `{subject, predicate, value}` is uttered by a
person, and each operand id is one the utterer held a claim on at the moment of utterance, whose provenance
chain ends at a world Event (not at an authored string).
- *Falsifier:* walk every computed (not hand-built) motion's operands to the utterer's ledger; one operand with
  no claim, or a claim with no Event ancestry, falsifies.
- *Control:* a hand-built motion with a fabricated operand must be REFUSED at utterance/tabling (the
  `own_ledger` conjunct), not docketed.

**AP-2 · The outcome depends on the operands.** Two persons debate the same motion; members decide; the division
result is a function of what the motion says, not only of who moved it.
- *Falsifier:* same seed, same mover, same members; swap ONLY the `value` operand (40 grain → 25 grain; a ford →
  the capital). If no member's commit/decline changes in any of N seeds, outcome is operand-blind.
- *Control:* swap the value to one that touches no member's holdings, ties or pursuits → the division must NOT
  change. (This separates content-sensitivity from noise; without it a reader that perturbs on any change passes.)

**AP-3 · Debate moves THIS subject, in both directions.** Same seed, three arms: no speech; a won speech for; a
won speech against, to the same members. Commits to the motion move up / stay / move down.
- *Falsifier:* the three arms' counts are equal, or move the same direction.
- *Control A:* the same speeches on motion A leave the members' decisions on an unrelated motion B, docketed
  in the same sitting, unchanged (kills the present defect: a won `argue` moves turnout on every motion at once).
- *Control B:* a lost speech (Failure) moves nothing on the hearer's side, and still emits.

**AP-4 · A carried motion changes the world by a lawful path.** After a resolution, at least one gate write in a
later round/season has, in its `causes[]` chain, (i) the act of a PERSON other than the declarant who held the
resolution or a writ derived from it, and (ii) no write by the assembly itself.
- *Falsifier:* a world change whose nearest act-cause is `determine` on the council seat writing anything beyond
  its declared Record; or zero executor occasions formed for any carried motion across the corpus.
- *Control:* the same world with the motion defeated → that change does not occur via that chain.

**AP-5 · A defeated or ignored motion leaves a trace.** (a) A motion below its threshold when its declared term
matures is closed and the closing EMITS a witnessable event at the venue whose `causes[]` names the tabling act.
(b) A resolution an executor declines is declined BY AN ACT that emits (`compliance.withheld` or successor).
- *Falsifier:* a motion that leaves the docket, or a resolution that leaves play, with no event; or an executor
  who holds the writ for its whole term and emits nothing.
- *Control:* silence-beats-refusal table (§4) — the silent and the refusing executor must both emit, with
  DIFFERENT kinds.

**AP-6 · A parliament exists at each rung and differs by rung.** For each rung kind that has a holder (realm,
duchy, province where one is assembled, territory), a council seat exists or can be established; its joinable
pool, the motion kinds whose strain queries can hold at its scope, and the acts its executor's seat can reach
all differ with the rung.
- *Falsifier:* two sittings at different rung kinds that produce identical pools, motion kinds and executable
  acts; OR any difference produced by a `kind ==` branch on a literal (ID-7, §B.3) rather than by containment,
  scope and purview read from data.
- *Control:* two councils at the same rung kind in different places differ only in operands, never in shape.

**AP-7 · Opinion change alone is a real, legible outcome.** A sitting that carries nothing still alters a value
a LATER decision reads (a member's stance or pursuit on this subject; a claim about who argued what), and the
player can see why.
- *Falsifier (reality):* compare next-season decisions of present members against the no-sitting arm; identical
  for all → inert. *Falsifier (legibility):* `explain(p, v)` (§C.11) for the moved value returns no derivation
  naming the speech the member heard.
- *Control:* persons absent from the sitting show no change.

**AP-8 · Persons differ in risk and horizon, observably.** Two members identical except risk appetite (or
horizon) diverge on a motion whose consequence is uncertain (or lands ≥3 seasons out).
- *Falsifier:* no divergence across seeds. *Control:* a motion whose consequence is certain and lands this season
  → no divergence (else the trait is a flat bonus, NERS disqualifier 5).

**AP-9 · The world debates without the player (R-WORLD).** Over the seeded corpus with no played person, motions
are tabled, carried and lapsed at more than one rung.
- *Falsifier:* zero computed motions corpus-wide (every instance hand-built). *Control:* the hash: same seed,
  same `World.content_hash()`.

---

## 2. THE CONTRACTS, I1..I12

Format per seam: **IN / OUT / HOLDER & CHANNEL / WRITER / NEVER / DONE / ABOVE→BELOW.** "Above" is the
seam closer to the goal (the room, the world change); "below" is the substrate it stands on.

### I1 · World → topic
- **IN:** a strain (an existing resolver-side query: `vacancies`, `uncontrolled`, `hunger`, `at_war`,
  `restrained`, rival HOLDS) holding at the would-be mover's scope, PLUS claims in the mover's own ledger naming
  the operands.
- **OUT:** a Question whose referents include the OPERANDS (not only the party), ranking high enough to be
  answered; from it, an `utter` Candidate of an OUGHT Proposition.
- **HOLDER & CHANNEL:** the strain query raises the question (resolver-side, T-b: it changes what can be
  chosen); the decision reads only the mover's `PersonInterior` (T-f).
- **WRITER:** `utter` (creates an immutable Proposition; `utterer` on it, AX-6).
- **NEVER:** a motion with no uttering person (AX-1); an operand the mover holds no claim on; a per-motion or
  per-kind scoring table (ID-4 / scripting drift); a strain band producing the motion (T-b).
- **DONE:** a computed `utter` of an OUGHT whose operands pass AP-1, in a seeded run.
- **ABOVE→BELOW:** the room requires the question source to (a) carry the value operand as a typed referent
  and (b) not be permanently out-ranked by `need`. A motion kind is a DATA row (ID-12) naming its strain query
  and its executing verb, refused at load when either is missing.

### I2 · Topic → room
- **IN:** an uttered Proposition; a tabling act by a person entitled to table at the venue.
- **OUT:** a docket item whose IDENTITY IS THE PROPOSITION (not the party), at the council seat's venue,
  carrying a term declared by the tabling act.
- **HOLDER & CHANNEL:** the docket item is calendar matter at the venue rung (Rung owns `dates[]`, matter);
  members learn of it only by channel (I3).
- **WRITER:** the tabling act (`open_case`/`carry` through `slot_for`, or successor), ACTS class; its term's
  maturation closes the item in MATTER with `causes[] = term.declared_by` (the T-n shape, §B.8).
- **NEVER:** two items for one Proposition; one tally shared by every motion about a party; a lapse with no
  declared term (a fourth clock, T-c); a re-tabling inheriting commits (a re-tabling is a new Proposition).
- **DONE:** two motions about the same party docketed at once, tallied separately, each closed by its own term.
- **ABOVE→BELOW:** the division requires the item to expose the tabling tick (readable off the tabling act) so
  commits made before tabling are excluded.

### I3 · Summons and attendance
- **IN:** a `convene` (a wound Date, T-c handles: it can be bribed, delayed, killed) by the convener.
- **OUT:** each member holds a claim that a sitting exists, and can be co-located at the venue in a round of it.
- **HOLDER & CHANNEL:** what HAPPENED (a sitting called) is AX-7 territory — it must arrive by a channel
  (co-location, a held document, telling, post_remit). WHAT IS PERMITTED (that I may sit on this seat) is held
  with certainty (AX-7 scope clause) and needs no claim.
- **WRITER:** `convene`; the member's own `move` (attendance has a cost: the absent home).
- **NEVER:** minting the summons straight into the addressee's hand (Jordan, ED-IN-0292 (1)); teleporting a
  member to the venue; absence that is invisible when the member HELD a summons (a summons answered by nothing is
  silence-beats-refusal).
- **DONE:** a member not co-located at the venue at convening arrives at it, in computed play, because of a
  summons he holds.
- **ABOVE→BELOW:** the room requires that at least one channel which FORMS in computed play reaches every
  current member. Expected primitive: the convener `issue`s a dispensation (terms: attend) to each member, so
  `writs_held` stamps it and the member answers `comply` (then `move`) or `evade / defy` (emits). Second
  candidate: a `post_remit`-class channel declared for obligers of the seat. Bottom-up verifies which forms.

### I4 · Room → bench
- **IN:** live `oblige` edges to ONE council seat (AX §E.2.5: one seat, many holders); its single `hold` (the
  chair); the ruler's separate seat.
- **OUT:** two different Queries, never one: **(a) the DIVISION** — members whose commit to THIS Proposition is
  live and was made after tabling; **(b) the DECLARANT** — the chair, acting `via` the council seat.
- **HOLDER & CHANNEL:** both computed when read (T-a, ID-1). No stored roster, no stored count.
- **WRITER:** joining is the joiner's own `oblige` (own-eligible); leaving is his `release` (T-m).
- **NEVER:** the council seat's grant making its chair a judge of EVERY realm matter (the declarant's power is
  bounded to items docketed at this seat); a second owner of "who sits in judgment" (the judging set stays
  "seats whose remit covers the matter", §B.7 call 3 — the division is NOT a judging set); persons the seat
  SENTENCED counted as members; joining a council read as vassalage (the seat's `remit.binds` declares what an
  oblige to it binds — data, §B.7); a party who is a member making the motion unenactable.
- **DONE:** a motion against a sitting member is carried by a division of ≥2 members and refused at 1, and the
  King's own realm-wide `determine` is unchanged by the council's existence.
- **ABOVE→BELOW:** the declaration requires the division to be readable by the gate at RESOLVE as the same set
  the Query lists (one owner, AP falsifier 8 of the proposal).

### I5 · Speech → hearer
- **IN:** a speaker and hearer co-present at the venue during the sitting; the docketed Proposition.
- **OUT:** two kept-apart effects (AX-3): **(a) evidence** — HOLDS claims the speaker tells about the operands
  and their consequences land through WITNESS by channel, competence and prior (moves what is held TRUE);
  **(b) argument** — on a won contest, the hearer's held-right on THIS Proposition moves toward the speaker's
  side, which may be FOR or AGAINST (moves what is held RIGHT).
- **WRITER:** the speech act's effect, ACTS class, through the gate. WITNESS writes only claims (T-j).
- **NEVER:** a speech moving the hearer toward the speaker's whole pursuit profile; a win that moves every
  motion; argument moving a HOLDS claim or evidence moving a stance (AX-3); an unbounded step (see I12); an
  obstacle blind to the hearer's prior on this Proposition (a hostile room must be harder).
- **DONE:** AP-3 with both controls.
- **ABOVE→BELOW:** the vote requires that what the speech changed be readable by `choose` from the hearer's
  `PersonInterior` alone, keyed to the Proposition or its operands.

### I6 · Hearer → vote
- **IN:** the member's `PersonInterior` (pursuits, stance, ledger, own tenures, risk appetite, horizon); the
  Proposition's operands; the verb table's DECLARATIONS for the predicate's verb (which `choose` already receives,
  §C.3).
- **OUT:** an ACT in either direction: `commit` to the motion, `commit` to its contrary, or `release` of an
  earlier commit. Not committing is not a vote (it emits nothing).
- **WRITER:** the member's own act.
- **NEVER:** a voter reading the world, another person's ledger, or an aggregate (T-f, F8); a reader that names a
  motion kind, an entity or an outcome (scripting drift); a stored opinion-of-motion field.
- **DONE:** AP-2 and AP-8.
- **ABOVE→BELOW:** the declaration requires that a nay be countable, so a defeat is a count, not an absence.

### I7 · Vote → declaration
- **IN:** the division (I4a) at a moment the chair acts; the item's threshold (data on the arrangement row).
- **OUT:** `determine` admitted or refused, keyed to the Proposition.
- **WRITER:** the chair's `determine` `via` the council seat.
- **NEVER:** a counted division resolved by dice (§C.4's synthesis call: a contest is opened only where a row
  DECLARES a prize; a counted arm declares none); a below-threshold attempt retried forever with no end; the
  chair's refusal to call a carried division being silent.
- **DONE:** the same division declared twice on two seeds gives the same result; a chair who never declares a
  carried motion is visible when the item's term matures (the closing event carries the state of the count).
- **ABOVE→BELOW:** the document requires the declaration to name the Proposition, so the Record's terms are
  what members committed to, never the petition's text.

### I8 · Declaration → document
- **IN:** a carried declaration; or a matured term.
- **OUT:** carried → a `resolution` Record (held, givable, forgeable, burnable — §D.4) naming the Proposition,
  its operands and the executing seat; defeated → the item closes and emits; contrary carried → a resolution of
  the contrary.
- **WRITER:** `determine` writes `Record.exists` only; MATTER closes the item under its term.
- **NEVER:** a resolution with world effect of its own; a defeat with no event; a resolution that can never leave
  play (AX-6: it is a Record, so it can be destroyed by an act).
- **DONE:** AP-5(a) and the carried/defeated kinds differ.

### I9 · Document → executor
- **IN:** a held resolution.
- **OUT:** an occasion on the executor's candidate list, and an act in answer whichever way he goes.
- **HOLDER & CHANNEL:** the executor must HOLD the instrument (or a writ derived from it) — the warrant reading
  is of the actor's own held Record (CR-36/37 precedent; F8 carve-out); never the gate reading a Record.
- **WRITER:** the transfer act (`give` of the Record, or `issue` of a dispensation `to` the executor); the
  answer (`comply` + the named act, or `evade / defy`).
- **NEVER:** minting into the executor's hand; an executor who can ignore a held writ by not acting and leave no
  trace (silence beats refusal); a term-less writ that is an occasion forever.
- **DONE:** a computed `comply` or `evade / defy` on a writ derived from a resolution, in a seeded run.

### I10 · Executor act → world
- **IN:** the executor's ordinary verb (`confer`, `revoke`, `give`, `transfer`, `requisition`, `seize`,
  `covenant`), admitted under its own conditions; where the arrangement declares CONSENT REQUIRED, the extra
  conjunct *the actor holds a live resolution naming this object*.
- **OUT:** gate writes under an existing basis; `causes[]` includes the writ/resolution occasion.
- **NEVER:** a "parliament" gate basis; the assembly writing land, assets or seats; the consent discriminator in
  an effect body (it lives at a data owner — a hold-kind or rung-kind row).
- **DONE:** AP-4.

### I11 · World → witness → memory
- **IN:** every Event of the chain (tabling, speeches, commits, declaration, writ, answer, execution, lapse).
- **OUT:** per-witness claims by channel (§C.6); attribution only where the channel carries it; reputation via
  the deed reader.
- **NEVER:** a stored division record or tally (anyone who wants the count reconstructs it from the commits he
  witnessed — and may be wrong, which is play); a deposit of engine truth (AX-7); WITNESS writing a stance (T-j).
- **DONE:** a non-present person later holds a (possibly wrong) claim about how a named member voted, via telling.

### I12 · Stability, the player, scarcity — contract in §4 (loops bounded and signed, ID-16; no dominant act
at a playable seat; attending costs something; every sitting ends).

---

## 3. THE ROOT PROBLEMS — the principle each repair must have

### R1 · Consequence-blindness (and risk and horizon, the same hole)
**Principle.** A content-sensitive reader is lawful iff it is ONE general function of three things the chooser
already receives — the Proposition's typed operands, the verb table's DECLARED writes for the predicate's verb
(§C.3: `choose` receives the table's declarations), and the voter's own `PersonInterior` — and names no motion
kind, entity or outcome. Such a function is a reading of the act grammar; a table keyed by motion is a script.

**What "a representation of consequences" minimally is** — a value computed inside `choose` and discarded
(per-person, per-decision: not an aggregate, not a field, so T-a and ID-1 are not engaged):

    Consequence = ( write   : (kind, field) from the predicate verb's declared writes, per degree where keyed
                  , object  : the operand id the write lands on
                  , mine    : how the object relates to ME, read from my own tenures / ties / commits / claims
                              (unknown -> neutral, never an oracle: AX-2)
                  , sign    : whether that write on that relation advances or harms my pursuits
                  , size    : the value operand relative to my own claimed holding of that kind (40 of my 100)
                  , lands   : the earliest season the write can occur = the chain's declared lags (term to
                              maturity, then the executor's act) - read off declarations, not simulated
                  , p       : believed odds of that band (CR-17's term) )

Risk appetite is a person's curvature over `p`; horizon is a weight over `lands` in Jordan's ruled bands
(short ≤ s+1, medium 3-4, long ≥5). **Both are held fields on `Person`** (AX-4: the person owns them; written
at world build; any later writer needs a matrix row). That is a schema-text update to §B.2's field list, not an
axiom change — flagged, not assumed free.

**Options.** (a) *the projection above* — general, reads the value operand, makes risk/horizon expressible; cost:
the largest reader in the chooser. (b) *`pursuit_lean` over the predicate verb* — cheaper, already sketched, but
blind one level down (40 vs 25 score the same): fails AP-2's falsifier by construction. (c) *stance rows naming
each fresh Proposition* — scripting drift; refused. **The architecture settles (a) over (c); AP-2 settles (a)
over (b), which cannot pass it.** Whether risk/horizon land now or wait on CR-17 is sequencing, not Jordan's:
the `p` slot can be a constant until CR-17 lands, with AP-8 stated as a limit meanwhile.

### R2 · Information does not reach the members
**Principle.** Split by AX-7's own scope clause. *What is permitted* — that a council seat exists and I am
eligible to join it — is a standing permission, held with certainty, and needs NO ledger claim; requiring one
(`oblige` forms only on a seat my ledger names) is stricter than Layer 1 and is the M-2 defect. *What happened* —
a motion tabled, a sitting called, a member's vote — must arrive by a declared channel and be a claim in the
holder's ledger, and at least one such channel must FORM in computed play for every current member, without
minting into his hand. Candidates, in order of expected cost: the convener `issue`s a summons writ to each member
(rides `writs_held`; the answer is `comply`/`evade / defy`, so absence is an act); a seat channel for obligers of
the council seat (the `post_remit` / `SEAT_CHANNEL` precedent: `inferred`, place-bounded); plain tellings (S-DOWN's
ideal — published, distorting — but too slow to be the only carrier of a dated summons). The sitting question's
referents must include the motion, and its rank must be a stamped occasion, not tier 4.

### R3 / R7 · How an assembly causes change under "only persons act"
**Principle.** An assembly never writes; it changes **what persons can and must choose** (T-b) by minting a held
instrument. "Cause" therefore means: a resolution creates an occasion that a named person must answer by an act,
and both answers emit. Six lawful shapes, none needing a new gate basis:

| shape | how change happens | NERS | emergent narrative | decided by |
|---|---|---|---|---|
| **α licence** (T3a) | the ruler's own `confer`/`revoke`/`give` is admitted only, or additionally, while he holds a resolution naming the object | E high; R-world thin — a body that only ever enables | the King who sits on a carried resolution; the held record cited later | architecture (CR-36/37 already) |
| **β writ** | carrying licenses the chair to `issue` a dispensation `to` the executor; executor `comply` + the named act, or `evade / defy` | S high (reuses the writ machinery); R high | defiance is an act → censure motions, warrants, rebellion; the writ can be stolen, burned, forged | **JORDAN** — gives the council seat `remit:issue` bounded to resolutions: a real transfer of power (H-90) |
| **γ warrant** | the resolution licenses a third person's `seize`/`arrest` against the party | R-world very high; R-choice risk: legal expropriation can dominate war | civil war, legal theft, a tyrannous majority | **JORDAN** — coercive power for a body |
| **δ members' own acts** | members committed to the carried OUGHT act on it with their own means; the commit edges ARE a faction (T-h) | E highest — zero new power; R-world good | a parliament breeds factions: motion → coalition → war | architecture (free) |
| **ε election arm** | `determine` fills a vacant seat whose conferral is `determine` (CR-35 arm, §C.2) | already lawful | contested successions, regencies | architecture |
| **ζ opinion only** | AP-7 | carries goal (3)'s "even if only opinion" | slow drift of a court | architecture |

**Recommendation:** δ + ε + ζ always, α as the base on every executing seat; β and γ are live design choices that
change who rules (H-90's *"no monopoly of power in the ruler"* argues for β; the adjudication argues T3b gives the
assembly that monopoly). **R7, stated plainly:** parliament's causal power is carried by its members' and
executors' own acts and by the occasions its instruments create; under α/δ/ε/ζ alone it can restrain, coordinate
and fill seats, but cannot compel.

### R4 · Motion identity and lifecycle
**Principle.** The Proposition is the motion's identity (immutable, uttered by a named person — exactly what a
docket key needs). Tally, docket item and resolution all key on it. Every end is authored: the tabling act
declares a term; MATTER closes the item at maturity with `causes[] = term.declared_by` (T-n; needs a MATTER cell in
`write_matrix.yaml`) and emits. **A nay is an act:** the opposer utters the CONTRARY OUGHT and members `commit` to
it — no new verb, and a defeat becomes a count. Commits count only if made after tabling by current members; a
member changes his vote by `release` (a witnessed vow-break).

### R5 · The body and the bench
**Principle: who DECLARES and who COUNTS are two Queries with two owners, and neither widens the judging set.**
- The chair's `determine` via the council seat is admitted only on items docketed AT that seat, under the declared
  arm; the council seat must not enter benches elsewhere (no `bench.size` hash mover). Bottom-up decides whether
  that is a conjunct or a remit narrowing; either is data plus one conjunct.
- The division counts own-made `oblige`s only (an imposed `oblige` — a sentence — is not membership).
- Joining is not vassalage: the seat's `remit.binds` declares it. The tree carries a `binds` roster with
  `members_by_admission` as a default (`state/carriers.py:917`) — verify it is the basis `predicates.py:380` foresaw.
- Membership term: renewal only by the chair's purse makes the chair own the roster (patron capture). Options:
  (i) council obliges carry no term (leave by `release` or death); (ii) the member renews his own term by attending;
  (iii) keep the purse as content. **(ii) is my pick on R-CHOICE grounds (it prices abstention). It is JORDAN's
  only if he wants seat patronage as a designed lever**; otherwise AX-6/ID-14 settle for (i) or (ii).
- A party need not be present or a member: under the declared arm the object is the Proposition; the party is an
  operand. This removes A1-M3 and A2-P-9's refusals for council motions without touching `may_determine` elsewhere.
- The King's realm-wide `determine` stays (a portrait, lawful); whether the council restrains him is β / H-90.

### R6 · Reach and unread keys
**Principle: ID-13 — every arrangement key gets a reader in this work or is deleted in it.** Reach is not a
parliament property: it is the purview of the seat the EXECUTOR exercises (`Act.via`, §B.7). A territory council's
resolution reaches what its lord's seat reaches, by construction, so `venue_min_rank` and `disposal_reach` are
redundant with purview and should be deleted rather than read. `disposal` (bench | declared | mutual) is the one key
this design needs a runtime reader for. The declared arm does not roll (§C.4: no declared prize, no contest) —
settled by architecture, not by taste.

### R8 · Stability, legibility, the player — §4.

### R9 · Verdict corrections
Accepted. Consequences here: sortition later, as the convener's own act over obligers; non-reply and
self-contradiction are evaluable from held claims (a future speech-quality input, not v1); weighted votes only as
a weight computed when read (precedent `legitimacy`), out of v1.

---

## 4. A SITTING AS A GAME

### 4.1 What the player sees (AX-7: nothing hidden from the PLAYER; the character's option set narrows)
The docket at the venue (each item: the Proposition with operands, its mover, its term); the members the
character KNOWS of and what he holds about their past votes (claims, possibly wrong); for each own option, the
`explain()` derivation (§C.11) of its score — including §R1's projection **over the character's own holdings
only**: "this cession costs my duchy 40 grain within 2 seasons, at odds as I believe them." Not the count. Room
legibility without a GM is the arithmetic of the character's own claims, so a character who skipped the last
sitting reads an older room — that gap is play.

### 4.2 The menu (existing verbs only)
**Move** a motion (`utter`, table if entitled) · **oppose** (`utter` the contrary) · **speak / argue** for or
against, to the room or one member · **tell** a consequence (evidence) · **commit / release** · **bargain**
outside the room (`covenant`, `give`, `exchange`) · **attend or not** (`move`; answer the summons with
`comply` or `evade / defy`) · after the vote, **burn, forge, steal or seize** the resolution.

### 4.3 Scarcity
One decision per round, `scene_budget` rounds a season; a sitting is a convened, dated window at one place, so at
most one per seat per season by the convener's act, and one venue per person per round. Attending costs rounds and
an unattended home; a member cannot argue to a room he is not in. Term lengths and thresholds are
`[OPEN — Jordan tuning]`. **R-CHOICE depends on the act economy (NERS §6.3):** under multi-act-per-round readings,
petition-spray dominates; this table assumes one act per round.

### 4.4 R-CHOICE — dominance at the three seats (upper bounds, not estimates)

| seat · intent | act | gain | cost | dominance → required bound |
|---|---|---|---|---|
| **proposer** · carry M | table & argue | M carried, his name on it | rounds; witnessed advocacy | — |
| | table & buy votes (`give`) | votes | goods; a `give` | *shape mismatch* if the gift is unwitnessed → `give` emits, attributable to the co-located |
| | (as chair) table only friendly motions | a room that always agrees | nothing | **strict** → any member may table; a chair's refusal to table or to call a division emits |
| **opposer** · M fails | argue against; contrary motion | M fails, record says why | rounds; a witnessed side | — |
| | stay away so quorum fails | M fails | **nothing, if silent** | **SILENCE BEATS REFUSAL** → threshold compares commits FOR vs AGAINST, not attendance; an unanswered summons emits at its term |
| | burn or steal the resolution | M nullified | a crime, witnessed or not | lawful churn (Record semantics), not a defect |
| **swing member** · best for self | commit by consequence | his interest | a witnessed vow | — |
| | sell the vote | goods | witnessed `give`; a vow later broken | bounded only while `release` costs reputation |
| | never vote | no exposure | nothing | **dominant if voting costs and abstaining is free** → membership renewed by attending (§R5 ii) |

**Loops (ID-16: each a signed `LOOP` row with its falsifier over N seasons):**
- **L1 judge self-reinforcement (+)**, `consequence_pursuits` unclamped. Bound: a saturating step (shrinks near the
  bound). No clock may decay a pursuit (AX-3). Falsifier: a judge ruling one way for 40 seasons stays inside it.
- **L2 convergence (− on variance)**, `argued_pursuits` pulls toward the arguer only. Bound: speech moves stance on
  THIS Proposition only, either direction, obstacle rising with the hearer's prior distance. Falsifier: pursuit
  variance over 40 seasons does not collapse against a no-speech arm.
- **L3 herding (+)**, social proof over regard. Bound: weighted below the member's own consequence term; reads only
  commits he witnessed. Falsifier: one early high-regard commit does not decide most divisions.
- **L4 always-agree (−)**. Bound: right of motion, contrary motions, emitting chair refusals. Falsifier: corpus share
  of unanimous divisions.
- **L5 patron capture (+)**, purse renewal. Bound: §R5 (i)/(ii). Falsifier: clients' alignment with the chair vs
  non-clients'.
- **L6 motion runaway (+)**, a carried motion feeds the strain that tables the next. Bound: re-tabling is a new
  Proposition with no inherited commits; each sitting costs the convener a Date.

---

## 5. INVARIANTS AS LAW (any bottom-up proposal is checked against these)

1. Every motion, vote, declaration and execution is a named person's act; no institution, faction, council,
   threshold or clock acts (**AX-1**, **T-h**).
2. `choose` reads only the actor's `PersonInterior` and the verb table's declarations; the fold reads only the
   actor's own ledger (**T-f**, **§B.2 F8**).
3. No stored tally, roster, division record, opinion-of-motion or "parliament mood" (**T-a**, **ID-1**, §B.3 NEVER).
4. Evidence moves HOLDS claims; argument and consequence move stance/pursuits; WITNESS writes no stance (**AX-3**, **T-j**).
5. No deposit of engine truth; what happened arrives by channel (**AX-7**); standing permissions need no claim
   (**AX-7 scope clause**).
6. Every end is authored: a docket term is declared by the tabling act; no fourth clock (**T-c**, **T-n**, §D.4).
7. Every open has a close: council `oblige`, `commit`, resolution, writ (**AX-6**, **ID-14**).
8. A threshold changes what may be chosen, never an outcome (**T-b**, **ID-17**).
9. Every refusal, defeat, lapse and declining emits — an act, or a matured authored term (**§C.4**; NERS §6).
10. A counted division is not a contest; a contest opens only where a row declares a prize (**§C.4**, **T-k**).
11. The gate applies every write under an existing basis; no "parliament" basis (**ID-9**, **§C.2**).
12. One council seat per body; membership a Query over own-made `oblige` (**AX §E.2.5**, **§B.7** call 2).
13. Purview is asked of the seat exercised; reach is never a parliament property (**§B.7**).
14. No per-motion, per-entity or per-rung branch; rungs differ by data and containment (**ID-4**, **ID-7**).
15. Motion kinds are a data roster refused at load without a strain query and an executing verb (**ID-12**, **ID-5**).
16. Every declared arrangement key reaches a reader or is deleted (**ID-13**).
17. Every feedback path is a signed `LOOP` row (**ID-16**).
18. A player character is shown the arithmetic of what the character holds, nothing more (**§C.11**).
19. Nothing is minted into an addressee's hand; delivery is an act (**ED-IN-0292 (1)**).
20. No new verb, no new entity type, no new gate basis; a remedy adding one must argue its N-line (NERS META-RULE).

---

## 6. MY WEAKEST POINTS

1. **The value operand may not be bindable.** H-94: a computed act binds `subject` and `to` to the question's ONE
   referent. A Proposition whose `value` the chooser can read may need an operand form beyond the closed eight —
   a grammar change. If so, AP-1/AP-2 demand something expensive.
2. **The consequence projection is the largest reader in the chooser** and assumes declarations say enough:
   many `writes` name a field, not an amount or a direction; `lands` assumes lags are declared, and most are not.
   Honest grade: expressible, not yet implementable.
3. **Risk/horizon fields extend §B.2's Person.** I call it a schema-text update; a strict reader may call it a
   Layer-1 amendment. Flagged for Jordan's eye, not assumed.
4. **Absence emitting** relies on a held summons with a term (T-n) closing with an event when unanswered. If the
   writ machinery cannot carry a term, absence stays free and "stay away" dominates the opposer seat.
5. **β is where goal (2) becomes strong, and it is Jordan's.** Under α/δ/ε/ζ alone, AP-4 against an unwilling ruler
   passes mostly through δ (members acting for themselves) — weaker than "the parliament decided".
6. **`evade / defy` has 0 computed executions and is untyped**; my contract leans on it for both the summons and the
   executor's refusal. If it cannot be made to form, every "declining is an act" clause is paper.
7. **AX-7's permission clause as the answer to M-2** is my reading of Layer 1; if the chooser's interior has no
   carrier for eligibilities, the bottom-up designer must add the read (a remit-like standing view), not a claim.
8. **Province:** the authored realm has no province rung, so AP-6 for province runs only on a world that
   assembles one.
