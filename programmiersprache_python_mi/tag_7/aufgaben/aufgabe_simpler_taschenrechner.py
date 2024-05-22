"""
Programmiere einen simplen Taschenrechner mit den 4 Grundrechenarten.

Der Taschenrechner soll in einem unendlichen Loop laufen.
Wenn der eingegebene Operator "q" ist, soll das Programm abbrechen.
Division durch 0 soll nicht möglich sein, das Programm soll deshalb aber auch
nicht abbrechen, sondern es soll eine User-Meldung kommen: Division durch Null ist nicht möglich.

Eine Eingabe könnte so aussehen:

---Beispiel 1-------------
Bitte gebe die gewünschte Operation ein (q für Abbruch): 2 + 3.2
Das Ergebnis ist: 5.2

---Beispiel 2-------------
Bitte gebe die gewünschte Operation ein (q für Abbruch): q
good bye...
"""


while True:
    result = 0
    user_input = input("Bitte gebe die gewünschte Operation ein (q für Abbruch): ").split()
    
    if user_input[0] in ["q", "quit", "exit"]:
        print("Goodbye!")
        break
    
    if len(user_input) == 3:
        a = float(user_input[0]) 
        b = float(user_input[2])
        
    else:
        print("Arguments missing")
        continue
         

    if user_input[1] == "+":
        result = a + b
    elif user_input[1] == "-":
        result = a - b
    elif user_input[1] == "*":
        result = a * b
    elif user_input[1] == "/":
        if b == 0:
            print("Division durch Null ist nicht möglich.")
            continue
        result = a / b   
    
    print("Das Ergebnis ist: ", result)

        
    
         
   