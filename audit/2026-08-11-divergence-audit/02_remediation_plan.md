# Remediation plan — divergence audit

## Status: PROPOSED. Nothing here is executed. Four items are held for Jordan and marked so.

_Companion to `00_divergence_findings.md` (the defects) and `01_locations.tsv` (196 locations,
196/196 verified strict by `verify_locations.py`)._

Methodology designed by three independent read-only passes over the tree; every `BEFORE` block is
copied from disk, not reconstructed. Written up, sequenced and adversarially checked here.

---

## 0. How to read this, and the two rules that govern it

**Rule 1 — conventions and units before vocabularies.** Folding return types while four input
conventions and two unit scales remain in place converts a *visible* divergence into an *invisible*
one. Every consolidation item below is sequenced after the unit fix it depends on.

**Rule 2 — a fix that changes shipped, calibrated behaviour is a design ruling, not routine work.**
Four items are balance changes wearing bugfix clothing. They are marked **HELD** and carry the exact
question plus options with consequences. Per CLAUDE.md §2, holding must be *loud*: they must not be
bundled into a routine PR on the assumption someone ratifies them later.

Each item states: defect · files with line numbers · order rationale · byte-exact BEFORE/AFTER ·
blast radius · the guard that makes recurrence impossible · verification command · rollback signal.

**Every guard must be able to fail.** Each carries the mutation that kills it. A guard that cannot
observe the defect it excludes is absent, not weak (§0.1 point 2).

### Global sequencing

| Phase | Items | Moves goldens? |
|---|---|---|
| **P0** Behaviour-preserving consolidation | B1, B2, B4, B5, B6, B11 | No — a diff here means a transcription error |
| **P1** Bugfix against the code's own cited canon | B3, B7, B8, B9, B10 | B3 and B10 yes; declare in-commit |
| **P2** Gates and exports | C-series (pending) | Backlog must be counted first |
| **P3** Resolution core | A-series (pending) | Yes, extensively |
| **P4** HELD for ruling | B13, B14, B12, B11-bounds | Per ruling |

Sections A (resolution core) and C (gates/tooling) are **pending** — their methodology passes had not
returned when this was written. Section B is complete.

---

## Section B — units, state and cross-scale (complete)

### B0 · NEW FINDING — the Mass Seizure degree inversion, found while checking B4

Not in the audit; found verifying B4's preconditions, and it **changes what B4 must do**.

At `systems/factions/sim/mass_seizure.py:275-279`, the Success branch is **uncapped** while the
Overwhelming branch is capped at 3:

```python
base_accord = max(pt // 2 + 1, SEIZURE_ACCORD_FLOOR)   # :275  — no upper bound
if degree == 'Overwhelming':
    starting_accord = min(pt // 2 + 2, 3)              # :277  — capped at 3
else:
    starting_accord = base_accord                      # :279
```

Measured across the four real starting PT values (`PT_MAP` via `STARTING_PT`):

| pt | Success index | Overwhelming index | today | after the B4 unit fix |
|---|---|---|---|---|
| 2.5 | 2.0 | 3.0 | S→1, OW→1 | S→2, OW→3 |
| 4.0 | 3.0 | 3 | S→1, OW→1 | S→3, OW→3 |
| 5.5 | 3.0 | 3 | S→1, OW→1 | S→3, OW→3 |
| **7.0** | **4.0** | **3** | S→2, OW→1 | **S→4, OW→3** |

Two defects, both currently masked by the unit bug that flattens everything to bucket 1:

1. **At pt = 7.0, Success outranks Overwhelming.** A degree inversion.
2. **At pt ≥ 4.0, Overwhelming confers nothing over Success** — the cap binds.

**Applying B4 alone amplifies both**, because the unit bug is what currently compresses the range.
So B4 must not ship alone. Also note `pt // 2` is float division on a float field, so
`starting_accord` can be `4.0`; `ACCORD_MAP[4.0]` resolves only because float/int hash equality.

**HELD — question for Jordan:** should the Overwhelming cap of 3 be raised to 4 (making Overwhelming
weakly dominant), or the Success branch capped at 3 (making them equal at high PT), or the whole
ladder re-derived? Canon §3.2 gives the Accord values but the interaction with the PT term is not
stated. **Recommendation:** cap the Success branch at `min(..., 3)` and raise Overwhelming to
`min(..., 4)` — restores monotonicity with the smallest change. Do not ship B4 until this is ruled.

---

### B1 · Bind the seven private `MULTS` literals to the owner

**Defect** D12 · **Files** `crown_initiative.py:32-34`, `council_solmund.py:24`,
`excommunication.py:35`, `absolution.py:26-27`; owner `engine/autoload/game_state.py:42`
**Order** FIRST — zero behaviour change, and B3 edits lines that currently use `_MULTS_ACCORD`.

