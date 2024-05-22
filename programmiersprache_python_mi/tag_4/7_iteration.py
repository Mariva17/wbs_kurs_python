"""
Iteration - Schleifen

"""
students = ["Bob", "Alice", "Trudy"]
noten = [1, 2, 3]
ages = [21, 25, 23]

for student in students:
    print(student)

print("hier ist Iteration beendet")

# eine Liste Filtern (leere Liste anlegen und in Iteration neue Liste füllen)
THRESHOLD = 30
temperatures = [34, 23, 12, 11, 4, 42, 33]
temperatures_filtered = []
for temp in temperatures:
    if temp >= THRESHOLD:
        temperatures_filtered.append(temp)
print(temperatures_filtered)

# klassisch / oldschool
count = 0
for student in students:
    print(student, noten[count], ages[count])
    # count = count + 1
    count+=1

print("*" * 30)

# enumerate. Pythonische Variante
for index, student in enumerate(students):
    print(student, noten[index], ages[index])

# Enumerate Objekt (ist ein Iterator)
x = enumerate(students)
print(next(x))
print(next(x))