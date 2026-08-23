# Suite 03 — Competing Vocabularies, Adjudicated

**Status:** ADJUDICATED REGISTER. Every entry below was produced by a sweep, attacked by a
structurally independent read-only critic, and then re-read at source before landing here. Roughly a
third of the sweep's original findings did not survive that process; **the overturns are kept in place
rather than deleted**, because the sweep's failure mode is more instructive than its successes.

---

## §0 The taxonomy, and the error class that governs it

Four kinds of thing get lumped together as "conflict," and they want different remedies:

| | Definition | Remedy |
|---|---|---|
| **CONFLICT** | Two surfaces state incompatible things about the same referent | Rule one wrong |
| **DUPLICATION** | The same thing stated twice, consistently | Name one owner; the copies become citations |
| **COMPETITION** | Two mechanisms doing one job | Retire one, or partition the job |
| **OVERLAP** | Partial intersection of two legitimate concepts | Name the boundary — **do not merge** |

**The error class.** This session's dominant failure was matching a **name** across two surfaces and
inferring a defect **without establishing that the two surfaces discuss the same thing**. It was
committed at least six times, caught six times, and it is the reason this document reports overturns
as prominently as findings. A sweep that finds shared tokens produces *candidates*; only reading
produces *findings*.

The check is one question: **do these two surfaces have the same referent?** If they do not, a shared
word is a legibility hazard at worst — not a contradiction.

---

## §1 Master register

Verdict column: ✅ stands · ⚠️ narrowed · ❌ overturned.

| # | Topic | Claim as swept | Verdict | What is actually true |
|---|---|---|---|---|
| V1 | Convictions | Code roster ≠ authored roster | ✅ **CONFLICT** | §2.1 — and it is a documented supersession, not drift |
| V2 | Degree/outcome | Nine rival outcome vocabularies in the key-type registry | ⚠️ **narrowed** | §3.1 — three ladder-shaped, six disjoint enums, plus a **tenth** the sweep missed |
| V3 | Degree/outcome | `graze` has four incompatible meanings | ⚠️ **narrowed + sharpened** | §3.2 — two semantics, one declared; the real defect is behavioural port/oracle divergence |
| V4 | Scale | "A Foundational Weaving cannot emit a Key" | ❌ **overturned** | §4.1 — three different concepts share the word "scale" |
| V5 | Threadwork | Scale roster carries both `Field` and `Territorial` | ✅ **CONFLICT** | §4.2 — the residue of V4, and real |
| V6 | Factions | Church-dominance threshold is 40/60/65/100 across four surfaces | ❌ **overturned** | §5.1 — one graduated milestone table |
| V7 | Vocabulary | `AMPLIFY` / `DIVERGE` exist nowhere in the tree | ❌ **overturned** | §5.2 — ED-150 / PP-529 / PP-301; stale, not phantom |
| V8 | Threadwork | The 4-member Gap scale is invented | ❌ **overturned** | §5.2 — matches `threadwork_v30.md:468-471` |
| V9 | Voice | The canonical voice doc is cited by nothing | ✅ **stands**, with a fix site | §6 |
| V10 | Pools | Two canonical fieldwork docs disagree on the Knot pool | ✅ **CONFLICT** | Suite 01 §3.2 |
| V11 | Machinery | The `[ASSUMPTION]` resolver count is 10/27 | ❌ **overturned** | §7.1 — it is **11/27**, and the "correction" was queued for CLAUDE.md |
| V12 | Machinery | `scene.contest_resolved` is emitted every season | ⚠️ **narrowed** | §7.2 — conditional on winner + degree |
| V13 | Machinery | Chronicle band bug at `narrative.py:114/:126` | ⚠️ **citation wrong, substance right** | §7.3 — the defect is at `:88/:92` |
| V14 | Combat | `combat/sim/combat.py` competes with `combat_engine_v1` | ❌ **not a live conflict** | §8 — DEPRECATED banner names its supersession |
| V15 | Threadwork | `_compute_degree` is a second degree ladder | ❌ **not a conflict** | §8 — a delegating adapter, and its docstring says so |
| V16 | Social contest | The armature's 4th axis drifts from canon's Solidarity | ❌ **not a conflict** | §8 — a ratified deliberate substitution with a stated reason |

---

## §2 Person vocabulary

