# Open Editorial Items — Jordan Decision Docket

## Status: PROPOSAL DOCKET — **nothing here ratifies on merge** (ED-1094 exception, called out loudly). Every recommendation below awaits Jordan's explicit pick. Merging this PR files the docket as a proposal artifact; it does NOT flip any `needs_jordan` flag, `status`, or `CURRENT.md` row. · Lane: IN (cross-cutting) · Date: 2026-07-08

**What this is.** A single consolidated recommendation surface for **all 32 open `needs_jordan: true`
editorial items** in `canon/editorial_ledger.jsonl` (as of 2026-07-08). Jordan asked for
"editorial content / infill / resolutions / suggestions / recommendations for all open editorial
items that require my decisions, based upon precedent, previous work, shape and intent." This docket
delivers exactly that: for each item it states the **fork**, a **recommendation** with its grounding,
and the **consequence** of adopting it.

**How to rule.** Read the summary table, then the per-item sections. For each item, reply with your
pick (adopt the recommendation / choose the alternative / defer). A follow-on execution pass then
files each ruling under its owning lane per the session-lane-scoping convention (CLAUDE.md §3–4),
citing this docket as provenance. Recommendations that only *propagate* an already-made ruling are
marked as such and can be executed as a `[cleanup]` batch.

**Discipline.** Every numeric value below is a **shape proposal**, not a ledger constant — any number
crossing into `sim/` routes through a seeded calibration run first (CLAUDE.md §5/§7). Historical
citations ground the *mechanism*, never the magnitude. No mechanic is fabricated: where nothing
grounds a resolution, the item says "strike / defer," not an invented rule.

---

## Summary table — 32 items, clustered

