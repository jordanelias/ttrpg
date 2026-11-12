# GO — a witness may connect what he holds: `Seen.why` is the antecedent he himself holds, by a draw

## Status: PROPOSED

Carries F-PES-GO-04 of `audits/16_PESSIMIST_GO.md` (§2.2, §2.5). Lanes IN, CHAR (the owner files are
`engine/season/epistemic.py`, `rosters.yaml`, `decision/sheet.py`); GO measured it at the player's
surface. Read at `826b747`. Reference only (`CLAUDE.md` §0.05). It closes `R8.4` in a narrower form
than `R8.4` asks: not the actor's motive, which the engine does not keep, but the link a witness is
entitled to draw between two things he has himself seen.

## What it changes in `engine/season/` at runtime

A `seen` claim's `why` term, `None` on every deposit today, is filled for some witnesses with **the
id of a claim in the witness's own ledger** that was deposited from an antecedent of the witnessed
Event. Whether a witness who holds the antecedent makes the connection is a draw. At the new
fixture's control value (`0.0`) no draw is taken and every content hash is today's; above it, `seen`
values change and the hash moves (a declared mover).

## The problem, with evidence

`probe.py base {0,1,2} 2` (`runs/PES_GO/`; control: hash equal to the automated run).

| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| `seen` claims held at the end of two seasons | 8,694 | 8,072 | 8,056 |
| … with `who` | 4,045 | 4,079 | 4,093 |
| … with `why` | **0** | **0** | **0** |
| consequence chains (cross-person depth ≥ 2) | 29 | 27 | 28 |
| … every link held, as claims, by one bystander | 23 | 20 | 22 |

The witnesses hold both ends of three chains in four. Nothing they hold says the ends are joined.
The Event has `causes[]`; the deposit cites the Event as the cause of the *deposit*
(`loop/witness.py:601-608`) and the claim carries none of it. The term exists and is declared dead:
`_term_why` "ALWAYS `None`, AND THAT IS A SCOPE DECISION" (`epistemic.py:939-950`); "NO CHANNEL
SUPPLIES `why`, AND THAT IS `R8.4`'s DEFECT … Case 4 (*no discernible reason*) is therefore every
deposit today" (`rosters.yaml:1303-1306`).

A player therefore cannot be shown "in answer to what" for anything, including for the two-link
stories the world does produce and does show him; and `harness/chronicle.py`, which can, reads the
World and the act store from outside.

## The resolution, decided

Ladder step 5, on two precedents (step 4): `Seen.who` (a term a channel supplies or withholds), and
`intent_disclosure` (H-190: "one draw keyed by the telling's own id, so no other stream moves";
`0` returns untouched and takes no draw).

### 1. What `why` holds

For a witness `pid` of Event `e`: walk `e.causes` in order, skipping `ROOT` and act ids. For the
first cause that is an Event `c` (`state/attribution.py::event_by_id`) for which `pid`'s ledger holds
a claim WITNESS deposited from `c` (the ids WITNESS itself mints: `H(seed, c.emitted_at, pid,
f"seen:{c.id}")`, else `…f"claim:{c.id}:0"`; `[ASSUMPTION; verify at build: a deposit's tick is the
Event's `emitted_at`; if not, the claim id is looked up through the `claim.deposited` Event whose
`causes[0]` is `c.id`]`), `why` is that claim's id. Otherwise `None`.

It is an id in his own ledger, so it leaks nothing: he already holds the thing it points to. It is
not a motive and does not say the later actor *decided because of* the earlier act
(`harness/chronicle.py:44-48` states the same limit for the outside reading); it says the witness
connects the two.

### 2. Who gets it, and the draw

`rosters.yaml`, `observation_terms.supplied_by`:

```
co_located:   [stratum, marks, who, why]
witness_key:  [stratum, who, why]
document_key: []            # unchanged (R8.5, ruled)
post_remit:   [stratum]     # unchanged
chronicle:    [stratum]     # unchanged
```

A channel that supplies `why` makes the witness **eligible**. Whether he connects them is one keyed
draw, `draw(pid, f"why:{e.id}")`, against a chance:

