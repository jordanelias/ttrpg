# A Core of Primary Attributes, derived from the four resolving systems

## Status: PROPOSED — DESIGN-ONLY, HELD FOR JORDAN. No registry row added, no export regenerated, no `.py` touched.

**Date:** 2026-09-05 · **Lane:** IN (cross-cutting: MB · PC · SC · FI) · **IDs:** none allocated (design-only)
**Answers:** Jordan, this session — *"Suggest a core of primary attributes for a character based upon
our mass battle system, personal combat system, social contest system, fieldwork and investigation
system."*
**Bears on:** Q7 of the 2026-08-14 ruling agenda (*"it will be 10 attributes"*, ED-IN-0185) ·
`OPT-AV-1` · `proposals/2026-09-01-holonic-architecture/03_DROPPED_IN_CHAIN.md:159` item **25**,
which asks for exactly this: *"`Recall` as the tenth attribute — recorded by precedent, then 'this
shape does not name the tenth' | contradicted-silently | **verify, then a row**."* This document is
the verify.

> **This proposal was rewritten after an adversarial pass.** A structurally independent critic
> (read-only) overturned two of its load-bearing claims and found five prior records it had not
> cited. What it said before is not preserved here — §8.1 records what was retracted and why, per
> §0.1 point 3.

---

## §0 THE RECOMMENDATION

**Six attributes are the core. Four more earn a slot on weaker grounds. That is the ruled ten.**

The split is not stylistic — it applies a criterion this tree already owns. The 2026-08-28 systems
harvest proposes that a name is promoted to the shared roster only on **evidence from ≥2 systems,
same semantics, same shape** (`research/provenance/2026-08-28-systems-integration-harvest/records.json:2205`).
Applied to what the four named systems actually ask for (§2):

| | Attribute | Systems | What it governs |
|---|---|---|---|
| **CORE** | **Cognition** | 4 | Reading an opponent · Command's tactical half · the Primary before a judge or panel · Examine, Surveil, and the Depth gates |
| **CORE** | **Attunement** | 4 | Reflex · the Appraise roll, every exchange · Read, Interview, Negotiate · the Lattice's emotional gate |
| **CORE** | **Charisma** | 3 | Command's **primary** weight · the Primary before a crowd · Face ceiling · sets the Appraise obstacle · Impress, Rumour |
| **CORE** | **Spirit** | 3 | Wound Interval · Stamina · Concentration · the Thread pool · Sincerity · Knot formation |
| **CORE** | **Endurance** | 3 | Wound Interval · Health · Stamina · forced march and exposure · tending the wounded |
| **CORE** | **Recall** | 2 | A term in the **Appraise pool** · the Primary for Research and Reconstruct · caps every History |
| outer | **Strength** | 1 | Impact · weapon handling · half of balance |
| outer | **Agility** | 1 | Tempo · half of balance · half of reflex |
| outer | **Bonds** | 1 | The Knot gate and Knot count · Connect |
| outer | **Focus** | 1 | Concentration ceiling · poise recovery · disruption resistance |

**Read the two tiers differently.** The core six are what the four systems *demand* — each is asked
for, by name, by at least two of them, for the same job. The outer four are each asked for by exactly
one, and they are in for three different reasons that should not be confused:

- **Strength and Agility** are *irreducible substrate*. They reach one system because only one system
  models bodies. Nothing else can carry impact or tempo, and no acquisition layer will absorb them.
  Their single-system reach is a fact about the other three systems, not about them.
- **Bonds** is a *capacity*, not a faculty — it gates how many Knots you may hold. It reaches one
  system because Knots live in one system.
- **Focus** is the genuinely weak one. It has three live sites, all in combat, and the only sweep that
  measures it finds no effect. §6 is the only place in this document where I cannot pick from evidence.

**And the tenth is Recall.** Not restored out of deference to a historical list — it earns the core on
the same criterion as the other five, and §3 is that case.

> **[ASSUMPTION] "Primary attributes" read in the ordinary sense** — the character's base attribute
> set, as against *derived* values. That is what the ruled question asks and what
> `descriptor_registry.yaml` means by `attribute_scalar`. This repo also uses **Primary Attribute** as
> a term of art — the slot in `(Primary × 2) + History + 3` (`social_contest_v30.md:121`,
> `fieldwork_v30.md:65`). **Both answers are in §2's table.** The corpus fields exactly **seven**
> attributes as a Primary: Cognition · Attunement · Charisma (social contest, by adjudicator type),
> and those three plus **Endurance · Recall · Spirit · Bonds** (fieldwork §2.1). **Strength, Agility
> and Focus are never a Primary anywhere** — they govern faculties instead, which is the §1
> distinction. So the narrow reading yields seven and the ordinary reading yields ten. I have answered
> the ordinary one, because that is what the ruled count is about.