```python
# BEFORE — crown_initiative.py:32-34
_MULTS_W = 100  # [canonical: params/factions.md §Stat multipliers — W=100]
_MULTS_L = 20   # [canonical: params/factions.md §Stat multipliers — L=20]
_MULTS_ACCORD = 10  # [canonical: game_state.py MULTS — accord=10]

# AFTER (add `from engine.autoload.game_state import MULTS` after :28)
_MULTS_W = MULTS['W']            # [canonical: game_state.py:42 MULTS — BOUND, not re-spelled]
_MULTS_L = MULTS['L']            # [canonical: game_state MULTS]
_MULTS_ACCORD = MULTS['accord']  # [canonical: game_state MULTS]
```

Same transformation at `council_solmund.py:24` (`_MULTS_L = MULTS['L']`), `excommunication.py:35`,
`absolution.py:26-27` (`_MULTS_L`, `_MULTS_STA = MULTS['Sta']`).

Note the existing citations to `params/factions.md` are **also stale** — that tree was evacuated
2026-08-05. The new comments cite the live owner.

**Blast radius** None. Every replaced literal equals its owner value. No golden movement is legal.
**Guard** B2. **Verify** `python -m pytest engine/tests tests/valoria -q` — green.
**Rollback** Any golden diff means a key name is wrong (which would raise `KeyError` at import).

---

### B2 · Guard — `MULTS` may be spelled as a numeric literal exactly once

**Defect** D12 · **File** NEW `tests/valoria/test_owned_constants_sweep.py` · **Order** immediately after B1.

**The model case does not transfer directly, and this is the interesting part.**
`test_combat_invariants.py:298` uses `is`-identity, which works for floats. For `MULTS` the values are
small ints, and **CPython interns them** — `20 is 20` is `True`, so identity can never detect a
re-typed `_MULTS_L = 20`. Verified. The transferable half is the AST scan
(`test_combat_invariants.py:316`), so this guard is AST-only.

It scans `systems/` and `engine/` for a module-level assignment whose target matches
`^_?MULTS(_[A-Z]+)?$` and whose RHS is a numeric literal. The legal form is `MULTS['L']`.

**Killable mutation** Revert `crown_initiative.py:33` to `_MULTS_L = 20` → fails naming that line.
**Self-test** Include `test_the_guard_itself_can_fail`, asserting the matcher sees the defect shape.
**Verify** Stash B1 → must FAIL listing 4 files / 7 names; unstash → PASS.

---

### B3 · One owner for "+1 canonical Accord", and fix the half-step write

**Defect** D-accord-step · **Files** `game_state.py:58-59` (new constant),
`crown_initiative.py:102`, `:110` · **Order** after B1; before B6.

Add to `game_state.py` below `PT_MAP`:

```python
ACCORD_STEP_GRANULAR = (ACCORD_MAP[1] - ACCORD_MAP[0]) * MULTS['accord']   # == 15.0
```

Derived from the owner tables, so it cannot desync. Then:

```python
# BEFORE crown_initiative.py:102
                t.adjust_accord(15)  # +1.5 stat-tier (canonical "1 -> 2") per v17 mc_v17:483
# AFTER
                t.adjust_accord(ACCORD_STEP_GRANULAR)  # +1 canonical Accord per v17 mc_v17:483

# BEFORE crown_initiative.py:110
            target_t.adjust_accord(_MULTS_ACCORD)  # +1.0 stat-tier
# AFTER
            target_t.adjust_accord(ACCORD_STEP_GRANULAR)  # +1 canonical Accord [BUGFIX: was +1.0, a no-op from mid-bucket]
```

`_MULTS_ACCORD` then has zero uses — delete it from B1's block.

**Why `:110` is a bugfix, not a balance change:** both lines are commented "+1 Accord (canonical)".
`ACCORD_MAP` steps are uniformly 1.5 wide, so `+1.0` from a mid-bucket value changes **no canonical
bucket at all**. The code does not do what its own citation says.

**Blast radius** `crown_initiative` is campaign-reachable, so **the mc_v18 golden re-records.**
Declare it in-commit citing this item.
**Guard** B6's literal-argument registry, plus a value test asserting the step crosses exactly one
bucket from every bucket.
**Rollback** If the golden does *not* move, `:110` never fired in the seeded window — the fix is
still correct.

---

### B4 · Mass Seizure writes a canonical index onto the continuous field — **BLOCKED ON B0**

**Defect** D3 · **Files** `mass_seizure.py:50`, `:290-295` · **Order** after B0's ruling; before B5, B6.

