# Suite 06 — Method, the Falsifier Record, and the Queue

**Status:** PROCESS RECORD. This document contains no design proposals. It records **how** the rest of
the suite was produced, **every claim this session retracted**, and the actual shape of the decision
queue.

It exists because the retractions are more useful than the findings. Roughly a third of what this
session first produced did not survive being attacked, and the failures cluster into **one repeating
error** with a one-line check.

---

## §1 The method

Four stages, in order. Skipping any one of them produced a retraction.

**1. Mechanical extraction — parse, never pattern-match.**
Rosters, call sites and reachability came from AST walks and YAML/structural parses. `grep` located
candidates and concluded nothing. This is the repo owner's standing constraint and it earned its
keep twice in one document — §4.4's `[ASSUMPTION]` count is **13 by grep, 0 by naive parse, and 11 by
structural attribution**, and only the third is right.

**2. Producer agents — sweep and draft.**
Wide passes producing candidate findings. Their output is *candidates*, and treating them as findings
is what produced most of §4.

**3. Structurally independent antagonists — attack the output, never the reasoning.**
Read-only critics (`Read`/`Grep`/`Glob`; no write tools) given the producer's **output only**. Their
independence is structural, not declared — a critic that never saw the reasoning cannot be
persuaded by it. Three such passes ran; each overturned something material.

**4. Verify load-bearing claims myself before reporting.**
The stage that matters most, and the one with no substitute. Antagonists were wrong too — one
asserted `symbolic_dimensions` does not exist in the Key substrate, when it is a real field at
`keys.py:150`. **Accepting that would have retracted a correct claim.** Another put the
`[ASSUMPTION]` count at 11 by grep-line-counting; the number is right, but the derivation was the
same technique that gives 13.

Both directions of error are live. A finding is not true because a producer found it, and not false
because a critic attacked it.

---

## §2 The error class

> **Matching a *name* across two surfaces and inferring a defect without establishing that the two
> surfaces discuss the same thing.**

Committed at least six times. Every instance had the same shape — a token appears in two places, the
two declarations differ, a contradiction is reported — and in every instance the two places were about
different things.

**The check is one question, and it costs one file read: do these two surfaces have the same
referent?**

| # | The token | What was claimed | What the surfaces actually are |
|---|---|---|---|
| 1 | `scale` | "A Foundational Weaving cannot emit a Key" | A `Key.scale_signature` enum, a Thread-operation difficulty table, and one of three Ob axes |
| 2 | Resonant Style | The armature's 4th axis drifts from canon | A ratified deliberate substitution with its reason in the file |
| 3 | `accord` | Value conflict across two writers | One writer is genuinely wrong-scale; the "conflict" framing was not |
| 4 | Mandate | "Mandate computes to 0" | `Faction.L` **is** Mandate, by a convention cited five times |
| 5 | outcome enums | "Nine rival degree ladders" | Three ladders; six enums with disjoint referents |
| 6 | Church threshold | "40 / 60 / 65 / 100 across four surfaces" | One graduated milestone table plus a separate availability gate |

**The generalisable rule: a shared token is a candidate, never a finding.** In Suite 03's register the
cost of skipping the check was 38% of the output — and it fell hardest on the *most confident* items.

---

## §3 What the method caught that a single pass would not

Recorded so the cost is judged against the return.

- **Suite 01 §1.3** — the Tree A removal fires **five** guards, and the J2 seam test **fails** on
  deletion because its own state-B probe imports the module being deleted. A single pass published
  "one guard, and the seam test passes by construction." Executing on that would have produced five
  failures and no diagnosis.
- **Suite 03 §7.1** — a correction this session had **queued for CLAUDE.md** would have put a false
  number into the governing document.
- **Suite 02 §2.9** — two registry records lose data to an unquoted `#` on every parse. Found by
  parsing and comparing to the raw lines; invisible to reading either one alone.
- **Suite 02 §1.2** — T15/T16 are mirror holes in two 16-member rosters. **No count check can see
  this**, and both rosters are individually well-formed.