---

## §1 THE ARCHITECTURE THIS IS DERIVED FROM, WHICH IS ALREADY RULED

Not proposed here. Already law in the one finished engine, in Jordan's own words, in code:

> `systems/combat/combat_engine_v1/combat_systems.py:185`
> `# BALANCE is NOT a stat (Jordan): it is GOVERNED BY AGILITY, modulated by CURRENT poise`

**Attributes govern · faculties resolve · state modulates.** An attribute is not a thing you roll. It
sets the level of one or more *faculties*, and the faculties resolve. Combat runs this way throughout
— nothing rolls `Strength`; `impact`, `handling_penalty`, `balance_eff` and `health_full` read it.

That fixes the test, and it is narrow:

> **Does it govern a faculty that at least one of the four systems needs, and that no other attribute
> already governs?**

Two consequences that cut against instinct:

- **Breadth of appearance is not sufficient, but it is the only evidence available** for the three
  systems that have no engine (§8.2). Hence §0's two tiers: the six that clear ≥2 systems are asserted
  with confidence; the four that clear one are argued individually.
- **Being rolled is not necessary.** Bonds' whole job is a gate; Focus's whole job is a ceiling and two
  recovery rates. A capacity that binds what a character may hold is as real as a term in a pool.

---

## §2 WHAT THE FOUR SYSTEMS ACTUALLY DEMAND

Read from the resolvers and the current heads. Three states, because the distinction matters and
collapsing it would overstate the case: **`live`** = executable and reached · **`dead`** = executable
and unreachable at every call site · **`prose`** = named in a current head with no executable
counterpart.

| Attribute | Personal combat | Mass battle | Social contest | Fieldwork / investigation | Σ |
|---|---|---|---|---|---|
| **Cognition** | `live` reading, 2⁄3 weight | `dead` Command, secondary weight | `prose` Primary: expert judge, panel | `prose` Primary: Examine, Surveil, terrain; Depth gates | **4** |
| **Attunement** | `live` reflex · ⅓ reading † | `prose` post-battle: tend the wounded | `prose` Primary: no adjudicator; **a term in the Appraise pool, every exchange** | `prose` Primary: Read, Interview, Negotiate; Lattice emotional gate | **4** |
| **Charisma** | — | `dead` Command, **primary** weight | `prose` Primary: crowd · Face ceiling · **sets the Appraise obstacle** | `prose` Primary: Impress, Rumour | **3** |
| **Spirit** | `live` Wound Interval · Stamina · Concentration | — | `prose` Concentration term | `prose` Primary: Thread-Read · Sincerity Gate · Knot formation | **3** |
| **Endurance** | `live` Wound Interval · Health · Stamina | `prose` post-battle: tend the wounded | — | `prose` Primary: forced march, exposure | **3** |
| **Recall** | — | — | `prose` **a term in the Appraise pool** · +2D citation bonus | `prose` Primary: Research, Reconstruct · caps every History | **2** |
| **Strength** | `live` impact · handling deficit · ½ balance · Health term | — | — | — | **1** |
| **Agility** | `live` tempo · ½ balance · ½ reflex | — | — | — | **1** |
| **Bonds** | — | — | — | `prose` Primary: Connect · Knot gate ≥5 · count `floor(B/2)+1` | **1** |
| **Focus** | `live` concentration ceiling · poise recovery · disruption resistance | — | — | — | **1** |

† **`att` is the one cell I would not defend without a ruling.** The engine carries `att`
(`combatant.py:97`) and contains **zero** occurrences of "Attunement", "Acuity" or "Cognition". Its own
comment glosses `att` as **"attention"** — `combat_systems.py:1326`, *"`reading` — cog/attention/
experience"* — which is not Attunement's declared alias (that is *Perception*). If combat's `att` is
attention-under-pressure rather than empathetic perception, Attunement is two faculties wearing one
name and fails the promotion criterion's *"same semantics"* clause. **This is a ruling question, and
it is the sharpest one in the document after §6.**

### Sites, for checking

