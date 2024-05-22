"""
Thema: Zeichenkodierung

Hallo
ASCII: 128 Zeichen max

Codepages: 256 Zeichen max (Zeichen 1 Byte)

Unicode-Projekt: unicode.org (Kodierung aller mrnschlichen Zeichen)

konkrete Implementierungen: utf-8 (Mehrbyte-Kodierung 1 bis 4 Byte), utf-16 (Zweibyte-Kodierung)
"""

import string

# den Unicode-Codepoint von einem Zeichen ermiteln
print(ord("a"))

print("a:", ord("a"), hex(ord("a")))
print("z:", ord("z"), hex(ord("z")))
print("A:", ord("A"), hex(ord("A")))

print(ord("c") - ord("a"))

# Alle druckbaren ASCII-Zeichen
print(string.printable)

print(ord("ü"))
print(list("ü".encode("utf-8")))
print(list("ü".encode("iso-8859-1")))

# sich für einen dezimalen (oder hex) Wert das Zeichen geben lassen
print(chr(54111))

print(chr(ord('a') + 3))
print(chr(ord('d') - 3))

if "a" < "A":
    print("a ist kieiner als A")
else:
    print("A ist kieiner als a")

names = ["affw", "alfa", "Amerika"]
names = sorted(names)
print(names)