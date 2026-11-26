"""B11.72 (`08_FI_07` §2 (a), FRES §2 row 8): `examine` FORMS ON A PLACE HE HAS HEARD OF.

`examine` is classed on a Site (`verb_table.yaml`) and no question the realm delivers carries a Site among its referents, so it formed
nowhere. Its `site` is now choice-sourced (`rosters.yaml: choice_sourced`, `ledger_ranges`): the range is the ids his OWN ledger presents as a
Site, read person-side with no World. Whether he stands there is the fold's (`present_at`), and a man who does not is refused.

B11.76 (`08_FI_07` Cut A): THE INQUIRY ROW'S ENDING AND ITS TRANSCRIPT. The twenty runs are `test_playable_inquiry.py::inquiry_runs`'s (one set, two seasons).
"""
from __future__ import annotations

import inspect
import io
from collections import Counter

from ..data.matrix import Step, WriteClass
from ..decision.options import opening_set
from ..decision.sheet import take_ranked
from ..harness import aperture
from ..harness import probes as P
from ..harness import scenarios as S
from ..harness.play_surface import board
from ..loop.driver import SeasonDriver, mint_token
from ..queries.person_q import LedgerReader, deed_doers, ledger_weigh
from ..seam import Resolution
from ..state.carriers import DETERMINED_BY, Act, Claim, Question, Tenure, View, fade_of
from .test_playable_inquiry import SEASONS, inquiry_runs

HEARD, NOT_A_SITE = "site_harbour", "Hh"      # `tiny_world`: a Site in `S`; a hearth. `p_low` stands in `Hh`, not at the harbour.


def _examines(w, pid="p_low"):
    p = w.persons[pid]
    q = Question("q_b1172", "claim_landed", ("p_mid",), "")
    return [c for c in opening_set(p, View(p.id, [], w.fixtures.get("view_k"), q), q, w.fixtures) if c.verb == "examine"]


def test_examine_forms_on_a_site_he_has_heard_of():
    """§2 (a): "a planted investigator who holds a claim about a Site and stands elsewhere forms it and is refused". He holds one firsthand reading
    of the harbour's condition and one of a hearth's grain, and stands at the hearth: `examine` is offered on the harbour alone (the hearth is no
    Site his claims present), carries it as `site`, and the fold refuses it on `present_at` with the row's one kind. FALSIFIER: the bag naming a
    place he is not at is the CP-T06-04 presence-aware decline's case, not this range's. CONTROL: with no claim about a Site he forms none."""
    w = P.tiny_world()
    assert _examines(w) == [], "control: a man who has heard of no Site forms no `examine`"
    p = w.persons["p_low"]
    p.ledger.append(Claim("c_site", p.id, HEARD, "condition", 1, 0, "firsthand", 80, "own"))
    p.ledger.append(Claim("c_hearth", p.id, NOT_A_SITE, "stores:grain", 8, 0, "firsthand", 80, "own"))
    got = _examines(w)
    assert [(c.subject, c.operands.get("site")) for c in got] == [(HEARD, HEARD)], got
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    act = Act(id="a_examine", actor=p.id, verb="examine", payload={"subject": HEARD, **got[0].operands})
    w.acts.append(act)
    out = d._fold(w, mint_token(w, WriteClass.ACTS), act, Resolution("Success", {}))
    assert [e.kind for e in out] == ["inquiry.refused"], [e.kind for e in out]


# ======================================================================================
# B11.76 (`08_FI_07` Cut A, §4): THE INQUIRY ROW'S ENDING, ITS CONTROL AND ITS TRANSCRIPT.
# ======================================================================================
def test_cut_a_runs_end_by_a_predicate_at_seeds_0_to_19():
    """Gate: `inquiry_world(s)` at seeds 0 to 19, two seasons, the shipped chooser in the investigator's seat: every run ends by one of the row's predicates or at
    the cap (`inquiry_ending` read off the finished world agrees with what the runner named), two runs of one seed give one content hash, and at least two
    ending kinds occur among the twenty. FALSIFIER (`08_FI_07` falsifier 3): all twenty end by the same predicate, so the scenario offers no real choice."""
    runs = inquiry_runs()
    for r in runs:
        assert (r["ending"] is None and r["seasons"] == SEASONS) or r["ending"] in S.INQUIRY_KINDS, (r["ending"], r["seasons"])
        assert S.inquiry_ending(r["world"], r["seat"]) == r["ending"]
    assert S.run("inquiry", 0, SEASONS)["hash"] == runs[0]["hash"], "two runs of one seed gave two hashes"
    endings = Counter(r["ending"] for r in runs if r["ending"] is not None)
    assert len(endings) >= 2, f"FALSIFIER: ending kinds among twenty runs {dict(endings)} ({len(runs) - sum(endings.values())} reached the cap)"