- **Combat** — actor signature `workbench/catalogue.py:46`:
  `NEUTRAL = dict(strength=4, agi=4, end=4, cog=3, att=3, spirit=3, focus=3, history=3, disp=4)`.
  `combat_systems.py:171` `reading(c) = (2*c.cog + c.att)/3 + K*(c.history-3)`; `:172`
  `reflex(c) = (K_agi*c.agi + K_att*c.att)/(K_agi+K_att)`; `:188` `balance_eff` = `½agi + ½strength − 1
  + skill('balance')`, times poise; `:1435` poise recovery scaled by `(c.focus−3)`; `:1451`
  `disrupt_resist = logistic(K*(c.focus−3))`. `combatant.py:35-47`
  `wound_interval = end + 4 + 0.4·spirit`, `health_full = WI·(MW+1) + 0.25·strength·end`,
  `stamina_max = 3·end + 2·spirit`; `:147` `conc_max = 3·focus + 2·spirit` (ED-902). The pool takes no
  attribute: `core.py:51`, *"Agility-INDEPENDENT resolution pool (ED-901): max(5, History + 6)"*.
- **Mass battle** — `sim/core/exchange.py:42-51` `derive_command(charisma, cognition)`;
  `sim/config.py:416-417` `CMD_CHA_WEIGHT=2` (primary), `CMD_COG_WEIGHT=1` (secondary); prose source
  `mass_battle_v30.md:298` `Command = clamp(round((2·Charisma + Cognition) ÷ 3), 1, 7)` (ED-899);
  post-battle `mass_battle_v30.md:917-919` — *"Tend the wounded | **Endurance or Attunement** check"*,
  *"Survey the damage | Cognition"*, *"Address the population | Charisma"*.
- **Social contest** — `social_contest_v30.md:121-129` `Argue Pool = (Primary Attribute × 2) + History
  bonus`, Primary by adjudicator: Cognition (expert judge, panel) · Charisma (crowd) · Attunement
  (none). **`:147` is the load-bearing line and the one this document previously missed:** *"Step 1 —
  Appraise (both orators) (PP-278 / PP-614): Roll **Attunement + Recall**, TN 7, **Ob = opponent's
  Charisma ÷ 2**"*. Kernel: `sim/contest/primitives.py:132-149` `face_max = charisma × 3`.
- **Fieldwork** — `fieldwork_v30.md:82-93` (§2.1 Primary Attribute table) and `:293-298` (§4.2):
  Cognition · Attunement · Endurance · Recall · Spirit · Charisma · Bonds — **seven of the ten**, the
  widest attribute surface of any system. `:422` Sincerity = Spirit; `:467` Knot count
  `floor(Bonds/2)+1`; `:469` Bonds ≥ 5 gate; `:475` Knot pool `(Spirit×2)`.

**One line in that table is worth pausing on.** `social_contest_v30.md:147` sets the Appraise obstacle
at **opponent's Charisma ÷ 2** — which is Jordan's own `score/2` obstacle derivation, ruled 2026-08-14
and recorded in `HANDOFF.md` as *"wired nowhere — the largest outstanding piece"*. It is wired in
prose, here, in a current head. That is not this document's business to fix, but a session executing
the score/2 ruling should start from this line rather than from a blank page.

---

## §3 THE TENTH IS RECALL — on the criterion, not on the history

`Recall` is not a candidate I generated, and the earlier draft of this section made a weaker case for
it than the evidence supports. The strong case is one line:

> `systems/social_contest/social_contest_v30.md:147` — *"Step 1 — Appraise (both orators)
> (PP-278 / PP-614): Roll **Attunement + Recall**, TN 7, Ob = opponent's Charisma ÷ 2… [ED-893] Recall
> contributes to the Appraise pool and the citation bonus."*

**Recall is a rolled term in the current social-contest head's opening step, in every exchange of
every contest** — and the Primary attribute for two of fieldwork's six investigation actions
(`fieldwork_v30.md:87,295,298` — Research, Reconstruct, under `(Primary × 2) + History + 3`). Two
systems, same semantics (retained knowledge brought to bear), same shape (a term in a pool). It clears
the promotion criterion on its own, without appeal to any historical roster.

**The capacity job is real but is the weaker half of the argument, and the earlier draft overstated it.**
Recall caps every History (`investigation_systems_v30.md:44`, a CANONICAL head:
`| Histories | Character creation, cap = Recall |`; and `references/glossary.md:186` under the
pre-rename name, *"History | Skill-equivalent… Cap = Memory score"*, with `Memory (score) → Recall`
recorded at `references/name_collision_database.yaml:442-446`). It also sets equip slots and learning
rate (`character_histories_v30.md:7,26-28,509`).

**Three corrections to how that argument was put:**

