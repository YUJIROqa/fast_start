#2 task

def fuzz_buzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print('Fuzz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fuzz_buzz()

#3 task


def calc():
    num_1 = int(input('Введите первое число: '))
    operation = input('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\nВведите операцию: ')
    num_2 = int(input('Введите второе число: '))
    if operation == '1' or operation =='Сложение':
        print(num_1 + num_2)
    elif operation == '2' or operation == 'Вычитание':
        print(num_1 - num_2)
    elif operation == '3' or operation == 'Умножение':
        print(num_1 * num_2)
    elif operation == '4' or operation == 'Деление':
        if num_2 != 0:
            print(num_1 / num_2)
        else:
            print('На ноль делить нельзя')
    else:
        print('Неверная операция')

calc()
    