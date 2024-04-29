from const import *
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Argenchess(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciar_app()

    def iniciar_app(self):
        self.setGeometry(100,100,MAX_HEIGHT,MAX_WIDTH)
        self.setWindowTitle("Argenchess")

        icon_path = 'horse.png'
        self.setWindowIcon(QIcon(icon_path))
        self.generar_menu()
        self.show()

    def generar_menu(self):
        frame_argenchess = QFrame()
        frame_argenchess.setGeometry(190,80,271,311)
        frame_argenchess.setStyleSheet()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    argenchess = Argenchess()
    sys.exit(app.exec()) 