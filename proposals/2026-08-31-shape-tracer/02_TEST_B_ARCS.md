# TEST b:ARCS — can the arcs in `designs/arcs` be played out under the shape?

## Status: **PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge.**
## This test RAN. Same instrument, same tracer, same gap register as `01_TEST_A_NPC.md`.

> **THE TEST.** Take the arc corpus at `v30-snapshot-2026-06-28/designs/arcs`, extract from each arc
> **what the engine must be able to DO for that story to happen at all** — written by lanes blind to
> the shape — and run those requirements against PR #350's executing season loop.

⚠ **SCOPE AS RUN.** 20 arcs: the 18 of the current `gm_ref` series, plus 2 cases from the emergent
corpus. A further lane covering the root series (arcs 19–45) was still extracting when this was
written; its cases fold in without changing the instrument.

---

## §1 · THE RESULT

| | |
|---|---|
| cases | **20 arcs** |
| verdict | **14 BLOCKED · 2 DEGRADED · 4 PLAYABLE** |
| top blockers | `P3` covert action (4) · `A5` boundedness (3) · `A15` held reserve (3) · `W2` band strobing (3) |

**Four arcs run.** Fourteen stop on a need their own lane graded `core`.

---

## §2 · THE HEADLINE — how these stories END

This is the most valuable single distribution the test produced, because it is the exact axis
PR #350's Law 1 cuts along. Each arc's lane recorded `ends_when` independently, with no knowledge
of the shape.

| how the arc ends | count |
|---|---|
| **a threshold or counter reaching a number, with NOBODY deciding** | **8** |
| a person chooses | 3 |
| a roll resolves it | 3 |
| never — by design, no closing condition | 2 |
| UNCLEAR — the source names none | 2 |
| other | 2 |

**Eight of twenty arcs — 40% — end in the one way Law 1 forbids.** `A2` executes this and it is
`FORBIDDEN`: an Event may not write a `social: true` row, so no counter can depose a governor, force
a question, or close a crisis on its own.

**And two arcs name the absence explicitly.** `ARC-01` and `ARC-02` both record `who_acts:` entries
that say, in the lane's own words, *"nobody is named as deciding"* — for `ARC-01` the cultural track
that produces the crisis, for `ARC-02` the character's own transformation. These are not arcs that
happen to lack a decider; **they are arcs whose subject is that nobody decided.**

> **This confirms PR #350's own estimate and sharpens it.** `06` §6.1 says that in its measured band
> *"three end at a counter… and lose their ending"*. Measured across twenty arcs by execution, the
> figure is **eight**. The suite's refusal is real, it is deliberate, and **it is more expensive than
> the suite priced it.**

---

## §3 · WHAT BLOCKS THE ARCS

### 3.1 `A13` — an ambient social quantity cannot drift from nobody acting *(FORBIDDEN)*

`ARC-01`'s entire engine is a cultural track drifting toward a pole **purely from the absence of any
faction's action**, compounding two rulers' separate restraint into a shared crisis.

The shape does exactly this for **matter**: `wear` writes `(Site, condition)`, which is
`social: false`. It **cannot** do it for a population's disposition, because that is a stance and
`(Person, stance)` is `social: true` — an Event may not write it. The probe executes both and the
second raises.

**So: the harbour silts on its own; the town's mood cannot.** That asymmetry is Law 4 working
exactly as designed, and it costs `ARC-01` its mechanism.

### 3.2 `A14` — a person cannot change with nobody deciding *(UNSPECIFIED)*

`ARC-02`'s premise is that Cardinal Klapp develops a perceptual sensitivity through routine duty,
and the source states it flatly: *"spontaneous — no actor triggers this."* The probe tries to write
`Person.capability` from an Event and gets **UNSPECIFIED**, not FORBIDDEN — because the suite has
**no Partition row for capability at all**, so one cannot even ask whether an Event may write it.
`04` §4 says an unmarked cell is a violation; this is one.

### 3.3 Three separate gaps that are one gap

`A16` (a formal process advancing through stages on its own timetable), `A18` (a rare roll leaving a
condition that outlives its scene), and `P30` (work spanning seasons) all fail for **the same
missing object**:

> **The shape has no DURABLE CONDITION attached to a carrier that gates later acts.**

