

# Session 4: Object-Oriented Programming

**Goal: refactor code using classes**


### Excercise 1: Pandas go to space

In the folder for this session, you find the game **pandas go to space**.
This is a Python adventure I designed for programming courses.

Start the game by running the text-based interface in `cli.py` with

    python cli.py

### Exercise 2: Code review

Read through the three Python files.
Depending on your experience, focus on:

- `cli.py` (beginner)
- `game.py` (intermediate)
- `location.py` (advanced)

You may also want to inspect the smaller JSON file to see the game data.

Note sections in the code that you would like to know more about.
Also, think about whether there are parts of the code that you find problematic or hard to read.


### Exercise 3a: Traditional Python class

Examine the class `game.LoadCargoCommand`. Find the following:

- the class name
- the attributes and their types
- the methods
- the self attribute
- an attribute that is accessed within the class
- an attribute or method that is accessed from outside the class

### Exercise 3b: Pydantic class

Examine the class `location.Location`. Find the following:

- the class name
- the attributes and their types
- the methods
- the self attribute
- an attribute that is accessed within the class
- an attribute or method that is accessed from outside the class

### Exercise 4: Create a class

In this exercise, we will get rid of the global variables.
In `game.py`, create a new class `Game` that contains three attributes:

- location
- cargo
- crew

Create a global instance of `Game` right after the definition:

    game = Game(...)

Change the code to use the instance, e.g. `game.cargo` instead or `cargo` wherever applicable.

Run the program and make sure it works.


### Exercise 5: Create a method

Move the function `is_solved()` into the `Game` class:

- indent it so that it is inside the block of the class
- add the `self` parameter
- change references to `game.` to `self.`
- change the function call `is_solved()` to `game.is_solved()`

Make sure the program still works.

### Exercise 6: Object Composition

Where do you have composition in the new `Game` class?
Wouldn't it be easier to merge the code from all classes in one?

Discuss why composition is important.

### Exercise 7: Inheritance and Polymorphism

Create a superclass `Command`:

    from abc import ABC, abstractmethod

    class Command(ABC):
    
        def __init__(self, name):
            self.name = name

        @abstractmethod
        def executed(self):
            pass

Now adjust the other types of commands to inherit the new class.
If you want to use an inherited method, use in the child classes:

    def __init__(self, name):
        super().__init__(self, name)
        ...


### Exercise 8: Static methods

Try making the three `execute()` methods static by adding the `staticmethod` decorator and removing the `self` parameter:

    @staticmethod
    def execute():
        ...
    
For which of the methods does it work?
