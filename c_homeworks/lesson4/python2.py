w = ('=' * 50)
my_dict = {
    'tuple': (1, 7, "text", 5.67, False, None),
    'list': [None, 42, True, 3.14, "shit"],
    'dict': {"One": "First", "Two": "Second", "Three": "Third", "Four": "Fourth", "Five": "Fifth"},
    'set': {2, False, 2.556, None, "Dick"},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
}

print(my_dict)

print(w)
#Вывести все элементы со второго по предпоследний
print('First tsk: ')
my_dict['tuple'][1:-1]
print(my_dict['tuple'])

print(w)
#Добавить элемент в конец и удалить второй элемент
print('Second task: ')
my_dict['list'].append(69.96)
my_dict['list'].pop(1)
print(my_dict['list'])

print(w)
#Добавить элемент в словарь и удалить второй элемент
print('Third task: ')
my_dict['dict'][('I am a tuple',)] = 'I am a tuple'
my_dict['dict'].pop('Two')
print(my_dict['dict'])

print(w)
#Добавить элемент в множество и удалить элемент из множества
print('Fourth task: ')
my_dict['set'].add('additional text')
my_dict['set'].remove(2)
print(my_dict['set'])

print(w)
print('Fifth task: ')
#Вывести первые 8 символов
print(my_dict['str'][0:7])
#Вывести 4 символа из центра строки
middle = len(my_dict['str']) // 2
start = middle - 2 
end = middle + 2
#Вывести символы с индексом кратные трем
print(my_dict['str'][::3])

print(my_dict)