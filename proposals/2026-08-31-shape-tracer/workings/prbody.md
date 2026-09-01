> ## ⚠ HELD BACK IN FULL — NOTHING RATIFIES ON MERGE
>
> Every document here is `PROPOSED`. Under `CLAUDE.md` §0.05 all of it is **REFERENCE, never
> mechanism**. **Two items need Jordan and only Jordan** — they are named in "Held back" and are
> not ratified by merging this.

Jordan-directed, in two parts. **Part 2 is the deliverable; part 1 is what preceded it.**

---

# PART 2 · TWO EXECUTED TESTS OF THE IDEALIZED SHAPE, AND A UNIFIED PROPOSAL

`proposals/2026-08-31-shape-tracer/` — **read `04_UNIFIED_SHAPE.md` first.**

Under `CLAUDE.md` §0.2 a thing is done when it **runs**. So PR #350's shape was implemented faithfully
enough to execute — six steps, four write classes, the Partition asymmetry, and a `View` that raises
on any world collection so Law 2 holds by type rather than by discipline — and then driven with real
cases.

| | |
|---|---|
| **a:NPC** | a season for **27 named NPCs**, copyist to King → **22 BLOCKED · 4 NOT-ASSESSED · 1 DEGRADED · 0 PLAYABLE** |
| **b:ARCS** | **50 arcs** from `designs/arcs` played out → **39 BLOCKED · 10 NOT-ASSESSED · 1 PLAYABLE** |
| the run | 65 probes · 527 need-rows · 79 acts · 116 events · **334 class-checked writes** |

Case specs were written by six lanes **blind to the shape**, in engine-neutral language, so a need
could not be phrased to fit what the proposal happens to contain.

## The five findings that changed the proposal

**1 · The corpus does not want the counter to ACT. It wants the counter to COMPEL SOMEONE TO ACT.**
Every arc's `ends_when` was classified by a pass that saw nothing else: 20 close on a person's
decision, 9 on a roll, 10 never, **8 on a threshold with nobody deciding** — 16%, not the 40% a
smaller sample reported, a correction in the shape's favour. But **19 of 50 are
`forced_by_threshold`**: a crossing forces the moment, *then* a person chooses. Law 1 forbids only
the first. This dissolves most of the bill without touching a law.

**2 · `Record` is the highest-leverage object in the suite and it is inert.** Seven probes across
both tests resolve to it, and an independent clustering of the 95 unrouted `core` needs found **19 of
them are the `Record`** — the largest single cluster by far.

**3 · One act per person per season, against a stated model of ~5.** The factor is not the finding.
**The finding is that with one act nobody ever chooses what to leave undone**, so a King's scarcity is
identical to a copyist's — and triage is most of what high office *is*. Largest blocker on the NPC
side. It also **voids `14`:139's provisional close of petition spray**, which was "one act per person".

**4 · `causes[]` is never written.** The suite rests its narrative layer, audit trail and arc model on
the provenance chain, and `resolve()` as specified emits Events with `causes=[]`.

**5 · A hidden quantity that climbs from a person's own ordinary acts, unreadable by them, and fires.**
Seven arcs want it independently. It surfaced only because a bad keyword route was **investigated
rather than deleted**.

## What the unified proposal does

Five laws. Four are PR #350's, two amended; **the fifth is new and load-bearing**:

> **THE EDGE LAW.** Any monotone quantity may, on crossing a declared edge, change **what may be
> chosen and by whom** — including to nothing. The crossing emits. It may never write a social row and
> never produce an outcome. **And every clock that moves such a quantity was set by a nameable act —
> so it can be bribed, delayed, burned, or killed.**

The first half promotes `05` row 8 from a CALENDAR detail to a law, and it turns seven special cases
into one: band edges, Record stages, conviction crises, agency exit, arc endings, and the summons that
19 arcs want. **The second half is the anti-scripting rule stated positively** — it is what makes
*characters drive the churn* mechanical rather than aspirational, because a quantity that advances
with no author is a shadow actor: unbuyable, undelayable, unkillable.

Also lands: an act budget of ~5 with the budget a Query; contention as an **ordered fold** rather than
a second resolver; required non-empty `causes[]`; **gated** abstention as a synthesized Act;
audience-scoped standing; and derived-valid `holds`, so a dead king stops holding the crown with **no
Partition change**.

## Two adversarial audits, and the two things they killed

Both were `valoria-critic` — **read-only by agent definition rather than by prompt**, and neither saw
the reasoning that produced what it attacked.

- **My own worst error, retracted in §3.2.** I proposed a `Record` stage *that MATTER advances*. That
  is a **fourth clock-driven quantity** in a document whose §5 reads *"no fourth may be added"*, and it
  resolved the escalated ambient-social question **locally, silently, on the side the laws refuse**,
  through a Record-shaped door labelled *"adds no type"*. The lawful version is already in the suite
  at row 11b — **act-declared terms** — and it produces a better game, because a clock a person wound
  has handles: bribe the clerk who set the term, burn the Record that carries it, kill the man who
  must renew it.
