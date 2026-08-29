# 04 — Consolidated owner map, keying register, and modularization

## Status: FILED (2026-08-29) — analysis. Reads: [`00_INDEX.md`](00_INDEX.md)
## This is the organizing/modularizing/keying/curating half of the request, collated across all nine
## critics. Where two critics disagreed the disagreement is shown rather than averaged.

---

## 1. The owner map — who owns what, and what is orphaned

**Owned and sound** (no critic found a hole):

| object | owner |
|---|---|
| the no-leader-no-action gate, per tier | `05 §1` `fa.gate`, executing ED-IN-0201 |
| delegation — acting on behalf of | `01 §4` Post; `remit`-as-gate `01 §4.3` |
| the player as a person holding posts | `01 §4.4` |
| the roll's actor is a person, never the faction | `05 part2 §6` |
| the acted-upon as actor (refusal) | `04 §4.0` — *the suite's best single mechanism* |
| disclosure as a registry field | `01 part2 §8` (E-2) |
| the cast gate and five witness channels | `10 §3` |
| headless resolution + three invariance properties | `10 part2 §6` |
| footing as one derivation at many nodes | `06 §4.2`, adopting canon's arithmetic |
| creed subset, cap, Scar, revision gate | `02 §6` |
| memory decay / forgetting (salience top-K) | `01 §3.2` |
| feelings person↔person | `01 §7` + PP-724, cited not invented |
| feelings person→faction | `01 part2 §7.2.1` (`allegiance`) |
| the guard-predicate table that forbids guarding prose | `13 §6` |

**Contested — two owners, or one owner and one contradiction:**

| object | claimant A | claimant B | consequence |
|---|---|---|---|
| **`Holding` storage** | `01 §3.1` — a Tag kind on `substrate.ledger` | `02 §6.2` + ruled design §4 — `npc_memory` registry bucket | **A reader implementing either page alone builds a different store.** T2 finding 3, T3 finding 8 |
| **`information`** | `01 §5.2` — owner *faction* | `05 part2 §5.3, §10.4` — owner *target*, 0–5 | T4 finding 2; and neither resolves the **knower** |
| **`exposure`** | `01 §5.2` — person-scoped, decaying, survives reassignment | `fieldwork_exposure.md` — per-territory, Cover-thresholded, reset each season | X-4; `08` uses both senses in one document |
| **the Finding Key** | `08 §8` — `investigation.resolved`, "not yet contracted" | `key_type_registry_v30.md:881` — `scene.investigation_resolved`, **registered** | T9 finding 2 |
| **the commitment object** | `12 §4` — treaty `Debt` clauses | `clock_registry_v30.md:89` — the Obligation clock | T7 finding 6; no override row filed |
| **`faction.treasury`** *(resolved in-suite)* | `06 part2 §9` had it `writable: false` | `05` spent it | Fixed by O-5.10/C-7 — **the suite caught this one itself** |

**Orphaned — owned by nobody:**

