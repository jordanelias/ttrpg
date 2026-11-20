"""B04.18 -- THE ONE SOCIAL SKILL: `law` (ED-IN-0378: the social contest's V2 governs; `insight`, `deception` and
`rhetoric` are not created).

`references/descriptor_registry.yaml: capabilities.rows` is the one definition of a skill; the leaf reader
`engine/substrate/descriptors.py::CAPABILITIES` reads it from `engine/engine_params/descriptors.json`.
"""
from __future__ import annotations

from engine.substrate import descriptors


def test_rhetoric_is_not_a_capability_row():
    rows = set(descriptors.CAPABILITIES)
    assert "law" in rows
    for absent in ("rhetoric", "insight", "deception"):
        assert absent not in rows, f"{absent} is not a skill row (D-U1-03; ED-IN-0378)"
    law = descriptors.capability("law")
    # B05.25 step 7: a skill row carries no `base:` and no `opposed_by:` (the verb row names its attributes); was
    # `law.base == "attr.mind.acuity" and law.opposed_by is None`
    assert law.kind == "skill" and not hasattr(law, "base") and not hasattr(law, "opposed_by")
    assert (law.floor, law.ceiling) == (0, 7) and law.grows_by == ("train", "practice")
    assert "judge" not in law.gloss.lower()  # a judge's close rolls no skill (V2 part 2 §D)
