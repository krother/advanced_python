"""
Metaclasses: Crazy stuff you can do with classes.

Instructions: 
1) Run the code
2) Admire what is happening
3) Don't try this at work, unless you have excluded all alternatives
   and you really know what you are doing 
   and you have talked to at least one sane person.
"""

class monkeymeta(type):

    def __new__(mcs, name, bases, dict):
        cls = type.__new__(mcs, name, bases, dict)

        def wrapper(*args):
            instance = cls('monkeys')
            instance.monkeys = args[0]
            return instance

        return wrapper


class CrazyMonkeys(metaclass=monkeymeta):
    """
    Class with monkeys appearing out of nowhere
    """
    def __init__(self, name):
        self.name = name


monkeys = CrazyMonkeys(12)
print(monkeys.monkeys, monkeys.name)

