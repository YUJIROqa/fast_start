from selenium import webdriver # импортируем библиотеку selenium
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options() # создаем объект опций. Options() - это класс, который отвечает за настройки браузера.

#options.add_argument('start-maximized') # добавляем опцию для максимизации окна браузера

options.add_argument('--window-size=500, 1080') #окно открывается сразу с заданными параметрами

driver = webdriver.Chrome(options=options) # создаем объект драйвера. Webdriver - это класс, который отвечает за управление браузером. 
#Переводчик между браузерным языком и языком программирования. Вместо хром можно использовать любой другой браузер. 

driver.get("https://www.google.com")
# driver.maximize_window() # максимизируем окно браузера
#driver.set_window_size(500, 1080) # устанавливаем размер окна браузера
print(driver.title) # выводим заголовок страницы
print(driver.current_url) # выводим текущий url
sleep(3)

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("cat")
sleep(200)
press_input = driver.find_element(By.LINK_TEXT, "Поиск в Google")
press_input.click()

print('='*100)


#параметрайз короче первое это переменная которую передаем а второе это значения 
#которые эта переменная принимает? так же в переменной могут быть несколько переменных,
# но всегда только 2 объекта? переменная\переменные, и значения к этой\этим переменным
 