# Импортируем ABC (Abstract Base Class) и декоратор abstractmethod для создания абстрактных классов и методов
from abc import ABC, abstractmethod

# Определяем базовый класс Car
class Car():
    # Статические атрибуты класса, общие для всех экземпляров
    wheels = 4  # Количество колес по умолчанию
    fuel_type = 'benzin'  # Тип топлива по умолчанию
    manufacturer = 'undefind'  # Производитель по умолчанию

    # Конструктор класса, вызывается при создании нового экземпляра
    def __init__(self, brand, color, year): #селф - ссылка на создаваемый объект, а остальное - характеристики объекта
        # Инициализация атрибутов экземпляра
        self.brand = brand  # Бренд автомобиля
        self.color = color  # Цвет автомобиля
        self.year = year    # Год выпуска

    # Метод для запуска двигателя
    def start_engine(self):
        print('Engine started')

    # Метод для остановки двигателя
    def stop_engine(self):
        print('Engine stopped')

    # Метод для подачи сигнала
    def honk(self):
        print('Honk!')

    # Абстрактный метод, который должен быть реализован в дочерних классах
    @abstractmethod
    def get_vehicle_type(self):
        pass
    
# Определяем класс SportsCar, наследующийся от Car
class SportsCar(Car):
    # Специфические атрибуты для спортивных машин
    max_speed = 300  # Максимальная скорость
    type = 'sport'   # Тип автомобиля

    # Уникальный метод для спортивных машин
    def turbo_boost(self):
        print('Turbo turned on!')

    # Переопределение метода start_engine родительского класса
    def start_engine(self):
        print('Sports car engine started!')

    # Реализация абстрактного метода get_vehicle_type
    def get_vehicle_type(self):
        print(f'Тип автомобиля: {self.type}, бренд: {self.brand}')

# Определяем класс Truck, наследующийся от Car
class Truck(Car):
    # Специфические атрибуты для грузовиков
    wheels = 6  # Переопределение количества колес
    cargo_capacity = 5000  # Грузоподъемность
    type = 'truck'  # Тип автомобиля

    # Уникальный метод для грузовиков
    def load_cargo(self):
        print('Cargo loaded!')

    # Переопределение метода start_engine с использованием родительского метода
    def start_engine(self):
        super().start_engine()  # Вызов метода родительского класса
        print(f'{self.brand} is too loud')

    # Реализация абстрактного метода get_vehicle_type
    def get_vehicle_type(self):
        print(f'Тип автомобиля: {self.type}, бренд: {self.brand}')

# Создание экземпляра обычного автомобиля
my_car = Car('Mercedes', 'black', 2020)
print('My car:')
print('wheels:', my_car.wheels)
print('brand:', my_car.brand)
print('color:', my_car.color)
print('year:', my_car.year)

# Создание второго экземпляра обычного автомобиля
friend_car = Car('BMW', 'red', 2021)
print('Friend car:')
print('wheels:', friend_car.wheels)
print('brand:', friend_car.brand)
print('color:', friend_car.color)
print('year:', friend_car.year)

# Создание третьего экземпляра обычного автомобиля
parent_car = Car('Toyota', 'white', 2019)
print('Parent car:')
print('wheels:', parent_car.wheels)
print('brand:', parent_car.brand)
print('color:', parent_car.color)
print('year:', parent_car.year)

# Создание четвертого экземпляра и демонстрация методов
new_car = Car('Bugatti', 'blue', 2022)
new_car.start_engine()  # Запуск двигателя
new_car.honk()         # Подача сигнала
new_car.stop_engine()  # Остановка двигателя

# Создание экземпляра спортивного автомобиля
ferrari = SportsCar('Ferrari', 'red', 2023)
ferrari.start_engine()  # Запуск спортивного двигателя
ferrari.turbo_boost()   # Включение турбо-режима
print(ferrari.wheels)   # Вывод количества колес

# Создание экземпляра грузовика
kamaz = Truck('Kamaz', 'blue', 2022)
kamaz.start_engine()  # Запуск двигателя грузовика
kamaz.load_cargo()    # Загрузка груза
print(kamaz.wheels)   # Вывод количества колес (6)

# Демонстрация работы с разными типами автомобилей
defolt_car = Car('Toyota', 'white', 2019)
defolt_car.start_engine()  # Запуск обычного двигателя

sport_car = SportsCar('F1', 'white', 2023)
sport_car.start_engine()      # Запуск спортивного двигателя
sport_car.get_vehicle_type()  # Вывод типа транспортного средства

track_car = Truck('Truck', 'white', 2023)
track_car.start_engine()      # Запуск двигателя грузовика
track_car.get_vehicle_type()  # Вывод типа транспортного средства

print(sport_car.wheels)