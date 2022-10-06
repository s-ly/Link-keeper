from appQt import MyWindow
from PyQt5 import QtWidgets

class FuncApp(MyWindow):
    def __init__(self):
        MyWindow.__init__(self)
    
    def test(self):
        print('tts')