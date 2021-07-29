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