1. **"History is a term in every pool" is false.** Threadwork's History term is **identically the
   constant 3**: `systems/threadwork/sim/operations.py:173`, `history_contrib = min(3, history + 3)`
   with `history >= 0`. The prose caps it too (`threadwork_v30.md:155`, *"up to +3D from History
   level"*), and the code is a mis-implementation of that cap. This is already filed —
   `registers/handoffs/HANDOFF_IN.md:3587`, *"threadwork History inert"*. Several current-head pools
   have no History term at all: Knot formation (`fieldwork_v30.md:475`), the Sincerity check (`:422`),
   and *"Roll Cognition only (no History)"* (`threadwork_v30.md:236`). Fieldwork makes History optional
   outright (`:65`).
2. **No code enforces the cap anywhere in this tree.** I looked; there is no reader of Recall→History
   under `engine/` or `systems/`. The nearest is `tests/sim/v32-combat-balance/r1_sigma_resolution.py:38`,
   `HISTORY_MAX = 7  # [canonical: … Recall caps History points <= 7]` — a constant equal to maximum
   Recall, i.e. inert as a differentiator, and `tests/sim/` is not the executable suite.
3. **`character_histories_v30.md` has no `CURRENT.md` row.** Its `## Status: CANONICAL` is a
   self-declaration, which §0.05 classes as reference. CLAUDE.md §3 says `characters/` is a doc home,
   *"not yet formalized"*. So of the two heads cited, one (`investigation_systems_v30.md`) is indexed
   in `CURRENT.md:31` and one is not.

**What survives all three:** the Appraise pool and the two fieldwork primaries, which are in indexed
current heads and are the case. The History cap is corroboration, not the load.

---

## §4 THE OUTER FOUR, GRADED HONESTLY

They reach one system each and are in for different reasons. Ranked by how much I would defend them.

**Strength and Agility — keep, and their single-system reach is not evidence against them.** Combat is
the only one of the four that models a body, so it is the only place they could appear. They are
irreducible in the strict sense: no acquisition layer substitutes for them (§8.3's shrink argument
concedes exactly this — *"what will not be replaced… is the substrate tier"*). Both are live across
many sites (§2).

**Bonds — keep, on a narrow but clean case.** It is the only attribute that governs relational
*capacity*: the Knot prerequisite (`fieldwork_v30.md:469`, Bonds ≥ 5, ED-912) and the Knot count
(`:467`, `floor(Bonds/2)+1`). Nothing else can carry it, and ED-912 specifically *decoupled* Disposition
from Bonds (`derived_stats_v30.md §10.1`), so the capacity job is what Bonds was left with on purpose.
It is also read in code — `systems/fieldwork/sim/knots.py:185`.

**Focus — the open question. §6.**

---

## §5 THE TWO RENAMES — direction clear, my earlier numbers were not

The registry ships `Acuity` (aliases Reasoning, Cognition) and `Will` (alias Spirit). The corpus, in
both prose and code, overwhelmingly says **Cognition** and **Spirit**. I recommend reverting, but the
earlier draft argued it with four grep counts that do not reproduce, and that method is precisely what
this lane's own handoff records as having previously *inverted* an attribute ranking
(`registers/handoffs/HANDOFF_IN.md:3591-3596` — *"grep counts (which **inverted** the true attribute
ranking)"*, against Jordan's *"read code, not prose"*). **The counts are withdrawn.** What replaces
them is specific and checkable:

- **`Acuity` appears in no `.py` file in the tree, and the registry itself flags the rename as an
  assumption awaiting a veto** — `references/descriptor_registry.yaml:54`:
  `{key: attr.mind.acuity, name: Acuity, aliases: [Reasoning, Cognition]}   # [ASSUMPTION] legacy 'Cognition' folds to Acuity -- Jordan veto`.
  Meanwhile the combat engine's ratified module contract, the mass-battle Command derivation, and every
  design head use Cognition.
- **`Will` appears as an attribute in no engine.** The combat engine carries `spirit`
  (`combatant.py:97`) and so does its **ratified contract** — `references/module_contracts.yaml:1326,1333`,
  `WI=round(End+4+0.4*Spi)`, `inputs: ["Endurance", "Spirit", "Strength", …]`. Fieldwork's knot code
  reads `spirit` (`sim/knots.py:214`). The registry's own comment concedes the fold is a convenience:
  `:55`, *"'spirit move': formerly standalone Spirit; legacy formulas resolve via alias"*.
- **A third roster agrees.** `references/glossary.md:59,62` uses Cognition and Spirit — in a 7-attribute
  table that carries its own `⚠️ IN FLUX` banner (`:53`) declaring it *conflicts with* the registry's
  nine and that **neither file defers to the other**. Four rosters are in circulation: glossary-7,
  registry-9, engine-9 (a different nine — `workbench/balance.py:43`, `workbench/server.py:28`,
  `workbench/static/index.html:132`, `phase4_5_plan_v1.md:58` — which includes History and Disposition
  and excludes Charisma and Bonds), and prose-10.

**⚠ The one surface where the registry's names win, and it is the surface §0.05 privileges.**
`engine/engine_params/descriptors.json:18-19` carries `attr.mind.acuity` and `attr.mind.will`, and
`engine/substrate/descriptors.py:59` loads them into `ATTRIBUTES` **at import**. Under §0.05 a registry
code reads at runtime *is* a mechanism. So Acuity and Will are the only attribute names with any
runtime presence at all, and the markdown corpus is — by that same rule — reference. **This inverts the
naive reading of the evidence and the earlier draft did not disclose it.** My recommendation is
unchanged, because the runtime presence is a bare key list nothing consumes (§7), while the ratified
combat contract and every design head say Cognition and Spirit. But it is now a judgement between two
kinds of evidence rather than a tally, and Jordan should see it that way.

**And the revert is not free — see §7.** Reverting churns keys, which is the one thing the registry
exists to prevent.

---

## §6 FOCUS — the call I cannot make from evidence

**What it has:** three sites, all in combat, all live rather than declared-only —
`conc_max = 3·Focus + 2·Spirit` set at `combatant.py:147` and read at `wrapper.py:22,24,487`;
poise recovery `combat_systems.py:1435`, called at `wrapper.py:130-131`; disruption resistance
`:1451`, called at `wrapper.py:419`. Its governing idea is coherent: **steadiness under pressure.**

**What it lacks:** presence in the other three systems, and any measured effect. **Two sweeps exist and
disagree on magnitude, so take the ranking and not the numbers:** the 2026-06-28 baseline (N=300/cell,
*"point-in-time, not targets"*) reports `cog +26 · strength +20 · agi +20 · history +15 … disp +4.5` and
does not list Focus at all (`combat_balancing_methodology.md:70,78`); the later n=600 position-swapped
sweep with Wilson intervals puts Cognition at **+20.4pp** and Focus at **+0.3pp**, CI 46.3–54.3 —
overlapping the mirror control at 53.1, i.e. indistinguishable from no effect
(`proposals/2026-08-15-character-and-faction-stats-and-progression.md:24-40`). Its stated canonical job,
*"Contact Rounds = Focus score"* (`params_tables.yaml:9133`), is unimplemented.

**Two options.** I lean to (a) but will not pretend the evidence picks:

- **(a) Keep it and give it the steadiness job across all four systems.** Three of the four have
  carved that socket and filled it with a flat constant: contest's `Reserve`
  (`sim/contest/primitives.py:49-56`, `MAX = 12  # [SEED]`), combat's Concentration (which does use
  Focus), and fieldwork's Desperate Trail (`fieldwork_v30.md:331` — three failures escalate TN 7→8,
  governed by nothing). ⚠ **Correction to how I first put this:** binding Focus to `Reserve` would
  *not* be "the contest kernel's first attribute" — the kernel already takes Charisma as an argument
  (`primitives.py:132-149`) and already names `(3*Focus)+(2*Spirit)` as the canonical magnitude the
  wrapper carries (`:101-103`). The socket is not unowned; the question is narrower — whether the
  kernel should read the formula rather than carry a `[SEED]` constant beside it.
