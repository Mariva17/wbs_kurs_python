
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QFormLayout,
    QLineEdit,
    QComboBox, 
    QPushButton,
    QMessageBox
)


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")  # Fenster Title
        self.form_layout = QFormLayout()

        self.btn = QPushButton("Absenden")
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.profession = QComboBox()
        self.profession.addItems(["Developer", "SysAdmin", "Tester"])
        
        self.form_layout.addRow("Name:", self.name_input)
        self.form_layout.addRow("Age:", self.age_input)
        self.form_layout.addRow("Profession:", self.profession)
        self.form_layout.addRow(self.btn)


        # Events
        self.btn.clicked.connect(self.show_something)

        self.setLayout(self.form_layout)

    def show_something(self):
        print(f"Name: {self.name_input.text()}")
        print(f"Age: {self.age_input.text()}")
        print(f"Profession: {self.profession.currentText()}")
        QMessageBox.information(self, "All good?", "Hurra")



if __name__ == "__main__":
    app = QApplication([])  # Hauptprogramm
    main_dialog = MainDialog()
    main_dialog.show()  # Anzeigen des Fensters
    app.exec()