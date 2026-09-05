# WHAT VALORIA IS, AND WHAT RUNS

## Status: **REFERENCE.** Not canon, not a proposal, nothing ratifies on merge.
## Measured 2026-09-05 against `main` + `claude/game-architecture-review-kagi8k` at `9ebd148`. Lane: IN. ED-IN-0202.
## Under `CLAUDE.md` §0.05 this document is **reference and information only**. It is a mechanism for nothing. Where it disagrees with code, **the code is right and this file is stale** — every number below carries the command that re-measures it, so a later session re-runs rather than trusts.

**Why it exists.** A session asked to describe the game had to read across `canon/`, `engine/`,
`systems/`, `workplans/` and the September proposal chain to answer, and in doing so found **eight
claims the tree makes about itself that are false**. Those corrections are §3 and are the most
perishable-if-lost part of this file. The rest is orientation: what the game is, what executes, and
what the held-back architecture chain would change if it were ratified.

**What it is not.** Not a head of any lineage — `CURRENT.md`'s head map is unchanged by it. Not a
continuity surface — that is `HANDOFF.md` and the lane files. Not a docket — no row here is
`needs_jordan`, and §5 records questions the proposal chain leaves open as *facts about the chain*,
not as requests.

---

# §1 · THE GAME, IN ONE PASS

## §1.1 The premise

You play **one person inside a political body on a post-catastrophe peninsula**, and the same engine
resolves your duel, your speech to a council, your province's harvest and your faction's war.
**There is no GM** (`CLAUDE.md`, opening). That is not a production constraint; nearly every
distinctive mechanic descends from it.

Removing the referee does not remove the question the referee answered — *why did that happen?* The
architecture chain's answer, and the tightest statement of the game's epistemic contract, is that
the engine owes **the arithmetic of what your character already holds, and nothing about the world
they do not** (`proposals/2026-09-03-meta-architecture/04_CODE_ARCHITECTURE.md` §C.11). Hidden actors
are hidden in their *existence*, never in their *arithmetic*.

## §1.2 The fiction is load-bearing

`canon/00_philosophical_foundations.md`, enforced as P-01..P-15 by `canon/02_canon_constraints.md`
with a violation test per row.

- **Threads** are both what things are made of and what makes it possible for things to be. All three
  dimensions — temporal, epistemic, actualized — co-move; **foregrounding is impossible** (§1.1,
  P-01). No thread operation is surgical.
- **The Ein Sof** is infinite positive being, not a void (§2.1). **Monstrosity is ontological, never
  moral** (§4.1, P-02/P-04) — there is no alignment system, and practitioners manage a rendering
  failure rather than fight evil.
- **The Calamity** was rendered-side: the Einhir over-drew the substrate until it tore at the anchors,
  ~12 years before 0 AG (§6.1; `canon/03_canonical_timeline.md`). The ground has no agency (P-07).
  **Locked Zones** are where being-as-such failed.
- **Solmund** is a third-mode threadcut being who came through the tear and *catalyzed* rather than
  founded the Church; its essentialist theology forecloses thread sensitivity, and the foreclosure is
  **emergent, not conspiratorial** (§8, §9.2).
- **The epistemological barrier**: non-sensitives can recite thread facts and cannot render them
  (§10.1, P-08/P-13). Knowledge is not a token you can hand somebody.
- **Coherence** is the integrity of layer-two self-rendering, 10→0, orthogonal to Thread Sensitivity,
  tridimensional in its loss, and it **propagates through knots to everyone bound to you** (§16,
  P-10/P-12/P-15).

Two consequences are canon-level rather than system-level, and they are the game's best properties:
**a person's belief can be false and they cannot tell**, and **intervention always costs somewhere
you were not aiming.**

## §1.3 Two scales, one continuous game

`systems/_architecture/videogame_mode_spec.md` §0: strategic and personal run **simultaneously**,
joined by zoom rather than a mode switch. Mandatory triggers pull the player down; Domain Echo pushes
outcomes back up. No session boundaries, no GM adjudication, no `GameMode` enum.

