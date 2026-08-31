# SHARED BRIEF — read this, then your lane assignment

## THE EXERCISE
Designing the videogame VALORIA FROM SCRATCH. No-GM; the engine resolves everything. Personal-scale
resolution (dice pools, skill checks, social contests) fused with a strategic layer (territory,
faction politics, domain actions).

## THE ABSOLUTE RULE
ALL EXISTING WORK IS REFERENCE ONLY, NEVER RULING. No prior design document, no `## Status:
RATIFIED` line, no ED-NNNN, no PP-NNN, no recorded ruling, and NO EXISTING CODE constrains you.
DO NOT read or cite engine/, systems/, tools/, or any proposals/ directory other than the one file
named as your spine. If you catch yourself writing "per ruling X", "to unblock Y", "retarget Z", or
"this closes blocker B-n", STOP - that is the exact failure this exercise exists to escape.
You are a DESIGNER, not a maintainer. Nothing you write is a fix.

## FILES YOU MUST READ FIRST, IN THIS ORDER
1. /home/user/ttrpg/proposals/2026-08-29-valoria-from-scratch/01_substrate.md
   *** THE SPINE. BINDING. Compose on it. Do not re-derive it, do not contradict it. If you believe
   it is wrong somewhere, say so in a clearly marked CHALLENGE section at the end - do not silently
   diverge. ***
2. .../scratchpad/SETTING.md    - the actual game content. Setting-blindness was a diagnosed failure
                                  in a prior attempt (caste, Church, Restoration, Knots appeared
                                  ZERO times in 3,793 lines). YOU MUST NAME REAL SETTING CONTENT.
3. .../scratchpad/PRECEDENT.md  - cross-game and historical ammunition: STEALS, NULLS, REFUSALS,
                                  and everything known about scale coupling. THE NULLS MATTER MOST:
                                  they tell you where you are inventing rather than adapting.
4. .../scratchpad/NERS.md       - the audit criteria you will be judged against. Design to them.
5. .../scratchpad/ARCH.md       - the modular hierarchy code architecture. BINDING.
(Absolute scratchpad path: /tmp/claude-0/-home-user-ttrpg/3e252927-aab6-508a-bc93-753009215ed9/scratchpad/)

## THE NINE THROUGHLINES — the whole brief
T1 all actions in the game are performed by characters
T2 all characters have memories, feelings and beliefs that may change over time
T3 memories are fallible, people are biased, multiple perspectives on one event
T4 no one is omniscient
T5 granular actions/demands/choices aggregate UPWARDS in scale (individual resentment coalescing
   into revolt; a town's demand filtered out as irrelevant one rung up)
T6 large actions ripple DOWNWARDS in scale (a blockade or treaty expressed as individuals getting
   excited about opportunities)
T7 events, political occurrences, clocks and gates are the basis for what gets debated, negotiated
   and argued about
T8 the world always churns - the player is not necessary for it, though they can influence it
T9 field investigations are first-class

## JORDAN'S NERS CRITERIA — design to these, you WILL be audited on them
N NECESSARY - cannot be removed without affecting EMERGENCE
E ELEGANT   - as distilled as possible WITHOUT AFFECTING FUNCTION
R ROBUST    - offers CHOICES WITH REAL IMPACTS for the player
S SMOOTH    - integrates well and PROPAGATES AS REQUIRED ACROSS SCALES
E IS A RATIO AGAINST N AND R, NOT AN INDEPENDENT AXIS. So EVERY object you introduce carries a
one-line N-STATEMENT: "cut this and you lose ___". An object that cannot name a lost emergent
possibility IS SURPLUS AND YOU MUST CUT IT YOURSELF.
R IS STRUCTURAL: A STRUCTURALLY DOMINANT OPTION IS A DESIGN FAILURE. For every player fork you
write, check the SHAPE of gain against the SHAPE of cost over time. Decaying gain against
compounding cost means one option is dominant and the fork is broken, not unbalanced.
S IS T5 AND T6: can a demand travel UP and be filtered by a person at a rung? can an opportunity
travel DOWN and reach a person WHO HOLDS NO POST?

## HARD OUTPUT DISCIPLINE
- Every object: a CLOSED LOOP stated as producer -> carrier -> consumer. If you cannot name all
  three, the object is not ready and you must say so. (A prior attempt's two worst failures were
  both well-designed stores with no writer, no channel, and no reader.)
- Every object: its N-line.
- NAME REAL SETTING CONTENT. Southern Einhir, the Masterpiece Examination, the Kettlemakers, the
  Church's four Dicasteries, the Restoration cells, Knots, cadet branches, the Baralta Crown Claim.
  Abstract examples are a failure.
- NO CI gates, NO validators, NO registries whose only consumer is process, NO ledger rows, NO
  build phases, NO migration plans. This is a GAME design document.
- NEVER special-case a named entity or a scripted outcome. Compose primitives. If you find yourself
  writing a rule that mentions one faction by name as an exception, you have failed.
- Prefer mechanism to prose. Give formulas, tables, state, and worked traces.
- Markdown. Return the FULL document as your final message.
