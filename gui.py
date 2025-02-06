from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from diferenciranje import diferenciraj
from integriranje import integriraj
import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, symbols

class Ui_MainWindow:
    def __init__(self, MainWindow):
        self.window = MainWindow
        self.layout = QVBoxLayout()

        # Unos funkcije
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Unesite funkciju (npr. x**2 + 3*x + 2)")

        # Dugme za diferenciranje
        self.dif_button = QPushButton("Diferenciraj")
        self.dif_button.clicked.connect(self.diferenciraj)

        # Dugme za integriranje
        self.int_button = QPushButton("Integriraj")
        self.int_button.clicked.connect(self.integriraj)

        # Prikaz rezultata
        self.result_label = QLabel("Rezultat će biti prikazan ovdje.")
        
        # Prikazivanje grafa
        self.plot_button = QPushButton("Prikazi graf")
        self.plot_button.clicked.connect(self.plot_graph)

        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.dif_button)
        self.layout.addWidget(self.int_button)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.plot_button)

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
        try:
            result = integriraj(function_str)
            self.result_label.setText(f"Integral: {result}")
        except Exception as e:
            self.result_label.setText(f"Greška: {str(e)}")

    def plot_graph(self):
        function_str = self.function_input.text()
        try:
            x = symbols('x')
            func = sympify(function_str)
            f = lambda x_val: float(func.subs('x', x_val))
            x_vals = np.linspace(-10, 10, 400)
            y_vals = np.array([f(x) for x in x_vals])

            plt.plot(x_vals, y_vals)
            plt.title(f"Graf funkcije: {function_str}")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.grid(True)
            plt.show()

        except Exception as e:
            self.result_label.setText(f"Greška u grafu: {str(e)}")
