Concurrency
===========

*Concurrent programming* means that you have two or more sub-programs
running simultaneously. This potentially allows you to use all your
processors at once. This sounds like an enticing idea, but there are
good reasons to be very cautious with it.

----

Pros and Cons of Concurrency
----------------------------

Often concurrency is a bad idea. The devil is lurking in the details:

-  Coordinating parallel sub-programs is very difficult to debug (look up the words *“race condition”* and *“heisenbug”*).
-  Python has a strange thing called the **GIL (Global Interpreter Lock)**. That means, Python can really only execute one command at a time.
-  There are great existing solutions for many typical applications (web scraping, web servers).

On the other hand, concurrency can be a good idea:

-  if your tasks are waiting for some I/O anyway, the speed of Python does not matter.
-  starting multiple separate Python processes is rather easy (with the `multiprocessing` module).
-  if you are looking for a challenge.

There are three noteworthy approaches to concurrency in Python:
**threads**, **coroutines** and **multiple processes**.

----

Multithreading
--------------

This is the old way to implement parallel execution.
It has its flaws but you can grasp the basic idea:

.. literalinclude:: thread_factorial.py

----

Async Coroutines
----------------

The `async` interface has been added to Python more recently.
It fixes many problems of threads.

.. literalinclude:: async_factorial.py

----

Subprocesses
------------

The `subprocess` module allows you to launch extra processes through the operating system.
Subprocesses are not restricted to Python programs.
This is the most flexible approach, but also has the highest overhead.

.. literalinclude:: subprocess_factorial.py

.. literalinclude:: factorial.py

----

Challenge: Gaussian Elimination
-------------------------------

In :download:`gauss_elim.py` you find an implementation of the `Gauss Elimination Algorithm <https://en.wikipedia.org/wiki/Gaussian_elimination>`__ to solve linear equation systems.
The algorithm has a **cubic time complexity**.

Parallelize the execution of the algorithm and check whether it gets any faster.

In :download:`test_gauss_elim.py` you find unit tests for the module.

.. note::

   The linear equation solver is written in plain Python.
   Of course, Numpy would also speed up the execution considerably.
