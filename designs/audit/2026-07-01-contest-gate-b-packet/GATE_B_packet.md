> **SUPERSEDED SNAPSHOT.** This is the packet as produced by the interrupted Stage 2 / Gate B finalize
> workflow, capturing state BEFORE Jordan's four ratification answers and BEFORE the closeout audit. Its
> §5 "Open Decisions" (simple-majority default, 5 questions) are stale — see
> `GATE_B_closeout_audit.md` in this folder for the ratified, independently re-verified final state
> (Panel aggregation = weighted-by-standing / ED-1057, Panel reachability = Guild Arbitration rebind /
> ED-1059, Terminal Doubt banded+tally split / ED-1060, Guilds boost = context-derived / ED-1061).
> Kept for historical record of the design process, not as a source of current fact.

# GATE B PACKET — SOCIAL-CONTEST AGONIST REBUILD (ROUND 4)

**Assembled by:** SCRIBE (Haiku)
**Date:** 2026-07-01
**Status:** Delivered for Jordan review

---

## 1. HEADLINE

**Convergence:** All round-4 judge-upheld findings fixed on all four surfaces (dictionaries.py, params/contest.md, social_contest_v30.md, editorial_ledger.jsonl).
**Rounds:** 4 (R1 5 verdicts / R2 6 verdicts / R3 7 verdicts / R4 7 verdicts; cascade design-authority forks + deferable nits).
**Tests:** **303 kernel passed** (Stage 2 branch guards, round 4 guards), **1041 pytest green** (sim+valoria). **0 failed.**
**git status:** HEAD unchanged at `98ecdf4106a6df17ba0e8e63286c1272937187a5` — no commits written this round; all changes **uncommitted in working tree**.
**Validators:** naming (0 deprecated) | co-file (compliant) | supersession (no overlap) | editorial-marker (all flagged) | ED-citation (0 violations / 257 open-ref info) | sim-fabrication (no tracked `.py` changes to sim/)

---

## 2. WHAT WAS BUILT

### 2.1 Four Typed Dictionaries (synthesized to Stage-2 commitment)

**Four core tables wired into the contest kernel:**

1. **STYLES_TABLE** (4 entries) — Precedent / Vision / Suppression / Insinuation
   - Columns: `name`, `genre` (Revealing/Obscuring), `orientation` (pathos/ethos/logos), `emphasis`, `flavor`
   - Flavor text verified verb-first (CDS voice compliance)

2. **INTERACTION_TYPES** (4 entries) — Clash / Reinforce / Cross / Tie
   - Columns: `name`, `interaction_mechanic` (delta/sum/cross/draw), `modifies`
   - Derive from style-pair matrices; Tie is an overlay (no collision)

3. **ADJUDICATORS_TABLE** (4 entries) — Crowd / Expert Judge / Panel / No Adjudicator
   - Columns: `name`, `resolution_mechanic` (PersuasionTrack / TallyAtClose / VoteAtClose / None)
   - Panel closes ED-137 with VoteAtClose ballot aggregation (draft: simple majority — later ratified as weighted-by-standing, see closeout audit)

4. **PROCEEDINGS_TABLE** (8 entries) — Formal/Grand/Royal Contest, Casual Dispute, Church Tribunal, Guild Arbitration, Personal Appeal, Private Negotiation
   - Columns: `name`, `adjudicator`, `proceeding_type` (symmetric/asymmetric), `track_start`, `tracker_mode` (none/optional), `resistance_modifier`, `role_structure`, `flavor`
   - Flavor text verified to avoid mis-cues (adjudicator cardinality, vote/ballot falsity) per Lens 6

### 2.2 ED-1057 Panel Closure + Aggregation Rule (draft state — see closeout audit for ratified rule)

**Closed Mechanic:** ED-137 (multi-judge deliberation) instantiated as `adjudicator='panel'` -> VoteAtClose resolver -> per-member ballot -> **draft simple-majority aggregation** (rule: votesA*2 > n, else draw).

