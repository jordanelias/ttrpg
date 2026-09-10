"""`decision/` -- the `choose` member of `04_CODE_ARCHITECTURE.md` §A.2:133.

`make_chooser` and everything it resolves by BARE NAME: `align` (which reads `ALIGNMENT`),
`stance_toward`, `urgency`, and `pack_scenes` (with `_payload_of`).

⚠ **THE BARE-NAME CLUSTER IS WHY THESE FOUR ARE ONE FILE, AND IT IS NOT A STYLE CHOICE.** Three
names in the old `decision.py` are read bare inside a body and rebound from OUTSIDE as module
attributes -- `ALIGNMENT` (by `align`), `pack_scenes` (by `make_chooser`) and `belief_contradicts`
(by `opening_set`, which is why that one lives in `options.py`). A bare name resolves in ITS OWN
module's globals, so a rebind reaches it only if it targets the module the reader lives in. Split
`align` from `make_chooser` and `PS.pack_scenes = spy` in the degree-sweep arms becomes a NO-OP
that reports every branch identical -- a fabricated null, which `CLAUDE.md` §0.1 pt 4 calls the
worse of the two directions. The rebind sites name `decision.choose` and `decision.options`
directly for this reason; see `__init__.py`.

⚠ **`ALIGNMENT` AND `belief_contradicts` ARE NOT RE-EXPORTED FROM `__init__.py`** -- step 8's
`_LADDER` lesson: a rebound value re-exported is a stale snapshot, and a reader who rebinds the
package attribute would silently miss the reader.

AX-2 binds every file under `decision/`: no `World`, as an import, a name, an attribute or a
string. Enforced BY PATH over this directory (`04:1046`).
"""

from __future__ import annotations

from typing import Callable, Optional
from ..data.rosters import CONVICTION_AXES, SCENE_PACKING_RULES
from ..data.verbs import ALIGNMENT, ALIGNMENT_DEFAULT_CELL
from ..gaps import Unspecified
from ..state.carriers import Act, Candidate, Person, Question, Scene, Sensation, View
from .options import opening_set


def align(verb: str, axis: str) -> float:
    """§F2's `alignment(c.verb, axis)`. Sparse: an unlisted pair reads the table's own declared
    `default_cell`, never a literal here."""
    return float(ALIGNMENT.get(axis, {}).get(verb, ALIGNMENT_DEFAULT_CELL))


def stance_toward(p: Person, referent: str) -> float:
    """§F2's second term, from `p`'s OWN stance rows. #353 `:333`: `(referent, valence -5..+5,
    weight 0..5)`. Valence times weight, summed over the rows naming this referent -- weight is
    what `:333` supplies it for, and dropping it would make a 5-weight conviction and a 0-weight
    one count alike."""
    total = 0.0
    for row in p.stance:
        if len(row) >= 3 and row[0] == referent:
            total += float(row[1]) * float(row[2])
    return total


def urgency(subsistence: int, fx: "Fixtures") -> float:
    """§F2's third term. NO IN-CHAIN FORMULA -- `H-73`, `assumption`, swept.

    ⚠ AND IT CANNOT CHANGE ANY DECISION, WHICH IS A DEFECT IN §F2 RATHER THAN IN THIS FUNCTION.
    §F2's score is

        score(c) = SIGMA_axis conviction[axis] * alignment(c.verb, axis)
                 + stance_toward(c.subject)
                 + urgency(sensation.subsistence)

    and the third term HAS NO `c` IN IT. It is added identically to every candidate, so it cannot
    move the ranking, cannot change which candidates survive `ask_budget()`, and cannot change the
    order they are returned in. `choose` returns "the top ask_budget() candidates, ORDERED by
    score", so a term constant across candidates is INERT BY CONSTRUCTION -- it is the dead-carrier
    shape #353 `:739-744` names, arriving in the scoring function instead of in a field.

    Kept and computed anyway, faithfully, because deleting it would hide the finding: the sweep
    (`H-73`) reports that NO verdict moves across three urgency scales, and that null result IS
    the measurement. `test_w5_f2_third_term_is_inert` is the falsifier."""
    return float(subsistence) / float(fx.get("condition_scale"))


