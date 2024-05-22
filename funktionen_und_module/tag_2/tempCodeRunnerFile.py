def f(*args, **kwags):
    print(args)
    print(kwags)


f(1, 2, 31, 78, x=1, y=6, z=34)