- **Suite 03 §2.2** — `tests/valoria/test_knots_ed912.py:103-116` asserts the intent flag and never
  the state, so it passes while the mechanism it tests silently no-ops. A test that cannot observe the
  failure it excludes.

---

## §4 The falsifier record — every retraction

Kept in full, per CLAUDE.md §0.1 point 3. A result claim without its falsifier is unfalsifiable.

### §4.1 Overturned outright

| Claim | Verdict | What is actually true |
|---|---|---|
| "The gap is ONE function body" | **OVERTURNED** | Four structural blockers |
| "The single missing artifact is a loader" | **OVERTURNED** | Registry schema and `NPC` dataclass do not correspond — Suite 04 §1 |
| "`owner_faction` is populated for one settlement" | **OVERTURNED** | 37 of 37. Producer misread a docstring |
| "4 of `conviction.py`'s 9 are in no taxonomy" | **OVERTURNED** | Zero. It is the legacy 9 verbatim |
| "46 fully-structured characters" | **OVERTURNED** as a population claim | `stats` 1/46, `coherence` 1/46, `territory` 7/46 |
| "`scene.contest_resolved` is the only emitted type" | **OVERTURNED** | `faction_action.py:342` emits `scene.battle_concluded` |
| "Our authored fields forbid nothing" | **OVERTURNED** | `npc_behavior_v30.md:52`, `:991`, and more |
| "A null band is the mechanism we most lack" | **OVERTURNED** | One exists at two levels — `npc_behavior_v30.md:901-912` |
| "A biased reading function is new design" | **OVERTURNED** | Specified twice in canon already |
| "`mass_seizure` needs only a call site" | **OVERTURNED** | `:293` writes a canonical index into a continuous field |
| "Mandate computes to 0" | **OVERTURNED** | `Faction.L` **is** Mandate |
| "Reputation silently erases" | **OVERTURNED** | Replacement is specified behaviour |
| "A Foundational Weaving cannot emit a Key" | **OVERTURNED** | Suite 03 §4.1 |
| "The Church threshold is 40/60/65/100" | **OVERTURNED** | Suite 03 §5.1 |
| "`AMPLIFY`/`DIVERGE` exist nowhere" | **OVERTURNED** | ED-150 / PP-529 / PP-301 |
| "The 4-member Gap scale is invented" | **OVERTURNED** | `threadwork_v30.md:468-471` |
| "One guard blocks Tree A removal" | **OVERTURNED** | Five — Suite 01 §1.3 |
| "The `[ASSUMPTION]` count is 10/27" | **OVERTURNED** | 11 — Suite 03 §7.1 |

### §4.2 Narrowed

| Claim | What survives |
|---|---|
| "Nine rival outcome vocabularies" | Three ladder-shaped, six disjoint enums, **plus a tenth the sweep missed** at `key_type_registry_v30.md:887` |
| "`graze` has four incompatible meanings" | Two semantics, one declared; the real defect is a **behavioural** port/oracle divergence on `partial` |
| "`scene.contest_resolved` is emitted every season" | Conditional on winner and degree |
| "Chronicle band bug at `narrative.py:114/:126`" | Substance right; the defect is at `:88/:92` — **fixing the cited lines would patch the wrong function** |

### §4.3 Inverted by ruling

The TN finding. This session published the TN-blind `roll_pool` as the defect. Under Jordan's ruling
that TN is always 7, **the roller is correct** and the two non-7 declaration sites are the defect.
Nothing was measured wrong; the frame was.

### §4.4 A correction to a correction

The most instructive single item. CLAUDE.md §6 states 10 of 27 modules have `doc: null` and 11 have
`[ASSUMPTION]`-grade resolvers. This session filed a correction saying 9 and 10, and queued it.

```
grep -c ASSUMPTION           →  13   (picks up a header comment and two state entries)
naive YAML parse             →   0   (the marker is a trailing COMMENT on resolver:)
structural attribution       →  11   ← correct
doc: null, parsed            →   9   ← the other half of the correction is right
```