- **Strategic** — 16 authored territories of which **15 playable**; four factions (Crown, Church,
  Hafenmark, Varfell) opening at 6 / 1 / 4 / 4 territories with one unowned; **37 settlements**;
  seasons, four to an arc.
- **Personal** — scenes: combat, social contest, fieldwork/investigation, threadwork.
- **Your seat** — an officer inside a faction, not its leader (`player_agency_v30.md` §0). Three
  self-authored **Convictions** against faction-issued **Duties**; that tension is the game's central
  one for a non-leader. **Standing 0–7** from Petitioner to Regent-Designate. The Scene Slate offers
  4–9 opportunities against 3–5 scene actions — **the surplus is the point**; triage is the mechanism.
  The ending is **Portrait Retirement**, available and never forced once two of three Convictions
  resolve.

## §1.4 Resolution — one primitive

`engine/autoload/dice_engine.py`.

- d10 pool. **TN is 7 always**; the engine raises on any other value (`_require_tn7`, ED-IN-0196).
- Die rule: **1 = −1 · 2–6 = 0 · 7–9 = +1 · 10 = +2**, no chaining; pool floors at 1D.
- **margin = net − Ob**, and the ladder reads the margin, never the obstacle's size:
  `< 0` Failure · `0 ≤ m < 1` Partial · `1 ≤ m < 3` Success · `m ≥ 3` Overwhelming.
- Continuous mode: `Normal(0.40·N, 0.800·√N)`, so pools and obstacles may be fractional.
- σ-leverage (`sigma_leverage.py`): named advantage levels (minor .25 → major 1.0) become a μ-shift,
  soft-capped at `1.5·tanh(x/1.5)`.
- **One ladder for every scale.** A subsystem varies it only through a `BandExtension` injected by its
  wrapper, whose sole power is to **veto an Overwhelming** — structurally, not by convention. One
  declared holdout remains: `systems/combat/combat_engine_v1/core.py`, held until Ob is derived from
  the defender, and `tests/valoria/test_degree_ladder_single_owner.py` asserts it *still diverges* so
  the exemption cannot outlive its reason.

---

# §2 · THE NINE SYSTEMS, MEASURED

Jordan's framing, 2026-09-05, verbatim: *"an overview layer that manages worldly events and sets up
scenes and arcs, a layer that allows for factions at different scales to act and organize accordingly
including duchies and kingdoms issuing edicts and policies and managing their holdings etc, a
personnel management system that allows for duties/assignments to offices/recruitment/etc, a city
builder/management system for settlements and territories, a military system that organizes content
for mass battles, a social contest/parliamentary system, a grid-based map squad battle system that
includes dueling, a fieldwork & investigation system where you can explore settlements and interact
with characters and things and locations, a character generation/progression/management/chronicling
system"*, drawing on *"grand strategy games, territorial board games, political board games, military
strategy games, strategy RPGs, RPGs, tactics games, city builders, management games, interactive
fiction, freeform social simulators, detective games, mystery games, lifestyle simulations."*

