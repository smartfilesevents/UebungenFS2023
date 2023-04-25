import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import urllib.parse

def buttonClick():
    L = mainwindow.Laenge.text()
    B = mainwindow.Breite.text()
    print("https://www.google.ch/maps/place/breite,länge")

    link = "https://www.google.ch/maps/place/"+L+","+B
    a = urllib.parse.quote(link)  # enthält 'Hell%C3%B6%20W%C3%B6rld%40'
    QDesktopServices.openUrl(QUrl(link))# benötigt QtCore & QtGui

# Eine Qt-Applikation erstellen:

app = QApplication(sys.argv)
mainwindow = loadUi("Uebung 06/showmap.ui")

# Nun kann auf die im UI-Designer gesetzten Namen zugegriffen werden
mainwindow.Button.clicked.connect(buttonClick)

mainwindow.show()

# Fenster anzeigen
# Application-L
app.exec()