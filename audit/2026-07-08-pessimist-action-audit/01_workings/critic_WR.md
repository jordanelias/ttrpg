## Inverted Critic Pass — Lane WR (Scene Slate / Personal-Phase Triage)

**Method note:** re-read `designs/architecture/player_agency_v30.md` §4.2–4.5 directly (not just the dossier's characterization) before steelmanning, since the merge/duplication and flavor-only claims are falsifiable against the actual spec text. Cardinal-rule check performed on every row: none of the four condemned verdicts below cite stub/unwired/unbuilt/Godot-unported status as reasoning — all four rest on N/Ω/Q design-merit grounds, correctly separated into `build_state_note`. No correction needed on that front.

---

### Step 6 — Territorial Scenes (MERGE, P3) → **UPHELD** (with a remedy-target refinement)

**Steelman attempted:** Could "Thread phenomenon (if MS ≤ 60...)" be a deliberate *second tier* of Thread content — ambient/steady-state texture for the MS 21–60 band where Step 2b's event-triggered conditions (Critical MS≤20, threshold-crossing, active Gap/Lock, WC-advance) structurally generate nothing, rather than true duplicate coverage? This is a real possibility: 2b fires on *state changes* or *active named conditions*; a territory sitting steadily at MS 45 with no Gap/Lock/WC-advance gets nothing from 2b. Read generously, Step 6's clause could be filling that steady-state gap.

**Where the steelman fails:** even granting that reading, the *proposed remedy* the dossier names (fold into Step 2b) is wrong, not the underlying diagnosis. Step 2b's dossier-KEEP rationale explicitly credits "the genuinely elegant one-scene-max scarcity rule" (`Max 1 Thread-State scene per Slate. Highest priority fires.`, confirmed verbatim in the doc) as the mechanism's core virtue. Merging a lower-bar, non-event-gated "MS≤60" clause into that same bucket dilutes exactly the scarcity discipline the sibling KEEP praises — it's self-contradictory to fix Step 6 by importing the collision into 2b. The correct subtractive move for the Thread-phenomenon clause specifically is **CUT outright** (fold its "don't leave the world thread-silent" backfill purpose into Step 6's general territorial-texture pool, not into 2b), while "NPC arrival" genuinely does converge on Step 5's apparatus when built rigorously — the doc gives Step 5 a precise triple-AND gate (Disposition, relevant active Conviction, priority-tree fire) and gives "NPC arrival" *no gating condition at all*, meaning any real implementation has nowhere else to borrow logic from except Step 5's machinery, arriving at strictly the same content with a weaker gate. That half of the MERGE call fully survives.

**Verdict:** MERGE stands (UPHELD). Refine the *remedy* only: retarget the Thread-phenomenon sub-clause to CUT (not merge into 2b) to protect 2b's scarcity discipline; NPC-arrival→Step 5 merge stands as specified. Top-line verdict/severity unchanged.

---

### Step 7 — Ambient Scenes (DISTILL, P3) → **UPHELD** (with an accuracy correction)

**Steelman attempted:** the dossier's own quote — "pursued or unpursued alike produce no traceable world-state change" — overreaches. Checked against §4.5's actual table, the row `Ambient (Priority 5) | No consequence. The world moved on.` is explicitly titled "Resolution *When Not Pursued*" — it says nothing about the pursued case. §4.2's Step 7 description gives pursuit a real (if minor) payoff: "low-stakes information or minor relationship opportunity," i.e., a small Disposition or info gain when the player *does* spend a scarce scene action on it. That is a nonzero world-state effect, and the dossier's phrasing conflates the two cases.

**Where the steelman fails:** correcting the overreach doesn't rescue the verdict. Ambient sits at the lowest priority (5) and — per the cross-step pruning algorithm (§4.3, step-ordered fill) — only reaches the Slate once every higher-priority Step's content is exhausted; it is definitionally backfill, not a competed-for choice. Its own spec gives it no gating condition, no named stakes, and (confirmed) an explicit "no consequence" outcome on the far more common not-pursued path. Even crediting the minor payoff when pursued, nothing in "unstructured encounter, low-stakes info or minor relationship opportunity" is a dynamic that Step 6's general territorial-texture bucket couldn't equally deliver — it doesn't need its own numbered Step, its own pruning-table row, and its own consequence-table row to exist. The Q/Flavor-only reasoning holds once corrected.

**Verdict:** DISTILL stands (UPHELD), fold into Step 6 as proposed. Recommend the write-up cite §4.5's *unpursued-only* framing precisely rather than "pursued or unpursued alike," so the finding isn't vulnerable to a literal-text rebuttal on this point.

---

### Step 4 — Conviction validator, capitalization heuristic (REFINE, P3) → **UPHELD**

**Steelman attempted:** the doc already contains what looks like the dossier's own proposed fix — an explicit UI prompt: on a weak match it displays "Did you mean [System keyword X]? If so, capitalize it... Player chooses: (a) capitalize... (b) leave lowercase..." That is already an explicit confirmation flow, not a silent trap; if the mitigation already exists, is the REFINE finding stale?

**Where the steelman fails:** the confirmation prompt only fires *after* the underlying signal (bare capitalization of an ordinary English word) has already been used to bucket the Conviction into strong/weak/no-match. The elegance problem isn't the absence of a prompt, it's that several of the ~25 system keywords (`Order`, `Standing`, `Crown`, `Accord`, `Regency`) double as extremely common English words a player would naturally use lowercase in ordinary Conviction prose ("I want order restored," "my sense of standing"). A capitalization-triggered classifier over freeform prose will therefore either (a) fire the weak-match nag routinely on ordinary sentences (noise attrition — players learn to dismiss/ignore it, defeating its purpose), or (b) get dismissed once and then silently and permanently forfeit Step-4 firing for that Conviction without the player tracking which of their ~25 keyword-adjacent words they left lowercase. That second-order consequence genuinely isn't restatable in one breath alongside "Convictions scan for NPC/faction/territory/keyword/role matches" — you need the full three-way strong/weak/no table plus the a/b choice-tree to predict what any given sentence will do. An explicit tag-based selection (player picks system-keyword chips to attach to a Conviction, no prose-capitalization inference at all) would collapse this to a genuinely one-breath rule and remove the noise/silent-miss failure mode entirely.

**Verdict:** REFINE stands (UPHELD), P3, core rule sound / validator mechanism should simplify away from capitalization-as-signal.

---

### Witness Mode — Narrative Input Sentence (DISTILL, P2, NOT-INTENDED) → **UPHELD**, severity **DOWNGRADED P2→P3**

**Steelman attempted:** could the "dialogue branch tagged to Conviction" have a real downstream mechanical hook — e.g., feeding a later Read/Appraise, banking toward a future Slate-generation input, or nudging Disposition trajectory — making it more than pure color? Checked the full Witness Mode spec (`player_agency_v30.md` lines 207–218): item 2 places "one narrative input opportunity at scene resolution" as its own bullet, and item 3 states "the scene's mechanical resolution proceeds via NPC AI as if the player had declined to engage" — i.e., resolution is computed treating the player as fully absent. No downstream mechanical linkage is specified anywhere for the narrative-input sentence; nothing else in the corpus (Domain Echo, Momentum/Coherence — both explicitly *not* generated in Witness Mode per items 3–4) references it either. The tabletop framing ("GM may incorporate or reject") is a discretionary-judgment call with no engine-executable analogue, and the CLAUDE.md invariant ("There is no GM — the engine resolves everything") is direct, load-bearing project doctrine, not audit-invented framing. The steelman has nothing load-bearing to point to.

**Where I adjust the dossier:** the underlying Flavor-only + NOT-INTENDED diagnosis is correct and DISTILL is the right disposition, but P2 ("materially narrows meaningful choice") overstates the stakes for a mechanism that, by the dossier's own finding, "adds no decision the player weighs" — if it never carried decision-weight, cutting it doesn't *narrow* a choice, it removes an inert flavor beat. That maps more precisely to P3 (friction/authoring-debt: avoiding the invented task of building a GM-less equivalent from scratch), consistent with how the sibling Flavor-only finding (Step 7) is scored P3.

**Verdict:** DISTILL/fold-into-Read-Appraise-outcome stands (UPHELD); severity revised P2 → P3.

---

### Spot-checks on KEEP verdicts (no steelman required, checked for over-generosity)

- **Scene Slate umbrella (P1 KEEP):** confirmed via §4.3's own text ("The surplus is the point... The player cannot prevent the world from moving") — the cross-scale/autonomous-continuation claim is textually grounded, not inflated. No downgrade.
- **Step 2b Thread-State (P2 KEEP):** confirmed the "max 1 per Slate, highest priority fires" scarcity rule verbatim in the doc — exactly the elegant discipline the dossier credits. No downgrade.
- **Step 5 NPC Outreach (P2 KEEP):** confirmed both branches (outreach: triple-AND Disposition+Conviction+priority-tree fire; demand: triple-AND with a priced decline cost, "-1 Disposition, +1 Exposure") are exactly as rigorously gated as claimed. No downgrade.

No KEEP verdict inspected rests on build-state reasoning either — the good and bad rows both keep `build_state_note` strictly as routing metadata, as the charter requires.

---

### Summary table

| Action | Dossier verdict | Critic outcome | Final verdict |
|---|---|---|---|
| Step 6 — Territorial Scenes | MERGE (P3) | UPHELD (remedy-target refined: Thread-phenomenon → CUT not merge-into-2b) | MERGE |
| Step 7 — Ambient Scenes | DISTILL (P3) | UPHELD (dossier's "pursued or unpursued alike" phrasing corrected — only unpursued is stated no-consequence, doesn't change outcome) | DISTILL |
| Step 4 — Conviction validator | REFINE (P3) | UPHELD | REFINE |
| Witness Mode — Narrative Input Sentence | DISTILL (P2) | UPHELD, severity downgraded | DISTILL (P3) |

