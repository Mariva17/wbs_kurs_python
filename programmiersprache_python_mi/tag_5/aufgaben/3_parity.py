"""
Pruefbit (schwer)

# Das letzte (von 8) Bit wird in der 7-Bit Übertragung häufig als Paritätsbit (Prüfbit) verwendet.
Das SMTP-Protokoll nutzt auch heute noch eine 7-bit Kodierung für die Übertragung
von plain-Text Emails.

1 Byte = 8 bit
01000011
       ^
-------|
      parity-bit


wenn die Summe der ersten 7 bit gerade (even) ist, muss prüfbit 1 sein
wenn die Summe der ersten 7 bit ungerade (odd) ist, muss prüfbit 0 sein
Wenn das nicht zutreffen sollte, hat sich bei der Datenübertragung ein
Fehler eingeschlichen. 

m = [
    [0, 1, 1, 0, 1, 1, 0, 1], # richtig (Paritätsbit 1), Summe der 7 Bit: 4
    [0, 0, 0, 0, 0, 1, 0, 0], # richtig (Paritätsbit 0), Summe der 7 Bit: 1
    [0, 0, 0, 0, 1, 1, 0, 0], # falsch (Paritätsbit 0), Summe der 7 Bit: 2
    [0, 0, 0, 1, 1, 1, 0, 1], # falsch (Paritätsbit 1), Summe der 7 Bit: 3
]

Hintergrund:
https://de.wikipedia.org/wiki/Hamming-Code
https://de.wikipedia.org/wiki/Parit%C3%A4tsbit

prüfe iterativ, in welchen Zeilen sich ein Fehler in der Übertragung befindet.
Hinweis: falls zwei Fehler in einer Zeile sind, kann die Parity-Prüfung fehlschlagen.

Beispiel:
--------------
In den folgenden Zeilen kamen Fehler vor:
Zeile 2: [0, 0, 0, 1, 1, 0, 0, 0] expected: 1 real: 0
Zeile 3: [0, 0, 1, 1, 1, 0, 0, 1] expected: 0 real: 1
"""
m = [
    [1, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1],
]


for x in m:
    if sum (x[:-1]) %2 == 0  and x[-1] == 1:
        print ("gibt es keinen Fehler und Prüfbit ist 1")
    if sum (x[:-1]) %2 != 0 and x[-1] == 0:
        print ("gibt es keinen Fehler und Prüfbit ist 0")
    if (sum (x[:-1]) % 2 == 0 and x[-1] == 0 ) or (sum (x[:-1]) % 2!= 0 and x[-1] == 1):
        print("Datenübertragung ein Fehler eingeschlichen")