def test_a_never_inquiring_script_ends_cold_or_rests():
    """`IS-B2-FI-03`'s control (`08_FI_07`'s `test_a_never_inquiring_callback_ends_by_the_budget_predicate`, one test): a seat that never picks an inquiry verb
    forms no inquiry, holds no conclusion, and so cannot end `rests`; the run ends `cold` once four seasons have passed and at the cap before. CONTROL: the same
    seed with the shipped ranking inquires (an inquiry act of his, the aperture's `formed`) and moves the content hash, so the choice is load-bearing."""
    inquiry = set(aperture.inquiry_verbs())
    never = lambda sheet: [i for i in take_ranked(sheet) if sheet.candidates[i].verb not in inquiry]
    seed = 0
    quiet, ranked = S.run("inquiry", seed, SEASONS, pick=never), inquiry_runs()[seed]
    formed = lambda r: sum(c["formed"] for c in aperture.inquiry_counts(r["world"], S.INVESTIGATOR_SEAT).values())
    assert quiet["seat_deliberations"] >= 1, "the seat was never asked; the control proves nothing"
    assert formed(quiet) == 0 and not S.concluded(quiet["world"], S.INVESTIGATOR_SEAT)
    assert quiet["ending"] == ("cold" if SEASONS >= S.COLD_SEASONS else None), quiet["ending"]
    assert formed(ranked) > 0 and ranked["hash"] != quiet["hash"], "the ranking never inquired, or the pick moved nothing"


def _planted_row(monkeypatch):
    """The `inquiry` row with a bench's disposal edge on the forger planted after the first season: the one run in which `answer` has something to print."""
    row = S.SCENARIOS["inquiry"]

    def ending(w, pid, left):
        if w.tick > S.CASE_OPENS and not any(t.id == "t_planted" for t in w.tenures):
            w.add_tenure(Tenure("t_planted", S.INQUIRY_FORGER, "off_bench_a", "oblige", since=w.tick, payload={DETERMINED_BY: "planted"}))
        return row.ending(w, pid, left)
    monkeypatch.setitem(S.SCENARIOS, "inquiry", S.Scenario(build=row.build, seat=row.seat, ending=ending, verbs=row.verbs, kinds=row.kinds,
                                                           reading=row.reading, answer=row.answer))


def _transcript(monkeypatch, capsys, *flags):
    monkeypatch.setattr("sys.stdin", io.StringIO("\n" * 200))          # blank: take the ranking, every lap
    assert S.main(["inquiry", "--seed", "0", "--seasons", "2", "--play", *flags]) == 0
    return capsys.readouterr().out.splitlines()


def test_the_play_transcript_never_prints_the_true_doer(monkeypatch, capsys):
    """`IS-B2-FI-03` (4), A-49: whether the person named is the Event's actor is printed only under `--developer`, and not while the run lives. A planted run
    (a bench's disposal edge on the forger after season one) ends `determined` and names him: the `--play` transcript carries no such line; with `--developer` it
    carries one, after the last lap. SOURCE: the row's `answer` is called from one line of the module and that line is guarded by `--developer`. CONTROL: the
    developer run prints it, so the absence above could have failed."""
    _planted_row(monkeypatch)
    plain = _transcript(monkeypatch, capsys)
    dev = _transcript(monkeypatch, capsys, "--developer")
    assert any(t.startswith("-- lap") for t in plain), "the run held no lap: nothing was played"
    assert any(" · ending determined" in t for t in plain), "the planted run did not end determined"
    assert not [t for t in plain if "DEVELOPER" in t or "actor" in t], "the play transcript printed the doer's reading"
    marked = [i for i, t in enumerate(dev) if t.startswith("DEVELOPER · named p_forger")]
    assert len(marked) == 1 and "named is the actor: yes" in dev[marked[0]], dev[-6:]
    assert marked[0] > max(i for i, t in enumerate(dev) if t.startswith("-- lap")), "printed while the run lived"
    src = inspect.getsource(S).splitlines()
    calls = [i for i, t in enumerate(src) if ".answer(" in t]
    assert len(calls) == 1 and "if a.developer" in src[calls[0] - 1], [src[i - 1: i + 1] for i in calls]


