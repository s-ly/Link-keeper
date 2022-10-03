# Хранитель ссылок 1.6 alpha, служит для децентрализованного хранения ссылок.
# Основной модуль

from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui # для кнопки открытия URL
import ui_v2               # наш дизайн окна (из файла)
import json


class MyWindow(QtWidgets.QWidget):
    """Базовая форма"""
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        """Наполнение графическими элементами базовой формы."""
        self.button = QtWidgets.QPushButton("Добавить новую карточку")
        self.button2 = QtWidgets.QPushButton("Функция 1 - вывод данных карточек.")
        self.button3 = QtWidgets.QPushButton("Функция 2 - чтение данных.")
        self.button4 = QtWidgets.QPushButton("Функция 3 - запись данных в файл.")
        self.button5 = QtWidgets.QPushButton("Загрузить карточки")
        self.button6 = QtWidgets.QPushButton("Сохранить карточки")
        self.button7 = QtWidgets.QPushButton("Открыть все карточки")

        # порождаем 3 лайоута
        self.buttonLayout = QtWidgets.QGridLayout() # дочерний для верхних кнопок
        self.cardsLayout = QtWidgets.QVBoxLayout() # дочерний для карточек
        self.mainLayout = QtWidgets.QVBoxLayout() # главный, для двух дочерних

        # цыфры позиционируют кнопки по колонкам и строкам
        # addWidget(widget, row, columnt, row_span=1, column_span=1)
        self.buttonLayout.addWidget(self.button, 0, 0, 1, 2)
        self.buttonLayout.addWidget(self.button5, 1, 0, 1, 2)
        self.buttonLayout.addWidget(self.button6, 2, 0)
        self.buttonLayout.addWidget(self.button7, 2, 1, 1,1)

        self.setLayout(self.mainLayout) # задаём главный лайоут
        self.mainLayout.addLayout(self.buttonLayout) # помещаем дочерний в главный
        self.mainLayout.addLayout(self.cardsLayout) # помещаем дочерний в главный

        self.button.clicked.connect(self.generate_group)        # обработка сигнала для генерации
        # self.my_signal_get_cursor_coordinate.connect(self.get_cursor_coordinate) # обработка сигнала из группы для поиска координат курсора

        # эти обработчики пока вроде не нужны
        self.button2.clicked.connect(self.testPrint)            # обработка тестовой функции
        self.button3.clicked.connect(self.readingData)          # обработка функции чтения данных с карточек
        self.button4.clicked.connect(self.writingDataToFile)    # обработка функции запись данных в файл

        self.button5.clicked.connect(self.loadingFromFile)      # обработка функции загрузка из файла
        self.button6.clicked.connect(self.saveCards)            # обработка функции сохранить карточки
        self.button7.clicked.connect(self.openAllCards)         # обработка функции "открыть все карточки"

        self.list_obj = [] # список экземпляров карточек
        self.dict_data = {} # словарь только атрибутов карточек

    def openAllCards(self):
        """Открывает все карточки."""
        print("openAllCards")
        for i in self.list_obj:
            i.openUrl()

    def get_cursor_coordinate(self):
        pass

    def mousePressEvent(self, event):
        """РАЗРАБОТКА!!!"""
        # self.grabMouse() # захват мыши

        xx = event.globalX()
        yy = event.globalY()

        print ("11")
        print (xx, yy)
        # self.grabMouse() # захват мыши

    def mouseReleaseEvent(self, event):
        """РАЗРАБОТКА!!!"""
        # self.grabMouse() # захват мыши

        xxx = event.globalX()
        yyy = event.globalY()

        print ("12")
        print (xxx, yyy)
        # self.releaseMouse() # отпускаем мышь

    def mouseMoveEvent(self, event):
        x2 = event.globalX()
        y2 = event.globalX()
        print (x2, y2)

    def saveCards(self):
        """Сохранить карточки. Удобная унопка для пользователя.
        Комбинирует несколько действий в одной кнопке."""
        self.readingData()          # обработка функции чтения данных с карточек
        self.writingDataToFile()    # обработка функции запись данных в файл

        """Делаем два раза, так-как с одного раза не срабатывает, если карточек нет.
        Необходимо, разобраться, это не дело."""
        self.readingData()          # обработка функции чтения данных с карточек
        self.writingDataToFile()    # обработка функции запись данных в файл

    def loadingFromFile(self):
        """загрузка из файла"""
        print("Загрузка из файла.")

        """удаляем все карточки"""
        for i in self.list_obj:
            i.groupBox.setParent(i)  # удаление (вроде) группы из главной формы

        self.resize(550, 150)  # размер главного окна по умолчанию
        self.list_obj = [] # обнуляем список экземпляров карточек
        self.dict_data = {} # обнуляем словарь только атрибутов карточек

        """Чтение json файла и его декодирование в словарь."""
        with open('data.json') as obj_file:
            self.dict_data = json.loads(obj_file.read())
        # print(self.dict_data)

        """Автоматическое создание карточек"""
        for k, v in self.dict_data.items():
            # print(k, v)
            id_fromFile = int(k)
            url_fromFile = v['url']
            description_fromFile = v['description']
            img_fromFile = v['img']
            # print(id_fromFile, url_fromFile, description_fromFile)
            self.auto_generate_group(id_fromFile, url_fromFile, description_fromFile, img_fromFile)

    def writingDataToFile(self):
        """Запись данных во внешний файл."""
        print("Запись во внешний файл.")

        """Наполнение словаря атрибутов карточек данными."""
        for i in self.list_obj:
            self.dict_data[str(i.id)] = {'url': i.url, 'description': i.description, 'img': i.img}

        """Кодирование словаря в данные json, и запись данных в файл."""
        with open('data.json', 'w') as obj_file:
            json.dump(self.dict_data, obj_file, indent=4) # indent - отступ
        self.dict_data = {} # очищаем

    def readingData(self):
        """Чтение всех полей карточек и запись эти данных
        в соответствующие атрибуты карточек."""
        print("Чтение полей карточек.")
        for i in self.list_obj:
            i.description = i.lineEdit.text()
            i.url = i.lineEdit_2.text()

    def auto_generate_group(self, id_file, url_file, description_file, img_file):
        """Автоматически создать объект формы (карточку) с кнопками из файла.
        Но это плохо сделанно, дублирую метод."""
        self.myUi = MyUi(self)                                        # создаём карточку
        self.myUi.my_signal.connect(self.deleteGroup)                 # обработка сигнала из группы для удаления карточки
        self.cardsLayout.addWidget(self.myUi.groupBox)                       # добавляем группу, в которой всё есть
        self.resize(550, self.height() + 160)                         # наращиваем высоту окна

        self.myUi.id = id_file                                        # присваиваем объекту карточки id
        self.myUi.url = url_file                                      # присваиваем объекту карточки url
        self.myUi.description = description_file                      # присваиваем объекту карточки description
        self.myUi.img = img_file                                      # присваиваем объекту карточки img

        self.myUi.lineEdit_2.setText(self.myUi.url)                   # вводим url в текстовое поле
        self.myUi.lineEdit.setText(self.myUi.description)             # вводим description в текстовое поле
        self.myUi.groupBox.setTitle("Карточка " + str(self.myUi.id))  # подпись к карточке = id

        # загрузка картинки
        if self.myUi.img != None:
            print("в img " + str(self.myUi.id)  + " что то есть")

            # разгребаем байтовые данные
            self.bytes_img = bytes(self.myUi.img, encoding='cp855')
            self.myUi.pixmap2 = QtGui.QPixmap()
            self.myUi.pixmap2.loadFromData(self.bytes_img, "PNG")
            self.myUi.label_img.setPixmap(self.myUi.pixmap2)
        else:
            print("в img " + str(self.myUi.id)  + " пусто")
        self.list_obj.append(self.myUi)                               # добавляем экземпляр карточки в список


    def generate_group(self):
        """Создать объект формы (карточку) с кнопками из файла"""
        self.myUi = MyUi(self)                                        # создаём карточку
        self.myUi.my_signal.connect(self.deleteGroup)                 # обработка сигнала из группы для удаления карточки
        # self.myUi.my_signal_loadImg_fromFile.connect(self.openImgFromFile)       # обработка сигнала из группы для открытия картинки из файла
        self.cardsLayout.addWidget(self.myUi.groupBox)                       # добавляем группу, в которой всё есть
        self.resize(550, self.height() + 160)                         # наращиваем высоту окна

        self.myUi.id = self.id_create()                               # присваиваем объекту карточки id
        self.myUi.groupBox.setTitle("Карточка " + str(self.myUi.id))  # подпись к карточке = id

        self.list_obj.append(self.myUi)                               # добавляем экземпляр карточки в список

    def deleteGroup(self):
        """Удаление карточки"""
        self.resize(550, self.height() - 160)   # уменьшаем высоту окна

        """Поиск flag == True среди экземпляров карточек, и их удаление из списка карточек."""
        for i in self.list_obj:
            if i.flag == True:
                self.list_obj.remove(i)

    def testPrint(self):
        """Печать списка экземпляров карточек, вывод данных всех карточек и число карточек."""
        print("\nTest func")
        for i in self.list_obj:
            print("id: " + str(i.__dict__['id']) +
            " description: " + str(i.__dict__['description']) +
            " URL: " + str(i.__dict__['url']))
        print("len list: " + str(len(self.list_obj)))

    def id_create(self):
        """Создание id для новой карточки"""
        id_list = [] # список для всех id

        for i in self.list_obj: # наполняем список существующих id
            id_list.append(i.id)

        """от 0 до бесконечности проверяем id_test, содержится ли он в списке id"""
        id_test = 0
        while True:
            if id_test in id_list:
                id_test += 1
            else: # найден наименьший уникальный id
                break

        return id_test



