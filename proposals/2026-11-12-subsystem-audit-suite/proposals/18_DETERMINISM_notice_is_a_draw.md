# 18 · DETERMINISM · B — whether a bystander notices a deed is a draw

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13, C-U5a-14) — the roll is the one sampler (A-5: `roll_net_continuous`, not `roll_net`). The witness's pool is not read by calling `sigma.faculty` from WITNESS: it comes from a per-holder projection built at the barrier (the register's D-74, taken B: `loop/witness` is brought back to Layer 1's may-read list), at the uses-table site `notice`. A crisis of faith and an overridden scruple are deeds of a non-public kind and reach bystanders through this draw (A-24: *drawn and seen*).

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 rows notice_is_a_draw (VIOLATES as written; the `public:` column AMBIGUOUS), §2 row Odds/Exact edits, §7, 7b; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` site `notice`; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-04, D-U1-08; `unified/U3_DEPENDENCY_ORDER.md` §1 item 12, §3.1). The body now follows the head. Changed: (1) WITNESS reads no World pool: the driver builds a per-holder notice pool into the barrier cache (`queries/cache.py::notice_pools`), and `notice` reads only that map, the presence cache, the act store and the Event (04 §A.2 `:180`; D-74 B); (2) the pool and obstacle follow U1: the `notice` site's rows are `dice · inquiry · actor` and `edge · attr.mind.perception · actor · per: mid` (U1 decides `inquiry`, not R5's `insight`); the pool is the one pool rule (D-U1-08); `notice_ob` is a member of `rosters.yaml: difficulty_levels` set at calibration (D-U1-04), no whole-dice figure; the roll is the one sampler (A-5) on a keyed draw (A-30); (3) `public:` is a required, loader-validated column on every verb row, never derived from the verb's name (R5 §1 pick, U1's `capability:` precedent); (4) "the actor" is read from the act store through `e.causes` (an Event has no actor field, 04 §B.9 `:433`); (5) tests, the barrier-cache member and the initial `public:` values are named; (6) batch and tier lines.

Depends on: U1's capability block (B04: the `notice` site in `capability_use_sites`, `capability_uses` rows); `05_SC_hearing_capabilities.md` (B04); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (B07: the `conceal` cover band); the one sampler (B05) and the keyed draw (B06).
Lands in batch: B11 (lane FI), after `16_PESSIMIST_FI_C` and before `14_VERBS_SOCIAL1_A`; ships at `notice_arm: off`.
Tier: opus for the barrier-cache member and the odds (the Layer 1 placement), sonnet / high for the column, fixtures and tests.

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
  Event deposits) and `pid` is neither the doer of the act that caused `e` (read from the act store
  through `e.causes`, which WITNESS may read, 04 §A.2 `:180`; an Event carries no actor, §B.9 `:433`) nor
  a subject of its changes. A deed is public by its nature only when its verb row says so: a boolean
  column `public:` on `verb_table.yaml`, **required on every row and refused at load where absent or not
  a boolean** (`data/verbs.py`; 04 §B.13 inv. 10 admits it once the loader knows the key; never derived
  from the verb's name). Initial `true` rows: `speak`, `utter`, `issue`, `march`, `determine`,
  `convene`, `petition` [ASSUMPTION: the acts done to be seen; `convene` and `petition` added as
  sittings — basis: this file's own list; the verb lanes correct the rest]; every other row is written
  `public: false` in the landing commit. A `public` row's deeds deposit to the co-present without a draw
  (the act's publicity is the channel's eligibility).
- **Odds.** The witness's pool comes from the `notice` site of `rosters.yaml: tables.capability_uses`
  (U1's site table): `dice · inquiry · actor` (the trained score, through the one pool rule
  `sigma_leverage.pool_of`, D-U1-08; an untrained witness reads `pool_default`) and
  `edge · attr.mind.perception · actor · per: mid` (talent as levels, A-7) [ASSUMPTION; medium: noticing
  in passing is the fieldwork skill with Perception as its talent — basis: U1's site row, which the FI
  lane confirms]. **WITNESS does not compute it:** the driver builds `queries/cache.py::notice_pools(w)
  -> {pid: int}` at the barrier, beside the presence cache, through the pool helper; `notice` reads that
  map (04 §A.2 `:168`, `:180`; D-74 B). Obstacle, composed by the one obstacle composer: the task
  difficulty `notice_ob` (a member of `rosters.yaml: difficulty_levels`, sized by
  `Fixtures.difficulty_ob`, D-U1-04; its member is set at calibration, `routine` at landing
  [ASSUMPTION: the starting level — basis: OBS's control arm uses `routine`]) plus one level if the
  channel is not the precedence head (`WITNESS_CHANNELS[0]`, presence), plus the doer's live cover
  quality if he holds one (`conceal`'s band, `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 4),
  plus one level if the kind is in `rosters.yaml: covert_kinds`. Each term recorded on the deposit's
  `observed` as the reason trail (D-U1-06).
