# VALORIA — UI/UX Comprehensive Reference v4
## Godot-development-ready interface specification

**Date:** 2026-04-16
**Supersedes:** valoria_ui_proposal_v3.md (earlier today)
**Status:** CANONICAL — approved for development reference with editorial permission to resolve UI-01 through UI-15
**Scope:** every interface surface the player encounters, from first boot through Rupture or Victory
**Dependencies:** all 19 v30 canonical design documents + combat_v30 ED-548 Wound patch (applied in-session)
**Resolves:** ED-544 (P-03 videogame rendering model), ED-545 (Zoom In triggers expanded via Scene Slate), UI-01 through UI-15 (resolved inline)
**New editorial items introduced:** none — this document resolves, does not defer

---

# HOW THIS DOCUMENT WORKS

This is the reference specification. It is read two ways:

- **Linearly by designers** working through the player experience end-to-end. Parts 0–22 flow as one argument: the game is constituted by mutual couplings between factions, settlements, NPCs, and the player; the interface's sole purpose is to render those couplings legibly without collapsing them into numbers.
- **Non-linearly by Godot developers** needing the spec for one screen or one system. Every part is self-contained with explicit inputs, outputs, state transitions, and asset manifests. Cross-references use `§N.N` notation — search the document for the numeral.

Each part has:
1. **Authoritative sources** — which v30 files govern the mechanics rendered here
2. **What the player sees** — the surface description
3. **Why it is that way** — the design argument grounded in mechanics
4. **How it is built** — Godot-facing implementation notes (data shape, state flow, asset calls)

When a section says "resolved UI-N," it means one of the v3 open items is closed in this document. The resolution is marked `[RESOLVES UI-N]` inline.

---

# TABLE OF CONTENTS

- **Part 0** — Three design oaths (the constraints that bind every screen)
- **Part 1** — The full state machine (what mode the game is in, when, and why)
- **Part 2** — The persistent chrome (every element always on screen)
- **Part 3** — Travel and zoom (movement between layers)
- **Part 4** — Fieldwork (exploration, investigation, socialising)
- **Part 5** — Dialogue as Disco-Elysium Conviction interface
- **Part 6** — Social contest (Parliament, Tribunal, Royal Audience, Grand Contest)
- **Part 7** — Personal combat
- **Part 8** — Mass combat and settlement invasion
- **Part 9** — Threadwork (the felt radicality)
- **Part 10** — The integrated loop (fieldwork → investigation → contest → combat → fieldwork)
- **Part 11** — National-level faction management
- **Part 12** — Settlement management
- **Part 13** — Character management
- **Part 14** — Party management
- **Part 15** — Parliament interface
- **Part 16** — Inquisition Hearing interface
- **Part 17** — Treaty negotiation and Grand Debate
- **Part 18** — The Clock Column and substrate state
- **Part 19** — The cutscene system (Triangle Strategy / Final Fantasy Tactics register)
- **Part 20** — The feel layers (ambient, cue, haptic-equivalent, threadwork-radical)
- **Part 21** — The Codex, Journal, Accounting Scroll, and supplementary screens
- **Part 22** — Accessibility, input, and resolution scaling
- **Part 23** — Precedent attribution (every borrowing, named)
- **Part 24** — Godot implementation reference (scene tree, signals, assets)
- **Part 25** — Resolved items index (UI-01 through UI-15, all resolutions)

---

# PART 0 — THREE DESIGN OATHS

Before anything: three non-negotiables that override all other considerations.

**Oath I — The world is always present.** The peninsula, the clocks, the factions, the Scene Slate — all persist visually whether the player is on the Peninsula map, inside a settlement, or in a combat hex grid. Zoom in does not hide the world. The player sees the layer they are in AND a compressed version of the layers above. The Codex is always one button away. No screen is modal except cutscenes (§19) and a narrow set of commit-confirmations (Conviction violations, permanent decisions).

**Oath II — Transparency is not over-explanation.** Every number the player needs to plan with is visible. Every number they do not need is hidden but inspectable on hover. The UI never says "Your action succeeded" when it can say "Your action rolled 14 dice against Ob 2, produced 8 net successes, and triggered Domain Echo on Crown Mandate +1." But it also never surfaces faction stat values as raw numbers by default — band names first, numbers on hover. Transparency serves comprehension; opacity serves mood. Balance is screen-by-screen.

**Oath III — The game is felt, not narrated.** When a faction Mandate changes, you see its banners change, you hear its musical motif shift, you feel the color temperature of its territories drift, and only then do you see the number. When a Conviction scars, the screen briefly warps — a flicker, not a notification box. When threadwork fires at structural scale, everything changes — audio, palette, the shape of the UI itself. The game does not tell the player that something happened. It shows them, then annotates if annotation is needed. Cutscenes (§19) are the high end of this principle; ambient cues (§20) are the low end.

---

# PART 1 — THE FULL STATE MACHINE

Authoritative sources: player_agency_v30 §7.2, board_game_v30 §9.1 + §9.8, faction_layer_v30 §7, scale_transitions_v30 §4, §6, companion_specification_v30 §4.3.

## §1.1 Top-level states and allowed transitions

The game is always in exactly one of 14 states. The state machine is deterministic — every transition is either player-initiated (labeled P) or game-initiated (labeled G). No state is dwelt-in ambiguously.

```
            ┌─────────────────────────────────────────────────────────┐
            │                   [MAIN MENU]                            │
            │         New Campaign · Continue · Codex · Settings       │
            └──────────────┬──────────────────────────────────────────┘
                           │ P: New Campaign
                           ▼
            ┌─────────────────────────────────────────────────────────┐
            │              [CHARACTER CREATION]                        │
            │   Attributes → Histories → Faction → Convictions (3)     │
            └──────────────┬──────────────────────────────────────────┘
                           │ G: Create complete → Season 1 opens
                           ▼
   ╔═══════════════════════════════════════════════════════════════════╗
   ║                        SEASON LOOP                                 ║
   ║                                                                    ║
   ║   [PHASE 0: BRIEFING]  cinematic, ~30s                             ║
   ║        │ G: auto-advance                                           ║
   ║        ▼                                                           ║
   ║   [PHASE 1a: DUTY ASSIGNMENT]  scripted dialogue scene             ║
   ║        │ G: duty accepted or negotiated (Counselor+)               ║
   ║        ▼                                                           ║
   ║   [PHASE 1b: SLATE REVEAL]  Slate animates in                      ║
   ║        │ G: auto → Phase 1c                                        ║
   ║        ▼                                                           ║
   ║   ┌──► [PHASE 1c: PERSONAL PHASE]  PLAYER-DRIVEN                   ║
   ║   │       │                                                        ║
   ║   │       ├── P: select Slate entry ────────┐                      ║
   ║   │       │                                  ▼                      ║
   ║   │       │                ┌────────────────────────────┐           ║
   ║   │       │                │  SCENE RESOLUTION MODES    │           ║
   ║   │       │                │  • Fieldwork (§4)          │           ║
   ║   │       │                │  • Dialogue (§5)           │           ║
   ║   │       │                │  • Contest (§6)            │           ║
   ║   │       │                │  • Combat (§7)             │           ║
   ║   │       │                │  • Threadwork (§9)         │           ║
   ║   │       │                │  • Travel (§3)             │           ║
   ║   │       │                │  • Cutscene (§19)          │           ║
   ║   │       │                └─────────┬──────────────────┘           ║
   ║   │       │                          │ G: scene resolves            ║
   ║   │       ◄──────────────────────────┘                              ║
   ║   │       │                                                        ║
   ║   │       │ P: scene budget exhausted OR                            ║
   ║   │       │    player commits "End Personal Phase"                  ║
   ║   │       ▼                                                        ║
   ║   │   [PHASE 2: STRATEGIC PHASE]  faction board play                ║
   ║   │       │ G: player's faction actions + NPC tree resolutions     ║
   ║   │       ▼                                                        ║
   ║   │   [PHASE 3: CASCADE]  5-step animated sequence                  ║
   ║   │       │ G: 13-step Accounting embedded                         ║
   ║   │       ▼                                                        ║
   ║   │   [PHASE 4: AFTERMATH]  companion scene + Conviction revision   ║
   ║   │       │ G: next season opens                                   ║
   ║   └───────┘                                                        ║
   ║                                                                    ║
   ╚════════════════════════════════════════════════════════════════════╝
                           │ G: victory or shared loss condition met
                           ▼
            ┌─────────────────────────────────────────────────────────┐
            │                    [ENDGAME]                             │
            │        Epilogue cutscene → Credits → Main Menu           │
            └─────────────────────────────────────────────────────────┘
```

## §1.2 Phase timing

| Phase | Target duration | Skippable after first | Notes |
|-------|-----------------|----------------------|-------|
| 0 Briefing | 30–60s | Partial (cutscene only; summary persists) | Cinematic; sets the emotional register |
| 1a Duty | 60–120s | Yes after Counselor stature (negotiable duties) | Personal scene with faction leader |
| 1b Slate Reveal | 10–15s | Yes | Entries animate in, one per beat |
| 1c Personal Phase | 30–120 min | N/A | The bulk of play; player-paced |
| 2 Strategic | 60–180s | N/A | Animated board state, partly auto-resolved |
| 3 Cascade | 60–120s | Partial (each step dismissible after read) | The season closes; consequences land |
| 4 Aftermath | 60–180s | Yes once company has been established | Companion scene + Conviction revision |

Total season length: one sitting of 45–150 minutes depending on play pace and Slate engagement. Campaigns target 30–50 seasons.

## §1.3 Auto-save boundaries

The game auto-saves at every phase boundary. Save slots named by Season + Year (e.g., "Spring 3"). 10 rolling slots + 3 player-named manual saves.

**Critical rule:** no saves within a single scene resolution. Once a roll has started, the player cannot reload to re-roll. This is philosophical — the game does not let the player save-scum the d10 engine. Scene resolution is atomic. Reloading mid-season returns to the most recent phase boundary, which is always pre-resolution.

## §1.4 Pause behavior

- Personal Phase pausable (menu)
- Strategic Phase pausable (menu), but the board animations freeze — not a tactical pause
- Cascade NOT pausable — it is a viewing phase; you watch the world close its accounts
- Cutscenes pausable (menu) but not fast-forwardable until fully watched once (first viewing is sacred per §19)

## §1.5 State data shape (Godot)

```
state {
  campaign_id: UUID
  season: { year, name, number }
  phase: enum {BRIEFING, DUTY, SLATE_REVEAL, PERSONAL, STRATEGIC, CASCADE, AFTERMATH}
  current_location: LocationRef
  scene_action_budget: { base, current, modifiers: [{source, delta}] }
  active_slate: [SlateEntry]
  slate_entries_pursued_this_season: [SlateEntryId]
  current_scene: SceneRef | null
  pending_cutscenes: [CutsceneRef]  // fire at phase boundaries
  world: PeninsulaState
  player: PlayerState
  companions: [CompanionState, max 2]
  factions: [FactionState]
  clocks: { MS, CI, IP, GEN }
  investigations: [Investigation]
  journal: JournalState
  codex: CodexState
  unlocked_codex_entries: [EntryId]
}
```

Signal bus: every state change emits a typed signal. UI components subscribe to the signals they render from. No polling.

---

# PART 2 — THE PERSISTENT CHROME

Every element always on screen during play. These elements are spatial constants — they do not move, they do not vanish (except during cutscenes and combat full-zoom, both explicitly noted).

## §2.1 Layout

```
╔════════════════════════════════════════════════════════════════════════════════════╗
║  [BREADCRUMB TRAIL]        season [name · year]        [actions: 3/4]   ☰ menu    ║
╠════════════╦════════════════════════════════════════════════╦══════════════════════╣
║            ║                                                 ║                      ║
║  [LEFT     ║                                                 ║    [RIGHT RAIL:      ║
║   CONTEXT  ║                                                 ║     clocks, drift,   ║
║   PANEL]   ║          MAIN VIEW                              ║     stature, conv,   ║
║            ║          (layer-specific content)               ║     obligations]     ║
║  resource  ║                                                 ║                      ║
║  tracks,   ║                                                 ║                      ║
║  evidence, ║                                                 ║                      ║
║  cover/    ║                                                 ║                      ║
║  exposure  ║                                                 ║                      ║
║            ║                                                 ║                      ║
╠════════════╩════════════════════════════════════════════════╩══════════════════════╣
║  [COMPANION STRIP]  Eira · Tamm  (portraits, status, Conviction tag, commentary)   ║
╠════════════════════════════════════════════════════════════════════════════════════╣
║  [SLATE DOCK — docked left edge, expandable]  OR  [ACTION PROMPT — current scene]  ║
╚════════════════════════════════════════════════════════════════════════════════════╝
```

## §2.2 Breadcrumb trail (top bar)

```
Peninsula  ›  Gransol (T8)  ›  Parliament (S-015)  ›  Court
```

- Each segment clickable; clicking zooms out to that layer
- The rightmost segment is the current scope (non-clickable; you are here)
- Season displayed centered: `Winter · Year 3`
- Scene action counter right-anchored: `actions: 3/4` (amber at 1, red at 0)
- Menu hamburger far right — opens Codex, Settings, Save/Load

## §2.3 Right rail (persistent column)

Six stacked blocks. Fixed width 280px at 1080p, scales at higher resolutions (§22).

### §2.3.1 Clocks (top)

Four global clocks, band-labeled:

```
┌─────────────────────────────────────┐
│  MS · Fragile     [■■■■■□□□□□]  48  │
│  CI · Strained    [■■■■■■□□□□]  52  │
│  IP · Strained    [■■■■■□□□□□]  41  │
│  GEN · Year 3     [□□□□□□□□□□]  0.2 │
└─────────────────────────────────────┘
```

Hover any bar: full tooltip with exact value, next band threshold, and most recent change source.

**Visual treatment of band transitions (ambient, always-on):** the MS bar is not just a number — as MS crosses from Strained to Fragile, the bar itself acquires a barely-perceptible shimmer. At Fractured, the shimmer intensifies and the bar's geometry has minor inconsistency frame-to-frame. This is one of the §20 feel layers: the HUD itself reflects substrate state. `[RESOLVES UI-06]` — Framework Drift pulse and MS shader intensity spec in §20.

### §2.3.2 Framework Drift strip

```
┌─────────────────────────────────────┐
│  FRAMEWORK DRIFT                    │
│  Crown   · → · Influence +1         │
│  Church  · ↑ · CI +1 accounting     │
│  Hafen   · · · stable               │
│  Varfell · ↓ · Intel −1             │
│  L-R     · · · stable               │
└─────────────────────────────────────┘
```

Each faction's current-season drift direction. Arrow = up (↑), down (↓), flat (·), shifting (→).
`[RESOLVES UI-06]`: pulse intensity is 80% alpha at 1.2s cycle — perceptible but not distracting. In tests (informal), this lands as ambient rather than demanding attention.

### §2.3.3 Stature stack

```
┌─────────────────────────────────────┐
│  STANDING · Crown · ●●●○○ Counselor │
│  RENOWN   · ●●●●●●○○○○ 6/10         │
│            scope: Multi-Settlement  │
└─────────────────────────────────────┘
```

### §2.3.4 Convictions (always visible)

```
┌─────────────────────────────────────┐
│  CONVICTIONS (3)                    │
│  A · I will prove to Almud the      │
│     Thread is real          ●○○     │
│  B · I will protect Torben          │
│     from the Altonian       ●○○     │
│  C · I will build a network of      │
│     Thread-aware allies    ●●○ ⚠   │
└─────────────────────────────────────┘
```

Scar pips per Conviction. Third Conviction at 2 scars shows the ⚠ amber warning — one more scar forces transform-or-abandon in Phase 4.

### §2.3.5 Obligations (new in v4, resolves UI-05)

```
┌─────────────────────────────────────┐
│  OBLIGATIONS                        │
│  ▸ Crown: no Altonian marriage      │
│     talks for Torben · 2 seasons    │
│  ▸ you: help Eira find her sister   │
│     in T17 · no deadline            │
└─────────────────────────────────────┘
```

