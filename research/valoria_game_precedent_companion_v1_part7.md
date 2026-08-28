# Game Precedent Companion — Part 7: The Person Across Systems — Stance, Management, Presence

## Status: PROPOSED (2026-08-28) · reference under §0.05, not canon
## Version: v1.0 · Lane: IN (cross-cutting)
## Reads: Parts 5–6. **Corrects a coverage gap in Parts 1–4.**

**Reading order:** [1](valoria_game_precedent_companion_v1.md) → [2](valoria_game_precedent_companion_v1_part2.md) → [3 · Critique](valoria_game_precedent_companion_v1_part3.md) → [4 · Reconcile](valoria_game_precedent_companion_v1_part4.md) → [5 · Matrix](valoria_game_precedent_companion_v1_part5.md) → [6 · Decomposition](valoria_game_precedent_companion_v1_part6.md) → [7 · The Person Across Systems](valoria_game_precedent_companion_v1_part7.md)

Part 5 §12.5 surveyed **what a person is**. That is one of three questions, and the smallest. The
other two were not asked:

1. **Which stance is the person taking?** Acting *on behalf of* a faction at some scale is a different
   activity from acting *within* it — different objects, different failure modes, different fun.
2. **How is the person managed?** Assignment, appointment, promotion, recall — the layer where, in
   most surveyed games, the player spends the majority of their decisions.

⚠ **And a coverage failure in this companion, stated before anything else.** Valoria already has a
**declared six-title precedent analysis for the within-faction stance** — `systems/_architecture/player_agency_v30.md`
§1, covering ROTK Officer Mode, CK3 Vassal Play, Disco Elysium, Mount & Blade / Manor Lords,
Pathologic 2 and Pentiment, each with an explicit *"What Valoria takes"*. **Parts 1–4 of this
companion never read it.** They surveyed the strategic layer's precedents and skipped the design's own
personal-agency precedent set. §14.2 is that reading.

---

## §14.1 The two stances

**On behalf of** — you are the faction's instrument at a scale. A governor governing, a general
commanding, an envoy negotiating. Your success is the faction's success, and the interesting failure
is *incapacity*.

**Within** — you are competing for position inside the faction. Climbing, patronage, succession,
intrigue. Your success may come **at the faction's expense**, and the interesting failure is
*exposure*.

| Game | On behalf | Within | How the two relate |
|---|---|---|---|
| **RoTK (Officer Mode)** | ✔ assignments — develop a city, train troops, conduct diplomacy | ✔ **retains personal ambition** | **The same person carries both, and the friction is the design.** The officer may *"follow orders, exceed them, or subtly work toward personal goals that may conflict with their lord's interests."* Promotion runs officer → governor → lord |
| **CK3 (Vassal Play)** | ✔ liege obligations — levy, taxes | ✔ personal schemes — seduction, murder, fabricating claims | **Dual agenda held simultaneously.** Sometimes aligned, sometimes opposed; *"the friction between tracks is where gameplay lives"* |
| **Kremlin** | ✘ — you never act on behalf of anything | ✔ **exclusively** — you compete for control of politicians you do not own | There is no on-behalf layer at all. The whole game is *within* |
| **John Company** | ✔ ventures serve the Company | ✔ you compete for the offices that run it | **And the Company can fail while you win** — the tension is explicit and scored |
| **Republic of Rome** | ✔ the Republic must survive | ✔ factions compete for offices and prosecute each other | The **shared-loss** condition is what makes the tension real rather than nominal |
| **Total War** | ✔ **only** — you *are* the faction | ✘ (Three Kingdoms adds a court with Satisfaction) | No within-layer for twenty years; TK is the first |
| **Victoria 3** | ✔ you act as the state | ✘ — interest groups act within, but **you do not play them** | The within-layer exists and is not yours |
| **Suzerain** | ✔ you are the president | ✔ ministers advise **in their own interest** | The within-layer is NPC-side pressure on your on-behalf decisions |
| **Jagged Alliance 2** | ✔ mercs execute your contracts | ✔ **merc-versus-merc opinion**, which constrains who you may field together | The within-layer is a *staffing constraint* rather than a career |
| **Mount & Blade** | ✔ eventually, as a king | ✔ first, as a vassal | **Sequential rather than simultaneous** — you graduate from one stance to the other |
| **Brigandine / Unicorn Overlord** | ✔ | ✘ | Pure on-behalf |
| **VALORIA** | **Neither, because there is no person.** `governor_id` is the delegation object and has no writer; Standing is the position object and has no code | | — |

