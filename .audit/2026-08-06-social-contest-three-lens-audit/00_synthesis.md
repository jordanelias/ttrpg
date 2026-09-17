# Social Contest — Three-Lens Pessimistic NERS Audit + Upload Delta

## Status: PROPOSED — audit findings filed; the two design forks (§5) need Jordan
## Date: 2026-08-06 · Lane: SC · Branch: `claude/social-contest-audit-n63p07`
## IDs: ED-SC-0017 .. ED-SC-0022 (allocated from `references/id_reservations.yaml`, next_free 17 → 23)
## Method: three structurally-independent read-only Fable 5 lenses (`valoria-critic`: Read/Grep/Glob only),
## relayed agonist→antagonist per CLAUDE.md §10; every gating claim re-verified by the orchestrator
## against the working tree before being banked.

---

## §0 — Verdict

**The social contest is not one system with gaps. It is three resolution models wearing one name, and
the one the campaign actually runs is the one nobody designed.**

- **Model A — the canonical prose** (`social_contest_v30.md` §4): paired exchanges, Appraise, style
  picks, CLASH/REINFORCE/CROSS/TIE margin algebra against audience resistance, strain → Face →
  Rattled, Doubt Markers, forfeits, rolled first-to-speak. **It has no engine.** Not "partially
  wired" — no engine.
- **Model B — the promoted kernel** (`sim/contest/resolver.py`): a budgeted per-move loop over
  stasis grounds and rhetorical appeals, with a reserve economy, hidden-weight evidence dossiers,
  a Nyāya fault/clinch catalogue, readiness/resonance/leak, and institutional pressure. **It is
  genuinely good, and it is absent from the canonical head.** No section of `social_contest_v30.md`
  describes the loop a player would actually play.
- **Model C — the deprecated legacy stub** (`contest_legacy_stub.py`): a bare pool-compare. Still
  exported on the live package API, still carrying a struck formula, and until ED-SC-0006 it was
  the only thing the campaign called.

Everything ratified at Stage 3 / Gate C — the adjudicator armature, CR4's stasis×genre bonus, CR5's
self-Face backfire — is **unreachable from every production path**, because `build_contest` has no
parameter through which a Style can be chosen (`wrapper.py:101-102`) and `_resolve_agon` constructs
`Bout(...)` without an armature (`wrapper.py:197`). The live campaign path resolves every contest as
`logos_spammer` vs `logos_spammer` (`scene_dispatch.py:311`) — two identical loops differing only in
a faculty scalar.

And the thing the design exists to say, it cannot say. `social_contest_v30.md:310` and `:358` both
promise that a contest's consequence is *"not just a stat change"*. **Every wired output is a stat
change.** The one output shaped like a guard — the Projection channel's "+1D on the first Domain
Action pursuing that outcome" — was flattened into a stat delta at the interface because
`domain_echo` only carries numbers (`scene_dispatch.py:316-319`, which says so explicitly and
declines to fabricate it).

**Against the North Star** (`audit/2026-07-04-ners-qualitative-audit`): the subsystem currently
fails Ω-Intent clause 1 (cross-scale consequence — the consequence is a scalar), clause 3
(autonomous world — factions have no aims, memory, or patience), and clause 4 (non-dominance —
§3 below shows the prepared side wins exchange 1 at p≈0.93). It passes the dramatic-legibility test
only at faction scale, and only because five scalars are legible.

**The good news, and it is substantial: almost nothing needs to be invented.** The record primitive
this system needs already exists, single-owner, one subsystem over. The stacking cap Jordan is being
asked to pick a number for is already ratified canon. The burden token already exists in disguise as
four win-condition classes. The audit's dominant recommendation is not *build* — it is *compose*,
then *delete*.

---

## §1 — Method and verification discipline

Three lenses ran in parallel with disjoint mandates (primitives / mechanics / emergence), each
read-only by tool grant rather than by instruction — structural independence per CLAUDE.md §10.
Each was told to report NULL results explicitly and forbidden to assert without `file:line`.

Per §0.1 point 3 (*name the falsifier, or you have not attacked the result*), the orchestrator
independently re-verified every claim this report banks as load-bearing. The verification log:

