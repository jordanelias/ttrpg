# 02 · THE BUILT WORLD — settlements and their buildings, infrastructure, fortifications and works, as the expression of factions and the contents of their holdings

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Method: `opus` (`claude-opus-5`), per `CLAUDE.md` §10 — the authoring tier for *"large-context synthesis"* and *"contract closure"*. A reconciliation stage at tier `fable` (read-only by role, §10's audit/guardrail node) adjudicated every disagreement before this file was written; this file writes that adjudication rather than re-deriving it. Lane **SE**, id **ED-SE-0052** (`registers/editorial_ledger_se.jsonl:52`).
## Scope pin: every `path:line` below was opened in this session against the working tree. Every count was produced by running the thing that would have shown it wrong (`CLAUDE.md` §0.1 pt 3). **Grade under §0.2: `paper`** — ⚠ **§D.15 says what would move it** (~~§D.9~~: there is no §D.9, only the falsifier row `BW-9`, and the grade section is **D.15**; orphaned pointer repaired 2026-09-17).
## ⚠ **UNIFIED 2026-09-17 (`00_THE_DESIGN.md`).** Suite-wide: **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`, **`AX`** = `architecture/meta/01_AXIOMS.md`; a bare `01`/`02`/`03`/`04` means a file in THIS directory. This file's falsifiers are **`BW-n`** and its loops **`BW-L±n`**. The multi-season construction is **a `works`** (`01` §A.12's ruling, binding on the suite), never *a work* or *a project*. Reconciliation edits are struck in place.

---

> **Jordan, this session, which is the sentence that reverses a prior cut:** *"a player whose character
> can govern a settlement would like to be able to explicitly set policies or advance a project to
> build something."*
>
> **And the clause this file exists to make false**, `architecture/meta/04_CODE_ARCHITECTURE.md` §F.20
> (at `:1082`), verbatim: *"⚠ **FOUNDING VERBS** — no stage names a verb that founds a hearth or builds
> a site | the rows are dropped until a verb is ruled | **the world only decays — nothing is ever
> founded or built.** This is what blocks build step 2."*
>
> ⚠ **THE SECOND QUOTATION IS THE FALSIFIER OF THE FIRST.** §F.20 is not a gap this file closes by
> being written. It closes when a `rung.founded` and a `site.built` Event appear in a run's log, and
> **MEASURED THIS SESSION, one season of `build_realm(0)` emits neither.**

---

# PART A · WHAT A BUILT THING IS, AND WHOSE IT IS

## A.1 · The ontology — the fabric is a `Site`, the address is a `Rung`, and the seam is occupancy

The tree's type system already split a building in half and never joined the halves. `Rung` answers
*who is addressed here* and *what is kept here* and has no condition:
`_DECLARED = {"id", "kind", "stores", "sites", "records", "dates", "stake", "envelope",
"transmission", "judging_set_rule", "yield"}` with `__setattr__` raising on anything else
(`engine/season/state/carriers.py:568-569`, gate at `:590`). `Site` answers *what may be done here*
and addresses nobody: `Site := (id, rung, kind, condition, drawers[])`
(`carriers.py:411-418`; the same shape at `architecture/holonic_ARCHITECTURE.md:441`), where
`condition` *"is PRIMARY STATE, a FIXED-POINT INT (S48), and it GATES VERBS (S12.1)"*
(`carriers.py:412-413`).

**MEASURED, `build_realm(0)`, this session (re-run 2026-09-17, unchanged):** 211 `hearth` rungs — the
rows `venues.yaml` calls buildings, which A.1.2 narrows to **the plots buildings stand on** — and 74
`Site`s, every one of the 74 keyed to a `settlement` rung. The two populations are disjoint by construction. So the
211 buildings cannot wear, cannot be damaged, cannot be repaired and cannot be lost; and the 74
fabrics house nobody.

| candidate | who would own it | verdict |
|---|---|---|
| a built thing is a **`hearth` `Rung`**, full stop (ED-IN-0223 read widely) | `Rung` | **NARROWED.** Right about the ADDRESS, silent about the FABRIC — and the silence is why `venues.yaml` carries 211 buildings and not one wall |
| a built thing is a **`Site`**, and its `rung` is the plot it stands on | `Site` for the fabric, `Rung` for the plot | **TAKEN** |
| a built thing is **one object** — put `condition` on `Rung` | `Rung` | **REFUSED** on cardinality — A.1.1 |
| a built thing is a **new carrier** (`Building`, `Facility`, `Work`) | itself | **REFUSED.** Seven live functions key on `w.rungs` to answer *where is somebody* — `parent_of` (`engine/season/queries/world_q.py:48`), `descendants` (`:54`), `home_of` (`:150`), `presence` (`:172`), `footprint` (`:254`), `density` (`:276`), `World.contain_ascends` (`state/world.py:197`) — and `contain_ascends`'s ladder walk (`:220-221`) has no meaning across two address types |
| a **third** type for works, beside habitations | itself | **REFUSED** on `01_AXIOMS.md` **ID-7** (`:444`, *"One type, many kinds… refuse the subclass"*): a wall and a mill wear by the same subtraction, and two code paths drift |

> ### RULED: **A BUILT THING'S FABRIC IS A `Site`; ITS ADDRESS IS THE `Rung` ITS `Site.rung` NAMES. THE PLOT AND THE FABRIC ARE TWO OBJECTS AND ONE BUILT THING, AND THE SEAM IS OCCUPANCY — DERIVED, NEVER STORED.**
>
> ```
> occupiable(w, site) ⇔ w.rungs[site.rung].kind == "hearth"
> ```
>
> No `is_occupiable` field, no second type, no subclass. Cited to `01_AXIOMS.md` **ID-7** (`:444`) for
> one type/many kinds, and to `holonic_ARCHITECTURE.md:444-451` for why `condition` is primary state
> on the `Site` rather than an aggregate anywhere.

Three consequences follow from that one read, which is what makes it **one seam and not three rules**:
a fabric whose `rung` is not a `hearth` can take no `contain` edge (`contain : Rung → Rung`,
`holonic_ARCHITECTURE.md:539` — and there is no rung), can hold no date and can hold no store (`dates[]`
and `stores` are `Rung` fields, `carriers.py:568`). **A wall has no household, therefore no hearth,
therefore none of the three** — not a special case for walls, but what *nobody lives in a wall* means
in this vocabulary.

### A.1.1 · ⚠ THE ARGUMENT THAT LICENSED THIS IN THE DESIGN PASS IS UNSOUND, AND IS STRUCK RATHER THAN QUIETLY REPLACED

The design pass refused the one-object collapse like this, and the refusal is right while the argument
is not:

> ~~"`StateChange.destroy` sets `until = tick` on every Tenure whose subject or object is the
> destroyed id, so under the collapse **a rampart and its quarter are one object, and breaking the
> wall destroys the district and every building in it.**"~~

⛔ **UNSOUND, and an antagonist pass found it.** Opened: `holonic_ARCHITECTURE.md:588-589` says
*"`destroy` sets `until = tick` on every Tenure whose subject or object is the destroyed id, and
**destroys nothing else.** It does not cascade into other carriers."* That is a rule about **which
Tenures end when an object is destroyed** — it says nothing about **which objects may be destroyed**.
And nothing in the tree destroys a `Rung` or a `Site` at all: `(Rung, exists)` and `(Site, exists)`
are declared at `engine/season/write_matrix.yaml:294-300` and `:322-328` with **zero producers**
(§F.20; `H-41` graded `absent` at `engine/season/hole_register.yaml:462-467`), so the destruction the
argument feared has no spelling. **A conclusion licensed by a step that does not hold is a finding
wearing a pass's clothes**, and it is struck here rather than left to be discovered.

**THE REFUSAL SURVIVES ON CARDINALITY INSTEAD, and cardinality is measured rather than argued.**
`holonic_ARCHITECTURE.md:449-451`, opened, verbatim: *"**Node-keying destroys site identity and yields
two wrong answers at once** — a settlement holding a silted harbour at `0.1` and a healthy seam at
`0.9` collapses to `~0.5`, which keeps the bulk shipping verbs the harbour should have closed and
closes the mining verbs the seam should have kept."* Put `condition` on `Rung` and that collapse is
exactly what you have built, because the cardinality is not 1:1 in either direction:

- **many fabrics, one address.** `engine/season/harness/populated.py:369-374` mints one Site per
  producing kind at each settlement, so `set_S-018` today carries a `harbour` **and** a `seam` at one
  rung. Measured: `{harbour: 37, seam: 37}` over 37 settlements.
- **one address, no fabric.** All 60 `community` rungs and all 211 `hearth` rungs carry none.
- **and a field on a type is available to every kind of that type.** Give `Rung` a condition for
  `hearth` and you have given it to `realm`; the type system cannot scope a field to a kind, so the
  settlement's condition is then precisely the node-keyed average `:449-451` forbids. `ARCH §B.4` states
  the same thing from the other side: *"Node-keying is structurally unwritable: a Rung has no
  condition field, so the collapse cannot be spelled."*

**Direction of the loss: vertical.** The fabric sits at a finer grain than the address it hangs from,
and collapsing the grain deletes the finer one.

### A.1.2 · ED-IN-0223 is NARROWED, not overturned

`engine/season/venues.yaml:20-25` rules, and it is a mechanism rather than reference by its own
declaration at `:15-18` (*"`engine/season/harness/populated.py` opens it at runtime and the rungs it
builds come from these rows"* — verified: `populated.py:355-364` builds every quarter and building
from it): *"A BUILDING is a `hearth` — the rung a person is seated in. A QUARTER is a `community` — a
group of buildings inside one settlement."* The ruling is `ED-IN-0223`, status `landed`
(`registers/editorial_ledger_in.jsonl:84`).

> **A BUILDING IS NOT A HEARTH. A BUILDING STANDS ON ONE.** `hearth` is the address tier below a
> quarter — **the plot.** The fabric is what stands on the plot. The ruling is right about occupiable
> buildings and silent about the rest, and the silence is the defect rather than the ruling: it did not
> put walls in the wrong box, it had no box, so walls do not exist.

**Two things the narrowing buys, both checkable.** (1) **Founding becomes expressible**: you found the
plot, and then you build on it — two write-matrix rows with two emissions, which is what
`write_matrix.yaml` has declared all along. (2) It repairs a live `CLAUDE.md` §4 **idempotence**
failure, which is the test §4 states: a reader with no memory of this repo, told *"a Cathedral is a
hearth"*, does not land on the intended meaning — a hearth is a fireplace or a household and a
cathedral is neither. Told *"a cathedral stands at a hearth, which is the plot it occupies"*, they do.
**The rung kind keeps its roster name** — `rung_kinds` is
`[person, hearth, community, settlement, territory, province, duchy, realm]` at `rosters.yaml:106-109`,
and it is load-bearing on `World.contain_ascends`'s ordinal walk (`state/world.py:220-221`). **The
SENTENCE changes, not the roster.**

**Cost, stated:** each of `venues.yaml`'s 211 building rows gains a site-kind column, and it is
world-generation content — lawful under `01_AXIOMS.md:178-179` (*"A world-generation roster is not a
clock and is lawful"*).

---

## A.2 · Five site families, each discriminated by which EXISTING table its condition band reaches

A dwelling, a granary, a wall and a mine are not one category, and the discriminator is not the
fiction. **It is which column of which existing table the site's condition band reaches.**

| family | kinds (illustrative) | what its condition gates | the reader column | destruction removes |
|---|---|---|---|---|
| **PRODUCER** | `croft · field · seam · harbour · mill · quarry` | the rung's `yield` at MATTER | `site_yield[kind]` — **exists**, `rosters.yaml:1146-1173`; scaled by `condition/condition_scale` at `engine/season/loop/matter.py:205-209` | a source of matter |
| **VESSEL** | `granary · warehouse · cistern · byre` | how much the rung may KEEP | a bound on `Rung.stores`, which is an unbounded `dict` today (`carriers.py:568`) — **the one genuinely absent reader column** | the bound on a surplus, and the surplus |
| **ENCLOSURE** | `rampart · gate · ditch · tower · keep` | **somebody else's** verb at this rung | `band_floors[kind]` — the mechanism **exists**, `rosters.yaml:1175-1199`; the kind does not | a refusal |
| **HALL** | `moot_hall · guildhall · minster · chapter_house` | whether a sitting may `convene` here | `band_floors[kind]`, read by `convene`'s `requires` | a venue |
| **DWELLING** | `cottage · townhouse · longhouse · barracks` | how many persons this rung may address | `capacity(w, rung)` — A.7 | the shelter |

> ### RULED: **THE FAMILIES ARE ROSTER ROWS, NEVER CARRIERS, AND THE DISCRIMINATOR IS THE RULE: *A KIND THAT REACHES NO NEW COLUMN IS NOT A NEW FAMILY.***
>
> A bakery that only produces is a PRODUCER with a different `site_yield` row. A gatehouse that both
> refuses an attacker and quarters a watch is **two** Sites — an ENCLOSURE at the quarter and a
> DWELLING at a hearth — because it does two things and they can be lost separately. Cited to
> `01_AXIOMS.md` **ID-12** (`:454`, *"A closed set lives in data"*) and to `rosters.yaml:809-812`,
> whose own note is the refusal that makes the roster safe: *"Adding a kind means adding a row here;
> asking about a kind that has no row RAISES."*

**THE BASELINE IS TWO, NOT THREE, AND THE ROSTER SAYS SO ITSELF.** `site_kinds` is
`[harbour, seam, body]` (`rosters.yaml:816` — ⚠ line repair 2026-09-17, ~~`:817`~~ is blank) and its own
note at `:814-815` reads: *"⚠⚠ `body` IS NOT
A SITE. It is `(Person, body)`'s band row, here because `band_floors` keys on THIS roster."* So the
tree has **two** site kinds. Five families is therefore not a richer taxonomy than what exists — it is
the first taxonomy, replacing an absence.

**What a new kind COSTS, measured at the loader rather than asserted.**
`engine/season/data/fixtures.py:106-123` checks `wear_per_season` and `band_floors` against
`site_kinds` **in both directions**: a table keyed past the roster raises `Forbidden`, and a roster
member with no row raises `Ungraded` (*"a wear table that returns 20 for an unregistered site kind
does not fail — it answers, plausibly and wrongly, forever"*). `site_yield` is checked one way only
(`:124-129`). **So every family lands with a `wear_per_season` row and a `band_floors` row or the world
does not load** — which is `ID-5`'s refusal doing the work a convention would not, and it is why the
data rows are mandatory rather than defaulted.

⚠ **AND EVERY NUMBER IN ALL THREE TABLES IS AN INJECTED DEFAULT WITH A SWEEP, NOT A RULED VALUE.**
`site_yield` is `H-93` with `sweep: [declared, uniform, none]` (`rosters.yaml:1150`) and its own note
*"⚠ WHAT A HARBOUR PRODUCES IS INVENTED"* (`:1153`); `band_floors` is `H-08` with *"⚠ THE FLOORS ARE
INVENTED"* (`:1186`); `wear_per_season` is `H-07`, all three kinds at `10` against
`condition_scale = 1000` (`rosters.yaml:841-844`; `fixtures.py:160`). **No claim about pacing may be
made anywhere in this document**, and none is. The wear-to-restore ratio is the corpus's own *largest
unmeasured number*, and it sets not a difficulty slider but **where every site in the world sits at
rest.**

---

## A.3 · Fortification — an ENCLOSURE `Site` whose CONDITION IS ITS STRENGTH

**What fortification is today: a type and a stat.** `venues.yaml:50-51` spells it as a settlement kind
plus two quarter names (`Fortress-City: [ward, muster_field]`, `Fortress: [ward]`) whose buildings
(`keep`, `gatehouse`, `armoury`) are `hearth` rungs built at `populated.py:359-364` and therefore
**cannot be damaged, repaired, breached or lost**. Beside that, the superseded tree carries
`fort_level` as an int feeding `Garrison Strength = Defense × 20 + Fort Level × 30`
(`systems/settlements/sim/registry.py:66`; formula at
`systems/settlements/reference/settlement_layer_v30.md:48`) with no construction act, no cost and no
decay.

| candidate | who would own it | verdict |
|---|---|---|
| a **Query** over what a place contains | Nobody | **REFUSED.** A Query stores nothing (`holonic_ARCHITECTURE.md:591`, *"never stored, always recomputed"*), and a fortification must hold damage across seasons. It cannot carry the state |
| a **property of a built `Rung`** | `Rung` | **REFUSED** — it needs `Rung.condition`, refused at A.1.1 |
| a **scalar** (`fort_level`, `defense`) on anything in the head | whoever declares it | **REFUSED** as the head's representation — `01_AXIOMS.md`'s R7 sibling ruling (`references/design_rulings_2026-09-06.md:169`): *"no magnitude carrier is admitted at any scale. Every aggregate is DERIVED, none is PUSHED"* |
| an **ENCLOSURE-family `Site` whose condition is its strength** | `Site` | **TAKEN** |

> ### RULED: **A FORTIFICATION IS AN `ENCLOSURE`-FAMILY `Site` WHOSE `rung` IS THE QUARTER IT ENCLOSES. ITS CONDITION IS ITS STRENGTH — BANDS, NOT A LEVEL — AND WHAT IT GATES IS SOMEBODY ELSE'S VERB.**
>
> ```
> band_floors.rampart:
>   holds_a_gate:  <lo>     # below this the quarter has no closable edge
>   shelters:      <mid>    # below this the fabric gives no cover
>   mans:          <hi>     # below this the walk cannot be manned
> wear_per_season.rampart:  <masonry in weather>
> site_yield.rampart:       { }        # a wall produces nothing. It only costs.
> ```
>
> Three bands, not a level, and the difference is not cosmetic: a band is a read off a field with
> exactly one writer per write class (`write_matrix.yaml:315-321` — `(Site, condition)`, `steps: [MAT,
> RES]`, `class: MATTER/ACTS`), where a level is a second authored ladder for a quantity the tree
> already has. **One rampart per QUARTER, not per settlement**, which gives the `community` rung an
> N-line it does not have today: a Fortress-City's `ward` can stand while its `muster_field` has
> fallen, so **a besieger picks a quarter.**

### A.3.1 · Three reads, each onto a mechanism that already exists. **NO SIEGE SUBSYSTEM.**

**1 · THE BATTLEFIELD, when the wall is intact.**
`systems/mass_battle/reference/mass_battle_v30.md:543` already carries the row, opened and verbatim:
`| Walls / fortifications | Defender +3 DR; no flanking; Slow cannot advance |` — an **environmental
selector**, a terrain row, not a stat. The reading is: a mass-battle provider's IN-side calls
`verbs(w, enclosure_site, band_floors[kind])` (`world_q.py:133-137`) at the contested rung and passes
that terrain row **iff `mans` is in the returned set.** The seam already receives the rung —
`contest(w, rung, prize, claimants, …)` at `engine/season/seam/contest.py:74`. ⚠ **The cost is one read
inside a wrapper that does not exist**: `mass_battle` has no registered provider, so this read has
nothing to read yet, and saying otherwise would be claiming a mechanism.

**2 · THE CHOKEPOINT — a band refusing a `move`, and this is the sharpest reuse available.**
Canon's rule, opened at `settlement_layer_v30.md:912`: *"A Fortress settlement in the invader's path
forces engagement — it cannot be bypassed unless the invader's Military exceeds the Fortress Defense
by 3+."* Re-expressed with **no new mechanism and no stat comparison**: bypass is a `move` whose
`contain_path` conjunct runs through the rung, and a standing enclosure at that rung refuses it.

*As execution, precisely:* `move`'s row is `eligibility: ["own"]`,
`requires_typed: {form: contain_path, of: actor, to: to}`, `emits_on_refusal: ["travel.blocked"]`
(`engine/season/verb_table.yaml:361-372`). The typed form is evaluated by
`ContainPath.check` (`engine/season/data/requires.py:252-278`), which observes the stem
`contain.path:{dest}` off a reader; the resolver-side answer lives in **one** place,
`WorldReader.read`'s `contain.path` branch (`world_q.py:670`, branch at `:732-737`), today a
shared-ancestor test. **The reading adds one conjunct in that one branch** — a path is not a path if a
standing ENCLOSURE lies on it and the mover is not admitted. `travel.blocked` already fires: measured,
**23 times in one season** of `build_realm(0)`.

⚠ **AND THE FORM CANNOT NAME THE WALL AS AN OPERAND, WHICH IS WHY THE READING GOES IN THE PREDICATE.**
`contain_path`'s `needs:` is `[actor, subject, from, to]` (`rosters.yaml:1118`) — **no `site`** — and
`requires_forms` is **CLOSED AT SEVEN**, where *"A cell naming a form outside this roster REFUSES AT
LOAD, because an eighth form is a new thing a precondition can ask and that is a design change, not a
table edit"* (`:1092-1094`). So the enclosure must be read by the predicate off the world, never bound
as a cell operand. **That is a constraint the roster imposes, not a workaround**, and it is the reason
this reading costs one branch rather than an eighth form.

**3 · THE SIEGE — a contest grading a negative condition delta, and nothing more.**
A besieger does not roll against the wall. A `contest` at the rung returns a degree the fold grades
into a **negative `(Site, condition)` delta** — the same channel a repair uses with the sign flipped,
already licensed at `[MAT, RES]` (`write_matrix.yaml:315-321`). Several besiegers commute by
construction, because `engine/season/loop/resolve.py:538-553` **sums every delta and clamps once**,
`max(0, min(scale, …))` at `:549`, and its own TRACE records the alternative it refused (*"clamp per
delta (arrival-order dependent)"*). **No new write class, no new step, no new carrier, no new degree
ladder** — and no siege object anywhere.

**A consequence nobody chose, which falls out of an ordering that shipped for other reasons:** the
strata are `[movement, binding_decision, contested_physical, uncontested_material, social]` and
*"ORDER IS SEMANTIC HERE"* (`rosters.yaml:138-146`). A siege is `contested_physical`; a repair is
`uncontested_material`. **So a defender cannot patch a breach in the season it opens, and must
pre-invest.**

**A wall's resistance is not a number, and that is why the row asking for one has no answer.** It is
the verbs it removes from the attacker, the verbs it grants the defender, and the seasons it takes to
grade it down through three bands. `01_AXIOMS.md` **T-g** (`:353`, *"Obstruction needs no verb"*) is
the distinction: an obstacle is rolled against; an obstruction is not rolled against at all. **A wall
is an obstruction.** And a garrison is not a troop type: it is `presence(w, ward)`
(`world_q.py:172-177`) filtered by who is bound to keep the walk — which is the precedent corpus's one
four-of-four convergence, *"garrison-versus-field as the same unit pool wearing a different
assignment"* (`research/valoria_game_precedent_companion_v1.md:323-326`).

### A.3.2 · The epistemic half — **the band may never be rendered as fact**

> **A WALL'S CONDITION IS WORLD TRUTH. WHAT AN ATTACKER HOLDS IS A CLAIM ABOUT IT, AT A CONFIDENCE
> THAT DECAYS.**

This is not decoration; it is what the two readers already enforce. The typed predicate is evaluated
against **`WorldReader`** at RESOLVE (`resolve.py:187`) and against **`LedgerReader`** person-side
(`epistemic.py:99`). A relation the reader cannot answer returns `UNKNOWN`, *"so an unimplemented one
refuses rather than admitting"* (`requires.py:283-286`). And `Claim.confidence` already decays at
MATTER, writing through the gate and emitting `claim.decayed` (`matter.py:147-153`).

**So a defender who lets the walls rot and tells everyone they are sound is a play the design supports
with no new mechanism**, and an attacker who storms on a stale claim is `AX-2` working rather than a
bug. The presentation hazard is where this usually breaks, and it is refused by name: a viewer shown
the true band has been handed world truth through the interface layer, so
**a fortification's band is rendered as the viewer's own estimate or not at all.** `ARCH §C.11`
(`:758-761`) is why the obvious escape fails — *"the player CONTROLS a person… for a player character
the player IS the decision procedure"*, so anything shown before they declare is shown inside a
decision — and R7 composes with it: *"a ruler can be wrong about their own standing… the player sees
their character's ESTIMATE, never the true aggregate"*
(`design_rulings_2026-09-06.md:181-184`).

### A.3.3 · ⚠⚠ `fort_level` AND `facility_tier` ARE **NOT** FREE CUTS. THE CUT IS WITHDRAWN AS A BREAKAGE.

The design pass listed both as free cuts. **Both claims are false, and cutting either is breakage.**
Every reader below was opened.

| the claim | what is actually there |
|---|---|
| ~~"`fort_level` is a bare scalar with no construction, cost or decay — cut it"~~ | ⛔ **WITHDRAWN.** It is declared on the **live** `Territory` at `engine/autoload/game_state.py:241`; **derived** from garrison at `:324` under a comment that is the single-owner rule stated in place — *"fort_level stays DERIVED from garrison rather than authored: it is a rule, not data, and authoring it would give one number two owners"* (`:322-323`); round-tripped through the snapshot at `:381` and rebuilt at `:452`; and the rule is repeated at the export leaf, `engine/substrate/world_initial_state.py:17-18`. Further: `terr.fort_level` is an authored descriptor key at `references/descriptor_registry.yaml:94`, cooked into `engine/engine_params/descriptors.json:143` behind `tools/export_descriptors.py --check`, which is **BLOCKING** in CI (`.github/workflows/valoria-ci.yml:137`) |
| ~~"`facility_tier` is never set anywhere including the loader"~~ | ⛔ **WITHDRAWN.** It is read live at `systems/settlements/sim/registry.py:97` (`return 2 + self.facility_tier + bonus`, the AP property) and **set by its own loader** at `:146` (`facility_tier=d.get('facility_tier', 0)`), serialised at `:119`, and registered as `set.facility_tier` at `descriptor_registry.yaml:173` → `descriptors.json:123`, behind the same blocking export |

> ### RULED: **NEITHER IS CUT BY THIS DOCUMENT, AND THE ENGINE'S `fort_level` ALREADY *IS* THE SHAPE THIS SECTION ARGUES FOR.**
>
> A derived quantity with one owner and a comment saying why it is derived is not the defect
> `fort_level` was cited as; it is the defect's repair, made in 2026 in the live engine. What this
> section proposes is the **head's** representation of a fortification, in `engine/season/`, where
> there is none. It does not reach into `engine/autoload/` or the ED-IN-0204-superseded
> `systems/settlements/` tree, and **a session that deletes either field on this document's authority
> has misread it.**
>
> ⚠ The deletion may still be defensible on *other* grounds — both sit in trees ED-IN-0204 Decision 1
> superseded. **The stated grounds were false**, and this row records that rather than the verdict.
>
> ⚠ **SINGLE OWNER (2026-09-17): this subsection owns the `fort_level` / `facility_tier` withdrawal.**
> `04` §B.3 restated it; it is now a pointer here.

**Why this row is in PART A rather than an appendix:** `CLAUDE.md` §0.1 pt 3's first shape is *"X is
absent / dead / never fires → RUN the thing that would show presence."* Two absence claims were made
about live readers sitting behind a blocking gate. **An absence is the cheapest claim to make and the
hardest to see wrong.**

---

## A.4 · The lifecycle — `found`, a `works` `Record`, MATTER, and `restore` against a ceiling

Four moments, and **exactly one new verb.**

| # | moment | act | eligibility | writes | emits / on refusal |
|---|---|---|---|---|---|
| 1 | **FOUND the plot** | **`found`** *(NEW)* | `own`, presence entering through `requires` | `(Rung, exists)` — a `hearth`; its `contain` edge to the quarter; the founder's own `contain` moves | `rung.founded` / `found.refused` |
| 2 | **OPEN the `works`** | **`create_record`** *(exists, RUNS)* | `own`, `requires: —` | `(Record, exists)`, `(Record, stages)` — **act-declared** — and the maker's `hold` on it | `record.created` |
| 3 | **RIPEN a stage** | *nobody; the clock act 2 wound* | — | `(Record, matured)` at MATTER | `term.matured` |
| 4 | **RAISE the fabric** | **`restore`** *(row exists, NO effect)* | `own`, `presence:<site>` | `(Site, condition)`, through the summing clamp | `site.restored` / `restore.refused` |
| — | **WEAR** | *nobody* | — | `(Site, condition)` down at MATTER | `condition.worn` · `condition.band_crossed` |

> ### RULED: **THERE IS NO `undertake` VERB, NO `build`, NO `repair`, NO `raze`, NO `garrison` AND NO `convert`. A `works` IS A `Record` KIND WITH ACT-DECLARED STAGES, OPENED BY THE `create_record` THAT ALREADY RUNS; AND BUILDING AND REPAIRING ARE ONE ACT AT DIFFERENT BANDS.**
>
> Cited to `ARCH §A.3` row 11 (*"`Petition`, `Dispensation` … **kinds of `Record`**"*) and `ARCH §B.4/B.5`
> (`:255-261`, the synthesis call that folded them, *"with no new rows"*), extended to `works` on the
> same grounds. `01_AXIOMS.md` **ID-12** (`:454`) makes the kind a data row.

**AND THE SPINE OF STEP 2 IS ALREADY EXECUTING, WHICH IS THE CHEAPEST THING IN THIS DOCUMENT.**
Opened: `create_record` is `eligibility: ["own"]`, `requires: "—"`,
`writes: ["Record.exists", "Record.stages"]`, `grade: "ruled"` (`verb_table.yaml`, `create_record`
row). Its effect body at `engine/season/loop/effects.py:262-290` takes the stages **from the act**
(*"THE STAGES COME FROM THE ACT, NOT FROM A DEFAULT"*, `:267-271`) and — the part that makes the
lifecycle close — **mints the maker's `hold` in the same act**: `:286-289`, *"S13: possession is a
`hold` Tenure owned by the holder, never a field on the Record. The maker holds what they made until
they part with it."* MEASURED: `record.created` fired **69 times** in one season. `Record` carries
`ttl`, `stages`, `subject_matter` and `rung` (`carriers.py:426-431`), and `Record.matured` is
**Jordan-ruled, 2026-09-10, written at MATTER** (`carriers.py:432-437`).

**MATTER matures stages, and it already stops if the maker is gone.** `matter.py:65-78`: the stage's
holder is looked up as a live `hold` whose object is the Record (`:73-74`), and where there is none the
maturation is refused with the reason TRACEd verbatim — *"a half-made copy STOPS rather than finishing
itself"* (`:76-77`). **A `works` with no master does not advance. Zero new code**, and it is the best
drama generator in the design.

### A.4.1 · The ceiling, and why building and repairing are one act

`restore`'s effect is already specified on its row:
`effect: "Δ = +(1 − condition) × f(degree) × share"` (`verb_table.yaml:465`, from `§54` item 7). Bound
it:

```
ceiling(w, site) -> int          # resolver-side, World FIRST, owned by Nobody
  = condition_scale × (matured stages / declared stages) of the live works Record naming this site
  = condition_scale                                       if no live works Record names it
```

The clamp is already there and already order-independent (`resolve.py:538-553`); **the ceiling is one
more term in the same `min`.** One Query, owned by Nobody, storing nothing — `01_AXIOMS.md` **T-a**
(`:255`, *"An aggregate cannot be stored"*).

| the same act | reads as | because |
|---|---|---|
| `restore` at condition 0, 1 of 5 stages matured | **raising the first courses** | the ceiling is a fifth of the scale, and the fabric climbs toward it |
| `restore` at near-scale, 5 of 5 matured | **repairing wear** | the ceiling is full |
| `restore` on a slighted fabric, 5 of 5 matured | **rebuilding** | a finished work can always be repaired to full |

### A.4.2 · The stall, designed honestly in both directions

- **MATTER-STALL.** Stages have matured and the containing rung's store cannot meet the cost. The
  `scalar_threshold` conjunct fails, the act is **refused, and the refusal emits** —
  `emits_on_refusal: ["restore.refused"]` is already on the row (`verb_table.yaml:463`). **A fabric
  sitting visibly below a ceiling it is entitled to reach is a scaffolding standing empty**, and it
  says so every season somebody tries.
- **TERM-STALL.** Matter and hands are there and no stage has matured. The ceiling is where it was, so
  the delta clamps to zero — and **the fold refuses an act whose effect touched nothing.** That is not
  a hope: `ARCH` PART D row 5 (`:934`) records it as strengthened, with `work` emitting `site.worked`
  with no delta as `ID-9`'s own worked instance, and *"the gate now refuses `before == after` at the
  write, so the receipt is never minted."* **You cannot hurry mortar**, and it is arithmetic, not a
  cooldown.

### A.4.3 · The unfinished `works` is a designed state with five legible causes, none of them an error

Nobody has the matter · nobody has the hands · the terms have not ripened · the master is dead · the
master was replaced by somebody who does not care. **Each emits something different, and the emissions
are the only way anybody learns which.** The machinery is all present:

- **the master dies** → his Tenures take `until`, the `works` becomes unheld, and `matter.py:73-78`
  refuses to mature it.
- **a successor who does not want it** → he simply never takes the `hold`. The `works` stands; the fabric
  stands at whatever condition it reached. **A half-built `works` is an indictment of whoever should have
  finished it, and it is visible.**
- **a rival raises what somebody else began** → `restore` asks for `own` and presence and **no office
  at all** (`verb_table.yaml:450`). A cathedral begun by one faction and brought to full condition by
  another's mason is a whole political event with **no special case anywhere**: the first holds the
  works Record, the second holds nothing and stands there with the matter.
- **abandonment must be endable** or `AX-6` breaks. `Record.ttl` already exists (`carriers.py:430`);
  the opening act declares one; the lapse emits. That is `01_AXIOMS.md` **T-n** (`:1165`) exactly — *an
  end that is not the owner's discretion is declared by the act that opened it.* And `destroy_record`
  (`eligibility: ["hold:<record>", "presence"]`) ends every `hold` on it (`effects.py:293-296`), so
  abandoning by choice is also already spelled.
- **one work per plot** is a `cardinality` conjunct — one of the closed seven (`rosters.yaml:1114`) —
  and the refusal emits. `T-g`'s obstruction, free, with **no build queue and no scheduler.**

⚠ **What `found` costs, stated rather than hidden.** It is the one new verb, and it must avoid the
three load failures a predecessor proposal hit (`proposals/2026-09-10-settlements-factions-populations/`
P4): a form outside the closed seven; a disjunctive `kind:` cell the roster deliberately omits; and
`eligibility: [presence:<rung>]` **alone**, which is declined person-side at
`engine/season/decision/options.py:167`. **So `found`'s eligibility leads with `own` and presence
enters through `requires`** — the shape `restore` already has, and whose own note says why:
*"eligibility is a DISJUNCTION (`own | presence:<site>`) so `own` alone admits, and the precondition is
where presence actually binds"* (`verb_table.yaml:460`).

⚠ **And `found` is the one item here that needs an `@effect_for` body writing a row whose subject is
not the actor**, so it is downstream of the Arc-2 gate. There are **eleven** effect bodies today —
`confer release revoke convene move work create_record destroy_record "kill / wound" utter transfer`
(`effects.py:92-437`) — and neither `restore` nor `found` is among them. `resolvable_verbs()` returns
**18 of 38**; `restore` is excluded and `work` is not.

---

## A.5 · Holdings — what is held, and what may never be

| link | the edge | the Query | what it gets you |
|---|---|---|---|
| **membership** | `commit : Person → Proposition`, many — *"this is faction membership"* (`holonic_ARCHITECTURE.md:540`) | `members` (`world_q.py:200`) | you are of this faction |
| **title** | `hold : Person → Rung`, **1 per object** (`:538`) | `in_holdings` (`engine/season/loop/predicates.py:60`) | **the plot is yours** |
| **governing** | `hold : Person → Office` | `under_purview` (`predicates.py:105`) | you govern a rung kind whether or not you hold anything in it |
| **custody** | `hold : Person → Record` | `hold_force` (`world_q.py:138-145`, which **raises** on a second live hold) | the keys, the ledger, the `works` — master of it without owning the ground |
| **presence** | `contain : Rung → Rung`, 1 parent | `presence`, `density` (`world_q.py:172`, `:276`) | you are here, and how many of yours are |
| **the fabric** | **none** | `verbs(w, site, floors)` (`world_q.py:133`) | **nobody holds a fabric** |

> ### RULED: **`hold` MUST NOT REACH A `Site`. CONFIRMED — AND NOT FOR THE REASON THE DESIGN PASS OFFERED.**
>
> `hold`'s object domain is `Office | Rung | Record | Proposition`
> (`holonic_ARCHITECTURE.md:538`); `ARCH §A.3` row 12 fixes its **subject** as a Person only; `ARCH` PART D
> row 14 grades *"a banner holding territory"* **STRUCTURAL (typed)**. What is held is the **RUNG** the
> site keys to, or the **works Record** on it. Never the fabric.

### A.5.1 · ⚠ THE ARGUMENT FOR WIDENING IT IS FALSE, AND IS STRUCK IN PLACE

The design pass's strongest case for adding `Site` was this, and it is the one claim in the whole
subject that a single `sed -n` refutes:

> ~~"`restore`'s formula's third term has no source in the model. `share` is the actor's draw-share of
> the site — and the only field that could carry who draws is `Site.drawers`, which is on the write
> matrix's `retired:` list. **Widening `hold` to `Site` is what makes the restoration formula
> computable** — with a single holder per Site, `share` is 1 and the term vanishes. That is the
> strongest single argument for the amendment and no document in the corpus makes it."~~

⛔ **FALSE ON BOTH HALVES.** Opened: `share(w, ...)` and `draw_share(w, ...)` are declared
**RESOLVER-SIDE QUERIES** in `holonic_ARCHITECTURE.md`'s §17 roster (`:599-600`, under the header
*"`Query` — never stored, always recomputed"* at `:591`). **`share` was never a field**, so no field
being retired can have deprived it of a source, and widening `hold` cannot "make it computable" — a
Query is computed from the world, not from a holder count. And `Site.drawers` **still exists and is
readable**: it is declared at `carriers.py:418`. What `write_matrix.yaml:368-372` retires is the
**ability to write it through the gate**, which is a different fact and the reason a repair cannot
change who draws on a commons.

**THE ACTUAL `restore` BLOCKER IS THAT `share` AND `draw_share` ARE DECLARED AND UNIMPLEMENTED.**
That is the whole of it, and it is `01_AXIOMS.md` **ID-13** (`:489`, *"A DECLARED FIELD MUST REACH A
READER, OR IT IS NOT DECLARED"*) read at a Query instead of a field. The second half is units: the
formula's `(1 − condition)` is normalised while `Site.condition` is a fixed-point int on
`condition_scale = 1000` (`fixtures.py:160`), so registering the effect requires deciding the units.
**Two problems, neither of them `hold`'s domain.**

### A.5.2 · The ground the refusal actually stands on: **widening it deletes the commons**

Mandatory single-holdership is not a neutral simplification. `hold` is **1 per object**
(`holonic_ARCHITECTURE.md:538`) and `hold_force` **raises** on a second live hold
(`world_q.py:138-145`). So a held fabric has exactly one holder, `share = 1`, and — opened at
`proposals/2026-08-31-ideal/10_SUPERSEDING.md:1275-1279` — the shape that dies is named there:

> *"**At a commons with many drawers, single-act closure is impossible.** One boat among a harbour's
> forty moves at most a fortieth of a quarter of the harbour's condition in a maximum-degree season.
> **Closure is a collective outcome** — many actors, many seasons, crossing a band edge — which is the
> tragedy-of-the-commons shape the mechanism exists to produce: many rational private acts making
> everyone's practice worse, including the actor's."*

And the same passage records the other arm, withdrawn in place by its own author: at a single-drawer
site *"`share = 1`, and one Overwhelming season moves a quarter of the condition"* (`:1280-1282`).
**Make every fabric single-held and every site becomes the second case.** The commons — a harbour, a
seam, a road, a wall — stops existing as a category, and with it the only mechanism in the design that
produces collective ruin from rational private acts.

⚠ **SINGLE OWNER (2026-09-17): this subsection owns the commons `share` reading.** `04` §A.5 item 15
and §B.3 restated it; both are now pointers here. `share = 1` at a single-drawer site is the
*special* case, not the general one, and a `restore` body written against the special case deletes the
commons — which is why the two halves at `10_SUPERSEDING.md:1275-1279` and `:1280-1282` must be read
together and never one at a time.

**Three things the refusal keeps, and they cost nothing.** (1) **The fabric outlives its holder's
claim** — a cathedral stands on a plot somebody holds; take the plot and the cathedral does not move,
so **you have taken it by taking the ground under it**, one edge changing hands rather than two.
(2) **A work can be held by somebody who does not hold the ground** — `hold : Person → Record` already
exists, so the mason holds the `works` and the lord holds the plot and **neither can finish without the
other**: the mason's `hold` is what makes MATTER advance the stages (`matter.py:73-74`), the lord's is
what admits the `restore`. (3) **Nobody holds a wall, and nobody should** — a rampart's rung is the
quarter, and a wall is a common thing.

**The cost, stated plainly:** you cannot confiscate a single building. You confiscate its plot, which
takes everything on that plot. **That is correct** — a plot is a building's footprint, and a granary
and its store move together because the store is the plot's (`stores` is a `Rung` field).

### A.5.3 · ⚠ THE REFUSAL IS CURRENTLY UNENFORCEABLE, SO THE GUARD IS **REPORTED AS SHIPPING**, NOT ASKED FOR

Opened: `World.add_tenure` is *"The ONE writer"* (`state/world.py:223`). It validates **two** things —
that `t.kind` is on `TENURE_KINDS`, raising `Unowned` with code `S15` (`:242-247`), and that a
`contain` edge ascends the ladder, raising `Forbidden` with code `S10` (`:248-256`) — and then appends
(`:257`). **It checks nothing whatever about the object class of a `hold`.** So
`Tenure(p, <a site id>, "hold")` is accepted today, and Layer 1's `ARCH` PART D row 14 grade of
**STRUCTURAL (typed)** describes a typed language this one is not.

> ### RULED: **the object-domain conjunct lands in `add_tenure` alongside the two checks already there — `hold`'s object in `{Office, Rung, Record, Proposition}` or `Forbidden`, `S15`.**
>
> ⚠ **SINGLE OWNER (2026-09-17): this subsection owns the earns-its-existence argument for that guard.**
> `04` §A.3 item 4 made the same argument at the same length; it is now a pointer here, plus the build
> step. Two homes for one argument is `CLAUDE.md` §8's defect read at prose.
>
> This guard **earns its existence** under `CLAUDE.md` §0.1 pt 5's predicate, and the predicate is the
> reason it is not apparatus: a `Tenure` the engine reads at RESOLVE, at MATTER and in six Queries is
> **load-bearing on the game**, not on this repository's process. It is one owner for the operation
> (`add_tenure` is already the single writer), every site routed through it (there is no other), and
> it fails on recurrence. **Reported to Jordan as shipping, not queued as a question** — `CLAUDE.md`
> §0's step 3: a design document answers it, and two of them do.

### A.5.4 · The ghost polity is **live**, not hypothetical — a Layer 1 / Layer 2 contradiction

**MEASURED, `build_realm(0)`, this session:** 35 live `hold` Tenures. **19 have a person as subject;
16 have a faction Proposition.** Objects: 19 offices, 16 rungs, **0 sites.**

The 16 are written knowingly at `engine/season/harness/populated.py:613-618`, and the comment above
them is both the licence and the warning (`:602-607`): *"`geography_v30.md`'s starting-control table
names an owner per PROVINCE and never a person, so the holder has to be the faction, and a faction IS
a Proposition. The declared defect is §54's, not repaired here."* `footprint` reads them knowingly too
(`world_q.py:263-266`): *"⚠ A FACTION HOLDS A RUNG AS THE `hold` SUBJECT, WHICH §15's TABLE TYPES AS
`Person -> …`… That defect is declared there and is not repaired here."*

**And ratified Layer 1 forbids it in two places by name.** `01_AXIOMS.md:1078` — a Faction's
**`NEVER.`** list includes *"a `hold` subject"*, with the reason at `:1086-1089`: it is *"what prevents
**territory held by a banner nobody carries**, uncontestable because the holder can never appear at a
venue."* `ARCH` PART D row 14 (`:944`) grades the shape **STRUCTURAL (typed)**.

> ### RULED: **KEEP THE SUBJECT A `Person` AND MINT THE HOLDERS. THE FIX IS CONTENT, NOT SCHEMA.**
>
> A province "held by the Crown" is held by a **named person** with a live `commit` to the Crown's
> Proposition. Then `footprint(w, faction)` — already *"the rungs it holds, plus the rungs its members
> sit in"* (`world_q.py:254-255`) — returns the same answer, and **the ghost polity cannot arise**,
> because the last member leaving orphans no Tenure: the person still holds it, and a person can be
> killed, revoked from, or released. The ratified `confer`-eligibility patch for a memberless
> holder-Proposition becomes **unnecessary rather than unbuilt** — it repaired a condition this removes.
>
> **The cost:** a faction cannot hold ground *as* a faction. A named person does, and **his death is a
> political event somebody has to win.** That is strictly more game than a banner, and it is what
> `AX-1` has been saying all along.

⚠ **Two honest notes.** (1) This document does **not** adopt the ratified fold-in, and a proposal that
contradicts a fold-in must say so; this is that sentence. (2) The alternative route — `confer` made
eligible at the Rung's venue when the holder-Proposition has zero live `commit` edges — is **blocked**
independently: `judging_set` raises `Unspecified` today (`world_q.py:146-148`, *"S61 — NOTHING IS
DECIDED AT A SITTING"*), so it needs a venue that cannot yet decide anything.

### A.5.5 · `serves:` — world-generation content, plus a runtime Query. **Never a stored fact.**

What it is today: a per-building list of institution tags in `venues.yaml`, read once by
`populated.py` to decide **where to seat a person**, matched against an ordered `seat_precedence`
whose order *"MOVES PEOPLE, which is a game change"* (`venues.yaml:128-140`). It is a **seating
hint**, and nothing reads it after world-build.

> ### RULED: **`serves:` survives as WORLD-GENERATION CONTENT and is derived at runtime. It never becomes a fact about a building.**
>
> ```
> serves(w, site) = { prop : ∃ p . (p holds site.rung ∨ p ∈ presence(w, site.rung))
>                              ∧ p has a live commit to prop }
> ```
>
> A cathedral serves a creed **because the canons in it are committed to that creed's Proposition** —
> and when the last one repudiates it stops serving, **with no write anywhere.** Cited to
> `01_AXIOMS.md:1086-1088`, the same argument one level down: *"THE RESOLVED FORM BEATS A STORED ONE ON
> ITS OWN TERMS: IT CANNOT GO STALE."* The world-gen half is lawful by `:178-179`.
>
> **What dies is the affiliation being UNCONTESTABLE.** Today it is authored, so nothing can change
> it. Under the derivation a rival changes the answer by taking the plot or moving the people — which
> is the whole subject of this document. **That is the gain, and it is the only thing the cut buys.**

⚠ **And the validator the file claims for itself does not exist — stated exactly, because the loose
version of this claim is wrong.** `venues.yaml:15` declares itself *"A MECHANISM, NOT REFERENCE
(`CLAUDE.md` §0.05)"* and `:37-38` claims *"The validator that caught it is `tests/valoria`-side: every
id below must resolve in the geography file and its description must match the institution it is
claimed for."* **No such `tests/valoria` validator exists.** What DOES gate part of this surface, and
is why the sweeping version of the claim would be false: (a) `populated.py` *"reads this list and
REFUSES if it and `seats:` disagree in either direction"* (`venues.yaml:136-138`), so the ordering
cannot silently never-match; and (b) `tools/export_npc_roster.py --check`, whose registry `role:` line
is explicit that it *"REPORTS every row that differs WITHOUT failing… It FAILS only on a row naming a
case, a place or a person that does not exist"* (`references/ci_checks_registry.yaml:380`), wired into
CI only in 2026-09. **So the building rows' geography resolution is ungated, and the seat ordering and
the NPC homes are not.** Stated, not proposed: a guard over the first would be load-bearing on the
game and would earn its existence under §0.1 pt 5 — but it is not this document's deliverable, and
minting it in prose is what §0's adversarial-pass bound forbids.

### A.5.6 · Holding and governing come apart, and the built world is where it is felt

Jordan ruled them disjoint and `in_holdings` implements it verbatim (`predicates.py:63-68`):
*"King/Queen cannot revoke title of Duke/Duchess if they do not have duchy is in their holdings."*
Three worked seats, no new mechanism in any of them. **A mayor who holds no plot in his own town**
governs it and **cannot build in it** — every improvement needs somebody else's leave, and getting it
is the game. **A duke who holds three plots in a town he does not govern** may build on all three and
cannot levy a grain of it: his chapel, his granary and his townhouse are three unremovable facts in
somebody else's jurisdiction. **A landless mason** holds nothing and is the most useful person at a
cathedral site, because `restore` asks for `own` and presence and **no office at all.**

---

## A.6 · THE CASCADE'S BOTTOM HALF — measured, and it reorders the work

Jordan: *"a provincial policy on farming taxation may end up impacting a hearth."* Document 01 owns
the policy instrument. **This document owns the bottom of that sentence, and the bottom is not
connected.**

> ### MEASURED THIS SESSION, one season of `build_realm(0)`:
>
> ```
> rungs by kind      {realm 1, duchy 3, territory 17, settlement 37, community 60, hearth 211, person 46}
> sites by kind      {harbour 37, seam 37}    — all 74 keyed to a `settlement` rung
> after 1 season, rungs holding any matter:   {settlement: 37}
>   settlement total 4,810 units              {grain 1480, ore 1850, salt 1110, timber 370}
>   HEARTHS HOLDING ANY MATTER:               0  of 211
> sites with any person present at their rung: 0  of 74
> log                yield.taken 37 · stores.changed 37 · condition.worn 74 · work.unavailable 38
>                    travel.blocked 23 · record.created 69 · claim.deposited 2175
>                    site.built 0 · rung.founded 0 · site.restored 0 · site.worked 0
> ```

**The diagnosis is the type split, observed — not a placement bug.** Yield credits **the Site's own
rung** (`matter.py:204-224`: `if site.rung != rid: continue` at `:205-206`, then a MATTER write to that rung's
`stores`), and all 74 Sites name a settlement. Subsistence draws from **the rung the eaters are
contained in** (`matter.py:169-176`: `eaters = world_q.presence(w, rid)`, then
`draw = {k: wt * len(eaters) …}`), and all 46 persons are contained in hearths. So **37 settlements
accumulate 4,810 units a season that nobody is addressed to eat, and 46 people are short every season
in rungs that hold nothing.**

**And the shortfall is clamped away, deliberately and in writing.** `matter.py:179-185`: *"⚠ A
SHORTFALL EMITS NOTHING AND DECIDES NOTHING, on L5's rule… It is recorded so a run can be read"*,
closing *"recorded, not acted on (L5: a crossing produces no outcome)"* at **`:185`**.

> ### RULED: **MATTER MUST NOT MOVE MATTER ACROSS A `contain` EDGE. A PERSON MUST — AND THAT IS WHY THE CASCADE WORKS RATHER THAN WHY IT FAILS.**
>
> A tax that collects itself is a fourth clock, which `01_AXIOMS.md` **T-c** (`:304`) forbids and
> **AX-5** (`:151`) closes the list against: *"THE WORLD MOVES BY ITSELF IN EXACTLY THREE WAYS…
> Nobody wound any of the three, and you cannot bribe silt"*, with the axiom stated **as the list** and
> the prohibition as `T-c` (`:162-163`). An automatic cascade would be deterministic, unbribable, and
> authored by nobody.
>
> **The pipe already exists and is act-driven.** `transfer` is built, conserves, and writes
> `(Rung, stores)` on both sides (`effects.py:437`). **What is missing is the crossing at the bottom**,
> and it is two content moves plus a predicate, in this order:
>
> 1. **Eaters at a COMMONS site are the persons under its rung by `contain` closure.** A commons feeds
>    the settlement — that is what it is. `World.contain_ascends` (`state/world.py:197`) already walks
>    the edge; `matter.py:169`'s `presence(w, rid)` is the one read that changes.
> 2. **DWELLING and PRODUCER fabrics key to the hearth or community they ARE**, which is
>    `populated.py:357` (community), `:361` (hearth) and `:373` (the Site mint) — **content, not code.**
>    Then `matter.py:205`'s `site.rung != rid: continue` loop is correct as written and yields to the
>    right place for the first time, and `presence:<site>` acquires a referent.

**The tempo then falls out of an ordering that already shipped, and it is exactly right.** MATTER
precedes RESOLVE, and larder precedes yield so *"a rung cannot eat what it has not yet produced"*
(`matter.py:155`, the `LARDERS, THEN YIELD` step). **So matter taken in one season is felt as hunger in
the next, and the collector is not present at the barrier where the shortfall fires.** Nobody authors
the family's crisis; somebody is nevertheless to blame; whether anybody can prove it is an epistemic
problem.

**And the noise Jordan asked for is already in the engine, none of it decoration.** `season_factor`
scales every yield (`matter.py:208`); `Site.condition` scales it **multiplicatively** —
`int(base × (condition/scale) × factor)` at `:207-209`, so ⭐ **a worn mill is a tax nobody voted
for**, and two settlements under one policy deliver different amounts because their fabrics are in
different repair; and the collector is a person who may be ill, absent, bribed, dead, or simply have a
better use for one of about five acts.

### A.6.1 · Two corrections to what is and is not built at MATTER

| claim | status |
|---|---|
| larder draw and yield are **NOT IMPLEMENTED** | ⛔ **FALSE, and the tree says so about itself.** `matter.py`'s own `TRACE.decision` row lists `not_implemented=["the death cascade", "bodies, larders, yield, travel"]` at **`:50-51`** — and the larder step runs at `:164-195`, the yield step at `:196-224`. **The decision row is STALE about larders and yield.** MEASURED: `yield.taken 37`, `stores.changed 37` in one season |
| **bodies and travel** are not built | **TRUE as stated in that row.** No verb writes any `Person` interior field (`ARCH §F.20a`, `:1083`), so a shortfall has no body to reach |
| band crossings run | **TRUE, and DOWNWARD ONLY.** The predicate is `before >= floor > s.condition` at **`matter.py:262`**, the Event is built at `:267-270`, and `w.crossings.append((s.id, verb, before, s.condition, ev.id))` at `:272`. **A building becoming usable emits nothing**, so the whole positive half would be silent. The repair is the same predicate in the other direction — `before < floor <= s.condition` — and it is one line in one file |

### A.6.2 · ⚠ THE BUILT WORLD IS UNASKABLE-ABOUT TODAY, AND IT IS ONE OPERAND

`questions_for` has four sources, read in a semantic order (`rosters.yaml:250-261`, `open: true`,
`ordered: true`). **Q3 `band_crossed` is already exactly the right source for the built world, and its
presence gate is already correct** — `world_q.py:508-517`, verbatim: *"a crossing is a fact about a
PLACE, and it becomes a person's question when that person is THERE to notice it… A person elsewhere
gets no question, which is L2 working."* The code even looks the site up: `site = w.sites.get(who)`,
`at = getattr(site, "rung", None)` at `:515-516`.

And then it throws the site away:

```python
# world_q.py:518, as it stands
out.append(Question(f"q:band:{what}", "band_crossed", (what,), what))
```

`what` is the band's key, and `band_floors`' inner keys are **site-use verbs** — `bulk_shipping`,
`fishing`, `deep_mining`, `surface_gleaning` (`rosters.yaml:1191-1195`, whose own note says they are
*"SITE-USE verbs … NOT verb-table rows"* at `:1182-1185`). And `_derive_operand` binds `site`,
`subject` and `to` **from the question's referent** — one rule, stated once at
`options.py:269-273`: *"AN OPERAND NAMING WHAT THE ACT IS ABOUT BINDS THE QUESTION'S REFERENT… that is
why `subject`, `to` and `site` all bind the referent."*

> **SO A PERSON PRESENT AT A SILTING HARBOUR FORMS A `work` CANDIDATE WITH `site = "bulk_shipping"` —
> A STRING THAT IS NO SITE — AND THE `existence` CLAUSE READS UNKNOWN.**

That is `H-110`, tier 1, grade `absent` (`hole_register.yaml:1533-1544`), whose own `cite` says the fix
is one line and *"is NOT taken here on purpose… a design edit, not a repair"* (`:1543`). And it is what
two verb-table cells report as something else. `work`'s note (`verb_table.yaml:765`) closes: *"the
corpus refuses all 723 because no referent it produces is a Site, **which is a fact about these worlds
and not about the threshold**."* `restore`'s note (`:460`) closes the same way: *"no referent this
corpus produces is a Site."*

> ### RULED: **IT IS NEITHER A FACT ABOUT THE WORLDS NOR ABOUT THE THRESHOLD. IT IS ONE OPERAND BOUND TO THE WRONG HALF OF A TUPLE, PLUS A RUNG — AND THE TWO ARE ONE DELIVERABLE.**
>
> The site id is already in the tuple, read and discarded (`matter.py:272` appends it;
> `world_q.py:515` reads it). Binding the referent to the site is one line. **But it changes nothing
> alone** — and ⚠ **the REASON was corrected 2026-09-17 by re-measuring, because this file and `04`
> named two different blockers and only one of them binds everywhere.**
>
> ~~"because **0 of 74 fabrics have anybody present at their rung** — so Q3's presence gate can never
> fire… A.6's rung moves are the deeper of the two blockers."~~ **That is true of the POPULATED world
> and false of the CORPUS worlds**, which co-locate persons and sites by construction —
> `corpus_run.py:216` mints every Site at `ids[chain[0]]` and `:231` seats every person at the same
> rung, and `venues.yaml:24-25` says so in its own words: *"`corpus_run.build_at` seats every person
> directly in the settlement… every person in every world is therefore in the same room as every
> other."*
>
> **The blocker that binds in BOTH families is the one `04` §A.3 item 1 measured: Q3 FIRES ON NOTHING.**
> Re-measured here 2026-09-17, driving MATTER on `build_realm(0)`: every site starts at
> `condition_scale = 1000` (`fixtures.py:160`), `wear_per_season` is 10 for every kind
> (`rosters.yaml:841-844`), the highest floor is `bulk_shipping: 800` (`rosters.yaml:1191`), and **the
> first crossing fires at MATTER pass 21** — 37 of them, `s_s_001_harbour` `bulk_shipping` 800 → 790.
> CI runs the populated world for one season and the corpus for at most six. `w.crossings` is empty in
> every world any gate executes.
>
> **So the referent fix (`04` item 1a) needs a world in which a floor is crossed (`04` item 1b), and
> A.6's rung moves are a SECOND, populated-world-only blocker rather than "the deeper of two."**
>
> ⚠ Fixing Q3 **re-records goldens**, and that is said here rather than discovered: the seeded goldens
> under `engine/tests/` observe any output-moving change to campaign-reachable code, and `CLAUDE.md` §7
> requires a re-pin to be declared. This one is intended.

---

## A.7 · `ED-SE-0051` — the recommendation, with the argument that decides it

`ED-SE-0051` is open, `needs_jordan: true`, at `registers/editorial_ledger_se.jsonl:51` — *"THE BOUND
ON THE DEMOGRAPHIC LOOP: matter only, or matter plus hearth capacity?"*, recorded there as *"the one
question in [that proposal set] that survived all five of `CLAUDE.md` §0's tests"*, with **LAYER 1 IS
SILENT** stated in the row itself. It gates position 24 of the ratified order.

> ### RECOMMENDED (not ruled): **THE CAPACITY ARM — and capacity is a `capacity(w, rung)` Query over DWELLING sites with a FLOOR, never a fixture.**
>
> ```
> capacity(w, rung) -> int          # resolver-side, World FIRST, Nobody's
>   = floor_fixture                                  # what a household keeps in a corner
>   + Σ over DWELLING Sites in this rung's containment subtree
>       whose condition ≥ band_floors[kind]["shelters"]
>     of that kind's declared `houses` count
> ```

**Three grounds, and the first is decisive.**

1. ⭐ **MATTER-ONLY IS NOT CURRENTLY A BOUND AT ALL.** `matter.py:185` records a shortfall and states
   in its own comment *"recorded, not acted on (L5: a crossing produces no outcome)"*, and **MEASURED:
   0 of 211 hearths hold any matter after a season**, so nothing is even being compared. The choice is
   not between two bounds; **it is between a bound and a TRACE note.**
2. **Capacity-as-a-fixture is the spreadsheet failure mode** — a number per facility kind, authored,
   never measured, and unburnable, unholdable, untaxable. Capacity-as-a-Query-over-live-fabric costs
   zero new tables beyond one `houses` column on a kind roster that must be authored anyway, and it
   makes the player's building the lever Jordan asked for. `design_rulings_2026-09-06.md:169` is the
   governing line: *"Every aggregate is DERIVED, none is PUSHED."*
3. ⭐ **It makes decay and growth the same arithmetic.** A village whose crofts have worn below
   `shelters` **cannot hold the people in it**: capacity falls, and the excess must leave. So the
   damping term of the growth loop and the meaning of the decay loop are **one number.** Under an
   authored fixture they are two.

**`T-b` compliance** (`01_AXIOMS.md:284`): capacity bounds CENSUS's *individuation*, which is
demand-driven only — **AX-5**'s own resolution licenses exactly this (`:172-175`, *"So individuation is
authored: the demand is its author"*). It **changes what may be admitted** and produces no outcome.

**THE FLOOR IS NOT DECORATION, AND AN ATTACK PUT IT THERE.** Attack: *a rung with `capacity == 0` and
`stores > 0`.* A newly founded hearth has no fabric, so capacity is zero, so founding is
self-defeating and the design fails at its own extreme — R's completeness clause
(`CLAUDE.md` §0.06, *"a mechanism breaking at its extremes fails"*). **The attack succeeded and changed
the design**: the floor is what a household keeps and can be, and the fabrics raise it above that.
Recorded as the licence for the clause rather than patched silently.

**The counter-argument, not hidden:** capacity lets a player opt out of the demographic game by simply
not building, where matter-only does not. The answer is that opting out is itself priced — a small
place is a weak place — whereas matter-only makes growth something that happens *to* the player. **The
objection is real and is the best case for the other arm.**

**Cost of being wrong:** one Query swapped for a fixture. **It gates one build item and nothing else.**

---

## A.8 · PLAYER AGENCY — building is a `works` you START and ADVANCE, never a tag a system deposits

> ### RULED: **NO SYSTEM EVER DEPOSITS A BUILT THING. EVERY FABRIC IN THE GAME WAS RAISED BY A NAMED PERSON'S ACT, AND FOR EVERY ACT THIS DOCUMENT NAMES, THE QUESTION THAT PUTS IT IN FRONT OF A PERSON IS NAMED WITH IT.**
>
> *"A verb nothing raises a question about is unreachable by anyone."* Candidate acts derive from
> `Question`s, and there are exactly four sources (`world_q.py:439-550`; `rosters.yaml:250`).

| act | what raises the question | source | present? |
|---|---|---|---|
| **`restore`** (build / repair) | **the fabric crossed a band and I am here** — a wall past `mans`, a granary past `keeps`, a half-built work crossing *up* as it rises | **Q3** + A.6.2's referent + A.6.1's upward predicate | ✓ exists |
| **`work`** (use) | the same crossing | **Q3**, same two | ✓ exists |
| **`create_record`** (open the `works`) | a claim landing about the place, or a docket matter about it | **Q2** / **Q1** | ✓ exists, and it RUNS |
| **`transfer`** (feed a `works`, ship relief) | the crossing at the store I am at; or the claim that a place is short | **Q3** / **Q2** | ✓ exists |
| **contest a fabric** (slight, sabotage) | ⚠ **a crossing tells me the wall is SOUND, not that I want it broken. The want is mine** | **Q4** — a live `commit` to an OUGHT whose subject is that place. *This wall should not stand* is an uttered belief somebody committed to | ✓ exists, and it is the right home: **sabotage is an ambition, not a stimulus** |
| **`found`** (stake a plot) | ⚠ **nothing. A plot that does not exist cannot raise a question about itself** | — | ⚠ **needs the fifth source document 01 proposes (`Q5 purview`)** |
| **neglect** (the absence of `restore`) | ⭐ **nothing, and that is correct.** The crossing neglect eventually causes **is** Q3, one or ten seasons later. **Neglect is not an act and must raise no question**; what raises the question is the wall, when it falls | — | ✓ by design |

**THE PAYOFF, AS EXECUTION RATHER THAN AS A PROMISE.** `wear` writes condition down at MATTER
(`matter.py:229-246` — unconditional, over every site, **before** any act's delta, so the two writers
need no commutativity argument, and `w.fixtures.wear(s.kind)` at `:233` carries *"NO SILENT DEFAULT —
unregistered kind raises"*); the floor is crossed at `:262`; an Event is built at `:267-270` and appended;
`w.crossings` records `(site_id, verb, before, after, ev_id)` at `:272`; at DELIBERATE **every person
present at that granary's rung gets a Question whose referent is the granary**; each forms whatever
Candidate their own state admits — repair it, move the store out, petition about it, or nothing — and
each is scored against their own convictions.

> **A GRANARY THAT FALLS BELOW ITS `keeps` BAND ASKS SOMEBODY ABOUT ITSELF. Nobody wrote that scene.
> No player was present. The building started it.**

**And the symmetric half is why A.6.1's upward predicate and A.6.2's referent are ONE deliverable:** a
wall repaired past `mans` asks the people in the ward about itself too, and what they form from it is
*keeping the walk*. **Without the upward crossing only ruin speaks.**

**What the player TOUCHES — five affordances, every one an existing or proposed act, never a menu of
abstract options:** at a plot you hold — `found` a new plot (with leave), open a works Record naming a
kind; at a fabric you are present at — `restore` it, `work` it, contest it; at a `works` you hold —
`confer` it on somebody, `destroy_record` it (abandon); at a rung you govern — `utter` an order scoped
to it and court swearers (their act, their choice); at a store you hold — `transfer` it up, down, into
a `works`, or to a hearth that is short.

**Five bounds stop a player building everything, and none is a cap.** Acts (each of `found`,
`create_record` and every `restore` is one of about five, at one place, and the actor must be present)
· terms (stages ripen on their own schedule — **matter cannot buy time**) · matter (the cost draws from
a store that also feeds the people in it — **every building is a decision not to eat**) · wear
(everything already built is a standing bill against the same store, so **the more you have built the
less you can build** — a bound that tightens with success, which no cap does) · **other people**
(leave, masters, swearers, and whoever is present to break what you raise).

---

## A.9 · THE LOOPS, NAMED AND SIGNED (`01_AXIOMS.md` **ID-16**, `:544-548`)

**ID-16, verbatim:** *"Every feedback path appears in the register with a direction. **A model in which
every loop is negative CONVERGES** — season 40 resembles season 30 — and convergence is not a design
goal, it is what happens when a design has no other ideas."*

⚠ **THE TREE'S CURRENT STATE IS THAT DEFECT, AND `ARCH §F.20` IS THE SAME OBSERVATION FROM THE OTHER
SIDE.** The live register (`engine/season/hole_register.yaml`, `kind: LOOP`) has four rows — and
**all four are inside the claims machinery. Nothing in the register is about the world.** §F.20 says
why: *"the world only decays — nothing is ever founded or built."*

| id | the cycle | sign | the damping, named — each a mechanism that already runs |
|---|---|---|---|
| **BW-L−1 · WEAR** | condition ↓ at MATTER → verbs removed → less yield → less to spend → condition ↓ | **−** | the ceiling is full for a finished work, so repair is always possible in principle; a fabric at 0 is a ruin on a plot that can be built on again. **The loop has a floor and the floor is re-enterable.** MEASURED: `condition.worn 74` per season, 1000 → 990 |
| **BW-L−2 · SUBSISTENCE** | people eat stores → less surplus → fewer people can be seated | **−** | `draw = wt × len(eaters)` (`matter.py:174`). **Built, and currently unreachable** — A.6 |
| **BW-L−3 · SIEGE** | a contest loss grades a negative condition delta → fewer verbs → weaker defence → more losses | **−** | the strata order forces pre-investment (A.3.1); the clamp bounds the sum |
| **BW-L+1 · THE WORKS LOOP** | a PRODUCER above its band → `(Rung, yield)` → `(Rung, stores)` → matter for `restore` → condition up → more yield | **+** | **structural, three ways:** `wear` subtracts unconditionally at MATTER **before** any act's delta; `condition_scale` clamps once (`resolve.py:549`); `ceiling` bounds it to the matured stages; and every act comes out of a budget of about five |
| **BW-L+2 · THE SHELTER LOOP** | DWELLINGs above `shelters` → `capacity` → the envelope may grow → more presence → more hands **and more mouths** → more works | **+** | every added body raises the draw against the same larder; and **capacity falls with the fabric**, so the bound tightens as the place wears. **This is `ED-SE-0051`'s subject** |
| **BW-L+3 · THE PATRONAGE LOOP** | a faction builds in a place → its members are present → `density` rises → more hands and more claims → more works | **+** | an act budget per person; `hold` is 1-per-object, so a rival taking the plot ends the patron's route in; and ⭐ **the memory of who built it decays** (`claim.decayed`, `matter.py:147-153`), so patronage must be renewed or forgotten |
| **BW-L−4 · THE NEGLECT LOOP** | a governor stops paying → bands cross → **crossings emit** → witnesses mint claims → his standing falls → he can bind fewer people to keep the wall → fewer keep it | **−** on him, **+** as drama | claim decay erodes the grievance; and **T-m** (`:1154`) means he may always re-court and re-bind, paying acts. **The loop is escapable and the escape costs politics** |

⭐ **THE TWO HALVES ARE COUPLED AT THE MECHANISM RATHER THAN BY TUNING:** every act of BW-L+1 adds a term
to BW-L−1, so the amplifying loop's gain falls monotonically as it grows. That is a bound that is a
property of the arithmetic rather than of a number somebody picked.

⚠ **THREE HONEST NOTES.** (1) **ID-16's own representation is BLOCKED** — it asks for a cycle
enumeration over *what is written × what is read* and says the read half is blocked (`:556-560`), so
this table is a claim about the loops I know of, **not a completeness claim.** (2) **The standing/
reputation loop is designed and INERT**: no verb writes any `Person` interior field (`ARCH §F.20a`), so
building visibly cannot move anyone's conviction. R7 calls that *"unavoidable and first-rank"*
(`design_rulings_2026-09-06.md:178`). (3) **The falsifier of the whole table is one sentence**:
§F.20's *"the world only decays"*. **The design stops being all-negative exactly when a `rung.founded`
and a `site.built` appear in a run's log, and that is currently zero and measurable in one grep.**

---

# PART B · WHAT THIS ADDS, AND WHAT IT MAKES UNNECESSARY

**The bar:** `01_AXIOMS.md` **ID-13** (`:489`, *"A DECLARED FIELD MUST REACH A READER, OR IT IS NOT
DECLARED"*) and **ID-12** (`:454`, a closed set lives in data). No new primitive without a row here.

## B.1 · Added, each with why it is not a new primitive

| added | what | why it is not a new primitive |
|---|---|---|
| **verbs: 1** | `found` | it is the **producer two declared write-matrix rows have been waiting for** — `(Rung, exists)` at `write_matrix.yaml:294-300` and `(Site, exists)` at `:322-328`, both with a step, a class, a `by:` and an emission and **no verb naming either cell.** `H-41` is `absent` and §F.20 blocks build step 2 on it. **This closes `ID-13` rather than adding to the tree** |
| **effect bodies: 2** | `@effect_for("found")`, `@effect_for("restore")` | `restore`'s row is `grade: "ruled"` with five full columns and a specified formula (`verb_table.yaml:448-467`); what is missing is the body. Eleven exist (`effects.py:92-437`); this is the twelfth and thirteenth |
| **Queries: 2** | `ceiling(w, site)`, `capacity(w, rung)` | resolver-side, owned by Nobody, storing nothing — **T-a** (`:255`). `capacity` is already **declared** in the §17 Query roster (`holonic_ARCHITECTURE.md:600`), so it is an implementation, not an addition |
| **Record kinds: 1** | `works` | a data row under **ID-12**, opened by `create_record`, which already runs. `ARCH §A.3` row 11 and `ARCH §B.4/B.5` (`:255-261`) already folded two kinds in on this reasoning |
| **roster rows: 5 families** | `site_kinds` + the coordinated `wear_per_season` / `band_floors` rows the loader demands (`fixtures.py:106-123`) | data under **ID-12**, in an extensible roster whose lookup still refuses (`rosters.yaml:809-812`). Baseline is two kinds, not three (`:814-815`) |
| **terms operands: 2** | a `ttl` and a `cardinality` conjunct on the works Record | `Record.ttl` already exists (`carriers.py:430`); `cardinality` is one of the closed seven (`rosters.yaml:1114`) |
| **predicate conjuncts: 2** | the ENCLOSURE reading in `WorldReader.read`'s `contain.path` branch; the object-domain check in `add_tenure` | both land **inside a single existing owner** — `world_q.py:732-737` and `state/world.py:242-256`. Neither is a new form; an eighth `requires` form would refuse at load (`rosters.yaml:1092-1094`) |
| **fixture columns: 1** | `houses` per DWELLING kind | one column on a kind roster that must be authored anyway. `[OPEN — Jordan tuning]`, and it is an **addition** |
| **content moves: 2** | fabrics at the rungs people are in; 16 faction-subject holds → the person who holds that rung's seat | `populated.py:357/361/373` and `:613-618`. **Content, not schema** |

## B.2 · Made unnecessary — and every row here is a DELETION, not a renaming

| made unnecessary | why it survives the cut |
|---|---|
| `Rung.sites` | it is whitelisted at `carriers.py:568` and is *"a BACK-REFERENCE NOTHING MAINTAINS — it is empty for every rung in the corpus"* (`matter.py:198`), with **no `(Rung, sites)` row in `write_matrix.yaml`** — so it cannot be written through the gate at all. `footprint`-style walks and `matter.py:205`'s `Site.rung` read are the maintained side. ⚠ **AND THIS IS A DEPARTURE, NOT PURE CONFORMANCE:** `ARCH §B.3:235` declares `Rung := (id, kind, matter(stores, sites[], records[]), …)`, so Layer 1 lists `sites[]`. **ID-13** (`:489`) is what licenses the cut against that declaration, and saying so is the honest form |
| an `undertake` verb | `create_record` does the whole of it, holder included (`effects.py:262-290`), so this collapses to a Record kind plus a stage template |
| `build` / `raise` / a `Build` family | `restore`, bounded by `ceiling`. **One act at different bands**, arithmetically exact |
| `raze` as a verb, **and a build queue** | a further negative-delta contest at `Felled`; and `hold`'s 1-per-object plus the `cardinality` conjunct, which is a **refusal** rather than a scheduler |
| `garrison` / `convert` / `capture` / `improve` / `ruin` as verbs | a garrison is `presence` filtered by who is bound; conversion is a new works Record on a standing fabric with a different kind; capture is `hold` changing hands; improvement is `restore` under a rising ceiling; a ruin **is** condition 0 |
| `hold : Person → Site` | A.5 — three expressible things die, and the commons dies with them |
| the 16 faction-subject `hold` Tenures | A.5.4 — a Layer 1 violation shipping in the default world, fixed by content |
| the ratified `confer`-on-a-memberless-holder patch | it repaired a condition A.5.4 **removes** |
| a settlement's stored civic kind, its transition registry, hysteresis, dwell counters and their load check | **nothing writes on the crossing.** A Query read differently two seasons running has written nothing and broken nothing. A place whose walls fall stops reading as a fortress with no transition row |
| thirteen settlement gauges as stored fields | `ARCH §B.3:237` — `NEVER: any social aggregate` — graded STRUCTURAL at the type, CONVENTION at a schema edit (`:240-244`). Each is a Query over fabrics, stores, holds, contains and commits |
| a three-grade footing table with a `charter` **edge kind** | **a `Site` standing at a rung you do not hold.** The fabric IS the charter, and the grade costs nothing: `hold` gives you the ground, a standing fabric gives you presence-in-fact, `density` gives you reach |
| `serves:` as a runtime fact | A.5.5 — a Query over `hold ∩ commit`, which cannot go stale |
| a `Holding{confers:[Capability]}` object | `eligibility_kinds` is `[own, remit, hold, presence]` (`rosters.yaml:160`) and its note reads *"⚠ `capability` IS NOT AND MUST NEVER BE A MEMBER… An office makes an ORDINARY verb eligible; no verb exists only for office-holders. Adding a fifth kind is a DESIGN CHANGE… and not a table edit"* (`:152-156`). **A built thing may supply an OPERAND — a store to spend, a hall to sit in, a site to be present at — never a gate on who may attempt a verb.** This is the most tempting import in the subject and the one that would break the eligibility model |
| a facility-tier ladder **in the head**; any `infrastructure_score` or settlement-level `condition` | the node-keyed average by another name (`holonic_ARCHITECTURE.md:449-451`); and R7's *"no magnitude carrier is admitted at any scale"* |
| a **siege subsystem** | A.3.1 — three reads onto three mechanisms that already exist |

## B.3 · Two cuts WITHDRAWN as breakages, and one argument withdrawn as unsound

| withdrawn | why |
|---|---|
| ~~cut `fort_level`~~ | **A.3.3.** Live readers in `engine/autoload/game_state.py`, an already-derived single-owner shape with the rule in a comment, and a descriptor key behind a **blocking** export |
| ~~cut `facility_tier`~~ | **A.3.3.** Read live at `systems/settlements/sim/registry.py:97`, set by its loader at `:146`, exported behind the same gate |
| ~~the destroy-cascade licence for the ontology~~ | **A.1.1.** `holonic_ARCHITECTURE.md:588-589` is about which Tenures end, not which objects may exist; and nothing destroys a Rung or a Site at all |
| ~~"widening `hold` makes `restore`'s `share` computable"~~ | **A.5.1.** `share` and `draw_share` are declared **Queries** (`:599-600`); `share` was never a field |

## B.4 · E, scored LAST and as a ratio — `CLAUDE.md` §0.06

**In:** 1 verb · 2 effect bodies · 2 Queries (one already declared) · 1 Record kind · 5 roster
families · 2 terms operands · 2 conjuncts inside existing owners · 1 fixture column · 2 content moves.
**Out:** 1 declared-but-unwritable field · 9 verbs never minted · 1 edge kind · 1 object · 16 content
rows · a transition registry with its hysteresis and its load check · 13 gauges · 3 stored aggregates
· and **every "+N to a roll" reading of a built thing.**

**Carriers added: 0. Fields on carriers added: 0. Write classes, steps, strata, eligibility kinds,
tenure kinds and `requires` forms added: 0.**

> **E PASSES AS A RATIO — net deletion, against what N and R found — AND WOULD FAIL IF SCORED ALONE.**
> §0.06: *"alone it is satisfiable by amputation."* The legibility half passes on its own test: the
> player reads a **band name** because that is what the resolver reads, and remaining work as a
> picture. ⚠ **FINDING:** the three-way coupling of `wear` × `restore` × yield-scaled-by-condition has
> a steady state **the player cannot compute** — they can intuit direction and not equilibrium. The
> repair is interface-side, from claims they already hold. **Stated as a limit, not scored around.**

---

# PART C · THE THREE QUESTIONS

## C.1 · Who owns this?

| the thing | owner | not |
|---|---|---|
| a fabric's condition | **`Site`**, one writer per write class (`write_matrix.yaml:315-321`) | never a `Rung`, never an aggregate |
| a plot, its store, its dates, its records | **`Rung`** (`carriers.py:568`) | never a social aggregate (`ARCH §B.3:237`) |
| a `works` in progress, its stages and its ttl | **`Record`** (`carriers.py:422-431`) | never fields on the Site — then nobody would be master and MATTER would have no holder to check |
| who is master of a `works` | the **`hold` Tenure's subject**, minted by `create_record` (`effects.py:288`) | never a field on the Record (`effects.py:286`) |
| who holds the ground | the **`hold` Tenure**, 1 per object, `Person` subject only | never a faction (A.5.4) |
| `ceiling`, `capacity`, `verbs`, `presence`, `density`, `footprint`, `serves` | **Nobody.** Resolver-side Queries, World first | never stored, never cached outside the driver |
| a new site kind's wear and band rows | `rosters.yaml`, enforced **both directions** at `fixtures.py:106-123` | never a default |
| the enclosure reading | **one branch**, `WorldReader.read`'s `contain.path` (`world_q.py:732-737`) | never a per-verb table, never an eighth `requires` form |
| the object-domain refusal | **`World.add_tenure`**, already *"The ONE writer"* (`state/world.py:223`) | never a per-call-site check |

## C.2 · What can check this? — `STRUCTURAL | MECHANICAL | CONVENTION`

A claim of STRUCTURAL that is really MECHANICAL is *"a guard that cannot observe what it guards."*

| claim | grade | the checker, named |
|---|---|---|
| a fabric's condition cannot be node-keyed onto a place | **STRUCTURAL at the type** | `Rung` has no condition field and `__setattr__` raises (`carriers.py:590`); `ARCH §B.4:252-253` says the collapse *"cannot be spelled"* |
| a built thing gains no new carrier | **STRUCTURAL** | there is no class to construct |
| `hold` never reaches a `Site` | ⚠ **MECHANICAL, once the conjunct lands — ~~CONVENTION~~ NOTHING today** (corrected 2026-09-17: *convention* implies a reviewer with a rule to read, and no rule is written anywhere in the code; `04` §C.2's *"Today: nothing"* is the honest word) | `add_tenure` checks kind (`:242-247`) and `contain` ascent (`:248-256`) and **nothing about object class**. Layer 1 grades it STRUCTURAL (typed) (`ARCH` PART D row 14) in a typed language this is not. **The gap is named rather than graded away** |
| a faction is never a `hold` subject | ⚠ **CONVENTION, and VIOLATED 16 times in the default world** | same conjunct; `01_AXIOMS.md:1078`; `populated.py:613-618` |
| a new site kind arrives with its wear and band rows | **MECHANICAL at load** | `fixtures.py:106-123`, both directions, raising `Forbidden`/`Ungraded` |
| no eighth `requires` form is smuggled in | **MECHANICAL at load** | `rosters.yaml:1092-1094` — *"a design change, not a table edit"* |
| a built kind never regrows unauthored | **MECHANICAL** — an explicit `regrowth: 0` row per built kind, plus a test asserting it | the polarity rule makes a missing row RAISE (`rosters.yaml:809-812`), so the absence of a row is a crash rather than a silent zero. **Load-bearing on the game** — it is the line between authored and unauthored construction — so the test earns its existence under §0.1 pt 5 |
| a repair that changed nothing mints no success Event | **MECHANICAL at the write** | `ARCH` PART D row 5 (`:934`): the gate refuses `before == after`, so the receipt is never minted |
| a fortification's band is never rendered as fact | **CONVENTION**, and it cannot be made structural here | the renderer does not exist. `ARCH §C.11:758-761` is the argument; the check is that a reviewer reads the read list |
| **the capacity arm of `ED-SE-0051`** | ⚠ **NOT A GRADE — a RULING REQUEST**, corrected 2026-09-17 | ~~STRUCTURAL~~ was a category error: this column asks *what construction checks this claim*, and a ruling request has no construction because it has no answer yet. It is the suite's **RR-2** (`04` §C.4), `needs_jordan: true`, **LAYER 1 SILENT** stated in the row itself (`editorial_ledger_se.jsonl:51`). A.7 recommends; it does not decide. What IS checkable once ruled is `capacity`'s shape — a Query with a floor and no magnitude field (`BW-7`) |
| **the commons `share` reading** | **MECHANICAL** | `share`/`draw_share` are declared Queries (`holonic_ARCHITECTURE.md:599-600`) with no implementation; a repair's `share` at a many-drawer site is a *formula* question with one owner, checkable by a test over a commons with N drawers |
| **site-kind naming** (`rampart` vs `wall`; `minster` vs `chapel`) | **CONVENTION** | the roster refuses an unregistered kind, so nothing breaks either way. `CLAUDE.md` §4's idempotence test applies: choose the word ordinary usage supplies |

## C.3 · Whose act makes it happen?

**Every row: what is written, by whose act, read by whom, emitting what.** No row is a system
depositing a thing.

| what is written | by whose act | read by | emitting |
|---|---|---|---|
| `(Rung, exists)` + the founder's `contain` move | a **person**, `found`, `own` + presence in `requires` | `presence`, `parent_of`, `descendants`, the larder step | `rung.founded` / `found.refused` |
| `(Record, exists)`, `(Record, stages)`, the maker's `hold` | a **person**, `create_record`, `own` | `matter.py:73-74`'s holder check; `ceiling` | `record.created` |
| `(Record, matured)` | **nobody** — the clock the opening act wound, at MATTER, `causes[]` naming that act | `ceiling` | `term.matured` |
| `(Site, condition)` **up** | a **person**, `restore`, `own` + `presence:<site>`, through the summing clamp | `verbs`, `site_yield`'s scaling, `capacity`, the band predicate | `site.restored` / `restore.refused` |
| `(Site, condition)` **down, by wear** | **nobody** — MATTER, AX-5 motion 1 | the same four | `condition.worn` · `condition.band_crossed` |
| `(Site, condition)` **down, by an attacker** | a **person**, through the contest seam, graded to a negative delta | the same four | the contest's own emission |
| `(Rung, stores)` up | **nobody** at MATTER (yield, scaled by condition); a **person** by `transfer` | the larder step next season; `restore`'s threshold | `yield.taken`, `stores.changed` |
| a shortfall | **nobody**, and **it produces no outcome** (`matter.py:179-185`) | a run's TRACE, and nothing else today | nothing — and A.7 is why that matters |
| a `hold` changing hands | a **person**, `confer`/`revoke`/`release`, refused while one is live | `in_holdings`, `hold_force`, `footprint`, `serves` | the verb's own emission / its refusal |
| a `works` ending unfinished | the **ttl the opening act declared** (**T-n**), or `destroy_record` by its holder (**T-m**) | `ceiling` — which freezes where it stood | the lapse / `record.destroyed` |

---

# PART D · FALSIFIERS — `01_AXIOMS.md` **ID-11** (`:453`), *ship the falsifier with the claim*

| # | claim | what would show it wrong |
|---|---|---|
| **BW-1** | Binding Q3's referent to the site makes the built world actionable | `test_q3_a_band_crossing_raises_a_question_about_the_site_not_the_verb`, run as a **unit** test that plants a crossing tuple — a season run is the wrong instrument (`04` item 1a). ⚠ **ARTIFACT CORRECTED 2026-09-17.** ~~"`work` candidates > 0 on the harness corpus, against 723-of-723 refused today"~~ confuses two counts: **723 Candidates DO form** — `work` is `own`-eligible and `site` already binds to the referent — and all 723 are **refused by the fold**, which the tree measures in its own words (*"`work` 723 refusals with no execution"*, `test_season_shape.py:7279`; *"`work` alone refuses 723 times"*, `:7240`; `verb_table.yaml:765`). The artifact is therefore **`work` EXECUTIONS > 0**, i.e. `work` leaving `corpus_run`'s `VERBS ONLY REFUSED` list — and it is **conditional on a world where a floor is crossed** (`04` item 1b), not on BW-2. **If executions rise with neither 1b nor BW-2, my account of the blockers is wrong** |
| **BW-2** | Matter reaches people once commons eaters ascend and fabrics key to the rungs people are in | `test_a_commons_site_draws_for_everyone_under_its_rung`; `test_some_site_has_a_person_present`. **Artifact: hearths holding matter > 0 and sites-with-presence > 0, against 0/211 and 0/74 measured today** |
| **BW-3** | `hold` reaching a `Site` is refused | `test_a_hold_on_a_site_is_refused_at_add_tenure` — `Tenure(p, <site id>, "hold")` raises `Forbidden`. **It goes RED today**, which is the point: the refusal is currently unenforceable. Control: `populated` still loads, and all 35 live holds still land |
| **BW-4** | No faction is a `hold` subject | `test_no_hold_tenure_has_a_faction_subject`. **Artifact: hold subjects person 35 / faction 0, against 19 / 16 measured today.** If the count cannot reach 35 without minting persons beyond the ruled 46-NPC roster, the content fix is wrong and the schema question re-opens |
| **BW-5** | Five families are roster rows and cost no machinery | the loader's coordinated-row check goes red on a kind with no `wear_per_season` or `band_floors` row (`fixtures.py:106-123`); and `test_built_kinds_do_not_regrow` asserts `regrowth == 0` for every ENCLOSURE, HALL, VESSEL and DWELLING kind. **If a built kind ever carries a non-zero row, a fortification repairs itself with no author and the design has silently taken the fourth-motion route AX-5 refuses** |
| **BW-6** | `Rung.sites` is dead and deletable | `test_rung_has_no_sites_field`. ⚠ **The falsifier that matters is the other direction:** if any reader is found that needs it, the cut is wrong **and `ARCH §B.3:235` was right to declare it** |
| **BW-7** | `capacity` is a Query with a floor and no magnitude carrier | `test_capacity_has_a_floor_and_no_magnitude_field`. Falsified by a rung whose `capacity == 0` while `stores > 0` making `found` self-defeating — **the attack that put the floor there** (A.7). Gated on `ED-SE-0051` |
| **BW-8** | `restore` mirrors decay and stops at the ceiling | `test_restore_mirrors_decay_and_stops_at_ceiling`. **Artifact: condition rises in a run's log — `site.restored` is 0 today.** And the two units decisions (`(1 − condition)` normalised against a 1000-scale int; `share` at a many-drawer commons) must be **decided in the same commit or the body is not writable** |
| **BW-9** | `found` is the producer `(Rung, exists)` and `(Site, exists)` have been waiting for | `test_found_is_the_producer_for_rung_exists`. **Artifact: a `rung.founded` and a `site.built` Event in a `populated.py` run's log — currently zero, measurable in one grep. THIS IS THE ARTIFACT THAT MOVES THIS DOCUMENT'S GRADE OFF `paper`**, and nothing else in this file does |
| **BW-10** | A standing enclosure refuses a `move` through its rung | `test_move_through_a_standing_enclosure_is_refused_unless_admitted`, with the refusal TRACE as the artifact. **Control: `travel.blocked` fires 23 times per season today, so the channel is live and a rise must be attributable to the conjunct and not to the ladder check.** Falsified if the reading needs an operand the `contain_path` form's `needs:` does not carry (`rosters.yaml:1118`) — then it is an eighth form and refuses at load |
| **BW-11** | The upward band crossing makes the positive half witnessable | `test_an_upward_band_crossing_emits`. **Artifact: a Q3 question raised by a repair.** Control: the 74 downward `condition.band_crossed` emissions per season must not change count |
| **BW-12** | A built world with no player in it founds, wears, stalls, falls, forgets and **asks** | a season in which it emits nothing. Five channels are named and **all five are conditional on BW-1 + BW-2**: a stage ripening with nobody present; a crossing; a stall's refusal; a master's death stopping a `works`; a `works` lapsing at its ttl. ⚠ **Stated as a condition, not banked** |
| **BW-13** | `fort_level` and `facility_tier` are not free cuts | delete either and show CI green. **Predicted red** at `tools/export_descriptors.py --check` (blocking, workflow `:137`) and at `systems/settlements/sim/registry.py:97`'s `ap` property |
| **BW-14** | The ontology stands on cardinality, not on a destroy cascade | name an object in this tree that a verb destroys. **There is none: `(Rung, exists)` and `(Site, exists)` have zero producers.** If one is found, A.1.1's struck argument must be re-argued rather than re-instated |

### D.15 · **GRADE: `paper`** — and exactly what would move it

`CLAUDE.md` §0.2: *"A milestone juncture is done when the behaviour EXECUTES. Not when a document
exists with a `## Status:` line."* **Nothing designed in this document executes.** What runs today, and
is the honest ledger of it:

```
$ python -m engine.season.harness.populated  (1 season, seed 0) — MEASURED this session
  wear                    RUNS      condition.worn 74 ·  1000 -> 990
  larder draw             RUNS      matter.py:164-195   (the not_implemented row at :50-51 is STALE)
  yield                   RUNS      yield.taken 37 · stores.changed 37 · 4,810 units at 37 settlements
  band crossings          RUNS, DOWNWARD ONLY          matter.py:262
  a shortfall             RECORDED, NOT ACTED ON       matter.py:185
  works Records           RUN       record.created 69, with the maker's hold minted (effects.py:288)
  claim decay             RUNS      matter.py:147-153
  founding / building     ZERO PRODUCERS               site.built 0 · rung.founded 0
  restore                 NO EFFECT BODY               site.restored 0 · resolvable_verbs() 18 of 38
  work                    RUNS, REFUSES EVERY TIME     work.unavailable 38 · site.worked 0
  a fabric anybody is at  NONE      0 of 74 sites
  a hearth holding matter NONE      0 of 211
```

**The first execution artifact is BW-1's `work` candidate count; the artifact that moves the grade is
BW-9's `rung.founded`.** Both are cheap, both are currently zero, and both are measurable in one run.

---

# APPENDIX · CITATION REPAIRS

Every `path:line` in this document was opened before it was written (`CLAUDE.md` §0.1 pt 3: *"A
citation you have not opened is not a citation"*). These were carried in from the design and analysis
stages **wrong**, and are corrected silently above and recorded here.

| cited as | actual | consequence |
|---|---|---|
| `world_q.py:520` — Q3's referent | **`:518`** | the append; the presence gate is `:515-517` |
| `matter.py:265` — the crossing predicate | **`:262`**; the Event at `:267-270`; `w.crossings.append` at `:272` | — |
| `matter.py:188-193` — "recorded, not acted on" | **`:179-185`**, closing at **`:185`** | — |
| `matter.py:196-201` / `:198` — the `r.sites` back-reference | **`:197-204`**, the sentence at **`:198`** | — |
| `matter.py:229-245` / `:242` — wear | the wear step; `not_implemented` is at **`:50-51`** and **is stale about larders and yield** | the stale row was quoted as evidence they were unbuilt |
| `holonic_ARCHITECTURE.md:583-585` — destroy sets `until` | **`:588-589`** | and the clause says *"destroys nothing else"*, which is why A.1.1's argument is struck |
| `holonic_ARCHITECTURE.md:536` — `hold`'s domain | **`:538`** (`:536` is the table header) | — |
| `holonic_ARCHITECTURE.md:600` — `share` | **`:599-600`** — `draw_share` at `:599`, `share` at `:600`, under §17's header at `:591` | — |
| `carriers.py:557` — `Rung.sites` whitelisted | **`:568-569`**; `__setattr__` gate at `:590` | — |
| `carriers.py:410-418` — `Site` | the dataclass at **`:411`**, fields `:413-418`, `drawers` at **`:418`** — **declared and readable** | *retired* on the write matrix means unwritable through the gate, not absent |
| `world.py:245` — `add_tenure`'s kind check | **`:242`**; the `contain` ascent check at **`:248`**; the append at `:257` | — |
| `populated.py:366-375` — the site mint | **`:357`** community, **`:361`** hearth, **`:369-374`** the loop, **`:373`** the mint | — |
| `populated.py:612-618` — the faction holds | the loop opens at **`:613`**, the `Tenure` at **`:617-618`**, the comment at `:602-607` | — |
| `verb_table.yaml:464` — `restore`'s effect | the row is **`:448-467`**; the formula is at **`:465`**; `writes` `:461`; `emits_on_refusal` `:463` | — |
| `resolve.py:541-551` — the summing clamp | **`:538-553`**, the clamp expression at **`:549`** | — |
| `predicates.py:60-103` / `:105-141` | `in_holdings` at **`:60`**, `under_purview` at **`:105`** | — |
| `fixtures.py:105-125` — the coordinated-row check | **`:106-123`** for `wear_per_season` + `band_floors`, **both directions**; **`:124-129`** for `site_yield`, **one direction only** | a new kind needs wear and band rows or the world will not load; a `site_yield` row is optional |
| `10_SUPERSEDING.md:1275-1278` — the commons closure | **`:1275-1279`**, with the single-drawer arm at **`:1280-1282`** | both halves are load-bearing on A.5.2 |
| `tools/registry.py:88-96` / `:93` — `terr.fort_level` as a descriptor key | **that is a docstring.** The authored row is `references/descriptor_registry.yaml:94`, cooked to `engine/engine_params/descriptors.json:143` by `tools/export_descriptors.py --check`, **blocking** at `.github/workflows/valoria-ci.yml:137`. `set.facility_tier` likewise, `descriptor_registry.yaml:173` → `descriptors.json:123` | the chain is stronger than the citation, not weaker — which is why A.3.3's cut is withdrawn |
| `settlement_layer_v30.md:905` — *"canon's `Ob = 2 + Fort Level`"* | **that string is not in that file.** `:905` is a table separator. The live formula there is `Defense × 20 + Fort Level × 30` at **`:48`**; `Ob = 2 + Fort Level` lives at `systems/characters/reference/conviction_track_v30.md:138` and `systems/mass_battle/reference/military_layer_v30.md:177` | a fortification claim was cited to a file that does not carry it |
| `rosters.yaml:149-160` — `capability` forbidden | values at **`:160`**, the note at **`:152-156`** | — |
| *"the 211-building layer sits outside every gate"* | **overclaimed, and corrected in place at A.5.5.** The `tests/valoria` validator `venues.yaml:37-38` claims does not exist; but `populated.py` **does** refuse when `seat_precedence` and `seats:` disagree (`venues.yaml:136-138`), and `tools/export_npc_roster.py --check` fails on a row naming a nonexistent case, place or person (`references/ci_checks_registry.yaml:380`). **What is ungated is the building rows' geography resolution, and only that** | found by this document's own adversarial pass; the sweeping form was the easier claim to make |
| `ARCH:NNN` line forms throughout | rewritten as **`§Letter.Number`** — `§A.3`, `§B.3`, `§B.4`, `§B.8`, `§C.11`, `§F.20`, `§F.20a`, `Part D` rows 5 and 14 | `CLAUDE.md` §9 / the plan's standing instruction |

**Two scope notes, so the appendix is honest about what it does not cover.** (1) The reconciled build
order's item 5 — deleting `budget_office_bonus` — is **IN-lane** and belongs to document 01; it is not
falsified here. (2) **No precedent finding is cited anywhere above.** Heroes of Might and Magic is
*"Absent entirely. Not surveyed, not declared, not cited"*
(`research/valoria_game_precedent_companion_v1.md:553`); Manor Lords is named twice and never surveyed
on its own terms; the burgage plot appears in this repository only inside a prior proposal's own
Borrows line (`proposals/2026-09-10-settlements-factions-populations/02_PROPOSALS_SUBSTRATE.md:430,434`).
**Citing any of them as a precedent finding would be inventing one.** The single shape used above
is the garrison convergence, which has a pass behind it: *"garrison-versus-field as the same unit pool
wearing a different assignment"*, four of four titles (`valoria_game_precedent_companion_v1.md:323-326`).

---

**END — `02_THE_BUILT_WORLD.md`. PROPOSED. HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Grade: `paper`.**