- **(b) Fold it into Spirit.** Defensible on the measurement alone. It leaves the sockets above
  unowned, and no candidate exists for the freed tenth slot — which under the ruled count means (b)
  requires naming something else, and nothing in the four systems asks for anything else.

---

## §7 WHAT IT ACTUALLY COSTS TO EXECUTE — and it is not what I first said

**⚠ RETRACTED: my earlier claim that naming the tenth is "a registry edit and an export, not a code
change" was false.** It requires editing a blocking test in `tests/valoria/` whose assertions encode
the opposite decision — and one of them says Recall was *retired*, not dropped:

> `tests/valoria/test_descriptor_registry.py:36`
> ```python
> # retired attribute must NOT resolve
> assert dr.resolve(reg, 'Recall') is None, "'Recall' was retired; must not resolve"
> ```

**This is the most important artifact in the tree bearing on §3, and it argues against it.** It is in
the blocking pytest suite (CLAUDE.md §8). Adding Recall and reverting the two names breaks at least
eight assertions in that one file:

| line | assertion | breaks on |
|---|---|---|
| `:19` | `len(all_attributes(reg)) == 9` | adding Recall |
| `:21` | each of body/mind/social has exactly 3 | Recall into `mind` → 4 |
| `:24` | `resolve('Spirit')['key'] == 'attr.mind.will'` | the Spirit revert |
| `:25` | `resolve('Cognition')['key'] == 'attr.mind.acuity'` | the Cognition revert |
| `:31` | `resolve('Will')['key'] == 'attr.mind.will'` | the revert |
| `:36` | `resolve('Recall') is None` | adding Recall |
| `:39` | `aggregate_members('agg.mind') == {focus, acuity, will}` | both |
| `:43` | `len(by_domain('actor')) == 9` | adding Recall |

