# Modul sys pruža pristup nekim varijablama koje koriste ili održavaju tumač i funkcijama koje komuniciraju s tumačem
import sys
# Importiranje potrebnih klasa iz PyQt5 modula za kreiranje GUI aplikacija
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importiranje korisničkog sučelja iz gui modula
from gui import Ui_MainWindow

class MainApp(QMainWindow):
    def __init__(self):
        # Poziva konstruktor nadklase (QMainWindow) kako bi osigurao inicijalizaciju potrebnih komponenti
        super().__init__()
        # Postavljanje naslova prozora
        self.setWindowTitle("Numeričko Diferenciranje i Integriranje")
        # Postavljanje geometrije prozora (pozicija i veličina)
        self.setGeometry(100, 100, 600, 400)
        # Inicijalizacija korisničkog sučelja iz gui modula
        self.ui = Ui_MainWindow(self)
        
# Provjerava da li se skripta pokreće direktno (a ne importira kao modul)
if __name__ == "__main__":
    # Stvaranje QApplication objekta koji upravlja događanjima aplikacije
    app = QApplication(sys.argv)
    # Stvaranje instance glavnog prozora aplikacije
    window = MainApp()
    # Prikazivanje glavnog prozora aplikacije
    window.show()
    # Ulazak u glavnu događajnu petlju aplikacije, izlaz s aplikacijom kad se završi
    sys.exit(app.exec_())