**CLAUDE.md's `11/27` was correct.** The queued edit must be reduced to the `doc: null` half only.

### §4.5 Two things I got right by checking

Recorded because verification runs both ways:

- An antagonist claimed `symbolic_dimensions` does not exist. It is a real `Key` field at
  `keys.py:150`. Accepting the critique would have retracted a true claim.
- A pool sweep by function name found five of eight formulas. Three are invisible to it —
  `contest/primitives.py:208-211` is a **class** named `Pool` with a static `size`, and
  `knots.py:214-216` is an **inline expression**. The AST sweep was correct *and* incomplete, which is
  the more dangerous combination.

---

## §5 The queue

Measured directly from `registers/editorial_ledger*.jsonl` (excluding archives), 2026-08-23.

```
total ledger entries                                            535
genuinely open (after excluding disposed statuses)              254
   of those, flagged needs_jordan                               110
```

"Disposed statuses" excluded: resolved, closed, done, ratified, superseded, struck, applied, landed,
ruled, deprecated, and `resolved-mechanical-tier-jordan-vetoable`. The residual open statuses are
`open` (240), `provisional` (5), `partial` (4), `deferred` (2), `confirmed` (2), `proposed` (1).

*The SessionStart banner reports 239 open / 112 needing Jordan. The difference is filter definition,
not disagreement — the banner's is not this one. Both are defensible; neither is documented, which is
itself worth fixing.*

### §5.1 By age

| | open | needs Jordan |
|---|---|---|
| pre-July | 78 | **14** |
| July | 135 | **70** |
| August | 35 | **26** |
| undated | 6 | 0 |

**This corrects the framing that prompted the count.** The instinct was that a large queue is mostly
stale, and that dropping anything older than July would clear most of it. It does not: **96 of the 110
Jordan items are July or August.** Dropping pre-July removes 14. The queue is not old — it is current
and genuinely unanswered.

### §5.2 By lane

```
IN 30 · SE 23 · SC 17 · FA 15 · MB 8 · PC 2 · WR 1
plus 14 flat pre-cutover IDs (ED-NNN)
```

Infrastructure and Settlements together are half the Jordan queue. The 14 flat pre-cutover IDs are the
oldest cohort and map onto §5.1's pre-July row almost exactly.

### §5.3 What this suite does to the queue

Suite 04 §6 reduces the *build-blocking* subset to **seven** questions, of which **two** — what a
character is at runtime, and what a strategic army is in cells — block nearly everything else. That is
a different object from the 110: the 110 are editorial items of varied weight; the seven are the
decisions the engine is actually waiting on.

Answering Q1 and Q2 unblocks five chains and one of the three rulings. Answering the other 108 items
unblocks, individually, very little.

---

## §6 What this cost, and whether it was worth it

Three antagonist passes, four adjudication passes, and several dozen direct verifications, over
sixteen commits.

**Return:** eighteen claims overturned, four narrowed, one framing inverted, one false correction
stopped before it reached the governing document, and five defects found that no single pass surfaced
(§3).

**The honest negative result:** the session's scratchpad contained **no unique salvage**. Both prose
drafts were already fully committed, and one of them — the pre-adversarial draft — is *stale*, since
the committed version had already falsified three of its own claims. Anyone salvaging from the draft
rather than the committed document would have re-introduced them. Recorded per CLAUDE.md §0.1 point 4:
a null result reported is a measurement; a null result suppressed is a bias.

**What I would keep:** stages 1 and 4 — parse rather than pattern-match, and verify load-bearing
claims yourself. Stage 3's independent critics earned their cost on judgment calls and produced noise
on mechanical ones. Stage 2's producers are only worth their cost if their output is treated as
candidates, which was the whole failure of §2.

---

_Compiled 2026-08-23 against `claude/fable5-investigations-architecture-1phbx9`. Every retraction in
§4 names the reading that overturned it. Queue figures re-measured for this document, not carried
forward._
