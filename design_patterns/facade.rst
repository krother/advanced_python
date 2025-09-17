
The Facade Pattern
==================

Implement the `Facade Pattern <https://sourcemaking.com/design_patterns/facade>`__ for the class `DungeonGame`.
The Facade class should serve as the **only** contact point with the UI, so that:

- the UI (`main.py`) only accesses attributes and methods of the Facade.
- the UI may use auxiliary data structures (e.g. models returned by Facade methods)
- the `DungeonGame` class or any classes beneath contain any UI code (textures, drawing, screen I/O)
- the graphics engine in UI could be replaced, without modifying the Facade
- the Facade serves as a contact point for writing test code.

Automated Tests
===============

Write one or more Unit Tests against the Facade.
See `https://github.com/krother/advanced_python_de/tree/main/solutions/packages/space-package/tests` for an example of test code.