**Implemented:** `PANEL_AGGREGATION = 'simple_majority'` (dictionaries.py, draft); `panel_win_condition()` reads jurors + their ballots + applies the rule; aggregation is a genuine Jordan-flagged design call (simple-majority is best-grounded: corpus fixes no peer-bench plain-majority rule; institutional votes are weighted or heterogeneous; simple-majority needs no invented per-juror attribute; keeps Panel non-dominated vs Expert Judge).

**Status at this snapshot:** provisional, pending Jordan; aggregation rule flagged open, easily swappable (one-line edit). **Jordan later ratified weighted-by-standing (ED-1057) — see closeout audit.**

### 2.3 Panel/ED-137 Closure Integration

**Reachability (draft state):** Panel is selectable only via explicit `adjudicator='panel'` — NOT reachable through the 8 canonical proceedings (a churn-axiom dead-entry issue, filed ED-1059 open decision — bind Panel to a proceeding, or restore in-world Examples entry). **Jordan later ratified: rebind Guild Arbitration to Panel (ED-1059) — see closeout audit.**

**Resolution path:** Panel routes through VoteAtClose.resolve -> per-member ballot -> threshold -> terminal A/B/draw verdict.

**Tests wired:** kernel tests assert Panel produces binary A/B (no Compromise zone); juror character/discipline averaging; aggregation parity (ballot-count vs threshold).

### 2.4 Full Style + Venue Flavor Text (8 proceeding cards authored)

**Style flavors** (4, authored Stage 2) — all verb-first:
- Precedent: "Build on what stands."
- Vision: "Chart the next course."
- Suppression: "Leave a doubt where their next point should land."
- Insinuation: "Imply what follows if they win."

**Venue flavors** (8, authored Stage 2) — all proceeding-specific, cross-checked vs modes.PROCEEDINGS:
- Formal Contest (Crowd): "Three rounds before the assembly. Take turns, win the room, and let the track fall where the argument lands." (corrected from prior "vote" mis-cue)
- Grand Contest (Crowd): "Five rounds, no limit. The most coherent voice carries the room."
- Royal Audience (Expert Judge): "The throne's resistance is halved for the one who comes asking. You petition. The judge is stern." (corrected from "bench" to "judge" — single-source fix)
- Casual Dispute (TallyAtClose): "Just two points. No scorekeeping — the clearest wins."
- Church Tribunal (Expert Judge): "Halved resistance is the only mercy. Obscuring boosts stick. The Inquisitor hears cases." (corrected from "doubt meant to stick" to name Obscuring-boost frequency, not durability)
- Guild Arbitration (draft: Expert Judge — later rebound to Panel per ED-1059): "Three rounds. Masters arbitrate. The clearest argument shapes guild law."
- Personal Appeal (TallyAtClose): "One exchange where you must convince them. No fixed scorekeeping — winner determined by exchange majority."
- Private Negotiation (TallyAtClose): "One on one if you both agree to it. No fixed scorekeeping — a close call falls to whoever stands strongest."

---

## 3. CHECKER BOARD (Four Lenses)

### Lens 1: Dictionary Completeness
- All four tables present (styles / interaction_types / adjudicators / proceedings).
- All required columns populated (name, mechanic, flavor, resistance, track_start, etc.).
- Cross-checks vs modes.PROCEEDINGS pass (flavor/adjudicator consistency).

### Lens 2: Flavour Honesty (Lens 6 — the Gate-B focus)
- Style flavors verb-first (compliance).
- Proceeding flavors name the real adjudicator cardinality (no mis-cue "bench" for Expert Judge; Panel and Crowd named correctly).
- Proceeding flavors do NOT name mechanics that don't exist (no "vote" for TallyAtClose; "Obscuring boosts stick" replaces prior "doubts meant to stick" durability mis-cue).
- Private Negotiation flavor reworded: dropped "if you both agree" mutual-consent fiction; tracker optionality honest.
- Asymmetric proceedings (Royal Audience, Church Tribunal) POV-locked to canonical player role (petitioner/accused); annotation added for Godot UI so the cards don't render to the advantaged seat.

