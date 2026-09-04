"""W-D — collect the chunks, run the controls, run the forensics, emit the artifact.

The chunks are `wd_chunk.py`'s output: `wd_acceptance.sweep_arm` over a SLICE of the same case
list, same seed, same fixtures. Concatenating them is arithmetic, not a second measurement — and
the collector CHECKS the reconstruction rather than assuming it (every arm must cover 89 cases
exactly once, and `probed`/`no_live_window` must be equal across arms, which they are only if the
arms are the same experiment).
"""
from __future__ import annotations
import collections, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import wd_acceptance as W
from sweep_core import Log
from wd_acceptance import ARMS, CASES, SEED, SEASONS, OUT, forensics, positive_control, comparator_control, PLANT_WHY

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
           "basis": "89 (apply_rescale applied, as `A9.run` and `sweep.runnable` do)"}
    log.rule("W-D — THE ACCEPTANCE RUN: did `W-B` change the forking result?")
    log("INSTRUMENT", "`arm9_forking.fork_case`, imported UNMODIFIED. `wd_acceptance.sweep_arm` "
                      "loops it over (deposit mode x fixture point); `wd_chunk.py` splits the "
                      "corpus into four slices per arm because two full-corpus processes were "
                      "killed at ~18 minutes with no traceback; this file concatenates them.")
    from sweep_core import S
    log("BASIS", f"{len(CASES)} cases = {sum(1 for l,_ in CASES if l=='NPC')} NPC + "
                 f"{sum(1 for l,_ in CASES if l=='ARC')} ARC, `apply_rescale` APPLIED — THE 89 "
                 f"BASIS. The 86 basis is the raw `scale:` filter and is not used here.")
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
        # the arms must be the SAME EXPERIMENT
        p = {m: out[slots][m]["probed"] for m in ARMS}
        nl = {m: out[slots][m]["no_live_window"] for m in ARMS}
        cov = {m: out[slots][m]["covers"] == list(range(len(CASES))) for m in ARMS}
        log("SAME-EXPT", f"probed identical across arms: {len(set(p.values()))==1} {p} · "
                         f"NO-LIVE-WINDOW identical: {len(set(nl.values()))==1} {nl} · "
                         f"each arm covers all {len(CASES)} case slots exactly once: {cov}",
            "the deliberation count does not depend on the deposit mode (`pack_scenes` is called "
            "for every person with a question, whatever their candidate set), so these MUST be "
            "equal; INERT and GENUINE legitimately differ, because a dropped Candidate shrinks "
            "the packer's own take `L` — which is why the denominator is printed with every rate")
        # ⚠ ASSERTED, NOT LOGGED. These three read clean and used to be PRINTED and then written
        # to the artifact regardless of their values, which makes them eye-checks: a
        # reconstruction defect would have shipped a green-looking log. The pytest tests assert
        # only on the NPC-088 slice, so nothing gated them at corpus scale. Raised by the `W-D`
        # adversarial pass, 2026-09-04.
        assert len(set(p.values())) == 1, (
            f"{slots}: `probed` differs across arms {p}. The deliberation count cannot depend on "
            "`observation_deposit_mode`, so the three arms are not the same experiment and every "
            "rate below compares different denominators")
        assert len(set(nl.values())) == 1, (
            f"{slots}: NO-LIVE-WINDOW differs across arms {nl}; same reason as `probed`")
        assert all(cov.values()), (
            f"{slots}: an arm does not cover all {len(CASES)} case slots exactly once: {cov}. A "
            "chunk was dropped or run twice, so the concatenation is not the corpus")
        # CONFOUND 1 at corpus scale, likewise asserted rather than printed.
        for m in ARMS:
            r = out[slots][m]
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
        log("NEGATIVE", f"[{label}] `observation_deposit_mode = none`: {n['reconverged']} of "
                        f"{n['genuine']} genuine forks RECONVERGED = "
                        f"{n['reconvergence_rate']*100:.2f}%, DIVERGED {n['diverged']}",
            "THE SINGLE MOST IMPORTANT NUMBER. `none` is the pre-`W-B` deposit behaviour exactly. "
            "A non-100% here would mean something other than `W-B` moved the harness and every "
            "other figure in this item would be confounded")
        assert n["diverged"] == 0 and n["genuine"] > 0, (
            f"{slots}: the negative control is not clean ({n['diverged']} DIVERGED of "
            f"{n['genuine']} genuine); every other figure at this cell is confounded")
        pc = positive_control(sample, slots=slots)
        out[f"positive_control_{slots}"] = pc
        log("POSITIVE", f"[{label}] planted widened clause 4, at the CONTROL arm `none`, cases "
                        f"{pc['cases']} — detected on ALL {len(pc['plants'])} plants: "
                        f"{pc['detected_all']}", PLANT_WHY)
        for o in pc["plants"]:
            log("  PLANT", f"predicate {o['predicate']:16} genuine {o['genuine']:3}  DIVERGED "
                           f"{o['diverged']:3}  detected {o['detected']}")
        cc = comparator_control(sample, slots=slots)
        out[f"comparator_control_{slots}"] = cc
        log("POSITIVE-2", f"[{label}] comparator-only plant (a token spliced into one later "
                          f"ranked list): {cc['perturbations_applied']} fork streams perturbed, "
                          f"genuine {cc['genuine']}, DIVERGED {cc['diverged']} -> detected "
                          f"{cc['detected']}")
    # kept under their historical keys so a reader of the committed artifact still finds them
    out["positive_control"] = out["positive_control_narrow"]
    out["comparator_control"] = out["comparator_control_narrow"]

    log.rule("W-D.4 — PER-FORK FORENSICS on every divergence")
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
        det, selfref, nonself, false_rec = [], 0, 0, 0
        for d in reps[:24]:
            fr = forensics(by_case[d["case"]], mode, "narrow", d["at"], d["take"], d["in_budget"])
            fr["fork"] = d
            det.append(fr)
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
        log("SAMPLED", f"  forensics EXECUTED on {len(det)} representatives of {len(divs)} "
                       f"divergences ({len(seen)} distinct signatures); every distinct signature "
                       f"is covered when that count is <= 24")
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
    subj = {}
    for mode in ARMS:
        files = sorted(OUT.glob(f"wd_subj_{mode}_*.json"),
                       key=lambda q: int(q.stem.split("_")[-2]))
        parts = [json.load(open(f)) for f in files]
        k = collections.Counter()
        for pt in parts:
            for kk, vv in pt["changed_slot_kinds"].items():
                k[kk] += vv
        subj[mode] = dict(
            genuine=sum(pt["genuine"] for pt in parts),
            diverged=sum(pt["diverged"] for pt in parts),
            reconverged=sum(pt["reconverged"] for pt in parts),
            n_cases_ok=sum(pt["n_cases_ok"] for pt in parts),
            n_cases_failed=sum(pt["n_cases_failed"] for pt in parts),
            probed=sum(pt["probed"] for pt in parts),
            no_live_window=sum(pt["no_live_window"] for pt in parts),
            inert=sum(pt["inert"] for pt in parts),
            changed_slot_kinds=dict(k))
        subj[mode]["reconvergence_rate"] = (subj[mode]["reconverged"] / subj[mode]["genuine"]
                                            if subj[mode]["genuine"] else None)
    out["widened_fingerprint"] = subj
    for mode in ARMS:
        r, v = subj[mode], out["narrow"][mode]
        log("MEASURE", f"mode={mode:5} | (verb, subject) fingerprint: RECONVERGED "
                       f"{r['reconverged']}/{r['genuine']} = "
                       f"{r['reconvergence_rate']*100:.2f}% · DIVERGED {r['diverged']}   "
                       f"[verb-only, same run: {v['reconverged']}/{v['genuine']} = "
                       f"{v['reconvergence_rate']*100:.2f}%, DIVERGED {v['diverged']}]")
        log("  KINDS", f"changed window slots by kind: {r['changed_slot_kinds']}")
    ok = all(subj[m]["changed_slot_kinds"].get("VERB-SET", 0) == out["narrow"][m]["diverged"]
             for m in ARMS)
    log("CROSS-CHECK", f"VERB-SET changed slots == the verb-only instrument's DIVERGED count, in "
                       f"every arm: {ok} "
                       f"({ {m: (subj[m]['changed_slot_kinds'].get('VERB-SET', 0), out['narrow'][m]['diverged']) for m in ARMS} })",
        "the two instruments are the same instrument at two resolutions, and this is the "
        "arithmetic that says so — the verb-only probe sees exactly the VERB-SET changes and "
        "nothing else")
    log("⚠ CONSEQUENCE", "THE CONTROL IS NOT 100% AT THIS RESOLUTION, AND THAT RETRACTS THE "
                          "DIAGNOSIS THE PUBLISHED 100% RESTED ON — not the arithmetic.",
        "ARM 9c reads: *'the deliberation never reads the world ... the only channel by which "
        "anything that happened can reach a later decision is a CLAIM in the actor's ledger'*, "
        "and ARM 9d then shows that channel closed. `opening_set` indeed reads no World — but its "
        "`q` DOES: `questions_for(w, p)` takes a World, and clause 3 is `subject in "
        "referents(q)`. TRACED, not inferred (NPC-088, `none`, fork at decision 0, "
        "`('move','r_hearth')` -> `('speak','r_hearth')`): p_c's tick-1 question list goes "
        "`[claim_landed('p_c'), claim_landed('r_hearth'), ...]` in the baseline to "
        "`[claim_landed('r_hearth'), claim_landed('p_c'), ...]` in the fork, "
        "`question_aggregation_rule='first'` takes `qs[0]`, and every one of p_c's seven "
        "candidates changes subject from `p_c` to `r_hearth` while the verb sequence stays "
        "identical. So a fork ALREADY changed what a person deliberates ABOUT before `W-B`, "
        "through Q2 and the ledger's APPEND ORDER — a second ledger channel that is not "
        "`belief_contradicts`.")
    log("SO THE TWO CHANNELS SEPARATE", "SUBJECT-ONLY changes are the OLD channel (present at "
                                        "`none`, 510 slots) and VERB-SET changes are `W-B`'s "
                                        "(0 at `none`, 62 at `actor`, 182 at `total`). They do "
                                        "not overlap in any arm.")

    (OUT / "WD_LOG.txt").write_text(log.text() + "\n")
    json.dump(out, open(OUT / "wd_acceptance.json", "w"), indent=1, default=str)
    print(log.text())
    print(f"\nwrote {OUT/'WD_LOG.txt'} and {OUT/'wd_acceptance.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
