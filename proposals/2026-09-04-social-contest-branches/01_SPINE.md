# 01 · THE SPINE — one seam, one return shape, one ladder

## §0 · Status, grade, and what a PR #362 veto costs

## Status: **PROPOSED — nothing ratifies on merge.** 2026-09-04. Agonist (producer) output for the shared spine of the social-contest rebuild. Verified against the working tree at branch `claude/social-contest-system-review-dn2y5d`, HEAD `1e163ee`. **Nothing was executed:** no `pytest`, no mutation of `systems/`, `engine/`, `registers/`, `references/`, `canon/` or `CURRENT.md`. This file is the only one created.
## Consumers: `02_NEGOTIATION.md`, `03_INQUIRY.md`, `04_CONSENSUS.md`. **They consume this; they do not restate it.** Anything branch-specific is theirs and is deliberately absent here.
## Compliance target: `proposals/2026-09-03-meta-architecture/04_CODE_ARCHITECTURE.md` (PR #362, PROPOSED, HELD BACK IN FULL) — a **shape constraint, not canon**. Where its shape and the live kernel conflict, the conflict is NAMED (§3.4, §9), never resolved by declaring prose authoritative (`CLAUDE.md` §0.05).

**Paper/executes grade (`CLAUDE.md` §0.2): `paper`.** Nothing in this document runs. Every element it
specifies is an edit to code that exists and passes today; none of the edits has been made. The grade
changes only when S0's execution artifact exists (§7.1). Say `paper` out loud rather than letting a
`## Status:` line imply otherwise — that is the one claim this repository cannot satisfy by writing.

**What a PR #362 veto would cost — `00_BRANCH_SHAPES.md` §7.2 claims the spine is kernel-local and
survives. I tested that claim element by element. It is TRUE for six of eight elements and FALSE for
two**, and the two are worth naming because they are the ones a builder would otherwise assume safe.

| spine element | survives a PR #362 veto? | why |
|---|---|---|
| `WinCondition.margin()` | **yes** | six methods inside `resolver.py`; imports nothing outside the package |
| `ContestOutcome` | **yes** | a frozen dataclass in `contract.py`, which imports only `dataclasses` |
| `burden` on `PROCEEDINGS` | **yes** | a dict key in `modes.py` |
| `GAMES` deletion | **yes** | pure deletion; the thing deleted has no external caller except one test (§6.2) |
| `armature=` passthrough | **yes** | `wrapper.py` → `resolver.Bout`, both in-package |
| `rng` injection | **yes** | `sigma_leverage.roll_net` already takes `rng` (`sigma_leverage.py:269`) |
| **`contestant_from_person`** | **NO — it does not exist to be vetoed** | `PersonId`, `Person` and `person_q` are PR #362 types (`04_CODE_ARCHITECTURE.md:209 §B.2`). Nothing in `engine/` or `systems/` defines a `Person`. Under a veto this adapter has no input type and no caller; what survives is `_as_contestant` (`wrapper.py:91`), which already exists |
| **the binding-in-scene invariant (§1.9)** | **survives the veto, but its enforcement is not PR #362's to veto** — it is IN-lane, in `engine/substrate/keys.py:463 TickScheduler` | a veto of PR #362 changes nothing about it; the invariant comes from a Jordan ruling, not from the meta-architecture |

So the honest form of §7.2's claim: **the spine's six mechanical elements are kernel-local and survive;
the one new adapter is PR #362-dependent by construction and should be built last within S0**, behind
the six that are not.

---

## §1 · Verification of the shape — element by element

Method: read the anchor, then decide. Every `path:line symbol` below was opened this session. An
amendment here is a result, not a failure; the shape spec was written by a planner that executed
nothing.

**Score, with the counting rule stated so a reader can re-run it** (PR #362 `§G.3.3` — a count typed
by hand and not reproducible is worse than no count). *The unit is the eight spine elements the brief
names, plus the ruling. The verdict is the first word of each §1 subsection's verdict clause.*

| verdict | count | which |
|---|---|---|
| **CONFIRMED** outright | **3** | `GAMES` collapse (§1.6) · `armature=` passthrough (§1.7) · degree-keyed consequences on the calling verb (§1.9, re-derived) |
| **CONFIRMED WITH AMENDMENT** | **4** | `margin()` (§1.1, two amendments + the sign convention §1.2) · `ContestOutcome` (§1.4, two) · `contestant_from_person` (§2 A10 — confirmed as a shape, **downgraded** because it has no producer) · `KEY_TYPE_BY_SCENE` (§2 A11 — confirmed, with a missing second half that is a crash) |
| **REFUTED as specified** | **2** | `degree_from_net(margin, ob=0)` — the six margins are incommensurable (§1.3) · `rng` on `roll_net` alone — three draw sites, not one (§1.8) |
| **PARTLY REFUTED** | **1** | `burden` — right as a field, wrong as an S0 selector (§1.5) |
| **ADDED** | **1** | the binding-in-scene invariant (§1.9, Jordan 2026-09-04) |

One further refutation is not a shape element and is counted separately: **my own claim that the
ruling conflicts with PR #362 — refuted in §3.4 (iii).**

### §1.1 `WinCondition.margin(state) -> float` — **CONFIRMED WITH TWO AMENDMENTS, one of them severe**

`resolver.py:52 WinCondition` is an ABC with one method, `resolve(self, s, closing, adj=None)`
(`:53`). Six subclasses, not five — the shape spec groups `ThresholdRace`/`TallyAtClose`, which is
fine, but a builder should be told the number: `ThresholdRace:54`, `TallyAtClose:62`, `ProofBar:67`,
`GraceThreshold:74`, `PersuasionTrack:81`, `VoteAtClose:98`.

Per-subclass formulas, checked against the actual `resolve()`:

| class | shape spec says | verdict |
|---|---|---|
| `TallyAtClose:62` | `adv[A] − adv[B]` | **CONFIRMED.** `:66` is exactly `A if a > b else B if b > a else "draw"` |
| `ThresholdRace:54` | `adv[A] − adv[B]` | **CONFIRMED, with a named consequence.** The closing branch (`:60`) is the same comparison, but the *early* branch (`:58-59`) fires on `a >= self.T and a > b` — so a race can be won at a lead of 0.01 once `T` is crossed. `adv[A] − adv[B]` drops `T` entirely, and such a win reads as a `Partial`. That is defensible ("you won, barely") but it is a behaviour statement, not a transcription, and it must be recorded as one |
| `ProofBar:67` | `net − bar` | **CONFIRMED as a magnitude, REFUTED as a signed value** — see §1.2 |
| `GraceThreshold:74` | `adv[pet] − bar` | same — **CONFIRMED as a magnitude, REFUTED as a signed value** (§1.2) |
| `PersuasionTrack:81` | `track − start` | **CONFIRMED, and it is not the ±5 the spec claims** — see below |
| `VoteAtClose:98` | weighted share − 0.5 | **CONFIRMED as a sign, and it is where the unit defect bites hardest** — see §1.3 |

**Amendment A — `PersuasionTrack`'s margin is NOT `−5..+5`.** `track()` (`:87`) is
`max(0.0, min(10.0, start + scale*(adv[A]−adv[B])))` — clamped to `[0,10]` *absolutely*, not
relative to `start`. Measured (read-only probe, reproduced below): at `start=5.0` the margin range is
`[−5.0, +5.0]`; at `start=6.0` — `church_tribunal`, `modes.py:476 CHURCH_TRIBUNAL_TRACK_START` — it is
`[−6.0, +4.0]`. The asymmetry is the accused's handicap and is *correct*, but the shape spec's
"closing the −5..+5 vs 0–10 scale collision" overstates it: the collision closes for the neutral start
and becomes an asymmetric range for the biased one. State the range as `[−start, 10−start]`.

```
python3 -c "
from systems.social_contest.sim.contest.resolver import PersuasionTrack, ContestState
from systems.social_contest.sim.contest.contract import A,B
for st in (5.0,6.0):
    p=PersuasionTrack(start=st); s=ContestState()
    s.adv[A]=100; s.adv[B]=0; hi=p.track(s)-st
    s.adv[A]=0; s.adv[B]=100; lo=p.track(s)-st
    print(st, lo, hi)"
```

### §1.2 **AMENDMENT — the shape spec never states the SIGN CONVENTION, and two subclasses invert it**

`ProofBar.__init__(self, bar, challenger=A)` (`:68`) and
`GraceThreshold.__init__(self, bar, petitioner=A)` (`:75`) both take a **configurable side**. Live
instances prove it is used: `modes.py:182-196 inquisition_hearing_venue` builds `ProofBar(bar=2.5)`
with the inquisitor as A; nothing prevents `challenger=B`. Under the spec's literal formula
`net − bar` where `net = adv[ch] − adv[df]` (`:70`), a `ProofBar(challenger=B)` produces a **positive**
margin when **B** prevails, while every other subclass produces a positive margin when **A** prevails.

That is a silent sign inversion at a seam whose entire contract is "the sign is the winner". A caller
cannot detect it.

**Ruled here by architecture (`CLAUDE.md` §0 five-test rung 5 — one option is clearly right and there
is no competing reading):**

> **`margin()` is ALWAYS oriented A-positive.** Positive means side `A` (`contract.py:7`) prevails;
> negative means `B`; zero is a draw. A win condition that internally favours a configured side
> multiplies by `+1 if that side is A else −1` inside its own `margin()`.

This is one line per affected subclass and one falsifier (F-S2, §7.2). It is not a design choice; the
alternative is a seam that lies about its own sign for one venue family.

### §1.3 **REFUTATION — `degree = degree_from_net(margin, ob=0)` DOES NOT WORK. The six margins are on incommensurable scales.**

This is the largest defect I found, and it invalidates `00_BRANCH_SHAPES.md` §2.1's seam pseudocode as
written.

`dice_engine.degree_from_net` (`engine/autoload/dice_engine.py:227`) reads `margin = net − ob` in
**units of whole d10 successes**: `>= 3` Overwhelming, `>= 1` Success, `[0,1)` Partial, `< 0` Failure
(`:279-294`). The six win conditions return margins in six unrelated units:

| win condition | margin unit | reachable magnitude | `degree_from_net(margin, 0)` |
|---|---|---|---|
| `TallyAtClose` / `ThresholdRace` | accumulated `adv`, `MERIT_SCALE = 2.6` per landed move (`resolver.py:39`, `:334`) over up to `venue.budget` exchanges | tens | Overwhelming on almost any win |
| `PersuasionTrack` | track points, `scale = 1.5` (`:86`) | `[−start, 10−start]` | plausible: Overwhelming at margin ≥ 3 |
| `ProofBar` / `GraceThreshold` | `adv` less a venue bar (2.0–8.0 across `modes.py`) | units of `adv` | as row 1 |
| `VoteAtClose` | a **vote share**, `wA/total − 0.5` (`:139-142`) | **`[−0.5, +0.5]`** | **`Partial` at the theoretical maximum. A unanimous 7–0 verdict bands as PARTIAL.** |

Measured band-vs-ladder disagreement inside the *one* condition that is nominally compatible
(`PersuasionTrack`, `start=5.0`): margin `1.0` is `committee` by band and `SUCCESS` by ladder; margin
`3.0` is `A_decisive` by band and `OVERWHELMING` by ladder. The two answers are not the same answer,
and at `start=6.0` the disagreement moves.

**What the spine must specify instead.** `margin()` returns a signed, A-positive scalar **already
expressed in success units** — each subclass owns the conversion because each subclass owns its unit.
One method, six implementations, no new module, no new type; the meta-rule (`14_NERS.md` §1: *a fix
that adds a system has failed*) is respected.

**Every conversion constant is a `[SEED]`.** The research licenses none of them
(`rhetoric_oratory_contest_research.md` §9.7: structure, never numbers), no design document supplies
one, and this document refuses to invent one. What it does supply is the *measurement* that sets them
— `tools/balance_oracle.py` (built 2026-08-21, 240 campaigns, deliberately not a CI gate; `CLAUDE.md`
§7). The builder's obligation is to ship them tagged `[SEED]` and to say in the same commit that they
are uncalibrated, exactly as `resolver.py:39-44` already does for `MERIT_SCALE`/`JITTER`.

⚠ **This does not close ED-SC-0002.** ED-SC-0002 (resolved 2026-07-08) ruled *composed keying* — the
band gates magnitude, the genre selects the channel. That ruling is about the **echo**, not about the
degree ladder, and it is preserved: §1.4 keeps the band.