| # | required | measured state |
|---|---|---|
| 1 | **Overview — events, scenes, arcs** | **Designed, essentially unbuilt.** `scene_slate`, `game_director`, `scenario_authoring`, `scene_timer` are four of the **nine of 27 module contracts carrying `doc: null`**. The narrative engine (one beat stream, scale as a projection, no runtime LLM) is RATIFIED design with no engine. `engine/cross_scale/articulation.py` is **stub in full** — all 13 Key callbacks are no-ops. **1 of 8** mandatory zoom triggers is field-evaluable. |
| 2 | **Factions at multiple scales; edicts; holdings** | **One scale acts.** Four peninsula factions choosing among four buckets. **No duchy or kingdom tier acts at all.** The mechanism exists only as proposal: rank is the *ordinal of a seat's domain*, stored nowhere; a seat makes **ordinary** acts eligible where they otherwise are not. Edicts are `issue`/dispensation in the proposed verb table, and its **nine dispensation terms are unspecified — the downward mechanism has no executable content** (`04_CODE_ARCHITECTURE.md` F.15). |
| 3 | **Personnel — duties, offices, recruitment** | **Ontology settled; nothing runs.** Duties are canon design. **Only `revoke` was rebuilt on the ruling's eligibility model, so conferral runs the wrong one** — which is why delegation read as unbuildable. Resolved by ruling 2026-09-03: **authority is a property of the seat exercised, never of the person exercising it**; regency, puppet rulers and governors are then all a conferred seat. Recruitment: none. |
| 4 | **City builder / settlements & territory** | **State model executes; the builder does not.** 37 settlements with derived stats, a durable ledger (Precedent · Grudge · Debt · Reputation · Leverage) surviving succession, adjacency, infrastructure, temperaments. But **no verb founds a hearth or builds a site** — *the world only decays* (F.20). |
| 5 | **Military / mass battle** | **The strongest subsystem.** 51×51 field, formation cell patterns, 18 ticks per turn in three phases, volleys with Lanchester scaling and density, stochastic rout drawn in du Picq's 15–30% band, facing octagon as a **damage-received** multiplier, cavalry shock, envelopment, per-battle friction. One real hole: **army construction has no spec** — a faction army is one Line subunit (`massbattle.py`, own `[GAP:]`). |
| 6 | **Social contest / parliamentary** | **One of four `GAMES` rows built** (`agon`). The parliamentary vote runs every season. The later reading (2026-08-06 three-lens, upheld 2026-09-04) says **abandon the four-games framing**: inquiry and consensus are *venue rows*, `settle()` is the one new build — and there are **four resolution models executing under one name plus a fifth in prose**. Jordan's four 2026-09-04 requirements jointly say the **unit of resolution is wrong**: the kernel resolves one matter between two sides to one label. |
| 7 | **Grid squad battle incl. dueling** | **Dueling is strong; the squad layer does not exist.** No `squad` mechanic and no person-scale grid anywhere in code. The duel is a **16-state** fight/engagement graph over *continuous measure* (no grid; zones), 53 weapons whose coefficients derive from physical parts at build time, armour-defeat thresholds `none 0 / light .30 / medium .45 / heavy .72`, damage `(strength+heft)×coupling×quality×1.55` through a penetration knee, **wounds as fractional obstacles rather than lost dice**, a 5% upset floor. The route is latent: mass battle **is** a facing-aware cell grid, and the proposal's answer is *a squad is the persons present at a rung, every combatant a `Person`; a cohort is a Person at weight > 1.* At weight 1 the same code is a squad game. |
| 8 | **Fieldwork & investigation** | **Most designed, least built.** `fieldwork.py` and `investigation.py` are stubs; both scene resolvers are stubs; only `knots.py` runs. In the proposed verb table **the six investigation acts declare no contest**, so inquiry is not merely ungraded — nothing resolves it. |
| 9 | **Character generation / progression / chronicling** | **Generation exists and never fires** — a five-axis NPC population engine deliberately never called at world-gen or season tick, because no canon names a count and the tree refused to invent one. **Progression does not exist: `capability` has no season writer, so nobody improves at anything** (F.6; repair is a `practice` verb, not a field). Chronicling is designed end to end (Portrait, draft Portrait) and built nowhere. |

**The structural observation.** **Seven of the nine module contracts with no design document are
exactly the layers this list names** — the overview director, scenario authoring, the scene slate and
timer, domain actions, settlement economy, NPC memory. The subsystems that are strong are the ones
whose physics could be modelled and measured. The ones absent are the ones where somebody must decide
**what a person wants, what an institution may declare, and what the world offers you this season.**

---

# §3 · EIGHT CLAIMS THE TREE MAKES ABOUT ITSELF THAT ARE FALSE

Found by reading across lanes, then attacked by a structurally independent read-only critic
(`subagent_type: valoria-critic`) which found further defects in the reading itself. **Each row below
was re-verified by hand after the critic reported it.** Three are corrected in code by the commit that
adds this file; five are recorded for their owning lane.

