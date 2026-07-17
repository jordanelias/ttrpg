"""
sim/autoload/scene_slate.py — Scene selection and queue manager

Canon source: designs/architecture/scale_transitions_v30.md §4 Zoom In-Out Protocol
Status: [CANONICAL — Phase 1 implementation 2026-05-17]

Manages the queue of personal-scale scenes to resolve during a strategic season.
Strategic phase generates scene triggers; this module queues and dispatches them.

Dependencies:
  - sim/autoload/game_state

Entry points:
  - queue_scene(scene_type, context) -> SceneSlot
  - next_scene() -> SceneSlot | None
  - clear() -> None
"""
from __future__ import annotations

from dataclasses import dataclass, field
from collections import deque


@dataclass
class SceneSlot:
    scene_type: str   # e.g. "combat", "contest", "fieldwork", "companion", "thread"
    context: dict = field(default_factory=dict)
    priority: int = 0  # higher = resolve first


_queue: deque[SceneSlot] = deque()


def queue_scene(scene_type: str, context: dict | None = None,
                priority: int = 0) -> SceneSlot:
    """Add a scene to the resolution queue."""
    slot = SceneSlot(scene_type=scene_type, context=context or {}, priority=priority)
    _queue.append(slot)
    # Re-sort by priority (stable sort preserves insertion order within same priority)
    sorted_items = sorted(_queue, key=lambda s: -s.priority)
    _queue.clear()
    _queue.extend(sorted_items)
    return slot


def next_scene() -> SceneSlot | None:
    """Pop and return the next scene to resolve, or None if empty."""
    if _queue:
        return _queue.popleft()
    return None


def pending_count() -> int:
    return len(_queue)


def clear():
    """Clear the scene queue (e.g. at season start)."""
    _queue.clear()
