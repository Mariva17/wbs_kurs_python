"""
(MITTEL)
Lese die Daten aus log.txt und bereinige die Zahlen von allen anderen Zeichen.
Leerzeichen lösche raus.

Speichere die veränderten Daten in eine Datei log_clean.txt

IST:
24343#
34341 #
3422 #

24323#

SOLL:
24343
34341
3422
24323

Nutze dazu folgenden vordefinierten Funktionen.
Man kann davon ausgehen, dass die log.txt 1000 Einträge nicht übersteigt, der
Content der Datei kann also problemlos in den RAM gelesen werden.
"""
from pathlib import Path


BASE_DIR = Path(__file__).parent


def read_data(filename):
    """Einlesen der Daten.

    Datei öffnen und zeilenweise einlesen
    Es sollen die Roh-Daten als Liste von Strings zurückgegeben werden.
    Rückgabewert ist also eine Liste (von Strings)
    """
    word_list = []
    with open(BASE_DIR / filename, mode="r", encoding="utf-8") as f:   
        for line in f:
            word_list.append(line)
        return word_list
       

def filter_data(word_list):
    """Filtere die Daten und befreie sie von unzulässigen Zeichen.

    Die Funktion bekommt eine word_list übergeben (Liste von Strings)
    Die Zeilen sollen am Ende jeweils nur eine Ganzzahl als String enthalten.
    Leerzeilen sollen entfernt werden.  Ein Konvertieren nach int ist
    nicht notwendig.

    Rückgabewert ist eine Liste von Strings:
    ["24343", "34341", "3422"]

    """
    word_list = [el.strip() for el in word_list]
    word_list = [el.strip("#*=") for el in word_list if el]
    
    return word_list



def write_data(filename, word_list):
    """Die sauberen Daten sollen zeilenweise in eine Datei geschrieben werden.
    hier soll ein Dateiname und eine Liste von Strings übergeben werden.
    Der Rückgabewert ist None
    """
    with open(BASE_DIR / filename, mode="w") as f:
        f.writelines([el + "\n" for el in word_list])
    

def main():
    """Hauptprogramm. Führe die Reihenfolge wie folgt aus:
    - Daten einlesen (read_data) EXTRACT
    - Daten filtern / bereinigen (filter_data) TRANSFORM
    - Daten schreiben (write data) LOAD
    """
    word_list = read_data("log.txt")
    word_list_2 = filter_data(word_list)
    write_data("log_filtered.txt", word_list_2)


main()