### §1.4 `ContestOutcome(margin, reason, veto, beats)` — **CONFIRMED WITH TWO AMENDMENTS**

`00_BRANCH_SHAPES.md` §1 defect 3 is **CONFIRMED**: `wrapper.py:254-259` says "TWO RETURN SHAPES, not
one"; `_resolve_agon:217` returns `(bout.resolve(...), bout)` = `((winner, reason), bout)`;
`_stub:227` returns a bare `stubwire.StubResult`; and `scene_dispatch.py:301` unpacks a 2-tuple
unconditionally, so a stub game reaching production would raise.

**Amendment A — `veto` cannot be a bool here.** `Bout.resolve` (`resolver.py:439-441` in the
`resolve` body) returns `(other(loser), f"clinch:{reason}...")` on a fault-out. **The clinch winner is
not derivable from `adv`** — a side can fault out while leading. A boolean `veto` therefore destroys
the information the current return shape carries, and the seeded goldens would move on any campaign
in which a clinch fires. PR #362 §C.5's `veto : bool` is written for a seam invoked *by an actor* —
`kill / wound` (`verb_table.yaml:234`), where "who" is the acting Person. **The contest seam has two
claimants and no actor**, so the field must name the faulting side:

```python
veto: str | None      # contract.A | contract.B — the side whose FAULT ended the bout; None otherwise.
                      # Demote-only, per PR#362 §C.5: a veto can make the vetoed side's degree worse
                      # and can never improve it.
```

**Amendment B — `ContestOutcome` must be a strict SUPERSET of today's tuple, and that is what makes
S0 controllable.** Add `band: str | None` carrying `WinCondition.resolve()`'s output **verbatim**.
Then `scene_dispatch.py:308-309` reconstructs its `out["result"]` dict byte-identically, the
`verdict == composition.require('contest_side.a')` comparison at `:337` is unchanged, the emitted
`Key` payload (`echo_transport.py:434-438`) is unchanged, and **the two campaign goldens cannot move —
which is what makes them a real control rather than a decorative one** (§7.1).

`band` is a winner, and PR #362 §C.5 says *"a subsystem returning a winner has not met the contract"*.
**That conflict is real and is not resolved here.** It is graded and dispositioned in §3.4: `band` is
a legibility field with one production consumer and a deletion date (when `scene_dispatch` is
converted to read `margin`), not a permanent part of the contract.

The final shape, complete and typed:

```python
# systems/social_contest/sim/contest/contract.py  (this file imports only `dataclasses`)
@dataclass(frozen=True)
class ContestOutcome:
    """The ONE thing a resolved contest returns. Never a winner; the sign of `margin` is the winner.

    `margin`  signed, A-POSITIVE, in whole-d10-SUCCESS units (resolver.WinCondition.margin).
    `reason`  'win' | 'draw' | 'clinch:<family> - <detail>'  — Bout.resolve's string, verbatim.
    `veto`    contract.A | contract.B | None — the side that faulted out. Demote-only.
    `band`    WinCondition.resolve()'s own output, verbatim. LEGIBILITY ONLY (§3.4); slated for
              deletion once scene_dispatch reads `margin`.
    `beats`   Bout.log when record=True, else ().  Consumed by narrative.summarize.
    """
    margin: float
    reason: str
    veto: str | None = None
    band: str | None = None
    beats: tuple = ()
```

⚠ **Naming collision, ruled here (`CLAUDE.md` §4, *idempotent in meaning*).**
`narrative.py:44 Chronicle.margin` is a **different quantity** — `|advA−advB| / (advA+advB)` at
close, in `[0,1]`, a normalised share, with three `[SEED]` thresholds at `narrative.py:30-32`. Two
fields called `margin` meaning two things is exactly the failure `§4` was written against. **The
spine keeps `ContestOutcome.margin`; `Chronicle.margin` is renamed `Chronicle.share`** in the same
commit (a 6-site rename inside one file: `:44`, `:55`, `:96`, `:98`, and two `render()` reads). This
is a rename, not a mechanism change.

### §1.5 `burden ∈ {ACCUSER, RESPONDENT, LOWER_STANDING, NONE}` on `PROCEEDINGS` — **CONFIRMED AS A FIELD, REFUTED AS AN S0 SELECTOR**

The field is right and the ED-SC-0020 reasoning is right. **The claim that it *selects* the
`WinCondition` in S0 is wrong, and shipping it that way would move dozens of pinned checks.**

Measured against `modes.py:485-519 PROCEEDINGS`: **not one of the eight canonical proceedings uses
`ProofBar`, `GraceThreshold` or `ThresholdRace`.** Six resolve to `PersuasionTrack` or `TallyAtClose`
via `_use_tracker` (`:521-534`) and one (`guild_arbitration`) to `VoteAtClose` via the panel branch
(`:553-555`). `ProofBar`/`GraceThreshold`/`ThresholdRace` exist **only** in the `VENUES` /
`INSTITUTIONAL_MODES` / `CROSS_CULTURAL_VENUES` factories (`:69`, `:72`, `:82`, `:140`, `:196`,
`:215`, `:237`, `:277`), none of which any canonical proceeding names.

So `burden` *selecting* the win condition flips `church_tribunal` from `PersuasionTrack(start=6.0)` to
`ProofBar` at S0 — a behaviour change, in the proceeding with the most pinned kernel checks
(`_kernel_tests.py` sections 33, and `:1387-1430`, the Gate-C CR4 reachability block). **Split it:**

- **S0 adds `burden` as declared metadata** on all eight rows, plus a kernel check asserting the
  declared burden is *consistent with* the win condition already selected (`ACCUSER` ⇒ the venue's
  `win` is burden-bearing; `NONE` ⇒ it is not). Additive; value-identical.
- **S1 (inquiry) flips `church_tribunal` to burden-selection** with its own control, because that is
  the branch whose whole content is *silence convicts* and whose falsifiers can observe the change.

**Does this close ED-SC-0020? Partly, and I will say which part.** The five tests, run in order:
(1) *superseded* — no successor ruling exists. (2) *irrelevant* — no; the subject is live.
(3) *answered by a design document* — no; `social_contest_v30.md` describes proceedings, not burdens.
(4) *answered by precedent* — **yes for the taxonomy**: `ProofBar`'s own closing branch (`:71-72`,
`if closing: return df`) *already implements* Fork A's stall semantics — whoever holds the burden
loses on a stall — so the mechanism Fork A proposes to add already exists under another name.
(5) *answered by architecture* — **yes for adoption**: one ladder + one Margin (§1.3) leaves no room
for four parallel win-condition taxonomies. **So ED-SC-0020 closes on rungs 4 and 5 and should be
marked `resolved`, citing this section.** What does **not** close by architecture is *which burden
each of the eight rows carries* — that is eight design assignments, and I decline to invent them here
because seven of the eight belong to branch documents that are being written concurrently. That is
not an escalation; it is a work item with a named owner.

### §1.6 `GAMES` collapses into `PROCEEDINGS` — **CONFIRMED**

`wrapper.py:236-245 GAMES`; `resolve_contest(contest, *, game="agon", ...)` at `:248`; the only
production caller passes nothing (`scene_dispatch.py:301`). Defect 2 confirmed. The deletion is
clean and is the point: `GAMES` (10 lines), `_stub` (15 lines), the `game=` parameter and its
validation (`:260-261`), `Contest.game` (a field hardcoded to `"agon"` at `:193` and read nowhere
outside the constructor — grep-verified), three `MECHANICS` rows (`:372-374`), the
`from engine.substrate import stubwire` import at `:23` (its only use is `_stub`), and the `"GAMES"`
entries in `__init__.py:73` and `:119`.

### §1.7 `armature=` passthrough — **CONFIRMED**

`build_contest` (`wrapper.py:110-111`) takes
`(side_a, side_b, *, venue, adjudicator=None, stakes=None, world=None, use_tracker=None, degree_extension=CONTEST_DEGREE_EXTENSION)`
— **no `armature`**. `_resolve_agon:215-216` constructs `Bout(...)` without one. `Bout.__init__`
(`resolver.py:239-240`) accepts `armature=None`. The self-test that "proves" the armature is live
(`wrapper.py:377 _stage3_resolution_invocation_check`) builds its own `Bout(..., armature=ac)` at
`:412` and `:423`, i.e. **the green self-check bypasses the seam it is supposed to vouch for.**
`agon_harness.py:71-76` names the same gap as "WORKAROUND 3" and has zero callers. Confirmed.

The derivation is confirmed too: `armature.py:374 position_of(adjudicator, *, opponent_is_adjudicator=False, armature_positions=None)`
returns `ArmaturePosition.zero()` when the flag is set (`:389-390`), and `ArmatureConfig.opponent_is_adjudicator`
(`:430`) is the carrier. The two asymmetric role strings are `"crown_objects"` (`modes.py:493`) and
`"inquisitor_proposes"` (`:496`). Deriving the flag from `PROCEEDINGS[name]["roles"]` rather than
letting a caller pass it is right and is a **gate-off, not a flag**: a caller cannot switch
double-counting back on.

### §1.8 `rng` injection — **CONFIRMED AS NECESSARY, REFUTED AS SPECIFIED. It names one draw site of three.**

`scene_dispatch.py:297-303` does a save/seed/restore dance on the global `random` module, and its own
comment (`:291-296`) explains why: the kernel draws from the module-level stream. Retiring it is
right.

But `00_BRANCH_SHAPES.md` §2.1 says only *"`resolver.py:28 roll_net` takes `rng`"*. Grepped
(`grep -n "random\." resolver.py`) — there are **three** draw sites, in two different classes:

| site | draw | reachable from |
|---|---|---|
| `resolver.py:32` (inside `roll_net`) | `_sigma.roll_net(pool, rng=random)` | `_reception` → every argue move |
| `resolver.py:334` | `random.uniform(1 - JITTER, 1 + JITTER)` | `_advance` → **every** scoring event, including evidence |
| `resolver.py:139` and `:144` | `random.gauss(0, self.noise)` ×2 | `VoteAtClose.resolve` — **the production proceeding's win condition** (`guild_arbitration` → panel → `VoteAtClose`) |

Threading `rng` into `roll_net` alone leaves `_advance`'s jitter and the entire ballot on the global
stream, so the reseed at `scene_dispatch.py:299` **could not be retired** and the claim "the spine
retires the global reseed" would be false. The third row is the awkward one: `VoteAtClose` is a
`WinCondition`, and `WinCondition.resolve(self, s, closing, adj=None)` has no rng parameter.

**Specified:**

```python
class WinCondition:
    def resolve(self, s, closing, adj=None, rng=None): ...   # rng=None => module `random` (unchanged)
    def margin(self, s, adj=None, rng=None) -> float: ...    # A-positive, success units (§1.1-§1.3)

def roll_net(pool, rng=None):                                # resolver.py:28
    return _sigma.roll_net(pool, rng=rng if rng is not None else random)

class Bout:
    def __init__(self, ca, cb, venue, adjudicator=None, record=False, armature=None,
                 degree_extension=_DEFAULT_DEGREE_EXTENSION,
                 rng: "random.Random | None" = None): ...
    # self._rng = rng; every draw site reads `self._rng or random`
```

`rng=None` preserving the module stream is what keeps the 389 seeded kernel checks and both campaign
goldens green — the default is the control.

⚠ **`sigma_leverage.roll_net` already takes `rng`** (`engine/autoload/sigma_leverage.py:269`), so no
engine change is needed for row 1. Rows 2 and 3 are entirely inside `resolver.py`.

### §1.9 ⚠ **ADDED — THE BINDING-IN-SCENE INVARIANT (Jordan, ruled 2026-09-04, mid-session)**

> **Verbatim: *"negotiated agreement bind in scene. in fact, everything that occurs within a scene
> should bind or else it's as if time doesn't exist within a season."***

The escalation came from negotiation; the second sentence generalises it to scene resolution, which
is the spine's territory. It is stated here **once** so the three branch documents consume it rather
than restating it three times.

**It has two halves, and they have different owners and different grades.**

**(a) BINDING AS COMMITMENT — the outcome is settled at return.** No second consent act, no
ratification step, no "agreed, pending". Owner: **SC, this document.**