- **The roll.** One draw through the one sampler (A-5: `roll_net_continuous` and `degree_from_net`, the
  functions `modules/social_contest/roll.py::roll` composes after B05; no new arithmetic), keyed
  `H(seed, tick, pid, "notice:" + e.id)` through the one `Draw` owner (A-30; B06), so it moves no other
  draw. 04 PART D 41a's permutation test still passes: a keyed draw does not depend on deposit order.
- **Graded outcome.**

  | band | deposit |
  |---|---|
  | Failure | nothing from this Event (the person was there and did not see; a later telling can still reach him) |
  | Partial | the deed's claims with the hand withheld (the found deposit's Partial shape) — he knows it happened, not who |
  | Success | as today |
  | Overwhelming | as today, at confidence 1.0 (the `confidence_default` otherwise) |

- **Held in one place.** `epistemic.py` gains `notice(w, pid, e, ch) -> str | None` (the band, or
  `None` when the pair is out of scope), reading only `notice_pools`, the presence cache, the act store
  and the Event; `witness.py`'s deposit loop reads it once per pair. No second copy of the channel
  precedence, no new channel.

## Exact edits, by owner

1. `engine/season/verb_table.yaml` — column `public:` on every row (the seven `true` rows above, the
   rest `false`); `data/verbs.py` refuses a row without it or with a non-boolean value.
2. `engine/season/queries/cache.py` — `notice_pools(w) -> {pid: int}`, built by the driver at the
   barrier beside the presence cache (`loop/driver.py`, the barrier-cache build), through the pool
   helper for the `notice` site.
3. `engine/season/epistemic.py` — `notice(...)` as above.
4. `engine/season/loop/witness.py` — in the fan, skip a Failure, mark a Partial for `_refract`'s
   existing withheld-hand path, raise confidence at Overwhelming.
5. `engine/season/rosters.yaml` — the `notice` site in `capability_use_sites` (U1 §3 lists it) and its
   two `capability_uses` rows.
6. `engine/season/data/fixtures.py` — `notice_ob` (a `difficulty_levels` member), `notice_arm: off | on`.
7. `engine/season/hole_register.yaml` — one row for `notice_ob` graded `assumption` with its sweep (its
   id from B00's block).

## Gate (execution artifacts)

Tests: NEW `engine/season/tests/test_notice_draw.py`: `test_all_four_bands_occur`,
`test_party_deposits_equal_across_arms`, `test_inquiry_three_notices_more_often_than_default`,
`test_cover_quality_lowers_notice`, `test_arm_off_reproduces_the_pinned_hash` (seed 0, one season), and
`test_public_column_absent_is_refused_at_load` (a planted row without `public:`).

1. Realm seeds 0, 1, 2, one season, `notice_arm: on`: all four bands occur among notice draws; deed
   claims deposited to non-parties fall strictly below the `off` arm and stay above 0; deposits to doers
   and subjects are equal across arms (counted per arm).
2. Odds respond to state: in a planted world, a witness holding `inquiry` 3 notices a `forge` more
   often over 200 seeds than one at `pool_default`, and a forger holding a Success cover is noticed
   less often than one with none; no share is 0 or 1.
3. Control: `notice_arm: off` reproduces the pinned seed-0, one-season hash. At the working tree before
   B01 that hash read `5ab73af282d0779646c38839fbab85d8`; every such pin moves at B01 and at B05/B06's
   re-pins, so the test reads the pin current at B11, not this string (C3-N27's rule).
4. 04 PART D 41a's permutation test passes at `on` (deposit order does not change any band).

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