`[RESOLVES UI-05]`: Obligations live in the right rail as a dedicated block, not a separate panel. Clicking an Obligation expands it to a floating card with full terms, violation consequence, and current compliance status. Obligations do NOT require a dedicated top-level screen — they belong alongside the other commitments the player tracks (Convictions, Duty, Standing).

### §2.3.6 Duty

```
┌─────────────────────────────────────┐
│  CURRENT DUTY                       │
│  Investigate Vaelke                 │
│  Evidence: 3/5 (Complex)            │
│  Success: reveal Niflhel ties       │
│  Failure: Crown Stability −1        │
└─────────────────────────────────────┘
```

## §2.4 Left context panel

Content changes by layer — not a persistent column the way the right rail is. During combat it shows Health/Stamina/Composure/Momentum/Coherence; during fieldwork it shows Cover/Exposure and active Evidence Tracks; during Strategic Phase it shows the faction hand panel.

Width 240px at 1080p.

## §2.5 Companion strip (bottom)

```
┌─────────────────────────────────────────────────────────────────┐
│  [Eira portrait]  [ Eira : Equity ]   Disp +4 (Devoted) · Knot ●│
│     Health 7/24 · free: Social · 💬 "Push her. She knows."       │
│                                                                  │
│  [Tamm portrait]  [ Tamm : Order ]    Disp +3 (Trusting)         │
│     Health 12/24 · free: Governance at S-008 · 💬 quiet          │
└─────────────────────────────────────────────────────────────────┘
```

**Slate commentary format is `[ Name : Conviction ]`** per Jordan's specification. The Conviction is the NPC's primary Conviction from their Stance Triangle per npc_behavior_v30 §1.2. The companion's commentary line follows in natural speech — their voice, their concern, not an abstract moral claim.

Example commentary formats across all seven Conviction types (npc_behavior §1.2):

- `[ Arne : Faith ]` "The Confessor's sermon was true. We must attend."
- `[ Almud : Order ]` "This one first. The rest can wait."
- `[ Maret : Reason ]` "The evidence contradicts that account. Investigate."
- `[ Eira : Equity ]` "These people have no one. Go to them."
- `[ Inge : Precedent ]` "Parliament has ruled on this before. Cite it."
- `[ Lisbeth : Autonomy ]` "Let them choose. Don't impose."
- `[ Edeyja : Continuity ]` "The work continues. Nothing else matters."

## §2.6 Slate dock (left edge)

Docked to the left edge during Personal Phase. Expandable. Collapsed state shows priority pips only.

```
collapsed:      expanded:
┌─┐            ┌──────────────────────────────┐
│0│            │ SLATE · 7 entries            │
│1│            │ ─────────────────────────    │
│1│            │ ⚠0 Ambush in Feldmark        │
│1│            │   [ Eira : Equity ] urgent   │
│2│            │ ─────────────────────────    │
│3│            │ ●1 Heresy investigation      │
│4│            │   against Vaynard opens      │
│5│            │   [ Tamm : Order ]           │
│ │            │ ─────────────────────────    │
│ │            │ ●1 Treasury crisis at S-015  │
│ │            │   [ Eira : Equity ] relevant │
│ │            │ ...                          │
└─┘            └──────────────────────────────┘
```

