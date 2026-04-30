<!-- [PROVISIONAL: 2026-04-29 — terminology conversion workplan, pre-Jordan-approval] -->
<!-- STATUS: PROVISIONAL — workplan proposal, not canonical until decisions §4 are resolved and PP-675 promotes -->
<!-- AUTHORITY: PP-675, ED-759 -->

# Terminology Conversion Workplan — TTRPG / Hybrid / BG → Videogame

**Date:** 2026-04-29
**Status:** PROVISIONAL
**Scope:** Eliminate framing terminology that asserts Valoria is a tabletop or board game product. Preserve mechanical vocabulary (dice pools, TN, Ob, exchange, degree of success).
**Source:** Jordan directive 2026-04-29.
**Related:** PP-675, ED-759.

---

## §0 Why this is a Class A change, not a rename

The headline rename is cosmetic. The load-bearing architectural change is **retiring "Hybrid" as a third mode of play**. `scale_transitions_v30.md §6` canonizes a three-mode model (TTRPG · BG · Hybrid) where Hybrid is treated as a distinct mode with its own transition procedures (§6.1, §6.2, §6.3). In a pure videogame, "Hybrid" was never a mode — it was always Strategic Mode paused for one Scene, then Strategic Mode resumed. The third-mode framing was a tabletop-publishing accommodation: a way of telling players "you can run this at a table, around a board, or both at once."

A videogame-only Valoria has two modes — **Strategic Mode** (peninsula map, seasons advancing, Domain Actions resolving, clocks ticking) and **Scene Mode** (one zoomed-in scene resolving). The verb that connects them is **Zoom-In**. Hybrid as a noun ceases to exist.

This is the only change in the workplan that touches game architecture. Everything else is vocabulary substitution. The two are bundled because they cannot be done independently — the vocabulary substitution requires the structural change to land first, otherwise the renamed sections still describe a three-mode architecture.

---

## §1 N — Necessity case

| N question | Answer |
|---|---|
| What Renaissance-era political dynamic does this model? | None — meta-framework, not gameplay. The change *removes* a non-Renaissance abstraction (Hybrid mode as a third register) and aligns vocabulary with what the videogame actually is |
| Already covered by existing mechanics? | Hybrid mode is fully covered by Strategic + Zoom-In (Scene). No mechanical content is lost |
| Different player situations? | Player situations are unchanged — same scenes, same strategic actions. Only the framing vocabulary changes |
| Load-bearing in subject? | N/A — this is meta-framework cleanup, not a new mechanic |
| What's lost by abstracting? | Nothing. The abstraction being removed is the tabletop framing, which has no Renaissance-political-leadership content |

**N verdict: pass** — meta-framework cleanup, not gameplay addition. Same self-exempting pattern as PP-674.

---

## §2 Vocabulary canon

### 2.1 Retire entirely (framing terms)

| Legacy | Status | Replacement |
|---|---|---|
| TTRPG, tabletop, pen-and-paper | RETIRE | **Scene Mode** |
| BG, board game, BG mode, BG layer | RETIRE | **Strategic Mode** |
| Hybrid mode | RETIRE (noun + mode concept) | replaced by **Zoom-In** as event/verb |
| GM, Game Master, referee, narrator | RETIRE | "the engine" if a referent is needed |
| at the table, the group, players around the table | RETIRE | "in play" or "during a scene" |
| session (TTRPG-evening sense) | RETIRE | **Scene** or **Scene chain** (context-dependent) |
| session boundary (sense: TTRPG session-end) | RETIRE | **Season tick** |
| card-hand economy, card hand (tabletop metaphor) | RETIRE | **Action slot system** |
| draw / discard (tabletop metaphor sense) | RETIRE | **allocate / consume** |
| Adjudicator (TTRPG-flavored sense in social contests) | DECISION § 4.4 | Resolver, or keep |

### 2.2 Preserve (mechanical vocabulary)

These are tabletop-derived but are valid videogame engine terms. **Keep:**

dice pool · die · D (e.g. "+2D") · TN · Ob · exchange · round · turn · degree of success · clash · cross · reinforce · tie · pool formula language (`(Stat × 2) + H + 3`) · contest · action · phase · tick · Wound · Stamina · Fibonacci scaling.

### 2.3 Context-sensitive — disambiguate before automation

- **session** has three meanings in the codebase: (a) TTRPG-evening — RETIRE; (b) `valoria_hooks.py` "session token" / "active session" — KEEP (engineering term); (c) "play session" in user-facing UI strings — KEEP.
- **card** has two meanings: (a) tabletop hand metaphor for action selection — RETIRE; (b) literal videogame UI element (Tensions Deck cards, action cards on the slate) — KEEP. Disambiguate by surrounding nouns.
- **draw** has two meanings: (a) tabletop "draw a card" metaphor — RETIRE; (b) literal Tensions Deck UI ("draw 1 at game start") — KEEP only when referring to that exact UI affordance.

