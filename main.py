import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QWidget, QTableWidgetItem, QTableWidget, QVBoxLayout, \
    QComboBox, QPushButton, QLineEdit, QHBoxLayout

con = sqlite3.connect("pyqt2/films.db")
title = ['Номер', 'Название', 'Год', 'Жанр', 'Продолжителность']

# Создание курсора
cur = con.cursor()

oper_year = """SELECT year FROM Films"""
buffer = cur.execute(oper_year).fetchall()
buffer = [int(i[0]) for i in buffer]
max_y = max(buffer)
min_y = min(buffer)

oper_dura = """SELECT duration FROM Films"""
buffer = cur.execute(oper_dura).fetchall()

buffer = [int(i[0]) for i in buffer if i[0] != '']
max_d = max(buffer)
min_d = min(buffer)

oper_genre = """SELECT id, title FROM genres"""
genre = {}
genre_2 = {}
genre[0] = '-'
buffer = cur.execute(oper_genre).fetchall()
for i, j in buffer:
    genre[i] = j
    genre_2[i] = j


# print(genre)
# Вывод результатов на экран
def get_key(d, value):
    if value == '-':
        return ''
    for k, v in d.items():
        if v == value:
            return k


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.loadUI()
        self.result = []
        self.genre_on = ''
        self.years = []
        self.during = []
        self.called = ''
        self.oper1 = ''

    def loadUI(self):
        self.setGeometry(100, 100, 900, 600)
        self.lay = QVBoxLayout()

        # жанр -------------------------------------------
        self.h1 = QLabel(self)
        self.h1.setText('Жанр')
        self.lay.addWidget(self.h1)

        self.combo = QComboBox(self)
        self.combo.addItems(genre.values())
        self.lay.addWidget(self.combo)

        # год -------------------------------------------
        self.h1 = QLabel(self)
        self.h1.setText('Год')
        self.lay.addWidget(self.h1)
        self.lay1_h = QHBoxLayout()
        self.year_f = QLineEdit(self)
        self.year_f.setText(str(min_y))
        self.year_to = QLineEdit(self)
        self.year_to.setText(str(max_y))
        self.h2 = QLabel(self)
        self.h2.setText('c')
        self.h2_1 = QLabel(self)
        self.h2_1.setText('по')
        self.lay1_h.addWidget(self.h2)
        self.lay1_h.addWidget(self.year_f)
        self.lay1_h.addWidget(self.h2_1)
        self.lay1_h.addWidget(self.year_to)
        self.lay.addLayout(self.lay1_h)

        # продолжительность -------------------------------------------
        self.h1 = QLabel(self)
        self.h1.setText('Продолжительность')
        self.lay.addWidget(self.h1)

        self.lay2_h = QHBoxLayout()
        self.dur_f = QLineEdit(self)
        self.dur_f.setText(str(min_d))
        self.dur_to = QLineEdit(self)
        self.dur_to.setText(str(max_d))
        self.h2 = QLabel(self)
        self.h2.setText('от')
        self.h2_1 = QLabel(self)
        self.h2_1.setText('до')
        self.lay2_h.addWidget(self.h2)
        self.lay2_h.addWidget(self.dur_f)
        self.lay2_h.addWidget(self.h2_1)
        self.lay2_h.addWidget(self.dur_to)
        self.lay.addLayout(self.lay2_h)

        # название -------------------------------------------
        self.h1 = QLabel(self)
        self.h1.setText('Название')
        self.lay.addWidget(self.h1)

        self.name = QLineEdit(self)
        self.lay.addWidget(self.name)

        # кнопка -----------------------------------
        self.lay3_h = QHBoxLayout()

        self.button_search = QPushButton(self)
        self.button_search.setText('Найти')
        self.button_search.clicked.connect(self.loadTable)

        self.button_save = QPushButton(self)
        self.button_save.setText('Сохранить')
        self.button_save.clicked.connect(self.saveTable)

        self.button_add = QPushButton(self)
        self.button_add.setText('Добавить')
        self.button_add.clicked.connect(self.open_third_form)

        self.lay3_h.addWidget(self.button_search)
        self.lay3_h.addWidget(self.button_save)
        self.lay3_h.addWidget(self.button_add)

        self.lay.addLayout(self.lay3_h)

        self.table = QTableWidget(self)
        self.lay.addWidget(self.table)

        self.setLayout(self.lay)

    def loadTable(self):
        self.generateList()
        self.table.setColumnCount(len(title))
        self.table.setHorizontalHeaderLabels(title)
        self.table.setRowCount(0)
        for i, row in enumerate(self.result):
            buf = [str(i) for i in row]
            buf[3] = genre[int(buf[3])]
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(buf):
                if elem == '':
                    elem = '-'
                self.table.setItem(i, j, QTableWidgetItem(elem))
        self.table.resizeColumnsToContents()

    def generateList(self):
        self.genre_on = self.combo.currentText()
        self.checkingValue()
        self.called = self.name.text()
        self.checkingOper()

        self.result = cur.execute(self.oper1).fetchall()
        self.clearingValue()

    def checkingOper(self):
        if self.called == '' and self.genre_on == '-':
            self.oper1 = f"""SELECT * FROM 'Films' WHERE (year BETWEEN {self.years[0]} AND {self.years[1]}) AND (duration BETWEEN {self.during[0]} AND {self.during[1]})"""
        elif self.called == '' and self.genre_on != '-':
            self.oper1 = f"""SELECT * FROM 'Films' WHERE (year BETWEEN {self.years[0]} AND {self.years[1]}) AND (duration BETWEEN {self.during[0]} AND {self.during[1]}) AND (genre=(SELECT id FROM genres WHERE title = '{self.genre_on}'))"""
        elif self.called != '' and self.genre_on == '-':
            self.oper1 = f"""SELECT * FROM 'Films' WHERE (year BETWEEN {self.years[0]} AND {self.years[1]}) AND (duration BETWEEN {self.during[0]} AND {self.during[1]}) AND (title LIKE '{self.called}%')"""
        else:
            self.oper1 = f"""SELECT * FROM 'Films' WHERE (year BETWEEN {self.years[0]} AND {self.years[1]}) AND (duration BETWEEN {self.during[0]} AND {self.during[1]}) AND (title LIKE '{self.called}%') AND (genre=(SELECT id FROM genres WHERE title = '{self.genre_on}'))"""

    def clearingValue(self):
        self.years = []
        self.during = []
        self.called = []

    def checkingValue(self):

        if int(self.year_f.text()) < min_y or self.year_f.text() == '':
            self.years.append(str(min_y))
        else:
            self.years.append(self.year_f.text())
        if int(self.year_to.text()) > max_y or self.year_to.text() == '':
            self.years.append(str(max_y))
        else:
            self.years.append(self.year_to.text())
        if int(self.dur_f.text()) < min_d or self.dur_f.text() == '':
            self.during.append(str(min_d))
        else:
            self.during.append(self.dur_f.text())
        if int(self.dur_to.text()) > max_d or self.dur_to.text() == '':
            self.during.append(str(max_d))
        else:
            self.during.append(self.dur_to.text())

    def saveTable(self):
        data = []
        column = self.table.columnCount()
        for i in range(self.table.rowCount()):
            buf = []
            for j in range(column):
                buf.append(self.table.item(i, j).text())
            data.append(buf)
        oper_save = ''
        for row in data:
            oper_save = f"""UPDATE Films SET title = '{row[1]}', year = '{row[2]}', genre = '{get_key(genre, row[3])}', duration = '{row[4]}' WHERE id = {row[0]}"""
            cur.execute(oper_save)
            con.commit()
        self.open_second_form()

    def open_second_form(self):
        self.second_form = SecondForm()
        self.second_form.show()

    def open_third_form(self):
        self.third_form = ThirdForm()
        self.third_form.show()


class SecondForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Оповещение')
        self.lbl = QLabel(self)
        self.lbl.setText('Изменения сохранены')
        self.lbl.adjustSize()


class ThirdForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Оповещение')
        self.lay = QVBoxLayout()

        self.title = QLabel(self)
        self.title.setText('Название фильма')
        self.lay.addWidget(self.title)

        self.name = QLineEdit(self)
        self.lay.addWidget(self.name)

        self.title = QLabel(self)
        self.title.setText('Год')
        self.lay.addWidget(self.title)

        self.year = QLineEdit(self)
        self.lay.addWidget(self.year)

        self.title = QLabel(self)
        self.title.setText('Жанр')
        self.lay.addWidget(self.title)

        self.combo = QComboBox(self)
        self.combo.addItems(genre_2.values())
        self.lay.addWidget(self.combo)

        self.title = QLabel(self)
        self.title.setText('Продолжительность')
        self.lay.addWidget(self.title)

        self.dur = QLineEdit(self)
        self.lay.addWidget(self.dur)

        self.button = QPushButton(self)
        self.button.setText('Добавить')
        self.button.clicked.connect(self.adding)
        self.lay.addWidget(self.button)

        self.setLayout(self.lay)

    def adding(self):
        oper_id = """SELECT * FROM Films WHERE id = (SELECT MAX(id) FROM Films)"""
        ides = cur.execute(oper_id).fetchall()
        print(ides)
        ides = str(int(ides[0][0]) + 1)

        open_add = f"""INSERT INTO Films(id,title,year,genre,duration) VALUES({ides},'{self.name.text()}','{self.year.text()}','{get_key(genre, self.combo.currentText())}','{self.dur.text()}')"""
        print(open_add)
        cur.execute(open_add)
        con.commit()
        con.commit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
