"""Importing this package registers every shipped adapter (via @register_adapter)
with tools.sim_harness.adapter.ADAPTER_REGISTRY. Adding a new adapter: write
adapters/my_adapter.py with @register_adapter("my_adapter") on its Adapter
subclass, then add one import line below — no other file needs editing."""
from . import dice_pool_demo  # noqa: F401
