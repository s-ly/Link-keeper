# Создаёт простое окно с надписью "Привет, Мир!" и
# кнопкой "Закрыть окно".


# Берём класс QWidget для создания простого окна
from PyQt5 import QtWidgets 

# Берём класс Qt для для выравнивания
from PyQt5 import QtCore


class MyWindow(QtWidgets.QWidget):
    """ Создаём свой класс, и наследуем его от QWidget.
    Это простое окно. """

    def __init__(self, parent=None):
        """ Метод - конструктор класса. Принимает ссылку на экземпляр класса,
        и на родительский компонент parent. В нём, ниже, вызывается ещё один конструктор,
        уже базового класса. Ему передаётся ссылка на родительский компонент. """
        
        QtWidgets.QWidget.__init__(self, parent)

        # текст и кнопка
        self.label = QtWidgets.QLabel("Привет, Мир!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter) # выравнивание по центру
        self.btnQuit = QtWidgets.QPushButton("&Закрыть окно")
        
        self.vbox = QtWidgets.QVBoxLayout() # вертикальный контейнер
        
        # добавление в контейнер объектов GUI
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        
        self.setLayout(self.vbox)   # добавляем контейнер в окно

        # Для кнопки назначает обработчик сигнала clicked().
        # Метод connect назначает действие (выход).
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


# Запускать только если запускается как основная программа,
# тоесть при импорте этого модуля __name__ не будет равен __main__,
# и запуска не будет. Это нужно что бы можно было импортировать модуль в другие программы.
if __name__ == "__main__":
    # список параметров, переданных в командной строке (argv) и exit()
    import sys   

    app = QtWidgets.QApplication(sys.argv)            # Объект приложения
    window = MyWindow()                               # объект окна
    window.setWindowTitle("ООП-стиль создания окна")  # заголовок окна
    window.resize(300, 70)                            # размер окна
    window.show()                                     # Выводит окно на экран.
    sys.exit(app.exec_())                             # Бесконечный цикл обработки событий.