Each entry shows: priority badge, summary, companion tag (if commentary exists), Conviction-relevance highlight (if any of player's Convictions matches).

Clicking an entry opens it (enters scene). Shift-clicking archives it (marks "not pursued") — archived entries resolve through NPC AI per player_agency §4.5.

---

# PART 3 — TRAVEL AND ZOOM

Authoritative sources: fieldwork_v30 §3.3, settlement_layer_v30 §4.1, scale_transitions_v30 §4, geography_v30.

## §3.1 The three layers

| Layer | Zoom state | Surface |
|-------|-----------|---------|
| Peninsula | outermost | 17-territory illustrated map |
| Province | intermediate | province panel overlay with settlement nodes |
| Settlement | innermost | location list (Darklands / Pentiment) |
| Scene | deepest | scene-specific resolution surface (combat grid, dialogue, contest chamber, Thread panel) |

The persistent chrome (§2) is present at all four layers. Only cutscenes (§19) remove it.

## §3.2 The Peninsula map

Rendered as an illustrated 2D overhead. Hand-painted style (Triangle Strategy precedent — see §23). Water textured, mountains shaded, roads visible, territory borders marked with ink lines.

### §3.2.1 Encoding table

| Element | Visual encoding |
|---------|-----------------|
| Faction control | Color fill per territory (Crown forest-green, Church indigo, Hafenmark amber, Varfell violet, Löwenritter oxblood, RM teal, Guilds ochre, Uncontrolled gray) |
| Accord | Fill saturation (3+: full, 1–2: muted, 0: desaturated + agitation shader) |
| Occupation | Hatched overlay, base color + hatch pattern in occupier color |
| Framework Drift | Subtle edge pulse (1.2s cycle, 80% alpha peak) in faction color |
| MS substrate state | Global shader on the whole map (§9.6 details) |
| Calamity gradient | Static radial darkening from Askeheim T15, intensifies as MS drops per calamity_radiation_v30 |
| Player position | Illustrated character silhouette token |
| Companion positions | Smaller silhouettes beside player |
| Active Slate anchor | Amber glow halo around the relevant territory/settlement node |
| Incoming threat | Red arrow from source to target territory, visible 1 season before resolution |

### §3.2.2 Interaction

- Hover territory: tooltip with province name, controller, Accord band, Fort Level, Garrison strength, Calamity proximity band
- Left-click territory: open province panel (§3.3)
- Right-click (or long-press on touch): open Codex entry for the territory
- Scroll/pinch: zoom in/out within the Peninsula (smooth, not layer-changing — just visual magnification)

## §3.3 The province panel

Opens over the Peninsula when a territory is clicked. Peninsula dims to 40% opacity behind.

```
╔══════════════════════════════════════════════════════════════════════════╗
║  ← back to Peninsula                    T8 GRANSOL                        ║
║                                                                            ║
║  Controller: Hafenmark (Duchess Inge Baralta)                             ║
║  Accord: ⌊(Order_S15 + Order_S16 + Order_S17) / 3⌋ = 2 (Content)         ║
║  Fort Level: 2   Garrison: HI×1, Archers×1                                ║
║  Calamity proximity: Distant (T15 → T8 path length 4)                     ║
║  Heresy Investigation active: no                                          ║
║                                                                            ║
║  ─── SETTLEMENTS ─────────────────────────────────────────────            ║
║                                                                            ║
║   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐            ║
║   │ S-015         │    │ S-016         │    │ S-017         │            ║
║   │ Parliament    │    │ Harbor        │    │ Market Quarter│            ║
║   │ SEAT          │    │ PORT          │    │ CITY          │            ║
║   │ P 5 / D 3 / O 3│   │ P 6 / D 1 / O 3│   │ P 4 / D 0 / O 2│           ║
║   │ gov: Baralta  │    │ gov: Harbor-  │    │ gov: Guild-   │            ║
║   │               │    │     master    │    │     master    │            ║
║   │ ★ anchor here │    │               │    │               │            ║
║   └───────────────┘    └───────────────┘    └───────────────┘            ║
║                                                                            ║
║  ─── SUBNATIONAL PRESENCE ────────────────────────────────────            ║
║  ✓ Ministry (clerks, administrators)                                      ║
║  ✓ Guilds (merchant houses)                                               ║
║  ? something · Cognition 3 detects unease at S-015 (covert presence?)     ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

- Settlement cards arranged spatially per their rough in-province geography (not random grid)
- Governor/Provincial Authority tension line appears between badges when they diverge (Crown-governed settlement in Hafenmark province, for example)
- Subnational presence listed at bottom; Niflhel covert presence shows as `? something · Cognition N detects unease` until revealed
- `[RESOLVES UI-15]`: covert Niflhel pre-reveal is always-ambient (any player can see the `?` entry) BUT only Cognition ≥ 3 parses the specific cue. Below Cognition 3, the `?` reads as "unclear — something uncategorizable here." At Cognition 3+, it reads as "something · unease at S-015." This shifts the information gate from perceptual (you can/can't see it) to interpretive (you see the cue, but parsing requires skill). That is closer to P-03's core: rendering is consciousness-performed, and perception is gradient, not binary.

## §3.4 The settlement interior

Opens when a settlement node is clicked. Rendered as a **location list**, not a walkaround environment. This is deliberate — Darklands / Pentiment precedent. The art is illustrated vignettes, one per location.

```
╔══════════════════════════════════════════════════════════════════════════╗
║  ← back to Gransol                 S-015 PARLIAMENT                       ║
║                                                                            ║
║  Type: Seat  |  Stats: Prosperity 5 / Defense 3 / Order 3                 ║
║  Governor: Duchess Inge Baralta (Conviction: Precedent)                   ║
║                                                                            ║
║  ┌────────────────────────────────────────────────────────────────┐       ║
║  │ THE COURT                                                       │       ║
║  │ [vignette illustration: high-ceilinged hall, banners]           │       ║
║  │ Depth: [●●●○○] access up to Hidden                              │       ║
║  │ NPCs present: Baralta's Aide (Disp +2) · Clerk of Seals (Disp 0)│       ║
║  │ ★ Active anchor: "Baralta treasury crisis" (Evidence 2/?)       │       ║
║  │ [ Enter ]                                                       │       ║
║  └────────────────────────────────────────────────────────────────┘       ║
║                                                                            ║
║  ┌────────────────────────────────────────────────────────────────┐       ║
║  │ THE ARCHIVES                                                    │       ║
║  │ [vignette: dim shelves, scrolls, a ladder]                      │       ║
║  │ Depth: [●●●●○] access up to Buried (institutional)              │       ║
║  │ NPCs present: Head Archivist (Disp −1)                          │       ║
║  │ [ Enter ]                                                       │       ║
║  └────────────────────────────────────────────────────────────────┘       ║
║                                                                            ║
║  ┌────────────────────────────────────────────────────────────────┐       ║
║  │ THE DUCHESS'S CHAMBERS                                          │       ║
║  │ [vignette: private study, heraldic tapestry]                    │       ║
║  │ Depth: [●○○○○] access Surface only (Disp −1 with Duchess)       │       ║
║  │ NPCs present: Duchess Inge Baralta (Disp −1)                    │       ║
║  │ [ Enter ]                                                       │       ║
║  └────────────────────────────────────────────────────────────────┘       ║
║                                                                            ║
║  ┌────────────────────────────────────────────────────────────────┐       ║
║  │ THE GALLERIES (public)                                          │       ║
║  │ [vignette: a market-like corridor where petitioners wait]       │       ║
║  │ Depth: [●●○○○] access up to Settled                             │       ║
║  │ NPCs present: 3 petitioners · 2 guards                          │       ║
║  │ [ Enter ]                                                       │       ║
║  └────────────────────────────────────────────────────────────────┘       ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

Each location card shows:
- Name and brief atmospheric description
- Vignette illustration (painted, not rendered 3D)
- Depth access (per fieldwork §5.4)
- NPCs present with Disposition
- Active Slate anchor if one anchors here
- Enter button (opens the action panel for the location — §4.3)

## §3.5 The scene surface

The innermost layer. Differs per resolution mode:
- Fieldwork: action panel (§4.3)
- Dialogue: dialogue interface (§5)
- Contest: contest exchange UI (§6)
- Combat: hex grid (§7)
- Threadwork: Thread panel overlay (§9)

All scene surfaces retain the persistent chrome (§2) except combat at full focus (chrome compresses to bars on edges) and cutscenes (chrome hidden).

## §3.6 Zoom transitions (animated)

| Transition | Duration | Easing | Audio cue |
|------------|----------|--------|-----------|
| Peninsula → Province | 400ms | ease-out cubic | Faint parchment-turn |
| Province → Settlement | 500ms | ease-out cubic | Muted bell |
| Settlement → Scene | 600ms | ease-in-out | Soft drawing-in breath |
| Scene → Settlement | 500ms | ease-in cubic | Soft release |
| Settlement → Province | 400ms | ease-in cubic | Faint parchment-turn |
| Province → Peninsula | 400ms | ease-in cubic | Broader air |

The slower inner zoom reinforces scene-entry weight. Skippable via Settings after first campaign.

## §3.7 Travel costs (fieldwork §3.3)

| Move | Scene action cost |
|------|-------------------|
| Within settlement (switch location) | 0 |
| Between settlements in same province | 0 |
| Between provinces (adjacent) | 1 |
| Cross-peninsula (non-adjacent) | 1 per province traversed |

The UI displays travel cost on the breadcrumb segment before commit:

> `Peninsula › Gransol (T8) › ... click T9 Himmelenger: 1 action`

Travel to Askeheim (T15) requires TS ≥ 30 party-wide per mass_battle §A.11. The UI displays this as a red lock on Askeheim with the warning on hover; non-qualifying party members cannot traverse.

---

# PART 4 — FIELDWORK

Authoritative source: fieldwork_v30.md (full).

## §4.1 What fieldwork is

Fieldwork is the master activity during Personal Phase. Most Slate entries resolve through it. It encompasses exploration (§3 of the ruleset), investigation (§4), and socialising (§5), all sharing a unified pool system and depth-axis perception gate.

## §4.2 The depth axis is the perception system

Fieldwork §1 defines 5 depths: Surface (0), Settled (1), Hidden (2), Buried (3), Liminal (4), Unintelligible (5).

The UI always displays the current character's accessible depth at the current location. Unlocked depths are illuminated; locked depths are dim with their gate requirement on hover.

```
Location: Gransol Parliament · Court
Depth access: [●●●○○]
Accessible: Surface, Settled, Hidden
Locked: Buried — requires TS ≥ 10 OR Disposition +3 with Court NPC
Locked: Liminal — requires TS ≥ 30
```

This is not a menu. It is the character's perceptual horizon rendered as UI. P-03 made explicit. `[RESOLVES ED-544]`: the videogame rendering model IS the depth-access gate. A non-sensitive character literally cannot access Liminal-depth options because the options do not appear. A sensitive character sees them. Same scene, different renderings.

## §4.3 Action panel

When a location is entered, the action panel opens. This is the primary fieldwork surface.

```
╔══ GRANSOL PARLIAMENT · COURT ═══════════════════════════════════════════╗
║                                                                          ║
║  [ambient: sound of murmurs, footsteps on stone, distant bell]          ║
║                                                                          ║
║  NPCs: Baralta's Aide (+2 Friendly) · Clerk of Seals (0 Neutral)         ║
║  Your Depth access: Hidden  ·  Cover: 6  ·  Exposure: 3/9 Compromised    ║
║  Active investigation: Baralta treasury crisis · 2/?                     ║
║                                                                          ║
║  ─── EXPLORATION ────────────────────────────────────────────────       ║
║                                                                          ║
║   ▸ Examine the ledger                                                   ║
║     Cognition 4 + Accounting 2 = 10D · TN 7 · Ob 2 · Exp +1             ║
║                                                                          ║
║   ▸ Surveil the Court                                                    ║
║     Cognition 4 + Concealment 2 = 10D · TN 7 · Ob 2 · Exp +2            ║
║                                                                          ║
║  ─── INVESTIGATION ──────────────────────────────────────────────       ║
║                                                                          ║
║   ▸ Research the Parliament records                                      ║
║     Recall 3 + Archives 1 = 7D · TN 7 · Ob 2 · Exp +1                   ║
║                                                                          ║
║   ▸ Reconstruct current evidence                                         ║
║     Recall 3 × 2 + Deduction 0 = 6D · TN 7 · Ob = thresh − 2, min 1     ║
║     → Synthesis attempted with 2/? Evidence                              ║
║                                                                          ║
║   ▸ Thread-Read this chamber    [TS 42 — AVAILABLE]                      ║
║     (Spirit 4 × 2) + Thread 2 + TPS 4 = 14D · TN 7 · Ob per Depth       ║
║     Depth 3 (Buried): Ob 3 · Exp +1 · −1 Coherence · co-movement fires  ║
║                                                                          ║
║  ─── SOCIALIZING ────────────────────────────────────────────────       ║
║                                                                          ║
║   ▸ Read Baralta's Aide · Attunement 4 = 4D · TN 7 · Ob 2               ║
║   ▸ Converse with Aide   · Charisma 5 = 5D · TN 7 · Ob 2                ║
║   ▸ Connect with Aide    · Bonds 3 + relational 1 = 4D · Ob 3           ║
║   ▸ Impress Clerk (1st)  · Charisma 5 + Courtier 2 = 7D · Ob 2          ║
║   ▸ Rumour               · Charisma 5 = 5D · Ob 2 · Exp +1              ║
║   ▸ Negotiate with Aide  · Attunement 4 + Courtier 2 = 6D · Ob 3        ║
║   ▸ Gift (once per NPC per season)  · no roll · +1 starting Disp        ║
║                                                                          ║
║  ─── TRANSITIONS ────────────────────────────────────────────────       ║
║                                                                          ║
║   ▸ Enter dialogue with Baralta's Aide                                   ║
║   ▸ Escalate to Contest                                                  ║
║   ▸ Initiate combat  [warning: conspicuous, +2 Exp]                      ║
║   ▸ Leave the Court (go to another location)                             ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

Each action line shows: action name, primary pool formula, TN, Ob, Exposure projection. Hover: detailed breakdown.

### §4.3.1 Action buttons — click flow

1. Click action → confirmation modal with projected outcome band:

   > Examine the ledger
   > Pool 10D vs Ob 2
   > Projected: 92% success rate, 45% overwhelming, 3% failure
   > Exposure cost: +1 → 4/9 Compromised
   > Continue?

2. Confirm → dice roll animation (1.2s; each die lands with a small thud audio). 10-face d10 visualization. 1s red, 2–6 gray, 7–9 blue check, 10 gold chain icon.

3. Result animates: net successes highlight, degree label fades in (SUCCESS · PARTIAL · OVERWHELMING · FAILURE), Evidence Track bar fills visibly, Exposure bar advances.

4. If Overwhelming or critical threshold reached: subtle screen flash + audio cue.

5. Return to action panel; some actions may now be unavailable (e.g., once Gift used on an NPC, its button is disabled for the season; once Reconstruct is attempted, the Evidence Track is re-evaluated).

## §4.4 Cover and Exposure

Per fieldwork §6, two separate mechanics.

**Cover** is a character stat: `Cover = Cognition + relevant concealment History`. Determines Exposure thresholds (Noticed / Watched / Compromised).

**Exposure** is per-territory per-season. Actions generate Exposure; thresholds trigger consequences.

Display in left context panel during fieldwork:

```
┌────────────────────────────┐
│  COVER: 6                  │
│  (Cognition 4 + Conc 2)    │
│                            │
│  thresholds                │
│  ● Noticed       5         │
│  ● Watched       7         │
│  ● Compromised   9         │
│                            │
│  EXPOSURE in T8 Gransol    │
│  [■■■□□□□□□] 3/9           │
│  next action projects +1   │
│                            │
│  at Noticed: +1 Ob all     │
│  at Watched: Heresy    [!] │
│  at Compromised: scene     │
│    ends, Disp−1 all NPCs   │
└────────────────────────────┘
```

Every action button in the action panel shows its projected Exposure cost. The player sees the threat clearly.

When a threshold is crossed, a full-screen event fires:

- Noticed: a muted notification — "Noticed. They know you're here. +1 Ob to fieldwork rolls this season in Gransol."
- Watched: louder notification with faction-specific cue — "The Duchess has been informed. A Hafenmark counter-intel officer is now active. Expect response."
- Compromised: hard stop. Scene ends. "Your cover is blown. Leave the territory or go to ground." The action panel dismisses; the player is returned to the Settlement view with a "Go to ground" action available.

## §4.5 The Journal

Accessible from any layer via the Journal icon in the breadcrumb or the `J` keyboard shortcut.

```
╔══════════════════════════════════════════════════════════════════════════╗
║                              JOURNAL                                       ║
║                                                                            ║
║  ┌──────────────────┬───────────────────────────────────────────────┐    ║
║  │ ACTIVE (4)       │  Baralta treasury crisis                      │    ║
║  │ ● Baralta crisis │  Status: Open · Complex (threshold hidden)    │    ║
║  │ ● Church secret  │  Evidence: [■■□□□] 2/?                        │    ║
║  │ ● Niflhel ops    │                                                │    ║
║  │ ● Einhir ruin    │  EVIDENCE ASSEMBLED                            │    ║
║  │                  │  ─────────────────                             │    ║
║  │ RESOLVED (2)     │  ▸ Ledger discrepancy                         │    ║
║  │ ○ Vaelke poison  │    Documentary · S-015 Archives · today       │    ║
║  │ ○ Forged decree  │    "Payment ledger shows 1,200 gold           │    ║
║  │                  │     transferred without authorization entry"  │    ║
║  │ RUMORS (7)       │                                                │    ║
║  │ · Almud whisper  │  ▸ Overheard remark                           │    ║
║  │ · Ehrenfeld      │    Testimonial · Clerk of Seals · today       │    ║
║  │   practitioner   │    "The Duchess met with someone three        │    ║
║  │ · ...            │     nights ago. I saw her leave the East       │    ║
║  │                  │     corridor at the second bell."             │    ║
║  │                  │                                                │    ║
║  │                  │  [ Reconstruct → ]  [ Close investigation ]   │    ║
║  │                  │                                                │    ║
║  └──────────────────┴───────────────────────────────────────────────┘    ║
║                                                                            ║
║  [ back ]                                            [Codex → ] [Settings]║
╚══════════════════════════════════════════════════════════════════════════╝
```

- Left column: investigation list sorted by status
- Right panel: detail view of selected investigation
- Each evidence piece shows: text, reliability tag (colored chip), source NPC/location, date acquired
- Inert Knowledge evidence: strikethrough with tooltip — "You can recite this, but you cannot act on it with Thread-level precision. P-08."
- Desperate Trail status: red banner at top of detail view
- Reconstruct button: prominent when Evidence Track at threshold; muted but available when below

## §4.6 The Reconstruct surface

When Reconstruct is clicked, a deduction-board overlay opens. This is a distinct screen — one of the few times the UI takes over.

```
╔══════════════════════════════════════════════════════════════════════════╗
║  RECONSTRUCT · Baralta treasury crisis                    [ cancel ]      ║
║                                                                            ║
║  Arrange evidence into a coherent account.                                ║
║  Drag evidence cards. Links auto-form between supporting pairs.           ║
║                                                                            ║
║  ┌────────────────────────────────────────────────────────────────┐       ║
║  │                                                                  │       ║
║  │   [Ledger discrepancy]────links──[Clerk's remark]               │       ║
║  │                    \                  /                         │       ║
║  │                     \                /                          │       ║
║  │                      [Unknown 3rd party meeting]                │       ║
║  │                               │                                 │       ║
║  │                         [Motive? Target?]                       │       ║
║  │                                                                  │       ║
║  └────────────────────────────────────────────────────────────────┘       ║
║                                                                            ║
║  POOL: Recall 3 × 2 + Deduction History 0 = 6D                            ║
║  TN 7 · Ob = threshold − progress = ? − 2 (probe)                         ║
║                                                                            ║
║  On Success: Finding produced, usable as +1D in contests, Domain Action   ║
║              justification, Parliamentary citation.                        ║
║  On Failure: Conclusion produced is WRONG. You will not know it is wrong  ║
║              unless subsequent evidence contradicts it.                   ║
║                                                                            ║
║  [ Commit — roll the Reconstruct ]                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

`[RESOLVES UI-12]`: the deduction board uses a **template per investigation type** (Simple: 3 slots + synthesis, Complex: 5 slots + 2 synthesis, Structural: 8 slots + 3 synthesis branches). The template is not freeform — it scaffolds the player's thinking without forcing interpretation. The arrangement maps to mechanical synthesis; the roll determines correctness. The template visualizes like a detective's pinboard (Case of the Golden Idol precedent), but with pre-set slots to avoid the common freeform-board failure of players getting lost in visual space with no structural guidance.

---

# PART 5 — DIALOGUE AS DISCO-ELYSIUM CONVICTION INTERFACE

Authoritative sources: player_agency_v30 §2 (Convictions), fieldwork_v30 §10.4 (dialogue), social_contest_v30 §9.5 (Beliefs integration), npc_behavior_v30 §1 (Stance Triangle), §3 (Beliefs), §6 (Resonant Style).

## §5.1 What dialogue is and is not

Dialogue is the most frequent personal-scale interaction. It is NOT the social contest system (§6) — that is structured multi-exchange with Conviction Track and adjudicator. Dialogue is the conversational register: a single scene of back-and-forth where social actions (fieldwork §5.2) resolve discrete meanings.

Dialogue in Valoria is Disco Elysium's spiritual descendant. The player's Convictions and the NPC's Convictions form the frame that constrains what can be said.

## §5.2 Dialogue layout

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║  [NPC portrait, full body, painted — Pentiment-style]                    ║
║                                                                            ║
║  Baralta's Aide                                                            ║
║  Disposition: +2 (Friendly)  ·  Depth access: Hidden                      ║
║  [ Conviction: Precedent ]  (revealed via Appraise)                        ║
║  Primary Resonant Style: Authority  (revealed)                             ║
║                                                                            ║
║  ┌────────────────────────────────────────────────────────────────┐       ║
║  │ "The Duchess is not seeing petitioners today. You'd under-     │       ║
║  │  stand if you'd seen the ledger I've seen."                    │       ║
║  │                                                                  │       ║
║  │  [ Aide's internal state, visible after Read:                   │       ║
║  │    anxious, concealing something specific, protective ]         │       ║
║  └────────────────────────────────────────────────────────────────┘       ║
║                                                                            ║
║  YOUR OPTIONS                                                              ║
║  ──────────────                                                            ║
║                                                                            ║
║  ▸ [READ · Attunement 4 + History 2 = 6D vs Ob 2]                         ║
║     your senses reach out to her                                           ║
║     "Look at the crease between her brow and her hair."                   ║
║                                                                            ║
║  ▸ [CONVERSE · Charisma 5 + Courtier 2 = 7D vs Ob 2]                      ║
║     you know how to hold a room                                            ║
║     "What happened with the ledger? Take your time."                      ║
║                                                                            ║
║  ▸ [CONVICTION · I will protect Torben from the Altonian]                 ║
║     ✦ your Conviction — the Aide may be key to this                       ║
║     "Something the Duchess knows could save the Prince. Help me."        ║
║     [+1 Momentum on Belief-aligned success]                               ║
║                                                                            ║
║  ▸ [FRAMEWORK · Categorical Imperative · Hafenmark-aligned]                ║
║     −1 Ob: she recognizes oath-based appeals                               ║
║     "You swore an oath of service. My oath is to the Prince."             ║
║                                                                            ║
║  ▸ [BELIEF-TARGETED · She serves the institution, not the person]         ║
║     ◆ pressure (3 cumulative = Belief Scar without a contest)            ║
║     "Then serve it. The Duchess is not the institution. Parliament is."  ║
║                                                                            ║
║  ▸ [NEGOTIATE · Attunement 4 + Courtier 2 = 6D vs Ob 3]                   ║
║     below contest threshold — informal agreement                           ║
║     "What would the Duchess need to see me today?"                        ║
║                                                                            ║
║  ▸ [ RUMOUR · Charisma 5 = 5D vs Ob 2 · Exp +1 ]                          ║
║     "I've heard things about that ledger. Care to confirm?"               ║
║                                                                            ║
║  ▸ [AGREE WITH CARDINAL'S POSITION — LOCKED]                              ║
║    🔒 your Conviction forbids: "I will never cooperate with the Church"  ║
║      override = +1 scar on that Conviction. click to confirm override.    ║
║                                                                            ║
║  ▸ [ WALK AWAY ]   no roll, no cost                                        ║
║                                                                            ║
║  ──────────────                                                            ║
║                                                                            ║
║  [ Eira : Equity ]  💬  "She's afraid. Don't bully her."                  ║
║  [ Tamm : Order ]   💬  quiet                                              ║
║                                                                            ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## §5.3 The eight row types

Every dialogue option is one of eight types. Each has its own mechanical and visual treatment.

| Row type | Visual | Mechanical effect |
|----------|--------|-------------------|
| **Mechanical social action** | Plain text + pool | Standard fieldwork §5.2 roll |
| **Conviction-driven** | ✦ gold mark + Conviction text | +1 Momentum on Belief-aligned success per player_agency §2.3 |
| **Framework-aligned** | Amber mark + framework name | −1 Ob on the roll per social_contest §2 Step 3 audience/framework alignment |
| **Belief-targeted** | Purple ◆ mark + Belief text | Adds pressure tick; 3 cumulative = Belief Scar per npc_behavior §3.3 |
| **Negotiate** | Plain with pool | Below contest threshold; escalates to Contest above |
| **Walk away** | Muted text | No roll, no cost, ends scene |
| **Locked by Conviction** | 🔒 red + Conviction text | Override costs +1 scar on player Conviction |
| **Locked by prerequisite** | 🔒 gray + requirement text | Cannot be selected; hover shows what's needed |

### §5.3.1 Conviction-driven options (relevance check)

A player Conviction appears as a dialogue option when the scene is relevant to it. Relevance is one of:
- The NPC is named in the Conviction
- The NPC's faction is named
- The current territory/settlement is named
- Keyword match (Thread, Church, Einhir, Calamity, investigation, treaty, specific NPC name)

Relevance evaluation runs deterministically per scene. The option always shows the literal Conviction text, followed by a specific utterance.

### §5.3.2 Framework alignment

Per social_contest §2 Step 3, a faction's Ethical Framework gives +1D when aligned. In dialogue this reads as −1 Ob (equivalent for single-roll resolution).

Frameworks:
- Crown — Virtue Ethics (appeals to visible excellence)
- Hafenmark — Categorical Imperative (appeals to oath, duty, precedent-as-obligation)
- Church — Divine Command (appeals to doctrine, revelation, institutional sanction)
- Varfell — Consequentialism (appeals to outcome, demonstration, pragmatic benefit)

The framework option appears ONLY when the player's faction framework aligns with the NPC's, OR when the player has deliberately studied the NPC's framework (lifepath history or Appraise Overwhelming).

### §5.3.3 Belief-targeted options (pressure system)

`[NEW IN V4 — pressure mechanism]`: an NPC has up to 5 Beliefs (npc_behavior §3.1). Each Belief has a hidden pressure counter 0–2. When the counter reaches 3 via dialogue pressure (not contest), the Belief is Scarred per npc_behavior §3.3 — this produces the same arc effects as a formal contest Scar, WITHOUT requiring the full contest.

Why this matters: the player can grind down an NPC across many scenes without ever fighting a contest. This is the Disco Elysium texture — relationships change through many small acts, not just big ones.

Pressure rules:
- Each Belief-targeted option uses a pressure that is hidden from the player (they see the option, not the counter)
- One successful Belief-targeted Converse/Negotiate in a dialogue = +1 pressure
- One Overwhelming = +2 pressure
- Pressure persists across sessions
- At 3 pressure: Scar fires at next Phase 3 Accounting, with a Phase 4 revelation dialogue scene

## §5.4 How Convictions LIMIT what the player can say

This is the inversion that makes Valoria's dialogue Disco Elysium-textured. Player Convictions do not only empower options — they REMOVE options.

An option that would directly contradict a stated Conviction appears LOCKED:

```
 ▸ [AGREE WITH CARDINAL'S POSITION — LOCKED]
   🔒 Your Conviction forbids: "I will never cooperate with the Church"
   Override strains this Conviction (+1 scar). Click to confirm.
```

Clicking the locked option opens a confirmation:

```
╔══ CONVICTION OVERRIDE ═════════════════════════════════════════════╗
║                                                                     ║
║  You are about to take an action against your Conviction:           ║
║  "I will never cooperate with the Church"                           ║
║                                                                     ║
║  Current scars on this Conviction: ●●○ (2 / 3)                      ║
║  After override:                   ●●● (3 / 3)                      ║
║                                                                     ║
║  ⚠ At 3 scars, this Conviction MUST transform or be abandoned       ║
║     at the next Phase 4 Aftermath. You may rewrite it as a          ║
║     different stance or remove it entirely (new Conviction slot).  ║
║                                                                     ║
║  [ Confirm — take the locked action, accept the strain ]            ║
║  [ Cancel — do not take this action ]                               ║
╚═════════════════════════════════════════════════════════════════════╝
```

This is the Conviction-strain symmetry from player_agency §2.1 made mechanical. Player Convictions are as real as NPC Convictions.

## §5.5 How NPC Convictions LIMIT their responses

The NPC's responses are generated from their Stance Triangle (npc_behavior §2). Responses consistent with the NPC's primary Conviction are the most likely; responses requiring Conviction strain on the NPC side are blocked unless the player has forced it via contest or pressure.

For player clarity: when an NPC's response is visibly constrained by their Conviction, a subtle italic line sits above the NPC's spoken text:

```
[ Conviction: Precedent restrains her to procedural language ]
"The ledger review would be premature. Parliament has not yet returned from recess."
```

This shows the WHY. The player sees not just what the NPC said, but what frame they were speaking from. Disco Elysium's "internal voices" mapped onto the NPC's reality.

## §5.6 History as skill-voice

Each social action button shows the History that applies. Clicking the History opens a subtle tooltip:

> "Courtier History applies. You know how to navigate formal settings. You know when to bow, when not to, when silence is the right answer. An Appraiser History would apply if you were reading intent; a Commons History would apply if you were among villagers. This History gives you +2D on this roll."

This surfaces character specificity without chattering. One line of skill-voice per option.

## §5.7 Dialogue flow and scene budget

A dialogue is a sequence of exchanges within one scene. Each exchange:

1. NPC speaks (generated text or scripted line)
2. Player selects option
3. Roll fires if needed
4. Consequences apply (Disposition, Evidence, pressure, scars)
5. NPC responds (next exchange)

Typical dialogue scene = 1 scene action. Extended investigations / contests embedded = 2 scene actions.

The dialogue ends when:
- Player walks away
- Player escalates to Contest
- NPC cuts conversation (Disposition drops to −3 during the scene)
- Scene action budget is consumed
- An event interrupts (Slate Priority 0 firing, mandatory scene elsewhere, combat initiation)

## §5.8 Companion voice (re-stated with corrected format)

Per Jordan's specification, companion commentary uses the format `[ Name : Conviction ]` with the companion's primary Conviction from their Stance Triangle (npc_behavior §1.2 taxonomy).

Below every NPC speech, a companion present may interject:

```
[ Eira : Equity ]      💬  "She's afraid. Don't bully her."
[ Tamm : Order ]       💬  "Press. She's hiding something."
[ Vossen : Reason ]    💬  "The ledger's a symptom. What's the cause?"
```

The commentary is in the companion's own voice, reflecting their Conviction but not abstractly naming it. The `[ Name : Conviction ]` tag sits beside the speech bubble as meta-information, not as the speech itself.

Clicking the bubble opens a brief sidebar where the companion elaborates. The player may respond; this is free (no scene action). Returning to the main dialogue continues where it left off.

## §5.9 Ambient cues during dialogue

A dialogue scene is emotionally layered via the §20 feel system:

- **Audio:** NPC's mood drives subtle chamber-music underscore. Anxious NPC = detuned strings; calm NPC = warm woodwinds; hostile NPC = percussive tension
- **Portrait animation:** the painted portrait subtly shifts expression with NPC state. Blink cycles, slight head tilts, brow tension. Pentiment precedent.
- **Background:** the location background varies subtly with time of day and weather (per season state)
- **Thread-sensitive player (TS 30+):** in any scene with another practitioner, a faint shimmer overlay on the NPC portrait reveals their sensitivity. This is P-03 at its strongest — you see what you are attuned to see.

---

# PART 6 — SOCIAL CONTEST

Authoritative sources: social_contest_v30.md (full), npc_behavior_v30 §6.

## §6.1 When contest fires

- Player escalates from dialogue (Negotiate exceeds informal threshold)
- Institutional proceeding opens (Parliament §15, Church Tribunal §16, Royal Audience §16)
- NPC-initiated Demand (npc_behavior §8.11)
- Grand Debate (Treaty §17 escalation)

Contest is structured multi-exchange with Conviction Track. See social_contest_v30 for the mechanics.

## §6.2 Contest setup screen

```
╔══════════════════════════════════════════════════════════════════════════╗
║                       CONTEST OPENING                                      ║
║                                                                            ║
║  [two portraits facing each other: you and Almud, center dais between]    ║
║                                                                            ║
║  PROCEEDING: Royal Audience · adjudicator: King Almud Almqvist            ║
║  EXCHANGE COUNT: 3       (Crown objects throughout)                        ║
║  GENRE PRIMARY: Projection ("what will follow")                            ║
║  AUDIENCE BOOST: Crown · Revealing (+1D match)                             ║
║  [ audience resistance: 1 ]                                                ║
║                                                                            ║
║  CONVICTION TRACK                                                          ║
║  ┌──────────────────────────────────────────────────────────────┐         ║
║  │  0 ─── 2 ─── 4 ─── 5 ─── 6 ─── 8 ─── 10                      │         ║
║  │                     ◉ start 5                                │         ║
║  └──────────────────────────────────────────────────────────────┘         ║
║  Win zones: ≤ 3 = you win · 4–6 compromise · ≥ 7 Almud wins               ║
║                                                                            ║
║  NPC STANCE TRIANGLE (revealed intelligence)                               ║
║  ─────────────────────────────────────                                    ║
║  [ Almud : Order ]          primary Conviction                             ║
║  [ Almud : Reason ]         secondary Conviction (Appraise revealed)       ║
║  Ethical Framework: Virtue Ethics (Crown)                                  ║
║  Primary Resonant Style:  Consequence (Appraise revealed)                  ║
║  Secondary Resonant Style: [ unrevealed ]                                  ║
║  Revealed Belief (1 of 3 active): "Torben must be kept from Altonia"       ║
║                                                                            ║
║  YOUR OPENING BONUSES                                                      ║
║  ────────────────────                                                      ║
║  ▸ Preparation available (1 hour prep: Attunement Ob 1 for +1D Exchange 1)║
║  ▸ Findings available for citation:                                        ║
║    • "Church financial records reveal Crown collusion" (Verified, +1D)    ║
║    • "Baralta's aide overheard crisis remark" (Testimonial, reliability−1)║
║  ▸ Maximum Exchange 1 bonus from Findings: +2D                            ║
║                                                                            ║
║  [ Begin preparation → ]    [ Skip to Exchange 1 → ]                       ║
╚══════════════════════════════════════════════════════════════════════════╝
```

`[RESOLVES UI-13]`: Contests (including Parliament/Tribunal/Audience) use a **layered stage**: a top-down tally view for vote-based contests AND a first-person chamber view that replaces it during key moments (opening statements, Veto declarations, Rebuttal, Total Victory). Switches via `C` key or automatic on decisive events. The stage metaphor is preserved — it feels like a play where sometimes you watch the whole stage, sometimes you zoom in on the speaker.

## §6.3 The exchange

Each exchange unfolds per social_contest §4's step sequence, every step animated:

1. **Appraise** — both orators roll Attunement, results compare, audience boost revealed or confirmed
2. **Style selection** — player picks genre (Memory / Projection) and orientation (Revealing / Obscuring)
3. **Corroborate** — companion offers assist (if eligible)
4. **Evidence citation** — player cites Finding from Journal if available
5. **Resonant Style targeting** — player picks one of NPC's revealed styles (+1D)
6. **Argue roll** — pool animates with all bonuses stacked, then rolls
7. **Resolution** — CLASH / REINFORCE / CROSS / TIE logic resolves, Conviction Track moves
8. **Composure damage** — losing side takes strain, displayed as Composure bar decrement
9. **Doubt Markers / Obscuring effects** — visual indicators applied to opponent
10. **Next exchange** or final resolution

### §6.3.1 Pool assembly visualization

As the player selects bonuses, the pool assembles visibly:

```
Base pool:   Charisma 5 × 2  =  10D     ░░░░░░░░░░
+ History:   Courtier 2       =  12D     ░░░░░░░░░░░░
+ Genre:     Projection       =  13D     ░░░░░░░░░░░░░
+ Audience:  Revealing match  =  14D     ░░░░░░░░░░░░░░
+ Corrob:    Eira (Ob 1)      =  15D     ░░░░░░░░░░░░░░░
+ Finding:   Church records   =  16D     ░░░░░░░░░░░░░░░░
+ MS target: Consequence      =  17D     ░░░░░░░░░░░░░░░░░
─────────────────────────────  vs  Ob 2
                              = 17D vs 2
```

Each addition lands with a small cue — dice clicking into the pool. The player sees exactly what they've built.

### §6.3.2 Free-text argument field

```
STATE YOUR ARGUMENT (flavor; mechanical resolution is the roll)
┌────────────────────────────────────────────────────────────┐
│ The Church's records are clear. Crown funds were redirected│
│ to an Altonian account last season. Your own Chancellor    │
│ signed. If this continues, Torben's inheritance is already │
│ sold — not to parliament, but to foreign powers.           │
└────────────────────────────────────────────────────────────┘
```

This is optional flavor. Does not affect mechanics. Some players will skip; others will savor. Pentiment precedent — the argument text can be saved to the Codex as part of the session record.

### §6.3.3 Roll and resolution

Dice roll animates. Net successes calculated. Opposition's roll follows (animated). Comparison resolves with a specific visual per interaction type:

- CLASH: swords cross, clang audio, Conviction Track jerks toward winner
- REINFORCE: both arguments push together, Track glides
- CROSS: two speakers past each other, Track splits slightly, Doubt Marker appears as a question mark on opponent
- TIE: the argument hovers; neither side claimed it

## §6.4 Post-contest resolution

```
╔══════════════════════════════════════════════════════════════════════════╗
║                          CONTEST RESOLVED                                  ║
║                                                                            ║
║  TOTAL VICTORY · You                                                       ║
║  Final Track: 2 / 10 (your side)                                          ║
║                                                                            ║
║  IMMEDIATE CONSEQUENCES                                                    ║
║  ─────────────────────                                                     ║
║    • Almud: Contest Fatigue (−1D next social roll, clears next session)  ║
║    • You: +1 Momentum                                                      ║
║    • Disposition with all witnesses shifted                               ║
║                                                                            ║
║  CONVICTION SCAR on Almud's Order — 1 scar accumulated                    ║
║  [ the NPC portrait briefly cracks — a second flicker — then settles ]    ║
║                                                                            ║
║  OBLIGATION GENERATED                                                      ║
║  ─────────────                                                             ║
║    Commitment: Crown will not authorize Altonian marriage talks for       ║
║                Torben for 2 seasons                                        ║
║    Bound: Crown (NPC compliance enforced via priority tree override)      ║
║    Duration: 2 seasons                                                     ║
║    Violation consequence: Crown Mandate −1, Stability −1                  ║
║                                                                            ║
║  DOMAIN ECHO                                                               ║
║  ───────────                                                               ║
║    Crown · Mandate +1 (Projection-genre decisive win per §6)              ║
║                                                                            ║
║  [animated: the Peninsula map flashes in the reduced-chrome header;       ║
║   Crown's color pulses; a brief shimmer across Gransol territory]         ║
║                                                                            ║
║  [ continue ]                                                              ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## §6.5 Chain contests

Compromise outcomes (Track 4–6) defer tension. Chain logic per social_contest §6.3: max 3 chain contests, then cold equilibrium (4 seasons no contest on topic). The Journal tracks active chains.

---

# PART 7 — PERSONAL COMBAT

Authoritative source: combat_v30.md (full), **including ED-548 Wound Interval correction (patched in this session)**.

## §7.1 Entry

Combat fires from:
- Fieldwork → Combat (hostile contact; Exposure cost per combat §11.5)
- Contest → Combat (mid-contest violence)
- Slate Priority 0 (ambush)
- Deliberate initiation
- Mass combat General Duel (§8)

## §7.2 The corrected Wound system (ED-548)

**Wound Interval = Endurance + 6** (7–13 range)
**Max Wounds = floor(Endurance / 2) + 1** (1–4 range)
**Total Damage Capacity = Wound Interval × (Max Wounds + 1)** (14–65 range)

A character with Endurance 5 has Wound Interval 11 and Max Wounds 3. Total capacity = 11 × 4 = 44 damage. Wounds accrue at 11, 22, 33. Incapacitation at 44. Each Wound: −1D Combat Pool.

## §7.3 The combat HUD (left context panel)

```
┌──────────────────────────────────┐
│  HEALTH — current wound interval │
│  [■■■■■■■■□□□] 8/11              │
│                                  │
│  WOUNDS  ●●○ 2/3 (−2D pool)      │
│  Total capacity: 20/44            │
│                                  │
│  STAMINA [■■■■□] 4/6              │
│  Composure [■■■■■■■■■■■] 11/11    │
│  Momentum ● ● ○ ○  2/4           │
│  Coherence [■■■■■■■■■■] 10/10     │
│                                  │
│  Rattled: 0 marks                 │
│  Out of breath: no                │
└──────────────────────────────────┘
```

All five tracks visible at all times during combat. The Wound Interval bar is the primary one — it fills up to Wound Interval damage, then resets and a Wound pip fills. The mental model: every Wound Interval damage = one Wound taken.

## §7.4 The hex grid

`[RESOLVES UI-01]`: personal combat grid is **12 hexes wide × 8 hexes tall** for standard scenes. Expanded to **16×10 for larger set-pieces** (settlement interior fights, Duchess's chambers with multiple combatants). The grid scales to fit the scene but never shrinks below 10×6 (tactical viability) or exceeds 20×12 (cognitive load).

```
╔══════════════════════════════════════════════════════════════════════════╗
║                          COMBAT · 12×8                                     ║
║                                                                            ║
║       ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                            ║
║      ⬡ ⬡ ⬡ ⬡ 𝐕 ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡    𝐕 = Vaelke (enemy, High init)            ║
║       ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                            ║
║      ⬡ ⬡ ⬡ ⬡ ⬡ 𝐂 ⬡ ⬡ ⬡ ⬡ ⬡ ⬡    𝐂 = Eira (companion, +Fib bonus adj)     ║
║       ⬡ ⬡ ⬡ ⬡ ⬡ 𝐏 ⬡ ⬡ ⬡ ⬡ ⬡ ⬡    𝐏 = player                               ║
║      ⬡ ⬡ ⬡ ⬡ 𝐆 ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡    𝐆 = guard NPC (hostile)                 ║
║       ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                            ║
║      ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                            ║
║                                                                            ║
║  Initiative: Vaelke → Eira → Player → Guard                                ║
║  This round: Vaelke (Phase 1: declare split, secret to you)               ║
║                                                                            ║
║  Reach display (hover any enemy):                                          ║
║    distance 3 hexes · Ranged distance                                     ║
║    your weapon: Longsword (Long Heavy Blade, TN 7, Reach Long)            ║
║    closing to Melee: 2 move actions; they may Feint on approach           ║
╚══════════════════════════════════════════════════════════════════════════╝
```

Hex grid. Six-direction movement. Reach rules visualized per weapon (Short vs Long reach from combat §5).

### §7.4.1 Turn structure

Per combat §2 — phase-based round. The UI presents each phase as a discrete moment:

1. **Phase 1 — Movement declarations** (all characters, simultaneous-declaration)
2. **Phase 2 — Range establishment** (reach priority; who sets the range?)
3. **Phase 3 — Action declarations** (simultaneous, blind-declared)
4. **Phase 4 — Resolution** (priority order per combat §4)
5. **Phase 5 — Damage application** (simultaneous)
6. **Phase 6 — Tracking update** (Stamina, Wounds, Momentum)

### §7.4.2 Offence/Defence split asymmetric information

The key mechanic (combat §3): lower initiative declares first BLIND, higher initiative sees and counter-declares.

**Lower initiative UI (you are lower):**

```
YOUR TURN — Vaelke is watching, then will counter-declare
Pool: 8D  (Agility 3 × 2 + Sword 1 + 3 base − 1 wound − 0 out of breath = 7... corrected: 8 per pool formula)

Adjust split:
  Offence [░░░░]    ◆    [████] Defence
  currently: 3 Off / 5 Def

[ CONFIRM ] (commits split; Vaelke sees it and responds)
[ Full Guard (all Def) ]  [ Take a Breath (no action) ]

⚠ Once you confirm, your commitment is visible to Vaelke. She will declare after.
```

**Higher initiative UI (you are higher, after lower commits):**

```
VAELKE HAS DECLARED:  5 Off / 2 Def [visible]
Your pool: 10D
Adjust split:
  Offence [░░░]    ◆    [███████] Defence
  currently: 3 Off / 7 Def (recommended — she leans heavy attack)

[ CONFIRM ]
[ Feint (3+ Off, pool reduction next round if successful) ]
[ Rescue (Eira at 6,6 is outnumbered — redirect her attacker to you) ]
```

The commit interface is designed around the canonical mechanic — one screen per side, visible commitment asymmetry.

## §7.5 Actions list

All 12 actions from combat §4 available via a hex-bound action panel. Dimmed actions show why:

- Feint — require 3+ Off commit
- Rescue — require adjacent ally outnumbered 2+
- Tie Up — require Close range
- Dodge — require ranged attack incoming
- Leap (Thread) — require TS 30+
- etc.

Hovering a dimmed action shows the unlock condition ("Rescue unavailable — no adjacent ally is outnumbered").

## §7.6 Dice and damage

Standard d10 pool visualization. Damage calculation inline:

```
YOUR OFFENCE: [7 9 10 3 8] → 4 hits + 1 bonus = 5 net
VAELKE DEF:   [6 9 1 5]    → 1 hit − 1 penalty = 0 net

NET HITS: 5 - 0 = 5
STR mod: +3
Weapon: Longsword (Heavy Blade) vs Light Armor: +4
Damage: 5 + 3 + 4 = 12

VAELKE Wound Interval: 13. Previous: 4/13. New: 16/13 → Wound pip +1, WI resets to 3/13.
```

Critical Hit on net ≥ 3: weapon modifier doubles. Damage recalculates, animation brief.

## §7.7 Fibonacci group bonus

When 2+ characters engage one target (melee adjacent), the target hex shows:

```
  ⬡ 𝐕  Vaelke
  [Fibonacci +1D] (2 attackers, unsupported)
```

Movement that ends adjacency removes the bonus, visibly. The player sees consequence of positioning in real time.

## §7.8 Rescue

Rescue is exclusive — one character cannot be the target of two Rescues per round. The UI enforces this by removing Rescue indicators from adjacent hexes after one is declared.

```
Ally E (outnumbered 2+):  🛡 Rescue opportunity — click to commit N dice
```

Committing N dice opens a modal:
```
RESCUE — commit to contest Vaelke's attack redirect to you
Minimum 1 die, maximum your entire Offence pool.
Remaining dice available as Defence against your own engagement only.

Slide commit: [1 ─────● 8]  current 5 dice to Rescue contest, 3 Def remaining

Vaelke will roll her Offence (TN 7); you roll 5D at TN 7; higher net wins.
If you win: her attack redirects to you (armor DR applies; your contest dice expended).
If you lose: her attack resolves on E; your 5 dice wasted; 3 remain for your Def.

[ Confirm ]  [ Cancel ]
```

## §7.9 Death Cascade

On named NPC kill, combat §13.3's five consequences animate in sequence:

Each as its own panel, 1 second apart. Player cannot dismiss. Reads:

1. `KNOT RUPTURE` — list of Knotted NPCs, strain applied to each
2. `SCENE SLATE: GRIEF QUEUE` — NPCs with Disposition ≥ +2 toward the dead generate Priority 1 entries next season
3. `FACTION CONSEQUENCE` — Stability trigger if officer; Succession if leader
4. `EXPOSURE CASCADE` — Exposure +2 in every territory where the dead had ally network; map pulses red in each
5. `YOUR CONVICTION TEST` — any active Conviction relevant to the dead: revise, transform, or abandon at Phase 4

A brief Triangle Strategy-style cutscene fires for Step 5 if the dead was central to a Conviction: the screen dims, the character portrait faces left and right at the moment of reckoning, a chorus swell from the §20 audio system, and the player sees the emotional weight landed. `[SEE §19 for cutscene spec]`.

## §7.10 Sufficient Scope (Domain Echo indicator)

Before the first combat exchange, if the NPC is officer-level or faction-aligned, a banner appears:

```
⚠ SUFFICIENT SCOPE — this combat qualifies as an institutional event
  Victory: target faction Stability −1
  Kill: Stability −1, Mandate −1, Death Cascade fires
  Defeat (you lose): target Mandate +1
  (faction-layer consequences propagate at scene end via Domain Echo)
```

The player knows before rolling. No hidden faction consequences.

---

# PART 8 — MASS COMBAT AND SETTLEMENT INVASION

Authoritative sources: mass_battle_v30.md (full), settlement_layer_v30 §5.

## §8.1 The 16×10 battle map

Larger hex scale. Each hex = formation position (~100–500 soldiers per mass_battle §A.3). Units are represented as painted unit tokens with formation indicators below.

```
╔══════════════════════════════════════════════════════════════════════════╗
║                     BATTLE · Feldmark approach                             ║
║                                                                            ║
║         ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                 ║
║        ⬡ ⬡ [HI] ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ [LI] ⬡ ⬡                               ║
║         ⬡ [HI] ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ [LI] ⬡ ⬡ ⬡                              ║
║        ⬡ [AR] ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ [CV] ⬡ ⬡ ⬡                              ║
║         ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                   ║
║        ⬡ ⬡ ⬡ ⬡ [YOU] ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                  ║
║         ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                   ║
║        ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡ ⬡                                    ║
║                                                                            ║
║  YOUR FORCE (commander: you, Command 4)                                    ║
║  A · HI Size 5 Power 4 Disc 4 Fresh  formation: Line  tactic: Hold        ║
║  B · AR Size 3 Power 3 Disc 3 Fresh  formation: Skirmish  tactic: Volley  ║
║  C · AR Size 3 Power 3 Disc 3 Fresh  formation: Skirmish  tactic: Volley  ║
║                                                                            ║
║  ENEMY (Altonian Vanguard; commander: unknown Command ?)                   ║
║  D · LI Size 4 Power 3 Disc 3 Seasoned                                    ║
║  E · LI Size 4 Power 3 Disc 3 Fresh                                       ║
║  F · CV Size 3 Power 5 Disc 5 Fresh                                       ║
║                                                                            ║
║  Phase 3: Manoeuvre                                                        ║
║  Your turn — move units (Fast→Std→Slow)                                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## §8.2 Phase structure UI

Each of the 7 phases (mass_battle §A.7) presented as a discrete UI step with specific affordances:

- Phase 1 Strategy: sub-unit assignment grid (up to 3 for TTRPG-size), formation dropdown per sub-unit, tactic dropdown, Thread declaration toggle, secret Off/Def split slider
- Phase 2 Volley: projectile units animate, damage recorded not applied yet, sight-line visualizations
- Phase 3 Manoeuvre: unit tokens drag-drop (Fast first, Std second, Slow third), terrain modifiers shown
- Phase 4 Offensive Thread: practitioner panels open if declared; Leap resolves; operation rolls
- Phase 5 Engagement: engaged pair panels with split reveals; General Duel option
- Phase 6 Cascade: simultaneous damage application (all damage lands at once, then Morale / Discipline checks)
- Phase 7 Reform: non-engaged units recover; reserve commitment for next turn

## §8.3 General Duel (Zoom In)

`[RESOLVES UI-09]` partially: settlement capture interrupts use a **side panel** rather than interrupting battle flow. The General Duel does full Zoom In because it is a personal combat embedded in mass combat — a separate tactical space. Settlement capture events (territory transfer mid-battle) fire as a side-panel notification that does NOT interrupt the current Phase — the player acknowledges, the battle continues.

Zoom In to General Duel:

```
╔══════════════════════════════════════════════════════════════════════════╗
║  [mass battle thumbnail (frozen)]   │   PERSONAL COMBAT — General Duel    ║
║    ⬡ ⬡ ⬡                           │                                       ║
║    ⬡ ⬡ ⬡                           │   ╔═════════════════════════╗       ║
║    ⬡ ⬡ ⬡   ← frozen at Phase 5     │   ║ YOUR GENERAL (you)      ║       ║
║                                      │   ║    vs                    ║       ║
║  The mass battle pauses.             │   ║ Altonian Commander      ║       ║
║  1 exchange only.                    │   ║                          ║       ║
║  Command Rating suspended during     │   ║ [12×8 hex grid]         ║       ║
║  duel (mass_battle §A.5).            │   ║                          ║       ║
║                                      │   ║ Wounds persist; +1 Ob   ║       ║
║                                      │   ║ to post-duel tactic     ║       ║
║                                      │   ║ rolls per wound.        ║       ║
║                                      │   ╚═════════════════════════╝       ║
║                                      │   [ Return to mass battle ]        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

One personal combat exchange = one mass combat turn.

## §8.4 Settlement invasion (settlement_layer §5.1)

An invading army engages settlements in sequence. The UI presents this as a progression panel embedded in the province view:

```
╔══ INVASION · T3 LOWENSKYST ═══════════════════════════════════════════════╗
║                                                                            ║
║  INVADER: Altonian Vanguard (6 units, Mil 6)                               ║
║  DEFENDER: Crown garrison                                                  ║
║                                                                            ║
║  SETTLEMENT SEQUENCE (order determined by geography)                       ║
║  ────────────────────                                                      ║
║                                                                            ║
║  ▸ S-006 · Lowenskyst Fortress  [Def 4, Garrison HI×2]                    ║
║    ┌──────────────────────────────────────┐                               ║
║    │ Assault    · Mil 6 vs Def 4 + garr    │                               ║
║    │ Siege      · Mil ≥ Def · Order −1/s   │                               ║
║    │ Bypass     · LOCKED (Mil > Def+3 = 7) │                               ║
║    └──────────────────────────────────────┘                               ║
║    Chokepoint — must engage.                                               ║
║                                                                            ║
║  ▸ S-007 · Lowenskyst Garrison Town  [Def 1, LI×1]                         ║
║    [LOCKED until S-006 engaged]                                            ║
║                                                                            ║
║  ▸ S-008 · Feldmark  [Def 0, unfortified]                                  ║
║    [LOCKED until T3 capital falls]                                         ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

Fortresses are structural. Chokepoints cannot be bypassed unless Military > Defense + 3. The UI makes this visible as locked option.

## §8.5 Post-battle consequence scene

Mass battle §Part D: significant battles generate Priority 0 Slate entries for next Personal Phase. The player experiences the aftermath at personal scale — walking the field, speaking with survivors. This is non-negotiable; the game does not let mass combat be pure abstraction.

If a General Duel occurred, an additional cutscene fires at post-battle per §19 — the survivor stands over the fallen, the sky is low, the clocks pause.

## §8.6 Southernmost constraint

Any unit token dragged toward T15 Askeheim is checked for TS ≥ 30 at the individual level (mass_battle §A.11). Non-qualifying individuals dissolve without awareness; the unit Size reduces proportionally. The UI makes this explicit: dragging a LI unit with 0 TS-capable individuals into Askeheim shows a red × and refuses the drop.

---

# PART 9 — THREADWORK (THE FELT RADICALITY)

Authoritative sources: threadwork_v30.md (full), canon constraints §P-01 (Inseparability), §P-03 (consciousness-performed rendering).

Jordan's requirement: *"we want players to feel threadwork as something so radically unique that it can't quite be captured by any playable character."*

This is the document's hardest design problem. The solution has to be felt, not described. But because this is a reference document, I must describe the felt.

## §9.1 The design argument

Threadwork is not a combat move. It is not a skill with a dice roll attached. It is a fracture in the game's own logic. When a player Leaps, the UI is supposed to feel WRONG in a specific way — not broken, but suspended. The player has stepped outside rendering (per P-03, rendering is consciousness-performed; the Leap suspends the performer's rendering). Everything that was stable becomes tentative. The Thread panel is not an overlay on the game; it is a different game that the player temporarily plays, then returns from.

`[RESOLVES ED-544, the P-03 videogame rendering model]`: the solution is that the UI itself has a different state during Thread contact — a state so different that returning from it feels like waking up.

## §9.2 Thread sight toggle

For characters with TS ≥ 30, a Thread sight toggle exists in the HUD. Enabling it changes the rendering of the current scene:

**Non-Thread mode:**
- Standard illumination
- NPC portraits standard
- Environment solid, consistent, complete

**Thread mode (TS 30+):**
- Environmental shader: subtle geometric highlighting on Thread configurations (cracks in a wall become visible tensile lines; a door's hinge shows the Thread of its repeated opening; a floor stone shows the Thread of footfall history)
- NPC portraits gain a faint aura — if another practitioner, a visible shimmer; if a character with strong Belief-Conviction tension, an inner unrest visible as internal light patterns
- Background audio: a high-frequency underlayer, like distant harmonics — not quite musical, not quite ambient

The toggle is ambient. It does not unlock new actions directly. Its purpose is to reveal — to make visible what was already present to the attuned. This is P-03: rendering is consciousness-performed. A practitioner's consciousness performs more, so they see more.

`[RESOLVES UI-08]`: the Thread sight toggle is **manual** (player-initiated). Making it automatic would flatten the experience — the point of Thread sight is that the practitioner chooses to see. The one exception: when entering a scene with an active Gap or a Thread practitioner in the Depth ≥ 3 range, a prompt appears — "Thread phenomena detected. Switch perception?" — but the switch is still deliberate.

## §9.3 The Leap

When the player initiates a Leap, the UI enters a transition state — a 1.5-second sequence:

```
[screen briefly desaturates]
[audio: the current scene's ambient layer fades]
[a low, vibrating bass-drone enters, barely at hearing threshold]
[the UI elements themselves shift 1–3 pixels in random directions, then resettle]
[the Leap resolution modal appears]
```

This is not a loading screen. This is a rendered event — the character's consciousness suspending its performative engagement with the world. The player feels it.

```
╔══════════════════════════════════════════════════════════════════════════╗
║  THE LEAP                                                                  ║
║                                                                            ║
║   your Approach: Scholarship (learned through study)                       ║
║   your Thread Sensitivity: 42                                              ║
║   your Coherence: 10 / 10                                                  ║
║                                                                            ║
║   pool: (Spirit 4 × 2) + Thread History 2 + TPS 4 = 14D                   ║
║   TN 7 · Ob 2 (for TS 30–49 band) + 0 (no wounds) = 2                     ║
║                                                                            ║
║   if you Leap this round:                                                  ║
║     — you commit all dice to Defence for the Leap round                   ║
║     — ~60% hit probability from any opponent                              ║
║     — contact lasts Focus 4 rounds                                         ║
║     — 3 operations available during contact                               ║
║                                                                            ║
║   you are stepping out of rendering. it will not be quiet here.            ║
║                                                                            ║
║   [ Leap ]    [ Cancel — do not suspend rendering ]                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

The prose "you are stepping out of rendering" is deliberate. The game is explicit about what is happening. This is not a spell. It is a metaphysical act.

## §9.4 The Thread panel (during contact)

Once contact is established, the game's visual register shifts — not catastrophically, but noticeably. The normal scene remains visible beneath, but with:

- A persistent low-frequency visual shimmer across all elements
- Ambient audio replaced with a layered drone (evolving, not static)
- The UI chrome's borders acquire a faint Thread pattern (visible tensile lines, barely perceptible)
- Time feels slower — even though rounds resolve at the same pace, the UI's animation speeds decrease by 20%, making every action feel more deliberate
- Non-practitioner NPCs on screen appear slightly less defined — their Thread aspect dormant, their consciousness unengaged with the substrate

The Thread panel itself overlays the current scene:

```
╔══════════════════════════════════════════════════════════════════════════╗
║  THREAD OPERATIONS · contact rounds 3 / 4                                  ║
║                                                                            ║
║  [ambient: layered drone, slowly evolving]                                 ║
║                                                                            ║
║  COHERENCE  [■■■■■■■■□□]  8 / 10   Stable                                  ║
║  THREAD POOL: (Spirit 4 × 2) + Thread 2 + TPS 4 = 14D                      ║
║                                                                            ║
║  THREE-AXIS Ob BUILDER                                                     ║
║  ──────────                                                                ║
║                                                                            ║
║   DEPTH    [●1]  [●2]  [●3]  [●5]  [●8]  [ 13 ]                           ║
║            surface ─────── buried ──── liminal (locked: TS 70+)           ║
║                                                                            ║
║   BREADTH  [Object]  [Personal]  [Relational]  [Territorial]  [Structural]║
║                                                                            ║
║   DISTANCE [adj] [province] [adj province] [cross-peninsula]              ║
║                                                                            ║
║   current config: Personal · Depth 3 · adj                                ║
║   computed Ob: 4                                                           ║
║                                                                            ║
║  OPERATION                                                                 ║
║  ─────────                                                                 ║
║                                                                            ║
║   ▸ Mending (TN 7)      Ob 4 − 1 = 3  substrate repair                    ║
║   ▸ Weaving (TN 7)      Ob 4  things cohere                                ║
║   ▸ Pulling (TN 7)      Ob 4  things open (loosely actualized)            ║
║   ▸ Locking (TN 8)      Ob 4  forced rigidity · FR surcharge −1 Coh       ║
║   ▸ Dissolution (TN 8)  Ob 4  forced absence · FR surcharge −1 Coh        ║
║   ▸ Past-Oriented Pull  (TN 8) Ob 4 + recency · chronic −1 Coh            ║
║                                                                            ║
║  MS COST PREVIEW                                                           ║
║   Overwhelming: MS +1 (Weaving only, Relational+)                         ║
║   Success: MS 0                                                           ║
║   Partial: MS −2 (Personal scale)                                         ║
║   Failure: MS −3 (Personal scale)                                         ║
║                                                                            ║
║   ⚠ at Structural scale Failure: MS −8 to −12 (catastrophic)              ║
║                                                                            ║
║  COHERENCE COST: −1 (Personal scale auto)                                 ║
║                                                                            ║
║  CO-MOVEMENT fires after operation: all three axes (P-01)                 ║
║                                                                            ║
║  [ CAST ]   [ Cancel — remain in contact without operating ]               ║
╚══════════════════════════════════════════════════════════════════════════╝
```

Every number the player needs is shown BEFORE commit. No hidden costs. This is Oath II.

## §9.5 Co-movement (mandatory display)

After every operation, the co-movement panel takes over. It is NOT dismissable for at least 3 seconds. Co-movement is the Valoria experience — Thread operations are never just their primary effect; they always move the world in three dimensions.

```
╔══════════════════════════════════════════════════════════════════════════╗
║  CO-MOVEMENT · your Pulling operation succeeded                            ║
║                                                                            ║
║  The substrate responded in three dimensions.                              ║
║                                                                            ║
║  ─── TEMPORAL ────────────────────────────────────────────                ║
║    Calamity Drift: +1 (deferred to Phase 3 Cascade)                       ║
║    History Resonance: a flash — Vaelke's grandmother                      ║
║      (Mode 2 Providence event, brief)                                     ║
║                                                                            ║
║  ─── EPISTEMIC ───────────────────────────────────────────                ║
║    Vaelke's Certainty: 3 → 2 (she sensed something)                       ║
║    Clerk of Seals (nearby, non-sensitive) experiences an                  ║
║      involuntary perceptual moment. Inert Knowledge forms.                ║
║                                                                            ║
║  ─── ACTUALIZED ──────────────────────────────────────────                ║
║    Co-Movement Card drawn: Substrate Settling                             ║
║    Effect: Thread ops in this settlement −1 Ob next season               ║
║                                                                            ║
║  [ acknowledge — 3 second minimum read time ]                              ║
╚══════════════════════════════════════════════════════════════════════════╝
```

## §9.6 MS environmental rendering

Per calamity_radiation_v30, MS band state has territory-specific effects. The UI renders these as environmental shifts visible on the Peninsula map and within settlements:

| MS Band | Peninsula map | Settlement interior | Audio |
|---------|---------------|--------------------|----|
| 100–80 Stable | Warm painted palette, clear lighting | Soft, grounded, natural ambient | Clean chamber music |
| 79–60 Strained | Slight muting, edges less crisp | Occasional flicker in torch flames | Underlayer of distant harmonics |
| 59–40 Fragile | Shifting-Object animations on high-traffic Thread territories | Objects in locations very subtly mispositioned | Detuned accompaniment |
| 39–20 Fractured | Gap overlays visible on map; territorial Fort Level rumors | Strong color aberration, memory inconsistency | Dissonant bass drone |
| 19–1 Critical | Map aberration; territory tint shifts unpredictably | Full rendering failures — the vignette itself wrong | Terror bed: low-frequency rumble, occasional sub-audible pulse |
| 0 Rupture | (campaign over — cutscene fires) | — | — |

The Peninsula map breathes with MS. A game played at MS 85 feels completely different from one played at MS 25 — not because the rules changed, but because the world literally renders differently.

## §9.7 Coherence and rendering corruption

Per threadwork §3.3, Coherence thresholds trigger UI dysfunction at low values:

| Coherence | UI state |
|-----------|----------|
| 10–8 Stable | Normal |
| 7–5 Dissonant | Very occasional UI element 1-pixel jitter; minor ambient shift |
| 4–3 Fragmented | Menus occasionally flicker; dialogue text has one-word displacements; minor color aberration |
| 2 Fractured | HEAVY aberration, dialogue options appear/disappear briefly, Beliefs show in a ghostly second version representing the shifted framework |
| 1 Severed | The UI fights the player; menus rearrange between clicks; audio drops out briefly |
| 0 Crisis | Campaign event — mandatory narrative resolution scene per threadwork §3.3 |

`[RESOLVES UI-11]`: dialogue internal-voice rendering is always present when a Conviction-row option is relevant (the italic subtext appears beneath the option). No Spirit check required. The Spirit-gated versions are the Thread-specific internal voices — which show when Coherence ≤ 5 or when in Thread contact. The normal Conviction internal voices are always present because they represent the character's self-awareness, not Thread perception.

## §9.8 Knot visualization

A Knot with another character is visualized as a thin silver thread between the player portrait and the Knotted NPC's portrait — visible on the companion strip (§2.5), on the NPC's character sheet, and briefly during any scene where the Knotted NPC is present.

Knot strain pips show beside the thread. When strain accumulates, the thread color shifts from silver toward gold (wrongness), then red (rupture imminent). A ruptured Knot triggers a cutscene — see §19.

## §9.9 Why this is "radically unique"

Threadwork in Valoria cannot be "just another skill" because:

1. **The game's visual/audio register changes** for Thread operations — not as a special effect, but as a structural shift. You literally perceive differently.
2. **Co-movement is mandatory** — you do not get to "just cast the spell." Every operation costs in three dimensions, visibly, with animations you cannot skip.
3. **The UI itself degrades at low Coherence** — the interface you trust becomes unreliable. You are no longer the secure operator of a game; you are the character struggling to hold their rendering together.
4. **Structural-scale operations can END the game** — MS 0 = Rupture = campaign over. Threadwork is the only mechanic that carries this weight, and the UI surfaces that weight pre-roll every time.
5. **Non-practitioners cannot access this UI at all.** A character with TS < 30 has no Thread panel, no Thread sight toggle, no Leap option in combat. The ENTIRE Thread layer is invisible to them. This is the mechanical expression of P-08 (epistemological barrier): non-sensitives literally cannot perceive what sensitives perceive.

The player who plays a non-sensitive character sees the Peninsula as a solid, legible place. The player who plays a sensitive character sees the same Peninsula as a configuration. Both are playing the same game; neither is playing the full game.

---
## §20.3 Layer 3 — haptic-equivalent (visceral, rare), continued

- **Critical hit:** screen flash white for 50ms, heavy low-end thud
- **Death (combat §7.9 Stage 2 failure):** screen briefly pulses red; a heavy bell tolls
- **Conviction scar:** the UI frame jitters for 300ms, a faint glass-cracking audio
- **Knot strain (major):** the Knot thread visible in the companion strip visibly frays; audio is a low hum increasing in pitch
- **Knot rupture:** cutscene (§19)
- **Sufficient Scope Domain Echo:** the Peninsula map in the chrome-reduced header flashes; the affected factions' colors pulse; an audio chord lands — the composition of the chord encodes direction (ascending for gain, descending for loss)
- **Band transition (any clock):** the clock bar pulses with its band's characteristic color; ambient underscore shifts in register; a single low bell for downward transitions, a single high bell for upward

## §20.4 Layer 4 — threadwork-radical (the fracture)

This layer is what makes threadwork uncapturable by any playable character. It is the interface itself becoming a different interface.

Triggered by:
- Active Thread contact (§9.4 Thread panel)
- Coherence ≤ 5 (§9.7 UI corruption)
- MS ≤ 40 inside Calamity-proximate territories (§9.6)

**During Thread contact, the entire game register shifts:**

- Animation speeds decrease 20% across all UI — every click takes a beat longer to respond. The world is slower because the player has stepped out of it.
- A persistent low-frequency drone replaces ambient audio. The drone evolves — it is not static; it responds to the Thread operation being considered (Weaving: rising; Pulling: falling; Locking: a sustained tone; Dissolution: a descending gliss).
- The UI frame itself acquires Thread-tensile lines, barely perceptible, as if the chrome were made of thread
- Non-practitioner NPC portraits desaturate slightly — their dormancy relative to the substrate becomes visible
- Operations panel (§9.4) has a different typography — older, heavier, with illuminated initial letters for each operation name

**At Coherence 4 (Fragmented):**

- Menus occasionally flicker; a menu item appears for 50ms that was not supposed to be there ("?" or a single glyph from another language, then gone)
- Dialogue text has rare one-word displacements (a word that was "truth" reads as "truth*" for a frame, where * is a Thread-glyph)
- Ambient audio: a high-frequency overlay — the consciousness-performed rendering of sound becoming imperfect

**At Coherence 2 (Fractured):**

- Heavy color aberration on the peripheral UI
- The player's Beliefs show in a ghostly second version above each Belief — what the transforming framework would revise them to
- Convictions occasionally flicker between their current text and a subtly altered text representing the framework-drift
- Scene transitions take an extra 200ms and feel wrong — the animation pauses briefly before completing
- During combat: the hex grid's geometry has a barely-perceptible wobble

**At Coherence 1 (Severed):**

- The UI fights the player. Menus rearrange between clicks (never in a way that prevents action, but in a way that unsettles). Audio drops briefly to silence at unexpected moments.
- The character portrait in the HUD occasionally blinks to a different version — aged, diseased, or dissolved
- Rendering failure becomes the rule: scene backgrounds have brief dropouts (1 frame of black, then recovery)

**At Coherence 0 (Rendering Crisis):**

- Full cutscene fires (§19) — the Rendering Crisis scene. The character's narrative recovery path opens. This is the threshold at which Valoria becomes a different game for that character.

## §20.5 Layer integration

The four layers are not independent. Layer 1 (ambient) is always present and is modulated by Layer 4 (threadwork-radical) when active. Layer 2 (cue) fires on discrete events regardless of other layers. Layer 3 (haptic-equivalent) takes precedence over Layers 1–2 for its brief duration. Layer 4, when active, dampens Layer 2 cues (they become slightly muffled — the world is less crisp).

The player should never consciously think "this is Layer 2." They should feel the game respond.

## §20.6 The Peninsula's pulse

A final ambient layer: the Peninsula map, when viewed, has a subtle visual "breathing" — a 6-second cycle where the colors of faction territories gently pulse in their own faction rhythms (Crown: slow; Church: regular procession; Varfell: irregular, rustic; Hafenmark: measured parliamentary; Löwenritter: martial drumbeat; RM: communal; Niflhel: erratic; Guilds: counting-house regular).

The pulse is slowest at high Accord and fastest at low Accord. At Accord 0 (revolt), the pulse is agitated. This is the peninsula showing the player its mood without showing a number.

---

# PART 21 — THE CODEX, JOURNAL, ACCOUNTING SCROLL, AND SUPPLEMENTARY SCREENS

Valoria generates dense state. The player needs reference surfaces to navigate their own history.

## §21.1 The Codex

Accessible from any layer via the hamburger menu or `K` key.

The Codex is the game's encyclopedia — but not a flat wiki. It is organized by engagement: entries appear and become fully legible as the player encounters the subject.

```
╔══════════════════════════════════════════════════════════════════════════╗
║  CODEX                                          Season 12 · Year 3        ║
║                                                                            ║
║  ┌─────────────┬────────────────────────────────────────────────┐        ║
║  │ CATEGORIES  │  CROWN                                          │        ║
║  │             │                                                  │        ║
║  │ ▸ Factions  │  [painted illustration: Crown royal regalia]    │        ║
║  │   Crown ●   │                                                  │        ║
║  │   Church ◐  │  First encountered: Season 1, Year 1            │        ║
║  │   Hafen ◐   │                                                  │        ║
║  │   Varfell ○ │  Ethical Framework: Virtue Ethics                │        ║
║  │   L-R ○     │  Victory Path: Peninsula Sovereignty             │        ║
║  │   RM ○      │                                                  │        ║
║  │   Guilds ○  │  CURRENT STATE (Fog of War reduced visibility)  │        ║
║  │   Niflhel 🔒│   Mandate: Good (4–5)                            │        ║
║  │   Wardens 🔒│   Influence: Good                                │        ║
║  │             │   Wealth: Poor                                   │        ║
║  │ ▸ NPCs      │   Military: Good                                 │        ║
║  │   Almud ●   │   Intel: Hidden                                  │        ║
║  │   Torben ●  │   Stability: Good                                │        ║
║  │   Arne ◐    │                                                  │        ║
║  │   ...       │  LEADERSHIP                                       │        ║
║  │             │   King Almud Almqvist (Conviction: Order)        │        ║
║  │ ▸ Terr.     │   Crown Prince Torben (Conviction: Autonomy)    │        ║
║  │   T1 ●      │                                                  │        ║
║  │   T2 ◐      │  ORIGIN                                           │        ║
║  │   T3 ●      │   Founded during the post-Calamity reunification ║
║  │   ...       │   ... [revealed through Research at Archives]    │        ║
║  │             │                                                  │        ║
║  │ ▸ Clocks    │  CUTSCENE HISTORY                                 │        ║
║  │ ▸ Mechanics │   1 cutscene featuring Crown (rewatch →)         │        ║
║  │ ▸ Cutscenes │                                                  │        ║
║  │ ▸ Lore      │                                                  │        ║
║  │             │                                                  │        ║
║  └─────────────┴────────────────────────────────────────────────┘        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

Entry states:
- ● Fully known — encountered and engaged extensively
- ◐ Partially known — encountered but not deeply engaged
- ○ Heard of — mentioned but not encountered
- 🔒 Unknown — has not entered player awareness yet

The Codex is the reference for the world, and it respects the player's epistemic position. It shows what they know and flags what they do not. Rumors and Inert Knowledge appear in a "Fragments" section of relevant entries — things you have heard but cannot verify.

## §21.2 The Journal

Already described in §4.5. The primary investigation-tracking surface. Accessible via `J`.

## §21.3 The Accounting Scroll

Fires at Phase 3 Cascade. An illuminated scroll unrolls down the screen, with each of the 5 Cascade steps writing themselves in period calligraphy.

```
[Scroll unrolls; text appears as if written in real time with a quill]

         ACCOUNTING · Winter · Year 3

  Step 1 — Domain Echoes from Personal Phase
    Crown · Mandate +1 (Grand Contest decisive win, Projection genre)
    Hafenmark · Mandate −1 (same event, target)

  Step 2 — Thread operation clock changes
    MS: no personal-phase Thread operations this season
    CI: unchanged

  Step 3 — Clock threshold events
    CI from 51 → 52 (passive +1, Church Mandate ≥ 3)
    IP from 41 → 43 (inter-faction battle in T3)
    No band transitions this season

  Step 4 — Board order consequences
    Crown Muster in T1: unit raised (LI, Size 3, Power 3)
    Church Assert: CI +1 (folded into Step 3 above)
    Hafenmark Trade: Wealth +1
    Varfell Intel: +1 Intel (T12 revealed)

  Step 5 — Accounting
    13 sub-steps ran. No Stability failures this season.
    Peninsular Strain: 2 (stable)
    Victory progress: 3 of 4 for Crown; T5 Accord must recover.

[Scroll finishes writing; pause 3 seconds; scroll rolls up]
```

The calligraphy and scroll metaphor make what would otherwise be a spreadsheet-like info-dump into a weighty ritual. The player watches the season close.

Duration: 60–120 seconds depending on how many changes. Skippable after first campaign via Settings.

## §21.4 The Relationships screen

Accessible from the character sheet or `R` key. A tableau of every NPC the character has significant relationship with.

```
╔══════════════════════════════════════════════════════════════════════════╗
║  RELATIONSHIPS                                                             ║
║                                                                            ║
║  COMPANIONS                                                                ║
║  [Eira portrait] [ Eira : Equity ]  Disp +4  Knot ●  strain 0/5            ║
║    last spoken: this season · next free action: Social                    ║
║                                                                            ║
║  [Tamm portrait] [ Tamm : Order ]   Disp +3  no Knot                      ║
║    last spoken: 2 seasons ago · risk of drift                             ║
║                                                                            ║
║  NAMED NPCs                                                                ║
║  [Almud] [ Almud : Order ]      Disp +2      your faction leader           ║
║  [Torben] [ Torben : Autonomy ] Disp +1      subject of Conviction B       ║
║  [Baralta] [ Baralta : Precedent ] Disp −2   contest rival                 ║
║  [Vaynard] [ Vaynard : Reason ] Disp 0       investigating                 ║
║  [Vossen] [ Vossen : Reason ]   Disp +2      potential Thread ally         ║
║                                                                            ║
║  KNOTS (complete)                                                          ║
║  Eira · active                                                            ║
║                                                                            ║
║  OBLIGATIONS                                                               ║
║  Crown: no Altonian marriage talks for Torben · 2 seasons                 ║
║  You: help rescue Eira's sister in T17 · no deadline                      ║
║                                                                            ║
║  CONVICTION SCARS YOU HAVE CAUSED                                          ║
║  Almud: 1 scar on Order    (from Royal Audience season 10)                ║
║  Baralta: 1 scar on Precedent (from treasury Grand Contest season 12)     ║
║                                                                            ║
║  CONVICTION SCARS ON YOU                                                   ║
║  Conviction A (Thread/Almud): ●○○                                          ║
║  Conviction B (Torben):        ●●○ ⚠                                       ║
║  Conviction C (Thread allies): ●○○                                         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

This is the character's social/relational dashboard. One screen, all the people who matter.

## §21.5 The Map overlay

Full-screen Peninsula view accessible from `M` key. Same Peninsula as the main map but full-screen with overlay toggles:

- Show faction control
- Show Accord
- Show Framework Drift
- Show MS gradient
- Show IP threat vectors
- Show player presence history (where you have been this campaign)
- Show NPC positions (named NPCs you know about)
- Show trade routes
- Show Church influence (Piety Track + Theocracy)
- Show Thread configurations (TS 30+ player only)

Each toggle layers additional information. Players can build their own view of the peninsula.

## §21.6 The Options menu

Accessible from anywhere via ESC or hamburger menu.

- **Display:** resolution, fullscreen, UI scale (§22), colorblind mode, motion reduction
- **Audio:** master, music, dialogue, ambient, UI cues — each with slider
- **Gameplay:** difficulty (Narrative / Normal / Hard), tooltip verbosity, cutscene skip behavior, Accounting Scroll autoplay
- **Controls:** keyboard remapping (§22), mouse sensitivity, controller remapping
- **Accessibility:** text size, high-contrast UI, screen-reader support, cutscene subtitles on/off/forced
- **Save / Load:** 10 rolling slots + 3 manual + export savefile

---

# PART 22 — ACCESSIBILITY, INPUT, AND RESOLUTION SCALING

## §22.1 Input methods

Supported:
- Keyboard + mouse (primary)
- Controller (Xbox / PlayStation / generic HID)
- Touch (tablet; not optimized for phone)

Every action in the game is performable with any input method. No keyboard-only or mouse-only flows.

### §22.1.1 Keyboard shortcuts (default)

| Key | Action |
|-----|--------|
| J | Journal |
| K | Codex |
| C | Character sheet |
| M | Map (full-screen) |
| V | Victory progress |
| R | Relationships |
| T | Thread sight toggle (if TS 30+) |
| ESC | Menu / pause / cancel |
| Space | Confirm / next |
| 1–9 | Action panel option 1–9 |
| Tab | Switch between Slate / chrome focus |
| Shift+Click | Archive Slate entry |

All remappable in Settings.

### §22.1.2 Controller mapping

- D-pad: menu navigation
- A: confirm
- B: cancel
- X: alternate action (Thread sight, secondary)
- Y: menu hub
- L/R bumpers: cycle between chrome regions (right rail / left panel / main view)
- L/R triggers: zoom out / zoom in
- Start: pause menu
- Select: Codex

### §22.1.3 Touch

Settlement and Peninsula layers support pinch-zoom and drag-pan. Combat hex grid supports tap-to-move, drag-to-attack. Dialogue options are tap-to-select. The chrome regions (right rail, companion strip) are persistent but collapse to edge tabs when screen space is constrained.

## §22.2 Resolution scaling

Target: 1920×1080 native. Scales down to 1280×720 minimum. Scales up to 3840×2160 with UI element size preserved (UI does not become tiny at 4K — it preserves absolute pixel sizes and adds white-space).

UI scale setting: 75% / 100% / 125% / 150% / 200%. All text and iconography scales. The Peninsula map and combat grid scale independently — they always fill available space.

Tablet portrait mode: not supported in v1. Tablet landscape: full support.

## §22.3 Accessibility features

- **Colorblind modes:** Deuteranopia / Protanopia / Tritanopia filters. Faction colors and band indicators have secondary encoding (shape / pattern) that does not rely on color alone.
- **High contrast:** bolder borders, stronger background-foreground separation, larger type.
- **Motion reduction:** suppresses most ambient animations (NPC breathing, Peninsula pulse, Framework Drift pulse). Cutscenes still play (they are content). Layer 4 threadwork effects reduced in intensity.
- **Text size:** 75% / 100% / 125% / 150% / 200%.
- **Screen-reader support:** every UI element has an accessible label. Dice roll results narrate on completion. Cutscenes have full text narration option.
- **Cutscene subtitles:** on by default. Large-text option available.
- **Dyslexia-friendly font option** (OpenDyslexic or equivalent).
- **Reduced flicker:** Coherence ≤ 2 UI corruption effects can be disabled entirely for photosensitivity. The mechanical effect remains but the visual degradation is replaced with a persistent warning banner.

## §22.4 Minimum specifications

- 4GB RAM
- GPU supporting Vulkan 1.1 (Godot 4 requirement)
- 8GB storage
- 1280×720 display

Target specifications:
- 8GB RAM
- GPU mid-range (GTX 1060 / RX 580 / integrated Iris Xe or better)
- 16GB storage (with extended cutscene assets)
- 1920×1080 display

---

# PART 23 — PRECEDENT ATTRIBUTION

Every design decision draws from specific precedent games. This section is the index.

| Precedent | What we take | Applied to |
|-----------|--------------|-----------|
| **Disco Elysium** | Conviction-gated dialogue options; internal voices; interpretation-as-play; skill-as-perspective | Part 5 (full), Part 13 (Independence path), Part 19 (cutscene text register) |
| **Pentiment** | Investigation-as-social-act; painted illustrated NPCs with subtle animation; location-list settlement interior; dialogue-driven prosecution; text calligraphy | Part 4, Part 16 (Inquisition), §3.4 settlement interior, §19 cutscene typography |
| **Crusader Kings III** | Vassal-tier agency; council mechanics with priority evaluation; settlement-county-duchy hierarchy; succession tension | Part 11 (Stature-gated faction access), Part 12 (Governor Panel), Part 13 (Stature ladder) |
| **Darklands** | Location-list settlement interior; chapter-book readability; long-horizon character sheet | §3.4, Part 13 (character sheet), Part 21 (Codex as illuminated reference) |
| **Pathologic 2** | Triage-as-gameplay; irreversible consequence; time-as-scarce; emotional weight of choosing what to miss | §1 (scene action budget), §2.6 (Slate dock), Part 10 (integrated loop) |
| **Mount & Blade / Manor Lords** | Emergent stature progression; visible settlement development | §12.5 (emergence ladder) |
| **Romance of the Three Kingdoms** | Officer-city assignment; promotion track; faction management at officer level | §11 (Stature gates), §12 (Governor Panel), §13 (Renown track) |
| **Total War** | Strategic map with battle interludes; campaign-to-battle zoom | Part 3 (zoom), Part 8 (mass combat) |
| **King of Dragon Pass** | Seasonal narrative events; faction-mat strategic play; phase structure | Part 1 (season architecture), Part 11 (hand panel) |
| **XCOM 2** | Hex combat action-declaration clarity; turn-based tactical grid | Part 7 (personal combat hex grid), §7.4 declaration UI |
| **Battle Brothers** | Medieval reach zones; wound persistence; zone-based combat geometry | Part 7 (reach rules visualization, Wound tracking) |
| **Control** | Altered-reality rendering for perception; deliberately wrong geometry | Part 9 (Thread sight toggle), §20.4 (threadwork-radical layer) |
| **Dragon Age / Tyranny** | 2–3 companion sweet spot; companion commentary | Part 14 (party cap of 2), §2.5 (companion strip), §4.4 companion §4.4 Slate commentary |
| **Case of the Golden Idol** | Evidence synthesis on a deduction board; Reconstruct as arrangement | §4.6 (Reconstruct surface) |
| **Final Fantasy Tactics** | Painted cutscene backgrounds; character portrait framing; orchestral leitmotif | Part 19 (cutscene anatomy) |
| **Triangle Strategy** | Conviction-driven narrative branching at key decisions; painted cutscene aesthetic; multi-character scene framing | Part 19 (full), §19.6 (text registers), Part 11 (hand panel art direction) |
| **Soundtrack reference: Final Fantasy XII** | Orchestral underscore with motif layering for political vs personal scenes | §20.1 (ambient), §19 (cutscene music) |

No single game is the model. Valoria's UI is the overlap of CK3's council politics, Pentiment's social-act investigation, Disco Elysium's perceptual ambience, Darklands' settlement readability, Pathologic's triage weight, ROTK's officer-to-leader emergence, Triangle Strategy's painted cutscene register, and Control's interface-as-metaphysical-status.

---

# PART 24 — GODOT IMPLEMENTATION REFERENCE

This part is the developer-facing section. Designers can skip.

## §24.1 Engine version and architecture

- Godot 4.2+ (Vulkan-based renderer)
- Primary language: GDScript (core systems, UI)
- Secondary: C# (performance-critical — combat resolution, cascade evaluation)
- Asset format: .tres (Godot resource), .tscn (scene), .png (art), .ogg (audio)

## §24.2 Scene tree top-level structure

```
Main (Node)
├── GameState (autoloaded singleton)
│   ├── Campaign (Resource)
│   ├── Season (Resource)
│   ├── World (Resource)
│   ├── Player (Resource)
│   ├── Factions (Dictionary<FactionId, FactionState>)
│   ├── Companions (Array<CompanionState>, max 2)
│   ├── Clocks (Resource)
│   ├── Investigations (Array<Investigation>)
│   ├── Journal (Resource)
│   ├── Codex (Resource)
│   ├── SlatePending (Array<SlateEntry>)
│   └── PendingCutscenes (Array<CutsceneRef>)
├── SignalBus (autoloaded singleton)
│   └── All typed signals (see §24.4)
├── ChromeRoot (CanvasLayer, always visible)
│   ├── TopBar (Breadcrumb, SceneActionCounter, Menu)
│   ├── RightRail (Clocks, Drift, Stature, Convictions, Obligations, Duty)
│   ├── LeftContext (layer-specific)
│   ├── CompanionStrip
│   └── SlateDock
├── LayerStack (Node, z-ordered)
│   ├── PeninsulaLayer
│   ├── ProvinceLayer
│   ├── SettlementLayer
│   ├── SceneLayer (fieldwork, dialogue, contest, combat, threadwork)
│   └── CutsceneLayer (on top of everything)
├── DiceEngine (Node)
│   └── Roll evaluator
├── RNGManager (autoloaded; single seed per campaign for reproducibility)
├── AudioDirector (Node; manages layered audio)
├── SaveManager (Node)
└── EventLog (Node; for Codex history and replay)
```

## §24.3 Core resources

```
Resource: Attribute
  name: String
  value: int (1-7)
  modifiers: Array<Modifier>

Resource: Character
  attributes: Dictionary<String, Attribute>
  histories: Dictionary<String, int>
  derived: Dictionary<String, int>  // computed from attrs+histories
  convictions: Array<Conviction, max 3>
  beliefs: Array<Belief, max 5>
  knots: Array<KnotRef>
  duty: Duty | null
  obligations: Array<Obligation>
  wounds: int
  wound_interval_current: int
  max_wounds: int
  stamina_current: int
  composure_current: int
  rattled_marks: int
  coherence_current: int
  thread_sensitivity: int
  scene_action_budget_base: int
  combat_reputation: int

Resource: Conviction
  text: String
  scars: int (0-3)
  relevance_keywords: Array<String>

Resource: StanceTriangle  // for NPCs
  primary_conviction: enum {Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity}
  secondary_conviction: enum
  ethical_framework: enum {VirtueEthics, CategoricalImperative, DivineCommand, Consequentialism}
  primary_resonant_style: enum {Evidence, Consequence, Authority, Solidarity}
  secondary_resonant_style: enum
  beliefs: Array<Belief, max 5>
  scars_by_conviction: Dictionary<ConvictionEnum, int>

Resource: Faction
  id: FactionId
  mandate: int (0-7)
  influence: int (0-7)
  wealth: int (0-7)
  military: int (0-7)
  intel: int (0-7)
  stability: int (0-7)
  hand: Array<Card>
  cooldowns: Dictionary<CardType, int>
  territories_controlled: Array<TerritoryId>
  casus_belli: Array<CasusBelliRef>

Resource: Territory
  id: String (T1-T17)
  controller: FactionId
  accord: int (0-5)
  cv: int
  pt: int
  fort_level: int (0-4)
  exposure_per_player: Dictionary<CharacterId, int>  // resets per season per territory
  calamity_proximity: enum {Distant, Near, Close, Adjacent, Askeheim}
  settlements: Array<SettlementId>

Resource: Settlement
  id: String (S-001 to S-036)
  type: enum {Seat, City, Town, Village, Outpost, Fortress, Mine, Port, Cathedral}
  prosperity: int
  defense: int
  order: int
  controller: FactionId
  governor: NPCId | PlayerCharacterId
  subnational_presences: Array<SubnationalRef>
  covert_presences: Array<CovertRef>  // hidden until revealed

Resource: Investigation
  question: String
  threshold: int (3, 5, or 8)
  threshold_hidden: bool
  evidence: Array<Evidence>
  status: enum {Open, DesperateTrail, Resolved, Closed}
  finding: Finding | null

Resource: SlateEntry
  priority: int (0-4)
  summary: String
  anchor_location: LocationRef
  relevant_convictions: Array<ConvictionRef>  // player convictions this scene relates to
  companion_commentary: Array<CompanionCommentary>
  generated_at: Season
  resolved: bool
  pursuit_cost: int  // scene actions

Resource: CutsceneRef
  id: String
  trigger_source: String  // e.g., "knot_rupture:eira"
  shortened: bool  // true if not first occurrence
  priority: int  // determines queue ordering
```

## §24.4 Signal bus

Core signals (emitted by GameState, consumed by UI):

```
signal phase_changed(old_phase, new_phase)
signal scene_entered(scene_ref)
signal scene_resolved(scene_ref, result)
signal roll_started(pool, target, context)
signal roll_completed(pool, results, net_successes, degree)
signal evidence_added(investigation_id, evidence_ref)
signal investigation_resolved(investigation_id, finding)
signal disposition_changed(npc_id, old, new)
signal conviction_scar_added(character_id, conviction_index, new_count)
signal belief_revised(character_id, belief_index, old, new)
signal belief_pressure_added(npc_id, belief_index, new_count)
signal belief_scarred(npc_id, belief_index)  // pressure=3
signal knot_formed(char_a, char_b)
signal knot_strained(knot_id, strain_delta)
signal knot_ruptured(knot_id)
signal domain_echo_fired(source_scene, faction_effects)
signal sufficient_scope_evaluated(scene_ref, qualifies)
signal clock_changed(clock_name, old, new)
signal clock_band_transitioned(clock_name, old_band, new_band)
signal rs_threshold_crossed(direction, new_band)
signal coherence_degraded(character_id, old_coherence, new_coherence)
signal thread_contact_entered(character_id, contact_rounds)
signal thread_operation_resolved(operation_type, scale, degree, consequences)
signal co_movement_fired(temporal_axis, epistemic_axis, actualized_axis)
signal slate_generated(entries)
signal slate_entry_selected(entry_id)
signal slate_entry_archived(entry_id)
signal companion_joined(companion_id)
signal companion_departed(companion_id, reason)
signal companion_free_action_used(companion_id, type)  // Social or Governance
signal cutscene_queued(cutscene_ref)
signal cutscene_started(cutscene_ref)
signal cutscene_ended(cutscene_ref)
signal stature_changed(character_id, faction_id, old, new)
signal renown_changed(character_id, old, new)
signal settlement_event_fired(settlement_id, event_type)
signal combat_initiated(scene_ref, participants)
signal combat_resolved(scene_ref, outcomes)
signal contest_initiated(scene_ref, proceeding_type, exchange_count)
signal contest_resolved(scene_ref, final_track, winner, obligation)
signal parliament_motion_declared(motion_ref)
signal parliament_vote_resolved(motion_ref, tally, passed)
signal treaty_phase_advanced(treaty_ref, phase)
signal faction_emergence_stage_changed(faction_id, old_stage, new_stage)
signal faction_collapsed(faction_id)
signal victory_condition_met(faction_id, condition)
signal rupture_imminent()  // MS 0
signal rupture_occurred()  // campaign ends
```

UI nodes subscribe to only the signals relevant to them. No polling.

## §24.5 Persistent chrome implementation

```
ChromeRoot (CanvasLayer layer=10, always visible except during cutscenes)
├── TopBar (HBoxContainer)
│   ├── BreadcrumbTrail (custom node, updates on scene_entered)
│   ├── SeasonDisplay (Label, updates on phase_changed)
│   ├── SceneActionCounter (custom node, updates on scene_resolved)
│   └── MenuButton (opens hamburger menu)
├── RightRail (VBoxContainer, fixed width 280)
│   ├── ClocksPanel (4 ClockBars stacked)
│   ├── DriftStrip (FactionDriftRow array)
│   ├── StaturePanel (StandingDisplay + RenownBar)
│   ├── ConvictionsPanel (3 ConvictionCards stacked)
│   ├── ObligationsPanel (Array<ObligationCard>)
│   └── DutyPanel (DutyCard)
├── LeftContext (VBoxContainer, fixed width 240)
│   └── (content swapped by layer_stack.current_layer signal)
├── CompanionStrip (HBoxContainer, bottom, fixed height 120)
│   └── (up to 2 CompanionSlots)
└── SlateDock (custom node, left edge, collapsible)
```

Cutscene shown: ChromeRoot fades to alpha 0 for 1.0s; cutscene layer renders; on cutscene end, ChromeRoot fades back in over 1.0s.

## §24.6 Dice engine

```
class DiceEngine:
  static func roll_pool(pool_size: int, tn: int = 7, context: RollContext) -> RollResult:
    # Emit roll_started signal
    # For each die: roll d10
    # Count hits (≥ TN), count 10s as double-hits (chained dice), count 1s (penalty)
    # net_successes = hits + 10s_bonus − 1s_count (floor 0 in some contexts)
    # Compare to Ob → degree (Failure / Partial / Success / Overwhelming)
    # Emit roll_completed signal
    # Return RollResult
```

RollResult includes the individual die values (for visualization), net_successes, degree, and any context-specific data (Reputation bonus, chained-dice count, etc.).

Animation duration: 1.2s base + 80ms per die. A 20-die roll takes ~2.8 seconds to visualize.

## §24.7 State machine implementation

The phase state machine is implemented as a finite state machine with explicit transitions:

```
class PhaseStateMachine:
  signal phase_changed(from, to)
  
  var current: PhaseEnum = PhaseEnum.MAIN_MENU
  
  var legal_transitions = {
    PhaseEnum.MAIN_MENU: [PhaseEnum.CHARACTER_CREATION, PhaseEnum.LOAD],
    PhaseEnum.CHARACTER_CREATION: [PhaseEnum.BRIEFING],
    PhaseEnum.BRIEFING: [PhaseEnum.DUTY_ASSIGNMENT],
    PhaseEnum.DUTY_ASSIGNMENT: [PhaseEnum.SLATE_REVEAL],
    PhaseEnum.SLATE_REVEAL: [PhaseEnum.PERSONAL],
    PhaseEnum.PERSONAL: [PhaseEnum.STRATEGIC, PhaseEnum.CUTSCENE],
    PhaseEnum.STRATEGIC: [PhaseEnum.CASCADE, PhaseEnum.CUTSCENE],
    PhaseEnum.CASCADE: [PhaseEnum.AFTERMATH, PhaseEnum.CUTSCENE],
    PhaseEnum.AFTERMATH: [PhaseEnum.BRIEFING, PhaseEnum.ENDGAME, PhaseEnum.CUTSCENE],
    PhaseEnum.CUTSCENE: [<preceding phase>],  // returns to whence it came
    PhaseEnum.ENDGAME: [PhaseEnum.MAIN_MENU]
  }
  
  func transition_to(target: PhaseEnum) -> bool:
    if target in legal_transitions[current]:
      emit_signal("phase_changed", current, target)
      current = target
      return true
    return false
```

## §24.8 Asset manifest (outline)

Required art assets for v1:

- 17 territory illustrations (Peninsula map base)
- 36 settlement vignettes (location list backgrounds)
- ~40 named NPC portraits (half-body, 3 expression states each)
- ~80 location interior vignettes (settlement locations)
- 9 faction hand panel card arts (Legionary, Senator, Consul, Tribune, Pontifex, Prefect, Recess, Policy, Parliamentary Manoeuvre) × 8 factions = 72 card arts (many shared)
- Cutscene backgrounds: 40+ painted scenes (per §19.2 trigger list)
- UI iconography: ~120 icons (stat, clock, action, condition, Conviction, Belief)
- Peninsula map shader variants (MS band states × 5)

Required audio assets:

- Main theme + 8 faction themes (Crown, Church, Hafenmark, Varfell, Löwenritter, RM, Guilds, Niflhel — Wardens share a theme with Edeyja-specific variant)
- 12 NPC leitmotifs for major named NPCs
- Combat loop (3 variations)
- Contest loop
- Threadwork drone (base + 5 operation-type variants)
- Cutscene orchestral stems (modular for mixing)
- UI cue library (~40 cues for rolls, transitions, notifications)
- Settlement ambient (9 type variants × dawn/noon/dusk/night)

This manifest is a starting count. Fully scoped asset list lives in a separate Godot dev document (to be created when asset pipeline begins).

## §24.9 Save system

Save on phase boundaries only. One save file per slot; manual saves export to a separate export location.

Save format: Godot binary (`.sav` extension) with version header. Campaign state is serialized via Godot's ResourceSaver API. Backward compatibility: version header allows migration paths if save format changes post-release.

Critical rule: no saves within atomic scene resolutions. Once a roll has started, the game cannot be reloaded to re-roll. This is philosophical as well as practical — Valoria's d10 engine is non-deterministic and meant to be lived with.

## §24.10 Cutscene implementation

Cutscenes are scripted Timeline resources. Each cutscene is a `Cutscene.tres` file describing:

- Background painting reference
- Character portrait sequence (who enters when, from which side, at what position)
- Dialog beats (text + voice-over audio + calligraphy font + duration)
- Music track reference
- Phase-boundary return target

The CutsceneLayer plays a Timeline deterministically. Player input during cutscene is limited to pause / skip (post-first-viewing).

Cutscene scripting is data-driven — designers author Cutscene resources in the Godot editor using a custom inspector plugin. This lets writing happen in text files, not code.

## §24.11 Deterministic RNG

All rolls use a seeded PCG RNG per campaign. Seed is saved with the campaign. This means:

- Two players starting the same seed with the same choices will see the same rolls
- Reloading a save does not re-roll resolved outcomes (the RNG state is saved)
- Combat rolls, contest rolls, Thread rolls, NPC decision rolls all draw from the same sequence

This enables reproducibility testing and makes bugs diagnosable. It also prevents save-scumming of rolls.

---

# PART 25 — RESOLVED ITEMS INDEX

All UI-01 through UI-15 items from v3 resolved in this document. Summary index with back-references.

| ID | Question | Resolution | Location |
|----|----------|-----------|----------|
| UI-01 | Combat grid size | 12×8 standard, 16×10 set-piece, never below 10×6 or above 20×12 | §7.4 |
| UI-02 | Hand panel card visual | Iconic card art, Triangle Strategy / illuminated manuscript aesthetic; symbolic icon + typography + stat line + readiness state | §11.2 |
| UI-03 | Involuntary Thread perception | Implemented as ambient glyph flickers during Coherence ≤ 5 and as Thread sight reveal in specific high-MS territories | §9.2, §9.7 |
| UI-04 | Slate volume at Hard difficulty | 9 entries at Hard; manageable because of tiered visibility (priority markers collapse to edge at a glance) and companion commentary that annotates 1–2 per season | §2.6 |
| UI-05 | Obligation panel placement | Dedicated block in right rail; expandable on click; no separate top-level screen | §2.3.5 |
| UI-06 | Framework Drift pulse intensity | 80% alpha at 1.2s cycle; perceptible but not distracting. MS band shader intensity scales with band severity | §2.3.2, §20.1 |
| UI-07 | Panel adjudicator type | Upstream ED-137 dependency persists; the UI is designed to accept any of Panel / Individual / Crowd adjudicators by changing the venue illustration and voting mechanic | §15 (deferred to ED-137 resolution) |
| UI-08 | Thread sight toggle default | Manual; player-initiated. One exception: prompt appears when entering scene with active Gap or Depth ≥ 3 Thread phenomena | §9.2 |
| UI-09 | Settlement capture interrupt handling | Side panel notification, not battle interruption. General Duel still does full Zoom In (it IS personal combat) | §8.3 |
| UI-10 | Companion arc phase visibility | Tiered: Knot status always visible; public arc phase always visible; private arc phase reveals via Connect success | §14.3 |
| UI-11 | Internal voice rendering | Always present when Conviction-row option is relevant; no Spirit check required. Thread-specific internal voices only at Coherence ≤ 5 or in Thread contact | §5.5, §9.7 |
| UI-12 | Reconstruct board layout | Template per investigation type (3 / 5 / 8 slots); scaffolds structure while preserving the pinboard metaphor | §4.6 |
| UI-13 | Parliament interface | Dual-view: top-down tally + first-person chamber cutaway; switches automatically at key moments (Veto, Rebuttal, Total Victory) | §15.1 |
| UI-14 | Companion governance animation | Brief Phase 3 animation of the governance roll (2-second overlay); 4-second cutaway if Overwhelming or band transition | §12.2 |
| UI-15 | Covert Niflhel reveal cue | Always-ambient `?` entry in province panel; only Cognition 3+ parses it as specific cue | §3.3 |

Plus two ED-level resolutions:

| ID | Question | Resolution |
|----|----------|-----------|
| ED-544 | P-03 videogame rendering model | The depth-access perception gate is the rendering model; Thread sight toggle + environmental shaders enforce P-03; sensitivity-gated information IS the mechanic, not an overlay |
| ED-545 | Only 5 Zoom In triggers for 120+ arcs | The Scene Slate is the Zoom In trigger system. Any arc moment fires as a Priority 0 (mandatory) or Priority 1 (optional) Slate entry. This multiplies Zoom In pathways to 120+ without bespoke trigger code |

Plus Jordan's Health correction:

| ID | Question | Resolution |
|----|----------|-----------|
| ED-548 | Wound Interval formula | `Wound Interval = Endurance + 6`; wound every WI damage; Total Capacity = WI × (Max Wounds + 1). Applied to combat_v30 §7, propagated throughout this document |

---

# CLOSING

The v30 rulesets specify what Valoria IS. This document specifies how Valoria MEETS the player.

Central design argument: mutual constitution, made legible. Four layers (faction, settlement, NPC, player) are bidirectionally coupled. The UI's job is to make every coupling visible without flattening it.

Four felt registers:

1. **The persistent chrome IS the game's commitment to the player** — your Convictions, your Obligations, your Duty, your clocks, your companions are always present. You are never lost.

2. **The Scene Slate IS the world talking to you** — each season you see what's demanding attention. You choose. What you miss resolves through NPC AI. Triage is the game.

3. **Threadwork IS the fracture that cannot be captured** — the UI itself changes when you cross into Thread contact. The game you play for 99% of the time is not the game you play during a Leap. Non-practitioners never see this layer at all. Per P-03, rendering is consciousness-performed; a non-sensitive character's consciousness does not perform the Thread, and the UI reflects that by literally not showing it.

4. **Cutscenes ARE the emotional rendering** — when the game must carry weight that a number cannot carry, the painted backgrounds, the orchestral swell, the character portraits facing each other in silence: this is how Valoria says "this mattered." The cutscene is the game's acknowledgment that the player is owed more than a notification.

Every question the player might ask has an interface:

- *Where am I?* — breadcrumb and Peninsula map
- *What's happening this season?* — Scene Slate and right rail
- *What do I want?* — Convictions (always visible)
- *What does my faction want?* — Duty (always visible)
- *What am I bound to?* — Obligations (right rail)
- *Who walks with me?* — Companion strip
- *What do I remember?* — Journal + Codex
- *What did I just do?* — Phase 3 Accounting Scroll
- *What comes next?* — Phase 1b Slate Reveal

Every transition is smooth. Every state change is felt before it is announced. Every roll is transparent. Every consequence ripples visibly. Every Conviction limits what you say; every Conviction makes new things sayable.

This is the game. This is the document the Godot team can build from.

---

**END OF v4 REFERENCE DOCUMENT**

*Audit coverage: 19 v30 canonical design documents + ED-548 Health correction.*
*Resolutions: UI-01 through UI-15 (all 15), plus ED-544, ED-545, ED-548.*
*New editorial items introduced: zero.*
*Pages: ~90 at standard markdown rendering.*
*Status: CANONICAL; approved for Godot development reference use.*