class MyUi(QtWidgets.QWidget, ui_v2.Ui_Form):
    """Форма с кнопками из ui_v2.py"""
    my_signal = QtCore.pyqtSignal()   # сигнал для удаления карточки
    my_signal_get_cursor_coordinate = QtCore.pyqtSignal()   # сигнал для активации поиска курсора

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # вызываем конструктор базового класса
        self.setupUi(self)                         # настройка нашего дизайна окна из файла

        self.id = None          # id экземпляра карточки
        self.url = None         # хрение url в карточке
        self.description = None # описание карточки
        self.img = None         # картинка в байтовом потоке

        self.flag = False # флаг для удаления
        # self.flagCreateImg = False # флаг, True если была определена область экрана для принскрина

        # Обработка сигналов
        self.pushButton.clicked.connect(self.openUrl)
        self.pushButton_2.clicked.connect(self.del_group)
        self.pushButton_3.clicked.connect(self.openImgLoadImg)
        self.pushButton_4.clicked.connect(self.createSubWindow)

    def del_group(self):
        """Удаление группы"""
        self.flag = True               # флаг на удаление из списка экземпляров карточек
        self.groupBox.setParent(self)  # удаление (вроде) группы из главной формы
        self.my_signal.emit()          # излучение сигнала из группы, что группа удалена

    def openUrl(self):
        """Открыть URL в браузере по умолчанию"""
        print("сработала кнопка 1")
        # testUrl = QtCore.QUrl('https://ya.ru/') # создаём (кажется) оюъект url
        # QtGui.QDesktopServices.openUrl(testUrl) # открываем url программой по умолчанию
        url = QtCore.QUrl(str(self.url)) # создаём (кажется) объект url из атрибута url
        if not QtGui.QDesktopServices.openUrl(url): # открываем url программой по умолчанию
            print("Херовый url")

    def openImgLoadImg(self):
        """Открывает картинку и загружаем её в карточку"""
        # self.my_signal_loadImg_fromFile.emit(self.id)          # излучение сигнала из группы, что надо загрузить картинку из файла

        print("img ok")
        self.fileImg = QtWidgets.QFileDialog.getOpenFileName() # создаёт диалог выбора файла
        print(self.fileImg)
        print(self.fileImg[0]) # отделяем часть информации

        # грузим картинку в лейбл
        self.pixmap = QtGui.QPixmap(self.fileImg[0]) # грузанули в pixmap
        self.pixmap = self.pixmap.scaled(128, 128) # подгоняем размер картинки
        self.label_img.setPixmap(self.pixmap) # помещаем pixmap в наш лейбел

        # создать байтовый поток картинки
        self.myBytes = QtCore.QByteArray()
        self.myBuffer = QtCore.QBuffer(self.myBytes)
        self.myBuffer.open(QtCore.QIODevice.WriteOnly)
        self.pixmap.save(self.myBuffer, "PNG")

        # сохраняем байтовый поток картинки в атрибут карточки img
        self.img = str(self.myBytes, encoding='cp855') # простобайты в виде обычной строки

    def createImg(self, scaleWindow2):
        """Дублируем строки, ай-яй-яй!!! Создать изображение из принскрина по координатам:
        принимает специальный объект scaleWindow2, в котором хранятся 4-е координаты габаритов подОкна."""

        # вот как этот кусок кода работает, я доконца и не понял
        self.screen = QtWidgets.QApplication.primaryScreen() # вот это самое непонятное
        self.winid = QtWidgets.QApplication.desktop().winId() # идентификатор окон винды (откуда брать скриншот)

        # берём скриншот и суём в pixmap
        self.pixmap = self.screen.grabWindow(self.winid,
                                             self.scaleWindow2.left(),
                                             self.scaleWindow2.top(),
                                             self.scaleWindow2.width(),
                                             self.scaleWindow2.height())

        self.pixmap = self.pixmap.scaled(128, 128) # подгоняем размер картинки
        self.label_img.setPixmap(self.pixmap) # помещаем pixmap в наш лейбел

        # создать байтовый поток картинки
        self.myBytes = QtCore.QByteArray()
        self.myBuffer = QtCore.QBuffer(self.myBytes)
        self.myBuffer.open(QtCore.QIODevice.WriteOnly)
        self.pixmap.save(self.myBuffer, "PNG")

        # сохраняем байтовый поток картинки в атрибут карточки img
        self.img = str(self.myBytes, encoding='cp855') # простобайты в виде обычной строки

    def createSubWindow(self):
        """создаём дочернее окно, по нему попытаемся получить координаты"""
        self.window2 = QtWidgets.QWidget()
        self.window2.setWindowTitle("Выберете область экрана")
        self.window2.resize(256, 256)
        self.window2.setWindowOpacity(0.75) # прозрачность подОкна

        self.but = QtWidgets.QPushButton("Выбрать", self.window2) # кнопка подОкна
        self.but.clicked.connect(self.closeSubWindow) # обработка сигнал нажатия на кнопу подОкна

        self.window2.show() # показать подОкно

    def closeSubWindow(self):
        """Отработка закрытия дочернего окна"""
        # получаем координаты подОкна без учёта заголовка: left(), top(), width(), height(),
        # кладём их в специальный объект self.scaleWindow2.
        self.scaleWindow2 = self.window2.geometry()

        print("system: захват координат:")
        print(self.id)
        print(self.scaleWindow2.left(), self.scaleWindow2.top())
        print(self.scaleWindow2.width(), self.scaleWindow2.height())

        self.flagCreateImg = True # меняем флаг, совершён захват области для принскрина
        self.window2.close() # закрыть подОкно
        self.createImg(self.scaleWindow2) # захват был совершён, создаём принскрин по захваченным координатам



if __name__ == "__main__":                        # запуск приложения, если это исполняемый модуль
    import sys
    app = QtWidgets.QApplication(sys.argv)        # Создание приложения
    window = MyWindow()                           # Создание экземпляра окна (может быть несколько)
    window.setWindowTitle("Link keeper")
    window.resize(550, 100)
    # window.show()                                 # показать окно
    """приколхозим скролл"""
    scroll = QtWidgets.QScrollArea()
    scroll.setWindowTitle("Link keeper 1.6 alpha")
    scroll.setWidget(window)
    scroll.resize(570,200)
    scroll.setMinimumSize(570, 200)
    scroll.setMaximumWidth(570)
    scroll.show()

    sys.exit(app.exec_())                         # бесконечно слушаем события
