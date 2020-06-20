
# Inheritance
Example for classes, properties and inheritance

Exercise:
1) make the balance a property as well.
2) make it impossible for the interest rate to go above 20%
"""

        @staticmethod
        def info_text():
            """Static methods belong to a class, but know nothing about it."""
            return """This is a bank account. It keeps your money safe."""

        @classmethod
        def prefix_text(cls):
            """Class methods belong to a class, but know nothing about its instances."""
            return """Bank account has the prefix: {}.""".format(cls.prefix)


from account import Account


class SavingsAccount(Account):

    prefix = 'SAVINGS:'

    def __init__(self, newname, interest):
        super().__init__(newname, 0)
        self.__interest = interest

    @property
    def interest_rate(self):
        return self.__interest

    @interest_rate.setter
    def interest_rate(self, interest):
        self.__interest = interest

    def add_interest(self):
        self.balance *= self.interest_rate

    def withdraw(self, amount):
        print('**extra identification step approved**')
        super().withdraw(amount)


if __name__ == '__main__':
    b = SavingsAccount('Betty', interest=1.03)
    print(b)

    b.deposit(100)
    print(b)

    b.withdraw(50)
    print(b)

    b.add_interest()
    print(b)

    b.interest_rate = 1.06    
    b.add_interest()
    print(b)

    # print(b.__interest)



## Abstract Base Classes

If you want to use inheritance but not allow instances of the superclass, you can use the **ABC Metaclass**.
With `ABCMeta`, you need to create a subclass that overwrites all abstract methods and properties:

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

    class Dog(AbstractAnimal):

    ...

    rex = Dog()
    rex.name = 'Rex'
    print(rex.is_alive())
    rex.make_noise()
    print(rex.species())