### §2.1 Convictions — CONFLICT, with a known cause

Three rosters are in play:

| Surface | Members | Count |
|---|---|---|
| `systems/characters/sim/conviction.py:44-48` | Faith, Order, **Reason**, Equity, Precedent, **Autonomy**, **Continuity**, Community, Warden | 9 |
| `references/npc_registry.yaml` (what 46 characters actually use) | Authority, Order, Utility, Precedent, Equity, Faith, Liberty, Warden, Honor, Community, Scholastic, Virtue, Identity | 13 |
| `systems/_architecture/conviction_axis_matrix_v30.md:24-38` | the same 13 | 13 |

The intersection is **six**. Seven authored convictions silently no-op in code
(`conviction.py:191-193` returns `magnitude=0`); three coded convictions are used by nobody.

**This is not an unexplained divergence.** `systems/npcs/npc_behavior_v30.md:30` states the
supersession outright: the legacy 9 is superseded, **Reason and Continuity are deprecated**, and
**Autonomy is renamed Liberty**. That accounts for the residue exactly — the three orphaned code names
are the two deprecations plus the old name of Liberty.

**Remedy: propagation, not adjudication.** The ruling was made and dated; it never reached the code.
The measured player-facing consequence is in Suite 02 §2.3.

A fourth roster is worth naming because it will be found: `systems/world/sim/npe.py:78-80` carries an
**eight**-member roster, quoted inline from `investigation_systems_v30.md:84`. The code faithfully
reproduces its canon source; the divergence lives in canon, so the fix site is the design doc.

### §2.2 `'Loyalty'` — a fifth name, in neither roster

`systems/fieldwork/sim/knots.py:351-353` calls `apply_conviction_scar(..., conviction='Loyalty')`.
`'Loyalty'` is in neither the coded 9 nor the canonical 13, so the call is a silent no-op.

Three things make this the sharpest single exhibit in the register:

1. `knots.py:346` sets `consequences['conviction_scar'] = 1` **before** the call — so the caller
   reports a scar that was never recorded.
2. `tests/valoria/test_knots_ed912.py:103-116` asserts `c["conviction_scar"] == 1` and never calls
   `get_state`. **The test passes by construction and can never observe the failure it exists to
   exclude** — CLAUDE.md §0.1 point 2, in the wild.
3. A `try/except` around the call would not catch it either. The no-op is a return value, not a raise.

### §2.3 Voice markers — OVERLAP, not conflict

Canon defines four Resonant Styles (`npc_behavior_v30.md:33-42`). The registry uses exactly those
four. `systems/social_contest/sim/contest/armature.py:145-180` runs a four-axis vector whose fourth
axis is **Insinuation** rather than Solidarity — a substitution **ratified by Jordan at Gate C
(2026-07-02)** with its reason recorded in the file: Solidarity is Knot-gated and relational, which
cannot apply to a third-party adjudicator.

This is the model case for the taxonomy's OVERLAP row. Two legitimate concepts partially intersect;
the boundary is named; nothing needs merging. Recorded here only so the next sweep does not re-raise
it.

The one live hazard is nominal: **"Authority" is both a conviction (14 characters) and a Resonant
Style (2 characters)**, on different mechanical axes, in the same file.

### §2.4 Cultural labels — the shape, not the values

Covered in Suite 02 §2.6: `cultural_label` and `self_other_initial` each live at two nesting depths
with zero overlap, partitioning the value vocabulary by depth, and the vocabulary itself carries one
unnormalised pair (`altonian` / `altonian_imperial`).

---

## §3 Outcome and degree vocabulary

### §3.1 The key-type registry — NARROWED, and a tenth found

The sweep reported nine rival outcome vocabularies in
`systems/_architecture/key_type_registry_v30.md`. Read at all nine cited lines, **only three are
degree-ladder-shaped**:

| Line | Enumeration | Ladder-shaped? |
|---|---|---|
| `:198` | `success \| partial \| failure` | ✅ |
| `:403` | `overwhelming \| success \| partial \| failure \| unknown` | ✅ |
| `:942` | `graze \| partial \| success \| overwhelming` | ✅ (field named `degree`) |
| `:52`, `:845` | contest result | ❌ different referent |
| `:568` | event lifecycle states | ❌ |
| `:657` | challenge result | ❌ |
| `:905` | win attribution | ❌ |
| `:974` | echo category | ❌ |

