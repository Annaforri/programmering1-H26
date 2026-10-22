from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys

# Lager en klasse, Hovedvindu, som skal arve fra klassen QWidget.
# Denne klassen er tenkt å inneholde all kode for å lage GUI-et som skal vises for vinduet vårt.
class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QVBoxLayout-test')     # Gir vinduet en tittel

        layout = QVBoxLayout()                      # Oppretter et layout av klassen QVBoxLayout
        self.setLayout(layout)                      # Sier at denne klassen (Hovedvindu) skal bruke nevnte layout

        button1 = QPushButton('Knapp 1')            # Oppretter en knapp av klassen QPushButton. Gir den teksten 'Knapp 1'
        button2 = QPushButton()                     # Oppretter en knapp av klassen QPushButton
        button2.setText('Knapp 2')                  # Alternativ måte å gi knappen en tekst
        button3 = QPushButton('Knapp 3')            # Oppretter en knapp av klassen QPushButton og gir den en tekst

        layout.addWidget(button1)                   # Legger til button1 i layout (vil bli vist på toppen siden den legges til først)
        layout.addWidget(button3)                   # Legger til button3 i layout (vil bli vist under button1, jmf. append()-metoden vi har sett på tidligere)
        layout.addWidget(button2)                   # Legger til button2 i layout
      
        self.show()                                 # Her har vi lagt show() i klassen. Siden denne ligger i __init__-metoden vil den bli utført når vi oppretter et objekt av Hovedvindu

if __name__ == '__main__':                          # Sjekker om det er denne filen vi starter/kjører. I så tilfelle kjøres koden under.
    app = QApplication(sys.argv)                    # Må alltid med

    vindu = Hovedvindu()                            # Oppretter et objekt av Hovedvindu()-klassen

    sys.exit(app.exec())                            # Må alltid med
