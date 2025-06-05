from random import randint, randrange, choice
import os
import sys
from assist import assist, veraible
print(randint(1, 100)) #random.randint(1, 100) - функция, которая генерирует случайное число от 1 до 100
print(randrange(1, 100, 2)) #random.randrange(1, 100, 2) - функция, которая генерирует случайное число от 1 до 100 с шагом 2

users = ['user1', 'user2', 'user3', 'user4', 'user5']
print(choice(users)) #r]andom.choice(users) - функция, которая генерирует случайный элемент из списка

print(sys.platform)

assist.assist()
print(assist.veraible)