| # | the false claim | where | the measured truth | falsifier |
|---|---|---|---|---|
| **1** | *"GD-2 mandatory-actions precedence is enforced inside `faction_take_action`"* and *"GD-2: mandatory threat-response before stochastic selection"* | `engine/mc_v18.py` `_faction_actions_callback` docstring · `systems/factions/sim/faction_action.py` `faction_take_action` docstring | **There is no mandatory pass.** The body computes four signals, three weight multipliers and takes **one** `rng.random()` draw. "Threat" is a *Muster weight multiplier* (`muster_mult = 1.0 + threat`), not a forced action. Canon's own violation test (`canon/02_canon_constraints.md` GD-2) fails against live code. **The faction AI has no reflex: it can be threatened and roll something else.** | `grep -n "mandatory" systems/factions/sim/faction_action.py` returns docstrings only |
| **2** | Political Stability ≤ 6 is a live victory clause | `engine/autoload/victory.py` reads `world.clocks['Turmoil']` | **Nothing writes Turmoil.** It appears exactly twice in the tree: initialised `0.0` in `game_state.py:338`, read in `victory.py:73`. The clause is **vacuously true**, so GD-1 is currently two of its three conditions. Canon's *"(treaties counting)"* is also unimplemented — territories count by `owner` only and treaty proposal is a stub. | `grep -rn "Turmoil" --include="*.py" engine/ systems/` → 2 hits |
| **3** | The insurgency pipeline and the NPC population engine "execute" | `systems/world/sim/` both invoked every season from `accounting.py` | **Both are pinned at zero and named as such:** `engine/tests/test_f7_smoke_oracle.py` asserts `insurgencies == 0` and `npcs == 0`, calling them *"built-but-unreachable islands"*. NPE drifts an empty population. **GD-3's revolt→insurgency→faction pipeline has never fired.** | `python -c "from engine import mc_v18; r=mc_v18.run_campaign(seed=7); print(r.insurgencies_formed, r.npcs_generated)"` → `0 0` |
| **4** | *"every call site in the tree still passes a hand-set Ob"* | `engine/autoload/dice_engine.py` `degree_from_net` docstring | **False.** `systems/factions/sim/crown_initiative.py` `coronation_renewal_ob` implements `floor(Church.L / 2) + 1` exactly, and Royal Progress derives from the gap; tribunal derives under formal grounds; only `parliamentary_transfer` contradicts (`L+2`), and **that number is ratified canon**. Reconciling the three is **SUSPENDED by Jordan, 2026-08-21** — it is a systems ruling, not an edit. Recorded on the progress board and contradicted by the docstring. | `grep -n "coronation_renewal_ob" systems/factions/sim/crown_initiative.py` |
| **5** | The mass-battle **cell is the primitive** for morale, discipline, quality, stamina, rout, health, armour, facing, damage, troop count | `systems/mass_battle/sim/config.py` — the quoted **directive**, followed on the next line by *"PHASE 1: MORALE"* | **Live: morale, facing and damage placement per cell. Stamina is per column** (`percell.py`, `_ColBlock.stamina`); **discipline is subunit-level.** The list is an instruction, and reading it as accomplished state is the error. | `grep -rn "cell.*discipline" systems/mass_battle/sim/` → empty |
| **6** | Four mass-battle flags are *"Default OFF"* / *"RETRACTED to OFF"* | `config.py`: `PC_CELL_MORALE`, `PC_CELL_DAMAGE`, `PC_CLOSE_RANKS`, `PC_FRICTION_CEV` | **All four default ON** (`environ.get(..., '1')`). For `PC_CELL_MORALE` the block above it explains why — the goldens were re-recorded under the flip so the change-detector keeps tracking the shipped configuration — and the trailing comment was never updated. **Code is the mechanism; these comments are stale.** MB lane. | read the four assignments |
| **7** | Six faction-unique actions are unbuilt | commonly cited count | **Seven.** The six stub-wired ones plus `systems/mass_battle/sim/altonian_reinforcements.py`, which still `raise NotImplementedError` — the only unconditional raise outside an abstract base, and an action GD-1 names by name. | `grep -rn "raise NotImplementedError" systems/` |
| **8** | Every verb's `requires` is prose, full stop (F.24) | `04_CODE_ARCHITECTURE.md` F.24 | **Half-closed since rev. 2.** §F.24a **derived** the seven-form grammar *from the 32 live cells rather than designing it*, and `verb_table.yaml` now carries `requires_typed:` per row. Prose survives in the seam, not in the specification. | `grep -c "requires_typed" proposals/2026-09-02-executable-architecture/verb_table.yaml` |

