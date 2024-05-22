"""
Einstiegs-Datei

"""

from library import infos
import library.infos
import library.infos as info
import check
from check import checker
from library.infos import operating_system as ops
import library



def main():
    """Haupt-Funktion"""
    # check.checker(3)
    # checker(3)
    # print("computer name: ", infos.computer_name())
    # print("machine type: ", infos.machine_type())
    # print("OS: ", ops())
    # print("machine type", library.infos.machine_type())
    # print("machine type", info.machine_type())
    print("version:", infos.version())
    library.dummy_func()

if __name__ == "__main__":
    # wenn __name__ "__main__" ist, ist dies das Hauptprogramm
    main()