Six of the nine were the name-match error: `outcome`-shaped enums with disjoint referents counted as
rival ladders.

**The sweep also missed one.** `key_type_registry_v30.md:887` —
`scene.investigation_resolved → finding # exonerated | guilty | inconclusive`. A tenth enumeration,
and the only one that carries the *fieldwork* verdict vocabulary. Whatever the pattern is, the sweep
under-counted it while over-counting the ladders.

On `:942` specifically: `:939` describes `scene.combat_hit` as "a landed blow," so the field
enumerates **hit qualities** — mirroring `combat_engine_v1/core.py:126 QUAL` exactly. "It puts `graze`
where `failure` belongs" is therefore wrong. What survives is a genuine hazard: **it shares the field
name `degree` with the ruled ladder**, which a Godot importer binding by field name would conflate.

### §3.2 `graze` — SOFTENED, then SHARPENED into something worse

Two semantics, not four: **wound quality** and **percussion impulse**. One of them is explicitly
declared: `systems/combat/combat_engine_v1/config.py:251-256` states that `PERC_QUAL` "is
DELIBERATELY NOT `core.QUAL` … the divergence is stated rather than left implicit." And
`godot/skeleton/engines/combat/resources/combat_config.gd:27` is a **faithful export** of
`core.py:126`, not a third meaning.

But reading the two engines side by side surfaced a real defect the sweep had not found — a
**behavioural port/oracle divergence on `partial`**:

| | Oracle | Port |
|---|---|---|
| | `core.py:527`, `wrapper.py:321-324` | `strike_module.gd:74-80` |
| **partial →** | `damage()` returns 0. A *probabilistic* graze strike only under dodge/parry (`PARTIAL_DODGE_GRAZE` / `PARTIAL_PARRY_GRAZE`); otherwise a **bind**, no damage. | **Unconditionally** becomes graze quality and **deals damage**. |

Different distributions on every partial. **Narrowing caveat, and it matters:**
`strike_module.gd:13-15` declares defensive-mode selection and bind/winding **out of the slice's
scope**. So this is a declared-incomplete slice, not a covert ED-1050-style port "correction". Real
divergence; announced scope.

---

## §4 Scale vocabulary

### §4.1 The headline was OVERTURNED — three concepts, one word

The sweep's flagship finding was: *"A Foundational-depth Weaving — Ob 13, TS 90 — cannot emit a Key."*
It rests on matching the word **scale** across three surfaces that are not about the same thing:

| Surface | What it actually is | Members |
|---|---|---|
| `engine/substrate/keys.py:64-65` `SCALES` | The roster of legal **`Key.scale_signature`** values | personal, settlement, territory, peninsula |
| `systems/_architecture/scale_transitions_v30.md:28-36` | A **Thread-operation difficulty table** (Base Ob / Min TS / Coherence cost) | Object, Personal, Relational, **Territorial**, Structural |
| `systems/threadwork/sim/operations.py:52-61` `DEPTH_OB` | **One of three Ob axes** (alongside `BREADTH_OB` at `:82-88` and `DISTANCE_OB` at `:91-96`) | Object, Personal, Relational, **Field**, Structural, Foundational |

A Key's `scale_signature` and a Thread operation's depth are different quantities that happen to share
a word. And the claim is unreachable regardless: **`systems/threadwork/sim/` constructs no Keys at
all** — the package's only substrate import is `stubwire` (`rendering.py:18`), and the only other
`Key` occurrence is a dict comment (`coherence.py:53`). `keys.py`'s scale validation is never reached
by a Weaving, so no Weaving of any depth can be rejected by it.

This was the sweep's most confident finding and it is wrong. It is left standing here, overturned in
place, as the register's own worked example of the §0 error class.

### §4.2 What actually survives — and it is real

`systems/threadwork/sim/operations.py:105-113` `COHERENCE_COST_BY_SCALE` carries **both `"Field"` and
`"Territorial"` as keys in one dict**. The design doc's table says Territorial (5 rows); the code's own
depth axis says Field (6 rows). One dictionary holds both names for what is evidently one tier,
so a lookup resolves by whichever string the caller happens to pass.

**CONFLICT.** Small, local, and genuinely a defect — which is the point: the overturned headline
concealed a real finding one tenth its size.

