
# Classes

## What are classes?

Classes are a tool to manage complexity in a program.
They group two things in a single structural unit: **attributes (data)** and **methods (behavior)**.

In more simple terms, you can use a class to stuff complexity into it, so that your main program becomes simple. In my opinion, this way of structuring code should be the main motivation to using classes in Python.

In this article, you find an example how to use a class to structure your code.

----

## Defining a class

To define a class, you need to define three things:

* give the class a name (in `SnakeCase`)
* define attributes (variables that belong to the class)
* define methods (functions that belong to the class)

In the code below, a class for a bank account is defined:

    :::python3
    class Account:
        """
        Account of a bank client.
        """
        def __init__(self, owner, start_balance=0):
            self.name = owner
            self.balance = start_balance

        def deposit(self, amt):
            self.balance += amt

        def withdraw(self, amt):
            self.balance -= amt

The class `Account` contains two attributes (`name` and `balance`) and two methods (`deposit` and `withdraw`).

Note that you need to add the word `self` every time you refer to an attribute.
You also must use `self` as the first parameter in every method of a class.

----

## Creating Objects

To use a class, you need to create an object from it first.
Objects are *"live versions"* of a class, the class being an idealized abstration (in the sense of [Platos Theory of Forms](https://en.wikipedia.org/wiki/Theory_of_forms)).
If you think of **Human** as a class, **Ada Lovelace** and **Mahatma Gandi** would be objects.

You can create multiple objects from a class, and each objects has its own, independent attributes
(e.g. if **Human** has an attribute **age**, the age of **Ada** and **Mahatma** might be different).

Syntactically, you can think of a class as a function that returns objects.
(This is a gross oversimplification to what textbooks on classes say, but in Python it is more or less what happens).

To create `Account` objects, you need to call the class.
Creating an object will automatically call the constructor `__init__(self)` with the parameters supplied.

    :::python3
    a = Account('Ada Lovelace', 1234)
    m = Account('Mahatma Gandhi', 10)

Then you can access the attributes like any variable using the dot (`.`) syntax:

    :::python3
    print(a.name)
    print(m.balance)

And you can call methods in a similar way:

    :::python3
    a.deposit(100)
    a.withdraw(10)
    print(a.balance)

Note that these methods modify the state of *Adas* account object, but not *Mahatmas*.  

----

## Making classes printable

One disadvantage of classes is that when you print an object, you will see something like this:

    :::bash
    <__main__.Account at 0x7f64519d8438>

A good workaround is to add a special method, `__repr__(self)` to the class that returns a string.
This method will be called every time a string representation is needed: when printing and object, when an object appears inside a list or in error messages.

Typically, you would build a short string in `__repr__(self)` that describes the object:

    :::python3
        def __repr__(self):
            return f"<Account of '{self.name}' with {self.balance} galactic credits>"

With this method defined, the instruction

    :::python3
    print(a)

would result in the output

    :::bash
    <Account of 'Ada Lovelace' with 1324 galactic credits>"

It is a good idea to implement `__repr__(self)` as the first method in a new class.


----

## Caveats

In other programming languages classes are often advertised for *"modeling real-world objects or logical entities"*. This is partially true in Python. Note that Python offers a lot of alternatives to using classes, e.g. dictionaries, named tuples or DataFrames may often serve the same purpose equally well.

Another motivation for using classes you find in textbooks is **encapsulation**, isolating parts of your program from the rest. Encapsulation does not exist in Python (e.g. you cannot declare parts of a class as `private` in a way that cannot be circumvented). If you depend on your code being strictly isolated from other parts (e.g. in a security-critical application or when organizing a very large program), **consider other programming languages than Python.**

----

## Dirty Tricks

On the other hand, Python allows using classes in multiple creative ways. I call them **dirty tricks**.
Most of them have their uses in larger programming libraries. But if you are writing a smaller program, they probably do more harm than good.

Especially if you are still learning about classes, consider yourself warned of the following tricks:

* Multiple Inheritance
* Operator Overloading
* Metaclasses
* Monkey Patching

These dirty tricks are likely to mess up your program.
Do not use any of them unless you really know what you are doing!
