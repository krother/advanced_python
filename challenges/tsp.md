
# Traveling Salesman

**🎯 Implement a Solution for the Traveling Salesman Problem**

A traveling salesman would like to visit N cities and cover as short a distance as possible.

Write a program that *visits* all cities with the following coordinates:

    import random

    N = 10
    random.seed(42)
    x = [random.randint(1, 100) for i in range(N)]
    y = [random.randint(1, 100) for i in range(N)]

A solution could look like this:

    7 5 2 8 6 1 0 3 9 4

    total distance traveled: 123.45


## Tasks

* Implement a random solution first.
* Try a *brute force* solution that tries out all the options.
* Why isn't this solution always the best?
* Measure the runtime for different values of *N*.
* Write a *heuristic solution*.
* Research the traveling salesman problem.
* Research what a **NP-complete problem** is.


*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
