# Pessimist brief — the most extensive, curious, pessimistic NERS, emergent-narrative and premise audit, of the game and of every subsystem

## Status: WORK ORDER (Jordan's direction of 2026-11-12: *"Fable 5.2 high to perform the most extensive curious pessimistic NERS audit and emergent narrative audit and premise audit across game itself and subsystems"*; not canon)

## Stance

Pessimistic and curious are one stance: assume the game does not do what its documents say, and find out
what it does instead. Try to break every claim by the cheapest observation that could. Look where nobody
looked: the second route through a mechanism, the extreme value, the seed nobody pinned, the thing that
only fires when no player is watching, the output no reader reads. A pessimist who stops at the first
failure is not curious; keep going until the failures are mapped. A steelman is still owed (what would the
best defender say), but the burden of proof is on the mechanism. Symmetric skepticism applies (CLAUDE.md
§0.1 pt 4): a control for every measurement, in either direction; a "does not work" is as much a claim
as a "works".

## The three methods (run all three on your subject; they are evidence for each other)

1. **NERS** (`CLAUDE.md` §0.06 owns the definitions; `skills/ners/SKILL.md` owns the method; for anything
   that resolves by a draw, run `skills/resolution-diagnostic/SKILL.md` and bring its findings in as
   evidence). The cut test: propose the cut and name what dies. Graded on FALSE N-LINES: cuts that turn
   out free because something already ruled in provides the lost possibility. Attack the other way too:
   mechanisms that survive because nothing was ever tried against them. N from all six directions (top-down,
   bottom-up, vertical, diagonal, lateral, horizontal); E last, as a ratio against what N and R found; R
   includes the half with no player in it and completeness at the extremes; S includes "pauses correctly"
   and "calculations consistent in methodology with siblings" (two ladders for one quantity is a defect).
2. **Premise audit** (`skills/premise-check/SKILL.md`): break each gameplay element into premise sentences
   in the ordinary meaning of their words, write what each link should do BEFORE reading any note or code,
   build the second account from the code's notes in aggregate, locate the code that owns each link, RUN
   the smallest world that exhibits the premise with controls, and compare the three accounts (ordinary
   understanding, the notes, the running code). Three questions: would a player who knows strategy/RPG
   games be surprised (genre)? does the behaviour correspond to the premise (intent)? do the results make
   sense of the words (names, parameters, levels, values)? Verdict by execution, never by reading.
3. **Emergent-narrative audit**: with no player acting, over several seeds and seasons, do persons,
   institutions and the world generate stories: beginnings, escalation, reversal, cost, an ending that is
   not an arbitrary stop, retelling (a record a narrator could read)? Use and extend the instruments
   (`harness/storybar.py`, `chronicle.py`, `arc.py`, `strife.py`, `aperture.py`, `corpus_run.py`,
   `ENDINGS_CLASSIFIED.yaml`) but treat their verdicts as claims to test (a story bar with one arm cannot
   fail; test it). Questions: what stories can this subject produce at all (enumerate from the code, not the
   docs); which does it produce in computed play (count, with seeds and controls); which are dead ends;
   what does a player's choice change in them; what is the shape of the tail (are all runs the same run);
   are the persons' reasons readable afterwards; does the story survive the subject's extremes (zero
   population, one person, a hundred factions)?

## Scope and output

Each lane takes one scope: the whole game (as a suite of engines; the seams and the loop) or one
subsystem (CORE, CHAR, PC, MB, SC, FA, SE, FI, WR, DICE, GO) or one cross-cutting subject (the verbs; the
institutions kit once it exists). Read the scope's dossier and audit and addenda and proposals and digests
(cite, do not redo), the full design set, and the code; then do NEW work: run, break, measure. Write
`audits/16_PESSIMIST_<SCOPE>.md` (verdict first; sections: NERS, Premise, Emergent narrative; findings
`F-PES-<SCOPE>-nn` ranked worst first with severity, the falsifier run and its control, the requirement(s)
touched, the minimal fix at the owner; the false N-lines found; the premises that failed; the stories that
cannot happen and the ones that can; an evidence log). Where a fix is clear, write it as a proposal
(`proposals/16_PESSIMIST_<SCOPE>_*.md`, decided, exact edits, gate); where it is a Jordan call, list the two
options. Authority and limits as `AUDIT_BRIEF.md` ("Authority granted"): proposals only; edit only your own
files; no commit; no pytest; no Bash edits of tracked files; no long `aperture` run (the machine is
loaded: short seeded probes only, `PYTHONHASHSEED=0`, scratchpad output `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_<SCOPE>/`). Write early and append.
Receipt <= 200 words: file, verdict, the five worst findings, false N-lines found, stories possible and
impossible, proposals.
