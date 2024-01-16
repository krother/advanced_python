The Facade Pattern
==================

Before you can write automated tests, you need to make sure that your code is testable.
It is not a great idea to test any function or class in your program,
because that makes the program harder to modify in the future.
Whatever you test, you want to be stable and not change very often.
Testable code means that you need to define an **interface** you are testing against.

Also, some things are harder to test than others, graphics and keyboard input for instance.
We won't test them for now. Instead, we want to make the code more testable 
by **separating the graphics engine and game logic**.

The Design
----------

In the `Facade Pattern <https://sourcemaking.com/design_patterns/facade>`__, you define a single class
that serves as the interface to an entire subsysten.
We will define such a Facade class for the game logic named ``DungeonExplorer``:

.. code:: python3

    class DungeonExplorer(BaseModel):

        player: Player
        level: Level

        def get_objects() -> list[DungeonObject]:
            """Returns everything in the dungeon to be used by a graphics engine"
            ...

        def execute_command(cmd: str) -> None:
            """Performs a player action, such as 'left', 'right', 'jump', 'fireball'"""
            ...


Note that the attributes ``player`` and ``level`` of the game might change in the future.
We will treat them as private.
All the communication should happen through the two methods.

In the following exercise, you refactor the code to use the Facade pattern.

Step 1: Separate Modules
------------------------

Split the existing code into two Python modules ``graphics_engine.py`` and ``game_logic.py``.
For each paragraph of code decide, which of the two modules it belongs to.

Step 2: Implement the Facade class
----------------------------------

Copy the skeleton code for the ``DungeonExplorer`` class to ``game_logic.py``.
Leave the methods empty for now.

Step 3: Define a class for data exchange
----------------------------------------

In the ``get_objects()`` method, we use the type ``DungeonObject`` to send everything that
should be drawn to the graphics engine.
This includes walls, the player for now, but will include more stuff later.
Define it as follows:

.. code:: python3

    class DungeonObject(BaseModel):
        position: Position
        name: str

Example objects could be:

.. code:: python3

    DungeonObject(Position(x=1, y=1), "wall")
    DungeonObject(Position(x=4, y=4), "player")

.. note::

    This is really a very straightforward approach to send the information for drawing.
    In fact, it makes a couple of things very hard, e.g. animation.
    This is an example of a design decision: we choose that we do not want animations in the game.
    Our design makes adding them more expensive.

Step 4: Implement the get_objects method
----------------------------------------

Implement the ``get_objects()`` method from scratch.
Create a list of the player and all walls as a list of ``DungeonObject``.

Step 5: Implement the execute_command method
--------------------------------------------

Move the code you have for handling keyboard input into the ``execute_command()`` method.
Replace the keys by explicit commands like `"left"`, `"right"` etc.
The idea behind that is that we do not want the game logic to know anything about
which key you press to walk right. This belongs to the user interface.

Step 6: Import the Facade class
-------------------------------

In the module ``graphics_engine.py``, import the Facade class ``DungeonExplorer``.
The only things the user interface needs to know about are the Facade class and
the data exchange class ``DungeonObject`` (although we do not have to import the latter).

Create an instance of it.

Step 7: Adjust the graphics engine
----------------------------------

Make sure the graphics engine does the following:

- it calls ``DungeonExplorer.get_objects`` in the draw function.
- it does not access the level or player attributes in the draw function.
- it translates the keys to commands
- it calls the ``DungeonExplorer.execute_command`` method.