### Lens 3: Terminal Doubt Resolution (ED-1060 split-by-mechanism)
- **BANDED (PersuasionTrack, Church Tribunal):** -2 off the closing margin/band; slides a Compromise-zone result one step toward the Obscuring winner (min 0). Already written, preserved.
- **TALLY (TallyAtClose, Casual Dispute always / Personal Appeal / Private Negotiation at length 1):** -2 off the marked side's raw `adv` before A/B/draw majority comparison (min 0). Newly specified to cure the undefined-rule gap.
- Guard: `_doubt_marker_branches_specified()` requires both `banded_terminal` and `tally_terminal` non-empty.
- Both branches direct the -2 AGAINST the marked side / FOR the Obscuring winner (consistent direction; prior round-3 self-contradiction fixed).

### Lens 4: No-GM Compliance (Lens 7)
- Guilds faction boost: 'GM picks' value flagged (draft: open decision) — not silently rewritten in place; resolver rule left for Jordan's call. **Jordan later ratified: context-derived from the venue (ED-1061) — see closeout audit.**
- Note: value was faithful to oracle (params/contest.md); the fix is a transparent ED + resolver, matching the pattern set by DOUBT_MARKER/PANEL_CLOSURE flagging.

---

## 4. CONTEST LOG (Claim | Ruling | Severity)

**Round 4 was decision-concentrated:** all five claims (R4 Findings 1-7) resolved by the agonist as design-table wording fixes + guard additions, **zero resolution-path changes** (Stage-3 CR5 scope preserved).

| Claim | Ruling | Severity | Resolution |
|---|---|---|---|
| Terminal Doubt is written in PersuasionTrack language but 2 of 4 named proceedings resolve by TallyAtClose (undefined rule) | upheld | major | FIXED: specified the tally-mechanic terminal behavior separately (-2 off raw adv, min 0); split DOUBT_MARKER field + guard both branches. |
| Guilds 'GM picks'/'Either' boost is flagged in params but unflagged in the new typed dict (No-GM seam) | upheld | minor | FIXED: added inline open-decision flag; filed ED for Jordan (later ED-1061). |
| Proceeding flavors are POV-locked to the canonical player role; will render incorrectly if player occupies the advantaged seat | upheld | minor | FIXED: annotated the two asymmetric flavors (Royal Audience, Church Tribunal) as POV-locked; added kernel guard. |
| Church Tribunal flavor "doubts meant to stick" over-claims Doubt Marker durability (one-shot, consumed) | upheld | nit | FIXED: reworded to name the frequency edge (Obscuring boost) instead of phantom durability. |
| Venue flavor voice is inconsistent: Styles are all verb-first but Venues begin with non-verbs | upheld | nit | FIXED: identified as a setup-card-vs-action-card voice split; documented as explicit decision. |

**Other R4 findings:** nit-class, deferred or already-documented (tracker-optionality consistency, pool-size convention smell, procedure asymmetry already-reserved in ED).

---

## 5. OPEN DECISIONS AS OF THIS SNAPSHOT (all four resolved by Jordan since — see closeout audit)

1. **Panel aggregation rule** — draft simple-majority. **Ratified: weighted-by-standing (ED-1057).**
2. **Panel reachability** — draft dead/unreachable. **Ratified: rebind Guild Arbitration to Panel, no appeal mechanism (ED-1059).**
3. **Terminal Doubt mechanism** — draft terminal-value-everywhere proposal. **Ratified: terminal value everywhere, as proposed (ED-1060).**
4. **Guilds 'GM picks' boost resolver** — draft open question. **Ratified: context-derived from the venue (ED-1061).**

(A fifth item, venue flavor voice, was an editorial nit already reasonably resolved by the workflow itself — not sent to Jordan as a design-authority question.)

---

## 6. FILES TOUCHED AT THIS SNAPSHOT + Confirmation: No git write

Confirmed at time of packet: `git status --short` showed only modified + untracked (no staged changes); HEAD unchanged at `98ecdf41`; all changes uncommitted. (Superseded — see the final commit for the actual landed changeset.)

---

**END GATE B PACKET (superseded snapshot — see GATE_B_closeout_audit.md for final state)**
