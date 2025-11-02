
import random


class Dynamic:
    """
    A class without attributes apart from a dictionary.
    Everything is created dynamically.
    """
    def __init__(self):
        self._fields = {}

    def __getattr__(self, name):
        if name == "dice":
            return random.randint(1, 6)
        elif name == "fish":
            return random.choice(["salmon", "herring", "shark", "dorada"])
        else:
            return self._fields.get(name, 42)
        
    def __setattr__(self, name, value):
        if name.startswith("x"):
            self._fields[name[1:]] = value
        else:
            super().__setattr__(name, value)


if __name__ == "__main__":
    dyn = Dynamic()
    print(dyn.dice)
    print(dyn.fish)
    print(dyn.foo)
    dyn.xdolphin = True
    print(dyn.dolphin)
    print()
