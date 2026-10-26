# IN-31: what a revocation costs, and where a seat's provenance lives

## Status: PROPOSED (2026-10-14) · design only · reference under `CLAUDE.md` §0.05 · BUILT as of 2026-10-26: IN-31's revocation cost by the seat's provenance landed in `d16bd895` (B-Q) ("builds nothing" was the state at drafting); the IN-48 `delegate` passages stay conditional on a delegation carrier, and IN-48 is unbuilt (`workplans/valoria_master_workplan_v10_part5.md` IN-48).
## Position: IN-31 (H-100), `workplans/valoria_master_workplan_v9_part5.md` `### IN-31` · Lane: IN (SE) · IDs: none allocated
## ⚠ Measured at HEAD `40926a95`, where IN-48's `delegate` carrier was built. THAT BUILD WAS REVERTED at the B-J close (it contradicts ratified Layer 1; `proposals/2026-10-14-in48-delegation-carrier.md` §9). Every passage below that names IN-48's `delegate` edge or dismissal branch (§0 table row, §2.4, §3.1, falsifier 8, §7's IN-48 edit) is CONDITIONAL on a delegation carrier surviving, and says nothing until one does; the provenance reading and the appointed/elected/None dispositions do not depend on it. ALSO CONDITIONAL OR STALE for the B-Q builder: §2.6's instruction anchored to the deleted `loop/predicates.py` delegate branch; every use of `test_in48_delegation.py`'s `_fold` and `_gate_open` (that file was deleted by the revert; write the helpers afresh); and the line cites taken from the reverted tree (`effects_governance.py:128` is now `:105`, `predicates.py:414` is now `:397`; re-open each before building). ONE INTERACTION THE REDESIGN MUST SETTLE: on Layer 1's route a regent is an ordinary `hold` on a second seat, so a revocation of an `appointed` regent would carry this design's ban (A1); whether a regent is exempt is part of IN-48's redesign, not decided here.
## Measured at HEAD `40926a95` (B-J; IN-48 built). A path with no top-level directory is under `engine/season/`.
## Revised 2026-10-14 for an independent critic's twelve findings. The orchestrator took the decisions marked ORCH (ladder steps 4-5); where one is new it is marked [ASSUMPTION; medium; Jordan to correct], with its revert.

The brief is the IN-31 entry: WHAT, DEPS, EDITS, EXIT and FALSIFIER. This document does not restate it.

---

## 0. Verdict

> **Passages that name IN-48's `delegate` edge are CONDITIONAL: that carrier was built and reverted (see the banner above and `proposals/2026-10-14-in48-delegation-carrier.md` §9).**

**The provenance carrier already exists. It is `Office.conferral` for a `hold`, and `Tenure.kind` for
a `delegate` edge. No field is added, so the Tenure schema does not move.**

- A `hold`'s provenance is the SEAT's declared conferral basis: `appointed`, `elected`, `annex`, or
  `None`. That roster is Jordan's ED-IN-0256 ruling (2), *"HOW A SEAT IS FILLED"*
  (`rosters.yaml:1845-1863`). No act can change it on a live seat: `_req_establish` refuses a
  `conferral` difference on an existing id (`loop/predicates.py:296-300`). So reading it at revoke time
  gives the same answer a stamp taken at seating would.
- ⚠ **It is the seat's basis, not the route by which this man came to sit** (R3, §8). That limit is
  live: the one computed seating that executes is a self-`confer` onto an `elected` seat.
- A `delegate` edge's provenance is its kind. IN-48 already gives its dismissal its own branch
  (`loop/effects_governance.py:318-324`).

**What `revoke` writes, per provenance:**

| provenance | `revoke` closes | `revoke` also writes on the person revoked | event emitted |
|---|---|---|---|
| `appointed` | his `hold` | a **permanent** `ban : him → Act.via` (the revoking seat) | `tenure.closed` |
| `elected`, `annex`, `None` | his `hold` | nothing | `tenure.closed` |
| `delegate` (IN-48 branch) | his `delegate` edge | nothing | `tenure.closed` |

- **The `ban` is SC-03a's existing restraint, and its existing readers make it bite:**
  - `confer` declines to seat a banned conferee (`loop/effects_governance.py:128`);
  - `_req_confer` refuses to open a delegation for one (`loop/predicates.py:137`);
  - `oblige` refuses him service (`loop/predicates.py:414`).
- **No new reader is built.**
- **No effect in `loop/` closes a ban.** Only his death ends it (§2.3).
- **`revoke`'s `emits` stays `[tenure.closed]`** (ORCH, finding 2). The ban is an edge the revoke
  opens that earns no event of its own. That is `determine`'s precedent: it opens its disposal
  emitting only `matter.determined` (`verb_table.yaml:249-251`).

**The mapping has one owner:** `REVOCATION_DISPOSAL` in `state/gate.py`, beside `REVOCATION_RULES`.
- The import refuses a mapping that is not total over `CONFERRAL_BASES ∪ {None}`.
- A conferral outside the mapping makes the precondition REFUSE, never default. Only a hand-mutation
  can reach that, because `Office.__post_init__` refuses an off-roster value.

