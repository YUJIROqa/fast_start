#Условия
user_input = int(input('Enter your number: '))

if user_input == 1:
    print('You entered 1')
elif user_input == 2:
    print('You entered 2')
#if user_input not in [1, 2]:
else:
    print('You entered  not 1 or 2')

#LOOP - циклы

names = ['John', 'Jane', 'Jim', 'Jill', 'Jack', 'Egor']
for name in names: #для каждого элемента в списке names
    if name.startswith('J'):
        print(f'Mr. {name}')

persons = {'John': 20, 'Jane': 21, 'Jim': 22, 'Jill': 23, 'Jack': 24, 'Egor': 25}
print(persons.items()) #выводит кортежи (ключ, значение)
for name, age in persons.items():
    print(f'{name}: {age}')

text = 'Sed vitae justo malesuda commodo liberio eu, bibendum mauris'

words = text.split()
fin_words = []
for word in words:
    if 'o' in word:
        print(word)
    else:
        fin_words.append(word)
print(fin_words)






