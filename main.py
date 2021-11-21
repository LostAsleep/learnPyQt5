from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys  # Needed for access to command line arguments.


class MainWindow(QMainWindow):
    """Subclass QMainWindow to customize your application's main window."""

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title will be passed to the function.
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is discarded in the lambda and the
        # function is called without parameters
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        # SIGNAL: The connected function wil be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter. Extra data is passed from
        # within the lambda.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        # This sets the window title which will trigger all the above signals
        # sending the new title to the attached functions or lambdas as the
        # first parameter.
        self.setWindowTitle("My first App")

        label = QLabel("This is interesting.")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)  # QMainWindow specific function

    # SLOT: This accepts a string, e.g. the window title, and prints it
    def onWindowTitleChange(self, s):
        print(s)

    # SLOT: This has default parameters and can be called without a value
    def my_custom_fn(self, a="HELLO!", b=5):
        print(a, b)

    def contextMenuEvent(self, event):
        """Intercept the contextMenuEvent (right click)."""
        print("Context menu event!")
        # And still trigger the default event (parent).
        super(MainWindow, self).contextMenuEvent(event)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
