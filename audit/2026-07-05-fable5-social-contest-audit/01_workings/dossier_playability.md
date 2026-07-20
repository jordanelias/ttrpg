# Dossier — Playability / Player-Experience Evidence (Agent D, sonnet tier)
## Status: WORKING EVIDENCE — no verdicts; judgment reserved to the orchestrator
## Date: 2026-07-05

---

## Part 1 — The dramatic-legibility three-question walk, per game-shape

**Canonical bar** (`designs/audit/workplan_v2_throughline_2026-04-26.md:209`): "Playability confirms
the experience works: can a designer read the game-state and answer 'whose position is at risk, what
each actor wants, what happens if no one acts'? This is Q-robust's dramatic legibility test, which
requires a human and a screen." (Exit criteria, line 234: "A designer plays one season and answers
the three dramatic-legibility questions correctly from the screen.")

### 1a. Agôn — walkthrough §0 principle and screen inventory

`designs/audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md:19-24` (§0):
> "Every number the resolver uses to decide the outcome is a number the player can see before they
> commit to a choice that depends on it. This is the direct answer to the stated core pain (opacity):
> not 'hide less,' but 'the hidden-GM-ledger and the player-facing screen are the same data, rendered.'
> Where the *resolved value* is legitimately hidden ... the player still gets the *consequence class*."

Screen inventory the walkthrough specifies (all cited `path:line` within the same file):
- **Setup (§1, lines 30-45):** Venue, Adjudicator type, own pool composition, both-directions stakes,
  Persuasion Track start + all 5 bands, banked Appraise hints — "the direct translation of v30 §2
  'GM Setup'... confirming the GM-removal mandate is satisfiable" (line 43-45).
- **Exchange loop (§2, lines 48-115):** Appraise 4-band ladder (lines 54-61), Style cards with grounded
  flavor + visible pool/boost preview (lines 66-79), Roll & resolve screen naming CLASH/REINFORCE/
  CROSS/TIE in plain language plus margin/resistance/Doubt Marker (lines 81-96), two persistent Face/
  Concentration bars with exact penalty text on threshold (lines 98-108), conditional Forfeit/Regroup
  button with both branches shown (lines 110-114).
- **Resolution (§3, lines 118-134):** headline banner off final Track band, every consequence traced to
  its emitted Key (Obligation terms, Domain Echo grant, Conviction Scar kept deliberately unexposed per
  `§6.2 ED-1042`, Contest Fatigue/Chain scheduling).

Applying the three questions to this screen set:
| Q | Answerable from the walkthrough's designed screens? | Cite |
|---|---|---|
| (i) whose position is at risk | Yes — Persuasion Track meter with drawn bands (≤1/≤3/4-6/≥7/≥9) shown from setup and animated live each exchange; Face bar shows standing buffer | walkthrough_v1.md:40, 93-94, 100-108 |
| (ii) what each actor wants | Partial — stakes both directions shown at setup (win/lose/draw text, line 39); adjudicator armature (what moves the judge) is only *coarsely* revealed by design (Partial/Success/Overwhelming bands), residual deliberately stays hidden | walkthrough_v1.md:39; `social_contest_v30.md:177` ("No band ever reveals the judge's exact per-axis weights... a legitimate source of tension") |
| (iii) what happens if no one acts | Yes — Forfeit/Regroup screen shows "both branches' consequences shown side by side (continue vs. regroup)" when live; Chain Contest / Deadlock rules (compromise stall) are specified even if not yet in a screen mock | walkthrough_v1.md:110-114; `social_contest_v30.md §6.3` (365-369) |

Corroborating lineage — PR #77's independent lens result:
`designs/audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_playability_legibility.md:75-79`:
> "**Social contest:** PASS — for Agôn only. The walkthrough's §0 principle ('every number the resolver
> uses is a number the player can see before committing') makes all three answerable, and hidden values
> (opponent Face, adjudicator convictions) degrade to a *consequence class* (Appraise hint / debuff
> icon), which is the correct legibility discipline. But 3 of 4 games raise NotImplementedError, so the
> test literally cannot be run for Negotiation/Inquiry/Consensus."

