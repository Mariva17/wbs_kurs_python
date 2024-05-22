from functools import partial


def fn(event, b, c):
    print(event, b, c)


# Partielle Funktion erzeugen
fn = partial(fn, c=1)
fn(2, 3)
