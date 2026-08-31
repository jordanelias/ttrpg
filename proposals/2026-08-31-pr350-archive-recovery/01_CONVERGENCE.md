# CROSS-LANE CONVERGENCE INDEX

Twelve lanes read **disjoint file sets** across two trees. Where lanes whose assigned directories do
not overlap reach the same finding, that is corroboration. Where they reach it because they each read
a different copy of one propagated ruling, **that is not independent discovery and is marked as such**
— `CLAUDE.md` §16's warning that agreement between documents that read each other is correlated
error, not corroboration, applies to lanes too.

Tree separation, for judging independence:
- **archives/audit** — lanes A (factions/mandate), B (world/topography), C (architecture/flow), D (NPC/NERS)
- **designs/ heads** — lanes E (npcs/personal), F (world/territory), G (provincial/architecture)
- **designs/audit** — lanes H (political dynamics), I (NPC audit), J (syntheses), K (arcs)
- **cross-cutting** — lane L (scene/season economy)

---

## C-1 · MANDATE IS DERIVED FROM PER-SETTLEMENT LEGITIMACY AND POPULAR SUPPORT
**Lanes: A, B, C, D, E, F, H, K — eight, across all three trees.**

The single most-corroborated finding in the scrape. Jordan ruling 2026-05-30 (LPS-2e): L and PS are
**base stats of a settlement** (0–7 each), not faction-level. Faction Mandate is a **size-weighted
saturating aggregate**:
```
q_s = 0.5·L_s + 0.5·PS_s                    per-settlement acceptance
W_s = base(Type) + Prosperity_s + FacilityTier_s     settlement weight, 1–11
T   = Σ_s W_s·(q_s/7)
Mandate = clamp(round(7·T/(T+K)), 0, 7),  K = 6
```
plus mean-reverting feedback: settlements ≥1 below Mandate drift L+1, ≥1 above drift PS−1, capped
±1/settlement/season. **Sim-verified bounded and convergent over 30 seasons** (lane B, F).

⚠ **INDEPENDENCE: PARTLY CORRELATED.** A, B, F and H each read a different document restating one
ruling, so their agreement is propagation, not rediscovery. **What IS independent:** lane C
(architecture/flow, archives) derived the *rule* — "never write a derived aggregate directly" — from
module wiring rather than from the ruling, and lane D found the same ruling in a ratification register.
Different methods, same conclusion.

**Sharper than the ruling itself:** the corpus then **violated it 78+ times.** Mandate is directly
written at ≥78 sites across ≥6 canon docs AND read as a live resolver input, and `derived_stats §14`
still states the **inverted** arrow (`Legitimacy = Mandate×20`). Lane C found the violation is in
**ratified canon prose** (`scale_transitions §5.2/5.4/5.6` literally say "+1 Mandate"), not merely in
code.

---

## C-2 · THE PERSONAL→FACTION SEAM HAS A NAME, A THROTTLE, AND A KNOWN DEFECT
**Lanes: A, B, C, D, H, I, K — seven.**

**Domain Echo.** A personal-scale scene meeting a "Sufficient Scope" test emits one bounded write to
faction state: Overwhelming ±2 / Success ±1 / Failure −1, **capped ±2 per stat, one Echo per faction
per scene, and QUEUED to the next Accounting rather than applied live — explicitly "to prevent
real-time manipulation"** (lane C). Four sub-channels (Domain, Debate→Mandate, Accord, Thread).

Lane D found it is **one single-owned primitive reused by three unrelated subsystems** (investigation
findings, thread operations, mass-battle outcomes) — genuine single ownership, not three parallel
implementations.

**The defect all seven circle:** it writes a **scalar delta straight to a faction integer**, which
contradicts C-1's derivation. The proposed fix, never executed: route the ripple to the settlement
locus or a national-event Key ledger — "the ripple still flows up, but through the substrate, one
scale at a time, rather than teleporting to a faction integer."

**Design statement worth keeping verbatim (lane C):** *a player moves institutions a point or two a
season through scenes; institutions move themselves through Domain Actions.*

---

