Virtual Environments
====================

When developing software, you often need a specific combination of
Python libraries. Sometimes this is difficult, because you require a
specific version of a library, want to test your program on multiple
Python versions, or simply need to develop your program further, while a
stable version is installed on the same machine. In these cases,
**virtual environments** come to the rescue.

--------------

What is a virtual environment?
------------------------------

A virtual environment manages multiple parallel installations of Python
interpreters and libraries, so that you can switch between them. The
virtual environment consists of a folder per project, in which Python
libraries for that project are installed.

--------------

How to install a virtual environment?
-------------------------------------

There are many Python tools to manage virtual environments: venv,
virtualenv, Pipenv and Poetry. A beginner-friendly tool is to use
**conda**. If you haven’t installed Anaconda already, you can find the
**Miniconda installer** at https://conda.io/miniconda.html.

--------------

How to set up a project with conda?
-----------------------------------

Once the installer finishes and you open a new terminal, you should see
``(base)`` before the prompt:

::

   (base) ada@adas_laptop:~$

This means you are in an virtual environment called *“base”*.

Let’s create a new one for a project called **dungeon_explorer**, specifying a
Python version:

::

   conda create -n dungeon_explorer python=3.11

Behind the scenes **conda** creates a new subdirectory. This is where
libraries for your project will be stored. There are also scripts to
activate the environment.

--------------

How to work with an environment
-------------------------------

To start working with your project, type:

::

   conda activate dungeon_explorer

You should see *(dungeon_explorer)* appearing before your prompt. Now, whenever you
use *pip* to install something, it will be installed only for
*myproject*.

Now check which libraries you have installed:

::

   pip freeze

You can install additional libraries with ``pip`` or ``conda``.
For instance, you need to install OpenCV even if you already installed it in your base environment:

::

   conda install opencv-python

When you want to switch back to the base environment, type:

::

   conda activate base

The virtual environment is specific for a terminal session. Thus, you
can work on as many projects simultaneously as you have terminals open.
