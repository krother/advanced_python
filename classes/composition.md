
# Object Composition

Objects can be attributes of other objects.

You can use this mechanism to represent relationships between objects.
For instance you could model one-to-one, one-to-many or many-to-many relationships.
This has some similarity to database design, but with classes you have more options.

Object Composition is something you use in Python all the time, e.g. when you have a list of integers and refer to the first item of the list, you are accessing an `int` object inside a `list` object.

Modeling classes using Object Composition is one of the most important techniques in Object-Oriented-Programming.
Look up the terms **Object-Oriented-Design** and **Design Patterns** for further reading.

Here are two examples:

----

## Example 1: Bank

Imagine you want to have a `Bank` class that represents many accounts.

A very bad design solution would be:

    :::bash
    Bank is a subclass of Account

This violates **Liskovs Substitution Principle**.
A bank **is not** a special type of account!

A better design solution would be:

    :::bash
    A Bank contains many Accounts

An implementation could look like this:

    :::python3
    class Bank:

        def __init__(self):
            self.accounts = {}

        def add_account(self, number, accounts):
            self.accounts[number] = account


    barclays = Bank()
    ada = Account('Ada Lovelace', 100)
    barclays.add_account(1234, ada)
    barclays.add_account(5555, Account('Bob', 255))

----

## Example 2:Composite Pattern

In this exaple, `Node` objects contain other `Node` objects and `Leaf` objects to construct a tree.
The `traverse()` method walks across all nodes in the tree.

    :::python3
    class Node:

        def __init__(self, *args):
            self.subnodes = args

        def traverse(self):
            result = []
            for n in self.subnodes:
                result += n.traverse()
            return result


    class Leaf:

        def __init__(self, name):
            self.value = name

        def traverse(self):
            return [self.value]


    my_tree = Node(
                Node(
                    Node(
                        Leaf('gorilla'),
                        Node(
                            Leaf('chimp'), Leaf('human')
                            )
                        ),
                    Node(
                        Leaf('cat'),Leaf('dog')
                        ),
                    ),
                Node(
                    Node(
                        Leaf('chicken'),
                        Node(
                            Leaf('lizard'),Leaf('turtle')
                            ),
                        ),
                    Node(
                        Leaf('shark')
                        ),
                    )
                )

    print(my_tree.traverse())