**Three readings.**

1. **The games that do both put both stances on the same person**, and say so explicitly. RoTK and
   CK3 — Valoria's own two declared precedents — are the two clearest cases.
2. **The two stances need different objects.** *On behalf of* requires a **delegation object**: a post,
   a commission, a term, a mandate that can be granted and revoked. *Within* requires a **position
   object**: a rank, a standing, a claim on a seat someone else holds. **Valoria has named both and
   runs neither** — `governor_id`/`succeed_governor` (delegation, zero callers) and the 0–7 Standing
   ladder (position, zero code).
3. **Pure on-behalf is a viable design** — Total War shipped it for two decades. Pure within is also
   viable — Kremlin is one of the best political games ever made and has no on-behalf layer at all.
   **What is not attested anywhere is a game with neither**, which is where Valoria currently sits.

---

## §14.2 What Valoria already declared, and whether anything supports it

`player_agency_v30 §1` is a precedent analysis for the *within* stance, with a stated take from each
title. Judged against the working tree:

| Declared precedent | What Valoria says it takes | Does anything support it? |
|---|---|---|
| **RoTK Officer Mode** | *"The duty assignment loop. A non-leader character receives faction objectives but retains personal agency to exceed, reinterpret, or subvert those objectives. Performance is tracked — success builds standing, failure erodes it."* | **No.** No assignment flow exists. The eight Duty types are designed-only. `Faction.standing` is a bare int mutated at eleven sites and is a **different quantity** from the officer ladder that shares its name |
| **CK3 Vassal Play** | *"The dual-agenda structure. The player always has two simultaneous motivation tracks — what their faction expects and what they personally want."* | **No.** There is no faction-expectation object (no Directive writer) and no personal-goal object (`goals` on 17/46 registry rows, zero loaders) |
| **Disco Elysium** | *"The scene opportunity as interpretive invitation, not directive… Beliefs are what the character finds significant"* | **No.** `add_belief` is the sole constructor of a `Belief` and has zero callers, so a live campaign can never contain one |
| **Mount & Blade / Manor Lords** | *"Stature progression as emergent possibility, not scripted path… the player's accumulated standing, relationships and capabilities reach a threshold where leadership becomes mechanically available"* | **No.** And a UI audit independently flags it: the faction-emergence pathway *"is not surfaced as a tracked progression"* — the design's most rewarding long-form arc, with invisible progress |
| **Pathologic 2** | *"The scene action budget as triage… opportunities not pursued do not wait"* | **Partially.** The Slate exists; the budget does not, and nothing resolves unpursued opportunities |
| **Pentiment** | *"Investigation is social performance"* | **No.** Fieldwork and social contest do not touch |

**The finding is not that these are unbuilt.** It is that **six declared precedents were analysed, a
take was written for each, and the take was never bound to a module.** That is the same shape as the
integration master's F3 — a claim that agrees with itself across surfaces because all the surfaces
descend from one un-executed source — and it is why this companion's Part 3 rated People *"below the
floor, built inside-out."*

---

## §14.3 The management layer

Where the player actually spends decisions in every surveyed game that has people — and the layer
Valoria has no representation of at all.

