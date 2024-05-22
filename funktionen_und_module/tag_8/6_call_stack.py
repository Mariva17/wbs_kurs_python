"""
Call Stack

"""

def f():
    print("ich bin f")
    3 / 0 # ZeroDivisionError
    

def fn():
    print("ich bin fn")
    f()


def g():
    print("ich bin g")
    fn()

    

def main():
    print("main")
    g()
    # a()
    # b()


try:
    main()   
except Exception as e:
        print(e, type(e))

print("hier gehts weiter")