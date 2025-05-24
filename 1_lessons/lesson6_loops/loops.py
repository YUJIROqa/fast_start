#Условия
user_input = int(input('Enter your number: '))

if user_input == 1:
    print('You entered 1')
elif user_input == 2:
    print('You entered 2')
#if user_input not in [1, 2]:
else:
    print('You entered  not 1 or 2')

#LOOP FOR - циклы

names = ['John', 'Jane', 'Jim', 'Jill', 'Jack', 'Egor']
for name in names: #для каждого элемента в списке names
    if name.startswith('J'):
        print(f'Mr. {name}')

persons = {'John': 20, 'Jane': 21, 'Jim': 22, 'Jill': 23, 'Jack': 24, 'Egor': 25}
print(persons.items()) #выводит кортежи (ключ, значение)
for name, age in persons.items():
    print(f'{name}: {age}')

text = 'Sed vitae justo malesuda commodo liberio eu, bibendum mauris'

words = text.split()#разделяет строку на список слов
fin_words = [] #создает пустой список
for word in words: #для каждого слова в списке words
    if 'o' in word: #если в слове есть 'o'
        print(word) #выводит слово
    else: #иначе
        fin_words.append(word) #добавляет слово в список fin_words
print(' '.join(fin_words)) #объединяет список fin_words в строку

#WHILE цикл
i = 0 
while i < 5: 
    print('hello')
    i += 1
print('End')

while True:
    user_input = input('Enter something: ')
    if user_input == 'exit':
        break #последняя точка работы цикла
    if user_input == 'skip':
        continue #пропуск проверки следующих шагов и переход снова к первому
        print('skipping....')
    elif len(user_input) > 10:
        print(f' Yout input is {user_input}')
    elif len(user_input) < 2:
        print(f'Yout text {user_input} is too short')
    else:
        print(user_input)

print('End')

#FUNCTIONS - это блоки кода, которые можно вызывать в программе
#они позволяют избежать дублирования кода DRY (Don't Repeat Yourself)

a = 1
b = 2
c = 3 
d = 4
e = 5

main_num = 45

def calc(numb): #numb - параметр функции. То есть при вызове функции внутри должно быть значение
    if numb < 4:
        print(numb + main_num) #выводит сумму параметра и main_num
    else:
        print(main_num - numb) #выводит разность main_num и параметра

print(calc(a)) #вызов функции с аргументом a
print(calc(b)) #вызов функции с аргументом b
print(calc(c)) #вызов функции с аргументом c
print(calc(d)) #вызов функции с аргументом d
print(calc(e)) #вызов функции с аргументом e


a = 1
b = 2
c = 3
d = 4
e = 5
y = 0

main_number = 47

def calc(number):
    if y == 0:
        return number #возвращает значение number
    else:
        result = number + main_number #возвращает сумму number и main_number
        return result

print(calc(a)) #вызов функции с аргументом a
print(calc(b)) #вызов функции с аргументом b
print(calc(c)) #вызов функции с аргументом c
print(calc(d)) #вызов функции с аргументом d
print(calc(e)) #вызов функции с аргументом e

def calc(num):
    return num #ретурн возвращает значение в функцию

print(calc(3)) #распечатай мне значение функции с переданой тройкой

def hello():
    a = 12
    #retuen None
#если в функции нет принта или ретурна, то это равноценно return None
print(hello()) #распечатай мне значение функции hello


def print_words(first, second, third, fourht, fifth):
    print(f'The first word is {first}, the second word is {second}, the third word is {third}, the fourth word is {fourht}, the fifth word is {fifth}')
    
print_words('one', 'two', 'three', 'four', 'five')#позиционное использование аргументов
print_words(fifth='five', third='three', first='one', second='two', fourth='four')#именованное использование аргументов


def power(number, degree = 2):
    return number ** degree

print(power(2)) #если не передать второй аргумент, то будет возведено в квадрат
print(power(2, 3)) #если передать второй аргумент, то будет возведено в степень


def example(e, f, g, ff='one', gg='two'):
    return e, f, g, ff, gg

print(example(2, 3, 6, 22)) #если не передать ff и gg, то будет использованы значения по умолчанию


def sum_all(*args):
    # print(args)
    # result = 0
    # for x in args:
    #     result += x
    # return result
    return sum(args)
print(sum_all(1, 4, 6))


def price_list(**kwargs): #**kwargs - аргументы, которые передаются в виде словаря
    print(kwargs) #распечатает словарь
    for title, price in kwargs.items(): #для каждого ключа и значения в словаре
        print(f'Product: {title}, price: {price}')

price_list(iphone=2500, laptop=1750, samsung=3000)

