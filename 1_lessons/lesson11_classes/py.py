from abc import ABC, abstractmethod #abc - это модуль для абстрактных классов
#класс - это описание того какими характеристиками и действиями обладает объект который создается по этому опиисанию
#класс - это чертеж дома, а объект - это дом построенный по этому чертежу
#отличие метода от функции в том, что метод принадлежит классу, а функция нет + метод принимает в себя self
class Group:
    pypils = True
    school_name = 42
    director = 'Marivanna'

    def __init__(self, title, pupls_count, group_leader): #
        self.title = title
        self.pupls_count = pupls_count
        self.group_leader = group_leader


    def study(self): #метод класса, self - это ссылка на сам объект
        print('Sit and read')

    @abstractmethod
    def move(self): #абстрактный метод, который должен быть переопределен в дочерних классах
        pass       #подмечаем, что у дочерних классов есть метод move и его необходимо обозначить

class PrimaryGroup(Group):
    max_age = 11
    min_age = 6  
    building_section = 'left'

    def __init__(self, title, pupls_count, group_leader, classroom):
        super().__init__(title, pupls_count, group_leader)
        self.classroom = classroom
    #метод инит нужен что бы создать экземпляр класса с индивидуальными характеристиками
    #с помощью класса у каждого экземпляра класса есть какие-то дефолтные свойства этого класса
    #а с помощью метода инит мы можем создавать экземпляры с дополнительными индивидуальными характеристиками
    def moove(self):
        print('Run fast')


class HighGroup(Group):
    max_age = 18
    min_age = 14 

    def move(self):
        print('Go slow')

class MiddleGroup(Group):
    max_age = 15
    min_age = 10

#объект класса = экземпляр класса = представитель класса = объект типа
#Инкапсуляция - каждый объект умеет хранить в себе свойства и методы. Из каждого объекта можно получить свойства и методы
#Наследование - дочерние классы наследуют свойства и методы родительского класса
#Полиморфизм - способность объектов разных классов использовать один и тот же метод
first_a = PrimaryGroup('1a', 18, 'MF', 5)
first_b = PrimaryGroup('1b', 20, 'TD', 8)
eleven_a = HighGroup('11a', 22, 'AR')
six_a = MiddleGroup('6a', 25, 'RI')
 
print(first_a.pupls_count)
print(first_a.classroom)
print(first_b.title)

print(first_a.max_age) #мы смотрим на max_age из класса PrimaryGroup
print(first_a.school_name) #мы смотрим на school_name из класса Group
print(first_a.director) #мы смотрим на director из класса Group
first_a.study() #мы смотрим на study из класса Group
first_a.move() #мы смотрим на move из класса Group

print(first_a.pypils) #мы смотрим на pypils из класса Group
print(eleven_a.school_name) #мы смотрим на school_name из класса Group
print(eleven_a.director) #мы смотрим на director из класса Group
eleven_a.study() #мы смотрим на study из класса Group
eleven_a.move() #мы смотрим на move из класса Group
