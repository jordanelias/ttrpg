# Strategic Judgments — the path to the North Star

## Status: PROPOSED (audit judgments — Jordan review; nothing here self-ratifies)
## Date: 2026-07-04 · Companion to `ners_qualitative_audit_v1.md`

The North Star: **a Godot emergent grand-strategy · tactical-management · political-simulation ·
narrative RPG where every subsystem points toward an emergent-narrative player experience with
rich, meaningful choices through myriad options and decisions.** These are judgments on how to
get there from the audited state — ranked, opinionated, and each traceable to audit evidence.

---

## I · Sequencing to the Godot end-state

**J-1 · Name the milestone: one playable season.** Nothing in workplan v5, roadmap_state, or the
decision queue defines a first end-to-end slice (sequence lens). Define it now: *one season played
from the screen — a strategic decision, one domain action, one social contest, one combat, one
thread op, season close, and an articulation render — passing the three dramatic-legibility
questions at each juncture.* Make **distance-to-this-milestone the ordering criterion** for all
lane work. Everything below is justified by it.

**J-2 · The critical path runs through connective tissue, not depth.** The audit's clearest
structural result (audit §6): the least-specified modules are the most load-bearing
(`domain_actions` — the player's primary strategic verb, doc:null, consumes:[]; `engine_clock` —
the temporal spine, doc:null pending ED-1051). Combat, by contrast, is the best-specified
subsystem and received two further deep passes while Gate-0 stayed frozen (sequence lens).
**Judgment: finish R3, then stop deepening combat until Gate-0 (Key v2 migration, three-doc
reconciliation, engine_clock authoring) is executed and domain_actions has a home doc.** The
propagation spec (ED-1093) already supplies engine_clock's candidate home — flipping ED-1051 is
mostly authorship, not invention.

**J-3 · Close the transport seams before building new emitters.** Three cheap, high-leverage
wiring tasks (audit §6, F-4): add the missing consumer entries for `scene.combat_resolved`;
populate `targets[]` for the 8 §12.4 down-seams; add articulation triggers for
battle_concluded/investigation_resolved (+ decide the thread-beat rendering policy, audit §4
item 2). Every one of these makes *already-computed* consequence arrive — the highest
emergence-per-effort ratio available anywhere in the corpus.

**J-4 · Give the collision engine its engine (F-2).** A minimal Convergence Marker detector is a
small mechanic: a registry of (trigger-pair → combined payload) rows checked once per Accounting,
emitting a `meta.convergence_marker` Key that articulation §3.1 triggers on. It converts the
corpus's flagship emergence claim from prose to mechanism, and it is exactly the kind of
cross-scale, player-visible payoff the North Star is named for. Candidate home: `game_director`
(doc:null — this could be the doc that justifies it) or a new small module.

**J-5 · Player decision surfaces are the biggest North-Star debt — schedule them as first-class
increments.** The three thin-choice verdicts (combat, settlement, faction — audit §2) share one
root: resolvers were built before choice surfaces (correct for oracle discipline, but the second
half is now the bottleneck). Concretely: ratify-or-revise the settlement governance redesign
(F-1 — its G1 prerequisite is already built); reserve named R-sequence slots for combat's
player-input surface and ED-911 (both currently unscheduled — R-1); give faction seasons at least
one genuine per-season fork beyond the signature action. The contest lane's walkthrough-first
method (Stage 6 seeding) is the model — apply it per subsystem as each stabilizes.

**J-6 · Threadwork is the mechanical model of the North Star — protect and propagate it.** The
one "rich" choice-density verdict in the corpus (audit §2). Its two debts are naming (MS/RS —
resolve to ONE name before any typed export binds the track) and sinks (ED-911, articulation).
Wiring thread into combat and rendering is not just P-14 compliance; it is putting the game's
best decision economy in front of the player at the game's highest-frequency moments.

**J-7 · Emergence is real but must be made visible to be believed.** Ω(c) verified: the world
ticks without the player. What's missing is rendering (F-2/F-3/F-4) and compounding (§12.4,
cross-tick convergence unproven). Prioritize visibility over new autonomy: the seeded-sim ~87%
single-winner (KNOWN) matters less right now than the fact that a player cannot *watch* the world
change — fix render-paths first, then rebalance what players can finally see.

