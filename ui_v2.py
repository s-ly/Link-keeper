# ui карточки


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(611, 193)        

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 550, 161))
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 50, 13))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 365, 20))
        self.lineEdit.setObjectName("lineEdit")        

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 74, 47, 13))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 70, 335, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # кнопки 4x2
        self.butOpenCard = QtWidgets.QPushButton(self.groupBox)
        self.butOpenCard.setGeometry(QtCore.QRect(10, 98, 180, 23))
        self.butOpenCard.setObjectName("butOpenCard")
        
        self.butDeleteCard = QtWidgets.QPushButton(self.groupBox)
        self.butDeleteCard.setGeometry(QtCore.QRect(10, 125, 180, 23))
        self.butDeleteCard.setObjectName("pushButton_2")

        self.butScreenshot = QtWidgets.QPushButton(self.groupBox)
        self.butScreenshot.setGeometry(QtCore.QRect(196, 98, 180, 23))
        self.butScreenshot.setObjectName("pushButton_4")

        self.butLoadImage = QtWidgets.QPushButton(self.groupBox)
        self.butLoadImage.setGeometry(QtCore.QRect(196, 125, 180, 23))
        self.butLoadImage.setObjectName("pushButton_3")    

        icon_OpenCard = QtGui.QIcon()
        icon_DeleteCard = QtGui.QIcon()
        icon_Screenshot = QtGui.QIcon()
        icon_LoadImage = QtGui.QIcon()
        icon_OpenCard.addPixmap(QtGui.QPixmap("ico/book.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_DeleteCard.addPixmap(QtGui.QPixmap("ico/delete.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_Screenshot.addPixmap(QtGui.QPixmap("ico/camera.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_LoadImage.addPixmap(QtGui.QPixmap("ico/picture.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butOpenCard.setIcon(icon_OpenCard)
        self.butDeleteCard.setIcon(icon_DeleteCard)
        self.butScreenshot.setIcon(icon_Screenshot)
        self.butLoadImage.setIcon(icon_LoadImage)
        self.butOpenCard.setToolTip("Открыть ссылку или папку")    
        self.butDeleteCard.setToolTip("Удалить карточку")    
        self.butScreenshot.setToolTip("Снимок области экрана")    
        self.butLoadImage.setToolTip("Загрузить файл фото")    

        # для картинки
        self.label_img = QtWidgets.QLabel(self.groupBox)
        self.label_img.setGeometry(QtCore.QRect(390, 20, 128, 128))
        self.label_img.setStyleSheet('background-color: grey')
        self.label_img.setObjectName("label_img")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Карточка"))
        self.label.setText(_translate("Form", "Описание"))
        self.label_2.setText(_translate("Form", "URL"))
        
        self.butOpenCard.setText(_translate("Form", "Открыть"))
        self.butDeleteCard.setText(_translate("Form", "Удалить"))
        self.butLoadImage.setText(_translate("Form", "Загрузить фото"))
        self.butScreenshot.setText(_translate("Form", "Снимок экрана"))
        
        self.label_img.setText(_translate("Form", "     нет изображения"))
