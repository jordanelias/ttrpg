# 03 · SEATS AND CONTENT — how a seat becomes fillable

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` · id: **ED-IN-0235**. Carries **RR-B**.
## Grade under `CLAUDE.md` §0.2: **`paper`**. Nothing in this file executes. §C.8 names the artifacts
## that would move it and says why none has been produced. No row here may be cited as done.
## Method: authored at tier **`opus`** (`CLAUDE.md` §10 — *competing-considerations judgment,
## multi-doc synthesis*), against the working tree on **2026-09-17**. Every `path:line` below was
## opened at that line in this session; every count was **re-measured with the command printed
## beside it** (the plan's standing instruction 8, and `UNIFICATION_LEDGER.md` rows 20–21 are why:
## three of round one's *"opened and found CORRECT"* lines were false verifications). The APPENDIX
## lists the citations I found wrong **in my own sources** and repaired.
## Citation discipline: **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`, cited
## `ARCH §Letter.Number` and **never by line** — its line numbers have drifted twice. **`AX`** =
## `architecture/meta/01_AXIOMS.md`, cited `AX-n` / `AX §Letter.Number`, with a line in parentheses
## only as a finding aid. `holonic §NN.N` = `architecture/holonic_ARCHITECTURE.md`. A bare `01`/`02`/
## `04`/`05` means a file in **this** directory. `path:line` is for engine files only.
## Supersedes: round one's `01_SEATS_AND_POLICY.md` **seat half's MECHANISM** (§A.2, §A.3, §A.6).
## Its **seat model** is kept verbatim and is `ARCH §B.7` entire — restated here only where this
## file changes it, struck-and-kept. Round one's `00_THE_DESIGN.md` §A.2 is superseded by §A.2 here.
## Falsifiers in this file are **`SC-n`**; loops **`SC-L±n`**.

---

> **Round one's sharpest sentence, and this file owns it:**
>
> ### ***A plan that fixes the eligibility model and not the CONTENT fixes nothing.***
>
> **Jordan's remit, verbatim:** *"I do not want this work to be constrained by existing work. I want
> the best possible design ideas and concepts, and we can modify code accordingly."* · *"Your remit
> is to develop the most NERS-positive work possible."*
>
> **And the two clauses this file applies.** `ARCH §B.7`, grade MECHANICAL: *"**purview is asked of
> the seat exercised, not the actor** — `Act.via : SeatId?`; every purview walk uses `via.scope`.
> **A regent has the seat's purview**."* And `ARCH §B.7` call 1: *"**No `Title` type; the revocation
> rule is data.** An ordinary seat revocable on purview alone and a title needing purview + holdings
> + higher rank are two *values* of `revocation.conjuncts`, declared at `establish`. **No `is_title`
> branch exists anywhere** — ID-4."*
>
> **`AX` ID-14 (`AX:519`), which nobody in round one cited and which settles half of this file:**
> *"`Seat.conferral` becomes `hold-kind → {confer | determine | succeed}` and stops being a field
> nobody reads — which is `ID-13` closed at the site `§E.2.5` says has 'been on the Office since
> #353 carrying nothing.'"*

---

# PART 0 · THE CONFORMANCE DIVISION, AND IT IS THE SPINE OF THIS FILE

**The MECHANISM half of this file is almost entirely ratified Layer 1 and merely unbuilt.** The
value sets, the deletion of the `is_title` branch, the death of `establishment` as a field, the
purview rule — all four are `ARCH §B.7` or `AX` ID-14, and a proposal that restates ratified
architecture as a proposal invites a session to re-decide a settled thing. **The CONTENT half is
entirely new**, and it is where the work is: `offices.yaml` did not exist, `offices_draft.yaml`
cannot be copied into it, and every seat in the built world is unfillable for reasons that have
nothing to do with the eligibility model.

So every section below carries one of three words, and the three lists are in front.

## §0.1 · The three lists

**CONFORMANCE — RATIFIED Layer 1, UNBUILT in the engine. Nothing here is proposed; it is owed.**

| item | the ratified clause | the engine as measured, 2026-09-17 |
|---|---|---|
| `conferral ∈ {confer, determine, succeed}` as a **declared value** | `ARCH §B.7`'s own list; **`AX` ID-14 (`AX:519`) spells the set** | `Optional[str] = None` (`engine/season/state/carriers.py:489`), **`None` on 19 of 19 offices** |
| `revocation` as a **declared value**, not a code path | `ARCH §B.7` call 1 | `Optional[str] = None` (`carriers.py:490`), **`None` on 19 of 19** |
| **no `is_title` branch anywhere** (`AX` ID-4, `AX:443`) | `ARCH §B.7` call 1 | the branch runs: `engine/season/loop/predicates.py:252` computes `target_is_title` and `:254` takes one of two rules on it — **H-109** (`engine/season/hole_register.yaml:1520`) |
| **purview is asked of the seat exercised** | `ARCH §B.7`, grade **MECHANICAL** | asked of the actor's **post STRING**: `predicates.py:152` filters on `title_domain(o.post) is not None` |
| `Act.via : SeatId?` | `ARCH §B.9`; `ARCH §C.2` F3 | **absent.** `Act` (`carriers.py:332-365`) carries `id, actor, verb, changes, reads, contests, payload, stratum, obstacle, pool, scene` and no `via`. Verified by `grep -rn "a\.via\|act\.via\|'via'\|\"via\"" engine/season/` → **0 hits** |
| **`establishment` is a Query over `oblige`, not a field** | `ARCH §B.7` call 2; `AX §E.2.5`'s own correction (`AX:1465`) | a field (`carriers.py:491`) read at exactly one site (`engine/season/queries/world_q.py:413`) and **`[]` on 19 of 19** |
| a council is **one seat, many holders via `oblige`** | `AX §E.2.5` (`AX:1477`) | `Office.binds` is `"members_by_admission"` on 19 of 19 — the dataclass default (`carriers.py:488`) and its only occurrence |
| succession is the holder's disposition | `ARCH §A.3` row 8; `ARCH §B.8` | `succeed` is `own`-eligible with a typed `relation` cell (`engine/season/verb_table.yaml:490-506`) and has **no `@effect_for` body** |

**EXTENSION — consistent with ratified Layer 1, unratified, and this file's actual proposal.**

| item | what it rests on | §here |
|---|---|---|
| **the value sets are CLOSED ROSTERS the loader enforces**, refusing an off-roster basis in `Office.__post_init__` exactly as it already refuses an off-roster remit act | `carriers.py:508-512` (the existing `Unowned`); `World.add_tenure`'s own docstring, *"the same failure shape `Office.__post_init__` already refuses for remit acts (§8: one rule, applied at every constructor rather than at one)"* (`engine/season/state/world.py:240-241`) | §A.4, §A.5 |
| **purview = `descendants(w, seat.rung) ∪ {seat.rung}`, minus the seat you are exercising** — one walk, shared with REACH (`01`) | `world_q.descendants` (`world_q.py:54`); `under_purview` already walks the same ladder (`predicates.py:132-141`) | §A.6 |
| **the higher-rank conjunct is DERIVED from containment, not deleted** — proof in §A.5.1 from `World.contain_ascends` (`world.py:197-221`), enforced at the one writer (`world.py:248-256`) | `rosters.yaml:106-109` (`rung_kinds`); `data/rosters.py:465-472` (`title_rank` IS the rung ordinal) | §A.5.1 |
| **`engine/season/data/offices.yaml`** — a world-gen content file read by `build_realm`, declaring **29 seats**, each with a rung ANCHOR, a remit, a conferral basis and a revocation basis | `CLAUDE.md` §0.05 clause 1 (a fact code reads is authored in YAML, never in prose); the `office_bodies`/`titles` precedent of one authored field and two derived (`data/rosters.py:408-453`) | §A.13–§A.16 |
| **a rung ANCHOR rather than a rung id**, resolved by the loader against the world it is building | `CLAUDE.md` §5 — *"every value crossing into Godot is hand-transcribed — live drift risk"*, applied one layer earlier: a hand-transcribed `terr_T9` rots the moment `build_realm` renames a rung | §A.14 |
| **the commission `Record`** minted by `_eff_confer`, so the conferee **believes** his remit | `AX-2` (`AX:100-110`); `_eff_create_record`'s existing hold mint (`engine/season/loop/effects.py:287-289`); the deposit rule owned by `02` §the-writ | §A.11 |
| **`oblige` is admission**, so F.17 closes without a sixth remit act | `ARCH F.17`; `holonic §15`'s `oblige : Person → Person \| Office, many`; `verb_table.yaml:375-383` (`oblige`, `own`, `Tenure.since`, no body) | §A.9 |

**DEPARTURE — needs a ruling. There are TWO in this file, and both are RR-B.**

| item | why the five gates cannot answer it |
|---|---|
| **`ARCH §B.7`'s `Seat :=` line spells `upkeep` and `dates[]`, which this file deletes** (0 readers each, measured §0.2) | `architecture/` is RATIFIED (ED-IN-0204). `CLAUDE.md` §0 gate 5 may not overwrite ratified canon. Quoted at its `§`, **not edited** |
| **`ARCH F.21` presupposes a `higher_rank` conjunct** — *"the loader forbids a `higher_rank` conjunct on [a cluster seat]"* — and §A.5.1 derives rank from containment instead, so no value set names the conjunct | §A.5.1 argues the conjunct is **redundant given a structural guard**, which is gate 5's shape; but F.21 is a ratified row that assumes the conjunct **exists**, and gate 5 cannot delete a thing ratified canon names. ⚠ **F.21 is therefore NARROWED, NOT CLOSED, and this file says so rather than claiming it** |

