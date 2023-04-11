import sys
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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


        karte = QPushButton("Auf Karte zeigen")
        laden = QPushButton("Laden")
        save = QPushButton("Save")
        

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameEdit)
        layout.addRow("Name:", self.nameEdit)
        layout.addRow("Geburtstag:", self.geburtstagEdit)
        layout.addRow("Adresse :", self.adresseEdit)
        layout.addRow("Postleitzahl:", self.postleitzahlEdit)
        layout.addRow("Ort:", self.ortEdit)
        layout.addRow("Land:", self.landEdit)
        layout.addRow(karte)
        layout.addRow(laden)
        layout.addRow(save)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center) # Zentrales Widget in diesem Fenster setzen
        self.show() # Fenster anzeigen
#----------------------------------------------------------------------------------------
#Speichern Teil 1
        karte.clicked.connect(self.karte_clicked)
        laden.clicked.connect(self.laden_clicked)
        save.clicked.connect(self.save_clicked)
#----------------------------------------------------------------------------------------
#File Menue
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(self.save_clicked)
        laden = QAction("Laden", self)
        laden.triggered.connect(self.laden_clicked)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        # Rolle "beenden" (für MacOS)
        quit.setMenuRole(QAction.QuitRole)

        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(laden)
        filemenu.addSeparator()
        filemenu.addAction(quit)


        viewmenue = menubar.addMenu("View")
        karte = QAction("Karte", self)
        karte.triggered.connect(self.karte_clicked)

        viewmenue.addAction(karte)
        viewmenue.addSeparator()   


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

        Location = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        filename, filter = QFileDialog.getSaveFileName(self,"Datei speichern",Location,"Text (*.txt)")
        print(Location)

        file = open(filename, "w", encoding="utf-8")
        writer = csv.writer(file, delimiter=',', lineterminator='\n')
        writer.writerow([vorname, name, geburtstag, adresse, postleitzahl, ort, land])

        file.close()
#----------------------------------------------------------------------------------------
#Auf Karte Zeigen
    def karte_clicked(self):
        adresse = self.adresseEdit.text()
        postleitzahl = self.postleitzahlEdit.text()
        ort = self.ortEdit.text()
        land = self.landEdit.currentText()

        adresse = adresse.replace(" ","+")

        link = "https://www.google.ch/maps/place/"+adresse+"+"+postleitzahl+"+"+ort+"+"+land
        import urllib.parse
        a = urllib.parse.quote(link)  # enthält 'Hell%C3%B6%20W%C3%B6rld%40'

        QDesktopServices.openUrl(QUrl(link))# benötigt QtCore & QtGui

#----------------------------------------------------------------------------------------
#Kontakt Laden
    def laden_clicked(self):
        Location = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        filename, filter = QFileDialog.getOpenFileName(self,"Datei öffnen",Location,"txt-Dateien (*.txt)")
        if (filename != ""):
            print(filename)
            print(filter)

        file = open(filename, "r", encoding="utf-8")
        data = file.readline().strip().split(",")
        loadVorname, loadNachname, loadGeburtsdatum, loadStrasse, loadPlz, loadOrt, loadLand = data

        date_parts = loadGeburtsdatum.split("/")
        date = QDate(int(date_parts[2]), int(date_parts[1]), int(date_parts[0]))

        self.vornameEdit.setText(loadVorname)
        self.nameEdit.setText(loadNachname)
        self.geburtstagEdit.setDate(date)
        self.adresseEdit.setText(loadStrasse)
        self.postleitzahlEdit.setText(loadPlz)
        self.ortEdit.setText(loadOrt)
        self.landEdit.setCurrentText(loadLand)

        file.close()

#----------------------------------------------------------------------------------------


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = Fenster()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()