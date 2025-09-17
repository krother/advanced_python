The Observer Pattern
====================

Read about the `Observer Pattern <https://sourcemaking.com/design_patterns/observer>`__ .
Use it to implement **doors and switchers**:

- define a class `Door` and a class `Switch`
- there is no need to add extra interfaces, the two classes are sufficient
- the `DungeonGame` class keeps a list of `Door` objects and a list of `Switch` objects
- the switch keeps a list of doors
- the doors register with a switch in their constructor
- doors and switches have a position
- all doors are closed initially
- when a player steps on a switch, it notifies its doors to open
- when the player steps on the switch again, the doors close

Use the signature:

.. code:: python3

    class Door(BaseModel):
        position: tuple[int, int]
        open: bool = False

    class Switch(BaseModel):
        position: tuple[int, int]
        observables: list[Door]
