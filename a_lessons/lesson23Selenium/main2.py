from selenium import webdriver # импортируем библиотеку selenium
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options) # создаем объект драйвера. Webdriver - это класс, который отвечает за управление браузером. 
    #Переводчик между браузерным языком и языком программирования. Вместо хром можно использовать любой другой браузер. 
    yield chrome_driver


def test_id_name(driver): #внутрь помещаем фикстуру driver
    input_data = 'Hello'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    #text_field = driver.find_element(By.NAME, 'text_string')
    text_field = driver.find_element(By.ID, 'id_text_string')
    text_field.send_keys(input_data)
    text_field.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data

def test_classname(driver):
    input_data = 'Hello'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_field = driver.find_element(By.CLASS_NAME, 'textinput.textInput.form-control') #если несколько классов в атрибуте, то разделяем их точкой
    text_field.send_keys(input_data)
    text_field.submit()
    result_text = driver.find_element(By.CLASS_NAME, 'result-text')
    assert result_text.text == input_data

def test_tagname(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'

def test_link(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
    contact_link.click()
    assert  driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'

def test_css_selector(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_field = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]') #найди элемент с атрибутом placeholder и значением Submit me
    text_field.send_keys('Hello')
    text_field.submit()
    result_text = driver.find_element(By.CSS_SELECTOR, '[class="result-text"]')
    assert result_text.text == 'Hello'
    assert text_field.get_attribute('placeholder') == 'Submit me'

def test_xpath(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_field = driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
    # // - любой уровень вложенности, * - любой тег, @placeholder - атрибут placeholder, Submit me - значение атрибута
    text_field.send_keys('Hello')
    text_field.submit()
    result_text = driver.find_element(By.XPATH, '//*[@class="result-text"]')
    assert result_text.text == 'Hello'
    

# select_state = driver.find_element(By.XPATH, "//*[text()='Select State']")
# #//*[text()='Select State'] - найди элемент с текстом Select State
    