> **I-S6a.** `ContestOutcome` has **no field that can represent a not-yet-effective outcome.** There
> is no `pending`, no `provisional`, no `awaiting_ratification`, no `parties_agreed` bitmask, and the
> seam returns exactly one value.
>
> **Grade: STRUCTURAL.** The defect has no spelling — a frozen dataclass with five declared fields
> cannot express deferral, and adding a sixth is a visible edit to the contract. This is the strong
> grade honestly earned, and it is earned by an *absence*, which is the only way §0's rule allows a
> STRUCTURAL claim in an unchecked Python build.

**(b) BINDING AS EFFECT — the outcome is in force for everything that happens after it in the same
season.** This is the half the rationale sentence is about, and **the tree currently does the
opposite.** Owner: **IN lane** — `engine/substrate/keys.py:463 TickScheduler`.

> **I-S6b.** A scene's resolved consequence is applied before the next scene in the same season
> resolves.
>
> **Grade today: NOT ENFORCED, and actively contradicted by a passing test.** Not CONVENTION —
> weaker than that. Stating it as CONVENTION would be the "guard that cannot observe what it guards"
> defect (`04_CODE_ARCHITECTURE.md:78`) wearing a better label.

**The mechanism, traced (this is the part that makes the ruling concrete rather than rhetorical):**

1. `engine/cross_scale/scene_dispatch.py:402-414 dispatch_scenes` drains the **entire** slate in one
   `while scene_slate.pending_count() > 0` loop, inside one action phase. **Multiple scenes resolve
   in sequence within a single season.**
2. Each resolved contest emits its Key through `echo_transport.emit_scene_echo` (`:393`), which calls
   `sched.emit(key, apply=_apply)` — and `TickScheduler._emit_at_depth` (`keys.py:569-573`) appends
   `_apply` to `_pending_apply` instead of running it, because `defer_apply` is on and the phase is
   `_PHASE_ACTION` (OF-7).
3. The queued applies run only at `accounting_boundary()` (`keys.py:581-591`), which
   `engine/autoload/engine_clock.py:122` calls **after the whole action phase closes**.
4. Therefore **scene 2 of season N reads the faction stats as they stood before scene 1 resolved.**
   That is, exactly, *"as if time doesn't exist within a season"* — and it is not hypothetical:
   `scene_dispatch.py:139 _emergency_council_parties` derives both contest sides from `f.L` and
   `f.Sta`, the very stats an earlier contest's echo moves.

**The inconsistency already exists inside this one subsystem, which is the precedent that settles the
direction.** `parliamentary_bridge.py:155` states it in its own words: *"The §10 loser Mandate penalty
is applied inside `run_parliamentary_vote`; the winner echo is emitted (deferred) here."* The penalty
binds immediately (`parliamentary_vote.py:214`, a direct `Faction.adjust`); the reward defers. One
procedure, two timings. Jordan's ruling resolves it toward the immediate one.

**What S0 does about it.** SC cannot land (b) — the owner is `engine/substrate/keys.py`. S0's
obligation is to (i) state the invariant, (ii) not make it worse, and (iii) ship the falsifier that
observes the failure (§7.4), which will **fail on the current tree**. An `xfail` with the ruling
cited is the honest form; a skip is not, because a skip cannot observe anything.

**The minimal IN-lane change, named so it is not hand-waved:** `TickScheduler.emit` grows a per-key
`bind_now: bool = False`, and `_emit_at_depth` (`keys.py:569-573`) runs `apply(key)` immediately when
it is set, bypassing `_pending_apply`. Per-key rather than a global flag flip, because §5.5 Accord and
§5.2 Domain Echo have different owners and four live tests pin the Accord deferral
(`engine/tests/test_accord_echo.py:152-228`). `echo_transport.emit_scene_echo` then passes
`bind_now=True` for `scene.*_resolved` keys. **That is one parameter and one branch — it adds no
system**, which is what the meta-rule asks.

**Does the ruling change my change list?** Re-derived rather than assumed:

- `ContestOutcome`'s contract: **yes** — I-S6a is now a stated invariant on it (the absence above),
  and it removes an option a branch author might otherwise have reached for. No field is added.
- The degree-keyed consequence column on the calling verb: **no change in shape.** `writes_at(degree)`
  (`04_CODE_ARCHITECTURE.md:584`) is already a per-degree list; the ruling constrains **when** those
  writes take effect, not what they are.
- Where the write lands relative to the gate: **no change to the gate; a change to what happens after
  it.** In PR #362's shape the gate applies the write synchronously (`:536`, *"THE GATE APPLIES THE
  WRITE"*), so a PR #362 build satisfies (b) natively. It is the **current** engine — OF-7 — that
  does not. **The ruling and PR #362's write gate agree; the live tree disagrees with both.**
- **What the write IS, and this is the constraint the negotiation branch inherits:** a mutual outcome
  is recorded as a **`Record`**, not as per-claimant `commit` Tenures. That is what lets one act bind
  both parties inside one RESOLVE without touching `AX-4`. **Fully derived in §3.4 (iii)**, which also
  retracts an earlier draft of this document that claimed PR #362 had to be amended. It does not.

**The cost of removing the deferral window, stated rather than hidden.**

| cost | measured verdict |
|---|---|
| Intra-season **scene order becomes load-bearing** — `scene_slate.next_scene()` (`scene_slate.py:46-50`) is a FIFO `popleft` over a module-level deque, so the order is the queueing order and now feeds balance | **REAL and unavoidable.** It is also the point: an order that does not matter is the absence of time |
| **Re-entrancy / cascade risk** — an immediate apply firing a trigger that queues a scene inside the drain loop | **DOES NOT ARISE TODAY.** `queue_scene` has exactly one caller in the whole tree, `queue_triggered_scenes` (`scene_dispatch.py:106`), and `run_scene_phase:421-422` runs it *before* `dispatch_scenes`. Verified by grep. The `TickScheduler` cascade cap (`keys.py:556-565`) remains the backstop if that ever changes |
| **Goldens move** for any seeded campaign that resolves ≥2 scenes in a season affecting the same faction | **REAL, and it is a re-pin, not a regression** — but it must be done deliberately, with the delta measured and stated (`CLAUDE.md` §0.1 pt 4), never as a silent re-record |
| **Four live tests pin the deferral**: `engine/tests/test_echo_transport.py:107 test_echo_apply_is_deferred_to_accounting_boundary`, and `test_accord_echo.py:152/193/211/228` | **REAL.** The first is directly about the contest echo and must be **narrowed or inverted** by whoever lands (b). The other three are the §5.5 Accord leg (settlement Order), a different write with a different owner — the ruling reaches them by its own words, but the disposition is SE/IN's, not this document's |
| Loss of "one place where stats move" as a debugging property | **REAL but small.** `Faction.adjust` (`engine/autoload/game_state.py:153`) is still the single owner of the write; only its *timing* changes |

---

## §2 · The change list

Ordered so a builder can follow it top to bottom. **Additions: 11. Deletions: 9. Rewrites: 6.**
Every deletion is load-bearing — the NERS benchmark is that the vocabulary gets shorter, and it does:
`GAMES`, `game=`, `_stub`, `Contest.game`, three `MECHANICS` rows, one import, four kernel checks out;
one dataclass, one method per win condition, three parameters and one adapter in.

### D — DELETIONS (do these first; they make the additions smaller)

**D1 · `wrapper.py:236-245` — delete `GAMES`.**
```python
GAMES = {
    "agon":        {"resolve": _resolve_agon,          "status": "WIRED", "source": "..."},
    "consensus":   {"resolve": _stub("consensus"),     "status": "STUB",  "source": "..."},
    "negotiation": {"resolve": _stub("negotiation"),   "status": "STUB",  "source": "..."},
    "inquiry":     {"resolve": _stub("inquiry"),       "status": "STUB",  "source": "..."},
}
```
→ *(nothing)*. Why: a four-row router with one wired row and one caller that never uses the parameter
is a switch that does not switch. The proceeding already carries everything the four rows claimed to
distinguish.

**D2 · `wrapper.py:220-234` — delete `_stub`** (the whole factory, including its `stubwire.stub_resolve`
call at `:227`). Why: it exists only to populate D1's three rows.

**D3 · `wrapper.py:23` — delete `from engine.substrate import stubwire`.** Grep-verified: `stubwire`
appears in `wrapper.py` only at `:23` and `:227`. Why: an unused import of a stub primitive reads as
"this module has stubs".

**D4 · `wrapper.py:248` — delete the `game=` parameter and its validation at `:260-261`.**
```python
def resolve_contest(contest, *, game="agon", policy_a=logos_spammer, policy_b=logos_spammer, record=False):
    if game not in GAMES:
        raise ValueError(f"resolve_contest: unknown game {game!r}; valid: {sorted(GAMES)}")
    ...
    return GAMES[game]["resolve"](contest, policy_a=pa, policy_b=pb, record=record)
```
→
```python
def resolve_contest(contest, *, policy_a=logos_spammer, policy_b=logos_spammer,
                    record=False, rng=None) -> "ContestOutcome":
    pa = POLICIES[policy_a] if isinstance(policy_a, str) else policy_a
    pb = POLICIES[policy_b] if isinstance(policy_b, str) else policy_b
    return _resolve(contest, policy_a=pa, policy_b=pb, record=record, rng=rng)
```
Why: this is defect 2 closing by deletion.

**D5 · `wrapper.py:64-88` — delete the `game` parameter and `self.game` from `Contest.__init__`,** and
the `game="agon"` argument at `:193`. Why: hardcoded at the one construction site, read nowhere else
(grep-verified). A field with one writer and no reader.

**D6 · `wrapper.py:372-374` — delete the three STUB `MECHANICS` rows** (`consensus_game`,
`negotiation_game`, `inquiry_game`, each `"fn": None`). Why: `mechanics_selftest` (`:443-444`) already
excludes `fn=None` rows, so they assert nothing.

**D7 · `systems/social_contest/sim/contest/__init__.py:73` and `:119` — remove `GAMES`.**

**D8 · `_kernel_tests.py:696-703` — delete four checks** (the `GAMES table:` check at `:696-697`, and
the three-iteration stub loop at `:700-703`). Why: they pin a table that no longer exists.
**`_KERNEL_EXPECTED` arithmetic: −4 from here.** Keep `from engine.substrate.stubwire import StubResult`
at `:9` — still used at `:444` and `:1095`.

**D9 · `engine/tests/test_pipeline_reach.py:826-844` — delete `_OI18A_GAMES_ROWS` and
`test_oi18a_contest_games_router_stub_rows_are_self_flagged`.** ⚠ **This test is not in
`00_BRANCH_SHAPES.md`'s blast radius and it reads `wrapper.GAMES[g]["resolve"](None)` directly at
`:838` — it fails the moment D1 lands.** Delete rather than update: the contract it guards
("the stub rows self-flag") ceases to have a subject. Leave
`test_oi18a_mode_scaffolds_are_self_flagged` (`:847`) alone — the three `modes.py` scaffolds are
untouched by the spine and are the branch authors' material.

### A — ADDITIONS

**A1 · `contract.py` — add `ContestOutcome`** (full text in §1.4). Why: one return shape. **Home
chosen deliberately:** `contract.py` "depends on nothing else in the package" (`:2-3`) and imports
only `dataclasses`, so this adds no import edge and cannot enlarge the tolerated import cycle (§6.1).

**A2 · `resolver.py:52-53` — add `margin()` to the ABC and a `rng` parameter to both methods.**
```python
class WinCondition:
    def resolve(self, s, closing, adj=None): raise NotImplementedError
```
→
```python
class WinCondition:
    #: Units the subclass's raw lead is measured in, per ONE whole d10 success. [SEED] — see §1.3.
    #: Uncalibrated; set by measurement (tools/balance_oracle.py), not by argument.
    SUCCESS_UNIT: float = 1.0

    def resolve(self, s, closing, adj=None, rng=None): raise NotImplementedError

    def margin(self, s, adj=None, rng=None) -> float:
        """Signed, A-POSITIVE, in whole-d10-SUCCESS units. Positive => side A prevails.

        NEVER a winner: a caller reads the sign, and the seam reads the magnitude through the
        ONE ladder (engine/autoload/dice_engine.py:227). A subclass whose internal favoured side
        is configurable MUST orient here (§1.2) — a seam whose sign inverts per venue is a seam
        that lies.
        """
        raise NotImplementedError
```
Why: this is the whole spine in one method. Without it every branch invents its own degree and four
resolvers become seven.

**A3 · six `margin()` implementations.** Each is one or two lines; each divides by its own
`SUCCESS_UNIT`; each `SUCCESS_UNIT` ships tagged `[SEED]`.

