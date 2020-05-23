
# Concurrency

*Concurrent programming* means that you have two or more sub-programs running simultaneously.
This potentially allows you to use all your processors at once.
This sounds like an enticing idea, but there are good reasons to be very cautious with it.

### Why is Concurrency a bad idea?

* Starting multiple Python processes instead is really easy (e.g. from a batch script).
* Coordinating parallel sub-programs is very difficult to debug (look up the words *"race condition"* and *"heisenbug"*).
* Python has a strange thing called the **GIL (Global Interpreter Lock)**. That means, Python can really only execute one command at a time.
* There are great existing solutions for the most typical applications.

### Alternatives

* if you want to read/write data, use a database
* if you want to scrape web pages, use the `scrapy` framework.
* if you want to build a web server, use `Flask` or `Django`.
* if you want to do number crunching, use `Spark`, `Pytorch` or `Tensorflow`

### When could concurrency be a good idea?

I can think of one reason:

You are writing a computer game for fun and would like many sprites to move at the same time
**AND** you are looking for difficult problems to solve.

There are two noteworthy approaches to concurrency in Python: **threads** and **coroutines**.
