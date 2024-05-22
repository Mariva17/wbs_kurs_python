"""



"""

x = "10"

try:
    p = x / 0
except ZeroDivisionError as e:
    print("hier ist ein Fehler")
    print(e) # division by zero
finally:
    print("ich bin finally und werde immer ausführt")


# falls finally ein return (oder break, oder continue) Statment
# ausführt, wird kein Exception ausgelöst!
def fn():
    try:
        1 / 0
        return "test"
    except NameError as e:
        print(e) 
    finally:
        print("finally ins log file schreiben")
        return "finally wurde zurückgeben"

x = fn()
print(x)