## C-3 · "DERIVE IT, DON'T STORE IT" WAS REACHED INDEPENDENTLY, REPEATEDLY
**Lanes: A, B, D, E, F, H — six, and here the independence is real.**

Distinct applications, different authors, different PPs, no cross-citation:
- **Province Accord** = floor(mean(settlement Order)) — "emerges from settlement governance rather
  than being set directly" (F).
- **NPC-NPC Disposition** derived from the relational edge graph — "storing both edges + Disposition
  risks divergence; deriving keeps the substrate single-sourced" (E, PP-724).
- **`armature_position`** never stored; recomputed from the 13×4 matrix at compute time, so a matrix
  change needs no migration (E, PP-684 — **a different PP nine days apart from the above**).
- **Settlement political sentiment** recomputed from the people currently on station (H).
- **Faction stat inversion** — every stat an aggregate of holdings ⊕ a decaying event ledger (A).

This is the archive independently converging on **PR #350's Law 3**, from five directions.

---

## C-4 · A FACTION IS AN AGGREGATE OF NAMED PEOPLE, NOT AN AGENT
**Lanes: A, H, I — three, across two trees.**

- **A:** PP-686 v2 — faction "personality" is an α-weighted cascade of its officers' Conviction
  vectors down a supervisor graph; `effective(npc) = α·personal + (1−α)·effective(supervisor)`;
  `aggregate = normalize(Σ standing×effective)`.
- **H:** `FactionMetaArmature` = Standing-weighted average of the inner circle (S7:1.0 … S4:0.3,
  leader ×1.5), Mood-dampened, plus one merged `institutional_stability` term anchored to the
  faction's historical dominant Conviction — **which is why a reformist leader's court resists him.**
- **I:** the same cascade, plus `role_acting` — an NPC acting *as office-holder* swaps their personal
  Conviction vector for the cascade-derived one, a **cross-scale singleton** owned by neither schema.

**This is the archive's version of PR #350's Law 1, and it is strictly richer:** the shape says a
faction acts only through persons; the archive says *how much each person's psychology weighs*, and
adds institutional inertia the shape has no counterpart for.

---

## C-5 · THE CORPUS'S CHARACTERISTIC FAILURE: RULED, THEN NEVER PROPAGATED
**Lanes: A, C, D, H, I — five, on five different subjects.**

Not one bug — a recurring class:
| subject | lane | the residue |
|---|---|---|
| Mandate derivation | A, C | ≥78 direct writes; the inverted arrow still in `derived_stats §14` |
| Faction actions | A | canon / BG-params / sim define **three disjoint catalogues**; only "Excommunication" appears in all three |
| Niflhel (struck faction) | D | struck by ED-764, its toolkit still live in `fieldwork_v30 §5.8/§6.3` months later |
| Settlement schema PP-726 | F, H | migrated adjacency but not the YAML's own `settlements:` block — **the same file's S-006 names two different places** |
| Ethical Framework Ob modifiers | I | "simultaneously canonically retired AND mechanically active" |

**Lane H's framing is the durable one:** *a migration only touched the load-bearing half.* Three
separate audits across three months found this independently on three different subsystems.

---

## C-6 · FEEDBACK LOOPS WERE FOUND UNBOUNDED AND CLOSED WITH NAMED DAMPERS
**Lanes: A, C, E, H — four.**

- **FSS-LOOP-1** (deterministic floor): at Stability ≤2 the Accounting check cannot itself reduce
  Stability further; only an active Trigger can.
- **FSS-LOOP-2** (conditional re-muster): while Wealth ≥1, Military re-musters +1/Accounting up to its
  pre-collapse value.
- **Mandate** (saturating + mean-reverting): C-1's `7T/(T+6)`.
- **Defection cascade** (E): hop-attenuated ½ per ring, Fragility capped +3 decaying −1/season, a
  player "Suppress" brake, one hop-ring per Accounting, hard cap tier-3 — **shipped with its own
  termination argument attached**, though flagged as designed, not simulated.
- **Standing recalculation** (H): counting a *lost competition* as a failure created a rich-get-richer
  exclusion loop worth ~8 points of faction Order-share over 3 years; fixed by counting only actual
  failed rolls.