## §3.1 · What the campaign actually does, stated plainly

`python -c "from engine import mc_v18; r=mc_v18.run_campaign(seed=7); print(r.winner, r.season, r.stub_hits, r.scenes_resolved)"`
→ `Crown 50 100 111`.

**It ran all fifty seasons and a tiebreak named Crown** (`held×10 + L + len(territories)`), because a
GD-1 victory cannot fire (§3 row 2). `stub_hits == 100` is two deliberate refusals per season ×50 —
`generate_npc` and `form_knot`, neither of which has a canon-named trigger or count, both recorded
through `stubwire` rather than invented. Those two are the stub calls `tools/m1_acceptance.py` reports.

**So the honest description of the shipped campaign is: four factions take weighted actions for fifty
seasons, battles resolve properly, and then a tiebreak names someone.** The parts run; the world does
not notice.

## §3.2 · The corroborating measurement

The repository's own instrument says the same thing from the other end. Forking every mechanical
decision in the ARC/NPC corpus and following three decisions on: **2,403 forks changed nothing
downstream, 2,403 times.** After the 2026-09-04 work the world diverges in **100%** of forks and later
decisions diverge **4.2% at the 2×1 cell by verb-only fingerprint** — 34.6% by `(verb, subject)`, and
**0% at 2×3**. ⚠ **The result is cell-dependent and the number must never be quoted without its cell**
(`HANDOFF.md`, and `registers/handoffs/HANDOFF_IN.md` top section, which says so in as many words).
`NPC RUNS = 0`, `ARC ENDS = 0`.

Corpus run: 122 probes at **63 PASS / 59 GAP**; **46 NPC cases** (6 BLOCKED, 2 DEGRADED, 38
NOT-ASSESSED) and **97 ARC cases**, all NOT-ASSESSED. ⚠ NOT-ASSESSED is defined by the caselog as
*nobody authored an `exercises:` overlay* — **a fact about authoring, not a verdict on the design** —
and there are zero ARC overlays, so every ARC is NOT-ASSESSED by construction.

Milestone gate: `python tools/m1_acceptance.py --summary` → **NOT MET**. Rows 1–2 are honest execution
measurements (a seeded probe season; same-seed `KeyLog.content_hash()` equality). **Row 4 is
doc-derived and says so of itself** — it counts `state: done` strings on a hand-edited board — so a
green row 4 is never evidence that a juncture runs.

---

# §4 · THE ARCHITECTURE CHAIN, AND WHAT RATIFYING IT WOULD DO