| # | ID | Cluster | The fork, in one line | Recommendation |
|---|---|---|---|---|
| 1 | ED-SC-0003 | A · Social contest P0 | Name the 0–10 debate tracker (Piety vs Persuasion) + its home doc | **"Persuasion Track", home = `social_contest_v30.md`**; scope-tag the 0–5 territorial "Piety Track" |
| 2 | ED-SC-0004 | A · Social contest P0 | Canon Argue-pool `(Primary×2)+History−Wounds+fatigue, floor 1` vs kernel `[SEED]` `max(5, faculty·2+3)` | **Keep the canon formula**; retire the `[SEED]`; tag `RES_FLOOR` `[SEED]` pending calibration |
| 3 | ED-SC-0005 | A · Social contest P0 | Numeric cap on the Recall/Corroborate/Prep/Findings bonus stack | **+3D combined cap, Findings included** (Option B — reuses the doc's own worked ceiling) |
| 4 | ED-SC-0015 | B · Parliamentary | Total-victory Sanction: stack two −1 Mandate hits to −2, or cap at −1 | **Cap at −1 (lex specialis)**; generalize to the whole Sanction family |
| 5 | ED-FA-0001 | C · Faction | Canonical faction count (corpus says 4–8) | **Ratify the concentric taxonomy**: 4 core + 2 conditional = 6 player-eligible; +Guilds = 7 factions; +Ministry = 8 binding entities |
| 6 | ED-FA-0010 | C · Faction | Coercion- vs capital-intensive muster asymmetry (Hafenmark/Varfell) | **Adopt** — realizes Varfell's own "tribute and conscription" Mission text |
| 7 | ED-FA-0013(c) | C · Faction | Sack mechanic (atrocity + W-for-legitimacy) | **Adopt the mechanic, keep presentation abstract** (Magdeburg reputational contagion is good disincentive design) |
| 8 | ED-FA-0014 | C · Faction | Regency interregnum on heirless leader death | **Adopt** — reuses PP-686 multi-root machinery; fills a real gap |
| 9 | ED-FA-0015 | C · Faction | Protected Tributary (Ragusa) alongside Extortive (Danegeld) | **Adopt, at reduced hegemony-path weight** — resolves the stated GD-1 softening concern |
| 10 | ED-FA-0016 | C · Faction | Guild collective embargo ("Withdrawal of Trade") | **Adopt** — grounds the existing mechanism-free "Economic Leverage" line |
| 11 | ED-SE-0002 | D · Settlement | Accord/Order stacking: scale_transitions §5.5 vs peninsular_strain §2.7 | **peninsular_strain §2.7 wins** ("stack, cap ±1/source/settlement/season") |
| 12 | ED-SE-0013 | D · Settlement | Venal appointment (sell governorships)? | **Adopt as an option with a hard downside** (audit-waiver + α↑) — coherent with the fiscal spine |
| 13 | ED-SE-0014 | D · Settlement | Local Interdict (Church settlement-scale coercion) | **Adopt** — genuinely two-edged (can cost Church L); queue with the Church-roster pass |
| 14 | ED-SE-0015 | D · Settlement | Plant Colony (converts a frontier node, never adds one) | **Adopt with the conversion guardrail** |
| 15 | ED-SE-0017 | D · Settlement | Optional founder-solidarity `Sta+1` decaying to Threshold 2 | **Adopt** — makes the annotated *asabiyyah* cycle mechanically real |
| 16 | ED-PC-0008 | E · Combat | U2 blockers: percussion self-gate; thrust_factor floor; blast radius | **File JD-9 (pommel percussion sub-model) + JD-10 (drop thrust floor); implement both before U2** |
| 17 | ED-1051 | F · Infra | Ratify `propagation_spec_v1.md` as `engine_clock`'s home, flip `doc:null` | **Flip `engine_clock` now**; sequence the other ~10 doc:null + 13 [ASSUMPTION] resolvers |
| 18 | ED-1043 | F · Infra | Mass-battle bottom-up re-architecture roadmap | **Approve methodology + greenlight Stage 1 only**; gate Stages 2–6 (combat-lane precedent) |
| 19 | ED-IN-0029 | F · Infra | Residual open sub-items: OPT-AV-1 roster, OPT-AV-13 naming, Renown cap | **Adopt 9-key roster + Cognition/Spirit + `recall`**; resolve OPT-AV-13 via ED-SC-0003; **cap Renown at 10** |
| 20 | ED-IN-0030 | F · Infra | Phantom "debt scene" — author it or strike it | **Strike & reuse** the existing Obligation/Grudge tag; drop the invented "§1 debt scene" |
| 21 | ED-885 | F · Infra | Confirm/fix the phantom "ED-885" ratification citation | **Repoint → ED-874** (the ratified faction Domain-Action resolver); resolve as citation-fixed |
| 22 | ED-634 | G · NPC/world | Crown inner-circle names + Stance Triangles | **Approve all 5 as-is** (already in provisional use); re-skin Thale's Niflhel tie |
| 23 | ED-508 | G · NPC/world | Starting Dispositions for the named NPC roster | Formula is canon; **seed from already-stated relationships**, flag only ~4–5 NPCs for your lifepath input |
| 24 | ED-595 | G · NPC/world | Ehrenwall full arc (A/B/C) | **Approve**; re-skin Coup Counter → graduated autonomy |
| 25 | ED-596 | G · NPC/world | Torsvald (Riskbreaker) full arc | **Approve**; re-skin Niflhel → intel broker |
| 26 | ED-597 | G · NPC/world | Vossen full arc | **Approve** (no re-skin) |
| 27 | ED-598 | G · NPC/world | Hann full arc | **Approve** (depends on ED-608 Mediation type); re-skin Niflhel |
| 28 | ED-599 | G · NPC/world | Orm (Warden second) full arc | **Approve** (cleanly grounded, no re-skin) |
| 29 | ED-601 | G · NPC/world | Almud Arc C (Abdicant/Pretender/Broken) | **Approve** with ED-595; re-skin Coup Counter |
| 30 | ED-602 | G · NPC/world | Vaynard Arc A & B | **Approve**; re-skin Niflhel clock; hold bonus Arc C separately |
| 31 | ED-610 | G · NPC/world | Baralta successor (unnamed Hafenmark heir) | **Propose institutional (Option B) successor**; draft name for approval |
| 32 | ED-507 | G · NPC/world | POI catalog per territory (2–6 each) | **Reframe per-settlement 2–4** (currency); schedule authoring lane; draft-batch offered |

---

## CLUSTER A — Social Contest P0 docket (ED-SC-0003 / 0004 / 0005)

These three are the last unresolved forks on the Fable-5 social-contest audit's P0 docket
(`designs/audit/2026-07-05-fable5-social-contest-audit/ed_options.md`). ED-SC-0002 was ruled
2026-07-08 (composed keying); these three still block Stage 4 and calibration. ED-SC-0004 is the
one P1 (it gates calibration, the ED-IN-0013 re-verdict, and any Godot export).

### ED-SC-0003 — "Piety Track" name collision (P2)

**The fork.** One name, three referents (confirmed by direct read):
- **0–10 debate-position tracker** (Side A wins ≥7, B ≤3, compromise 4–6): `social_contest_v30.md`
  calls it **"Persuasion Track"** (32 uses; §Step 4 is its mechanical home); `glossary.md:92`,
  `scale_transitions_v30`, `npc_behavior_v30` call it **"Piety Track (CT)"** and the glossary points
  its home at `designs/personal/conviction_track_v1.md`.
- **0–5 per-territory BG stat** (`designs/scene/conviction_track_v30.md`, "Conviction (PT)"): a
  genuinely different thing (Church-Victory territorial piety).
- **Personal moral-belief mechanic** (`designs/personal/conviction_track_v1.md` +
  `conviction_taxonomy_v30.md`, the 13-Conviction set): also different (Conviction Scars, crises).

The glossary conflated the first two: it labels the *debate* tracker "Piety Track" and points it at
the *personal-conviction* doc — neither of which is right.

**Recommendation.** Separate the three cleanly by what each actually does:
1. **0–10 debate tracker → "Persuasion Track"**, canonical home **`social_contest_v30.md`**. The name
   is accurate (it tracks persuasion in a debate and generalizes past religious venues, where "Piety"
   wrongly narrows it), and social_contest is already its mechanical head. Retire the "CT" abbreviation
   for it.
2. Correct `glossary.md:92`/`:100`/`:247` accordingly and **stop pointing the debate tracker at
   `conviction_track_v1.md`**. Rename the debate-tracker "Piety Track" references in
   `scale_transitions_v30`/`npc_behavior_v30` → "Persuasion Track" (one-time alias note).
3. **0–5 territorial stat keeps "Piety Track (PT)"**, scope-tagged as the territorial/BG stat, with a
   `name_collision_database.yaml` entry so the collision cannot recur.
4. **Personal moral-belief mechanic stays "Conviction"** (home `conviction_taxonomy_v30.md`).

**Grounding / intent.** Name-by-function is the repo's own naming discipline; this is the same move
that separated CI/Church Influence from the debate tracker (ED-782). It respects the "resolve by what
the doc does, not by filename" rule (CLAUDE.md §4).

**Consequence.** Resolves ED-SC-0003 **and** the debate-tracker + abbreviation halves of **OPT-AV-13**
(attribute-coherence audit). The *broad* Conviction/CT/CV family rename that **ED-644** defers
pending cost-benefit stays deferred — this touches only the debate tracker's collision, which is
ED-SC-0003's actual scope. Add the missing registry key for the tracker regardless (OPT-AV-13 floor).

### ED-SC-0004 — kernel's canonical Argue-pool formula (P1 — the blocker)

**The fork.** Two live, contradictory implementations:
- **Canon (legacy stub, `contest_legacy_stub.py:111-127`):** `(Primary×2) + History − Wounds + fatigue`,
  **floor 1** — the formula the campaign loop actually reaches today.
- **Kernel `[SEED]` (`primitives.py:208-211`):** `Pool.size(faculty) = max(5, faculty·2+3)` — drops
  History/Wounds/fatigue and raises the floor 1→5, erasing the low-pool (≈2D) regime the 2026-05-28
  NERS diagnostic measured.

**Recommendation. Keep the canon formula; retire the `[SEED]`.** Reasons, in priority order:
1. **Cross-system coupling is a core design value.** History rewards the veteran debater; Wounds and
   fatigue tie the social contest into the same character-state economy as combat and fieldwork.
   The `[SEED]` severs all three, making social contest a stat-only silo — the exact "developed in
   silos" incoherence Jordan flagged on 2026-07-08 (ED-IN-0029 directive).
2. **The `[SEED]` floor-5 was convenience, not a designed choice** (`primitives.py` labels it `[SEED]`).
   No ledger entry ratifies erasing the low-pool regime; the diagnostic deliberately measured it.
3. **Canon fidelity** is the tie-breaker the repo defaults to when a `[SEED]` competes with a ratified
   number.

Treat the floor itself as separable: keep **floor 1** (canon), but tag `RES_FLOOR` `[SEED]` (per
ED-IN-K/ED-IN-0013) so that *if* calibration (P4) shows the 1–2D regime is genuinely unfun, raising
the floor becomes an evidence-based tuning decision — not something pre-empted by an unratified seed.

**Consequence.** Unblocks calibration (P4), the rolling-engine re-verdict (**ED-IN-0013**), and Godot
export. The kernel's `Pool.size` is rewritten to `max(1, faculty·2 + History − Wounds + fatigue)`;
`faculty` maps to the contest's Primary Attribute.

### ED-SC-0005 — cap the Recall/Corroborate/Prep/Findings bonus stack (P2)

**The fork.** The *principle* of a single global cap is already ratified (ED-SC-0012); only the
**value** is open. Candidate ceilings (per `DP-2_SC_KU1_stacking_cap.md`): **A** +2D (strict mirror of
the genre cap) · **B** +3D · **C** +4D · **D** one combined cap across both bonus classes. Uncapped is
+8D worst case (a 44–67% pool inflation), reachable only at Exchange 1.

**Recommendation. Option B — a +3D combined cap, Findings included.** Reasons:
1. **It reuses a number the doc already establishes.** `social_contest_v30.md:539` already states
   Findings+Prep gives "a maximum Exchange 1 bonus of +3D." Elevating that same +3D to the class-wide
   cap introduces **no new magic number** and makes the existing worked example the ceiling case.
2. **It bites the full four-source stack** (halves the +6D subtotal) while still rewarding a
   genuinely-prepared player — every source is *earned* (a verifiable citation, declared coalition,
   an Overwhelming pre-roll, prior investigation), so collapsing them to a single +2D (Option A) makes
   three of the four dead most of the time.
3. **Two clean caps beat one grand total.** Keeping genre/audience (+2D) and the bonus class (+3D) as
   separate ceilings is simpler to reason about than Option D's rewrite of line 85 into a sub-clause,
   and matches ED-SC-0012's "mirror the +2D cap in spirit" framing rather than exceeding it.

**Consequence.** Prose-only (all four channels have zero code presence yet). Closes the last
cap-specific P0 item and satisfies the named Stage-4 entry criterion ("ED-SC-0005's stack cap must
land in prose before wiring", `HANDOFF_SC.md`).

---

## CLUSTER B — Parliamentary Sanction stacking (ED-SC-0015)

**The fork.** On a **total-victory** Parliamentary Censure pass, two independently-authored −1 Mandate
hits land on the same faction in one motion: (1) `parliamentary_vote.py`'s §10 generic **Total-Victory
Mandate −1** to the losing coalition's dominant faction, and (2) `faction_layer_v30` §5.4's **Censure
target-effect −1**. Neither source says whether they compound. Currently implemented as **stacking
(−2)** — the literal default, not ratified. Generalizes to every future Sanction tier
(Embargo/Blockade/Combined/Outlawry, per ED-FA-0006).

**Recommendation. Cap the target at −1 total (lex specialis), and make it the uniform rule for the
whole Parliamentary Sanction family.** When the generic Total-Victory rider and a specific Sanction
target-effect would both hit the **same** faction in one motion, the **specific effect governs and the
generic rider does not additionally stack**. Reasons:
1. **Avoids double-counting one event from two rules.** Nobody *designed* "total-victory Censure = −2";
   it emerged from two rules co-firing. That reads as an accounting artifact, not an escalation curve.
2. **The Total-Victory rider still bites in its intended general case** — when the losing coalition's
   dominant faction is **not** the specific Sanction target (a common case), the −1 rider applies
   normally. It is only suppressed on the overlap.
3. **One uniform rule for the whole family** (ED-FA-0006's parameterized tiers) beats N ad-hoc
   per-tier stacking decisions.

**Alternative, honestly stated.** Stacking to −2 *is* defensible under the engine's "degree of success
matters" throughline (Overwhelming should hurt more than Success). If you prefer that, the cleaner
form is to keep the target at −1 but let total victory escalate a **different** axis (Mandate-penalty
*duration*, or a one-season action-lock) rather than doubling the same stat — so the escalation is
designed, not a coincident double-hit. My primary recommendation is the −1 cap for its uniformity.

**Consequence.** `sim/tests/test_parliamentary_action.py` currently *documents* the −2 stacking as
"current composition, not ratified intent." Ruling this flips that test to assert the ratified rule.

---

## CLUSTER C — Faction design forks (ED-FA-0001, 0010, 0013(c), 0014, 0015, 0016)

All grounded in `designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md`
(the report's own §"Priority & sequencing" names exactly this needs_jordan queue: FA-3, FA-6(c),
FA-7, FA-8, FA-9). Each shape number below is sim-calibrated before it reaches `sim/`.

### ED-FA-0001 — faction-count reconciliation

**The fork.** The corpus carries "4–8 factions" across four sources. Enumerated (per
`designs/audit/2026-07-05-emergent-narrative-engine/01_workings/dossier_combinatorial_census.md §1.2`):

| Count | Source | What it counts |
|---|---|---|
| **4** | `faction_layer_v30 §8.1` + `faction_systems_overview_v30 §2.2` | Base/starting, unconditional player roster: **Crown, Church, Hafenmark, Varfell** |
| **6** | `faction_state_authoring_v30` line 12 | +the two conditional/optional players: **Restoration Movement** (optional 5th), **Löwenritter** (NPC pre-coup → playable post-coup) |
| **7** | `silo_cohesion_analysis.md:72` | +**Guilds** (NPC, but carries a full 6-stat sheet) |
| **8** | `stats_1_7_scale.md` + `faction_canon_v30 §11` | +**Ministry of the Peninsula** (explicit *non-faction* institutional infrastructure, 2 stats) |

The key finding: **these are concentric, not contradictory.** Each count adds one category of
entity to the prior set. The axis is *inclusiveness of definition*, not four docs disagreeing about
who exists. (Niflhel is separately STRUCK/dissolved, CR-STRIKE-2026-04-19 — historical marker only,
counted by none. Schoenland/Altonia are external BG-NPC entities, not peninsula factions.)

**Recommendation. Ratify the concentric taxonomy explicitly (define all four tiers), and adopt
"7 fully-statted factions + Ministry as a tagged non-faction stat-bearing entity" as the canonical
count for the narrative-engine binding/aggregation tables.** Rationale:
1. **The disagreement is illusory** — no doc is wrong; they answer different questions. The fix is to
   *name the tiers*, not to pick one number and delete the others.
2. **Bind on what the engine actually binds.** The narrative engine's faction-scope bank/binding
   tables (v2 §6) and aggregation templates key on **fully-statted entities** — that is the **7**
   (the four core + RM + Löwenritter + Guilds), all of which carry a stat block the templates read.
   Ministry of the Peninsula is the **8th binding entity** but is tagged `non_faction` (2 stats,
   Throughline-T4 actor) so it never enters a "faction" aggregation by accident.
3. **Record the player-roster view separately:** **4** core + **2** conditional = the 6 player-eligible
   factions for victory/roster purposes; **4** for the base 2–4-player game.

Concretely, the canonical registry entry should read: *4 core player factions {Crown, Church,
Hafenmark, Varfell}; +2 conditional player-eligible {Restoration Movement, Löwenritter}; +1 NPC
fully-statted {Guilds} = 7 factions; +1 tagged non-faction stat-bearing entity {Ministry of the
Peninsula} = 8 binding entities. Niflhel struck; Schoenland/Altonia external.*

**Consequence.** Unblocks the narrative-engine faction-scope tables and clean aggregation templates
(the stated blocker). Propagates via `names_index.yaml` + the roster surfaces (ties **ED-IN-0008**);
tracked in workplan v6 §5 T1. Pure taxonomy ratification — no faction is added, removed, or restatted.

### ED-FA-0010 (FA-3) — coercion- vs capital-intensive muster asymmetry

**The fork.** Hafenmark musters via **capital** (`W−2` substitutes for the Mil prerequisite, no PS
cost); Varfell musters via **conscription** (no W cost, but `PS−1` in the levied province — the levy
*is* the tax). Same verb, two political economies. Flagged needs_jordan because it differentiates
faction identity (a surface reserved cf. ED-776).

**Recommendation. Adopt.** This is the strongest of the faction forks:
1. It **realizes existing canon** rather than inventing identity — Varfell's Mission text already reads
   "tribute and conscription" (`faction_state_authoring §5`). The asymmetry makes that text mechanical.
2. It makes the two factions **play differently**, which is the same contextual-balance principle the
   combat engine already ratified ("a battlefield weapon ≠ a duelling weapon"): differentiation, not
   symmetry, is the goal.
3. It is a **trade-off, balanced by construction** (capital cost vs. population/legitimacy cost), so it
   does not hand either faction a strict advantage.

**Consequence.** Sits only on PROVISIONAL surfaces. Magnitudes (`W−2`, `PS−1`) sim-calibrated. Composes
with ED-FA-0009 (Muster-as-purchase, already resolved).

### ED-FA-0013(c) (FA-6c) — the Sack mechanic

**The fork.** Parts (a) Terms and (b) Storm are already executed. Part (c) **Sack** (post-storm only):
`W+2` to attacker, settlement PS/Order→0, and **every other peninsula settlement PS −1 toward the
attacker for 2 seasons** (the Magdeburg reputational-contagion effect). Flagged needs_jordan as an
atrocity-content + W-for-legitimacy tone call.

**Recommendation. Adopt the mechanic; keep the presentation abstract.** Reasons:
1. **The Magdeburg effect is genuinely good disincentive design** — it makes the "evil" option carry a
   real, *systemic* strategic cost (peninsula-wide legitimacy damage), not just flavor. Atrocity being
   "cheap locally, ruinous reputationally" is exactly the tension that makes the choice interesting.
2. The engine **already models brutal outcomes** systemically (combat lethality, Excommunication,
   Storm's own Accord−25) — Sack is consistent in kind, not a new register.
3. Keep the *content* abstract: Sack is a strategic-reputation mechanic (`W`-for-legitimacy exchange
   rate + contagion), surfaced through consequences, with no graphic depiction required.

**Alternative.** If your world-tone keeps atrocity fully off-screen, omit Sack and let **Storm** remain
the maximal military option. That is a clean, coherent choice too — the cost is losing the
Magdeburg-contagion disincentive that discourages maximal brutality.

**Consequence.** The `W+2`/contagion magnitudes and the 2-season window are sim-calibrated.

### ED-FA-0014 (FA-7) — Regency interregnum on heirless leader death

**The fork.** When a leader dies with **no adult designated heir**, the faction enters **Regency**:
unique action locked, Mandate read −1, council members become temporary multi-roots at elevated α
(their private agendas leak), rivals gain an automatic CB window — until succession resolves.

**Recommendation. Adopt.** Reasons:
1. It **reuses existing machinery** — PP-686 already has the multi-root cascade + elevated-α mechanics;
   Regency is just a defined trigger for them plus a damping suspension.
2. It **fills a real gap**: the Generational Shift clock (`settlement_layer §7.1`) ages leaders toward
   death, but nothing currently catches the interregnum — the moment Kantorowicz's "King's Two Bodies"
   fiction was engineered to abolish. SE-6 (already authored) handles *normal* succession; this handles
   the heirless/contested case.
3. The interaction with the Royal Assassination fuse arcs D/E/F is a **feature** — it gives those arcs
   a concrete landing state.

**Trigger discipline.** Fire Regency **only** when there is no adult designated heir — normal
succession with an heir preserves continuity via SE-6 (the corporate crown never dies). Magnitudes
(Mandate −1, CB-window duration) sim-calibrated.

### ED-FA-0015 (FA-8) — Protected Tributary treaty variant

**The fork.** Add a **Protected Tributary** row (Ragusa/haraç: `W−1/yr` but `+1/yr` gross trade access
= net 0, plus casus foederis, Stability cost 0) alongside the existing row, renamed **Extortive
Tributary** (Danegeld pole, `−1/yr` Stability). Flagged needs_jordan because it "softens the hegemony
path GD-1 counts Tributary toward."

**Recommendation. Adopt — but count Protected Tributaries toward hegemony at reduced weight (or a
longer dwell requirement).** Reasons:
1. The current flat "Tributary → Stability −1/yr" models **only the humiliation pole**; Ragusa shows
   subordination-without-humiliation was a real, stable equilibrium worth 4+ centuries. Adding it gives
   diplomacy a genuinely different texture.
2. **The reduced hegemony weight directly resolves the stated concern.** A consensual, mutually
   beneficial tributary relationship *should* advance a hegemony claim less than an extractive one —
   so weighting Protected Tributaries lower (or requiring longer tenure to count) preserves the
   GD-1 hegemony tension the fork worries about, instead of undercutting it.

**Consequence.** One new treaty-table row + a rename; the hegemony-weight rule is the one design
decision to confirm. Magnitudes sim-calibrated.

### ED-FA-0016 (FA-9) — Guild collective embargo ("Withdrawal of Trade")

**The fork.** A Guilds unique action (Verhansung): target faction's Port/City/Mine settlements yield
−50% Treasury + frozen Prosperity growth while active; costs the Guilds only exposure; ends on
privilege restoration or buyout. Distinct from the Parliamentary Embargo (private — no vote, no
Mandate minimum). Flagged needs_jordan as an NPC-faction-roster addition.

**Recommendation. Adopt.** Reasons:
1. It **grounds an existing but mechanism-free line** — `faction_canon §9`'s "Economic Leverage ≥ Guild
   Favour 5" currently has no mechanism. This completes canon rather than adding a wholly new capability.
2. The **private/no-vote character gives it a clear niche** distinct from the Parliamentary Embargo,
   and it is historically exact (Hanseatic blockades of Bruges 1358 & 1451–57 — a merchant corporation
   coercing princes with no army).

**Sequencing note.** It is the same *class* of call as the other blocked NPC-faction-roster items
(the Church-roster additions ED-SE-0014, etc.). If you prefer to batch roster additions, queue this
with a consolidated NPC-roster pass; otherwise adopt standalone — the "grounds an existing line"
property makes it lower-risk than a net-new roster power.

---

## CLUSTER D — Settlement design forks (ED-SE-0002, 0013, 0014, 0015, 0017)

ED-SE-0002 is from the edge-playability audit; the rest are the SE half of the FA/SE historical
docket. The report's own needs_jordan queue names SE-7-venality, SE-8(b), SE-9(a), CP-2-option.

### ED-SE-0002 — Accord/Order stacking ruling (P1, "cheapest in the audit")

**The fork.** `scale_transitions_v30 §5.5`: personal Accord Domain Echoes "do **not** stack" with
faction Govern in the same territory/season — "whichever produces the higher Accord applies."
`peninsular_strain_v30 §2.7` (the **CURRENT.md-listed head**): personal + governor actions "stack
normally… cap ±1 per source per settlement per season." Accounting §7 Step 4c resolves neither.

**Recommendation. `peninsular_strain_v30 §2.7` wins** ("stack, cap ±1 per source per settlement per
season"). Reasons:
1. **It is the CURRENT.md-listed canonical head** for this subsystem — currency priority decides ties.
2. **The ±1-per-source cap already prevents runaway stacking**, so allowing player *and* governor to
   both contribute (each capped) rewards coordinated play without breaking the economy.
3. **"Higher applies" is anti-player-agency** — it silently wastes the player's action whenever a
   governor also acted on the same settlement, which cuts against a throughline value.

**Consequence.** `scale_transitions_v30 §5.5` gets a supersession marker; Accounting §7 Step 4c gains
the resolving clause ("personal and faction contributions stack, each capped ±1 per source per
settlement per season"). Cheapest fix on the docket.

### ED-SE-0013 (SE-7) — venal appointment (does Valoria sell offices?)

**The fork.** The residencia/visita/rotation oversight toolkit is promote-ready (not a fork). The
**venal-appointment variant** is the call: sell a governorship — `W+2` now, governor α↑, **audit
rights waived** (the French *paulette*).

**Recommendation. Adopt as an option with a hard, permanent downside.** Reasons:
1. It is a **rich strategic trade** — immediate cash for long-term loss of control (Ertman's
   patrimonial trap): a venal office **waives your residencia/visita rights** over that governor and
   raises his α (he pursues his own agenda), and he is **harder to rotate**. That tension against the
   very oversight toolkit SE-7 introduces is the point.
2. It is **structurally central** to the fiscal-military spine this whole docket builds (tax farming
   FA-4, Fiscal Stance FA-1) — selling offices is the same "cash-now / control-later" family.
3. No graphic content — "selling offices" is a clean economic mechanic.

**Alternative.** If your world's legitimacy is meant to be traditional/meritocratic (offices are a
trust, not property), omit it — the oversight toolkit stands fine without it. Default is adopt, because
the fiscal spine is more coherent *with* a venality pole than without one.

### ED-SE-0014 (SE-8b) — Local Interdict

**The fork.** Advowson (a) is promote-ready. **Local Interdict** (b) is the call: a Church action vs one
settlement suspending Parish Social Services + Order/PS drain toward the controller, with a cumulative
resentment check that can cost the **Church** L in that settlement too.

**Recommendation. Adopt.** Reasons:
1. It is **genuinely two-edged** — the cumulative-resentment check (Church L−1 risk) means it is not a
   strictly-good Church power; prolonged use backfires (John's England, Venice 1606). Two-edged tools
   are better design than free levers.
2. It **fills a scale gap** — the Church currently jumps from parish passives (§1.5–1.7) straight to
   faction-scale Excommunication, with nothing settlement-scale between.

**Sequencing note.** Same class as the other blocked Church-roster items — queue with a consolidated
Church-roster pass if batching, or adopt standalone. Slots below Excommunication in the Church ladder.

### ED-SE-0015 (SE-9a) — Plant Colony

**The fork.** Marcher-autonomy (b) is promote-ready. **Plant Colony** (a) is the call: a frontier
Village/Outpost → garrison-colony (Defense+1 permanent, self-defending militia, L seeds 5 toward the
founder, PS seeds 1). Flagged needs_jordan because it touches the **fixed 37-settlement registry**.

**Recommendation. Adopt, with the conversion guardrail as a hard invariant.** The critical constraint
is already identified and correct: Plant Colony must **convert an existing frontier Village/Outpost,
never add a node**. With that guardrail it is well-grounded (Byzantine themata, Habsburg Militärgrenze,
Roman coloniae) and gives frontier play real texture, feeding the existing GD-3 emergence pipeline via
`governor_emergence`. The "natives displaced" note stays abstract (PS seeds low).

**Flag (not part of this fork).** The registry count is cited inconsistently across the corpus (this
item says **37**; CLAUDE.md §6 notes `data_serialization_spec` ships **34 vs 35**). Worth a separate
reconciliation — it does not block this ruling, but Plant Colony's "convert, never add" invariant makes
getting the canonical count right more important, not less.

### ED-SE-0017 (CP-2 option) — founder-solidarity bonus

**The fork.** The Ibn Khaldun *asabiyyah* annotation on the Generational Shift clock is already
authored. The **optional mechanic** is the call: a founder-generation `Sta+1` that expires at
Threshold 2.

**Recommendation. Adopt.** It makes the *asabiyyah* cycle you already annotated **mechanically real**
rather than pure flavor: a new/young dynasty gets a tangible early-cohesion advantage that decays by
the 3rd–4th generation — which is precisely Ibn Khaldun's theory. It is small and bounded (`Sta+1`,
expires at Threshold 2). If you would rather the clock stay a flavor annotation with no numeric bite,
omit — but adopting closes the loop between the annotation and the mechanic. Magnitude sim-calibrated.

---

## CLUSTER E — Personal combat (ED-PC-0008)

**The context.** Attempting U2 (graded mode affordance) surfaced three findings, each needing a
Jordan-reviewed default before U2 can safely land. Nothing was committed to engine code — all verified
by direct measurement against the live post-U1 tree.

**The three findings + recommendation (endorsing the ledger entry's own analysis):**

1. **Percussion self-gate removal is a severe balance regression, not "ships weak."** Measured: naively
   dropping the head-not-blunt gate lets swords' whole blade+PoB feed the blunt-fit `PERC_SCALE`/`PERC_EXP`
   formula → greatsword 6.12, katana 6.26, longsword 5.77, rivaling the poleaxe's 7.48. Root cause: the
   percussion formula was fit against *dedicated blunt* weapons (whole forward mass = striking surface); a
   sword's percussion-capable mass is its **small rear pommel**, not its blade.
   → **Recommendation: file this as JD-9 and adopt a pommel-specific percussion sub-model** — derive
   edged-weapon percussion from the pommel's own `mass_kg`/`x_m` via `percussion_element_authority`, not
   the whole-weapon formula. This is the correct fix under the repo's **combat-grounding-methodology**
   (derive from primitives, never sim-fit); JD-4's "ships weak" bare self-gate removal is measurably wrong.

2. **`thrust_factor` carries its own undocumented floor bug** (structurally identical to the flagged
   `cut_factor` 0.45 floor): mace (pc=0.02) scores thrust 0.34, staff 0.31 — nontrivial "thrust" for
   pointless weapons, purely from rigid cross-section. This forces `MODE_TIP_MIN` into a fragile
   0.34–0.37 band (sabre clears it by only 0.03) — the anti-sim-fit principle warns against exactly this.
   → **Recommendation: file this as JD-10 and drop `thrust_factor`'s floor** the same way U2 drops
   `cut_factor`'s, widening the margin. It is an additional formula change beyond consolidation_v1's
   literal text, so it needs its own sign-off (not a silent bundle) — hence JD-10.

3. **The graded-affordance change has a wider blast radius than the plan's 5 named tests.**
   `test_combat_invariants.py` already pins exact afforded-head sets for composite weapons (ji, guisarme,
   voulge, bec_de_corbin, lucerne_hammer, goedendag, poleaxe) that a naive head-independent cut/point
   check would break (e.g. ji's spearhead element clears `MODE_EDGE_MIN` and adds a third "cut" token).
   → **Recommendation: treat (3) as a scope/effort note, not a fork** — whoever implements U2 must
   re-derive the expected afforded-set for **every** composite weapon (fixture-regeneration rigor, no
   pre-existing "right answer"), not just the 5 single-mode weapons named.

**Net.** Adopt JD-9 (pommel percussion sub-model) and JD-10 (drop `thrust_factor` floor), extending
`consolidation_v1.md` §6; **implement both before U2**; carry (3) as an implementation-scope note.

---

## CLUSTER F — Infrastructure & citations (ED-1051, 1043, IN-0029, IN-0030, 885)

### ED-1051 — Godot module-contract coverage gap

**The fork (narrowed).** The broad task (author 11/27 `doc:null` modules + adjudicate 13/27
`[ASSUMPTION]` resolvers) is a work-plan, not a single ruling. The **ready decision** is narrow:
`engine_clock` (the temporal spine) now has a **CANDIDATE home doc** — `propagation_spec_v1.md`
(ED-1093, CANONICAL, ratified 2026-07-02) — but its `doc:null` stays unflipped pending this entry.

**Recommendation.**
1. **Ratify `propagation_spec_v1.md` as `engine_clock`'s home and flip its `doc:null` now.** The
   authoring half of "start with engine_clock" is effectively done; only the ordering call remains.
   This is the cheap, ready win.
2. **Sequence the rest, don't batch-close it.** Author the remaining ~10 `doc:null` modules in
   dependency order (temporal spine first — done; then the modules the combat/contest slices already
   exercise), adjudicating each `[ASSUMPTION]` resolver's determinism class as its home doc lands. This
   is the CLAUDE.md §6 "drive the register + Gate-0 to closure" directive, paced.

**Consequence.** Composes with ED-FA-0002 (the `domain_actions` home doc, which flips another
`doc:null`). Note the counts have *grown* since 2026-06-30 (11/27 and 13/27) — the register needs an
owner, not just a one-time sweep.

### ED-1043 — mass-battle bottom-up re-architecture roadmap

**The fork.** Approve (or veto) a staged, gated, adversarial re-architecture of the mass-battle sim:
`orchestration.py` is a 2,899-line god-file; troop-types/formations/tactics/strategy are inert data;
~20 `PC_*` magnitudes are calibrated-to-band debt. The proposal: clean module split (wrapper resolves
nothing / core resolves only), a derive-from-primitive constant bar, a GRANULARITY dial
(unit/subunit/cell), and a 7-gate per-stage sequence. Stages 1–6 gated for separate approval.

**Recommendation. Approve the methodology and diagnosis; greenlight Stage 1 only; gate Stages 2–6.**
Reasons:
1. **The methodology is already proven in this repo.** The scene-combat engine went through exactly
   this arc (god-file → clean split → derive-from-primitive → adversarial gates) and it worked
   (combat_engine_v1, merged PR #40). The precedent is strong and the diagnosis matches.
2. **The derive-from-primitive constant bar is already ratified doctrine** — it is the
   combat-grounding-methodology ("history validates behaviour, never licenses a value; calibrated =
   debt→0") applied to a second subsystem. Consistent, not novel.
3. **Do not authorize all six stages at once** — gate each per the plan, exactly as the combat lane
   was gated. Stage 1 (the byte-exact clean module split) is the safe first increment.

**One design confirm.** The **GRANULARITY dial** (deploy at unit / subunit / cell) is a genuine design
addition, not just a refactor — it gives mass battle the same zoom flexibility the scale-transitions
doctrine values. Recommend adopt; it is the piece most worth your explicit eye.

### ED-IN-0029 — attribute/value coherence audit (residual open sub-items)

The docket (`ed_options.md`) is **mostly ratified already** (Jordan, 2026-07-08). Three sub-items
remain genuinely open:

- **OPT-AV-1 (attribute roster) — you SKIPPED this.** The standing recommended default is: adopt the
  **registry's 9-key structure** with naming corrections — primaries → **Cognition** (ED-899, already
  live as named engine constants) and **Spirit** (zero live "Will" usage), **plus `attr.mind.recall`
  as a 10th key** — retire the glossary Part-One formula tables, supersede the competing
  `canonical_registry.md` table.
  → **Recommendation: adopt the stated default now.** Your own 2026-07-08 directive was that the
  "explosion of attributes across silos" needs "unity, consistency and coherence" — a ratified roster
  is precisely the fix, and every fold-target name (Acuity/Will) has zero consumers, so the cost is
  near-zero. If you skipped it to author the roster yourself, that is the one reason to keep deferring;
  otherwise this is the highest-leverage coherence win on the board.
- **OPT-AV-13 (Piety/Conviction/CT/CV/PT naming) — left open (ED-644 defers the broad rename).**
  → **Recommendation: resolve the debate-tracker + abbreviation half via ED-SC-0003** (Cluster A
  above: "Persuasion Track" for the 0–10 tracker, "Piety Track (PT)" scope-tagged for the 0–5
  territorial stat, "Conviction" for the personal mechanic). Add the missing registry key(s)
  regardless. The residual broad-family cost-benefit that ED-644 defers can stay deferred.
- **OPT-AV-18 Renown sub-item (cap 10 vs uncapped + Shadow Renown relation) — no default stated.**
  → **Recommendation: cap public Renown at 10, keep the two tracks separate.** Shadow Renown is
  explicitly **0–10 capped** and "spills into Deniability Debt above 10" (`faction_politics_v30 §2.2b.i`)
  and is described as "the mirror of public Renown." Scale-symmetry with its own mirror — and with the
  general 0–10 track convention — makes capped-at-10 the clean default. The existing conversion rules
  (2:1 citation loss, Infamy on exposure) already govern the cross-track relationship.

### ED-IN-0030 — phantom "debt scene" mechanic

**The fork.** `scale_transitions_v30 §4.3.2` row 8 says a withheld Rank-Advancement Recognition Event
"creat[es] a debt scene per §1" — but **no "debt scene" concept exists anywhere** in
`faction_politics_v30` (confirmed by grep + two prior audits). Author the mechanic, or strike the clause.

**Recommendation. Strike the invented term and rewrite the clause to reuse existing machinery.** A
withheld Recognition should set an **Obligation/Grudge tag** on the withholding faction toward the
passed-over candidate (the faction "owes" recognition), resolvable through a later social contest /
Hold Court — rather than a net-new "debt scene" primitive. Reasons:
1. **Anti-fabrication (CLAUDE.md §5/§7):** no "debt scene" mechanic was ever specified; inventing one to
   satisfy a dangling citation is exactly what the discipline forbids.
2. **The machinery already exists** — the Obligation system (`social_contest_v30 §6.1`) and the
   standing-debt / Deniability-Debt family (`faction_politics_v30 §2.2b`) already model "owed
   recognition." Reuse over invention.

**Alternative.** If you *do* want a distinct "debt scene" as its own scene type, that is a real design
task to spec separately (what it opens on, how it resolves, what it costs) — but the default should be
strike-and-reuse. Prose-only fix either way.

### ED-885 — phantom ratification citation

**The fork.** `canonical_sources.yaml:521` cites "ED-885" as the Jordan-ratified authority for the
2026-05-30 F-RESID migration (4 bare-stat Unique Actions → d+σ resolver), but ED-885 was never written.

**Recommendation. Repoint the citation → ED-874 and resolve ED-885 as citation-fixed.** Verified:
**ED-874** *is* the "Faction Domain Action resolver — RATIFIED (Jordan 2026-05-31, 'works well')" —
the bare-stat→d+σ migration for faction Domain Actions, i.e. exactly the F-RESID work. The
`canonical_sources.yaml` comment itself already hedges "ratification ID to confirm, likely ED-874,"
and ED-883 already resolved the broader "forward-referenced-but-unwritten ED 874–882 block." Pure
bookkeeping; no design content changes. (Fix the line to read `ED-874`; strike the "ED-885" phantom.)

---

## CLUSTER G — NPC, roster & world content (ED-634, 508, 595–602, 610, 507)

These are the creative-authorial items ("Requires user approval"). The good news from the roster
survey: most already have **complete proposals** in the corpus that the ledger simply never closed —
so the call is "approve / adjust," not "author from scratch." Only two are genuine blank-slate design
(ED-610 successor identity, ED-507's bulk POI content), and for those this docket proposes a concrete
shape + a first draft rather than leaving them open.

### ED-634 — Crown inner-circle names + Stance Triangles

**The proposal (already written).** `faction_politics_v30 §1.1d` proposes five named inner-circle
NPCs, each with a full **Stance Triangle** (Conviction + Resonant Style + Certainty 0–5 — the standard
NPC definition from `npc_behavior_v30 §1.1`). The names are **already echoed into `npc_behavior_v30`
and `faction_canon_v30`** as if provisionally accepted:

| Role | Name | Conviction / RS / Certainty | Seed relationship |
|---|---|---|---|
| Royal Marshal | **Wilhelm Voss** | Order / Authority / 4 | Distrusts Löwenritter; −1 toward Ehrenwall |
| Lord Treasurer | **Annalie Reichard** | Precedent / Evidence / 5 | Distant Feldhaus (Guild) cousin; +1 toward Baralta |
| Spymaster (Schattendienst) | **Kolbrun Thale** | Autonomy / Consequence / 3 | Only IC member with (former-)Niflhel contacts |
| Archbishop's Representative | **Father Gustav Linder** | Faith / Authority / 5 | Church secondee; −2 vs visible Thread-practitioners |
| Royal Guard Captain / Löwenritter Liaison | **Theodor Kreutz** | Order / Authority / 4 | Allegiance to Almud personally over Ehrenwall |

Plus **Torben Almqvist** as inner-circle-adjacent (non-voting; Continuity / Evidence).

**Recommendation. Approve all five names + Stance Triangles as-is and ratify.** Reasons: (1) the set is
complete and internally consistent (each has a full triangle); (2) the seed relationships are
load-bearing and already wired into the arc logic (Voss/Ehrenwall friction, Kreutz→Almud loyalty feed
Ehrenwall's coup arc; Reichard→Baralta ties the Treasury to the Guild axis); (3) the names follow the
established Germanic/Norse convention and pass the naming gate (none is the deprecated "Galbados").
Flip the §1.1d provisional markers, close §10.2 P1, run `ci_naming_check.py` on ratification. One
housekeeping note: re-skin Thale's "Niflhel contacts" to the settlement-layer intelligence-broker
framing (Niflhel is struck) — same re-skin the arcs need below.

### ED-508 — starting Dispositions for the named NPC roster

**State.** The **lifepath Disposition formula is canonical and needs no decision**
(`params/fieldwork.md:148-157`: per lifepath element assign ±0.5 on alignment/conflict with the
NPC's faction/culture/role vs the reference; sum, floor, clamp [−5,+5]). What is missing is per-NPC
**values** for the roster: **Vaynard, Baralta, the Cardinals (Jarnstal/Olafsson/Tormann/Klapp),
Torben, Elske, Klapp, Almud, Maret Uln, Edeyja** — none has an assigned starting Disposition anywhere.

**Recommendation. Don't treat this as fully blocked — resolve it in two moves:**
1. **Seed from relationships the corpus already states.** Disposition is relational, and several
   pairs are *already* specified in prose (Voss −1→Ehrenwall, Reichard +1→Baralta, Kreutz allegiance
   →Almud, and the arc docs' inter-NPC frictions). A follow-up pass can extract those into a
   Disposition table mechanically — they are the formula's output already written in words — and
   default all un-stated pairs to **0 (neutral)**. This unblocks most of the roster with zero new
   creative input.
2. **Flag the genuinely-unspecified NPCs for your lifepath input.** Only the NPCs with no stated
   relationships (**Maret Uln, Edeyja, the individual Cardinals**) need you to supply a one-line
   lifepath profile (birthplace / trade / faction tie / lineage / formative event) to run through the
   formula. This narrows "roster values pending Jordan" from ~11 open profiles to ~4–5.

I can draft the extracted table + provisional profiles for the unspecified few for your approval on
request — but the creative facts (a Cardinal's birthplace, Edeyja's formative history) are yours to
confirm, so I've stopped short of inventing them.

### ED-595–602 — the seven NPC full-arc proposals

**State.** **Complete arc text exists for all seven** in `designs/arcs/arc_expansion_v30.md` (Parts
II/III). The doc header self-declares "CANONICAL — approved 2026-04-17," but the ledger rows stayed
`open`/`needs_jordan` — a classic "ruling made, row never closed." Two **mechanical** caveats apply
across several (not content changes): (i) the **Coup Counter** mechanic (Ehrenwall, Almud) is
superseded by **Löwenritter graduated autonomy** — the beats are valid, the trigger needs translating;
(ii) **Niflhel** references (Torsvald, Vossen, Hann, Vaynard) are struck and need re-skinning to
"settlement-layer intelligence broker."

**Recommendation. Approve all seven arcs, conditioned on the two mechanical re-skins applied during
ratification.** The arc content is well-developed, internally consistent, and grounded in each NPC's
Stance Triangle. Per-arc essence + any per-item note:

- **ED-595 Ehrenwall** — A "Watchman" (scores Almud yearly) → B "Instrument at the Edge" → C "The
  Regency" (installs Torben as figurehead or rules directly; secondary "Failed Regency" cedes to
  Torben). *Re-skin: Coup Counter → graduated-autonomy stages.* **Approve.**
- **ED-596 Torsvald/Riskbreaker** — A "The Operative" → B "The Operative Who Sees" (TS≥30, Thread as
  intel) → C "The Riskbreaker at Risk" (untrained Discovery decay). *Re-skin: Niflhel extraction op →
  intel-broker op.* **Approve.**
- **ED-597 Vossen** — A "The Organiser" → B "The Strained Leader" (pacifist-Equity fork) → C "The
  Legacy" (Captured/Killed/Schism; Schism splits RM into cultural vs operational wings, gating
  co-victory paths). **Approve.**
- **ED-598 Hann** — A "The Infrastructure" → B "The Operator" (unauthorized non-violent ops; spawns
  the Mediation contest type, ED-608) → C "The Fractured Operator" (leads RM's independent intel arm).
  *Re-skin: Niflhel refs.* **Approve** (note it depends on ED-608 Mediation contest type existing).
- **ED-599 Orm (Warden second)** — A "The Anchor" → B "The Exhausted" (grief strips Continuity) → C
  "The Last Stand" (witnessed narrative death sealing a Catastrophic Gap). **Approve** — cleanly
  grounded in the warden/Gap machinery, no re-skin needed.
- **ED-601 Almud Arc C** — three trajectories gated by Certainty at exile: **C-i Abdicant** (cedes to
  Torben; may produce a Thread-theology refutation artifact), **C-ii Pretender** (raises a loyalist
  faction — a legitimate "restore Almud" co-victory variant), **C-iii Broken** (collapse; Dissonant
  Coherence risk unless the player becomes his framework). *Re-skin: Coup Counter trigger.* **Approve**
  — this is the payoff of the Ehrenwall/Crown arc and should ratify together with ED-595.
- **ED-602 Vaynard Arc A & B** — A "The Scholar" (instrumental Thread study; hidden intel-leak clock)
  → B "The Awakened" (involuntary Thread perception; "Collaborator" sub-branch to genuine
  practitioner). *Re-skin: Niflhel-Contact clock → intel-broker-contact clock.* **Approve** (the doc's
  bonus Arc C "Consumed" is not in ED-602's scope — hold it or file it separately, your call).

Ratifying these closes seven ledger rows at once and applies the two re-skins as a bundled
`[editorial]` propagation.

### ED-610 — Baralta successor (unnamed Hafenmark heir)

**State.** Genuine blank slate — only a one-line stub. Baralta = **Duchess Inge Baralta**, sovereign of
Hafenmark (constitutional-duchy; Categorical-Imperative / parliamentary-procedural ethics; anchors
Isabella I of Castile / Henry VIII). The *institutional* succession mechanic already exists
(`baralta_crown_claim_v30 §5`: Option A Hafenmark merges into Crown; **Option B** a PI-gated
"institutional successor" keeps Hafenmark alive as an NPC faction) — but it names no actual heir,
which is exactly the gap.

**Recommendation (proposed content, for your approval).** Make the successor **institutional, not
dynastic** — a parliamentary-confirmed successor consistent with Option B. This is the thematically
correct shape: a *constitutional duchy* whose ethos is parliamentary-procedural should not hinge on a
bloodline heir; its legitimacy passes through its institution. That also lets ED-610 resolve **with**
the already-designed Option B instead of adding a parallel dynastic track.

Concrete proposal to accept or replace: the successor is the sitting **Speaker of the Hafenmark
Kammer** (its parliamentary assembly), confirmed by a PI-gated vote on Baralta's death — carrying
Hafenmark's Precedent/procedural conviction but *lower* personal Mandate than Inge (an institutional
caretaker, not a charismatic sovereign), which mechanically models the "institutional successor keeps
Hafenmark alive but weaker" outcome Option B already implies. A provisional name in convention:
**Kammer-Speaker Adelheid Feldhaus** (tying the successor to the Feldhaus/Guild axis already seeded
via Reichard) — or a name of your choosing. **This is your creative call; the docket proposes the
shape + one concrete option rather than leaving it blank, but will not ratify a named NPC without your
sign-off.**

### ED-507 — POI catalog per territory

**State.** The **framework is canonical** (`fieldwork_v30 §3.1`: the Depth 0–5 ladder
Landmark/Resource/Secret/Remnant/Anomaly/Breach; per-settlement-type templates; 7 worked examples such
as Valorsplatz's "Lion's Archive" and Askeheim's "Wound Core"). The **content is not authored** — only
7 one-off POIs exist campaign-wide, not a full 2–4 set anywhere.

**Recommendation.**
1. **Currency fix first:** ED-507's "per **territory**, 2–6 POIs" framing is **stale** — `fieldwork_v30
   §3.1`'s Throughline-T3 redesign now assigns POIs **per settlement, 2–4 each**. Re-scope the item to
   the current framing before authoring against it.
2. **This is a bulk authorial lane, not a single ruling.** ~2–4 POIs × ~35 settlements ≈ 100 POIs is a
   dedicated content pass, seeded from the 7 existing worked examples + the per-settlement-type
   templates, with each POI grounded in its settlement's established faction / geography / Thread
   history. Recommend scheduling it as a WR-lane authoring pass (it is not blocking any mechanic).
3. **Offer:** I can draft a first batch — the ~8 major settlements (Seat/Cathedral/Parliament tier) —
   as a template-setting exercise for your approval, so the pattern is fixed before the long tail is
   filled. Say the word and I'll produce that batch grounded in each settlement's canon.

This item stays `needs_jordan` in the sense that the *content* is yours to approve, but the *decision*
it needs is small: approve the per-settlement reframe + greenlight the authoring lane (and optionally
the draft batch).