```python
# BEFORE mass_seizure.py:290-295
        if seized:
            t.owner = 'Church'
            # Convert int accord to ACCORD_MAP-style continuous if needed; for now,
            # set directly using same continuous scale game_state uses
            t.accord = float(starting_accord)

# AFTER (import ACCORD_MAP at :50)
        if seized:
            t.owner = 'Church'
            # starting_accord is a CANONICAL INDEX (0-4); Territory.accord is CONTINUOUS.
            # Route through ACCORD_MAP like parliamentary_transfer.py:278 — the raw float
            # write made canon Accord 2 AND 3 both read back as canonical 1. [audit D3]
            t.accord = ACCORD_MAP[starting_accord]
```

**Blast radius** Zero callers (verified: the symbol appears only in its own module's docstrings and
`def`), so zero golden movement. But `is_available()` advertises it, so it must be correct before
anyone wires it.
**Do not ship without B0.** Alone, this amplifies the degree inversion.
**Guard** B6. **Rollback** Any golden movement contradicts the zero-caller measurement — stop and re-grep.

---

### B5 · One owner for the `Territory.owner` ↔ `Faction.territories` dual-write

**Defect** D3-second-half · **Files** new `game_state.transfer_territory`; route
`mass_seizure.py:292`, `faction_action.py:461-472`, `parliamentary_transfer.py:273-274,293`
**Order** after B4.

`parliamentary_transfer.py:279-292` already *files* this consolidation in a comment
("THIRD `t.owner = <faction>` owner-assign site"). This item executes filed work.

```python
def transfer_territory(world: "World", tid: str, new_owner: str) -> None:
    """SINGLE OWNER of the territory-ownership dual-write (audit D3).

    Ownership is represented BOTH as Territory.owner and as membership in
    Faction.territories (parliamentary_transfer._holder_of derives the holder by
    scanning the lists). Every transfer must update both, atomically, here — the
    desync has now occurred twice. Removes tid from EVERY faction list so a
    pre-existing desync is repaired rather than propagated."""
    t = world.territories.get(tid)
    for name, f in world.factions.items():
        if name != new_owner and tid in f.territories:
            f.territories.remove(tid)
    if t is not None:
        t.owner = new_owner
    nf = world.factions.get(new_owner)
    if nf is not None and tid not in nf.territories:
        nf.territories.append(tid)
```

At `faction_action.py:461-472` the loser-Legitimacy `adjust('L', -10)` **must stay before** the
transfer call — it is RNG-adjacent and reordering moves the draw stream.

**Blast radius** Operation-for-operation identical in healthy state ⇒ goldens must **not** move. The
only behavioural delta is in already-desynced states, which become unreachable once this lands.
**Guard** B6's `owner` key. **Rollback** A golden diff means an operation-order mistake; revert the
`faction_action` hunk first.

---

### B6 · Guard — field-parameterized write sweep for `accord` / `pt` / `owner` / `standing`

**Defect** D3, and the whole canonical-index-vs-continuous pattern · **File** NEW
`tests/valoria/test_world_state_write_sweep.py` · **Order** after B3–B5.

Modelled on `test_morale_write_sweep.py`'s `_CELL_OWNED` registry (`:168-207`) — **field-parameterized,
so covering a new field is adding one dict key**, not writing a new test. That property is the whole
point; a hand-listed test rots.

Registry shape, one entry per owned field, each with an annotated allowed-set:

```python
_WRITE_OWNED = {
    'accord':   {'owners': 'adjust_accord (relative) or ACCORD_MAP[...] (absolute)', 'allowed': {...}},
    'pt':       {'owners': 'adjust_pt or PT_MAP[...]',                               'allowed': {...}},
    'owner':    {'owners': 'game_state.transfer_territory',                          'allowed': {...}},
    'standing': {'owners': 'Faction.adjust_standing',                                'allowed': {...}},
}
```

Plus a second test rejecting **numeric literals passed to `adjust_accord`/`adjust_pt`** — the other
face of B3. `faction_action.py:546`'s Govern `+15/+10` is whitelisted with its reason: it cites a
continuous-tier grant, not a canonical step.

**Killable mutations** Reintroduce `t.accord = float(starting_accord)`; reintroduce
`t.owner = 'Church'`; revert `crown_initiative.py:110` to a literal. Each must fail.
**When it flags a legitimate new write**, the fix is an annotated allowed-set entry with a reason —
**never** a regex change.

---

### B7 · Effects declared before a swallowing `try`

**Defect** D8 · **Files** `knots.py:338-367`, `opposing.py:236-249`, and
`contest_legacy_stub.py:239-248` — a **fourth site found by sweeping the pattern rather than the
citations** · **Order** independent; before B8.

The `except ImportError` legs are provably dead: both callees exist and import cleanly
(`coherence.py:138`, `conviction.py:167`). Keep the late import (that is the module's stated
cycle posture); delete only the `try`/`except` frame, and **record the effect after the call
succeeds**:

