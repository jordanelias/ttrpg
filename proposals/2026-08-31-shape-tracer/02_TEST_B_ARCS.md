# TEST b:ARCS — can the arcs in `designs/arcs` be played out under the shape?

## Status: **PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge.**
## This test RAN. Same instrument, same tracer, same gap register as `01_TEST_A_NPC.md`.

> **THE TEST.** Take the arc corpus at `v30-snapshot-2026-06-28/designs/arcs`, extract from each arc
> **what the engine must be able to DO for that story to happen at all** — written by lanes blind to
> the shape — and run those requirements against PR #350's executing season loop.

**SCOPE AS RUN: 50 arcs.** The 18 of the `gm_ref` current series, the root series' arcs 16–19 and
20–45, and 2 cases from the emergent corpus. Together with a:NPC's 27 characters that is **78 cases
and 527 `season_requires` rows** driven through 65 probes. **The corpus is committed at
`cases/`** — it used to be read from a session scratchpad, which meant nothing here was
reproducible by anyone but the session that ran it.

---

## §1 · THE RESULT

| | |
|---|---|
| cases | **50 arcs** |
| verdict | **38 BLOCKED · 11 NOT-ASSESSED · 1 PLAYABLE** |
| top core blockers | `A2` threshold-ending (8) · `P34` hidden self-accumulation (7) · `P4` conviction motion (7) · `A5` unbounded spiral (5) · `P3` covert action (5) · `P26` accumulated harm (5) · `A4` provenance (4) · **`A13` ambient social drift (3)** |

**One arc runs.** `ARC-06`, *The Debate That Won the Wrong Thing* — and it runs because its subject
is the one thing the shape gets right for free (§4).

⚠ **`NOT-ASSESSED` is not a soft PLAYABLE.** It means more than half that arc's `core` needs did not
route onto any probe, so **the test did not aim at it**. Ten arcs are in that state and they are
reported untested rather than graded. Case verdicts are advisory throughout; **the probe verdicts
and the blocker attribution are the hard result**, because each is an execution.

---

## §2 · THE HEADLINE — how these stories END

This is the most valuable single distribution the test produced, because it is the exact axis
PR #350's Law 1 cuts along. Each arc's lane recorded `ends_when` independently, with no knowledge
of the shape; the classification below was made by a separate pass that saw only those strings.

| how the arc closes | count | what Law 1 says |
|---|---|---|
| **a person chooses** — an officer, a tribunal, a vote, the players | **20** | ✅ exactly what the shape is built for |
| **a roll resolves it** — someone acted; the dice decided | **9** | ✅ `resolve()` already does this |
| **never** — persistent by design, or no single terminal condition | **10** | ✅ the shape has no arc object to close anyway |
| **a threshold fires with nobody deciding** | **8** | ❌ **FORBIDDEN** |
| UNCLEAR — the source names no condition | 3 | — |

**Eight of fifty close in the one way Law 1 forbids. That is 16%, not the 40% the twenty-arc run
reported** — and the correction is in the shape's favour. The earlier figure came from a smaller
sample read by a regex; this one was classified from the lanes' own `ends_when` strings by a pass
that saw nothing else.

### But the useful number is the other one.

The classifier was also asked, for every arc, whether a threshold **forces the moment** even where a
person makes the final call.

> ## **19 of 50 arcs — 38% — are `forced_by_threshold: yes`.**

Read the phrases it returned and the pattern is unmistakable:

- `ARC-04` — *"the patron is **forced** to choose publicly among defend/abandon/extract"*
- `ARC-40` — *"the head of state's **forced** choice is made (act, abdicate, or be replaced)"*
- `ARC-34` — *"whose ceiling **issues a formal ultimatum** resolved through the ordinary civic debate mechanism"*
- `ARC-R16` — *"players complete a **triage response** addressing (or accepting) the accumulated consequences"*
- `ARC-01` — *"background cultural track bottoms out … **forcing** an Emergence crisis"*

