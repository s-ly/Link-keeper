# Класс карточек


from PyQt5 import QtCore, QtWidgets, QtGui
import os   # открытие ссылок и файлов
import ui_v2 # наш дизайн окна (из файла)


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
        """ Открыть URL в браузере по умолчанию.
        Парсим строку URL, если она начинается с 'http',
        то открываем способом PyQt, иначе считаем строку адресом в Windows,
        и открываем её командой 'cmd'. Это нужно, так-как иногда в URL появляются
        спец.символы, например знак '?'. С таким символом cmd не справляется."""
        print("сработала кнопка 1")        

        url = str(self.url)  
        url_parse = url[0:4]
        if url_parse == 'http':
            url = QtCore.QUrl(str(self.url)) # создаём (кажется) объект url из атрибута url
            if not QtGui.QDesktopServices.openUrl(url): # открываем url программой по умолчанию
                print("Херовый url")
        else:
            url_cmd = r"explorer.exe " + url   # соединяем с командой
            os.system(url_cmd)                # открываем


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