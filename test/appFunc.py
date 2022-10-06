from appQt import MyWindow
from PyQt5 import QtWidgets
import sys


class QtApp(MyWindow):
    def __init__(self):
        MyWindow.__init__(self)

    def text_edit(self):
        self.tex.setText('ok2')


app = QtWidgets.QApplication(sys.argv)
window = QtApp()
window.setWindowTitle("Test")
window.resize(300, 200)
window.show()
sys.exit(app.exec_())