**Whether that `:36` assertion is well-founded is itself the question.** Its own docstring (`:8-10`)
says the assertions are *"UNCHANGED from the original"*, so the "retired" claim predates 2026-07-08 and
may simply be older than the ruling that the roster will be ten. But **deleting it is a design act, not
a chore**, and this document should have said so from the start.

**The full, corrected recipe:**

1. Add the row to `references/descriptor_registry.yaml` (`attributes.mind`) — and **also** update
   `aggregates.agg.mind` at `:65`, which the exporter never reads and which `test_descriptor_registry.py:39`
   does.
2. Rewrite the eight assertions above, including the retirement claim at `:36`.
3. `python3 tools/export_descriptors.py` regenerates `engine/engine_params/descriptors.json`.
   **The `pending_tenth` sentinel is not deleted — it is derived**: `tools/export_descriptors.py:159-163`
   emits it conditionally on `len(roster) < 10` and sets it to `null` at ten. My earlier "delete the
   sentinel" step was a no-op; the sentinel's own instruction describes a regenerated file.
4. `python3 tools/export_descriptors.py --check` is blocking in CI
   (`.github/workflows/valoria-ci.yml:137`, `tools/valoria_local.py:63`).
5. **The renames are a separate and larger cost.** `descriptor_registry.yaml:3-5,13-14` states the
   invariant the file exists for: *"Systems bind descriptors BY KEY… a descriptor can be renamed…
   without rewriting any consumer."* Reverting Acuity→Cognition either churns the key
   `attr.mind.acuity` → `attr.mind.cognition` (breaking bind-by-key, `descriptors.json`, and any
   `.tres` keyed on it) **or** changes only `name:` and leaves a permanent key/name mismatch. There is
   no free branch. My §5 recommendation stands but its cost does not — this is a rename against
   shipped data, and it should be ruled as one.

**⚠ And the "falsifiable" claim was overstated too.** There is **no attribute-roster assertion**.
`engine/substrate/descriptors.py:97` `assert_faction_roster_is_covered` is called at import from
`engine/autoload/game_state.py:230` — that is the registry→field→dataclass gate, and it exists **only
for faction stats**. `descriptors.ATTRIBUTES` has **zero consumers** anywhere in `engine/` or
`systems/`; the only reader in the tree is `tests/valoria/test_descriptors_runtime.py`, which asserts
the sentinel↔count biconditional. So adding Recall cannot halt anything, because **no code implements
any attribute at all.** What step 4 falsifies is that the YAML and the JSON agree — a self-consistency
check on the exporter, not evidence the game uses the tenth.

**What that means for §0.2 ("done means it runs").** Naming the tenth does not make it run. It lifts
the *"do not bind Godot resource fields to these keys yet"* flag (CLAUDE.md §5) and unblocks the port;
it does not by itself put an attribute into a resolver. The honest framing is that this is a **ruling
that unblocks execution**, not execution.

---

## §8 AGAINST MY OWN ANSWER

### 8.1 What the adversarial pass retracted

Recorded rather than quietly fixed, per §0.1 point 3. A structurally independent read-only critic
overturned:

1. **"Naming the tenth is not a code change"** — false; §7 above.
2. **"History is a term in every personal pool"** — false; §3 correction 1.
3. **Four grep counts supporting the renames** — withdrawn; §5. The direction survives, the numbers did
   not reproduce, and the method is the one this lane recorded as having inverted an attribute ranking.
4. **"Binding Focus to contest `Reserve` gives the kernel its first attribute"** — false; the kernel
   already takes Charisma (§6).
