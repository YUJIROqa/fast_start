def calc():
    print(1 + 1)

calc() #выполни то что внутри этой функции(приготовление)
calc
print(calc) #распечатай мне саму функцию(рецепт)

new_calc = calc #мы можем в переменную засунуть функцию
print(new_calc) #распечатай мне саму функцию(рецепт)
new_calc() #выполни то что внутри этой функции(приготовление)

print('=' * 50)

def greet(): #это главная функция. в нее возвращается то, что возвращает функция hello(hello)

    def hello():
        return 'hello'  
    return hello() #возвращается результат функции hello
    
print(greet())

print('=' * 50)

def outer():

    def inner():
        return 'inner'
    return inner #возвращаем саму функцию иннер(приготовление)

print(outer()) #получил результат функции outer - это функция inner(приготовление)
print(outer()()) #получил результат функции inner(приготовление)
innert_function = outer() #поместили результат функции outer в переменную
print(innert_function()) #выполни то что внутри этой функции(приготовление)

print('=' * 50)

def func1(funk):
    print('before')
    funk()
    print('after')


def simple1():
    print('simple1')

def simple2():
    print('simple2')
    
simple1()
simple2()

func1(simple1) #вызывается функция funk1 и внутрь передается simple1
#то есть def func1(simple1) print('before') simple1() тут будет симпл 1 print('after')
func1(simple2)
 
def simple3():
    print('I')
    print('Love')
    print('Python')

func1(simple3)

print('=' * 50)

def add_text(funk):

    def wrapper():
        print('before')
        funk()
        print('after')
    return wrapper #возвращаем саму функцию wrapper


def simpl1():
    print('simple1')
simpl2 = add_text(simpl1) 
print(simpl2)
simpl2()#в эд текст идет функция симпл1, далее идет функция враппер и пишет бефор
#далее идет выполнение функции симпл1, далее афтер, и в эдд текст возвращается
#сама функция враппер(с выполнением функции симпл1). и далее мы эту функцию
#симпл2 вызываем как функцию. и то есть получаем результат функции враппер
###то есть мы инициировали выполнение функции add_text(с переданной внутрь симпл1)
###и получили результат функции враппер(с выполнением функции симпл1)
def simpl2():
    print('simple2') 
simpl2 = add_text(simpl2)
simpl2()

print('=' * 50)

def add_text(funk):
    def wrapper():
        print('before')
        funk()
        print('after')
    return wrapper

@add_text #декоратор. То есть мы принимаем в функцию add_text функцию simpl1
def simpl1():
    print('simple1')

@add_text
def simpl2():
    print('simple2')

simpl1()
simpl2()

print('=' * 50)

def add_logs(funk):

    def wrapper():
        print(f'Function {funk.__name__} started') #__name__ - это имя функции
        funk()
        print(f'Function {funk.__name__} finished')
    return wrapper

@add_logs #декоратор. То есть мы принимаем в функцию add_logs функцию simpl1
def simpl1():
    print('simple1')

@add_logs
def simpl2():
    print('simple2')

@add_logs
def print_nothing():
    print('nothing')

simpl1()
simpl2()
print_nothing()

print('=' * 50)

def add_logs(funk):

    def wrapper(*args): #*smth -  значит что мы можем передавать сколько угодно аргументов
        print(f'Function {funk.__name__} started') #__name__ - это имя функции
        funk(*args)
        print(f'Function {funk.__name__} finished')
    return wrapper

@add_logs
def calc(x):
    print(x * 2)

@add_logs
def calc2(x, y):
    print(x * y)

calc(3)
calc2(3, 4)

calc(3)
calc2(3, 7)

#LIST COMPREHENSION
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [x * 2 for x in my_list]#х умножаем на 2 для х(каждого элемента)
#списка my_list
print(new_list)

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list2 = [x for x in my_list2 if x % 2 == 0] #добавляй каждый х из списка my_list2
#если х делится на 2 без остатка
print(new_list2)

print('=' * 50)

new_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_dict = {x: x * 3 for x in new_list3}
print(new_dict)

data = [('one', 'two'), ('three', 'four'), ('five', 'six')]

new_dict2 = {key: value for key, value in data} 
new_dict3 = dict(data)#только для кортежей
print(new_dict2)

print('=' * 50)
import time 
#1
def count_time(funk):

    def wrapper():
        start = time.time()
        funk()
        end = time.time()
        print(f'Time: {end - start}')
    return wrapper

@count_time
def fanka():
    lisst = [x / 3 for x in range(1000000)]
    print(lisst)

fanka()

#2
def log_calls(funk):

    def wrapper():
        print(f'Function {funk.__name__} started')
        funk()
        print(f'Function {funk.__name__} finished')
    return wrapper

@log_calls
def hello():
    print('hello')

hello()

#4
def validaator(funk):

    def wrapper(*args): #*args - значит что мы можем передавать сколько угодно аргументов
        lissst = []
        for i in args: #перебираем все аргументы
            if i < 0:
                print('Number less than 0')
                continue
            else:
                lissst.append(i)
        print(lissst)
    return wrapper

@validaator
def hello(*args):
    print(args)

hello(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10)







