"""W-D — collect the chunks, run the controls, run the forensics, emit the artifact.

The chunks are `wd_chunk.py`'s output: `wd_acceptance.sweep_arm` over a SLICE of the same case
list, same seed, same fixtures. Concatenating them is arithmetic, not a second measurement — and
the collector CHECKS the reconstruction rather than assuming it: every arm must cover all
`len(CASES)` cases exactly once, and each arm's chunks must partition ITS OWN `probed` into
`no_live_window` + `inert` + `genuine` + `fork_rows_failed`. `probed`/`no_live_window` are NOT
asserted equal ACROSS arms (re-based 2026-09-30, WD-REBASE): since U2/R-03 a season is rounds, and
a deposit in one round can raise a question a later round would not otherwise have, so the three
deposit-mode arms are no longer the same experiment at the deliberation-count level, only at the
case-coverage level.
"""
from __future__ import annotations
import collections, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "engine" / "reference" / "degree-sweep"))  # sweep_core/arm9_* moved (ED-IN-0231 precedent)
import wd_acceptance as W
from sweep_core import Log
from wd_acceptance import ARMS, CASES, SEED, SEASONS, OUT, forensics, positive_control, comparator_control, PLANT_WHY
from engine.season.trace_log import TRACE

SUM = ("probed", "no_live_window", "inert", "genuine", "reconverged", "diverged",
       "acts_differ", "hash_differ", "stream_only", "window_slots_checked",
       "window_slots_same_tick", "n_cases_attempted", "n_cases_ok", "n_cases_failed",
       "fork_rows_failed")


def collect(slots: str, mode: str) -> dict:
    files = sorted(OUT.glob(f"wd_chunk_{slots}_{mode}_*.json"),
                   key=lambda p: int(p.stem.split("_")[-2]))
    parts = [json.load(open(f)) for f in files]
    assert parts, f"no chunks on disk for {slots}/{mode}; run `wd_chunk.py {mode} {slots} <a> <b>`"
    covered = []
    for p in parts:
        covered.extend(range(p["chunk"][0], p["chunk"][1]))
    out = dict(mode=mode, slots=slots, chunks=[p["chunk"] for p in parts],
               covers=sorted(covered), seconds=round(sum(p["seconds"] for p in parts), 1))
    for k in SUM:
        out[k] = sum(p[k] for p in parts)
    out["reconvergence_rate"] = (out["reconverged"] / out["genuine"]) if out["genuine"] else None
    out["divergences"] = [d for p in parts for d in p["divergences"]]
    cd = collections.Counter()
    for p in parts:
        for k, v in p["changed_distribution"].items():
            cd[int(k)] += v
    out["changed_distribution"] = dict(sorted(cd.items()))
    out["failures"] = [f for p in parts for f in p["failures"]]
    return out


