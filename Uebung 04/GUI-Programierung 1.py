import sys
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI-Programierung") # Fenster-Titel definieren
#----------------------------------------------------------------------------------------
#Layout + Attribute
        layout = QFormLayout() # Layout erstellen

        # Widget-Instanzen erstellen:
        self.vornameEdit = QLineEdit()
        self.nameEdit = QLineEdit()

        self.geburtstagEdit = QDateEdit()
        self.geburtstagEdit.setDisplayFormat("dd/MM/yyyy")

        self.adresseEdit = QLineEdit()
        self.postleitzahlEdit = QLineEdit()
        self.ortEdit = QLineEdit()
        
        self.landEdit = QComboBox()
        self.landEdit.addItems(["Schweiz", "Deutschland", "Österreich"])

        save = QPushButton("Save")

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameEdit)
        layout.addRow("Name:", self.nameEdit)
        layout.addRow("Geburtstag:", self.geburtstagEdit)
        layout.addRow("Adresse :", self.adresseEdit)
        layout.addRow("Postleitzahl:", self.postleitzahlEdit)
        layout.addRow("Ort:", self.ortEdit)
        layout.addRow("Land:", self.landEdit)
        layout.addRow(save)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center) # Zentrales Widget in diesem Fenster setzen
        self.show() # Fenster anzeigen
#----------------------------------------------------------------------------------------
#Speichern Teil 1
        save.clicked.connect(self.save_clicked)
#----------------------------------------------------------------------------------------
#File Menue
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(self.save_clicked)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        # Rolle "beenden" (für MacOS)
        quit.setMenuRole(QAction.QuitRole)

        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

    def menu_quit(self):
        self.close()  # Hauptfenster schliessen = beenden!
#----------------------------------------------------------------------------------------
#Speichern
    def save_clicked(self):
        vorname = self.vornameEdit.text()
        name = self.nameEdit.text()
        geburtstag = self.geburtstagEdit.text()
        adresse = self.adresseEdit.text()
        postleitzahl = self.postleitzahlEdit.text()
        ort = self.ortEdit.text()
        land = self.landEdit.currentText()

        file = open("Kontakte.txt", "w", encoding="utf-8")
        writer = csv.writer(file, delimiter=',', lineterminator='\n')
        writer.writerow([vorname, name, geburtstag, adresse, postleitzahl, ort, land])

        file.close()

#----------------------------------------------------------------------------------------

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = Fenster()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()