"""Importing this package registers every shipped adapter (via @register_adapter)
with tools.sim_harness.adapter.ADAPTER_REGISTRY. Adding a new adapter: write
adapters/my_adapter.py with @register_adapter("my_adapter") on its Adapter
subclass, then add one import line below — no other file needs editing."""
from . import dice_pool_demo  # noqa: F401
from .pr119_governance import pr119_bind_the_cells  # noqa: F401
from .pr119_governance import pr119_guild_ladder  # noqa: F401
from .pr119_governance import pr119_ledger_family_collision  # noqa: F401
from .pr119_governance import pr119_pressure_homeostat  # noqa: F401
from .pr119_governance import pr119_recognition_accountability  # noqa: F401
from .pr119_governance import pr119_structural_gaps  # noqa: F401
from .pr119_governance import pr119_subnational_factions  # noqa: F401
