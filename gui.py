# gui.py
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QRadioButton, QHBoxLayout
from diferenciranje import diferenciraj
from integriranje import odaberi_metodu
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, symbols, integrate

class Ui_MainWindow:
    def __init__(self, MainWindow):
        self.window = MainWindow
        self.layout = QVBoxLayout()

        # Unos funkcije
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Unesite funkciju (npr. x**2 + 3*x + 2)")

        # Unos intervala
        self.interval_start_input = QLineEdit()
        self.interval_start_input.setPlaceholderText("Unesite početak intervala (npr. -10)")

        self.interval_end_input = QLineEdit()
        self.interval_end_input.setPlaceholderText("Unesite kraj intervala (npr. 10)")

        # Dugme za diferenciranje
        self.dif_button = QPushButton("Diferenciraj")
        self.dif_button.clicked.connect(self.diferenciraj)

        # Dugme za integriranje
        self.int_button = QPushButton("Integriraj")
        self.int_button.clicked.connect(self.integriraj)

        # Dugme za integriranje neodređenog integrala
        self.indefinite_int_button = QPushButton("Neodređeni integral")
        self.indefinite_int_button.clicked.connect(self.neodredjeni_integral)

        # Prikaz rezultata
        self.result_label = QLabel("Rezultat će biti prikazan ovdje.")
        
        # Prikazivanje grafa
        self.plot_button = QPushButton("Prikazi graf")
        self.plot_button.clicked.connect(self.plot_graph)

        # Dodajemo opcije za odabir integrala
        self.integration_type_layout = QHBoxLayout()
        self.definite_radio = QRadioButton("Određeni integral")
        self.indefinite_radio = QRadioButton("Neodređeni integral")
        self.definite_radio.setChecked(True)
        self.integration_type_layout.addWidget(self.definite_radio)
        self.integration_type_layout.addWidget(self.indefinite_radio)

        # Dodajemo sve na layout
        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.interval_start_input)
        self.layout.addWidget(self.interval_end_input)
        self.layout.addWidget(self.dif_button)
        self.layout.addWidget(self.int_button)
        self.layout.addWidget(self.indefinite_int_button)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.plot_button)
        self.layout.addLayout(self.integration_type_layout)

        container = QWidget()
        container.setLayout(self.layout)
        self.window.setCentralWidget(container)

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

            result = odaberi_metodu(f, interval_start, interval_end)
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
            x = symbols('x')
            func = sympify(function_str)
            f = lambda x_val: float(func.subs('x', x_val))
            interval_start = float(self.interval_start_input.text())
            interval_end = float(self.interval_end_input.text())
            x_vals = np.linspace(interval_start, interval_end, 400)
            y_vals = np.array([f(x) for x in x_vals])

            plt.plot(x_vals, y_vals)
            plt.title(f"Graf funkcije: {function_str}")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.grid(True)
            plt.show()

        except Exception as e:
            self.result_label.setText(f"Greška u grafu: {str(e)}")
