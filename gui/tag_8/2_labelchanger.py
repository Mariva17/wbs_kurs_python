
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QHBoxLayout,
    QPushButton,
)


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label Changer")  # Fenster Title

        main_layout = QHBoxLayout()  # Horizontales Box-Layout

        # Widgets definieren
        self.label = QLabel("First label")
        self.btn = QPushButton("Change Label")
        self.btn.clicked.connect(self.change_label)  # EVENT!

        # Add widgets to Layout
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.btn)

        # MainLayout dem QDialog hinzufügen
        self.setLayout(main_layout)

    def change_label(self):
        self.label.setText("Label wurde verändert.")


if __name__ == "__main__":
    app = QApplication([])  # Hauptprogramm
    main_dialog = MainDialog()
    main_dialog.show()  # Anzeigen des Fensters
    app.exec()
