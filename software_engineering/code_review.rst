Code Reviews
============

A **Code review** means that another person reads your code. This could
be:

-  a senior engineer
-  a programmer with similar experience
-  a junior developer

All three provide complementary feedback that is useful in many ways.
Besides discovering bugs, they also expose general design weaknesses
(that might become bugs in the future) or simply learn you
alternative/better ways to solve the problem.

Because of that, many engineers see code reviews as the 
**number one technique to build high-quality software.**


Exercise 1: Code Review
-----------------------

Inspect the Python code in :download:`prototype_opencv.py`.
Answer the following questions:

* What libraries does the program use?
* What variables does the program define?
* What do the functions do?
* Which parts of the code correspond to the flowchart?
* How are the grid coordinates represented?
* What would you like to know more about?

Exercise 2: Modify
------------------

Extend the code such that:

* the player can be moved up and down.
* the player stops at the border of the screen
* the player respawns at the left if they leave the grid on the right side
* there is a "teleport" key that jumps to a random grid point


.. topic:: What to look for in a code review?

   Here are a few things to pay attention to in a code review.
   The list is by far not exhaustive:

   -  Does the module header explain understandably what the code does?
   -  Are constants listed right after the import statements?
   -  Is the code sufficiently documented?
   -  Are the functions understandable?
   -  Are the variable names descriptive
   -  Is the code formatted in a consistent way?
   -  Are there code duplications?
   -  Is there dead code that does nothing?
   -  Are there code sections that are unnecessarily long?
   -  Are there while loops that could run forever?
   -  Are there deeply nested code sections?
   -  Do all functions have exactly one way to return data (either by
      return value OR by modifying an object, not both).
   