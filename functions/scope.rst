Variable Scope
==============

Python distinguishes local and global variable scope:

**local scope** refers to variables that only exist within a function.

**global scope** refers to variables that are taken from the next level
above the function definition. Usually this is the module (unless you
have nested functions).

Knowing when a variable is local and when global is especially important
when writing values. To avoid trouble, it is a good idea to avoid global
variable most of the time. Still you need to know the difference

--------------

Exercise
--------

Guess the value of the variable ‘a’ in the three programs. Check your
guess by running the code.

Example 1:
^^^^^^^^^^

.. code:: python3

   def addition(number1, number2):
       a = number1 + number2
       return a

   a = 3
   b = 5
   c = addition(a, b)
   print(a)

Example 2:
^^^^^^^^^^

.. code:: python3

   def addition(number1, number2):
       global a
       a = number1 + number2
       return a

   a = 3
   b = 5
   c = addition(a, b)
   print(a)

Example 3:
^^^^^^^^^^

.. code:: python3

   def addition(number1, number2):
       a = number1 + number2
       global a
       return a

   a = 3
   b = 5
   c = addition(a, b)
   print(a)
