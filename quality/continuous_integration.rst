Continuous Integration
======================

In this exercise you will create a simple **Continuous Integration**
workflow.

What CI does
------------

When anyone pushes to a **remote git repository**, the git  server should:

1. create an empty virtual computer
2. clone the repository
3. install all dependencies
4. run automated tests
5. report whether the tests succeed or fail

Step 1: Preparations
--------------------

You need:

-  a GitHub repo for your project
-  a ``requirements.txt`` file
-  at least one automated test

Step 2: Create a workflow
-------------------------

GitHub Actions needs instructions how to install the program.

Create a folder ``.github/workflows/``. Place a text file ``run_tests.yml``
into that folder containing the following:

::

   name: run_tests

   on:
     push:
       branches: [ main ]

   jobs:
     build:

       runs-on: ubuntu-latest

       steps:
       - uses: actions/checkout@v2
       - name: Set up Python 3.11
         uses: actions/setup-python@v2
         with:
           python-version: 3.11
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt
       - name: Test with pytest
         run: |
           pytest


Step 3: Requirements
--------------------

A best practice is to have a separate file for **development requirements**.

-  Create a separate file ``dev_requirements.txt``
-  Add ``pytest`` to it
-  Add a **pip install** line to the yml file.

Step 4: Push
------------

Commit and push the changes.

Step 5: Observe
---------------

-  Go to GitHub. Check the **Actions** tab.
-  Watch the output of your project building.
-  Also check your mailbox.

Step 6: Badge
-------------

Copy the following code into your ``README.md`` file:

::

   ![Python application](https://github.com/USER/REPO/workflows/run_tests/badge.svg)

Replace **USER** and **REPO** by the data of your project. **run_tests**
is the name from the workflow file.

You should see a red or green badge in the README that updates itself.

.. topic:: Authors

   Malte Bonart participated in the writing of this chapter.