- **A bound that did not bound.** "A monotone tally counting only the holder's own ledger" was broken
  in one move: a per-cohort *harms witnessed* counter satisfies it and reconstructs stored `unrest` —
  **worse than the field Law 3 banned, because it cannot go down.** Keyed instead to the **closed
  canon Conviction roster**, the violation cannot be spelled.

## Five instrument defects, all of which flattered the shape

The tracer gates every finding, so its own honesty is tested by `tracer/test_tracer_is_honest.py`
(**20 self-tests**). Defects found and regression-tested: `W2` counted only `resolve()`'s return and
missed MATTER-emitted band events, so a site strobing 6× in 6 seasons reported clean; the Partition
table carried **rows the suite does not have**, turning a real gap into a PASS; and **four separate
greedy-keyword routing defects** — the last found by an audit, which caught `01` §3.2 naming three
blockers the instrument had produced one of. **The rule they cost me: when a route is wrong, read what
it was catching before you cut it.** Two of the most consequential findings arrived that way.

**226 of 527 needs did not route and are reported `UNMAPPED` rather than passed.** Fourteen cases are
`NOT-ASSESSED` rather than graded, because a case whose `core` needs mostly failed to route was not
tested, and grading it PLAYABLE would be the instrument flattering the shape by failing to aim at it.
**Probe verdicts are hard; case verdicts are advisory**, and the reports say so on every page.

## A corpus finding, not a shape finding

Root `arcs_16_19.md` and `gm_ref/arcs_10_18.md` **both number three entirely different stories 16, 17
and 18**, with no reconciliation note in either file. Any tool indexing arcs by bare number silently
merges or discards one of each pair. This test namespaces them; it needs a ruling, not a shape change.

---

# PART 1 · THE 2026-06-28 ARCHIVE, INTERROGATED AGAINST PR #350

`proposals/2026-08-31-pr350-archive-recovery/` — 12 Sonnet scrape lanes over all 819 snapshot files,
each **blind to PR #350 by instruction**, then 3 read-only comparative lanes.

**The standard, ruled by Jordan mid-session:** *"It doesn't matter if anything was already built — it
only matters if it was built extremely well."* So `## Status: CANONICAL` and prior ratifications are
evidence about quality, never a substitute for it — **§5 rejects canonical and ratified archive
material on those grounds, and §4 names PR #350's own best ideas.**

Roughly **two-thirds** of what the lanes surfaced was dispositioned COVERED or SUPERSEDED: PR #350
regenerates most of the archive's governance layer from smaller primitives, and several of its answers
are strictly better. The three findings that survived — the moral layer is a nameplate, the act economy
is contradicted three ways, and *"nothing is lost"* is false — were each verified by hand against
primaries. The third: a `Proposition` may be a `hold` subject and is never destroyed, so a dissolved
faction leaves **territory held by a banner nobody carries**, uncontestable because the holder can
never appear at a venue.

---

## ⚠ HELD BACK — needs Jordan, and survives all five of `CLAUDE.md` §0's tests

1. **May a social quantity sink by neglect alone — as memory already does — and is a person acting on
   witnessed loss enough to turn that sinking into a crisis?** This is the *narrowed* form of the
   ambient-social question. Three earlier framings of it were wrong: it is not an ending problem (Law 1
   refuses those separately); one arc on its table was an **unmarked Partition cell, not a law
   conflict**; and the suite **already ships** a licensed decider-free social-adjacent drift — claim
   confidence decaying and evicting, *"he loses the town by being forgotten"* — that the escalation
   never considered. If the answer is yes, this costs nothing and no law moves.
2. **Does a scene contain acts, or is a scene an act?** Jordan's own hedge — *"which **may** mean ~5
   actions."* The proposal takes act ≡ scene-action, with a scene as the rendered resolution at
   `played` fidelity. His call.

## Lane, IDs, and the ED-1094 checklist

- **Lane:** cross-cutting **IN**. Lands only in `proposals/`.
- **IDs allocated: none, deliberately.** Per `CLAUDE.md` §0's amendment a ledger row is warranted only
  where it requires a human decision — and the two that do are carried prominently here and in
  `04_UNIFIED_SHAPE.md` §6.1, which is ED-1094's "called out loudly" discipline rather than a queue
  entry. Nothing consumes `id_reservations.yaml`.
- [x] **Ratify-on-merge:** nothing is landed as PROPOSED-pending-flip. There is no `## Status:` line,
      ED field or `CURRENT.md` row that merging should flip.
- [x] **Currency:** no `CURRENT.md` row is owed — `proposals/` is surfaced **by location** (§3), which
      is how PR #350 itself sits.
- [x] **Green locally:** `python -m pytest tests/valoria -q` → **1778 passed, 23 skipped, 15 xfailed**.
      `cd tracer && python3 -m pytest test_tracer_is_honest.py -q` → **20 passed**.

## The honest state

**Nothing here executes as the game.** The tracer executes *a model of the proposal* — that is what
makes the findings measurements rather than readings, and it is also its ceiling: it says what the
shape as specified can and cannot do, not what an implementation would do. `04_UNIFIED_SHAPE.md` §7
carries a falsifier for every load-bearing claim, including the ones I expect to survive.

---
_Generated by [Claude Code](https://claude.ai/code/session_011CEsHWuCxKAiNbB7mRLmuE)_