---

## §5 Faction and world vocabulary

### §5.1 The Church threshold — OVERTURNED

Reported as four rival values (40 / 60 / 65 / 100) for one threshold. `systems/factions/ci_political_v30.md:76-87` is a
**single graduated milestone table**:

```
28 start · 40 Church Assertive · 55 Institutional Reach · 65 Church Dominant
80 Church Ascendant · 100 Theocracy
```

…plus a Mass Seizure availability gate at CI ≥ 60 (`:87`). Four **different gates in one system**, not
four rival values for one gate. Do not put this in front of Jordan.

*Residual, unverified:* the sweep never enumerated which four surfaces it meant. If some other surface
assigns a different number to the *same* milestone, that is a separate, uncited finding.

### §5.2 `AMPLIFY` / `DIVERGE` and the Gap scale — OVERTURNED

- **`AMPLIFY` / `DIVERGE`** were reported as tokens existing nowhere in the tree. They have provenance:
  `registers/editorial_ledger_archive.jsonl:149` (ED-150, "AMPLIFY combined pool cap," resolved
  2026-04-04) and `registers/patch_register_index.md:149` (PP-529) / `:120` (PP-301, "DIVERGE+TIE").
  **Stale and archived — not phantom.**
- **The 4-member Gap scale** was reported as invented. `systems/threadwork/threadwork_v30.md:468-471`
  gives exactly four Gap types — Micro, Standard, Entrenched, Catastrophic. (The table's other two
  rows, `:467` "Shifting Object (pre-Gap)" and `:472` "Locked Zone border", are not Gap types.)
  **Matches canon.**
- **Fix site correction.** Both were reported against `references/alias_registry.yaml`, which declares
  itself at `:1-2` as *"GENERATED by tools/vocab_store.py --build … DO NOT EDIT BY HAND."* Any fix
  lands in `references/definitions/vocab_source.yaml`.

*Not adjudicated:* the sweep's `Regular` and `Past|Present|Future` sub-claims. They stand at sweep
grade — which, given this section's hit rate, means unverified.

---

## §6 Voice — the finding stands, and there is a one-field fix

`systems/world/narrative_voice_canon_v30.md:1-4` reads **Status: CANONICAL (ratified by Jordan
2026-06-19, ED-1030)**.

`references/canonical_sources.yaml:237-241` records that same document as **`status: provisional`**,
"home pending Jordan ratification," added 2026-06-09.

The ratification never reached the machine index — precisely the failure mode CLAUDE.md §2 names in
the ED-1094 ruling. **One field.**

**Do not over-claim it.** Whether this stale field *caused* the downstream problem — a ratified
narrative-engine document citing the provisional corpus — is not established by these lines; that
document's citations were authored independently. Report it as a fix site, not as a proven mechanism.

The substantive finding is unchanged and is not about status fields: **no code cites the voice
canon.** The corpus that defines how Valoria sounds has no runtime consumer.

---

## §7 Machinery vocabulary

### §7.1 The correction that was itself wrong — and was queued for CLAUDE.md

CLAUDE.md §6 states that of 27 modules in `references/module_contracts.yaml`, 10 have `doc: null` and
**11** have `[ASSUMPTION]`-grade resolvers. This session filed a correction saying the true figures are
9 and **10**, and queued it as a CLAUDE.md edit.

Settled by parsing the file and attributing every marker to its enclosing module:

```
total modules                                     27
doc: null                                          9   ← the correction is RIGHT
module-level resolver tagged [ASSUMPTION]         11   ← the correction is WRONG
   faction_state · npc_behavior · npc_memory · piety_track · territorial_piety
   domain_actions · peninsular_strain · settlement_economy · faction_politics
   miraculous_event · scenario_authoring        (11 distinct modules)
```

Two traps sit on top of each other here, and both must be avoided to get the right answer:

- A naive `grep -c ASSUMPTION` returns **13** — it picks up the file header at `:14` and a *struck*
  tag inside a state entry at `:357`, plus `:878`, none of which are module resolvers.
- A naive YAML parse returns **0** — because `[ASSUMPTION]` is a trailing **comment** on the
  `resolver:` line, so the parsed value is clean.

Only structural attribution over the raw lines gets 11. **CLAUDE.md's original figure was correct.**
The queued edit must be reduced to `10/27 → 9/27` on the `doc: null` half only; applying it as filed
would put a false number into the governing document.

