"""`engine.season.boot` -- the realm builder and the chooser's set-up: reads the authored data,
constructs the World, holds no token after construction; imports no instrument.

*Boot* is the start-up step that builds the world before the first season, as a computer boots
before it runs. This is game code (`04_CODE_ARCHITECTURE.md` §A.2's `boot/` row, PART D row 53):
the instruments under `harness/` import it, and it never imports them. It re-exports nothing.
"""
