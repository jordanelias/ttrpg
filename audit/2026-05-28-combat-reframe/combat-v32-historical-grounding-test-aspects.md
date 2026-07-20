# Combat v32 — Historical-Grounding Test, Part 2: Aspect specializations (§6) + matchup mechanics (§7)

The operating layer beneath the schools. Last turn's test covered weapons (§8) and the ten Traditions (§5); this completes the grounding lens over the **nine aspect-specialization categories** (`§6.1–§6.9`) and the **§7 reaction/stance mechanics** — the granular building blocks that the ten Traditions bundle. These map almost exactly onto the seven axes built in the first precedent document, so the historical guides apply most tightly here.

`[SELF-AUTHORED — bias risk]` v32 is prior-Claude work; tested as external. **The circularity caveat from Part 1 applies even more strongly here** — the §6 aspect vocabulary is the same near-transcription of the historical traditions (Forward-point = Agrippa; Tactile = *Fühlen*; Thumb-anchor = the *szabla*'s *paluch*), so this checks **internal consistency and surfaces divergences**, it does not independently *validate*. Historical fidelity is not the design goal (`design_doc_framing`); divergences are design flags for Jordan, not canonical defects.

---

## VERDICT (read first)

**The aspect layer is the most strongly grounded of the three layers tested** — all nine categories map onto the manual's axes/cognitive-modes, and crucially the precedent's *two strongest convergent universals are both directly represented*: the **bind-as-information-channel** (the manual's single strongest cross-cultural result — *Fühlen / sentimento del ferro / ting jin / chi sao*) is v32's **Tactile reading channel**, and the **convergent ~5-guard reduction** (Agrippa's 4, the Vier Leger, the 5 kamae) is v32's **5-stance set**. A third correspondence resolves an open question from earlier in this work: **Silver's *true times* biomechanics — which I noted in the weapon pass were *not* in Weapon Speed — turn out to be implemented in the §6.7/§7.2 Reaction families.** Against this, only **two real divergences**: the historically-unified *initiative (sen)* concept is mechanically **distributed across three systems** (F-A1), and one commitment spec (Escalating) is a **game archetype with no historical anchor** (F-A2). Two further nitpicks (F-A3, F-A4) are noted but minor.

**Scope.** Historical-grounding lens only — Phase-5 intent gate + axis-coherence. Complements `ners_verdict_combat_v32.md` and Part 1; not the full 4-stage NERS, not the I-17 balance sim.

---

## THE GROUNDING MATRIX — nine aspect categories (§6.1–§6.9)

v32 specializations cited from `combat_v32_proposal §6.1–§6.9` (fetched this session); reaction families from `§7.2`, stance counter from `§7.1` (Part 1). Historical axes/anchors from `combat-manuals-seven-axes-throughlines.md`.

| § | Aspect category | v32 specializations | Manual axis / mode | Grounding | Finding |
|---|---|---|---|---|---|
| 6.1 | **Stance** (5) | Centered · Raised · Low · Side · Forward-point | Axis 3 (stance/guard) | **PASS (strong)** | = the convergent ~5-guard reduction; Forward-point = Agrippa; transcendence (Musashi) captured by Single-strike's Stance-flux. |
| 6.2 | **Footwork** (5) | Linear · Curvilinear · Triangular · Drawing · Bursting | Axis 5 (footwork) | **PASS** | Curvilinear = Spanish *compás curvo*; Triangular = Katori/FMA. Minor: positional, not tempo-generating (F-A4). |
| 6.3 | **Grip** (5) | Standard · Thumb-anchor · Short grip · Half-grip-available · Paired | Axis 6 (grip) | **PASS (strong)** | Thumb-anchor = the *szabla*'s *paluch*; Short grip + Half-grip = the *Halbschwert*. Elevates the manual's most under-theorised axis. Minor: two adjacent half-sword grips (F-A3). |
| 6.4 | **Approach** (5) | Direct press · Angled · Feinted · Drawing · Explosive | Axis 4 (approaches/initiation) | **PASS (strong)** | Drawing = the *invito* (draw the commitment); Angled = periphery-seeking; Explosive = the committed close. |
| 6.5 | **Reading** (4 + Thread) | Tactile · Kinetic · Geometric · Rhythmic · (Thread) | The cognitive-modes typology + T3 | **PASS (strong)** | The headline correspondence — see below. T3 (bind-as-channel) = Tactile, directly. |
| 6.6 | **Anticipation** (5) | Predictive · Reactive · Proactive · Adaptive · Patterned | Axis 4 (the *sen* tiers) | **PASS, flag F-A1** | Reactive = *go-no-sen/sen-no-sen*; Proactive = *Vor*. But the *sen* scheme is split across 3 systems — F-A1. |
| 6.7 | **Reaction** (5) | Hand-led · Body-led · Yielding · Pressing · Voiding | Axis 2/4 (Silver's *true times*) | **PASS (strong)** | Implements Silver's true-times exactly — see below. Resolves the Part-1 "where are the true times?" question. |
| 6.8 | **Commitment** (5) | Cautious · Decisive · Escalating · Burst · Sustained | Commit-depth / Silver's over-commit | **PASS, flag F-A2** | Burst = the over-commit penalty (Silver's false time); but **Escalating has no historical anchor** — F-A2. |
| 6.9 | **Disengage** (5) | Clean · Pursuing · Defensive · Drawing · Sudden | Withdrawal (*Abzug*) | **PASS** | Pursuing = the German *Nachreisen* (counter-pursuit). v32 develops withdrawal further than the sources (which barely theorise *Abzug*). |

---

## THE HEADLINE CORRESPONDENCES (record — they confirm grounding and resolve an earlier question)

Review-mode permits positives that confirm grounding. These three are the load-bearing internal-coherence signals at the aspect layer (still under the circularity caveat).

### C-1 — The Reading channels comprehensively cover the manual's cognitive-modes typology
The manual's central structural claim is that combat traditions differ in *how they perceive the opponent* — seven cognitive modes. v32's Reading layer maps onto them almost completely:

| Manual cognitive mode | v32 home |
|---|---|
| Tactile (*Fühlen* / bind-feel — **T3, the strongest universal**) | **Tactile** channel (§6.5) |
| Temporal-spatial (tempo / commit-timing) | **Kinetic** channel |
| Geometric (Spanish positional) | **Geometric** channel |
| Kinetic-rhythmic (Filipino cadence) | **Rhythmic** channel |
| Intentional / consciousness-theoretical (*mushin* / intent) | **Intent track** (§10, separate) |
| **Cosmological** (Chinese *wuxing* / Indian *marma* overlays) | **Thread** channel (Valoria's own metaphysical-state read) |
| Biomechanical (provisional; Silver's true-times) | *not a perception mode* — lives in Reaction/Commitment (C-2) |

The notable insight: the manual's **cosmological mode** — the one most *outside* the Western dueling paradigm, and which I flagged in the bridge as a dimension v32 "does not enter" — actually *does* have a v32 home in the **Thread** channel. Reading the metaphysical Thread state is structurally Valoria's cosmological-mode perception. So every one of the manual's perception modes has a v32 channel; only the "biomechanical mode" sits elsewhere (because it is a movement principle, not a perception). This is the strongest structural correspondence in the whole grounding exercise.

### C-2 — The Reaction families implement Silver's *true times* — resolving the Part-1 open question
In the weapon pass I noted Silver's true-times biomechanics (fast-part-first beats slow-part-first; over-commitment exposes you) were *not* in Weapon Speed and must live elsewhere. They live **here**, in the §6.7/§7.2 reaction families:
- **Fast-part reactions** (Hand-led, Voiding, Pressing) — "punish hesitation," strong vs probe/light, **overrun by deep commitment**. This is Silver exactly: the fast hand deflects a light attack but cannot stop a full body-and-foot commit.
- **Whole-body reactions** (Body-led, Yielding) — "punish overcommitment," weak vs light, **strongest vs deep/full** (Yielding-vs-Full is the archetype). This is the reversal of an over-committed opponent's force — the consequence Silver warns the over-committer about.

The two families *are* the two halves of Silver's true-times doctrine, encoded as a 2-parameter formula (baseline + depth-slope). Strong grounding, and it closes the Part-1 thread.

### C-3 — The two strongest convergent universals are both direct aspects
- **Bind-as-information-channel** (the manual's strongest cross-cultural result — independent convergence of *Fühlen / sentimento del ferro / ting jin / chi sao / hubud*) = the **Tactile** reading channel (§6.5), active in the In-bind state.
- **Convergent ~5-guard reduction** (Agrippa's 4, the Vier Leger, the 5 kamae, all derived from natural body geometry) = the **5-stance set** (§6.1), with Forward-point = Agrippa's deduced thrusting line and the **transcendence** caution (Musashi's "stances and no stances") captured by the Single-strike Tradition's **Stance-flux** technique.

---

## THE FINDINGS WITH TEETH (the divergences)

### F-A1 — The initiative (*sen*) scheme is distributed across three systems (legibility cost)
The manual's cleanest initiative finding is the unified three-tier scheme — *go-no-sen* (after) / *sen-no-sen* (simultaneous) / *sen-sen-no-sen* (pre-commitment), with the Japanese pre-commitment tier the finest. In v32 this single concept is **split across three places**: **Anticipation** (Reactive = read-during-commit; Proactive = take-initiative), the **Intent track** (§10 Tier 4 Pre-empt / Tier 5 Master = the pre-commitment read), and **Commitment** (depth = how hard you initiate). A player who wants to build "counter-initiative" must coordinate Anticipation + Reaction + Intent + Commitment across four aspect categories.
- **Bearing:** **NERS-E** (the player intuiting a coherent capability from simple choices). This is the same family of concern as the existing `ners_verdict` E-findings — the historically-unified concept is mechanically dispersed. Not a defect (the dispersion buys granularity), but a real legibility cost worth naming.
- **Not proposed here:** whether to surface a unified "initiative" view over the dispersed mechanics is a design call for Jordan.

### F-A2 — "Escalating" commitment has no historical anchor (the one ungrounded aspect spec)
`§6.8` Escalating = "depth raises by 1 per round (forced); cannot lower depth back." Every other Commitment spec maps to the record (Burst = Silver's over-commit; Decisive = the controlled committed strike; Cautious = staying shallow/safe; Sustained = the long exchange). **Escalating does not** — forced, irreversible escalation is a *game archetype* (momentum / berserk build), not a documented historical commitment pattern. It is a reasonable game-design choice; it is simply the **one aspect specialization in §6 that is a pure invention** relative to the precedent record.
- **Status:** `[INTENT UNDETERMINED]` from a *historical* standpoint — defensible as game design, ungrounded as history. Flag for Jordan: keep as a deliberate archetype, or reconsider.

### Minor notes (recorded, low-priority)
- **F-A3 — two adjacent half-sword grips.** `Short grip` (a static half-sword *hold*) and `Half-grip-available` (the dynamic *ability to transition* mid-bout) are close. They are genuinely different (state vs capability), so probably not a Lesson-1 redundancy — but adjacent enough to verify the distinction is load-bearing.
- **F-A4 — footwork is positional, not tempo-generating.** The manual treats footwork as *the substrate of measure and tempo* — you *create* an opening/tempo by stepping. v32 footwork affects the Approach Pool and Bout movement options (positional), less a direct initiative/tempo generator. Flavour observation; the tempo-generation lives in Approach + Commitment instead.

---

## NERS / DIAGNOSTIC CROSS-REFERENCE & DISPOSITION

| Finding | NERS criterion | Diagnostic lesson | Severity (grounding lens) |
|---|---|---|---|
| F-A1 *sen* distributed | E (intuitability) | — (legibility, not a resolution defect) | **Moderate** |
| F-A2 Escalating ungrounded | N (necessity of the spec) | A5 (don't add apparatus without need) | **Minor** |
| F-A3 two half-sword grips | N / E | Lesson 1 (one variable, one role) — *probably passes* | **Minor** |
| F-A4 footwork positional | (flavour) | — | **Cosmetic** |

**Relationship to the prior outputs.** This completes the grounding coverage the Part-1 disposition named ("extend the lens to §7 Reaction families and §6 aspects"). Findings here are orthogonal to `ners_verdict_combat_v32.md`'s balance findings, except **F-A1 reinforces that verdict's E concerns** (dispersed complexity) from the historical angle. **C-2 closes the Part-1 open question** (Silver's true-times are in §6.7/§7.2, not Weapon Speed).

**Editorial-ledger disposition.** Design-review flags, not canon-consistency gaps — none *forces* a `canon/editorial_ledger.jsonl` entry. If Jordan wants any logged, **F-A2 (Escalating)** is the one with a concrete keep/cut decision attached. (A ledger write needs a commit; branch protection finding B6 currently blocks PAT commits to main → would stage inline + flag `[DRIFT]`, not commit. Not done here.)

**Grounding coverage is now complete for the three design layers** — weapons (§8, Part 1), schools (§5, Part 1), aspects + matchup mechanics (§6/§7, Part 2). The whole-design picture: combat_v32 is **internally very coherent with the historical record it was apparently built from**, with the strongest convergent universals directly represented and only a short list of divergences (the staff handling F-W1, the short-blunt gap F-W2, the distributed *sen* F-A1, the ungrounded Escalating F-A2) — each a design flag, none a canonical defect. The remaining work is a different mode: the full per-system 4-stage NERS on the flagged items (staff first), and feeding the grounding findings into the I-17 balance sim as calibration inputs.

---

`[CONFIDENCE: high — every v32 claim cites the fetched §6.1–§6.9 / §7; every historical claim cites the seven-axis precedent doc]`
`[CONFIDENCE: medium — on the "PASS" verdicts specifically, per the circularity caveat (high internal consistency, not independent validation); strongest caveat at this layer because §6 is the same tradition-transcribed vocabulary]`
`[SELF-AUTHORED — bias risk: v32 is prior-Claude work; the aspect layer is the most flattering to it, so I (a) led with the circularity caveat, (b) actively hunted divergences and found two real ones (F-A1, F-A2) plus two minor, and (c) framed C-1/C-2/C-3 as internal-coherence signals, not validation]`
`[READ: combat_v32_proposal.md §6.1–§6.9 (L642–753, this session); §7.1/§7.2 (prior turn, in context); §10 Intent referenced not deep-read; seven-axis precedent doc + PI <definitions> for axes/NERS]`

*Grounding documents (external, heuristic — not canon): `combat-manuals-seven-axes-throughlines.md`, `manual-vs-combat-v32-bridge.md`, `blunt-weapon-martial-traditions-completed.md`. v32 source: `designs/proposals/combat_v32_proposal.md` (PROPOSAL; canon baseline `designs/scene/combat_v30.md`). Companion to `combat-v32-historical-grounding-test.md` (Part 1: weapons × schools).*
