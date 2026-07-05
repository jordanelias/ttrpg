# Fable 5 Audit — The Social Contest System

## Status: PROPOSED (audit findings — Jordan review)
## Date: 2026-07-05
## Lane: SC · Branch: `claude/fable5-social-contest-audit-oxibtb`
## Method: 4 Sonnet evidence dossiers + 1 independent Sonnet critic; all verdicts rendered by Fable 5 (orchestrator). Read-only — no canon, params, code, ledger, or handoff edits. Evidence: `01_workings/`; criteria: `00_grounding/`.

---

## §0 · Verdict summary

| # | Dimension | Verdict | One-line basis |
|---|---|---|---|
| D1a | Code architecture — intrinsic kernel quality | **PASS (flag calibration)** | Best-documented, best-self-tested subsystem in `sim/` (385 seeded CI-gated checks, honest stub registries) — but 78 `[SEED]` constants and a non-canonical pool formula make the balance surface provisional beneath a rigorous skeleton. |
| D1b | Code architecture — integration reachability | **FAIL** | The promoted kernel has **zero non-test callers**; the campaign loop routes contests to the deprecated legacy stub and structurally defers every contest scene; the built `domain_echo.py` is orphaned. The subsystem is an island: rigorous inside, disconnected outside. |
| D2 | Qualitative NERS (North-Star) | **PARTIAL** | N and Q-elegant pass; Ω(a) cross-scale consequence is declared-only at every level; Q-robust partial-fails on formula coexistence and the inert Face/Rattled channel. |
| D3 | Throughlines / meta-throughlines | **PARTIAL FAIL** | Every declared throughline touch (T-03, T-14, T-16, T-23) is doc-only — none reaches the kernel; the registry itself cites the contest under retired vocabulary (Piety Track, Composure), so the causal-spine index has not tracked the CR3 rebuild. P-14 fails at kernel depth. |
| D4 | Playability / player experience | **PARTIAL** | Agôn's legibility discipline is the corpus's best (three-question walk: pass/partial/pass, hidden values degrade to consequence classes) — but one exchange demands ~13 per-decision consults against a 3–4 ceiling, ¾ game-shapes cannot be walked at all, and the CANONICAL UI doc's contest section specifies the pre-CR3 system wholesale. |
| D5 | Interactions (echo · emergence · prose) | **PARTIAL FAIL** | Domain-echo transport fails executable and has an unreconciled two-scheme spec conflict (§5.4 band-keyed vs §6 genre-keyed); the emergence feed is a near-miss (kernel emits a structured Chronicle nothing consumes); prose doctrine is coherent with the mechanics (the Ratchet holds) but the code-side narrative surface violates P-03. |
| D6 | Viability path | **Recommendation** | Reconcile the small spec-conflict set (P0), then wire the consequence spine (P1: kernel → dispatch → domain_echo), put a human in front of Agôn (P3-lite), and only then build Stage 4 (P2) with the deferred guardrails as entry criteria. Calibration (P4) last. §6. |

**Headline judgment.** The social contest system is a well-theorized engine standing on a gap where its
game should be. Its intrinsic craft is the best in the corpus — the bet-under-uncertainty armature, the
honest stub registries, the 385-check oracle. But *as a gaming experience it does not yet exist*: no
campaign can reach the kernel, no outcome changes the world, no throughline passes through it, no human
has played it, and three of its four game-shapes are registered promises. The prior audits (PR #77 and
the gate chain) correctly identified Stage 4 as the biggest *content* gap; this audit's central addition
is that the **consequence spine** — reachability plus echo transport — is the binding constraint on
viability, is cheaper than Stage 4 (most of its parts already exist, unwired), and is partially blocked
by a small set of spec conflicts that only Jordan can resolve.

Finding tags per `finding_status.md`: 8 KNOWN-TRACKED (cited, not re-litigated), 3 KNOWN-UNTRACKED
(deepened), and the NEW findings N-1..N-10 introduced below (all survived or were qualified by the
critic pass, `01_workings/critic.md`).

---

## §1 · D1 — Code architecture

Evidence: `01_workings/dossier_code_architecture.md` (agent A) + orchestrator reads of
`sim/cross_scale/scene_dispatch.py`, `references/module_contracts.yaml`.

### 1.1 Intrinsic quality — PASS (flag calibration)