This is the most consequential entry in the register, and it is a correction to a correction.

### §7.2 `scene.contest_resolved` — NARROWED

The omission finding stands: the type is absent from `articulation.py:116-130`'s `_TRIGGER_TYPE_IDS`
while `key_type_registry_v30.md:854` declares articulation one of its consumers.

The **frequency** claim does not. `parliamentary_bridge.py:212` emits inside
`if winner is not None and degree in ("Overwhelming", "Success")` (`:206`) — a vote season that draws
or lands weak emits nothing. "Emitted every season" is an overstatement; "the most frequent emitter"
is accurate.

Its sibling `scene.battle_concluded` (`faction_action.py:342`) is likewise absent from the roster,
is emitted **unconditionally** per resolved war action, and `references/key_graph.json:1307-1313`
declares four consumers including articulation. That one stands as swept.

### §7.3 Chronicle band bug — substance right, citations wrong

The misclassification is real: a banded verdict is read as a draw, and any non-A, non-draw winner
string is treated as side B. But it lives in `classify` at **`narrative.py:88` and `:92`** — not at
`:114`/`:126`, which are the empty-log branch and a different, non-defective guard in `summarize`.

Recorded prominently because the consequence is concrete: **anyone "fixing" the cited lines would
patch the wrong function** and leave the defect in place.

---

## §8 Cleared on inspection — do not re-raise

Three candidates that look like conflicts, are not, and will be found again by the next sweep:

- **`systems/combat/sim/combat.py:121` vs `combat_engine_v1/core.py:50`.** Two different Combat Pool
  formulas — but `combat.py:4-11` carries a DEPRECATED banner naming `combat_engine_v1` as its
  supersession. A labelled historical file, not a live rival.
- **`systems/threadwork/sim/operations.py:135` `_compute_degree`.** Looks like a rival degree ladder;
  delegates to `dice_engine.degree_label`, and its own docstring says "Adapter over the owner, not a
  second ladder."
- **`armature.py`'s Insinuation axis.** §2.3 — ratified deliberate substitution, reason recorded.

One naming precision while here: the degree ladder's owner is `dice_engine.degree_from_net`, but
adapters reach it through **`dice_engine.degree_label`**. A future reader grepping `degree_from_net`
to find every consumer will miss them all.

---

## §9 The three structural causes

Individual entries above are cheap. These are why they keep recurring.

**S1 — There is no roster primitive.** No registry in the tree can express *"this is the set of legal
conviction names, and here is its owner."* So a roster is re-declared wherever it is needed — as a
Python tuple, a YAML list, a markdown table — and each copy ages independently. The conviction
divergence (§2.1) is not a mistake anybody made; it is the guaranteed output of having no place to say
it once.

**S2 — The naming gate enforces exactly one rule.** `references/descriptor_registry.yaml` carries 113
entries at `enforce: warn` and **1** at `block` (the Solmund/Galbados pair). Every other vocabulary
rule in the tree is advisory. A `warn`-tier rule does not stop a divergence; it annotates one.

**S3 — Some subsystems have no `CURRENT.md` row.** Convictions, Characters and `systems/world` have no
row in the currency index. A supersession affecting them — like `npc_behavior_v30.md:30`'s — therefore
**has nowhere to land**. It was ruled, it was written down, and there was no surface whose job it was
to carry it into code. That is exactly the shape of §2.1.

S1 and S3 are the same defect at two altitudes: **a decision with no owner does not propagate.**

---

## §10 What this register is worth

Sixteen entries. **Six overturned, three narrowed, seven standing.** A sweep-only report would have
put all sixteen in front of Jordan, and six of them would have been wrong — including the two most
confident ones (§4.1's Foundational Weaving, §5.1's Church threshold).

The generalisable rule: **a shared token is a candidate, never a finding.** The cost of the check is
one file read; the cost of skipping it, in this register, was 38% of the output.

---

_Adjudicated 2026-08-23 against `claude/fable5-investigations-architecture-1phbx9` at `512400f`.
Unadjudicated and carried at sweep grade: §5.2's `Regular` and `Past|Present|Future` tokens; whether
`ci_sim_fabrication_check` reacts to the §7.1 figures; the four surfaces §5.1 was originally counting._
