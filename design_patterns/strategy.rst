The Strategy Pattern
====================

Implement the `Strategy Pattern <https://sourcemaking.com/design_patterns/strategy>`__ to move traps and monsters in the game.
There should be multiple **movement patterns** that can be freely combined with monsters.
Each monster should have a `movement` attribute that references the strategy.

Implement the following strategies:

- no movement at all
- move left-right until an obstacle is hit
- move up-down until an obstacle is hit
- move randomly

Instead of implementing each strategy as a class, Python gives us the option to use a generator.
Consider the following signature:

.. code:: python3

    Position = tuple[int, int]

    def move_always_left(dungeon: DungeonGame) -> Iterable(Position):
        while True:
            yield "left"

The strategy will require a dungeon object to check for obstacles.
Use the strategy in a monster class:

.. code:: python3

    class Monster:

        def __init__(self, dungeon):
            self.movement = move_always_left(dungeon)

        def update():
            self.position = next(self.movement)
