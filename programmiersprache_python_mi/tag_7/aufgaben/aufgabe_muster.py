""" 
mittel

(Mustererzeugung). Schreiben Sie ein Programm, das mit Hilfe von
Schleifen das folgende Muster erzeugt:

Eingabe: 5

*
**
***
****
*****
****
***
**
*

Eingabe: 3

*
**
***
**
*

"""

user_input = int(input("Bitte gebe ein Zahl ein: "))
for i in range(1, user_input + 1):
    print("*" * i)
    
for i in range(user_input-1, 0, -1):
    print("*" * i)
