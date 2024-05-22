# Matplotlib in Pyqt nutzen
import random
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QVBoxLayout,
    QPushButton,
    QComboBox,
)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


def get_data() -> dict:
    return {
        "Baseballs": [random.randint(10, 100) for _ in range(10)],
        "T-Shirts": [random.randint(10, 100) for _ in range(10)],
        "Cups": [random.randint(10, 100) for _ in range(10)],
    }


class SalesChartApp(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mein Matplotlib Fenster")
        self.setGeometry(100, 100, 800, 800)
        self.data = get_data()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Combobox zur Produktauswahl
        self.combo = QComboBox()
        self.combo.addItems(self.data.keys())
        self.combo.currentIndexChanged.connect(self.switch_product)
        # todo: aktion bei Change

        layout.addWidget(self.combo)

        # Create Matplotlib Figure
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        self.current_product = "Baseballs"
        self.plot_sales_data()

    def switch_product(self):
        self.current_product = self.combo.currentText()
        self.plot_sales_data()

    def plot_sales_data(self):
        self.ax.clear()  # Plot-Bereich löschen
        years = range(2014, 2024)
        sales = self.data[self.current_product]
        self.ax.bar(years, sales, color="skyblue")
        self.ax.set_title(f"Sales per year - {self.current_product}")
        self.canvas.draw()  # den Canvas zeichnen


if __name__ == "__main__":
    app = QApplication([])
    my_window = SalesChartApp()
    my_window.show()
    app.exec()
