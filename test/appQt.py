from PyQt5 import QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.but = QtWidgets.QPushButton('test')
        self.tex = QtWidgets.QLineEdit('test text')
        self.lay = QtWidgets.QVBoxLayout()

        self.lay.addWidget(self.tex)
        self.lay.addWidget(self.but)
        self.setLayout(self.lay)

        # self.but.clicked.connect(self.text_edit)

    # def text_edit(self):
    #     self.tex.setText('ok')


# app = QtWidgets.QApplication(sys.argv)
# window = MyWindow()
# window.setWindowTitle("Test")
# window.resize(300, 200)
# window.show()
# sys.exit(app.exec_())