"""
Berechne den Body-Mass-Index: (LEICHT)

Der Body-Mass-Index (kurz: BMI) ist eine Zahl, mit der man abschätzen kann,
ob man Unter-, Normal oder Übergewicht hat. Man berechnet diese Zahl nach der folgenden Formel:

          Gewicht (kg)
BMI = ---------------
       Größe (m) * Größe (m)

WICHTIG:
Dabei wird das Gewicht in kg und die Größe in m angegeben.

AUFGABE:
-----------
über Input wird das Gewicht in Gramm (g) eingegeben und die Höhe in cm. Rechne
die Eingabewerte entsprechend um (zb. g in kg) und berechne das Ergebnis. Lege dafür passende
Variablen an.

Wir gehen von legalem und validem Input aus.
Runde auf zwei Nachkommastellen.

Überprüfen:
Der Body-Mass-Index (BMI) für eine Person, die 95 kg wiegt und 1,80 Meter groß ist, beträgt etwa 29,32.
"""
print("Hallo User! Willkommen zum Body-Mass-Index Berechnung!")
gewicht = input("Bitte gebe dein Gewicht in Gram(g) ein: ")
größe = input("Bitte gebe deine Höhe in cm. ein: ") 
gewicht = int(gewicht) / 1000
größe = int(größe) / 100
bmi = gewicht / (größe ** 2)
print(round(bmi, 2))