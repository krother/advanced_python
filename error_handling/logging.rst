
Logging
=======

**Logging** is used collect diagnostic information from a program in case you need to debug or analyze its execution later.
Logging is conceptually similar to adding ``print`` statements to your code, but with more fine-grained control.
In Python, the ``logging`` module provides an entry point to generate log messages:

.. literalinclude:: logging_example.py


.. topic:: Exercise

   Change the logging level through ``DEBUG, ERROR, WARNING, INFO and CRITICAL``
   and observe what is the priority order of the display levels.

----

Multiple Loggers
----------------

It is possible to create multiple loggers with different output channels, like screen, file or HTTP services.
Each of them can be configured individually.
Some of the options of the logging module include:

=============================== ====================================================
option                          description
=============================== ====================================================
level                           order of precedence
filename                        where to save the log-messages
format                          string that specifies what the message looks like    
filter                          more sophisticated filtering than with levels only 
=============================== ====================================================

Whether you need multiple loggers or not, the code example below contains a few ways to customize your log messages:

.. literalinclude:: loggers.py