**The write gate admits the `ban` under `T-o` through a same-write licence.** The licence is computed
in `refuse_unauthored`'s first pass, which is `handover`'s two-pass shape (`state/gate.py:1139-1150`,
`:1045`). The gate enforces the mapping only for a revoking seat that does not judge: a judging seat's
`determination` arm admits a ban on its own authority (§2.5).

**A computed `revoke` executes 0 times** (H-207 ruling (A), `hole_register.yaml:4451`; measured in §4).
- At build, only `appointed` seats can be revoked by anyone.
- So the EXIT cannot be a corpus run. It is a seeded test with one hand-built `revoke` per seat
  provenance, and the build amends IN-31's EXIT to say so (ORCH, §7).

### What only Jordan can answer: A1

**What does losing a seat cost, by provenance and by the verb that removes the holder?**

This design takes one answer [ASSUMPTION; medium; Jordan to correct; revert: every
`REVOCATION_DISPOSAL` value `None`]:
- `appointed` → a ban;
- `elected`, `annex`, `None` → nothing;
- a `confer` that displaces an incumbent → nothing (former A3, folded in);
- the ban is irreversible: nothing but death ends it.

Everything else in this document is answered by precedent or by the architecture.

---

## 1. The six ways, read against the code

The H-100 row says the corpus holds seats six different ways (`hole_register.yaml:1925-1960`). Its cite
names the research vocabulary (bureaucratic, kinship, military, ideological, patronage, purchased) and
records that a `power_bases` roster built from it was DELETED because nothing read it. The brief's six
are a different list:

| way | carrier in code today | reachable at `build_realm(0)` |
|---|---|---|
| appointed | `Office.conferral == "appointed"` (ED-IN-0256 (2)) | 15 held seats; **6 can be revoked by a sitting holder** |
| elected | `Office.conferral == "elected"` | 8 held; 6 declare a revocation basis; 0 can be revoked at build |
| annexed | `Office.conferral == "annex"` | **0 seats declare it** |
| inherited | none: some `conferral: null` seats, by the header note in `offices.yaml` (`:43-50`) | part of the 7 `None` holds, see below |
| imposed | none. `Tenure.imposed` marks a sentenced `oblige`, which is not a seat, and no act seats a person by force | — |
| delegated | `Tenure.kind == "delegate"` (IN-48) | built per test only |

The figures come from the §4 probe.

**The ladder applied to the two with no carrier** (`CLAUDE.md` §0, steps 2 and 4):
- **imposed**: irrelevant. No act or edge seats a person by imposition.
- **inherited**: precedent. The H-100 row records that a roster with no reader was deleted, so nothing
  is minted. Heirship belongs to the unbuilt `succeed` kind (`offices.yaml:43-50`).

### `None` mixes three provenances, and is still a value (finding 7)

The 7 held `None` seats are not one way of holding:
- **Heredity, by a judgment call.** The header's translation note leaves the `succeed` seats `null`
  (King, Queen, Heir, Princess, Duke of Valorsmark; `offices.yaml:43-50`) and itself flags that as *"a
  JUDGMENT CALL flagged for attack"*.
- **Hafenmark, unexplained.** The Duchess's seat is `conferral: null` (`offices.yaml:214`), but it is
  NOT in the header's list, and no note says why. It is the one `None` seat that declares a
  revocation basis (`rung_above_in_holdings`, `:215`).
- **Nothing authored.** `off_npc_084` (guild leader) is `None` only because no `offices.yaml` row
  authors it. The builder's declared exception passes `(_off_row or {}).get("conferral")`, which is
  `None` (`harness/populated.py:1047-1057`).

**Why `None` is still read as a VALUE and not as "unreadable":**
- `Office.conferral` is optional by declaration (`state/carriers.py`: `if self.conferral is not None:
  require_member(...)`, quoted at `offices.yaml:48-49`).
- Jordan ruled Hafenmark strippable on 2026-10-12 (`offices.yaml:215`; the H-207 cite,
  `hole_register.yaml:4451`). Refusing every `None` revocation would overwrite that ruling.
- So `None` reads as *"this seat declares no ruled way of being filled"* and costs what the mapping
  says. It does NOT read as heredity: §2.3's reason for `None` → nothing does not rest on it.