### 1b. Negotiation / Inquiry / Consensus — what the docs give a player to read

No dedicated walkthrough exists for these three (walkthrough_v1.md §4, lines 137-153, sketches intended
divergent UI shapes — offer-panel/ZOPA, belief-alignment meter, per-assenter roster — as **not yet
built**, explicitly flagged "so Stage 2-4 don't lock in an Agôn-only UI"). Evaluated per question against
what currently exists in prose + code:

| Game | (i) whose position at risk | (ii) what each actor wants | (iii) what happens if no one acts | Basis |
|---|---|---|---|---|
| Negotiation (ZOPA) | N-A — no ZOPA/offer-bracket UI spec exists; `social_contest_v30.md §2 Step 4` line 92 only says "Persuasion Track is optional" for no-adjudicator format | N-A — no BATNA-range display spec | Answerable-from-doc only in narrative-flavor form: `social_contest_v30.md:93` "the contest stalls: strain persists, all Read results ... become permanent knowledge... The narrative moves forward" — this is prose, not a screen | `params/contest.md:184-213` lists Private Negotiation/Personal Appeal as proceedings, but `wrapper.py:211-212` marks `negotiation` a STUB ("author-new — later stage") |
| Inquiry (truth) | N-A-because-unbuilt — Church Tribunal proceeding exists mechanically (asymmetric resistance, biased Track start at 6) but no "belief-alignment meter per contested proposition" UI exists | Partial from prose only — `social_contest_v30.md §7` (376-384) states Inquisitor's institutional bias in text form, not a UI read | N-A — no inquiry-specific consequence screen; general Obligation/Heresy Investigation lifecycle (§7.3) is prose-specified but not player-screen-specified | `wrapper.py:213-214` marks `inquiry` a STUB ("author-new — later stage") |
| Consensus (holdout) | N-A-because-unbuilt — no per-assenter roster exists; BG Parliamentary Vote (§10) exposes only aggregate Mandate-pool sums, not individual holdouts | Answerable only via `params/contest.md` faction ethical-mode table (line 68-79 region of `social_contest_v30.md`, "Church/Divine Command/Obscuring" etc.) as flavor text, not a live UI panel | N-A — no consensus-specific "if no one acts" text found | `wrapper.py:209-210` marks `consensus` a STUB ("largely in faction.py — Stage 4") |

**Player-facing proceeding flavor** (the one player-facing copy layer that DOES exist for all 8
proceedings, including the ones whose *game* is unbuilt): `params/contest.md:198-213` (ED-1058) —
e.g. "Private Negotiation | Just the two of you, up to three rounds, no judge and no fixed scorekeeping.
Read them well, because failing to agree is its own answer." This gives setup-screen flavor for
Negotiation/Inquiry-adjacent proceedings, but flavor text is not a per-exchange interaction model — it
answers none of the three legibility questions mid-contest.

`wrapper.py` GAMES-stub notes (exact text, lines 199-215):
```
def _stub(game):
    def _f(contest, **kw):
        raise NotImplementedError(
            f"resolve_contest: game={game!r} is a registered STUB (Stage 1c) — not yet wired. "
            f"Only game='agon' resolves this stage (see DECISIONS.md Stage-1 entry criteria).")
    return _f

GAMES = {
    "agon":        {"resolve": _resolve_agon,          "status": "WIRED", ...},
    "consensus":   {"resolve": _stub("consensus"),     "status": "STUB",
                    "source": "social_contest_v30 §10 BG-Vote / §7.2 (largely in faction.py — Stage 4)"},
    "negotiation": {"resolve": _stub("negotiation"),   "status": "STUB",
                    "source": "social_contest_v30 §2 Private Negotiation (author-new — later stage)"},
    "inquiry":     {"resolve": _stub("inquiry"),       "status": "STUB",
                    "source": "social_contest_v30 §7 Church Tribunal / Inquisition (author-new — later stage)"},
}
```

