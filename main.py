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
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("The main toolbar")
        # Prevent the toolbar from being removed via right-click menu
        toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.addToolBar(toolbar)
        
        # You must also pass in any QObject to act as the parent for the action
        # here we’re passing self as a reference to our main window. Strangely
        # for QAction the parent element is passed in as the final parameter.
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")  # For the status bar
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))


    def onMyToolBarButtonClick(self, s):
        """The signal passed indicates whether the button is checked and returns a bool."""
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

