Variable Scope
==============

Guess the value of the variable ‘a’ in the three example programs.
Check your guess by running the code.

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
