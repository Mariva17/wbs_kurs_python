"""
for loop

"""
wizards = ["gandalf", "saruman"]
for index, wizards in enumerate(wizards):
    print(index, wizards)

for x in range(3):
    print(x)

# Suche: wenn das Suchwort gefunden ist, breche Iteration ab.
for x in range(1_000_000):
    if x == 50:
        print(x)
        break
    print(".", end="")


for i in range(4):
    for k in range(4):
        print("k:", k)
    print("i:", i)

# continue bricht nur den aktuellen Schleifendurchlauf ab
for x in range(10):
    if x % 2 == 0:
        print(x**2)
        continue # gehe zum nächsten Iterationsschritt
        print("------------------") # wird nie ausgeführt
    print("ungerade zahl:", x)