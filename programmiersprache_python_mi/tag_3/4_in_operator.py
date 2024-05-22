"""
Membership Operator IN:
Prüfen, ob ein Wert in einer Sequenz vorhanden ist.

"""

values = "3259864"
if "98" in values:
    print("98 ist in", values, "enthalten")

# python springt schon beim ersten ("99" in values) raus, da Aussage unwahr
unbekannte_variable = 0
if "99" in values and unbekannte_variable > 0:
    print("99 ist nicht enthalten")