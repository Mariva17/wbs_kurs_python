
"""
Aufgabe:

a) ein Dialog-Fenster bauen
b) ein Layout erstellen (Horizontal oder Vertical)
c) einen Button erstellen und dem layout hinzufügen
d) Klasse MainDialog hat einen Counter. counter = 0
e) immer, wenn Button gedrückt wird, zählt counter um 1 hoch
f) falls der counter größergleich 6, dann soll eine Messagebox.warning
ausgegeben werden (und counter nicht weiter hochgezählt)

"""

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QMessageBox 
    )

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.setWindowTitle("Count Druck")

        main_layout = QHBoxLayout()

        self.label = QLabel("First Label")
        self.btn = QPushButton("druck!")
        self.btn.clicked.connect(self.count_druck)

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.btn)

        self.setLayout(main_layout)


    def count_druck(self):
        while self.counter != 6:
            self.counter += 1
            print(self.counter)
            break
        else:
            QMessageBox.critical(self, "Information:", "Error!")
            self.counter = 0
            
        

if __name__ == "__main__":
    app = QApplication([])  # Hauptprogramm
    main_dialog = MainDialog()
    main_dialog.show()  # Anzeigen des Fensters
    app.exec()

    
    