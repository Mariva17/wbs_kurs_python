"""
Userinput: User gibt eine Zahl ein
wir prüfen, ob die Zahl in der folgenden Menge enthalten ist

entweder im Bereich [45, 99],
oder im Bereich [0, 15],
oder im Bereich [17, 43],

falls das zutrifft, kommt meldung: Zahl ist in der Menge der erlaubten
zahlen enthalten, ansonsten, Zahl unbekannt
"""

x = input("Bitte gebe eine Zahl ein: ")
x = int(x)

if 45 <= x <= 99:
    print("Zahl ist in der Menge der erlaubten zahlen enthalten")
elif 0 <= x <= 15:
    print("Zahl ist in der Menge der erlaubten zahlen enthalten")
elif 17 <= x <= 43:
    print("Zahl ist in der Menge der erlaubten zahlen enthalten")
else:
    print("Zahl unbekannt")            