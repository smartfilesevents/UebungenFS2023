from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import urllib.parse
import sys
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("08 mathplotlib & pyqt5/GUI.ui", self)
        self.show()

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.removeWidget(self.Grafik)
        self.verticalLayout.insertWidget(0,self.canvas)

        self.PlotStarten.clicked.connect(self.plot)

        self.Farbe.addItem("Blau")
        self.Farbe.addItem("Grün")
        self.Farbe.addItem("Rot")

    def plot(self):
        plt.clf()
        coeff_input = self.PolyEingabe.text()
        coeffs = coeff_input.split(',')

        numberOfPoints = self.AnzahlPunkte.value()
        Obergrenze = self.Obergrenze.value()
        Untergrenze = self.Untergrenze.value()

        colorText = self.Farbe.currentText()
        if colorText == "Blau":
            color = "b"
        elif colorText == "Grün":
            color = "g"
        elif colorText == "Rot":
            color = "r"
    



        try:
            coeffs = [float(coeff.strip()) for coeff in coeffs]
        except ValueError:
            self.error_message.showMessage('Fehler: Bitte geben Sie nur Zahlen ein.')
            return
        
        if len(coeffs) == 0 or coeffs[0] == 0:
            self.error_message.showMessage('Fehler: Bitte geben Sie einen gültigen Polynom ein.')
            return
        
        poly_str = ''
        for i, coeff in enumerate(coeffs):
            if i == 0:
                poly_str += str(coeff)
            else:
                sign = '+' if coeff >= 0 else '-'
                poly_str += f' {sign} {abs(coeff)}x^{i}'



        f = np.poly1d(coeffs)
        x = np.linspace(Untergrenze, Obergrenze,numberOfPoints)
        y = f(x)
        plt.plot(x,y,color+'o-')

        plt.axis("equal")
        self.canvas.draw()

app = QApplication([])
window = Window()
app.exec()