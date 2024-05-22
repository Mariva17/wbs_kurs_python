"""(MITTEL)
Die derzeitigen Regeln zur Bestimmung, ob ein Jahr ein Schaltjahr ist, lauten wie folgt:

- Kann man die Zahl durch 4 teilen? Wenn ja, dann ist das Jahr unter Umständen ein Schaltjahr.
  2200 / 4 = 550. Es besteht also den ersten Test und wird vorläufig zum
  Schaltjahr erklärt. Es folgen aber noch zwei weitere Regeln.

- Wenn man die Jahreszahl durch 100 ohne Rest (modulo) teilen kann,
  ist das Jahr kein Schaltjahr.
  2200 / 100 = 22. Obwohl Regel 1 erfüllt ist, handelt es sich also nicht um
  ein Schaltjahr.

- Wenn man das Jahr durch 400 teilen kann, dann ist es ein Schaltjahr, auch
  wenn es durch 100 teilbar ist. 2200 / 400 = 5.5. Großer Fehler hier! 2200 ist
  nicht durch 400 teilbar, also greifen wir auf Regel 2 zurück und erklären das
  Jahr zu einem NICHT-Schaltjahr.

Beispiel:
Bitte gebe eine Jahreszahl ein: 2200
Das Jahr 2200 ist kein Schaltjahr.
"""
jahr = int(input("Bitte gebe eine Jahreszahl ein: "))
if jahr % 400 == 0:
  print("Das Jahr", jahr, "ist ein Schaltjahr.")
elif jahr % 100 != 0 and jahr % 4 == 0:
  print("Das Jahr", jahr, "ist ein Schaltjahr.")
else:
  print("Das Jahr", jahr, "ist kein Schaltjahr.")


