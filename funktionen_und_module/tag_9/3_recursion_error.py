import sys

print("recursion limit:" , sys.getrecursionlimit())


def fn():
    fn()


#fn()