### Part 1 summary table — 4 games × 3 questions

| Game | (i) whose position at risk | (ii) what each actor wants | (iii) what happens if no one acts |
|---|---|---|---|
| **Agôn** | answerable (Persuasion Track + bands, Face bar) | partial (stakes shown; armature convictions deliberately residual-hidden) | answerable (Forfeit/Regroup dual-consequence screen; Chain/Deadlock rules) |
| **Negotiation** | N-A-because-unbuilt (no ZOPA UI; resolver STUB) | N-A-because-unbuilt | answerable only as prose narrative outcome (stall text), not a screen |
| **Inquiry** | N-A-because-unbuilt (no belief-meter UI; resolver STUB) | partial-from-prose only (Inquisitor bias stated in doc text) | N-A-because-unbuilt |
| **Consensus** | N-A-because-unbuilt (no holdout-roster UI; resolver STUB) | answerable only as flavor/ethical-mode table text | N-A-because-unbuilt |

---

## Part 2 — Cognitive-load count for one Agôn exchange

**Ceiling** (`designs/audit/2026-05-08-meta-audit-immersion.md:64`, §4 "Am I pulled out by mechanics?"):
> "Seven per-decision consultations is tractable for strategic decisions. For personal-scale dialogue
> — where immersion matters most — it's too many. DE's personal-scale per-decision surface is 3–4.
> Valoria should aim for 3–4 in personal scenes: Conviction voice intrusion + player's dialogue choice
> + consequence."
And §5 finding 2 (line 82): "Personal-scale per-decision surface should be 3–4, not 7... For
personal-scale scenes ... the engine should handle more silently."

### Enumeration — every distinct quantity/table to make ONE exchange decision (choose style + commit dice)

