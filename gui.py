from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QRadioButton, QHBoxLayout, QFormLayout, QScrollArea
from diferenciranje import diferenciraj
from integriranje import odaberi_metodu, trapezna_formula, simpsonova_formula, midpoint_formula
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, symbols, integrate

class Ui_MainWindow:
    def __init__(self, MainWindow):
        self.window = MainWindow

        # Glavni widget i layout
        self.central_widget = QWidget()
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setWidgetResizable(True)
        
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        
        self.window.setCentralWidget(self.scroll_area)

        self.layout = QVBoxLayout()

        self.window.setWindowTitle("Numerički Kalkulator")
        self.window.resize(400, 600)

        form_layout = QFormLayout()

        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Unesite funkciju (npr. x^2 + 3*x + 2)")
        self.function_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Funkcija:", self.function_input)

        # Unos intervala
        self.interval_start_input = QLineEdit()
        self.interval_start_input.setPlaceholderText("Unesite početak intervala:")
        self.interval_start_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Početak intervala:", self.interval_start_input)

        self.interval_end_input = QLineEdit()
        self.interval_end_input.setPlaceholderText("Unesite kraj intervala:")
        self.interval_end_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Kraj intervala:", self.interval_end_input)

        self.layout.addLayout(form_layout)

        # Dugme za diferenciranje
        self.dif_button = QPushButton("Eulerova metoda")
        self.dif_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.dif_button.clicked.connect(self.diferenciraj)
        self.layout.addWidget(self.dif_button)

        # Dugme za integriranje (Trapezna metoda)
        self.int_trap_button = QPushButton("Trapezna metoda")
        self.int_trap_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.int_trap_button.clicked.connect(self.trapezna)
        self.layout.addWidget(self.int_trap_button)

        # Dugme za integriranje (Simpsonova metoda)
        self.int_simp_button = QPushButton("Simpsonova metoda")
        self.int_simp_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.int_simp_button.clicked.connect(self.simpsonova)
        self.layout.addWidget(self.int_simp_button)

        # Dugme za integriranje (Midpoint metoda)
        self.int_mid_button = QPushButton("Midpoint metoda")
        self.int_mid_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.int_mid_button.clicked.connect(self.midpoint)
        self.layout.addWidget(self.int_mid_button)
        
        # Dugme za integriranje neodređenog integrala 
        self.indefinite_int_button = QPushButton("Neodređeni integral") 
        self.indefinite_int_button.setStyleSheet("font-size: 18px; padding: 10px;") 
        self.indefinite_int_button.clicked.connect(self.neodredjeni_integral) 
        self.layout.addWidget(self.indefinite_int_button)
        
        # Prikaz rezultata
        self.result_label = QLabel("Rezultat će biti prikazan ovdje.")
        self.result_label.setStyleSheet("font-size: 18px; padding: 10px;")
        self.layout.addWidget(self.result_label)
        
        # Prikazivanje grafa
        self.plot_button = QPushButton("Prikazi graf")
        self.plot_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.plot_button.clicked.connect(self.plot_graph)
        self.layout.addWidget(self.plot_button)

        self.scroll_layout.addLayout(self.layout)

    def diferenciraj(self):
        function_str = self.function_input.text()
        try:
            x_vals, y_vals = diferenciraj(function_str)
            result_str = "\n".join([f"x: {x:.2f}, y: {y:.2f}" for x, y in zip(x_vals, y_vals)])
            self.result_label.setText(f"Rezultati:\n{result_str}")
        except Exception as e:
            self.result_label.setText(f"Greška: {str(e)}")

    def trapezna(self):
        self.integriraj_metoda(trapezna_formula)

    def simpsonova(self):
        self.integriraj_metoda(simpsonova_formula)

    def midpoint(self):
        self.integriraj_metoda(midpoint_formula)

    def integriraj_metoda(self, metoda):
        function_str = self.function_input.text()
        interval_start = float(self.interval_start_input.text())
        interval_end = float(self.interval_end_input.text())
        try:
            x = symbols('x')
            func = sympify(function_str)
            f = lambda x_val: float(func.subs('x', x_val))

            result = metoda(f, interval_start, interval_end, 1000)  # Defaultni broj podintervala je 1000
            self.result_label.setText(f"Rezultat integrala: {result}")
        except Exception as e:
            self.result_label.setText(f"Greška: {str(e)}")

    def neodredjeni_integral(self):
        function_str = self.function_input.text()
        try:
            x = symbols('x')
            func = sympify(function_str)
            integral = integrate(func, x)
            self.result_label.setText(f"Neodređeni integral: {integral}")
        except Exception as e:
            self.result_label.setText(f"Greška: {str(e)}")

    def plot_graph(self):
        function_str = self.function_input.text()
        try:
            if not function_str:
                self.result_label.setText("Molimo unesite funkciju.")
                return

            interval_start_str = self.interval_start_input.text()
            interval_end_str = self.interval_end_input.text()

            if not interval_start_str:
                interval_start_str = "-10"
            if not interval_end_str:
                interval_end_str = "10"

            interval_start = float(interval_start_str)
            interval_end = float(interval_end_str)

            x = symbols('x')
            func = sympify(function_str)
            f = lambda x_val: float(func.subs('x', x_val))
            x_vals = np.linspace(interval_start, interval_end, 400)
            y_vals = np.array([f(x) for x in x_vals])

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