"""mass_battle.core — the resolver layer (Stage-1 of the bottom-up re-architecture).
Pure state-in -> state-out: pool assembly, exchange, attrition application, state transitions.
Depends only on config (+ duck-typed unit/atom objects); never imports up the DAG."""