| Claim | Verified how | Result |
|---|---|---|
| Audience resistance never read in resolution | `grep resistance resolver.py` | 3 comments, 0 code. Registry self-declares `PARTIAL` (`wrapper.py:318`) |
| `build_contest` cannot pass an armature | Read `wrapper.py:101-102`, `:197` | Confirmed — no parameter, no construction |
| `Contestant.charisma` never set by the adapter | Read `_as_contestant`, `wrapper.py:82-98` | Confirmed — `Face_current` would raise `TypeError` on `None×3` |
| Doc's "Standing.strip() is never called" is stale | Read `resolver.py:418` | **Doc is wrong against its own code** — `strip_points` fires on the CR5 foul |
| CLASH/REINFORCE/CROSS/TIE unimplemented | `grep` + read `derive_interaction` callers | Only tests and one *flavor line* (`agon_harness.py:458-463`) |
| Live path uses `logos_spammer` both sides | Read `scene_dispatch.py:285-320` | Confirmed, and documented in-code |
| Settlements `LedgerTag` is the missing Record primitive | Read `systems/settlements/sim/ledger.py:1-31`, `registry.py:101-107` | Confirmed — `Precedent`/`Grudge`/`Debt`/`Reputation`/`Leverage`, durable across succession |
| `world.casus_belli` has no producer | `grep` repo-wide | Confirmed — readers only; `parliamentary_transfer.py:22` says so |
| `tribunal.py` dropped the prior-conviction gate | Read `formal_grounds_check` | Confirmed — *"not yet ported"* |
| CR6's tanh soft-cap already ratified | Read `sigma_leverage.py:92,130-136` | `M_MAX = 1.5σ`, cited to `modifier_system_spec.md §3.1` |
| Stacking arithmetic | Recomputed from `MU_PER_DIE=0.40`, `SD_PER_DIE=0.80` (`sigma_leverage.py:100-101`) | P(win E1) = Φ(2.4/4.38) = **0.708**; with 4 Momentum, P(one-exchange Total Victory) = **0.62**. Lens 2's figures reproduce |
| `counterpuncher` self-clinches in canonical venues | Read `policy.py:45-54`, `modes.py` `allow_rebuttal` | Confirmed — `True` only on 2 non-canonical presets; 2 evasions = clinch loss (`primitives.py:267`) |
| `opponent_is_adjudicator` never set in production | `grep` repo-wide | Confirmed — tests only |
| Projection-primary stasis unreachable | Read the 8 proceedings' `start_ground` | Only `church_tribunal` overrides; rest default QUALITY; CONSEQUENCE/FEASIBILITY never a start |

**One finding a lens flagged as *observed, not ruled*, the orchestrator closed** — see F6 below. It
is a live bug, not a design question.

**Provenance caveat, stated loudly.** `CURRENT.md:151` names
`audit/2026-07-05-fable5-social-contest-audit/` as the artifact ratifying the current sequencing.
**That directory does not exist on `main`** — it went in the 2026-08-05 evacuation (ED-IN-0145).
Every "already ratified" claim in this report therefore rests on `registers/editorial_ledger_sc.jsonl`
and the Gate-A/B/C packets under `audit/2026-07-0{1,2}-contest-gate-*`, not on the audit text itself.
Separately, `params/contest.md` is cited **3× in the canonical head and 97× across the kernel** as the
provenance source for nearly every ratified number; `engine/params/` was evacuated the same day. The
content survives in `engine/engine_params/params_tables.yaml` (88 contest entries) — nothing is lost —
but the entire `source=` chain the MECHANICS registry uses to vouch for itself points at a deleted
file. **This is the anti-fabrication gate's own citation spine, and it is broken.** (ED-SC-0017.)

---

## §2 — The central structural finding (P1, NEW, intent: NOT-INTENDED)

### 2.1 The divergence is not drift; it is two designs

Doc-only (specified, zero engine): the Appraise roll as a costed action · per-exchange style picks ·
the entire CLASH/REINFORCE/CROSS/TIE algebra · strain, Charisma modifier ×3, Focus defence ×3,
Rattled, Knot-as-Face-buffer · Doubt Marker and Terminal Doubt · Regroup and Concede a Point ·
rolled first-to-speak and its transfer · Recall +2D, Corroborate +1D, Prep +1D, Findings +2D ·
Momentum spend · faction/audience boost +1D · resistance and its erosion · §11 Hybrid ·
no-adjudicator stall-with-consequences.

Code-only (shipped, undocumented in canon): the stasis ladder and the `shift` reframe move · the
fault/clinch defeat catalogue (barred device / self-contradiction / evasion / silence — the Nyāya
*nigrahasthāna* frame) · the `Reserve` per-move cost economy · hidden-weight evidence dossiers with
corroboration decay and `EVIDENCE_CAP` · `rebut` · institutional and public `Pressure` ·
`Readiness`/`Room`/leak · the 3×3 Aristotelian `RhetoricalWeights` matrix · the ethos/pathos/logos
appeal axis · `ProofBar`/`GraceThreshold`/`ThresholdRace`/`VoteAtClose` · nine non-canonical venue
presets · `SelfGating` on `hard` moves.

The two lists do not overlap **anywhere except the Persuasion Track's band thresholds.**

The sharpest instance: there is **no Style→Appeal mapping**. The player-facing "single style pick"
(`social_contest_v30.md:160`) and the kernel's appeal axis are orthogonal dimensions, so the
interactive harness has to prompt for both — its own code calls this WORKAROUND 4
(`agon_harness.py:77-82`) and flags it an open design question. It is tracked by no ED.

### 2.2 Consequences that follow mechanically

1. **Contest length is decided at setup, not played** (P1). §3 below.
2. **Two of seven exchange verbs are strictly dominated as specified** — Concede a Point pays
   1 track + 1 strain for +1D ≈ +0.25 expected track; Regroup pays 1 track and a forfeited exchange
   to refill a pool whose exhaustion costs ≈1.2 net once. Neither is ever correct in a 3-exchange
   Formal Contest.
