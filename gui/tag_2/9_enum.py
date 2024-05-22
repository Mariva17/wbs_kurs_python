"""
Enums

"""
import enum

#verfuegbarkeit = "stock"
#verfuegbarkeit in ["in stock", "out of stock"]


#IN_STOCK = "in stock"
#OUT_OF_STOCK= "out of stock"

class ProductState(enum.StrEnum):
    IN_STOCK = "in stock"
    OUT_OF_STOCK= "out of stock"
    COMMING_SOON = "comming soon"



class Produkt:
    def __init__(self, name, verfuegbarkeit: ProductState):
        self.name = name
        self.verfuegbarkeit = verfuegbarkeit



milka = Produkt("Milka zartbitter", ProductState.IN_STOCK)
print(milka.verfuegbarkeit)


## INT ENUM: Beispiel HTTP Codes

class HTTPCode(enum.IntEnum):
    BAD_REQUEST = 400
    NOT_FOUND = 404


print(HTTPCode.BAD_REQUEST)
for value in HTTPCode:
    print(value)


response = 404
if response == HTTPCode.NOT_FOUND:
    print("die Addresse wurde nicht gefunden.")