def make_chooser(fx: "Fixtures", mint: Callable[[str, str, str], str],
                 verbs: Optional[frozenset] = None) -> Callable[..., list[Act]]:
    """§F2's decision policy as a FACTORY, so `choose(p, view, sensation, ask_budget)` keeps the
    FOUR-parameter signature §26 states while still reaching its params.

    `H-03` is the row: "grade: assumption. THE SHAPE IS RULED (§3 L1, §9, §26); only the weighting
    is open", so §G's discipline applies to the weights and not to this structure.

    Four properties, and each is checked by a test rather than asserted here:
      1. EVERY INPUT IS PERSON-SIDE -- `convictions`, `stance`, the View, the two Sensation
         scalars. No World, no resolver-side Query. L2 by parameter list.
      2. It CONSUMES `convictions` and `stance`, which #353 declares as fields and no formula in
         the chain reads -- a carrier nothing consumes is dead state (§22.1's own complaint).
      3. THE PERSON TRIAGES. `ask_budget()` is asked, not imposed; the engine never truncates.
      4. A lookup on one's own interior is indistinguishable from a deliberation at this
         boundary, and the design does not claim otherwise (§F2 property 4).

    ⚠ `mint` IS HERE BECAUSE §F2 TYPES `choose -> Act[]` AND GIVES THE PERSON NO WAY TO MINT ONE.
    An `Act` needs an id, and §33 derives every id from the world seed and the tick -- "unique per
    DRAW, not per operation" -- so a person-side function cannot produce one. That is a real gap
    between §F1's `-> Candidate[]` and §F2's `-> Act[]` and it is registered (`H-74`), not filled:
    the barrier passes a minter closed over the seed and tick, which are the CLOCK, not anybody's
    interior. Same shape as `fx`, and the AST proof still sees no `World`."""
    def choose(p: Person, v: View, s: Sensation, ask_budget) -> list[Act]:
        q = getattr(v, "question", None)
        if q is None:
            return []
        cands = opening_set(p, v, q, fx)
        if verbs is not None:
            cands = [c for c in cands if c.verb in verbs]
        u = urgency(s.subsistence, fx)
        def score(c: Candidate) -> float:
            return (sum(float(p.convictions.get(ax, 0.0)) * align(c.verb, ax)
                        for ax in CONVICTION_AXES)
                    + stance_toward(p, c.subject or "")
                    + u)
        # Deterministic: score DESC, then verb then subject, so a tie cannot depend on dict order.
        ranked = sorted(cands, key=lambda c: (-score(c), c.verb, c.subject or ""))
        # §26.3: the PERSON triages. The slice is the person's own choice of what to leave
        # undone, taken against a budget they ASKED for -- not an engine truncating a tail.
        # `W17`: the budgeted unit is the SCENE, so the slice is over scenes and each carries up
        # to `interactions_per_scene` of the ranked candidates. The default policy fills scenes
        # greedily in score order -- a person spends a scene on their best option and whatever
        # else it can carry, which is what "1-3 mechanical interactions" describes.
        return pack_scenes(p, ranked, ask_budget(), fx, mint, occasion=q)
    return choose


def _payload_of(c: "Candidate") -> Optional[dict]:
    """WHAT A COMPUTED ACT CARRIES: its subject, and the operands its verb's cell names.

    ⚠ `subject` STAYS EVEN WHEN NO CELL BINDS IT, because it is not only an operand. `act_refs`
    reads it to say what an act NAMES, `claim_subjects` reads it to say what a deposit is ABOUT,
    and `tell` -- whose `writes:` is empty by design -- has nothing else that knows what was told.
    Dropping it for a verb whose requirement happens not to mention `subject` would break the
    causal graph for the one verb the corpus most relies on."""
    d = dict(c.operands or {})
    if c.subject:
        d.setdefault("subject", c.subject)
    return d or None


