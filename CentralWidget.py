import sys
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QFont
from PyQt6.QtCore import Qt

# Hey Git Link:  ab Zeile 76: https://github.com/chey00/pointNclick/blob/master/TemplateRoom.py
#
# Github: https://github.com/chey00/drawing/

class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.setWindowTitle("Zeichenprogramm")

    def paintEvent(self, event):

        painter = QPainter(self)

        # Fülle den Kreis mit Schwarz
        painter.setBrush(Qt.GlobalColor.black)

        #oder
        #painter.setBrusch(QColor("black"))

        # (X-ACHSE, Y-ACHSE, durchmesser X-ACHSE, durchmesser Y-ACHSE)
        painter.drawEllipse(50, 50, 100, 100)

        # Ändere die Zeichenfarbe auf Grün
        painter.setPen(QPen(Qt.GlobalColor.green, 2))


        # Liniendicke ändern + Farbe + Style
        # pen = QPen()
        # pen.setColor(QColor("red"))
        # pen.setWidth(25)
        # pen.setStyle(Qt.PenStyle.DashDotDotLine()


        # Zeichne eine Ellipse
        painter.drawEllipse(200, 50, 100, 100)

        # Zeichne einen Kreis
        painter.drawEllipse(200, 200, 100, 100)

        # Zeichne ein Quadrat
        painter.drawRect(50, 200, 100, 100)

        # Zeichne eine Linie
        painter.drawLine(50, 350, 350, 350)

        # Zeichne den Text
        painter.setFont(QFont("Arial", 12))
        painter.drawText(150, 390, "Zeichenprogramm")