| class | body (before the `/ SUCCESS_UNIT`) | orientation |
|---|---|---|
| `ThresholdRace:54` | `s.adv[A] - s.adv[B]` | already A-positive. `self.T` is dropped — §1.1's named consequence |
| `TallyAtClose:62` | `s.adv[A] - s.adv[B]` | already A-positive |
| `ProofBar:67` | `(s.adv[self.ch] - s.adv[other(self.ch)]) - self.bar` | `* (1.0 if self.ch == A else -1.0)` |
| `GraceThreshold:74` | `s.adv[self.pet] - self.bar` | `* (1.0 if self.pet == A else -1.0)` |
| `PersuasionTrack:81` | `self.track(s) - self.start` | already A-positive; range `[-start, 10-start]` (§1.1) |
| `VoteAtClose:98` | the weighted A-share minus `0.5`, computed by the **same** ballot code `resolve()` runs | already A-positive |

⚠ **`VoteAtClose` needs care and is the one place a builder will introduce a real bug.** Its
`resolve()` (`:124-147`) *draws random numbers*. Calling `margin()` and `resolve()` separately draws
twice and they can disagree about who won. **Specified: `VoteAtClose` computes the ballot once into a
private `_tally(s, adj, rng) -> (wA, total)` helper, and `resolve()` and `margin()` both read it.**
The `Bout` must call the pair once at close and cache; F-S4 (§7.2) is the falsifier.

**A4 · `resolver.py:239` — `Bout.__init__` gains `rng: random.Random | None = None`;** all three draw
sites (`:32`, `:139`/`:144`, `:334`) read `self._rng or random` (§1.8).

**A5 · `resolver.py:28` — `roll_net(pool, rng=None)`** delegating to `_sigma.roll_net(pool, rng=rng or random)`.

**A6 · `wrapper.py:110` — `build_contest` gains two parameters.**
```python
def build_contest(side_a, side_b, *, venue, adjudicator=None, stakes=None, world=None,
                  use_tracker=None, degree_extension=CONTEST_DEGREE_EXTENSION,
                  armature: "ArmatureConfig | None" = None,
                  rng: "random.Random | None" = None):
```
and `Contest` carries both. Why: defect 1. `armature=None` keeps today's behaviour exactly (`Bout`
already documents `armature=None` as byte-identical to Stages 0–2, `resolver.py:246-249`).

**A7 · `wrapper.py` — derive `opponent_is_adjudicator` from the proceeding, not from a caller.**
```python
_ASYMMETRIC_ROLES = frozenset({"crown_objects", "inquisitor_proposes"})   # modes.py:493, :496
...
if armature is not None and proc_name is not None:
    import dataclasses as _dc
    armature = _dc.replace(
        armature,
        opponent_is_adjudicator=(PROCEEDINGS[proc_name]["roles"] in _ASYMMETRIC_ROLES))
```
Why: gate-off, not a flag. `ArmatureConfig` is `@dataclass(frozen=True)` (`armature.py:414`), so
`dataclasses.replace` is the idiomatic move and a caller cannot re-enable double-counting by passing
`False`.

**A8 · `wrapper.py` — `_resolve` replaces `_resolve_agon` and returns a `ContestOutcome`.**
```python
def _resolve(contest, *, policy_a, policy_b, record=False, rng=None) -> ContestOutcome:
    bout = Bout(contest.side_a, contest.side_b, contest.venue, contest.adjudicator,
                record=record,
                degree_extension=getattr(contest, 'degree_extension', CONTEST_DEGREE_EXTENSION),
                armature=getattr(contest, 'armature', None),
                rng=rng if rng is not None else getattr(contest, 'rng', None))
    band, reason = bout.resolve(policy_a, policy_b)
    return ContestOutcome(
        margin=contest.venue.win.margin(bout.state, adj=bout.adj, rng=bout._rng),
        reason=reason,
        veto=bout.faulted_side,          # A5b, below
        band=band,
        beats=tuple(bout.log or ()))
```

**A5b · `resolver.py` — `Bout` records which side faulted out.** `Bout.resolve`'s clinch branch
(`:439-441`) already computes `loser` from `self.v.faults.check(...)`; store it as
`self.faulted_side = loser` (default `None`) before returning. One assignment, one attribute; §1.4
Amendment A is unbuildable without it.

**A9 · `modes.py:485-519` — add `burden=` to all eight `PROCEEDINGS` rows**, declared metadata only
in S0 (§1.5), with the domain `{"ACCUSER", "RESPONDENT", "LOWER_STANDING", "NONE"}` defined once as a
module constant beside `PROCEEDINGS`.

**A10 · `wrapper.py` — `contestant_from_person`.**
```python
def contestant_from_person(person, proceeding: str) -> Contestant:
    """The ONE new adapter: a Person -> the kernel's Contestant spec.

    REFUSES anything that is not a Person, by type, with a typed refusal rather than a coercion.
    This is where the STRUCTURAL faction-as-claimant leak (PR#362 §C.5) becomes MECHANICAL until
    engine/cross_scale/scene_dispatch.py:121 _emergency_council_parties returns PersonIds.
    """
```
⚠ **This function cannot be written today and the shape spec does not say so.** There is no `Person`
type anywhere in `engine/` or `systems/`; `PersonId`, `Person` and `person_q` are PR #362 types
(`04_CODE_ARCHITECTURE.md:209 §B.2`), HELD BACK IN FULL. **Build it last within S0, and if PR #362
is vetoed, drop it** — `_as_contestant` (`wrapper.py:91-107`) already covers every input the tree
actually produces. Specifying its *refusal* is still worth doing now, because the refusal is the whole
mechanical content: it is what stops a faction-derived int reaching the kernel silently.

**A11 · `echo_transport.py:108 KEY_TYPE_BY_SCENE` — add one row.**
```python
KEY_TYPE_BY_SCENE = {
    "contest": "scene.contest_resolved",
    "combat":  "scene.combat_resolved",
    "inquiry": "scene.investigation_resolved",    # already in the roster — zero new key types
}
```
Verified: `scene.investigation_resolved` is a real entry in `engine/engine_params/key_types.json`
(`type_count: 55`, generated from `systems/_architecture/key_type_registry_v30.md`). **Zero new key
types** — confirmed (§4). This row also requires a matching `_OUTCOME_BY_DEGREE["inquiry"]` entry
(`echo_transport.py:114-119`), or `emit_scene_echo:436` raises `KeyError` on the first inquiry echo.
**That second half is missing from the shape spec and is a crash, not a gap.** The outcome vocabulary
for it belongs to `03_INQUIRY.md`.

### R — REWRITES

**R1 · `scene_dispatch.py:297-303` — retire the global reseed.**
```python
prev_random_state = random.getstate()
try:
    random.seed(rng.getrandbits(32))
    built = build_contest(parts[0], parts[1], venue=proceeding)
    (verdict, verdict_reason), _bout = resolve_contest(built)
finally:
    random.setstate(prev_random_state)
```
→
```python
built = build_contest(parts[0], parts[1], venue=proceeding,
                      rng=random.Random(rng.getrandbits(32)))
outcome = resolve_contest(built)
verdict, verdict_reason = outcome.band, outcome.reason
```
⚠ **Value-identity is NOT free here and the shape spec implies it is.** `random.seed(n)` on the module
RNG and `random.Random(n)` are the same Mersenne Twister seeded identically, so the *draw sequence* is
identical **only if every draw site moves to the injected object in the same order**. If any site is
missed (§1.8's three), the two streams interleave differently and the goldens move. **Land A4/A5
completely, or not at all** — and the goldens are the control that says which happened (§7.1).

**R2 · `_kernel_tests.py:694-695` — rewrite two checks 1-for-1** to the `ContestOutcome` shape.
Net 0 on the count.

**R3 · `narrative.py` — rename `Chronicle.margin` → `Chronicle.share`** (6 sites, §1.4). No mechanism
change.

**R4 · `wrapper.py:2-19` — rewrite the module docstring.** It currently advertises the router and
"the other three games ... registered STUB rows". Leaving it is the stale-pointer defect this repo
keeps finding in its own tree.

**R5 · `agon_harness.py:71-76` — rewrite WORKAROUND 3** to record that the passthrough landed, or
delete the file. It has **zero callers anywhere in the tree** (grep-verified, confirmed twice
independently in `SC_INVENTORY.md` §A and `SESSION_BRIEF.md` §9). Leaving a WORKAROUND note that
describes a fixed defect is worse than leaving the file.

**R6 · `references/module_contracts.yaml:176-183` — `contest_side.a` / `contest_side.b`.** These are
`kind: value` roles (`:178`, `:182`) that exist so `scene_dispatch.py:337,339` can compare a verdict
against a subsystem's own side labels. They stay **unchanged in S0** because `band` preserves the
comparison. They are deleted when `scene_dispatch` reads `sign(margin)` — the same later step that
deletes `band` (§3.4). ⚠ Any edit to this block requires `python3 tools/export_composition.py` and a
co-commit of `engine/engine_params/composition.json`; the exporter has a blocking `--check`
round-trip (`tools/export_composition.py:33-34`, `:230-234`).

---

## §3 · Ownership and the write path

In PR #362 vocabulary (`04_CODE_ARCHITECTURE.md:143-164`).

### §3.1 Who owns what

| state | owner | grade | note |
|---|---|---|---|
| `ContestState.adv` | `resolver.Bout._apply` (`:335`, `:373`) | **MECHANICAL** | per-bout, discarded at return. `faction.py:144-145 coalition_vote` builds its **own** `ContestState` — a second instance, not a second writer of a shared object |
| `Standing` / `Reserve` / `Room` / `FaultState` / `Dossier` | each primitive's own mutator, called only from `Bout._apply` | **MECHANICAL** | verified per-mutator in `SC_INVENTORY.md` §D2 |
| `Bout.live` (the stasis ground) | `_apply:356` | **MECHANICAL** | one site |
| `WinCondition.margin` | **`seam/wrappers/*` equivalent — owns nothing** (`04_CODE_ARCHITECTURE.md:164`) | **STRUCTURAL** | `margin()` receives `ContestState` and returns a float. It has no token, no world, and no store. The defect has no spelling |
| `ContestOutcome` | constructed once in `wrapper._resolve`, frozen | **STRUCTURAL** | `@dataclass(frozen=True)`; a consumer cannot mutate an outcome |
| `Faction.<stat>` | `engine/autoload/game_state.py:153 Faction.adjust` | **MECHANICAL** | one method; the contest reaches it only through `echo_transport._apply` (`:441`) |
| the emitted `Key` | `engine/cross_scale/echo_transport.py:427` | **MECHANICAL** | **the subsystem constructs zero Keys** (§4) |
| **effect timing** | `engine/substrate/keys.py:463 TickScheduler` | **NOT ENFORCED** (§1.9) | the binding-in-scene invariant's real owner |

### §3.2 The one write that crosses an ownership boundary

`systems/social_contest/sim/parliamentary_vote.py:214`:
```python
world.factions[dominant].adjust("L", BG_VOTE_TOTAL_VICTORY_MANDATE_DELTA * MULTS["L"])
```
A subsystem writing a Faction stat directly, inside its own resolver.

**Grade, honestly:** PR #362 would call this **STRUCTURAL under a write gate** (`§C.2:523` — no token,
no write) — but **there is no write gate in this tree**, so §0's rule applies: *"if the build does not
run the checker in CI, the runtime grade is the real one."* The real grade today is **CONVENTION**:
nothing prevents any module from calling `Faction.adjust`. The spine does not fix this and should not
pretend to.

It is also, per §1.9, the **only** contest-side write that already satisfies the binding-in-scene
ruling, which is why it is worth naming twice.

### §3.3 What the spine adds to the write path

**Nothing.** The spine adds one return type, one method, three parameters and one adapter. It writes
no state, emits no Key, and touches no store. That is deliberate and it is the property that makes
S0's control (§7.1) meaningful.

### §3.4 ⚠ **Where the spine departs from PR #362, named rather than routed around**

Three candidate conflicts. Two are real, graded and accepted. **The third — the one I was asked to
write up as "where PR #362 has to give" — I tried to establish and COULD NOT. It is refuted below,
against the primary text, and reporting it as refuted is the result.**

