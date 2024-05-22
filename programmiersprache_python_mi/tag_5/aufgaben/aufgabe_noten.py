"""
**Aufgabe: Statistik über Studentenleistungen**

Du bist ein Dozent an einer Universität und möchtest die Leistungen deiner Studenten in einem Kurs analysieren. 
Du hast eine Liste von Noten (zwischen 0 - 100) für jeden Studenten in deinem Kurs. Deine Aufgabe ist es, verschiedene Statistiken über die Noten zu berechnen.

Gegeben ist eine Liste `noten`, die die Noten der Studenten enthält:

noten = [80, 90, 75, 85, 95, 65, 70, 88, 92, 83]


1. Berechne den Durchschnitt (Mittelwert) der Noten.
2. Finde die höchste und niedrigste Note in der Liste.
3. Bestimme die Anzahl der Studenten, die eine Note über 90 erreicht haben.
4. Erstelle eine neue Liste `passing_grades`, die nur die Noten enthält, die größer oder gleich 70 sind.
5. Konvertiere alle Noten in Buchstaben (A, B, C, D, F) basierend auf folgender Skala:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: weniger als 60

"""
noten = [80, 90, 75, 85, 95, 65, 70, 88, 92, 83]
# 1.
print("Mittelwert von Noten: ", sum(noten) / len(noten))

# 2.
print("Höhste Note: ", max(noten))
print("Niedrigste Note: ", min(noten))

# 3.
noten_ueber90 = 0

for note in noten:
   if note >= 90:
      noten_ueber90 += 1

print("Die Anzahl der Studenten, die eine Note über 90 erreicht haben:", noten_ueber90)

# 4.
passing_grades = []

for note in noten:
   if note >= 70:
      passing_grades.append(note)
print("Liste passing_grades: ", passing_grades)

# 5
noten_buchstaben = []

for note in noten:
   if 90 <= note <= 100:
      noten_buchstaben.append("A")
   elif 80 <= note <= 89:
      noten_buchstaben.append("B")
   elif 70 <= note <= 79:
      noten_buchstaben.append("C")
   elif 60 <= note <= 69:
      noten_buchstaben.append("D")
   elif note < 60:
      noten_buchstaben.append("F")
print("Noten in Buchstaben: ", noten_buchstaben)