**J-8 · Jordan-decisions that gate the most North-Star value** (from the frozen queue + audit):
(1) settlement governance redesign ratification (F-1); (2) thread-beat rendering policy (§4
item 2); (3) MS/RS name; (4) combat player-interface staging (R-1) + ED-911 scheduling;
(5) Stage 4 contest games (already NEXT in the SC lane — confirm it stays next); (6) ED-1051
engine_clock flip. Most of the 23 queue items are narrower than these six.

---

## II · Anti-drift governance

The audit's refutation pass (25/30 refuted, dominant pattern "fact true, safeguard one file
away") and the two corpus-level signals (S-1 register blindness, S-2 steering fragmentation)
point to specific drift classes with specific fixes:

**J-9 · Ratification must back-propagate to the registers, mechanically.** Root cause of F-5 and
S-1: striking or ratifying canon updates the head doc but not `supersession_register.yaml` /
`mechanics_index.yaml` / propagation lists. Extend the ED-1094 merge-ratifies convention with a
**register-touch rule**: a PR that flips a `## Status:` line or strikes a mechanic must co-commit
the register rows, enforced by a CI check in the currency-gate family (`tools/`, one rule one
home). GD-1's missed sweep of peninsular_strain happened because the propagation list was a
hand-maintained enumeration — derive sweep targets by grep, not by list.

**J-10 · One name, one home, block-tier for Godot-load-bearing vocabulary.** From the
centralization lens: fold `glossary.md`'s tables into the names_index mirror gate (or generate
them from it); reconcile the 7-vs-9 attribute roster and `resonance_style`-vs-Resonant-Style;
flip attribute/stat/clock names from `enforce: warn` to `block` once reconciled. The naming
architecture is already right — the binding is loose. Every typed-export field (CLAUDE.md §5)
should require a block-tier name.

**J-11 · Institutionalize the skeptic.** This audit's strongest methodological result: unverified
finder-claims are wrong ~5 times out of 6, while verified findings are load-bearing. Adopt
refutation-with-intent-gate as the standing convention for any audit or balance claim entering
the ledger (cheap: one opus-tier refuter per candidate; the 01_workings refutation records are
the template). Symmetrically: safeguards that defeated refutations deserve to be *cited where the
exploit reader looks* (e.g., the deterministic vote rule beside the stale "GM controls" line).

**J-12 · Retire or regenerate the dead steering files.** `roadmap_state.yaml` describes a May
track (S-2) — either regenerate it from workplan v5 + CURRENT.md or retire it to deprecated/ with
a banner; a stale steering file is worse than none (resumed-from-superseded risk, the charter's
own warning). Same rule for the UI/UX v4.1 stale-CANONICAL header (F-3): no doc should read
CANONICAL while its dependencies are superseded — banner it or supersede it.

---

## III · Roadmap management (one steering surface)

**J-13 · Declare the hierarchy: CURRENT.md → lane handoffs → decision queue; everything else is
derived.** The audit found four surfaces disagreeing (S-2). The working pattern is already
visible: CURRENT.md is hand-reconciled and fresh; lane handoffs carry in-flight state; the
decision queue holds open forks. Make workplan v5 explicitly a *derived* document — its per-lane
status lines should point at `handoffs/HANDOFF_<LANE>.md` rather than duplicating status that
rots (the J-38 contradiction is exactly this failure).

**J-14 · Reconcile monthly, and make the reconcile a session type.** The 2026-07-01
month-overview session demonstrably worked (12 commits, ED block, decision queue). Schedule it:
a monthly overview session whose fixed checklist is (a) CURRENT.md reconcile, (b) register
back-propagation sweep (J-9), (c) decision-queue refresh against merged PRs (items 1–3 currently
reflect pre-R2 physics), (d) steering-surface diff (workplan/roadmap/handoffs), (e) milestone
distance check (J-1).

**J-15 · Track the audit's own follow-ups as lane work, not as a new surface.** The [GAP:]
register (audit §8) and unverified candidates (§5) should flow into existing lanes via the ED
options — not spawn a parallel tracking file. One continuity surface per lane is the hard-won
convention (HANDOFF split rationale); this audit conforms to it by writing its residue into
`handoffs/HANDOFF_IN.md` and `ed_options.md` only.
