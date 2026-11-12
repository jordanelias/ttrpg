# DICE — the arcs' modifiers enter by the one door: a signed advantage channel, and `wounds` as its second member

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-12) — Edits A–D stand as written and are confirmed by Jordan's answer A-8 (a wound is a level against the roll, as combat spends it). The replacement proposed in `audits/10_DICE_audit_addendum_B.md` §5.4 (a wound as an obstacle term) is not built. Favourable sources stay levels and hostile situation terms go to the obstacle (A-25). The gate gains: at the largest stack of levels against, the chance is not under the per-pool floor (`U5a_DICE_owed_edits.md` §1 row 3, §3 row 11).

## Status: PROPOSED

Carries finding F-DICE-06 and §13 of `../audits/10_DICE_audit.md`. Lane: IN (the seam's advantage
binding and its roster); cross-listed to PC (the wound it reads), SC and FA (the sources that wait on
their state).

## What it changes in `engine/season/` at runtime

At the shipped arm it is a mover for a wounded person and for nobody else: a person whose `body` is below
his `body_ceiling` rolls every social roll and graded inquiry with a negative named level (the channel is
signed after this edit; today it can only add). An unwounded person's roll, and so every realm hash in
which nobody is hurt before rolling, is unchanged. The control arm (`wound_level = None`) is today's
bytes.

## The problem, with evidence

1. **The channel has one member and one sign.** `rosters.yaml: advantage_sources` holds `effort` alone
   (probe, audit §12, E-09: `('effort',)`). `sigma.py::advantage_sigma` (`:160-167`) passes one list to
   `levels_to_net_sigma`, whose second parameter (`defender`, the levels against) is never supplied, so no
   source can count against the actor.
2. **In computed play the channel sums to zero.** Realm, seed 0, 4 seasons: 284 graded rolls, leverage
   0.0 on all 284 (audit §12, E-02). The chooser forms `effort` only where a believed chance prices it
   (`decision/choose.py::settle_efforts`), and a believed opposition for a person subject is `None`
   because nothing deposits a capability claim (`sigma.py:234-238`).
3. **The provided arcs ask for exactly this channel and get none of it.** Of 973 `need:` rows in
   `engine/season/cases/`, the ones that turn on a modifier to a roll include (audit §13): a wound taken
   at personal scale persisting as a penalty on the same person's later rolls at a larger scale (ARC-53,
   core, twice); precedent correctly cited improving an advocate's odds (NPC-085, core); a third party's
   support easing a formal contest (SCN-12, important); a first exchange's result carrying a bonus into
   later exchanges of the same scene (SCN-04, important); a stacking penalty from a spent stress resource
   (SCN-04, SCN-07, core); helpers adding dice to an anchor (SCN-13, core); and successes bought before
   the roll at a fixed rate (SCN-05, core). The last is stated in a dialect the engine has retired: a
   flat bonus on the net is `resolution-diagnostic` §2's bypass 1 (its leverage scales as 1/√pool).

## The resolution, decided

