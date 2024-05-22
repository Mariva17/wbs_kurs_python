"""
Mehrfach - Vererbung.

Method Resolution Order (MRO): C3 Linearisierung

"""

class A:
    def say_hello(self):
        print("Ich bin A")


class B:
    def say_hello(self):
        print("Ich bin B")


class C(A, B):
    pass



c = C()
c.say_hello()

# Method Resolution Order (Auflösung der Methoden)
print(C.mro())