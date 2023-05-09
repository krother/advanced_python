Warnings
========

The ``warnings`` module writes warning messages to the ``sys.stderr``
stream:

.. code:: python3

   import warnings

   warnings.warn("This is a drill!")

The output warning also contains a line number:

::

   warn.py:3: UserWarning: This is a drill!

Python has an option to stop with an error as soon as a warning occurs:

::

   python -W error warnme.py

You could also mute all warnings:

::

   python -W ignore warnme.py
