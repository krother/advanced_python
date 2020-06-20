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


    @property
    def interest_rate(self):
        return self.__interest

    @interest_rate.setter
    def interest_rate(self, interest):
        self.__interest = interest
