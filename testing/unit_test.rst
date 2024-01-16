Unit Tests
==========

In this short exercise, we will write a test against the Facade.

Step 1: Install pytest
----------------------

Make sure pytest is installed:

::

    pip install pytest

Step 2: Create a test
---------------------

Create a file ``test_game_logic.py``. In it, you need the folowing code:

.. code:: python3

    from game_logic import DungeonExplorer, DungeonObject

    def test_move():
        dungeon = DungeonExplorer(
            player=Player(Position(x=1, y=1),
            ...  # add other attributes if necessary
        dungeon.execute_command("right")
        assert DungeonObject(Position(x=2, y=1), "player") in dungeon.get_objects()

A typical automated test consists of three parts:

1. setting up test data (fixtures)
2. executing the code that is tested
3. checking the results against expected values

Step 3: Run the test
--------------------

Run the tests from the terminal with:

::

    pytest

You should see a message that the test either passes or fails.
