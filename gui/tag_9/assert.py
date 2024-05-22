"""
assert => Behauptung
wird haupsachlich beim Testen oder Entwickeln

"""

def summe(a, b):
    return a + b


def test_summe():
    assert summe(2, 2) == 5, "2 + 2 muss 4 sein"
    assert summe(-1, 1) == 0


test_summe()