3. **The Obscuring orientation is dominated contest-wide, not just in single-exchange proceedings.**
   ED-1060 was scoped to the final-exchange corner. The arithmetic: a Revealing win yields
   E[(m−1)⁺ | win] ≈ 2.1 immediately plus strain plus initiative retention; an Obscuring win yields
   0 movement and a marker worth ≈1.55 *conditional on the opponent winning a later exchange*, so
   ≈1.2 at exchange 1 of a Formal and exactly 0 at the last. Revealing dominates at every
   resistance value. **The 2×2 style grid collapses to Precedent/Vision — the exact Burning Wheel
   Point/Dismiss collapse (upload 1 §3.1, Constraint C1) that the design cites Burning Wheel to
   avoid, reproduced with more rules.** And CR5's cost half is *wired* while the Doubt Marker (its
   entire upside) is *not*, so in the only path where orientation matters at all, Obscuring is
   currently pure downside. The dominance is not merely present — it is shipped inverted.
4. **Genre content is mechanically empty on 7 of 8 proceedings.** QUALITY terrain carries no primary
   genre (`social_contest_v30.md:54`), so Memory vs Projection decides only whether the two orators
   match — one bit. Combined with (3), the four Styles reduce to one bit plus a dominated bit.
5. **CR4's reachability fix is itself unreachable, and it fixed the wrong half.** ED-1062 moved
   Church Tribunal to a FACT start so Memory-primary could fire. But CONSEQUENCE/FEASIBILITY — the
   grounds that make *Projection* primary — are the start ground of no proceeding, and the doc
   specifies **no reframe action at all** (the kernel's `Move("shift")` is undocumented in canon).
   So Projection's +1D is unreachable in all 8 proceedings, permanently, by the doc's own procedure.
   ED-1062 fixed Memory's reachability and left Projection's identically broken. (ED-SC-0018.)
6. **Adjudicator-type differentiation fires nowhere.** §3's design point — Cognition before judges,
   Charisma before crowds, Attunement in private (`social_contest_v30_infill.md:26`) — is the
   subsystem's cleanest character-differentiation claim. `ADJUDICATOR_PRIMARY` is display metadata
   (`wrapper.py:159`); kernel pools are faculty-based. (Tracked: ED-SC-0004, needs_jordan.)
7. **The asymmetric gate-off never fires.** `opponent_is_adjudicator` exists (`armature.py:374-395`)
   and no caller ever sets it — so the only armature-carrying path double-counts against the accused
   in exactly the two proceedings the doc says must not (`social_contest_v30.md:179`). The Gate-C
   critic already found this (`audit/2026-07-02-contest-gate-c-packet/verdict_log.json:317`); it is
   five weeks unfixed.

---

## §3 — Stacking: the contest is decided at setup (P1, KNOWN-TRACKED as KU-1, SHARPENED)

ED-SC-0012 adopted a combined cap on Recall + Corroborate + Prep + Findings and left the ceiling
value to Jordan (ED-SC-0005). This audit upholds the finding and sharpens it twice.

**The arithmetic.** Formal Contest, both orators Attr 4 / History +4 → base 12D. Legal exchange-1
stack for the prepared side: Recall +2 (`:169`) + Corroborate +1 (`:162`) + Prep +1 (`:541`) +
Findings +2 (`:546`) = **18D vs 12D**. At TN7 (μ 0.40/die, σ 0.80/die):

| Stack | μ diff | σ diff | P(win exchange 1) | P(one-exchange Total Victory) |
|---|---|---|---|---|
| 18D vs 12D | 2.4 | 4.38 | **0.71** | 0.24 |
| + 4 Momentum | 6.4 | 4.38 | **0.93** | **0.62** |

A three-exchange proceeding whose first exchange ends decisive-to-total 70–90% of the time for the
prepared side is not a contest; exchanges 2–3 are epilogue. In Church Tribunal — accused gets no
corroboration, track starts biased at 6, Inquisitor sets length to 1 (`:396`) — the stacked
Inquisitor's one-exchange conviction is near-deterministic.

**Sharpening 1: Momentum is a fifth uncapped channel that KU-1's list omits.** `:172` permits
spending any amount pre-roll; stock cap 4. It stacks on top of whatever combined ceiling lands.

**Sharpening 2 — and this closes ED-SC-0005 without a new number.** The cap Jordan is being asked to
invent **already exists in ratified canon**. CR6 (`:508`, `:514`) rules that setup advantages
"accumulate as δσ, tanh soft-capped", and the kernel enforces it: `M_MAX = 1.5σ` with
`M·tanh(net/M)` (`sigma_leverage.py:92,130-136`), cited to `modifier_system_spec.md §3.1`. The
kernel already routes the armature, evidence, and corroboration through saturating channels
(`EVIDENCE_CAP=3.0`, `Dossier.CORROB` diminishing returns). **The doc's four bonuses are flat pool
dice — i.e. the canonical head violates its own ratified CR6 on precisely the channels KU-1 flags.**
Routing them through δσ dissolves the open question: the number is 1.5σ, already ratified, already
single-sourced, already tested.

**Recommendation:** ED-SC-0005 should not be answered with a die count. It should be closed by
declaring the four bonuses δσ-leverage channels under the existing CR6 cap. (ED-SC-0017.)

---

## §4 — The delta against the uploads

### 4.1 What the uploads get right about us that we did not know

Upload 3's separation rule — *"a mechanism is code that takes inputs and branches; a configuration is
a row in a table"* — is not a proposal for Valoria. **It is a description of what our own code
already did.** `modes.PROCEEDINGS` collapsed all eight proceedings to rows
(`dictionaries.py:607-624` cross-checks them). Upload 3 §8's claim that "S1 Court and S3 Inquisition
differ in exactly two fields" is empirically confirmed here: our Excommunication Tribunal differs
from Church Tribunal in **track start, budget, and a corroboration flag** — and occupies ~20 lines of
bespoke prose section (`§7.1`) instead of a row.

**Roughly 300+ of the canonical head's 724 lines are special-casing that the composition rules
forbid** and that our own kernel already refuted: §6.1.1's overlay residue, §7.1 (a config row as
prose), §7.3's 49-line bespoke Heresy lifecycle (which is Loop A + a Clock + a Record, and to which
ED-SC-0012's own interruption-rule generalization was never applied), §9.2/§9.6/§9.7, ED-617's
proceeding-conditional Recall scope, and ED-1060's mechanism-split terminal rule. **The doc, not the
code, is where forum-as-minigame still lives.**