---

## §3 Architectural change: retire Hybrid as a mode

### 3.1 Current canonical model (`scale_transitions_v30 §1, §6`)

Three modes: **TTRPG** (full-scene resolution) · **BG** (peninsula clocks, Domain Actions) · **Hybrid** (BG paused mid-game while one scene resolves, then BG resumes). Three transition procedures: TTRPG → BG (§6.1) · BG → Hybrid (§6.2) · Hybrid → TTRPG (§6.3).

### 3.2 Replacement model

Two modes: **Strategic Mode** · **Scene Mode**. One transition verb: **Zoom-In** (Strategic → Scene) and **Zoom-Out** (Scene → Strategic). The "Hybrid" experience — a scene popping out of a strategic turn — becomes simply *the player Zooming-In during a strategic turn*, and Zooming-Out resumes the strategic turn. This is what the experience always was; the third-mode framing added a phantom layer.

### 3.3 What this affects

- `scale_transitions_v30.md` §1 (mode model) and §6 (transition procedures) — structural rewrite, not search-replace
- All cross-referencing docs that name "Hybrid mode" — scope inventory in §5.1
- `params/scale_transitions.md` — params file mirrors design doc, mirror change required
- `valoria_hooks.py` mode constants if any (audit needed)

### 3.4 What does NOT change

- The 8 handoff rules
- Sufficient Scope, Domain Echo, Coherence cost rules
- The Scene Slate, Zoom-In trigger taxonomy
- Any actual gameplay behavior

The change is structural-vocabulary only: the engine already runs on a binary Strategic/Scene state machine. The three-mode framing was textual, not implementation.

---

## §4 Decisions required from Jordan before propagation

| # | Decision | Recommended |
|---|---|---|
| 4.1 | "Strategic Mode" vs "Map Mode" vs other for BG | **Strategic Mode** — describes what happens (strategy at peninsula scale), not the UI surface |
| 4.2 | "Scene Mode" vs "Encounter Mode" vs other for TTRPG | **Scene Mode** — already used elsewhere as a noun; "Encounter" is D&D-flavored |
| 4.3 | Confirm Hybrid retired (3-mode → 2-mode + Zoom-In) | **Confirm** — the load-bearing change. Without this, the vocabulary substitution is incoherent |
| 4.4 | Adjudicator → Resolver, or keep | **Keep** — buried in mechanical math, low confusion risk; revisit only if it surfaces in player-facing UI |
| 4.5 | "session" policy | **RETIRE in TTRPG-evening sense; allowed for hooks engineering term ("session token") and for any user-facing "play session" UI string** |

---

## §5 Phased rollout

### Phase 0 — decisions locked
Jordan signs off on §4. Without §4.3 in particular, no propagation begins — converting headers to "Strategic Mode" while leaving the three-mode model in place produces a worse state than current.

### Phase 1 — terminology canon doc + ledger commitment
- Create `references/terminology_canon.md` — final mapping table, definitions of the new terms, one example sentence per term, deprecation notes
- Add to `references/canonical_sources.yaml` as authority
- Add to `valoria_hooks.py` as a forbidden-token list (Phase 4 enforcement)
- Patch register: this workplan committed as PP-675 PROVISIONAL → promoted to APPLIED only after Phase 4 lands

### Phase 2 — sweep inventory
- Repo-wide ripgrep for every legacy term, dump per-file occurrence counts to `references/terminology_sweep_inventory.md`
- Classify each occurrence: pure-replace · context-sensitive · cut · skip (archives, deprecated)
- Build replacement plan; flag every context-sensitive case for manual review

### Phase 3 — staged propagation by directory cluster
Order by stability so we don't rewrite work currently in flux:

1. `designs/architecture/` — most cross-referenced; structural rewrite of `scale_transitions_v30 §6` happens here
2. `references/` — vocabulary, indices, propagation maps
3. `params/` — mechanical specs (mostly clean; small sweep)
4. `designs/provincial/`, `designs/territory/`, `designs/scene/`
5. `designs/threadwork/`, `designs/world/`, `designs/npcs/`
6. `designs/arcs/` — narrative-flavored; manual review heavier
7. `canon/` (excluding `*_archive*`), `skills/`, `.github/`, project root files
8. `archives/`, `deprecated/` — **skip** (historical record)

After each cluster: skeleton-first re-fetch, spot-check that mechanical content survived intact, commit, decrement `propagation-pending` counter.

