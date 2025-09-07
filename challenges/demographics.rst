
Demographics
============

In this exercise, you will use **comprehensions** to convert, filter and analyze JSON data.
The data in the file :download:`population.json` contains the population of all the countries in the world and their population.

Exercise 1: Read the data
-------------------------

Get started by reading the data in :download:`population.json` and display the first records:

.. code:: python3

   import json
   from pprint import pprint
   
   pop = json.load(open("population.json"))
   pprint(pop[:3])

Exercise 2: Countries
---------------------

Write code for the following tasks

- extract a list of all countries.
- extract unique countries only.
- print the number of unique countries.

Exercise 3: Filter
------------------

Calculate the total sum of the population in 1961 and 2010.

.. note::

   There might be some overlaps in the data such as *East Germany* and *Germany*,
   so the overall sum will be higher than the actual world population.

Exercise 4: Nested List
-----------------------

Convert the data to a nested list with the columns *country, continent, population* for the year 2010:

.. code:: python3

    [['Afghanistan', 'Asia', 27962207.0],
    ['Albania', 'Europe', 2901883.0],
    ['Algeria', 'Africa', 36036159.0]]

Exercise 5: Dictionary
----------------------

Convert the nested list back to a dictionary with the key being the country name and the value a dictionary of the other values:

.. code:: python3

   {
       'Afghanistan': {'population': 27962207.0, 'continent': 'Asia'},
       'Albania': {'population': 2901883.0, 'continent': 'Europe'},
       'Algeria': {'population': 36036159.0, 'continent': 'Africa'},
   }

Exercise 6: Transpose
---------------------

Create a dictionary, but this time it should contain three lists:

.. code:: python3

   {
       ['Afghanistan', 'Albania', 'Algeria', ...],
       ['Asia', 'Europe', 'Africa', ...],
       [27962207.0, 2901883.0, 36036159.0, ...],
   }