| orphan | raised by | consequence |
|---|---|---|
| **a battle's actor** — no mechanism routes the commander's person into the force model | T1 | T1 fails at the seam |
| **NPC epistemic policy** — what an NPC may read | T4 | no shared rule governs `appeal`, `preference`, `accepts`, bloc formation or advance terms |
| **the perception → Holding edge** — `scene_slate` emits `scene.witness`, `npc_memory` consumes `scene.gossip`, nothing connects either to a Holding | T2, T3 | misperception has no producer |
| **belief consumer in any decision function** | T2, T4 | promised by `01 §4.3`, implemented nowhere |
| **the `legitimating.*` producer** | T1, T5 | the mass actor cannot fire |
| **a declaration path for bloc/faction projects** | T1 | change C's schism chain dies at step one |
| **the agentive/non-agentive criterion for `remit_kinds: []`** | T1 | any actor can be demoted to weather |
| **the leaf-1/2 fence on actorless effects, post-merge** | T1 | a world event revoking a governor is schema-legal |
| **iteration of non-faction posts** (`08 §3`'s residual) | T1 | a character can be stopped from acting |
| **an upward demand object** | T5 | filtering-by-nonexistence |
| **person→place / person→policy feeling** | T2, T6 | the down-stroke's last hop |
| **conducting an authorized investigation** | T9 | Authorize opens a case nothing can conduct |
| **the tick-wide emission budget** | T8 | `11` disclaimed it, `13` never received it |
| **log-read reactivity** — who may derive from the Key log, how far back | T8 | J-N's open flank |
| **the Precedent key namespace** | T5 | how X-3 shipped invisibly |
| **`env.population_change`** — declared edge, zero emitters | T8 | *flagged as a check, not a ruling — `03` unread by that critic* |
| **the community rung** | T5, T6 | → **J-2** |

---

## 2. The keying register

Consolidated across critics. **EXISTS** means verified in the ratified registry, by reading.

### 2.1 Key types

| type | status |
|---|---|
| `mechanical.project_advanced` | **EXISTS** — `key_type_registry_v30.md:446`, ED-935 · no live emitter |
| `state.project_completed` / `state.project_failed` | **EXISTS** — `:691`, `:710` · no live emitter |
| **`scene.investigation_resolved`** | **EXISTS** — `:881-897`, with `finding`, `subject_id`, optional `witnesses` · **the suite declares it missing** (T9 finding 2) |
| `scene.witness` | **EXISTS** as an emission — `module_contracts.yaml:630` (`scene_slate`) · consumer edge unclaimed |
| `state.belief_revised` | **EXISTS**, reserved for the creed beat · attribution conflict `[OPEN — Jordan]` at `module_contracts.yaml:331` |
| `state.opinion_revised` | **EXISTS** — the `[1,5]` confidence ladder the ruled design reuses |
| `state.project_formed` | **MISSING** — adopted from G-29 · BLOCKED on P0-1 **and** G-17 |
| `state.proposition_revised` | **MISSING** — designed in the ruled proposal, **absent from `00 §9.2`'s minimum set** · would then be P0-1-blocked |
| `entity.created` | **MISSING** — needed by `fa.charter` **and** `act.muster`; one registration, two callers · P0-1-blocked |
| `form.transitioned`, `post.granted/revoked/vacant`, `faction.action_declined`, `edge.formed/transitioned`, `world.event_fired`, `slate.item_surfaced`, `place.directive_issued/answered` | **PROPOSED-IN-SUITE** · all BLOCKED on P0-1 |
| a Key for a motion proposed/passed/defeated | **MISSING** — `ad.motion` emits nothing (T7 finding 2) |
| `investigation.resolved` (`08`'s consumed id) | **DUPLICATE** of `scene.investigation_resolved` |

### 2.2 Gauges and registry rows

| row | status |
|---|---|
| `fac.*` ×6, `set.*` ×6, `terr.fort_level` | **EXISTS**, all 0–7 / 0–5 / 0–4 — the pool-commensurate family |
| attribute roster (9) + `pending_tenth` sentinel | **EXISTS** — the suite's claim is accurate |
| conviction roster (13, incl. Virtue) | **EXISTS** — the suite's claim is accurate |
| `prac.thread_sensitivity` | **EXISTS-DEFECTIVE** — `ceiling: null` with a non-binding `open_ceiling_reference: 100` |
| **`prac.tps`** | **EXISTS-DEFECTIVE, and named nowhere in the suite** — floor **and** ceiling null. See [05](05_independent_verification.md) |
| `presence.<institution>` 0–7 | **PROPOSED-IN-SUITE** (`07 §4.1a`) — closes P0-3 |
| `allegiance.strength` −5…+5 | **PROPOSED-IN-SUITE**; descriptor row not yet written; **contradicted by `09:137-139`** |
| `information` | **BLOCKED** — contradictory owners, no scale, no knower |
| `exposure` (suite sense) | **PROPOSED**, scale undeclared, **name collision** |
| `faction.treasury`, `post.budget`, `cohesion`, `pressure`, `standing`, `acceptance.*`, `condition.*`, `accrual.entitlement` | **PROPOSED-IN-SUITE** — none present in the cooked registry today |
| `HOLDING_CAP`, `λ_sal`, `RELATION_SHARE_MAX` | **PROPOSED** in prose; **no registry rows proposed** |
| `credence.<proposition>` | **CUT by `02`, still written by `08`** — the ghost |
| a Turmoil writer (or gauge migration) | **MISSING** — P0-7 |
| evidence-reliability enum | **EXISTS in canon prose only**; `08:300` reads it; no registry row |
| investigator post kind / `reachable_by` vocabulary | **MISSING** — `08:301` is a placeholder |

### 2.3 Registry files and checks

| item | status |
|---|---|
| `references/rendering_dispositions.yaml` | **ABSENT** — verified. P0-1 gates every Key append |
| `references/form_registry.yaml` | **ABSENT** — verified. P0-6 |
| `references/content_registry.yaml` | **ABSENT** — verified. P0-6 |
| the Precedent **key namespace** registry | **MISSING** — no registry owns tag key vocabularies |
| the predicate registries (ruled P4: IN engine-evaluable, FI claim-only) | **MISSING** — no home under `00 §9`'s two-file ceiling |
| successor-graph acyclicity check | **MISSING**, admitted |
| `hysteresis:` present iff `entity_kind: place` | **MISSING**, admitted |
| per-emission magnitude-channel field (Q-5) | **MISSING** — `emits:` carries only `{type, terminal}`, so the declaration `01 part2 §9.2` requires is **undeclarable** |
| tick-wide emission budget check | **MISSING** — `11` proposes only its own slice |
| log-derivation allowlist | **MISSING** — nothing proposes it |

---

## 3. Modularization — against `00 §1`'s own elegance criterion

### 3.1 Under-distilled: several objects doing one job

| the job | the objects | source |
|---|---|---|
| **what an agent knows** | `Holding` · the `information` gauge · FI's reliability-tagged evidence · (and `investigation_surface` rows) | T3, T4, T9 |
| **how firmly a belief is held** | `Holding.confidence` (stored int) · the ghost `credence` gauge · *effective* confidence (a rest-prior derivation) · canon's `truth` 0–5 meter | T2, T3 |
| **what a political act is about** | a motion's `subject` (a tag) · a candidate's `subject_refs` (entity ids) · an argument's `prop_id`s | T7 — *"the same occurrence is three unjoinable records"* |
| **being noticed / being exposed** | the suite's `exposure` gauge · canon's Exposure track | T4, T9 |
| **a negotiated commitment** | treaty `Debt` clauses · canon's Obligation clock | T7 |
| **the route-cut fact** | `11`'s proposed tag · canon's route economics | T6 |
| **involuntary post removal** | `pm.recall` with cause+frequency+escalation · the rising's bare `post_revoke` | T1 |
| **what an actor attends to** | the Light Function (player) · `appeal`'s ad-hoc `signal(s, world)` list (every NPC) | T5 — *one salience mechanism evaluated per focalizer would honour `01 §4.4`'s one-engine rule* |
| **the event id** | `investigation.resolved` · `scene.investigation_resolved` | T9 |

### 3.2 One object doing two or more jobs

| object | the jobs | verdict |
|---|---|---|
| **`Precedent`** | institutional memory · machine trigger (`we_cooldown:*`) · cross-document transport (`founding_claim`, `failure_mark.*`, `legitimating.*`) | **Splitting is wrong** — that is the over-distilled failure. **Registering the key namespace is the fix**: one block, not a new file. T5, T7 |
| **`Holding`** | episodic memory (*I perceived this*) · doxastic state (*I hold this true*) | **Mostly right** per `00 §1` — but *"I saw it and no longer believe it"* leaves only a Scar; the perception record dies with the revision. Name the residue rule or accept the loss explicitly. T3 |
| **`Holding.value`** | confidence **and** salience amplitude | A half-believed suspicion about a murder should be maximally present; under this coupling weakly-held beliefs fade fastest, and the top-K sweep **preferentially forgets the `suspects`-stance leads P2 was ruled to protect.** T3 |
| **`acceptance.support`** | population stake · posture's cost sink · muster's consent cost · Defy's reward | **`00 §1`'s *over*-distillation failure** — the world cannot distinguish a town angry about conscription from one angry about taxes, so nothing downstream can route the right grievance to the right person. T6 |
| **the Key log** | append-only causality record · the Slate's only cross-season memory | J-O may split these; today only one J-O-fragile line is named while the memory role is bound by nothing. T8 |
| **`sm.respond`** | directive-response engine · investigation gate | The second job arrives through an **undeclared channel** — its contract declares only `consumes: place.directive_issued`. T9 |
| **`ad.motion`** | procedure · sanction-pricing · an unmodelled "persuasion" it has no fields for | The first two fuse defensibly; the third is a debate-shaped hole. T7 |
| **the O-5.11/O-5.13 dispatcher** | *characters acting* · *world happening* | **Over-distilled**: T1 itself becomes a field value (`remit_kinds: []`) rather than a type distinction. The merge is defensible; the missing pieces are the constraint row and the criterion. T1 |

### 3.3 Correctly distilled — worth naming, because the criterion is not only a stick

- **`04 §4.0`'s `accepts`** is `§4.2`'s preference function read from the other side. A dot product is
  symmetric, so it is *the same number computed once*. **This is what the elegance criterion looks like
  when it works.**
- **`06 §4.2`'s footing** — one function, three tiers, no third quantity to keep consistent.
- **`09 §5`'s obstruction** — no verb, no module, no branch: any act moving a term the project reads
  obstructs it, with no knowledge of the project at all.
- **`01 §3.2`'s salience** — a derivation over data the tag already carries, adding no stored field and
  no second decay law.

### 3.4 Three filters with three dialects, and no stated doctrine

`RELATION_SHARE_MAX` (selection) · `T/(T+K)` (aggregation) · Slate truncation (attention). Each is
per-rung correct; **no document states them as one filtering doctrine**, which is why T5's brief could
ask *"where does filtering live"* and get three half-answers. — T5
