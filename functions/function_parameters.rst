Function parameters
===================

There are four types of function parameters in Python:

-  obligatory parameters
-  optional parameters
-  list parameters (`*args`)
-  keyword parameters (`**kwargs`)

The following example uses all four of them:

.. code:: python3

   def example(obligatory, optional=77, *args, **kwargs):
       print("obligatory: ", obligatory)
       print("optional  : ", optional)
       print("args      : ", args)
       print("kwargs    : ", kwargs)


   example(True, 99, 77, 55, a=33, b=11)

--------------

Mutable and immutable parameters
--------------------------------

Depending on their data type, some function parameters are **mutable**,
others are not:

-  lists, dictionaries and sets are **mutable**
-  integers, floats, strings and tuples are **immutable**

Here is a small illustration:

.. code:: python3

   def change(var1, var2):
       """Change two values."""
       var1 += [7]
       var2 += 7
       
       
   data = [3,4,5]
   number = 6

   change(data, number)

   print("The list now contains", data)
   print("The number is now", number)


.. topic:: Good function style

   -  Arguments for input only.
   -  Return statement for output only.
   -  No global variables.
   -  One function serves exactly one purpose.
   -  Write documentation string first.
   -  keep functions small (below one screen page)
   -  If you have too many parameters, make a new class.
   -  Do not mix mutable types and return output.
