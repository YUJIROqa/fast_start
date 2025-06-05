import random
#1 task
text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
text = text.replace(', ', ' ЗАПЯТАЯ ')
print(text)
list_from_text = text.split()
print(list_from_text)

new_list_with_ing = []
for word in list_from_text:
    new_words = word + 'ing'
    new_list_with_ing.append(new_words)
print(new_list_with_ing)


finish_text = ' '.join(new_list_with_ing)
result = finish_text.replace(' ЗАПЯТАЯing ', ', ')

print(result)

#2 task
while True:
    user_num = int(input('Enter your number: '))
    num = 255
    if user_num == num:
        print('Congratulations. You got the right number')
        break
    else:
        print('Try again')
        

#3 task
import random
list = []
for i in range(15):
    number = random.randint(1, 5500)
    list.append(number)
print(list)
print(f'Max number: {max(list)}')
print(f'Min number: {min(list)}')
print(f'Sum of numbers: {sum(list)}')
print(f'Average of numbers: {sum(list) / len(list)}')




