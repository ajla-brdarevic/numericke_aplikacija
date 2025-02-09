# Modul sys pruža pristup nekim varijablama koje koriste ili održavaju tumač i funkcijama koje komuniciraju s tumačem
import sys

# Importiranje potrebnih klasa iz PyQt5 modula za kreiranje GUI aplikacija
from PyQt5.QtWidgets import QApplication, QMainWindow

# Importiranje korisničkog sučelja iz gui modula
from gui import Ui_MainWindow

# Definicija glavne klase aplikacije koja nasljeđuje QMainWindow
class MainApp(QMainWindow):
    def __init__(self):
        # Poziva konstruktor nadklase (QMainWindow) kako bi osigurao inicijalizaciju potrebnih komponenti
        super().__init__()
        
        # Postavljanje naslova prozora na naziv aplikacije
        self.setWindowTitle("Numeričko Diferenciranje i Integriranje")
        
        # Postavljanje geometrije prozora (pozicija i veličina) u pikselima
        self.setGeometry(100, 100, 600, 400)
        
        # Inicijalizacija korisničkog sučelja iz gui modula
        # Ovdje se veže UI sa glavnim prozorom aplikacije
        self.ui = Ui_MainWindow(self)

# Provjera da li se skripta pokreće direktno (a ne importira kao modul)
if __name__ == "__main__":
    # Stvaranje QApplication objekta koji upravlja događanjima aplikacije
    # Ovaj objekt je potreban za pokretanje i upravljanje aplikacijom
    app = QApplication(sys.argv)
    
    # Stvaranje instance glavnog prozora aplikacije
    window = MainApp()
    
    # Prikazivanje glavnog prozora aplikacije
    # Ovdje se poziva funkcija za prikazivanje aplikacije korisniku
    window.show()
    
    # Ulazak u glavnu događajnu petlju aplikacije
    # Ovdje aplikacija počinje obrađivati događaje i interakcije korisnika
    sys.exit(app.exec_())