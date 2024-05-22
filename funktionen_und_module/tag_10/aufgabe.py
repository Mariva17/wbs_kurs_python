"""
Gegeben ist eine CSV-Datei mit 4 numerischen, ganzzahligen Spalten (diese Datei findet ihr in Unterrichtsmaterial/tag_10/data.csv).

Diese Datei soll eingelesen und die Spaltenwerte pro Reihe jeweils summiert werden. Gesucht ist der Gesamtwert, der sich durch das Summieren aller Spalten und Zeilen ergibt.

Falls sich in einer Zeile ein nicht-numerischer Wert befinden sollte, der nicht zu einer Ganzzahl konvertiert werden kann, 
soll die Berechnung für diese Zeile übersprungen werden.

Die Zahl der übersprungenen Zeilen muss später ausgegeben werden.

Beispiel für eine CSV-Datei

3, 3, 3, 3

1, 2, 3, 5

3, 2, a, 3

Bei drei Reihen und 4 Spalten wäre der Gesamtwert 12 (1.Reihe) + 11 (2. Reihe) = 23
die letzte Reihe kann nicht konvertiert werden (Gesamtzahl übersprungener Reihen = 1)

eine legale Reihe sieht so aus (sie enthält nur Zahlen):

3,7,0,7

Diese Zeile hingegen beinhaltet einen Wert, der nicht konvertiert werden kann. Sie soll bei der Zählung übersrpungen werden.

3,7,0,a

Die Frage ist:

Was ist die Summe aller Zahlen der validen Zeilen?

Wieviele Zeilen mussten übersprungen werden, da ein nicht-numerischer Wert vorkam?

Hinweis: der Header soll nicht als fehlerhaft gezählt und beim Einlesen einfach ignoriert werden.

	Gesamt: 22840, fehlerhafte Zeilen: 38 ***
	Gesamt: 32840, fehlerhafte Zeilen: 37
	Gesamt: 11840, fehlerhafte Zeilen: 38
	Gesamt: 32840, fehlerhafte Zeilen: 38


"""

from pathlib import Path
import csv

BASE_PATH = Path(__file__).parent

def load_data(filename):
    with open(BASE_PATH / filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)
            
        data = list(reader)
    return data

#data = load_data("data.csv")
#print(load_data("data.csv"))

def filtered_data(data):
    counter = 0
    sum_data = 0
    for value in data:
        if all(map(lambda i: i.isdigit(), value)):
            value = list(map(int, value))
            sum_data = sum_data + sum(value)         
        else:
            counter += 1         
 
    return print(f"Gesamt: {sum_data}, fehlerhafte Zeilen: {counter}")


def main():
    list_data = load_data("data.csv")
    result = filtered_data(list_data)

    return result

if __name__ == "__main__":
    main()
