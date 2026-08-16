# PyQt5 Qlabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Welcome to ITE_M2")
        self.setWindowIcon(QIcon("tos_tv_srok.png"))

        label = QLabel("Hello World", self)
        label.setFont(QFont("Nillambari ", 23))
        label.setGeometry(0, 0, 300, 100)
        label.setStyleSheet("color: red;"
                            "background-color: #1eccfc;"
                            "font_weight: bold;"
                            "font_style: italic;"
                            "text-decoration: underline;")
        # label.setAlignment(Qt.AlignTop) # vertically top
        # label.setAlignment(Qt.AlignBottom) # vertically bottom
        # label.setAlignment(Qt.AlignVCenter) # vertically center

        # label.setAlignment(Qt.AlignRight) # horizontally right
        # label.setAlignment(Qt.AlignHCenter) # horizontally center
        # label.setAlignment(Qt.AlignLeft) # horizontally left

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # center & top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # center & bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # center & center
        
        label.setAlignment(Qt.AlignCenter)
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


main()