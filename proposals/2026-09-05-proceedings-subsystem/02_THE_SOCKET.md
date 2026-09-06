# 02 · THE SOCKET — what the season loop actually exposes, measured rather than assumed

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## This file describes the tree AT A COMMIT (`1b1e382`, 2026-09-05). Every *X is / X does* below is a
## fact at that commit and says so, per `04_CODE_ARCHITECTURE.md` §G.3.3.

---

> ### THE HEADLINE, BEFORE THE DETAIL
> **The season loop already has a hole shaped like this subsystem, and the hole has been measured.**
> `contest()` at `shape.py:6690` dispatches by module name; `rosters.yaml` declares four contest
> prizes; **exactly one of the four is called, and exactly one of the thirty-two verbs in the table
> declares `contests:` at all.** `Query.judging_set` — the function that would say who decides at a
> sitting — **raises `Unspecified` unconditionally** (`shape.py:3161-3163`), with the law text
> *"NOTHING IS DECIDED AT A SITTING."* And `(Person, coherence)` is the **one** matrix row whose
> write the gate licenses to a **`driver="Seam"`** (`shape.py:2829-2836`) — a socket wired for a
> subsystem that does not exist.
>
> **This design is not proposing to add a seam. It is proposing what goes in the one the loop
> already has, and it is proposing the thing the loop is missing at its own critical path.**

---

## 1 · The loop, in the order it runs

`SeasonDriver.season()`, `shape.py:6470-6486`:

```python
w.draw = 0                              # S33: the draw ordinal is per-TICK, so replay is exact
self.calendar()                         # step 1 — barrier 1 — DECIDES NOTHING (S24)
matter_events = self.matter(actorless)  # step 2 — barrier 2 — THE WORLD FREEZES AT ITS END (S25)
acts = self.deliberate(choose, ...)     # step 3 — a MAP, not a barrier (S26)
events = self.resolve(acts, contest_max_depth)   # step 4 — barrier 3 — the ONLY writing step for acts
for e in events: w.log.append(e)        #          S19.5 — ONE LOG, NOT TWO
deposits = self.witness(matter_events + events)  # step 5 — barrier 4 — THE JOIN (S28)
self.census()                           # step 6 — shares WITNESS's join (S29)
w.tick += 1                             # the ONE place the season advances
```

| step | lines | what it may write | relevance to a proceeding |
|---|---|---|---|
| **CALENDAR** | `5363-5381` | `Date.fired`; appends a `DocketItem` when a fired date is **vacant** | **this is how a proceeding is CONVENED.** A date comes due; nothing is decided |
| **MATTER** | `5384-5631` | the three motions; term maturation; **claim-confidence decay**; wear; band crossings | **this is how a summons ripens and how memory of a hearing fades** |
| **DELIBERATE** | `5634-5743` | **nothing** — no token exists in scope | **this is where a person decides whether to attend, and with what** |
| **RESOLVE** | `5745-6235` | every act, through the gate, as an **ordered fold** | **this is where the proceeding runs**, and the only place a contest may open |
| **WITNESS** | `6238-6452` | claim deposits into each holder's **own** ledger | **this is how the world learns what the hearing decided — differently per witness** |
| **CENSUS** | `6455-6467` | currently a no-op; demand-driven only | not reached by this design |

**Two consequences bind the design before it is written.**

1. **A proceeding can only run at RESOLVE.** `deliberate()` raises `Forbidden` if the world is not
   frozen (`shape.py:5637-5639`), and no write token exists in its scope. **So a hearing is not a
   phase of the season; it is one act's resolution, subdivided.**
2. **Everybody decides simultaneously, from a frozen world.** Nobody reacts to a same-season act
   (Stage 3 §D.1). **So a proceeding's internal back-and-forth cannot be modelled as people taking
   season-turns at each other.** It is a nested run on a shorter clock, which is exactly what
   `02_HIERARCHIES.md` §B.2 calls **process-nesting** — the second kind of nesting, bounded by
   nothing intrinsic and therefore requiring a **caller-supplied depth cap with no default.**

---

## 2 · The seam, exactly as it is built

### 2.1 The dispatch, and the branch that is source code rather than data

`contest()` — `shape.py:6690-6771`. Reached from RESOLVE at `shape.py:6106-6189`, gated on
`_contests = list(a.contests or ()) or ([_row.contests] if _row and _row.contests else [])`
(`shape.py:6115`) — the act names a contest, or its verb row does.

