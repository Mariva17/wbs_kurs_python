"""
Implementiere die folgenden Funktionen.
Führe print nicht in einer Funktion aus, es sei denn, es ist explizit
gewünscht.
--------------------------------------------------------------------
Die Ausgabe bezieht sich immer auf die Rückgabewerte der Funktion!!
--------------------------------------------------------------------
z.B.
def fn():
    return 1

result = fn()  # fn() aufrufen und Rückgabewert in result speichern
print(result) # den Rückgabewert von fn printen

####
"""

"""
0. Identitätsfunktion (LEICHT)
Schreibe eine Funktion identity, die einen Paramter hat und diesen Wert
unverändert zurückgibt.

value = identity(42)
print(value)
42
"""



def identity(x):
    return x

value = identity(86)
print("Aufgabe 0: ", value)



"""
0.b Aufruf der Funktion für eine Liste  (MITTEL)
n = 10
Führe die Funktion identity für die range(n) aus und speichere das Ergebnis in
einer Liste, zum Beispiel via List-Comprehension.

"""
n = 15
def identity(n):
    return n

result = [i for i in range(n)]
print("Aufgabe 0.b: ", result)

"""
1. Vokale zählen (MITTEL)
Schreibe eine Funktion count_vowels() die einen String als Parameter erwartet,
und alle Vokale  in diesem String zählt. Der Rückgabewert der Funktion ist die
Anzahl der Vokale (int). Als Vokale zählen im deutschen: aeiouüäö
Beachte Groß- und Kleinschreibung! Auge hat 3 Vokale

Beispiel:
number_of_vowels = count_vowels("teleport").
print(number_of_vowels)
// 3

number_of_vowels = count_vowels("Ööll").
print(number_of_vowels)
// 2
"""
text = input("Bitte gebe ein Wort ein: ")

vowels = "aeiouüöä"

def count_vowels(text):
    vowels_count = 0
    for letter in text:
        if letter.isalpha():
            if letter.lower() in vowels:
                vowels_count += 1
        # else:
        #     print("Die Eingabe ist kein String.")
    return vowels_count


number_of_vowels = count_vowels(text)
print("Aufgabe 1. Number of vowels: ", number_of_vowels)


"""
3. Liste filtern (MITTEL)
Schreibe eine Funktion filter_input(), die eine Liste A entgegennimmt und
anhand einer weiteren Liste B mit erlaubten Werten prüft, ob diese Werte
zulässig sind. Rückgabewert der Funktion ist eine Liste mit Werten, die
mithilfe B geprüft worden ist.

Beispiel
input_filtered = filter_input([1, 3, 4, 5, 3], [3, 4])
print(input_filtered)
// [3, 4, 3]

input_filtered = filter_input([1, 3, 4, 5, 3], [])
print(input_filtered)
// []

input_filtered = filter_input(["gold", "gelb", "gelb", "rot", "gelb"], ["gelb", "rot"])
// ["gelb", "gelb", "rot", "gelb"]
"""
values = [1, 3, 4, 5, 3]
erl_werte = [3, 4]
# values = ["gold", "gelb", "gelb", "rot", "gelb"]
# erl_werte = ["gelb", "rot"]
# values = [1, 3, 4, 5, 3]
# erl_werte = []
filtered = []

def filter_input(val, werte):
    for i in val:
        if i in werte:
            filtered.append(i)
    return filtered


input_filtered = filter_input(values, erl_werte)
print("Aufgabe 3: ", input_filtered)


"""
4. Rückwärts (SCHWER)
Schreibe eine Funktion reverse_cutter(), die einen String entgegennimmt, diesen
zu Kleinbuchstaben transformiert, den ersten und letzten Index abschneidet und
das Ergebnis umgedreht zurückgibt. Ein Input kleiner gleich Länge zwei gibt
einen leeren String zurück.  Beispiel:
reversed = reverse_cutter("Petersburg")
// rubsrete
"""
s = input("Bitte gebe ein Wort ein: ")

def reverse_cutter(s):
    if len(s) > 2:
        s = s.lower()
        s = s[1:-1]
        s = s[::-1]
        return s
    else:
        return ""

reversed = reverse_cutter(s)
print("Aufgabe 4: ", reversed)

"""
5. Max (MITTEL)
Implementiere die Funktion max. Diese soll aus einer gegebenen Liste von
Integerwerten den größten Wert zurückgeben. Nutze dazu nicht die Built-In
Funktion max oder max aus dem Numpy-Modul! Die Funktion soll None zurückgeben,
wenn eine leere Liste übergeben wurde.

Beispiel:
values = [3, 2, 4]
x_max = max(values)
// 4

values = []
x_max = max(values)
// None
"""
values = [3, 2, 6, 9, 1]
def max(val):
    val = sorted(val)
    if val == []:
        return None
    else:
        x = val[-1]
    return x

x_max = max(values)
print("Aufgabe 5: max = ", x_max)



"""
6. Median (SCHWER)
Implementiere die Funktion median(), die eine Liste von Integerwerten
entgegennimmt und den Median berechnet. Prüfe die Funktion mit verschiedenen
Input-Werten! Nicht die Funktion median aus dem Numpy Modul o.ä. nutzen.
Ergebnis kann hier geprüft werden:
http://www.alcula.com/calculators/statistics/median/


Beispiel:
values = [1, 2, 4, 8, 2, 19]
x_median = median(values)
// 3.0
"""
values = [1, 2, 4, 8, 2, 19, 5]

def median(val):
    val_sorted = sorted(val)
    length = len(val_sorted)
    index = (length - 1) // 2
    if length % 2 != 0:
        return val_sorted[index]
    else:
        return (val_sorted[index] + val_sorted[index + 1]) / 2
    

x_median = median(values)
print("Aufgabe 5: ", x_median)




""" (LEICHT)
7. Schwellenwertfunktion (Heaviside, Hard Limit)
Eine Funktion, die häufig im Zusammenhang mit neuronalen Netzen
genutzt wird, ist die Heaviside funktion.
Sie gibt 1 zurück, wenn der Eingangswert größergleich 0 ist, ansonsten,
gibt sie 0 zurück.

Hintergrundwissen:
https://de.wikipedia.org/wiki/Heaviside-Funktion
"""

x = input("Bitte gebe ein Zahl ein: ")
def fn(a):
    if x.replace(".", "").isdigit() and float(x) >= 0:
        return 1
    else:
        return 0
result = fn(x)
print("Aufgabe 7: ", result)

"""
8. Rectifier (RELU) (MITTEL)
im DeepLearning häufig genutze Funktion, die als Positivteil ihres Arguments
definiert ist.

Hintergrundwissen:
https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html

f(v) = max(0, v)

Führe die Funktion von der Range -10 bis 10 aus, zum Beispiel via einer
List-Comprehension.
"""

def fn(x, y):
    x = 0
    if y > 0:
        return y, x == 0 
    else:
        return 0
result = [fn(x, y) for x, y in range(-10, 10)]
print(result)


"""
9. Sigmoid (Schwer)
in neuronalen Netzen genutze Aktivierungsfunktion
https://de.wikipedia.org/wiki/Sigmoidfunktion
"""


def sigmoid(x): ...


result = sigmoid(-5)  # 0.0067
result = sigmoid(0)  # 0.5
result = sigmoid(5)  # 0.9933
