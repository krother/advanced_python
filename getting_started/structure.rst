Create a Folder Structure
=========================

A small but important part of a project is creating folders for your
code. In the Python world, there is a standard structure that you will
find in many other projects. The next few steps let you create one.

Step 1: A package folder
~~~~~~~~~~~~~~~~~~~~~~~~

First, you need a place for the package you want to write. A **Python
package** is simply a folder that contains ``.py`` files. Create a
folder ``dungeon_explorer`` inside your repository. On the bash terminal, you would
use

::

   mkdir dungeon_explorer

If your project folder (with the git repo) is also called ``dungeon_explorer``,
you may want to rename the project folder to something else like ``dungeon_project`` or similar.
Having two folders called ``dungeon_explorer``
inside each other could lead to strange import bugs later

--------------

Step 2: A folder for tests
~~~~~~~~~~~~~~~~~~~~~~~~~~

You will also want to have a place where you add test code later. Name
that folder ``tests/``. We will leave it empty for now.

::

   mkdir tests

--------------

Step 3: Create a Python module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may want to create a Python module (a ``.py`` file) to make sure
everything is set up correctly. Create a file ``game.py`` inside the
``dungeon_explorer/`` folder. Add a placeholder function to it:

::

   def play():
       print('this is the Dungeon Explorer game')

Now start Python in your main project folder (above the package) through
the terminal. **It is important that you start Python in your project
folder. It will probably not work from your IDE at this point.** The
code that you want to get running is:

::

   from dungeon_explorer.game import play

   play()

You should see the message from the print statement.

--------------

Step 4: main Python file
~~~~~~~~~~~~~~~~~~~~~~~~

Importing the ``play()`` function to play the game is a bit
inconvenient. Let’s create a shortcut. Create a file named
``__main__.py`` (with double underscores on both ends) in the package
folder that contains the following code:

::

   from game import play

   play()

Now it should be possible to start the game by typing:

::

   python dungeon_explorer

--------------

Summary
~~~~~~~

At this point, your project folder should contain:

::

   LICENSE
   prototype.py
   README.md
   dungeon_explorer/
       game.py
       __main__.py
   tests/


.. seealso::
   
   You find detailed info on importing stuff in 
   `Python Modules and Packages on realpython.com <https://realpython.com/python-modules-packages/>`__