```python
# shape.py:6738-6748
if _sub["module"] == "personal_combat":
    import combat_seam
    out = combat_seam.resolve(w, claimants, causes, prize)
    if out.get("status") == "RESOLVED":
        TRACE.decision(f"contest for {prize!r} dispatched", "S39", ...)
        return out
    raise Unspecified(...)
```

⚠ **THE DISPATCH IS A HARDCODED `if` ON A MODULE NAME, AND THIS IS THE ONE PLACE THE ADDITION IS NOT
A DATA EDIT.** `rosters.yaml:441-446` maps prizes to modules; `contest_subsystem()`
(`shape.py:6493-6528`) resolves the name; and then a single `if` decides whether anything is
actually called. Every other declared prize falls through to `raise Unspecified` whose own text is
*"mass_battle and social_contest still resolve to a name only"* (`shape.py:6765`).

> **This is a defect by the architecture's own rule and it should be named as one before it is used
> as a template.** `04_CODE_ARCHITECTURE.md` §C.5 specifies `provider = manifest.resolve("contest",
> prizes[prize])` — **resolution by declaration, at boot, by string** (`02_HIERARCHIES.md` §D.4:
> *"the engine names the ROLE, the registry names the MODULE, resolution happens by string"*). A
> literal `if module == "..."` is `G.2.6`'s *resolution is a row, never an import, never an
> inference* violated at the one site the whole seam exists to protect. **The honest statement is
> that the executable chain has not yet built the manifest, not that a second `if` is the way in.**
> This design therefore specifies a **manifest row**, and registers the `if`-branch as the
> compatibility shim it is — a `PROVIDER` hole, not a pattern to copy.

### 2.2 The one built provider, and the four disciplines worth copying

`combat_seam.py` (184 lines). Its public contract:

```python
resolve(w, claimants: list, causes: list, prize) -> dict
#   status ∈ {"RESOLVED", "PARTY-GAP", "ENGINE-UNAVAILABLE"}      -- a closed vocabulary
#   on RESOLVED: module, resolver, result(+1/-1/0), winner|None,
#                wound_state{id: {...}}, unresolved(bool), bouts, parties, seed
```

| discipline | where | why it transfers to a proceeding |
|---|---|---|
| **derive exactly ONE field from something the actor genuinely has; leave every other input at the target's own constructor default** | `combat_seam.py:21-27, 109-122` — `Person.body` → `Combatant.end`, via the registered `body_band_penalty` | a proceeding is far more tempting to over-derive. **The discipline is the defence against inventing a rhetoric stat block** |
| **return a typed gap, never a stand-in** | `derive_party` returns `None`; `resolve` returns `PARTY-GAP` | a proceeding with one party, or with no seat that can decide, must **refuse in a named way** rather than resolve to nothing |
| **seed from the world's own clock and the causing act** | `seed = int(S.H(w.world_seed, w.tick, a_id, f"contest:{prize}:{causes[0]}"), 16)` (`:150`) | replay exactness is not optional; the same season must produce the same hearing |
| **READ the degree off the scene; never MAP it from the winner** | `:158-176`, and the Jordan ruling of 2026-09-03 quoted in the module header | **the single most important one.** See §2.3 |

### 2.3 The degree, and the rule that governs every subsystem including this one

⚠ **JORDAN, 2026-09-03, carried in `combat_seam.py`'s header and in `04_CODE_ARCHITECTURE.md`
§C.4:** *"kill/wound degrees should be directly taken from scene combat, which is what actually needs
to be called when kill/wound is considered."*

> **The degree is READ OFF THE SUBSYSTEM, never mapped onto it by the table.** A contested verb's
> branches are named by **what its subsystem can actually distinguish**, and where the subsystem
> distinguishes fewer states than a four-band ladder, **the verb declares fewer branches rather than
> the table inventing the difference.**

The worked instance is exact and instructive: `wrapper.fight` returns `+1/-1/0` and **throws away
what it computed**; the seam still holds the `Combatant` objects, each carrying a `WoundTracker` with
`felled`, `wounds`, `max_wounds`, `health_remaining`, `health_full` — *"the severity of the outcome
was computed by scene combat and is sitting on objects this module owns."* The seam reads it before
it is lost. **The degree was never missing; it was thrown away at the return.**

`degree_of()` (`shape.py:6653-6688`) recognises exactly **two** result shapes today:

