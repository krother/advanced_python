
Static Code Checks
==================

Exercise 1: Type Hints
-----------------------

Complete the code in :download:`type_annotations.py` and make sure it works.

*Does the code work even if you enter wrong types?*


Exercise 2: Type Checks
-----------------------

Check the types with:

::

    uv run mypy type_annotations.py

Exercise 3: Linter
------------------

Clean the code with:

::

    uv run black type_annotations.py

Exercise 4: Sort imports
------------------------

Run `isort` on the `space_game` program to sort the imports:

    uv run isort space_game.py

Exercise 5: Style Checks
------------------------

Run `ruff` on the `space` program to get extra hints:

    uv run ruff check space_game.py