### Phase 4 — CI/hook enforcement
Add `terminology_gate` to `valoria_hooks.safe_commit`. Reject any commit that introduces legacy framing tokens in non-archive paths. Same `RuntimeError`-on-violation pattern as `vetting_gate`. Mirror in `.github/workflows/`. This makes the conversion permanent — entropy can't reintroduce the old vocabulary without an explicit override.

Forbidden token list (Phase 1 doc is the source of truth):
- exact: `TTRPG`, `tabletop`, `pen-and-paper`, `Game Master`, `Hybrid mode`, `Hybrid Mode`, `BG mode`, `BG Mode`, `BG layer`
- regex (case-insensitive, word-boundary): `\bGM\b` outside of code/tooling, `\bat the table\b`, `\bcard.?hand economy\b`

Allowlist for `session`, `card`, `draw` — only flagged when adjacent to retired-context indicators.

### Phase 5 — project-level cleanup
- Update the project knowledge instructions block (currently the single most contagious source of the old vocabulary)
- Update `valoria_hooks.py` and `github_ops.py` docstrings if they reference modes
- Update SKILL.md files in `skills/` if they reference modes
- Update the connections artifact's node descriptions (currently uses "Two-mode model" — already aligned, but verify)

---

## §6 Risks

- **`scale_transitions_v30 §6` is structural, not vocabulary.** A search-replace would produce gibberish ("Strategic Mode → Hybrid" is meaningless once Hybrid is gone). This section needs hand-rewriting as part of Phase 3 cluster 1.
- **`canonical_sources.yaml` at 4670/5000 tokens.** Adding the terminology canon entry pushes us closer to threshold. Pruning needs to happen at the same time or first.
- **In-flight session docs** (the `2026-04-28-political-dynamics-session/` cluster, `mass_battle_*_2026-04-29.md`) are full of `BG mode` / `TTRPG mode` references but are working documents. **Do not convert mid-session.** Defer until session close to avoid corrupting in-flight references.
- **PP-666 provisional docs** (settlement_adjacency_v30, fractional_province_ownership_v30, faction_succession_split_v30) are still PROVISIONAL. Cleaner to convert them as part of their canonical promotion, not as a separate sweep.
- **`Adjudicator`** in social contests is genuinely tabletop-flavored; if Jordan keeps it (recommended), document the decision so it doesn't get caught by future cleanups.
- **Audit trail.** Archive paths preserve the old vocabulary for historical accuracy. Document this exception explicitly so the enforcement hook doesn't trip on archive files.

---

## §7 Success criteria

- All non-archive docs use the new vocabulary
- `scale_transitions_v30 §1, §6` describes a two-mode + Zoom-In model
- `terminology_canon.md` is canonical authority
- `terminology_gate` rejects commits introducing legacy framing tokens
- `references/canonical_sources.yaml` lists `terminology_canon` as authority
- The session log at first message of every chat no longer reinforces TTRPG/BG/Hybrid framing
- A new contributor (or a Claude instance in a fresh chat) cannot accidentally regress because tooling rejects the regression

---

## §8 Vetting block

```yaml
vetting:
  class: A
  necessity: pass  # meta-framework cleanup; removes non-Renaissance abstraction (Hybrid as third mode); §1 N case
  omega: pass  # not a gameplay mechanic; supports Ω-readable framing by aligning vocabulary with the videogame the player actually plays
  mu: []  # meta-framework, doesn't directly serve any Μ mode
  m_ratings:
    M-1: "○"
    M-2: "○"
    M-3: "○"
    M-4: "○"
    M-5: "○"  # arguably "+" — clarifies cross-scale vocabulary, but indirect
    M-6: "○"
    M-7: "○"
    M-8: "○"
    M-9: "○"
    M-10: "○"
    M-11: "○"
  q: pass  # workplan structure: phased rollout with gates, decisions itemized, risks called out, enforcement spec'd
  note: "Self-exempting on Ω/Μ — meta-framework + vocabulary infrastructure, not gameplay mechanic. Same exemption pattern as PP-674. The single Class A gameplay-touching element (retiring Hybrid as a mode in scale_transitions_v30) is structural-vocabulary only: removes a textual abstraction, no behavior change."
```

---

## §9 Open items / next session

This workplan is a **proposal**. Before any propagation begins:

1. Jordan resolves §4 decisions (5 items, recommended answers given)
2. PP-675 promotes from PROVISIONAL → APPLIED on Jordan signoff
3. Phase 1 begins: build `terminology_canon.md` and `terminology_sweep_inventory.md`

**Not in scope of this workplan:** retroactive conversion of archive directories. Archives preserve historical vocabulary by design.
