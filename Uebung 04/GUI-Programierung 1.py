import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programierung")

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:
        vornameLineEdit = QLineEdit()
        nameLineEdit = QLineEdit()
        emailLineEdit = QLineEdit()
        geburtstagSpinBox = QSpinBox()
        adresseLineEdit = QLineEdit()
        postleitzahlLineEdit = QLineEdit()
        ortLineEdit = QLineEdit()
        landLineEdit = QComboBox()

        landLineEdit.addItems(["Schweiz", "Deutschland", "Österreich"])

        # Layout füllen:
        layout.addRow("Vorname:", vornameLineEdit)
        layout.addRow("Name:", nameLineEdit)
        layout.addRow("Email:", emailLineEdit)
        layout.addRow("Geburtstag:", geburtstagSpinBox)
        layout.addRow("Adresse :", adresseLineEdit)
        layout.addRow("Postleitzahl:", postleitzahlLineEdit)
        layout.addRow("Ort:", ortLineEdit)
        layout.addRow("Land:", landLineEdit)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()