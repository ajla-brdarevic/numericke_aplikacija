# Importiranje potrebnih klasa iz PyQt5 modula za kreiranje GUI aplikacija
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QFormLayout, QScrollArea
# Importiranje funkcija za numeričke operacije iz modula diferenciranje i integriranje
from diferenciranje import diferenciraj
from integriranje import odaberi_metodu, trapezna_formula, simpsonova_formula, midpoint_formula
# Importiranje modula za grafičko prikazivanje i matematičke operacije
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, symbols, integrate

# Kreiranje klase koja predstavlja korisničko sučelje glavnog prozora aplikacije
class Ui_MainWindow:
    def __init__(self, MainWindow):
        # Inicijalizacija glavnog prozora aplikacije
        self.window = MainWindow

        # Glavni widget i layout za pomični sadržaj prozora
        self.central_widget = QWidget()
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setWidgetResizable(True)

        # Widget za sadržaj koji se prikazuje unutar scroll area
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        # Postavljanje scroll area kao centralni widget glavnog prozora
        self.window.setCentralWidget(self.scroll_area)

        # Kreiranje osnovnog layouta za formu
        self.layout = QVBoxLayout()

        # Postavljanje naslova i veličine prozora aplikacije
        self.window.setWindowTitle("Numerički Kalkulator")
        self.window.resize(400, 600)

        # Kreiranje layouta za unos podataka (funkcija i intervali)
        form_layout = QFormLayout()

        # Polje za unos funkcije
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Unesite funkciju (npr. x^2 + 3*x + 2)")
        self.function_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Funkcija:", self.function_input)

        # Polje za unos početka intervala
        self.interval_start_input = QLineEdit()
        self.interval_start_input.setPlaceholderText("Unesite početak intervala:")
        self.interval_start_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Početak intervala:", self.interval_start_input)

        # Polje za unos kraja intervala
        self.interval_end_input = QLineEdit()
        self.interval_end_input.setPlaceholderText("Unesite kraj intervala:")
        self.interval_end_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Kraj intervala:", self.interval_end_input)

        # Dodavanje forme za unos podataka u osnovni layout
        self.layout.addLayout(form_layout)

        # Dugme za izvođenje diferenciranja pomoću Eulerove metode
        self.dif_button = QPushButton("Eulerova metoda")
        self.dif_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.dif_button.clicked.connect(self.diferenciraj)
        self.layout.addWidget(self.dif_button)

        # Dugme za izvođenje integriranja pomoću trapezne metode
        self.int_trap_button = QPushButton("Trapezna metoda")
        self.int_trap_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.int_trap_button.clicked.connect(self.trapezna)
        self.layout.addWidget(self.int_trap_button)

        # Dugme za izvođenje integriranja pomoću Simpsonove metode
        self.int_simp_button = QPushButton("Simpsonova metoda")
        self.int_simp_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.int_simp_button.clicked.connect(self.simpsonova)
        self.layout.addWidget(self.int_simp_button)

        # Dugme za izvođenje integriranja pomoću Midpoint metode
        self.int_mid_button = QPushButton("Midpoint metoda")
        self.int_mid_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.int_mid_button.clicked.connect(self.midpoint)
        self.layout.addWidget(self.int_mid_button)

        # Dugme za izračunavanje neodređenog integrala
        self.indefinite_int_button = QPushButton("Neodređeni integral")
        self.indefinite_int_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.indefinite_int_button.clicked.connect(self.neodredjeni_integral)
        self.layout.addWidget(self.indefinite_int_button)

        # Labela za prikazivanje rezultata izračuna
        self.result_label = QLabel("Rezultat će biti prikazan ovdje.")
        self.result_label.setStyleSheet("font-size: 18px; padding: 10px;")
        self.layout.addWidget(self.result_label)

        # Dugme za prikazivanje grafa funkcije
        self.plot_button = QPushButton("Prikazi graf")
        self.plot_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.plot_button.clicked.connect(self.plot_graph)
        self.layout.addWidget(self.plot_button)

        # Dodavanje osnovnog layouta u scrollable layout
        self.scroll_layout.addLayout(self.layout)

    # Funkcija koja poziva diferenciranje funkcije pomoću Eulerove metode
    def diferenciraj(self):
        function_str = self.function_input.text()
        try:
            # Poziva funkciju za diferenciranje iz modula diferenciranje
            x_vals, y_vals = diferenciraj(function_str)
            result_str = "\n".join([f"x: {x:.2f}, y: {y:.2f}" for x, y in zip(x_vals, y_vals)])
            self.result_label.setText(f"Rezultati:\n{result_str}")
        except Exception as e:
            self.result_label.setText(f"Greška: {str(e)}")

    # Funkcija koja poziva trapeznu metodu za integriranje
    def trapezna(self):
        self.integriraj_metoda(trapezna_formula)

    # Funkcija koja poziva Simpsonovu metodu za integriranje
    def simpsonova(self):
        self.integriraj_metoda(simpsonova_formula)

    # Funkcija koja poziva Midpoint metodu za integriranje
    def midpoint(self):
        self.integriraj_metoda(midpoint_formula)

    # Opća funkcija za izvođenje integriranja pomoću zadate metode
    def integriraj_metoda(self, metoda):
        function_str = self.function_input.text()
        interval_start_str = self.interval_start_input.text()
        interval_end_str = self.interval_end_input.text()

        # Provjera unosa intervala
        if not interval_start_str or not interval_end_str:
            self.result_label.setText("Greška: Molimo unesite početak i kraj intervala.")
            return

        try:
            interval_start = float(interval_start_str)
            interval_end = float(interval_end_str)
            x = symbols('x')
            func = sympify(function_str)
            f = lambda x_val: float(func.subs('x', x_val))

            # Izvođenje integriranja korištenjem zadate metode
            result = metoda(f, interval_start, interval_end, 1000)  # Defaultni broj podintervala je 1000
            self.result_label.setText(f"Rezultat integrala: {result}")
        except ValueError:
            self.result_label.setText("Greška: Molimo unesite valjane numeričke vrijednosti za intervale.")
        except Exception as e:
            self.result_label.setText(f"Greška: {str(e)}")

    # Funkcija za izračunavanje neodređenog integrala
    def neodredjeni_integral(self):
        function_str = self.function_input.text()
        try:
            x = symbols('x')
            func = sympify(function_str)
            # Izračunavanje neodređenog integrala
            integral = integrate(func, x)
            self.result_label.setText(f"Neodređeni integral: {integral}")
        except Exception as e:
            self.result_label.setText(f"Greška: {str(e)}")

    # Funkcija za prikazivanje grafa funkcije
    def plot_graph(self):
        function_str = self.function_input.text()
        try:
            if not function_str:
                self.result_label.setText("Molimo unesite funkciju.")
                return

            interval_start_str = self.interval_start_input.text()
            interval_end_str = self.interval_end_input.text()

            # Provjera unosa intervala, postavljanje defaultnih vrijednosti
            if not interval_start_str:
                interval_start_str = "-10"
            if not interval_end_str:
                interval_end_str = "10"

            interval_start = float(interval_start_str)
            interval_end = float(interval_end_str)

            # Kreiranje funkcije za izračunavanje vrijednosti funkcije na određenim točkama
            x = symbols('x')
            func = sympify(function_str)
            f = lambda x_val: float(func.subs('x', x_val))
            x_vals = np.linspace(interval_start, interval_end, 400)
            y_vals = np.array([f(x) for x in x_vals])

            # Prikazivanje grafa funkcije
            plt.plot(x_vals, y_vals)
            plt.title(f"Graf funkcije: {function_str}")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.grid(True)
            plt.show()

        except ValueError:
            self.result_label.setText("Greška: Molimo unesite valjane numeričke vrijednosti za intervale.")
        except Exception as e:
            self.result_label.setText(f"Greška u grafu: {str(e)}")