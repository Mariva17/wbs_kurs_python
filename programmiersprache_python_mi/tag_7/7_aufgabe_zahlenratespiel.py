"""
Aufgabe:

Zahlenratespiel

Der User muss eine Zufallszahl erraten. 
Falls er die Zahl richtig errät, ist das Spiel beendet.
Bei Fehlversuch darf er erneut raten. Es gibt n Rateversuche.

"""
import random 

MAX_RATEVERSUCHE = 3

zufallszahl = random.randint(1, 6)
rateversuche = 1

while rateversuche <= MAX_RATEVERSUCHE:
    user_input = input("Bitte geben Sie eine Zahl ein : ")
    if user_input.isdigit():
        rateversuche += 1
        user_input = int(user_input)
        if user_input == zufallszahl:
            print(user_input, "Sie haben geraten! Bravo!")
            break
        elif user_input != zufallszahl:        
            print("Sie haben leider nicht geraten!")
    else:
        print("Ungültige Eingabe")
              
else:
    print("Die maximale Anzahl an Ratenversuchen ist erreicht. Goodbye!")