### 4.2 The single most important finding in the audit (P1, NEW)

Upload 2's throughline T1 says every political system terminates by emitting a Record, and that the
chain *closes* only when a Record from one playthrough **guards a transition** in another.

Traced exhaustively, every wired contest output is a stat delta. The complete list of things that
**guard**: one arc-scoped boolean, `parl_transfer_used_this_arc` (`parliamentary_bridge.py:143`),
which is a frequency limiter. That is the whole spine.

Everything else dead-ends. The KeyLog is written and read by tests only (`echo_transport.py:416-438`;
every non-test reader is under `engine/tests/`). The Chronicle that would narrate cause is discarded
per bout (`narrative.py:112-154`). Succession split ratios are computed and their consequences
explicitly unmodelled (`faction.py:93-95`). Obligations — the doc's headline "lasting consequence in
the game world, not just a stat change" (`:310`) — have **no code consumer anywhere**, and
`tribunal.py:73-80` *deleted* the one canonical record-guard in the corpus, the Excommunication
prerequisite "2 prior Tribunal convictions OR documented Obligation violation", as *"a personal-scale
concept not yet ported"*. Committee referral — the most common band — produces literally nothing.

**A claim that "Valoria lacks a record mechanic" would be false, and the truth is worse.** The
mechanic exists, single-owner, one subsystem over:

```
systems/settlements/sim/ledger.py:7-14
  Precedent  — a ruling/policy that biases future events (±Ob, opens/closes cards)
  Grudge     — an actor/faction wronged; raises their hostile-action weight
  Debt       — an obligation (a sponsorship expectation, a called-in favour)
  Reputation — the settlement's read on the governor
  Leverage   — a hook the player holds
```

Deduped, TTL-aware, swept on season boundaries, and *"live on the Settlement … NOT on the governor,
so they survive succession — the player→world persistence guarantee"* (`ledger.py:15-17`), consumed
via `ledger_add/has/get` (`registry.py:101-107`). This is P16 Recorded Defeat, P3 Commitment, M10
Record, and upload 3's `Record{status, citableAs}` — already built, already ratified, already
consumed by governance verbs.

