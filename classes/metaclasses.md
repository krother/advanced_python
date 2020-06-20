
# Metaclasses

**WARNING: This code is meant to drive you nuts!**

Metaclasses change the way objects are created.
That is, instead of simply calling `__init__()` something else might happen without you knowing it.

They are an ugly, incoherent, intransparent construct that exploits everything Python offers.

----

## Valid Use Cases:

* writing an ORM like **Django models** or **SQLAlchemy**
* hijacking internal Python logic (e.g. like **pytest** does)
* emulating JavaScript-like objects (the Prototype pattern)
* showing off

----

## Instructions

1. run the code
2. admire what is happening
3. try to understand what is happening
4. return to 1

Here is the code

    :::python3
    class CrazyMonkeyPack(type):

        def __new__(mcs, name, bases, dict):
            cls = type.__new__(mcs, name, bases, dict)

            def wrapper(*args):
                instance = []
                for i in range(1, args[0]+1):
                    monkey = cls(f'monkey #{i}')  # calls __init__
                    monkey.state = 'crazy'  # monkey-patches the state attribute
                    instance.append(monkey)
                return instance

            return wrapper


    class CrazyMonkeys(metaclass=CrazyMonkeyPack):
        """A self-expanding horde of monkeys"""
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f"<{self.name} ({self.state})>"


    monkeys = CrazyMonkeys(3)  # calls __new__
    print(monkeys)             # see what happens!

----

## Final Warning

Don't try this at work, unless

* you have excluded all alternatives
* you really know what you are doing
* you have talked to a developer more experienced than you
