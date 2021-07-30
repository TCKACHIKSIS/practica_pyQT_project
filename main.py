import sqlite3


class Student:
    def __init__(self, id, name, last_name, student_class):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.student_class = student_class


class Rating:
    def __init__(self, id, math, phys, comp_science):
        self.id = id
        self.math = math
        self.phys = phys
        self.comp_science = comp_science
        self.average_score = (math+phys+comp_science)/3


def load_start_values():
    student_list = [
        Student(1, "Егор", "Ткаченко", "11 А"),
        Student(2, "Вася", "Петров", "5 В"),
        Student(3, "Алексей", "Петухов", "5 В"),
        Student(4, "Павел", "Пехов", "11 А"),
        Student(5, "Сергей", "Алексеев", "7 Б")
    ]
    rating_list = [
        Rating(1, 5, 5, 5),
        Rating(2, 4, 3, 5),
        Rating(3, 4, 5, 5),
        Rating(4, 2, 5, 3),
        Rating(5, 3, 4, 4)
    ]

    for student in student_list:
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?);", [student.id, student.name, student.last_name, student.student_class])
        connect.commit()

    for rating in rating_list:
        cursor.execute("INSERT INTO rating VALUES (?, ?, ?, ?, ?);", [rating.id, rating.math, rating.phys, rating.comp_science, rating.average_score])
        connect.commit()