```python
# BEFORE knots.py:361-367
        consequences['coherence_delta'] = RUPTURE_COHERENCE_LOSS
        try:
            from systems.threadwork.sim.coherence import apply_coherence_delta
            apply_coherence_delta(actor, RUPTURE_COHERENCE_LOSS,
                                  f"Knot rupture (id={knot_id})", world=world)
        except (ImportError, AttributeError):
            pass

# AFTER
        # Effect recorded AFTER the call succeeds; no swallow. The dict may not lie. [audit D8]
        from systems.threadwork.sim.coherence import apply_coherence_delta
        apply_coherence_delta(actor, RUPTURE_COHERENCE_LOSS,
                              f"Knot rupture (id={knot_id})", world=world)
        consequences['coherence_delta'] = RUPTURE_COHERENCE_LOSS
```

**Blast radius** No RNG or arithmetic change ⇒ goldens must not move.
**Rollback** *A new `AttributeError` surfacing in tests is the guard working* — it was previously
swallowed while the dict lied. Fix the surfaced bug; do not restore the `except`.

---

### B8 · Guard — no `pass`-swallowed `ImportError`/`AttributeError` in sim code

**Defect** D8 · **File** NEW `tests/valoria/test_no_swallowed_effect_sweep.py` · **Order** after B7.

AST scan: no `ExceptHandler` catching `ImportError` or `AttributeError` with a body of only `pass`,
anywhere in `systems/` or `engine/` outside test directories.

**Killable mutation** Restore the frame at the `knots.py` rupture leg → fails naming that file:line.
**Verify** Pre-B7 tree → fails with exactly the four known sites; post-B7 → green.

---

### B9 · `province_accord` exceeds the canonical range

**Defect** D-range · **File** `systems/settlements/sim/registry.py:184-190` · **Order** independent.

`Settlement.order` is 0–5; canonical Accord is 0–4. An all-order-5 province yields **5**, outside the
range, polluting `accounting._probe_province_accord_drift`'s like-for-like comparison — whose
docstring claims floor-of-mean "clamps the same range". The claim is false at the top edge.

```python
# AFTER — the only change
    return min(4, math.floor(sum(m.order for m in members) / len(members)))
```

**Blast radius** Report-only probe; no goldens. **Rollback** If the probe's test fails, its fixture
depended on the out-of-range value — fix the fixture's orders, not the clamp.

---

### B10 · The one-season Mandate penalty that compounds forever

**Defect** D7 · **Files** `game_state.py:209` (new `World` field), `:327-329` (serialize),
`:416-420` (restore), `season_manager.py:31-43`, `parliamentary_vote.py:206-218`
**Order** after B1. **Bugfix, not a ruling** — `parliamentary_vote.py:72` cites "Mandate −1 **for one
season**" and `:217` defers restoration to `season_manager`, which has no such logic (verified: 49
lines, none of it restoration).

Add `World.pending_stat_restorations: list`, serialized and restored (older snapshots default to
empty). `season_manager.advance_season` drains it. The applier records the **realized** give-back:

```python
            before_l = fac.L
            fac.adjust("L", BG_VOTE_TOTAL_VICTORY_MANDATE_DELTA * MULTS["L"])
            realized = before_l - fac.L   # adjust may clamp at the floor
```

so cited == applied even when the penalty clamped — the `strip_points` precedent
(`contest/primitives.py:37`).

**Blast radius** If any seeded vote hits Total Victory the golden re-records; if none does, it does
not. Run the regen either way and compare.
**Rollback** Symptom of a misplaced `realized` capture is L creeping *up* across repeated total
victories; the guard's exact-equality assertion catches that mechanism.

---

### B11 · `Faction.standing` — one owner now, bounds held

**Defect** D-standing · **Files** `game_state.py:114`; ten writes at `crown_initiative.py:97,115,118,166,176,253,266,269`, `absolution.py:85`, `parliamentary_transfer.py:311`
**Order** after B1–B3. Routing lands now with **no clamp** (zero behaviour change); bounds are held.

**Recommended: a dedicated integer mutator — not the contest `Standing` primitive, and not `adjust()`.**
The argument, which I endorse:

- `contest.primitives.Standing` is a float 0–10 tracker with `START = 5`. Rebasing onto it silently
  adds +5 to every dice pool at `crown_initiative.py:80,308`, turns a serialized int into an object,
  and imports a venue-local shape into faction scale — the shape-divergence guardrail (§10).
- `adjust()` is the wrong domain: it divides by `MULTS[stat]` and clamps to `[0.5, 7.0]`. `standing`
  is a signed integer pool modifier that legitimately starts at 0 and goes negative
  (`crown_initiative.py:118` fires `-= 1` from 0).

```python
    def adjust_standing(self, delta: int,
                        floor: int | None = None, ceiling: int | None = None):
        """SINGLE OWNER of Faction.standing writes (audit D-standing). floor/ceiling are
        None PENDING JORDAN'S BOUND RULING: the field shipped unbounded and any clamp is a
        balance change."""
```

