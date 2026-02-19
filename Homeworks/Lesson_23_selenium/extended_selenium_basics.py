from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



"""предусловия и постусловия настройки сессии браузера"""
@pytest.fixture()
def chrome_driver():
    options = Options()
    options.add_argument('--window-size=1440,900')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10) # неявное ожидание до момента когда появится сам элемент (не факт что успеет появится начинка элемента)
    yield driver
    driver.quit()

"""два теста в одном, не имеет смысла думать как об одном целостном тесте"""
def test_clear(chrome_driver):
    chrome_driver.get('https://www.qa-practice.com/elements/input/simple')
    input_field = chrome_driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
    input_field.send_keys('123123')
    # input_field.clear()
    for _ in range(20):
        input_field.send_keys(Keys.BACKSPACE)
    input_field.send_keys(Keys.ENTER)
    result_text = chrome_driver.find_element(By.ID, 'result-text')
    assert result_text.text == '123123'


def test_something(chrome_driver):
    chrome_driver.get('https://www.qa-practice.com/elements/input/simple')
    input_field = chrome_driver.find_element(By.ID, 'id_text_string')
    input_field.send_keys('123123')
    input_field.send_keys(Keys.ENTER)
    assert input_field.is_displayed() # элемент отображается

"""тыкам на выдающий список отрисованный браузером и потом нажимаем на кнопку, которая изначально была не активна"""
def test_enable(chrome_driver):
    chrome_driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = chrome_driver.find_element(By.ID, 'submit-id-submit')
    print(button.is_enabled())
    select_menu = chrome_driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select_menu)
    dropdown.select_by_value('enabled')
    print(button.is_enabled())
    print(chrome_driver.get_cookies())

"""кароч тут ждем до момента с явным ожиданием когда появится значение в элементе"""
def test_cart(chrome_driver):
    chrome_driver.get('https://www.qa-practice.com/elements/button/cart')
    WebDriverWait(chrome_driver, 10).until(EC.text_to_be_present_in_element_attribute())

'''достаем первый элемент и последний элемент карточки товара с листинга'''
def test_same_element(chrome_driver):
    chrome_driver.get('https://www.sds-group.ru/catalog/instrument/')
    find_element = chrome_driver.find_elements(By.CLASS_NAME, 'catalog-tile_body__HPX5F')
    print(find_element[0].text)
    print(find_element[-1].text)

'''достаем вложенный элемент (цена) из первой карточки'''
def test_find_one_element_in_element(chrome_driver):
    chrome_driver.get('https://www.sds-group.ru/catalog/instrument/')
    find_element = chrome_driver.find_elements(By.CLASS_NAME, 'catalog-tile_body__HPX5F')
    print(find_element[0].find_element(By.CLASS_NAME, 'catalog-tile_price__6PVHr').text)# внутри элемента ищем вложенный элемент

'''достаем все вложенные элементы (цены) из карточек товара и суем в список'''
my_list = []
def test_find_many_element_in_element(chrome_driver):
    chrome_driver.get('https://www.sds-group.ru/catalog/instrument/')
    find_elements = chrome_driver.find_elements(By.CLASS_NAME, 'catalog-tile_body__HPX5F')
    for price in find_elements:
        my_list.append(price.find_element(By.CLASS_NAME, 'catalog-tile_price__6PVHr').text)
    print(my_list)