| Game | Assignment surface | What gates a good assignment | Anti-spam guardrail |
|---|---|---|---|
| **RoTK** | Officers to cities, posts and armies; **eight domestic commands**, each keyed to one of four stats | The officer's stat against the command's keyed stat, and **class** for troop caps | Officer actions per turn, flat 10 gold each |
| **CK3** | **Five council seats**; granting and revoking titles; renegotiating vassal contracts | Councillor skill; vassal opinion | **Explicit and deliberate**: one "tyrannical" contract change outstanding at a time, escalating opinion costs (−15 then −25 up, +5 then +10 down), a per-vassal frequency cap. Built *as a guardrail* rather than trusting self-regulation |
| **Total War** | General recruitment and retinues; agent assignment; governors (three times) | Traits, retinue, class *(TK)* | Turn economy; agent caps |
| **TW: Three Kingdoms** | Administrators — **decoupled from physical presence** | Class, satisfaction | Court capacity |
| **Jagged Alliance 2** | Hiring and contract renewal (per-day pricing); squad assignment | Merc skills, **and pairwise opinion — mercs refuse to serve with people they dislike** | Money; the opinion matrix itself acts as a constraint |
| **Brigandine** | Knights to bases; **monsters to knights** | Knight class and Rune Area capacity | Base capacity |
| **Unicorn Overlord** | Squad composition and leader assignment | Class synergy | Squad size |
| **Suzerain** | Cabinet appointments | Minister competence vs loyalty | Political capital |
| **VALORIA** | **None.** `governor_id` is `None` on all 37 settlements after world-gen; its only writer `succeed_governor` has **zero callers**; `Settlement.npc_ids` is an empty list with no writer anywhere | n/a | n/a |

**Two findings.**

1. **The assignment surface is where the game is, in almost every case.** RoTK's eight commands, CK3's
   council, JA2's squad-building — these are the screens players spend time on. Valoria has designed a
   verb menu, an AP budget and a governor field, and wired none of them to each other.
2. **The guardrail is not optional and nobody discovers it early.** CK's caps exist because assignment
   surfaces get spammed; JA2's opinion matrix doubles as a staffing constraint. Any Valoria appointment
   flow needs its cap designed **with** it, not after — which is the same lesson as Imperator's, from
   the other end.

---

## §14.4 The person *inside* each system — does identity change the outcome, or only a stat?

The presence question. A person can be present in a system three ways: **absent**, **present as a
stat** (their number feeds a formula), or **present as an identity** (which person it is changes what
is possible, not just how much).

