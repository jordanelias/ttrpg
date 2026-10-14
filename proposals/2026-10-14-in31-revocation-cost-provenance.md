# IN-31: what a revocation costs, and where a seat's provenance lives

## Status: PROPOSED (2026-10-14) · design only, builds nothing · reference under `CLAUDE.md` §0.05
## Position: IN-31 (H-100), `workplans/valoria_master_workplan_v9_part5.md` `### IN-31` · Lane: IN (SE) · IDs: none allocated
## Measured at HEAD `40926a95` (B-J; IN-48 built). A path with no top-level directory is under `engine/season/`.

The brief is the IN-31 entry: WHAT, DEPS, EDITS, EXIT and FALSIFIER. This document does not restate it.

---

## 0. Verdict

**The provenance carrier already exists. It is `Office.conferral` for a `hold`, and `Tenure.kind` for
a `delegate` edge. No field is added, so the Tenure schema does not move.**

- A `hold`'s provenance is the seat's declared conferral basis: `appointed`, `elected`, `annex`, or
  `None`. That roster is Jordan's ED-IN-0256 ruling (2), *"HOW A SEAT IS FILLED"*
  (`rosters.yaml:1845-1863`). No act can change it on a live seat: `_req_establish` refuses a
  `conferral` difference on an existing id (`loop/predicates.py:296-300`). So reading it at revoke time
  gives the same answer a stamp taken at seating would.
- A `delegate` edge's provenance is its kind. IN-48 already gives its dismissal its own branch
  (`loop/effects_governance.py:318-324`).

**What `revoke` writes, per provenance:**

| provenance | `revoke` closes | `revoke` also writes on the person revoked |
|---|---|---|
| `appointed` | his `hold` | a `ban : him → Act.via` (the revoking seat) |
| `elected`, `annex`, `None` | his `hold` | nothing |
| `delegate` (IN-48 branch, unchanged) | his `delegate` edge | nothing |

The `ban` is SC-03a's existing restraint. Its existing readers already make it bite: `confer` declines
to seat a banned man (`loop/effects_governance.py:128`), and `oblige` refuses him service
(`loop/predicates.py:414`). No new reader is built.

**The mapping has one owner**, `REVOCATION_DISPOSAL` in `state/gate.py`, beside `REVOCATION_RULES`.
The import refuses a mapping that is not total over `CONFERRAL_BASES ∪ {None}`. A seat whose
conferral is outside the mapping makes the precondition REFUSE, never fall back to a default.

**The write gate admits the `ban` under `T-o`, through a licence.** The licence is computed in
`refuse_unauthored`'s first pass from the `hold`s this write closed under `T-o` on an `appointed`
seat. That is `handover`'s two-pass shape (`state/gate.py:1139-1150`, `:1045`).

**A computed `revoke` is not driven** (Jordan, H-207 ruling (A), `hole_register.yaml:4451`).
- Measured: it is formed and attempted, and it executes 0 times in four seasons of seed 0 (§4).
- At build, only `appointed` seats can be revoked by anyone.

So no computed run can show two provenances, and the design cannot move a computed outcome. The EXIT
is a seeded world, with one holding placed by hand, plus hand-built revocations.

---

## 1. The six ways, read against the code

The H-100 row says the corpus holds seats six different ways (`hole_register.yaml:1925-1960`). Its cite
names the research vocabulary (bureaucratic, kinship, military, ideological, patronage, purchased),
and records that a `power_bases` roster built from it was DELETED because nothing read it. The brief's
six (appointed, elected, annexed, inherited, imposed, delegated) are a different list. Each one,
checked against the code:

| way | carrier in code today | reachable at `build_realm(0)` |
|---|---|---|
| appointed | `Office.conferral == "appointed"` (ED-IN-0256 (2)) | 15 held seats; **6 can be revoked by a sitting holder** |
| elected | `Office.conferral == "elected"` | 8 held; 6 declare a revocation basis; 0 can be revoked at build |
| annexed | `Office.conferral == "annex"` | **0 seats declare it** |
| inherited | none. `conferral: null` on the Crown seats, by the translation note in the `offices.yaml` header (*"`succeed` ... left `null`"*). Heirship is the unbuilt `succeed` kind. | 7 held with `None`; 1 declares a basis (Hafenmark, `rung_above_in_holdings`, `offices.yaml:208-218`); 0 can be revoked at build |
| imposed | none. `Tenure.imposed` marks a sentenced `oblige` (`state/carriers.py`, `DETERMINED_BY`), which is not a seat, and no act seats a person by force | — |
| delegated | `Tenure.kind == "delegate"` (IN-48) | built per test only |

The figures come from the §4 probe.

**The ladder applied to the two with no carrier** (`CLAUDE.md` §0, steps 2 and 4):
- **imposed**: irrelevant. No act or edge seats a person by imposition. The nearest thing, a
  determination's sentence, is an `oblige`, not a seat.
- **inherited**: precedent. The H-100 row records that a roster with no reader was deleted, so
  nothing is minted for it. A `hold` on a seat declaring `conferral: None` reads as the value `None`,
  which the `offices.yaml` header's translation note already gives as heredity for the Crown seats
  (King, Queen, Heir, Princess, Duke of Valorsmark). When `succeed` is built, its edge carries
  heirship.

**Why `None` is a VALUE here and not "unreadable":**
- `Office.conferral` is optional by declaration (`state/carriers.py`: `if self.conferral is not None:
  require_member(...)`, quoted in the `offices.yaml` header).
- Jordan ruled the one revocable `None` seat strippable on 2026-10-12 (Hafenmark, `offices.yaml:215`;
  H-207 cite, `hole_register.yaml:4451`).
- Refusing every revocation of it would overwrite that ruling. The ladder forbids that without
  escalating, and nothing escalates, because the mapping (§2) gives `None` an outcome.

---

## 2. The design

### 2.1 The carrier: read, not stamped

`seat_provenance(off) -> Optional[str]` is NOT built. The provenance of a `hold` is `off.conferral`,
read where it is needed. A one-line accessor over one field is overhead (§0.06 E). The single owner
is the mapping below, and it is what every reader asks.

**Why reading at revoke time is exact, not approximate:** `Office.conferral` has no act-side writer.
- `_req_establish` refuses a re-founding that changes `conferral` (`loop/predicates.py:296-300`,
  *"re-founding, which `writes:` does not declare"*).
- The only other assignments are builders (`harness/populated.py:1057`, `:1114`) and one probe's
  hand-mutation (`harness/probes.py:1513`).

So a snapshot stamped at seating would always equal the live value. It would buy nothing and cost a
hash move (§3.2).

### 2.2 The owner: `REVOCATION_DISPOSAL` in `state/gate.py`

```
REVOCATION_DISPOSAL = {"appointed": BAN_KIND, "elected": None, "annex": None, None: None}
```

It sits beside `REVOCATION_RULES` (`state/gate.py:537-547`), with that dict's import-time refusal
shape:
- `set(REVOCATION_DISPOSAL) != set(CONFERRAL_BASES) | {None}` raises `Unspecified`.
- So does a value outside `RESTRAINT_KINDS | {None}`.

A fourth conferral basis therefore cannot be added without an outcome (`conferral_bases` is
`open: false`, `rosters.yaml:1847`).

**Why Python and not a YAML column:** the precedent is `REVOCATION_RULES`. The `revocation_bases`
roster note says *"THIS ROSTER NAMES THE BASIS AND NOTHING ELSE ... The rule is BEHAVIOUR and lives in
`state/gate.py`"* (`rosters.yaml`, the `revocation_bases` note). A dict hung on `conferral_bases` would
give one roster a second shape, which is shape divergence. The closest data precedent,
`arrangements.yaml`'s `disposes:`, is a per-ROW column. There is no row to put a column on here: the
key is a roster value.

### 2.3 Why `appointed` gets the ban, and the others get nothing

This is ladder step 5, taken as an assumption.

