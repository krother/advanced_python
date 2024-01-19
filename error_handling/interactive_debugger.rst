
Interactive Python Debugger
===========================

The ``ipdb`` program is an *interactive debugger* that allows you to execute a program in slow motion.

Install it with:

::

    pip install ipdb

Then you can start your program in debugging mode from the terminal:

::

    python -m ipdb dungeon_explorer.py

In ``ipdb`` you have a couple of keyboard shortcuts that allow you to navigate the programs execution:

=================== ========================================================================
command             description
=================== ========================================================================
``n``               execute the next line
``s``               execute the next line. If it contains a function, step inside it
``b 57``            set a breakpoint at line 57
``c``               continue execution until the next breakpoint
``ll``              list lots of lines around the current one
``myvar``           print contents of the variable ``myvar``
``myvar = 1``       modify a variable
=================== ========================================================================