**"Unreadable" therefore has one reachable meaning:** a `conferral` outside the roster. Since
`Office.__post_init__` refuses such a value, only a hand-mutation can produce it
(`harness/probes.py:1513`'s pattern). The refusal in §2.6 is a backstop with a falsifier (test 2),
not a path a built world takes.

---

## 2. The design

### 2.1 The carrier: read, not stamped

**`seat_provenance(off)` is NOT built.**
- The provenance of a `hold` is `off.conferral`, read where it is needed. A one-line accessor over
  one field is overhead (§0.06 E).
- The single owner is the mapping below.

**Why reading at revoke time is exact:** `Office.conferral` has no act-side writer.
- `_req_establish` refuses a re-founding that changes it (`loop/predicates.py:296-300`).
- The other assignments are builders (`harness/populated.py:1057`, `:1114`) and one probe's
  hand-mutation (`harness/probes.py:1513`).

### 2.2 The owner: `REVOCATION_DISPOSAL` in `state/gate.py`

```
REVOCATION_DISPOSAL = {"appointed": BAN_KIND, "elected": None, "annex": None, None: None}
```

It sits beside `REVOCATION_RULES` (`state/gate.py:537-547`) and copies that dict's import-time refusal:
- keys `!= set(CONFERRAL_BASES) | {None}` → `Unspecified`;
- a value outside `RESTRAINT_KINDS | {None}` → `Unspecified`.

So a fourth basis cannot be added without an outcome (`conferral_bases` is `open: false`,
`rosters.yaml:1847`).

**Why Python and not a YAML column:**
- The precedent is `REVOCATION_RULES`. Its roster's note says the roster *"NAMES THE BASIS AND NOTHING
  ELSE ... The rule is BEHAVIOUR and lives in `state/gate.py`"* (the `revocation_bases` note in
  `rosters.yaml`).
- A dict hung on `conferral_bases` would give one roster a second shape.
- `arrangements.yaml`'s `disposes:` is a per-ROW column, and here the key is a roster value, not a row.

**Every reader asks the dict in place, as `gate.REVOCATION_DISPOSAL` or through a function in
`state/gate.py`.**
- A `from ..state.gate import REVOCATION_DISPOSAL` in `loop/` would bind a reference to the dict.
- A test that monkeypatches the module attribute would then miss that binding: the stale-binding
  hazard `align`'s docstring names (`data/verbs.py:1342-1346`).
- Tests mutate it with `monkeypatch.setitem`, in place (§5, tests 3 and 11).

### 2.3 Why `appointed` gets a permanent ban, and the others nothing (A1)

This is ladder step 5. Its marker is in the box at the end of §0.

- **The reason.** An appointed seat is filled by a superior's choice; the `offices.yaml` header's
  gloss is *"`confer` (a superior names the holder) -> `appointed`"* (`:41`). Its revocation is that
  favour withdrawn. The H-100 research reads favour-derived seats as facing *"total ruin"* and
  kinship-derived seats as getting *"containment"*. It is tier 3: vocabulary, not authority.
- **What makes the ban mean ruin is code.** `restrained(w, p, BAN_KIND)` reads a ban on ANY seat
  (`queries/world_q.py:1019`, itself an [ASSUMPTION; medium] there). So he is never again:
  - seated as a conferee (`loop/effects_governance.py:119`, `:128`);
  - delegated a seat (`loop/predicates.py:137`);
  - admitted to serve (`loop/predicates.py:414`).