**The social contest writes bespoke stat deltas instead of composing on it.** That is a composition
failure of exactly the class CLAUDE.md §0 names ("find the single-owner primitive first and compose
on top of it — never re-implement a rule that already lives once"). It is also the cheapest fix in
this report: a Decisive win emits a `Precedent`; an Obligation *is* a `Debt` (and Compact was already
ruled a Debt subtype, ED-IN-0046 D3); a violation emits a `Grudge`. No new primitive. (ED-SC-0019.)

### 4.3 CUT — ranked, with the emergence consequence of each

Removal is welcome and most of these cost nothing.

| # | Cut | Lines | What breaks / emergence lost |
|---|---|---|---|
| 1 | **§4 Step 4 strain algebra + Charisma modifier + Focus defence + Rattled** (`:189-191`, `:244-247`, `:500-501`) | ~50 | Nothing in code — four stages of parallel arithmetic that no engine evaluates. Two derived stats in §8 exist solely to parameterize it. Keep a one-line bridge note for the Knot-as-Face-buffer (`infill:33` → `knots_v30 §4.2`) rather than silently dropping it. Its actual role (cost of losing) is already covered by the kernel's fault/clinch catalogue + the CR5 Face strip. |
| 2 | **`social_contest_system_v2.md` + its `_index`** | 513 | Banner-marked ⛔ SUPERSEDED, still sitting in the live subsystem folder, citing `designs/scene/…` paths retired 2026-07-19. Move to `deprecated/`. Emergence lost: none. |
| 3 | **Doubt Marker + Terminal Doubt + the CROSS-Obscuring clause** (`:203`, `:212-220`) | ~15 | Moots ED-1060's pending ratification. Replace with one rule on `adv` (the tally branch at `dictionaries.py:190-195`, generalized — the banded branch is redundant since both families share `adv`), **or** delete the orientation bit entirely if the §5 anti-collapse fork goes to warrant×attack. |
| 4 | **Concede a Point** (`:230`), and Regroup with it if cut 1 lands | ~4 | Strictly dominated (§2.2). Let the kernel's `support`/regroup economy be canon. |
| 5 | **Appraise channel (a), the audience-boost read table** (`:150-157`) | ~10 | ED-SC-0012 already ruled fold-to-setup-screen; this is executing a ruling, not making one. The boost is a deterministic function of public state — a solved lookup, not a concealed value. |
| 6 | **The 9 non-canonical venue presets** (`modes.py:121-325`) | ~200 | Zero campaign callers; `[SEED]` constants with "Jordan assigns names" placeholders inside a kernel under active rebuild. Park in a reference doc. Emergence lost: none today; a future venue library, which a doc preserves. |
| 7 | **§6.1.1 overlay rows that restate the general rule** (`:342-343`) | ~6 | ED-SC-0012's DISTILL already hoisted the shared machinery to §6.1; the retained rows still re-narrate transfer/suspension. Trim to the Wager-specific deltas + structural impossibility. |
| 8 | **§9.7's bespoke Niflhel Ob formula** (`:583`) | 2 | **Scripting drift by CLAUDE.md §10's own standard** — an entity special-case where a config field exists: `Faction.parliamentary=False` (`parliamentary_vote.py:25-27`). Re-key the personal-scale bar on the same flag. Same treatment for PP-349's Church shield (`:646`). |
| 9 | **Contest Fatigue** (`:302`) | 2 | Session-scoped, single-instance, clears-if-unused — a table convenience with no videogame session concept, dead since the legacy stub left dispatch. It is subtractive and evaporating: the exact opposite of the durable-defeat asset the system needs. |
| 10 | **§4's success-count vocabulary** (`:184-208`) | — | Rewrite in δσ net/degree terms per CR2 (`:508`) or mark §4 SUPERSEDED-BY-KERNEL. The doc teaches an arithmetic the ratified substrate retired. |
| 11 | **`infill:19-23`'s GM-format / GM-genre sentences** | 3 | They contradict CR4 (`:48`, terrain-derived) and the wrapper's own GM-removal. |
| 12 | **§12's stale apparatus** (`:663-724`) + 9 retired-path citations + `wrapper.py:165-167`'s stale "no proceeding maps to panel" comment (false since ED-1059) | ~30 | Propagation table cites `compilation/v0.14/*_deprecated.md` and `designs/mass_combat/`; SIM-DEBT-04 is claimed closed by `armature.py:126`; ED-136's rename has been pending since April. |
| 13 | **Merge Casual Dispute into Personal Appeal** (`modes.py:510-518`) | — | Both are 1-exchange / no-adjudicator / TallyAtClose, differing in a role label. Roster 8 → 7. Emergence lost: negligible. |

Net: roughly **800 lines out of the live surface**, of which ~50 are the only ones a player would
ever have noticed.

### 4.4 ADD — ranked, with the no-GM / single-PC argument

1. **Record, by composition on `LedgerTag`** (§4.2). Makes Let It Ride enforceable, makes Recall's
   "named precedent" verifiable *by the engine rather than a GM*, gives Chain Contests something to
   carry besides a scalar, gives the loser a durable asset (P16 *senatus auctoritas* — upload 1
   §4.3 calls it "nearly free to implement", and here it is literally free: the object exists).
   Restore the `tribunal.py` prerequisite it enables. **Highest value-to-cost ratio in the report.**
2. **M2 Scope — binding authority** (`upload 3 §4`). Today `:310-312` lets a personal contest win
   bind an entire faction with **no check that the orator could bind anyone** and no repudiation
   path — the only escape is breach. `faction_politics_v30.md:74` even *consumes* Obligations in its
   demotion table, a consumer for an object that exists nowhere. Upload 3's argument is right and it
   is specifically right for us: single-player removes opponent cunning as the tension source, and
   no-GM removes the arbiter of overreach, so *"can you deliver what you promised"* is the tension
   that remains. Wire as `{scope, limits, PROVISIONAL(risk)}` at Obligation creation.
3. **Faction opposition fields** `{aims, redLines, concessionCurve, patience}` (upload 3 §9), plus a
   **concede/offer move** in the contest vocabulary. Today the kernel's move set is
   advance/hard/shift/support/pass/evidence/rebut — **the AI opponent cannot concede, because
   concession is not a move.** `Faction.fixed_lean` is a hardcoded red line, but since no
   side-payment verb exists anywhere, "unbuyable" is unfalsifiable: nothing is buyable. Without at
   least aims + patience, obstruction can never end *for a reason*, and a crisis can never be a
   negotiating window.
4. **Forum choice + wire `invoke_stay`.** Upload 1 §6.2 calls forum-shopping "the primary navigation
   verb of the whole game", and our forums genuinely differ (ProofBar vs PersuasionTrack vs
   TallyAtClose vs weighted VoteAtClose; asymmetric resistance; burden-analogue role structures) —
   so shopping would pay. But the one wired trigger hardcodes its proceeding
   (`scene_dispatch.py:117`), and `parliamentary_stay.py` — a *translatio* mechanic, Parliament
   suspending an ecclesiastical proceeding, historically exactly P10 — has **zero campaign callers**.
   `build_contest` already accepts `venue=`. This is the cheapest add relative to the size of the
   verb it unlocks.
5. **Armature passthrough + derived gate-off.** `build_contest(..., armature=)`, and derive
   `opponent_is_adjudicator` from `PROCEEDINGS[...]["roles"] ∈ {crown_objects, inquisitor_proposes}`
   — the data already exists (`modes.py:492-498`). Without this, Stage 3 does not exist in the
   product.