**Everything in this section is PROPOSED and held back in full.** `proposals/2026-09-01-holonic-architecture/`
(#353, Parts I–VI, inherited whole) → `proposals/2026-09-02-executable-architecture/` (#357, the verb
table and write matrix as data) → `proposals/2026-09-03-meta-architecture/` (#358 rev. 3, the axioms
and the code shape) → `proposals/2026-09-04-social-contest-branches/` (#365/#369). By their own status
lines **nothing ratifies on merge.**

## §4.1 What it commits to

Three questions, asked in order. **Who owns this?** — one owner about one thing is a field, one owner
about two is an edge, no possible owner is a Query computed and stored nowhere; **two owners means you
have located a defect exactly.** **What can check this?** — data a loader validates, or code with a
falsifier; **prose is a pointer, never a mechanism.** **Whose act makes this happen?** — a named person
at a venue paying for it, or one of three licensed motions; **nobody's means you have found a narrator,
and you remove it.**

Six axioms: only a person acts · nobody has privileged access to the world · what is true and what is
right are different kinds of thing · every value has exactly one owner and the owner is its only writer
· the world moves by itself in exactly three ways (matter, bodies, the fading of memory) · nothing
becomes permanent without an author.

What falls out without being built: **obstruction needs no verb** (the stranger takes the seat; your
act is simply refused, and the refusal emits); **scarcity is the fold's order** (the second person at
the granary finds it empty and gets a *different* event, and no verb mentions contention);
**deception is free** (an Event carries no actor, so attribution is a claim each witness mints);
**institutions have handles** (every opening act declares its own end condition, so a term can be
bribed, delayed, burned or killed — *a process nobody authored has none of those, which is the
definition of a GM*).

The loop: **CALENDAR → MATTER** (the world moves, then **freezes**) **→ DELIBERATE** (simultaneous, a
pure map) **→ RESOLVE** (an ordered fold, the only writing step for acts) **→ WITNESS** (one fan-out,
then each person deposits into their **own** ledger) **→ CENSUS**. A contest re-enters at exactly one
point, sides frozen at entry, and must return **a Margin, never a winner**.

## §4.2 What ratification would replace

- **The faction stat block.** `L / Sta / W / I / Mil` are aggregates over many owners; `AX-4` + `T-a`
  forbid storing an aggregate. A faction **owns nothing** — it is a view resolved from `commit` edges.
  This takes `Faction.adjust` (the current single write owner), `MULTS`, the domain-echo amount table,
  the parliamentary genre→stat mapping, the emergency-council faculties derived from `L` and `7 − Sta`,
  the combat bridge's `history = Mil`, and the fallback tiebreak.
- **Accord and PT as territory fields.** `Rung`'s NEVER row is written against exactly this: *no norms,
  no unrest, no legitimacy, no reputation.* They become Queries, or they move onto persons.
- **GD-1**, which is a predicate over those fields. Restating it as a Query is easy; whether to is
  canon-level. Mitigated by §3 row 2 — it is already unreachable.
- **The seven world clocks**, one at a time, against `AX-5`: each needs a named winding act or it is a
  fourth clock. Turmoil resolves by deletion.
- **`Event.subject`.** Today the fold sets it to the actor and WITNESS deposits every claim with it, so
  every ledger reads *"I hold that X did Y"*, certainly and identically. `T-d` deletes the field.
  **That one deletion is what turns the epistemic layer on** — and it is the change most likely to move
  goldens quietly.
- **The contest terminal**, which must return the margin `PersuasionTrack`/`ProofBar` already compute
  and discard. The cheapest conformance in the chain.

## §4.3 What it would keep

The **dice primitive** entire. The **physics of both combat layers** — weapon derivation, armour-defeat,
the penetration knee, wounds as fractional obstacles; cells, morale, rout, Lanchester, facing. What
changes there is *who the units are* (persons at weight, no unit class) and *what the seam returns*.
The **Key substrate** (log, invariants, content hash, deferred-apply boundary), which is already most of
the proposed `state/log`. The **settlement ledger**, the closest thing in the tree to the proposed
`Record`, needing a custody dimension rather than a rewrite. And **the fiction entire.**

> **The shape of the work is therefore: keep the physics, replace the spine.** The shipped engine's
> replaceable half is the World/Faction/Territory state and the fold; its irreplaceable half is combat,
> mass battle, the dice, the substrate, and the calibration behind them — the only execution artifacts
> in the repository, and the only evidence `CLAUDE.md` §0.2 accepts. The chain proposes no change to any
> of the physics.

## §4.4 What ratification would not give