**HELD — bounds.** Run this first and attach the output to the ruling request; it monkeypatches the
new mutator to record the empirical envelope across a seeded batch:

```
python - <<'EOF'
from engine.autoload import game_state as gs
lo = hi = 0
orig = gs.Faction.adjust_standing
def probe(self, delta, floor=None, ceiling=None):
    global lo, hi
    orig(self, delta, floor, ceiling); lo = min(lo, self.standing); hi = max(hi, self.standing)
gs.Faction.adjust_standing = probe
from engine.mc_v18 import run_batch; run_batch(n=2, base_seed=0)
print('observed standing range:', lo, '..', hi)
EOF
```

If Jordan's bounds contain the envelope the clamp is golden-inert; if not, the ruling should say so
knowingly rather than discovering it in a re-record.

**Guard** Add `'standing'` to B6's registry — the payoff of field-parameterizing it.

---

### B12 · **HELD** — pin the dead Political Stability victory leg

**Defect** D2 · **File** `engine/autoload/victory.py:73`

Do **not** invent a writer. The writers are specified in `peninsular_strain_v30.md §4` (battles,
revolts, eliminations advance Turmoil 0–10) and that module is unbuilt. The mapping and threshold in
`victory.py` are *correct once wired*.

Land now: an annotation at the read, plus a **tripwire** modelled on the repo's own dead-param pin
(`test_f7_smoke_oracle.py:175`) that fails the day a `Turmoil` writer appears — forcing deliberate
re-validation of `PS_MAX` instead of a silent go-live. The `create_world` seed is a dict literal, not
a per-key write, so it does not match by construction.

**Question:** (a) accept the pinned dead leg until §4 lands — **recommended**, nothing needs to change
but the writer; or (b) build the §4 writers now, making victory strictly harder (golden re-record).

---

### B13 · **HELD** — Muster's Wealth cost is 100× under-scaled

**Defect** D5 · **File** `faction_action.py:515` (constant at `:69`)

Arithmetic, no execution needed: `adjust('W', -1)` with `MULTS['W'] = 100` charges **−0.01 W**.

The reason this is a ruling and not a fix: **ED-FA-0009 retired the old W−3-on-Failure penalty on the
stated ground that the up-front cost carries the failure-penalty role.** At −0.01 it carries nothing,
and the old penalty is gone. A double buff shipped inside a golden re-record.

```python
# AFTER (Option A) — MULTS already imported at :34
    faction.adjust('W', -MUSTER_WEALTH_COST * MULTS['W'])  # [BUGFIX audit D5: was -0.01 W]
```

**Question:** (A) charge a true −1.0 stat-tier — Muster becomes a real fiscal decision and the pool
term `Mil + floor(W/2)` feeds back; goldens re-record and win-shares move. This is what the ED text
says. (B) Ratify the shipped behaviour, rewrite the ED-FA-0009 comments to say the cost is *token*,
and accept that the retired failure penalty was removed for a consideration that does not exist.
(C) A ruled intermediate.

**The current state is (B)'s behaviour wearing (A)'s comments.** That is the thing to decide.

**Measure it first:**
```
python -c "from engine.autoload import game_state; import random; from systems.factions.sim import faction_action; w=game_state.create_world(seed=0); f=w.factions['Crown']; b=f.W; faction_action._try_muster(f,w,random.Random(0)); print('W charged:', b-f.W)"
```
→ prints `0.01` today, `1.0` under Option A.

---

### B14 · **HELD** — continuous-vs-canonical comparisons in victory and insurgency promotion

**Defect** D2-second-half · **Files** `victory.py:28,71`; `insurgency_pipeline.py:44-48,228-231,237-245`
Correct model to copy: `npe.py:189`, which buckets before comparing.

- `victory.py:71` compares **continuous** accord to `ACCORD_MIN = 2.0`, where GD-1 states a
  **canonical index**. Continuous 2.5 = canonical 1 passes today; canon-correct requires ≥ 3.25.
  **One bucket lenient.**
- `insurgency_pipeline.py:230` compares a raw continuous mean to `4` (a canonical index per GD-3).
  **Two buckets lenient.** And at `:239` the PT split misclassifies RM vs parliamentary near the
  boundary in both directions.

**Question:** (A) fix both to canonical bucketing — victory gets strictly harder, promotion much
rarer; first confirm GD-3's "Accord ≥ 4" meant the index and was not authored against the continuous
scale. (B) Ratify the continuous thresholds and rewrite the constants to say CONTINUOUS explicitly —
no behaviour change, but GD-1/GD-3 prose needs an editorial amendment. (C) **Split** — fix the PT
*classification* (pure correctness; the fork is symmetric) and rule the two *difficulty* thresholds
separately. **(C) is my recommendation**: it separates a defect from a calibration decision.

