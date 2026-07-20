# Player Interaction Walkthrough v1 — Social Contest (first draft, working document)

**Status:** DRAFT — an audit/design working document, not yet canon. Produced 2026-07-01 as the seed
artifact for the Stage 6 "Player Interaction Model" deliverable (see the amended staged plan). Grounds
every UI beat in a primitive already established (Stage 1/1d) so this is a concrete spec, not a promise.

**Why this exists.** Everything built so far (wrapper, kernel, primitives, trackers) answers "does the
resolver work?" Nothing yet answers "what does the player actually see and do?" — and this system has
**no GM** (CLAUDE.md: "the engine resolves everything"). Every "GM setup" step in the v30 prose (adjudicator
type, venue, stakes) must become something the engine PRESENTS to the player, not something a human
narrates. This walkthrough is the first attempt to make that concrete, exchange by exchange, for the
one game that is fully built (Agôn/Formal Contest) — with explicit notes on how the other three games
(Stage 4) would diverge in interaction shape, so their design doesn't accidentally converge onto one UI.

---

## 0. Design principle this walkthrough enforces

**Every number the resolver uses to decide the outcome is a number the player can see before they commit
to a choice that depends on it.** This is the direct answer to the stated core pain (opacity): not "hide
less," but "the hidden-GM-ledger and the player-facing screen are the same data, rendered." Where the
*resolved value* is legitimately hidden (an NPC's exact Conviction vector, an opponent's Face total), the
player still gets the *consequence class* (an Appraise hint, a visible debuff icon) — per the existing
lens taxonomy's playability rule: "is every consequence surfaced even when a number is hidden?"

---

## 1. SETUP — before the first exchange

**Screen: Contest Framing.**

The player is shown, before committing to the contest:

| Shown | Source primitive |
|---|---|
| **Venue** ("Formal Contest — 3 exchanges") | `venues.py` `Venue` dataclass (Stage 2): exchange_count, role_structure |
| **Adjudicator type** ("Crowd — swayed by delivery and force") | `adjudicators.py` `Adjudicator` (Stage 2); determines primary attribute |
| **Your pool** ("Argue Pool: 8D — Charisma×2 + History") | `build_argue_pool` (wrapper.py `build_contest` adapter) |
| **Stakes, both directions** ("Win: the Council grants the concession (Domain Echo). Lose: Contest Fatigue. Draw: scheduled to reconvene next season.") | §6 Post-Contest Resolution table, surfaced BEFORE the roll, not after |
| **Starting Persuasion Track position + bands** (a 0–10 meter, already drawn with its zones: ≤1 Total Defeat / ≤3 Decisive Loss / 4–6 Compromise / ≥7 Decisive Win / ≥9 Total Victory) | `PersuasionTrack` win-condition (groundup, promoted Stage 1) |
| **Any Appraise-derived hints already banked** ("You sense the Council favors precedent over speculation") | prior Appraise actions this scene, per `params/contest.md §Pools` degree-of-success ladder |

This screen is the direct translation of v30 §2 "GM Setup" — every step in that GM checklist becomes a
row the engine renders, confirming the **GM-removal mandate** is satisfiable, not just declared.

---

## 2. THE EXCHANGE LOOP — repeated `exchange_count` times

### Step 1 — Appraise (optional, costs the exchange's setup beat)

The player may spend this beat reading the room instead of arguing. Attunement+Recall pool, TN 7,
resolved with a visible die-pool animation (or its Godot-mode statistical equivalent). Outcome maps
directly to the existing 4-band ladder (`params/contest.md §Pools`, PP-614/ED-893):

| Roll degree | What the player sees |
|---|---|
| Failure (0) | A **misleading** hint (deliberately wrong — this is a real cost of a bad Appraise, not a null result) |
| Partial (1) | "They lean toward **directness**" (orientation revealed, genre not) |
| Success (2) | "They favor **Precedent**" (full style revealed) |
| Overwhelming (3+) | Style + one concrete detail (a cited Belief, the numeric resistance, an emotional tell) |

This is the primary in-fiction, player-actioned counter to opacity: information is *earned through play*,
not granted by the UI or withheld by a GM's mood.

### Step 2 — Style choice (the core tactical decision)

Four cards, not a dropdown — each should read as a distinct rhetorical move, not a stat combo:

| Card | = Genre × Orientation | Grounding (must be behaviorally true, not flavor-only — Lens 6) |
|---|---|---|
| **Precedent** | Memory × Revealing | Aristotle logos: cite settled fact openly |
| **Suppression** | Memory × Obscuring | bury inconvenient precedent |
| **Vision** | Projection × Revealing | argue openly for a future outcome |
| **Insinuation** | Projection × Obscuring | imply unstated future consequence |

Each card shows, before the player commits: the die pool it will roll, any active faction/adjudicator
boost it is known (via Appraise) to hit or miss, and — once Stage 3's armature lands — a rough read of
"this adjudicator tends to reward [X]" so the choice is a real bet, not a guess in the dark.

### Step 3 — Roll & resolve (the transparency moment)

This is where the opacity fix is load-bearing, not decorative. The screen shows, in order:

