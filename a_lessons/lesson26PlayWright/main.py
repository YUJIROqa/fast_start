import playwright
from playwright.sync_api import Page, expect
import re
from time import sleep

def test_first_cat(page: Page): #page - это объект страницы. Как driver в selenium
    page.goto("https://www.google.com")
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')

    expect(page).to_have_title(re.compile('^cat')) #ПРОВЕРЯЕМ ЧТО У СТРАНИЦЫ ЕСТЬ ТАЙТЛ КОТОРЫЙ (^) НАЧИНАЕТСЯ СО СЛОВА CAT

    sleep(3)

def test_by_role(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.get_by_role('menuitem', name="What's New").click() #поиск по роли у которой есть такой name
    sleep(3)
    page.get_by_role('link', name='Search Terms').click()
    sleep(3)

def test_by_text(page: Page):
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Single UI Elements').click()
    
    
def test_by_label(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    field = page.get_by_label('Text string')
    field.press_sequentially('Hello', delay=100)
    sleep(3)
    field.press('Control+A')
    sleep(1)
    field.press('Backspace')
    
def test_by_placeholder(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_placeholder('Submit me').fill('Hello')
    sleep(3)
    
def test_by_title(page: Page):
    page.goto('https://www.google.com')
    page.get_by_title('поиск').fill('cat')
    sleep(3)

def test_by_test_id(page: Page):
    page.goto('https://www.airbub.com/')
    sleep(2)
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
    sleep(2)

def test_by_css_selector(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('.showcart').click()
    sleep(2)

def test_by_xpath(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('//*[@class="action showcart"]')
    sleep(2)
    

    
    