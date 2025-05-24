#Добавление ing к каждому слову в строке
text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
#Меняем реальные запятые на слова ЗАПЯТАЯ
text = text.replace(', ', ' ЗАПЯТАЯ ')
print(text)
#Разделяем строку на список
list_from_text = text.split()
print(list_from_text)
#Добавляем ing к каждому слову в списке
new_list_with_ing = []
for word in list_from_text:
    new_words = word + 'ing'
    new_list_with_ing.append(new_words)
print(new_list_with_ing)

#обратное преобразование списка в строку
finish_text = ' '.join(new_list_with_ing)
#меняем слова ЗАПЯТАЯ на реальные запятые
result = finish_text.replace(' ЗАПЯТАЯing ', ', ')
#выводим результат
print(result)