**(i) `ContestOutcome.band` returns a winner.** §C.5's fourth crossing (`:692`) says *"a subsystem
returning a winner has not met the contract."* `band` is a winner.
**Grade: CONVENTION** — a reader notices; nothing refuses it.
**Disposition: accepted, with a deletion condition.** It exists so S0 is provably value-identical
(§1.4 Amendment B). It has exactly one production consumer, `scene_dispatch.py:308,337,339`. It is
deleted, together with the `contest_side.a/b` composition roles, in the step that converts that
consumer to `sign(margin)`. **A builder who keeps `band` past that step has broken the contract**, and
the honest way to hold them to it is a dated comment on the field, not a guard.

**(ii) `veto` is a side, not a bool** (§1.4 Amendment A). §C.5's fifth leak (`:696`) specifies
`veto : bool`. **Grade of the departure: STRUCTURAL by signature** — the field's type makes the
information non-optional. **Disposition: this is a correction to §C.5, not a violation of it.** §C.5
was written for `kill / wound`, a seam with one actor; a contest has two claimants and no actor, so a
demote-only bool cannot express "the *other* side faulted out". Feedback owed: **`04_CODE_ARCHITECTURE.md:696`,
the `veto : bool` clause, needs a second sentence — *where the seam has no single actor, the veto
names the vetoed party.***

**(iii) ⚠⚠ THE BINDING-IN-SCENE RULING VS PR #362 — *REFUTED.* THERE IS NO CONFLICT, AND NOTHING IN PR #362 NEEDS AMENDING.**

I was asked to write the amendment. I tried to establish the conflict against the primary text and
**could not.** The attack failed and is reported as failed, which under `04_ners_audit.md`'s rule and
`CLAUDE.md` §0.1 pt 3 is a result and not a wasted pass. **An earlier draft of this section asserted
the conflict and proposed an `AX-4` amendment; that draft was wrong and is retracted here rather than
quietly deleted**, because the retraction is the useful part.

**The decisive question, stated exactly:** *under PR #362, can a scene-internal outcome bind within
the same RESOLVE that produced it — without nesting an Act inside another Act's resolution, and
without DELIBERATE reacting to RESOLVE?*

**Answer: YES.** Four findings, each read off the text:

| # | finding | anchor |
|---|---|---|
| 1 | **Everything resolves inside one season.** The driver runs `calendar → matter → deliberate → resolve → witness → census`, then `t += 1` as *"the ONE place the season advances"*. Nothing defers an act's effect to a later season | `04_CODE_ARCHITECTURE.md:505-514 §C.1` |
| 2 | **Two persons' acts resolve in the SAME pass, neither nested.** `acts = canonical_order(flatten(scenes))` **flattens across all scenes** into one list, then `for a in acts:`. `PART D` row 49 forbids *"no Act resolves inside another's resolution"* — that is **nesting**, and a flat ordered fold is not nesting | `:576-586 §C.4`; `:871 D-49` |
| 3 | **A later act in the fold SEES an earlier act's writes.** `(ok, failed_conjunct) = eval(row.requires, world_as_predecessors_left_it)` — the phrase is explicit and is the whole answer | `:579 §C.4` |
| 4 | **DELIBERATE never reacts to RESOLVE, and must not.** `scenes = deliberate(frozen)` runs on the barrier-2 projection, with no token in scope; `D-41` grades it STRUCTURAL and `D-41a` makes order-independence *observable* by a permutation test on the `Scene` **set** and the season hash | `:508-509 §C.1`; `:862 D-41`; `:863 D-41a` |

**So what made it look like a conflict?** Not PR #362. **A modelling choice** — representing a bargain
as **two interior `commit` edges** instead of as **one Record.** Under that modelling the conflict is
real, and it is worth showing why, because it is the trap a builder walks into:

- `tenure_kinds` is `[hold, contain, commit, oblige, succeed, tie, knot]` (`:475`) — **`commit` IS a
  Tenure kind.**
- So the gate's `AX-4` clause 2 fires: `kind is Tenure => actor == subject(id)` (T-m) or one of three
  named cases, `otherwise raise NotYours` (`:528-534`). **A's act cannot write B's commit.** That is
  `AX-4` itself (`01_AXIOMS.md:141`), not a gate quirk.
- So B must act. B's acts live in B's own `Scene` (`Scene := (id, person, occasion, place, interactions : Act[])`,
  `:396`), authored in DELIBERATE **before** the contest resolved (finding 4). **B's assent would be a
  blank cheque — chosen before the terms exist.**
- ⚠ **And it is worse than awkward: it is ORDER-FRAGILE.** `canonical_order` is
  `(stratum, actor-hash, intra-person position)` (`:576`), and `D-36` (`:857`) says *"the canonical key
  is declared data plus a hash tiebreak; rank never breaks a tie."* **Nothing orders A's negotiation
  act before B's conditional commit.** Roughly half the time B's commit is folded first, its `requires`
  fails, and the bargain does not bind — **for a reason nobody chose.** A design whose outcome depends
  on an actor-hash coin flip is broken independently of any ruling.

**The modelling that satisfies the ruling with the freeze fully intact — and PR #362 already has it.**

> **A settlement is a `Record`, not two interior edges.** `§B.4/§B.5` (`:249-261`) already folds
> `Petition` and `Dispensation` into `Record` kinds, so the precedent is in the document. **A Record
> is not a Tenure, so the gate's `AX-4` clause 2 does not fire at all** — the write matches its
> matrix row and its `writer:` column like any other, and `AX-4` is satisfied because the Record's
> owner is the record store, with A's act as its author, exactly as `Proposition.utterer` carries
> authorship (`§B.6:265-267`).
>
> **One act. One write. No nesting. No DELIBERATE reacting to RESOLVE. No order fragility.** The
> bargain binds in the scene that produced it, and the season hash is untouched.

