# импорт компонентов GUI
from PyQt5 import QtCore, QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Привет, Мир!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("&Закрыть окно")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("ООП-стиль создания окна")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())



"""
# список параметров, переданных в командной строке (argv) и exit()
import sys

# Объект приложения
app = QtWidgets.QApplication(sys.argv)

# объект окна
window = QtWidgets.QWidget()

# заголовок окна
window.setWindowTitle("Первая программа на PyQt")

# размер окна
window.resize(300, 70)

# текст и кнопка
label = QtWidgets.QLabel("<center>Привет Мир!</center>")
btnQuit = QtWidgets.QPushButton("&Закрыть окно")

# вертикальный контейнер
vbox = QtWidgets.QVBoxLayout()

# добавление в контейнер объектов GUI
vbox.addWidget(label)
vbox.addWidget(btnQuit)

# добавляем контейнер в окно
window.setLayout(vbox)

# Для кнопки назначает обработчик сигнала clicked().
# Метод connect назначает действие (выход).
btnQuit.clicked.connect(app.quit)

# Выводит окно на экран.
window.show()

# Бесконечный цикл обработки событий.
sys.exit(app.exec_())

"""