
# Inheritance

Classes can extend other classes.
In that case, the subclass (the inheriting one) will have all the attributes and methods of the other class.

A subclass can also replace attributes methods of the superclass.
If you want to use both inherited and new

The most important design principle when using inheritance is **Liskovs Substitution Principle**.
It says that you should be able to use a subclass instead of its superclass.

The second important design principle is to avoid excessive subclassing.
Most of the time **Object Composition** is the better idea.

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

Using the subclass is very similar to using the superclass:

    :::python3
    b = SavingsAccount('Betty', 100, interest_rate=1.03)
    print(b)

    b.deposit(100)  # calls Account.deposit()
    print(b)        # calls Account.__repr__()

    b.add_interest()  # calls SavingsAccount.add_interest()
    print(b)

----

## Abstract Base Classes

If you want to use inheritance but not allow instances of the superclass, you can use the **ABC Metaclass**.
With `ABCMeta`, you need to create a subclass that overwrites all abstract methods and properties:

    :::python3
    from abc import ABCMeta, abstractmethod, abstractproperty

    class AbstractAnimal(metaclass=ABCMeta):

        @abstractmethod
        def make_noise(self):
            pass

        # an abstract read-only-property
        @abstractproperty
        def species(self):
            pass

        # abstract read/write property
        def getname(self):
            pass

        def setname(self, value):
            pass

        name = abstractproperty(getname, setname)

        # non-abstract method
        def is_alive(self):
            return True

### Exercise

Implement the Dog class so that the code below runs.

    :::python3
    class Dog(AbstractAnimal):

        ...

    rex = Dog()
    rex.name = 'Rex'
    print(rex.is_alive())
    rex.make_noise()
    print(rex.species())
