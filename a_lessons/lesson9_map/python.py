a = 1 #если строка не пустая, то она true
if a: #если а тру, то выполняется условие 
    print('true')

b = ''
if b:
    print('true')

#Встроенные функции
numbers = [2, 1, 5, 4, 3]
print(max(numbers)) #максимальное число
a = 1 / 3
print(round(a, 2)) #округление числа до 2 знаков после запятой

print(abs(-5)) #возвращает абсолютное значение числа.

print(sorted(numbers)) #сортировка списка по возрастанию
print(sorted(numbers, reverse = True)) #возвращает обратный порядок элементов в списке
    
##MAP - принимает функцию и итерируемый объект и применяет функцию к каждому элементу
my_list = [1, 2, 3, 4, 5]
def mult_by_2(x):
    return x * 2
new_list = map(mult_by_2, my_list) #для каждого элемента списка выполнить функцию
print(list(new_list))

#LAMBDA - анонимная функция
#map - для каждого элемента списка lambda - выполнить функцию(х * 2), далее сам список
new_list2 = map(lambda x: x * 2, my_list)

#Тернарный оператор
def mult_by_2(x):
    if x > 10:
        return x * 5
    else:
        return x * 2
#для каждого элемента списка выполнить х * 2 если элемент больше 10, иначе х * 5
new_list3 = map(lambda x: x * 5 if x > 10 else x * 2, my_list)
print(list(new_list3))

#FILTER - принимает функцию и итерируемый объект и возвращает новый список с элементами, для которых функция вернула True
my_listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lisst1 = []
for x in my_listt:
    if x % 2 == 0:
        new_lisst1.append(x)
print(new_lisst1)

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
#для каждого элемента списка выполнить функцию is_even, если тру то добавить элемент 
#в новый список new_lisst2, иначе не добавлять
new_lisst2 = filter(is_even, my_listt) 
print(list(new_lisst2))

def is_even(x):
    return x % 2 == 0 #если остаток от деления на 2 равен 0, то число четное 
#и возвращает тру, если не четное, то возвращает фолс

new_lisst3 = filter(is_even, my_listt)
print(list(new_lisst3))


#DATETIME - работа с датами
import datetime

time_now = datetime.datetime.now()
print(time_now)
print(time_now.year)
print(time_now.month)
print(time_now.day)
print(time_now.hour)
print(time_now.minute)
print(time_now.second)

my_time = '2023/06/05 12 hours, 30 minutes, 10 seconds'
python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M minutes, %S seconds')
print(python_date)
print(python_date.year)
print(python_date.month)
print(python_date.day)
print(python_date.hour)
print(python_date.minute)
print(python_date.second)
human_date = python_date.strftime('Year: %Y, Month: %m, Day: %d, Hour: %H, Minute: %M, Second: %S')
print(human_date)








