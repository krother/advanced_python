
# Class Diagrams

One of the first and most important things converting ideas and into code is to structure data.
You want to start structuring your core business data.
In the case of a snake game, this means how the playing field, the snake and the food items are represented.

Class diagrams are a graphical tool to structure your data and check whether it is complete and non-redundant before writing code.

## What does a class diagram contain?

Here is a class diagram for a `PlayingField` class, the box in which a snake will move:

![class diagram for the PlayingField](images/class_playing_field.png)

On top, the class diagram contains a **title**, the name of the class in `SnakeCase` notation.

The second section lists the **attributes** of the class and their **data types**:

* the x/y size of the playing field, a tuple of two integers
* the x/y position of the food item, also a tuple of two integers

The third section lists the **methods** of the class with their **arguments** and **return types**:

* the `add_food()` method takes two integer arguments and returns nothing
* the `add_random_food()` method has no arguments and returns nothing
* the `get_walls()` method takes no arguments and returns a list of x/y integer tuples

## What the PlayingFiled does not contain

It is worth pointing out that the `PlayingField` class lacks two things on purpose:

First, it does not contain an attribute `snake`.
To be precise, it does not know that snakes even exist.
It does not have to know about it.
We want the `PlayingField` and the `Snake` to manage themselves as independently as possible.
This will make debugging a lot easier.

Second, there is no method `draw()`.
Drawing things is usually not part of your core business.
In the snake game, you may want to change the user interface later (e.g. by adding graphics and sound effects).
The core logic of how the snake moves should not change because of that.

----

## Write Skeleton Code

A great thing about class diagrams is that you can create them to code easily.
The Python `dataclasses` module saves you a lot of typing:

    from dataclasses import dataclass

    @dataclass
    class PlayingField:

        size: (int, int)
        food: (int, int) = None

        def add_food(self, x, y):
            ...

        def add_random_food(self):
            ...

        def get_walls(self):
            ...

This code defines the `size` and `food` attributes and annotates their data types.
The `food` attribute has a default value.
The class also defines the methods from the class diagram (each with the obligatory `self`).
But we leave the method bodies empty for now.

The `@dataclass` automatically creates the `__init__()` and `__repr__()` methods for you, so that you can set and inspect the attribute values.
The code is already executable:

    pf = PlayingField(size=(10, 10))
    print(pf)
    print(pf.size)
    print(pf.get_walls())

Although our class does nothing yet, it helps to think about your desing and write other code that depends on it.

----

## Alternative Designs

Usually, there is more than one way to design a class.
Consider this alternative design for `PlayingField`:

![alternative PlayingField class](images/class_playing_field_alt.png)

There are a few differences:

* size and food have separate x and y attributes instead of being tuples
* the walls are represented by a list of `(int, int)` tuples
* the `add_food()` method expects a tuple instead of two integers
* there methods `is_wall()` and `get_walls()` are no longer there

One could discuss a lot which design is better.
You are better off postponing that discussion to a cleanup stage once the code is running.
The differences are very small and easy to change.
In Python, one could even state that the data structures are practically *identical*.

Using the `@property` decorator, you can translate attributes into each other.
The following code translates the `size` attribute into two new attributes `size_x` and `size_y`:

    @property
    def size_x(self):
        return self.size[0]
    
    @property
    def size_y(self):
        return self.size[1]

Now you can use all three attributes without storing redundant data:

    pf = PlayingField(size=(5, 5))
    print(pf.size)
    print(pf.size_x)
    print(pf.size_y)


More complex and difficult questions arise when planning relationships between multiple classes.
There will be multiple working alternatives, but some may fall on your feet in the long run.
You may want to read more about **SOLID principles**, **Object Composition** and **Design Patterns**.

## Classes vs SQL

If you have worked with SQL, there is a striking parallel between SQL tables and classes.
Tables have columns, classes have attributes.
Tables have rows, classes have instances.
Both structure data.
Class diagrams are conceptually very close to Entity-Relationship (ER) diagrams used in the database world.

----

## Exercise

Turn the class diagram of the Snake class into skeleton code.
Leave all methods empty.

![Snake class diagram](images/class_snake.png)

----
## Further Reading

The class diagrams in this article were designed with the online tool [Creately](https://app.creately.com).
