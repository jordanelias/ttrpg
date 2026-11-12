# CORE — one scene contract: a registered module is a season call and a playable scene by the same entry

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-03, C-U5a-04) — Edit 3: `decide=None` does not mean the module's own policy. It asks the decider the host builds for that person from `decision/` (sampled through `_sample_order`, never a top-score pick: `18_DETERMINISM_SWEEP.md` D-06), and a module default is the named interim until one exists; the outcome carries a typed `trace`; the closed choice tuple is exported (`11_GO_player_surface_contract_B.md` §6 rules 2–4, which govern). Edit 1's role-keyed `deciders` mapping is the one `PlayHost` shape: `05_SC_playable_hearing_B.md` edit 4 reads it. Edit 5 (the player is shown all his questions) is the register's D-62, option B; it lands on that answer and is dropped on A.

## Status: PROPOSED

Source: `audits/01_CORE_audit_addendum_B.md` F-CORE-13, §4.4, §7.1. Read at `785bc62`.

## What it changes in `engine/season/` at runtime

Nothing in an automated season: with no host, every provider makes today's call and every hash is
today's. With a host, a contest or inquiry one of whose parties the host plays hands the host's decider
to the *same* module entry — which personal combat already does. A new harness entry runs one module's
scene alone from a fixture, through the same input builder and entry the fold uses.

## The problem, with evidence

The standing requirement asks that each subsystem be playable alone and integrated, by one code path.
The path exists once. `seam/wrappers/combat.py:394-395`:

```python
if host is not None and any(c in host.persons for c in (a_id, b_id)):
    got = entry.fn(inp, random.Random(seed), decide=host.decide)
```

Same input (`combat_input`), same seed, same entry, same return; `queries/inputs.py:189`: *"Nothing
records the mode."* `seam/contest.py` passes `host` to every provider.
`seam/wrappers/mass_battle.py:361-363` accepts it and says it is not used; `sigma.py` and `fieldwork.py`
likewise. `PlayHost` is typed for combat alone (`decide: (CombatTurnView) -> str`). No instrument under
`harness/` enters a module except by running a season, so "playable alone" has no entry point for any
module, combat included.

The archived doctrine (`.designs/…/auto_manual_resolution_duality_v1.md` §8, fork A, ruled 2026-07-08;
intent only) states the shape the combat seam executes: *one engine, event-parameterised; auto is the
kernel run headless, played is the same kernel run interactively.*

## The resolution

Generalise what combat does, at the three places it is specific to combat, and add the standalone
runner. The module lanes own their choice points; this proposal owns the contract.

## Edits

### 1 · owner `engine/season/queries/inputs.py` — `PlayHost` names a decider per module role

```python
@dataclass(frozen=True)
class PlayHost:
    persons: frozenset
    deciders: Mapping[str, Callable]     # module role (`combat.fight`, `social_contest.roll`, …) -> decide(view) -> choice
    def decider_for(self, role: str) -> Optional[Callable]
```

`decide` (today's single field) becomes `deciders["combat.fight"]`; a constructor argument `decide=`
is kept for the three existing callers and maps to that key. A role with no decider is automated for
that host, so a client may play fights and leave hearings to the engine.

### 2 · owner `engine/season/seam/wrappers/_entry.py` — the party test, once

```python
def played_by(host, role: str, parties) -> Optional[Callable]:
    """The host's decider for `role` when the host plays one of `parties`, else None (AUTOMATED)."""
```

`combat.resolve` calls it in place of its inline test. `sigma.resolve`, `mass_battle.resolve` and the
fieldwork provider call it and pass the result as `decide=` to `entry.fn`. Until a module's entry
accepts `decide`, its provider passes nothing and the mode is automated: the contract lands before the
modules do, and no module is touched by this proposal.

### 3 · the module's side (owned by each module lane; stated here as the interface)

A module entry that can be played has the signature `fn(inp, rng, *, decide=None) -> outcome` and
exports, from its own package: a frozen view type (what the decider is shown: the person's own state and
what he perceives, never the opponent's true state), and a closed tuple of choices
(`modules/combat/wrapper.py::TURN_CHOICES` is the precedent). With `decide=None` the entry plays its own
policy. `decide` draws nothing, writes nothing and holds no token (`PlayHost`'s existing rule). The
witnessed fidelity the doctrine names is a decider that returns the module's own policy choice after
being shown the view: no third mode is built.

### 4 · owner new `engine/season/harness/scene.py` — a module's scene, alone

```python
def play(role: str, fixture: dict, *, seed: int = 0, decide=None, apply: bool = False) -> dict
```

`fixture` is a small world (the builders in `harness/headless.py` and `harness/scarce.py` are the
precedent) plus the act that opens the scene (actor, verb, operands). `play` constructs the world and a
driver, and either (a) `apply=False`: calls the provider `manifest.resolve` names for the act's prize
with the same arguments `_contest` passes, and returns the provider's result and the degree the one
ladder grades it at; or (b) `apply=True`: runs a one-act season with that act as an authored `choose`
return, so the fold's `writes_at(degree)` and emissions happen and the returned world carries the
consequences. Both use `host=PlayHost(persons={actor}, deciders={role: decide})` when `decide` is given.
It is an instrument; it adds no rule and reads no file a module does not already receive.

`python -m engine.season.harness.scene combat.fight --fixture duel --seed 0` is the entry point a
subsystem's standalone instructions cite.

### 5 · owner `engine/season/harness/play_surface.py` — the player sees his questions

Recorded here because it is the core's share of the design's *slate* (addendum §7.1, resolution 20).
No engine edit is needed: `View.questions` (CP-T02-07, `state/carriers.py:466-484`) already carries
every question the driver computed for the person this round, in attention order, beside the aggregated
`View.question`. What is missing is a client that shows them: `DevelopmentSheet` holds `question` only
(`decision/sheet.py:124`). The sheet gains `questions` (a tuple, copied from the view) and
`development_space` ranks for the question the player picks. The automated chooser is untouched. No
slate object is built.

## Gate (execution artifacts)

1. `harness.scene combat.fight` with `decide=None` and with a decider that echoes the module's policy
   return the same result at the same seed (the echo control, `play_surface.py:29-32`).
2. A season run with `PlayHost(deciders={})` and one with no host produce one content hash.
3. For each module that later accepts `decide`: the same two controls, and a planted deviating decider
   that moves the result.

## Falsifier

A provider that builds a different input, or draws a different seed, when a host is present (compare
`inp` and the seed across the two modes for one act). A standalone run whose result differs from the
season's result for the same act, world and seed.

## NERS reading

- **N.** Top-down, the player's request is "let me play this hearing"; bottom-up, the module needs one
  optional argument; laterally, combat already has it and the estimate functions already call the same
  builder and entry. Diagonally (a duel inside a field) it is what lets the mass-battle entry hand a
  nested fight to the same decider. Without it each lane builds its own standalone mode.
- **R.** Variety in approach and resolution is the played mode; the automated mode is the no-player
  half and is untouched.
- **S.** *Zooms in and out cleanly; pauses correctly*: the call-out is ENCOUNTER's existing one, and the
  season resumes on the decider's return. One methodology for every module.
- **E (last).** One mapping, one shared test, one runner.

## Cost class

Edits 1, 2, 5: edit. Edit 4: small build. Edit 3: each module lane's own build, design-first where the
module has no per-turn choice yet (mass battle's orders, the hearing's moves).
