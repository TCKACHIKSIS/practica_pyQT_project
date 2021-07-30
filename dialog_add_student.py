
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 250, 321, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(10, 20, 113, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_last_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(10, 60, 113, 21))
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.lineEdit_class = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_class.setGeometry(QtCore.QRect(10, 100, 113, 21))
        self.lineEdit_class.setObjectName("lineEdit_class")
        self.lineEdit_math = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_math.setGeometry(QtCore.QRect(10, 140, 113, 21))
        self.lineEdit_math.setObjectName("lineEdit_math")
        self.lineEdit_phys = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_phys.setGeometry(QtCore.QRect(10, 190, 113, 21))
        self.lineEdit_phys.setObjectName("lineEdit_phys")
        self.lineEdit_comp_science = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_comp_science.setGeometry(QtCore.QRect(10, 230, 113, 21))
        self.lineEdit_comp_science.setObjectName("lineEdit_comp_science")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 140, 211, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 190, 191, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(130, 230, 221, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Введите имя"))
        self.label_2.setText(_translate("Dialog", "Введите фамилию"))
        self.label_3.setText(_translate("Dialog", "Введите класс"))
        self.label_4.setText(_translate("Dialog", "Введите оценку по математике"))
        self.label_5.setText(_translate("Dialog", "Введите оценку по физике"))
        self.label_6.setText(_translate("Dialog", "Введите оценку по информатике"))
