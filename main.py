from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys  # Needed for access to command line arguments.


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My First App")

        label = QLabel("This is interesting.")

        # The 'Qt' namespace has a lot of attributes to customize
        # widgets. See: https://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)  # QMainWindow specific function


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

