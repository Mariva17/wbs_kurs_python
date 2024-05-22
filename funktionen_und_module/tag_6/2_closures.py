"""
Einsatz von einem Closure

"""


def family_greeter(last_name, first_name):
    print(f"Hallo {first_name} {last_name}")

family_greeter("vogt", "Katharina")
family_greeter("vogt", "Klaus")
family_greeter("vogt", "Michael")

print("*" * 40)

def family_greeter_closure(last_name):
    def inner(first_name):
        print(f"Hallo {first_name} {last_name}")
    return inner


vogt_greeter = family_greeter_closure("Vogt")
vogt_greeter("Katharina")
vogt_greeter("Klaus")   
