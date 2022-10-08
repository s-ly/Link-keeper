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
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 98, 180, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 125, 180, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(196, 98, 180, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(196, 125, 180, 23))
        self.pushButton_3.setObjectName("pushButton_3")        

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
        
        self.pushButton.setText(_translate("Form", "Открыть URL или DIR"))
        self.pushButton_2.setText(_translate("Form", "Удалить карточку"))
        self.pushButton_3.setText(_translate("Form", "Загрузить фото"))
        self.pushButton_4.setText(_translate("Form", "Снимок экрана"))
        
        self.label_img.setText(_translate("Form", "     нет изображения"))
