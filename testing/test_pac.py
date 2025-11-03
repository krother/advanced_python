## 2. Write Tests

Write a test function `test_eat()` in a file `test_pac_game.py` against the following scenario:

- there is a small level with lots of empty space.
- the pac is in the top left corner (0/0)
- the pac is facing right
- the pac moves
- check the new position of the pac, it should now be (1/0) 

Run the test with:

    uv run pytest

Make sure the test works.

## 3. Eating Dots

Write another test against this scenario:

- there is a small level full of dots.
- the pac is in the top left corner
- the pac is facing right
- the pac moves
- it eats a dot and gets a point
- the dot disappears from the map

## 5. Fixture

Move the creation of the game data for testing into a fixture.

## 6. Conftest

Move the fixture in `test_pac_game.py` to a file `conftest.py`.
Discuss the scope of fixtures (session, module, class, test).
