class MonkeyPack(type):
    """A self-expanding horde of monkeys"""

    def __new__(mcs, name, bases, dict):
        cls = type.__new__(mcs, name, bases, dict)

        def wrapper(*args):
            instance = []
            for i in range(1, args[0]+1):
                monkey = cls(f'monkey #{i}')  # calls __init__
                instance.append(monkey)
            return instance

        return wrapper


class Monkey(metaclass=MonkeyPack):
    """A monkey never comes alone"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<{self.name}>"


monkeys = Monkey(7)        # calls __new__
print(monkeys)             # see what happens!