"""
assert => Behauptung
wird hauptsächlich beim Testen oder Entwickeln
weniger geeignet für Produktiv-Code
"""


class A:
    __c = 2

    def __b(self):
        self.__x = 2
        self.__class__.__name__


class B:
    pass


class C(A, B):
    pass


print(C.__bases__)  # Basisklassen


print(ord("A"))
"\n"


def summe(a, b):
    return a + b


def test_summe():
    assert summe(2, 2) == 4, "2 + 2 muss 4 sein"
    assert summe(-1, 1) == 0


test_summe()