| System | Absent | Present as a stat | Present as an identity |
|---|---|---|---|
| **Settlement** | Victoria 3 (states, not governors) | RoTK — the officer's stat scales the command's effect | CK3's councillors (different tasks per seat); TW governors' traits |
| **Mass battle** | — | **TW's lord aura** — a flat bonus; **Dominions' commander** — an anchor | **TK's class gating** — *which* commander determines which unit types exist; **Brigandine's Rune Area** — the knight's position determines what survives a rout |
| **Deliberation** | Victoria 3 (IGs, not people); **Valoria** | — | Republic of Rome's senators; John Company's officeholders; **Kremlin's politicians**; Suzerain's ministers |
| **Contest / persuasion** | — | — | **Burning Wheel** — the person *is* the resolution; **Disco Elysium** — skills as interlocutors with agendas; **Triangle Strategy** — convictions gate which arguments are available |
| **Recruitment** | — | CK levy size from control and opinion | **TK** — the commander's class gates the roster |
| **VALORIA** | Deliberation (the emergency council derives **both sides from the same faction's aggregates**) | Mass battle (`power = round(Mil)`); everything else | **Nowhere.** `derive_command(charisma, cognition)` is the one place identity would change a battle, it is clamped, its flag defaults ON — and the adapter sets neither attribute |

**The discussion.** Present-as-a-stat is cheap and reads as a modifier. Present-as-an-identity is what
makes a roster worth having, because it turns *losing a person* from a subtraction into a
**capability loss**. Every surveyed game that people remember for its characters is in the third
column somewhere.

**And it is the third column that carries the failure mode Part 6 §13.3 flagged.** TK gates on
**class**, so losing a person means promoting another. Valoria's designed §1.5 gates on **biography** —
*"the officer with Cavalry History"* — so losing one person costs you cavalry permanently. Identity
presence is right; identity presence keyed to an individual rather than a role is the trap.

---

## §14.5 The divergent-interest agent — where the two stances collide

The interesting case is a person acting *on behalf of* a faction at a scale whose *within*-faction
interest points elsewhere. Every game that has both stances builds this deliberately.

| Game | How divergence is expressed | What it costs the diverging agent |
|---|---|---|
| **RoTK** | The officer may *"follow orders, exceed them, or subtly work toward personal goals that may conflict with their lord's interests"* | Loyalty, and the recruiter-side tell at LOY ≤ 70 |
| **CK3** | Vassal schemes run **against the liege** — murder, claim fabrication, factions | Dread, opinion, tyranny |
| **Kremlin** | The entire game — your man's rise is other players' loss | Exposure and purge |
| **John Company** | Office powers serve you and the Company unevenly; **payoffs are uneven by design** | The Company's failure, which is also yours |
| **Republic of Rome** | Prosecution of senators for ethical lapses | The shared-loss condition bounds how far anyone can push |
| **Suzerain** | Ministers advise in their own interest | — |
| **VALORIA** | — | — |

**The corpus's own verdict, and it is sharper than "unbuilt":**

> *"Does any executing code model an agent whose interest diverges from its own faction's? **No.**
> Five lanes said so independently. But 'no' is the wrong shape of answer. The divergent-interest
> **contest** already executes on the default campaign path **~975 times per golden batch**. What is
> missing is not the contest, the trigger, the resolver or the consequence. **What is missing is that
> neither side is anybody.**"*

**Three near-misses, each verified, and each is the same shape as everything else in this companion:**

| the near-miss | why it does not fire |
|---|---|
| **`NPC.hidden_allegiance`** — the one field modelling an agent whose interest diverges from its faction | Computed at `npe.py:327` on one of five deviation branches, then **omitted from the constructor call** below it. The field defaults to `None`. One branch consumes an RNG draw and writes nothing; **zero reads** anywhere |
| **The ledger's rivalry vocabulary** | `TAG_KINDS` contains exactly the intra-faction rivalry primitives, and **every Grudge/Debt/Leverage key authored anywhere in the corpus is already intra-polity** — governor ↔ local actor ↔ Crown agent, inside one Crown settlement. **The substrate's intended first use *is* intra-faction rivalry.** It has no writer |
| **`contest/faction.py::succession`** | Two claimants **within one faction** contest leadership on the Persuasion Track, with §7.2.1 ratios and a Verdun-843 grounding. Callers: its own helper and a kernel test. **Unreachable by construction** — `Faction` has no leader field, so leader elimination is not an event the season loop can produce |

**So the within-stance is not merely undesigned. It is designed three times over, in three different
modules, and none of the three can fire** — one because a constructor drops an argument, one because
nothing writes a tag, and one because the entity it contests over does not exist.

---

## §14.6 What this adds to the four unified moves

Part 4's U-3 said *"the person as a relationship ledger with a roster attached."* This part narrows it:

- **U-3 needs two objects, not one.** A **delegation object** (post, term, mandate — grantable and
  revocable) for the on-behalf stance, and a **position object** (rank, standing, claim) for the
  within stance. Valoria has named both and runs neither. Building only the first gives you Total
  War; building only the second gives you Kremlin; **the two declared precedents, RoTK and CK3, are
  both games that build both.**
- **The management layer is a first-class surface, not a consequence of having people.** It is where
  the player spends decisions in every surveyed title, and it needs its anti-spam guardrail designed
  with it.
- **Aim for identity-presence, keyed to a role rather than a person.** That is the difference between
  losing a governor being a promotion opportunity and losing a governor being a permanent capability
  loss.
- **The divergent-interest case is nearly free.** The contest already runs ~975 times per golden
  batch; the ledger's intended first use is already intra-faction rivalry; `hidden_allegiance` needs
  one constructor argument. **What is missing is that neither side is anybody** — which is exactly
  what U-3 supplies.
