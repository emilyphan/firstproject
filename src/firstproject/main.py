from PyQt5 import Qt
import sys

def entry_point():
    app = Qt.QApplication(sys.argv)
    label = Qt.QLabel()
    label.setText('Hello Emily')
    label.show()
    app.exec()