"""
die wichtisten isxxx.py - Methoden (für PCAP Prüfung)


"""

s = "223ase"
print("ist s alphanumerisch?", s.isalnum())
s = "bsdjvbnd"
print("ist s alphabetisch?", s.isalpha())

s = "asjgöjtß-%&"
print("ist s Teil des Ascii-Tables?", s.isascii())

s = "gfd&/("
print("ist s printable?", s.isprintable())

s = "gfhslkfhl\t"
print("ist s in Kleinbuchstaben?", s.islower())

s = "HELLO"
print("ist s in Großbuchstaben?", s.isupper())

# Sonderfall scharfes ß
s = "gfhslß"
print("ist s in Kleinbuchstaben?", s.islower())

s = "HELLOß"
print("ist s in Großbuchstaben?", s.isupper())


s = "½¼"
s = "१२३" # devanagri-ziffern
s = "ⅨⅩⅪ"  # römische zahlen
s = "0.12345"
s = "4²"
s = "5"
s = "05"

print("ist s decimal?", s.isdecimal())
print("ist s digit?", s.isdigit())
print("ist s numeric?", s.isnumeric())
