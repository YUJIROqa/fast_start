import os

with open('lessons_tasks_homeworks/1_lessons/lesson13_reading/data.txt', 'r') as file: #открываем файл для чтения
    data = file.read() #читаем файл
    print(data) #выводим данные

with open('lessons_tasks_homeworks/1_lessons/lesson13_reading/data.txt', 'r') as file: #открываем файл для чтения
    for line in file.readlines():
        print(line)

print(os.path.dirname(__file__)) #выводим путь к файлу
base_path = os.path.dirname(__file__) #определяем путь к файлу
file_path = f'{base_path}/data.txt' #определяем путь к файлу до файла
print(file_path) #выводим путь к файлу


with open(file_path, 'r') as file: #открываем файл для чтения
    for line in file.readlines():
        print(line)


def calc(a, b):
    try:                          #трай нужно для того чтобы мы могли обрабатывать ошибки и программа продолжала работать
        return a / b              #то что мы выполняем в блоке трай
    except Exception as e:     #исключение/ошибка которая может произойти
        print(e) #какое сообщение об ошибке будет входить
        #raise e #вызываем ошибку

print(calc(input('Введите число 1: '), input('Введите число 2: ')))
print('Hello')

import datetime

now = datetime.datetime.now()
print(now)











