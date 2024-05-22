"""
Das Info-Modul: liefert Information zur Plattform


PCAP Exam Syllabus für platform.
platform(), 
machine(), 
processor(), 
system(), 
version(), 
python_implementation(), 
python_version_tuple()
"""

import platform



def machine_type() -> str:
    """the machine type of user."""
    return platform.machine()



def computer_name() -> str:
    """Computer network name."""
    return platform.node()


def operating_system() -> str:
    """Computers operating system."""
    return platform.platform()


def version() -> tuple:
    """Python version info """
    return (platform.python_implementation(), platform.python_version_tuple())



if __name__ == "__main__":
    # wird nur ausgeführt, wenn infos.py das Hauptprogramm ist
    # python infos.py
    print("Name des Infos-Moduls: ", __name__)
    print("Python Version: ", version())