"""
Verschachtelte Scope

"""

def outer():
    x = 1
    print("x aus outer: ", x)

    def inner():
        # verschachtelter Scope
        p = 3
        nonlocal x
        x = x + 1
        print("p aus inner: ", p)

        def most_inner():
            nonlocal x
            x = x + 50

        most_inner()
    inner()

    # print(p)

    print(locals())

outer()