**And one ruling this file does NOT make:** `ARCH F.18` (upkeep's source) **stays open.** Deleting
`Office.upkeep` removes a field with zero readers; it does not answer *"out of the office's stake"*,
and `stake` was retired. F.18's own consequence line — *"no economic pressure on any office"* —
remains true after this file. Named so a reader does not conclude it fell with the field.

## §0.2 · What I measured, today, rather than quoted

**Command, run 2026-09-17 against this working tree:**

```sh
python -c "from engine.season.harness.populated import build_realm; ..."   # the table of §A.2
grep -rn 'title_domain\|title_rank\|titles_held\|highest_title_rank' --include=*.py engine/
for f in conferral revocation establishment upkeep dates scope_rung binds body_function; do
  grep -rn "\.$f\b" --include=*.py engine/season/ | grep -v '/tests/' | grep -v 'carriers.py'; done
```

```
rungs 375   persons 46   offices 19
  realm 1 · duchy 3 · province 0 · territory 17 · settlement 37 · community 60 · hearth 211 · person 46
offices:  conferral None ×19 · revocation None ×19 · upkeep None ×19 · establishment [] ×19
          dates [] ×19 · scope_rung set on 3 (by __post_init__, never authored)
          binds "members_by_admission" ×19  (the dataclass default; its only occurrence)
          remit_acts non-empty on 3 of 19   (the three authored case overlays)
          body set on 10 of 19             (all ten ON the live `office_bodies` roster)
seats with a rung at all:              3 of 19   (King · Duchess · Duke)
posts on the `titles.domains` ladder:  3 of 19
holders with purview over their own seat's rung:  3 of 19 (the same three)
holders with purview over ANY rung:    3 of 19 — King 365, Duchess 85, Duke 94; the other sixteen 0
holders SEATED at their seat's rung:   0 of 19 — all nineteen are contained in a `hearth`
holders living INSIDE their seat's rung closure: 1 of 3 (the King; the Duke and the Duchess are not)
live `hold` Tenures 35 = 19 person→office + 16 FACTION→territory.  person→rung holds: 0
Office field readers outside tests and `carriers.py`:
  conferral 1 (predicates.py:181) · revocation 1 (predicates.py:234) · establishment 1 (world_q.py:413)
  remit_acts 2 (resolve.py:56, epistemic.py:360) · upkeep 0 · dates 0 · scope_rung 0 · binds 0 · body_function 0
verb rows 38 · resolvable 18 · `establish` NOT resolvable · `oblige` NOT resolvable
`"inferred"` occurrences in engine/**/*.py: 0        `record_kinds` anywhere in engine/: 0
```

**Six of those are load-bearing on what follows and none is in any source document in this form.**

1. **Every one of the nineteen seats has an empty `conferral` and an empty `revocation` basis** —
   and `_req_confer` refuses an office with no conferral basis (`predicates.py:181-182`),
   `_req_revoke` one with no revocation basis (`predicates.py:234-235`). **So no seat in the built
   world can be conferred or revoked, and the reason is not `remit:` — it is two empty strings.**

2. **Sixteen of nineteen seat-holders have purview over NOTHING, including their own seat's rung.**
   Measured as a number, not a category: `sum(under_purview(w, holder, rid) for rid in w.rungs)` is
   365 for the King, 85 for the Duchess, 94 for the Duke, and **0** for the other sixteen. The cause
   is `titles_held` filtering on `title_domain(o.post) is not None` (`predicates.py:152`) against an
   eleven-name roster (`engine/season/rosters.yaml:755-766`), so *Chief Parliamentary Clerk*,
   *Cardinal Justice*, *Royal Marshal* and *Skald-Chief* govern nothing. **`ARCH §B.7`'s MECHANICAL
   invariant, measured in the negative: purview is read off a post STRING.**

3. ⭐ **NEW, and round one did not have it: 0 of 19 holders are seated at their seat's rung, and the
   Duke and the Duchess do not live inside the duchy they govern.** All nineteen holders are
   contained in a `hearth` (`options.containing_rung_of`, `options.py:172`, returns the person's own
   live `contain` object). The King's hearth chains up through `set_s_002 → terr_T1 →
   duchy_valorsmark → r_valoria`, so he is inside his own closure; the Duke of Varfell's chains
   through `set_s_003 → terr_T1 → duchy_valorsmark`, and **`duchy_valorsmark` is not
   `duchy_varfell`.** So is the Duchess of Hafenmark's. **Two of the three seats that work are held
   by people standing in another duke's duchy.** §A.14 is where the content fixes this and §A.10 is
   why it is not fixed by moving them.

4. ⭐ **NEW: all 16 rung-holds are FACTION-subject and every one is a TERRITORY.** Zero persons hold
   any rung. `in_holdings(w, actor, rung)` tests `t.subject == actor` with `actor` a **person**
   (`predicates.py:101-102`), so **a `revocation: holdings` basis refuses 100% of the time today**,
   for a reason that has nothing to do with the basis. That is a hidden dependency of this file's
   build item on the faction-hold re-homing, and §D's `SC-6` is its falsifier.

5. **`records 0` and `Record.kind` is a free string** — `_eff_create_record` writes
   `d.get("kind") or "text"` (`effects.py:285`). There is no `record_kinds` roster anywhere in
   `engine/` (grep: 0 hits). The `commission` of §A.11 therefore needs `02`'s roster, and this file
   declares the dependency rather than assuming it.

6. **`conferral_path` (`world_q.py:416-436`) has ZERO non-test callers and never reads `conferral`.**
   Its docstring says *"§11 gives an Office a `conferral` basis and a `rung?`"* and its body reads
   `off.rung` alone. A Query named for a field it does not open, called by nothing but
   `engine/season/tests/test_season_shape.py:11071`. §A.12 disposes of it.

## §0.3 · THREE CLAIMS THIS FILE DOES NOT MAKE, struck in place

**⛔ STRUCK.** ~~*Sixteen seats have purview over nothing because they have no rung.*~~ Two different
defects were being run together, and the conflation would have made the content fix look sufficient.
**Measured:** `under_purview(w, actor, None)` returns `False` at its own first line
(`predicates.py:118-119`, *"if holding is None: return False"*), so a seat with `rung = None` is
unreachable **whatever** the post says. But `titles_held` filters on the POST, so even a seat WITH a
rung governs nothing unless its post is on the title roster. **The two are independent and both are
live:** 16 seats have `rung = None` **and** 16 seats have a non-title post, and they are the same
sixteen only by coincidence of this world's content. Giving all 19 a rung and leaving the post filter
in place would fix **nothing**; deleting the filter and leaving the rungs null would fix **nothing**.
§A.13's content and §A.7's mechanism are therefore **both** preconditions, neither sufficient.

**⛔ STRUCK.** ~~*`title_domain` and `title_rank` are pure roster reads with no structural role, so
deleting them is a four-line change.*~~ **Measured:** `title_domain` is called inside
`Office.__post_init__` **twice** (`carriers.py:536` and `:546`), where it enforces two invariants
this file must re-home or lose — the title/body `Forbidden` at `:537-543` and the `scope_rung`
defaulting at `:546-548`. Deleting the helper without re-homing those is a silent removal of two
constructor refusals. §A.8 re-homes both.

**⛔ STRUCK.** ~~*Deleting the four title helpers deletes Jordan's revocation rule's rank conjunct.*~~
It deletes the **implementation** of it and keeps the **rule**, and §A.5.1 is the proof rather than
the assertion: `World.contain_ascends` (`world.py:197-221`) makes every `contain` edge strictly
ascend `rung_kinds` **at the one writer that can create one** (`world.py:248-256` raises `Forbidden`
otherwise), and `title_rank` is *defined* as the domain's ordinal in `rung_kinds`
(`data/rosters.py:465-472`). So containment entails strictly-higher rank **structurally**, and the
conjunct is a second reading of a ladder that already exists — which is the `S-METHOD` defect
`CLAUDE.md` §0.06 names in terms (*"two ladders for one quantity is an S defect even when each is
individually correct"*). ⚠ **The residue is real and is declared:** two seats at the SAME rung, where
containment says nothing. §A.5.1 handles that case by **seat identity**, and F.21 stays open (§0.1).

---

# PART A · THE CLAIMS, EACH WITH ITS VERDICT

Every subsection is a candidate/owner/verdict table closed by a `> ### RULED:` line citing the
clause that decides it. **CONFORMANCE** means *this was decided; build it*. **EXTENSION** means
*this is the proposal*. **DEPARTURE** means *do not build it until Jordan rules*.

## §A.1 · THE TWO EMPTY STRINGS — both predicates read at the line, with the exact refusal each makes

### §A.1.1 · `_req_confer` (`predicates.py:167-192`), opened

```python
@requires_predicate("confer")
def _req_confer(w, a) -> bool:
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}   # :177
    obj = d.get("office")                                          # :178
    if not obj or obj not in w.offices:                            # :179
        return False                                               # :180
    if not (w.offices[obj].conferral or "").strip():               # :181
        return False   # no conferral basis: the office cannot be conferred   # :182
    if not any(t.kind == "hold" and t.object == obj and t.live for t in w.tenures):  # :183
        return True    # 1-per-object satisfied                    # :184
    holder = next((t.subject for t in w.tenures                    # :188-189
                   if t.kind == "hold" and t.object == obj and t.live), None)
    return holder is not None and not any(                         # :190-192
        t.kind == "commit" and t.subject == holder and t.live for t in w.tenures)
```

| line | the refusal | reaches the 19? |
|---|---|---|
| `:179-180` | the payload names no office, or an id not in `w.offices` | not the content's problem — a malformed act |
| **`:181-182`** | **`conferral` is `None` or blank** | ⭐ **all 19. This is the wall.** `(None or "").strip()` is `""`, falsy, so `not ""` is `True`, so **every seat in the built world returns `False` here** |
| `:183-184` | — (an admission) | unreachable: `:182` already returned |
| `:190-192` | a held seat whose holder has a live `commit` | unreachable, same reason |

**The verb row's cell, read for what it asks** (`verb_table.yaml:148`): *"the office's **conferral
basis**, and 1-per-object: no live hold on the object, **or** the holder-Proposition has zero live
commit (§54 it. 20)"*. The predicate implements it faithfully. **The cell asks for a basis and the
content supplies none, and no amount of eligibility work reaches past line 181.**

### §A.1.2 · `_req_revoke` (`predicates.py:222-287`), opened

```python
    if not obj or obj not in w.offices:      return False          # :232-233
    if not (w.offices[obj].revocation or "").strip():  return False  # :234-235
    target_is_title = title_domain(w.offices[obj].post) is not None  # :252
    domain = w.offices[obj].rung                                   # :253
    if target_is_title:                                            # :254
        if not under_purview(w, a.actor, domain):   return False    # :266-267
        if not in_holdings(w, a.actor, domain):     return False    # :268-269
        if highest_title_rank(w, a.actor) <= title_rank(w.offices[obj].post):  # :270
            return False                                           # :274
    elif not under_purview(w, a.actor, domain):     return False    # :275-276
    return any(t.kind == "hold" and t.object == obj and t.live for t in w.tenures)  # :287
```

| line | the refusal | reaches the 19? |
|---|---|---|
| **`:234-235`** | **`revocation` is `None` or blank** | ⭐ **all 19. The second wall, and it is the same shape as the first.** |
| `:252` | — | the `is_title` computation. **H-109** (`hole_register.yaml:1520`): *"THERE IS AN `is_title` BRANCH … the meta-architecture states the opposite in terms"* |
| `:266-274` | the title rule: purview **and** holdings **and** strictly-higher rank | unreachable; and §0.2 pt 4 shows the holdings conjunct is unsatisfiable by any person today |
| `:275-276` | the ordinary rule: purview alone | unreachable; and §0.2 pt 2 shows purview is 0 for sixteen |

**So `revoke` has three independent walls stacked**, and round one saw one of them. Measured, in
order of arrival: the empty basis at `:235`; then, if a basis were set, the post-string purview filter
at `:152` reached through `:275`; then, for a title, the faction-subject holds at `:268`.

| candidate | who owns it? | verdict |
|---|---|---|
| the refusals are a mechanism defect | round one's implicit reading | **REFUSED.** Both predicates do exactly what their `requires:` cells say. `verb_table.yaml:148` and `:473` ask for a declared basis; **the content declares none**. A mechanism that correctly refuses an under-specified world is not broken |
| the refusals are a CONTENT defect | this file | ⭐ **EXTENSION, ADOPTED.** `AX §E.2.5` (`AX:1495-1498`) already says it: *"**Delegation does not need a delegation mechanism. It needs the `conferral` basis to be specified**, and that field has been on the Office since #353 carrying nothing"* |
| both, and they are separable | this file | **CONFORMANCE + EXTENSION, and the order matters.** The `is_title` branch is a Layer-1 conformance defect (H-109) that exists **independently** of the empty bases; the empty bases are content. Fixing either alone leaves `confer` and `revoke` unformable |

> ### **RULED: two empty strings, not one blocked eligibility model — and the walls are stacked, so
> the content and the mechanism are BOTH preconditions.** Cited to `predicates.py:181-182` and
> `:234-235` (opened above), `verb_table.yaml:148` and `:473` (the cells they implement), `AX:1495-1498`
> (the basis was always the slot) and `hole_register.yaml:1520` (H-109, the branch). **`_req_confer`'s
> and `_req_revoke`'s bodies are otherwise CORRECT and this file does not rewrite what they check —
> only WHAT THEY READ IT FROM** (§A.7).

## §A.2 · THE PURVIEW DEFECT, MEASURED — and the new half round one did not have

Round one measured *"3 of 19 posts on the ladder, 16 of 19 `rung None`"*. Both reproduce. **Two
further measurements change what the fix has to do.**

| candidate | who owns it? | verdict |
|---|---|---|
| purview read off the actor's **post string** | `predicates.py:144-154` `titles_held`, filtering `title_domain(o.post) is not None` at `:152` | **CONFORMANCE defect.** `ARCH §B.7` grades the repair MECHANICAL. Measured: purview over **0** rungs for 16 of 19 |
| purview read off the seat's **rung** | `ARCH §B.7`; `ARCH §B.9`'s `Act := (id, actor, via : SeatId?, …)` | **CONFORMANCE.** The walk is `world_q.descendants` (`world_q.py:54`), which `01` also uses for REACH — one walk, two readers |
| ⭐ **a seat with no rung governs nothing, and sixteen have none** | `carriers.py:485` (`rung: Optional[str]`); `predicates.py:118-119` | **CONTENT defect, and independent of the post filter** (§0.3, struck claim 1). `ARCH §B.7`'s `scope? (null = a cluster)` makes a null rung **lawful**; `ARCH F.21` records what it costs — *"church seats become revocable by purview alone — **which they also lack**"* |
| ⭐ **a holder standing outside the rung he governs** | nothing | **CONTENT defect, NEW.** Measured: the Duke of Varfell and the Duchess of Hafenmark are both contained in `terr_T1` → `duchy_valorsmark`. Their purview walks work and reach 94 and 85 rungs; **they are co-located with none of them**, so no Event at any of those rungs reaches them by `_ch_co_located` (`epistemic.py:244`) |
| a `via.scope` sub-field distinct from the seat's rung | nothing | **REFUSED**, as round one refused it: *"nothing licenses a second scope. `via` names the seat; the seat carries the scope."* Measured support: `Office.scope_rung` (`carriers.py:487`) already exists, is set by `__post_init__` for titled posts only, and has **0 readers** — a second scope field that nothing reads is what the refusal looks like when it is ignored |

> ### **RULED: `ARCH §B.7`, MECHANICAL — purview is the seat's ground, and the seat's ground is its
> rung's containment closure.** Three consequences, and they are one item: the post filter goes
> (`predicates.py:152`), the four helpers go with it (§A.3), and **every seat gets a rung** (§A.13).
> ⚠ **A fourth consequence, NEW and not in round one:** a seat's rung must be somewhere its holder
> can stand, because purview decides what he may ACT on and co-location decides what he ever HEARS
> about. §A.14 makes that a schema requirement; §D `SC-3` is its falsifier.

## §A.3 · THE FOUR TITLE HELPERS — where each lives, and every call site

⚠ **Round one placed `title_domain` in `predicates.py` and repaired it in its own appendix**, with
the reason stated: *"a session deleting 'four helpers in one file' would have found three."* **It is
worse than that, and here is the full map, measured** (`grep -rn 'title_domain\|title_rank\|titles_held\|highest_title_rank' --include=*.py --include=*.yaml engine/`):

| helper | defined at | call sites OUTSIDE tests | what deleting it breaks |
|---|---|---|---|
| **`title_domain`** | `engine/season/data/rosters.py:459-463` | **five, in three files:** `data/rosters.py:471` (inside `title_rank`) · `loop/predicates.py:152` (`titles_held`) · `loop/predicates.py:252` (`_req_revoke`) · **`state/carriers.py:536`** (`Office.__post_init__`, the title/body `Forbidden`) · **`state/carriers.py:546`** (`Office.__post_init__`, the `scope_rung` default) | **two constructor invariants**, not just two predicates. §A.8 re-homes both |
| **`title_rank`** | `engine/season/data/rosters.py:465-472` | **two:** `loop/predicates.py:163` (`highest_title_rank`) · `loop/predicates.py:270` (`_req_revoke`'s rank conjunct) | the rank conjunct. §A.5.1 derives it |
| **`titles_held`** | `engine/season/loop/predicates.py:144-154` | **two, both inside its own module:** `:132` (`under_purview`) · `:163` (`highest_title_rank`) | nothing outside `predicates.py` |
| **`highest_title_rank`** | `engine/season/loop/predicates.py:157-163` | **one:** `:270` (`_req_revoke`) | the rank conjunct |

**Imports to remove:** `predicates.py:27` (`from ..data.rosters import RELEASABLE_KINDS, title_domain,
title_rank` → `RELEASABLE_KINDS` alone) and `carriers.py:34` (the `title_domain` member of a
multi-name import). **`harness/populated.py:75` and `:671` also import and call `title_domain`** to
decide whether a registry row's title names a governing rung — that call is **replaced by the content
file, not repaired** (§A.13), because `offices.yaml` declares the rung and nothing needs to infer it.

**Test sites that pin the current behaviour and must be rewritten, not deleted** — measured, and each
named with what it will assert instead:

| test | line | asserts today | becomes |
|---|---|---|---|
| `test_the_title_ladder_is_total_over_the_rungs_and_rank_is_the_rung_ordinal` | `engine/season/tests/test_season_shape.py:4403` | `title_rank(ttl) == RUNG_KINDS.index(dom)` for all eleven; `title_domain("Dicastery") is None` | **the same claim about the ROSTER**, which survives: `rosters.yaml:755-766` still names eleven titles and `rung_kinds` still orders them. The test loses its two helper calls and reads the roster directly |
| `test_purview_is_containment_and_stops_at_the_holders_own_domain` | `:4445` | ⚠ **`assert not under_purview(w, "p_mid", "S")`** — an ordinary seat at the duchy confers **no** purview inside it (`:4478-4480`) | ⭐ **goes RED, and it is SUPPOSED to.** §A.6 rules that an ordinary seat at the duchy DOES reach inside it. The replacement assertion is the one the old test's own comment gestures at: the Dicastery holder **reaches** `S` and **may still do nothing there**, because `remit_acts` is `[]` and `off_duke.revocation == "holdings"` |
| `test_revoking_a_title_needs_holdings_and_revoking_an_office_needs_purview` | `:4514` | the two-rule branch, by post string | **the two VALUES**, by basis: `revocation: "holdings"` on the Duke's seat, `"purview"` on the clerk's |
| `test_no_person_can_choose_a_governance_verb_and_h71_is_why` | `:4992` | `remit:` declines person-side | **goes RED when §A.11 lands** and is rewritten as the control: *a seat whose remit lacks the act forms no candidate* |
| `test_the_corpus_cannot_reach_the_governance_branch_and_h71_is_not_the_reason` | `:4640` | no probe mints a governance Act; `headless.build_world` creates no offices | **stays green and becomes the measurement that matters.** Its own docstring says it *"goes red when a probe or the headless world starts reaching the branch — at which point `PROBE FLIPS 0` starts meaning something"* |

> ### **RULED: four helpers, three files, nine non-test call sites, five test sites — and TWO of the
> nine are constructor invariants that must be re-homed rather than removed.** Cited to
> `data/rosters.py:459,465`, `predicates.py:144,157`, `carriers.py:536,546` and the grep above.
> ⚠ **Struck and kept from round one:** ~~`predicates.py:144-164` for `title_domain`~~ → **`data/rosters.py:459`**,
> and ~~"the deletion of four helpers"~~ → **four helpers plus two constructor clauses**, because a
> session working from the shorter sentence would have deleted `title_domain` and silently dropped
> the title/body refusal that keeps a King out of the Church (`carriers.py:537-543`).

## §A.4 · `conferral` — THREE VALUES, AND THE SET IS ALREADY RATIFIED

`AX` ID-14 (`AX:505-521`, opened) is the sentence round one did not cite and it settles this
subsection outright:

> *"The check as first written asks, for every kind, **which verb closes it**. It never asks which
> verbs may OPEN it — so a hold opened by an undeclared verb passes every gate, and `Seat.conferral`
> (*"which ACT fills the seat"*) sits on the schema carrying nothing. … **What this buys immediately:**
> `Seat.conferral` becomes `hold-kind → {confer | determine | succeed}` and stops being a field nobody
> reads."*

| value | means, operationally | the act that fills the seat | what `_req_confer` does |
|---|---|---|---|
| **`confer`** | *a superior names the holder.* A seat whose ground lies inside another seat's ground, filled by that seat's exercise | `confer` (`verb_table.yaml:143-153`), `remit:confer`, writes `Tenure.until` + `Tenure.since`, effect `_eff_confer` (`effects.py:92-126`) — **built** | **admits**, if the actor exercises a seat whose purview reaches this seat (§A.6) and 1-per-object holds |
| **`determine`** | *a body decides.* A council, an assembly, a chapter or an electorate resolves a vacancy at a sitting | `determine` (`verb_table.yaml:186-195`), `remit:determine`, writes `Tenure.degree`, **no effect body, `grade: absent`** | **refuses** `confer` outright. The seat is filled by `determine` at a fired Date, `AX §E.2.5`'s third shape — *"a seat filled by a PROCESS, not by a superior … **`determine`, not `confer`**"* |
| **`succeed`** | *it passes to the designated heir.* The holder's own disposition, declared in life | `succeed` (`verb_table.yaml:490-506`), eligibility **`own`**, typed `relation`/`held_by` cell, writes `Tenure.since`, **no effect body** | **refuses** `confer`. The heir fills it by `succeed`, which is `own`-eligible and therefore formable by the heir with no remit at all |

**Why exactly three and no fourth.** `ARCH §B.7`'s own list is *"confer by `<seat>` | determine by
`<judging seats>` | succeed"*, and `AX` ID-14 spells the identical set. Round one proposed a fourth,
`warrant`, for a consecration, and **refused it correctly**: a consecration is `determine` by a
judging set whose members' seats lie **outside** the consecrated seat's containment path, so what must
widen is `ARCH §B.7` call 3's **door** (*"the seats whose remit covers the matter at that venue"*),
not `conferral`'s value set. **That refusal stands here verbatim and is not re-argued.**

⚠ **The value is a BASIS, not an authority, and the distinction is `ARCH §B.8`'s.** A `confer` basis
does not name **which** seat may confer — that falls out of purview (§A.6), so the same basis works
for every seat on the ladder without a per-seat pointer. `ARCH §B.8`'s `T-o` row says it at the other
end: *"**The basis resolves against the Seat** — `Seat.revocation` is authoritative and `term.closer`
names a basis, not a second authority."* One fact, one home.

**Which seats take which, in this world** (the full table is §A.16; the shape is here):

| `conferral` | seats | why |
|---|---|---|
| `succeed` | the realm and duchy titles, the Heir Apparent, the Widow Regent, the Princess | **6** — a crown passes; `ARCH F.22` is exactly this (*"the named heir is eligible by `own`"*) |
| `determine` | the three Varfell Jarl-Council seats, the Hafenmark Commune Representative, the Guild Comptroller, the Confessor, the Duke of Varfell | **8** — an assembly, a commune, a forum, a chapter, a Jarl-Confederacy. Canon: *"first among the Jarls, not a monarch"* (`faction_politics_v30.md:246`, quoted in `harness/populated.py:308-310`) |
| `confer` | the fifteen remaining — the Crown Inner Circle, the four Cardinals, the Senior Inquisitor, the two Hafenmark ducal seats, the Löwenritter Grand Master, the Archbishop's Representative, the Restoration leadership | **15** — a superior names them |

> ### **RULED: CONFORMANCE — the value set is `{confer, determine, succeed}` and it is ratified twice
> over.** Cited to `ARCH §B.7` call 1's list and **`AX` ID-14 (`AX:519`)**, which spells the three.
> The EXTENSION is the loader clause: `Office.__post_init__` refuses a `conferral` off the roster,
> the same shape as its existing remit refusal (`carriers.py:508-512`). `warrant` is refused on
> `ARCH §B.7` call 3, as round one refused it. **Nothing here is a design choice; it is a transcription
> that never happened.**

## §A.5 · `revocation` — THREE VALUES, AND ONE OF THEM IS A CONJUNCTION

`ARCH §B.7` call 1, verbatim: *"An ordinary seat revocable on purview alone and a title needing
purview + holdings + higher rank are two **values** of `revocation.conjuncts`."* So the field's value
names a **conjunct set**, and there are three sets.

| value | conjunct set | means, operationally | which seats |
|---|---|---|---|
| **`purview`** | `{reaches}` | *whoever governs the ground may empty the seat.* Jordan, 2026-09-02: *"a Duke can revoke office from any individual in that office so long as that office is for a holding under their purview"* (`rosters.yaml:719-720`) | **19** — every ordinary seat: the Inner Circle, the Cardinals, the councils, the ducal officers |
| **`holdings`** | `{reaches, in_holdings}` | *governing the ground is not enough; you must OWN it.* Jordan: *"King/Queen cannot revoke title of Duke/Duchess if they do not have duchy is in their holdings. King/Queen CAN revoke title of Duke/Duchess if the duchy is one of their holdings."* (`rosters.yaml:721-723`) | **3** — the three duchy titles |
| **`none`** | `⊥` | *nobody may empty this seat by an act.* It ends by death, by `release` (the holder's own resignation, `T-m`), or by `succeed`. | **7** — the realm seat, the Widow Regent, the Heir, the Princess, the Confessor, and the two Restoration seats canon calls *"informal"* |

**`reaches` is defined once, in §A.6, and both value sets call the same function.** That is the
point of making them values: two conjunct sets over one predicate, rather than two code paths over
one post string.

### §A.5.1 · THE HIGHER-RANK CONJUNCT IS **DERIVED**, NOT DELETED — and here is the proof

This is the one place where deleting the title family could silently drop a ruled behaviour, so the
argument is a proof from a structural guard rather than an appeal to tidiness.

**Claim.** For any two seats `A` and `B` with rungs `ra` and `rb`, if `rb ∈ descendants(w, ra)` then
`rank(A) > rank(B)`, where `rank` is `title_rank`'s own definition — the domain's ordinal in
`rung_kinds`.

**Step 1 — `title_rank` IS the rung ordinal.** `data/rosters.py:465-472`, opened: *"A title's rank as
its domain's ordinal in `rung_kinds`. Higher governs wider. ⚠ **RANK IS NOT A SECOND LADDER.**
`rung_kinds` is already ordered person → realm, and each title names the rung kind it governs, so the
ordering falls out of a roster that exists rather than from a number somebody assigns."* The body is
`list(RUNG_KINDS).index(dom)`.

**Step 2 — every `contain` edge strictly ascends `rung_kinds`, enforced at the one writer.**
`World.contain_ascends` (`world.py:197-221`) returns `order.index(obj.kind) > order.index(sub.kind)`
— a **strict** inequality — and `World.add_tenure` (`world.py:223-257`, the docstring's own words:
*"The ONE writer"*) raises `Forbidden` on a `contain` that fails it (`world.py:248-256`), with the
law quoted in the exception: *"#353 §10 — `contain : Rung → Rung` is the containment LADDER. An edge
that does not ascend makes `under_purview` walk sideways or loop, and Jordan's governance canon reads
purview off that walk."*

**Step 3 — `descendants` is transitive over `contain` and PROPER.** `world_q.descendants`
(`world_q.py:54-64`) seeds `seen = {rung_id}` and never appends the seed, so `rung_id ∉
descendants(w, rung_id)`. **Verified by execution:** `'r_valoria' in descendants(w, 'r_valoria')` →
`False`.

**Step 4 — therefore.** `rb ∈ descendants(w, ra)` means a chain of ≥1 strictly-ascending `contain`
edges from `rb` to `ra`, so `ordinal(kind(ra)) > ordinal(kind(rb))`, so `rank(A) > rank(B)`. **∎**

**Verified by measurement, not only by reading:** all **373** rung→rung `contain` edges in
`build_realm(0)` satisfy strict ascent — **0 violations** — and the observed child→parent kind pairs
are `person→hearth, hearth→community, community→settlement, settlement→territory, territory→duchy,
territory→realm, duchy→realm`. Two of those skip a tier (`territory→realm`, and `duchy→realm` skips
the absent `province`), which is **lawful and deliberate**: `harness/populated.py:297-298` records it —
*"`contain_ascends` permits `territory → duchy` directly (checked: the parent need only be strictly
above), so the ladder skipping a conditional tier is legal by construction."* Skipping a tier
preserves the strict inequality, so the proof is unaffected.

**The residue, stated rather than hidden: two seats at the SAME rung.** Containment says nothing
there, and the rank conjunct also said nothing (equal rank fails `>`). So the residue needs one
comparison, and it is **seat identity, not rank**:

```
# the `reaches` conjunct, in full (§A.6 is its home)
def reaches(w, via: Office, target: Office) -> bool:
    if target.id == via.id:        return False   # never the seat you are exercising
    if target.rung is None:        return False   # a seat with no ground is reached by nothing
    if via.rung is None:           return False   # a seat with no ground reaches nothing
    return target.rung == via.rung or target.rung in world_q.descendants(w, via.rung)
```

**What this buys over the rank conjunct, case by case** — and the third row is a genuine behaviour
change, declared:

| case | today (`highest_title_rank(actor) > title_rank(target.post)`) | under `reaches` |
|---|---|---|
| a Duke revoking **his own** ducal seat | refused (6 > 6 is false) | **refused** (`target.id == via.id`) — and now for the right reason |
| the Duke of Varfell revoking the **Duchess of Hafenmark**, holding Hafenmark | refused (6 > 6) | **refused** — `duchy_hafenmark ∉ descendants(duchy_varfell)`; they are siblings under the realm |
| a **Ducal Chancellor** at `duchy_varfell` revoking the **Duke of Varfell**, having the duchy in his holdings | refused (a non-title has rank −1) | ⭐ **ADMITTED.** Same rung → `reaches` is true; `revocation: holdings` then demands `in_holdings`, which he has. **A coup by landholding.** |
| the King revoking a Duke whose duchy he does **not** hold | refused (`in_holdings` fails) | **refused**, identically |
| a Cardinal at `terr_T9` revoking a hearth-scale seat inside T9 | refused (a Cardinal has rank −1, and `under_purview` is 0 for him) | **ADMITTED** if the target's basis is `purview` — which is §A.6's whole point |

⚠ **THE THIRD ROW IS THE ONE TO ATTACK, AND I AM RULING IT RATHER THAN HIDING IT.** The rank conjunct
was the code's own addition, and the code says so: `predicates.py:263-265`, *"Both terms, therefore,
plus rank: the whole point of 'they do not necessarily have sovereign power' is that holding the land
is not the same as outranking the person who governs it."* **Jordan's two sentences state purview and
holdings and never state rank.** Under `CLAUDE.md` §0's five-step gate, step 5 (*where 1–4 are silent
but one option is clearly right for the code*) takes the reading that keeps both stated conjuncts and
replaces the unstated third with a structural exclusion — **because the unstated third is a second
ladder over a quantity the first ladder already orders, which is `CLAUDE.md` §0.06's named `S` defect.**
And the game it produces is better, which is the NERS argument and not a tiebreak: **holdings become
dangerous.** A man who buys the duchy can unmake its Duke, which is precisely what *"governing
authority, sovereign power and holdings are three different things"* (`rosters.yaml:697-706`) is for.

⚠ **AND F.21 IS NARROWED, NOT CLOSED.** `ARCH F.21` reads: *"the rank of a cluster seat (`scope =
null`) | no rank; the loader forbids a `higher_rank` conjunct on one | church seats become revocable
by purview alone — which they also lack."* After §A.5.1 **no value set names a `higher_rank`
conjunct at all**, so the loader clause F.21 assumes is vacuous, and its consequence line is answered
by content (every seat gets a rung, §A.13) rather than by the conjunct. **That is not the same as
closing it:** F.21 is a ratified row that presupposes the conjunct exists, and gate 5 may not delete a
thing ratified canon names. **Filed as RR-B, second item (§C.9).**

### §A.5.2 · `term` IS NOT A FOURTH VALUE — and `ARCH §B.8` says so

Round one proposed `revocation ∈ {purview, purview+holdings+rank, none, term}` and graded `term`
CONFORMANCE on `ARCH §B.8`. **Read at the clause, it is the opposite.** `ARCH §B.8`'s `T-o` row:
*"⚠ **The basis resolves against the Seat** — `Seat.revocation` is authoritative and `term.closer`
names a basis, not a second authority (Stage 1 `§E.1.2` asks that this be said at both sites)."*

So a `term` is a property of the **Tenure** (`Tenure.term? (matures_at, declared_by : ActId, closer)`),
and its `closer` **cites** one of the three seat bases. A fourth value would put the term's existence
on the seat, where `ARCH §B.8` puts it on the edge — two homes for one fact, `AX` ID-2.

> **Struck and kept:** ~~`revocation ∈ {purview, purview+holdings+rank, none, term}`~~ →
> **`revocation ∈ {purview, holdings, none}`**. Four values become three, `rank` is derived (§A.5.1),
> and `term` moves to the edge where `ARCH §B.8` already put it.

### §A.5.3 · H-91 closes here, as round one closed it, and the closure is re-verified

`hole_register.yaml:1093` (H-91): `remit:revoke` NECESSARY per Part E against purview SUFFICIENT per
Jordan. Round one closed it at gate 5 and the closure holds, restated once because it is what makes
the three values safe: **`remit_acts` is the ACTOR's side** (*may this seat take this kind of act?*),
**the basis is the TARGET's side** (*what does emptying THIS seat require?*). Two conjuncts, two
owners, no over-refusal. Re-verified against the code: `resolve.py:52-57` (`_eligible`) reads
`off.remit_acts` for the actor; `predicates.py:234` reads `w.offices[obj].revocation` for the target.
**They already read different objects.** A seat whose basis is `none` is unrevocable however broad the
remit; a seat with a `purview` basis is unrevocable by someone whose remit lacks `revoke` however wide
the purview.

> ### **RULED: three values, one of them a two-term conjunction, the rank conjunct DERIVED from a
> structural guard, `term` on the edge, H-91 closed.** Cited to `ARCH §B.7` call 1, `ARCH §B.8`'s
> `T-o` row, Jordan's two rules at `rosters.yaml:719-723`, `world.py:197-221` + `:248-256` (the guard
> the proof rests on) and `data/rosters.py:465-472` (rank is the rung ordinal). **One declared
> behaviour change** (the coup by landholding) and **one narrowing that is not a closure** (F.21).

## §A.6 · PURVIEW IS `descendants`, AND THE REFLEXIVE CASE IS THE ONE THAT MATTERS

| candidate | who owns it? | verdict |
|---|---|---|
| `descendants(w, seat.rung)` alone, PROPER | the plan's §2.4 | **REFUSED, and this is a correction to my own spec.** `descendants` is proper (§A.5.1 step 3, verified by execution), so a seat at `duchy_varfell` would not reach **`duchy_varfell` itself** — and the office seated exactly there is the one thing every seat must reach. Measured: today's `under_purview` **is** reflexive — it returns `True` on the first loop iteration when `holding == seat` (`predicates.py:135-138`), which is why the King's purview count is **365** while `len(descendants(w, 'r_valoria'))` is **364**. The difference is exactly one rung: his own |
| `descendants(w, seat.rung) ∪ {seat.rung}`, minus the seat exercised | this file | ⭐ **EXTENSION, ADOPTED.** `reaches` as written in §A.5.1. Reflexive on the **rung**, exclusive on the **seat** — which is the only pairing that lets a Duke revoke his own chancellor and not himself |
| `ancestors_or_self` as well, so a subordinate may act upward | nothing | **REFUSED.** `test_purview_is_containment_and_stops_at_the_holders_own_domain` (`test_season_shape.py:4467-4469`) asserts the direction and gives the reason in its own message: *"the REALM is under the duke's purview — purview is reaching upward, so a duke could act on the king's domain."* Upward reach is `petition` (`02`), never purview |
| `under_purview` rewritten on `reaches`, with the disjunction over seats KEPT | `predicates.py:105-141` | **CONFORMANCE.** The comment at `:128-131` is load-bearing and survives: *"It is a DISJUNCTION over the seats: authority over a holding is authority from ANY title the actor holds. Taking the highest-ranked seat instead would be the same bug wearing a better argument."* **Until `Act.via` lands** (§A.10), `under_purview(w, actor, rung)` is `any(reaches(w, seat, target) for seat in seats_held(actor))`; **after** `via` lands it is `reaches(w, w.offices[a.via], target)` and the disjunction retires with the interim |
| `seats_held(w, actor)` replaces `titles_held(w, actor)` | this file | **EXTENSION, and it is a one-line change with a large consequence.** `titles_held` (`:144-154`) minus the `title_domain` filter at `:152` **is** `seats_held`: every live `hold` whose object is in `w.offices`. It is not a new helper — it is the existing one with a filter removed, and it keeps the docstring's own claim to be *"THE SINGLE OWNER of the question what does this person govern"* |

**The consequence, stated plainly because a test pins the opposite.** Deleting the post filter means
**an ordinary seat at the duchy reaches everything inside the duchy.**
`test_season_shape.py:4478-4480` asserts it must not, and names the fear:

> *"an ORDINARY office at the duchy confers purview over the settlement inside it — then rank is not
> part of the rule and any office-holder governs everything beneath them"*

**The fear is misdirected, and the answer is the two-sided eligibility model.** Purview says *the
seat's ground reaches here*. It does not say what may be done on that ground — **`remit_acts` says
that, on the actor's side, and the target's basis says it on the target's side.** A Dicastery clerk
seated at a duchy with `remit_acts: []` reaches 93 rungs and may take **no act at all** on any of
them, because `_eligible` (`resolve.py:52-57`) finds no matching remit. What today's post filter
actually does is stand in for a remit check it cannot see — and it does the job **wrong in the
direction that matters**, stripping sixteen of nineteen seats of purview over their own ground
(§0.2 pt 2). **A filter that silences 84% of the seats to prevent an over-reach that `remit_acts`
already prevents is not a safeguard; it is the defect.**

⚠ **And the clerk should not be seated at the duchy in the first place** — which is a CONTENT claim,
and it is §A.15's rule: *a seat's rung is the smallest rung containing everything the seat must reach,
never the largest its faction owns.*

> ### **RULED: purview is `reaches` — the seat's rung, its containment closure, and not the seat
> being exercised.** Cited to `ARCH §B.7` (MECHANICAL), `world_q.py:54-64` (the walk, shared with
> `01`'s REACH), `predicates.py:135-138` (today's reflexivity, measured as the 365/364 difference)
> and `test_season_shape.py:4467-4469` (the direction). ⚠ **Struck and kept from my own plan:**
> ~~*"Purview = `descendants(seat.rung)`"*~~ → **`descendants(seat.rung) ∪ {seat.rung}`, minus the
> seat exercised**, because proper descendants exclude the seat's own rung and that is where the
> subordinate seats sit. `SC-2` is the falsifier.

## §A.7 · THE TWO PREDICATES, REWRITTEN — line for line, and nothing else moves

**What changes is WHAT THEY READ, never WHAT THEY CHECK.** Both bodies keep their cardinality
clauses, their `or` disjunct and their payload guards; the diff is three reads.

```python
# loop/predicates.py  —  after
from ..data.rosters import CONFERRAL_BASES, RELEASABLE_KINDS, REVOCATION_BASES   # :27

def reaches(w, via, target) -> bool:            # NEW — §A.5.1's body, the single owner
    ...

def seats_held(w, actor) -> list:               # was `titles_held` (:144) minus the :152 filter
    return [w.offices[t.object] for t in w.tenures
            if t.kind == "hold" and t.subject == actor and t.live and t.object in w.offices]

def under_purview(w, actor, holding) -> bool:   # :105 — the DISJUNCTION survives (:128-131)
    return any(seat.rung is not None
               and (holding == seat.rung or holding in world_q.descendants(w, seat.rung))
               for seat in seats_held(w, actor))

@requires_predicate("confer")
def _req_confer(w, a) -> bool:
    ...                                          # :177-180 unchanged
    off = w.offices[obj]
    if off.conferral != "confer":                # was :181-182 — a TRUTHINESS test on a string
        return False                             #   now a VALUE test against a closed roster
    if not any(reaches(w, via, off) for via in seats_held(w, a.actor)):   # NEW conjunct
        return False                             #   the conferring seat must reach the conferred
    ...                                          # :183-192 unchanged (1-per-object and its disjunct)

@requires_predicate("revoke")
def _req_revoke(w, a) -> bool:
    ...                                          # :232-233 unchanged
    off = w.offices[obj]
    basis = off.revocation
    if basis == "none":                          # was :234-235
        return False
    if not any(reaches(w, via, off) for via in seats_held(w, a.actor)):
        return False                             # the `reaches` conjunct, both value sets
    if basis == "holdings" and not in_holdings(w, a.actor, off.rung):
        return False                             # the second conjunct, titles only
    return any(t.kind == "hold" and t.object == obj and t.live for t in w.tenures)   # :287 unchanged
```

| what goes | lines | what replaces it |
|---|---|---|
| the truthiness test on `conferral` | `:181-182` | a **value** test, `== "confer"`. `determine` and `succeed` refuse `confer` **by being other values**, not by a second branch |
| the truthiness test on `revocation` | `:234-235` | `== "none"` refuses; the other two values each name their conjunct set |
| **`target_is_title = title_domain(...)`** | `:252` | **deleted.** H-109 closes |
| the `if target_is_title:` branch and its three conjuncts | `:254-274` | two conjuncts selected by a value, and the rank one derived (§A.5.1) |
| the `elif not under_purview(...)` tail | `:275-276` | folded into the shared `reaches` conjunct |
| `titles_held`'s title filter | `:152` | deleted; the function becomes `seats_held` |
| `highest_title_rank` | `:157-163` | **deleted** (§A.5.1) |
| `_req_dispatch` | `:291-294` | **deleted with the verb** (`02` §f, under RR-A) |

**Three refusals GAINED, each naming what is missing** — because a predicate that refuses silently is
the defect `predicates.py`'s own module docstring exists about (*"A verb with a prose precondition and
no predicate here REFUSES, naming what is missing, rather than silently succeeding"*, `:33-36`):

1. **a `conferral` off the roster** → refused at **load**, in `Office.__post_init__`, not at act time.
2. **a seat with `rung = None`** → `reaches` returns `False` and the refusal says *this seat has no
   ground*, which is a content finding rather than a permission failure. Under §A.13 no such seat
   exists, so the clause is a guard on the content file and not a live branch.
3. **`via.id == target.id`** → *you may not revoke the seat you are exercising.*

> ### **RULED: two predicates, three value tests, one shared `reaches` conjunct, and the `is_title`
> branch gone.** Cited to `ARCH §B.7` call 1 (*"No `is_title` branch exists anywhere — ID-4"*),
> `AX` ID-4 (`AX:443`, *"Declare, don't route"*) and `hole_register.yaml:1520` (H-109). **`H-109`
> closes by design, no ruling.** The predicates' own docstrings — which record two historical
> over-refusals and one over-admission — are **kept verbatim**, because they are the argument for
> every clause the rewrite does not touch.

## §A.8 · `Office` AS THE SCHEMA — field by field, against `__post_init__` as built

`carriers.py:479-548`, opened. Thirteen fields; **eight have zero readers outside `carriers.py` and
the tests** (measured, §0.2).

| field | line | type | readers | disposition |
|---|---|---|---|---|
| `id` | `:483` | `str` | everywhere | **keep** |
| `post` | `:484` | `str` | `__post_init__:536,546`; `_req_revoke:252`; `titles_held:152`; display | **keep as a NAME from which nothing is inferred.** All four mechanical readers are deleted by this file, which is what makes the `AX` ID-4 claim true rather than aspirational |
| `rung` | `:485` | `Optional[str]` | `_req_revoke:253`; `titles_held:152`; `conferral_path:430` | **keep, and REQUIRE it** (§A.13). The `Optional` stays in the dataclass — `ARCH §B.7`'s `scope? (null = a cluster)` is ratified — and the **content file** forbids null, which is the right layer for a content rule |
| `remit_acts` | `:486` | `list[str]` | `resolve.py:56`; `epistemic.py:360` | **keep.** The only field with two live readers, and both are eligibility |
| `scope_rung` | `:487` | `Optional[str]` | **0** | **DELETE.** Set by `__post_init__:546-548` from `rung` for titled posts and read by nothing. A second scope field, which §A.2 refuses |
| `binds` | `:488` | `str` | **0** | **DELETE.** `"members_by_admission"` on 19 of 19 — the dataclass default and its only occurrence. `AX` ID-13 (`AX:489`) calls this *"not a weak field but one that does not exist, wearing a schema's clothes"*. ⚠ **`ARCH F.17`'s own default names it** — *"`oblige`'s `requires` reads the seat's `binds`"* — so §A.9 must answer F.17 **without** it, and it does |
| `conferral` | `:489` | `Optional[str]` | `predicates.py:181` | **keep; make it a ROSTER member and required** |
| `revocation` | `:490` | `Optional[str]` | `predicates.py:234` | **keep; make it a ROSTER member and required** |
| `establishment` | `:491` | `list[str]` | `world_q.py:413` | **DELETE** (§A.9). `ARCH §B.7` call 2 |
| `dates` | `:492` | `list[str]` | **0** | **DELETE.** Every one of the 13 `.dates` hits in `engine/season/**/*.py` is `w.dates` or `self.dates`, the World's dict — **not one is `Office.dates`**. ⚠ **RR-B: `ARCH §B.7`'s `Seat :=` line spells `dates[]`** |
| `upkeep` | `:493` | `Any` | **0** | **DELETE.** ⚠ **RR-B: the `Seat :=` line spells `upkeep`**, and `ARCH F.18` (upkeep's source) **stays open** — deleting a field with no readers answers no economic question (§0.1) |
| `body` | `:500` | `Optional[str]` | `__post_init__:528,530,536`; `office_faction` | **keep.** One authored field, two derived — the shape `data/rosters.py:408-420` argues for |
| `faction` | `:501` | `Optional[str]` | derived at `:528` | **keep, derived** |
| `body_function` | `:502` | `Optional[str]` | **0** | **keep anyway, and say why.** Derived at `:530` from `BODY_FUNCTION`, so it is a **cache of a roster read**, not a second home for a fact; deleting it saves nothing and the derivation is one lookup. Round one's list had it as a deletion; **struck**: ~~`body_function` (0 readers, delete)~~ → **kept as a derived cache**, and `05`'s ledger carries the count difference |

**`__post_init__` (`:504-548`), clause by clause, and what this file does to each:**

| clause | lines | raises | disposition |
|---|---|---|---|
| **remit acts off the closed roster** | `:508-512` | `Unowned`: *"office `<id>` claims remit acts not on the roster: `[…]`"* — **verified by construction** with `remit_acts=['issue','tax']` | **KEEP, and COPY its shape** for `conferral` and `revocation`. Its own law line is the argument: *"a typo here would mint a remit act and every `remit:<that act>` eligibility would silently never match — a verb quietly unavailable to everyone, which is the worst shape a failure can take"* |
| **the faction axis** | `:528` | `office_faction` raises `Unspecified` for an unknown body, `Forbidden` for a body/faction mismatch, `Unspecified` for neither — **all four verified by construction** (§A.15) | **KEEP untouched.** This is the clause that makes `offices_draft.yaml` uncopyable |
| **`body_function` derivation** | `:529-530` | `KeyError` on a body absent from `BODY_FUNCTION` — unreachable, since `:528` already refused it | keep |
| **title + body → `Forbidden`** | `:536-543` | *"office `<id>` names the TITLE `'King'` and the body `'Inner Circle'`"* — **verified by construction** | ⭐ **RE-HOME, DO NOT DELETE.** It calls `title_domain`, which this file deletes. The invariant is real and canon's: *"the overlay `{post: "King", body: "Cardinal of Justice"}` was ACCEPTED before this check and produced a realm title whose Church affiliation existed nowhere in canon."* **Re-homed as a CONTENT rule** in `offices.yaml`'s loader: a seat whose `post` is a member of `titles.domains` may not name a `body`. Same refusal, same law string, read from the roster at load instead of through a helper |
| **`scope_rung` defaulting** | `:546-548` | — | **DELETE with the field.** Its purpose was *"a Duke seated at the realm has realm-wide purview"*, and §A.13 answers that by content: a titled post's rung must be of the kind its title governs, checked at load |

> ### **RULED: five fields deleted, one derived cache kept against round one's list, two constructor
> clauses re-homed rather than removed, and the remit refusal's SHAPE copied to the two new
> rosters.** Cited to `ARCH §B.7`'s `Seat :=` line (RR-B for `upkeep` and `dates[]`),
> `ARCH §B.7` call 2 (`establishment`), `AX` ID-13 (`AX:489`, `binds`) and the measured reader counts
> of §0.2. ⚠ **Struck from round one:** ~~`Office.{establishment, upkeep, dates, scope_rung, body_function, binds}` — six deletions~~
> → **five deletions**, `body_function` kept as a derived cache.

## §A.9 · ESTABLISHMENT IS A QUERY OVER `oblige` — and F.17 closes without a sixth remit act

`ARCH §B.7` call 2, verbatim: *"**`establishment` is a Query over `oblige`, not a field.** A set of
persons on a seat is two homes for one fact. A person joins by `oblige : Person → Seat` and leaves by
`release`. A council is one seat whose members oblige. **Rejected:** the chain's field, with
*establishment size* as a number nobody can source."*

| candidate | who owns it? | verdict |
|---|---|---|
| the field, read at `world_q.py:413` | `carriers.py:491` | **CONFORMANCE: delete.** Measured `[]` on 19 of 19, so the one reader returns `[]` for every seat in the world — a Query over nothing |
| `establishment_of(w, office_id)` over live `oblige` tenures | `ARCH §B.7` call 2 | ⭐ **CONFORMANCE.** The function stays at `world_q.py:399-413`; its body becomes `[t.subject for t in w.tenures if t.kind == "oblige" and t.object == office_id and t.live and t.subject in w.persons]`. **Same signature, same caller, same name** — so this is a body change, not a new object |
| `oblige`'s `requires` reads the seat's `binds` | **`ARCH F.17`'s own assumed default** | **REFUSED, and the refusal is why F.17 closes cheaply.** `binds` has 0 readers and one value on 19 of 19 (§A.8), so reading it would give the same answer for every seat in the world. F.17's stated cost — *"if admission is a seat's own act, the closed remit roster **needs a sixth member — a ruling, not a row**"* — is avoided by making admission the **joiner's** act, not the seat's |
| `_req_oblige`: the actor may oblige to a seat that reaches where he stands | this file | ⭐ **EXTENSION.** `oblige` is `own`-eligible already (`verb_table.yaml:377`), so **no remit act is needed and the roster does not move.** The precondition is the seat exists, its `rung` reaches the actor's containing rung (`reaches`, with the actor's rung in place of a seat), and no live `oblige` from this actor to this seat |
| `@effect_for("oblige")`: mint the Tenure the row already declares | `verb_table.yaml:379` (`writes: ["Tenure.since"]`) | ⭐ **EXTENSION**, and it is a body for a row that exists — the cheapest kind of addition. ⚠ **`_eff_oblige` was WRITTEN AND REVERTED once** (`ED-IN-0211`, recorded at `predicates.py:212-218`) *"for opening a Tenure to `einhir_texts`, a bare string naming no entity, because an OPENER takes an id and asserts a relation into existence."* The re-build must take the id from the payload and refuse a non-office: that is `_req_oblige`'s job, and the reversion is the reason it has one |

**A council is then one seat and its bench is a Query** — `AX §E.2.5` (`AX:1477`), verbatim: *"a
council | **one seat, many holders** | ⚠ **not N seats.** `hold` is **1-per-object** (§D.8), so a
council is **one seat whose membership is a Query over `oblige`**."* Enforced in code already:
`world_q.hold_force` raises on a second live `hold` (`world_q.py:138-144`). **This file uses that
shape once in its content** — the Restoration Movement's second leader obliges to the first's seat
rather than holding a second seat (§A.16, row 29) — so the mechanism ships with a live instance
instead of an empty roster.

> ### **RULED: the field dies, the Query keeps its name and signature, admission is the joiner's
> `own` act, and `ARCH F.17` closes with no sixth remit act.** Cited to `ARCH §B.7` call 2,
> `ARCH F.17` (whose default is refused on a measured 0-reader field), `AX §E.2.5` (`AX:1477`),
> `holonic §15`'s `oblige : Person → Person | Office, many`, `verb_table.yaml:375-383` and
> `world_q.py:138-144`. **F.17 closes by design, no ruling.**

## §A.10 · `Act.via` — POSITION 6, AND THE INTERIM IS NAMED WITH ITS RETIREMENT

`Act.via` is **not this file's to land.** It is position 6 of the ratified program
(`workplans/2026-09-11-reconciled-program_part2.md:239`, *"G3 — `NotYours` at the gate, `Act.via`,
purview through `via.scope`"*), whose INSTRUCTION already names this file's two predicates: *"Re-point
`loop/resolve.py`'s `_eligible` `remit:` branch, `under_purview`, `_req_revoke` and `_req_confer` from
the actor's own `hold` tenures to `via.scope`."*

| candidate | verdict |
|---|---|
| this file lands `Act.via` | **REFUSED.** Position 6 owns it, the ratified ORDER is ratified (`workplans/2026-09-11-reconciled-program.md:3`, scoped to *"§3's ORDER"*), and `ARCH §C.2` F3's gate branch is authored **there or twice** — `_part2.md:249-250`: *"Write it here or it is written twice"* |
| this file ships the interim: **the disjunction over seats held** | ⭐ **EXTENSION, and it is what `_eligible` already does.** `resolve.py:52-57` scans the actor's live holds for a matching remit; §A.7's `any(reaches(w, via, off) for via in seats_held(w, a.actor))` is the same scan one column along. **No new mechanism, and the seat is still the thing asked** — it is asked over every seat the actor holds instead of over the one he declared |
| the interim is equivalent | **REFUSED, and the inequivalence is the point.** The disjunction admits a **regent** only if the regency is itself a seat he holds — which §A.13's content makes true for the Widow Regent — and it cannot express *"I act as the Duke's deputy today and as myself tomorrow"*. `hole_register.yaml:1508` (H-108) states the general failure: *"authority is read off the ACTOR and delegation is unbuildable here."* **The interim narrows H-108; it does not close it** |

⚠ **AND THE `from` OPERAND IS A SEPARATE, MEASURED LIMIT.** `02` §execution notes that `transfer`
binds `from` to `containing_rung_of(p)` (`options.py:316-317`), and the plan's §2.4 concludes *"which
is why office-holders are SEATED at their seat's rung."* **Measured, that conclusion does not survive
contact with the world:** 0 of 19 holders are seated at their seat's rung and all 19 are in a
`hearth` (§0.2 pt 3). Moving a Duke's `contain` edge onto `duchy_varfell` would take him out of every
larder (`matter.py:169`'s `presence`) and out of every co-location channel at his own court. **So this
file does NOT move any person**, and rules instead:

> **A seat-borne act draws on the SEAT's rung, and that is `Act.via`'s job, not `contain`'s.** Until
> position 6 lands, `from` stays `containing_rung_of(p)` and a levy or transfer taken through a seat
> draws on the holder's own hearth. **That is a LIMIT, stated, and it is the second thing position 6
> pays for.** What §A.14 requires instead — and can require today — is that a holder **live inside
> the closure of the rung he governs**, which costs no person a move for 17 of 19 and is measurably
> false for 2 (§0.2 pt 3).

> ### **RULED: `Act.via` stays at position 6 of the ratified order; this file ships the disjunction
> as a NAMED interim, with its retirement written.** Cited to `_part2.md:239-266`,
> `workplans/2026-09-11-reconciled-program.md:3`, `hole_register.yaml:1508` (H-108) and
> `resolve.py:52-57` (the same scan, already shipped). **H-108 is NARROWED, not closed, and this
> file says so.**

## §A.11 · THE COMMISSION — H-71 closes on BOTH sides, and they are allowed to disagree

`H-71` (`hole_register.yaml:795-808`), verbatim: *"§F1 clause 2 says eligibility is evaluated
PERSON-SIDE, and `remit:<act>` CANNOT BE. The person owns the `hold` Tenure; the OFFICE owns the
remit."* The decline is `options.py:163-165`, and its `TRACE.note` names the row.

| candidate | who owns it? | verdict |
|---|---|---|
| widen `choose`'s signature to take a `World` | — | **REFUSED, structurally.** `ARCH §C.3`: `decision/` *"does not import `state/`, `world_q` or `loop/`"*, and `ARCH §A.3` row 1 gives the reason: *"the only thing making no World in scope checkable by path rather than by reading bodies"* |
| the grant on `Tenure.payload` | the 2026-09-16 sweep | **REFUSED — retired.** `ARCH §B.8`: `term?` *"Replaces payload?"*, and the matrix row `(Tenure, payload)` (`write_matrix.yaml:336-342`) is on `05`'s deletion list |
| the grant on `Tenure.conferrer` | round one's carrier candidate | **REFUSED — deleted by `ARCH §B.8`** in terms: *"`conferrer? : SeatId` IS DELETED — `ID-13` ADMITS NO THIRD STATE, AND THIS FIELD HAD NO READER ANYWHERE IN THIS EXERCISE."* |
| **a `commission` Record, held by the conferee, whose held content becomes a claim** | this file, with `02` owning the deposit rule | ⭐ **EXTENSION, ADOPTED** |

**The mechanism, as execution, in four steps that each already exist:**

1. **`_eff_confer` (`effects.py:92-126`) also mints a Record.** It already opens the conferee's `hold`
   (`:120-121`); `_eff_create_record` (`effects.py:262-290`) already shows the pattern — write the
   Record, then `w.add_tenure(Tenure(H(...), a.actor, rid, "hold", since=w.tick))` at `:287-289`.
   `_eff_confer` mints `Record(rid, rung=off.rung, kind="commission",
   subject_matter={"seat": off.id, "to": to})` and the conferee's hold on it. **The effect returns a
   per-kind mapping** (`:126`, `{"tenure.opened": [...], "tenure.closed": [...]}`) and gains a
   `record.exists` key — the contract `:97-101` states and the docstring warns about (*"an effect
   mutates and returns the ids it touched; it does not call `w.write`"*).
2. **WITNESS deposits a content claim.** `02` owns the rule; this file states only what it needs:
   `Claim(holder=p, subject=R.id, predicate="content:commission", value=copy(R.subject_matter),
   source="firsthand")`. ⚠ **This is a NEW claim SHAPE on an existing channel, and round one called it
   a ride** — the audit's limit 8 is correct and verified here: the deposit's predicate is the **event
   kind** (`witness.py:191`, `Claim(cid, pid, subj, e.kind, True, w.tick, src, conf, "own", self.round)`),
   so nothing today mints *S's remit contains X*. **Counted as the addition it is**, in `05`'s ledger.
3. **`person_side_eligible`'s `remit:` branch reads the claim.** `options.py:163-165` becomes: *the
   actor's ledger carries a live `content:commission` claim whose value names a seat, and that seat's
   `remit_acts` contains the act.* ⚠ **The seat's remit must be IN the claim's value**, not looked up
   — `decision/` may not reach `w.offices`. So the commission's `subject_matter` carries
   `{"seat": <id>, "to": <pid>, "remit": [<acts>]}`, a snapshot at conferral. **That snapshot going
   stale is the mechanism, not a bug:** a seat whose remit is later narrowed leaves its holder
   believing he may still act, and RESOLVE refuses him.
4. **RESOLVE keeps asking the world.** `_eligible` (`resolve.py:52-57`) is untouched: it scans live
   holds and reads `off.remit_acts` from the World.

**The gap between the two readings is the mechanism, and it runs both ways** — round one's table,
re-verified against the code and kept:

| the belief says | the world says | what happens | the code |
|---|---|---|---|
| permitted | permitted | the act resolves | — |
| permitted | forbidden | **refused**, and `emits_on_refusal` fires — *so he learns* | `verb_table.yaml:151` (`confer.refused`), `:476` (`revoke.refused`) |
| forbidden | permitted | **he never tries, and nobody ever learns.** A struck seat goes on governing because its holder still believes in it | no mechanism needed — the candidate is never formed |
| forbidden | forbidden | nothing, correctly | — |

**Row 2 is where a forged commission lives.** `forge` (`verb_table.yaml:247`) writes
`Record.forgery_quality` (`carriers.py:428`); the holder deposits a `content:commission` claim in good
faith by the same deposit rule, attempts the act, and **RESOLVE refuses it because RESOLVE asks the
seat.** No special case, no forgery branch in the predicate.

**And this is what makes H-71 close on BOTH sides rather than one.** `AX-2` (`AX:100-110`) is honoured
rather than dodged: *"A person decides from what they hold, and what they hold may be false. There is
no view of world truth available inside a decision — not capped, not filtered: **absent**."* A claim
about a seat **is** the person's own state.

> ### **RULED: the grant is a CLAIM about a HELD DOCUMENT, and H-71 closes on both sides.** Cited to
> `AX-2` (`AX:100-110`), `ARCH §C.3` (no World in `decision/`), `ARCH §B.8` (no payload, no
> conferrer), `effects.py:287-289` (the mint pattern), `witness.py:191` (the existing deposit, whose
> predicate is `e.kind` — **the new shape is counted**) and `hole_register.yaml:795` (H-71).
> ⚠ **Dependency declared:** the `commission` kind needs `02`'s `record_kinds` roster, which does not
> exist (`grep record_kinds engine/` → 0). **This file cannot close H-71 alone**, and `05`'s build
> order sequences it.

## §A.12 · WHAT DIES WITH THE TITLE FAMILY — and one Query nobody has noticed

| thing | where | why it dies |
|---|---|---|
| `title_domain`, `title_rank` | `data/rosters.py:459,465` | §A.3. The `titles` **roster** (`rosters.yaml:692-766`) **STAYS** — it is canon's ladder, Jordan's verbatim ruling, and the content file reads it to check that a titled post sits at a rung of the kind its title governs (§A.13) |
| `titles_held`, `highest_title_rank` | `predicates.py:144,157` | §A.3. `titles_held` is **renamed and narrowed**, not deleted, so `05`'s ledger counts one deletion and one rename, not two deletions |
| the `is_title` branch | `predicates.py:252-276` | §A.7. **H-109 closes** |
| `_req_dispatch` | `predicates.py:291-294` | with the verb, under `02`'s RR-A |
| `Office.{scope_rung, binds, establishment, dates, upkeep}` | `carriers.py:487-493` | §A.8 |
| `Office.__post_init__`'s `scope_rung` default | `carriers.py:546-548` | §A.8, with the field |
| ⭐ **`world_q.conferral_path`** | `world_q.py:416-436` | **NEW FINDING (§0.2 pt 6): zero non-test callers, and it never reads `conferral`.** Its docstring announces the field and its body reads `off.rung`, so it is a containment walk wearing a governance name. **`descendants`/`parent_of` already own that walk** (§8: one rule, once). Its one caller is `test_season_shape.py:11071`, which asserts it *"starts at its own rung and climbs"* — a property of `parent_of`, tested through a wrapper |
| `harness/populated.py`'s title inference | `:75, :671` (`governs = title_domain(title) if title else None`) | §A.13. The content file **declares** the rung; nothing infers it from a name |

**What is NOT deleted, and the list matters because a session reading "the title family goes" would
over-reach:**

- **`rosters.yaml: titles`** (`:692-766`) — canon. Jordan's three-concepts note (`:697-706`) and his
  two revocation rules (`:719-723`) are the design's own record of what the values mean.
- **`in_holdings`** (`predicates.py:60-104`) — the `holdings` conjunct's only reader, and its
  docstring is Jordan's ruling made mechanical.
- **`under_purview`** (`:105-141`) — rewritten on `reaches`, name and signature kept, **and its
  disjunction comment (`:128-131`) kept verbatim** because it records a bug this rewrite could
  reintroduce.
- **`RUNG_KINDS`** (`rosters.yaml:106-109`) — the one ladder, now the only one.

> ### **RULED: nine named things die, four named things stay, and one of the nine is a Query nobody
> had measured.** Cited to the grep of §A.3, the reader counts of §0.2, and `world_q.py:416-436`
> opened. `05`'s ledger is the single owner of the count; this section is its evidence.

---

## §A.13 · `offices_draft.yaml` CANNOT BE COPIED — measured, row class by row class

`proposals/2026-09-16-term-ownership/offices_draft.yaml`, 570 lines, `## meta.authority:
"TRANSCRIBED FROM CANON 2026-09-13. Not authored. Every row cites its source."` **It is a good
document and it is not a content file, and the difference is measured rather than asserted.**

**Command:** `python -c "import yaml; d=yaml.safe_load(open('proposals/2026-09-16-term-ownership/offices_draft.yaml')); …"`

```
570 lines · 188 rows = 178 leaf data rows + 10 container headers
  ladders        4 headers + 47 standings/branches
  sub_ladders    6 headers + 42 standings
  bodies        36
  seats         25          <- 13% of the rows, and the only ones an Office can be built from
  titles         4
  holdings       6
  unsourced     18
seats field union: [body, case, faction, holder_name, ladder, note, post, rung_kind, source, standing, tier]
  seats missing `id`:          25 of 25
  seats missing `remit_acts`:  25 of 25
  seats with `conferral`:       0 of 25
  seats with `revocation`:      0 of 25
  seats with a `rung_kind`:     2 of 25  (both `province`, of which the world has ZERO instances)
  seats with a `body`:         15 of 25
Office(...) constructed for each of the 25 against today's rosters:
  CONSTRUCTS                 10
  Unspecified (body off the live `office_bodies` roster)   14
  Unspecified (faction off the live `factions` roster)      1
bodies rows against the live roster:  9 on it, 27 NOT on it
```

⚠ **THREE OF MY OWN SPEC'S NUMBERS WERE WRONG AND ARE REPAIRED HERE** (`CLAUDE.md` §0.1 pt 3 — the
support, not the claim, is the thing to check):

| my spec said | measured | the repair |
|---|---|---|
| ~~*"13 of 14 body-bearing seats name a body absent from the live `BODY_FACTION` roster"*~~ | **15** seats carry a body; **14** name an absent one; exactly **one** (`Grand Master (Großmeister)`, body `Lions' Table`) is on the roster | **14 of 15** |
| ~~*"26 of its 36 `bodies:` rows are non-canonical"*~~ | **27** of 36 | **27 of 36** |
| ~~*"would raise `Unowned`"*~~ | `require_member` raises **`Unspecified`** (`data/rosters.py:299-302`); `Unowned` is what `Office.__post_init__:510` raises for a bad **remit act** | **`Unspecified`**, and the two exception classes matter because a loader that catches the wrong one passes the row |

**And the 27 off-roster bodies decompose exactly, which is the finding that makes the derivation
simple:** `engine/season/rosters.yaml:1035-1040` **names and declines 22 of them by number**, verbatim:

> *"⚠ ONLY THREE ARE ADDED, AND THE RESTRAINT IS THIS FILE'S OWN PRECEDENT. `faction_politics_v30`
> PART 7 names **22 more organs** with quoted jurisdictions — six Crown ministries, six Hafenmark
> committees, four Church dicasteries, five Varfell councils. NOT ONE IS READ by anything that builds
> a world … Adding the other 22 would repeat `governance_modes` and `power_bases`, deleted from this
> file for exactly that — 'not wrong; UNREAD', and §0.1 pt 5 forbids apparatus that is load-bearing on
> nothing. **They go in the day a seat needs one.**"*

`27 = 22 declined organs + 5 SPELLING VARIANTS of rows already on the roster` — measured:
`Fortitude (Military Arm)` → `Cardinal of Fortitude`, and likewise Justice, Prudence, Temperance;
`Ministries (general)` → `Ministries`. (The draft's seven Crown ministries against the note's "six" is
`Hochschule`, a seventh the note did not count; `7+6+4+5 = 22`.)

**So the roster's own sentence is the derivation rule**, and it is the opposite of a copy: a body
enters `office_bodies` **because a seat needs one**, one at a time, with the seat.

### §A.13.1 · What transfers, what is dropped, what must be authored fresh

| row class | n | disposition | reason, cited |
|---|---|---|---|
| `ladders:` standings | 47 | ⛔ **DROPPED ENTIRELY** | a standing ladder is a **faction-standing** model, not a seat. Nothing in `engine/season/` reads a standing; `rosters.yaml` has no `standings` roster. Transcribing it would be `governance_modes` again |
| `ladders:`/`sub_ladders:` headers + branches | 10 + ~14 | ⛔ **DROPPED** | same |
| `sub_ladders:` standings | 42 | ⛔ **DROPPED** | same |
| `bodies:` on the live roster | 9 | ✅ **ALREADY LIVE** — transfers as a no-op | `rosters.yaml:1004-1040` |
| `bodies:` off the roster, needed by an authored seat | **5** | ⚠ **AUTHORED FRESH into `rosters.yaml: office_bodies`**, one per seat that needs it, with `faction:` and `function:` quoted from the source the draft cites | the roster's own *"they go in the day a seat needs one"* (`:1040`) |
| `bodies:` off the roster, needed by no authored seat | **22** | ⛔ **DROPPED** | `§0.1 pt 5` via the roster's note: apparatus load-bearing on nothing |
| `seats:` | 25 | ⚠ **12 transfer their POST and BODY only; 9 are authored fresh; 4 are dropped** — §A.13.2 | every one is missing `id`, `remit_acts`, `conferral`, `revocation` — **four of the seven fields `offices.yaml` needs** |
| `titles:` | 4 | ⚠ **3 transfer** (King NPC-020, Duke of Varfell NPC-052, Duchess of Hafenmark NPC-050 — all three already live); **1 is authored fresh** (Confessor NPC-021, whose `governs: "ecclesiastical institution"` is **not a rung kind**, so the rung is authored not transferred) | measured: all four `case` ids resolve in the 46-row cast |
| `holdings:` | 6 | ⚠ **16 of 17 territory rows are ALREADY LIVE** as faction→territory `hold` Tenures; the 17th names `Uncontrolled` (Askeheim/T15), **which is not a faction** and so cannot hold anything | measured: the 16 live rung-holds are exactly Crown 6 · Varfell 4 · Hafenmark 4 · Church 1 · Schoenland 1; the draft adds `Uncontrolled: [Askeheim (T15)]` |
| `unsourced:` | 18 | ⛔ **DROPPED as content; READ as a warning list.** Three of the eighteen are live hazards for this file: the Niflhel strike, the `MIN-01..06` absence, and the two `§3.5` stale post-rename labels | `rosters.yaml:70-73` already carries the Niflhel and `People's Revolution` exclusions |

**Net: of 178 leaf rows, 44 inform `offices.yaml` and 134 are dropped.** The draft reads as a 570-line
roster and yields **44 usable rows**, of which **25 supply at most three of seven required fields**.

### §A.13.2 · The 25 `seats:` rows, adjudicated — and five of them are SUPERSEDED

⚠ **THE SUPERSESSION IS THE FINDING MY SPEC NAMED AND IT IS WORSE THAN "TWO COUNTS".** The draft's
Hafenmark block is headed `# ===== HAFENMARK INNER CIRCLE (§1.2c) =====` (`:316`) and its Varfell
block `# ===== VARFELL INNER CIRCLE (§1.3c) =====` (`:365`) — **four rows and five rows from
`faction_politics_v30.md` §1.2c/§1.3c.** `engine/season/rosters.yaml:58-67`, the precedence header,
verbatim:

> *"TIER 2a · `systems/npcs/reference/npc_behavior_v30.md` **SUPERSEDES**
> `systems/factions/reference/faction_politics_v30.md`. ⭐ RULED by Jordan, **2026-09-13**, verbatim:
> *"NPC behaviour supersedes faction politics."* It was asked because the two disagree about WHO SITS
> IN A FACTION'S INNER CIRCLE, by half: politics §1.2c gives Hafenmark **four** named and §1.3c gives
> Varfell **five**; behaviour §2.16/§2.17 give **TWO and TWO**, dropping **Almstedt, Feldhaus,
> Thorvald Hann, Maret Uln and Edeyja**."*

**All five dropped names are seats in the draft** — measured against the `holder_name` column:
Peder Almstedt (`Senior Parliamentary Chair`), Annika Feldhaus (`Guild Comptroller`), Thorvald Hann
(`Senior Jarl of the Eastern March`), Maret Uln (`Vaynard's Huscarl Captain`), Edeyja
(`Warden Liaison`). **The draft's own `meta` dates it 2026-09-13 — the same day as the ruling** — so
it transcribed the superseded section and the ruling landed beside it.

**And the live roster already builds to the ruling**, which is why this costs nothing to honour:
`rosters.yaml:1067-1069` — *"`Inner Council`: Inner Council (**2 named** per npc_behavior §2.16). The
Duchess's standing council; **§1.2c names four and is SUPERSEDED** (Jordan, 2026-09-13)"*, and the same
for `Jarl Council`.

| the 25 rows, by fate | n | rows |
|---|---|---|
| **transfer post+body, already seated** | 12 | Royal Marshal (036) · Lord Treasurer (037) · Spymaster (033)\* · Archbishop's Rep (034)\*\* · Guard Captain (035) · Heir Apparent (031) · Senior Parliamentary Chair (008)\*\*\* · Baralta's Legal Advisor (071) · Military Commander HM (072) · Senior Jarl West (073)\* · Skald-Chief (074)\* · Cardinal of Justice (038)\* |
| **authored fresh from a draft row** | 9 | Lord Steward (009) · Cardinal of Fortitude (040) · Cardinal of Prudence (013) · Cardinal of Temperance (039) · Senior Inquisitor (004) · Grand Master (070) · Guild Comptroller (007)† · Restoration Leader (003) · Restoration secondary (041)‡ |
| ⛔ **DROPPED** | 4 | Senior Jarl of the **Eastern** March (`case: null` — **no person in the 46-row cast**; the draft's own note: *"the 46-case NPC corpus has no 'Thorvald Hann'"*) · Vaynard's Huscarl Captain (Maret Uln — superseded, and a personal retainer is an occupation not a seat) · Warden Liaison (Edeyja — superseded, and *"appears in Inner Circle only on Path B, WR ≥ 3"*, a conditional seat) · Warden-Chief (Edeyja again — `faction: "independent (Southernmost)"`, **not on the live `factions` roster**, verified: raises `Unspecified`) |

\* the draft's **body is off-roster** and the live body is kept: `Schattendienst`→none (faction Crown);
`Council of the Highlands`→`Jarl Council`; `Council of the Skald`→`Jarl Council`;
`Dicastery for Doctrinal Adjudication`→`Cardinal of Justice`.
\*\* **CONFLICT, adjudicated:** the draft says `faction: Crown`, the live build derives
`Church of Solmund`. The post names an Archbishop; the registry row names a dual loyalty
(`harness/populated.py:705-708` records it: *"`dual-loyalty: Crown Inner Circle agent…` (NPC-034)
resolve to nothing and keep `body=None`, which is honest"*). **The live derivation wins** (gate 4,
precedent: the tree already decided this row), and the draft's reading is recorded here, not dropped.
\*\*\* **DOUBLY SUPERSEDED, and the live post wins.** The draft's own note records an unresolved
conflict — *"npc_roster_v30.md:102-109 … describes NPC #8 as a 'Ministry Bureaucrat' / 'Chief
Parliamentary Clerk' … its own summary table lists his faction as 'Ministry', not Hafenmark. The two
canonical-status documents disagree … the conflict is not resolved"* — **and** Almstedt is one of the
five the 2026-09-13 ruling drops from Hafenmark's council. So `offices.yaml` keeps the live
`Chief Parliamentary Clerk` / `Ministries` / Crown, which is the reading both surviving sources allow.
† **DERIVED, and flagged for attack:** the ruling drops Feldhaus from Hafenmark's **council**, not
from the world; her registry primary role is *"Guilds Representative"* and the draft's own note says
*"Primary npc_roster_v30 role (#7) is 'Guilds Representative', not Hafenmark-specific."* Seated on
`Guild` (**on** the live roster, faction `Guilds`). **§D `SC-7` is its falsifier.**
‡ **NOT a seat — an `oblige` obligee** of the Restoration leader's seat, which is `AX §E.2.5`'s
council shape used once so the mechanism ships with a live instance (§A.9).

**And four LIVE seats have no draft row at all** — measured: NPC-030 (Princess), NPC-032 (Queen /
Widow Regent), NPC-081 (Commune Representative, `proposed`), NPC-082 (Military Jarl, `proposed`).
**They are kept**, because the draft's silence is not a deletion: the two `proposed` rows are
`harness/populated.py:718-724`'s declared marginal call, and the two Royal Family rows are the
succession seats `:688-691` argues for.

> ### **RULED: the draft is a SOURCE, not a file. 44 of 178 rows inform `offices.yaml`; five seats are
> SUPERSEDED by a ruling dated the day the draft was transcribed; 15 of 25 seats cannot construct
> against today's rosters; and not one of the 25 supplies more than three of the seven fields.**
> Cited to the measurements above (each with its command), `rosters.yaml:58-67` (the 2026-09-13
> ruling), `rosters.yaml:1035-1040` (the 22 declined organs), `rosters.yaml:1067-1069` (the roster
> already builds to the ruling) and `data/rosters.py:408-453` (the four refusals, each verified by
> construction). **A copy would have imported five superseded seats, 22 organs the tree names and
> declines, and fifteen construction failures.**

## §A.14 · `offices.yaml` — THE SCHEMA, FIELD BY FIELD, AGAINST `Office` AS BUILT

`engine/season/data/offices.yaml` — **world-gen content, read by `harness/populated.py`**, living
beside `rosters.yaml` and `fixtures.py` under `engine/season/data/` because that is where a fact code
reads at build time lives (`CLAUDE.md` §0.05 clause 1: the head of a fact code reads is YAML, never
prose).

```yaml
meta:
  source: "engine/season/data/offices.yaml -- the 29 seats of the built realm."
  derivation: "proposals/2026-09-16-term-ownership/offices_draft.yaml, per 03_SEATS_AND_CONTENT §A.13"
  rule: "one seat = one row. Seven required fields. No row may be added without a canon citation."

seats:
  - id:          off_king                  # REQUIRED, unique, `off_<slug>` -- Office.id
    post:        "King"                    # REQUIRED -- Office.post. A NAME. Nothing is inferred.
    rung:        {realm: true}             # REQUIRED -- an ANCHOR, resolved at load. Never an id.
    body:        null                      # OPTIONAL -- must be a member of `office_bodies`
    faction:     "Crown"                   # REQUIRED IFF body is null -- a member of `factions`
    remit_acts:  [issue, determine, confer, revoke, convene]   # REQUIRED, may be []
    conferral:   succeed                   # REQUIRED -- a member of `conferral_bases`
    revocation:  none                      # REQUIRED -- a member of `revocation_bases`
    holder:      "NPC-020"                 # REQUIRED -- a case id in the 46-row cast
    obligees:    []                        # OPTIONAL -- case ids that `oblige` to this seat
    source:      "systems/world/reference/worldbuilding_v30.md:24"    # REQUIRED
    note:        "..."                     # OPTIONAL
```

| field | required | maps to | the loader refuses when… |
|---|---|---|---|
| `id` | ✅ | `Office.id` (`carriers.py:483`) | duplicated, or not matching `^off_[a-z0-9_]+$`. ⚠ **All 25 draft rows lack this**, so 25 ids are authored here |
| `post` | ✅ | `Office.post` (`:484`) | empty. **Not** checked against any roster — `AX` ID-4: a post is a name and nothing is inferred from it. ⚠ **One exception, and it is the re-homed constructor clause** (§A.8): if `post ∈ titles.domains`, then `body` MUST be null and `rung`'s resolved kind MUST equal `title_domain(post)` |
| `rung` | ✅ | `Office.rung` (`:485`) | the anchor resolves to zero rungs, or to more than one. **Four anchor forms only:** `{realm: true}` · `{duchy: "<faction>"}` · `{territory: "<code>"}` · `{settlement: "<code>"}`. ⚠ **NEVER an id**, so a `build_realm` rename cannot rot the file (`CLAUDE.md` §5's hand-transcription hazard, one layer earlier) |
| `body` | ⬜ | `Office.body` (`:500`) | not a member of `office_bodies` → `Unspecified` at `data/rosters.py:423-430`, **verified by construction** |
| `faction` | ✅ iff `body` is null | `Office.faction` (`:501`) | `body` and `faction` both null → `Unspecified` (`:440-445`); `faction` not on `factions` → `Unspecified` (`:446-452`); **both** set and disagreeing → `Forbidden` (`:432-438`). All three **verified by construction** |
| `remit_acts` | ✅ (may be `[]`) | `Office.remit_acts` (`:486`) | any member off `remit_acts` → `Unowned` at `carriers.py:510-512`, **verified**. After `02` deletes `dispatch` the roster is `[issue, determine, confer, revoke, convene]` |
| `conferral` | ✅ | `Office.conferral` (`:489`) | not a member of the **NEW** `conferral_bases` roster → a new `Unowned`, same shape as the remit refusal (§A.8) |
| `revocation` | ✅ | `Office.revocation` (`:490`) | not a member of the **NEW** `revocation_bases` roster → same |
| `holder` | ✅ | a `hold` Tenure | the case id is not in the cast; or the case already holds this seat id; or a **live `hold` already exists on this seat** — `world_q.hold_force` raises on a second (`world_q.py:138-144`) |
| `obligees` | ⬜ | `oblige` Tenures | a case id not in the cast, or equal to `holder` |
| `source` | ✅ | — | empty. **Not mechanism** — but a seat with no citation is the fabrication `data/rosters.py:428-429` exists to prevent, so the loader refuses it |

**Three schema rules that are not fields, and each answers a measured defect:**

> **R-1 · EVERY SEAT HOLDS A RUNG.** `Office.rung` stays `Optional` in the dataclass because
> `ARCH §B.7`'s `scope? (null = a cluster)` is ratified; **`offices.yaml` forbids null**, which is the
> right layer for a content rule. Answers §0.2 pt 2 (16 of 19 with no rung) and `ARCH F.21`'s
> consequence line (*"church seats become revocable by purview alone — which they also lack"*).
>
> **R-2 · A SEAT'S RUNG IS THE SMALLEST RUNG CONTAINING EVERYTHING THE SEAT MUST REACH — NEVER THE
> LARGEST ITS FACTION OWNS.** The Lord Treasurer's business is the court, so his rung is the capital
> territory, not the realm. Answers §A.6's E-attack (*"any office-holder governs everything beneath
> them"*) at the content layer, where it belongs: purview is the ground, `remit_acts` is the
> authority, **and the ground is authored small.**
>
> **R-3 · EVERY HOLDER LIVES INSIDE THE CLOSURE OF THE RUNG HE GOVERNS.** Not *at* it — §A.10 refuses
> moving anyone onto a duchy — but **within** `descendants(rung) ∪ {rung}`. Checked at build, after
> homes are assigned (`harness/populated.py:400-422`). ⭐ **Measured false for 2 of the 3 rung-bearing
> seats today** (§0.2 pt 3), and the repair is a `home:` for those two cases in
> `references/npc_registry.yaml` — which `:408-409` already reads (*"if row and row.get("home") in
> w.rungs: home = row["home"]"*), so the mechanism exists and the data does not. **`SC-3` is the
> falsifier.**

**Two NEW rosters in `rosters.yaml`, beside `tenure_kinds` (`:101`) and `remit_acts` (`:111`):**

```yaml
  conferral_bases:
    source: "ARCH §B.7 call 1's list; AX ID-14 (AX:519) -- `hold-kind -> {confer|determine|succeed}`"
    open: false          # CLOSED. A fourth basis is a design change, not a table edit (ARCH §B.7 call 3)
    values: [confer, determine, succeed]

  revocation_bases:
    source: "ARCH §B.7 call 1 -- *two VALUES of `revocation.conjuncts`*; Jordan's two rules at rosters.yaml:719-723"
    open: false
    note: >-
      `purview` = {reaches}.  `holdings` = {reaches, in_holdings}.  `none` = no act empties it.
      The higher-rank conjunct is DERIVED from `contain_ascends` (state/world.py:197-221), not
      declared -- 03 §A.5.1 carries the proof. ARCH F.21 presupposes a `higher_rank` conjunct and is
      NARROWED, not closed: see 03 §C.9 RR-B.
    values: [purview, holdings, none]
```

⚠ **`open: false` is deliberate and is the `requires_forms` precedent** (`rosters.yaml:1086-1094`):
*"⚠ CLOSED AT SEVEN. A cell naming a form outside this roster REFUSES AT LOAD, because an eighth form
is a new thing a precondition can ask and that is a design change, not a table edit."* A fourth
conferral basis is exactly that, and `ARCH §B.7` call 3 already says where a consecration goes instead.

> ### **RULED: seven required fields, four anchor forms, three schema rules, two closed rosters, and
> the rung is an ANCHOR rather than an id.** Cited to `carriers.py:479-548` field by field,
> `data/rosters.py:408-453` (the four refusals, each verified by construction),
> `carriers.py:508-512` (the refusal shape copied), `ARCH §B.7` (the ratified type),
> `AX` ID-14 (`AX:519`) and `rosters.yaml:1086-1094` (the closed-roster precedent).

## §A.15 · THE TWENTY-NINE SEATS — every field, every derivation, every citation

**19 live + 10 authored = 29.** Nine new people are seated; NPC-020 gains a second seat; NPC-041
obliges rather than holding. `T` = territory anchor, `D` = duchy anchor. `cnf`/`rvk` are the bases.
**`[NEW]`** = authored here; **`[LIVE]`** = the seat exists in `build_realm(0)` today; **`⚠`** = a row
a reviewer should attack first (§D).

| # | id | post | rung anchor | body | faction | remit_acts | cnf | rvk | holder | derivation |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `off_king` | King | realm | — | Crown | issue determine confer revoke convene | succeed | none | NPC-020 | `[LIVE]` draft `titles:` row 1 |
| 2 | `off_duke_valorsmark` | Duke | D Crown | — | Crown | issue confer revoke convene | succeed | none | NPC-020 | **`[NEW]`** ⚠ `duchy_valorsmark` exists and has NO seat. `harness/populated.py:302-305`: *"the Crown's duchy is **Valorsmark**, and Almud holds the realm seat **AS WELL**"*. `hold` is 1-per-**object**, so two seats is lawful |
| 3 | `off_duchess_hafenmark` | Duchess | D Hafenmark | — | Hafenmark | issue confer revoke convene | succeed | **holdings** | NPC-050 | `[LIVE]` draft `titles:` row 3 |
| 4 | `off_duke_varfell` | Duke | D Varfell | — | Varfell | issue confer revoke convene | **determine** | **holdings** | NPC-052 | `[LIVE]`. ⚠ `conferral: determine`, not `succeed`: `faction_politics_v30.md:246` — *"first among the Jarls, **not a monarch**"*, quoted at `harness/populated.py:308-310`. The Jarl Assembly determines him |
| 5 | `off_widow_regent` | **Queen** | realm | — | Crown | issue determine confer revoke convene | succeed | none | NPC-032 | `[LIVE]`, **post NORMALISED.** ⭐ Live post is `"Queen (Widow Regent if Almud eliminated)"`, which is **not** on `titles.domains`, so `title_domain` → `None` and she governs nothing. **A parenthesis is what stops a regent from being a regent** — `AX` ID-4's failure in one cell. Normalised to `Queen`; the condition moves to `note:` |
| 6 | `off_heir` | Prince (Heir Apparent) | realm | — | Crown | — | succeed | none | NPC-031 | `[LIVE]` + draft `Heir Apparent` row. `ARCH F.22`: *"the named heir is eligible by `own`"* |
| 7 | `off_princess` | Princess | realm | — | Crown | — | succeed | none | NPC-030 | `[LIVE]`. No draft row; kept — `harness/populated.py:686-689` argues the Royal Family seats |
| 8 | `off_royal_marshal` | Royal Marshal | T T1 | Inner Circle | ⟵derived | issue convene | confer | purview | NPC-036 | `[LIVE]` + draft row 1 (standing 7, `faction_politics_v30.md:194`) |
| 9 | `off_lord_treasurer` | Lord Treasurer | T T1 | Inner Circle | ⟵ | issue | confer | purview | NPC-037 | `[LIVE]` + draft row 2 |
| 10 | `off_spymaster` | Crown's Spymaster | T T1 | — | Crown | issue | confer | purview | NPC-033 | `[LIVE]` (authored case overlay, `remit: [issue, dispatch]` → `dispatch` deleted by `02`). Draft body `Schattendienst` **dropped** (off-roster) |
| 11 | `off_parliamentary_clerk` | Chief Parliamentary Clerk | T T1 | Ministries | ⟵ | issue | confer | purview | NPC-008 | `[LIVE]`. ⚠ Draft row **doubly superseded** (§A.13.2 \*\*\*): its own note records an unresolved source conflict, **and** Almstedt is dropped by the 2026-09-13 ruling |
| 12 | `off_guard_captain` | Royal Guard Captain | T T1 | — | Crown | — | confer | purview | NPC-035 | `[LIVE]` + draft `Captain of the Royal Guard / Löwenritter Liaison` |
| 13 | `off_lord_steward` | Lord Steward | T T1 | — | Crown | issue | confer | purview | NPC-009 | **`[NEW]`** draft row, `faction_canon_v30` Crown *"Member NPCs"*; the draft's note: *"Not one of the five §1.1d Inner Circle NPCs"* — so **no body** |
| 14 | `off_archbishops_rep` | Archbishop's Representative | T T1 | — | Church of Solmund | — | confer | purview | NPC-034 | `[LIVE]`. ⚠ Draft says `faction: Crown`; **live derivation wins** (gate 4), conflict recorded (§A.13.2 \*\*) |
| 15 | `off_confessor` | Confessor | T T9 | Holy See | ⟵ | issue determine confer revoke convene | **determine** | none | NPC-021 | **`[NEW]`** draft `titles:` row 4. ⚠ `governs: "ecclesiastical institution"` is **not a rung kind**, so the rung is AUTHORED: T9 Himmelenger is the Church's one territory (measured: `fac_church_of_solmund → terr_T9`). `Confessor` ∉ `titles.domains`, so a `body` is lawful. `determine`: the Cardinals elect |
| 16 | `off_cardinal_fortitude` | Cardinal of Fortitude | T T9 | Cardinal of Fortitude | ⟵ | issue convene | confer | purview | NPC-040 | **`[NEW]`** draft row; body remapped from `Dicastery for the Defense of the Faith` |
| 17 | `off_cardinal_justice` | Cardinal of Justice | T T9 | Cardinal of Justice | ⟵ | issue determine convene | confer | purview | NPC-038 | `[LIVE]` (post `Cardinal Justice` → normalised). Body remapped from `Dicastery for Doctrinal Adjudication` |
| 18 | `off_cardinal_prudence` | Cardinal of Prudence | T T9 | Cardinal of Prudence | ⟵ | issue | confer | purview | NPC-013 | **`[NEW]`** draft row; body remapped from `Dicastery for Temporal Affairs` |
| 19 | `off_cardinal_temperance` | Cardinal of Temperance | T T9 | Cardinal of Temperance | ⟵ | issue | confer | purview | NPC-039 | **`[NEW]`** draft row; body remapped from `Dicastery for Doctrine and Archives` |
| 20 | `off_senior_inquisitor` | Senior Inquisitor | T T9 | Cardinal of Justice | ⟵ | determine | confer | purview | NPC-004 | **`[NEW]`** draft `Cardinal Justice (alternate) / Senior Inquisitor`. Two seats on one body is lawful (a body is not a seat) |
| 21 | `off_legal_advisor_hm` | Legal Advisor to Baralta | D Hafenmark | Inner Council | ⟵ | — | confer | purview | NPC-071 | `[LIVE]` + draft `Baralta's Legal Advisor`. One of `npc_behavior §2.16`'s **two** |
| 22 | `off_military_commander_hm` | Military Commander | D Hafenmark | Inner Council | ⟵ | convene | confer | purview | NPC-072 | `[LIVE]` + draft row. The second of the two. `convene`: a muster is a sitting |
| 23 | `off_commune_rep_hm` | Commune Representative (Banneret) | D Hafenmark | Inner Council | ⟵ | — | **determine** | purview | NPC-081 | `[LIVE]`, **`proposed`**. No draft row. ⚠ Exceeds `npc_behavior §2.16`'s two; kept with `harness/populated.py:718-724`'s declared marginal call attached. `determine`: a commune elects |
| 24 | `off_guild_comptroller` | Guild Comptroller | D Hafenmark | **Guild** | ⟵ Guilds | — | **determine** | purview | NPC-007 | **`[NEW]`** ⚠⚠ **DERIVED, attack this first.** The 2026-09-13 ruling drops Feldhaus from Hafenmark's **council**, not from the world; her registry primary is *"Guilds Representative"*. Re-seated on `Guild` (on the live roster). `determine`: the Guild Forum |
| 25 | `off_senior_jarl_west` | Senior Jarl of the Western Highlands | D Varfell | Jarl Council | ⟵ | determine | **determine** | purview | NPC-073 | `[LIVE]` + draft row (ED-637 rename to Björn Holdar). Draft body `Council of the Highlands` **dropped**; draft `rung_kind: province` **dropped** — the world has **0 provinces** |
| 26 | `off_skald_chief` | Skald-Chief | D Varfell | Jarl Council | ⟵ | determine | **determine** | purview | NPC-074 | `[LIVE]` + draft row (ED-638 rename to Ingrid Stenskald). `determine` remit is canon: the draft's note — *"any Deed-Claim succession in Varfell needs the Skald-Chief's endorsement"* |
| 27 | `off_military_jarl` | Military Jarl | D Varfell | Jarl Council | ⟵ | convene | **determine** | purview | NPC-082 | `[LIVE]`, **`proposed`**. No draft row; same marginal call as row 23 |
| 28 | `off_grand_master` | Grand Master | T T1 | **Lions' Table** | ⟵ Löwenritter | convene | confer | purview | NPC-070 | **`[NEW]`** ⚠ **the ONE draft seat that constructs today** (verified). `Lions' Table` is on the live roster. Rung authored: the Löwenritter hold no territory, and T1 is the capital (measured: `b_s_001_court → set_s_001 → terr_T1`). The draft's own note: the first name *"Lisbeth"* is untiered — **`holder_name` is not transferred**, only the case id |
| 29 | `off_restoration_leader` | Leader | T T15 | — | Restoration Movement | issue | **determine** | none | NPC-003 | **`[NEW]`** ⚠⚠ **the WEAKEST row; attack it second.** `obligees: [NPC-041]` — one seat, two holders, `AX §E.2.5`. Canon calls the movement's authority *"informal"* (`worldbuilding_v30.md` §8) and gives it **no organ and no territory**, so `body: null` is honest and the **rung is authored**: T15 Askeheim is the one territory inside the realm that no faction holds (the draft's `holdings:` names it `Uncontrolled`; measured: no live `hold` on `terr_T15`). `revocation: none` follows from *"informal"* |

**The distributions, counted from the table:**

| | | |
|---|---|---|
| `conferral` | `confer` **15** · `determine` **8** · `succeed` **6** | rows 8-22 + 28 · 4, 15, 23, 24, 25, 26, 27, 29 · 1, 2, 3, 5, 6, 7 |
| `revocation` | `purview` **20** · `holdings` **2** · `none` **7** | rows 8-14, 16-28 · rows 3, 4 · rows 1, 2, 5, 6, 7, 15, 29 |
| rung anchors | `realm` **4** · duchy **10** · territory **15** | 1, 5, 6, 7 · 2, 3, 4, 21-27 · 8-20, 28, 29 |
| `remit_acts` non-empty | **22 of 29** (today: **3 of 19**) | seven seats hold ground and no authority: 6, 7, 12, 14, 21, 23, 24 |
| seats with a `body` | **17 of 29**, every one on the live `office_bodies` roster | 8, 9, 11, 15-20, 21-24, 25-28 |

⚠ **Every distribution above was re-added by hand and two were wrong on the first pass**, which is
recorded rather than quietly fixed: `revocation` came out `19/2/8 = 29` by double-counting row 2 and
dropping row 20 (`off_senior_inquisitor`, which is `purview`), and `body` came out 14 by missing the
three `Jarl Council` rows. **A distribution that does not sum to the table's own row count is the
defect `CLAUDE.md` §0.1 pt 4 names** — a number without a control. All four now sum to **29**.

**ZERO new `office_bodies` rows are needed, and that is the derivation paying for itself.** Measured:
every body in the table is already on the live roster — `Holy See` (`rosters.yaml:1010`), the four
`Cardinal of X` (`:1011-1014`), `Guild` (`:1022`), `Inner Circle`/`Inner Council`/`Jarl Council`
(`:1038-1040`), `Ministries` (`:1006`), `Lions' Table` (`:1016`). The five the draft appeared to require
were its own **spelling variants** of rows already there (§A.13), and remapping them to canon's names
removes the need entirely. ⭐ **A copy would have added 27 roster rows; the derivation adds none.**

> ### **RULED: twenty-nine seats, every one with a rung, a remit, a conferral basis and a revocation
> basis; nine new people seated; five draft seats dropped as superseded; four live seats kept against
> the draft's silence; ZERO new `office_bodies` rows.** Cited per row above. ⚠ **Two rows are marked
> for attack and one distribution error is corrected in place** — because a content table that reports
> only its favourable count fails `CLAUDE.md` §0.1 pt 4.

---

# PART B · WHAT THIS ADDS, AND WHAT IT MAKES UNNECESSARY

## §B.1 · The ledger extract — `05` is the single owner of the count

`05_LEDGER_AND_BUILD.md` owns the suite's net (`CLAUDE.md`-adjacent discipline: the plan's §4 is the
single owner). This file's contribution, stated so `05` can reconcile it:

| this file | names | n |
|---|---|---|
| **REMOVED** — helpers | `title_domain`, `title_rank`, `highest_title_rank` (`titles_held` is RENAMED to `seats_held`, not removed), `conferral_path` | **4** |
| **REMOVED** — predicates | `_req_dispatch` (with `02`'s verb, under RR-A) | 1 |
| **REMOVED** — fields | `Office.{scope_rung, binds, establishment, dates, upkeep}` | **5** |
| **REMOVED** — branches | the `is_title` branch (`predicates.py:252-276`); `__post_init__`'s `scope_rung` default | 2 |
| **ADDED** — helpers | `reaches` | 1 |
| **ADDED** — predicates | `_req_oblige` | 1 |
| **ADDED** — effect bodies | `oblige` | 1 |
| **ADDED** — rosters | `conferral_bases`, `revocation_bases` | 2 |
| **ADDED** — content (counts 0) | `offices.yaml` · the two `Office.__post_init__` roster refusals (the *shape* is copied, not a new rule) | 0 |
| **NET, this file** | | **−8** |

⚠ **Three honest caveats, each of which a favourable count would hide:**
1. `body_function` is **kept** against round one's list (§A.8), so this file's field deletions are
   **five, not six**.
2. `titles_held` → `seats_held` is a **rename plus a one-line narrowing**, counted as 0, not as
   −1/+1. A reader's unit is *"names I must hold"*, and the name changes while the thing does not.
3. The `commission` Record and the deposit rule are **`02`'s objects**, not this file's, even though
   §A.11 is where H-71 closes. Counting them here would double-count them in `05`.

## §B.2 · Refused and deferred, each with the clause that refuses it

| refused | the clause |
|---|---|
| a `Title` type | `ARCH §B.7` call 1 — *"There is no `Title` type"* |
| a fourth `conferral` basis (`warrant`) | `ARCH §B.7` call 3 — widen the **door**, not the value set |
| a fourth `revocation` value (`term`) | `ARCH §B.8`'s `T-o` row — *"`term.closer` names a basis, not a second authority"* |
| `domain : RungId[]` — a set-valued scope | `ARCH §B.7`'s `scope?` is **singular**; and `predicates.py:128-131`'s disjunction already covers a person holding several seats |
| `remit : (act, scope?)[]` — a scope per act | `ARCH §B.7` pairs `acts[]` with one `binds`; a Duke who may `confer` in one province **establishes a sub-seat** — `ARCH §B.7`'s own delegation row |
| a `higher_rank` conjunct | §A.5.1 derives it. ⚠ **`ARCH F.21` presupposes it, so this is RR-B, not a refusal** |
| `oblige`'s `requires` reading `binds` | `ARCH F.17`'s own default, refused on a **measured** 0-reader field with one value on 19 of 19 (§A.9) |
| moving office-holders onto their seat's rung | §A.10 — it costs them every larder and every co-location. R-3 requires **inside the closure**, which costs 17 of 19 nothing |
| a `rung:` field holding an id | §A.14 — an anchor cannot rot when `build_realm` renames |
| `Act.via` here | position 6 of the ratified ORDER (`_part2.md:239`) |

**Deferred, and named so nobody reads them as closed:** `ARCH F.18` (upkeep's source — a field with no
readers dies, an economic question does not); `ARCH F.21` (RR-B); `H-108` (`Act.via`, narrowed by the
interim); `H-101` (an Office cannot name a superior Office — `conferral_path`'s docstring records it
and this file deletes the Query, not the hole); seizure (`02`'s LIMIT); `ED-SE-0051` (`04`'s RR-2).

## §B.3 · E, scored LAST and as a RATIO — and it FAILS if scored alone

`CLAUDE.md` §0.06: *"⚠ **E is never scored as an independent axis**: alone it is satisfiable by
amputation, so score it **last, as a ratio against what N and R found**."*

**What N found necessary** (the cuts are §D's): the two value sets (cut them → 19 of 19 seats stay
unfillable); `reaches` (cut it → 16 of 19 hold purview over nothing); `offices.yaml` (cut it → the
mechanism has no content and fixes nothing); the commission (cut it → nobody can form a governance
verb, H-71 stands). **Four N-lines, four cuts, each with a measured consequence.**

**What R found necessary:** a seat that can be **emptied** (R-completeness: a seat that can be created
and never destroyed is `AX-6`'s unenumerated permanence); a seat whose holder **hears** about his own
ground (R-3, and measured false for 2 of 3 today); `determine` and `succeed` as **fillers**, so a
vacancy is not always a superior's gift — which is `ARCH F.22`'s consequence line, *"every death is a
vacancy only a superior can fill, **which may be right for an office and is wrong for a crown**."*

**The ratio.** Four additions against nine removals: `reaches`, `_req_oblige`, the `oblige` body, two
rosters = **5 named things in, 12 out.** Of the five, the pre-commitment concedes **two as overhead**:

1. **the two rosters are +2 names for a closed set of six strings.** Conceded. The alternative — a
   literal tuple in `predicates.py` — is what `AX` ID-12 (`AX:454`, *"a closed set lives in data"*) refuses — `ARCH F.20b` states it in those words, *"a definition living as a literal in a body is what `ID-12` refuses"* —
   so the overhead buys a load-time refusal. **Kept.**
2. **`reaches` is a fifth Query-shaped helper.** ⚠ **NOT conceded, and here is the deletion:**
   `under_purview` **becomes** `reaches` over the seat disjunction, so `reaches` is not an addition
   beside it — it is `under_purview`'s body **with the seat as a parameter instead of the actor**.
   Counted as **0**, and §B.1's `+1` is therefore this file's one deliberate over-count: it is listed
   as added because a reader meets a new name, and the honest net is **−9, not −8**, if the unit is
   *functions*. **Both figures are stated; §0.1 pt 4 forbids reporting only the favourable one.**

**So E is scored as 5 in / 12 out with one conceded overhead of 2 names**, and the design would fail E
if the author could not delete one of the two. ⚠ **The author cannot, and says so:** both rosters are
required by the `requires_forms` precedent, and collapsing them into one (`bases: {conferral: [...],
revocation: [...]}`) would make one roster do two jobs — which is the `titles`/`values` duplication
`rosters.yaml:733-742` already corrected once. **E passes narrowly, on a ratio, and the concession
stands.**

---

# PART C · THE THREE QUESTIONS

## §C.1 · WHO OWNS THIS? — one owner per value, and the owner is its only writer (`AX-4`, `AX:141`)

| the fact | its one owner | its only writer |
|---|---|---|
| **which act fills a seat** | `Office.conferral` (`carriers.py:489`) | `engine/season/data/offices.yaml` at build; `establish` at RESOLVE (`verb_table.yaml:215`, `writes: [Office.exists, Office.remit, Office.establishment]` — ⚠ the third goes with the field, §A.9) |
| **what emptying a seat requires** | `Office.revocation` (`:490`) | as above |
| **the roster of admissible bases** | `rosters.yaml: conferral_bases` / `revocation_bases` | nobody — a closed roster, `open: false` |
| **a seat's ground** | `Office.rung` (`:485`) | `offices.yaml` at build; `establish` at RESOLVE |
| **whether a ground reaches another ground** | `predicates.reaches` | nobody — a function over `contain` edges |
| **the containment ladder** | `contain` Tenures, with `World.add_tenure` as *"The ONE writer"* (`world.py:223-224`) | `World.add_tenure` alone, and it refuses a non-ascending edge (`:248-256`) |
| **rank** | ⭐ **NOBODY — it is derived** (§A.5.1). Before this file, two owners: `title_rank` (`data/rosters.py:465`) and the `contain` ladder | — |
| **who holds a seat** | a `hold` Tenure, owned by its subject (`ARCH §B.7` invariant *"a seat does not know its holder"*) | `_eff_confer`, `_eff_revoke`, `succeed`'s body (unwritten) |
| **who serves a seat** | `oblige` Tenures, read by `establishment_of` (`world_q.py:399`) | `_eff_oblige` (§A.9), `_eff_release` |
| **what a holder BELIEVES his remit to be** | his own ledger's `content:commission` claim (`carriers.py:129-156`) | WITNESS's deposit, via `02`'s rule |
| **what his remit IS** | `Office.remit_acts` (`:486`), read by `_eligible` (`resolve.py:56`) and `_ch_post_remit` (`epistemic.py:360`) | `offices.yaml`; `establish` |

⭐ **The row that matters is `rank`.** Before this file it had **two homes** — a title's ordinal and the
containment ladder — and `AX-4` (*"every value has exactly one owner"*) was broken in a way nothing
could see, because the two agreed on all 373 edges (measured, §A.5.1). **They agreed by construction,
not by luck**, which is exactly why the duplicate was invisible and exactly why it can be deleted.

## §C.2 · WHAT CAN CHECK THIS? — `STRUCTURAL | MECHANICAL | CONVENTION`

| claim | grade | the construction |
|---|---|---|
| a `conferral` off the roster cannot exist | **STRUCTURAL** (typed, at load) | `Office.__post_init__` raises `Unowned`, the shape at `carriers.py:508-512`. There are four `Office` construction sites in the chain (`carriers.py:518-519`'s own count) and all four go through it |
| a `revocation` off the roster cannot exist | **STRUCTURAL** | same |
| **no `is_title` branch exists** | **MECHANICAL** | `grep -rn 'title_domain\|is_title' engine/season --include=*.py` → 0 outside history. A grep is mechanical, not structural: a new branch keyed on a post string could be written tomorrow |
| a seat with no rung cannot exist | **MECHANICAL** | the `offices.yaml` loader refuses it. **Not structural** — `Office.rung` stays `Optional` because `ARCH §B.7`'s `scope?` is ratified, so a hand-built `Office(..., rung=None)` in a test is still lawful, and `SC-2` is the falsifier |
| every holder lives inside his seat's closure | **MECHANICAL** | a build-time assertion after homes are assigned. Measured **false for 2 of 3** today (§0.2 pt 3) |
| containment implies strictly higher rank | ⭐ **STRUCTURAL** | `World.add_tenure` raises on a non-ascending `contain` (`world.py:248-256`); `contain_ascends` is a strict `>` on the `rung_kinds` ordinal (`:220-221`). **This is the guard §A.5.1's proof rests on, and it is the strongest grade in this file** |
| a seat cannot revoke itself | **STRUCTURAL** (typed) | `reaches` returns `False` on `target.id == via.id` before any walk |
| purview never reaches upward | **MECHANICAL** | `descendants` walks `contain.object == cur` only (`world_q.py:62`); `test_season_shape.py:4467-4469` observes it |
| a council is one seat | **STRUCTURAL** | `world_q.hold_force` raises on a second live `hold` (`world_q.py:138-144`) |
| a seat's remit grants only rostered acts | **STRUCTURAL** | `Office.__post_init__:508-512`, already shipped |
| **`offices.yaml` matches canon** | **CONVENTION** | a `source:` per row, and nothing checks that the cited line says what the row says. ⚠ **Stated as the weakest grade in the file.** `tools/validate_ed_citations.py` covers ED ids only (`CLAUDE.md` §0), and no tool validates a `systems/**` line citation |

## §C.3 · WHOSE ACT MAKES IT HAPPEN? — every mechanism as execution

| mechanism | the act, or the absence of one |
|---|---|
| a seat exists | `establish` (`verb_table.yaml:209-219`), `remit:confer`, `grade: assumption`. ⚠ **NOT resolvable today** (measured, §0.2). `offices.yaml` is the **build-time** producer; `establish` is the in-play one and remains unbuilt. **This file does not build it**, and says so |
| a seat is filled by a superior | `confer` — **resolvable today**, effect at `effects.py:92-126`. Blocked only by the empty basis (§A.1.1) |
| a seat is filled by a body | `determine` (`verb_table.yaml:186-195`) — **NOT resolvable**, `grade: absent`, `requires: "a fired Date with a DocketItem; judging_set — D11, absent"`. ⚠ **A `conferral: determine` seat is therefore UNFILLABLE IN PLAY today**, which is 8 of 29 seats, and `world_q.judging_set` raises `Unspecified` (`world_q.py:146-148`). **Stated as a LIMIT, not resolved** |
| a seat is filled by an heir | `succeed` — **NOT resolvable**: `own`-eligible with a typed `relation` cell and **no `@effect_for` body**. Six of 29 seats. `ARCH F.22` |
| a seat is emptied | `revoke` — **resolvable**, effect at `effects.py:159-172`. Blocked by the empty basis and, for `holdings`, by the faction-subject holds (§0.2 pt 4) |
| a holder resigns | `release` (`verb_table.yaml:419-432`), `own`, **resolvable**, effect at `effects.py:129`. ⭐ **The one way a seat empties today that needs nothing from this file** |
| a person joins an establishment | `oblige` — **NOT resolvable**; the row declares `writes: [Tenure.since]` and there is no body. §A.9 adds it |
| a holder learns his remit | the `commission` Record + `02`'s deposit. **Nothing today**: `_eff_confer` mints no Record, and the deposit's predicate is `e.kind` (`witness.py:191`) |
| purview is asked of the seat | `Act.via` — position 6. **Nothing today**; the interim is the seat disjunction (§A.10) |

⭐ **The honest summary: of the four ways a seat is filled or emptied, TWO execute today (`confer`,
`revoke`, both blocked on content alone) and TWO do not (`determine`, `succeed`, each missing an
effect body).** So `offices.yaml` alone would make 15 of 29 seats conferrable and leave 14 fillable
only at build. **That is the sentence a reader should take from this file**, and it is why §C.8's grade
is `paper` rather than `partial`.

## §C.4 · THE LOOPS, NAMED AND SIGNED (`AX` ID-16, `AX:544-549`)

| loop | sign | the mechanism | what damps it |
|---|---|---|---|
| **`SC-L+1`** | **+** | a holder confers a subordinate seat; the subordinate's purview is a subset of his; the subordinate confers further down | **the ladder is finite and strictly descending.** `contain_ascends` (`world.py:220-221`) makes each step strictly lower on an 8-member roster, so the chain is at most 8 deep. **Structurally bounded, not tuned** |
| **`SC-L+2`** | **+** | a man who holds land may unmake the seat that governs it, take the seat, and hold more land | **`in_holdings` requires a live `hold` on the rung**, which `transfer` cannot create (it moves matter, not rungs) and only `confer`/a build can. ⚠ **The damping is UNMEASURED because no person holds any rung today** (§0.2 pt 4), so this loop has never run. `SC-6` is where it first would |
| **`SC-L−1`** | **−** | a seat emptied and not refilled loses its ground to nobody; nothing beneath it is conferred | **`release` is `own`-eligible and always available**, so a ladder can always shorten. `AX-6`: nothing becomes permanent without an author |
| **`SC-L0`** | **0** | a holder believes a remit he no longer has (§A.11 row 3) and never acts | **not a loop — a fixed point**, and it is the mechanism: a struck seat goes on governing. Terminates when a claim decays or a witness corrects it |

**No loop here has an unbounded positive arm**, and the reason is the containment ladder's finiteness
rather than a fixture. ⚠ **`SC-L+2` is the one a reviewer should distrust**, because its damping term
lives in a relation (`hold` over a rung) whose only current instances have **faction** subjects.

## §C.5 · WHAT THIS FILE DOES NOT CLAIM

1. That anything **runs**. Grade `paper` (§C.8).
2. That a ratified `architecture/` sentence is changed. `ARCH §B.7`'s `Seat :=` line and `ARCH F.21`
   are **quoted at their `§` and not edited** — RR-B (§C.9).
3. That `Act.via` lands here. Position 6 (`_part2.md:239`).
4. That a `Title` type or a rank ladder survives, **or that Jordan's rank clause is discarded** — it is
   derived (§A.5.1) and the one behaviour change is declared.
5. That `ARCH F.18` (upkeep), `ARCH F.21`, `H-101` or `H-108` close.
6. That `offices.yaml`'s rows are verified against canon by anything but a human reading a `source:`
   line. Grade **CONVENTION** (§C.2, last row), and it is the weakest claim in the file.
7. That the five superseded draft seats are *wrong about canon* — they are **correctly transcribed from
   a section a ruling superseded on the day of transcription** (§A.13.2).
8. That round one's `03_THE_SURFACE.md` is superseded. It **STANDS**.
9. That Jordan's principle (RR-P, `02`) is settled. Nothing in this file leans on it.
10. That `ED-SE-0051` is answered. RR-2 stays open.

## §C.6 · THE GRADE, AND WHAT WOULD MOVE IT

**`paper`.** Nothing in this file executes. `CLAUDE.md` §0.2: *"A milestone juncture is done when the
behaviour EXECUTES. Not when a document exists with a `## Status:` line."*

**Four artifacts would move it, in cost order, and each is a build item in `05`:**

| # | artifact | what it would show | why it has not been produced |
|---|---|---|---|
| 1 | `offices.yaml` + the two rosters + the two predicates on values, then `python -m engine.season.harness.corpus_run` | `confer` and `revoke` move out of *"foldable but never even attempted"* (`corpus_run.py:645-648`) and into `VERBS THAT EXECUTED` | it is one commit and this file is a proposal, `HELD BACK IN FULL` |
| 2 | the same, plus a `census` before/after | 19 seats → 29; purview over **0** rungs → over a measured closure for all 29 | as above |
| 3 | `@effect_for("oblige")` + `_req_oblige`, then `establishment_of` over live tenures | `establishment_of` returns a non-empty list for the Restoration seat (row 29) — **the first non-empty establishment in the world's history** | needs the body; §A.9 |
| 4 | the commission + `02`'s deposit rule, then `test_no_person_can_choose_a_governance_verb_and_h71_is_why` (`test_season_shape.py:4992`) | that test goes **RED**, which is H-71 closing. Its own docstring (`:5005-5006`) says *"it goes red the day `H-71` closes, which is exactly when the claim becomes true"* | depends on `02`'s `record_kinds` roster, which does not exist (grep: 0) |

⚠ **Artifact 1 alone does NOT make the milestone's governance juncture done**, and the temptation to
say so is why §C.3 is in this file: `determine` and `succeed` have no effect bodies, so **14 of 29
seats would still be fillable only at build.**

## §C.7 · RULING REQUESTS — `RR-B`, and it has two items

Each candidate was run through `CLAUDE.md` §0's five steps — Superseded → Irrelevant → Design doc →
Precedent → Architecture — and the step that answered it is named. **Only survivors reach Jordan.**

### Surviving: **RR-B** (this file's two items; `02` and `04` carry the others)

| item | the ratified text | why steps 1–5 cannot take it |
|---|---|---|
| **RR-B.1 · `ARCH §B.7`'s `Seat :=` line spells `upkeep` and `dates[]`, which §A.8 deletes** | *"`Seat := ( id, post, body?, scope? …, remit(acts[], binds), conferral, revocation, **upkeep, dates[]**, exists )`"* | Step 1: nothing supersedes `§B.7`. Step 2: not irrelevant — the fields are in the ratified type. Step 3: no design doc outranks `architecture/`. Step 4: no precedent deletes a ratified schema field. **Step 5 may not overwrite ratified canon** (ED-IN-0204). Measured support for the request: **0 readers each** |
| **RR-B.2 · `ARCH F.21` presupposes a `higher_rank` conjunct, and §A.5.1 derives rank instead** | *"the rank of a cluster seat (`scope = null`) \| no rank; **the loader forbids a `higher_rank` conjunct** on one \| church seats become revocable by purview alone — which they also lack"* | Step 1–4: silent. **Step 5 nearly takes it** — the derivation is sound and the guard is structural — **but F.21 is a ratified row that assumes the conjunct EXISTS**, and gate 5 cannot delete a thing ratified canon names. ⚠ **So F.21 is NARROWED, NOT CLOSED, and this file refuses to claim otherwise** |

**RR-B also carries `02`'s and `04`'s items** — `ARCH §B.8`'s `Tenure :=` fields, `ARCH §B.5`/F.15's
*"nine typed terms"*, and `ARCH §C.6`'s mint table. `05` §C is the single owner of the list.

### Closed by the five-step gate, with the step named

| candidate | closed at | by what |
|---|---|---|
| **H-91** — `remit:revoke` NECESSARY vs purview SUFFICIENT | **step 5** | two conjuncts, two owners, and the code already reads two different objects (`resolve.py:56` vs `predicates.py:234`). §A.5.3 |
| **H-109** — the `is_title` branch | **step 3** | `ARCH §B.7` call 1 says *"No `is_title` branch exists anywhere"* in terms. Not a choice; a transcription |
| **H-71** — `remit:` person-side | **step 5**, jointly with `02` | §A.11, and it closes on **both** sides. Depends on `02`'s roster |
| **`ARCH F.17`** — how a person joins an establishment | **step 5** | admission is the joiner's `own` act, so the closed remit roster needs no sixth member. F.17's own default (read `binds`) is refused on a **measured** 0-reader field |
| **`ARCH F.22`** — how succession fills a seat | **step 3** | `conferral: succeed` **is** the answer, and `succeed` is already `own`-eligible with a typed cell. What is missing is an effect body, which is work, not a ruling |
| **a fourth `conferral` basis** | **step 3** | `ARCH §B.7` call 3 puts a consecration in the judging-set **door** |
| **`term` as a fourth `revocation` value** | **step 3** | `ARCH §B.8`'s `T-o` row: *"`term.closer` names a basis, not a second authority"* |
| **the rank conjunct's deletion** | **step 5** for the mechanism; ⚠ **RR-B.2 for the TEXT** | §A.5.1's proof plus `CLAUDE.md` §0.06's `S`-defect clause. The mechanism is decided; the ratified sentence is not this file's to edit |
| **the five superseded draft seats** | **step 1** | Jordan ruled it, 2026-09-13, and `rosters.yaml:58-67` records the ruling verbatim |
| **the 22 declined organs** | **step 4** | `rosters.yaml:1035-1040` is the precedent and names the number |
| **the Archbishop's Representative faction conflict** | **step 4** | the tree already decided this row (`harness/populated.py:705-708`) |

### NOT closed, and named so nobody reads them as closed

`ARCH F.18` (upkeep's source) · `ARCH F.21` (RR-B.2) · `H-101` (an Office cannot name a superior
Office) · `H-108` (`Act.via`; narrowed by the interim) · `determine`'s and `succeed`'s effect bodies ·
`establish`'s unresolvability · the `offices.yaml` citation grade (CONVENTION) · `ED-SE-0051`.

---

# PART D · FALSIFIERS (`AX` ID-11 — ship the falsifier with the claim)

**Each one names the assertion that would observe the failure it excludes** (`CLAUDE.md` §0.1 pt 2: an
assertion that cannot observe the failure it excludes is not a weak test but an absent one), and each
says **what it controls against**.

| # | the claim | the falsifier, as an executable assertion | the control |
|---|---|---|---|
| **SC-1** | bases as values make seats conferrable | build with `offices.yaml`; `_req_confer` returns **True** for a `conferral: confer` seat under a reaching seat, and **False** for a `conferral: determine` one. ⚠ **The second half is the falsifier** — a version that admitted every non-empty string would pass the first half alone | today's world: `_req_confer` → **False** on 19 of 19, at `predicates.py:182` |
| **SC-2** | purview is `reaches`, and it is reflexive on the rung and exclusive on the seat | four assertions, and **the fourth is the one that fails a naive rewrite**: (a) a seat reaches a rung strictly inside its own → True; (b) a seat reaches **its own rung** → True; (c) a seat reaches its own rung's **parent** → False; (d) `reaches(w, seat, seat)` → **False**. A `descendants`-only implementation fails (b); an `ancestors_or_self` one fails (c); today's `under_purview` fails (d) | `len(descendants(w,'r_valoria')) == 364` against `sum(under_purview(w,king,r) for r in w.rungs) == 365` — **the measured one-rung difference is the reflexivity, and it is the control** |
| **SC-3** | every holder lives inside the closure of the rung he governs | for all 29: `containing_rung_of(holder) in descendants(w, seat.rung) | {seat.rung}`. ⭐ **Measured FALSE for 2 of 3 today** — the Duke of Varfell and the Duchess of Hafenmark are in `terr_T1 → duchy_valorsmark`. **So this assertion FAILS on the current tree and must be made to pass by a `home:` in `references/npc_registry.yaml`, not by weakening the assertion** | the King, who passes today |
| **SC-4** | rank is derived, not lost | `for every pair (A,B) of the 29: B.rung in descendants(w, A.rung) ⟹ RUNG_KINDS.index(kind(A.rung)) > RUNG_KINDS.index(kind(B.rung))`, **and** `assert checked >= 1` (`CLAUDE.md` §0.1 pt 2's *"a loop that asserts conditionally must assert that it asserted"*). ⚠ **Plus the negative:** plant a `contain` edge that descends and assert `World.add_tenure` **raises `Forbidden`** — if it does not, the proof's step 2 is false and the rank conjunct must come back | the 373 live `contain` edges, **0 violations measured** |
| **SC-5** | deleting the title helpers loses no constructor invariant | `Office(id, "King", rung, [], body="Inner Circle")` still raises, and the message still names **both** the title and the body. ⚠ **This is the falsifier for §A.8's re-homing, and it is the one most likely to be silently dropped** — a session deleting `title_domain` would delete the clause with it and every test would stay green, because **no test constructs that pair** (measured: `test_season_shape.py:6544` is the nearest and tests a body/faction mismatch, not a title/body one) | today: the same construction raises `Forbidden` (verified by construction, §A.8) |
| **SC-6** | `revocation: holdings` is satisfiable | `_req_revoke` on `off_duke_varfell` by a holder of `duchy_varfell` → **True**, and by a non-holder with purview → **False**. ⭐ **It is UNSATISFIABLE today and the reason is not the basis:** all 16 rung-holds have **faction** subjects and `in_holdings` tests `t.subject == actor` for a person. **So this falsifier fails until the faction holds are re-homed** (`05`'s item 16), and the dependency runs **opposite to the plan's build order** | `sum(in_holdings(w,p,r) for p in w.persons for r in w.rungs) == 0`, measured |
| **SC-7** | the derivation's judgment calls are right | two named rows, each with the assertion that would show it wrong: **row 24** (Guild Comptroller) — if `Guild`'s faction is `Guilds` and NPC-007's registry faction is Hafenmark, `office_faction` raises `Forbidden` on the mismatch, so the row must author `body: Guild` and **no** `faction:`; **row 29** (Restoration leader at T15) — if any faction ever holds `terr_T15`, the seat is standing on somebody else's ground and the row is wrong. `assert not any(t.kind=="hold" and t.object=="terr_T15" and t.live for t in w.tenures)` | measured today: no live `hold` on `terr_T15`; `BODY_FACTION["Guild"] == "Guilds"` |
| **SC-8** | `offices.yaml` is a derivation, not a copy | `for row in offices.yaml: Office(**row)` constructs **29 of 29**. ⚠ **The control is the copy:** `for row in offices_draft.yaml['seats']: Office(...)` constructs **10 of 25** and raises `Unspecified` **15** times — 14 on the body, 1 on the faction. **Both numbers in the same test**, or the claim has no control (`CLAUDE.md` §0.1 pt 4) | measured, §A.13 |
| **SC-9** | H-71 closes on both sides and they may disagree | two assertions: a holder with a `content:commission` claim naming a seat whose remit includes `issue` **forms** an `issue` candidate person-side; **and** a holder whose seat was revoked but whose claim survives **still forms it** and RESOLVE **refuses** it, emitting `issue.refused`. ⚠ **The second is the falsifier** — a design that kept the two readings in sync would pass the first and fail the second, and would have deleted every deception mechanism in the game | today: `person_side_eligible` declines every `remit:` alternative at `options.py:163-165`, so candidate count is **0** |
| **SC-10** | the title family is gone | `grep -rn 'title_domain\|title_rank\|titles_held\|highest_title_rank\|is_title\|conferral_path' engine/season --include=*.py` → **0**. ⚠ **And the positive control, without which the grep proves nothing:** `rosters.yaml: titles.domains` still has its **eleven** members and `test_the_title_ladder_is_total_over_the_rungs...` (`:4403`) still passes against the roster — **the ladder is canon and stays; only its readers go** | the current grep returns the nine non-test sites of §A.3 |

⚠ **THREE OF THESE TEN FAIL ON THE CURRENT TREE AND THAT IS DELIBERATE.** `SC-3` (holders outside
their duchy), `SC-6` (faction-subject holds) and `SC-9` (the `remit:` decline) are **red today**, and
each names the work that turns it green. A falsifier suite where every member passes before the work is
done is a suite that observes nothing.

---

# APPENDIX · CITATION REPAIRS

**Every `path:line` in this file was opened at that line in this session.** These are the ones I found
**wrong in my own sources** — the plan, round one, and my own first pass — repaired in place above and
listed here so a later session does not re-derive them.

| # | source | said | measured | where repaired |
|---|---|---|---|---|
| 1 | my spec | *"13 of 14 body-bearing seats name a body absent from `BODY_FACTION`"* | **15** carry a body; **14 of 15** are absent | §A.13 |
| 2 | my spec | *"26 of its 36 `bodies:` rows are non-canonical"* | **27 of 36**, decomposing as 22 declined organs + 5 spelling variants | §A.13 |
| 3 | my spec | *"would raise `Unowned`"* | `require_member` raises **`Unspecified`** (`data/rosters.py:299-302`); `Unowned` is `Office.__post_init__:510`'s, for a bad **remit act** | §A.13 |
| 4 | my spec / the plan §2.4 | *"Purview = `descendants(seat.rung)`"* | `descendants` is **PROPER** (verified: `'r_valoria' in descendants(w,'r_valoria')` → `False`), so it excludes the seat's own rung — where the subordinate seats sit. Today's `under_purview` **is** reflexive (`predicates.py:135-138`; the measured 365/364 difference) | §A.6, and struck in place |
| 5 | the plan §2.4 | *"the `is_title` branch (:252-274)"* | the branch is `:252` (assignment), `:254` (`if`), `:255-274` (the title conjuncts), **`:275-276` (the `elif` tail)**. Citing `:252-274` leaves the `elif` behind | §A.1.2, §A.7 |
| 6 | the plan §2.4 | *"`offices_draft.yaml` … ~178 data rows"* | **178 leaf data rows + 10 container headers = 188 rows.** Both figures are true of their own basis and a session citing either must say which | §A.13 |
| 7 | the plan §2.4 | *"`Office` … zero non-test readers for `scope_rung`, `binds`, `upkeep`, `dates`, `body_function`"* | **CONFIRMED, all five.** ⚠ And `dates` needed care: all 13 `.dates` hits in `engine/season/**/*.py` are `w.dates`/`self.dates`, the World's dict — a naive grep reads as 13 readers | §A.8 |
| 8 | the plan §2.4 | *"`establishment` is read once (`world_q.py:413`)"* | **CONFIRMED** — one non-test reader; the second hit is `harness/probes.py:1376`, an assertion | §A.9 |
| 9 | the plan §2.4 | *"`offices_draft.yaml` … `seats:` :230, `titles:` :538"* | **CONFIRMED** both | §A.13 |
| 10 | round one `01` §A.2 | *"`title_domain` … is `engine/season/data/rosters.py:459`"* (its own repair of ~~`predicates.py:144-164`~~) | **CONFIRMED, and INCOMPLETE:** `title_domain` has **five** non-test call sites in **three** files, two of them in `Office.__post_init__` (`carriers.py:536,546`). Round one's repair fixed the location and kept the undercount | §A.3, §0.3 |
| 11 | round one `01` §A.3 | *"`revocation ∈ {purview, purview+holdings+rank, none, term}` … `term` CONFORMANCE on `ARCH §B.8`"* | `ARCH §B.8`'s `T-o` row says the opposite: *"`term.closer` names a basis, not a second authority"* | §A.5.2, struck in place |
| 12 | round one `01` §B.2 | `Office.body_function` among the deletions | it is a **derived cache** of a roster read (`carriers.py:530`), not a second home for a fact. **Kept**, and `05`'s count adjusts | §A.8, struck in place |
| 13 | round one `01` §A.1 | *"`Office` (`carriers.py:481-549`)"* | `@dataclass` at `:480`, `class Office:` at `:481`, last body line `:548`. `:549` is blank | §A.8 (cited `:479-548`) |
| 14 | round one `01` §A.2 | *"`rosters.yaml:718-724`"* for Jordan's two revocation rules | **effectively correct**: the two rules are at `:719-723` and the whole revocation note is `:714-726`. Cited here as `:719-723` for the rules | §A.5 |
| 15 | round one `01` §0.2 | *"the eleven-name `titles.domains` roster (`rosters.yaml:755-766`)"* | **CONFIRMED exactly**: `domains:` at `:755`, `King` at `:756`, `Individual` at `:766` | §A.2 |
| 16 | the plan §2.4 | *"`_req_confer` (`loop/predicates.py:167-193`)"*, *"`_req_revoke` (:222-289)"* | `_req_confer` `:167-192`; `_req_revoke` `:222-287`, with `:288-289` blank. The refusal lines `:181-182` and `:234-235` are **exact** | §A.1 |
| 17 | the plan §2.4 | *"`Act.via` is nowhere in `carriers.py:332-365`"* | **CONFIRMED**, and stronger: `grep -rn "a\.via\|act\.via\|'via'\|\"via\"" engine/season/` → **0 hits in the whole package** | §0.1 |
| 18 | the plan §10 | `hole_register.yaml` `:795` (H-71), `:1000` (H-84), `:1520` (H-109), `:1533` (H-110), `:1106` (H-92), `:1508` (H-108) | **ALL CONFIRMED** at the `- id:` line | throughout |
| 19 | the plan §10 | `ARCH` F.15 `:1077`, F.17 `:1079`, F.18 `:1080`, F.20 `:1082`, F.22 `:1086` | **ALL CONFIRMED.** ⚠ **And `F.21` at `:1085` is in that block and no source document cites it** — it is the one F-row about seat rank, and it is this file's RR-B.2 | §0.1, §C.7 |
| 20 | — | *nobody cited it* | ⭐ **`AX` ID-14 (`AX:505-521`) already spells the conferral value set**: *"`Seat.conferral` becomes `hold-kind → {confer \| determine \| succeed}`"*. Round one cited `AX:1495-1498` (the field exists and carries nothing) and missed the sentence that names the three values | §A.4, and it is why §A.4's verdict is CONFORMANCE rather than EXTENSION |
| 21 | — | *nobody measured it* | ⭐ **`world_q.conferral_path` (`:416-436`) has zero non-test callers and never reads `conferral`** | §0.2 pt 6, §A.12 |
| 22 | — | *nobody measured it* | ⭐ **0 of 19 holders are seated at their seat's rung; the Duke of Varfell and the Duchess of Hafenmark do not live inside the duchy they govern** | §0.2 pt 3, §A.14 R-3, `SC-3` |
| 23 | — | *nobody measured it* | ⭐ **all 16 rung-holds have FACTION subjects, so `revocation: holdings` is unsatisfiable by any person today**, for a reason unrelated to the basis | §0.2 pt 4, `SC-6` |
| 24 | — | *nobody measured it* | ⭐ **`World.contain_ascends` is a STRICT ascent check enforced at the one writer** (`world.py:197-221`, `:248-256`), which is what makes the rank conjunct derivable rather than merely redundant | §A.5.1, `SC-4` |
| 25 | my own first pass, §A.15 | the `revocation` distribution as `19/2/8` and `body` as `14` | `20/2/7` and `17`, both summing to 29 | §A.15, corrected in place with the error recorded |
| 26 | my own first pass, throughout | **thirteen `path:line` citations off by one to three lines**, each written from a `grep -n` of a definition rather than from the line the claim is about | repaired by opening each: `in_holdings`'s test `:103-104`→**`:101-102`** · `under_purview`'s reflexive return `:135-137`→**`:135-138`** · `office_faction`'s body refusal `:421-428`→**`:423-430`**, its mismatch `:431-438`→**`:432-438`**, its law string `:425-427`→**`:428-429`**, the function `:408-452`→**`:408-453`** · `revoke`'s `requires` `:472`→**`:473`** and its refusal `:474`→**`:476`** · `descendants`' walk `:61`→**`:62`** · `succeed`'s row `:490-504`→**`:490-506`** · the Royal-Family note `:688-691`→**`:686-689`** · the dual-loyalty note `:707-710`→**`:705-708`** · the proposed-seat note `:726-732`→**`:718-724`** · the `home:` read `:406-407`→**`:408-409`** · the `office_bodies` mapping `:1003-1027`→**`:1004-1040`** | everywhere |

⚠ **Row 26 is the most useful row in this appendix and it is about METHOD, not about lines.** Every
one of the thirteen was written from a `grep -n` that found a **definition** and then cited a range
around it, which is `CLAUDE.md` §0.1 pt 3's third shape exactly: *"claiming 'as `F` says at `:L`' →
open `F` at `:L`. A citation you have not opened is not a citation."* **A grep locates; it does not
verify.** Every one was caught by the adversarial pass over this file's own citations, run before the
file was closed, and none was caught by writing it carefully.

⚠ **Two of my own numbers were wrong on the first pass (row 25), and they are recorded rather than
quietly fixed**, because `UNIFICATION_LEDGER.md` rows 20–21 are this suite's own precedent: three of
round one's *"opened and found CORRECT"* lines were **false verifications**, and the repair is to show
the correction, not the clean result.

---

_End of `03_SEATS_AND_CONTENT.md` · `ED-IN-0235` · lane `IN` · grade `paper` · HELD BACK IN FULL._
