"""
args und kwags. Häuftiges Pattern beim Erstellen von

"""


def f(*args, **kwags):
    print(args)
    print(kwags)


f(1, 2, 31, 78, x=1, y=6, z=34)



def fn(a, *args, b, **kwags):
    print(f"{a=}")
    print(f"{b=}")
    print(args)
    print(kwags)


fn(1, 2, 31, 78, b=100, x=1, y=6, z=34)


def fn1(**kwags):
    
    print(kwags)

fn1(a=3, b=9)