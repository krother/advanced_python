
class Account:
    """
    Account for a bank client.
    """
    prefix = 'GIRO'

    def __init__(self, newname, balance=0):
        self.name = newname
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def __str__(self):
        return "{} | {:10s}:{:10.2f}".format(self.prefix, self.name, self.balance)

    @staticmethod
    def info_text():
        """Static methods belong to a class, but know nothing about it."""
        return """This is a bank account. It keeps your money safe."""

    @classmethod
    def prefix_text(cls):
        """Class methods belong to a class, but know nothing about its instances."""
        return """Bank account has the prefix: {}.""".format(cls.prefix)


if __name__ == '__main__':
    a = Account('Adam', 100)
    print(a)
    
    a.deposit(50)
    print(a)

    a.withdraw(10)
    print(a)

    print(a.info_text())
    print(a.prefix_text())

    print(Account.info_text())
    print(Account.prefix_text())
