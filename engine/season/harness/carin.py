"""`harness/carin.py` -- CARIN'S WORLD (`NPC-088`, #353 §13.1), the one builder of it: `headless.build_world` re-exports it, and `harness/scenarios.py` plays it as a scenario.

A LEAF of the harness: it imports no other harness module. `headless.py`'s `--world` flag plays a scenario from `scenarios.SCENARIOS`, and `scenarios.py` plays this
world as one, so the world could not live in `headless.py` without the two importing each other. Moved verbatim (B11 close); every comment on a choice below is the
one `headless.py` carried.
"""
from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import pursuit as _pursuit
from ..queries.world_q import RESIDE_KIND
from ..state.carriers import Person, Proposition, Rung, Site, Tenure, generated_attributes
from ..state.world import World

# The three people #353 §13.1's worked case needs, and no more. `carin` makes the copies; `bailiff`
# is the person a copy can reach, so that a claim landing in SOMEONE ELSE'S ledger produces THEIR
# Q2 question -- which is the link check 2 walks. `warden` holds the rung.
CARIN, BAILIFF, WARDEN = "p_carin", "p_bailiff", "p_warden"


def build_world(seed: int = 0, fixtures: "S.Fixtures" = None) -> World:
    """Carin's world. Fixtures default to `DEFAULT_FIXTURES`, unmodified, so check 3's claim --
    that every number read resolves to a register `site:` -- is about the registered defaults and
    not about a set tuned for this run.

    ⚠ `fixtures` IS A PARAMETER BECAUSE THE FIRST VERSION BUILT THE WORLD FROM `DEFAULT_FIXTURES`
    AND THEN RAN IT ON WHATEVER WAS SWEPT. The site's starting `condition` came from the unswept
    default while the band floors and the wear came from the swept one, so a `condition_scale`
    sweep silently compared a site at 1000 against floors scaled to 10000 -- a confounded arm,
    which duly reported a "finding" that was the confound. Found while writing the sweep itself;
    §0.1 point 1 is the general form of it."""
    w = World(seed, fixtures or DEFAULT_FIXTURES)
    w.rungs["hearth_ostvik"] = Rung("hearth_ostvik", "hearth")
    w.rungs["ostvik"] = Rung("ostvik", "settlement")
    w.sites["scriptorium"] = Site("scriptorium", "hearth_ostvik", "body",
                                    condition=w.fixtures.get("condition_scale"))

    for pid, name in ((CARIN, "Carin Vedel"), (BAILIFF, "Uwe the bailiff"),
                      (WARDEN, "the warden")):
        # B01a.03: each of the three holds a DRAWN SHEET (`state/carriers.py::generated_attributes`, the owner `build_realm` seats by).
        w.persons[pid] = Person(pid, name, attributes=generated_attributes(
            w.world_seed, pid, w.fixtures.get("generated_attribute_range")))
    w.add_tenure(Tenure("t_carin_in", CARIN, "hearth_ostvik", "contain", since=0))
    w.add_tenure(Tenure("t_bailiff_in", BAILIFF, "hearth_ostvik", "contain", since=0))
    w.add_tenure(Tenure("t_warden_in", WARDEN, "ostvik", "contain", since=0))
    w.add_tenure(Tenure("t_hearth_in", "hearth_ostvik", "ostvik", "contain", since=0))
    # Plan position `19c`: each of the three LIVES where he stands at build -- the `reside` edge a
    # `move` leaves behind (`populated.build_realm`'s rule, and `loop/effects.py::_eff_migrate`).
    for pid, home in ((CARIN, "hearth_ostvik"), (BAILIFF, "hearth_ostvik"), (WARDEN, "ostvik")):
        w.add_tenure(Tenure(f"t_{pid}_home", pid, home, RESIDE_KIND, since=0))

    # ⚠ HER MOTIVE IS A `commit` TO AN OUGHT PROPOSITION, WHICH IS Q4 -- the source `PLAN.md` `W5`
    # added and V2 §F1 omitted. Without it "an NPC with a standing ambition and a quiet season
    # forms no candidates at all", and Carin IS that NPC: nothing is due, nobody has told her
    # anything, and her subsistence has not moved. Q4 is the only reason she acts.
    prop = Proposition("prop_einhir", "OUGHT", "einhir_texts",
                         "the Einhir texts should survive", True, 0)
    w.propositions[prop.id] = prop
    w.add_tenure(Tenure("t_carin_commits", CARIN, prop.id, "commit", since=0))

    # Convictions read PERSON-SIDE ONLY, scored against `rosters.yaml`'s alignment table. These
    # are hers; nothing else in the loop reads them.
    # ⚠ THESE ARE WORLD DATA, NOT A DEFINITION, and the distinction is the one `rosters.yaml`
    # states: a roster or a table is a definition the GAME resolves from; a person's conviction
    # weight is a fact about that person, like their name. It is nonetheless load-bearing on the
    # result and saying so is owed — her `stability` projected onto `precedent_substantive` against
    # the alignment table's `create_record: -0.8` there is what puts `create_record` high in her
    # ranking, and therefore what starts the causal chain check 2 measures. A different Carin
    # produces a different season, which is the point of her having convictions at all.
    # ⚠⚠ **EACH NAME IS LOOKED UP IN THE OWNER RATHER THAN TYPED, AND THE GUARD THAT FORCED THIS
    # IS RIGHT EVEN THOUGH ITS FIRST READING OF THESE LINES WAS NOT.**
    # `tests/valoria/test_conviction_roster_single_owner.py` fails on any literal holding TWO OR
    # MORE canonical conviction names, because three incompatible rosters once shipped at the same
    # time and silently disabled ED-912 §6.1's Conviction Scar. `{"Precedent": 0.9, "Utility": 0.3}`
    # is two canonical names in one dict, so it read as a roster fragment — and the distinction
    # between a ROSTER (an enumeration that can drift out of step with the owner) and a REFERENCE
    # (a choice of one member) is not one an AST scan can draw.
    # `_pursuit` draws it by CONSTRUCTION rather than by argument: one name per call, each checked
    # against the pursuit roster, which IS `engine.substrate.descriptors.PURSUITS` — the same object,
    # not a copy. A rename in `references/descriptor_registry.yaml` now raises here by name instead
    # of silently seeding a conviction nobody holds, which is strictly more than the literals did.
    # ⚠ IN-08's CELLS COMMIT MIGRATED THE THREE TO THE FIFTEEN PURSUITS, by the rule the cast
    # registry was migrated by (the retired pursuit-cells draft's §4.1, folded into the build by Jordan
    # 2026-10-06): `Precedent` and `Order` have no pursuit of their own name -- `stability` is the
    # successor for the procedural readers; `Utility` has none, and goes to the pursuit the
    # character's own goal names. Weights are carried, not renormalised.
    #   * Carin: `Precedent .9` -> `stability .9`; `Utility .3` -> `community .3`, the pursuit her
    #     one standing goal names (the `commit` above: *"the Einhir texts should survive"* -- the
    #     §4.3 reading of NPC-082's *"Fights for Einhir"* as categorical belonging).
    #   * the bailiff: `Order .8` -> `stability .8`; `Precedent .4` -> `justice .4`, §4.1's other
    #     successor for `Precedent` (Baralta's *"procedure IS justice"*), rather than collapsing into
    #     `stability` at 1.2, past the 0-1 weight scale.
    #   * the warden: `Precedent .6` -> `stability .6`.
    # So the three stay three: Carin and the warden share a direction only in `stability`, and
    # Carin's `community` separates their rankings (a pure rescale would not).
    # [JUSTIFIED: these five weights are AUTHORED CHARACTER, not a mechanical constant -- #353 §14 types pursuits as "weights over the closed roster | 1-3 primary + distributed" and supplies no magnitudes. Carin's `stability` is what puts `create_record` (precedent_substantive -0.8) high in her ranking and starts her causal chain; the rest are her, the bailiff and the warden being three different people. `H-46` is the row, closed as framed by IN-43]
    w.persons[CARIN].pursuits = {_pursuit("stability"): 0.9, _pursuit("community"): 0.3}
    # [JUSTIFIED: as the line above -- authored character under `H-46`, not a mechanical constant. The bailiff is procedural-first (stability 0.8) and the warden holds one pursuit weakly, which is what makes the three people three]
    w.persons[BAILIFF].pursuits = {_pursuit("stability"): 0.8, _pursuit("justice"): 0.4}
    # [JUSTIFIED: as above -- one pursuit, held weakly; the warden is the least opinionated of the three by design]
    w.persons[WARDEN].pursuits = {_pursuit("stability"): 0.6}
    return w
