# 08 · FI · 08 — Knots in the season: a directed edge, strain as a reading, and the order that makes a tie worth building

## Status: PROPOSED (§1 and §2 are edits; §3 is sequencing; §4 is design-first)

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-29) — the knot index's pair order opened (`queries/cache.py:95`, owner first); §1's line stands as written.

Carries `audits/08_FI_audit_addendum_B.md` correction C-1 and resolutions R-34, R-48, R-50. It corrects the
first FI audit's disposition of H-182 (*"waits on `_eff_tie`, plan position `14`, CHAR's"*): the effect was
built at v9 IN-32 and reverted as falsified, for want of a reader.

## What this changes in `engine/season/` at runtime

§1: `epistemic.py::_ch_witness_key` admits a person through a `knot` he owns, not through either end. In
every world the tree builds this moves nothing (no `knot` has a producer; where a builder plants a mutual
bond it is two edges). §2 touches only the unplugged oracle. §3 and §4 change nothing until built.

## The problem, with evidence

- **The season's knot is read against Layer 1.** `architecture/meta/04_CODE_ARCHITECTURE.md` §A.3 row 9 makes
  `tie` and `knot` two directed edges, one owned by each party (as H-182's `cite:` records it, with `:388`:
  *"`tie`/`knot` are directed"*). `_ch_witness_key` reads the pair either way round (`epistemic.py:559-560`:
  `(pid, anchor) in knots or (anchor, pid) in knots`), so a bond one person declared lets the *other* see
  his partner's acts.
- **The effect was built once and nothing read it.** H-182's `cite:`: IN-32 (attempt `53ed995d`, revert
  `7c6df560`) opened the actor's `tie` to the act's subject and added a `tied` term to
  `decision/options.py::teller_weight` at `tie_gain` 0.5. The realm's `tie / knot` row went from
  83 / 0 / 0 / 0 to 80 / 80 / 43 / 11 (formed / offered / attempted / executed); `teller_weight` was never
  built at seeds 0 and 5 over two seasons, because no told claim carried a chain; `tied()` was called 0
  times and the two gains hashed identically. Eleven to thirteen live ties, read by nothing (`ID-13`).
- **The archived gauge cannot be a field.** `knots_v30.md` and `fieldwork_v30.md` §5.6b specify strain as a
  stored −5..+5 number per bond. Layer 1's same row makes strain a Query stored nowhere; `Tenure.degree` is
  `Optional[str]`; ruling R7 admits no magnitude carrier at any scale.
- **The oracle still hides a failed import.** `systems/fieldwork/sim/knots.py:347-364` and `:373-378` wrap
  both lateral calls in `try/except (ImportError, AttributeError): pass`. The 2026-08-08 churn audit named
  this as the second silencing layer of its D6; the first layer (a conviction name the callee did not know)
  was fixed on 2026-08-24 and this one was left.
- The season's `thread_read` reads no bond (H-331), and the oracle's `form_knot` admits a self-knot and
  draws unseeded (H-332; `08_FI_04` §5 already carries those two).

## Edits and decisions

**1. A person witnesses through a knot he owns (R-48).** `epistemic.py::_ch_witness_key`'s last line reads
`(pid, anchor) in knots` (reading the index pair as owner first `[GROUNDED, 25 G-29: opened. The pair is
`(t.subject, t.object)`, `queries/cache.py:95`: owner first, so `(pid, anchor)` is the line]`).
The code is the defect and Layer 1 is not edited to match it (`CLAUDE.md` §0.05).
A mutual bond is two edges and reads exactly as before.

**2. The oracle fails loudly (R-50).** Delete both `try/except` wrappers in `knots.py`. An oracle whose
callee cannot be imported should raise; `engine/tests/test_knots_ed912.py` then observes the lateral calls
it asserts on.

