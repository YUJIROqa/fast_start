from datetime import datetime

try:
    user_input = int(input('Введите дату: '))
    date_obj = datetime.strptime(user_input, '%d.%m.%Y')
    print(date_obj)
except Exception as e:
    print(e, 'Вы ввели неверный формат даты, попробуйте снова')