**And lane C supplies the principle that makes all of this necessary:** *acyclic provenance is not
loop-safety.* The Key substrate's `causes[]` graph is acyclic by construction, but every turn of a
behavioural spiral emits a new legitimately-caused Key, so the DAG grows forward and **never trips
cycle detection while the systems spiral.** There is no engine-level bounded-loop assertion anywhere.

---

## C-7 · THE WORLD DECAYS FROM NEGLECT, AND A POWER VACUUM BIRTHS A FACTION
**Lanes: A, B, F — three.**

- **Insurgency from neglect:** 2+ contiguous Uncontrolled territories for 2 consecutive seasons — *no
  faction action required* — spawns an Insurgency that invades like a faction, **including against its
  own former parent**, and is promoted at thresholds into a full faction, then victory-eligible.
- **Dissolution follows RAND's *How Insurgencies End*** (89 cases, Jordan ruling ED-881): military
  defeat, **sponsor withdrawal** (the RAND-strongest predictor), negotiated amnesty, or stalemate —
  replacing a model that "could only escalate, never represent the modal real outcome."
- **Symmetric contraction (F):** losing every province does not delete a faction — it becomes a
  **city-state** with a partial stat sheet (Influence/Wealth/Stability, no Mandate/Military) that can
  re-emerge through the same ladder.
- ⚠ **Two independently-built faction-lifecycle ladders were never reconciled** — the player-driven
  Cell→Hegemon emergence ladder and the world-driven insurgency pipeline overlap in subject, use
  different baselines, and neither cites the other.

---

## C-8 · SCARCITY OF INSTITUTIONAL SEATS MANUFACTURES POLITICS WITH NOBODY ACTING
**Lanes: F, H, K — three.**

A Seat has exactly **3 Wing slots** (Standing-6+ residency). When full and a 4th claimant arrives the
only outcomes are: an existing holder departs (death/exile/succession), the settlement pays to expand
(+1 Wing/settlement/decade cap), or the claimant takes a provisional "Prince-in-Waiting" rank
requiring a recurring social contest to hold.

**Lane K's framing is the one that matters:** *this is functionally a political crisis without any
political act by any faction* — the crisis is generated by a settlement resource limit, not a
decision. Cross-faction Wings at composite-control Seats belong to the district's controller and can
be ceded as treaty concessions.

---

## C-9 · INSTITUTIONAL CAPTURE THROUGH HELPFULNESS
**Lanes: B, F — two, one archive and one design head.**

Church presence is four **independent stacking axes** (building tier / Templar / Inquisitor /
governor), not a ladder. A Chapel gives **+0.5 Order/season to any governor who hosts it, secular or
not** — so accepting the help is itself the vector of losing control, and it generates Piety the host
cannot switch off. **Pastoral Assumption** lets the Church auto-install a governor in any ungoverned
settlement holding a Chapel (Ob 1), removable only by Mass Battle, Mandate Challenge Ob6+, or an overt
Restoration action. Church infrastructure also **raises the Ob of military seizure**, stacking to −4.

Explicit historical grounding cited: Papal States, Calvin's Geneva, 1979 Iran — *"theocracies grew not
through hostility but through helpfulness."* Lane F notes an NPC in the Goldenfurt slice (the curate
Wessel) whose entire arc *is* this mechanic played out — an independent confirmation it reads in play.

---

## C-10 · THE 13-CONVICTION TAXONOMY AND ITS 4-AXIS SUBSTRATE
**Lanes: A, E, H, I — four.**

Thirteen named Convictions (Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent,
Community, Identity, Warden, Virtue, Honor), each Renaissance-grounded, projecting onto four axes
(`hierarchical`, `sacred`, `instrumental`, `traditional`) via a **fixed 13×4 matrix with per-cell
calibration rationale**. Composition is a literal dot-product, recomputed at read.

