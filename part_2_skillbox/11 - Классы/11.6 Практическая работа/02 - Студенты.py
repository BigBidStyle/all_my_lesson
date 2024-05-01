"""Задача 2. Студенты
Что нужно сделать.
Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя) и
отсортируйте список по возрастанию среднего балла. Выведите результат на экран."""
import random
class Student:
    def __init__(self, first_name, last_name, group_number, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.group_number = group_number
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

students = []
for num_students in range(10):
    first_name = input('Введите имя студента: ')
    last_name = input('Введите фамилию студента: ')
    group_number = random.randint(1, 5)
    grades = []
    for i in range(5):
        grades.append(random.randint(1, 5))
    student = Student(first_name, last_name, group_number, grades)
    students.append(student)

students.sort(key=lambda x: x.average_grade())

for student in students:
    print(f'Студент: {student.first_name} {student.last_name}, Группа: {student.group_number}, '
          f'Средний балл: {student.average_grade()}')