5. **Five prior records naming Recall as the tenth, all uncited** — §8.2.
6. **A "Concentration is defined twice" finding** — withdrawn entirely. `character_histories_v30.md:209`'s
   *"Concentration (Focus + Recall)"* is already struck by ED-694, in the current head:
   `social_contest_v30.md:147`, *"Recall contributes to the Appraise pool and the citation bonus, **but
   not to Concentration (ED-694)**."* Not a live defect; a stale line in a non-indexed doc.
7. Six citation line-number errors, all corrected in place.

It also found the §2 line that **strengthens** the case — the Appraise pool (§3) — which the first
draft had missed while quoting the same file.

### 8.2 This conclusion is not new, and one newer record calls the precedent contradicted

`Recall`-as-the-tenth has been stated at least five times before, four within one week in August:

- `proposals/2026-08-18-breaking-the-recursion.md:335,660` — §4.5 names it, and recommends verbatim
  what §0 recommends here, eighteen days earlier.
- `proposals/2026-08-18-recursion-interrogation-log.md:233` — *"THE 'UNNAMED TENTH ATTRIBUTE' IS
  RECALL, AND IT SHIPPED IN APRIL"*.
- `proposals/2026-08-18-next-session-handoff.md:162`; `proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:570`.
- `proposals/2026-09-01-holonic-architecture/03_DROPPED_IN_CHAIN.md:159` item **25**, four days ago:
  *"recorded by precedent, then 'this shape does not name the tenth' | **contradicted-silently** |
  verify, then a row."*

Under CLAUDE.md §0's five-test ordering (superseded → irrelevant → doc → **precedent** → architecture),
the precedent test should have been applied before authoring. **What this document adds over the
precedent** is the derivation from the four systems Jordan named, the promotion criterion, the Appraise
evidence, and §7's cost — the precedent asserted the conclusion; this argues it and prices it.

**A second-hand fact I could not verify and that matters.** `breaking-the-recursion.md:344-353` reports
that the implementation repo already ships all ten as live `@export` fields, with 31-point allocation
across the exact ten of §0, `effective_recall(coherence_state)`, and **`History dice_bonus ≤ recall`
validation** — i.e. the History cap *is* enforced in code, in the port. `valoria-game` is a separate
clone not in this tree, so I have **not** verified any of it. If it holds, §3's correction 2 is wrong
about the cap being unenforced everywhere, and the roster question is partly a question about
re-synchronising two repositories rather than about design.

### 8.3 Two live positions argue the other way, and I have not defeated either

- **Name no tenth at all.** `proposals/2026-08-29-valoria-from-scratch/02_the_person.md:144-149`:
  *"I cannot write an N-line for a tenth attribute, so it is carried as a reservation, not a
  mechanism… Naming it now would be the exact failure this exercise exists to escape."* **This
  document's answer to that is §3**: the N-line is the Appraise pool and the two fieldwork primaries —
  remove Recall and those lose a term and a Primary. That is a real N-line, and it is the thing that
  document said it lacked. Whether it is *sufficient* is Jordan's call.
- **The roster should shrink.** `proposals/2026-08-15-character-and-faction-stats-and-progression.md`
  §10.5: *an attribute dependency is what a subsystem has instead of an acquisition layer.* Combat
  carried `(Agility×2)+History+3` until it grew weapons, traditions and graded abilities — then ED-901
  removed the attribute from its pool. Four of six systems have no acquisition layer and are exactly
  the ones leaning on attributes. Its recommendation was **eight**, against a ruled ten. I have not
  refuted it; if it holds, the attributes most at risk are Charisma, Recall and Bonds.

**Two corrections to that document, both running the other way** — and both concern the systems it
read least:

1. **"Charisma — zero occurrences in any `.py`" is false.** `mass_battle/sim/core/exchange.py:42-51`,
   `hierarchy/units.py:2382-2389`, `config.py:413-416`, `engine.py:76` — and it carries the **primary**
   weight of Command (`CMD_CHA_WEIGHT=2` vs `CMD_COG_WEIGHT=1`), the one personal→mass crossing in the
   game. Plus `sim/contest/primitives.py:132-149`.
2. **"Recall — never rolled" is false.** `social_contest_v30.md:147` (Appraise) and
   `fieldwork_v30.md:87,295,298` (Research, Reconstruct).

### 8.4 Three of the four systems do not read attributes in code at all

The largest standing caveat, and it qualifies every `prose` cell in §2. Under §0.05 prose is reference;
only code is mechanism.

