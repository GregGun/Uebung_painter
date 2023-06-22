from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Text für die Titelleiste des QMainWindows
        self.setWindowTitle("Painter-Fenster")

        self.setMinimumSize(400, 400)

        central_widget = CentralWidget(self)
        self.setCentralWidget(central_widget)
