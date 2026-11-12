# CHAR — pessimist audit (NERS, premise, emergent narrative) of the character model and the decision layer

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: d161a61 (working tree)

Scope: `engine/season/decision/`, `engine/season/queries/person_q.py`, goals, convictions, scars,
attributes, the cast, the chooser; the NPC and AI-chooser intent as established in `02_CHAR_audit.md` §0A
and `02_CHAR_audit_addendum_B.md`; and the six premise sentences of a person. Prior work cited, not redone:
`02_CHAR_audit.md` (F-CHAR-01..15), `02_CHAR_audit_addendum_B.md`, the `02_CHAR_*` proposals,
`18_DETERMINISM_SWEEP.md`, `16_PESSIMIST_GAME.md`.

**IN PROGRESS: this head was written before the reading finished; sections are appended as they are
established. If this line is still present, the lane was interrupted and what follows is partial.**

## 0. Verdict

(pending the runs)

## The six premise sentences, in the ordinary meaning of their words (written BEFORE reading any note or code)

This is account one of three (`skills/premise-check`): what a player who knows strategy and RPG games
would take each sentence to mean. Accounts two (the code's notes) and three (the running code) follow in
§2.

| # | premise | what each link should do, in ordinary words |
|---|---|---|
| P1 | a man pursues what he wants and is stopped by what he believes | He has a want that is his own and that he can name. Given a free hand he takes the act that advances it. There is at least one act that would advance it and that he will not take because of a belief, and a man without that belief takes it. The stop has a cost he can be seen to pay (the want goes unserved), and under enough pressure the belief may give way, which is itself an event. |
| P2 | two men with different convictions choose differently in the same situation | Hold the situation fixed (same place, same options, same knowledge, same want); change only the conviction; the choices differ often enough to be noticed, in the direction the convictions' names predict (the merciful man spares, the lawful man reports). The difference is the conviction's and not the dice's: the same man re-drawn mostly chooses as himself. |
| P3 | a man changes over time because of what he does and what is done to him | What he does (kills, betrays, keeps faith, fails) and what is done to him (wounded, robbed, pardoned, bereaved) leave marks that persist, and the marks change later choices: he chooses differently after than before, in a direction the event explains. Change is not only decay; it is specific to the event. A man to whom nothing happened is unchanged. |
| P4 | a man is wrong about the world | He holds a belief about a fact (who did it, who holds the seat, how strong the garrison is, whether he is liked) that differs from the truth; he acts on the belief and not the truth; the act goes badly or strangely because of it; he can find out, and finding out changes what he does. Ignorance (not knowing) is the weaker cousin; the sentence asks for a false belief. |
| P5 | a man's reasons are readable afterwards | After the act, a record states why this man took this act rather than the other on offer: which want, which belief, which pressure, what he knew. A narrator can read it without re-running the chooser, and two different reasons produce two different records. |
| P6 | a skilled man usually beats an unskilled one | Skill is a property of the person. In any contest where it applies, the more skilled wins more than half the time, rising with the gap, never to certainty (the standing rule: no deterministic outcome); the same holds in a choice of what to attempt (the skilled man attempts what he is good at). |
