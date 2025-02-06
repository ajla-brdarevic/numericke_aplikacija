import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numeričko Diferenciranje i Integriranje")
        self.setGeometry(100, 100, 600, 400)
        self.ui = Ui_MainWindow(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())