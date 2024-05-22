"""
Closure: 

"""

def outer():
    def inner():
        print("inner")

    print("outer")
    return inner

inner_function = outer() # outer
print(inner_function) 
inner_function() # inner()


# Closure

def outer_2(x):
    def inner(y):
        return x * y

    return inner

inner_function2 = outer_2(x=10)
result = inner_function2(y=4)
print("result von inner_function2:", result)
