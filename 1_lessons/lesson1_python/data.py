python --version #windows узнать версию python
python3 --version #linux узнать версию python
pip --version #узнать версию pip - пакетный менеджер для установки и управления Python-пакетами.
pip list #список установленных пакетов(библиотек)
pip freeze > requirements.txt #переместить в файл список установленных пакетов(библиотек)
pip install -r requirements.txt #установить все библиотеки из файла requirements.txt

#Linux
python3 -m venv venv #создать виртуальное окружение
source venv/bin/activate #активировать виртуальное окружение

#Windows
python -m venv venv #создать виртуальное окружение
venv\Scripts\activate #активировать виртуальное окружение

-m #означает что нужно найти модуль и запустить его как программу. 
#Ффйл - просто документ, а модуль - это файл с кодом, который можно импортировать в другие программы.

-r #означает что нужно использовать файл requirements.txt для установки библиотек. 
#Без -r команда попытается установить модуль requirements.txt как библиотеку.

mkdir name_folder #создать папку
cd name_folder #перейти в папку
ls #посмотреть что в папке
rm -r name_folder #удалить папку
rm name_file #удалить файл

touch name_file #создать файл
echo "text" > name_file #записать текст в файл
cat name_file #прочитать файл