Nothing runs by it — every stage says so of itself. **Nothing founds or builds** (F.20). The typed
`requires` grammar is derived but not applied (F.24/F.24a). **No verb writes any `Person` interior
field** (F.20a), so convictions cannot move and the moral layer has no producer. **`capability` has no
season writer** (F.6). And three gaps were opened by the 2026-09-03 amendment itself: whose edge a war
is and therefore who makes peace when the declarer dies (F.32); whether `at_war` may reach a verb's
eligibility (F.33); what a demand is, without which individuation starves the political layer (F.1).

---

# §5 · WHAT THE CHAIN LEAVES OPEN

Recorded as facts about the chain. No row here is flagged `needs_jordan`; each is a live design choice
where two defensible options lead to materially different games, which is the only thing `CLAUDE.md` §0
counts as a genuine escalation.

1. **Whether the faction stat block survives.** Either `AX-4` is scoped to exclude the strategic
   aggregate layer — a deliberate exception with a stated cost — or the stats become Queries and every
   consumer is rebuilt. A choice about what game it is, not a refactor.
2. **Whether Accord and PT survive as territory fields**, and whether GD-1 is restated or redesigned.
3. **Which of the seven clocks survive `AX-5`**, act by act.
4. **Four games, or venue rows plus one `settle()` build.** The later audit says abandon the framing.
5. **Who authors the occasions.** CALENDAR fires dates; what *puts* a date there is `scenario_authoring`,
   one of the nine contracts with no design doc. The chain does not answer where drama comes from — it
   makes the question askable exactly, and hands it back.

## §5.1 · Two process hazards, recorded so they are decided rather than discovered

- **Ratification-by-merge collides with the chain's own status lines.** `CLAUDE.md` §2 (ED-1094) says
  merging ratifies PROPOSED contents by default; every document in the chain says *nothing ratifies on
  merge*. Both cannot hold on the merge that ratifies. If it happens, the `## Status:` flips, the ledger
  `status`/`needs_jordan` fields and the `CURRENT.md` rows must move **in the same commit** — otherwise
  the chain sits PROPOSED in `main` and the next session reads it as unratified, which is the failure
  ED-1083 recorded.
- **`FORK:c451bcb` is unfollowable in a shallow clone.** `references/restructure_ledger.md` sends rows
  there; `git cat-file -t c451bcb` fails in an 89-commit checkout, which is what fails
  `tests/valoria/test_forked_status.py`'s two ref tests locally. Independently hit by the social-contest
  branch-shapes pass. **A provenance pointer nobody can follow reads as resolved and is not.** IN lane.

---

# §6 · REPRODUCTION — do not re-derive these by reading

```
python tools/m1_acceptance.py --summary                 # does the milestone RUN (not: is it documented)
python -c "from engine import mc_v18; r=mc_v18.run_campaign(seed=7); \
           print(r.winner, r.season, r.stub_hits, r.scenes_resolved, r.insurgencies_formed, r.npcs_generated)"
python -m pytest tests/valoria -q -n auto               # unit suite
python -m pytest engine/tests -q                        # seeded campaign + parity regression (~5m30s)
python tools/balance_oracle.py                          # n=120/arm campaign control; NOT a CI gate (~13m)
python tools/export_sim_params.py --build               # citation coverage over the typed params
grep -rn "Turmoil" --include="*.py" engine/ systems/    # §3 row 2
grep -rn "raise NotImplementedError" systems/           # §3 row 7
```

⚠ `tests/valoria/test_forked_status.py` fails in a shallow clone for the reason in §5.1. That is an
environment artifact, not a regression — check the clone depth before reading it as one.

---

## Provenance

Session of 2026-09-05, IN lane, ED-IN-0202. Method: read `CURRENT.md` → `HANDOFF.md` + `HANDOFF_IN.md`
→ `canon/` → `engine/` and `systems/` bottom-up → the September proposal chain; two scoped mapping
agents over `engine/` and `systems/`; then the whole reading handed to a structurally independent
read-only critic (`.claude/agents/valoria-critic.md` — `Read, Grep, Glob`, no write tools, so its
independence is structural rather than declared), which found eight defects in it, **every one of which
was re-verified by hand before being recorded here** and one of which — an ARC case count — was
**wrong**, and is not carried.