def pack_scenes(p: Person, ranked: list, n_scenes: int, fx: "Fixtures", mint,
                occasion: Optional["Question"] = None) -> list:
    """`H-78`: WHICH interactions share one scene. `H-76` says how many; this says which.

    ⚠ THIS WAS A COMMENT IN `make_chooser` UNTIL THE `W17` ADVERSARIAL PASS READ IT -- "the
    default policy fills scenes greedily in score order", with no row, no alternative and no
    sweep. That is `H-53`'s defect one level up, and `H-53`'s own row names the shape: the
    instrument answering a WHICH question the specification left open, inside a slice.

    `greedy` is that behaviour declared and kept as the control. `one_per_scene` is the pre-ruling
    accounting. `by_subject` groups the interactions that share a subject, which is what
    `player_agency_v30.md` §6.3's "one scene opportunity pursued" describes -- an opportunity is
    an opportunity to do something ABOUT something."""
    rule = fx.get("scene_packing_rule")
    if rule not in SCENE_PACKING_RULES:
        raise Unspecified(
            f"scene-packing rule {rule!r} is not in the roster", "H-78",
            needs=f"one of {sorted(SCENE_PACKING_RULES)}",
            law="H-78 -- nothing in the chain says WHICH interactions share a scene, so a rule "
                "outside the roster is a fourth answer nobody declared")
    per = fx.get("interactions_per_scene")
    width = 1 if rule == "one_per_scene" else (len(ranked) if per is None else per)

    def scene(n: int, chunk: list) -> "Scene":
        # ⚠ `occasion=` IS NOT DECORATION. `choose` already holds the question — it refuses to
        # produce anything without one — and dropping it here is what left the act with no route
        # back to what raised it (`N3`).
        return Scene(mint(p.id, "scene", str(n)), p.id,
                     # ⚠ THE CANDIDATE'S SUBJECT REACHES THE ACT, AND IT USED NOT TO. This read
                     # `Act(mint(...), p.id, c.verb)` — three arguments — so `opening_set`
                     # computed a subject from the question's referents, `mint` folded it into the
                     # act's ID, and the act itself carried NOTHING. `_req_tell` reads
                     # `payload["subject"]` and got `None`, so `tell` was attempted and refused in
                     # every world in the corpus; `_eff_tell` had no target either.
                     #
                     # ⚠ THAT WAS HALF OF `H-94` AND `W-C` CLOSED THE OTHER HALF. The
                     # Candidate carries `operands` now, derived person-side from the actor's own
                     # Tenures, the question's referent and two fixtures, so
                     # `stores(hearth(giver), kind) >= amount` has a `from`, a `kind` and an
                     # `amount` -- and the act CARRIES them, which is what makes the fold bind
                     # what the person bound. The subject is written first and the operands over
                     # it, so a cell that binds the referent under its own name (`to`, `site`)
                     # cannot disagree with `subject` about which thing that is.
                     [Act(mint(p.id, c.verb, c.subject or ""), p.id, c.verb,
                          payload=_payload_of(c)) for c in chunk],
                     # `H-77`: a scene carrying more than one interaction is the EXTENDED one.
                     # This is what `extended` MEANS, and until W17's adversarial pass nothing
                     # ever set it -- so `Scene.cost` returned 1 unconditionally, H-77's sweep
                     # could not move any verdict, and the row passed R2 while being
                     # unexecutable. That is the laundering R2 exists to stop, in the row that
                     # was added the same day the rule was written.
                     extended=len(chunk) > 1, occasion=occasion)

    # ⚠ THE BOUND IS THE COST, NOT THE SCENE COUNT, and getting that wrong made the DEFAULT
    # chooser overspend by construction: once `extended` was actually set, five greedy scenes
    # cost ten against a budget of five and every season using `make_chooser` refused itself.
    # Found by running the corpus after `H-77` stopped being inert -- the row and the packer are
    # the same mechanism seen from two sides, and fixing one without the other is what broke it.
    ext = fx.get("extended_scene_cost")

    def take(chunks) -> list:
        out, left = [], n_scenes
        for chunk in chunks:
            if left <= 0:
                break
            # An extension the person cannot afford is taken as a PLAIN scene rather than
            # skipped: they still pursue the opportunity, with less in it. Skipping would be the
            # engine deciding what they leave undone, which is L1.
            if len(chunk) > 1 and ext > left:
                chunk = chunk[:1]
            cost = ext if len(chunk) > 1 else 1
            out.append(scene(len(out), chunk))
            left -= cost
        return out

    if rule == "by_subject":
        seen: dict = {}
        for c in ranked:
            seen.setdefault(c.subject or "", []).append(c)
        chunks = [seen[subj][start:start + width]
                  for subj in sorted(seen)
                  for start in range(0, len(seen[subj]), width)]
    else:
        chunks = [ranked[i:i + width] for i in range(0, len(ranked), width)]
    return take(chunks)
