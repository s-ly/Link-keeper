# импорт компонентов GUI
from sqlite3 import connect
from PyQt5 import QtWidgets

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
