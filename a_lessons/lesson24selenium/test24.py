from selenium import webdriver # импортируем библиотеку selenium
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver

def test_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles #получаем список всех вкладок
    driver.switch_to.window(tabs[1]) #переходим на вторую вкладку(0 - основная и первая вкладка, 1 - вторая вкладка)
    sleep(3)
    result_text = driver.find_element(By.ID, 'result-text').text
    assert result_text == 'I am a new page in a new tab'
    sleep(3)
    driver.close() #закрываем вторую вкладку
    driver.switch_to.window(tabs[0]) #переходим на первую вкладку
    sleep(3)
    
def test_stale_exception(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()

    assert driver.find_element(By.ID, 'result-text').text == 'select me or not'

    checkbox.click()
    submit_button.click()

    checkbox = driver.find_element(By.ID, 'id_checkbox_0')#повторяем тк при переходе на новую страницу, селениум забывает
    #что мы уже находили элементы
    checkbox.click()
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    
def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    burger_menu = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
    burger_menu.click()
    sleep(3) 
    driver.switch_to.default_content()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'Iframe').click()
    

def test_drop_menu(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')

    #ActionChains(driver).move_to_element(women).move_to_element(tops).click(jackets).perform()#perform - выполняет все действия
    actions = ActionChains(driver)

    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()

    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Jackets'


def test_drag_and_drop(driver):
    driver.get('https://qa-practice.com/elements/drandrop/boxes')
    source = driver.find_element(By.ID, 'rect-draggable')
    target = driver.find_element(By.ID, 'rect-droppable')
    #ActionChains(driver).drag_and_drop(source, target).perform()
    actions = ActionChains(driver) #создаем объект actions для работы с элементами
    actions.click_and_hold(source) #нажимаем и держим
    actions.move_to_element(target) #перемещаем на target
    actions.release() #отпускаем
    actions.perform() #выполняем все действия

     
def test_open_in_new_tab(driver):
    driver.get('https://qa-practice.com')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
     #нажимаем ctrl и кликаем по ссылке, затем отпускаем ctrl
    
def test_alert(driver):
    driver.get('https://qa-practice.com/elements/alert/alert')
    driver.find_element(By.CLASS_NAME, 'a-button').click() #кликаем по кнопке
    alert = Alert(driver) #создаем объект alert для работы с алертами
    alert.accept() #нажимаем на кнопку ок
    sleep(3)