Ladder step 4 (precedent) for the form, step 5 for what is built now. The tree has decided how a
modifier reaches a roll: a roster row and its binding function, returning named levels
(`rosters.yaml: advantage_sources`' note: *"A later source … is a ROW HERE plus its function … never a
flat bonus on the net and never an inline `net_boost`"*); dice are added by an addend in
`pool.py::POOL_ADDENDS`. Each arc need above is therefore one row in one of those two doors, and the
only question per need is whether the state it reads exists. One does today: `Person.body` against
`Person.body_ceiling` (`state/carriers.py:761-768`), written by `_eff_kill` and `_eff_march`. That one is
built here. The others are listed with the state they wait on; none is built ahead of its reader's
state (a source reading a field nobody writes would be a declared row read by nothing).

SCN-05's need is resolved as wrongly stated in mechanism and right in intent: a resource spent before a
roll buys named levels (as `effort` spends scene slots), never whole successes.

## The edits

**A. `engine/season/seam/wrappers/sigma.py` — the channel becomes signed.**

```python
# each source: fn(fixtures, operands) -> (levels_for, levels_against)
def advantage_sigma(fx, operands) -> float:
    for_, against = [], []
    for name in roster("advantage_sources", ordered=True):
        f, a = ADVANTAGE_SOURCES[name](fx, operands)
        for_.extend(f); against.extend(a)
    return levels_to_net_sigma(for_, against)      # the owner's own signature, both lists
```

`_effort_levels` returns `(levels, [])`. The import-time roster/binding equality check is unchanged.

**B. The `wounds` source.**

```python
def _wound_levels(fx, operands) -> tuple:
    """One named level AGAINST the actor per `wound_step` of body lost below his ceiling, capped at
    `wound_levels_max`. None at full body, and none at all when `wound_level` is None (the control)."""
    level = fx.get("wound_level")
    lost = int(operands.get("body_ceiling", 0)) - int(operands.get("body", 0))
    if level is None or lost <= 0:
        return [], []
    n = min(int(fx.get("wound_levels_max")), lost // int(fx.get("wound_step")))
    return [], [level] * n
ADVANTAGE_SOURCES = {EFFORT: _effort_levels, "wounds": _wound_levels}
```

`contest_input` (the one place operands are named) adds the actor's `body` and `body_ceiling` to the
operands it passes `_frame`; `believed_input` passes the believer's own (his body is his to know).

**C. `engine/season/rosters.yaml: advantage_sources`** gains the member `wounds`.

**D. `engine/season/data/fixtures.py`**, three fixtures, each with a hole-register row graded
`assumption` and its three-point sweep: `wound_level` (`None` control / `minor` / `moderate`; SHIPPED
`minor`), `wound_step` (a third of `condition_scale` per level: two thresholds, at one third and two
thirds lost), `wound_levels_max` (2). [ASSUMPTION; medium; Jordan to correct; revert: `wound_level`
`None`.] The soft cap (`M_MAX`) bounds the sum whatever is stacked: the loop wound → worse rolls is
capped by `wound_levels_max` and damped by `tend` and healing, which already write `body`.

**E. Not built; the door each waits at.**

| arc need | door | state it waits on | owner lane |
|---|---|---|---|
| precedent cited improves odds (NPC-085) | `advantage_sources: precedent` | a determined matter readable as precedent for a proposition (`Tenure.degree` is unproduced, H-162) | SC |
| third-party support (SCN-12) | `advantage_sources: support` | a standing commitment of support to the act's proposition | SC / FA |
| first exchange carries a bonus (SCN-04) | `advantage_sources: momentum` | a multi-exchange scene; the social roll is one draw per act | SC (proceedings) |
| stress penalty, stacking (SCN-04, SCN-07) | `advantage_sources: strain` | a per-person stress carrier; none exists | CHAR |
| helpers' dice, `floor(stat/2)` (SCN-13) | `POOL_ADDENDS` addend | a collective act naming helpers; threadwork is outside the loop | WR / FI |
| a faction's stat adds to its leader's roll (ARC-53) | `POOL_ADDENDS` addend | none by design: a faction is a resolved view with no stored stat (`queries/faction_q.py`); the need is restated as *the seat's remit or the faction's resources bring dice*, an addend over `Act.via` | FA |

## The gate (execution artifacts)

1. `wound_level = None`: `python -m engine.season.harness.headless --seasons 2 --seed 0` prints today's
   `CONTENT HASH`.
2. A hand-built world in `engine/season/tests/test_effort.py`'s fixture: the same `tell` by the same
   person at full body and at one third lost; `odds_of` reads `record_odds(2, ob, 0.0)` and
   `record_odds(2, ob, -0.25)`; the dealt distribution over 200,000 seeded rolls sits within three
   standard errors of each.
3. `python -m engine.season.harness.aperture 4 0`: the count of graded rolls with nonzero leverage,
   before and after (today 0 of 284 at seed 0).

## The falsifier

A person wounded in a `fight` at tick t who `argue`s at tick t+1 must show a lower Partial-or-better than
the control arm on the same seed; if `resolve`'s returned `leverage` is 0.0 for him, the operand never
reached the source. A source returning a level name not in `LEVEL_SIGMA` must raise `KeyError` at the
owner, never score zero.

## NERS reading (E last)

- **N.** Cut it and a wound is a number on a body that changes nothing a person does next: ARC-53's two
  core needs have no carrier. Tested vertically (a fight's outcome reaches a debate), diagonally (a
  duel's wound reaches a seat-holder's `determine`), and with no player present (a wounded lord argues
  worse whether or not anyone watches).
- **R.** A consequence that persists across scales; bounded and damped (cap, healing), so it does not
  break at its extreme. Strategic: wounding an opponent before a hearing becomes a reason to act.
- **S.** One door for every modifier, in sigma units, so each is worth the same shift at every pool
  size; signed, so a penalty and a bonus are one calculation.
- **E, as a ratio.** One roster row, one twelve-line function, three fixtures; in exchange, the channel
  the engine was built around carries something in computed play for the first time.

## Cost class

Small build (A to D). E is design-first in the lanes named.
