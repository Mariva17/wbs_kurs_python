# pyright: reportGeneralTypeIssues=false
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QHBoxLayout,
    QPushButton,
)
from PyQt6.uic import loadUi
from pathlib import Path


class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(Path(__file__).parent / "example.ui", self)
        self.set_actions()

    def set_actions(self):
        self.pushButton.clicked.connect(self.print_values)

    def print_values(self):
        name = self.nameInput.text()
        age = self.ageInput.text()
        prof = self.professionInput.text()
        institute = self.institutInput.text()

        print(name, age, prof, institute)


if __name__ == "__main__":
    app = QApplication([])
    my_window = MyWindow()
    my_window.show()
    app.exec()
