"""
PyQt6 -> Binding an QT6
pip install pyqt6
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget

# unsere Haupt - Instanz
app = QApplication(sys.argv)


# window
window = QWidget()
window.show()

# Starten des Eventloops
app.exec()

print("Hier ist das Ende")


