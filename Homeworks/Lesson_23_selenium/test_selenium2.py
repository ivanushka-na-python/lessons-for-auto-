from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep
"""селениум выкидывает найденные элементы, если сессия страницы перезагружена/умерла"""



@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1440,900')
    driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()


"""заходим на страницу, ищем и нажимаем на вкладку на сайте, переходим на новую страницу и там ищем что кнопка доступна"""
@pytest.mark.Tab
def test_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    # find_tab = driver.find_element(By.CLASS_NAME, 'tab')
    driver.find_element(By.LINK_TEXT, 'New tab button').click()
    result = driver.find_element(By.ID, 'new-page-button')
    assert result.is_enabled()


"""заходим на страницу, кликаем на ссылку, открывается новая вкладка, переходим туда, сверяем результат, потом закрываем
вкладку, переключаемся на первую вкладку, там жмем на вкладку на сайте и сверяем что кнопка доступна"""
@pytest.mark.Test_new_tab_window
def test_new_tab_window(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(windows[0])
    driver.find_element(By.LINK_TEXT, 'New tab button').click()
    assert driver.find_element(By.ID, 'new-page-button').is_displayed()


"""заходим на страницу, находим айфрейм (страницу в странице), тыкаем на меню-бургер в айфрейме и потом возвращаемся на 
основную страницу и на ней сверяем h1"""
def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.CLASS_NAME, 'embed-responsive-item')
    driver.switch_to.frame(iframe)
    burger_menu = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
    burger_menu.click()
    driver.switch_to.default_content()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Iframes'


"""заходим на страницу, находим надпись у чек-бокса, кликаем на нее, потом находим кнопку, кликаем на кнопку, 
потом сверяем ui состояние прожатой кнопки"""
def test_stale_exception(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.CLASS_NAME, 'form-check-label')
    checkbox.click()
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    assert driver.find_element(By.ID, 'result-text').text == 'select me or not'
    """селениум выкидывает найденные элементы, если сессия страницы перезагружена/умерла"""
    checkbox.click()
    submit_button.click()


"""СПРОСИТЬ У ДИМЫ. скролим страницу сначала, потом наводимся мышкой всплывающий меню-бургер, потом жмем на одну из ссылок и сверяем, 
что h2 открытой страницы такой, который нам нужен"""
def test_drop_down_menu(driver):
    driver.get('https://neon-night.ru/')
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollBy(0, 400);")
    menu_burger = driver.find_element(By.CLASS_NAME, 'index-module-scss-module__NzBddW__menuButton')
    project_link = driver.find_element(By.LINK_TEXT, 'Проекты')
    """в одну строку это работает"""
    ActionChains(driver).move_to_element(menu_burger).move_to_element(project_link).click().perform()
    sleep(3)
    """вариант как написать в несколько строк кода наведение курсора, в несколько строк не работает, не успевает
    страница загрузится"""
    # actions = ActionChains(driver)
    # actions.move_to_element(menu_burger)
    # actions.click(project_link)
    # actions.perform()
    # sleep(4)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'page-content-module-scss-module__nqAzHG__pageTitle')))
    assert driver.find_element(By.TAG_NAME, 'h2').text == 'ПРОЕКТЫ, РЕАЛИЗОВАННЫЕ С ИСПОЛЬЗОВАНИЕМ ПРОДУКЦИИ NEON-⁠NIGHT'


"""перетаскивали один элемент в другой"""
def test_drag_and_drop(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_box = driver.find_element(By.ID, 'rect-draggable')
    drop_box = driver.find_element(By.ID, 'rect-droppable')
    """готовое решение перетягивать элементы"""
    # ActionChains(driver).drag_and_drop(drag_box, drop_box).perform()
    """своя реализаця перетягивания"""
    ActionChains(driver).click_and_hold(drag_box).move_to_element(drop_box).release().perform()
    assert driver.find_element(By.ID, 'text-droppable').text == 'Dropped!'


"""открытие новой вкладки через ActionsChains и кнопки с клавы, потом переключаемся на открытую вкладку и там 
ищем h1 с текстом hello"""
def test_open_in_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Hello!'


"""тыкаем на браузерный алерт, заходим на страницу, тыкаем на кнопку, вылезает алерт, ему скармливаем драйвер, 
и через встроенный метод жмем на кнопку принять"""
def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    alert = Alert(driver)
    alert.accept()