Around it: a **separate orthogonal Self-Other scalar** [−1,+1] so two actors with identical Convictions
play differently (Cesare Borgia vs a public-spirited magistrate share high Utility; what differs is
*for whom*); **structured concentration** (1–3 primaries at 0.6–0.8 + one of 8 cultural-background
templates at 0.2–0.4) which measurably reduced authoring cost; and **per-Conviction Scarring** (PP-718)
replacing an aggregate counter — so a multi-primary NPC is *more* resilient, which the doc grounds in
Charles V's Habsburg-Catholic combination being load-bearing for his longevity.

⚠ Independence is partial — E and I read different trees but both trace to PP-684.

---

## THE LINE THAT RECURS ACROSS EVERY LANE
Lane A stated it for factions and lane H restated it for governance without seeing A:

> **The mechanics that make the world feel alive are the intermediate ones, and they are the ones
> every implementation generation skipped.** The sim implements terminal states — immediate conquest
> transfer, treaty lapse, collapse — but not the 3-season occupation window (resist / cede /
> recapture), not the 3-phase treaty negotiation (positioning / concession / ratification), and not
> one of the ten canonical parliamentary motion types. *"Exactly the branch points that produce
> emergent narrative."*

---

## C-11 · THE SEASON'S SHAPE AND ITS ACTION BUDGET — the strongest convergence in the scrape
**Lanes: B, D, E, F, H, L — six, and lane L reports FIVE independently-authored documents converging
on the identical figures, plus FOUR independently reconstructing the same season phase order.**

**The budget.** `player_agency_v30.md` §4–§6, `## Status: CANONICAL — approved 2026-04-17`:
**3 / 4 / 5 scene actions per season** (Hard / Normal / Narrative) against a slate of **7–9 / 5–7 / 4–5
opportunities** — the slate always exceeds the budget, deliberately. Verified verbatim:

> *"There are always more opportunities than actions. **Choosing is the gameplay** — not executing, but
> deciding what to attend to and what to let pass. Opportunities not pursued do not wait — they resolve
> through NPC AI and clock advancement without player input, often in ways the player would not have
> chosen."*

Modifiers: `+1` Standing 4–5 · `+2` Standing 6–7 · `+1` in a Knotted NPC's territory · `−1` Stamina 0 ·
`−1` at 2+ Wounds. A scene holds **1–3 mechanical interactions**; an extended scene costs **2** actions.

**The season.** Four documents reconstruct the same phase order without citing each other for it:
Briefing → Duty Assignment → Slate Generation → **Personal Phase (the 3–5 actions)** → Strategic Phase
(Domain Actions) → Accounting → Aftermath (free, 0 cost).

**Three surrounding rules that are as valuable as the number:**
- **Witness Mode** — when mandatory scenes exceed the budget, unattended ones resolve at **0 cost** via
  a Read/Appraise at Ob 1 (not auto-success), with **no Domain Echo and no Momentum/Coherence change.**
- **Exactly one between-scene currency, by explicit decision.** Each subsystem owns a *within*-scene
  resource (Wounds/Stamina · Composure/Concentration · Coherence · Exposure); the scene-action budget is
  the only *between*-scene one. A second was proposed and rejected as double-penalising.
- **The budget is fractal** — inside an investigation scene, a *scene time budget of 3* over a 4–9 node
  graph, described in-doc as *"not a new resource — it is the scene action budget expressed spatially."*

⚠ **AND THE TWO FINDINGS THAT CUT AGAINST ADOPTING IT UNCHANGED:**
1. **It is explicitly NOT universal.** NPC factions take exactly one action off a 7-level priority tree;
   individual named NPCs have **no budget at all** — they generate slate entries that cost *the
   player's* budget. Plus Standing grants `+1`/`+2`. **Rank changes the budget, and the player and the
   NPC do not share an economy.**
2. **Five was stress-tested and saturated.** Test **R-39**: at a Year-4 season, mandatory content alone
   (1 leader crisis + 1 heresy investigation + 3 Concern-driven Outreach scenes) consumes the entire
   5-action budget, leaving **zero** discretionary play — filed as a Robust/Smooth violation,
   *"NPCs always have the initiative."* The proposed fix was a **slate-generation policy change**, not a
   larger budget, and that fix was never promoted while the mechanism it tested was.
