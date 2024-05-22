"""
Einen Counter mit einem Dict erzeugen
z.b. Vorkommen von Wörten im Satz zählen, oder Buchstaben im Satz
"""

from collections import Counter

# Zählen der Häuftigkeit von Buchstaben im Satz

sentence = "The brown fox jumps over the lazy dog"

# klassisch
d = {} # d["a"] = 2
for char in sentence:
    if char in d:
        d[char] = d[char] + 1
    else:
        d[char] = 1

# oder
for char in sentence:
    d[char] = d.get(char, 0) + 1


# pythonisch: Counter nutzen
c = Counter(sentence)
print(c.most_common(5))