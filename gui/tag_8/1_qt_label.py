from PyQt6.QtWidgets import (QApplication, QDialog, QLabel, QHBoxLayout, QPushButton, QLineEdit, QComboBox)


class  MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my first window") # Fenster Title
        self.resize(600, 400)

        main_layout = QHBoxLayout() # Horizontales Box-Layout

        # Widgets definieren
        self.label = QLabel("First label")
        self.btn = QPushButton("Button 2")
        self.eingabe_feld = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.addItems(["item 1", "item 2"])
        

        # Add widgets to Layout
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.btn)
        main_layout.addWidget(self.eingabe_feld)
        main_layout.addWidget(self.combo_box)
        

        # MainLayout dem QDialog hinzufügen
        self.setLayout(main_layout)



if __name__ == "__main__":
    app = QApplication([])  # Hauptprogramm
    main_dialog = MainDialog()
    main_dialog.show()  # Anzeigen des Fensters
    app.exec()