1. Both pools rolled (or their continuous-engine equivalent), successes tallied.
2. The **interaction type**, computed and *named in plain language*, not left as an internal enum:
   - CLASH → "**Direct Clash**" (same genre, opposite orientation — margin vs. resistance)
   - REINFORCE → "**Mutual Reinforcement**" (same genre, same orientation)
   - CROSS → "**Talking Past Each Other**" (different genres — independent evaluation)
   - TIE → "**Deadlocked**" (first-to-speak advantage moves)
3. The **margin** and the **resistance** it was compared against (resistance shown as a number, not a
   hidden threshold the player has to infer from outcomes).
4. The **Persuasion Track meter animates** — the player watches the same number the resolver used to
   decide the contest move, live, in the band-colored meter set up in §1.
5. A **Doubt Marker** icon appears on whichever side just won an Obscuring exchange (visible debuff, not
   a hidden flag the player only learns about when it fires later).

### Step 4 — Resource feedback (Face / Concentration, visible at all times, not just on threshold)

Two persistent bars, not a single hidden "stamina" number:

- **Concentration** (3×Focus + 2×Spirit, 5–35): depletes −5/exchange, −5 more on a loss. At 0: a
  **Spent** banner fires immediately with the exact penalty text ("−2D next exchange, opponent +1D").
- **Face** (per the Gate-A-ratified formula — a Charisma×3 ceiling with position tracked by the
  in-contest Standing primitive): shown as a bar *within* its Charisma-derived ceiling, so a
  high-Charisma character visibly has a bigger buffer, and the current fill visibly reflects how the
  contest is going, not a hidden roll. At the Rattled threshold: a Rattled-mark icon appears with its
  exact mechanical cost (−1D Argue, cumulative).

### Step 5 — Forfeit / Regroup (only offered when it is a live choice)

If Concentration is low enough that Regroup is meaningfully on the table, the engine offers it as an
explicit button with both branches' consequences shown side by side (continue vs. regroup), not buried
in a rules footnote the player has to already know.

---

## 3. RESOLUTION — after the last exchange

One screen, not a wall of dice logs:

- **Headline outcome banner**, mapped directly off the final Persuasion Track position (Decisive
  Win/Loss, Compromise, Total Victory/Defeat) — the same bands the player watched all contest.
- **Every consequence enumerated explicitly**, each traceable to the Key the engine actually emitted
  (this is the same seam as Stage 5's Key-bus closure — replay-determinism and player-legibility are
  the *same fix* viewed from two sides):
  - Obligation created → its exact terms, duration, and violation-consequence shown in full, not just
    "an Obligation was created."
  - Domain Echo → what it actually grants (Mandate shift / next Domain Action bonus) and where.
  - Conviction Scar → the existing canon design (narrative signal, no stat reveal) is correct as-is and
    should NOT be over-exposed here — a subtle visual cue on the NPC, consistent with `§6.2 ED-1042`.
  - Contest Fatigue / Chain Contest scheduling, if applicable, shown with the concrete next-session
    trigger, not just a flag.

---

## 4. How the OTHER THREE GAMES (Stage 4) would diverge — so Stage 2–4 don't lock in an Agôn-only UI

The one governing constraint carried forward: **the resolved value is always the visible value.** Beyond
that, each game's interaction shape should look and feel different, or they are not four games (Lens 1):

- **Negotiation (ZOPA)** — replace the single Persuasion Track meter with a **two-sided offer panel**
  (each side's BATNA range shown as a bracket, not a point; a live "zone of possible agreement" overlay
  once both sides' offers are visible enough to imply one) — a bargaining table, not a tug-of-war bar.
- **Inquiry (truth)** — replace the win/lose banner with a **belief-alignment meter** per contested
  proposition (which side the emerging evidence currently favors), closer to a shared whiteboard than a
  contest track — the "win" condition is convergence, not domination.
- **Consensus (holdout)** — replace the two-party track with a **per-assenter roster** (a row per NPC/
  faction in the room, each flipping from undecided → assenting as the argument lands), with a visible
  holdout counter and the frivolous-block cost shown live if the player is tempted to stall.

This section exists so that when Stage 4 fans out the four games, each agonist inherits "this must look
and play differently from Agôn," not just "this must resolve differently."

---

## 5. Open questions this walkthrough surfaces (not resolved here — flagged for the relevant later gate)

- **Style-card flavor text** needs to be authored once (Stage 2/3), not per-implementation — it is the
  single highest-leverage legibility surface (four buttons the player sees every single exchange).
- **Adjudicator-preference visibility** (Stage 3's armature) needs a UI answer, not just a resolver
  answer: how much of the `armature_position` dot-product should Appraise be able to reveal, and how much
  should stay genuinely hidden (an adjudicator with unknown convictions is a legitimate source of
  tension, not an opacity bug — this is the one place "hidden" is correct, and the antagonist should
  distinguish it from an opacity finding).
- **Godot vs. tabletop rendering** — this walkthrough is written screen-agnostic (it should read
  correctly whether "screen" means a Godot UI panel or a physically-laid-out TTRPG table); the eventual
  Godot port (CLAUDE.md §6, still Gate-0-blocked) will need to choose concrete widgets, but the
  information contract above should not change when it does.
