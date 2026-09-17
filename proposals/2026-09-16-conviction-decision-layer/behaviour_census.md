<!-- STATUS: PROPOSED — held back in full. Diagnosis, not a decision. -->
<!-- AUTHORITY: none claimed. This document rules nothing and supersedes nothing. -->

# Behaviour Census — everything in the tree that answers *how does this character behave?*

## Status: PROPOSED — HELD BACK

> ⚠⚠ **SUPERSEDED BY ED-IN-0232 (PR #407, 2026-09-17) — THE KEY SUBSTRATE IS RETIRED, AND FOUR
> CLAIMS IN THIS DIRECTORY DIED WITH IT.** Measured on the merged tree: `engine/substrate/keys.py`
> is **gone**; `engine/substrate/` now holds only `canon_buckets · composition · descriptors ·
> names · stubwire · world_initial_state`. Grepped, not assumed: **no `beneficiary` role survives
> anywhere in `engine/`**, and **nothing validates axis names at emission** — no
> `KeyValidationError`, no invariant 6.
>
> | claim, as landed | status now |
> |---|---|
> | the axis roster is **blocking** at Key emission (`keys.py:400`) | **DEAD** — the validator is deleted |
> | falsifier: emit a Key with `{"equity": 0.5}` and watch it raise | **UNRUNNABLE** — there is no `Key` to emit |
> | two hardcoded axis rosters with nothing comparing them | **RESOLVED BY DELETION** — one copy is gone, so `engine/season/rosters.yaml` is now the single owner |
> | `beneficiary` is *"already a Key role — a bridge, not an invention"* | **FALSE** — it is an invention again, and orientation's obstacle is larger than this directory says |
>
> One flag this directory raised is also resolved by the same PR: `tools/export_key_types.py`,
> which parsed a `systems/**/*.md` against §0.05 clause 2, was **deleted**.


**§0.05 class: REFERENCE.** Nothing here is a mechanism. It cites code and documents; it changes
neither. If this file were deleted the game would behave identically — which is the test, and it
passes as reference.

**What it is for.** Jordan, this session: *"So many different documents speak towards items that all
converge on the same question of: how does the character behave?"* — and, on the same thread,
*"all this different related work is why we need to start from scratch."* This is that convergence,
counted, so the from-scratch build starts from a measured inventory rather than from memory.

**What it is not.** Not a design. Not a proposal for an axis set. Not a retirement plan. It names
what exists and what condition it is in. Every row was opened at the line cited; nothing here is
reported from a grep count or a summary.

---

## §1 The convergence already has a name, and the tree lost it in a file split

`systems/npcs/reference/npc_behavior_v30.md` is the canonical head for NPC behaviour
(`CURRENT.md` row **NPC behaviour**; the doc's own line 6 reads
`## Status: CANONICAL — approved 2026-04-17`). Its §1.1, at `:16`, reads in full:

```
### §1.1 The Stance Triangle

Every named NPC holds three interconnected attributes.
                                        ← five blank lines, then §1.2
```

The three attributes are in the other half of a grandfathered index+infill pair,
`npc_behavior_v30_infill.md:12`:

> **Conviction** — the NPC's operative worldview. What they believe grounds value. **Determines what
> the NPC wants to do.**
>
> **Ethical Framework** — inherited from the NPC's faction. What the institution incentivises.
> **Determines what the NPC is rewarded for doing.**
>
> **Resonant Style** — the argument form that bypasses the NPC's defenses. Their structural
> vulnerability in social engagement. **Determines how the NPC can be moved.**
>
> *"These three attributes jointly produce NPC decisions in TTRPG, NPC priority trees in BG, and arc
> transitions in all modes."*

**Want · rewarded · moved.** Three *different kinds of operator* — a preference, an incentive, a
susceptibility — named as one structure on 2026-04-13, and invisible to anyone who reads the head.

This is the single most important finding in this census, and it is not a criticism of the Stance
Triangle. It is the observation that **the repository already answered Jordan's question, correctly,
and then filed the answer where no reader arrives.** §4 of `CLAUDE.md` retired the index+infill
pattern as a default for exactly this reason; this pair is one of the grandfathered ones.

---

## §2 The census

Every mechanism in the tree that decides, modifies, gates or generates a character's behaviour.
**`live?` means: does code execute it today.**

| # | mechanism | shape | decides | opened at | live? |
|---|---|---|---|---|---|
| 1 | **Conviction** (13, weighted) | vector over a closed roster; 1–3 primary at 0.6–0.8 plus cultural 0.2–0.4 | what they want | `conviction_taxonomy_v30.md` §2, §4 | **yes** — `Person.convictions` |
| 2 | **Conviction axes** (4) | 13×4 projection matrix | the scoring basis | `conviction_axis_matrix_v30.md` §2; `engine/substrate/keys.py:59` | **yes**, and blocking — `keys.py:400` raises on an unlisted axis name |
| 3 | **Ethical Framework** (7) | **Ob modifier**, −1 aligned / +1 contradicting / +2 Church-Thread | what they are rewarded for | `factions_personal_v30.md:69`, roster at `:104–:365` | no |
| 4 | **Resonant Style** (4) | Evidence · Consequence · Authority · Solidarity | how they can be moved | `npc_behavior_v30.md` §1.3 `:32` | no |
| 5 | **Conviction Scar → crisis** | per-Conviction counter; 3+ → **d6 crisis table** | when they act unpredictably | `conviction_track_v1.md` §2 | **no** — `(Person, scar)` exists, nothing writes it |
| 6 | **Self-Other orientation** | scalar `[-1,+1]`, drift κ=0.03, attribution `raw × (1 − 0.5·max(0,orient))` | whose benefit | `conviction_taxonomy_v30.md` §3–§3.3 | no |
| 7 | **Belief** | revisable commitment; on revision becomes a Scar | the situated stance | `derived_stats_v30.md:216`; `npc_behavior_v30_infill.md:45` | field exists, unwritten |
| 8 | **Inspiration** | focus granting +1D / Ob −1 | engagement | `derived_stats_v30.md:217` | no |
| 9 | **stance rows** | `(referent, valence −5..+5, weight 0..5)` | opinion of a named other | `engine/season/decision/choose.py:77` | **yes — and no verb produces one** |
| 10 | **Truth** (ex-Certainty, ex-Piety Track) | 0–5 metaphysical stance; players see bands | cosmological position | `CURRENT.md` clocks row (ED-IN-0075) | not opened at its owner — see §6 |
| 11 | **Institutional Tendency** | faction default action | the fallback | `npc_behavior_v30.md:779` | no |
| 12 | **7-level faction priority tree** | **lexicographic, first-match-wins**; Survival overrides all | faction action | `npc_behavior_v30.md` §8.1 `:774` | no |
| 13 | **Second faction priority tree** | numbered `IF` ladder, different shape | faction action | `npc_behavior_v30.md:1108` — a **duplicate §7** | no |
| 14 | **Institutional Filter → Conviction Filter → Decision Fork** | 3-step procedure keyed on Scar count | named-NPC action | `npc_behavior_v30.md` §4.1 `:473` + infill `:54` | no |
| 15 | **Coherence thresholds** | 10–0 ladder, per-band decision rule | practitioner action | `npc_behavior_v30.md` §4.3 `:487` | no |
| 16 | **Dialogue Lattice five-filter chain** | 5 filters, personal↔personal | conversational action | `integration_proposal_v30.md:210` — named, not opened at its owner (§6) | no |
| 17 | **§F2 score** | **additive weighted sum**, 3 terms | the actual choice, today | `engine/season/decision/choose.py:302` | **yes — the only live one** |

**Seventeen mechanisms. Four are live. One decides anything.**

---

## §3 The measured condition of the canonical head

`npc_behavior_v30.md` is the head that owns the Stance Triangle, and it is in worse repair than its
`## Status: CANONICAL` line suggests. Four measurements, each reproducible:

**3.1 — 11 of 21 Conviction assignments name a retired Conviction.**
The head's own §1.2 `:30` declares: *"The legacy 9-Conviction set … is **superseded**. Reason and
Continuity are deprecated labels; Autonomy is renamed Liberty."* The same document then assigns
`Primary Conviction` / `Secondary Conviction` 21 times across its named-NPC tables. Counted by regex
over the head:

| name | assignments | in the canonical 13? |
|---|---:|---|
| Reason | 4 | **no — retired at `:30`** |
| Autonomy | 4 | **no — renamed Liberty at `:30`** |
| Continuity | 3 | **no — retired at `:30`** |
| Order | 3 | yes |
| Equity | 3 | yes |
| Faith | 2 | yes |
| Precedent | 2 | yes |

**52% of the head's own character sheets name a Conviction the head itself retires nine lines into
§1.** Edeyja, the Southernmost Warden-Chief, carries Primary `Continuity` and Secondary `Reason`
(`:212`, `:213`) — both retired. §4.3 `:487` then writes a live decision rule on one of them:
*"Continuity Conviction overrides personal safety."*

**3.2 — §1.1 has no body in the head** (§1 above).

**3.3 — §4.1's decision procedure is missing its Step 2 in the head.** It runs
`Step 1 — Institutional Filter` at `:477` straight to `Step 3 — Decision Fork` at `:480`. Step 2 —
*the Conviction Filter, the only step that consults Convictions at all* — is in the infill at `:54`,
along with a Step 4 the head never mentions. §4.2 `Non-Named NPC Behavior` is likewise a heading with
no body; its content (*"They have no Conviction, no Resonant Style, no Beliefs"*) is at infill `:57`.

**3.4 — Section numbers repeat.** §7 appears at `:742` and again at `:1108`; §11 at `:1080` and again
at `:1217`. The two §7s are different documents' worth of content.

---

## §4 Why this is a from-scratch job and not a patch

Three structural reasons. Each is independent; each alone would be sufficient.

### 4.1 Two incompatible decision architectures, both canonical

| | `npc_behavior_v30.md` §8.1 `:774` | `choose.py:302` |
|---|---|---|
| shape | **lexicographic** | **additive** |
| rule | first match wins; *"Survival … Overrides all"* | Σ of three terms, ranked |
| can survival be outvoted? | **no, by construction** | **yes** — a large enough alignment term outranks it |
| reactive behaviour | priority **6 of 7**, below four proactive tiers | no reactive term exists |

These are not two descriptions of one mechanism. A priority tree and a weighted sum disagree about
whether an override is possible, which is the whole question. Whichever survives, the other is
deleted rather than reconciled.

### 4.2 The vocabulary collides at the root

The seven Ethical Frameworks (`factions_personal_v30.md:104–:365`) are **Virtue · Faith ·
Categorical Imperative · Utility-driven Pragmatism · Moral Relativism · Equity Social Contract ·
Administrative Proceduralism**.

Four of those names — **Virtue, Faith, Utility, Equity** — are also Conviction names.

| word | as a Conviction | as an Ethical Framework |
|---|---|---|
| Faith | a weight in a person's own 13-vector | a faction-inherited **Ob modifier** |
| Virtue | " | " |
| Utility | " | " |
| Equity | " | " |

Different scale, different owner, different math, same word, one document apart. `CLAUDE.md` §4's
idempotency rule requires a later session to read a process word cold and land on the same meaning.
Here it cannot — and the ambiguity is not at the periphery, it is inside the Stance Triangle, whose
first two vertices are these two systems.

### 4.3 Five operator kinds were written as though they were one

This is why the pieces have never composed, and it is the deepest of the three.

| mechanism | is actually a… | acts on |
|---|---|---|
| Conviction / axes | **weight** | the ranking of candidates |
| Ethical Framework | **modifier** | the difficulty of a candidate |
| office · remit · eligibility · caste | **gate** | whether a candidate exists at all |
| priority tree · ambition | **generator** (+ override) | which candidates are proposed |
| Resonant Style | **susceptibility** | *other people's* actions toward this character |

A weight, a modifier, a gate, a generator and a susceptibility. Prior work — and this session's own
first attempt — repeatedly tried to merge them into one basis and then measured whether the basis
was any good. That measurement can only ever speak to row 1.

> ⚠ **THE SINGLE-WEIGHTED-SUM FRAME IS `choose.py`'s AND THIS SESSION'S. IT WAS NEVER THE BRIEF, AND
> A LATER SESSION MUST NOT READ IT AS ONE.** Jordan, 2026-09-16, verbatim: *"I didn't say this needed
> to be a clean weighted sum equalling 1. I expect this to include formulas and transformations and
> matrices and gates and so forth."* He said it before this census was written and repeated it while
> it was being written. The sum is what `engine/season/decision/choose.py:302` happens to implement
> and what this session reached for when it should have been sorting operators by kind. **A
> from-scratch decision layer is expected to be heterogeneous** — gates, matrices, transformations
> and thresholds composing, not one score. The five kinds above are the shape of that expectation,
> not a concession to it.

Note also that **Resonant Style is the odd one out in a way that matters**: it is not an input to
this character's decision at all. It describes what *works on them*. Filing it beside Conviction, as
a vertex of the same triangle, is a category error the from-scratch build should not inherit —
though the taxonomy itself is sound (§5).

---

## §5 What is worth keeping

Not everything in the pile is debris. Three things are load-bearing and well-made:

1. **The want / rewarded / moved distinction** (§1). It is the correct decomposition and it is
   already canon. The from-scratch build should adopt it explicitly rather than rediscover it.
2. **Resonant Style's four** — Evidence · Consequence · Authority · Solidarity
   (`npc_behavior_v30.md:32`). A closed, behaviour-derived basis defined by *what the character is
   vulnerable to*, with a stated reason per member (*"because their Conviction … claims to be
   reality-responsive"*). It independently reproduces the **Grounding Claim** column of the legacy
   nine at `conviction_track_v1.md:22` — *value is discovered through evidence / produced through
   results / revealed through authority / constituted through collective being*. Two documents,
   written apart, converging on the same four-way split is the strongest signal in the corpus.
3. **"What it dismisses"** (`conviction_track_v1.md:22`, fourth column). Faith dismisses *empirical
   contradiction*; Order dismisses *innovation, even beneficial*; Continuity dismisses *politics,
   ideology, anything that does not directly serve the ongoing task*. This is the reactive half in
   its sharpest form — it predicts what a character **refuses to hear** — and it is the natural
   producer for a Scar, which is the write nothing currently performs.

---

## §6 What this census does not establish

Stated so that no later session mistakes a gap for a null result.

- **Row 10 (Truth) and row 16 (Dialogue Lattice) were not opened at their owning documents.** Truth
  is characterised from `CURRENT.md`'s clocks row; the Dialogue Lattice from a description in
  `integration_proposal_v30.md`. Both rows are therefore weaker evidence than the rest of the table
  and should be re-read before either is relied on.
- **No claim is made that the seventeen are exhaustive.** The census covers what a targeted sweep
  found. A mechanism nobody named is a mechanism this table misses.
- **No claim is made about which mechanism is correct.** §4.1 says two architectures conflict; it
  does not say which to keep. That is a live design choice.
- **The `## Status:` lines are not evidence** (§0.05). `npc_behavior_v30.md` reads CANONICAL and
  §3 measures its condition; the two are compatible because a status line is reference.

---

## §7 Falsifiers

Per `CLAUDE.md` §0.1 pt 3, each load-bearing claim with the observation that would show it wrong.

| claim | falsifier |
|---|---|
| §1 — the head's §1.1 has no body | `sed -n '16,23p' systems/npcs/reference/npc_behavior_v30.md`. A body appears → claim is wrong. |
| §3.1 — 11 of 21 assignments are retired | the regex in this file's §3.1, re-run over the head. A different count → claim is wrong. |
| §3.3 — §4.1's Step 2 is absent from the head | `sed -n '473,516p' … \| grep -n "Step "` — **scoped to §4.1, and the scoping is load-bearing.** A bare `grep -n "Step 2"` over the head hits `:993`, an unrelated *"Step 2 — Approach"* in §9.5's recruitment procedure, and would have falsely cleared this claim. Run as scoped it returns Step 1 and Step 3 only. |
| §4.1 — the two architectures conflict | find a reading on which a lexicographic override and an additive sum agree about whether Survival can be outranked. |
| §4.2 — four names collide | `grep -n "^\*\*Ethical Framework" systems/factions/reference/factions_personal_v30.md` against the roster at `descriptor_registry.yaml:conviction_roster`. |
| §2 row 17 — §F2 is the only live decider | rebind or delete the other sixteen and observe a season run change. Nothing else is called. |
| §2 row 2 — the axis roster is blocking | **RUN 2026-09-16, not reasoned.** A `Key` built with `symbolic_dimensions={"traditional": 0.5}` appends; the same Key with `{"equity": 0.5}` raises `KeyValidationError: key 'k1' uses non-canonical axis 'equity' (§2.3 invariant 6)`. One of the seven axes under discussion is **rejected at Key emission today.** |

**One defect found while compiling this and not yet fixed:** `engine/substrate/keys.py:59` and
`engine/season/rosters.yaml: conviction_axes.values` are two independently hardcoded copies of the
axis roster. `rosters.yaml`'s own note claims *"a fifth axis or a rename is one edit there and a
loader refusal here"* — **there is no refusal.** `CONVICTION_AXES = roster("conviction_axes")`
(`engine/season/data/rosters.py:219`) never reads the substrate tuple, and no test compares them.
They agree today by coincidence. This is load-bearing on the game (row 2 is blocking at Key
emission) and it will fire on the first axis-roster change — which is the work this proposal exists
to prepare. One assertion closes it.