The 13-module kernel (`sim/personal/contest/`, 5,858 LOC) is the most disciplined code surface in
`sim/`: near-every canonical constant carries an inline params/ED citation; the `MECHANICS` registry
self-reports 21 WIRED / 1 PARTIAL / 3 STUB across 25 rows rather than over-claiming
(`wrapper.py:270-338`; count settled by orchestrator re-derivation after dossier A and the critic
disagreed — critic.md bonus catch); the
seeded oracle gates CI on an exact 385-check count (`sim/tests/test_contest_kernel.py:84`). Stubs are
structurally honest — registered rows that raise loudly, not silent no-ops.

Flags:
- **78 `[SEED]` tags** (census: dossier A §5; tag-occurrence count re-verified by the orchestrator —
  the critic's lower figure counted unique constants, several of which carry multiple tags) — the
  entire balance surface beneath the structural skeleton is provisional. Two calibration constants (`RES_FLOOR`, `REBUT_CAP`, `resolver.py:33,35`)
  are of `[SEED]` character but lack the tag, weakening the census as a debt tracker.
- **N-2 — two contradictory Argue-pool formulas are simultaneously live.** The deprecated stub
  implements canon verbatim — `(Primary×2)+History−Wounds+fatigue`, floor 1
  (`contest_legacy_stub.py:111-127`) — and is the formula the campaign loop would actually reach. The
  promoted kernel's `Pool.size(faculty)=max(5, faculty*2+3)` (`primitives.py:208-211`) is `[SEED]`,
  drops History/Wounds/fatigue, and raises the floor from 1 to 5 (erasing the low-pool regime the
  2026-05-28 diagnostic measured down to 2D). Which formula is canon for the kernel is an unmade
  decision, and it gates calibration, the rolling-engine re-verdict (§2.5), and any Godot export.

### 1.2 Integration reachability — FAIL

The verified chain (dossier A §1):
1. `mc_v18` → `season` → `scene_dispatch`; the **only** contest trigger is Stability Crisis, whose
   context omits `parties` by design (`scene_dispatch.py:63` — "derivation bridge gap (flagged)").
2. `_resolve_slot` therefore defers every contest scene
   (`scene_dispatch.py:100-104`) — **N-1**: in practice, contest resolution is dead code from the
   campaign loop's perspective.
3. Even the hypothetical resolved path calls `contest.run_contest` — the **deprecated legacy stub**
   re-exported by `__init__.py:30-36` — never the promoted kernel. Repo-wide grep: **zero non-test
   callers** of `build_contest`/`resolve_contest`/`Bout`.
4. Downstream, the feedback call passes an empty dict — `zoom_out({}, world)`
   (`scene_dispatch.py:116`) — so **N-5**: `sim/cross_scale/domain_echo.py`, a complete and
   individually-correct implementation of scale_transitions §5, **has no caller anywhere**. The
   consequence machinery exists at both ends; only the connective tissue is missing.
5. `parliamentary_vote.py` (the one module that writes a Mandate penalty to faction state) is itself
   never called from `mc_v18` (dossier C §1.4).

Both gaps are self-flagged in code comments (the module-level "CONTEXT-DERIVATION BRIDGE GAP" and
"OUTCOME→ECHO MAPPING GAP" notes, `scene_dispatch.py:16-32`) — the engineers knew; no ledger item
tracks either. The deferral discipline itself is *correct* (no fabricated actors — the gap is honest),
but the consequence is that five ratified gate-stages of engine have never resolved inside a campaign,
and the campaign-level regression's golden output is structurally incapable of noticing contest
regressions (its docstring: the happy path "does not touch any of sim's NotImplementedError stubs").

### 1.3 Contract and registry currency — N-3

`references/module_contracts.yaml:425-447` predates the entire rebuild: `resolver: dice_pool` (the
kernel is δσ since CR2); all five declared Key/state literals have **zero hits** in the kernel; no
`godot_home`, no `typed_params` (combat's entry has both). A Godot developer binding to this contract
would implement the wrong resolver against Keys the reference implementation never emits. The contract
is the port's map, and the map is of the previous city.

---

## §2 · D2 — Qualitative NERS (North-Star walk)

Evidence: `01_workings/dossier_design_and_ners.md` (agent B). Framework:
`references/throughlines_meta.md` (N → Ω → Μ/М/Τ → Q).

| Clause | Verdict | Basis |
|---|---|---|
| N — Necessity | **PASS (flag 1)** | Every budget item (8 proceedings, 4 adjudicators, 4 styles, 4 interactions, 3 trackers, 4 armature axes) carries a doc-cited earn; the flag is that the realized game cashes only a fraction of it (KT-1), and the deliberation-critique trilogy's depth remains read-cited-not-applied. |
| Ω(a) cross-scale consequence | **FAIL (executable) / declared-only** | §6 Domain Echo + §6.1 Obligations are well-specified prose; kernel emits nothing faction-ward; `faction.py` only *consumes* Mandate as vote weight; the one stat-writing module is uncalled (§1.2). |
| Ω(b) personal transformation | **PARTIAL** | Face is deliberately transient (doc-consistent); Conviction Scar (§6.2) and Beliefs (§9.5) are the transformation channels — both doc-only; `Contestant` is immutable by construction, so no outcome persists onto a character in code. |
| Ω(c) autonomous world | **PARTIAL** | The armature gives adjudicators genuine hidden conviction (wired, the subsystem's best Ω(c) asset); but no NPC-initiated-contest path exists, and the npc_behavior side of the 2-cycle dampers is still `[OPEN — Jordan]`. |
| Ω(d) non-dominance | **PARTIAL** | KU-1 refined: the Recall/Corroborate/Prep/Findings stack is **entirely unimplemented in the kernel** — the +8D doc-math hazard cannot currently manifest; it is a spec bug to cap *before* wiring, not a live exploit. KU-2 confirmed: the audience-boost dimension of Appraise is a solvable public lookup (`guilds_boost_for` is deterministic); only the armature dimension is reveal-protected. KU-3 confirmed and sharpened: Face is monotonic-up (`primitives.py:83-90` — "Standing.strip() is NEVER called… Face has NO strip/strain channel wired"), Rattled unrealized; the CR3 three-tracker tradeoff triangle is running on two legs. |
| Q-robust | **PARTIAL FAIL** | N-2 formula coexistence; audience-resistance PARTIAL (derived, unplumbed, and static where ED-295 Option D specifies per-exchange erosion); KU-3; continuous-`t` band resolution where prose specifies integer cuts (compatible at integers, unspecified between them). |
| Q-smooth | **PARTIAL** | Terminology drift at three seams: `params/contest.md:98` still reads "Direct/Indirect" against its own ED-897 rename; "Piety Track" vs "Persuasion Track" split-brain across the doc corpus (§5.2); retired "Composure" persists in the throughline registry and UI doc. |
| Q-elegant | **PASS** | The armature/rhetoric/appraise triad is genuinely elegant — a continuous bet-under-uncertainty mechanism, never a lookup table; the 5-band track resolution correctly folds §6's Total Victory thresholds; `venue_brief()` shows the design can self-describe. |

### 2.5 Rolling-engine annex — prior verdict is stale-based (N-10)

The 2026-05-28 NERS-COMPLIANT verdict stands on a component model the rebuild has since replaced
wholesale: its success-counting pool, 5-type interaction taxonomy (CLASH/CROSS/COMPETITION/DIVERGENCE/
AMPLIFY), Composure resource, and 2D floor all have no code counterpart (dossier B §3). Nothing found
invalidates the *conclusion* — TN stays 7, the armature δσ is bounded (+0.50σ on-axis under a 1.5σ tanh
ceiling) — but the verdict's basis no longer describes the system. The diagnostic should be re-run
against the σ-substrate kernel once the pool-formula decision (N-2) lands; until then the subsystem's
NERS-compliance citation is an inherited label, not a current measurement.

---

## §3 · D3 — Throughlines and meta-throughlines

Evidence: `01_workings/dossier_design_and_ners.md` Part 2.

| Throughline | Declared in doc | Wired in kernel | Note |
|---|---|---|---|
| T-03 Inseparability (temporal-axis conflict penalty) | Yes — §9.4, PP-351 | **No** | Zero thread/weave/coherence hits in any resolution module. |
| T-14 Conviction as Moral Architecture | Yes — but cited as "Piety Track, Composure", both retired names | Trackers exist (Face/Concentration); the Conviction chain itself is npc_behavior's scope | Registry citation stale. |
| T-16 Knot Propagation (Solidarity Resonant Style) | Yes — under **T-16**, not T-17 as commonly cited | **No** — named-and-rejected as the armature's 4th axis (correctly: it is Knot-gated/relational, wrong for a third-party judge) | Citation-boundary confusion in downstream docs (including this audit's own grounding, corrected here). |
| T-23 NPC Arc Emergence | Yes — §6.2 Conviction Scar is the feed | **No** (boundary is npc_behavior's; no Scar hook exists on either side) | Registry cites retired names again. |
| T-24 Convergence Markers | T-24's own Systems line does **not** name social contest; only COLLISION E carries a contest *payload* (Grand Debate as resolution mechanism) | **No** (F-2: the engine has no engine — KT-8) | Contest is a consequence-venue for convergence, not a vector of it. |

**P-14 — the direct bar — fails at kernel depth.** §9.3/§9.4/§9.4b are present and well-specified in
the doc (declaration-visible weaving, between-exchange ops with genre locks, the certainty-indexed
adjudicator response table); the kernel contains zero thread hooks (KT-5 deepened). Under P-14's own
terms — the videogame mode *must* express inseparability — the executable social contest currently
cannot: a practitioner in a rebuilt-kernel contest is mechanically indistinguishable from anyone else.

**N-9 — the throughline registry has not tracked the contest rebuild.** T-14 and T-23 cite the contest
via two retired tracker names; the Solidarity citation sits under a different throughline than
downstream docs assume; T-24's systems line and the §VI marker triggers never name the contest even
though COLLISION E resolves *through* one. The registry is the corpus's causal-spine index — for this
subsystem it currently indexes the pre-CR3 system. Verdict: **PARTIAL FAIL** — the throughlines exist
as design intent, none passes through the running system, and the index that should catch this is
itself stale.

---

## §4 · D4 — Playability and player experience

Evidence: `01_workings/dossier_playability.md` (agent D).

### 4.1 Dramatic-legibility walk (the canonical bar)

| Game | whose position at risk | what each actor wants | if no one acts |
|---|---|---|---|
| Agôn | **answerable** (Track meter + bands, Face bar) | **partial — by design** (stakes shown; armature residual deliberately hidden, and the doc pre-empts misreading this as opacity) | **answerable** (Forfeit dual-branch screen; Chain/Deadlock rules) |
| Negotiation | N/A — unbuilt | N/A | prose-only |
| Inquiry | N/A — unbuilt | partial-from-prose | N/A |
| Consensus | N/A — unbuilt | flavor-table only | N/A |

Agôn's discipline — "every number the resolver uses is a number the player can see before committing,"
hidden values degrading to consequence classes — is the correct one, and PR #77's independent lens
agrees (KT-7 lineage). The walk simply cannot be run for ¾ of the design.

### 4.2 Cognitive load — N-7

One Agôn exchange requires **~13 recurring per-decision consultations** (pool, TN, genre bonus, boost
table, armature reveal state, both Faces, Concentration, Track, Doubt Marker, interaction-type
prediction, Recall availability, Momentum — dossier D §2's enumeration; the critic notes the exact
digit is not independently re-derivable, and the conclusion is robust to ±2 items), against the
immersion audit's **3–4 ceiling for personal scenes** and above even its "7 at ceiling" strategic
allowance. The walkthrough's screens
compress three of these (bars, post-roll interaction naming, style-cards-as-single-pick) and leave ten.
This is a *design-shape* problem, not a UI-polish problem: legibility-per-item is excellent, but the
item count is triple the corpus's own stated budget, and no onboarding/complexity-gating doc exists
anywhere (dossier D §3.5). Verdict weight: this is the strongest reason to put a human in front of
Agôn *before* Stage 4 multiplies the shape count (§6).

### 4.3 The UI reference actively misleads — N-6

`designs/ui/valoria_ui_ux_v4_1.md` Part 6 — the contest section of the corpus's only CANONICAL
player-facing spec — specifies the **pre-CR3 system wholesale**: "Piety Track displayed", "Composure
damage", Stance-Triangle reveal, Resonant-Style targeting (dossier D §3.2). This is deeper than the
Taint/CD contamination PR #77 flagged (KT-7): a Godot developer implementing the contest screen from
the canonical UI doc would build the wrong contest end-to-end. The current-era artifacts that should
replace it (the DRAFT walkthrough; the ED-1058 flavor table) do not cross-reference each other.
Smaller gap in the same class: Grand Contest's once-per-source Recall rule requires the player to
remember exhausted sources across 5 exchanges with no depicted tracker anywhere.

**Verdict: PARTIAL** — the one built shape has the corpus's best legibility discipline and its worst
consult-count; the other three shapes are unwalkable; the canonical UI reference describes a retired
system.

---

## §5 · D5 — Interactions: domain echoes · narrative emergence · prose

Evidence: `01_workings/dossier_interactions.md` (agent C).

### 5.1 Domain-echo transport — FAIL, with a spec conflict on top

Executable: fails at every link (§1.2). But the deeper finding is **N-4 — the two echo specs disagree**:
`scale_transitions_v30.md §5.4` keys the Debate echo by **track band** (winner +1 Mandate, loser −1 if
institutional, regardless of genre) while `social_contest_v30.md §6` keys it by **genre won** (Memory →
Mandate; Projection → +1D Domain Action; no loser-penalty row at all). They agree only that Compromise
fires nothing. Neither doc references the other's scheme; PP-108 never appears in the contest head.
Compounding it, §5.4's tracker name "Piety Track" resolves through the glossary to a *different
canonical doc* (`conviction_track_v1.md`) than the contest head, and `params/bg/` uses "Piety Track
(PT)" for an unrelated per-territory stat — **one name, two referents, three docs** (N-4b). Until
Jordan picks one keying scheme (or specifies their composition) and one name, Stage-4 echo wiring is
blocked at the spec level, not the code level.

### 5.2 Narrative-emergence feed — PARTIAL FAIL (a near-miss)

The prose corpus shows the contest is *already* the connective tissue of the strongest emergent chains —
NEW-S24's Obligation-vs-Chain-Contest escalation incentive is exactly the "no single decision caused
this" emergence the arc-generator demands, produced by two mechanics interacting as designed. But the
mechanical feed is absent end-to-end: only COLLISION E among the 8 convergence markers even carries a
contest payload (as resolution venue, not trigger); the kernel's one structured outcome record —
`narrative.py`'s `Chronicle` (winner, shape, turning point, lead changes, decisive appeal/ground) — is
consumed by **nothing but its own tests**; and the cross-scale `articulation.py` chronicle stub is
`NotImplementedError`. **N-8a:** the Chronicle is precisely the artifact an arc-generator or
convergence-detector would want, already computed, already shaped — an unconsumed asset, which makes
this the cheapest genuine wiring win in the whole audit.

### 5.3 Prose surface — PARTIAL

**The Ratchet holds — a coherence PASS worth stating plainly.** The mechanics do not violate the
Ratchet Principle; they implement it. Compromise is defined as deferral ("the tension is deferred, not
resolved") generating a Priority-1 crisis next season; three Compromises harden into cold equilibrium —
escalation with no mutual-accommodation exit, exactly the doctrine. The prose skill and the contest
mechanics were evidently designed from the same instinct.

Two real gaps:
- **N-8b — the code narrative surface violates P-03.** `Chronicle`/`classify()` carries no
  focalization/chronicler field and renders neutral omniscient summaries ("[REVERSAL] X came from
  behind…"). P-03 admits no neutral narrator; the prose skill mandates routing through one of four
  chroniclers. If Chronicle output ever reaches a player (the natural Stage-6 move), it must acquire a
  perspective parameter first — cheap now, expensive after.
- **Narration guidance is near-zero**: one "GM narrates" clause and one Conviction-Scar template line
  are the entire contest-outcome narration spec. The numbers-visible walkthrough and the numbers-hidden
  prose doctrine are *not* in conflict — they govern different surfaces (screen vs prose), and the PC's
  "genuinely omniscient" vantage licenses both — but no doc says so, and Stage 6 will need the boundary
  drawn explicitly.

---

## §6 · D6 — Viability: how best to pursue the social contest as a gaming experience

The evidence supports a clear sequencing judgment. The lane's current plan (Stage 4 next) treats
*content* as the binding constraint. The audit shows the binding constraint is *consequence*: a contest
no campaign can reach, whose outcome changes nothing, is not yet a game — it is an engine with
excellent posture. And the consequence spine is cheap: most of its parts exist, built and orphaned.

| Path | What it is | What it unblocks | Cost/risk | What stays broken if skipped |
|---|---|---|---|---|
| **P0 · Spec reconciliation** (prerequisite batch) | Jordan decisions: echo keying (§5.4 band vs §6 genre — or their composition); Piety/Persuasion/PT naming; kernel pool formula (N-2); module-contract refresh (N-3); cap the Recall/Corroborate/Prep/Findings stack in prose (KU-1) | P1, P2, P4, the rolling-engine re-verdict | Low — a decision docket, not a build | Echo wiring blocked at spec level; calibration aims at an unchosen formula |
| **P1 · Consequence spine** | Route `scene_dispatch` → kernel API (retire the stub path); author the party-derivation bridge (canon-backed, keeping the no-fabrication discipline); map Bout outcome → the already-built `domain_echo.py`; call `parliamentary_vote` from the loop | The kernel finally runs in campaigns; Ω(a) becomes measurable; the campaign regression can actually guard contests; N-1/N-5 close | Medium — the derivation bridge is real design work; everything else is connective code | Five gate-stages of engine remain unfalsifiable in situ; every downstream verdict stays hypothetical |
| **P3-lite · Human-plays-Agôn slice** | The walkthrough → a minimal interactive harness (terminal or bare Godot scene) over the existing kernel; run the canonical three-question test with a human; measure the 13-consult load empirically | The playability bar (which "requires a human and a screen") gets its first real data; UI-compression decisions before Stage 4 multiplies shapes; supersedes v4.1 Part 6 (N-6) | Low-medium — kernel and walkthrough exist; no campaign wiring needed (parallel to P1) | Stage 4 builds three more shapes atop an untested interaction model with a known 3× load overrun |
| **P2 · Stage 4 four games** | Consensus (promote-existing from `faction.py`), then Negotiation/Inquiry (author-new) — with wire-time guardrails as entry criteria: Face/Rattled strain channel (KU-3), stack cap (KU-1), thread hooks §9.3–9.4b (P-14), Chronicle focalization (N-8b) | KT-1 (the lane's known highest content leverage); ¾ of the design becomes real | High — the largest build; Negotiation/Inquiry are genuinely new systems | The "one game wearing eight venue skins" ceiling on choice density |
| **P4 · Calibration + typed params** | The 78-`[SEED]` sweep, typed engine-params export, rolling-engine re-run | Godot port readiness; balance trust | Medium, but wasted if run before P0/P1 (calibrating an unreachable kernel against an unchosen formula) | Balance surface stays provisional — acceptable while shapes are still moving |

**Recommended sequence: P0 → P1 ∥ P3-lite → P2 → P4.**

The argument in one paragraph: every prior gate validated the engine against itself; nothing yet
validates it as a *game*. P0 is a one-docket unblock. P1 converts the subsystem from island to organ —
and it is the only path that makes Ω(a), the throughline traces, and the emergence feed *testable*
rather than declared. P3-lite is the only path that produces evidence about the 13-consult problem,
and it must precede Stage 4 because Stage 4 multiplies interaction shapes — building three new games
on an interaction model that has never met a player risks quadrupling a known overrun. P2 then lands
on a system where a new game-shape can be reached by a campaign, echoes into the world, and gets
played by a human in the same week it is built. P4 last, once the formulas it would calibrate are
chosen and reachable. The independent critic built the strongest available case for Stage-4-first
(the ratified workplan's own ordering; the derivation bridge being open-ended design work) and
concluded it does not survive contact: the workplan never weighed reachability, and Stage 4 built
first still ships games nothing can reach (`01_workings/critic.md`). Every step above is a candidate
in `ed_options.md`, not a decision — the sequencing is this audit's judgment; the picks are Jordan's.

---

## §7 · Provenance

Dossiers A–D (`01_workings/`): Sonnet, evidence-only, parallel, read-only tools. Critic E: Sonnet,
independent (draft + charter only). Verdicts, reconciliation, and this synthesis: Fable 5. Finding
novelty ledger: `finding_status.md`. Candidate ledger entries (deliberately unfiled): `ed_options.md`.
Currency-surface observations recorded, not fixed (read-only): `HANDOFF_SC.md` trails Gate C by one
stage; `CURRENT.md`'s row still says "Stage 1a landed".
