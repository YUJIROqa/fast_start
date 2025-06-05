from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()

def test_hw1(driver): 
    try:
        driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
        assert driver.current_url == 'https://www.qa-practice.com/elements/checkbox/mult_checkbox'
        assert driver.title == 'Checkboxes | Multiple Checkboxes | QA Practice'

        print('Step 1: Перешли на страницу и проверили url и title. Done')
    except Exception as e:
        print(e)

    try:
        checkbox1 = driver.find_element(By.XPATH, '//*[@id="id_checkboxes_0"]')
        checkbox2 = driver.find_element(By.XPATH, '//*[@id="id_checkboxes_1"]')
        checkbox3 = driver.find_element(By.XPATH, '//*[@id="id_checkboxes_2"]')
        submit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')

        print('Step 2: Нашли элементы и кнопку Submit. Done')
    except Exception as e:
        print(e)

    try:
        submit_button_value = submit_button.get_attribute('value')
        if submit_button_value == 'Submit':
            print(submit_button_value)
        else:
            print('Submit button value is not Submit')
        
        print('Step 3: Проверили значение кнопки Submit. Done')
    except Exception as e:
        print(e)

    try:
        checkbox1.click()
        checkbox2.click()
        assert checkbox1.is_selected() == True
        assert checkbox2.is_selected() == True
        assert checkbox3.is_selected() == False

        print('Step 4: Отметили два чекбокса и проверили, их отображение. Done')
    except Exception as e:
        print(e)

    try:
        submit_button.click()
        print('Step 5: Нажали на кнопку Submit. Done')
    except Exception as e:
        print(e)

    try:
        result_text = driver.find_element(By.XPATH, '//*[@class="result-text"]')

        if result_text.text == 'one, two':
            print(result_text.text)
        else:
            print('Result text is not one, two')
        print('Step 6: Проверили результат. Done')
    except Exception as e:
        print(e)


    