from selenium import webdriver # импортируем библиотеку selenium
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10) #жди появления элемента максимум 10 секунд(если появится раньше, то сразу продолжить)
    yield chrome_driver
    

def test_clear(driver):
    input_data = 'Hello'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_field = driver.find_element(By.NAME, 'text_string')
    text_field.send_keys(input_data)
    #text_field.clear()
    for i in range(len(input_data)):
        text_field.send_keys(Keys.BACK_SPACE)

    assert text_field.get_attribute('value') == ''

def test_enabled_and_selected(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.NAME, 'submit')
    print(button.is_enabled())
    selector = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(selector)
    dropdown.select_by_value('enabled')
    print(button.is_enabled())
    sleep(2)
    
@pytest.mark.skip(reason='Skipping test')
def test_welcome(driver):
    welcome_massage = driver.find_element(By.CSS_SELECTOR, 'li.welcome.greet') #найди элемент с классом welcome и greet
    assert welcome_massage.text == 'Clock "Write for us" link in the footer to submit a guest post'

@pytest.mark.skip(reason='Skipping test')
def test_5_sec(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'visibleAfter'))) #ждем 5 секунд пока элемент с id visibleAfter станет кликабельным
    visible_after = driver.find_element(By.ID, 'visibleAfter')
    visible_after.click()
    driver.add_cookie({'name': 'test', 'value': 'test'})
    print(driver.get_cookies())
    

def test_same_elements(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    sleep(3)
    product_link = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    print(product_link[0].text)