- **Personal combat** genuinely consumes attributes — seven of the ten, in live faculty functions.
- **Mass battle's** Charisma+Cognition seam is real code, **dead at every call site**: every `Unit(...)`
  passes `command=` as a bare int and never passes `charisma`/`cognition`, including the sole strategic
  entry point (`sim/massbattle.py:90`, `command=4,  # [canonical: inherited default — see GAP above]`).
  ⚠ *Narrower than I first wrote:* `POOL_QUALITY_MODEL` supersedes the Command **base-pool term only**
  (`config.py:419-424`); Command still drives morale, formation-hold and rout.
- **Social contest's** kernel refuses attributes by design — `Pool.size(faculty) = max(5, faculty*2 + 3)`
  (`primitives.py:208-211`), fed in production by `faculty = round(Faction.L)` / `round(7 − Faction.Sta)`
  (`engine/cross_scale/scene_dispatch.py:121-139`): **faction stats, not personal attributes.**
- **Fieldwork's** sim is `stub_resolve` throughout; only `sim/knots.py` reads anything (`bonds`, `spirit`).

**So the ten is sourced from the four systems' current heads and one finished engine — not from four
running engines.** Three of the four could not currently tell this roster from any other. §2's
three-state legend is there so that weight is visible rather than assumed.

### 8.5 The tier scheme changes nothing executable

§0 groups by function rather than by Body/Mind/Social. That grouping is a *reading*, and it should not
be mistaken for a proposal:

- **No code distinguishes any grouping.** `tools/descriptor_registry.py:35` and
  `tools/export_descriptors.py:138` both hardcode `for cat in ('body','mind','social')`, and the
  category is **not emitted into `descriptors.json` at all** — the runtime artifact is a flat key list.
- **The only consumer of grouping is a placeholder** — `descriptor_registry.yaml:62-71`, `agg.body/mind/social`,
  `status: placeholder`, *"NOT active until that migration."*
- **So a real regroup costs two tool edits plus a key churn** (the keys encode the taxonomy:
  `attr.body.*`, `attr.mind.*`, `attr.social.*`), which contradicts §7's framing of this as cheap.

**Recommendation: adopt the tiers as sheet-and-doctrine language, not as a registry change.** They
explain *why* Bonds and Recall behave unlike the other eight, which is worth having; they do not need
to reach the keys to do that.

---

## §9 WHAT WOULD FALSIFY THIS

- **§3 falls** if `social_contest_v30.md:147` is superseded — ED-893 is marked *"pending
  reconciliation"* in that very line, which is the crack to check first. If Appraise reverts to
  *"Attunement alone, Ob 1"*, Recall drops to one system and out of the core.
- **§0's core/outer split falls** if the promotion criterion is not the right instrument. It is a
  proposal (`records.json:2205`), not a ruling.
- **§5 falls** if Jordan intended Acuity and Will as rulings rather than as the registry's own
  `[ASSUMPTION]` — `:54` says assumption; a ruling supersedes it.
- **§7's cost estimate falls** if `test_descriptor_registry.py:36` was itself written after the
  2026-08-14 ruling; its docstring says the assertions are *"UNCHANGED from the original"*, so check
  `git log` on that file before treating the retirement claim as considered.
- **The whole roster falls toward six** if §8.3's prediction holds and the non-combat systems grow
  acquisition layers. That is the honest long-run risk and it is why §0 grades the outer four
  separately rather than presenting a flat ten.

---

## §10 THE CALLS THAT ARE JORDAN'S

1. **Is the tenth `Recall`?** — §3. If yes, §7's five steps execute, and the *"do not bind Godot
   fields"* flag lifts. **Note that step 2 requires overruling a test that says Recall "was retired"** —
   that is the actual decision, and it should be made explicitly rather than absorbed as cleanup.
2. **Is combat's `att` the same faculty as Attunement?** — §2's footnote. The engine glosses it
   "attention" and never says Attunement. If they are different, Attunement is two things and the core
   is five, not six. This is the sharpest unresolved question here.
3. **Focus: the steadiness job (§6a), or fold it (§6b)?** — the only place evidence does not pick.
4. **Do `Acuity` and `Will` revert to `Cognition` and `Spirit`?** — §5. ⚠ Not a free edit: it is a
   rename against shipped keys and shipped data (§7 step 5).
5. **Does the port already settle this?** — §8.2. If `valoria-game` ships all ten with History-cap
   validation, questions 1 and 4 are partly re-synchronisation rather than design, and someone with
   that clone should check before this is ruled.