**The corpus overwhelmingly does not want the counter to ACT. It wants the counter to COMPEL SOMEONE
TO ACT.** Those are different mechanisms and the shape refuses only the first.

This is the most consequential thing either test found, because **it dissolves most of `A2`'s bill
without touching Law 1.** A crossing that produces an *outcome* is forbidden and should stay
forbidden. A crossing that produces **a summons — a thing at a venue that a named person must now
answer, and whose refusal is itself witnessable** — writes no social row, needs no decider-free
social change, and is what 19 arcs are actually asking for. The 8 pure-THRESHOLD arcs are the real
residue, and it is a fifth of what the small sample implied.

> **One classification note, recorded because it argues with itself.** `ARC-17`'s source says the
> superior *"chooses"* and then immediately reclassifies that same act as *"determined by a
> threshold lookup on his own internal state … a stat, not a deliberation."* It is counted as
> THRESHOLD, following the source's own correction. **An arc whose text cannot decide whether a
> person decided is itself evidence for how blurred this line is in the corpus.**

---

## §3 · WHAT BLOCKS THE ARCS

Ranked by how many arcs stop on each, counting only needs the arc's own lane graded `core`.

### 3.1 `A2` — the arc ends at a counter, with nobody deciding *(FORBIDDEN — 8 arcs)*

The largest single blocker in the corpus, and **it is the shape working exactly as designed.** An
Event may not write a `social: true` row, so no counter can depose a governor, force a question, or
close a crisis on its own.

> ⚠ **This count was 10 and is 8, after the route was narrowed off the bare substring `counter`,
> which was matching inside *"counter-productive"*.** The correction is worth more than the two rows
> it removed: **8 is now exactly what the independent ending classification counted** — a pass that
> saw only the lanes' `ends_when` strings and no probe at all. Two instruments looking at different
> things and landing on the same number is the strongest evidence in this report, and it did not
> exist until the loose regex was fixed. A self-test now fails if the two ever diverge.

### 3.2 `A13` — an ambient social quantity cannot drift from nobody acting *(FORBIDDEN — 3 arcs, was 8)*

⚠ **THE MOST EXPENSIVE CORRECTION IN THIS REPORT. This blocker was reported as 8 arcs and it is 3.**
The route keyed on the bare word `ambient`, which caught four rows about an *ambient world-health*
or *ambient environmental* quantity — `ARC-27`, `ARC-41`, `ARC-42`, `ARC-43`. **Those are matter,
they are lawful, and the shape already serves them** (`A3` passes: the substrate is a `Site` kind).
**I sent Jordan a bill for eight arcs and the real number is three.** Found by a read-only audit
that named `ARC-41` specifically.

The three that genuinely need it: `ARC-01`'s cultural track, `ARC-44`'s per-location cultural
allegiance, and `ARC-04`'s subordinate whose trust erodes from a patron's inaction alone.

`ARC-01`'s engine is a cultural track drifting toward a pole **purely from the absence of any
faction's action**, compounding two rulers' separate restraint into a shared crisis.

The shape does exactly this for **matter**: `wear` writes `(Site, condition)`, which is
`social: false`. It **cannot** do it for a population's disposition, because that is a stance and
`(Person, stance)` is `social: true`. The probe executes both and the second raises.

**So: the harbour silts on its own; the town's mood cannot.** That asymmetry is Law 4 working
exactly as designed, and it costs **three** arcs their mechanism.

### 3.3 `P34` — a quantity accumulates in a person from their OWN acts, unreadable by them *(NO-PRODUCER — 7 arcs)*

**This probe did not exist until the corpus doubled**, and adding it is the most important thing the
expansion produced. Five arcs say the same thing in different clothes — a duke's repeated
self-directed institutional actions, a leader's intentional use of an asset, an official's long
routine service, a surveillance file growing from unrelated encounters, a private threshold one NPC
maintains against another — and every one of them wants a quantity that