**3. Order: the reader first, then the producer (C-1).** `_eff_tie` is not re-designed; IN-32's commit is
the build. It re-lands when both hold: (a) chained told claims exist in seeded play, which is
`08_FI_02`'s gate (two-hop chains above 0), so `teller_weight`'s relation term runs; (b) the person-side
decline the register names as the untried lever is in place, so a tie forms only on a referent the actor's
own ledger presents as a person he has seen since he last moved (`08_FI_02` edit 5's `present_persons`
reader serves both). Until then the row stays declined, as it is.

**4. Strain is a reading, and a rupture is an act (R-34; design-first).** The form is decided; the kinds
and the threshold are a design pass.
- `queries/person_q.py::knot_strain(p, partner, since) -> int`: a count, over `p`'s **own** ledger since the
  bond opened, of claims naming the partner whose kind is a member of a new roster, `knot_strain_kinds`.
  Person-side, World-free, stored nowhere. Two partners can read the same bond differently, which is ruling
  R7's *"a ruler can be wrong about their own standing"* applied to a friendship.
- The roster's first member is already emitted: `confidence.broken`, the Event a holder causes by passing a
  confided claim outside its circle (`loop/resolve.py::_confidence_broken`). It is the archived design's one
  immediate rupture trigger, *"public citation of private counsel"*, in the engine's own terms. If
  `08_FI_05_B`'s citing act is given the same fold check, citing a confided claim before a bench breaks the
  confidence there too `[named for SC; one call at the fold]`.
- A rupture is not a MATTER write. When `knot_strain` crosses a fixture threshold, one question is raised
  whose referent is the partner (`world_q.standing_crossed`'s shape), and the person may `release` his own
  edge (`release`'s `domain:` already lists `knot`). His partner's edge stands until *he* reads the bond as
  broken.
- What a knot gives beyond witnessing (the archived five use-sites: remote reading, a shared buffer in a
  contest, counsel, anchoring, cheaper corroboration) is T07's and SC's and is not decided here.

## Gate (execution artifacts)

- §1: on `probes.tiny_world` with one planted one-sided `knot` (A owns it, to B): an act of B's elsewhere is
  witnessed by A and an act of A's elsewhere is not witnessed by B; with both edges planted both witness, as
  today. `build_realm(0..2)` one-season hashes equal the base.
- §2: `engine/tests/test_knots_ed912.py` green with the wrappers gone; with the conviction module's name
  misspelt on purpose the same test errors where today it passes.
- §3: at re-land, `tied()` is called more than 0 times in a seeded realm and the `tie_gain` 0 and 0.5 arms
  hash differently (IN-32's own stopping rule, reversed).
- §4 (after its design pass): two partners holding different claims of one breach read different strain;
  the one over the threshold forms `release` on the bond and the other does not.

## Falsifiers

- §1: if any shipped builder plants a one-sided `knot` and a test relied on the partner witnessing through
  it, that test reddens; that is the defect surfacing, to be fixed at the builder (plant both edges).
- §3: if chained claims exist and `tied()` still reads 0 calls, the relation term is not reached for
  another reason; stop and report, as IN-32 did.

## NERS reading

N: a bond that lets one person learn what another does at a distance is the one private channel the
information model has, and it has no producer; top-down (R-06 and R-07's "relationships"), bottom-up (one
predicate line, one reader), lateral (the telling's `tied` term; the hearing's confidences). R: a bond that
each party reads for himself and that one of them can break generates the estrangement and the betrayal
with no player. S: one ladder for the bond's state (a count over held claims) where the archive and the
oracle keep a stored gauge beside an undegreed Tenure. E, last: one line corrected, two wrappers deleted, a
build re-landed in the right order, against a relation the game currently names and does not have.

## Cost class

§1, §2: edit. §3: small build (re-land), after `08_FI_02`. §4: design-first, then small build. Lanes: FI;
CHAR (`teller_weight`, the decline); T07 (`thread_read`, the use-sites).
