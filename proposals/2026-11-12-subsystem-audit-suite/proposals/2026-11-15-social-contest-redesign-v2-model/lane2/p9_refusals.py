"""P9: refusal and error paths.  PYTHONHASHSEED=0 python lane2/p9_refusals.py"""
from dataclasses import replace
from common import *
from scmodel.records import Choice
D = dials.shipped()
def t(label, fn):
    try:
        r = fn(); print(f"  {label}: returned {r}")
    except Exception as e:
        print(f"  {label}: {type(e).__name__}: {str(e)[:110]}")
P = people()
q = build_input(P, "questioning", "full", actor="a", addressed="b", effort=3, dials=D)
t("respondent press under questioned", lambda: proceed(q, draw(0), lambda v: Choice("press", "evidence") if v.mover == "b" else Choice("argue", "evidence")).ended)
t("abridged rest", lambda: build_input(P, "conversation", "abridged", "rest", actor="a", addressed="b", dials=D))
def ab(mv):
    i = build_input(P, "conversation", "abridged", mv, actor="a", addressed="b", dials=D)
    o = proceed(i, draw(0)); m, _ = act_margin(o, i.type, i); return (o.exchanges[0].move, round(m.net - m.ob, 3), degree(m))
t("abridged press (accepted?)", lambda: ab("press"))
t("abridged divert (accepted?)", lambda: ab("divert"))
i = build_input(P, "conversation", "abridged", actor="a", addressed="b", dials=D)
o = proceed(i, draw(0))
def resumed():
    o2 = proceed(replace(i, state=o.state), draw(1)); return (len(o2.exchanges), o2.verdicts, act_margin(o2, i.type, i))
t("abridged resumed at n=1 (verdict typing)", resumed)
t("effort -1 under abridged", lambda: (lambda o: (len(o.exchanges), o.ended, o.verdicts))(proceed(build_input(P, "conversation", "abridged", actor="a", addressed="b", effort=-1, dials=D), draw(0))))
t("effort -1 full legal_trial", lambda: (lambda o: (len(o.exchanges), o.ended, len(o.verdicts)))(proceed(build_input(P, "legal_trial", "full", actor="a", addressed="b", bench=("pol0",), effort=-1, dials=D), draw(0))))
P2 = people(); P2["a"]["operands"] = [("rank_gap", -1.0, 0.5, "reason")]
t("negative operand raw", lambda: proceed(build_input(P2, "conversation", "full", actor="a", addressed="b", dials=D), draw(0)).ended)
P3 = people(); P3["a"]["attributes"] = {k: 0 for k in ATTRS}; P3["b"]["attributes"] = {k: 12 for k in ATTRS}
t("attributes 0 vs 12 (outside 1..7)", lambda: proceed(build_input(P3, "legal_trial", "full", actor="a", addressed="b", bench=("pol0",), dials=D), draw(0)).ended)
P4 = people(); P4["a"]["attributes"] = {k: -1 for k in ATTRS}
t("attributes -1", lambda: proceed(build_input(P4, "conversation", "full", actor="a", addressed="b", dials=D), draw(0)).ended)
P5 = people(); P5["cohort"]["weight"] = 0
t("hearer cohort weight 0", lambda: (lambda i: act_margin(proceed(i, draw(0)), i.type, i))(build_input(P5, "rally", "full", actor="a", addressed="cohort", dials=D)))
t("difficulty_level 'impossible'", lambda: build_input(P, "conversation", "full", actor="a", addressed="b", dials=D, difficulty_level="impossible"))
t("order 'single' (RD:194)", lambda: proceed(build_input(P, "rally", "full", actor="a", addressed="cohort", dials=D, order="single"), draw(0)).ended)
t("order 'written_only' on a two-speaker contest row", lambda: proceed(build_input(P, "legal_trial", "full", actor="a", addressed="b", bench=("pol0",), dials=D, order="written_only"), draw(0)).ended)
t("declared, 1 seat < quorum 2 (admitted?)", lambda: build_input(P, "excommunication_deliberation", "full", actor="a", addressed="b", bench=("ch0",), dials=D).type.quorum)
t("bench of a weight-30 cohort seat (legal_trial)", lambda: [ (d.id, d.weight, d.pool) for d in build_input(P, "legal_trial", "full", actor="a", addressed="b", bench=("seatcohort",), dials=D).deciders])