Prerequisite either way: finish the filed move of `canonical_pt` into `canon_buckets.py`
(`canon_buckets.py:27-33` logs it), re-exporting from `game_state` so existing imports keep working.

---

## Section B — pattern summary

| Pattern | Single owner | Routed sites | Guard |
|---|---|---|---|
| Canonical-index vs continuous | `ACCORD_MAP`/`PT_MAP` + `canonical_accord`/`canonical_pt` + new `ACCORD_STEP_GRANULAR` | `mass_seizure:295`, `crown_initiative:102,110`, `victory:71`*, `insurgency_pipeline:228,237`*, `registry:190` | `test_world_state_write_sweep.py` + literal-argument registry + boundary pins |
| Private copy of an owned constant | `game_state.MULTS:42` | 7 copies in 4 modules | `test_owned_constants_sweep.py` (AST — identity is vacuous here) |
| Effect declared before a swallowing try | structural rule | `knots:347,362`, `opposing:237`, `contest_legacy_stub:239` | `test_no_swallowed_effect_sweep.py` |
| Dual-representation write | new `transfer_territory` | `mass_seizure:292`, `faction_action:461`, `parliamentary_transfer:273,293` | `owner` key in the write sweep |
| Unowned mutable stat | new `adjust_standing` | 10 sites | `standing` key in the write sweep |

\* post-ruling

**Held for Jordan, not to be landed silently:** B0 (seizure degree inversion), B13 (Muster cost),
B14 (victory/promotion thresholds), B11's bound values, B12's wiring choice.

---

## Sections A and C — pending

**A · Resolution core** (TN-blindness, 16 degree producers, the epsilon twins, the six-way per-die
table). The sharp question there is already visible: honouring TN 8/9 makes threadwork's binding
operations **harder than they have been for the entire calibration history**, so D1 is a balance
change disguised as a bugfix and will be marked HELD.

**C · Gates and tooling** (the dead co-file rule, the two gates that cannot fail, the export scanning
a superseded model). The governing constraint: **a repaired gate fails on a backlog, and the backlog
must be counted before the gate is switched on** — that is what turning on D4's Rule 4 means, and
`engine/params/` no longer exists to satisfy it.

Both sections will be appended here on the same contract as Section B.

---

## Section A — resolution core (complete)

### A0 · Sequencing verdict — the assumption I was carrying was wrong

I had assumed fixing the TN-blindness re-records every seeded golden. **It does not**, and the
reason is structural. Verified on disk:

1. **The draw stream is untouched.** `dice_engine.py:71` materialises `rolls` *before* `_die_result`
   is applied — `rolls = [rng.randint(1, 10) for _ in range(effective_pool)]`. Changing the face
   rule cannot change draw count or order. So determinism tests and
   `test_combat_draw_stream.py` (which keys per-method call counts, not lines) are unaffected.
2. **Every `tn != 7` caller is a campaign island.** Full census: threadwork
   (`operations.py:176`, `collective.py:163`, `opposing.py:143-144`) — the only `engine/` importer
   is `test_thread_mending_ed871.py`, and it uses TN-7 operations. `knots.py:222` is TN 7 anyway.
   The one campaign-reachable exception is the DEPRECATED `combat/sim/combat.py:212-214` (weapon
   TNs 5–8) via `scene_dispatch.py:273-274` while `DISPATCH_COMBAT_BRIDGE` is off — **measured, not
   assumed**, by the spy command in A5.

**A5 and A7 must not share a golden re-record even if both move goldens.** Two behaviour changes
under one re-record is precisely the confound §0.1 exists to prevent. Each carries its own
before/after values and its own falsifier.

### A1 · Pin the canon ladder — it has no test

**Defect** D1-precondition · **File** NEW `tests/valoria/test_degree_from_net_pin.py` · **Order** FIRST.

`degree_from_net` appears in zero test files (verified: one comment mention). Consolidating producers
onto an **unpinned owner** means a silent owner mutation propagates everywhere at once. This is the
precondition for every later item.

Parameterized table including the discriminating rows: `(7, 4) → SUCCESS` (additive `ob+3` would say
Overwhelming) and `(2, 1) → SUCCESS` (meets `2·ob` but under the PP-232 floor of 3), plus the full
Ob-20 exception.

**Mutation-kill** `net >= 2*ob` → `net >= ob+3` reds row `(7,4)`; `net >= 3` → `net >= 2` reds `(2,1)`.
**If any row fails against current source**, the ladder is not what its docstring claims — escalate, do not tune.

### A2 · Bind the unbound `random` in both collision twins, rng-injectable

**Defect** D9 · **Files** `units.py:28,255,299`; `tests/sim/mass_battle/hierarchy/units.py:2061,2105`

