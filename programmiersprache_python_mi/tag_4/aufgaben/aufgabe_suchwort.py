"""(Leicht)
Schreibe ein Python-Programm, das folgende Anforderungen erfüllt:

- Eine variable satz definiert, die einen beliebigen Satz als String enthält.
- Eine variable suchwort definiert, die das zu suchende Wort als String enthält.
- Die find-Methode verwendet, um zu überprüfen, ob suchwort im satz vorhanden ist.
- Eine Ausgabe erzeugt, die angibt, ob das suchwort gefunden wurde oder nicht.
- Der Suchbegriff kann auch nur ein Teil eines Wortes sein.

Wenn das suchwort gefunden wurde, soll die Position (Index) des ersten
Buchstabens des suchwort im satz ausgegeben werden.

Beispiel:
satz = "Python ist eine tolle Programmiersprache"
suchwort = "Programmiersprache"
das suchwort "Programmiersprache" wurde gefunden an Position 22

satz = "Python ist eine tolle Programmiersprache"
suchwort = "is"
das suchwort "is" wurde gefunden an Position 7

satz: "Python ist eine tolle Programmiersprache"
suchwort: "Zeiger"
das suchwort "Zeiger" wurde nicht gefunden

Erweiterung:
Nutze input um den Satz und das Suchwort vom Benutzer eingeben zu lassen.
"""
satz = "Python ist eine tolle Programmiersprache"
print(satz)
suchwort = input("Bitte geben Sie ein Wort ein: ")


position = satz.find(suchwort)
if  position != -1:
    print(f"Das suchwort {suchwort} wurde gefunden an Position {position}.")
else:
    print(f"Das suchwort {suchwort} wurde nicht gefunden.")