connect = sqlite3.connect('students.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER,
    student_name TEXT,
    last_name TEXT,
    student_class TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS rating(
    id INTEGER,
    math INTEGER,
    phys INTEGER ,
    computer_science INTEGER ,
    average_score FLOAT 
)
""")

connect.commit()
if len(list(cursor.execute("SELECT * FROM students"))) == 0:
    load_start_values()

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.list_of_student = []
        self.list_of_rating = []
        self.datatable_list = []
        self.class_list = set()
        self.add_student_window = SecondForm()
        self.last_id = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 701, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_student = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_student.setObjectName("add_student")
        self.horizontalLayout.addWidget(self.add_student)
        self.sort_by_rating = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sort_by_rating.setObjectName("sort_by_rating")
        self.horizontalLayout.addWidget(self.sort_by_rating)
        self.sort_by_class = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sort_by_class.setObjectName("sort_by_class")
        self.horizontalLayout.addWidget(self.sort_by_class)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 1000, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1000, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1000, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.hide()
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 30, 221, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.sort_averege_score_pannel = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.sort_averege_score_pannel.setContentsMargins(0, 0, 0, 0)
        self.sort_averege_score_pannel.setObjectName("sort_averege_score_pannel")
        self.tolowest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.tolowest.setStyleSheet("background-color: rgb(33, 255, 197);")
        self.tolowest.setObjectName("tolowest")
        self.sort_averege_score_pannel.addWidget(self.tolowest)
        self.tohighest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.tohighest.setStyleSheet("background-color: rgb(34, 255, 219);")
        self.tohighest.setObjectName("tohighest")
        self.sort_averege_score_pannel.addWidget(self.tohighest)

        self.input_class_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_class_line.setGeometry(405, 30, 155, 20)
        self.input_class_line.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.get_datatable_list()
        self.send_datatable_to_table()
        self.sort_by_rating.clicked.connect(lambda: self.show_sort_score_pannel())
        self.tohighest.clicked.connect(lambda: self.sort_by_average(-1))
        self.tolowest.clicked.connect(lambda: self.sort_by_average(1))
        self.sort_by_class.clicked.connect(lambda: self.show_class_panel())
        self.get_class_list()
        self.add_student.clicked.connect(lambda: self.show_add_student_dialog())
        self.tableWidget.itemChanged.connect(lambda: self.change_student(self.tableWidget.selectedItems()))

    def get_list_of_student(self):
        tmp_list_of_student = list(cursor.execute("SELECT * FROM students"))
        for student in tmp_list_of_student:
            self.list_of_student.append(Student(student[0], student[1], student[2], student[3]))
        self.last_id = len(self.list_of_student)

    def get_datatable_list(self):
        self.list_of_student.clear()
        self.datatable_list.clear()
        self.get_list_of_student()
        for student in self.list_of_student:
            tmp_rating = list(cursor.execute("SELECT * FROM rating WHERE id ='%s'" % student.id))
            self.datatable_list.append(
                [student, Rating(tmp_rating[0][0], tmp_rating[0][1], tmp_rating[0][2], tmp_rating[0][3])])

    def send_datatable_to_table(self):
        self.tableWidget.setRowCount(0)
        for data_student in self.datatable_list:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            tmp_item = [
                data_student[0].id,
                data_student[0].name,
                data_student[0].last_name,
                data_student[0].student_class,
                data_student[1].math,
                data_student[1].phys,
                data_student[1].comp_science,
                data_student[1].average_score
            ]
            for i in range(8):
                item = QtWidgets.QTableWidgetItem(str(tmp_item[i]))
                if i == 0 or i == 7:
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(row_position, i, item)
        self.tableWidget.resizeColumnsToContents()

    def sort_by_average(self, to):
        print("ok")
        if to == 1:
            for i in range(len(self.datatable_list)):
                for j in range(len(self.datatable_list)-1):
                    if self.datatable_list[j][1].average_score < self.datatable_list[j+1][1].average_score:
                        tmp = self.datatable_list[j]
                        self.datatable_list[j] = self.datatable_list[j+1]
                        self.datatable_list[j+1] = tmp
        else:
            for i in range(len(self.datatable_list)):
                for j in range(len(self.datatable_list)-1):
                    if self.datatable_list[j][1].average_score > self.datatable_list[j+1][1].average_score:
                        tmp = self.datatable_list[j]
                        self.datatable_list[j] = self.datatable_list[j+1]
                        self.datatable_list[j+1] = tmp
        self.verticalLayoutWidget.hide()
        self.send_datatable_to_table()

    def show_sort_score_pannel(self):
        if self.verticalLayoutWidget.isVisible():
            self.verticalLayoutWidget.hide()
        else:
            self.verticalLayoutWidget.show()

    def show_class_panel(self):
        if self.input_class_line.isVisible():
            if self.input_class_line.text() in self.class_list:
                self.send_to_table_by_class(self.input_class_line.text())
            if self.input_class_line.text() == "Все":
                self.get_datatable_list()
                self.send_datatable_to_table()
            self.input_class_line.hide()
            self.input_class_line.clear()
            self.sort_by_class.setText("Вывести класс")

        else:
            self.input_class_line.show()
            self.sort_by_class.setText("Найти")

    def get_class_list(self):
        self.get_list_of_student()
        for student in self.list_of_student:
            self.class_list.add(student.student_class)

    def send_to_table_by_class(self, what):
        self.get_datatable_list()
        self.get_class_list()
        ptr_list = []
        for data in self.datatable_list:
            if data[0].student_class == what:
                ptr_list.append(data)
        self.datatable_list = ptr_list
        self.send_datatable_to_table()

    def show_add_student_dialog(self):
        self.add_student_window.show()

    def add_new_student_to_database_and_table(self, student, rating):
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?);",
                       [student.id, student.name, student.last_name, student.student_class])
        connect.commit()
        cursor.execute("INSERT INTO rating VALUES (?, ?, ?, ?, ?);",
                       (rating.id, rating.math, rating.phys, rating.comp_science, rating.average_score))
        connect.commit()
        self.get_datatable_list()
        self.send_datatable_to_table()

    def change_student(self, change_item):
        print("ok2")
        if len(change_item) != 0:
            cursor.execute("""UPDATE students SET student_name = ? , last_name = ? , student_class = ? WHERE student_id = ?;""", (
                        self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 1).text(),
                        self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 2).text(),
                        self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 3).text(),
                        int(self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 0).text())
                        )
                       )
            connect.commit()
            cursor.execute("""UPDATE rating SET math = ? , phys = ? , computer_science = ?, average_score = ? WHERE id = ?;""",
                           (
                               int(self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 4).text()),
                               int(self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 5).text()),
                               int(self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 6).text()),
                               float((int(self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 4).text())+int(self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 5).text())+int(self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 6).text()))/3),
                               int(self.tableWidget.item(self.tableWidget.indexFromItem(change_item[0]).row(), 0).text())
                           )
                           )
            connect.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_student.setText(_translate("MainWindow", "добавить ученика"))
        self.sort_by_rating.setText(_translate("MainWindow", "сортировать по успеваемости"))
        self.sort_by_class.setText(_translate("MainWindow", "вывести класс"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "класс"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "математика"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "физика"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "информатика"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "средний балл"))
        self.tolowest.setText(_translate("MainWindow", "по убыванию"))
        self.tohighest.setText(_translate("MainWindow", "по возрастанию"))


class SecondForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(450, 200, 400, 400)
        self.setWindowTitle('Оповещение')
        self.lineEdit_name = QtWidgets.QLineEdit(self)
        self.lineEdit_name.setGeometry(QtCore.QRect(10, 20, 113, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_last_name = QtWidgets.QLineEdit(self)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(10, 60, 113, 21))
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.lineEdit_class = QtWidgets.QLineEdit(self)
        self.lineEdit_class.setGeometry(QtCore.QRect(10, 100, 113, 21))
        self.lineEdit_class.setObjectName("lineEdit_class")
        self.lineEdit_math = QtWidgets.QLineEdit(self)
        self.lineEdit_math.setGeometry(QtCore.QRect(10, 140, 113, 21))
        self.lineEdit_math.setObjectName("lineEdit_math")
        self.lineEdit_phys = QtWidgets.QLineEdit(self)
        self.lineEdit_phys.setGeometry(QtCore.QRect(10, 190, 113, 21))
        self.lineEdit_phys.setObjectName("lineEdit_phys")
        self.lineEdit_comp_science = QtWidgets.QLineEdit(self)
        self.lineEdit_comp_science.setGeometry(QtCore.QRect(10, 230, 113, 21))
        self.lineEdit_comp_science.setObjectName("lineEdit_comp_science")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 20, 91, 16))
        self.label.setObjectName("label")
        self.label.setText("Введите имя")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Введите фамилию")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 111, 16))
        self.label_3.setText("Введите класс")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(130, 140, 211, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Введите оценку по математике")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(130, 190, 191, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Введите оценку по физике")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(130, 230, 221, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Введите оценку по информатике")

        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setGeometry(150, 350, 100, 40)
        self.add_button.setText("Добавить")
        self.add_button.clicked.connect(lambda: self.add_new_student())

    def add_new_student(self):
        if self.lineEdit_name.text() == "" or self.lineEdit_last_name.text() == "" or self.lineEdit_class.text() == "":
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Заполните все обязательные поля")
            error.setIcon(QtWidgets.QMessageBox.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error.exec_()
            self.lineEdit_name.setStyleSheet("border: 1px solid red;")
            self.lineEdit_last_name.setStyleSheet("border: 1px solid red;")
            self.lineEdit_class.setStyleSheet("border: 1px solid red;")
        else:
            ui.last_id += 1
            new_student = Student(int(ui.last_id), self.lineEdit_name.text(), self.lineEdit_last_name.text(), self.lineEdit_class.text())
            if self.lineEdit_math.text() == "":
                self.lineEdit_math.setText("0")
            if self.lineEdit_phys.text() == "":
                self.lineEdit_phys.setText("0")
            if self.lineEdit_comp_science.text() == "":
                self.lineEdit_comp_science.setText("0")
            new_rating = Rating(int(ui.last_id), int(self.lineEdit_math.text()), int(self.lineEdit_phys.text()), int(self.lineEdit_comp_science.text()))
            ui.add_new_student_to_database_and_table(new_student, new_rating)
            self.lineEdit_name.clear()
            self.lineEdit_last_name.clear()
            self.lineEdit_class.clear()
            self.lineEdit_math.clear()
            self.lineEdit_phys.clear()
            self.lineEdit_comp_science.clear()
            self.close()


class MyMainWindow(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow).__init__()
        self.setupUi(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
