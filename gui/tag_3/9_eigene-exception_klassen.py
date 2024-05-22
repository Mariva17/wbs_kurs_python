"""
Eigene Exceptionklassen anlegen

eine EIGENE Exception muss von Exception erben
"""
class InvalidValue(Exception):
    pass


class InvalidValueExtended(Exception):
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value

    def __str__(self) -> str:
        return f"{self.msg} Wert: {self.value}"


def values():
    # tritt ein ValueError auf
    x = "jkjkhk"
    y = int(x) # potentieller ValueError

    if y == 2:
        #raise InvalidValue("y darf nicht kleiner als zwei sein")
        raise InvalidValueExtended(msg="y darf nicht kleiner als zwei sein", value=y)


try:
    values()
except ValueError as e:
    print(e, type(e))
except InvalidValue as e:
    print(e, type(e))
except InvalidValueExtended as e:
    print(e)  # ruft InvalidValueExtended __str__(self) auf
    print(e.msg)
    print(e.value)