Land early: Pass-2n wires reachability and must find an **rng-injectable** signature, not a
module-global fallback — that is the exact non-determinism bug already fixed once at
`massbattle.py:1826-1830`. Add `rng=None` to the signature and `_r = rng if rng is not None else random`.
The canon twin's module alias is `_cell_random`, not `random`.

**Guard** `test_units_collision_rng.py` — executes the collision path for the first time with a
counting rng, asserting `rng.calls >= 1`. **Run it on unfixed code first and record the `NameError`**;
that artifact is the falsifier.
**Blast radius** Zero callers (that is the defect's cover), so goldens byte-identical. Any movement
means something *does* call it — stop and re-census.

### A3 · One owner for the per-die table and `TN_STANDARD`; add TN 9; kill the silent fallback

**Defect** D-perdie, D-tn7 · **Files** `dice_engine.py:54-62,88`; `sigma_leverage.py:73-79,98-101`

Move `TN_STANDARD` and the per-die table to `dice_engine` (the root primitive — `sigma_leverage` is
*downstream*, which is why the owner could never be imported). Then `sigma_leverage` binds:

```python
PER_DIE = dice_engine.PER_DIE                    # single owner (D-perdie)
TN_STANDARD = dice_engine.TN_STANDARD            # single owner, value unchanged (7)
MU_PER_DIE, SD_PER_DIE = PER_DIE[TN_STANDARD]    # (0.40, 0.800) — same floats
```

Add the TN 9 row (μ=0.20, σ=0.748, derived from the face rule — the canon table stops at TN 8, so
**flag the missing canon row to Jordan alongside A5**). Replace the silent
`.get(tn, _CONTINUOUS_PARAMS[7])` at `:88` with a raising `KeyError` — that fallback is *how* TN 8/9
resolved at the wrong odds undetected.

**Deliberately NOT touched:** `SIGMA_N_COEFF = 0.8`. It equals `PER_DIE[7][1]` by *documented
coincidence* (`sigma_leverage.py:186-187`); binding it would change its meaning from spec constant to
derived value. Already pinned by `test_net_boost_tn7_equals_sigma_n`.

**Blast radius** Values byte-identical for TN 6/7/8 ⇒ the 1,758-row parity golden is **not**
regenerated. Regenerating here would violate that file's own header rule ("never to make a red test
green"). **Guard** `is`-identity that `SL.PER_DIE is dice_engine.PER_DIE`, plus a raise-not-fallback test.

### A4 · TN drift tripwire across the ~15 spellings

**Defect** D-tn7 · **File** NEW `tests/valoria/test_tn_single_owner.py`

Deliberately a **guard, not a rebinding**: rewriting ten modules buys no behaviour and risks import
churn in path-hacked modules. The failure mode worth guarding is *silent divergence*. Parameterized
over the ten modules declaring a standard TN, asserting each equals the owner. Threadwork's
`TN_BINDING`/`TN_POP`/`TN_POP_BINDING` are excluded — they are non-standard **on purpose**.

### A5 · **HELD** — make `roll_pool` honour its TN

**Defect** D1 · **Files** `dice_engine.py:41-52,72`

```python
# AFTER — generalised exactly as the two independent discrete implementations already do
def _die_result(face: int, tn: int = 7) -> int:
    if face == 1:
        return -1
    if face == 10:
        return 2
    if tn <= face <= 9:
        return 1
    return 0
```
and `:72` becomes `net = sum(_die_result(face, tn) for face in rolls)`. **At TN 7 this is
byte-identical** to the hardcoded rule.

**Why held.** Honouring TN 8 cuts per-die EV 0.40 → 0.30 (−25% expected successes); TN 9 → 0.20
(−50%). *Every threadwork result to date was produced at TN 7 odds.* The fix is simultaneously a
canon restoration and an uncalibrated balance change.

**Question:** (a) fix and let TN 8/9 go live — canon-as-written; threadwork is a verified campaign
island so no golden moves unless the measurement says so; prior threadwork sim observations are
invalidated. (b) Fix the engine but re-declare the threadwork TNs to 7 with a loud `[PROVISIONAL]`
marker and an ED, preserving observed behaviour while contradicting PP-619. (c) Leave it TN-blind —
**recommend against**: the continuous path already honours TN, so the engine disagrees with itself,
and *both* independent mass-battle implementations already generalise the rule. **TN-blindness is
the outlier, not the convention.** Recommendation: **(a)**.

**Measure before landing** — spy on `resolve_combat_round` across golden seeds 0/1. `{'n': 0}` means
no re-record anywhere; `n > 0` with any tn ≠ 7 means re-record in *this* commit, citing this item as
sole cause.

**Guard** Exhaustive face-rule table over TN 6–9; a same-seed/same-draws/different-net witness
(`r7.rolls == r8.rolls` but `r7.net != r8.net` — a TN-blind engine ties here); and a
discrete-vs-continuous agreement check at 5 standard errors, which is the "engine disagrees with
itself" half. **Run the guard on unfixed code first and record both reds.**

### A6 · Silent degree consumers become loud

**Defect** D1-consumers · **Files** `domain_echo.py:89-95`, `echo_transport.py:425`, `wrapper.py:329-331`

Order matters: with strict consumers in place, any label typo introduced by A7's rerouting **crashes
in tests instead of silently killing echoes**.

Byte-exact for every currently-flowing value (producer census: `scene_dispatch` emits only
`Success`/`Partial`/`Failure`; `core.degree` only its four lowercase tokens). The worst of the three
is `wrapper.py:329`, whose bare `else` promoted *any* unrecognised label — including a Capitalised
`'Success'` — to overwhelming:

```python
        elif deg=='overwhelming':
            ...
        else:
            raise ValueError(f"unrecognised degree label {deg!r} from core.degree — closed set: fail/partial/success/overwhelming; an unknown label must never resolve as overwhelming")
```

**Rollback** A campaign crash naming this `ValueError` means a live producer emits off-vocabulary
degrees. **Fix the producer; never re-silence the consumer.**

### A7 · **HELD** — one owner for the Capitalised ladder; retire the four `Ob+3` copies

**Defect** D-degree · **Files** add `dice_engine.degree_label`; reroute `operations.py:134-142`,
`collective.py:166-173`, `mass_seizure.py:264-271`, `knots.py:225-233`

```python
def degree_label(net: int | float, ob: int | float) -> str:
    """Capitalised-string surface of degree_from_net — the ONE canon ladder."""
    return degree_from_net(net, ob).value.capitalize()
```

`operations._compute_degree`'s docstring already claims "standard dice-engine semantics" and its body
was not. The delegate makes the claim true.

**Why held.** Canon is explicit (`net ≥ 2·Ob AND ≥ 3`) and **no design doc anywhere states an `Ob+3`
bar** — corpus-wide search found only this audit's own findings. Consolidating shifts behaviour in
both directions: at Ob ≤ 2 canon is *more* generous (more Overwhelming Locks, more `TIER_CLOSE`
knots); at Ob ≥ 4 canon is *stricter*.

**Question:** (a) consolidate onto canon — **recommended**; all four are islands or measured-zero-fire.
(b) Ratify `Ob+3` as a deliberate house ladder — then it gets **one** named owner plus an exception
clause in the canon table, and the four inline copies still die.

**The LEAVE list — six producers that must NOT be consolidated**, each a different contract:

| Producer | Why it stays |
|---|---|
| `sigma_leverage.degree:284` | Documented deliberate contest variant, pinned by the 1,758-row golden. Touching it is golden vandalism |
| `faction_action._degree:97` | A **d6 ≥ 4 margin** ladder with Ob pre-subtracted — not the d10 system. Consolidating it *because it is named `_degree`* is pattern-matching on the term |
| `opposing._degree_label:87` | Documented §2.6 three-degree shorthand (`Meets`) |
| `combat/sim/combat.py:161` | DEPRECATED, frozen byte-exact until the bridge flip; deletion rides that flip |
| `massbattle.py:1838` | Not a dice ladder — a battle-outcome→vocabulary adapter |
| `combat_engine_v1/core.py:57` | ER-2 continuity-corrected continuous banding, self-documented as deliberately unrouted |

That list is the discriminating judgment in this section. Six of sixteen producers look like copies
and are not.

### A8 · Close the epsilon divergence by **deletion, not by porting the epsilon**

**Defect** D-epsilon · **Files** `massbattle.py:640-647,951-952,1517`

I had assumed the fix was to port `_DEGREE_EPS` into the systems twin. **That is wrong**, and the
reason is verified: `massbattle.roll_pool` (`:627-638`) accumulates `net` in integer steps and returns
an **int**. An epsilon has nothing to recover there. The epsilon belongs only where `net` is
continuous — the J2-canon twin, which has it and is pinned.

So: delete the dead ladder (`compute_degree`, `DAMAGE_BY_DEGREE`, and the three dead `a_deg`/`b_deg`
assignments), leaving a tombstone comment so the next reader does not re-derive it. The twins then
cannot diverge on a surface only one of them uses.

**Blast radius** No RNG consumed ⇒ goldens byte-identical. **Guard** assert the names stay absent
from the module.

### A9 · Drift guard for the copy that cannot be rebound

**Defect** D-perdie residual · The canon twin's `_SIG` (`resolution.py:195`) is function-local in a
path-local module that must stay standalone-runnable, so rebinding is unavailable. Guard the equality
instead — recover σ through the arithmetic (`_sigma_net_boost(1, 1, tn) / _sigma_softcap(1)`) and
compare to the owner table. Per §0.1 point 5, **the guard is what makes the copy tolerable.**

