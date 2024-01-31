"""
Using tutorial at: https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/
NOTE: Solution found at:
https://stackoverflow.com/questions/56726580/no-name-qapplication-in-module-pyqt5-qtwidgets-error-in-pylint
"""

# NOTE: the following lines solved the issues where 
# the system could not locate libraries like QApplication
# Solution: https://stackoverflow.com/questions/56726580/no-name-qapplication-in-module-pyqt5-qtwidgets-error-in-pylint
# from PyQt5 import QtGui
from PyQt5 import QtWidgets
# from PyQt5 import QtCore

import sys


# Define the window here
# class MainWindow(QMainWindow):
#     pass

# This line accepts command line arguments
# If there are no command line arguments just pass in []
# app = QtWidgets.QApplication(sys.argv)


if __name__ == '__main__':
    # window = MainWindow()
    # window.show()

    app = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    window.setWindowTitle("Test")
    window.show()

    # Start the event loop
    # REM: exec is a keyword in Python; we add the underscore to circumvent that
    # NOTE: This will run, but since there is no window nothing will appear if no window has been defined
    app.exec_()