```
# data/fixtures.py
connection_chance = 0.0      # CONTROL (shipped at first landing): no draw, hash EQUAL
                             # proposed on-value 0.6, + 0.2 where his claim on the antecedent carries a `who`
```

`[ASSUMPTION; medium; Jordan to correct; revert: 0.0]`. State sets the odds (what he holds of the
antecedent); the draw decides; a well-placed witness still misses it sometimes (the standing rule).
His own act is not a draw: where `pid` is the actor (`doer` is stamped), `why` is the occasion he
acted on, with certainty, because "a person always knows his own act" (`state/carriers.py:375`) is
an eligibility fact, not an outcome. When CHAR's attributes land, the modifier is the capability
key the inquiry verbs already read (`VERB_CAPABILITY`), through the same fixture block; no second
ladder.

### 3. Where the code changes

- `epistemic.py`: the term readers take the witness (`TERM_READERS[t](w, e, act, pid)`; three of the
  four ignore it); `_term_why` returns the claim id per §1; `seen_of` takes the draw for an eligible
  witness. The docstring's "ALWAYS `None`" paragraph is replaced.
- `rosters.yaml`: the two `supplied_by` rows; the `⚠ NO CHANNEL SUPPLIES why` note replaced by what
  `why` is.
- `data/fixtures.py`: `connection_chance` and its register row.
- `decision/sheet.py::chronicle`: `Chronicle` gains `threads`, a tuple of `(claim id, why id)` for
  each `seen` claim of his whose `why` names a claim he still holds. This is the reader the term has
  lacked (a carrier with no reader is what `ID-13` refuses), and it is what SURF-B's `account` shows
  as "in answer to".

Nothing in `decision/choose.py` reads it: no choice changes. A chooser term that weighs a connected
claim is a separate design, not proposed.

## The gate (execution artifacts)

1. Control: `connection_chance = 0.0`, seeds 0–2, two seasons: every hash equal to today's
   (`bacd687f…`, `8aae8412…`, `89109213…` at `826b747`); `seen` claims with `why`: 0.
2. On-arm, same seeds: `seen` claims with `why` > 0, and **every** `why` is the id of a claim present
   in the same holder's ledger at the tick of deposit (`assert checked >= 100`, so the loop cannot
   pass by checking nothing).
3. The draw is a draw: over the eligible deposits (the witness holds an antecedent and his channel
   supplies `why`), the share that carry `why` lies inside the binomial 99% band of the fixture's
   chance, and is neither 0 nor 1.
4. The reading: for the chains of `chronicle --chains --min-depth 2`, the count whose later link is
   held by a bystander **with a `why` naming his claim on the earlier link** is printed per seed. At
   the control it is 0; on-arm it is above 0 and below the "held whole by a bystander" count (23, 20,
   22 today).
5. `chronicle(p).threads` is non-empty for at least one person per seed on-arm, and empty for all at
   the control.

## The falsifier

A `why` naming a claim the holder does not hold. A `why` on a document-channel deposit. An on-arm
run in which every eligible witness connects (the draw is decoration) or none does. A hash move at
the control.

## NERS reading (§0.06; E last)

- **N.** The cut is today's state, and what is dead is named in the audit: every reason, for every
  witness, in every seed. From the six directions: bottom-up (a term with a reader), top-down (R-07's
  memory gains a relation between memories), lateral (FI's inquiry and SC's argument both want "this
  follows from that" as a held thing), diagonal (a chain held across a settlement and a court),
  vertical (the season's chains become readable at a seat), horizontal (`who` and `why` are filled by
  one mechanism).
- **R.** The no-player half: persons who hold connected beliefs differ from persons who hold the
  same beliefs unconnected, which is material a later chooser term or a telling can use. Complete at
  the extremes: no antecedent held, no `why`; chance 0, today.
- **S.** One methodology with `who` (a supplied term) and with `intent_disclosure` (a keyed chance).
- **E.** One reader filled, two roster rows, one fixture, one tuple on `Chronicle`; no new carrier
  field (the prior lane's reason for not adding an act id to `Claim` is respected: `04` §B.9 is not
  amended).

## Cost class

Small build; hash EQUAL at the control, a declared mover when the chance is raised.