| shape | branch | state |
|---|---|---|
| `"wound_state" in result` | `combat_degree(result, subject)` → `Felled \| Wounded \| Untouched` | **live** |
| `"net" in result and "ob" in result` | `degree_ladder()` → `engine/autoload/dice_engine.py::degree_from_net` | ⚠ **a reader with no producer** — `shape.py:6553-6561`: *"NOTHING PRODUCES A `net` ANYWHERE IN THE TRACER"* |

⚠ **THE SECOND BRANCH IS THE ONE A PROCEEDING WOULD USE, AND IT HAS NEVER RUN.** The margin-graded
path exists in code, imports the one ladder, and has never been fed. `H-31` — *the degree ladder's
margin model* — is the register row. **That is a hole this design must fill with a producer, and it
must not fill it by inventing band edges.**

### 2.4 What comes back, and what the caller may do with it

```python
# shape.py:6182 — the fold's contest branch
produced = self._fold(w, a, Resolution(degree_of(r, _target), r))
```

`degree_of(r, _target)` — and `_target` is **the act's `payload["subject"]`, deliberately not "the
loser"** (a corrected defect, `verb_table.yaml:303`). The token plus the raw result are wrapped in
`Resolution(degree, result)` (`shape.py:6618-6628`) and handed to `_fold`, where
`row.writes_at(degree)` / `row.emits_at(degree)` (`shape.py:1511-1543` / `1476-1509`) select the
degree-keyed branch.

**The caller is forbidden from inventing a mapping.** All it may do is pass the subsystem's own
report through a table-driven lookup keyed on the token `degree_of()` derived.

---

## 3 · The five things the loop is missing that a proceeding needs

This is the part that makes the subsystem worth proposing now rather than later: **four of these five
are already on the executable chain's own critical path, and the fifth is the register's largest
open governance row.**

| | what is missing | the evidence, at this commit | on the critical path? |
|---|---|---|---|
| **1** | **`Query.judging_set` — who decides at a sitting** | `shape.py:3161-3163` raises `Unspecified("judging_set_rule", "S61", needs="who decides at a sitting", law="S61 — NOTHING IS DECIDED AT A SITTING")`. Register row `H-32`, graded **absent**, `default: none` | **YES — `PLAN.md` `W26 — THE SITTING DECIDES`** |
| **2** | **`determine` — the verb that decides a matter** | `verb_table.yaml:168-178`, `eligibility: ["remit:determine"]`, `writes: ["Tenure.degree"]`, `emits: ["matter.determined"]`, **`grade: "absent"`**, `requires: "a fired Date with a DocketItem; judging_set — D11, absent"` | **YES — via W26** |
| **3** | **a producer for the margin-graded degree branch** | `shape.py:6553-6561` — *"nothing produces a `net` anywhere in the tracer"*. `H-31` | beside — but it is the branch a proceeding uses |
| **4** | **`Tenure.degree` — a field with a writer and no reader** | written by `determine` (`verb_table.yaml:174`); `Stage 4 §F.4` grades it *"a field with a writer and no reader"*, and `ID-13` says a field nothing reads is not a field | **it is `F.4`, the standing candidate for `G.1`'s falsifier** |
| **5** | **a parliament, a council, a delegation of any kind** | `H-90` lists *"PARLIAMENT (does not exist)"*; `rosters.yaml:466-469` — *"a Duke can assign a governor… assign a **council**… or allow for mayoral elections… **NOT BUILT**: this roster is the ladder only, and delegation is registered as open"* | **it is the largest open governance row** |

> ### **AND `(Person, coherence)` IS A SOCKET WIRED FOR PRECISELY THIS AND NOTHING ELSE.**
> `write_matrix.yaml:175-181` — `steps: [RES]`, `class: ACTS`, `social: false`, `emits:
> coherence.changed` — and `World.write` special-cases it (`shape.py:2829-2836`) to **require
> `driver="Seam"`.** It is the only field in the matrix the gate licenses a seam to write.
> `04_CODE_ARCHITECTURE.md` `F.5` asks what reads it and answers: *"carried unread, flagged for
> deletion — if the social-contest wrapper's margin reads it, social contests are undecidable."*
>
> **So the tree contains one field reserved for a seam that decides proceedings, and that field is
> currently a candidate for deletion under `ID-13` because the seam was never built.** Either this
> design gives it a reader and a writer, or the honest act is to delete it. **Both outcomes are
> results; carrying it unread for another revision is not.**

---

## 4 · The prize sockets — and a decision that is Jordan's, not this design's

