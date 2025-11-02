
class A:
    foo="a"

class B:
    bar="b"

class C(A, B):
    pass


c = C()
type(c).mro()
