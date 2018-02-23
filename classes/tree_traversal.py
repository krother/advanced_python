"""
Example of a object architecture with classes.

Also see: Composite Pattern
"""

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
        
