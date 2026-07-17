"""
agon_harness.py — P3-lite: the human-plays-Agôn interactive harness (Stage-1 kernel validation).

WHY THIS EXISTS. The promoted social-contest kernel (systems/social_contest/sim/contest/) is fully built and
engine-against-itself tested (_kernel_tests.py, sim/tests/test_contest_kernel.py), but — per the
2026-07-05 Fable-5 subsystem audit (designs/audit/2026-07-05-fable5-social-contest-audit/
fable5_social_contest_audit_v1.md, finding D4/N-7) — NO HUMAN has ever played it. N-7 (UPHELD by the
independent critic, finding_status.md): "~13 recurring per-decision consultations per Agôn exchange
vs the immersion audit's 3–4 personal-scene ceiling; no onboarding/complexity-gating doc exists."
D4 (§4, same report): "one exchange demands ~13 per-decision consults against a 3–4 ceiling ... the
CANONICAL UI doc's contest section specifies the pre-CR3 system wholesale" — i.e. the dramatic-
legibility promise (the walkthrough's own 3-question test) has never been empirically checked.

WORKPLAN CONTEXT (cite per task instruction). HANDOFF_SC.md's Decisions/Next-actions log this
explicitly: "Sequencing adopted: P0 spec-reconciliation -> P1 consequence spine (∥ P3-lite
human-plays-Agôn slice) -> Stage 4 -> calibration" and, after ED-SC-0006/0007 executed the P1
consequence-spine work (kernel routing + party-derivation bridge — registers/editorial_ledger.jsonl
ED-SC-0006), "NEXT: P3-lite — a minimal interactive Agôn harness over the existing kernel to run the
dramatic-legibility test with a human and measure the ~13-consult load (audit D4/N-7) before Stage 4
multiplies interaction shapes." THIS FILE is that harness. It is additive-only: no kernel file
(wrapper.py/resolver.py/policy.py/appraise.py/armature.py/dictionaries.py/modes.py/primitives.py/
contract.py) is modified. It is read-only against the public API plus the same private accessors the
kernel's OWN test suite already uses (Bout._view/_apply, bout.c[...] fields — see
wrapper._stage3_resolution_invocation_check and _kernel_tests.py for the precedent of touching these
from outside resolve()); no new kernel behavior is introduced.

WHAT IT DOES (per designs/audit/2026-07-01-contest-player-interaction/
player_interaction_walkthrough_v1.md, "the walkthrough"):
  1. SETUP screen (walkthrough §1): builds a real Contest via wrapper.build_contest(...) on a named
     canonical proceeding (default: formal_contest — the walkthrough's own worked example, "Formal
     Contest — 3 exchanges"); shows venue, adjudicator type + primary attribute, Argue-pool size,
     Persuasion-Track start/bands, stakes (harness-authored generic flavor — this is a standalone demo
     with no in-fiction scene context, not a claim about a specific canonical stake).
  2. THE EXCHANGE LOOP (walkthrough §2): the human plays Side A. Each of the human's turns prints the
     Appraise-visible information (via appraise.appraise_armature, against the adjudicator's
     armature_position — see WORKAROUND 1 below), then prompts, in the walkthrough's own order,
     Style-card pick (walkthrough §2 Step 2) followed by whatever the chosen Move kind additionally
     requires (an Appeal for advance/hard; a target ground for shift). Side B runs on an existing AI
     policy (policy.logos_spammer by default; --ai-policy selects any policy.POLICIES key).
  3. After each exchange, prints Face / Concentration / the venue's ACTUAL win-condition tracker
     (Persuasion Track / tally / proof-bar / grace-threshold / vote-at-close room-momentum — whichever
     the chosen proceeding really uses; walkthrough §2 Step 4 + §0's "every number the resolver uses is
     a number the player can see" principle).
  4. At contest end: the verdict (winner/band/reason — walkthrough §3), plus the harness's own reason
     for existing — a prominent CONSULT COUNT: the total number of discrete input() prompts the human
     answered across the whole contest (the empirical measurement N-7/D4 asked for).
  5. Resilient to garbage input: every choice re-prompts on an unrecognised answer (and on EOF/exhausted
     scripted input, which VERIFICATION relies on), with a bounded retry ceiling that auto-selects a
     safe default rather than hanging or crashing — see ask_choice().

WORKAROUNDS / DISCOVERED GAPS (flagged per task instruction — none of these touch the kernel):
  WORKAROUND 1 — no in-kernel "appraise the opponent's style" Move exists. VALID_KINDS (resolver.py)
    has no "appraise" kind, and ContestView carries no pre-roll signal of the opponent's chosen Style;
    the only REAL, callable Appraise-reveal primitive in the corpus is appraise.appraise_armature(),
    which reveals the ADJUDICATOR's armature_position (Stage 3 / Gate C), not the opponent's style. The
    harness therefore (a) simulates a plain "read the room" pool roll locally, reusing the kernel's own
    Pool.size/roll_net/degree functions and the REAL venue's base_ob (no fabricated numbers), and
    (b) feeds the resulting degree into appraise_armature() against the adjudicator's armature_position
    to produce the walkthrough's info-ladder reveal. This demonstrates the one Appraise primitive that
    actually exists; it is NOT gated behind the exchange's setup beat (no kind/action-economy exists for
    that in VALID_KINDS) — a real "spend the beat to Appraise" mechanic is future kernel/wrapper scope,
    not invented here.
  WORKAROUND 2 — ArmatureConfig.styles is documented as "a single per-contest choice" (armature.py) and
    is a frozen dataclass, set once. But Bout.armature is a plain (non-frozen) instance attribute, so
    the harness reassigns a fresh ArmatureConfig each exchange to give the human (and the AI, via a
    simple deterministic style-rotation stand-in) a genuinely PER-EXCHANGE style choice, matching the
    walkthrough's "Step 2 — Style choice" happening inside "THE EXCHANGE LOOP — repeated exchange_count
    times". This is a discovered flexibility (Bout never re-validates armature between exchanges), not
    an officially-sanctioned per-exchange API — flag for a future kernel improvement: an explicit
    Bout.set_style(side, style_key) or a documented per-exchange ArmatureConfig contract.
  WORKAROUND 3 — build_contest()/resolve_contest() do not accept or pass through an `armature=`
    parameter (Bout does, but _resolve_agon() in wrapper.py never supplies one). The harness builds its
    own Bout directly from the Contest's own public fields (side_a/side_b/venue/adjudicator — exactly
    what wrapper._resolve_agon does internally) plus an armature= kwarg, rather than calling
    resolve_contest(). Future wrapper enhancement: build_contest/resolve_contest could accept an
    optional armature passthrough.
  WORKAROUND 4 — no Style→Appeal (ethos/pathos/logos) mapping exists anywhere in the corpus; the two
    are genuinely orthogonal Move-contract axes (Style feeds CR4/armature; Appeal feeds resonance via
    Venue.role()/Adjudicator.character()). The walkthrough's Step 2 presents "Style choice" as the core
    tactical decision without naming a second Appeal axis. Rather than invent a mapping, the harness
    asks for BOTH explicitly (Style, then Appeal) — flagged here as an open design-authority question
    for a future synthesis of the two axes into one player-facing choice, not fabricated silently.
  WORKAROUND 5 — Bout.resolve() is not called. Its exchange loop (advance the budget, apply each side's
    move, check faults after each move, check the win-condition after each full exchange, check again
    closing=True after budget exhaustion) is REPLICATED verbatim in run_contest_interactive() below (not
    altered) so the harness can interleave printing between steps. Future kernel improvement: an
    optional per-move / per-exchange callback hook on Bout.resolve() would let a harness observe without
    duplicating the loop.

VERIFICATION. See the task's own driving script (this file is exercised, not eyeballed): a scripted
run monkeypatches builtins.input with a canned queue simulating a human clicking through a full
contest, and asserts the harness completes without crashing, prints a verdict, and reports a consult
count — done for >=2 divergent playthroughs (aggressive/Direct-only vs passive/support-heavy). See the
session's final report for the exact commands and captured output.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from .contract import A, B, other, Move, ContestView, Panel
from .primitives import Stasis, Appeal, Reserve, Pool, EvidenceItem, Dossier
from .resolver import (Bout, Contestant, PersuasionTrack, TallyAtClose, ProofBar,
                       GraceThreshold, VoteAtClose, roll_net, degree)
from .wrapper import build_contest
from .policy import POLICIES, logos_spammer
from .dictionaries import STYLES_TABLE, PROCEEDINGS_TABLE, ADJUDICATORS_TABLE, derive_interaction
from .armature import ArmatureConfig, ArmaturePosition
from .appraise import appraise_armature

__all__ = ["HarnessState", "ask_choice", "setup_contest", "print_setup_screen", "print_appraise",
           "print_bars", "human_turn", "ai_turn", "print_move_result", "run_contest_interactive", "main"]

STYLE_KEYS = list(STYLES_TABLE.keys())              # ["precedent", "suppression", "vision", "insinuation"]
GROUND_LABELS = {                                     # display labels for the Stasis ladder
    Stasis.FACT: "Fact (what happened)",
    Stasis.DEFINITION: "Definition (what it counts as)",
    Stasis.QUALITY: "Quality (was it justified)",
    Stasis.JURISDICTION: "Jurisdiction (the right venue)",
    Stasis.CONSEQUENCE: "Consequence (what follows)",
    Stasis.FEASIBILITY: "Feasibility (can it even be done)",
}

# [SEED] harness demo value — an illustrative adjudicator armature_position for THIS standalone demo
# contest only (armature.py: any per-adjudicator armature_position is authored per-instance content,
# defaulting to the zero vector when unset; there is no canonical "Formal Contest crowd" value to cite
# — this is scenario flavor, analogous to authoring one NPC's stats for a worked example, not a
# ratified mechanical constant). Leans toward Consequence (a crowd swayed by "what happens next") with
# a secondary Evidence lean, per WORKAROUND 1 above.
DEMO_JUDGE_POSITION = ArmaturePosition(consequence=0.75, evidence=0.35)

# Deterministic AI-side style rotation (WORKAROUND 2) — a harness-authored stand-in so the AI side also
# carries a Style for CR4/armature + the derive_interaction() flavor line; NOT an NPC behavior policy
# (that is Stage-4/npc_behavior_v30 scope), just a round-robin so the demo isn't Style-less on one side.
_AI_STYLE_ROTATION = STYLE_KEYS


@dataclass
class HarnessState:
    """Tracks the harness's own measurement: the discrete input() consult count (the empirical number
       audit finding D4/N-7 asked for)."""
    consult_count: int = 0


def _raw_input(state: HarnessState, prompt: str) -> str:
    """Every call is one discrete consult (counted whether the answer is valid or garbage — the
       harness's whole point is measuring how many of these a human is asked). Resilient to EOF /
       exhausted scripted input (verification pipes a finite canned queue): returns '' rather than
       raising, which ask_choice() below treats as an ordinary invalid answer."""
    state.consult_count += 1
    try:
        return input(prompt)
    except (EOFError, StopIteration):
        return ""


def ask_choice(state: HarnessState, title: str, options: List[Tuple[str, str]],
              retries: int = 15) -> str:
    """Prompt a numbered menu; return the chosen option KEY. Accepts either the 1-based index or the
       key itself (case-insensitive). RESILIENT to garbage/EOF input: re-prompts (never crashes) up to
       `retries` times, then auto-selects the first option (flagged loudly) so a pathological or
       exhausted input stream can never hang the harness."""
    if not options:
        raise ValueError("ask_choice: no options offered")
    print("\n" + title)
    for i, (_, label) in enumerate(options, 1):
        print(f"  [{i}] {label}")
    attempts = 0
    while True:
        raw = _raw_input(state, "> ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1][0]
        for key, _ in options:
            if raw.lower() == str(key).lower():
                return key
        attempts += 1
        if attempts >= retries:
            print(f"  (no valid answer after {retries} tries -- defaulting to "
                  f"[1] {options[0][1]})")
            return options[0][0]
        print(f"  Didn't catch {raw!r} -- enter a number 1-{len(options)}, or try again.")


# ─────────────────────────────────────────────────────────────────────────────────────────
# SETUP (walkthrough §1)
# ─────────────────────────────────────────────────────────────────────────────────────────

def setup_contest(proceeding: str = "formal_contest", human_faculty: int = 5, ai_faculty: int = 4,
                  human_charisma: int = 4, ai_charisma: int = 4):
    """Build a real Contest (wrapper.build_contest) + the manually-assembled Bout carrying an opt-in
       armature (WORKAROUND 3). Faculties default to 4-5, matching the kernel's own test conventions
       (_kernel_tests.py). Gives the human two illustrative EvidenceItem rows (instance/demo content —
       not a canonical constant) so the 'evidence' action has something to demonstrate."""
    human = Contestant(
        human_faculty, charisma=human_charisma,
        dossier=Dossier([
            EvidenceItem(Stasis.QUALITY, 1.8, Appeal.LOGOS),      # usable at the default start_ground
            EvidenceItem(Stasis.CONSEQUENCE, 1.2, Appeal.PATHOS), # usable if the issue reframes upward
        ]))
    ai = Contestant(ai_faculty, charisma=ai_charisma)

    contest = build_contest(human, ai, venue=proceeding)

    adjudicator = contest.adjudicator
    if isinstance(adjudicator, Panel):
        judge_positions = {id(m): DEMO_JUDGE_POSITION for m in adjudicator.members}
    else:
        judge_positions = {id(adjudicator): DEMO_JUDGE_POSITION}

    armature = ArmatureConfig(styles={}, positions=judge_positions, cr5=True)
    bout = Bout(contest.side_a, contest.side_b, contest.venue, contest.adjudicator,
               record=True, armature=armature)
    return contest, bout, judge_positions


def print_setup_screen(contest, bout, proceeding: str) -> None:
    proc = PROCEEDINGS_TABLE[proceeding]
    adj = ADJUDICATORS_TABLE.get(contest.adjudicator_type) if contest.adjudicator_type else None
    pool = Pool.size(bout.c[A].faculty)
    print("=" * 70)
    print(f"  CONTEST FRAMING -- {proc.name} ({proc.exchange_count[1]} exchanges)")
    print("=" * 70)
    print(f"  {proc.flavor}")
    if adj is not None:
        print(f"\n  Adjudicator: {adj.name} -- {adj.who_decides}")
        print(f"  Primary attribute (doubles your Argue pool): {adj.primary_attribute}")
    print(f"  Your Argue pool this contest: {pool}D (faculty {bout.c[A].faculty})")
    win = bout.v.win
    if isinstance(win, PersuasionTrack):
        print(f"  Persuasion Track starts at {win.start:.1f}/10 "
              f"(bands: <=1 Total Defeat / <=3 Decisive Loss / 4-6 Compromise / "
              f">=7 Decisive Win / >=9 Total Victory)")
    else:
        print(f"  Win condition: {type(win).__name__} (no Persuasion Track for this proceeding)")
    print(f"  Stakes (harness demo -- a generic illustrative frame, not a specific in-fiction scene):")
    print(f"    Win: your position carries. Lose: you walk away with nothing to show for it. "
          f"Draw/Compromise: a partial, unsatisfying middle ground.")
    print(f"  Appraise hints banked so far: none -- nothing banked before the first exchange.")
    print()


# ─────────────────────────────────────────────────────────────────────────────────────────
# APPRAISE (WORKAROUND 1) + STATE BARS (walkthrough §2 Steps 1/4)
# ─────────────────────────────────────────────────────────────────────────────────────────

def _band_name(deg: int) -> str:
    return {0: "Failure", 1: "Partial", 2: "Success"}.get(deg, "Overwhelming")


def print_appraise(bout, judge_position: ArmaturePosition) -> None:
    """Simulate a 'read the room' Appraise roll (reusing the kernel's own Pool/roll_net/degree
       functions and the REAL venue's base_ob -- no fabricated numbers), then reveal via the actual
       appraise_armature() primitive (Stage 3 / Gate C). See WORKAROUND 1: no in-kernel Appraise Move
       kind exists to gate this behind the exchange's setup beat, so it prints as free information."""
    pool = Pool.size(bout.c[A].faculty)
    net = roll_net(pool)
    deg = degree(net, bout.v.base_ob, pool)
    reveal = appraise_armature(judge_position, deg)
    print(f"[Appraise -- reading the room: {pool}D, degree {deg} ({_band_name(deg)})]")
    band = reveal["band"]
    if band == "failure":
        print(f"  A misleading read: you sense the room favors {reveal['read']} -- "
              f"(this is a deliberately WRONG signal; a bad Appraise costs you, it never returns null)")
    elif band == "partial":
        reg = reveal["register"] or "no clear lean"
        print(f"  Partial read: the room's register leans {reg}.")
    elif band == "success":
        print(f"  Clear read: the room is most moved by {reveal['dominant_axis']}.")
    else:
        axis = reveal.get("dominant_axis")
        if axis is None:
            print("  Overwhelming read: ...but this room has no strong armature to read (flat/neutral).")
        else:
            print(f"  Overwhelming read: the room is most moved by {axis} "
                  f"(strength: {reveal['strength']}).")


def print_bars(bout) -> None:
    for side, label in ((A, "YOU"), (B, "OPPONENT")):
        c = bout.c[side]
        face_line = f"Face {c.face.v:.1f}/10"
        if c.charisma:
            face_line += f" (Face_current {c.face_current()}/{c.face_max()})"
        print(f"  {label:8s} {face_line} | Concentration {c.reserve.cur}/{c.reserve.max}")
    win = bout.v.win
    if isinstance(win, PersuasionTrack):
        t = win.track(bout.state)
        print(f"  Persuasion Track: {t:.2f}/10")
    elif isinstance(win, TallyAtClose):
        print(f"  Exchange tally (majority at close decides): "
              f"YOU {bout.state.adv[A]:.2f} -- OPPONENT {bout.state.adv[B]:.2f}")
    elif isinstance(win, ProofBar):
        net = bout.state.adv[win.ch] - bout.state.adv[other(win.ch)]
        print(f"  Proof bar: net {net:.2f} vs bar {win.bar:.2f} (challenger: "
              f"{'YOU' if win.ch == A else 'OPPONENT'})")
    elif isinstance(win, GraceThreshold):
        print(f"  Grace threshold: {bout.state.adv[win.pet]:.2f} vs bar {win.bar:.2f} "
              f"(petitioner: {'YOU' if win.pet == A else 'OPPONENT'})")
    elif isinstance(win, VoteAtClose):
        print(f"  Room momentum (drives the terminal bench ballot's lean): "
              f"YOU {bout.state.adv[A]:.2f} -- OPPONENT {bout.state.adv[B]:.2f}")
    else:
        print(f"  adv: YOU {bout.state.adv[A]:.2f} -- OPPONENT {bout.state.adv[B]:.2f}")


# ─────────────────────────────────────────────────────────────────────────────────────────
# THE HUMAN'S TURN (walkthrough §2 Step 2: Style/genre/orientation, then whatever the Move requires)
# ─────────────────────────────────────────────────────────────────────────────────────────

def human_turn(state: HarnessState, bout, view: ContestView, i: int) -> Tuple[Move, Optional[str]]:
    """Print the current legible state + Appraise, then walk the human through the walkthrough's own
       decision order: Style card first, then whatever the chosen Move kind additionally needs.
       Returns (Move, chosen_style_key_or_None)."""
    print(f"\n{'=' * 70}\nEXCHANGE {i + 1} of {bout.v.budget} -- YOUR MOVE "
          f"(live issue: {GROUND_LABELS.get(view.live_ground, view.live_ground)})\n{'=' * 70}")
    print_bars(bout)
    print_appraise(bout, DEMO_JUDGE_POSITION)

    c = bout.c[A]
    kind_options: List[Tuple[str, str]] = [
        ("advance", f"Argue on the live issue (cost {Reserve.COST['advance']} Concentration)"),
    ]
    if view.can_hard:
        kind_options.append(
            ("hard", f"Press hard -- a bigger swing (cost {Reserve.COST['hard']}; only licit if you "
                      f"clearly outrank them -- if it's NOT licensed, it's an immediate barred-device "
                      f"loss for you, not just a wasted turn)"))
    kind_options.append(
        ("support", f"Support / regroup (cost {Reserve.COST['support']}; refills Concentration, "
                    f"builds a little Face)"))
    if view.evidence_available > 0:
        kind_options.append(
            ("evidence", f"Present evidence (cost {Reserve.COST['evidence']}; {view.evidence_available} "
                        f"relevant item(s) held, hidden value)"))
    ladder_idx = Stasis.LADDER.index(view.live_ground)
    if ladder_idx + 1 < len(Stasis.LADDER):
        kind_options.append(
            ("shift", f"Reframe the issue to stronger ground (cost {Reserve.COST['shift']})"))
    if bout.v.allow_rebuttal:
        kind_options.append(
            ("rebut", f"Rebut -- attack the opponent's advancement directly (cost {Reserve.COST['rebut']})"))
    kind_options.append(("pass", "Pass -- decline this exchange"))

    kind = ask_choice(state, "What do you do?", kind_options)

    style_key: Optional[str] = None
    if kind in ("advance", "hard"):
        style_options = [(k, f"{s.name} ({s.genre} x {s.orientation}) -- {s.flavor}")
                         for k, s in STYLES_TABLE.items()]
        style_key = ask_choice(state, "Pick your Style (Genre x Orientation):", style_options)
        appeal_options = [(Appeal.ETHOS, "Ethos -- your character/credibility"),
                          (Appeal.PATHOS, "Pathos -- the room's emotion"),
                          (Appeal.LOGOS, "Logos -- logic and evidence")]
        appeal = ask_choice(state, "Which appeal carries it?", appeal_options)
        mv = Move(kind, appeal, view.live_ground)
    elif kind == "shift":
        ground_options = [(g, GROUND_LABELS.get(g, g)) for g in Stasis.LADDER[ladder_idx + 1:]]
        target = ask_choice(state, "Reframe to which ground?", ground_options)
        mv = Move("shift", None, target)
    elif kind == "rebut":
        mv = Move("rebut", ground=view.live_ground)
    else:  # support / evidence / pass need no further input
        mv = Move(kind)
    return mv, style_key


def ai_turn(policy, view: ContestView, i: int) -> Tuple[Move, Optional[str]]:
    """The AI side's move (an existing policy callable) + its demo style-rotation stand-in
       (WORKAROUND 2) so CR4/armature and the interaction-type flavor line have something on both
       sides. The rotation is a harness convenience, not an NPC behavior policy."""
    mv = policy(view)
    style_key = _AI_STYLE_ROTATION[i % len(_AI_STYLE_ROTATION)] if mv.kind in ("advance", "hard") else None
    return mv, style_key


def print_move_result(bout, side: str, mv: Move, before_adv: float,
                      before_fault: Tuple) -> None:
    c = bout.c[side]
    who = "YOU" if side == A else "OPPONENT"
    gain = bout.state.adv[side] - before_adv
    after_fault = (c.fault.evasion, c.fault.yields, c.fault.contradicted, c.fault.barred)
    faulted = after_fault != before_fault
    line = f"  {who} -> {mv.kind}"
    if mv.appeal:
        line += f"/{mv.appeal}"
    if mv.ground:
        line += f" ({GROUND_LABELS.get(mv.ground, mv.ground)})"
    line += f": gain {gain:+.2f}"
    if faulted and c.fault.reason:
        line += f"  [{c.fault.reason}]"
    print(line)


# ─────────────────────────────────────────────────────────────────────────────────────────
# THE EXCHANGE LOOP (WORKAROUND 5 — replicates Bout.resolve()'s own loop; does not modify it)
# ─────────────────────────────────────────────────────────────────────────────────────────

def _describe_verdict(bout, verdict) -> str:
    winner, reason = verdict
    band_names = {
        "A_total": "TOTAL VICTORY for YOU", "A_decisive": "DECISIVE WIN for YOU",
        "committee": "COMPROMISE", "B_decisive": "DECISIVE LOSS for YOU",
        "B_total": "TOTAL DEFEAT for YOU",
    }
    if winner in band_names:
        headline = band_names[winner]
    elif winner == A:
        headline = "YOU WIN"
    elif winner == B:
        headline = "YOU LOSE"
    else:
        headline = "DRAW"
    return f"{headline}  (raw result: winner={winner!r}, reason={reason!r})"


def run_contest_interactive(contest, bout, judge_positions: Dict, state: HarnessState,
                           ai_policy=logos_spammer) -> Tuple[Tuple, HarnessState]:
    """Runs the full contest with the human playing Side A. Replicates resolver.Bout.resolve()'s exact
       control flow (advance the budget; apply each side's move; check faults after EACH move; check
       the win-condition after each full exchange; check again closing=True after budget exhaustion —
       see WORKAROUND 5) so printing can be interleaved without altering resolution. Returns
       (verdict, state)."""
    verdict = None
    final_exchange = 0
    for i in range(bout.v.budget):
        final_exchange = i + 1
        a_style_this_exchange: Optional[str] = None
        b_style_this_exchange: Optional[str] = None
        for side in (A, B):
            view = bout._view(side, i)
            if side == A:
                mv, style_key = human_turn(state, bout, view, i)
                a_style_this_exchange = style_key
            else:
                mv, style_key = ai_turn(ai_policy, view, i)
                b_style_this_exchange = style_key

            # WORKAROUND 2: reassign a fresh per-exchange ArmatureConfig right before EACH side's own
            # move, carrying only THIS exchange's chosen style(s) (a move only ever reads its OWN
            # side's style_of() in resolver._apply, so nothing is lost by not carrying the other side's
            # entry forward across exchanges).
            styles: Dict[str, str] = {}
            if a_style_this_exchange is not None:
                styles[A] = a_style_this_exchange
            if b_style_this_exchange is not None:
                styles[B] = b_style_this_exchange
            bout.armature = ArmatureConfig(styles=styles, positions=judge_positions, cr5=True)

            before_adv = bout.state.adv[side]
            c = bout.c[side]
            before_fault = (c.fault.evasion, c.fault.yields, c.fault.contradicted, c.fault.barred)
            bout._apply(side, mv)
            print_move_result(bout, side, mv, before_adv, before_fault)

            if side == B and a_style_this_exchange is not None and b_style_this_exchange is not None:
                # NOTE: derive_interaction() is a descriptive typed-surface lookup (dictionaries.py),
                # not consumed by resolver.py's live resolution (each side's argument resolves via its
                # own additive _advance() call, not a pairwise compare). Printed here for player
                # legibility/flavor per the walkthrough §2 Step 3 naming convention -- it does not
                # change the numeric outcome.
                it = derive_interaction(a_style_this_exchange, b_style_this_exchange)
                print(f"  Interaction: {it.player_name} ({it.condition})")

            hit = bout.v.faults.check({A: bout.c[A].fault, B: bout.c[B].fault})
            if hit:
                loser, reason = hit
                detail = bout.c[loser].fault.reason
                verdict = (other(loser), f"clinch:{reason}" + (f" - {detail}" if detail else ""))
                break
        if verdict is not None:
            break
        print(f"\n--- After exchange {i + 1} of {bout.v.budget} ---")
        print_bars(bout)
        w = bout.v.win.resolve(bout.state, closing=False, adj=bout.adj)
        if w:
            verdict = (w, "win")
            break
    if verdict is None:
        w = bout.v.win.resolve(bout.state, closing=True, adj=bout.adj)
        verdict = (w, "draw" if w == "draw" else "win")

    print("\n" + "=" * 70)
    print("  RESOLUTION")
    print("=" * 70)
    print_bars(bout)
    print(f"\n  VERDICT: {_describe_verdict(bout, verdict)}")
    per_exchange = state.consult_count / final_exchange if final_exchange else 0.0
    print(f"\n  {'=' * 66}")
    print(f"  CONSULT COUNT (the measurement this harness exists to take, audit D4/N-7):")
    print(f"    {state.consult_count} discrete input() prompts across {final_exchange} exchange(s) "
          f"(~{per_exchange:.1f} per exchange).")
    print(f"  {'=' * 66}")
    return verdict, state


# ─────────────────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────────────────

def main(argv: Optional[List[str]] = None) -> Tuple[Tuple, HarnessState]:
    p = argparse.ArgumentParser(description="P3-lite: play one Agon contest against an AI opponent.")
    p.add_argument("--proceeding", default="formal_contest", choices=sorted(PROCEEDINGS_TABLE))
    p.add_argument("--human-faculty", type=int, default=5)
    p.add_argument("--ai-faculty", type=int, default=4)
    p.add_argument("--ai-policy", default="logos", choices=sorted(POLICIES))
    args = p.parse_args(argv)

    contest, bout, judge_positions = setup_contest(
        proceeding=args.proceeding, human_faculty=args.human_faculty, ai_faculty=args.ai_faculty)
    print_setup_screen(contest, bout, args.proceeding)

    state = HarnessState()
    verdict, state = run_contest_interactive(
        contest, bout, judge_positions, state, ai_policy=POLICIES[args.ai_policy])
    return verdict, state


if __name__ == "__main__":
    main(sys.argv[1:])
