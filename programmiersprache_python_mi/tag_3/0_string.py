"""
Datentyp String: sequentieller, unveränderlicher Datentyp

https://pythoninstitute.org/pcap-exam-syllabus

"""

name = "Donald ist neu hier. print('x')"
daten = "12, 23.2, 13, 24.3"

userinput = input("Bitte gebe Zahl ein: ")
print(type(userinput))
print("Typ von name: ", type(name))  # <class 'str'>

# String per Index addressieren
name = 'Alice'
print(name[0]) # A
print(name[3]) # c
# print(name[12]) # IndexError: string index out of range

# name[0] = "B"  # Strings sind unveränderlich

# Letze Zeichen eines Strings
print("letzes Zeichen: ", name[-1]) # e
print("vorletzes Zeichen: ", name[-2]) # c

# String addieren (konkatenieren). Additionsoperatoren-Überladung
a = "hallo"
b = "welt"
c = a + "," + b
print("a+b:", c)

# String multiplizieren
star = "*"
print(star * 30)

# Anführungszeichen in einem String
# satz = "Paul sagte: "das Wetter ist schön""
satz = "Paul sagte: 'das Wetter ist schön'"
print(satz)
satz = "Paul sagte: \"das Wetter ist schön\"" # Maskieren per Backslash
print(satz)
satz = 'it\' s ok' # Maskieren

# Zahl nach String konvertieren
zahl = 12
print(zahl, type(zahl))
zahl_string = str(zahl)
print(zahl_string, type(zahl_string))



