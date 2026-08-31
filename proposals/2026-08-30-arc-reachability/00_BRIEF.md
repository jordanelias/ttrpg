# Arc reachability — can the new design produce the old arcs?

## Status: BRIEF (2026-08-30) — planned by Fable 5 (read-only sweep); executed by Sonnet and Opus lanes.
## Corpus: `designs/arcs/` at ref `v30-snapshot-2026-06-28` — 39 files, ~8,400 non-index lines, arcs 1–55.
## Extracted to: /tmp/claude-0/-home-user-ttrpg/3e252927-aab6-508a-bc93-753009215ed9/scratchpad/arcs/
## Tests against: `proposals/2026-08-29-valoria-from-scratch/` (the merged suite).

---

## 1. Why these arcs are the right test, and the trap in using them

**Jordan: "we do not need these arcs to be sacred — they are old and deprecated in many ways… we just
want to test."** That framing is exactly right, and it defines the method.

Each arc makes a **precise, falsifiable claim**: *these named mechanics, interacting across N seasons,
produce this story, and no one authored it.* Every arc ships a mechanical causal chain with named
thresholds. That is a specification, and a specification can be checked against a different design.

**The trap, and the whole reason this is worth doing:** the arcs are built on objects the new design
**refuses by name**. Arc 1's engine is a Restoration ambient track that drifts *from the absence of
action*, plus Church Influence accumulating per season, plus thresholds that fire with nobody
deciding. The new design forbids all three — no unrest gauge on a place, no faction-wide scalar, and
explicitly **no threshold, because "a threshold would let the world revolt without anyone having
decided to."**

So a naive check returns "arc unreachable" for most of the corpus and learns nothing. **The question
that is actually worth asking is two-layered, and every arc must be scored on both:**

| | question |
|---|---|
| **MECHANISM** | can the new design run the arc's stated causal chain? Usually **no**, often *by design* |
| **STORY** | can the new design produce the arc's narrative outcome by a different route — persons acting, claims propagating, commitments migrating — **with nobody authoring it**? |

**A `MECHANISM: NO / STORY: YES` is a WIN for the new design.** It means the story was real and the
old machinery was scaffolding. Arc 1 is the worked example: two men's individually rational restraint
compounding into a vacuum neither intended is *precisely* what the new design claims to produce — as
grievance accumulating in ledgers because no petition is ever carried, not as a track drifting.

**A `STORY: NO` is a genuine loss and the most valuable finding in this exercise.** It means the old
design could tell a story the new one cannot.

---

## 2. The verdict set

Every arc gets exactly one:

| verdict | meaning |
|---|---|
| **REPRODUCED** | story reachable, and by composition rather than authoring. Name the persons and acts |
| **REPRODUCED-BETTER** | reachable, *and* the new route removes an authored element the arc needed (a threshold, an ambient drift, a scripted actor) |
| **TRANSFORMED** | a story happens, but a materially different one. Say what changed and whether the change is an improvement |
| **LOST** | the story is not reachable. **State precisely which missing mechanism blocks it** |
| **NEVER-WORKED** | the arc did not work in its own terms either — it is scaffolding, an unbuilt dependency, or a GM instruction. **Do not count these as losses** |

That last one matters: the corpus is CP14-era, self-declared superseded, and full of forward
references to designs that were never built. **An arc that was already broken is not evidence against
the new design**, and a lane that scores it as a loss has corrupted the result.

---

## 3. What every arc entry must contain

1. **Arc id and one-line premise.**
2. **The arc's own stated mechanics**, quoted from its "Primary mechanics" line.
3. **Which of those the new design refuses, and where it says so.** This is the interesting half.
4. **The new design's route to the same story** — named persons, named acts, the propagation path. Or
   the statement that there is none.
5. **Verdict**, with the reason.
6. **What it cost.** If TRANSFORMED or LOST, what specifically is gone.

---

## 4. The four questions the suite must answer at the end

- **How many arcs survive, and does the pattern have a shape?** Are the losses concentrated in one
  mechanism class (ambient drift, faction scalars, GM fiat) or scattered?
- **Does the new design's refusal of thresholds cost stories?** This is the sharpest single question.
  The design forbids a threshold on principle; the arcs use thresholds constantly to force a
  position. If the design cannot force a position, arcs do not resolve — they just continue.
- **Which arcs need an NPC the design cannot motivate?** Cross-reference the play-space coverage
  finding that **19 of 55 characters have a blocked core**. An arc whose engine is a character whose
  want is unreachable is dead on arrival, and that is the two exercises meeting.
- **What does the corpus want that the design has no object for?** The arcs were written by people
  imagining this game. A recurring demand with no home is a design gap found from the fiction side.

---

## 5. Discipline

- **The arcs are not sacred.** They are deprecated, CP14-era, and often self-superseded. Test them;
  do not defend them, and do not defer to them.
- **The merged suite is the thing under test.** Where it lacks a mechanism, that is a finding — but
  check first whether the *refusal was deliberate and reasoned*, because a deliberate refusal that
  costs no story is a success and must be reported as one.
- **No new mechanisms.** Not one. This is an assessment.
- Where an arc depends on a canon contradiction or an unbuilt dependency, mark it NEVER-WORKED and
  move on rather than adjudicating canon.
