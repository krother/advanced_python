Create a Folder Structure
=========================

A small but important part of a project is creating folders for your
code. In the Python world, there is a standard structure that you will
find in many other projects. The next few steps let you create one.

Step 1: A package folder
~~~~~~~~~~~~~~~~~~~~~~~~

First, you need a place for the package you want to write. A **Python
package** is simply a folder that contains ``.py`` files. Create a
folder ``snake`` inside your repository. On the bash terminal, you would
use

::

   mkdir snake

If your git repository is also called ``snake``, you may want to rename
your project folder to something else like ``snake_project``,
``snake_repo`` or similar. If you have two folders calles ``snake``
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
``snake/`` folder. Add a placeholder function to it:

::

   def play_snake():
       print('this is a snake game')

Now start Python in your main project folder (above the package) through
the terminal. **It is important that you start Python in your project
folder. It will probably not work from your IDE at this point.** The
code that you want to get running is:

::

   from snake.game import play_snake

   play_snake()

You should see the message from the print statement.

--------------

Step 4: main Python file
~~~~~~~~~~~~~~~~~~~~~~~~

Importing the ``play_snake()`` function to play the game is a bit
inconvenient. Let’s create a shortcut. Create a file named
``__main__.py`` (with double underscores on both ends) in the package
folder that contains the following code:

::

   from game import play_snake

   play_snake()

Now it should be possible to start the game by typing:

::

   python snake

--------------

Summary
~~~~~~~

At this point, your project folder should contain:

::

   LICENSE
   prototype.py
   README.md
   snake/
       game.py
       __main__.py
   tests/


.. seealso::
   
   You find detailed info on importing stuff in 
   `Python Modules and Packages on realpython.com <https://realpython.com/python-modules-packages/>`__