- **The ban is PERMANENT (finding 5; corrects this section's earlier "only a bench closes it").**
  - It carries no term, on SC-03a's assumption for a sentence's ban
    (`loop/effects_information.py:378-383`).
  - Nothing in `loop/` closes one. Every `t.until = w.tick` site was opened:
    `loop/effects_governance.py:161` (confer) and `:336` (`_closing`); `loop/effects_information.py:524`
    (give) and `:548` (destroy_record, a Record's edges); `loop/effects_migration.py:101` and `:206`
    (contain, reside); `loop/matter.py:232` (term maturity; a ban has none).
  - The gate WOULD admit a bench's closure (`state/gate.py:1063-1067`), but no effect writes one: the
    gate's own note says *"no effect writes that closure yet"* (`:1072`), and `pardon` is unbuilt.
  - At build the only seat that can revoke anyone is `off_duke_valorsmark` (§4), and it grants no
    `determine` (`offices.yaml:200`). So even a future bench closure would need a different seat.
  - **Only the man's death (the `cascade`) ends it.**
- **Applying §6.7's own test honestly.** §6.7 rejects `detain` as *"a sentence without proceedings"*.
  A permanent ban opened by a revocation is also a sentence without proceedings. It differs from
  `detain` in degree, not kind: it bars, it does not hold. **This is the strongest objection to A1**
  and the reason the irreversibility is part of Jordan's question.
  - **Its revert** is a narrower outcome: every value `None`.
  - **The other revert** is a ban with a declared term: `_disposal`'s own revert line,
    `term=_new_oblige_term(w, a)`, `loop/effects_information.py:380`.
- **The `elected` row is the SEAT's basis, not the route (finding 6).** Writing nothing on an elected
  revocation reads *"his electors may return him"*. It holds only where an election seated him, and
  nothing models one: `confer` is the only act that fills any seat (`rosters.yaml:1859-1862`). The
  one computed seating that executes is a self-`confer` onto the `elected` `off_military_jarl`/
  `off_npc_082` (R3).
- **`annex` and `None` → nothing.** `annex` has no seat, so its outcome is declared and unobserved
  (R2).

**Why not grade by `Tenure.degree`, or write `standing` or `regard`?** §6.

### 2.4 The writes in `_eff_revoke`

**The IN-48 dismissal branch (`loop/effects_governance.py:321-324`)** gains one argument:
`_closing(w, [...], "tenure.closed")`.
- `earns=None` earns every kind the row declares (`loop/resolve.py:525`).
- With `emits` unchanged (ORCH, finding 2) that is still `tenure.closed`, so behaviour does not move.
- The explicit kind pins the outcome that `test_in48_delegation.py:181` asserts
  (`kinds == ["tenure.closed"]`) against any later `emits` widening. Test 8 (§5) falsifies it.

**The ordinary branch (`:325`)** becomes:
1. **`closed`**: the live `hold`s on `obj`, as today. There is at most one.
2. **`off.conferral not in gate.REVOCATION_DISPOSAL` → `NO_CHANGE`.** This backstops `_req_revoke`
   (§2.6), in the shape of `_eff_confer`'s `:120-121`.
3. **When the mapping gives `BAN_KIND`**, for each closed hold whose subject `h` is not `a.actor`,
   not already `restrained(w, h, BAN_KIND)`, and still in `w.persons`: build
   `Tenure(H(w.world_seed, w.tick, h, f"ban:{a.via}:{a.id}"), h, a.via, "ban", w.tick)`.
   - The kind is spelled LITERALLY, so `_derive_openers_from_effects` derives `ban`'s openers as
     `{determine, revoke}` (`_disposal`'s precedent, `loop/effects_information.py:372-376`).
   - The id salt follows `:384`.
   - The object is the revoking seat: *"`ban` (person -> the excluding seat)"*
     (`rosters.yaml:115-123`).

**What it names.** The closure and the ban are each `Subject.edge(t)` with `earns=None`, `determine`'s
shape (`Subject.edge(nt)`, `loop/effects_information.py:368`).
- Both earn the row's one kind, so an appointed revocation emits `["tenure.closed"]`, exactly as an
  elected one does.
- **The ban is not witnessed as its own event.** Witnesses see a closure.
- Its readers consult the edge, not the log. It is visible to `restrained` the moment it opens.

**No disposal on the actor himself.** A self-revocation's closure is `T-m` (checked before `T-o`).
`T-m` never admits an owner opening his own restraint (`COR4`, `state/gate.py:1009-1019`). So a
self-ban would be refused, the write put back, and the resignation lost.

**A revoked man already banned gets no second ban.** The hold still closes.

### 2.5 The write gate: `T-o` admits the ban by a licence

**Where the arm goes.** In `tenure_write_basis`, the ban's `seat` is `None` (`state/gate.py:977`:
`ban` is not in `SEAT_KINDS`). So the arm goes before `if seat is None` (`:1076`), beside `warrant`.

**Why the licence is computed in `refuse_unauthored`.** The function judges one Tenure, and
*"`until == w.tick` cannot tell this write's closure from an earlier write's in the same tick"*
(`:960-962`). So:
- the first pass collects
  `revoked = Counter(was.subject for each closure judged T_O with was.kind == "hold" and
  REVOCATION_DISPOSAL.get(w.offices[was.object].conferral) == BAN_KIND)`, beside `released` (`:1140`).
  It uses `.get`, so a hand-mutated conferral grants no licence and does not raise in the gate;
- the second pass runs when `+released or +revoked` (`:1145`) and passes `revoked` as a new keyword,
  empty by default;
- the arm is `opened and t.kind == BAN_KIND and t.object == via and owner in revoked` → `T_O`. One unit
  of the licence is spent per ban.

**Basis name: `T-o`, not a twelfth basis.**
[ASSUMPTION; medium; Jordan to correct; revert: a named basis `revocation`, with its line in
`not_yours`' `needs=` text, `:1159`.] The authority is the one `T-o` judged on the closure in the same
write; a second name for one authority is coinage (ED-IN-0179).

**What the gate enforces depends on the revoking seat (finding 4).**

The `determination` arm (`state/gate.py:1063-1067`) is checked BEFORE the new arm. It admits ANY
opened `DISPOSABLE_KINDS` edge (`ban` included) on `via` whenever `may_determine(actor, via, owner)`
holds. Its three conjuncts (`:688-710`):
- `via`'s grant carries `determine`;
- the owner is a person other than the actor;
- the bench sits over the owner's home.

**For a NON-JUDGING revoking seat, the gate enforces the mapping.** It refuses a ban that comes with no
revocation, a ban after an `elected`/`annex`/`None` revocation, a ban on another seat, and a second
ban.

**For a JUDGING revoking seat, it does not.** Measured on `build_realm(0)` (§4):
- `may_determine(p_npc_020, off_npc_020, p_npc_052)` is **True**. The EXIT's elected revocation runs
  through that seat, so a ban an erroneous effect opened there would be admitted under
  `determination`.
- `may_determine(p_npc_020, off_duke_valorsmark, p_npc_009)` is **False**, so the appointed
  revocation's ban can only enter by the licence.

**Recommendation: accept this. Add no conjunct.**
- The gate judges AUTHORITY, not route. Its signature carries the actor, `via`, `gone`, `born` and
  `released`, never the verb (`:810-813`).
- A judging seat already holds the authority to ban that man by a `determine` in the same season. The
  gate admitting the edge grants nothing the seat could not write another way.
- A conjunct keyed on the act's verb would widen the gate's judgment interface for one caller, which
  is shape divergence.
- So for a judging seat the mapping is held by its one owner, `_eff_revoke`, and by tests 1 and 4b.

### 2.6 `_req_revoke`: provenance unreadable means refuse

On the ordinary path, after IN-48's delegate branch returns (`loop/predicates.py:453-458`) and before
the `may_revoke` clause: `if off.conferral not in gate.REVOCATION_DISPOSAL: return False`. The act
emits `revoke.refused`.
- Reachable only by a hand-mutation past `Office.__post_init__` (§1).
- The delegate branch does not ask it.

### 2.7 What is NOT a revocation, and so writes no cost

| ending | basis | cost |
|---|---|---|
| a termed hold matures at MATTER (IN-10 (b)) | `T-n`, actor `None` | none |
| `release` of one's own hold | `T-m` | none |
| `confer` onto a held seat closes the incumbent's hold | `T-o` inside `confer`'s write | none: part of A1 |
| the holder's death | `cascade` | none |
| the holder's `revoke` of his own seat | `T-m` | none (§2.4) |

**On `confer`.** Its displacement of an incumbent produces a `T-o` closure, so its write carries a
licence too. The licence is never spent, because `_eff_confer` opens no ban. Charging the displacement
is the verb half of Jordan's A1 question: its answer would make `_eff_confer`'s ordinary branch open
the same ban through the same mapping and licence.

---

## 3. Interactions

### 3.1 IN-48's delegate edge

- **Branch order.** `_req_revoke` (`loop/predicates.py:453-458`) and `_eff_revoke`
  (`loop/effects_governance.py:321-324`) return from the `office == via` + `to` branch first. The
  mapping is never consulted for a delegation, and a dismissed delegate is not banned. The branch
  gains only the explicit `earns` (§2.4).
- **Gate placement.** The ban arm sits before `if seat is None` (`state/gate.py:1076`); IN-48's
  `DELEGATE_KIND` block sits after it (`:1078-1093`). The kinds are disjoint.
- **Revoking a principal who has delegates.** His hold closes, and he is banned if the seat is
  `appointed`. His delegates' edges stay live and go dormant (IN-48 §2.5).
- **A delegate exercising a seat that grants `revoke`.** `may_revoke` admits him through `seat_hold`.
  The ban's object is `Act.via`, the delegated seat: the seat excludes, whoever exercises it.
- **Residue R1: a ban bars openings; it closes nothing.** Only openings check a ban (the three readers
  in §0). The banned man's other live `hold`s and `delegate` edges stay; so does SC-03a's
  determination ban. **Finding 12:** a delegate on seat `S` who also holds an `appointed` seat `X`,
  stripped of `X` through `S`, is banned on `S` and **keeps exercising `S`**. `seat_hold` reads no
  ban (`state/gate.py:304-319`). Refusing a banned delegate in `seat_hold` is IN-48's surface and is
  not done here.

### 3.2 IN-10's `Tenure.term`

- **A termed hold maturing at MATTER** closes under `T-n`, actor `None` (`state/gate.py:1042-1044`).
  That is not a revocation and writes no cost.
- **A termed hold revoked early** reads the seat's conferral. The term does not change provenance.
- **A termed regent displacing the principal** (`_eff_confer`'s ordinary branch) is a `confer`
  displacement (§2.7).

---

## 4. Hash, and the measurement

**Schema: no move.** No dataclass field changes (`state/carriers.py`).

**Build: no move.** No builder opens a `ban`. Measured: `build_realm(0).content_hash()` begins
`11989dcf` at this HEAD.

**Loader-derived tables: what moves and what does not (finding 2).**
- `revoke`'s `emits` and `emits_on_refusal` are unchanged. So `KIND_VERB`'s single-emitter derivation
  (`data/verbs.py:1205-1213`) is unchanged, and so is `align_kind` (`:1362-1374`).
- Had `tenure.opened` been added, it would have had two emitters. `KIND_VERB` would then have dropped
  it, unpricing every `confer` deed in `deeds_judged`, with `judged_gain` live
  (`queries/person_q.py:128-132`). That is why `emits` does not change.
- `writes` gains `Tenure.since`, `determine`'s precedent.
- `ban`'s derived openers gain `revoke`. Their one code reader outside the loader is
  `_DELEGATE_OPENERS` (`decision/options.py:46`), which reads `delegate` only.

**Computed play, measured.** `aperture.instrumented_season(build_realm(0), 4)`, the chooser watched,
not steered: 2900 acts. `revoke` was formed by 6 persons, attempted 11 times, and **executed 0
times**. "Not driven" (H-207 (A)) means that no motive scores it, not that it is never formed.

**What can be claimed:**
- Every one of those refusals reaches the new `_req_revoke` clause with a rostered conferral or `None`,
  so the clause answers True.
- `revoke` has one refusal kind (`verb_table.yaml:872`).
- So the precondition's answers and the refusal Events are unchanged by construction, and **no ban
  opens in computed play at seed 0 over 4 seasons**.
- **What is NOT claimed:** that no other seed or season count moves. That is unmeasured; one
  four-season run took about 19 minutes here.

**The instrument the build must run (ORCH, finding 2; not run now):**
- the 4-season seed-0 `content_hash` (`populated.run(4, 0)`), before and after the build, asserted
  equal;
- the `engine/tests/` goldens at the close.

A moved hash is a finding to explain, not a re-pin.

**At build, who can revoke whom:**

| conferral | held | declare a revocation basis | revocable by some sitting holder (`may_revoke` over every live `(holder, seat)` pair) |
|---|---|---|---|
| `appointed` | 15 | 8 | **6** |
| `elected` | 8 | 6 | 0 |
| `None` | 7 | 1 (Hafenmark) | 0 |
| `annex` | 0 | — | — |

**The revoking seat for the six (finding 3).**
- The six appointed T1 seats sit on `terr_T1`, whose parent rung is `duchy_valorsmark` (Crown T1 is
  contained in the Crown duchy, `harness/populated.py:519-525`, `:545`).
- `seated_on_the_rung_above_structure` checks the PARENT rung only (`state/gate.py:447-453`), so the
  seat above them is `off_duke_valorsmark` (`offices.yaml:195-206`, held by NPC-020), not the realm
  seat `off_npc_020`.
- Measured: `may_revoke(p_npc_020, "off_duke_valorsmark", off_lord_steward)` is **True** and
  `may_revoke(p_npc_020, "off_npc_020", off_lord_steward)` is **False**.

**The EXIT world's second provenance.**
- A build-placed `hold : p_npc_020 → duchy_varfell` makes `off_npc_052` (Duke of Varfell, `elected`,
  `rung_above_in_holdings`) revocable through `off_npc_020`: `may_revoke` False before, True after.
- The same placement on `duchy_hafenmark` does it for `off_npc_050` (`None`).
- This is Jordan's 2026-10-12 *"a flag as to whether that office is in the holdings of the monarch"*,
  set by hand.

---

## 5. Falsifiers the build must add

All go in `engine/season/tests/test_in31_revocation_cost.py`, each seen red before its clause is
written. Reuse `test_in48_delegation.py`'s `_fold` and `_gate_open` (`:74-112`) and
`test_g3_not_yours._gov_world`.

1. **The plan's falsifier.** One revoker, through a NON-judging seat, revokes an `appointed` seat and
   an `elected` seat by hand-built acts through the fold. The first leaves a live `ban : holder → via`;
   the second leaves none. The opened `(kind, subject, object)` sets are asserted unequal. Both acts
   emit exactly `["tenure.closed"]`.
2. **Provenance unreadable means refuse (a hand-mutation backstop).** Set
   `w.offices[x].conferral = "purchased"` past `__post_init__`, on `probes.py:1513`'s pattern. The act
   emits `revoke.refused`, the hold stays live, and no ban opens. **Control:** restored to
   `appointed`, it is revoked. The test's docstring says no built world reaches this (§1).
3. **Import totality.** `monkeypatch.setitem`/`delitem` on `gate.REVOCATION_DISPOSAL` (in place,
   §2.2), then re-run the module's check:
   - dropping `elected` raises `Unspecified`;
   - so does a value outside `RESTRAINT_KINDS | {None}`.
4. **The gate enforces the mapping where it can.**
   - **(a) NON-judging `via`**, bare `w.write`s in the shape of `_gate_open`: a ban with no revocation
     in the write, a ban beside an `elected` closure, a ban on another seat, and a second ban are each
     `NotYours`. **Control:** a closure plus one ban in one write is admitted, both under `T-o`.
   - **(b) Judging `via`** (its grant holds `determine`, its bench sits over the man's home): a ban
     beside an `elected` closure is ADMITTED, under `determination`. That pins §2.5's accepted scope;
     if a later conjunct closes it, the test is flipped deliberately.
5. **The ban bites through existing readers.** After an `appointed` revocation:
   - a `confer` naming the banned man as conferee (`to`) returns `NO_CHANGE` and emits `confer.refused`
     (`loop/effects_governance.py:119`, `:128`);
   - his `oblige` is refused at `_req_oblige` clause 5.

   **Control:** after an `elected` revocation, the same two acts are admitted.
6. **No self-ban.** A holder of both `via` and the target revokes the target. The hold closes under
   `T-m`, no ban opens, and the act is not refused.
7. **No second ban.** An already-banned holder, revoked again, has his hold closed and holds exactly
   one live ban.
8. **IN-48 unchanged, and a dismissal earns exactly `tenure.closed` (finding 1).**
   - A delegate dismissal (`office == via` + `to`) on an `appointed` seat emits exactly
     `["tenure.closed"]` and opens no ban.
   - With `revoke`'s declared `emits` monkeypatched to `["tenure.closed", "tenure.opened"]`, it STILL
     emits exactly `["tenure.closed"]`. That is the explicit `earns` observed.
   - The principal's `appointed` revocation leaves his delegate's edge live and unbanned.
9. **Not a revocation, no cost.** A termed hold maturing at MATTER, a `release` of one's own hold, and
   a `confer` displacing an `appointed` incumbent each open no ban.
10. **Derived openers.** `ban`'s derived opener set is `{"determine", "revoke"}`. `KIND_VERB` is
    unchanged against a snapshot taken before the build. In particular `tenure.opened` still maps to
    `confer`, which is finding 2's falsifier.
11. **The EXIT.** `build_realm(0)` plus one build-placed `hold : p_npc_020 → duchy_varfell` (§4). By
    hand-built acts through the fold, NPC-020 revokes:
    - `off_lord_steward` (`appointed`) through **`off_duke_valorsmark`**: the hold closes, and
      `ban : p_npc_009 → off_duke_valorsmark` opens (a non-judging seat, so the ban enters by the
      licence);
    - `off_npc_052` (`elected`) through `off_npc_020`: the hold closes, and no ban opens.

    The test asserts `restrained(p_npc_009)` is True, `restrained(p_npc_052)` is False, and the two
    acts' opened-edge sets differ.

    **Controls:**
    - without the placement, the second revoke emits `revoke.refused`;
    - with `monkeypatch.setitem(gate.REVOCATION_DISPOSAL, "appointed", None)` (in place: a module
      rebind would leave any `from`-import stale, finding 11), the outcomes are equal and the third
      assertion fails. That is the plan's falsifier observed live.

    H-100 closes on this test, with R1-R3 in its cite.

---

## 6. Alternatives rejected

1. **A `Tenure.provenance` field stamped at opening.**
   - It is a schema move (the `repr` comment on `Tenure.term`, `state/carriers.py`).
   - It is a second home for a fact (`state/carriers.py:84-93`: `conferrer` was deleted because
     *"WHAT CONFERRED a Tenure is the opening Act ... A field here would be a second home for a fact
     the act already holds — `ID-2`"*).
   - Every builder would copy `Office.conferral` into it.
2. **A payload key stamped by `World._grant_remit`** (`seat_rung`'s precedent). The build hash moves
   by value, and it buys nothing: `conferral` is immutable by act (`loop/predicates.py:296-300`).
3. **Reading the opening act off the log** (the home `state/carriers.py:90-93` names).
   - Build-placed holds have no opening act: builders write outside the gate (the `founding` comment,
     `state/gate.py:1022-1030`). All 30 build holds would be unreadable, which forces refusal or
     default.
   - It would answer R3, but only for holds seated after tick 0, with a second rule for the rest.
   - The log route stays the natural fix for R3 once a non-`confer` filler exists (§8).
4. **Writing `standing`.** It is computed when read (`decision/options.py:1118-1140`); there is no
   field. Writing it means minting claims no witness made.
5. **Writing `regard` through a stance row.**
   - The precedent exists (`loop/effects_combat.py:250-261`; `write_matrix.yaml:220-226`).
   - It needs a new fixture: reusing `field_grudge_weight` is two decisions on one fixture (H-121,
     `queries/person_q.py:133-135`).
   - A grudge does not change whether losing a seat is survivable.
   - Declined, not foreclosed.
6. **Grading by `Tenure.degree`.** `revoke` is uncontested (`write_matrix.yaml:353`).
7. **`detain` for some provenance.**
   - A detention opens only by `warrant` or a bench (`state/gate.py:1055-1075`). Custody without a
     bench is a sentence without proceedings, and its candidate, `annex`, has no seat.
   - ⚠ The same objection reaches the chosen permanent ban, in degree (§2.3). It is carried into A1
     rather than answered here.
8. **A YAML column** (§2.2). **A twelfth gate basis** (§2.5). **A verb conjunct on the
   `determination` arm** (§2.5).
9. **`tenure.opened` on `revoke`'s `emits`.** It would unprice `confer` deeds through `KIND_VERB` (§4),
   and it would phantom-emit on every delegate dismissal, through `earns=None`.

---

## 7. EDITS for the build (B-Q, after IN-26)

`state/gate.py`
- `REVOCATION_DISPOSAL` and its import-time totality check, beside `REVOCATION_RULES` (`:537-547`).
- Import `BAN_KIND` (`:52`).
- `tenure_write_basis`:
  - keyword `revoked: frozenset = frozenset()`;
  - the ban arm before `if seat is None` (`:1076`), returning `T_O`;
  - the basis list in its docstring, including §2.5's judging-seat scope.
- `refuse_unauthored`:
  - the `revoked` Counter (`:1140`);
  - the second-pass condition `+released or +revoked` (`:1145`);
  - spend one unit per ban;
  - the docstring.
- `not_yours`' `needs=` text (`:1159`).

`loop/effects_governance.py`
- `_eff_revoke`:
  - the IN-48 branch passes `"tenure.closed"` explicitly to `_closing` (`:323-324`, finding 1);
  - the ordinary branch (§2.4) reads `gate.REVOCATION_DISPOSAL` in place, builds the literal `"ban"`,
    names both edges `earns=None`, and keeps the `NO_CHANGE` backstop;
  - the docstring.

`loop/predicates.py`
- `_req_revoke`: the refusal (§2.6), reading `gate.REVOCATION_DISPOSAL` in place, and the docstring.

`verb_table.yaml`, the `revoke` row (`:862-877`)
- `writes: ["Tenure.until", "Tenure.since"]` (`determine`'s precedent, `:249`).
- **`emits` unchanged: `["tenure.closed"]`** (ORCH, finding 2).
- A `disposal_note`:
  - the mapping's owner;
  - the ban earns no event of its own (`determine`'s precedent, `:249-251`);
  - the ban is permanent;
  - §2.7's non-revocations.
- `requires:` gains *"and the seat's conferral basis has a revocation disposal"*.

`rosters.yaml`
- The `tenure_kinds` note: `ban`'s openers are `determine` and `revoke`; a revocation's ban has no
  closer but death.

`workplans/valoria_master_workplan_v9_part5.md`, `### IN-31` (ORCH, finding 8)
- In the same commit, the EXIT becomes: *"a seeded test with a hand-built `revoke` per seat
  provenance, since a computed `revoke` executes 0 times (H-207)"*.
- [ASSUMPTION; medium; Jordan to correct; revert: keep the corpus-run EXIT and do not close H-100.]
- Reason: `corpus_run` has no route for scripted acts, and the computed `revoke` count is 0 (§4).

`hole_register.yaml`
- H-100 closed when test 11 passes, with R1-R3 in its cite.

`engine/season/tests/test_in31_revocation_cost.py`: §5.

**The build's hash instrument:** §4, the 4-season seed-0 `content_hash` before and after.

**Not edited:**
- `state/carriers.py`.
- `offices.yaml`.
- `queries/world_q.py::restrained`.
- `decision/`.
- `data/verbs.py`: the derivation picks up the literal; `KIND_VERB` is unchanged because `emits` is.

---

## 8. Assumptions, residues, and what survives the ladder

Assumptions, each [medium; Jordan to correct] and marked inline:
- **A1. What losing a seat costs, by provenance and by removing verb** (§0's box, §2.3, §2.7):
  - `appointed` → a permanent ban; `elected`, `annex`, `None` → nothing;
  - `confer`'s displacement → nothing (former A3);
  - irreversible except by death.

  Reverts: every value `None`; a termed ban; `_eff_confer` opening the same ban.
- **A2. The ban is admitted under `T-o`, not a twelfth basis** (§2.5). Revert: a basis named
  `revocation`.
- **A4. `conferral: None` is a value, not "unreadable"** (§1). The reason is not that `None` means
  heredity, since it mixes three provenances. The reasons are that the field is optional by
  declaration and that Jordan ruled the one revocable `None` seat strippable. Revert: refuse a `None`
  revocation. That overwrites the 2026-10-12 Hafenmark ruling, so the revert itself needs Jordan.
- **ORCH, finding 8:** the EXIT amendment (§7).
- **§2.5 scope (recommended, not an assumption about the game):** no verb conjunct on
  `determination`.

Named residues:
- **R1.** A ban closes nothing. The banned man's other seats and delegations stay live, including a
  delegation on the very seat that banned him (§3.1, `state/gate.py:304-319`).
- **R2.** `annex` has no seat: its outcome is declared and unobserved.
- **R3. LIVE, not hypothetical (finding 6).** Provenance is the SEAT's basis, not the seating route.
  - `confer` is the only filler of all three bases (*"NOTHING DISCRIMINATES BETWEEN THE THREE YET"*,
    `rosters.yaml:1859-1862`).
  - The one computed seating that executes on `build_realm(0)` is
    `Act(p_npc_032, confer, {to: p_npc_032, subject: off_npc_082}, via=off_npc_032)` in season 4
    (H-58's cite, `hole_register.yaml:676`; the H-207 cite at `:4451` names the same actor and
    seat). `off_npc_082`, the Military Jarl, is `conferral: elected` (`offices.yaml:520-531`).
  - So the one man who comes to sit by computed play reads `elected`: revocable at no cost, although
    he took the seat himself.
  - The route's home is the opening Act (`state/carriers.py:90-93`).
  - R3 closes either when the `13d-i` question (should `confer` narrow to `appointed`?) is ruled at
    `may_fill`, or when a filler for `elected`/`annex` exists and provenance is read off the opening
    act (§6.3).

**What survives all five ladder steps: A1 only**, stated in §0's box.
- It is a live design choice in which the defensible options produce materially different games:
  whether losing a seat is survivable, which provenances and which removing verbs carry a cost, and
  whether that cost can ever be undone.
- Steps 1-4 are silent: the research is tier 3, and ED-IN-0256 rules how a seat is filled, not what
  losing it costs.
- Everything else here is decided by precedent or by the architecture.
