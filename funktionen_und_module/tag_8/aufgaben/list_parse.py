"""

Parse list

1. Schreibe eine Funktion list_parse(), die eine Liste von Strings
entgegennimmt und versucht, die Elemente dieser Liste
in Floats zu konvertieren.

Es finden sich auch Strings in der Liste, die das Komma als
Dezimaltrennzeichen nutzen. Diese Werte gelten als legale Eingabe,
allerdings muss die Funktion die Kommas vorab durch Punkte ersetzen.

2.  Alle Strings, die nach Float konvertierbar sind, sollen
in einer Liste namens "cleaned" gespeichert werden.


3. Alle nicht zu Float konvertiereben Eingabestrings werden
in einer Fehlerliste "errors" gesammelt.
Diese muss die Originalstrings enthalten.

3. Der Rückgabewert der Funktion soll ein Tupel sein aus den Listen
cleaned und errors


Beispiel:
a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,"]

Folgende Werte sind nach float konvertiebar:
2
0.2
0,4 (nach Umwandlung in 0.4)
3

in der Errorliste finden sich alle Werte, die nicht nach
float konvertiert werden konnten:
a3
a01
,
a.a
a,


Result:
cleaned = [2.0, 0.2, 0.4, 3.0]
errors = ['a3', 'a01', ',', 'a.a', 'a,']

"""
a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,"]


def list_parse(values: list) -> tuple[list, list]:
    cleaned = []
    errors = []
    
    for value in values:
        if value.replace(".", "").isdigit() or value.replace(",", "").isdigit():
            try:
                value = value.replace(",", ".")
                value = float(value)
                cleaned.append(value)
            except Exception as e:
                print(e)
        else:
            errors.append(value)                           
            
    return cleaned, errors


x = list_parse(a)
print(x)
            




def list_parse2(a: list[str]) -> tuple[list, list]:
    res = []
    errorlist = []

    for el in a:
        try:
            res.append(float(el.replace(",", ".")))
        except ValueError:
            errorlist.append(el)
    return res, errorlist


res, errorlist = list_parse2(a)
print("Result: ", res)
print("Fehler:", errorlist)

    
    