`rosters.yaml:441-446` declares four contest prizes:

```yaml
prizes:
  "the body":       "personal_combat"      # CALLED
  "a field":        "mass_battle"          # named only
  "a standing":     "social_contest"       # named only
  "a proposition":  "social_contest"       # named only
```

⚠ **`H-120`, measured 2026-09-04: three of the four declared prizes are claimed by NO VERB.** Exactly
one row in the thirty-two-verb table carries `contests:` at all (`kill / wound`,
`verb_table.yaml:254`). **So even if the seam called those modules, nothing in the loop could reach
them.**

> ### **THE DECISION, STATED RATHER THAN TAKEN.**
> Two of those four sockets are mapped to a module named `social_contest`, which `H-120` records
> Jordan as calling, on 2026-09-04, *"an unfinished engine."* **This design was directed to be a
> from-scratch derivation that does not build on prior social-contest work, and it is one.** That
> leaves a naming and routing question which is a ruling and not an engineering call:
>
> | option | what it means |
> |---|---|
> | **(a) new prizes, new provider** | this subsystem declares its own prize(s) and its own manifest row; the two `social_contest` rows are left exactly as they are, claimed by no verb, and their disposition stays open |
> | **(b) claim the existing sockets** | `"a standing"` and `"a proposition"` route to this provider instead; the previously named module is superseded at the roster row |
>
> **This directory assumes (a) throughout and marks every site where (b) would differ.** The reason
> is `ID-5`'s polarity — absence refuses, it does not default — and the reason it is not decided
> here is that (b) supersedes somebody else's work by editing one line, which is exactly the kind of
> quiet ratification `CLAUDE.md` §2 says must be **loud** or not done at all.

---

## 5 · What the tracer has that the meta-architecture does not, and vice versa — stated so the design does not silently assume either

**A design written only against `04_CODE_ARCHITECTURE.md` will name types the executable chain does
not have.** The divergences that matter here:

| meta-architecture (Stage 4) | tracer, at this commit | consequence for this design |
|---|---|---|
| `Receipt`, minted only by the gate; `Event.changes : Receipt[]`; append asserts every receipt is in the minted set | **no `Receipt` type exists.** `Event.changes` is a fold-built `StateChange[]`; `Event.__post_init__` checks only `causes` | `H-1g` in `HANDOFF_NEXT.md` — the append-side integrity check has **no implementation**, at **eleven** append/extend sites. **This design must not claim its Events are gate-verified.** It may specify the property and must grade it `absent` |
| `Person.beliefs` **deleted** — a belief is a `commit` to an `OUGHT` Proposition | `Person.beliefs: list[tuple]` still on the dataclass (`shape.py:2372`) | the design specifies the Stage-1 shape and registers the tracer's field as the migration it implies |
| `Tenure.conferrer` deleted; `Tenure.term(matures_at, declared_by, closer)` | `Tenure` carries `degree`, `payload`; **no `term`** | `T-n` — *every opener declares its terms* — is the mechanism a summons, a term of service and a stay of proceedings all need. **It is not built** |
| `Act.via : SeatId?` — how a seat enters an act | **`Act` has no `via`** (`shape.py:2333-2355`) | `H-108`: *"delegation unbuildable."* An adjudicator acting **as** a seat cannot currently be spelled, and the gate's `T-o` check (`§C.2`) has nothing to read |
| four write tokens minted only by the driver | `WriteClass` + a `Step` check inside `World.write` | equivalent in effect, weaker in grade. Record it, do not overclaim it |
| `explain(p, v) -> Derivation`, person-side, no `World` | **does not exist** | the player-facing contract (`07_THE_GAME.md`) specifies it and grades it `absent` |

`[CONFIDENCE: high — every row above is a direct read of the named file at commit 1b1e382. The line numbers in §2 were reported by an independent read-only mapping pass and spot-checked against `combat_seam.py`, which was read in full.]`

`[ASSUMPTION: that the executable chain (`proposals/2026-09-01-season-loop-tests/`, `proposals/2026-09-02-executable-architecture/`) is the surface this subsystem must fit, and the meta-architecture (`proposals/2026-09-03-meta-architecture/`) is the shape it must obey — basis: `HANDOFF_NEXT.md` conditions #357 against #358 and treats the first as the executable expression of the second. Where they disagree, this directory follows Stage 4 and registers the tracer's divergence, per §1's currency rule that the later governing document governs.]`
