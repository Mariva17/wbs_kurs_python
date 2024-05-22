"""
(MITTEL)
Gegeben ist eine Variable x im globalen Scope.
Schreibe eine Funktion increment, die x im globalen Scope um eins erhöht.


"""
x = 4

def fn():
    global x
    x += 1

fn()
print("x global: ", x)