6. **Stasis-shift as a canonical player action** — adopt the kernel's `Move("shift")` into §4.
   Without it CR4's Projection half is unreachable forever (§2.2 item 5).
7. **P41 Scaled Compromise** — directly replaces "GM narrates partial outcome" (`:279`) with a
   formula. Nothing anywhere in the kernel charges a winner for what winning cost.

### 4.5 Cluster map (upload 2 §11)

| Cluster | Valoria |
|---|---|
| **Adjudication** (S1/S2/S3) | All 8 proceedings. This is the only cluster we have, and we have it eight times. Notably S2-Tribunal — upload 2's build-first hinge — *is* our most-built family (church_tribunal + `tribunal.py` + §7.1/§7.3 + the Stay). **The sequencing instinct was independently correct.** Missing: the cluster's connective tissue — P16 records, P10 forum moves, P41 scaled compromise. |
| **Exchange** (S4/S8) | **Absent.** `NegotiationMode` is a stub; ZOPA "not designed" (`:702`); treaty formation stubbed; no reservation values, no side payments, no instruments. This matters *inside this subsystem's scope* because upload 2 Finding 9 shows S4 is a **subroutine with three inbound callers**. Consequently our Church Tribunal **cannot end in a negotiated abjuration** — historically the ordinary outcome — its only exits are track bands; and the Wager Obligation is a bare instrument with no machine to produce it. **The missing S4 is the missing terminal of the adjudication cluster we do have.** |
| **Administration** (S6/S7) | Lives in the settlements lane — and is where the repo's only real Record primitive sits. The clusters do not touch: no contest output reaches a settlement ledger, no bond guards a compliance roll (upload 2's T5 bond chain, absent). |
| **S5 Parliament** | A division-only stub: one pooled roll. No agenda control, no speaking order, no veto, no drafting right, no enactment clock, no session slots. Upload 1 §5.2 argues "the vote is a formality"; **ours is *only* the formality.** |
| **S9 Selection** | Partially present, and here we are *ahead* of the uploads: the Succession Contest with graduated split ratios is a real selection mechanism upload 2 lists as its largest gap. But benches are never constituted (`_default_panel` hardcoded), investiture confers nothing, and the split's consequences are unmodelled. |

---

## §5 — Two design forks that need Jordan

These are hard design calls. Per CLAUDE.md §2 they are **held back explicitly** rather than bundled
into routine work, and this audit does not execute either.

### FORK A — adopt a burden-parameterized gate? (ED-SC-0020)

Upload 3 §6.4 collapses court, inquisition, political tribunal and negotiation to one `gate()`
function with `burden ∈ {ACCUSER, RESPONDENT, LOWER_STANDING, NONE}`, and shows that
**negotiation is not a separate system** — it is the gate with `burden = NONE`.

**We already have a burden family in disguise:** `ProofBar` (= ACCUSER — the challenger must clear
the bar or lose at close), `GraceThreshold` (burden on petitioner), `TallyAtClose`/`PersuasionTrack`
(= NONE). What we lack is the **stall semantics** — "whoever holds the burden loses the stasis if the
exchange stalls" — which the doc currently fakes with biased track starts (Church 6, Excommunication
7). A handicap changes expected value; it cannot express *silence convicts*.

Adopting it would replace four `WinCondition` classes, two biased starts, and the `use_tracker`
tri-state opt-in machinery (`modes.py:521-534`) with **one Venue field** — and would make
"Private Negotiation = burden NONE" literally true, since it already resolves as `TallyAtClose`.

**Keep the Persuasion Track.** Its compromise band is the one thing burden does not give, and
ED-SC-0002 already composes band-as-magnitude with genre-as-channel. Burden and Track are
complements, not substitutes.

*Recommendation: adopt.* It is the cheapest single unification available. Cost: a moderate refactor
of `resolver.resolve`'s close logic.

### FORK B — what is the anti-collapse device? (ED-SC-0021)

**The adjudicator armature is not an anti-collapse device.** All four Styles produce *identical state
changes* — an additive `_advance` gain — differing only in the magnitude of one upside-only scalar
(≤0.5σ, `armature.py:336`) against a hidden judge vector. That is precisely Constraint C1's failure
signature: *manoeuvres differing only in damage output*. Once Appraise reveals the dominant axis
(Success band, `appraise.py:168-170`), the Style choice is a solved lookup; the "bet under
uncertainty" survives only in the residual, and an AI opponent grinds a residual to its mean.

**The warrant × attack table** (upload 1 P7; upload 3 §6.2) differs *structurally*: Undermine deletes
a premise, Rebut stacks a counter-claim for weighing, Undercut severs the inference. The correct verb
varies with the **opponent's observable claim structure, per claim** — the only anti-collapse shape
that works with no GM and an AI opponent.

And the kernel is already ~80% there: `EvidenceItem` carries ground + appeal + hidden weight;
`rebut` exists behind a venue flag. Adding a `warrant` field and splitting `rebut` into three kinds
is an *extension of existing types*, not a new system.