def main() -> int:
    log = Log()
    out = {"seed": SEED, "seasons": SEASONS, "n_cases": len(CASES),
           "basis": f"{len(CASES)} (apply_rescale applied, as `A9.run` and `sweep.runnable` do)"}
    log.rule("W-D — THE ACCEPTANCE RUN: did `W-B` change the forking result?")
    log("INSTRUMENT", "`arm9_forking.fork_case`, imported UNMODIFIED. `wd_acceptance.sweep_arm` "
                      "loops it over (deposit mode x fixture point); `wd_chunk.py` splits the "
                      "corpus into four slices per arm because two full-corpus processes were "
                      "killed at ~18 minutes with no traceback; this file concatenates them.")
    from sweep_core import S
    log("BASIS", f"{len(CASES)} cases = {sum(1 for l,_ in CASES if l=='NPC')} NPC + "
                 f"{sum(1 for l,_ in CASES if l=='ARC')} ARC, `apply_rescale` APPLIED — THE "
                 f"{len(CASES)} BASIS.")
    log("SEED", f"{SEED}; seasons {SEASONS} — `runs/arm9.json`'s own published configuration")
    log("CONTEST", "confound 2, CHECKED NOT ASSUMED: `A9._run` does not pass `contest_max_depth`, "
                   "and does not need to. The only contesting verb is "
                   f"{sorted(v for v,r in S.VERB_TABLE.items() if getattr(r,'contests',''))}; "
                   f"`resolvable_verbs()` — the verb set `A9._run` hands `make_chooser` — "
                   f"excludes it (intersection "
                   f"{sorted(set(v for v,r in S.VERB_TABLE.items() if getattr(r,'contests','')) & set(S.resolvable_verbs()))}"
                   "), so `resolve()`'s `Forbidden` branch is unreachable and the probe is left "
                   "unedited. `n_cases_failed` below is the empirical check.")

    log.rule("W-D.0 — WHICH CELLS OF THE DECLARED SWEEP CROSS CAN THE QUESTION BE ASKED AT?")
    log("⚠ CORRECTION", "THE FIRST WRITING OF THIS ITEM SAID `exactly ONE cell gives L <= 3` AND "
                        "THAT IS FALSE. TWO of the nine cells qualify, and the one that was NOT "
                        "run is the SMALLER intervention. Found by an independent read-only "
                        "critic, 2026-09-04; re-measured over the corpus by `wd_cells.py`.",
        "`L` is THE PACKER'S OWN TAKE — `sum(len(sc.acts) for sc in pack_scenes(...))`, read off "
        "`recorder.in_budget` — and NOT the slot product `scene_budget x interactions_per_scene`. "
        "The product was used as a proxy for it. `take()` charges an EXTENDED scene "
        "`extended_scene_cost`=2 and takes a whole chunk whenever `ext <= left`, so at 2 x 3 the "
        "first chunk of three candidates is taken entire for a cost of 2 and L = 3, not 6. And L "
        "is PER DELIBERATION, not per cell: it varies with the person's own ranked list, so "
        "`L <= 3` is a property of a deliberation and a cell is askable when ANY of its "
        "deliberations has one.")

    for slots, title in (("default", "W-D.1 — THE SHIPPED FIXTURE POINT (5 x 3 = 15 slots)"),
                         ("narrow", "W-D.2 — THE ACCEPTANCE FIXTURE POINT (2 x 1 = 2 slots): "
                                    "scene_budget=2 (`H-10` arm) x interactions_per_scene=1 "
                                    "(`H-76` arm) — TWO declared-arm changes"),
                         ("2x3", "W-D.2b — THE SECOND QUALIFYING CELL (2 x 3 = 6 slots): "
                                 "scene_budget=2 (`H-10` arm) x interactions_per_scene LEFT AT "
                                 "ITS DEFAULT — ONE declared-arm change, so by the item's own "
                                 "minimum-departure criterion this is the BETTER acceptance "
                                 "point, and it was never run until the adversarial pass")):
        log.rule(title)
        if slots == "2x3":
            log("⚠ WINDOW", "the live window scores only strictly-LATER-TICK decisions "
                            "(`arm9_forking.py:201`); since U2 a tick is a season of R rounds, "
                            "each freezing and thawing (`driver.py:352-355`); so "
                            "round-to-round divergence INSIDE a season is NOT SCORED, and every "
                            "reconvergence rate printed below is an UPPER BOUND on that "
                            "channel. The probe is not edited.")
        out[slots] = {}
        for mode in ARMS:
            r = collect(slots, mode)
            out[slots][mode] = r
            rate = ("n/a — EMPTY DENOMINATOR" if r["reconvergence_rate"] is None
                    else f"{r['reconvergence_rate']*100:.2f}%")
            log("MEASURE", f"mode={mode:5} | cases {r['n_cases_ok']}/{r['n_cases_attempted']} ok, "
                           f"{r['n_cases_failed']} failed, {r['fork_rows_failed']} fork rows failed"
                           f" | probed {r['probed']} = NO-LIVE-WINDOW {r['no_live_window']} + "
                           f"INERT-BY-CONSTRUCTION {r['inert']} + GENUINE {r['genuine']} | "
                           f"RECONVERGED {r['reconverged']}/{r['genuine']} = {rate} · "
                           f"DIVERGED {r['diverged']}  [{r['seconds']}s]")
            log("  WINDOW", f"strictly-later-tick: {r['window_slots_checked']} slots inspected, "
                            f"{r['window_slots_same_tick']} at the fork's own tick or earlier "
                            f"(confound 1; must be 0)")
            log("  STREAM", f"acts differ {r['acts_differ']}/{r['genuine']} · event-log hash "
                            f"differs {r['hash_differ']}/{r['genuine']} · CHANGED THE STREAM AND "
                            f"NOT A DECISION {r['stream_only']} (the pre-`W-B` condition)")
            log("  CHANGED", f"decisions changed within the lookahead: {r['changed_distribution']}")
        # ⚠ THE ARMS ARE NOT THE SAME EXPERIMENT ANY MORE, AND A ROUNDS-LOOP DEPOSIT IS THE
        # PLAUSIBLE MECHANISM, NOT A CHECKED ONE -- NEITHER IS THIS A RECONSTRUCTION DEFECT.
        # Since U2/R-03 (`engine/season/loop/driver.py:331-371`), a season is R rounds rather
        # than one pass, and a deposit landed in round r can raise a Q2 question in round r+1
        # (`claim_landed`, `engine/season/queries/world_q.py:1346-1356`) that the next round's
        # `opening_set` did not have before -- and whether that deposit lands at all depends on
        # `observation_deposit_mode`. That is ONE candidate reason `probed`/`no_live_window` no
        # longer match across arms. It is not the only one on the record, and nothing in THIS
        # file isolates which contributes what: `engine/season/tests/test_season_shape.py`
        # documents at least two more live channels that differ by arm in every season, not only
        # the rounds loop -- U4's sampler keyed on `(verb, subject)` (`:11501-11508`), Q4's person
        # referent added 2026-09-13 (`:11525-11537`, `:11554-11566`), and position `11a`'s
        # widening of Q2 `claim_landed` through `reach`/`place_of` (`:11538-11547`,
        # `:11581-11591`, which reports `none` 10/36 against `actor` 10/33 at NPC-088 -- the arms
        # AT PARITY, not the rounds loop dominating). `:11565` says outright that these figures
        # are "a JOINT measurement of clause 4 and the Q4 referent". So: `probed`/`no_live_window`
        # are NOT asserted equal across arms (below), and per-arm denominators are printed rather
        # than assumed -- but do not read this comment as claiming the rounds loop alone did it.
        p = {m: out[slots][m]["probed"] for m in ARMS}
        nl = {m: out[slots][m]["no_live_window"] for m in ARMS}
        cov = {m: out[slots][m]["covers"] == list(range(len(CASES))) for m in ARMS}
        log("SAME-EXPT", f"per-arm PROBED (own denominator, NOT asserted equal across arms -- "
                         f"several live channels differ by arm, the rounds loop among them and "
                         f"not isolated from the others here; see the comment above): {p} · "
                         f"per-arm NO-LIVE-WINDOW (likewise per-arm): {nl} · each arm covers all "
                         f"{len(CASES)} case slots exactly once: {cov}")
        assert all(cov.values()), (
            f"{slots}: an arm does not cover all {len(CASES)} case slots exactly once: {cov}. A "
            "chunk was dropped or run twice, so the concatenation is not the corpus")
        # CONFOUND 1 at corpus scale, likewise asserted rather than printed.
        for m in ARMS:
            r = out[slots][m]
            # §0.1 pt 2 -- able to observe the failure it excludes. The old cross-arm EQUALITY
            # asserts are retired (they are false by construction once a round-to-round deposit
            # moves the question count); what must still hold, per arm, is that the chunks
            # PARTITION their own denominator. MEASURED: holds in all nine cell x arm sums of the
            # committed chunks; raised by the `W-D` adversarial pass, 2026-09-04, re-based for the
            # rounds loop and the 143 basis, 2026-09-30 (WD-REBASE).
            assert r["probed"] == (r["no_live_window"] + r["inert"] + r["genuine"]
                                    + r["fork_rows_failed"]), (
                f"{slots}/{m}: probed {r['probed']} != no_live_window {r['no_live_window']} + "
                f"inert {r['inert']} + genuine {r['genuine']} + fork_rows_failed "
                f"{r['fork_rows_failed']}. The chunks do not partition their own denominator")
            assert r["window_slots_same_tick"] == 0, (
                f"{slots}/{m}: {r['window_slots_same_tick']} of {r['window_slots_checked']} "
                "scored window slots sit at the fork's own tick or earlier. DELIBERATE is a "
                "parallel map over a frozen world, so those slots cannot differ and counting "
                "them inflates reconvergence")
            assert r["n_cases_failed"] == 0 and r["fork_rows_failed"] == 0, (
                f"{slots}/{m}: {r['n_cases_failed']} cases and {r['fork_rows_failed']} fork rows "
                "failed; the rates are over a silently smaller population than the log says")
            # §0.1 pt 2 -- ASSERT THAT IT ASSERTED. A window check over zero windows is absent.
            if r["genuine"]:
                assert r["window_slots_checked"] > 0, (
                    f"{slots}/{m}: {r['genuine']} genuine forks and ZERO window slots inspected — "
                    "the strictly-later-tick check has nothing to be true of")

    log.rule("W-D.3 — CONTROLS, AT BOTH QUALIFYING CELLS")
    sample = CASES[:3]
    for slots, label in (("narrow", "2 x 1 = 2 slots"), ("2x3", "2 x 3 = 6 slots")):
        n = out[slots]["none"]
        a = out[slots]["actor"]
        t = out[slots]["total"]
        # ⚠ `none` IS NOT A NULL ARM ANY MORE. Something OTHER than `W-B` now moves it too --
        # at least the rounds loop, U4's sampler, Q4's person referent and position `11a`'s Q2
        # widening are all live in every arm including `none` (cited above, at the SAME-EXPT
        # comment; none isolated here). So "diverged == 0 at none" is no longer the control;
        # U6's own control is, verbatim from its content owner: "`observation_deposit_mode=none`
        # arm ≥ the default arm — that is the only control this instrument produces"
        # (the retired `workplans/2026-09-09-r-execution-plan.md:1472-1473`; read it with `git show 0671283:workplans/2026-09-09-r-execution-plan.md`).
        # The default arm is `actor` (`engine/season/data/fixtures.py:448`).
        assert n["genuine"] > 0, (
            f"{slots}: the control arm `none` has an EMPTY denominator ({n['genuine']} genuine); "
            "there is nothing for the control to be true of")
        # ⚠ `a`/`t` GUARDED TOO, NOT JUST `n` (methodology-close Phase 1, 2026-09-30). `collect()`
        # returns `reconvergence_rate=None` whenever `genuine == 0`; without this, an empty
        # `actor`/`total` denominator would raise `TypeError` at the `>=` below or at the CONTROL
        # log's unconditional `*100` formatting, instead of the named `AssertionError` this block
        # is built to produce (§0.1 pt 2). Not live against the committed 143-case chunks --
        # `actor` genuine is nonzero at every cell today -- closing a gap the plan's own A.3
        # inherited (it guarded only `n`).
        assert a["genuine"] > 0, (
            f"{slots}: the default arm `actor` has an EMPTY denominator ({a['genuine']} genuine); "
            "`none >= actor` is undefined over an empty denominator")
        assert t["genuine"] > 0, (
            f"{slots}: `total` has an EMPTY denominator ({t['genuine']} genuine); the CONTROL log "
            "line below formats its rate unconditionally")
        assert n["reconvergence_rate"] >= a["reconvergence_rate"], (
            f"{slots}: control `none` reconvergence {n['reconvergence_rate']} is BELOW the "
            f"default `actor` arm's {a['reconvergence_rate']}. U6's own control: "
            "\"`observation_deposit_mode=none` arm ≥ the default arm — that is the only control "
            "this instrument produces\"")
        log("CONTROL", f"[{label}] `none` (a channel-open arm now, NOT a null arm): "
                       f"{n['reconverged']}/{n['genuine']} reconverged = "
                       f"{n['reconvergence_rate']*100:.2f}% · default `actor`: "
                       f"{a['reconverged']}/{a['genuine']} = {a['reconvergence_rate']*100:.2f}% "
                       f"(none >= actor: "
                       f"{n['reconvergence_rate'] >= a['reconvergence_rate']}) · `total`, "
                       f"UNASSERTED (U6 names only the default arm): "
                       f"{t['reconverged']}/{t['genuine']} = {t['reconvergence_rate']*100:.2f}%",
            "U6's own control, verbatim: \"`observation_deposit_mode=none` arm ≥ the default arm "
            "— that is the only control this instrument produces\". Something other than `W-B` "
            "DOES move `none` now -- the rounds loop among several live channels, not isolated "
            "from the others here -- so the old 100%-reconvergence-at-`none` premise is RETIRED "
            "here, not upheld.")

        # POSITIVE / COMPARATOR CONTROLS -- a planted divergence counts as detected only if it
        # EXCEEDS the unplanted `none` arm on the SAME sample; `diverged > 0` alone no longer
        # detects anything once `none` itself diverges through the rounds-loop channel.
        TRACE.rows.clear()  # precedent: `wd_cells.py:64-74` -- nothing reads `TRACE.rows` mid-run
        base = W.sweep_arm("none", slots, cases=sample)
        base = dict(genuine=base["genuine"], diverged=base["diverged"],
                    reconverged=base["reconverged"])
        out[f"control_baseline_{slots}"] = base
        vacuous_note = ("legacy `detected`/`detected_all` fields below ARE vacuous: the unplanted "
                        f"baseline itself diverges ({base['diverged']} of {base['genuine']})"
                        if base["diverged"] > 0 else
                        "legacy `detected`/`detected_all` fields below are NOT vacuous here: the "
                        "unplanted baseline is clean")
        log("BASELINE", f"[{label}] unplanted `none` on the SAME {len(sample)}-case sample: "
                       f"{base['diverged']} DIVERGED of {base['genuine']} genuine "
                       f"(reconverged {base['reconverged']}) — the bar a plant must clear",
            vacuous_note)

        TRACE.rows.clear()
        pc = positive_control(sample, slots=slots)
        out[f"positive_control_{slots}"] = pc
        for o in pc["plants"]:
            o["detected_over_base"] = o["diverged"] > base["diverged"]
        log("POSITIVE", f"[{label}] planted widened clause 4, at the CONTROL arm `none`, cases "
                        f"{pc['cases']} — detected OVER THE BASELINE on ALL "
                        f"{len(pc['plants'])} plants: "
                        f"{all(o['detected_over_base'] for o in pc['plants'])} "
                        f"(legacy `detected_all` {pc['detected_all']}; `fires` below is how often "
                        "each plant's own clause changed a verdict -- 0 would mean the plant is "
                        "inert, whatever `detected_over_base` reads)", PLANT_WHY)
        for o in pc["plants"]:
            log("  PLANT", f"predicate {o['predicate']:16} fires {o['fires']:6} genuine "
                           f"{o['genuine']:3}  DIVERGED {o['diverged']:3}  detected_over_base "
                           f"{o['detected_over_base']}  (legacy detected {o['detected']})")
        if any(o["fires"] == 0 for o in pc["plants"]):
            # ⚠ A PLANT THAT NEVER FIRES TESTS NOTHING (the original `act.refused` failure, and
            # the 2026-09-30 `via`/`weigh` signature mis-bind that left every plant at 0). Reported
            # here as a MEASURED per-plant condition, not a standing assertion.
            log("⚠ PLANT INERT", f"[{label}] at least one plant's own clause never changed a "
                                 f"verdict: {[o['predicate'] for o in pc['plants'] if o['fires'] == 0]}"
                                 " -- its `detected_over_base` is a false negative, not a "
                                 "measurement.")
        TRACE.rows.clear()
        cc = comparator_control(sample, slots=slots)
        cc["detected_over_base"] = cc["diverged"] > base["diverged"]
        out[f"comparator_control_{slots}"] = cc
        log("POSITIVE-2", f"[{label}] comparator-only plant (a token spliced into one later "
                          f"ranked list): {cc['perturbations_applied']} fork streams perturbed, "
                          f"genuine {cc['genuine']}, DIVERGED {cc['diverged']} -> "
                          f"detected_over_base {cc['detected_over_base']} (legacy detected "
                          f"{cc['detected']}; every genuine fork DIVERGED, the reading a working "
                          f"comparator owes: {cc['detected_all_genuine']})")
        if not cc["detected_over_base"]:
            # ⚠ DIAGNOSED BY EXECUTION 2026-10-01 (it was a null at both cells on 2026-09-30, and
            # the first writing of this branch called its cause undiagnosed): the old plant rewrote
            # the run's LAST decision, which `A9.fork_case`'s strictly-later-tick window cannot
            # contain while the final tick holds more than `LOOKAHEAD` (3) deliberations (4-6 at the
            # control sample; 0 forks held it). `wd_acceptance.comparator_control` now rewrites the
            # first later-tick decision, `live_window[0]`. Reaching this branch AGAIN therefore
            # means the comparator itself did not register a perturbation inside its own window.
            log("⚠ COMPARATOR NULL", f"[{label}] the comparator control did not detect over "
                                      "baseline: a perturbation of `live_window[0]` in every "
                                      "genuine fork's own decision stream did not raise DIVERGED "
                                      "above the unplanted baseline. `detected_over_base` here is "
                                      "NOT evidence this control can see a change.")
    # kept under their historical keys so a reader of the committed artifact still finds them
    out["positive_control"] = out["positive_control_narrow"]
    out["comparator_control"] = out["comparator_control_narrow"]

    log.rule("W-D.4 — PER-FORK FORENSICS on every divergence, AT THE 2 x 1 CELL")
    log("SCOPE", "The forensics below are the 2 x 1 cell's. The 2 x 3 cell's divergences are "
                 "reported in W-D.2b and are NOT dissected here — stated rather than left to "
                 "look like an absence of divergences (§0.1 pt 4 cuts both ways).")
    out["forensics"] = {}
    by_case = {c["id"]: c for _, c in CASES}
    for mode in ("actor", "total"):
        divs = out["narrow"][mode]["divergences"]
        sig = collections.Counter((d["from_verb"], d["to_verb"], tuple(d["changed_at"]))
                                  for d in divs)
        log("COUNT", f"mode={mode}: {len(divs)} divergent forks of "
                     f"{out['narrow'][mode]['genuine']} genuine")
        log("SIGNATURES", f"  (from_verb -> to_verb, which of the next 3 changed) x count: "
                          f"{dict(sig)}")
        seen, reps = set(), []
        for d in divs:
            k = (d["from_verb"], d["to_verb"], tuple(d["changed_at"]), d["person"], d["lane"])
            if k in seen:
                continue
            seen.add(k); reps.append(d)
        det, selfref, nonself, false_rec, broken = [], 0, 0, 0, 0
        for d in reps[:24]:
            fr = forensics(by_case[d["case"]], mode, "narrow", d["at"], d["take"], d["in_budget"])
            fr["fork"] = d
            det.append(fr)
            if not (fr["base_ok"] and fr["fork_ok"]):
                broken += 1
                continue
            for side, ds in (("fork-only", fr["drops_only_in_fork"]),
                             ("base-only", fr["drops_only_in_base"])):
                for x in ds:
                    c = x.get("carrier") or {}
                    ops = x.get("operands") or {}
                    sr = any(v == x["subject"] for k2, v in ops.items() if k2 != "subject")
                    selfref += bool(sr); nonself += (not sr)
                    if x.get("true_when_recorded") is False:
                        false_rec += 1
                    prov = x.get("provenance") or {}
                    log("  DROP", f"{fr['case']} fork(at={d['at']},take={d['take']}) "
                                  f"{d['from_verb']}->{d['to_verb']} @tick {d['tick']} | clause-4 "
                                  f"drop present ONLY IN {side}: {x['pid']} declines "
                                  f"`{x['verb']}` on {x['subject']!r}, ops={ops} — "
                                  f"SELF-REFERENTIAL={sr}")
                    log("  CLAIM", f"    carrier ({c.get('subject')!r}, {c.get('predicate')!r}, "
                                   f"{c.get('value')!r}) when={c.get('when')} "
                                   f"conf={c.get('confidence')} src={c.get('source')} | deposited "
                                   f"by Event {prov.get('by_event')} kind={prov.get('by_kind')} "
                                   f"actor={prov.get('by_subject')} | holder={x['pid']} "
                                   f"CROSS-PERSON={prov.get('by_subject') != x['pid']} | "
                                   f"TRUE WHEN RECORDED = {x.get('true_when_recorded')} "
                                   f"(world at deposit {x.get('world_at_deposit')!r}; world now "
                                   f"{x.get('world_now')!r})")
        out["forensics"][mode] = det
        if broken:
            # `A9._run`'s own `except BaseException` (`arm9_forking.py:148-149`) swallows ANY raise
            # into `ok=False` with no traceback surfaced, so `base_ok`/`fork_ok` False means the
            # spy run raised, not that it found nothing. Until 2026-10-01 that was ALWAYS the spy's
            # 4-positional `belief_contradicts` closure meeting `opening_set`'s five-plus-`weigh=`
            # call (`TypeError`; 24 of 24 representatives at both modes); `wd_acceptance._instrumented`
            # now forwards the signature. A nonzero count here is a NEW failure -- read the swallowed
            # exception by calling `A9._run` on that case directly.
            log("⚠ FORENSICS BROKEN", f"  mode={mode}: {broken} of {len(det)} representatives "
                                      "came back `base_ok`/`fork_ok` False (an exception inside "
                                      "the spy run, swallowed by `A9._run`) and were SKIPPED, not "
                                      "counted as zero-drop evidence.")
        log("SAMPLED", f"  forensics attempted on {len(det)} representatives of {len(divs)} "
                       f"divergences ({len(seen)} distinct signatures; {len(det) - broken} "
                       f"usable, {broken} broken -- see ⚠ FORENSICS BROKEN above if nonzero); "
                       f"every distinct signature is covered when that count is <= 24")
        log("SHAPE", f"  carrying clause-4 drops seen: {selfref} SELF-REFERENTIAL "
                     f"(operand == subject, the degenerate class the operand channel produces), "
                     f"{nonself} not")
        ig = sum(f["in_grammar_base"] + f["in_grammar_fork"] for f in det)
        fw = sum(f["false_when_recorded_base"] + f["false_when_recorded_fork"] for f in det)
        log("TRUTH", f"  carrying beliefs FALSE WHEN RECORDED: {false_rec} of "
                     f"{selfref + nonself}. Over ALL in-grammar deposits in those runs: {fw} of "
                     f"{ig} disagreed with `WorldReader` at the barrier that stored them",
            "`W-B`'s retraction was that a self-refuting belief produced 95% of its published "
            "effect, so a divergence driven by a belief that was false at deposit is a DEFECT and "
            "not a result. This is that check, generalized over every predicate the reader has a "
            "branch for.")

    # ---------------------------------------------------------------------------------------
    log.rule("W-D.5 — IS THE DECISION FINGERPRINT WIDE ENOUGH? (it is not, and this is the "
             "largest finding in the item)")
    log("READ", "`arm9_forking.recorder` records a deliberation as `(person, [verb, ...], tick)` "
                "— VERBS ONLY. `Query.opening_set` returns `Candidate(verb, subject, why, "
                "operands)`, so two candidate lists with the SAME VERBS about DIFFERENT SUBJECTS "
                "compare EQUAL and the fork is scored RECONVERGED.")
    def collect_subj(slots: str, mode: str) -> dict:
        pat = (f"wd_subj_{mode}_*.json" if slots == "narrow"
               else f"wd_subj_{slots}_{mode}_*.json")
        files = sorted(OUT.glob(pat), key=lambda q: int(q.stem.split("_")[-2]))
        parts = [json.load(open(f)) for f in files]
        if not parts:
            return {}
        # ⚠ A STALE BASIS READS CLEAN AND IS NOT THE SAME AS 100%. These chunks may be slices of
        # an OLDER, SMALLER case list (the `wd_subj_*` files are the 89-case slices committed
        # 2026-09-11; the corpus is 143 since `20-ii`) -- computed the same way `collect` does at
        # `:34-36` -- and the caller must not silently compare them against the current basis.
        covered = []
        for pt in parts:
            covered.extend(range(pt["chunk"][0], pt["chunk"][1]))
        # `!=` rather than a length check ALONE -- catches both a short basis (missing slots) and
        # a mismatched one. It does not separately name an OVERLAPPING/duplicated chunk as a
        # distinct case (both read as "covers != range(len(CASES))"), so the `covers` count in the
        # message may read as fewer THAN, EQUAL TO, or coincidentally cover the same slot twice;
        # either way this still REFUSES to compare rather than guessing, which is what matters.
        if sorted(covered) != list(range(len(CASES))):
            return {"stale_basis": True, "covers": len(set(covered)), "of": len(CASES)}
        k = collections.Counter()
        for pt in parts:
            for kk, vv in pt["changed_slot_kinds"].items():
                k[kk] += vv
        r = dict(
            genuine=sum(pt["genuine"] for pt in parts),
            diverged=sum(pt["diverged"] for pt in parts),
            reconverged=sum(pt["reconverged"] for pt in parts),
            n_cases_ok=sum(pt["n_cases_ok"] for pt in parts),
            n_cases_failed=sum(pt["n_cases_failed"] for pt in parts),
            probed=sum(pt["probed"] for pt in parts),
            no_live_window=sum(pt["no_live_window"] for pt in parts),
            inert=sum(pt["inert"] for pt in parts),
            changed_slot_kinds=dict(k))
        r["reconvergence_rate"] = (r["reconverged"] / r["genuine"]) if r["genuine"] else None
        return r

    out["widened_fingerprint"] = {}
    any_widened_ran = False
    for slots, label in (("narrow", "2 x 1 = 2 slots"), ("2x3", "2 x 3 = 6 slots")):
        subj = {m: collect_subj(slots, m) for m in ARMS}
        out["widened_fingerprint"][slots] = subj
        stale = {m: v for m, v in subj.items() if v.get("stale_basis")}
        if stale:
            v0 = next(iter(stale.values()))
            log("MEASURE", f"[{label}] NOT RUN — the `wd_subj_*` chunks on disk cover "
                           f"{v0['covers']} of {v0['of']} case slots (a stale basis); "
                           f"unmeasured here, which is not the same as measured at 100%.")
            continue
        if not all(subj.values()):
            log("MEASURE", f"[{label}] NOT RUN — no `wd_subj_*` chunks on disk for this cell. "
                           f"Stated rather than silently omitted: the widened fingerprint is "
                           f"unmeasured here, which is not the same as measured at 100%.")
            continue
        any_widened_ran = True
        for mode in ARMS:
            r, v = subj[mode], out[slots][mode]
            log("MEASURE", f"[{label}] mode={mode:5} | (verb, subject) fingerprint: RECONVERGED "
                           f"{r['reconverged']}/{r['genuine']} = "
                           f"{r['reconvergence_rate']*100:.2f}% · DIVERGED {r['diverged']}   "
                           f"[verb-only, same run: {v['reconverged']}/{v['genuine']} = "
                           f"{v['reconvergence_rate']*100:.2f}%, DIVERGED {v['diverged']}]")
            log("  KINDS", f"changed window slots by kind: {r['changed_slot_kinds']}")
            assert r["genuine"] == v["genuine"], (
                f"{slots}/{mode}: the widened copy scored {r['genuine']} genuine forks and the "
                f"shipped probe {v['genuine']}. The fingerprint must change only WHETHER a fork "
                "diverged, never WHICH forks are genuine — so the two columns are two "
                "instruments, not two resolutions")
        ok = all(subj[m]["changed_slot_kinds"].get("VERB-SET", 0) == out[slots][m]["diverged"]
                 for m in ARMS)
        pairs = {m: (subj[m]["changed_slot_kinds"].get("VERB-SET", 0), out[slots][m]["diverged"])
                 for m in ARMS}
        dist = {m: out[slots][m]["changed_distribution"] for m in ARMS}
        log("CONSISTENCY", f"[{label}] VERB-SET changed slots == the verb-only instrument's "
                           f"DIVERGED count, in every arm: {ok} ({pairs})",
            "⚠ THIS IS A CONSISTENCY CHECK, NOT INDEPENDENT CORROBORATION, AND THE FIRST WRITING "
            "OF IT OVERCLAIMED. It cannot fail while every divergent fork changes EXACTLY ONE "
            f"window slot — `changed_distribution` is {dist} — because then the VERB-SET slot "
            "count is identically the count of verb-differing divergent forks. It would become "
            "informative only if a fork ever changed two verb-differing slots. Raised by an "
            "independent read-only critic, 2026-09-04.")
    log("⚠ CONSEQUENCE", "THE CONTROL IS NOT 100% AT THIS RESOLUTION, AND THAT RETRACTS THE "
                          "DIAGNOSIS THE PUBLISHED 100% RESTED ON — not the arithmetic.",
        "ARM 9c reads: *'the deliberation never reads the world ... the only channel by which "
        "anything that happened can reach a later decision is a CLAIM in the actor's ledger'*, "
        "and ARM 9d then shows that channel closed. `opening_set` indeed reads no World — but its "
        "`q` DOES: `questions_for(w, p)` takes a World, and clause 3 is `subject in "
        "referents(q)`.")
    log("⚠ THE CARRIER", "IT IS NOT THE LEDGER'S APPEND ORDER. `questions_for` SORTS, WHICH "
                          "DESTROYS APPEND ORDER: `out.sort(key=lambda q: (order[q.source], "
                          "q.id))`. The first writing of this item named append order and that is "
                          "corrected here. Found by an independent read-only critic, 2026-09-04.",
        "Several `claim_landed` questions SHARE a source, so among them `q.id` alone decides — "
        "and `q.id` is `f'q:claim:{c.id}'` where `c.id` is a CONTENT HASH, "
        "`H(w.world_seed, w.tick, pid, f'claim:{e.id}:{n}')`, minted in `SeasonDriver.witness` "
        "off the DEPOSITING EVENT'S OWN ID. So WHICH QUESTION A PERSON ANSWERS IS DECIDED BY "
        "LEXICOGRAPHIC ORDER OVER CONTENT-HASHED CLAIM IDS. That is an undeclared tiebreaker with "
        "decision consequences, and it sits one level ABOVE `H-54`, whose three arms "
        "(`first`/`all`/`one_per_source`) every one read `qs[0]` or `qs[0].id` and none of which "
        "says what breaks ties WITHIN a source. RE-TRACED with a spy on `questions_for` (NPC-088, "
        "`none`, fork at decision 0, p_a `move` -> `speak`; p_c at tick 1): the baseline's five "
        "`claim_landed` questions come back at LEDGER INDICES [6, 0, 1, 9, 10] and the fork's six "
        "at [12, 5, 0, 1, 8, 9] — neither is append order, both are ascending `q.id`. The fork's "
        "`speak` emits `speech.made` about `r_hearth`; that lands in p_c's ledger at index 12 as "
        "claim `0261dc5bd7431c56`, and `0261...` < `219a...`, so `qs[0]` goes from "
        "`q:claim:219a9f960a5fa368` (referents ('p_c',)) to `q:claim:0261dc5bd7431c56` "
        "(referents ('r_hearth',)) — which is exactly the p_c -> r_hearth subject flip reported, "
        "reached by a different mechanism than the one reported. ⚠ AND THE DEPOSITING EVENT'S "
        "SUBJECT IS `p_a`, NOT `p_c`: the pre-`W-B` channel is CROSS-PERSON at the control arm, "
        "because event-kind claims are minted in every arm and `fan_out_mode` defaulted to "
        "`total` WHEN THIS RAN (it ships `all_five` from 2026-09-07, R7 / ED-IN-0205; this finding "
        "is about the deposit arms and is unaffected). So a fork already changed what a person "
        "deliberates ABOUT before `W-B`, through "
        "Q2 and a content-hash tiebreak nobody declared.")
    if any_widened_ran:
        log("SO THE TWO CHANNELS SEPARATE", "SUBJECT-ONLY changes are the OLD channel and "
                                            "VERB-SET changes are `W-B`'s. They do not overlap "
                                            "in any arm — the per-cell counts are in the KINDS "
                                            "lines above rather than transcribed here, so this "
                                            "sentence cannot go stale against them.")
    else:
        # ⚠ GATED, 2026-09-30 (WD-REBASE): both cells above printed NOT RUN (a stale `wd_subj_*`
        # basis, or no chunks on disk at all) -- there are no KINDS lines this run, and printing
        # the claim above unconditionally, as the pre-rebase file did, asserts a finding this run
        # produced no evidence for. The claim is the LAST TIME `wd_subj_*` chunks were fresh
        # (2026-09-04, on the 89-case basis, `runs/WD_LOG.txt`); it is not re-verified here.
        log("SO THE TWO CHANNELS SEPARATE", "NOT RE-VERIFIED THIS RUN — both cells above are "
                                            "NOT RUN (see the MEASURE/NOT-RUN lines), so there "
                                            "are no fresh KINDS lines for this claim to rest on. "
                                            "The claim stands only as the 2026-09-04 finding on "
                                            "the stale 89-case `wd_subj_*` basis, not as a "
                                            "property re-checked here.")

    (OUT / "WD_LOG.txt").write_text(log.text() + "\n")
    json.dump(out, open(OUT / "wd_acceptance.json", "w"), indent=1, default=str)
    print(log.text())
    print(f"\nwrote {OUT/'WD_LOG.txt'} and {OUT/'wd_acceptance.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