1. **climbs from the person's own ordinary acts**, taken for ordinary reasons;
2. **is not readable by that person**;
3. **fires** when it crosses.

The shape retains those acts only as Events in the world log and as **decaying Claims in whoever
witnessed them**. The nearest object, the claim ledger, is the wrong shape three ways over: *it is
other people's, it decays, and its holder reads it.*

> This is the strongest empirical case in either test for admitting a bounded ratchet — and note
> what it must NOT become: point 3 is `A2` wearing a hat unless the firing produces **an Act by
> somebody else** rather than an outcome.

### 3.4 `P4` — a conviction cannot move *(UNSPECIFIED — 7 arcs)*

`02` §5.5 promises convictions move *"slowly, by scar and crisis"*; nothing specifies a scar or a
crisis, and no formula consumes a conviction. Seven arcs are about a person being changed by what
happened to them. **This is a:NPC's blocker (b) arriving at the arc scale with more weight.**

### 3.5 Three separate gaps that are one gap — the durable condition

`A16` (a formal process advancing through stages on its own timetable), `A18` (a rare roll leaving a
condition that outlives its scene), and `P30` (work spanning seasons) all fail for the **same
missing object**:

> **The shape has no DURABLE CONDITION attached to a carrier that gates later acts.**

An `Event` is a fact in the log, not a state on a thing. A `Record` exists and is the right shape —
keepable at a Rung, burnable, admissible at a venue — but nothing creates one (`P28`), nobody can
hold one (`P29`), and **its `ttl` is never decremented by any step** (`A9`). So an accusation cannot
ripen against you while you do nothing, an army cannot be stuck, a copy cannot be half-made.

**One object, properly wired, unblocks `A16`, `A18`, `A9`, `P28`, `P29`, `P30` and `P10` — seven
probes across both tests.**

### 3.6 `P3` — covert action *(NO-PRODUCER — 5 arcs)*

Five arcs turn on someone acting without others learning **who** acted. An `Event` has no field
separating the deed from its doer, and `witness()` builds a Claim from the Event, so **witnessing an
act necessarily reveals its actor.** Attribution and occurrence are one thing where the arcs need two.

### 3.7 `A15` · `A19` · `A5` — the smaller recurrences

- **`A15` (3 arcs)** — a reserve held is indistinguishable from a reserve absent. `ARC-03` is *about*
  a leader holding a decisive one-use resource while two clocks she is not watching close the window.
  Combined with `P19`, **waiting is not a move the world can see.**
- **`A19` (3 arcs)** — nobody can stop being an agent. `ARC-09` states its own premise: *"the arc
  exists because the rule has no exit."* The loop hands **every** person in `world.persons` to
  `choose`. **The arc that exists because the rule has no exit has no rule.**
- **`A5` (4 arcs)** — a self-reinforcing loop that provably terminates. Four arcs are spirals;
  nothing in the shape bounds one.

---

## §4 · WHAT SUCCEEDED

- **`A17` — winning the argument and enforcing the win are separate, and the second can fail.**
  `ARC-06`'s whole subject is that gap, and it is the one arc in fifty that runs. The shape gets it
  **for free**: a Dispensation is published as a telling, and compliance is each hearer's own
  `choose`. Nothing had to be added. *This is the single best evidence in either test that the
  shape's core is right.*
- **`A7`** — an institution acts only through a named person at a venue. *"The Church excommunicates"*
  is not spellable; *"the Confessor, at a venue, issues"* is. `ARC-21` needs exactly this.
- **`A6`** — a secret becomes public and legitimacy collapses **per-knower, at telling speed**.
- **`A3`** — the world-substrate as a `Site` kind carries the arcs that turn on it (`ARC-05`,
  `ARC-22`, `ARC-33`).
- **`P12`** again: an arc's rival can emerge without being assigned.

---

## §5 · LESSONS

