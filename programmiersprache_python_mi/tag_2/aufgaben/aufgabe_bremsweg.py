"""
Anhalteweg: (LEICHT)

Es gibt folgende Faustformeln zur Berechnung von Anhaltewegen:

Reaktionsweg (in Metern) = (Geschwindigkeit (in km/h) geteilt durch 10) mal 3

Bremsweg (in Metern) = (Geschwindigkeit (in km/h) geteilt durch 10) mal (Geschwindigkeit (in km/h) geteilt durch 10)

Anhalteweg (in Metern) = Reaktionsweg plus Bremsweg

Eingabe: km/h (via input-funktion)

Gebe den Reaktionsweg, den Bremsweg und den Anhalteweg
entsprechend der km/h aus. Hinweis: 124.4 ist ein gültiger Eingabewert.

Quelle: https://www.adac.de/verkehr/rund-um-den-fuehrerschein/erwerb/anhalteweg-berechnen/
"""

print("Hallo User! Willkommen zum Anhaltewegsberechnung!")
geschwindigkeit = input("Bitte gebe dein Geschwindigkeit (in km/h) ein: ")
geschwindigkeit = float(geschwindigkeit)
reaktionsweg = geschwindigkeit / 10 * 3
bremsweg = (geschwindigkeit / 10) * (geschwindigkeit / 10)
anhalteweg = reaktionsweg + bremsweg
print("Reaktionsweg: ", round(reaktionsweg, 2), "Meter")
print("Bremsweg: ", round(bremsweg, 2), "Meter")
print("Anhalteweg: ", round(anhalteweg, 2), "Meter")