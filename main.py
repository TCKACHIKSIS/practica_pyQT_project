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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 644)
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
        self.find_student = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.find_student.setObjectName("find_student")
        self.horizontalLayout.addWidget(self.find_student)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 701, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 701, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_student.setText(_translate("MainWindow", "добавить ученика"))
        self.sort_by_rating.setText(_translate("MainWindow", "сортировать по успеваемости"))
        self.sort_by_class.setText(_translate("MainWindow", "вывести класс"))
        self.find_student.setText(_translate("MainWindow", "найти ученика"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "математика"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "физика"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "информатика"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Средний балл"))


class MyMainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
        self.list_of_student = []
        self.list_of_rating = []
        self.datatable_list = []
        self.get_datatable_list()
        self.send_datatable_to_table()
        self.add_student.setText("ok")

    def get_list_of_student(self):
        tmp_list_of_student = list(cursor.execute("SELECT * FROM students"))
        for student in tmp_list_of_student:
            self.list_of_student.append(Student(student[0], student[1], student[2], student[3]))

    def get_datatable_list(self):
        self.get_list_of_student()
        for student in self.list_of_student:
            tmp_rating = list(cursor.execute("SELECT * FROM rating WHERE id ='%s'" % student.id))
            self.datatable_list.append([student, Rating(tmp_rating[0][0], tmp_rating[0][1], tmp_rating[0][2], tmp_rating[0][3])])

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
                print(tmp_item[i])
                item = QtWidgets.QTableWidgetItem(str(tmp_item[i])[0])
                self.tableWidget.setItem(row_position, i, item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())