# AGONIST -> ANTAGONIST RELAY — the discipline for parts 2 and 3
# Jordan, 2026-08-31: parts 2 and 3 run in agonist-antagonist mode.

## IT IS A RELAY, NOT A DIALOGUE. This is the whole point.
Subagents are stateless and isolated. So:
  1. dispatch the AGONIST (producer). It writes.
  2. capture its OUTPUT.
  3. dispatch the ANTAGONIST with THAT OUTPUT ONLY -- never the agonist's reasoning, never its prompt.
  4. reconcile in the orchestrator (Fable). The orchestrator, not the antagonist, decides.

A critic that never saw the producer's reasoning is MORE independent, not less informed. Do not let
the two converse; do not pass the agonist's justifications forward. The antagonist must meet the
claims cold, exactly as a later reader would.

## INDEPENDENCE IS STRUCTURAL, NOT DECLARED
The antagonist runs on the `valoria-critic` definition: Read, Grep, Glob. No Write, no Edit, no Bash.
It CANNOT repair the thing it reviews whatever its prompt says. That property lives in the agent
definition, not in an instruction -- which is the failure the definition exists to fix, since a
"critic" declared read-only by a sentence inside its own prompt is restricted by nothing.

## MODEL TIERING (CLAUDE.md section 10)
AGONIST   Opus -- producing a synthesis artifact; reviewable and cheap to revise.
ANTAGONIST Opus or Fable -- an audit verdict is where being wrong is SILENT, so spend the tier here.
Sonnet takes the mechanical or bounded stages where the reasoning is already fixed.

## WHAT THE ANTAGONIST IS FOR, PRECISELY
Not "find flaws in the prose". Attack the CLAIMS, on the four axes already in use:
  FACTUALITY  is it true? recount, re-read, verify citations against the documents named
  LOGIC       does the conclusion follow? is any test circular or unfalsifiable?
  RIGOUR      is the method sound? was the scale one-sided? was a convergence seeded?
  COMPLIANCE  does the proposal obey PR #342's code shape -- the forbidden list, the ownership table,
              the three signatures, R-1/R-2? (verbatim in scratchpad/CODESHAPE_FORBIDDEN.md)
And apply scratchpad/PESSIMISTIC_NERS.md, especially P-4: PREFER THE INTERPRETATION THAT COSTS THE
DESIGN MORE.

## THE ORCHESTRATOR'S JOB AFTER THE RELAY
Reconcile -- which is NOT "accept the antagonist". This session has already had a correction agent
correctly REFUSE an instruction of mine that would have put a false claim into the register, and an
arc lane correctly overturn a defect I had filed. Both directions happen. The reconciliation must
say, per contested claim, which side won and why, and it must record the losers.
