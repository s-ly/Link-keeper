# Хранитель ссылок 1.7, служит для децентрализованного хранения ссылок.
# Основной модуль

# from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui # для кнопки открытия URL
# import ui_v2               # наш дизайн окна (из файла)
import json
# import os   # открытие ссылок и файлов
from card import MyUi # класс карточек

class MyWindow(QtWidgets.QWidget):
    """Базовая форма"""
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Наполнение графическими элементами базовой формы.   
        self.fileNameDefault = "Сохраните или откройте файл. Изменения вступают в силу после сохранения файла."   
        self.linefileName = QtWidgets.QLineEdit(self.fileNameDefault)   # Текс имя файла данных
        self.butAddNewCard = QtWidgets.QPushButton("Добавить новую карточку")
        self.button2 = QtWidgets.QPushButton("Функция 1 - вывод данных карточек.")
        self.button3 = QtWidgets.QPushButton("Функция 2 - чтение данных.")
        self.button4 = QtWidgets.QPushButton("Функция 3 - запись данных в файл.")
        self.butSaveFileAs = QtWidgets.QPushButton("Сохранить файл как")
        self.butSaveFile = QtWidgets.QPushButton("Сохранить файл")
        self.butOpenAllCards = QtWidgets.QPushButton("Открыть все карточки")
        self.butOpenFile = QtWidgets.QPushButton("Открыть файл")
        self.butNewFile = QtWidgets.QPushButton("Новый файл")
        
        # Настройка элементов
        # self.butt_fileName.setReadOnly(True) # только чтение
        self.linefileName.setFrame(False) # показывать рамку
        self.linefileName.setEnabled(False)
        self.butSaveFile.setEnabled(False)

        # порождаем 3 лайоута
        self.buttonLayout = QtWidgets.QGridLayout() # дочерний для верхних кнопок
        self.cardsLayout = QtWidgets.QVBoxLayout() # дочерний для карточек
        self.mainLayout = QtWidgets.QVBoxLayout() # главный, для двух дочерних

        # цифры позиционируют кнопки по колонкам и строкам
        # номер строки, номер колонки, высота элемента, ширина элемента
        self.buttonLayout.addWidget(self.linefileName , 0, 0, 1, 4)

        self.buttonLayout.addWidget(self.butNewFile, 1, 0, 1, 1)
        self.buttonLayout.addWidget(self.butOpenFile , 1, 1, 1, 1)
        self.buttonLayout.addWidget(self.butSaveFile, 1, 2, 1, 1)
        self.buttonLayout.addWidget(self.butSaveFileAs, 1, 3, 1, 1)

        self.buttonLayout.addWidget(self.butAddNewCard, 2, 0, 1, 2)
        self.buttonLayout.addWidget(self.butOpenAllCards, 2, 2, 1, 2)


        # цифры позиционируют кнопки по колонкам и строкам
        # номер строки, номер колонки, высота элемента, ширина элемента
        # self.buttonLayout.addWidget(self.butt_fileName , 0, 0, 1, 3)
        # self.buttonLayout.addWidget(self.butOpenFile , 1, 1, 1, 1)
        # self.buttonLayout.addWidget(self.button, 1, 0, 1, 1)
        # self.buttonLayout.addWidget(self.button5, 1, 2, 1, 1)
        # self.buttonLayout.addWidget(self.button6, 2, 0, 1, 1)
        # self.buttonLayout.addWidget(self.button7, 2, 1, 1, 1)
        # self.buttonLayout.addWidget(self.butNewFile, 2, 2, 1, 1)
        

        self.setLayout(self.mainLayout) # задаём главный лайоут
        self.mainLayout.addLayout(self.buttonLayout) # помещаем дочерний в главный
        self.mainLayout.addLayout(self.cardsLayout) # помещаем дочерний в главный

        self.butAddNewCard.clicked.connect(self.generate_group)        # обработка сигнала для генерации
        # self.my_signal_get_cursor_coordinate.connect(self.get_cursor_coordinate) # обработка сигнала из группы для поиска координат курсора

        # эти обработчики пока вроде не нужны
        self.button2.clicked.connect(self.testPrint)            # обработка тестовой функции
        self.button3.clicked.connect(self.readingData)          # обработка функции чтения данных с карточек
        self.button4.clicked.connect(self.writingDataToFile)    # обработка функции запись данных в файл

        self.butSaveFileAs.clicked.connect(self.saveFileAs)           # обработка функции сохранить файл как
        self.butSaveFile.clicked.connect(self.saveCards)            # обработка функции сохранить карточки
        self.butOpenAllCards.clicked.connect(self.openAllCards)         # обработка функции "открыть все карточки"

        self.butOpenFile.clicked.connect(self.openFileDialo)         # обработка функции "открыть все карточки"
        self.butNewFile.clicked.connect(self.newFile)         # обработка функции "новый файл"

        self.list_obj = [] # список экземпляров карточек
        self.dict_data = {} # словарь только атрибутов карточек

        self.fileName = "" # Имя файла данных, с которым работает приложение

    
    # def newFile(self):
    #     fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Новый файл', QtCore.QDir.currentPath(), 'Image files (*.json)')[0]
    #     if fname == '':
    #         print('no')
    #     else:
    #         self.deleteAllCards()
    #         self.linefileName.setText(fname)
    #         self.saveCards()
    #         self.loadingFromFile()
    #         self.butSaveFile.setEnabled(True) # файл можно сохранять
    
    
    def newFile(self):
        self.deleteAllCards()
        self.linefileName.setText(self.fileNameDefault)
        self.butSaveFile.setEnabled(False) # файл нельзя сохранять
        
    
    
    def saveFileAs(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить файл как', QtCore.QDir.currentPath(), 'Image files (*.json)')[0]
        if fname == '':
            print('no')
        else:
            print(fname)
            self.linefileName.setText(fname)
            self.saveCards()
            self.butSaveFile.setEnabled(True) # файл можно сохранять

    
    def openFileDialo(self):
        """ Диалог открытия файла.
        QtCore.QDir.currentPath() - текущий каталок исполняемой программы. """

        print('testing')
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Открыть файл', QtCore.QDir.currentPath(), 'Image files (*.json)')[0]
        if fname == '':
            print('no')
        else:
            print(fname)
            self.linefileName.setText(fname)
            self.loadingFromFile()
            self.butSaveFile.setEnabled(True) # файл можно сохранять

    
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

    
    def deleteAllCards(self):
        """Удаляем все карточки"""
        for i in self.list_obj:
            i.groupBox.setParent(i)  # удаление (вроде) группы из главной формы

        self.resize(550, 150)  # размер главного окна по умолчанию
        self.list_obj = [] # обнуляем список экземпляров карточек
        self.dict_data = {} # обнуляем словарь только атрибутов карточек
    
    
    def loadingFromFile(self):
        """загрузка из файла"""
        print("Загрузка из файла.")

        self.deleteAllCards() # удаляем все карточки

        """Чтение json файла и его декодирование в словарь."""
        # получаем текущее имя файла данных из текстового поля
        self.fileName = self.linefileName.text() 

        with open(self.fileName) as obj_file:
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

        # получаем текущее имя файла данных из текстового поля
        self.fileName = self.linefileName.text() 
        
        """Кодирование словаря в данные json, и запись данных в файл."""
        with open(self.fileName, 'w') as obj_file:
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


if __name__ == "__main__":                        # запуск приложения, если это исполняемый модуль
    import sys
    app = QtWidgets.QApplication(sys.argv)        # Создание приложения
    window = MyWindow()                           # Создание экземпляра окна (может быть несколько)
    window.setWindowTitle("Link keeper")
    window.resize(550, 100)
    # window.show()                                 # показать окно
    """приколхозим скролл"""
    scroll = QtWidgets.QScrollArea()
    scroll.setWindowTitle("Link keeper 1.7")
    scroll.setWidget(window)
    scroll.resize(570,200)
    scroll.setMinimumSize(570, 200)
    scroll.setMaximumWidth(570)
    scroll.show()

    sys.exit(app.exec_())                         # бесконечно слушаем события
