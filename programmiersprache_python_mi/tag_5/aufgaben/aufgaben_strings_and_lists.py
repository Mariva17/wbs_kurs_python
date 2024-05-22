
"""(leicht)

Schreiben Sie ein Python-Programm, das eine Zeichenkette umkehrt, wenn ihre Länge ein Vielfaches von 4 ist
Hinweis: Benutze len, um die Zeichen der Zeichenkette zu zählen. Wenn len % 4 gleich 0 ist, wird die Zeichenkette umgekehrt.

ABER => REBA 
ABE => ABE 
ROTTDAMM = MMADTTOR
"""

# word = "ABER"
word = input("Bitte geben Sie ein Wort an: ")
if len(word) % 4 == 0:
    word_neu = word[::-1]
    print(word, word_neu)
else:
    print("Das Wort passt nicht.")



"""
(Mittel)
Schreiben Sie ein Python-Programm, um aus zwei gegebenen Strings, die durch ein Leerzeichen getrennt sind, 
einen einzigen String zu erhalten und die ersten beiden Zeichen jedes Strings zu vertauschen. Man kann davon ausgehen, dass die beiden Strings 
jeweils eine Länge >= 2 haben. 

Use String-Slicing for this task!

Sample Strings: 'abc', 'xyz'
Expected Result: 'xyc abz'
"""
word1 = input("Bitte geben Sie ein Wort an: ")
word2 = input("Bitte geben Sie noch ein Wort an: ")
# satz = word1 + " " + word2

word1 = word1.replace(word1[0:1], word2[0:1])
word2 = word2.replace(word2[0:1], word1[0:1])
satz_neu = word1 + " " + word2
print(satz_neu)
# word1 = list(word1)
# word2 = list(word2)
# word1[0], word1[1] = word2[0], word2[1]
# word2[0], word2[1] = word1[0], word1[1]
# word1[1] = word2[1]
# word2[0] = word1[0]
# word2[1] = word1[1]
# print(word1, " ", word2)
# word1 = list(word1)
# word2 = list(word2)
# for i, elem in enumerate(word1):
#     for j, el in enumerate(word2):
#         elem.replace(elem[i], el[j])
#         elem.replace(el[j], elem[i])
#         if i == 1 and j == 1:
#             print(word1 + " " + word2)
#             break
    



"""
(Mittel)
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

Sample String : 'ab'
Expected Result : 'ab'

Sample String : 'abc'
Expected Result : 'abcing'

Sample String : 'string'
Expected Result : 'stringly'
"""
str = input("Bitte geben Sie eine Zeile an: ")
if str[-3:] != "ing" and len(str) >= 3:
    str = str +"ing"

elif str[-3:] == "ing" and len(str) >= 3:
    str = str + "ly"
else:
    print(str) 
 
print(str)

""" (SCHWER)
Write a Python program to convert a given string to all uppercase if it 
contains at least 2 uppercase characters in the first 4 characters.

Hilfe:
Nutze dazu die String-Methode isupper() für die ersten vier Element der Liste und prüfe,
ob das jeweilige Zeichen uppercase ist. Zähle die Großbuchstaben.

"""
word = "PyThon"
word = list(word)
count = 0

for i, elem in enumerate(word):
    if elem.isupper():
        count += 1
        if count == 2 and i <= 3: 
            word_n = "".join(word)
            print(word_n.upper())      
            break
            
else:
    print("Das Wort passt nicht.")        
       
   

""" (SCHWER)
Berechne den Median folgender Liste, dazu NICHT die Funktion median nutzen.
Um eine Liste sortieren, gibt es die built-in Funktion sorted()

liste = sorted(liste)
"""
values = [1, 2, 4, 3, 8, 19]
values = sorted(values)
anzahl = len(values)

if not anzahl % 2:
    median = (values[anzahl // 2 - 1] + values[anzahl // 2]) / 2
else:
    median = values[anzahl // 2]
print(median)