An `Event` is a fact in the log, not a state on a thing. A `Record` exists and is the right shape —
keepable at a Rung, burnable, admissible at a venue — but nothing creates one (`P28`), nobody can
hold one (`P29`), and **its `ttl` is never decremented by any step** (`A9`). So an accusation cannot
ripen against you while you do nothing, an army cannot be stuck, a copy cannot be half-made.

**This is the single highest-leverage finding in b:ARCS**: one object, properly wired, unblocks
`A16`, `A18`, `A9`, `P28`, `P29`, `P30` and `P10` — seven probes across both tests.

### 3.4 `A15` — a reserve held is indistinguishable from a reserve absent

`ARC-03` is *about* a leader holding a decisive one-use resource for the right moment while two
clocks she is not watching close the window. The shape has no once-per-arc act, no record that an
act is being **withheld**, and no value that decays while unused. Combined with `P19` — a person who
chooses nothing emits nothing — **waiting is not a move the world can see.** Three arcs need it.

### 3.5 `A19` — nobody can stop being an agent

`ARC-09` states its own premise: *"the arc exists because the rule has no exit."* A practitioner
crossing zero becomes lucid, competent, and **no longer able to choose**. The loop hands **every**
person in `world.persons` to `choose`; there is no state in which a person exists and may not decide.
**The arc that exists because the rule has no exit has no rule.**

### 3.6 `P3` — covert action, the most frequent blocker

Four arcs turn on someone acting without others learning **who** acted. An `Event` has no field
separating the deed from its doer, and `witness()` builds a Claim from the Event, so **witnessing an
act necessarily reveals its actor.** Attribution and occurrence are one thing where the arcs need two.

---

## §4 · WHAT SUCCEEDED

Four arcs run, and one success is a genuine design win worth naming:

- **`A17` — winning the argument and enforcing the win are separate, and the second can fail.**
  `ARC-06`'s whole subject is that gap. The shape gets it **for free**: a Dispensation is published
  as a telling, and compliance is each hearer's own `choose`. Nothing had to be added.
- **`A7`** — an institution acts only through a named person at a venue. *"The Church excommunicates"*
  is not spellable; *"the Confessor, at a venue, issues"* is. Several arcs need exactly this.
- **`A6`** — a secret becomes public and legitimacy collapses **per-knower, at telling speed**.
- **`A3`** — the world-substrate as a `Site` kind carries the arcs that turn on it.
- **`P12`** again: an arc's rival can emerge without being assigned.

---

## §5 · LESSONS

1. **The refusal that costs the most is the one the suite already knew about, and it costs double.**
   Law 1's ban on threshold-endings is deliberate and defensible. Measured, it takes the ending off
   **8 of 20 arcs**, not 3 of 18. The design should either pay that knowingly or find the one
   substitute that does not reintroduce a decider-free social write.
2. **The world may decay; society may not.** `wear` is the shape's best mechanism and it is available
   *only* to matter. Every arc whose engine is an ambient social drift is blocked by the same clean,
   correct application of Law 4. **This is the sharpest tension the two tests jointly expose.**
3. **The arcs need a noun the shape almost has.** `Record` is the right object and is inert. Seven
   probes across both tests resolve to it.
4. **Not acting is the arcs' most common verb, and it emits nothing.** Held reserves, deliberate
   non-commitment, restraint, a Church that declines to move — four arcs are *about* someone not
   acting, and the shape cannot represent the difference between choosing not to and being absent.

---

## §6 · WHAT THIS TEST SAYS IS REQUIRED

1. **Make `Record` live**: creatable by an act, holdable by a person, with a `ttl` and a **stage**
   that MATTER advances, and the power to gate what acts are available. *(Unblocks 7 probes.)*
2. **Give abstention a producer.** An emitted abstention makes restraint witnessable, which
   simultaneously fixes `P19`, `A15` and the King's invisible doubt from a:NPC.
3. **Separate the deed from the doer.** Attribution as a per-witness claim distinct from occurrence.
4. **Decide the ambient-social question.** Either social quantities may drift without a decider —
   a real amendment to Law 4 — or eight arcs lose their engine and the design says so out loud.
5. **Let a person cease to be an agent**, one way only.

**Deliberately NOT recommended:** re-admitting thresholds that fire outcomes. `A2` is the shape
working. The right move is to make *what people do about a crossing* cheap and legible, not to let
the counter act.
