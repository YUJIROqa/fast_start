w = '=' * 50

#Распаковка списка
my_list = [1, 3]
my_tuple = (2, 6, 9)
# a = my_list[1]
# c = my_tuple[2]

a, b = my_list #распаковка списка a - 1, b - 3
c, d, e = my_tuple #распаковка кортежа c - 2, d - 6, e - 9

print(a, b, c, d, e)

print(w)

#Срез
lll = [1, 3, 5, 2, 5, 7, 1, 3]
print(lll[0:3]) #срез списка с 0 по 4 элемент. От включительно до не включительно \
print(lll[:2]) #срез списка с 0 по 2 элемент. Если с 0 то можно не писать
print(lll[2:]) #срез списка с 2 элемента по конец списка. Если до конца то можно не писать
print(lll[1::2]) #срез списка с 1 элемента по конец списка с шагом 2
print(lll[:])#копия списка
print(lll[::-1])#переворот списка
print(lll[::-2])#переворот списка с шагом 2

print(w)

text = 'my long long string'
print(text[3]) #получение символа по индексу
print(len(text)) #длина строки
print(text.index('l')) #поиск индекса первого вхождения символа
print('long' in text) #проверка на вхождение подстроки в строку
print(text.count('l')) #подсчет вхождений символа в строку
print(text.find('long')) #поиск индекса первого вхождения подстроки
print(text[:7]) #срез строки
print(text.startswith('my')) #проверка на начало строки
print(text.endswith('ing')) #проверка на окончание строки

print(w)

txt = 'This is my FuCkInG string'
print(txt.capitalize()) #первый символ заглавный
print(txt.title()) #каждое слово с заглавной буквы
print(txt.upper()) #все символы заглавные
print(txt.lower()) #все символы маленькие
print(txt.swapcase()) #меняет регистр символов

print(w)

msg = 'Hello World'
msg = msg.replace('World', 'There') #перезаписать строку
print(msg)

data = '12,3'
data_new = data.replace(',', '.') #замена символов
print(data_new)

msg = 'Hello World'
msg = msg.replace('World', 'There') #перезаписать строку
print(msg)

data = '12,3'
data_new = data.replace(',', '.') #замена символов
print(data_new)

txxt = ' admin '
#txxt = txt.replace(' ', '') #удаление пробелов
txxt_new = txxt.strip() #удаление пробелов

print(w)

#Перевод строки в список

my_string = 'some title text'
my_string2 = 'some,title,text'
list_from_text = my_string.split() #разделение строки по пробелу
list_from_text2 = my_string2.split(',') #разделение строки по запятой
print(list_from_text) 
print(list_from_text2)

print(w)

#Перевод списка в строку

my_list = ['some', 'title', 'text']
text_from_list = ', '.join(my_list) #перевод списка в строку. Сделай пробелы и запятые между 
#элементами списка и переведи в строку
print(text_from_list)
print('Here is my hunny text: ', ', '.join(my_list)) #перевод списка в строку. Сделай пробелы 
#и запятые между 

print(w)

a = 'one'
b = 'two'
print(f'First word is {a}, second word is {b}') #f-строка. Вывод переменных в строку