**(a) Must-consult every single exchange** (recur each of the `exchange_count` repetitions):
1. Own current pool size (Primary Attribute × 2 + History bonus) — `social_contest_v30.md:119`
2. TN (7 standard, situational 6/8) — `social_contest_v30.md:128`
3. Genre bonus (+1D if matching live stasis's primary genre) — `social_contest_v30.md:58,66`
4. Audience/faction boost table (which of 7 factions boosts which axis) — `social_contest_v30.md:68-79`
5. Adjudicator armature reveal state (coarse register/dominant axis/strength band from Appraise, four
   axes Evidence/Consequence/Authority/Insinuation) — `social_contest_v30.md:171-178`
6. Opponent's Face (bar, within Charisma-ceiling) — `social_contest_v30.md:236-239`, walkthrough §2
   Step 4 (lines 98-108)
7. Own Face / Standing position and Rattled threshold — same cites
8. Own Concentration (stamina bar, depletion −5/exchange) and Spent state — `social_contest_v30.md:256-259`
9. Persuasion Track current position + band zone — `social_contest_v30.md:90-92`, walkthrough §1 (line 40)
10. Current Doubt Marker state (present/absent, which side) — `social_contest_v30.md:210-217`
11. Interaction-type prediction (CLASH/REINFORCE/CROSS/TIE depending on own+predicted opponent genre/
    orientation) — `social_contest_v30.md §4 Step 4` (lines 179-224), named in plain language per
    walkthrough (lines 87-90)
12. Recall availability (whether a not-yet-cited source remains, esp. Grand Contest's once-per-source
    rule) — `social_contest_v30.md:166-168`
13. Momentum available to spend (auto-successes) — `social_contest_v30.md:169`

**(b) Consult once-per-contest** (fixed at setup, not re-checked per exchange):
14. Venue/exchange_count and role structure — `social_contest_v30.md §2 Step 5` (95-106)
15. Adjudicator type (fixes primary attribute for the whole contest) — `social_contest_v30.md §2 Step 1`
16. Stasis start / genre-primary mapping (fixed per proceeding, only shifts upward) — `social_contest_v30.md:48-60`
17. Stakes (win/lose/draw text) — `social_contest_v30.md §2 Step 6`
18. Starting Persuasion Track position + audience resistance — `social_contest_v30.md §2 Step 4`
19. Pre-Contest Preparation / Evidence Track Findings bonus, if used — `social_contest_v30.md §9.1`

**(c) Optional / situational** (not consulted every exchange, only when the option is live):
20. Corroborate (declare support, Ob 1 vs Ob 2 by Knot status) — `social_contest_v30.md §4 Step 2b`
21. Forfeit options (Regroup vs Concede a Point vs continue) — `social_contest_v30.md §4 Step 5`, only
    "offered when it is a live choice" per walkthrough (line 111)
22. Practitioner Weaving (TS≥30 bonus dice) — `social_contest_v30.md §9.3` (R-65)
23. Thread Operations Between Exchanges + temporal-axis conflict — `social_contest_v30.md §9.4/§9.4b`

**Count:** 13 items in group (a) that recur *every single exchange* to make the two-part decision
(style pick + commit dice) — more than 3x the 3-4 ceiling the immersion audit sets for personal scenes,
and above even the "7 at ceiling" figure that audit reserves for *strategic*-layer decisions. Groups
(b) and (c) add a further 6 and 4 items respectively, though these do not recur every exchange.

### What the walkthrough's screen design does to compress this

- Face and Concentration collapse tracker items #6-8 into "two persistent bars... not a single hidden
  'stamina' number" (walkthrough_v1.md:100-108) — a visual compression of 3 raw numbers into 2 bars
  with threshold-triggered banner text, rather than requiring the player to do threshold arithmetic.
- The interaction-type prediction (#11) is pre-computed and named in plain language post-roll ("Direct
  Clash," "Mutual Reinforcement," etc., lines 87-90) rather than left for the player to derive from the
  CLASH/REINFORCE/CROSS/TIE rule table before committing — this converts a *pre-commit* calculation
  into a *post-roll* readout, which reduces the count of items needed strictly to decide, but the Style
  cards (§2 Step 2, lines 66-79) still ask the player to weigh "any active faction/adjudicator boost it
  is known ... to hit or miss" before rolling — i.e., items #3-5 are still pre-commit knowledge, only
  #11 is deferred to post-roll.
- Style cards are framed as "Four cards, not a dropdown" with grounded flavor (line 68), folding the
  Genre×Orientation matrix (4 combinations) into a single named choice rather than two separate
  genre/orientation picks — a UI compression of what §4 Step 2 specifies as two independent picks
  (`social_contest_v30.md:157`, "Each orator selects a genre... and an orientation... as a single style
  pick").
- The walkthrough does not describe any compression for items #1-2 (pool/TN) or #9-10,12-13 (Track/
  Doubt Marker/Recall/Momentum) beyond stating they are shown; no aggregate "recommended play" or
  single dashboard number is proposed that would reduce the consult-count below the enumerated items.

---

## Part 3 — Coverage and staleness evidence

### 3.1 Walkthrough coverage vs the 8 proceedings

The walkthrough is explicitly scoped: "for the one game that is fully built (Agôn/Formal Contest)"
(walkthrough_v1.md:12-13), and its screen inventory is drawn from the Formal Contest / generic Agôn
exchange loop, not proceeding-specific variants (Church Tribunal asymmetry, Panel VoteAtClose, etc. are
not separately walked through). 8 proceedings exist per `params/contest.md:184-194` (Formal Contest,
Grand Contest, Royal Audience, Church Tribunal, Guild Arbitration, Casual Dispute, Private Negotiation,
Personal Appeal) — all resolve through the single wired `agon` GAMES entry per `wrapper.py:207-208`, so
the walkthrough's Agôn coverage nominally spans all 8 proceeding *skins*, but its screen mocks (Style
cards, Face/Concentration bars, Doubt Marker icon) are drawn generically and do not separately depict
the asymmetric-proceeding variants (Royal Audience Crown-objects framing, Church Tribunal Inquisitor-
proposes framing, Panel per-member ballot) called out in `social_contest_v30.md §7`.

PR #77 F-3 (`designs/audit/2026-07-04-ners-qualitative-audit/ners_qualitative_audit_v1.md:148-157`):
> "**F-3 · The playability bar has no maintained home** `[Q-robust · P2 · backwards · UNDETERMINED]`
> The only comprehensive player-facing spec (`designs/ui/valoria_ui_ux_v4_1.md`, CANONICAL,
> 2026-04-16) predates the entire v40 generation, is absent from CURRENT.md (no UI/legibility row
> exists), still specifies player-facing tracks canon has STRUCK (Taint 0–6, CD), and its 69-finding
> / 20-P1 repair workplan (v4.2) was never executed. The only current-era interaction artifact is the
> DRAFT one-subsystem contest walkthrough."

### 3.2 UI spec `designs/ui/valoria_ui_ux_v4_1.md` — social-contest/debate screens

Located at Part 6 (lines 592-649), "PART 6 — SOCIAL CONTEST," authoritative source cited as
`social_contest_v30.md (full)`. Contest interface, quoted (§6.1, lines 598-613):
> "Contest opening: NPC Stance Triangle revealed, Piety Track displayed, exchange count set, player's
> opening bonuses (preparation, Findings).
> Each exchange: 1. Appraise (both orators roll Attunement) 2. Style selection (Memory/Projection ×
> Revealing/Obscuring) 3. Corroborate (companion assist) 4. Evidence citation (Finding from Journal if
> available) 5. Resonant Style targeting (+1D on match to NPC's revealed styles) 6. Argue roll (pool
> assembles visibly with bonuses) 7. Resolution (CLASH / REINFORCE / CROSS / TIE) 8. Composure damage
> 9. Doubt Markers / Obscuring effects 10. Next exchange or final resolution."

Also §6.2-6.6 (lines 616-647): Parliament chamber view + lobbying-as-personal-contest (620), Inquisition
Hearing asymmetric register (622-628), Royal Audience (630-632), Treaty/Grand Debate three-phase
structure (634-641, "This is the game's central vertical"), Chain contests (645-647).

**Staleness evidence, direct in the v4.1 text itself:** the interface names "**Piety Track** displayed"
and step 8 "**Composure** damage" — but the current canonical `social_contest_v30.md` §8 (line 481,
CR3, RATIFIED 2026-06-01) states Composure is **retired as the social-contest tracker**, split into
Concentration + Face; the tracker the current spec displays is the **Persuasion Track** (§2 Step 4,
line 89-92), not a "Piety Track." Neither "Piety Track" nor "Stance Triangle" appears anywhere in
`social_contest_v30.md`'s eleven sections (per the full read of that file, offsets 1-711).

PR #77's lens on staleness/contamination (`lens_playability_legibility.md:32-42`):
> "v4.1 §9.7/§9.8/§10.2/§11.3 still specify **Taint** (a separate 0–6 track) and a **CD track** as
> player-facing. Canon STRUCK both... So a Godot developer building the character sheet from the
> canonical UI reference renders two trackers that do not exist." (These specific struck-tracker
> citations are for character-sheet sections, not Part 6 directly, but establish the general staleness
> pattern the same lens applies to the whole v4.1 doc, including Part 6's stale "Piety Track"/
> "Composure" terms found directly above.)

