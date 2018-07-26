from PyQt5 import Qt
import sys

def entry_point():
    app = Qt.QApplication(sys.argv)
    label = Qt.QLabel()
    label.setText('Hello Kyle')
    label.show()
    app.exec()