**And the coordinator's second bullet is confirmed: the counterparty's assent is COMPUTED, not
chosen.** `settle()` is a pure map (`§C.3`'s DELIBERATE-is-a-pure-map idiom, `:564-571`) whose inputs
include B's own floor. B's floor is state **B already owns** — B's prior commitments — so B's assent
is *revealed by B's own earlier acts*, never invented at the seam. **`AX-1` is intact**: only A acted
this season, and B's floor was set by B's own acts in earlier ones. Nothing here lets an engine decide
for a person; it lets a person's standing commitments answer for them, which is what a reservation
price *is*.

> ### ⚠ **THE CONSTRAINT THIS PUTS ON `02_NEGOTIATION.md`, WHICH IS THE PART MY SIBLING NEEDS**
>
> 1. **The NPC's assent must be computed by `settle()` from state the NPC already owns. It must NOT
>    be an act chosen in DELIBERATE.** A speculative `commit` authored before the terms exist is a
>    blank cheque, and it is order-fragile (`D-36`). This is not a preference; it is what the fold's
>    ordering rule forces.
> 2. **A Record binds the FACT. An `oblige` binds the PERSON — and only that person can open their
>    own.** So: the *settlement* is a Record written by the resolving act and binds in-scene; a
>    durable *duty* on the counterparty is an `oblige` Tenure and needs that person's own act, in
>    this season or a later one. **Design the bargain so the enforceable content is the document**,
>    which is also what the history says: a treaty is a document, and breach is a visible act — which
>    is exactly what `repudiate` (`verb_table.yaml:378`) is for.
> 3. `§C.5.1`'s roster freeze (`:704-716`) **helps rather than hinders**: the claimants are resolved
>    once at the seam boundary, so the Record's subject set is fixed and checkable, and `D-49`'s
>    STRUCTURAL grade in Python is a consequence of the same property.

**What remains true from my §1.9, and it is the only real conflict:** PR #362's gate applies the
write **synchronously** — `before = get(); store._set(); after = get()`, annotated *"THE GATE APPLIES
THE WRITE"* (`:536`). **So PR #362 satisfies the ruling natively.** The tree does not, because of
OF-7's deferral to `accounting_boundary` (§1.9). **The ruling and PR #362 agree; the live engine
disagrees with both.** That is where the work is, and it is IN-lane.

**Feedback owed to the PR #362 chain: none on this point.** One optional note, and it is a note and
not an amendment: `§C.5`'s five-leak list (`:694-697`) could say that a mutual seam outcome is
recorded as a Record rather than as per-claimant Tenures, since the derivation above is
reconstructible but not written down anywhere. That is a clarification, not a change of shape.

---

## §4 · Keys and state changes

Reconciled against `SC_INVENTORY.md` §C/§D and against **`engine/engine_params/key_types.json`** — the
real roster, generated from `systems/_architecture/key_type_registry_v30.md`. The inventory's finding
that `references/descriptor_registry.yaml` and `engine/substrate/keys.py` carry **none** of the five
strings is **CONFIRMED**; `descriptor_registry.yaml` is a descriptor vocabulary, not a Key-type roster,
and `keys.py` is the mechanism. Do not look for Key types in either.

**The subsystem constructs zero Keys.** Re-verified this session:
`grep -rn "Key(\|KeyLog\|\.emit(" systems/social_contest --include="*.py"` returns nothing. Every Key
credited to social contest is built at `engine/cross_scale/echo_transport.py:427`.

| Key type | in `key_types.json`? | spine's effect |
|---|---|---|
| `scene.contest_resolved` | yes | **unchanged.** Same construction site, same payload keys (`echo_transport.py:434-438`), same `_OUTCOME_BY_DEGREE` lookup |
| `scene.investigation_resolved` | yes (already in the 55) | **A11 maps it**, `KEY_TYPE_BY_SCENE` + `_OUTCOME_BY_DEGREE`. Consumed by `03_INQUIRY.md` |
| `scene.dialogue` | yes | declared in `module_contracts.yaml:751`; **no construction site anywhere in the tree.** Unchanged by the spine |
| `scene.insult`, `scene.threat` | yes | declared at `:753`, `:755`; **zero construction sites, zero consumers.** Unchanged |
| `state.opinion_revised` | yes | declared consumed at `:750`; **no consumer inside the package.** Unchanged |

**New Key types introduced by the spine: zero.** Confirmed against the roster, not asserted.

**Persistent state changes the spine makes: zero.** Every element is a return type, a method, a
parameter or an adapter. The one persistent write the subsystem already makes
(`parliamentary_vote.py:214`) is untouched.

**Registry rows that ride along** (not code, and each needs its co-commit):

| file | edit | gate |
|---|---|---|
| `references/module_contracts.yaml:739-771` | `social_contest` module row: nothing required by the spine. `wiring.note` at `:770` ("Agon kernel built (1 of 4 games)") becomes false when the branches land — a branch-document item, not the spine's | `tools/export_module_contracts.py` |
| `references/module_contracts.yaml:176-183` | `contest_side.a/b` — **unchanged in S0** (§2 R6) | `tools/export_composition.py --check` (blocking) |
| `registers/editorial_ledger_sc.jsonl` | **ED-SC-0020** → `status: resolved`, `needs_jordan: false`, citing §1.5 | `tools/validate_ed_citations.py` |
| `references/id_reservations.yaml:195` | SC `next_free: 33` — ⚠ `00_BRANCH_SHAPES.md` §6 says this "could not be located by grep". **It is at line 195.** Read it, allocate, bump, co-commit; never max+1 | — |

---

## §5 · The N-line for every spine object, and the false-N-line hunt

`14_NERS.md` §3: *no object enters without one — cut it, and the emergent possibility you lose is ____.*

### §5.1 N-lines

| object | cut it, and the emergent possibility lost is… | confidence |
|---|---|---|
| `WinCondition.margin()` | a contest that can feed the **one** ladder. Without it each branch invents its own degree map: four win conditions become seven, and `dice_engine.degree_from_net`'s "single owner for every scale" (`:229`) becomes false by addition | high |
| `SUCCESS_UNIT` per subclass | **the ladder's answer being meaningful at all.** §1.3 measured it: without a per-unit conversion a unanimous 7–0 ballot bands as `Partial`. This is not distillable — the units genuinely differ | high |
| `ContestOutcome` | a caller that can tell a stub from a result. `scene_dispatch.py:301` breaks on a stub today, and every branch would otherwise add a fourth return shape | high |
| `ContestOutcome.veto` (as a side) | **a fault-out win.** A side can fault out while leading (`resolver.py`'s clinch branch returns `other(loser)`, not the adv leader), so without it the contest cannot express "you lost by cheating" | high |
| `ContestOutcome.band` | **nothing emergent — it is a compatibility field with a deletion date** (§3.4 i). Recorded here honestly rather than given a manufactured N-line | n/a |
| `burden` on `PROCEEDINGS` | *silence convicts* — an outcome no handicap expresses. A biased track start (`start=6.0`) makes winning harder; it cannot make **not answering** lose | medium — the mechanism is real, its eight assignments are not written |
| `armature=` passthrough | every Stage-3 mechanic from the one production seam: CR4 terrain, CR5 backfire, the adjudicator's convictions. Today all three are reachable only by hand-building a `Bout` | high |
| `rng` injection | same-seed reproducibility **through the seam** without mutating global state; and any parity harness at all | high |
| `contestant_from_person` | a **Person** as a claimant. Today only faction-derived ints reach the kernel from production (`scene_dispatch.py:139`) | **low — see §5.2 row 7.** It cannot be built yet |
| binding-in-scene (I-S6a/b) | **time inside a season.** Jordan's own words; and §1.9 traced the mechanism that removes it | high |

### §5.2 False N-lines hunted

The pattern (`14_NERS.md` §3): *a mechanism was named, a **store** was proposed for it, and the
store's job was already being done by an object the design had ruled in.* Hunted explicitly against
`systems/settlements/sim/ledger.py`, the σ resolver, and the armature, as the brief directs. **Seven
candidates. Six cut. One survives with a downgrade.**

| candidate | its claim | verdict |
|---|---|---|
| **A `ContestResult` store on `Contest`** | "the outcome must persist for the caller" | **CUT.** `Contest` is write-once at construction (verified: no post-`__init__` mutation, `SC_INVENTORY.md` §D2). The outcome is a return value; a store would give it two homes and let them disagree |
| **A `winner` field on `ContestOutcome`** | "callers need to know who won" | **CUT — and this is the highest-value cut in this document.** `sign(margin)` is the winner, and I verified it reproduces `VoteAtClose.resolve` **exactly** in both aggregations (`:139-142` weighted, `:143-147` simple: A iff `wA*2 > total` ⟺ `share > 0.5` ⟺ `margin > 0`). The one case it does *not* cover is the clinch — which `veto` covers, and `veto` is not a winner field: it names who **faulted**, not who won |
| **A `degree` field on `ContestOutcome`** | "the seam should return the band" | **CUT.** `dice_engine.degree_from_net` is the single owner (`:229`, Jordan 2026-08-14). A degree computed in the seam is a second ladder; PR #362 §C.5 puts `ladder.degree(...)` outside the provider for exactly this reason |
| **A `ContestRecord` for the resolved contest** | "there is no record spine" (defect 4) | **CUT.** The Record primitive exists **once**, single-owner: `systems/settlements/sim/ledger.py` (`LedgerTag`, `ledger_add` dedupe-by-`(kind,key)`, `ledger_sweep`). The subsystem has **zero code cross-references to it in either direction** — confirmed twice — so the failure is a **composition** failure, not a missing object. A record on the contest would be a second owner of the same fact. **What the branches write is a `LedgerTag`** |
| **A per-contest RNG *store*** | "reproducibility needs seed state" | **CUT.** `random.Random` **is** the store; `Bout` holds a reference. A seed field on `Contest` would be a second, drift-prone copy of a thing that already carries its own state |
| **A `stall_clock` for burden semantics** | "whoever holds the burden loses on a stall — that needs a timer" | **CUT, and it is a textbook instance of the pattern.** `ProofBar.resolve:71-72` already *is* the stall rule: `if net >= self.bar: return self.ch` / `if closing: return df`. The bout's own exchange budget (`Venue.budget`, `:157`) is the clock. The mechanism was named, a store was proposed, and the store's job was already being done |
| **`contestant_from_person`** | "a Person must be able to enter a contest" | **SURVIVES, DOWNGRADED to low confidence.** It is not a store, so the pattern does not fire. But it fails a different test: `14_NERS.md` §3 row 6 — *"an object with no producer cannot have an N-line."* **There is no `Person` producer in this tree** (§2 A10). Its N-line is conditional on PR #362 landing. Recorded as conditional rather than asserted, and it is the element I would cut first if a reviewer pushed |

### §5.3 Watched despite being distillable (E-as-a-ratio, both directions — `14_NERS.md` §4.1)

| kept | the N it protects | confidence |
|---|---|---|
| `WinCondition.resolve()` alongside `margin()` | `narrative.py:83 classify` reads the band; `_kernel_tests.py:622 _BANDS` pins it in ~4 checks; ED-SC-0002's composed keying rules on bands. Distilling `resolve()` away would delete the legibility layer to save one method | high |
| six `SUCCESS_UNIT` constants rather than one shared scalar | the units genuinely differ (§1.3's table). One shared constant is over-distillation — it would make five of six win conditions wrong to save four lines | high |
| `ContestOutcome.band` | **nothing.** Kept purely so S0 has a control. **This is the most distillable thing in this document and it is on a deletion path** (§3.4 i) | n/a — deliberate debt |
| `Contest` as a separate object from `ContestOutcome` | build/resolve separation is the wrapper's whole stated duty (`wrapper.py:4`, *"the wrapper ADAPTS + ROUTES; it RESOLVES NOTHING"*), and `Contest` is reusable across bouts | high |

---

## §6 · Migration and blast radius

### §6.1 ⚠ The import-cycle test — **the brief's §9.1 is CORRECT about the number and WRONG about what the test asserts, and the difference decides how a builder proceeds**

`SESSION_BRIEF.md` §9.1 says `test_exactly_two_cycles_remain_and_they_are_the_expected_families`
*"fails if the count changes"*. I read the test. **The 9 appears only in the module docstring
(`tests/valoria/test_import_cycle_game_state_npe.py:23`). It is asserted nowhere.**

What the test actually asserts (`:56-103`):
- `len(cycles) == 2` — the number of cycle **families** in the whole repo (`:71`);
- exactly one family whose every member starts with `systems.social_contest.sim.contest` (`:79`, `:96`);
- exactly one whose every member starts with `systems.mass_battle.sim`;
- that the deleted `massbattle <-> units` family has not returned;
- `checked == 2`, an assert-that-asserted guard (`:99`).

**Consequence:** changing the contest family from 9 members to 8 or 10 **passes**. Deleting the family
entirely **fails** (`len(cycles)` → 1, and `len(contest)` → 0). Both figures in the brief were right
on their own basis; the executable constraint is the family count, not the member count.

**I measured the family's actual structure** so a builder can predict the effect rather than guess.
Re-running the repo's own detector (read-only, no repo write):

```
PKG            -> appraise armature dictionaries faction modes resolver rhetoric wrapper
PKG.appraise   -> armature
PKG.armature   -> dictionaries
PKG.dictionaries -> PKG  modes  resolver
PKG.faction    -> resolver
PKG.modes      -> dictionaries resolver
PKG.resolver   -> rhetoric
PKG.rhetoric   -> dictionaries
PKG.wrapper    -> PKG  armature dictionaries modes resolver rhetoric
```

The cycle closes through **exactly two back-edges into the package node**: `dictionaries -> PKG` and
`wrapper -> PKG`. Both come from bare `from . import X` statements — `dictionaries.py:45`
(`from . import modes as _modes`) and `wrapper.py:284,293,294` — because `structure_audit.build_g_code`
resolves a bare `from . import X` to **both** the package and the submodule (`:312-325`), whereas
`from .X import Y` resolves only to the submodule. That is why `contract`, `primitives`, `policy` and
`narrative` are outside the family despite being imported by `__init__`.

**What the spine does to it: NOTHING.** Verified against the change list:
- `ContestOutcome` goes in `contract.py` (A1), which is outside the family and gains no import.
- No new module is created.
- `wrapper.py` keeps `from . import dictionaries/armature/rhetoric` (`:284`, `:293-294`) — those lines
  are untouched, so the `wrapper -> PKG` back-edge survives.
- `dictionaries.py:45` is untouched, so `dictionaries -> PKG` survives.

**So the family stays at 9 and `test_exactly_two_cycles_remain_and_they_are_the_expected_families`
passes unchanged. No test update is required by the spine.** State it that way in the commit rather
than leaving the reader to infer it.

⚠ **What WOULD break it, so a branch author does not do it by accident:** creating a new submodule
(e.g. `settle.py`) that `__init__.py` imports **and** which itself uses a bare `from . import X` adds
a tenth member — still passing. But converting `wrapper.py:284/293/294` and `dictionaries.py:45` to
`from .X import Y` would drop **both** back-edges, dissolve the family, and **fail** the test at
`:71` and `:96`. That is a desirable repair, but it is an IN-lane commit with its own deliberate test
update, never a side effect. Reproducer:

```
python3 -c "
import importlib.util; from pathlib import Path
s=importlib.util.spec_from_file_location('sa','skills/valoria-vector-audit/scripts/structure_audit.py')
sa=importlib.util.module_from_spec(s); s.loader.exec_module(sa)
g,_=sa.build_g_code(Path('.').resolve(), sa.collect_py_modules(Path('.').resolve()))
print([sorted(c) for c in sa._cycles(sa.tarjan_scc(g), g)])"
```

### §6.2 Everything that breaks, with `path:line`

| # | `path:line` | what breaks | fix, in the same commit |
|---|---|---|---|
| 1 | `engine/cross_scale/scene_dispatch.py:301` | `(verdict, verdict_reason), _bout = resolve_contest(built)` — the return shape changes | R1. `outcome.band` / `outcome.reason` reproduce both values verbatim |
| 2 | `engine/cross_scale/scene_dispatch.py:297-303` | the reseed dance is retired | R1, and **only if A4/A5 are complete** |
| 3 | ⚠ **`engine/tests/test_pipeline_reach.py:832-844`** | reads `wrapper.GAMES[g]["resolve"](None)` at `:838`; `GAMES` is gone | **D9 — delete the test.** Its subject ceases to exist. **This is not in `00_BRANCH_SHAPES.md`'s blast radius** |
| 4 | `_kernel_tests.py:696-703` | pins `GAMES` and the three stub rows | **D8 — delete 4 checks.** `_KERNEL_EXPECTED` −4 |
| 5 | `_kernel_tests.py:694-695` | pins `((band, reason), bout)` | **R2 — rewrite 1-for-1.** Net 0 |
| 6 | `_kernel_tests.py:633` | imports `GAMES as GM` | drop from the import list |
| 7 | `engine/tests/test_contest_kernel.py:93 _KERNEL_EXPECTED = 389` | the count moves | **Re-pin from the measured `RESULT:` line, never from arithmetic in your head.** The auditable part: **−4** from D8, **0** from R2, **+N** from the new checks (§7.2 F-S1..F-S7 are seven checks minimum). **I do not state the total — that would be a fabricated number** (`CLAUDE.md` §0.1 pt 4). The file's own convention (`:90-107`) requires the arithmetic in the comment; supply it from the measurement |
| 8 | `systems/social_contest/sim/contest/__init__.py:73,119` | re-exports `GAMES` | D7 |
| 9 | `engine/tests/test_mc_v18_regression.py:142-158`, `test_f7_smoke_oracle.py` | **the control, not a break** | must NOT move (§7.1) |
| 10 | `engine/tests/test_echo_transport.py:107` | asserts the deferral the ruling overturns | **not touched by S0.** Named in §1.9 as the IN-lane blocker for I-S6b |
| 11 | `narrative.py:44,55,96,98` + 2 `render()` reads | `Chronicle.margin` renamed | R3 |
| 12 | `agon_harness.py:71-76`, `:214-215` | WORKAROUND 3 becomes false | R5 |
| 13 | `tools/balance_oracle.py:153-154`, `tests/valoria/test_balance_oracle_arms.py:65-66,88-89`, `test_band_extension_seam.py:133`, `test_degree_ladder_single_owner.py:138`, `engine/tests/test_sigma_leverage_parity.py:52` | all import `degree_extension` / `resolver` **submodules directly** | **no break** — the spine does not touch `degree_extension.py` and does not change `resolver`'s module-level names |
| 14 | `tests/valoria/test_engine_does_not_import_systems.py:436` | asserts `systems.social_contest.sim.contest:build_contest` resolves as a callable | **no break** — `build_contest` keeps its name and stays callable |
| 15 | `engine/tests/test_parliamentary_bridge.py` (10 tests) | exercises `parliamentary_vote`, not the contest kernel | **no break** — untouched by the spine |

### §6.3 ⚠ A trap in `degree_from_net(margin, ob=0, extension=...)`

`00_BRANCH_SHAPES.md` §2.1 writes `extension=proceeding.extension`. **There is no `extension` field on
any proceeding** (`modes.py:485-519`, read in full). And if a builder substitutes
`CONTEST_DEGREE_EXTENSION`, it is **inert**: `PoolDesaturation.may_overwhelm` abstains when `pool is
None` (`degree_extension.py:77-82`), and there is no pool at contest close. Measured:

```
degree_from_net(5.0, 0.0, extension=CONTEST_DEGREE_EXTENSION) -> Degree.OVERWHELMING
degree_from_net(5.0, 0.0)                                     -> Degree.OVERWHELMING     # identical
degree_from_net(5.0, 0.0, extension=..., poool=8)             -> TypeError (declared-key refusal)
```

**Specified: the contest-level degree uses the owner's unmodified ladder — `extension=None`.**
`PoolDesaturation` is a **per-roll** de-saturation for `_reception` (`resolver.py:307-308`), where a
pool exists. Injecting it at contest level is a false affordance: an injection point that looks
configurable and can never fire.

---

## §7 · Falsifiers

`CLAUDE.md` §0.1 pt 3 (name the falsifier in the same commit as the claim) and pt 2 (**an assertion
must be able to observe the failure it excludes**). Each row below states what it would see fail.

### §7.1 THE CONTROL — the two campaign goldens must NOT move

The spine is meant to be **value-identical for agôn**. If the goldens move, the spine changed agôn,
and that is a regression regardless of how good the reasoning looked.

```
python -m pytest engine/tests/test_mc_v18_regression.py -q     # n=2, seed 0  (:142-158)
python -m pytest engine/tests/test_f7_smoke_oracle.py -q       # n=8, seed 42 (:16)
```

**Why this control is real and not decorative** — three independent reasons, each verified:

1. `ContestOutcome` is a strict **superset** of today's tuple (§1.4 Amendment B), so
   `scene_dispatch.py:308-309`'s `out["result"]` dict is byte-identical, the
   `contest_side.a/b` comparison at `:337-339` is unchanged, and the emitted `Key`'s payload
   (`echo_transport.py:434-438`) is unchanged.
2. `armature=None` and `rng=None` are the defaults, and `Bout` already documents `armature=None` as
   byte-identical to Stages 0–2 (`resolver.py:246-249`).
3. `margin()` is **added and not consumed** by any production path in S0. Adding an unread method
   cannot move a number.

`test_mc_v18_regression.py:151-158 test_mc_v18_resolves_at_least_one_contest` is the row that proves
the seam is actually exercised — a green golden with zero contests resolved would be a vacuous
control, and that test is what excludes it. **Report both: the goldens held AND the contest count was
non-zero.** Also run `engine/tests/test_parliamentary_bridge.py` (10 tests) and
`tests/valoria/test_import_cycle_game_state_npe.py`.

### §7.2 Per-claim falsifiers

| id | the claim | the test that would show it wrong | can it observe the failure? |
|---|---|---|---|
| **F-S1** | `margin()` exists on **every** subclass and returns a float | iterate `WinCondition.__subclasses__()`, call `margin()` on a fixture `ContestState`, assert `isinstance(m, float)`; then `assert checked == 6` | **yes** — the `checked == 6` guard is what stops a subclass being silently skipped (§0.1 pt 2's own template) |
| **F-S2** | the margin is **A-positive for every subclass**, including configured-side ones | build a state where A leads. For each subclass **and** for `ProofBar(challenger=B)` / `GraceThreshold(petitioner=B)`, assert `margin > 0`. Then flip and assert `< 0` | **yes** — this is the one test that catches §1.2's inversion, and without it the inversion is invisible |
| **F-S3** | `sign(margin)` agrees with `resolve()` wherever `resolve()` names a side | over a seeded sweep of states per subclass, assert `resolve(closing=True)` is `A` iff `margin > 0`, `B` iff `< 0`; count and assert the count | **yes**, with one carve-out that must be **written into the test, not omitted**: `ThresholdRace`'s early branch (`:58-59`) can name a winner at `closing=False` where the margin is near zero. Test the closing case; assert the early case separately as a known, named divergence (§1.1) |
| **F-S4** | `VoteAtClose.margin()` and `.resolve()` describe **the same ballot** | seed; call `margin()` then `resolve()` on the same state; assert agreement over N seeds and `assert checked == N` | **yes** — and it fails loudly on the naive implementation that draws twice (§2 A3). This is the falsifier for the bug a builder is most likely to write |
| **F-S5** | the armature is reachable **through the seam** | `build_contest(..., venue="church_tribunal", armature=ArmatureConfig(styles={A:"precedent"}, positions={...}))`, resolve over N seeds, assert the mean track differs from `armature=None`. Assert the difference is non-zero, not merely that it ran | **yes** — and it is the *only* honest test of defect 1, because `wrapper.py:377`'s existing self-check builds its own `Bout` and therefore proves nothing about the seam. **The precedent for the assertion shape already exists** at `_kernel_tests.py:1430`, which measures exactly this delta on a `build_contest`-built church tribunal |
| **F-S6** | `armature` gate-off is **derived**, not caller-set | `build_contest(venue="church_tribunal", armature=ArmatureConfig(opponent_is_adjudicator=False))`; assert the built contest's armature has it **True**. Same for `royal_audience`; assert **False** for `formal_contest` | **yes** — it observes a caller re-enabling double-counting, which a `not None` check would not |
| **F-S7** | `rng` injection is **complete** — no draw escapes to the global stream | snapshot `random.getstate()`; run a full `resolve_contest(..., rng=Random(7))` on `guild_arbitration` (so `VoteAtClose` fires); assert `random.getstate()` is unchanged. Then assert two runs with `Random(7)` are identical and `Random(8)` differs | **yes, and it is the strongest test in this list.** It observes *any* missed draw site, including ones added later, because a missed site necessarily advances the global stream. It also observes the `Random(8)` half — without which a stub returning a constant would pass |
| **F-S8** | `burden` is declared on all eight rows and is **consistent with** the win condition already selected | for each of the eight, assert `burden` ∈ the domain and that `ACCUSER`/`RESPONDENT` rows build a burden-bearing `win` while `NONE` rows do not; `assert checked == 8` | **yes** — and it fails if a builder wires `burden` as a *selector* in S0 (§1.5), which is precisely the mistake to catch |
| **F-S9** | zero new Key types | assert every string in `KEY_TYPE_BY_SCENE.values()` is in `engine/engine_params/key_types.json`'s `types`, and that `_OUTCOME_BY_DEGREE` has a row for every `KEY_TYPE_BY_SCENE` key | **yes** — the second half catches the `KeyError` at `echo_transport.py:436` that A11's first half would otherwise introduce |

### §7.3 The execution artifact that makes S0 DONE (`CLAUDE.md` §0.2)

Not a `## Status:` line. Three artifacts, all of which are runs:

1. `python -m pytest engine/tests/test_contest_kernel.py -q` green at the **re-pinned** `_KERNEL_EXPECTED`,
   with the measured `RESULT:` line quoted in the commit message.
2. `python -m pytest engine/tests/test_mc_v18_regression.py engine/tests/test_f7_smoke_oracle.py -q`
   green **and unchanged** — the control (§7.1).
3. A seeded `scene_dispatch._resolve_slot` run on a `guild_arbitration` emergency-council slot that
   returns a `ContestOutcome` and puts one `scene.contest_resolved` Key in the `KeyLog`, with
   `KeyLog.content_hash()` **identical to the pre-spine run**. That hash equality is what makes
   "value-identical" a measurement rather than a claim.

### §7.4 ⚠ The falsifier for the binding-in-scene ruling — **it is constructible, and it fails today**

This is the item the coordinator asked to be answered plainly, so here it is plainly.

**The test.** Queue **two** contest scenes in one season against the same faction, and assert the
second saw the first's write:

```
scene_slate.clear()
scene_slate.queue_scene("contest", {"faction": fid, "stakes": {"kind": "emergency_council"}})
scene_slate.queue_scene("contest", {"faction": fid, "stakes": {"kind": "emergency_council"}})
before = world.factions[fid].L
run_scene_phase(world, rng=Random(0))            # drains BOTH, one action phase
assert world.factions[fid].L != before, "the first scene's outcome did not bind before the second resolved"
```

**Can it observe the failure it excludes? YES — and I verified the observation channel rather than
assuming it.** `scene_dispatch.py:139 _emergency_council_parties` returns
`(max(1, round(f.L)), max(1, round(7.0 - f.Sta)))`. So the **second** scene's side faculties are
derived from `f.L` — the exact stat the **first** scene's echo moves. If the write binds, the second
contest is built from different faculties; if it defers, it is built from the same ones. The failure
is visible in the contest's own inputs, not only in a stat register.

**Would a deferred write pass it silently? No** — that is what the `!= before` comparison excludes,
and it is why the assertion is on the stat *before* `accounting_boundary()` rather than after. A test
that called `accounting_boundary()` first would pass under both regimes and would be exactly the
absent assertion `§0.1` pt 2 warns about.

**And it fails on the current tree**, by construction (§1.9's trace: OF-7 defers to
`accounting_boundary`, which `engine_clock.py:122` calls after the action phase closes).

**So: ship it as `xfail(strict=True)` citing the ruling, not as a skip.** A strict xfail *observes*
— it fails if the behaviour is fixed and the marker is not removed, which is the property that makes
it a real record of an open ruling rather than a silenced test. A `skip` observes nothing.

**One thing this falsifier does NOT establish**, said rather than glossed: it tests half (b) of the
ruling — effect ordering. Half (a) — no second consent act — has no failing test because there is
**no bargain in the tree to fail**; `settle()` does not exist. I-S6a is enforced structurally by
`ContestOutcome`'s field list (§1.9), and the falsifier for it is a **negative** one: a test asserting
`ContestOutcome`'s `__dataclass_fields__` contains no field matching
`{pending, provisional, ratified, awaiting_*}`. That is a weak test and I will call it weak: it
observes the field being *added*, not the concept being reintroduced under another name.

---

## §8 · What this does NOT fix

Plainly, and with the anchors, so nobody reads a silence as a claim.

1. **The faction-as-claimant leak.** `scene_dispatch.py:121-139 _emergency_council_parties` returns
   two **ints** derived from `f.L` and `f.Sta`. PR #362 §C.5 (`:695`) grades "a faction as combatant"
   STRUCTURAL via `claimants : PersonId[]`. The spine's `contestant_from_person` **refuses** non-Person
   input, which makes the leak MECHANICAL at the adapter — but the production path does not go through
   that adapter and cannot, because there are no Persons. **Unfixed, and unfixable in the SC lane.**
2. **The `LedgerTag` custody gap.** `systems/settlements/sim/ledger.py:36 LedgerTag` has no holder
   field; tags live on `Settlement.ledger`. A negotiated Debt between two Persons has nowhere to
   live. **SE-owned.** The branches write to the settlement's ledger at `place` until it exists.
3. **I-S6b — binding as effect.** Owner `engine/substrate/keys.py:463`. §1.9 specifies the minimal
   change; the spine cannot land it. **The most important thing this document does not fix.**
4. **The `SUCCESS_UNIT` calibration.** Six `[SEED]`s. `tools/balance_oracle.py` is the instrument;
   it is not a CI gate (240 campaigns ≈ 13 min) and it is a *campaign* instrument, so for a
   campaign-unreachable change both its arms are identical by construction. Whether the contest margin
   is campaign-reachable is itself unmeasured.
5. **Three resolution models remain** (defect 6): `resolver.Bout`, `parliamentary_vote.run_parliamentary_vote`,
   `faction.coalition_vote` (`:128-154`, its own `ContestState`, its own `roll_net`, `PersuasionTrack.resolve`
   outside the loop). Plus the dead `contest_legacy_stub.run_contest` (`:191`, zero callers) whose
   **constants are live** through `parliamentary_vote.py:44-50`. The spine deletes none of them —
   `coalition_vote` is `04_CONSENSUS.md`'s, and the legacy stub is a separate cleanup with a live
   re-export surface.
6. **97 dangling `params/contest.md` citations** across 8 kernel files. `params/contest.md` does not
   exist; `references/restructure_ledger.md:768` resolves it into the evacuated `engine/params/` tree.
   The spine touches none of them and adds none.
7. **`parliamentary_stay.py`** — `invoke_stay:54` and `resolve_stay_lift:101` have **zero callers
   anywhere**. Not the spine's.
8. **`agon_harness.py`** — zero callers. R5 fixes its stale comment, not its uselessness.
9. **The BG one-season Mandate penalty is permanent** (defect 5): `parliamentary_vote.py:214` with
   `:218`'s own note that temporary-modifier restoration is "deferred to season_manager", and
   `season_manager.advance_season` has no such facility. ED-SC-0015, still open.
10. **`ContestOutcome.band` returns a winner**, in acknowledged violation of PR #362 §C.5, on a
    deletion path with no enforcing gate (§3.4 i). Debt, recorded as debt.

---

## §9 · The case against this spine

The strongest version I can make, plus every attack I ran. **An attack that fails and is reported as
failed is a result** (`04_ners_audit.md`; `CLAUDE.md` §0.1 pt 3).

### §9.1 The strongest case against

**The spine's central claim is that one Margin can carry six win conditions to one ladder, and §1.3
shows that claim was false as specified — I repaired it with six `[SEED]` constants that nothing
calibrates.** So the honest description of what happened here is: *the planner's spine did not work, a
verification found out why, and the repair replaced a broken conversion with an uncalibrated one.*
Six uncalibrated constants at the seam every future branch reads is a worse failure surface than the
band strings they replace, because a wrong band is visible in a log and a wrong `SUCCESS_UNIT` is a
silently mis-graded outcome. The mitigation — mark them `[SEED]`, don't consume `margin()` in
production during S0, measure before any branch reads it — is real, but it is a *process* mitigation
for a *mechanism* defect, which is the weaker kind.

The second-strongest: **`ContestOutcome.band` is the spine conceding its own central contract on the
first commit.** "One shape, never a winner" ships with a winner field, and its removal depends on a
future step that nothing forces to happen. `CLAUDE.md` §2's whole ED-1094 story is about exactly that
failure mode — a thing left for an unprompted follow-up nobody triggers.

### §9.2 Attacks run, and their results

| attack | result |
|---|---|
| *"`sign(margin)` cannot reproduce `VoteAtClose`'s verdict, so the winner field is load-bearing"* | **FAILS.** Read both branches (`:139-142`, `:143-147`): A iff `wA*2 > total` ⟺ `share > 0.5` ⟺ `margin > 0`, and the same for simple majority. Exact, in both aggregations |
| *"…but it cannot reproduce a CLINCH"* | **SUCCEEDS.** `Bout.resolve`'s clinch branch returns `other(loser)`, and a side can fault out while leading. This is why `veto` is a **side**, not a bool (§1.4 Amendment A), and it is a correction to PR #362 §C.5 (§3.4 ii) |
| *"`degree_from_net(margin, 0)` works — the ladder is unit-free"* | **FAILS SPECTACULARLY, against the shape spec.** Measured: `VoteAtClose`'s margin maxes at 0.5, so a unanimous 7–0 verdict bands `Partial`. §1.3 |
| *"the spine changes agôn, so the goldens are not a control"* | **FAILS**, on three independent grounds (§7.1), each verified against a line rather than argued |
| *"the 9-module cycle test blocks the spine"* | **FAILS.** The 9 is a docstring, not an assertion (§6.1). I read the test rather than the brief's summary of it, and the difference changes what a builder must do |
| *"`ProofBar`'s configurable challenger is theoretical — nothing sets it to B"* | **INCONCLUSIVE, and I kept the fix anyway.** No live instance sets `challenger=B` (grepped `modes.py`); the parameter exists and defaults to A. The inversion is latent, not live. Keeping the orientation costs two multiplications; discovering it later costs a wrong verdict in a venue nobody is testing |
| *"`burden` can select the win condition in S0 — the spec says so"* | **SUCCEEDS AGAINST THE SPEC.** Not one of the eight canonical proceedings uses `ProofBar`/`GraceThreshold`/`ThresholdRace` (§1.5), so selection at S0 flips `church_tribunal` and moves the pinned Gate-C block. Split into S0-metadata / S1-selector |
| *"deleting `GAMES` breaks only the kernel suite"* | **SUCCEEDS.** `engine/tests/test_pipeline_reach.py:838` reads `wrapper.GAMES` directly and is absent from the shape spec's blast radius (§6.2 row 3) |
| *"`rng` on `roll_net` retires the global reseed"* | **SUCCEEDS AGAINST THE SPEC.** Three draw sites, not one; `VoteAtClose` is on the production proceeding's own win condition (§1.8) |
| *"binding-in-scene is a negotiation concern, not a spine concern"* | **FAILS.** `dispatch_scenes:404` drains the whole slate in one phase and `_emergency_council_parties:139` reads the stats a prior scene's echo moves — so the deferral is observable in *agôn today*, with no bargain anywhere near it (§1.9, §7.4) |
| *"removing the deferral risks a cascade inside the drain loop"* | **FAILS, measured.** `queue_scene` has exactly one caller in the tree, `queue_triggered_scenes` (`scene_dispatch.py:106`), and it runs before `dispatch_scenes` (`:421-422`). No re-entrancy today. A genuine cost avoided by checking rather than assumed |
| ⚠ *"Jordan's binding-in-scene ruling conflicts with PR #362 §C.4's act sequencing, so §C.2's `AX-4` clause needs a fourth case"* — **my own §3.4 (iii), first draft** | **REFUTED, against the primary text, and the refutation is the single most valuable result in this document.** `§C.4:576` flattens acts **across all scenes** into one ordered fold; `D-49:871` forbids *nesting*, not same-pass resolution; `:579` says a later act's `requires` is evaluated against `world_as_predecessors_left_it`. So two persons' acts already bind in one RESOLVE. **What looked like a conflict was a modelling choice of mine** — a bargain as two `commit` Tenures (`commit` ∈ `tenure_kinds`, `:475`, so `AX-4` clause 2 fires) rather than as one `Record` (`§B.4/B.5:249-261`, where it does not). I wrote the amendment before checking whether the shape it patched was forced. It was not |
| *"then at least the two-`commit` modelling is workable, just clumsy"* | **FAILS, and this is what killed it independently of the ruling.** `canonical_order` is `(stratum, actor-hash, intra-person position)` (`:576`) and `D-36:857` says rank never breaks a tie — so **nothing orders A's act before B's conditional commit.** About half the time B's commit folds first, refuses, and the bargain silently fails to bind. Order-fragile by actor-hash is broken on its own terms |
| *"`settle()` computing an NPC's assent violates `AX-1` — nobody acted for B"* | **FAILS.** `AX-1:71-74` forbids a non-person being *the subject of a decision*. A is the actor; B's floor is state B's own earlier acts set. A reservation price *is* revealed preference — the engine reads B's commitments, it does not choose for B |
| *"`contestant_from_person` is the one new adapter and it is necessary"* | **SUCCEEDS against my own N-line.** It has no producer in this tree, and `14_NERS.md` §3 row 6 says an object with no producer cannot have an N-line. Downgraded to conditional (§5.2 row 7); the first thing I would cut |
| *"the spine needs a `ContestRecord` for defect 4"* | **FAILS — a false N-line.** `LedgerTag` already does it, single-owner; the failure is composition, not absence (§5.2 row 4) |
| *"burden's stall semantics need a clock"* | **FAILS — a false N-line, and a textbook one.** `ProofBar:71-72` *is* the stall rule and `Venue.budget` is the clock (§5.2 row 6) |

### §9.3 Asymmetric skepticism check

`04_ners_audit.md`'s discipline: unfavourable and favourable results must clear the same bar.

I found two defects in the shape spec (§1.3, §1.8) and reported them loudly. I also **accepted six
elements as CONFIRMED**, and I should say what that acceptance rests on: for `GAMES`, `armature=` and
the two-return-shapes defect I read every anchor and the surrounding code. For `burden` I read the
proceedings table and the win conditions — which is what produced the S0/S1 amendment. For
`contestant_from_person` I confirmed the *absence* of `Person` rather than the presence of a design,
which is a weaker check, and that is exactly why it is the element I downgraded.

**The `SUCCESS_UNIT` fix is the asymmetry I am most exposed on.** I refused to invent values, which is
correct, but refusing to invent them means the spine's central mechanism ships uncalibrated and I
graded that mitigation more kindly than I would have graded someone else's. **Marked PROVISIONAL.**

### §9.4 "No dominant option" is an upper bound, everywhere

No AI-vs-AI best-response sweep was run — ED-SC-0021's falsifier remains unrun, and only combat has a
parity harness. Nothing in this document claims a balance property. Where it claims value-identity, it
claims it from *construction* (§7.1's three reasons) and names the run that would falsify it, which is
a different and weaker claim than a measured one until that run happens.

### §9.5 What an independent reviewer would add

1. **The whole document assumes the six `SUCCESS_UNIT` conversions are the right *shape* of fix.** An
   alternative exists that I considered and did not take: give each `WinCondition` an `ob` instead
   (`ProofBar`'s `bar`, `ThresholdRace`'s `T`) and call `degree_from_net(raw_margin, that_ob)`. It is
   arguably closer to the ladder's own semantics (`margin = net − ob`) and it needs **no new
   constant** for three of the six. I did not take it because `TallyAtClose` and `VoteAtClose` have no
   natural `ob`, so it solves half the problem and leaves the worst half (`VoteAtClose`'s 0.5 ceiling)
   untouched. **A reviewer should re-litigate this choice; it is the least-tested judgment here.**
2. **Self-review bias, marked** (`SESSION_BRIEF.md` §8.6): I verified the shape spec and then verified
   my own amendments to it, in the same pass, with no independent reader between. The two refutations
   (§1.3, §1.8) came from *running probes*, which is the part I trust; the S0/S1 split (§1.5) and the
   `band` compatibility field (§1.4 B) came from *reasoning about what would keep goldens green*,
   which is the part a critic should attack first.
3. ⚠ **A reviewer should ask why I wrote an amendment to PR #362 before checking whether the shape it
   patched was forced — and the answer is that I did not check, until I was told to.** §3.4 (iii) now
   records the refutation, but the process failure is worth naming on its own: I inherited "the
   conflict" from a summary and *specified a fix for it* rather than opening `§C.4` and reading the
   fold. Two lines of primary text (`:576` flattening across scenes, `:579`
   `world_as_predecessors_left_it`) dissolve it. **That is `CLAUDE.md` §0's adversarial-pass rule
   failing in the direction it is least often watched for: I attacked the shape spec hard and did not
   attack my own conflict claim at all.** A reviewer should assume the same asymmetry elsewhere in
   this document and probe the claims I was *given* rather than the ones I *found*.
4. **The Record-vs-`oblige` split (§3.4 iii) is a judgment, not a reading.** The text supports it —
   `Record` is not a Tenure, and `§B.4/B.5` already folds documents in — but PR #362 never says *a
   mutual seam outcome is a Record*, and I inferred it. **If a reviewer prefers per-claimant Tenures,
   the ruling then genuinely does require an `AX-4` amendment**, and it would have to read: *`§C.2`'s
   Tenure clause gains a fourth lawful case — `cause is a seam outcome this same act resolved, and
   id's subject is a claimant the seam returned` — bounded by `§C.5.1`'s frozen roster.* I do not
   propose it, because the Record route reaches the same behaviour without touching `AX-4` at all, and
   because the two-Tenure route is order-fragile on its own terms (§9.2). **Attack this first.**

### §9.6 Escalations

**Zero.** Every candidate was run through the five tests (`CLAUDE.md` §0, 2026-08-24) and closed:

| candidate | closed by |
|---|---|
| ED-SC-0020 (burden-parameterized gate) | **rungs 4 and 5** — `ProofBar:71-72` already implements the stall semantics Fork A proposes (precedent); one ladder plus one Margin leaves no room for four taxonomies (architecture). §1.5. **Mark it `resolved`.** |
| the negotiation binding question (`00_BRANCH_SHAPES.md` §3(k)1 — the shape spec's **only** escalation) | **rung 1, superseded** — Jordan ruled it 2026-09-04 (§1.9). The row should be closed with the ruling, not preserved |
| does the ruling reach the §5.5 Accord leg and combat echoes? | **rungs 4 and 5** — the ruling's own words are general, and `parliamentary_vote.py:214` is a live precedent for immediate binding inside the same procedure. What remains is execution and a deliberate golden re-pin, both IN/SE-owned. Not a Jordan question |
| the six `SUCCESS_UNIT` values | **rung 5, plus the tree's own `[SEED]` convention** — a calibration is not a ruling. `resolver.py:39-44` is the precedent for shipping one tagged and uncalibrated |
| the eight `burden` assignments | **not an escalation — a work item with named owners** (three branch documents, concurrently in progress) |

---

*End. `PROPOSED — nothing ratifies on merge.* Grade: **paper**. One file created; nothing else edited.*
