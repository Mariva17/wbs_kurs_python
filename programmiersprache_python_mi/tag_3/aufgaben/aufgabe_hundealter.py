"""(mittel)
Allgemein rechnet man Hundejahre in Menschenjahre um, indem man das Alter des Hundes
mit 7 multipliziert. Je nach Hundegröße und Rasse sieht die Umrechnung jedoch
etwas komplizierter aus, z.B.:

- Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
- 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
- Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger Methode
berechnet, welchem Alter in Menschenjahren das entspricht.
Beachte, dass ein Hund mindestens 1 Jahr alt sein muss!

Ein Hund mit drei Jahren ist also 22 + ((3 - 2) * 5) Jahre alt.
Falls ein Hund jünger ist als 1 Jahr, sollte die Meldung ausgegeben werden: Hund muss mindestens ein Jahr alt sein.
"""
hundenjahre = int(input("Bitte geben Sie das Alter eines Hundes: "))

if hundenjahre == 1:
    alter_menschen = 14
    print(alter_menschen, "Menschenjahre")
elif hundenjahre == 2:
    alter_menschen = 22
    print(alter_menschen, "Menschenjahre")
elif hundenjahre > 2:
    alter_menschen = 22 + ((hundenjahre - 2) * 5)
    print(alter_menschen, "Menschenjahre")
else:
    print("Hund muss mindestens ein Jahr alt sein.")