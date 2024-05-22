"""
Zip Funktion

"""

grades = [3, 5, 1, 2, 4]
students = ["Bob", "Alice", "Mallory", "Trudy", "Peter"]
ages = [22, 32, 40, 25, 16]

# Zip: für jeden Index wird ein Tupel zur Verfügung gestellt
for student, grade in zip(students, grades):
    print(student, grade)
print()

# mit enumerate
for index, (student, grade) in enumerate(zip(students, grades)):
    print(index, student, grade)

print()

zip_objekt = zip(students, grades)
print(next(zip_objekt))
print(next(zip_objekt))

print()

# in einem Schritt Listen in ein Dict unwaldeln
student_dict = dict(zip(students, grades))
print(student_dict)

print("---------------------------")

d = {}

for student, grade, age in zip(students, grades, ages):
   # print(student, grade, age)
    d[student] = {
        "age": age,
        "grade": grade
    }
print(d)

products = ["tshirt", "jeans"]
prices = [21.5, 45.99]
amounts = [3, 1]

for product, price, amount in zip(products, prices, amounts):
    print(f"{product} Total", price * amount)

