
The Repository Pattern
======================

Add a save/load functionality to the game. Implement the Repository Pattern.
Consider the following:

- put the repository in a separate module
- create a `Repository` class
- the repository class should have two methods `load` and `save`
- only one saved game should exist at any given time
- none of the code outside the repository should know what is used to store the game
- call the load/save functions from within the UI

Consider the following signature:

.. code:: python3

    class Repository:

        def __init__(self):
            ...

        def save(self, game: DungeonGame) -> None:
            ...

        def load(self) -> DungeonGame:
            ...

To implement the Repository, pick one of the following libraries:

- `json <https://github.com/krother/Python3_Package_Examples/blob/master/json/example_json.py>`__
- `pickle <https://python-basics-tutorial.readthedocs.io/en/latest/save-data/pickle.html>`__
- `sqlite <https://github.com/krother/Python3_Package_Examples/blob/master/sqlite3/example_sqlite.py>`__
