
# Inheritance

Classes can extend other classes.
A **subclass** will have all the attributes and methods of a **superclass**.
You can say the subclass inherits from the superclass.

A subclass can define new methods and attributes.
It can also replace methods of the superclass.

The most important design principle when using inheritance is **Liskovs Substitution Principle**.
It says that you should be able to use a subclass whereever the superclass is used.

----

## Example

Here you find an example using the `Account` class defined earlier.

    :::python3
    class SavingsAccount(Account):

        def __init__(self, owner, start_balance=0, interest_rate=1.0):
            super().__init__(owner, start_balance)
            self.interest_rate = interest_rate

        def add_interest(self):
            self.balance *= self.interest_rate

        def withdraw(self, amount):  # replaces Account.withdraw
            print('**extra identification approved**')
            super().withdraw(amount)

The `super()` function returns an instance of the superclass, so that you can call the inherited methods, even if you are replacing them.

Using the subclass is very similar to using the superclass:

    :::python3
    b = SavingsAccount('Betty', 100, interest_rate=1.03)
    print(b)

    b.deposit(100)  # calls Account.deposit()
    print(b)        # calls Account.__repr__()

    b.add_interest()  # calls SavingsAccount.add_interest()
    print(b)

----

## Caveats

Once you get the hang of object-oriented programming, inheritance is not that difficult.
At some point, it is very tempting to define lots of subclasses, and class hierarchies with multiple levels.
Most of the time, having one level of inheritance is enough.
Many times you do not need inheritance at all, and you are better off using **object composition**.

Python allows to use **multiple inheritance** (i.e. a subclass with more than one superclass).
Avoid writing your own multiple inheritance hierarchy unless you know exactly what you are doing.
