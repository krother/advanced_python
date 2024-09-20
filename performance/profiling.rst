
Measuring Performance
=====================

Profiling Python Scripts
------------------------

Run the code in :download:`mandelbrot.py` and time its execution with `cProfile`, the Python profiler:

.. code::

    python -m cProfile -s cumtime mandelbrot.py > profile.txt

Inspect the output and look for bottlenecks.

Then insert the line:

.. code:: python3

    z[index] = z[index] \*\* 2 + c[index]

Re-run the profiling.

.. hint::

   cProfile also works inside a program:

   .. code:: python3

       import cProfile
       cProfile.run("[x for x in range(1500)]")

Timing in Jupyter / IPython
---------------------------

IPython (including Jupyter notebooks) has two magic commands for measuring execution time.

.. code:: ipython3

    %time len(range(100000))

compare the output to

.. code:: ipython3

    %timeit


C Extensions
------------

Inspect how a Python-C interfacee looks like.
Examine the code at `https://github.com/biopython/biopython/blob/master/Bio/PDB/ <https://github.com/biopython/biopython/blob/master/Bio/PDB/>`__

In particular, inspect the files:

- NeighborSearch.py
- kdtrees.c
- setup.py (in the main directory)
- README.md (in the main directory)
