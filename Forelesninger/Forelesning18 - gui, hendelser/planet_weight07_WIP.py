# TO BE CONTINUED...

import sys, random
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QFormLayout, QComboBox, QDoubleSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon


planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

# OBS! merk at i lista under er filnavnene til planetbildene. I timen la vi disse i en egen mappe kalt bilder, og derfor er stien være med. Dersom bildene ligger i samme mappe som denne fila må 'bilder/' fjernes for alle.
planetbilder = ['bilder/sun.png', 'bilder/merkur.png', 'bilder/venus.png', 'bilder/jorden.png', 'bilder/mars.png', 'bilder/jupiter.png', 'bilder/saturn.png', 'bilder/uranus.png', 'bilder/neptun.png']

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        # Setter tittel og størrelse på vinduet, og legger også til et ikon
        self.setWindowTitle('Planetvekt')
        self.setGeometry(100, 100, 500, 400)
        vinduicon = QIcon('bilder/sun.png')
        self.setWindowIcon(vinduicon)

        # Oppretter et gridlayout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Lager en label som skal plasseres øverst i layoutet
        self.topplabel =QLabel()
        self.topplabel.setText("Hva er din vekt på en annen planet?")
        self.layout.addWidget(self.topplabel, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)  # 0,0 er koordinatene, 1 er antall rader topplabel skal strekke seg over, og 2 er antall kolonner den skal strekke seg over. alignment sentrerer widgeten .

        # Oppretter et skjema av typen QFormLayout, og legger til widgets for å ta input fra brukeren. skjema skal så plasseres i gridlayout (linje 55)
        self.skjema = QFormLayout()
        # Rullegardinmeny/comboboks
        self.meny_combobox = QComboBox()
        self.meny_combobox.setPlaceholderText("Velg en planet ...")
        self.meny_combobox.addItem("Tilfeldig planet")              # Legger til et valg for Tilfeldig planet
        for planet in planeter:                                     # Løkken fyller så inn valg for her av planetene som fins i planeter-lista
            self.meny_combobox.addItem(planet)                      #      Istedenfor en for-løkke kunne vi også brukt self.meny_combobox.addItems(planeter) for å fylle inn valgene
       
        self.skjema.addRow(self.meny_combobox)                      # Legger til comboboksen i skjemaet

        # Oppretter et inputfelt for desimaltall. Her skal brukeren skrive inn sin vekt
        self.vekt_input = QDoubleSpinBox()
        self.vekt_input.setPrefix("Din vekt i kg:      ")           # Litt forklaringstekst i spinboksen
        self.vekt_input.setDecimals(1)                              # Vi ønsker 1 desimal på inputen
        self.skjema.addRow(self.vekt_input)                         # Legger til i skjemaet

        # Oppretter en knapp
        self.regnutknapp = QPushButton("Regn ut")
        
        self.skjema.addRow(self.regnutknapp)                        # Legger til knappen i skjemaet

        self.layout.addLayout(self.skjema, 1, 0)                    # Legger til skjemaet i gridlayouten, med koordinatene 1,0

        # Label for å holde på et bilde
        self.bildelabel = QLabel()                                  # Lager en label som skal inneholde et bilde av en planet
        self.pixmap = QPixmap('bilder/sun.png')                     # standardbilde settes til å være et bilde av solen
        self.pixmap = self.pixmap.scaled(256, 256)                  # skalerer bildet (antall piksler i parentes)
        self.bildelabel.setPixmap(self.pixmap)                      # Setter inn bildet i labelen

        self.layout.addWidget(self.bildelabel, 1,1)                 # legger til bildelabelen i layoutet, med koordinatene 1,1

        # Label som skal plasseres nederst i vinduet
        self.bunnlabel = QLabel("Velg en planet og skriv inn vekten din")       
        self.layout.addWidget(self.bunnlabel, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)  # legger til labelen i layoutet, med koordinater, utstrekning og alignment

        self.show()                                                 # Må være med for at vinduet skal vises

        # TO BE CONTINUED...

# Må alltid med:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())
