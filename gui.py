# gui.py
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QRadioButton, QHBoxLayout, QFormLayout
from diferenciranje import diferenciraj
from integriranje import odaberi_metodu
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, symbols, integrate

class Ui_MainWindow:
    def __init__(self, MainWindow):
        self.window = MainWindow
        self.layout = QVBoxLayout()

        # Podesavanje stila
        self.window.setWindowTitle("Numerički Kalkulator")
        self.window.resize(400, 600)

        # Organizacija layouta
        form_layout = QFormLayout()

        # Unos funkcije
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Unesite funkciju (npr. x**2 + 3*x + 2)")
        self.function_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Funkcija:", self.function_input)

        # Unos intervala
        self.interval_start_input = QLineEdit()
        self.interval_start_input.setPlaceholderText("Unesite početak intervala (npr. -10)")
        self.interval_start_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Početak intervala:", self.interval_start_input)

        self.interval_end_input = QLineEdit()
        self.interval_end_input.setPlaceholderText("Unesite kraj intervala (npr. 10)")
        self.interval_end_input.setStyleSheet("font-size: 18px; padding: 10px;")
        form_layout.addRow("Kraj intervala:", self.interval_end_input)

        # Dodavanje form layouta u glavni layout
        self.layout.addLayout(form_layout)

        # Dugme za diferenciranje
        self.dif_button = QPushButton("Diferenciraj")
        self.dif_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.dif_button.clicked.connect(self.diferenciraj)
        self.layout.addWidget(self.dif_button)

        # Dugme za integriranje
        self.int_button = QPushButton("Integriraj")
        self.int_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.int_button.clicked.connect(self.integriraj)
        self.layout.addWidget(self.int_button)

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

        # Dodajemo opcije za odabir integrala
        self.integration_type_layout = QHBoxLayout()
        self.definite_radio = QRadioButton("Određeni integral")
        self.definite_radio.setStyleSheet("font-size: 18px; padding: 10px;")
        self.indefinite_radio = QRadioButton("Neodređeni integral")
        self.indefinite_radio.setStyleSheet("font-size: 18px; padding: 10px;")
        self.definite_radio.setChecked(True)
        self.integration_type_layout.addWidget(self.definite_radio)
        self.integration_type_layout.addWidget(self.indefinite_radio)
        self.layout.addLayout(self.integration_type_layout)

        container = QWidget()
        container.setLayout(self.layout)
        self.window.setCentralWidget(container)  # Postavljamo centralni widget

    def diferenciraj(self):
        function_str = self.function_input.text()
        try:
            result = diferenciraj(function_str)
            self.result_label.setText(f"Diferencijal: {result}")
        except Exception as e:
            self.result_label.setText(f"Greška: {str(e)}")

    def integriraj(self):
        function_str = self.function_input.text()
        interval_start = float(self.interval_start_input.text())
        interval_end = float(self.interval_end_input.text())
        try:
            x = symbols('x')
            func = sympify(function_str)
            f = lambda x_val: float(func.subs('x', x_val))

            result, _ = odaberi_metodu(f, interval_start, interval_end)  # Ignoriramo poruku metode
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

            # Postavimo podrazumevane intervale ako nisu uneseni
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
