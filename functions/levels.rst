Writing a new Function
======================

In this exercise, you will rehearse writing a new Python function.

Requirement: Edit Levels
------------------------

The Dungeon levels should be easy to edit, so that we can add multiple levels more easily.

The Design
----------

At this stage, you should have a class ``DungeonExplorer`` that is the top-level class
for the game logic.
It has defined attributes that contain everything: the player, walls, coins and anything
else you have implemented already.
The exact attributes are not important, all we need to know is that they are somewhere
inside the ``DungeonExplorer`` class and you know their names.

For creating levels, we want to define a new function ``start_level()`` with the following signature:

.. code:: python3

    def start_level(
        dungeon: DungeonExplorer,
        level: list[str],
        start_position: list[int],
        **kwargs
        ) -> None:
        ...

Here, **dungeon** is a DungeonExplorer game object, **level** should be a map of the level, **start_position** where the player starts.
The ``**kwargs`` parameter is a placeholder for things we might add later.
The function does not return anything.

Step 1: Create a test
---------------------

Create a test function in a new file ``test_level.py``:

.. code:: python3

    def test_start_level():
        d = DungeonExplorer(...)  # add necessary parameters but they can be empty
        level=[
            "########",
            "#.#....#",
            "#.#.##.#",
            "#.#..#.#",
            "#.##.#.#",
            "#....#x#",
            "########",
        ]
        start_level(d, level=level, start_position={"x": 1, "y": 1})
        assert [1, 1, "player"] in d.get_objects() # change if your interface is different

The **#** symbols are walls, the **.** are floor, and the **x** is an exit to the next level.
With such a data structure, we should be able to edit levels in a text editor easily!

Add imports as necessary.
Run the test with ``pytest`` from the command line.
It should fail.

Step 2: Implement the function
------------------------------

First, copy the empty function from the design into the code with the game logic.
For now, we keep the function outside of the ``DungeonExplorer`` class.

Then, write code in the function body that changes the position of the player in the ``dungeon`` object.

Run the test again. They should pass now.

.. note::

    You now have a function that *modifies* one of its arguments.
    It is a good practice to not modify arguments and return results at the same time.


Step 3: Handle walls
--------------------

Add the following line to ``test_start_level()``:

.. code:: python3

    assert [4, 2, "wall"] in d.get_objects()   # an example wall

Modify the function body to set the walls of the ``dungeon`` object as well.
To find all walls, you probably will have to iterate through all the positions
of the dungeon somewhere (in ``start_level()`` or ``DungeonExplorer.get_objects()``).
You can loop over a list of strings using the ``enumerate`` function with the following pattern:

.. code:: python3

    for y, row in enumerate(level):         # y is a row number 0, 1, 2, ...
        for x, tile in enumerate(row):      # x is a column number 0, 1, 2, ...
            ...                             # tile is a single character (#, . or x)

Run all tests afterwards and make sure they pass.

Step 4: Handle coins
--------------------

To include a coin in the test, modify the call in  ``test_start_level()``:

.. code:: python3

    coin = {'position': {"x": 1, "y": 5}, 'value': 100}
    start_level(d, level=level, start_position={"x": 1, "y": 1}, coins=[coin])

And add an assertion to the test function:

.. code:: python3

    assert [1, 5, "coin"] in d.get_objects()

Even though we haven't defined coins as part of the function signature, we can use them.
This is what the ``**kwargs`` is for.
Inside the ``start_level()`` function, check whether there are coins in the ``**kwargs`` dictionary:

.. code:: python3

   if "coins" in kwargs:
       for coin in kwargs["coins"]:
            ...    # coin is a dictionary with the fields 'position' and 'value'

Implement the coins and make sure the tests pass.

Step 5: Use the function
------------------------

Modify the ``graphics_engine.py`` module so that:

- it imports the ``start_level()`` function.
- it calls ``start_level()`` to define a dungeon.

To make things a bit easier, you might want to add default values to
the attributes of ``DungeonExplorer`` so that it becomes easier to leave them away.

Make sure the game is still playable.

Step 6: Load levels from a file
-------------------------------

Create a text file that you call ``level_01.json``.
Place the following there.

.. code:: json

    {
        "level": [
            "########",
            "#.#....#",
            "#.#.##.#",
            "#.#..#.#",
            "#.##.#.#",
            "#....#x#",
            "########"
        ],
        "start_position": {"x": 1, "y": 1},
        "coins": [
            {
                "position": {"x": 1, "y": 5},
                "value": 100
            }
        ]
    }

Now you can use the following phrase to load the level:

.. code:: 

    import json

    ...

    level_data = json.load(open("level_01.json"))
    start_level(dungeon, **level_data)


Step 7: More Levels
-------------------

Edit another level in a new JSON file.
See if you can switch between levels by changing the file name.

.. note::

    Be aware that JSON only understands double quotes around strings.
    Also, there must not be any spare commas at the end of a dictionary.
