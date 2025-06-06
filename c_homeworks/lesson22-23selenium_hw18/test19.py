from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()

def test_practice_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    print(3)
    try:
        first_name = driver.find_element(By.XPATH, '//*[@id="firstName"]')
        print('Найден элемент first_name')
    except Exception as e:
        print(e)

    try:
        last_name = driver.find_element(By.XPATH, '//*[@id="lastName"]')
        print('Найден элемент last_name')
    except Exception as e:
        print(e)

    try:
        email = driver.find_element(By.XPATH, '//*[@pattern="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"]')
        print('Найден элемент email')
    except Exception as e:
        print(e)

    try:
        male = driver.find_element(By.XPATH, '//*[@for="gender-radio-1"]')
        print('Найден элемент male')
    except Exception as e:
        print(e)

    try:
        female = driver.find_element(By.XPATH, '//*[@for="gender-radio-2"]')
        print('Найден элемент female')
    except Exception as e:
        print(e)

    try:
        other = driver.find_element(By.XPATH, '//*[@for="gender-radio-3"]')
        print('Найден элемент other')
    except Exception as e:
        print(e)

    try:
        mobile = driver.find_element(By.ID, 'userNumber')
        print('Найден элемент mobile')
    except Exception as e:
        print(e)

    try:
        date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
        print('Найден элемент date_of_birth')
    except Exception as e:
        print(e)

    try:
        subjects = driver.find_element(By.CSS_SELECTOR, '#subjectsContainer input')
        print('Найден элемент subjects')
    except Exception as e:
        print(e)

    try:
        hobbi_sport = driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-1"]')
        print('Найден элемент hobbi_sport')
    except Exception as e:
        print(e)

    try:
        hobbi_reading = driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-2"]')
        print('Найден элемент hobbi_reading')
    except Exception as e:
        print(e)

    try:
        hobbi_music = driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-3"]')
        print('Найден элемент hobbi_music')
    except Exception as e:
        print(e)

    try:
        picture_choose_file = driver.find_element(By.ID, 'uploadPicture')
        print('Найден элемент picture_choose_file')
    except Exception as e:
        print(e)

    try:
        current_adress = driver.find_element(By.XPATH, '//*[@placeholder="Current Address"]')
        print('Найден элемент current_adress')
    except Exception as e:
        print(e)

    try:
        state_selector = driver.find_element(By.XPATH, '//*[text()="Select State"]')
        print('Найден элемент state_selector')
    except Exception as e:
        print(e)

    try:
        city_selector = driver.find_element(By.XPATH, '//*[text()="Select City"]')
        print('Найден элемент city_selector')
    except Exception as e:
        print(e)

    try:
        submit_button = driver.find_element(By.ID, 'submit')
        print('Найден элемент submit_button')
    except Exception as e:
        print(e)

    try:
        first_name.send_keys('Egor')
        last_name.send_keys('Kravchenko')
        email.send_keys('egor@gmail.com')
        female.click()
        mobile.send_keys('1234567890')
        print('Введены данные полей: first_name, last_name, email, female, mobile')
    except Exception as e:
        print(e)

    try:
        date_of_birth.click()
        selector_month = driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]')
        dropdown_month = Select(selector_month)
        dropdown_month.select_by_value('6')
        print('Выбран месяц')
        sleep(3)
    except Exception as e:
        print(e)

    try:
        selector_year = driver.find_element(By.XPATH, '//*[@class="react-datepicker__year-select"]')
        dropdown_year = Select(selector_year)
        dropdown_year.select_by_value('1990')
        print('Выбран год')
        sleep(3)
    except Exception as e:
        print(e)

    try:
        selector_day = driver.find_element(By.XPATH, '//*[@class="react-datepicker__day react-datepicker__day--026"]')
        day = driver.find_element(By.XPATH, '//*[text()="3"]')
        day.click()
        print('Выбран день')
        sleep(3)
    except Exception as e:
        print(e)

    try:
        subjects.send_keys('Math')
        subjects.send_keys(Keys.ENTER)
        hobbi_sport.click()
        hobbi_reading.click()
        hobbi_music.click()
        sleep(1)
        picture_choose_file.send_keys('/home/egor/Documents/ЖБ.docx')
        current_adress.send_keys('Moscow')
        sleep(1)
    except Exception as e:
        print(e)

    try:
                # Просто кликни по полю State
        state = driver.find_element(By.ID, "state")
        state.click()

        # Кликни по любой опции (первой попавшейся)
        option = driver.find_element(By.XPATH, "//div[text()='NCR']")
        option.click()
        print('Выбран штат')
    except Exception as e:
        print(e)

    try:    
            # Подожди секунду
        sleep(1)

        # Кликни по полю City  
        city = driver.find_element(By.ID, "city")
        city.click()

        # Кликни по любой опции
        option = driver.find_element(By.XPATH, "//div[text()='Delhi']")
        option.click()
        print('Выбран город')
    except Exception as e:
        print(e)

    try:
        submit_button.click()
    except Exception as e:
        print(e)
