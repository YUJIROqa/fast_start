#OOP
#Инкапсуляция - это способность объектов скрывать свои внутренние данные и методы от внешнего воздействия
#Все данные объекта должны храниться в объекте и никто не может изменить данные объекта без его ведома

#Наследование - это способность объектов наследовать свойства и методы друг друга
#Полиморфизм - это способность объектов использовать один и тот же метод, но с разными параметрами


class Group:  # класс родитель
    students = True #
    shcool_number = 42
    director = 'Marivanna'

    def __init__(self, title, student_count, group_lider):
        self.title = title
        self.student_count = student_count
        self.group_lider = group_lider

    def study(self):  # метод класса. Отличается от функции тем, что идет в классе
        print('study')


class PrimaryGroup(Group): # класс наследник(наследует все свойства и методы класса Group)
    max_age = 11
    min_age = 6
    location = 'left'

    def __init__(self, title, student_count, group_lider, classroom): # конструктор класса, нужен для того чтобы передавать параметры в класс
        super().__init__(title, student_count, group_lider) # вызываем конструктор класса родителя
        self.classroom = classroom # добавляем новое свойство

    def move(self):
        print('run fust')


class HightGroup(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('go slowly')

class MediumGroup(Group):
    max_age = 14
    min_age = 10

first_a = PrimaryGroup('1a', 20, 'MF', 5)

first_a.class_room = 1111

print(first_a.class_room)

import json
def read_file(file_path):
    file_data = open(file_path, 'r') #открываем файл для чтения
    data = file_data.read()
    data = json.loads(data)
    file_data.close()
    return data

data1 = read_file('lessons_tasks_homeworks/1_lessons/lesson12_classesOOP/data1.txt')
data2 = read_file('lessons_tasks_homeworks/1_lessons/lesson12_classesOOP/data2.txt')

print(data1['Country'])
print(data1['avg_temp'])
print(data2['Country'])
print(data2['avg_temp'])

class CountryData:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_file()
        self.country = self.data['Country']
        self.avg_temp = self.data['avg_temp']
        self.comfort = self.is_comfort()

    def read_file(self):
        file_data = open(self.file_path, 'r') #открываем файл для чтения
        data = json.load(file_data)
        file_data.close()
        return data
    
    def is_comfort(self):
        return self.avg_temp > 25

data1 = CountryData('lessons_tasks_homeworks/1_lessons/lesson12_classesOOP/data1.txt')
print(data1.data)
print(data1.country)
print(data1.avg_temp)
print(data1.comfort)