Same lens, on currency-index absence and never-executed v4_2 (`lens_playability_legibility.md:12-25`):
> "A large **CANONICAL** player-facing spec exists — `designs/ui/valoria_ui_ux_v4_1.md`... but: It
> predates the ENTIRE current generation... It is **absent from `CURRENT.md`** entirely... Its own
> repair workplan `designs/ui/valoria_ui_ux_v4_2_workplan.md` (69 findings, **20 P1**) targets a
> replacement `valoria_ui_ux_v4_2.md` that **was never created** (dir listing: only the workplan
> exists). Last substantive git touch of v4.1 = 2026-06-28 bulk workplan commit, not content."

### 3.3 Board-game §10 + Hybrid §11 — player action and visible state

**§10 BG Parliamentary Vote** (`social_contest_v30.md:575-597`): player actions per turn are: (1) declare
Side A/B or Abstain (579), (2) declare one genre (580), (3) prior-season Diplomacy-action lobbying
offsets the starting Track within a capped 4-6 compromise-zone band (582-585, ED-621). Resolution itself
(587-596) is a single combined-pool roll with no further player decision inside the vote — visible state
is the Persuasion Track (5±lobbying) and the pass/fail/committee bands. No per-exchange interaction loop
comparable to §4 exists at BG scale; "Thread consequences do not fire from BG Parliamentary Vote" (596).

