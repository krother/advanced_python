
The Iterator Pattern
====================

Implement a `MonsterManager` class that is reponsible for keeping all opponents in the game.
Use the `Iterator Pattern <https://sourcemaking.com/design_patterns/iterator>`__ to make the class iterable.
One option

In Python, there exists a shortcut using magic methods:

.. code:: python3

    class MonsterManager(BaseModel):

        monsters: list[Monster]

        def __iter__(self):
            """
            resets the iterator.
            has to return something with a next() method
            """
            self.__i = 0
            return self
        
        def __next__(self):
            if self.__i < len(self.monsters):
                self.__i += 1
                return self.monsters[self.__i - 1]
            else:
                raise StopIteration("the end")

    mm = MonsterManager(monsters=["trap", "ghost", "skeleton"])
    for m in mm:
        print(m)
                
Contrast this implementation with an alternative:

.. code:: python3

    class MonsterManager(BaseModel):

        monsters: list[Monster]

        def __iter__(self):
            return iter(self.monsters)

How does the behavior of the two implemenations differ?
