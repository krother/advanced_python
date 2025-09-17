The Factory Pattern
===================

Implement a zoom factor so that the game can be played with different resolutions.
The tile bitmaps will be produced by a class implementing the `FactoryMethod <https://sourcemaking.com/design_patterns/factory_method>`__ pattern.
Use the following:

- create a new module `tiles.py`
- create a new class `TileFactory` that takes an integer zoom factor
- only very few zoom factors need to work (1, 2, 4)
- move the `read_images`, `read_image` and `TILE_SIZE` objects to the new module
- edit the line with `np.kron` (a Kronecker product) to zoom the tiles.

To retrieve tiles by a name, implement a `get_tile()` method. Alternatively, use the `__getitem__` magic method:

.. code:: python3

    class TileFactory:

        def __getitem__(self, name: str) -> np.ndarray:
            ...

    tf = TileFactory(zoom=2)
    tile = tf["player"]

.. hint::

    Having the factory opens up more flexible options like adding synonyms for the tiles
    or reading the tile definitions from a file.