**§10.1 Parliamentary Stay** (ED-631, lines 633-645): a Side-A-vs-Church BG vote gated on CI<55; player
action is the same BG-vote mechanism, visible state is CI value vs the 55 threshold and season-count of
the suspension window.

**§11 Hybrid Contest** (601-607): player actions are (1) run one BG Vote round (§10) producing a capped
±2 offset, (2) then run a standard TTRPG personal contest (Formal/Grand, §§4-7) from the adjusted
starting position. Visible state is the same BG Track/genre declaration plus the full personal-contest
exchange loop once escalated.

**Evidence for interaction-spec depth beyond the design doc:** no walkthrough, no wrapper.py resolver
path, and no UI-spec section beyond v4.1 §6.2/§6.5 (already flagged stale above) was found describing
BG-Vote or Hybrid player screens; `wrapper.py`'s GAMES table marks `consensus` (the BG/faction-vote game
shape) as STUB with source note "largely in faction.py — Stage 4" (`wrapper.py:209-210`), i.e. the BG
Parliamentary Vote described in prose has no current resolver wiring of its own distinct from the
stubbed `consensus` game.

### 3.4 Choice-density lineage — PR #77 dossier decision-point table (verbatim wording)

`designs/audit/2026-07-04-ners-qualitative-audit/01_workings/dossiers/dossier_social_contest.json`,
`decision_points` array (quoted, file's own wording):

- Style pick: `"where": "Step 2 Style pick (Genre x Orientation, 4 cards)"`, `"meaningful": "moderate"`,
  `"note": "genre half wired via CR4 stasis; orientation's CR5 risk/reward (Doubt Marker + self-Face
  backfire) is design-table only, not resolver-consumed yet"`.
- Appraise + armature-informed style choice: `"meaningful": "rich"`, `"note": "continuous delta-sigma
  leverage, never a lookup table"`.
- Forfeit: `"meaningful": "moderate"`.
- **Which of the four games to engage:** `"where": "which of the four games to engage (Agon/
  Negotiation/Inquiry/Consensus)"`, `"options": "proceeding type implies a game"`, `"meaningful":
  "degenerate"`, `"note": "only Agon is wired; the other three raise NotImplementedError (Stage 4 not
  yet built) - KNOWN-TRACKED"`.
- Obligation naming: `"meaningful": "rich"`.
- Corroborate: `"meaningful": "moderate"`.
- Recall citation: `"meaningful": "thin"`, `"note": "near-costless in per-exchange (Formal) form;
  degenerate-leaning"`.
- Proceeding/venue selection: `"meaningful": "thin"`, `"options": "context-determined, not really
  player-chosen"`.

The same file's `legibility` field: `"answerable": "partial"`, `"note": "Yes for an Agon-shaped
proceeding... No for Negotiation/Inquiry/Consensus - those game states don't exist yet
(NotImplementedError), so the test can't be run against them."` And `north_star.verdict`: "the
executable slice is currently one game wearing eight venue skins, so today's realized choice density is
narrower than the design promises."

### 3.5 Onboarding/complexity-gating evidence

Searched `designs/` (case-insensitive) for `tutorial|onboard|first-time|learn` in the context of the
contest system specifically. Findings:
- No hit for `tutorial` or `onboard` inside `designs/architecture/cogload_moderate_target.md` (the
  cognitive-load doc most likely to gate contest complexity by player experience level).
- `designs/architecture/player_agency_v30.md:482` contains one onboarding reference, but it is
  character-creation-scoped, not contest-scoped: `[EDITORIAL: ED-659 — Character creation caste +
  viability onboarding applied PP-661.]` — this is about caste/viability at character creation, not
  sequencing how a player learns the contest system's mechanics.
- No file was found that sequences a contest-specific tutorial (a first-Appraise walkthrough, a
  reduced-complexity first contest, a gated introduction of Style cards before the full armature/
  Doubt-Marker/Chain-Contest stack). The walkthrough itself (`player_interaction_walkthrough_v1.md`)
  is a single fully-loaded exchange-loop spec with no stated "first contest is simplified" provision.
- No complexity-gating mechanism (e.g., "armature reveal disabled until X," "Doubt Marker introduced
  only after N contests") was found anywhere the searches above touched.

**Absence, not evidence of a specific doc:** based on the searches run (`tutorial|onboard` across
`designs/`, `cogload_moderate_target.md`, `player_agency_v30.md`), no doc was found that sequences how
a player learns the social-contest system specifically.

---

## Anomalies noticed in passing

- `designs/ui/valoria_ui_ux_v4_1.md:600` names "**Piety Track**" as the contest-opening tracker where
  the current canonical spec (`social_contest_v30.md:89-92`) uses "**Persuasion Track**" — a direct
  terminology mismatch between the CANONICAL-status UI doc and the CANONICAL-status mechanical spec,
  beyond the Taint/CD staleness PR #77 already flagged elsewhere in the same UI doc.
- `designs/ui/valoria_ui_ux_v4_1.md:610` step 8 "Composure damage" names a tracker retired by CR3
  (`social_contest_v30.md:481`, RATIFIED 2026-06-01) — the UI spec's per-exchange step list has not
  been updated to the three-tracker (Concentration/Face/Persuasion Track) model at all, not just the
  character-sheet contamination PR #77 cited.
- The walkthrough (`player_interaction_walkthrough_v1.md`) and the params flavor-text table
  (`params/contest.md:198-213`, ED-1058) are both current-era, player-facing, Agôn/proceeding-setup
  artifacts that appear not to cross-reference each other — the walkthrough's §1 Setup screen
  (line 30-45) does not cite the ED-1058 flavor-text table as its "Venue"/"Adjudicator type" row
  source, despite the flavor table being the more recently-dated (Stage 2/Gate B) player-facing copy
  layer for exactly that screen.
- The Adjudicator Armature's Appraise partial-reveal boundary (`social_contest_v30.md:177`, "No band
  ever reveals the judge's exact per-axis weights") is framed by the same doc as a *deliberate*
  legibility exception ("a legitimate source of tension, not an opacity bug") — this is the one place
  in the Agôn design that the walkthrough's own §5 open-questions section (lines 161-165) flags as
  needing "the antagonist [to] distinguish it from an opacity finding," i.e. the design doc itself
  anticipates this could be mis-read as a Part-1 legibility failure and pre-empts that reading.
- Grand Contest's Recall exhaustion rule (`social_contest_v30.md:168`, ED-617, "once per cited source
  for the entire contest") is a per-exchange consult item (#12 in Part 2) whose state (which sources
  are already exhausted) has no cited UI representation anywhere read for this dossier — neither the
  walkthrough nor v4.1 depict a "sources already cited" tracker, despite the rule requiring the player
  to remember it across up to 5 exchanges.
