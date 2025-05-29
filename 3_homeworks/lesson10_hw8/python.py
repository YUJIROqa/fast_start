

def decorator(funk):

    def wrapper(first, second):
        if first < 0 or second < 0:
            return funk(first, second, '*')
        elif first == second:
            return funk(first, second, '+')
        elif first > second:
            return funk(first, second, '-')
        elif second > first:
            return funk(first, second, '/')
        else:
            return 'Error: Invalid operation'
    return wrapper

@decorator
def calc(firs, second, operation):
    if operation == '/':
        if second == 0:
            return 'Error: Division by zero'
        return firs / second
    if operation == '+':
        return firs + second
    elif operation == '-':
        return firs - second
    elif operation == '*':
        return firs * second
    else:
        return 'Error: Invalid operation'
    

print(calc(int(input('Enter first number: ')), int(input('Enter second number: ') )))
#мы вызываем функцию calc с какими-то значениями. Далее сама функция calc со значениями идет в декоратор.
#декоратор принимает функцию и далее значения функции calc и идет в wrapper.
#wrapper принимает значения и в зависимости от них возвращает функцию calc с определенными значениями
#и далее уже работает сама функция calc с этими переданными значениями из wrapper