1. **The biggest refusal is mostly a misreading of what the corpus wants, and the bill was
   overstated twice over.** `A2` and `A13` are one law seen twice — *a social quantity may not
   change without a decider.* The ending classification says only **8 of 50** arcs need a counter to
   *act*, while **19** need a counter to *compel someone to act*: the shape forbids the first and has
   no mechanism for the second, and building the second is the cheap fix. Then the routes were
   narrowed and the counts themselves fell — `A2` 10→8, `A13` 8→3. **A refusal is not a bill until
   you have checked what was actually being bought, and then checked that your instrument was
   pointing at it.**
2. **The world may decay; society may not.** `wear` is the shape's best mechanism and it is
   available *only* to matter.
3. **The arcs need a noun the shape almost has.** `Record` is the right object and is inert.
4. **Not acting is the arcs' most common verb, and it emits nothing.**
5. **A hidden self-accumulating quantity is the corpus's favourite engine and nobody wrote it down.**
   Seven arcs, five of them from a corpus half nobody had read when the change list was drafted,
   independently want a person's own ordinary conduct to build something they cannot see. It only
   became visible when a bad keyword route was investigated instead of merely deleted.
6. **The 228 needs that did not route were read, not dropped.** A separate pass clustered the 95
   graded `core` and found **roughly a third are restatements of the existing change list** — 19 of
   them the `Record` alone — and about nine need no engine capability at all. Of the genuine
   remainder exactly **one** looks like a missing primitive: *an ordered periodic settlement pass
   with capped, contested shared capacity*, raised independently by `ARC-R19` and `EMG-11`. It is
   the same hole `P35` reaches from the other side — **`resolve(Act[], World)` applies acts
   independently, so two people cannot contend for one scarce thing in one season.** Two of the
   largest unmapped clusters (branching named outcomes, n=11; a hidden per-person bias, n=9) are
   authoring conventions over `Record`, not systems the engine lacks, and the political-escalation
   cluster (n=8) is scene dramaturgy. **The unmapped territory is narrow, and naming it that way is
   worth more than the count.**

---

## §6 · A CORPUS FINDING, NOT A SHAPE FINDING

**`ARC-META-COLLISION` — the arc corpus numbers two different series identically.** Root
`arcs_16_19.md` and `gm_ref/arcs_10_18.md` **both use arc numbers 16, 17 and 18 for entirely
different stories**:

| number | root series | gm_ref series |
|---|---|---|
| 16 | *The World Without Direction* | *The Empty Fort* |
| 17 | *The Favour Gate* | *The Sinigaglia Dinner* |
| 18 | *The Tied Vote* | *The Stolen Steward* |

Neither file carries a reconciliation or supersession note. **Any tool indexing arcs by bare number
silently merges or discards one of each pair.** This test namespaces them (`ARC-R16..R19` vs
`ARC-16..18`) to avoid exactly that, which is why the corpus is 50 and not 47. It is a data-hygiene
defect in the source, and it needs a ruling on which series is canonical for 16–18 — not a shape
change.

---

## §7 · WHAT THIS TEST SAYS IS REQUIRED

1. **Make `Record` live**: creatable by an act, holdable by a person, with a `ttl` and a **stage**
   that MATTER advances, and the power to gate what acts are available. *(Unblocks 7 probes.)*
2. **Admit the hidden self-accumulator** — the corpus's most frequent unwritten engine — with the
   firing rule constrained to produce *someone else's Act*, never an outcome.
3. **Give abstention a producer.** An emitted abstention makes restraint witnessable, which
   simultaneously fixes `P19`, `A15` and the King's invisible doubt from a:NPC.
4. **Separate the deed from the doer.** Attribution as a per-witness claim distinct from occurrence.
5. **Decide the ambient-social question** — now worth **three** arcs, not eight.
6. **Let a person cease to be an agent**, one way only.

**Deliberately NOT recommended:** re-admitting thresholds that fire outcomes. `A2` is the shape
working, and eight arcs pay for it — that is a price, not a defect. The right move is to make *what
people do about a crossing* cheap and legible, not to let the counter act.
