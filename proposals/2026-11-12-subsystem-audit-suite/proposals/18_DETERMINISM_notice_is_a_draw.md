# 18 · DETERMINISM · B — whether a bystander notices a deed is a draw

## Status: PROPOSED

Source: `audits/18_DETERMINISM_SWEEP.md` C-02 (ranked first by play decided). Standing rule:
`AUDIT_BRIEF.md` (Jordan, 2026-11-12). Reference only (CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime (first)

At WITNESS, a person admitted to a **deed** Event by a channel, who is neither its doer nor its
subject, deposits the deed's claims only through a notice draw; on a Partial he holds that it happened
and not who did it. Every other deposit (the doer's, the subject's, a non-deed Event's, a telling, a
document's content) is unchanged. Hash mover for every world in which a deed has a non-party witness:
all of them. Ships behind `notice_arm: off` (the control) until the gate reads.

## The problem (evidence)

- `engine/season/loop/witness.py:387-389`: `fan = [(pid, e, ch) … for pid, ch in observers_for(w, e,
  mode, everyone)]` and every pair in `fan` deposits. `epistemic.py:794-834::observers_for` admits by
  channel predicate (shipped `fan_out_mode: all_five`, `data/fixtures.py:421`) and never draws.
- Whether a man in the market saw the cutpurse, or a servant in the hall saw who struck first, could go
  either way for the people in the fiction; today it is a function of where they stood. The one draw at
  this barrier is the confiding draw (`witness.py:136`), which proves the keyed-stream shape works here.
- Reach: every belief starts at this barrier — 84,443 `claim.deposited` over seeds 0–4 × two seasons
  (`engine/season/hole_register.yaml` HR-9 controls, quoted in the `choice_temperature` row).

## The resolution, decided

Ladder step 4 (precedent: the found deposit's Partial already withholds the hand, `_found_claims`;
the confiding draw keys a per-Event stream at this barrier) and step 5.

- **Scope.** A pair `(pid, e)` draws iff `e` is a deed (`queries/person_q.py::is_deed` on the kind the
  Event deposits) and `pid` is neither `e`'s actor nor a subject of its changes. A deed is public by
  its nature only when its verb row says so: a new boolean column `public:` on `verb_table.yaml`
  (`speak`, `utter`, `issue`, `march`, `determine` … — the acts done to be seen; the verb lanes set it),
  and a `public` row's deeds deposit to the co-present without a draw (the act's publicity is the
  channel's eligibility). Default `false`.
- **Odds.** Pool = the witness's `insight` capability (SC-B3's key, `05_SC_hearing_capabilities.md`;
  until it lands, `inquiry`; else `pool_default`), read by the one pool reader `seam/wrappers/sigma.py::
  faculty`. Obstacle = `notice_ob` (fixture, proposed 1, NUMBER row, swept 0/1/2) `+ 1` if the channel
  is not the precedence head (`WITNESS_CHANNELS[0]`, presence) `+` the actor's live cover quality if
  he holds one (`conceal`'s band, `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 4) `+ 1` if
  the kind is in `rosters.yaml: covert_kinds`. Each term recorded on the deposit's `observed` as the
  reason trail.
- **The roll.** One draw through the one roller: `engine/dice_engine/sigma_leverage.roll_net` and
  `dice_engine.degree_from_net`, the two functions `modules/social_contest/roll.py::roll` composes
  (`[verify the exact signatures at landing; no new arithmetic]`), on the keyed stream
  `draw_factory(w.world_seed, lambda: w.tick)(pid, f"notice:{e.id}")` — `_circle_of`'s shape, so it
  moves no other draw.
- **Graded outcome.**

  | band | deposit |
  |---|---|
  | Failure | nothing from this Event (the person was there and did not see; a later telling can still reach him) |
  | Partial | the deed's claims with the hand withheld (the found deposit's Partial shape) — he knows it happened, not who |
  | Success | as today |
  | Overwhelming | as today, at confidence 1.0 (the `confidence_default` otherwise) |

- **Held in one place.** `epistemic.py` gains `notice(w, pid, e, ch) -> str | None` (the band, or
  `None` when the pair is out of scope); `witness.py`'s deposit loop reads it once per pair. No second
  copy of the channel precedence, no new channel.

## Exact edits, by owner

1. `engine/season/verb_table.yaml` — column `public:` (default false), validated by `data/verbs.py`.
2. `engine/season/epistemic.py` — `notice(...)` as above.
3. `engine/season/loop/witness.py` — in the fan, skip a Failure, mark a Partial for `_refract`'s
   existing withheld-hand path, raise confidence at Overwhelming.
4. `engine/season/data/fixtures.py` — `notice_ob`, `notice_arm: off | on`.
5. `engine/season/hole_register.yaml` — one row for `notice_ob` graded `assumption` with its sweep.

## Gate (execution artifacts)

1. Realm seeds 0, 1, 2, one season, `notice_arm: on`: all four bands occur among notice draws; deed
   claims deposited to non-parties fall strictly below the `off` arm and stay above 0; deposits to doers
   and subjects are equal across arms (counted per arm).
2. Odds respond to state: in a planted world, a witness holding `insight` 3 notices a `forge` more
   often over 200 seeds than one at `pool_default`, and a forger holding a Success cover is noticed
   less often than one with none; no share is 0 or 1.
3. Control: `notice_arm: off` reproduces `5ab73af282d0779646c38839fbab85d8` (seed 0, one season).

**Declared hash movers:** every world with a deed and a non-party witness at `on`.

## Falsifier

A non-party witness whose deposit is identical in both arms at every seed (the draw is not reached); a
Partial deposit that names the hand; a doer who does not know his own act.

## NERS reading

- **N**: from below, every carrier exists (channels, withheld hand, keyed stream); from above, R-07
  (imperfect knowledge) asks that people hold different things for reasons; laterally, the inquiry
  verbs already roll to find what this barrier now may miss.
- **R**: a crime can go unseen, a rumour can name the wrong man because the witness saw only that it
  happened; concealment and perception become capabilities worth having; the world keeps secrets
  without a player.
- **S**: the same roller and band ladder as every other draw; the Partial shape is the found deposit's.
- **E** (last): one function, one column, two fixtures, against the largest source of fixed outcomes in
  the game.

## Cost class

Small build. Interacts with R-07's instruments (`told_by` shares will move); report them, do not gate on
them.
