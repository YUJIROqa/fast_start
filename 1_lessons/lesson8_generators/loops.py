def generate_text(text1, text2): #text1, text2 - параметры функции
    return f'Text consists on the words:{text1} and {text2}' #возвращает строку
#return - конечная строка, которая возвращается в результате выполнения функции. Под после не работает
print(generate_text('Hello', 'World')) #вызывает функцию generate_text с аргументами 'Hello' и 'World'

my_list = [1, 2, 3, 4, 5]

for x in my_list:
    print(x)

# n = 2
# progression = []
# num = 1
# while len(progression) < 10000:
#     progression.append(num)
#     num += n

# print(progression)

def progression(limit=100): #limit - параметр функции
    n = 2 #n - шаг прогрессии
    num = 1 #num - начальное значение прогрессии
    count = 1 #count - счетчик
    while count <  limit: #while - цикл
        yield num
        num += n #num = num + n
        count += 1 #count = count + 1
# for number in progression(10): #for - цикл, который проходит по всем значениям в генераторе
#     print(number) #print - выводит значение number
    
# print(list(progression(10)))

count = 1
for number in progression(1000000):
    if count == 1000000:
        print(number)
        break
    count += 1

print('w'*50)
