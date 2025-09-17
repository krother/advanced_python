
The Adapter Pattern
===================

Read about the `Adapter Pattern <https://sourcemaking.com/design_patterns/adapter>`__

In this exercise, lets consider we have the following definition of the main game class:

.. code:: python3

   class DungeonGame(BaseModel):
       _status: GameStatus = "running"
       x: int = 8
       y: int = 1
       level: list[str]

However, it turns out that a web API requires a different interface:

.. code:: python3

    Position = tuple[int, int]
    
    class Player(BaseModel):
        health: int = 3
        position: Position

    class Level(BaseModel):
        level_map: list[list[str]]

    class WebGame(BaseModel):
        id: int
        player: Player
        level: Level
        x: int = 8
        y: int = 1
        level: list[str]


Exercise 1
----------
Write a mapper function that converts a `DungeonGame` object into a `WebGame` object.

Exercise 2
----------
Write an Adapter class that allows to use a live object of the first type with the interface of the second.
