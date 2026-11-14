# SC · DICE — the social contest as it exists, read against Jordan's six attribute roles: an interrogation

Written: 2026-11-14, stage 1 of three (1: this interrogation, read-only; 2: a redesign proposal with build instructions
and a fold map into workplan v12; 3: the plan edits). Read at the working tree of branch `exec/v12-b00-b03` on
2026-11-14 (B01 landed; B01a .01 to .04 landed: drawn attributes and the `pairs` instrument). Every claim carries a
file:line read in this session; short probes ran with `PYTHONHASHSEED=0`. Nothing here was edited outside this file.

**Jordan's rulings this reads against (verbatim, relayed 2026-11-14):** *"proceedings/social contests should be calling
in: focus as staying on topic, not being pulled away from argument into something irrelevant; reason as constructing the
argument/speech, making it logical and reasonable and evidentiary with ability to account for opponent's factual
circumstances like resources office influence etc; attunement as understanding what is most likely to rattle your
opponent or reading their intent, being able to read the room, identifying what kind of argumentation/speech is most
effective for audience adjudicator opponent; charisma as the ability to be listened to and be compelling with your
delivery; grace as acting in the correct manner for the venue and occasion, as being seen as respectable, for remaining
composed in face of difficulties and challenges; will as the ability to keep arguing your case, to believe in yourself
and remain confident, to not get rattled in first place, that 'x factor' that supports you"*; *"the subsystem needs to be
using all of these attributes in the manner that I specified"*; *"argue/speech/etc verbs should all be calling the social
contest/proceedings subsystem as they all concern influencing people"*.

**Depends on:** B01 (drawn attributes), B01a .01 to .04 (`engine/season/harness/pairs.py`), the Spirit-group ruling
(`attr.spirit.will` replaces `attr.mind.will`; new `attr.spirit.threadsensitivity`; not yet in
`references/descriptor_registry.yaml`).
**Lands in batch:** none (an interrogation; stage 2 decides the fold).

## Status: PROPOSED

Design input, reference under CLAUDE.md §0.05: it describes code, it is not a mechanism. Design documents under
`.designs/` and `proposals/` are cited for INTENT only and are labelled *reference* where cited. Lanes owning the files
it reads: SC (`modules/social_contest/`, `systems/social_contest/`), IN (`engine/season/`), DICE (`engine/dice_engine/`).

Markers: `[ASSUMPTION: ... — basis]`; `[UNVERIFIED]` for a claim not opened or not run.

