Concurrency
===========

*Concurrent programming* means that you have two or more sub-programs
running simultaneously. This potentially allows you to use all your
processors at once. This sounds like an enticing idea, but there are
good reasons to be very cautious with it.

----

Why is Concurrency risky?
-------------------------

Many times, the devil is so much in the details that it is even a bad idea.

-  Coordinating parallel sub-programs is very difficult to debug (look up the words *“race condition”* and *“heisenbug”*).
-  Starting multiple Python processes instead is really easy (e.g. from a batch script or the `multiprocessing` module).
-  Python has a strange thing called the **GIL (Global Interpreter Lock)**. That means, Python can really only execute one command at a time.
-  There are great existing solutions for the most typical applications.

----

Alternatives
------------

-  if you want to read/write data, use a database
-  if you want to scrape web pages, use the ``scrapy`` framework.
-  if you want to build a web server, use ``FastAPI`, ``Flask`` or ``Django``.
-  if you want to do number crunching, use ``Spark``, ``Dask``, ``Pytorch`` or ``Tensorflow``

----

When could concurrency be a good idea?
--------------------------------------

Here is one example:

You are writing a computer game for fun and would like many sprites to
move at the same time **AND** you are looking for difficult problems to solve.

There are two noteworthy approaches to concurrency in Python:
**threads** and **coroutines**.

----

Multithreading
--------------

This is the old way to implement parallel execution.
It has its flaws but you can grasp the basic idea:

.. literalinclude:: multithreading.py

----

Async Coroutines
----------------

The `async` interface has been added to Python more recently.
It fixes many problems of threads.

.. literalinclude:: coroutine_asyncio.py

