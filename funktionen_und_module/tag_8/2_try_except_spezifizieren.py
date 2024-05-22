"""
Spezifizieren der Ausnahme

"""

#x = "10"

try:
    y = "hallo welt"
    p = x / 0
    z = "hier i come again" # Vorsicht! Wenn x / 0 scheitert
except ZeroDivisionError as e:
    print("hier ist ein Fehler")
    print(e) # division by zero
except (TypeError, NameError) as e:
    print("Type oder Name Error:", e) # unsupported operand type(s) for /: 'str' and 'int'
except Exception as e:
    print("Fehler bei Exception: ", e, type(e))


print("y: ", y)
# print("z: ", z) # z existiert nicht, weil x / 0 schief ging


