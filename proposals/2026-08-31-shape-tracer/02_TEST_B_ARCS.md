# TEST b:ARCS — can the arcs in `designs/arcs` be played out under the shape?

## Status: **PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge.**
## This test RAN. Same instrument, same tracer, same gap register as `01_TEST_A_NPC.md`.

> **THE TEST.** Take the arc corpus at `v30-snapshot-2026-06-28/designs/arcs`, extract from each arc
> **what the engine must be able to DO for that story to happen at all** — written by lanes blind to
> the shape — and run those requirements against PR #350's executing season loop.

**SCOPE AS RUN: 50 arcs.** The 18 of the `gm_ref` current series, the root series' arcs 16–19 and
20–45, and 2 cases from the emergent corpus. Together with a:NPC's 27 characters that is **78 cases
and 527 `season_requires` rows** driven through 64 probes.

---

## §1 · THE RESULT

| | |
|---|---|
| cases | **50 arcs** |
| verdict | **39 BLOCKED · 10 NOT-ASSESSED · 1 PLAYABLE** |
| top core blockers | `A2` threshold-ending (10) · `A13` ambient social drift (8) · `P34` hidden self-accumulation (7) · `P4` conviction motion (7) · `P3` covert action (5) · `P26` accumulated harm (5) |

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

<!--ENDINGS-->

---

## §3 · WHAT BLOCKS THE ARCS

Ranked by how many arcs stop on each, counting only needs the arc's own lane graded `core`.

### 3.1 `A2` — the arc ends at a counter, with nobody deciding *(FORBIDDEN — 10 arcs)*

The largest single blocker in the corpus, and **it is the shape working exactly as designed.** An
Event may not write a `social: true` row, so no counter can depose a governor, force a question, or
close a crisis on its own. Ten arcs are built on a counter that does exactly that.

> **This confirms PR #350's own estimate and doubles it.** `06` §6.1 says that in its measured band
> *"three end at a counter… and lose their ending"*. Measured across fifty arcs by execution, ten
> `core` needs across the corpus die here. The refusal is real, it is deliberate, and **it is more
> expensive than the suite priced it.**

### 3.2 `A13` — an ambient social quantity cannot drift from nobody acting *(FORBIDDEN — 8 arcs)*

`ARC-01`'s entire engine is a cultural track drifting toward a pole **purely from the absence of any
faction's action**, compounding two rulers' separate restraint into a shared crisis. Seven more arcs
need the same motion.

The shape does exactly this for **matter**: `wear` writes `(Site, condition)`, which is
`social: false`. It **cannot** do it for a population's disposition, because that is a stance and
`(Person, stance)` is `social: true`. The probe executes both and the second raises.

**So: the harbour silts on its own; the town's mood cannot.** That asymmetry is Law 4 working
exactly as designed, and it costs eight arcs their mechanism.

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

1. **The two FORBIDDEN blockers are the top two, and together they are 18 arcs.** `A2` and `A13`
   are one law seen twice: *a social quantity may not change without a decider.* That law is right
   about polities and it is what the arc corpus is overwhelmingly built on. **This is the design's
   central bill, and doubling the corpus doubled it rather than diluting it.**
2. **The world may decay; society may not.** `wear` is the shape's best mechanism and it is
   available *only* to matter.
3. **The arcs need a noun the shape almost has.** `Record` is the right object and is inert.
4. **Not acting is the arcs' most common verb, and it emits nothing.**
5. **A hidden self-accumulating quantity is the corpus's favourite engine and nobody wrote it down.**
   Seven arcs, five of them from a corpus half nobody had read when the change list was drafted,
   independently want a person's own ordinary conduct to build something they cannot see. It only
   became visible when a bad keyword route was investigated instead of merely deleted.

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
5. **Decide the ambient-social question.** Either social quantities may drift without a decider —
   a real amendment to Law 4 — or eight arcs lose their engine and the design says so out loud.
6. **Let a person cease to be an agent**, one way only.

**Deliberately NOT recommended:** re-admitting thresholds that fire outcomes. `A2` is the shape
working, and ten arcs pay for it — that is a price, not a defect. The right move is to make *what
people do about a crossing* cheap and legible, not to let the counter act.