**Carried caveat (upload 1's own A1, and it is the honest one):** the table anti-collapses only if the
authored claim corpus is warrant-diverse. It is *a content dependency wearing a mechanic's clothes*.
If this fork is taken, adopt the 40%-per-attack-type authoring invariant as a script check on day
one — before writing claims, not after.

**Falsifier, named per §0.1 point 3:** AI-vs-AI best-response sweeps across judge and venue
distributions. If Style-pick entropy under the armature alone stays high (no Style above 40% pick
rate), this recommendation is wrong. If attack-pick under the warrant table collapses past 40% on the
shipped corpus, the table fails its own promise too. **Neither has been run. This verdict is argued,
not measured** — medium confidence, and it should not be ratified without the sweep.

*Recommendation: warrant × attack, decisively — conditional on the sweep.* The armature is worth
keeping as a *seasoning* on top (it makes judges feel different) but it cannot be the load-bearing
anti-collapse mechanism.

---

## §6 — Live bugs (P1/P2, NEW — not design questions)

| # | Bug | Evidence | Severity |
|---|---|---|---|
| F1 | **Stage 3 is unreachable in production.** `build_contest` has no armature parameter; `_resolve_agon` never builds one. CR4, armature δσ, and CR5 fire only in tests and the demo harness. | `wrapper.py:101-102,197` | P1 |
| F2 | **`Face_current` crashes through the public API.** `_as_contestant` never sets `charisma`, which defaults `None`; `face_max()` computes `None × 3`. The Gate-A scale-binding is unreachable and would `TypeError` if reached. | `wrapper.py:82-98`, `resolver.py:183,193,228-234` | P2 |
| F3 | **The doc misreports its own code, in the conservative direction.** `social_contest_v30.md:248,257,519` and `primitives.py:82-87` all state `Standing.strip()` is never called and Face is monotonic-up. **It is called** — `strip_points` fires on the CR5 foul. An honesty note that has gone stale is worse than none: it stops the next reader from looking. | `resolver.py:418` | P2 |
| F4 | **`counterpuncher` self-destructs in every canonical proceeding.** It rebuts in the back half when behind; all 8 canonical venues leave `allow_rebuttal=False`, so each rebut scores an evasion fault and **2 evasions is a clinch loss**. Its docstring says it "self-limits" — it self-eliminates, and only when losing, i.e. exactly when it activates. | `policy.py:45-54`, `resolver.py:349-350`, `primitives.py:267` | P2 |
| F5 | **A struck formula is live on the package API.** `CONCENTRATION_MULTIPLIER = 3`, commented `"Concentration restores to max (Focus × 3)"` — the form STRUCK by ED-901 in favour of (3×Focus)+(2×Spirit) — is re-exported from `contest/__init__.py`. Relatedly, `primitives.py:161-162` claims the canonical magnitude "is carried by params/contest.md + wrapper.py"; **`wrapper.py` contains no such formula.** | `contest_legacy_stub.py:61-63`, `__init__.py:42,104` | P2 |
| F6 | **The "one-season" Mandate penalty is permanent.** `parliamentary_vote.py:213` applies −1 × MULTS["L"] = **−20 granular Legitimacy** with the note *"[one-season penalty; temporary-modifier restoration deferred to season_manager]"*. `engine/autoload/season_manager.py` is 48 lines containing `advance_season` and `check_arc_boundary` — **no temporary-modifier facility exists**, and `Faction.adjust` is a direct write. Every BG Total Victory strips 20 granular L forever against a spec that says one season. *(Flagged as observed-not-ruled by the emergence lens; closed by orchestrator verification.)* | `parliamentary_vote.py:207-218`, `season_manager.py`, `game_state.py:42,126` | **P1** |
| F7 | **Silent side-A bias in the live tie path.** The legacy stub resolves a tied exchange with `movement = +1 # toward A by convention` — a permanent thumb on the scale in every dispatch that still routes through it. | `contest_legacy_stub.py:174-178` | P2 |
| F8 | **The asymmetric armature gate-off never fires** (§2.2 item 7). Known since Gate C, unfixed. | `armature.py:374-395` (no production setter) | P2 |

---

## §7 — What survived attack (null results — do NOT change these)

Reported as survivals, not as compensating praise. Each was attacked and held.

- **The kernel's evidence model.** `Dossier`/`EvidenceItem` with hidden weights, per-source
  exhaustion, diminishing corroboration, and a hard cap is a genuine M3 Concealed Value instance and
  is the correct single owner for what the doc scatters across Recall/Corroborate/Prep/Findings.
- **The fault/clinch defeat catalogue.** Venue-configured *nigrahasthāna* — which faults are fatal is
  a property of the institution. This is exactly the config-not-mechanism discipline the uploads
  argue for, arrived at independently.
- **Panel / weighted-by-standing `VoteAtClose`** (ED-1057/1059). Fully wired, proceeding-reachable
  via Guild Arbitration, degenerate-bench draw handled, bench-weight reuses existing `discipline`
  with no invented state. The one Gate-B closure that is genuinely live.
- **`Pressure`.** Institutional and public tilt, wired into every `_advance`, feeding leak. It is the
  right home for the faction/audience boost the doc implements as a flat die — and it is a live
  mechanic with *no canonical prose owner*, the mirror image of the doc's inert prose mechanics.
- **CR6's tanh soft-cap and the single σ-kernel.** `M_MAX=1.5σ`, single-sourced with combat, cited,
  parity-tested. This is the substrate the rest of the subsystem should be conformed *to*.
- **The Succession Contest** as a selection mechanism (ahead of the uploads).
- **ED-SC-0002's composed keying** (band gates magnitude, genre selects channel) — doc and code agree.
- **Church Tribunal FACT start + track 6, the §10 BG vote constants, the 8-proceeding registry
  cross-check** — verified, doc and code agree.
- **No fabricated constants found.** Every kernel constant checked carries a `[SEED]` tag or cited
  provenance. The anti-fabrication read-through pattern held on cross-check. *This is a real
  positive result and it is worth stating.*

---

## §8 — Recommended sequencing

Ordered by shared surface, not by interest — and note this order is the same one upload 3 §10 derives
independently (Record + Standing first, concealed value second, the parameterized loop third).

1. **Bug batch F1–F8** (ED-SC-0022). Mechanical, no design authority needed, and F1 is the difference
   between Stage 3 existing and not existing in the product.
2. **Record by composition on `LedgerTag`** (ED-SC-0019). No new primitive. Unblocks Let It Ride,
   the loser's durable asset, chain contests, the restored `tribunal.py` prerequisite, and — with
   the Projection token — the first genuine record-guards-transition instance in the campaign.
3. **Close ED-SC-0005 as "already ratified: CR6, 1.5σ tanh"** rather than picking a die count
   (ED-SC-0017), and conform the four bonuses to δσ.
4. **The cut list** (§4.3). ~800 lines. Do it after 2–3 so the deletions land against a doc that has
   somewhere to point.
5. **Fork A (burden)** if ratified — it subsumes several of the special cases the cut list only trims.
6. **Fork B (warrant × attack)** only after the AI-vs-AI sweep named in §5 actually runs.
7. **M2 Scope** (ED-SC-0019 sibling), then forum choice + `invoke_stay`.

**Explicitly deferred, not forgotten:** the Exchange cluster (S4 negotiation as a callable
subroutine) is the missing terminal of the adjudication cluster and will keep generating symptoms —
abjuration that cannot be negotiated, charters that cannot be bargained, Wagers with no producing
machine — until it exists. It is the largest single piece of *new* design this subsystem needs, and
it is out of scope for a cut-and-compose pass.

---

## §9 — Audit trail

`[READ: social_contest_v30.md (725 ln), _infill, _index, social_contest_system_v2 (banner only); the
full sim/contest/ package; contest_legacy_stub.py; parliamentary_vote.py; parliamentary_stay.py;
engine/cross_scale/{scene_dispatch,parliamentary_bridge,domain_echo,echo_transport}.py;
engine/autoload/{sigma_leverage,game_state,season_manager}.py; systems/settlements/sim/{ledger,registry}.py;
systems/factions/sim/{tribunal,parliamentary_transfer,faction_action}.py; auto_manual_resolution_duality_v1.md;
HANDOFF_SC.md; editorial_ledger_sc.jsonl; audit/2026-07-04-ners-qualitative-audit charter; all four uploads in full]`

`[METHOD: three read-only Fable 5 lenses (valoria-critic, tools Read/Grep/Glob — independence is
structural, not declared), relayed agonist→antagonist per CLAUDE.md §10. Model tiering: fable for the
read-only audit nodes per §10's ruling; Opus for synthesis. Every gating claim re-verified by the
orchestrator against the working tree — the verification log is §1.]`

`[NULL: searched and did not find — any code consumer of Rattled, strain, Momentum spend, Corroborate,
rolled first-to-speak, CLASH/REINFORCE/CROSS margin math, Obligations, chain contests, or the Doubt
Marker; any resolution consumer of FACTION_BOOSTS outside tests; any producer of world.casus_belli;
any non-test reader of the KeyLog; any campaign caller of invoke_stay or propose_treaty; any
side-payment/offer/concession/reservation-value construct; any persistence of a contest-local tracker
across bouts; any mention of contests in faction_behavior_v30.md. No findings were manufactured to
fill a lane — the survivals in §7 are reported as survivals.]`

`[SELF-AUTHORED — bias risk] The three lenses and this synthesis were produced in one session. The
lenses had structural independence from each other (disjoint mandates, no shared context, read-only
tools) but not from the orchestrator that briefed them, and the briefs named specific hypotheses drawn
from the uploads — so a finding may be present because the brief pointed at it. Mitigation applied:
every banked claim was re-verified against the tree by the orchestrator, and the verification log (§1)
records what was checked and how. Residual risk concentrates in §5's two design verdicts, which are
argued rather than measured; §5 names the falsifier for each and neither has been run.`

`[CONFIDENCE: high — the prose↔code divergence table, the reachability findings, the bug batch, the
record-spine trace, and the stacking arithmetic (closed-form, recomputed independently from the
canonical per-die constants). medium — the dominance expected values (analytic approximations; a
Monte Carlo over the doc algebra is the falsifier and was not run) and the Fork B verdict. low — any
estimate of how much work the recommendations represent.]`

`[PASS-3: eight graphs and 45 primitives from the uploads mapped against the live surface; three
lenses attacked it along disjoint axes; findings verified rather than relayed; two design forks held
back for Jordan per CLAUDE.md §2 rather than bundled. The largest finding is not a gap — it is a
composition failure: the Record primitive this subsystem needs is already built, single-owner, one
subsystem over.]`