[ASSUMPTION; medium; Jordan to correct; revert: set every value in `REVOCATION_DISPOSAL` to `None`,
and the plan's FALSIFIER then fails by construction, as it should.]

- **The reason.** An appointed seat is filled by a superior's choice: r2 `03` §A.4, *"a superior names
  the holder"*, which is the gloss the `offices.yaml` header gives `confer` → `appointed`. Its
  revocation is that favour withdrawn by the rung that gave it. The H-100 research reads favour-derived
  seats as facing *"total ruin"* and kinship-derived seats as getting *"containment"*. It is tier 3: it
  gives vocabulary, not authority.
- **What makes the ban mean ruin is code, not that sentence.** `restrained(w, p, BAN_KIND)`
  (`queries/world_q.py:1019`) reads a ban on ANY seat. So a banned man is never seated by `confer`
  again (`loop/effects_governance.py:128`), never delegated a seat (`loop/predicates.py:137`), and
  never admitted to serve by `oblige` (`loop/predicates.py:414`).
- **The ban carries no term.** That follows SC-03a's assumption for a sentence's ban
  (`loop/effects_information.py:378-383`). Only a bench closes it (`determination`'s restraint
  closure) or a death (`cascade`).
- **An elected holder keeps his electors.** Revocation unseats him but does not bar him; his body may
  return him. The seat's own act (`confer` today, an unruled election act later) may seat him again.
- **`annex` and `None` (heredity, as read in §1) get containment**: the hold closes and nothing more.
  `annex` has no seat at build, so its outcome is declared but cannot be observed (§5, residue R2).

**Why not grade by `Tenure.degree`, or write `standing` or `regard`?** §6 covers each.

### 2.4 The writes in `_eff_revoke`

The ordinary branch (the code after IN-48's `office == via` + `to` branch, `loop/effects_governance.py:325`)
becomes three steps.

1. **`closed`**: the live `hold`s on `obj`, as today. There is at most one, by S15 cardinality.
2. **`disposal = REVOCATION_DISPOSAL[off.conferral]`.** A `KeyError` cannot be reached here, because
   `_req_revoke` refuses first (§2.6). The effect still checks `off.conferral in REVOCATION_DISPOSAL`
   and returns `NO_CHANGE` otherwise, the backstop shape of `_eff_confer`'s `:120-121`.
3. **When `disposal == BAN_KIND`**, for each closed hold whose subject `h` is not `a.actor`, not
   already `restrained(w, h, BAN_KIND)` and still in `w.persons`: build
   `Tenure(H(w.world_seed, w.tick, h, f"ban:{a.via}:{a.id}"), h, a.via, "ban", w.tick)`.
   - The kind is spelled LITERALLY. `data/verbs.py::_derive_openers_from_effects` reads it there, as
     `_disposal` does (`loop/effects_information.py:372-376`), and the derived opener set for `ban`
     becomes `{determine, revoke}`.
   - The id salt follows `_disposal`'s `f"{kind}:{seat}:{a.id}"` (`:384`).
   - The object is the revoking seat, `Act.via`: *"`ban` (person -> the excluding seat)"*
     (`rosters.yaml:115-123`).

**What it names.** The closed hold earns `tenure.closed` and the ban earns `tenure.opened`, each named
explicitly, on `_eff_release`'s narrowing precedent (`loop/effects_governance.py:297`). `_closing`'s
`earns=None` would let the closure earn every kind the row declares, and that is wrong once the row
declares two.

**No disposal on the actor himself.** A self-revocation's closure is `T-m`, not `T-o`
(`state/gate.py`, `T-m` before `T-o`). `T-m` never admits an owner opening his own restraint (the
`COR4` comment, `state/gate.py:1009-1019`). So a self-ban would be refused, the whole write put back, and
the resignation lost with it. A man stripping his own seat resigns; resignation writes no cost
(§2.7).

**A revoked man already banned gets no second ban.** One live ban suffices for every reader, which
asks `any(...)`. The name is a no-op guard, not a refusal: the hold still closes.

### 2.5 The write gate: `T-o` admits the ban only by a licence

The ban's object is a seat, but its kind is not in `SEAT_KINDS`. So in `tenure_write_basis`, `seat`
is `None` (`state/gate.py:977`), and the function returns `None` before `T-o` is reached. The arm goes
before `if seat is None` (`state/gate.py:1076`), beside `warrant`.

**The licence is computed in `refuse_unauthored` and is not read off the world.** The `handover`
docstring gives the reason (`state/gate.py:960-970`): this function sees one Tenure, and
*"`until == w.tick` cannot tell this write's closure from an earlier write's in the same tick"*. So it
is built in four steps:
- `refuse_unauthored`'s first pass already has every verdict (`:1139`).
- It collects `revoked = Counter(was.subject for each closure judged T_O whose was.kind == "hold" and
  REVOCATION_DISPOSAL.get(w.offices[was.object].conferral) == BAN_KIND)`, beside `released`
  (`:1140`). It uses `.get`, so a hand-mutated conferral grants no licence and does not raise inside
  the gate.
- It passes that to the second pass as a new keyword, `revoked: frozenset = frozenset()`. It is empty
  by default, so every other caller is unchanged, as `born` was.
- The arm is `opened and t.kind == BAN_KIND and t.object == via and owner in revoked` → `T_O`. One
  unit of the licence is spent per ban, as `handover` spends `released`.

**Basis name: `T-o`, not a twelfth basis.**

[ASSUMPTION; medium; Jordan to correct; revert: a named basis `revocation` with its line in
`not_yours`' `needs=` text.]

- The authority is the one `T-o` already judged on the closure in the same write: `may_revoke`
  through `via`.
- A new name for it would be a second word for one authority (ED-IN-0179).
- `not_yours`' `needs=` text (`state/gate.py:1159`) gains half a sentence on `T-o`'s disposal arm.

**What the gate then refuses:**
- a ban with no revocation in the same write;
- a ban on any seat other than `via`;
- a ban after an `elected`, `annex` or `None` revocation;
- two bans for one revocation.

The gate enforces the mapping. The effect's discipline is not what holds it.

### 2.6 `_req_revoke`: provenance unreadable means refuse

On the ordinary path only, after IN-48's delegate branch returns (`loop/predicates.py:453-458`) and
before the `may_revoke` clause, add `if off.conferral not in REVOCATION_DISPOSAL: return False`. The
act emits `revoke.refused`.
- Today this is reachable only by hand-mutating `Office.conferral` past `Office.__post_init__`'s
  refusal, which is `harness/probes.py:1513`'s pattern.
- That is the brief's second falsifier: refuse, not default.

The delegate branch (`:453-458`) does not ask it. A `delegate` edge's provenance is its kind, and its
outcome is fixed by IN-48.

### 2.7 What is NOT a revocation, and so writes no cost

| ending | basis | cost |
|---|---|---|
| a termed hold matures at MATTER (IN-10 (b), regency by term) | `T-n`, actor `None` | none |
| `release` of one's own hold (resignation) | `T-m` | none |
| `confer` onto a held seat closes the incumbent's hold | `T-o` inside `confer`'s write | **none** (§6, alternative 5) |
| the holder's death | `cascade` | none |
| the holder's `revoke` of his own seat | `T-m` | none (§2.4) |

**The `confer` row is a choice.** `confer` closing an incumbent is a displacement. Charging it would
put a second cost site on a second verb. The licence (§2.5) is computed from `T-o` closures in any
write, so `confer`'s write would ALSO carry a licence. It is never spent, because `_eff_confer` opens
no ban.

[ASSUMPTION; medium; Jordan to correct; revert: `_eff_confer`'s ordinary branch also opens the ban
for an `appointed` incumbent it displaces, using the same mapping and licence.]

---

## 3. Interactions

### 3.1 IN-48's delegate edge: no collision

- **Branch order.** `_req_revoke` (`loop/predicates.py:453-458`) and `_eff_revoke`
  (`loop/effects_governance.py:321-324`) return from the `office == via` + `to` branch before the
  ordinary path. So `REVOCATION_DISPOSAL` is never consulted for a delegation, and a dismissed delegate
  is not banned. That branch is the `delegate` row of §0's table, unchanged.
- **Gate placement.** The new ban arm sits before `if seat is None` (`state/gate.py:1076`). IN-48's
  `DELEGATE_KIND` block sits after it (`:1078-1093`). The kinds are disjoint, so neither arm can
  admit the other's edge.
- **Revoking a principal who has delegates.** His `hold` closes; if his seat is `appointed`, he is
  banned. His delegates' edges stay live and go dormant (IN-48 §2.5: `seat_hold` reads a `delegate`
  only while the seat has a live `hold`). Nothing in this design closes or bans them.
- **A delegate who exercises a seat granting `revoke`.** IN-48 §2.7 lets him strip other seats in the
  delegated seat's purview, because `may_revoke` asks `seat_hold`, which admits him. The ban's object
  is `Act.via`, the delegated seat: the seat excludes the man, whoever exercises it. The licence is
  computed from the `T-o` verdict, which already judged the delegate's authority, so no new rule is
  needed.
- **Residue R1: a banned man's existing seats.** Only an opening checks a ban:
  - `_req_confer`'s delegation branch refuses to OPEN a delegation for a banned man
    (`loop/predicates.py:137`);
  - `confer` declines to seat one (`loop/effects_governance.py:128`).

  Neither `seat_hold` nor anything else closes his other live `hold`s or `delegate` edges. SC-03a's
  determination ban leaves them live too. A ban bars FUTURE seating and service; it does not cascade.
  Widening `seat_hold` to refuse a banned delegate is IN-48's surface and is not done here.

### 3.2 IN-10's `Tenure.term` (regency by term)

- **A termed hold maturing at MATTER** is closed under `T-n`, with actor `None`
  (`state/gate.py:1042-1044`). It is not a `revoke` and writes no cost (§2.7).
- **A termed hold revoked early** reads the seat's conferral like any other hold; the term does not
  change its provenance. A regent seated by term on an `appointed` seat and stripped before term is
  banned. A regent on an `elected` seat is not.
- **A termed regent who DISPLACES the principal** (`_eff_confer`'s ordinary branch, IN-10 (b)) closes
  the principal's hold inside `confer`. That is not a revocation either (§2.7).

---

## 4. Hash, and the measurement

**Schema: no move.** No dataclass field changes (`state/carriers.py`, `Tenure` and `Office`). A
`Tenure.provenance` field would move every world's digest, because *"`repr(Tenure)` FOLDS INTO
`World.content_hash` AND CARRIES EVERY FIELD NAME"* (the comment on `Tenure.term`). That cost is part
of why it is rejected (§6).

**Build: no move.** No builder opens a `ban`, and every widened reader reads nothing new in a world
holding none. Measured: `populated.build_realm(0).content_hash()` begins `11989dcf` at this HEAD,
which is IN-48's recorded `BASE_HASHES[0]` prefix.

**Computed outcomes: none can move**, because a computed `revoke` is not driven (H-207 ruling (A)). The
probe is below.

**The probe at HEAD `40926a95`.** A scratch script imported the harness and the gate. It changed
nothing in the tree.

At `build_realm(0)`, 30 offices, 30 live seat-holds:

| conferral | held | declare a revocation basis | revocable by some sitting holder (`may_revoke` over every live `(holder, seat)` pair) |
|---|---|---|---|
| `appointed` | 15 | 8 | **6** |
| `elected` | 8 | 6 | 0 |
| `None` | 7 | 1 (Hafenmark) | 0 |
| `annex` | 0 | — | — |

So at build only `appointed` seats can be revoked: H-207's six Crown T1 seats. A computed run could
show only one provenance even if revocation were driven.

**The control for the EXIT world.** A build-placed `hold : p_npc_020 (King) → duchy_varfell` makes
`off_npc_052` (Duke of Varfell, `elected`, `rung_above_in_holdings`) revocable by the King through
`off_npc_020`: `may_revoke` False before the placement, True after. The same placement on
`duchy_hafenmark` does the same for `off_npc_050` (`None`). This is Jordan's 2026-10-12 *"a flag as to
whether that office is in the holdings of the monarch"*, set by hand.

**Computed play, measured.** `aperture.instrumented_season(build_realm(0), 4)`, the chooser watched
but not steered: 2900 acts. `revoke` was formed by 6 persons and attempted 11 times. **It executed 0
times.**

So "not driven" means that no motive scores a `revoke`, not that none is ever formed. It is formed and
attempted, and it is refused every time.

**Why the design cannot move these refusals:**
- The new `_req_revoke` clause answers True for every rostered conferral and for `None`.
- `revoke` has one refusal kind (`revoke.refused`, `verb_table.yaml:872`).

So each of the 11 refusals stays the same Event. Nothing executes, so nothing is banned.

**Only seed 0 was measured.** A run takes about 19 minutes here; seed 1 was not run. The build's
test 11 is the instrument that must be re-run, together with a seeded-run hash comparison against the
pre-build HEAD on the golden seeds.

**When H-207's design-first motive makes a computed `revoke` execute,** the ban moves outcomes. That
is a declared consequence of this design, not a defect.

---

## 5. Falsifiers the build must add

All go in `engine/season/tests/test_in31_revocation_cost.py`. Each must be seen red before the clause
that turns it green is written. Reuse `test_in48_delegation.py`'s `_fold` and `_gate_open` shape
(`:74-112`) and `test_g3_not_yours._gov_world`.

1. **The plan's falsifier.** Two hand-built revocations through the fold, by one revoker, of an
   `appointed` seat and of an `elected` seat. The first leaves a live `ban : holder → via`. The second
   leaves none. The two outcomes are asserted unequal on the set of `(kind, subject, object)` opened.
   If every revocation writes the same thing, the test fails.
2. **Provenance unreadable means refuse.** Hand-mutate `w.offices[x].conferral = "purchased"`, past
   `__post_init__`, on `probes.py:1513`'s pattern. The revoke emits `revoke.refused`, the hold stays
   live, and no ban opens. **Control:** the same seat restored to `appointed` is revoked.
3. **Import totality.** Monkeypatch `REVOCATION_DISPOSAL` to drop `elected`, and re-running the
   module's check raises `Unspecified`. A value outside `RESTRAINT_KINDS | {None}` raises too.
4. **The gate enforces the mapping.** With bare `w.write`s, the shape of `_gate_open`:
   - a `ban` opened by the revoker on `via` with no revocation in the same write → `NotYours`;
   - a `ban` beside the closure of an `elected` hold → `NotYours`;
   - a `ban` on a seat other than `via` → `NotYours`;
   - two bans for one revocation → the second `NotYours`.

   **Control:** the closure and one ban in one write are admitted, both under `T-o`.
5. **The ban bites through existing readers.** After an `appointed` revocation, the banned man's
   `confer` onto a vacant seat returns `NO_CHANGE` (`confer.refused`), and his `oblige` is refused at
   `_req_oblige` clause 5. **Control:** after an `elected` revocation the same two acts are admitted.
6. **No self-ban.** A holder of both `via` and the target seat revokes the target. The hold closes
   under `T-m` and no ban opens; the act is not refused.
7. **No second ban.** An already-banned holder revoked again has his hold closed and holds exactly one
   live ban.
8. **IN-48 unchanged.** A dismissal (`office == via` + `to`) of a delegate opens no ban, whatever the
   seat's conferral, including on an `appointed` seat. The principal's `appointed` revocation leaves
   his delegate's edge live (dormant) and unbanned.
9. **Not a revocation, no cost.** A termed hold maturing at MATTER, a `release` of one's own hold, and
   a `confer` displacing an `appointed` incumbent each open no ban.
10. **Derived openers.** `_verbs`' derived opener set for `ban` is `{"determine", "revoke"}`.
11. **The EXIT.** `build_realm(0)` plus one build-placed `hold : p_npc_020 → duchy_varfell` (the
    measured control, §4). The King revokes, by hand-built acts through the fold:
    - `off_lord_steward` (`appointed`): the hold closes and `ban : p_npc_009 → off_npc_020` opens;
    - `off_npc_052` (`elected`): the hold closes and no ban opens.

    The test asserts:
    - `restrained(w, "p_npc_009", BAN_KIND)` is True;
    - `restrained(w, "p_npc_052", BAN_KIND)` is False;
    - the two acts' opened-edge sets differ.

    Two controls:
    - without the placement, the second revoke emits `revoke.refused`, so the EXIT world is what makes
      the second provenance reachable;
    - with `REVOCATION_DISPOSAL` monkeypatched to all `None`, the two outcomes are equal and assertion
      three fails. That is the plan's falsifier observed live.

    H-100 is closed on this test, with R1-R3 (§8) in its cite.

---

## 6. Alternatives rejected

1. **A new `Tenure.provenance` field, stamped at opening.**
   - It is a schema move: the `repr` comment on `Tenure.term` in `state/carriers.py`.
   - It is a second home for a fact. `state/carriers.py:84-93` deleted `Tenure.conferrer` on exactly
     that ground: *"WHAT CONFERRED a Tenure is the opening Act ... A field here would be a second home
     for a fact the act already holds — `ID-2`"*.
   - Every builder (`harness/populated.py:1057`, `:1114`) would have to stamp it, and would only copy
     `Office.conferral` into it.
2. **A payload key stamped by `World._grant_remit`, on `seat_rung`'s precedent** (`Tenure.seat_rung`,
   `state/carriers.py`).
   - No schema move, but every office hold's payload `repr` changes, so the build hash moves by value.
   - It buys nothing: `conferral` is immutable by act (`loop/predicates.py:296-300`), and `establish`
     re-stamps every sitting holder anyway.
3. **Reading the opening act off the log.**
   - Build-placed holds have no opening act: builders write outside the gate (the `founding` comment,
     `state/gate.py:1022-1030`). So provenance would be unreadable for all 30 holds at build. That
     forces either refusing every ruled `T-o` revocation or defaulting, which the brief's falsifier
     forbids.
   - It would discriminate nothing anyway: `confer` fills all three bases today (*"NOTHING
     DISCRIMINATES BETWEEN THE THREE YET"*, `rosters.yaml:1858-1862`), so the act would read `confer`
     for every seat.
4. **Writing `standing`.** `standing_of` is computed when read, as the gap between `told_by` and
   `firsthand` claims about oneself (`decision/options.py:1118-1140`). There is no field. Writing it
   means minting claims into the revoked man's ledger that no witness made.
5. **Writing `regard` through a stance row.**
   - The precedent exists: field battle appends `(faction, -1.0, grudge_w)` rows
     (`loop/effects_combat.py:250-261`), and `(Person, stance)` has a write-matrix row
     (`write_matrix.yaml:220-226`).
   - It would need a new fixture. Reusing `field_grudge_weight` would be two decisions on one fixture
     (H-121, quoted in `regard`'s docstring, `queries/person_q.py:131-135`). It would also need
     `revoke.writes += Person.stance`.
   - A grudge is the revoked man's feeling, not what the world does to him. It does not change whether
     losing a seat is survivable, which is the question H-100's `unblocks:` names.

   Declined, not foreclosed: it can be added beside the ban later.
6. **Grading by `Tenure.degree`.** `revoke` is uncontested, and an uncontested act carries no degree
   (H-162's `unproduced:` note, `write_matrix.yaml:353`).
7. **`detain` for some provenance.** A detention opens only by `warrant` or a bench
   (`state/gate.py:1055-1075`). Custody without a bench is a sentence without proceedings, and the
   candidate it would fit, `annex`, has no seat.
8. **A YAML column for the mapping:** §2.2. **A twelfth gate basis:** §2.5. **A cost on `confer`'s
   displacement:** §2.7.

---

## 7. EDITS for the build (B-Q, after IN-26)

`state/gate.py`
- `REVOCATION_DISPOSAL` and its import-time totality check, beside `REVOCATION_RULES` (`:537-547`).
  Import `BAN_KIND` from `data/rosters.py`, beside `DETAIN_KIND` (`:52`).
- `tenure_write_basis`:
  - a keyword `revoked: frozenset = frozenset()`;
  - the ban arm before `if seat is None` (`:1076`), returning `T_O`;
  - the docstring's basis list, adding `T-o`'s disposal arm.
- `refuse_unauthored`:
  - the `revoked` Counter beside `released` (`:1140`);
  - the second-pass condition `+released or +revoked` (`:1145`);
  - one licence unit spent per ban admitted;
  - the docstring's pass description.
- `not_yours`' `needs=` text (`:1159`).

`loop/effects_governance.py`
- `_eff_revoke`'s ordinary branch (§2.4): the mapping read, the literal `"ban"` construction, the
  per-subject `earns`, and the `NO_CHANGE` backstop. Import `BAN_KIND` and `restrained` (both already
  imported, `:19`) and `REVOCATION_DISPOSAL`.
- The docstring.

`loop/predicates.py`
- `_req_revoke`: the `off.conferral not in REVOCATION_DISPOSAL` refusal on the ordinary path (§2.6),
  and the docstring.

`verb_table.yaml`, the `revoke` row (`:862-877`)
- `writes: ["Tenure.until", "Tenure.since"]`, as `determine` declares the disposal it opens (`:249`).
- `emits: ["tenure.closed", "tenure.opened"]`.
- A `disposal_note` naming the mapping's owner and §2.7's non-revocations.
- `requires:` gains *"and the seat's conferral basis has a revocation disposal"*.

`rosters.yaml`
- The `tenure_kinds` note: `ban`'s openers are now `determine` and `revoke`.

`hole_register.yaml`
- H-100 closed when test 11 passes, with R1-R3 in its cite.

`engine/season/tests/test_in31_revocation_cost.py`: §5.

**Not edited:**
- `state/carriers.py` (no field).
- `offices.yaml` (no data edit).
- `queries/world_q.py::restrained` (read as it is).
- `decision/` (nothing computed forms a `revoke` with a different shape).
- `data/verbs.py`: its opener derivation picks up the literal. One check for the build: confirm that
  `emits` gaining `tenure.opened` passes the loader's emits checks for a `binding_decision` row. `confer`
  is a `binding_decision` row emitting both kinds (`verb_table.yaml:166`, `:178`), so precedent says
  it does.

---

## 8. Assumptions, residues, and what survives the ladder

Each assumption is [medium; Jordan to correct] and marked inline:
- **A1. `appointed` → `ban`; `elected`, `annex` and `None` → nothing** (§2.3). Revert: all `None`.
- **A2. The ban is admitted under `T-o`, not a twelfth basis** (§2.5). Revert: basis `revocation`.
- **A3. `confer`'s displacement of an incumbent costs nothing** (§2.7). Revert: `_eff_confer` opens
  the same ban.
- **A4. `conferral: None` reads as a value (heredity, by the `offices.yaml` header), not as
  "unreadable"** (§1). Revert: refuse a revocation of a `None` seat. That would overwrite the
  2026-10-12 Hafenmark ruling, so the revert itself needs Jordan.

Named residues:
- **R1.** A ban does not close the banned man's other live seats or delegations (§3.1).
- **R2.** `annex` has no seat, so its outcome is declared and unobserved.
- **R3.** Provenance is the SEAT's basis, not the seating act's. A person `confer`red onto an `elected`
  seat reads `elected`. This closes when the `13d-i` open question (should `confer` narrow to
  `appointed`?) is ruled. It narrows at `may_fill` (`state/gate.py`, `may_fill`'s *"WHAT IT DOES NOT
  DECIDE"*), after which seat and act agree by construction.

**What survives all five ladder steps, for the orchestrator to put to Jordan:** **A1 only.** It is a
live design choice in which defensible options produce materially different games: whether losing an
appointed seat is survivable, and whether elected or hereditary seats carry any cost at all. Steps 1-4
are silent on it:
- the research is tier 3;
- ED-IN-0256 rules how a seat is filled, not what losing it costs.

Step 5 picks the ban as the one disposal with existing readers. Everything else above is decided by
precedent or architecture and is not a question.
