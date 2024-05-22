"""
Name Mangling

"""
class A:
    def foo(self):
        self.bar()  # eigentlich sollte jetzt A.bar() aufgerufen werden, es wird ab B.bar() aufgerufen.
        self.__baz() # __ stellt sicher, dass auch wirklich A.__baz() aufgerufen wird!

    def bar(self):
        print("A.bar")

    def __baz(self):
        print("A.baz")

class B(A):
    def bar(self):
        print("B.bar")

    def __baz(self):
        print("B.baz") 


b = B()
b.foo()  # ruft fälschlicherweise b.bar() auf

print("*" * 40)

class C:
    def __init__(self) -> None:
        self.alfa = 1
        self._beta = 2
        self.__gamma = 3



a = C()

print(a.alfa)
print(a._beta)
print(vars(a))
#print(a._C__gamma)
#print(a.__gamma)