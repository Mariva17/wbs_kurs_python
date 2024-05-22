"""
Zugriff auf Note eines Schülers

"""

grades = [3, 5, 1, 2, 4]
students = ["Bob", "Alice", "Mallory", "Trudy", "Peter"]

# von welchem Schüler möchtest du die Note wissen?

user_input = "Alice"

for index, student in enumerate(students):
    if student == user_input:
        print(f"Die Note von {user_input} ist {grades[index]}")