# ======================================================================================
# B11.77 (`08_FI_07` §3, `IS-B2-FI-04`): ONE BOARD, ONE OWNER -- `person_q.dossier` read, `play_surface.board` printed.
# ======================================================================================
def test_every_claim_appears_in_one_board_group():
    """`IS-B2-FI-04`: for the scenario's investigator after one season, every claim in his ledger appears in exactly one board group (`dossier`'s rows are one per claim,
    a group being the rows that share `(subject, predicate, value)`), a group's `support` is what clause 4 weighs for the same claims, and the suspects line equals
    `deed_doers` of his goal. FALSIFIER: a claim in no row or in two; a group whose support differs from `LedgerReader._support` under `ledger_weigh`. CONTROL: a
    ledger the run left too thin to tell (told claims of two origins, a contradiction, a covert deed, a held document) is planted on the same investigator, and the
    same readings are made again, so each could have failed."""
    r = S.run("inquiry", 0, 1)
    w, p = r["world"], r["world"].persons[r["seat"]]
    goal = S.inquiry_goal().object

    def read():
        rows = [x["row"] for x in board(p, w.fixtures) if x["kind"] == "claim"]
        assert sorted(id(x.claim) for x in rows) == sorted(id(c) for c in p.ledger), "a claim in no row, or in two"
        keys = [(x.claim.subject, x.claim.predicate, x.claim.value) for x in rows]
        runs = sum(1 for i, k in enumerate(keys) if i == 0 or k != keys[i - 1])
        assert runs == sum(1 for i, k in enumerate(keys) if k not in keys[:i]), "a group's rows are not together"
        tick, decay = fade_of(p)
        weigh = ledger_weigh(p, w.fixtures, tick)
        for x in rows:
            same = [c for c in p.ledger if (c.subject, c.predicate, c.value) == (x.claim.subject, x.claim.predicate, x.claim.value)]
            assert x.support == LedgerReader(p.ledger, weigh, tick=tick, decay=decay)._support(same)[0], x.claim
        suspects = [x for x in board(p, w.fixtures) if x["kind"] == "suspects"]
        assert [x["doers"] for x in suspects] == [deed_doers(p.ledger, goal, p.id)]
        return rows, suspects[0]["doers"]

    assert len(p.ledger) == len({c.id for c in p.ledger}) > 0, "the investigator held nothing: the board proves nothing"
    _, before = read()
    held_before = [x for x in board(p, w.fixtures) if x["kind"] == "document"]
    me, a, b = p.id, "p_holder", "p_witness"
    told = lambda cid, origin, value: Claim(cid, me, "p_forger", "stores:grain", value, w.tick, "told_by", 60, "own", chain=(origin,))
    p.ledger += [told("c_t1", a, 7), told("c_t2", b, 7), told("c_t3", a, 7), told("c_t4", b, 9),
                 Claim("c_deed", me, "p_bench_a", "site.damaged", True, w.tick, "firsthand", 90, "own"),
                 Claim("c_doc", me, "rec_doc", "content:dispensation", (("terms", "t"), ("to", (me,)), ("at", None)), w.tick, "firsthand", 90, "own")]
    w.add_tenure(Tenure("t_doc", me, "rec_doc", "hold", since=w.tick))
    rows, doers = read()
    assert "p_bench_a" in doers and "p_bench_a" not in before, "the planted covert deed names nobody"
    by_id = {x.claim.id: x for x in rows}
    weigh = ledger_weigh(p, w.fixtures, fade_of(p)[0])
    one, two = (weigh(c) for c in (by_id["c_t1"].claim, by_id["c_t2"].claim))
    assert by_id["c_t1"].support == by_id["c_t2"].support == by_id["c_t3"].support == 1.0 - (1.0 - one) * (1.0 - two) > max(one, two), "two origins do not stand higher than one"
    assert by_id["c_t4"].support == 1.0 - (1.0 - weigh(by_id["c_t4"].claim)) and set(by_id["c_t1"].against) == {"c_t4"} and set(by_id["c_t4"].against) == {"c_t1", "c_t2", "c_t3"}
    assert by_id["c_t1"].proof_kind == "" and by_id["c_deed"].proof_kind == "testimony" and by_id["c_deed"].against == ()      # B24.44: `person_q.proof_kind` -- a cell is no proof
    assert by_id["c_doc"].proof_kind == "record"                                                                                # a held Record's, `RECORD_MATTER` or `record`
    docs = [x for x in board(p, w.fixtures) if x["kind"] == "document"]
    assert [x.claim.id for x in rows if x.record][-1:] == ["c_doc"] and by_id["c_doc"].record == "rec_doc" and len(docs) == len(held_before) + 1
    assert docs[-1] == {"kind": "document", "id": "rec_doc", "of": "dispensation", "about": {"terms": "t", "to": (me,), "at": None}}
    assert docs[:-1] == held_before, "a document he held before the plant moved"
