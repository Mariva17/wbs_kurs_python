"""

Das Paket library.

Besteht aus den Modulen infos und ...


__init__.py => ist die Initialisierungdatei für ein Python Package (optional)

"""

# __file__ => absoluter Pfad zur Datei
# __name__ => der Name des Moduls (__main__ oder filename)

__author__ = "Donald Duck"
__status__ = "development"

from library.infos import *
from library.dummy import *

print("Hallo, ich bin aus __init__ aus library!"
    "Ich werde überall geprintent, wo ein Modul aus library genutzt wird"
)